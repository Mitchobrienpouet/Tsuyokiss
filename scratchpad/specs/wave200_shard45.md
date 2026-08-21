# Wave-200 shard 45 continuity preflight

Scenes and rows after fail-closed regeneration:
- `SC_M0580_00_M0581_00` - 13 permitted / 0 excluded (13 source rows)
- `SC_M0581_00_M0590_00` - 38 permitted / 0 excluded (38 source rows)
- `SC_M0590_00_M0600_00` - 63 permitted / 1 excluded (64 source rows)
- `SC_M0600_00_M0601_00` - 71 permitted / 0 excluded (71 source rows)

Total: 185 permitted rows; 1 excluded row; 186 source rows. No target scene
is fully excluded.

## Safety / extraction / gates

- The supervisor's regenerated extraction reports 4,590 permitted and 147
  excluded rows globally. This shard reconciles independently as 186 raw =
  185 permitted + 1 excluded.
- The active `state/content_exclusions_wave500_overlay.json` excludes only
  `SC_M0590_00_M0600_00:32` within this shard.
- `SC_M0590_00_M0600_00` therefore contains exactly indexes `1-31,33-64`.
  The other three scenes are contiguous across their complete source ranges.
- All four shard payloads match their generated `scratchpad/model_sources/`
  projections after normalized JSON comparison. Counts, indexes, speakers,
  kinds, Japanese text, and source hashes therefore agree.
- No duplicate projected index, malformed dialogue wrapper, ruby/furigana
  marker, choice text, or engine control token appears in the 185 permitted
  rows.
- The excluded index is outside model scope and is not translation debt. Do
  not inspect, reconstruct, summarize, bridge, or create a downstream entry
  for it. In particular, `M0590:31` must jump directly to `M0590:33`.
- `narrative_gates.json` declares no source mirrors or repeated-choice groups.
- No additional restricted content surfaced in the regenerated projections.
  The shard is clean for translation from these filtered sources.

## Immediate continuity and timeline

- The preceding permitted scene ends the one-night, two-day Ikajima stay. The
  public remains unaware, and Leo admits only to himself that the turbulent
  trip was enjoyable. The earlier exclusion gaps remain opaque.
- `M0580` returns Leo to ordinary home life. The public cover is that Principal
  Heizo personally trained him over the weekend; his tan is visible, but the
  island stay is still secret.
- `M0581` occurs as tests are returned. Leo's improved results, Sunao's ranking,
  and their newly easy conversation show the practical and interpersonal
  effects of the weekend without declaring a relationship.
- `M0590` is a humid night shortly afterward. Leo's friends discover only the
  permitted facts stated on screen, promise secrecy, and prompt his tentative
  recognition that he may like Sunao.
- `M0600` is the end of the first school term, immediately before summer
  vacation. Leo returns Sunao's notebook and asks to spend time together again
  under the stated rationale of starting fresh and repaying the notebook favor.
- The following permitted scene begins summer vacation. Otome calls the outing
  a date, but Leo himself remains unsure whether that label fits. Preserve that
  boundary here: this shard reaches an accepted invitation, not a confession,
  an official couple, or an agreed romantic date.

## Scene functions and reveal boundaries

### `SC_M0580_00_M0581_00`

- Leo's opening `シャバ` is comic prisoner/release slang for being back in the
  free, everyday world. It does not establish literal imprisonment or an
  arrest.
- Otome repeats the cover story that Heizo trained Leo over Saturday and Sunday.
  Index `3` explicitly marks this as what the outside world believes; do not
  convert it into objective narration or expose the island secret.
- Otome reads Leo's tan as a sign that he seems a little tougher. Leo and the
  parenthetical narration remain skeptical that anything beyond the tan has
  changed.
- The onigiri is Otome's homemade food and restores the feel of everyday life.
  `日常の味` is emotional/comic familiarity, not a literal flavor description.
- Otome says she will return to her family home occasionally during summer
  vacation. Do not imply she will be away for the entire break.
- Her good mood comes from Leo appearing slightly tougher. Keep her energetic,
  familial approval; the scene contains no suspicion that the cover is false.

### `SC_M0581_00_M0590_00`

