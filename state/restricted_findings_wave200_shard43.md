# Restricted-content preflight — wave-200 shard 43

STATUS: BLOCKED BEFORE SPEC / TRANSLATION

The canonical exclusion manifest and both configured overlays leave the target
scenes unfiltered. Fail-closed review of the generated model projection found
new restricted rows. Their contents are intentionally not reproduced,
summarized, translated, or used for continuity work here.

## Exact held-out ranges

- `SC_M0567_00_M0568_00`: indexes `1-12` (fully held out)
- `SC_M0568_00_M0569_00`: indexes `1-59`
- `SC_M0569_00_M0570_00`: indexes `1-4`

## Rows eligible for a regenerated projection

- `SC_M0566_00_M0567_00`: indexes `1-25` (25 rows)
- `SC_M0568_00_M0569_00`: indexes `60-63` (4 rows)
- `SC_M0569_00_M0570_00`: indexes `5-9` (5 rows)

Total eligible rows after remediation: 34. Total newly held-out rows: 75.

## Required remediation

Record the exact ranges above in the authoritative exclusion configuration,
then regenerate and validate the affected `scratchpad/model_sources/`
projections and `scratchpad/model_shards/w200-43.json` through
`tools/codex_vn_pipeline.py`. Resume continuity preflight only from the
regenerated filtered sources.

No shard spec, translation, QC, arbitration, contested note, or deterministic
validation output was produced.

