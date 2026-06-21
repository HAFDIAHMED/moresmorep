#!/usr/bin/env python3
"""
book_cover.py — Front and back covers for
"More Solutions = More Problems" by Ahmed Hafdi.

Output: book_cover.pdf  (page 1 = front, page 2 = back)
Run:    python3 book_cover.py
"""

import io, warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from reportlab.pdfgen   import canvas as rl_canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units  import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus   import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums  import TA_CENTER, TA_LEFT, TA_JUSTIFY

# ── Dimensions ──────────────────────────────────────────────────────────────
import os as _os
OUT = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'book_cover.pdf')
W   = 8.27 * inch  # A4 width — match the interior PDF dimensions exactly
H   = 11.69 * inch # A4 height — required for KDP/IngramSpark pre-flight

# ── Black & White Palette ───────────────────────────────────────────────────
BG        = HexColor('#FFFFFF')          # pure white background
BG_PANEL  = HexColor('#F4F4F4')          # very light gray panel (back cover)
INK       = HexColor('#0A0A0A')          # near-black (titles, rules)
INK_MED   = HexColor('#2A2A2A')          # dark gray (subtitle, author name)
INK_BODY  = HexColor('#3A3A3A')          # body text
INK_LIGHT = HexColor('#666666')          # captions, small text
INK_XLIT  = HexColor('#999999')          # very light gray accents
RULE_COL  = HexColor('#000000')          # solid black rules


# ═══════════════════════════════════════════════════════════════════════════
#  CASCADE TREE IMAGE  (root=top, leaves=bottom)  — black & white
# ═══════════════════════════════════════════════════════════════════════════
def _tx(level: int, idx: int) -> float:
    n = 2 ** level
    return 0.5 if n == 1 else idx / (n - 1)

def make_cascade_tree(w_pt, h_pt, dpi=180):
    """
    Binary cascade tree — root (black) at TOP, leaf cloud (gray) at BOTTOM.
    White background. Root is solid black, leaves fade to light gray.
    """
    LEVELS  = 5
    # Root = solid black → leaves = medium gray
    COLORS  = ['#0A0A0A', '#1E1E1E', '#383838', '#555555', '#777777', '#999999']
    NSIZES  = [320, 170, 90, 46, 24, 14]
    LWIDTHS = [2.4, 1.8, 1.2, 0.7, 0.40]
    ALPHAS  = [0.95, 0.80, 0.62, 0.44, 0.28]

    w_in = w_pt / 72
    h_in = h_pt / 72

    fig, ax = plt.subplots(figsize=(w_in, h_in), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.set_xlim(-0.04, 1.04)
    ax.set_ylim(-0.03, 1.04)   # y=1 → root (TOP), y=0 → leaves (BOTTOM)
    ax.axis('off')

    # ── draw edges first ──────────────────────────────────────────────────
    for lv in range(LEVELS):
        n   = 2 ** lv
        col = COLORS[lv + 1]
        lw  = LWIDTHS[lv]
        alp = ALPHAS[lv]
        for i in range(n):
            px = _tx(lv, i)
            py = 1.0 - lv / LEVELS        # parent y (higher = closer to top)
            cx_l = _tx(lv + 1, 2 * i)
            cx_r = _tx(lv + 1, 2 * i + 1)
            cy   = 1.0 - (lv + 1) / LEVELS  # child y
            for cx in (cx_l, cx_r):
                ax.plot([px, cx], [py, cy],
                        color=col, lw=lw, alpha=alp,
                        solid_capstyle='round', zorder=2)

    # ── draw nodes ────────────────────────────────────────────────────────
    for lv in range(LEVELS + 1):
        n   = 2 ** lv
        col = COLORS[lv]
        s   = NSIZES[min(lv, len(NSIZES)-1)]
        xs  = [_tx(lv, i)         for i in range(n)]
        ys  = [1.0 - lv / LEVELS] * n
        ax.scatter(xs, ys, s=s, c=col, zorder=5, edgecolors='none')

    # ── "THE SOLUTION" label under root node ──────────────────────────────
    ax.text(0.5, 1.015, '— THE SOLUTION —',
            color='#444444', fontsize=7.5, ha='center', va='bottom',
            alpha=0.65, fontfamily='sans-serif', style='italic')

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=dpi,
                bbox_inches='tight', pad_inches=0.0,
                facecolor='#FFFFFF')
    plt.close(fig)
    buf.seek(0)
    return ImageReader(buf)


