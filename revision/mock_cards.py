#!/usr/bin/env python3
"""Render 4 design variants of a 'principle card' to PNGs for comparison."""
import os, textwrap
from io import BytesIO
import fitz
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = os.path.join(os.path.dirname(__file__), '_mock')
os.makedirs(OUT, exist_ok=True)
TW = 6.0 * inch
CH = colors.HexColor('#1C1C1C')
LABEL = 'SECOND PRINCIPLE OF CASCADE INNOVATION'
TEXT = ("The rate at which a solution ecosystem generates problems eventually outruns the rate "
        "at which solutions can be deployed. No matter how fast new solutions arrive — whether "
        "the rate grows linearly, quadratically, or at any ordinary pace — the rate of new "
        "problems will, sooner or later, exceed it.")

def render(flows, name, pad=12):
    buf = BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=(TW + 2 * pad * 1.0 + 60, 230),
                            leftMargin=30, rightMargin=30, topMargin=18, bottomMargin=18)
    doc.build(flows)
    d = fitz.open('pdf', buf.getvalue())
    d[0].get_pixmap(dpi=140).save(os.path.join(OUT, name))

# V0 — CURRENT: dark header + light body
def v0():
    head = Paragraph(LABEL, ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=8.5,
                     textColor=colors.white, leading=13))
    body = Paragraph('<i>%s</i>' % TEXT, ParagraphStyle('b', fontName='Times-Italic',
                     fontSize=11, leading=16))
    t = Table([[head], [body]], colWidths=[TW - 36])
    t.setStyle(TableStyle([('BOX', (0,0),(-1,-1),0.8,colors.black),
        ('BACKGROUND',(0,0),(0,0),CH),('TOPPADDING',(0,0),(0,0),7),('BOTTOMPADDING',(0,0),(0,0),7),
        ('LEFTPADDING',(0,0),(0,0),12),('RIGHTPADDING',(0,0),(0,0),12),
        ('LINEBELOW',(0,0),(0,0),0.5,colors.HexColor('#444444')),
        ('BACKGROUND',(0,1),(0,1),colors.HexColor('#F8F8F8')),('TOPPADDING',(0,1),(0,1),10),
        ('BOTTOMPADDING',(0,1),(0,1),12),('LEFTPADDING',(0,1),(0,1),14),('RIGHTPADDING',(0,1),(0,1),14)]))
    render([t], 'v0_current.png')

# V1 — EDITORIAL: rules, small-caps label, larger italic, NO box
def v1():
    lab = Paragraph('S E C O N D &#160; P R I N C I P L E', ParagraphStyle('l',
        fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.HexColor('#777777'), leading=11))
    stmt = Paragraph(TEXT, ParagraphStyle('s', fontName='Times-Italic', fontSize=13, leading=18.5,
        textColor=colors.HexColor('#1a1a1a'), leftIndent=6, rightIndent=6))
    render([HRFlowable(width='100%', thickness=1.0, color=CH, spaceAfter=7),
            lab, Spacer(1, 7), stmt, Spacer(1, 8),
            HRFlowable(width='100%', thickness=0.4, color=colors.HexColor('#999999'))], 'v1_editorial.png')

# V2 — SOFT PANEL: tinted background + thick left accent bar + serif label
def v2():
    lab = Paragraph(LABEL, ParagraphStyle('l', fontName='Helvetica-Bold', fontSize=8,
        textColor=CH, leading=12, spaceAfter=6))
    body = Paragraph('<i>%s</i>' % TEXT, ParagraphStyle('b', fontName='Times-Italic', fontSize=11.5,
        leading=16.5, textColor=colors.HexColor('#222222')))
    t = Table([[lab], [body]], colWidths=[TW - 30])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#F3F2EE')),
        ('LINEBEFORE',(0,0),(-1,-1),3.5,CH),
        ('LEFTPADDING',(0,0),(-1,-1),16),('RIGHTPADDING',(0,0),(-1,-1),16),
        ('TOPPADDING',(0,0),(0,0),11),('BOTTOMPADDING',(0,-1),(-1,-1),12),
        ('TOPPADDING',(0,1),(0,1),0)]))
    render([t], 'v2_panel.png')

# V3 — SKETCH: hand-drawn box (xkcd) to show the look the reader asked about
def v3():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.6, 2.3)); ax.axis('off')
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        ax.add_patch(FancyBboxPatch((0.015, 0.04), 0.97, 0.92, boxstyle='round,pad=0.015',
                     fill=False, edgecolor='black', lw=2))
        ax.text(0.05, 0.86, LABEL, fontsize=10, fontweight='bold', va='top')
        ax.text(0.05, 0.66, textwrap.fill(TEXT, 74), fontsize=9, style='italic', va='top')
        fig.savefig(os.path.join(OUT, 'v3_sketch.png'), dpi=140, bbox_inches='tight',
                    facecolor='white'); plt.close(fig)

v0(); v1(); v2(); v3()
print('wrote', os.listdir(OUT))
