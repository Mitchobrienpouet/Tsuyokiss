# Wave-200 shard 48 continuity preflight

Scenes and rows after fail-closed regeneration:

- `SC_M0609_00_M0610_00` - 29 permitted / 20 excluded (49 source rows)
- `SC_M0610_00_M0611_00` - 37 permitted / 13 excluded (50 source rows)
- `SC_M0611_00_M0612_00` - 10 permitted / 5 excluded (15 source rows)
- `SC_M0612_00_M0615_00` - 0 permitted / 363 excluded (363 source rows; fully excluded)

Total: 76 permitted rows; 401 excluded rows; 477 source rows. The fourth
scene is fully excluded and carries no translation debt.

## Safety / extraction / gates

- The assigned regenerated checkpoint reported 4,177 permitted and 560
  excluded rows globally. During this preflight, a later out-of-shard
  supervisor update advanced the active extraction report to 4,100 permitted
  and 637 excluded. None of the added ranges intersects shard 48; this shard's
  four manifest entries, three model hashes, and independent reconciliation
  remain unchanged at 477 raw = 76 permitted + 401 excluded.
- The active wave-500 overlay declares exactly `SC_M0609:1-20`,
  `SC_M0610:37-49`, `SC_M0611:11-15`, and `SC_M0612:1-363` for this shard.
- The three surviving projections contain exactly `M0609:21-49`,
  `M0610:1-36,50`, and `M0611:1-10`. Their file hashes match the regenerated
  extraction report.
- `SC_M0612_00_M0615_00` has no `scratchpad/model_sources/` projection and no
  translation, QC, or contested artifact. None should be created while the
  exclusion remains active.
- Every excluded range is an opaque omission boundary. Do not inspect,
  reconstruct, summarize, bridge, or create a downstream line for any omitted
  index. In particular, `M0610:36` must jump directly to `M0610:50`, and
  `M0611` must end for model purposes at index `10`.
- `narrative_gates.json` declares no source mirrors or repeated-choice groups.
- No newly restricted content or dependent continuation surfaced in the 76
  permitted rows. The remaining projections are clean for translation.

## Immediate continuity and omission boundaries

- The preceding permitted scene ends with Sunao accepting Leo's request for
  ordinary dates and Leo admitting that her answer made him very happy. That
  is the last usable earlier context.
- `SC_M0608_00_M0609_00:55-66` and `SC_M0609_00_M0610_00:1-20` form a double
  opaque boundary before this shard resumes at `M0609:21`. Do not infer what
  was said or done between the earlier acceptance and the culture-festival
  callback at index `21`.
- `M0609:21-49` supplies its own permitted progression: the pair revisit the
  long detour caused by their middle-school disagreement, Leo teases Sunao
  about affection concealed by hostility, and they explicitly establish a
  dating relationship.
- `M0610` occurs later the same day. Leo has brought Sunao to his home; index
  `5` notes that nobody else is there. Their new relationship makes both of
  them self-conscious while they watch a DVD, but the permitted text states no
  further intent.
- `M0610:37-49` is opaque. Index `50` independently resumes with a window
  opening and supplies the entry beat for `M0611`; do not add a cause, reaction,
  action, or transition across the gap.
- `M0611:1-10` is the immediate comic interruption. Its references to Leo and
  Sunao dating are licensed by `M0609:39-42`, not by excluded material.
- `M0611:11-15` and the entirety of `SC_M0612_00_M0615_00` remain opaque. No
  later outcome, action, or relationship development may be inferred from
  them in this shard.

## Timeline and relationship reveal boundary

- `M0609:21` recalls the failed middle-school culture festival already
  established earlier in the route. The exact disagreement is not restated in
  the permitted rows; keep the callback general.
- At `M0609:22-23`, Leo begins an unfinished question and privately wonders
  whether Sunao's harsh words were affection in disguise. This is Leo's
  inference, not a blanket admission by Sunao.
- Sunao immediately qualifies the idea at `M0609:27`: before they made up, she
  says she was genuinely angry. Do not rewrite all past hostility as secret
  flirtation.
- `M0609:35` states reciprocal liking. Leo then makes an explicit relationship
  request at `39`, and Sunao accepts at `42`. This is the point where the date
  request from the preceding scene becomes an established dating relationship.
- The strong handclasp and hand compliments at `M0609:40-47` deliberately land
  like comradeship. Index `48` explicitly jokes that they look more like male
  friends than lovers; do not sexualize or sentimentalize the gag.
- `M0611:4,7,9` confirm the new status with `girlfriend`, `started dating`, and
  `we're dating`. Preserve this confirmation; do not weaken it back into merely
  spending time together.
- Leo only speculates at `M0611:8` that people at the day's crowded venues may
  already have viewed them as a couple. The source of Shinichi's information
  remains unknown.

## Scene functions and reveal locks

### `SC_M0609_00_M0610_00`

