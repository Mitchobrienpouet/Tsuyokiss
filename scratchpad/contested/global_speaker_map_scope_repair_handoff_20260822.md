# Global speaker-map scope repair handoff

Date: 2026-08-22

Stage: translation metadata repair only

## Adopted removals

Only speaker-map entries absent from the corresponding permitted filtered
projection were removed. No translated line or other speaker mapping changed.

| Translation | Removed source key | Removed target value |
|---|---|---|
| `SC_E0650_00_E0650_50.json` | `２年男子` | `Second-Year Boy` |
| `SC_E0650_00_E0650_50.json` | `赤組応援団` | `East Cheer Squad` |
| `SC_E0650_00_E0650_50.json` | `白組応援団` | `West Cheer Squad` |
| `SC_E0650_00_E0650_50.json` | `アナウンス` | `Announcement` |
| `SC_E0710_00_E0720_00.json` | `祈` | `Inori` |
| `SC_F0840_00_F0850_00.json` | `スバル` | `Subaru` |
| `SC_G0500_00_G0520_00.json` | `レオ` | `Leo` |
| `SC_G0500_00_G0520_00.json` | `良美` | `Yoshimi` |
| `SC_G0650_00_G0700_00.json` | `エリカ` | `Erika` |
| `SC_G0650_00_G0700_00.json` | `鉢巻先生` | `Headband Teacher` |

## Validation contract

- The five repaired maps must equal the exact set of non-null speakers in
  their permitted model projections, with no missing or excess keys.
- Translation line objects, indexes, file identity, and text are unchanged.
- JSON parsing, exact projection joins, wrappers, and CP932 must pass the
  public validator.
