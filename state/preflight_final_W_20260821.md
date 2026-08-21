# Final W-lane continuity and policy preflight

Scope:

- `SC_W0100_00_W0110_00`
- `SC_W0100_10_W0210_00`
- `SC_W0100_20_Z9999_99`
- `SC_W0100_30_W0410_00`
- `SC_W0110_10_Z9999_99`
- `SC_W0110_20_Z9999_99`
- `SC_W0210_20_Z9999_99`
- `SC_W0410_20_Z9999_99`

This is continuity/content-safety preflight only. No translation, QC,
arbitration, pipeline/configuration, immutable source, or Git artifact was
modified.

## Authoritative extraction and classification

A fresh read-only extraction from the retained Full Edition
`/tmp/tsuyokiss_data.fpk` (SHA-256
`9255ad580bf94bdfd5970715cc3ff5e343f320a2085a4ecae6a4322d10b73a94`)
reproduced all eight configured `scratchpad/jp_dumps` documents exactly:
scene/source labels, row payloads, stable engine IDs, speakers, kinds, Japanese,
and source hashes. The W material is in block `B0041` and contains 54 raw rows,
all dialogue.

The canonical manifest plus both configured overlays now yield 44 permitted
rows and 10 excluded rows:

| Scene | Raw | Excluded | Permitted projection | Classification |
|---|---:|---|---|---|
| `SC_W0100_00_W0110_00` | 3 | none | `1-3` (3) | fully permitted, text-bearing |
| `SC_W0100_10_W0210_00` | 3 | none | `1-3` (3) | fully permitted, text-bearing |
| `SC_W0100_20_Z9999_99` | 12 | `2-4`, `6-12` (10) | `1`, `5` (2) | partially excluded, sparse |
| `SC_W0100_30_W0410_00` | 2 | none | `1-2` (2) | fully permitted, text-bearing |
| `SC_W0110_10_Z9999_99` | 27 | none | `1-27` (27) | fully permitted, text-bearing |
| `SC_W0110_20_Z9999_99` | 2 | none | `1-2` (2) | fully permitted, text-bearing |
| `SC_W0210_20_Z9999_99` | 2 | none | `1-2` (2) | fully permitted, text-bearing |
| `SC_W0410_20_Z9999_99` | 3 | none | `1-3` (3) | fully permitted, text-bearing |

Classification totals: seven fully permitted scenes, one partially excluded
scene, zero fully excluded scenes, and zero zero-text scenes. All eight require
a permitted model-source projection; all eight projections now exist.

## Content boundary

The supervisor-approved wave-500 overlay excludes only these W ranges:

- `SC_W0100_20_Z9999_99:2-4`: sexualized proposition/innuendo policy category;
  the first row is structural setup, the middle row is the triggering core,
  and the final row is its immediate dependent response.
- `SC_W0100_20_Z9999_99:6-12`: sexualized personal-garment/body-framing policy
  category; `6-7` are dependent setup and `8-12` form the continuous triggering
  sequence.

No excluded wording is reproduced here. These rows are not translation debt
and must remain absent from translation, QC, arbitration, and build artifacts.
Permitted indexes `1` and `5` are independently coherent generic tutorial
beats: neither contains a held referent nor requires a bridge across either
gap. Translators must preserve the sparse key set exactly and must not smooth,
explain, infer, or reconstruct either omission.

All other projected W rows passed policy screening. No additional restricted
or dependent range was found.

## Continuity and scene function

The W lane is a self-aware tutorial/meta-game sequence rather than an in-story
route block. Kinu supplies loud, playful prompts; Subaru is the relaxed
straight man and explainer; Yoshimi appears only as the softly protesting
backstage helper in `W0110_10`. Do not import later route relationships or
story outcomes into these system-facing scenes.

- `W0100_00` is the initial short invitation to hear the controls tutorial.
  Kinu's opening uses an adult-fan euphemism as a teasing audience address; do
  not render it as a literal statement about physical size.
