# Critical full-route speed readthrough: wave C

Date: 2026-08-22  
Stage: post-QC critical readthrough only  
Verdict: **PASS after repair, independent QC, and arbitration closure**  
Translation changes: NONE

## Scope and evidence

I read all 37 current `SC_C` translation files continuously in scene order,
covering exactly 6,589 permitted rows. Suspicious passages were checked against
their manifest-permitted authoritative source rows, stable row hashes, engine
IDs, speaker metadata, surrounding reveal chronology, the C continuity specs,
the project bible/glossary/style/character locks, and the existing accuracy,
literary, and arbitration records.

The authoritative C inventory contains 45 source scenes and 8,472 raw rows.
Configured exclusions remove 1,883 rows: 1,289 rows in eight fully excluded
scenes and 594 rows inside the 37 translated scenes. The resulting public
translation/readthrough scope is exactly 6,589 rows. No excluded row was read,
quoted, summarized, bridged, or reconstructed.

All 37 accuracy records, 37 literary records, and 37 arbitration/no-op records
were present and reviewed. Persistent C model-source projection files are not
present in the current tree. Source-trigger verification therefore used only
exact manifest-permitted rows through the project's fail-closed,
exclusion-aware loader; this report does not claim a persisted projection-file
hash audit.

This pass changed no translation, QC, arbitration, source, exclusion,
configuration, pipeline, or Git artifact.

## Deterministic validation

| Gate | Result |
| --- | --- |
| Translation files | PASS: 37 |
| Permitted rows | PASS: 6,589 / 6,589 |
| Raw rows / excluded rows | 8,472 / 1,883 |
| Exact permitted index joins | PASS: 0 missing, extra, or excluded keys |
| Fully excluded artifacts | PASS: all 8 scenes remain translation/QC/arbitration-free |
| Engine IDs | PASS: 6,589 present, unique, and exactly `B0031:<scene>:<zero-padded-index>` |
| Source SHA-256 metadata | PASS: 6,589 / 6,589 recompute from the permitted Japanese body |
| Translation JSON/file metadata | PASS: duplicate-key rejection and all 37 `file` labels |
| Speaker-map coverage | PASS: 0 permitted source speakers missing |
| Project per-scene validator | PASS: 37 / 37 |
| Dialogue/narration wrappers | PASS: 6,589 / 6,589 match authoritative row kind |
| CP932 encoding | PASS: 0 failures |
| Forbidden typography | PASS: 0 failures |
| Placeholder scan | PASS: no TODO, TBD, FIXME, untranslated, or replacement-character markers |
| Narrative/exclusion manifest gates | PASS: 0 findings |

The only Japanese-block code point found in target text is the source-exact
emoticon punctuation at `SC_C0600_40_C0650_00:1583`; accuracy QC explicitly
preserved both emoticons, so it is not untranslated script.

Deterministic validity does not override the open narrative, naming, lore, and
literary findings below.

## Blocking findings

### C-RT-001 -- Shinichi's surname is wrong in two different ways

- scene: `SC_C0100_00_K0900_00`; `SC_C0180_00_K0900_00`;
  `SC_C0400_30_C0450_00`; `SC_C0550_00_C0600_00`;
  `SC_C0600_40_C0650_00`; `SC_C0950_00_C0960_00`
- indexes: `[39]`; `[23,57,58,59]`; `[288]`; `[84,296]`;
  `[331,339,623,2186,2199]`; `[12,19]`
- severity: blocking
- category: lore / continuity
- current_text_and_minimal_source-faithful_direction:

