"""Claude's hand-drawn figures for c-graphics-u5 (Computer Graphics and Multimedia, unit 5: animation, morphing,
authoring tools, image editing, vector paths and timeline tweens), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def ell(cx, cy, rx, ry, fill, c, w=2.4, dash=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" style="fill:{fill};stroke:{c};stroke-width:{w}{d}"/>'


def hdim(o, x1, x2, y, label, c=INK, below=True):
    """horizontal dimension line with end ticks and a label"""
    o.append(L(x1, y, x2, y, c, 1.4)); o.append(L(x1, y - 6, x1, y + 6, c, 1.4)); o.append(L(x2, y - 6, x2, y + 6, c, 1.4))
    o.append(T((x1 + x2) / 2, y + (20 if below else -8), label, 13, 'middle', c, True))


def vdim(o, x, y1, y2, label, c=INK, right=True):
    o.append(L(x, y1, x, y2, c, 1.4)); o.append(L(x - 6, y1, x + 6, y1, c, 1.4)); o.append(L(x - 6, y2, x + 6, y2, c, 1.4))
    o.append(T(x + (10 if right else -10), (y1 + y2) / 2 + 5, label, 13, 'start' if right else 'end', c, True))


# ---- 5.1 squash with constant volume, and spacing ----
def f1():
    o = []
    s, floor = 130, 200
    o.append(L(30, floor, 690, floor, L2, 2))
    # round ball
    cx = 130
    o.append(ell(cx, floor - 0.5 * s, 0.5 * s, 0.5 * s, ACS, AC))
    hdim(o, cx - 0.5 * s, cx + 0.5 * s, floor + 18, 'width 1 unit', AC)
    vdim(o, cx - 0.5 * s - 18, floor - s, floor, '1', AC, False)
    o.append(T(cx, 26, 'before impact, r = 0.5', 13, 'middle', AC, True))
    # squashed
    cx2 = 420
    a, c = 0.6455, 0.3
    o.append(ell(cx2, floor - c * s, 0.5 * s, 0.5 * s, 'none', L2, 1.4, '5 4'))
    o.append(ell(cx2, floor - c * s, a * s, c * s, NXS, NX))
    hdim(o, cx2 - a * s, cx2 + a * s, floor + 18, 'width 2a = 1.29 units', NX)
    vdim(o, cx2 + a * s + 18, floor - 2 * c * s, floor, 'height 0.6', NX)
    o.append(T(cx2, 26, 'maximum squash, same volume', 13, 'middle', NX, True))
    o.append(T(cx2, floor - 2 * c * s - 34, 'dashed: the round ball', 13, 'middle', MUT))
    xr = 40
    y = 270
    o.append(T(xr, y, 'keep volume: (4/3)πa²c = (4/3)πr³, so a²c = r³', 14, 'start', INK, True))
    o.append(T(xr, y + 24, 'a² × 0.3 = 0.5³ = 0.125  →  a² = 0.41667  →  a = 0.6455,  width 2a = 1.29 units', 14, 'start', NX, True))
    # spacing strip
    ys = y + 60
    o.append(T(xr, ys, 'spacing over one bounce (one dot per frame)', 13, 'start', MUT, True))
    base = ys + 134
    o.append(L(60, base + 8, 660, base + 8, L2, 1.6))
    n = 12
    for i in range(n + 1):
        u = i / n
        x = 80 + u * 560
        h = 4 * u * (1 - u)
        y_ = base - h * 90
        near = h < 0.4
        o.append(C(x, y_, 6, AC if near else LV))
    o.append(T(360, base - 102, 'tight spacing: hangs at the top, reads slow', 13, 'middle', LV, True))
    o.append(T(80, base + 30, 'wide spacing near the floor:', 13, 'start', AC, True))
    o.append(T(80, base + 48, '2-frame squash, 2-frame recovery', 13, 'start', AC))
    return base + 60, ''.join(o)
FIG[1] = (f1, 'The ball 1 unit wide squashes to 0.6 high. Keeping its volume, a²c = r³ gives a = 0.6455, so it spreads to 1.29 units wide. The squash takes only 2 frames, wide spacing for a fast hit, while tight spacing at the top makes it hang.',
          'A round ball 1 unit wide on the floor beside the squashed ellipse 0.6 high and 1.29 wide, with the round outline dashed inside it; below, the volume equation and a bounce arc of frame dots, close together at the top and far apart near the floor.')


# ---- 5.2 linear tween between two keys ----
def f2():
    o = []
    x0, x1, y0, y1 = 80, 470, 30, 310
    fx = lambda f: x0 + f / 10 * (x1 - x0)
    fy = lambda v: y1 - (v - 0) / 130 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, list(range(0, 11)), [0, 20, 40, 60, 80, 100, 120], fx, fy, 'frame (24 fps)', 'x (px)'))
    o.append(L(fx(0), fy(20), fx(10), fy(120), AC, 2.4))
    for f in range(11):
        key = f in (0, 10)
        o.append(C(fx(f), fy(20 + 10 * f), 8 if key else 5, NX if key else AC))
    o.append(T(fx(0) + 12, fy(20) + 5, 'key 0: 20 px', 13, 'start', NX, True))
    o.append(T(fx(10) - 12, fy(120) - 10, 'key 10: 120 px', 13, 'end', NX, True))
    o.append(L(x0, fy(75), fx(5.5), fy(75), LV, 1.6, '5 4')); o.append(L(fx(5.5), fy(75), fx(5.5), y1, LV, 1.6, '5 4'))
    o.append(C(fx(5.5), fy(75), 6, LV))
    o.append(Tb(fx(5.5) + 10, fy(75) + 20, '75 px at frame 5.5', 13, 'start', LV, True))
    xr = 500
    lines = [('step = 100 px ÷ 10 frames', INK, True), ('= 10 px per frame', INK, True), ('', 0, 0),
             ('frame 2: 40 px', AC, False), ('frame 4: 60 px', AC, False), ('frame 6: 80 px', AC, False), ('frame 8: 100 px', AC, False), ('', 0, 0),
             ('x = 75: u = 55 ÷ 100 = 0.55', LV, True), ('frame 0.55 × 10 = 5.5', LV, False), ('t = 5.5 ÷ 24 = 0.2292 s', LV, True)]
    for i, (t, c, b) in enumerate(lines):
        if t: o.append(T(xr, 46 + i * 22, t, 13, 'start', c, b))
    return 360, ''.join(o)
FIG[2] = (f2, 'Keys at frame 0 (x = 20 px) and frame 10 (x = 120 px) with the straight linear tween between them; each computed in-between is 10 px further on. The value 75 px falls between frames, at 5.5, which is 0.2292 s at 24 fps.',
          'A graph of x in pixels against frame from 0 to 10: a straight line from the key at 20 px to the key at 120 px with a dot at every frame, and dashed guides marking 75 px at frame 5.5.')


# ---- 5.3 one t for warp and dissolve ----
def f3():
    o = []
    s, X0, Y0 = 4.2, 70, 50
    fx = lambda v: X0 + v * s
    fy = lambda v: Y0 + v * s  # y grows downward (origin top-left)
    o.append(L(fx(0), fy(0), fx(112), fy(0), L2, 1.6, arrow='m')); o.append(L(fx(0), fy(0), fx(0), fy(52), L2, 1.6, arrow='m'))
    for v in (0, 30, 50, 100):
        o.append(L(fx(v), fy(0) - 5, fx(v), fy(0), L2, 1.4)); o.append(T(fx(v), fy(0) - 10, str(v), 13, fill=MUT))
    for v in (12, 40):
        o.append(L(fx(0) - 5, fy(v), fx(0), fy(v), L2, 1.4)); o.append(T(fx(0) - 9, fy(v) + 4.5, str(v), 13, 'end', MUT))
    o.append(T(fx(112), fy(0) + 18, 'x (px)', 13, 'end', MUT, True)); o.append(T(fx(0) + 8, fy(52) + 4, 'y (px), down', 13, 'start', MUT, True))
    o.append(L(fx(0), fy(0), fx(100), fy(40), L2, 1.8, '6 4'))
    o.append(L(fx(30), fy(0), fx(30), fy(12), LV, 1.2, '3 3')); o.append(L(fx(0), fy(12), fx(30), fy(12), LV, 1.2, '3 3'))
    o.append(C(fx(0), fy(0), 7, AC)); o.append(C(fx(100), fy(40), 7, NX)); o.append(C(fx(30), fy(12), 7, LV))
    o.append(T(fx(0) - 10, fy(0) - 10, 'A (0, 0)', 13, 'end', AC, True))
    o.append(T(fx(100) + 10, fy(40) + 20, 'B (100, 40)', 13, 'middle', NX, True))
    o.append(Tb(fx(30) + 12, fy(12) + 22, 'P(0.3) = (30, 12)', 13, 'start', LV, True))
    o.append(T(fx(60), 84, 'x = 0.7 × 0 + 0.3 × 100 = 30', 13, 'start', INK))
    o.append(T(fx(60), 104, 'y = 0.7 × 0 + 0.3 × 40 = 12', 13, 'start', INK))
    # dissolve
    yb = 336
    o.append(T(40, yb - 16, 'cross-dissolve at the same t = 0.3', 14, 'start', INK, True))
    o.append(boxt(40, yb, 120, 50, ['source', 'weight 0.7'], ACS, AC, 13, True))
    o.append(T(176, yb + 30, '+', 18, 'middle', INK, True))
    o.append(boxt(192, yb, 120, 50, ['target', 'weight 0.3'], NXS, NX, 13, True))
    o.append(T(328, yb + 30, '=', 18, 'middle', INK, True))
    o.append(R(344, yb, 0.7 * 330, 50, ACS, AC, 0, 2)); o.append(R(344 + 0.7 * 330, yb, 0.3 * 330, 50, NXS, NX, 0, 2))
    o.append(T(344 + 0.35 * 330, yb + 31, '0.7 C_A', 13, 'middle', AC, True)); o.append(T(344 + 0.85 * 330, yb + 31, '0.3 C_B', 13, 'middle', NX, True))
    o.append(T(40, yb + 80, 'weights add to 1.0, so brightness holds; shape and colour move together because both read t = 0.3', 13, 'start', MUT))
    return yb + 96, ''.join(o)
FIG[3] = (f3, 'Warp and dissolve read the same t = 0.3. The control point moves 0.3 of the way from A(0, 0) to B(100, 40), landing at (30, 12), while each colour is 0.7 of the source and 0.3 of the target, so outline and colour change together.',
          'Pixel axes with the origin at the top left, the dashed path from A(0,0) to B(100,40) and the point P(0.3) = (30,12) on it; below, a source box weighted 0.7 plus a target box weighted 0.3 equals a bar split 70 to 30.')


# ---- 5.4 frames, keys and in-betweens ----
def f4():
    o = []
    cw, X0, y = 19, 40, 60
    o.append(T(X0, y - 24, 'the first 30 of 240 frames: one key pose every 6 frames', 14, 'start', INK, True))
    for i in range(30):
        key = i % 6 == 0
        o.append(R(X0 + i * cw, y, cw, 40, NXS if key else PANEL, NX if key else L2, 0, 1.6 if key else 1))
        if i % 6 == 0 or i == 29:
            o.append(T(X0 + i * cw + cw / 2, y + 60, str(i + 1), 13, 'middle', NX if key else MUT, True))
        if key:
            o.append(T(X0 + i * cw + cw / 2, y + 26, 'K', 13, 'middle', NX, True))
    o.append(T(X0 + 30 * cw + 8, y + 26, '…', 18, 'start', MUT, True))
    o.append(brace(X0 + 2, X0 + 6 * cw - 2, y + 74, LV))
    o.append(T(X0 + 3 * cw, y + 94, '1 key + 5 in-betweens', 13, 'middle', LV, True))
    o.append(T(X0 + 30 * cw + 30, y + 60, 'frame', 13, 'start', MUT))
    yc = y + 150
    rows = [('frames', '24 frames/s × 10 s', '240', INK, PANEL), ('key poses', '240 ÷ 6', '40', NX, NXS), ('in-betweens', '240 − 40', '200', AC, ACS)]
    for i, (a, b, v, c, f) in enumerate(rows):
        yy = yc + i * 52
        o.append(T(X0, yy + 27, a, 14, 'start', c, True))
        o.append(T(X0 + 130, yy + 27, b, 14, 'start', INK))
        o.append(T(X0 + 300, yy + 27, '=', 14, 'start', INK))
        sc = 1.1
        o.append(R(X0 + 324, yy + 8, int(v) * sc, 28, f, c, 0, 1.8))
        o.append(T(X0 + 324 + int(v) * sc + 10, yy + 27, v, 15, 'start', c, True))
    o.append(T(X0, yc + 176, 'check: 40 + 200 = 240 frames', 13, 'start', MUT, True))
    return yc + 192, ''.join(o)
FIG[4] = (f4, 'A 10 s cel clip at 24 fps is 240 frames. With a key pose every 6 frames, each group of six is 1 key and 5 in-betweens, so the clip needs 40 keys and 200 in-betweens.',
          'A strip of the first 30 frame cells with every sixth cell marked K for a key pose and a brace over one group of six; below, bars for 240 frames, 40 key poses and 200 in-betweens with their sums.')


# ---- 5.5 the card deck, and a flat timeline ----
def f5():
    o = []
    def stack(x, y, n, lab, f, c, w=110, h=60):
        k = min(n, 4)
        for i in range(k - 1, -1, -1):
            o.append(R(x + i * 6, y - i * 6, w, h, f, c, 6, 1.8))
        o.append(T(x + w / 2, y + h / 2 - 2, lab, 13, 'middle', c, True))
        o.append(T(x + w / 2, y + h / 2 + 16, f'{n} card' + ('s' if n > 1 else ''), 13, 'middle', INK))
    y = 60
    stack(40, y, 1, 'menu', PANEL, INK)
    stack(200, y, 12, 'lessons', ACS, AC)
    stack(380, y, 5, 'quizzes', LVS, LV)
    stack(560, y, 1, 'score', NXS, NX)
    for xa, xb in ((152, 196), (330, 376), (510, 556)):
        o.append(L(xa, y + 30, xb, y + 30, INK, 2, arrow='m'))
    o.append(arc(430, y + 64, 260, y + 64, 0.35, LV, 2, 'l', '6 4'))
    o.append(T(345, y + 116, 'wrong answer: jump back to a lesson', 13, 'middle', LV, True))
    o.append(T(360, 28, 'card-based: 1 + 12 + 5 + 1 = 19 cards', 14, 'middle', INK, True))
    yt = 230
    o.append(T(40, yt - 18, 'time-based rebuild: each card plays once for 30 s', 14, 'start', INK, True))
    cw = 640 / 19
    for i in range(19):
        f, c = (PANEL, INK) if i == 0 else (ACS, AC) if i <= 12 else (LVS, LV) if i <= 17 else (NXS, NX)
        o.append(R(40 + i * cw, yt, cw, 34, f, c, 0, 1.4))
    o.append(xaxis(40, 680, yt + 34, [0, 3, 6, 9, 12, 15, 19], lambda v: 40 + v * cw, None, lambda v: f'{v * 30}'))
    o.append(T(680, yt + 74, 'seconds', 13, 'end', MUT))
    o.append(T(360, yt + 100, '19 × 30 s = 570 s = 9.5 min, but the quiz branch is lost', 14, 'middle', NX, True))
    return yt + 116, ''.join(o)
FIG[5] = (f5, 'The card deck needs 19 cards: 1 menu, 12 lessons, 5 quizzes and 1 score, with the quiz able to jump back to a lesson. Rebuilt as a flat time-based title at 30 s a card, every screen plays once: 570 s, or 9.5 minutes, and the jump back is gone.',
          'Four card stacks, menu 1, lessons 12, quizzes 5 and score 1, joined by arrows with a dashed arrow from the quizzes back to the lessons; below, a timeline of 19 cells of 30 s each reaching 570 s.')


# ---- 5.6 resampling at a fixed print size ----
def f6():
    o = []
    side = 200
    for k, (x, dpi, n, f, c, px, mb) in enumerate(((60, 300, 24, ACS, AC, '1200 × 1200 px', '4.32 MB'), (400, 150, 12, NXS, NX, '600 × 600 px', '1.08 MB'))):
        y = 50
        o.append(R(x, y, side, side, f, c, 0, 2.2))
        st = side / n
        for i in range(1, n):
            o.append(L(x + i * st, y, x + i * st, y + side, c, 0.6)); o.append(L(x, y + i * st, x + side, y + i * st, c, 0.6))
        o.append(T(x + side / 2, y - 14, f'{dpi} dpi', 14, 'middle', c, True))
        hdim(o, x, x + side, y + side + 16, '4 in', INK)
        o.append(T(x + side / 2, y + side + 62, f'4 × {dpi} = {px}', 14, 'middle', c, True))
        o.append(T(x + side / 2, y + side + 84, f'× 3 B = {mb}', 14, 'middle', c, True))
    o.append(L(278, 150, 386, 150, LV, 2.4, arrow='l')); o.append(T(332, 140, 'resample', 13, 'middle', LV, True))
    o.append(T(620, 120, 'grid lines:', 13, 'start', MUT)); o.append(T(620, 138, 'every 50 px', 13, 'start', MUT))
    o.append(T(360, 370, 'same 4 in print; pixels 1,440,000 → 360,000 and bytes 4,320,000 → 1,080,000: both one quarter', 13, 'middle', INK, True))
    return 386, ''.join(o)
FIG[6] = (f6, 'The same 4 in × 4 in print before and after resampling: 1200 × 1200 px and 4.32 MB at 300 dpi become 600 × 600 px and 1.08 MB at 150 dpi. Halving the dpi quarters the pixels and the bytes; the printed size does not change.',
          'Two equal 4 inch squares, the left with a dense grid labelled 300 dpi, 1200 by 1200 px, 4.32 MB, the right with a grid half as dense labelled 150 dpi, 600 by 600 px, 1.08 MB, joined by a resample arrow.')


# ---- 5.7 layer, opacity and mask ----
def f7():
    o = []
    # layer stack in perspective
    def layer(y, lab, f, c):
        pts = [(60, y + 30), (200, y), (300, y + 20), (160, y + 50)]
        o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" style="fill:{f};stroke:{c};stroke-width:2"/>')
        o.append(T(310, y + 30, lab, 13, 'start', c, True))
    layer(40, 'blue fill (0, 0, 255), opacity 0.5', ACS, AC)
    layer(110, 'mask: 40% white = 0.4', PANEL, MUT)
    layer(180, 'background (200, 100, 50)', NXS, NX)
    o.append(T(60, 290, 'α = opacity × mask = 0.5 × 0.4 = 0.2', 15, 'start', LV, True))
    o.append(T(60, 314, 'result = 0.2 × top + 0.8 × below, each channel', 13, 'start', MUT))
    # table
    xt, yt = 60, 346
    widths = [90, 90, 90, 230, 90]
    head = ['channel', 'below', 'top', '0.8 × below + 0.2 × top', 'result']
    rows = [['R', '200', '0', '160 + 0', '160'], ['G', '100', '0', '80 + 0', '80'], ['B', '50', '255', '40 + 51', '91']]
    rh = 28
    o.append(R(xt, yt, sum(widths), rh, ACS, AC, 0, 1.4))
    cx = xt
    for w, h in zip(widths, head):
        o.append(T(cx + w / 2, yt + 19, h, 13, 'middle', AC, True)); cx += w
    for i, r in enumerate(rows):
        yy = yt + rh * (i + 1)
        o.append(R(xt, yy, sum(widths), rh, 'none', LN, 0, 1))
        cx = xt
        for j, (w, v) in enumerate(zip(widths, r)):
            c = NX if j == 1 else AC if j == 2 else LV if j == 4 else INK
            o.append(T(cx + w / 2, yy + 19, v, 14, 'middle', c, j in (0, 4))); cx += w
    o.append(R(xt, yt, sum(widths), rh * 4, 'none', L2, 0, 1.4))
    o.append(T(xt + sum(widths), yt + rh * 4 + 24, 'composite pixel (160, 80, 91)', 14, 'end', LV, True))
    return yt + rh * 4 + 40, ''.join(o)
FIG[7] = (f7, 'The blue layer\'s opacity 0.5 times the mask value 0.4 gives an effective alpha of 0.2, so each channel takes 0.2 of the top layer and 0.8 of the background. Blue rises from 50 to 91 while red falls from 200 to 160: the pixel becomes (160, 80, 91).',
          'Three stacked layers, the blue fill at opacity 0.5, the mask at 0.4 and the background (200, 100, 50), with α = 0.5 × 0.4 = 0.2, above a table that mixes each channel to give the result (160, 80, 91).')


# ---- 5.8 a cubic Bezier path ----
def f8():
    o = []
    s, X0, Y0 = 5.2, 90, 320
    fx = lambda v: X0 + v * s
    fy = lambda v: Y0 - v * s
    o.append(axes(X0, fx(56), fy(56), Y0, [0, 10, 20, 25, 30, 40, 50], [0, 10, 20, 30, 37.5, 50], fx, fy, 'x (mm)', 'y (mm)', str, lambda v: f'{v:g}'))
    Pp = [(0, 0), (0, 50), (50, 50), (50, 0)]
    o.append(L(fx(0), fy(0), fx(0), fy(50), L2, 2, '6 4')); o.append(L(fx(50), fy(0), fx(50), fy(50), L2, 2, '6 4'))
    o.append(L(fx(0), fy(50), fx(50), fy(50), L2, 1.2, '2 4'))
    bz = lambda t: tuple((1 - t) ** 3 * Pp[0][i] + 3 * t * (1 - t) ** 2 * Pp[1][i] + 3 * t * t * (1 - t) * Pp[2][i] + t ** 3 * Pp[3][i] for i in range(2))
    o.append(P([(fx(bz(i / 60)[0]), fy(bz(i / 60)[1])) for i in range(61)], AC, 3))
    for (x, y), lab, an, dx, dy, c in (((0, 0), 'P₀ (0, 0) anchor', 'start', 12, -6, AC), ((0, 50), 'P₁ (0, 50)', 'start', 12, 5, MUT),
                                        ((50, 50), 'P₂ (50, 50)', 'end', -12, 5, MUT), ((50, 0), 'P₃ (50, 0) anchor', 'end', -12, -6, AC)):
        o.append(C(fx(x), fy(y), 6.5, c if c == AC else L2)); o.append(T(fx(x) + dx, fy(y) + dy, lab, 13, an, c, True))
    o.append(C(fx(25), fy(37.5), 7, NX))
    o.append(T(fx(25), fy(37.5) - 14, 'B(0.5) = (25, 37.5)', 13, 'middle', NX, True))
    o.append(L(fx(0), fy(2), fx(0), fy(22), LV, 3, arrow='l'))
    o.append(T(fx(0) - 30, fy(25) + 5, 'B′(0)', 13, 'end', LV, True))
    o.append(T(fx(25), fy(50) - 10, 'handles', 13, 'middle', MUT))
    xr = 420
    o.append(T(xr, 60, 'weights at t = 0.5:', 14, 'start', INK, True))
    o.append(T(xr, 82, '0.125, 0.375, 0.375, 0.125', 13, 'start', INK))
    o.append(T(xr, 116, 'x = 0.375 × 50 + 0.125 × 50 = 25', 13, 'start', NX))
    o.append(T(xr, 138, 'y = 0.375 × 50 + 0.375 × 50 = 37.5', 13, 'start', NX))
    o.append(T(xr, 176, 'B′(0) = 3(P₁ − P₀) = (0, 150)', 13, 'start', LV, True))
    o.append(T(xr, 198, 'straight up: the path leaves P₀', 13, 'start', LV))
    o.append(T(xr, 218, 'along its handle', 13, 'start', LV))
    o.append(T(xr, 254, 'the curve bends toward the', 13, 'start', MUT))
    o.append(T(xr, 274, 'handles but never touches them', 13, 'start', MUT))
    return 370, ''.join(o)
FIG[8] = (f8, 'The path runs from anchor P₀(0, 0) to anchor P₃(50, 0); the handles P₁ and P₂ pull it up without being touched. It peaks at B(0.5) = (25, 37.5) mm, and because P₁ is straight above P₀, the path leaves P₀ going straight up.',
          'Axes in millimetres with a blue arch from (0,0) to (50,0), dashed handle lines up to P1 (0,50) and P2 (50,50), the point B(0.5) = (25, 37.5) marked at the top and an upward tangent arrow beside P0.')


# ---- 5.9 a tween and its motion blur ----
def f9():
    o = []
    x0, x1, y0, y1 = 80, 440, 30, 300
    fx = lambda f: x0 + f / 24 * (x1 - x0)
    fy = lambda v: y1 - (v - 0) / 420 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 6, 12, 18, 24], [0, 100, 200, 300, 400], fx, fy, 'frame (24 fps), frame 24 = 1 s', 'x (px)'))
    o.append(L(fx(0), fy(100), fx(24), fy(400), AC, 2.4))
    for f in range(25):
        key = f in (0, 24)
        o.append(C(fx(f), fy(100 + 12.5 * f), 7 if key else 3.5, NX if key else AC))
    o.append(T(fx(0) + 12, fy(100) + 5, 'key: 100 px at 0 s', 13, 'start', NX, True))
    o.append(T(fx(24) - 12, fy(400) - 10, 'key: 400 px at 1 s', 13, 'end', NX, True))
    o.append(T(fx(14) + 8, fy(275) + 30, '12.5 px per frame', 13, 'start', AC, True))
    xr = 480
    o.append(T(xr, 50, '300 px in 1 s = 300 px/s', 14, 'start', INK, True))
    o.append(T(xr, 76, 'shutter open 1/48 s', 14, 'start', INK))
    o.append(T(xr, 102, 'blur = 300 × 1/48 = 6.25 px', 14, 'start', LV, True))
    # blur inset, zoomed 8x
    z = 8
    bx, by = xr + 10, 170
    o.append(T(xr, by - 18, 'one frame, drawn 8 × size:', 13, 'start', MUT))
    o.append(R(bx, by, 6.25 * z + 40, 40, LVS, 'none', 20, 0))
    o.append(f'<circle cx="{bx + 20:.1f}" cy="{by + 20}" r="20" style="fill:none;stroke:var(--line2);stroke-width:1.6;stroke-dasharray:4 3"/>')
    o.append(f'<circle cx="{bx + 20 + 6.25 * z:.1f}" cy="{by + 20}" r="20" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    hdim(o, bx + 20, bx + 20 + 6.25 * z, by + 58, '6.25 px smear', LV)
    o.append(T(xr, by + 120, 'shutter half the frame time:', 13, 'start', MUT))
    o.append(T(xr, by + 138, '1/48 s of each 1/24 s frame', 13, 'start', MUT))
    return 350, ''.join(o)
FIG[9] = (f9, 'Keys at x = 100 px (0 s) and x = 400 px (1 s) with 24 frames at 24 fps between them, a straight path of 12.5 px a frame, 300 px/s. With the shutter open 1/48 s, the ball smears 300 × 1/48 = 6.25 px in each frame.',
          'A graph of x against frame from 0 to 24 with a straight tween from 100 px to 400 px and a dot at every frame; beside it the speed 300 px/s and a zoomed ball smeared 6.25 px during the 1/48 s shutter.')


spec = make_spec(FIG)
