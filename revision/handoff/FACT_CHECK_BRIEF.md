# Fact-Checker Brief — *More Solutions = More Problems* (Reader's Edition)

**Engagement:** verify the factual claims in the manuscript and supply citable sources.
**Inputs you receive:** `revision/claims_triage.csv` (the worklist) and `revision/KNOWN_ISSUES.md`
(claims already flagged as wrong/contested, plus a few already sourced).

## How to work it
1. Open `claims_triage.csv`. It is sorted by priority. Work in this order:
   - **STAT (303 rows)** — every hard number ($, %, deaths, lives, dates-with-claims). Highest risk.
   - **ATTRIB (70 rows)** — every quotation/epigraph: confirm exact wording **and** author.
   - DATE / OTHER — spot-check only.
   - NAV — ignore (navigational false positives).
2. For each STAT/ATTRIB row, fill the two empty columns:
   - **verdict:** `OK` · `FIX` (give the corrected figure/wording) · `CUT` (unverifiable) · `SOFTEN`
     (true but presented too precisely → recommend hedge).
   - **source:** a citable reference (author, title, year, page/URL). Prefer primary or
     peer-reviewed sources; flag any claim that rests only on a press release or advocacy report.
3. Apply the standing rules:
   - Any number presented to false precision that is really an estimate → `SOFTEN` + label "estimated".
   - Any causal/blame claim about a named living person or company → must have a strong source
     (this also feeds the legal review).
   - Epigraphs: if the attribution can't be confirmed to a primary source, mark `FIX` or `CUT` — do
     not keep "(attributed)" hedges.

## Already flagged (don't re-litigate; just confirm)
See `KNOWN_ISSUES.md`. Headlines: the **Einstein/Cameron** duplicate quote (Cameron is correct);
the apocryphal **Einstein "measure of intelligence"** and **Keynes "when the facts change"** lines;
lead antibiotic-resistance deaths with the **2019 Lancet 1.27M** figure (not 700k) and flag the
**O'Neill "10M by 2050"** as a contested projection; the **"4.8 billion COVID shares in 48h"** stat
looks wrong; the **Delhi cobra** anecdote is thinly sourced (lean on the documented Hanoi case).
Already well-sourced (leave): leaded-petrol 824M IQ (PNAS 2022), false-news 6× (Science 2018), CDC
YRBS teen figures, WHO air-pollution deaths.

## Deliverable back to author
The completed CSV (verdicts + sources) plus a short list of any claim you could not source at all.
Those become the master list for the citation/endnotes pass.
