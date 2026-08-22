# Critical full-route speed readthrough: route M

- Date: 2026-08-22
- Stage: post-QC critical readthrough (read-only)
- Verdict: **PASS / closed after repair, independent QC, and targeted arbitration**
- Reviewed corpus: **156 translation files / 6,366 permitted rows**
- Filtered projection ledger: **156 projections / 6,366 permitted rows / 270 opaque excluded gap rows**
- Fully excluded zero-debt boundary: **10 scenes / 895 opaque rows**
- Finding count: **5 closed** (**2 major, 3 minor**)
- Runtime or story-image claim: **NONE**

## Scope and method

I read every permitted English row continuously in scene order, from `SC_M0100_00_K0900_00:1` through `SC_M0690_00_Z9999_99:45`. Suspicions were checked only against the public overlay-aware files in `scratchpad/model_sources/SC_M*.json`, plus the project bible, glossary/style locks, narrative gates, and existing accuracy/literary records. I did not open, infer, bridge, or summarize excluded rows.

The read covered the route's school-life opening, middle-school flashback, Sunao/Leo feud, Hakkeijima truce, drama-club and Sports and Martial Arts Festival arc, reconciliation, examinations, opaque island boundaries, confession and dating arc, script contest, and open coda. Branch entrances, convergence points, scene transitions, and reveal order were followed in translation-file order.

This is a static text/projection audit. No engine was executed; textbox, backlog, line wrapping, timing, input flow, and rendered assets remain unverified. This report makes no runtime or scene-image localization claim.

## Deterministic corpus gates

| Gate | Result | Evidence |
|---|---|---|
| Translation/projection scene set | PASS | 156 translation stems exactly equal 156 filtered projection stems |
| Exact permitted indexes | PASS | 6,366/6,366 translation keys join one-to-one with projection rows; sparse sets retained |
| Exclusion accounting | PASS | 270 projection-declared gap rows; 895 additional fully excluded zero-debt rows kept opaque |
| Strict JSON/schema | PASS | No duplicate keys; translation objects retain only `file`, `speaker_map`, and `lines` |
| Internal `file` identity | PASS | 156/156 values equal the filename/scene stem |
| Projection scene/source identity | PASS | 156/156 scene labels and source-label prefixes align |
| Source hashes | PASS | SHA-256 recomputed from all 6,366 permitted Japanese strings; 6,366/6,366 match |
| Engine IDs | PASS | 6,366 present, 6,366 unique, each aligned to its authoritative projection source label |
| Speaker-map key coverage | PASS | Every source speaker key is mapped once per scene; no extra keys |
| CP932 | PASS | All translated lines and speaker-map values encode successfully |
| Forbidden target typography | PASS | No curly quotes, em dashes, or Unicode ellipses |
| Japanese-script residue/placeholders | PASS | No residual Japanese script, TODO/TBD/FIXME, replacement characters, or template placeholders in target lines |
| Dialogue wrappers | PASS after repair | Zero mismatches; `SC_M0430_00_M0431_00:37` restored |
| Source control markers | PASS after repair | `$L` restored at `SC_M0270_00_M0271_00:27` |
| Stale Shinichi surnames | PASS | Zero `Samehyo`, `Samehyou`, or `Samejima`; `Samesuga` is stable |
| Accuracy/literary report inventory | PASS | 156 accuracy and 156 literary reports exactly cover the translated scene set |

The public mutating pipeline entrypoint was not invoked because this lane forbids pipeline/state edits. The checks above were run with a read-only projection-to-translation validator.

## Critical findings

### M-RT-001 - Major - dialogue wrapper / presentation

- Location: `SC_M0430_00_M0431_00:37`
- Speaker/source kind: Leo / dialogue
- Permitted source: `「村田の奴、迷いなく走りやがって」`
- Current target: `Murata took off without a second of hesitation.`
- Diagnosis: the target drops the mandatory `「...」` dialogue wrapper, causing a spoken Leo line to present as narration. It also flattens the rough `村田の奴` register.
- Minimal repair direction: `「That Murata took off without a second's hesitation.」`
- Systemic: no. This is the only route-M wrapper mismatch.
- Status: CLOSED.

