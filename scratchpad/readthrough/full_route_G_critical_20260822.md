# Critical full-route speed readthrough: route G

Date: 2026-08-22  
Stage: post-QC critical readthrough only  
Verdict: **FAIL — 3 major and 4 minor findings remain open**  
Translation changes: NONE

## Scope and evidence

I read all 38 current `SC_G` translation files continuously in scene order,
covering exactly 2,427 permitted rows. Every suspicious passage was checked
against its overlay-aware filtered model-source row, stable source hash, engine
ID, speaker metadata, adjacent permitted chronology, the 13 G-route continuity
specifications, the project bible/glossary/style/character locks, and the
existing accuracy, literary, and arbitration records.

Only `scratchpad/model_sources/SC_G*.json` was used for Japanese text. No raw
source body was opened. The 38 public projections contain 2,427 permitted rows
and record 601 exclusions inside those translated scenes. The canonical
manifest additionally contains 1,424 rows in 14 fully excluded G scenes. The
complete route inventory is therefore 52 source scenes / 4,452 raw rows, with
2,025 excluded and 2,427 permitted rows.

All 38 accuracy records, 38 literary records, and 38 arbitration/no-op records
were present and reviewed. The active wave-500 overlay contributes no G-route
entry, and `narrative_gates.json` contains no G-route gate. No excluded row was
read, quoted, summarized, bridged, or reconstructed.

This pass changed no translation, QC, arbitration, source, exclusion,
configuration, pipeline, or Git artifact. This report is its only output.

## Deterministic validation

| Gate | Result |
| --- | --- |
| Filtered model-source projections | PASS: 38 / 38 present; all `scene` and `source_label` values match their stems |
| Translation files | PASS: 38 / 38 present |
| Permitted rows | PASS: 2,427 / 2,427 |
| Raw / excluded / permitted inventory | PASS: 4,452 / 2,025 / 2,427 |
| Exact permitted index joins | PASS: 0 missing, extra, reordered, or excluded keys |
| Fully excluded artifacts | PASS: all 14 fully excluded scenes remain projection/translation/QC/arbitration-free |
| Engine IDs | PASS: 2,427 present, 2,427 unique, all bound to `B0035:<scene>:<zero-padded-index>` |
| Source SHA-256 metadata | PASS: 2,427 / 2,427 recompute from permitted Japanese rows |
| JSON duplicate-key rejection | PASS: 38 projections and 38 translations |
| Translation `file` identity | PASS: 38 / 38 exact scene stems |
| Speaker-map coverage | PASS: 0 permitted source speakers missing |
| Manifest and translation-identity unit gates | PASS: 10 / 10 |
| CP932 encoding | PASS: all 38 complete translation JSON files |
| Forbidden Unicode typography | PASS: 0 rows |
| Japanese script in English targets | PASS: 0 rows |
| Placeholder scan | PASS: no TODO, TBD, FIXME, untranslated, placeholder, missing, or replacement-character markers |
| Control-sequence audit | PASS: no control-bearing permitted G row |
| Dialogue/narration wrapper audit | **FAIL: 2 mismatches across 1,625 dialogue and 802 narration rows** |

Static integrity does not override the open meaning, naming, reveal, and
literary findings below.

## Blocking findings

NONE.

## Major findings

### G-RT-001 — Two rows have wrong presentation wrappers, and one also drops an audible beat

- scenes: `SC_G0500_00_G0520_00`; `SC_G0650_00_G0700_00`
- indexes: `[46]`; `[50]`
- severity: major
- category: engine presentation / omission
- current_text_and_minimal_source-faithful_direction:

