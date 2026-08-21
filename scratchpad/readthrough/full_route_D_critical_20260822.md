# Critical full-route speed readthrough: D route

Date: 2026-08-22  
Stage: post-QC critical readthrough only  
Verdict: **PASS after repair, independent QC, and arbitration closure**  
Translation changes: NONE

## Scope and evidence

I read all 67 extant SC_D translation files continuously in scene order, covering
all 7,989 permitted rows. Suspicious passages were checked against authoritative
source rows only after exclusion-aware filtering. I also reviewed the project
bible, glossary, style and character files, all 19 D-route continuity
specifications, canonical and overlay exclusions, narrative and choice gates,
all existing D accuracy and literary QC reports, the D arbitration records, and
the story/UI image localization manifest.

The authoritative D inventory contains 76 source scenes and 10,040 raw rows.
Configured exclusions remove 2,051 rows, leaving 7,989 permitted rows. Nine
source scenes are fully excluded and carry zero translation debt:

- `SC_D0720_00_D0730_00`: 1-212
- `SC_D0730_00_D0740_00`: 1-24
- `SC_D0760_10_D0760_40`: 1-17
- `SC_D0760_20_D0760_40`: 1-16
- `SC_D0760_70_D0760_40`: 1-7
- `SC_D0760_80_Z9999_99`: 1-19
- `SC_D0840_00_D0850_00`: 1-451
- `SC_D0880_00_D0880_50`: 1-234
- `SC_D0950_00_D0960_00`: 1-186

No fully excluded row was read, summarized, or reconstructed. This pass did not
edit translations, QC, arbitration, configuration, sources, pipeline state, or
Git.

## Deterministic validation

| Gate | Result |
| --- | --- |
| Translation files | PASS: 67 |
| Permitted rows | PASS: 7,989 / 7,989 |
| Raw rows / excluded rows | 10,040 / 2,051 |
| Exact permitted index joins | PASS: 0 missing, extra, or excluded keys |
| Engine IDs | PASS: 7,989 present, 7,989 unique, 0 malformed scene bindings |
| Source SHA-256 metadata | PASS: 0 recomputation mismatches |
| Translation JSON fields and duplicate keys | PASS under the project validator |
| Translation `file` identity field | PASS: 67 / 67 exact scene stems |
| Speaker-map coverage | PASS: 0 source speakers missing |
| Project per-scene validator | PASS: 67 / 67 |
| CP932 encoding | PASS: 0 failures |
| Forbidden Unicode typography | PASS: 0 failures |
| Japanese script in English targets | PASS: 0 rows |
| Placeholder scan | PASS: no TODO, TBD, FIXME, untranslated, placeholder, or replacement-character markers |
| Dialogue-wrapper audit | PASS: 5,430 source dialogue rows checked; 0 mismatches |
| Control-sequence audit | 9 controlled rows checked; 1 intentional mismatch at D0500:163 is explicitly locked by the spec and prior accuracy QC |

The project validator now also rejects missing or mismatched internal `file`
identities; the repaired route passes that strengthened gate.

## Blocking findings

### D-RT-001 — Shinichi's surname has three incompatible renderings

- scene: `SC_D0140_00_K0900_00`; `SC_D0440_00_D0460_00`;
  `SC_D0630_00_D0640_00`; `SC_D0660_00_D0670_00`;
  `SC_D0670_00_D0680_00`; `SC_D0690_00_D0700_00`;
  `SC_D0700_00_D0720_00`; `SC_D0770_00_D0780_00`;
  `SC_D0780_00_D0790_00`; `SC_D0790_40_D0800_00`;
  `SC_D0800_00_D0810_00`
- indexes: [9]; [21]; [3]; [86]; [35]; [79, 109]; [16]; [88]; [279];
  [73]; [141, 149]