### M-RT-002 - Major - lost engine control marker

- Location: `SC_M0270_00_M0271_00:27`
- Permitted source: `$L説教地獄だ！`
- Current target: `A lecture hell!`
- Diagnosis: the leading `$L` control marker is absent. Other certified route files preserve this marker byte-for-byte, and no route-M spec authorizes stripping it.
- Minimal repair direction: retain the current wording but restore the prefix: `$LA lecture hell!`
- Systemic: no. This is the only source/target control-token mismatch in route M.
- Status: CLOSED.

### M-RT-003 - Minor - locked event-name capitalization

Four source references to `体育武道祭` use the generic lowercase phrase instead of the locked proper name `Sports and Martial Arts Festival`.

| Location | Current target |
|---|---|
| `SC_M0283_00_M0290_00:17` | `「Yes. Everyone is busy preparing for the sports and martial arts festival.」` |
| `SC_M0290_00_M0291_00:17` | `「To commemorate making up with her, could you help the drama club--help Konoe--until the sports and martial arts festival is over?」` |
| `SC_M0291_00_M0300_00:55` | `「All right, everyone. Let's summarize the drama club's situation for the sports and martial arts festival.」` |
| `SC_M0320_00_M0330_00:2` | `It was the academy's foundation day, so classes were off, but many students had come voluntarily to prepare for the sports and martial arts festival.` |

- Repair direction: capitalize only the event name in these four rows: `Sports and Martial Arts Festival`.
- Systemic: yes, four rows. Shortened source `体育祭` at `M0263:1,11` is not included; those are not full-name occurrences.
- Status: CLOSED.

### M-RT-004 - Minor - Tsuchinaga speaker-map drift

The same Japanese speaker key `土永さん` is canonically mapped as `Mr. Tsuchinaga` in seven route-M scenes, but four maps retain `Tsuchinaga-san`.

| Scene | Affected permitted speaker rows | Current map | Required map |
|---|---|---|---|
| `SC_M0340_00_M0341_00` | 2, 4, 6, 8, 9, 12, 14, 16 | `Tsuchinaga-san` | `Mr. Tsuchinaga` |
| `SC_M0411_00_M0412_00` | 6, 8, 9, 17, 41, 51 | `Tsuchinaga-san` | `Mr. Tsuchinaga` |
| `SC_M0432_00_M0440_00` | 84, 87 | `Tsuchinaga-san` | `Mr. Tsuchinaga` |
| `SC_M0530_00_M0540_00` | 4 | `Tsuchinaga-san` | `Mr. Tsuchinaga` |

- Diagnosis: this is display-name metadata drift, not a source speaker mismatch. Seventeen displayed speaker rows are affected through four map values.
- Repair direction: normalize only those four map values to `Mr. Tsuchinaga`.
- Systemic: yes, four translation files / 17 displayed speaker rows.
- Status: CLOSED.

### M-RT-005 - Minor - obvious literary ambiguity

- Location: `SC_M0640_00_M0650_00:12`
- Speaker: Kinu
- Permitted source: `「碁のトラウマがあるんだよボクは」`
- Current target: `「Go traumatized me.」`
- Diagnosis: although capitalized, sentence-initial `Go` reads like an imperative before it reads as the board game, and the construction is unnaturally terse for Kinu's stated trauma.
- Minimal repair direction: `「I'm traumatized by Go.」`
- Systemic: no.
- Status: CLOSED.

## Source-checked suspicions cleared

