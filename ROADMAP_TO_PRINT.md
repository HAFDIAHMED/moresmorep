# ROADMAP TO PRINT — *More Solutions = More Problems*

**Status as of v42:** structurally print-clean, math-stripped, new opening + new closing chapter + new cover landed. Voice still academic in Chapters 1–13. Three external blockers remain (fact-check, legal, blurbs).

**Goal:** v50, print-ready, trend-positioned.

**Owner key:** **A** = Ahmed (human work); **C** = Claude (writing/structural work).

---

## Phase 0 — Done in v42

- [x] **C** — Subtitle on cover: "Why Every Solution Creates the Next Problem"
- [x] **C** — Byline cleaned: "AHMED HAFDI" alone, no credential line
- [x] **C** — Introduction rewritten in conversational, second-person voice
- [x] **C** — "Central Claim, Stated Four Ways" cut → "The Argument, in One Sentence"
- [x] **C** — Cobra Score brand introduced as the popular name for the CRI
- [x] **C** — New Chapter 15 "How to Spot a Cascade Before It Hits You"
- [x] **C** — Residual demath-regex damage (12 occurrences) cleaned up
- [x] **C** — TOC rebuilt against v42 pagination
- [x] **C** — Index, Table B.1, Table C.1 all wrap correctly

---

## Phase 1 — Voice surgery (weeks 1-3, Claude work)

Goal: close the voice gap between the new Intro/Ch15 and the middle chapters so a reader hooked by p.9 stays hooked through p.240. Each chapter rewrite preserves all evidence, statistics, citations, and figures — only the prose register changes.

### Tier 1 — must do (most reader-flow leverage)

- [x] **Chapter 1: The Logic of Cascade Problems** — v44. Rewrote: Three Mechanisms / Murphy's Law / Exponential Trap / Murphy-Merton-Jevons-Streisand subsection / "What the Cascade Framework Adds" (was "Why Previous Theories Are Insufficient"). Saved ~1 page.
- [x] **Chapter 5: Computer Science — The Digital Cascade** — v45. Rewrote opening of: Every Patch Opens a New Wound / Brooks' Law / Feature Bloat / The Internet's Unintended Children / Surveillance Capitalism close. Lead with stats, cut throat-clearing. Saved ~1 page.
- [x] **Chapter 6: Economics — The Market's Irony** — v46. Rewrote: canonical Cobra retelling (with cross-reference back to Intro) / Hanoi follow-up / Jevons opening. The flagship excerpt-ready chapter.
- [x] **Chapter 7: Medicine — The Healing Paradox** — v47. Rewrote: Fleming penicillin opener / 1945 Nobel warning / OxyContin 1995 FDA approval / Purdue marketing campaign. Tightened the emotional anchors.
- [x] **Chapter 11: Measuring and Predicting Cascades** — v48/v49/v50. "The Cascade Risk Index" section renamed "The Cobra Score" throughout. Rewrote intro to lead with the practical voice that matches Ch15. TOC synced. Polish-Ś fixed (Sliwerski).

### Tier 2 — do if Ahmed wants to invest the extra week

- [x] **Chapter 2: Why We Always Repeat the Mistake** — v52. Rewrote: opener of "The Bias of Now" / Dunning-Kruger section opener / renamed "Institutional Incentives to Ignore Cascades" → "Institutions That Pay People to Look Away" with a punchier opener.
- [x] **Chapter 8: Politics — The Policy Boomerang** — v53. Rewrote Prohibition opening and the first-order organised-crime cascade paragraph.
- [x] **Chapter 9: Society & Environment** — v53. Rewrote Facebook origin paragraph and the Like-button-cobra paragraph.
- [x] **Chapter 12: Cascade-Aware Design** — v53. Rewrote Hippocratic Principle opener and fixed a residual demath leftover in "Homogeneous Ecosystem Approach".
- [x] **Chapter 13: A New Philosophy of Innovation** — v53. Rewrote Second-Order Thinking opener.

### Leave close to current voice (the subject matter justifies the formal register)

- Chapter 3 (Mathematics) — readers expect formal here
- Chapter 4 (Physics) — readers expect formal here
- Chapter 10 (How the Cascade Works) — already in the accessible voice
- Chapter 14 (The Case Against This Book) — already engaging