- severity: blocking
- category: lore / continuity
- current_text: The 13 D-route surname occurrences alternate among one
  `Samesuga`, five `Samejima`, and seven `Samehyo` renderings. Twelve rows are
  inconsistent with the source reading.
- source_evidence: `SC_D0630_00_D0640_00:3` explicitly writes
  `鮫氷（さめすが）`. Every listed row refers to the same character and uses the
  same surname kanji `鮫氷`; `SC_D0780_00_D0790_00:279` also pairs it directly
  with `新一`.
- project_evidence: The repaired A-route authority now consistently uses
  `Samesuga` for all nine occurrences, based on explicit `さめすが` ruby at two
  A-route introductions. Older D specs and QC conflict with that authority by
  treating `Samejima` or `Samehyo` as the route lock and the one explicit D ruby
  as a joke.
- visual_evidence: NONE
- diagnosis: A recurring character's surname changes twice within one route,
  including direct address, lineup narration, and the `Shark` nickname beat.
  This is a systemic identity/lore failure, not speaker-dependent variation.
- fix_direction: Keep `SC_D0630_00_D0640_00:3` unchanged as the source-ruby
  anchor. Normalize the other twelve listed occurrences to `Samesuga`, while
  preserving `Shinichi`, `Fukahire`, and `Shark` and making no wider prose
  changes. Reconcile the stale D-route locks afterward.
- systemic: true
- status: closed by the global surname/D repair and independent QC

## Major findings

### D-RT-002 — Spoken Leo dialogue is emitted as narration

- scene: `SC_D0500_00_D0520_00`
- indexes: [81]
- severity: major
- category: other / engine presentation
- current_text: `So that's what she meant by a harem.`
- source_evidence: The permitted source row is kind `dialogue`, speaker `レオ`,
  and text `「ハーレムってこういう事ね」`.
- project_evidence: Project style requires Japanese corner brackets around
  spoken dialogue. Existing accuracy and literary QC, and the local preferred
  rendering, retained the prose but missed the absent wrapper.
- visual_evidence: NONE
- diagnosis: Dropping the corner quotes changes an aloud Leo reaction into
  narrator text in the static script representation.
- fix_direction: Restore the wrapper only:
  `「So that's what she meant by a harem.」`
- systemic: false
- status: closed by the global surname/D repair and independent QC

### D-RT-003 — Two translation scene IDs contain filename suffixes

- scene: `SC_D0810_00_D0820_00`; `SC_D0870_00_D0880_00`
- indexes: [`file` metadata]; [`file` metadata]
- severity: major
- category: other / engine metadata
- current_text: The internal `file` values are respectively
  `SC_D0810_00_D0820_00.json` and `SC_D0870_00_D0880_00.json`.
- source_evidence: The authoritative scene IDs are
  `SC_D0810_00_D0820_00` and `SC_D0870_00_D0880_00`; `.json` is the artifact
  extension, not part of either scene ID.
- project_evidence: The other 65 D translations, and every translation outside
  D, use the bare scene stem in `file`. The current project validator does not
  check this field, which is why both artifacts still report `OK`.
- visual_evidence: NONE
- diagnosis: These are the only two translation artifacts whose declared
  identity differs from their scene key and filename stem. Any downstream
  consumer that trusts `file` rather than the path receives a different ID.
- fix_direction: Remove only the `.json` suffix from the two `file` values.
  Do not alter lines, speaker maps, hashes, or filenames.
- systemic: false
- status: closed by the global surname/D repair and independent QC

## Minor findings

### D-RT-004 — Three established event names drift in six rows

- scene: `SC_D0580_00_D0600_00`; `SC_D0810_00_D0820_00`;
  `SC_D0870_00_D0880_00`
- indexes: [33]; [355]; [102, 128, 212, 469]
- severity: minor
- category: lore / continuity
- current_text:
  - D0580:33 uses `Sports and Combat Festival`.
  - D0810:355 uses `Ryuumeikan Festival`.
  - D0870:102, 128, and 212 omit `Port` from the `Matsukasa Port Opening
    Festival` / `Port Opening Festival` name.
  - D0870:469 uses `Athletics and Martial Arts Festival`.
