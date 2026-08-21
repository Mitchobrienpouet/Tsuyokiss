# Wave-200 shard 40 continuity preflight

Scenes and permitted rows after fail-closed projection:
- `SC_M0554_00_M0555_00` — 7 permitted / 23 excluded
- `SC_M0555_00_M0556_00` — 34 permitted / 0 excluded
- `SC_M0556_00_M0557_00` — 79 permitted / 20 excluded
- `SC_M0557_00_M0558_00` — 17 permitted / 0 excluded

Total: 137 permitted rows; 43 excluded rows remain absent from all model stages and builds.

## Safety / gates

- Active `state/content_exclusions_wave500_overlay.json` excludes `M0554:2-24` and `M0556:1-20`, including dependent setup/bridge lines so filtered scenes resume at self-contained beats.
- Do not reconstruct, summarize, infer, or bridge the excluded Japanese.
- `narrative_gates.json` declares no source mirrors or repeated-choice groups.
- Preserve original row indexes; gaps caused by exclusions are intentional and are not translation debt.

## Continuity

- `M0554` permitted material only establishes the tropical-island mood, then resumes after the omitted section by confirming Sunao can swim because she attended swimming school and noticing Heizo has disappeared. The omitted middle is not to be described.
- `M0555`: Heizo starts the cruiser while Leo and Sunao are still ashore, says he will contact their parents, and leaves them on Ikajima until the following evening because a movie convinced him isolation produces romance. The scene treats his matchmaking logic as absurd; Leo and Sunao blame him/each other rather than accepting the premise.
- The film title/reference is a deliberate parody. Preserve it as an obviously spoofed movie title rather than silently replacing it with a real title.
- `M0556` resumes after the excluded opening argument. Leo and Sunao draw childish territorial borders in the sand, escalate to claiming the sea/mountain/pier/water source, then finally turn to the practical problem of obtaining food before dark.
- Preserve the `素直 / Sunao` name pun at rows 78-79: Leo calls her `not very sunao`, and she immediately bans the name joke.
- Leo opens Heizo's emergency scroll because their current survival problem already counts as trouble. The scroll is a practical `Survival Knowledge for Ikajima` guide covering edible/inedible foods and gathering methods; this is the first reveal of its contents.
- `M0557`: Sunao fantasizes about returning with mountain food and making Leo apologize, then admits she has no survival knowledge and cannot identify mushrooms. She considers testing one on Leo, then rejects doing something that cruel.

## Voice / terminology

- Leo/Sunao: childhood-friend bickering at maximum comic pettiness; anger is real but the territory war is deliberately childish.
- Heizo: deadpan, impossible matchmaker-adventurer; his movie logic should sound absurd rather than sinister.
- Keep `Ikajima`, `Ryuumeikan Academy`, and other glossary locks unchanged.
- `恩を仇で返す` = repay kindness with betrayal / return a favor with harm.
- `ソリがあわない` = not get along / be incompatible.
- `強欲` / `貪欲` are reciprocal greed insults; preserve the mirrored jab without forcing unnatural thesaurus English.
- `椰子（？）の実` = fruit/nut from a palm(?) tree; preserve the source's uncertainty marker.

## Deterministic expectations

- Translation files must contain exactly the permitted indexes from the filtered model sources, with excluded gaps absent.
- Japanese dialogue brackets and ASCII punctuation conventions must remain intact.
- All target strings must be CP932 encodable.
