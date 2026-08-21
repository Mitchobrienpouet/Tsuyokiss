# Legacy validator repair preflight: wave-500 shard 57

Date: 2026-08-21

Status: **AUDIT COMPLETE -- REPAIR REQUIRED**

This was an audit-only pass. No translation, QC, arbitration, source,
projection, exclusion, configuration, or Git artifact was changed. The only
file written by this pass is this preflight report.

## Safety and source authority

- The canonical exclusion manifest and both configured overlays contain no
  entry for any of the five scenes below. There are no excluded rows in scope.
- Authoritative `scratchpad/jp_dumps`, filtered `scratchpad/model_sources`, and
  packaged `scratchpad/model_shards` agree on every index in scope. The raw and
  filtered structures also agree on engine ID, speaker, kind, Japanese body,
  and source hash for every row compared.
- For `SC_M0375_00_M0380_00:43-44`, row content was inspected **only** through
  the permitted filtered projection. Raw row content was not opened or quoted.
- `narrative_gates.json` declares no source mirror or repeated-choice group.

| Scene | Authoritative projection | Packaged projection | Current target keys | Structural status |
|---|---:|---|---:|---|
| `SC_M0341_00_M0350_00` | 75, exactly `1-75` | `w200-29.json`, exact match | 76, `1-76` | unknown `76` |
| `SC_M0372_00_M0373_00` | 60, exactly `1-60` | `w200-30.json`, exact match | 61, `1-61` | unknown `61`; earlier drift |
| `SC_M0375_00_M0380_00` | 44, exactly `1-44` | `w200-31.json`, exact match | 42, `1-42` | missing `43-44`; earlier collapse |
| `SC_M0382_00_M0383_00` | 182, exactly `1-182` | `w200-32.json`, exact match | 185, `1-185` | unknown `183-185`; three earlier drifts |
| `SC_M0391_00_M0392_00` | 27, exactly `1-27` | `w200-33.json`, exact match | 28, `1-28` | unknown `28`; earlier drift |

## Root cause

The authoritative projections are sound. The legacy target/QC path treated a
contiguous translation key set and the translation's own cardinality as proof
of source coverage instead of joining each key to the filtered projection.
That allowed ungrounded inserted target lines and one three-to-one source-row
collapse to shift later bodies while still producing apparently contiguous
JSON.

The stale accuracy records consequently certify `76/76`, `61/61`, `42/42`,
`185/185`, and `28/28`, even though the authoritative counts are `75`, `60`,
`44`, `182`, and `27`. Wrapper mismatches and the wrong source/target joins
were also missed. The literary records and one-line `NONE` arbitration files
were produced on those invalid joins and cannot serve as completion evidence.

## Scene findings and minimal repair

### `SC_M0341_00_M0350_00`

- Target indexes `1-75` align structurally with projected indexes `1-75`.
- Target `76`, `Konoe working alone, huh...`, has no projected source row,
  engine ID, or source hash. It is an inferred connective after the actual
  final narration, not translation debt.
- Minimal translation repair: delete target `76`; do not shift any earlier row.
- Required routing: independent accuracy QC over exact indexes `1-75`, then
  literary QC, then targeted arbitration (explicit `NONE` if no issue), then
  deterministic validation. Replace the stale `76/76` QC claims.

### `SC_M0372_00_M0373_00`

- Target indexes `1-25` align with projected indexes `1-25`.
- Target `26`, `「Butler Kick!」`, has no projected source row. It was inserted
  between the chair demand and the customer's reaction.
- Because of that insertion, old target `27-61` maps in order to projected
  source `26-60`.
- The existing accuracy correction labeled target `44` belongs to
  authoritative source index `43`; its index must move with the repair.
- Minimal translation repair: delete old target `26`; rekey old `27-61` to
  `26-60`, preserving bodies and wrappers pending QC.
- Required routing: independent accuracy QC over exact indexes `1-60` (with
  the chest-reading decision documented at source index `43`), then literary
  QC, arbitration/no-op record, and deterministic validation. Replace the
  stale `61/61` records.

### `SC_M0375_00_M0380_00`

