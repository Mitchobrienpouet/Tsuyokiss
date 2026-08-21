# Runtime QA feasibility audit

Date: 2026-08-22  
Mode: read-only repository/environment audit; no extraction, injection, repack,
archive read, executable launch, configuration change, or state mutation.  
Result: **NATIVE TEXTBOX, BACKLOG, AND RUNTIME SMOKE QA CANNOT BE EXECUTED NOW.**

Portable static word-wrap analysis is available. It is not a substitute for
native GDI measurement or in-engine visual proof.

## Feasibility decision

| QA activity | Executable now? | Evidence |
| --- | --- | --- |
| Translation JSON/schema/CP932 checks | Yes, statically | Repository validators and unit tests exist. |
| Portable pixel-width preflight | Yes, non-authoritatively | Python 3.12.13, Pillow 12.3.0, and DejaVu Sans are available. |
| Native `MS UI Gothic` GDI measurement | **No** | Host is Linux/posix; the GDI backend explicitly refuses non-Windows hosts; the requested font is absent. |
| Patched scenario build | **No** | No decoded block tree, block manifest, unified current translation JSONL, wrapped JSONL, translated blocks, or patched `data.fpk` exists. |
| Patched UI archive build | **No in this task/current tree** | Three packed UI replacement members exist, but no extracted `chip.fpk` or disposable game tree is present. |
| Game executable launch | **No** | `tkfe.exe` and its game/DLL/config tree are absent; Wine/Proton and a display server are absent. |
| Textbox visual QA | **No** | No launchable patched game, native renderer, display, or capture harness. |
| Backlog/history visual QA | **No** | Same launch blockers; no save/jump harness or backlog capture automation exists. |
| End-to-end smoke test | **No** | No executable environment or complete injection-ready archive set. |

## Current host and runtime evidence

| Requirement | Current evidence | Status |
| --- | --- | --- |
| Host OS | Linux 6.18.35, x86_64, `os.name == "posix"` | Incompatible with the native Win32 GDI backend |
| Windows compatibility runtime | `wine`, `wine64`, `proton`, `protontricks`, and `winetricks` are absent from `PATH` | Missing |
| Headed/headless display | `DISPLAY`, `WAYLAND_DISPLAY`, and `XDG_RUNTIME_DIR` are unset; `Xvfb`, `xvfb-run`, Weston, and Gamescope are absent; no `/dev/dri` device was exposed | Missing |
| Native game font | `MS UI Gothic` is not installed; `fc-match` substitutes DejaVu Sans | Missing |
| Portable fonts | DejaVu Sans and Nimbus Sans Narrow are installed | Available for static preflight/UI generation only |
| Game executable | No `tkfe.exe`, other `.exe`, or game DLL exists in the repository, workspace search, or temporary candidate search | Missing |
| Extracted game install | No game directory, configuration files, save files, or launch scripts exist | Missing |
| Scenario archive candidate | `/tmp/tsuyokiss_data.fpk`, 4,288,677 bytes | Present by metadata only; not opened or modified |
| Full Edition media candidate | `/tmp/Tsuyokiss_Full_Edition.iso`, 4,216,410,112 bytes | Present by metadata only; size matches the manifest baseline; hash not recomputed and image not opened |
| UI/source archives | No extracted `chip.fpk`, `cg.fpk`, or `kg.fpk` exists in the repository, workspace, or temporary search | Missing |
| UI packed replacements | `patch/ui/chip/titlechip.kg.zlc2`, `CGChip.kg.zlc2`, and `EDChip.kg.zlc2` | Present, but cannot be runtime-loaded without `chip.fpk` and a game install |
| Scenario intermediates | No `data_blocks/`, block `manifest.json`, current `.jsonl`, wrapped output, `translated_blocks/`, or patched FPK | Missing |
| Runtime navigation/capture | No prepared saves, scene-jump tool, autoplay harness, screenshot capture tool, or backlog verifier | Missing |

The temporary ISO and `data.fpk` candidates were located using filename and
file-size metadata only. This audit did not mount, extract, hash, parse, copy,
or modify either retail artifact.

