# Restricted findings — shard 43

STATUS: BLOCKED BEFORE SPEC / TRANSLATION

The regenerated model projection still contains sexualized material involving
high-school students. Fail-closed review stopped before any shard spec,
translation, QC, or arbitration artifact was created.

## Exact ranges

- `SC_E0580_00_E0590_00:6-8` — Shinichi, Leo, and Subaru explicitly compare
  their genitals through weapon metaphors and describe them as tools for
  intimidating women. The speakers are high-school students.
- `SC_E0580_00_E0590_00:45-49` — Erika drops and identifies a coercive kit of
  rope, duct tape, a handheld camera, and candles that she intended to use to
  force Nagomi's cooperation; the surrounding narration confirms Nagomi was
  fortunate to comply before it was used. Both are high-school students, and
  the bondage/voyeuristic staging is sexualized.

## Required remediation

Add the exact ranges above to `content_exclusions.json`, validate the manifest,
and regenerate `scratchpad/model_sources/SC_E0580_00_E0590_00.json` before the
shard is resumed. Re-read the regenerated projection in full and repeat the
fail-closed check for any further unfiltered restricted material.