| Scene:index | Current text | Minimal correction proposal |
| --- | --- | --- |
| `SC_G0500_00_G0520_00:46` | `「Don't worry about me. I'll explain everything properly on Sunday or so, so until then, please just leave me alone.」` | Use an ASCII quoted narration line rather than spoken-dialogue brackets: `"Don't worry about me. I'll explain everything properly on Sunday or so, so until then, please just leave me alone."` |
| `SC_G0650_00_G0700_00:50` | `Summer really brings out the weirdos.` | Restore both the source dialogue wrapper and the audible eating beat: `「(Munch, munch.) Summer really brings out the weirdos.」` |

- source_evidence: G0500:46 is kind `narration`, has no speaker, and uses the
  source's embedded quotation marks rather than `「」`. G0650:50 is kind
  `dialogue`, speaker `レオ`, and reads
  `「（もぐもぐ）夏になると変なのが沸いてくるなぁ」`.
- project_evidence: Project style reserves Japanese corner brackets for spoken
  dialogue. Other permitted G narration quotations use ASCII quotes or
  apostrophes. G0180:47 already preserves the same `もぐもぐ` beat as
  `(munch, munch)`.
- diagnosis: G0500:46 is statically emitted as dialogue instead of quoted
  message/narration. G0650:50 is emitted as narration instead of Leo dialogue
  and silently loses his chewing delivery. Both existing accuracy and literary
  reports incorrectly passed the wrappers.
- systemic: false
- status: OPEN

### G-RT-002 — Four uses of Kinu's locked nickname drift to `Kani`

- scene: `SC_G0650_00_G0700_00`
- indexes: `[10,13,14,24]`
- severity: major
- category: character / continuity
- current_text_and_minimal_source-faithful_direction:

| Index | Current text | Minimal correction proposal |
| ---: | --- | --- |
| 10 | `「Let's see Kani's call history...」` | `「Let's see Crab's call history...」` |
| 13 | `「Still, I guess Kani really is someone I need to keep an eye on.」` | `「Still, I guess Crab really is someone I need to keep an eye on.」` |
| 14 | `「Come on, wake up. Wake up, Kani.」` | `「Come on, wake up. Wake up, Crab.」` |
| 24 | `「Leo said waking Kani up takes a lot of work.」` | `「Leo said waking Crab up takes a lot of work.」` |

- source_evidence: Every listed source row uses `カニっち` for Kinu.
- project_evidence: `bible/glossary.md` locks `カニ` to `Crab`, and the local G
  continuity spec explicitly locks both `カニ` and `カニっち` to `Crab`.
  This same route uses `Crab` for the nickname at G0100:5, G0180:8/15,
  G0200:23/33, G0500:51, and G0540:395/397.
- diagnosis: The four-row cluster introduces a second English nickname for the
  same character during one scene. The current accuracy record compounds the
  error by expressly certifying `Kani` as route-consistent despite the bible,
  scene spec, and route precedent.
- systemic: true
- status: OPEN

### G-RT-003 — Yoshimi is given an unsupported posture and hallucination-like perception

- scene: `SC_G0800_00_G0850_00`
- index: `[96]`
- severity: major
- category: hallucination / characterization
- current_text: `She crouched in the corner, groaning and apologizing to
  something only she could see.`
- source_evidence: `部屋の隅でうめきながら見えない何かに謝ってた。`
  says only that she groaned in the room's corner and apologized to something
  unseen. It does not state that she crouched or that she visually perceived
  an entity.
- project_evidence: The G continuity spec requires the unease to remain in
  Leo's observations and forbids invented motive or diagnosis. Existing
  accuracy and literary QC also claim that the breakdown was preserved without
  melodramatic padding or diagnostic editorialization.
- diagnosis: `crouched` invents blocking/posture, while `only she could see`
  converts an unseen object of apology into a hallucination-like visual claim.
  That is a materially stronger characterization than the permitted source.
- fix_direction: Use a source-bounded line such as `She groaned in the corner
  of the room, apologizing to something unseen.`
- systemic: false
- status: OPEN

## Minor findings

### G-RT-004 — Leo's full name is left in Japanese order

