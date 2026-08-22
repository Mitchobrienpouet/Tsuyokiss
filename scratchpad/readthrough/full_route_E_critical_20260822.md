# Critical full-route speed readthrough: E route

Date: 2026-08-22  
Stage: post-QC critical readthrough only  
Verdict: **PASS / closed after repair, independent QC, and targeted arbitration**
Translation changes after audit: 15 targeted line values plus 2 speaker-map values

## Scope and evidence

I read all 81 extant `SC_E` translation files continuously in scene order,
covering all 8,893 permitted rows. Every concrete suspicion was checked only
against the corresponding overlay-aware filtered projection in
`scratchpad/model_sources/SC_E*.json`. I also reviewed the project bible,
glossary, style and character locks, the applicable E-route continuity specs,
canonical and overlay exclusions, narrative gates, and the existing 81
accuracy and 81 literary QC reports.

The exclusion-accounted E inventory contains 94 scene identities and 10,987
rows: 8,893 permitted rows in the 81 translated scenes and 2,094 configured
excluded rows. Of the excluded rows, 657 are opaque gaps inside translated
scenes and 1,437 belong to 13 fully excluded scenes with zero translation debt.
No excluded row was opened, read, summarized, bridged, or reconstructed. No
raw source dump was used.

This pass did not edit translations, QC, arbitration, configuration, sources,
pipeline state, or Git. The only artifact written is this report.

## Deterministic validation

| Gate | Result |
| --- | --- |
| Translation files | PASS: 81 |
| Filtered projections | PASS: 81 |
| Permitted rows | PASS: 8,893 / 8,893 |
| Exclusion-accounted rows | PASS: 10,987 total = 8,893 permitted + 2,094 excluded |
| Exact permitted index joins | PASS: 0 missing, extra, duplicate, or excluded keys |
| Fully excluded scene artifacts | PASS: 13 / 13 have no translation or model-source artifact |
| Translation JSON schema and duplicate keys | PASS: 0 errors; all use exactly `file`, `speaker_map`, and `lines` |
| Translation `file` identity | PASS: 81 / 81 match the filename/scene stem |
| Projection scene identity | PASS: 81 / 81 |
| Engine IDs | PASS: 8,893 present, 8,893 unique, 0 malformed scene bindings |
| Source SHA-256 metadata | PASS: 8,893 / 8,893 recompute from permitted projected Japanese |
| Speaker-map coverage | PASS: 0 permitted source speakers missing |
| CP932 encoding | PASS: 0 translation-line or speaker-map failures |
| Forbidden Unicode typography | PASS: 0 curly-quote, Unicode dash, or ellipsis failures |
| Japanese script in English targets | PASS: 0 rows |
| Placeholder scan | PASS: no TODO, TBD, FIXME, replacement character, templating token, or obvious untranslated marker |
| Control sequences | PASS: 0 source/translation token mismatches |
| Dialogue wrappers | PASS after repair: 0 of 6,280 permitted dialogue rows mismatched |

The findings below record the original audit evidence; every status and the
closure section now reflect the completed repair and recertification lanes.

## Major findings

### E-RT-001 — Tonfa is mislabeled as Touka in two scenes

- scenes: `SC_E0580_00_E0590_00`; `SC_E0700_00_E0710_00`
- indexes:
  - `SC_E0580_00_E0590_00`: speaker rows `30,31,33`; narration `41`
  - `SC_E0700_00_E0710_00`: speaker rows
    `124,130,132,135,141,143,145,147,148,150,152,154,159`; narration `167`
- severity: major
- category: lore / speaker metadata / continuity
- current_text:
  - both speaker maps use `豆花` -> `Touka` on the listed spoken rows;
  - E0580:41 says `Yashi left with Touka.`;
  - E0700:167 says `But even Touka had given up on working there...`.
- source_evidence: the permitted introduction at
  `SC_E0560_00_E0570_00:60` explicitly gives `楊豆花（ヤン・トンファー）`,
  and that scene correctly maps and names her as `Tonfa`. The two affected
  scenes use the same source name and speaker identity.
- project_evidence: current cross-route use and the later E-route locks use
  `Tonfa`; the two affected local E specs retain an older contradictory
  `Touka` lock.
- diagnosis: one recurring classmate changes displayed name and narration name
  inside a single route, shortly after her explicit Tonfa introduction.
- fix_direction: change only the two speaker-map values to `Tonfa`, plus
  `Touka` -> `Tonfa` at E0580:41 and E0700:167. Preserve her lightly clipped,
  non-caricatured English and all surrounding prose.
