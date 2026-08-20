# Wave ledger

## 200-scene campaign

- Status: FIRED 2026-08-20T04:35:53Z
- Requested scene count: 200 (50 shards x 4 contiguous scenes)
- Planned first/last scene: SC_A0130_30_A0130_40 / SC_A0440_60_A0440_70
- Active concurrency: 6 shards; shards 7-12 are preflight-cache only and NOT FIRED
- Durable shard plan: `state/preflight_cache_plan.md`
- Intended GitHub remote/branch: Mitchobrienpouet/Tsuyokiss / main
- Last remotely verified commit at launch: 994448d93859a8f95f41239af0a33d8021478852
- Fired shard IDs:
  - shard-SC_A0130_30_A0130_40-SC_A0130_40_A0130_50-SC_A0130_50_A0130_60-SC_A0130_60_A0130_70-f97d2848
  - shard-SC_A0130_70_A0130_80-SC_A0130_80_A0130_90-SC_A0130_90_A0140_00-SC_A0140_00_A0140_10-44b07c85
  - shard-SC_A0140_10_A0140_20-SC_A0140_20_A0140_30-SC_A0140_30_A0140_40-SC_A0140_40_A0140_50-1af726e0
  - shard-SC_A0140_50_A0140_60-SC_A0140_60_A0140_70-SC_A0140_70_A0140_80-SC_A0140_80_A0140_90-09710444
  - shard-SC_A0140_90_A0150_00-SC_A0150_00_A0150_10-SC_A0150_10_A0150_20-SC_A0150_20_A0150_30-56cf8cb7
  - shard-SC_A0150_30_A0150_40-SC_A0150_40_A0150_50-SC_A0150_50_A0150_60-SC_A0150_60_A0150_70-4821536a
- Checkpoint debt: NONE

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