- scene: `SC_G0650_00_G0700_00`
- index: `[223]`
- severity: minor
- category: name / style continuity
- current_text: `「Hold on. Tsushima Leo isn't the kind of cold-blooded guy who
  ignores someone who needs help.」`
- source_evidence: The row uses Leo's full name, `対馬レオ`.
- project_evidence: `bible/glossary.md` locks the name as `Leo Tsushima`, and
  `bible/style.md` says English prose uses given-name-first order.
- diagnosis: This is the only `Tsushima Leo` occurrence in the G route and
  conflicts with the canonical full-name order.
- fix_direction: Change only the name order: `「Hold on. Leo Tsushima isn't the
  kind of cold-blooded guy who ignores someone who needs help.」`
- systemic: false
- status: OPEN

### G-RT-005 — The source's `JoySta 2 = game console` gloss is omitted

- scene: `SC_G0800_00_G0850_00`
- index: `[54]`
- severity: minor
- category: omission / lore clarity
- current_text: `「Oh, you have a JoySta 2 in here. That's unexpected.」`
- source_evidence: `ジョイステ２（ゲーム機）` explicitly identifies the
  fictional product as a game console.
- project_evidence: No bible entry independently defines `JoySta 2` for the
  English reader; the parenthetical is the permitted source's only local gloss.
- diagnosis: The scene remains understandable from the following game talk,
  but one explicit source proposition is missing.
- fix_direction: Restore the identification without inventing a brand, e.g.
  `「Oh, you have a JoySta 2 game console in here. That's unexpected.」`
- systemic: false
- status: OPEN

### G-RT-006 — Two emotional/domestic lines retain conspicuous translationese

- scenes: `SC_G0760_00_G0800_00`; `SC_G0800_00_G0850_00`
- indexes: `[93]`; `[77]`
- severity: minor
- category: literary / voice
- current_text_and_minimal_source-faithful_direction:

| Scene:index | Current text | Minimal correction proposal |
| --- | --- | --- |
| `SC_G0760_00_G0800_00:93` | `「I already loved you, Leo, but after what you just said I love you even, even more...」` | `「I already loved you, Leo, but after what you just said, I love you so, so much more...」` |
| `SC_G0800_00_G0850_00:77` | `「Mmm. This kind of thing really makes me feel like I'm enjoying a woman's happiness.」` | `「Mmm. This really does feel like one of the joys of being a woman.」` |

- source_evidence: G0760:93 uses emphatic `もっともっと好きになっちゃった`;
  G0800:77 uses the familiar phrase `女の幸せを実感できる`.
- project_evidence: Yoshimi's established English is soft and colloquial. The
  current comma repetition at G0760:93 and `feel like I'm enjoying a woman's
  happiness` at G0800:77 are literal Japanese syntax rather than deliberate
  characterization.
- diagnosis: Meaning is recoverable, but both lines visibly break otherwise
  natural late-route dialogue at important emotional/comic beats.
- systemic: false
- status: OPEN

### G-RT-007 — Two backstory lines add unsupported referential/temporal cues

- scene: `SC_G0870_00_G0900_00`
- indexes: `[144,187]`
- severity: minor
- category: reveal timing / chronology
- current_text_and_minimal_source-faithful_direction:

| Index | Current text | Minimal correction proposal |
| ---: | --- | --- |
| 144 | `「Yes... and that's where I met her.」` | `「Yes... and that's where I met someone.」` |
| 187 | `「...Your mother isn't here anymore.」` | `「...Your mother isn't here.」` |

- source_evidence: G0870:144 says `そこで、出会ったんだ` without naming,
  gendering, or otherwise supplying the object before the orientation
  flashback. G0870:187 says only `お前のお母さんここにはいない`, a spatial
  statement that Yoshimi's mother is not here.
- project_evidence: The scene's accuracy record claims that source uncertainty
  and sequence are preserved. Erika is staged in the following flashback, and
  Yoshimi's mother remains back home; the source neither supplies an antecedent
  for `her` at 144 nor says that her mother is absent `anymore` at 187.
