"""Claude's hand-drawn figures for c-ml-u5 (Machine Learning, unit 5: neural networks and deep learning), one per
chapter, each drawn from that chapter's worked example with its own numbers. No chapter sentence describes the old
drawings, so text_fixes is empty. The university course-notes link is left out of the sources (drop_sources)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def node(x, y, s, r=22, f=PANEL, c=AC, size=14):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{f};stroke:{c};stroke-width:2"/>' + T(x, y + size * 0.35, s, size, bold=True)


def hollow(x, y, r, c):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2.5"/>'


def grid(x, y, vals, cell=30, hi=None, f=PANEL, c=L2, size=14, hif=None):
    """a matrix of numbers; hi = set of (r, c) cells to highlight"""
    o = []
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            h = hi and (i, j) in hi
            o.append(R(x + j * cell, y + i * cell, cell, cell, (hif or ACS) if h else f, AC if h else c, 2, 1.2))
            o.append(T(x + j * cell + cell / 2, y + i * cell + cell / 2 + size * 0.35, neg(v), size, bold=bool(h)))
    return ''.join(o)


# ---- 5.1 one McCulloch-Pitts unit, two thresholds ----
def f1():
    o = [T(40, 24, 'One McCulloch–Pitts unit: w₁ = w₂ = 1, b = 0', 15, 'start', bold=True)]
    o.append(node(70, 90, 'x₁')); o.append(node(70, 170, 'x₂'))
    o.append(L(94, 96, 196, 124, AC, 2, arrow='n')); o.append(L(94, 164, 196, 140, AC, 2, arrow='n'))
    o.append(T(140, 98, 'w₁ = 1', 13, fill=MUT)); o.append(T(140, 176, 'w₂ = 1', 13, fill=MUT))
    o.append(node(226, 130, 'z', 28)); o.append(T(226, 182, 'z = x₁ + x₂', 13))
    o.append(L(256, 130, 296, 130, AC, 2, arrow='n'))
    o.append(boxt(300, 108, 90, 44, ['z ≥ θ ?'], ACS, AC, 14))
    o.append(L(392, 130, 420, 130, AC, 2, arrow='n')); o.append(T(436, 135, 'y', 15, 'start', bold=True))
    X, Y = 470, 52
    heads = ['x₁ x₂', 'z', 'θ = 2', 'θ = 1']
    cw = [64, 40, 60, 60]
    cx = [X]
    for w in cw[:-1]: cx.append(cx[-1] + w)
    for x, w, h in zip(cx, cw, heads):
        o.append(T(x + w / 2, Y, h, 13, bold=True, fill=MUT if h in ('x₁ x₂', 'z') else AC))
    rows = [('0 0', 0, 0, 0), ('0 1', 1, 0, 1), ('1 0', 1, 0, 1), ('1 1', 2, 1, 1)]
    for i, (xs, z, a, b) in enumerate(rows):
        y = Y + 14 + i * 32
        o.append(R(X, y, sum(cw), 30, PANEL if i % 2 == 0 else 'none', 'none', 0, 0))
        for x, w, v, bold in zip(cx, cw, [xs, z, a, b], [False, False, a == 1, b == 1]):
            o.append(T(x + w / 2, y + 20, str(v), 14, bold=bold, fill=AC if bold else INK))
    y = Y + 14 + 4 * 32 + 22
    o.append(T(cx[2] + 30, y, 'AND', 14, bold=True, fill=AC)); o.append(T(cx[3] + 30, y, 'OR', 14, bold=True, fill=AC))
    o.append(T(40, 262, 'Same weights, different threshold: θ = 2 needs both inputs on (AND), θ = 1 needs one (OR).', 14, 'start'))
    o.append(T(40, 286, 'NOT x₁: w₁ = −1, w₂ = 0, θ = 0 gives z = −x₁, so y = 1 at x₁ = 0 and y = 0 at x₁ = 1.', 14, 'start', NX, True))
    return 302, ''.join(o)
FIG[1] = (f1, 'The unit adds its inputs, z = x₁ + x₂, and fires when z reaches the threshold. With θ = 2 only (1, 1) fires, giving AND; with θ = 1 any input pair with a 1 fires, giving OR.',
          'A unit with inputs x1 and x2, weights 1, summing to z and testing z ≥ θ. A truth table lists z = 0, 1, 1, 2 for inputs 00, 01, 10, 11, with outputs 0, 0, 0, 1 at θ = 2 (AND) and 0, 1, 1, 1 at θ = 1 (OR). A note gives NOT x1.')


# ---- 5.2 the perceptron's final AND boundary ----
def f2():
    o = [T(40, 24, 'Perceptron trained on AND settles at w = (1, 2), b = −2', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 70, 340, 60, 320
    fx = lambda v: x0 + (v + 0.5) / 2.8 * (x1 - x0)
    fy = lambda v: y1 - (v + 0.5) / 2.0 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2], [0, 1], fx, fy, 'x₁', 'x₂'))
    o.append(f'<polygon points="{fx(-0.5):.1f},{fy(1.25):.1f} {fx(2.3):.1f},{fy(-0.15):.1f} {fx(2.3):.1f},{fy(1.5):.1f} {fx(-0.5):.1f},{fy(1.5):.1f}" style="fill:var(--accent-soft)"/>')
    o.append(L(fx(-0.5), fy(1.25), fx(2.3), fy(-0.15), LV, 3))
    o.append(Tb(fx(1.75), fy(0.35) - 10, 'x₁ + 2x₂ = 2', 13, 'start', LV, True))
    pts = [((0, 0), 0, '−2'), ((1, 0), 0, '−1'), ((0, 1), 0, '0'), ((1, 1), 1, '+1')]
    for (x, y), t, net in pts:
        c = AC if t else NX
        o.append(C(fx(x), fy(y), 9, c) if t else hollow(fx(x), fy(y), 8, c))
        o.append(Tb(fx(x) + 14, fy(y) + 20, f'net {net}', 13, 'start', c, bool(t)))
    o.append(T(fx(1.6), fy(1.3), 'net > 0: fires', 13, fill=AC, bold=True))
    X = 380
    o.append(T(X, 70, 'first two updates (η = 1)', 13, 'start', MUT))
    o.append(T(X, 94, '(1,1), t = 1: net 0, y = 0, e = +1', 13, 'start'))
    o.append(T(X, 114, '→ w = (1, 1), b = 1', 13, 'start', AC, True))
    o.append(T(X, 140, '(1,0), t = 0: net 2, y = 1, e = −1', 13, 'start'))
    o.append(T(X, 160, '→ w = (0, 1), b = 0', 13, 'start', AC, True))
    o.append(T(X, 196, 'later passes keep fixing errors until', 13, 'start', MUT))
    o.append(T(X, 214, 'a full pass changes nothing:', 13, 'start', MUT))
    o.append(T(X, 240, 'w = (1, 2), b = −2', 15, 'start', LV, True))
    o.append(T(X, 272, '(0, 1) sits on the line: net = 0', 13, 'start'))
    o.append(T(X, 290, 'is not > 0, so it outputs 0.', 13, 'start'))
    return 376, ''.join(o)
FIG[2] = (f2, 'After training, the line x₁ + 2x₂ = 2 leaves only (1, 1) on the firing side, with net +1; the other three AND inputs give net −2, −1 and 0, and 0 is not above 0, so all three output 0.',
          'The four AND inputs on a grid with the boundary x1 + 2x2 = 2. The shaded side above the line holds only (1,1), net +1. Points (0,0), (1,0), (0,1) have net −2, −1, 0. Side notes list the first two updates and the final weights w = (1, 2), b = −2.')


# ---- 5.3 the hidden layer makes XOR separable ----
def f3():
    o = [T(40, 24, 'XOR: the hidden layer moves the points so one line works', 15, 'start', bold=True)]

    def plane(x0, title, pts, labx, laby, line=None):
        s = 200
        fx = lambda v: x0 + 30 + v * (s - 60)
        fy = lambda v: 260 - 30 - v * (s - 60)
        p = [T(x0 + s / 2, 54, title, 14, bold=True)]
        p.append(R(x0, 60, s, s, 'none', L2, 6, 1.4))
        if line: p.append(L(fx(line[0][0]), fy(line[0][1]), fx(line[1][0]), fy(line[1][1]), LV, 2.5, dash='6 4'))
        for (x, y), out, lab in pts:
            c = AC if out else NX
            p.append(C(fx(x), fy(y), 10, c) if out else hollow(fx(x), fy(y), 9, c))
            p.append(Tb(fx(x), fy(y) + (28 if y < 0.5 else -16), lab, 13, fill=c, bold=bool(out)))
        p.append(T(x0 + s / 2, 282, labx, 13, fill=MUT)); p.append(T(x0 - 8, 160, laby, 13, 'end', MUT))
        return ''.join(p)
    o.append(plane(60, 'inputs (x₁, x₂)', [((0, 0), 0, '(0,0)'), ((0, 1), 1, '(0,1)'), ((1, 0), 1, '(1,0)'), ((1, 1), 0, '(1,1)')], 'x₁', 'x₂'))
    o.append(L(280, 160, 380, 160, AC, 2.5, arrow='n'))
    o.append(T(330, 140, 'h₁ = step(x₁ + x₂ − 0.5)', 13, fill=INK)); o.append(T(330, 186, 'h₂ = step(x₁ + x₂ − 1.5)', 13, fill=INK))
    o.append(plane(430, 'hidden (h₁, h₂)', [((0, 0), 0, 'from (0,0)'), ((1, 0), 1, 'from (0,1), (1,0)'), ((1, 1), 0, 'from (1,1)')], 'h₁', 'h₂',
                   line=((0.55, -0.1), (1.15, 0.5))))
    o.append(T(530, 306, 'y = step(h₁ − h₂ − 0.5): one cut', 13, fill=LV, bold=True))
    o.append(T(40, 336, 'No single line splits the left plane; on the right the two 1s land on one point, (1, 0).', 14, 'start'))
    o.append(T(40, 358, 'A 2–3–1 network has (2×3 + 3) + (3×1 + 1) = 9 + 4 = 13 parameters.', 13, 'start', MUT))
    return 374, ''.join(o)
FIG[3] = (f3, 'In the input plane no straight line separates XOR’s 1s from its 0s. The hidden units send (0, 1) and (1, 0) to the same point (1, 0), and there one line h₁ − h₂ = 0.5 cuts the 1s off.',
          'Left: the four XOR inputs, with (0,1) and (1,0) as filled output-1 points at opposite corners. An arrow with the two hidden-unit formulas leads right: in hidden space (0,0) stays, (0,1) and (1,0) both land on (1,0), and (1,1) goes to (1,1). A dashed line separates (1,0) from the others.')


# ---- 5.4 softmax and cross-entropy ----
def f4():
    o = [T(40, 24, 'Softmax turns logits (2, 1, 0) into probabilities', 15, 'start', bold=True)]
    cols = [('class 1', 2, 7.389, 0.665), ('class 2', 1, 2.718, 0.245), ('class 3', 0, 1.0, 0.090)]
    xs = [200, 360, 520]
    rows = [('logit z', 70), ('eᶻ', 130), ('p = eᶻ ÷ 11.107', 190)]
    for lab, y in rows:
        o.append(T(40, y + 6, lab, 14, 'start', MUT, True))
    for x, (n, z, e, p) in zip(xs, cols):
        o.append(T(x, 48, n, 14, bold=True))
        o.append(boxt(x - 50, 52, 100, 36, [str(z)], PANEL, L2, 15))
        o.append(boxt(x - 50, 112, 100, 36, [f'{e:.3f}' if e != 1 else '1'], PANEL, L2, 15))
        bw = 100 * p / 0.7
        o.append(R(x - 50, 172, 100, 36, 'none', L2, 4, 1.2))
        o.append(R(x - 50, 172, bw, 36, ACS, AC, 4, 1.6))
        o.append(T(x, 196, f'{p:.3f}', 15, bold=True))
        o.append(L(x, 90, x, 108, L2, 1.4, arrow='m')); o.append(L(x, 150, x, 168, L2, 1.4, arrow='m'))
    o.append(T(620, 136, 'sum 11.107', 13, 'start', MUT))
    o.append(T(40, 250, 'Cross-entropy loss = −ln(p of the true class)', 14, 'start', bold=True))
    o.append(boxt(40, 264, 300, 50, ['true class 1: −ln 0.665 = 0.408', 'confident and right: small loss'], ACS, AC, 13))
    o.append(boxt(380, 264, 300, 50, ['true class 3: −ln 0.090 = 2.408', 'gave it little chance: large loss'], LVS, LV, 13))
    return 330, ''.join(o)
FIG[4] = (f4, 'Exponentiating the logits gives 7.389, 2.718 and 1; dividing by their sum 11.107 gives probabilities 0.665, 0.245 and 0.090. The loss is small (0.408) if class 1 is true and large (2.408) if class 3 is.',
          'Three columns for classes 1, 2, 3: logits 2, 1, 0; exponentials 7.389, 2.718, 1; probabilities 0.665, 0.245, 0.090 shown as bars. Below, cross-entropy loss 0.408 when class 1 is true and 2.408 when class 3 is true.')


# ---- 5.5 forward values and backward gradients through one unit ----
def f5():
    o = [T(40, 24, 'One sigmoid unit: values go forward, blame comes back', 15, 'start', bold=True)]
    xs = [70, 230, 390, 560]
    labs = [['x = 1', 'w = 1, b = 0'], ['z = wx + b', '= 1.000000'], ['a = σ(z)', '= 0.731059'], ['L = ½(a − t)²', '= 0.036165']]
    for x, l in zip(xs, labs):
        o.append(boxt(x - 60, 62, 120 if x != 560 else 140, 54, l, PANEL, L2, 13, True))
    for a, b in zip(xs, xs[1:]):
        o.append(L(a + 62, 80, b - 62, 80, AC, 2.2, arrow='n'))
        o.append(L(b - 62, 104, a + 62, 104, LV, 2.2, dash='6 4', arrow='l'))
    o.append(T(40, 52, 'forward', 13, 'start', AC, True))
    y = 150
    o.append(T(40, y, 'backward (chain rule, t = 1)', 13, 'start', LV, True))
    steps = [('∂L/∂a = a − t', '= −0.268941'), ('σ′(z) = a(1 − a)', '= 0.196612'), ('δ = ∂L/∂z', '= −0.052877'), ('∂L/∂w = δ·x', '= −0.052877')]
    for i, (a, b) in enumerate(steps):
        bx = 40 + i * 165
        o.append(boxt(bx, y + 14, 150, 52, [a, b], LVS if i == 2 else PANEL, LV if i == 2 else L2, 13))
        if i: o.append(T(bx - 8, y + 46, '×' if i == 2 else '→', 15, bold=True))
    o.append(T(40, y + 104, 'Update with η = 0.5:', 14, 'start', bold=True))
    o.append(T(40, y + 128, 'w ← 1 − 0.5 × (−0.052877) = 1.026439', 14, 'start', AC))
    o.append(T(40, y + 150, 'b ← 0 − 0.5 × (−0.052877) = 0.026439', 14, 'start', AC))
    o.append(T(420, y + 128, 'negative gradient, so both rise', 13, 'start', MUT))
    o.append(T(420, y + 150, 'and a moves toward the target 1', 13, 'start', MUT))
    return y + 168, ''.join(o)
FIG[5] = (f5, 'The forward pass gives z = 1, a = 0.731059 and loss 0.036165. Going back, the loss slope −0.268941 times σ′ = 0.196612 gives δ = −0.052877, which is also the weight gradient, so w rises to 1.026439.',
          'Top row: boxes for x = 1, z = 1, a = 0.731059 and L = 0.036165 joined by forward arrows, with dashed arrows going back. Second row: dL/da = −0.268941, σ′(z) = 0.196612, δ = −0.052877 and dL/dw = −0.052877. Below, the updated w = 1.026439 and b = 0.026439.')


# ---- 5.6 plain SGD against momentum ----
def f6():
    o = [T(40, 24, 'Same gradient g = 0.4 each step, η = 0.1: SGD against momentum', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 460, 60, 300
    fx = lambda v: x0 + v / 3 * (x1 - x0)
    fy = lambda v: y1 - (v - 0.75) / 0.27 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3], [0.75, 0.8, 0.85, 0.9, 0.95, 1.0], fx, fy, 'step', 'weight w', yfmt=lambda v: f'{v:.2f}'))
    sgd = [1, 0.96, 0.92, 0.88]; mom = [1, 0.96, 0.884, 0.7756]
    o.append(P([(fx(i), fy(v)) for i, v in enumerate(sgd)], NX, 2.5)); o.append(P([(fx(i), fy(v)) for i, v in enumerate(mom)], LV, 2.5))
    for i, v in enumerate(sgd): o.append(C(fx(i), fy(v), 5, NX))
    for i, v in enumerate(mom): o.append(C(fx(i), fy(v), 5, LV))
    o.append(Tb(fx(3) + 10, fy(0.88) + 5, '0.88', 13, 'start', NX, True)); o.append(Tb(fx(3) + 10, fy(0.7756) + 5, '0.7756', 13, 'start', LV, True))
    o.append(Tb(fx(2) - 8, fy(0.92) - 10, '0.92', 13, 'end', NX)); o.append(Tb(fx(2) - 8, fy(0.884) + 18, '0.884', 13, 'end', LV))
    o.append(Tb(fx(1) + 6, fy(0.96) - 10, '0.96 (both)', 13, 'start'))
    X = 520
    o.append(L(X, 70, X + 26, 70, NX, 2.5)); o.append(T(X + 32, 75, 'plain SGD', 13, 'start'))
    o.append(L(X, 94, X + 26, 94, LV, 2.5)); o.append(T(X + 32, 99, 'momentum β = 0.9', 13, 'start'))
    o.append(T(X, 140, 'velocity v ← 0.9v + g', 13, 'start', MUT))
    o.append(T(X, 164, 'v₁ = 0.4', 14, 'start')); o.append(T(X, 186, 'v₂ = 0.9×0.4 + 0.4 = 0.76', 13, 'start'))
    o.append(T(X, 208, 'v₃ = 0.9×0.76 + 0.4', 13, 'start')); o.append(T(X, 226, '= 1.084', 13, 'start'))
    o.append(T(X, 262, 'SGD steps stay 0.04;', 13, 'start')); o.append(T(X, 280, 'momentum’s grow to 0.1084', 13, 'start'))
    return 352, ''.join(o)
FIG[6] = (f6, 'Both runs start at w = 1 with the same gradient 0.4. Plain SGD moves 0.04 every step to 0.88; momentum’s velocity builds to 0.76 and 1.084, so its steps grow and it reaches 0.7756 after three steps.',
          'Line plot of weight against step 0 to 3. Plain SGD: 1, 0.96, 0.92, 0.88. Momentum: 1, 0.96, 0.884, 0.7756. Side notes give velocities 0.4, 0.76, 1.084.')


# ---- 5.7 the gradient through five layers ----
def f7():
    o = [T(40, 24, 'Gradient left after each layer (best case), starting from 1.0', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 100, 480, 60, 300
    fx = lambda v: x0 + v / 5 * (x1 - x0)
    fy = lambda v: y1 - (math.log10(v) + 3.2) / 3.2 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v, lab in [(1, '1'), (0.1, '0.1'), (0.01, '0.01'), (0.001, '0.001')]:
        o.append(L(x0, fy(v), x1, fy(v), LN, 1)); o.append(T(x0 - 8, fy(v) + 4.5, lab, 13, 'end', MUT))
    for k in range(6):
        o.append(T(fx(k), y1 + 20, str(k), 13, fill=MUT))
    o.append(T((x0 + x1) / 2, y1 + 42, 'layers passed', 14, fill=MUT)); o.append(T(x0, y0 - 14, 'gradient (log scale)', 13, 'start', MUT))
    sig = [0.25 ** k for k in range(6)]
    o.append(P([(fx(k), fy(1)) for k in range(6)], AC, 3)); o.append(P([(fx(k), fy(v)) for k, v in enumerate(sig)], LV, 3))
    for k, v in enumerate(sig): o.append(C(fx(k), fy(v), 5, LV))
    for k in range(6): o.append(C(fx(k), fy(1), 5, AC))
    for k, lab in [(1, '0.25'), (2, '0.0625'), (3, '0.0156'), (4, '0.0039'), (5, '0.00098')]:
        o.append(Tb(fx(k) + (-10 if k == 5 else 8), fy(sig[k]) + (18 if k == 5 else -10), lab, 13, 'end' if k == 5 else 'start', LV, k == 5))
    o.append(Tb(fx(4.6), fy(1) - 12, 'ReLU: 1.0', 13, 'middle', AC, True))
    X = 510
    o.append(T(X, 80, 'sigmoid', 14, 'start', LV, True)); o.append(T(X, 100, 'σ′ ≤ 0.25 per layer', 13, 'start'))
    o.append(T(X, 120, '0.25⁵ = 0.00098', 13, 'start')); o.append(T(X, 140, 'step = 0.1 × 0.00098', 13, 'start'))
    o.append(T(X, 158, '= 9.77 × 10⁻⁵', 13, 'start', LV, True))
    o.append(T(X, 196, 'ReLU (z > 0)', 14, 'start', AC, True)); o.append(T(X, 216, 'slope 1 per layer', 13, 'start'))
    o.append(T(X, 236, 'step = 0.1 × 1.0 = 0.1', 13, 'start', AC, True))
    o.append(T(X, 272, 'ratio 0.1 ÷ 9.77×10⁻⁵', 13, 'start', MUT)); o.append(T(X, 290, '= 1024', 13, 'start', MUT))
    return 356, ''.join(o)
FIG[7] = (f7, 'Each sigmoid layer passes back at most a quarter of the gradient, so five layers leave 0.25⁵ ≈ 0.00098 and the first weight moves only 9.77 × 10⁻⁵ per step. Active ReLU units pass it back whole, so the step is 0.1, 1024 times larger.',
          'Log-scale plot of the gradient against layers passed, 0 to 5. The ReLU line stays at 1.0. The sigmoid line falls 1, 0.25, 0.0625, 0.0156, 0.0039, 0.00098. Side notes give the weight steps 9.77 × 10⁻⁵ and 0.1.')


# ---- 5.8 convolution, ReLU, pooling ----
def f8():
    o = [T(40, 24, '3×3 filter on a 5×5 image, then ReLU and 2×2 max pooling', 15, 'start', bold=True)]
    I = [[1, 0, 1, 2, 0], [0, 1, 2, 1, 0], [1, 2, 3, 1, 1], [0, 1, 1, 2, 0], [1, 0, 2, 1, 0]]
    Fl = [[1, 0, -1]] * 3
    Cv = [[-4, -1, 5], [-5, 0, 5], [-4, -1, 5]]
    Re = [[0, 0, 5], [0, 0, 5], [0, 0, 5]]
    Po = [[0, 5], [0, 5]]
    win = {(i, j) for i in range(3) for j in range(3)}
    y = 70
    o.append(T(40 + 75, 56, 'input 5×5', 13, bold=True))
    o.append(grid(40, y, I, 30, win))
    o.append(T(212, y + 80, '∗', 22, bold=True))
    o.append(T(270, 56, 'filter', 13, bold=True)); o.append(grid(225, y + 30, Fl, 30, None, NXS, NX))
    o.append(L(330, y + 75, 362, y + 75, AC, 2, arrow='n'))
    o.append(T(410, 56, 'conv 3×3', 13, bold=True)); o.append(grid(365, y + 30, Cv, 30, {(0, 0)}, hif=ACS))
    o.append(L(460, y + 75, 486, y + 75, AC, 2, arrow='n')); o.append(T(473, y + 58, 'ReLU', 13, fill=MUT))
    o.append(T(535, 56, 'ReLU', 13, bold=True)); o.append(grid(490, y + 30, Re, 30))
    o.append(L(585, y + 75, 611, y + 75, AC, 2, arrow='n')); o.append(T(598, y + 58, 'pool', 13, fill=MUT))
    o.append(T(645, 56, 'pooled', 13, bold=True)); o.append(grid(615, y + 45, Po, 30, {(0, 1), (1, 1)}, hif=LVS))
    yy = 244
    o.append(T(40, yy, 'top-left value: the shaded 3×3 window times the filter, column by column', 13, 'start', MUT))
    o.append(T(40, yy + 24, '(1 + 0 + 1) × 1  +  (0 + 1 + 2) × 0  +  (1 + 2 + 3) × (−1)  =  2 − 6  =  −4', 15, 'start', AC, True))
    o.append(T(40, yy + 56, 'sizes: (5 − 3) ÷ 1 + 1 = 3, then (3 − 2) ÷ 1 + 1 = 2.   Parameters: 3 × 3 × 1 + 1 bias = 10.', 13, 'start'))
    o.append(T(40, yy + 78, 'The filter subtracts the right column from the left, so it lights up where brightness drops to the right.', 13, 'start', MUT))
    return yy + 94, ''.join(o)
FIG[8] = (f8, 'The 3×3 filter slides over the 5×5 input to give a 3×3 map whose first value is −4. ReLU sets the negatives to 0, and 2×2 max pooling with stride 1 leaves [[0, 5], [0, 5]].',
          'Left to right: the 5 by 5 input with its top-left 3 by 3 window shaded, the filter with columns 1, 0, −1, the convolution map −4 −1 5 / −5 0 5 / −4 −1 5, the ReLU map 0 0 5 in every row, and the pooled map 0 5 / 0 5. Below, the top-left sum 2 − 6 = −4.')


# ---- 5.9 two unrolled RNN steps ----
def f9():
    o = [T(40, 24, 'An RNN unrolled for two steps: same W = 0.5 and U = 0.5 each time', 15, 'start', bold=True)]
    hx = [90, 330, 570]
    hv = ['h₀ = 0', 'h₁ = 0.4621', 'h₂ = 0.6237']
    for x, v in zip(hx, hv):
        o.append(boxt(x - 70, 100, 140, 46, [v], ACS if x > 100 else PANEL, AC if x > 100 else L2, 14))
    for x in hx[1:]:
        o.append(boxt(x - 40, 210, 80, 40, ['x = 1'], NXS, NX, 14))
        o.append(L(x, 208, x, 150, NX, 2, arrow='x')); o.append(T(x + 8, 184, 'W', 13, 'start', NX, True))
    for a, b in zip(hx, hx[1:]):
        o.append(L(a + 72, 123, b - 74, 123, AC, 2.2, arrow='n')); o.append(T((a + b) / 2, 114, 'U', 13, fill=AC, bold=True))
    o.append(T(330, 82, 'tanh(0.5 × 1 + 0.5 × 0) = tanh(0.5)', 13, fill=MUT))
    o.append(T(570, 82, 'tanh(0.5 + 0.5 × 0.4621) = tanh(0.7311)', 13, fill=MUT))
    y = 286
    o.append(T(40, y, 'backward factor per step  ∂hₜ/∂hₜ₋₁ = U(1 − hₜ²)', 14, 'start', bold=True))
    o.append(T(40, y + 26, 'step 1: 0.5 × (1 − 0.2136) = 0.3932', 14, 'start', LV)); o.append(T(380, y + 26, 'step 2: 0.5 × (1 − 0.3890) = 0.3055', 14, 'start', LV))
    o.append(T(40, y + 52, 'two steps: 0.3932 × 0.3055 = 0.1201;   ten steps: 0.1201⁵ ≈ 0.000025', 14, 'start', LV, True))
    o.append(T(40, y + 78, 'Every factor is below 1, so an input ten steps back barely reaches the gradient: it vanishes.', 13, 'start', MUT))
    return y + 94, ''.join(o)
FIG[9] = (f9, 'The same weights turn x = 1 into h₁ = 0.4621 and then h₂ = 0.6237. Going back, each step multiplies the gradient by U(1 − h²): 0.3932, then 0.3055, so ten steps shrink it to about 0.000025.',
          'Three hidden-state boxes h0 = 0, h1 = 0.4621, h2 = 0.6237 joined by arrows labelled U, each later state also fed by an input x = 1 through W. Below, the backward factors 0.3932 and 0.3055, their product 0.1201, and about 0.000025 over ten steps.')


spec = make_spec(FIG)


def text_fixes(k):
    return []


def drop_sources():
    # university-hosted course notes: the books name no universities
    return ['cs231n.github.io']
