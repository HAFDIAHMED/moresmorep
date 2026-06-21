# Phase 1 — Reframe the Thesis (log)

Status: **source complete; PDF render pending** (sandbox has no `matplotlib`; rebuild in an
environment with `reportlab + matplotlib + numpy + Pillow` to produce `v23`).

Goal: stop the book claiming its central idea is a *proven mathematical law*, and dial back
grandiosity — without touching the evidence. This removes the largest reviewer attack surface.

## Edits made (Reader's Edition source)

### `book_chapters_intro_reader.py`
- **First claim** ("It is mathematically inevitable…") → "a deep structural tendency"; added the
  key honest caveat that *possible* combinations double, and how many become *real* problems
  depends on the harmful fraction (argued to be non-zero).
- **Colloquial formulation** ("it is, in fact, a law: derivable from…") → "a strong and consistent
  regularity — motivated by the mathematics… and confirmed by the evidence."
- **Mathematical formulation** "the total number of problems… doubles" → "the number of *potential*
  problem-generating combinations roughly doubles"; "core mathematical fact" → "central quantitative claim."
- **"Why This Book Is Different"** — removed the "transforms a pattern into a theorem / a theorem
  cannot [be disputed]" passage; replaced with an honest statement that the aim is precision and
  testability, not placing the claim beyond dispute.
- **Map of the Book** — rewrote to (a) demote "proves the Cascade Theorem," "formal statement,"
  "illustrations of a theorem," and (b) **fix the stale structure**: correct Part III/IV, correct
  the Ch 4–9 domains (Physics/CS/Economics/Medicine/Politics/Social), and remove the phantom
  "Chapters 12–16 / three extended case studies." Now matches the actual book. *(Also a Phase 2 item.)*
- **Chapter 1 title** "The Law of Cascade Problems" → "The Logic of Cascade Problems" (updates the
  running header too, via `chapter_opener`).
- **Merton passage** "it is its mathematical proof" → "it gives that insight a concrete, quantitative form."
- **"Unique contribution"** "(1) a mathematical proof that cascade generation is exponential" →
  "(1) an explicit structural argument for why cascade generation can grow combinatorially."
- **"Three Laws of Cascade Innovation"** → **"Three Principles of Cascade Innovation."** Reframed the
  preamble (no longer "theorems derived from the mathematical structure"; now "empirical
  generalisations… open to revision"). Renamed the three boxes to "Principle," and every "First/
  Second/Third Law" + "Main Theorem" reference in the surrounding prose.
- **Complexity-theory section** "the theoretical case for cascade inevitability" → "for the
  unpredictability of cascades" (the undecidability result itself, via Rice's theorem, is left intact).

### `book_chapters_7to9_reader.py`
- Callout "**The Cascade Theorem:**" → "**The Cascade Pattern:**".

### `book_chapters_10to13_reader.py`
- **"Main Theorem"** → **"central claim"** throughout (≈11 occurrences + glossary entry).
- **Central one-line callout (Ch 10)** — removed "the formal proof of this result"; rewrote to the
  *ways problems can arise* framing + non-zero harmful fraction; "in the author's source research paper."
- **Ch 10 body** — added the possible-vs-real-problems caveat; "The answer is no." → "In the long run, no."
- **"Empirical Validation of the Main Theorem"** → **"Empirical Support for the Central Claim"**;
  "a mathematical result about the asymptotic behaviour" → "a structural argument about the long-run
  behaviour"; "the theorem predicts" → "the argument predicts"; "exactly as… predicts" → "broadly as…
  anticipates"; "data supports" → "data is consistent with."
- **"mathematically inevitable"** (Taleb section, climate-CRI callout) → "the rule rather than the
  exception" / "close to structurally unavoidable."
- **"Cascade wisdom is the next stage of civilisational maturity"** → "cascade awareness is a
  necessary next step in how we mature as problem-solvers"; "a cascade wisdom revolution" → "a shift
  toward cascade awareness."

## Verification
- All five edited modules pass `python -m py_compile`. ✅
- Grep confirms zero remaining instances of the targeted overclaim phrases. ✅
- `reportlab` and `numpy` present in sandbox; `matplotlib` absent → PDF not rendered here.
- Word count: 142,808 → **142,973** (+165). Phase 1 reframes, it does not cut — the small rise is the
  added honesty caveats minus the removed phantom-chapter text. The cut is Phase 2.

## Residual sweep (Phase 1 completion pass)
A second pass closed the deliberately-deferred items so the source side of Phase 1 is now complete:
- Softened the book's *own* "grows exponentially / problems multiply / exponential growth is
  catastrophic" assertions to combinatorial / compounding / "near-doubling of *possible*
  interactions" language — while **leaving legitimate technical uses intact** (NP-completeness,
  EXPTIME, quantum inefficiency, scientific-literature doubling, state-space explosion, resistance
  evolution).
- "The Exponential Trap" body, the Murphy's-Law passages, the Merton/complexity-theory comparisons,
  and the Conclusion's "single mathematical fact… grows exponentially" all reframed.
- Demoted every remaining lowercase **"cascade theorem"** → **"cascade framework"** (incl. two that
  had escaped because "cascade" and "theorem" sat on different source lines), and the stray
  **"network amplification theorem"** → "network-amplification mechanism".
- Removed dangling numbered-theorem pointers that no longer exist in the Reader's Edition:
  "Theorem 1 and 2" → "the first two principles", "Chapter 10's Theorem 2" → "central claim",
  "Theorem 5" monitoring references → "the frequency the framework recommends" / "adequate
  monitoring frequency", and "theorem statements in Chapters 10 and 11" → "statements of the central
  claims".
- "as a mathematical certainty" → "as a structural tendency"; "this mathematical fact" (the
  incompressibility limit) → "this limit".
- **Left intact (legitimately):** Gödel/Rice/Bell/Nash/Carnot/virial/Ricardo/Shannon theorems, the
  `theorem_box` flowable, the Cook (1971) citation, and the Appendix A / Preface pointers that
  honestly attribute the formal proofs to the source research paper (incl. its named results in the
  back-matter index).

Final audit grep: **zero** remaining instances of the book presenting its *own* claim as a proven
law/theorem/mathematical certainty/inevitability. Word count after both passes: **143,008**
(reframing is roughly length-neutral; the cut is Phase 2).

## Deliberately left for later
- The **standard (non-reader) edition** (`book_chapters_*.py`, no `_reader`) was *not* touched — it is
  a separate build and should get the same reframe before it ships.
- Author read-through + approval of the new framing, and the **`v23` PDF render** (needs an
  environment with `matplotlib`), remain to close Gate 1.

## Next
Phase 2 — structural cut & de-pad (target −35–40%, ~86k words). The map is already reconciled.
