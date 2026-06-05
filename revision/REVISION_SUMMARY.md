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
retelling. **143,008 → ~127,900 words (−10.6%).** (The original −40% target was retired as unwise to
hit by blunt deletion; further trimming belongs in the copyedit.)

**Phase 3 — Integrity (the other big credibility fix).** New **Chapter 14, "The Case Against This
Book"** (~1,690 words) steelmans six objections and concedes what each takes. Added an explicit
**falsifiability statement** in the Introduction. Added a **CRI honesty caveat** (not a validated
instrument; worked scores are retrospective illustrations, not predictions).

**Phase 4 — Sourcing (triage).** Verification needs a human; delivered the infrastructure:
`claims_triage.csv` (303 STAT + 70 ATTRIB priority items) and `KNOWN_ISSUES.md` (curated flags +
corrections + an "already-sourced" list).

**Phase 5 — Polish (figures).** Split the figure system: **clean professional style for the 11
quantitative charts**, sketch style kept only for the **9 conceptual diagrams**; rewrote the figures
disclaimer to match. Copyedit + legal read are [Pro].

Net after Phases 0–5: **≈129,900 words** (Phase 3 added the adversarial chapter back).

---

## How to build the PDF (do this first)
This sandbox has no `matplotlib`, so no PDF was rendered here. On your machine:
```
pip install matplotlib numpy reportlab Pillow
python book_main_reader.py      # writes versions/More_Solutions_..._Reader_Edition_vN.pdf
```
Then read it end-to-end. Confirm: (1) the reframed claims read well, (2) Chapter 14 lands, (3) the
clean-style charts look right.

---

## What remains — and who must do it
| Item | Owner | Notes |
|---|---|---|
| Render `v23` and read it | **You** | needs matplotlib; the one true blocker |
| Fact-check the claims | **Fact-checker** | brief: `handoff/FACT_CHECK_BRIEF.md`; worklist: `claims_triage.csv` |
| Legal / defamation read | **Lawyer** | checklist: `handoff/LEGAL_REVIEW_CHECKLIST.md` |
| Citation/endnotes apparatus | AI, **after** fact-check | I can add the flowable + back-matter once sources exist |
| Professional copyedit | **Copyeditor** | comma splices etc.; also trims length further |
| Expert sign-off (4 fields) | **You + experts** | brief: `handoff/EXPERT_REVIEWER_BRIEF.md` |
| Front/back matter (copyright, ISBN, bio, acks) | **You** (+AI to typeset) | content needs you |
| Cover subtitle "A Theory of…" | **You** | branding call; flagged, not changed |
| Query agents / publish | **You** | drafts: `handoff/AGENT_QUERY_AND_SYNOPSIS.md` |

## Reversibility
Everything is whole-block and logged. To see any original: `git show v22-baseline:<file>`. Per-phase
detail in `revision/PHASE{1..5}_LOG.md`, `PHASE2_CUTLOG.md`, `KNOWN_ISSUES.md`.

## Bottom line
The two changes that decide whether this book is taken seriously — **dropping the false "proven law"
framing (Phase 1)** and **making it argue honestly against itself (Phase 3)** — are done. The rest is
verification, polish, and review that only humans/tools outside this sandbox can complete.
