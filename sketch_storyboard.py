"""Generate `storyboard_sketch.html` — the trailer storyboard rendered as
pencil-style SVG sketches. Each line is drawn as 2-3 overlapping strokes with
slight jitter to mimic graphite on paper. Output is one HTML file you can open
in a browser, print, or hand to a director."""
import os, math, random

random.seed(7)

# ── palette ──────────────────────────────────────────────────────────────────
PAPER   = '#ece6d4'
GRAPH_L = '#7a6e5a'   # light pencil — construction lines
GRAPH_M = '#3a3326'   # medium pencil — main strokes
GRAPH_D = '#1a160e'   # dark pencil — accents
WHITE   = '#f4efde'   # eraser highlight

W = 600        # frame width
H = 338        # frame height (16:9)


# ── sketchy primitives ───────────────────────────────────────────────────────
def jitter(x, mag=1.5):
    return x + random.uniform(-mag, mag)


def sk_line(x1, y1, x2, y2, strokes=3, weight=1.4, color=GRAPH_M, opacity=0.75, jit=1.2):
    """Draw a sketchy line as N overlapping strokes."""
    out = []
    for i in range(strokes):
        # control points slightly offset for each pass
        a = (jitter(x1, jit), jitter(y1, jit))
        b = (jitter(x2, jit), jitter(y2, jit))
        # bezier curve with a slight bow for hand-drawn feel
        midx = (a[0] + b[0]) / 2 + random.uniform(-jit, jit)
        midy = (a[1] + b[1]) / 2 + random.uniform(-jit, jit)
        op = opacity * random.uniform(0.55, 1.0)
        sw = weight * random.uniform(0.7, 1.15)
        out.append(
            f'<path d="M {a[0]:.1f} {a[1]:.1f} Q {midx:.1f} {midy:.1f} {b[0]:.1f} {b[1]:.1f}" '
            f'stroke="{color}" stroke-width="{sw:.2f}" fill="none" '
            f'stroke-linecap="round" stroke-linejoin="round" opacity="{op:.2f}"/>'
        )
    return '\n'.join(out)


def sk_path(d, strokes=2, weight=1.4, color=GRAPH_M, opacity=0.75):
    """Multi-stroke version of any SVG path."""
    out = []
    for i in range(strokes):
        op = opacity * random.uniform(0.55, 1.0)
        sw = weight * random.uniform(0.75, 1.1)
        offset = f'translate({jitter(0, 0.8):.1f},{jitter(0, 0.8):.1f})'
        out.append(
            f'<path d="{d}" stroke="{color}" stroke-width="{sw:.2f}" '
            f'fill="none" stroke-linecap="round" stroke-linejoin="round" '
            f'opacity="{op:.2f}" transform="{offset}"/>'
        )
    return '\n'.join(out)


def sk_rect(x, y, w, h, strokes=2, weight=1.3, color=GRAPH_M, opacity=0.75):
    """Sketchy rectangle, four sketchy lines."""
    parts = []
    parts.append(sk_line(x, y, x + w, y, strokes, weight, color, opacity))
    parts.append(sk_line(x + w, y, x + w, y + h, strokes, weight, color, opacity))
    parts.append(sk_line(x + w, y + h, x, y + h, strokes, weight, color, opacity))
    parts.append(sk_line(x, y + h, x, y, strokes, weight, color, opacity))
    return '\n'.join(parts)


def sk_ellipse(cx, cy, rx, ry, strokes=3, weight=1.3, color=GRAPH_M, opacity=0.75):
    """Sketchy ellipse from multiple overlapping arc paths."""
    out = []
    for i in range(strokes):
        dx = jitter(0, 0.8)
        dy = jitter(0, 0.8)
        r1 = rx + jitter(0, 0.8)
        r2 = ry + jitter(0, 0.8)
        op = opacity * random.uniform(0.55, 1.0)
        sw = weight * random.uniform(0.75, 1.1)
        out.append(
            f'<ellipse cx="{cx + dx:.1f}" cy="{cy + dy:.1f}" rx="{r1:.1f}" ry="{r2:.1f}" '
            f'stroke="{color}" stroke-width="{sw:.2f}" fill="none" '
            f'stroke-linecap="round" opacity="{op:.2f}"/>'
        )
    return '\n'.join(out)


def hatch(x, y, w, h, angle=45, spacing=4, weight=0.8, color=GRAPH_L, opacity=0.45):
    """Diagonal hatching to indicate shadow."""
    out = []
    rad = math.radians(angle)
    dx, dy = math.cos(rad), math.sin(rad)
    diag = math.hypot(w, h)
    n_lines = int(diag / spacing) + 4
    # perpendicular vector
    px, py = -dy, dx
    for i in range(-n_lines, n_lines):
        offset = i * spacing
        x0 = x + w/2 + px*offset - dx*diag
        y0 = y + h/2 + py*offset - dy*diag
        x1 = x + w/2 + px*offset + dx*diag
        y1 = y + h/2 + py*offset + dy*diag
        # clip to bbox
        out.append(
            f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" '
            f'stroke="{color}" stroke-width="{weight * random.uniform(0.7, 1.2):.2f}" '
            f'opacity="{opacity * random.uniform(0.6, 1.0):.2f}" stroke-linecap="round"/>'
        )
    clip_id = f'cliphatch_{x}_{y}_{angle}'.replace('.', '_').replace('-', 'n')
    clip_def = (
        f'<defs><clipPath id="{clip_id}">'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath></defs>'
    )
    return f'{clip_def}<g clip-path="url(#{clip_id})">{"".join(out)}</g>'


def sk_text(x, y, text, size=13, color=GRAPH_D, font='Georgia', italic=False, anchor='middle'):
    style = 'italic' if italic else 'normal'
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{font}" '
        f'font-size="{size}" font-style="{style}" fill="{color}" '
        f'letter-spacing="0.5">{text}</text>'
    )