- Sunao describes the pair's middle-school culture-festival disagreement as
  the start of a long detour. Preserve the counterfactual framing without
  supplying the omitted dispute.
- Leo's `好意の裏返し` thought and his `素直じゃない` teasing form a setup
  that Sunao first bans as a joke and then corrects. Her name/adjective wordplay
  and the repeated `NG` response must remain legible across indexes `23-34`.
- `トサカ来る` at indexes `27` and `32` is Sunao's recurring crest-standing-
  on-end anger tic. Keep it consistent with the recent visible-crest rendering.
- At indexes `35-42`, preserve the progression from mutual liking, through
  Leo's serious face and direct request, to Sunao's acceptance. Do not move the
  formal relationship reveal earlier than index `39` or its acceptance earlier
  than index `42`.
- Leo extends his hand; Sunao extends hers; they grip firmly. Preserve that
  exact reciprocal agency. Their physical contact is a handshake-like comic
  seal on the relationship, not evidence of any unstated act.
- Index `49` is a narrator transition fragment beginning with the source's
  long dash. Keep its suspended cadence and do not complete it with invented
  material.

### `SC_M0610_00_M0611_00`

- Sunao denies having said that she wanted to come; she does not say that Leo
  forced her or that she did not want to visit. Leo answers that he brought
  her, and narration confirms the destination is his home.
- Sunao correctly attributes the downstairs cleaning to Kurogane-senpai, then
  checks whether Leo cleans his own room. Leo says that he does. Preserve who
  cleans which space and do not turn the exchange into criticism of Otome.
- The mutual silence after the room inspection is new-couple awkwardness. Leo
  abruptly adopts a lightly polite register when suggesting a DVD, then tries
  to take a small amount of initiative.
- Sunao and Leo are both only children. Her admiration is for having a TV in
  his room; Leo suggests that she ask for one of her own. Do not invent a
  sibling or ownership dispute.
- During the DVD, Leo cannot concentrate. Each catches the other looking, both
  hurriedly look away, and Leo concludes that they may be too conscious of each
  other. Keep the mutuality and mild self-consciousness; do not state arousal,
  fear, or a plan absent from the source.
- Index `36` ends the DVD viewing. The next permitted index is `50`, where the
  window suddenly opens. Treat this as a hard cut across the exclusion gap.

### `SC_M0611_00_M0612_00`

- Shinichi enters through the window with an overblown third-person self-
  introduction. Leo gives him five counts to leave and glares at the `thing`
  that entered; retain the comic dehumanization rather than upgrading it to a
  neutral `person`.
- Shinichi invokes an `urban legend` that friends turn cold when one gets a
  girlfriend. His melodramatic conclusion is a joke, but `girlfriend` itself
  matches the now-established relationship.
- Shinichi leaves crying. Leo's private apology uses the locked nickname
  `Fukahire`.
- Leo wonders how the information leaked, then offers only a tentative public-
  appearance hypothesis. Do not identify a source or turn the hypothesis into
  fact.
- Leo reminds himself that he and Konoe are now dating and that he needs to get
  his act together. Keep `しっかり` broad; do not invent a promise to protect,
  provide for, or control her.
- Shinichi's interruption releases Leo's tension at index `10`. Stop there;
  the excluded tail authorizes no additional beat.

### `SC_M0612_00_M0615_00`

- Fully excluded: 0 permitted / 363 excluded.
- No model source, translation, QC record, arbitration note, continuity
  reconstruction, or future translation debt should exist for this scene.

## Voice and speaker locks

- `レオ` = `Leo`: brisk first-person narration, quick teasing, and
  self-conscious sincerity. His request at `M0609:39` is deliberately direct;
  his awkwardness at home remains recognizably casual rather than poetic.
- `素奈緒` = `Sunao`; Leo normally calls her `Konoe`, while she calls him
  `Tsushima`: proud, combative, easily flustered, and newly willing to answer
  him directly. Preserve her tsundere-shaped denial without making it a denial
  of the relationship she has just accepted.
- `新一` = `Shinichi`; narration may use `Fukahire`: grandiose,
  self-dramatizing, intrusive, and quickly reduced to comic despair. His
  third-person `新さん` self-label should remain playful rather than formal.
- `鉄先輩` remains the established `Kurogane-senpai` in Sunao's speech.
- Null-speaker rows are Leo's narration. Do not assign the internal inferences,
  transitions, silences, or window action to a character.

## Hard renderings and terminology