| Scene:index | Current text | Minimal correction proposal |
| --- | --- | --- |
| `SC_C0100_00_K0900_00:39` | `「Samehyo, can ask you question?」` | `「Samesuga, can ask you question?」` |
| `SC_C0180_00_K0900_00:23` | `Shinichi Samehyo's Matchmaking Service.` | `Shinichi Samesuga's Matchmaking Service.` |
| `SC_C0180_00_K0900_00:57` | `Practice Date with Shinichi Samehyo Standing In for Subaru Date. (I give it my all, even in practice.)` | Replace `Samehyo` with `Samesuga`; preserve the rest. |
| `SC_C0180_00_K0900_00:58` | `Post-Rejection Aftercare with Shinichi Samehyo. (Thorough care guaranteed.)` | Replace `Samehyo` with `Samesuga`; preserve the rest. |
| `SC_C0180_00_K0900_00:59` | `Play Lovers with Shinichi Samehyo Standing In for Subaru Date. (I fully commit to the role.)` | Replace `Samehyo` with `Samesuga`; preserve the rest. |
| `SC_C0400_30_C0450_00:288` | `「Samehyo, you're saying your inner monologue out loud. And no.」` | Replace `Samehyo` with `Samesuga`; preserve the rest. |
| `SC_C0550_00_C0600_00:84` | `Shinichi Samehyo had confessed to a girl and been resoundingly rejected, driving him to distrust humanity while he was still in elementary school.` | Replace `Samehyo` with `Samesuga`; preserve the rest. |
| `SC_C0550_00_C0600_00:296` | `「Samehyo. I heard every word.」` | `「Samesuga. I heard every word.」` |
| `SC_C0600_40_C0650_00:331` | `「Please do. I contacted Samejima's parents, and it appears he never made it home.」` | Replace `Samejima` with `Samesuga`; preserve the rest. |
| `SC_C0600_40_C0650_00:339` | `「Samejima. So you were here after all.」` | `「Samesuga. So you were here after all.」` |
| `SC_C0600_40_C0650_00:623` | `「We deeply apologize. Commentator Samejima has been transported to the hospital following a sudden illness.」` | Replace `Samejima` with `Samesuga`; preserve the rest. |
| `SC_C0600_40_C0650_00:2186` | `「Samejima!」` | `「Samesuga!」` |
| `SC_C0600_40_C0650_00:2199` | `「Incidentally, Samejima and Mana will have no summer vacation. May the storm of remedial classes drive you to a frenzied death.」` | Replace `Samejima` with `Samesuga`; preserve the rest. |
| `SC_C0950_00_C0960_00:12` | `「Samehyo, please come back.」` | `「Samesuga, please come back.」` |
| `SC_C0950_00_C0960_00:19` | `「Sa-me-hyo! Sa-me-hyo!」` | `「Sa-me-su-ga! Sa-me-su-ga!」` |

- source_evidence: The listed kanji rows use `鮫氷`. The same C route spells the
  surname out phonetically at `SC_C0950_00_C0960_00:19` as
  `さーめすがっ、さーめすがっ`. The authoritative introduction outside this
  route also supplies explicit ruby `鮫氷新一（さめすが しんいち）`.
- project_evidence: `bible/style.md` requires uncertain romanization to be
  contested instead of invented. The C0600 accuracy record incorrectly changed
  five `Samehyo` instances to `Samejima` while the other C scenes retained
  `Samehyo`. `scratchpad/readthrough/full_route_A_critical_20260822.md` already
  records the same source-ruby conflict and identifies `Samesuga` as the
  source-supported form.
- visual_evidence: NONE
- diagnosis: One recurring character has two incompatible C-route surnames,
  and both conflict with the explicit source reading. The error reaches full
  names, a business name, narration, direct address, roll call, and a phonetic
  chant.
- fix_direction: Reopen the naming authority through accuracy and targeted
  arbitration, canonize `Samesuga` unless a documented localization authority
  explicitly overrides the source ruby, update the surname lock, search the
  translated corpus, and normalize every confirmed occurrence. Preserve
  `Shinichi`, `Fukahire`, and explicit `Shark` uses.
- systemic: true
- status: closed by the route-C repair and independent QC

### C-RT-002 -- `Ikajima` is translated under two ad-hoc names

- scene: `SC_C0350_00_C0400_00`; `SC_C0500_00_C0550_00`;
  `SC_C0600_40_C0650_00`
- indexes: `[168]`; `[130]`; `[322,330]`
- severity: blocking
- category: lore / continuity
- current_text_and_minimal_source-faithful_direction:

| Scene:index | Current text | Minimal correction proposal |
| --- | --- | --- |
| `SC_C0350_00_C0400_00:168` | `「That was a joke. Today we will swim to Ika Island.」` | Replace `Ika Island` with `Ikajima`. |
| `SC_C0500_00_C0550_00:130` | `「Ika Island, owned by Ryuumeikan Academy.」` | `「Ikajima, owned by Ryuumeikan Academy.」` |
| `SC_C0600_40_C0650_00:322` | `「Was Fukahire on the boat back from Squid Island?」` | Replace `Squid Island` with `Ikajima`. |
| `SC_C0600_40_C0650_00:330` | `「Full speed to Squid Island!」` | `「Full speed to Ikajima!」` |