# ── figure helpers ───────────────────────────────────────────────────────────
def sk_seated_figure(cx, cy, scale=1.0, dark=True):
    """A seated figure, gesture-drawing style."""
    s = scale
    color = GRAPH_D if dark else GRAPH_M
    parts = []
    # head — slightly tilted oval
    parts.append(sk_ellipse(cx, cy - 60*s, 14*s, 17*s, strokes=4, weight=1.3, color=color, opacity=0.78))
    # construction lines through head (gesture-drawing convention)
    parts.append(sk_line(cx - 14*s, cy - 60*s, cx + 14*s, cy - 60*s, strokes=1, weight=0.6, color=GRAPH_L, opacity=0.5))
    parts.append(sk_line(cx, cy - 77*s, cx, cy - 43*s, strokes=1, weight=0.6, color=GRAPH_L, opacity=0.5))
    # neck — two short lines
    parts.append(sk_line(cx - 5*s, cy - 43*s, cx - 8*s, cy - 30*s, strokes=2, weight=1.1, color=color, opacity=0.75))
    parts.append(sk_line(cx + 5*s, cy - 43*s, cx + 8*s, cy - 30*s, strokes=2, weight=1.1, color=color, opacity=0.75))
    # torso — trapezoid via 4 lines
    parts.append(sk_line(cx - 8*s, cy - 30*s, cx - 22*s, cy + 5*s, strokes=2, weight=1.3, color=color))
    parts.append(sk_line(cx + 8*s, cy - 30*s, cx + 22*s, cy + 5*s, strokes=2, weight=1.3, color=color))
    parts.append(sk_line(cx - 22*s, cy + 5*s, cx - 20*s, cy + 35*s, strokes=2, weight=1.3, color=color))
    parts.append(sk_line(cx + 22*s, cy + 5*s, cx + 20*s, cy + 35*s, strokes=2, weight=1.3, color=color))
    parts.append(sk_line(cx - 20*s, cy + 35*s, cx + 20*s, cy + 35*s, strokes=2, weight=1.2, color=color))
    # shoulders gesture
    parts.append(sk_line(cx - 22*s, cy - 25*s, cx - 8*s, cy - 30*s, strokes=2, weight=1.1, color=color, opacity=0.7))
    parts.append(sk_line(cx + 8*s, cy - 30*s, cx + 22*s, cy - 25*s, strokes=2, weight=1.1, color=color, opacity=0.7))
    # arms resting on thighs — quick lines
    parts.append(sk_line(cx - 22*s, cy + 5*s, cx - 18*s, cy + 32*s, strokes=2, weight=1.1, color=color, opacity=0.7))
    parts.append(sk_line(cx + 22*s, cy + 5*s, cx + 18*s, cy + 32*s, strokes=2, weight=1.1, color=color, opacity=0.7))
    return '\n'.join(parts)


def sk_chair(cx, cy_seat, scale=1.0):
    """Simple chair underneath a figure."""
    s = scale
    parts = []
    # seat
    parts.append(sk_line(cx - 24*s, cy_seat, cx + 24*s, cy_seat, strokes=2, weight=1.4, color=GRAPH_M))
    # front legs
    parts.append(sk_line(cx - 22*s, cy_seat, cx - 22*s, cy_seat + 38*s, strokes=2, weight=1.3, color=GRAPH_M))
    parts.append(sk_line(cx + 22*s, cy_seat, cx + 22*s, cy_seat + 38*s, strokes=2, weight=1.3, color=GRAPH_M))
    return '\n'.join(parts)


def sk_wood_wall(x, y, w, h, n_panels=6):
    """Vertical wood panel lines on a wall."""
    parts = []
    # outer rect
    parts.append(sk_line(x, y, x + w, y, strokes=2, weight=1.0, color=GRAPH_M))
    parts.append(sk_line(x, y + h, x + w, y + h, strokes=2, weight=1.0, color=GRAPH_M))
    # vertical panels — light construction lines
    for i in range(1, n_panels):
        px = x + (w / n_panels) * i + jitter(0, 1.5)
        parts.append(sk_line(px, y, px, y + h, strokes=2, weight=0.7, color=GRAPH_L, opacity=0.55))
    return '\n'.join(parts)


def sk_ceiling_lamp(cx, top_y, width=44):
    parts = []
    parts.append(sk_line(cx - width/2, top_y, cx + width/2, top_y, strokes=3, weight=2.0, color=GRAPH_D))
    parts.append(sk_line(cx - width/2, top_y + 4, cx + width/2, top_y + 4, strokes=2, weight=1.4, color=GRAPH_D, opacity=0.8))
    return '\n'.join(parts)


def sk_light_cone(cx, top_y, base_y, half_top=22, half_base=80):
    """Faint cone of light beneath an overhead lamp — drawn as 2 angled lines."""
    parts = []
    parts.append(sk_line(cx - half_top, top_y, cx - half_base, base_y,
                         strokes=2, weight=0.7, color=GRAPH_L, opacity=0.4))
    parts.append(sk_line(cx + half_top, top_y, cx + half_base, base_y,
                         strokes=2, weight=0.7, color=GRAPH_L, opacity=0.4))
    return '\n'.join(parts)


# ── frame wrapper ────────────────────────────────────────────────────────────
def frame_open():
    """Open an SVG element with paper background."""
    return (
        f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
        f'class="shot">\n'
        f'<rect width="{W}" height="{H}" fill="{PAPER}"/>\n'
        # subtle paper texture: very faint speckle via filter
        f'<defs><filter id="rough"><feTurbulence type="fractalNoise" '
        f'baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/>'
        f'<feColorMatrix values="0 0 0 0 0.7 '
        f'0 0 0 0 0.65 '
        f'0 0 0 0 0.55 '
        f'0 0 0 0.06 0"/></filter></defs>\n'
        f'<rect width="{W}" height="{H}" filter="url(#rough)"/>\n'
        # frame border — sketchy
        + sk_rect(4, 4, W-8, H-8, strokes=2, weight=2.0, color=GRAPH_D, opacity=0.85)
        + '\n'
    )


def frame_close():
    return '</svg>'


# ── individual frames ────────────────────────────────────────────────────────
def frame_1():
    """Cold open · Delhi 1880s title card."""
    parts = [frame_open()]
    # darken to near-black with hatch
    parts.append(f'<rect x="4" y="4" width="{W-8}" height="{H-8}" fill="#1a160e" opacity="0.92"/>')
    parts.append(f'<text x="{W/2}" y="{H*0.42}" text-anchor="middle" font-family="Georgia" font-style="italic" font-size="26" fill="{PAPER}" letter-spacing="2">Delhi. 1880s.</text>')
    parts.append(f'<text x="{W/2}" y="{H*0.58}" text-anchor="middle" font-family="Georgia" font-style="italic" font-size="15" fill="#a8a08c" letter-spacing="1">The British have a problem.</text>')
    parts.append(frame_close())
    return ''.join(parts)