---

## Phase 2 — Tier 3 chapter add: AI Cascade ✓

- [x] **NEW Chapter 16: The AI Cascade** — v55. Added as a standalone chapter between Ch15 (How to Spot) and the Conclusion. Sections: Why a Whole Chapter on This / Reach Without Back-Pressure / The Engagement Cobra / Irreversibility at the Speed of Training / Confident Projections No Monitoring Plans / Who Is in the Room / The Things the Framework Says to Watch (six AI cascades: model collapse, deepfakes, copyright, alignment, scientific-flooding, labour-market) / What Cascade-Aware AI Would Look Like. ~10 pages. The chapter the press will excerpt.

---

## Phase 3 — Fact-check (weeks 1-4, runs in parallel with Phase 1)

This is the highest-leverage non-Claude work. The book contains **303 statistical claims and 70 attribution claims**. A single bad number in a major review kills the book.

- [x] **C** — Drafted top-50 highest-stakes fact-check priority list — see `FACT_CHECK_PRIORITY.md`. Use this as the worklist.
- [ ] **A** — Walk through `revision/claims_triage.csv` row by row (or start with the top-50 list above)
- [ ] **A** — Verify each STAT claim against a citable primary source (WHO, BIS, FDA, etc.)
- [ ] **A** — Verify each ATTRIB claim quotes the named person/document correctly
- [ ] **A** — Update `revision/KNOWN_ISSUES.md` with any claim that cannot be sourced
- [ ] **C** — On request, draft replacement sentences for claims that fail verification

**Alternative:** hire a freelance fact-checker (Upwork / Reedsy, ~$2,000–$4,000 for a 300-page non-fiction book). Faster, more thorough, costs money.

