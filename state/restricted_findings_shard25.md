# Restricted findings: shard 25

Fail-closed classification found new held material in all four current model
projections. No translation, QC, or arbitration work was started.

| Scene | Held ranges | Reason |
|---|---:|---|
| `SC_D0830_00_D0840_00` | `8-10`, `14`, `54`, `62-64`, `74-190` | Direct references to prior sexual activity and genital exposure, followed by a continuous erotic lead-in, contraception discussion, arousal, nudity preparation, and intent to have sex involving high-school students. |
| `SC_D0840_00_D0850_00` | `1-451` | Continuous explicit sexual activity, nudity, genital contact, and sexualized dialogue involving high-school students. |
| `SC_D0850_00_D0860_00` | `6-17` | Direct explicit sexual aftermath, orgasm/ejaculation tally, intercourse reflection, and post-sex washing involving high-school students. |
| `SC_D0860_00_D0870_00` | `1-50`, `57-63` | Continuous nude sexual aftermath, breast touching/sucking, fetishized underwear request, direct intercourse discussion, and renewed breast contact involving high-school students. |

The supervisor must register the exact ranges above in
`content_exclusions.json` and regenerate all four filtered projections before
any model-backed translation stage uses them. After regeneration, the eligible
rows should be:

- `SC_D0830_00_D0840_00`: 65 rows (`1-7`, `11-13`, `15-53`, `55-61`,
  `65-73`)
- `SC_D0840_00_D0850_00`: no rows; create no downstream artifact
- `SC_D0850_00_D0860_00`: 5 rows (`1-5`)
- `SC_D0860_00_D0870_00`: 17 rows (`51-56`, `64-74`)

Never bridge, summarize, euphemize, or reconstruct a held row.
