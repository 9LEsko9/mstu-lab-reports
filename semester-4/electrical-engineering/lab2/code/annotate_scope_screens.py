from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"


def load_font(size: int):
    return ImageFont.truetype(FONT_PATH, size)


def draw_label(draw: ImageDraw.ImageDraw, xy, text, color, font):
    draw.text(xy, text, font=font, fill=color)


def annotate(source_name, target_name, labels):
    image = Image.open(IMAGES / source_name).convert("RGBA")
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    font = load_font(16)

    for label in labels:
        draw_label(
            draw,
            xy=label["xy"],
            text=label["text"],
            color=label["color"],
            font=font,
        )

    merged = Image.alpha_composite(image, overlay).convert("RGB")
    merged.save(IMAGES / target_name, quality=95)


def main():
    annotate(
        "3_2_B_oscilograph.png",
        "osc_B_scope_marked.png",
        [
            {"xy": (15, 58), "text": "268.7V", "color": (255, 255, 0)},
            {"xy": (105, 102), "text": "66.99V", "color": (0, 255, 0)},
            {"xy": (27, 86), "text": "19.67V", "color": (0, 255, 255)},
        ],
    )

    annotate(
        "3_2_v_osciloscope.png",
        "osc_V_scope_marked.png",
        [
            {"xy": (67, 112), "text": "268.7V", "color": (255, 255, 0)},
            {"xy": (47, 62), "text": "9.0V", "color": (0, 255, 0)},
            {"xy": (79, 88), "text": "83.0V", "color": (0, 255, 255)},
        ],
    )

    annotate(
        "3_2_g_osciloscope.png",
        "osc_G_scope_marked.png",
        [
            {"xy": (13, 68), "text": "268.7V", "color": (255, 255, 0)},
            {"xy": (13, 106), "text": "9.0V", "color": (0, 255, 0)},
            {"xy": (23, 68), "text": "83.0V", "color": (0, 255, 255)},
        ],
    )


if __name__ == "__main__":
    main()
