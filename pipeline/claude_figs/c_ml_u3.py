"""Claude's hand-drawn figures for c-ml-u3 (Machine Learning, unit 3: classification with trees, Bayes, kNN and SVM), one
per chapter, each drawn from that chapter's worked example with its own numbers. No chapter sentence describes the old
drawings, so text_fixes is empty."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def dots(x, y, labels, r=8, gap=20):
    """a row of class dots: 'Y' filled accent, 'N' filled live"""
    o = []
    for i, c in enumerate(labels):
        col = AC if c == 'Y' else LV
        o.append(f'<circle cx="{x + i * gap:.1f}" cy="{y:.1f}" r="{r}" style="fill:{col}"/>')
    return ''.join(o)


# ---- 3.1 ID3 compares the two splits ----
def f1():
    o = [T(40, 24, 'ID3 tries each attribute and keeps the bigger entropy drop', 15, 'start', bold=True)]
    o.append(R(250, 40, 220, 66, PANEL, L2, 8, 1.8))
    o.append(T(360, 62, '6 days: 4 Yes, 2 No', 14, bold=True))
    o.append(dots(310, 84, 'YYYYNN', 7, 20)); o.append(T(360, 124, 'H(S) = 0.918 bits', 14, bold=True))
    for side, (x0, attr, kids, ig, good) in enumerate([
            (30, 'split on Weather', [('Sunny', 'YYN', '0.918'), ('Rain', 'YYN', '0.918')], '0.918 − 0.918 = 0 bits', False),
            (380, 'split on Wind', [('Weak', 'YYYY', '0'), ('Strong', 'NN', '0')], '0.918 − 0 = 0.918 bits', True)]):
        c = AC if good else L2
        o.append(L(360, 130, x0 + 155, 150, L2, 1.6, arrow='m'))
        o.append(R(x0, 152, 310, 170, ACS if good else 'none', c, 10, 2.2 if good else 1.6))
        o.append(T(x0 + 155, 176, attr, 15, bold=True, fill=AC if good else INK))
        for j, (v, labs, h) in enumerate(kids):
            bx = x0 + 14 + j * 148
            o.append(R(bx, 190, 134, 76, PANEL, L2, 8, 1.4))
            o.append(T(bx + 67, 210, v, 14, bold=True))
            o.append(dots(bx + 67 - (len(labs) - 1) * 10, 230, labs, 7, 20))
            o.append(T(bx + 67, 256, f'H = {h}', 13))
        o.append(T(x0 + 155, 290, 'IG = ' + ig, 14, bold=True, fill=AC if good else MUT))
        o.append(T(x0 + 155, 310, 'chosen as the root' if good else 'tells us nothing', 13, bold=good, fill=AC if good else MUT))
    o.append(dots(40, 348, 'Y', 7)); o.append(T(54, 353, 'Play = Yes', 13, 'start'))
    o.append(dots(150, 348, 'N', 7)); o.append(T(164, 353, 'Play = No', 13, 'start'))
    o.append(T(690, 353, 'Both Wind branches are pure, so each ends in a leaf.', 13, 'end', MUT))
    return 368, ''.join(o)
FIG[1] = (f1, 'Weather leaves each branch as mixed as the parent (2 Yes, 1 No), so its gain is 0 bits. Wind splits the six days into 4 Yes and 2 No exactly, a gain of 0.918 bits, so ID3 puts Wind at the root and both branches become leaves.',
          'The parent node of 6 days, 4 Yes and 2 No, entropy 0.918 bits, above two candidate splits. Weather gives Sunny and Rain, each 2 Yes 1 No with entropy 0.918, gain 0. Wind gives Weak with 4 Yes and Strong with 2 No, entropy 0 each, gain 0.918, chosen as the root.')


# ---- 3.2 likelihood picks h2, the prior flips it to h1 ----
def f2():
    o = [T(40, 24, '7 heads in 10 tosses: h1 says p = 0.5, h2 says p = 0.8', 15, 'start', bold=True)]

    def panel(x0, title, sub, vals, fmt, top, pick, note):
        y0, y1 = 80, 260
        fy = lambda v: y1 - v / top * (y1 - y0)
        p = [T(x0 + 120, 54, title, 15, bold=True), T(x0 + 120, 72, sub, 13, fill=MUT)]
        p.append(L(x0, y1, x0 + 240, y1, L2, 1.5))
        for i, (lab, v) in enumerate(vals):
            bx = x0 + 30 + i * 110
            c = AC if i == pick else L2
            p.append(R(bx, fy(v), 70, y1 - fy(v), ACS if i == pick else PANEL, c, 3, 2 if i == pick else 1.6))
            p.append(T(bx + 35, fy(v) - 8, fmt(v), 14, bold=True, fill=AC if i == pick else INK))
            p.append(T(bx + 35, y1 + 22, lab, 14, bold=True))
        p.append(T(x0 + 120, y1 + 48, note, 14, bold=True, fill=AC))
        return ''.join(p)
    o.append(panel(30, 'likelihood P(D | h)', '120 × pᵏ(1 − p)ⁿ⁻ᵏ', [('h1', 0.1172), ('h2', 0.2013)], lambda v: f'{v:.4f}', 0.24, 1, 'MLE picks h2'))
    o.append(L(300, 170, 380, 170, AC, 2.2, arrow='n'))
    o.append(Tb(340, 150, '× prior', 14, bold=True)); o.append(T(340, 196, '0.9 and 0.1', 13, fill=MUT))
    o.append(panel(420, 'score P(D | h) · P(h)', '0.9 × 0.1172,  0.1 × 0.2013', [('h1', 0.1055), ('h2', 0.0201)], lambda v: f'{v:.4f}', 0.24, 0, 'MAP picks h1'))
    o.append(T(40, 340, 'Normalised posteriors: h1 0.8397, h2 0.1603. The strong prior 0.9 outweighs h2’s better fit.', 14, 'start'))
    o.append(T(40, 362, 'Unrestricted MLE: p = k ÷ n = 7 ÷ 10 = 0.7.', 13, 'start', MUT))
    return 378, ''.join(o)
FIG[2] = (f2, 'On likelihood alone h2 fits better (0.2013 against 0.1172), so MLE picks h2. Multiplying by the priors 0.9 and 0.1 gives scores 0.1055 and 0.0201, so MAP picks h1: the prior flips the decision.',
          'Two bar panels. Left, likelihood: h1 0.1172, h2 0.2013, MLE picks h2. An arrow labelled times prior leads to the right panel, scores: h1 0.1055, h2 0.0201, MAP picks h1. Below, the normalised posteriors 0.8397 and 0.1603.')


# ---- 3.3 the two class scores for the new day ----
def f3():
    o = [T(40, 24, 'New day: Weather = Sunny, Wind = Strong (Laplace α = 1, V = 2)', 15, 'start', bold=True)]
    heads = ['prior', 'P(Sunny | C)', 'P(Strong | C)', 'score']
    xs = [110, 250, 390, 560]
    for x, h in zip(xs, heads):
        o.append(T(x + 55, 56, h, 13, fill=MUT, bold=True))
    rows = [('Yes', ['4/6 = 0.667', '3/6 = 0.5', '1/6 = 0.167', '0.0556'], ['', '(2+1)/(4+2)', '(0+1)/(4+2)', ''], PANEL, L2),
            ('No', ['2/6 = 0.333', '2/4 = 0.5', '3/4 = 0.75', '0.125'], ['', '(1+1)/(2+2)', '(2+1)/(2+2)', ''], ACS, AC)]
    for i, (cls, vals, sub, f, c) in enumerate(rows):
        y = 70 + i * 96
        o.append(T(40, y + 38, cls, 16, 'start', AC if i else INK, True))
        for j, (x, v, s) in enumerate(zip(xs, vals, sub)):
            last = j == 3
            o.append(R(x, y, 110, 58, f if last else PANEL, c if last else L2, 8, 2 if last else 1.4))
            o.append(T(x + 55, y + (26 if s else 35), v, 14, bold=last))
            if s: o.append(T(x + 55, y + 46, s, 13, fill=MUT))
            if j < 2: o.append(T(x + 125, y + 35, '×', 16, bold=True))
        o.append(T(530, y + 35, '=', 16, bold=True))
    o.append(Tb(445, 142, 'zero Strong days for Yes: smoothing keeps 1/6, not 0', 13, fill=LV, bold=True))
    o.append(T(40, 286, 'Compare: 0.125 > 0.0556, so predict No.', 15, 'start', AC, True))
    o.append(T(40, 310, 'Posterior for No = 0.125 ÷ (0.125 + 0.0556) = 0.692.', 14, 'start'))
    return 326, ''.join(o)
FIG[3] = (f3, 'Each class score is prior × P(Sunny | class) × P(Strong | class). No wins, 0.125 to 0.0556, mostly because Strong wind is common on No days (3/4) and rare on Yes days, where smoothing gives 1/6 instead of 0.',
          'Two rows of products. Yes: prior 0.667 times P(Sunny given Yes) 0.5 times P(Strong given Yes) 0.167 equals 0.0556. No: 0.333 times 0.5 times 0.75 equals 0.125. The No score is highlighted; posterior for No is 0.692.')


# ---- 3.4 posterior weight split by vote ----
def f4():
    o = [T(40, 24, 'Every hypothesis votes, weighted by its posterior P(h | D)', 15, 'start', bold=True)]
    x0, W, y = 60, 600, 84
    segs = [('h1', 0.5, 'Yes', AC, ACS), ('h3', 0.2, 'Yes', AC, ACS), ('h2', 0.3, 'No', LV, LVS)]
    x = x0
    for name, w, vote, c, f in segs:
        o.append(R(x, y, W * w, 54, f, c, 4, 1.8))
        o.append(T(x + W * w / 2, y + 24, name, 15, bold=True)); o.append(T(x + W * w / 2, y + 44, f'{w} → {vote}', 13))
        x += W * w
    o.append(T(x0, y - 12, '0', 13, fill=MUT)); o.append(T(x0 + W, y - 12, '1', 13, fill=MUT))
    o.append(brace(x0, x0 + W * 0.7, y + 66, AC))
    o.append(T(x0 + W * 0.35, y + 92, 'Yes: 0.5 + 0.2 = 0.7', 15, bold=True, fill=AC))
    o.append(brace(x0 + W * 0.7, x0 + W, y + 66, LV))
    o.append(T(x0 + W * 0.85, y + 92, 'No: 0.3', 15, bold=True, fill=LV))
    o.append(boxt(40, 214, 300, 78, ['Bayes optimal', 'adds the weights by label', 'predicts Yes (0.7 > 0.3)'], ACS, AC, 13, True))
    o.append(boxt(380, 214, 300, 78, ['Gibbs', 'draws one h at random from the bar,', 'so says Yes with probability 0.7'], NXS, NX, 13, True))
    return 306, ''.join(o)
FIG[4] = (f4, 'The posterior mass 1 splits as h1 0.5, h3 0.2 and h2 0.3. h1 and h3 say Yes, so Yes collects 0.7 and Bayes optimal predicts Yes. Gibbs instead draws one hypothesis, so it says Yes 70% of the time.',
          'A bar from 0 to 1 split into h1 0.5 and h3 0.2, both voting Yes, and h2 0.3 voting No. Braces show Yes totals 0.7 and No 0.3. Two boxes: Bayes optimal predicts Yes; Gibbs draws one hypothesis and says Yes with probability 0.7.')


# ---- 3.5 the chain Fear -> Study -> Pass ----
def f5():
    o = [T(40, 24, 'A three-node Bayes net and its two eliminations', 15, 'start', bold=True)]
    nodes = [(110, 'Fear'), (360, 'Study'), (610, 'Pass')]
    for x, n in nodes:
        o.append(f'<ellipse cx="{x}" cy="70" rx="62" ry="24" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
        o.append(T(x, 75, n, 15, bold=True))
    o.append(L(174, 70, 294, 70, AC, 2.2, arrow='n')); o.append(L(424, 70, 544, 70, AC, 2.2, arrow='n'))
    tabs = [(40, ['P(F) = 0.3']), (290, ['P(S | F) = 0.8', 'P(S | ¬F) = 0.5']), (540, ['P(P | S) = 0.9', 'P(P | ¬S) = 0.3'])]
    for x, lines in tabs:
        o.append(boxt(x, 104, 140, 22 + 20 * len(lines), lines, PANEL, L2, 13))
    y = 186
    o.append(T(40, y, 'Sum out Fear', 14, 'start', NX, True))
    o.append(T(40, y + 24, 'P(S) = 0.3 × 0.8 + 0.7 × 0.5 = 0.24 + 0.35 = 0.59', 14, 'start'))
    o.append(T(40, y + 46, 'P(¬S) = 0.3 × 0.2 + 0.7 × 0.5 = 0.06 + 0.35 = 0.41', 14, 'start'))
    o.append(T(40, y + 82, 'Sum out Study', 14, 'start', NX, True))
    o.append(T(40, y + 106, 'P(Pass) = 0.9 × 0.59 + 0.3 × 0.41 = 0.531 + 0.123 = 0.654', 14, 'start'))
    o.append(R(470, y + 80, 210, 40, ACS, AC, 8, 2)); o.append(T(575, y + 106, 'P(Pass) = 0.654', 15, bold=True, fill=AC))
    o.append(T(40, y + 142, 'Each node needs only its own parent: 1 + 2 + 2 = 5 numbers instead of a full 8-row table.', 13, 'start', MUT))
    return y + 158, ''.join(o)
FIG[5] = (f5, 'Fear influences Study and Study influences Pass, each through its own small table. Summing out Fear gives P(Study) = 0.59; summing out Study then gives P(Pass) = 0.654.',
          'Three nodes in a row, Fear to Study to Pass, each with its conditional table: P(F) 0.3; P(S given F) 0.8 and given not F 0.5; P(P given S) 0.9 and given not S 0.3. Below, the two sums give P(S) 0.59 and P(Pass) 0.654.')


# ---- 3.6 the three nearest neighbours of Q ----
def f6():
    o = [T(40, 24, 'k = 3 nearest neighbours of Q(2, 2)', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 70, 400, 62, 320
    fx = lambda v: x0 + v / 6 * (x1 - x0)
    fy = lambda v: y1 - v / 5 * (y1 - y0)
    r = 2.24 * (x1 - x0) / 6
    o.append(f'<circle cx="{fx(2):.1f}" cy="{fy(2):.1f}" r="{r:.1f}" style="fill:var(--accent-soft);fill-opacity:0.5;stroke:var(--accent);stroke-width:1.6;stroke-dasharray:6 4"/>')
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5], fx, fy, 'x₁', 'x₂'))
    pts = [('A', 1, 1, '+', '1.41'), ('B', 2, 1, '+', '1.00'), ('C', 4, 4, '−', '2.83'), ('D', 4, 3, '−', '2.24'), ('E', 5, 4, '−', '3.61')]
    for n, x, y, s, d in pts:
        near = n in 'ABD'
        o.append(L(fx(2), fy(2), fx(x), fy(y), AC if near else L2, 2 if near else 1.2, dash=None if near else '4 3'))
    for n, x, y, s, d in pts:
        c = AC if s == '+' else LV
        o.append(C(fx(x), fy(y), 9, c)); o.append(T(fx(x), fy(y) + 5, s, 14, bold=True, fill='var(--fig)'))
    lab = {'A': (-14, 18, 'end'), 'B': (14, 20, 'start'), 'C': (-12, -14, 'end'), 'D': (14, 5, 'start'), 'E': (12, -14, 'start')}
    for n, x, y, s, d in pts:
        dx, dy, a = lab[n]
        o.append(Tb(fx(x) + dx, fy(y) + dy, f'{n} {d}', 13, a, INK, n in 'ABD'))
    o.append(R(fx(2) - 9, fy(2) - 9, 18, 18, NX, NX, 3, 1)); o.append(Tb(fx(2) - 14, fy(2) - 14, 'Q', 14, 'end', NX, True))
    X = 440
    o.append(T(X, 70, 'sorted distances', 13, 'start', MUT))
    for i, (n, d, s) in enumerate([('B', '1.00', '+'), ('A', '1.41', '+'), ('D', '2.24', '−'), ('C', '2.83', '−'), ('E', '3.61', '−')]):
        near = i < 3
        o.append(T(X, 96 + i * 22, f'{n}  {d}  {s}', 14, 'start', AC if near else MUT, near))
    o.append(T(X + 120, 118, 'k = 3', 13, 'start', AC, True))
    o.append(T(X, 228, 'vote: 2 plus, 1 minus → +', 14, 'start', bold=True))
    o.append(T(X, 254, 'weights 1/d:', 13, 'start', MUT))
    o.append(T(X, 274, '+ : 1.000 + 0.707 = 1.707', 13, 'start'))
    o.append(T(X, 294, '− : 0.447  → still +', 13, 'start'))
    return 376, ''.join(o)
FIG[6] = (f6, 'The dashed circle of radius 2.24 around Q holds its three nearest points, B, A and D. Two are + and one is −, so the vote is +; weighting by 1/d gives 1.707 against 0.447, still +.',
          'Scatter with query Q at (2,2), positive points A (1,1) and B (2,1), negative points C (4,4), D (4,3), E (5,4). Lines from Q show distances; a circle of radius 2.24 encloses B, A and D, the three nearest, voting plus.')


# ---- 3.7 one-feature maximum margin ----
def f7():
    o = [T(40, 24, 'Maximum margin on one feature: w = 1, b = −1', 15, 'start', bold=True)]
    fx = lambda v: 120 + v * 200
    y = 170
    o.append(R(fx(0), 70, fx(2) - fx(0), 150, ACS, 'none', 0, 0))
    o.append(L(fx(-0.4), y, fx(2.45), y, L2, 2, arrow='m'))
    for v in [0, 1, 2]:
        o.append(T(fx(v), y + 36, f'x = {v}', 14, fill=MUT))
    o.append(L(fx(0), 70, fx(0), y + 16, NX, 1.8, dash='6 4')); o.append(L(fx(2), 70, fx(2), y + 16, NX, 1.8, dash='6 4'))
    o.append(L(fx(1), 60, fx(1), y + 16, LV, 3))
    o.append(C(fx(0), y, 11, NX)); o.append(T(fx(0), y + 5, '−', 15, bold=True, fill='var(--fig)'))
    o.append(C(fx(2), y, 11, AC)); o.append(T(fx(2), y + 5, '+', 15, bold=True, fill='var(--fig)'))
    o.append(T(fx(0), 58, 'wx + b = −1', 13, fill=NX, bold=True)); o.append(T(fx(2), 58, 'wx + b = +1', 13, fill=NX, bold=True))
    o.append(Tb(fx(1), 92, 'boundary x = 1', 14, fill=LV, bold=True))
    o.append(T(fx(0), 250, 'support vector', 13, fill=NX)); o.append(T(fx(2), 250, 'support vector', 13, fill=AC))
    o.append(L(fx(0), 280, fx(2), 280, INK, 1.8, arrow=None)); o.append(L(fx(0), 274, fx(0), 286, INK, 1.8)); o.append(L(fx(2), 274, fx(2), 286, INK, 1.8))
    o.append(Tb(fx(1), 285, 'margin 2 / ‖w‖ = 2', 14, bold=True))
    o.append(T(40, 322, 'At the support vectors w·0 + b = −1 and w·2 + b = +1, so b = −1 and w = 1.', 14, 'start', bold=True))
    return 338, ''.join(o)
FIG[7] = (f7, 'The negative point at x = 0 and the positive point at x = 2 both sit on the margin, so both are support vectors. Solving wx + b = ∓1 at them gives w = 1, b = −1: the boundary is x = 1 and the margin is 2.',
          'A number line with a negative point at 0 and a positive point at 2, dashed margin lines through both, a solid boundary at x = 1 and a bracket showing margin width 2. Side note: w·0 + b = −1, w·2 + b = +1, so b = −1, w = 1.')


# ---- 3.8 one AdaBoost round moves the weight to x = 3 ----
def f8():
    o = [T(40, 24, 'One AdaBoost round: the weak rule “+1 if x ≤ 3” misses x = 3', 15, 'start', bold=True)]
    xs = [140, 270, 400, 530]
    y = 64
    o.append(T(40, y + 24, 'point', 13, 'start', MUT)); o.append(T(40, y + 56, 'true y', 13, 'start', MUT)); o.append(T(40, y + 86, 'h(x)', 13, 'start', MUT))
    ys = ['+1', '+1', '−1', '−1']; hs = ['+1', '+1', '+1', '−1']
    for i, x in enumerate(xs):
        o.append(T(x, y + 24, f'x = {i + 1}', 14, bold=True))
        o.append(T(x, y + 56, ys[i], 14))
        bad = i == 2
        o.append(T(x, y + 86, hs[i] + ('  ✗' if bad else '  ✓'), 14, bold=bad, fill=LV if bad else AC))
    o.append(L(465, y + 4, 465, y + 100, LV, 2, dash='5 4')); o.append(T(465, y + 116, 'threshold x = 3', 13, fill=LV))
    y0, y1 = 200, 320
    fy = lambda v: y1 - v / 0.55 * (y1 - y0)
    o.append(L(90, y1, 600, y1, L2, 1.5))
    before = [0.25] * 4; after = [0.1667, 0.1667, 0.5, 0.1667]
    for i, x in enumerate(xs):
        o.append(R(x - 40, fy(before[i]), 34, y1 - fy(before[i]), PANEL, L2, 3, 1.6)); o.append(T(x - 23, fy(before[i]) - 6, '0.25', 13))
        bad = i == 2
        o.append(R(x + 4, fy(after[i]), 34, y1 - fy(after[i]), LVS if bad else ACS, LV if bad else AC, 3, 1.8))
        o.append(T(x + 21, fy(after[i]) - 6, f'{after[i]:.4g}', 13, bold=bad, fill=LV if bad else INK))
    o.append(R(620, 230, 18, 14, PANEL, L2, 3, 1.4)); o.append(T(644, 242, 'before', 13, 'start'))
    o.append(R(620, 254, 18, 14, ACS, AC, 3, 1.4)); o.append(T(644, 266, 'after', 13, 'start'))
    o.append(T(40, 350, 'ε = 0.25,  α = ½ ln(0.75 ÷ 0.25) = ½ ln 3 = 0.5493', 14, 'start', bold=True))
    o.append(T(40, 374, 'wrong: 0.25·e^0.5493 = 0.4330 → 0.5;   right: 0.25·e^−0.5493 = 0.1443 → 0.1667 (÷ 0.8660)', 13, 'start'))
    return 390, ''.join(o)
FIG[8] = (f8, 'The weak rule is wrong only at x = 3, so ε = 0.25 and α = 0.5493. After the round that point carries half of all the weight (0.5) and the three correct points drop to 0.1667 each, so the next rule must focus on x = 3.',
          'Four points x = 1 to 4 with true labels +1, +1, −1, −1 and weak-rule outputs +1, +1, +1, −1; x = 3 is marked wrong. Bars show weights before, 0.25 each, and after, 0.1667, 0.1667, 0.5, 0.1667.')


# ---- 3.9 locally weighted line at the query x = 1 ----
def f9():
    o = [T(40, 24, 'Locally weighted regression at the query x = 1 (τ = 1)', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 480, 62, 250
    fx = lambda v: x0 + (v + 0.5) / 3 * (x1 - x0)
    fy = lambda v: y1 - v / 5 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2], [0, 1, 2, 3, 4, 5], fx, fy, '', 'y'))
    o.append(L(fx(-0.5), fy(0.774 - 0.75), fx(2.5), fy(0.774 + 3.75), AC, 2.5))
    o.append(Tb(fx(2.48), fy(3.3), 'y = 0.774 + 1.5x', 13, 'end', AC, True))
    w = {0: 0.607, 1: 1.0, 2: 0.607}
    for (x, y) in [(0, 1), (1, 2), (2, 4)]:
        o.append(C(fx(x), fy(y), 4 + 5 * w[x], NX))
    o.append(Tb(fx(0) + 14, fy(1) + 6, '(0, 1)', 13, 'start')); o.append(Tb(fx(2) - 14, fy(4) - 2, '(2, 4)', 13, 'end'))
    o.append(L(fx(1), y1, fx(1), fy(2.274), LV, 1.6, dash='4 3'))
    o.append(R(fx(1) - 7, fy(2.274) - 7, 14, 14, LV, LV, 2, 1))
    o.append(Tb(fx(1) - 14, fy(2.274) - 10, 'prediction 2.274', 14, 'end', LV, True))
    o.append(Tb(fx(1) + 14, fy(2) + 18, '(1, 2)', 13, 'start'))
    # the Gaussian weight under the plot
    g0, g1 = 270, 330
    o.append(L(x0, g1, x1, g1, L2, 1.5))
    o.append(P([(fx(-0.5 + i * 3 / 120), g1 - (g1 - g0) * math.exp(-((-0.5 + i * 3 / 120) - 1) ** 2 / 2)) for i in range(121)], LV, 2.2))
    for x in [0, 1, 2]:
        o.append(L(fx(x), g1, fx(x), g1 - (g1 - g0) * w[x], LV, 1.4, dash='3 3'))
        o.append(T(fx(x), g1 + 20, str(x), 13, fill=MUT))
        o.append(Tb(fx(x) + (20 if x == 0 else (-20 if x == 2 else 0)), g1 - (g1 - g0) * w[x] - 8, f'{w[x]:.3f}', 13, 'middle', LV, True))
    o.append(T(x0 - 8, g0 + 34, 'weight', 13, 'end', MUT))
    o.append(T((x0 + x1) / 2, g1 + 42, 'x', 14, fill=MUT))
    X = 510
    o.append(T(X, 72, 'weights', 13, 'start', MUT)); o.append(T(X, 92, 'exp(−(x − 1)² / 2)', 14, 'start'))
    o.append(T(X, 128, 'weighted means', 13, 'start', MUT))
    o.append(T(X, 148, 'x̄ = 2.213 ÷ 2.213 = 1', 14, 'start')); o.append(T(X, 170, 'ȳ = 5.033 ÷ 2.213 = 2.274', 14, 'start'))
    o.append(T(X, 206, 'local slope b = 1.500', 14, 'start')); o.append(T(X, 228, 'intercept a = 0.774', 14, 'start'))
    o.append(T(X, 264, 'ŷ(1) = 0.774 + 1.500', 14, 'start', LV, True)); o.append(T(X, 286, '= 2.274', 14, 'start', LV, True))
    return 384, ''.join(o)
FIG[9] = (f9, 'Points near the query count more: the Gaussian gives weight 1.000 at x = 1 and 0.607 at x = 0 and x = 2 (dot size shows weight). The weighted line y = 0.774 + 1.5x predicts 2.274 at x = 1.',
          'Top: three training points (0,1), (1,2), (2,4) with the local line y = 0.774 + 1.5x and the prediction 2.274 marked at x = 1. Bottom: the Gaussian weight curve centred at x = 1, with weights 0.607, 1.000, 0.607 at x = 0, 1, 2.')


spec = make_spec(FIG)


def text_fixes(k):
    return []
