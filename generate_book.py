#!/usr/bin/env python3
"""
MORE SOLUTIONS = MORE PROBLEMS
Why Progress Breeds New Problems, and How to Get Ahead of the Cascade
By Ahmed Hafdi

Run: python3 generate_book.py
Output: More_Solutions_More_Problems.pdf
Requires: pip install reportlab matplotlib numpy Pillow
"""

import warnings, sys
warnings.filterwarnings('ignore')
from io import BytesIO
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether, Flowable
)
from reportlab.pdfgen import canvas as pdfcanvas

# ─── PAGE GEOMETRY ────────────────────────────────────────────────────────────
PW, PH = A4          # 595.27 x 841.89 pts
ML, MR  = 1.25*inch, 1.0*inch
MT, MB  = 1.0*inch, 1.0*inch
TW      = PW - ML - MR   # text width

# ─── GLOBAL STATE for running headers ─────────────────────────────────────────
G = {'chapter': '', 'part': ''}

# ─── CUSTOM FLOWABLES ─────────────────────────────────────────────────────────
class Mark(Flowable):
    """Zero-height marker that updates G['chapter'] / G['part']."""
    def __init__(self, chapter='', part=''):
        super().__init__(); self.chapter=chapter; self.part=part
        self.width=self.height=0
    def draw(self):
        if self.chapter: G['chapter']=self.chapter
        if self.part:    G['part']=self.part


class _RedrawChapterHeader(Flowable):
    """Repaints the running head on a chapter-opening page.

    on_page() fires at the *start* of every page and reads G['chapter'] for the
    odd-page running head — but on a chapter-opening page, G has not yet been
    updated by the chapter's Mark flowable, so on_page paints the previous
    chapter's title. This flowable runs as the first visible element of a
    chapter's chapter_opener: it covers the wrong header with a white box,
    redraws the top rule, and prints the correct chapter title. Coordinates
    are in flowable-local space — this flowable sits at the top of the frame
    (after the zero-height Mark), so y ≈ 16 in local coords lines up with the
    absolute running-head row that on_page used.
    """
    def __init__(self, chapter):
        super().__init__()
        self.chapter = chapter
        self.width = 0
        self.height = 0

    def wrap(self, availW, availH):
        return (0, 0)

    def draw(self):
        c = self.canv
        pg = c.getPageNumber()
        if pg <= 2:
            return  # cover + blank verso, no running head exists
        c.saveState()
        # Cover the previous chapter's header (text + rule) with a white strip.
        c.setFillColor(colors.white)
        c.rect(-4, 8, TW + 8, 16, fill=1, stroke=0)
        # Repaint the top rule in case it was hidden by the white box.
        c.setStrokeColor(colors.black)
        c.setLineWidth(0.3)
        c.line(0, 10, TW, 10)
        # Repaint the correct running head: odd pages show the chapter, even
        # pages show the book title — match on_page()'s parity rule.
        c.setFont('Times-Italic', 8.5)
        c.setFillColor(colors.black)
        if pg % 2 == 0:
            c.drawString(0, 16, 'More Solutions = More Problems')
        else:
            c.drawRightString(TW, 16, self.chapter)
        c.restoreState()


class VSpace(Spacer):
    def __init__(self, h): super().__init__(1, h)

class Rule(Flowable):
    def __init__(self, w=None, thick=0.4, spaceAfter=4):
        super().__init__()
        self.w=w or TW; self.thick=thick; self.height=thick+spaceAfter; self.width=self.w
    def draw(self):
        self.canv.setLineWidth(self.thick); self.canv.setStrokeColor(colors.black)
        self.canv.line(0,self.thick,self.w,self.thick)

# ─── STYLES ───────────────────────────────────────────────────────────────────
def make_styles():
    S={}
    def s(name, **kw):
        base=kw.pop('parent',None)
        defaults=dict(fontName='Times-Roman',fontSize=11,leading=17,
                      alignment=TA_JUSTIFY,textColor=colors.black,
                      spaceAfter=6,spaceBefore=0,firstLineIndent=0,
                      leftIndent=0,rightIndent=0)
        if base: [defaults.update({k:getattr(base,k,None)}) for k in defaults if hasattr(base,k)]
        defaults.update(kw); return ParagraphStyle(name,**defaults)

    S['body']        = s('body',        firstLineIndent=18, spaceAfter=7)
    S['body0']       = s('body0',       firstLineIndent=0,  spaceAfter=7)
    S['bold_body']   = s('bold_body',   fontName='Times-Bold', firstLineIndent=0, spaceAfter=7)
    S['italic_body'] = s('italic_body', fontName='Times-Italic',firstLineIndent=0,spaceAfter=7)

    S['chap_num']    = s('chap_num',    fontName='Times-Roman',fontSize=10,
                         alignment=TA_CENTER,spaceBefore=72,spaceAfter=4,tracking=3)
    S['chap_title']  = s('chap_title',  fontName='Times-Bold',fontSize=28,leading=36,
                         alignment=TA_CENTER,spaceAfter=8,spaceBefore=8)
    S['chap_sub']    = s('chap_sub',    fontName='Times-Italic',fontSize=13,leading=19,
                         alignment=TA_CENTER,spaceAfter=36)
    S['section']     = s('section',     fontName='Times-Bold',fontSize=13,leading=18,
                         alignment=TA_LEFT,spaceBefore=20,spaceAfter=6,
                         firstLineIndent=0)   # keepWithNext removed; _SectionHead enforces
                                              # minimum room via wrap() override.
    S['subsection']  = s('subsection',  fontName='Times-BoldItalic',fontSize=11,leading=16,
                         alignment=TA_LEFT,spaceBefore=12,spaceAfter=4,
                         firstLineIndent=0)
    S['caption']     = s('caption',     fontName='Times-Italic',fontSize=9.5,leading=13,
                         alignment=TA_CENTER,spaceAfter=14,spaceBefore=3)
    S['epigraph']    = s('epigraph',    fontName='Times-Italic',fontSize=11,leading=16,
                         alignment=TA_CENTER,leftIndent=54,rightIndent=54,
                         spaceBefore=12,spaceAfter=2)
    S['epig_attr']   = s('epig_attr',   fontName='Times-Roman',fontSize=9,leading=13,
                         alignment=TA_CENTER,leftIndent=54,rightIndent=54,spaceAfter=20)
    S['blockquote']  = s('blockquote',  fontName='Times-Italic',fontSize=10.5,leading=15,
                         leftIndent=36,rightIndent=36,spaceBefore=8,spaceAfter=8,
                         firstLineIndent=0,alignment=TA_JUSTIFY)
    S['theorem']     = s('theorem',     fontName='Times-Bold',fontSize=11,leading=16,
                         leftIndent=12,firstLineIndent=0,spaceAfter=2,spaceBefore=8)
    S['theorem_b']   = s('theorem_b',   fontName='Times-Italic',fontSize=11,leading=16,
                         leftIndent=12,firstLineIndent=0,spaceAfter=8)
    S['list']        = s('list',        leftIndent=24,firstLineIndent=-12,spaceAfter=3)
    S['part_label']  = s('part_label',  fontName='Times-Roman',fontSize=12,
                         alignment=TA_CENTER,spaceBefore=100,spaceAfter=10,tracking=4)
    S['part_title']  = s('part_title',  fontName='Times-Bold',fontSize=36,leading=44,
                         alignment=TA_CENTER,spaceAfter=16)
    S['part_desc']   = s('part_desc',   fontName='Times-Italic',fontSize=13,leading=19,
                         alignment=TA_CENTER,leftIndent=48,rightIndent=48)
    S['cover_title'] = s('cover_title', fontName='Times-Bold',fontSize=46,leading=56,
                         alignment=TA_CENTER,spaceAfter=18,spaceBefore=108)
    S['cover_sub']   = s('cover_sub',   fontName='Times-Italic',fontSize=18,leading=26,
                         alignment=TA_CENTER,spaceAfter=48)
    S['cover_auth']  = s('cover_auth',  fontName='Times-Roman',fontSize=15,leading=22,
                         alignment=TA_CENTER,spaceAfter=6)
    S['cover_year']  = s('cover_year',  fontName='Times-Roman',fontSize=11,
                         alignment=TA_CENTER)
    S['toc_h']       = s('toc_h',       fontName='Times-Bold',fontSize=20,leading=28,
                         alignment=TA_CENTER,spaceBefore=36,spaceAfter=24)
    S['toc_part']    = s('toc_part',    fontName='Times-Bold',fontSize=11,
                         spaceBefore=12,spaceAfter=2,firstLineIndent=0)
    S['toc_chap']    = s('toc_chap',    fontName='Times-Roman',fontSize=10.5,leading=16,
                         leftIndent=16,firstLineIndent=0,spaceAfter=1)
    S['toc_sub']     = s('toc_sub',     fontName='Times-Roman',fontSize=9.5,leading=14,
                         leftIndent=32,firstLineIndent=0,
                         textColor=colors.HexColor('#444444'))
    S['preface_t']   = s('preface_t',   fontName='Times-Bold',fontSize=18,leading=24,
                         alignment=TA_CENTER,spaceBefore=60,spaceAfter=20)
    S['preface']     = s('preface',     firstLineIndent=18,spaceAfter=7)
    S['note']        = s('note',        fontName='Times-Italic',fontSize=10,leading=14,
                         leftIndent=30,rightIndent=30,spaceAfter=8,firstLineIndent=0)
    # ── math display styles ───────────────────────────────────────────────
    S['theorem_head'] = s('theorem_head',
        fontName='Helvetica-Bold', fontSize=8.5, leading=13,
        textColor=colors.white, alignment=TA_LEFT,
        firstLineIndent=0, spaceBefore=0, spaceAfter=0)
    S['formula']     = s('formula',
        fontName='Times-Italic', fontSize=11.5, leading=18,
        alignment=TA_CENTER, spaceBefore=10, spaceAfter=10,
        firstLineIndent=0)
    return S

