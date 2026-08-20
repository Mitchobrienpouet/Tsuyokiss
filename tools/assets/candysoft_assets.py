#!/usr/bin/env python3
"""Extract CandySoft FPK members and convert GCGK images losslessly.

The Full Edition archives use an encrypted tail index. Individual members may
be wrapped in one or more ZLC2 layers. GCGK (``.kg``) images are row-RLE RGBA
bitmaps. This tool keeps the original engine-facing member names and provides
pixel-exact PNG round-trip checks before localized assets are repacked.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mmap
import os
import struct
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

from PIL import Image


@dataclass(frozen=True)
class Entry:
    index: int
    name: str
    offset: int
    size: int


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_entries(source: bytes | mmap.mmap) -> list[Entry]:
    if len(source) < 16:
        raise ValueError("FPK is too short")
    raw_count = struct.unpack_from("<i", source, 0)[0]
    if raw_count >= 0:
        raise ValueError("only the encrypted-index CandySoft FPK variant is supported")
    count = raw_count & 0x7FFFFFFF
    index_offset = struct.unpack_from("<I", source, len(source) - 4)[0]
    key = bytes(source[len(source) - 8 : len(source) - 4])
    record_size = 36
    index_size = count * record_size
    if index_offset < 4 or index_offset + index_size > len(source) - 8:
        raise ValueError("invalid encrypted FPK index placement")
    encrypted = source[index_offset : index_offset + index_size]
    index = bytes(value ^ key[pos & 3] for pos, value in enumerate(encrypted))
    entries: list[Entry] = []
    for number in range(count):
        pos = number * record_size
        offset, size = struct.unpack_from("<II", index, pos)
        raw_name = index[pos + 8 : pos + 32].split(b"\0", 1)[0]
        name = raw_name.decode("cp932", errors="strict")
        if not name or Path(name).name != name:
            raise ValueError(f"unsafe or empty member name at index {number}: {name!r}")
        if offset < 4 or offset + size > len(source):
            raise ValueError(f"member outside archive: {name}")
        entries.append(Entry(number, name, offset, size))
    return entries


def decode_zlc2(data: bytes) -> bytes:
    if data[:4] != b"ZLC2" or len(data) < 8:
        raise ValueError("not a ZLC2 member")
    expected = struct.unpack_from("<I", data, 4)[0]
    src = 8
    output = bytearray(0x1000)
    base = len(output)
    while len(output) - base < expected:
        if src >= len(data):
            raise EOFError("truncated ZLC2 flags")
        flags = data[src]
        src += 1
        for bit in range(7, -1, -1):
            if len(output) - base >= expected:
                break
            if flags & (1 << bit):
                if src + 2 > len(data):
                    raise EOFError("truncated ZLC2 back-reference")
                lo, hi = data[src], data[src + 1]
                src += 2
                distance = lo | ((hi & 0xF0) << 4)
                distance = distance or 0x1000
                count = (hi & 0x0F) + 3
                if distance > len(output):
                    raise ValueError("invalid ZLC2 distance")
                for _ in range(count):
                    if len(output) - base >= expected:
                        break
                    output.append(output[-distance])
            else:
                if src >= len(data):
                    raise EOFError("truncated ZLC2 literal")
                output.append(data[src])
                src += 1
    return bytes(output[base : base + expected])


def encode_zlc2(data: bytes) -> bytes:
    """Encode one CandySoft ZLC2 member with a bounded 4 KiB window."""
    chains: dict[bytes, deque[int]] = defaultdict(deque)
    payload = bytearray()
    pos = 0
    while pos < len(data):
        flag_at = len(payload)
        payload.append(0)
        flags = 0
        for bit in range(7, -1, -1):
            if pos >= len(data):
                break
            best_length = 0
            best_distance = 0
            if pos + 3 <= len(data):
                key = data[pos : pos + 3]
                chain = chains[key]
                while chain and pos - chain[0] > 0x1000:
                    chain.popleft()
                for candidate in reversed(chain):
                    distance = pos - candidate
                    length = 3
                    maximum = min(18, len(data) - pos)
                    while length < maximum and data[candidate + length] == data[pos + length]:
                        length += 1
                    if length > best_length:
                        best_length, best_distance = length, distance
                        if length == maximum:
                            break
            if best_length >= 3:
                flags |= 1 << bit
                encoded_distance = 0 if best_distance == 0x1000 else best_distance
                payload.append(encoded_distance & 0xFF)
                payload.append(((encoded_distance >> 4) & 0xF0) | (best_length - 3))
                advance = best_length
            else:
                payload.append(data[pos])
                advance = 1
            for at in range(pos, pos + advance):
                if at + 3 <= len(data):
                    queue = chains[data[at : at + 3]]
                    queue.append(at)
                    if len(queue) > 1024:
                        queue.popleft()
            pos += advance
        payload[flag_at] = flags
    return b"ZLC2" + len(data).to_bytes(4, "little") + payload


def unwrap_member(data: bytes) -> tuple[bytes, int]:
    layers = 0
    while data[:4] == b"ZLC2":
        data = decode_zlc2(data)
        layers += 1
    return data, layers


def kg_to_image(data: bytes) -> Image.Image:
    if len(data) < 12 or data[:4] != b"GCGK":
        raise ValueError("not a GCGK image")
    width, height, packed_size = struct.unpack_from("<HHi", data, 4)
    if not width or not height or packed_size <= 0:
        raise ValueError("invalid GCGK dimensions or packed size")
    table_end = 12 + height * 4
    if table_end + packed_size > len(data):
        raise ValueError("truncated GCGK payload")
    offsets = struct.unpack_from(f"<{height}I", data, 12)
    pixels = bytearray(width * height * 4)
    for y, row_offset in enumerate(offsets):
        src = table_end + row_offset
        x = 0
        while x < width:
            if src + 2 > len(data):
                raise EOFError(f"truncated GCGK row {y}")
            alpha, count = data[src], data[src + 1]
            src += 2
            count = count or 256
            if x + count > width:
                raise ValueError(f"GCGK run exceeds row {y}")
            dst = (y * width + x) * 4
            if alpha:
                need = count * 3
                if src + need > len(data):
                    raise EOFError(f"truncated GCGK RGB run in row {y}")
                for _ in range(count):
                    pixels[dst : dst + 4] = data[src : src + 3] + bytes((alpha,))
                    src += 3
                    dst += 4
            x += count
    return Image.frombytes("RGBA", (width, height), bytes(pixels))


def image_to_kg(image: Image.Image) -> bytes:
    rgba = image.convert("RGBA")
    width, height = rgba.size
    if not 0 < width <= 0xFFFF or not 0 < height <= 0xFFFF:
        raise ValueError("GCGK dimensions must fit unsigned 16-bit fields")
    raw = rgba.tobytes()
    offsets: list[int] = []
    payload = bytearray()
    for y in range(height):
        offsets.append(len(payload))
        x = 0
        while x < width:
            alpha = raw[(y * width + x) * 4 + 3]
            run = 1
            while run < 256 and x + run < width:
                next_alpha = raw[(y * width + x + run) * 4 + 3]
                if next_alpha != alpha:
                    break
                run += 1
            payload.extend((alpha, 0 if run == 256 else run))
            if alpha:
                for at in range(x, x + run):
                    pos = (y * width + at) * 4
                    payload.extend(raw[pos : pos + 3])
            x += run
    header = b"GCGK" + struct.pack("<HHi", width, height, len(payload))
    table = struct.pack(f"<{height}I", *offsets)
    return header + table + payload


def extract_archive(source_path: Path, output: Path, names: set[str]) -> None:
    output.mkdir(parents=True, exist_ok=True)
    manifest = []
    with source_path.open("rb") as fp, mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ) as source:
        entries = read_entries(source)
        for entry in entries:
            if names and entry.name.lower() not in names:
                continue
            packed = bytes(source[entry.offset : entry.offset + entry.size])
            unpacked, layers = unwrap_member(packed)
            target = output / entry.name
            temp = target.with_suffix(target.suffix + ".partial")
            temp.write_bytes(unpacked)
            os.replace(temp, target)
            manifest.append(
                {
                    "index": entry.index,
                    "name": entry.name,
                    "offset": entry.offset,
                    "packed_size": entry.size,
                    "zlc2_layers": layers,
                    "unpacked_size": len(unpacked),
                    "packed_sha256": sha256(packed),
                    "unpacked_sha256": sha256(unpacked),
                    "signature": unpacked[:8].hex(),
                }
            )
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"archive={source_path.name} extracted={len(manifest)} output={output}")


def list_archive(source_path: Path) -> None:
    with source_path.open("rb") as fp, mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ) as source:
        for entry in read_entries(source):
            print(f"{entry.index:05d}\t{entry.offset:010d}\t{entry.size:010d}\t{entry.name}")


def decode_kg(source: Path, output: Path) -> None:
    image = kg_to_image(source.read_bytes())
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, format="PNG", optimize=False)
    print(f"decoded={source} size={image.width}x{image.height} output={output}")


def decode_directory(source: Path, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    converted = 0
    for path in sorted(source.iterdir(), key=lambda item: item.name.lower()):
        if not path.is_file() or path.name == "manifest.json":
            continue
        data = path.read_bytes()
        if data[:4] == b"GCGK":
            image = kg_to_image(data)
        elif data[:2] == b"BM":
            with Image.open(path) as opened:
                image = opened.convert("RGBA")
        else:
            continue
        image.save(output / f"{path.name}.png", format="PNG", optimize=False)
        converted += 1
    print(f"decoded={converted} source={source} output={output}")


def encode_kg(source: Path, output: Path) -> None:
    with Image.open(source) as image:
        encoded = image_to_kg(image)
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_suffix(output.suffix + ".partial")
    temp.write_bytes(encoded)
    os.replace(temp, output)
    print(f"encoded={source} bytes={len(encoded)} output={output}")


def pack_zlc2(source: Path, output: Path, slot_size: int | None) -> None:
    raw = source.read_bytes()
    packed = encode_zlc2(raw)
    if decode_zlc2(packed) != raw:
        raise AssertionError("ZLC2 encoder round-trip failed")
    if slot_size is not None:
        if len(packed) > slot_size:
            raise ValueError(f"ZLC2 payload {len(packed)} exceeds slot {slot_size}")
        packed += bytes(slot_size - len(packed))
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_suffix(output.suffix + ".partial")
    temp.write_bytes(packed)
    os.replace(temp, output)
    print(f"packed={source} bytes={len(packed)} slot={slot_size} output={output}")


def replace_archive_member(
    source_path: Path,
    output: Path,
    member_name: str,
    replacement_path: Path,
) -> None:
    """Rebuild an encrypted-index FPK with one already-packed member replaced."""
    source = source_path.read_bytes()
    entries = read_entries(source)
    index_offset = struct.unpack_from("<I", source, len(source) - 4)[0]
    key = source[len(source) - 8 : len(source) - 4]
    index_size = len(entries) * 36
    encrypted_index = source[index_offset : index_offset + index_size]
    index = bytearray(value ^ key[pos & 3] for pos, value in enumerate(encrypted_index))
    matches = [entry for entry in entries if entry.name.casefold() == member_name.casefold()]
    if len(matches) != 1:
        raise ValueError(f"expected one FPK member named {member_name!r}, found {len(matches)}")
    replacement = replacement_path.read_bytes()
    if not replacement:
        raise ValueError("replacement payload is empty")

    first_offset = min(entry.offset for entry in entries)
    rebuilt = bytearray(source[:first_offset])
    previous_end = first_offset
    replaced = False
    for entry in sorted(entries, key=lambda item: item.offset):
        if entry.offset < previous_end:
            raise ValueError(f"overlapping FPK members near {entry.name}")
        rebuilt.extend(source[previous_end : entry.offset])
        new_offset = len(rebuilt)
        if entry.name.casefold() == member_name.casefold():
            payload = replacement
            replaced = True
        else:
            payload = source[entry.offset : entry.offset + entry.size]
        rebuilt.extend(payload)
        struct.pack_into("<II", index, entry.index * 36, new_offset, len(payload))
        previous_end = entry.offset + entry.size
    if not replaced:
        raise AssertionError("replacement disappeared during archive rebuild")
    rebuilt.extend(source[previous_end:index_offset])
    new_index_offset = len(rebuilt)
    rebuilt.extend(value ^ key[pos & 3] for pos, value in enumerate(index))
    rebuilt.extend(source[index_offset + index_size : len(source) - 8])
    rebuilt.extend(key)
    rebuilt.extend(struct.pack("<I", new_index_offset))

    reparsed = read_entries(rebuilt)
    expected = [
        (item.name, len(replacement) if item.name.casefold() == member_name.casefold() else item.size)
        for item in entries
    ]
    if [(item.name, item.size) for item in reparsed] != expected:
        raise AssertionError("rebuilt FPK index validation failed")
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_suffix(output.suffix + ".partial")
    temp.write_bytes(rebuilt)
    os.replace(temp, output)
    print(
        f"rebuilt={source_path} member={member_name} replacement={len(replacement)} "
        f"bytes={len(rebuilt)} output={output}"
    )


def verify_roundtrip(source: Path) -> None:
    original = kg_to_image(source.read_bytes())
    encoded = image_to_kg(original)
    restored = kg_to_image(encoded)
    if original.size != restored.size or original.tobytes() != restored.tobytes():
        raise AssertionError(f"pixel round-trip mismatch: {source}")
    print(
        f"PASS source={source} size={original.width}x{original.height} "
        f"rgba_sha256={sha256(original.tobytes())} encoded_bytes={len(encoded)}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    list_cmd = sub.add_parser("list", help="list encrypted-index FPK members")
    list_cmd.add_argument("archive", type=Path)

    extract_cmd = sub.add_parser("extract", help="extract and unwrap FPK members")
    extract_cmd.add_argument("archive", type=Path)
    extract_cmd.add_argument("output", type=Path)
    extract_cmd.add_argument("--name", action="append", default=[])

    decode_cmd = sub.add_parser("decode-kg", help="convert GCGK to PNG")
    decode_cmd.add_argument("source", type=Path)
    decode_cmd.add_argument("output", type=Path)

    decode_dir_cmd = sub.add_parser("decode-dir", help="convert a raw asset directory to PNG")
    decode_dir_cmd.add_argument("source", type=Path)
    decode_dir_cmd.add_argument("output", type=Path)

    encode_cmd = sub.add_parser("encode-kg", help="convert PNG to GCGK")
    encode_cmd.add_argument("source", type=Path)
    encode_cmd.add_argument("output", type=Path)

    verify_cmd = sub.add_parser("verify-roundtrip", help="prove GCGK pixel round-trip")
    verify_cmd.add_argument("source", type=Path)

    zlc2_cmd = sub.add_parser("pack-zlc2", help="compress a member and optionally pad to its FPK slot")
    zlc2_cmd.add_argument("source", type=Path)
    zlc2_cmd.add_argument("output", type=Path)
    zlc2_cmd.add_argument("--slot-size", type=int)

    replace_cmd = sub.add_parser("replace-member", help="rebuild an FPK with one packed member replaced")
    replace_cmd.add_argument("archive", type=Path)
    replace_cmd.add_argument("member")
    replace_cmd.add_argument("replacement", type=Path)
    replace_cmd.add_argument("output", type=Path)

    args = parser.parse_args()
    if args.command == "list":
        list_archive(args.archive)
    elif args.command == "extract":
        extract_archive(args.archive, args.output, {name.lower() for name in args.name})
    elif args.command == "decode-kg":
        decode_kg(args.source, args.output)
    elif args.command == "decode-dir":
        decode_directory(args.source, args.output)
    elif args.command == "encode-kg":
        encode_kg(args.source, args.output)
    elif args.command == "pack-zlc2":
        pack_zlc2(args.source, args.output, args.slot_size)
    elif args.command == "replace-member":
        replace_archive_member(args.archive, args.output, args.member, args.replacement)
    else:
        verify_roundtrip(args.source)


if __name__ == "__main__":
    main()
