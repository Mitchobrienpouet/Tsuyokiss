# Full-route F targeted translation repair handoff

Date: 2026-08-22  
Stage: targeted post-readthrough translation repair only  
Status: **COMPLETED**  
Source finding: `F-m01` in
`scratchpad/readthrough/full_route_F_critical_20260822.md`  
Changed translation indexes: **1**  
Blockers: **NONE**

This repair was limited to the sole confirmed route-F readthrough finding. It
changed one target line and this handoff only. No surrounding prose, source or
model projection, QC, arbitration, readthrough, bible, exclusion, gate,
configuration, pipeline, state, or Git artifact was edited.

## Exact target-text change

| Scene:index | Before | After | Reason |
|---|---|---|---|
| `SC_F0630_00_F0640_00:7` | `「Now then, the rest of Mr. Tsushima's long-time family should come along as well.」` | `「Then let's have the Tsushima family, who've known him for years, come along too.」` | Preserve the established `Tsushima family` friend-group label while attaching the long-standing relationship to the friends' history with Leo, not to a literal family. |

Filtered source row 7 is Inori's dialogue. The replacement preserves her
invitation, the inclusion of the `Tsushima family`, the long-standing
relationship, and the Japanese corner-quote wrapper. Speaker mapping remains
`祈 -> Inori`. Materially contested readings introduced by this repair:
**NONE**.

## Files changed

- `translations/SC_F0630_00_F0640_00.json`
- `scratchpad/contested/full_route_F_repair_handoff_20260822.md`

## Deterministic validation

| Gate | Result |
|---|---|
| JSON and internal file identity | PASS |
| Exact permitted join | PASS: 23/23 indexes, 0 missing/extra/excluded |
| Public project validator | PASS: `SC_F0630_00_F0640_00: OK (23/23 rows)` |
| Source identity | PASS: index 7 remains joined to engine ID `B0034:SC_F0630_00_F0640_00 //意識野ＧＯＧＯＧＯ！:0007` and source SHA-256 `b9da2afab7aaf4c5968b2893d77d1ddf49e351ccc1d2fd4309f2527fda59e553` |
| Speaker map | PASS: `祈 -> Inori` |
| Dialogue wrapper | PASS: `「...」` retained |
| CP932 | PASS: all 23 target strings encode strictly |

Existing accuracy, literary, arbitration, and readthrough records were
intentionally left untouched. Any required post-repair recertification and
readthrough closure remain separate downstream stages.
