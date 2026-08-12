#!/usr/bin/env python3
"""Decompress CandySoft's concatenated ZLC2 LZSS blocks."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path


def decode_block(data: bytes, pos: int) -> tuple[bytes, int]:
    if data[pos : pos + 4] != b"ZLC2":
        raise ValueError(f"missing ZLC2 marker at {pos:#x}")
    expected = int.from_bytes(data[pos + 4 : pos + 8], "little")
    pos += 8
    stream = bytearray(0x1000)
    base = len(stream)
    while len(stream) - base < expected:
        flags = data[pos]
        pos += 1
        for bit in range(7, -1, -1):
            if len(stream) - base >= expected:
                break
            if flags & (1 << bit):
                lo, hi = data[pos], data[pos + 1]
                pos += 2
                distance = lo | ((hi & 0xF0) << 4)
                if distance == 0:
                    distance = 0x1000
                count = (hi & 0x0F) + 3
                for _ in range(count):
                    stream.append(stream[-distance])
            else:
                stream.append(data[pos])
                pos += 1
    return bytes(stream[base : base + expected]), pos


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--blocks-dir", type=Path)
    args = ap.parse_args()
    source = args.source.read_bytes()
    # FPK begins with a 32-bit archive count/flag word; its payload follows.
    archive_word = int.from_bytes(source[:4], "little")
    pos = 4
    blocks = []
    manifest = []
    while pos < len(source):
        while pos < len(source) and source[pos] == 0:
            pos += 1
        if source[pos : pos + 4] != b"ZLC2":
            break
        source_offset = pos
        block, pos = decode_block(source, pos)
        blocks.append(block)
        manifest.append(
            {
                "index": len(blocks) - 1,
                "source_offset": source_offset,
                "source_end": pos,
                "decoded_size": len(block),
                "sha256": hashlib.sha256(block).hexdigest(),
            }
        )
    temp = args.output.with_suffix(args.output.suffix + ".partial")
    temp.parent.mkdir(parents=True, exist_ok=True)
    with temp.open("wb") as fp:
        for block in blocks:
            fp.write(block)
    os.replace(temp, args.output)
    if args.blocks_dir:
        args.blocks_dir.mkdir(parents=True, exist_ok=True)
        for index, block in enumerate(blocks):
            (args.blocks_dir / f"{index:04d}.bin").write_bytes(block)
        (args.blocks_dir / "trailer.bin").write_bytes(source[pos:])
        (args.blocks_dir / "manifest.json").write_text(
            json.dumps(
                {"archive_word": archive_word, "blocks": manifest, "trailer_offset": pos},
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    print(
        f"archive_word={archive_word:#010x} blocks={len(blocks)} "
        f"size={args.output.stat().st_size} sha256={digest}"
    )


if __name__ == "__main__":
    main()