- source_evidence: All four permitted rows use the same proper name, `烏賊島`.
- project_evidence: `bible/glossary.md` locks `烏賊島 -> Ikajima` and expressly
  says not to translate the proper name ad hoc. Two C preflight/QC records
  instead introduced `Ika Island`, while the long scene independently used
  `Squid Island`.
- visual_evidence: NONE
- diagnosis: The Ryuumeikan-owned island acquires two English names within one
  route, and neither is the canonical glossary form.
- fix_direction: Route the four rows through terminology accuracy and targeted
  arbitration, normalize them to `Ikajima`, reconcile the stale C local spec/QC
  locks, search the corpus for the same source term, then revalidate the island
  arc.
- systemic: true
- status: closed by the route-C repair and independent QC

### C-RT-003 -- neutral unknown crush becomes `she` before the reveal

- scene: `SC_C0330_00_C0350_00`
- indexes: `[45]`
- severity: blocking
- category: reveal / hallucination
- current_text: `「I don't know who she is, but good luck. I'm rooting for
  you.」`
- source_evidence: `「とにかく誰か知らないけど頑張れよ、応援してやんから」`
  uses neutral `誰か` and supplies neither gender nor identity. At indexes
  38-39, Subaru has only said Leo probably does not know the person, and Leo
  wonders whether the person attends another school.
- project_evidence: The scene's accuracy record explicitly corrected indexes
  38-39 to preserve the withheld gender. The crush is not identified as Kinu
  until `SC_C0600_40_C0650_00:1408`.
- visual_evidence: NONE
- diagnosis: `she` narrows a deliberately unknown referent and contradicts the
  adjacent gender-neutral correction. This is an early reveal leak even though
  it does not yet disclose Kinu by name.
- fix_direction: Use a neutral referent, minimally `「I don't know who they are,
  but good luck. I'm rooting for you.」`, and reread the C0330 conversation and
  the later Kinu reveal.
- systemic: false
- status: closed by the route-C repair and independent QC

### C-RT-004 -- the male recruiter is addressed as `Ms. Nakajima`

- scene: `SC_C0740_00_C0750_00`
- indexes: `[120]`
- severity: blocking
- category: lore / continuity
- current_text: `「Hello? Good evening, Ms. Nakajima.」`
- source_evidence: `「あーもしもし。中島さん、こんばんわ」` uses the
  gender-neutral honorific. The same person is introduced at
  `SC_C0600_40_C0650_00:1347-1368` as a male speaker, Yuihama's track captain,
  with masculine narration; the current English already calls him
  `Mr. Nakajima` at index 1353.
- project_evidence: The C0740 accuracy/literary records retain the wrong title
  despite documenting Subaru's acceptance of that recruiter's school offer.
- visual_evidence: NONE
- diagnosis: The English changes an established male character's title and
  makes the acceptance call appear to target a different person.
- fix_direction: Minimally change the line to `「Hello? Good evening, Mr.
  Nakajima.」`; retain Subaru's polite call register and the offer timing.
- systemic: false
- status: closed by the route-C repair and independent QC

## Major findings

### C-RT-005 -- the recruiter omits the source's `Dragon = Ryuumeikan` gloss

- scene: `SC_C0600_40_C0650_00`
- indexes: `[1367]`
- severity: major
- category: meaning / lore
- current_text: `「The Dragon has a strong reputation in martial arts and
  handball, but to be frank, its track program still has a long way to go.」`
- source_evidence: `「ドラゴン（竜鳴館のこと）は武道やハンドボールには定評があるけど、正直陸上はまだまださ」`
  explicitly identifies the nickname in parentheses as Ryuumeikan.
- project_evidence: `bible/glossary.md` locks `竜鳴館 -> Ryuumeikan Academy` and
  warns against creating a different school name. The surrounding recruitment
  scene contrasts Yuihama with Subaru's current school.
- visual_evidence: NONE
- diagnosis: `The Dragon` is licensed by the dialogue, but dropping the
  parenthetical identification makes it read like an unexplained second school
  and removes an explicit source proposition.
- fix_direction: Preserve both pieces, minimally `「The Dragon (Ryuumeikan) has
  a strong reputation in martial arts and handball, but to be frank, its track
  program still has a long way to go.」` Do not replace the source nickname or
  add a new organization.
- systemic: false
- status: closed by the route-C repair and independent QC

### C-RT-006 -- direct-address `Crab/Crabby` lock is flattened or left Japanese

