"""Claude's hand-drawn figures for c-cv-u4 (Computer Vision, unit 4: segmentation and description), one per chapter,
from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARR = {AC: 'n', L2: 'm', LV: 'l', NX: 'x', MUT: 'm', INK: 'm'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=ARR[c])


def mat(x, y, M, cell=48, hot=None, size=15, f0=PANEL):
    o = []
    for i, row in enumerate(M):
        for j, v in enumerate(row):
            h = hot(i, j) if hot else None
            f, st = h if h else (f0, L2)
            o += [R(x + j * cell, y + i * cell, cell, cell, f, st, 0, 1.6 if h else 1.2), TM(x + j * cell + cell / 2, y + i * cell + cell * 0.62, str(v), size, bold=bool(h))]
    return ''.join(o)


def row(x, y, vals, cw=30, h=32, f=PANEL, st=L2, size=14, bold=False):
    o = []
    for i, v in enumerate(vals):
        o += [R(x + i * cw, y, cw, h, f, st, 0, 1.2), TM(x + i * cw + cw / 2, y + h * 0.66, str(v), size, bold=bold)]
    return ''.join(o)


# ---- 4.1 line masks on a horizontal line ----
def f1():
    o = [T(20, 92, 'window', 14, 'start', INK, True), mat(20, 102, [[0, 0, 0], [3, 3, 3], [0, 0, 0]], 40, lambda i, j: (ACS, AC) if i == 1 else None, 14)]
    for y, name, M, P_, res, verdict, c, cs in ((46, 'horizontal mask', [['−1', '−1', '−1'], [2, 2, 2], ['−1', '−1', '−1']], [[0, 0, 0], [6, 6, 6], [0, 0, 0]], 'R = 18', '18 > 10: line pixel', LV, LVS),
                                                (180, 'vertical mask', [['−1', 2, '−1'], ['−1', 2, '−1'], ['−1', 2, '−1']], [[0, 0, 0], ['−3', 6, '−3'], [0, 0, 0]], 'R = 0', '0 < 10: not vertical', MUT, PANEL)):
        o += [T(180, y - 8, name, 13, 'start', INK, True), mat(180, y, M, 34, size=13), T(298, y + 58, '→', 18, fill=MUT, bold=True)]
        o += [T(320, y - 8, 'products', 13, 'start', MUT), mat(320, y, P_, 34, lambda i, j: (cs, c) if i == 1 and c == LV else None, 13)]
        o += [ar(430, y + 51, 456, y + 51, c if c != MUT else L2), boxt(460, y + 20, 240, 62, [res, verdict], cs, c, 14, True)]
    o += [T(160, 160, '×', 18, fill=MUT, bold=True)]
    o.append(T(20, 316, 'Point mask on a lone 5 with eight 0 neighbours: R = 8 × 5 = 40 > 20, an isolated point.', 13, 'start', NX, True))
    return 330, ''.join(o)


FIG[1] = (f1, 'The window 0 0 0 / 3 3 3 / 0 0 0 times the horizontal mask gives products 6, 6, 6 in the middle row, so R = 18 > 10: a horizontal line pixel. The vertical mask gives −3 + 6 − 3 = 0.',
          'The window with a row of 3s, the horizontal mask and its products 0 0 0 / 6 6 6 / 0 0 0 summing to 18, then the vertical mask and its products 0 0 0 / −3 6 −3 / 0 0 0 summing to 0. A note gives the point mask response 40 > 20.')


# ---- 4.2 Sobel gradient and the Canny thresholds ----
def f2():
    P_ = [[10, 10, 50], [10, 10, 50], [10, 10, 50]]
    o = [T(20, 40, 'patch', 14, 'start', INK, True), mat(20, 50, P_, 44, lambda i, j: (NXS, NX) if j == 2 else None, 14)]
    o += [L(108, 44, 108, 188, LV, 2.5, '6 4'), T(108, 206, 'edge runs vertically', 13, fill=LV, bold=True), ar(24, 230, 92, 230, AC, 2.5), T(100, 235, 'gradient +x', 13, 'start', AC, True)]
    o += [T(210, 40, 'Gx mask', 13, 'start', AC, True), mat(210, 48, [['−1', 0, 1], ['−2', 0, 2], ['−1', 0, 1]], 30, size=13)]
    o += [TM(320, 74, 'Gx = (50 + 2×50 + 50)', 14, 'start'), TM(347, 96, '− (10 + 2×10 + 10)', 14, 'start'), T(320, 120, '= 200 − 40 = 160', 14, 'start', AC, True)]
    o += [T(210, 154, 'Gy mask', 13, 'start', AC, True), mat(210, 162, [['−1', '−2', '−1'], [0, 0, 0], [1, 2, 1]], 30, size=13)]
    o += [TM(320, 196, 'Gy = (10 + 20 + 50) − (10 + 20 + 50)', 14, 'start'), T(320, 220, '= 80 − 80 = 0', 14, 'start', AC, True)]
    o.append(T(320, 252, '|G| = √(160² + 0²) = 160,  θ = atan2(0, 160) = 0°', 14, 'start', INK, True))
    fx = lambda g: 60 + g * 620 / 200
    y = 300
    o += [R(fx(0), y - 12, fx(50) - fx(0), 24, PANEL, L2, 0, 1), R(fx(50), y - 12, fx(150) - fx(50), 24, LVS, L2, 0, 1), R(fx(150), y - 12, fx(200) - fx(150), 24, NXS, L2, 0, 1)]
    o += [T((fx(0) + fx(50)) / 2, y + 5, 'rejected', 13, fill=MUT), T((fx(50) + fx(150)) / 2, y + 5, 'weak', 13, fill=LV, bold=True), T((fx(150) + fx(200)) / 2 - 20, y + 5, 'strong', 13, fill=NX, bold=True)]
    for g in (0, 50, 150, 200):
        o.append(T(fx(g), y + 30, str(g) if g not in (50, 150) else ('T_low = 50' if g == 50 else 'T_high = 150'), 13, fill=MUT))
    o += [L(fx(160), y - 22, fx(160), y + 14, AC, 3), C(fx(160), y - 22, 6, AC), T(fx(160) + 10, y - 22, '|G| = 160: strong, kept', 13, 'end' if False else 'start', AC, True)]
    return 344, ''.join(o)


FIG[2] = (f2, 'On the patch 10 10 50, Sobel gives Gx = 200 − 40 = 160 and Gy = 0, so |G| = 160 and θ = 0°: the gradient points along +x and the edge is vertical. 160 ≥ 150, so the pixel is strong.',
          'The 3 by 3 patch with a bright right column, a dashed vertical edge and an arrow along +x. The Sobel masks with Gx = 160 and Gy = 0. A strip from 0 to 200 split at 50 and 150 into rejected, weak and strong, with |G| = 160 marked in the strong part.')


# ---- 4.3 Hough votes for two points ----
def f3():
    fx = lambda x: 50 + x * 46
    fy = lambda y: 210 - y * 46
    o = [L(fx(0), fy(0), fx(3.3), fy(0), L2, 1.5), L(fx(0), fy(0), fx(0), fy(3.3), L2, 1.5)]
    for v in range(4):
        o += [T(fx(v), fy(0) + 18, str(v), 13, fill=MUT), T(fx(0) - 8, fy(v) + 4, str(v), 13, 'end', MUT) if v else '']
    o += [T(fx(3.3) + 4, fy(0) + 4, 'x', 13, 'start', MUT), T(fx(0), fy(3.3) - 8, 'y', 13, fill=MUT)]
    o += [L(fx(0), fy(0), fx(3.2), fy(3.2), NX, 2, '6 4'), C(fx(1), fy(1), 6, AC), C(fx(2), fy(2), 6, LV)]
    o += [T(fx(1) + 10, fy(1) + 16, 'A (1,1)', 13, 'start', AC, True), T(fx(2) + 10, fy(2) + 16, 'B (2,2)', 13, 'start', LV, True), Tb(fx(2.6) - 10, fy(3) - 4, 'y = x', 13, 'end', NX, True)]
    x0, y0, cw, rh = 260, 40, 72, 36
    th = ['0°', '45°', '90°', '135°']
    cells = {(0, 3): 'A + B = 2', (1, 0): 'A', (1, 1): 'A', (1, 2): 'A', (2, 0): 'B', (2, 2): 'B', (3, 1): 'B'}
    o += [R(x0, y0, 64, rh, ACS, L2, 0, 1.2), T(x0 + 32, y0 + 24, 'ρ \\ θ', 13, bold=True)]
    for j, t in enumerate(th):
        o += [R(x0 + 64 + j * cw, y0, cw, rh, ACS, L2, 0, 1.2), T(x0 + 64 + j * cw + cw / 2, y0 + 24, t, 14, bold=True)]
    for r in range(4):
        y = y0 + rh * (r + 1)
        o += [R(x0, y, 64, rh, ACS, L2, 0, 1.2), T(x0 + 32, y + 24, str(r), 14, bold=True)]
        for j in range(4):
            v = cells.get((r, j), '')
            peak = (r, j) == (0, 3)
            c = NX if peak else AC if v == 'A' else LV if v == 'B' else INK
            o += [R(x0 + 64 + j * cw, y, cw, rh, NXS if peak else PANEL, NX if peak else L2, 0, 2 if peak else 1.2), T(x0 + 64 + j * cw + cw / 2, y + 24, v, 13, fill=c, bold=bool(v))]
    o.append(T(x0, 250, 'A: ρ = 1, 1.41 → 1, 1, 0.   B: ρ = 2, 2.83 → 3, 2, 0.', 13, 'start', MUT))
    o.append(T(x0, 276, 'Peak (ρ = 0, θ = 135°): −0.707x + 0.707y = 0, so y = x.', 14, 'start', NX, True))
    return 300, ''.join(o)


FIG[3] = (f3, 'A = (1,1) and B = (2,2) vote once in each θ column at their rounded ρ. Only the cell ρ = 0, θ = 135° gets both votes, and −0.707x + 0.707y = 0 is the line y = x.',
          'Left: points A (1,1) and B (2,2) on a dashed line y = x. Right: an accumulator with rows ρ = 0 to 3 and columns θ = 0°, 45°, 90°, 135°. A votes at ρ = 1, 1, 1, 0 and B at 2, 3, 2, 0, so the cell ρ = 0, θ = 135° holds 2.')


# ---- 4.4 Otsu on a four-level histogram ----
def f4():
    h = [4, 6, 6, 4]
    base, sc = 210, 22
    o = [T(40, 30, 'histogram, 20 pixels', 14, 'start', INK, True), L(30, base, 290, base, L2, 1.5)]
    for k, n in enumerate(h):
        x = 50 + k * 60
        f, st = (ACS, AC) if k <= 1 else (NXS, NX)
        o += [R(x, base - n * sc, 44, n * sc, f, st, 0, 1.6), T(x + 22, base - n * sc - 6, str(n), 13, fill=INK, bold=True), T(x + 22, base + 18, str(k), 13, fill=MUT)]
    o += [L(170 + 2, 62, 170 + 2, base + 4, LV, 2.5, '6 4'), T(172, 54, 'T = 1', 13, fill=LV, bold=True)]
    o += [T(97, base + 42, 'class 0: 10 px', 13, fill=AC, bold=True), T(247, base + 42, 'class 1: 10 px', 13, fill=NX, bold=True)]
    fx = lambda k: 450 + k * 100
    fy = lambda v: 210 - v * 150
    o.append(axes(400, 700, 60, 210, [0, 1, 2], [0, 0.25, 0.5, 0.75, 1], fx, fy, 'split k', 'σB²', yfmt=lambda v: f'{v:g}'))
    for k, v in enumerate([0.5625, 0.81, 0.5625]):
        c = LV if k == 1 else AC
        o += [L(fx(k), fy(0), fx(k), fy(v), c, 3), C(fx(k), fy(v), 6, c), Tb(fx(k), fy(v) - 12, f'{v:g}', 13, fill=c, bold=True)]
    o.append(T(20, 296, 'μT = 1.5. At k = 1: w₀ = w₁ = 0.5, μ₀ = 0.6, μ₁ = 2.4, so σB² = 0.25 × 1.8² = 0.81, the largest.', 13, 'start', INK, True))
    return 310, ''.join(o)


FIG[4] = (f4, 'For counts 4, 6, 6, 4 the between-class variance is 0.5625, 0.81 and 0.5625 at k = 0, 1, 2. It peaks at k = 1, so T = 1 puts levels 0 and 1 in one class and 2 and 3 in the other.',
          'Left: a histogram with bars 4, 6, 6, 4 at levels 0 to 3, split by a dashed line T = 1 into two classes of 10 pixels. Right: stems of σB² at k = 0, 1, 2 with heights 0.5625, 0.81 and 0.5625.')


# ---- 4.5 region growing from a seed ----
def f5():
    G = [[5, 5, 4, 4], [5, 6, 4, 9], [4, 4, 5, 9], [3, 3, 3, 9]]
    cs = 56
    def hot(i, j):
        v = G[i][j]
        if abs(v - 5) <= 1: return (ACS, AC)
        return (NXS, NX)
    o = [mat(40, 40, G, cs, hot, 17)]
    o.append(f'<circle cx="{40 + cs / 2}" cy="{40 + cs / 2}" r="20" style="fill:none;stroke:{LV};stroke-width:3"/>')
    o.append(T(40, 286, 'ring = seed (0,0) = 5', 13, 'start', LV, True))
    o += [boxt(330, 40, 370, 50, ['accept |f − 5| ≤ 1: levels 4, 5, 6'], ACS, AC, 14, True),
          boxt(330, 104, 370, 66, ['reject 3s: |3 − 5| = 2', 'reject 9s: |9 − 5| = 4'], NXS, NX, 14, True),
          boxt(330, 184, 370, 50, ['grow through 4-connected neighbours'], PANEL, L2, 14, True)]
    o.append(T(330, 270, 'Region = 10 pixels; the 3s and 9s stop it.', 15, 'start', AC, True))
    return 300, ''.join(o)


FIG[5] = (f5, 'From the seed 5 at (0,0), growing through 4-connected neighbours with |f − 5| ≤ 1 accepts every 4, 5 and 6 it can reach: 10 pixels. The 3s and the 9s fail the test and bound the region.',
          'A 4 by 4 grid 5 5 4 4 / 5 6 4 9 / 4 4 5 9 / 3 3 3 9 with the seed ringed. Ten cells of value 4, 5 or 6 are shaded as the region; the 3s along the bottom and the 9s down the right are marked as rejected.')


# ---- 4.6 flooding a 1-D profile ----
def f6():
    f = [9, 7, 3, 7, 9, 8, 3, 7, 9]
    x0, cw = 110, 62
    base, sc = 150, 10.5
    o = []
    for i, v in enumerate(f):
        x = x0 + i * cw
        o += [R(x + 4, base - v * sc, cw - 8, v * sc, PANEL, L2, 2, 1.5), T(x + cw / 2, base - v * sc - 6, str(v), 13, fill=INK, bold=True), T(x + cw / 2, base + 17, f'x={i + 1}', 13, fill=MUT)]
    o.append(T(20, base - 40, 'height', 13, 'start', MUT, True))
    o.append(T(20, base - 22, '= grey', 13, 'start', MUT, True))
    flood = {3: ({3}, {7}), 7: ({2, 3, 4}, {7, 8}), 8: ({2, 3, 4}, {6, 7, 8}), 9: ({1, 2, 3, 4}, {6, 7, 8, 9})}
    for r, (lv, (A, B)) in enumerate(flood.items()):
        y = 176 + r * 32
        o += [R(20, y, 90, 32, ACS if False else PANEL, L2, 0, 1.2), T(65, y + 21, f'level {lv}', 13, bold=True)]
        for i in range(9):
            x = x0 + i * cw
            n = i + 1
            if n in A: f_, st, s, c = ACS, AC, 'A', AC
            elif n in B: f_, st, s, c = NXS, NX, 'B', NX
            elif lv == 9 and n == 5: f_, st, s, c = LVS, LV, 'dam', LV
            else: f_, st, s, c = PANEL, L2, '', INK
            o += [R(x, y, cw, 32, f_, st, 0, 1.2), T(x + cw / 2, y + 21, s, 13, fill=c, bold=True)]
    o.append(T(20, 330, 'A fills from x = 3 and B from x = 7; at level 9 both reach x = 5, so x = 5 is the watershed line.', 13, 'start', INK, True))
    return 344, ''.join(o)


FIG[6] = (f6, 'The profile 9 7 3 7 9 8 3 7 9 has minima at x = 3 and x = 7. Basin A fills from x = 3 and basin B from x = 7; at level 9 both reach x = 5, which becomes the watershed line.',
          'Bars of heights 9, 7, 3, 7, 9, 8, 3, 7, 9 at x = 1 to 9. Below, rows for levels 3, 7, 8 and 9 mark which pixels are under water in basin A or basin B; at level 9 the cell x = 5 is the dam.')


# ---- 4.7 a square snake stretched ----
def f7():
    fx = lambda x: 70 + x * 72
    fy = lambda y: 250 - y * 72
    old = [(0, 0), (2, 0), (2, 2), (0, 2)]
    new = [(0, 0), (3, 0), (2, 2), (0, 2)]
    o = [P([(fx(x), fy(y)) for x, y in old + [old[0]]], MUT, 2, '6 4'), P([(fx(x), fy(y)) for x, y in new + [new[0]]], AC, 3)]
    o.append(ar(fx(2) + 8, fy(0), fx(3) - 10, fy(0), LV, 2.5))
    for k, (x, y) in enumerate(old):
        o.append(C(fx(x), fy(y), 6, MUT))
    for k, (x, y) in enumerate(new):
        o.append(C(fx(x), fy(y), 7, AC if k != 1 else LV))
    o += [T(fx(0) - 10, fy(0) + 22, 'v₁ (0,0)', 13, 'start', INK, True), T(fx(3), fy(0) + 22, 'v₂ → (3,0)', 13, fill=LV, bold=True),
          T(fx(2) - 30, fy(0) + 22, '(2,0)', 13, fill=MUT), T(fx(2) + 10, fy(2) - 10, 'v₃ (2,2)', 13, 'start', INK, True), T(fx(0) - 10, fy(2) - 10, 'v₄ (0,2)', 13, 'start', INK, True)]
    o += [Tb(fx(1.5), fy(0) - 12, '9', 14, fill=LV, bold=True), Tb(fx(2.5) + 14, fy(1), '5', 14, fill=LV, bold=True),
          Tb(fx(1), fy(2) + 22, '4', 14, fill=AC, bold=True), Tb(fx(0) + 14, fy(1), '4', 14, fill=AC, bold=True)]
    o += [boxt(360, 40, 340, 56, ['before: 4 + 4 + 4 + 4 = 16', 'each side 2, squared 4'], PANEL, L2, 14, True),
          boxt(360, 112, 340, 56, ['after: 9 + 5 + 4 + 4 = 22', 'sides 3 and √5 now'], LVS, LV, 14, True),
          boxt(360, 184, 340, 56, ['E_int rises by 6', 'accept only if E_ext falls more'], NXS, NX, 14, True)]
    o.append(T(20, 296, 'Numbers on the sides are squared lengths, with α = 1 and β = 0.', 13, 'start', MUT))
    return 310, ''.join(o)


FIG[7] = (f7, 'The square snake has four sides of squared length 4, so E_int = 16. Moving v₂ from (2,0) to (3,0) makes the changed sides 9 and 5, so E_int = 22 and the move needs the external energy to fall by more than 6.',
          'A dashed square with corners (0,0), (2,0), (2,2), (0,2) and a solid quadrilateral with v₂ moved to (3,0). Side labels give squared lengths 9, 5, 4, 4. Boxes: before 16, after 22, accept only if external energy falls by more than 6.')


# ---- 4.8 chain code of a 3x3 ring ----
def f8():
    cs, gx, gy = 56, 40, 50
    o = []
    for r in range(3):
        for c in range(3):
            on = (r, c) != (1, 1)
            o.append(R(gx + c * cs, gy + r * cs, cs, cs, ACS if on else PANEL, AC if on else L2, 0, 1.4, None if on else '4 3'))
    cen = lambda r, c: (gx + cs / 2 + c * cs, gy + cs / 2 + r * cs)
    path = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0)]
    codes = [0, 0, 6, 6, 4, 4, 2, 2]
    for k in range(8):
        (x1, y1), (x2, y2) = cen(*path[k]), cen(*path[k + 1])
        dx, dy = (x2 - x1) / cs, (y2 - y1) / cs
        o.append(ar(x1 + dx * 12, y1 + dy * 12, x2 - dx * 14, y2 - dy * 14, NX, 2.2))
        mx, my = (x1 + x2) / 2 + dy * 16, (y1 + y2) / 2 - dx * 16
        o.append(Tb(mx, my + 5, str(codes[k]), 14, fill=NX, bold=True))
    o.append(C(*cen(0, 0), 6, LV))
    o.append(T(gx, gy + 3 * cs + 22, 'start (0,0), clockwise', 13, 'start', LV, True))
    cx, cy, rr = 300, 140, 40
    o.append(T(cx, 62, 'directions', 13, fill=MUT, bold=True))
    for k in range(8):
        a = math.radians(45 * k)
        o += [L(cx, cy, cx + rr * math.cos(a), cy - rr * math.sin(a), L2, 1.5), T(cx + (rr + 14) * math.cos(a), cy - (rr + 14) * math.sin(a) + 5, str(k), 13, fill=INK, bold=True)]
    x0 = 470
    for i, (lab, vals, f, st) in enumerate((('chain code', [0, 0, 6, 6, 4, 4, 2, 2], NXS, NX), ('first difference', [6, 0, 6, 0, 6, 0, 6, 0], PANEL, L2), ('shape number', [0, 6, 0, 6, 0, 6, 0, 6], LVS, LV))):
        y = 56 + i * 64
        o += [T(x0, y - 8, lab, 13, 'start', st if st != L2 else INK, True), row(x0, y, vals, 30, 32, f, st, 14, True)]
    o.append(T(20, 296, 'Length L = 8 even steps × 1 + 0 odd steps × √2 = 8 pixels.', 13, 'start', INK, True))
    return 310, ''.join(o)


FIG[8] = (f8, 'Tracing the 3 × 3 ring clockwise from (0,0) gives the chain code 0 0 6 6 4 4 2 2. Its first difference is 6 0 6 0 6 0 6 0, and the smallest rotation, the shape number, is 0 6 0 6 0 6 0 6.',
          'A 3 by 3 ring of pixels with an empty centre and arrows around the boundary labelled 0, 0, 6, 6, 4, 4, 2, 2. A compass shows the eight Freeman directions 0 to 7. Three rows give the chain code, first difference and shape number.')


# ---- 4.9 components, holes and the Euler number ----
def f9():
    B = [[1, 1, 1, 0, 0], [1, 0, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0]]
    comp = {}
    for r in range(3):
        for c in range(3):
            if (r, c) != (1, 1): comp[(r, c)] = 1
    comp[(1, 4)] = comp[(2, 4)] = 2
    comp[(4, 0)] = comp[(4, 1)] = 3
    sty = {1: (ACS, AC), 2: (NXS, NX), 3: (LVS, LV)}
    cs, gx, gy = 44, 40, 40
    o = []
    for r in range(5):
        for c in range(5):
            k = comp.get((r, c))
            f, st = sty[k] if k else (PANEL, L2)
            o += [R(gx + c * cs, gy + r * cs, cs, cs, f, st, 0, 1.6 if k else 1), TM(gx + c * cs + cs / 2, gy + r * cs + cs * 0.64, str(B[r][c]), 15, bold=bool(k), fill=INK if k else MUT)]
    o.append(R(gx + cs + 3, gy + cs + 3, cs - 6, cs - 6, 'none', INK, 0, 2, '4 3'))
    o.append(T(gx, gy + 5 * cs + 24, 'dashed: the hole at (1,1)', 13, 'start', INK, True))
    o += [boxt(310, 40, 390, 40, ['1: the ring, rows 0–2, columns 0–2'], ACS, AC, 14, True),
          boxt(310, 90, 390, 40, ['2: the pair (1,4)–(2,4)'], NXS, NX, 14, True),
          boxt(310, 140, 390, 40, ['3: the pair (4,0)–(4,1)'], LVS, LV, 14, True)]
    o.append(T(310, 214, 'C = 3 pieces (8-connected 1s)', 14, 'start', INK, True))
    o.append(T(310, 238, 'H = 1 hole (0 cut off from the border)', 14, 'start', INK, True))
    o.append(T(310, 270, 'Euler number E = C − H = 3 − 1 = 2', 15, 'start', AC, True))
    return 310, ''.join(o)


FIG[9] = (f9, 'The ring, the pair (1,4)–(2,4) and the pair (4,0)–(4,1) are three 8-connected pieces, so C = 3. The 0 at (1,1) cannot reach the border, so H = 1 and E = 3 − 1 = 2.',
          'A 5 by 5 binary image with three coloured pieces: a ring of eight 1s around a 0 at (1,1), a vertical pair at (1,4) and (2,4), and a horizontal pair at (4,0) and (4,1). The hole is outlined. Text gives C = 3, H = 1 and E = 2.')

spec = make_spec(FIG)
