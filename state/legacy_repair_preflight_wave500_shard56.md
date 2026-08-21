# Wave-500 shard 56 legacy validator repair preflight

Audit only. No translation, QC, arbitration, source, exclusion, pipeline
configuration, or Git artifact was modified.

## Corrected authority and conclusion

This report supersedes the earlier provisional source-omission conclusion.

The supervisor performed a fresh direct extraction of all five scenes from the
verified Full Edition archive at `/tmp/tsuyokiss_data.fpk`. That independent
extraction reproduces the current configured `scratchpad/jp_dumps/` documents:
the same 321 total rows, the same per-scene counts, and the same row payloads and
hashes.

The current raw source is therefore authoritative at:

- `SC_M0184_00_M0190_00`: `1-43`
- `SC_M0210_00_M0211_00`: `1-39`
- `SC_M0225_00_M0230_00`: `1-93`
- `SC_M0301_00_M0310_00`: `1-91`
- `SC_M0320_00_M0330_00`: `1-55`

The five extra English rows belong to a legacy version/index mismatch. They are
not current Full Edition source rows and must not be restored to raw source.
For the first four scenes, deleting the legacy-only interior English row and
shifting all later English keys down by one aligns the remaining translations
with the authoritative Japanese. M0320 requires only deletion of its final
legacy-only English row.

## Policy and artifact inventory

- No canonical or configured-overlay exclusion applies to any target scene.
- No narrative mirror or repeated-choice gate applies.
- No target scene currently has a generated
  `scratchpad/model_sources/<scene>.json` projection.
- Translation JSON, accuracy QC, literary QC, and an arbitration `NONE` record
  exist for all five scenes.
- The existing QC reports use the legacy counts `44/40/94/92/56`; those count
  claims are stale against the verified Full Edition source and require later
  source-aligned recertification. They were not edited in this audit.

No excluded row was inspected.

## Exact minimal translation mapping

| Scene | Authoritative keys | Delete legacy English key | Ungrounded legacy English | Rekey surviving English | Result |
|---|---|---:|---|---|---|
| `SC_M0184_00_M0190_00` | `1-43` | 13 | `「...Thank you.」` | old `14-44` -> new `13-43`; keep old `1-12` unchanged | exact `1-43` |
| `SC_M0210_00_M0211_00` | `1-39` | 21 | `「No way!」` | old `22-40` -> new `21-39`; keep old `1-20` unchanged | exact `1-39` |
| `SC_M0225_00_M0230_00` | `1-93` | 36 | `「Spirit!!!」` | old `37-94` -> new `36-93`; keep old `1-35` unchanged | exact `1-93` |
| `SC_M0301_00_M0310_00` | `1-91` | 63 | `「You're an idiot.」` | old `64-92` -> new `63-91`; keep old `1-62` unchanged | exact `1-91` |
| `SC_M0320_00_M0330_00` | `1-55` | 56 | `But wasn't honestly complimenting her the gentlemanly thing to do?` | none; keep old `1-55` unchanged | exact `1-55` |

These are key moves, not prose rewrites. The string associated with each
surviving old key must be copied unchanged to its specified new key. Build the
replacement `lines` object atomically so a descending/in-place rename cannot
overwrite values.

## Per-scene diagnosis

### `SC_M0184_00_M0190_00`

Legacy English `1-12` already aligns with current raw `1-12`. Legacy English
13 has no current source row. Current raw `13-43` aligns with legacy English
`14-44`, including legacy 44 as the translation of authoritative raw 43's
silent separator. Delete old 13 and shift old `14-44` down one.

### `SC_M0210_00_M0211_00`

Legacy English `1-20` already aligns with current raw `1-20`. Legacy English
21 has no current source row. Current raw `21-39` aligns with legacy English
`22-40`, including legacy 40 as the translation of authoritative raw 39's
silent separator. Delete old 21 and shift old `22-40` down one.

### `SC_M0225_00_M0230_00`

Legacy English `1-35` already aligns with current raw `1-35`. Legacy English
36 has no current source row. Current raw `36-93` aligns with legacy English
`37-94`; legacy 94 is the translation of authoritative raw 93's final
narration. Delete old 36 and shift old `37-94` down one.

### `SC_M0301_00_M0310_00`

Legacy English `1-62` already aligns with current raw `1-62`. Legacy English
63 has no current source row. Current raw `63-91` aligns with legacy English
`64-92`; legacy 92 is the translation of authoritative raw 91's closing
narration. Delete old 63 and shift old `64-92` down one.

### `SC_M0320_00_M0330_00`

Legacy English `1-55` aligns exactly with current raw `1-55`. Legacy English 56
has no current Full Edition row. Delete 56; no surviving key moves.

## Cause

The legacy translation/QC artifacts were banked with one additional line and a
larger claimed span in each scene. The verified FPK extraction proves those
additional lines are version-mismatched or historically drifted content rather
than lost current source.

For the first four scenes, the legacy-only line sits inside the old index
sequence. Consequently, every later valid English line is one key too high and
the validator reports only the final old key as `unknown`. The validator is
behaving correctly; the apparent tail error is the end of an earlier index
shift.

M0320's legacy-only line is already at the tail, so no downstream key shift is
present.

## No-write repair simulation

The exact mapping above was applied in memory only, then checked against the
current authoritative raw documents.

| Scene | Simulated key set | Dialogue wrapper parity | CP932 | Source hashes | Speaker map |
|---|---|---|---|---|---|
| M0184 | exact `1-43` | PASS | PASS | PASS | PASS |
| M0210 | exact `1-39` | PASS | PASS | PASS | PASS |
| M0225 | exact `1-93` | PASS | PASS | PASS | PASS |
| M0301 | exact `1-91` | PASS | PASS | PASS | PASS |
| M0320 | exact `1-55` | PASS | PASS | PASS | PASS |

Aggregate simulated result: 321 exact rows, consisting of 255 dialogue rows and
66 narration rows. There are zero missing, excluded, or unknown keys after the
mapping. All surviving English strings remain unchanged.

## Required follow-up actions

1. Apply the five exact translation delete/rekey mappings above. Do not alter
   source text, source indexes, source hashes, exclusions, or pipeline config.
2. Regenerate filtered model projections from the verified current raw source.
   With no exclusions, they must contain exact sets `1-43`, `1-39`, `1-93`,
   `1-91`, and `1-55`.
3. Perform source-aligned accuracy confirmation over all 321 repaired mappings,
   with special attention to the four shift boundaries and M0320's new hard
   stop at 55.
4. Replace or amend the accuracy and literary QC reports so they state the
   authoritative counts and indexes. Remove claims that the deleted legacy
   keys were source-reviewed. Keep arbitration `NONE` only after the repaired
   source-aligned QC confirms no remaining contested row.
5. Run the overlay-aware deterministic validator and confirm exact index sets,
   duplicate-free JSON, wrapper parity, CP932, source hashes, speaker maps, and
   absence of unknown keys.

## Rejected repairs

- Do not add the five legacy lines to `jp_dumps`; verified FPK extraction proves
  they are absent from the current Full Edition source.
- Do not add exclusions. These are absent/version-mismatched rows, not
  restricted current source content, and no manifest entry applies.
- Do not delete only the validator-reported tail keys in M0184, M0210, M0225,
  or M0301. That would leave the surviving post-drift English mapped one row
  too high and discard a valid current-source translation.
- Do not rewrite surviving prose during the mechanical repair.

## Blockers

Technical blockers: NONE. The authoritative extraction resolves the prior
source uncertainty. Translation and QC edits remain pending only because this
assignment authorizes an audit report, not production artifact changes.
