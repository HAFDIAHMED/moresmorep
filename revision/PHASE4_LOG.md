# Phase 4 — Evidence & Sourcing (log)

**Honest scope:** the actual fact-check (verifying claims against live sources) is a [Pro/Author]
job and cannot be done in this sandbox — no network. What this phase delivered is the **pre-fact-check
infrastructure** that makes that job fast and targeted, plus an expert pass flagging the claims most
likely to be wrong.

## Done ✅ (AI-doable)
1. **`revision/phase4_triage.py`** — buckets the claims register by type/priority.
2. **`revision/claims_triage.csv`** — the register, categorised and sorted so the highest-risk claims
   come first. Of 1,188 rows:
   - **STAT 303** (hard $/%/deaths/lives numbers) — verify first
   - **ATTRIB 70** (quotation attributions) — verify wording + author
   - DATE 572, OTHER 213, NAV 30 (mostly lower-priority or false positives)
   The fact-checker works ~373 priority items, not 1,188.
3. **`revision/KNOWN_ISSUES.md`** — curated expert flags: misattributed/apocryphal epigraphs (the
   Einstein/Cameron duplicate, the apocryphal Einstein and Keynes lines), claims with better data
   available (antibiotic-resistance deaths: lead with the 2019 Lancet 1.27M, label the O'Neill
   "10M by 2050" projection as contested), order-of-magnitude figures to label as estimates (Borlaug
   "1 billion," "$8T cybercrime," GPT-4 "50 GWh"), one likely-wrong stat to verify ("4.8B COVID
   shares in 48h"), weak anchor anecdotes (Delhi cobra historicity), and a "already well-sourced —
   don't bother" list (leaded-petrol 824M IQ → PNAS 2022; false-news 6× → Science 2018; CDC YRBS).

## NOT done — requires you / a professional
- The verification itself (needs sources/network).
- Adding numbered endnotes/citations in the PDF generator — deferred on purpose: the citation
  apparatus should be **populated with confirmed sources**, so it belongs *after* the fact-check, not
  before. Building an empty footnote system now would be busywork. (When sources are in hand, I can
  add an endnotes flowable + a "Notes & Sources" back-matter section to `generate_book.py` quickly.)
- Resolving the math paper's peer-review status (author decision).
- Applying the epigraph/figure fixes from KNOWN_ISSUES (need confirmation; epigraphs are authorial).

## Recommended next action for you
Hand `claims_triage.csv` + `KNOWN_ISSUES.md` to a fact-checker (or work the STAT rows yourself). Once
the priority claims have confirmed sources, I'll build the citation apparatus and wire the endnotes.
