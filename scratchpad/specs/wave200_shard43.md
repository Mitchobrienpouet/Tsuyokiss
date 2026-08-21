# Wave-200 shard 43 continuity preflight

Scenes and permitted rows after fail-closed regeneration:
- `SC_M0566_00_M0567_00` - 25 permitted / 0 excluded
- `SC_M0567_00_M0568_00` - 0 permitted / 12 excluded (fully excluded)
- `SC_M0568_00_M0569_00` - 4 permitted / 59 excluded
- `SC_M0569_00_M0570_00` - 5 permitted / 4 excluded

Total: 34 permitted rows; 75 excluded rows. The fully excluded scene and all
excluded ranges are outside model scope and are not translation debt.

## Safety / gates

- Active `state/content_exclusions_wave500_overlay.json` excludes
  `SC_M0567_00_M0568_00:1-12`, `SC_M0568_00_M0569_00:1-59`, and
  `SC_M0569_00_M0570_00:1-4`.
- The regenerated `scratchpad/model_shards/w200-43.json` marks `M0567` as
  `fully_excluded`, gives it a null payload, and provides no model-source file
  for it. Do not create a translation, QC record, contested note, bridge, or
  summary for that scene.
- The only eligible target rows are `M0566:1-25`, `M0568:60-63`, and
  `M0569:5-9`. Their shard payloads exactly match the regenerated filtered
  `scratchpad/model_sources/` projections.
- Preserve the original non-contiguous indexes. The gaps are intentional and
  must never be filled, reconstructed, summarized, or treated as missing work.
- `narrative_gates.json` declares no source mirrors or repeated-choice groups.

## Immediate continuity and omission boundaries

- The preceding permitted scene ends with Leo separating the futons by roughly
  six meters after sleeping Sunao crosses the improvised border and clings to
  him. He returns to bed believing the extra distance has solved the problem.
- `M0566` immediately repeats and escalates that nonsexual bad-sleeping-habits gag:
  Sunao has crossed the room and clung to Leo again while still fully asleep.
- After `M0566:25`, continuity enters a fully excluded scene and then an
  excluded block through `M0568:59`. Make no claim about what happens in that
  interval and do not use later context to reverse-engineer it.
- `M0568` resumes only at index 60 with a sudden unexplained boom and ground
  tremor. Its source, cause, and any prior positions or actions are unknown in
  the permitted projection.
- `M0569:1-4` are also excluded. Index 5 resumes after that gap. Do not add a
  connective explanation between `M0568:63` and `M0569:5`.

## Scene functions and reveal boundaries

### `SC_M0566_00_M0567_00`

- Sunao is asleep throughout. Leo briefly wonders whether the renewed clinging
  is deliberate, checks her face, and immediately confirms that she is still
  asleep. Her embrace and arm around his neck remain unconscious bad sleeping
  habits, not an intentional romantic or sexual advance.
- Leo's theory that Sunao is unconsciously arranging to kill him `legally` once
  she wakes is deliberately nonsensical self-preservation comedy. Do not make it
  a real plan, legal claim, or threat from Sunao.
- Leo peels her off, takes her by the ankle, and slides her across the floor
  like a bowling ball. She hits the stacked futons, they fall over her, and he
  calls it a strike. Preserve the bowling setup/payoff as broad slapstick.
- Sunao still does not wake. Leo finally recognizes how exhausted she must be,
  moves farther away again, and returns to sleep. Do not anticipate or describe
  the excluded material that follows.

### `SC_M0567_00_M0568_00`

- Fully excluded. No scene-function, speaker, action, or continuity summary is
  permitted. It requires no translation or downstream model artifact.

### `SC_M0568_00_M0569_00`

- Only indexes 60-63 are eligible. Leo reacts in alarm; an unexplained explosive
  noise and ground tremor surround the area; groggy Sunao begins to wake; Leo's
  narration ends on the realization that the situation is bad.
- Preserve the disturbance as a mystery. Do not identify an explosion's cause,
  assert who or what is present, or supply any action from indexes 1-59.

### `SC_M0569_00_M0570_00`

- Only indexes 5-9 are eligible. The unquoted opening asks what the preceding
  explosion was, but the filtered source does not safely establish a named
  speaker for that line. Preserve its unquoted form and do not invent a tag.
- The permitted narration says that the hut has ended up occupied/taken over,
  without identifying the responsible agent. Keep the passive ambiguity; do
  not name an occupier or explain how it happened.
