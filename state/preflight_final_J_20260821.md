# Final J-lane continuity and content-safety preflight

Requested artifact date: 2026-08-21. Preflight run: 2026-08-22.

Status: **CLEAN -- FOUR PERMITTED PROJECTIONS READY; STOPPED BEFORE TRANSLATION**

Scenes:

- `SC_J0100_16_J0100_20`
- `SC_J0100_17_J0100_20`
- `SC_J0100_18_J0100_20`
- `SC_J0100_20_Z9999_99`

## Authority and stale zero-text records

The current authoritative `scratchpad/jp_dumps` files are text-bearing and
internally valid. They supersede the historical zero-text classifications in
`state/preflight_wave200_shard12.md` and
`state/wave200_shard13_zero_text_20260821.md`:

| Scene | Historical claim | Current raw rows | Classification |
|---|---:|---:|---|
| `SC_J0100_16_J0100_20` | 0 | 14 | permitted projection |
| `SC_J0100_17_J0100_20` | 0 | 9 | permitted projection |
| `SC_J0100_18_J0100_20` | 0 | 16 | permitted projection |
| `SC_J0100_20_Z9999_99` | 0 | 127 | permitted projection |

The current rows use verified block-0037 engine IDs, contiguous scene-local
indexes, nonempty source labels, and valid source hashes. No old zero-text
state was used to suppress or invent a row.

## Exclusions and narrative gates

The overlay-aware public loader merged:

- canonical `content_exclusions.json`;
- `state/content_exclusions_wave200_overlay.json`;
- `state/content_exclusions_wave500_overlay.json`.

No merged exclusion entry names any of the four scenes. There is no overlap,
gap, or fully excluded scene in this scope. `narrative_gates.json` declares no
source mirror and no repeated-choice group, including none for these scenes.

The three short scenes are nevertheless mutually exclusive answer branches
that converge on `SC_J0100_20_Z9999_99`. That structural relationship is a
continuity fact, not an identity gate: branch-specific lines must not be copied
across the alternatives.

## Exact counts and projections

| Scene | Raw | Permitted | Excluded | Projection | Exact indexes | Dialogue / narration |
|---|---:|---:|---:|---:|---|---:|
| `SC_J0100_16_J0100_20` | 14 | 14 | 0 | 14 | `1-14` | 13 / 1 |
| `SC_J0100_17_J0100_20` | 9 | 9 | 0 | 9 | `1-9` | 9 / 0 |
| `SC_J0100_18_J0100_20` | 16 | 16 | 0 | 16 | `1-16` | 15 / 1 |
| `SC_J0100_20_Z9999_99` | 127 | 127 | 0 | 127 | `1-127` | 103 / 24 |
| **Total** | **166** | **166** | **0** | **166** | four contiguous sets | **140 / 26** |

Permitted projections written:

- `scratchpad/model_sources/SC_J0100_16_J0100_20.json`
- `scratchpad/model_sources/SC_J0100_17_J0100_20.json`
- `scratchpad/model_sources/SC_J0100_18_J0100_20.json`
- `scratchpad/model_sources/SC_J0100_20_Z9999_99.json`

Because every row is permitted, each projection is byte-identical to its
current authoritative dump. No translation, QC, arbitration, or placeholder
artifact exists for these four scenes at this checkpoint.

## Content-safety result

All 166 rows passed fail-closed screening. The material contains broad comic
threats, a non-graphic mechanical explosion, slapstick fighting language, and
an interrupted comic attempt to undress. It contains no restricted explicit
sexual content and no directly dependent continuation requiring exclusion.
No new manifest finding is needed.

The translation must keep these beats brief and non-graphic. It must not add
injury detail, exposure, erotic framing, or a lethal outcome absent from the
source.

## Continuity and reveal boundaries

### `SC_J0100_16_J0100_20` -- incorrect Erika answer

- Continues directly from Leo's reaction test at `J0100_10:70`.
- Leo wrongly accuses the apparent Erika. The apparent Nagomi performs the
  exaggerated wrong-answer buzzer, then Honami reveals the disguise.
- Erika's silence becomes a wounded, imperious grudge after Leo realizes the
  mistake. End on Leo's `worst possible outcome` reaction; do not soften it
  into reconciliation.

### `SC_J0100_17_J0100_20` -- correct Nagomi answer

- Leo correctly identifies the apparent Nagomi because real Nagomi insults
  him but would not disparage food someone sincerely made.
- Preserve the distinction between calling Leo gross and insulting the meal.
- The fake's theatrical praise leads to Honami's reveal. Otome and Erika praise
  Leo; this is the successful branch only.

### `SC_J0100_18_J0100_20` -- incorrect Inori answer

- Leo wrongly accuses Inori. The apparent Nagomi again performs the
  wrong-answer routine before Honami reveals herself.
- Inori is the real Inori. Her quiet threat concerns Leo's future English
  grade; keep it composed and ominous, not openly vindictive.
- End on Leo's bad-outcome reaction. Do not import the praise from the correct
  branch.

### `SC_J0100_20_Z9999_99` -- common convergence and epilogue

- The group realizes the real Nagomi is missing. She is revealed as the captive
  held by Mecha Takane; do not imply that the branch-disguise Nagomi and the
  captive were simultaneously the same person.
- Poem delivers the hostage threat in sparse, shy, deadpan speech. Kinu triggers
  the small explosion immediately; Nagomi remains able to retort. The joke is
  failed teamwork, not serious injury.
