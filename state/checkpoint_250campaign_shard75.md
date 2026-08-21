# 250-campaign shard 75 checkpoint

Status: DONE (ROLLING CONTINUATION; 3 TRANSLATED, 1 FULLY EXCLUDED)

Scenes:
- SC_G0720_00_G0750_00 — 27 permitted rows translated + accuracy/literary QC; excluded index 4 remains absent
- SC_G0750_00_G0760_00 — fully excluded; indexes 1-362 remain absent and no translation or QC payload exists
- SC_G0760_00_G0800_00 — 121 permitted rows translated + accuracy/literary QC; excluded indexes 1-7, 96-97, 115-116, and 124 remain absent
- SC_G0800_00_G0850_00 — 408 permitted rows translated + accuracy/literary QC; registered filtered ranges remain absent

Validation:
- direct accuracy and literary QC verification passed for all three permitted projections
- exact permitted row counts reconcile with the machine-generated tail audit: 27 + 121 + 408 = 556 rows
- JSON duplicate-key/index-set, speaker-map, ASCII-typography, CP932, and exclusion-boundary gates are recorded PASS in accuracy QC
- the fully excluded scene and all partial exclusion ranges are present in content_exclusions.json and remain absent, unbridged, and unsummarized
- literary QC reports no post-accuracy changes and no contested alternatives; targeted arbitration was not required
- no completed scene was retranslated and content_exclusions.json was not modified

Next shard: 76.
