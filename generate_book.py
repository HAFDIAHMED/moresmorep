#!/usr/bin/env python3
"""
MORE SOLUTIONS = MORE PROBLEMS
A Theory of Cascade Innovation and the Hidden Cost of Progress
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
    """Zero-height marker that updates G['chapter']."""
    def __init__(self, chapter='', part=''):
        super().__init__(); self.chapter=chapter; self.part=part
        self.width=self.height=0
    def draw(self):
        if self.chapter: G['chapter']=self.chapter
        if self.part:    G['part']=self.part

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
                         firstLineIndent=0,keepWithNext=1)
    S['subsection']  = s('subsection',  fontName='Times-BoldItalic',fontSize=11,leading=16,
                         alignment=TA_LEFT,spaceBefore=12,spaceAfter=4,
                         firstLineIndent=0,keepWithNext=1)
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

def on_first(c, doc):
    pass   # cover page — clean

# ─── FIGURE FACTORY (xkcd sketch style) ───────────────────────────────────────
def fig_to_image(fig, w=5.0*inch, h=3.2*inch):
    buf=BytesIO(); fig.savefig(buf,format='png',dpi=160,bbox_inches='tight',
                               facecolor='white',edgecolor='none')
    buf.seek(0); plt.close(fig); return Image(buf,width=w,height=h)

def fig_exponential_cascade():
    with plt.xkcd():
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
        # Level 4 sprouts
        for x in [0.3,1.7,2.3,3.7,5.5,6.9,7.8,9.2]:
            ax.text(x,1.6,'?',ha='center',fontsize=10,color='gray')
            ax.plot([x,x+np.random.uniform(-0.2,0.2)],[1.9,2.6],'k-',alpha=0.3,lw=0.8)
        ax.text(5,0.6,'Each fix spawns more problems...',ha='center',
                fontsize=9,fontstyle='italic',color='gray')
        ax.set_title('The Cascade Tree: One Fix, Infinite Branches', fontsize=11, fontweight='bold')
        fig.tight_layout()
    return fig

def fig_antibiotic_resistance():
    with plt.xkcd():
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
    with plt.xkcd():
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
    with plt.xkcd():
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
    with plt.xkcd():
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
    with plt.xkcd():
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
    with plt.xkcd():
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
    with plt.xkcd():
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
    with plt.xkcd():
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
    with plt.xkcd():
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
    with plt.xkcd():
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

def P(text, style): return Paragraph(_fix_math(text), style)
def SP(h):          return VSpace(h)
def HR():           return Rule()

def callout(text, S):
    """Modern left-accent bar callout — clean white with 4pt black left bar."""
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
    return t

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
    """2-row styled box: dark charcoal header + light body with left accent.
    Pass formula_img=math_img(...) to embed a LaTeX-rendered equation in the body.
    If both formula_img and text are given, the image appears above the text.
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
    return t


