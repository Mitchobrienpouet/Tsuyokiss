# Wave-500 shard 55 continuity preflight

Authorized raw scenes after fail-closed content screening:

- `SC_M0682_00_M0683_00` - 70 clean rows, exact indexes `1-70`
- `SC_M0683_00_M0690_00` - 148 clean rows, exact indexes `1-148`
- `SC_M0690_00_Z9999_99` - 45 clean rows, exact indexes `1-45`

Total: 263 raw rows screened; 263 permitted; 0 restricted or dependent rows
identified in this shard.

## Safety / extraction / gates

- Screening used only the three authorized immutable raw dumps. Every scene has
  consecutive indexes, unique engine IDs, complete source hashes, and valid
  dialogue/narration wrappers.
- The canonical manifest and both configured overlays currently contain no
  entry for any shard-55 scene.
- The supervisor-generated filtered projections now exist and reconcile
  exactly with the screened raw payloads: 70, 148, and 45 permitted rows, with
  zero excluded rows. Indexes, speakers, kinds, Japanese text, engine IDs, and
  source hashes are structure-identical in all three scenes.
- The 263 rows contain no restricted sexual content and no setup, aftermath, or
  other dependency that requires an exclusion. Brief teasing physical contact
  in `M0682`, a nonsexual forced karaoke detour in `M0683`, and a verbal kiss
  bargain in `M0690` remain non-explicit and narratively self-contained.
- The earlier shard-54 exclusion remains opaque and was not used to reconstruct
  continuity. Shard 55 independently establishes every relationship and event
  fact needed for its own scenes.
- `narrative_gates.json` declares no source mirrors or repeated-choice groups.
- No restricted-findings report, exclusion-manifest edit, translation, QC,
  arbitration, or build artifact was created by this preflight.

## Immediate continuity and timeline

- `M0682` opens on the final result of the script competition already in
  progress. Yoshimi announces a `39-62` vote, with Erika's entry winning.
- Sunao had worked seriously and expected to win. Erika emphasizes the gap in
  broad natural aptitude, but the later ballot explanation must prevent that
  taunt from becoming the scene's objective verdict on writing quality.
- Erika claims Leo as a joking winner's prize and lightly teases Sunao with the
  gesture. Otome intervenes when Erika goes too far; Sunao leaves the executive
  committee room upset.
- Leo reads the written ballot reasons, realizes why the result occurred, and
  immediately follows Sunao. `M0683` directly continues that pursuit toward the
  station.
- Leo catches Sunao before she reaches home, tries to lift her mood, and takes
  her to karaoke. Their impromptu score contest restores her competitive energy.
- After karaoke, they sit back-to-back at a familiar bench. The place recalls a
  middle-school conversation when Leo saw Sunao hurt and blamed himself. He now
  recognizes that both of them have grown.
- Leo explains the ballots: many voters preferred Sunao's story itself, while
  Erika's more chaotic and entertaining entry was judged better suited to the
  Ryuumei Festival performance. The competition selected a festival piece, not
  the universally superior writer.
- Sunao accepts the loss without erasing it, recognizes that effort alone can
  narrow her perspective, and resolves to leave herself more emotional room.
  Leo and Sunao frame their differing strengths as a reason to support one
  another.
- `M0690` is a subsequent school morning. The exact elapsed time is not stated.
  Sunao wakes Leo at his home while Otome looks on, fulfilling her promise to
  take better care of him.
- The route ends with their familiar bickering, mutual affection, Sunao's
  courage-and-charm slogan, and a displayed Tutorial 6 unlock notice.

## Relationship, reveal, and agency locks

- Leo and Sunao are already an established couple. Otome explicitly calls
  Sunao Leo's girlfriend at `M0682:62`; this is not a new relationship reveal.
- Erika's winner's-prize routine does not transfer ownership or romantic
  commitment. She pulls Leo close, gives him a light hug and cheek-rub tease,
  and tries to provoke Sunao. Preserve Leo's surprise and Sunao's protective
  objection without making the contact more intimate.
- Sunao says Erika may punish or insult her as the loser but must leave Leo out
  of it. This is frustrated self-sacrifice, not consent to harm beyond the
  comic contest context.
