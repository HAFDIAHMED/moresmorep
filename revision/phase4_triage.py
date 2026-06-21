#!/usr/bin/env python3
"""
Phase 4 pre-fact-check triage.

Reads revision/claims_register.csv (produced by phase0_analyze.py) and buckets every
row so a human fact-checker can work the high-risk claims first instead of all ~1,240
rows blind. This does NOT verify anything against sources — no network here — it only
categorises and prioritises.

Categories:
  STAT   — hard quantitative/empirical claim ($, %, million/billion/trillion, death
           tolls, lives saved): highest fact-check priority
  ATTRIB — an epigraph / quotation attribution: verify wording + author
  NAV    — navigational/cross-reference or trivially a non-claim: drop (false positive)
  DATE   — a dated historical statement without a hard number: lower priority
  OTHER  — everything else

Output: revision/claims_triage.csv (adds category + priority columns) and a console summary.
"""
import csv, re, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'claims_register.csv')
OUT = os.path.join(HERE, 'claims_triage.csv')

STAT = re.compile(r'(\$|\b\d+(\.\d+)?\s?(million|billion|trillion)\b|\d+\s?%|'
                  r'\b(deaths?|overdose|lives|fatalities|casualties|killed)\b|'
                  r'\bGWh?\b|\bTWh\b|\bppm\b|\btonnes?\b|\bper cent\b)', re.I)
NAV  = re.compile(r'\bChapters?\b|\bAppendix\b|\bPart (I|II|III|IV)\b|see also', re.I)
DATE = re.compile(r'\b(1[5-9]\d{2}|20\d{2})\b')

def categorise(row_type, text):
    if row_type == 'epigraph':
        return 'ATTRIB', 2
    words = len(text.split())
    if NAV.search(text) and words < 28:
        return 'NAV', 5
    if STAT.search(text):
        return 'STAT', 1
    # attribution line captured as a quant-claim (short, ends with a name/year)
    if words < 16 and DATE.search(text) and ('—' in text or text.count(',') >= 1):
        return 'ATTRIB', 2
    if DATE.search(text):
        return 'DATE', 3
    return 'OTHER', 4

def main():
    rows = list(csv.reader(open(SRC, encoding='utf-8-sig')))
    header, data = rows[0], rows[1:]
    out = [['id', 'chapter_fn', 'type', 'category', 'priority', 'text',
            'verdict (TODO)', 'source (TODO)']]
    from collections import Counter
    cats = Counter()
    for r in data:
        if len(r) < 4:
            continue
        rid, ch, typ, text = r[0], r[1], r[2], r[3]
        cat, pri = categorise(typ, text)
        cats[cat] += 1
        out.append([rid, ch, typ, cat, pri, text, '', ''])
    # sort by priority then chapter for a ready-to-work sheet
    body = sorted(out[1:], key=lambda x: (x[4], x[1], int(x[0])))
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f); w.writerow(out[0]); w.writerows(body)
    total = sum(cats.values())
    print(f'triaged {total} rows -> {OUT}')
    for c in ['STAT', 'ATTRIB', 'DATE', 'OTHER', 'NAV']:
        print(f'  {c:6} {cats[c]:4}  ({100*cats[c]//total}%)')
    print(f'High-priority STAT claims to verify first: {cats["STAT"]}')

if __name__ == '__main__':
    main()
