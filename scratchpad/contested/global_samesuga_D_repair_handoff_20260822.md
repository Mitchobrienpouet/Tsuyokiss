# Global Samesuga and D-route repair handoff

Date: 2026-08-22  
Stage: translation repair only  
Scope: all open `D-RT-001` through `D-RT-004` findings plus the authorized
project-wide Shinichi surname normalization in B, D, E, F, G, J, and M

## Translation repairs

### Canonical surname

All listed occurrences retain their existing syntax, dialogue wrappers,
speaker attribution, `Shinichi`, `Fukahire`, `Shark`, and joke structure. Only
the obsolete surname token changed to `Samesuga`.

| Route | Translation file | Indexes | Before | After |
| --- | --- | --- | --- | --- |
| B | `SC_B0380_00_B0390_00.json` | `57, 152, 171` | `Samehyou` | `Samesuga` |
| B | `SC_B0390_00_B0400_00.json` | `29` | `Samehyou` | `Samesuga` |
| D | `SC_D0140_00_K0900_00.json` | `9` | `Samehyo` | `Samesuga` |
| D | `SC_D0440_00_D0460_00.json` | `21` | `Samehyo` | `Samesuga` |
| D | `SC_D0660_00_D0670_00.json` | `86` | `Samejima` | `Samesuga` |
| D | `SC_D0670_00_D0680_00.json` | `35` | `Samejima` | `Samesuga` |
| D | `SC_D0690_00_D0700_00.json` | `79, 109` | `Samejima` | `Samesuga` |
| D | `SC_D0700_00_D0720_00.json` | `16` | `Samejima` | `Samesuga` |
| D | `SC_D0770_00_D0780_00.json` | `88` | `Samehyo` | `Samesuga` |
| D | `SC_D0780_00_D0790_00.json` | `279` | `Samehyo` | `Samesuga` |
| D | `SC_D0790_40_D0800_00.json` | `73` | `Samehyo` | `Samesuga` |
| D | `SC_D0800_00_D0810_00.json` | `141, 149` | `Samehyo` | `Samesuga` |
| E | `SC_E0460_00_E0470_00.json` | `113` | `Samehyou` | `Samesuga` |
| E | `SC_E0630_00_E0640_00.json` | `29, 33, 50` | `Samehyou` | `Samesuga` |
| E | `SC_E0680_00_E0690_00.json` | `59` | `Samehyou` | `Samesuga` |
| F | `SC_F0840_00_F0850_00.json` | `64` | `Samehyou` | `Samesuga` |
| G | `SC_G0160_00_G0170_00.json` | `4` | `Samehyou` | `Samesuga` |
| J | `SC_J0100_09_J0100_10.json` | `4, 13` | `Samehyo` | `Samesuga` |
| M | `SC_M0261_00_M0262_00.json` | `35` | `Samehyo` | `Samesuga` |
| M | `SC_M0280_00_M0281_00.json` | `9` | `Samehyo` | `Samesuga` |
| M | `SC_M0470_00_M0471_00.json` | `46` | `Samehyou` | `Samesuga` |

Result: 28 line occurrences normalized across 21 translation files. The
existing explicit-ruby anchor `SC_D0630_00_D0640_00:3` was already `Samesuga`
and remains unchanged.

### Remaining D readthrough findings

| Finding | Translation file | Index/field | Before | After |
| --- | --- | --- | --- | --- |
| D-RT-002 | `SC_D0500_00_D0520_00.json` | `81` | `So that's what she meant by a harem.` | `「So that's what she meant by a harem.」` |
| D-RT-003 | `SC_D0810_00_D0820_00.json` | `file` | `SC_D0810_00_D0820_00.json` | `SC_D0810_00_D0820_00` |
| D-RT-003 | `SC_D0870_00_D0880_00.json` | `file` | `SC_D0870_00_D0880_00.json` | `SC_D0870_00_D0880_00` |
| D-RT-004 | `SC_D0580_00_D0600_00.json` | `33` | `Sports and Combat Festival` | `Sports and Martial Arts Festival` |
| D-RT-004 | `SC_D0810_00_D0820_00.json` | `355` | `Ryuumeikan Festival--our cultural festival` | `Ryuumei Festival--our cultural festival` |
| D-RT-004 | `SC_D0870_00_D0880_00.json` | `102` | `Matsukasa Opening Festival` | `Matsukasa Port Opening Festival` |
| D-RT-004 | `SC_D0870_00_D0880_00.json` | `128, 212` | `Opening Festival` | `Port Opening Festival` |
| D-RT-004 | `SC_D0870_00_D0880_00.json` | `469` | `Athletics and Martial Arts Festival` | `Sports and Martial Arts Festival` |

