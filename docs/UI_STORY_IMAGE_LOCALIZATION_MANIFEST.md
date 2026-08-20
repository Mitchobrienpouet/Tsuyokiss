# Tsuyokiss UI and story-image localization manifest

Status: STARTED — source inventory blocked locally by a full temporary volume
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

## Current blocker

The eight multipart archive copies supplied to the scratch workspace filled the backing temporary filesystem. Even read-only shell startup currently fails with `No space left on device` before a command can execute, so the original images cannot yet be enumerated or inspected locally. The persistent supplied files remain intact. Resume with source inventory immediately after temporary workspace capacity is restored.
