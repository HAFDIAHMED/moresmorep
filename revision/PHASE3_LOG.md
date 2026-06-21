# Phase 3 — Intellectual Integrity (log)

Goal: make the book survive a hostile expert review by stating its own limits and the strongest
case against it. This is the highest-leverage pass for publishability — Phase 1 stopped the
overclaiming; Phase 3 makes the argument honest and self-aware.

## Done ✅

### 1. New chapter — "The Case Against This Book" (Chapter 14, ~1,690 words)
`book_chapters_10to13_reader.py` (`chapter14`), wired into `book_main_reader.py` after Ch13.
A genuinely adversarial chapter that steelmans six objections and concedes what each fairly takes:
1. **Selection bias** — "you went looking for cascades" (concede: the case studies illustrate, they
   don't prove; the structural argument carries the weight).
2. **The ledger is overwhelmingly positive** (concede: net progress is real; the quarrel is only
   with single-entry bookkeeping that omits the cascade).
3. **Unfalsifiability** (answer: states explicit refutation conditions; calls out the
   "too recent / contained" dodge).
4. **Cascade thinking can do harm** — status-quo bias / weaponisation by incumbents (concede it's
   the gravest risk; insist on symmetry — inaction cascades too).
5. **The numbers are theatre** — CRI false precision (concede: it's a checklist, not a measurement).
6. **None of this is new** — Merton/Tenner/Perrow/Taleb (concede priority; claim only synthesis).
Closes with "What Survives": the narrower, defensible book, plus a callout — *not 'every solution is
a mistake' but 'every solution is an incomplete ledger.'*

### 2. Falsifiability statement (Introduction)
Added an explicit "this is what would refute the claim" paragraph in "Why This Book Is Different",
pointing forward to Chapter 14. The thesis can now lose: a domain that grows more interconnected for
decades yet shows a flat/falling rate of interaction-problems, or a problem-to-solution ratio
unrelated to connectivity, would refute it.

### 3. CRI honesty fix (Chapter 11)
Folded a caveat into the CRI's opening definition: it is **not a validated instrument**, has **not
been tested prospectively**, every worked score is a **retrospective illustration computed with the
outcome already known**, and a real test would be prospective. Kills the false two-decimal precision
at the source (reinforced by Objection 5 in Ch14).

### 4. Map of the Book updated to include Chapter 14.

## Verification
- All edited modules + `book_main_reader.py` pass `py_compile`; `chapter14` confirmed defined and wired.
- Net words: 127,903 → **129,836** (Phase 3 adds integrity content by design).
- PDF render still pending (no matplotlib in sandbox) — build in your environment to see Ch14 typeset.

## Gate 3 status
**Substantially met:** a hostile reviewer can now find, in the book itself, (a) a falsifiability
statement, (b) a full adversarial chapter, and (c) an explicit disavowal of the CRI's false
precision — alongside the pre-existing "Limitations of the Cascade Risk Index" section in Ch11.

## Remaining (author judgment)
- Optionally deepen the treatment of genuine counterexamples (e.g., argue the Montreal Protocol as a
  partial *refutation* of inevitability, not merely an instance of "cascade-aware design").
- Author read-through + approval; render `v23+`.
