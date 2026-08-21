# Story-image manifest integrity audit

Date: 2026-08-22  
Scope: static inspection of
`docs/UI_STORY_IMAGE_LOCALIZATION_MANIFEST.md` and every repository artifact
supporting its three localized asset-ledger entries.  
Result: **LOCAL ASSET INTEGRITY PASS; SCENE-LINK COVERAGE NOT ESTABLISHED.**

This audit makes no runtime-rendering claim. Retail archives, the rebuilt
archive, and the game executable were not available as repository artifacts,
and no engine session was launched.

## Exact inventory

| Measure | Count |
| --- | ---: |
| Localized asset-ledger mappings | 3 |
| Unique engine-member paths | 3 |
| UI-only mappings | 2 |
| Mixed UI/story-label mappings | 1 |
| Repository support artifacts expected per mapping | 4 |
| Repository support artifacts present | 12/12 |
| Unique mapped Japanese/English string pairs | 61/61 |
| Duplicate Japanese mappings | 0 |
| Duplicate English mappings | 0 |
| Rendered mapped text placements | 163 |
| Exact `SC_*` scene bindings | 0 |
| Exact source-index bindings | 0 |
| Route-letter bindings | 0 |
| Scene-linked assets | **0** |

The 61 unique mapped strings comprise 30 title/bonus-menu strings, 10 CG
gallery category strings, and 21 opening/ending titles. Their rendered
placements are respectively 60, 40, and 63 because the button labels are
repeated across visual states while the title-menu descriptions appear once.

## Engine mappings and local support paths

| Engine member | Class | Translation map | Localized PNG | QA record | Deployable ZLC2 | Result |
| --- | --- | --- | --- | --- | --- | --- |
| `chip.fpk:titlechip.kg` | UI | `assets/ui/translations/titlechip.json` | `assets/ui/png/titlechip.kg.png` | `qa/ui/titlechip.json` | `patch/ui/chip/titlechip.kg.zlc2` | PASS |
| `chip.fpk:CGChip.kg` | UI | `assets/ui/translations/CGChip.json` | `assets/ui/png/CGChip.kg.png` | `qa/ui/CGChip.json` | `patch/ui/chip/CGChip.kg.zlc2` | PASS |
| `chip.fpk:EDChip.kg` | UI / STORY | `assets/ui/translations/EDChip.json` | `assets/ui/png/EDChip.kg.png` | `qa/ui/EDChip.json` | `patch/ui/chip/EDChip.kg.zlc2` | PASS |

All 12 paths exist. Asset/member capitalization is consistent across the
ledger, translation maps, PNGs, QA records, and ZLC2 patches. All six JSON
documents parse strictly without duplicate keys. Recombining each translation
map's `source_archive` and `asset` fields reproduces the corresponding ledger
engine path exactly.

The common font path recorded in all three QA files exists and its SHA-256 is
`6d7cec07f5a9035e208532dab35a51312aef4a7f26eb524dd614c9fcd97c3264`,
matching every QA record.

## Static technical verification

| Asset | PNG SHA-256 | ZLC2 SHA-256 | Decoded KG SHA-256 | Decoded pixels vs PNG | Dimensions/mode/alpha |
| --- | --- | --- | --- | --- | --- |
| `titlechip.kg` | PASS | PASS | PASS | byte-equivalent pixels | 1024x1024 RGBA; alpha 0-255 |
| `CGChip.kg` | PASS | PASS | PASS | byte-equivalent pixels | 1024x1024 RGBA; alpha 0-255 |
| `EDChip.kg` | PASS | PASS | PASS | byte-equivalent pixels | 1024x1024 RGBA; alpha 0-255 |

Each checked-in ZLC2 has one compression layer, decodes successfully to GCGK,
matches the `localized_kg_sha256` recorded in QA, and decodes to pixels exactly
matching its checked-in PNG. The checked-in PNG and ZLC2 hashes also match the
QA records. Visual inspection confirms that the mapped English labels are
present in all three sheets and remain inside the intended button regions.

The uncompressed `patch/ui/chip/*.kg` intermediates are not checked in, but
their recorded hashes remain independently reproducible by decoding the three
present ZLC2 files in memory. This is therefore not a broken deployable mapping.

