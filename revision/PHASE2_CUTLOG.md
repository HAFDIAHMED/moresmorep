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

### Chapters 3–6, 8–9 — DONE  ✅  (conservative dedupe, via `revision/phase2_cut.py`)
Each chapter reduced to exactly **one** synthesis; blatant duplicate topic sections removed.
- **Ch3 (Mathematics)** 6,753 → 6,123: cut "The Computability Cascade" (re-covers the halting
  problem / undecidability / crypto already in earlier sections) and "Extended Synthesis: Why
  Mathematics Is Not Exempt".
- **Ch4 (Physics)** 10,463 → 8,720: cut two redundant syntheses ("What Physics Teaches Us",
  "The Physicist's Melancholy" — kept "Physics and the Limits of Knowability") and "The Measurement
  Problem and the Cascade of Interpretation" (dup of the measurement-crisis section).
- **Ch5 (Computer Science)** 11,556 → 9,372: cut one of two syntheses, "The Artificial Intelligence
  Inflection" (dup of "The AI Alignment Cascade"), "Open Source and the Dependency Cascade" (dup of
  "Open Source Software"), and "Platform Economics and the Network Effect Cascade" (dup of "Platform
  Monopolies").
- **Ch6 (Economics)** 13,165 → 11,482: cut "Extended Synthesis: The Self-Referential Economy",
  "Trade Policy and the Cascade of Comparative Advantage" (dup of "Trade Liberalisation"), and "The
  Inequality Cascade" (dup of the QE inequality section).
- **Ch8 (Politics)** 9,094 → 8,295: cut the duplicate synthesis "The State as Cascade Generator"
  (kept "The State as Cascade Architecture").
- **Ch9 (Social/Ecological)** 15,035 → 13,441: cut "Extended Synthesis: The Cascade in Daily Life",
  "The Food System Cascade" (dup of "The Green Revolution"), and "Transportation, Mobility, and the
  Urban Cascade" (dup of "The Urban Planning Cascade").

**Phase-2 dedupe total so far: 143,008 → 131,996 words (−11,012).** All whole-block, git-reversible.
Ch9 is still the longest (13.4k) and has further candidates (surveillance capitalism, AI cognition,
energy transition) held back as borderline.

### Round 2 — theory chapters + Ch9 borderline  ✅  131,996 → 128,422 (−3,574)
- **Ch1:** cut "The Cascade and Murphy's Law: A Precise Relationship" (dup of "Murphy's Law Is Not a
  Joke"), "The Three Mechanisms, Looked At More Closely" (dup of "The Three Mechanisms"), and "The
  Digital Revolution as Second Industrial Revolution" (overlaps "Four Technological Revolutions").
- **Ch2:** cut "Temporal Discounting and the Cascade Horizon" and "Scope Insensitivity and the
  Collapse of Cascade Accounting" (both already covered as sub-parts of "The Bias of Now"), and
  "Narrative and Metaphor in Innovation Discourse" (overlaps "The Narrative Fallacy").
- **Ch9:** cut "The Surveillance Capitalism Cascade" and "Artificial Intelligence and the Cognition
  Cascade" (overlap social-media / GPS-cognition / Ch5 AI). **Kept** "The Energy Transition and the
  Resource Cascade" — genuinely distinct (lithium/rare-earth), not a dup.

**Cumulative Phase 2: 143,008 → 128,422 (−14,586, −10.2%).** Safe whole-block dedupe is now
essentially exhausted — remaining sections are distinct topics.

## Reality check on the −40% target
Dedupe + redundant-synthesis removal alone yields roughly **−15%** (≈120–125k). The remaining
~35k words needed to reach ~86k cannot be removed without **editorial decisions that are the
author's to make** — see the fork recorded in the chat / next step:
1. **Conservative (safe, ~120k):** dedupe + redundant syntheses only, across all chapters.
2. **Target (~86k):** also merge the seven evidence chapters into ~5, trim within-section padding
   (the tricolon/"not-X-but-Y" bloat), and condense the appendices. Higher reward, needs sign-off
   on what to merge.
