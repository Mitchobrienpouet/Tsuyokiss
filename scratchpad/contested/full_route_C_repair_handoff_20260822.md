# Full-route C targeted translation repair handoff

Date: 2026-08-22  
Stage: targeted post-readthrough translation repair only  
Status: **COMPLETED**  
Scope: all 4 blocking, 2 major, and 1 minor findings in
`scratchpad/readthrough/full_route_C_critical_20260822.md`  
Changed translation indexes: **29**  
Blockers: **NONE**

The supervisor supplied the final decisions for every finding. This repair
therefore applies only the approved source-faithful changes below; it does not
reopen unrelated prose or create new alternatives. No QC, per-scene
arbitration, readthrough, bible, source, exclusion, configuration, pipeline,
state, or Git artifact was edited.

## 1. Canonical Shinichi surname: `Samesuga`

Decision: normalize every listed `鮫氷` occurrence and the phonetic chant to
`Samesuga`, grounded in explicit source ruby/reading. Preserve `Shinichi`,
`Fukahire`, and explicit `Shark` uses.

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_C0100_00_K0900_00:39` | `「Samehyo, can ask you question?」` | `「Samesuga, can ask you question?」` | Correct surname reading; Tonfa's clipped grammar is unchanged. |
| `SC_C0180_00_K0900_00:23` | `Shinichi Samehyo's Matchmaking Service.` | `Shinichi Samesuga's Matchmaking Service.` | Correct surname in the business name. |
| `SC_C0180_00_K0900_00:57` | `Practice Date with Shinichi Samehyo Standing In for Subaru Date. (I give it my all, even in practice.)` | `Practice Date with Shinichi Samesuga Standing In for Subaru Date. (I give it my all, even in practice.)` | Correct full name only. |
| `SC_C0180_00_K0900_00:58` | `Post-Rejection Aftercare with Shinichi Samehyo. (Thorough care guaranteed.)` | `Post-Rejection Aftercare with Shinichi Samesuga. (Thorough care guaranteed.)` | Correct full name only. |
| `SC_C0180_00_K0900_00:59` | `Play Lovers with Shinichi Samehyo Standing In for Subaru Date. (I fully commit to the role.)` | `Play Lovers with Shinichi Samesuga Standing In for Subaru Date. (I fully commit to the role.)` | Correct full name only. |
| `SC_C0400_30_C0450_00:288` | `「Samehyo, you're saying your inner monologue out loud. And no.」` | `「Samesuga, you're saying your inner monologue out loud. And no.」` | Correct direct surname address. |
| `SC_C0550_00_C0600_00:84` | `Shinichi Samehyo had confessed to a girl and been resoundingly rejected, driving him to distrust humanity while he was still in elementary school.` | `Shinichi Samesuga had confessed to a girl and been resoundingly rejected, driving him to distrust humanity while he was still in elementary school.` | Correct full name in narration. |
| `SC_C0550_00_C0600_00:296` | `「Samehyo. I heard every word.」` | `「Samesuga. I heard every word.」` | Correct direct surname address. |
| `SC_C0600_40_C0650_00:331` | `「Please do. I contacted Samejima's parents, and it appears he never made it home.」` | `「Please do. I contacted Samesuga's parents, and it appears he never made it home.」` | Correct surname and preserve parent/contact proposition. |
| `SC_C0600_40_C0650_00:339` | `「Samejima. So you were here after all.」` | `「Samesuga. So you were here after all.」` | Correct direct surname address. |
| `SC_C0600_40_C0650_00:623` | `「We deeply apologize. Commentator Samejima has been transported to the hospital following a sudden illness.」` | `「We deeply apologize. Commentator Samesuga has been transported to the hospital following a sudden illness.」` | Correct commentator surname only. |
| `SC_C0600_40_C0650_00:2186` | `「Samejima!」` | `「Samesuga!」` | Correct roll-call surname. |
| `SC_C0600_40_C0650_00:2199` | `「Incidentally, Samejima and Mana will have no summer vacation. May the storm of remedial classes drive you to a frenzied death.」` | `「Incidentally, Samesuga and Mana will have no summer vacation. May the storm of remedial classes drive you to a frenzied death.」` | Correct surname only. |
| `SC_C0950_00_C0960_00:12` | `「Samehyo, please come back.」` | `「Samesuga, please come back.」` | Correct direct surname address. |
| `SC_C0950_00_C0960_00:19` | `「Sa-me-hyo! Sa-me-hyo!」` | `「Sa-me-su-ga! Sa-me-su-ga!」` | Match explicit phonetic source chant `さーめすがっ`. |

Post-repair C search: `Samehyo`, `Samejima`, and `Sa-me-hyo` each return zero
target occurrences; the 15 approved rows use `Samesuga`/`Sa-me-su-ga`.

## 2. Canonical island name: `Ikajima`

Decision: normalize all four listed `烏賊島` rows to the bible-locked proper
name `Ikajima`; do not translate the name ad hoc.

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_C0350_00_C0400_00:168` | `「That was a joke. Today we will swim to Ika Island.」` | `「That was a joke. Today we will swim to Ikajima.」` | Restore locked proper name. |
| `SC_C0500_00_C0550_00:130` | `「Ika Island, owned by Ryuumeikan Academy.」` | `「Ikajima, owned by Ryuumeikan Academy.」` | Restore locked proper name; ownership remains unchanged. |
| `SC_C0600_40_C0650_00:322` | `「Was Fukahire on the boat back from Squid Island?」` | `「Was Fukahire on the boat back from Ikajima?」` | Restore locked proper name. |
| `SC_C0600_40_C0650_00:330` | `「Full speed to Squid Island!」` | `「Full speed to Ikajima!」` | Restore locked proper name. |

