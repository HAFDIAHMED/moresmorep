# Publication Roadmap — *More Solutions = More Problems*

**Goal:** Take the manuscript from "strong idea, unpublishable execution" to a globally publishable trade-nonfiction title.
**Current state (expert assessment):** C+ / "revise and resubmit." The pattern is real and valuable; the framing as a proven mathematical *law* is the fatal flaw, compounded by bloat, weak sourcing, unfalsifiability, and structural inconsistency.
**Target state:** ~75–90k words. An honest, well-sourced "pattern + toolkit" book that engages its own critics. B+/A- trade title.

Legend — **[AI]** I can execute in the source/PDF • **[Author]** needs you/domain judgment • **[Pro]** needs a hired specialist (fact-checker, copyeditor, lawyer, peer reviewers)

---

## STATUS (revision 2.0, branch `revision-2.0`) — see `revision/REVISION_SUMMARY.md`
- **Phase 0 — Baseline:** ✅ done (143,008-word baseline; `v22-baseline` tag).
- **Phase 1 — Reframe/de-overclaim:** ✅ done. Zero self-overclaim phrases remain.
- **Phase 2 — Structural cut:** ✅ dedupe done (−10.6% → ~128k); −40% target retired (deeper trim → copyedit).
- **Phase 3 — Integrity:** ✅ done. New Ch14 "The Case Against This Book" + falsifiability + CRI honesty caveat.
- **Phase 4 — Sourcing:** ✅ triage done (`claims_triage.csv`, `KNOWN_ISSUES.md`); **verification ⏳ [fact-checker]**.
- **Phase 5 — Polish:** ✅ figures (clean vs sketch) done; **copyedit + legal ⏳ [Pro]**.
- **Phase 6 — Review/publish:** ⏳ **[Author/Pro]** — needs the PDF render, expert/beta reads, and the publishing decision. Handoff kit in `revision/handoff/`.

**The AI-executable work across Phases 0–5 is complete and pushed.** Remaining items are
render + human/professional review (see the status table in `revision/REVISION_SUMMARY.md`).

---

## Phase 0 — Setup & baseline (0.5 week)
*Make the work measurable and reversible.*

- [ ] **[AI]** Freeze current build as `v22` baseline; tag it. Establish a clean git branch `revision-2.0`.
- [ ] **[AI]** Generate a word-count + section inventory across all chapter modules (per-chapter word counts, list of every section/callout/theorem_box/figure).
- [ ] **[AI]** Build a "claims register" — extract every quantitative claim, named attribution, and epigraph into a spreadsheet for the later fact-check pass.
- [ ] **[Author]** Confirm target length, audience (general trade vs. business/policy), and whether the ResearchGate paper will be pursued for peer review (gates Phase 4).

**Gate 0:** Baseline tagged, inventory + claims register exist.

---

## Phase 1 — Reframe the thesis (1 week) — *highest leverage, lowest risk*
*Removes ~80% of the reviewer attack surface without touching the evidence.*

- [ ] **[AI]** Global vocabulary demotion: "theorem," "law," "mathematically inevitable," "proven," "structurally guaranteed" → "pattern," "tendency," "strong regularity," "lens/heuristic." (Scripted, reviewed case-by-case.)
- [ ] **[AI]** Rewrite the doubling argument in Ch 1 and Ch 10 honestly: explosion of *possible* interactions + non-zero harmful fraction → problems can outrun fixes. Drop the "2ⁿ ⇒ law" leap.
- [ ] **[AI]** Rename "The Three Laws of Cascade Innovation" → "Three Principles" (or similar); rewrite their statements as empirical generalizations, not theorems.
- [ ] **[AI]** Dial back grandiosity ("most important challenge of our era," "next stage of civilisational maturity") → confident-but-humble phrasing.
- [ ] **[Author]** Approve the new framing language (one-page style sheet).

**Gate 1:** No sentence claims mathematical proof of inevitability. Rebuild `v23`, read-through.

---

## Phase 2 — Structural cut & de-pad (2–3 weeks)
*Target: −35–40% length. This is where the book gets good.*

- [ ] **[AI]** De-duplicate case studies: ONE canonical treatment each of opioids, 2008/CDOs, antibiotics, the cobra parable; everywhere else → cross-reference.
- [ ] **[AI]** Collapse the stacked "Synthesis / Extended Synthesis / Extended Synthesis II" sections to one synthesis per chapter.
- [ ] **[AI]** Strip LLM-tell prose: compulsive tricolons, "not X; Y" antithesis, repeated "first-/second-generation cascade" scaffolding.
- [ ] **[Author]** Decide which chapters merge. Recommendation: the 7 evidence domains (Ch 3–9) are too many at current length — consider merging to 5 tighter chapters, or keep 7 but cut each ~30%.
- [ ] **[AI]** Reconcile the **Introduction "Map of the Book"** with the actual chapter lineup (currently describes wrong chapters and references nonexistent ch. 12–16).

**Gate 2:** Manuscript ≤ ~90k words; no case study told twice; map matches book. Rebuild `v24`.

---

## Phase 3 — Intellectual integrity (2–3 weeks)
*Turns a sales pitch into an argument. Makes it credible to experts.*

