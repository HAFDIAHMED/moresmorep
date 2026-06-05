#!/usr/bin/env python3
"""
Phase 0 analysis — baseline inventory + claims register for the revision.

Parses the Reader's Edition chapter modules with Python's AST, extracts the
prose carried inside P()/callout()/theorem_box()/epigraph()/chapter_opener()/
part_page() calls and ('kind', text) content tuples, and produces:

  revision/inventory.md         — per-chapter word counts + structural map
  revision/claims_register.csv  — every quantitative claim, epigraph, and
                                  named attribution, for the Phase 4 fact-check

Run: python3 revision/phase0_analyze.py
Pure stdlib; no third-party dependencies.
"""
import ast, os, csv, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# Reader's Edition modules in reading order, with the chapter functions each defines.
MODULES = [
    ("book_chapters_intro_reader.py",
     ["preface", "intro_chapter", "chapter1", "chapter2", "chapter3"]),
    ("book_chapters_4to6_reader.py",
     ["chapter4", "chapter5", "chapter6"]),
    ("book_chapters_7to9_reader.py",
     ["chapter7", "chapter8", "chapter9"]),
    ("book_chapters_10to13_reader.py",
     ["chapter10", "chapter11", "chapter12", "chapter13", "chapter14", "conclusion", "appendices"]),
]

# Style keys / short control strings we never want to count as prose.
STYLE_KEYS = {
    'body', 'body0', 'section', 'subsection', 'bold_body', 'italic_body',
    'caption', 'epigraph', 'epig_attr', 'blockquote', 'theorem', 'theorem_b',
    'list', 'note', 'preface', 'preface_t', 'formula', 'chap_num', 'chap_title',
    'chap_sub', 'part_label', 'part_title', 'part_desc',
}

CONTENT_CALLS = {'P', 'callout', 'theorem_box', 'epigraph',
                 'chapter_opener', 'part_page'}


def const_str(node):
    """Return the string value of a Constant node, else None."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def clean(text):
    """Collapse the source's wrapped whitespace the way the book does."""
    return ' '.join(text.split())


def strip_tags(text):
    """Remove the simple inline markup tags used in the prose."""
    text = re.sub(r'<[^>]+>', '', text)
    return clean(text)


def is_prose(s):
    """Heuristic: a real prose string, not a style key or tiny control token."""
    if s is None:
        return False
    if s.strip() in STYLE_KEYS:
        return False
    return len(s.split()) >= 4 or len(s) >= 28


def wordcount(s):
    return len(strip_tags(s).split())


# Sentence splitter that is conservative about abbreviations/decimals.
_SENT = re.compile(r'(?<=[.!?])\s+(?=[A-Z"“(])')
_HAS_NUMBER = re.compile(r'(\$\s?\d|\d+\s?%|\b\d{2,}\b|\b\d+(\.\d+)?\s?(million|billion|trillion|thousand'
                         r'|percent|years?|deaths?|ppm|GW|TWh|tonnes?|km|mg|mph|x|×)\b'
                         r'|\b(1[5-9]\d{2}|20\d{2})\b)', re.IGNORECASE)


