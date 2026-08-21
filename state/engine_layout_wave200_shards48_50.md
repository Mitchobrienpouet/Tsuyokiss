# Engine/layout QA: wave-200 shards 48 and 50

Date: 2026-08-21

## Scope

Static engine/layout gates were run on the six permitted scenes only:

- shard 48: `SC_M0609_00_M0610_00` (29 rows),
  `SC_M0610_00_M0611_00` (37 rows), and
  `SC_M0611_00_M0612_00` (10 rows);
- shard 50: `SC_M0620_00_M0621_00` (50 rows),
  `SC_M0621_00_M0622_00` (10 rows), and
  `SC_M0622_00_M0630_00` (81 rows).

Total: 217 permitted translated messages. Fully excluded sibling scenes and
excluded source rows were not inspected, reconstructed, wrapped, or counted.

## Deterministic text gates

- Exact translation-index coverage against each filtered `model_sources`
  projection: PASS (217/217; no missing or unknown index).
- Strict CP932 encoding: PASS (217/217).
- Dialogue `「...」` wrappers and unwrapped narration by source kind: PASS
  (217/217).
- Forbidden smart typography (`‘’“”–—…`): PASS (zero occurrence).
- Embedded authored CR/LF in logical target messages: PASS (zero occurrence).
- Existing word-boundary, newline-normalization, long-token rejection,
  fourth-line rejection, greedy-fill, and reduce/paginate unit tests:
  PASS (7/7).

## Portable pixel-layout gate

The committed `tools/wordwrap/tsuyokiss_wrap.py` gate was run with the static
project profile documented in `docs/TSUYOKISS_WORDWRAP_REPORT.md`:

- physical width: 659 px;
- conservative reserved margin: 3%;
- effective line limit: 639 px;
- maximum lines per page: 3;
- nominal/minimum font height: 26/23;
- portable backend: Pillow with `/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`.

Result: PASS for portable pre-QA.

- `status=ok`: 217/217;
- rejected unbreakable tokens: 0;
- messages requiring an unproven additional page: 0;
- messages requiring font reduction below 26: 0;
- text loss or non-word-boundary split: 0;
- maximum measured composed-line width: 639/639 px.

| Scene | Messages | 1 line | 2 lines | 3 lines | Max width |
|---|---:|---:|---:|---:|---:|
| `SC_M0609_00_M0610_00` | 29 | 21 | 6 | 2 | 614 px |
| `SC_M0610_00_M0611_00` | 37 | 30 | 7 | 0 | 621 px |
| `SC_M0611_00_M0612_00` | 10 | 4 | 5 | 1 | 638 px |
| `SC_M0620_00_M0621_00` | 50 | 30 | 17 | 3 | 639 px |
| `SC_M0621_00_M0622_00` | 10 | 7 | 3 | 0 | 633 px |
| `SC_M0622_00_M0630_00` | 81 | 53 | 27 | 1 | 638 px |

Three-line messages: `M0609:21`, `M0609:27`, `M0611:8`, `M0620:14`,
`M0620:19`, `M0620:42`, and `M0622:34`.

The tightest portable case is `SC_M0620_00_M0621_00:37`, whose longest
composed line measures exactly 639 px under the fallback metric. It passes the
configured 3% bound but has zero additional portable-metric headroom.

## Limits and remaining debt

This is not native runtime visual QA. The environment is not Windows, native
GDI measurement is unavailable, and the requested `MS UI Gothic` face is not
installed; font substitution would be rejected by the authoritative GDI
backend. DejaVu Sans metrics therefore cannot freeze the final right boundary
or prove glyph positioning in `tkfe.exe`.

Textbox/backlog equivalence, actual `MS UI Gothic` height and width, the exact
right edge, nameplate interaction, and the seven three-line messages still
require native runtime inspection. `M0620:37` is a mandatory edge-case sample.
No scenario injection, FPK repack, or runtime build was performed by this gate.

Final status: portable static engine/layout gates PASS; native GDI/runtime
visual QA remains OPEN and must not be reported as completed.
