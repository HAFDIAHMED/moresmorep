#!/usr/bin/env python3
"""
MORE SOLUTIONS = MORE PROBLEMS — Reader's Edition
Assembles all chapter modules and builds the accessible PDF
(formal proofs and symbolic notation removed; figures, callouts,
case studies, and historical evidence preserved; underlying research
paper referenced in the Preface and in Appendix A).

Each run produces a NEW numbered version — older builds are never overwritten.
The output filename is `More_Solutions_More_Problems_Reader_Edition_vN.pdf`
where N is one higher than the highest existing version in the folder.

Run: python3 book_main_reader.py
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))

from generate_book import build_book, on_first, on_page, PW, PH, ML, MR, MT, MB

from book_chapters_intro_reader   import preface, intro_chapter, chapter1, chapter2, chapter3
from book_chapters_4to6_reader    import chapter4, chapter5, chapter6
from book_chapters_7to9_reader    import chapter7, chapter8, chapter9
from book_chapters_10to13_reader  import (chapter10, chapter11, chapter12, chapter13,
                                          chapter14, conclusion, appendices)

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate


BASENAME = 'More_Solutions_More_Problems_Reader_Edition'
PROJECT_DIR = os.path.dirname(__file__) or '.'
VERSIONS_DIR = os.path.join(PROJECT_DIR, 'versions')


def next_version_path():
    """Find the next available _vN.pdf filename in the versions/ folder.

    All numbered Reader's Edition builds live in `<project>/versions/` to keep
    the project root clean. The folder is created if it does not exist yet.
    """
    os.makedirs(VERSIONS_DIR, exist_ok=True)
    pattern = re.compile(rf'^{re.escape(BASENAME)}_v(\d+)\.pdf$', re.IGNORECASE)
    highest = 0
    for name in os.listdir(VERSIONS_DIR):
        m = pattern.match(name)
        if m:
            n = int(m.group(1))
            if n > highest:
                highest = n
    new_version = highest + 1
    return os.path.join(VERSIONS_DIR, f'{BASENAME}_v{new_version}.pdf'), new_version


OUTPUT, VERSION = next_version_path()


def main():
    print(f"=== Reader's Edition build — version {VERSION} ===")
    print(f"Output: {OUTPUT}\n")
    print("Building front matter (Reader's Edition)…")
    story, S = build_book(accessible=True)

    print("Building Preface…")
    story += preface(S)

    print("Building Introduction…")
    story += intro_chapter(S)

    print("Building Part I (Chapters 1–2)…")
    story += chapter1(S)
    story += chapter2(S)

    print("Building Part II (Chapters 3–9)…")
    story += chapter3(S)
    story += chapter4(S)
    story += chapter5(S)
    story += chapter6(S)
    story += chapter7(S)
    story += chapter8(S)
    story += chapter9(S)

    print("Building Part III (Chapters 10–11)…")
    story += chapter10(S)
    story += chapter11(S)

    print("Building Part IV (Chapters 12–14)…")
    story += chapter12(S)
    story += chapter13(S)
    story += chapter14(S)

    print("Building Conclusion & Appendices…")
    story += conclusion(S)
    story += appendices(S)

    print(f"Assembling PDF -> {OUTPUT}")
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=ML,
        rightMargin=MR,
        topMargin=MT,
        bottomMargin=MB,
        title="More Solutions = More Problems — Reader's Edition",
        author='Ahmed Hafdi',
        subject="A Theory of Cascade Innovation — Reader's Edition",
    )
    doc.build(story, onFirstPage=on_first, onLaterPages=on_page)
    print(f"Done. PDF written to: {OUTPUT}")


if __name__ == '__main__':
    main()
