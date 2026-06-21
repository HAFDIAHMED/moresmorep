"""Generate `book_cover_wrap.pdf` — a single-page KDP-compliant cover wrap
combining back cover + spine + front cover, with bleed margins on the outside
edges. This is the file you upload to Amazon KDP as the cover.

Spine width is calculated from page count and paper type. Defaults below
assume:
    Trim size:  A4  (8.27 × 11.69 inches)
    Pages:      249
    Paper:      cream (0.0025 inch per page)
    Bleed:      0.125 inch on outside edges

If KDP rejects the upload citing dimensions, update PAGES or PAPER and re-run.
"""
import os
from io import BytesIO
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import Paragraph, Frame


# ── parameters (the only knobs you should ever touch) ────────────────────────
TRIM_W = 8.27 * inch          # A4 width
TRIM_H = 11.69 * inch         # A4 height
PAGES  = 249                  # interior page count of v69
PAPER_THICKNESS = 0.0025      # cream paper, KDP spec (white = 0.002252)
BLEED  = 0.125 * inch         # KDP requires 0.125" on outside edges


# ── derived ──────────────────────────────────────────────────────────────────
SPINE_W   = PAGES * PAPER_THICKNESS * inch
WRAP_W    = TRIM_W * 2 + SPINE_W + BLEED * 2
WRAP_H    = TRIM_H + BLEED * 2

# Layout coordinates (in points, with 0,0 at bottom-left of full wrap):
BACK_LEFT   = BLEED                    # back cover starts after left bleed
BACK_RIGHT  = BLEED + TRIM_W           # back cover ends at the start of spine
SPINE_LEFT  = BACK_RIGHT
SPINE_RIGHT = SPINE_LEFT + SPINE_W
FRONT_LEFT  = SPINE_RIGHT
FRONT_RIGHT = FRONT_LEFT + TRIM_W
TOP         = BLEED + TRIM_H
BOTTOM      = BLEED

# Safe zone — KDP recommends keeping critical content >= 0.25" from any trim
SAFE_MARGIN = 0.25 * inch


# ── palette (matches book interior) ──────────────────────────────────────────
INK       = HexColor('#0A0A0A')
INK_MED   = HexColor('#2A2A2A')
INK_BODY  = HexColor('#3A3A3A')
INK_LIGHT = HexColor('#666666')
INK_XLIT  = HexColor('#999999')
BG_WHITE  = HexColor('#FFFFFF')


# ── output path ──────────────────────────────────────────────────────────────
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'book_cover_wrap.pdf')


def flow_text(c, html, style, x, y, w, h):
    """Render an HTML paragraph inside a Frame."""
    f = Frame(x, y - h, w, h, leftPadding=0, rightPadding=0,
              topPadding=0, bottomPadding=0, showBoundary=0)
    f.addFromList([Paragraph(html, style)], c)


