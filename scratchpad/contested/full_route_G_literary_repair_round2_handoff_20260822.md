# Route G targeted literary repair round 2 - 2026-08-22

## Scope and result

Stage: targeted post-recertification translation repair only

Status: **COMPLETED**

This round resolves only the residual literary findings recorded in the
current reports for `SC_G0800_00_G0850_00` and
`SC_G0870_00_G0900_00`. It changes seven permitted translation rows:
G0800 `60` and G0870 `2, 26, 74-76, 192`.

No excluded row was inspected, reconstructed, summarized, or bridged.
In particular, G0870 `192` remains an independent permitted line after the
opaque exclusion at `191`. No QC, readthrough, state, configuration, source,
pipeline, or Git artifact was edited.

## SC_G0800_00_G0850_00

| Index | Before | After | Reason |
| ---: | --- | --- | --- |
| `60` | `Living with Yoshimi went by without any particular problems.` | `I lived with Yoshimi without any particular problems.` | Removes the unidiomatic gerund/`went by` collocation while preserving the source statement that the cohabitation proceeded without problems. |

## SC_G0870_00_G0900_00

| Index | Before | After | Reason |
| ---: | --- | --- | --- |
| `2` | `「What are you saying now?! You're the one who called me a people-hater, Leo!」` | `「How can you say that now?! You're the one who called me a people-hater, Leo!」` | Gives Yoshimi's heated `何を今さら` retort natural English without changing her callback to Leo's earlier label. |
| `26` | `「But forget that. Just tell me now. Why did you become so unable to trust people?」` | `「But forget that. Just tell me now. What made you stop trusting people like this?」` | Removes the translationese `become so unable` construction while preserving Leo's question about the change in Yoshimi. |
| `74` | `「Leo... You're strange...」` | `「Leo... You really do have strange tastes...」` | Restores the `物好き` setup as Yoshimi's remark about Leo's strange tastes. |
| `75` | `「I don't know whether I'm strange, but I do know I like you.」` | `「I don't know if my tastes are strange, but I do know I like you.」` | Audibly carries the `strange tastes` setup into Leo's `like you` turn, preserving the source `物好き / 好き` joke without adding a new proposition. |
| `76` | `「That wasn't clever at all.」` | `「That was terrible.」` | Gives Yoshimi's immediate rejection of the bad wordplay a short natural punchline without explaining the joke. |
| `192` | `「Yoshimi, don't decide that in advance. We don't know yet.」` | `「Don't jump to conclusions, Yoshimi. We don't know yet.」` | Renders `決め付けるな` idiomatically while remaining neutral about the opaque excluded row `191`. |

## Preservation locks

- The 41 first-round literary repairs and five intentionally full G0760 forms
  remain unchanged.
- Accuracy sentinels G0760 `32, 54`, G0800 `54, 77, 96`, and G0870
  `66, 102, 119, 127, 144, 187` remain unchanged.
- Exact sparse indexes, dialogue wrappers, speaker maps, source metadata,
  engine IDs, and all exclusion gaps remain intact.

## Deterministic validation

| Gate | Result |
| --- | --- |
| Strict JSON and duplicate keys | **PASS** |
| Exact projection joins | **PASS**: G0800 `408/408`; G0870 `190/190` |
| Source hashes and engine IDs | **PASS**: `598/598` |
| Translation file identity and speaker maps | **PASS** |
| Dialogue/narration wrappers and controls | **PASS** |
| Excluded-key absence | **PASS** |
| CP932 and forbidden typography | **PASS** |
| Targeted new-text and stale-form sentinels | **PASS** |
| Public overlay-aware validator | **PASS**: `408/408`, `190/190` |

Runtime rendering, textbox fit, backlog behavior, timing, sprites, CGs, and
other visual state were not tested in this static repair stage.
