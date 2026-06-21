# Phase 0 — Baseline & Findings

Status: **complete**. Establishes the measurable starting point for the revision.

## What was done
- Tagged the pre-revision build as **`v22-baseline`** (git tag).
- Opened branch **`revision-2.0`** for all revision work.
- Built `revision/phase0_analyze.py` (stdlib-only AST parser).
- Generated **`revision/inventory.md`** — per-chapter word counts + structural map.
- Generated **`revision/claims_register.csv`** — fact-check worklist (Excel-ready).

## Headline numbers
- **Total prose: ~142,808 words.** A typical trade-nonfiction target is 75–90k. The manuscript is roughly **1.6–1.9× too long** — this quantifies the Phase 2 cut. A 40% reduction lands at ~86k, squarely on target.
- **17 chapter units** (preface → appendices).
- **26 epigraphs**, **~1,221 candidate quantitative claims** flagged for verification.

## Biggest chapters (cut targets)
| Chapter fn | Words |
|---|--:|
| `chapter9` (Social/Ecological) | 15,035 |
| `chapter6` (Economics) | 13,165 |
| `chapter5` (Computer Science) | 11,556 |
| `chapter7` (Medicine) | 11,080 |
| `chapter11` (Measuring/CRI) | 10,649 |
| `chapter4` (Physics) | 10,463 |
| `appendices` | 9,504 |
| `chapter8` (Politics) | 9,094 |
| `chapter1` (Theory) | 8,915 |

The seven evidence chapters (3–9) total **~72,700 words** — over half the book. This is where de-duplication and merging will recover the most length.

## Concrete defects already surfaced
- **Self-contradicting attribution:** the epigraph *"Not everything that can be counted counts…"* appears **twice** — attributed to **Einstein** (Ch 6) and to **William Bruce Cameron** (Ch 11). (Cameron is the correct origin.) The book contradicts itself.
- **Multiple epigraphs already self-flagged as unreliable:** "Attributed variously" (statesman/Clarke), "Attributed to Albert Einstein," "Attributed to John Maynard Keynes," Saint-Exupéry "(origin disputed)," Hippocrates "absent from his actual writings." These should be sourced or cut, not printed with a disclaimer.
- **Theorem boxes:** the "Three Laws of Cascade Innovation" (Ch 1) are formatted as `theorem_box` — the exact framing Phase 1 must demote from "law/theorem" to "principle."

## How to use the artifacts
- **`claims_register.csv`** — the Phase 4 worklist. Columns `verdict / source / notes` are blank TODOs. Triage each row: `OK` (sourced), `FIX` (wrong/needs softening), `CUT`, or `N/A` (false positive — cross-references like "Chapters 1, 10, 11" are over-captured by design; better a superset than a gap).
- **`inventory.md`** — the Phase 2 map. Use the structural section list to spot duplicate case studies across chapters (opioids, 2008, antibiotics, cobra) for consolidation.

## Next
Proceed to **Phase 1 — Reframe the thesis** (vocabulary demotion + honest doubling argument + de-grandiosing) and the Phase 2 map reconciliation in the Introduction. Lowest-risk, highest-visibility step; rebuilds as `v23`.
