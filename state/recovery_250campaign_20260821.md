# Tsuyokiss 250-scene campaign recovery — 2026-08-21

Status: ACTIVE RECOVERY / WAVES RESUMED

## Source recovery

The historical multipart `Tsuyokiss_Full_Edition.zip.001`–`.008` objects remain indexed in the file library but are not currently materializable. Recovery therefore uses the banked Tsuyokiss wordwrap test package as an alternate local source.

Recovered local source:
- `data.fpk` from `Tsuyokiss_Wordwrap_Test_01.zip`
- ZLC2 decode: 547 blocks
- decoded payload size: 14,573,517 bytes
- decoded SHA-256: `a05e29c33ac2416f5c3390b25455dbc829ac65454bb6a58b603d089f99a41282`
- scenario extraction: 59,773 messages across 835 `SC_*` scenes
- relevant scenario blocks: 0028–0040

The recovered source contains the C-route scenes needed beyond completed 250-campaign shard 22, including `SC_C0200_00_C0300_00`, `SC_C0300_00_C0330_00`, `SC_C0330_00_C0350_00`, `SC_C0350_00_C0400_00`, and subsequent C-route scenes.

## Campaign front

Completed commit history is preserved through 250-campaign shard 22.

Shard 23 recovered scene set:
1. `SC_C0200_00_C0300_00`
2. `SC_C0300_00_C0330_00`
3. `SC_C0330_00_C0350_00`
4. `SC_C0350_00_C0400_00`

All four translations are already banked on `codex/wave-300-continuation-20260820`. Accuracy QC is banked for all four; literary QC is also present. Existing content exclusions remain authoritative, including omitted ranges in `SC_C0300_00_C0330_00` and `SC_C0330_00_C0350_00`. Do not reconstruct excluded text.

Shard 24 begins with `SC_C0400_10_C0400_30`, `SC_C0400_20_C0400_30`, `SC_C0400_30_C0450_00`, and `SC_C0450_00_C0500_00`; banked translation payloads are being recovered/validated before promotion. Existing shard-24 exclusions remain authoritative.

No completed scene is to be retransmitted, rewritten, or retranslated merely because the prior campaign checkpoint was incomplete.
