# Final J-lane translation handoff

Stage: translation only.

Authoritative inputs:

- `state/preflight_final_J_20260821.md`
- the four certified `scratchpad/model_sources/SC_J*.json` projections
- project bible, merged exclusions, and narrative gates

No raw source, model projection, exclusion, gate, configuration, state,
accuracy QC, literary QC, arbitration, readthrough, or Git artifact was edited.

## Files and exact coverage

| Translation | Required indexes | Rows |
|---|---|---:|
| `translations/SC_J0100_16_J0100_20.json` | `1-14` | 14 |
| `translations/SC_J0100_17_J0100_20.json` | `1-9` | 9 |
| `translations/SC_J0100_18_J0100_20.json` | `1-16` | 16 |
| `translations/SC_J0100_20_Z9999_99.json` | `1-127` | 127 |
| **Total** | four exact contiguous sets | **166** |

All four scenes have zero excluded rows. The three short answer branches remain
distinct and converge on the common `J0100_20` scene without an invented bridge.

## Translation locks carried forward

- The incorrect Erika and Inori branches end badly for Leo; only the Nagomi
  branch gives him Otome and Erika's praise.
- The apparent Nagomi is Honami in disguise. The real Nagomi appears only as
  Mecha Takane's captive in the common scene.
- `声` remains `Voice` at `J0100_20:53-54`; `Hinano` appears only with the
  explicit `雛乃` speaker tag at `57`.
- Poem stays sparse and deadpan; Honami theatrical; Serori hyperactive and
  catlike; Takane haughty; Hinano grandiose; Kaname cool; Yoshimi's colder beat
  remains unexplained.
- `Coconut`, `Crab`, `Princess`, `Fukahire`, `Mecha Takane`, `Ice Lawyer`, and
  Sunao's crest catchphrase follow prior locks.
- `イガグリ` uses speaker-map name `Igaguri`, not the drifting legacy
  `Burrhead` alternative.
- The explosion and Shinichi's interrupted disrobing remain brief,
  non-graphic slapstick.

## Contested permitted readings for independent QC

- `J0100_16:3` / `J0100_18:4`: adopted `Ahn, ... wrooong! ☆` for the
  deliberately glamorous game-show wrong-answer call. `Wrong answer!` is a
  defensible flatter alternative, but would weaken the shared reveal gag.
- `J0100_17:6`: adopted `Sharp... very sharp indeed!` for `シブい`, praising
  Leo's perceptive answer. Literal taste language is not viable here; `Cool`
  remains a possible tonal alternative.
- `J0100_20:4`: adopted `Poepoe` as the direct phonetic nickname `ぽえぽえ` while
  retaining `Poem` in the speaker map and ordinary address.
- `J0100_20:45`: adopted `take out` for ruby-marked `殺（と）らせて`, retaining
  competitive target-claiming and the dark written undertone without asserting
  an actual killing.
- `J0100_20:55-56`: retained `Kaname-nee` and `Hinano-neesan` because the sister
  hierarchy is explicit and character-relevant. Naturalized `Big Sis Kaname /
  Hinano` remains a literary alternative.
- `J0100_20:66-67`: adapted the `コカン / 沽券` malapropism as `privates / pride`.
  This preserves the mistaken anatomical word and Takane's immediate
  correction without expanding the joke.
- `J0100_20:80`: adopted unwrapped narration `Sato... san?` to make Leo's sudden
  fearful formality visible. `Ms. Sato...?` is more idiomatic but less
  consistent with established in-script address.
- `J0100_20:110`: retained only `their little brother`; no identity was inferred.
- `J0100_20:119`: used `You're making my crest stand on end!` for Sunao's
  recurring `トサカ来る` catchphrase rather than generic anger.

Blocking contested readings: NONE.

## Deterministic self-check

PASS (`166/166`):

- exact key sets `1-14`, `1-9`, `1-16`, and `1-127`;
- complete and exact speaker-map source-key coverage;
- dialogue/narration wrapper parity on every row;
- valid source hashes and 166 unique nonempty engine IDs on model-source joins;
- CP932 encodability and no forbidden smart typography or manual line breaks;
- zero missing, unknown, or excluded rows;
- zero applicable mirror or repeated-choice gates;
- branch-outcome, `Voice` / `Hinano`, unnamed-brother, and crest-catchphrase
  sentinels all preserved.
