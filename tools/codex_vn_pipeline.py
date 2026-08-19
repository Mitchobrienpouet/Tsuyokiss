#!/usr/bin/env python3
"""Rolling Codex orchestrator for sharded visual-novel translation.

The runner keeps model work nondeterministic and orchestration deterministic:
atomic claims, bounded concurrency, JSONL/thread capture, idempotent stage outputs,
point-in-time dead/stalled checks, resume support, and final source/encoding gates.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import threading
import time
import uuid


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "codex_pipeline.json"
STATE_PATH = ROOT / "state" / "pipeline.json"
LOCK_PATH = ROOT / "state" / "pipeline.lock"
REPORT_SCHEMA = ROOT / "schemas" / "run_report.schema.json"
PROMPT_DIR = ROOT / "prompts"
STATE_MUTEX = threading.RLock()
STAGES = ("preflight", "translate", "accuracy", "literary", "arbitrate")


def utcnow() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def read_json(path: Path, *, reject_duplicates: bool = False):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key {key!r} in {path}")
            result[key] = value
        return result

    with path.open(encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=unique_pairs if reject_duplicates else None)


def atomic_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + f".{os.getpid()}.tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, path)


def config() -> dict:
    value = read_json(CONFIG_PATH, reject_duplicates=True)
    models = value.get("models", {})
    missing = [stage for stage in STAGES if stage not in models]
    if missing:
        raise SystemExit(f"missing model configuration for stages: {', '.join(missing)}")
    required_model = value.get("required_model")
    if required_model:
        mismatches = {
            stage: models[stage].get("model")
            for stage in STAGES
            if models[stage].get("model") != required_model
        }
        if mismatches:
            details = ", ".join(f"{stage}={model}" for stage, model in mismatches.items())
            raise SystemExit(
                f"quality profile requires {required_model}; refusing model substitution: {details}"
            )
    return value


def configured_path(key: str, default: str) -> Path | None:
    configured = config().get(key)
    if configured is False:
        return None
    path = ROOT / str(configured or default)
    if configured and not path.exists():
        raise SystemExit(f"configured {key} manifest does not exist: {path}")
    return path if path.exists() else None


def narrative_gates() -> dict:
    path = configured_path("narrative_gates", "narrative_gates.json")
    return read_json(path, reject_duplicates=True) if path else {
        "schema_version": 1,
        "source_mirrors": [],
        "repeated_choices": [],
    }


def content_exclusions() -> dict:
    path = configured_path("content_exclusions", "content_exclusions.json")
    return read_json(path, reject_duplicates=True) if path else {
        "schema_version": 1,
        "entries": [],
    }


def index_sort_key(value: str):
    return (0, int(value)) if str(value).isdigit() else (1, str(value))


def scene_sort_key(value: str):
    return [(0, int(part)) if part.isdigit() else (1, part.lower())
            for part in re.split(r"(\d+)", str(value))]


def row_index(row: dict) -> str:
    return str(row[config().get("row_index_field", "index")])


def row_source_text(row: dict) -> str:
    return str(row[config().get("source_text_field", "japanese")])


def excluded_indexes(scene: str) -> set[str]:
    indexes: set[str] = set()
    for entry in content_exclusions().get("entries", []):
        if str(entry.get("scene")) != scene:
            continue
        for start, end in entry.get("ranges", []):
            if int(start) > int(end):
                raise ValueError(f"invalid exclusion range {scene}:{start}-{end}")
            indexes.update(str(index) for index in range(int(start), int(end) + 1))
        indexes.update(str(index) for index in entry.get("indexes", []))
    return indexes


def model_source_path(scene: str) -> Path:
    return ROOT / "scratchpad" / "model_sources" / f"{scene}.json"


def prepare_model_source(scene: str) -> Path:
    source = read_json(source_path(scene), reject_duplicates=True)
    excluded = excluded_indexes(scene)
    projected = dict(source)
    projected["rows"] = [
        row for row in source.get("rows", []) if row_index(row) not in excluded
    ]
    projected["translatable_count"] = len(projected["rows"])
    projected["excluded_row_count"] = len(source.get("rows", [])) - len(projected["rows"])
    destination = model_source_path(scene)
    atomic_json(destination, projected)
    return destination


def source_rows(scene: str) -> dict[str, str]:
    source = read_json(source_path(scene), reject_duplicates=True)
    return {row_index(row): row_source_text(row) for row in source.get("rows", [])}


def exclusion_entry_indexes(entry: dict) -> set[str]:
    indexes = {str(index) for index in entry.get("indexes", [])}
    for start, end in entry.get("ranges", []):
        if int(start) > int(end):
            raise ValueError(
                f"invalid exclusion range {entry.get('scene')}:{start}-{end}"
            )
        indexes.update(str(index) for index in range(int(start), int(end) + 1))
    return indexes


def validate_exclusion_manifest() -> list[str]:
    problems: list[str] = []
    known = {path.stem for path in scene_paths()}
    seen: dict[str, set[str]] = {}
    for entry in content_exclusions().get("entries", []):
        scene = str(entry.get("scene"))
        if scene not in known:
            problems.append(f"exclusion references unknown scene {scene}")
            continue
        try:
            indexes = exclusion_entry_indexes(entry)
        except (TypeError, ValueError) as exc:
            problems.append(str(exc))
            continue
        raw = set(source_rows(scene))
        explicit = {str(index) for index in entry.get("indexes", [])}
        unknown_explicit = explicit - raw
        if unknown_explicit:
            problems.append(
                f"exclusion {scene} references absent explicit rows: "
                f"{sorted(unknown_explicit, key=index_sort_key)[:5]}"
            )
        for start, end in entry.get("ranges", []):
            declared = {str(index) for index in range(int(start), int(end) + 1)}
            if not (declared & raw):
                problems.append(f"exclusion range {scene}:{start}-{end} matches no source rows")
        matched = indexes & raw
        duplicate = seen.setdefault(scene, set()) & matched
        if duplicate:
            problems.append(
                f"overlapping exclusions in {scene}: "
                f"{sorted(duplicate, key=index_sort_key)[:5]}"
            )
        seen[scene].update(matched)
    return problems


def validate_narrative_sources() -> list[str]:
    """Fail before claims if declared mirrors or repeated choices drifted."""
    problems: list[str] = []
    known = {path.stem for path in scene_paths()}
    gates = narrative_gates()
    for mirror in gates.get("source_mirrors", []):
        scenes = [str(scene) for scene in mirror.get("scenes", [])]
        indexes = [str(index) for index in mirror.get("indexes", [])]
        canonical_scene = str(mirror.get("canonical_scene", scenes[0] if scenes else ""))
        if len(scenes) < 2 or canonical_scene not in scenes or any(scene not in known for scene in scenes):
            problems.append(f"invalid source mirror {mirror.get('id', '<unnamed>')}")
            continue
        canonical = source_rows(canonical_scene)
        for scene in scenes:
            if scene == canonical_scene:
                continue
            candidate = source_rows(scene)
            for index in indexes:
                if canonical.get(index) != candidate.get(index):
                    problems.append(
                        f"source mirror {mirror.get('id', '<unnamed>')} diverged "
                        f"at {canonical_scene}/{scene}:{index}"
                    )
    for choice in gates.get("repeated_choices", []):
        scene = str(choice.get("scene"))
        if scene not in known:
            problems.append(f"repeated choice references unknown scene {scene}")
            continue
        rows = source_rows(scene)
        values = {rows.get(str(index)) for index in choice.get("indexes", [])}
        if not values or None in values or len(values) != 1:
            problems.append(f"repeated choice {choice.get('id', '<unnamed>')} diverged in source")
    return problems


def validate_narrative_translation(scene: str, lines: dict[str, str]) -> list[str]:
    """Validate repeated choices and any translated branch mirror."""
    problems: list[str] = []
    gates = narrative_gates()
    for choice in gates.get("repeated_choices", []):
        if str(choice.get("scene")) != scene:
            continue
        indexes = [str(index) for index in choice.get("indexes", [])]
        values = {lines.get(index) for index in indexes}
        if None not in values and len(values) != 1:
            problems.append(
                f"{scene}: repeated choice {choice.get('id', '<unnamed>')} "
                "has inconsistent English"
            )

    for mirror in gates.get("source_mirrors", []):
        scenes = [str(value) for value in mirror.get("scenes", [])]
        if scene not in scenes:
            continue
        indexes = [str(index) for index in mirror.get("indexes", [])]
        for other in scenes:
            if other == scene or not translation_path(other).exists():
                continue
            try:
                other_doc = read_json(translation_path(other), reject_duplicates=True)
            except Exception as exc:
                problems.append(f"{scene}: mirror {other} is invalid JSON: {exc}")
                continue
            other_lines = other_doc.get("lines", {})
            for index in indexes:
                if index in lines and index in other_lines and lines[index] != other_lines[index]:
                    problems.append(
                        f"{scene}:{index}: English differs from mirror {other}:{index}"
                    )
    return problems


def default_state() -> dict:
    return {
        "schema_version": 1,
        "created_at": utcnow(),
        "updated_at": utcnow(),
        "scenes": {},
        "shards": [],
        "runs": [],
    }


def load_state() -> dict:
    return read_json(STATE_PATH) if STATE_PATH.exists() else default_state()


def mutate_state(mutator):
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with STATE_MUTEX, LOCK_PATH.open("a+") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        state = load_state()
        result = mutator(state)
        state["updated_at"] = utcnow()
        atomic_json(STATE_PATH, state)
        fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
    return result


def scene_paths() -> list[Path]:
    pattern = config().get("scene_id_regex", r".+")
    paths = [p for p in ROOT.glob(config()["scene_glob"]) if re.fullmatch(pattern, p.stem)]
    return sorted(paths, key=lambda p: scene_sort_key(p.stem))


def initialize() -> dict:
    paths = scene_paths()
    if not paths:
        raise SystemExit("no narrative scene JSON files found")

    for relative in (
        "translations", "qc/accuracy", "qc/literary", "scratchpad/specs",
        "scratchpad/contested", "scratchpad/model_sources", "state/logs", "state/final",
    ):
        (ROOT / relative).mkdir(parents=True, exist_ok=True)

    def update(state):
        for path in paths:
            scene = path.stem
            rows = set(source_rows(scene))
            fully_excluded = bool(rows) and rows <= excluded_indexes(scene)
            entry = state["scenes"].setdefault(scene, {
                "source": str(path.relative_to(ROOT)),
                "status": "excluded" if fully_excluded else "pending",
                "shard_id": None,
            })
            if fully_excluded and entry.get("status") == "pending":
                entry.update(status="excluded", shard_id=None)
        return state

    state = mutate_state(update)
    return state


def translation_path(scene: str) -> Path:
    return ROOT / "translations" / f"{scene}.json"


def source_path(scene: str) -> Path:
    matches = [path for path in scene_paths() if path.stem == scene]
    if len(matches) != 1:
        raise FileNotFoundError(f"expected exactly one source for scene {scene}, found {len(matches)}")
    return matches[0]


def validate_scene(scene: str, *, quiet: bool = False) -> tuple[bool, list[str]]:
    problems: list[str] = []
    source = source_path(scene)
    output = translation_path(scene)
    if not source.exists():
        return False, [f"{scene}: missing source"]
    if not output.exists():
        return False, [f"{scene}: missing translation"]
    try:
        src = read_json(source, reject_duplicates=True)
        translated = read_json(output, reject_duplicates=True)
    except Exception as exc:
        return False, [f"{scene}: invalid JSON: {exc}"]

    lines = translated.get("lines")
    if not isinstance(lines, dict):
        return False, [f"{scene}: lines must be an object"]
    excluded = excluded_indexes(scene)
    required = {row_index(row) for row in src.get("rows", [])} - excluded
    present = set(map(str, lines))
    missing = sorted(required - present, key=index_sort_key)
    if missing:
        problems.append(f"{scene}: missing {len(missing)} rows, first={missing[:5]}")
    forbidden_present = sorted(present & excluded, key=index_sort_key)
    if forbidden_present:
        problems.append(
            f"{scene}: contains {len(forbidden_present)} excluded rows, "
            f"first={forbidden_present[:5]}"
        )
    unexpected = sorted(present - required - excluded, key=index_sort_key)
    if unexpected:
        problems.append(
            f"{scene}: contains {len(unexpected)} unknown rows, first={unexpected[:5]}"
        )
    for seq, value in lines.items():
        if not isinstance(value, str):
            problems.append(f"{scene}:{seq}: expected string")
            continue
        try:
            value.encode(config()["codec"])
        except UnicodeEncodeError as exc:
            problems.append(f"{scene}:{seq}: not {config()['codec']}-clean: {exc}")
        forbidden = [char for char in "‘’“”–—…" if char in value]
        if forbidden:
            problems.append(f"{scene}:{seq}: non-ASCII typography {forbidden}")
    problems.extend(validate_narrative_translation(scene, lines))
    if not quiet:
        print(f"{scene}: {'OK' if not problems else 'FAIL'} ({len(lines)}/{len(required)} rows)")
        for problem in problems:
            print(f"  {problem}")
    return not problems, problems


def validate_all() -> bool:
    state = initialize()
    ok = True
    for scene in sorted(state["scenes"], key=scene_sort_key):
        if state["scenes"][scene]["status"] == "excluded":
            if translation_path(scene).exists():
                print(f"{scene}: FAIL (fully excluded scene has a translation)")
                ok = False
            continue
        good, _ = validate_scene(scene)
        ok = good and ok
    return ok


def scene_block(scene: str) -> str:
    pattern = config().get("narrative_block_regex", r"^(.).*" )
    match = re.match(pattern, scene)
    if not match:
        return scene
    return match.group(1) if match.groups() else match.group(0)


def chunk_pending(
    state: dict,
    limit: int,
    *,
    scene_limit: int | None = None,
) -> list[list[str]]:
    size = int(config()["shard_size"])
    pending = [scene for scene in sorted(state["scenes"], key=scene_sort_key)
               if state["scenes"][scene]["status"] == "pending"]
    if scene_limit is not None:
        if scene_limit < 0:
            raise ValueError("scene_limit must be non-negative")
        pending = pending[:scene_limit]
    groups: list[list[str]] = []
    current: list[str] = []
    block = None
    for scene in pending:
        next_block = scene_block(scene)
        if block is not None and (next_block != block or len(current) >= size):
            groups.append(current)
            current = []
        block = next_block
        current.append(scene)
    if current:
        groups.append(current)
    return groups[:limit]


def acquire_shards(
    count: int,
    *,
    dry_run: bool,
    scene_limit: int | None = None,
) -> list[dict]:
    initialize()
    source_gate_problems = validate_narrative_sources()
    if source_gate_problems:
        raise SystemExit("narrative source gate failed: " + "; ".join(source_gate_problems))
    exclusion_problems = validate_exclusion_manifest()
    if exclusion_problems:
        raise SystemExit("content exclusion gate failed: " + "; ".join(exclusion_problems))

    def acquire(state):
        existing = [s for s in state["shards"] if s["status"] in {"claimed", "blocked"}]
        selected = existing[:count]
        needed = max(0, count - len(selected))
        already_selected = sum(len(shard["scenes"]) for shard in selected)
        remaining_scene_limit = None
        if scene_limit is not None:
            remaining_scene_limit = max(0, scene_limit - already_selected)
        for scenes in chunk_pending(state, needed, scene_limit=remaining_scene_limit):
            shard = {
                "id": f"shard-{'-'.join(scenes)}-{uuid.uuid4().hex[:8]}",
                "scenes": scenes,
                "status": "claimed",
                "created_at": utcnow(),
                "updated_at": utcnow(),
            }
            selected.append(shard)
            if not dry_run:
                state["shards"].append(shard)
                for scene in scenes:
                    state["scenes"][scene].update(status="claimed", shard_id=shard["id"])
        return selected

    if dry_run:
        state = load_state()
        existing = [s for s in state.get("shards", []) if s["status"] in {"claimed", "blocked"}]
        selected = existing[:count]
        already_selected = sum(len(shard["scenes"]) for shard in selected)
        remaining_scene_limit = None
        if scene_limit is not None:
            remaining_scene_limit = max(0, scene_limit - already_selected)
        for scenes in chunk_pending(
            state,
            max(0, count - len(selected)),
            scene_limit=remaining_scene_limit,
        ):
            selected.append({"id": "DRY-RUN", "scenes": scenes, "status": "planned"})
        return selected
    return mutate_state(acquire)


def set_shard_status(shard_id: str, status: str) -> None:
    def update(state):
        for shard in state["shards"]:
            if shard["id"] == shard_id:
                shard["status"] = status
                shard["updated_at"] = utcnow()
                for scene in shard["scenes"]:
                    if status == "done":
                        state["scenes"][scene]["status"] = "done"
                    elif status == "blocked":
                        state["scenes"][scene]["status"] = "claimed"
                break
    mutate_state(update)


def spec_path(shard: dict) -> Path:
    return ROOT / "scratchpad" / "specs" / ("-".join(shard["scenes"]) + ".md")


def adjacent_files(scenes: list[str]) -> list[Path]:
    all_ids = [p.stem for p in scene_paths()]
    positions = [all_ids.index(s) for s in scenes]
    indices = {min(positions) - 1, max(positions) + 1}
    return [prepare_model_source(all_ids[i]) for i in sorted(indices) if 0 <= i < len(all_ids)]


def render_prompt(stage: str, task: dict) -> str:
    template = (PROMPT_DIR / f"{stage}.md").read_text(encoding="utf-8")
    shard = task["shard"]
    scene = task.get("scene", "")
    replacements = {
        "SCENES": ", ".join(shard["scenes"]),
        "SCENE": scene,
        "SOURCE_FILES": "\n".join(
            str(prepare_model_source(s).relative_to(ROOT)) for s in shard["scenes"]
        ),
        "ADJACENT_FILES": "\n".join(str(p.relative_to(ROOT)) for p in adjacent_files(shard["scenes"])) or "NONE",
        "SOURCE_FILE": str(prepare_model_source(scene).relative_to(ROOT)) if scene else "",
        "SPEC_FILE": str(spec_path(shard).relative_to(ROOT)),
        "TRANSLATION_FILE": f"translations/{scene}.json" if scene else "",
        "QC_FILE": task.get("qc_file", ""),
        "ACCURACY_FILE": f"qc/accuracy/{scene}.md" if scene else "",
        "LITERARY_FILE": f"qc/literary/{scene}.md" if scene else "",
        "CONTESTED_FILE": f"scratchpad/contested/{scene}.md" if scene else "",
    }
    for key, value in replacements.items():
        template = template.replace("{{" + key + "}}", value)
    return template


def record_run_start(task: dict, log: Path, final: Path) -> str:
    run_id = uuid.uuid4().hex

    def update(state):
        state["runs"].append({
            "id": run_id,
            "stage": task["stage"],
            "scene": task.get("scene"),
            "shard_id": task["shard"]["id"],
            "scenes": task["shard"]["scenes"],
            "status": "starting",
            "pid": None,
            "thread_id": None,
            "log": str(log.relative_to(ROOT)),
            "final": str(final.relative_to(ROOT)),
            "started_at": utcnow(),
            "ended_at": None,
            "exit_code": None,
        })
    mutate_state(update)
    return run_id


def update_run(run_id: str, **changes) -> None:
    def update(state):
        for run in state["runs"]:
            if run["id"] == run_id:
                run.update(changes)
                break
    mutate_state(update)


def codex_command(task: dict, prompt: str, final: Path) -> list[str]:
    codex = shutil.which(os.environ.get("CODEX_BIN", "codex"))
    if not codex:
        raise RuntimeError("codex executable not found in PATH (or set CODEX_BIN)")
    stage_cfg = config()["models"][task["stage"]]
    return [
        codex, "exec", "--json", "--approve-for-me", "--cd", str(ROOT),
        "--model", stage_cfg["model"],
        "--config", f'model_reasoning_effort="{stage_cfg["reasoning"]}"',
        "--output-schema", str(REPORT_SCHEMA),
        "--output-last-message", str(final), prompt,
    ]


def validate_run_report(path: Path, task: dict) -> list[str]:
    problems: list[str] = []
    try:
        report = read_json(path, reject_duplicates=True)
    except Exception as exc:
        return [f"invalid structured report: {exc}"]
    required = {"status", "stage", "scenes", "files_written", "issues", "contested_seqs"}
    missing = sorted(required - set(report))
    if missing:
        problems.append(f"structured report missing keys: {missing}")
    if report.get("status") not in {"completed", "skipped", "blocked"}:
        problems.append(f"invalid report status {report.get('status')!r}")
    if report.get("stage") != task["stage"]:
        problems.append(
            f"report stage {report.get('stage')!r} does not match {task['stage']!r}"
        )
    expected_scenes = [task["scene"]] if task.get("scene") else task["shard"]["scenes"]
    if report.get("scenes") != expected_scenes:
        problems.append(
            f"report scenes {report.get('scenes')!r} do not match {expected_scenes!r}"
        )
    for key in ("files_written", "issues", "contested_seqs"):
        if key in report and not isinstance(report[key], list):
            problems.append(f"report {key} must be an array")
    return problems


def run_task(task: dict) -> bool:
    stage = task["stage"]
    label = task.get("scene") or "-".join(task["shard"]["scenes"])
    stamp = f"{stage}-{label}-{uuid.uuid4().hex[:8]}"
    log = ROOT / "state" / "logs" / f"{stamp}.jsonl"
    err = ROOT / "state" / "logs" / f"{stamp}.stderr.log"
    final = ROOT / "state" / "final" / f"{stamp}.json"
    for path in (log, err, final):
        path.parent.mkdir(parents=True, exist_ok=True)
    run_id = record_run_start(task, log, final)
    try:
        command = codex_command(task, render_prompt(stage, task), final)
        with log.open("w", encoding="utf-8") as out, err.open("w", encoding="utf-8") as errors:
            process = subprocess.Popen(
                command, cwd=ROOT, stdout=subprocess.PIPE, stderr=errors,
                text=True, encoding="utf-8", errors="replace", bufsize=1,
            )
            update_run(run_id, status="running", pid=process.pid)
            assert process.stdout is not None
            for line in process.stdout:
                out.write(line)
                out.flush()
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if event.get("type") == "thread.started" and event.get("thread_id"):
                    update_run(run_id, thread_id=event["thread_id"])
            code = process.wait()
        report_problems = validate_run_report(final, task) if code == 0 else []
        status = "completed" if code == 0 and not report_problems else "failed"
        update_run(
            run_id,
            status=status,
            exit_code=code,
            ended_at=utcnow(),
            report_problems=report_problems,
        )
        if report_problems:
            with err.open("a", encoding="utf-8") as errors:
                errors.write("\n".join(report_problems) + "\n")
        return status == "completed"
    except Exception as exc:
        err.write_text(f"{type(exc).__name__}: {exc}\n", encoding="utf-8")
        update_run(run_id, status="failed", exit_code=127, ended_at=utcnow(), error=str(exc))
        return False


def run_phase(tasks: list[dict], max_parallel: int) -> dict[str, bool]:
    if not tasks:
        return {}
    results: dict[str, bool] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_parallel) as pool:
        futures = {pool.submit(run_task, task): task for task in tasks}
        for future in concurrent.futures.as_completed(futures):
            task = futures[future]
            key = task.get("scene") or task["shard"]["id"]
            try:
                results[key] = future.result()
            except Exception:
                results[key] = False
    spot_check_dead(mark=True)
    return results


def output_exists(stage: str, shard: dict, scene: str | None = None) -> bool:
    if stage == "preflight":
        path = spec_path(shard)
    elif stage == "translate":
        return validate_scene(scene or "", quiet=True)[0]
    elif stage == "accuracy":
        path = ROOT / "qc" / "accuracy" / f"{scene}.md"
    elif stage == "literary":
        path = ROOT / "qc" / "literary" / f"{scene}.md"
    else:
        path = ROOT / "scratchpad" / "contested" / f"{scene}.md"
    return path.exists() and path.stat().st_size > 0


def execute(
    shard_count: int,
    max_parallel: int,
    dry_run: bool,
    *,
    scene_limit: int | None = None,
) -> bool:
    spot_check_dead(mark=True)
    shards = acquire_shards(shard_count, dry_run=dry_run, scene_limit=scene_limit)
    if not shards:
        print("No unfinished shards.")
        return True
    print(json.dumps({"shards": [{"id": s["id"], "scenes": s["scenes"]} for s in shards]}, indent=2))
    if dry_run:
        return True
    if not shutil.which(os.environ.get("CODEX_BIN", "codex")):
        print("codex executable not found; plan created but no model work launched", file=sys.stderr)
        return False

    for shard in shards:
        set_shard_status(shard["id"], "running")

    preflight_tasks = [{"stage": "preflight", "shard": shard} for shard in shards
                       if not output_exists("preflight", shard)]
    preflight = run_phase(preflight_tasks, max_parallel)
    active = [s for s in shards if output_exists("preflight", s) and preflight.get(s["id"], True)]

    translate_tasks = [{"stage": "translate", "shard": shard, "scene": scene}
                       for shard in active for scene in shard["scenes"]
                       if not output_exists("translate", shard, scene)]
    translated = run_phase(translate_tasks, max_parallel)

    accuracy_tasks = [{"stage": "accuracy", "shard": shard, "scene": scene,
                       "qc_file": f"qc/accuracy/{scene}.md"}
                      for shard in active for scene in shard["scenes"]
                      if validate_scene(scene, quiet=True)[0]
                      and not output_exists("accuracy", shard, scene)
                      and translated.get(scene, True)]
    accurate = run_phase(accuracy_tasks, max_parallel)

    literary_tasks = [{"stage": "literary", "shard": shard, "scene": scene,
                       "qc_file": f"qc/literary/{scene}.md"}
                      for shard in active for scene in shard["scenes"]
                      if output_exists("accuracy", shard, scene)
                      and not output_exists("literary", shard, scene)
                      and accurate.get(scene, True)]
    literary = run_phase(literary_tasks, max_parallel)

    arbitration_tasks = [{"stage": "arbitrate", "shard": shard, "scene": scene}
                         for shard in active for scene in shard["scenes"]
                         if output_exists("literary", shard, scene)
                         and not output_exists("arbitrate", shard, scene)
                         and literary.get(scene, True)]
    run_phase(arbitration_tasks, max_parallel)

    all_ok = True
    for shard in shards:
        complete = all(
            validate_scene(scene, quiet=True)[0]
            and output_exists("accuracy", shard, scene)
            and output_exists("literary", shard, scene)
            and output_exists("arbitrate", shard, scene)
            for scene in shard["scenes"]
        )
        set_shard_status(shard["id"], "done" if complete else "blocked")
        all_ok = complete and all_ok
    return all_ok


def pid_alive(pid) -> bool:
    if not isinstance(pid, int) or pid <= 0:
        return False
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError):
        return False


def spot_check_dead(*, mark: bool) -> list[dict]:
    state = load_state()
    stale_after = int(config()["stale_after_seconds"])
    now = time.time()
    findings = []
    for run in state.get("runs", []):
        if run.get("status") not in {"starting", "running"}:
            continue
        log = ROOT / run["log"]
        age = now - log.stat().st_mtime if log.exists() else float("inf")
        if not pid_alive(run.get("pid")):
            status, reason = "dead", "process is absent"
        elif age > stale_after:
            status, reason = "stalled", f"no JSONL event for {int(age)} seconds"
        else:
            continue
        findings.append({"run_id": run["id"], "stage": run["stage"], "scene": run.get("scene"),
                         "thread_id": run.get("thread_id"), "status": status, "reason": reason})
        if mark:
            update_run(run["id"], status=status, checked_at=utcnow(), diagnostic=reason)
            set_shard_status(run["shard_id"], "blocked")
    print(json.dumps({"checked_at": utcnow(), "findings": findings}, indent=2))
    return findings


def resume_dead(max_parallel: int) -> bool:
    codex = shutil.which(os.environ.get("CODEX_BIN", "codex"))
    if not codex:
        print("codex executable not found", file=sys.stderr)
        return False
    spot_check_dead(mark=True)
    state = load_state()
    targets = [run for run in state.get("runs", [])
               if run.get("status") in {"dead", "stalled", "failed"} and run.get("thread_id")]
    if not targets:
        print("No resumable dead/stalled/failed runs with a thread ID.")
        return True

    def resume(run: dict) -> bool:
        log = ROOT / "state" / "logs" / f"resume-{run['id']}-{uuid.uuid4().hex[:8]}.jsonl"
        prompt = "Resume the interrupted stage. Re-read AGENTS.md and the current files, finish only the original task, preserve idempotency, run its checks, and return the required structured report."
        command = [
            codex, "exec", "--json", "--approve-for-me", "--cd", str(ROOT),
            "resume", run["thread_id"], prompt,
        ]
        update_run(run["id"], status="resuming", resumed_at=utcnow())
        with log.open("w", encoding="utf-8") as out:
            result = subprocess.run(command, cwd=ROOT, stdout=out, stderr=subprocess.STDOUT, text=True)
        update_run(run["id"], status="completed" if result.returncode == 0 else "failed",
                   exit_code=result.returncode, ended_at=utcnow(), resume_log=str(log.relative_to(ROOT)))
        return result.returncode == 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_parallel) as pool:
        results = list(pool.map(resume, targets))
    return all(results)


def print_status() -> None:
    findings = spot_check_dead(mark=True)
    state = initialize()
    counts: dict[str, int] = {}
    for entry in state["scenes"].values():
        counts[entry["status"]] = counts.get(entry["status"], 0) + 1
    running = sum(run.get("status") in {"starting", "running", "resuming"} for run in state["runs"])
    failed = sum(run.get("status") in {"failed", "dead", "stalled"} for run in state["runs"])
    print(json.dumps({
        "scene_total": len(state["scenes"]),
        "scene_status": counts,
        "shards": len(state["shards"]),
        "runs_in_flight": running,
        "runs_failed_or_suspect": failed,
        "dead_or_stalled_found_now": len(findings),
    }, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    sub.add_parser("status")
    run = sub.add_parser("run")
    run.add_argument("--shards", type=int, default=6)
    run.add_argument(
        "--scene-limit",
        type=int,
        default=None,
        help="claim at most this many scenes across the selected shards",
    )
    run.add_argument("--max-parallel", type=int, default=None)
    run.add_argument("--dry-run", action="store_true")
    sub.add_parser("check-dead")
    resume = sub.add_parser("resume-dead")
    resume.add_argument("--max-parallel", type=int, default=None)
    sub.add_parser("validate")
    args = parser.parse_args()
    maximum = args.max_parallel if hasattr(args, "max_parallel") and args.max_parallel else int(config()["max_parallel"])

    if args.command == "init":
        state = initialize()
        print(f"initialized {len(state['scenes'])} scenes")
        return 0
    if args.command == "status":
        print_status()
        return 0
    if args.command == "run":
        return 0 if execute(
            args.shards,
            maximum,
            args.dry_run,
            scene_limit=args.scene_limit,
        ) else 1
    if args.command == "check-dead":
        spot_check_dead(mark=True)
        return 0
    if args.command == "resume-dead":
        return 0 if resume_dead(maximum) else 1
    return 0 if validate_all() else 1


if __name__ == "__main__":
    raise SystemExit(main())