- Otome physically stops Erika by pulling her ponytail and condemns her lack of
  compassion. Inori and Nagomi add punishment/reprimand jokes; do not turn those
  lines into an actual depicted disciplinary ordeal.
- At `M0683:33-34`, Leo explicitly forces the karaoke detour and notes that
  Sunao's weakened state lets him be pushy. Preserve that source agency and the
  nonsexual cheering-up context. Do not rewrite it as Sunao's initiative or
  intensify it into violence.
- Sunao first refuses karaoke because of her mood. Leo provokes her competitive
  streak through repeated scoring rounds; her recovery is gradual and visible,
  not instantaneous.
- The ballot explanation preserves two distinct judgments: many voters liked
  Sunao's beautiful story better, but Erika's entry fit the festival assignment
  better. Leo does not declare either writer universally superior.
- Erika knew the distinction and still taunted Sunao. Leo calls that sadistic,
  but the term remains a character judgment about her cruelty in the contest,
  not a new sexual implication.
- Sunao's resolution is to balance serious effort with perspective. It does not
  renounce ambition, hard work, drama, or her competitive personality.
- `M0683:139-140` is a mutual statement about supporting one another through
  life. Keep its romantic weight without turning it into a formal marriage
  proposal.
- At `M0690:20-25`, Leo offers a kiss only as a bargaining ploy for more sleep.
  Sunao is tempted, catches herself, and rejects the trick. No kiss occurs in
  the displayed sequence.
- Sunao's promise to look after Leo indefinitely prompts Leo to wonder whether
  it was an understated proposal. It remains his comic internal question, not a
  confirmed engagement.

## Scene functions and local hazards

### `SC_M0682_00_M0683_00`

- Yoshimi's opening is a neutral results announcement. Erika's `I'm winner`
  outburst is deliberately exuberant and affected; keep it comic rather than
  polishing her into formal victory speech.
- Erika's tennis comparison distinguishes being broadly talented from devoting
  oneself long enough to become the best in a field. Do not make her claim that
  practice is useless.
- Erika compares Sunao's prefectural-level script with writing produced by her
  own world-aiming intellect. Preserve the boast as Erika's taunt, not narrator
  fact.
- `お嬢様頬擦り` at `31` is Erika announcing a silly named cheek-rub move. The
  payoff is Sunao's distress and Erika's deliberate provocation.
- `そそる顔` at `36` means Sunao's expression is enticing/tempting to tease.
  Keep the line suggestive but non-graphic and centered on Erika enjoying the
  reaction.
- Leo's formal-sounding announcement at `61` that he will give in to his mood
  and chase Sunao is a callback to the route's recurring restraint language.
  Retain the self-aware comic register.
- Otome tells Leo to take care of his girlfriend and assumes responsibility for
  lecturing Erika. Leo leaves only after judging that the others can handle the
  executive-room aftermath.

### `SC_M0683_00_M0690_00`

- Sunao's drooping twintails visually mirror her mood. Leo's peanut-butter tube
  gag deliberately fails, showing that she is genuinely upset.
- `３点リーダー多いぞ` at `23` is Leo's meta joke that Sunao is using too many
  ellipses. Preserve the punctuation joke rather than replacing it with a
  generic comment about mumbling.
- The unfinished karaoke contest from their earlier date motivates Leo's new
  challenge. Do not invent the earlier result or any intervening event.
- Preserve every displayed score and its speaker: Leo `86`, Sunao `69`, Leo
  `83`, Sunao `71`, Leo `87`, Sunao `89`, Leo `95`, Sunao `95`, and Sunao's
  eventual `99`. Leo claims the average-score consolation only after losing.
- The fictional/parodic karaoke titles are displayed quoted titles:
  `欲望のサンタクロース`, `米屋がやってきた`, `小粋なマジシャン`, and
  `マイティハート`. Keep title treatment consistent and do not substitute a
  real song or franchise.
- `十八番` at `58` means Sunao's signature/go-to song, not song number eighteen.
- Sunao thanks Leo after realizing that the contest was his way of cheering her
  up. Her laughter then breaks into tears; she turns away and asks not to show
  her face. Keep the emotional change sincere.
- The back-to-back posture at `92` gives Sunao privacy while they talk. Do not
  add an embrace, visible tears, or other contact not stated.