- Leo scores above average and gets through every subject with decent results
  thanks to efficient studying. Kinu only just avoids a failing mark. Do not
  upgrade either result into an exact class rank.
- Leo pats Kinu's head with patronizing kindness, then presents an ad from the
  back of a boys' magazine as his supposed secret. Kinu credulously treats the
  advertised quick improvement as real. Leo's withheld `本当の事` remains
  unspecified; do not explain the hidden study arrangement beyond permitted
  context.
- When Leo and Sunao meet, ordinary conversation feels strange because the
  weekend was so unusual. Their ease is new but not yet romantic confirmation.
- Preserve the posted rankings exactly: Sunao is fifteenth, Erika first, Yohei
  second, and Yoshimi fifth. Sunao aims first for the top ten and eventually
  wants to do something about the number-one spot.
- Leo's narration identifies Sunao's continuing rivalry with `Princess`
  (Erika). Sunao does not explicitly name Erika in her own line, so do not make
  her wording more direct than the source.
- Subaru and Kinu observe the conversation from outside it. Subaru trusts Leo
  to talk when the time is right; Kinu instead plans an interrogation for the
  next day. Their suspicion must not become advance knowledge of the island.

### `SC_M0590_00_M0600_00`

- Sunao's brief phone call checks that the deserted-island incident is still
  secret. Leo reassures her, then finds Kinu, Shinichi, and Subaru emerging from
  his closet after eavesdropping. Their cramped hiding and Shinichi/Subaru
  contact are purely physical-comedy complaints.
- At indexes `18-25`, Shinichi guesses that Leo stayed on an island alone with
  a girl and leaps to a stock adventure fantasy. Leo accidentally gives himself
  away. The snakebite/blood-sucking question is another conjectured trope; it
  is not a fact about the weekend.
- Leo requires a serious promise of confidentiality at indexes `26-31` because
  he does not want stray rumors. Preserve the emphasis in `本当の“約束”` without
  inventing a prior promise or explaining why the typography is emphasized.
- Index `32` is excluded. Index `31` ends with Leo beginning his account;
  index `33` resumes only with Kinu's displayed general reaction to a one-night,
  two-day island stay. Do not supply any missing narration, speech, disclosed
  detail, reaction, or causal bridge across the gap.
- Subaru asks whether Leo will date Sunao. Leo says he does not know yet. Kinu's
  movie-based claim is only a generalization that couples formed under unusual
  circumstances do not last; do not state that Leo and Sunao already became a
  couple, and do not name an unstated film.
- Leo's irritation triggers a tentative internal question: he may have come to
  like Sunao. `やっぱり` suggests a returning suspicion, while `かな` keeps it
  uncertain. His decision is to try a fresh start and spend time with her again,
  not to confess or formalize a relationship.
- The permanent-marker threat is interrupted by Subaru. Shinichi then demands
  that Subaru introduce him to a girl, and Kinu/Shinichi trade matching
  fish-versus-crustacean taxonomy insults.
- When Otome enters, Kinu and Shinichi protect the secret with a false claim
  that they are correcting Leo's desire to make easy money. Otome sincerely
  joins the joint-lock punishment. Index `59` confirms the friends kept their
  confidentiality promise; it must not be used to reconstruct the omitted row.

### `SC_M0600_00_M0601_00`

- The first term has ended. Leo waits to return Sunao's notebook and propose a
  fresh start; weak reception at Ryuumeikan, not a broken phone or deliberate
  avoidance, prevents him from reaching her.
- Tonfa calls Leo to karaoke because the group has assembled. He asks them to
  go ahead and heads to Class 2-A himself.
- Indexes `13-18` are a timed wrong-name gag. Yohei deliberately calls Tsushima
  `Tsumura`; Leo answers with `Murano` instead of `Murata`. Yohei initially
  assumes it is a clever retaliation, then discovers Leo was sincerely wrong.
  Preserve all three surnames and do not correct or homogenize them.
- Yohei says Sunao's looks are excellent but her preachy, sometimes shrill
  scolding cancels out her appeal among the Class 2-A boys. Leo feels quietly
  relieved and then defends her as interesting. Keep the relief implicit; do
  not label it jealousy in narration.
