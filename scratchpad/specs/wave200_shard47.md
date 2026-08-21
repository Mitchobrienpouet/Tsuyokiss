# Wave-200 shard 47 continuity preflight

Scenes and rows after fail-closed regeneration:

- `SC_M0605_00_M0606_00` - 51 permitted / 0 excluded (51 source rows)
- `SC_M0606_00_M0607_00` - 47 permitted / 0 excluded (47 source rows)
- `SC_M0607_00_M0608_00` - 16 permitted / 0 excluded (16 source rows)
- `SC_M0608_00_M0609_00` - 54 permitted / 12 excluded (66 source rows)

Total: 168 permitted rows; 12 excluded rows; 180 source rows. No target scene
is fully excluded.

## Safety / gates

- The supervisor-verified extraction reports 4,578 permitted rows and 159
  excluded rows globally.
- The active `state/content_exclusions_wave500_overlay.json` excludes only
  `SC_M0608_00_M0609_00:55-66` within this shard.
- `SC_M0605`, `SC_M0606`, and `SC_M0607` contain their complete consecutive
  source indexes. The regenerated `SC_M0608` projection contains exactly
  indexes `1-54` and ends before the excluded tail.
- Each `scratchpad/model_sources/` file is structure-identical to its
  payload in `scratchpad/model_shards/w200-47.json`; counts and source hashes
  agree.
- Excluded rows are outside model scope and are not translation debt. Do not
  inspect, infer, bridge, summarize, or create downstream entries for them.
- The 168 permitted rows contain no newly surfaced restricted range.
- `narrative_gates.json` declares no source mirrors or repeated-choice groups.

## Immediate continuity and omission boundaries

- The outing was arranged as Leo's clean do-over after the Ikajima trip and as
  repayment for Sunao's notebook-related favor. The day is the start of summer
  vacation, and Leo and Sunao have agreed to spend it together from the outset.
- Immediately before this shard, the permitted part of `M0604` places them at
  Oasis for lunch and has them discuss personality preferences. `M0604:33-40`
  are excluded, while its permitted index `41` is only a silent separator. Do
  not use `M0605` to reconstruct the omitted lunch exchange.
- `M0605:1` independently resumes after lunch at an arcade. It needs no causal
  bridge from the omitted material.
- `M0606` and `M0607` form one continuous karaoke sequence. `M0608` then moves
  to evening after the day's activities.
- `M0608` ends for model purposes at index `54`. Indexes `55-66` remain a
  complete omission boundary. Do not add a transition, response, action,
  relationship outcome, or following-scene setup after the permitted final
  line.

## Timeline and relationship reveal boundary

- All four scenes occur on the same summer-vacation outing: after lunch at the
  arcade, then karaoke, then an evening conversation.
- At the arcade, Shinichi calls Leo and Sunao a couple before realizing who the
  man is. This is Shinichi's outsider assumption, not authoritative
  relationship status.
- Sunao's romantic song lyrics are lyrics she is performing. They are not a
  direct confession and must not be rewritten as her own factual statement.
- The duet score and Leo's `相性` remark support a playful double reading about
  musical compatibility and personal chemistry. Neither score proves anything
  about their relationship.
- In `M0608`, Sunao first uses Leo's unpaid `debt` as an indirect excuse to ask
  for more days like this. Leo explicitly rejects continuing under that excuse
  and asks her to go on ordinary dates with him.
- Sunao praises the return of Leo's impulsive, forthright side, delays her
  answer to tease him, and accepts at index `49`. This establishes acceptance
  of the date request. It does not by itself establish a formal exclusive
  relationship, a girlfriend label, or any event beyond index `54`.

## Scene functions and reveal locks

### `SC_M0605_00_M0606_00`

- Leo introduces the venue with the mock-grand label `amusement park`, then
  immediately clarifies that it is an arcade. Do not turn it into a literal
  theme park.
- Leo recruits academically strong Sunao for an online four-choice quiz game.
  The history question divides their strengths: Sunao knows the academic and
  general-knowledge answer immediately, while Leo later handles entertainment
  trivia.
- Indexes `17-19` are on-screen quiz text, not narration spoken by either
  character. Preserve the four numbered options and Sunao's explicit choice of
  answer `4`; do not revise the game's answer from outside knowledge.
- Shinichi initially watches what he assumes is an anonymous couple, envies
  the man, and boasts that he could crush him at a fighting game. He recognizes
  Leo only at index `37`.
