# Wave-500 shard 53 continuity preflight

Scenes and rows after fail-closed regeneration:

- `SC_M0664_00_M0665_00` - 56 permitted / 6 excluded (62 source rows;
  permitted `1-9,14-56,59-62`, excluded `10-13,57-58`)
- `SC_M0665_00_M0666_00` - 59 permitted / 11 excluded (70 source rows;
  permitted `1-15,23-39,44-70`, excluded `16-22,40-43`)
- `SC_M0666_00_M0670_00` - 28 permitted / 0 excluded (28 source rows;
  permitted `1-28`)
- `SC_M0670_00_M0671_00` - 15 permitted / 0 excluded (15 source rows;
  permitted `1-15`)

Total: 158 permitted rows; 17 excluded rows; 175 source rows. Translation debt
is exactly 158 rows.

## Safety / extraction / gates

- The four regenerated projections contain exactly the permitted index sets
  above. Every projected row has a nonempty engine ID and a 64-character source
  hash; no duplicate index is present.
- `SC_M0664_00_M0665_00:10-13,57-58` and
  `SC_M0665_00_M0666_00:16-22,40-43` are opaque policy gaps. They are zero
  translation debt and must remain absent from translation, both QC lenses,
  arbitration, contested notes, and build output.
- The preceding `SC_M0663_00_M0664_00` is fully excluded. This preflight did not
  inspect or reconstruct it, and the permitted opening of `M0664` must stand as
  a fresh boundary without any explanation of prior events.
- No newly restricted material appears in the 158 permitted rows. The brief
  romantic contact in `M0666` is mutual, non-explicit, self-contained, and does
  not depend on an excluded event.
- `narrative_gates.json` declares no source mirrors or repeated-choice groups.

## Immediate continuity and omission boundaries

- `M0664` opens during summer vacation at the home shared by Leo and Otome.
  Otome's work ended quickly, so she has brought Erika and Yoshimi home to
  visit. The exact time elapsed since the preceding opaque scene is unstated.
- Otome and the guests hear someone inside. Leo is surprised that Otome has
  returned, then the projection jumps from `9` to `14`. Do not state what Leo
  or Sunao did during `10-13` or use the gap to explain his surprise.
- At `14-18`, Leo asks Sunao to remain upstairs and out of sight because he did
  not tell Otome that Sunao was visiting. That displayed explanation is the
  only permitted motive for the concealment.
- The second `M0664` gap lies between Leo believing he has blocked access to his
  room at `56` and Otome calling Sunao by name at `59`. Do not supply a trick,
  sound, action, or discovery across `57-58`.
- `M0665` begins after Leo has explained that he and Sunao had arranged from the
  start to spend time at the house. Otome objects to his attempt to conceal the
  visit, not to the couple spending time together.
- Both gaps in `M0665` are hard cuts inside Erika and Sunao's escalating
  argument. Translate only the displayed before/after beats: do not invent what
  causes the resumption at `23` or which discarded competition idea precedes
  Erika asking Yoshimi to choose an event at `44`.
- The permitted argument resolves into an anonymous script contest for the
  Ryuumei Festival play, scheduled for September 9 during the second term.
  `M0666` has Sunao recount the decision to Leo; its precise location and time
  relative to `M0665` are unstated.
- `M0670:1` advances to the beginning of the second term. Erika's script is in
  progress, but no result, completion state, submission outcome, or contest
  winner has been revealed.
- `M0670:15` is a silent scene separator and the shard's hard stop. Do not
  foreshadow the next scene.

## Relationship, reveal, and agency locks

- Leo and Sunao remain an established couple. Leo calls her `Konoe`; she calls
  him `Tsushima`. Do not switch either character to first-name address.
- At `M0664:38-39`, Otome asks whether the date is already over and Leo gives a
  qualified affirmative while Sunao is still upstairs. Preserve the brevity
  and ambiguity; do not label the answer a lie or explain why Sunao remains.
- Yoshimi infers Sunao's presence from women's shoes that do not fit Otome.
  Erika then openly chooses teasing over tact. Neither character is given
  knowledge of any omitted event.
- At `M0665:13`, Erika calls Sunao a well-trained `girlfriend` while comparing
  her defense of Leo's room to a guard dog. The couple status is already known;
  keep the line playful and barbed rather than literal or dehumanizing.
