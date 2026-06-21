"""Generate `book_trailer.pdf` — a short marketing PDF you can attach to
emails to agencies, journalists, podcasters. Shows enough to sell the book
without giving away the whole manuscript. ~6 pages.

Run: python book_trailer.py
Output: ./book_trailer.pdf
"""
import os
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                Table, TableStyle, HRFlowable)

# ── output path ─────────────────────────────────────────────────────────────
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'book_trailer.pdf')

# ── A4 page constants ───────────────────────────────────────────────────────
PW, PH = A4
ML = MR = 0.85 * inch
MT = MB = 0.85 * inch
TW = PW - ML - MR

# ── palette ─────────────────────────────────────────────────────────────────
INK       = HexColor('#0A0A0A')
INK_MED   = HexColor('#2A2A2A')
INK_BODY  = HexColor('#3A3A3A')
INK_LIGHT = HexColor('#666666')
INK_XLIT  = HexColor('#999999')
ACCENT    = HexColor('#1C1C1C')
CREAM     = HexColor('#F3F2EE')


# ── styles ──────────────────────────────────────────────────────────────────
def make_styles():
    S = {}
    S['body']     = ParagraphStyle('body', fontName='Times-Roman', fontSize=11,
                                   leading=17, alignment=TA_JUSTIFY,
                                   textColor=INK_BODY, spaceAfter=8)
    S['body0']    = ParagraphStyle('body0', parent=S['body'], spaceBefore=4)
    S['lead']     = ParagraphStyle('lead', fontName='Times-Italic', fontSize=13,
                                   leading=20, alignment=TA_LEFT,
                                   textColor=INK_MED, spaceAfter=10)
    S['h1']       = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=24,
                                   leading=30, alignment=TA_LEFT,
                                   textColor=INK, spaceBefore=4, spaceAfter=8)
    S['h2']       = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=13,
                                   leading=18, alignment=TA_LEFT,
                                   textColor=INK, spaceBefore=12, spaceAfter=6)
    S['caption']  = ParagraphStyle('caption', fontName='Helvetica', fontSize=8,
                                   leading=11, alignment=TA_LEFT,
                                   textColor=INK_LIGHT)
    S['cover_t']  = ParagraphStyle('cover_t', fontName='Helvetica-Bold',
                                   fontSize=42, leading=46, alignment=TA_CENTER,
                                   textColor=INK, spaceAfter=8)
    S['cover_s']  = ParagraphStyle('cover_s', fontName='Times-Italic',
                                   fontSize=14, leading=20, alignment=TA_CENTER,
                                   textColor=INK_MED, spaceAfter=24)
    S['cover_a']  = ParagraphStyle('cover_a', fontName='Helvetica-Bold',
                                   fontSize=12, leading=16, alignment=TA_CENTER,
                                   textColor=INK, spaceAfter=2)
    S['cover_l']  = ParagraphStyle('cover_l', fontName='Helvetica', fontSize=9,
                                   leading=12, alignment=TA_CENTER,
                                   textColor=INK_LIGHT)
    S['blockquote'] = ParagraphStyle('blockquote', fontName='Times-Roman',
                                     fontSize=11.5, leading=18, alignment=TA_JUSTIFY,
                                     textColor=INK_BODY, leftIndent=16,
                                     rightIndent=16, spaceBefore=8, spaceAfter=8)
    return S