- scene: `SC_C0100_00_K0900_00`; `SC_C0120_00_K0900_00`;
  `SC_C0330_00_C0350_00`; `SC_C0600_40_C0650_00`;
  `SC_C0820_00_C0850_00`
- indexes: `[5,20]`; `[95]`; `[120]`; `[1803]`; `[10]`
- severity: major
- category: character / continuity
- current_text_and_minimal_source-faithful_direction:

| Scene:index | Current text | Minimal correction proposal |
| --- | --- | --- |
| `SC_C0100_00_K0900_00:5` | `「Oh, Kinu. See, we have cleaning duty, but Date is asleep...」` | Replace direct `Kinu` with `Crabby`. |
| `SC_C0100_00_K0900_00:20` | `「Kinu very amazing.」` | `「Crabby very amazing.」` |
| `SC_C0120_00_K0900_00:95` | `「Kinu!」` | `「Crabby!」` |
| `SC_C0330_00_C0350_00:120` | `「Kinu, it's amazing how you can say whatever you want to a boy's face.」` | Replace direct `Kinu` with `Crabby`. |
| `SC_C0600_40_C0650_00:1803` | `「Come now, Kani-san. Eat all you want today.」` | `「Come now, Crab. Eat all you want today.」` |
| `SC_C0820_00_C0850_00:10` | `「Good morning, Tsushima. Kinu.」` | Replace direct `Kinu` with `Crabby`. |

- source_evidence: The first, second, third, fourth, and sixth rows use direct
  `カニち/カニっち`; the manager directly uses `カニさーん` at C0600:1803.
- project_evidence: `bible/characters.md` and `bible/glossary.md` lock direct
  `カニ` as `Crab`; C-route literary precedent renders the affectionate
  `カニっち` variant as `Crabby` at C0600:1614 and 1843. C0600:1803 alone leaves
  the address as the untranslated hybrid `Kani-san`.
- visual_evidence: NONE
- diagnosis: Six direct addresses flatten a recurring relationship nickname,
  while one also leaks a Japanese romanization/honorific into otherwise
  localized English. Third-person uses of Kinu and natural pronouns are not
  included in this finding.
- fix_direction: Restore `Crabby` for direct `カニち/カニっち` and `Crab` for
  direct `カニさん`, then confirm the route-wide nickname policy in targeted
  terminology/literary arbitration. Do not replace legitimate given-name
  address after Leo explicitly switches to `Kinu`.
- systemic: true
- status: closed by the route-C repair and independent QC

## Minor findings

### C-RT-007 -- accuracy correction left a broken sentence opening

- scene: `SC_C0500_00_C0550_00`
- indexes: `[19]`
- severity: minor
- category: other
- current_text: `「Me, the spot where a certain someone punched me years ago is
  aching again.」`
- source_evidence: `「俺はなぁ。昔、誰かさんにブン殴られた所が また痛むんだよ」`
  says the place where Shinichi was punched is aching again. It does not require
  an isolated object-form `Me,` in English.
- project_evidence: The accuracy record correctly removed an invented knocked-
  out tooth but its recorded replacement begins with `the spot`; the current
  translation has an extra `Me,` prefixed to that correction.
- visual_evidence: NONE
- diagnosis: The meaning is recoverable, but the dialogue is ungrammatical and
  reads like an incomplete merge between draft and accuracy correction.
- fix_direction: Minimally remove `Me, `, yielding `「The spot where a certain
  someone punched me years ago is aching again.」`; retain the vague
  `a certain someone` and body-location meaning.
- systemic: false
- status: closed by the route-C repair and independent QC

## Continuous-route checks

- **Hallucination/omission:** No additional unsupported motive, action,
  relationship, object, or causal bridge survived source verification beyond
  C-RT-003 and C-RT-005. The prophecy at C0600:1847-1852 remains framed as a
  prediction, not a confirmed event.
- **Voice/character:** Leo's quick self-deprecation, Kinu's competitive direct
  affection, Subaru's relaxed capability, Otome's clipped authority, Erika's
  polished dominance, Yoshimi's outwardly gentle register, Nagomi's cold
  politeness, and Shinichi's comic bravado remain distinguishable. The direct-
  nickname drift in C-RT-006 and the malformed Shinichi line in C-RT-007 are
  the surviving voice defects.
- **Agency/relationships:** The test-of-courage kiss, Kinu's injury, the sports
  festival, Subaru's confession, Leo's withdrawal, Kinu's silent-treatment
  counterplan, Subaru's deliberate villain role, the mutual confession, and
  Subaru's transfer keep their source agents and causal order.
