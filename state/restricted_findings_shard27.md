# Restricted findings: shard 27

Fail-closed classification found two new held ranges in one current model
projection. No translation, QC, or arbitration work was started.

| Scene | Held ranges | Reason |
|---|---:|---|
| `SC_D0920_20_D0920_60` | `76-77`, `139-141` | Direct breast-focused recollection of excluded sexual aftermath, followed by sexualized uniform/skirt exposure and under-skirt fanning involving high-school students. |

`SC_D0900_00_D0910_00`, `SC_D0910_00_D0920_00`, and
`SC_D0920_10_D0930_00` contain no newly restricted row. The supervisor must
register the exact ranges above in `content_exclusions.json` and regenerate
`SC_D0920_20_D0920_60` before any model-backed translation stage uses it.
After regeneration, that scene should contain 270 eligible rows:
`1-75`, `78-138`, and `142-275`. Never bridge, summarize, euphemize, or
reconstruct a held row.