# ─── PAGE CALLBACKS ───────────────────────────────────────────────────────────
def on_page(c, doc):
    pg = doc.page
    if pg <= 2: return  # cover + blank
    c.saveState()
    c.setFont('Times-Italic',8.5)
    c.setStrokeColor(colors.black); c.setLineWidth(0.3)
    # top rule
    c.line(ML, PH-MT+10, PW-MR, PH-MT+10)
    if pg%2==0:
        c.drawString(ML, PH-MT+16, "More Solutions = More Problems")
    else:
        c.drawRightString(PW-MR, PH-MT+16, G['chapter'])
    # bottom rule + page number
    c.line(ML, MB-10, PW-MR, MB-10)
    c.setFont('Times-Roman',9)
    c.drawCentredString(PW/2, MB-22, str(pg-2))
    c.restoreState()

# ── Designed front cover (ported from book_cover.py, scaled to A4) ──────────
_COVER_INK       = colors.HexColor('#0A0A0A')   # near-black titles + bars
_COVER_INK_LIGHT = colors.HexColor('#666666')   # grey "MORE" / subtitle / "Engineer · Thinker"
_COVER_INK_XLIT  = colors.HexColor('#999999')   # very light grey hairlines
_COVER_BG        = colors.HexColor('#FFFFFF')   # white background


def _draw_cascade_symbol(c, cx, cy, sym_w, sym_h):
    """A 3-level binary tree drawn with canvas primitives.
    Root at top, 8 leaves at the bottom; all in solid black."""
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
        c.setFillColor(_COVER_INK)
        for i in range(n):
            c.circle(nx(lv, i), ny(lv), r, fill=1, stroke=0)


