# Wave-200 shard 44 continuity preflight

Scenes and rows after fail-closed regeneration:
- `SC_M0570_00_M0571_00` - 3 permitted / 12 excluded (15 source rows)
- `SC_M0571_00_M0572_00` - 36 permitted / 0 excluded (36 source rows)
- `SC_M0572_00_M0573_00` - 24 permitted / 2 excluded (26 source rows)
- `SC_M0573_00_M0580_00` - 16 permitted / 6 excluded (22 source rows)

Total: 79 permitted rows; 20 excluded rows; 99 source rows. No target scene is
fully excluded.

## Safety / gates

- The regenerated filtered sources correspond to the supervisor's supplied
  remote checkpoint `0fb7915d`.
- The active `state/content_exclusions_wave500_overlay.json` excludes
  `M0570:1-12`, `M0572:14`, `M0572:16`, and `M0573:13-18`.
- The four model-source projections omit exactly those indexes, contain no
  duplicates, and have no other gaps. Preserve their non-contiguous indexes.
- Excluded rows are outside model scope and are not translation debt. Do not
  infer, bridge, summarize, or create downstream entries for them.
- `narrative_gates.json` declares no source mirrors or repeated-choice groups.
- The 79 permitted rows contain no newly surfaced restricted range. Preflight
  may proceed from the regenerated projections.

## Immediate continuity and omission boundaries

- The preceding permitted context (`M0569:5-9`) leaves the earlier disturbance
  unexplained, says the hut has ended up occupied without naming an occupier,
  and closes on Leo sleeping outdoors while looking toward the distant city
  lights. `M0569:1-4` remain excluded and must not be reconstructed.
- `M0570` resumes only at index 13, after its own excluded opening. The permitted
  tail contains Leo's brief acceptance, his recollection of a promise to enjoy
  the day, and a transition. Do not supply the object of `まあいいか`, the
  circumstances of the promise, or any action from indexes `1-12`.
- The following permitted context (`M0580:1-13`) returns Leo to ordinary life.
  Otome accepts the public explanation that Principal Heizo trained him over
  the weekend; Leo's tan is visible, but the island stay remains unreported.

## Scene functions and reveal boundaries

### `SC_M0570_00_M0571_00`

- Only indexes `13-15` are eligible. Leo decides not to dwell on something left
  outside the projection and recalls that the day was meant to be enjoyed.
- Keep index `14` subject-light: Japanese does not safely establish whether Leo
  alone made the promise or whether it was mutual. Do not invent an addressee,
  occasion, or quoted wording.
- Index `15` is a silent transition. It must not become a recap of the excluded
  opening.

### `SC_M0571_00_M0572_00`

- In bright daylight Leo and Sunao spend the day swimming around Ikajima. Sunao
  calls Leo over to see an unusual fish, ranges farther offshore, and warns him
  about a jellyfish. Leo's urge to go first is protective banter; she answers
  that he would probably overlook it.
- Their exploration moves from a possibly sea-bream-like fish to a possible
  turban shell and another attractive shell. Preserve every uncertainty marker;
  neither underwater identification is authoritative.
- The shell contest calls back to Sunao's failed fishing the previous day. Her
  regret is counterfactual: she wishes she had pursued shells instead; do not
  claim she caught fish then.
- With no rock to rest on, Sunao calls the treading-water Leo her rest point and
  holds onto him. The sequence is competitive physical comedy, not a confession
  or sexual advance. Leo calls the extra load a subtle attack, refuses to give
  up, and then tows her by the hand when challenged.
- Sunao's final laughter and narration establish genuine, wholehearted delight.
  Preserve the unguarded joy without prematurely turning it into romantic
  self-awareness.

### `SC_M0572_00_M0573_00`

- The pair finally leave the water at evening, exhausted after spending the day
  playing. Sunao says they made up for the previous day and that, had it been
  summer vacation, one more night might even have been acceptable. Preserve the
  conditional; do not assert that the present day is already summer vacation.
- Heizo is late for the promised evening pickup. Sunao nevertheless says the day
  was that enjoyable, producing a brief mutual, near-romantic pause.
- Only permitted indexes `10-13`, `15`, and `17-19` define that pause. Leo feels
  drawn toward Sunao's eyes, finds her candid side cute, experiences a racing
  heart, calls her name, and moves his face closer. Indexes `14` and `16` are
  excluded and must remain complete holes.
- `素直` at index `13` is the adjective `honest`, `candid`, or `unguarded`; it
  may lightly echo Sunao's name but is not an overt name-pun exchange. Do not
  force the earlier `sunao` joke into this line.
- Heizo's shout and approaching boat interrupt the moment before any permitted
  line confirms contact. Do not add a kiss, confession, or completed action.
  Leo's complaint is only that the timing is bad.

### `SC_M0573_00_M0580_00`

- On the cruiser back to the mainland, Heizo promises not to tell others about
  the incident; Leo agrees and asks him to inspect the island because Sunao saw
  an unfamiliar silhouette the previous night.
