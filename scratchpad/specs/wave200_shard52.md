# Wave-200 shard 52 continuity preflight

Scenes and rows after final fail-closed regeneration:

- `SC_M0660_00_M0661_00` - 10 permitted / 0 excluded (10 source rows)
- `SC_M0661_00_M0662_00` - 30 permitted / 13 excluded (43 source rows;
  permitted `1-30`, excluded `31-43`)
- `SC_M0662_00_M0663_00` - 0 permitted / 9 excluded (9 source rows;
  fully excluded)
- `SC_M0663_00_M0664_00` - 0 permitted / 271 excluded (271 source rows;
  fully excluded)

Total: 40 permitted rows; 293 excluded rows; 333 source rows. Translation debt
is exactly 40 rows.

## Safety / gates

- Deterministic reconciliation finds 3,620 permitted model-source rows and
  1,117 excluded rows in the current wave-500 M-route extraction, for 4,737
  source rows total. Ten scenes are fully excluded.
- The only shard-52 model-source projections are
  `SC_M0660_00_M0661_00:1-10` and
  `SC_M0661_00_M0662_00:1-30`. Both ranges are consecutive, contain no
  duplicate indexes, and carry complete engine IDs and source hashes.
- The active overlay records exactly `SC_M0661_00_M0662_00:31-43`,
  `SC_M0662_00_M0663_00:1-9`, and
  `SC_M0663_00_M0664_00:1-271` as excluded. No projection exists for either
  fully excluded scene.
- All 293 excluded rows are zero translation debt. They were not inspected or
  reconstructed during this preflight and must remain absent from translation,
  QC, arbitration, contested, and build artifacts.
- The permitted material is a non-explicit domestic/date setup. It contains no
  newly surfaced restricted material and does not require any fact from the
  opaque continuation to make its displayed events intelligible.
- `narrative_gates.json` declares no source mirrors or repeated-choice groups.

## Immediate continuity and omission boundaries

- The last permitted scene in shard 51 established Leo and Sunao as a couple
  and ended with Sunao flustered by Yoshimi's questions. Its excluded tail
  remains opaque. Do not bridge that omission or claim what happened between
  it and this shard.
- `M0660` opens on a later summer-vacation morning. The precise elapsed time
  from the prior permitted date is unstated. Otome expects to be occupied first
  by her club and then by executive-committee work, while Leo has a date with
  Sunao.
- The closing narration at `M0660:10` explicitly identifies the exchange as
  having happened that morning. `M0661:1` then advances to the appointed time
  later that day; preserve the clean time jump without inventing a clock time.
- Sunao arrives at Leo's home in uniform because she came directly from
  preparing drama-club props. Otome is away at the martial-arts club and will
  then help the executive committee.
- The permitted scene ends at `M0661:30` while Leo internally complains that
  Sunao rejects every activity he proposes. It supplies no answer, next action,
  or scene transition. Translation must stop there.
- `M0661:31-43` and both following scenes are an opaque hard boundary. Do not
  foreshadow, summarize, infer, or bridge anything beyond index `30`.

## Timeline, relationship, and agency locks

- Leo and Sunao remain an established couple, but their habitual address has
  not changed: Leo calls her `Konoe`, and she calls him `Tsushima`. Do not
  switch either character to first-name address.
- Otome knows about the date and gives Leo practical grooming and conduct
  advice. Her tone is concise and protective, not suspicious, prurient, or a
  prediction about how the date will develop.
- Otome says that she, the Princess, and Sato are sufficient for the committee
  work. Erika and Yoshimi are only mentioned; neither is present or speaking in
  these permitted rows.
- Sunao's realization at `M0661:10` is that she and Leo are alone because
  Otome is absent. Her repeated phrasing shows sudden self-consciousness. It is
  not an accusation, refusal, or statement of a further plan.
- Leo's heart begins pounding at `M0661:11`. His joke about Otome's room at
  `12` draws Sunao's immediate retort, and the familiar banter lets him relax at
  `14`. Preserve that emotional sequence.
