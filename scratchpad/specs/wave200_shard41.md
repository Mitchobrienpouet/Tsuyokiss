# Wave-200 shard 41 continuity preflight

Scenes and permitted rows after fail-closed projection:
- `SC_M0558_00_M0559_00` - 43 permitted / 0 excluded
- `SC_M0559_00_M0560_00` - 170 permitted / 0 excluded
- `SC_M0560_00_M0561_00` - 85 permitted / 0 excluded
- `SC_M0561_00_M0562_00` - 79 permitted / 0 excluded

Total: 377 permitted rows; 0 excluded rows.

## Safety / gates

- The canonical `content_exclusions.json` and both configured overlays declare no exclusion for these four scenes. The active wave-500 overlay affects only earlier adjacent scenes `M0554` and `M0556`; no omitted material may be reconstructed or imported from them.
- The filtered `scratchpad/model_sources/` projections contain all 377 assigned rows. Preserve their original indexes exactly.
- `narrative_gates.json` declares no source mirrors or repeated-choice groups.
- The assigned projections contain survival comedy, mild romantic embarrassment, a swimsuit-clad mixed hot-spring scene, and overheating. Nothing crosses the current fail-closed boundary. If a later pass discovers newly restricted content, stop that scene and report the exact indexes rather than translating the affected rows.

## Immediate continuity

- Leo and Sunao (`素奈緒`, normally addressed by Leo as `Konoe`) have been stranded overnight on Ikajima by Principal Heizo's absurd matchmaking scheme. They spent the day drawing territorial borders and refusing one another's help.
- Leo opened Heizo's emergency scroll. It explicitly explains which island foods are edible and how to gather and prepare them. Sunao does not know this yet because she repeatedly ran off before Leo could finish speaking.
- Sunao's immediately preceding mountain-foraging attempt failed. She does not know how to identify mushrooms and rejected the idea of testing one on Leo as too cruel.
- The following adjacent scene begins after Sunao has passed out from staying in the hot spring too long: she wakes on the beach and learns that Leo carried her there while she was still in her swimsuit. Do not anticipate that rescue in this shard.

## Scene functions and reveal boundaries

### `SC_M0558_00_M0559_00`

- Sunao returns empty-handed. Leo offers the food he gathered, but an accidental jab at her competence makes her refuse it before he can explain the scroll.
- Sunao tries fishing with crumbs from her peanut-butter bread, catches nothing, then role-plays a veteran ama diver with a no-good husband. Preserve the theatrical "setting" and the RPG-like attack/result diagrams as overt meta comedy.
- The scene ends with Sunao still pursuing fish by hand; do not grant her a catch.

### `SC_M0559_00_M0560_00`

- At dusk Leo has gathered food by following the scroll. Sunao's pride makes her keep trying alone, briefly consider eating a cicada, and return empty-handed.
- The campfire meal moves from comic refusal to a sincere childhood-friend beat. Sunao admits a childhood incident made fish hard for her to eat, tends Leo's small hand injuries, and acknowledges that they could have enjoyed the day by cooperating.
- Preserve the middle-school bread callback without inventing details not supplied here.
- Sunao's apology and praise create a deliberately near-romantic beat. Her red face and later complaint are intentionally suggestive but not explicit. Leo breaks the moment by revealing the scroll and explaining that he followed it all day.
- Sunao's final `その気にさせといて` complaint must remain ambiguous: Leo repeatedly gets her emotionally invested/worked up and then ruins the moment. Do not state a confession or romantic intent the Japanese has not made explicit.

### `SC_M0560_00_M0561_00`

- Sunao sees a person-sized figure near the mountain entrance. No person is found, but a trampled path suggests something may have passed through.
- Preserve the uncertainty. Do not identify the figure as a criminal, ghost, animal, Heizo, or any known character. Leo's criminal hypothesis is only one possibility and he immediately calls it overthinking.
- Leo's 221 increasingly absurd theories keep Sunao as the running cause; the hug theory is teasing, not a factual claim.
- The evidence leads them to agree to stay together until pickup. Sunao responds to Leo's fake alarm by assuming a fighting stance rather than squealing, reinforcing her practical courage.
- The cold night air motivates the move to the hot spring.

### `SC_M0561_00_M0562_00`

- Sunao proposes entering the hot spring together because they have agreed to stay together. Leo's shock is punctured immediately: both keep their swimsuits on.
- Hair-down Sunao looks unfamiliar to Leo, but his observation stays brief and non-explicit. Preserve her mild embarrassment and water-pistol deflection.
- Their shared-birthday memory establishes how they first began talking in middle school: Sunao's horoscope described people born that day as meticulous and tidy, which made Leo's sloppiness annoy her.
- A playful water-pistol exchange becomes an endurance contest over who can remain in the hot spring longer. Neither backs down. Sunao overheats and becomes unresponsive; the scene ends with Leo recognizing the danger and calling to her.
- Do not narrate undressing, nudity, sexual contact, a rescue, or recovery. Those events are absent from this scene.

## Voice / speaker locks

- `レオ` = `Leo`: brisk, teasing, self-satisfied straight man whose mock gallantry often becomes the punchline. His narration can admit private nerves without making him cowardly.
- `素奈緒` = `Sunao`; Leo normally calls her `Konoe`: proud, quick-tempered, theatrical, competitive, and capable. Her repeated refusals are stubborn childhood-friend pride, not hatred.
- Preserve `「...」` around every spoken line. Narration remains unquoted.
- Keep `Ikajima` and `Ryuumeikan Academy` locked. The scroll remains `Survival Knowledge for Ikajima` when referred to by title/context.

## Hard renderings / ambiguity locks

- `カチン！` (`M0558:9`) is an audible/comic flash of irritation, not a literal clicking object.
- `海女` (`M0558:32,34`) = an `ama diver` / traditional woman diver. Keep the forty-year-old-veteran role-play and `ろくでなしのダンナ` as a `no-good husband`.
- `近衛攻撃フェイズ` / `戦闘結果` (`M0558:36,38`) are game-battle captions. Preserve the fish/Konoe directional diagram and `MISS!` outcome in CP932-safe text.
- `セミとムカデは食える` (`M0559:21`) means cicadas and centipedes are edible according to the scroll; Leo is not ordering Sunao to eat them.
- `アブラゼミはアブラのってて` (`M0559:61`) plays on the oily cicada's name and food being fatty/oily. Preserve the food-pun function without claiming she actually ate it; she immediately admits the boast is a lie.
- `相変わらず小気味いい` (`M0559:119`) praises Sunao's brisk efficiency in wrapping the gauze, not her physical appearance.
- `柳の幽霊` (`M0560:35`) invokes mistaking a willow/tree for a ghostly person; preserve it as Leo's teasing hypothesis, not real supernatural evidence.
- `抱きつく口実` (`M0560:44`) = an excuse to cling/hug Leo. It remains a hypothetical joke.
- `目が記号になってる` (`M0561:68`) is visual/meta comedy about Sunao's overheated expression; do not replace it with a medical diagnosis.
- `男と２人きりの無人島で気絶していいのか` (`M0561:72`) is Leo trying to provoke Sunao's usual retort. Keep the implication light and source-bounded; her failure to respond is what proves she is seriously overheated.

## Deterministic expectations

- Each translation JSON must contain exactly the indexes in its filtered model source: 43, 170, 85, and 79 lines respectively.
- `file` must match the scene ID. `speaker_map` must map every non-null Japanese speaker used by that scene and no speaker identity may be invented.
- All translated values must be strings, dialogue lines must retain Japanese corner brackets, narration must not acquire them, forbidden smart typography must be absent, and every target string must be CP932 encodable.