def draw_back_cover(c):
    """Draw the back cover content on the LEFT side of the wrap."""
    # white background covering back + bleed
    c.setFillColor(BG_WHITE)
    c.rect(0, 0, BACK_RIGHT, WRAP_H, fill=1, stroke=0)

    # black top bar (full width including bleed)
    c.setFillColor(INK)
    c.rect(0, TOP - 0.04*inch, BACK_RIGHT, 0.04*inch, fill=1, stroke=0)

    # text area within safe margins
    text_left = BACK_LEFT + SAFE_MARGIN
    text_right = BACK_RIGHT - SAFE_MARGIN
    text_w = text_right - text_left

    # styles
    hook_st = ParagraphStyle('hook', fontName='Times-Italic', fontSize=15,
                             leading=21, alignment=TA_CENTER, textColor=INK)
    key_st  = ParagraphStyle('key',  fontName='Helvetica-Bold', fontSize=10,
                             leading=14, alignment=TA_CENTER, textColor=INK)
    body_st = ParagraphStyle('body', fontName='Helvetica', fontSize=9,
                             leading=14, alignment=TA_CENTER, textColor=INK_BODY)
    tag_st  = ParagraphStyle('tag',  fontName='Times-Italic', fontSize=9,
                             leading=13, alignment=TA_CENTER, textColor=INK_LIGHT)
    pull_st = ParagraphStyle('pull', fontName='Times-Italic', fontSize=10,
                             leading=16, alignment=TA_CENTER, textColor=INK)
    attr_st = ParagraphStyle('attr', fontName='Helvetica', fontSize=7.5,
                             leading=11, alignment=TA_CENTER, textColor=INK_LIGHT)
    bio_st  = ParagraphStyle('bio',  fontName='Helvetica', fontSize=8.5,
                             leading=14, alignment=TA_CENTER, textColor=INK_BODY)
    quote_st = ParagraphStyle('quote', fontName='Times-Italic', fontSize=8.5,
                              leading=13, alignment=TA_CENTER, textColor=INK_MED)
    quote_attr_st = ParagraphStyle('qa', fontName='Helvetica', fontSize=7,
                                   leading=11, alignment=TA_CENTER, textColor=INK_LIGHT)

    # vertical layout: walk down from top
    y = TOP - 0.7*inch

    flow_text(c,
        '<i>Every solution carries<br/>the seed of the next crisis.</i>',
        hook_st, text_left, y, text_w, 1.0*inch)
    y -= 1.0*inch

    # rule
    c.setStrokeColor(INK); c.setLineWidth(0.7)
    c.line(text_left, y, text_right, y)
    y -= 0.25*inch

    flow_text(c, 'This is not bad luck. It is mathematics.',
              key_st, text_left, y, text_w, 0.3*inch)
    y -= 0.4*inch

    flow_text(c,
        '<b>AHMED HAFDI</b> proves that solutions breed new problems '
        '<i>exponentially</i> — and constructs <b>Cascade Theory</b>: '
        'the framework explaining why celebrated innovations generate '
        'the defining crises of the next era.',
        body_st, text_left, y, text_w, 1.1*inch)
    y -= 1.15*inch

    flow_text(c,
        'Essential reading for anyone who leads, governs, builds, or decides.',
        tag_st, text_left, y, text_w, 0.4*inch)
    y -= 0.5*inch

    c.setStrokeColor(INK_XLIT); c.setLineWidth(0.5)
    c.line(text_left, y, text_right, y)
    y -= 0.3*inch

    flow_text(c,
        '‘Every solution, once released into a connected system, '
        'creates problems faster than the system can absorb them — and the '
        'more connected the system, the wider the gap.’',
        pull_st, text_left, y, text_w, 1.1*inch)
    y -= 1.1*inch
    flow_text(c, '— from the Introduction',
              attr_st, text_left, y, text_w, 0.2*inch)
    y -= 0.45*inch

    flow_text(c,
        '<b>AHMED HAFDI</b> is a software engineer and researcher based in '
        'Kenitra, Morocco. <i>More Solutions = More Problems</i> is the trade '
        'edition of his Cascade Innovation framework. The full mathematical '
        'treatment appears in the underlying research paper at '
        'researchgate.net/publication/395720779.',
        bio_st, text_left, y, text_w, 1.4*inch)
    y -= 1.5*inch

    c.setStrokeColor(INK_XLIT); c.setLineWidth(0.5)
    c.line(text_left, y, text_right, y)
    y -= 0.25*inch

    flow_text(c,
        '‘For every complex problem there is an answer that is clear, '
        'simple, and wrong.’',
        quote_st, text_left, y, text_w, 0.45*inch)
    y -= 0.5*inch
    flow_text(c, '— H. L. Mencken', quote_attr_st, text_left, y, text_w, 0.2*inch)
    y -= 0.35*inch

    flow_text(c,
        '‘Those who cannot remember the past are condemned to repeat it.’',
        quote_st, text_left, y, text_w, 0.35*inch)
    y -= 0.4*inch
    flow_text(c, '— George Santayana', quote_attr_st, text_left, y, text_w, 0.2*inch)

    # bottom black bar (full back-cover width including bleed)
    c.setFillColor(INK)
    c.rect(0, 0, BACK_RIGHT, 0.04*inch, fill=1, stroke=0)

    # URL just above the bar
    c.setFont('Helvetica', 7)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString((BACK_LEFT + BACK_RIGHT) / 2, 0.16*inch,
                        'www.moresolutions-moreproblems.com')


