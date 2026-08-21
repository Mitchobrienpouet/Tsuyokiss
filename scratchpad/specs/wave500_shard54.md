# Wave-500 shard 54 continuity preflight

Scenes and rows after fail-closed regeneration:

- `SC_M0671_00_M0680_00` - 30 permitted / 31 excluded (61 source indexes;
  permitted `1-22,54-61`, excluded `23-53`)
- `SC_M0680_00_M0681_00` - 77 permitted / 0 excluded (permitted `1-77`)
- `SC_M0681_00_M0682_00` - 32 permitted / 0 excluded (permitted `1-32`)

Total: 139 permitted rows; 31 excluded rows; 170 source indexes. Translation
debt is exactly 139 rows.

## Safety and deterministic gates

- The only authorized source text for this preflight is the three regenerated
  files in `scratchpad/model_sources/`. No raw source was consulted.
- `SC_M0671_00_M0680_00` contains the exact sparse key set `1-22,54-61`.
  The omission at `23-53` is intentional, contiguous, and zero translation
  debt. Do not seek, reconstruct, summarize, bridge, or foreshadow it.
- `SC_M0680_00_M0681_00` and `SC_M0681_00_M0682_00` are consecutive at
  `1-77` and `1-32`. All three projections have unique indexes, nonempty
  engine IDs, and nonempty source hashes.
- No newly surfaced restricted material appears in the permitted projections.
  The active exclusion overlay already owns `SC_M0671_00_M0680_00:23-53`.
- `narrative_gates.json` declares no source mirrors and no repeated-choice
  groups.
- Hard boundary: a later translation may emit only the 139 permitted keys. It
  must preserve the M0671 gap exactly and stop at `SC_M0681_00_M0682_00:32`.

## Immediate continuity and omission boundaries

- `M0671:1-22` takes place on the school rooftop on opening-ceremony day. Leo
  and Sunao are already dating, and their relationship has become known among
  classmates and friends. Do not stage a confession or treat the relationship
  as newly beginning here.
- Sunao says her friends noticed her feelings from how absorbed she becomes
  when talking about Leo. Index `14` introduces a reenacted example of that
  earlier conversation; indexes `15-18` remain Sunao's quoted retelling rather
  than a live exchange with the absent friends.
- Stop cleanly after `M0671:22`, then resume at `54` without connective text.
  Index `54` is already in progress with `ま`; retain its mild resumption but
  do not explain how the script topic arose during the opaque interval.
- `M0671:54-61` establishes only that Sunao is working extremely hard on her
  script and refuses to underestimate her opponent. Leo contrasts her strain
  with the Princess enjoying her own work and senses something troubling in
  the difference. Do not name a predicted winner, cause, or consequence.
- `M0680` moves to an early-September Friday while the late-summer heat
  continues. It is the day of the script contest. Do not invent an exact date
  or elapsed interval from the opening ceremony.
- `M0680` ends after all 101 votes have been collected and the group heads to
  the student council room to count them. Sunao declares that earnest effort
  will beat the Princess's fun-first approach; Leo alone has a bad feeling.
  No result or explanation is revealed there.
- `M0681` covers only the partial count. The tally begins close, then shifts
  strongly toward ballot `B`. The scene stops on a silent beat at index `32`
  before a final total, winner, or aftermath appears. Do not import any later
  result.

## Scene functions and reveal locks

### `SC_M0671_00_M0680_00` (permitted `1-22,54-61` only)

- The empty rooftop gives Leo and Sunao privacy to discuss who knows they are
  dating. Leo's class learned without a formal announcement; Sunao explicitly
  told friends, who had already inferred it.
- At index `10`, the friends' observation concerns a perceived mature quality
  in how Sunao's makeup looks or sits. Do not state a physical cause, a sexual
  history, or a transformation more specific than the source.
- Sunao warns Leo because she herself gets carried away talking about him. Her
  reenacted monologue complains that he is hopeless and says she has to cover
  for or look after him, while transparently revealing her fondness.
- `ごちそうさま` at index `19` is a conventional response to excessive
  romantic gushing: the listeners have had their fill. It is not a literal
  meal, invitation, or gratitude for food.
- The permitted post-gap passage is a separate script-contest beat. Sunao's
  determination is sincere and competitive; Leo's warning at `56` is concern
  that she is too tense, not a request to concede or work less carefully.
- Indexes `59-61` contrast Sunao working desperately with the Princess having
  fun. Leo's unease is deliberately unspecific and must remain internal.

### `SC_M0680_00_M0681_00`

- Yoshimi has the two scripts printed for the contest. The source mentions 120
  copies without safely requiring a per-author split; keep the number and avoid
  inventing a different print run. Otome volunteers to use her martial-arts
  strength to carry the finished copies to the school gate.
- Yoshimi owns the original proposal for the contest and has secured teacher
  permission. Inori's assistance is framed comically: she claims to be free,
  then asks Heizo not to dock her pay for lateness. Do not turn this into a
  bonus request, formal disciplinary hearing, or proof that teachers have no
  work.