- [ ] **[Author + AI]** Add a **falsifiability statement** early: state explicitly what evidence would refute the thesis.
- [ ] **[Author + AI]** Write a new chapter, **"The Case Against This Book"**: steelman selection/survivorship bias, net-positive innovation (vaccination, sanitation, anesthesia), and cases where the cascade frame misleads toward harmful inaction. (~5–7k words.)
- [ ] **[Author]** Stop hand-waving the counterexamples (Montreal, smallpox) as merely "cascade-aware design"; engage them as genuine partial refutations.
- [ ] **[Author + AI]** **CRI honesty fix** — choose one:
  - (a) Demote CRI to a structured pre-deployment *checklist/brainstorm*; remove precise retrospective scores (0.92, 0.95) computed on known disasters; **or**
  - (b) Run a genuine *prospective* test: compute CRI on 3–5 current solutions before outcomes are known, report methodology and limits.
- [ ] **[Author]** Add a frank "Limits of This Framework" section (partly exists in Ch 11 — strengthen it).

**Gate 3:** A hostile expert reviewer can find the book's own statement of its limits and counterarguments. Rebuild `v25`.

---

## Phase 4 — Evidence & sourcing (3–5 weeks) — *the slow, unavoidable pass*
*A serious-idea book with no in-body sourcing is not publishable in 2026.*

- [ ] **[Pro/Author]** Fact-check every entry in the claims register. Flag: wrong, unverifiable, apocryphal.
- [ ] **[Author + AI]** Add numbered endnotes or inline citations for every statistic and causal/blame claim.
- [ ] **[Author]** Fix or cut dubious anchors: the Delhi cobra bounty's historicity, "824M IQ points," "saved a billion lives," "$22 trillion," etc. Replace misattributed/"origin disputed" epigraphs with sourced ones (or cut).
- [ ] **[Author]** Resolve the math's status: pursue peer review of the ResearchGate paper **or** remove all appeals to its authority. (Decision from Gate 0.)
- [ ] **[AI]** Build the endnotes/bibliography apparatus in the PDF generator (new flowable styles + back-matter).

**Gate 4:** Every body claim is sourced or cut. No reliance on an unreviewed paper's authority. Rebuild `v26`.

---

## Phase 5 — Production polish (2–3 weeks)
- [ ] **[AI]** Replace data-bearing xkcd-sketch figures with clean, properly-labeled charts; keep sketch style only for conceptual diagrams. Remove the "illustrative data" ambiguity.
- [ ] **[AI]** Tighten title/subtitle/cover claim to match the honest framing.
- [ ] **[Pro]** Professional copyedit (line + consistency).
- [ ] **[Pro]** Legal read — every named living person/company in a blame context (Sacklers, Purdue, Meta, named researchers) must be sourced and phrased defensibly.
- [ ] **[AI]** Front/back matter: acknowledgments, about-the-author, index regeneration, ISBN/colophon page.

**Gate 5:** Camera-ready. Rebuild `v27` = release candidate.

---

## Phase 6 — Pre-publication validation (2–4 weeks, parallelizable)
- [ ] **[Author]** Send the RC to 3–5 expert readers across the domains it touches (a mathematician, an economist, a physician, a historian/STS scholar). Require sign-off that the claims in their field are defensible.
- [ ] **[Author]** Beta-read with 5–10 general readers for clarity/engagement.
- [ ] **[Author]** Incorporate feedback → `v28` final.
- [ ] **[Author/Pro]** Decide channel: query agents/publishers (the credibility fixes make this viable) **or** professional self-publish.

**Gate 6:** Expert sign-offs in hand. Ready to publish worldwide.

---

## Critical path & sequencing

```
Phase 0 → Phase 1 → Phase 2 → Phase 3 ─┐
                                       ├→ Phase 5 → Phase 6
              Phase 4 (start after 2) ─┘
```
- Phases 1→2→3 are sequential (each assumes the prior framing).
- Phase 4 (fact-check) can start once Phase 2 stops moving text around.
- Phase 6 expert reads can overlap Phase 5 polish.

## Rough timeline
- **Aggressive (full-time author + paid pros):** ~10–12 weeks.
- **Realistic (part-time):** ~4–6 months.
- The two long poles are **Phase 4 (sourcing)** and **Phase 2 (the cut)** — neither can be skipped.

## Effort split
- **[AI] can do now, fast:** Phase 0, most of Phase 1, the mechanical 60% of Phase 2, the map fix, figure/typography work, the citations apparatus.
- **[Author] judgment required:** chapter merges, the adversarial chapter, CRI decision, which claims to defend vs. cut, peer-review decision.
- **[Pro] must hire:** fact-checker, copyeditor, IP/defamation lawyer, expert readers.

## The one-line test for "ready"
The book no longer says *"I proved a law of progress."* It says *"Here is a striking, well-sourced pattern, the best cases for and against it, and a practical way to spot it early."* When that sentence is true, it's ready.

---

### Suggested immediate start
Phase 0 + Phase 1.1 (vocabulary demotion) + Phase 2 map fix → rebuild `v23`. Lowest risk, instantly visible improvement, and it de-risks everything downstream.
