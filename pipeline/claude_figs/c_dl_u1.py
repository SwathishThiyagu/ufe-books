"""Claude's hand-drawn figures for c-dl-u1 (Deep Learning, unit 1: foundations, neurons and backpropagation), one per
chapter, from each chapter's worked example."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def circ(x, y, r, s, c=AC, fill=ACS, size=15, bold=True):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{fill};stroke:{c};stroke-width:2"/>' + T(x, y + size * 0.35, s, size, bold=bold)


def table(o, x0, y0, head, rows, widths, hot_col=None, rh=30, size=14):
    xs = [x0]
    for w in widths: xs.append(xs[-1] + w)
    for j, h in enumerate(head):
        o.append(T((xs[j] + xs[j + 1]) / 2, y0 - 8, h, 13, fill=MUT, bold=True))
    for i, r in enumerate(rows):
        y = y0 + i * rh
        for j, v in enumerate(r):
            h = j == hot_col
            o.append(R(xs[j], y, widths[j], rh, ACS if h else PANEL, AC if h else LN, 0, 1.1))
            o.append(T((xs[j] + xs[j + 1]) / 2, y + rh / 2 + 5, str(v), size, fill=AC if h else INK, bold=h))
    return xs


# ---- 1.1 AI, ML and DL ----
def f1():
    o = []
    o.append(f'<ellipse cx="300" cy="190" rx="280" ry="170" style="fill:var(--panel);stroke:var(--line2);stroke-width:2"/>')
    o.append(f'<ellipse cx="360" cy="210" rx="200" ry="130" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(f'<ellipse cx="430" cy="236" rx="110" ry="74" style="fill:var(--next-soft);stroke:var(--next);stroke-width:2"/>')
    o.append(T(60, 120, 'AI', 18, 'start', MUT, True)); o.append(T(60, 140, 'acts intelligently', 13, 'start', MUT))
    o.append(T(200, 120, 'ML', 18, 'start', AC, True)); o.append(T(200, 140, 'rules learned from data', 13, 'start', AC))
    o.append(T(380, 196, 'DL', 18, 'start', NX, True)); o.append(T(380, 214, 'many learned layers', 13, 'start', NX))
    def sysbox(x, y, w, lines, c):
        o.append(boxt(x, y, w, 20 + 18 * len(lines), lines, 'var(--fig)', c, 13, bold_first=True))
    sysbox(28, 180, 126, ['(a) chess program', 'rules written', 'by hand'], L2)
    sysbox(182, 150, 140, ['(b) house price', 'one straight line'], AC)
    sysbox(176, 246, 150, ['(d) 3 customer groups', 'no labels, shallow'], AC)
    sysbox(370, 232, 140, ['(c) face network', '8 learned layers'], NX)
    xr = 600
    o.append(T(xr, 60, 'Count', 14, 'start', bold=True))
    for i, (s, n, c) in enumerate((('AI only', 1, MUT), ('ML, not DL', 2, AC), ('DL', 1, NX))):
        o.append(T(xr, 88 + i * 24, s, 13, 'start', c, True)); o.append(T(712, 88 + i * 24, str(n), 14, 'end', c, True))
    o.append(L(xr, 156, 712, 156, LN, 1)); o.append(T(xr, 176, 'total', 13, 'start', bold=True)); o.append(T(712, 176, '4', 14, 'end', bold=True))
    return 372, ''.join(o)
FIG[1] = (f1, 'Deep learning sits inside machine learning, which sits inside AI. The hand-written chess program is AI only, the straight-line price fit and the 3 customer groups learn from data but are shallow, and the 8-layer face network is deep learning.',
          'Three nested ovals for AI, ML and DL with the four systems placed in them: chess in AI only, house price and customer groups in ML, the face network in DL, and a count of 1, 2 and 1.')


# ---- 1.2 one k-means round on six spends ----
def f2():
    x0, x1, y = 40, 690, 150
    fx = lambda v: x0 + (v - 200) / 1200 * (x1 - x0)
    o = [T(30, 30, 'With a yes/no label column: supervised classification. Without it: group the spends.', 13, 'start', MUT)]
    o.append(T(30, 60, 'One round of k-means from centres ₹400 and ₹1200', 15, 'start', bold=True))
    o.append(xaxis(x0, x1, y, [200, 400, 600, 800, 1000, 1200, 1400], fx, 'monthly spend (₹)'))
    for c, col in ((400, AC), (1200, NX)):
        o.append(L(fx(c), y - 60, fx(c), y, col, 1.6, '5 4'))
        o.append(T(fx(c), y - 66, f'start {c}', 13, fill=col))
    for v in (300, 350, 400):
        o.append(C(fx(v), y - 18, 8, AC))
    for v in (1200, 1250, 1300):
        o.append(C(fx(v), y - 18, 8, NX))
    for c, col, s in ((350, AC, '350'), (1250, NX, '1250')):
        X = fx(c)
        o.append(L(X, y + 58, X, y + 4, col, 1.5, '3 3'))
        o.append(f'<path d="M{X:.1f},{y + 60:.1f} l10,12 l-10,12 l-10,-12 z" style="fill:{col}"/>')
        o.append(T(X + 16 if c < 800 else X - 16, y + 77, f'new centre ₹{s}', 13, 'start' if c < 800 else 'end', col, True))
    o.append(boxt(40, 250, 300, 50, ['Group A: 300, 350, 400', '1050 ÷ 3 = 350'], ACS, AC, 13, bold_first=True))
    o.append(boxt(390, 250, 300, 50, ['Group B: 1200, 1250, 1300', '3750 ÷ 3 = 1250'], NXS, NX, 13, bold_first=True))
    return 316, ''.join(o)
FIG[2] = (f2, 'Each spend joins the nearer starting centre, giving {300, 350, 400} and {1200, 1250, 1300}. Averaging each group moves the centres to ₹350 and ₹1250.',
          'A number line of monthly spend with six points, dashed starting centres at 400 and 1200, the two groups coloured, and diamonds for the new centres 350 and 1250.')


# ---- 1.3 bias, variance and noise ----
def f3():
    data = [('degree 1', 0.40, 0.03, 0.05, 0.40, 'underfits: high bias'), ('degree 3', 0.08, 0.02, 0.05, 0.13, 'best balance'),
            ('degree 9', 0.00, 2.25, 0.05, 0.001, 'overfits: high variance')]
    x0, x1 = 130, 650
    fx = lambda v: x0 + v / 2.4 * (x1 - x0)
    o = [T(30, 26, 'Test MSE = bias² + variance + noise (σ² = 0.05)', 15, 'start', bold=True)]
    o.append(xaxis(x0, x1, 300, [0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4], fx, 'mean squared error', lambda v: f'{v:g}'))
    for i, (name, b, v, n, tr, why) in enumerate(data):
        y = 60 + i * 76
        o.append(T(x0 - 12, y + 22, name, 14, 'end', bold=True))
        x = x0
        for val, c, cs in ((b, AC, ACS), (v, LV, LVS), (n, MUT, PANEL)):
            if val > 0:
                o.append(R(x, y, fx(val) - x0, 32, cs, c, 0, 1.5)); x = fx(val) + (x - x0)
        tot = b + v + n
        o.append(T(fx(tot) + 8, y + 22, f'{tot:.2f}', 14, 'start', bold=True))
        o.append(T(x0, y + 50, f'bias² {b:.2f} · variance {v:.2f} · train MSE {tr:g} — {why}', 13, 'start', MUT if i != 1 else NX, i == 1))
    lx = 420
    for j, (s, c, cs) in enumerate((('bias²', AC, ACS), ('variance', LV, LVS), ('noise', MUT, PANEL))):
        o.append(R(lx + j * 100, 16, 16, 14, cs, c, 2, 1.5)); o.append(T(lx + j * 100 + 22, 28, s, 13, 'start', c))
    return 350, ''.join(o)
FIG[3] = (f3, 'Degree 1 loses almost all of its 0.48 to bias², degree 9 loses almost all of its 2.30 to variance, and degree 3 has the smallest test error, 0.15.',
          'Three stacked horizontal bars of test error for polynomial degrees 1, 3 and 9, split into bias squared, variance and noise, with totals 0.48, 0.15 and 2.30.')


# ---- 1.4 McCulloch-Pitts AND neuron ----
def f4():
    o = []
    o.append(circ(70, 80, 24, 'x₁', L2, PANEL)); o.append(circ(70, 200, 24, 'x₂', L2, PANEL))
    o.append(circ(260, 140, 38, 'Σ', AC, ACS, 22))
    o.append(L(94, 88, 222, 128, AC, 2.5, arrow='n')); o.append(L(94, 192, 222, 152, AC, 2.5, arrow='n'))
    o.append(Tb(160, 96, 'w₁ = 1', 13, fill=AC, bold=True)); o.append(Tb(160, 194, 'w₂ = 1', 13, fill=AC, bold=True))
    o.append(L(298, 140, 338, 140, AC, 2.5, arrow='n'))
    o.append(boxt(342, 112, 110, 56, ['sum ≥ θ = 2 ?'], LVS, LV, 14, bold_first=True))
    o.append(L(452, 140, 486, 140, AC, 2.5, arrow='n'))
    o.append(circ(510, 140, 22, 'y', NX, NXS))
    o.append(T(260, 200, 'adds the inputs', 13, fill=MUT)); o.append(T(397, 186, 'fires or not', 13, fill=MUT))
    rows = [('0', '0', '0', '0'), ('0', '1', '1', '0'), ('1', '0', '1', '0'), ('1', '1', '2', '1')]
    xs = table(o, 120, 260, ['x₁', 'x₂', 'sum', 'y'], rows, [70, 70, 90, 70], hot_col=3)
    o.append(R(xs[0], 260 + 3 * 30, xs[-1] - xs[0], 30, 'none', NX, 0, 2.5))
    o.append(T(440, 286, 'Only (1, 1) reaches 2, and 2 ≥ 2 fires.', 13, 'start', NX, True))
    o.append(T(440, 308, '(0, 1) sums to 1 and stays at 0.', 13, 'start'))
    o.append(T(440, 336, 'OR: same weights, θ = 1.', 13, 'start', MUT))
    o.append(T(440, 356, 'XOR: no weights and θ work.', 13, 'start', LV))
    return 392, ''.join(o)
FIG[4] = (f4, 'With both weights 1 and threshold 2, the neuron adds its inputs and fires only when the sum reaches 2, which happens just for (1, 1): that is AND.',
          'A McCulloch–Pitts neuron with inputs x₁ and x₂, weights 1 and 1, a sum and a threshold test of 2, above its truth table with sums 0, 1, 1, 2 and outputs 0, 0, 0, 1.')


# ---- 1.5 perceptron learns OR ----
def f5():
    x0, x1, y0, y1 = 70, 330, 50, 310
    fx = lambda v: x0 + (v + 0.5) / 2 * (x1 - x0)
    fy = lambda v: y1 - (v + 0.5) / 2 * (y1 - y0)
    o = [f'<polygon points="{fx(0.5):.1f},{fy(-0.5):.1f} {fx(1.5):.1f},{fy(-0.5):.1f} {fx(1.5):.1f},{fy(1.5):.1f} {fx(-0.5):.1f},{fy(1.5):.1f} {fx(-0.5):.1f},{fy(0.5):.1f}" style="fill:var(--next-soft)"/>']
    o.append(axes(x0, x1, y0, y1, [0, 1], [0, 1], fx, fy, 'x₁', 'x₂'))
    o.append(L(fx(-0.5), fy(0.5), fx(0.5), fy(-0.5), NX, 2.5, '7 5'))
    o.append(T(fx(1.1), fy(1.32), 'class 1', 14, fill=NX, bold=True))
    o.append(T(fx(-0.35), fy(-0.3), 'x₁ + x₂ = 0', 13, 'start', NX))
    for (a, b), c in (((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 1)):
        o.append(C(fx(a), fy(b), 9, NX if c else LV))
        o.append(T(fx(a) + 14, fy(b) - 10, f'({a},{b})→{c}', 13, 'start', NX if c else LV))
    o.append(T(420, 40, 'Weights after each pass', 14, 'start', bold=True))
    rows = [('1', '(0, 1)', '1', '1'), ('2', '(1, 1)', '1', '2'), ('3', '(1, 1)', '0', '1'), ('4', '(1, 1)', '0', '0')]
    table(o, 420, 80, ['epoch', 'w', 'b', 'mistakes'], rows, [60, 90, 50, 80])
    o.append(R(420, 80 + 3 * 30, 280, 30, 'none', NX, 0, 2.5))
    o.append(T(420, 224, 'Epoch 4 makes no mistake, so training', 13, 'start', NX, True))
    o.append(T(420, 242, 'stops at w = (1, 1), b = 0.', 13, 'start', NX, True))
    o.append(T(420, 272, 'Fire when x₁ + x₂ &gt; 0: only (0,0)', 13, 'start'))
    o.append(T(420, 290, 'gives 0, so it is class 0.', 13, 'start'))
    return 360, ''.join(o)
FIG[5] = (f5, 'Starting from zero weights, the perceptron fixes a mistake each time one appears; after 4 passes it makes none and stops at w = (1, 1), b = 0. The line x₁ + x₂ = 0 leaves (0, 0) in class 0 and the other three points in class 1.',
          'The four OR points on a square with the learned boundary x₁ + x₂ = 0 and the class 1 side shaded, beside a table of weights after each of the 4 epochs.')


# ---- 1.6 2-2-1 network for XOR ----
def f6():
    o = []
    X = {'x1': (60, 90), 'x2': (60, 230)}
    H = {'h1': (250, 90), 'h2': (250, 230)}
    Y = (440, 160)
    for k, (x, y) in X.items(): o.append(circ(x, y, 24, 'x₁' if k == 'x1' else 'x₂', L2, PANEL))
    for (hx, hy) in H.values():
        for (xx, xy) in X.values():
            o.append(L(xx + 24, xy + (hy - xy) * 0.12, hx - 30, hy - (hy - xy) * 0.12, AC, 1.8, arrow='n'))
    o.append(Tb(150, 72, '1', 13, fill=AC, bold=True)); o.append(Tb(150, 248, '1', 13, fill=AC, bold=True))
    o.append(Tb(120, 132, '1', 13, fill=AC, bold=True)); o.append(Tb(120, 194, '1', 13, fill=AC, bold=True))
    o.append(circ(250, 90, 28, 'h₁', AC, ACS)); o.append(circ(250, 230, 28, 'h₂', LV, LVS))
    o.append(T(250, 46, 'bias −0.5: OR', 13, fill=AC, bold=True)); o.append(T(250, 284, 'bias −1.5: AND', 13, fill=LV, bold=True))
    o.append(L(278, 100, 412, 152, AC, 2, arrow='n')); o.append(L(278, 220, 412, 170, LV, 2, arrow='l'))
    o.append(Tb(350, 116, '+1', 13, fill=AC, bold=True)); o.append(Tb(350, 206, '−1', 13, fill=LV, bold=True))
    o.append(circ(440, 160, 28, 'ŷ', NX, NXS)); o.append(T(440, 208, 'bias −0.5', 13, fill=NX, bold=True))
    o.append(T(440, 226, 'OR and not AND', 13, fill=NX))
    rows = [('0', '0', '0', '0', '0'), ('0', '1', '1', '0', '1'), ('1', '0', '1', '0', '1'), ('1', '1', '1', '1', '0')]
    table(o, 500, 80, ['x₁', 'x₂', 'h₁', 'h₂', 'ŷ'], rows, [40, 40, 40, 40, 44], hot_col=4, rh=34)
    o.append(T(602, 250, 'ŷ = 0, 1, 1, 0: XOR', 14, fill=NX, bold=True))
    o.append(T(360, 316, 'A unit fires when its net input is above 0. One line cannot split XOR; two hidden lines can.', 13))
    return 332, ''.join(o)
FIG[6] = (f6, 'h₁ fires for any input except (0, 0), so it is OR; h₂ fires only for (1, 1), so it is AND. The output fires for h₁ and not h₂, giving 0, 1, 1, 0: XOR.',
          'A 2-2-1 network: inputs x₁ and x₂ with weight 1 into hidden units h₁ (bias −0.5) and h₂ (bias −1.5), which feed the output with weights +1 and −1 and bias −0.5, beside its truth table.')


# ---- 1.7 four activation functions ----
def f7():
    funcs = [('sigmoid', lambda z: 1 / (1 + math.exp(-z)), (-0.2, 1.2), [0, 1], '0.881', '0.119'),
             ('tanh', math.tanh, (-1.2, 1.2), [-1, 0, 1], '0.964', '−0.964'),
             ('ReLU', lambda z: max(0, z), (-1, 4), [0, 2, 4], '2', '0'),
             ('leaky ReLU, α = 0.1', lambda z: z if z > 0 else 0.1 * z, (-1, 4), [0, 2, 4], '2', '−0.2')]
    o = []
    for k, (name, f, (lo, hi), yt, v2, vm2) in enumerate(funcs):
        px, py = 50 + (k % 2) * 350, 20 + (k // 2) * 190
        w, h = 290, 130
        fx = lambda z, px=px: px + (z + 4) / 8 * w
        fy = lambda v, py=py, lo=lo, hi=hi: py + 26 + (hi - v) / (hi - lo) * h
        o.append(T(px, py + 12, name, 14, 'start', bold=True))
        o.append(L(px, fy(0), px + w, fy(0), L2, 1.2)); o.append(L(fx(0), py + 26, fx(0), py + 26 + h, L2, 1.2))
        for v in yt:
            if v: o.append(T(fx(0) - 5, fy(v) + 4, neg(f'{v:g}'), 13, 'end', MUT)); o.append(L(fx(0) - 3, fy(v), fx(0) + 3, fy(v), L2, 1.2))
        o.append(T(fx(-4) + 2, py + h + 42, 'z = −4', 13, 'start', MUT)); o.append(T(fx(4) - 2, py + h + 42, '4', 13, 'end', MUT))
        o.append(P([(fx(z / 10), fy(f(z / 10))) for z in range(-40, 41)], AC, 2.5))
        o.append(C(fx(2), fy(f(2)), 5, LV)); o.append(C(fx(-2), fy(f(-2)), 5, NX))
        o.append(Tb(fx(2) + 8, fy(f(2)) + 18, f'z = 2: {v2}', 13, 'start', LV, True))
        o.append(Tb(fx(-2) - 6, fy(f(-2)) - 10, f'z = −2: {vm2}', 13, 'middle', NX, True))
    o.append(T(360, 404, 'Sigmoid and tanh flatten at both ends; ReLU is exactly 0 for negative z, while leaky ReLU keeps a small slope.', 13))
    return 418, ''.join(o)
FIG[7] = (f7, 'Each curve is drawn from z = −4 to 4 with its values at z = 2 and z = −2 marked. Sigmoid and tanh flatten at both ends, ReLU is 0 for negative z, and leaky ReLU keeps a slope of 0.1 there.',
          'Four small plots of sigmoid, tanh, ReLU and leaky ReLU from z equals −4 to 4, each with its values at z = 2 and z = −2 marked.')


# ---- 1.8 softmax and cross-entropy ----
def f8():
    z = [2, 1, 0]; p = [0.665, 0.245, 0.090]; g = [0.665, 0.245, -0.910]
    o = []
    cols = [(40, 'logits z'), (280, 'softmax p'), (520, 'gradient p − y')]
    for x, t in cols: o.append(T(x, 30, t, 14, 'start', bold=True))
    base = 230
    for i in range(3):
        hot = i == 2
        y = 52 + i * 0
        # logits bars (vertical)
        bx = 50 + i * 60
        o.append(R(bx, base - z[i] * 70, 44, z[i] * 70 if z[i] else 2, ACS, AC, 2, 1.5))
        o.append(T(bx + 22, base - z[i] * 70 - 8, str(z[i]), 14, bold=True))
        o.append(T(bx + 22, base + 22, f'class {i + 1}', 13, fill=LV if hot else MUT, bold=hot))
        px = 290 + i * 60
        o.append(R(px, base - p[i] * 200, 44, p[i] * 200, LVS if hot else NXS, LV if hot else NX, 2, 1.5))
        o.append(T(px + 22, base - p[i] * 200 - 8, f'{p[i]:.3f}', 13, bold=True, fill=LV if hot else INK))
        o.append(T(px + 22, base + 22, f'class {i + 1}', 13, fill=LV if hot else MUT, bold=hot))
        gx = 530 + i * 60
        hgt = g[i] * 100
        o.append(R(gx, base - 90 - max(hgt, 0), 44, abs(hgt), LVS if g[i] < 0 else ACS, LV if g[i] < 0 else AC, 2, 1.5))
        o.append(T(gx + 22, base - 90 - hgt + (18 if g[i] < 0 else -8), neg(f'{g[i]:.3f}'), 13, bold=True, fill=LV if g[i] < 0 else INK))
    o.append(L(520, base - 90, 712, base - 90, L2, 1.5))
    for x in (230, 470): o.append(L(x - 20, 140, x + 12, 140, AC, 2.5, arrow='n'))
    o.append(T(40, base + 54, 'e² + e¹ + e⁰ = 11.107', 13, 'start', MUT))
    o.append(T(280, base + 54, 'divide each by 11.107', 13, 'start', MUT))
    o.append(T(520, base + 54, 'true class 3: one-hot y = (0, 0, 1)', 13, 'start', MUT))
    o.append(T(360, base + 90, 'Loss if class 3 is true: −log 0.090 = 2.41.  If class 1 were true: −log 0.665 = 0.41.', 14, bold=True))
    return base + 106, ''.join(o)
FIG[8] = (f8, 'The logits (2, 1, 0) become probabilities (0.665, 0.245, 0.090). The true class 3 got only 0.090, so the loss is −log 0.090 = 2.41, and the gradient at the logits is simply p − y = (0.665, 0.245, −0.910).',
          'Three bar groups: logits 2, 1, 0; softmax probabilities 0.665, 0.245, 0.090 with class 3 marked as true; and the gradient p minus y with a negative bar for class 3.')


# ---- 1.9 forward and backward pass ----
def f9():
    nodes = [(60, 'x', '(1, 2)'), (210, 'z¹', '2.5'), (350, 'h', '2.5'), (490, 'ŷ', '4.0'), (640, 'L', '0.5')]
    y = 130
    o = [T(20, 30, 'forward: store each value', 14, 'start', AC, True)]
    for i, (x, n, v) in enumerate(nodes):
        o.append(circ(x, y, 32, n, AC if n != 'L' else LV, ACS if n != 'L' else LVS, 17))
        o.append(T(x, y - 44, f'= {v}', 14, fill=AC, bold=True))
    ops = ['W¹·x', 'ReLU', '2h − 1', '½(ŷ − 5)²']
    for i in range(4):
        xa, xb = nodes[i][0] + 34, nodes[i + 1][0] - 36
        o.append(L(xa, y, xb, y, AC, 2.5, arrow='n'))
        o.append(Tb((xa + xb) / 2, y - 10, ops[i], 13, fill=MUT))
    grads = ['(−2, −4)', '−2.0', '−2.0', '−1.0']
    yb = y + 90
    o.append(T(20, yb + 66, 'backward: multiply by each local slope', 14, 'start', LV, True))
    for i in range(4):
        xa, xb = nodes[i + 1][0] - 20, nodes[i][0] + 20
        o.append(arc(xa, y + 34, xb, y + 34, -0.25, LV, 2, 'l', '6 4'))
    labs = [('∂L/∂W¹ = −2 × (1, 2)', '= (−2, −4)'), ('∂L/∂z¹ = −2 × 1', 'ReLU slope 1'), ('∂L/∂h = −1 × 2', '= −2.0'), ('∂L/∂ŷ = 4 − 5', '= −1.0')]
    for i, (a, b) in enumerate(labs):
        x = (nodes[i][0] + nodes[i + 1][0]) / 2
        o.append(T(x, yb + 4, a, 13, fill=LV, bold=True)); o.append(T(x, yb + 22, b, 13, fill=LV))
    o.append(boxt(180, yb + 84, 360, 46, ['∂L/∂w² = −1 × h = −2.5, so w² → 2 + 0.25 = 2.25', 'b¹ → 0 + 0.2 = 0.2  (step size 0.1)'], PANEL, L2, 13))
    return yb + 140, ''.join(o)
FIG[9] = (f9, 'The forward pass runs left to right and keeps every value: z¹ = 2.5, h = 2.5, ŷ = 4.0, L = 0.5. The backward pass runs right to left, multiplying by each local slope, and reaches the first-layer weights as (−2, −4).',
          'A chain of nodes x, z¹, h, ŷ and L with forward values above and dashed backward arrows below carrying the gradients −1.0, −2.0, −2.0 and (−2, −4).')


spec = make_spec(FIG)
