# Wave-200 shard 51 continuity preflight

Scenes and rows after fail-closed regeneration:

- `SC_M0630_10_M0640_00` - 0 permitted / 163 excluded (163 source rows;
  fully excluded)
- `SC_M0630_20_M0640_00` - 5 permitted / 0 excluded (5 source rows)
- `SC_M0640_00_M0650_00` - 46 permitted / 0 excluded (46 source rows)
- `SC_M0650_00_M0660_00` - 41 permitted / 24 excluded (65 source rows)

Total: 92 permitted rows; 187 excluded rows; 279 source rows. Translation debt
is exactly 92 rows.

## Safety / gates

- The supervisor-verified extraction reports 3,913 permitted rows and 824
  excluded rows globally, with eight fully excluded scenes.
- `SC_M0630_10_M0640_00:1-163` is fully excluded and zero translation debt.
  It was not inspected or reconstructed during this regenerated preflight.
- `SC_M0650_00_M0660_00:42-65` is an excluded tail. The filtered projection
  ends exactly at index `41`; no omitted line may be inferred, summarized, or
  represented in downstream artifacts.
- The three permitted projections contain exact consecutive indexes:
  `M0630_20:1-5`, `M0640:1-46`, and `M0650:1-41`. There are no gaps inside the
  permitted ranges.
- The 92 permitted rows contain no newly surfaced restricted material and do
  not require reconstruction of an excluded event.
- `narrative_gates.json` declares no source mirrors or repeated-choice groups.

## Immediate continuity and omission boundaries

- `M0630_20` is the clean public-restraint branch from the permitted ending of
  `M0622`. Leo decides not to give himself over to the festival mood in public;
  Sunao sulks, and he promises to make it up to her after they return home.
- That promise remains deliberately vague. Do not state what Leo will do at
  home, and do not compare this branch with or infer events from the fully
  excluded `M0630_10` alternative.
- `M0640` moves to the friends' usual evening gathering on an unspecified later
  night. Sunao is away at the drama club's training camp but continues calling
  Leo every evening. Do not invent the camp's location, duration, or events.
- `M0650` is another summer date after a movie. The exact time elapsed from the
  phone scene is unstated. It ends for model purposes at index `41`, with Sunao
  blushing and flustered during Yoshimi's relationship questions.
- No translation may bridge `M0650:41` to the excluded tail or supply the next
  response, action, topic, or scene transition.

## Timeline and relationship locks

- Leo and Sunao remain an established couple. `M0630_20` continues their
  recurring effort to balance affection with public manners and not become a
  `バカップル`.
- Sunao's irritation in `M0630_20` is a comic reaction to Leo stopping their
  public affection, not a breakup, withdrawal of consent, or serious dispute.
- `M0640` demonstrates their regular contact while apart: Sunao calls nightly,
  and Leo gives the call priority over Kinu's challenge. Only Leo's side of the
  call is displayed; do not invent Sunao's words or Yamada's off-screen action.
- Kinu, Subaru, and Shinichi are visiting Leo for their normal evening
  get-together. They tease him for focusing on his new girlfriend, but remain
  friendly and comic rather than resentful.
- `M0650` independently confirms the couple status to Erika and Yoshimi.
  Sunao says they decided to date, then struggles to reconcile that with her
  earlier first-term claim that she disliked Leo.
- Sunao's permitted explanation progresses carefully: she says Leo won her
  over, is teased for falling quickly, then admits she had already liked him
  somewhat. Do not turn this into a precise confession date or expose a motive
  beyond what she says.
- Yoshimi's questions remain outwardly friendly and congratulatory. Preserve
  their gently probing quality without narrating jealousy, hostility, or later
  route knowledge that the source has not revealed here.

## Scene functions and reveal locks

### `SC_M0630_20_M0640_00`

- Leo's opening internal line directly answers the prior question: he cannot
  simply surrender to the mood. Keep it hesitant and unfinished rather than
  making it a moral lecture.
- Sunao claims she does not mind, despite clearly sulking. Preserve the gap
  between her words and mood as light couple comedy.
- `その分は帰ってから頑張る` at index `3` is a vague promise to make up for
  stopping after they get home. Do not specify affection, an activity, or an
  outcome.
- The closing narration recognizes the difficulty of avoiding an obnoxiously
  lovey-dovey couple image while still considering a girl's feelings. Leo is
  self-aware, not dismissive of Sunao.

### `SC_M0640_00_M0650_00`

- Leo is already on the phone with Sunao at the opening and laughs about
  Yamada. Index `3` explicitly marks the line as being spoken during the call;
  preserve that stage-like parenthetical without inventing what Yamada did.
