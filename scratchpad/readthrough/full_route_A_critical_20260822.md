# Critical full-route speed readthrough: A route

Date: 2026-08-22  
Stage: post-QC critical readthrough only  
Verdict: **FAIL — 2 blocking and 2 major findings remain open**  
Translation changes: NONE

## Scope and evidence

I read all 269 extant SC_A translation files continuously in scene order, covering all
6,078 permitted rows. I compared suspicious passages against the authoritative
source metadata through the exclusion-aware project loader, and reviewed the
project bible, glossary, style and character files, the 68 A-route continuity
specifications, narrative and choice gates, all existing A accuracy and literary
QC reports, and the A arbitration records.

The authoritative A inventory contains 270 source scenes and 6,183 raw rows.
Configured exclusions remove 105 rows, leaving 6,078 permitted rows. The one
fully excluded, zero-debt scene is SC_A0400_20_A0400_30:1-10; it has no
translation artifact and its text was not inspected or reconstructed.

This pass did not edit translations, QC, arbitration, configuration, sources,
pipeline state, or Git.

## Deterministic validation

| Gate | Result |
| --- | --- |
| Translation files | PASS: 269 |
| Permitted rows | PASS: 6,078 / 6,078 |
| Raw rows / excluded rows | 6,183 / 105 |
| Exact permitted index joins | PASS: 0 missing, extra, or excluded keys |
| Engine IDs | PASS: 6,078 present and 6,078 unique |
| Source SHA-256 metadata | PASS: 0 recomputation mismatches |
| Translation JSON fields and duplicate keys | PASS: 0 errors |
| Speaker-map coverage | PASS: 0 source speakers missing |
| Project per-scene validator | PASS: 269 / 269 |
| CP932 encoding | PASS: 0 failures |
| Forbidden Unicode typography | PASS: 0 failures |
| Japanese script in English targets | PASS: 0 rows |
| Placeholder scan | PASS: no TODO, TBD, FIXME, untranslated, or replacement-character markers |
| Dialogue-wrapper audit | 11 candidates; 10 manually dismissed as intentional annotation/thought handling, 1 major defect remains |

Deterministic validity does not override the open narrative, naming, and wrapper
findings below.

## Blocking findings

### A-RT-001 — Shinichi surname has three incompatible renderings

- scene: SC_A0100_16_A0100_18; SC_A0100_32_A0100_40;
  SC_A0110_60_A0110_70; SC_A0180_90_A0190_00;
  SC_A0360_40_A0360_50; SC_A0360_70_A0360_80;
  SC_A0370_60_A0370_70; SC_A0450_20_A0450_30
- indexes: [2]; [35]; [2]; [3]; [35]; [10]; [12]; [4, 7]
- severity: blocking
- category: lore / continuity
- current_text: The A route alternates among “Samesuga,” “Samejima,” and
  “Samehyou” for the same surname.
- source_evidence: SC_A0100_16_A0100_18:2 explicitly introduces
  鮫氷新一（さめすが　しんいち）. SC_A0180_90_A0190_00:3 again supplies
  鮫氷（さめすが）. The other listed rows use the same kanji.
- project_evidence: The current A intro uses Samesuga, while existing A accuracy
  reports at A0360_40:35 and A0370_60:12 accepted Samejima; later C/D specs and
  QC also describe Samejima as established. The project evidence therefore
  conflicts with the explicit source ruby and with itself.
- visual_evidence: NONE
- diagnosis: A recurring character surname is not stable. At least two of the
  three current forms are necessarily wrong, and the inconsistency reaches two
  self-introductions and multiple direct addresses.
- fix_direction: Reopen the naming authority in a targeted accuracy/arbitration
  lane. The explicit ruby supports Samesuga unless a documented localization
  authority deliberately overrides it. Whichever canonical form is adopted,
  normalize all nine A-route occurrences and the corresponding lock; preserve
  “Shinichi,” “Fukahire,” and “Shark.”
- systemic: true
- status: open

### A-RT-002 — Leo reverses the rescue roles

- scene: SC_A0440_60_A0440_70
- indexes: [5]
- severity: blocking
- category: meaning
- current_text: 「Actually, maybe I saved the delinquents from a pickup artist?」
- source_evidence: 「あ、いやナンパ男からヤンキーを助けた、かな？」
  Leo hesitantly reframes the earlier event as saving the singular rough girl
  (Nagomi) from the pickup men.
