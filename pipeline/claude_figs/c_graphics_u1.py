"""Claude's hand-drawn figures for c-graphics-u1 (Computer Graphics, unit 1: displays, colour, pipeline and raster
algorithms), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def arrow_down(x, y1, y2, c=AC, ar='n'):
    return L(x, y1, x, y2, c, 2.2, arrow=ar)


def pgrid(o, X0, Y0, cs, xs, ys, labels=True):
    """pixel grid with integer pixel centres; returns (fx, fy) mapping pixel coords to svg (y up)"""
    fx = lambda x: X0 + (x - xs[0]) * cs + cs / 2
    fy = lambda y: Y0 + (ys[-1] - y) * cs + cs / 2
    for x in xs:
        for y in ys:
            o.append(R(fx(x) - cs / 2, fy(y) - cs / 2, cs, cs, 'none', LN, 0, 1))
    if labels:
        for x in xs:
            o.append(T(fx(x), fy(ys[0]) + cs / 2 + 18, str(x), 13, fill=MUT))
        for y in ys:
            o.append(T(fx(xs[0]) - cs / 2 - 8, fy(y) + 5, str(y), 13, 'end', MUT))
    return fx, fy


def pix(o, fx, fy, cs, x, y, f=ACS, c=AC):
    o.append(R(fx(x) - cs / 2 + 1, fy(y) - cs / 2 + 1, cs - 2, cs - 2, f, c, 2, 1.8))


# ---- 1.1 one frame, end to end ----
def f1():
    o = []
    o.append(R(40, 30, 120, 210, PANEL, INK, 14, 2.2))
    o.append(R(50, 46, 100, 178, ACS, AC, 4, 1.4))
    o.append(T(100, 128, '1080', 14, fill=AC, bold=True)); o.append(T(100, 146, '× 1920', 14, fill=AC, bold=True))
    o.append(T(100, 164, 'pixels', 13, fill=AC))
    o.append(T(100, 262, 'phone screen', 13, fill=MUT, bold=True))
    steps = [('pixels', '1080 × 1920 = 2,073,600', PANEL, L2, INK), ('bytes per frame, 3 per pixel', '2,073,600 × 3 = 6,220,800 B = 5.9326 MiB', ACS, AC, AC),
             ('data rate at 60 frames/s', '6,220,800 × 60 = 373,248,000 B/s = 373.248 MB/s', LVS, LV, LV)]
    y = 30
    for i, (h, s, f, c, tc) in enumerate(steps):
        o.append(boxt(220, y, 470, 54, [h, s], f, c, 14, bold_first=True))
        if i < 2: o.append(arrow_down(455, y + 56, y + 76))
        y += 80
    o.append(arrow_down(455, y - 24, y - 4, LV, 'l'))
    o.append(boxt(310, y, 290, 44, ['GPU: colours pixels in parallel'], NXS, NX, 14, bold_first=True))
    o.append(L(162, 130, 216, 57, L2, 1.4, '4 3'))
    return y + 56, ''.join(o)
FIG[1] = (f1, 'One frame, end to end: the phone colours 2,073,600 pixels at 3 bytes each, 6,220,800 bytes or 5.9326 MiB a frame. At 60 frames a second that is 373.248 MB/s, the job a dedicated GPU is built for.',
          'A phone screen of 1080 by 1920 pixels beside a chain of boxes: 2,073,600 pixels, 6,220,800 bytes per frame, 373.248 MB/s at 60 frames per second, and the GPU.')


# ---- 1.2 bitmap against vector ----
def f2():
    o = []
    # jagged bitmap circle on a coarse grid
    n, cs, X0, Y0 = 16, 13, 50, 40
    c0 = (n - 1) / 2
    for i in range(n):
        for j in range(n):
            inside = (i - c0) ** 2 + (j - c0) ** 2 <= (n / 2 - 0.3) ** 2
            o.append(R(X0 + i * cs, Y0 + j * cs, cs, cs, ACS if inside else 'none', AC if inside else LN, 0, 0.8))
    o.append(T(X0 + n * cs / 2, 28, '100 × 100 bitmap, printed 4 cm wide', 13, fill=AC, bold=True))
    o.append(T(X0 + n * cs / 2, Y0 + n * cs + 22, '100 px ÷ 1.5748 in = 63.5 ppi', 13, fill=AC, bold=True))
    o.append(T(X0 + n * cs / 2, Y0 + n * cs + 40, 'each pixel ≈ 0.4 mm: a jagged edge', 13, fill=MUT))
    # smooth vector circle
    cx, cy, r = 520, 144, 102
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:var(--next-soft);stroke:var(--next);stroke-width:2.5"/>')
    o.append(L(cx - r, cy, cx + r, cy, NX, 1.6, '5 4'))
    o.append(T(cx, cy - 10, 'd = 4 cm = 1.5748 in', 13, fill=NX, bold=True))
    o.append(T(cx, 28, 'vector: circle, radius 2 cm', 13, fill=NX, bold=True))
    o.append(T(cx, Y0 + n * cs + 22, 'recomputed at 300 dpi:', 13, fill=NX, bold=True))
    o.append(T(cx, Y0 + n * cs + 40, '1.5748 × 300 = 472 dots across', 13, fill=MUT))
    return Y0 + n * cs + 56, ''.join(o)
FIG[2] = (f2, 'The same logo stored two ways. The 100 × 100 bitmap printed 4 cm wide gives only 63.5 ppi, so each pixel is about 0.4 mm and the edge is jagged; the vector circle is recomputed at 300 dpi into 472 dots and stays smooth.',
          'Left, a circle drawn as a staircase of square pixels on a coarse grid; right, a smooth circle with its 4 cm diameter marked, with the 63.5 ppi and 472-dot figures below each.')


# ---- 1.3 the frame buffer and the refresh loop ----
def f3():
    o = []
    o.append(R(20, 50, 220, 170, ACS, AC, 6, 2))
    for i in range(1, 8):
        o.append(L(20, 50 + i * 21.25, 240, 50 + i * 21.25, AC, 0.8))
    o.append(T(130, 36, 'frame buffer', 14, fill=AC, bold=True))
    o.append(T(130, 244, '1024 × 768 = 786,432 pixels', 13, fill=AC, bold=True))
    o.append(T(130, 262, '× 3 bytes = 2,359,296 B = 2.25 MiB', 13, fill=AC, bold=True))
    o.append(boxt(290, 100, 140, 70, ['video', 'controller'], PANEL, INK, 14, bold_first=True))
    o.append(L(242, 135, 286, 135, AC, 2.4, arrow='n')); o.append(T(264, 124, 'read', 13, fill=AC))
    o.append(R(500, 60, 200, 140, PANEL, INK, 8, 2.2)); o.append(R(512, 72, 176, 116, NXS, NX, 2, 1.2))
    o.append(L(600, 200, 600, 220, INK, 3)); o.append(L(560, 222, 640, 222, INK, 3))
    o.append(T(600, 136, 'monitor', 14, fill=NX, bold=True))
    o.append(L(432, 135, 496, 135, NX, 2.4, arrow='x')); o.append(T(464, 124, 'rows', 13, fill=NX))
    o.append(P([(360, 172), (360, 290), (130, 290), (130, 276)], LV, 2, '6 4'))
    o.append(T(370, 286, 'refresh 60 times a second', 13, 'start', LV, True))
    o.append(T(20, 318, '2,359,296 B × 60 = 141,557,760 B/s ≈ 141.6 MB/s read by the controller', 14, 'start', LV, True))
    return 334, ''.join(o)
FIG[3] = (f3, 'The frame buffer holds all 786,432 pixels of the 1024 × 768 screen at 3 bytes each, 2.25 MiB. The video controller re-reads the whole buffer 60 times a second, about 141.6 MB/s, and sends the rows to the monitor, so the picture never fades.',
          'A frame buffer block of 2,359,296 bytes read by a video controller that sends rows to a monitor, with a dashed loop marked 60 times a second, 141.6 MB/s.')


# ---- 1.4 RGB to CMY and HSV ----
def f4():
    o = [T(20, 26, 'Pixel (255, 128, 0), the orange #FF8000', 14, 'start', bold=True)]
    def bars(x0, title, vals, c, f):
        o.append(T(x0, 54, title, 14, 'start', c, True))
        for i, (n, v, t) in enumerate(vals):
            y = 68 + i * 40
            o.append(T(x0 + 14, y + 20, n, 14, 'end', INK, True))
            o.append(R(x0 + 22, y, 180, 28, PANEL, L2, 3, 1.2))
            if v: o.append(R(x0 + 22, y, 180 * v, 28, f, c, 3, 1.6))
            o.append(T(x0 + 210, y + 20, t, 13, 'start', c, True))
    bars(20, 'RGB scaled to 0–1', [('R', 1.0, '1'), ('G', 0.502, '0.502'), ('B', 0.0, '0')], AC, ACS)
    o.append(T(20, 206, 'CMY = 1 − RGB', 14, 'start', LV, True))
    for i, (n, v, t) in enumerate([('C', 0.0, '0'), ('M', 0.498, '0.498 (127)'), ('Y', 1.0, '1 (255)')]):
        y = 218 + i * 36
        o.append(T(34, y + 20, n, 14, 'end', INK, True))
        o.append(R(42, y, 180, 26, PANEL, L2, 3, 1.2))
        if v: o.append(R(42, y, 180 * v, 26, LVS, LV, 3, 1.6))
        o.append(T(230, y + 19, t, 13, 'start', LV, True))
    # hue wheel
    cx, cy, r = 520, 170, 110
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:var(--line2);stroke-width:2"/>')
    for ang, n in ((0, 'red 0°'), (60, 'yellow 60°'), (120, 'green 120°'), (180, 'cyan 180°'), (240, 'blue 240°'), (300, 'magenta 300°')):
        a = math.radians(ang)
        x, y = cx + r * math.cos(a), cy - r * math.sin(a)
        o.append(C(x, y, 5, L2))
        o.append(T(cx + (r + 14) * math.cos(a), cy - (r + 14) * math.sin(a) + 5, n, 13, 'start' if math.cos(a) > 0.1 else ('end' if math.cos(a) < -0.1 else 'middle'), MUT))
    a = math.radians(30.1)
    o.append(L(cx, cy, cx + r * math.cos(a), cy - r * math.sin(a), NX, 3, arrow='x'))
    o.append(f'<path d="M{cx + 46},{cy} A46,46 0 0 0 {cx + 46 * math.cos(a):.1f},{cy - 46 * math.sin(a):.1f}" style="fill:none;stroke:var(--next);stroke-width:2"/>')
    o.append(T(cx + 54, cy - 8, 'H = 30.1°', 14, 'start', NX, True))
    o.append(T(cx, cy + r + 34, 'max 1, min 0: V = 1, S = 1', 13, fill=NX, bold=True))
    o.append(T(cx, cy + r + 52, 'H = 60° × 0.502 = 30.1°, an angle, not a byte', 13, fill=MUT))
    return cy + r + 66, ''.join(o)
FIG[4] = (f4, 'The pixel (255, 128, 0) scaled to 0–1 is (1, 0.502, 0); subtracting from 1 gives CMY (0, 0.498, 1), or (0, 127, 255) in bytes. On the hue wheel it sits at 30.1° with S = 1 and V = 1, the bright orange #FF8000.',
          'Bars for R 1, G 0.502, B 0 and for C 0, M 0.498, Y 1, beside a hue wheel with red at 0°, yellow at 60° and so on, and a pointer at 30.1°.')


# ---- 1.5 a triangle in the 200 × 200 viewport ----
def f5():
    x0, x1, y0, y1 = 80, 380, 30, 330
    fx = lambda v: x0 + v / 200 * (x1 - x0)
    fy = lambda v: y1 - v / 200 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 50, 100, 150, 200], [0, 50, 100, 150, 200], fx, fy, 'x (pixels)', 'y (pixels)')]
    o.append(f'<polygon points="{fx(0)},{fy(0)} {fx(200)},{fy(0)} {fx(0)},{fy(200)}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2.5"/>')
    for (a, b) in ((0, 0), (200, 0), (0, 200)):
        o.append(C(fx(a), fy(b), 6, AC))
    o.append(T(fx(200) + 8, fy(0) - 10, '(200, 0)', 13, 'start', AC, True))
    o.append(T(fx(0) + 10, fy(200) + 6, '(0, 200)', 13, 'start', AC, True))
    o.append(T(fx(60), fy(55), 'about 20,000', 13, 'middle', AC, True)); o.append(T(fx(60), fy(55) + 18, 'fragments', 13, 'middle', AC, True))
    xr = 420
    o.append(T(xr, 60, 'vertex shader: (x, y) → (200x, 200y)', 13, 'start', INK, True))
    o.append(T(xr, 84, '(0,0) → (0,0)', 13, 'start', MUT)); o.append(T(xr, 104, '(1,0) → (200,0)', 13, 'start', MUT))
    o.append(T(xr, 124, '(0,1) → (0,200)', 13, 'start', MUT))
    o.append(T(xr, 170, 'rasteriser: one fragment', 13, 'start', INK, True)); o.append(T(xr, 190, 'per covered pixel', 13, 'start', INK, True))
    o.append(T(xr, 230, 'area = ½ × 200 × 200', 14, 'start', NX, True)); o.append(T(xr, 254, '= 20,000 px²', 14, 'start', NX, True))
    o.append(T(xr, 290, '≈ 20,000 fragment-shader runs', 13, 'start', NX, True))
    return 380, ''.join(o)
FIG[5] = (f5, 'The triangle (0,0), (200,0), (0,200) inside the 200 × 200 pixel viewport. Its area, ½ × 200 × 200 = 20,000 px², is about how many fragments reach the fragment shader, one per covered pixel.',
          'A 200 by 200 pixel viewport with a shaded right triangle on vertices (0,0), (200,0) and (0,200), beside the vertex mapping and the 20,000-fragment estimate.')


# ---- 1.6 Bresenham from (2,3) to (8,6) ----
def f6():
    o = []
    cs = 44
    fx, fy = pgrid(o, 60, 20, cs, list(range(1, 10)), list(range(2, 8)))
    pts = [(2, 3, '0'), (3, 4, '−6'), (4, 4, '0'), (5, 5, '−6'), (6, 5, '0'), (7, 6, '−6'), (8, 6, '0')]
    o.append(L(fx(2), fy(3), fx(8), fy(6), LV, 2, '6 4'))
    for i, (x, y, p) in enumerate(pts):
        nonneg = p == '0'
        pix(o, fx, fy, cs, x, y, NXS if nonneg else ACS, NX if nonneg else AC)
        o.append(T(fx(x), fy(y) + 5, p, 13, fill=NX if nonneg else AC, bold=True))
    xr = 480
    o.append(T(xr, 40, 'Δx = 6, Δy = 3', 14, 'start', INK, True))
    o.append(T(xr, 64, 'p₀ = 2Δy − Δx = 0', 14, 'start', INK, True))
    o.append(R(xr, 90, 22, 18, NXS, NX, 3, 1.6)); o.append(T(xr + 30, 104, 'p = 0: next step diagonal,', 13, 'start', NX, True))
    o.append(T(xr + 30, 122, 'p += 2Δy − 2Δx = −6', 13, 'start', NX))
    o.append(R(xr, 140, 22, 18, ACS, AC, 3, 1.6)); o.append(T(xr + 30, 154, 'p = −6: next step east,', 13, 'start', AC, True))
    o.append(T(xr + 30, 172, 'p += 2Δy = +6', 13, 'start', AC))
    o.append(T(xr, 210, 'numbers in cells: p', 13, 'start', MUT))
    o.append(T(xr, 228, 'when that pixel is plotted', 13, 'start', MUT))
    o.append(T(xr, 260, '7 pixels, (2,3) to (8,6)', 14, 'start', INK, True))
    return 20 + 6 * cs + 34, ''.join(o)
FIG[6] = (f6, 'Each shaded cell is one plotted pixel from (2,3) to (8,6), with the decision value p it carries. p = 0 sends the next step diagonally and p = −6 sends it east, so the choices alternate around the dashed ideal line.',
          'A pixel grid with seven shaded pixels (2,3), (3,4), (4,4), (5,5), (6,5), (7,6), (8,6) along a dashed ideal line, each labelled with p = 0 or −6.')


# ---- 1.7 midpoint circle, r = 8, first octant ----
def f7():
    o = []
    cs = 34
    fx, fy = pgrid(o, 50, 16, cs, list(range(0, 9)), list(range(0, 9)))
    o.append(P([(fx(8 * math.sin(t / 60 * math.pi / 2)), fy(8 * math.cos(t / 60 * math.pi / 2))) for t in range(61)], LV, 2, '6 4'))
    o.append(L(fx(0), fy(0), fx(8), fy(8), L2, 1.4, '3 3'))
    o.append(T(fx(8) - 6, fy(8) + 24, 'y = x: stop', 13, 'end', MUT, True))
    pts = [(0, 8, '−7'), (1, 8, '−4'), (2, 8, '1'), (3, 7, '−6'), (4, 7, '3'), (5, 6, '2'), (6, 5, '5')]
    for i, (x, y, p) in enumerate(pts):
        down = i > 0 and pts[i - 1][1] != y
        pix(o, fx, fy, cs, x, y, NXS if down else ACS, NX if down else AC)
        o.append(T(fx(x), fy(y) + 5, p, 13, fill=NX if down else AC, bold=True))
    xr = 400
    o.append(T(xr, 40, 'x² + y² = 64 (dashed), r = 8', 14, 'start', LV, True))
    o.append(T(xr, 66, 'p₀ = 1 − r = −7', 14, 'start', INK, True))
    o.append(R(xr, 88, 22, 18, ACS, AC, 3, 1.6)); o.append(T(xr + 30, 102, 'previous p < 0: y stays', 13, 'start', AC, True))
    o.append(R(xr, 116, 22, 18, NXS, NX, 3, 1.6)); o.append(T(xr + 30, 130, 'previous p ≥ 0: y − 1', 13, 'start', NX, True))
    o.append(T(xr, 168, 'cell number = p after that pixel', 13, 'start', MUT))
    o.append(T(xr, 204, '8-way symmetry: (3, 7) also gives', 13, 'start', INK, True))
    o.append(T(xr, 224, '(7, 3), (−3, 7), (−7, 3), (−3, −7),', 13, 'start', MUT))
    o.append(T(xr, 244, '(−7, −3), (3, −7), (7, −3)', 13, 'start', MUT))
    return 16 + 9 * cs + 34, ''.join(o)
FIG[7] = (f7, 'The seven first-octant pixels for r = 8 hug the true arc x² + y² = 64. x rises by one every step, and y drops only after the steps where p was zero or positive, the green cells.',
          'A quarter grid from 0 to 8 with the dashed arc of radius 8 and seven shaded pixels (0,8), (1,8), (2,8), (3,7), (4,7), (5,6), (6,5), each labelled with its p value, and the dashed line y = x where the octant stops.')


# ---- 1.8 scan-line fill of a trapezoid ----
def f8():
    o = []
    cs = 38
    fx, fy = pgrid(o, 50, 16, cs, list(range(0, 11)), list(range(0, 9)))
    poly = [(1, 1), (9, 1), (7, 7), (3, 7)]
    for y, a, b, xs_ in ((4, 2.0, 8.0, range(2, 9)), (6, 2.667, 7.333, range(3, 8))):
        for x in xs_:
            pix(o, fx, fy, cs, x, y, NXS if y == 4 else ACS, NX if y == 4 else AC)
    o.append(f'<polygon points="{" ".join(f"{fx(x)},{fy(y)}" for x, y in poly)}" style="fill:none;stroke:var(--live);stroke-width:2.5"/>')
    for y, a, b, c in ((4, 2.0, 8.0, NX), (6, 2.667, 7.333, AC)):
        o.append(L(fx(a), fy(y), fx(b), fy(y), c, 2))
        o.append(C(fx(a), fy(y), 5, c)); o.append(C(fx(b), fy(y), 5, c))
    xr = 480
    o.append(T(xr, 50, 'polygon (1,1) (9,1) (7,7) (3,7)', 13, 'start', LV, True))
    o.append(T(xr, 92, 'y = 4: span 2.0 to 8.0', 14, 'start', NX, True))
    o.append(T(xr, 112, 'centres 2 … 8 → 7 pixels', 13, 'start', NX))
    o.append(T(xr, 152, 'y = 6: span 2.667 to 7.333', 14, 'start', AC, True))
    o.append(T(xr, 172, 'centres 3 … 7 → 5 pixels', 13, 'start', AC))
    o.append(T(xr, 214, 'left edge x = 1 + (y − 1)/6 × 2', 13, 'start', MUT))
    o.append(T(xr, 234, 'right edge x = 9 − (y − 1)/6 × 2', 13, 'start', MUT))
    o.append(T(xr, 266, 'horizontal edges are skipped', 13, 'start', MUT))
    return 16 + 9 * cs + 34, ''.join(o)
FIG[8] = (f8, 'Scan-line fill of the polygon (1,1), (9,1), (7,7), (3,7). At y = 4 the span runs from x = 2.0 to 8.0 and fills 7 pixels; at y = 6 it runs from 2.667 to 7.333 and fills 5, because only integer centres inside the span count.',
          'A pixel grid with the trapezoid outline and two filled rows: y = 4 with seven pixels from x 2 to 8, and y = 6 with five pixels from x 3 to 7, the span end points marked.')


# ---- 1.9 scanning a passport photo ----
def f9():
    o = []
    o.append(R(30, 50, 160, 120, PANEL, INK, 4, 2))
    o.append(T(110, 40, '4 cm × 3 cm photo', 13, fill=INK, bold=True))
    o.append(f'<circle cx="110" cy="96" r="22" style="fill:none;stroke:var(--line2);stroke-width:2"/>')
    o.append(P([(70, 170), (80, 136), (140, 136), (150, 170)], L2, 2))
    o.append(L(194, 110, 246, 110, AC, 2.4, arrow='n')); o.append(T(220, 98, '300 ppi', 13, fill=AC, bold=True))
    o.append(R(252, 50, 160, 120, ACS, AC, 2, 2))
    for i in range(1, 8):
        o.append(L(252 + i * 20, 50, 252 + i * 20, 170, AC, 0.6)); o.append(L(252, 50 + i * 15, 412, 50 + i * 15, AC, 0.6))
    o.append(T(332, 40, '472 × 354 pixels', 13, fill=AC, bold=True))
    o.append(T(332, 190, '4 ÷ 2.54 × 300 = 472.4 → 472', 13, fill=MUT))
    o.append(T(332, 208, '3 ÷ 2.54 × 300 = 354.3 → 354', 13, fill=MUT))
    o.append(T(560, 100, '472 × 354', 15, fill=INK, bold=True)); o.append(T(560, 124, '= 167,088 pixels', 15, fill=INK, bold=True))
    sc = 0.0006
    y = 240
    for i, (n, b, kib, c, f) in enumerate((('24-bit colour, 3 B/px', 501264, '501,264 B = 489.5 KiB', LV, LVS), ('8-bit grey, 1 B/px', 167088, '167,088 B = 163.2 KiB', NX, NXS))):
        yy = y + i * 44
        o.append(T(180, yy + 22, n, 13, 'end', c, True))
        o.append(R(190, yy, b * sc, 32, f, c, 3, 1.6))
        o.append(T(198 + b * sc, yy + 22, kib, 13, 'start', c, True))
    o.append(T(20, y + 110, 'Same pixels in both files; only the bytes per pixel change, so grey is a third of colour.', 13, 'start', MUT))
    return y + 126, ''.join(o)
FIG[9] = (f9, 'A 4 cm × 3 cm photo scanned at 300 ppi becomes 472 × 354 = 167,088 pixels. Both files hold the same pixels; only the bytes per pixel change, so colour needs 489.5 KiB and grey 163.2 KiB.',
          'A photo of 4 by 3 cm, an arrow labelled 300 ppi to a pixel grid of 472 by 354, the count 167,088 pixels, and two storage bars of 489.5 KiB for colour and 163.2 KiB for grey.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        2: [
            ('= 63.499... ppi, rounded to 63.5 ppi.',
             '= 63.500... ppi, rounded to 63.5 ppi.'),
            ('In the figure, 1 means ink and 0 means paper, so the 1s draw the letter L.',
             'In a 1-bit bitmap, 1 means ink and 0 means paper, so a pattern of 1s can draw a letter such as L.')],
        3: [(' Only a few universities teach this display hardware in depth.', ''),
            ('The figure shows the chain.',
             'The figure shows the last link: the video controller re-reading the frame buffer for every refresh.')],
        5: [(' Only a few universities teach this depth.', ''),
            ('The figure shows six of these eight stages, leaving out clipping and the per-fragment tests for space.',
             'The figure follows one triangle from its three vertices to the roughly 20,000 fragments the rasterizer makes in a 200 × 200 viewport.')],
        9: [('shrinking by two replaces each 2 × 2 block with its mean, as the figure shows.',
             'shrinking by two replaces each 2 × 2 block with its mean.')],
    }.get(k, [])
