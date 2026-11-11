"""Claude's hand-drawn figures for c-ml-u4 (Machine Learning, unit 4: unsupervised learning and dimensionality
reduction), one per chapter, each drawn from that chapter's worked example with its own numbers.

Drawing the examples exposed two errors that the module also corrects:
- 4.2 claimed the SSE "drops to 30 after three iterations, as shown in the figure"; the example converges after one
  iteration at SSE 78.75 (text_fixes).
- 4.5 took (1,1)/√2 as the first principal component of (2,0), (0,2), (2,2); the covariance [[1.333, −0.667],
  [−0.667, 1.333]] has (1,−1)/√2 for λ₁ = 2, so the projections are 1.414, −1.414 and 0 (chapter_fix)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def sq(x, y, s=12, c=NX, fill=None):
    return f'<rect x="{x - s / 2:.1f}" y="{y - s / 2:.1f}" width="{s}" height="{s}" rx="2" style="fill:{fill or c};stroke:{c};stroke-width:2"/>'


# ---- 4.1 K-means on six monthly spends ----
def f1():
    o = [T(40, 24, 'K-means with K = 2 on six monthly spends (₹)', 15, 'start', bold=True)]
    fx = lambda v: 170 + (v - 1000) / 4500 * 500
    y = 120
    o.append(L(fx(1000), y, fx(5500), y, L2, 2))
    for v in [1000, 2000, 3000, 4000, 5000]:
        o.append(L(fx(v), y, fx(v), y + 6, L2, 1.5)); o.append(T(fx(v), y + 24, f'{v:,}', 13, fill=MUT))
    low, high = [1200, 1300, 1250], [5000, 5200, 5100]
    for v in low: o.append(C(fx(v), y, 7, AC))
    for v in high: o.append(C(fx(v), y, 7, LV))
    o.append(R(fx(1150), y - 22, fx(1350) - fx(1150), 44, 'none', AC, 10, 1.6, dash='5 4'))
    o.append(R(fx(4950), y - 22, fx(5250) - fx(4950), 44, 'none', LV, 10, 1.6, dash='5 4'))
    o.append(T(fx(1250), y - 34, '1200, 1300, 1250', 13, fill=AC, bold=True))
    o.append(T(fx(5100), y - 34, '5000, 5200, 5100', 13, fill=LV, bold=True))
    o.append(T(fx(3150), y - 8, 'gap of 3700', 13, fill=MUT))
    yy = 196
    o.append(T(40, yy, 'start', 13, 'start', MUT)); o.append(T(40, yy + 34, 'after one pass', 13, 'start', MUT))
    o.append(sq(fx(1200), yy - 4, 12, AC, 'var(--fig)')); o.append(T(fx(1200) + 14, yy + 1, 'c₁ = 1200', 13, 'start', AC))
    o.append(sq(fx(5000), yy - 4, 12, LV, 'var(--fig)')); o.append(T(fx(5000) - 14, yy + 1, 'c₂ = 5000', 13, 'end', LV))
    o.append(sq(fx(1250), yy + 30, 12, AC)); o.append(T(fx(1250) + 14, yy + 35, 'c₁ = (1200 + 1300 + 1250) ÷ 3 = 1250', 13, 'start', AC, True))
    o.append(sq(fx(5100), yy + 30, 12, LV)); o.append(T(fx(5100) - 14, yy + 35, 'c₂ = 5100', 13, 'end', LV, True))
    o.append(T(40, yy + 76, 'A second pass assigns every customer to the same centroid, so K-means has converged.', 14, 'start'))
    o.append(T(40, yy + 98, 'It is a partitioning method: K is fixed first and each point joins exactly one cluster.', 13, 'start', MUT))
    return yy + 114, ''.join(o)
FIG[1] = (f1, 'The six spends fall into a low group and a high group 3700 apart. One K-means pass moves c₁ from 1200 to the group mean 1250 and c₂ from 5000 to 5100; no customer changes group, so the method stops.',
          'A number line from 1000 to 5500 rupees with three low spends near 1250 and three high spends near 5100. Square markers show the centroids starting at 1200 and 5000 and moving to 1250 and 5100.')


# ---- 4.2 one Lloyd iteration in 2-D ----
def f2():
    o = [T(40, 24, 'One K-means iteration on eight points, K = 2', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 70, 420, 56, 330
    fx = lambda v: x0 + v / 10 * (x1 - x0)
    fy = lambda v: y1 - v / 10 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6, 8, 10], [0, 2, 4, 6, 8, 10], fx, fy, 'x', 'y'))
    c1 = [(1, 2), (1, 4), (2, 3), (8, 1)]; c2 = [(5, 8), (6, 9), (5, 7), (9, 2)]
    n1, n2 = (3, 2.5), (6.25, 6.5)
    for p in c1: o.append(L(fx(p[0]), fy(p[1]), fx(n1[0]), fy(n1[1]), AC, 1.2, dash='3 3'))
    for p in c2: o.append(L(fx(p[0]), fy(p[1]), fx(n2[0]), fy(n2[1]), LV, 1.2, dash='3 3'))
    for p in c1: o.append(C(fx(p[0]), fy(p[1]), 6, AC))
    for p in c2: o.append(C(fx(p[0]), fy(p[1]), 6, LV))
    o.append(sq(fx(1), fy(2), 16, AC, 'none')); o.append(sq(fx(5), fy(8), 16, LV, 'none'))
    o.append(sq(fx(3), fy(2.5), 13, AC)); o.append(sq(fx(6.25), fy(6.5), 13, LV))
    o.append(Tb(fx(3) + 12, fy(2.5) - 10, "C₁′ (3, 2.5)", 13, 'start', AC, True))
    o.append(Tb(fx(6.25) + 12, fy(6.5) + 18, "C₂′ (6.25, 6.5)", 13, 'start', LV, True))
    o.append(Tb(fx(8), fy(1) + 22, '(8, 1)', 13, fill=AC)); o.append(Tb(fx(9), fy(2) - 12, '(9, 2)', 13, fill=LV))
    X = 450
    o.append(T(X, 70, 'hollow squares: start', 13, 'start', MUT)); o.append(T(X, 88, 'C₁ = (1, 2), C₂ = (5, 8)', 13, 'start'))
    o.append(T(X, 116, 'filled squares: new means', 13, 'start', MUT))
    o.append(T(X, 150, 'close calls (distance²):', 13, 'start', bold=True))
    o.append(T(X, 172, '(8, 1): 50 to C₁, 58 to C₂', 13, 'start', AC)); o.append(T(X, 192, '→ joins C₁', 13, 'start', AC))
    o.append(T(X, 216, '(9, 2): 64 to C₁, 52 to C₂', 13, 'start', LV)); o.append(T(X, 236, '→ joins C₂', 13, 'start', LV))
    o.append(T(X, 272, 'SSE: 111 → 78.75', 14, 'start', bold=True))
    o.append(T(X, 294, 'next pass: no point moves,', 13, 'start')); o.append(T(X, 312, 'so this is the answer', 13, 'start'))
    return 380, ''.join(o)
FIG[2] = (f2, 'Each point joins its nearer starting centroid; the two corner points (8, 1) and (9, 2) are close calls that split between the clusters. The centroids then move to the means (3, 2.5) and (6.25, 6.5), and SSE falls from 111 to 78.75.',
          'Scatter of eight points with dashed lines to their new centroids. Cluster 1: (1,2), (1,4), (2,3), (8,1) with mean (3, 2.5). Cluster 2: (5,8), (6,9), (5,7), (9,2) with mean (6.25, 6.5). Hollow squares mark the starting centroids (1,2) and (5,8).')


# ---- 4.3 the single-linkage dendrogram ----
def f3():
    o = [T(40, 24, 'Single-linkage dendrogram of four cities', 15, 'start', bold=True)]
    x0, y1 = 90, 300
    fy = lambda d: y1 - (d - 0) / 18 * (y1 - 60)
    o.append(L(x0, 60, x0, y1, L2, 1.5))
    for d in [0, 5, 10, 12, 15]:
        o.append(L(x0 - 5, fy(d), x0, fy(d), L2, 1.5)); o.append(T(x0 - 9, fy(d) + 4.5, str(d), 13, 'end', MUT))
    o.append(T(x0, 48, 'merge distance (km)', 13, 'start', MUT))
    xs = {'A': 150, 'B': 230, 'C': 330, 'D': 410}
    for n, x in xs.items():
        o.append(L(x, y1, x, fy(10 if n in 'AB' else 12), INK, 2.2))
        o.append(T(x, y1 + 22, n, 15, bold=True))
    o.append(L(150, fy(10), 230, fy(10), INK, 2.2)); o.append(L(330, fy(12), 410, fy(12), INK, 2.2))
    o.append(L(190, fy(10), 190, fy(15), INK, 2.2)); o.append(L(370, fy(12), 370, fy(15), INK, 2.2)); o.append(L(190, fy(15), 370, fy(15), INK, 2.2))
    for x, d in [(190, 10), (370, 12), (280, 15)]:
        o.append(C(x, fy(d), 5, AC)); o.append(Tb(x, fy(d) - 10, f'{d} km', 13, fill=AC, bold=True))
    o.append(L(x0, fy(13.5), 460, fy(13.5), LV, 2, dash='6 4')); o.append(Tb(x0 + 10, fy(13.5) - 8, 'cut at 13.5', 13, 'start', LV, True))
    X = 520
    o.append(T(X, 80, 'merges', 13, 'start', MUT))
    o.append(T(X, 104, '1. A–B at 10', 14, 'start')); o.append(T(X, 128, '2. C–D at 12', 14, 'start'))
    o.append(T(X, 152, '3. AB–CD at 15', 14, 'start'))
    o.append(T(X, 186, 'd(AB, C) = min(20, 15)', 13, 'start', MUT)); o.append(T(X, 204, '= 15', 13, 'start', MUT))
    o.append(T(X, 240, 'The cut crosses two', 13, 'start', LV)); o.append(T(X, 258, 'branches: {A, B} and', 13, 'start', LV))
    o.append(T(X, 276, '{C, D}', 13, 'start', LV))
    return 336, ''.join(o)
FIG[3] = (f3, 'A and B join first at 10 km, then C and D at 12 km, and the two pairs meet at 15 km, the shortest road between them (B–C). Cutting the tree anywhere between 12 and 15 km leaves two clusters, {A, B} and {C, D}.',
          'A dendrogram with leaves A, B, C, D. A and B join at height 10, C and D at 12, and the two pairs at 15. A dashed horizontal cut at 13.5 crosses two branches, giving clusters A B and C D.')


# ---- 4.4 one EM step for two Gaussians ----
def f4():
    o = [T(40, 24, 'One EM step: data 1, 2, 5, 6 and two Gaussians (σ² = 1, π = 0.5 each)', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 60, 520, 50, 200
    fx = lambda v: x0 + v / 7 * (x1 - x0)
    fy = lambda v: y1 - v * (y1 - y0)
    o.append(xaxis(x0, x1, y1, [0, 1, 2, 3, 4, 5, 6, 7], fx))
    g = lambda x, m: math.exp(-(x - m) ** 2 / 2)
    o.append(P([(fx(i / 20), fy(g(i / 20, 2))) for i in range(141)], AC, 2.5))
    o.append(P([(fx(i / 20), fy(g(i / 20, 5))) for i in range(141)], LV, 2.5))
    o.append(T(fx(2), y0 - 8, 'μ₁ = 2', 13, fill=AC, bold=True)); o.append(T(fx(5), y0 - 8, 'μ₂ = 5', 13, fill=LV, bold=True))
    for x in [1, 2, 5, 6]: o.append(C(fx(x), y1, 6, NX))
    # responsibilities as split bars under each point
    gam = {1: 0.99945, 2: 0.9890, 5: 0.0110, 6: 0.00055}
    yb = 252
    o.append(T(40, yb - 6, 'responsibility γ (share of each point given to each Gaussian)', 13, 'start', MUT))
    for i, x in enumerate([1, 2, 5, 6]):
        bx = 60 + i * 120; w = 100
        o.append(R(bx, yb + 4, w * gam[x], 22, ACS, AC, 3, 1.4)); o.append(R(bx + w * gam[x], yb + 4, w * (1 - gam[x]), 22, LVS, LV, 3, 1.4))
        o.append(T(bx + w / 2, yb + 44, f'x = {x}', 13, bold=True))
        o.append(T(bx + w / 2, yb + 62, f'γ₁ = {gam[x]:.4g}', 13, fill=AC if x < 4 else LV))
    o.append(T(560, 74, 'M-step means', 13, 'start', MUT))
    o.append(T(560, 98, 'μ₁: 2 → 1.5179', 14, 'start', AC, True)); o.append(T(560, 122, 'μ₂: 5 → 5.4821', 14, 'start', LV, True))
    o.append(T(560, 158, 'each mean moves', 13, 'start')); o.append(T(560, 176, 'toward the middle', 13, 'start'))
    o.append(T(560, 194, 'of its own points', 13, 'start'))
    o.append(L(fx(2), y0 + 30, fx(1.5179), y0 + 30, AC, 2, arrow='n')); o.append(L(fx(5), y0 + 30, fx(5.4821), y0 + 30, LV, 2, arrow='l'))
    o.append(T(40, 348, 'μ₁ = (0.99945·1 + 0.9890·2 + 0.0110·5 + 0.00055·6) ÷ 2.0000 = 1.5179', 13, 'start'))
    return 364, ''.join(o)
FIG[4] = (f4, 'Points 1 and 2 belong almost wholly to the first Gaussian and 5 and 6 to the second, as the responsibility bars show. Re-averaging with those weights moves μ₁ from 2 to 1.5179 and μ₂ from 5 to 5.4821.',
          'Two bell curves centred at 2 and 5 over an axis from 0 to 7 with data points at 1, 2, 5, 6. Under them, split bars give each point’s responsibility: about 1 for the first Gaussian at x = 1 and 2, about 0 at x = 5 and 6. Arrows show μ1 moving to 1.5179 and μ2 to 5.4821.')


# ---- 4.5 PCA on three points ----
def f5():
    o = [T(40, 24, 'PCA on (2, 0), (0, 2), (2, 2)', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 70, 370, 50, 350
    fx = lambda v: x0 + (v + 0.5) / 3 * (x1 - x0)
    fy = lambda v: y1 - (v + 0.5) / 3 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2], [0, 1, 2], fx, fy, 'x₁', 'x₂'))
    m = 4 / 3
    o.append(L(fx(m - 1.1), fy(m + 1.1), fx(m + 1.1), fy(m - 1.1), AC, 3))
    o.append(L(fx(m - 0.9), fy(m - 0.9), fx(m + 0.85), fy(m + 0.85), NX, 2, dash='6 4'))
    o.append(Tb(fx(m - 1.1) + 10, fy(m + 1.1) + 2, 'PC1, λ₁ = 2', 14, 'start', AC, True))
    o.append(Tb(fx(m + 0.62), fy(m + 0.85) - 2, 'PC2, λ₂ = 0.667', 13, 'end', NX, True))
    for (x, y) in [(2, 0), (0, 2)]:
        t = ((x - m) - (y - m)) / 2
        fxp, fyp = m + t, m - t
        o.append(L(fx(x), fy(y), fx(fxp), fy(fyp), L2, 1.5, dash='3 3'))
    o.append(L(fx(2), fy(2), fx(m), fy(m), L2, 1.5, dash='3 3'))
    for (x, y) in [(2, 0), (0, 2), (2, 2)]:
        o.append(C(fx(x), fy(y), 7, LV))
    o.append(sq(fx(m), fy(m), 11, INK)); o.append(Tb(fx(m) - 14, fy(m) + 20, 'mean (1.333, 1.333)', 13, 'end'))
    o.append(Tb(fx(2) + 12, fy(0) + 5, '(2, 0)', 13, 'start', LV, True)); o.append(Tb(fx(0), fy(2) + 26, '(0, 2)', 13, 'middle', LV, True))
    o.append(Tb(fx(2) + 12, fy(2) - 8, '(2, 2)', 13, 'start', LV, True))
    X = 400
    o.append(T(X, 70, 'Σ = [[1.333, −0.667], [−0.667, 1.333]]', 13, 'start'))
    o.append(T(X, 98, 'Σ(1, −1) = (2, −2) = 2·(1, −1)', 13, 'start', AC, True))
    o.append(T(X, 118, 'Σ(1, 1) = 0.667·(1, 1)', 13, 'start', NX, True))
    o.append(T(X, 150, 'PC1 = (1, −1)/√2 = (0.707, −0.707)', 14, 'start', AC, True))
    o.append(T(X, 186, 'projections on PC1:', 13, 'start', MUT))
    o.append(T(X, 208, '(2, 0) → +1.414', 14, 'start')); o.append(T(X, 230, '(0, 2) → −1.414', 14, 'start'))
    o.append(T(X, 252, '(2, 2) → 0  (its foot is the mean)', 14, 'start'))
    o.append(T(X, 288, 'check: (1.414² + 1.414² + 0) ÷ 2', 13, 'start', MUT))
    o.append(T(X, 306, '= 2.0 = λ₁', 13, 'start', MUT))
    return 396, ''.join(o)
FIG[5] = (f5, 'The data spread most along the direction (1, −1), from (0, 2) to (2, 0), so that is PC1 with variance λ₁ = 2. Dropping perpendiculars onto PC1 gives the projections 1.414, −1.414 and 0.',
          'Scatter of (2,0), (0,2), (2,2) with the mean (1.333, 1.333). A solid line through the mean along direction (1,−1) is PC1; a dashed line along (1,1) is PC2. Dashed perpendiculars drop the points onto PC1 at +1.414, −1.414 and 0.')


# ---- 4.6 the correlation filter ----
def f6():
    o = [T(40, 24, 'Filter selection: keep a feature if |r| with Y is at least 0.6', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 520, 66, 290
    fy = lambda v: y1 - v * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in [0, 0.2, 0.4, 0.6, 0.8, 1.0]:
        o.append(L(x0, fy(v), x1, fy(v), LN, 1)); o.append(T(x0 - 8, fy(v) + 4.5, f'{v:.1f}', 13, 'end', MUT))
    o.append(T(x0, y0 - 14, '|r| with Y', 13, 'start', MUT))
    r = [('F1', 0.45), ('F2', 0.78), ('F3', 0.30), ('F4', 0.62), ('F5', 0.20)]
    for i, (n, v) in enumerate(r):
        bx = 110 + i * 84
        keep = v >= 0.6
        o.append(R(bx, fy(v), 50, y1 - fy(v), ACS if keep else PANEL, AC if keep else L2, 3, 2 if keep else 1.4))
        o.append(T(bx + 25, fy(v) - 8, f'{v:.2f}', 13, bold=keep, fill=AC if keep else INK))
        o.append(T(bx + 25, y1 + 22, n, 14, bold=True))
        o.append(T(bx + 25, y1 + 42, 'keep' if keep else 'drop', 13, bold=keep, fill=AC if keep else MUT))
    o.append(L(x0, fy(0.6), x1, fy(0.6), LV, 2, dash='6 4')); o.append(T(x1 + 6, fy(0.6) + 5, 'cut-off 0.6', 13, 'start', LV, True))
    o.append(T(560, 206, 'kept: F2, F4', 14, 'start', AC, True)); o.append(T(560, 228, '2 of 5 features', 13, 'start'))
    o.append(T(560, 264, 'A filter looks at', 13, 'start', MUT)); o.append(T(560, 282, 'each feature alone,', 13, 'start', MUT))
    o.append(T(560, 300, 'before any model.', 13, 'start', MUT))
    return 350, ''.join(o)
FIG[6] = (f6, 'Each bar is one feature’s absolute correlation with the target. Only F2 (0.78) and F4 (0.62) reach the 0.6 cut-off, so the filter keeps two of the five features.',
          'Bar chart of absolute correlation with Y: F1 0.45, F2 0.78, F3 0.30, F4 0.62, F5 0.20, with a dashed cut-off line at 0.6. F2 and F4 are highlighted as kept; the other three are dropped.')


# ---- 4.7 LDA projects onto (1,1)/√2 ----
def f7():
    o = [T(40, 24, 'LDA: project both classes onto w = (1, 1)/√2', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 70, 340, 56, 326
    fx = lambda v: x0 + v / 7 * (x1 - x0)
    fy = lambda v: y1 - v / 7 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], fx, fy, 'x₁', 'x₂'))
    o.append(L(fx(0), fy(0), fx(6.6), fy(6.6), NX, 2.2, arrow='x'))
    o.append(Tb(fx(6.4) - 8, fy(6.6) + 4, 'w', 14, 'end', NX, True))
    pts = [((1, 2), 'A', AC), ((2, 3), 'A', AC), ((4, 5), 'B', LV), ((5, 6), 'B', LV)]
    for (x, y), c, col in pts:
        t = (x + y) / 2
        o.append(L(fx(x), fy(y), fx(t), fy(t), col, 1.4, dash='3 3'))
        o.append(C(fx(t), fy(t), 4, col))
        o.append(C(fx(x), fy(y), 7, col))
        o.append(Tb(fx(x) - 10, fy(y) - 8, f'({x}, {y})', 13, 'end', col, True))
    # 1-D number line of projections
    lx0, lx1, ly = 400, 690, 200
    fz = lambda v: lx0 + v / 9 * (lx1 - lx0)
    o.append(T(lx0, 120, 'projected values w·x', 14, 'start', bold=True))
    o.append(L(lx0, ly, lx1, ly, L2, 2))
    for v in [0, 3, 6, 9]:
        o.append(L(fz(v), ly, fz(v), ly + 6, L2, 1.5)); o.append(T(fz(v), ly + 24, str(v), 13, fill=MUT))
    for v, col in [(2.12, AC), (3.54, AC), (6.36, LV), (7.78, LV)]:
        o.append(C(fz(v), ly, 7, col)); o.append(T(fz(v), ly - 14, f'{v}', 13, fill=col, bold=True))
    o.append(brace(fz(3.54) + 8, fz(6.36) - 8, ly + 40, INK, up=True))
    o.append(T((fz(3.54) + fz(6.36)) / 2, ly + 60, 'empty gap', 13, fill=MUT))
    o.append(T(lx0, 296, 'class A: 2.12, 3.54', 14, 'start', AC, True)); o.append(T(lx0, 318, 'class B: 6.36, 7.78', 14, 'start', LV, True))
    o.append(T(lx0, 352, 'One threshold on this line separates them.', 13, 'start'))
    return 380, ''.join(o)
FIG[7] = (f7, 'Each point drops onto the line along w = (1, 1)/√2, the direction joining the two class means. On that line class A lands at 2.12 and 3.54 and class B at 6.36 and 7.78, with an empty gap between them.',
          'Left: class A points (1,2), (2,3) and class B points (4,5), (5,6) with dashed drops onto the diagonal direction w. Right: a number line of the projections 2.12 and 3.54 for class A and 6.36 and 7.78 for class B, with an empty gap between.')


# ---- 4.8 silhouette of two tight clusters ----
def f8():
    o = [T(40, 24, 'Silhouette s = (b − a) ÷ max(a, b) for each point', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 70, 360, 66, 336
    fx = lambda v: x0 + (v + 0.5) / 7 * (x1 - x0)
    fy = lambda v: y1 - (v + 0.5) / 7 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6], [0, 2, 4, 6], fx, fy, 'x', 'y'))
    A = [('A', 0, 0, '0.868'), ('B', 1, 0, '0.825'), ('C', 0, 1, '0.825')]
    B = [('D', 5, 5, '0.868'), ('E', 6, 5, '0.825'), ('F', 5, 6, '0.825')]
    for grp, col, f in [(A, AC, ACS), (B, LV, LVS)]:
        cx = sum(p[1] for p in grp) / 3; cy = sum(p[2] for p in grp) / 3
        o.append(f'<circle cx="{fx(cx):.1f}" cy="{fy(cy):.1f}" r="38" style="fill:{f};stroke:{col};stroke-width:1.5;stroke-dasharray:5 4"/>')
        for n, x, y, s in grp:
            o.append(C(fx(x), fy(y), 7, col))
    lab = {'A': (-12, 18, 'end'), 'B': (12, 18, 'start'), 'C': (-12, -10, 'end'), 'D': (-12, 18, 'end'), 'E': (12, 18, 'start'), 'F': (-12, -10, 'end')}
    for n, x, y, s in A + B:
        dx, dy, a = lab[n]
        o.append(Tb(fx(x) + dx, fy(y) + dy, f'{n} {s}', 13, a, AC if n in 'ABC' else LV, True))
    X = 440
    o.append(T(X, 70, 'point A', 14, 'start', bold=True))
    o.append(T(X, 94, 'a = mean distance inside its', 13, 'start')); o.append(T(X, 112, 'cluster = (1 + 1) ÷ 2 = 1', 13, 'start'))
    o.append(T(X, 138, 'b = mean distance to D, E, F', 13, 'start')); o.append(T(X, 156, '= (7.071 + 7.810 + 7.810) ÷ 3', 13, 'start'))
    o.append(T(X, 174, '= 7.564', 13, 'start'))
    o.append(T(X, 200, 's = (7.564 − 1) ÷ 7.564 = 0.868', 14, 'start', AC, True))
    o.append(T(X, 244, 'average over six points', 13, 'start', MUT))
    o.append(T(X, 266, '(2 × 0.868 + 4 × 0.825) ÷ 6', 14, 'start'))
    o.append(T(X, 288, '= 0.839', 15, 'start', bold=True))
    o.append(T(X, 314, 'near 1: compact and far apart', 13, 'start', MUT))
    return 384, ''.join(o)
FIG[8] = (f8, 'Each point is about 1 unit from its own cluster-mates but more than 6 units from the other cluster, so every silhouette is high: 0.868 for the corner points A and D, 0.825 for the rest, 0.839 on average.',
          'Scatter of two tight clusters: A (0,0), B (1,0), C (0,1) and D (5,5), E (6,5), F (5,6), each point labelled with its silhouette, 0.868 for A and D and 0.825 for the others. Side working for point A gives a = 1, b = 7.564, s = 0.868, and the average 0.839.')


# ---- 4.9 fuzzy memberships of four customers ----
def f9():
    o = [T(40, 24, 'Fuzzy C-means, K = 2, m = 2: memberships after one pass', 15, 'start', bold=True)]
    fx = lambda v: 80 + (v - 50) / 350 * 560
    y = 210
    o.append(L(fx(50), y, fx(400), y, L2, 2))
    for v in [100, 150, 200, 250, 300, 350]:
        o.append(L(fx(v), y, fx(v), y + 6, L2, 1.5)); o.append(T(fx(v), y + 24, f'₹{v}', 13, fill=MUT))
    u = {100: 1.0, 150: 0.941, 300: 0.0588, 350: 0.0}
    H = 110
    for v, u1 in u.items():
        bx = fx(v) - 20
        o.append(R(bx, y - 18 - H, 40, H * (1 - u1) if u1 < 1 else 0.01, LVS, LV, 3, 1.4))
        o.append(R(bx, y - 18 - H * u1, 40, H * u1 if u1 > 0 else 0.01, ACS, AC, 3, 1.4))
        o.append(C(fx(v), y, 6, NX))
        o.append(T(fx(v), y - 24 - H, f'u₁ = {u1:g}', 13, fill=AC, bold=True))
    o.append(sq(fx(100), y + 50, 12, AC, 'none')); o.append(sq(fx(123.8), y + 50, 12, AC))
    o.append(L(fx(100) + 8, y + 50, fx(123.8) - 9, y + 50, AC, 1.8, arrow='n'))
    o.append(T(fx(123.8) + 12, y + 55, 'c₁: 100 → 123.8', 13, 'start', AC, True))
    o.append(sq(fx(350), y + 50, 12, LV, 'none')); o.append(sq(fx(326.2), y + 50, 12, LV))
    o.append(L(fx(350) - 8, y + 50, fx(326.2) + 9, y + 50, LV, 1.8, arrow='l'))
    o.append(T(fx(326.2) - 12, y + 55, 'c₂: 350 → 326.2', 13, 'end', LV, True))
    o.append(R(400, 44, 16, 14, ACS, AC, 3, 1.4)); o.append(T(422, 56, 'share in c₁', 13, 'start'))
    o.append(R(530, 44, 16, 14, LVS, LV, 3, 1.4)); o.append(T(552, 56, 'share in c₂', 13, 'start'))
    o.append(T(40, y + 92, '₹150: u₁ = 1 ÷ ((50/50)² + (50/200)²) = 1 ÷ 1.0625 = 0.941. Each centroid is a u²-weighted mean,', 13, 'start'))
    o.append(T(40, y + 112, 'so the near-boundary customers pull both centroids inward a little.', 13, 'start'))
    return y + 128, ''.join(o)
FIG[9] = (f9, 'Each customer splits one unit of membership between the two clusters: ₹150 is 0.941 in c₁ and ₹300 is 0.0588. Weighting by u² moves c₁ from 100 to 123.8 and c₂ from 350 to 326.2.',
          'A line of four customers at 100, 150, 300 and 350 rupees, each with a stacked bar showing its membership in cluster 1 and cluster 2: 1, 0.941, 0.0588 and 0 in cluster 1. Below, the centroids move from 100 to 123.8 and from 350 to 326.2.')


spec = make_spec(FIG)

TEXT = {
    2: [('After three iterations the SSE drops to 30, as shown in the figure.',
         'A second pass changes no assignment, so the algorithm has converged; the SSE fell from 111 with the starting centroids to 78.75. Figure 4.2.1 shows the assignments and the moved centroids.')],
}


def text_fixes(k):
    return TEXT.get(k, [])


def chapter_fix(k, ch):
    """4.5: the first principal component of (2,0), (0,2), (2,2) is (1,−1)/√2, not (1,1)/√2."""
    if k != 5:
        return ch
    e = ch['examples'][0]
    if e['answer'].startswith('The three projected values on PC1 are 1.414'):
        return ch  # already corrected on this branch
    old3 = 'Eigenvector for λ₁ is v₁ = (1,1)/√2 ≈ (0.707, 0.707). Eigenvector for λ₂ is v₂ = (1,-1)/√2 ≈ (0.707, -0.707).'
    assert old3 in e['steps'][3], 'c-ml-u4 4.5 step 4 changed'
    e['steps'][3] = e['steps'][3].replace(old3, 'Σ(1,-1) = (1.333 + 0.667, −0.667 − 1.333) = (2, −2), so the eigenvector for λ₁ = 2 is v₁ = (1,-1)/√2 ≈ (0.707, -0.707). Σ(1,1) = (0.667, 0.667), so the eigenvector for λ₂ ≈ 0.666 is v₂ = (1,1)/√2 ≈ (0.707, 0.707).')
    e['steps'][4] = 'Projection of each centered point p onto v₁:  p·v₁ = (0.667·0.707) + (−1.333·−0.707) = 1.414;  (−1.333·0.707) + (0.667·−0.707) = −1.414;  (0.667·0.707) + (0.667·−0.707) = 0.'
    e['steps'].append('Check: the variance of the projections is (1.414² + 1.414² + 0²) ÷ 2 = 2.0, which equals λ₁.')
    e['answer'] = 'The three projected values on PC1 are 1.414, –1.414 and 0 (rounded to three decimals).'
    c = e['code']['code']
    a = '// first principal component direction (1,1)/sqrt(2)\n    double v[2] = {1.0/sqrt(2.0), 1.0/sqrt(2.0)};'
    assert a in c, 'c-ml-u4 4.5 code changed'
    e['code']['code'] = c.replace(a, '// first principal component direction (1,-1)/sqrt(2)\n    double v[2] = {1.0/sqrt(2.0), -1.0/sqrt(2.0)};')
    e['dry_run']['rows'] = [['0', '1.414'], ['1', '-1.414'], ['2', '0.000']]
    e['output'] = '1.414\n-1.414\n0.000'
    return ch
