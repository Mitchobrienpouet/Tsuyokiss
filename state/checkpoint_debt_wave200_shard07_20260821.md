# Checkpoint debt: wave 200 shard 7

Recorded: 2026-08-21

## Durable state

- Branch: `codex/wave-300-continuation-20260820`
- Starting remote head inspected: `0a27c81fae529e4fd6fc3d39df7746c2489e9545`
- Continuity/safety preflight is present for shard 7.
- `SC_G0930_00_G0990_00` has a translation for permitted indexes `1-38`.
- `SC_G0970_00_Z9999_99` has a translation for permitted indexes `91-101`.
- `SC_G0950_00_G0960_00` and `SC_G0960_00_G0970_00` are fully excluded and correctly have no downstream translation or QC artifacts.

## Validation completed

Both permitted translation JSON files parse successfully. Their index sets exactly match the preflight projection, contain no duplicate or out-of-range rows, preserve the required dialogue brackets and ASCII punctuation profile, and encode successfully as CP932.

## Resume hardening

The active wave-200 overlay in `state/content_exclusions_wave200_overlay.json` is additive to `content_exclusions.json`. The public `tools/codex_vn_pipeline.py` entry point now merges both manifests before any source projection, claim, QC, or validation step. A missing overlay, mismatched base manifest, schema mismatch, duplicate path, or repository-escaping path fails closed. The original orchestrator is preserved as `tools/codex_vn_pipeline_core.py` and must not be invoked directly.

## Open gate

Source-dependent accuracy QC is blocked in this execution environment because the ignored local source workspace and generated `scratchpad/model_sources/` projections are not mounted. The Japanese source is intentionally absent from Git. No source-based PASS has been invented.

Mandatory ordering is preserved: literary QC and targeted arbitration were not promoted ahead of accuracy QC. Shard 7 is not marked complete, and shard 8 has not been promoted.

## Exact resume point

1. Restore the local source workspace.
2. Use only `python tools/codex_vn_pipeline.py ...`; it applies canonical and wave-overlay exclusions fail-closed.
3. Regenerate model projections for the two permitted scenes from the authoritative exclusions.
4. Run independent accuracy QC for `SC_G0930_00_G0990_00` and `SC_G0970_00_Z9999_99`.
5. Run literary QC, then targeted arbitration or a documented no-op.
6. Re-run JSON, index, exclusion, punctuation, and CP932 gates.
7. Commit each fully gated scene narrowly, close shard 7, then continue with wave 200 shard 8.

No translation text, exclusion entry, retail archive, binary, or completed scene was modified by this checkpoint.