- Erika is certain she will win. Leo's observation that the loser may have her
  pride crushed is comic anticipation, not a revealed outcome.
- Index `18` opens a school-gate vignette with Tonfa, Mana, Akao, Handsome Ono,
  Inori, and Heizo. Index `34` then returns to Leo's group moving to the gate;
  preserve both transitions instead of flattening them into one continuous
  group conversation.
- The voters must compare two anonymous scripts and choose the one more
  suitable for a Ryuumei Festival production. Inori withholds authorship and
  permits only the labels `A` and `B`. Do not let ordinary voters know that
  `A` is Sunao and `B` is the Princess.
- The target is exactly 101 votes. Leo declines to vote but accepts a spare
  copy so he can read; the source gives no motive for his abstention, so do not
  add neutrality, eligibility, or conflict-of-interest rules.
- Mr. Tsuchinaga peers over Leo's shoulder, rushes his page turns, and mocks
  his manga-heavy reading habits. His praise of Sunao's script is sincere but
  comic because it comes from the parrot. Sunao's mixed reaction must retain
  both halves.
- Leo finds Sunao's tightly constructed romance genuinely beautiful and is
  slightly moved. The permitted text supplies no plot synopsis; do not invent
  characters, events, or an ending for either script.
- The Princess's script is a slapstick farce. Sunao fairly recognizes Erika's
  talent but still declares that her own script's beauty will win. Yoshimi and
  Erika also acknowledge Sunao's quality; Erika nevertheless keeps her
  confidence.
- At `71-73`, all 101 ballots are in and the group relocates to the student
  council room for counting. Sunao's `74` is a figurative promise to take the
  Princess down a peg, not physical violence.
- Indexes `75-77` are the shard's foreshadowing hinge: Sunao equates desperate
  effort with likely victory over work written in a spirit of fun, while Leo
  feels only an unnamed bad premonition. Preserve the mismatch and reveal
  nothing further.

### `SC_M0681_00_M0682_00`

- Inori assigns Nagomi to read the ballots. Kinu says the first-year must do it
  because she is youngest; Nagomi's tongue-click and terse compliance preserve
  her cold resistance without escalating into a serious dispute.
- Leo states the mapping for the people in the room: `A` is Konoe and `B` is
  the Princess. Keep every later ballot label and score tied to that mapping.
- Yoshimi records the count on a whiteboard beneath the authors' names. The
  source's `正` refers to the Japanese five-stroke tally convention; translate
  its counting function, not as prose that Yoshimi repeatedly writes a person's
  name or awards multiple votes at once.
- The displayed intermediate scores are exact: `13-17`, then `25-26`, then
  `29-40`, always in `A-B` order. Sunao is behind at each stated total even
  when she predicts she will catch up or pull ahead.
- Indexes `21`, `26`, and `28` give ballot-label sequences rather than final
  totals. Preserve their order and repeated `B`s; do not silently recompute or
  replace them with summarized narration.
- The sudden skew toward `B` alarms Sunao and concerns Leo, but the permitted
  source does not establish fraud, ballot tampering, a counting error, or a
  causal explanation. Erika's confidence is not itself proof of one.
- Index `32` is only a pause. Stop there with the contest unresolved.

## Voice and speaker locks

- `レオ` = `Leo`: casual, observant first-person narration. His unease at the
  effort-versus-fun contrast stays understated; do not make him omniscient.
- `素奈緒` = `Sunao`; Leo calls her `Konoe`: proud, competitive, blunt, and
  easily embarrassed. She can brag and then visibly unravel during the count
  without becoming cruel or incoherent.
- `エリカ` = `Erika`; Leo and the circle use the locked title `Princess` for
  `姫` / `お姫様`: polished, imperious, playful, and serenely confident.
- `良美` = `Yoshimi`: warm, practical organizer and scorekeeper. Preserve her
  familiar `Nao-chan` for `ナオちゃん`, `Ellie` for `エリー`, and Erika's
  address `Yoppi` for `よっぴー`. Do not expose any unstated undercurrent.
- `乙女` = `Otome`: concise and physically capable; her transport offer is
  matter-of-fact rather than boastful.
- `祈` = `Inori`: airy, composed adult-teacher delivery with elongated comic
  endings. Her grand claim of loving students and plea about docked pay are a
  linked deadpan gag, not childish speech.
- `平蔵` = `Heizo`: measured headmaster authority. His `考えておきましょう`
  is noncommittal, not approval.
- `豆花` = `Tonfa`: cheerful, lightly non-native syntax without caricatured
  misspelling. `楊さん` at `M0680:24` refers to Tonfa by surname, not a new
  person; `Miss Yang` is a defensible teacher-to-student address.
- `真名` = `Mana`: casual Kansai rhythm rendered with light colloquial English,
  not phonetic dialect.
- `赤王` = `Akao` in established M-route usage: rough, feral energy with the
  recurring `Kishaa!` cry.
- `ハンサム大野` = `Handsome Ono`: self-admiring and grandiose; preserve the
  repeated handsome-persona joke.