- Leo's parenthetical at index `5` is a quiet warning not to interrupt. Kinu is
  physically present, and Leo waves her away with his hand at index `6`.
- Subaru checkmates Shinichi, then teaches Kinu the basic chess pieces. Kinu's
  old trauma is from losing badly at go; the source does not recap that match.
- Kinu treats chess as though it were a fantasy tactics game. She expects the
  knight to breathe fire across the square directly in front of it and wants a
  long-range sniper that can kill the enemy king in one shot. Subaru and
  Shinichi correct the game-balance absurdity; do not silently teach real chess
  rules in place of the joke.
- Kinu immediately challenges Leo after the explanation, but he postpones the
  match because he is still on the phone. When he tells Sunao that his childhood
  friends are visiting, Kinu makes a loud celebratory/noisy cry to intrude on
  the call.
- Subaru's `Crab Fried Rice` address is an established silly expansion of
  Kinu's `Crab` nickname, not a food order.
- Subaru matter-of-factly explains that someone with a new girlfriend will
  remain glued to his phone. Kinu insults all twintailed girls, and Subaru
  punctures the claim by recalling her childhood twintails.
- Shinichi is relaxed because he made Leo promise to ask Sunao to introduce him
  to a girl. At index `42`, Leo says every girl refuses when shown Shinichi's
  photo; preserve the girls' agency and the photo as the cause of the refusal.
- Kinu's final remark lands the joke that effort does not guarantee reward.
  Leo's silent final line should remain silent.

### `SC_M0650_00_M0660_00`

- Leo and Sunao emerge from an air-conditioned cinema into humid midsummer
  heat. Sunao enjoyed the action film because it avoided wire action and kept
  the romance element moderate.
- Their earlier romance-film date was awkward because the movie was too
  intense. The permitted source gives no details about its content; do not
  specify what made it intense.
- Leo reflects that easygoing entertainment may suit the beginning of a
  relationship. This is practical dating nerves, not dissatisfaction with
  Sunao.
- It is 29 degrees, cicadas are loud, and Leo suggests shaved ice. Sunao wishes
  peanut-butter syrup existed, extending her established peanut-butter fixation.
- Sunao jokingly associates the craving with her twintail hairstyle, and Leo
  imagines the twintails themselves demanding nutrients. Keep the impossible
  image as a dry narration gag.
- Erika and Yoshimi encounter the couple. Sunao addresses Erika as `Princess`;
  Yoshimi addresses Sunao as the established `Nao-chan`.
- Erika teasingly treats the lively-looking twintails like a creature that
  might eat her crepe. Sunao rejects Erika's already-bitten food. Preserve the
  joke without turning it into literal dehumanization or adding physical detail.
- Erika asks whether Sunao is Leo's girlfriend. Leo hesitates for one beat,
  confirms it, and is immediately scolded by Sunao for the pause.
- At `M0650:29-41`, Yoshimi asks for an explanation, congratulates them, and
  recalls Sunao's earlier claim that she disliked Leo. Sunao's increasingly
  tangled explanation ends with her blushing and flustered. Stop there.

## Voice and speaker locks

- `レオ` = `Leo`: brisk, teasing first-person narration. He tries to balance
  consideration, friendship, and new-couple nerves without becoming formal or
  emotionally detached.
- `素奈緒` = `Sunao`; Leo normally calls her `Konoe`: blunt, proud, quick with
  retorts, easily embarrassed about romance, and transparent when she tries to
  hide enthusiasm or affection.
- `きぬ` = `Kinu`; direct nickname `カニ` = `Crab`: loud, shameless, impatient,
  and imaginative enough to turn chess into a destructive strategy game.
- `スバル` = `Subaru`: relaxed, capable, and dryly corrective. His mock-formal
  `幼少のみぎり` jab about Kinu's childhood twintails should sound playfully
  overdone, not genuinely archaic.
- `新一` = `Shinichi`; nickname `フカヒレ` = `Fukahire`: competitive and
  boastful, then hopeful about Leo finding him a girlfriend. His failures remain
  friendly slapstick.
- `エリカ` = `Erika`; Sunao calls her `Princess`: polished, socially dominant,
  and casually teasing.
- `良美` = `Yoshimi`; direct nickname `よっぴー` remains `Yoppi` when used,
  though it is not spoken in the permitted rows. She calls Sunao `Nao-chan` and
  remains soft, friendly, and gently probing; do not expose later undercurrents.
- `山田君` is mentioned only and remains `Yamada`. Do not create a speaker or
  off-screen line for him.

