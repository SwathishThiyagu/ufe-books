"""Claude's hand-drawn figures for c-cv-u3 (Computer Vision, unit 3: restoration, reconstruction and compression), one per chapter,
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


def tab(x, y, widths, rows, rh=30, head=True, fills=None):
    o = []
    for i, row in enumerate(rows):
        cx = x
        for j, (w, s) in enumerate(zip(widths, row)):
            f = fills(i, j) if fills else None
            o.append(R(cx, y + i * rh, w, rh, f or (ACS if head and i == 0 else PANEL), L2, 0, 1.2))
            o.append(T(cx + w / 2, y + i * rh + rh * 0.66, s, 13, bold=(head and i == 0) or j == 0))
            cx += w
    return ''.join(o)


def curve(f, a, b, fx, fy, c, w=2.5, dash=None, n=160):
    return P([(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


# ---- 3.1 a 4-pixel motion blur in frequency ----
def f1():
    fx = lambda u: 70 + u * 400 / 256
    fy = lambda h: 240 - h * 190
    o = [axes(70, 470, 50, 240, [0, 64, 128, 192, 256], [0, 0.5, 1], fx, fy, 'frequency u (cycles per 256 pixels)', '|H(u)|', yfmt=lambda v: f'{v:g}')]
    H = lambda u: 1.0 if u % 256 == 0 else abs(math.sin(4 * math.pi * u / 256) / math.sin(math.pi * u / 256)) / 4
    o.append(curve(lambda u: H(u), 0.0001, 255.9, fx, fy, AC, 2.6, n=400))
    o.append(C(fx(0), fy(1), 6, AC))
    for u in (64, 128, 192):
        o.append(C(fx(u), fy(0), 6, NX))
    o.append(Tb(fx(0) + 12, fy(1) + 4, 'H(0) = 1', 13, 'start', AC, True))
    # the kernel
    o.append(T(510, 44, 'kernel h(x)', 14, 'start', INK, True))
    base = 150
    o.append(L(500, base, 700, base, L2, 1.5))
    for x in range(6):
        X = 520 + x * 34
        if x < 4:
            o += [R(X - 12, base - 60, 24, 60, ACS, AC, 0, 1.6), T(X, base - 68, '¼', 15, fill=AC, bold=True)]
        o.append(T(X, base + 18, str(x), 13, fill=MUT))
    o.append(T(510, base + 44, '¼ + ¼ + ¼ + ¼ = 1', 13, 'start', INK, True))
    o.append(T(510, base + 66, 'brightness is kept', 13, 'start', MUT))
    o.append(T(20, 304, 'At u = 64, 128 and 192 the four terms cancel, so G = 0 × F + N = N: only noise is left there,', 13, 'start', NX, True))
    o.append(T(20, 326, 'and the inverse filter G ÷ H divides by zero.', 13, 'start', NX, True))
    return 340, ''.join(o)


FIG[1] = (f1, 'A 4-pixel motion blur averages four positions with weight ¼. On a 256-pixel row it keeps the average brightness, H(0) = 1, but its response is exactly 0 at u = 64, 128 and 192.',
          'Left: |H(u)| against u from 0 to 256, starting at 1 and touching 0 at u = 64, 128 and 192, marked with dots. Right: the kernel as four bars of height ¼ at x = 0 to 3, summing to 1.')


# ---- 3.2 estimating noise from a flat patch ----
def f2():
    vals = [[8, 10, 12], [10, 12, 14], [12, 14, 16]]
    o = [T(20, 40, 'flat patch', 14, 'start', INK, True), mat(20, 50, vals, 40, lambda i, j: (ACS, AC) if vals[i][j] == 12 else None, 14)]
    fx = lambda z: 210 + (z - 4) * 18
    fy = lambda c: 200 - c * 40
    o += [L(fx(4), fy(0), fx(20), fy(0), L2, 1.5)]
    for z, c in ((8, 1), (10, 2), (12, 3), (14, 2), (16, 1)):
        o += [R(fx(z) - 16, fy(c), 32, fy(0) - fy(c), ACS if z != 12 else NXS, AC if z != 12 else NX, 0, 1.6), T(fx(z), fy(c) + 18, str(c), 13, fill=INK, bold=True)]
    for z in range(4, 21, 2):
        o.append(T(fx(z), fy(0) + 18, str(z), 13, fill=MUT))
    s = 2.31
    g = lambda z: 9 * 2 / (s * math.sqrt(2 * math.pi)) * math.exp(-(z - 12) ** 2 / (2 * s * s))
    o.append(curve(g, 4, 20, fx, fy, LV, 2.6))
    o += [L(fx(12), fy(3.4), fx(12), fy(0), NX, 1.4, '4 3'), brace(fx(12), fx(12 + s), 58, LV),
          T(fx(12 + s) + 8, 64, 'σ = 2.31', 13, 'start', LV, True)]
    o += [T(fx(12), 224 + 16, 'grey level z', 13, fill=MUT), T(fx(12), 32, 'mean 12', 13, fill=NX, bold=True)]
    o.append(boxt(520, 40, 190, 180, ['mean = 108 ÷ 9 = 12', 'deviations −4 … +4', 'squares sum to 48', 'variance = 48 ÷ 9', '= 5.33', 'σ = √5.33 = 2.31'], PANEL, L2, 14, True))
    o.append(T(20, 290, 'Symmetric about 12 with no spikes, so zero-mean Gaussian noise with σ ≈ 2.31 fits.', 13, 'start', LV, True))
    o.append(T(20, 312, 'A real estimate would use a patch of 20 × 20 pixels or more.', 13, 'start', MUT))
    return 326, ''.join(o)


FIG[2] = (f2, 'The nine readings of a flat patch, 8 to 16, have mean 12, variance 48 ÷ 9 = 5.33 and σ = 2.31. Their histogram is symmetric with no spikes, so a Gaussian with σ ≈ 2.31 fits.',
          'The 3 by 3 patch 8 10 12 / 10 12 14 / 12 14 16, a histogram with counts 1, 2, 3, 2, 1 at levels 8 to 16 and a Gaussian curve over it centred on 12 with σ marked, and a box with the steps mean 12, variance 5.33, σ 2.31.')


# ---- 3.3 mean, median and midpoint on an impulse ----
def f3():
    W = [[10, 12, 11], [9, 255, 10], [11, 10, 12]]
    o = [T(20, 40, 'window', 14, 'start', INK, True), mat(20, 50, W, 40, lambda i, j: (NXS, NX) if W[i][j] == 255 else None, 14)]
    srt = sorted(sum(W, []))
    o.append(T(170, 40, 'sorted', 14, 'start', INK, True))
    for k, v in enumerate(srt):
        x = 170 + k * 52
        f, st = (ACS, AC) if k == 4 else (NXS, NX) if v == 255 else (PANEL, L2)
        o += [R(x, 50, 52, 40, f, st, 0, 1.6 if st != L2 else 1.2), TM(x + 26, 76, str(v), 14, bold=st != L2), T(x + 26, 108, f'{k + 1}', 13, fill=MUT)]
    o.append(T(170 + 4 * 52 + 26, 130, '5th value = median', 13, fill=AC, bold=True))
    fx = lambda v: 40 + v * 640 / 255
    y = 230
    o += [xaxis(40, 680, y, [0, 64, 128, 192, 255], fx)]
    for v, lab, c, dy in ((11, 'median 11', AC, -40), (37.8, 'mean 37.8', LV, -16), (132, 'midpoint 132', LV, -16)):
        o += [L(fx(v), y, fx(v), y + dy + 6, c, 2), C(fx(v), y, 6, c), Tb(fx(v), y + dy, lab, 13, 'start' if v < 20 else 'middle', c, True)]
    o.append(T(fx(11) - 4, y + 44, 'true value ≈ 11', 13, 'start', MUT))
    o.append(T(20, 304, 'Mean = 340 ÷ 9 = 37.8 and midpoint = (9 + 255) ÷ 2 = 132 are dragged up; the median ignores the 255.', 13, 'start', INK, True))
    return 318, ''.join(o)


FIG[3] = (f3, 'Sorting the window puts the 255 impulse last, so the 5th value, the median, is 11. The mean (37.8) and the midpoint (132) are pulled up by the impulse.',
          'The 3 by 3 window with 255 in the centre, the nine values sorted 9, 10, 10, 10, 11, 11, 12, 12, 255 with the 5th highlighted, and a 0 to 255 number line marking median 11, mean 37.8 and midpoint 132.')


# ---- 3.4 a notch filter for stripes ----
def f4():
    o = [T(20, 40, 'stripes, T = 8 px', 14, 'start', INK, True), R(20, 50, 128, 128, PANEL, L2, 0, 1.5)]
    for k in range(8):
        o.append(R(20 + k * 16, 50, 8, 128, NXS, NX, 0, 0.8))
    o += [T(20, 200, 'N = 256 pixels', 13, 'start', MUT), T(20, 224, 'u₀ = 256 ÷ 8 = 32', 14, 'start', NX, True)]
    fx = lambda u: 230 + u * 460 / 256
    base1 = 140
    o += [T(230, 40, 'spectrum along v = 0', 14, 'start', INK, True), L(225, base1, 700, base1, L2, 1.5)]
    o += [L(fx(0), base1, fx(0), 60, MUT, 4), T(fx(0), base1 + 18, 'mean', 13, fill=MUT)]
    for u in (32, 224):
        o += [L(fx(u), base1, fx(u), 70, NX, 4), Tb(fx(u), 62, f'({u}, 0)', 13, fill=NX, bold=True)]
    o += [brace(fx(32), fx(224), base1 + 14, MUT), T(fx(128), base1 + 34, '224 − 32 = 192 bins apart', 13, fill=INK, bold=True)]
    base2, top2 = 270, 200
    o += [T(230, 192, 'notch mask H, D₀ = 2', 14, 'start', LV, True), L(225, base2, 700, base2, L2, 1.5)]
    H = lambda u: (1 - math.exp(-(u - 32) ** 2 / 8)) * (1 - math.exp(-(u - 224) ** 2 / 8))
    o.append(curve(H, 0, 255, fx, lambda h: base2 - h * (base2 - top2 - 6), LV, 2.6, n=512))
    for u in (0, 32, 128, 224, 255):
        o.append(T(fx(u), base2 + 18, str(u), 13, fill=MUT))
    o.append(T(fx(128), base2 + 40, 'u', 13, fill=MUT))
    o.append(T(20, 328, 'A notch at (32, 0) alone leaves H ≈ 1 at (224, 0), 192 bins away, so both spikes must be cut.', 13, 'start', INK, True))
    return 342, ''.join(o)


FIG[4] = (f4, 'Stripes with a period of 8 pixels on a 256-pixel image give spikes at (32, 0) and (224, 0), 192 bins apart. The notch mask is 0 at both and 1 everywhere else.',
          'Left: vertical stripes with period 8 pixels and u₀ = 256 ÷ 8 = 32. Right top: the spectrum along v = 0 with the mean at 0 and two spikes at 32 and 224, braced as 192 bins apart. Right bottom: a notch mask at 1 that dips to 0 at u = 32 and u = 224.')


# ---- 3.5 inverse against Wiener gain ----
def f5():
    fx = lambda h: 70 + h * 400 / 0.2
    fy = lambda g: 250 - g * 10
    o = [axes(70, 470, 50, 250, [0, 0.05, 0.1, 0.15, 0.2], [0, 5, 10, 15, 20], fx, fy, '|H|', 'gain', xfmt=lambda v: f'{v:g}')]
    K = 0.001
    o.append(curve(lambda h: 1 / h, 0.05, 0.2, fx, fy, NX, 2.6))
    o.append(curve(lambda h: h / (h * h + K), 0, 0.2, fx, fy, AC, 2.8, n=300))
    o += [ar(fx(0.05), fy(20), fx(0.05) - 4, fy(20) - 10, NX, 2), Tb(fx(0.06), 56, 'inverse 1/|H| → 100 at 0.01', 13, 'start', NX, True)]
    hp = math.sqrt(K)
    o += [L(fx(hp), fy(0), fx(hp), fy(15.811), L2, 1.2, '3 3'), C(fx(hp), fy(15.811), 6, AC), Tb(fx(hp) + 10, fy(15.811) - 10, 'peak 15.811 at √K = 0.0316', 13, 'start', AC, True)]
    o += [C(fx(0.01), fy(9.091), 5, AC), C(fx(0.1), fy(9.091), 5, AC), C(fx(0.1), fy(10), 5, NX), C(fx(0), fy(0), 5, AC)]
    o.append(Tb(fx(0.12), fy(4.2), 'Wiener', 13, 'start', AC, True))
    rows = [['|H|', 'inverse', 'Wiener'], ['1', '1.000', '0.999'], ['0.1', '10.000', '9.091'], ['0.01', '100.000', '9.091'], ['0', '∞', '0']]
    o.append(tab(500, 50, [56, 80, 70], rows, 32, fills=lambda i, j: (NXS if j == 1 else ACS) if i >= 3 and j > 0 else None))
    o.append(T(500, 238, 'K = 0.001: where |H| is', 13, 'start', INK, True))
    o.append(T(500, 258, 'tiny, Wiener stops dividing.', 13, 'start', INK, True))
    return 310, ''.join(o)


FIG[5] = (f5, 'With K = 0.001 the inverse gain 1/|H| climbs to 100 at |H| = 0.01, while the Wiener gain |H| ÷ (|H|² + K) peaks at 15.811 when |H| = 0.0316 and falls to 0 at |H| = 0.',
          'Gain against |H| from 0 to 0.2. The inverse curve 1/|H| rises off the top as |H| shrinks; the Wiener curve rises from 0 to a peak of 15.811 at 0.0316, then follows 1/|H|. A table gives both gains at |H| = 1, 0.1, 0.01 and 0.')


# ---- 3.6 projections and the blurred back-projection ----
def f6():
    s = 60

    def panel(x, y, M, title, c45, col):
        o = [T(x + s, 30, title, 14, fill=col, bold=True)]
        grid = mat(x, y, M, s, lambda i, j: (ACS, AC) if M[i][j] else None, 16)
        if c45:
            for k, v in enumerate(c45):
                # ray x + y = k, drawn from the bottom-left cell centre outwards to the top-right
                cx = [(x + s / 2 + s * a, y + s / 2 + s * (k - a)) for a in range(2) if 0 <= k - a <= 1]
                x0, y0 = min(cx)[0], max(p[1] for p in cx)
                ex, ey = x + s / 2 + s * min(k, 1) + 46, y + s / 2 + s * (k - min(k, 1)) - 46
                o.append(L(x0 - 12, y0 + 12, ex, ey, LV, 1.4, '4 3'))
                o.append(T(ex + 4, ey - 2, str(v), 14, 'start', LV, True))
            o.append(T(x + 2 * s + 34, y - 46, '45°', 13, 'start', LV))
            for j in range(2):
                o.append(T(x + s / 2 + j * s, y + 2 * s + 20, str(M[0][j] + M[1][j]), 14, fill=NX, bold=True))
                o.append(T(x - 10, y + s / 2 + j * s + 5, str(M[j][0] + M[j][1]), 14, 'end', AC, True))
            o += [T(x + s, y + 2 * s + 40, '0°: column sums', 13, fill=NX), T(x - 10, y - 8, '90°', 13, 'end', AC)]
        o.append(grid)
        return ''.join(o)

    o = [panel(60, 80, [[1, 0], [0, 1]], 'object f', [1, 0, 1], AC), panel(290, 80, [[0, 1], [1, 0]], 'object h', [0, 2, 0], MUT)]
    o.append(T(610, 30, 'back-projection b', 14, fill=LV, bold=True))
    o.append(mat(550, 80, [[3, 2], [2, 3]], s, lambda i, j: (LVS, LV), 16))
    o.append(T(610, 232, 'total 10, true total 2', 13, fill=LV, bold=True))
    o.append(T(20, 280, 'f and h give the same 0° and 90° sums; only 45° tells them apart (1, 0, 1 against 0, 2, 0).', 13, 'start', INK, True))
    o.append(T(20, 304, 'Back-projecting puts 2 in each empty cell. The ramp filter |ω| removes this blur.', 13, 'start', MUT))
    return 318, ''.join(o)


FIG[6] = (f6, 'Objects f and h have the same row and column sums, 1 and 1; only the 45° view separates them (1, 0, 1 against 0, 2, 0). Back-projecting f\'s three views gives 3 2 / 2 3, a total of 10 instead of 2.',
          'Three 2 by 2 grids. Object f with 1s on the main diagonal and object h with 1s on the other diagonal, each with column sums below, row sums to the left and 45° ray sums at the top right. The back-projection b reads 3 2 / 2 3, total 10.')


# ---- 3.7 the source encoder and its numbers ----
def f7():
    o = [chain([(['image', '1024 × 1024 × 8', '8,388,608 bits'], PANEL, L2), (['mapper', 'reversible'], ACS, AC), (['quantizer', 'lossy'], LVS, LV),
                (['symbol coder', 'reversible'], ACS, AC), (['bitstream', '256 KiB', '2,097,152 bits'], NXS, NX)], 30, 20, 120, 20, 76, 13)]
    o.append(T(20, 140, '2,097,152 ÷ (1024 × 1024) = 2 bits per pixel', 14, 'start', NX, True))
    o.append(boxt(20, 160, 300, 76, ['C = 8,388,608 ÷ 2,097,152 = 4', 'R = 1 − 1/4 = 0.75, so 75% redundant'], NXS, NX, 14, True))
    rows = [['p', 'log₂(1/p)', 'p × bits'], ['0.5', '1', '0.5'], ['0.25', '2', '0.5'], ['0.125', '3', '0.375'], ['0.125', '3', '0.375']]
    o.append(tab(380, 128, [70, 90, 90], rows, 26))
    o.append(T(380, 274, 'H = 0.5 + 0.5 + 0.375 + 0.375', 14, 'start', AC, True))
    o.append(T(380, 296, '= 1.75 bits per symbol, below 2', 14, 'start', AC, True))
    o.append(T(20, 274, 'Only the quantizer throws', 13, 'start', LV, True))
    o.append(T(20, 294, 'information away.', 13, 'start', LV, True))
    return 312, ''.join(o)


FIG[7] = (f7, 'A 1 MiB image at 8 bits per pixel leaves the encoder as 256 KiB at 2 bits per pixel, so C = 4 and R = 0.75. For probabilities 0.5, 0.25, 0.125, 0.125 the entropy limit is 1.75 bits per symbol.',
          'Five boxes in a row: the image of 8,388,608 bits, the mapper, the lossy quantizer, the symbol coder and a bitstream of 2,097,152 bits. Below: C = 4 and R = 0.75, and a table for the entropy 0.5 + 0.5 + 0.375 + 0.375 = 1.75 bits.')


# ---- 3.8 a Huffman tree and run-length pairs ----
def f8():
    N = {'root': (200, 46, '1.0'), 'n6': (290, 112, '0.6'), 'n4': (350, 178, '0.4'),
         'a': (110, 112, '0.4'), 'd': (230, 178, '0.2'), 'b': (300, 244, '0.2'), 'c': (400, 244, '0.2')}
    E = [('root', 'a', '0'), ('root', 'n6', '1'), ('n6', 'd', '0'), ('n6', 'n4', '1'), ('n4', 'b', '0'), ('n4', 'c', '1')]
    o = []
    for p, q, bit in E:
        (x1, y1, _), (x2, y2, _) = N[p], N[q]
        o.append(L(x1, y1, x2, y2, L2, 2))
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        o.append(Tb(mx + (-12 if bit == '0' else 12), my - 2, bit, 14, fill=AC, bold=True))
    for k, (x, y, p) in N.items():
        leaf = k in 'abcd' and len(k) == 1
        o.append(f'<circle cx="{x}" cy="{y}" r="22" style="fill:{NXS if leaf else PANEL};stroke:{NX if leaf else L2};stroke-width:2"/>')
        o.append(T(x, y + 5, p, 14, bold=True))
    codes = {'a': '0', 'd': '10', 'b': '110', 'c': '111'}
    for k, cd in codes.items():
        x, y, _ = N[k]
        o.append(T(x, y + 42, f'{k} = {cd}', 14, fill=NX, bold=True))
    o.append(T(20, 230, 'merge order:', 13, 'start', MUT))
    o.append(T(20, 250, 'b + c = 0.4', 13, 'start', MUT))
    o.append(T(20, 270, 'd + 0.4 = 0.6', 13, 'start', MUT))
    o.append(T(20, 290, 'a + 0.6 = 1.0', 13, 'start', MUT))
    rows = [['symbol', 'p', 'code', 'bits'], ['a', '0.4', '0', '1'], ['d', '0.2', '10', '2'], ['b', '0.2', '110', '3'], ['c', '0.2', '111', '3']]
    o.append(tab(460, 30, [64, 56, 70, 50], rows, 28))
    o.append(T(460, 190, 'L = 0.4 + 0.4 + 0.6 + 0.6 = 2.0', 13, 'start', INK, True))
    o.append(T(460, 212, 'H ≈ 1.92, gap 0.08 bit', 13, 'start', INK, True))
    o.append(T(460, 248, 'run-length', 13, 'start', MUT, True))
    bits = '0000111000'
    for i, b in enumerate(bits):
        o += [R(460 + i * 24, 256, 24, 28, NXS if b == '1' else PANEL, NX if b == '1' else L2, 0, 1.2), TM(472 + i * 24, 276, b, 14, bold=b == '1')]
    o.append(T(460, 308, '(0,4) (1,3) (0,3): 3 pairs', 14, 'start', AC, True))
    return 322, ''.join(o)


FIG[8] = (f8, 'b and c merge first into 0.4, that joins d to make 0.6, and a joins last. Reading 0 for left and 1 for right gives a = 0, d = 10, b = 110, c = 111, so L = 2.0 bits against H ≈ 1.92.',
          'A Huffman tree: root 1.0 splits into leaf a 0.4 and node 0.6; 0.6 splits into leaf d 0.2 and node 0.4; 0.4 splits into leaves b and c, 0.2 each. Left edges are 0, right edges 1. A table gives the codes, and the row 0000111000 is shown as the pairs (0,4) (1,3) (0,3).')


# ---- 3.9 quantising the DC coefficient ----
def f9():
    o = []
    for y, v, items, note in ((40, 4, [(['DCT', 'DC = 0.5 × 16 = 8', 'others 0'], PANEL, L2), (['quantise, step 4', '8 ÷ 4 = 2', 'send 2'], LVS, LV),
                                         (['decode', '2 × 4 = 8'], PANEL, L2), (['pixels', '8 ÷ 2 = 4', 'error 0'], NXS, NX)], 'flat 4s'),
                              (170, 8, [(['DCT', 'DC = 0.5 × 32 = 16', 'others 0'], PANEL, L2), (['quantise, step 6', '16 ÷ 6 = 2.667', 'send 3'], LVS, LV),
                                         (['decode', '3 × 6 = 18'], PANEL, L2), (['pixels', '18 ÷ 2 = 9', 'error +1'], LVS, LV)], 'flat 8s')):
        o += [T(20, y - 6, note, 13, 'start', MUT, True), mat(20, y + 6, [[v, v], [v, v]], 32, size=14)]
        o.append(ar(86, y + 38, 102, y + 38, AC))
        o.append(chain(items, y, 104, 136, 18, 76, 13))
    o.append(T(20, 290, 'Rounding 2.667 up to 3 is the only lossy step: every pixel of the flat 8 block comes back as 9.', 13, 'start', LV, True))
    return 304, ''.join(o)


FIG[9] = (f9, 'A flat block of 4s has DC 8; step 4 sends 2 and decodes exactly. A flat block of 8s has DC 16; step 6 sends round(2.667) = 3, decodes to DC 18 and pixels of 9, one grey level high.',
          'Two rows. Flat 4s: DCT gives DC 8, quantise with step 4 sends 2, decode 2 × 4 = 8, pixels 4, error 0. Flat 8s: DC 16, step 6 sends 3, decode 18, pixels 9, error +1.')

spec = make_spec(FIG)