Result: seven D line rows and two D metadata fields repaired. Across both
sections, this handoff covers 35 changed translation rows and two metadata
fields in 25 translation files.

## Central and continuity locks updated

- `bible/characters.md`: added the Shinichi Samesuga identity/voice lock,
  preserving `Fukahire` and `Shark` usage.
- `bible/glossary.md`: fixed Shinichi's canonical full name and added canonical
  locks for the Sports and Martial Arts Festival, Ryuumei Festival, and
  Matsukasa Port Opening Festival / Port Opening Festival.
- `scratchpad/specs/SC_A0360_20_A0360_30-SC_A0360_30_A0360_40-SC_A0360_40_A0360_50-SC_A0360_50_A0360_60.md`
- `scratchpad/specs/SC_A0370_40_A0370_50-SC_A0370_50_A0370_60-SC_A0370_60_A0370_70-SC_A0370_70_A0370_80.md`
- `scratchpad/specs/SC_C0100_00_K0900_00-SC_C0120_00_K0900_00-SC_C0140_00_K0900_00-SC_C0180_00_K0900_00.md`
- `scratchpad/specs/SC_D0610_00_D0620_00-SC_D0620_00_D0630_00-SC_D0630_00_D0640_00-SC_D0640_00_D0650_00.md`
- `scratchpad/specs/SC_D0690_00_D0700_00-SC_D0700_00_D0720_00-SC_D0720_00_D0730_00-SC_D0730_00_D0740_00.md`
- `scratchpad/specs/SC_D0760_40_D0770_00-SC_D0760_70_D0760_40-SC_D0760_80_Z9999_99-SC_D0770_00_D0780_00.md`
- `scratchpad/specs/SC_D0790_40_D0800_00-SC_D0800_00_D0810_00-SC_D0810_00_D0820_00-SC_D0820_00_D0830_00.md`
- `scratchpad/specs/SC_D0870_00_D0880_00-SC_D0880_00_D0880_50-SC_D0880_50_D0890_00-SC_D0890_00_D0900_00.md`
- `scratchpad/specs/SC_E0560_00_E0570_00-SC_E0570_10_E0570_30-SC_E0570_20_E0570_30-SC_E0570_30_E0580_00.md`
- `scratchpad/specs/SC_E0580_00_E0590_00-SC_E0590_00_E0600_00-SC_E0600_10_E0610_00-SC_E0600_20_E0610_00.md`
- `scratchpad/specs/SC_E0640_00_E0650_00-SC_E0650_00_E0650_50-SC_E0650_50_E0660_00-SC_E0660_00_E0670_00.md`

Only directly contradictory surname/event terminology was changed in these
specifications. No QC, arbitration, readthrough, source, exclusion,
configuration, pipeline-state, or Git artifact was edited.

## Deterministic validation

The repair was checked with a non-mutating metadata/index validator; excluded
source text was not inspected.

| Gate | Result |
| --- | --- |
| Translation JSON and duplicate keys | PASS: 771 files, 0 errors |
| Global cardinality | PASS: 48,023 translated rows for 48,023 permitted rows |
| Exact source/exclusion joins | PASS: 0 missing, extra, or excluded translation keys |
| Artifact coverage | PASS: 0 missing or extra translation artifacts |
| Internal `file` identity | PASS: 0 mismatches |
| CP932 encoding | PASS: 0 failures |
| Source metadata | PASS: 59,819 present and unique engine IDs; 0 malformed SHA-256 fields |
| D-route dialogue wrappers | PASS: 0 mismatches after the D0500:81 repair |
| Targeted D values | PASS: all seven repaired line values and both metadata fields exact |
| Stale surname scan in all translations | PASS: 0 occurrences of `Samehyo`, `Samehyou`, or `Samejima` |

No blockers remain. Translations are frozen at this handoff pending independent
QC/arbitration updates by their owning stages.
