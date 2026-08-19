#!/usr/bin/env python3
"""Convert the stable Tsuyokiss JSONL extraction into per-scene Codex sources."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def canonical_scene(label: str) -> str:
    return label.split("//", 1)[0].strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("messages", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()

    scenes: dict[str, list[dict]] = defaultdict(list)
    labels: dict[str, str] = {}
    with args.messages.open(encoding="utf-8") as source:
        for raw in source:
            if not raw.strip():
                continue
            record = json.loads(raw)
            scene = canonical_scene(str(record["scene"]))
            previous = labels.setdefault(scene, str(record["scene"]))
            if canonical_scene(previous) != scene:
                raise ValueError(f"scene collision for {scene}")
            scenes[scene].append(
                {
                    "index": str(record["ordinal"]),
                    "engine_id": record["id"],
                    "speaker": record.get("speaker"),
                    "kind": record["kind"],
                    "japanese": record["source"],
                    "source_sha256": record["source_sha256"],
                }
            )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for scene, rows in scenes.items():
        indexes = [row["index"] for row in rows]
        if len(indexes) != len(set(indexes)):
            raise ValueError(f"duplicate indexes in {scene}")
        document = {
            "scene": scene,
            "source_label": labels[scene],
            "rows": rows,
        }
        (args.output_dir / f"{scene}.json").write_text(
            json.dumps(document, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(f"scenes={len(scenes)} output={args.output_dir}")


if __name__ == "__main__":
    main()
