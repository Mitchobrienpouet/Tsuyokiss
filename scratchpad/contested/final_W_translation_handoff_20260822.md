# Final W Translation Handoff — 2026-08-22

## Scope

- Translation stage only: eight filtered W projections, 44 permitted rows total.
- `SC_W0100_20_Z9999_99` contains only permitted indexes 1 and 5. Excluded indexes were not accessed or reconstructed, and no connective text was added across either gap.
- No source, exclusion, gate, pipeline, QC, arbitration, readthrough, or state artifact was changed.

## Output cardinality

| Scene | Permitted indexes | Rows |
| --- | --- | ---: |
| `SC_W0100_00_W0110_00` | 1-3 | 3 |
| `SC_W0100_10_W0210_00` | 1-3 | 3 |
| `SC_W0100_20_Z9999_99` | 1, 5 | 2 |
| `SC_W0100_30_W0410_00` | 1-2 | 2 |
| `SC_W0110_10_Z9999_99` | 1-27 | 27 |
| `SC_W0110_20_Z9999_99` | 1-2 | 2 |
| `SC_W0210_20_Z9999_99` | 1-2 | 2 |
| `SC_W0410_20_Z9999_99` | 1-3 | 3 |
| **Total** |  | **44** |

## Locked decisions

- `SC_W0100_30_W0410_00:1` and `SC_W0410_20_Z9999_99:2` use the byte-identical callback `「This is Tutorial Village.」`.
- `大きいお友達` at `SC_W0100_00_W0110_00:1` is localized as "grown-up fans," preserving the adult-fan euphemism rather than implying physical size.
- `子蟹ちゃん` at `SC_W0110_10_Z9999_99:4` is rendered as "little crab," preserving the playful one-off diminutive rather than replacing the established direct-address name `Crab` globally.
- Tutorial terminology is consistent: route, character story, ending, map, keyboard settings, screen size, quick-save, panic button, F5, and main game.

## Materially contested permitted readings

1. `SC_W0100_10_W0210_00:2-3` — The false-kanji phonetic joke `中途現実` has no exact English sound match. The adopted pair keeps the bogus orthography and melancholy "halfway to reality" meaning, with Subaru immediately rejecting it. Later QC may prefer a more strongly phonetic adaptation if it can retain both functions without adding lore.
2. `SC_W0210_20_Z9999_99:1-2` — The `聞かん坊` / `機関坊` homophone is adapted as "ornery kid" / "machinery kid." This preserves the scolding setup, Kinu's machine-word mishearing, and her alarm, but the English relation is a near-rhyme rather than an exact homophone.

No other permitted reading remained materially contested at translation handoff.