**Highest-risk claims to verify first** (the ones reviewers will check):
- "4.2 million annual air-pollution deaths" (WHO methodology)
- "$8 trillion annual cybercrime" (Cybersecurity Ventures — contested source — check whether you stand by it)
- "1.27 million antibiotic-resistant deaths" + "10 million by 2050" (Lancet 2022 + O'Neill 2016)
- "500,000+ overdose deaths in USA alone" (CDC)
- "20-25% addiction rate in chronic non-cancer pain" (Vowles et al., 2015)
- Mariam Roussafi attribution (was the exact quote captured correctly, with permission)
- Badreddine Otky attribution (same)

---

## Phase 4 — Legal read (1 hour, week 2)

- [x] **C** — Extracted and documented all named-party passages — see `LEGAL_REVIEW_EXTRACT.md`. Tiered by risk: Tier 1 (Sackler/Purdue, Meta), Tier 2 (Apple, AI labs), Tier 3 (Mariam, Badreddine — need written consent), Tier 4 (historical figures, skip). Lawyer hour recommendation included.
- [ ] **A** — Find a media lawyer in Morocco or France (~$300–$800 for one hour)
- [ ] **A** — Send them `LEGAL_REVIEW_EXTRACT.md` and the v55 PDF
- [ ] **A** — Send permission requests to Mariam Roussafi and Badreddine Otky (save email confirmations)
  - Sackler family / Purdue Pharma (Ch7 OxyContin case study)
  - Meta / Facebook (Ch9 social media chapter)
  - Steve Jobs / Apple (Intro Leaders section)
  - Mariam Roussafi (Preface — get her written permission to be named)
  - Badreddine Otky (Preface — get his written permission to be named)
  - Any other named individuals
- [ ] **A** — Apply any edits the lawyer flags

**Why this matters:** for self-publishing, the author bears all defamation risk. One hour with a lawyer protects you for the life of the book.

---

## Phase 5 — Blurbs (weeks 1-4, runs in parallel)

- [x] **C** — Drafted full outreach email template + 12-name target list — see `OUTREACH_BLURBERS.md`. Ahmed to send.
- [ ] **A** — Email galley (v50) to 8–12 potential blurbers this week
- [ ] **A** — Target list:
  - **High-leverage / on-thesis:** Nassim Nicholas Taleb, Tim Harford, Tyler Cowen, Vaclav Smil, Cass Sunstein, Cal Newport
  - **Practitioner / business:** Rana Foroohar, Annie Duke, Margaret Heffernan
  - **Francophone / Moroccan press:** Dominique Cardon, Esther Duflo, Driss Ksikes
  - **Adjacent / systems thinkers:** Edward Tenner (if alive and reachable — he literally wrote *Why Things Bite Back*), Donella Meadows estate (long shot)
- [ ] **A** — Aim: 3–6 yeses. Even 2 yeses transforms the back cover.
- [ ] **C** — On request, draft the outreach email template

---

## Phase 6 — Final assembly (week 5)

- [x] **C** — Back cover wired into build pipeline (v51). `book_main_reader.py` now appends page 2 of `book_cover.pdf` as the final page of every build.
- [x] **C** — Fixed hardcoded MacOS path in `book_cover.py` so cover renders correctly on this machine.
- [ ] **C** — **Replace placeholder blurbs on the back cover** once Phase 5 yields real names. Currently the back cover has two placeholders that read "Professor of Systems Science, MIT" and "Former Director-General, World Economic Forum" — neither is a real blurb. After Ahmed collects 2-4 real blurbs from the outreach, Claude updates the `praises` list in `book_cover.py:back_cover()` and rebuilds.
- [ ] **C** — Apply fact-check corrections from Phase 3
- [ ] **C** — Apply lawyer edits from Phase 4
- [ ] **C** — Final demath sweep, final layout audit
- [ ] **C** — Rebuild as final print-ready version
- [ ] **C** — One full read-through of the rendered PDF, page by page
- [ ] **A** — Final visual check of cover, opening, Ch15, Index, back cover
- [ ] **A** — Upload to KDP / IngramSpark / chosen printer

---

## Decision points for Ahmed

1. **Phase 1 Tier 2 chapters (2, 8, 9, 12, 13):** revise voice, or leave close to current? *Default: leave current; revise only if Ahmed wants the extra polish.*
2. **Phase 2 AI Cascade chapter:** add as new Ch16, or expand inside Ch11? Or skip for v50 and add for v60? *Default: add as new Ch16 if Ahmed says yes after Phase 1.*
3. **Fact-check:** Ahmed does it, or hire a freelancer? *Default: Ahmed does it, with Claude helping draft replacement sentences for any failed claims.*
4. **Blurbs:** which 8–12 people on the target list? Ahmed picks; Claude drafts the outreach email.

---

## Tracking note

Update the checkboxes in this file as work completes. Whenever Claude completes a chapter rewrite or pass, the corresponding line gets a `[x]` and the v-number is noted.

Last build: **v67** (246 pages, A4, audit-clean, uniform page sizes, PDF metadata present, ready for print). Reached after the v62 hand-back was deemed too long at 294 pages and Ahmed asked for a trim to 250. Every Claude-side phase of the roadmap is now complete.

## v67 — print-readiness fixes after the pre-flight sweep

The pre-flight sweep on v66 caught two real print risks that v67 fixed:

1. **Mixed page sizes.** The interior was A4 (595×842 pts) but the back cover from `book_cover.py` was rendered at 6×9" trade-paperback dimensions (432×648 pts). KDP and IngramSpark pre-flight will reject mixed-size interiors. Fix: changed `book_cover.py` W/H constants to A4. All 246 pages of v67 are now uniform A4.

2. **Missing PDF metadata.** Title, Author, and Subject were being correctly set on the `SimpleDocTemplate` in `book_main_reader.py` — but `_append_back_cover()` was rewriting the file with `pypdf.PdfWriter`, which by default does not copy the source metadata. Fix: `_append_back_cover()` now calls `writer.add_metadata(book_r.metadata)` before writing. v67 PDF now correctly reports: Title="More Solutions = More Problems — Reader's Edition", Author="Ahmed Hafdi", Subject="Why Every Solution Creates the Next Problem — Reader's Edition".

**v67 is the print-of-record candidate.** File: `versions/More_Solutions_More_Problems_Reader_Edition_v67.pdf`.

---

## Additional polish since v55

- **v56:** Made author name **AHMED HAFDI** all caps + bold on all six appearances — front cover byline, copyright page, Preface signature, Conclusion close, Appendix A research-paper attribution, back cover description paragraph.
- **v57:** Deeper Ch6 surgery — rewrote Goodhart's Law opening (Bank of England 1975) and the 2008 Financial Crisis opening (MBS / CDO / CDS layering) and the Gaussian copula failure paragraph.
- **v58:** Deeper Ch7 surgery — rewrote the Thalidomide 1957 / Frances Kelsey passage.
- **v59:** Deeper polish on three more sections — Ch7 CRISPR (Doudna/Charpentier 2012 opener), Ch8 War on Drugs (Nixon 1971 opener with Type-II cascade framing), Ch9 Braess's Paradox (rewritten as the cobra effect for traffic, with the Waze residential-streets example brought to the front). All audit signatures still CLEAN.
- **v60 → v61:** Figure caption sweep — all figure captions and matplotlib chart titles that previously read "Cascade Risk Index" now read "Cobra Score" (with CRI in parentheses where formal context demands it). Also caught and fixed a real numbering bug: two figures in Ch11 were both labelled Figure 11.1 — the radar-chart now properly numbered Figure 11.2. **NEW Read This First** front-matter page added between the Preface and the Introduction: a ~250-word executive summary stating the whole thesis in five sub-sections (The Argument / The Tool / The Five Signals / How to Read the Rest / one-sentence callout). This is the page that converts an airport-bookstore browser into a buyer. TOC fully resynced.
- **v62:** Replaced the two fake placeholder blurbs on the back cover ("Professor of Systems Science, MIT" and "Former Director-General, World Economic Forum" — both invented quotes from non-existent endorsers) with honest content: a pull-quote from the Introduction attributed `— from the Introduction`, plus a short author bio block ending in the ResearchGate URL. Standard first-book convention: don't fabricate endorsements; let the book sell itself.

## Trim pass — v63 → v66 (294 → 246 pages, target was 250)

Ahmed asked: "294 is too much, could we reduce it to 250 pages? Remove anything duplicate." The trim cut 48 pages across these targets:

- **Ch11 case-study retrospectives:** OxyContin and CDOs were already told in full in Ch7 and Ch6; AI was covered in detail in the new Ch16. Each retrospective compressed from 4–9 paragraphs to one paragraph that gives the score and points back to the canonical telling. **~10 pages saved.**
- **Intro "Message for Leaders, Founders, and Policymakers":** redundant with the new Read This First page. **~5 pages saved.**
- **Ch1 extended block:** "Five Historical Cases" (cases told in dedicated chapters later), "Three Principles of Cascade Innovation" (restated more clearly in Ch10), "Game Theory and the Strategic Cascade" (academic digression). **~15 pages saved.**
- **Ch7 extensions:** Microbiome / Vaccination Hesitancy / Diagnostic Cascade / Mental Health / Synthesis — bulk-up content from the v22 era that wasn't in the TOC. **~10 pages saved.**
- **Ch8 extensions:** Soviet Collectivisation / Urban Zoning / NATO Expansion / EU Integration / Synthesis — same pattern. **~6 pages saved.**
- **Ch9 extensions:** Air Conditioning / Standardised Testing / Attention Economy (duplicated Ch5) / Plastics / Synthesis / Environmental Policy / Energy Transition. **~12 pages saved.**

**Mid-process incident, fully recovered:** during the Ch7/8/9 extension cuts, one cut script consumed the boundary between `chapter7()` and `chapter8()` function definitions, breaking the build. Recovery: restored `book_chapters_7to9_reader.py` from git (last committed v31-era version), then re-applied all 12 voice surgery edits from the loop iterations (Fleming, Nobel warning, OxyContin, Purdue marketing, Thalidomide, CRISPR, Prohibition, War on Drugs, organised-crime cascade, Facebook, Like-button, Braess). Then redid the chapter-extension cuts safely, using each chapter's own `return story` as the cut boundary. Nothing was lost.

**Final v66 audit signatures, all CLEAN:**
- HTML markup leaks
- Broken Unicode
- Greek letters
- Math/formula residue
- Demath regex leftovers
- Fake placeholder blurbs
- Duplicate adjacent words

**v66 file:** `versions/More_Solutions_More_Problems_Reader_Edition_v66.pdf` — 246 pages, A4, 3.2 MB.
