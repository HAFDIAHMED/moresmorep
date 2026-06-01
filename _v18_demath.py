"""v18 — comprehensive de-mathing pass.

Two parts:

A. **Rewrite the Exponential Trap section** in Chapter 1 (book_chapters_intro_reader.py).
   The page the reader showed contained C(n,2) = n(n-1)/2, k-way C(n,k-1),
   Σ C(n,k) = 2ⁿ - 1, and 'on 10 medications has over 1,000 possible interactions'
   — all rendered as bullet-point combinatorics. Replace with philosophical prose
   that makes the same point without the math.

B. **Global regex sweep** across all four chapter-source files. Replace every
   remaining Greek-symbol / function-notation passage with its plain-English
   equivalent. Order matters: longer/more-specific patterns first.

Maps (case-insensitive on the labels, identifier-aware):
  Φ(LLM)                → the model\'s complexity
  Φ(OxyContin)          → OxyContin\'s complexity
  Φ(CDO)                → the CDO\'s complexity
  Φ(VLSI), Φ(s), ...    → "the complexity of <…>" / "complexity"
  Σ(X, Y)               → "interaction between X and Y"
  Σ(LLM, ...) etc.      → "the model\'s interaction with the information ecosystem"
  Ω(s, sᵢ) / Ω(...)     → "domain overlap"
  α \= 1.4              → "around 1.4"
  α \>/< 1              → "the amplification factor"
  C(s) / C(X)           → "cascade coefficient"
  C(s,sᵢ)               → "cascade coefficient of the pair"
  N(s) / N(X)           → "reach"
  N(s)^α                → "reach raised to the amplification exponent"
  Greek letters standalone (Σ, Φ, Ω, α) → contextual plain English

This is the heaviest content edit yet. Build v18 after.
"""
import io, os, re

DIR = os.path.dirname(__file__) or '.'

# ───────────────────────────────────────────────────────────────────────────
# PART A — Exponential Trap rewrite
# ───────────────────────────────────────────────────────────────────────────
PATH_INTRO = os.path.join(DIR, 'book_chapters_intro_reader.py')
with io.open(PATH_INTRO, 'r', encoding='utf-8') as f:
    intro = f.read()

# The bullet-list math block + the three professional-examples paragraphs.
OLD = '''        ('body0', """To understand why the growth is exponential, consider a simplified model.
You have a system (a city, a codebase, a body, an economy) that currently contains
n solutions. You introduce a new solution s. That solution creates:"""),

        ('body', """• Its own direct problems (individual complexity): proportional to n⁰ = 1 (constant)"""),
        ('body', """• Pairwise interaction problems with each existing solution: n terms"""),
        ('body', """• Three-way interaction problems: C(n,2) = n(n-1)/2 terms"""),
        ('body', """• k-way interaction problems: C(n, k-1) terms for each k"""),

        ('body', """Summing all interaction orders from k=1 to n gives Σ C(n,k) = 2ⁿ - 1.
This is the combinatorial explosion at the heart of the cascade. Every new solution
potentially interacts with every subset of existing solutions. In practice, most of
these interactions are negligible or benign but in complex systems, the fraction
that are harmful is never zero, and even a small harmful fraction of 2ⁿ is a large
number of real problems."""),

        ('body', """This is not a theoretical abstraction. Software engineers know this
reality by the name of "integration complexity." Every time a new feature is added to
a large codebase, the testing burden grows not linearly but combinatorially — because
the new feature must be tested not just in isolation but in combination with every
existing feature, and every combination of existing features that might plausibly
interact with it. This is why large software projects routinely consume testing budgets
that dwarf development budgets, and why the number of bugs in a mature codebase never
reaches zero no matter how much testing is done."""),

        ('body', """Physicians know this reality as polypharmacy. When a patient takes
multiple medications, the number of possible drug-drug interactions grows as 2ⁿ. A
patient on 10 medications has over 1,000 possible interaction effects to monitor. This
is why elderly patients (who are typically on the most medications) are the most
vulnerable to adverse drug reactions, and why medication reconciliation (the process
of checking a patient's complete drug list) is one of the highest-risk activities in
clinical medicine."""),

        ('body', """Economists know this reality as systemic risk. A financial system with
many institutions and instruments has many more channels for contagion than a simpler
system. The 2008 financial crisis was, at its structural core, an exponential cascade
problem: complex instruments created complex interdependencies, and when one component
failed, the failure propagated through 2ⁿ channels simultaneously. The bailout programs
that followed added further complexity, creating new interaction effects that are still
being managed today."""),'''