def analyze():
    inventory = []          # (module, func, words, n_sections, n_callouts, n_theorems, n_epigraphs, n_figs, sections[])
    claims = []             # (chapter, kind, text, source_func)

    for fname, funcs in MODULES:
        path = os.path.join(ROOT, fname)
        with open(path, encoding='utf-8') as fh:
            tree = ast.parse(fh.read(), filename=fname)

        funcdefs = {n.name: n for n in tree.body
                    if isinstance(n, ast.FunctionDef)}

        for func in funcs:
            node = funcdefs.get(func)
            if node is None:
                inventory.append((fname, func, 0, 0, 0, 0, 0, 0, []))
                continue

            words = 0
            sections = []
            n_callout = n_theorem = n_epigraph = n_fig = 0

            for sub in ast.walk(node):
                # ---- call-based content ----
                if isinstance(sub, ast.Call):
                    cname = (sub.func.id if isinstance(sub.func, ast.Name)
                             else getattr(sub.func, 'attr', ''))
                    if cname == 'callout':
                        n_callout += 1
                    elif cname == 'theorem_box':
                        n_theorem += 1
                    elif cname == 'epigraph':
                        n_epigraph += 1
                        args = [const_str(a) for a in sub.args]
                        if args and args[0]:
                            attr = args[1] if len(args) > 1 and args[1] else ''
                            claims.append((func, 'epigraph',
                                           strip_tags(args[0]) + (f'  —{strip_tags(attr)}' if attr else ''),
                                           cname))
                    elif cname and cname.startswith('fig_'):
                        n_fig += 1

                    # section heading via P(text, S['section'])
                    if cname == 'P' and len(sub.args) >= 2:
                        key = None
                        a1 = sub.args[1]
                        if isinstance(a1, ast.Subscript):
                            key = const_str(a1.slice)
                        if key in ('section', 'subsection'):
                            head = const_str(sub.args[0])
                            if head:
                                sections.append((key, strip_tags(head)))

                # ---- ('kind', text) content tuples ----
                if isinstance(sub, ast.Tuple) and len(sub.elts) == 2:
                    k = const_str(sub.elts[0])
                    t = const_str(sub.elts[1])
                    if k in ('section', 'subsection') and t:
                        sections.append((k, strip_tags(t)))

            # word count: every prose constant in the function
            for sub in ast.walk(node):
                s = const_str(sub)
                if is_prose(s):
                    words += wordcount(s)
                    # quantitative-claim extraction
                    for sent in _SENT.split(strip_tags(s)):
                        sent = sent.strip()
                        if len(sent.split()) >= 5 and _HAS_NUMBER.search(sent):
                            claims.append((func, 'quant-claim', sent, ''))

            inventory.append((fname, func, words,
                              sum(1 for k, _ in sections if k == 'section'),
                              n_callout, n_theorem, n_epigraph, n_fig, sections))

    return inventory, claims


def write_inventory(inventory):
    out = os.path.join(HERE, 'inventory.md')
    total_words = sum(r[2] for r in inventory)
    with open(out, 'w', encoding='utf-8') as f:
        f.write("# Baseline Inventory — Reader's Edition (Phase 0)\n\n")
        f.write(f"**Total prose words (approx):** {total_words:,}\n\n")
        f.write("Approximate: counts prose inside P()/callout()/theorem_box()/epigraph()/"
                "content-tuple calls, inline tags stripped. Excludes figure-internal "
                "matplotlib text and PDF chrome.\n\n")
        f.write("| Module | Chapter fn | Words | Sections | Callouts | Theorem boxes | Epigraphs | Figures |\n")
        f.write("|---|---|--:|--:|--:|--:|--:|--:|\n")
        for (mod, fn, w, nsec, ncall, nthm, nepi, nfig, _secs) in inventory:
            f.write(f"| {mod.replace('book_chapters_','').replace('_reader.py','')} "
                    f"| `{fn}` | {w:,} | {nsec} | {ncall} | {nthm} | {nepi} | {nfig} |\n")
        f.write(f"\n**TOTAL** — {total_words:,} words\n\n")
        f.write("---\n\n## Structural map (section headings in order)\n\n")
        for (mod, fn, w, nsec, ncall, nthm, nepi, nfig, secs) in inventory:
            f.write(f"### `{fn}`  ({w:,} words)\n")
            if not secs:
                f.write("_(no detected section headings — opener-only or list-driven)_\n\n")
                continue
            for kind, head in secs:
                bullet = "- " if kind == 'section' else "    - "
                f.write(f"{bullet}{head}\n")
            f.write("\n")
    return out, total_words


def write_claims(claims):
    out = os.path.join(HERE, 'claims_register.csv')
    # utf-8-sig so Excel renders em-dashes/accents correctly on open.
    with open(out, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['id', 'chapter_fn', 'type', 'text',
                    'verdict (TODO)', 'source (TODO)', 'notes (TODO)'])
        for i, (fn, kind, text, _src) in enumerate(claims, 1):
            w.writerow([i, fn, kind, text, '', '', ''])
    return out, len(claims)


if __name__ == '__main__':
    inv, claims = analyze()
    inv_path, total = write_inventory(inv)
    cl_path, n = write_claims(claims)
    print(f"Inventory  -> {inv_path}  ({total:,} words)")
    print(f"Claims reg -> {cl_path}  ({n} rows)")
