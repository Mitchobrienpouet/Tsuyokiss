# Wave ledger

## 300-scene continuation campaign

- Status: FIRED 2026-08-20T09:06:06Z
- Requested scene count: 300 (77 contiguous shards; short route-terminal shards preserve narrative-block boundaries)
- Planned first/last scene: SC_C0200_00_C0300_00 / SC_G0920_00_G0930_00
- Progress checkpoint: 200/300 scenes closed; 100 scenes remain claimed
- Last remotely verified campaign checkpoint: 2fd5cf4b181d41051e9507c460540cd94c363429
- Anti-block recovery: SC_C0600_40_C0650_00 was translated in six exact permitted-index segments, mechanically merged, then independently accuracy-QCed, literary-QCed, and arbitrated as one canonical scene
- Active execution mode: three Codex Work workers in rolling rotation; supervisor-only validation and GitHub checkpoints
- Global concurrency ceiling: 6 model calls; at most three workers active in this environment
- Existing completed coverage excluded from claims: 322 translated scenes plus 11 fully excluded scenes
- Rolled-forward debt from the 250-scene campaign: 165 scenes after 75 translations and 10 full-scene exclusions were completed
- Additional new coverage claimed: 135 scenes, for an exact 300-scene continuation wave
- Durable shard plan: `state/wave_300_plan.md`
- Durable claim state: `state/pipeline.json` (local orchestration cache; intentionally ignored by Git)
- Intended GitHub remote/branch: Mitchobrienpouet/Tsuyokiss / codex/wave-300-continuation-20260820 (default `main` is protected)
- Anti-block recovery: shards 16-18 completed after fail-closed projection refreshes; legacy index drift in SC_D0200_00_D0220_00 and SC_D0430_00_D0440_00 was fully realigned and revalidated.
- Anti-block recovery: shards 19-21 completed after serial fail-closed refreshes; four scenes were fully excluded and eight permitted scenes/partials were fully gated.
- Anti-block recovery: shards 22-30 are closed. Shard 29 contains one fully excluded scene; the other eleven scenes/partials passed both QC lenses, arbitration, JSON/index, exclusion, and CP932 gates.
- Anti-block recovery: shards 31-33 are closed after exact fail-closed filtering in shards 31 and 33; all twelve permitted scene outputs passed both QC lenses, arbitration, JSON/index, exclusion, and CP932 gates.
- Anti-block recovery: shards 34-36 are closed after exact fail-closed filtering; shard 39 was independently classified as four fully excluded bath-voyeurism scenes. Twelve permitted outputs passed both QC lenses, arbitration, JSON/index, exclusion, and CP932 gates.
- Anti-block recovery: shards 37-38 and 40-42 are closed after exact fail-closed filtering. Shard 40 contains one fully excluded scene; nineteen permitted outputs passed both QC lenses, arbitration, JSON/index, exclusion, and CP932 gates.
- Anti-block recovery: shards 43-45 are closed after exact fail-closed filtering. Shard 45's 898-line scene was translated in two exact permitted-index segments, mechanically merged, then independently accuracy-QCed, literary-QCed, and arbitrated as one canonical scene; all twelve outputs pass deterministic gates.
- Anti-block recovery: shards 46-47 are closed after exact fail-closed filtering. Their eight outputs cover 2,026 permitted lines and pass both QC lenses, arbitration, JSON/index, exclusion, and CP932 gates.
- Starting remotely verified commit: 60cc5e1d1833f77ae11584ea9b3c022f500a2630
- Dead/stalled check at launch: PASS; no active, dead, stalled, or failed runs
- Translation debt at launch: 300 claimed scenes
- QC debt at launch: NONE (no newly translated scene has bypassed QC)
- Checkpoint debt at launch: NONE

## 250-scene campaign

- Status: ROLLED FORWARD 2026-08-20T09:06:06Z
- Progress at rollover: 85/250 scenes closed (75 translated, 10 fully excluded); the remaining 165 scenes are claimed by the 300-scene continuation campaign
- Requested scene count: 250 (64 contiguous shards; short terminal shards preserve narrative-block boundaries)
- Planned first/last scene: SC_A0440_70_A0440_80 / SC_E0570_30_E0580_00
- Active execution mode: three Codex Work workers in rolling rotation; supervisor-only validation and GitHub checkpoints
- Global concurrency ceiling: 6 model calls; at most three workers active in this environment
- Existing completed coverage excluded from claims: 247 translated scenes plus 1 fully excluded scene
- Durable claim state: `state/pipeline.json` (local orchestration cache; intentionally ignored by Git)
- Intended GitHub remote/branch: Mitchobrienpouet/Tsuyokiss / main
- Starting remotely verified commit: 083a19ad5a37c822a911c5e39e88ab97f6c4e4c0
- Dead/stalled check at launch: PASS; no active, dead, stalled, or failed runs
- Translation debt at launch: 250 claimed scenes
- QC debt at launch: NONE (no newly translated scene has bypassed QC)
- Checkpoint debt at launch: NONE

