# Wave500 shard58 legacy-validator repair preflight

Status: **repair-ready; no policy blocker**. This is an audit-only record. No
translation, QC, arbitration, source, exclusion, configuration, or Git artifact
was changed during this preflight.

## Scope and policy boundary

Audited scenes:

- `SC_M0431_00_M0432_00`
- `SC_M0470_00_M0471_00`
- `SC_M0500_00_M0501_00`
- `SC_M0520_00_M0530_00`

The canonical `content_exclusions.json` and both configured overlays
(`state/content_exclusions_wave200_overlay.json` and
`state/content_exclusions_wave500_overlay.json`) contain no entry for any of
these scenes. The four filtered projections each report zero excluded rows.
`narrative_gates.json` declares no mirror or repeated-choice group. Only these
permitted scene projections and permitted adjacent filtered context were
inspected; no excluded row was read or inferred.

## Authoritative evidence

Current `scratchpad/jp_dumps` rows and filtered `scratchpad/model_sources` rows
are exactly identical for each scene. Their byte hashes also match the recorded
hashes in `state/wave200_remaining_extraction_report.json`.

| Scene | Current raw/model rows | Current translation keys | Validator result | Historical accuracy claim |
|---|---:|---:|---|---|
| `SC_M0431_00_M0432_00` | 65 (`1-65`) | 69 (`1-69`) | unknown `66-69` | 69/69 |
| `SC_M0470_00_M0471_00` | 68 (`1-68`) | 69 (`1-69`) | unknown `69` | 69/69 |
| `SC_M0500_00_M0501_00` | 65 (`1-65`) | 67 (`1-67`) | unknown `66-67` | 67/67 |
| `SC_M0520_00_M0530_00` | 57 (`1-57`) | 58 (`1-58`) | unknown `58` | 58/58 |

The current authoritative file hashes are:

| Scene | Raw SHA-256 | Filtered-model SHA-256 |
|---|---|---|
| `SC_M0431_00_M0432_00` | `2094ec2295ad510c451e70141198e3e8ca0cc1dc3f0d0612fa5e41ccd744f8f2` | `89e5b0888f1048a1b2def5cf3af6f6125d8104252f3f18e32aaf976eff60dfcc` |
| `SC_M0470_00_M0471_00` | `eadb85b8a7db41a2ba411cf533347fedc379db30ba615085cbf240d109f5fded` | `257b8c183e020ab1881b3f6ea65c8d8f265b087cc2093b02a56b044f3bb918dd` |
| `SC_M0500_00_M0501_00` | `23dfb47b84397cb2f07214b3c969250f336a48c33e29bd63d030c0c0a42a9dff` | `dce3d45f372dee9dab35a102ac4751a291b40e6b711211192dc877e9b7bc012f` |
| `SC_M0520_00_M0530_00` | `74b2cbf217f489928df2e5a2a66d518c2e4c337d322e494118bc517e7b2b705f` | `99590e251155ea694d56c710cfb44c9f52776bb194e4b31f34ba9f6ece87c046` |

## Exact cause

The translations and their historical QC/preflight records were produced
against larger legacy Full Edition projections. The subsequently established
authoritative raw/model projections contain eight fewer displayed messages at
internal positions. The legacy translations therefore retain eight
source-absent messages and keep the old indexes for every later message.

This is **projection-version index drift**, not an exclusion error and not a
case where the validator merely objects to harmless tail padding. Because both
old and current key sets are contiguous from `1`, the validator exposes only
the overflow keys; it does not expose the much larger overlapping suffixes
whose values are now attached to the wrong current indexes.

## Minimal source-faithful translation repair

Perform a mechanical delete-and-compact operation only. Do not rewrite any
surviving English text.