- systemic: true
- status: closed

### E-RT-002 — Erika's spoken victory aside loses meaning and breaks its wrapper

- scene: `SC_E0910_00_E0920_00`
- index: `47`
- severity: major
- category: meaning / voice / engine presentation
- current_text: `「Victory!」 The smile of someone who has accomplished her mission.`
- source_evidence: the entire permitted row is Erika dialogue. It includes an
  opening self-satisfied `ふっ`, `ヴィクトリー！`, and a parenthetical comic
  self-caption pointing to her triumphant expression, all inside the source
  dialogue wrapper.
- project_evidence: project style requires Japanese corner brackets around the
  entire spoken line. The current English is the sole wrapper mismatch among
  6,280 permitted E dialogue rows.
- diagnosis: the English drops Erika's opening scoff, converts her spoken comic
  aside into external narration, and ends the corner wrapper before the row is
  finished. That changes both voice and static engine presentation.
- fix_direction: keep the whole row in dialogue and retain the comic aside,
  e.g. `「Hmph, victory! (← triumphant smile)」`. Do not turn the aside into a
  separate narration row.
- systemic: false
- status: closed

## Minor findings

### E-RT-003 — Locked event names drift in six rows

- scenes: `SC_E0490_00_E0500_00`; `SC_E0560_00_E0570_00`;
  `SC_E0580_00_E0590_00`; `SC_E0590_00_E0600_00`;
  `SC_E0710_00_E0720_00`
- indexes: `39`; `59,71`; `72`; `1`; `1`
- severity: minor
- category: lore / terminology / continuity
- current_text:
  - E0560:59,71; E0580:72; and E0590:1 use
    `Athletics and Martial Arts Festival`.
  - E0490:39 uses `Matsukasa's Port-Opening Festival`.
  - E0710:1 uses `Matsukasa Port Opening Anniversary Festival` even though
    this row's source says `まつかさ開国祭`, without `記念`.
- source_evidence: the four school-event rows use `体育武道祭`; E0490:39 uses
  `松笠の開国祭`; E0710:1 uses `まつかさ開国祭`.
- project_evidence: the current central glossary locks these to
  `Sports and Martial Arts Festival`, `Matsukasa Port Opening Festival`, and
  `Port Opening Festival`. The same E route already uses the correct sports
  name seventeen times, the correct full civic name at E0720:19, and the
  correct shortened civic name throughout E0700. E0700:141 is not part of the
  finding: its source explicitly includes `開国記念祭`, so its `Anniversary`
  wording is source-grounded.
- diagnosis: all six rows remain understandable, but they fragment proper
  event names within one route and against the central terminology authority.
- fix_direction:
  - E0560:59,71; E0580:72; E0590:1 ->
    `Sports and Martial Arts Festival`.
  - E0490:39 and E0710:1 -> `Matsukasa Port Opening Festival`, preserving the
    surrounding syntax.
- systemic: true
- status: closed

## Continuous-route checks

- **Hallucinations and omissions:** No additional unsupported event, invented
  motive, material omission, or unexplained expansion survived filtered-source
  verification. E-RT-002 is the only material line-level omission/reframing
  found.
- **Voice and characterization:** PASS apart from E-RT-001 and E-RT-002.
  Leo's dry self-justification, Nagomi's formal hostility and gradual private
  softness, Kinu's loud physical comedy, Erika's polished dominance, Yoshimi's
  gentle support, Otome's stern athletic formality, Subaru's laconic practical
  care, Shinichi's shameless bravado, Inori's languor, and Heizo's booming
  authority remain distinct. Tonfa's clipped syntax is intentional; only her
  English name label drifts.
- **Agency and relationship logic:** PASS. Nagomi chooses to accept the cooking
  assignment, initiates the beach invitation, initiates the impulsive first
  kiss, decides to speak with Tennoji, and chooses the chef path. Leo chooses
  to shield her, confesses first, asks before the later mutual kiss, offers his
  home, and eventually chooses a complementary business dream. The handholding,
  kiss, confession, and dream decisions are not reassigned.
- **Reveal timing:** PASS. Nagomi's father, cooking inheritance, closed `line`,
  hostility toward Tennoji, fear of losing her father's memory, and chef dream
  are disclosed in stages. The relationship is not publicly confirmed before
  the second-semester council scene, and the future restaurant plan does not
  leak before the rooftop resolution.
