"""Scan the latest Reader's Edition PDF in versions/ and emit a fresh `toc=[...]`
list ready to paste into generate_book.py:build_toc(). Uses strict structural
anchors (uppercase 'CHAPTER ONE', 'APPENDIX A', etc.) chained so each search
starts AFTER the previous anchor — this avoids matching TOC entries.
"""
import io, os, re, glob, sys
from pypdf import PdfReader

DIR = os.path.dirname(__file__) or '.'
versions_dir = os.path.join(DIR, 'versions')
pdfs = glob.glob(os.path.join(versions_dir,
                              'More_Solutions_More_Problems_Reader_Edition_v*.pdf'))
pdfs.sort(key=lambda p: int(re.search(r'_v(\d+)', p).group(1)))
latest = pdfs[-1]
print(f'Scanning: {os.path.basename(latest)}', file=sys.stderr)

reader = PdfReader(latest)
PAGE_TEXT = []
for p in reader.pages:
    try:
        PAGE_TEXT.append(p.extract_text() or '')
    except Exception:
        PAGE_TEXT.append('')
TOTAL = len(PAGE_TEXT)


def find_strict(needle, start_page=1, end_page=None):
    if end_page is None:
        end_page = TOTAL
    for i in range(start_page - 1, end_page):
        if needle in PAGE_TEXT[i]:
            return i + 1
    return None


def pp(pdf_page):
    return None if pdf_page is None else str(pdf_page - 2)


PREFACE = find_strict('A Note on Origins')
TOC_END = PREFACE - 1 if PREFACE else 10
INTRO_CHAP = find_strict('The Great Paradox', TOC_END + 1)

CHAPTER_OPENER = {}
prev = TOC_END
for n, word in enumerate(['ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN',
                          'EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN',
                          'FOURTEEN','FIFTEEN'], 1):
    p = find_strict(f'CHAPTER {word}', prev + 1)
    CHAPTER_OPENER[n] = p
    if p:
        prev = p

PART = {
    'I':   find_strict('Two chapters establishing the mathematical', TOC_END + 1),
    'II':  find_strict('Seven domains. Seven independent bodies of research',
                       (CHAPTER_OPENER.get(2) or TOC_END) + 1),
    'III': find_strict('Two chapters laying out, in plain language, the framework',
                       (CHAPTER_OPENER.get(9) or TOC_END) + 1),
    'IV':  find_strict('Two chapters on cascade-aware design',
                       (CHAPTER_OPENER.get(11) or TOC_END) + 1),
}

prev = (CHAPTER_OPENER.get(15) or CHAPTER_OPENER.get(14)
        or CHAPTER_OPENER.get(13) or TOC_END)
CONCLUSION = find_strict('Living with the Paradox', prev + 1)
prev = CONCLUSION or prev
APPENDIX = {}
for letter in 'ABCDEFGH':
    needle = f'APPENDIX {letter}'
    p = find_strict(needle, prev + 1)
    APPENDIX[letter] = p
    if p:
        prev = p

BIBLIOGRAPHY = find_strict('BIBLIOGRAPHY', (APPENDIX['H'] or prev) + 1)
INDEX = find_strict('INDEX', (BIBLIOGRAPHY or prev) + 1)


def sub_in_chapter(sub_needle, ch_num):
    start = CHAPTER_OPENER.get(ch_num)
    if not start:
        return None
    end = CHAPTER_OPENER.get(ch_num + 1) or APPENDIX['A'] or TOTAL
    return find_strict(sub_needle, start, end)


toc = []
toc.append(('part', 'FRONT MATTER', ''))
toc.append(('chap', 'Preface — A Note on Origins', pp(PREFACE)))
toc.append(('part', 'INTRODUCTION', ''))
toc.append(('chap', 'The Great Paradox', pp(INTRO_CHAP)))
intro_end = CHAPTER_OPENER[1] or TOTAL
toc.append(('sub', 'The Day Britain Created More Snakes',
            pp(find_strict('The Day Britain Created More Snakes',
                            INTRO_CHAP or 1, intro_end))))
toc.append(('sub', 'What This Book Argues',
            pp(find_strict('What This Book Argues', INTRO_CHAP or 1, intro_end))))
