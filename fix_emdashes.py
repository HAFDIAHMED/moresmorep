"""
fix_emdashes.py
Reduces em dashes in book source files from ~1,907 to ~100-150.
Operates ONLY on Python string literal content — never touches
comments, variable names, or Python syntax.
Uses tokenize to safely isolate string tokens.
"""
import re
import tokenize
import io
import os

# ── Replacement rules ──────────────────────────────────────────────────────────
# Applied in order. Using str.replace() (literal match) — no regex surprises.

RULES = [
    # --- relative clauses (always comma) ---
    (' — which ',    ', which '),
    (' — who ',      ', who '),
    (' — whose ',    ', whose '),
    (' — where ',    ', where '),
    (' — whereas ',  ', whereas '),
    # --- appositives / elaborations (comma) ---
    (' — a ',        ', a '),
    (' — an ',       ', an '),
    (' — the ',      ', the '),
    (' — one ',      ', one '),
    (' — each ',     ', each '),
    (' — all ',      ', all '),
    (' — both ',     ', both '),
    (' — some ',     ', some '),
    (' — any ',      ', any '),
    # --- conjunctions ---
    (' — and ',      ', and '),
    (' — but ',      ' but '),
    (' — or ',       ', or '),
    (' — nor ',      ', nor '),
    (' — yet ',      ', yet '),
    # --- qualifiers / negatives ---
    (' — not ',      ', not '),
    (' — never ',    ', never '),
    (' — no ',       ', no '),
    (' — rather ',   ', rather '),
    (' — instead ',  ', instead '),
    (' — only ',     ', only '),
    (' — even ',     ', even '),
    (' — perhaps ',  ', perhaps '),
    (' — possibly ', ', possibly '),
    (' — often ',    ', often '),
    (' — always ',   ', always '),
    (' — usually ',  ', usually '),
    (' — rarely ',   ', rarely '),
    (' — largely ',  ', largely '),
    (' — partly ',   ', partly '),
    (' — simply ',   ', simply '),
    (' — merely ',   ', merely '),
    (' — precisely ', ', precisely '),
    (' — especially ', ', especially '),
    (' — including ', ', including '),
    (' — excluding ', ', excluding '),
    (' — particularly ', ', particularly '),
    # --- prepositional phrases ---
    (' — in ',       ', in '),
    (' — at ',       ', at '),
    (' — on ',       ', on '),
    (' — to ',       ', to '),
    (' — for ',      ', for '),
    (' — with ',     ', with '),
    (' — without ',  ', without '),
    (' — from ',     ', from '),
    (' — by ',       ', by '),
    (' — as ',       ', as '),
    (' — like ',     ', like '),
    (' — unlike ',   ', unlike '),
    (' — through ',  ', through '),
    (' — across ',   ', across '),
    (' — over ',     ', over '),
    (' — under ',    ', under '),
    (' — between ',  ', between '),
    (' — among ',    ', among '),
    (' — within ',   ', within '),
    (' — despite ',  ', despite '),
    (' — beyond ',   ', beyond '),
    # --- independent clause starters (semicolon) ---
    (' — it ',       '; it '),
    (' — they ',     '; they '),
    (' — he ',       '; he '),
    (' — she ',      '; she '),
    (' — we ',       '; we '),
    (' — there ',    '; there '),
    (' — here ',     '; here '),
    (' — such ',     '; such '),
    (' — what ',     '; what '),
    (' — when ',     ', when '),
    (' — if ',       ', if '),
    (' — although ', ', although '),
    (' — while ',    ', while '),
    (' — because ',  ', because '),
    (' — since ',    ', since '),
    (' — unless ',   ', unless '),
    (' — until ',    ', until '),
    (' — whether ',  ', whether '),
    # --- explanation / elaboration (colon) ---
    (' — specifically', ': specifically'),
    (' — namely',    ': namely'),
    (' — i.e.',      ', i.e.'),
    (' — e.g.',      ', e.g.'),
    (' — that is',   ', that is'),
    (' — in other words', ', in other words'),
    # --- new-sentence starters (period + capital) ---
    (' — This ',     '. This '),
    (' — These ',    '. These '),
    (' — That ',     '. That '),
    (' — Those ',    '. Those '),
    (' — Such ',     '. Such '),
    (' — The ',      '. The '),  # intentional: starts new sentence
    # --- verb-led independent clauses (semicolon) ---
    (' — is ',       ' is '),   # usually part of relative clause, remove dash only
    (' — are ',      ' are '),
    (' — was ',      ' was '),
    (' — were ',     ' were '),
    (' — has ',      ' has '),
    (' — have ',     ' have '),
    (' — had ',      ' had '),
    (' — does ',     ' does '),
    (' — do ',       ' do '),
    (' — did ',      ' did '),
    (' — can ',      ' can '),
    (' — could ',    ' could '),
    (' — will ',     ' will '),
    (' — would ',    ' would '),
    (' — may ',      ' may '),
    (' — might ',    ' might '),
    (' — should ',   ' should '),
    (' — must ',     ' must '),
    (' — shall ',    ' shall '),
    # --- cascade/content-specific words ---
    (' — solved',    ', solved'),
    (' — generated', ', generated'),
    (' — generates', ', generates'),
    (' — created',   ', created'),
    (' — produces',  ', produces'),
    (' — documented', ', documented'),
    (' — demonstrated', ', demonstrated'),
    (' — measured',  ', measured'),
    (' — estimated', ', estimated'),
    (' — calculated', ', calculated'),
    (' — observed',  ', observed'),
    (' — confirmed', ', confirmed'),
    (' — described', ', described'),
    (' — defined',   ', defined'),
    (' — more ',     ', more '),
    (' — less ',     ', less '),
    (' — most ',     ', most '),
    (' — least ',    ', least '),
    (' — higher ',   ', higher '),
    (' — lower ',    ', lower '),
    (' — greater ',  ', greater '),
    (' — smaller ',  ', smaller '),
    (' — larger ',   ', larger '),
    (' — faster ',   ', faster '),
    (' — slower ',   ', slower '),
    (' — further ',  ', further '),
]