- `SC_M0383_00_M0384_00:57-60`: the projection supports Leo's self-deprecating reassessment of his middle-school guilt. The current `like me` reading is defensible and does not independently reassign the route's established attack chronology; no finding retained.
- `SC_M0664_00_M0665_00:24,25,34,54`: the local target tense movement follows the permitted source's own present/past shifts and does not reorder action; no finding retained.
- `SC_M0184_00_M0190_00:13`: the authoritative post-repair projection contains no omitted thank-you row at this point; the apparent discontinuity is not translation debt.
- `SC_M0680_00_M0681_00`: 120 printed copies and 101 judges are not contradictory; the projection explicitly distinguishes copies from ballots/judges.
- `SC_M0572_00_M0573_00`, `SC_M0604_00_M0605_00`, `SC_M0609_00_M0610_00`, `SC_M0610_00_M0611_00`, `SC_M0650_00_M0660_00`, `SC_M0661_00_M0662_00`, `SC_M0664_00_M0665_00`, `SC_M0665_00_M0666_00`, and `SC_M0671_00_M0680_00`: abrupt joins coincide with certified opaque gaps and were not bridged or reconstructed.

## Route-level continuity assessment

| Area | Result | Notes |
|---|---|---|
| Hallucination / omission | PASS | No source-verified hallucination or permitted-row omission retained after suspicion checks |
| Character voice | PASS with one minor defect | Sunao's earnest force, Leo's defensive humor and gradual recommitment, Kinu's energy, Otome's authority, and Erika's teasing remain distinguishable; M0640:12 needs naturalization |
| Agency and relationship progression | PASS | Middle-school guilt, drama-club decisions, reconciliation, confession, handholding, kiss, and public couple reveal preserve actor and order |
| Reveal timing | PASS | Past conflict, truce, renewed cooperation, romance, and public relationship knowledge are not disclosed early |
| Chronology | PASS | June school arc, festival preparation, examinations, summer/island boundaries, Port Opening Festival, and September Ryuumei Festival progress coherently |
| Branches and opaque boundaries | PASS | Sparse joins remain visibly discontinuous; fully excluded scenes carry zero translation debt |
| Names and lore | PASS with minor metadata drift | Samesuga, Matsukasa Port Opening Festival, and Ryuumei Festival are stable; official event capitalization and Tsuchinaga display maps require normalization |
| Engine presentation | PASS after repair | Dialogue wrapper and `$L` control restored |
| Ending | PASS | The script-contest sequence and open coda remain unresolved where the source remains unresolved |

## Exact permitted coverage