def frame_2():
    """Wide establishing — empty dark room with single seated figure."""
    parts = [frame_open()]
    # back wall
    parts.append(sk_wood_wall(40, 60, W-80, 180, n_panels=7))
    # floor line
    parts.append(sk_line(0, 248, W, 248, strokes=3, weight=1.4, color=GRAPH_M))
    # ceiling lamp
    parts.append(sk_ceiling_lamp(W/2, 56))
    # light cone
    parts.append(sk_light_cone(W/2, 60, 270, 24, 110))
    # chair + figure
    parts.append(sk_chair(W/2, 235, scale=1.0))
    parts.append(sk_seated_figure(W/2, 200, scale=1.0))
    # subtle shadow under figure (hatching)
    parts.append(hatch(W/2 - 50, 245, 100, 14, angle=20, spacing=3, opacity=0.35))
    # large dark walls on sides (hatched)
    parts.append(hatch(8, 60, 50, 240, angle=70, spacing=4, weight=0.7, opacity=0.4))
    parts.append(hatch(W-58, 60, 50, 240, angle=110, spacing=4, weight=0.7, opacity=0.4))
    parts.append(frame_close())
    return ''.join(parts)


def frame_3():
    """Medium shot · Ahmed in black · side light."""
    parts = [frame_open()]
    # vertical wood lines behind
    for px in [120, 230, 340, 450]:
        parts.append(sk_line(px + jitter(0, 2), 20, px + jitter(0, 2), H, strokes=2, weight=0.7, color=GRAPH_L, opacity=0.55))
    # heavy shadow on right (back-light from left)
    parts.append(hatch(W*0.55, 0, W*0.45, H, angle=110, spacing=3, weight=0.9, opacity=0.55, color=GRAPH_M))
    # torso/shoulders large silhouette
    parts.append(sk_path(f'M {W*0.30} {H} L {W*0.34} {H*0.55} Q {W*0.50} {H*0.42} {W*0.66} {H*0.55} L {W*0.70} {H} Z', strokes=3, weight=2.0, color=GRAPH_D, opacity=0.85))
    # solid fill on torso (very dark via hatch)
    parts.append(hatch(W*0.32, H*0.55, W*0.36, H*0.50, angle=60, spacing=2.2, weight=1.0, opacity=0.65, color=GRAPH_D))
    # head
    parts.append(sk_ellipse(W*0.50, H*0.39, 40, 50, strokes=4, weight=1.6, color=GRAPH_D, opacity=0.85))
    # hatch the head darker
    parts.append(hatch(W*0.45, H*0.30, 50, 70, angle=50, spacing=2.5, opacity=0.55, color=GRAPH_D))
    # eyes — small marks
    parts.append(f'<ellipse cx="{W*0.475}" cy="{H*0.40}" rx="3" ry="2" fill="{PAPER}" opacity="0.9"/>')
    parts.append(f'<ellipse cx="{W*0.525}" cy="{H*0.40}" rx="3" ry="2" fill="{PAPER}" opacity="0.9"/>')
    # arrow indicating light direction
    parts.append(sk_line(20, 30, 70, 70, strokes=2, weight=1.2, color=GRAPH_L, opacity=0.7))
    parts.append(sk_line(60, 65, 70, 70, strokes=2, weight=1.2, color=GRAPH_L, opacity=0.7))
    parts.append(sk_line(70, 70, 65, 60, strokes=2, weight=1.2, color=GRAPH_L, opacity=0.7))
    parts.append(sk_text(82, 38, 'LIGHT', 9, GRAPH_L, 'Helvetica', anchor='start'))
    parts.append(frame_close())
    return ''.join(parts)


def frame_4():
    """Insert · coin dropped on wood."""
    parts = [frame_open()]
    # wood grain — horizontal wavy lines
    for y in [40, 90, 140, 190, 240, 290]:
        # generate a wavy line
        d_parts = [f'M 10 {y + jitter(0, 2)}']
        for x in range(60, W, 50):
            d_parts.append(f'Q {x-25} {y + jitter(0,3)} {x} {y + jitter(0,2)}')
        d = ' '.join(d_parts)
        parts.append(sk_path(d, strokes=1, weight=0.6, color=GRAPH_L, opacity=0.45))
    # shadow under coin
    parts.append(hatch(W/2 - 80, H*0.62, 160, 30, angle=15, spacing=2.5, opacity=0.45, color=GRAPH_M))
    # coin — circle, slightly off-center
    parts.append(sk_ellipse(W/2, H*0.55, 55, 55, strokes=4, weight=1.8, color=GRAPH_D, opacity=0.85))
    parts.append(sk_ellipse(W/2, H*0.55, 48, 48, strokes=2, weight=0.9, color=GRAPH_M, opacity=0.6))
    parts.append(sk_text(W/2, H*0.57, '1 rupee', 13, GRAPH_D, italic=True))
    # hand outline retreating top — partial silhouette
    parts.append(sk_path(f'M {W*0.32} 0 Q {W*0.35} 60 {W*0.40} 100 Q {W*0.46} 130 {W*0.54} 130 Q {W*0.64} 130 {W*0.66} 100 Q {W*0.70} 60 {W*0.68} 0', strokes=3, weight=1.5, color=GRAPH_D, opacity=0.75))
    parts.append(frame_close())
    return ''.join(parts)


def frame_5():
    """The cobra shadow on the wall."""
    parts = [frame_open()]
    parts.append(sk_wood_wall(40, 60, W-80, 180, n_panels=7))
    parts.append(sk_line(0, 248, W, 248, strokes=3, weight=1.4, color=GRAPH_M))
    parts.append(sk_ceiling_lamp(W/2, 56))
    parts.append(sk_light_cone(W/2, 60, 270, 24, 110))
    # COBRA SHADOW — large sinuous shape on the wall
    cobra_d = f'M 60 {H*0.42} Q 160 {H*0.32} 250 {H*0.42} T 430 {H*0.42} Q 500 {H*0.36} 540 {H*0.46}'
    # thick stroke
    parts.append(sk_path(cobra_d, strokes=4, weight=14, color=GRAPH_D, opacity=0.6))
    parts.append(sk_path(cobra_d, strokes=2, weight=10, color=GRAPH_D, opacity=0.4))
    # cobra head — wedge at the end
    parts.append(sk_path(f'M 540 {H*0.46} L 560 {H*0.42} L 555 {H*0.48} Z', strokes=2, weight=2, color=GRAPH_D, opacity=0.7))
    # chair + figure (smaller, unchanged from F2)
    parts.append(sk_chair(W/2, 235, scale=1.0))
    parts.append(sk_seated_figure(W/2, 200, scale=1.0))
    # annotation
    parts.append(sk_text(85, H*0.38, 'shadow only · 1 sec pass', 9, '#a04030', 'Helvetica', anchor='start'))
    parts.append(frame_close())
    return ''.join(parts)


