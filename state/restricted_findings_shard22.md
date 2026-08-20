# Restricted findings: shard 22

Fail-closed classification found new held material in three filtered model
projections. No translation, QC, or arbitration work was started.

| Scene | Held ranges | Reason |
|---|---:|---|
| `SC_D0760_40_D0770_00` | `8-18` | Direct explicit sexual aftermath, bodily-fluid cleanup, ejaculation recollection, and sexualized masochism involving high-school students. |
| `SC_D0760_70_D0760_40` | `1-7` | Continuous explicit genital stimulation, ejaculation, and sexualized punishment involving high-school students. |
| `SC_D0760_80_Z9999_99` | `1-19` | Continuous coercive fetish humiliation culminating in explicit genital violence involving high-school students. |

`SC_D0770_00_D0780_00` contains no newly restricted row. The supervisor must
register the exact ranges above in `content_exclusions.json` and regenerate the
three affected filtered projections before any model-backed translation stage
uses them. `SC_D0760_40_D0770_00:1-7` remains ordinary translatable material;
the other two affected scenes are fully held. Do not bridge, summarize, or
reconstruct any held row.
