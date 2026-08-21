#!/usr/bin/env python3
"""Extract Tsuyokiss wave-200 shards 29-52 into safe per-scene source files.

The stable retail extraction stays local. Raw scene dumps are written immutably
under ``scratchpad/jp_dumps``. Model-visible projections are written under
``scratchpad/model_sources`` only after the canonical exclusion manifest and
all configured fail-closed overlays have been applied.

The command is idempotent. It refuses source drift, missing target scenes,
duplicate indexes, malformed hashes, and any excluded row in a model source.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable, Iterator

REQUIRED_FIELDS = {"scene", "ordinal", "id", "kind", "source", "source_sha256"}


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle, object_pairs_hook=unique_object)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temp = Path(name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def immutable_write(path: Path, value: dict[str, Any]) -> str:
    data = canonical_bytes(value)
    if path.exists():
        if path.read_bytes() != data:
            raise RuntimeError(f"immutable source drift: {path}")
        return "reused"
    atomic_write(path, data)
    return "created"


def replaceable_write(path: Path, value: dict[str, Any]) -> str:
    data = canonical_bytes(value)
    if path.exists() and path.read_bytes() == data:
        return "reused"
    action = "replaced" if path.exists() else "created"
    atomic_write(path, data)
    return action


def canonical_scene(label: str) -> str:
    return label.split("//", 1)[0].strip()


def normalize_index(value: Any) -> str:
    index = str(value)
    if not index:
        raise ValueError("empty source row index")
    return index


def index_key(value: str) -> tuple[int, int | str]:
    return (0, int(value)) if value.isdigit() else (1, value)


def manifest_targets(manifest: dict[str, Any]) -> tuple[list[str], dict[str, int]]:
    shards = manifest.get("shards")
    if not isinstance(shards, list) or not shards:
        raise ValueError("manifest shards must be a non-empty array")
    scenes: list[str] = []
    shard_by_scene: dict[str, int] = {}
    for shard in shards:
        if not isinstance(shard, dict):
            raise ValueError("manifest shard entry must be an object")
        number = int(shard["shard"])
        values = shard.get("scenes")
        if not isinstance(values, list) or not values:
            raise ValueError(f"manifest shard {number} has no scenes")
        for raw_scene in values:
            scene = str(raw_scene)
            if scene in shard_by_scene:
                raise ValueError(f"duplicate target scene: {scene}")
            shard_by_scene[scene] = number
            scenes.append(scene)
    if int(manifest.get("scene_count", len(scenes))) != len(scenes):
        raise ValueError("manifest scene_count does not match shard contents")
    if int(manifest.get("shard_count", len(shards))) != len(shards):
        raise ValueError("manifest shard_count does not match shard contents")
    return scenes, shard_by_scene


def jsonl_records(path: Path) -> Iterator[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, 1):
            if not raw.strip():
                continue
            try:
                value = json.loads(raw, object_pairs_hook=unique_object)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number}: expected an object")
            missing = REQUIRED_FIELDS - set(value)
            if missing:
                raise ValueError(f"{path}:{line_number}: missing {sorted(missing)}")
            yield value


def discover_messages(root: Path) -> Path:
    preferred = [
        root / "translation_template.jsonl",
        root / "scratchpad/project_sources/translation_template.jsonl",
        root / "scratchpad/game_extract/translation_template.jsonl",
        root / "scratchpad/game_media/translation_template.jsonl",
        root / "scratchpad/data_blocks/translation_template.jsonl",
    ]
    for path in preferred:
        if path.is_file():
            return path
    candidates: set[Path] = set()
    for directory in (
        root / "scratchpad/project_sources",
        root / "scratchpad/game_extract",
        root / "scratchpad/game_media",
        root / "scratchpad/data_blocks",
    ):
        if directory.is_dir():
            candidates.update(path.resolve() for path in directory.rglob("*.jsonl"))
    candidates.update(path.resolve() for path in root.glob("*.jsonl"))
    valid: list[Path] = []
    for path in sorted(candidates):
        try:
            first = next(jsonl_records(path), None)
        except (OSError, ValueError):
            continue
        if first is not None:
            valid.append(path)
    if len(valid) != 1:
        detail = ", ".join(str(path) for path in valid) or "none"
        raise FileNotFoundError(
            "unable to select one stable retail extraction JSONL; "
            f"candidates={detail}. Pass --messages explicitly."
        )
    return valid[0]


def validate_row(path: Path, scene: str, row: dict[str, Any]) -> dict[str, Any]:
    required = {"index", "engine_id", "kind", "japanese", "source_sha256"}
    missing = required - set(row)
    if missing:
        raise ValueError(f"{path}: {scene} row missing {sorted(missing)}")
    index = normalize_index(row["index"])
    japanese = str(row["japanese"])
    expected = str(row["source_sha256"]).lower()
    actual = hashlib.sha256(japanese.encode("utf-8")).hexdigest()
    if expected != actual:
        raise ValueError(f"{path}: source hash mismatch at {scene}:{index}")
    normalized = dict(row)
    normalized["index"] = index
    normalized["source_sha256"] = expected
    return normalized


def documents_from_jsonl(messages: Path, targets: set[str]) -> dict[str, dict[str, Any]]:
    rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    labels: dict[str, str] = {}
    indexes: dict[str, set[str]] = defaultdict(set)
    for record in jsonl_records(messages):
        label = str(record["scene"])
        scene = canonical_scene(label)
        if scene not in targets:
            continue
        labels.setdefault(scene, label)
        index = normalize_index(record["ordinal"])
        if index in indexes[scene]:
            raise ValueError(f"{messages}: duplicate index {scene}:{index}")
        indexes[scene].add(index)
        japanese = str(record["source"])
        expected = str(record["source_sha256"]).lower()
        actual = hashlib.sha256(japanese.encode("utf-8")).hexdigest()
        if expected != actual:
            raise ValueError(f"{messages}: source hash mismatch at {scene}:{index}")
        rows[scene].append({
            "index": index,
            "engine_id": record["id"],
            "speaker": record.get("speaker"),
            "kind": record["kind"],
            "japanese": japanese,
            "source_sha256": expected,
        })
    documents: dict[str, dict[str, Any]] = {}
    for scene, scene_rows in rows.items():
        scene_rows.sort(key=lambda row: index_key(str(row["index"])))
        documents[scene] = {"scene": scene, "source_label": labels[scene], "rows": scene_rows}
    return documents


def documents_from_directory(source_dir: Path, targets: Iterable[str]) -> dict[str, dict[str, Any]]:
    documents: dict[str, dict[str, Any]] = {}
    for scene in targets:
        path = source_dir / f"{scene}.json"
        if not path.is_file():
            continue
        document = read_json(path)
        if str(document.get("scene")) != scene:
            raise ValueError(f"{path}: scene field does not match filename")
        rows = document.get("rows")
        if not isinstance(rows, list):
            raise ValueError(f"{path}: rows must be an array")
        seen: set[str] = set()
        normalized_rows: list[dict[str, Any]] = []
        for raw_row in rows:
            if not isinstance(raw_row, dict):
                raise ValueError(f"{path}: row must be an object")
            row = validate_row(path, scene, raw_row)
            index = str(row["index"])
            if index in seen:
                raise ValueError(f"{path}: duplicate index {index}")
            seen.add(index)
            normalized_rows.append(row)
        normalized_rows.sort(key=lambda row: index_key(str(row["index"])))
        normalized = dict(document)
        normalized["rows"] = normalized_rows
        documents[scene] = normalized
    return documents


def exclusion_indexes(entries: list[dict[str, Any]]) -> dict[str, set[str]]:
    result: dict[str, set[str]] = defaultdict(set)
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("scene"):
            raise ValueError("malformed content exclusion entry")
        scene = str(entry["scene"])
        result[scene].update(normalize_index(value) for value in entry.get("indexes", []))
        ranges = entry.get("ranges", [])
        if not isinstance(ranges, list):
            raise ValueError(f"{scene}: ranges must be an array")
        for pair in ranges:
            if not isinstance(pair, list) or len(pair) != 2:
                raise ValueError(f"{scene}: invalid exclusion range {pair!r}")
            start, end = int(pair[0]), int(pair[1])
            if start > end:
                raise ValueError(f"{scene}: invalid exclusion range {start}-{end}")
            result[scene].update(str(index) for index in range(start, end + 1))
    return dict(result)


def load_configured_exclusions(root: Path) -> tuple[dict[str, set[str]], list[str]]:
    tools = root / "tools"
    sys.path.insert(0, str(tools))
    try:
        from translation.exclusion_manifests import load_content_exclusions
    except ImportError as exc:
        raise RuntimeError("cannot import tools/translation/exclusion_manifests.py") from exc
    config = read_json(root / "codex_pipeline.json")
    merged = load_content_exclusions(root, config)
    entries = merged.get("entries", [])
    if not isinstance(entries, list):
        raise ValueError("merged content exclusions have no entries array")
    names = [str(config.get("content_exclusions") or "content_exclusions.json")]
    overlays = config.get("content_exclusion_overlays", [])
    names.extend([overlays] if isinstance(overlays, str) else list(overlays))
    return exclusion_indexes(entries), names


def project(raw: dict[str, Any], excluded: set[str]) -> dict[str, Any]:
    raw_rows = raw.get("rows", [])
    rows = [row for row in raw_rows if normalize_index(row["index"]) not in excluded]
    projection = dict(raw)
    projection["rows"] = rows
    projection["translatable_count"] = len(rows)
    projection["excluded_row_count"] = len(raw_rows) - len(rows)
    projected_indexes = {normalize_index(row["index"]) for row in rows}
    forbidden = projected_indexes & excluded
    if forbidden:
        raise RuntimeError(f"excluded rows leaked into {raw['scene']}: {sorted(forbidden)[:5]}")
    return projection


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--messages", type=Path, help="stable retail extraction JSONL")
    source.add_argument("--source-dir", type=Path, help="existing immutable per-scene JSON directory")
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--raw-output", type=Path)
    parser.add_argument("--model-output", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--verify-only", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.repo.resolve()
    manifest_path = (args.manifest or root / "state/wave200_remaining_source_manifest.json").resolve()
    raw_output = (args.raw_output or root / "scratchpad/jp_dumps").resolve()
    model_output = (args.model_output or root / "scratchpad/model_sources").resolve()
    report_path = (args.report or root / "state/wave200_remaining_extraction_report.json").resolve()

    manifest = read_json(manifest_path)
    targets, shard_by_scene = manifest_targets(manifest)
    target_set = set(targets)
    exclusions, exclusion_files = load_configured_exclusions(root)

    if args.source_dir:
        source_path = args.source_dir.resolve()
        documents = documents_from_directory(source_path, targets)
        source_kind = "scene_directory"
    else:
        source_path = args.messages.resolve() if args.messages else discover_messages(root)
        documents = documents_from_jsonl(source_path, target_set)
        source_kind = "stable_jsonl"

    missing = [scene for scene in targets if scene not in documents]
    if missing:
        raise RuntimeError(
            f"source extraction incomplete: missing {len(missing)}/{len(targets)} target scenes; "
            f"first={', '.join(missing[:8])}"
        )

    rows_report: list[dict[str, Any]] = []
    total_raw = total_model = total_excluded = 0
    fully_excluded: list[str] = []
    actions: dict[str, int] = defaultdict(int)

    for scene in targets:
        raw = documents[scene]
        projection = project(raw, exclusions.get(scene, set()))
        raw_path = raw_output / f"{scene}.json"
        model_path = model_output / f"{scene}.json"
        raw_count = len(raw.get("rows", []))
        model_count = len(projection.get("rows", []))
        excluded_count = raw_count - model_count

        if raw_count and not model_count:
            fully_excluded.append(scene)

        if args.verify_only:
            if not raw_path.is_file() or read_json(raw_path) != raw:
                raise RuntimeError(f"raw verification failed: {raw_path}")
            if model_count:
                if not model_path.is_file() or read_json(model_path) != projection:
                    raise RuntimeError(f"model verification failed: {model_path}")
                model_action = "verified"
            else:
                if model_path.exists():
                    raise RuntimeError(f"fully excluded model source must be absent: {model_path}")
                model_action = "absent"
            raw_action = "verified"
        else:
            raw_action = immutable_write(raw_path, raw)
            if model_count:
                model_action = replaceable_write(model_path, projection)
            else:
                if model_path.exists():
                    model_path.unlink()
                    model_action = "removed_forbidden"
                else:
                    model_action = "absent"

        actions[f"raw_{raw_action}"] += 1
        actions[f"model_{model_action}"] += 1
        total_raw += raw_count
        total_model += model_count
        total_excluded += excluded_count
        rows_report.append({
            "scene": scene,
            "shard": shard_by_scene[scene],
            "raw_rows": raw_count,
            "model_rows": model_count,
            "excluded_rows": excluded_count,
            "status": "fully_excluded" if raw_count and not model_count else "ready",
            "raw_sha256": hashlib.sha256(canonical_bytes(raw)).hexdigest(),
            "model_sha256": hashlib.sha256(canonical_bytes(projection)).hexdigest() if model_count else None,
        })

    report = {
        "schema_version": 1,
        "campaign": manifest.get("campaign"),
        "batch": manifest.get("batch"),
        "repository": manifest.get("repository"),
        "branch": manifest.get("branch"),
        "source": {
            "kind": source_kind,
            "path": str(source_path),
            "sha256": hashlib.sha256(source_path.read_bytes()).hexdigest() if source_path.is_file() else None,
        },
        "target_scene_count": len(targets),
        "target_shard_count": len(manifest.get("shards", [])),
        "raw_row_count": total_raw,
        "model_row_count": total_model,
        "excluded_row_count": total_excluded,
        "fully_excluded_scene_count": len(fully_excluded),
        "fully_excluded_scenes": fully_excluded,
        "exclusion_manifests": exclusion_files,
        "actions": dict(sorted(actions.items())),
        "launch_ready": True,
        "scenes": rows_report,
    }
    if not args.verify_only:
        atomic_write(report_path, canonical_bytes(report))
    print(json.dumps({
        "launch_ready": True,
        "scenes": len(targets),
        "shards": len(manifest.get("shards", [])),
        "raw_rows": total_raw,
        "model_rows": total_model,
        "excluded_rows": total_excluded,
        "fully_excluded_scenes": len(fully_excluded),
        "report": str(report_path),
    }, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
