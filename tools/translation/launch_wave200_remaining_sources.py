#!/usr/bin/env python3
"""One-shot source preparation for Tsuyokiss wave-200 shards 29-52.

Accepts data.fpk, a ZIP/.001 containing it, decoded members, stable JSONL, or
existing per-scene dumps. It creates immutable jp_dumps, exclusion-filtered
model_sources, 24 launch payloads, and a deterministic launch index. Excluded
rows never enter model payloads; fully excluded scenes have no model-source file.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import mmap
import os
import shutil
import struct
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

SCENE_MARKER = b"***SC_"


@dataclass(frozen=True)
class Entry:
    index: int
    name: str
    offset: int
    size: int


def read_json(path: Path) -> dict[str, Any]:
    def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate JSON key {key!r} in {path}")
            out[key] = value
        return out

    with path.open(encoding="utf-8") as handle:
        value = json.load(handle, object_pairs_hook=unique)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def encoded(value: Any) -> bytes:
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


def write_or_verify(path: Path, value: dict[str, Any], verify: bool) -> str:
    data = encoded(value)
    if verify:
        if not path.is_file() or path.read_bytes() != data:
            raise RuntimeError(f"verification failed: {path}")
        return "verified"
    if path.is_file() and path.read_bytes() == data:
        return "reused"
    action = "replaced" if path.exists() else "created"
    atomic_write(path, data)
    return action


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rel(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path.resolve())


def targets(manifest: dict[str, Any]) -> list[str]:
    shards = manifest.get("shards")
    if not isinstance(shards, list) or not shards:
        raise ValueError("manifest shards must be a non-empty array")
    scenes: list[str] = []
    for shard in shards:
        if not isinstance(shard, dict) or not isinstance(shard.get("scenes"), list):
            raise ValueError("malformed manifest shard")
        scenes.extend(str(scene) for scene in shard["scenes"])
    if len(scenes) != len(set(scenes)):
        raise ValueError("manifest contains duplicate scenes")
    if int(manifest.get("scene_count", len(scenes))) != len(scenes):
        raise ValueError("manifest scene_count mismatch")
    if int(manifest.get("shard_count", len(shards))) != len(shards):
        raise ValueError("manifest shard_count mismatch")
    return scenes


def fpk_entries(source: bytes | mmap.mmap) -> list[Entry]:
    if len(source) < 16:
        raise ValueError("FPK is too short")
    raw_count = struct.unpack_from("<i", source, 0)[0]
    if raw_count >= 0:
        raise ValueError("only encrypted-index CandySoft FPK is supported")
    count = raw_count & 0x7FFFFFFF
    index_offset = struct.unpack_from("<I", source, len(source) - 4)[0]
    key = bytes(source[len(source) - 8 : len(source) - 4])
    size = count * 36
    if index_offset < 4 or index_offset + size > len(source) - 8:
        raise ValueError("invalid FPK index placement")
    encrypted = source[index_offset : index_offset + size]
    index = bytes(value ^ key[pos & 3] for pos, value in enumerate(encrypted))
    result: list[Entry] = []
    for number in range(count):
        pos = number * 36
        offset, length = struct.unpack_from("<II", index, pos)
        name = index[pos + 8 : pos + 32].split(b"\0", 1)[0].decode("cp932")
        if not name or Path(name).name != name or offset < 4 or offset + length > len(source):
            raise ValueError(f"unsafe FPK member at index {number}")
        result.append(Entry(number, name, offset, length))
    return result


def decode_zlc2(data: bytes) -> bytes:
    if len(data) < 8 or data[:4] != b"ZLC2":
        raise ValueError("not a ZLC2 member")
    expected = struct.unpack_from("<I", data, 4)[0]
    src, base = 8, 0x1000
    out = bytearray(base)
    while len(out) - base < expected:
        if src >= len(data):
            raise EOFError("truncated ZLC2 flags")
        flags, src = data[src], src + 1
        for bit in range(7, -1, -1):
            if len(out) - base >= expected:
                break
            if flags & (1 << bit):
                if src + 2 > len(data):
                    raise EOFError("truncated ZLC2 reference")
                lo, hi = data[src], data[src + 1]
                src += 2
                distance = (lo | ((hi & 0xF0) << 4)) or 0x1000
                count = (hi & 0x0F) + 3
                if distance > len(out):
                    raise ValueError("invalid ZLC2 distance")
                for _ in range(count):
                    if len(out) - base >= expected:
                        break
                    out.append(out[-distance])
            else:
                if src >= len(data):
                    raise EOFError("truncated ZLC2 literal")
                out.append(data[src])
                src += 1
    return bytes(out[base : base + expected])


def unwrap(data: bytes) -> bytes:
    while data[:4] == b"ZLC2":
        data = decode_zlc2(data)
    return data


def scenario_parser(root: Path) -> Any:
    path = root / "tools/wordwrap/tsuyokiss_scenario.py"
    if not path.is_file():
        raise FileNotFoundError(f"missing scenario parser: {path}")
    spec = importlib.util.spec_from_file_location("tsuyokiss_scenario_source", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load scenario parser: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.records_for


def canonical_scene(label: str) -> str:
    return label.split("//", 1)[0].strip()


def records_to_jsonl(
    records: Iterable[Any], wanted: set[str], rows: dict[tuple[str, str], dict[str, Any]]
) -> None:
    for record in records:
        scene = canonical_scene(str(record.scene))
        if scene not in wanted:
            continue
        index = str(record.ordinal)
        key = (scene, index)
        source = str(record.source)
        row = {
            "scene": str(record.scene),
            "ordinal": record.ordinal,
            "id": str(record.id),
            "block": int(record.block),
            "kind": str(record.kind),
            "speaker": record.speaker,
            "source": source,
            "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
            "text": "",
        }
        if key in rows and rows[key] != row:
            raise ValueError(f"duplicate source index with drift: {scene}:{index}")
        rows[key] = row


def scan_blocks(
    root: Path, files: Iterable[tuple[int, str, bytes]], scene_order: list[str]
) -> tuple[bytes, dict[str, Any]]:
    parse = scenario_parser(root)
    wanted = set(scene_order)
    rows: dict[tuple[str, str], dict[str, Any]] = {}
    total = parsed = 0
    for block, _name, packed in files:
        total += 1
        data = unwrap(packed)
        if SCENE_MARKER not in data:
            continue
        try:
            _, found = parse(block, data)
        except (UnicodeDecodeError, ValueError):
            continue
        parsed += len(found)
        records_to_jsonl(found, wanted, rows)
    by_scene = {scene: 0 for scene in scene_order}
    for scene, _index in rows:
        by_scene[scene] += 1
    missing = [scene for scene, count in by_scene.items() if not count]
    if missing:
        raise RuntimeError(
            f"source missing {len(missing)}/{len(scene_order)} target scenes; "
            f"first={', '.join(missing[:8])}"
        )
    lines: list[str] = []
    for scene in scene_order:
        selected = [row for (name, _), row in rows.items() if name == scene]
        selected.sort(key=lambda row: int(row["ordinal"]))
        lines.extend(json.dumps(row, ensure_ascii=False) for row in selected)
    return ("\n".join(lines) + "\n").encode("utf-8"), {
        "block_count": total,
        "parsed_record_count": parsed,
        "target_record_count": len(rows),
    }


def from_fpk(root: Path, path: Path, scene_order: list[str]) -> tuple[bytes, dict[str, Any]]:
    with path.open("rb") as handle, mmap.mmap(handle.fileno(), 0, access=mmap.ACCESS_READ) as source:
        entries = fpk_entries(source)
        files = (
            (entry.index, entry.name, bytes(source[entry.offset : entry.offset + entry.size]))
            for entry in entries
        )
        jsonl, stats = scan_blocks(root, files, scene_order)
    return jsonl, {
        "kind": "data_fpk",
        "path": str(path.resolve()),
        "sha256": sha256(path),
        "archive_member_count": len(entries),
        **stats,
    }


def one(directory: Path, predicate: Any, label: str) -> Path | None:
    found = [path for path in directory.rglob("*") if path.is_file() and predicate(path)]
    if len(found) > 1:
        raise RuntimeError(f"multiple {label} candidates: {', '.join(str(p) for p in found[:8])}")
    return found[0] if found else None


def source_args(
    root: Path, source: Path, scene_order: list[str], temporary: Path
) -> tuple[list[str], dict[str, Any]]:
    if source.is_dir():
        fpk = one(source, lambda p: p.name.casefold() == "data.fpk", "data.fpk")
        if fpk:
            return source_args(root, fpk, scene_order, temporary)
        jsonl = one(source, lambda p: p.suffix.casefold() == ".jsonl", "JSONL")
        if jsonl:
            return ["--messages", str(jsonl)], {
                "kind": "stable_jsonl", "path": str(jsonl.resolve()), "sha256": sha256(jsonl)
            }
        if all((source / f"{scene}.json").is_file() for scene in scene_order):
            return ["--source-dir", str(source)], {"kind": "scene_directory", "path": str(source.resolve())}
        files = sorted((p for p in source.rglob("*") if p.is_file()), key=lambda p: str(p).casefold())
        jsonl, stats = scan_blocks(
            root,
            ((int(path.stem) if path.stem.isdigit() else n, path.name, path.read_bytes()) for n, path in enumerate(files)),
            scene_order,
        )
        generated = temporary / "translation_template.jsonl"
        generated.write_bytes(jsonl)
        return ["--messages", str(generated)], {"kind": "decoded_blocks", "path": str(source.resolve()), **stats}

    name = source.name.casefold()
    if name == "data.fpk" or source.suffix.casefold() == ".fpk":
        jsonl, meta = from_fpk(root, source, scene_order)
        generated = temporary / "translation_template.jsonl"
        generated.write_bytes(jsonl)
        return ["--messages", str(generated)], meta
    if source.suffix.casefold() == ".jsonl":
        return ["--messages", str(source)], {
            "kind": "stable_jsonl", "path": str(source.resolve()), "sha256": sha256(source)
        }
    if source.suffix.casefold() == ".zip":
        with zipfile.ZipFile(source) as archive:
            matches = [name for name in archive.namelist() if Path(name).name.casefold() == "data.fpk"]
            if len(matches) != 1:
                raise RuntimeError(f"{source}: expected one data.fpk, found {len(matches)}")
            extracted = temporary / "data.fpk"
            extracted.write_bytes(archive.read(matches[0]))
        args, meta = source_args(root, extracted, scene_order, temporary)
        meta |= {"input_archive": str(source.resolve()), "input_sha256": sha256(source)}
        return args, meta
    if name.endswith(".zip.001") or source.suffix.casefold() == ".001":
        exe = next((shutil.which(item) for item in ("7z", "7zz", "7za") if shutil.which(item)), None)
        if not exe:
            raise RuntimeError("multipart archive requires 7z, 7zz, or 7za")
        subprocess.run([exe, "x", "-y", f"-o{temporary}", str(source)], check=True)
        fpk = one(temporary, lambda p: p.name.casefold() == "data.fpk", "data.fpk")
        if not fpk:
            raise RuntimeError("multipart extraction produced no data.fpk")
        args, meta = source_args(root, fpk, scene_order, temporary)
        meta |= {"input_archive": str(source.resolve()), "input_sha256": sha256(source)}
        return args, meta
    raise ValueError(f"unsupported source: {source}")


def discover(root: Path) -> Path:
    preferred = [
        root / "data.fpk",
        root / "translation_template.jsonl",
        root / "scratchpad/project_sources/data.fpk",
        root / "scratchpad/project_sources/translation_template.jsonl",
        root / "scratchpad/game_extract/data.fpk",
        root / "scratchpad/game_extract/translation_template.jsonl",
    ]
    found = [path for path in preferred if path.exists()]
    if len(found) != 1:
        detail = ", ".join(str(path) for path in found) or "none"
        raise FileNotFoundError(f"unable to auto-select one source; candidates={detail}; pass --source")
    return found[0]


def launch_payloads(
    root: Path,
    manifest: dict[str, Any],
    report: dict[str, Any],
    raw_dir: Path,
    model_dir: Path,
    shard_dir: Path,
    verify: bool,
) -> tuple[dict[str, Any], dict[str, int]]:
    info = {str(item["scene"]): item for item in report["scenes"]}
    actions: dict[str, int] = {}
    index_rows: list[dict[str, Any]] = []
    for order, shard in enumerate(manifest["shards"], 1):
        number = int(shard["shard"])
        claim = str(shard.get("claim") or f"w200-{number:02d}")
        rows: list[dict[str, Any]] = []
        for scene_value in shard["scenes"]:
            scene = str(scene_value)
            current = info[scene]
            if not (raw_dir / f"{scene}.json").is_file():
                raise RuntimeError(f"missing immutable source: {scene}")
            model_path = model_dir / f"{scene}.json"
            if int(current["model_rows"]):
                if not model_path.is_file():
                    raise RuntimeError(f"missing model source: {scene}")
                payload: dict[str, Any] | None = read_json(model_path)
            else:
                if model_path.exists():
                    raise RuntimeError(f"fully excluded model source must be absent: {scene}")
                payload = None
            rows.append({
                "scene": scene,
                "status": current["status"],
                "raw_rows": current["raw_rows"],
                "model_rows": current["model_rows"],
                "excluded_rows": current["excluded_rows"],
                "payload": payload,
            })
        document = {
            "schema_version": 1,
            "campaign": manifest.get("campaign"),
            "branch": manifest.get("branch"),
            "launch_order": order,
            "shard": number,
            "claim": claim,
            "scenes": rows,
        }
        path = shard_dir / f"{claim}.json"
        action = write_or_verify(path, document, verify)
        actions[action] = actions.get(action, 0) + 1
        index_rows.append({
            "launch_order": order,
            "shard": number,
            "claim": claim,
            "path": rel(root, path),
            "scene_count": len(rows),
            "translatable_scene_count": sum(bool(int(row["model_rows"])) for row in rows),
            "model_row_count": sum(int(row["model_rows"]) for row in rows),
            "sha256": hashlib.sha256(encoded(document)).hexdigest(),
        })
    index = {
        "schema_version": 1,
        "campaign": manifest.get("campaign"),
        "branch": manifest.get("branch"),
        "scene_count": sum(row["scene_count"] for row in index_rows),
        "shard_count": len(index_rows),
        "launch_ready": True,
        "shards": index_rows,
    }
    action = write_or_verify(shard_dir / "launch_index.json", index, verify)
    actions[f"index_{action}"] = 1
    return index, actions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--source", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--raw-output", type=Path)
    parser.add_argument("--model-output", type=Path)
    parser.add_argument("--shard-output", type=Path)
    parser.add_argument("--extraction-report", type=Path)
    parser.add_argument("--launch-report", type=Path)
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()

    root = args.repo.resolve()
    manifest_path = (args.manifest or root / "state/wave200_remaining_source_manifest.json").resolve()
    extractor = root / "tools/translation/extract_wave200_remaining_sources.py"
    if not extractor.is_file():
        raise FileNotFoundError(f"missing delegated extractor: {extractor}")
    manifest = read_json(manifest_path)
    scene_order = targets(manifest)
    source = args.source.resolve() if args.source else discover(root)
    raw_dir = (args.raw_output or root / "scratchpad/jp_dumps").resolve()
    model_dir = (args.model_output or root / "scratchpad/model_sources").resolve()
    shard_dir = (args.shard_output or root / "scratchpad/model_shards").resolve()
    extraction_path = (args.extraction_report or root / "state/wave200_remaining_extraction_report.json").resolve()
    launch_path = (args.launch_report or root / "state/wave200_remaining_launch_report.json").resolve()

    with tempfile.TemporaryDirectory(prefix="tsuyokiss-wave200-") as name:
        delegated_args, source_meta = source_args(root, source, scene_order, Path(name))
        command = [
            sys.executable, str(extractor), "--repo", str(root), "--manifest", str(manifest_path),
            *delegated_args, "--raw-output", str(raw_dir), "--model-output", str(model_dir),
            "--report", str(extraction_path),
        ]
        if args.verify_only:
            command.append("--verify-only")
        subprocess.run(command, check=True)

    report = read_json(extraction_path)
    if not report.get("launch_ready") or int(report.get("target_scene_count", -1)) != len(scene_order):
        raise RuntimeError("delegated extraction did not validate exact target coverage")
    index, actions = launch_payloads(root, manifest, report, raw_dir, model_dir, shard_dir, args.verify_only)
    launch_report = {
        "schema_version": 1,
        "campaign": manifest.get("campaign"),
        "batch": manifest.get("batch"),
        "repository": manifest.get("repository"),
        "branch": manifest.get("branch"),
        "source": source_meta,
        "manifest": {"path": rel(root, manifest_path), "sha256": sha256(manifest_path)},
        "extraction_report": rel(root, extraction_path),
        "launch_index": rel(root, shard_dir / "launch_index.json"),
        "scene_count": index["scene_count"],
        "shard_count": index["shard_count"],
        "first_shard": manifest.get("first_shard"),
        "last_shard": manifest.get("last_shard"),
        "first_scene": manifest.get("first_scene"),
        "last_scene": manifest.get("last_scene"),
        "launch_ready": True,
        "actions": actions,
    }
    if args.verify_only:
        existing = read_json(launch_path)
        for key in (
            "schema_version", "campaign", "batch", "repository", "branch", "manifest",
            "extraction_report", "launch_index", "scene_count", "shard_count", "first_shard",
            "last_shard", "first_scene", "last_scene", "launch_ready",
        ):
            if existing.get(key) != launch_report.get(key):
                raise RuntimeError(f"launch report verification failed at {key}")
    else:
        atomic_write(launch_path, encoded(launch_report))
    print(json.dumps({
        "launch_ready": True,
        "source": source_meta.get("kind"),
        "scenes": index["scene_count"],
        "shards": index["shard_count"],
        "first_shard": manifest.get("first_shard"),
        "last_shard": manifest.get("last_shard"),
        "launch_index": rel(root, shard_dir / "launch_index.json"),
        "launch_report": rel(root, launch_path),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError, zipfile.BadZipFile) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
