"""Claude's hand-drawn figures for c-ml-u2 (Machine Learning, unit 2: regression and model evaluation), one per chapter,
each drawn from that chapter's worked example with its own numbers. No chapter sentence describes the old drawings, so
text_fixes is empty."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def legend(x, y, items):
    o = []
    for i, (lab, c, dash) in enumerate(items):
        o.append(L(x, y + i * 24, x + 26, y + i * 24, c, 2.5, dash=dash)); o.append(T(x + 32, y + i * 24 + 5, lab, 13, 'start'))
    return ''.join(o)


# ---- 2.1 the least-squares line through the three shops ----
def f1():
    o = [T(40, 24, 'Three shops: ads spend x and units sold y', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 450, 56, 296
    fx = lambda v: x0 + v / 4 * (x1 - x0)
    fy = lambda v: y1 - v / 5 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], fx, fy, 'ad spend x (thousand ₹)', 'units sold y'))
    o.append(L(fx(0), fy(2 / 3), fx(4), fy(2 / 3 + 4), AC, 2.5))
    pts = [(1, 2), (2, 2), (3, 4)]
    res = ['+1/3', '−2/3', '+1/3']
    for (x, y), r in zip(pts, res):
        yh = 2 / 3 + x
        o.append(L(fx(x), fy(y), fx(x), fy(yh), LV, 2.2, dash='4 3'))
        o.append(C(fx(x), fy(y), 6, NX))
        o.append(Tb(fx(x) + 10, (fy(y) + fy(yh)) / 2 + 5, r, 13, 'start', LV, True))
    o.append(Tb(fx(3.35), fy(4.3) - 6, 'ŷ = 0.6667 + 1·x', 14, 'end', AC, True))
    X = 490
    o.append(T(X, 80, 'x̄ = 2,  ȳ = 8/3', 14, 'start'))
    o.append(T(X, 106, 'S<tspan baseline-shift="sub" font-size="11">xy</tspan> = 2,  S<tspan baseline-shift="sub" font-size="11">xx</tspan> = 2', 14, 'start'))
    o.append(T(X, 132, 'b₁ = 2 ÷ 2 = 1', 14, 'start', bold=True))
    o.append(T(X, 158, 'b₀ = 8/3 − 1 × 2 = 2/3', 14, 'start', bold=True))
    o.append(T(X, 196, 'residuals (dashed):', 13, 'start', LV, True))
    o.append(T(X, 218, '1/3, −2/3, 1/3', 14, 'start'))
    o.append(T(X, 248, 'SSE = 1/9 + 4/9 + 1/9', 14, 'start'))
    o.append(T(X, 272, '= 0.6667 units²', 14, 'start', bold=True))
    o.append(T(X, 296, 'MSE = 0.6667 ÷ 3 = 0.2222', 13, 'start', MUT))
    return 346, ''.join(o)
FIG[1] = (f1, 'The least-squares line ŷ = 0.6667 + x passes among the three shops. The dashed residuals are 1/3, −2/3 and 1/3; their squares add to SSE = 0.6667, and no other line gives a smaller sum.',
          'Scatter of three points (1,2), (2,2), (3,4) with the line y-hat = 0.6667 + x. Dashed vertical residuals of +1/3, −2/3 and +1/3 join each point to the line. Side notes give b1 = 1, b0 = 2/3, SSE 0.6667 and MSE 0.2222.')


# ---- 2.2 four gradient steps down J(w) = (w-3)^2 + 2 ----
def f2():
    o = [T(40, 24, 'Gradient descent on J(w) = (w − 3)² + 2, α = 0.2', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 520, 56, 300
    fx = lambda v: x0 + v / 5 * (x1 - x0)
    fy = lambda v: y1 - v / 12 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3, 4, 5], [0, 2, 4, 6, 8, 10, 12], fx, fy, 'weight w', 'loss J(w)'))
    o.append(P([(fx(w / 20), fy((w / 20 - 3) ** 2 + 2)) for w in range(0, 101) if (w / 20 - 3) ** 2 + 2 <= 12.2], L2, 2))
    ws = [0, 1.2, 1.92, 2.352, 2.6112]
    Js = [(w - 3) ** 2 + 2 for w in ws]
    for i in range(4):
        o.append(arc(fx(ws[i]) + 4, fy(Js[i]) - 4, fx(ws[i + 1]) - 2, fy(Js[i + 1]) - 8, -0.25, AC, 2, 'n'))
    labs = ['w₀ = 0, J = 11', 'w₁ = 1.2, J = 5.24', 'w₂ = 1.92, J = 3.17', 'w₃ = 2.352', 'w₄ = 2.6112']
    for i, (w, J) in enumerate(zip(ws, Js)):
        o.append(C(fx(w), fy(J), 6, AC))
    o.append(Tb(fx(0) + 12, fy(11) + 5, labs[0], 13, 'start'))
    o.append(Tb(fx(1.2) + 12, fy(5.24) + 5, labs[1], 13, 'start'))
    o.append(Tb(fx(1.92) + 12, fy(3.1664) + 2, labs[2], 13, 'start'))
    o.append(L(fx(2.7), fy(2), fx(3.3), fy(2), LV, 2.5)); o.append(C(fx(3), fy(2), 5, LV))
    o.append(Tb(fx(3), fy(2) + 26, 'minimum: w = 3, J = 2', 13, fill=LV, bold=True))
    X = 548
    o.append(T(X, 80, 'update rule', 13, 'start', MUT))
    o.append(T(X, 102, 'w ← w − α · 2(w − 3)', 14, 'start', bold=True))
    o.append(T(X, 136, 'each step keeps', 13, 'start'))
    o.append(T(X, 156, '1 − 2α = 0.6 of the', 13, 'start'))
    o.append(T(X, 176, 'distance to w = 3:', 13, 'start'))
    o.append(T(X, 202, '3 → 1.8 → 1.08', 14, 'start', AC, True))
    o.append(T(X, 224, '→ 0.648 → 0.3888', 14, 'start', AC, True))
    o.append(T(X, 258, 'steps shrink as', 13, 'start'))
    o.append(T(X, 278, 'the slope flattens', 13, 'start'))
    return 350, ''.join(o)
FIG[2] = (f2, 'Starting at w = 0, four updates with α = 0.2 move w to 1.2, 1.92, 2.352 and 2.6112, and J falls from 11 to 2.1512. Each step keeps 0.6 of the distance to the minimum, so the hops get shorter near w = 3, J = 2.',
          'A U-shaped loss curve J(w) = (w−3)² + 2 for w from 0 to 5. Five dots at w = 0, 1.2, 1.92, 2.352, 2.6112 are joined by arrows hopping down toward the minimum at w = 3, J = 2.')


# ---- 2.3 the sigmoid and the 0.5 threshold ----
def f3():
    o = [T(40, 24, 'p = σ(z) with z = −5 + 2x', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 540, 56, 286
    fx = lambda v: x0 + v / 5 * (x1 - x0)
    fy = lambda v: y1 - v * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3, 4, 5], [0, 0.25, 0.5, 0.75, 1], fx, fy, 'input x', 'p(class 1)', yfmt=lambda v: f'{v:g}'))
    sig = lambda x: 1 / (1 + math.exp(-(-5 + 2 * x)))
    o.append(R(fx(2.5), y0, fx(5) - fx(2.5), y1 - y0, ACS, 'none', 0, 0))
    o.append(T(fx(4.2), y1 - 14, 'class 1', 14, bold=True, fill=AC)); o.append(T(fx(0.8), y0 + 22, 'class 0', 14, bold=True, fill=MUT))
    o.append(L(x0, fy(0.5), x1, fy(0.5), LV, 1.8, dash='6 4')); o.append(T(x1 + 6, fy(0.5) + 5, 'threshold 0.5', 13, 'start', LV))
    o.append(L(fx(2.5), y0, fx(2.5), y1, LV, 1.8, dash='3 3'))
    o.append(P([(fx(i / 40), fy(sig(i / 40))) for i in range(0, 201)], AC, 3))
    o.append(Tb(fx(2.5), y1 + 40, 'boundary x = 2.5 (z = 0)', 13, fill=LV, bold=True))
    for x, lab, anc, dx in [(1, 'x = 1: z = −3, p = 0.047', 'start', 12), (3, 'x = 3: z = 1, p = 0.731', 'end', -12)]:
        o.append(C(fx(x), fy(sig(x)), 6, NX))
        o.append(Tb(fx(x) + dx, fy(sig(x)) - 12, lab, 13, anc, NX, True))
    return 344, ''.join(o)
FIG[3] = (f3, 'The sigmoid turns the score z = −5 + 2x into a probability. It crosses 0.5 at x = 2.5, the decision boundary: x = 1 gives p = 0.047 (class 0) and x = 3 gives p = 0.731 (class 1).',
          'An S-shaped sigmoid curve of p against x from 0 to 5, crossing the dashed 0.5 threshold at x = 2.5. The region right of x = 2.5 is shaded as class 1. Marked points: x = 1 with p = 0.047 and x = 3 with p = 0.731.')


# ---- 2.4 the boundary 2x1 + 3x2 = 6 ----
def f4():
    o = [T(40, 24, 'g(x) = 2x₁ + 3x₂ − 6: the sign picks the class', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 420, 64, 304
    fx = lambda v: x0 + v / 4 * (x1 - x0)
    fy = lambda v: y1 - v / 3 * (y1 - y0)
    o.append(f'<polygon points="{fx(3):.1f},{fy(0):.1f} {fx(4):.1f},{fy(0):.1f} {fx(4):.1f},{fy(3):.1f} {fx(0):.1f},{fy(3):.1f} {fx(0):.1f},{fy(2):.1f}" style="fill:var(--accent-soft)"/>')
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3, 4], [0, 1, 2, 3], fx, fy, 'x₁', 'x₂'))
    o.append(L(fx(0), fy(2), fx(3), fy(0), LV, 3))
    o.append(Tb(fx(1.55), fy(1.2) - 4, 'g = 0', 14, fill=LV, bold=True))
    o.append(T(fx(3.3), fy(2.6), 'g > 0: class +', 14, bold=True, fill=AC))
    o.append(T(fx(0.7), fy(0.75), 'g < 0: class −', 14, bold=True, fill=MUT))
    o.append(C(fx(2), fy(1), 7, AC)); o.append(Tb(fx(2) + 12, fy(1) + 5, '(2, 1)', 14, 'start', AC, True))
    o.append(C(fx(0), fy(0), 7, NX)); o.append(Tb(fx(0) + 14, fy(0) - 12, '(0, 0)', 14, 'start', NX, True))
    X = 456
    o.append(T(X, 76, 'boundary: 2x₁ + 3x₂ = 6', 14, 'start', LV, True))
    o.append(T(X, 98, 'meets the axes at (3, 0) and (0, 2)', 13, 'start'))
    o.append(T(X, 142, 'x = (2, 1):', 14, 'start', AC, True))
    o.append(T(X, 164, 'g = 4 + 3 − 6 = +1 → class +', 14, 'start'))
    o.append(T(X, 206, 'x = (0, 0):', 14, 'start', NX, True))
    o.append(T(X, 228, 'g = 0 + 0 − 6 = −6 → class −', 14, 'start'))
    o.append(T(X, 270, 'The weights (2, 3) point', 13, 'start', MUT))
    o.append(T(X, 288, 'toward the + side.', 13, 'start', MUT))
    return 356, ''.join(o)
FIG[4] = (f4, 'The line 2x₁ + 3x₂ = 6 is where the score g is zero. The point (2, 1) scores +1 and falls on the shaded class + side; the origin scores −6 and is class −.',
          'Axes x1 from 0 to 4 and x2 from 0 to 3 with the boundary line from (0,2) to (3,0). The region above the line is shaded class +. Point (2,1) lies in it with g = +1; point (0,0) lies below with g = −6.')


# ---- 2.5 three degrees, two errors each ----
def f5():
    o = [T(40, 24, 'Training and validation MSE for three polynomial fits', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 520, 54, 270
    fy = lambda v: y1 - v / 7 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in range(0, 8):
        o.append(L(x0, fy(v), x1, fy(v), LN, 1)); o.append(T(x0 - 8, fy(v) + 4.5, str(v), 13, 'end', MUT))
    o.append(T(x0, y0 - 12, 'MSE', 14, 'start', MUT))
    data = [(1, 4.2, 4.5, 'underfits', MUT), (3, 1.1, 1.4, 'pick this', AC), (9, 0.01, 6.8, 'overfits', LV)]
    for i, (d, tr, va, verdict, c) in enumerate(data):
        gx = 150 + i * 145
        o.append(R(gx - 46, fy(tr), 42, max(y1 - fy(tr), 1.5), PANEL, L2, 3, 1.6)); o.append(T(gx - 25, fy(tr) - 8, f'{tr:g}', 13))
        o.append(R(gx + 4, fy(va), 42, y1 - fy(va), NXS, NX, 3, 1.8))
        o.append(T(gx + 25, fy(va) - 8, f'{va:g}', 13, bold=True))
        o.append(T(gx, y1 + 22, f'degree {d}', 14, bold=True))
        o.append(T(gx, y1 + 42, verdict, 13, bold=True, fill=c))
    o.append(R(548, 70, 20, 16, PANEL, L2, 3, 1.6)); o.append(T(576, 83, 'training MSE', 13, 'start'))
    o.append(R(548, 96, 20, 16, NXS, NX, 3, 1.6)); o.append(T(576, 109, 'validation MSE', 13, 'start'))
    o.append(T(548, 150, 'gaps:', 13, 'start', MUT))
    o.append(T(548, 172, 'degree 1: 0.3', 13, 'start')); o.append(T(548, 192, 'degree 3: 0.3', 13, 'start'))
    o.append(T(548, 212, 'degree 9: 6.79', 13, 'start', LV, True))
    o.append(T(548, 246, 'Same gap 0.3, but', 13, 'start')); o.append(T(548, 264, 'degree 1 is high', 13, 'start'))
    o.append(T(548, 282, 'everywhere.', 13, 'start'))
    return 330, ''.join(o)
FIG[5] = (f5, 'Degree 1 has both MSEs high (4.2 and 4.5), so it underfits even though its gap is only 0.3. Degree 9 drives training MSE to 0.01 but validation MSE to 6.8. Degree 3 has the lowest validation MSE, 1.4.',
          'Grouped bars for degrees 1, 3 and 9. Training MSE 4.2, 1.1, 0.01; validation MSE 4.5, 1.4, 6.8. Labels say degree 1 underfits, degree 3 is the pick, degree 9 overfits; the gaps are 0.3, 0.3 and 6.79.')


# ---- 2.6 ridge shrinks, lasso cuts to zero ----
def f6():
    o = [T(40, 24, 'One weight with least-squares value 3, under a growing penalty λ', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 500, 56, 290
    fx = lambda v: x0 + v / 5 * (x1 - x0)
    fy = lambda v: y1 - v / 3.5 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3, 4, 5], [0, 1, 2, 3], fx, fy, 'penalty strength λ', 'weight w'))
    o.append(P([(fx(i / 20), fy(3 / (1 + i / 20))) for i in range(0, 101)], AC, 3))
    o.append(P([(fx(i / 20), fy(max(3 - i / 20, 0))) for i in range(0, 101)], LV, 3))
    o.append(L(fx(1), y1, fx(1), fy(2), L2, 1.4, dash='4 3'))
    o.append(C(fx(1), fy(1.5), 6, AC)); o.append(Tb(fx(1) - 10, fy(1.5) + 20, 'ridge 1.5', 13, 'end', AC, True))
    o.append(C(fx(1), fy(2), 6, LV)); o.append(Tb(fx(1) + 12, fy(2) - 8, 'lasso 2.0', 13, 'start', LV, True))
    o.append(C(fx(3), fy(0), 6, LV)); o.append(Tb(fx(3), fy(0) - 16, 'exactly 0 at λ = 3', 13, fill=LV, bold=True))
    o.append(Tb(fx(4.4), fy(3 / 5.4) - 12, '3 ÷ (1 + λ)', 13, fill=AC))
    X = 530
    o.append(T(X, 80, 'ridge', 15, 'start', AC, True))
    o.append(T(X, 102, 'w = 3 ÷ (1 + λ)', 14, 'start'))
    o.append(T(X, 122, 'shrinks, never 0', 13, 'start', MUT))
    o.append(T(X, 164, 'lasso', 15, 'start', LV, True))
    o.append(T(X, 186, 'w = max(3 − λ, 0)', 14, 'start'))
    o.append(T(X, 206, 'soft threshold:', 13, 'start', MUT))
    o.append(T(X, 224, 'drops the feature', 13, 'start', MUT))
    o.append(T(X, 260, 'at λ = 1:', 13, 'start', bold=True))
    o.append(T(X, 280, 'ridge 1.5, lasso 2.0', 13, 'start', bold=True))
    return 342, ''.join(o)
FIG[6] = (f6, 'Both penalties start from the least-squares weight 3. Ridge shrinks it smoothly as 3 ÷ (1 + λ) and never reaches 0; lasso subtracts λ and hits exactly 0 at λ = 3. At λ = 1 they give 1.5 and 2.0.',
          'Plot of weight w against penalty λ from 0 to 5. The ridge curve 3/(1+λ) falls smoothly, staying above 0. The lasso line 3−λ falls straight to 0 at λ = 3 and stays there. At λ = 1 ridge is 1.5 and lasso is 2.0.')


# ---- 2.7 five-fold cross-validation ----
def f7():
    o = [T(40, 24, 'Five-fold cross-validation: every fold is tested once', 15, 'start', bold=True)]
    acc = [0.80, 0.82, 0.78, 0.84, 0.81]
    cx, cw, ch = 150, 84, 34
    for j in range(5):
        o.append(T(cx + j * (cw + 6) + cw / 2, 56, f'fold {j + 1}', 13, fill=MUT))
    for i in range(5):
        y = 68 + i * (ch + 8)
        o.append(T(40, y + ch / 2 + 5, f'round {i + 1}', 14, 'start', bold=True))
        for j in range(5):
            x = cx + j * (cw + 6)
            if i == j:
                o.append(boxt(x, y, cw, ch, ['test'], LVS, LV, 14))
            else:
                o.append(boxt(x, y, cw, ch, ['fit'], PANEL, L2, 13, fills=[MUT]))
        o.append(T(cx + 5 * (cw + 6) + 10, y + ch / 2 + 5, f'accuracy {acc[i]:.2f}', 14, 'start', LV, True))
    y = 68 + 5 * (ch + 8) + 10
    o.append(T(40, y + 16, 'mean = (0.80 + 0.82 + 0.78 + 0.84 + 0.81) ÷ 5 = 4.05 ÷ 5 = 0.81', 15, 'start', bold=True, fill=AC))
    o.append(T(40, y + 40, 'Each round fits on four folds and scores on the fifth; no case is scored by a model that saw it.', 13, 'start', MUT))
    return y + 56, ''.join(o)
FIG[7] = (f7, 'In each of five rounds one fold is held out for testing and the other four fit the model, so every fold is tested exactly once. The five accuracies, 0.80, 0.82, 0.78, 0.84 and 0.81, average to 0.81.',
          'A five by five grid of rounds and folds. The diagonal cells are marked test and the rest fit. Each round lists its accuracy: 0.80, 0.82, 0.78, 0.84, 0.81. The mean 0.81 is written below.')


spec = make_spec(FIG)


def text_fixes(k):
    return []


def drop_sources():
    # university-hosted course notes: the books name no universities
    return ['stanford.edu']
