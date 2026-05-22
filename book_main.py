#!/usr/bin/env python3
"""
MORE SOLUTIONS = MORE PROBLEMS
Main runner — assembles all chapter modules and builds the complete PDF.

Run: python3 book_main.py
Output: More_Solutions_More_Problems.pdf
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from generate_book import build_book, on_first, on_page, PW, PH, ML, MR, MT, MB

from book_chapters_intro  import preface, intro_chapter, chapter1, chapter2, chapter3
from book_chapters_4to6   import chapter4, chapter5, chapter6
from book_chapters_7to9   import chapter7, chapter8, chapter9
from book_chapters_10to13 import chapter10, chapter11, chapter12, chapter13, conclusion, appendices

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate

OUTPUT = os.path.join(os.path.dirname(__file__), 'More_Solutions_More_Problems.pdf')

def main():
    print("Building front matter…")
    story, S = build_book()

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

    print("Building Part IV (Chapters 12–13)…")
    story += chapter12(S)
    story += chapter13(S)

    print("Building Conclusion & Appendices…")
    story += conclusion(S)
    story += appendices(S)

    print(f"Assembling PDF → {OUTPUT}")
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=ML,
        rightMargin=MR,
        topMargin=MT,
        bottomMargin=MB,
        title='More Solutions = More Problems',
        author='Ahmed Hafdi',
        subject='A Theory of Cascade Innovation and the Hidden Cost of Progress',
    )
    doc.build(story, onFirstPage=on_first, onLaterPages=on_page)
    print(f"Done. PDF written to: {OUTPUT}")

if __name__ == '__main__':
    main()