## 200-scene campaign

- Status: COMPLETED 2026-08-20T06:01:12Z
- Requested scene count: 200 (50 shards x 4 contiguous scenes)
- Planned first/last scene: SC_A0130_30_A0130_40 / SC_A0440_60_A0440_70
- Active concurrency: NONE; all 50 shards are DONE
- Completed campaign coverage: 200/200 planned scenes (199 translated, 1 fully excluded), 4,384 permitted source rows
- Durable shard plan: `state/preflight_cache_plan.md`
- Intended GitHub remote/branch: Mitchobrienpouet/Tsuyokiss / main
- Last remotely verified commit: a588410001df87f7fe20900f9445bd50c211a506
- Fired shard IDs:
  - shard-SC_A0130_30_A0130_40-SC_A0130_40_A0130_50-SC_A0130_50_A0130_60-SC_A0130_60_A0130_70-f97d2848
  - shard-SC_A0130_70_A0130_80-SC_A0130_80_A0130_90-SC_A0130_90_A0140_00-SC_A0140_00_A0140_10-44b07c85
  - shard-SC_A0140_10_A0140_20-SC_A0140_20_A0140_30-SC_A0140_30_A0140_40-SC_A0140_40_A0140_50-1af726e0
  - shard-SC_A0140_50_A0140_60-SC_A0140_60_A0140_70-SC_A0140_70_A0140_80-SC_A0140_80_A0140_90-09710444
  - shard-SC_A0140_90_A0150_00-SC_A0150_00_A0150_10-SC_A0150_10_A0150_20-SC_A0150_20_A0150_30-56cf8cb7
  - shard-SC_A0150_30_A0150_40-SC_A0150_40_A0150_50-SC_A0150_50_A0150_60-SC_A0150_60_A0150_70-4821536a
  - shard-SC_A0150_70_A0150_80-SC_A0150_80_A0150_90-SC_A0150_90_A0160_00-SC_A0160_00_A0160_10-1091aaa0
  - shard-SC_A0160_10_A0160_20-SC_A0160_20_A0160_30-SC_A0160_30_A0160_40-SC_A0160_40_A0160_50-a3c41e6b
  - shard-SC_A0160_50_A0160_60-SC_A0160_60_A0160_70-SC_A0160_70_A0160_80-SC_A0160_80_A0160_90-a7039f81
  - shard-SC_A0160_90_A0170_00-SC_A0170_00_A0170_10-SC_A0170_10_A0170_20-SC_A0170_20_A0170_30-161d4b6b
  - shard-SC_A0170_30_A0170_40-SC_A0170_40_A0170_50-SC_A0170_50_A0170_60-SC_A0170_70_A0180_00-054399e9
  - shard-SC_A0170_80_A0170_60-SC_A0180_00_A0180_10-SC_A0180_10_A0180_20-SC_A0180_20_A0180_30-b47dbac3
  - shard-SC_A0180_30_A0180_40-SC_A0180_40_A0180_50-SC_A0180_50_A0180_60-SC_A0180_60_A0180_70-5513aa88
  - shard-SC_A0180_70_A0180_80-SC_A0180_80_A0180_90-SC_A0180_90_A0190_00-SC_A0190_00_A0190_10-47fe666a
  - shard-SC_A0190_10_A0190_20-SC_A0190_20_A0190_30-SC_A0190_30_A0190_40-SC_A0190_40_A0190_50-33272ab4
  - shard-SC_A0190_50_A0190_60-SC_A0190_60_A0190_70-SC_A0190_70_A0190_80-SC_A0190_80_A0190_90-36b3027e
  - shard-SC_A0190_90_A0200_00-SC_A0200_00_A0200_10-SC_A0200_10_A0200_20-SC_A0200_20_A0200_30-2eead99a
  - shard-SC_A0200_30_A0200_40-SC_A0200_40_A0200_50-SC_A0200_50_A0200_60-SC_A0200_60_A0200_70-d81c2317
  - shard-SC_A0200_80_A0210_00-SC_A0200_90_A0210_00-SC_A0210_00_A0210_10-SC_A0210_10_A0210_20-0c44f415
  - shard-SC_A0210_20_A0210_30-SC_A0210_30_A0210_40-SC_A0210_40_A0210_50-SC_A0210_50_A0210_60-7390fcd6
  - shard-SC_A0210_60_A0210_70-SC_A0210_70_A0210_80-SC_A0210_80_A0210_90-SC_A0210_90_A0220_00-caff7a11
  - shard-SC_A0220_00_A0220_10-SC_A0220_10_A0220_20-SC_A0220_20_A0220_30-SC_A0220_30_A0220_40-67502ffa
  - shard-SC_A0220_40_A0220_50-SC_A0220_50_A0220_60-SC_A0220_60_A0220_70-SC_A0220_70_A0220_80-689a6984
  - shard-SC_A0220_80_A0220_90-SC_A0220_90_A0230_00-SC_A0230_00_A0230_10-SC_A0230_10_A0230_15-e8d03387
  - shard-SC_A0230_15_A0230_20-SC_A0230_20_A0230_30-SC_A0230_30_A0230_40-SC_A0230_40_A0230_50-e6870910
  - shard-SC_A0230_50_A0230_60-SC_A0230_60_A0230_70-SC_A0230_70_A0230_80-SC_A0230_80_A0230_90-0e6e741d
  - shard-SC_A0230_90_A0240_00-SC_A0240_00_A0240_10-SC_A0240_10_A0240_20-SC_A0240_20_A0240_30-db65a17a
  - shard-SC_A0240_30_A0240_40-SC_A0240_40_A0240_50-SC_A0240_50_A0240_60-SC_A0240_70_A0250_00-fafb4263
  - shard-SC_A0240_80_A0250_00-SC_A0250_00_A0250_10-SC_A0250_10_A0250_20-SC_A0250_20_A0250_30-0ff07667
  - shard-SC_A0250_30_A0250_40-SC_A0250_40_A0250_50-SC_A0250_50_A0250_60-SC_A0250_70_A0360_00-a70d4321
  - shard-SC_A0250_80_A0360_00-SC_A0250_90_A0360_00-SC_A0360_00_A0360_10-SC_A0360_10_A0360_20-111a0034
  - shard-SC_A0360_20_A0360_30-SC_A0360_30_A0360_40-SC_A0360_40_A0360_50-SC_A0360_50_A0360_60-32a42b67
  - shard-SC_A0360_60_A0360_70-SC_A0360_70_A0360_80-SC_A0360_80_A0360_90-SC_A0360_90_A0370_00-08a18ac8
  - shard-SC_A0370_00_A0370_10-SC_A0370_10_A0370_20-SC_A0370_20_A0370_30-SC_A0370_30_A0370_40-0c38871c
  - shard-SC_A0370_40_A0370_50-SC_A0370_50_A0370_60-SC_A0370_60_A0370_70-SC_A0370_70_A0370_80-62e719a3
  - shard-SC_A0370_80_A0370_90-SC_A0370_90_A0380_00-SC_A0380_00_A0380_10-SC_A0380_10_A0380_20-4495712f
  - shard-SC_A0380_20_A0380_30-SC_A0380_30_A0380_40-SC_A0380_40_A0380_50-SC_A0380_50_A0390_50-3f731099
  - shard-SC_A0390_50_A0390_60-SC_A0390_60_A0390_70-SC_A0390_70_A0390_80-SC_A0390_80_A0390_90-b6854c17
  - shard-SC_A0390_90_A0400_00-SC_A0400_00_A0400_10-SC_A0400_10_A0400_20-SC_A0400_20_A0400_30-968689be
  - shard-SC_A0400_30_A0400_40-SC_A0400_40_A0400_50-SC_A0400_50_A0400_60-SC_A0400_60_A0400_70-77e068d6
  - shard-SC_A0400_70_A0400_80-SC_A0400_80_A0400_90-SC_A0400_90_A0410_00-SC_A0410_00_A0410_10-1c5e735a
  - shard-SC_A0410_10_A0410_20-SC_A0410_20_A0410_30-SC_A0410_30_A0410_40-SC_A0410_40_A0410_50-360a5cf4
  - shard-SC_A0410_50_A0410_60-SC_A0410_60_A0410_70-SC_A0410_70_A0410_80-SC_A0410_80_A0410_90-63600c93
  - shard-SC_A0410_90_A0420_00-SC_A0420_00_A0420_10-SC_A0420_10_A0420_20-SC_A0420_20_A0420_30-07ea67c0
  - shard-SC_A0420_30_A0420_40-SC_A0420_40_A0420_50-SC_A0420_50_A0420_60-SC_A0420_60_A0420_70-847eb965
  - shard-SC_A0420_70_A0420_80-SC_A0420_80_A0420_90-SC_A0420_90_A0430_00-SC_A0430_00_A0430_10-4d2c5401
  - shard-SC_A0430_10_A0430_20-SC_A0430_20_A0430_30-SC_A0430_30_A0430_40-SC_A0430_40_A0430_50-f7f8c6dc
  - shard-SC_A0430_50_A0430_60-SC_A0430_60_A0430_70-SC_A0430_70_A0430_80-SC_A0430_80_A0430_90-765e27d5
  - shard-SC_A0430_90_A0440_00-SC_A0440_00_A0440_10-SC_A0440_10_A0440_20-SC_A0440_20_A0440_30-315db8b1
  - shard-SC_A0440_30_A0440_40-SC_A0440_40_A0440_50-SC_A0440_50_A0440_60-SC_A0440_60_A0440_70-9c29aec4