## Hard renderings and terminology

- `テンションに身を任せる` (`M0630_20:1`) means giving in/getting carried
  away by the mood. Keep it consistent with the immediately preceding scene.
- `その分は帰ってから頑張る` (`M0630_20:3`) should remain a non-specific
  `I'll make it up to you when we get home`-type promise.
- `バカップル` remains the recurring `lovey-dovey idiot couple` idea.
- `演劇部の合宿` is the drama club's training camp. `いつもの夜の集い` is
  the friends' usual evening get-together.
- Chess terms remain `checkmate`, `knight`, and `king`. `碁` is `go`, and the
  player moving first is the one Kinu's imagined sniper would unfairly favor.
- `カニ` -> `Crab`; `カニチャーハン` -> `Crab Fried Rice`; `フカヒレ` ->
  `Fukahire`.
- `ドブメガネ` at `M0640:14` is Kinu's rough one-off insult for Shinichi.
  `Sewer four-eyes` or `gutter glasses` preserves the dirty-place plus glasses
  construction; keep it comic rather than adding a harsher slur.
- `女が出来た` at `M0640:32` means Leo has just gotten a girlfriend. It does
  not imply ownership.
- `ツインテール` is `twintails`, matching established project usage.
- `wire action` at `M0650:4` refers to wire-assisted movie stunts. Do not treat
  it as an in-story action or production command.
- `過激` at `M0650:6` remains the broad `too intense/over-the-top`; do not
  explain the earlier film's content.
- `かき氷` is `shaved ice`; `ピーナッツバターシロップ` is
  `peanut-butter syrup`.
- `姫` -> `Princess`; `良美` -> `Yoshimi`; `ナオちゃん` -> `Nao-chan`.
- `彼女` at `M0650:22` is `girlfriend`. `付き合うことにした` at `31`
  explicitly means Leo and Sunao decided to date.
- `落とされた` at `M0650:35-36` means being won over/made to fall for him,
  not being knocked down. `惚れやすい` means falling in love easily.
- `１学期` is the first school term. Preserve that timeline marker at
  `M0650:34`.
- `要領を得ない` at `M0650:38` means Sunao's explanation is hard to follow or
  not getting to the point; Yoshimi is not declaring it false.

## Ruby, formatting, and deterministic expectations

- No ruby/furigana control, choice token, or engine command appears in the 92
  permitted rows.
- Preserve `「...」` around spoken lines and keep ordinary narration unquoted.
  Preserve source parentheticals and the visible phone-call annotation at
  `M0640:3,5` without turning them into new speaker lines.
- Use ASCII `...`, `--`, straight apostrophes, and ordinary spaces. Do not carry
  source composition spaces into English as manual engine wrapping.
- Translation JSON must not be created for fully excluded
  `SC_M0630_10_M0640_00`. It must contain exactly `M0630_20:1-5`,
  `M0640:1-46`, and `M0650:1-41` for the three permitted scenes. No key from
  `M0650:42-65` may appear.
- All target values must be strings and CP932 encodable. Smart quotes, Unicode
  ellipses, and em/en dashes are forbidden.

## Contested permitted ranges and later QC attention

- `SC_M0630_20_M0640_00:1-5`: preserve Leo's public-restraint decision,
  Sunao's transparent sulk, and the non-specific promise at index `3` without
  importing any excluded-branch detail.
- `SC_M0640_00_M0650_00:3-6`: retain the visible phone-call annotation, keep
  Yamada's action unstated, and distinguish Leo's quiet aside from narration.
- `SC_M0640_00_M0650_00:12-21`: the go callback, `ドブメガネ` insult, and
  fantasy-chess mechanics need focused accuracy/comedy review. Do not repair
  Kinu's deliberately impossible rules.
- `SC_M0640_00_M0650_00:29-45`: preserve `Crab Fried Rice`, the phone teasing,
  childhood-twintail reversal, and every girl's agency in rejecting Shinichi.
- `SC_M0650_00_M0660_00:3-7`: retain the action-film evaluation and the earlier
  film's deliberately unspecified intensity.
- `SC_M0650_00_M0660_00:13-15`: preserve the peanut-butter/twintail nutrition
  gag without rationalizing it.
- `SC_M0650_00_M0660_00:20-28`: Erika's creature-like crepe tease needs playful
  diction without becoming literal or more demeaning than the source.
- `SC_M0650_00_M0660_00:29-41`: maintain Yoshimi's outward friendliness,
  Sunao's first-term timeline, and the progression from `won over` to admitting
  earlier affection. Stop exactly before the excluded tail.
