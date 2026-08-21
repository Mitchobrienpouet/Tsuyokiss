# Critical full-route speed readthrough: wave B

## Verdict

**PASS after repair, independent QC, and arbitration closure.** All 7,191
permitted rows were read continuously in scene order. The original `0`
blocking, `3` major, and `8` minor findings have all been repaired, recertified,
arbitrated, and reread. This audit itself changed no translation, QC,
arbitration, source, manifest, pipeline, or configuration artifact.

## Scope and exact coverage

The authoritative B inventory contains 59 source scenes and 8,870 rows. The
active canonical manifest plus configured wave-500 overlay exclude 1,679 rows:
1,237 rows in 10 fully excluded scenes and 442 rows inside the 49 translated
scenes. The result is exactly 49 translation files and 7,191 permitted rows.

| Scene | Exact permitted indexes read | Rows |
|---|---:|---:|
| `SC_B0100_50_K0900_00` | `1-149` | 149 |
| `SC_B0110_00_K0900_00` | `1-59` | 59 |
| `SC_B0120_00_B0120_10` | `1-115` | 115 |
| `SC_B0120_20_K0900_00` | `1-11` | 11 |
| `SC_B0120_30_K0900_00` | `1-4` | 4 |
| `SC_B0130_00_K0900_00` | `1-141` | 141 |
| `SC_B0140_00_B0150_00` | `1-54` | 54 |
| `SC_B0150_00_B0160_00` | `1-15` | 15 |
| `SC_B0160_00_B0170_00` | `1-124` | 124 |
| `SC_B0170_10_B0180_00` | `1-3` | 3 |
| `SC_B0170_20_B0180_00` | `1-10` | 10 |
| `SC_B0170_30_B0180_00` | `1-5` | 5 |
| `SC_B0170_40_B0180_00` | `1-10` | 10 |
| `SC_B0180_00_B0190_00` | `1-10` | 10 |
| `SC_B0190_40_B0190_50` | `1-55` | 55 |
| `SC_B0190_50_B0200_00` | `1-63,69-83,95-142` | 126 |
| `SC_B0200_00_B0300_00` | `1-171` | 171 |
| `SC_B0300_00_B0310_00` | `1-43` | 43 |
| `SC_B0310_00_B0320_00` | `1-29` | 29 |
| `SC_B0320_00_B0330_00` | `1-58` | 58 |
| `SC_B0330_00_B0340_00` | `1-104` | 104 |
| `SC_B0340_00_B0350_00` | `1-345` | 345 |
| `SC_B0350_00_B0360_00` | `1-245` | 245 |
| `SC_B0360_00_B0370_00` | `1-194` | 194 |
| `SC_B0370_00_B0380_00` | `1-557` | 557 |
| `SC_B0380_00_B0390_00` | `1-568` | 568 |
| `SC_B0390_00_B0400_00` | `1-428,432-556,561-564,571-2217` | 2,204 |
| `SC_B0400_00_B0500_00` | `1-93,98-154,173-183,191-201,203-204,206-239,244-245,250-260,265-345,351-444` | 396 |
| `SC_B0500_00_B0600_00` | `1-38,59` | 39 |
| `SC_B0600_10_B0610_00` | `1-10,12-42` | 41 |
| `SC_B0610_00_B0620_00` | `1-2,4-27,32-44,46,50-71,92-97,120,124-135` | 81 |
| `SC_B0630_30_B0660_10` | `1-39` | 39 |
| `SC_B0660_10_B0660_20` | `1` | 1 |
| `SC_B0660_20_B0670_00` | `1-18,24-36,46-47,49-50,54-68` | 50 |
| `SC_B0680_00_B0690_00` | `1-2,4-15,22` | 15 |
| `SC_B0690_00_B0700_00` | `1-14,17-21,47-48,50-52,56-64` | 33 |
| `SC_B0700_00_B0720_00` | `1-31,49-65,69-232,248-280` | 245 |
| `SC_B0720_00_B0800_00` | `1-21,26-81,93-97,111-115` | 87 |
| `SC_B0820_00_B0850_00` | `27-48` | 22 |
| `SC_B0850_00_B0860_00` | `1-177,179-195,216-243` | 222 |
| `SC_B0870_00_B0880_00` | `1-25,29-31,33-34,39-40,42-47,49,51-52,54-57` | 45 |
| `SC_B0880_00_B0900_00` | `1-64,69-121,140-197` | 175 |
| `SC_B0900_10_B0900_30` | `1-11` | 11 |
| `SC_B0900_20_B0900_30` | `1-5` | 5 |
| `SC_B0900_30_B0910_00` | `1-7` | 7 |
| `SC_B0920_00_B0930_00` | `3-51` | 49 |
| `SC_B0930_00_B0940_00` | `1-56` | 56 |
| `SC_B0940_00_B0990_00` | `1-51,56-98` | 94 |
| `SC_B0990_00_Z9999_99` | `1-69` | 69 |
| **Total** |  | **7,191** |