def frame_6():
    """Cages — implied. Dark room with bars and distant light."""
    parts = [frame_open()]
    # whole frame darker
    parts.append(f'<rect x="4" y="4" width="{W-8}" height="{H-8}" fill="#1a160e" opacity="0.78"/>')
    # distant window of light
    parts.append(f'<rect x="{W*0.62}" y="{H*0.20}" width="{W*0.22}" height="{H*0.35}" fill="#e8dcb4" opacity="0.55"/>')
    parts.append(sk_rect(W*0.62, H*0.20, W*0.22, H*0.35, strokes=2, weight=1.0, color=GRAPH_L, opacity=0.6))
    # window cross
    parts.append(sk_line(W*0.73, H*0.20, W*0.73, H*0.55, strokes=2, weight=0.8, color=GRAPH_M, opacity=0.7))
    parts.append(sk_line(W*0.62, H*0.375, W*0.84, H*0.375, strokes=2, weight=0.8, color=GRAPH_M, opacity=0.7))
    # cage bars — foreground
    for x in [40, 90, 140, 190, 240, 290, 340]:
        parts.append(sk_line(x, H*0.30, x, H*0.95, strokes=3, weight=2.6, color=GRAPH_D, opacity=0.95))
    # top of cage
    parts.append(sk_line(20, H*0.30, 360, H*0.30, strokes=3, weight=3.0, color=GRAPH_D, opacity=0.95))
    # coiled snake inside (hint only)
    parts.append(sk_path(f'M 110 {H*0.70} Q 145 {H*0.62} 175 {H*0.70} T 235 {H*0.70}', strokes=3, weight=2, color=GRAPH_L, opacity=0.6))
    parts.append(sk_path(f'M 100 {H*0.78} Q 140 {H*0.72} 180 {H*0.78} T 250 {H*0.78}', strokes=2, weight=1.5, color=GRAPH_L, opacity=0.5))
    parts.append(frame_close())
    return ''.join(parts)


def frame_7():
    """Close-up · Ahmed face — dramatic side light."""
    parts = [frame_open()]
    # large face fills frame
    parts.append(sk_ellipse(W*0.50, H*0.55, 200, 220, strokes=5, weight=2.0, color=GRAPH_D, opacity=0.9))
    # half in deep shadow (left)
    parts.append(hatch(0, 0, W*0.45, H, angle=60, spacing=2, weight=1.0, opacity=0.7, color=GRAPH_D))
    # half lit (right) — lighter hatch
    parts.append(hatch(W*0.45, 0, W*0.55, H, angle=120, spacing=4, weight=0.7, opacity=0.30, color=GRAPH_M))
    # brow lines
    parts.append(sk_path(f'M {W*0.35} {H*0.42} Q {W*0.42} {H*0.40} {W*0.48} {H*0.42}', strokes=3, weight=2, color=PAPER, opacity=0.95))
    parts.append(sk_path(f'M {W*0.52} {H*0.42} Q {W*0.58} {H*0.40} {W*0.65} {H*0.42}', strokes=3, weight=2, color=PAPER, opacity=0.95))
    # eyes — big and sharp
    parts.append(sk_ellipse(W*0.41, H*0.48, 15, 9, strokes=3, weight=1.8, color=GRAPH_D, opacity=0.9))
    parts.append(sk_ellipse(W*0.59, H*0.48, 15, 9, strokes=3, weight=1.8, color=GRAPH_D, opacity=0.9))
    parts.append(f'<ellipse cx="{W*0.41}" cy="{H*0.48}" rx="13" ry="7" fill="{PAPER}" opacity="0.92"/>')
    parts.append(f'<ellipse cx="{W*0.59}" cy="{H*0.48}" rx="13" ry="7" fill="{PAPER}" opacity="0.92"/>')
    parts.append(f'<ellipse cx="{W*0.41}" cy="{H*0.49}" rx="6" ry="6" fill="{GRAPH_D}" opacity="0.95"/>')
    parts.append(f'<ellipse cx="{W*0.59}" cy="{H*0.49}" rx="6" ry="6" fill="{GRAPH_D}" opacity="0.95"/>')
    # nose suggestion — single line
    parts.append(sk_line(W*0.50, H*0.50, W*0.51, H*0.66, strokes=2, weight=1.5, color=GRAPH_D, opacity=0.7))
    # mouth
    parts.append(sk_path(f'M {W*0.43} {H*0.78} Q {W*0.50} {H*0.80} {W*0.57} {H*0.78}', strokes=3, weight=1.8, color=GRAPH_D, opacity=0.85))
    parts.append(frame_close())
    return ''.join(parts)


def frame_8():
    """Transition · Detroit 1995."""
    parts = [frame_open()]
    parts.append(f'<rect x="4" y="4" width="{W-8}" height="{H-8}" fill="#1a160e" opacity="0.92"/>')
    parts.append(f'<text x="{W/2}" y="{H*0.50}" text-anchor="middle" font-family="Georgia" font-style="italic" font-size="26" fill="{PAPER}" letter-spacing="2">Detroit. 1995.</text>')
    parts.append(sk_line(W*0.40, H*0.60, W*0.60, H*0.60, strokes=2, weight=0.7, color='#a8a08c', opacity=0.6))
    parts.append(frame_close())
    return ''.join(parts)


