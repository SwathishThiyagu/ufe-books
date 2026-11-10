"""Claude's hand-drawn figures for c-cv-u2 (Computer Vision, unit 2: image enhancement and transforms), one per chapter,
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


def tab(x, y, widths, rows, rh=30, head=True, fills=None):
    """a plain table; rows are lists of strings, first row bold when head"""
    o = []
    for i, row in enumerate(rows):
        cx = x
        for j, (w, s) in enumerate(zip(widths, row)):
            f = fills(i, j) if fills else None
            o.append(R(cx, y + i * rh, w, rh, f or (ACS if head and i == 0 else PANEL), L2, 0, 1.2))
            o.append(T(cx + w / 2, y + i * rh + rh * 0.66, s, 13, bold=(head and i == 0) or j == 0))
            cx += w
    return ''.join(o)


def curve(f, a, b, fx, fy, c, w=2.5, dash=None, n=120):
    return P([(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


# ---- 2.1 negative, log and gamma curves ----
def f1():
    fx = lambda r: 70 + r * 330 / 255
    fy = lambda s: 280 - s * 240 / 255
    ticks = [0, 64, 128, 192, 255]
    o = [axes(70, 400, 40, 280, ticks, ticks, fx, fy, 'input r', 'output s')]
    lg = lambda r: 45.98 * math.log(1 + r)
    gm = lambda r: 255 * (r / 255) ** 0.4
    o += [curve(lambda r: r, 0, 255, fx, fy, MUT, 1.8, '6 4'), curve(lambda r: 255 - r, 0, 255, fx, fy, INK, 2.2),
          curve(lg, 0, 255, fx, fy, NX, 2.8), curve(gm, 0, 255, fx, fy, LV, 2.8)]
    o.append(L(fx(64), fy(0), fx(64), fy(192), L2, 1.2, '3 3'))
    o += [C(fx(64), fy(191), 5, INK), C(fx(64), fy(192), 5, NX), C(fx(64), fy(147), 5, LV), C(fx(64), fy(64), 5, MUT)]
    o += [Tb(fx(30) + 8, fy(232), 'negative', 13, 'start', INK, True),
          Tb(fx(14), fy(205), 'log', 13, 'start', NX, True),
          Tb(fx(150) + 6, fy(205.5) + 20, 'γ = 0.4', 13, 'start', LV, True),
          Tb(fx(205), fy(170), 's = r', 13, 'start', MUT, True)]
    rows = [['r', 'negative', 'log', 'γ = 0.4']] + [[str(r), str(255 - r), str(round(lg(r))), str(round(gm(r)))] for r in ticks]
    o.append(tab(440, 40, [50, 80, 60, 70], rows, 30, fills=lambda i, j: NXS if (i == 2 and j == 2) else LVS if (i == 2 and j == 3) else None))
    o.append(T(440, 252, 'At r = 64 the log curve gives 192', 13, 'start', INK, True))
    o.append(T(440, 272, 'and γ = 0.4 gives 147: dark pixels', 13, 'start', INK, True))
    o.append(T(440, 292, 'are lifted, the top stays near 255.', 13, 'start', INK, True))
    return 334, ''.join(o)


FIG[1] = (f1, 'On an 8-bit image the negative maps 64 to 191, the log curve s = 45.98 ln(1 + r) maps it to 192 and γ = 0.4 maps it to 147. Both curves lift the dark pixels and keep 255 at 255.',
          'A plot of output s against input r from 0 to 255 with four curves: the dashed identity s = r, the falling negative, the log curve and the γ = 0.4 curve, with dots at r = 64. A table gives the outputs for r = 0, 64, 128, 192 and 255.')


# ---- 2.2 histogram equalisation of a 3-bit image ----
def f2():
    n = [790, 1023, 850, 656, 329, 245, 122, 81]
    mp = [1, 3, 5, 6, 6, 7, 7, 7]
    out = [0] * 8
    for k, s in enumerate(mp): out[s] += n[k]
    base, sc = 210, 140 / 1023
    o = []
    for x0, cnt, title, hot in ((40, n, 'before: pixels at each level', lambda k: k >= 3), (400, out, 'after equalisation', lambda k: k >= 6)):
        o.append(T(x0, 36, title, 14, 'start', INK, True))
        o.append(L(x0 - 4, base, x0 + 8 * 36, base, L2, 1.5))
        for k in range(8):
            x = x0 + k * 36
            if cnt[k]:
                f, st = (LVS, LV) if hot(k) else (ACS, AC)
                o += [R(x, base - cnt[k] * sc, 28, cnt[k] * sc, f, st, 0, 1.5), T(x + 14, base - cnt[k] * sc - 6, str(cnt[k]), 13, fill=INK, bold=True)]
            o.append(T(x + 14, base + 18, str(k), 13, fill=MUT))
    o.append(T(40 + 4 * 36 - 4, base + 38, 'input level r', 13, fill=MUT))
    o.append(T(400 + 4 * 36 - 4, base + 38, 'output level s', 13, fill=MUT))
    cw, x0 = 48, 150
    o += [T(x0 - 10, 284, 'input r', 14, 'end', INK, True), T(x0 - 10, 314, 'output s', 14, 'end', INK, True)]
    for k in range(8):
        o += [R(x0 + k * cw, 266, cw, 28, ACS, L2, 0, 1.2), TM(x0 + k * cw + cw / 2, 285, str(k), 14, bold=True),
              R(x0 + k * cw, 296, cw, 28, LVS if k >= 3 else PANEL, LV if k >= 3 else L2, 0, 1.2), TM(x0 + k * cw + cw / 2, 315, str(mp[k]), 14, bold=k >= 3)]
    o.append(T(20, 350, 'Inputs 3 and 4 become 6, inputs 5, 6 and 7 become 7: five levels share the top two.', 13, 'start', LV, True))
    return 364, ''.join(o)


FIG[2] = (f2, 'For 4096 pixels at 3 bits, each level maps to round(7 × cumulative count ÷ 4096): 0→1, 1→3, 2→5, 3 and 4→6, 5, 6 and 7→7. The busy dark levels spread apart and five levels merge at the top.',
          'Two bar charts. Before: counts 790, 1023, 850, 656, 329, 245, 122, 81 at levels 0 to 7. After: 790 at 1, 1023 at 3, 850 at 5, 985 at 6 and 448 at 7. A two-row table gives the mapping 1, 3, 5, 6, 6, 7, 7, 7.')


# ---- 2.3 correlation against convolution ----
def f3():
    o = [T(20, 46, 'image f', 14, 'start', INK, True)]
    o.append(mat(20, 56, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 44, lambda i, j: (ACS, AC) if i < 2 and j < 2 else None))
    o += [T(20, 214, 'window 1 2 / 4 5', 13, 'start', AC, True), T(20, 238, 'dot on a mask = anchor', 13, 'start', MUT)]
    for y, M, anc, name, sums, res, at in ((40, [[1, 2], [3, 4]], (0, 0), 'mask w', '1×1 + 2×2 + 4×3 + 5×4', '= 37, written at (0,0)', (0, 0)),
                                         (170, [[4, 3], [2, 1]], (1, 1), 'w flipped 180°', '1×4 + 2×3 + 4×2 + 5×1', '= 23, written at (1,1)', (1, 1))):
        c = NX if at == (0, 0) else LV
        cs = NXS if at == (0, 0) else LVS
        o.append(T(200, y, name, 14, 'start', c, True))
        o.append(mat(200, y + 10, M, 40, lambda i, j: (cs, c) if (i, j) == anc else None))
        o.append(C(200 + anc[1] * 40 + (6 if anc == (0, 0) else 34), y + 10 + anc[0] * 40 + (6 if anc == (0, 0) else 34), 4, c))
        o.append(T(300, y + 30, 'correlation' if at == (0, 0) else 'convolution', 14, 'start', c, True))
        o.append(TM(300, y + 54, sums, 14, 'start'))
        o.append(T(300, y + 78, res, 14, 'start', c, True))
        o.append(T(560, y, 'output', 13, 'start', MUT, True))
        o.append(mat(560, y + 10, [[('37' if at == (0, 0) and (i, j) == (0, 0) else '23' if at == (1, 1) and (i, j) == (1, 1) else '') for j in range(3)] for i in range(3)], 36,
                     lambda i, j: (cs, c) if (i, j) == at else None, 15))
    o.append(T(20, 316, 'The mask is not symmetric, so flipping it changes the sum (37 against 23) and moves the anchor.', 13, 'start', INK, True))
    return 330, ''.join(o)


FIG[3] = (f3, 'On the window 1 2 / 4 5, correlation with w = 1 2 / 3 4 gives 37 at (0,0). Convolution uses the flipped mask 4 3 / 2 1, whose anchor is now bottom-right, and gives 23 at (1,1).',
          'A 3 by 3 image 1 to 9 with the top-left 2 by 2 window shaded. Top row: mask w with its anchor dot top-left, the sum 1×1 + 2×2 + 4×3 + 5×4 = 37, and an output grid with 37 at (0,0). Bottom row: the flipped mask 4 3 / 2 1 with anchor bottom-right, the sum 23, and 23 at (1,1).')


# ---- 2.4 box against Gaussian smoothing ----
def f4():
    o = [T(20, 46, 'noisy window', 14, 'start', INK, True)]
    o.append(mat(20, 56, [[10, 10, 10], [10, 80, 10], [10, 10, 10]], 44, lambda i, j: (NXS, NX) if (i, j) == (1, 1) else None))
    o.append(T(20, 214, '80 is a noise spike', 13, 'start', NX, True))
    o += [T(200, 40, 'box, ÷ 9', 14, 'start', AC, True), mat(200, 50, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], 30, size=14),
          T(200, 170, 'Gaussian, ÷ 16', 14, 'start', LV, True), mat(200, 180, [[1, 2, 1], [2, 4, 2], [1, 2, 1]], 30, lambda i, j: (LVS, LV) if (i, j) == (1, 1) else None, 14)]
    o += [boxt(310, 56, 210, 56, ['sum = 8 × 10 + 80 = 160', '160 ÷ 9 = 17.8'], ACS, AC, 14, False),
          boxt(310, 186, 210, 56, ['sum = 40 + 360 + 40 = 440', '440 ÷ 16 = 27.5'], LVS, LV, 14, False),
          ar(292, 84, 308, 84, AC), ar(292, 214, 308, 214, LV)]
    base, sc = 270, 2.0
    o.append(T(635, 40, 'centre value', 14, fill=INK, bold=True))
    o.append(L(552, base, 712, base, L2, 1.5))
    o.append(L(552, base - 10 * sc, 712, base - 10 * sc, MUT, 1.2, '4 3'))
    o.append(T(548, base - 10 * sc + 4, '10', 13, 'end', MUT))
    for x, v, lab, f, st in ((566, 80, 'input', NXS, NX), (626, 17.8, 'box', ACS, AC), (686 - 10, 27.5, 'Gauss', LVS, LV)):
        o += [R(x, base - v * sc, 34, v * sc, f, st, 0, 1.6), T(x + 17, base - v * sc - 6, f'{v:g}', 13, fill=st, bold=True), T(x + 17, base + 18, lab, 13, fill=MUT)]
    o.append(T(20, 316, 'The Gaussian gives the centre 4 of 16 parts, the box only 1 of 9.', 13, 'start', INK, True))
    return 330, ''.join(o)


FIG[4] = (f4, 'A spike of 80 among 10s: the 3 × 3 box average is 160 ÷ 9 = 17.8 and the Gaussian 1 2 1 / 2 4 2 / 1 2 1 gives 440 ÷ 16 = 27.5. Both pull the spike down; the box pulls harder.',
          'The noisy 3 by 3 window with 80 in the centre, the box mask of nine 1s divided by 9 giving 17.8, and the Gaussian mask divided by 16 giving 27.5. Bars compare the centre value: 80 in, 17.8 after the box, 27.5 after the Gaussian, over a background line at 10.')


# ---- 2.5 Laplacian sharpening, unsharp masking and high-boost ----
def f5():
    o = [T(20, 40, 'patch f', 14, 'start', INK, True)]
    o.append(mat(20, 50, [[10, 10, 10], [10, 20, 10], [10, 10, 10]], 36, lambda i, j: (ACS, AC) if (i, j) == (1, 1) else None, 14))
    for y, M, name, l1, l2 in ((40, [[0, 1, 0], [1, '−4', 1], [0, 1, 0]], '4-neighbour mask', '∇²f = 4×10 − 4×20 = −40', 'g = 20 − (−40) = 60'),
                               (160, [[1, 1, 1], [1, '−8', 1], [1, 1, 1]], '8-neighbour mask', '∇²f = 8×10 − 8×20 = −80', 'g = 20 − (−80) = 100')):
        o += [T(150, y, name, 13, 'start', LV, True), mat(150, y + 8, M, 28, lambda i, j: (LVS, LV) if (i, j) == (1, 1) else None, 13),
              T(246, y + 38, l1, 13, 'start', INK), T(246, y + 62, l2, 13, 'start', LV, True)]
    o.append(T(20, 286, 'Unsharp, k = 2: blur f̄ = 14, so g = 20 + 2 × (20 − 14) = 32.', 13, 'start', NX, True))
    o.append(T(20, 310, 'High-boost, A = 3: g = 3 × 20 − 14 = 46.', 13, 'start', AC, True))
    x0, sc = 556, 1.2
    o.append(T(630, 40, 'centre value after', 13, fill=INK, bold=True))
    o.append(L(x0 + 10 * sc, 52, x0 + 10 * sc, 262, MUT, 1.2, '4 3'))
    o.append(T(x0 + 10 * sc, 278, 'background 10', 13, fill=MUT))
    for i, (lab, v, f, st) in enumerate((('original', 20, PANEL, L2), ('unsharp k = 2', 32, NXS, NX), ('high-boost A = 3', 46, ACS, AC),
                                        ('4-nbr Laplacian', 60, LVS, LV), ('8-nbr Laplacian', 100, LVS, LV))):
        y = 58 + i * 40
        o += [T(x0 - 8, y + 18, lab, 13, 'end', INK, True), R(x0, y, v * sc, 26, f, st, 0, 1.6), T(x0 + v * sc + 6, y + 18, str(v), 13, 'start', st if st != L2 else INK, True)]
    return 326, ''.join(o)


FIG[5] = (f5, 'A bright centre 20 on a background of 10. Subtracting the 4-neighbour Laplacian (−40) lifts it to 60, the 8-neighbour one (−80) to 100; unsharp masking gives 32 and high-boost gives 46.',
          'The patch with 20 in the centre and 10 around it, the 4-neighbour and 8-neighbour Laplacian masks with their sums −40 and −80, and horizontal bars for the sharpened centre: 20 original, 32 unsharp, 46 high-boost, 60 and 100 for the two Laplacians.')


# ---- 2.6 a 4-point DFT ----
def f6():
    W = [['1', '1', '1', '1'], ['1', '−j', '−1', 'j'], ['1', '−1', '1', '−1'], ['1', 'j', '−1', '−j']]
    X = ['2', '1 − j', '0', '1 + j']
    x0, lw, cw, rh = 20, 90, 52, 34
    o = []
    hdr = [('n', 30), ('x(n)', 64)]
    for lab, y in hdr:
        o.append(R(x0, y, lw, rh, ACS, L2, 0, 1.2))
        o.append(T(x0 + lw / 2, y + 22, lab, 14, bold=True))
    for n in range(4):
        live = n < 2
        o += [R(x0 + lw + n * cw, 30, cw, rh, ACS, L2, 0, 1.2), TM(x0 + lw + n * cw + cw / 2, 52, str(n), 14, bold=True),
              R(x0 + lw + n * cw, 64, cw, rh, NXS if live else PANEL, NX if live else L2, 0, 1.4), TM(x0 + lw + n * cw + cw / 2, 86, '1' if live else '0', 14, bold=live)]
    xr = x0 + lw + 4 * cw
    o += [R(xr, 30, 90, rh, ACS, L2, 0, 1.2), T(xr + 45, 52, 'X(k)', 14, bold=True)]
    for k in range(4):
        y = 108 + k * rh
        o += [R(x0, y, lw, rh, PANEL, L2, 0, 1.2), T(x0 + lw / 2, y + 22, f'k = {k}', 14, bold=True)]
        for n in range(4):
            live = n < 2
            o += [R(x0 + lw + n * cw, y, cw, rh, PANEL, L2, 0, 1.2), TM(x0 + lw + n * cw + cw / 2, y + 22, W[k][n], 14, fill=INK if live else MUT, bold=live)]
        o += [R(xr, y, 90, rh, LVS if k != 2 else PANEL, LV if k != 2 else L2, 0, 1.4), TM(xr + 45, y + 22, X[k], 14, fill=LV if k != 2 else INK, bold=True)]
    o.append(T(x0, 266, 'Row k holds e^(−jπkn/2). Add the entries where x(n) = 1.', 13, 'start', MUT))
    base, sc = 236, 60
    o += [T(470, 40, 'magnitude |X(k)|', 14, 'start', INK, True), L(460, base, 712, base, L2, 1.5)]
    for k, m in enumerate([2, 1.414, 0, 1.414]):
        x = 490 + k * 64
        o += [L(x, base, x, base - m * sc, AC, 3), C(x, base - m * sc, 6, AC), T(x, base - m * sc - 12, f'{m:g}', 13, fill=AC, bold=True), T(x, base + 20, f'k = {k}', 13, fill=MUT)]
    o.append(T(20, 298, 'Bin 2 cancels: 1 + (−1) = 0. Bin 3 is the conjugate of bin 1, so its magnitude is also 1.414.', 13, 'start', INK, True))
    o.append(T(20, 322, 'For N = 1024: direct DFT 1024² = 1,048,576 multiplications; FFT 512 × 10 = 5,120.', 13, 'start', NX, True))
    return 336, ''.join(o)


FIG[6] = (f6, 'Only x(0) and x(1) are 1, so each X(k) is the sum of the first two entries in row k: X = 2, 1 − j, 0, 1 + j, with magnitudes 2, 1.414, 0 and 1.414.',
          'A table with x(n) = 1, 1, 0, 0 on top and rows of e^(−jπkn/2) for k = 0 to 3; the columns for n = 2 and 3 are greyed. The X(k) column reads 2, 1 − j, 0, 1 + j. A stem plot shows magnitudes 2, 1.414, 0, 1.414. A note compares 1,048,576 and 5,120 multiplications for N = 1024.')


# ---- 2.7 ideal, Butterworth and Gaussian low-pass ----
def f7():
    fx = lambda d: 70 + d * 400 / 150
    fy = lambda h: 260 - h * 210
    o = [axes(70, 470, 50, 260, [0, 50, 100, 150], [0, 0.25, 0.5, 0.75, 1], fx, fy, 'distance D from the centre (D₀ = 50)', 'H', yfmt=lambda v: f'{v:g}')]
    bw = lambda d: 1 / (1 + (d / 50) ** 4)
    ga = lambda d: math.exp(-d * d / 5000)
    o += [L(fx(50), fy(0), fx(50), fy(1), L2, 1.2, '3 3'), L(fx(100), fy(0), fx(100), fy(0.3), L2, 1.2, '3 3')]
    o += [P([(fx(0), fy(1)), (fx(50), fy(1)), (fx(50), fy(0)), (fx(150), fy(0))], NX, 2.8),
          curve(bw, 0, 150, fx, fy, AC, 2.6), curve(ga, 0, 150, fx, fy, LV, 2.6)]
    for d in (50, 100):
        o += [C(fx(d), fy(bw(d)), 5, AC), C(fx(d), fy(ga(d)), 5, LV)]
    o.append(C(fx(50), fy(1), 5, NX))
    for i, (lab, c) in enumerate((('ideal', NX), ('Butterworth, n = 2', AC), ('Gaussian', LV))):
        y = 80 + i * 24
        o += [L(fx(92), y - 5, fx(92) + 26, y - 5, c, 3), T(fx(92) + 34, y, lab, 13, 'start', c, True)]
    rows = [['filter', 'D = 50', 'D = 100'], ['ideal', '1', '0'], ['Butterworth', '0.5', '0.0588'], ['Gaussian', '0.607', '0.135']]
    o.append(tab(500, 50, [96, 56, 60], rows, 32))
    o.append(T(500, 218, 'Only the ideal mask jumps', 13, 'start', NX, True))
    o.append(T(500, 238, 'from 1 to 0, so only it rings.', 13, 'start', NX, True))
    return 316, ''.join(o)


FIG[7] = (f7, 'With D₀ = 50, at D = 50 the ideal mask passes 1, Butterworth order 2 passes 0.5 and Gaussian 0.607; at D = 100 they pass 0, 0.0588 and 0.135. Only the ideal mask has a step, so only it rings.',
          'H against distance D from 0 to 150 for three low-pass masks: the ideal step falling from 1 to 0 at D = 50, the Butterworth curve through 0.5 at 50, and the Gaussian through 0.607 at 50. Dots at D = 50 and 100, and a table of the six values.')


# ---- 2.8 two levels of the Haar transform ----
def f8():
    xs = [110 + i * 96 for i in range(4)]
    cw, ch = 80, 40
    rows = [(40, 'signal x', ['4', '6', '10', '12'], [PANEL] * 4, [L2] * 4),
            (130, 'level 1', ['7.07', '15.56', '−1.41', '−1.41'], [ACS, ACS, LVS, LVS], [AC, AC, LV, LV]),
            (220, 'level 2', ['16.0', '−6.0', '−1.41', '−1.41'], [NXS, NXS, LVS, LVS], [NX, NX, LV, LV])]
    o = []
    # arrows first so the boxes sit on top of them
    m01, m23 = (xs[0] + xs[1] + cw) / 2, (xs[2] + xs[3] + cw) / 2
    o += [ar(m01, 80, xs[0] + cw / 2, 128, AC, 1.8), ar(m01, 80, xs[2] + cw / 2 - 10, 128, LV, 1.8),
          ar(m23, 80, xs[1] + cw / 2, 128, AC, 1.8), ar(m23, 80, xs[3] + cw / 2, 128, LV, 1.8)]
    o += [ar(m01, 170, xs[0] + cw / 2, 218, NX, 1.8), ar(m01, 170, xs[1] + cw / 2, 218, NX, 1.8),
          ar(xs[2] + cw / 2, 170, xs[2] + cw / 2, 218, LV, 1.5, '4 3'), ar(xs[3] + cw / 2, 170, xs[3] + cw / 2, 218, LV, 1.5, '4 3')]
    for y, lab, vals, fs, sts in rows:
        o.append(T(20, y + 26, lab, 14, 'start', INK, True))
        for x, v, f, st in zip(xs, vals, fs, sts):
            o += [R(x, y, cw, ch, f, st, 6, 1.6), TM(x + cw / 2, y + 26, v, 15, bold=True)]
    o += [T(xs[0], 286, 'averages', 13, 'start', AC, True), T(xs[2], 286, 'details', 13, 'start', LV, True)]
    o.append(boxt(510, 40, 200, 100, ['energy in', '16 + 36 + 100 + 144', '= 296'], PANEL, L2, 14, True))
    o.append(boxt(510, 156, 200, 100, ['energy out', '256 + 36 + 2 + 2', '= 296'], NXS, NX, 14, True))
    o.append(T(20, 316, 'Average a = (p + q) ÷ √2 and detail d = (p − q) ÷ √2.', 13, 'start', INK, True))
    o.append(T(20, 340, 'Quantise the two small details to 0 and only 16.0 and −6.0 remain.', 13, 'start', MUT))
    return 354, ''.join(o)


FIG[8] = (f8, 'Haar on 4, 6, 10, 12: level 1 gives averages 7.07 and 15.56 and details −1.41 and −1.41; level 2 turns the averages into 16.0 and −6.0. The energy is 296 before and after.',
          'Three rows of boxes. Signal 4, 6, 10, 12. Level 1: averages 7.07 and 15.56, details −1.41 and −1.41. Level 2: 16.0 and −6.0 from the averages, with the details carried down. Two boxes show energy in and energy out, both 296.')

spec = make_spec(FIG)
