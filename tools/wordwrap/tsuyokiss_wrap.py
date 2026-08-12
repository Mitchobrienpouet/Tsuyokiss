#!/usr/bin/env python3
"""Pixel-accurate, word-boundary-only wrapping gate for Tsuyokiss FE.

On Windows the default backend uses the same ANSI/GDI metrics that underlie
ID3DXFont.  A Pillow font file can be supplied for portable/offline QA.
"""

from __future__ import annotations

import argparse
import ctypes
import json
import math
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


TOKEN_RE = re.compile(r"\S+(?:\s+|$)")


class Measurer(Protocol):
    def width(self, text: str) -> int: ...


class GdiMeasurer:
    """Measure CP932 strings with a Win32 ANSI font."""

    def __init__(self, face: str, height: int, weight: int = 400) -> None:
        if os.name != "nt":
            raise RuntimeError("the GDI backend is available only on Windows")
        gdi = ctypes.windll.gdi32
        self._gdi = gdi
        self._dc = gdi.CreateCompatibleDC(0)
        if not self._dc:
            raise OSError("CreateCompatibleDC failed")
        # D3DXCreateFontA parameters recovered from tkfe.exe: width 0,
        # weight 400, mip 1, italic false, SHIFTJIS_CHARSET (128),
        # output precision 0, quality 1, pitch/family 3 or 4.
        self._font = gdi.CreateFontA(
            height, 0, 0, 0, weight, 0, 0, 0, 128, 0, 0, 1, 3,
            face.encode("cp932"),
        )
        if not self._font:
            gdi.DeleteDC(self._dc)
            raise OSError("CreateFontA failed")
        self._old = gdi.SelectObject(self._dc, self._font)

    def width(self, text: str) -> int:
        raw = text.encode("cp932", errors="strict")
        size = (ctypes.c_long * 2)()
        if not self._gdi.GetTextExtentPoint32A(self._dc, raw, len(raw), size):
            raise OSError("GetTextExtentPoint32A failed")
        return int(size[0])

    def close(self) -> None:
        if getattr(self, "_dc", 0):
            self._gdi.SelectObject(self._dc, self._old)
            self._gdi.DeleteObject(self._font)
            self._gdi.DeleteDC(self._dc)
            self._dc = 0

    def __del__(self) -> None:
        self.close()


class PillowMeasurer:
    def __init__(self, path: Path, size: int) -> None:
        from PIL import ImageFont

        self.font = ImageFont.truetype(str(path), size=size)

    def width(self, text: str) -> int:
        return math.ceil(self.font.getlength(text))


@dataclass(frozen=True)
class WrapResult:
    lines: tuple[str, ...]
    widths: tuple[int, ...]
    limit_px: int

    @property
    def max_fill(self) -> float:
        return max(self.widths, default=0) / self.limit_px


def wrap_words(text: str, measurer: Measurer, limit_px: int, max_lines: int = 3) -> WrapResult:
    """Wrap without ever splitting a non-whitespace token.

    Dynamic programming minimizes raggedness while heavily penalizing extra
    lines. Existing CR/LF are treated as authoring layout and normalized to
    spaces; message boundaries belong in separate input records.
    """
    normalized = re.sub(r"\s+", " ", text).strip()
    if not normalized:
        return WrapResult((), (), limit_px)
    words = normalized.split(" ")
    for word in words:
        if measurer.width(word) > limit_px:
            raise ValueError(f"unbreakable token exceeds {limit_px}px: {word!r}")

    n = len(words)
    widths: dict[tuple[int, int], int] = {}
    for i in range(n):
        for j in range(i + 1, n + 1):
            widths[i, j] = measurer.width(" ".join(words[i:j]))
            if widths[i, j] > limit_px:
                break

    # state: (word index, lines used) -> (cost, previous index)
    states: list[dict[int, tuple[int, int | None]]] = [{0: (0, None)}]
    for used in range(1, max_lines + 1):
        cur: dict[int, tuple[int, int | None]] = {}
        for start, (cost, _) in states[-1].items():
            for end in range(start + 1, n + 1):
                width = widths.get((start, end), limit_px + 1)
                if width > limit_px:
                    break
                # Last-line whitespace is not "lost textbox"; only the
                # conservative safety margin is. Still prefer balanced rows.
                penalty = 0 if end == n else (limit_px - width) ** 2
                candidate = cost + penalty
                if end not in cur or candidate < cur[end][0]:
                    cur[end] = (candidate, start)
        states.append(cur)
        if n in cur:
            break
    else:
        raise ValueError(f"message needs more than {max_lines} lines")

    used = next(i for i in range(1, len(states)) if n in states[i])
    cuts = [n]
    end = n
    while used:
        start = states[used][end][1]
        assert start is not None
        cuts.append(start)
        end, used = start, used - 1
    cuts.reverse()
    lines = tuple(" ".join(words[cuts[i]:cuts[i + 1]]) for i in range(len(cuts) - 1))
    return WrapResult(lines, tuple(measurer.width(line) for line in lines), limit_px)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", type=Path, help="UTF-8 JSONL; each row needs id and text")
    ap.add_argument("output", type=Path)
    ap.add_argument("--width", type=int, default=659, help="physical text width in pixels")
    ap.add_argument("--margin", type=float, default=0.0, help="reserved fraction, 0..0.03")
    ap.add_argument("--lines", type=int, default=3)
    ap.add_argument("--face", default="MS UI Gothic")
    ap.add_argument("--height", type=int, default=26)
    ap.add_argument("--font-file", type=Path, help="portable QA backend instead of native GDI")
    args = ap.parse_args()
    if not 0 <= args.margin <= 0.03:
        ap.error("--margin must be between 0 and 0.03")
    limit = math.floor(args.width * (1 - args.margin))
    if args.font_file:
        measurer: Measurer = PillowMeasurer(args.font_file, args.height)
        backend = f"pillow:{args.font_file}"
    else:
        measurer = GdiMeasurer(args.face, args.height)
        backend = f"gdi:{args.face}"

    failures = 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temp = args.output.with_suffix(args.output.suffix + ".partial")
    with args.input.open(encoding="utf-8") as src, temp.open("w", encoding="utf-8", newline="\n") as dst:
        for lineno, raw in enumerate(src, 1):
            if not raw.strip():
                continue
            row = json.loads(raw)
            try:
                result = wrap_words(str(row["text"]), measurer, limit, args.lines)
                row.update(
                    wrapped="\r\n".join(result.lines),
                    wrap_lines=list(result.lines),
                    widths_px=list(result.widths),
                    status="ok",
                )
            except (KeyError, UnicodeError, ValueError) as exc:
                failures += 1
                row.update(status="reject", error=str(exc), source_line=lineno)
            row["wrap_contract"] = {
                "physical_width_px": args.width,
                "limit_px": limit,
                "reserved_fraction": args.margin,
                "max_lines": args.lines,
                "backend": backend,
            }
            dst.write(json.dumps(row, ensure_ascii=False) + "\n")
    os.replace(temp, args.output)
    print(f"rows written to {args.output}; rejected={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