## Scene and route coverage

There are **no scene-linked assets in the manifest**. Precisely:

- no ledger row names an `SC_*` scene;
- no ledger row supplies a source index or an index range;
- no ledger row binds an asset to an A/B/C/D/E/F/G/I/J/M/N/W route code or
  branch variant;
- no mapped image is identified as a scene CG, letter, document, card, sign,
  phone screen, location/date card, or other in-story evidence.

`EDChip.kg` provides aggregate ending-collection labels for seven named heroine
endings: Otome, Kinu, Erika, Nagomi, Inori, Yoshimi, and Sunao. It also contains
two opening labels, one crossover-ending label, and eleven other named
bonus/special-ending titles. These names provide human-readable route-category
coverage, but they do not establish route-code, trigger-scene, ending-scene, or
source-index coverage.

`CGChip.kg` likewise names the same seven heroine gallery categories plus
`OTHER`, `ITEMS`, and `BACKGROUNDS`; category names are not mappings from a CG
to the script scene in which it appears.

## Embedded translated text finding

Translated text is embedded in all three localized PNG sheets, but its role is
limited as follows:

- `titlechip.kg`: 15 UI buttons and 15 UI descriptions;
- `CGChip.kg`: 10 gallery filter labels;
- `EDChip.kg`: 21 story-related opening/ending **titles** repeated across three
  menu states.

Thus, `EDChip.kg` contains 21 unique translated story-related title labels (63
rendered placements), but **zero mapped images contain scene-level translated
story prose, dialogue, lore text, letters, documents, signs, or other text tied
to a script scene/index**. This result applies only to the three mapped local
assets. It does not prove that the unmapped retail `cg.fpk` or deferred
`kg.fpk` inventory contains no player-readable story text.

## Duplicate, malformed, and missing mapping findings

### Duplicate or broken engine mappings

**NONE.** The three engine-member identifiers are unique and their repository
support chains are complete. There are no duplicate JP/EN pairs and no
localized hash or pixel-roundtrip failures.

### Mapping completeness gaps

1. **Missing scene triggers:** all 3/3 ledger entries lack exact scene/index
   bindings. This prevents route readthroughs from using them as scene-specific
   visual evidence.
2. **Missing route-code bindings:** the single mixed UI/story asset lists named
   endings but no route letters, ending scene IDs, branch variants, or trigger
   conditions.
3. **Missing commit provenance:** the manifest's required-field table calls for
   an exact checkpoint commit, but none of the 3/3 ledger rows records one.
4. **No machine-readable local-path linkage:** the Markdown ledger records
   engine-facing paths only. The 12 supporting repository paths can be matched
   unambiguously by archive/member basename, but they are not explicitly linked
   from each row.
5. **Class spelling drift:** the ledger writes `UI / STORY`, while the EDChip
   translation and QA JSON files write `UI_STORY`. The meaning is consistent,
   but the enum is not normalized for machine comparison.

The ledger also summarizes Japanese/English scope, font/layout, and hashes
rather than carrying the manifest's declared per-asset fields inline.
Supplemental translation and QA JSON files provide those details, so this is a
manifest-normalization gap rather than a missing localized asset.

## Retail and runtime limitations

- `chip.fpk`, `cg.fpk`, `kg.fpk`, the Full Edition ISO, and any rebuilt
  `chip.fpk` are intentionally absent from the repository under the manifest's
  retail-source policy. Retail member existence, retail source hashes, archive
  member order, untouched-member identity, and rebuilt-archive re-extraction
  could not be independently repeated in this static audit.
- The QA claims for archive rebuild/re-extraction and untouched members remain
  documentary evidence from the existing records, not newly reproduced proof.
- No menu state, ending collection, CG gallery, story scene, backlog, or other
  engine view was run. Button selection, hit areas, scaling, font rasterization,
  clipping, alpha blending, archive loading, and actual runtime display remain
  unverified here.

Static conclusion: the three mapped local assets and their deployable patch
chains are intact, unique, and internally consistent. Story-image coverage is
not scene-addressable because the manifest currently contains exactly zero
scene-linked mappings.