- diagnosis: `her` anticipates the next reveal beat and is a dangling referent
  in the immediate English. `anymore` can imply a prior local presence or death,
  neither of which the line states.
- systemic: false
- status: OPEN

## Continuous-route checks

- **Hallucinations and omissions:** FAIL only for G-RT-001, G-RT-003, and
  G-RT-005. No other unsupported event, motive, object, material omission, or
  source expansion survived verification.
- **Voice and characterization:** PASS apart from G-RT-002 and G-RT-006.
  Leo's brash but protective narration, Yoshimi's gentle public register and
  anxious private repetition, Erika's confident directness, Otome's formal
  bluntness, Kinu's forceful comedy, Subaru's laconic steadiness, Shinichi's
  shamelessness, and the smaller school voices remain distinguishable. The
  report does not convert Yoshimi's source-described crisis into a clinical
  diagnosis.
- **Agency and relationship logic:** PASS. Yoshimi initiates the relationship,
  isolation requests, phone checking, attempted plan involving Erika, family
  disclosure, and later apology. Leo chooses the week-long stay, confronts her,
  remains during the collapse, pursues her in the rain, and offers reassurance.
  Erika independently refuses Yoshimi's demand, maintains their friendship, and
  later asks Leo to protect Yoshimi emotionally.
- **Reveal timing:** PASS except G-RT-007 at G0870:144. Yoshimi's distrust,
  family conditioning, performed smile, friendship origin, and clover memory
  unfold in their source order. The `良美？` speaker uncertainty at G0850:15-20
  remains intact until Erika is identified.
- **Chronology and locations:** PASS except G-RT-007 at G0870:187. The route's
  school days, one-week cohabitation, Sports and Martial Arts Festival,
  confrontation, overnight family disclosure, rain crisis, reconciliation,
  and Sweden coda remain ordered. `Matsukasa`, `Tokyo Bay`, `Ryuumeikan`, and
  Sweden are stable.
- **Branch structure:** PASS. The G0860_10 trust confrontation continues into
  G0870. The alternate G0860_20 wardrobe setup stops exactly at permitted index
  32 and does not infer its excluded continuation. G0930, the sparse G0970
  reconciliation coda, and the G0990 route epilogue remain distinct; no
  filtered branch result is imported into another branch.
- **Scene boundaries:** PASS at the JSON/index layer. Every sparse scene starts,
  stops, and resumes at exact permitted keys, and all 14 fully excluded scenes
  have zero downstream artifacts. Presentation still fails at the two wrapper
  rows in G-RT-001.
- **Systemic names and lore:** `Samesuga` is source- and bible-correct at its
  sole G surname occurrence. `Yoppi`, `Ellie`, `Princess`, `Fukahire`,
  `Igaguri`, `Kurogane-senpai`, `Mr. Tsuchinaga`, `Ryuumeikan`, and `Sports and
  Martial Arts Festival` remain stable. Kinu's nickname and Leo's full-name
  order fail only at G-RT-002 and G-RT-004.
- **Existing arbitration:** G0130:14 remains correctly closed as `Maaji Jima
  Baranga!!`; G0200:28 remains correctly closed as `Reions Mansion`. The other
  36 G arbitration records are no-op/NONE records. None resolves the new open
  findings.

## Exclusion boundaries

The following configured G-route exclusions were honored without inspection or
reconstruction. Counts include 601 rows inside projected scenes and 1,424 rows
in fully excluded scenes, totaling 2,025.

