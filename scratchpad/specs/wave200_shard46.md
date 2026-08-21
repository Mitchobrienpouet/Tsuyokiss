# Wave-200 shard 46 continuity preflight

Scenes and rows after fail-closed regeneration:

- `SC_M0601_00_M0602_00` - 25 permitted / 0 excluded (25 source rows)
- `SC_M0602_00_M0603_00` - 35 permitted / 0 excluded (35 source rows)
- `SC_M0603_00_M0604_00` - 61 permitted / 0 excluded (61 source rows)
- `SC_M0604_00_M0605_00` - 33 permitted / 8 excluded (41 source rows)

Total: 154 permitted rows; 8 excluded rows; 162 source rows. Translation debt
is exactly 154 rows.

## Safety / extraction / gates

- The active `state/content_exclusions_wave500_overlay.json` excludes
  `SC_M0604_00_M0605_00:33-40`. No other target row is excluded.
- The first three projections contain their complete consecutive index sets:
  `M0601:1-25`, `M0602:1-35`, and `M0603:1-61`.
- The regenerated `M0604` projection contains exactly indexes `1-32,41`.
  Permitted narrative content stops at `32`; index `41` is only a silent
  separator after the exclusion gap and carries no bridge or continuity fact.
- `M0604:33-40` is outside model scope and is not translation debt. Never
  inspect, reconstruct, summarize, infer, bridge, or create a downstream entry
  for any omitted index. Translation must jump directly from `32` to the
  literal separator at `41`.
- All four `scratchpad/model_sources/` projections are structure-identical to
  their payloads in `scratchpad/model_shards/w200-46.json`. Counts, indexes,
  speakers, kinds, Japanese text, and source hashes agree.
- The permitted projections have no duplicate index, malformed dialogue
  wrapper, ruby/furigana marker, choice text, or engine control token.
- The 154 permitted rows contain no newly surfaced restricted material.
- `narrative_gates.json` declares no source mirrors or repeated-choice groups.

## Immediate continuity and timeline

- The preceding permitted scene ends the first school term with Sunao accepting
  Leo's invitation to spend time together again. The outing is framed as a
  clean do-over after Ikajima and repayment for her notebook-related favor;
  neither character has called it an official date or established a romantic
  relationship.
- `M0601` opens at the start of summer vacation. Otome calls the outing a date,
  while Leo remains unsure whether that label applies and privately finds the
  alternative a little disappointing.
- Leo and Sunao discussed destinations by phone, settled only on wandering
  around Matsukasa, and planned to decide the details as they went. Their
  meeting point is the entrance to Dobuzaka Street near Leo's home.
- `M0602` continues at the meeting point. Leo plans to arrive fifteen minutes
  early, but Sunao is already there. She proposes exploring Dobuzaka because
  she lives beyond the station and has rarely looked around this part of their
  shared school district.
- `M0603` is the same outing before lunch: cosmetics and used-book shopping
  reveal ordinary preferences and unexpected points of compatibility.
- `M0604:1-32` moves to lunch at Oasis. While waiting for curry, Leo and Sunao
  discuss classmates' romantic preferences and then Leo's preferred type.
- Narrative analysis stops at `M0604:32`. The next permitted item, `41`, is a
  silent separator only. The following shard independently resumes after lunch
  at an arcade; it does not authorize any reconstruction of the omitted range.

## Relationship, reveal, and agency locks

- Otome's `date` label is her teasing interpretation. Leo's `maybe it isn't`
  response preserves uncertainty, and his disappointment remains an internal
  hint rather than a confession or relationship confirmation.
- Otome says Sunao and Leo seem well suited, but Leo answers only with a clipped
  sound before leaving. Do not expand it into agreement, denial, or a stated
  romantic intention.
- At `M0602:11-13`, Leo sees Sunao check her face in a mirror and merely wonders
  whether she is concerned about her appearance. Do not confirm her motive or
  turn his observation into a more intimate appraisal.
- At `M0602:21-24`, Leo asks whether any men approached or hit on Sunao. Sunao
  reports one occurrence after reaching the station. Preserve her report and
  the count; do not invent the man's behavior, her response, or danger.
