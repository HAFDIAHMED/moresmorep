# Revision 2.0 — Master Summary

Branch: `revision-2.0`  ·  Baseline tag: `v22-baseline`  ·  Goal: take the book from
"strong idea, unpublishable execution (C+)" toward a globally publishable trade title.

This file is the single place to understand what changed, what's left, and how to build it.

---

## What changed, by phase (all committed + pushed)

**Phase 0 — Baseline.** Tagged `v22-baseline`; built an AST inventory (`phase0_analyze.py`) and a
1,200-row claims register. Baseline: **143,008 words**.

**Phase 1 — De-overclaim (the credibility fix).** Removed every instance of the book presenting its
own idea as a *proven law/theorem/mathematical certainty/inevitability*. "Cascade Theorem" → "Cascade
framework/pattern"; "Three Laws" → "Three Principles"; "Main Theorem" → "central claim"; the doubling
argument now distinguishes *possible interactions* (which double) from *real problems* (a non-zero
fraction). De-grandiosed ("next stage of civilisational maturity" etc.). Also reconciled the stale
"Map of the Book." Final grep: zero self-overclaim phrases remain.

**Phase 2 — Structural cut.** Removed ~14 duplicate topic sections and ~8 surplus syntheses so every
chapter has exactly one synthesis and no topic is covered twice; tightened the redundant cobra
retelling. A later **deep de-boring trim** (keeping all chapter numbers and cross-references valid —
no renumber) then took it to the author's ≤100k target by removing the repetitive framework
re-explanation, duplicate appendix material, and secondary/overlapping sections across every chapter,
while preserving every canonical case study, Chapter 14, the figures, and the original cover.
**143,008 → 99,938 words (−30%); 354 → 283 pages.**

**Phase 3 — Integrity (the other big credibility fix).** New **Chapter 14, "The Case Against This
Book"** (~1,690 words) steelmans six objections and concedes what each takes. Added an explicit
**falsifiability statement** in the Introduction. Added a **CRI honesty caveat** (not a validated
instrument; worked scores are retrospective illustrations, not predictions).

**Phase 4 — Sourcing (triage).** Verification needs a human; delivered the infrastructure:
`claims_triage.csv` (303 STAT + 70 ATTRIB priority items) and `KNOWN_ISSUES.md` (curated flags +
corrections + an "already-sourced" list).

**Phase 5 — Polish (figures).** Split the figure system: **clean professional style for the 11
quantitative charts**, sketch style kept only for the **9 conceptual diagrams**; rewrote the figures
disclaimer to match. Later fixed the **text/arrow overlaps** in the tree diagrams (boxes drawn on top
of connector arrows via z-order). Copyedit + legal read remain [Pro].

**Plus:** accuracy corrections (apocryphal Einstein epigraphs replaced; antibiotic-resistance figures
updated to the 2019 Lancet 1.27M and the "10M by 2050" framed as a contested projection; estimates
hedged); a commercial cover subtitle was trialled and **reverted at the author's request**.

Final state, rendered as **v27**: **99,938 words / 283 pages.**

---

## The built PDF
The current book is rendered at `versions/More_Solutions_More_Problems_Reader_Edition_v27.pdf`
(283 pages). To rebuild after any edit:
```
pip install matplotlib numpy reportlab Pillow
python book_main_reader.py      # writes the next versions/..._Reader_Edition_vN.pdf
```
(Optional: install the "xkcd Script"/"Humor Sans" font for the true hand-drawn look on the conceptual
diagrams; without it they render in a clean fallback font.)

---

## What remains — and who must do it
| Item | Owner | Notes |
|---|---|---|
| Read `v27` end-to-end | **You** | already rendered (283 pp); confirm it reads well |
| Fact-check the claims | **Fact-checker** | brief: `handoff/FACT_CHECK_BRIEF.md`; worklist: `claims_triage.csv` |
| Legal / defamation read | **Lawyer** | checklist: `handoff/LEGAL_REVIEW_CHECKLIST.md` |
| Citation/endnotes apparatus | AI, **after** fact-check | I can add the flowable + back-matter once sources exist |
| Professional copyedit | **Copyeditor** | comma splices etc.; also trims length further |
| Expert sign-off (4 fields) | **You + experts** | brief: `handoff/EXPERT_REVIEWER_BRIEF.md` |
| Front/back matter (copyright, ISBN, bio, acks) | **You** (+AI to typeset) | content needs you |
| Cover/subtitle | **You** | original kept by your choice; a punchier subtitle is an option |
| Literal 7→5 chapter merge | **You + AI** | optional; needs a scripted remap of ~250 cross-refs + spot-check |
| Query agents / publish | **You** | drafts: `handoff/AGENT_QUERY_AND_SYNOPSIS.md` |

## Reversibility
Everything is whole-block and logged. To see any original: `git show v22-baseline:<file>`. Per-phase
detail in `revision/PHASE{1..5}_LOG.md`, `PHASE2_CUTLOG.md`, `KNOWN_ISSUES.md`.

## Bottom line
The two changes that decide whether this book is taken seriously — **dropping the false "proven law"
framing (Phase 1)** and **making it argue honestly against itself (Phase 3)** — are done. The rest is
verification, polish, and review that only humans/tools outside this sandbox can complete.