- project_evidence: The surrounding route continuity establishes Nagomi as the
  person Leo helped and keeps Leo’s self-correction tentative. Existing scene
  QC did not identify the reversal.
- visual_evidence: NONE
- diagnosis: The English changes both sides of the action: it makes plural
  delinquents the rescued group and a singular pickup artist the threat.
- fix_direction: Restore Leo as saving a delinquent/rough girl from pickup
  artists, while retaining his hesitant “maybe” and without newly naming Nagomi
  if the line itself does not.
- systemic: false
- status: open

## Major findings

### A-RT-003 — Tonfa is mislabeled as Touka in three speaker maps

- scene: SC_A0100_32_A0100_40; SC_A0120_60_A0120_70;
  SC_A0150_00_A0150_10
- indexes: [17]; [14]; [15]
- severity: major
- category: lore / other
- current_text: Each scene maps 豆花 to “Touka,” so the engine name label is
  wrong on the listed spoken rows.
- source_evidence: SC_A0100_22_A0100_24:26 explicitly gives
  豆花（トンファー）. The source speaker identity at all three affected rows is
  豆花.
- project_evidence: Seven other A speaker maps use “Tonfa,” and the nearby
  A0120_20 continuity spec locks 豆花 to Tonfa. Three older local specs preserve
  the contradictory Touka form.
- visual_evidence: NONE
- diagnosis: The displayed speaker name changes for the same classmate within
  one route despite an explicit ruby.
- fix_direction: Change only the three speaker-map values to Tonfa and reconcile
  the stale local locks; retain her lightly clipped, non-caricatured voice.
- systemic: true
- status: open

### A-RT-004 — Spoken dialogue is emitted as narration

- scene: SC_A0190_20_A0190_30
- indexes: [33]
- severity: major
- category: other
- current_text: They could tell me not to think about it, but...
- source_evidence: The source row is kind=dialogue, speaker=レオ, and text
  「意識するなって言われても」.
- project_evidence: Project style requires Japanese corner brackets around
  spoken dialogue. Existing accuracy and literary QC accepted the unwrapped
  line.
- visual_evidence: NONE
- diagnosis: Dropping the dialogue wrapper changes an aloud Leo line into
  narrator text in the engine presentation.
- fix_direction: Restore the corner-quoted dialogue wrapper while preserving the
  incomplete, uneasy thought and exact meaning.
- systemic: false
- status: open

## Minor findings

### A-RT-005 — Burrhead / Igaguri label drift

- scene: SC_A0160_20_A0160_30
- indexes: [1, 3]
- severity: minor
- category: continuity / other
- current_text: The speaker map labels イガグリ as “Igaguri.”
- source_evidence: Both rows are spoken by イガグリ.
- project_evidence: Four other A speaker maps use “Burrhead,” and
  qc/accuracy/SC_A0120_10_A0120_20.md explicitly corrected this label from
  Igaguri to Burrhead. The local A0160 spec instead records Igaguri pending
  context.
- visual_evidence: NONE
- diagnosis: The same recurring classmate receives two English name labels
  within the route.
- fix_direction: Resolve the house-style lock and use one A-route label
  consistently; current A precedent favors Burrhead. Do not alter the rustic
  cadence.
- systemic: true
- status: open

### A-RT-006 — Heizo romanization drift

- scene: SC_A0100_18_A0100_20
- indexes: [42, 48]
- severity: minor
- category: lore / continuity
- current_text: “Heizou Tachibana”; speaker map 平蔵 -> Heizou.
- source_evidence: Index 48 gives 橘平蔵（たちばな　へいぞう）.
- project_evidence: Three other A speaker maps and the project’s continuing
  route locks use Heizo.
- visual_evidence: NONE
- diagnosis: One early scene alone retains a different long-vowel
  romanization.
- fix_direction: Normalize the two target occurrences and speaker-map value to
  Heizo, preserving the full-name order already used.
- systemic: false
- status: open

### A-RT-007 — Ellie nickname typo

- scene: SC_A0410_70_A0410_80
- indexes: [28]
- severity: minor
- category: lore / character
- current_text: 「...you’re harassing me much more than Leo is, Elly.」
- source_evidence: The source nickname is エリー.
- project_evidence: The A-route specs and all other A occurrences lock Yoshimi’s
  nickname for Erika as Ellie.
- visual_evidence: NONE
- diagnosis: A single typo breaks a stable intimate nickname.
- fix_direction: Change Elly to Ellie without altering Yoshimi’s complaint.
- systemic: false
- status: open