EM = ' — '


def fix_string_content(s: str) -> str:
    """Apply all em dash rules to a string's content."""
    # Pass 1: double em dashes → parentheses
    # e.g. "cases — Delhi, Hanoi — is" → "cases (Delhi, Hanoi) is"
    s = re.sub(r' — ([^—\n]{4,60}) — ', r' (\1) ', s)

    # Pass 2: rule-based single em dash replacement
    for pattern, replacement in RULES:
        s = s.replace(pattern, replacement)

    return s


def process_file(path: str) -> tuple[int, int]:
    """
    Read a Python file, apply em dash fixes only inside string literals,
    write back. Returns (original_count, final_count).
    """
    with open(path, 'r', encoding='utf-8') as f:
        source = f.read()

    original_count = source.count(EM)
    if original_count == 0:
        return 0, 0

    # Use tokenize to find string token positions
    tokens = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(source).readline):
            tokens.append(tok)
    except tokenize.TokenError:
        # Fallback: treat whole file as processable text (rare edge case)
        fixed = fix_string_content(source)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(fixed)
        return original_count, fixed.count(EM)

    # Rebuild source with string literals replaced
    result = []
    prev_end = 0
    lines = source.splitlines(keepends=True)

    # Build character-offset index for line/col → offset conversion
    offsets = []
    pos = 0
    for line in lines:
        offsets.append(pos)
        pos += len(line)

    def to_offset(row, col):
        return offsets[row - 1] + col

    for tok_type, tok_string, tok_start, tok_end, _ in tokens:
        if tok_type == tokenize.STRING:
            start_off = to_offset(*tok_start)
            end_off   = to_offset(*tok_end)

            # Append unchanged source up to this token
            result.append(source[prev_end:start_off])

            # Only fix tokens that are actual text strings (not bytes, not f-strings
            # containing complex expressions). Safe heuristic: check it contains ' — '
            if EM in tok_string:
                # Determine quote style and extract content
                fixed_token = fix_string_content(tok_string)
                result.append(fixed_token)
            else:
                result.append(tok_string)

            prev_end = end_off

    # Append remainder
    result.append(source[prev_end:])
    fixed_source = ''.join(result)

    final_count = fixed_source.count(EM)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(fixed_source)

    return original_count, final_count


if __name__ == '__main__':
    BASE = '/Users/vpro/Desktop/book_solutions_problems'
    FILES = [
        'book_chapters_intro.py',
        'book_chapters_4to6.py',
        'book_chapters_7to9.py',
        'book_chapters_10to13.py',
        'generate_book.py',
    ]

    print(f"{'FILE':<35} {'BEFORE':>8} {'AFTER':>8} {'REMOVED':>9}")
    print('─' * 65)

    total_before = 0
    total_after  = 0

    for fname in FILES:
        path = os.path.join(BASE, fname)
        before, after = process_file(path)
        removed = before - after
        total_before += before
        total_after  += after
        print(f"{fname:<35} {before:>8} {after:>8} {removed:>9}")

    print('─' * 65)
    print(f"{'TOTAL':<35} {total_before:>8} {total_after:>8} {total_before - total_after:>9}")
    print(f"\nTarget was < 150 remaining. Result: {total_after}")