- **Chronology:** PASS. The route proceeds from mid-June council recruitment,
  the training retreat, the two-day Sports and Martial Arts Festival, finals,
  summer break, the July 30-31 Port Opening Festival, August courtship and
  reconciliation, second semester and the Ryuumei Festival setup, then the
  three-year coda. No date or event order contradiction was found.
- **Branch and scene boundaries:** PASS. The early table-tennis choice branches
  reconverge without contradiction. Every partial exclusion remains an opaque
  discontinuity, and all 13 fully excluded scenes remain zero-debt. The sparse
  three-row `SC_E0795_40_E0800_00` projection and the hard stop at
  `SC_E0960_00_E0990_00:38` are preserved without bridging.
- **Systemic names:** `Samesuga` is correct in every surname occurrence;
  `Heizo`, `Ellie`, `Mr. Tsuchinaga`, `Ryuumeikan`, `Ikajima`, and `Ryuumei
  Festival` remain stable. `Igaguri` is internally stable under the E-route
  lock. The Tonfa inconsistency identified as E-RT-001 is repaired and closed.
- **Events:** The score progression, East/West army identities, Dragon Cup,
  tied score, deciding dodgeball match, Port Opening Festival curry, and
  Ryuumei Festival setup remain coherent. The six naming variants in E-RT-003
  are repaired and closed.
- **Placeholders and engine surface:** PASS after closure of E-RT-002. No placeholder,
  untranslated target, control-token drift, missing speaker-map coverage, or
  file-identity defect was found.

## Exclusion boundaries

The following configured exclusions were honored without reconstruction:

| Scene | Excluded indexes | Count | Status |
| --- | --- | ---: | --- |
| `SC_E0120_00_E0120_10` | `32,47-54,63-70,79-85` | 24 | opaque gap(s) |
| `SC_E0200_00_E0300_00` | `28-30` | 3 | opaque gap(s) |
| `SC_E0300_00_E0310_00` | `61-63,76-94,99-100,218-220` | 27 | opaque gap(s) |
| `SC_E0320_00_E0330_00` | `5-6` | 2 | opaque gap(s) |
| `SC_E0360_00_E0370_00` | `11-24` | 14 | opaque gap(s) |
| `SC_E0380_00_E0390_00` | `10-12` | 3 | opaque gap(s) |
| `SC_E0400_10_E0410_00` | `163-167,175` | 6 | opaque gap(s) |
| `SC_E0430_00_E0440_00` | `29-31` | 3 | opaque gap(s) |
| `SC_E0450_00_E0460_00` | `26-29,52-53` | 6 | opaque gap(s) |
| `SC_E0460_00_E0470_00` | `37-40,74-80,123-128` | 17 | opaque gap(s) |
| `SC_E0490_00_E0500_00` | `45-54,87-98,101-137,150-183,189-192,312-315` | 101 | opaque gap(s) |
| `SC_E0510_00_E0520_00` | `87-101` | 15 | opaque gap(s) |
| `SC_E0520_10_E0520_30` | `1-23` | 23 | fully excluded |
| `SC_E0520_30_E0520_40` | `1-16` | 16 | fully excluded |
| `SC_E0520_40_E0520_60` | `1-68` | 68 | fully excluded |
| `SC_E0520_50_E0520_60` | `1-5` | 5 | fully excluded |
| `SC_E0520_60_E0530_00` | `1-14` | 14 | fully excluded |
| `SC_E0530_00_E0540_00` | `17-23,30-35,361-374,500-517,528-533,548,559-560` | 54 | opaque gap(s) |
| `SC_E0550_00_E0560_00` | `118-124` | 7 | opaque gap(s) |
| `SC_E0560_00_E0570_00` | `78-80` | 3 | opaque gap(s) |
| `SC_E0580_00_E0590_00` | `6-8,45-49` | 8 | opaque gap(s) |
| `SC_E0610_00_E0620_00` | `107-118` | 12 | opaque gap(s) |
| `SC_E0620_00_E0630_00` | `79-81,110-120` | 14 | opaque gap(s) |
| `SC_E0650_00_E0650_50` | `479-486` | 8 | opaque gap(s) |
| `SC_E0680_00_E0690_00` | `32-40,43-45,69,92-99,192-199` | 29 | opaque gap(s) |
| `SC_E0690_00_E0700_00` | `60-63,78-80` | 7 | opaque gap(s) |
| `SC_E0700_00_E0710_00` | `244,252-253,263-265` | 6 | opaque gap(s) |
| `SC_E0730_00_E0740_00` | `9-12,18-21` | 8 | opaque gap(s) |
| `SC_E0770_00_E0780_00` | `269-284,430-462` | 49 | opaque gap(s) |
| `SC_E0780_00_E0790_00` | `1-538` | 538 | fully excluded |
| `SC_E0790_00_E0795_00` | `78-82,95-118,206-224,240-246` | 55 | opaque gap(s) |
| `SC_E0795_00_E0795_10` | `1-5` | 5 | fully excluded |
| `SC_E0795_20_E0795_40` | `1-33` | 33 | fully excluded |
| `SC_E0795_30_E0795_40` | `1-33` | 33 | fully excluded |
| `SC_E0795_40_E0800_00` | `4-118` | 115 | opaque gap(s) |
| `SC_E0800_00_E0820_00` | `1-233` | 233 | fully excluded |
| `SC_E0820_00_E0830_00` | `112-125,136-138,145` | 18 | opaque gap(s) |
| `SC_E0840_00_E0860_00` | `1-137` | 137 | fully excluded |
| `SC_E0860_00_E0870_00` | `14-23,33-57` | 35 | opaque gap(s) |
| `SC_E0870_00_E0880_00` | `8-14` | 7 | opaque gap(s) |
| `SC_E0930_10_E0950_00` | `1-166` | 166 | fully excluded |
| `SC_E0930_20_E0950_00` | `1-166` | 166 | fully excluded |
| `SC_E0960_00_E0990_00` | `39` | 1 | opaque gap(s) |