def frame_9():
    """Same wide, transformed — white shirt + pill bottle."""
    parts = [frame_open()]
    # slight cool tint over paper
    parts.append(f'<rect x="4" y="4" width="{W-8}" height="{H-8}" fill="#aab8c0" opacity="0.15"/>')
    parts.append(sk_wood_wall(40, 60, W-80, 180, n_panels=7))
    parts.append(sk_line(0, 248, W, 248, strokes=3, weight=1.4, color=GRAPH_M))
    parts.append(sk_ceiling_lamp(W/2, 56))
    parts.append(sk_light_cone(W/2, 60, 270, 24, 110))
    parts.append(sk_chair(W/2, 235, scale=1.0))
    # figure NOW LIGHT — drawn without heavy fill
    parts.append(sk_ellipse(W/2, 140, 14, 17, strokes=4, weight=1.3, color=GRAPH_M, opacity=0.78))
    parts.append(sk_line(W/2 - 5, 157, W/2 - 8, 170, strokes=2, weight=1.1, color=GRAPH_M))
    parts.append(sk_line(W/2 + 5, 157, W/2 + 8, 170, strokes=2, weight=1.1, color=GRAPH_M))
    # torso outlined but not filled
    parts.append(sk_line(W/2 - 8, 170, W/2 - 22, 205, strokes=2, weight=1.3, color=GRAPH_M))
    parts.append(sk_line(W/2 + 8, 170, W/2 + 22, 205, strokes=2, weight=1.3, color=GRAPH_M))
    parts.append(sk_line(W/2 - 22, 205, W/2 - 20, 235, strokes=2, weight=1.3, color=GRAPH_M))
    parts.append(sk_line(W/2 + 22, 205, W/2 + 20, 235, strokes=2, weight=1.3, color=GRAPH_M))
    parts.append(sk_line(W/2 - 20, 235, W/2 + 20, 235, strokes=2, weight=1.2, color=GRAPH_M))
    parts.append(sk_line(W/2 - 22, 205, W/2 - 18, 232, strokes=2, weight=1.1, color=GRAPH_M, opacity=0.7))
    parts.append(sk_line(W/2 + 22, 205, W/2 + 18, 232, strokes=2, weight=1.1, color=GRAPH_M, opacity=0.7))
    # small table + bottle to the right
    parts.append(sk_line(W*0.58, 215, W*0.66, 215, strokes=2, weight=1.2, color=GRAPH_M))
    parts.append(sk_line(W*0.59, 215, W*0.59, 248, strokes=2, weight=1.0, color=GRAPH_M))
    parts.append(sk_line(W*0.65, 215, W*0.65, 248, strokes=2, weight=1.0, color=GRAPH_M))
    # pill bottle on table
    parts.append(sk_rect(W*0.605, 198, 14, 18, strokes=2, weight=1.2, color=GRAPH_D, opacity=0.85))
    parts.append(sk_line(W*0.605, 202, W*0.605 + 14, 202, strokes=2, weight=1.4, color=GRAPH_D))
    # side hatching lighter than F2
    parts.append(hatch(8, 60, 35, 240, angle=70, spacing=5, weight=0.6, opacity=0.25))
    parts.append(hatch(W-43, 60, 35, 240, angle=110, spacing=5, weight=0.6, opacity=0.25))
    parts.append(frame_close())
    return ''.join(parts)


def frame_10():
    """Pill bottle insert · macro top-down."""
    parts = [frame_open()]
    # wood grain
    for y in [40, 100, 160, 220, 290]:
        d_parts = [f'M 10 {y + jitter(0, 2)}']
        for x in range(60, W, 50):
            d_parts.append(f'Q {x-25} {y + jitter(0,3)} {x} {y + jitter(0,2)}')
        parts.append(sk_path(' '.join(d_parts), strokes=1, weight=0.6, color=GRAPH_L, opacity=0.45))
    # diagonal shadow
    parts.append(hatch(W*0.55, H*0.55, W*0.45, H*0.45, angle=25, spacing=3, opacity=0.5, color=GRAPH_M))
    # bottle body
    parts.append(sk_rect(W*0.42, H*0.30, W*0.16, H*0.42, strokes=3, weight=2.0, color=GRAPH_D, opacity=0.9))
    # cap
    parts.append(sk_rect(W*0.42, H*0.30, W*0.16, H*0.10, strokes=3, weight=2.0, color=GRAPH_D, opacity=0.9))
    parts.append(hatch(W*0.42, H*0.30, W*0.16, H*0.10, angle=45, spacing=2.5, weight=1.0, opacity=0.7, color=GRAPH_D))
    # label
    parts.append(sk_rect(W*0.44, H*0.46, W*0.12, H*0.22, strokes=2, weight=1.2, color=GRAPH_M))
    parts.append(sk_line(W*0.455, H*0.52, W*0.545, H*0.52, strokes=2, weight=0.8, color=GRAPH_M, opacity=0.6))
    parts.append(sk_line(W*0.455, H*0.56, W*0.545, H*0.56, strokes=2, weight=0.8, color=GRAPH_M, opacity=0.6))
    parts.append(sk_line(W*0.455, H*0.60, W*0.535, H*0.60, strokes=2, weight=0.8, color=GRAPH_M, opacity=0.6))
    parts.append(sk_line(W*0.455, H*0.64, W*0.540, H*0.64, strokes=2, weight=0.8, color=GRAPH_M, opacity=0.6))
    parts.append(frame_close())
    return ''.join(parts)


def frame_11():
    """Slow dolly · two side-by-side."""
    parts = [frame_open()]
    # START miniature (left, faint)
    parts.append(sk_rect(30, 50, 200, 200, strokes=2, weight=1.0, color=GRAPH_L, opacity=0.6))
    parts.append(sk_text(130, 42, 'START', 10, GRAPH_L, 'Helvetica'))
    # small figure inside
    parts.append(sk_seated_figure(130, 175, scale=0.7, dark=False))
    parts.append(sk_chair(130, 220, scale=0.7))
    # ARROW
    parts.append(sk_line(250, H/2, 340, H/2, strokes=3, weight=2.4, color='#a04030', opacity=0.85))
    parts.append(sk_line(335, H/2 - 10, 350, H/2, strokes=3, weight=2.4, color='#a04030', opacity=0.85))
    parts.append(sk_line(335, H/2 + 10, 350, H/2, strokes=3, weight=2.4, color='#a04030', opacity=0.85))
    parts.append(sk_text(297, H/2 - 18, 'PUSH IN', 10, '#a04030', 'Helvetica'))
    parts.append(sk_text(297, H/2 + 28, '8 sec', 9, '#a04030', 'Helvetica', italic=True))
    # END frame (right, larger)
    parts.append(sk_rect(360, 25, 215, 280, strokes=3, weight=1.8, color=GRAPH_D, opacity=0.85))
    parts.append(sk_text(467, 18, 'END', 10, GRAPH_D, 'Helvetica'))
    parts.append(sk_seated_figure(467, 175, scale=1.05, dark=False))
    parts.append(sk_chair(467, 220, scale=1.05))
    parts.append(frame_close())
    return ''.join(parts)


