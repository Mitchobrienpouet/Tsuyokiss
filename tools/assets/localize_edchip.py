#!/usr/bin/env python3
"""Render English ending-gallery labels at retail sprite geometry."""

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
)
BUTTON_WIDTH = 261
BUTTON_HEIGHT = 37
GROUP_HEIGHT = 111


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fit_font(text: str, maximum: int) -> ImageFont.FreeTypeFont:
    for size in range(24, 11, -1):
        font = ImageFont.truetype(str(FONT), size=size)
        left, _, right, _ = font.getbbox(text, stroke_width=1)
        if right - left <= maximum:
            return font
    raise ValueError(f"ending label does not fit its retail button: {text!r}")


def restore_button_interior(image: Image.Image, x0: int, y0: int) -> None:
    pixels = image.load()
    for y in range(y0 + 4, y0 + 33):
        background = Counter(pixels[x, y] for x in range(x0 + 8, x0 + 253)).most_common(1)[0][0]
        for x in range(x0 + 8, x0 + 253):
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
        raise ValueError(f"unexpected EDChip canvas: {image.size} {image.mode}")
    original = image.copy()
    copy = json.loads(translations.read_text(encoding="utf-8"))
    columns = copy["columns"]
    if [len(items) for items in columns] != [9, 9, 3]:
        raise ValueError("EDChip requires 9, 9, and 3 labels in its three columns")

    allowed = Image.new("1", image.size, 0)
    allowed_draw = ImageDraw.Draw(allowed)
    draw = ImageDraw.Draw(image)
    for column, items in enumerate(columns):
        x0 = column * BUTTON_WIDTH
        for group, item in enumerate(items):
            for state, (fill, stroke) in enumerate(STATE_COLORS):
                y0 = group * GROUP_HEIGHT + state * BUTTON_HEIGHT
                restore_button_interior(image, x0, y0)
                font = fit_font(item["en"], BUTTON_WIDTH - 18)
                draw.text(
                    (x0 + BUTTON_WIDTH / 2, y0 + BUTTON_HEIGHT / 2 - 1),
                    item["en"],
                    font=font,
                    anchor="mm",
                    fill=fill,
                    stroke_width=1,
                    stroke_fill=stroke,
                )
                allowed_draw.rectangle((x0 + 7, y0 + 3, x0 + 253, y0 + 33), fill=1)

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
        raise AssertionError(f"EDChip changed {outside} pixels outside approved label regions")

    png_output.parent.mkdir(parents=True, exist_ok=True)
    kg_output.parent.mkdir(parents=True, exist_ok=True)
    zlc2_output.parent.mkdir(parents=True, exist_ok=True)
    qa_output.parent.mkdir(parents=True, exist_ok=True)
    image.save(png_output, format="PNG", optimize=False)
    localized_kg = image_to_kg(image)
    kg_output.write_bytes(localized_kg)
    if kg_to_image(localized_kg).tobytes() != image.tobytes():
        raise AssertionError("localized EDChip GCGK pixel round-trip failed")
    packed = encode_zlc2(localized_kg)
    if decode_zlc2(packed) != localized_kg:
        raise AssertionError("localized EDChip ZLC2 round-trip failed")
    zlc2_output.write_bytes(packed)

    alpha = image.getchannel("A")
    retail_size = 478819
    qa = {
        "asset": "EDChip.kg",
        "class": "UI_STORY",
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
            "columns_x": [0, 261, 522],
            "state_stride_y": BUTTON_HEIGHT,
            "group_stride_y": GROUP_HEIGHT,
            "button_size": [BUTTON_WIDTH, BUTTON_HEIGHT],
            "canvas_unchanged": True
        }
    }
    qa_output.write_text(json.dumps(qa, indent=2) + "\n", encoding="utf-8")
    print(f"localized=EDChip.kg png={png_output} kg={kg_output} qa={qa_output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--translations", type=Path, default=Path("assets/ui/translations/EDChip.json"))
    parser.add_argument("--png-output", type=Path, default=Path("assets/ui/png/EDChip.kg.png"))
    parser.add_argument("--kg-output", type=Path, default=Path("patch/ui/chip/EDChip.kg"))
    parser.add_argument("--zlc2-output", type=Path, default=Path("patch/ui/chip/EDChip.kg.zlc2"))
    parser.add_argument("--qa-output", type=Path, default=Path("qa/ui/EDChip.json"))
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