| # | Scene | Permitted indexes | Permitted | Excluded gap rows |
|---:|---|---|---:|---:|
| 1 | `SC_M0100_00_K0900_00` | 1-47 | 47 | 0 |
| 2 | `SC_M0110_00_M0110_10` | 1-39 | 39 | 0 |
| 3 | `SC_M0110_10_M0110_20` | 1-29 | 29 | 0 |
| 4 | `SC_M0110_20_M0110_30` | 1-2 | 2 | 0 |
| 5 | `SC_M0110_30_K0900_00` | 1-13 | 13 | 0 |
| 6 | `SC_M0120_00_M0120_10` | 1-26 | 26 | 0 |
| 7 | `SC_M0120_20_K0900_00` | 1-49 | 49 | 0 |
| 8 | `SC_M0130_00_M0130_10` | 1-15 | 15 | 0 |
| 9 | `SC_M0130_30_K0900_00` | 1-50 | 50 | 0 |
| 10 | `SC_M0140_00_M0141_00` | 1-7 | 7 | 0 |
| 11 | `SC_M0142_00_M0150_00` | 1-10 | 10 | 0 |
| 12 | `SC_M0150_00_M0151_00` | 1-17 | 17 | 0 |
| 13 | `SC_M0152_00_M0153_00` | 1-12 | 12 | 0 |
| 14 | `SC_M0153_00_M0154_00` | 1-50 | 50 | 0 |
| 15 | `SC_M0154_00_M0155_00` | 1-9 | 9 | 0 |
| 16 | `SC_M0155_00_M0156_00` | 1-27 | 27 | 0 |
| 17 | `SC_M0156_00_M0157_00` | 1-19 | 19 | 0 |
| 18 | `SC_M0157_00_M0160_00` | 1-51 | 51 | 0 |
| 19 | `SC_M0170_00_M0171_00` | 1-15 | 15 | 0 |
| 20 | `SC_M0171_00_M0180_00` | 1-13 | 13 | 0 |
| 21 | `SC_M0180_00_M0181_00` | 1-84 | 84 | 0 |
| 22 | `SC_M0181_00_M0182_00` | 1-30 | 30 | 0 |
| 23 | `SC_M0182_00_M0183_00` | 1-121 | 121 | 0 |
| 24 | `SC_M0183_00_M0184_00` | 1-58 | 58 | 0 |
| 25 | `SC_M0184_00_M0190_00` | 1-43 | 43 | 0 |
| 26 | `SC_M0190_00_M0200_00` | 1-12 | 12 | 0 |
| 27 | `SC_M0202_00_M0203_00` | 1-15 | 15 | 0 |
| 28 | `SC_M0203_00_M0210_00` | 1-33 | 33 | 0 |
| 29 | `SC_M0210_00_M0211_00` | 1-39 | 39 | 0 |
| 30 | `SC_M0211_00_M0220_00` | 1-9 | 9 | 0 |
| 31 | `SC_M0220_00_M0221_00` | 1-41 | 41 | 0 |
| 32 | `SC_M0221_00_M0222_00` | 1-37 | 37 | 0 |
| 33 | `SC_M0222_00_M0223_00` | 1-16 | 16 | 0 |
| 34 | `SC_M0223_00_M0224_00` | 1-37 | 37 | 0 |
| 35 | `SC_M0224_00_M0225_00` | 1-14 | 14 | 0 |
| 36 | `SC_M0225_00_M0230_00` | 1-93 | 93 | 0 |
| 37 | `SC_M0230_00_M0240_00` | 1-7 | 7 | 0 |
| 38 | `SC_M0240_00_M0241_00` | 1-26 | 26 | 0 |
| 39 | `SC_M0241_00_M0250_00` | 1-67 | 67 | 0 |
| 40 | `SC_M0250_00_M0251_00` | 1-18 | 18 | 0 |
| 41 | `SC_M0251_00_M0260_00` | 1-47 | 47 | 0 |
| 42 | `SC_M0260_00_M0261_00` | 1-12 | 12 | 0 |
| 43 | `SC_M0261_00_M0262_00` | 1-43 | 43 | 0 |
| 44 | `SC_M0262_00_M0263_00` | 1-45 | 45 | 0 |
| 45 | `SC_M0263_00_M0270_00` | 1-21 | 21 | 0 |
| 46 | `SC_M0270_00_M0271_00` | 1-41 | 41 | 0 |
| 47 | `SC_M0271_00_M0272_00` | 1-15 | 15 | 0 |
| 48 | `SC_M0272_00_M0280_00` | 1-76 | 76 | 0 |
| 49 | `SC_M0280_00_M0281_00` | 1-53 | 53 | 0 |
| 50 | `SC_M0281_00_M0282_00` | 1-29 | 29 | 0 |
| 51 | `SC_M0282_00_M0283_00` | 1-19 | 19 | 0 |
| 52 | `SC_M0283_00_M0290_00` | 1-18 | 18 | 0 |
| 53 | `SC_M0290_00_M0291_00` | 1-42 | 42 | 0 |
| 54 | `SC_M0291_00_M0300_00` | 1-93 | 93 | 0 |
| 55 | `SC_M0300_00_M0301_00` | 1-79 | 79 | 0 |
| 56 | `SC_M0301_00_M0310_00` | 1-91 | 91 | 0 |
| 57 | `SC_M0310_00_M0320_00` | 1-100 | 100 | 0 |
| 58 | `SC_M0320_00_M0330_00` | 1-55 | 55 | 0 |
| 59 | `SC_M0330_10_M0340_00` | 1-6 | 6 | 0 |
| 60 | `SC_M0330_20_M0340_00` | 1 | 1 | 0 |
| 61 | `SC_M0340_00_M0341_00` | 1-17 | 17 | 0 |
| 62 | `SC_M0341_00_M0350_00` | 1-75 | 75 | 0 |
| 63 | `SC_M0350_10_M0360_00` | 1-6 | 6 | 0 |
| 64 | `SC_M0350_20_M0360_00` | 1-2 | 2 | 0 |
| 65 | `SC_M0360_00_M0370_00` | 1-3 | 3 | 0 |
| 66 | `SC_M0370_00_M0371_00` | 1-22 | 22 | 0 |
| 67 | `SC_M0371_00_M0372_00` | 1-90 | 90 | 0 |
| 68 | `SC_M0372_00_M0373_00` | 1-60 | 60 | 0 |
| 69 | `SC_M0373_00_M0374_00` | 1-53 | 53 | 0 |
| 70 | `SC_M0374_00_M0375_00` | 1-114 | 114 | 0 |
| 71 | `SC_M0375_00_M0380_00` | 1-44 | 44 | 0 |
| 72 | `SC_M0380_00_M0381_00` | 1-41 | 41 | 0 |
| 73 | `SC_M0381_00_M0382_00` | 1-33 | 33 | 0 |
| 74 | `SC_M0382_00_M0383_00` | 1-182 | 182 | 0 |
| 75 | `SC_M0383_00_M0384_00` | 1-130 | 130 | 0 |
| 76 | `SC_M0384_00_M0390_00` | 1-37 | 37 | 0 |
| 77 | `SC_M0390_00_M0391_00` | 1-11 | 11 | 0 |
| 78 | `SC_M0391_00_M0392_00` | 1-27 | 27 | 0 |
| 79 | `SC_M0392_00_M0400_00` | 1-42 | 42 | 0 |
| 80 | `SC_M0400_00_M0410_00` | 1-29 | 29 | 0 |
| 81 | `SC_M0410_00_M0411_00` | 1-36 | 36 | 0 |
| 82 | `SC_M0411_00_M0412_00` | 1-53 | 53 | 0 |
| 83 | `SC_M0412_00_M0420_00` | 1-15 | 15 | 0 |
| 84 | `SC_M0420_00_M0430_00` | 1-27 | 27 | 0 |
| 85 | `SC_M0430_00_M0431_00` | 1-85 | 85 | 0 |
| 86 | `SC_M0431_00_M0432_00` | 1-65 | 65 | 0 |
| 87 | `SC_M0432_00_M0440_00` | 1-100 | 100 | 0 |
| 88 | `SC_M0440_00_M0450_00` | 1-23 | 23 | 0 |
| 89 | `SC_M0450_00_M0460_00` | 1-58 | 58 | 0 |
| 90 | `SC_M0460_00_M0470_00` | 1-29 | 29 | 0 |
| 91 | `SC_M0470_00_M0471_00` | 1-68 | 68 | 0 |
| 92 | `SC_M0471_00_M0480_00` | 1-60 | 60 | 0 |
| 93 | `SC_M0480_00_M0490_00` | 1-18 | 18 | 0 |
| 94 | `SC_M0490_00_M0500_00` | 1-56 | 56 | 0 |
| 95 | `SC_M0500_00_M0501_00` | 1-65 | 65 | 0 |
| 96 | `SC_M0501_00_M0510_00` | 1-22 | 22 | 0 |
| 97 | `SC_M0510_00_M0520_00` | 1-32 | 32 | 0 |
| 98 | `SC_M0520_00_M0530_00` | 1-57 | 57 | 0 |
| 99 | `SC_M0530_00_M0540_00` | 1-29 | 29 | 0 |
| 100 | `SC_M0540_00_M0550_00` | 1-28 | 28 | 0 |
| 101 | `SC_M0550_00_M0551_00` | 1-24 | 24 | 0 |
| 102 | `SC_M0551_00_M0552_00` | 1-25 | 25 | 0 |
| 103 | `SC_M0552_00_M0553_00` | 1-21 | 21 | 0 |
| 104 | `SC_M0553_00_M0554_00` | 1-18 | 18 | 0 |
| 105 | `SC_M0554_00_M0555_00` | 1, 25-30 | 7 | 23 |
| 106 | `SC_M0555_00_M0556_00` | 1-34 | 34 | 0 |
| 107 | `SC_M0556_00_M0557_00` | 21-99 | 79 | 20 |
| 108 | `SC_M0557_00_M0558_00` | 1-17 | 17 | 0 |
| 109 | `SC_M0558_00_M0559_00` | 1-43 | 43 | 0 |
| 110 | `SC_M0559_00_M0560_00` | 1-170 | 170 | 0 |
| 111 | `SC_M0560_00_M0561_00` | 1-85 | 85 | 0 |
| 112 | `SC_M0561_00_M0562_00` | 1-79 | 79 | 0 |
| 113 | `SC_M0562_00_M0563_00` | 1-19 | 19 | 0 |
| 114 | `SC_M0563_00_M0564_00` | 1-23 | 23 | 0 |
| 115 | `SC_M0564_00_M0565_00` | 1-30 | 30 | 0 |
| 116 | `SC_M0565_00_M0566_00` | 1-33 | 33 | 0 |
| 117 | `SC_M0566_00_M0567_00` | 1-25 | 25 | 0 |
| 118 | `SC_M0568_00_M0569_00` | 60-63 | 4 | 59 |
| 119 | `SC_M0569_00_M0570_00` | 5-9 | 5 | 4 |
| 120 | `SC_M0570_00_M0571_00` | 13-15 | 3 | 12 |
| 121 | `SC_M0571_00_M0572_00` | 1-36 | 36 | 0 |
| 122 | `SC_M0572_00_M0573_00` | 1-13, 15, 17-26 | 24 | 2 |
| 123 | `SC_M0573_00_M0580_00` | 1-12, 19-22 | 16 | 6 |
| 124 | `SC_M0580_00_M0581_00` | 1-13 | 13 | 0 |
| 125 | `SC_M0581_00_M0590_00` | 1-38 | 38 | 0 |
| 126 | `SC_M0590_00_M0600_00` | 1-31, 33-64 | 63 | 1 |
| 127 | `SC_M0600_00_M0601_00` | 1-71 | 71 | 0 |
| 128 | `SC_M0601_00_M0602_00` | 1-25 | 25 | 0 |
| 129 | `SC_M0602_00_M0603_00` | 1-35 | 35 | 0 |
| 130 | `SC_M0603_00_M0604_00` | 1-61 | 61 | 0 |
| 131 | `SC_M0604_00_M0605_00` | 1-32, 41 | 33 | 8 |
| 132 | `SC_M0605_00_M0606_00` | 1-51 | 51 | 0 |
| 133 | `SC_M0606_00_M0607_00` | 1-47 | 47 | 0 |
| 134 | `SC_M0607_00_M0608_00` | 1-16 | 16 | 0 |
| 135 | `SC_M0608_00_M0609_00` | 1-54 | 54 | 12 |
| 136 | `SC_M0609_00_M0610_00` | 21-49 | 29 | 20 |
| 137 | `SC_M0610_00_M0611_00` | 1-36, 50 | 37 | 13 |
| 138 | `SC_M0611_00_M0612_00` | 1-10 | 10 | 5 |
| 139 | `SC_M0620_00_M0621_00` | 1-50 | 50 | 0 |
| 140 | `SC_M0621_00_M0622_00` | 1-10 | 10 | 0 |
| 141 | `SC_M0622_00_M0630_00` | 1-81 | 81 | 0 |
| 142 | `SC_M0630_20_M0640_00` | 1-5 | 5 | 0 |
| 143 | `SC_M0640_00_M0650_00` | 1-46 | 46 | 0 |
| 144 | `SC_M0650_00_M0660_00` | 1-41 | 41 | 24 |
| 145 | `SC_M0660_00_M0661_00` | 1-10 | 10 | 0 |
| 146 | `SC_M0661_00_M0662_00` | 1-30 | 30 | 13 |
| 147 | `SC_M0664_00_M0665_00` | 1-9, 14-56, 59-62 | 56 | 6 |
| 148 | `SC_M0665_00_M0666_00` | 1-15, 23-39, 44-70 | 59 | 11 |
| 149 | `SC_M0666_00_M0670_00` | 1-28 | 28 | 0 |
| 150 | `SC_M0670_00_M0671_00` | 1-15 | 15 | 0 |
| 151 | `SC_M0671_00_M0680_00` | 1-22, 54-61 | 30 | 31 |
| 152 | `SC_M0680_00_M0681_00` | 1-77 | 77 | 0 |
| 153 | `SC_M0681_00_M0682_00` | 1-32 | 32 | 0 |
| 154 | `SC_M0682_00_M0683_00` | 1-70 | 70 | 0 |
| 155 | `SC_M0683_00_M0690_00` | 1-148 | 148 | 0 |
| 156 | `SC_M0690_00_Z9999_99` | 1-45 | 45 | 0 |