# ═══════════════════════════════════════════════════════════════════════════
#  MINI CHART  (back cover) — black & white
# ═══════════════════════════════════════════════════════════════════════════
def make_growth_chart(w_pt, h_pt, dpi=140):
    w_in, h_in = w_pt / 72, h_pt / 72
    fig, ax = plt.subplots(figsize=(w_in, h_in), facecolor='#F4F4F4')
    ax.set_facecolor('#F4F4F4')

    x    = np.linspace(1, 8, 300)
    ylin = x / 8
    yexp = np.clip((2**x - 2) / (2**8 - 2), 0, 1)

    ax.fill_between(x, ylin, yexp, color='#666666', alpha=0.18)
    ax.plot(x, ylin, color='#555555', lw=2.0, linestyle='--')
    ax.plot(x, yexp, color='#0A0A0A', lw=2.2)

    ax.text(7.3, 0.88, 'Problems\nO(2n)', color='#0A0A0A', fontsize=7,
            ha='left', va='center', fontweight='bold')
    ax.text(7.3, 0.11, 'Solutions\nO(n)', color='#555555', fontsize=7,
            ha='left', va='center', fontweight='bold')
    ax.text(4.3, 0.42, 'THE\nGAP', color='#888888', fontsize=5.5,
            ha='center', va='center', alpha=0.55, style='italic')

    ax.set_xlim(1, 9.0)
    ax.set_ylim(-0.05, 1.1)
    for sp in ax.spines.values():
        sp.set_color('#CCCCCC')
        sp.set_linewidth(0.5)
    ax.tick_params(left=False, bottom=False,
                   labelleft=False, labelbottom=False)

    plt.tight_layout(pad=0.1)
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=dpi, facecolor='#F4F4F4')
    plt.close(fig)
    buf.seek(0)
    return ImageReader(buf)


# ═══════════════════════════════════════════════════════════════════════════
#  PARAGRAPH HELPER
# ═══════════════════════════════════════════════════════════════════════════
def ps(name, font='Helvetica', size=10, color=None,
       align=TA_LEFT, leading_mul=1.48):
    if color is None:
        color = INK_BODY
    return ParagraphStyle(name, fontName=font, fontSize=size,
                          textColor=color, alignment=align,
                          leading=size * leading_mul)

def flow(c, text, style, x, y, w, max_h=300):
    """Draw paragraph at (x, y-height); return height consumed."""
    p = Paragraph(text, style)
    p.wrapOn(c, w, max_h)
    p.drawOn(c, x, y - p.height)
    return p.height


# ═══════════════════════════════════════════════════════════════════════════
#  FRONT COVER  — pure typographic, no matplotlib
# ═══════════════════════════════════════════════════════════════════════════
def _draw_cascade_symbol(c, cx, cy, sym_w, sym_h):
    """
    Tiny elegant 3-level binary tree drawn with canvas primitives.
    Root at top, 8 leaf nodes at bottom. All in solid black.
    """
    LEVELS = 3

    def nx(lv, idx):
        n = 2 ** lv
        if n == 1:
            return cx
        return cx - sym_w / 2 + idx * sym_w / (n - 1)

    def ny(lv):
        return cy + sym_h / 2 - lv * sym_h / LEVELS

    # edges
    for lv in range(LEVELS):
        n   = 2 ** lv
        lw  = max(0.4, 1.3 - lv * 0.35)
        alp = 1.0 - lv * 0.18
        c.setStrokeColorRGB(0, 0, 0, alpha=alp)
        c.setLineWidth(lw)
        for i in range(n):
            px, py = nx(lv, i), ny(lv)
            for ci in [2 * i, 2 * i + 1]:
                cx2, cy2 = nx(lv + 1, ci), ny(lv + 1)
                c.line(px, py, cx2, cy2)

    # nodes — root biggest, leaves smallest
    node_sizes = [4.5, 3.0, 2.0, 1.3]
    for lv in range(LEVELS + 1):
        n = 2 ** lv
        r = node_sizes[min(lv, len(node_sizes) - 1)]
        c.setFillColor(INK)
        for i in range(n):
            c.circle(nx(lv, i), ny(lv), r, fill=1, stroke=0)