- At `M0661:16`, the grammar places both Leo and Sunao together on the bed while
  close to one another. It does not specify one character forcing, carrying,
  pinning, or otherwise unilaterally moving the other, and it does not say they
  lie down. Preserve shared agency and the limited physical fact.
- Sunao challenges the immediate choice of the bed; Leo explains that sitting
  directly on the floor seemed unsuitable, and she accepts that explanation.
  Do not add a hidden motive or an explicit interpretation.
- Music and games are Leo's only displayed suggestions. Sunao declines both,
  then tells him to decide what they should do. Her complaint at `M0661:27` is
  about his lack of consideration/initiative; it is not consent to an unstated
  activity.

## Scene functions and reveal locks

### `SC_M0660_00_M0661_00`

- Otome reports that executive-committee help will keep her out late. Leo's
  brief reaction at index `2` is noticeably hesitant, but the source does not
  explain his thought. Keep the pause without supplying a motive.
- Leo notes that Otome is busy despite summer vacation and asks whether he is
  needed. Otome answers that she, the Princess, and Sato can handle it. Preserve
  Leo's offer and Otome's refusal; do not imply that he is shirking a duty.
- Otome confirms that Leo has a date with Konoe, then tells him to look tidy and
  behave like a gentleman. The advice lands as firm older-cousin guidance.
- Index `10` retrospectively frames all preceding dialogue as the morning
  exchange. It is Leo's narration, not another spoken line or a new scene event.

### `SC_M0661_00_M0662_00` (permitted `1-30` only)

- Index `1` is a time-transition narration. Sunao's greeting at `2` is casual;
  the source spelling does not require an English misspelling.
- Sunao stopped at the drama club to prepare props and came straight over, which
  explains her uniform. Keep the causal sequence and do not imply that club
  practice itself continued at Leo's home.
- Sunao asks after `Kurogane-senpai`. Leo says Otome is at the martial-arts club
  and afterward has student-council work. Keep `Kurogane-senpai` as Sunao's
  established respectful address.
- The alone-together realization, Leo's nerves, and the Otome-room joke are a
  compact romantic-comedy beat. Keep the tone non-explicit and allow Sunao's
  sharp retort to release the tension.
- Sunao notes that this is her second visit to Leo's room. The permitted source
  does not describe the first visit here; do not recap it from memory or add a
  comparison beyond the count.
- The bed exchange depends on Sunao first protesting, Leo offering a mundane
  floor-versus-bed explanation, and Sunao accepting it. Leo then privately
  finds her reaction odd. Preserve this order and do not make his narration
  audible to her.
- Leo offers music, then a game. Sunao is not in the mood for music and says she
  does not play games much; she does not condemn either hobby in general.
- `M0661:25` is ordinary internal narration expressing that Leo has run out of
  options. It is not an engine choice, menu prompt, or branch instruction.
- Leo asks what Sunao wants; she turns the responsibility back on him and calls
  him inconsiderate. His final two beats are wounded comic protest followed by
  a generalization that merely shooting down suggestions gets nowhere.
- Stop after `M0661:30`. No wording may anticipate how the disagreement is
  resolved.

## Voice and speaker locks

- `レオ` = `Leo`: brisk, self-aware first-person narration and casual dialogue.
  His date nerves show through comic internal reactions, not elevated romance
  prose or explicit speculation.
- `素奈緒` = `Sunao`; Leo addresses her as `Konoe`: proud, blunt, easily
  embarrassed, and quick with tsukkomi retorts. She calls Leo `Tsushima` even
  while dating him.
- `乙女` = `Otome`: disciplined, direct, and unflustered. She calls Leo `Leo`
  or `you` according to the line's natural syntax; keep her advice firm without
  making it parental or threatening.
- `姫` is the locked title `Princess` for Erika. `佐藤` remains `Sato` in
  Otome's surname-register reference. Neither mention creates a speaker entry.
- `鉄先輩` is Sunao's established `Kurogane-senpai`, not a literal `Iron` name
  in this route context.
