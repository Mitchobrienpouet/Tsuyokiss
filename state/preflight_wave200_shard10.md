# Wave 200 shard 10 continuity/safety preflight

Scenes: `SC_J0000_00_J0100_01`, `SC_J0100_01_J0100_02`, `SC_J0100_02_J0100_03`, `SC_J0100_03_J0100_04`.

## Content-boundary result

The recovered Japanese source from `data.fpk` block 0037 contains 1, 109, 45, and 76 rows respectively. Neither the canonical `content_exclusions.json` nor the active wave-200 overlay declares an excluded range for these four J scenes. All 231 source rows are therefore eligible for model work. No omitted range is inferred or bridged.

## Crossover/name locks

- `瀬芦里` -> `Serori` (Hiiragi Serori): hyperactive, catlike, athletic; preserve occasional literal `nya` verbal tic without adding it where absent.
- `巴` -> `Tomoe` (Hiiragi Tomoe): gentle, hesitant, frequent `Auu...` reactions.
- `高嶺` -> `Takane` (Hiiragi Takane): haughty, refined, sharp-tongued.
- `帆波` -> `Honami` (Inugami Honami): glamorous actress, playful and self-assured.
- `ぽえむ` -> `Poem` (Inugami Poem): quiet, shy, sparse speech.
- Existing Tsuyokiss locks remain unchanged: `乙女` Otome, `レオ` Leo, `エリカ` Erika, `きぬ` Kinu, `なごみ` Nagomi, `新一` Shinichi, `スバル` Subaru, `祈` Inori, `良美` Yoshimi.
- Preserve the crossover title `Ane, Chanto Shiyou yo!` as a romanized proper title rather than inventing an English commercial title.

## Continuity

- `J0000` is the crossover title card.
- `J0100_01` explicitly warns that the story assumes familiarity with the `Ane, Chanto Shiyou yo!` series, then follows Serori and Tomoe arriving at Ryuumeikan. Serori infiltrates the school for a paid investigation and clashes with Otome before escaping.
- `J0100_02` follows Takane, Honami, and Poem eating at Dobuzaka stalls. Shinichi and Subaru recognize Honami as an actress; Shinichi embarrasses himself asking for an autograph.
- `J0100_03` returns to the Ryuumeikan student-council room the next day. Otome reports the intruder, the group digresses into banter, and the scene closes on Shinichi being denied tea after noticing Yoshimi's attention to Leo.
- Do not import route-romance resolutions into this crossover material beyond what the source states.

## Engine/profile

Preserve exact source indexes, Japanese corner quotes around dialogue, ASCII `...` and `--`, straight apostrophes, and CP932-clean text. No manual engine commands or invented line breaks.