def front_cover(c):
    # ── pure white background ─────────────────────────────────────────────
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # ── thin black top bar ────────────────────────────────────────────────
    c.setFillColor(INK)
    c.rect(0, H - 0.04 * inch, W, 0.04 * inch, fill=1, stroke=0)

    # ── small cascade symbol — upper portion ──────────────────────────────
    _draw_cascade_symbol(c,
        cx=W / 2,
        cy=H * 0.790,
        sym_w=1.9 * inch,
        sym_h=1.05 * inch)

    # ── title block ───────────────────────────────────────────────────────
    # "MORE"  (clearly above SOLUTIONS, no overlap)
    c.setFont('Helvetica', 13)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(W / 2, H * 0.638, 'MORE')

    # "SOLUTIONS"
    c.setFont('Helvetica-Bold', 46)
    c.setFillColor(INK)
    c.drawCentredString(W / 2, H * 0.570, 'SOLUTIONS')

    # "=" with flanking hairlines
    c.setStrokeColor(INK_XLIT)
    c.setLineWidth(0.55)
    c.line(W * 0.18, H * 0.530, W * 0.82, H * 0.530)

    c.setFont('Helvetica', 18)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(W / 2, H * 0.513, '=')

    c.line(W * 0.18, H * 0.497, W * 0.82, H * 0.497)

    # "MORE"  (clearly above PROBLEMS, no overlap)
    c.setFont('Helvetica', 13)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(W / 2, H * 0.464, 'MORE')

    # "PROBLEMS"
    c.setFont('Helvetica-Bold', 46)
    c.setFillColor(INK)
    c.drawCentredString(W / 2, H * 0.395, 'PROBLEMS')

    # ── subtitle ──────────────────────────────────────────────────────────
    c.setStrokeColor(INK_XLIT)
    c.setLineWidth(0.5)
    c.line(W * 0.28, H * 0.360, W * 0.72, H * 0.360)

    sub_st = ps('sub', font='Times-Italic', size=10, color=INK_LIGHT,
                align=TA_CENTER, leading_mul=1.55)
    flow(c,
         'Why Every Solution<br/>Creates the Next Problem',
         sub_st, W * 0.12, H * 0.342, W * 0.76)

    # ── author — pinned to bottom ─────────────────────────────────────────
    c.setFillColor(INK)
    c.rect(0, 0, W, 0.04 * inch, fill=1, stroke=0)

    c.setFont('Helvetica-Bold', 14)
    c.setFillColor(INK)
    c.drawCentredString(W / 2, 0.155 * inch, 'AHMED HAFDI')