The 10 fully excluded scenes remain artifact-free and are not translation or
readthrough debt: `SC_B0600_00_B0600_10` (350),
`SC_B0620_00_B0630_00` (4), `SC_B0630_10_B0630_20` (1),
`SC_B0630_20_B0660_00` (99), `SC_B0660_00_B0660_20` (1),
`SC_B0670_00_B0680_00` (265), `SC_B0800_00_B0810_00` (220),
`SC_B0810_00_B0820_00` (12), `SC_B0860_00_B0870_00` (41), and
`SC_B0910_00_B0920_00` (244). No excluded row was quoted, summarized, or
reconstructed during this audit.

Evidence reviewed: the complete B translation sequence; all B continuity
preflight specifications; `bible/characters.md`, `bible/glossary.md`, and
`bible/style.md`; the active exclusion manifests and narrative gates; all 49
accuracy records, all 49 literary records, and all 49 arbitration/no-op
records. No persistent SC_B model-source files are present in the current tree;
source-dependent trigger checks below used only exact manifest-permitted rows
through a fail-closed filtered read, never an excluded row.

## Major findings

### B-M01 — event-name drift across the central tournament arc

- **Scenes/indexes:** `SC_B0370_00_B0380_00:116,371,407,553`;
  `SC_B0380_00_B0390_00:1,27,126`;
  `SC_B0390_00_B0400_00:189,603`
- **Severity/category:** `major / continuity`
- **Current text:** the nine lines use `Combat Festival` or `Combat Festival
  tournament`, including `--The Combat Festival began.`, `Day two of the Combat
  Festival.`, and `Put the Combat Festival behind you.`
- **Source evidence:** the full event name is `体育武道祭` at every listed index
  except B0370:371, which says only `格闘トーナメント`. The immediately
  preceding setup correctly renders the same full name as `Sports Martial Arts
  Festival` at `SC_B0360_00_B0370_00:155,170,172`.
- **Project evidence:** the shard-12 preflight explicitly locks `Sports Martial
  Arts Festival` and `boxing tournament`. The event contains volleyball,
  debate, four-army scoring, and the Dragon Cup, so `Combat Festival` is not a
  harmless description of the whole event.
- **Diagnosis/fix direction:** one proper event acquires two English names in
  consecutive scenes, and B0370:371 adds the event label where the source says
  only the tournament. Standardize full `体育武道祭` occurrences to the locked
  `Sports Martial Arts Festival`; render B0370:371 as the tournament/fighting
  tournament without adding a second event name. Recheck all nine indexes as a
  systemic terminology repair.
- **Systemic/status:** `true / closed by repair and independent QC`

### B-M02 — localized speaker name regresses from `Burrhead` to `Igaguri`

- **Scenes/indexes:** `SC_B0370_00_B0380_00:370,372`;
  `SC_B0380_00_B0390_00:184`; `SC_B0390_00_B0400_00:215,742`
- **Severity/category:** `major / continuity`
- **Current text:** the three affected files set `speaker_map["イガグリ"]` to
  `Igaguri`.
