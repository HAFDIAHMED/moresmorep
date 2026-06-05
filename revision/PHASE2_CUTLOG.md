# Phase 2 — Structural Cut (log)

Goal: reduce ~143k → ~86k words (−40%). Every cut here is a whole-block deletion, fully
reversible via git (`git show v22-baseline:<file>` or `git revert`). Nothing is rewritten in a
way that loses unique content — only **duplicate** coverage and **redundant second/third
"Synthesis"** sections are removed.

## The redundancy pattern (why this is safe)
Chapters 3–9 were each extended in passes; every pass appended a new "Synthesis" and often
re-covered topics already handled. The inventory shows the fingerprint: chapters with **two or
three** "Chapter N Synthesis" sections and the same case study appearing twice.

## Cuts applied

### Chapter 7 (Medicine) — DONE  ✅  11,080 → 8,701 words (−2,379)
`book_chapters_7to9_reader.py`
- Removed the **first** of two syntheses ("The Healer's Paradox") — the second ("The Healer's
  Infinite Task") is retained as the chapter synthesis.
- Removed the **duplicate topic block** that re-covered vaccination, organ transplantation, and
  diagnostics a second time ("Vaccination and the Trust Cascade", "The Transplantation Cascade and
  the Organ Allocation Dilemma", "Personalised Medicine and the Diagnostic Expansion Cascade") —
  these are already covered earlier by "The Vaccination Hesitancy Cascade", "Organ Transplantation
  and the Immunosuppression Cascade", and "The Diagnostic Cascade: More Tests, More Problems".
- Kept: all unique topics (incl. both distinct mental-health angles — psychiatric pharmacology and
  DSM diagnostic-expansion) and Figure 7.1.

## Reality check on the −40% target
Dedupe + redundant-synthesis removal alone yields roughly **−15%** (≈120–125k). The remaining
~35k words needed to reach ~86k cannot be removed without **editorial decisions that are the
author's to make** — see the fork recorded in the chat / next step:
1. **Conservative (safe, ~120k):** dedupe + redundant syntheses only, across all chapters.
2. **Target (~86k):** also merge the seven evidence chapters into ~5, trim within-section padding
   (the tricolon/"not-X-but-Y" bloat), and condense the appendices. Higher reward, needs sign-off
   on what to merge.
