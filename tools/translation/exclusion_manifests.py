#!/usr/bin/env python3
"""Load canonical content exclusions plus additive fail-closed overlays."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> dict[str, Any]:
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key {key!r} in {path}")
            result[key] = value
        return result

    with path.open(encoding="utf-8") as handle:
        value = json.load(handle, object_pairs_hook=unique_pairs)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def _configured_overlay_names(config: dict[str, Any]) -> list[str]:
    value = config.get("content_exclusion_overlays", [])
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item.strip() for item in value
    ):
        raise ValueError(
            "content_exclusion_overlays must be a path or a list of paths"
        )
    names = [item.strip() for item in value]
    if len(names) != len(set(names)):
        raise ValueError("content_exclusion_overlays contains duplicate paths")
    return names


def _repository_path(root: Path, name: str, *, purpose: str) -> Path:
    relative = Path(name)
    if relative.is_absolute():
        raise ValueError(f"{purpose} must be repository-relative: {name}")
    resolved_root = root.resolve()
    resolved = (resolved_root / relative).resolve()
    try:
        resolved.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(f"{purpose} escapes the repository: {name}") from exc
    return resolved


def _entries(document: dict[str, Any], path: Path) -> list[dict[str, Any]]:
    value = document.get("entries", [])
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise ValueError(f"{path}: entries must be a list of objects")
    return value


def load_content_exclusions(root: Path, config: dict[str, Any]) -> dict[str, Any]:
    """Merge the configured canonical manifest and overlays without mutation."""
    base_name = config.get("content_exclusions") or "content_exclusions.json"
    if not isinstance(base_name, str) or not base_name.strip():
        raise ValueError("content_exclusions must name a repository-relative JSON file")
    base_name = base_name.strip()
    base_path = _repository_path(root, base_name, purpose="content exclusion manifest")
    if not base_path.is_file():
        raise FileNotFoundError(
            f"content exclusion manifest does not exist: {base_path}"
        )

    base = _read_json(base_path)
    schema_version = base.get("schema_version")
    merged_entries = list(_entries(base, base_path))
    overlay_names = _configured_overlay_names(config)

    for overlay_name in overlay_names:
        overlay_path = _repository_path(
            root, overlay_name, purpose="content exclusion overlay"
        )
        if not overlay_path.is_file():
            raise FileNotFoundError(
                f"content exclusion overlay does not exist: {overlay_path}"
            )
        overlay = _read_json(overlay_path)
        referenced_base = overlay.get("base_manifest")
        if referenced_base:
            if not isinstance(referenced_base, str) or not referenced_base.strip():
                raise ValueError(f"{overlay_path}: base_manifest must be a path")
            referenced_path = _repository_path(
                root,
                referenced_base.strip(),
                purpose=f"{overlay_path} base_manifest",
            )
            if referenced_path != base_path:
                raise ValueError(
                    f"{overlay_path}: base_manifest {referenced_base!r} "
                    f"does not match {base_name!r}"
                )
        if overlay.get("schema_version") != schema_version:
            raise ValueError(
                f"{overlay_path}: schema_version does not match {base_path}"
            )
        merged_entries.extend(_entries(overlay, overlay_path))

    merged = dict(base)
    merged["entries"] = merged_entries
    merged["overlay_manifests"] = overlay_names
    return merged