- Leo counters by asking about Yohei and Nishizaki. Yohei claims she is merely
  attached to him one-sidedly, yet admits he cannot leave her alone and will
  help with her summer photography trip to Minami-Boso. Do not declare them a
  couple or reverse who has become attached to whom.
- `兄貴気質` points to Yohei's protective big-brother nature and cues the
  recurring joke about his twelve younger sisters. Yohei takes Leo's comment as
  a request for an introduction; Leo rejects that as the conversational
  equivalent of scoring an own goal.
- Noriko vocalizes her usual `くー` while imitating a teasing whistle. Preserve
  both the `Kuu` mannerism and the parenthetical intended whistle rather than
  replacing her with ordinary fluent speech.
- Leo returns the wrapped notebook, struggles through his embarrassment, and
  asks whether Sunao has time during summer vacation. `踏み込む` is his resolve
  to take an interpersonal step; it is not physical movement toward her.
- `仕切り直し` directly continues Leo's thought at `M0590:44`: he wants a clean
  do-over in ordinary circumstances. The request is to hang out together from
  the beginning as a pair, not an explicit dating proposal.
- Leo says their last outing was fun but was thrown into chaos by the Principal.
  Sunao recalls that the original premise was for Leo to thank/repay her for the
  notebook. Her statement that the deserted island was `無意味` is restricted
  by `そういう意味では`: it did not fulfill that stated premise. It does not
  erase the fun they had or condemn the entire experience.
- Sunao accepts with lightly feigned reluctance. They will settle details by
  phone. Leo's `大義名分` is the convenient legitimate rationale that makes the
  invitation easier, not a noble cause or proof that his feelings are false.

## Voice and speaker locks

- `レオ` -> `Leo`: casual, quick, self-deprecating narration; easy banter with
  old friends; romantic thoughts stay guarded and tentative.
- `乙女` -> `Otome`: concise, commanding, upbeat, and familial. Her forceful
  encouragement and joint-lock enthusiasm are matter-of-fact, not malicious.
- `素奈緒` -> `Sunao`; Leo normally addresses her as `Konoe`: capable, blunt,
  competitive, and increasingly comfortable with Leo. Her agreement retains a
  light defensive/faux-reluctant edge.
- `きぬ` -> `Kinu`; narration/direct nickname `カニ` -> `Crab`: loud, vulgar,
  impulsive, suspicious, and fast with comic insults.
- `スバル` -> `Subaru`: relaxed, perceptive, and protective without becoming
  solemn. He trusts Leo's timing and acts as the group's restraint.
- `新一` -> `Shinichi`: excitable, self-serving, and committed to pulp-romance
  fantasies. Do not substitute `Fukahire` where the source does not use it.
- `洋平` -> `Yohei`; surname `村田` -> `Murata`: pompous, pedantic, and quick
  to spar verbally, but transparently protective toward Noriko.
- `豆花` -> `Tonfa`: preserve her lightly clipped, non-native cadence without
  caricatured spelling or invented nationality markers.
- `紀子` -> `Noriko`: preserve her recurring `Kuu!` vocalization and translate
  parenthetical intended meanings. Her teasing whistle is playful classmate
  heckling.
- Names appearing on the ranking list remain `Erika Kiriya`, `Yohei Murata`,
  `Yoshimi Sato`, and `Sunao Konoe`; `姫` remains `Princess` as Erika's title.
- Null-speaker rows remain narration and unquoted. Never assign a speaker to a
  transition or internal thought.

## Terminology and hard-rendering locks

| Japanese | Locked handling |
|---|---|
| `館長` | `Principal` in these scenes; it refers to Heizo. |
| `竜鳴館` | `Ryuumeikan Academy`. |
| `無人島` | `deserted island`; `無人島１泊２日` is a one-night, two-day island stay. |
| `シャバ` | comic `free world` / `air of freedom`, not literal criminal history. |
| `赤点ギリギリ` | barely avoiding a failing mark, not receiving a confirmed fail. |
| `少年誌の裏の広告` | an ad on the back of a boys' magazine; retain its dubious quick-results flavor. |
| `姫` | `Princess`, referring to Erika. |
| `魚類` / `甲殻類` | matching `fish` / `crustacean` taxonomy insults. |
| `油性ペン` | `permanent marker`, not merely any pen. |
| `関節技` | `joint lock` / `joint-lock move`, not a generic beating. |
| `南房総` | `Minami-Boso`. |
| `津村` / `村野` / `村田` | `Tsumura` / `Murano` / `Murata`; preserve the deliberate/error reveal order. |
| `１２人の妹` | Yohei's recurring twelve younger sisters. |
| `仕切り直し` | `fresh start` / `do-over`; preserve the callback between `M0590:44` and `M0600:4,60-61`. |
| `大義名分` | a convenient legitimate reason or pretext for inviting Sunao, not a grand moral cause. |