- **Reveal timing:** Subaru's crush remains unidentified until the later Kinu
  reveal except for C-RT-003's premature gender. His transfer decision follows
  the failed love triangle rather than preceding it.
- **Branch convergence:** The C0400_10/C0400_20 branches converge cleanly at
  C0400_30. The three C0600_10/20/30 kiss alternatives retain their distinct
  triggers and converge without importing sibling-branch agency into C0600_40.
  The C0780_10/20 bag-carrying alternatives remain distinct and both converge
  into C0790.
- **Scene/exclusion boundaries:** All sparse gaps remain opaque. The route does
  not invent transitions across the C0300, C0450, C0500, C0550, C0600_40,
  C0650, C0700, C0740, C0790, C0810, C0820, C0860, or C0900 exclusions.
- **Ending/coda:** Subaru's transfer, track progress, Olympic medal, return-home
  message, and Leo/Kinu seven-year coda remain chronologically coherent. The
  final `Tutorial 6 is now available.` control-facing line remains intact.

## Investigated non-findings

- `SC_C0600_40_C0650_00:600` uses `Shark Shinichi` because the source
  explicitly says `シャーク新一`; it does not establish `Shark` as his surname.
- `SC_C0810_00_C0820_00:59` says `broad daylight` while the earlier vignette is
  at night, but the source itself says `真昼間` after a separator and the scene
  QC identifies the later outside-viewpoint time jump. No translation
  chronology correction is justified.
- `SC_C0820_00_C0850_00:143`'s `hip-shaking` proverb distortion is source-
  authored (`腰振って、地固まる`) and the following silence is its punchline.
- C0650's fight injuries, C0740's one-month arm prognosis, and C0960's later
  fully healed state occur in the correct order.
- Quoted email, online-game chat, poster/score text, and mock scientific labels
  account for narration rows that legitimately contain quotation marks without
  Japanese dialogue wrappers.

## Fully excluded scenes

These eight scenes are exclusion/no-translation debt and remain artifact-free:

| Scene | Excluded indexes / rows |
| --- | ---: |
| `SC_C0705_00_C0710_00` | `1-511` / 511 |
| `SC_C0710_10_C0720_00` | `1-10` / 10 |
| `SC_C0710_20_C0720_00` | `1-14` / 14 |
| `SC_C0720_00_C0740_00` | `1-145` / 145 |
| `SC_C0800_00_C0810_00` | `1-157` / 157 |
| `SC_C0850_00_C0860_00` | `1-184` / 184 |
| `SC_C0910_00_C0920_00` | `1-253` / 253 |
| `SC_C0920_00_C0930_00` | `1-15` / 15 |
| **Total** | **1,289** |

## Story-image and runtime limitations

`docs/UI_STORY_IMAGE_LOCALIZATION_MANIFEST.md` inventories `titlechip.kg`,
`CGChip.kg`, and `EDChip.kg` but provides no exact C scene/index/variant mapping
to canonical story-image evidence. Therefore no C narrative image claim could
be corroborated or contradicted, and this report makes no runtime or visual
proof claim.

The manifest's static inventory is not live-engine evidence. No in-engine
textbox, backlog, nameplate, choice-screen, transition, sprite/CG, or localized
asset capture was available. Runtime wrapping, clipping, font fallback,
nameplate presentation, control timing, and actual story-image synchronization
remain unresolved even though static wrappers, exact indexes, and CP932 pass.

## Correction routing and pass condition

Route C does not pass the critical-readthrough gate while C-RT-001 through
C-RT-006 remain open. Route C-RT-001 and C-RT-002 through naming/terminology
accuracy plus targeted arbitration and corpus-wide confirmed-pattern searches;
C-RT-003 through reveal-aware accuracy and arbitration; C-RT-004 through
continuity accuracy; C-RT-005 through meaning/lore accuracy; C-RT-006 through
terminology-aware literary/accuracy arbitration; and C-RT-007 through targeted
literary cleanup. After corrections, rerun deterministic and narrative gates
and reread every affected passage. No broad rewrite is recommended.

## Exact translated-scene coverage

Every listed permitted index was read continuously. Counts sum to 6,589.