def display_eq(latex_str, S, number=None, h=0.8*inch):
    """Centred display equation rendered via matplotlib mathtext (LaTeX notation).
    latex_str: raw LaTeX without $ delimiters, e.g. r'P_{total}(n) = O(2^n)'
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
    return t

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
    return [
        Mark(chapter=f'{num_str}: {title}'),
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
def build_toc(S):
    story=[]
    story.append(P('Contents', S['toc_h']))
    toc=[
        ('part','— FRONT MATTER —',''),
        ('chap','Preface','7'),
        ('chap','A Note on Mathematics','9'),
        ('part','INTRODUCTION',''),
        ('chap','The Great Paradox','13'),
        ('sub','The Day Britain Created More Snakes','13'),
        ('sub','What This Book Argues','14'),
        ('sub','The Central Claim, Stated Four Ways','18'),
        ('part','PART I — THE THEORY',''),
        ('chap','Chapter 1: The Law of Cascade Problems','26'),
        ('sub','Three Mechanisms of the Cascade','26'),
        ('sub','Murphy\'s Law Is Not a Joke','27'),
        ('sub','The Exponential Trap','28'),
        ('chap','Chapter 2: Why We Always Repeat the Mistake','50'),
        ('sub','The Bias of Now','52'),
        ('sub','What Systems Thinking Offers','55'),
        ('sub','The Social Construction of Successful Solutions','67'),
        ('part','PART II — THE EVIDENCE',''),
        ('chap','Chapter 3: Mathematics — The Original Cascade','72'),
        ('sub','Hilbert\'s Dream, Gödel\'s Nightmare','73'),
        ('sub','Russell\'s Paradox and Its Descendants','73'),
        ('sub','The Halting Problem','74'),
        ('chap','Chapter 4: Physics — Nature\'s Revenge','91'),
        ('sub','Maxwell\'s Demon','91'),
        ('sub','Quantum Mechanics and the Measurement Crisis','93'),
        ('sub','Nuclear Power\'s 90,000-Year Problem','97'),
        ('sub','String Theory\'s Landscape of Despair','100'),
        ('chap','Chapter 5: Computer Science — The Digital Cascade','117'),
        ('sub','Every Patch Opens a New Wound','117'),
        ('sub','Brooks\' Law and the Mythical Man-Month','119'),
        ('sub','Feature Bloat and the Legacy Trap','121'),
        ('sub','The Internet\'s Unintended Children','123'),
        ('chap','Chapter 6: Economics — The Market\'s Irony','148'),
        ('sub','The Cobra Effect','148'),
        ('sub','Jevons Paradox: Efficiency Creates Demand','150'),
        ('sub','Goodhart\'s Law','152'),
        ('sub','The 2008 Financial Crisis','155'),
        ('chap','Chapter 7: Medicine — The Healing Paradox','183'),
        ('sub','Antibiotic Resistance: The Brewing Pandemic','185'),
        ('sub','The Opioid Crisis','186'),
        ('sub','Thalidomide\'s Double Life','189'),
        ('sub','CRISPR and the Editing Problem','191'),
        ('chap','Chapter 8: Politics — The Policy Boomerang','212'),
        ('sub','Prohibition and the Birth of the Mob','212'),
        ('sub','The War on Drugs','214'),
        ('sub','GDPR and the Compliance Industrial Complex','254'),
        ('sub','Urban Zoning\'s Housing Catastrophe','221'),
        ('chap','Chapter 9: Society & Environment','238'),
        ('sub','Social Media\'s Loneliness Paradox','238'),
        ('sub','Jevons Meets GPS: Braess\'s Paradox','242'),
        ('sub','The Green Revolution\'s Hidden Cost','245'),
        ('part','PART III — THE FRAMEWORK',''),
        ('chap','Chapter 10: A Formal Theory of Cascade Problems','279'),
        ('sub','The Solution-Problem Network','279'),
        ('sub','Cascade Propagation Functions','280'),
        ('sub','The Main Theorem: O(2ⁿ) Growth','281'),
        ('chap','Chapter 11: Measuring and Predicting Cascades','306'),
        ('sub','The Cascade Risk Index','306'),
        ('sub','Early Warning Signals','307'),
        ('part','PART IV — THE WAY FORWARD',''),
        ('chap','Chapter 12: Cascade-Aware Design','335'),
        ('sub','The Hippocratic Principle for Innovation','335'),
        ('sub','Pre-Mortem Analysis','327'),
        ('chap','Chapter 13: A New Philosophy of Innovation','347'),
        ('sub','Second-Order Thinking','347'),
        ('sub','The Call to Action','349'),
        ('part','CONCLUSION & APPENDICES',''),
        ('chap','Conclusion: Living with the Paradox','363'),
        ('chap','Appendix A: Mathematical Proofs','377'),
        ('chap','Appendix B: Cascade Classification','383'),
        ('chap','Appendix C: 50 Solution-Problem Pairs','384'),
        ('chap','Bibliography','386'),
    ]
    for kind,text,pg in toc:
        if kind=='part':
            story.append(SP(6))
            story.append(P(f'<b>{text}</b>', S['toc_part']))
        elif kind=='chap':
            line=f'{text}'
            if pg: line+=f'<font color="#888888">{"."*(55-len(text))}{pg}</font>'
            story.append(P(line, S['toc_chap']))
        else:
            line=f'{text}'
            if pg: line+=f'<font color="#888888">{"."*(52-len(text))}{pg}</font>'
            story.append(P(line, S['toc_sub']))
    story.append(PageBreak())
    return story

# =============================================================================
# MAIN BOOK BUILDER
# =============================================================================
def build_book():
    S=make_styles()
    story=[]

    # ─── COVER ───────────────────────────────────────────────────────────────
    story += [
        Mark(chapter='', part=''),
        SP(100),
        P('More Solutions = More Problems', S['cover_title']),
        P('A Theory of Cascade Innovation and the Hidden Cost of Progress', S['cover_sub']),
        HR(),
        SP(48),
        P('Ahmed Hafdi', S['cover_auth']),
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
    story += build_toc(S)

    # ─── PREFACE ─────────────────────────────────────────────────────────────
    story += [
        Mark(chapter='Preface'),
        P('Preface', S['preface_t']),
        SP(12),
    ]
    story += epigraph('This is a book about a trap. Most of us are already inside it.',
                      'Ahmed Hafdi', S)
    story += [SP(12)]
    preface_paras = [
        """I started writing this book on an ordinary Tuesday morning, sitting in a café in
        Casablanca, reading a newspaper story about a new government initiative that would
        "solve" the country's traffic congestion problem by widening a major highway. I had
        read enough urban planning literature to know what would happen next: within three
        years, the wider road would attract more traffic, congestion would return worse than
        before, and some new official would propose widening it further. This is not a
        Moroccan problem. It is not even a traffic problem. It is a fundamental feature of
        how complex systems respond to intervention.""",

        """The phenomenon has a name in transportation science (induced demand) but it is
        far older and far broader than any single domain. Every field I have studied, from
        pure mathematics to molecular biology, from monetary policy to social media design,
        exhibits the same structural pattern: a well-intentioned solution enters a complex
        system, and the system responds by generating new problems, often more numerous and
        more difficult than the original. The solution is real. The improvement is real. But
        it is temporary, and it comes at a hidden cost that compounds with each subsequent fix.""",

        """I am a researcher by training, a mathematician by inclination, and an obsessive
        reader of history. What struck me, as I began accumulating examples for what I thought
        would be a short essay, was not just the frequency of this pattern but its mathematical
        character. This was not mere pessimism or anti-progress sentiment. There was a precise
        structural reason, grounded in network theory and combinatorics, why introducing
        solutions into interconnected systems produces more problems than it resolves. The
        mathematics is not complicated, but its implications are profound.""",

        """This book is the result of three years of research across seven disciplines. It is
        intended for the curious general reader, the policymaker who wants to understand why
        well-designed programs so often backfire, the engineer who is proud of her latest
        optimization, and the scientist who believes that the next breakthrough will finally
        settle the question. I respect all of these people. But I want to show them something
        they may not have noticed: that the map of human knowledge is covered not in answers,
        but in an expanding frontier of new and better questions, generated precisely by the
        best minds working on the hardest problems.""",

        """The book is organized in four parts. Part I establishes the theoretical foundation:
        what the cascade problem is, why it is mathematically inevitable, and why human
        psychology is uniquely unsuited to perceiving it in real time. Part II surveys the
        evidence across seven domains: mathematics, physics, computer science, economics,
        medicine, politics, and social systems — building a cumulative case that transcends any
        single field. Part III presents the formal mathematical framework for quantifying and
        predicting cascade effects. Part IV asks: what can we do about it?""",

        """The answer to that last question is not despair. It is a more humble, more
        systemic, and ultimately more effective relationship with complexity. We can design
        solutions that are cascade-aware. We can create institutions that treat second-order
        effects as first-class concerns. We can cultivate a culture of intellectual humility
        that celebrates the question as much as the answer. These are not utopian aspirations.
        They are, as the evidence in this book shows, the distinguishing feature of the rare
        solutions that actually endure.""",

        """A word about the mathematics: I have tried to write every equation in this book
        so that a reader who has not studied mathematics since secondary school can follow the
        argument. Wherever a formula appears, it is immediately translated into plain language.
        The reader who wants the full technical derivations will find them in Appendix A. The
        reader who prefers to skip the equations entirely will still find a complete and
        self-contained argument in the prose.""",

        """I am grateful to the researchers, historians, physicians, economists, and engineers
        whose work I have drawn upon. All errors of interpretation are mine. I am especially
        grateful to the problems. Without them, this book would not exist, which is, in a way,
        the whole point.""",
    ]
    for i,p in enumerate(preface_paras):
        story.append(P(' '.join(p.split()), S['body'] if i>0 else S['body0']))
    story += [
        SP(20),
        P('<i>Ahmed Hafdi<br/>Casablanca, 2025</i>', S['epig_attr']),
        PageBreak(),
    ]

    # ─── NOTE ON MATHEMATICS ─────────────────────────────────────────────────
    story += [
        Mark(chapter='A Note on Mathematics'),
        P('A Note on Mathematics', S['preface_t']),
        SP(12),
        P('This book contains mathematics. Do not be alarmed.', S['body0']),
        P("""Every mathematical expression in these pages is a compressed version of an idea
        that can be stated in words. When you see the notation O(2ⁿ), which means "grows
        exponentially with n"; what it is really saying is: "double the number of solutions
        and the number of potential problems quadruples; triple it and they multiply by eight;
        each addition is worse than the last." When you see O(log n), it means the opposite:
        "each additional solution adds only a tiny increment of new problems." The difference
        between these two curves is the difference between sustainable progress and the kind
        that eventually consumes itself. """, S['body']),
        P("""The formal theorems in Chapters 10 and 11 can be read with full technical
        rigour or skipped to the conclusions. The case studies in Part II require no
        mathematical background at all, only an open mind and a willingness to accept that
        the world is more connected than our problem-solving instincts assume. """, S['body']),
        P("""Readers who want a complete grounding in the mathematical theory will find
        detailed proofs in Appendix A. Those proofs use nothing beyond calculus and introductory
        graph theory. The core arguments of Parts I through IV, however, stand entirely
        on their own, built from history, evidence, and the kind of logical reasoning that
        any careful thinker can follow. The mathematics is offered as confirmation, not
        prerequisite. """, S['body']),
        P("""A note on the key parameters. The network amplification exponent α, which
        appears throughout the formal framework, is not an abstract mathematical convention
        invented for the convenience of the theory. It is an empirically estimated quantity.
        Albert-László Barabási and Réka Albert's seminal 1999 <i>Science</i> paper
        demonstrated that real-world networks: citation networks, the internet, protein
        interaction networks: exhibit degree distributions following power laws, with
        characteristic exponents measured from real data. The exponent α used in this book
        is calibrated against measured cascade propagation data from three domains: software
        vulnerability cascades (α ≈ 1.4–1.5, from National Vulnerability Database dependency
        analysis); financial contagion (α ≈ 1.6–1.8, from Gai and Kapadia's 2010 Bank of
        England analysis of interbank networks); and information cascades in social media
        (α ≈ 1.7–2.1, from Vosoughi, Roy and Aral's 2018 <i>Science</i> study of Twitter
        rumour propagation). The cascade coefficient C(s) for specific solution categories
        is estimated from historical reference class data, for pharmaceutical drugs from
        FDA adverse event reporting, for software patches from the NVD, for financial
        instruments from Basel stress-test data. The parameters are uncertain, as all
        empirical quantities are. They are not arbitrary. """, S['body']),
        PageBreak(),
    ]

    return story, S

# save partial — will be extended in next module
if __name__ == '__main__':
    print("Part 1 loaded — run generate_book_FULL.py to build the complete PDF.")
