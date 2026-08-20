#!/usr/bin/env python3
"""Render the English CG gallery category buttons at retail geometry."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from candysoft_assets import decode_zlc2, encode_zlc2, image_to_kg, kg_to_image


FONT = Path("/usr/share/fonts/opentype/urw-base35/NimbusSansNarrow-Bold.otf")
STATE_COLORS = (
    ((72, 90, 156, 255), (255, 255, 255, 255)),
    ((255, 150, 105, 255), (255, 255, 255, 255)),
    ((238, 101, 120, 255), (255, 255, 255, 255)),
    ((255, 255, 255, 255), (255, 121, 156, 255)),
)
BUTTON_WIDTH = 123
BUTTON_HEIGHT = 35


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fit_font(text: str, maximum: int) -> ImageFont.FreeTypeFont:
    for size in range(24, 14, -1):
        font = ImageFont.truetype(str(FONT), size=size)
        left, _, right, _ = font.getbbox(text, stroke_width=1)
        if right - left <= maximum:
            return font
    raise ValueError(f"CG category does not fit its retail button: {text!r}")


def restore_button_interior(image: Image.Image, x0: int, y0: int) -> None:
    """Remove the Japanese glyphs while retaining the retail button gradient."""
    pixels = image.load()
    for y in range(y0 + 4, y0 + 31):
        background = Counter(pixels[x, y] for x in range(x0 + 5, x0 + 118)).most_common(1)[0][0]
        for x in range(x0 + 5, x0 + 118):
            pixels[x, y] = background


def localize(
    source: Path,
    translations: Path,
    png_output: Path,
    kg_output: Path,
    zlc2_output: Path,
    qa_output: Path,
) -> None:
    source_bytes = source.read_bytes()
    image = kg_to_image(source_bytes)
    if image.size != (1024, 1024) or image.mode != "RGBA":
        raise ValueError(f"unexpected CGChip canvas: {image.size} {image.mode}")
    original = image.copy()
    copy = json.loads(translations.read_text(encoding="utf-8"))
    categories = copy["categories"]
    if len(categories) != 10:
        raise ValueError("CGChip requires exactly ten category labels")

    allowed = Image.new("1", image.size, 0)
    allowed_draw = ImageDraw.Draw(allowed)
    for row, item in enumerate(categories):
        y0 = row * BUTTON_HEIGHT
        for state, (fill, stroke) in enumerate(STATE_COLORS):
            x0 = state * BUTTON_WIDTH
            restore_button_interior(image, x0, y0)
            font = fit_font(item["en"], BUTTON_WIDTH - 12)
            ImageDraw.Draw(image).text(
                (x0 + BUTTON_WIDTH / 2, y0 + BUTTON_HEIGHT / 2 - 1),
                item["en"],
                font=font,
                anchor="mm",
                fill=fill,
                stroke_width=1,
                stroke_fill=stroke,
            )
            allowed_draw.rectangle((x0 + 4, y0 + 3, x0 + 119, y0 + 31), fill=1)

    source_pixels = original.load()
    localized_pixels = image.load()
    allowed_pixels = allowed.load()
    changed = 0
    outside = 0
    for y in range(image.height):
        for x in range(image.width):
            if source_pixels[x, y] != localized_pixels[x, y]:
                changed += 1
                if not allowed_pixels[x, y]:
                    outside += 1
    if outside:
        raise AssertionError(f"CGChip changed {outside} pixels outside approved label regions")

    png_output.parent.mkdir(parents=True, exist_ok=True)
    kg_output.parent.mkdir(parents=True, exist_ok=True)
    zlc2_output.parent.mkdir(parents=True, exist_ok=True)
    qa_output.parent.mkdir(parents=True, exist_ok=True)
    image.save(png_output, format="PNG", optimize=False)
    localized_kg = image_to_kg(image)
    kg_output.write_bytes(localized_kg)
    if kg_to_image(localized_kg).tobytes() != image.tobytes():
        raise AssertionError("localized CGChip GCGK pixel round-trip failed")
    packed = encode_zlc2(localized_kg)
    if decode_zlc2(packed) != localized_kg:
        raise AssertionError("localized CGChip ZLC2 round-trip failed")
    zlc2_output.write_bytes(packed)

    alpha = image.getchannel("A")
    retail_size = 260637
    qa = {
        "asset": "CGChip.kg",
        "class": "UI",
        "source_archive": "chip.fpk",
        "dimensions": [image.width, image.height],
        "mode": image.mode,
        "alpha_extrema": list(alpha.getextrema()),
        "font": str(FONT),
        "font_sha256": digest(FONT.read_bytes()),
        "source_sha256": digest(source_bytes),
        "localized_png_sha256": digest(png_output.read_bytes()),
        "localized_kg_sha256": digest(localized_kg),
        "localized_zlc2_sha256": digest(packed),
        "kg_pixel_roundtrip": "PASS",
        "zlc2_roundtrip": "PASS",
        "zlc2_payload_size": len(packed),
        "retail_zlc2_size": retail_size,
        "in_place_slot_fit": "PASS" if len(packed) <= retail_size else "REBUILD_REQUIRED",
        "injection_mode": "rebuild chip.fpk with replace-member",
        "allowed_change_pixels": changed,
        "outside_allowed_change_pixels": outside,
        "geometry": {
            "state_columns_x": [0, 123, 246, 369],
            "row_stride_y": BUTTON_HEIGHT,
            "button_size": [BUTTON_WIDTH, BUTTON_HEIGHT],
            "canvas_unchanged": True
        }
    }
    qa_output.write_text(json.dumps(qa, indent=2) + "\n", encoding="utf-8")
    print(f"localized=CGChip.kg png={png_output} kg={kg_output} qa={qa_output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--translations", type=Path, default=Path("assets/ui/translations/CGChip.json"))
    parser.add_argument("--png-output", type=Path, default=Path("assets/ui/png/CGChip.kg.png"))
    parser.add_argument("--kg-output", type=Path, default=Path("patch/ui/chip/CGChip.kg"))
    parser.add_argument("--zlc2-output", type=Path, default=Path("patch/ui/chip/CGChip.kg.zlc2"))
    parser.add_argument("--qa-output", type=Path, default=Path("qa/ui/CGChip.json"))
    args = parser.parse_args()
    localize(
        args.source,
        args.translations,
        args.png_output,
        args.kg_output,
        args.zlc2_output,
        args.qa_output,
    )


if __name__ == "__main__":
    main()