- Sunao and Erika's conflict is a contest of pride. Yoshimi tries to calm them
  and then proposes a neutral script competition; she remains friendly and
  mediating rather than manipulative.
- The script contest is anonymous: author names are withheld and third parties
  judge the scripts themselves. Do not add a prize, penalty, formal school
  sponsorship, or result.
- Sunao initially proposes 100 randomly selected Ryuumeikan students as judges.
  Erika changes the number to 101 so a tie is impossible, and Sunao accepts.
  Preserve the proposal -> correction -> agreement order.
- `M0666:7-13` explains Sunao's jealousy through a hypothetical reversal: Leo
  would be jealous if she blushed when approached by a handsome boy, and she
  feels the same when Leo blushes at the Princess's teasing. Do not create a
  love triangle or claim that either hypothetical event actually occurred.
- Sunao's promise to make Leo completely hers is proud romantic possessiveness,
  not ownership, coercion, or a new relationship reveal.
- `M0666:15` means Sunao's speech left Leo no chance to get a word in. It does
  not mean an external deadline or that he refuses to speak.
- Leo says he can express his response through action, explicitly offers a
  kiss, and Sunao explicitly asks him to do it. Preserve Leo's offer and
  Sunao's assent before the brief kiss; do not extend or intensify the contact.
- Sunao says the kiss gave her strength more effectively than peanut butter,
  then claims her present romantic inspiration will make her romance writing
  unbeatable. This is confidence and a recurring food joke, not a guarantee of
  the contest result.

## Scene functions and local hazards

### `SC_M0664_00_M0665_00`

- Otome introduces the shared home; Erika's `commoner` remark is an imperious
  joke about the interior, while Yoshimi apologizes politely for intruding.
- Otome says the work finished quickly and invites the guests inside. Do not
  invent which task ended or a broader change to committee duties.
- Leo's concealment request at `14-18` is reluctant couple comedy. Sunao agrees
  only because he insists; do not add anger, fear, or an omitted motive.
- Otome catches Erika trying to enter another person's room and physically
  stops her. Erika's exaggerated complaints remain slapstick, not evidence of
  injury.
- Otome brought Erika and Yoshimi because they wanted to visit. `Princess` is
  Leo's established title for Erika; Yoshimi remains `Sato` / `Sato-san` in
  Leo's address according to natural English register.
- Yoshimi calls Erika `Ellie`, Sunao `Nao-chan`, and Otome
  `Kurogane-senpai`. Erika calls Otome `Otome-senpai`.
- Leo blocks the path to his room, and Otome respects how strongly he objects.
  The post-gap reveal at `59-61` is only that Sunao answers when Otome calls her
  name and Erika mocks how easily she gave herself away.

### `SC_M0665_00_M0666_00`

- Otome's opening lecture focuses on Leo's impulse to cover things up. Keep her
  concise disappointment; do not make her condemn the date or the relationship.
- Erika tries to search Leo's room while he is downstairs, and Sunao objects on
  the straightforward ground that it is someone else's home. Their argument is
  about privacy, entitlement, and pride.
- At `23-39`, preserve Erika's self-centered `I do it because I want to`
  reasoning, Sunao's rebuttal, and the escalation into a challenge. Do not
  bridge either adjacent exclusion gap.
- `闘志メラメラメラニン色素` at `33` is deliberately absurd sound-play
  linking blazing fighting spirit (`メラメラ`) to `melanin pigment`. Preserve
  the comic verbal derailment without asserting a literal change in Sunao's
  eyes, skin, or body.
- `鼻っ柱をへし折る` at `37` is a figurative promise to break Erika's pride
  or knock her down a peg, not a literal physical threat.
- Yoshimi's chosen event is a writing contest for the original play performed
  at the cultural festival. Sunao explains that accepting submitted scripts is
  a drama-club tradition and that she can enter through the same submission
  process.
- `人間性無しの純粋な脚本勝負` at `55` follows the rule that author names
  will not be disclosed. Render it as removing personalities, reputation, and
  personal bias from a pure comparison of the scripts; do not imply that the
  scripts lack human characters or humanity.
- `本職` at `56` means scriptwriting/drama is Sunao's specialty or home field.
  It does not establish that she is a paid professional playwright.
- Erika says she sometimes writes fiction and had already considered entering
  because scriptwriting sounded interesting. Do not claim prior theater or
  professional-writing experience.