- source_evidence: D0580:33 and D0870:469 use `体育武道祭`; D0810:355 uses
  `竜鳴祭（文化祭）`; D0870:102, 128, and 212 use `まつかさ開国祭` / `開国祭`.
- project_evidence: Current cross-route terminology locks render these as
  `Sports and Martial Arts Festival`, `Ryuumei Festival`, and `Matsukasa Port
  Opening Festival` / `Port Opening Festival`. The same D route uses `Sports
  and Martial Arts Festival` eighteen other times and `Ryuumei Festival` at
  D0930:95 and D0995_21:3. E and M routes consistently retain `Port` for the
  same civic festival.
- visual_evidence: NONE
- diagnosis: The meaning is still understandable, but three proper event names
  drift from their route/project locks, including two variants of the same
  sports event within D.
- fix_direction:
  - D0580:33 and D0870:469 -> `Sports and Martial Arts Festival`.
  - D0810:355 -> `Ryuumei Festival--our cultural festival`.
  - D0870:102 -> `Matsukasa Port Opening Festival`; D0870:128 and 212 ->
    `Port Opening Festival`.
- systemic: true
- status: closed by the global surname/D repair and independent QC

## Continuous-route checks

- **Hallucinations and omissions:** No additional unsupported event, invented
  motive, material omission, or unexplained source expansion survived source
  verification. D0500:163 intentionally omits a stray source `$L` marker under
  the continuity spec and completed accuracy QC; it is not an omission defect.
- **Voice and characterization:** PASS apart from D-RT-001's name drift. Leo's
  dry self-mockery, Erika's polished dominance and later vulnerability,
  Yoshimi's gentle surface and controlled possessiveness, Otome's formal
  bluntness, Kinu's loud physical comedy, Subaru's laconic pragmatism,
  Shinichi's shameless bravado, Nagomi's clipped hostility, Inori's languor,
  and Heizo's booming authority remain distinguishable. Tonfa is consistent in
  all 13 D speaker maps; her lightly non-native grammar at D0540:14,
  D0560:6, D0930:113, and D0960:40 is deliberate voice, not broken prose.
  `Igaguri` is consistent in all six applicable D speaker maps and matches the
  D-route lock; no `Burrhead`/`Igaguri` drift occurs inside this route.
- **Agency and relationship logic:** PASS. Leo chooses to wait, shields Erika
  on his own initiative, and voices both confessions. Erika initiates the first
  mutual kiss and later asks Leo back. Yoshimi initiates her confession and the
  late intimacy in her branch. The two final choice outcomes preserve Leo's
  agency and their distinct consequences.
- **Reveal timing:** PASS. Erika's trial-relationship framing precedes her
  realization of romantic attachment; Yoshimi's love is not confirmed before
  her confession; Erika's regret follows the breakup; Yoshimi's distrust and
  the doll oath remain implicit until the friendship rupture. No branch-only
  outcome leaks into an earlier common scene.
- **Chronology and locations:** PASS. The school-week progression, council
  retreat, Sports and Martial Arts Festival, finals, summer break, Port Opening
  Festival, second-term breakup, confessions, and both future codas remain in
  order. Dates at August 3, August 4, and August 29 do not conflict with the
  surrounding sequence.
- **Branch structure:** PASS. The early D0100/D0120/D0140/D0160 vignettes remain
  discrete. The D0760 route holes remain opaque. The late Yoshimi rejection and
  acceptance paths preserve different causal chains, and the final Erika versus
  Yoshimi selections retain distinct friendship and coda outcomes. No excluded
  setup was inferred to bridge a branch.
- **Scene boundaries:** PASS except D-RT-002. All sparse translated scenes end
  and resume on their exact permitted keys. The nine fully excluded scenes have
  no translation artifacts.