def draw_spine(c):
    """Spine text — title and author, rotated 90 degrees."""
    c.setFillColor(BG_WHITE)
    c.rect(SPINE_LEFT, 0, SPINE_W, WRAP_H, fill=1, stroke=0)

    # Centre of the spine
    cx = SPINE_LEFT + SPINE_W / 2

    # Title (rotated, reads top-to-bottom on a vertical spine)
    c.saveState()
    c.translate(cx, WRAP_H / 2)
    c.rotate(90)
    c.setFont('Helvetica-Bold', 14)
    c.setFillColor(INK)
    c.drawCentredString(0, 4, 'MORE SOLUTIONS = MORE PROBLEMS')
    c.restoreState()

    # Author (rotated, near the bottom of the spine)
    c.saveState()
    c.translate(cx, BOTTOM + 1.5*inch)
    c.rotate(90)
    c.setFont('Helvetica-Bold', 11)
    c.setFillColor(INK)
    c.drawCentredString(0, 0, 'AHMED HAFDI')
    c.restoreState()


def draw_front_cover(c):
    """Front cover content on the RIGHT side of the wrap."""
    # white background
    c.setFillColor(BG_WHITE)
    c.rect(FRONT_LEFT, 0, TRIM_W + BLEED, WRAP_H, fill=1, stroke=0)

    # top black bar
    c.setFillColor(INK)
    c.rect(FRONT_LEFT, TOP - 0.04*inch,
           TRIM_W + BLEED, 0.04*inch, fill=1, stroke=0)

    # vertical centre of front cover (within safe zone)
    cx = FRONT_LEFT + TRIM_W / 2

    # Title: MORE SOLUTIONS = MORE PROBLEMS — stacked, large
    c.setFont('Helvetica-Bold', 64)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(cx, WRAP_H * 0.72, 'MORE')
    c.setFont('Helvetica-Bold', 72)
    c.setFillColor(INK)
    c.drawCentredString(cx, WRAP_H * 0.64, 'SOLUTIONS')
    c.setFont('Helvetica-Bold', 42)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(cx, WRAP_H * 0.57, '=')
    c.setFont('Helvetica-Bold', 64)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(cx, WRAP_H * 0.49, 'MORE')
    c.setFont('Helvetica-Bold', 72)
    c.setFillColor(INK)
    c.drawCentredString(cx, WRAP_H * 0.41, 'PROBLEMS')

    # thin rule above subtitle
    c.setStrokeColor(INK_XLIT)
    c.setLineWidth(0.5)
    c.line(FRONT_LEFT + TRIM_W * 0.22, WRAP_H * 0.345,
           FRONT_RIGHT - TRIM_W * 0.22, WRAP_H * 0.345)

    # subtitle
    c.setFont('Times-Italic', 14)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(cx, WRAP_H * 0.32, 'Why Every Solution')
    c.drawCentredString(cx, WRAP_H * 0.295, 'Creates the Next Problem')

    # bottom black bar (full front width including bleed)
    bar_h = 0.7 * inch
    c.setFillColor(INK)
    c.rect(FRONT_LEFT, 0, TRIM_W + BLEED, bar_h, fill=1, stroke=0)

    # author name centred inside the bar
    c.setFont('Helvetica-Bold', 18)
    c.setFillColor(BG_WHITE)
    c.drawCentredString(cx, bar_h / 2 - 4, 'AHMED HAFDI')


def main():
    print(f'Generating KDP cover wrap -> {OUT}')
    print(f'  Trim size:       {TRIM_W/inch:.2f}" x {TRIM_H/inch:.2f}" (A4)')
    print(f'  Pages:           {PAGES}')
    print(f'  Spine width:     {SPINE_W/inch:.3f}" ({PAGES} pages x {PAPER_THICKNESS}"/page, cream paper)')
    print(f'  Bleed:           {BLEED/inch:.3f}"')
    print(f'  Total wrap size: {WRAP_W/inch:.3f}" x {WRAP_H/inch:.3f}"')
    print(f'                   ({WRAP_W:.1f} x {WRAP_H:.1f} pts)')
    c = rl_canvas.Canvas(OUT, pagesize=(WRAP_W, WRAP_H))
    draw_back_cover(c)
    draw_spine(c)
    draw_front_cover(c)
    c.showPage()
    c.save()
    print(f'  Saved.')


if __name__ == '__main__':
    main()