- After the separator, Shinichi plays alone until a challenger appears. Sunao's
  line at index `46` identifies Leo as the skilled challenger, but Leo does not
  knowingly target Shinichi and later treats the familiar voice as his
  imagination. Preserve this one-sided dramatic irony.
- Shinichi's loss is broad comic humiliation. His final realization is that he
  accidentally helped Leo look impressive in front of Sunao.

### `SC_M0606_00_M0607_00`

- The scene opens in mid-song. Sunao scores 92 and turns karaoke into another
  competition, despite Leo noting that they had been getting along peacefully
  before the scoring discussion.
- Indexes `1-2` are J-pop-style romantic lyrics with authored music-note
  markers. Preserve their lyric structure and emotional content without
  treating them as direct dialogue about Leo.
- Leo chooses the song that reliably earns his highest score. Its title at
  indexes `20`, `22`, and `23` must use one identical English rendering.
- Leo's song begins as sentimental comfort and then reveals that the woman has
  disappeared along with his bankbook and will to live. Preserve that exact
  escalation and land the repeated magician title after the theft punchline.
- Leo scores 95; Sunao answers with 96. Her gloating abruptly loses momentum
  when Leo watches her with an unusual look rather than acting defeated.
- Index `43` is a parenthetical nonverbal look inside Leo's dialogue wrapper,
  not a sentence he says aloud. Preserve the format and do not convert it into
  invented speech.
- Leo finds Sunao's unguarded excitement endearing at index `47`. Keep the
  warmth, but do not promote it into a confession.

### `SC_M0607_00_M0608_00`

- Leo immediately invites Sunao to sing a duet because he wants to sing with
  her. The direct eye contact flusters her, though she accepts under a mock
  reluctant excuse.
- They frame a perfect 100 as the happy ending, but the first duet scores only
  76. The low result is a compatibility joke, not a canonical judgment about
  the pair.
- Sunao insists they continue until they beat 96. The scene ends with both of
  them repeatedly singing together while the woman delivering drinks laughs at
  them.

### `SC_M0608_00_M0609_00`

- Evening arrives quickly because they have been absorbed in the day's games.
  Both say they had fun, and Leo asks whether the notebook debt is finally
  repaid.
- Sunao first agrees, then retracts it so that Leo will have to spend more time
  with her. Her index `14` clarification is still indirect: she wants to keep
  hanging out, without yet applying a relationship label.
- Leo understands the indirect appeal and rejects only the debt-based framing.
  `もうそんな関係でいたくない` at index `22` must not sound like a breakup
  or a rejection of Sunao herself.
- At index `24`, Leo clearly asks Sunao to date him normally, independent of the
  notebook. Preserve the assertive step without expanding it into a love
  confession or a demand for exclusivity.
- Sunao tests whether he has merely surrendered to the moment and whether he
  considered being refused. Leo says that he did, but wanted to speak more and
  would not treat one failure as a reason to give up.
- Sunao is pleased to see the old, forward-moving Leo again. Her `お帰り` at
  index `41` is metaphorical welcome-back language for that side of him, not a
  physical arrival.
- Sunao deliberately draws out her answer, then says `OK` at index `49`. Her
  subsequent lines through `54` explain that she teased him because his change
  had taken years and confirm how happy she is. Stop there.

## Voice and speaker locks

- `レオ` = `Leo`: brisk first-person narration, broad competitive confidence,
  pop-culture fluency, and self-aware romantic nerves. His evening directness
  is a deliberate character step, but he remains conversational rather than
  suddenly formal or poetic.
- `素奈緒` = `Sunao`; Leo normally calls her `Konoe`: academically capable,
  intensely competitive, proud of being a normal schoolgirl, and easily
  flustered when her enthusiasm or feelings show. Preserve her sharp retorts,
  crest/anger tic, triumphant gloating, and indirect-to-direct progression.
- `新一` = `Shinichi`; narration may call him `Fukahire`: envious, boastful,
  self-dramatizing comic loser. He is off to the side of Leo and Sunao's outing,
  not a participant in their conversation.
- Null-speaker rows remain narration or screen/UI text. Do not assign quiz
  prompts, game announcements, scores, or transitions to a character.

## Hard renderings and terminology

- `ゲーセン` (`M0605:2`) means `arcade`. Retain Leo's formal-to-casual joke;
  do not use `amusement park` as the venue name after his clarification.
