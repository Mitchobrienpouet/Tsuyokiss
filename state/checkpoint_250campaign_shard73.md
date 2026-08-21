# 250-campaign shard 73 checkpoint

Status: DONE (ROLLING CONTINUATION; 2 TRANSLATED, 2 FULLY EXCLUDED)

Scenes:
- SC_G0460_00_G0480_00 — 97 permitted rows translated + accuracy/literary QC; indexes 98-116 remain excluded and absent
- SC_G0480_00_G0500_00 — fully excluded; indexes 1-518 remain absent and no translation or QC payload exists
- SC_G0500_00_G0520_00 — 41 permitted rows translated + accuracy/literary QC; indexes 27-40 remain excluded and absent
- SC_G0520_00_G0540_00 — fully excluded; indexes 1-126 remain absent and no translation or QC payload exists

Validation:
- direct accuracy and literary QC verification passed for both permitted projections
- exact permitted row counts reconcile with the machine-generated tail audit: 97 + 41 = 138 rows
- JSON/index-set, speaker-map where applicable, ASCII-typography, CP932, and exclusion-boundary gates are recorded PASS in accuracy QC
- both fully excluded scenes and both partial exclusion ranges are present in content_exclusions.json and remain absent, unbridged, and unsummarized
- literary QC reports no post-accuracy changes and no contested alternatives; targeted arbitration was not required
- no completed scene was retranslated and content_exclusions.json was not modified

Next shard: 74.