toc.append(('sub', 'The Argument, in One Sentence',
            pp(find_strict('The Argument, in One Sentence',
                            INTRO_CHAP or 1, intro_end))))

toc.append(('part', 'PART I — THE THEORY', pp(PART['I'])))
toc.append(('chap', 'Chapter 1: The Law of Cascade Problems', pp(CHAPTER_OPENER[1])))
toc.append(('sub', 'Three Mechanisms of the Cascade',
            pp(sub_in_chapter('Three Mechanisms', 1))))
toc.append(('sub', "Murphy’s Law Is Not a Joke",
            pp(sub_in_chapter("Murphy's Law Is Not a Joke", 1))))
toc.append(('sub', 'The Exponential Trap',
            pp(sub_in_chapter('Exponential Trap', 1))))
toc.append(('chap', 'Chapter 2: Why We Always Repeat the Mistake',
            pp(CHAPTER_OPENER[2])))
toc.append(('sub', 'The Bias of Now', pp(sub_in_chapter('The Bias of Now', 2))))
toc.append(('sub', 'What Systems Thinking Offers',
            pp(sub_in_chapter('What Systems Thinking Offers', 2))))
toc.append(('sub', 'The Social Construction of Successful Solutions',
            pp(sub_in_chapter('The Social Construction', 2))))

toc.append(('part', 'PART II — THE EVIDENCE', pp(PART['II'])))
ch_evidence = [
    (3, 'Chapter 3: Mathematics — The Original Cascade',
     [("Hilbert’s Dream, Gödel’s Nightmare", "Hilbert's Dream"),
      ("Russell’s Paradox and Its Descendants", "Russell's Paradox"),
      ('The Halting Problem', 'The Halting Problem')]),
    (4, "Chapter 4: Physics — Nature’s Revenge",
     [("Maxwell’s Demon", "Maxwell's Demon"),
      ('Quantum Mechanics and the Measurement Crisis',
       'Quantum Mechanics and the Measurement Crisis')]),
    (5, 'Chapter 5: Computer Science — The Digital Cascade',
     [('Every Patch Opens a New Wound', 'Every Patch'),
      ("Brooks’ Law and the Mythical Man-Month", "Brooks' Law"),
      ('Feature Bloat and the Legacy Trap', 'Feature Bloat'),
      ("The Internet’s Unintended Children", "Internet's Unintended")]),
    (6, "Chapter 6: Economics — The Market’s Irony",
     [('The Cobra Effect', 'Cobra Effect'),
      ('Jevons Paradox: Efficiency Creates Demand', 'Jevons Paradox'),
      ("Goodhart’s Law", "Goodhart's Law"),
      ('The 2008 Financial Crisis', '2008 Financial Crisis')]),
    (7, 'Chapter 7: Medicine — The Healing Paradox',
     [('The Opioid Crisis', 'The Opioid Crisis'),
      ("Thalidomide’s Double Life", 'Thalidomide'),
      ('CRISPR and the Editing Problem', 'CRISPR')]),
    (8, 'Chapter 8: Politics — The Policy Boomerang',
     [('Prohibition and the Birth of the Mob', 'Prohibition'),
      ('The War on Drugs', 'War on Drugs'),
      ('GDPR and the Compliance Industrial Complex', 'GDPR')]),
    (9, 'Chapter 9: Society & Environment',
     [("Social Media’s Loneliness Paradox", 'Social Media'),
      ("Braess’s Paradox: When New Roads Make Traffic Worse", 'Braess'),
      ("The Green Revolution’s Hidden Cost", 'Green Revolution')]),
]
for n, ctit, subs in ch_evidence:
    toc.append(('chap', ctit, pp(CHAPTER_OPENER.get(n))))
    for tit_pretty, needle in subs:
        toc.append(('sub', tit_pretty, pp(sub_in_chapter(needle, n))))

toc.append(('part', 'PART III — THE CASCADE FRAMEWORK', pp(PART['III'])))
toc.append(('chap', 'Chapter 10: How the Cascade Works', pp(CHAPTER_OPENER[10])))
toc.append(('sub', 'The Solution-Problem Network',
            pp(sub_in_chapter('The Solution-Problem Network', 10))))
toc.append(('sub', 'How Problems Multiply',
            pp(sub_in_chapter('How Problems Multiply', 10))))