- **Source/project evidence:** `イガグリ` is introduced as `Burrhead` at
  `SC_B0200_00_B0300_00:9`, that scene's map uses `Burrhead`, the shard-12
  preflight locks `イガグリ -> Burrhead`, and
  `SC_B0850_00_B0860_00:94,96,98` returns to `Burrhead`.
- **Diagnosis/fix direction:** an untranslated nickname appears in the speaker
  metadata for five permitted lines between two correctly localized blocks.
  Restore `Burrhead` in the three maps and validate the affected nameplates.
  Runtime display is not claimed, but the authored maps themselves diverge.
- **Systemic/status:** `true / closed by repair and independent QC`

### B-M03 — one spoken Leo line is authored as unquoted narration

- **Scene/index:** `SC_B0880_00_B0900_00:166`
- **Severity/category:** `major / other`
- **Current text:** `He was a pretty hot-blooded guy himself.`
- **Source evidence:** the permitted source row is dialogue spoken by `レオ`,
  kind `dialogue`: `「こいつも結構熱いヤツだな」`.
- **Project evidence:** `bible/style.md` requires `「...」` around spoken
  dialogue. This is the only permitted B row whose authoritative kind is
  dialogue but whose target lacks the dialogue wrapper.
- **Diagnosis/fix direction:** restore the Japanese corner-quote wrapper around
  the current faithful body text and revalidate textbox/backlog presentation.
- **Systemic/status:** `false / closed by repair and independent QC`

## Minor findings

### B-m01 — `Ryugu` proper-name lock breaks once

- **Scene/index:** `SC_B0180_00_B0190_00:3`
- **Severity/category:** `minor / continuity`
- **Current text:** `Sato had something to take care of, so I was cleaning up
  the Dragon Palace in her place.`
- **Source/project evidence:** source `竜宮`; glossary lock `Ryugu`; the same
  location is `Ryugu` at `SC_B0110_00_K0900_00:44` and
  `SC_B0130_00_K0900_00:3-4`.
- **Fix direction/status:** replace the one ad-hoc literalization with `Ryugu`;
  `closed by repair and independent QC`.

### B-m02 — `Ikajima` proper-name lock is translated ad hoc

- **Scene/index:** `SC_B0370_00_B0380_00:3`
- **Severity/category:** `minor / continuity`
- **Current text:** `「Our destination is Ika Island, the one you can see from
  here.」`
- **Source/project evidence:** source `烏賊島`; glossary lock `Ikajima`.
- **Fix direction/status:** use `Ikajima` without translating half of the
  proper name; `closed by repair and independent QC`.

### B-m03 — `Tetchan` callback is misspelled and once omitted

- **Scene/indexes:** `SC_B0400_00_B0500_00:339,341,345,351`
- **Severity/category:** `minor / continuity`
- **Current text:** indexes 339, 345, and 351 use `Tecchan`; index 341 omits the
  direct address entirely.
- **Source/project evidence:** all four source lines use `てっちゃん` or
  `鉄ちゃん`. The nickname is established consistently as `Tetchan` at
  `SC_B0100_50_K0900_00:70-72,78-79,83,85-87,123`.
- **Fix direction/status:** restore `Tetchan` at 341 and normalize the other
  three spellings; `closed by repair and independent QC`.

### B-m04 — `Mr. Tsuchinaga` speaker-map honorific drifts

- **Scenes/indexes:** `SC_B0390_00_B0400_00:197,220,223,848,1144`;
  `SC_B0400_00_B0500_00:256`
- **Severity/category:** `minor / continuity`
- **Current metadata:** `speaker_map["土永さん"] = "Tsuchinaga"`.
- **Project evidence:** the same source tag maps to `Mr. Tsuchinaga` in
  `SC_B0160_00_B0170_00`, `SC_B0930_00_B0940_00`, and
  `SC_B0990_00_Z9999_99`; the preflight voice lock uses `Mr. Tsuchinaga`.
