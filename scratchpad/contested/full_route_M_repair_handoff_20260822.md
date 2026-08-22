# Route M critical-readthrough repair handoff

- Date: 2026-08-22
- Stage: targeted translation repair after critical readthrough
- Input findings: `M-RT-001` through `M-RT-005` from `scratchpad/readthrough/full_route_M_critical_20260822.md`
- Status: COMPLETE
- Translation files changed: 11
- Permitted line bodies changed: 7
- Speaker-map values changed: 4 files / 17 displayed speaker rows
- Directly contradictory specs changed: 1
- Contested readings: NONE

## Adopted line repairs

| Finding | Scene/index | Before | After | Basis |
|---|---|---|---|---|
| `M-RT-001` | `SC_M0430_00_M0431_00:37` | `Murata took off without a second of hesitation.` | `「That Murata took off without a second's hesitation.」` | Restores the source dialogue wrapper and Leo's rough `村田の奴` register. |
| `M-RT-002` | `SC_M0270_00_M0271_00:27` | `A lecture hell!` | `$LA lecture hell!` | Restores the source's leading `$L` engine control exactly at the start of the translated caption. |
| `M-RT-003` | `SC_M0283_00_M0290_00:17` | `「Yes. Everyone is busy preparing for the sports and martial arts festival.」` | `「Yes. Everyone is busy preparing for the Sports and Martial Arts Festival.」` | Applies the locked proper-event title for `体育武道祭`. |
| `M-RT-003` | `SC_M0290_00_M0291_00:17` | `「To commemorate making up with her, could you help the drama club--help Konoe--until the sports and martial arts festival is over?」` | `「To commemorate making up with her, could you help the drama club--help Konoe--until the Sports and Martial Arts Festival is over?」` | Applies the locked proper-event title for `体育武道祭`. |
| `M-RT-003` | `SC_M0291_00_M0300_00:55` | `「All right, everyone. Let's summarize the drama club's situation for the sports and martial arts festival.」` | `「All right, everyone. Let's summarize the drama club's situation for the Sports and Martial Arts Festival.」` | Applies the locked proper-event title for `体育武道祭`. |
| `M-RT-003` | `SC_M0320_00_M0330_00:2` | `It was the academy's foundation day, so classes were off, but many students had come voluntarily to prepare for the sports and martial arts festival.` | `It was the academy's foundation day, so classes were off, but many students had come voluntarily to prepare for the Sports and Martial Arts Festival.` | Applies the locked proper-event title for `体育武道祭`. |
| `M-RT-005` | `SC_M0640_00_M0650_00:12` | `「Go traumatized me.」` | `「I'm traumatized by Go.」` | Keeps Kinu's meaning while making `Go` unambiguously the board game and restoring natural English. |

## Speaker-map repair

The Japanese speaker key `土永さん` now maps from `Tsuchinaga-san` to canonical `Mr. Tsuchinaga` in exactly these files:

| Scene | Affected permitted speaker rows |
|---|---|
| `SC_M0340_00_M0341_00` | 2, 4, 6, 8, 9, 12, 14, 16 |
| `SC_M0411_00_M0412_00` | 6, 8, 9, 17, 41, 51 |
| `SC_M0432_00_M0440_00` | 84, 87 |
| `SC_M0530_00_M0540_00` | 4 |

This repair changes four display-map values and therefore 17 displayed speaker labels. Two contextual line-body uses of `Tsuchinaga-san` were not part of the finding and remain untouched; the stale-form gate below applies to speaker-map values.

## Directly contradictory continuity lock

`scratchpad/specs/wave200_shard38.md` had two prose references that treated `Tsuchinaga-san` as the locked display rendering. Both now read `Mr. Tsuchinaga`. No other spec was changed.

## Files changed

- `translations/SC_M0270_00_M0271_00.json`
- `translations/SC_M0283_00_M0290_00.json`
- `translations/SC_M0290_00_M0291_00.json`
- `translations/SC_M0291_00_M0300_00.json`
- `translations/SC_M0320_00_M0330_00.json`
- `translations/SC_M0340_00_M0341_00.json`
- `translations/SC_M0411_00_M0412_00.json`
- `translations/SC_M0430_00_M0431_00.json`
- `translations/SC_M0432_00_M0440_00.json`
- `translations/SC_M0530_00_M0540_00.json`
- `translations/SC_M0640_00_M0650_00.json`
- `scratchpad/specs/wave200_shard38.md`
- `scratchpad/contested/full_route_M_repair_handoff_20260822.md`

## Deterministic validation

| Gate | Result |
|---|---|
| Strict JSON / duplicate keys | PASS |
| Route-M translation/projection scene set | PASS - 156/156 |
| Exact permitted index joins | PASS - 6,366/6,366 |
| Opaque partial exclusions | PASS - 270 rows absent |
| Source hashes | PASS - 6,366/6,366 |
| Engine IDs | PASS - 6,366 unique and source-label aligned |
| Internal `file` identity | PASS - 156/156 |
| Speaker-map source-key coverage | PASS |
| Dialogue wrappers | PASS - zero mismatches |
| `$L`/`$M`/`$S` source controls | PASS - zero mismatches |
| CP932 translation values and maps | PASS |
| Forbidden target typography / Japanese residue | PASS |
| Stale `Tsuchinaga-san` speaker-map values | PASS - zero |
| Lowercase full `sports and martial arts festival` target forms | PASS - zero |
| Stale `Samehyo` / `Samehyou` / `Samejima` target forms | PASS - zero |

No QC, arbitration, readthrough, source/projection, exclusion, configuration, pipeline/state, or Git artifact was modified.