- **Systemic names:** `Tonfa`, `Igaguri`, `Heizo`, `Ellie`, and `Mr. Tsuchinaga`
  are internally stable. Only Shinichi's surname fails route/project continuity.
- **Existing arbitration:** The sole non-NONE D arbitration decision,
  `SC_D0870_00_D0880_00:160`, remains closed: `Dolphin` is a vocative and the
  Kiriya Company is the entity for which the speaker is appointed legal
  counsel.

## Exclusion boundaries

The following configured exclusions were honored without reconstruction:

| Scene | Excluded indexes | Count |
| --- | --- | ---: |
| `SC_D0100_50_K0900_00` | `25-31` | 7 |
| `SC_D0120_00_K0900_00` | `18-30,75-86,92-130` | 64 |
| `SC_D0260_00_D0300_00` | `30-32` | 3 |
| `SC_D0480_00_D0500_00` | `55-56` | 2 |
| `SC_D0540_00_D0560_00` | `147-151` | 5 |
| `SC_D0620_00_D0630_00` | `40-46,49-52` | 11 |
| `SC_D0660_00_D0670_00` | `92-98` | 7 |
| `SC_D0700_00_D0720_00` | `111-129` | 19 |
| `SC_D0720_00_D0730_00` | `1-212`, fully excluded | 212 |
| `SC_D0730_00_D0740_00` | `1-24`, fully excluded | 24 |
| `SC_D0740_00_D0760_00` | `1-12,33-34,41,194-303` | 125 |
| `SC_D0760_10_D0760_40` | `1-17`, fully excluded | 17 |
| `SC_D0760_20_D0760_40` | `1-16`, fully excluded | 16 |
| `SC_D0760_30_D0760_60` | `15-34` | 20 |
| `SC_D0760_40_D0770_00` | `8-18` | 11 |
| `SC_D0760_70_D0760_40` | `1-7`, fully excluded | 7 |
| `SC_D0760_80_Z9999_99` | `1-19`, fully excluded | 19 |
| `SC_D0800_00_D0810_00` | `163-165,193,205-260` | 60 |
| `SC_D0810_00_D0820_00` | `142,197` | 2 |
| `SC_D0820_00_D0830_00` | `49-215,245-250,329-339,404` | 185 |
| `SC_D0830_00_D0840_00` | `8-10,14,54,62-64,74-190` | 125 |
| `SC_D0840_00_D0850_00` | `1-451`, fully excluded | 451 |
| `SC_D0850_00_D0860_00` | `6-17` | 12 |
| `SC_D0860_00_D0870_00` | `1-50,57-63` | 57 |
| `SC_D0870_00_D0880_00` | `7-8,13,21-30,36-38,63-70,224-227,262-289,350-390,480-488` | 106 |
| `SC_D0880_00_D0880_50` | `1-234`, fully excluded | 234 |
| `SC_D0880_50_D0890_00` | `1-12,177-182,215-219,235-236` | 25 |
| `SC_D0890_00_D0900_00` | `29-32,90-91` | 6 |
| `SC_D0920_20_D0920_60` | `76-77,139-141` | 5 |
| `SC_D0940_00_D0950_00` | `13-14,75-81` | 9 |
| `SC_D0950_00_D0960_00` | `1-186`, fully excluded | 186 |
| `SC_D0960_00_D0990_00` | `1-19` | 19 |

Exclusion checksum: 32 affected source scenes; 2,051 excluded rows.

## Story-image and runtime limitations

`docs/UI_STORY_IMAGE_LOCALIZATION_MANIFEST.md` inventories `titlechip.kg`,
`CGChip.kg`, and `EDChip.kg` but supplies no scene-linked D-route story-image
evidence. Therefore no D-route visual contradiction could be tested, and this
report makes no story-image proof claim.

