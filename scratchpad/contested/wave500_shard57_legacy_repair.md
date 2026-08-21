# Wave-500 shard 57 legacy translation repair handoff

Stage: translation repair only. This file records the exact source-alignment
changes made from the authoritative filtered projections. Existing accuracy,
literary, and arbitration artifacts were intentionally left untouched and are
stale pending fresh post-repair review.

No exclusion applies to these scenes. No raw source, filtered projection,
configuration, state, QC, arbitration, or Git artifact was edited.

## Exact mapping

### `SC_M0341_00_M0350_00`

- Preserved old target `1-75` at new target `1-75`.
- Deleted old target `76`: `Konoe working alone, huh...`
  - Reason: no filtered source index, engine ID, or source hash exists for it.
- Final target set: exactly `1-75` (`75` rows).

### `SC_M0372_00_M0373_00`

- Preserved old target `1-25` at new target `1-25`.
- Deleted old target `26`: `「Butler Kick!」`
  - Reason: no filtered source row exists for this inferred attack call.
- Rekeyed old target `27-61` to new target `26-60` without changing bodies.
- The previously corrected chest-reading body moved from old target `44` to
  authoritative target `43` as part of that rekey.
- Final target set: exactly `1-60` (`60` rows).

### `SC_M0375_00_M0380_00`

- Preserved old target `1-2` at new target `1-2`.
- Replaced the collapsed old target `3`:
  - Before: `First, apply rust inhibitor. Second, wait for it to dry and paint over it. Third, finished... apparently.`
  - New `3`: `First, apply a base coat of rust inhibitor.`
    - Source index/hash: `3` /
      `f65c68b09abd0f0510302dc9c20caaa6597f9edcb69199daf467b92725ea5821`.
  - New `4`: `Second, paint it after that dries.`
    - Source index/hash: `4` /
      `20e3b6749306d0c0375372e75268f0bddb01cbf802d341820de29329cb59b804`.
  - New `5`: `Third, it should be finished... apparently.`
    - Source index/hash: `5` /
      `07763a279b7bdd25fa76e33b7d6db8ab5976e39f0f4ae5940daf12f85007ca0b`.
- Rekeyed old target `4-42` to new target `6-44` without changing bodies.
  In particular, old `41-42` became source-aligned `43-44`; no connective or
  new ending was invented.
- Final target set: exactly `1-44` (`44` rows).

The new procedural lines preserve the numbered three-step sequence.
`apply a base coat of rust inhibitor` is the adopted rendering of
`サビ止め剤を下塗り`; `undercoat it with rust inhibitor` is a defensible but
non-blocking alternative for later accuracy/literary review. `apparently`
preserves Leo's uncertainty at source index `5`.

### `SC_M0382_00_M0383_00`

- Preserved old target `1-4` at new target `1-4`.
- Deleted old target `5`: `「!?」` (no filtered source row).
- Rekeyed old target `6-29` to new target `5-28`.
- Deleted old target `30`: `「You three!!」` (no filtered source row).
- Rekeyed old target `31-133` to new target `29-131`.
- Deleted old target `134`: `「YOU THREE!!!」` (no filtered source row).
- Rekeyed old target `135-185` to new target `132-182`.
- Final target set: exactly `1-182` (`182` rows).

### `SC_M0391_00_M0392_00`

- Preserved old target `1-20` at new target `1-20`.
- Deleted old target `21`: `「Whaaat!?」`
  - Reason: no filtered source row exists for this inferred reaction.
- Rekeyed old target `22-28` to new target `21-27` without changing bodies.
- Final target set: exactly `1-27` (`27` rows).

## Post-repair routing

All five scenes require fresh full-scene accuracy QC, then literary QC, then
targeted arbitration or an explicit no-op. The legacy QC/arbitration files must
not be treated as proof of source-aligned review.

Blocking contested readings: NONE.