NEW = '''        ('body0', """Why does the growth accelerate rather than merely add up? The
answer has nothing to do with the particular field — it has to do with how complex
systems are wired. Picture a system: a city, a codebase, a body, an economy. It already
contains some number of moving parts. Now imagine adding one more. The new arrival
brings, by itself, a small amount of trouble. It also interacts with each existing part
on its own, then with every pair of existing parts, then with every triple, every group
of four, and so on, all the way up to interacting with all of them at once."""),

        ('body', """The number of these possible interaction patterns roughly doubles with
every new part added. Most of the patterns are harmless. But complex systems guarantee
that a non-trivial fraction will not be — and a small fraction of a doubling-with-each-
step number is, very quickly, a large number of real problems. This is the structural
reason why complex systems get worse faster than they get bigger."""),

        ('body', """This is not theory. Software engineers know it as <i>integration
complexity</i>. Every time a feature is added to a large codebase, the testing burden
grows not just by one but by the number of ways the new feature can combine with every
feature already there. This is why large software projects routinely spend more on
testing than on building, and why the count of bugs in any mature codebase never
quite reaches zero."""),

        ('body', """Physicians know it as <i>polypharmacy</i>. The combinations of drugs
that can interact with each other multiply with every new prescription. A patient on
ten medications has hundreds of possible drug-drug interactions to monitor; a patient
on twenty, many thousands. This is why elderly patients, who tend to be on the most
medications, are the most vulnerable to adverse drug reactions, and why medication
reconciliation — the careful review of a patient\\'s complete drug list — is among
the highest-risk activities in clinical medicine."""),

        ('body', """Economists know it as <i>systemic risk</i>. A financial system with
many institutions and instruments has dramatically more channels for contagion than a
simpler one. The 2008 crisis was, at its structural core, an interaction-cascade problem:
complex instruments created complex interdependencies, and when one component failed,
the failure spread through every connection at once. The bailout programmes that
followed added more complexity, creating new interactions that are still being managed
today."""),'''

if OLD in intro:
    intro = intro.replace(OLD, NEW, 1)
    print('  [A] Exponential-Trap section rewritten in plain prose')
else:
    print('  [A] anchor not found — SKIPPED')

with io.open(PATH_INTRO, 'w', encoding='utf-8') as f:
    f.write(intro)


