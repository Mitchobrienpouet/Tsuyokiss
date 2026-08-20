# Restricted findings: wave 300 shard 26

The current model-source projections contain newly detected sexualized content
involving high-school students. The supervising agent must add the exact ranges
below to `content_exclusions.json` and regenerate the affected projections
before any translation or QC work begins.

- `SC_D0870_00_D0880_00`: `7-8`, `13`, `21-30`, `36-38`, `63-70`,
  `224-227`, `262-289`, `350-390`, `480-488`.
  Reason: explicit post-sex references, sexual recollection and masturbation,
  repeated-sex discussion, sexualized contact and invitations, explicit
  aftermath, contraception discussion, and renewed sexual setup involving
  high-school students.
- `SC_D0880_00_D0880_50`: `1-234`.
  Reason: continuous explicit sexual scene involving high-school students.
- `SC_D0880_50_D0890_00`: `1-12`, `177-182`, `215-219`, `235-236`.
  Reason: explicit sexual aftermath, sexualized scenario, breast contact,
  intercourse discussion, and explicit sexual proposition involving
  high-school students.
- `SC_D0890_00_D0900_00`: `29-32`, `90-91`.
  Reason: explicit sexual-act callbacks and explicit sexual desire involving
  high-school students.

Do not translate, summarize, bridge, or reconstruct these rows in any
downstream artifact. `SC_D0880_00_D0880_50` is fully held and must receive no
translation, QC, arbitration, or build artifact.
