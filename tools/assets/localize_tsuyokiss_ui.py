#!/usr/bin/env python3
"""Render English Tsuyokiss UI sprites without moving engine geometry."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from candysoft_assets import decode_zlc2, encode_zlc2, image_to_kg, kg_to_image


FONT = Path("/usr/share/fonts/opentype/urw-base35/NimbusSansNarrow-Bold.otf")
BUTTON_STATES = (
    {"fill": (255, 255, 255, 255), "stroke": (65, 91, 148, 255)},
    {"fill": (255, 255, 255, 255), "stroke": (255, 167, 113, 255)},
    {"fill": (255, 137, 158, 255), "stroke": (255, 208, 128, 255)},
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fit_font(text: str, maximum: int, start: int = 30, minimum: int = 17) -> ImageFont.FreeTypeFont:
    for size in range(start, minimum - 1, -1):
        font = ImageFont.truetype(str(FONT), size=size)
        left, _, right, _ = font.getbbox(text, stroke_width=1)
        if right - left <= maximum:
            return font
    raise ValueError(f"text does not fit: {text!r}")


def button_backgrounds(image: Image.Image) -> list[dict[int, tuple[int, int, int, int]]]:
    """Sample clean scanlines from the short EXTRAS button in each state."""
    pixels = image.load()
    backgrounds: list[dict[int, tuple[int, int, int, int]]] = []
    for state in range(3):
        y0 = 3 * 129 + state * 43
        rows = {}
        for relative_y in range(7, 36):
            y = y0 + relative_y
            candidates = [pixels[x, y] for x in (*range(12, 70), *range(165, 219)) if pixels[x, y][3] > 0]
            rows[relative_y] = Counter(candidates).most_common(1)[0][0]
        backgrounds.append(rows)
    return backgrounds


def clear_button_text(
    image: Image.Image,
    box: tuple[int, int, int, int],
    state: int,
    backgrounds: list[dict[int, tuple[int, int, int, int]]],
) -> None:
    """Restore each interior scanline from a clean same-state reference."""
    x0, y0, x1, y1 = box
    pixels = image.load()
    for y in range(y0 + 7, y1 - 6):
        background = backgrounds[state][y - y0]
        for x in range(x0 + 9, x1 - 9):
            pixels[x, y] = background


def draw_button(
    image: Image.Image,
    box: tuple[int, int, int, int],
    text: str,
    state: int,
    backgrounds: list[dict[int, tuple[int, int, int, int]]],
) -> None:
    clear_button_text(image, box, state, backgrounds)
    x0, y0, x1, y1 = box
    font = fit_font(text, x1 - x0 - 20)
    draw = ImageDraw.Draw(image)
    draw.text(
        ((x0 + x1) / 2, (y0 + y1) / 2 - 1),
        text,
        font=font,
        anchor="mm",
        fill=BUTTON_STATES[state]["fill"],
        stroke_width=1,
        stroke_fill=BUTTON_STATES[state]["stroke"],
    )


def clear_description_area(image: Image.Image) -> None:
    pixels = image.load()
    for y in range(125, 390):
        for x in range(464, 900):
            pixels[x, y] = (0, 0, 0, 0)


def localize_titlechip(
    source: Path,
    translations: Path,
    png_output: Path,
    kg_output: Path,
    zlc2_output: Path,
    qa_output: Path,
) -> None:
    source_bytes = source.read_bytes()
    image = kg_to_image(source_bytes)
    if image.size != (1024, 1024):
        raise ValueError(f"unexpected titlechip dimensions: {image.size}")
    original = image.copy()
    copy = json.loads(translations.read_text(encoding="utf-8"))
    backgrounds = button_backgrounds(image)
    columns = [copy["left_buttons"], copy["right_buttons"]]
    for column, labels in enumerate(columns):
        x0 = column * 232
        for row, item in enumerate(labels):
            for state in range(3):
                y0 = row * 129 + state * 43
                draw_button(image, (x0, y0, x0 + 231, y0 + 42), item["en"], state, backgrounds)
    for state in range(3):
        y0 = state * 43
        draw_button(
            image,
            (464, y0, 695, y0 + 42),
            copy["reset_all_button"]["en"],
            state,
            backgrounds,
        )

    clear_description_area(image)
    description_font = ImageFont.truetype(str(FONT), size=15)
    draw = ImageDraw.Draw(image)
    for row, item in enumerate(copy["descriptions"]):
        draw.text(
            (467, 128 + row * 17),
            item["en"],
            font=description_font,
            fill=(255, 255, 255, 255),
            stroke_width=1,
            stroke_fill=(17, 24, 45, 255),
        )

    allowed = Image.new("1", image.size, 0)
    allowed_draw = ImageDraw.Draw(allowed)
    for column in range(2):
        x0 = column * 232
        for row in range(7):
            for state in range(3):
                y0 = row * 129 + state * 43
                allowed_draw.rectangle((x0 + 8, y0 + 3, x0 + 223, y0 + 38), fill=1)
    for state in range(3):
        y0 = state * 43
        allowed_draw.rectangle((472, y0 + 3, 687, y0 + 38), fill=1)
    allowed_draw.rectangle((464, 125, 899, 389), fill=1)
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
        raise AssertionError(f"titlechip changed {outside} pixels outside approved text regions")

    png_output.parent.mkdir(parents=True, exist_ok=True)
    kg_output.parent.mkdir(parents=True, exist_ok=True)
    zlc2_output.parent.mkdir(parents=True, exist_ok=True)
    qa_output.parent.mkdir(parents=True, exist_ok=True)
    image.save(png_output, format="PNG", optimize=False)
    localized_kg = image_to_kg(image)
    kg_output.write_bytes(localized_kg)
    restored = kg_to_image(localized_kg)
    if restored.size != image.size or restored.tobytes() != image.tobytes():
        raise AssertionError("localized GCGK pixel round-trip failed")
    packed = encode_zlc2(localized_kg)
    packed_size = len(packed)
    if decode_zlc2(packed) != localized_kg:
        raise AssertionError("localized titlechip ZLC2 round-trip failed")
    zlc2_output.write_bytes(packed)
    alpha = image.getchannel("A")
    qa = {
        "asset": "titlechip.kg",
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
        "zlc2_payload_size": packed_size,
        "retail_zlc2_size": 350619,
        "in_place_slot_fit": "PASS" if packed_size <= 350619 else "REBUILD_REQUIRED",
        "injection_mode": "rebuild chip.fpk with replace-member",
        "allowed_change_pixels": changed,
        "outside_allowed_change_pixels": outside,
        "geometry": {
            "button_columns_x": [0, 232],
            "button_group_stride_y": 129,
            "button_state_stride_y": 43,
            "button_size": [231, 42],
            "canvas_unchanged": True,
        },
    }
    qa_output.write_text(json.dumps(qa, indent=2) + "\n", encoding="utf-8")
    print(f"localized=titlechip.kg png={png_output} kg={kg_output} qa={qa_output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--translations", type=Path, default=Path("assets/ui/translations/titlechip.json"))
    parser.add_argument("--png-output", type=Path, default=Path("assets/ui/png/titlechip.kg.png"))
    parser.add_argument("--kg-output", type=Path, default=Path("patch/ui/chip/titlechip.kg"))
    parser.add_argument(
        "--zlc2-output",
        type=Path,
        default=Path("patch/ui/chip/titlechip.kg.zlc2"),
    )
    parser.add_argument("--qa-output", type=Path, default=Path("qa/ui/titlechip.json"))
    args = parser.parse_args()
    localize_titlechip(
        args.source,
        args.translations,
        args.png_output,
        args.kg_output,
        args.zlc2_output,
        args.qa_output,
    )


if __name__ == "__main__":
    main()