Totals: **156 scenes / 6,366 permitted rows / 270 excluded gap rows in projected scenes**.

## Opaque exclusion accounting

### Partial-scene gaps declared by the filtered projections

| Scene | Opaque excluded indexes | Count |
|---|---:|---:|
| `SC_M0554_00_M0555_00` | 2-24 | 23 |
| `SC_M0556_00_M0557_00` | 1-20 | 20 |
| `SC_M0568_00_M0569_00` | 1-59 | 59 |
| `SC_M0569_00_M0570_00` | 1-4 | 4 |
| `SC_M0570_00_M0571_00` | 1-12 | 12 |
| `SC_M0572_00_M0573_00` | 14, 16 | 2 |
| `SC_M0573_00_M0580_00` | 13-18 | 6 |
| `SC_M0590_00_M0600_00` | 32 | 1 |
| `SC_M0604_00_M0605_00` | 33-40 | 8 |
| `SC_M0608_00_M0609_00` | 55-66 | 12 |
| `SC_M0609_00_M0610_00` | 1-20 | 20 |
| `SC_M0610_00_M0611_00` | 37-49 | 13 |
| `SC_M0611_00_M0612_00` | 11-15 | 5 |
| `SC_M0650_00_M0660_00` | 42-65 | 24 |
| `SC_M0661_00_M0662_00` | 31-43 | 13 |
| `SC_M0664_00_M0665_00` | 10-13, 57-58 | 6 |
| `SC_M0665_00_M0666_00` | 16-22, 40-43 | 11 |
| `SC_M0671_00_M0680_00` | 23-53 | 31 |
| **Total** | | **270** |

