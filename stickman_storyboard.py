"""Generate `storyboard_stickman.pdf` — the trailer storyboard rendered in
black-and-white stick-figure animation style.

Output: 17 pages (cover + 15 frames + shoot summary), A4 portrait, pure
black and white throughout. Designed to be printed and used on-set."""

import os, math
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import black, white, HexColor
from reportlab.pdfbase import pdfmetrics

# ── page geometry ────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4   # portrait
MARGIN = 0.6 * inch
FRAME_W = PAGE_W - 2 * MARGIN
FRAME_H = FRAME_W * 9 / 16   # 16:9
FRAME_X = MARGIN
FRAME_Y = PAGE_H - MARGIN - FRAME_H

INK = black
PAPER = white
GREY_TXT = HexColor('#444444')

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   'storyboard_stickman.pdf')


# ─────────────────────────────────────────────────────────────────────────────
# CHARACTER PRIMITIVES — stick figure built from thick rounded lines
# ─────────────────────────────────────────────────────────────────────────────

def _within_frame(x, y):
    """Convert a coordinate in our 'frame-local' space (origin bottom-left of
    the frame box) to a PDF-page coordinate."""
    return FRAME_X + x, FRAME_Y + y


def thick_line(c, x1, y1, x2, y2, w=8):
    c.setLineCap(1)
    c.setLineJoin(1)
    c.setLineWidth(w)
    c.setStrokeColor(INK)
    c.line(*_within_frame(x1, y1), *_within_frame(x2, y2))


def black_circle(c, x, y, r):
    c.setFillColor(INK)
    c.setStrokeColor(INK)
    c.setLineWidth(0)
    cx, cy = _within_frame(x, y)
    c.circle(cx, cy, r, stroke=0, fill=1)


def white_shape(c, draw_fn):
    c.setFillColor(PAPER)
    c.setStrokeColor(PAPER)
    draw_fn()
    c.setFillColor(INK)
    c.setStrokeColor(INK)


def white_ninja_eye(c, x, y, size=4, side='left'):
    """Draw a white angular eye in the ninja-stickman style."""
    cx, cy = _within_frame(x, y)
    p = c.beginPath()
    if side == 'left':
        # angled slit going down-right
        p.moveTo(cx - size, cy + size*0.4)
        p.lineTo(cx + size, cy)
        p.lineTo(cx + size, cy - size*0.4)
        p.lineTo(cx - size, cy - size*0.2)
    else:
        p.moveTo(cx + size, cy + size*0.4)
        p.lineTo(cx - size, cy)
        p.lineTo(cx - size, cy - size*0.4)
        p.lineTo(cx + size, cy - size*0.2)
    p.close()
    c.setFillColor(PAPER)
    c.setStrokeColor(PAPER)
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(INK)
    c.setStrokeColor(INK)


