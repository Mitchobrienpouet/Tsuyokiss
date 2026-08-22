# Full-route J targeted translation repair handoff

Date: 2026-08-22  
Stage: targeted post-readthrough translation repair only  
Status: **COMPLETED**  
Source findings: `J-B01` and `J-m01` in
`scratchpad/readthrough/full_route_J_critical_20260822.md`  
Changed translation indexes: **3**  
Blockers: **NONE**

This repair changed only the three approved target rows and this handoff. No
surrounding prose, source/model projection, QC, arbitration, readthrough,
exclusion, gate, configuration, pipeline, state, or Git artifact was edited.
The existing preflight specifications do not prescribe either contradictory
wording, so no spec update was required.

## Exact target-text changes

| Scene:index | Before | After | Reason |
|---|---|---|---|
| `SC_J0100_03_J0100_04:2` | `The Ryuumeikan student-council room, also known as the Dragon Palace.` | `The Ryuumeikan student-council room, also known as Ryugu.` | Restore the bible-locked proper name `Ryugu` for source `竜宮`; retain the narration wrapper state and room/appositive structure. |
| `SC_J0100_08_J0100_09:29` | `「It's fine for the client to worry because his daughter's been down lately, but hiring a detective to investigate her feels kind of petty.」` | `「It's fine for the client to worry because their daughter's been down lately, but hiring a detective to investigate her feels kind of petty.」` | Source `依頼主` does not mark the client's gender. Singular `their` removes the invented male identity without anticipating the later mother reveal. |
| `SC_J0100_08_J0100_09:32` | `「The client also said that if anyone's bullying his daughter, we should teach them a painful lesson.」` | `「The client also said that if anyone's bullying their daughter, we should teach them a painful lesson.」` | Keep the still-anonymous client gender-neutral and preserve Serori's stated instruction and threat. |

The explicit Yoshimi-mother reveal at `SC_J0100_20_Z9999_99:68,76-77`
remains untouched. Materially contested readings introduced by this repair:
**NONE**.

## Files changed

- `translations/SC_J0100_03_J0100_04.json`
- `translations/SC_J0100_08_J0100_09.json`
- `scratchpad/contested/full_route_J_repair_handoff_20260822.md`

## Deterministic validation

| Gate | Result |
|---|---|
| JSON and internal file identity | PASS: 2/2 scenes |
| Exact permitted joins | PASS: `76/76` and `47/47`; 0 missing, extra, or excluded indexes |
| Public project validator | PASS: both scenes reported exact `OK` counts |
| Source identity | PASS: all 123 permitted engine IDs and source hashes remain joined to the same indexes |
| Speaker maps | PASS: unchanged and complete |
| Wrappers | PASS: J0100_03:2 remains unwrapped narration; J0100_08:29,32 retain `「...」` dialogue wrappers |
| CP932 | PASS: all 123 target strings encode strictly |
| Obsolete-form sentinels | PASS: zero `his daughter` or `Dragon Palace` occurrences remain in route-J translations |

Existing accuracy, literary, arbitration, and readthrough records were
intentionally left untouched. Independent post-repair recertification and
corrected-block reread closure remain separate downstream stages.
