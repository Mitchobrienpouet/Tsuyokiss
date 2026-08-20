#!/usr/bin/env python3
"""Run the committed longest-line baseline without changing translations."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from tsuyokiss_wrap import GdiMeasurer, PillowMeasurer, layout_message


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("baseline", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--font-file", type=Path)
    args = ap.parse_args()
    source = json.loads(args.baseline.read_text(encoding="utf-8"))
    contract = source["engine_contract"]
    nominal = int(contract["nominal_font_height"])
    minimum = int(contract["minimum_font_height"])
    width = int(contract["physical_width_px"])
    max_lines = int(contract["max_lines_per_page"])
    if args.font_file:
        factory = lambda height: PillowMeasurer(args.font_file, height)
        backend = f"portable-preflight:{args.font_file}"
        authoritative = False
    else:
        factory = lambda height: GdiMeasurer(contract["font_face"], height)
        backend = f"native-gdi:{contract['font_face']}"
        authoritative = True

    results = []
    for case in source["cases"]:
        layout = layout_message(case["text"], factory, width, nominal, minimum, max_lines)
        rebuilt = " ".join(line for page in layout.pages for line in page.lines)
        normalized = " ".join(case["text"].split())
        if rebuilt != normalized:
            raise AssertionError(f"text loss in {case['scene']}:{case['seq']}")
        results.append(
            case
            | {
                "font_height": layout.font_height,
                "page_count": len(layout.pages),
                "pages": [
                    {"lines": list(page.lines), "widths_px": list(page.widths)}
                    for page in layout.pages
                ],
                "status": "PASS",
            }
        )
    report = {
        "schema_version": 1,
        "authoritative": authoritative,
        "backend": backend,
        "contract": contract,
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"cases={len(results)} authoritative={authoritative} output={args.output}")


if __name__ == "__main__":
    main()