| Scene | Permitted indexes read | Count |
| --- | --- | ---: |
| `SC_C0100_00_K0900_00` | `1-96` | 96 |
| `SC_C0120_00_K0900_00` | `1-48,50-151` | 150 |
| `SC_C0140_00_K0900_00` | `1-73` | 73 |
| `SC_C0180_00_K0900_00` | `1-2,4-95,97-120,125-130` | 124 |
| `SC_C0200_00_C0300_00` | `1-42` | 42 |
| `SC_C0300_00_C0330_00` | `1-19,26-316,323-360` | 348 |
| `SC_C0330_00_C0350_00` | `1-27,36-195` | 187 |
| `SC_C0350_00_C0400_00` | `1-217` | 217 |
| `SC_C0400_10_C0400_30` | `1-5` | 5 |
| `SC_C0400_20_C0400_30` | `1-7` | 7 |
| `SC_C0400_30_C0450_00` | `1-350` | 350 |
| `SC_C0450_00_C0500_00` | `1-134,146-155,157-161,167-176,186-202,226-242,285-316,340-358` | 244 |
| `SC_C0500_00_C0550_00` | `1-159,163-267,270-276,280-289,291-377` | 368 |
| `SC_C0550_00_C0600_00` | `1-162,169-303,306-329,346-392` | 368 |
| `SC_C0600_10_C0600_40` | `1-11` | 11 |
| `SC_C0600_20_C0600_40` | `1-11` | 11 |
| `SC_C0600_30_C0600_40` | `1-12` | 12 |
| `SC_C0600_40_C0650_00` | `1-41,50-190,193-605,613-753,755-1227,1243-1247,1263-1292,1305-1343,1346-1413,1419-1509,1517-2310,2327-2367` | 2,277 |
| `SC_C0650_00_C0700_00` | `1-22,35-42,45-118,121-235,246-271` | 245 |
| `SC_C0700_00_C0705_00` | `1-26,30-58,61-73` | 68 |
| `SC_C0740_00_C0750_00` | `66-137,155-260` | 178 |
| `SC_C0750_00_C0760_00` | `1-153` | 153 |
| `SC_C0760_00_C0770_00` | `1-10` | 10 |
| `SC_C0770_00_C0780_00` | `1-100` | 100 |
| `SC_C0780_10_C0790_00` | `1-36` | 36 |
| `SC_C0780_20_C0790_00` | `1-30` | 30 |
| `SC_C0790_00_C0800_00` | `1-37` | 37 |
| `SC_C0810_00_C0820_00` | `8-71` | 64 |
| `SC_C0820_00_C0850_00` | `1-192,209-484` | 468 |
| `SC_C0860_00_C0900_00` | `14-76` | 63 |
| `SC_C0900_00_C0910_00` | `1-39` | 39 |
| `SC_C0930_00_C0940_00` | `1-10` | 10 |
| `SC_C0940_00_C0950_00` | `1-4` | 4 |
| `SC_C0950_00_C0960_00` | `1-30` | 30 |
| `SC_C0960_00_C0970_00` | `1-60` | 60 |
| `SC_C0970_00_C0990_00` | `1-29` | 29 |
| `SC_C0990_00_Z9999_99` | `1-75` | 75 |
| **Total** |  | **6,589** |

## Repair and closure addendum

All seven findings above were repaired in the route-C repair checkpoint. The
first independent accuracy pass then reviewed all 4,813 permitted rows in the
12 touched scenes and added six source-faithfulness corrections. The independent
literary pass reread the same scope, added ten localized prose improvements,
and escalated rather than smoothing over one upstream referent defect at
`SC_C0180_00_K0900_00:43`.

That scene was reopened through the accuracy lane. Its full 124 permitted rows
were checked again; indexes `13`, `25`, and `43` were corrected, including the
Leo/Tsushima self-referent error. A fresh literary reread accepted all three
corrections and cleared the block without further edits.

Targeted arbitration retained the established Heijo-kyo, BayStars, `little
miss`, and later wordplay decisions. No new accuracy-versus-literary conflict
survived. The corrected finding rows and their immediate continuity blocks were
reread after the final QC state: Samesuga and the chant, Ikajima, the withheld
crush gender, Mr. Nakajima, `The Dragon (Ryuumeikan)`, and Crab/Crabby address
locks are stable; the repaired sentence opening is grammatical. Exact joins,
exclusion gaps, hashes, engine IDs, speaker maps, wrappers, CP932 encoding,
word-wrap tests, and project validation pass. No route-C finding remains open.

This closure remains a static-script result. It does not claim runtime textbox,
backlog, sprite, CG, background, or in-engine rendering verification.
