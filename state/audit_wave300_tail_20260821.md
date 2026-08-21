# Wave-300 tail closeout audit — 2026-08-21

Status: **PASS — no actionable translation or QC gap in shards 72-77.**

The audit validates canonical exclusion coverage, translation/exclusion index disjointness, complete known index coverage, duplicate-free JSON, both QC payloads, and CP932 encodability for every banked scene.

## Shard 72

| Scene | Status | Rows | Accuracy | Literary | CP932 |
|---|---|---:|---:|---:|---:|
| `SC_G0390_00_G0400_00` | FULLY_EXCLUDED | 0 | not applicable | not applicable | not applicable |
| `SC_G0400_00_G0420_00` | BANKED | 25 | PASS | verified | PASS |
| `SC_G0420_00_G0440_00` | BANKED | 19 | PASS | verified | PASS |
| `SC_G0440_00_G0460_00` | BANKED | 41 | PASS | verified | PASS |

## Shard 73

| Scene | Status | Rows | Accuracy | Literary | CP932 |
|---|---|---:|---:|---:|---:|
| `SC_G0460_00_G0480_00` | BANKED | 97 | PASS | verified | PASS |
| `SC_G0480_00_G0500_00` | FULLY_EXCLUDED | 0 | not applicable | not applicable | not applicable |
| `SC_G0500_00_G0520_00` | BANKED | 41 | PASS | verified | PASS |
| `SC_G0520_00_G0540_00` | FULLY_EXCLUDED | 0 | not applicable | not applicable | not applicable |

## Shard 74

| Scene | Status | Rows | Accuracy | Literary | CP932 |
|---|---|---:|---:|---:|---:|
| `SC_G0540_00_G0600_00` | BANKED | 304 | PASS | verified | PASS |
| `SC_G0600_00_G0650_00` | BANKED | 74 | PASS | verified | PASS |
| `SC_G0650_00_G0700_00` | BANKED | 246 | PASS | verified | PASS |
| `SC_G0700_00_G0720_00` | BANKED | 4 | PASS | verified | PASS |

## Shard 75

| Scene | Status | Rows | Accuracy | Literary | CP932 |
|---|---|---:|---:|---:|---:|
| `SC_G0720_00_G0750_00` | BANKED | 27 | PASS | verified | PASS |
| `SC_G0750_00_G0760_00` | FULLY_EXCLUDED | 0 | not applicable | not applicable | not applicable |
| `SC_G0760_00_G0800_00` | BANKED | 121 | PASS | verified | PASS |
| `SC_G0800_00_G0850_00` | BANKED | 408 | PASS | verified | PASS |

## Shard 76

| Scene | Status | Rows | Accuracy | Literary | CP932 |
|---|---|---:|---:|---:|---:|
| `SC_G0850_00_G0860_00` | BANKED | 98 | PASS | verified | PASS |
| `SC_G0860_10_G0870_00` | BANKED | 22 | PASS | verified | PASS |
| `SC_G0860_20_G0950_00` | BANKED | 32 | PASS | verified | PASS |
| `SC_G0870_00_G0900_00` | BANKED | 190 | PASS | verified | PASS |

## Shard 77

| Scene | Status | Rows | Accuracy | Literary | CP932 |
|---|---|---:|---:|---:|---:|
| `SC_G0900_00_G0910_00` | BANKED | 78 | PASS | verified | PASS |
| `SC_G0910_00_G0920_00` | FULLY_EXCLUDED | 0 | not applicable | not applicable | not applicable |
| `SC_G0920_00_G0930_00` | BANKED | 42 | PASS | verified | PASS |

## Totals

- Banked scenes: 18
- Fully excluded scenes: 5
- Banked translation rows: 1869
- Actionable gaps: none
