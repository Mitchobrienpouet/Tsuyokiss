# Wave 200 shard 11 continuity/safety preflight

Scenes: `SC_J0100_04_J0100_05`, `SC_J0100_05_J0100_06`, `SC_J0100_06_J0100_07`, `SC_J0100_07_J0100_08`.

Recovered source: `data.fpk` block 0037. Row counts: 61, 36, 84, 60 (241 total).

## Content-boundary result

A new fail-closed finding was banked before translation: `SC_J0100_04_J0100_05:11-37` contains adult flirtation and a sexualized proposition toward high-school student Nagomi. Those 27 rows are excluded from model work and builds. The permitted set is therefore 214 rows total: `J0100_04` indexes `1-10,38-61` (34 rows), plus all rows of the remaining three scenes (36, 84, 60). The excluded passage must not be translated, reconstructed, summarized, or bridged.

## Crossover/name locks

- `要芽` -> `Kaname` (Hiiragi Kaname), the famous `Ice Lawyer`: cool, teasing, authoritative.
- `いるか` -> `Iruka`: devoted, talkative assistant with dolphin jokes.
- Existing crossover locks from shard 10 remain: Serori, Tomoe, Takane, Honami, Poem.
- `メカ高嶺` -> `Mecha Takane`.
- Existing Tsuyokiss names/voices remain unchanged: Erika, Otome, Leo, Kinu, Nagomi, Shinichi, Subaru, Inori, Yoshimi, Tonfa, Yohei, Sunao, Noriko.

## Continuity

- `J0100_04`: Kaname arrives to meet Erika. Preserve only the permitted setup before the excluded Nagomi passage and resume at Iruka asking Kaname to summon Erika; do not bridge the omitted interaction. The council later mistakes the lawyer visit for evidence Erika committed a crime.
- `J0100_05`: Erika meets Kaname and Iruka; a wrong phone digit explains the missed call. Kaname and Erika leave to discuss company/family business. Yoshimi later senses someone watching her.
- `J0100_06`: Yoshimi reports the watcher. Leo, Kinu, Subaru, and Shinichi tail her; Shinichi eventually confesses he was following her and gets punished by the group.
- `J0100_07`: Erika and Otome sense another watcher. Otome captures a strange `Mecha Takane`, which speaks and self-destructs; the scene ends on Leo shouting for Otome.

Preserve exact permitted indexes, Japanese corner quotes, ASCII punctuation, and CP932-clean text. No manual engine commands.