def frame_12():
    """Insert · doctor signing prescription."""
    parts = [frame_open()]
    # wood grain
    for y in [40, 100, 160, 240, 300]:
        d_parts = [f'M 10 {y + jitter(0, 2)}']
        for x in range(60, W, 50):
            d_parts.append(f'Q {x-25} {y + jitter(0,3)} {x} {y + jitter(0,2)}')
        parts.append(sk_path(' '.join(d_parts), strokes=1, weight=0.5, color=GRAPH_L, opacity=0.4))
    # prescription pad
    parts.append(sk_rect(W*0.22, H*0.22, W*0.42, H*0.55, strokes=3, weight=1.8, color=GRAPH_D, opacity=0.85))
    # pad lines
    parts.append(sk_line(W*0.24, H*0.30, W*0.62, H*0.30, strokes=2, weight=0.9, color=GRAPH_M))
    for ry in [H*0.36, H*0.43, H*0.50, H*0.57, H*0.64]:
        parts.append(sk_line(W*0.24, ry, W*0.58, ry, strokes=1, weight=0.5, color=GRAPH_M, opacity=0.5))
    parts.append(sk_text(W*0.27, H*0.295, 'Rx', 14, GRAPH_D, italic=True, anchor='start'))
    # signature scrawl
    parts.append(sk_path(f'M {W*0.36} {H*0.72} Q {W*0.40} {H*0.66} {W*0.44} {H*0.72} T {W*0.55} {H*0.70}', strokes=3, weight=2.4, color=GRAPH_D, opacity=0.85))
    # hand outline
    parts.append(sk_path(f'M {W*0.66} {H*0.05} Q {W*0.70} {H*0.30} {W*0.72} {H*0.45} Q {W*0.74} {H*0.58} {W*0.70} {H*0.66} Q {W*0.65} {H*0.72} {W*0.58} {H*0.70} Q {W*0.55} {H*0.55} {W*0.58} {H*0.30} Q {W*0.62} {H*0.10} {W*0.66} {H*0.05}', strokes=3, weight=1.8, color=GRAPH_D, opacity=0.85))
    # pen
    parts.append(sk_line(W*0.52, H*0.70, W*0.62, H*0.50, strokes=3, weight=3.5, color=GRAPH_D))
    parts.append(frame_close())
    return ''.join(parts)


def frame_13():
    """Close-up · white shirt · cooler light."""
    parts = [frame_open()]
    # cool tint
    parts.append(f'<rect x="4" y="4" width="{W-8}" height="{H-8}" fill="#aab8c0" opacity="0.18"/>')
    # face
    parts.append(sk_ellipse(W*0.50, H*0.55, 200, 220, strokes=5, weight=2.0, color=GRAPH_M, opacity=0.85))
    # half shadow but LIGHTER than F7
    parts.append(hatch(0, 0, W*0.45, H, angle=60, spacing=3, weight=0.8, opacity=0.45, color=GRAPH_M))
    parts.append(hatch(W*0.45, 0, W*0.55, H, angle=120, spacing=6, weight=0.5, opacity=0.18, color=GRAPH_M))
    # white shirt collar
    parts.append(sk_path(f'M {W*0.22} {H} L {W*0.50} {H*0.82} L {W*0.78} {H} Z', strokes=3, weight=1.8, color=GRAPH_M, opacity=0.85))
    parts.append(f'<path d="M {W*0.22} {H} L {W*0.50} {H*0.82} L {W*0.78} {H} Z" fill="{PAPER}" opacity="0.4"/>')
    # brows
    parts.append(sk_path(f'M {W*0.35} {H*0.42} Q {W*0.42} {H*0.40} {W*0.48} {H*0.42}', strokes=3, weight=2, color=GRAPH_D, opacity=0.9))
    parts.append(sk_path(f'M {W*0.52} {H*0.42} Q {W*0.58} {H*0.40} {W*0.65} {H*0.42}', strokes=3, weight=2, color=GRAPH_D, opacity=0.9))
    # eyes — same as F7 (visual rhyme)
    parts.append(sk_ellipse(W*0.41, H*0.48, 15, 9, strokes=3, weight=1.8, color=GRAPH_D, opacity=0.9))
    parts.append(sk_ellipse(W*0.59, H*0.48, 15, 9, strokes=3, weight=1.8, color=GRAPH_D, opacity=0.9))
    parts.append(f'<ellipse cx="{W*0.41}" cy="{H*0.48}" rx="13" ry="7" fill="{PAPER}" opacity="0.92"/>')
    parts.append(f'<ellipse cx="{W*0.59}" cy="{H*0.48}" rx="13" ry="7" fill="{PAPER}" opacity="0.92"/>')
    parts.append(f'<ellipse cx="{W*0.41}" cy="{H*0.49}" rx="6" ry="6" fill="{GRAPH_D}" opacity="0.95"/>')
    parts.append(f'<ellipse cx="{W*0.59}" cy="{H*0.49}" rx="6" ry="6" fill="{GRAPH_D}" opacity="0.95"/>')
    parts.append(sk_line(W*0.50, H*0.50, W*0.51, H*0.66, strokes=2, weight=1.5, color=GRAPH_D, opacity=0.7))
    parts.append(sk_path(f'M {W*0.43} {H*0.78} Q {W*0.50} {H*0.80} {W*0.57} {H*0.78}', strokes=3, weight=1.8, color=GRAPH_D, opacity=0.85))
    parts.append(frame_close())
    return ''.join(parts)