- `竜鳴祭（文化祭）` is the `Ryuumei Festival`, the school's cultural
  festival. Preserve the displayed clarification naturally at its first use in
  this shard.
- Yoshimi's final relief that things ended peacefully is dry irony after the
  fierce verbal challenge, not proof that the rivalry has ended.

### `SC_M0666_00_M0670_00`

- Sunao reports the script-contest arrangement and insists that Erika is
  arrogant to challenge someone in her own specialty. Leo acknowledges Erika's
  broad competence without predicting a winner.
- `凄くジェラシー` is Leo's clipped, comic `very jealous` response to
  Sunao's hypothetical. Keep the deliberately simple wording.
- Sunao wants to defeat the Princess so Leo will stop blushing when Erika
  teases him. Her motive combines rivalry, jealousy, and affection; do not add
  hostility beyond her own competitive language.
- `しゃべる暇がナッシング` is deliberately goofy mixed diction meaning
  that Sunao has not let Leo get a word in. Preserve the joke without treating
  `Nasshingu` as a proper name or external reference.
- The kiss at `19-24` is a short mutual romantic beat. The description of
  Sunao's sweet lips is Leo's affectionate metaphor; do not specify a flavor or
  make the scene explicit.
- `恋愛モノ` at `27` is romance writing/a romance story in the script-contest
  context, not a claim about a separate published work.

### `SC_M0670_00_M0671_00`

- The scene marks the start of the second term. Erika's Korean greeting and
  Kinu's one-word `kimchi` response are a quick non sequitur; preserve the joke
  without adding nationality claims or a broader stereotype.
- Leo asks only how Erika's script is going. Her answer says she is enjoying
  the work, not that it is finished or good.
- `土永さん` is `Mr. Tsuchinaga`, Inori's talking parrot. He literally flies
  in as the substitute for morning homeroom because Inori is at home insisting
  she is still on summer vacation.
- Mr. Tsuchinaga's `我輩` voice is grandiose and old-fashioned. His address to
  the class as `chicks` and complaint about chirping students form an avian
  joke; retain both halves.
- `街角の紙芝居` is an old-fashioned street picture-card show (`kamishibai`),
  and `水飴` is starch-syrup candy. His advice is intentionally dated. Leo's
  reply lands the joke by saying he has never seen such a street show; do not
  modernize it into television, a theater, or ordinary candy distribution.

## Voice and speaker locks

- `レオ` = `Leo`: brisk, embarrassed, and quick with deadpan retorts. His
  admiration for Erika and affection for Sunao remain distinct and do not
  become a confession to Erika.
- `素奈緒` = `Sunao`: proud, protective of Leo's privacy, intensely
  competitive, jealous without coyness, and easily energized by affection. She
  calls Leo `Tsushima` and Erika `Princess` when `姫` is used.
- `乙女` = `Otome`: firm, practical, protective of household boundaries, and
  disappointed by dishonesty rather than scandalized by romance.
- `エリカ` = `Erika`: polished, imperious, invasive for comedy, and delighted
  by a worthy challenger. Her diction can pivot from childish teasing to
  grandiose competitive claims without becoming generic slang.
- `良美` = `Yoshimi`: soft, friendly, and mediating. She calls Erika `Ellie`,
  Sunao `Nao-chan`, and uses respectful senior address for Otome. Do not expose
  later-route undercurrents.
- `きぬ` = `Kinu`: only a one-word comic interjection in this shard. Keep the
  timing sharp.
- `土永さん` = `Mr. Tsuchinaga`: a talking parrot with pompous first-person
  diction and deliberately antiquated advice. Do not write him as a human
  substitute teacher.

## Hard renderings and terminology

- `姫` -> `Princess`; `エリー` -> `Ellie`; `よっぴー` -> `Yoppi`;
  `ナオちゃん` -> `Nao-chan`.
- `乙女センパイ` -> `Otome-senpai`; `鉄先輩` -> `Kurogane-senpai`.
- `彼女` at `M0665:13` -> `girlfriend`.
- `物色する` in the room sequence means snooping/searching through the room;
  keep the privacy violation without upgrading it to theft.
- `番犬` -> `guard dog` in Erika's teasing comparison.
- `闘志メラメラメラニン色素` requires functional English sound-play; keep
  both the blazing-fighting-spirit setup and the absurd `melanin pigment` turn.