- Target indexes `1-2` align with projected indexes `1-2`.
- Old target `3` collapses three separately indexed numbered narration rows,
  projected source `3`, `4`, and `5`, into one English body.
- Old target `4-42` therefore maps in order to projected source `6-44`.
- The validator's reported missing `43-44` is only the tail symptom. Their
  source-grounded English already exists at old target `41-42`; it is attached
  to the wrong indexes.
- Permitted-projection metadata for the two reported rows:
  - `43`: narration, null speaker,
    `B0039:SC_M0375_00_M0380_00:0043`, source hash
    `4e1add1d6b816820ad810739db87acfd3da01ab53e219501d68eca20e58c8726`.
  - `44`: narration, null speaker,
    `B0039:SC_M0375_00_M0380_00:0044`, source hash
    `d73d71c1c704feaa5f40601c19eef116c78018c7c5498371d3bc3599b51c7a5c`.
- Minimal translation repair: in a translation-stage repair using only the
  filtered projection, split the current combined procedural body into exact
  source rows `3`, `4`, and `5`; then rekey old target `4-42` to `6-44`.
  Do not invent a new continuation for `43-44` and do not re-open raw content
  for those rows.
- Required routing: accuracy QC over all exact indexes `1-44`, literary QC,
  arbitration/no-op record, and deterministic validation. Replace the stale
  `42/42` records rather than merely editing their stated count.

### `SC_M0382_00_M0383_00`

Three target-only reaction/shout lines caused cumulative drift:

- old target `5`, `「!?」`, has no projected source row;
- old target `30`, `「You three!!」`, has no projected source row;
- old target `134`, `「YOU THREE!!!」`, has no projected source row.

The exact mapping is:

- old `1-4` -> source `1-4`;
- delete old `5`;
- old `6-29` -> source `5-28`;
- delete old `30`;
- old `31-133` -> source `29-131`;
- delete old `134`;
- old `135-185` -> source `132-182`.

Minimal translation repair: remove the three ungrounded bodies and apply the
mapping above. An in-memory simulation produces exact keys `1-182` with zero
dialogue/narration wrapper mismatches.

Required routing: accuracy QC over all `182` source-joined rows, literary QC,
arbitration/no-op record, and deterministic validation. The stale `185/185`
accuracy/literary/arbitration artifacts must not be retained as proof of review.

### `SC_M0391_00_M0392_00`

- Target indexes `1-20` align with projected indexes `1-20`.
- Old target `21`, `「Whaaat!?」`, is an inferred reaction with no projected
  source row.
- Old target `22-28` maps in order to projected source `21-27`.
- Minimal translation repair: delete old target `21`; rekey old `22-28` to
  `21-27`.
- Required routing: accuracy QC over exact indexes `1-27`, literary QC,
  arbitration/no-op record, and deterministic validation. Replace the stale
  `28/28` records.

## Repair order and gates

1. Repair translation indexing from the filtered model projections only.
   Preserve the existing `speaker_map`, source meaning, dialogue wrappers, and
   CP932-safe typography. Do not change raw dumps, model projections,
   exclusions, gates, or configuration.
2. Run independent accuracy QC on every repaired scene. Full-scene review is
   required because the previous records compared many bodies to the wrong
   source index.
3. Run literary QC only after the corrected accuracy pass.
4. Regenerate targeted arbitration records, including an explicit no-op where
   appropriate. Do not carry forward the legacy one-line `NONE` as validation.
5. Run deterministic gates against the filtered projections:
   - exact counts and key sets: `75`, `60`, `44`, `182`, `27`;
   - no unknown or missing indexes and no duplicate keys;
   - dialogue/narration wrapper parity and exact speaker-map key coverage;
   - stable engine IDs and source hashes on the source join;
   - CP932 encodability and forbidden-typography checks;
   - required accuracy, literary, and arbitration artifacts present.

The proposed in-memory delete/reindex/split mapping yields each exact source
key set and zero wrapper mismatches. Semantic approval remains intentionally
routed through the new accuracy and literary passes.

## Blockers

NONE. The filtered projections contain every row needed for repair, including
`SC_M0375_00_M0380_00:43-44`; no exclusion, mirror, or missing-source blocker
exists.