# ── flowable helpers ────────────────────────────────────────────────────────
def callout(text, S):
    """White card with a thin black left bar — like the in-book callouts."""
    para = Paragraph(text, S['blockquote'])
    t = Table([[para]], colWidths=[TW - 24])
    t.setStyle(TableStyle([
        ('LINEBEFORE',    (0,0), (-1,-1), 3, ACCENT),
        ('LEFTPADDING',   (0,0), (-1,-1), 14),
        ('RIGHTPADDING',  (0,0), (-1,-1), 14),
        ('TOPPADDING',    (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('BACKGROUND',    (0,0), (-1,-1), CREAM),
    ]))
    return t


def rule(thick=0.7, space=8):
    return HRFlowable(width='100%', thickness=thick, color=INK,
                      spaceBefore=space, spaceAfter=space)


# ── cover page (drawn directly on the canvas) ───────────────────────────────
def draw_cover(c, doc):
    """Mini-cover for the trailer's first page."""
    W, H = A4
    c.setFillColor(HexColor('#FFFFFF'))
    c.rect(0, 0, W, H, fill=1, stroke=0)
    # top black bar
    c.setFillColor(INK)
    c.rect(0, H - 0.04*inch, W, 0.04*inch, fill=1, stroke=0)
    # tagline
    c.setFont('Helvetica', 9)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(W/2, H - 0.6*inch, 'MARKETING TRAILER · GALLEY PREVIEW')
    # main title
    c.setFont('Helvetica-Bold', 56)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(W/2, H * 0.72, 'MORE')
    c.setFont('Helvetica-Bold', 64)
    c.setFillColor(INK)
    c.drawCentredString(W/2, H * 0.64, 'SOLUTIONS')
    c.setFont('Helvetica-Bold', 36)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(W/2, H * 0.58, '=')
    c.setFont('Helvetica-Bold', 56)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(W/2, H * 0.51, 'MORE')
    c.setFont('Helvetica-Bold', 64)
    c.setFillColor(INK)
    c.drawCentredString(W/2, H * 0.43, 'PROBLEMS')
    # subtitle
    c.setStrokeColor(INK_XLIT)
    c.setLineWidth(0.5)
    c.line(W * 0.28, H * 0.36, W * 0.72, H * 0.36)
    c.setFont('Times-Italic', 12)
    c.setFillColor(INK_LIGHT)
    c.drawCentredString(W/2, H * 0.335, 'Why Every Solution')
    c.drawCentredString(W/2, H * 0.315, 'Creates the Next Problem')
    # author bar
    c.setFillColor(INK)
    c.rect(0, 0, W, 0.7*inch, fill=1, stroke=0)
    c.setFont('Helvetica-Bold', 16)
    c.setFillColor(HexColor('#FFFFFF'))
    c.drawCentredString(W/2, 0.36*inch, 'AHMED HAFDI')
    c.setFont('Helvetica', 8.5)
    c.setFillColor(HexColor('#AAAAAA'))
    c.drawCentredString(W/2, 0.18*inch, 'Trade non-fiction · 249 pages · A4 · Reader\'s Edition 2025')


# ── content builder ─────────────────────────────────────────────────────────
def build_story(S):
    story = []

    # PAGE 1 = cover (handled by onFirstPage callback)
    story.append(PageBreak())

    # ── PAGE 2 — the hook / one-page pitch ──────────────────────────────────
    story.append(Paragraph('The Book in One Page', S['h1']))
    story.append(rule(thick=1.0, space=4))

    story.append(Paragraph(
        'Every solution, once released into a connected system, creates problems '
        'faster than the system can absorb them — and the more connected the system, '
        'the wider the gap. That is the argument, the whole argument, and nothing '
        'else this book says will contradict it.', S['lead']))

    story.append(Paragraph(
        'You have felt this before. The new feature that broke three other things. '
        'The regulation that bred the loophole industry. The medication that needed '
        'a second medication to manage its side effects. The road that was meant to '
        'relieve traffic and made it worse. The fix that became the next thing your '
        'team had to fix. The sense that the harder we work, the further behind we '
        'fall — that is not a feeling. It is arithmetic. <i>More Solutions = More '
        'Problems</i> spends 16 chapters making that arithmetic visible.',
        S['body']))

    story.append(Paragraph(
        'The book traces the same cascade pattern through seven domains of evidence '
        '— mathematics, physics, computer science, economics, medicine, politics, '
        'and society — then turns the pattern into a practical scoring tool, '
        '<b>the Cobra Score</b>, that estimates how dangerous a new solution\'s '
        'cascade is likely to be <i>before</i> it ships. The final chapter applies '
        'the framework to the technology readers are living through right now: '
        'large-scale AI.', S['body']))

    story.append(rule(thick=0.4, space=10))

    story.append(Paragraph('At a glance', S['h2']))
    facts = [
        ['Title',     '<i>More Solutions = More Problems</i>'],
        ['Subtitle',  'Why Every Solution Creates the Next Problem'],
        ['Author',    'Ahmed Hafdi (Kenitra, Morocco)'],
        ['Length',    '249 pages · A4 · 16 chapters across 4 parts'],
        ['Audience',  'General readers of Taleb, Harari, Kahneman, Tenner, Newport'],
        ['Hook',      'The Cobra Score · A 0–1 risk index for cascade-prone solutions'],
        ['Live angle','Chapter 16 applies the framework to AI in 2026'],
        ['Status',    'Print-ready (galley available on request)'],
    ]
    fact_rows = [[Paragraph(f'<b>{k}</b>', S['caption']),
                  Paragraph(v, S['caption'])] for k, v in facts]
    ft = Table(fact_rows, colWidths=[1.3*inch, TW - 1.3*inch])
    ft.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(ft)
    story.append(PageBreak())

    # ── PAGE 3 — sample excerpt ─────────────────────────────────────────────
    story.append(Paragraph('Excerpt — From the Introduction', S['h1']))
    story.append(rule(thick=1.0, space=4))
    story.append(Spacer(1, 6))
    story.append(Paragraph('The Day Britain Created More Snakes', S['h2']))

    story.append(Paragraph(
        'Delhi, the 1880s. The British administration has a problem: too many '
        'cobras. People are dying. So the colonial government does what any '
        'rational government would do — it offers a bounty. A rupee for every '
        'dead snake. The logic is impeccable. Citizens hunt the cobras, the '
        'population falls, the city becomes safer.', S['body0']))

    story.append(Paragraph('That is not what happens.', S['body']))

    story.append(Paragraph(
        'Within months, the people of Delhi discover something the administrators '
        'have not anticipated. It is much easier to <i>breed</i> cobras than to '
        'hunt them. Cobra farms appear across the city. Dead snakes arrive at the '
        'colonial offices by the basketful. The bounty payments flow. The '
        'administrators, watching their numbers climb, congratulate themselves on '
        'the program\'s success.', S['body']))

    story.append(Paragraph(
        'When the government finally realises what is happening and cancels the '
        'bounty, the farmers are left with thousands of suddenly worthless snakes. '
        'They do the rational thing. They release them. Delhi ends up with more '
        'cobras than when it started.', S['body']))

    story.append(Paragraph(
        'This is the Cobra Effect. It is not a story about stupidity. The '
        'administrators were not fools; they were applying standard incentive '
        'theory, which was and remains perfectly sound. The failure was not in the '
        'people. It was in the architecture of the solution.', S['body']))

    story.append(Spacer(1, 6))
    story.append(callout(
        'Every cascade in this book began as a solution that was working '
        'exactly as designed. The cascade was the system\'s response to its '
        'working. The cascade is not in the people. It is in the architecture.',
        S))
    story.append(PageBreak())

    # ── PAGE 4 — chapter list ───────────────────────────────────────────────
    story.append(Paragraph('Chapter List', S['h1']))
    story.append(rule(thick=1.0, space=4))
    story.append(Paragraph(
        'Sixteen chapters across four parts. Each chapter is structured the same '
        'way: a celebrated solution, the cascade it generated, and what cascade-'
        'aware design would have looked like.', S['body0']))

    chapters = [
        ('Front matter',     'Preface · Read This First · Introduction: The Great Paradox'),
        ('Part I — The Theory',
            'Ch1: The Logic of Cascade Problems\n'
            'Ch2: Why We Always Repeat the Mistake'),
        ('Part II — The Evidence',
            'Ch3: Mathematics — The Original Cascade\n'
            'Ch4: Physics — Nature\'s Revenge\n'
            'Ch5: Computer Science — The Digital Cascade\n'
            'Ch6: Economics — The Market\'s Irony (Cobra Effect, Goodhart\'s Law, 2008)\n'
            'Ch7: Medicine — The Healing Paradox (Antibiotic resistance, OxyContin, CRISPR)\n'
            'Ch8: Politics — The Policy Boomerang (Prohibition, War on Drugs, GDPR)\n'
            'Ch9: Society & Environment (Social media, GPS/Braess, the Green Revolution)'),
        ('Part III — The Framework',
            'Ch10: How the Cascade Works\n'
            'Ch11: Measuring and Predicting Cascades — the Cobra Score'),
        ('Part IV — The Way Forward',
            'Ch12: Cascade-Aware Design\n'
            'Ch13: A New Philosophy of Innovation\n'
            'Ch14: The Case Against This Book\n'
            'Ch15: How to Spot a Cascade Before It Hits You\n'
            'Ch16: The AI Cascade'),
        ('End matter',      'Conclusion · 7 Appendices · Bibliography · Index'),
    ]
    for label, content in chapters:
        story.append(Paragraph(label, S['h2']))
        for line in content.split('\n'):
            story.append(Paragraph(line, S['body']))
    story.append(PageBreak())

    # ── PAGE 5 — author bio + contact ───────────────────────────────────────
    story.append(Paragraph('About the Author', S['h1']))
    story.append(rule(thick=1.0, space=4))
    story.append(Paragraph(
        '<b>AHMED HAFDI</b> is a software engineer and researcher based in '
        'Kenitra, Morocco. <i>More Solutions = More Problems</i> is his first '
        'book — the trade edition of a research framework on cascade innovation '
        'that he developed in the underlying paper, <i>"From Cascade Chaos to '
        'Ecosystem Harmony: A Complete Mathematical Framework for Understanding '
        'and Solving the Solution-Problem Paradox"</i>, available on ResearchGate. '
        'The book translates that framework into accessible prose, working '
        'examples, and a single practical tool readers can apply — the '
        'Cobra Score.', S['body']))

    story.append(Paragraph(
        'The book\'s argument grew out of two conversations the author had with '
        'colleagues — one with his manager Mariam Roussafi during a bug-hunt in '
        'a large software system, and one with Badreddine Otky, a chief '
        'technology officer with over twenty years of experience. Both moments '
        'observed independently that solutions in connected systems tend to '
        'ripple through the rest of the system in ways their designers did not '
        'anticipate. The book begins where those conversations ended.', S['body']))

    story.append(rule(thick=0.4, space=12))

    story.append(Paragraph('Press &amp; partnership contact', S['h2']))
    contact_lines = [
        '<b>AHMED HAFDI</b>',
        'Author, <i>More Solutions = More Problems</i>',
        'Kenitra, Morocco',
        'Email: ahmedhafdi@buildwellai.com',
        'Research paper: researchgate.net/publication/395720779',
    ]
    for line in contact_lines:
        story.append(Paragraph(line, S['body']))

    story.append(Spacer(1, 24))
    story.append(callout(
        '<b>For agents, publicists, journalists, and podcasters:</b> a full '
        'galley copy of the manuscript is available on request. Please reply '
        'to the email above stating the purpose of the request (review, '
        'interview, excerpt enquiry, or marketing proposal) and Ahmed will '
        'send the PDF directly.', S))

    return story


def main():
    print(f'Generating book trailer -> {OUT}')
    S = make_styles()

    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=ML, rightMargin=MR, topMargin=MT, bottomMargin=MB,
        title='More Solutions = More Problems — Marketing Trailer',
        author='Ahmed Hafdi',
        subject='Book galley preview · 5-page marketing trailer',
    )
    story = build_story(S)
    doc.build(story, onFirstPage=draw_cover)
    print(f'  Saved -> {OUT}')
    print(f'  Pages: 5 (cover + hook + excerpt + chapter list + author/contact)')


if __name__ == '__main__':
    main()
