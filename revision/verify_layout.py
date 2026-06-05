#!/usr/bin/env python3
"""
Layout verifier — catches the two pagination bugs after any rebuild.

Scans a rendered PDF and reports:
  1. Orphaned figure captions  — a 'Figure X:' caption on a page with NO image.
  2. Caption-less image pages   — an image whose caption isn't on the same page.
  3. Orphaned headings          — a bold section/subsection heading that is the
                                  last text on a page (its paragraph fell overleaf).

Usage: python revision/verify_layout.py [path-to.pdf]
Requires: pymupdf  (pip install pymupdf)
Exit code 0 = clean, 1 = problems found.
"""
import sys, re, glob, os

def newest_pdf():
    vs = glob.glob(os.path.join(os.path.dirname(__file__), '..', 'versions',
                                'More_Solutions_More_Problems_Reader_Edition_v*.pdf'))
    return max(vs, key=lambda p: int(re.search(r'_v(\d+)\.pdf$', p).group(1))) if vs else None

def main():
    import fitz
    path = sys.argv[1] if len(sys.argv) > 1 else newest_pdf()
    print('Checking:', os.path.basename(path))
    doc = fitz.open(path)
    # A caption line mentions 'Figure <id>' AND has a colon (handles
    # 'Figure 1.3 (Illustrative):'); body cross-refs without a colon are ignored.
    fig_re = re.compile(r'Figure\s+[\w.]+', re.I)

    def captions_on(txt):
        return [ln for ln in txt.splitlines()
                if fig_re.search(ln) and ':' in ln]

    fig_orphans, capless, head_orphans = [], [], []
    caps_total = 0
    for i, p in enumerate(doc):
        txt = p.get_text()
        nimg = len(p.get_images(full=True))
        caps = captions_on(txt)
        caps_total += len(caps)
        if caps and nimg == 0:
            fig_orphans.append((i + 1, caps))
        if nimg > 0 and not caps:
            capless.append(i + 1)
        # heading at page bottom?
        spans = [s for b in p.get_text('dict')['blocks'] for l in b.get('lines', [])
                 for s in l.get('spans', []) if s['text'].strip()]
        cand = [s for s in spans if not s['text'].strip().isdigit()]
        if cand:
            last = sorted(cand, key=lambda s: s['bbox'][3])[-1]
            f, sz = last['font'], last['size']
            sec = sz >= 12.5 and 'Bold' in f and 'Italic' not in f
            sub = 10.5 <= sz < 12.5 and 'Bold' in f and 'Italic' in f
            if sec or sub:
                head_orphans.append((i + 1, last['text'].strip()[:60]))
    print(f'pages={len(doc)}  figure-captions={caps_total}')
    print(f'  orphaned figure captions : {len(fig_orphans)}  {fig_orphans or ""}')
    print(f'  caption-less image pages : {len(capless)}  {capless or ""}')
    print(f'  orphaned headings        : {len(head_orphans)}  {head_orphans or ""}')
    ok = not (fig_orphans or capless or head_orphans)
    print('RESULT:', 'CLEAN' if ok else 'PROBLEMS FOUND')
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()
