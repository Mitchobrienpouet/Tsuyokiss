# Critical full-route speed readthrough: route F

## Verdict

**PASS at the critical narrative gate, with one minor open finding.** All 1,174
permitted rows in the 35 translated route-F scenes were read continuously in
scene order. The review found `0` blocking, `0` major, and `1` minor issue. The
minor issue is narrowly routable and does not compromise route meaning,
chronology, reveal timing, or branch integrity. This audit changed no
translation, QC, arbitration, source, exclusion, manifest, pipeline, or
configuration artifact.

## Scope and exact coverage

The authoritative route-F inventory contains 42 source scenes and 1,931 rows.
The active merged exclusions remove 757 rows: 611 rows in seven fully excluded
scenes and 146 rows inside eleven partially translated scenes. The resulting
scope is exactly 35 translation files and 1,174 permitted rows.

| Scene | Exact permitted indexes read | Rows |
|---|---:|---:|
| `SC_F0100_00_F0110_00` | `1-36` | 36 |
| `SC_F0110_00_F0200_00` | `1-20` | 20 |
| `SC_F0200_00_F0300_00` | `1-32` | 32 |
| `SC_F0300_00_F0400_00` | `1-29` | 29 |
| `SC_F0400_00_F0500_00` | `1-54` | 54 |
| `SC_F0500_00_F0550_00` | `1-28` | 28 |
| `SC_F0550_00_F0600_00` | `1-16` | 16 |
| `SC_F0600_00_F0610_00` | `1-21` | 21 |
| `SC_F0610_00_F0620_00` | `1-13` | 13 |
| `SC_F0620_00_F0630_00` | `1-4` | 4 |
| `SC_F0630_00_F0640_00` | `1-23` | 23 |
| `SC_F0640_00_F0650_00` | `1-4` | 4 |
| `SC_F0650_00_F0660_00` | `1-7` | 7 |
| `SC_F0660_00_F0670_00` | `1-27` | 27 |
| `SC_F0670_00_F0680_00` | `1-32` | 32 |
| `SC_F0680_00_F0690_00` | `1-32` | 32 |
| `SC_F0710_00_F0720_00` | `41-45` | 5 |
| `SC_F0740_00_F0750_00` | `1-3,6-10,16-29,32-43` | 34 |
| `SC_F0760_00_F0770_00` | `1-13,21-24` | 17 |
| `SC_F0770_00_F0780_00` | `1-48` | 48 |
| `SC_F0780_00_F0790_00` | `1-9` | 9 |
| `SC_F0790_00_F0800_00` | `1-39` | 39 |
| `SC_F0800_00_F0810_00` | `1-32` | 32 |
| `SC_F0810_00_F0820_00` | `1-21,27-150` | 145 |
| `SC_F0820_00_F0830_00` | `1-13,15-17` | 16 |
| `SC_F0830_00_F0840_00` | `1-50` | 50 |
| `SC_F0840_00_F0850_00` | `1-89` | 89 |
| `SC_F0850_00_F0860_00` | `1-20` | 20 |
| `SC_F0860_00_F0870_00` | `1-15,31-63` | 48 |
| `SC_F0870_00_F0880_00` | `1-48` | 48 |
| `SC_F0880_00_F0900_00` | `1-83` | 83 |
| `SC_F0900_00_F0910_00` | `1-72` | 72 |
| `SC_F0930_00_F0940_00` | `1-3` | 3 |
| `SC_F0940_00_F0990_00` | `1-16,20-21` | 18 |
| `SC_F0990_00_Z9999_99` | `1-2,5-13,15-21,24-25` | 20 |
| **Total** |  | **1,174** |

The seven fully excluded scenes remain artifact-free and are not translation or
readthrough debt: `SC_F0690_00_F0700_00` (47),
`SC_F0700_00_F0710_00` (308), `SC_F0720_00_F0730_00` (8),
`SC_F0730_00_F0740_00` (20), `SC_F0750_00_F0760_00` (37),
`SC_F0910_00_F0920_00` (16), and `SC_F0920_00_F0930_00` (175).

The eleven partial-scene gaps are preserved exactly in
`SC_F0680_00_F0690_00`, `SC_F0710_00_F0720_00`,
`SC_F0740_00_F0750_00`, `SC_F0760_00_F0770_00`,
`SC_F0780_00_F0790_00`, `SC_F0810_00_F0820_00`,
`SC_F0820_00_F0830_00`, `SC_F0860_00_F0870_00`,
`SC_F0880_00_F0900_00`, `SC_F0940_00_F0990_00`, and
`SC_F0990_00_Z9999_99`. No excluded row was opened, quoted, summarized,
inferred, or reconstructed.

Evidence reviewed: the complete current F translation sequence; all eleven
route-F continuity preflight specifications; `bible/characters.md`,
`bible/glossary.md`, and `bible/style.md`; the active canonical exclusions and
configured overlay; `narrative_gates.json`; all 35 accuracy records, all 35
literary records, and all 35 contested/no-op records. There are no route-F
arbitration artifacts in the current tree. Source-dependent checks used only
the 35 overlay-aware filtered projections in
`scratchpad/model_sources/SC_F*.json`.

## Minor finding

### F-m01 — the `Tsushima family` relationship is misattached

- **Scene/index:** `SC_F0630_00_F0640_00:7`
- **Severity/category:** `minor / meaning and continuity`
- **Current text:** `「Now then, the rest of Mr. Tsushima's long-time family
  should come along as well.」`
- **Filtered source evidence:** `長い付き合いである` describes the group's
  long association with Leo; it does not make them a literal or
  long-established biological family. The source retains the coined group
  label `対馬さんファミリー`.