- Serori's group cites the failure as proof of weak bonds. Both sides prepare
  for a broad comic fight.
- Speaker tag `声` at indexes `53-54` must remain generic (`Voice`). Do not name
  the speaker as Hinano until the explicit `雛乃` tag at index `57`.
- Hinano and Kaname interrupt and de-escalate the confrontation. Yoshimi then
  recognizes that her mother hired the investigators to check whether she was
  doing well while living alone.
- At `76-81`, preserve Yoshimi's public explanation and the brief colder
  undercurrent about her mother's motives. Leo notices that tonal shift; do not
  explain or reveal more than he perceives.
- The crossover and Ryuumeikan women move into lively social chatter. Shinichi's
  attempted disrobing is interrupted immediately by Otome and remains
  non-graphic slapstick.
- Index `107` shifts to Leo recounting the incident to classmates back on the
  school grounds. Preserve the abrupt frame change rather than inventing a
  travel bridge.
- The younger brother at `110` remains unnamed. The ending is a meta ensemble
  gag about side characters demanding screen time, capped by Iruka having been
  left behind and Leo's final observation.

## Names, voices, and terminology

Existing locks remain in force:

- `瀬芦里` -> `Serori`: hyperactive, athletic, catlike; use `nya` only where the
  source does.
- `帆波` -> `Honami`: glamorous, playful, theatrical, self-assured.
- `ぽえむ` -> `Poem`: quiet, shy, sparse, and deadpan even while threatening.
- `高嶺` -> `Takane`: refined, haughty, sharply corrective.
- `海` -> `Umi`: airy, casual, and cheerfully ruthless; preserve drawn-out
  cadence without overloading tildes.
- `要芽` -> `Kaname`: the adult Ice Lawyer, cool and authoritative.
- `巴` -> `Tomoe`: gentle and conflict-averse.
- `いるか` -> `Iruka`; `豆花` -> `Tonfa`; `真名` -> `Mana`; `洋平` ->
  `Yohei`; `紀子` -> `Noriko`.
- `雛乃` -> `Hinano`: small but commanding, with grandiose/archaic first-person
  diction. `ひなのん` is Serori's familiar nickname and must not overwrite the
  speaker-map name.
- `イガグリ` -> `Igaguri` for the speaker map. Older project files also contain
  `Burrhead`; use the current M-route romanized mapping here and flag any direct
  nickname occurrence separately rather than drifting silently.
- `ココナッツ` -> `Coconut`; `姫` -> `Princess`; `フカヒレ` -> `Fukahire`;
  `メカ高嶺` -> `Mecha Takane`.

Tsuyokiss voice locks remain unchanged: Leo brisk and self-deprecating, Kinu
brash, Subaru dry, Otome concise and martial, Erika polished and imperious,
Nagomi coldly polite, Inori composed, Yoshimi friendly with unrevealed
undercurrents, and Sunao fiery without generic slang.

## Difficult permitted lines for later translation/QC

- `J0100_16:3-7` and `J0100_18:4-8`: preserve the game-show wrong-answer buzzer,
  drumroll, and reveal as one escalating gag. The two branches may use closely
  parallel English but are not an identity gate.
- `J0100_17:3`: preserve Leo's behavioral distinction: Nagomi insults him, not
  food prepared with sincere effort.
- `J0100_17:6`: `シブい` praises Leo's perceptiveness/style in context; avoid the
  literal taste adjective `bitter`. `Sharp` is the leading reading.
- `J0100_20:20-22`: Poem threatens a small Mecha Takane blast and pain, not a
  graphic injury or certain death.
- `J0100_20:38`: Kinu's mock-polite justification is that she ended Nagomi's
  suspense quickly. Do not make the living Nagomi literally dead.
- `J0100_20:45`: `殺（と）らせて` uses a murderous kanji with the spoken reading
  `take`. Preserve competitive target-claiming with a dark undertone, but do
  not assert an actual killing.
- `J0100_20:53-57`: protect the `Voice` -> `Hinano` reveal boundary.
- `J0100_20:66-67`: retain Serori's `コカン` / `沽券` malapropism and Takane's
  immediate correction. The joke may mention the mistaken anatomical word,
  but must remain non-explicit wordplay.
- `J0100_20:79-81`: Yoshimi's chilling shift is a tonal cue only; do not expose
  hidden motives not stated here.
- `J0100_20:93-97`: Shinichi begins a comic strip attempt and is immediately
  stopped and knocked out. No nudity or exposure is stated.
- `J0100_20:110`: keep the younger-brother referent vague.
- `J0100_20:111`: Mana says the story still lacks a proper ending/punchline;
  keep her light Kansai flavor without caricature.
- `J0100_20:119`: preserve Sunao's recurring crest/anger catchphrase rather
  than flattening it to a generic complaint.

## Deterministic validation

PASS:

- duplicate-key rejection for all raw and projection JSON;
- exact raw and permitted index sets `1-14`, `1-9`, `1-16`, `1-127`;
- raw / projection byte identity for all four clean scenes;
- 166 unique nonempty engine IDs within their scenes;
- every `source_sha256` recomputes from the projected Japanese body;
- dialogue/narration kind and speaker-nullability agree;
- every projected Japanese body is CP932-encodable;
- zero excluded, missing, or unknown projected indexes;
- zero applicable source-mirror or repeated-choice gates.

## Blockers

NONE. The four clean projections are ready for a translation-stage owner using
the configured required model `gpt-5.6-sol`.
