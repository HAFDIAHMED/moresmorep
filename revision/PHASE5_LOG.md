# Phase 5 — Production Polish (log)

**Honest scope:** the two biggest Phase 5 items — a professional **copyedit** and a **legal read**
— are genuinely [Pro] and out of scope for me. Full visual verification of the figures needs a
render I can't do here. What I did is the named **[AI] figure task** plus the consistency fixes that
follow from it, all compile-checked and reversible.

## Done ✅ (AI-doable, compiles)
1. **Two-style figure system** (`generate_book.py`). Added a `clean_style()` context manager (sober
   serif, gridlines, no top/right spines) and switched the **quantitative charts** to it, while
   keeping `plt.xkcd()` sketch style **only for the nine conceptual diagrams** (cascade tree, Gödel
   timeline, CRI concept, CRISPR, nuclear-waste timeline, historical timeline, quantum concept map,
   2008 flow, P-vs-NP steps). This fixes the credibility problem flagged in the evaluation: real-data
   charts were being undermined by a hand-drawn "joke" aesthetic.
   - Restyled to clean: exponential cascade, antibiotic resistance, Jevons, Brooks' Law, opioid,
     prohibition, Windows complexity, social media, Goodhart, Green Revolution, drug war.
2. **Reconciled the figures disclaimer** (Introduction). The old text claimed *all* figures are
   "drawn in sketch style" — no longer true. Rewritten to describe the two styles honestly and to
   state that data charts cite their source in the caption while illustrative charts say so and must
   not be read as measurements.
3. **Consistency fix:** the Map-of-the-Book reference "Chapter 3 (Mathematics. The Original Cascade)"
   now matches the actual chapter title's em-dash punctuation.

## ⚠️ Needs your render to verify (no matplotlib here)
- Confirm the `clean_style()` charts look right and the rc keys are supported by your matplotlib
  version (they are standard; `rc_context` ignores unknowns gracefully). Build with
  `python book_main_reader.py`.

## NOT done — [Pro] / author
- **Professional copyedit** (line edits, comma-splice cleanup — the book has many; that's a human
  pass, not safe to automate book-wide).
- **Legal / defamation read** — required: the book names living people and companies in blame
  contexts (the Sacklers/Purdue, Meta, named researchers). Each such claim needs sourcing + counsel.
- **Front/back matter:** copyright/colophon page, ISBN, dedication, acknowledgements, author bio —
  deferred because the content needs you and placement needs a render. Quick to add later.
- **Cover/subtitle:** left as "A Theory of Cascade Innovation…". Defensible for a trade subtitle, but
  if you want it to match the demoted framing, change "A Theory of" → "The Hidden Logic of" (or
  similar) on the cover in `generate_book.py` and the metadata in `book_main_reader.py`. Flagged, not
  changed — it's a branding call.

## Figure overlap fix (v24)
Reported issue: in the conceptual **tree/concept diagrams**, connector arrows were drawn *through*
the node boxes, slicing across the second line of label text ("solving homeownership" → cut, "C. diff"
→ cut, "World Wide Web" → cut). Root cause: arrows start/pass inside the boxes (and were painted over
the text). Fix: draw node boxes at **`zorder=5`** and connector arrows at **`zorder=1`**, so the
solid box always covers any line segment inside it and arrows emerge cleanly from the edges. No
coordinates moved.
Figures fixed (verified by rendering each to PNG and inspecting):
- chapter files: `fig_internet_cascade_tree`, `fig_cdo_cascade`, `fig_microbiome_cascade`,
  `fig_crispr_cascade`, `fig_quantum_interpretations`, `fig_attention_economy`.
- `generate_book.py`: `fig_cascade_tree`, `fig_cascade_risk_index`.
- Checked and left alone (arrows already run in the gaps between boxes): `fig_godel_timeline`,
  `fig_p_vs_np`; data charts unaffected.
Rebuilt as **v24**.

## Net
Prose ≈ 129,869 words (figure work is code, not prose). All touched modules pass `py_compile`.
