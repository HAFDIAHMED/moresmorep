# Fact-Check Priority List — Top 50 Highest-Stakes Claims

**Source file:** `versions/More_Solutions_More_Problems_Reader_Edition_v67.pdf` (246 pages, A4)

These are the claims a reviewer at the *Economist*, *NYT Book Review*, *Atlantic*, or a hostile podcast would check first. If any one of them is wrong, the book's credibility shifts from "rigorous" to "rigorous-but-sloppy" — and most reviewers stop reading there.

**Note on page numbers below:** the printed-page numbers shifted after the v66 trim. The references below were generated against v55 (294 pages). Most claims are now ~30–50 printed pages earlier than the references say. To find the actual passage, search the v66 PDF for a phrase from the claim rather than going to the listed page.

**Process:**
1. For each claim below, find the **primary** source (not a secondary report citing a primary source).
2. Verify the number and the citation match.
3. Mark ✅ confirmed, ⚠️ off-by-some, or ❌ does not check out.
4. For ⚠️ and ❌ cases, decide: update the number, weaken the language, or drop the claim.
5. Claude can draft replacement sentences on request.

---

## Tier 1 — globally cited numbers (every reviewer will check)

| # | Claim | Source claimed | Page | Verify |
|---|---|---|---|---|
| 1 | "4.2 million annual air-pollution deaths" | WHO, 2023 | Intro p.10 | WHO ambient air quality factsheet — verify current methodology and number |
| 2 | "$8 trillion annual cybercrime cost" | Cybersecurity Ventures, 2023 | Intro p.10, Ch5 | This is a contested industry estimate. Decide if you stand by it or use a more conservative source (e.g., Anderson et al., academic) |
| 3 | "1.27 million annual antibiotic-resistant deaths" | Murray et al. *Lancet* 2022 | Intro p.10, Ch7 | Verify against Murray et al. 2022 (Lancet) global burden estimate |
| 4 | "10 million deaths/yr by 2050 from AMR" | O'Neill Review 2016 | Intro p.10, Ch7 | This is the O'Neill projection; widely cited but methodologically contested. Note as projection |
| 5 | "500,000+ overdose deaths in USA from opioids" | Various — likely CDC | Ch7 | CDC WONDER dataset cumulative 1999–present |
| 6 | "20–25% addiction rate in chronic non-cancer pain" | Vowles et al. 2015 meta-analysis | Ch7 | Verify meta-analysis exists and the range matches |
| 7 | "Porter and Jick 1980 letter cited 600+ times" | Implied: Leung et al. 2017 | Ch7 | Leung et al. 2017 *NEJM* letter on this exact topic |
| 8 | "76 million → 219 million opioid prescriptions 1991–2011" | Implied: CDC / IMS Health | Ch7 | Verify prescription trend data from CDC |
| 9 | "Methicillin introduced 1959; MRSA identified 1961" | Standard medical history | Ch7 | Verify dates against authoritative medical history |
| 10 | "OS/360: 3 years became 5; budget exceeded by 10x" | Implied: Brooks 1975 | Ch5 | Verify against *The Mythical Man-Month* original text |

## Tier 2 — institutional and quantitative claims

| # | Claim | Source claimed | Page | Verify |
|---|---|---|---|---|
| 11 | "Windows NT 3.1: 4.5M LOC; Windows 11: ~100M LOC" | Various | Ch5 | These are widely cited but the exact numbers vary; cite a single authoritative source or weaken to "approximately" |
| 12 | "CVE: 894 in 1999 → 28,902 in 2023 = 32-fold" | NIST NVD | Ch5 | NIST NVD statistics page |
| 13 | "Log4Shell: 840,000 attack attempts/hour within 72 hours" | Various security firms | Ch5 | Multiple sources — pick one and cite |
| 14 | "SolarWinds: ~18,000 organisations compromised" | Various US gov sources | Ch5 | US CISA reporting |
| 15 | "Leftpad: 11-line function, broke React etc. in 30 min" | Standard tech-press account | Ch5 | The Register and others reported this; verify the line count and the 30-minute figure |
| 16 | "npm 2016: 250,000 packages → 2023: 1.8M+" | npm | Ch5 | npmjs.com statistics |
| 17 | "False news spreads 6× faster on Twitter; 70% more likely to be retweeted" | Aral et al. 2018 (NOT 2020 as in draft) | Ch5 | Vosoughi, Roy, Aral *Science* 2018 (correct citation — book currently has "2020 MIT study" which is wrong; should be 2018) |
| 18 | "319 billion daily emails; ~45% spam" | Statista or industry | Ch5 | Verify current figure |
| 19 | "Brooks' Law: communication links = n(n-1)/2" | Brooks 1975 | Ch5 | Mathematically trivially correct |
| 20 | "Colonial Pipeline ransomware May 2021" | Standard US press | Ch5 | DOJ, Bloomberg |

## Tier 3 — historical attributions

