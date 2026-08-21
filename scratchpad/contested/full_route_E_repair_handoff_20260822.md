# Full-route E targeted repair handoff (2026-08-22)

## Scope and result

- Input findings: `E-RT-001` through `E-RT-003` in `scratchpad/readthrough/full_route_E_critical_20260822.md`.
- Result: all three findings adopted and resolved.
- Translation impact: 7 JSON files, 9 line values, and 2 `speaker_map` values.
- Continuity impact: 2 directly contradictory local specs reconciled with the established locks.
- Contested permitted readings: NONE. Each repair follows the filtered projection evidence and the supervisor-approved terminology decision.

## Translation line repairs

| Finding | Translation file | Index | Before | After |
|---|---|---:|---|---|
| E-RT-003 | `SC_E0490_00_E0500_00.json` | 39 | `「That is the launch site for the fireworks at Matsukasa's Port-Opening Festival.」` | `「That is the launch site for the fireworks at the Matsukasa Port Opening Festival.」` |
| E-RT-003 | `SC_E0560_00_E0570_00.json` | 59 | `「Well, everyone. Shall we cheerfully prepare for the Athletics and Martial Arts Festival?」` | `「Well, everyone. Shall we cheerfully prepare for the Sports and Martial Arts Festival?」` |
| E-RT-003 | `SC_E0560_00_E0570_00.json` | 71 | `「Ryuumeikan's famous Athletics and Martial Arts Festival is a huge two-day event. It's a local attraction big enough for local TV stations to come.」` | `「Ryuumeikan's famous Sports and Martial Arts Festival is a huge two-day event. It's a local attraction big enough for local TV stations to come.」` |
| E-RT-001 | `SC_E0580_00_E0590_00.json` | 41 | `Yashi left with Touka.` | `Yashi left with Tonfa.` |
| E-RT-003 | `SC_E0580_00_E0590_00.json` | 72 | `「...The Athletics and Martial Arts Festival is a points competition between the North, South, East, and West Armies.」` | `「...The Sports and Martial Arts Festival is a points competition between the North, South, East, and West Armies.」` |
| E-RT-003 | `SC_E0590_00_E0600_00.json` | 1 | `The Athletics and Martial Arts Festival--` | `The Sports and Martial Arts Festival--` |
| E-RT-001 | `SC_E0700_00_E0710_00.json` | 167 | `But even Touka had given up on working there, so we couldn't let our guard down.` | `But even Tonfa had given up on working there, so we couldn't let our guard down.` |
| E-RT-003 | `SC_E0710_00_E0720_00.json` | 1 | `--The Matsukasa Port Opening Anniversary Festival.` | `--The Matsukasa Port Opening Festival.` |
| E-RT-002 | `SC_E0910_00_E0920_00.json` | 47 | `「Victory!」 The smile of someone who has accomplished her mission.` | `「Hmph, victory! (← triumphant smile)」` |

E0910:47 now keeps the scoff, victory cry, and comic direction inside one dialogue wrapper, matching the filtered row's dialogue kind and meaning.

## Speaker-map repairs

| Translation file | Map key | Before | After | Permitted rows whose displayed speaker is affected |
|---|---|---|---|---|
| `SC_E0580_00_E0590_00.json` | `豆花` | `Touka` | `Tonfa` | 30, 31, 33 |
| `SC_E0700_00_E0710_00.json` | `豆花` | `Touka` | `Tonfa` | 124, 130, 132, 135, 141, 143, 145, 147, 148, 150, 152, 154, 159 |

The lock is grounded by the explicit filtered-projection reading already rendered as `Yang Tonfa` at `SC_E0560_00_E0570_00:60`.

## Directly contradictory continuity locks reconciled

- `scratchpad/specs/SC_E0580_00_E0590_00-SC_E0590_00_E0600_00-SC_E0600_10_E0610_00-SC_E0600_20_E0610_00.md`
  - Replaced the local `Touka` speaker/voice lock with `Tonfa`.
  - Replaced the official-title summary wording with `Sports and Martial Arts Festival`.
- `scratchpad/specs/SC_E0700_00_E0710_00-SC_E0710_00_E0720_00-SC_E0720_00_E0730_00-SC_E0730_00_E0740_00.md`
  - Replaced the local `Touka` speaker lock with `Tonfa`.
  - Split the event lock by exact source form: `松笠開国記念祭` remains `Matsukasa Port Opening Anniversary Festival` at E0700:141; `まつかさ開国祭` is `Matsukasa Port Opening Festival`; shortened `開国祭` is `Port Opening Festival`.

Protected non-change: `SC_E0700_00_E0710_00:141` remains `「You know the Matsukasa Port Opening Anniversary Festival, yes?」` because its permitted source uses the distinct anniversary form.

## Deterministic validation

- Strict JSON and duplicate-key load: PASS for all 81 route-E translations and projections.
- Exact filtered joins: PASS, 81/81 scenes and 8,893/8,893 permitted rows; no missing or extra indexes.
- Internal `file` identity: PASS for all 81 route-E translations.
- Projection metadata: PASS; each `translatable_count` equals its row count, each engine ID names its scene, and every source hash is a 64-character lowercase SHA-256 value.
- Dialogue wrappers: PASS, 0 kind/wrapper mismatches across 8,893 rows; E0910:47 is now fully wrapped.
- CP932 and forbidden typography: PASS for every translated line, every speaker-map value, and both edited specs. The left arrow in E0910:47 is CP932-safe.
- Stale route-E forms: PASS. Zero `Touka`, zero `Athletics and Martial Arts Festival`, and zero `Port-Opening Festival` occurrences remain in route-E translations or route-E specs.
- Event distinction: PASS. `Matsukasa Port Opening Anniversary Festival` remains exactly once in route-E translations, at E0700:141.

No QC, arbitration, readthrough report, source/projection, exclusion, config, pipeline/state, or Git artifact was changed.