- **Fix direction/status:** normalize the two affected speaker maps to the
  established nameplate; `closed by repair and independent QC`.

### B-m05 — generic third-year speaker capitalization drifts

- **Scene/indexes:** `SC_B0400_00_B0500_00:339,341,343,345,351-353,360`
- **Severity/category:** `minor / other`
- **Current metadata:** `speaker_map["３年女生徒"] = "Third-year Girl"`.
- **Project evidence:** the same source tag is `Third-Year Girl` in
  `SC_B0100_50_K0900_00` and the project otherwise capitalizes school-year
  compounds in generic speaker labels.
- **Fix direction/status:** normalize the map capitalization; `closed by repair
  and independent QC`.

### B-m06 — collective Kurogane reference is unidiomatic

- **Scene/index:** `SC_B0130_00_K0900_00:87`
- **Severity/category:** `minor / other`
- **Current text:** `Come to think of it, the Kurogane had apparently always
  led the vanguard in battle.`
- **Source evidence:** `そういえば戦において鉄は常に先鋒だったらしい。`
- **Project evidence:** the ending explicitly uses `The Kurogane clan` at
  `SC_B0990_00_Z9999_99:39`.
- **Fix direction/status:** supply the collective noun (`the Kurogane clan`)
  without changing the historical claim; `closed by repair and independent QC`.

### B-m07 — malformed object/subject order in Otome's confession

- **Scene/index:** `SC_B0390_00_B0400_00:1084`
- **Severity/category:** `minor / other`
- **Current text:** `「But for some reason... you alone, I did not want to call
  me boring.」`
- **Source evidence:** `でもな、何故かお前にだけは……つまらないと言われたくはなかった`.
- **Diagnosis/fix direction:** the intended meaning is recoverable but the
  English assigns `you` the wrong syntactic role. Preserve: she did not want
  Leo, of all people, to call her boring; `closed by repair and independent QC`.

### B-m08 — Yohei's comparison is left as translationese

- **Scene/index:** `SC_B0390_00_B0400_00:1231`
- **Severity/category:** `minor / other`
- **Current text:** `「Women hold things so long. Troublesome. With Date, we
  nearly fought, but now we speak easily.」`
- **Source evidence:** `女は長引くから難儀だよ。その点伊達など、一度揉めそうになったけどすぐにこう話せるから気楽だよ`.
- **Diagnosis/fix direction:** express that matters with women drag on, in
  contrast with Yohei and Date quickly speaking normally again; do not turn it
  into a new claim about women holding objects or necessarily holding grudges;
  `closed by repair and independent QC`.

## Narrative and route-wide checks

- **Hallucination and omission:** No added motive, relationship, action,
  location, chronology, or resolved ambiguity survived verification beyond the
  findings above. The childhood promise remains withheld until B0940; Otome's
  feelings progress through qualified admissions before the full declarations
  at B0390:2190/2203; the deliberate first kiss remains at B0390:2212.
- **Character integrity:** Leo's dry self-protection and later resolve, Otome's
  discipline/caretaking/romantic inexperience, Erika's polished dominance,
  Kinu's aggressive comedy, Noriko's halting sincerity, Yohei's pride, and
  Yoshimi's friendly undercurrents remain coherent across the route.
- **Agency and chronology:** the patrol, computer lesson, weekend rupture,
  Noriko/Yohei conflict, island training, tournament, confession, thunder
  history, post-confession domestic arc, breakup/reconciliation, second-term
  return, school hearing, childhood-promise recall, and coda occur in the
  correct order with their causal agents intact.
- **Branch integrity:** the four B0170 confession-result branches preserve four
  distinct selected winners. The B0900 return/keep-item alternatives remain
  distinct and both converge cleanly into B0900_30. No branch-only fact leaks
  into its sibling.
- **Exclusion boundaries:** every partially translated scene preserves its
  exact sparse set. No target line bridges, summarizes, or creates connective
  material for an excluded range.