Post-repair C search: `Ika Island` and `Squid Island` each return zero target
occurrences.

## 3. Withheld crush gender

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_C0330_00_C0350_00:45` | `「Anyway, I don't know who she is, but good luck. I'm rooting for you.」` | `「Anyway, I don't know who they are, but good luck. I'm rooting for you.」` | Source `誰か` is gender-neutral; preserve the unknown referent until the later Kinu reveal. |

Only the gendered referent changed. The existing `Anyway`, encouragement, and
support remain intact.

## 4. Nakajima title/identity continuity

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_C0740_00_C0750_00:120` | `「Hello? Good evening, Ms. Nakajima.」` | `「Hello? Good evening, Mr. Nakajima.」` | The call is to the already-established male Yuihama track captain/recruiter. |

## 5. `Dragon` identification gloss

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_C0600_40_C0650_00:1367` | `「The Dragon has a strong reputation in martial arts and handball, but to be frank, its track program still has a long way to go.」` | `「The Dragon (Ryuumeikan) has a strong reputation in martial arts and handball, but to be frank, its track program still has a long way to go.」` | Restore explicit source parenthetical `ドラゴン（竜鳴館のこと）` without discarding the nickname. |

## 6. Direct `Crabby` / `Crab` address locks

Decision: use established `Crabby` for direct `カニち/カニっち` and `Crab`
for the manager's direct `カニさん`. Third-person given-name uses and Leo's
later explicit switch to `Kinu` remain untouched.

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_C0100_00_K0900_00:5` | `「Oh, Kinu. See, we have cleaning duty, but Date is asleep...」` | `「Oh, Crabby. See, we have cleaning duty, but Date is asleep...」` | Restore direct `カニち` nickname; preserve Tonfa's clipped voice. |
| `SC_C0100_00_K0900_00:20` | `「Kinu very amazing.」` | `「Crabby very amazing.」` | Restore direct `カニち` nickname; preserve clipped grammar. |
| `SC_C0120_00_K0900_00:95` | `「Kinu!」` | `「Crabby!」` | Restore direct `カニっち` call. |
| `SC_C0330_00_C0350_00:120` | `「Kinu, it's amazing how you can say whatever you want to a boy's face.」` | `「Crabby, it's amazing how you can say whatever you want to a boy's face.」` | Restore direct `カニっち` address. |
| `SC_C0600_40_C0650_00:1803` | `「Come now, Kani-san. Eat all you want today.」` | `「Come now, Crab. Eat all you want today.」` | Remove untranslated hybrid and apply direct-address lock. |
| `SC_C0820_00_C0850_00:10` | `「Good morning, Tsushima. Kinu.」` | `「Good morning, Tsushima. Crabby.」` | Restore direct `カニっち` address. |

Post-repair C search: `Kani-san` returns zero target occurrences.

## 7. Merged-grammar residue

| Scene:index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_C0500_00_C0550_00:19` | `「Me, the spot where a certain someone punched me years ago is aching again.」` | `「The spot where a certain someone punched me years ago is aching again.」` | Remove the broken draft prefix while preserving the accuracy-corrected body location, agency, and vague attacker. |

## Files changed

Translation JSON:

- `translations/SC_C0100_00_K0900_00.json`
- `translations/SC_C0120_00_K0900_00.json`
- `translations/SC_C0180_00_K0900_00.json`
- `translations/SC_C0330_00_C0350_00.json`
- `translations/SC_C0350_00_C0400_00.json`
- `translations/SC_C0400_30_C0450_00.json`
- `translations/SC_C0500_00_C0550_00.json`
- `translations/SC_C0550_00_C0600_00.json`
- `translations/SC_C0600_40_C0650_00.json`
- `translations/SC_C0740_00_C0750_00.json`
- `translations/SC_C0820_00_C0850_00.json`
- `translations/SC_C0950_00_C0960_00.json`

Handoff:

- `scratchpad/contested/full_route_C_repair_handoff_20260822.md`

## Deterministic validation

| Gate | Result |
| --- | --- |
| C translation files | PASS: 37 / 37 |
| Exact permitted joins | PASS: 6,589 / 6,589; 0 missing, extra, or excluded keys |
| Per-scene project validator | PASS: 37 / 37 |
| Source SHA-256 metadata | PASS: 6,589 / 6,589 recomputed from permitted source bodies |
| Engine IDs | PASS: 6,589 / 6,589 exact `B0031:<scene>:<zero-padded-index>` and unique |
| Translation `file` metadata | PASS: 37 / 37 |
| Speaker-map coverage | PASS: all 4,979 voiced permitted rows resolve through their scene map |
| Dialogue/narration wrappers | PASS: 6,589 / 6,589 |
| CP932 | PASS: 6,589 / 6,589 target strings encode strictly |
| Forbidden typography | PASS: 0 findings |
| Exclusion manifest gate | PASS: 0 findings |
| Narrative source/translation gates | PASS: 0 findings |
| Obsolete repaired-form search | PASS: 0 `Samehyo`, `Samejima`, `Sa-me-hyo`, `Ika Island`, `Squid Island`, `Kani-san`, or `Ms. Nakajima` target occurrences |

All approved repair decisions are resolved at the translation stage. Existing
QC/arbitration/readthrough records were intentionally left unchanged and remain
the responsibility of their downstream recertification lanes.
