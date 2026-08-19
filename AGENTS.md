# VN translation agent rules

Read every file in `bible/` before touching a translation. Treat
`scratchpad/jp_dumps/` as immutable Japanese source. Write translations only to
`translations/`, QC records only to `qc/`, continuity and contested notes only
to their designated `scratchpad/` directories, and orchestration state only to
`state/`.

Follow the mandatory order: continuity preflight -> translation -> accuracy QC
-> literary QC -> targeted arbitration -> deterministic validation. Preserve
source row indexes exactly and never invent missing text. Accuracy outranks
foreshadowing safety, which outranks voice, which outranks local smoothness.

Read `content_exclusions.json` before every model-backed stage. Model work may
read only generated `scratchpad/model_sources/` projections, never excluded
source rows. Excluded ranges are not translation debt and must stay absent from
translations, QC, arbitration, and builds.

Read `narrative_gates.json` before every model-backed stage. Repeated choices
must remain identical. Translate and fully arbitrate each declared canonical
mirror before deriving its siblings; never independently retranslate shared
Japanese.

Never modify or commit retail archives, binaries, authentication material, or
Codex session files. Never bypass the sandbox. Mark a scene complete only after
its JSON, both QC lenses, arbitration record (including a documented no-op),
and deterministic gates pass.

The supervising agent must create narrow regular GitHub commits and push them
to the intended remote branch: one after each completed preflight shard and one
after each fully gated scene. Verify that the remote contains the exact commit
before calling the work saved. Worker threads must not run concurrent Git
operations. If push or verification fails, record checkpoint debt and stop
claiming new shards; never force-push or rewrite unrelated history.

Honor `required_model` in `codex_pipeline.json`. Never downgrade or silently
substitute a model. Preserve completed work and leave the unavailable stage
blocked until the configured model returns.