The manifest's static source/layout checks are not live-engine evidence, and its
runtime status remains pending. No in-engine textbox, backlog, nameplate,
choice-screen, transition, or asset capture was available. Runtime wrapping,
clipping, font fallback, nameplate presentation, metadata consumption, and
actual story-image synchronization therefore remain unresolved limitations even
though static joins, engine IDs, wrappers except D-RT-002, and CP932 were
checked.

## Correction routing and pass condition

The required naming, wrapper, metadata, and terminology lanes are complete.
Their independent QC, targeted arbitration, deterministic reruns, and corrected-
block reread are recorded in the closure addendum below. No broad rewrite was
required.

## Exact translated-scene coverage

Every listed index was read continuously. Counts sum to 7,989.

| Scene | Permitted indexes read | Count |
| --- | --- | ---: |
| `SC_D0100_50_K0900_00` | `1-24,32-153` | 146 |
| `SC_D0120_00_K0900_00` | `1-17,31-74,87-91,131-159` | 95 |
| `SC_D0140_00_K0900_00` | `1-178` | 178 |
| `SC_D0160_00_K0900_00` | `1-46` | 46 |
| `SC_D0200_00_D0220_00` | `1-48` | 48 |
| `SC_D0220_00_D0260_00` | `1-54` | 54 |
| `SC_D0260_00_D0300_00` | `1-29,33-100` | 97 |
| `SC_D0300_00_D0330_00` | `1-132` | 132 |
| `SC_D0330_00_D0350_00` | `1-28` | 28 |
| `SC_D0350_00_D0380_00` | `1-26` | 26 |
| `SC_D0380_00_D0400_00` | `1-77` | 77 |
| `SC_D0400_00_D0420_00` | `1-66` | 66 |
| `SC_D0420_00_D0430_00` | `1-37` | 37 |
| `SC_D0430_00_D0440_00` | `1-23` | 23 |
| `SC_D0440_00_D0460_00` | `1-37` | 37 |
| `SC_D0460_00_D0470_00` | `1-59` | 59 |
| `SC_D0470_00_D0480_00` | `1-18` | 18 |
| `SC_D0480_00_D0500_00` | `1-54,57-71` | 69 |
| `SC_D0500_00_D0520_00` | `1-262` | 262 |
| `SC_D0520_00_D0540_00` | `1-193` | 193 |
| `SC_D0540_00_D0560_00` | `1-146,152-318` | 313 |
| `SC_D0560_00_D0580_00` | `1-199` | 199 |
| `SC_D0580_00_D0600_00` | `1-131` | 131 |
| `SC_D0600_00_D0610_00` | `1-60` | 60 |
| `SC_D0610_00_D0620_00` | `1-23` | 23 |
| `SC_D0620_00_D0630_00` | `1-39,47-48,53-59` | 48 |
| `SC_D0630_00_D0640_00` | `1-15` | 15 |
| `SC_D0640_00_D0650_00` | `1-56` | 56 |
| `SC_D0650_00_D0660_00` | `1-67` | 67 |
| `SC_D0660_00_D0670_00` | `1-91,99-118` | 111 |
| `SC_D0670_00_D0680_00` | `1-49` | 49 |
| `SC_D0680_00_D0690_00` | `1-61` | 61 |
| `SC_D0690_00_D0700_00` | `1-169` | 169 |
| `SC_D0700_00_D0720_00` | `1-110` | 110 |
| `SC_D0740_00_D0760_00` | `13-32,35-40,42-193` | 178 |
| `SC_D0760_30_D0760_60` | `1-14` | 14 |
| `SC_D0760_40_D0770_00` | `1-7` | 7 |
| `SC_D0770_00_D0780_00` | `1-109` | 109 |
| `SC_D0780_00_D0790_00` | `1-309` | 309 |
| `SC_D0790_10_D0790_30` | `1-13` | 13 |
| `SC_D0790_20_D0790_30` | `1-15` | 15 |
| `SC_D0790_30_D0790_40` | `1-108` | 108 |
| `SC_D0790_40_D0800_00` | `1-211` | 211 |
| `SC_D0800_00_D0810_00` | `1-162,166-192,194-204,261-395` | 335 |
| `SC_D0810_00_D0820_00` | `1-141,143-196,198-796` | 794 |
| `SC_D0820_00_D0830_00` | `1-48,216-244,251-328,340-403,405-651` | 466 |
| `SC_D0830_00_D0840_00` | `1-7,11-13,15-53,55-61,65-73` | 65 |
| `SC_D0850_00_D0860_00` | `1-5` | 5 |
| `SC_D0860_00_D0870_00` | `51-56,64-74` | 17 |
| `SC_D0870_00_D0880_00` | `1-6,9-12,14-20,31-35,39-62,71-223,228-261,290-349,391-479` | 382 |
| `SC_D0880_50_D0890_00` | `13-176,183-214,220-234,237-279` | 254 |
| `SC_D0890_00_D0900_00` | `1-28,33-89,92-93` | 87 |
| `SC_D0900_00_D0910_00` | `1-124` | 124 |
| `SC_D0910_00_D0920_00` | `1-83` | 83 |
| `SC_D0920_10_D0930_00` | `1-61` | 61 |
| `SC_D0920_20_D0920_60` | `1-75,78-138,142-275` | 270 |
| `SC_D0920_60_D0920_80` | `1-45` | 45 |
| `SC_D0920_80_D0980_00` | `1-76` | 76 |
| `SC_D0930_00_D0940_00` | `1-118` | 118 |
| `SC_D0940_00_D0950_00` | `1-12,15-74` | 72 |
| `SC_D0960_00_D0990_00` | `20-55` | 36 |
| `SC_D0980_00_D0985_00` | `1-25` | 25 |
| `SC_D0985_40_D0995_21` | `1-189` | 189 |
| `SC_D0990_00_Z9999_99` | `1-37` | 37 |
| `SC_D0995_00_Z9999_99` | `1-240` | 240 |
| `SC_D0995_21_D0995_22` | `1-100` | 100 |
| `SC_D0995_22_Z9999_99` | `1-41` | 41 |