- The unquoted narration then separately recalls the unexplained boom. Heizo's
  `それは儂だ` most immediately answers that boom, as Leo's following narration
  confirms. Keep `それ` narrow (`that`), not an expanded `both of those`.
- Heizo says he is not irresponsible and later swam over, partly for exercise,
  to check on them. This makes him a plausible source of the earlier silhouette,
  but the permitted text does not explicitly equate the silhouette with him.
  Preserve that residual uncertainty.
- Indexes `13-18` are excluded. Index `19` resumes with Leo's general assessment
  that Heizo is an exceptionally large-scale/dynamic person. Do not use it to
  reconstruct the omitted exchange.
- At index `20`, `そのおかげで` and `色々と` remain deliberately general after
  the gap: Leo says he was made to feel flustered/unsettled in various ways,
  without enumerating causes.
- The route beat closes the one-night, two-day island stay as eventful but, in
  Leo's understated admission, enjoyable. Do not convert that admission into a
  relationship declaration.

## Voice / speaker locks

- `レオ` = `Leo`: brisk first-person narration, competitive teasing, mock
  confidence, and guarded sincerity. His romantic awareness stays internal and
  tentative until the source makes an action explicit.
- `素奈緒` = `Sunao`; Leo normally calls her `Konoe`: energetic, capable,
  competitive, and increasingly unguarded while swimming. Her happiness is
  genuine, but no permitted line gives her an explicit confession.
- `平蔵` = `Heizo` / `Principal` in context: booming, matter-of-fact, and
  cheerfully eccentric. His assurances and exercise logic should sound sincere
  to him, not secretly malicious.
- Null-speaker rows remain unquoted. Do not invent a speaker for narration or
  assign omitted dialogue across a gap.

## Hard renderings / ambiguity locks

- `今日は楽しむと約束してたんだ` (`M0570:14`) recalls a promise/commitment
  to enjoy the day. Preserve the ellipsed subject and do not explain its origin.
- `ひょっとして鯛` (`M0571:6`) is only a guess that the fish might be a sea
  bream. `あれ、いねぇ` immediately loses sight of it.
- `クラゲ` (`M0571:13`) is a jellyfish. Sunao's warning is practical, not panic.
- `烏賊島` (`M0571:17`) remains locked as `Ikajima`.
- `サザエっぽい` (`M0571:18`) means something resembling a turban shell; keep
  `-like`/`looks like` uncertainty. `イケてる貝` (`M0571:20`) is the coolest or
  nicest shell, not a newly named species.
- `根をあげる` (`M0571:27`) means give in/give up under the strain. It is not a
  literal root or a cry of pain.
- `昨日の分は取り戻した` (`M0572:5`) means they made up for yesterday's lost
  enjoyment; it does not refer to recovering an object or catch.
- `吸い寄せられそう` (`M0572:11`) is felt attraction/drawing with `seems` or
  `almost`; do not make it irresistible fact. `胸が高鳴った` (`M0572:15`) is
  Leo's racing heart.
- `顔を近づける` (`M0572:19`) makes Leo move his face closer. It does not state
  the intended endpoint or confirm contact.
- `今回の事は他言せん` (`M0573:2`) is Heizo's promise not to tell others about
  this incident. Do not broaden it into a permanent secrecy oath.
- `ついでに` (`M0573:7`) introduces the boom as an additional recollection.
  `理解しがたい` keeps it inexplicable from Leo's prior perspective.
- `儂とて無責任ではない` / `運動がてら` (`M0573:11`) preserve Heizo's comic
  self-justification: he swam over to check on them while getting exercise.
- `無人島１泊２日` (`M0573:21`) is a one-night, two-day island stay, not a
  claim of exactly forty-eight hours.

## Ruby / engine / deterministic expectations

- No ruby/furigana syntax, choice text, or engine control token appears in the
  79 permitted rows.
- Preserve `「...」` around dialogue and leave narration unquoted. Do not add
  engine codes or reconstruct source line breaks as control syntax.
- Translation JSONs must contain exactly `M0570:13-15`, `M0571:1-36`,
  `M0572:1-13,15,17-26`, and `M0573:1-12,19-22`.
- All target values must be strings and CP932 encodable. Smart quotes, Unicode
  ellipses, and em/en dashes are forbidden.

## Items for later QC / targeted arbitration

- `SC_M0570_00_M0571_00:14`: preserve the ellipsed subject and unexplained
  promise context after the exclusion gap.
- `SC_M0571_00_M0572_00:6,18-21`: retain uncertain species identification and
  the shell-contest callback without upgrading guesses into facts.
- `SC_M0572_00_M0573_00:10-13,15,17-19`: maintain the allowed near-romantic
  sequence while leaving excluded indexes `14` and `16` wholly absent; no
  inferred contact or confession.
- `SC_M0573_00_M0580_00:6-11`: keep Heizo's `that was me` tied most directly to
  the boom and do not definitively identify Sunao's silhouette.
- `SC_M0573_00_M0580_00:19-20`: resume after the exclusion gap with generalized
  reactions only; do not supply the omitted exchange or enumerate unstated
  causes.