| Scene | Discard legacy keys absent from current source | Exact legacy-to-current remap |
|---|---|---|
| `SC_M0431_00_M0432_00` | `20`, `29`, `44`, `69` | old `1-19` -> new `1-19`; old `21-28` -> new `20-27`; old `30-43` -> new `28-41`; old `45-68` -> new `42-65` |
| `SC_M0470_00_M0471_00` | `48` | old `1-47` -> new `1-47`; old `49-69` -> new `48-68` |
| `SC_M0500_00_M0501_00` | `50`, `56` | old `1-49` -> new `1-49`; old `51-55` -> new `50-54`; old `57-67` -> new `55-65` |
| `SC_M0520_00_M0530_00` | `9` | old `1-8` -> new `1-8`; old `10-58` -> new `9-57` |

The affected current suffixes are therefore `M0431:20-65`, `M0470:48-68`,
`M0500:50-65`, and `M0520:9-57`; repairing only the validator-reported tail
keys would leave all of those ranges misindexed.

An in-memory simulation of the mapping above produces exactly 65, 68, 65, and
57 rows, with zero dialogue/narration wrapper mismatches and full CP932
encodability.

## Tail-row classification

The reported tail rows are not a set of stale silent separators:

- `M0431` old `66-68` are valid translations for current `63-65`; old `69` is
  the fourth legacy-only substantive message and must be discarded.
- `M0470` old `69` is the valid translation for current `68`. It is a silent
  ellipsis narration beat, but it is authoritative and must be retained at the
  corrected index rather than deleted.
- `M0500` old `66-67` are valid translations for current `64-65`.
- `M0520` old `58` is the valid translation for current `57`.

Blanket deletion of unknown tail keys would therefore delete seven valid
source-backed messages and still leave the overlapping suffixes misaligned.

## QC, arbitration, and preflight record actions

After the mechanical translation repair, re-run independent accuracy checks
against the current filtered projections and make these record corrections:

- `qc/accuracy/SC_M0431_00_M0432_00.md`: change the stale 69/69 and `1-69`
  claims to 65/65 and `1-65` after revalidation.
- `qc/accuracy/SC_M0470_00_M0471_00.md`: change 69/69 and `1-69` to 68/68 and
  `1-68` after revalidation.
- `qc/accuracy/SC_M0500_00_M0501_00.md`: change 67/67 and `1-67` to 65/65 and
  `1-65` after revalidation.
- `qc/accuracy/SC_M0520_00_M0530_00.md`: change 58/58 and `1-58` to 57/57 and
  `1-57`; remap its documented fidelity fixes from old `22` -> current `21`
  and old `41` -> current `40`.
- The four literary reports make no stale numeric coverage assertion and need
  no prose change if the revalidated text is unchanged.
- The `NONE` arbitration records for `M0431`, `M0470`, and `M0500` remain
  applicable after revalidation.
- `scratchpad/contested/SC_M0520_00_M0530_00.md`: change its deterministic
  coverage assertion from `1-58` to `1-57`; the retained fake-sender reading
  moves mechanically from old `55` to current `54`.

The earlier shard preflights also retain superseded counts. For consistent
documentation, correct or explicitly supersede these claims during the repair
checkpoint:

- shard35 `M0431`: 69 -> 65 (shard total 277 -> 273);
- shard36 `M0470`: 69 -> 68 (shard total 216 -> 215);
- shard37 `M0500`: 67 -> 65 (shard total 163 -> 161);
- shard38 `M0520`: 58 -> 57 (shard total 147 -> 146).

No source dump, model projection, exclusion manifest, narrative gate, speaker
map, or pipeline configuration should be changed for this repair.

## Required validation after repair

1. Confirm exact source-index sets `1-65`, `1-68`, `1-65`, and `1-57` with no
   unknown or missing keys.
2. Re-run line-by-line accuracy on every moved suffix listed above, preserving
   the current source's speakers, agency, reveal timing, and hard stops.
3. Validate JSON structure, unique indexes, dialogue wrappers, metadata,
   CP932, and forbidden typography.
4. Run `python3 tools/codex_vn_pipeline.py validate`; the expected scene
   results are `OK (65/65)`, `OK (68/68)`, `OK (65/65)`, and `OK (57/57)`.

## Blockers

NONE. The source of truth and exact lossless reindexing map are both
deterministic. Stage ownership still requires the actual translation/QC edits
and their post-repair validation to be performed outside this audit-only lane.