### Fully excluded zero-debt scenes outside the translation/projection set

| Fully excluded scene | Opaque excluded indexes | Count |
|---|---:|---:|
| `SC_M0567_00_M0568_00` | 1-12 | 12 |
| `SC_M0612_00_M0615_00` | 1-363 | 363 |
| `SC_M0615_10_M0615_50` | 1-13 | 13 |
| `SC_M0615_20_M0615_50` | 1-10 | 10 |
| `SC_M0615_50_M0615_70` | 1-13 | 13 |
| `SC_M0615_70_M0615_80` | 1-28 | 28 |
| `SC_M0615_80_M0620_00` | 1-13 | 13 |
| `SC_M0630_10_M0640_00` | 1-163 | 163 |
| `SC_M0662_00_M0663_00` | 1-9 | 9 |
| `SC_M0663_00_M0664_00` | 1-271 | 271 |
| **Total** | | **895** |

Combined authoritative route ledger: **166 scene identities / 7,531 rows = 6,366 permitted + 270 partial-scene excluded + 895 fully excluded**. Excluded text was neither opened nor reconstructed.

## Closure

All five finding groups were repaired. The 11 affected scenes then passed
complete 579-row accuracy and literary recertification; literary QC made six
additional source-faithful prose refinements, and a final 306-row accuracy pass
recertified every scene changed by those refinements. Targeted arbitration found
no competing permitted reading and made no further translation change. Exact
joins, source controls, wrappers, file identity, speaker maps, terminology,
exclusions, controls, and CP932 pass. Route M is **PASS / closed** within this
static-text scope. Runtime textbox/backlog/layout and story-image correctness
remain explicitly unproven.