def stickman_seated(c, cx, base_y, scale=1.0, accessory=None):
    """A seated stick-figure character.
    `base_y` is the seat-of-the-chair level. Character built upward from there.
    `accessory`: None | 'pill' | 'doctor-coat' | 'pith-helmet'
    """
    s = scale
    line_w = 9 * s
    # head
    head_y = base_y + 78 * s
    black_circle(c, cx, head_y, 16 * s)

    # torso
    thick_line(c, cx, head_y - 16*s, cx, head_y - 48*s, w=line_w)

    # left arm (resting on thigh)
    thick_line(c, cx, head_y - 24*s, cx - 30*s, head_y - 52*s, w=line_w)
    # right arm
    thick_line(c, cx, head_y - 24*s, cx + 30*s, head_y - 52*s, w=line_w)

    # left thigh (out to knee)
    thick_line(c, cx - 4*s, head_y - 50*s, cx - 24*s, head_y - 70*s, w=line_w + 1)
    # right thigh
    thick_line(c, cx + 4*s, head_y - 50*s, cx + 24*s, head_y - 70*s, w=line_w + 1)
    # left shin (down)
    thick_line(c, cx - 24*s, head_y - 70*s, cx - 24*s, head_y - 100*s, w=line_w)
    # right shin
    thick_line(c, cx + 24*s, head_y - 70*s, cx + 24*s, head_y - 100*s, w=line_w)
    # left foot
    thick_line(c, cx - 24*s, head_y - 100*s, cx - 36*s, head_y - 100*s, w=line_w + 1)
    # right foot
    thick_line(c, cx + 24*s, head_y - 100*s, cx + 36*s, head_y - 100*s, w=line_w + 1)

    # hands (small circles)
    black_circle(c, cx - 30*s, head_y - 52*s, 5*s)
    black_circle(c, cx + 30*s, head_y - 52*s, 5*s)

    # eyes (white)
    white_ninja_eye(c, cx - 6*s, head_y + 2*s, size=4.5*s, side='left')
    white_ninja_eye(c, cx + 6*s, head_y + 2*s, size=4.5*s, side='right')

    # accessory layer (drawn last, on top)
    if accessory == 'pith-helmet':
        # white rectangular helmet on top of the head
        c.setFillColor(PAPER)
        c.setStrokeColor(INK)
        c.setLineWidth(2)
        hx, hy = _within_frame(cx, head_y + 14*s)
        c.rect(hx - 18*s, hy - 4*s, 36*s, 12*s, fill=1, stroke=1)
        # brim
        c.rect(hx - 22*s, hy - 7*s, 44*s, 4*s, fill=1, stroke=1)
        c.setFillColor(INK)
    elif accessory == 'doctor-coat':
        # white V on the chest indicating a coat
        c.setFillColor(PAPER)
        c.setStrokeColor(PAPER)
        p = c.beginPath()
        x0, y0 = _within_frame(cx, head_y - 16*s)
        # V-shape collar
        p.moveTo(x0 - 8*s, y0)
        p.lineTo(x0, y0 - 14*s)
        p.lineTo(x0 + 8*s, y0)
        p.lineTo(x0 + 5*s, y0 + 2*s)
        p.lineTo(x0, y0 - 6*s)
        p.lineTo(x0 - 5*s, y0 + 2*s)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
        # white badge / pocket square
        c.rect(*_within_frame(cx + 8*s, head_y - 34*s), 7*s, 7*s, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setStrokeColor(INK)


def stickman_standing(c, cx, base_y, scale=1.0, holds_book=False):
    """Standing stick-figure character.
    `base_y` is the ground level.
    """
    s = scale
    line_w = 9 * s
    head_y = base_y + 120 * s
    black_circle(c, cx, head_y, 16 * s)
    # torso
    thick_line(c, cx, head_y - 16*s, cx, head_y - 60*s, w=line_w)

    if holds_book:
        # arms forward holding the book
        thick_line(c, cx, head_y - 24*s, cx - 22*s, head_y - 38*s, w=line_w)
        thick_line(c, cx, head_y - 24*s, cx + 22*s, head_y - 38*s, w=line_w)
        # hands
        black_circle(c, cx - 22*s, head_y - 38*s, 5*s)
        black_circle(c, cx + 22*s, head_y - 38*s, 5*s)
    else:
        # arms down by sides
        thick_line(c, cx, head_y - 22*s, cx - 18*s, head_y - 60*s, w=line_w)
        thick_line(c, cx, head_y - 22*s, cx + 18*s, head_y - 60*s, w=line_w)
        black_circle(c, cx - 18*s, head_y - 60*s, 5*s)
        black_circle(c, cx + 18*s, head_y - 60*s, 5*s)

    # legs
    thick_line(c, cx, head_y - 60*s, cx - 12*s, head_y - 115*s, w=line_w + 1)
    thick_line(c, cx, head_y - 60*s, cx + 12*s, head_y - 115*s, w=line_w + 1)
    # feet
    thick_line(c, cx - 12*s, head_y - 115*s, cx - 22*s, head_y - 115*s, w=line_w)
    thick_line(c, cx + 12*s, head_y - 115*s, cx + 22*s, head_y - 115*s, w=line_w)

    white_ninja_eye(c, cx - 6*s, head_y + 2*s, size=4.5*s, side='left')
    white_ninja_eye(c, cx + 6*s, head_y + 2*s, size=4.5*s, side='right')


def cobra_silhouette(c, x_start, y_start, x_end, y_end, thickness=18, hood_size=22):
    """Draw a stick-figure cobra: thick S-curve body with a flared hood head."""
    sx, sy = _within_frame(x_start, y_start)
    ex, ey = _within_frame(x_end, y_end)
    c.setStrokeColor(INK)
    c.setFillColor(INK)
    c.setLineWidth(thickness)
    c.setLineCap(1)
    # body as wavy path
    p = c.beginPath()
    p.moveTo(sx, sy)
    mid1x = sx + (ex - sx) * 0.3
    mid1y = sy + 25
    mid2x = sx + (ex - sx) * 0.65
    mid2y = sy - 25
    p.curveTo(mid1x, mid1y, mid2x, mid2y, ex, ey)
    c.drawPath(p, stroke=1, fill=0)

    # hood (flared shape at head end)
    hood = c.beginPath()
    hood.moveTo(ex - hood_size*0.3, ey + hood_size*0.6)
    hood.lineTo(ex + hood_size*0.6, ey + hood_size*0.4)
    hood.lineTo(ex + hood_size, ey)
    hood.lineTo(ex + hood_size*0.6, ey - hood_size*0.4)
    hood.lineTo(ex - hood_size*0.3, ey - hood_size*0.6)
    hood.lineTo(ex - hood_size*0.5, ey)
    hood.close()
    c.drawPath(hood, stroke=0, fill=1)

    # white slit-eye on the hood
    c.setFillColor(PAPER)
    c.setStrokeColor(PAPER)
    p_eye = c.beginPath()
    p_eye.moveTo(ex + 3, ey + 2)
    p_eye.lineTo(ex + 9, ey + 1)
    p_eye.lineTo(ex + 9, ey - 1)
    p_eye.lineTo(ex + 3, ey - 2)
    p_eye.close()
    c.drawPath(p_eye, stroke=0, fill=1)
    c.setFillColor(INK)
    c.setStrokeColor(INK)


# ─────────────────────────────────────────────────────────────────────────────
# SET / ENVIRONMENT PRIMITIVES
# ─────────────────────────────────────────────────────────────────────────────
def chair(c, cx, base_y, scale=1.0):
    """Simple chair beneath a seated figure."""
    s = scale
    c.setStrokeColor(INK)
    c.setLineWidth(4)
    c.setLineCap(1)
    x0, y0 = _within_frame(cx - 38*s, base_y)
    x1, y1 = _within_frame(cx + 38*s, base_y)
    c.line(x0, y0, x1, y1)
    # legs
    c.line(*_within_frame(cx - 34*s, base_y), *_within_frame(cx - 34*s, base_y - 38*s))
    c.line(*_within_frame(cx + 34*s, base_y), *_within_frame(cx + 34*s, base_y - 38*s))


def room_floor_and_walls(c):
    """Draw the dark room: floor line, ceiling line, vertical wood-panel hints."""
    c.setStrokeColor(INK)
    c.setLineWidth(2)
    c.setLineCap(1)
    # floor line
    c.line(*_within_frame(0, FRAME_H * 0.18), *_within_frame(FRAME_W, FRAME_H * 0.18))
    # ceiling line
    c.line(*_within_frame(FRAME_W * 0.08, FRAME_H * 0.82),
           *_within_frame(FRAME_W * 0.92, FRAME_H * 0.82))
    # vertical wood-panel hints
    c.setLineWidth(1)
    c.setStrokeColor(INK)
    for i in range(1, 7):
        px = FRAME_W * (0.08 + i * 0.84 / 7)
        c.line(*_within_frame(px, FRAME_H * 0.18),
               *_within_frame(px, FRAME_H * 0.82))


def overhead_lamp(c, cx, ceiling_y):
    """Black rectangle for ceiling lamp + downward light cone (faint)."""
    c.setFillColor(INK)
    c.rect(*_within_frame(cx - 18, ceiling_y - 4), 36, 6, stroke=0, fill=1)


def light_cone(c, cx, top_y, bottom_y, top_w=20, bot_w=85):
    """Diagonal lines suggesting a cone of light."""
    c.setStrokeColor(HexColor('#888888'))
    c.setLineWidth(1)
    c.line(*_within_frame(cx - top_w, top_y), *_within_frame(cx - bot_w, bottom_y))
    c.line(*_within_frame(cx + top_w, top_y), *_within_frame(cx + bot_w, bottom_y))
    c.setStrokeColor(INK)


def hatch_block(c, x, y, w, h, angle=45, spacing=6, weight=0.8):
    """Diagonal hatching for shadow/dark areas."""
    c.saveState()
    px, py = _within_frame(x, y)
    c.setStrokeColor(INK)
    c.setLineWidth(weight)
    # clip to rectangle
    p = c.beginPath()
    p.rect(px, py, w, h)
    c.clipPath(p, stroke=0)
    # draw lines
    rad = math.radians(angle)
    dx, dy = math.cos(rad), math.sin(rad)
    diag = math.hypot(w, h)
    n = int(diag / spacing) * 2 + 2
    perp_x, perp_y = -dy, dx
    cx, cy = px + w/2, py + h/2
    for i in range(-n, n):
        offset = i * spacing
        x0 = cx + perp_x * offset - dx * diag
        y0 = cy + perp_y * offset - dy * diag
        x1 = cx + perp_x * offset + dx * diag
        y1 = cy + perp_y * offset + dy * diag
        c.line(x0, y0, x1, y1)
    c.restoreState()


# ─────────────────────────────────────────────────────────────────────────────
# COMMON FRAME WRAPPER
# ─────────────────────────────────────────────────────────────────────────────
def frame_border(c, fill_black=False):
    """Draw the 16:9 frame border. Optionally fill with black."""
    if fill_black:
        c.setFillColor(INK)
        c.rect(FRAME_X, FRAME_Y, FRAME_W, FRAME_H, stroke=0, fill=1)
    c.setStrokeColor(INK)
    c.setLineWidth(2.5)
    c.setFillColor(PAPER)
    c.rect(FRAME_X, FRAME_Y, FRAME_W, FRAME_H, stroke=1, fill=0)


# ─────────────────────────────────────────────────────────────────────────────
# FRAMES
# ─────────────────────────────────────────────────────────────────────────────
def f1_cold_open(c):
    frame_border(c, fill_black=True)
    c.setFillColor(PAPER)
    c.setFont('Times-Italic', 30)
    c.drawCentredString(FRAME_X + FRAME_W/2, FRAME_Y + FRAME_H * 0.55, 'Delhi. 1880s.')
    c.setFont('Times-Italic', 16)
    c.setFillColor(HexColor('#999999'))
    c.drawCentredString(FRAME_X + FRAME_W/2, FRAME_Y + FRAME_H * 0.40, 'The British have a problem.')


def f2_establishing(c):
    frame_border(c)
    room_floor_and_walls(c)
    overhead_lamp(c, FRAME_W/2, FRAME_H * 0.82)
    light_cone(c, FRAME_W/2, FRAME_H * 0.82, FRAME_H * 0.10)
    chair(c, FRAME_W/2, FRAME_H * 0.22, scale=0.9)
    stickman_seated(c, FRAME_W/2, FRAME_H * 0.22, scale=0.9)
    # side shadow hatches
    hatch_block(c, FRAME_W * 0.02, FRAME_H * 0.18, FRAME_W * 0.08, FRAME_H * 0.64, angle=60, spacing=5)
    hatch_block(c, FRAME_W * 0.90, FRAME_H * 0.18, FRAME_W * 0.08, FRAME_H * 0.64, angle=120, spacing=5)


def f3_medium_black(c):
    frame_border(c)
    # vertical wood panel hints
    c.setStrokeColor(INK)
    c.setLineWidth(1)
    for px_frac in [0.18, 0.40, 0.60, 0.82]:
        x = FRAME_W * px_frac
        c.line(*_within_frame(x, 0), *_within_frame(x, FRAME_H))
    # hatch right side (shadow opposite the light)
    hatch_block(c, FRAME_W * 0.50, 0, FRAME_W * 0.50, FRAME_H, angle=120, spacing=4, weight=0.9)
    # large seated figure, lower portion of frame
    stickman_seated(c, FRAME_W/2, FRAME_H * 0.08, scale=1.4)


def f4_coin_insert(c):
    frame_border(c)
    # wood grain — horizontal wavy lines
    c.setStrokeColor(INK)
    c.setLineWidth(0.7)
    for yfrac in [0.18, 0.32, 0.48, 0.64, 0.80]:
        y = FRAME_H * yfrac
        p = c.beginPath()
        p.moveTo(*_within_frame(0, y))
        for x in range(40, int(FRAME_W), 60):
            p.curveTo(*_within_frame(x - 30, y + 3),
                      *_within_frame(x - 15, y - 3),
                      *_within_frame(x, y))
        c.drawPath(p, stroke=1, fill=0)
    # shadow under coin
    hatch_block(c, FRAME_W*0.30, FRAME_H*0.25, FRAME_W*0.40, FRAME_H*0.08, angle=15, spacing=3)
    # coin — large black circle with white text
    cx, cy = _within_frame(FRAME_W/2, FRAME_H*0.42)
    c.setFillColor(INK)
    c.circle(cx, cy, 55, stroke=0, fill=1)
    c.setFillColor(PAPER)
    c.setFont('Times-Italic', 16)
    c.drawCentredString(cx, cy - 6, '1 rupee')
    # hand silhouette retreating from top
    c.setFillColor(INK)
    p = c.beginPath()
    fx, fy = _within_frame(0, FRAME_H)
    p.moveTo(FRAME_X + FRAME_W*0.32, FRAME_Y + FRAME_H)
    p.curveTo(FRAME_X + FRAME_W*0.36, FRAME_Y + FRAME_H*0.85,
              FRAME_X + FRAME_W*0.45, FRAME_Y + FRAME_H*0.78,
              FRAME_X + FRAME_W*0.50, FRAME_Y + FRAME_H*0.75)
    p.curveTo(FRAME_X + FRAME_W*0.55, FRAME_Y + FRAME_H*0.78,
              FRAME_X + FRAME_W*0.64, FRAME_Y + FRAME_H*0.85,
              FRAME_X + FRAME_W*0.68, FRAME_Y + FRAME_H)
    p.lineTo(FRAME_X + FRAME_W*0.32, FRAME_Y + FRAME_H)
    p.close()
    c.drawPath(p, stroke=0, fill=1)


def f5_shadow(c):
    frame_border(c)
    room_floor_and_walls(c)
    overhead_lamp(c, FRAME_W/2, FRAME_H * 0.82)
    light_cone(c, FRAME_W/2, FRAME_H * 0.82, FRAME_H * 0.10)
    # COBRA SHADOW behind figure
    cobra_silhouette(c,
                     FRAME_W * 0.10, FRAME_H * 0.55,
                     FRAME_W * 0.85, FRAME_H * 0.55,
                     thickness=22, hood_size=26)
    # figure (small, in front of shadow)
    chair(c, FRAME_W/2, FRAME_H * 0.22, scale=0.9)
    stickman_seated(c, FRAME_W/2, FRAME_H * 0.22, scale=0.9)
    # annotation: "shadow only — 1 sec pass"
    c.setFillColor(HexColor('#990000'))
    c.setFont('Helvetica-Oblique', 9)
    c.drawString(FRAME_X + 16, FRAME_Y + FRAME_H * 0.92, 'cobra shadow on wall — 1 sec pass')
    c.setFillColor(INK)


def f6_cages(c):
    frame_border(c, fill_black=True)
    # distant window of light
    wx, wy = _within_frame(FRAME_W * 0.62, FRAME_H * 0.35)
    c.setFillColor(HexColor('#cccccc'))
    c.rect(wx, wy, FRAME_W * 0.22, FRAME_H * 0.32, stroke=0, fill=1)
    c.setStrokeColor(PAPER)
    c.setLineWidth(2)
    c.rect(wx, wy, FRAME_W * 0.22, FRAME_H * 0.32, stroke=1, fill=0)
    # window cross
    c.line(wx + FRAME_W * 0.11, wy, wx + FRAME_W * 0.11, wy + FRAME_H * 0.32)
    c.line(wx, wy + FRAME_H * 0.16, wx + FRAME_W * 0.22, wy + FRAME_H * 0.16)
    # cage bars — foreground
    c.setStrokeColor(PAPER)
    c.setLineWidth(3)
    c.setLineCap(1)
    for i in range(7):
        x_local = FRAME_W * (0.06 + i * 0.07)
        c.line(*_within_frame(x_local, FRAME_H * 0.15),
               *_within_frame(x_local, FRAME_H * 0.90))
    # top of cage
    c.line(*_within_frame(FRAME_W * 0.03, FRAME_H * 0.90),
           *_within_frame(FRAME_W * 0.55, FRAME_H * 0.90))
    # snake silhouette inside (coiled)
    c.setFillColor(PAPER)
    p = c.beginPath()
    cx0 = FRAME_W * 0.25
    cy0 = FRAME_H * 0.40
    p.moveTo(*_within_frame(cx0 - 30, cy0))
    p.curveTo(*_within_frame(cx0 - 30, cy0 + 25),
              *_within_frame(cx0 + 30, cy0 + 25),
              *_within_frame(cx0 + 30, cy0))
    p.curveTo(*_within_frame(cx0 + 30, cy0 - 15),
              *_within_frame(cx0 - 20, cy0 - 15),
              *_within_frame(cx0 - 20, cy0 - 5))
    p.curveTo(*_within_frame(cx0 - 20, cy0 + 5),
              *_within_frame(cx0 + 15, cy0 + 5),
              *_within_frame(cx0 + 15, cy0))
    c.drawPath(p, stroke=0, fill=1)
    c.setFillColor(INK)


def f7_closeup_black(c):
    frame_border(c)
    # half frame shadow (left side dark)
    hatch_block(c, 0, 0, FRAME_W * 0.45, FRAME_H, angle=60, spacing=2.5, weight=1.0)
    # giant head fills most of frame
    cx, cy = _within_frame(FRAME_W * 0.50, FRAME_H * 0.50)
    c.setFillColor(INK)
    c.setStrokeColor(INK)
    c.circle(cx, cy, FRAME_H * 0.42, stroke=0, fill=1)
    # big white eyes
    eye_y = cy + FRAME_H * 0.05
    eye_w = FRAME_H * 0.10
    eye_h = FRAME_H * 0.045
    # left eye
    c.setFillColor(PAPER)
    p = c.beginPath()
    lx = cx - FRAME_H * 0.13
    p.moveTo(lx - eye_w, eye_y + eye_h*0.4)
    p.lineTo(lx + eye_w, eye_y)
    p.lineTo(lx + eye_w, eye_y - eye_h*0.4)
    p.lineTo(lx - eye_w, eye_y - eye_h*0.5)
    p.close()
    c.drawPath(p, stroke=0, fill=1)
    # right eye
    p2 = c.beginPath()
    rx = cx + FRAME_H * 0.13
    p2.moveTo(rx + eye_w, eye_y + eye_h*0.4)
    p2.lineTo(rx - eye_w, eye_y)
    p2.lineTo(rx - eye_w, eye_y - eye_h*0.4)
    p2.lineTo(rx + eye_w, eye_y - eye_h*0.5)
    p2.close()
    c.drawPath(p2, stroke=0, fill=1)
    c.setFillColor(INK)


def f8_transition(c):
    frame_border(c, fill_black=True)
    c.setFillColor(PAPER)
    c.setFont('Times-Italic', 30)
    c.drawCentredString(FRAME_X + FRAME_W/2, FRAME_Y + FRAME_H * 0.50, 'Detroit. 1995.')
    c.setStrokeColor(HexColor('#888888'))
    c.setLineWidth(0.7)
    c.line(FRAME_X + FRAME_W * 0.40, FRAME_Y + FRAME_H * 0.40,
           FRAME_X + FRAME_W * 0.60, FRAME_Y + FRAME_H * 0.40)


def f9_establishing_white(c):
    frame_border(c)
    room_floor_and_walls(c)
    overhead_lamp(c, FRAME_W/2, FRAME_H * 0.82)
    light_cone(c, FRAME_W/2, FRAME_H * 0.82, FRAME_H * 0.10)
    chair(c, FRAME_W/2, FRAME_H * 0.22, scale=0.9)
    stickman_seated(c, FRAME_W/2, FRAME_H * 0.22, scale=0.9, accessory='doctor-coat')
    # small table to the right with pill bottle
    tx = FRAME_W * 0.65
    ty = FRAME_H * 0.24
    c.setFillColor(INK)
    c.rect(*_within_frame(tx, ty), 28, 4, stroke=0, fill=1)
    # table legs
    c.setLineWidth(3)
    c.setLineCap(1)
    c.line(*_within_frame(tx + 3, ty), *_within_frame(tx + 3, ty - 22))
    c.line(*_within_frame(tx + 25, ty), *_within_frame(tx + 25, ty - 22))
    # pill bottle
    c.rect(*_within_frame(tx + 8, ty + 4), 12, 18, stroke=0, fill=1)
    # cap (drawn slightly inset, white edge for label suggestion)
    c.setStrokeColor(PAPER)
    c.setLineWidth(1)
    c.rect(*_within_frame(tx + 9, ty + 9), 10, 8, stroke=1, fill=0)
    c.setStrokeColor(INK)
    # lighter side shadows than F2
    hatch_block(c, FRAME_W * 0.02, FRAME_H * 0.18, FRAME_W * 0.06, FRAME_H * 0.64, angle=60, spacing=10, weight=0.6)
    hatch_block(c, FRAME_W * 0.92, FRAME_H * 0.18, FRAME_W * 0.06, FRAME_H * 0.64, angle=120, spacing=10, weight=0.6)


def f10_pill_insert(c):
    frame_border(c)
    # wood grain
    c.setStrokeColor(INK)
    c.setLineWidth(0.6)
    for yfrac in [0.18, 0.34, 0.50, 0.66, 0.82]:
        y = FRAME_H * yfrac
        p = c.beginPath()
        p.moveTo(*_within_frame(0, y))
        for x in range(40, int(FRAME_W), 60):
            p.curveTo(*_within_frame(x - 30, y + 3),
                      *_within_frame(x - 15, y - 3),
                      *_within_frame(x, y))
        c.drawPath(p, stroke=1, fill=0)
    # diagonal shadow
    hatch_block(c, FRAME_W*0.50, FRAME_H*0.04, FRAME_W*0.50, FRAME_H*0.50, angle=25, spacing=3, weight=0.7)
    # pill bottle body (large, centered)
    bx = FRAME_W * 0.36
    by = FRAME_H * 0.18
    bw = FRAME_W * 0.18
    bh = FRAME_H * 0.55
    c.setFillColor(INK)
    c.rect(*_within_frame(bx, by), bw, bh, stroke=0, fill=1)
    # cap
    cap_h = bh * 0.20
    c.rect(*_within_frame(bx - 2, by + bh - cap_h), bw + 4, cap_h, stroke=0, fill=1)
    # label (white box)
    c.setFillColor(PAPER)
    c.rect(*_within_frame(bx + 8, by + 8), bw - 16, bh - cap_h - 16, stroke=0, fill=1)
    # lines on label
    c.setStrokeColor(INK)
    c.setLineWidth(1)
    for i in range(5):
        ly = by + 16 + i * 14
        c.line(*_within_frame(bx + 12, ly), *_within_frame(bx + bw - 12, ly))
    c.setFillColor(INK)


def f11_pushin(c):
    frame_border(c)
    # smaller START frame (left, faint)
    start_x = FRAME_W * 0.08
    start_y = FRAME_H * 0.20
    start_w = FRAME_W * 0.30
    start_h = FRAME_H * 0.60
    c.setStrokeColor(HexColor('#888888'))
    c.setLineWidth(1.2)
    c.setDash(3, 3)
    c.rect(*_within_frame(start_x, start_y), start_w, start_h, stroke=1, fill=0)
    c.setDash()
    c.setFont('Helvetica', 9)
    c.setFillColor(HexColor('#888888'))
    c.drawCentredString(FRAME_X + start_x + start_w/2,
                        FRAME_Y + start_y + start_h + 10, 'START')
    # smaller figure
    stickman_seated(c, start_x + start_w/2, start_y + 12, scale=0.55, accessory='doctor-coat')
    chair(c, start_x + start_w/2, start_y + 12, scale=0.55)
    # ARROW
    ax1 = FRAME_W * 0.42
    ax2 = FRAME_W * 0.55
    ay = FRAME_H * 0.50
    c.setStrokeColor(HexColor('#990000'))
    c.setLineWidth(2.5)
    c.line(*_within_frame(ax1, ay), *_within_frame(ax2, ay))
    c.line(*_within_frame(ax2 - 5, ay - 4), *_within_frame(ax2, ay))
    c.line(*_within_frame(ax2 - 5, ay + 4), *_within_frame(ax2, ay))
    c.setFillColor(HexColor('#990000'))
    c.setFont('Helvetica-Bold', 9)
    c.drawCentredString(FRAME_X + (ax1+ax2)/2, FRAME_Y + ay + 10, 'PUSH IN')
    c.setFont('Helvetica-Oblique', 9)
    c.drawCentredString(FRAME_X + (ax1+ax2)/2, FRAME_Y + ay - 18, '8 sec')
    # larger END frame (right)
    end_x = FRAME_W * 0.58
    end_y = FRAME_H * 0.12
    end_w = FRAME_W * 0.35
    end_h = FRAME_H * 0.76
    c.setStrokeColor(INK)
    c.setLineWidth(2)
    c.rect(*_within_frame(end_x, end_y), end_w, end_h, stroke=1, fill=0)
    c.setFillColor(INK)
    c.setFont('Helvetica-Bold', 10)
    c.drawCentredString(FRAME_X + end_x + end_w/2,
                        FRAME_Y + end_y + end_h + 8, 'END')
    stickman_seated(c, end_x + end_w/2, end_y + 8, scale=1.0, accessory='doctor-coat')
    chair(c, end_x + end_w/2, end_y + 8, scale=1.0)


def f12_prescription(c):
    frame_border(c)
    # wood grain
    c.setStrokeColor(INK)
    c.setLineWidth(0.5)
    for yfrac in [0.10, 0.85]:
        y = FRAME_H * yfrac
        p = c.beginPath()
        p.moveTo(*_within_frame(0, y))
        for x in range(40, int(FRAME_W), 60):
            p.curveTo(*_within_frame(x - 30, y + 2),
                      *_within_frame(x - 15, y - 2),
                      *_within_frame(x, y))
        c.drawPath(p, stroke=1, fill=0)
    # prescription pad
    pad_x = FRAME_W * 0.22
    pad_y = FRAME_H * 0.20
    pad_w = FRAME_W * 0.42
    pad_h = FRAME_H * 0.60
    c.setFillColor(PAPER)
    c.setStrokeColor(INK)
    c.setLineWidth(2.5)
    c.rect(*_within_frame(pad_x, pad_y), pad_w, pad_h, stroke=1, fill=1)
    # Rx
    c.setFillColor(INK)
    c.setFont('Times-Italic', 18)
    c.drawString(*_within_frame(pad_x + 12, pad_y + pad_h - 22), 'Rx')
    # lines on pad
    c.setStrokeColor(INK)
    c.setLineWidth(0.8)
    for i in range(4):
        ly = pad_y + pad_h - 40 - i * 28
        c.line(*_within_frame(pad_x + 12, ly), *_within_frame(pad_x + pad_w - 14, ly))
    # signature scrawl
    c.setLineWidth(2.5)
    sx0 = FRAME_W * 0.32
    sy0 = FRAME_H * 0.30
    p_sig = c.beginPath()
    p_sig.moveTo(*_within_frame(sx0, sy0))
    p_sig.curveTo(*_within_frame(sx0 + 30, sy0 + 16),
                  *_within_frame(sx0 + 60, sy0 - 14),
                  *_within_frame(sx0 + 90, sy0 + 4))
    p_sig.curveTo(*_within_frame(sx0 + 110, sy0 + 8),
                  *_within_frame(sx0 + 130, sy0 - 4),
                  *_within_frame(sx0 + 150, sy0))
    c.drawPath(p_sig, stroke=1, fill=0)
    # hand silhouette (stick-figure hand)
    c.setFillColor(INK)
    hx = FRAME_W * 0.70
    hy_top = FRAME_H * 0.95
    p_hand = c.beginPath()
    p_hand.moveTo(*_within_frame(hx, hy_top))
    p_hand.curveTo(*_within_frame(hx + 8, hy_top - 30),
                   *_within_frame(hx + 14, hy_top - 60),
                   *_within_frame(hx + 16, hy_top - 90))
    p_hand.curveTo(*_within_frame(hx + 8, hy_top - 105),
                   *_within_frame(hx - 8, hy_top - 100),
                   *_within_frame(hx - 12, hy_top - 80))
    p_hand.curveTo(*_within_frame(hx - 10, hy_top - 50),
                   *_within_frame(hx - 8, hy_top - 25),
                   *_within_frame(hx - 8, hy_top))
    p_hand.close()
    c.drawPath(p_hand, stroke=0, fill=1)
    # pen
    c.setLineWidth(4)
    pen_x = FRAME_W * 0.55
    pen_y = FRAME_H * 0.32
    c.line(*_within_frame(pen_x, pen_y - 4),
           *_within_frame(pen_x + 30, pen_y + 22))


def f13_closeup_white(c):
    frame_border(c)
    # lighter shadow than F7
    hatch_block(c, 0, 0, FRAME_W * 0.45, FRAME_H, angle=60, spacing=4, weight=0.7)
    # head
    cx, cy = _within_frame(FRAME_W * 0.50, FRAME_H * 0.55)
    c.setFillColor(INK)
    c.setStrokeColor(INK)
    c.circle(cx, cy, FRAME_H * 0.40, stroke=0, fill=1)
    # white doctor's coat showing on bottom (V-shape under the chin)
    c.setFillColor(PAPER)
    c.setStrokeColor(PAPER)
    p_v = c.beginPath()
    chin_x, chin_y = _within_frame(FRAME_W * 0.50, FRAME_H * 0.13)
    p_v.moveTo(chin_x - 60, chin_y)
    p_v.lineTo(chin_x, chin_y + 30)
    p_v.lineTo(chin_x + 60, chin_y)
    p_v.lineTo(chin_x + 60, chin_y - 30)
    p_v.lineTo(chin_x - 60, chin_y - 30)
    p_v.close()
    c.drawPath(p_v, stroke=0, fill=1)
    c.setFillColor(INK)
    # eyes
    eye_y = cy + FRAME_H * 0.05
    eye_w = FRAME_H * 0.10
    eye_h = FRAME_H * 0.045
    c.setFillColor(PAPER)
    p = c.beginPath()
    lx = cx - FRAME_H * 0.13
    p.moveTo(lx - eye_w, eye_y + eye_h*0.4)
    p.lineTo(lx + eye_w, eye_y)
    p.lineTo(lx + eye_w, eye_y - eye_h*0.4)
    p.lineTo(lx - eye_w, eye_y - eye_h*0.5)
    p.close()
    c.drawPath(p, stroke=0, fill=1)
    p2 = c.beginPath()
    rx = cx + FRAME_H * 0.13
    p2.moveTo(rx + eye_w, eye_y + eye_h*0.4)
    p2.lineTo(rx - eye_w, eye_y)
    p2.lineTo(rx - eye_w, eye_y - eye_h*0.4)
    p2.lineTo(rx + eye_w, eye_y - eye_h*0.5)
    p2.close()
    c.drawPath(p2, stroke=0, fill=1)
    c.setFillColor(INK)


def f14_book_reveal(c):
    frame_border(c)
    # stickman standing, holding book
    stickman_standing(c, FRAME_W/2, FRAME_H * 0.15, scale=1.1, holds_book=True)
    # book in hands (between the hands, visible)
    book_x = FRAME_W * 0.50 - 50
    book_y = FRAME_H * 0.50
    book_w = 100
    book_h = 75
    c.setFillColor(PAPER)
    c.setStrokeColor(INK)
    c.setLineWidth(3)
    c.rect(*_within_frame(book_x, book_y), book_w, book_h, stroke=1, fill=1)
    # title typography on the book
    c.setFillColor(INK)
    c.setFont('Helvetica-Bold', 7)
    tx = book_x + book_w / 2
    c.drawCentredString(*_within_frame(tx, book_y + book_h - 12), 'MORE')
    c.setFont('Helvetica-Bold', 10)
    c.drawCentredString(*_within_frame(tx, book_y + book_h - 24), 'SOLUTIONS')
    c.setFont('Helvetica-Bold', 7)
    c.drawCentredString(*_within_frame(tx, book_y + book_h - 34), '=')
    c.drawCentredString(*_within_frame(tx, book_y + book_h - 43), 'MORE')
    c.setFont('Helvetica-Bold', 10)
    c.drawCentredString(*_within_frame(tx, book_y + book_h - 55), 'PROBLEMS')
    c.setFillColor(INK)
    c.rect(*_within_frame(book_x, book_y), book_w, 4, stroke=0, fill=1)
    c.rect(*_within_frame(book_x, book_y + book_h - 8), book_w, 8, stroke=0, fill=1)
    c.setFillColor(PAPER)
    c.setFont('Helvetica-Bold', 5)
    c.drawCentredString(*_within_frame(tx, book_y + 0), 'AHMED HAFDI')
    c.setFillColor(INK)


def f15_end_card(c):
    frame_border(c, fill_black=True)
    c.setFillColor(PAPER)
    c.setFont('Helvetica-Bold', 18)
    c.drawCentredString(FRAME_X + FRAME_W/2, FRAME_Y + FRAME_H * 0.55, 'OUT NOW ON AMAZON')
    c.setStrokeColor(HexColor('#999999'))
    c.setLineWidth(0.7)
    c.line(FRAME_X + FRAME_W * 0.35, FRAME_Y + FRAME_H * 0.46,
           FRAME_X + FRAME_W * 0.65, FRAME_Y + FRAME_H * 0.46)
    c.setFillColor(HexColor('#999999'))
    c.setFont('Times-Italic', 12)
    c.drawCentredString(FRAME_X + FRAME_W/2, FRAME_Y + FRAME_H * 0.36,
                        'moresolutions-moreproblems.com')


# ─────────────────────────────────────────────────────────────────────────────
# PAGE BUILDER — frame at top + notes below
# ─────────────────────────────────────────────────────────────────────────────
def draw_notes(c, fno, timecode, title, camera, vo=None):
    """Below-frame notes block."""
    y = FRAME_Y - 30
    c.setFillColor(INK)
    c.setFont('Helvetica-Bold', 11)
    c.drawString(MARGIN, y, f'FRAME {fno}   ·   {timecode}')
    c.setFont('Helvetica-Bold', 16)
    c.drawString(MARGIN, y - 22, title)
    c.setFont('Helvetica', 10)
    c.setFillColor(GREY_TXT)
    # wrap-style camera notes
    text = c.beginText(MARGIN, y - 46)
    text.setFont('Helvetica-Oblique', 10)
    text.textLine('CAMERA / NOTES')
    text.setFont('Helvetica', 10)
    # split camera string into lines of ~95 chars
    words = camera.split()
    line = ''
    for w in words:
        if len(line) + len(w) + 1 > 95:
            text.textLine(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        text.textLine(line)
    c.drawText(text)

    if vo:
        # VO box
        c.setFillColor(HexColor('#f0f0f0'))
        vo_y = y - 110
        c.rect(MARGIN, vo_y - 60, FRAME_W, 70, stroke=0, fill=1)
        c.setStrokeColor(INK)
        c.setLineWidth(2)
        c.line(MARGIN, vo_y - 60, MARGIN, vo_y + 10)
        c.setFillColor(INK)
        c.setFont('Helvetica-Bold', 9)
        c.drawString(MARGIN + 10, vo_y + 0, 'VOICE-OVER')
        c.setFont('Times-Italic', 11)
        text = c.beginText(MARGIN + 10, vo_y - 18)
        words = vo.split()
        line = ''
        for w in words:
            if len(line) + len(w) + 1 > 105:
                text.textLine(line)
                line = w
            else:
                line = (line + ' ' + w) if line else w
        if line:
            text.textLine(line)
        c.drawText(text)


# ─────────────────────────────────────────────────────────────────────────────
# COVER PAGE
# ─────────────────────────────────────────────────────────────────────────────
def cover_page(c):
    # black band top
    c.setFillColor(INK)
    c.rect(0, PAGE_H - 1*inch, PAGE_W, 1*inch, stroke=0, fill=1)
    c.setFillColor(PAPER)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(MARGIN, PAGE_H - 0.6*inch, 'STORYBOARD · STICK-FIGURE TREATMENT')
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.6*inch, '15 frames · 2 min · B/W')

    # title
    c.setFillColor(INK)
    c.setFont('Helvetica-Bold', 44)
    c.drawString(MARGIN, PAGE_H - 2.4*inch, 'MORE')
    c.setFont('Helvetica-Bold', 60)
    c.drawString(MARGIN, PAGE_H - 3.4*inch, 'SOLUTIONS')
    c.setFont('Helvetica-Bold', 30)
    c.drawString(MARGIN, PAGE_H - 4.0*inch, '=')
    c.setFont('Helvetica-Bold', 44)
    c.drawString(MARGIN, PAGE_H - 4.7*inch, 'MORE')
    c.setFont('Helvetica-Bold', 60)
    c.drawString(MARGIN, PAGE_H - 5.7*inch, 'PROBLEMS')

    # rule
    c.setLineWidth(1)
    c.setStrokeColor(INK)
    c.line(MARGIN, PAGE_H - 6.0*inch, PAGE_W - MARGIN, PAGE_H - 6.0*inch)

    c.setFont('Times-Italic', 14)
    c.drawString(MARGIN, PAGE_H - 6.4*inch, 'A book trailer storyboard · 2 minutes · stick-figure animation aesthetic')
    c.setFont('Helvetica', 11)
    c.drawString(MARGIN, PAGE_H - 6.8*inch, 'Directed by Ahmed Hafdi · Kenitra, Morocco')

    # tiny stickman illustration bottom right
    big_stickman(c, PAGE_W - 1.8*inch, 1.5*inch, scale=1.4)

    # vignette summary
    c.setFont('Helvetica-Bold', 11)
    c.drawString(MARGIN, 3.3*inch, 'VIGNETTE 1 — THE COBRA  (0:00 – 0:55)')
    c.setFont('Helvetica', 10)
    c.drawString(MARGIN, 3.05*inch, 'Frames 1–8 · Delhi, 1880s · the British bounty on cobras · the cascade revealed')
    c.setFont('Helvetica-Bold', 11)
    c.drawString(MARGIN, 2.7*inch, 'VIGNETTE 2 — THE MEDICINE  (1:05 – 1:45)')
    c.setFont('Helvetica', 10)
    c.drawString(MARGIN, 2.45*inch, 'Frames 9–13 · Detroit, 1995 · the OxyContin approval · the same arithmetic')
    c.setFont('Helvetica-Bold', 11)
    c.drawString(MARGIN, 2.10*inch, 'REVEAL  (1:45 – 2:00)')
    c.setFont('Helvetica', 10)
    c.drawString(MARGIN, 1.85*inch, 'Frames 14–15 · the book · the call to action')

    # black band bottom
    c.setFillColor(INK)
    c.rect(0, 0, PAGE_W, 0.7*inch, stroke=0, fill=1)
    c.setFillColor(PAPER)
    c.setFont('Helvetica', 9)
    c.drawString(MARGIN, 0.32*inch, 'AHMED HAFDI · STORYBOARD · MORE SOLUTIONS = MORE PROBLEMS')
    c.drawRightString(PAGE_W - MARGIN, 0.32*inch, 'PAGE 1 / 17')


def big_stickman(c, cx, cy, scale=1.0):
    """A large stickman, standing, used as cover decoration."""
    s = scale
    line_w = 9 * s
    head_y = cy + 90 * s
    c.setFillColor(INK)
    c.circle(cx, head_y, 15 * s, stroke=0, fill=1)
    # body
    c.setStrokeColor(INK)
    c.setLineWidth(line_w)
    c.setLineCap(1)
    c.line(cx, head_y - 15*s, cx, head_y - 50*s)
    c.line(cx, head_y - 20*s, cx - 22*s, head_y - 50*s)
    c.line(cx, head_y - 20*s, cx + 22*s, head_y - 50*s)
    c.line(cx, head_y - 50*s, cx - 14*s, head_y - 90*s)
    c.line(cx, head_y - 50*s, cx + 14*s, head_y - 90*s)
    c.line(cx - 14*s, head_y - 90*s, cx - 22*s, head_y - 90*s)
    c.line(cx + 14*s, head_y - 90*s, cx + 22*s, head_y - 90*s)
    c.setFillColor(INK)
    c.circle(cx - 22*s, head_y - 50*s, 5*s, stroke=0, fill=1)
    c.circle(cx + 22*s, head_y - 50*s, 5*s, stroke=0, fill=1)
    # eyes
    c.setFillColor(PAPER)
    p = c.beginPath()
    p.moveTo(cx - 12*s, head_y + 2*s)
    p.lineTo(cx - 2*s, head_y)
    p.lineTo(cx - 2*s, head_y - 3*s)
    p.lineTo(cx - 12*s, head_y - 2*s)
    p.close()
    c.drawPath(p, stroke=0, fill=1)
    p2 = c.beginPath()
    p2.moveTo(cx + 12*s, head_y + 2*s)
    p2.lineTo(cx + 2*s, head_y)
    p2.lineTo(cx + 2*s, head_y - 3*s)
    p2.lineTo(cx + 12*s, head_y - 2*s)
    p2.close()
    c.drawPath(p2, stroke=0, fill=1)
    c.setFillColor(INK)


# ─────────────────────────────────────────────────────────────────────────────
# SHOOT SUMMARY PAGE
# ─────────────────────────────────────────────────────────────────────────────
def summary_page(c):
    c.setFillColor(INK)
    c.setFont('Helvetica-Bold', 20)
    c.drawString(MARGIN, PAGE_H - 1.0*inch, 'SHOOT SUMMARY · ONE EVENING, THREE HOURS')

    c.setLineWidth(1)
    c.line(MARGIN, PAGE_H - 1.15*inch, PAGE_W - MARGIN, PAGE_H - 1.15*inch)

    y = PAGE_H - 1.5*inch
    rows = [
        ('SETUP (30 min)', 'Black sheet stretched on a wall. One LED panel from camera-left (or one window). Tripod with phone clamp. Lavalier mic plugged into phone.'),
        ('BLOCK A — WIDE SHOTS (40 min)', 'Frames 2, 5, 9. Same locked camera position. Two wardrobe changes between takes (black → black + sheet/snake prop → white).'),
        ('BLOCK B — MEDIUM / CLOSE-UPS (45 min)', 'Frames 3, 7, 13. Same chair, same lens, two wardrobe changes. Shoot all three back-to-back so the lighting consistency holds.'),
        ('BLOCK C — TOP-DOWN INSERTS (30 min)', 'Frames 4, 10, 12. Same table-top setup. Coin, pill bottle, prescription pad — single 30-minute block.'),
        ('BLOCK D — BOOK REVEAL (15 min)', 'Frame 14. Stand against neutral wall, hold book, slow camera push-in.'),
        ('GENERATED IN EDITING', 'Frames 1, 6, 8, 15. Title cards + the cage shot (lit prop in a dark corner) + the end card.'),
        ('TOTAL', 'About 3 hours of shooting + 2 evenings in CapCut for the edit.'),
    ]
    for label, body in rows:
        c.setFont('Helvetica-Bold', 11)
        c.drawString(MARGIN, y, label)
        y -= 14
        c.setFont('Helvetica', 10)
        c.setFillColor(GREY_TXT)
        text = c.beginText(MARGIN, y)
        words = body.split()
        line = ''
        for w in words:
            if len(line) + len(w) + 1 > 100:
                text.textLine(line)
                line = w
            else:
                line = (line + ' ' + w) if line else w
        if line:
            text.textLine(line)
        c.drawText(text)
        y -= 32
        c.setFillColor(INK)

    # visual rhymes box
    c.setFillColor(INK)
    c.rect(MARGIN, 1.6*inch, FRAME_W, 2.0*inch, stroke=0, fill=1)
    c.setFillColor(PAPER)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(MARGIN + 14, 1.6*inch + 1.65*inch, 'THE FOUR VISUAL RHYMES')
    c.setFont('Helvetica', 9.5)
    rhymes = [
        'Frame 1  ↔  Frame 8  ↔  Frame 15      black title cards · the only moments of stillness',
        'Frame 2  ↔  Frame 9                                identical wide composition · different century',
        'Frame 4  ↔  Frame 10  ↔  Frame 12     coin · pill · signature · three top-down transactions',
        'Frame 7  ↔  Frame 13                              identical close-up · black shirt → white shirt',
    ]
    yy = 1.6*inch + 1.30*inch
    for r in rhymes:
        c.drawString(MARGIN + 14, yy, r)
        yy -= 18

    # bottom band
    c.setFillColor(INK)
    c.rect(0, 0, PAGE_W, 0.7*inch, stroke=0, fill=1)
    c.setFillColor(PAPER)
    c.setFont('Helvetica', 9)
    c.drawString(MARGIN, 0.32*inch, 'AHMED HAFDI · STORYBOARD · MORE SOLUTIONS = MORE PROBLEMS')
    c.drawRightString(PAGE_W - MARGIN, 0.32*inch, 'PAGE 17 / 17')


# ─────────────────────────────────────────────────────────────────────────────
# FRAME REGISTRY
# ─────────────────────────────────────────────────────────────────────────────
FRAMES = [
    ('1', '0:00–0:05', 'Cold open · title card', f1_cold_open,
     'Static · type only. No music. Faint city ambient + a single distant cobra hiss.', None),

    ('2', '0:05–0:18', 'Establishing wide · the room', f2_establishing,
     'Static · locked-off · wide. Composition: 80% room, 20% figure — the negative space carries the loneliness. Light from above-front.', None),

    ('3', '0:18–0:25', 'Medium · in black', f3_medium_black,
     'Eye-level · side light from camera-left · half the face in shadow. Focus the camera on the eyes.',
     '"Too many cobras. People are dying. So the government does what any rational government would do. It offers a bounty. One rupee per dead snake."'),

    ('4', '0:25–0:30', 'Insert · the bounty', f4_coin_insert,
     'Top-down macro. Coin sharp, hand soft, wood grain sharp. The transaction is the subject.', None),

    ('5', '0:30–0:45', 'The shadow', f5_shadow,
     'Same locked-off wide as Frame 2 — but a cobra shadow passes the wall behind him. He does not react. Sound: hiss + scrape of scales.',
     '"Then someone notices something. It’s easier to breed cobras than to hunt them."'),

    ('6', '0:45–0:50', 'Cages (implied)', f6_cages,
     'Low angle, slow push-in over 1–2 inches. Cage felt more than seen — distant window of light, foreground bars, a coiled snake hint.', None),

    ('7', '0:50–0:55', 'Close-up · the punchline', f7_closeup_black,
     'Tight close-up · eye-level · the eyes carry the shot · everything else loses focus.',
     '"This was 1880. Read the next page in any history book and you’ll find the same story under different names."'),

    ('8', '0:55–1:05', 'Transition · music in', f8_transition,
     'Black for three full seconds. First music cue here — a single sustained low synth note. The pacing changes.', None),

    ('9', '1:05–1:15', 'Same wide · transformed', f9_establishing_white,
     'IDENTICAL framing to Frame 2 — but white doctor’s coat on the figure, pill bottle on the table beside him, lighting slightly cooler.', None),

    ('10', '1:15–1:20', 'Insert · the prescription', f10_pill_insert,
     'Top-down macro at the same scale as Frame 4. Visual rhyme: coin → pill bottle. The transaction has changed shape.', None),

    ('11', '1:20–1:35', 'Slow dolly · 8 seconds', f11_pushin,
     'Camera dollies forward by about 12 inches over 8 seconds. The figure does not move — the room comes to him. Faint hospital monitor in the sound design.', None),

    ('12', '1:35–1:40', 'Insert · the signature', f12_prescription,
     'Top-down macro. Echoes Frame 4 and Frame 10. Three transactions, same arithmetic. Soft pen-scratch on paper.', None),

    ('13', '1:40–1:45', '"It’s mathematics."', f13_closeup_white,
     'Identical framing to Frame 7 — the strongest visual rhyme in the film. Black shirt becomes white. 1880 becomes 1995. Same person.',
     '"Two centuries between Delhi and Detroit. The architecture of the catastrophe is identical. This isn’t bad luck. It’s mathematics."'),

    ('14', '1:45–1:55', 'The book in his hands', f14_book_reveal,
     'Static · eye-level · slow push-in over 3 seconds. Soft natural window light. Wardrobe is neutral — neither black nor white. The transformation is complete.', None),

    ('15', '1:55–2:00', 'End card', f15_end_card,
     'Static black with title type. Hold four seconds. Music resolves to silence on the last second. The trailer ends where it began.', None),
]


# ─────────────────────────────────────────────────────────────────────────────
# DRIVER
# ─────────────────────────────────────────────────────────────────────────────
def main():
    print(f'Generating storyboard → {OUT}')
    c = rl_canvas.Canvas(OUT, pagesize=A4)
    c.setTitle('More Solutions = More Problems — Storyboard (Stick-Figure Treatment)')
    c.setAuthor('Ahmed Hafdi')
    c.setSubject('Book trailer storyboard, 15 frames, 2 minutes, B/W stick-figure animation aesthetic')

    # COVER
    cover_page(c)
    c.showPage()

    # FRAMES
    for i, (fno, time, title, draw_fn, cam_notes, vo) in enumerate(FRAMES, start=2):
        draw_fn(c)
        draw_notes(c, fno, time, title, cam_notes, vo)
        # footer band
        c.setFillColor(INK)
        c.rect(0, 0, PAGE_W, 0.55*inch, stroke=0, fill=1)
        c.setFillColor(PAPER)
        c.setFont('Helvetica', 9)
        c.drawString(MARGIN, 0.25*inch, 'AHMED HAFDI · STORYBOARD · MORE SOLUTIONS = MORE PROBLEMS')
        c.drawRightString(PAGE_W - MARGIN, 0.25*inch, f'PAGE {i} / 17')
        c.showPage()

    # SUMMARY
    summary_page(c)
    c.showPage()

    c.save()
    size_kb = os.path.getsize(OUT) / 1024
    print(f'Saved · {size_kb:.0f} KB · 17 pages')


if __name__ == '__main__':
    main()