- Null-speaker rows are Leo's narration or transitions. The permitted payload
  contains 30 dialogue rows and 10 narration rows; preserve those wrappers and
  roles exactly.

## Hard renderings and terminology

- `生徒会執行部` -> `executive committee`; `生徒会の仕事` may naturally be
  `student-council work`. Do not invent a meeting, emergency, or named task.
- `拳法部` follows established M-route usage as `martial-arts club`.
- `演劇部` -> `drama club`; `小道具の用意` means preparing/getting props
  ready, not performing or building a stage set unless the English remains that
  broad.
- `身だしなみはきっちり` means looking neat/well groomed for the date.
  `紳士的に振舞う` means behaving like a gentleman; preserve both pieces of
  Otome's advice.
- `早くも約束の時間` marks the appointed time arriving quickly/before long.
  It does not say Sunao arrived early or late.
- `二人きり` means Leo and Sunao are alone together. Keep Sunao's self-conscious
  repetition rather than compressing it into neutral exposition.
- `寄り添いながら二人してベッドの上に乗っかる` at `M0661:16`
  describes the two moving/sitting together close on the bed. Do not add lying
  down, an initiator, or further contact.
- `そのまま下に座る` at `M0661:18` contrasts the bed with sitting directly
  on the floor. `下` is not downstairs or beneath the bed.
- `気が利かない` at `M0661:27` is `inconsiderate`, `thoughtless`, or
  `you never take the hint` in this light banter; avoid a harsher moral judgment.
- `反論だけじゃ世の中うまくいかない` at `M0661:30` is Leo's comic claim
  that merely objecting/shooting down ideas gets nowhere. It is not a serious
  philosophical statement and does not grant assent to any unstated option.

## Formatting and deterministic expectations

- No ruby/furigana control, choice token, or engine command appears in the 40
  permitted rows.
- Preserve `「...」` around all spoken dialogue and keep narration unquoted.
  Normalize source `――` to project-safe `--` and Japanese ellipsis runs to
  ASCII `...` as natural English cadence requires.
- Use straight apostrophes and ordinary spaces. Do not retain Japanese source
  composition spaces as manual wrapping, and do not use smart quotes, Unicode
  ellipses, or em/en dashes.
- If a later translation stage is authorized, its JSON must contain exactly
  `SC_M0660_00_M0661_00:1-10` and
  `SC_M0661_00_M0662_00:1-30`, with no gaps or extra keys. Every target value
  must be a string and CP932 encodable.
- No translation JSON may be created for `SC_M0662_00_M0663_00` or
  `SC_M0663_00_M0664_00`. No key from `SC_M0661_00_M0662_00:31-43` may appear
  anywhere downstream.
- Hard stop: this preflight authorizes no translation. The next stage, only if
  separately assigned, must process the 40 permitted rows and stop exactly at
  `SC_M0661_00_M0662_00:30`.

## Contested permitted ranges and later QC attention

- `SC_M0660_00_M0661_00:1-2`: keep Otome's expectation of returning late and
  Leo's unexplained hesitant reaction without adding a reason or anticipation.
- `SC_M0660_00_M0661_00:3-9`: preserve Leo's offer to help, Otome's statement
  that the three committee members are sufficient, surname/title register, and
  both halves of her date advice.
- `SC_M0661_00_M0662_00:1-10`: retain the time transition, prop-preparation
  causality, uniform explanation, Kurogane-senpai address, and Sunao's repeated
  alone-together realization.
- `SC_M0661_00_M0662_00:11-20`: track Leo's nerves and relaxation, keep the
  Otome-room joke light, preserve joint agency at the bed, and do not add a
  lying posture or hidden intention.
- `SC_M0661_00_M0662_00:21-30`: distinguish Sunao's two separate refusals,
  keep index `25` as narration rather than a choice token, and preserve the
  suggestion/rebuttal punchline without implying any next activity.
- Boundary lock: stop at index `30`; excluded `31-43` and both following scenes
  must remain wholly opaque and artifact-free.