- Leo concludes that sleeping outdoors is their only option, wistfully regards
  the distant city lights as warm, and the narration closes with the dry joke
  that human beings are remarkable because they can sleep even so.
- End on that outdoor-sleeping beat. Do not use the following scene to recap or
  reconstruct any excluded overnight material.

## Voice / speaker locks

- `レオ` = `Leo`: brisk first-person narration, mock alarm, absurd defensive
  theorizing, and self-satisfied slapstick commentary. His later resignation
  should sound dry rather than grand or literary.
- `素奈緒` = `Sunao`; Leo normally calls her `Konoe`: asleep and inarticulate
  through `M0566`, then only groggily waking at `M0568:62`. Do not add conscious
  intent, dialogue, embarrassment, or reaction that the permitted rows lack.
- Null-speaker rows remain unquoted. In particular, do not assign `M0569:5` to
  Sunao or Leo merely from register or surrounding inference.
- Preserve `Konoe` for Leo's narration/reference and `Sunao` in the speaker map.

## Hard renderings / ambiguity locks

- `また抱きついてきてやがる` (`M0566:3`) explicitly marks recurrence and
  Leo's exasperation: she is clinging to him again.
- `素でこんな事をしてくる` (`M0566:8`) means Sunao does this naturally/even
  while genuinely asleep. It does not mean `bare`, `sober`, or deliberate.
- `合法的に俺を殺すために無意識にやってる` (`M0566:12`) is an internally
  absurd theory. Keep `unconsciously` and `legally` in the joke without adding
  an explanation for why Leo imagines the killing would be lawful.
- `ひっぺがして` (`M0566:15`) is a forceful comic peel/pull-off. The next action
  specifically takes Sunao by the ankle; do not change the body part.
- `ボーリングの球` / `ストライク` (`M0566:17-20`) form one bowling gag. Keep
  the slide, collision with the futon stack, and last-beat `strike` payoff in
  order.
- `この状況下でまだ寝てる` (`M0566:22`) expresses amazement that she remains
  asleep after the slapstick; `よほど疲れてる` is Leo's inference that she must
  be extremely tired, not a diagnosis or injury claim.
- `謎の爆音と地響き` (`M0568:61`) is a mysterious explosive boom/noise plus a
  ground tremor. Do not promote the noise into a known event or cause.
- `や、やばい！` (`M0568:63`) is Leo's clipped `This is bad` realization. Do not
  specify the danger.
- `何よさっきの爆発？` (`M0569:5`) calls the sound an explosion from the line's
  immediate perspective, but remains unquoted and untagged in the projection.
  Preserve that distinction from the narrator's earlier `mysterious noise`.
- `結局、小屋も占拠されてしまった` (`M0569:6`) leaves the occupier unstated.
  `も` carries `even/also the hut`; do not invent the other occupied place.
- `野宿するしかあるまい` (`M0569:7`) is Leo's mock-stoic conclusion that they
  have no choice but to sleep outdoors.
- `街の灯は暖かそうだなァ` (`M0569:8`) is wistful and drawn out; keep the
  contrast between the warm-looking city lights and their outdoor situation.
- `それでも寝れるから人間は偉大だった` (`M0569:9`) is a dry closing
  punchline about humans being impressive because they can sleep anyway.

## Ruby / engine / deterministic expectations

- No ruby/furigana syntax, choice text, or engine control token appears in the
  34 permitted rows.
- Preserve `「...」` around spoken lines and leave narration unquoted. Source
  spacing is authored Japanese composition, not a license to add engine codes.
- Later translation JSONs must contain exactly `M0566:1-25`, `M0568:60-63`, and
  `M0569:5-9`. No translation JSON should be created for fully excluded `M0567`.
- All target values must be strings, all text must be CP932 encodable, and smart
  quotes, Unicode ellipses, and em/en dashes are forbidden.

## Items for later QC / arbitration attention

- `SC_M0566_00_M0567_00:12-22`: preserve the absurd legal-killing theory,
  bowling sequence, and final exhaustion inference without sexualizing Sunao's
  unconscious behavior.
- `SC_M0568_00_M0569_00:60-63`: retain the mystery and abrupt re-entry after the
  exclusion gap; never backfill its cause.
- `SC_M0569_00_M0570_00:5-6`: preserve the unquoted/untagged question and passive
  unidentified occupancy despite the missing preceding rows.
