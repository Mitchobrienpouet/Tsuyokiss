# Full-route A targeted translation repair handoff

Date: 2026-08-22  
Status: completed  
Stage: translate / post-readthrough targeted repair  
Source findings: A-RT-001 through A-RT-010  
Blockers: NONE

## Scope

Applied only the supervisor-decided repairs from
scratchpad/readthrough/full_route_A_critical_20260822.md. No QC, arbitration,
readthrough, bible, configuration, source, pipeline, state, or Git artifact was
modified.

Repair totals:

- 20 translation files changed.
- 24 displayed text rows changed.
- 6 speaker-map entries changed, affecting 10 spoken-row name labels.
- SC_A0100_16_A0100_18:2 was inspected as the ninth surname occurrence and was
  already Samesuga, so it required no edit.
- No source index, file identity, or unrelated prose changed.

## Finding decisions

### A-RT-001: Samesuga normalization

The explicit ruby さめすが is authoritative for this repair. The following
eight rows changed to Samesuga:

| Scene | Indexes | Before | After |
| --- | --- | --- | --- |
| SC_A0100_32_A0100_40 | 35 | Samehyou | Samesuga |
| SC_A0110_60_A0110_70 | 2 | Samejima | Samesuga |
| SC_A0180_90_A0190_00 | 3 | Samejima | Samesuga |
| SC_A0360_40_A0360_50 | 35 | Samejima | Samesuga |
| SC_A0360_70_A0360_80 | 10 | Samehyou | Samesuga |
| SC_A0370_60_A0370_70 | 12 | Samejima | Samesuga |
| SC_A0450_20_A0450_30 | 4, 7 | Samehyou | Samesuga |

Control occurrence SC_A0100_16_A0100_18:2 remained unchanged as Shinichi
Samesuga. The A-route corpus now has exactly 9 Samesuga occurrences and zero
Samejima or Samehyou occurrences.

### A-RT-002: rescue roles

| Scene | Index | Before | After |
| --- | --- | --- | --- |
| SC_A0440_60_A0440_70 | 5 | Actually, maybe I saved the delinquents from a pickup artist? | Actually, maybe I saved a delinquent from some pickup artists? |

The repair restores the singular rough girl as the person rescued and the pickup
men as the threat, while retaining Leo's tentative self-correction.

### A-RT-003: Tonfa speaker labels

| Scene | Spoken index | Speaker-map change |
| --- | --- | --- |
| SC_A0100_32_A0100_40 | 17 | 豆花: Touka -> Tonfa |
| SC_A0120_60_A0120_70 | 14 | 豆花: Touka -> Tonfa |
| SC_A0150_00_A0150_10 | 15 | 豆花: Touka -> Tonfa |

### A-RT-004: dialogue wrapper

| Scene | Index | Before | After |
| --- | --- | --- | --- |
| SC_A0190_20_A0190_30 | 33 | They could tell me not to think about it, but... | 「They could tell me not to think about it, but...」 |

The target now matches source kind=dialogue and speaker=Leo.

### A-RT-005: Burrhead speaker label

| Scene | Spoken indexes | Speaker-map change |
| --- | --- | --- |
| SC_A0160_20_A0160_30 | 1, 3 | イガグリ: Igaguri -> Burrhead |

### A-RT-006: Heizo normalization

| Scene | Indexes | Change |
| --- | --- | --- |
| SC_A0100_18_A0100_20 | 42, 48 | Heizou Tachibana -> Heizo Tachibana |
| SC_A0100_18_A0100_20 | speaker map; affects 42, 48 | 平蔵: Heizou -> Heizo |

### A-RT-007: Ellie nickname

| Scene | Index | Change |
| --- | --- | --- |
| SC_A0410_70_A0410_80 | 28 | Elly -> Ellie |

### A-RT-008: Miss Inori address lock