| Japanese | Locked handling |
|---|---|
| `中学の文化祭` | `middle-school culture festival`; preserve the established failed-event callback without adding details. |
| `遠回り` | figurative `long detour`, referring to the years lost after the disagreement. |
| `好意の裏返し` | affection in disguise / the flip side of affection; keep it as Leo's inference and preserve Sunao's qualification. |
| `素直じゃない` / `素直になった` | retain the recurring `sunao` name/adjective wordplay consistently across `M0609:24-26,33-34`. |
| `NG` | one consistent `off-limits` / `no-go` response to the repeated joke. |
| `トサカ来る` | Sunao's crest-standing-on-end anger tic, consistent with the recent route rendering. |
| `付き合ってくれ` | an explicit `go out with me` / dating request here, not generic accompaniment. |
| `恋人` / `彼女` | `lovers` / `girlfriend`; the relationship is explicit after `M0609:42`. |
| `男の友情` | `male friendship` / male camaraderie; preserve the intentionally unromantic handshake gag. |
| `鉄先輩` | `Kurogane-senpai`. |
| `DVD` / `TV` | ordinary `DVD` / `TV`; fullwidth source typography is not an engine token. |
| `リードをとる` | take the initiative / lead the interaction slightly, not physically lead Sunao. |
| `意識しすぎ` | mutually too self-conscious / too aware of each other; do not make it explicit desire. |
| `新さん` | Shinichi's comic third-person self-label; `Shin-san` or a comparably self-important solution is contested. |
| `フカヒレ` | locked nickname `Fukahire`. |
| `都市伝説` | `urban legend`. |
| `しっかりしないと` | Leo needs to get his act together / be dependable; keep the obligation general. |

## Ambiguity and agency locks

- `M0609:21-27`: the festival disagreement remains unspecified; Leo's
  affection reading is an inference that Sunao explicitly narrows.
- `M0609:24-34`: preserve both repeated joke chains--the `sunao` wordplay and
  Sunao's crest anger--without flattening them into unrelated generic lines.
- `M0609:35`: grammar is reciprocal: Sunao likes Leo and Leo likes Sunao.
- `M0609:39-42`: Leo requests a dating relationship and Sunao accepts it.
  Preserve speaker, agency, and reveal order.
- `M0609:40-48`: Leo offers his hand, Sunao reciprocates, and they clasp. The
  final comparison is comic male friendship rather than a disavowal of their
  new relationship.
- `M0610:1-5`: Sunao's denial concerns who voiced the wish to visit; Leo is the
  one who brought her home. Being alone together is an observation only.
- `M0610:23-24`: Leo's DVD suggestion is his tentative initiative, not an
  instruction or an established plan from omitted context.
- `M0610:30-35`: both are looking at each other and both avert their eyes. Do
  not make either character the sole initiator.
- `M0610:36,50`: no semantic or causal bridge may cross omitted indexes
  `37-49`.
- `M0611:1-3`: Shinichi comes through the window; Leo's `thing` label is comic
  contempt, not genuine uncertainty about identity.
- `M0611:7-8`: the information leak is real, but Leo's explanation for it is
  only speculation.
- `M0611:9-10`: the dating status is certain; the scope of Leo's intended
  responsibility remains unspecific; the interruption merely eases his nerves.

## Ruby / engine / deterministic expectations

- No ruby/furigana control, choice token, or engine command appears in the 76
  permitted rows.
- Preserve `「...」` around all dialogue and leave narration unquoted. Source
  composition spaces are not engine codes.
- Translation JSONs may be created only for the three partially permitted
  scenes and must contain exactly `M0609:21-49`, `M0610:1-36,50`, and
  `M0611:1-10` respectively.
- No index from `M0609:1-20`, `M0610:37-49`, `M0611:11-15`, or
  `M0612:1-363` may appear in translation, QC, arbitration, or build outputs.
- Convert the long dash at `M0609:49` to the project's CP932-safe ASCII dash
  convention while preserving its transition function.
- All target values must be strings and CP932 encodable. Use ASCII `...`,
  `--`, straight apostrophes, and ordinary spaces; forbid smart quotes,
  Unicode ellipses, and em/en dashes.

## Contested permitted ranges for later QC / arbitration

- `SC_M0609_00_M0610_00:21-27`: festival callback, unfinished thought,
  affection inference, and Sunao's corrective qualification.
- `SC_M0609_00_M0610_00:24-34`: recurring `sunao` wordplay, repeated `NG`
  response, and crest-anger continuity.
- `SC_M0609_00_M0610_00:35-49`: reciprocal liking, exact formal-relationship
  reveal order, handshake agency, male-friendship punchline, and suspended
  transition fragment.
- `SC_M0610_00_M0611_00:1-5,9-18`: visit agency, being alone, and exact
  Kurogane-senpai versus Leo housekeeping attribution.
- `SC_M0610_00_M0611_00:20-35`: silence cadence, Leo's tentative initiative,
  only-child/own-TV facts, and mutual self-consciousness.
- `SC_M0610_00_M0611_00:36,50`: hard discontinuity across excluded indexes
  `37-49`; index `50` must stand alone.
- `SC_M0611_00_M0612_00:1-10`: Shinichi's self-label, comic `thing` referent,
  girlfriend/status confirmation, unknown leak source, and the limited scope of
  Leo's `しっかり` resolve.
