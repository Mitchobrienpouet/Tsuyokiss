# Global route-A wrapper repair handoff

Date: 2026-08-22

Scope: the ten supervisor-listed wrapper defects. The exact index list spans
nine translation JSON files (not eight); the supervisor confirmed that the
index list is authoritative.

Result: COMPLETE. Only the dialogue envelope changed. No proposition, voice,
speaker, index, metadata field, or non-target line was altered.

## Adopted repairs

| Scene/index | Before | After | Reason |
| --- | --- | --- | --- |
| `SC_A0120_85_A0120_90:25` | `「Whoa, she's gorgeous.」 (He never misses that sort of thing.)` | `「Whoa, she's gorgeous. (He never misses that sort of thing.)」` | Keeps the spoken aside and its source stage direction inside one complete dialogue envelope. |
| `SC_A0130_60_A0130_70:26` | `She muttered, 「He forgot me?」` | `「She muttered, "He forgot me?"」` | Places the complete displayed dialogue body inside one outer envelope; straight inner quotation marks preserve the embedded utterance without nested corner wrappers. |
| `SC_A0130_70_A0130_80:5` | `(She sure talks a lot.)` | `「(She sure talks a lot.)」` | Restores the source dialogue wrapper around the complete parenthetical body. |
| `SC_A0130_70_A0130_80:6` | `(Yeah. Loves lectures, loves talking. Not my kind of person.)` | `「(Yeah. Loves lectures, loves talking. Not my kind of person.)」` | Restores the source dialogue wrapper around the complete parenthetical body. |
| `SC_A0150_80_A0150_90:24` | `(That's just you.)` | `「(That's just you.)」` | Restores the source dialogue wrapper around the complete parenthetical body. |
| `SC_A0150_90_A0160_00:8` | `(Even though she's that dark?!)` | `「(Even though she's that dark?!)」` | Restores the source dialogue wrapper around the complete parenthetical body. |
| `SC_A0200_50_A0200_60:6` | `「...」 (Glare.)` | `「... (Glare.)」` | Moves the source stage direction inside the same complete dialogue envelope. |
| `SC_A0210_40_A0210_50:3` | `(Oh, crap!)` | `「(Oh, crap!)」` | Restores the source dialogue wrapper around the complete parenthetical body. |
| `SC_A0220_40_A0220_50:4` | `「Hahahaha.」 (A strangely hollow laugh.)` | `「Hahahaha. (A strangely hollow laugh.)」` | Keeps the laugh and its source stage direction inside one complete dialogue envelope. |
| `SC_A0230_80_A0230_90:7` | `「...」 (Blushing.)` | `「... (Blushing.)」` | Moves the source stage direction inside the same complete dialogue envelope. |

## Files changed

- `translations/SC_A0120_85_A0120_90.json`
- `translations/SC_A0130_60_A0130_70.json`
- `translations/SC_A0130_70_A0130_80.json`
- `translations/SC_A0150_80_A0150_90.json`
- `translations/SC_A0150_90_A0160_00.json`
- `translations/SC_A0200_50_A0200_60.json`
- `translations/SC_A0210_40_A0210_50.json`
- `translations/SC_A0220_40_A0220_50.json`
- `translations/SC_A0230_80_A0230_90.json`
- `scratchpad/contested/global_A_wrapper_repair_handoff_20260822.md`

## Deterministic validation

| Gate | Result |
| --- | --- |
| Active exclusions | PASS - none of the nine scenes or ten indexes is excluded by the canonical manifest or active overlay |
| Strict JSON / duplicate keys | PASS - 9/9 translation files |
| Public overlay-aware per-scene validator | PASS - 9/9 scenes; exact joins and file identities; exit 0 |
| Exact after-text sentinels | PASS - 10/10 |
| Complete unique target envelopes | PASS - every repaired target starts with one `「`, ends with one `」`, and contains no second corner-wrapper pair |
| Nine-scene wrapper structure | PASS - 181 wrapper-bearing rows across 248 rows; zero partial, trailing, or multiple corner-wrapper defects |
| CP932 | PASS - every line and speaker-map value in all nine files |
| Pipeline state | PASS - `state/pipeline.json` remained byte-for-byte unchanged during targeted public validation |

No QC, readthrough, state, configuration, source, exclusion, pipeline, or Git
artifact was modified.