- Script `A` is Sunao/Konoe; script `B` is Erika/Princess. The stated assignment
  is a performance for the `Ryuumei Festival`, not a pure composition contest.
- `頑（かたく）な` at `136` carries the reading and meaning `obstinately
  rigid/stubborn`. Do not render the visible reading as separate dialogue or
  confuse it with ordinary physical hardness.
- The Sports and Martial Arts Festival callback at `134-136` tracks reciprocal
  growth: Sunao previously taught Leo to hold to his core despite fear of the
  result; Leo now teaches her that holding too rigidly can narrow her view.
- `尽くしてあげる` at `145` means Sunao will devote herself/take even better
  care of Leo. It is affectionate and non-explicit.
- `素直じゃない` at `148` reprises the established Sunao/`sunao` name-versus-
  honesty wordplay. Preserve both her self-description and the name echo,
  consistent with `M0609`, without inserting a translator explanation.

### `SC_M0690_00_Z9999_99`

- The opening treats morning drowsiness as Leo's happy sanctuary before Sunao
  removes the towel blanket and warns that he will be late for school.
- Sunao's new caretaking consists of waking and pulling Leo up. Otome approves
  her spirited method while admitting mixed older-sister feelings about the
  couple's closeness.
- Leo's kiss offer is sleepy bargaining. Sunao nearly accepts, recognizes that
  he is exploiting her weakness for affection, and orders him up instead.
- Sunao quietly says she also likes Leo's less dependable side. When he asks
  what she said, she replaces it with the louder claim that he cannot manage
  without her. Preserve the heard/unheard distinction.
- `ずっっと面倒見てあげる` at `35` is an emphatic promise to keep taking care
  of Leo. Leo's proposal thought at `36` remains a joke about its implication.
- `女は、度胸と愛嬌` at `43` is Sunao's compact route-ending slogan: a woman
  needs guts/courage and charm. Preserve its punchy parallel form.
- Index `44` says Leo and Sunao's days together have only just begun. Index
  `45` is a system-style unlock notice and should follow the established
  `Tutorial 6 is now available` convention.

## Voice and speaker locks

- `レオ` = `Leo`: brisk, teasing first-person narration. He uses provocation to
  support Sunao, then becomes direct and thoughtful at the bench without losing
  his comic self-awareness.
- `素奈緒` = `Sunao`; Leo normally calls her `Konoe`: proud, competitive,
  deeply hurt by failure, quick to recover through challenge, and reluctant to
  state affection plainly. Preserve her `sunao` honesty pun.
- `エリカ` = `Erika`; direct title `姫` = `Princess`: dazzling, boastful,
  socially dominant, and deliberately merciless in victory until Otome stops
  her. Her cruelty stays comic-character specific rather than generic abuse.
- `乙女` = `Otome`: decisive, protective, and morally direct. She supports Leo
  and Sunao while retaining an older cousin's mixed feelings in the epilogue.
- `良美` = `Yoshimi`; Erika's nickname `エリー` = `Ellie`: neutral and clear
  when announcing the contest result.
- `なごみ` = `Nagomi`: coldly concise when joining the criticism of Erika.
- `祈` = `Inori`: composed and deadpan when proposing an exaggerated punishment
  for Erika; do not make her girlish or frantic.
- Null-speaker rows remain narration, score cards, separators, or the final
  system-style message. Do not assign them to a character.

## Hard renderings and terminology

- `姫` -> `Princess`; `エリー` -> `Ellie`; `近衛` -> `Konoe` in Leo's
  address; speaker `素奈緒` remains `Sunao`.
- `竜鳴祭` -> `Ryuumei Festival`; `体育武道祭` -> `Sports and Martial Arts
  Festival`.
- `ピーナッバター` at `M0683:14` is a source typo within the recurring
  peanut-butter gag; use the locked `peanut butter` rather than inventing a new
  product.
- `テンションに身を任せる` / `テンションに流される` retains the route's
  `get carried away/give in to the mood` motif while allowing context-sensitive
  natural phrasing.
- `トサカ来た` is Sunao's recurring crest-standing-on-end anger tic.
- `強制連行` is a forced march/dragging someone along; keep the comic karaoke
  context and stated agency.