### A-RT-008 — Miss Inori address lock drifts to Ms. Inori

- scene: SC_A0120_70_A0120_80; SC_A0120_80_A0120_85;
  SC_A0150_00_A0150_10; SC_A0230_00_A0230_10;
  SC_A0250_10_A0250_20; SC_A0460_40_A0460_50
- indexes: [3, 11, 22, 31]; [2]; [17]; [5]; [3, 14]; [2]
- severity: minor
- category: character / continuity
- current_text: Ten narration lines use “Ms. Inori.”
- source_evidence: Each line refers to 祈先生.
- project_evidence: The A-route preflight locks 祈先生 as Miss Inori, and multiple
  existing A accuracy reports explicitly normalized other occurrences to that
  form.
- visual_evidence: NONE
- diagnosis: The same familiar student-to-teacher address alternates between
  Miss and Ms. within one route.
- fix_direction: Normalize these ten occurrences to Miss Inori; do not change
  bare Inori speaker labels.
- systemic: true
- status: open

### A-RT-009 — Mr. Tsuchinaga loses his established title in one speaker map

- scene: SC_A0120_70_A0120_80
- indexes: [9, 23, 33]
- severity: minor
- category: character / other
- current_text: The speaker map renders 土永さん as “Tsuchinaga.”
- source_evidence: The three rows are spoken by 土永さん.
- project_evidence: Thirteen other A speaker maps use Mr. Tsuchinaga, and route
  prose/QC treats that as his stable displayed name.
- visual_evidence: NONE
- diagnosis: Only this scene drops the established title from his engine name
  label.
- fix_direction: Restore Mr. Tsuchinaga in the speaker map without changing his
  mock-grandiose dialogue.
- systemic: false
- status: open

### A-RT-010 — Otome toothbrush wordplay is grammatically broken

- scene: SC_A0380_40_A0380_50
- indexes: [6]
- severity: minor
- category: other
- current_text: 「Mistaking an 'Otome's' toothbrush for your own and using it...
  You will make her hate you.」
- source_evidence: 「お前、“乙女”の歯ブラシを間違えて
  使ってしまうなんてな。嫌われるぞ」. The quotation marks make a wordplay
  beat between 乙女 as “maiden” and Otome’s name.
- project_evidence: Existing scene QC correctly notes the name/wordplay but
  leaves the malformed English article and possessive.
- visual_evidence: NONE
- diagnosis: “an 'Otome's'” is not grammatical English and obscures rather than
  carries the pun.
- fix_direction: Recast the phrase so “a maiden’s” and “Otome’s” can both land
  grammatically, while retaining her warning and not expanding the joke.
- systemic: false
- status: open

## Continuous-route checks

- **Hallucinations and omissions:** No additional unsupported event, invented
  motive, material omission, or unexplained source expansion survived source
  verification.
- **Voice and characterization:** Leo’s dry straight-man narration, Otome’s
  formal bluntness, Erika’s polished dominance, Kinu’s loud physical comedy,
  Subaru’s laconic pragmatism, Shinichi’s shameless bravado, Nagomi’s clipped
  guardedness, Yoshimi’s gentle register, Inori’s languor, and Heizo’s booming
  authority remain distinguishable. The localized naming/address drift above is
  the only surviving systemic voice-label issue.
- **Reveal timing:** PASS. The opening flash-forward keeps Otome as
  “Upperclassman”; Erika is named at the planned school introduction; Sunao’s
  early “Tsushi...” remains interrupted; the Otome cousin connection is not
  exposed before its reveal; Nagomi’s temporary status and Sunao’s late full-name
  coda remain in order.
- **Chronology and locations:** PASS. School days, council work, route-choice
  branches, festival planning, the island sequence, Nagomi’s reentry, and the
  closing coda remain ordered without a chronology-breaking tense or impossible
  location jump.
- **Branch convergence:** PASS. The A0100_06/07/08 openings converge at A0100_10;
  the A0170_70 acceptance and A0170_80 refusal loop retain their distinct logic;
  the A0200_80/90 cleaning variants converge at A0210; the A0250_70/80/90 wish
  choices converge at A0360. No branch-only fact leaks into a sibling path.
- **Scene boundaries:** PASS except A-RT-004. Configured sparse gaps remain
  opaque and are not bridged. The fully excluded A0400_20 scene remains absent.