# ───────────────────────────────────────────────────────────────────────────
# PART B — Global regex sweep across all chapter files
# ───────────────────────────────────────────────────────────────────────────
# Substitutions ordered most-specific → least-specific.
SUBS = [
    # ---- Specific case-study identifiers ---------------------------------
    # Φ(name), C(name), N(name) for named solutions
    (r'\\u03a6\(LLM\)|Φ\(LLM\)',           "the model's complexity"),
    (r'\\u03a6\(OxyContin\)|Φ\(OxyContin\)', "OxyContin's complexity"),
    (r'\\u03a6\(CDO[^)]*\)|Φ\(CDO[^)]*\)', "the CDO's complexity"),
    (r'\\u03a6\(VLSI\)|Φ\(VLSI\)',         "the VLSI initiative's complexity"),
    (r'\\u03a6\(s\)|Φ\(s\)',               "the solution's complexity"),
    (r'\\u03a6',                            "complexity"),    # any remaining Φ
    (r'Φ',                                  "complexity"),
    (r'\bC\(LLM\)',                        "the model's cascade coefficient"),
    (r'\bC\(OxyContin\)',                  "OxyContin's cascade coefficient"),
    (r'\bC\(CDO[^)]*\)',                   "the CDO's cascade coefficient"),
    (r'\bC\(s,\s*s[ᵢi]\)',                 "the pair's interaction coefficient"),
    (r'\bC\(s,\s*s\w*\)',                  "the pair's interaction coefficient"),
    (r'\bC\(s\)',                          "cascade coefficient"),
    (r'\bN\(LLM\)',                        "the model's reach"),
    (r'\bN\(OxyContin\)',                  "OxyContin's reach"),
    (r'\bN\(CDO[^)]*\)',                   "the CDO's reach"),
    (r'\bN\(s\)\^[α\\u03b1]\d*[\.\d]*',    "reach raised to the amplification exponent"),
    (r'\bN\(s\)\^\\u03b1',                 "reach raised to the amplification exponent"),
    (r'\bN\(s,\s*s\w*\)',                  "the pair's reach"),
    (r'\bN\(s\)',                          "reach"),
    (r'\bN\(s\)⁺',                    "reach"),
    # Σ(X, Y) pair forms ---------------------------------------------------
    (r'Σ\(LLM,\s*[^)]+\)',                 "the model's interaction with the information ecosystem"),
    (r'Σ\(OxyContin[^)]+\)',               "the OxyContin interaction profile"),
    (r'Σ\(CDO,\s*CDS\)',                   "the CDO-CDS interaction"),
    (r'Σ\(s,\s*s[ᵢi]\)|Σ\(s,\s*sⱼ\)',      "the interaction amplification"),
    # Ω(s, sᵢ) forms -------------------------------------------------------
    (r'\\u03a9\(s,\s*s[ᵢi]\)|Ω\(s,\s*s[ᵢi]\)', "the domain overlap"),
    (r'\\u03a9\(s,\s*s\w+\)|Ω\(s,\s*s\w+\)',   "the domain overlap"),
    (r'\\u03a9\([^)]+\)|Ω\([^)]+\)',           "the domain overlap"),
    # Standalone Greek letters and α references ----------------------------
    (r'\bα\s*=\s*(\d+\.\d+)',              r'around \1'),
    (r'\bα\s*≈\s*(\d+\.\d+)',              r'around \1'),
    (r'\bα\s*>\s*1\b',                     "above one"),
    (r'\bα\s*<\s*1\b',                     "below one"),
    (r'\bα\b',                              "the amplification factor"),
    (r'Σᵢ\s*Ω\([^)]*\)\s*[·]\s*Σ\([^)]*\)', "the sum of interaction terms"),
    (r'Σᵢ',                                "the sum"),
    (r'\bΣ\b',                              "interaction amplification"),
    (r'\bΩ\b',                              "domain overlap"),
    # Polynomial-style expressions ----------------------------------------
    (r'P_total\(n\)',                      "the total problem count"),
    (r'S_total\(n\)',                      "the total solution count"),
    (r'\bO\(2[\^ⁿn]\)',                    "exponential"),
    (r'\bO\(2\^n\)',                       "exponential"),
    (r'\bO\(log\s*n\)',                    "logarithmic"),
    (r'\bO\(n\)',                          "linear"),
    (r'\bO\(n²\)',                         "quadratic"),
    (r'\bO\(n\^2\)',                       "quadratic"),
    (r'\bO\(n³\)',                         "cubic"),
    (r'\bO\(n\^3\)',                       "cubic"),
    (r'\bf\(n\)\b',                        "the solution-generation rate"),
    (r'\bg\(n\)\b',                        "the problem-generation rate"),
    (r'\bh\(n\)\b',                        "the rate"),
]

files = ['book_chapters_intro_reader.py',
         'book_chapters_4to6_reader.py',
         'book_chapters_7to9_reader.py',
         'book_chapters_10to13_reader.py']

for fname in files:
    path = os.path.join(DIR, fname)
    with io.open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    before = len(src)
    counts = {}
    for pat, repl in SUBS:
        new_src, n = re.subn(pat, repl, src)
        if n:
            counts[pat[:50]] = n
        src = new_src
    after = len(src)
    if counts:
        print(f'  [B] {fname}: {before} -> {after} chars ({after-before:+d})')
        for k, v in counts.items():
            print(f'        {v:>4}x  {k}')
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(src)

print('\nDone.')
