"""Generate `book_kindle_cover.jpg` — the front-cover-only image for the
Amazon Kindle ebook listing. Dimensions: 1600 x 2560 px (Amazon's recommended
size, 1.6:1 aspect ratio). Format: JPG, 95% quality, RGB color space.

Re-uses the visual identity of the print cover (front panel only — no spine,
no back, no bleed)."""
import os
from PIL import Image, ImageDraw, ImageFont

# Kindle cover dimensions (Amazon spec)
W, H = 1600, 2560

# Colors (matching the print cover palette)
INK         = (10, 10, 10)
INK_LIGHT   = (170, 170, 170)
INK_XLIGHT  = (200, 200, 200)
INK_GREY    = (110, 110, 110)
BG_WHITE    = (255, 255, 255)


def font(family, size):
    """Try to load a Windows system font; fall back gracefully."""
    candidates = {
        'helvetica-bold': ['arialbd.ttf', 'Arial Bold.ttf', 'helvetica-bold.ttf'],
        'helvetica':      ['arial.ttf', 'Arial.ttf'],
        'times-italic':   ['timesi.ttf', 'Times New Roman Italic.ttf'],
    }
    for name in candidates.get(family, [family]):
        for prefix in ['C:/Windows/Fonts/', '']:
            path = prefix + name
            if os.path.exists(path):
                return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_text_centered(draw, text, x, y, fnt, fill):
    """Draw text centred at (x, y) — works around PIL anchor inconsistencies."""
    bbox = draw.textbbox((0, 0), text, font=fnt)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text((x - w/2 - bbox[0], y - h/2 - bbox[1]), text, font=fnt, fill=fill)


def main():
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       'book_kindle_cover.jpg')
    print(f'Generating Kindle cover -> {out}')
    print(f'  Dimensions: {W} x {H} px (Amazon recommended)')

    img = Image.new('RGB', (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)

    # Fonts
    f_huge   = font('helvetica-bold', 320)   # SOLUTIONS / PROBLEMS
    f_med    = font('helvetica-bold', 260)   # MORE (lighter)
    f_eq     = font('helvetica-bold', 200)   # =
    f_sub    = font('times-italic', 64)      # subtitle
    f_author = font('helvetica-bold', 90)    # AHMED HAFDI

    # Top black hairline bar
    bar_top_h = 18
    draw.rectangle([(0, 0), (W, bar_top_h)], fill=INK)

    cx = W // 2

    # --- Title stack ---
    draw_text_centered(draw, 'MORE',      cx, int(H * 0.20), f_med,  INK_GREY)
    draw_text_centered(draw, 'SOLUTIONS', cx, int(H * 0.30), f_huge, INK)
    draw_text_centered(draw, '=',         cx, int(H * 0.40), f_eq,   INK_GREY)
    draw_text_centered(draw, 'MORE',      cx, int(H * 0.50), f_med,  INK_GREY)
    draw_text_centered(draw, 'PROBLEMS',  cx, int(H * 0.60), f_huge, INK)

    # --- Subtitle rule + 2 lines ---
    rule_y = int(H * 0.69)
    draw.line([(int(W * 0.22), rule_y), (int(W * 0.78), rule_y)],
              fill=INK_XLIGHT, width=2)
    draw_text_centered(draw, 'Why Every Solution',       cx, int(H * 0.725), f_sub, INK_GREY)
    draw_text_centered(draw, 'Creates the Next Problem', cx, int(H * 0.755), f_sub, INK_GREY)

    # --- Bottom black bar with author ---
    bar_h = 220
    draw.rectangle([(0, H - bar_h), (W, H)], fill=INK)
    draw_text_centered(draw, 'AHMED HAFDI', cx, H - bar_h // 2, f_author, BG_WHITE)

    # Save as JPG, RGB, high quality
    img.save(out, 'JPEG', quality=95, dpi=(300, 300), optimize=True)
    size_kb = os.path.getsize(out) / 1024
    print(f'  Saved.  ({size_kb:.0f} KB)')


if __name__ == '__main__':
    main()