- `土永さん` = `Mr. Tsuchinaga`: gruff, pompous talking parrot. `我輩` is his
  grandiose first person, not a name or a second speaker.
- `なごみ` = `Nagomi`: cold, clipped deadpan. Inori's `椰子さん` is the same
  character addressed by surname; Nagomi's `近衛先輩` should retain the
  hierarchy as `Konoe-senpai`.
- `きぬ` = `Kinu`: loud, shameless comic senior. `一年坊` is a dismissive
  first-year kid/brat jab, not a literal monk or a claim about gender.
- Null-speaker rows are Leo's narration or scene transitions. The permitted
  payload contains 114 dialogue rows and 25 narration rows; preserve all roles
  and wrappers exactly.

## Hard renderings and terminology

- `交際` in `M0671:5` is Leo and Sunao's dating relationship. `C組` is
  `Class 2-C` in current school context unless the target line can naturally
  retain just `Class C` without losing the established year.
- `化粧のノリ` at `M0671:10` concerns how makeup applies/looks. Keep the
  friends' subjective inference and avoid turning it into a medical or bodily
  claim.
- `フォローしてあげる` at `M0671:15` means covering for, supporting, or
  looking after Leo; it is not following him online.
- `脚本` -> `script`; `脚本勝負` / `脚本対決` -> `script contest` or one
  consistent equivalent. The scripts are prospective stage productions, not
  finished films or published novels.
- `拳法部` -> `martial-arts club`; `校門` -> `school gate`.
- `竜鳴祭` -> `Ryuumei Festival`. The visible parenthetical `文化祭` at
  `M0680:25` identifies it as the cultural festival; preserve that information
  without changing the locked event name. `出し物` here is the festival
  production/performance selected from the scripts.
- `A` is Sunao/Konoe and `B` is Erika/the Princess only after the cast states
  the mapping. Keep ASCII capital letters and exact vote order.
- `反面教師` at `M0680:13` is a cautionary/bad example, not a substitute
  teacher. `天変地異` at `19` is Tonfa's comic natural-disaster hyperbole.
- `格調高い` at `M0680:53` praises the script as elevated, dignified, or
  refined. `ドタバタ劇` at `64` is a slapstick farce, not a literal fight.
- `鼻っ柱を折る` at `M0680:74` is figurative: take the Princess down a peg.
  `必死でやった` at `75` emphasizes Sunao's all-out effort; do not add a
  claim that effort objectively determines artistic merit.
- `正` at `M0681:11` is a five-stroke tally mark. Preserve the functional count
  and the whiteboard location.

## Ambiguity and later-QC attention

- `M0671:10`: keep the makeup observation subjective and causally vague.
- `M0671:14-20`: preserve the nested reenactment, the absent friends' reaction,
  the nonliteral `ごちそうさま`, and Sunao's embarrassed self-awareness.
- `M0671:22 -> 54`: hard discontinuity. Translation must not add a transition,
  referent, recap, or explanation across the excluded range.
- `M0671:54-61`: retain Sunao's respect for her opponent, Leo's concern about
  overstrain, the desperate-versus-fun contrast, and the unspecified unease.
- `M0680:3-6`: keep both script ownership and the 120-copy count without
  inventing a per-script allocation; retain Otome's practical transport offer.
- `M0680:24-32`: preserve Tonfa as Inori's addressee, anonymous `A/B` voting,
  Heizo's noncommittal response, and the lateness/pay joke.
- `M0680:38-60`: Leo does not vote; Mr. Tsuchinaga reads over his shoulder;
  both the parrot's praise and Leo's sincere reaction concern Sunao's script.
- `M0680:62-77`: distinguish the Princess's farce from Sunao's romance, keep
  every speaker's confidence correctly attributed, and do not leak the vote.
- `M0681:1-18`: preserve seniority jokes, the `A/B` mapping, tally mechanics,
  and exact intermediate scores.
- `M0681:19-32`: retain the accelerating `B` streak and emotional pressure
  without implying misconduct or supplying the final outcome.

## Formatting and downstream deterministic expectations

- No projected row contains a separate ruby, choice, or engine-control field.
  `M0680:25` contains a visible parenthetical festival gloss in body text; it
  is semantic content, not permission to insert a new engine code.
- Preserve `「...」` around every spoken line and keep narration unquoted.
  Normalize source `――` to project-safe `--`, Japanese ellipsis runs to ASCII
  `...`, and full-width digits/letters to ordinary English forms where natural.
- Use straight apostrophes, ASCII punctuation, and ordinary spaces. Do not use
  smart quotes, Unicode ellipses, or em/en dashes. Every later target value must
  be a nonempty string and CP932 encodable.
- A later M0671 translation JSON must contain exactly
  `1-22,54-61`; keys `23-53` must remain absent. M0680 must contain exactly
  `1-77`, and M0681 exactly `1-32`. No line may be renumbered to close the gap.
- This preflight authorizes no translation, QC, arbitration, Git, config, or
  state action. Translation must begin only under a separate assignment.