| Scene | Excluded indexes | Count |
| --- | --- | ---: |
| `SC_G0100_00_K0900_00` | `26-28` | 3 |
| `SC_G0110_00_K0900_00` | `51,70-73` | 5 |
| `SC_G0120_00_K0900_00` | `25-28` | 4 |
| `SC_G0170_00_G0180_00` | `7` | 1 |
| `SC_G0280_00_G0290_00` | `3-23` | 21 |
| `SC_G0290_00_G0300_00` | `1-42`, fully excluded | 42 |
| `SC_G0300_00_G0310_00` | `4-6` | 3 |
| `SC_G0310_00_G0320_00` | `1-4`, fully excluded | 4 |
| `SC_G0320_00_G0340_00` | `1-3`, fully excluded | 3 |
| `SC_G0340_00_G0350_00` | `3-9,19-20` | 9 |
| `SC_G0350_00_G0360_00` | `1-34`, fully excluded | 34 |
| `SC_G0360_00_G0370_00` | `1-23`, fully excluded | 23 |
| `SC_G0370_00_G0380_00` | `1-9`, fully excluded | 9 |
| `SC_G0380_00_G0390_00` | `1-6`, fully excluded | 6 |
| `SC_G0390_00_G0400_00` | `1-2`, fully excluded | 2 |
| `SC_G0460_00_G0480_00` | `98-116` | 19 |
| `SC_G0480_00_G0500_00` | `1-518`, fully excluded | 518 |
| `SC_G0500_00_G0520_00` | `27-40` | 14 |
| `SC_G0520_00_G0540_00` | `1-126`, fully excluded | 126 |
| `SC_G0540_00_G0600_00` | `1-62,86,112-132,353-375,380-384` | 112 |
| `SC_G0650_00_G0700_00` | `35-39,61-111,241-242,290-306` | 75 |
| `SC_G0700_00_G0720_00` | `1-38` | 38 |
| `SC_G0720_00_G0750_00` | `4` | 1 |
| `SC_G0750_00_G0760_00` | `1-362`, fully excluded | 362 |
| `SC_G0760_00_G0800_00` | `1-7,96-97,115-116,124` | 12 |
| `SC_G0800_00_G0850_00` | `1-52,91-94,113-117,132-141,149-150,158-171,189-190,202-203,290-292,372-384,433-434,481,506-516` | 121 |
| `SC_G0850_00_G0860_00` | `99-101` | 3 |
| `SC_G0860_20_G0950_00` | `33-59` | 27 |
| `SC_G0870_00_G0900_00` | `122-125,191` | 5 |
| `SC_G0900_00_G0910_00` | `79-84` | 6 |
| `SC_G0910_00_G0920_00` | `1-99`, fully excluded | 99 |
| `SC_G0920_00_G0930_00` | `1-5,41-43,49-53` | 13 |
| `SC_G0950_00_G0960_00` | `1-191`, fully excluded | 191 |
| `SC_G0960_00_G0970_00` | `1-5`, fully excluded | 5 |
| `SC_G0970_00_Z9999_99` | `1-90,102-116` | 105 |
| `SC_G0990_00_Z9999_99` | `42-45` | 4 |

Exclusion checksum: 36 affected source scenes; 2,025 excluded rows; 14 fully
excluded scenes; 0 forbidden downstream artifacts.

## Story-image and runtime limitations

`docs/UI_STORY_IMAGE_LOCALIZATION_MANIFEST.md` inventories only
`titlechip.kg`, `CGChip.kg`, and `EDChip.kg`; it supplies no exact
scene/index-linked G-route story-image evidence. This report therefore makes no
story-image correctness claim and no visual contradiction claim.

The manifest's source/layout checks are not live-engine proof, and its runtime
status remains pending. No in-engine textbox, backlog, nameplate, choice,
transition, sprite, scene image, or localized-asset capture was available.
Runtime wrapping, clipping, font fallback, metadata consumption, speaker-name
presentation, branch execution, and story-image synchronization therefore
remain unresolved limitations despite the static joins, hashes, IDs, maps, and
CP932 checks.

## Correction routing and pass condition

Route G does not pass the mandatory critical readthrough gate in its current
state. Reopen only the 13 listed permitted indexes across five translation
files:

- translation accuracy/engine repair: G0500:46; G0650:10,13,14,24,50,223;
  G0800:54,96; G0870:144,187;
- literary repair: G0760:93; G0800:77;
- then independently recertify the affected full scenes through accuracy and
  literary QC as appropriate, target arbitration only if a documented conflict
  remains, rerun all deterministic gates, and reread the corrected blocks in
  route context.

No broad rewrite is warranted. The route can pass when G-RT-001 through
G-RT-007 are closed, both wrapper mismatches are zero, all 2,427 joins still
pass, and the corrected blocks preserve every exclusion and branch boundary.

## Exact translated-scene coverage

Every listed permitted index was read continuously. Counts sum to 2,427.

| Scene | Permitted indexes read | Count |
| --- | --- | ---: |
| `SC_G0100_00_K0900_00` | `1-25,29-71` | 68 |
| `SC_G0110_00_K0900_00` | `1-50,52-69,74-77` | 72 |
| `SC_G0120_00_K0900_00` | `1-24,29-68` | 64 |
| `SC_G0130_00_K0900_00` | `1-45` | 45 |
| `SC_G0140_00_G0150_00` | `1-9` | 9 |
| `SC_G0150_00_G0160_00` | `1-4` | 4 |
| `SC_G0160_00_G0170_00` | `1-10` | 10 |
| `SC_G0170_00_G0180_00` | `1-6,8-14` | 13 |
| `SC_G0180_00_G0190_00` | `1-50` | 50 |
| `SC_G0190_00_G0200_00` | `1-30` | 30 |
| `SC_G0200_00_G0250_00` | `1-69` | 69 |
| `SC_G0250_00_G0260_00` | `1-9` | 9 |
| `SC_G0260_00_G0270_00` | `1-4` | 4 |
| `SC_G0270_00_G0280_00` | `1-3` | 3 |
| `SC_G0280_00_G0290_00` | `1-2` | 2 |
| `SC_G0300_00_G0310_00` | `1-3` | 3 |
| `SC_G0340_00_G0350_00` | `1-2,10-18` | 11 |
| `SC_G0400_00_G0420_00` | `1-25` | 25 |
| `SC_G0420_00_G0440_00` | `1-19` | 19 |
| `SC_G0440_00_G0460_00` | `1-41` | 41 |
| `SC_G0460_00_G0480_00` | `1-97` | 97 |
| `SC_G0500_00_G0520_00` | `1-26,41-55` | 41 |
| `SC_G0540_00_G0600_00` | `63-85,87-111,133-352,376-379,385-416` | 304 |
| `SC_G0600_00_G0650_00` | `1-74` | 74 |
| `SC_G0650_00_G0700_00` | `1-34,40-60,112-240,243-289,307-321` | 246 |
| `SC_G0700_00_G0720_00` | `39-42` | 4 |
| `SC_G0720_00_G0750_00` | `1-3,5-28` | 27 |
| `SC_G0760_00_G0800_00` | `8-95,98-114,117-123,125-133` | 121 |
| `SC_G0800_00_G0850_00` | `53-90,95-112,118-131,142-148,151-157,172-188,191-201,204-289,293-371,385-432,435-480,482-505,517-529` | 408 |
| `SC_G0850_00_G0860_00` | `1-98` | 98 |
| `SC_G0860_10_G0870_00` | `1-22` | 22 |
| `SC_G0860_20_G0950_00` | `1-32` | 32 |
| `SC_G0870_00_G0900_00` | `1-121,126-190,192-195` | 190 |
| `SC_G0900_00_G0910_00` | `1-78` | 78 |
| `SC_G0920_00_G0930_00` | `6-40,44-48,54-55` | 42 |
| `SC_G0930_00_G0990_00` | `1-38` | 38 |
| `SC_G0970_00_Z9999_99` | `91-101` | 11 |
| `SC_G0990_00_Z9999_99` | `1-41,46-47` | 43 |
