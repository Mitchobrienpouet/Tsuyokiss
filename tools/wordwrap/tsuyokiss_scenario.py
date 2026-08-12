#!/usr/bin/env python3
"""Extract/apply stable translation records from decoded Tsuyokiss scenarios.

This deliberately stops at decoded ZLC2 members. Rebuilding data.fpk is a
separate archive-integrity step; emitting a superficially valid but corrupt FPK
is forbidden.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path


SPEAKER_RE = re.compile(r"^(.+?)　（[０-９0-9]+）")
COMMAND_RE = re.compile(r"^(?:\*\*\*|EF_|CG_|BG_|SE_|KM_|//|#)")


@dataclass(frozen=True)
class Record:
    id: str
    block: int
    start: int
    end: int
    scene: str
    ordinal: int
    kind: str
    speaker: str | None
    source: str


def is_text_start(lines: list[str], i: int) -> tuple[str, str | None] | None:
    line = lines[i]
    if not line or COMMAND_RE.match(line):
        return None
    if line.startswith("「"):
        speaker = None
        if i and (match := SPEAKER_RE.match(lines[i - 1])):
            speaker = match.group(1)
        return "dialogue", speaker
    if line.startswith("　") and line.strip():
        return "narration", None
    return None


def records_for(block: int, data: bytes) -> tuple[list[str], list[Record]]:
    text = data.decode("cp932")
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    records: list[Record] = []
    scene = "UNSCOPED"
    ordinal = 0
    i = 0
    while i < len(lines):
        if lines[i].startswith("***"):
            scene = lines[i].split("\t", 1)[0].lstrip("*")
            ordinal = 0
            i += 1
            continue
        found = is_text_start(lines, i) if scene.startswith("SC_") else None
        if not found:
            i += 1
            continue
        kind, speaker = found
        start = i
        i += 1
        while i < len(lines) and lines[i] and not COMMAND_RE.match(lines[i]):
            # A second independently indented narration begins a new record.
            if kind == "narration" and lines[i].startswith("　"):
                break
            i += 1
        end = i
        source = " ".join(part.lstrip("　") for part in lines[start:end]).strip()
        ordinal += 1
        rid = f"B{block:04d}:{scene}:{ordinal:04d}"
        records.append(Record(rid, block, start, end, scene, ordinal, kind, speaker, source))
    return lines, records


def extract(blocks_dir: Path, output: Path) -> None:
    count = 0
    with output.open("w", encoding="utf-8", newline="\n") as dst:
        for path in sorted(blocks_dir.glob("[0-9][0-9][0-9][0-9].bin")):
            block = int(path.stem)
            if not 28 <= block <= 40:
                continue
            _, records = records_for(block, path.read_bytes())
            for rec in records:
                row = rec.__dict__ | {
                    "text": "",
                    "source_sha256": hashlib.sha256(rec.source.encode("utf-8")).hexdigest(),
                }
                dst.write(json.dumps(row, ensure_ascii=False) + "\n")
                count += 1
    print(f"extracted={count} output={output}")


def apply(blocks_dir: Path, wrapped_jsonl: Path, output_dir: Path) -> None:
    translations: dict[str, dict] = {}
    for raw in wrapped_jsonl.read_text(encoding="utf-8").splitlines():
        if raw.strip():
            row = json.loads(raw)
            if row.get("status") != "ok":
                raise ValueError(f"record {row.get('id')} did not pass wrapping")
            translations[row["id"]] = row
    output_dir.mkdir(parents=True, exist_ok=True)
    applied = 0
    for path in sorted(blocks_dir.glob("[0-9][0-9][0-9][0-9].bin")):
        block = int(path.stem)
        if not 28 <= block <= 40:
            continue
        lines, records = records_for(block, path.read_bytes())
        for rec in reversed(records):
            row = translations.get(rec.id)
            if not row or not row.get("text"):
                continue
            expected = hashlib.sha256(rec.source.encode("utf-8")).hexdigest()
            if row.get("source_sha256") != expected:
                raise ValueError(f"stale source mapping for {rec.id}")
            replacement = str(row["wrapped"]).replace("\r\n", "\n").split("\n")
            if rec.kind == "narration":
                replacement[0] = "　" + replacement[0]
            lines[rec.start:rec.end] = replacement
            applied += 1
        encoded = "\r\n".join(lines).encode("cp932", errors="strict")
        (output_dir / path.name).write_bytes(encoded)
    print(f"applied={applied} output_dir={output_dir}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    ex = sub.add_parser("extract")
    ex.add_argument("blocks_dir", type=Path)
    ex.add_argument("output", type=Path)
    ins = sub.add_parser("apply")
    ins.add_argument("blocks_dir", type=Path)
    ins.add_argument("wrapped_jsonl", type=Path)
    ins.add_argument("output_dir", type=Path)
    args = ap.parse_args()
    if args.command == "extract":
        extract(args.blocks_dir, args.output)
    else:
        apply(args.blocks_dir, args.wrapped_jsonl, args.output_dir)


if __name__ == "__main__":
    main()