## Repository build and injection paths

### 1. Text measurement and wrapping

`tools/wordwrap/tsuyokiss_wrap.py` implements the documented 659 px physical
width, zero-to-three-percent margin, three-line envelope, 26-to-23 px local
font reduction, CP932 encoding checks, and word-boundary-only composition.

- On Windows, `GdiMeasurer` uses Win32 `CreateFontA` and rejects font
  substitution. That path cannot initialize on this posix host.
- With `--font-file`, `PillowMeasurer` provides a portable approximation. The
  committed portable baseline explicitly marks itself `authoritative: false`.
- When a message still needs more than one three-line page, the main wrapper
  marks it `needs_pagination` with `injection_ready: false`, because cloning the
  speaker/voice commands for an additional page has not been proven.

The committed six-case longest-line portable baseline requires two pages for
all six cases at the minimum 23 px size. `run_longest_baseline.py` records these
as static layout PASS cases, but this does not make them scenario-injection
ready. The production wrapper's pagination guard remains a concrete build
blocker unless each affected line is shortened source-faithfully or the
engine's page/speaker/voice command cloning is implemented and proven.

### 2. Scenario extraction and application

`tools/wordwrap/tsuyokiss_scenario.py` can:

- `extract`: turn decoded scenario blocks 0028-0040 into stable JSONL records;
- `apply`: accept only rows with `status == "ok"`, verify each source SHA-256,
  encode CP932, and write translated decoded blocks.

It deliberately stops at decoded blocks. It does not rebuild `data.fpk` and it
does not launch the game. No committed tool currently assembles the repository's
per-scene `translations/*.json` files plus stable IDs/source hashes into the
JSONL shape required by the wrapper and `apply`. Therefore the current
translation corpus is not connected to the scenario applicator by a complete,
committed end-to-end build command.

### 3. Scenario archive repack

`tools/wordwrap/zlc2_decompress.py` can decode the concatenated ZLC2 members and
emit decoded blocks plus a slot manifest. It writes outputs and was not run.

`tools/wordwrap/zlc2_repack_inplace.py` can recompress replacement blocks into
the original slots and write a new output FPK. It correctly rejects a block
that exceeds its original slot. It is a mutating build tool and was not run.
The necessary decoded blocks, slot manifest, translated blocks, and authorized
disposable input archive are not assembled in the current tree.

### 4. UI archive rebuild

`tools/assets/candysoft_assets.py replace-member` rebuilds an encrypted-index
FPK around one already-packed replacement member and validates the rebuilt
index. The three checked-in UI replacements are larger than their retail slots,
so the documented safe path is archive rebuild, not in-place overwrite.

The command was not run. `chip.fpk` is unavailable as an extracted disposable
input, and the repository has no one-shot script that chains all three current
replacement members into a runtime-ready copy and launches it.

### 5. Runtime launch

The repository contains no game launcher, Wine/Proton wrapper, DirectX setup,
runtime dependency manifest, save/jump harness, screenshot protocol, or
automated textbox/backlog comparator. `tools/codex_vn_pipeline.py` orchestrates
translation/QC state; it is not a build or game runtime launcher. Its global
`validate` command calls state initialization, so it was intentionally not run
for this read-only audit.

## Documentation discrepancies

The command examples in `docs/TSUYOKISS_WORDWRAP_REPORT.md` use
`scripts/tsuyokiss_wrap.py`, `scripts/tsuyokiss_scenario.py`, and
`scripts/zlc2_repack_inplace.py`. No `scripts/` directory or those paths exist.
The actual tools are under `tools/wordwrap/`. The underlying workflow is still
understandable, but the example commands are not directly runnable as written.

The report's renderer conclusions are static executable-analysis evidence. It
explicitly leaves native font height, the exact right edge, and textbox/backlog
visual confirmation open; the current environment does not close that debt.

## Concrete prerequisites for native QA

All of the following are needed before textbox, backlog, or smoke testing can
be called executable:

1. An authorized, extracted Full Edition game tree on a disposable writable
   copy, including the verified `tkfe.exe`, `data.fpk`, `chip.fpk`, remaining
   required archives, configuration, and runtime DLLs. Retail originals must
   remain untouched.
2. A native 32-bit Windows environment or a proven Wine/Proton configuration
   capable of running this PE32 DirectX title, including the required D3DX/DirectX
   runtime components.
3. The actual `MS UI Gothic` face installed and verified through the GDI backend
   without substitution.
4. A working display and capture path, plus input automation or a documented
   manual procedure for reaching deterministic scene samples and opening the
   backlog.
5. A committed bridge that joins every current permitted translation line to
   its stable engine ID and source hash, producing wrapper-compatible JSONL.
6. A complete native-GDI wrap pass. All `reject` and `needs_pagination` rows
   must be resolved without truncation, source expansion, or unproven command
   cloning.
7. Decoded scenario blocks and manifest from an authorized disposable
   `data.fpk`, translated blocks produced by the source-hash-checking applicator,
   and a successfully validated patched archive copy.
8. A rebuilt disposable `chip.fpk` containing all three current UI members,
   followed by index/member-integrity verification.
9. Deterministic runtime samples covering the longest dialogue and narration,
   three-line edge cases, punctuation-heavy lines, nameplates, choices,
   voice-replay entries, backlog pages, and the tight 639 px portable case
   `SC_M0620_00_M0621_00:37`.
10. Captures and a result log tied to stable scene/index IDs for both textbox
    and backlog. Visual failures must return to source-faithful translation or
    literary repair rather than blind clipping.

No credential is required or requested by this audit. The blockers are missing
runtime/build inputs and environment capabilities, not authentication.

## Safe commands currently available

These commands do not launch the game or mutate retail archives when used with
the stated outputs:

```bash
# Pure unit tests for word-boundary/layout behavior.
PYTHONDONTWRITEBYTECODE=1 python tools/wordwrap/test_tsuyokiss_wrap.py

# Portable, non-authoritative baseline; output goes to a disposable temp path.
PYTHONDONTWRITEBYTECODE=1 python tools/wordwrap/run_longest_baseline.py \
  qa/wordwrap/longest_baseline.json /tmp/longest_baseline.portable.audit.json \
  --font-file /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf

# Read-only syntax/help inspection of the available CLIs.
PYTHONDONTWRITEBYTECODE=1 python tools/wordwrap/tsuyokiss_wrap.py --help
PYTHONDONTWRITEBYTECODE=1 python tools/wordwrap/tsuyokiss_scenario.py --help
PYTHONDONTWRITEBYTECODE=1 python tools/assets/candysoft_assets.py --help
```

`candysoft_assets.py list <archive>` is read-only at the tool level, but it
would read a retail archive and was not run under this task. Extraction,
scenario application, `replace-member`, `zlc2_repack_inplace.py`, archive
mounting, and executable launch are intentionally outside this audit and must
not be treated as safe inspection commands here.

## Verified and unverified boundary

Verified now:

- repository tool presence and actual CLI paths;
- the static renderer contract already documented from `tkfe.exe` analysis;
- availability of Python/Pillow and portable fonts;
- absence of native GDI, the requested font, Windows runtime layers, display,
  extracted executable/game tree, scenario intermediates, and runtime harness;
- metadata-only presence of the temporary ISO and `data.fpk` candidates;
- existence of the three checked-in packed UI replacement members;
- fail-closed behavior encoded in the wrapper, source-hash applicator, slot
  repacker, and FPK member-rebuild code.

Not verified now:

- the temporary ISO/data archive hashes or contents;
- successful extraction or installation of the retail game;
- launchability under native Windows, Wine, or Proton;
- actual font selection, glyph metrics, right-edge boundary, clipping, alpha
  blending, nameplate width, choice layout, or voice behavior;
- successful construction and loading of current translated `data.fpk` and
  `chip.fpk` copies;
- textbox/backlog equivalence in the engine;
- any runtime smoke-test result or screenshot.

Final boundary: static preflight can continue, but **no native textbox,
backlog, UI, or end-to-end runtime QA claim is currently supportable**.