| Scene | Indexes | Change |
| --- | --- | --- |
| SC_A0120_70_A0120_80 | 3, 11, 22, 31 | Ms. Inori -> Miss Inori |
| SC_A0120_80_A0120_85 | 2 | Ms. Inori -> Miss Inori |
| SC_A0150_00_A0150_10 | 17 | Ms. Inori -> Miss Inori |
| SC_A0230_00_A0230_10 | 5 | Ms. Inori -> Miss Inori |
| SC_A0250_10_A0250_20 | 3, 14 | Ms. Inori -> Miss Inori |
| SC_A0460_40_A0460_50 | 2 | Ms. Inori -> Miss Inori |

All 10 requested narration mentions were normalized. The A-route corpus now has
zero Ms. Inori occurrences.

### A-RT-009: Mr. Tsuchinaga speaker label

| Scene | Spoken indexes | Speaker-map change |
| --- | --- | --- |
| SC_A0120_70_A0120_80 | 9, 23, 33 | 土永さん: Tsuchinaga -> Mr. Tsuchinaga |

### A-RT-010: maiden / Otome toothbrush pun

| Scene | Index | Before | After |
| --- | --- | --- | --- |
| SC_A0380_40_A0380_50 | 6 | Mistaking an 'Otome's' toothbrush for your own and using it... You will make her hate you. | You mistook a maiden's--Otome's--toothbrush for your own and used it... She'll hate you. |

The grammatical apposition preserves the maiden/name wordplay, mistaken-use
agency, and warning without explaining or extending the joke.

## Files and exact changed indexes

| Translation file | Displayed text indexes | Speaker-map entries and affected spoken indexes |
| --- | --- | --- |
| SC_A0100_18_A0100_20.json | 42, 48 | 平蔵 -> Heizo; 42, 48 |
| SC_A0100_32_A0100_40.json | 35 | 豆花 -> Tonfa; 17 |
| SC_A0110_60_A0110_70.json | 2 | NONE |
| SC_A0120_60_A0120_70.json | NONE | 豆花 -> Tonfa; 14 |
| SC_A0120_70_A0120_80.json | 3, 11, 22, 31 | 土永さん -> Mr. Tsuchinaga; 9, 23, 33 |
| SC_A0120_80_A0120_85.json | 2 | NONE |
| SC_A0150_00_A0150_10.json | 17 | 豆花 -> Tonfa; 15 |
| SC_A0160_20_A0160_30.json | NONE | イガグリ -> Burrhead; 1, 3 |
| SC_A0180_90_A0190_00.json | 3 | NONE |
| SC_A0190_20_A0190_30.json | 33 | NONE |
| SC_A0230_00_A0230_10.json | 5 | NONE |
| SC_A0250_10_A0250_20.json | 3, 14 | NONE |
| SC_A0360_40_A0360_50.json | 35 | NONE |
| SC_A0360_70_A0360_80.json | 10 | NONE |
| SC_A0370_60_A0370_70.json | 12 | NONE |
| SC_A0380_40_A0380_50.json | 6 | NONE |
| SC_A0410_70_A0410_80.json | 28 | NONE |
| SC_A0440_60_A0440_70.json | 5 | NONE |
| SC_A0450_20_A0450_30.json | 4, 7 | NONE |
| SC_A0460_40_A0460_50.json | 2 | NONE |

## Deterministic validation

Validation was rerun across all 269 A-route translations, not only the changed
files.

| Gate | Result |
| --- | --- |
| Translation files / permitted rows | PASS: 269 / 6,078 |
| Exact permitted index joins | PASS: 0 errors |
| Engine IDs | PASS: 6,078 present, 6,078 unique |
| Source SHA-256 recomputation | PASS: 0 errors |
| Speaker maps | PASS: 0 missing source speakers |
| Changed-row dialogue wrappers | PASS: 0 errors |
| CP932 target and speaker-map strings | PASS: 0 errors |
| Project per-scene validator | PASS: 269 / 269 |
| Requested stale forms in A route | PASS: 0 Samejima, Samehyou, Heizou, Elly, Ms. Inori, Touka maps, Igaguri maps, or bare Tsuchinaga maps |

## Handoff

All ten readthrough findings have translation-stage repairs. No contested
reading remains in this repair lane. Independent downstream recertification and
readthrough closure remain supervisor-owned.