# ═══════════════════════════════════════════════════════════════════════════
#  BACK COVER
# ═══════════════════════════════════════════════════════════════════════════
def back_cover(c):
    M  = W * 0.13          # left/right margin
    TW = W - 2 * M        # text width

    # ── pure white background ─────────────────────────────────────────────
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # ── black top bar ─────────────────────────────────────────────────────
    c.setFillColor(INK)
    c.rect(0, H - 0.04*inch, W, 0.04*inch, fill=1, stroke=0)

    # ── HOOK — large opening statement ───────────────────────────────────
    hook_st = ps('hook', font='Times-Roman', size=17,
                 color=INK, align=TA_CENTER, leading_mul=1.55)
    hook_h = flow(c,
        '<i>Every solution carries<br/>the seed of the next crisis.</i>',
        hook_st, M, H * 0.91, TW)

    # thin rule under hook
    rule_y = H * 0.91 - hook_h - 0.18*inch
    c.setStrokeColor(INK); c.setLineWidth(0.7)
    c.line(M, rule_y, W - M, rule_y)

    # ── key line ──────────────────────────────────────────────────────────
    key_st = ps('key', font='Helvetica-Bold', size=11,
                color=INK, align=TA_CENTER, leading_mul=1.5)
    key_h = flow(c, 'This is not bad luck. It is mathematics.',
                 key_st, M, rule_y - 0.22*inch, TW)

    # ── short body ────────────────────────────────────────────────────────
    body_st = ps('body', font='Helvetica', size=9.8,
                 color=INK_BODY, align=TA_CENTER, leading_mul=1.65)
    body_y  = rule_y - 0.22*inch - key_h - 0.20*inch
    body_h  = flow(c,
        '<b>AHMED HAFDI</b> proves that solutions breed new problems '
        '<i>exponentially</i> — and constructs <b>Cascade Theory</b>: '
        'the framework explaining why celebrated innovations '
        'generate the defining crises of the next era.',
        body_st, M, body_y, TW)

    # tagline
    tag_st = ps('tag', font='Times-Italic', size=9.5,
                color=INK_LIGHT, align=TA_CENTER, leading_mul=1.5)
    tag_y  = body_y - body_h - 0.22*inch
    flow(c, 'Essential reading for anyone who leads, governs, builds, or decides.',
         tag_st, M, tag_y, TW)

    # thin rule
    mid_rule_y = tag_y - 0.30*inch
    c.setStrokeColor(INK_XLIT); c.setLineWidth(0.5)
    c.line(M, mid_rule_y, W - M, mid_rule_y)

    # ── pull-quote from the book + author bio ────────────────────────────
    # First-book authors do not fake endorsements. The back cover instead
    # sells itself with a single pull-quote from the Introduction and a
    # short author bio. Both are honest and stand on their own. Once real
    # outside blurbs come in from outreach, they replace the author-bio
    # block at the bottom (see OUTREACH_BLURBERS.md).
    pull_st = ps('pull', font='Times-Italic', size=9.5,
                 color=INK, align=TA_CENTER, leading_mul=1.55)
    pull_attr_st = ps('pull_attr', font='Helvetica', size=7.5,
                      color=INK_LIGHT, align=TA_CENTER, leading_mul=1.3)
    bio_st = ps('bio', font='Helvetica', size=8.5,
                color=INK_BODY, align=TA_CENTER, leading_mul=1.55)

    py = mid_rule_y - 0.22*inch

    # The pull-quote — the Argument-in-One-Sentence from the Introduction.
    pull = ('\u2018Every solution, once released into a connected system, '
            'creates problems faster than the system can absorb them \u2014 and the '
            'more connected the system, the wider the gap.\u2019')
    qh = flow(c, pull, pull_st, M, py, TW)
    py -= qh + 0.05*inch
    ah = flow(c, '\u2014 from the Introduction', pull_attr_st, M, py, TW)
    py -= ah + 0.20*inch

    # The author bio.
    bio = ('<b>AHMED HAFDI</b> is a software engineer and researcher based in '
           'Kenitra, Morocco. <i>More Solutions = More Problems</i> is the trade '
           'edition of his Cascade Innovation framework; the full mathematical '
           'treatment appears in the underlying research paper at '
           'researchgate.net/publication/395720779.')
    bh = flow(c, bio, bio_st, M, py, TW)
    py -= bh + 0.18*inch

    # thin rule
    c.setStrokeColor(INK_XLIT); c.setLineWidth(0.5)
    c.line(M, py, W - M, py)

    # ── three book quotes ─────────────────────────────────────────────────
    bq_st   = ps('bq', font='Times-Italic', size=9.0,
                 color=INK_MED, align=TA_CENTER, leading_mul=1.50)
    bqs_st  = ps('bqs', font='Helvetica', size=7.5,
                 color=INK_LIGHT, align=TA_CENTER, leading_mul=1.3)

    book_quotes = [
        ('For every complex problem there is an answer that is clear, simple, and wrong.',
         '— H. L. Mencken'),
        ('We do not learn from experience. We learn from reflecting on experience.',
         '— John Dewey'),
        ('Those who cannot remember the past are condemned to repeat it.',
         '— George Santayana'),
    ]
    qpy = py - 0.22*inch
    for bq, src in book_quotes:
        qh = flow(c, bq, bq_st, M, qpy, TW)
        qpy -= qh + 0.04*inch
        ah = flow(c, src, bqs_st, M, qpy, TW)
        qpy -= ah + 0.13*inch

    # ── website + bottom bar ──────────────────────────────────────────────
    c.setFont('Helvetica', 7)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(W/2, 0.16*inch, 'www.moresolutions-moreproblems.com')

    c.setFillColor(INK)
    c.rect(0, 0, W, 0.04*inch, fill=1, stroke=0)


# ═══════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════
def main():
    print('Rendering cascade tree...')
    c = rl_canvas.Canvas(OUT, pagesize=(W, H))

    print('Drawing front cover...')
    front_cover(c)
    c.showPage()

    print('Drawing back cover...')
    back_cover(c)
    c.showPage()

    c.save()
    print(f'\n  Saved → {OUT}')
    print('  Page 1: Front cover')
    print('  Page 2: Back cover')


if __name__ == '__main__':
    main()