def frame_14():
    """Book in hands."""
    parts = [frame_open()]
    # warm soft light wash
    parts.append(f'<rect x="4" y="4" width="{W-8}" height="{H-8}" fill="#f0d4a0" opacity="0.18"/>')
    # hands (very loose)
    parts.append(sk_path(f'M 50 {H*0.85} Q 80 {H*0.65} 130 {H*0.62} L 180 {H*0.62} L 180 {H*0.92} Q 110 {H*0.95} 50 {H*0.92} Z', strokes=3, weight=1.8, color='#9a7b5a', opacity=0.85))
    parts.append(f'<path d="M 50 {H*0.85} Q 80 {H*0.65} 130 {H*0.62} L 180 {H*0.62} L 180 {H*0.92} Q 110 {H*0.95} 50 {H*0.92} Z" fill="#c9a880" opacity="0.55"/>')
    parts.append(sk_path(f'M {W-50} {H*0.85} Q {W-80} {H*0.65} {W-130} {H*0.62} L {W-180} {H*0.62} L {W-180} {H*0.92} Q {W-110} {H*0.95} {W-50} {H*0.92} Z', strokes=3, weight=1.8, color='#9a7b5a', opacity=0.85))
    parts.append(f'<path d="M {W-50} {H*0.85} Q {W-80} {H*0.65} {W-130} {H*0.62} L {W-180} {H*0.62} L {W-180} {H*0.92} Q {W-110} {H*0.95} {W-50} {H*0.92} Z" fill="#c9a880" opacity="0.55"/>')
    # book
    book_x, book_y, book_w, book_h = W*0.27, H*0.15, W*0.46, H*0.70
    parts.append(f'<rect x="{book_x}" y="{book_y}" width="{book_w}" height="{book_h}" fill="{PAPER}" opacity="0.96"/>')
    parts.append(sk_rect(book_x, book_y, book_w, book_h, strokes=3, weight=2.5, color=GRAPH_D))
    # top black bar
    parts.append(f'<rect x="{book_x}" y="{book_y}" width="{book_w}" height="6" fill="{GRAPH_D}"/>')
    # title stack
    cx = book_x + book_w/2
    parts.append(f'<text x="{cx}" y="{book_y + book_h*0.18}" text-anchor="middle" font-family="Helvetica" font-weight="700" font-size="13" fill="#888" letter-spacing="1">MORE</text>')
    parts.append(f'<text x="{cx}" y="{book_y + book_h*0.30}" text-anchor="middle" font-family="Helvetica" font-weight="700" font-size="16" fill="{GRAPH_D}" letter-spacing="1">SOLUTIONS</text>')
    parts.append(f'<text x="{cx}" y="{book_y + book_h*0.40}" text-anchor="middle" font-family="Helvetica" font-weight="700" font-size="13" fill="#888">=</text>')
    parts.append(f'<text x="{cx}" y="{book_y + book_h*0.52}" text-anchor="middle" font-family="Helvetica" font-weight="700" font-size="13" fill="#888" letter-spacing="1">MORE</text>')
    parts.append(f'<text x="{cx}" y="{book_y + book_h*0.64}" text-anchor="middle" font-family="Helvetica" font-weight="700" font-size="16" fill="{GRAPH_D}" letter-spacing="1">PROBLEMS</text>')
    parts.append(sk_line(book_x + book_w*0.20, book_y + book_h*0.71, book_x + book_w*0.80, book_y + book_h*0.71, strokes=2, weight=0.6, color=GRAPH_L))
    parts.append(f'<text x="{cx}" y="{book_y + book_h*0.78}" text-anchor="middle" font-family="Georgia" font-style="italic" font-size="8" fill="#666">Why Every Solution</text>')
    parts.append(f'<text x="{cx}" y="{book_y + book_h*0.84}" text-anchor="middle" font-family="Georgia" font-style="italic" font-size="8" fill="#666">Creates the Next Problem</text>')
    # bottom black bar
    parts.append(f'<rect x="{book_x}" y="{book_y + book_h - 14}" width="{book_w}" height="14" fill="{GRAPH_D}"/>')
    parts.append(f'<text x="{cx}" y="{book_y + book_h - 4}" text-anchor="middle" font-family="Helvetica" font-weight="700" font-size="9" fill="{PAPER}" letter-spacing="2">AHMED HAFDI</text>')
    parts.append(frame_close())
    return ''.join(parts)


def frame_15():
    """End card."""
    parts = [frame_open()]
    parts.append(f'<rect x="4" y="4" width="{W-8}" height="{H-8}" fill="#1a160e" opacity="0.95"/>')
    parts.append(f'<text x="{W/2}" y="{H*0.45}" text-anchor="middle" font-family="Helvetica" font-weight="700" font-size="16" fill="{PAPER}" letter-spacing="4">OUT NOW ON AMAZON</text>')
    parts.append(sk_line(W*0.35, H*0.52, W*0.65, H*0.52, strokes=2, weight=0.7, color='#a8a08c', opacity=0.6))
    parts.append(f'<text x="{W/2}" y="{H*0.62}" text-anchor="middle" font-family="Georgia" font-style="italic" font-size="12" fill="#a8a08c" letter-spacing="1">moresolutions-moreproblems.com</text>')
    parts.append(frame_close())
    return ''.join(parts)


# ── frame metadata ───────────────────────────────────────────────────────────
FRAMES = [
    ('1', '0:00–0:05', 'Cold open · Title card', frame_1,
     'static · type only — no music · faint city ambient + distant hiss', None),
    ('2', '0:05–0:18', 'Establishing wide · the room', frame_2,
     'static · locked-off · wide — 80% room, 20% figure', None),
    ('3', '0:18–0:25', 'Medium · Ahmed in black', frame_3,
     'eye-level · side light from camera-left · half face in shadow',
     '"Too many cobras. People are dying. So the government does what any rational government would do. It offers a bounty."'),
    ('4', '0:25–0:30', 'Insert · the bounty', frame_4,
     'top-down macro · coin sharp, hand soft, wood grain sharp', None),
    ('5', '0:30–0:45', 'The shadow', frame_5,
     'same wide as Frame 2 — shadow only · 1 sec pass · sound: hiss + scrape',
     '"Then someone notices something. It’s easier to breed cobras than to hunt them."'),
    ('6', '0:45–0:50', 'Cages (implied)', frame_6,
     'low angle · slow push-in · cage felt more than seen', None),
    ('7', '0:50–0:55', 'Close-up · "the same story"', frame_7,
     'tight close-up · eye-level · eyes carry the shot',
     '"This was 1880. Read the next page in any history book and you’ll find the same story under different names."'),
    ('8', '0:55–1:05', 'Transition · music in', frame_8,
     'black · 3 full seconds · first music cue · sustained low synth', None),
    ('9', '1:05–1:15', 'Same wide · transformed', frame_9,
     'IDENTICAL framing to Frame 2 · white shirt · pill bottle on side table',
     None),
    ('10', '1:15–1:20', 'Insert · the prescription', frame_10,
     'top-down macro · same scale as Frame 4 (coin → pill)', None),
    ('11', '1:20–1:35', 'Slow dolly · 12 inches over 8 sec', frame_11,
     'camera dollies forward · figure does not move · faint hospital monitor', None),
    ('12', '1:35–1:40', 'Insert · doctor signs prescription', frame_12,
     'top-down macro · echo of Frame 4 · soft pen scratch', None),
    ('13', '1:40–1:45', '"It’s mathematics."', frame_13,
     'identical framing to Frame 7 — black shirt becomes white · 1880 → 1995',
     '"Two centuries between Delhi and Detroit. The architecture of the catastrophe is identical. This isn’t bad luck. It’s mathematics."'),
    ('14', '1:45–1:55', 'Book in hands', frame_14,
     'static · eye-level · slow dolly in · soft natural window light',
     None),
    ('15', '1:55–2:00', 'End card', frame_15,
     'static · 4 sec hold · music resolves to silence',
     None),
]


