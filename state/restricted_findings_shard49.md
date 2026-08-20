# Restricted findings — shard 49

STATUS: BLOCKED BEFORE SPEC / TRANSLATION

The prepared model projections contain unfiltered explicit or sexualized
material involving high-school students. Fail-closed review stopped before any
shard spec, translation, QC, or arbitration artifact was created.

## Exact ranges

- `SC_E0780_00_E0790_00:1-538` — continuous explicit sexual scene and immediate
  aftermath involving Leo and first-year student Nagomi, including stripping,
  genital description and contact, intercourse, ejaculation, and repeated sex.
  The entire projection is restricted.
- `SC_E0790_00_E0795_00:78-82` — erotic kissing followed by Leo's stated desire
  to push Nagomi down.
- `SC_E0790_00_E0795_00:95-118` — Leo explicitly labels a harassment test, then
  fondles Nagomi's buttocks and breasts while she cooks and treats her reaction
  as permission for further harassment.
- `SC_E0790_00_E0795_00:206-224` — explicitly escalated harassment test involving
  shared bathing, undressing in front of Leo, nudity embarrassment, and Leo's
  conclusion that Nagomi will permit anything.
- `SC_E0790_00_E0795_00:240-246` — prolonged erotic kissing used to demonstrate
  the high-school student's degree of romantic/sexual devotion.
- `SC_E0795_00_E0795_10:1-5` — shared-bath setup explicitly fetishizing Nagomi's
  school swimsuit; the entire projection is restricted.
- `SC_E0795_20_E0795_40:1-33` — continuation of the shared bath in the school
  swimsuit, including infantilized commands/praise and a request to wash Leo's
  back again; the entire projection remains sexualized in context.

## Required remediation

Add the exact ranges above to `content_exclusions.json`, validate the manifest,
and regenerate all affected `scratchpad/model_sources/` projections before the
shard is resumed. Re-read the regenerated projections in full and repeat the
fail-closed check for any additional restricted material.