def _draw_designed_cover(c, W, H):
    """Render the front cover used by book_cover.py, scaled to A4.

    Layout uses percentages of W and H, so it scales between the 6x9 trade
    paperback size and A4 without any per-element retuning. Font sizes are
    scaled proportionally to the page height so they stay visually correct.
    """
    scale = H / (9 * inch)            # A4 height vs. original 9-inch cover
    bar_h = 0.04 * inch

    # white background
    c.setFillColor(_COVER_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # top black bar
    c.setFillColor(_COVER_INK)
    c.rect(0, H - bar_h, W, bar_h, fill=1, stroke=0)

    # cascade tree symbol — upper portion
    _draw_cascade_symbol(c,
        cx=W / 2,
        cy=H * 0.790,
        sym_w=1.9 * inch * scale,
        sym_h=1.05 * inch * scale)

    # "MORE" (small grey, above SOLUTIONS)
    c.setFont('Helvetica', 13 * scale)
    c.setFillColor(_COVER_INK_LIGHT)
    c.drawCentredString(W / 2, H * 0.638, 'MORE')

    # "SOLUTIONS" — huge bold
    c.setFont('Helvetica-Bold', 46 * scale)
    c.setFillColor(_COVER_INK)
    c.drawCentredString(W / 2, H * 0.570, 'SOLUTIONS')

    # "=" with flanking hairlines
    c.setStrokeColor(_COVER_INK_XLIT)
    c.setLineWidth(0.55)
    c.line(W * 0.18, H * 0.530, W * 0.82, H * 0.530)

    c.setFont('Helvetica', 18 * scale)
    c.setFillColor(_COVER_INK_LIGHT)
    c.drawCentredString(W / 2, H * 0.513, '=')

    c.line(W * 0.18, H * 0.497, W * 0.82, H * 0.497)

    # "MORE" (small grey, above PROBLEMS)
    c.setFont('Helvetica', 13 * scale)
    c.setFillColor(_COVER_INK_LIGHT)
    c.drawCentredString(W / 2, H * 0.464, 'MORE')

    # "PROBLEMS" — huge bold
    c.setFont('Helvetica-Bold', 46 * scale)
    c.setFillColor(_COVER_INK)
    c.drawCentredString(W / 2, H * 0.395, 'PROBLEMS')

    # subtitle hairline + italic two-line subtitle
    c.setStrokeColor(_COVER_INK_XLIT)
    c.setLineWidth(0.5)
    c.line(W * 0.28, H * 0.360, W * 0.72, H * 0.360)

    c.setFont('Times-Italic', 10 * scale)
    c.setFillColor(_COVER_INK_LIGHT)
    c.drawCentredString(W / 2, H * 0.335, 'Why Progress Breeds New Problems —')
    c.drawCentredString(W / 2, H * 0.315, 'and How to Get Ahead of the Cascade')

    # bottom black bar
    c.setFillColor(_COVER_INK)
    c.rect(0, 0, W, bar_h, fill=1, stroke=0)

    # AHMED HAFDI + role line, pinned to bottom
    c.setFont('Helvetica-Bold', 14 * scale)
    c.setFillColor(_COVER_INK)
    c.drawCentredString(W / 2, 0.22 * inch + bar_h, 'AHMED HAFDI')

    c.setFont('Helvetica', 7.5 * scale)
    c.setFillColor(_COVER_INK_LIGHT)
    c.drawCentredString(W / 2, 0.09 * inch + bar_h, 'Software Engineer  ·  Thinker')


def on_first(c, doc):
    # Page 1 is the designed cover, drawn directly on the canvas.
    _draw_designed_cover(c, PW, PH)

# ─── FIGURE FACTORY ───────────────────────────────────────────────────────────
# Two styles are used deliberately:
#   • clean_style()  — for charts that plot numbers (data or mathematical curves).
#                      A sober, professional look so quantitative figures are not
#                      undermined by a hand-drawn aesthetic.
#   • plt.xkcd()     — kept ONLY for conceptual diagrams (trees, timelines, concept
#                      maps) where the sketch look correctly signals "schematic idea,
#                      not measurement."
from contextlib import contextmanager

@contextmanager
def clean_style():
    """Professional chart style for quantitative figures (replaces the xkcd sketch)."""
    rc = {
        'font.family': 'serif',
        'font.size': 10,
        'axes.titlesize': 12, 'axes.titleweight': 'bold',
        'axes.grid': True, 'grid.alpha': 0.30, 'grid.linewidth': 0.6,
        'axes.spines.top': False, 'axes.spines.right': False,
        'axes.edgecolor': '#333333', 'axes.linewidth': 0.8,
        'lines.linewidth': 2.0,
    }
    with plt.rc_context(rc):
        yield

def fig_to_image(fig, w=5.0*inch, h=3.2*inch):
    buf=BytesIO(); fig.savefig(buf,format='png',dpi=160,bbox_inches='tight',
                               facecolor='white',edgecolor='none')
    buf.seek(0); plt.close(fig); return Image(buf,width=w,height=h)

def fig_exponential_cascade():
    with clean_style():
        fig,ax=plt.subplots(figsize=(6.5,3.8))
        n=np.arange(0,11)
        ax.plot(n, 2**n, 'k-', lw=2.5, label='Problems (traditional): $O(2^n)$')
        ax.plot(n, n**2,  'k--',lw=2,   label='Interactions: $O(n^2)$')
        ax.plot(n, n,     'k:', lw=2,   label='Solutions added: $O(n)$')
        ax.set_xlim(0,10); ax.set_ylim(0,600)
        ax.set_xlabel('Number of Solutions Introduced', fontsize=11)
        ax.set_ylabel('Count', fontsize=11)
        ax.set_title('Why More Solutions = More Problems', fontsize=12, fontweight='bold')
        ax.legend(fontsize=9, loc='upper left')
        ax.annotate('Each new solution\ninteracts with all others!',
                    xy=(8,256), xytext=(5.5,450),
                    arrowprops=dict(arrowstyle='->', lw=1.5),fontsize=9)
        fig.tight_layout()
    return fig

def fig_cascade_tree():
    with plt.xkcd():
        fig,ax=plt.subplots(figsize=(6.5,4.2))
        ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
        # Root
        ax.annotate('', xy=(5,8), xytext=(5,9.2),
                    arrowprops=dict(arrowstyle='->', lw=2))
        ax.text(5,9.5,'ORIGINAL\nPROBLEM',ha='center',va='center',fontsize=9,
                bbox=dict(boxstyle='round',fc='white',ec='black',lw=1.5))
        ax.text(5,7.5,'SOLUTION',ha='center',va='center',fontsize=9,
                bbox=dict(boxstyle='round',fc='lightgray',ec='black',lw=1.5))
        # Level 2
        for x,label in [(2.5,'New Problem A'),(7.5,'New Problem B')]:
            ax.annotate('',xy=(x,5.8),xytext=(5,7.2),
                        arrowprops=dict(arrowstyle='->',lw=1.5,color='black'))
            ax.text(x,5.4,label,ha='center',va='center',fontsize=8,
                    bbox=dict(boxstyle='round',fc='white',ec='black'))
        # Level 3
        positions=[(1,3.2,'Fix A.1'),(3,3.2,'Fix A.2'),(6.2,3.2,'Fix B.1'),(8.5,3.2,'Fix B.2')]
        parents=[(2.5,5.1),(2.5,5.1),(7.5,5.1),(7.5,5.1)]
        for (px,py),(x,y,l) in zip(parents,positions):
            ax.annotate('',xy=(x,y+0.5),xytext=(px,py),
                        arrowprops=dict(arrowstyle='->',lw=1.2,color='gray'))
            ax.text(x,y,l,ha='center',va='center',fontsize=7,
                    bbox=dict(boxstyle='round',fc='lightyellow',ec='gray'))
        # Level 4 sprouts (RNG seeded so the figure is reproducible across builds)
        rng = np.random.RandomState(42)
        for x in [0.3,1.7,2.3,3.7,5.5,6.9,7.8,9.2]:
            ax.text(x,1.6,'?',ha='center',fontsize=10,color='gray')
            ax.plot([x,x+rng.uniform(-0.2,0.2)],[1.9,2.6],'k-',alpha=0.3,lw=0.8)
        ax.text(5,0.6,'Each fix spawns more problems...',ha='center',
                fontsize=9,fontstyle='italic',color='gray')
        ax.set_title('The Cascade Tree: One Fix, Infinite Branches', fontsize=11, fontweight='bold')
        fig.tight_layout()
    return fig

def fig_antibiotic_resistance():
    with clean_style():
        fig,ax=plt.subplots(figsize=(6.5,3.6))
        years=np.array([1945,1955,1965,1975,1985,1995,2005,2015,2025])
        drugs=np.array([2,5,12,18,22,28,35,40,43])
        resistant=np.array([0,1,3,6,10,16,24,33,42])
        ax.fill_between(years,drugs,alpha=0.25,color='black',label='Antibiotics available')
        ax.fill_between(years,resistant,alpha=0.5,color='black',
                        label='Resistant strains known')
        ax.plot(years,drugs,'k-',lw=2); ax.plot(years,resistant,'k--',lw=2)
        ax.set_xlabel('Year'); ax.set_ylabel('Count (approximate)')
        ax.set_title('The Antibiotic Paradox: More Drugs -> More Resistance', fontsize=11, fontweight='bold')
        ax.legend(fontsize=9)
        ax.annotate('Lines converge:\nevery drug\ncreates resistance',
                    xy=(2015,33),xytext=(1975,36),
                    arrowprops=dict(arrowstyle='->',lw=1.5),fontsize=8)
        fig.tight_layout()
    return fig

def fig_jevons_paradox():
    with clean_style():
        fig,ax=plt.subplots(figsize=(6.5,3.6))
        years=np.arange(1850,1920)
        efficiency=50+np.cumsum(np.random.RandomState(42).uniform(0.3,0.8,len(years)))
        coal=300+np.cumsum(np.random.RandomState(7).uniform(1.5,4,len(years)))
        ax2=ax.twinx()
        ax.plot(years,efficiency,'k-',lw=2.5,label='Engine Efficiency (index)')
        ax2.plot(years,coal,'k--',lw=2.5,label='Coal Consumption (Mt)')
        ax.set_xlabel('Year'); ax.set_ylabel('Efficiency Index',color='black')
        ax2.set_ylabel('Coal Consumed (Mt)',color='black')
        ax.set_title("Jevons Paradox (1865): More Efficient -> More Consumed", fontsize=11, fontweight='bold')
        lines1,labels1=ax.get_legend_handles_labels()
        lines2,labels2=ax2.get_legend_handles_labels()
        ax.legend(lines1+lines2,labels1+labels2,fontsize=9,loc='upper left')
        ax.text(1890,efficiency[40]+8,'Better engines!',fontsize=8,color='black')
        ax2.text(1880,coal[30]+15,'...more coal burned',fontsize=8,color='black')
        fig.tight_layout()
    return fig

def fig_brooks_law():
    with clean_style():
        fig,ax=plt.subplots(figsize=(6.5,3.6))
        n=np.arange(1,21)
        links=n*(n-1)/2
        ax.bar(n,links,color='gray',alpha=0.7,edgecolor='black',lw=0.7)
        ax.set_xlabel('Number of Developers on Project')
        ax.set_ylabel('Communication Channels n(n-1)/2')
        ax.set_title("Brooks' Law: Adding People Adds Complexity Faster", fontsize=11, fontweight='bold')
        ax.annotate('5 devs = 10 channels',xy=(5,10),xytext=(8,80),
                    arrowprops=dict(arrowstyle='->',lw=1.5),fontsize=9)
        ax.annotate('20 devs = 190 channels!',xy=(20,190),xytext=(13,170),
                    arrowprops=dict(arrowstyle='->',lw=1.5),fontsize=9)
        fig.tight_layout()
    return fig

def fig_opioid_crisis():
    with clean_style():
        fig,ax=plt.subplots(figsize=(6.5,3.6))
        years=np.array([1999,2002,2005,2008,2011,2014,2017,2020,2023])
        deaths=np.array([6,9,15,20,26,35,47,70,81])
        ax.fill_between(years,deaths,alpha=0.35,color='black')
        ax.plot(years,deaths,'k-o',lw=2.5,markersize=5)
        ax.axvline(1995,color='black',lw=1.5,linestyle=':',alpha=0.7)
        ax.text(1995.5,65,'OxyContin\napproved\n(1995)',fontsize=8,va='top')
        ax.set_xlabel('Year'); ax.set_ylabel('Overdose Deaths (thousands, USA)')
        ax.set_title('The Opioid Cascade: Solving Pain Created an Epidemic', fontsize=11, fontweight='bold')
        ax.set_ylim(0,100)
        fig.tight_layout()
    return fig

def fig_prohibition():
    with clean_style():
        fig,ax=plt.subplots(figsize=(6.5,3.6))
        cats=['Alcohol-related\nhomicides (index)','Organized crime\ngroups','Police\ncorruption cases',
              'Illegal speakeasies\n(thousands)']
        pre=[1,1,1,0]
        during=[3.8,4.2,3.1,3.2]
        x=np.arange(len(cats)); w=0.35
        ax.bar(x-w/2,pre,w,label='Pre-Prohibition (1919)',color='white',edgecolor='black',lw=1.5)
        ax.bar(x+w/2,during,w,label='During Prohibition (1928)',color='gray',alpha=0.8,edgecolor='black',lw=1.2)
        ax.set_xticks(x); ax.set_xticklabels(cats,fontsize=8)
        ax.set_ylabel('Relative Index (Pre = 1.0)')
        ax.set_title('Prohibition (1920–33): Solving Drinking Created Crime', fontsize=11, fontweight='bold')
        ax.legend(fontsize=9); ax.set_ylim(0,5)
        fig.tight_layout()
    return fig

def fig_godel_timeline():
    with plt.xkcd():
        fig,ax=plt.subplots(figsize=(6.5,3.8))
        ax.set_xlim(0,12); ax.set_ylim(0,8); ax.axis('off')
        events=[
            (1,6.5,'1870s\nCantor:\nSet Theory','white'),
            (3.5,6.5,'1901\nRussell\'s\nParadox','lightgray'),
            (6,6.5,'1910\nPrincipia\nMathematica','white'),
            (8.5,6.5,'1931\nGödel:\nIncompleteness','lightgray'),
            (11,6.5,'1936\nTuring:\nHalting\nProblem','white'),
        ]
        for i,(x,y,label,fc) in enumerate(events):
            ax.text(x,y,label,ha='center',va='center',fontsize=8,
                    bbox=dict(boxstyle='round,pad=0.4',fc=fc,ec='black',lw=1.5))
            if i<len(events)-1:
                ax.annotate('',xy=(events[i+1][0]-0.8,y),xytext=(x+0.8,y),
                            arrowprops=dict(arrowstyle='->',lw=1.5))
        problems=[
            (2.25,4.2,'-> Naive set\ntheory breaks'),
            (4.75,4.2,'-> New axioms\nneeded'),
            (7.25,4.2,'-> Can\'t prove\nall truths'),
            (9.75,4.2,'-> Some problems\nundecidable'),
        ]
        for x,y,text in problems:
            ax.text(x,y,text,ha='center',va='top',fontsize=7.5,color='gray',fontstyle='italic')
        ax.text(6,2.2,'Each "solution" to mathematics opened a deeper abyss.',
                ha='center',fontsize=9,fontstyle='italic',color='black')
        ax.set_title("Mathematics' Cascade: Solving Foundations Created Undecidability", fontsize=10, fontweight='bold')
        fig.tight_layout()
    return fig

def fig_windows_complexity():
    with clean_style():
        fig,ax=plt.subplots(figsize=(6.5,3.6))
        versions=['Win 1.0\n(1985)','Win 95\n(1995)','Win XP\n(2001)','Win 7\n(2009)','Win 10\n(2015)','Win 11\n(2021)']
        loc_million=[0.001,15,45,40,80,100]
        install_gb=[0.001,0.055,1.5,20,32,64]
        x=np.arange(len(versions))
        ax.bar(x,loc_million,color='gray',alpha=0.7,edgecolor='black',lw=0.8,label='Code (millions of lines)')
        ax.set_xlabel('Windows Version'); ax.set_ylabel('Millions of lines of code')
        ax.set_xticks(x); ax.set_xticklabels(versions,fontsize=8)
        ax.set_title('Feature Bloat: Every Feature Adds Complexity', fontsize=11, fontweight='bold')
        ax.annotate('Solving one user need\nadds 1,000 edge cases',
                    xy=(4,80),xytext=(1.5,88),
                    arrowprops=dict(arrowstyle='->',lw=1.5),fontsize=8)
        fig.tight_layout()
    return fig

def fig_social_media():
    with clean_style():
        fig,ax=plt.subplots(figsize=(6.5,3.6))
        years=np.array([2004,2007,2010,2013,2016,2019,2022])
        users_bn=np.array([0.001,0.05,0.5,1.2,2.1,3.5,4.7])
        loneliness=np.array([1.0,1.05,1.15,1.28,1.45,1.62,1.8])
        teen_anxiety=np.array([1.0,1.02,1.08,1.2,1.45,1.7,1.95])
        ax2=ax.twinx()
        ax.plot(years,users_bn,'k-',lw=2.5,label='Global social media users (bn)')
        ax2.plot(years,loneliness,'k--',lw=2,label='Loneliness index')
        ax2.plot(years,teen_anxiety,'k:',lw=2,label='Teen anxiety index')
        ax.set_xlabel('Year'); ax.set_ylabel('Users (billions)')
        ax2.set_ylabel('Index (2004 = 1.0)')
        ax.set_title('Social Media: Connecting Everyone -> Everyone Alone', fontsize=11, fontweight='bold')
        lines1,l1=ax.get_legend_handles_labels(); lines2,l2=ax2.get_legend_handles_labels()
        ax.legend(lines1+lines2,l1+l2,fontsize=8,loc='upper left')
        fig.tight_layout()
    return fig

def fig_cascade_risk_index():
    with plt.xkcd():
        fig,ax=plt.subplots(figsize=(6.5,3.8))
        ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
        ax.text(5,9.3,'Cascade Risk Index (CRI)', ha='center', fontsize=13, fontweight='bold')
        formula=r'CRI(s, E) = C(s) × Φ(s) × N(s)^α'
        ax.text(5,7.8,formula,ha='center',fontsize=14,family='monospace',
                bbox=dict(boxstyle='round',fc='lightyellow',ec='black',lw=2))
        components=[
            (2,5.8,'C(s)','Cascade\nCoefficient\n(0–1)'),
            (5,5.8,'Φ(s)','System\nComplexity\n(log scale)'),
            (8,5.8,'N(s)^α','Network\nReach\n(α > 1)'),
        ]
        for x,y,sym,desc in components:
            ax.text(x,y+0.5,sym,ha='center',fontsize=12,fontweight='bold',
                    bbox=dict(boxstyle='round',fc='white',ec='black',lw=1.5))
            ax.text(x,y-0.6,desc,ha='center',fontsize=8.5,color='gray')
            ax.annotate('',xy=(x,y+0.0),xytext=(5,7.2),
                        arrowprops=dict(arrowstyle='-',lw=0.8,color='gray'))
        ax.text(5,2.8,'CRI < 0.3 -> Safe to deploy',ha='center',fontsize=9)
        ax.text(5,2.1,'CRI 0.3–0.6 -> Proceed with caution',ha='center',fontsize=9)
        ax.text(5,1.4,'CRI > 0.6 -> Redesign required',ha='center',fontsize=9,color='gray')
        fig.tight_layout()
    return fig

def fig_crispr():
    with plt.xkcd():
        fig,ax=plt.subplots(figsize=(6.5,3.8))
        ax.set_xlim(0,10); ax.set_ylim(0,8); ax.axis('off')
        ax.text(5,7.5,'CRISPR-Cas9: Precision That Isn\'t', ha='center',
                fontsize=12, fontweight='bold')
        ax.text(5,6.4,'Target Gene (intended edit)',ha='center',fontsize=10,
                bbox=dict(boxstyle='round',fc='lightgray',ec='black',lw=2))
        np.random.seed(42)
        for i in range(7):
            x=np.random.uniform(0.5,9.5); y=np.random.uniform(1,5)
            ax.text(x,y,'off-target\ncut',ha='center',fontsize=7,color='gray',
                    bbox=dict(boxstyle='round',fc='white',ec='gray',lw=0.8,alpha=0.7))
            ax.annotate('',xy=(x,y+0.4),xytext=(5,5.8),
                        arrowprops=dict(arrowstyle='->',lw=0.7,color='lightgray'))
        ax.text(5,0.5,'Every precision cut may silently edit elsewhere in the genome.',
                ha='center',fontsize=8.5,fontstyle='italic',color='black')
        fig.tight_layout()
    return fig

def fig_goodhart():
    with clean_style():
        fig,ax=plt.subplots(figsize=(6.5,3.6))
        t=np.linspace(0,10,200)
        real=2+0.5*t+np.sin(t)*0.8+np.random.RandomState(3).randn(200)*0.3
        measured=real.copy()
        # After measurement becomes target, metric diverges from reality
        measured[100:]=measured[100]+(t[100:]-t[100])*0.8
        real[100:]=real[100]+(t[100:]-t[100])*0.1
        ax.plot(t,real,'k-',lw=2.5,label='Actual performance')
        ax.plot(t,measured,'k--',lw=2.5,label='Measured metric (now a target)')
        ax.axvline(t[100],color='black',lw=1.5,linestyle=':')
        ax.text(t[100]+0.2,real[100]+0.5,'Metric\nbecomes\ntarget',fontsize=8)
        ax.set_xlabel('Time'); ax.set_ylabel('Value')
        ax.set_title("Goodhart's Law: Measuring It Breaks It", fontsize=11, fontweight='bold')
        ax.legend(fontsize=9)
        fig.tight_layout()
    return fig

def fig_nuclear_waste():
    with plt.xkcd():
        fig,ax=plt.subplots(figsize=(6.5,3.6))
        ax.set_xlim(0,10); ax.set_ylim(0,8); ax.axis('off')
        timeline=[
            (0.8,6,'1938\nNuclear\nfission\ndiscovered'),
            (3,6,'1945\nFirst\nnuclear\nreactor'),
            (5.2,6,'1954\nFirst\nnuclear\npower\nplant'),
            (7.4,6,'1986\nChernobyl\ndisaster'),
            (9.2,6,'Now\n90,000-yr\nwaste\nproblem'),
        ]
        for i,(x,y,label) in enumerate(timeline):
            fc='white' if i%2==0 else 'lightgray'
            ax.text(x,y,label,ha='center',va='center',fontsize=7.5,
                    bbox=dict(boxstyle='round',fc=fc,ec='black',lw=1.3))
            if i<len(timeline)-1:
                ax.annotate('',xy=(timeline[i+1][0]-0.6,y),xytext=(x+0.6,y),
                            arrowprops=dict(arrowstyle='->',lw=1.5))
        ax.text(9.2,4.2,'Still no\npermanent\nsolution',ha='center',fontsize=8,
                color='gray',fontstyle='italic')
        ax.annotate('',xy=(9.2,4.8),xytext=(9.2,5.3),
                    arrowprops=dict(arrowstyle='->',lw=1,color='gray'))
        ax.text(5,2.2,'The "clean energy" solution created a waste problem\nthat will outlast all of recorded human civilization.',
                ha='center',fontsize=9,fontstyle='italic')
        ax.set_title('Nuclear Power: Clean Energy, Eternal Waste', fontsize=11, fontweight='bold')
        fig.tight_layout()
    return fig

def fig_historical_timeline():
    with plt.xkcd():
        fig,ax=plt.subplots(figsize=(6.5,5.0))
        ax.set_xlim(0,10); ax.set_ylim(0,12); ax.axis('off')
        ax.set_title('Selected Solution->Problem Pairs Through History', fontsize=11, fontweight='bold')
        rows=[
            (1800,'Steamboat (mobility)','River monopolies, explosions'),
            (1860,'Railroad (speed)','Land dispossession, pollution'),
            (1900,'Automobile (freedom)','Sprawl, 1.35M deaths/yr'),
            (1928,'Penicillin (infection)','Antibiotic resistance'),
            (1950,'Pesticides (food supply)','Ecosystem collapse'),
            (1962,'Green Revolution (hunger)','Soil degradation, monoculture'),
            (1969,'Internet (communication)','Cybercrime, misinformation'),
            (1995,'OxyContin (pain)','500,000+ overdose deaths'),
            (2004,'Social media (connection)','Polarization, mental health crisis'),
            (2022,'AI (productivity)','Alignment problem, job disruption'),
        ]
        y=11
        ax.text(0.3,y+0.4,'Year',fontsize=8.5,fontweight='bold')
        ax.text(3.5,y+0.4,'Solution',fontsize=8.5,fontweight='bold')
        ax.text(7,y+0.4,'Problem Created',fontsize=8.5,fontweight='bold')
        ax.axhline(y+0.2,color='black',lw=0.8)
        for year,sol,prob in rows:
            y-=1
            ax.text(0.3,y+0.15,str(year),fontsize=8,va='center')
            ax.text(3.5,y+0.15,sol,fontsize=7.5,va='center')
            ax.text(7,y+0.15,prob,fontsize=7.5,va='center',color='gray')
            ax.axhline(y-0.3,color='lightgray',lw=0.4)
        fig.tight_layout()
    return fig

def fig_green_revolution():
    with clean_style():
        fig,ax=plt.subplots(figsize=(6.5,3.6))
        years=np.array([1960,1970,1980,1990,2000,2010,2020])
        yield_idx=np.array([100,142,175,198,220,250,270])
        soil_health=np.array([100,95,88,78,65,52,40])
        biodiversity=np.array([100,96,88,75,62,50,38])
        ax.plot(years,yield_idx,'k-',lw=2.5,label='Crop yield index')
        ax.plot(years,soil_health,'k--',lw=2,label='Soil health index')
        ax.plot(years,biodiversity,'k:',lw=2,label='Agricultural biodiversity')
        ax.axhline(100,color='gray',lw=0.5,linestyle='-')
        ax.set_xlabel('Year'); ax.set_ylabel('Index (1960 = 100)')
        ax.set_title('The Green Revolution: Fed the World, Starved the Soil', fontsize=11, fontweight='bold')
        ax.legend(fontsize=9)
        ax.annotate('Yields up\n170%',xy=(2020,270),xytext=(1985,260),
                    arrowprops=dict(arrowstyle='->',lw=1.5),fontsize=8)
        ax.annotate('Soil health\ndown 60%',xy=(2020,40),xytext=(1985,30),
                    arrowprops=dict(arrowstyle='->',lw=1.5),fontsize=8)
        fig.tight_layout()
    return fig

def fig_quantum_problems():
    with plt.xkcd():
        fig,ax=plt.subplots(figsize=(6.5,3.8))
        ax.set_xlim(0,10); ax.set_ylim(0,8); ax.axis('off')
        ax.set_title('Quantum Mechanics: Solving Atomic Structure -> New Problems', fontsize=11, fontweight='bold')
        center_items=[
            (5,6.8,'PROBLEM: Why do atoms\nnot collapse?'),
            (5,4.8,'SOLUTION: Quantum Mechanics\n(Bohr, Heisenberg, Schrödinger, 1920s)'),
        ]
        for x,y,text in center_items:
            ax.text(x,y,text,ha='center',va='center',fontsize=9,
                    bbox=dict(boxstyle='round',fc='white',ec='black',lw=1.5))
        new_problems=[
            (1.5,2.5,'What does\nmeasurement mean?'),
            (3.8,2.5,'Are there\nmany worlds?'),
            (6.2,2.5,'Why does\ntime have\na direction?'),
            (8.5,2.5,'Quantum\ngravity?'),
        ]
        for x,y,text in new_problems:
            ax.text(x,y,text,ha='center',va='center',fontsize=7.5,
                    bbox=dict(boxstyle='round',fc='lightyellow',ec='gray',lw=1))
            ax.annotate('',xy=(x,y+0.55),xytext=(5,4.3),
                        arrowprops=dict(arrowstyle='->',lw=1,color='gray'))
        ax.text(5,0.8,'100 years later, physicists still debate what quantum mechanics means.',
                ha='center',fontsize=8.5,fontstyle='italic')
        fig.tight_layout()
    return fig

def fig_drug_war():
    with clean_style():
        fig,ax=plt.subplots(figsize=(6.5,3.6))
        years=np.array([1971,1980,1990,2000,2010,2020])
        spending_bn=np.array([1,3.5,7,18,26,35])
        incarceration=np.array([200,300,600,1000,1400,1800])
        ax2=ax.twinx()
        ax.plot(years,spending_bn,'k-',lw=2.5,label='Annual drug war spending ($bn)')
        ax2.plot(years,incarceration,'k--',lw=2.5,label='Drug-related incarcerations (thousands)')
        ax.set_xlabel('Year'); ax.set_ylabel('Spending ($bn)',color='black')
        ax2.set_ylabel('Incarcerations (thousands)',color='black')
        ax.set_title('The War on Drugs: $1 Trillion Spent, Problem Unchanged', fontsize=11, fontweight='bold')
        lines1,l1=ax.get_legend_handles_labels(); lines2,l2=ax2.get_legend_handles_labels()
        ax.legend(lines1+lines2,l1+l2,fontsize=8.5,loc='upper left')
        ax.text(1990,22,'Drug use rates:\nstatistically unchanged',fontsize=8,
                fontstyle='italic',color='gray')
        fig.tight_layout()
    return fig

def fig_cdi_financial():
    with plt.xkcd():
        fig,ax=plt.subplots(figsize=(6.5,3.8))
        ax.set_xlim(0,10); ax.set_ylim(0,8); ax.axis('off')
        ax.set_title('2008 Crisis: CDOs Meant to Reduce Risk -> Systemic Collapse', fontsize=11, fontweight='bold')
        items=[
            (2,6.8,'Mortgage\nDefaults','white'),
            (5,6.8,'Bundle into\nCDOs','lightgray'),
            (8,6.8,'AAA Rating\nassigned','white'),
        ]
        for x,y,text,fc in items:
            ax.text(x,y,text,ha='center',va='center',fontsize=9,
                    bbox=dict(boxstyle='round',fc=fc,ec='black',lw=1.5))
        for i in range(len(items)-1):
            ax.annotate('',xy=(items[i+1][0]-0.6,items[i+1][1]),
                        xytext=(items[i][0]+0.6,items[i][1]),
                        arrowprops=dict(arrowstyle='->',lw=1.8))
        problems=[
            (1.5,4,'Hid underlying\nrisk'),
            (4,4,'Correlated assets\ncollapse together'),
            (6.5,4,'Rating agencies\ncompromised'),
            (9,4,'Systemic\ncontagion'),
        ]
        for x,y,text in problems:
            ax.text(x,y,text,ha='center',va='center',fontsize=7.5,
                    bbox=dict(boxstyle='round',fc='lightyellow',ec='gray',lw=1))
            ax.annotate('',xy=(x,y+0.5),xytext=(5,6.3),
                        arrowprops=dict(arrowstyle='->',lw=0.8,color='gray'))
        ax.text(5,2.0,'Result: $22 trillion in global wealth destroyed (2008–2009)',
                ha='center',fontsize=9,fontweight='bold',
                bbox=dict(boxstyle='round',fc='white',ec='black',lw=1.5))
        fig.tight_layout()
    return fig

def fig_p_vs_np():
    with plt.xkcd():
        fig,ax=plt.subplots(figsize=(6.5,3.6))
        ax.set_xlim(0,10); ax.set_ylim(0,8); ax.axis('off')
        ax.set_title("Hilbert's 10th Problem -> The P vs NP Abyss", fontsize=11, fontweight='bold')
        steps=[
            (1.2,6,'1900\nHilbert asks:\nCan all math\nbe decided?'),
            (5,6,'1931\nGödel:\nSome truths\nare unprovable'),
            (8.8,6,'1936\nTuring:\nSome problems\nare undecidable'),
        ]
        for x,y,text in steps:
            ax.text(x,y,text,ha='center',va='center',fontsize=8.5,
                    bbox=dict(boxstyle='round,pad=0.4',fc='white',ec='black',lw=1.5))
        ax.annotate('',xy=(3.2,6),xytext=(2.2,6),arrowprops=dict(arrowstyle='->',lw=1.8))
        ax.annotate('',xy=(7,6),xytext=(6.8,6),arrowprops=dict(arrowstyle='->',lw=1.8))
        ax.text(5,4,'Each answer revealed deeper questions',ha='center',fontsize=10,
                fontstyle='italic',color='gray')
        ax.text(5,3,'Now: P vs NP, the $1M question nobody can answer',
                ha='center',fontsize=9,
                bbox=dict(boxstyle='round',fc='lightyellow',ec='black',lw=1.5))
        ax.text(5,1.5,'The very act of formalizing mathematics\ncreated infinite new open problems.',
                ha='center',fontsize=9,fontstyle='italic')
        fig.tight_layout()
    return fig

# =============================================================================
# CONTENT BUILDER HELPERS
# =============================================================================

# ── Math markup fix ───────────────────────────────────────────────────────────
# Unicode superscript/subscript characters are not in WinAnsiEncoding (Core-14
# fonts), so they render as black squares.  Convert them to ReportLab's native
# <super> / <sub> XML tags which work with any font.
# ── superscript characters ────────────────────────────────────────────────
_SUPER = {
    'ⁿ': 'n', '⁰': '0', '¹': '1', '²': '2', '³': '3',
    '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
    '⁺': '+', '⁻': '-',                        # superscript plus / minus
}
# ── subscript characters ──────────────────────────────────────────────────
_SUB = {
    'ᵢ': 'i', 'ⱼ': 'j', 'ₖ': 'k', 'ₘ': 'm', 'ₙ': 'n',
    '₀': '0', '₁': '1', '₂': '2', '₃': '3',
    '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9',
    '₋': '-', '₌': '=',                        # subscript minus / equals
}
# ── characters not in Times-Roman glyph set → safe ASCII equivalents ─────
_REPLACE = {
    # Double-struck letters
    'ℝ': 'R',  'ℤ': 'Z',  'ℕ': 'N',  'ℂ': 'C',  'ℚ': 'Q',
    # Comparison operators not in WinAnsiEncoding
    '≫': '&gt;&gt;',  '≪': '&lt;&lt;',
    '≥': '&gt;=',     '≤': '&lt;=',
    '≠': '!=',        '≈': '~=',
    # Arrows
    '→': '-&gt;',     '←': '&lt;-',
    '⇒': '=&gt;',     '⟹': '=&gt;',
    # Set / math symbols
    '∈': 'in',        '∉': 'not in',
    '⊆': 'subset',    '⊂': 'subset',
    '∪': 'union',     '∩': 'intersect',
    '∞': 'inf.',       '√': 'sqrt',
    '∝': '~',
    # Letters with unusual diacritics (not in WinAnsiEncoding)
    'Ī': 'I',         'ī': 'i',      # I/i with macron
    'ő': 'o',         'Ő': 'O',      # o/O with double acute (Erdős)
    '\u0304': '',                     # combining macron — strip
    # Proof / checkbox symbols
    '□': '(QED)',      '☐': '[ ]',
}

def _fix_math(text):
    for ch, rep in _REPLACE.items():
        text = text.replace(ch, rep)
    for ch, rep in _SUPER.items():
        text = text.replace(ch, f'<super>{rep}</super>')
    for ch, rep in _SUB.items():
        text = text.replace(ch, f'<sub>{rep}</sub>')
    return text

from reportlab.platypus import CondPageBreak


class _SectionHead(Flowable):
    """A section heading that requests a page break if the remaining space on
    the current frame is less than MIN_SPACE points. Implemented by composition:
    we own a CondPageBreak and a Paragraph, and on the first wrap() call when
    the page is nearly full, we report ourselves as the size of the remaining
    frame — which is ReportLab's idiom for "I need a frame break." Once the
    break has happened (or wasn't needed), we delegate to the Paragraph's own
    wrap/draw, which is robust and never triggers Splitting errors.
    """
    MIN_SPACE = 1.6 * inch

    def __init__(self, text, style):
        super().__init__()
        self._para = Paragraph(text, style)
        self._broke = False
        self._w = 0
        self._h = 0

    def wrap(self, availW, availH):
        if not self._broke and availH < self.MIN_SPACE:
            # Take up all remaining space → Platypus moves us to next frame.
            self._broke = True
            return (availW, availH)
        # Either we've already broken once, or there is room → behave like the paragraph.
        self._w, self._h = self._para.wrap(availW, availH)
        return (self._w, self._h)

    def split(self, availW, availH):
        # Treat the heading as atomic — don't try to split it.
        return [self]

    def draw(self):
        if self._broke and self._h == 0:
            # The break-page placeholder draw — nothing to render, the frame break
            # is taken care of by the wrap geometry.
            return
        # Render the paragraph at our origin.
        self._para.canv = self.canv
        self._para.drawOn(self.canv, 0, 0)


def P(text, style):
    fixed = _fix_math(text)
    name = getattr(style, 'name', '')
    if name in ('section', 'subsection'):
        return _SectionHead(fixed, style)
    return Paragraph(fixed, style)


def SP(h):          return VSpace(h)
def HR():           return Rule()

def callout(text, S):
    """Modern left-accent bar callout — clean white with 4pt black left bar.
    Wrapped in KeepTogether so the callout never splits across a page boundary."""
    ACCENT = colors.HexColor('#1C1C1C')
    para = Paragraph(_fix_math(text), S['blockquote'])
    data = [[para]]
    t = Table(data, colWidths=[TW - 48])
    t.setStyle(TableStyle([
        ('LINEBEFORE',    (0,0), (-1,-1), 4,  ACCENT),
        ('LEFTPADDING',   (0,0), (-1,-1), 16),
        ('RIGHTPADDING',  (0,0), (-1,-1), 12),
        ('TOPPADDING',    (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('BACKGROUND',    (0,0), (-1,-1), colors.white),
    ]))
    return KeepTogether([t])

def math_img(latex_str, fontsize=13, w=5.0*inch, h=0.75*inch):
    """Render a LaTeX formula using matplotlib's built-in mathtext (no LaTeX install needed).
    Returns a ReportLab Image centred on white background, using Computer Modern font.
    Usage: story.append(math_img(r'P_{total}(n) = O(2^n)'))
    """
    import matplotlib.figure as mplfig
    fig = mplfig.Figure(figsize=(w / inch, h / inch), dpi=180)
    fig.patch.set_facecolor('white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    ax.text(0.5, 0.5, f'${latex_str}$',
            transform=ax.transAxes,
            fontsize=fontsize, ha='center', va='center',
            math_fontfamily='cm')   # Computer Modern — classic LaTeX look
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=180, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    buf.seek(0)
    return Image(buf, width=w, height=h)


def theorem_box(label, text, S, formula_img=None):
    """Two-row styled box: dark-charcoal header + light body with left accent.
    Wrapped in KeepTogether so the dark-charcoal header never appears at the
    bottom of one page with the body trailing onto the next (a split that
    looks broken to a reader).
    """
    DARK  = colors.HexColor('#1C1C1C')
    LIGHT = colors.HexColor('#F8F8F8')
    head  = Paragraph(_fix_math(label.upper()), S['theorem_head'])
    if formula_img is not None:
        if text:
            body_content = [formula_img,
                            Paragraph(_fix_math(text), S['theorem_b'])]
        else:
            body_content = formula_img
    else:
        body_content = Paragraph(_fix_math(f'<i>{text}</i>'), S['theorem_b'])
    data  = [[head], [body_content]]
    t = Table(data, colWidths=[TW - 36])
    t.setStyle(TableStyle([
        # outer border
        ('BOX',           (0,0), (-1,-1), 0.8,  colors.black),
        # header row
        ('BACKGROUND',    (0,0), (0,0),   DARK),
        ('TOPPADDING',    (0,0), (0,0),   7),
        ('BOTTOMPADDING', (0,0), (0,0),   7),
        ('LEFTPADDING',   (0,0), (0,0),   12),
        ('RIGHTPADDING',  (0,0), (0,0),   12),
        # divider
        ('LINEBELOW',     (0,0), (0,0),   0.5,  colors.HexColor('#444444')),
        # body row
        ('BACKGROUND',    (0,1), (0,1),   LIGHT),
        ('TOPPADDING',    (0,1), (0,1),   10),
        ('BOTTOMPADDING', (0,1), (0,1),   12),
        ('LEFTPADDING',   (0,1), (0,1),   14),
        ('RIGHTPADDING',  (0,1), (0,1),   14),
        # left accent bar across both rows
        ('LINEBEFORE',    (0,0), (-1,-1), 4,    DARK),
    ]))
    return KeepTogether([t])


def display_eq(latex_str, S, number=None, h=0.8*inch):
    """Centred display equation rendered via matplotlib mathtext (LaTeX notation).
    latex_str: raw LaTeX without $ delimiters, e.g. r'P_{total}(n) = O(2^n)'.
    Wrapped in KeepTogether so the equation, top rule, and bottom rule stay on
    the same page.
    """
    RULE_C = colors.HexColor('#AAAAAA')
    eq_img = math_img(latex_str, fontsize=13, w=TW - 80, h=h)
    if number:
        row = [[eq_img, Paragraph(f'({number})', S['epig_attr'])]]
        cw  = [TW - 72, 48]
    else:
        row = [[eq_img]]
        cw  = [TW - 48]
    t = Table(row, colWidths=cw)
    t.setStyle(TableStyle([
        ('LINEABOVE',     (0,0), (-1,0),  0.5, RULE_C),
        ('LINEBELOW',     (0,0), (-1,0),  0.5, RULE_C),
        ('TOPPADDING',    (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING',   (0,0), (-1,-1), 0),
        ('RIGHTPADDING',  (0,0), (-1,-1), 0),
        ('BACKGROUND',    (0,0), (-1,-1), colors.white),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
    ]))
    return KeepTogether([t])

def part_page(num, title, desc, S):
    return [
        PageBreak(),
        Mark(chapter=title, part=num),
        P(f'PART {num}', S['part_label']),
        P(title, S['part_title']),
        SP(18),
        HR(),
        SP(12),
        P(desc, S['part_desc']),
        PageBreak(),
    ]

def chapter_opener(num_str, title, subtitle, S):
    title_str = f'{num_str}: {title}'
    return [
        Mark(chapter=title_str),
        _RedrawChapterHeader(title_str),   # repaints the running head on this page
        P(num_str.upper(), S['chap_num']),
        P(title, S['chap_title']),
        P(subtitle, S['chap_sub']),
        HR(),
        SP(20),
    ]

def epigraph(quote, attribution, S):
    return [
        SP(6),
        P(f'"{quote}"', S['epigraph']),
        P(f'— {attribution}', S['epig_attr']),
    ]

# ─── TOC ──────────────────────────────────────────────────────────────────────
def build_toc(S, accessible=False):
    """Render the Table of Contents.

    Page numbers below are the printed page numbers (PDF page minus 2 for the
    cover + verso). They were extracted from the rendered PDF by
    _rebuild_toc.py — DO NOT edit them by hand; re-run that script after any
    structural change and copy its output here.

    The design uses three tiers:
      • Part dividers (uppercase, bold, with a subtle hairline below)
      • Chapter entries (book-weight body, right-flush page number with dot leader)
      • Subsection entries (slightly indented, lighter colour)
    """
    story = []
    story.append(P('Contents', S['toc_h']))

    toc = [
        ('part', 'FRONT MATTER',                                                  ''),
        ('chap', 'Preface — A Note on Origins',                                   '7'),

        ('part', 'INTRODUCTION',                                                  ''),
        ('chap', 'The Great Paradox',                                             '10'),
        ('sub',  'The Day Britain Created More Snakes',                           '10'),
        ('sub',  'What This Book Argues',                                         '11'),
        ('sub',  'The Central Claim, Stated Four Ways',                           '15'),

        ('part', 'PART I — THE THEORY',                                           '23'),
        ('chap', 'Chapter 1: The Law of Cascade Problems',                        '24'),
        ('sub',  'Three Mechanisms of the Cascade',                               '24'),
        ('sub',  'Murphy’s Law Is Not a Joke',                               '25'),
        ('sub',  'The Exponential Trap',                                          '26'),
        ('chap', 'Chapter 2: Why We Always Repeat the Mistake',                   '46'),
        ('sub',  'The Bias of Now',                                               '46'),
        ('sub',  'What Systems Thinking Offers',                                  '48'),
        ('sub',  'The Social Construction of Successful Solutions',               '61'),

        ('part', 'PART II — THE EVIDENCE',                                        '64'),
        ('chap', 'Chapter 3: Mathematics — The Original Cascade',                 '65'),
        ('sub',  'Hilbert’s Dream, Gödel’s Nightmare',              '65'),
        ('sub',  'Russell’s Paradox and Its Descendants',                    '66'),
        ('sub',  'The Halting Problem',                                           '67'),
        ('chap', 'Chapter 4: Physics — Nature’s Revenge',                    '83'),
        ('sub',  'Maxwell’s Demon',                                          '83'),
        ('sub',  'Quantum Mechanics and the Measurement Crisis',                  '85'),
        ('chap', 'Chapter 5: Computer Science — The Digital Cascade',             '109'),
        ('sub',  'Every Patch Opens a New Wound',                                 '109'),
        ('sub',  'Brooks’ Law and the Mythical Man-Month',                   '111'),
        ('sub',  'Feature Bloat and the Legacy Trap',                             '113'),
        ('sub',  'The Internet’s Unintended Children',                       '115'),
        ('chap', 'Chapter 6: Economics — The Market’s Irony',                '138'),
        ('sub',  'The Cobra Effect',                                              '138'),
        ('sub',  'Jevons Paradox: Efficiency Creates Demand',                     '140'),
        ('sub',  'Goodhart’s Law',                                           '142'),
        ('sub',  'The 2008 Financial Crisis',                                     '144'),
        ('chap', 'Chapter 7: Medicine — The Healing Paradox',                     '171'),
        ('sub',  'The Opioid Crisis',                                             '174'),
        ('sub',  'Thalidomide’s Double Life',                                '177'),
        ('sub',  'CRISPR and the Editing Problem',                                '178'),
        ('chap', 'Chapter 8: Politics — The Policy Boomerang',                    '199'),
        ('sub',  'Prohibition and the Birth of the Mob',                          '199'),
        ('sub',  'The War on Drugs',                                              '201'),
        ('sub',  'GDPR and the Compliance Industrial Complex',                    '209'),
        ('chap', 'Chapter 9: Society & Environment',                              '222'),
        ('sub',  'Social Media’s Loneliness Paradox',                        '222'),
        ('sub',  'Braess’s Paradox: When New Roads Make Traffic Worse',      '226'),
        ('sub',  'The Green Revolution’s Hidden Cost',                       '229'),

        ('part', 'PART III — THE CASCADE FRAMEWORK',                              '261'),
        ('chap',
         'Chapter 10: How the Cascade Works' if accessible
         else 'Chapter 10: A Formal Theory of Cascade Problems',
         '262'),
        ('sub',  'The Solution-Problem Network',                                  '262'),
        ('sub',  'How Problems Multiply',                                         '263'),
        ('sub',  'The Central Claim',                                             '263'),
        ('sub',  'The Tipping Point',                                             '267'),
        ('sub',  'The Shape of the Network Matters',                              '277'),
        ('chap', 'Chapter 11: Measuring and Predicting Cascades',                 '281'),
        ('sub',  'The Cascade Risk Index',                                        '281'),
        ('sub',  'Early Warning Signals',                                         '282'),
        ('sub',  'Limitations of the Cascade Risk Index',                         '290'),

        ('part', 'PART IV — THE WAY FORWARD',                                     '308'),
        ('chap', 'Chapter 12: Cascade-Aware Design',                              '309'),
        ('sub',  'The Hippocratic Principle for Innovation',                      '309'),
        ('sub',  'Pre-Mortem Analysis',                                           '310'),
        ('sub',  'The Role of Modularity and Reversibility',                      '311'),
        ('sub',  'Sunset Clauses and Reversibility Requirements',                 '316'),
        ('chap', 'Chapter 13: A New Philosophy of Innovation',                    '321'),
        ('sub',  'Second-Order Thinking',                                         '321'),
        ('sub',  'The Call to Action',                                            '322'),

        ('part', 'CONCLUSION & APPENDICES',                                       ''),
        ('chap', 'Conclusion: Living with the Paradox',                           '337'),
        ('chap',
         'Appendix A: Source Research' if accessible
         else 'Appendix A: Mathematical Proofs',
         '347'),
        ('chap', 'Appendix B: The Cascade Classification System',                 '349'),
        ('chap', 'Appendix C: Fifty Solution-Problem Pairs',                      '350'),
        ('chap', 'Appendix D: The Cascade Management Checklist',                  '352'),
        ('chap', 'Appendix E: Extended Case Studies in Cascade Management',       '355'),
        ('chap', 'Appendix F: A Glossary of Cascade Theory',                      '360'),
        ('chap', 'Appendix G: A Practical Cascade Assessment Checklist',          '366'),
        ('chap', 'Appendix H: The Intellectual Genealogy of Cascade Theory',      '370'),
        ('chap', 'Bibliography',                                                  '373'),
        ('chap', 'Index',                                                         '380'),
    ]

    # Render — three visual tiers with a clean right-flush dot leader.
    PAGE_COL = 56   # column at which page numbers start (in characters of TW)
    GREY = '#888888'

    def _line(text, page, max_len):
        """Compose a body line with a dot leader and the page number on the right."""
        if not page:
            return text
        # Use enough dots to fill the gap to the page column, avoid pathological short titles.
        gap = max(3, max_len - len(text))
        dots = '.' * gap
        return f'{text}<font color="{GREY}">{dots}{page}</font>'

    for kind, text, pg in toc:
        if kind == 'part':
            story.append(SP(8))
            if pg:
                story.append(P(_line(f'<b>{text}</b>', pg, PAGE_COL - 4),
                               S['toc_part']))
            else:
                story.append(P(f'<b>{text}</b>', S['toc_part']))
        elif kind == 'chap':
            story.append(P(_line(text, pg, PAGE_COL), S['toc_chap']))
        else:
            story.append(P(_line(text, pg, PAGE_COL - 4), S['toc_sub']))

    story.append(PageBreak())
    return story

# =============================================================================
# MAIN BOOK BUILDER
# =============================================================================
def build_book(accessible=False):
    S=make_styles()
    story=[]

    # ─── COVER ───────────────────────────────────────────────────────────────
    # The visible cover is drawn by on_first() directly on the canvas (the
    # designed cascade-tree + MORE/SOLUTIONS = MORE/PROBLEMS layout, ported
    # from book_cover.py). Here we just produce a placeholder page so that
    # on_first runs and the rest of the front matter starts on page 2.
    story += [
        Mark(chapter='', part=''),
        SP(1),
        PageBreak(),
    ]

    # ─── BLANK VERSO ─────────────────────────────────────────────────────────
    story += [SP(200), PageBreak()]

    # ─── COPYRIGHT ───────────────────────────────────────────────────────────
    story += [
        Mark(chapter='Copyright'),
        SP(300),
        P('Copyright © 2025 Ahmed Hafdi', S['note']),
        P('All rights reserved. No part of this publication may be reproduced without '
          'written permission of the author.', S['note']),
        P('<i>First Edition, 2025</i>', S['note']),
        PageBreak(),
    ]

    # ─── DEDICATION ──────────────────────────────────────────────────────────
    story += [
        SP(250),
        P('<i>To every engineer who ever said "this will fix it" —<br/>'
          'and to the problems that proved them wrong.</i>', S['epigraph']),
        PageBreak(),
    ]

    # ─── EPIGRAPHS ───────────────────────────────────────────────────────────
    story += [SP(160)]
    story += epigraph(
        'The curious task of economics is to demonstrate to men how little they '
        'really know about what they imagine they can design.',
        'Friedrich Hayek, <i>The Fatal Conceit</i>, 1988', S)
    story += [SP(28)]
    story += epigraph(
        'The first rule of any technology used in a business is that automation '
        'applied to an efficient operation will magnify the efficiency. The second '
        'is that automation applied to an inefficient operation will magnify the inefficiency.',
        'Bill Gates', S)
    story += [SP(28)]
    story += epigraph(
        'The unanticipated consequences of purposive social action are as '
        'pervasive and significant as the intended consequences.',
        'Robert K. Merton, <i>American Sociological Review</i>, 1936', S)
    story += [PageBreak()]

    # ─── TOC ─────────────────────────────────────────────────────────────────
    story += build_toc(S, accessible=accessible)

    # The Preface comes from the preface() function in the chapter modules;
    # the inline Preface and Note-on-Mathematics blocks that used to live here
    # have been removed because they duplicated the chapter-module preface and,
    # in the Reader's Edition, contradicted the no-math promise on the cover.
    return story, S

# save partial — will be extended in next module
if __name__ == '__main__':
    print("Part 1 loaded — run generate_book_FULL.py to build the complete PDF.")