# ── HTML output ──────────────────────────────────────────────────────────────
def render_html():
    css = """
    body { background:#d9d3bd; margin:0; padding:36px 24px; font-family:Georgia, serif; color:#2a2a2a; }
    .wrap { max-width:1280px; margin:0 auto; }
    h1 { font-size:30px; margin:0 0 4px; }
    h1 small { display:block; font-weight:400; font-style:italic; color:#6a614c; font-size:14px; margin-top:6px; }
    .meta { color:#5a5040; font-size:13px; margin-bottom:30px; padding-bottom:18px; border-bottom:1px solid #b8ad8e; }
    .label { font-family:Helvetica, Arial, sans-serif; font-size:11px; letter-spacing:3px; text-transform:uppercase; color:#5a5040; margin:30px 0 14px; padding-left:12px; border-left:3px solid #2a2a2a; }
    .grid { display:grid; grid-template-columns:repeat(3, 1fr); gap:22px; }
    @media (max-width:980px){ .grid { grid-template-columns:repeat(2, 1fr); } }
    @media (max-width:640px){ .grid { grid-template-columns:1fr; } }
    .panel { background:#ece6d4; padding:16px; box-shadow:0 2px 4px rgba(0,0,0,.12); border:1px solid #b8ad8e; }
    .fno { font-family:Helvetica, Arial, sans-serif; font-size:10px; letter-spacing:2px; color:#7a6e5a; }
    .ftitle { font-family:Helvetica, Arial, sans-serif; font-size:13px; font-weight:700; margin:2px 0 10px; color:#2a2a2a; }
    svg.shot { display:block; width:100%; height:auto; background:#ece6d4; }
    .notes { font-size:11.5px; line-height:1.55; color:#3a3326; margin-top:10px; font-family:Helvetica, Arial, sans-serif; }
    .vo { font-style:italic; color:#2a2a2a; margin-top:9px; padding:9px 11px; background:#dfd7be; border-left:2px solid #5a5040; font-size:11.5px; font-family:Georgia, serif; }
    .rhyme { margin-top:30px; padding:16px 20px; background:#1a160e; color:#ece6d4; font-size:12px; line-height:1.7; font-family:Helvetica, Arial, sans-serif; }
    .rhyme h3 { margin:0 0 8px; font-size:12px; letter-spacing:2px; text-transform:uppercase; color:#ece6d4; }
    """
    html = ['<title>Storyboard · sketch · More Solutions = More Problems</title>']
    html.append(f'<style>{css}</style>')
    html.append('<div class="wrap">')
    html.append('<h1>MORE SOLUTIONS = MORE PROBLEMS — book trailer storyboard <small>15 frames · 2 minutes · pencil-sketch treatment · directed by Ahmed Hafdi</small></h1>')
    html.append('<div class="meta">Aspect 16:9 · two vignettes (Delhi 1880s → Detroit 1995) plus reveal · single subject, controlled lighting, no CGI · cobra implied through shadow and sound design.</div>')

    # Vignette 1
    html.append('<div class="label">Vignette 1 — The Cobra (0:00 – 0:55)</div>')
    html.append('<div class="grid">')
    for fno, time, title, fn, note, vo in FRAMES[:8]:
        html.append('<div class="panel">')
        html.append(f'<div class="fno">FRAME {fno} · {time}</div>')
        html.append(f'<div class="ftitle">{title}</div>')
        html.append(fn())
        html.append(f'<div class="notes">{note}</div>')
        if vo: html.append(f'<div class="vo">{vo}</div>')
        html.append('</div>')
    html.append('</div>')

    # Vignette 2
    html.append('<div class="label">Vignette 2 — The Medicine (1:05 – 1:45)</div>')
    html.append('<div class="grid">')
    for fno, time, title, fn, note, vo in FRAMES[8:13]:
        html.append('<div class="panel">')
        html.append(f'<div class="fno">FRAME {fno} · {time}</div>')
        html.append(f'<div class="ftitle">{title}</div>')
        html.append(fn())
        html.append(f'<div class="notes">{note}</div>')
        if vo: html.append(f'<div class="vo">{vo}</div>')
        html.append('</div>')
    html.append('</div>')

    # Reveal
    html.append('<div class="label">Reveal (1:45 – 2:00)</div>')
    html.append('<div class="grid">')
    for fno, time, title, fn, note, vo in FRAMES[13:]:
        html.append('<div class="panel">')
        html.append(f'<div class="fno">FRAME {fno} · {time}</div>')
        html.append(f'<div class="ftitle">{title}</div>')
        html.append(fn())
        html.append(f'<div class="notes">{note}</div>')
        if vo: html.append(f'<div class="vo">{vo}</div>')
        html.append('</div>')
    html.append('</div>')

    html.append('<div class="rhyme">')
    html.append('<h3>The four visual rhymes</h3>')
    html.append('<b>FRAME 1 ↔ FRAME 8 ↔ FRAME 15</b> · the three black title cards — the trailer’s only moments of pure stillness<br>')
    html.append('<b>FRAME 2 ↔ FRAME 9</b> · identical wide composition · different century · the structural argument of the entire film<br>')
    html.append('<b>FRAME 4 ↔ FRAME 10 ↔ FRAME 12</b> · three top-down transactions · coin · pill bottle · signature · same composition, different solution<br>')
    html.append('<b>FRAME 7 ↔ FRAME 13</b> · identical close-up · black shirt → white shirt · 1880 → 1995')
    html.append('</div>')

    html.append('</div>')

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'storyboard_sketch.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html))
    print(f'Saved → {out}')


if __name__ == '__main__':
    render_html()
