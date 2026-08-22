# Route J targeted literary repair handoff - 2026-08-22

Stage: targeted literary translation repair  
Status: **COMPLETED**  
Changed translation rows: **4**  
Source findings: the open minor findings in the frozen literary reports for `SC_J0100_03_J0100_04` and `SC_J0100_08_J0100_09`

This repair changes only the two target translation files and this new handoff. Existing accuracy/literary QC, arbitration/contested records, readthrough reports, projections, exclusions, state, configuration, and pipeline artifacts remain untouched. No Git operation was performed.

## Exact changes

| Scene:index | Before | After | Reason |
|---|---|---|---|
| `SC_J0100_03_J0100_04:54` | `Everyone made an uncertain face.` | `Everyone looked dubious.` | Replaces a non-idiomatic facial-expression collocation while preserving the ensemble's unconvinced reaction to Inori. |
| `SC_J0100_03_J0100_04:70` | `「(Sato sure sticks close to Leo a lot.)」` | `「(Sato sure sticks awfully close to Leo.)」` | Removes the redundant `sticks close ... a lot` construction while preserving Shinichi's jealous observation and the internal-dialogue wrapper. |
| `SC_J0100_08_J0100_09:16` | `「Takane really is useless.」` | `「Takane really is useless, huh?」` | Restores the playful, drawn-out taunting cadence carried by `ね～（・ε・）` without mechanically importing the kaomoji. This keeps Umi airy and supplies the beat for Takane's immediate outrage. |
| `SC_J0100_08_J0100_09:34` | `「What about that walking firearms-and-swords-law violation?」` | `「What about that walking violation of the Firearms and Swords Control Law?」` | Removes the stacked translationese compound while preserving the legal-reference joke, Otome referent, and Takane's irritated voice. |

## Preserved continuity and accuracy sentinels

- `SC_J0100_03_J0100_04:2` remains `The Ryuumeikan student-council room, also known as Ryugu.`
- `SC_J0100_03_J0100_04:13` remains `「I think Crab's impression of you is pretty spot-on, Senpai.」`; Kinu remains the imitator and Leo the target.
- `SC_J0100_08_J0100_09:29,32` retain gender-neutral `their daughter`; the client is not identified before the later mother reveal.
- No later reveal line was edited.

## Deterministic validation

- Public overlay-aware `codex_vn_pipeline.validate_scene(..., quiet=True)`: **PASS** for both scenes with zero problems.
- Strict JSON, duplicate-key rejection, and internal `file` identity: **PASS**.
- Exact filtered projection joins: **PASS**, `76/76` and `47/47` (`123/123` aggregate); zero missing, extra, or excluded indexes.
- Projection counts, 123 unique/nonempty engine IDs, and 123 source hashes: **PASS**.
- Speaker maps and dialogue/narration wrappers: **PASS**, zero mismatches.
- Targeted repairs and preserved continuity/accuracy sentinels: **PASS**.
- CP932 encoding and forbidden typography: **PASS** for every translated line and speaker-map value.
- Stale target forms from all four findings: **0**.

Blockers: **NONE**. The two repaired translations are frozen for downstream recertification.
