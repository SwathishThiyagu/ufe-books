"""Claude's hand-drawn figures for c-cv-u5 (Computer Vision, unit 5: features, cameras and motion), one per chapter,
from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARR = {AC: 'n', L2: 'm', LV: 'l', NX: 'x', MUT: 'm', INK: 'm'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=ARR[c])


def chain(items, y, x0=20, w=124, gap=18, h=56, size=13):
    o = []
    for i, (lines, f, st) in enumerate(items):
        x = x0 + i * (w + gap)
        o.append(boxt(x, y, w, h, lines, f, st, size, True))
        if i < len(items) - 1: o.append(ar(x + w, y + h / 2, x + w + gap - 2, y + h / 2, st if st != L2 else AC))
    return ''.join(o)


def mat(x, y, M, cell=48, hot=None, size=15, f0=PANEL):
    o = []
    for i, row in enumerate(M):
        for j, v in enumerate(row):
            h = hot(i, j) if hot else None
            f, st = h if h else (f0, L2)
            o += [R(x + j * cell, y + i * cell, cell, cell, f, st, 0, 1.6 if h else 1.2), TM(x + j * cell + cell / 2, y + i * cell + cell * 0.62, str(v), size, bold=bool(h))]
    return ''.join(o)


# ---- 5.1 the Harris response at a corner ----
def f1():
    o = [T(20, 40, 'Ix', 14, 'start', AC, True), mat(20, 48, [[2, 2], ['−2', '−2']], 40, size=14),
         T(120, 40, 'Iy', 14, 'start', AC, True), mat(120, 48, [[2, '−2'], [2, '−2']], 40, size=14)]
    o += [T(20, 158, 'Σ Ix² = 4 + 4 + 4 + 4 = 16', 13, 'start', INK, True),
          T(20, 180, 'Σ Iy² = 4 + 4 + 4 + 4 = 16', 13, 'start', INK, True),
          T(20, 202, 'Σ IxIy = 4 − 4 − 4 + 4 = 0', 13, 'start', INK, True)]
    o += [T(250, 40, 'H =', 15, 'start', INK, True), mat(290, 20, [[16, 0], [0, 16]], 36, lambda i, j: (ACS, AC) if i == j else None, 14)]
    o += [boxt(240, 104, 230, 56, ['λ₁ = λ₂ = 16', 'det = 256, trace = 32'], PANEL, L2, 14, True),
          boxt(240, 176, 230, 56, ['R = 256 − 0.04 × 32²', '= 256 − 40.96 = 215.04'], NXS, NX, 14, True),
          ar(355, 94, 355, 102, AC), ar(355, 162, 355, 174, AC)]
    fx = lambda l: 540 + l * 8
    fy = lambda l: 250 - l * 8
    o += [R(fx(0), fy(4), 32, 32, PANEL, L2, 0, 1), R(fx(4), fy(4), 128, 32, LVS, L2, 0, 1), R(fx(0), fy(20), 32, 128, LVS, L2, 0, 1),
          R(fx(4), fy(20), 128, 128, NXS, L2, 0, 1)]
    o += [L(fx(0), fy(0), fx(20) + 8, fy(0), INK, 1.5), L(fx(0), fy(0), fx(0), fy(20) - 8, INK, 1.5),
          T(fx(20) + 4, fy(0) + 20, 'λ₁', 14, 'end', MUT, True), T(fx(0) - 6, fy(20) - 4, 'λ₂', 14, 'end', MUT, True)]
    o += [T(fx(2), fy(2) + 5, 'flat', 13, fill=MUT), T(fx(12), fy(2) + 5, 'edge', 13, fill=LV, bold=True), T(fx(12), fy(18.5), 'corner', 13, fill=NX, bold=True)]
    o += [C(fx(16), fy(16), 7, NX), T(fx(16) - 10, fy(16) + 5, '(16, 16)', 13, 'end', INK, True)]
    o.append(T(20, 276, 'Both eigenvalues are large and R = 215.04 > 0, so the point is a corner (k = 0.04).', 14, 'start', NX, True))
    return 292, ''.join(o)


FIG[1] = (f1, 'The window sums give H = [[16, 0], [0, 16]], so both eigenvalues are 16, det H = 256 and trace H = 32. R = 256 − 0.04 × 32² = 215.04 is large and positive: a corner.',
          'The 2 by 2 gradients Ix = 2 2 / −2 −2 and Iy = 2 −2 / 2 −2 with their sums 16, 16 and 0; the matrix H with 16 on the diagonal; boxes for the eigenvalues, det 256, trace 32 and R = 215.04; and a λ₁–λ₂ plane split into flat, edge and corner with the point (16, 16) in the corner region.')


# ---- 5.2 normalising a SIFT cell ----
def f2():
    base = 220
    panels = [(30, 'counts d', [1, 3, 0, 2], 40, lambda v: f'{v}', AC, ACS),
              (270, 'divide by ‖d‖ = 3.7417', [0.2673, 0.8018, 0, 0.5345], 150, lambda v: f'{v:g}', LV, LVS),
              (500, 'clip at 0.2, renormalise', [0.5774, 0.5774, 0, 0.5774], 150, lambda v: f'{v:g}', NX, NXS)]
    o = []
    for x0, title, vals, sc, fmt, c, cs in panels:
        o += [T(x0, 40, title, 14, 'start', c, True), L(x0 - 6, base, x0 + 200, base, L2, 1.5)]
        for k, v in enumerate(vals):
            x = x0 + 8 + k * 50
            if v: o.append(R(x, base - v * sc, 30, v * sc, cs, c, 0, 1.6))
            o += [T(x + 15, base - v * sc - 6, fmt(v), 13, fill=INK, bold=True), T(x + 15, base + 18, f'bin {k + 1}', 13, fill=MUT)]
    o += [L(264, base - 0.2 * 150, 476, base - 0.2 * 150, NX, 1.8, '6 4'), T(258, base - 0.2 * 150 + 5, '0.2', 13, 'end', NX, True)]
    o += [ar(240, 140, 262, 140, AC), ar(470, 140, 492, 140, LV)]
    o.append(T(20, 274, '‖d‖₂ = √(1 + 9 + 0 + 4) = √14 = 3.7417;  3 ÷ 3.7417 = 0.8018.', 14, 'start', INK, True))
    o.append(T(20, 298, 'Clipping caps the one strong bin, so a single bright edge cannot dominate the 128 values.', 13, 'start', MUT))
    return 312, ''.join(o)


FIG[2] = (f2, 'The bins 1, 3, 0, 2 have L2 norm √14 = 3.7417, so they normalise to 0.2673, 0.8018, 0 and 0.5345. Clipping at 0.2 and renormalising brings the three non-zero bins to 0.5774.',
          'Three small bar charts of four bins: counts 1, 3, 0, 2; the normalised values 0.2673, 0.8018, 0, 0.5345 with a dashed clip line at 0.2; and the renormalised values 0.5774, 0.5774, 0, 0.5774.')


# ---- 5.3 HOG votes in one cell ----
def f3():
    cx, cy, sc = 150, 196, 34
    o = [P([(cx + 112 * math.cos(math.radians(a)), cy - 112 * math.sin(math.radians(a))) for a in range(0, 181, 5)], L2, 1.2, '4 4'),
         L(cx - 120, cy, cx + 120, cy, L2, 1.5)]
    o += [T(cx + 122, cy + 18, '0°', 13, fill=MUT), T(cx, cy - 118, '90°', 13, fill=MUT), T(cx - 122, cy + 18, '180°', 13, fill=MUT)]
    samples = [(10, 2, 1), (50, 1, 3), (110, 3, 6), (170, 2, 9)]
    cols = [AC, LV, NX, AC]
    for (a, m, b), c in zip(samples, cols):
        r = math.radians(a)
        ex, ey = cx + m * sc * math.cos(r), cy - m * sc * math.sin(r)
        o.append(ar(cx, cy, ex, ey, c, 2.6))
        lx, ly = cx + (m * sc + 26) * math.cos(r), cy - (m * sc + 26) * math.sin(r)
        o.append(Tb(lx, ly + 5, f'{a}°, {m}', 13, fill=c, bold=True))
    o.append(T(cx, cy + 40, 'bin = floor(θ ÷ 20) + 1', 13, fill=MUT, bold=True))
    raw = [2, 0, 1, 0, 0, 3, 0, 0, 2]
    nrm = ['0.471', '0', '0.236', '0', '0', '0.707', '0', '0', '0.471']
    x0, sp, base, s2 = 316, 44, 170, 34
    o += [T(x0, 40, 'votes per 20° bin', 14, 'start', INK, True), L(x0 - 4, base, x0 + 9 * sp, base, L2, 1.5)]
    for k, v in enumerate(raw):
        x = x0 + k * sp
        if v: o += [R(x + 6, base - v * s2, 32, v * s2, NXS if k == 5 else ACS, NX if k == 5 else AC, 0, 1.6), T(x + 22, base - v * s2 - 6, str(v), 13, fill=INK, bold=True)]
        o.append(T(x + 22, base + 18, str(k + 1), 13, fill=MUT))
        o += [R(x, 214, sp, 30, NXS if k == 5 else PANEL, NX if k == 5 else L2, 0, 1.2), TM(x + sp / 2, 234, nrm[k], 12 if len(nrm[k]) > 3 else 13, bold=nrm[k] != '0')]
    o.append(T(x0, 206, '÷ √18 = 4.243', 13, 'start', LV, True))
    o.append(T(20, 290, 'The 110° sample with magnitude 3 gives bin 6 the biggest vote, 0.707 after normalising.', 13, 'start', NX, True))
    return 304, ''.join(o)


FIG[3] = (f3, 'Four gradients at 10°, 50°, 110° and 170° with magnitudes 2, 1, 3 and 2 vote into 20° bins 1, 3, 6 and 9. Dividing by √18 = 4.243 gives 0.471, 0.236, 0.707 and 0.471.',
          'Left: four arrows on a half circle of orientations 0° to 180°, labelled 10°, 2; 50°, 1; 110°, 3; 170°, 2. Right: a 9-bin histogram with votes 2, 0, 1, 0, 0, 3, 0, 0, 2 and below it the normalised row 0.471, 0, 0.236, 0, 0, 0.707, 0, 0, 0.471.')


# ---- 5.4 a bag-of-visual-words histogram ----
def f4():
    words = [1, 1, 2, 3, 3, 3]
    st = {1: (ACS, AC), 2: (LVS, LV), 3: (NXS, NX)}
    o = [T(20, 40, 'six descriptors, each given its nearest word', 14, 'start', INK, True)]
    for i, w in enumerate(words):
        x = 20 + i * 62
        f, c = st[w]
        o += [R(x, 52, 54, 34, PANEL, L2, 6, 1.2), T(x + 27, 74, f'd{i + 1}', 13, fill=INK, bold=True), ar(x + 27, 88, x + 27, 108, c, 1.8),
              R(x, 110, 54, 34, f, c, 6, 1.6), T(x + 27, 132, f'word {w}', 13, fill=c, bold=True)]
    o.append(T(20, 178, 'counts n = 2, 1, 3;  N = 6', 14, 'start', INK, True))
    o.append(T(20, 202, 'histogram = 2/6, 1/6, 3/6', 14, 'start', INK, True))
    base, sc = 210, 260
    o += [T(430, 40, 'normalised histogram', 14, 'start', INK, True), L(420, base, 700, base, L2, 1.5)]
    for k, (h, lab) in enumerate(((0.333, 'word 1'), (0.167, 'word 2'), (0.5, 'word 3'))):
        f, c = st[k + 1]
        x = 440 + k * 86
        o += [R(x, base - h * sc, 56, h * sc, f, c, 0, 1.6), T(x + 28, base - h * sc - 6, f'{h:.3f}', 13, fill=c, bold=True), T(x + 28, base + 18, lab, 13, fill=MUT)]
    o.append(boxt(20, 236, 680, 64, ['word 2: tf = 1/6 = 0.167,  idf = log₁₀(1000 ÷ 400) = 0.398', 'tf-idf weight = 0.167 × 0.398 = 0.066'], LVS, LV, 14, False))
    return 314, ''.join(o)


FIG[4] = (f4, 'Six descriptors fall on words 1, 1, 2, 3, 3, 3, so the counts 2, 1, 3 over N = 6 give the histogram 0.333, 0.167, 0.500. Word 2 is in 400 of 1000 training images, so its tf-idf weight is 0.167 × 0.398 = 0.066.',
          'Six descriptor boxes d1 to d6 with arrows to words 1, 1, 2, 3, 3, 3; a bar chart of 0.333, 0.167 and 0.500 for words 1 to 3; and a box with tf 0.167, idf 0.398 and weight 0.066 for word 2.')


# ---- 5.5 projecting a point to a pixel ----
def f5():
    o = [chain([(['camera point', '(1.0, 0.5, 2.0) m'], PANEL, L2), (['divide by Z = 2.0', '(0.5, 0.25)'], ACS, AC),
                (['× f = 800 px', '(400, 200) px'], ACS, AC), (['+ (cx, cy)', '(720, 440) px'], NXS, NX)], 30, 20, 150, 26, 56, 13)]
    ox, oy, s = 120, 130, 0.36
    U = lambda u: ox + u * s
    V = lambda v: oy + v * s
    o += [ar(U(0), V(0), U(820), V(0), INK, 1.5), ar(U(0), V(0), U(0), V(500), INK, 1.5), T(U(820), V(0) - 8, 'u', 14, 'end', MUT, True), T(U(0) - 8, V(500), 'v', 14, 'end', MUT, True)]
    o.append(T(U(0) - 8, V(0) + 4, '0', 13, 'end', MUT))
    for u in (320, 720):
        o.append(T(U(u), V(0) - 8, str(u), 13, fill=MUT))
    for v in (240, 440):
        o.append(T(U(0) - 8, V(v) + 4, str(v), 13, 'end', MUT))
    o += [L(U(320), V(0), U(320), V(240), L2, 1, '3 3'), L(U(0), V(240), U(320), V(240), L2, 1, '3 3'),
          L(U(720), V(0), U(720), V(440), L2, 1, '3 3'), L(U(0), V(440), U(720), V(440), L2, 1, '3 3')]
    o += [ar(U(320), V(240), U(720) - 8, V(240), AC, 2.2), ar(U(720), V(240), U(720), V(440) - 8, AC, 2.2),
          Tb(U(520), V(240) - 10, '+400 px', 13, fill=AC, bold=True), Tb(U(720) + 10, V(340) + 4, '+200 px', 13, 'start', AC, True)]
    o += [C(U(320), V(240), 6, INK), Tb(U(320) - 10, V(240) + 20, 'principal point (320, 240)', 13, 'middle', INK, True),
          C(U(720), V(440), 7, NX), Tb(U(720) + 12, V(440) + 5, 'pixel (720, 440)', 13, 'start', NX, True)]
    return 330, ''.join(o)


FIG[5] = (f5, 'The point (1.0, 0.5, 2.0) m divided by Z = 2.0 gives (0.5, 0.25); times 800 px that is an offset of 400 px across and 200 px down from the principal point (320, 240), which lands at pixel (720, 440).',
          'A chain of four boxes: camera point (1.0, 0.5, 2.0) m, divide by Z to get (0.5, 0.25), multiply by 800 px to get (400, 200) px, add (320, 240) to get (720, 440) px. Below, pixel axes u and v with arrows of 400 px right and 200 px down from the principal point to the pixel.')


# ---- 5.6 depth from disparity ----
def f6():
    cl, cr, by = (110, 270), (230, 270), 270
    X = (190, 60)
    o = [L(cl[0], by, X[0], X[1], AC, 2), L(cr[0], by, X[0], X[1], AC, 2)]
    o += [L(60, 220, 280, 220, L2, 2), T(286, 224, 'image row', 13, 'start', MUT)]
    o += [C(cl[0], by, 7, INK), C(cr[0], by, 7, INK), C(X[0], X[1], 7, NX), T(X[0] + 12, X[1] - 6, 'point X', 13, 'start', NX, True)]
    o += [T(cl[0] - 10, by + 6, 'left', 13, 'end', INK, True), T(cr[0] + 10, by + 6, 'right', 13, 'start', INK, True)]
    o += [brace(cl[0], cr[0], by + 14, MUT), T((cl[0] + cr[0]) / 2, by + 34, 'B = 0.12 m', 13, fill=INK, bold=True)]
    o += [L(40, by, 40, X[1], LV, 1.5), L(34, by, 46, by, LV, 1.5), L(34, X[1], 46, X[1], LV, 1.5), Tb(40, (by + X[1]) / 2, 'Z', 14, fill=LV, bold=True)]
    o.append(T(150, by + 58, 'top view, not to scale', 13, fill=MUT))
    for x0, name, px in ((360, 'left image', 470), (550, 'right image', 434)):
        o += [R(x0, 60, 150, 110, PANEL, L2, 4, 1.5), T(x0 + 75, 50, name, 13, fill=INK, bold=True), L(x0, 115, x0 + 150, 115, LV, 1.5, '5 4')]
        o.append(C(x0 + (px - 360), 115, 7, NX))
    o += [f'<circle cx="660" cy="115" r="6" style="fill:none;stroke:{MUT};stroke-width:1.5;stroke-dasharray:3 2"/>']
    o += [brace(624, 660, 140, NX), T(642, 160, 'd = 24 px', 13, fill=NX, bold=True)]
    o.append(T(360, 196, 'same row in both images', 13, 'start', LV, True))
    o.append(T(360, 238, 'Z = f B ÷ d', 15, 'start', INK, True))
    o.append(T(360, 264, '= 800 px × 0.12 m ÷ 24 px', 14, 'start', INK))
    o.append(T(360, 290, '= 96 ÷ 24 = 4.0 m', 15, 'start', LV, True))
    return 340, ''.join(o)


FIG[6] = (f6, 'In a rectified pair the point sits on the same row of both images, shifted by the disparity d = 24 px. With f = 800 px and B = 0.12 m, Z = f B ÷ d = 96 ÷ 24 = 4.0 m.',
          'Left: a top view of two cameras 0.12 m apart with rays meeting at point X at depth Z. Right: the left and right images with the same dashed row; the point in the right image sits 24 px left of where it was in the left image. Text: Z = 800 × 0.12 ÷ 24 = 4.0 m.')


# ---- 5.7 triangulating from two cameras ----
def f7():
    fx = lambda z: 80 + z * 100
    fy = lambda x: 250 - x * 150
    o = [axes(80, 480, 60, 250, [0, 1, 2, 3, 4], [0, 0.5, 1], fx, fy, 'depth Z (m)', 'X (m)', yfmt=lambda v: f'{v:g}')]
    zc, xc = 1 / 0.3, 0.2 / 0.3
    o += [L(fx(0), fy(0), fx(4), fy(0.8), AC, 2.5), L(fx(0), fy(1), fx(4), fy(0.6), LV, 2.5)]
    o += [L(fx(zc), fy(0), fx(zc), fy(xc), NX, 1.4, '4 3'), L(fx(0), fy(xc), fx(zc), fy(xc), NX, 1.4, '4 3')]
    o += [C(fx(0), fy(0), 7, AC), C(fx(0), fy(1), 7, LV), C(fx(zc), fy(xc), 7, NX)]
    o += [Tb(fx(0) + 12, fy(0) - 14, 'camera 1 (0, 0, 0)', 13, 'start', AC, True), Tb(fx(0) + 12, fy(1) - 12, 'camera 2 (1, 0, 0)', 13, 'start', LV, True),
          Tb(fx(1.8), fy(0.36) + 18, 'u₁ = 0.2', 13, 'start', AC, True), Tb(fx(1.6), fy(0.84) - 12, 'u₂ = −0.1', 13, 'start', LV, True),
          Tb(fx(zc) + 10, fy(xc) - 12, '(3.333, 0.667)', 13, 'start', NX, True)]
    o.append(boxt(510, 60, 200, 150, ['u₁ − u₂ = 1 ÷ Z', '0.2 − (−0.1) = 0.3', 'Z = 1 ÷ 0.3 = 3.333 m', 'X = 0.2 × 3.333', '= 0.667 m'], PANEL, L2, 14, True))
    return 310, ''.join(o)


FIG[7] = (f7, 'Camera 1 at X = 0 sees the point along slope u₁ = 0.2 and camera 2, 1 m away, along u₂ = −0.1. The rays cross at Z = 1 ÷ 0.3 = 3.333 m and X = 0.667 m.',
          'X against depth Z with two rays: one from camera 1 at X = 0 rising with slope 0.2, one from camera 2 at X = 1 falling with slope −0.1. They cross at Z = 3.333 m, X = 0.667 m. A box gives the steps.')


# ---- 5.8 Lucas-Kanade from two constraint lines ----
def f8():
    cx, cy, s = 200, 160, 110
    U = lambda u: cx + u * s
    V = lambda v: cy - v * s
    o = [ar(U(-1.2), V(0), U(1.2), V(0), INK, 1.5), ar(U(0), V(-1.2), U(0), V(1.2), INK, 1.5), T(U(1.2), V(0) + 20, 'u', 14, 'end', MUT, True), T(U(0) + 10, V(1.2) + 6, 'v', 14, 'start', MUT, True)]
    for t in (-1, 1):
        o += [L(U(t), V(0) - 4, U(t), V(0) + 4, INK, 1.5), T(U(t), V(0) + 20, neg(t), 13, fill=MUT), L(U(0) - 4, V(t), U(0) + 4, V(t), INK, 1.5), T(U(0) - 8, V(t) + 4, neg(t), 13, 'end', MUT)]
    o += [L(U(-0.5), V(1.1), U(-0.5), V(-1.1), AC, 2.5), L(U(-1.1), V(-0.5), U(1.1), V(-0.5), LV, 2.5)]
    o += [Tb(U(-0.5), V(1.1) - 4, 'A: 2u + 1 = 0', 13, 'middle', AC, True), Tb(U(1.1), V(-0.5) - 10, 'B: 2v + 1 = 0', 13, 'end', LV, True)]
    o += [ar(U(0), V(0), U(-0.5) + 6, V(-0.5) - 6, NX, 3), C(U(-0.5), V(-0.5), 6, NX), Tb(U(-0.5) - 8, V(-0.5) + 24, '(−0.5, −0.5)', 13, 'end', NX, True)]
    o += [boxt(420, 40, 290, 56, ['pixel A (2, 0, 1)', '2u + 1 = 0, so u = −0.5'], ACS, AC, 14, True),
          boxt(420, 110, 290, 56, ['pixel B (0, 2, 1)', '2v + 1 = 0, so v = −0.5'], LVS, LV, 14, True),
          boxt(420, 180, 290, 56, ['flow (−0.5, −0.5)', 'length √0.5 = 0.707 px/frame'], NXS, NX, 14, True)]
    o.append(T(20, 306, 'Each pixel alone fixes one line in the (u, v) plane; two pixels with different gradients pin the point.', 13, 'start', INK, True))
    return 320, ''.join(o)


FIG[8] = (f8, 'Pixel A gives the line 2u + 1 = 0 and pixel B the line 2v + 1 = 0 in the (u, v) plane. They cross at (−0.5, −0.5), a flow of 0.707 pixels a frame.',
          'A u–v plane with the vertical line u = −0.5 from pixel A and the horizontal line v = −0.5 from pixel B, crossing at (−0.5, −0.5), with a flow arrow from the origin. Boxes give each equation and the length 0.707 pixels per frame.')


# ---- 5.9 an affine fit from three corners ----
def f9():
    ox, oy, s = 90, 260, 62
    X = lambda x: ox + x * s
    Y = lambda y: oy - y * s
    o = []
    for k in range(5):
        o.append(L(X(k), Y(0), X(k), Y(3.6), LN, 1))
    for k in range(4):
        o.append(L(X(0), Y(k), X(4.2), Y(k), LN, 1))
    m = [(0, 0), (1, 0), (0, 1)]
    f = [(1, 1), (3, 1), (1, 3)]
    o += [P([(X(a), Y(b)) for a, b in m + [m[0]]], AC, 2, '6 4', ACS, 0.6), P([(X(a), Y(b)) for a, b in f + [f[0]]], NX, 2.5, None, NXS, 0.6)]
    for i, ((a, b), (c, d)) in enumerate(zip(m, f)):
        o.append(ar(X(a), Y(b), X(c) - (6 if c > a else 0), Y(d) + 6, LV, 1.6, '4 3'))
    for i, (a, b) in enumerate(m):
        o += [C(X(a), Y(b), 6, AC)]
    for i, (a, b) in enumerate(f):
        o += [C(X(a), Y(b), 6, NX)]
    o += [T(X(0) - 8, Y(0) + 5, 'm1 (0,0)', 13, 'end', AC, True), T(X(1) + 8, Y(0) + 20, 'm2 (1,0)', 13, 'start', AC, True), T(X(0) - 8, Y(1) + 5, 'm3 (0,1)', 13, 'end', AC, True),
          Tb(X(1) - 10, Y(1) - 10, 'f1 (1,1)', 13, 'end', NX, True), Tb(X(3) + 10, Y(1) + 5, 'f2 (3,1)', 13, 'start', NX, True), Tb(X(1) + 10, Y(3) - 6, 'f3 (1,3)', 13, 'start', NX, True)]
    o += [T(380, 40, '(0,0) → (1,1): c = 1, f = 1', 13, 'start', INK, True), T(380, 64, '(1,0) → (3,1): a = 2, d = 0', 13, 'start', INK, True),
          T(380, 88, '(0,1) → (1,3): b = 0, e = 2', 13, 'start', INK, True)]
    o += [T(380, 140, 'T =', 15, 'start', INK, True), mat(420, 112, [[2, 0, 1], [0, 2, 1], [0, 0, 1]], 40, lambda i, j: (NXS, NX) if (i, j) in ((0, 0), (1, 1)) else (LVS, LV) if j == 2 and i < 2 else None, 14)]
    o.append(T(550, 150, 'scale 2', 13, 'start', NX, True))
    o.append(T(550, 172, 'shift (1, 1)', 13, 'start', LV, True))
    o.append(T(380, 262, 'x_f = 2x_m + 1,  y_f = 2y_m + 1', 14, 'start', INK, True))
    return 296, ''.join(o)


FIG[9] = (f9, 'The moving corners (0,0), (1,0), (0,1) map to the fixed corners (1,1), (3,1), (1,3). Solving the three pairs gives a scale of 2 and a shift of (1, 1): x_f = 2x_m + 1, y_f = 2y_m + 1.',
          'A grid with a small dashed triangle m1 m2 m3 at (0,0), (1,0), (0,1) and a larger solid triangle f1 f2 f3 at (1,1), (3,1), (1,3), with arrows from each moving corner to its fixed corner. The 3 by 3 matrix [[2, 0, 1], [0, 2, 1], [0, 0, 1]] is shown with the scale and shift entries marked.')

spec = make_spec(FIG)
