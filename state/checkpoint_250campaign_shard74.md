# 250-campaign shard 74 checkpoint

Status: DONE (ROLLING CONTINUATION)

Scenes:
- SC_G0540_00_G0600_00 — 304 permitted rows translated + accuracy/literary QC; excluded indexes 1-62, 86, 112-132, 353-375, and 380-384 remain absent
- SC_G0600_00_G0650_00 — 74 rows translated + accuracy/literary QC; no restricted range
- SC_G0650_00_G0700_00 — 246 permitted rows translated + accuracy/literary QC; excluded indexes 35-39, 61-111, 241-242, and 290-306 remain absent
- SC_G0700_00_G0720_00 — 4 permitted rows translated + accuracy/literary QC; excluded indexes 1-38 remain absent

Validation:
- direct accuracy and literary QC verification passed for all four scenes
- exact permitted row counts reconcile with the machine-generated tail audit: 304 + 74 + 246 + 4 = 628 rows
- JSON duplicate-key/index-set, speaker-map, ASCII-typography, CP932, and exclusion-boundary gates are recorded PASS in accuracy QC
- all registered excluded ranges remain absent, unbridged, and unsummarized
- literary QC reports no post-accuracy changes and no contested alternatives; targeted arbitration was not required
- no completed scene was retranslated and content_exclusions.json was not modified

Next shard: 75.