| # | Claim | Source claimed | Page | Verify |
|---|---|---|---|---|
| 21 | "Cobra Effect: Horst Siebert 2001 *Der Kobra-Effekt*" | Siebert 2001 | Ch6, Intro | The book exists; the name "cobra effect" predates Siebert in oral economics tradition. Phrase as "named for the pattern by economist Horst Siebert" |
| 22 | "Hanoi rat-tail bounty, 1902, French colonial" | Michael Vann historical research | Intro, Ch6 | Vann's *The Great Hanoi Rat Hunt* and his French Colonial History journal articles |
| 23 | "Prague dog-tail bounty, early 1900s" | Folk story, less well documented | Intro | This is harder to source; consider weakening to "anecdotally reported" or dropping |
| 24 | "Cambodia UXO reward programme" | UN/MAG records | Intro | UN Mine Action records |
| 25 | "ARPANET first message Oct 29 1969: 'lo'" | Computer history standard | Ch5 | Charles Kline, UCLA — verified historical record |
| 26 | "First spam: Gary Thuerk, DEC, May 3 1978" | Computer history | Ch5 | Standard tech history sources |
| 27 | "Fleming's 1945 Nobel warning quote" | Fleming Nobel lecture 1945 | Ch7 | NobelPrize.org — direct quote verification |
| 28 | "Penicillin-resistant Staph isolated 1940; clinical hospitals 1947" | Medical history | Ch7 | Verify against multiple history-of-medicine sources |
| 29 | "Edward Murphy 1949 USAF deceleration experiment" | Standard engineering history | Ch1 | Multiple sources; the exact details vary |
| 30 | "Robert Merton 1936 paper in *American Sociological Review*" | Merton 1936 | Ch1 | Confirm — "The Unanticipated Consequences of Purposive Social Action" |

## Tier 4 — named people / named institutions (legal-adjacent)

These overlap with the legal-read in Phase 4. Verify the wording is factually defensible and tonally fair.

| # | Claim | Page | Risk |
|---|---|---|---|
| 31 | Sackler family / Purdue Pharma marketing tactics | Ch7 | Defamation risk if any specific claim is unsupported. Tie every claim to a court document or settlement record |
| 32 | "$4.5 billion settlement from Sackler family personally" | Ch7 | Verify against actual bankruptcy / DOJ filings |
| 33 | "Purdue 671 paid speakers" | Ch7 | Source needed — likely from DOJ filings or Keefe et al. journalism |
| 34 | Meta/Facebook "engagement-maximising algorithms" | Ch9 | General claim, defensible; but specifics about decision-making should cite leaked documents or Frances Haugen testimony |
| 35 | Steve Jobs "did not design the attention economy…" | Intro p.~15 | Opinion framing; defensible as commentary |
| 36 | Mariam Roussafi attribution | Preface | **Must get her written permission to be named.** |
| 37 | Badreddine Otky attribution | Preface | **Must get his written permission to be named.** |

## Tier 5 — chapters 8–9 (less verified in current draft)

| # | Claim | Page | Verify |
|---|---|---|---|
| 38 | "$1 trillion spent on War on Drugs" | Ch8 | Standard estimate, multiple sources; cite one |
| 39 | "GDPR compliance industry size" | Ch8 | DataPrivacyManager, IAPP reports |
| 40 | "Braess Paradox 1968" | Ch9 | Original Braess paper |
| 41 | "Green Revolution productivity numbers" | Ch9 | FAO statistics |
| 42 | "Social media teen mental health" | Ch9 | Be very careful here — Haidt's claims are contested. Cite specific studies, not just secondary press |
| 43 | "Holodomor casualty figures" | Ch8 | Use ranges from established historians (Snyder, Conquest) not single numbers |

## Tier 6 — Ch10 / Ch11 framework claims

| # | Claim | Page | Verify |
|---|---|---|---|
| 44 | "α typically falls between 1.2 and 1.8" (in book's research paper, mentioned in Ch10) | Ch10 | This is from your own research paper; ensure cross-reference is to the paper |
| 45 | "OxyContin retrospective Cobra Score above 0.85" | Ch11 | This is an illustration, not a measurement. Make sure the prose makes that clear |
| 46 | Cobra Score thresholds (0.3 / 0.6) | Ch11 | These are framework conventions; ensure they're presented as such, not as empirically calibrated |

## Tier 7 — appendices

| # | Claim | Page | Verify |
|---|---|---|---|
| 47 | "Fifty Solution-Problem Pairs" table | App C | Spot-check 5 random rows for date and effect accuracy |
| 48 | Bibliography entries | App | Verify each cited work has the right author/year/journal |
| 49 | Glossary definitions | App F | Cross-check with main text usage |
| 50 | Index references map to correct chapters | App / Index | Already verified structurally; verify a sample of 10 entries |

---

## Format for tracking results

Create `revision/factcheck_results.csv` with columns: `id, claim, page, source_found, status (✅⚠️❌), notes, action`.

When a claim fails or is off, message Claude with the id and the issue. Claude can draft a replacement sentence that keeps the rhetorical shape and uses a defensible number.
