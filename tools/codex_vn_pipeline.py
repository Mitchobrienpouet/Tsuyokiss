#!/usr/bin/env python3
"""Overlay-aware public entry point for the rolling Codex VN orchestrator."""

from __future__ import annotations

import codex_vn_pipeline_core as _pipeline
from translation.exclusion_manifests import load_content_exclusions


def content_exclusions() -> dict:
    try:
        return load_content_exclusions(_pipeline.ROOT, _pipeline.config())
    except (OSError, ValueError) as exc:
        raise SystemExit(
            f"refusing to run without complete content exclusions: {exc}"
        ) from exc


# Core functions resolve globals in the core module, so patch the loader there
# before re-exporting its public API.
_pipeline.content_exclusions = content_exclusions
for _name in dir(_pipeline):
    if not _name.startswith("_") and _name not in {"content_exclusions", "main"}:
        globals()[_name] = getattr(_pipeline, _name)


def main() -> int:
    return _pipeline.main()


if __name__ == "__main__":
    raise SystemExit(main())