- **Existing arbitration:** Five non-NONE A decisions were reviewed and remain
  closed: A0100_14:35 tongue twister, A0100_22:76 Princess title,
  A0160_10:68 Laurencin, A0250_90:2 Your Perviness, and
  A0390_70:17 Emmanuelle Shot.

## Exclusion boundaries

The following configured exclusions were honored without reconstruction:

| Scene | Excluded indexes |
| --- | --- |
| SC_A0160_80_A0160_90 | 24 |
| SC_A0240_10_A0240_20 | 1-24 |
| SC_A0240_30_A0240_40 | 27-35 |
| SC_A0360_00_A0360_10 | 8-14 |
| SC_A0360_10_A0360_20 | 9-18 |
| SC_A0370_10_A0370_20 | 10-15 |
| SC_A0400_20_A0400_30 | 1-10, fully excluded |
| SC_A0400_30_A0400_40 | 5-8 |
| SC_A0430_50_A0430_60 | 2-24 |
| SC_A0430_80_A0430_90 | 4-14 |

## Story-image and runtime limitations

docs/UI_STORY_IMAGE_LOCALIZATION_MANIFEST.md inventories titlechip.kg,
CGChip.kg, and EDChip.kg but provides no scene-linked A-route story-image
evidence. Therefore no A-route visual contradiction could be tested and this
report makes no story-image proof claim.

The manifest’s static source/layout checks are not live-engine evidence, and its
runtime status remains pending. No in-engine textbox, backlog, nameplate,
choice-screen, transition, or asset capture was available. Runtime wrapping,
clipping, font fallback, nameplate presentation, and actual story-image
synchronization therefore remain unresolved limitations even though static
wrappers and CP932 pass.

## Correction routing and pass condition

Route A does not pass the critical-readthrough gate while A-RT-001 through
A-RT-004 remain open. Route A-RT-001 and A-RT-002 through accuracy plus targeted
arbitration; A-RT-003 through naming/metadata accuracy and lock reconciliation;
A-RT-004 through engine-aware accuracy; and the minor items through targeted
literary or metadata cleanup as appropriate. After corrections, rerun
deterministic gates and reread the affected blocks. No broad rewrite is
recommended.

## Exact translated-scene coverage

Every listed index was read continuously. Counts sum to 6,078.