- **Investigated non-findings:** B0850:237's odd `older sister and her kid
  brother` comparison is source-exact (`姉弟みたいだった`) and was deliberately
  retained by accuracy QC. B0390:1500's geographically wrong `Australian place`
  is also source-exact and part of Kinu's joke. Quoted crowd lines, wish strips,
  book/film titles, and the departure note account for narration rows that
  legitimately contain quotation marks. The documented `$L/$M` spans at
  B0340:328, B0370:478, B0400:312, and B0850:97 are correctly absent from
  displayed target body text.

## Deterministic validation

- **Cardinality/index joins:** `PASS` — 49 files, 7,191/7,191 exact permitted
  indexes; 442 excluded indexes absent from the translated scenes.
- **Fully excluded artifacts:** `PASS` — all 10 fully excluded B scenes have no
  translation, accuracy, literary, or arbitration artifact.
- **Source metadata:** `PASS` — all 7,191 permitted SHA-256 values recompute;
  all 7,191 engine IDs are unique and exactly match
  `B0029:<scene>:<zero-padded-index>`; scene/source labels match filenames.
  Translation JSON does not embed per-line hashes or IDs, so identity was
  validated by exact scene/index join against current authoritative metadata.
- **QC/arbitration inventory:** `PASS` — 49 accuracy records, 49 literary
  records, and 49 arbitration/no-op records, with no missing or extra B scene.
- **Speaker-map key coverage:** `PASS` — every permitted non-null source speaker
  has a nonempty map entry. The B-M02, B-m04, and B-m05 localized-value drifts
  are repaired and independently recertified.
- **Codec/typography:** `PASS` — every target string encodes as CP932; no smart
  quotes, Unicode ellipses, em/en dashes, carriage returns, or manual newlines;
  quote and parenthesis counts balance.
- **Dialogue wrappers:** `PASS` — B-M03's missing wrapper is restored and the
  full affected QC scope was revalidated.
- **Narrative gates:** `PASS` — the current gate manifest declares no source
  mirrors or repeated-choice groups.

## Story-image and runtime limitations

`docs/UI_STORY_IMAGE_LOCALIZATION_MANIFEST.md` was checked as the sole allowed
visual authority. Its ledger contains `titlechip.kg`, `CGChip.kg`, and
`EDChip.kg`, but it maps no asset to an SC_B scene/index or route variant.
Accordingly, no event-CG, sprite/expression, background, prop-text, or story
image claim can be proved or contradicted for these lines from the current
manifest. `EDChip.kg` includes route-ending labels in aggregate, but the ledger
does not identify the B route's exact label/trigger, so no scene-level inference
is made.

The manifest marks runtime QC pending. No live engine, textbox, nameplate,
backlog, wordwrap, image-trigger, build, or reinjection proof was available in
this audit. Static CP932 and metadata checks do not establish runtime fit or
visual correctness.

## Repair and closure addendum

All eleven findings were routed through narrow repair lanes. The original seven
repair scenes received a 4,051-row independent accuracy reread. The later
project-wide Samesuga/D repair reopened the two large tournament scenes inside
a 5,959-row B/D accuracy scope, adding 27 source-faithfulness corrections
across B and D. Independent literary QC then reread that full scope, preserved
every accuracy lock, and added 34 localized prose improvements.

Targeted arbitration found no new accuracy-versus-literary conflict and retained
all earlier scene decisions. The corrected B finding rows and their immediate
continuity blocks were reread in final form: event names, Burrhead, Ryugu,
Ikajima, Tetchan, Mr. Tsuchinaga, Third-Year Girl, the Kurogane clan, Otome's
confession syntax, Yohei's contrast, and the dialogue wrapper are stable.
Exact joins, hashes, engine IDs, file identities, speaker maps, wrappers,
exclusions, CP932, narrative gates, and public validation pass. No route-B
finding remains open.

Runtime/image debt remains explicitly open under the separate feasibility and
manifest audits; this static closure does not claim live textbox, backlog,
wordwrap, image-trigger, build, or reinjection proof.
