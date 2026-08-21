# Critical full-route speed readthrough: I route

Date: 2026-08-22  
Stage: post-QC critical readthrough only  
Verdict: **PASS after repair, independent QC, and arbitration closure**  
Translation changes: NONE

## Scope and evidence

I read the sole extant I-route translation continuously in scene order:
`SC_I0100_00_Z9999_99`, all indexes `1-68`, for 68/68 permitted rows. The scene
is a self-contained winter-train friendship epilogue. No canonical or overlay
exclusion applies, so there is no sparse boundary or excluded continuation to
bridge.

Evidence reviewed:

- the current translation, speaker map, and engine identity field;
- `bible/characters.md`, `bible/glossary.md`, and `bible/style.md`;
- `scratchpad/specs/SC_I0100_00_Z9999_99.md`;
- the completed accuracy and literary QC reports;
- the `NONE` arbitration record;
- canonical and overlay exclusion manifests and `narrative_gates.json`;
- `docs/UI_STORY_IMAGE_LOCALIZATION_MANIFEST.md`.

There is no generated `scratchpad/model_sources/` projection for this legacy
scene. In accordance with model-access policy, raw Japanese body text was not
opened. Every semantic suspicion was checked against the completed 68-row
source accuracy certification and its scene-specific conclusions; raw source
metadata alone was used for deterministic index, kind, speaker, engine-ID, and
hash-field checks.

The story/UI localization manifest contains no mapping for this I-route scene.
Accordingly, this report makes no visual or runtime claim.

## Deterministic validation

| Gate | Result |
| --- | --- |
| Translation files | PASS: 1 |
| Raw / excluded / permitted rows | PASS: 68 / 0 / 68 |
| Exact index set | PASS: `1-68`, 0 missing, extra, or excluded keys |
| JSON fields and duplicate keys | PASS |
| Internal `file` identity | PASS: `SC_I0100_00_Z9999_99` |
| Engine IDs | PASS: 68 present, 68 unique |
| Source SHA-256 metadata | PASS: 68 well-formed fields |
| Speaker-map coverage | PASS: 5/5 source tags covered |
| Dialogue/narration wrappers | PASS: 0 mismatches |
| CP932 encoding | PASS: 0 failures |
| Forbidden typography | PASS: 0 smart-quote, ellipsis, dash, or nonbreaking-space failures |
| Japanese script in English targets | PASS: 0 rows after allowed corner wrappers |
| Placeholder scan | PASS: no TODO, TBD, FIXME, untranslated, placeholder, or replacement-character markers |
| Narrative gates | PASS: no source mirror or repeated-choice group applies |
| Required prior-stage artifacts | PASS: accuracy, literary, and arbitration records present |

## Findings

### I-RT-001 — Closing friendship line is needlessly awkward

- scene: `SC_I0100_00_Z9999_99`
- indexes: [54]
- severity: minor
- category: other / literary
- current_text: `That's right. These guys were my childhood friends and my
  friends, both.`
- source_evidence: The completed accuracy QC certifies all 68 rows against the
  recovered source and specifically confirms the closing reflection's meaning,
  order, agency, and emotional progression. The intended proposition is the
  twofold status of the same companions: childhood friends and present friends.
- project_evidence: The literary QC confirms that the final shift from banter
  into Leo's friendship reflection should remain gradual and unembellished.
- visual_evidence: NONE; no scene-linked asset is listed in the localization
  manifest.
- diagnosis: `my childhood friends and my friends, both` is grammatically
  decipherable but stiff, and final-position `both` can momentarily sound as if
  it counts people rather than the two relationship categories. The awkwardness
  interrupts an otherwise clean tonal descent into the coda.
- fix_direction: Preserve the deliberate distinction and all surrounding
  propositions while recasting only the syntax, for example: `That's right.
  They were my childhood friends--and my friends, too.` Route this through the
  literary repair lane; no accuracy rewrite is indicated.
- systemic: false
- status: closed by the route-I literary repair and independent QC

No blocking or major finding remains.

## Continuous-route checks

- **Hallucinations and omissions:** PASS. The Susukino/Snow Country opening
  gag, winter hotel and snowboarding plans, Shinichi's stalking joke, Kinu's
  single-life bravado, Subaru's apple beat, car-trip planning, and the closing
  train metaphor remain supported by the completed source certification. No
  invented relationship outcome or new causal explanation was found.
- **Character and voice:** PASS apart from I-RT-001's localized prose issue.
  Kinu is loud and combative, Shinichi shameless and desperate, Subaru dry and
  practical, and Leo the grounded straight man whose narration becomes quietly
  reflective only after the group banter subsides.
- **Agency:** PASS. Shinichi chooses the lodging and pursues girls; Kinu rejects
  suitors and proposes future travel; Subaru volunteers to drive because he
  distrusts the others behind the wheel; Leo owns the closing reflection.
- **Reveal and relationship discipline:** PASS. Kinu's promise to keep
  troubling Leo and the group's loneliness at any member leaving remain
  suggestive friendship beats, not a romantic confession or route outcome.
- **Timeline and continuity:** PASS. The train is already moving north through
  Tohoku toward a winter trip, the prior year's bad lodging is clearly a
  recollection, and the possible future road trip does not displace the current
  journey. The shared-destination/separate-paths image remains hypothetical and
  forward-looking.
- **Lore and terminology:** PASS. `Fukahire`, `Crab`, Tohoku, Susukino, and
  Snow Country are internally coherent; no surname variant or school-event
  terminology is introduced.
- **Scene boundary and coda:** PASS. The single scene opens in active train
  banter and ends on the continuing journey without implying a later event or
  reconstructing outside material.

## Repair and closure addendum

The single minor finding was repaired at index `54`. Independent accuracy then
reviewed all 68 permitted rows against the newly generated overlay-aware model
projection and retained the repaired distinction between childhood friends and
present friends. Independent literary QC reread the same 68 rows, retained index
`54` exactly, and made fourteen additional local prose improvements without
changing meaning, voice, agency, chronology, or the train coda.

Targeted arbitration found no competing accuracy/literary reading and made no
translation change. The repaired closing block was reread in final form. Exact
joins, hashes, engine IDs, file identity, speaker maps, wrappers, CP932,
narrative gates, word-wrap tests, and public validation pass. No route-I finding
remains open.

## Pass decision and limitations

The I route passes the mandatory critical narrative gate because all 68
permitted rows were read, the sole literary finding is closed, and every
deterministic gate passed.

This was a static artifact readthrough. No runtime build, injection, textbox,
backlog, sprite, CG, background, or in-engine rendering was exercised or
claimed. No translation, QC, configuration, source, pipeline-state, or Git
artifact was modified.
