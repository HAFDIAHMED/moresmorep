#!/usr/bin/env python3
"""
Phase 2 structural cutter — delete whole redundant sections by title.

Given a file and a list of exact section titles, it locates each section heading
(`story.append(P('<title>', S['section']))`), expands the start upward to swallow
the section's leading blank line / `# -- ... --` comment / `story.append(SP(...))`
spacers, and deletes through to the line just before the NEXT section heading (or
the chapter's `return story` / next `def`). Whole-block, reversible deletions.

Usage (dry run prints spans, no write):
    python revision/phase2_cut.py <file> --dry "Title A" "Title B"
Apply:
    python revision/phase2_cut.py <file> "Title A" "Title B"
"""
import sys, re, io

SECT = "S['section']"

def find_heading(lines, title):
    for i, ln in enumerate(lines):
        if SECT in ln and 'P(' in ln:
            norm = ln.replace("\\'", "'").replace('\\"', '"')
            if title in norm:
                return i
    return -1

def is_heading_line(ln):
    return SECT in ln and ('P(' in ln)

def expand_start(lines, idx):
    """Walk upward over the section's own preceding blank/comment/SP spacer lines."""
    s = idx
    j = idx - 1
    while j >= 0:
        t = lines[j].strip()
        if t == '' or t.startswith('# ') or t.startswith('#--') or \
           t.startswith('# --') or 'story.append(SP(' in lines[j]:
            s = j
            j -= 1
            continue
        break
    return s

def find_end(lines, idx):
    """End = line before the next section heading / return / next def."""
    j = idx + 1
    while j < len(lines):
        ln = lines[j]
        if is_heading_line(ln):
            break
        if re.match(r'\s*return story', ln) or re.match(r'^def ', ln):
            break
        j += 1
    # back up over the trailing blank/comment/SP that belongs to the NEXT block's lead-in
    e = j - 1
    while e > idx:
        t = lines[e].strip()
        if t == '' or t.startswith('# ') or 'story.append(SP(' in lines[e]:
            e -= 1
            continue
        break
    return e

def main():
    args = sys.argv[1:]
    dry = '--dry' in args
    args = [a for a in args if a != '--dry']
    path, titles = args[0], args[1:]
    lines = open(path, encoding='utf-8').read().split('\n')
    spans = []
    for t in titles:
        idx = find_heading(lines, t)
        if idx < 0:
            print('NOT FOUND:', t.encode('ascii', 'replace').decode()); continue
        s = expand_start(lines, idx)
        e = find_end(lines, idx)
        spans.append((s, e, t))
        head = lines[idx].strip().encode('ascii', 'replace').decode()[:60]
        print(f'span lines {s+1}-{e+1} ({e-s+1} lines)  <-  {head}')
    if dry:
        print('DRY RUN — no changes written'); return
    # delete descending so earlier indices stay valid
    spans.sort(key=lambda x: x[0], reverse=True)
    new = lines[:]
    for s, e, _ in spans:
        del new[s:e+1]
    open(path, 'w', encoding='utf-8', newline='\n').write('\n'.join(new))
    print(f'lines {len(lines)} -> {len(new)} (removed {len(lines)-len(new)})')

if __name__ == '__main__':
    main()
