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
from typing import Callable, Protocol


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
        actual = ctypes.create_string_buffer(128)
        if not gdi.GetTextFaceA(self._dc, len(actual), actual):
            self.close()
            raise OSError("GetTextFaceA failed")
        actual_face = actual.value.decode("cp932", errors="replace")
        if actual_face.casefold() != face.casefold():
            self.close()
            raise RuntimeError(f"font substitution rejected: requested {face!r}, got {actual_face!r}")

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


@dataclass(frozen=True)
class Page:
    lines: tuple[str, ...]
    widths: tuple[int, ...]


@dataclass(frozen=True)
class LayoutResult:
    pages: tuple[Page, ...]
    font_height: int
    limit_px: int


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _greedy_lines(text: str, measurer: Measurer, limit_px: int) -> tuple[tuple[str, ...], tuple[int, ...]]:
    """Fill every line maximally without splitting a whitespace-delimited token."""
    normalized = _normalize(text)
    if not normalized:
        return (), ()
    words = normalized.split(" ")
    lines: list[str] = []
    widths: list[int] = []
    at = 0
    while at < len(words):
        if measurer.width(words[at]) > limit_px:
            raise ValueError(f"unbreakable token exceeds {limit_px}px: {words[at]!r}")
        end = at + 1
        while end < len(words):
            candidate = " ".join(words[at:end + 1])
            if measurer.width(candidate) > limit_px:
                break
            end += 1
        line = " ".join(words[at:end])
        lines.append(line)
        widths.append(measurer.width(line))
        at = end
    return tuple(lines), tuple(widths)


def wrap_words(text: str, measurer: Measurer, limit_px: int, max_lines: int = 3) -> WrapResult:
    """Wrap without ever splitting a non-whitespace token.

    Dynamic programming minimizes raggedness while heavily penalizing extra
    lines. Existing CR/LF are treated as authoring layout and normalized to
    spaces; message boundaries belong in separate input records.
    """
    lines, widths = _greedy_lines(text, measurer, limit_px)
    if len(lines) > max_lines:
        raise ValueError(f"message needs more than {max_lines} lines")
    return WrapResult(lines, widths, limit_px)


def layout_message(
    text: str,
    measurer_for_height: Callable[[int], Measurer],
    limit_px: int,
    nominal_height: int,
    minimum_height: int,
    max_lines: int = 3,
) -> LayoutResult:
    """Reduce only when needed, then paginate at the minimum permitted size."""
    if minimum_height > nominal_height:
        raise ValueError("minimum font height exceeds nominal height")
    chosen_height = nominal_height
    chosen_lines: tuple[str, ...] = ()
    chosen_widths: tuple[int, ...] = ()
    for height in range(nominal_height, minimum_height - 1, -1):
        measurer = measurer_for_height(height)
        lines, widths = _greedy_lines(text, measurer, limit_px)
        chosen_height, chosen_lines, chosen_widths = height, lines, widths
        if len(lines) <= max_lines:
            break
    pages = tuple(
        Page(chosen_lines[i:i + max_lines], chosen_widths[i:i + max_lines])
        for i in range(0, len(chosen_lines), max_lines)
    )
    return LayoutResult(pages, chosen_height, limit_px)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", type=Path, help="UTF-8 JSONL; each row needs id and text")
    ap.add_argument("output", type=Path)
    ap.add_argument("--width", type=int, default=659, help="physical text width in pixels")
    ap.add_argument("--margin", type=float, default=0.0, help="reserved fraction, 0..0.03")
    ap.add_argument("--lines", type=int, default=3)
    ap.add_argument("--face", default="MS UI Gothic")
    ap.add_argument("--height", type=int, default=26)
    ap.add_argument("--min-height", type=int, default=23)
    ap.add_argument("--font-file", type=Path, help="portable QA backend instead of native GDI")
    args = ap.parse_args()
    if not 0 <= args.margin <= 0.03:
        ap.error("--margin must be between 0 and 0.03")
    limit = math.floor(args.width * (1 - args.margin))
    if args.min_height > args.height:
        ap.error("--min-height must not exceed --height")
    if args.font_file:
        factory = lambda height: PillowMeasurer(args.font_file, height)
        backend = f"pillow:{args.font_file}"
    else:
        factory = lambda height: GdiMeasurer(args.face, height)
        backend = f"gdi:{args.face}"

    failures = 0
    pagination_blocked = 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temp = args.output.with_suffix(args.output.suffix + ".partial")
    with args.input.open(encoding="utf-8") as src, temp.open("w", encoding="utf-8", newline="\n") as dst:
        for lineno, raw in enumerate(src, 1):
            if not raw.strip():
                continue
            row = json.loads(raw)
            try:
                result = layout_message(
                    str(row["text"]), factory, limit, args.height, args.min_height, args.lines
                )
                pages = [
                    {"lines": list(page.lines), "widths_px": list(page.widths)}
                    for page in result.pages
                ]
                row.update(font_height=result.font_height, pages=pages)
                if len(result.pages) == 1:
                    row.update(
                        wrapped="\r\n".join(result.pages[0].lines),
                        wrap_lines=list(result.pages[0].lines),
                        widths_px=list(result.pages[0].widths),
                        status="ok",
                    )
                else:
                    pagination_blocked += 1
                    row.update(
                        status="needs_pagination",
                        pagination_contract={
                            "backlog_entry_per_page": True,
                            "repeat_speaker": True,
                            "repeat_voice_replay": True,
                            "injection_ready": False,
                            "reason": "engine voice/speaker command cloning not yet proven",
                        },
                    )
            except (KeyError, UnicodeError, ValueError) as exc:
                failures += 1
                row.update(status="reject", error=str(exc), source_line=lineno)
            row["wrap_contract"] = {
                "physical_width_px": args.width,
                "limit_px": limit,
                "reserved_fraction": args.margin,
                "max_lines": args.lines,
                "nominal_font_height": args.height,
                "minimum_font_height": args.min_height,
                "backend": backend,
            }
            dst.write(json.dumps(row, ensure_ascii=False) + "\n")
    os.replace(temp, args.output)
    print(
        f"rows written to {args.output}; rejected={failures}; "
        f"pagination_not_injectable={pagination_blocked}"
    )
    if failures:
        return 1
    return 2 if pagination_blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())
