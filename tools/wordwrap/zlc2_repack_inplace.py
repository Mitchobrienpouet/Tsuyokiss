#!/usr/bin/env python3
"""Recompress selected ZLC2 members without moving CandySoft FPK offsets."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from collections import defaultdict, deque
from pathlib import Path

from zlc2_decompress import decode_block


def compress_block(data: bytes) -> bytes:
    # Positions keyed by the next three bytes; bounded chains keep this linear
    # enough for the multi-megabyte scenario members.
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
            best_len = 0
            best_dist = 0
            if pos + 3 <= len(data):
                key = data[pos:pos + 3]
                chain = chains[key]
                while chain and pos - chain[0] > 0x1000:
                    chain.popleft()
                for candidate in reversed(chain):
                    distance = pos - candidate
                    length = 3
                    maximum = min(18, len(data) - pos)
                    while length < maximum and data[candidate + length] == data[pos + length]:
                        length += 1
                    if length > best_len:
                        best_len, best_dist = length, distance
                        if length == maximum:
                            break
            if best_len >= 3:
                flags |= 1 << bit
                encoded_dist = 0 if best_dist == 0x1000 else best_dist
                payload.append(encoded_dist & 0xFF)
                payload.append(((encoded_dist >> 4) & 0xF0) | (best_len - 3))
                advance = best_len
            else:
                payload.append(data[pos])
                advance = 1
            for at in range(pos, pos + advance):
                if at + 3 <= len(data):
                    q = chains[data[at:at + 3]]
                    q.append(at)
                    if len(q) > 1024:
                        q.popleft()
            pos += advance
        payload[flag_at] = flags
    return b"ZLC2" + len(data).to_bytes(4, "little") + payload


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("original_fpk", type=Path)
    ap.add_argument("manifest", type=Path)
    ap.add_argument("replacement_blocks", type=Path)
    ap.add_argument("output_fpk", type=Path)
    args = ap.parse_args()
    source = bytearray(args.original_fpk.read_bytes())
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    changed = 0
    for entry in manifest["blocks"]:
        path = args.replacement_blocks / f"{entry['index']:04d}.bin"
        if not path.exists():
            continue
        decoded = path.read_bytes()
        packed = compress_block(decoded)
        start, end = entry["source_offset"], entry["source_end"]
        capacity = end - start
        if len(packed) > capacity:
            raise ValueError(
                f"block {entry['index']:04d}: compressed {len(packed)} > slot {capacity}; "
                "archive index rewrite required"
            )
        check, consumed = decode_block(packed, 0)
        if check != decoded or consumed != len(packed):
            raise AssertionError(f"compressor roundtrip failed for block {entry['index']:04d}")
        source[start:end] = packed + bytes(capacity - len(packed))
        changed += 1
    temp = args.output_fpk.with_suffix(args.output_fpk.suffix + ".partial")
    temp.write_bytes(source)
    os.replace(temp, args.output_fpk)
    print(
        f"changed={changed} size={args.output_fpk.stat().st_size} "
        f"sha256={hashlib.sha256(source).hexdigest()}"
    )


if __name__ == "__main__":
    main()