- `M0602:34` continues the notebook favor. `service` means accompanying Sunao,
  carrying purchases, and otherwise treating her to the outing. It is not
  monetary employment, romantic obligation, or an intimate euphemism.
- `M0603:20` has Leo become excited by the novelty of visiting this kind of
  shop because Kinu almost never does. Kinu is not the person getting excited.
- Leo's surprise that Sunao has `ordinary girl` tastes is explicitly his own
  expectation and framing. Do not convert it into an objective rule about
  women, make Sunao shallow, or intensify the gender judgment.
- At `M0604:24`, Leo first thinks of Princess internally. Sunao does not hear
  that name and must not be given knowledge of the thought.
- Leo then describes someone with a firm sense of self who stays true to it and
  admits he seems to like strong-willed girls. The description fits the Princess
  in his thought and also sounds flattering to Sunao. Preserve that double fit;
  do not rewrite it as a direct declaration that Sunao is his ideal type.
- Sunao interprets the answer as skillful flattery. Leo says he means it
  sincerely, and she becomes briefly flustered. This is a meaningful romantic
  beat, not a love confession, exclusive preference, or official-couple reveal.

## Scene functions and local hazards

### `SC_M0601_00_M0602_00`

- The cicada chorus and early morning establish the beginning of summer break.
  Keep the opening brisk rather than adding a calendar date.
- Otome pairs `date` with the deliberately dated `アツアツ` tease. The next
  narration explicitly calls her expression obsolete, so the English tease
  and punchline must function together. A dated `quite the hot item`-type line
  is preferable to a modern phrase that makes Leo's reaction inexplicable.
- Otome is going back to her family home that day. Do not imply she will be
  absent for all of summer vacation.
- Her assessment that Sunao is dependable and well matched with Leo is warm,
  matter-of-fact familial approval. It is not foreknowledge of a relationship.
- `変に気負うな` is encouragement not to get oddly worked up or try too hard;
  it does not accuse Leo of bad intent.
- Sunao's quoted phone stance leaves planning to Leo and challenges him to make
  the outing enjoyable. Preserve her proud, teasing expectation without making
  her hostile or Leo resentful.

### `SC_M0602_00_M0603_00`

- Leo arrives intending to be early, sees Sunao already waiting, and watches
  for only two or three minutes out of curiosity. Keep the beat light and
  self-aware; do not add surveillance, suspicion, or sexualized detail.
- His first `charming` compliment is deliberately generic, so Sunao asks for
  something wittier. His next compliment after her station report is more
  suave, and she calls it too affected before admitting she does not dislike
  hearing it. Preserve the escalation and her embarrassed receptiveness.
- `そんなイベント` gives the being-approached exchange a lightly self-aware
  `that kind of event` flavor. It is not an actual scheduled event.
- Sunao's home is on the far side of the station relative to Dobuzaka, although
  they were barely in the same school district. Do not invent an address,
  travel time, or different hometown.
- Leo offers to carry shopping bags or do whatever is useful because the outing
  is his promised repayment. `ドブ坂フラリ旅` is an aimless/leisurely
  Dobuzaka stroll, not a formal tour or trip out of town.

### `SC_M0603_00_M0604_00`

- Sunao finds daytime Dobuzaka less `outlaw` or rough than expected. Leo says
  bars and below-ground live shows make it livelier at night; do not turn this
  into criminal activity or an underground organization.
- Preserve the cosmetics vocabulary: `cosmetics`, `foundation`, `lip gloss`,
  `lip balm`, `perfume`, `concealer`, and `eyelash curler`.
- `M0603:8` means Leo was no longer listening while Sunao examined prices. Do
  not reverse the subject and claim Sunao ignored him.
- Sunao's unfinished comment that Leo may not need perfume remains suggestive
  but unexplained. Do not specify his scent or supply an attraction claim.
- Leo mistakes the eyelash curler for merely `the thing you use on your eyes`;
  nearby customers laugh, Sunao corrects him, and he apologizes. Preserve the
  embarrassment without inventing dialogue for the customers.
- `NANYA` is the displayed parody manga title. Do not silently repair it to a
  real title or insert an unsupported franchise reference.