- `W0100_10` is a repeat tutorial greeting built around Kinu's deliberately
  false kanji spelling and Subaru's correction. Preserve the faux-etymology
  joke's function rather than mechanically glossing its characters.
- `W0100_20` has only the independent opening at `1` and the renewed controls
  invitation at `5` in scope. The discontinuity is intentional policy
  filtering, not a missing connective.
- `W0100_30` turns Kinu's tutorial greeting into a formulaic RPG-village line;
  Subaru observes that the routine has become repetitive.
- `W0110_10` is the substantive game guide. It covers the map/character-route
  structure, limited map-movement period, possible ending branches, unlockable
  routes, suggested route order, keyboard configuration, display size,
  quick-save, and the `F5` panic-button function. Preserve the explicit
  meta-game register; do not rewrite these as events occurring to the cast.
- `W0110_20` is the brief decline/skip branch that sends the player to the main
  game.
- `W0210_20` is a two-line homophone exchange. The paired misunderstanding must
  be adapted as one joke rather than translated independently.
- `W0410_20` is a later repeat visit with no remaining gameplay benefit. It
  calls back to the tutorial-village formula and ends on the generic RPG
  `Villager A` role joke.

## Voice, terminology, and reveal locks

- Speakers: `きぬ` -> `Kinu`, `スバル` -> `Subaru`, `良美` -> `Yoshimi`,
  `レオ` -> `Leo`. Kinu remains high-energy and shameless; Subaru remains
  relaxed and teasing; Yoshimi remains soft and mildly plaintive.
- Direct `カニ` remains the locked nickname `Crab`. `子蟹ちゃん` in
  `W0110_10:4` is a playful diminutive wordplay item, not an age or relationship
  reveal; preserve the crab function without silently treating it as the
  ordinary locked direct address.
- `よっぴー` remains the established `Yoppi`; Yoshimi's protest at
  `W0110_10:7` is friendly annoyance, with no later-route undercurrent.
- Keep `BAR` as the displayed capitalization and preserve UI terms consistently:
  map, character route, ending, route order, keyboard settings, screen size,
  quick-save, panic button, and `F5`.
- Contextual `攻略` denotes pursuing/completing a character route. Do not use a
  literal conquest or violent sense. `固定シナリオ` is the committed/fixed
  character-route phase, and `攻略順位` is recommended route order.
- `W0100_30:1` and `W0410_20:2` have byte-identical Japanese and the same source
  hash. They must receive identical English as a deliberate callback even
  though `narrative_gates.json` declares no formal mirror.
- `W0100_10:2` and `W0210_20:1-2` are the principal contested wordplay ranges.
  Resolve each for equivalent comic function without adding a lore claim.
- Preserve Japanese dialogue wrappers in English, use only the project's ASCII
  ellipsis/dash/apostrophe profile, and keep every target string CP932-clean.

## Deterministic validation

W-specific gates pass:

- exact raw cardinality `54` and exact permitted cardinality `44`;
- exact exclusion cardinality `10` at `W0100_20:2-4,6-12`;
- duplicate-key rejection and exact projected index sets;
- projected rows are byte-for-field identical to their authoritative raw rows;
- source SHA-256 recomputation, stable engine IDs, speaker/kind metadata, and
  dialogue-wrapper checks;
- CP932 encodability of all 54 source strings;
- zero excluded rows in model projections;
- no declared source-mirror or repeated-choice gate applies.

### Repository-wide manifest gate

During final validation, the supervisor verified that every historical
wave-200 overlay index was already consolidated into the canonical manifest
and removed that historical record from the active overlay list. The active
configuration now merges `content_exclusions.json` with only
`state/content_exclusions_wave500_overlay.json`. The public overlay-aware
exclusion-manifest gate and narrative-source gate both return zero findings.
No repository-wide deterministic blocker remains.

## Hard stop

Preflight is complete for the 44 permitted W rows. Stop before translation.
Excluded rows must remain inaccessible to downstream model stages. Translation
may use only the eight filtered `scratchpad/model_sources` documents and must
preserve the sparse `W0100_20` boundary exactly.