- `竜鳴祭` -> `Ryuumei Festival`; `文化祭` -> `cultural festival` or natural
  `school festival` where the proper-name clarification is not required.
- `竜鳴館生徒` -> `Ryuumeikan students`.
- `脚本` -> `script`; `小説` -> `fiction` or `novels` according to syntax;
  `応募作品` -> submitted entry/script.
- `本職` at `M0665:56` -> `my specialty`, `my field`, or equivalent, not
  `professional playwright`.
- `凡夫` at `M0665:67` is Erika's polished insult meaning an ordinary mortal or
  mediocrity; do not turn it into a factual judgment by the narrator.
- `ジェラシー` -> `jealousy` / `jealous`; preserve Leo's clipped joke.
- `完全にアタシのもの` may be `make you all mine`, with playful romantic
  possession rather than coercive ownership.
- `しゃべる暇がナッシング` means `you did not give me a chance to get a
  word in`, with comic mixed diction.
- `ピーナッツバター` -> `peanut butter`, continuing Sunao's established
  fixation.
- `アニョハセヨー` may be rendered with a stable ASCII Korean greeting such
  as `Annyeonghaseyo`; `キムチ` -> `Kimchi`.
- `朝のHR` -> `morning homeroom`; `土永さん` -> `Mr. Tsuchinaga`.
- `ヒヨコども` -> `chicks`; `ピーピー鳥みたいに騒ぐ` should retain the
  noisy-chirping bird comparison.
- `紙芝居` -> `street picture-card show` or `kamishibai` with enough context to
  remain intelligible; `水飴` -> `starch-syrup candy`.

## Formatting and deterministic expectations

- The 158 permitted rows contain 144 dialogue rows and 14 narration rows.
  Preserve `「...」` around every dialogue row and leave narration unquoted.
- No ruby/furigana control, choice token, or engine command appears in the
  filtered projections. The visible `竜鳴祭（文化祭）` parenthetical is display
  text, not an engine instruction.
- A later authorized translation must contain exactly:
  - `M0664`: `1-9,14-56,59-62`
  - `M0665`: `1-15,23-39,44-70`
  - `M0666`: `1-28`
  - `M0670`: `1-15`
- No entry may be created for `M0664:10-13,57-58` or
  `M0665:16-22,40-43`. Sparse indexes must remain sparse rather than being
  renumbered.
- Use ASCII `...`, `--`, straight apostrophes, and ordinary spaces. Do not use
  smart quotes, Unicode ellipses, or em/en dashes. Every target value must be a
  string and CP932 encodable.
- This preflight authorizes no translation, QC, or arbitration artifact.

## Contested permitted ranges for later QC / arbitration

- `SC_M0664_00_M0665_00:1-9,14-19`: fresh-boundary handling, Leo's surprise,
  the first opaque gap, and the displayed concealment motive.
- `SC_M0664_00_M0665_00:20-39`: Otome/Erika household slapstick, honorifics,
  and Leo's qualified answer about whether the date ended.
- `SC_M0664_00_M0665_00:40-56,59-62`: shoe-based inference, Erika's teasing,
  the second opaque gap, and Sunao giving herself away only after Otome calls.
- `SC_M0665_00_M0666_00:1-15,23-39`: Otome's scolding target, privacy argument,
  guard-dog/girlfriend tease, gap-safe resumption, and the
  `メラメラメラニン色素` wordplay.
- `SC_M0665_00_M0666_00:44-70`: `Yoppi`, anonymized judging, Sunao's
  scriptwriting specialty, Ryuumei Festival naming, 100-to-101 judge correction,
  and September 9 schedule.
- `SC_M0666_00_M0670_00:7-20`: hypothetical jealousy, Princess referent,
  playful possession, `しゃべる暇がナッシング`, and kiss offer/assent
  agency.
- `SC_M0666_00_M0670_00:21-28`: restrained kiss cadence, sweet-lips metaphor,
  peanut-butter callback, and romance-writing confidence without result leakage.
- `SC_M0670_00_M0671_00:1-15`: second-term jump, Korean-greeting non sequitur,
  unresolved script progress, Mr. Tsuchinaga's parrot voice, and the dated
  picture-card-show/starch-syrup gag.