- `ヤっさん` is an in-work character reference whose English form is not
  otherwise locked in the permitted corpus. Keep a source-stable provisional
  form such as `Yas-san` and flag it for accuracy QC rather than identifying a
  real-world analogue.
- Sunao enjoys wondering which characters will get together, finding scenes
  romantic, and admiring Yas-san. Leo is surprised by the ordinary response.
- Leo invents an exaggerated accusation because he expects Sunao's usual sharp
  retort. She is genuinely hurt for one beat; he apologizes and admits he was
  baiting a comeback, then celebrates when she supplies it. Preserve the
  hurt/apology/retort timing rather than playing every line at one comic level.
- Sunao calls boys' manga childish but explicitly likes the effort characters
  put into defeating stronger opponents. Do not flatten her view into blanket
  contempt for the genre.
- Leo's `brainwash` threat is comic enthusiasm. He buys three indicated books
  for her himself, asks for her impressions, and keeps carrying them until the
  end of the day's outing.
- The closing observations are Leo learning Sunao's tastes and revising his
  image of her. Keep the limited first-person perspective and avoid authorial
  claims about what a `normal girl` must be.

### `SC_M0604_00_M0605_00` — permitted `1-32,41` only

- `店長` is the established Oasis `Manager`. His source lines use exuberant,
  clipped katakana speech. Retain the energetic cadence and occasional emphatic
  wording without inventing nationality markers or heavier caricature.
- Lunch is at Oasis. Kinu is not there at this time of day; do not imply she no
  longer works there or is absent for the whole day.
- Leo orders medium mushroom curry. Sunao orders navy curry, medium, with extra
  milk. Preserve who orders what and do not reinterpret `milk` as a separate
  drink without source support.
- While waiting, they discuss romantic gossip among Class 2-A students. Sunao's
  examples of disliked men must remain distinct: a narcissist who repeatedly
  makes his date hold a mirror for him, a mama's boy, a man who only boasts of
  his exploits, someone with vague dreams, a chronic ditherer, and a flashy liar.
- Leo says some examples make him flinch and complains that women are picky;
  Sunao immediately notes that men are equally picky. Keep the reciprocal
  correction and do not make either side a universal narrator judgment.
- Sunao asks Leo's preferred type. His internal Princess thought, general
  description, Sunao's pleased flattery reading, and his sincere denial of
  flattery must retain that exact reveal order.
- The last narratively usable line is Sunao's flustered `そ、そう` at index
  `32`. Stop there. Index `41` must remain only the translated silent separator;
  it cannot acquire an explanatory transition or imply what happened in
  `33-40`.

## Voice and speaker locks

- `レオ` = `Leo`: casual, observant, lightly self-mocking narration. His
  compliments alternate between awkwardly generic and knowingly suave; his
  romantic interest remains partly guarded and internal.
- `素奈緒` = `Sunao`; Leo normally calls her `Konoe`: proud, blunt, competitive,
  quick to demand better banter, and visibly pleased when sincere praise lands.
  Her ordinary interests should not erase her sharp cadence.
- `乙女` = `Otome`: concise, commanding, upbeat, and familial. Her date teasing
  and compatibility comment are direct but not knowing or intrusive.
- `店長` = `Manager`: exuberant clipped service register at Oasis. Preserve
  source emphasis while keeping the English intelligible.
- Null-speaker rows remain narration. Do not assign internal thoughts,
  separators, customer reactions, or transitions to a character.

## Hard renderings and terminology

