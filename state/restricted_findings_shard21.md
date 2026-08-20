# Restricted findings: shard 21

Fail-closed classification found new held material in the filtered model
projections. No shard-21 preflight, translation, QC, or arbitration work was
started.

| Scene | Held ranges | Reason |
|---|---:|---|
| `SC_D0740_00_D0760_00` | `1-12`, `194-303` | Explicit sexual aftermath and masturbation message, followed by a continuous explicit genital-contact, manual-stimulation, exposure, coercive sexual contact, fetishized violence, and genital-abuse sequence involving high-school students. |
| `SC_D0760_10_D0760_40` | `1-17` | Continuous explicit genital stimulation, ejaculation, underwear exposure, and fetishized sexual contact involving high-school students. |
| `SC_D0760_20_D0760_40` | `1-16` | Continuous explicit genital stimulation, ejaculation, and consensualized fetish-punishment discussion involving high-school students. |
| `SC_D0760_30_D0760_60` | `15-34` | Explicit genital violence and coercive fetish roleplay involving high-school students. |

The supervisor must register these exact ranges in `content_exclusions.json`
and regenerate all four filtered projections before shard 21 can resume. The
ordinary school, sports-festival, and relationship material outside the listed
ranges remains translatable.

## Supplemental finding after first refresh

The first regenerated `SC_D0740_00_D0760_00` projection still exposed two
short sexualized jokes tied to the earlier explicit material. The resumed
pipeline stopped again before preflight or translation.

| Scene | Additional held ranges | Reason |
|---|---:|---|
| `SC_D0740_00_D0760_00` | `33-34`, `41` | Explicit discussion of involuntary genital arousal and a callback comparing Leo's behavior to a morning erection, involving high-school students. |

Register these additional exact indexes and regenerate the partial projection
again before resuming shard 21.
