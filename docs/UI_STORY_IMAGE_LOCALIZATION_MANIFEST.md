# Tsuyokiss UI and story-image localization manifest

Status: ACTIVE — source inventory complete for `chip.fpk` and `cg.fpk`
Started: 2026-08-20
Branch: `codex/wave-300-continuation-20260820`

## Authorized scope

- Title menu and all image-backed submenus.
- Scenario select and other non-explicit UI sprites.
- Story-related images that carry plot, lore, characterization, location/date information, letters, documents, cards, or other player-readable content.
- English localization follows `bible/glossary.md`, `bible/style.md`, and `bible/characters.md`.
- Explicit sexualized assets involving school-age characters are excluded from model work and generated outputs under `content_exclusions.json`.

## Fail-closed invariants

Every localized image must preserve the retail source asset's:

- exact pixel width and height;
- file format and engine-facing filename;
- color mode, palette/indexing requirements, and bit depth where required;
- alpha/transparency semantics;
- non-text artwork, button states, shortcut icons, hit-area alignment, margins, and reading order.

No output is accepted solely because it looks plausible. Each item requires source transcription, context-backed English, visual comparison, deterministic metadata checks, and an engine-reference/runtime proof when the relevant build path is available.

## Per-asset fields

| Field | Required value |
|---|---|
| Asset path | Exact engine-facing path |
| Class | UI / STORY / DECORATIVE |
| Trigger/context | Script scene and source index, or menu state |
| Japanese | Verbatim transcription |
| English | Locked final rendering |
| Dimensions | Width x height, source = output |
| Format/mode | Format, mode, palette/indexing, bit depth |
| Alpha | Source and output alpha semantics |
| Font/layout | Typeface, size, alignment, bounds |
| QC | Linguistic, visual, technical, runtime |
| Hashes | Source and localized SHA-256 |
| Commit | Exact checkpoint commit |

## Checkpoint policy

Commit and push narrow, verified batches. Do not modify or commit retail archives or binaries. Generated replacement assets, their editable/localization sources, manifests, and QA evidence belong in the repository; retail originals remain local-only.

## Retail source baseline

- Full Edition ISO: 4,216,410,112 bytes, SHA-256 `0a9487dec8610fc9a9555c77f71629c021d8f6cee64639dde583f8a37e8ab6aa`.
- `chip.fpk`: 97/97 members extracted and decoded for visual inventory.
- `cg.fpk`: 1,151/1,151 members extracted and decoded for visual inventory.
- `kg.fpk`: 3,172 indexed members; extraction is deferred until script-trigger filtering removes ordinary character sprites.
- Retail source extraction remains outside Git. Only localization sources, replacements, and QA evidence are committed.

## Localized asset ledger

| Asset | Class | Japanese scope | English scope | Dimensions / mode | Technical QC | Visual/runtime QC |
|---|---|---|---|---|---|---|
| `chip.fpk:titlechip.kg` | UI | Title/bonus menu buttons and descriptions | 15 buttons and 15 descriptions | 1024x1024 RGBA, alpha retained | GCGK and ZLC2 round-trips PASS; rebuilt FPK index/re-extraction PASS; engine name retained | Source/layout comparison PASS; runtime pending |

The image-generation draft for `titlechip.kg` was rejected because it changed the canvas to 1254x1254 RGB, moved button geometry, and omitted copy. The committed asset is rebuilt deterministically from the retail 1024x1024 RGBA sheet with fixed coordinates and byte-proven GCGK re-encoding.

The localized ZLC2 payload is 387,527 bytes versus the retail member's 350,619 bytes. Injection therefore uses the checked `replace-member` FPK rebuild path rather than unsafe in-place overwrite. The rebuilt 97-member archive reparses successfully, the localized member re-extracts byte-identically, and every untouched packed member remains byte-identical to retail. The rebuilt retail archive itself remains local-only and is never committed.