toc.append(('sub', 'The Central Claim',
            pp(sub_in_chapter('The Central Claim', 10))))
toc.append(('sub', 'The Tipping Point',
            pp(sub_in_chapter('The Tipping Point', 10))))
toc.append(('sub', 'The Shape of the Network Matters',
            pp(sub_in_chapter('The Shape of the Network Matters', 10))))
toc.append(('chap', 'Chapter 11: Measuring and Predicting Cascades',
            pp(CHAPTER_OPENER[11])))
toc.append(('sub', 'The Cascade Risk Index',
            pp(sub_in_chapter('The Cascade Risk Index', 11))))
toc.append(('sub', 'Early Warning Signals',
            pp(sub_in_chapter('Early Warning Signals', 11))))
toc.append(('sub', 'Limitations of the Cascade Risk Index',
            pp(sub_in_chapter('Limitations of the Cascade Risk Index', 11))))

toc.append(('part', 'PART IV — THE WAY FORWARD', pp(PART['IV'])))
toc.append(('chap', 'Chapter 12: Cascade-Aware Design', pp(CHAPTER_OPENER[12])))
toc.append(('sub', 'The Hippocratic Principle for Innovation',
            pp(sub_in_chapter('Hippocratic Principle', 12))))
toc.append(('sub', 'Pre-Mortem Analysis',
            pp(sub_in_chapter('Pre-Mortem Analysis', 12))))
toc.append(('sub', 'The Role of Modularity and Reversibility',
            pp(sub_in_chapter('Modularity', 12))))
toc.append(('sub', 'Sunset Clauses and Reversibility Requirements',
            pp(sub_in_chapter('Sunset Clauses', 12))))
toc.append(('chap', 'Chapter 13: A New Philosophy of Innovation',
            pp(CHAPTER_OPENER[13])))
toc.append(('sub', 'Second-Order Thinking',
            pp(sub_in_chapter('Second-Order Thinking', 13))))
toc.append(('sub', 'The Call to Action',
            pp(sub_in_chapter('The Call to Action', 13))))
toc.append(('chap', 'Chapter 14: The Case Against This Book',
            pp(CHAPTER_OPENER.get(14))))
toc.append(('chap', 'Chapter 15: How to Spot a Cascade Before It Hits You',
            pp(CHAPTER_OPENER.get(15))))

toc.append(('part', 'CONCLUSION & APPENDICES', ''))
toc.append(('chap', 'Conclusion: Living with the Paradox', pp(CONCLUSION)))
toc.append(('chap', 'Appendix A: Source Research', pp(APPENDIX['A'])))
toc.append(('chap', 'Appendix B: The Cascade Classification System',
            pp(APPENDIX['B'])))
toc.append(('chap', 'Appendix C: Fifty Solution-Problem Pairs',
            pp(APPENDIX['C'])))
toc.append(('chap', 'Appendix D: The Cascade Management Checklist',
            pp(APPENDIX['D'])))
toc.append(('chap', 'Appendix E: Extended Case Studies', pp(APPENDIX['E'])))
toc.append(('chap', 'Appendix F: A Glossary of Cascade Theory',
            pp(APPENDIX['F'])))
toc.append(('chap', 'Appendix G: A Practical Cascade Assessment Checklist',
            pp(APPENDIX['G'])))
toc.append(('chap', 'Appendix H: The Intellectual Genealogy of Cascade Theory',
            pp(APPENDIX['H'])))
toc.append(('chap', 'Bibliography', pp(BIBLIOGRAPHY)))
toc.append(('chap', 'Index', pp(INDEX)))

missing = [(k, t) for k, t, pg in toc if not pg and k != 'part']
if missing:
    print(f'\nWARNING — {len(missing)} entries unlocated:', file=sys.stderr)
    for k, t in missing:
        print(f'   ({k}) {t}', file=sys.stderr)
    print(file=sys.stderr)

print('# === AUTO-GENERATED TOC ===')
print(f'# Source: {os.path.basename(latest)} ({TOTAL} PDF pages)')
print()
print('toc = [')
for kind, text, pg in toc:
    text_esc = text.replace("'", "\\'")
    print(f"    ('{kind}', '{text_esc}', '{pg or ''}'),")
print(']')
