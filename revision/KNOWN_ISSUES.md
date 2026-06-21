# Phase 4 — Known Issues (curated pre-fact-check flags)

**Scope/honesty note:** I have no live sources in this environment, so this is *not* the fact-check —
it is an expert triage from training knowledge. Every "FIX/CONTESTED" item below should be confirmed
by a fact-checker before the change is finalised. But these are the claims most likely to embarrass
the book, plus a short list of claims that are *already* well-sourced so the checker doesn't waste
time on them.

Work order: do **A** (misattributions — cheap, high-embarrassment), then **B** (better data exists),
then **C** (label as estimates), then **D** (verify hard), then **E** (weak anecdotes).

---

## A. Misattributed / apocryphal epigraphs — FIX
1. **"Not everything that can be counted counts…"** appears **twice** — attributed to **Einstein**
   (Ch6, inline) and to **William Bruce Cameron** (Ch11). Cameron, *Informal Sociology* (1963), is
   the correct source; the Einstein attribution is false. **Fix:** correct the Ch6 attribution to
   Cameron *and* drop one of the two (same quote twice is itself a defect) — or replace the Ch6 one.
2. **"The measure of intelligence is the ability to change."** (Ch13 epigraph) — attributed to
   Einstein; **apocryphal**, no documented Einstein source. Replace with a sourced line or cut.
3. **"When the facts change, I change my mind…"** (Ch11, attributed Keynes) — **likely apocryphal**;
   no contemporaneous Keynes source exists. Keep only with an explicit "attributed" hedge, or replace.
4. **"We do not inherit the earth from our ancestors; we borrow it from our children."** (Ch9,
   Saint-Exupéry, already flagged "origin disputed") — genuinely unverified; commonly mis-sourced.
   Fine to keep with the hedge, better to cut.
5. **"If the product is free, you are the product"** (Ch9, attributed Serra/Schoolman 1973) — the
   *idea* traces to their 1973 video "Television Delivers People"; this exact wording is modern.
   Re-word the attribution to "after Richard Serra…" or similar.
6. **"First, do no harm"** (Ch12) — correctly already flagged as absent from the Hippocratic corpus. OK.

## B. Better-sourced numbers exist — RE-FIGURE
7. **Antibiotic resistance deaths.** The book leads with **"700,000/year"** (older O'Neill-era
   figure). The current best estimate is **1.27 million deaths directly attributable and 4.95 million
   associated (2019)** — Murray et al., *The Lancet* GRAM study (2022). **Fix:** lead with 1.27M
   (2019, Lancet).
8. **"10 million deaths/year by 2050."** This is the **O'Neill Review (2016) projection** and is
   **widely criticised as speculative** (extrapolated, contested methodology). Keep only if labelled
   as a contested projection, not a fact.

## C. Order-of-magnitude estimates presented as facts — LABEL AS ESTIMATES
9. **Borlaug "saved ~1 billion lives."** Popular attribution; unverifiable. Phrase as "credited with
   helping avert famine for hundreds of millions," or label as an estimate.
10. **"200 million lives saved by antibiotics."** Order-of-magnitude estimate, no rigorous source. Label.
11. **Cybercrime "$8 trillion (2023)… $10.5T by 2025."** These are **Cybersecurity Ventures** figures
    — widely cited, methodology opaque/disputed. Attribute explicitly and call them industry estimates.
12. **"Training GPT-4 consumed ~50 GWh / 4,500 households."** Third-party estimate; never disclosed by
    OpenAI. Label as an external estimate.
13. **Bitcoin "~130 TWh/yr ≈ Argentina."** Roughly tracks the Cambridge CBECI but the figure swings;
    cite CBECI and give a range/date.

## D. Looks wrong / verify hard — CHECK
14. **COVID "vaccine-microchip claim: 4.8 billion shares by March 2021, in 48 hours."** This specific
    number looks **implausible/unsourced** (4.8B shares would dwarf total platform volume). Verify or cut.
15. **"$22 trillion" (2008 crisis).** Defensible if cited to the **US GAO (2013)** cumulative-output
    estimate; confirm and attribute.
16. **Phoenix "+8°F overnight minimum since 1948."** Plausible urban-heat-island figure; confirm source.
17. **Foxconn "~350,000 workers, Zhengzhou."** Plausible at peak; confirm.

## E. Weak primary sourcing on anchor anecdotes — FLAG
18. **The Delhi cobra bounty** (the book's keystone parable). Historicity is **thin** — no strong
    primary documentation; usually traced to Siebert (2001) as illustrative. The **Hanoi rat-tail**
    bounty is the well-documented case (Michael Vann, 2003). **Recommendation:** present the cobra
    story as "the often-told (if thinly documented) parable" and rest weight on Hanoi. (Partly done
    in the revised Introduction.)
19. **Prague dog-tail bounty** — book already concedes it is "less well documented." Very weak; cut or
    explicitly caveat.

## F. Already well-sourced — DO NOT waste fact-check time
- **Leaded petrol "~824 million IQ points lost."** Real: **McFarland, Hauer & Reuben, PNAS (2022)** —
  cite it.
- **"False news spreads ~6× faster than true."** Real: **Vosoughi, Roy & Aral, *Science* (2018)** — cite.
- **Teen "persistent sadness" 36%→57% (girls, 2011→2021).** Real: **CDC Youth Risk Behavior Survey** — cite.
- **MMR/Wakefield → UK measles return; 1998 *Lancet*, retracted.** Well-documented — cite.
- **Air pollution ~4.2M deaths/yr (WHO).** Standard WHO figure — cite.

---

## What I did NOT change
I deliberately made **no edits to epigraphs or prose** in this phase: the attribution fixes need a
fact-checker's confirmation, and replacing epigraphs is an authorial-voice decision. This file +
`claims_triage.csv` are the worklist for that pass.