- `３点リーダー` means ellipsis, specifically the Japanese three-dot leader.
  The English line should joke about Sunao's excessive ellipses.
- `マグレ` means a fluke. `コンディション` is her current condition/form,
  and the elementary-school sports-day comparison is Leo mocking the excuse.
- `１８番` means signature song or go-to number.
- `Ａ（近衛）` / `Ｂ（姫）` must remain mapped to `A (Konoe)` / `B
  (Princess)` throughout the ballot explanation.
- `ドタバタ` describes lively slapstick/farce suited to a festival production.
- `話の構成力` is story construction/compositional skill; Leo says that was
  not the sole competition criterion.
- `頑（かたく）な` -> `stubborn`, `rigid`, or `obstinate` according to the
  sentence; preserve the ruby-derived meaning.
- `尽くす` means devoted caretaking in these scenes, not servitude or an
  intimate euphemism.
- `素直じゃない` means not honest/frank/straightforward and must retain the
  `Sunao` name pun.
- `女は度胸と愛嬌` should retain the balanced `guts/courage and charm`
  slogan.
- Final system line -> established `Tutorial 6 is now available` wording.

## Formatting and deterministic expectations

- The raw payload contains exactly `M0682:1-70`, `M0683:1-148`, and
  `M0690:1-45`, with no gaps or duplicate indexes.
- No choice token or engine command appears. `M0683:136` contains a visible
  parenthetical ruby reading that must inform meaning without becoming an
  extra line or engine code.
- Preserve `「...」` around spoken dialogue and leave narration, score cards,
  separators, and the Tutorial notice unquoted.
- Preserve the displayed song-title and score quotation function with natural
  ASCII punctuation in English. Do not copy Japanese composition spaces as
  manual wrapping.
- Use ASCII `...`, `--`, straight apostrophes, and ordinary spaces. All target
  strings must be CP932 encodable; smart quotes, Unicode ellipses, and em/en
  dashes are forbidden.
- Any later translation JSON must match its filtered projection exactly: 70,
  148, and 45 rows respectively, for 263 permitted rows total.
- Hard stop: this screen/preflight authorizes no translation, QC, arbitration,
  config, state, or exclusion-manifest edit.

## Contested clean ranges for later QC attention

- `SC_M0682_00_M0683_00:1-18`: preserve the `39-62` result, Erika's talent
  boast as character speech, and Sunao's sincere frustration.
- `SC_M0682_00_M0683_00:19-42`: keep the winner's-prize provocation light and
  non-explicit, preserve Sunao's protective agency, and retain Erika's named
  cheek-rub gag without escalation.
- `SC_M0682_00_M0683_00:43-69`: preserve Otome's intervention, the written
  ballot-reason setup, Leo's mood-language callback, and the explicit
  girlfriend reference.
- `SC_M0683_00_M0690_00:1-34`: maintain the pursuit chronology, peanut-butter
  gag, excessive-ellipsis joke, prior-date karaoke callback, and forced-detour
  agency without inventing danger or consent.
- `SC_M0683_00_M0690_00:35-78`: verify all scores, speakers, fictional titles,
  `signature song`, and the transition from dejection to competitive energy.
- `SC_M0683_00_M0690_00:79-99`: keep Sunao's gratitude, broken laughter,
  unseen emotion, back-to-back posture, and middle-school callback distinct.
- `SC_M0683_00_M0690_00:100-138`: preserve the two ballot judgments, A/B
  ownership, Ryuumei Festival criterion, accepted loss, reciprocal growth, and
  ruby-derived `stubborn` meaning.
- `SC_M0683_00_M0690_00:139-148`: retain the mutual-support weight, Sunao's
  caretaking promise, Leo's request for plainer affection, and the concluding
  Sunao/honesty wordplay.
- `SC_M0690_00_Z9999_99:1-27`: preserve the morning setting, Otome's presence,
  the unfulfilled kiss bargain, and her mixed older-sister reaction.
- `SC_M0690_00_Z9999_99:28-45`: keep Sunao's unheard admission, quasi-proposal
  implication, courage-and-charm slogan, route-ending line, and Tutorial 6
  system notice in exact order.
