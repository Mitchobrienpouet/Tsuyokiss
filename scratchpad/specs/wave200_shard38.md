# Wave-200 shard 38 continuity preflight

Scenes:
- `SC_M0510_00_M0520_00` — 32 permitted rows
- `SC_M0520_00_M0530_00` — 58 permitted rows
- `SC_M0530_00_M0540_00` — 29 permitted rows
- `SC_M0540_00_M0550_00` — 28 permitted rows

Total: 147 permitted rows.

## Safety / gates

- Canonical `content_exclusions.json`: no `SC_M` entry applies to these scenes.
- Configured historical overlay contains no `SC_M` entry and is marked consolidated; no additional row is removed here.
- `narrative_gates.json` declares no source mirrors and no repeated-choice groups.
- Translate displayed message text only. Preserve exact 1-based row indexes, Japanese dialogue brackets, ASCII punctuation conventions, and CP932-safe target text.

## Continuity locks

- The preceding scene ends with Principal Heizo ordering Leo to bring Sunao to the school gate the following Saturday at 10:00, both carrying swimsuits. Leo does not know the destination or plan yet.
- `M0510`: Sunao calls Leo during rainy-day exam study to make sure the notes/materials she lent him are working. She frames the follow-up as responsibility after lending them, not as a confession or overt romantic advance. Leo reads her as intensely conscientious.
- `M0520`: Kinu and Fukahire separately try to derail Leo's studying. Otome physically hauls Kinu off to study. Fukahire's `sexy-type book` and dating-site spam are broad comedy; do not add explicit content absent from the displayed source. Sunao's later phone check remains practical concern.
- `M0530`: final exams begin. Inori's mock-horror threat is completed by Tsuchinaga-san's blunt warning about losing summer vacation / expulsion. Leo's preparation pays off but is not perfect; Sunao explicitly says the notebook only analyzes tendencies and ordinary effort still decides the result.
- `M0540`: Kinu/Tonfa banter uses Tonfa's clipped `ne` register. Leo and Sunao confirm the Saturday appointment. Leo only knows Heizo demanded swimsuits and a 10:00 school-gate meeting; Sunao reasonably infers sea or pool. Do not reveal more.
- The following scene begins after all exams have ended, so shard 38 should leave the Saturday setup intact rather than resolving it early.

## Voice / terminology

- Leo: brisk, casual, self-aware narration and teasing.
- Sunao: serious, combative when teased, conscientious; warmth stays indirect.
- Kinu: loud, selfish comic sabotage without softening her shamelessness.
- Otome: clipped, commanding, physically formidable.
- Fukahire/Shinichi: grandiose loser-comedy register; retain `Fukahire` when used as nickname and `Shark` only where the source explicitly self-styles that way.
- Inori: composed mock-formality; do not make her girlish.
- Tsuchinaga-san: blunt adult/bird gag voice already established.
- Tonfa: preserve clipped Chinese-accent comedy lightly without unreadable caricature.

Hardest renderings to preserve function:
- `あそこまでして赤点でもとられたら、やるせない` = Sunao would feel it was all for nothing / couldn't stand it if Leo still failed after all her help.
- `第２第３のボク` = melodramatic `a second and third me` threat, immediately undercut by Fukahire's entrance.
- `ヤマ` in exam context = predicted/likely questions or the notebook's predictions, not a mountain.
- `今の口癖で人物立てるのはどうかと思うネ` = meta joke about defining a character by a verbal tic.