- Checkpoint debt: NONE
- Deterministic closure validation: JSON duplicate-key guard, exact filtered indexes, speaker maps, accuracy QC, literary QC, arbitration artifacts, CP932, exclusion gates PASS
- Translation debt: NONE within the translatable campaign set
- QC debt: NONE

## Wave 2

- Status: COMPLETED 2026-08-20T04:35:13Z
- Requested scene count: 24 (6 shards x 4 contiguous scenes)
- Planned first/last scene: SC_A0110_10_A0110_20 / SC_A0130_20_A0130_30
- Intended GitHub remote: Mitchobrienpouet/Tsuyokiss
- Intended branch: main
- Last remotely verified commit: 994448d93859a8f95f41239af0a33d8021478852
- Claimed shard IDs:
  - shard-SC_A0110_10_A0110_20-SC_A0110_20_A0110_30-SC_A0110_30_A0110_40-SC_A0110_40_A0110_50-a1e1695b
  - shard-SC_A0110_50_A0110_60-SC_A0110_60_A0110_70-SC_A0110_70_A0110_80-SC_A0110_80_A0110_90-22f4e9e3
  - shard-SC_A0110_90_A0120_00-SC_A0120_00_A0120_05-SC_A0120_05_A0120_10-SC_A0120_10_A0120_20-4c011219
  - shard-SC_A0120_20_A0120_30-SC_A0120_30_A0120_40-SC_A0120_40_A0120_50-SC_A0120_50_A0120_60-53224de9
  - shard-SC_A0120_60_A0120_70-SC_A0120_70_A0120_80-SC_A0120_80_A0120_85-SC_A0120_85_A0120_90-db235a17
  - shard-SC_A0120_90_A0130_00-SC_A0130_00_A0130_10-SC_A0130_10_A0130_20-SC_A0130_20_A0130_30-881d3cea