Fully excluded zero-debt scenes: `SC_D0720_00_D0730_00`,
`SC_D0730_00_D0740_00`, `SC_D0760_10_D0760_40`,
`SC_D0760_20_D0760_40`, `SC_D0760_70_D0760_40`,
`SC_D0760_80_Z9999_99`, `SC_D0840_00_D0850_00`,
`SC_D0880_00_D0880_50`, and `SC_D0950_00_D0960_00`; permitted NONE.

Coverage checksum: 67 translated scenes; 7,989 permitted rows.

## Repair and closure addendum

All four findings above were repaired in the combined global Samesuga/D
checkpoint: twelve D surname rows were normalized, the Leo dialogue wrapper was
restored, both internal scene IDs lost their invalid suffix, and all six event
names were aligned with the central locks.

Independent accuracy QC then reread the 16 affected B/D scenes in full, covering
5,959 permitted rows, and added 27 source-faithfulness corrections across nine
scenes. Independent literary QC reread the same scope, preserved every accuracy
and D-route lock, and added 34 local prose improvements. Targeted arbitration
retained the established decisions and found no new conflict.

The corrected D finding rows and their immediate continuity blocks were reread
in final form. Samesuga is stable, the wrapper and internal file identities are
exact, and the Sports and Martial Arts Festival, Ryuumei Festival, and Matsukasa
Port Opening Festival names remain consistent. Exact joins, exclusions, hashes,
engine IDs, speaker maps, wrappers, CP932, narrative gates, and public
validation pass. No route-D finding remains open.

This closure remains a static-script result. It does not claim runtime textbox,
backlog, sprite, CG, background, image-trigger, or reinjection verification.
