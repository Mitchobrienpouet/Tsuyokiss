# Wave 200 closure checkpoint: shards 7-10

Recorded: 2026-08-21
Branch: `codex/wave-300-continuation-20260820`

## Shard 7 — DONE

- `SC_G0930_00_G0990_00`: 38/38 permitted rows translated; source-grounded accuracy QC, literary QC, and no-op arbitration complete.
- `SC_G0950_00_G0960_00`: fully excluded by active manifest; no model artifact created.
- `SC_G0960_00_G0970_00`: fully excluded by active manifest; no model artifact created.
- `SC_G0970_00_Z9999_99`: permitted indexes `91-101` translated and source-grounded QC complete; excluded indexes remain absent. Accuracy tightened index 93 to preserve `怖い` as `scary` rather than merely `hurt`.

## Shard 8 — DONE

- `SC_G0990_00_Z9999_99`: 43 permitted rows translated and QC complete.
- Exact permitted set: `1-41,46-47`; indexes `42-45` remain excluded and unbridged.

## Shard 9 — DONE

- `SC_I0100_00_Z9999_99`: 68/68 rows translated and QC complete; no restricted range.

## Shard 10 — DONE

- `SC_J0000_00_J0100_01`: 1/1.
- `SC_J0100_01_J0100_02`: 109/109.
- `SC_J0100_02_J0100_03`: 45/45.
- `SC_J0100_03_J0100_04`: 76/76.
- Total: 231/231 source rows translated, source-grounded accuracy QC complete, literary QC complete, and arbitration recorded as `NONE` for every scene.
- Crossover names are locked as Serori, Tomoe, Takane, Honami, and Poem. The proper title remains `Ane, Chanto Shiyou yo!`.

## Source recovery

Authoritative Japanese rows were recovered locally from the retained Tsuyokiss `data.fpk` archive using the existing toolkit decoder/parser. This removes the prior shard-7 source gate while preserving canonical plus wave-overlay exclusions fail-closed.

## Next claim

Wave 200 shard 11: `SC_J0100_04_J0100_05`, `SC_J0100_05_J0100_06`, `SC_J0100_06_J0100_07`, `SC_J0100_07_J0100_08`.