| Japanese | Locked handling |
|---|---|
| `松笠` | `Matsukasa`. |
| `ドブ坂通り` / `ドブ坂` | `Dobuzaka Street` / `Dobuzaka`. |
| `オアシス` | `Oasis`, the established curry restaurant. |
| `姫` | `Princess`, referring to Erika. |
| `カニ` | `Crab`, referring to Kinu. |
| `アツアツ` | A deliberately dated couple tease whose obsolescence supports the next-line joke; provisional `hot item`-type handling. |
| `ン` (`M0601:13`) | A clipped grunt/acknowledgment, not the letter `N` or a full verbal answer. |
| `声をかけられる` | In `M0602:21-24`, being approached/hit on; do not invent what followed. |
| `借りを返す` | Repaying the notebook-related favor/debt. |
| `サービス` (`M0602:34`) | Attentive treatment/help during the outing, not employment or sexual euphemism. |
| `コスメ` / `ファンデーション` / `グロス` | `cosmetics` / `foundation` / `lip gloss`. |
| `リップクリーム` / `香水` / `コンシーラー` / `ビューラー` | `lip balm` / `perfume` / `concealer` / `eyelash curler`. |
| `ＮＡＮＹＡ` | `NANYA`; preserve the parody spelling. |
| `ヤっさん` | Provisional `Yas-san`; contested proper-name treatment. |
| `ツッコミ` | A sharp retort/comeback in this exchange, not physical contact. |
| `少年漫画` | `shonen manga` or natural `boys' manga`; retain the genre distinction. |
| `洗脳` | Comic `brainwash`; do not literalize it into coercion. |
| `俺のオゴリ` | Leo is paying/treating Sunao to the books. |
| `きのこカレー中辛` | `medium mushroom curry`. |
| `海軍カレー。中辛。ミルク多め` | `navy curry`, medium, with extra milk. |
| `色恋沙汰` | Romantic entanglements/gossip, not an established relationship for Leo and Sunao. |
| `母親離れできない` | A `mama's boy` / man unable to separate from his mother. |
| `武勇伝ばっか語る` | Constantly boasting about one's exploits. |
| `自分というものをしっかり持っていて、それを貫く` | Having a firm sense of self and staying true to it; not selfishness. |
| `気が強い` | `strong-willed`; do not make it `mean`, `angry`, or physically strong. |
| `お世辞` / `本気` | `flattery` / sincerely meaning what was said. |

## Ruby, formatting, and deterministic expectations

- No ruby/furigana control, choice token, or engine command appears in the 154
  permitted rows.
- Preserve `「...」` around spoken dialogue and leave narration unquoted. Source
  visual spaces and manual line composition are not engine commands.
- Translation JSON must contain exactly `M0601:1-25`, `M0602:1-35`,
  `M0603:1-61`, and `M0604:1-32,41`.
- `SC_M0604_00_M0605_00:33-40` must remain absent from translation, both QC
  lenses, arbitration, build output, and all continuity claims.
- `M0604:41` is a silent separator, not permission to add a bridge across the
  gap. Preserve it as a standalone string only.
- All source indexes and target values remain strings. Do not insert engine
  codes or normalize the immutable source.
- All target text must be CP932 encodable. Use ASCII `...`, `--`, straight
  apostrophes, and ordinary spaces; forbid smart quotes, Unicode ellipses, and
  em/en dashes.

## Contested permitted ranges for later QC / arbitration

- `SC_M0601_00_M0602_00:3-15,17-24`: Otome's date label and dated-expression
  joke, Leo's uncertainty and clipped response, Otome's partial absence, and
  Sunao's leave-the-planning-to-you challenge.
- `SC_M0602_00_M0603_00:1-14,19-27,30-35`: arrival chronology, the unconfirmed
  mirror motive, compliment escalation, one reported approach with no invented
  aftermath, local geography, and the notebook-service framing.
- `SC_M0603_00_M0604_00:1-22`: Dobuzaka's day/night contrast, cosmetics terms,
  Leo as the subject of `聞いてなかった`, the unfinished perfume implication,
  and Leo—not Kinu—as the subject of the novelty reaction.
- `SC_M0603_00_M0604_00:26-43`: `NANYA`, provisional `Yas-san`, ordinary
  romance-manga reactions, and the hurt/apology/retort comedy sequence.
- `SC_M0603_00_M0604_00:44-60`: Sunao's qualified shonen-manga view, Leo's
  three-book gift, carrying agency, and the limited-perspective `ordinary girl`
  conclusion.
- `SC_M0604_00_M0605_00:1-8,10-32,41`: Manager register and exact orders; the
  disliked-type list; Princess as an internal referent; the general type that
  also flatters Sunao; and the absolute hard stop before the excluded range,
  with index `41` retained only as a silent separator.