- **Project evidence:** the scene preflight identifies the travelers as the
  long-time `Tsushima family` friends, and the route consistently uses the
  label for Leo's close friend circle.
- **Diagnosis/fix direction:** the English attaches `long-time` to `family`,
  which can turn the friend-group joke into a claim about literal kinship.
  Preserve the label and move the duration to the relationship, for example:
  `「Then let's have the Tsushima family, who've known him for years, come
  along too.」` Route this as one narrow source-faithful correction and reread
  the immediate block.
- **Systemic/status:** `false / open`

## Narrative and route-wide checks

- **Hallucination and omission:** No invented motive, relationship, action,
  location, resolved ambiguity, or material omission survived source checking
  beyond F-m01. The memory loss and memory-world episode, Mount Senjo
  contradiction, locket reveal, school events, Ikoi account, date, beach
  sequence, and understated coda preserve their source roles and order.
- **Character and agency:** Leo's defensive humor and growing resolve, Inori's
  abrupt menace and supernatural competence, Kinu's kinetic comedy, Erika's
  polished teasing, Yoshimi's friendly classroom presence, and the supporting
  cast remain distinct. The person who predicts, causes, witnesses, recalls,
  disappears, investigates, and reacts remains correct at each checked beat.
- **Reveal timing:** The translation does not certify Ikoi's fate or a
  supernatural explanation before the route does. The Mount Senjo discrepancy,
  hidden past, locket, and autumn resolution remain staged rather than
  prematurely explained.
- **Chronology and scene boundaries:** The photo mystery, accident prophecy,
  bicycle collision, amnesia, memory dive, remedial lessons, school festival,
  exams, disappearance account, date, beach material, and coda connect in
  coherent order. Hard exclusion boundaries are not bridged with invented
  connective prose.
- **Branch integrity:** No route-F source mirror or repeated-choice group is
  declared by the narrative-gate manifest. The translated sequence contains no
  branch-only fact leakage or contradictory outcome.
- **Names and lore:** Canonical `Samesuga` is present at
  `SC_F0840_00_F0850_00:64`; stale `Samehyo`, `Samehyou`, and `Samejima` forms
  are absent. Locked event naming, including `Sports and Martial Arts Festival`,
  remains consistent. Other route names and relationships remain stable.
- **Investigated non-findings:** `SC_F0400_00_F0500_00:29` (`feast`) and `:46`
  (the 24-hour traffic-accident statement), `SC_F0600_00_F0610_00:19`
  (`Ellie`), `SC_F0770_00_F0780_00:24-28` (the virgin-at-heart/English gag),
  `SC_F0830_00_F0840_00:13` (Superman/breakdance),
  `SC_F0870_00_F0880_00:20` (the missing-person count), and
  `SC_F0990_00_Z9999_99:9-13` (the relationship-distance reflection) are odd
  but source-faithful. `SC_F0630_00_F0640_00:11` deliberately retains Tonfa's
  lightly non-native syntax; the source, preflight voice lock, and accuracy
  record support it, so it is not an English grammar defect.

## Deterministic validation

- **Public validator:** `PASS` — `python tools/codex_vn_pipeline.py validate`
  exited `0`, including exact route-F joins, exclusion enforcement, speaker
  maps, wrappers, metadata, source hashes, engine identifiers, JSON, and codec
  checks for all 35 scenes.
- **Cardinality/index joins:** `PASS` — 35 files and 1,174/1,174 exact permitted
  indexes; all 146 excluded indexes are absent from the translated scenes.
- **Fully excluded artifacts:** `PASS` — all seven fully excluded scenes have
  no translation, accuracy, literary, or contested artifact.
- **Projection identity:** `PASS` — 35 filtered model projections; 1,174
  present, unique engine IDs; every source SHA-256 field is present in canonical
  64-hex form; scene/source identity and internal translation `file` values
  match their filenames.
- **QC/contested inventory:** `PASS` — exactly 35 accuracy, 35 literary, and 35
  contested/no-op records, with no missing or extra translated F scene. No
  route-F arbitration artifact exists to review.
- **Speaker maps and wrappers:** `PASS` — every permitted non-null source
  speaker has a nonempty localized map entry, dialogue/narration wrappers agree
  with source kinds, and paired corner quotes and parentheses balance.
- **Codec/controls:** `PASS` — all 1,174 targets encode as CP932. No smart
  quotes, Unicode ellipses, em/en dashes, carriage returns, manual newlines,
  unresolved placeholders, or leaked source control tokens were found.
- **Narrative gate:** `PASS` — no blocking or major narrative defect and no
  declared F mirror/repeated-choice invariant.

## Story-image and runtime limitations

`docs/UI_STORY_IMAGE_LOCALIZATION_MANIFEST.md` is the sole visual authority
used by this audit. Its ledger covers aggregate title, gallery, and ending UI
assets but maps no asset to a route-F scene/index or variant. No scene-linked
image was inspected or used as evidence. Therefore this report makes no claim
about a route-F CG, sprite or expression, background, prop text, image trigger,
ending-image label, or other story-image correctness.

No live engine, textbox, nameplate, backlog, wordwrap, build, image trigger, or
reinjection proof was available. Static joins, wrappers, metadata, and CP932
checks do not establish runtime fit or visual correctness.

## Required routing

Route only F-m01 through the narrowest accuracy/literary correction lane, then
revalidate and reread `SC_F0630_00_F0640_00:6-9`. No broader rewrite or route
arbitration is indicated. The route remains **PASS** at the critical narrative
gate while this minor prose/relationship attachment debt is open.
