# Full-route G targeted translation repair handoff

Date: 2026-08-22  
Stage: targeted post-readthrough translation repair only  
Status: **COMPLETED**  
Scope: all 3 major and 4 minor findings in
`scratchpad/readthrough/full_route_G_critical_20260822.md`  
Changed translation indexes: **13**  
Blockers: **NONE**

This repair applies only the source-faithful decisions recorded by the critical
readthrough. It does not reopen unrelated prose, bridge an exclusion, or create
a new contested alternative. No QC, per-scene arbitration, readthrough, bible,
source, exclusion, configuration, pipeline, state, or Git artifact was edited.

The relevant continuity specs already require `Crab`, English given-name-first
order, exact dialogue wrappers, source-bounded characterization, and preserved
reveal timing. No spec was contradictory, so no spec update was required.

## 1. Wrapper and presentation repairs

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_G0500_00_G0520_00:46` | `「Don't worry about me. I'll explain everything properly on Sunday or so, so until then, please just leave me alone.」` | `"Don't worry about me. I'll explain everything properly on Sunday or so, so until then, please just leave me alone."` | The filtered source row is unvoiced narration containing an embedded quotation, not spoken dialogue; replace the incorrect corner wrapper with ASCII quotation marks. |
| `SC_G0650_00_G0700_00:50` | `Summer really brings out the weirdos.` | `「(Munch, munch.) Summer really brings out the weirdos.」` | Restore Leo's dialogue wrapper and the explicit `（もぐもぐ）` eating beat. |

## 2. Locked `Crab` nickname

All four listed rows use source `カニっち`. The local spec and bible lock this
nickname to `Crab`; the stale `Kani` form is not retained.

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_G0650_00_G0700_00:10` | `「Let's see Kani's call history...」` | `「Let's see Crab's call history...」` | Restore the recurring nickname lock. |
| `SC_G0650_00_G0700_00:13` | `「Still, I guess Kani really is someone I need to keep an eye on.」` | `「Still, I guess Crab really is someone I need to keep an eye on.」` | Restore the recurring nickname lock. |
| `SC_G0650_00_G0700_00:14` | `「Come on, wake up. Wake up, Kani.」` | `「Come on, wake up. Wake up, Crab.」` | Restore direct nickname address. |
| `SC_G0650_00_G0700_00:24` | `「Leo said waking Kani up takes a lot of work.」` | `「Leo said waking Crab up takes a lot of work.」` | Restore the recurring nickname lock. |

Route-wide post-repair target search: standalone `Kani` returns zero G-route
occurrences. Legitimate `Kinu Kanisawa` full-name uses remain unchanged.

## 3. Source-bounded breakdown description

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_G0800_00_G0850_00:96` | `She crouched in the corner, groaning and apologizing to something only she could see.` | `She groaned in the corner of the room, apologizing to something unseen.` | Source `部屋の隅でうめきながら見えない何かに謝ってた` supplies neither a crouching posture nor a claim that Yoshimi visually perceives an entity. Remove both unsupported additions without adding a diagnosis. |

## 4. English full-name order

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_G0650_00_G0700_00:223` | `「Hold on. Tsushima Leo isn't the kind of cold-blooded guy who ignores someone who needs help.」` | `「Hold on. Leo Tsushima isn't the kind of cold-blooded guy who ignores someone who needs help.」` | Apply the bible-locked `Leo Tsushima` order; preserve the rest of Leo's self-description. |

## 5. `JoySta 2` source gloss

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_G0800_00_G0850_00:54` | `「Oh, you have a JoySta 2 in here. That's unexpected.」` | `「Oh, you have a JoySta 2 game console in here. That's unexpected.」` | Restore the explicit source gloss `（ゲーム機）` without inventing a different product or brand. |

## 6. Translationese cleanup

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_G0760_00_G0800_00:93` | `「I already loved you, Leo, but after what you just said I love you even, even more...」` | `「I already loved you, Leo, but after what you just said, I love you so, so much more...」` | Preserve emphatic `もっともっと` in natural Yoshimi dialogue. |
| `SC_G0800_00_G0850_00:77` | `「Mmm. This kind of thing really makes me feel like I'm enjoying a woman's happiness.」` | `「Mmm. This really does feel like one of the joys of being a woman.」` | Preserve `女の幸せを実感できる` while removing literal Japanese syntax. |

## 7. Referential and temporal discipline

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_G0870_00_G0900_00:144` | `「Yes... and that's where I met her.」` | `「Yes... and that's where I met someone.」` | Source withholds the object and gender before the orientation flashback; remove the dangling early `her`. |
| `SC_G0870_00_G0900_00:187` | `「...Your mother isn't here anymore.」` | `「...Your mother isn't here.」` | Source is spatial (`ここにはいない`) and does not imply prior local presence or death; remove unsupported `anymore`. |

## Files changed

Translation JSON:

- `translations/SC_G0500_00_G0520_00.json` — index 46
- `translations/SC_G0650_00_G0700_00.json` — indexes 10, 13, 14, 24, 50, 223
- `translations/SC_G0760_00_G0800_00.json` — index 93
- `translations/SC_G0800_00_G0850_00.json` — indexes 54, 77, 96
- `translations/SC_G0870_00_G0900_00.json` — indexes 144, 187

Handoff:

- `scratchpad/contested/full_route_G_repair_handoff_20260822.md`

Specs changed: **NONE**. Existing G specs already support every adopted repair.

## Deterministic validation

| Gate | Result |
| --- | --- |
| G model-source projections / translations | PASS: 38 / 38 and 38 / 38 |
| Exact permitted joins | PASS: 2,427 / 2,427; 0 missing, extra, reordered, or excluded keys |
| Projection scene/source labels | PASS: 38 / 38 exact stems |
| Source SHA-256 metadata | PASS: 2,427 / 2,427 recomputed from permitted projection text |
| Engine IDs | PASS: 2,427 unique and exact `B0035:<scene>:<zero-padded-index>` |
| Translation `file` metadata | PASS: 38 / 38 exact stems |
| Strict JSON / duplicate keys | PASS: all 38 projections and 38 translations |
| Speaker-map coverage | PASS: 1,625 / 1,625 voiced rows |
| Dialogue/narration wrappers | PASS: 2,427 / 2,427; previous two mismatches reduced to zero |
| CP932 | PASS: all 38 complete translation JSON files encode strictly |
| Forbidden typography / Japanese target text / placeholders | PASS: 0 findings |
| Exclusion boundary gate | PASS: 601 projected-scene exclusions absent; no excluded key entered a translation |
| G narrative gates | PASS: no G-route mirror/repeated-choice entry is configured |
| Manifest and translation-identity unit tests | PASS: 10 / 10 |
| Obsolete repaired-form scan | PASS: 0 standalone `Kani`, `Tsushima Leo`, unsupported crouch/visual phrase, old translationese, old `JoySta 2` line, early `met her`, or `isn't here anymore` occurrences |
| Corrected-block reread | PASS: all 13 repaired rows reread with their adjacent permitted context |

All readthrough findings are resolved at the translation-repair stage. Existing
QC, per-scene arbitration, and readthrough records were intentionally left
unchanged for their downstream recertification lanes.