| Scene | Permitted indexes read | Count |
| --- | --- | --- |
| `SC_A0100_01_A0100_02` | `1-17` | 17 |
| `SC_A0100_02_A0100_03` | `1-32` | 32 |
| `SC_A0100_03_A0100_04` | `1-7` | 7 |
| `SC_A0100_04_A0100_05` | `1-13` | 13 |
| `SC_A0100_06_A0100_10` | `1-9` | 9 |
| `SC_A0100_07_A0100_10` | `1-5` | 5 |
| `SC_A0100_08_A0100_10` | `1-6` | 6 |
| `SC_A0100_10_A0100_12` | `1-9` | 9 |
| `SC_A0100_12_A0100_14` | `1-3` | 3 |
| `SC_A0100_14_A0100_16` | `1-63` | 63 |
| `SC_A0100_16_A0100_18` | `1-21` | 21 |
| `SC_A0100_18_A0100_20` | `1-87` | 87 |
| `SC_A0100_20_A0100_22` | `1-17` | 17 |
| `SC_A0100_22_A0100_24` | `1-80` | 80 |
| `SC_A0100_24_A0100_30` | `1-37` | 37 |
| `SC_A0100_30_A0100_32` | `1-26` | 26 |
| `SC_A0100_32_A0100_40` | `1-50` | 50 |
| `SC_A0100_40_A0100_50` | `1-26` | 26 |
| `SC_A0100_50_A0100_60` | `1-34` | 34 |
| `SC_A0100_60_A0100_70` | `1-23` | 23 |
| `SC_A0100_70_A0100_80` | `1-33` | 33 |
| `SC_A0100_80_A0100_90` | `1-31` | 31 |
| `SC_A0100_90_A0110_00` | `1-37` | 37 |
| `SC_A0110_00_A0110_10` | `1-7` | 7 |
| `SC_A0110_10_A0110_20` | `1-25` | 25 |
| `SC_A0110_20_A0110_30` | `1-4` | 4 |
| `SC_A0110_30_A0110_40` | `1-32` | 32 |
| `SC_A0110_40_A0110_50` | `1-16` | 16 |
| `SC_A0110_50_A0110_60` | `1-10` | 10 |
| `SC_A0110_60_A0110_70` | `1-39` | 39 |
| `SC_A0110_70_A0110_80` | `1-18` | 18 |
| `SC_A0110_80_A0110_90` | `1-23` | 23 |
| `SC_A0110_90_A0120_00` | `1-59` | 59 |
| `SC_A0120_00_A0120_05` | `1-20` | 20 |
| `SC_A0120_05_A0120_10` | `1-20` | 20 |
| `SC_A0120_10_A0120_20` | `1-15` | 15 |
| `SC_A0120_20_A0120_30` | `1-50` | 50 |
| `SC_A0120_30_A0120_40` | `1-16` | 16 |
| `SC_A0120_40_A0120_50` | `1-8` | 8 |
| `SC_A0120_50_A0120_60` | `1-42` | 42 |
| `SC_A0120_60_A0120_70` | `1-16` | 16 |
| `SC_A0120_70_A0120_80` | `1-35` | 35 |
| `SC_A0120_80_A0120_85` | `1-5` | 5 |
| `SC_A0120_85_A0120_90` | `1-79` | 79 |
| `SC_A0120_90_A0130_00` | `1-34` | 34 |
| `SC_A0130_00_A0130_10` | `1-25` | 25 |
| `SC_A0130_10_A0130_20` | `1-17` | 17 |
| `SC_A0130_20_A0130_30` | `1-13` | 13 |
| `SC_A0130_30_A0130_40` | `1-56` | 56 |
| `SC_A0130_40_A0130_50` | `1-71` | 71 |
| `SC_A0130_50_A0130_60` | `1-77` | 77 |
| `SC_A0130_60_A0130_70` | `1-33` | 33 |
| `SC_A0130_70_A0130_80` | `1-9` | 9 |
| `SC_A0130_80_A0130_90` | `1-12` | 12 |
| `SC_A0130_90_A0140_00` | `1-33` | 33 |
| `SC_A0140_00_A0140_10` | `1-8` | 8 |
| `SC_A0140_10_A0140_20` | `1-34` | 34 |
| `SC_A0140_20_A0140_30` | `1-17` | 17 |
| `SC_A0140_30_A0140_40` | `1-22` | 22 |
| `SC_A0140_40_A0140_50` | `1-22` | 22 |
| `SC_A0140_50_A0140_60` | `1-46` | 46 |
| `SC_A0140_60_A0140_70` | `1-14` | 14 |
| `SC_A0140_70_A0140_80` | `1-18` | 18 |
| `SC_A0140_80_A0140_90` | `1-6` | 6 |
| `SC_A0140_90_A0150_00` | `1-8` | 8 |
| `SC_A0150_00_A0150_10` | `1-20` | 20 |
| `SC_A0150_10_A0150_20` | `1-17` | 17 |
| `SC_A0150_20_A0150_30` | `1-22` | 22 |
| `SC_A0150_30_A0150_40` | `1-31` | 31 |
| `SC_A0150_40_A0150_50` | `1-38` | 38 |
| `SC_A0150_50_A0150_60` | `1-19` | 19 |
| `SC_A0150_60_A0150_70` | `1-19` | 19 |
| `SC_A0150_70_A0150_80` | `1-24` | 24 |
| `SC_A0150_80_A0150_90` | `1-27` | 27 |
| `SC_A0150_90_A0160_00` | `1-14` | 14 |
| `SC_A0160_00_A0160_10` | `1-18` | 18 |
| `SC_A0160_10_A0160_20` | `1-71` | 71 |
| `SC_A0160_20_A0160_30` | `1-14` | 14 |
| `SC_A0160_30_A0160_40` | `1-23` | 23 |
| `SC_A0160_40_A0160_50` | `1-9` | 9 |
| `SC_A0160_50_A0160_60` | `1-18` | 18 |
| `SC_A0160_60_A0160_70` | `1-7` | 7 |
| `SC_A0160_70_A0160_80` | `1-20` | 20 |
| `SC_A0160_80_A0160_90` | `1-23,25` | 24 |
| `SC_A0160_90_A0170_00` | `1-13` | 13 |
| `SC_A0170_00_A0170_10` | `1-19` | 19 |
| `SC_A0170_10_A0170_20` | `1-15` | 15 |
| `SC_A0170_20_A0170_30` | `1-6` | 6 |
| `SC_A0170_30_A0170_40` | `1-51` | 51 |
| `SC_A0170_40_A0170_50` | `1-32` | 32 |
| `SC_A0170_50_A0170_60` | `1-55` | 55 |
| `SC_A0170_70_A0180_00` | `1-34` | 34 |
| `SC_A0170_80_A0170_60` | `1-4` | 4 |
| `SC_A0180_00_A0180_10` | `1-22` | 22 |
| `SC_A0180_10_A0180_20` | `1-18` | 18 |
| `SC_A0180_20_A0180_30` | `1-22` | 22 |
| `SC_A0180_30_A0180_40` | `1-13` | 13 |
| `SC_A0180_40_A0180_50` | `1-16` | 16 |
| `SC_A0180_50_A0180_60` | `1-13` | 13 |
| `SC_A0180_60_A0180_70` | `1-9` | 9 |
| `SC_A0180_70_A0180_80` | `1-25` | 25 |
| `SC_A0180_80_A0180_90` | `1-29` | 29 |
| `SC_A0180_90_A0190_00` | `1-32` | 32 |
| `SC_A0190_00_A0190_10` | `1-13` | 13 |
| `SC_A0190_10_A0190_20` | `1-53` | 53 |
| `SC_A0190_20_A0190_30` | `1-47` | 47 |
| `SC_A0190_30_A0190_40` | `1-19` | 19 |
| `SC_A0190_40_A0190_50` | `1-16` | 16 |
| `SC_A0190_50_A0190_60` | `1-45` | 45 |
| `SC_A0190_60_A0190_70` | `1-19` | 19 |
| `SC_A0190_70_A0190_80` | `1-20` | 20 |
| `SC_A0190_80_A0190_90` | `1-48` | 48 |
| `SC_A0190_90_A0200_00` | `1-19` | 19 |
| `SC_A0200_00_A0200_10` | `1-32` | 32 |
| `SC_A0200_10_A0200_20` | `1-35` | 35 |
| `SC_A0200_20_A0200_30` | `1-15` | 15 |
| `SC_A0200_30_A0200_40` | `1-15` | 15 |
| `SC_A0200_40_A0200_50` | `1-22` | 22 |
| `SC_A0200_50_A0200_60` | `1-38` | 38 |
| `SC_A0200_60_A0200_70` | `1-26` | 26 |
| `SC_A0200_80_A0210_00` | `1-13` | 13 |
| `SC_A0200_90_A0210_00` | `1-8` | 8 |
| `SC_A0210_00_A0210_10` | `1-24` | 24 |
| `SC_A0210_10_A0210_20` | `1-44` | 44 |
| `SC_A0210_20_A0210_30` | `1-5` | 5 |
| `SC_A0210_30_A0210_40` | `1-43` | 43 |
| `SC_A0210_40_A0210_50` | `1-15` | 15 |
| `SC_A0210_50_A0210_60` | `1-48` | 48 |
| `SC_A0210_60_A0210_70` | `1-32` | 32 |
| `SC_A0210_70_A0210_80` | `1-18` | 18 |
| `SC_A0210_80_A0210_90` | `1-24` | 24 |
| `SC_A0210_90_A0220_00` | `1-17` | 17 |
| `SC_A0220_00_A0220_10` | `1-25` | 25 |
| `SC_A0220_10_A0220_20` | `1-11` | 11 |
| `SC_A0220_20_A0220_30` | `1-24` | 24 |
| `SC_A0220_30_A0220_40` | `1-27` | 27 |
| `SC_A0220_40_A0220_50` | `1-17` | 17 |
| `SC_A0220_50_A0220_60` | `1-7` | 7 |
| `SC_A0220_60_A0220_70` | `1-19` | 19 |
| `SC_A0220_70_A0220_80` | `1-6` | 6 |
| `SC_A0220_80_A0220_90` | `1-18` | 18 |
| `SC_A0220_90_A0230_00` | `1-19` | 19 |
| `SC_A0230_00_A0230_10` | `1-9` | 9 |
| `SC_A0230_10_A0230_15` | `1-10` | 10 |
| `SC_A0230_15_A0230_20` | `1-43` | 43 |
| `SC_A0230_20_A0230_30` | `1-20` | 20 |
| `SC_A0230_30_A0230_40` | `1-21` | 21 |
| `SC_A0230_40_A0230_50` | `1-43` | 43 |
| `SC_A0230_50_A0230_60` | `1-20` | 20 |
| `SC_A0230_60_A0230_70` | `1-24` | 24 |
| `SC_A0230_70_A0230_80` | `1-20` | 20 |
| `SC_A0230_80_A0230_90` | `1-16` | 16 |
| `SC_A0230_90_A0240_00` | `1-10` | 10 |
| `SC_A0240_00_A0240_10` | `1-29` | 29 |
| `SC_A0240_10_A0240_20` | `25-42` | 18 |
| `SC_A0240_20_A0240_30` | `1-27` | 27 |
| `SC_A0240_30_A0240_40` | `1-26,36-42` | 33 |
| `SC_A0240_40_A0240_50` | `1-15` | 15 |
| `SC_A0240_50_A0240_60` | `1-4` | 4 |
| `SC_A0240_70_A0250_00` | `1` | 1 |
| `SC_A0240_80_A0250_00` | `1-13` | 13 |
| `SC_A0250_00_A0250_10` | `1-26` | 26 |
| `SC_A0250_10_A0250_20` | `1-17` | 17 |
| `SC_A0250_20_A0250_30` | `1-19` | 19 |
| `SC_A0250_30_A0250_40` | `1-16` | 16 |
| `SC_A0250_40_A0250_50` | `1-34` | 34 |
| `SC_A0250_50_A0250_60` | `1-44` | 44 |
| `SC_A0250_70_A0360_00` | `1-9` | 9 |
| `SC_A0250_80_A0360_00` | `1-10` | 10 |
| `SC_A0250_90_A0360_00` | `1-6` | 6 |
| `SC_A0360_00_A0360_10` | `1-7,15-19` | 12 |
| `SC_A0360_10_A0360_20` | `1-8` | 8 |
| `SC_A0360_20_A0360_30` | `1-20` | 20 |
| `SC_A0360_30_A0360_40` | `1-10` | 10 |
| `SC_A0360_40_A0360_50` | `1-40` | 40 |
| `SC_A0360_50_A0360_60` | `1-20` | 20 |
| `SC_A0360_60_A0360_70` | `1-15` | 15 |
| `SC_A0360_70_A0360_80` | `1-15` | 15 |
| `SC_A0360_80_A0360_90` | `1-8` | 8 |
| `SC_A0360_90_A0370_00` | `1-18` | 18 |
| `SC_A0370_00_A0370_10` | `1-18` | 18 |
| `SC_A0370_10_A0370_20` | `1-9,16-28` | 22 |
| `SC_A0370_20_A0370_30` | `1-9` | 9 |
| `SC_A0370_30_A0370_40` | `1-18` | 18 |
| `SC_A0370_40_A0370_50` | `1-29` | 29 |
| `SC_A0370_50_A0370_60` | `1-6` | 6 |
| `SC_A0370_60_A0370_70` | `1-26` | 26 |
| `SC_A0370_70_A0370_80` | `1-13` | 13 |
| `SC_A0370_80_A0370_90` | `1-10` | 10 |
| `SC_A0370_90_A0380_00` | `1-25` | 25 |
| `SC_A0380_00_A0380_10` | `1-22` | 22 |
| `SC_A0380_10_A0380_20` | `1-9` | 9 |
| `SC_A0380_20_A0380_30` | `1-18` | 18 |
| `SC_A0380_30_A0380_40` | `1-19` | 19 |
| `SC_A0380_40_A0380_50` | `1-21` | 21 |
| `SC_A0380_50_A0390_50` | `1-8` | 8 |
| `SC_A0390_50_A0390_60` | `1-8` | 8 |
| `SC_A0390_60_A0390_70` | `1-10` | 10 |
| `SC_A0390_70_A0390_80` | `1-34` | 34 |
| `SC_A0390_80_A0390_90` | `1-11` | 11 |
| `SC_A0390_90_A0400_00` | `1-35` | 35 |
| `SC_A0400_00_A0400_10` | `1-16` | 16 |
| `SC_A0400_10_A0400_20` | `1-20` | 20 |
| `SC_A0400_30_A0400_40` | `1-4,9-15` | 11 |
| `SC_A0400_40_A0400_50` | `1-15` | 15 |
| `SC_A0400_50_A0400_60` | `1-19` | 19 |
| `SC_A0400_60_A0400_70` | `1-50` | 50 |
| `SC_A0400_70_A0400_80` | `1-10` | 10 |
| `SC_A0400_80_A0400_90` | `1-39` | 39 |
| `SC_A0400_90_A0410_00` | `1-19` | 19 |
| `SC_A0410_00_A0410_10` | `1-15` | 15 |
| `SC_A0410_10_A0410_20` | `1-15` | 15 |
| `SC_A0410_20_A0410_30` | `1-11` | 11 |
| `SC_A0410_30_A0410_40` | `1-10` | 10 |
| `SC_A0410_40_A0410_50` | `1-8` | 8 |
| `SC_A0410_50_A0410_60` | `1-28` | 28 |
| `SC_A0410_60_A0410_70` | `1-2` | 2 |
| `SC_A0410_70_A0410_80` | `1-30` | 30 |
| `SC_A0410_80_A0410_90` | `1-21` | 21 |
| `SC_A0410_90_A0420_00` | `1-30` | 30 |
| `SC_A0420_00_A0420_10` | `1-35` | 35 |
| `SC_A0420_10_A0420_20` | `1-10` | 10 |
| `SC_A0420_20_A0420_30` | `1-18` | 18 |
| `SC_A0420_30_A0420_40` | `1-6` | 6 |
| `SC_A0420_40_A0420_50` | `1-28` | 28 |
| `SC_A0420_50_A0420_60` | `1-20` | 20 |
| `SC_A0420_60_A0420_70` | `1-27` | 27 |
| `SC_A0420_70_A0420_80` | `1-10` | 10 |
| `SC_A0420_80_A0420_90` | `1-22` | 22 |
| `SC_A0420_90_A0430_00` | `1-4` | 4 |
| `SC_A0430_00_A0430_10` | `1-22` | 22 |
| `SC_A0430_10_A0430_20` | `1-24` | 24 |
| `SC_A0430_20_A0430_30` | `1-25` | 25 |
| `SC_A0430_30_A0430_40` | `1-31` | 31 |
| `SC_A0430_40_A0430_50` | `1-28` | 28 |
| `SC_A0430_50_A0430_60` | `1,25-26` | 3 |
| `SC_A0430_60_A0430_70` | `1-28` | 28 |
| `SC_A0430_70_A0430_80` | `1-16` | 16 |
| `SC_A0430_80_A0430_90` | `1-3,15` | 4 |
| `SC_A0430_90_A0440_00` | `1-8` | 8 |
| `SC_A0440_00_A0440_10` | `1-46` | 46 |
| `SC_A0440_10_A0440_20` | `1-32` | 32 |
| `SC_A0440_20_A0440_30` | `1-15` | 15 |
| `SC_A0440_30_A0440_40` | `1-82` | 82 |
| `SC_A0440_40_A0440_50` | `1-17` | 17 |
| `SC_A0440_50_A0440_60` | `1-18` | 18 |
| `SC_A0440_60_A0440_70` | `1-47` | 47 |
| `SC_A0440_70_A0440_80` | `1-10` | 10 |
| `SC_A0440_80_A0440_90` | `1-8` | 8 |
| `SC_A0440_90_A0450_00` | `1-44` | 44 |
| `SC_A0450_00_A0450_10` | `1-35` | 35 |
| `SC_A0450_10_A0450_20` | `1-9` | 9 |
| `SC_A0450_20_A0450_30` | `1-16` | 16 |
| `SC_A0450_30_A0450_40` | `1-20` | 20 |
| `SC_A0450_40_A0450_50` | `1-11` | 11 |
| `SC_A0450_50_A0450_60` | `1-21` | 21 |
| `SC_A0450_60_A0450_70` | `1-18` | 18 |
| `SC_A0450_70_A0450_80` | `1-7` | 7 |
| `SC_A0450_80_A0450_85` | `1-8` | 8 |
| `SC_A0450_85_A0450_90` | `1-32` | 32 |
| `SC_A0450_90_A0460_00` | `1-15` | 15 |
| `SC_A0460_00_A0460_10` | `1-17` | 17 |
| `SC_A0460_10_A0460_20` | `1-24` | 24 |
| `SC_A0460_20_A0460_30` | `1-33` | 33 |
| `SC_A0460_30_A0460_40` | `1-10` | 10 |
| `SC_A0460_40_A0460_50` | `1-7` | 7 |
| `SC_A0460_50_A0460_60` | `1-30` | 30 |
| `SC_A0460_60_A0460_70` | `1-17` | 17 |
| `SC_A0460_70_A0500_00` | `1-8` | 8 |

Fully excluded zero-debt scene: SC_A0400_20_A0400_30, permitted NONE,
excluded 1-10, raw count 10.

Coverage checksum: 269 translated scenes; 6,078 permitted rows.