## Exact translated-scene coverage

| # | Scene | Permitted | Excluded in translated scene |
| ---: | --- | ---: | ---: |
| 1 | `SC_E0100_00_K0900_00` | 29 | 0 |
| 2 | `SC_E0120_00_E0120_10` | 75 | 24 |
| 3 | `SC_E0120_20_E0120_40` | 3 | 0 |
| 4 | `SC_E0120_30_E0120_40` | 4 | 0 |
| 5 | `SC_E0120_40_E0120_60` | 100 | 0 |
| 6 | `SC_E0120_60_K0900_00` | 23 | 0 |
| 7 | `SC_E0140_00_K0900_00` | 66 | 0 |
| 8 | `SC_E0160_00_K0900_00` | 11 | 0 |
| 9 | `SC_E0200_00_E0300_00` | 123 | 3 |
| 10 | `SC_E0300_00_E0310_00` | 244 | 27 |
| 11 | `SC_E0310_00_E0320_00` | 32 | 0 |
| 12 | `SC_E0320_00_E0330_00` | 33 | 2 |
| 13 | `SC_E0330_00_E0340_00` | 12 | 0 |
| 14 | `SC_E0340_00_E0350_00` | 19 | 0 |
| 15 | `SC_E0350_00_E0360_00` | 72 | 0 |
| 16 | `SC_E0360_00_E0370_00` | 12 | 14 |
| 17 | `SC_E0370_00_E0380_00` | 98 | 0 |
| 18 | `SC_E0380_00_E0390_00` | 55 | 3 |
| 19 | `SC_E0390_00_E0400_00` | 63 | 0 |
| 20 | `SC_E0400_00_E0400_10` | 2 | 0 |
| 21 | `SC_E0400_10_E0410_00` | 186 | 6 |
| 22 | `SC_E0410_00_E0420_00` | 6 | 0 |
| 23 | `SC_E0420_00_E0430_00` | 4 | 0 |
| 24 | `SC_E0430_00_E0440_00` | 59 | 3 |
| 25 | `SC_E0440_00_E0450_00` | 92 | 0 |
| 26 | `SC_E0450_00_E0460_00` | 68 | 6 |
| 27 | `SC_E0460_00_E0470_00` | 171 | 17 |
| 28 | `SC_E0470_00_E0480_00` | 30 | 0 |
| 29 | `SC_E0480_00_E0490_00` | 13 | 0 |
| 30 | `SC_E0490_00_E0500_00` | 260 | 101 |
| 31 | `SC_E0500_00_E0510_00` | 3 | 0 |
| 32 | `SC_E0510_00_E0520_00` | 86 | 15 |
| 33 | `SC_E0530_00_E0540_00` | 513 | 54 |
| 34 | `SC_E0540_10_E0540_40` | 20 | 0 |
| 35 | `SC_E0540_20_E0540_40` | 21 | 0 |
| 36 | `SC_E0540_30_E0540_40` | 4 | 0 |
| 37 | `SC_E0540_40_E0540_50` | 33 | 0 |
| 38 | `SC_E0540_50_E0550_00` | 9 | 0 |
| 39 | `SC_E0550_00_E0560_00` | 119 | 7 |
| 40 | `SC_E0560_00_E0570_00` | 174 | 3 |
| 41 | `SC_E0570_10_E0570_30` | 27 | 0 |
| 42 | `SC_E0570_20_E0570_30` | 6 | 0 |
| 43 | `SC_E0570_30_E0580_00` | 125 | 0 |
| 44 | `SC_E0580_00_E0590_00` | 81 | 8 |
| 45 | `SC_E0590_00_E0600_00` | 22 | 0 |
| 46 | `SC_E0600_10_E0610_00` | 22 | 0 |
| 47 | `SC_E0600_20_E0610_00` | 20 | 0 |
| 48 | `SC_E0600_30_E0610_00` | 18 | 0 |
| 49 | `SC_E0610_00_E0620_00` | 106 | 12 |
| 50 | `SC_E0620_00_E0630_00` | 113 | 14 |
| 51 | `SC_E0630_00_E0640_00` | 59 | 0 |
| 52 | `SC_E0640_00_E0650_00` | 9 | 0 |
| 53 | `SC_E0650_00_E0650_50` | 898 | 8 |
| 54 | `SC_E0650_50_E0660_00` | 268 | 0 |
| 55 | `SC_E0660_00_E0670_00` | 254 | 0 |
| 56 | `SC_E0670_10_E0670_20` | 7 | 0 |
| 57 | `SC_E0670_20_E0680_00` | 55 | 0 |
| 58 | `SC_E0680_00_E0690_00` | 517 | 29 |
| 59 | `SC_E0690_00_E0700_00` | 207 | 7 |
| 60 | `SC_E0700_00_E0710_00` | 850 | 6 |
| 61 | `SC_E0710_00_E0720_00` | 179 | 0 |
| 62 | `SC_E0720_00_E0730_00` | 69 | 0 |
| 63 | `SC_E0730_00_E0740_00` | 142 | 8 |
| 64 | `SC_E0740_00_E0750_00` | 38 | 0 |
| 65 | `SC_E0750_00_E0760_00` | 221 | 0 |
| 66 | `SC_E0760_00_E0770_00` | 33 | 0 |
| 67 | `SC_E0770_00_E0780_00` | 413 | 49 |
| 68 | `SC_E0790_00_E0795_00` | 284 | 55 |
| 69 | `SC_E0795_40_E0800_00` | 3 | 115 |
| 70 | `SC_E0820_00_E0830_00` | 173 | 18 |
| 71 | `SC_E0830_00_E0840_00` | 90 | 0 |
| 72 | `SC_E0860_00_E0870_00` | 22 | 35 |
| 73 | `SC_E0870_00_E0880_00` | 26 | 7 |
| 74 | `SC_E0880_00_E0890_00` | 2 | 0 |
| 75 | `SC_E0890_00_E0900_00` | 97 | 0 |
| 76 | `SC_E0900_00_E0910_00` | 43 | 0 |
| 77 | `SC_E0910_00_E0920_00` | 57 | 0 |
| 78 | `SC_E0920_00_E0930_00` | 125 | 0 |
| 79 | `SC_E0950_00_E0960_00` | 156 | 0 |
| 80 | `SC_E0960_00_E0990_00` | 38 | 1 |
| 81 | `SC_E0990_00_Z9999_99` | 71 | 0 |
| **Total** | **81 translated scenes** | **8,893** | **657** |

## Static-only limitation

This is a source-checked static script audit. I did not run the game, inject or
repack assets, inspect textbox/backlog rendering, or verify any story image in
runtime. No runtime or scene-image correctness claim is made. Findings and PASS
statements above apply only to the filtered text, metadata, and deterministic
artifact checks described here.

## Closure

E-RT-001 through E-RT-003 were repaired in the seven affected scenes. Full-scene
accuracy recertification then found and corrected four additional meaning
defects; full-scene literary recertification found the remaining `Ika Island`
terminology drift, repaired it to locked `Ikajima` at indexes 55 and 84, and
returned all seven scenes PASS. A final independent accuracy pass reread all 260
permitted E0490 rows after that change. Targeted arbitration found no competing
accuracy/literary reading and adopted no further translation change. The route-E
critical narrative gate is therefore **PASS / closed** within the static-text
scope and the runtime/story-image limitations above.