- Execution mode: six claimed shards, processed by three Codex Work workers in rolling pairs
- Completed coverage: 24/24 scenes, 621/621 source rows
- Deterministic validation: JSON, exact indexes, duplicate-key guard, QC artifacts, arbitration artifacts, CP932 PASS
- Translation debt: NONE within the wave
- QC debt: NONE
- Checkpoint debt: NONE

## Wave 1

- Status: COMPLETED 2026-08-19T12:22:44Z
- Requested scene count: 24 (6 shards x 4 contiguous scenes)
- Planned first/last scene: SC_A0100_01_A0100_02 / SC_A0110_00_A0110_10
- Intended GitHub remote: Mitchobrienpouet/Tsuyokiss
- Intended branch: main
- Last remotely verified commit: 4baa70e19e0477da0d405bca822fb815f0473802
- Claimed shard IDs:
  - shard-SC_A0100_01_A0100_02-SC_A0100_02_A0100_03-SC_A0100_03_A0100_04-SC_A0100_04_A0100_05-75634a76
  - shard-SC_A0100_06_A0100_10-SC_A0100_07_A0100_10-SC_A0100_08_A0100_10-SC_A0100_10_A0100_12-7b8e7796
  - shard-SC_A0100_12_A0100_14-SC_A0100_14_A0100_16-SC_A0100_16_A0100_18-SC_A0100_18_A0100_20-72eb62a6
  - shard-SC_A0100_20_A0100_22-SC_A0100_22_A0100_24-SC_A0100_24_A0100_30-SC_A0100_30_A0100_32-e2671108
  - shard-SC_A0100_32_A0100_40-SC_A0100_40_A0100_50-SC_A0100_50_A0100_60-SC_A0100_60_A0100_70-0881c9b2
  - shard-SC_A0100_70_A0100_80-SC_A0100_80_A0100_90-SC_A0100_90_A0110_00-SC_A0110_00_A0110_10-bdde9009
- Execution mode: six claimed shards, processed by three Codex Work workers in rolling pairs
- CLI bootstrap debt: two preflight launch attempts failed before thread creation; no source or translation file was written
- Completed coverage: 24/24 scenes, 673/673 source rows
- Deterministic validation: JSON, exact indexes, duplicate-key guard, QC artifacts, arbitration artifacts, CP932 PASS
- Translation debt: NONE
- QC debt: NONE
- Checkpoint debt: NONE

Change `Status` to `FIRED <UTC timestamp>` and record claimed shard/run IDs in
the same checkpoint that launches the wave. Update the last remotely verified
commit only after checking that the intended remote branch contains it.