## Ambiguity and agency locks

- `M0580:4,12`: Otome says Leo *seems* tougher; the narration allows that he
  may only be tanned. Do not confirm physical growth.
- `M0581:9-13`: Leo's magazine ad is a cover, and the exact withheld truth is
  not restated here. Do not add a specific tutoring claim.
- `M0581:31-32`: Sunao wants eventually to challenge the number-one position;
  Leo supplies the Erika/Princess rivalry inference in narration.
- `M0590:18-25`: distinguish Shinichi's guesses from established facts and
  Leo's accidental self-betrayal from a deliberate admission.
- `M0590:29`: preserve the marked `real "promise"` emphasis without explaining
  it from excluded or unstated material.
- `M0590:31,33`: preserve the hard discontinuity around excluded index `32`.
  Index `33` stands on its own and authorizes no reconstruction of the account.
- `M0590:36-45`: dating is posed as a question, Leo's attraction remains
  tentative, and his next step is another outing rather than a confession.
- `M0600:24`: Leo merely feels relieved. Any jealousy reading remains subtext.
- `M0600:30,35-36`: Nishizaki is the one attached to Yohei; his protective
  concern then complicates his claim without reversing its grammar.
- `M0600:38-39`: Yohei interprets the big-brother comment as Leo soliciting an
  introduction to one of his sisters; Leo's `own goal` rejects that setup.
- `M0600:64`: Sunao says the original arrangement was for Leo to repay/thank
  her for the notebook. Keep Leo as the party who owes the favor.
- `M0600:65`: `in that sense` narrows `meaningless` to the notebook-repayment
  purpose; it is not an emotional rejection of the island stay.
- `M0600:68-71`: Sunao agrees to the outing, but neither party names it a date
  or openly confirms romantic intent.

## Engine / deterministic expectations

- Preserve `「...」` around all dialogue and leave narration unquoted.
- Translation JSONs must contain exactly `M0580:1-13`, `M0581:1-38`,
  `M0590:1-31,33-64`, and `M0600:1-71`.
- `SC_M0590_00_M0600_00:32` must remain absent from translation and all later
  QC/arbitration artifacts.
- Preserve all source indexes as strings, all target values as strings, and all
  source speaker mappings. Do not add engine codes or treat source visual line
  breaks/spaces as control syntax.
- All target text must be CP932 encodable. Use ASCII `...`, `--`, straight
  apostrophes, and ordinary spaces; forbid smart quotes, Unicode ellipses, and
  em/en dashes.

## Contested permitted ranges for later QC / arbitration

- `SC_M0580_00_M0581_00:1,3-4,9-12`: comic freedom slang, public-cover framing,
  apparent-versus-actual toughness, everyday-life flavor, and Otome's partial
  summer absence.
- `SC_M0581_00_M0590_00:9-13,17-18,21-32,33-38`: the false ad and unspecified
  withheld truth; post-weekend ease; exact ranking/rivalry agency; observers'
  suspicion without premature knowledge.
- `SC_M0590_00_M0600_00:18-31,33-45,53-64`: conjecture versus fact, accidental
  disclosure, confidentiality emphasis, the hard exclusion gap, tentative
  attraction/fresh-start logic, taxonomy insults, and the friends' safe cover.
- `SC_M0600_00_M0601_00:8,13-18,19-27,28-40,45-47,53-71`: Tonfa's cadence,
  wrong-name timing, Leo's implicit relief, Yohei/Noriko agency and sister gag,
  Noriko's vocalized whistle, and the invitation's deliberately non-official
  romantic status.