- `享保の改革` (`M0605:17`) is the `Kyoho Reforms` in CP932-safe English.
  `株仲間` are merchant guilds, `目安箱` is the petition box, and `上知令` is
  the Agechi Order. Keep option numbering and line order exact.
- `SC_M0605:18` displays the historical title as `上公事方御定書`. The extra
  leading source character makes the precise title rendering contested. Do not
  silently repair the immutable Japanese or invent a confident reading.
- `乱入` in the fighting-game sequence means entering/challenging another
  player's match. `ラスボス` is `final boss`. `ハメ技` is a cheap trap,
  exploit, or lockdown tactic; it has no sexual meaning here.
- The on-screen `ヒア カムズ ア ニュー チャレンジャー!` (`M0605:41`)
  should be the familiar `Here comes a new challenger!` announcement.
- `フカヒレ` (`M0605:50`) remains the locked nickname `Fukahire`.
- `J-POP` (`M0606:6`) should remain recognizable as `J-pop`.
- `トサカ来る` (`M0606:12,34`) is Sunao's recurring crest-standing-on-end
  anger tic. Preserve the visible crest callback established in the recent
  route rather than flattening both occurrences into unrelated generic anger.
- `小粋なマジシャン` (`M0606:20,22-23`) needs one consistent comic song
  title. `The Dapper Magician` is a workable provisional rendering, not yet a
  glossary lock.
- Preserve `♪` music-note markers in sung lines. `通帳` in Leo's song is his
  bankbook/passbook, not a generic wallet or all of his money.
- `大団円` (`M0607:7`) is the happy/grand ending to their duet plan.
  `相性` (`M0607:11`) is compatibility/chemistry and should retain its musical
  and interpersonal double reading.
- `借り` throughout `M0608` is the notebook-related favor/debt, not a literal
  monetary loan. `乙女心` (`M0608:16`) is Sunao's roundabout girlish impulse to
  spend more time together; do not make it an explicit declaration.
- `甲斐性` (`M0608:28`) concerns backbone, initiative, or being man enough to
  speak plainly here, not money or earning power.
- `テンションに身を任せる` (`M0608:30`) means acting on the momentum/heat of
  the moment. Preserve Sunao's challenge rather than diagnosing loss of control.
- `自分殺してた` (`M0608:39`) means Leo had been suppressing his real nature.
  It must never be rendered as literal killing or self-harm.
- `気を持たせて` (`M0608:51`) means keeping Leo in suspense/teasing him over
  the answer. Avoid an erotic reading.

## Ruby, UI, and deterministic expectations

- No ruby/furigana control, choice token, or engine command appears in the 168
  permitted rows.
- The Japanese quotation marks around quiz prompts, game announcements, and
  numeric results occur in null-speaker UI/narration rows. Keep them distinct
  from spoken dialogue and use CP932-safe target punctuation.
- Preserve `「...」` around spoken lines and leave ordinary narration unquoted.
  Do not turn source composition spaces or line wrapping into engine codes.
- Translation JSONs must contain exactly `M0605:1-51`, `M0606:1-47`,
  `M0607:1-16`, and `M0608:1-54`. No key from `M0608:55-66` may appear.
- All target values must be strings and CP932 encodable. Smart quotes, Unicode
  ellipses, and em/en dashes are forbidden.

## Contested permitted ranges and later QC attention

- `SC_M0605_00_M0606_00:17-19`: preserve the quiz's exact option structure;
  index `18` has a source-form historical-title anomaly requiring focused
  accuracy review rather than silent normalization.
- `SC_M0605_00_M0606_00:32-50`: preserve when Shinichi recognizes Leo, when
  Leo remains unaware of Shinichi, and who actually wins the challenge.
- `SC_M0606_00_M0607_00:1-2,20,22-23`: lyric adaptation and the repeated song
  title require consistency review; meaning and comic reveal outrank rhyme.
- `SC_M0606_00_M0607_00:43-47`: retain the nonverbal parenthetical, Sunao's
  abrupt self-consciousness, and Leo's endearing assessment without invented
  dialogue or confession.
- `SC_M0607_00_M0608_00:9-13`: keep the score literal and the compatibility
  double reading playful, not prophetic.
- `SC_M0608_00_M0609_00:12-24,28-34,39-54`: maintain the progression from
  indirect request, through Leo's rejection of the debt framing, to his date
  request and Sunao's permitted acceptance. Do not infer any excluded tail.
