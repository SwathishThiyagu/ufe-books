"""Claude's hand-drawn figures for c-data-u4 (Data Science, unit 4: inferential statistics), one per chapter, from each
chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARR = {AC: 'n', L2: 'm', LV: 'l', NX: 'x', MUT: 'm', INK: 'm'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=ARR[c])


def curve(f, a, b, fx, fy, n=160):
    return [(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)]


def area(f, a, b, fx, fy, base, fill, op):
    pts = [(fx(a), base)] + curve(f, a, b, fx, fy, 60) + [(fx(b), base)]
    return P(pts, 'none', 0, None, fill, op)


phi = lambda z: math.exp(-z * z / 2)


# ---- 4.1 stratified and systematic samples ----
def f1():
    years = [('1st', 480, 24), ('2nd', 360, 18), ('3rd', 240, 12), ('4th', 120, 6)]
    fills = [(ACS, AC), (NXS, NX), (LVS, LV), (PANEL, L2)]
    x0, W = 140, 560
    o = [T(x0 - 12, 66, 'population', 14, 'end', INK, True), T(x0 - 12, 82, '1,200', 13, 'end', MUT),
         T(x0 - 12, 166, 'sample', 14, 'end', INK, True), T(x0 - 12, 182, '60', 13, 'end', MUT)]
    x = x0
    for (nm, N, n), (f, st) in zip(years, fills):
        w = N / 1200 * W
        o += [R(x, 50, w, 40, f, st, 0, 1.5), T(x + w / 2, 75, f'{nm}: {N}', 14 if N > 120 else 13, bold=True),
              R(x, 150, w, 40, f, st, 0, 1.5), T(x + w / 2, 175, str(n), 15, fill=st if st != L2 else INK, bold=True),
              L(x + w / 2, 92, x + w / 2, 146, st, 1.5, '4 3'), Tb(x + w / 2, 124, '÷ 20', 13, fill=MUT)]
        x += w
    o.append(T(x0, 30, 'proportional stratified allocation: nₕ = 60 × Nₕ ÷ 1,200 = Nₕ ÷ 20', 14, 'start', AC, True))
    o.append(T(20, 236, 'systematic: k = 1,200 ÷ 60 = 20, random start 7', 14, 'start', NX, True))
    fx = lambda r: 40 + (r - 1) * 640 / 1199
    o.append(L(fx(1), 268, fx(1200), 268, L2, 1.5))
    for j in range(60):
        r = 7 + 20 * j
        o.append(L(fx(r), 260, fx(r), 276, NX, 1.5))
    o += [T(fx(1), 294, '1', 13, fill=MUT), T(fx(1200), 294, '1,200', 13, fill=MUT),
          T(46, 254, '7, 27, 47, 67, …', 13, 'start', NX, True), T(fx(1187), 254, '60th: 7 + 59 × 20 = 1,187', 13, 'end', NX, True)]
    o.append(T(20, 330, 'Estimate: p̂ = 21 ÷ 60 = 0.35, about 0.35 × 1,200 = 420 students.', 14, 'start', INK, True))
    return 344, ''.join(o)


FIG[1] = (f1, 'Each year group gets the same share of the sample as of the college: 480, 360, 240 and 120 students give 24, 18, 12 and 6. A systematic sample takes every 20th roll number from 7 to 1,187.',
          'Two stacked bars of equal length: the population split into 480, 360, 240 and 120 students by year, and the sample of 60 split into 24, 18, 12 and 6. Below, a roll-number line from 1 to 1,200 with 60 ticks every 20 starting at 7.')


# ---- 4.2 the sampling distribution of the mean ----
def f2():
    fx = lambda v: 60 + (v - 28) * 80
    base = 220
    fy = lambda h: base - 160 * h
    f = lambda v: phi(v - 32)
    o = [area(f, 31, 33, fx, fy, base, AC, 0.25), area(f, 34, 36, fx, fy, base, LV, 0.45), P(curve(f, 28, 36, fx, fy), INK, 2.5)]
    o += [L(fx(32), fy(1), fx(32), base, MUT, 1.5, '4 4'), T(fx(32), fy(1) - 8, 'μ = 32, SE = 8 ÷ √64 = 1', 14, fill=INK, bold=True)]
    o += [T(fx(32), 160, '31 to 33', 13, fill=AC, bold=True), T(fx(32), 178, '0.6826', 15, fill=AC, bold=True),
          T(fx(34.9), 160, 'x̄ > 34', 13, fill=LV, bold=True), T(fx(34.9), 178, '0.0228', 15, fill=LV, bold=True), ar(fx(34.9), 184, fx(34.4), 208, LV, 1.5)]
    o.append(xaxis(fx(28), fx(36), base, range(28, 37), fx, 'sample mean x̄ (minutes)'))
    o.append(T(20, 296, 'after new routing: x̄ = 30.5, 95% CI = 30.5 ± 1.96 × 1', 14, 'start', NX, True))
    o += [L(fx(28.54), 318, fx(32.46), 318, NX, 4), L(fx(28.54), 308, fx(28.54), 328, NX, 2), L(fx(32.46), 308, fx(32.46), 328, NX, 2),
          C(fx(30.5), 318, 6, NX), T(fx(28.54), 346, '28.54', 13, fill=NX, bold=True), T(fx(32.46), 346, '32.46', 13, fill=NX, bold=True),
          L(fx(32), 304, fx(32), 332, INK, 2, '3 3'), T(fx(32) + 8, 304, '32 is inside', 13, 'start', INK)]
    o.append(T(20, 380, 'For a margin of 0.5 min: n = (1.96 × 8 ÷ 0.5)² = 983.4, so 984 orders.', 14, 'start'))
    return 394, ''.join(o)


FIG[2] = (f2, 'Means of 64 orders vary around 32 with standard error 1: 68.26% fall between 31 and 33 and only 2.28% above 34. The interval 28.54 to 32.46 after the new routing still holds 32.',
          'A bell curve of the sample mean centred on 32 with SE 1, the band 31 to 33 shaded blue (0.6826) and the tail above 34 shaded orange (0.0228). Below, a green interval from 28.54 to 32.46 around 30.5, with a dashed mark at 32 inside it.')


# ---- 4.3 the Poisson log-likelihood ----
def f3():
    data = [2, 0, 3, 1, 2, 4]
    lf = sum(math.log(math.factorial(x)) for x in data)
    ll = lambda l: -6 * l + 12 * math.log(l) - lf
    x0, x1, y0, y1 = 80, 450, 40, 260
    fx = lambda l: x0 + (l - 0.5) * (x1 - x0) / 3.5
    fy = lambda v: y1 - (v + 18) * (y1 - y0) / 9
    o = [axes(x0, x1, y0, y1, [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4], [-18, -16, -14, -12, -10], fx, fy, 'λ, outages a day', 'log-likelihood ℓ(λ)',
              xfmt=lambda v: f'{v:g}', yfmt=neg)]
    o.append(P(curve(ll, 0.5, 4, fx, fy), AC, 2.5))
    for l, s in [(1.5, '−10.49'), (2.0, '−10.04'), (2.5, '−10.36')]:
        o.append(C(fx(l), fy(ll(l)), 5.5, NX if l == 2 else AC))
        o.append(T(fx(l) + (0 if l == 2 else (-8 if l < 2 else 8)), fy(ll(l)) + (-12 if l == 2 else 22), s, 13, 'middle' if l == 2 else ('end' if l < 2 else 'start'), NX if l == 2 else AC, True))
    o += [L(fx(2), fy(ll(2)) + 6, fx(2), y1, NX, 1.8, '5 4'), Tb(fx(2), y1 - 14, 'MLE λ = 2.0', 14, fill=NX, bold=True)]
    o.append(T(500, 50, 'outages on 6 days', 14, 'start', MUT, True))
    for i, x in enumerate(data):
        bx = 500 + i * 34
        o += [R(bx, 200 - x * 30, 26, x * 30 if x else 1, LVS, LV, 0, 1.5), T(bx + 13, 194 - x * 30, str(x), 13, fill=LV, bold=True),
              T(bx + 13, 218, f'd{i + 1}', 13, fill=MUT)]
    o.append(L(496, 200, 700, 200, L2, 1.5))
    o += [T(500, 248, 'MLE: λ = x̄ = 12 ÷ 6 = 2.0', 14, 'start', NX, True), T(500, 270, 'P(no outage) = e⁻² = 0.135', 14, 'start', INK, True)]
    o.append(T(20, 330, 'dℓ/dλ = −6 + 12 ÷ λ = 0 gives λ = 2, and the curve is highest there.', 14, 'start'))
    return 344, ''.join(o)


FIG[3] = (f3, 'The log-likelihood of the six days\' outages peaks at λ = 2.0, the sample mean: ℓ is −10.04 there against −10.49 at 1.5 and −10.36 at 2.5. Then P(no outage) = e⁻² = 0.135.',
          'A curve of log-likelihood against λ from 0.5 to 4, highest at λ = 2.0 with value −10.04; points at 1.5 and 2.5 are lower. Beside it, bars of the daily outages 2, 0, 3, 1, 2, 4 and the results λ-hat = 2.0 and P(no outage) = 0.135.')


# ---- 4.4 two-tailed z-test ----
def f4():
    fx = lambda z: 360 + z * 90
    base = 230
    fy = lambda h: base - 170 * h
    o = [area(phi, 1.96, 3.6, fx, fy, base, LV, 0.25), area(phi, -3.6, -1.96, fx, fy, base, LV, 0.25),
         area(phi, 2.4, 3.6, fx, fy, base, LV, 0.6), area(phi, -3.6, -2.4, fx, fy, base, LV, 0.6), P(curve(phi, -3.6, 3.6, fx, fy), INK, 2.5)]
    o += [L(fx(2.4), 70, fx(2.4), base, AC, 2.5), T(fx(2.4), 62, 'z = 2.40', 14, fill=AC, bold=True),
          L(fx(2.576), 100, fx(2.576), base, NX, 1.8, '5 4'), T(fx(2.576) + 6, 108, '2.576 (α = 0.01)', 13, 'start', NX, True)]
    o += [T(fx(-2.6), 160, 'reject', 13, fill=LV, bold=True), T(fx(2.9), 160, 'reject', 13, fill=LV, bold=True),
          T(fx(0), 150, 'do not reject H₀', 14, fill=INK, bold=True), T(fx(0), 170, '95% of the area', 13, fill=MUT)]
    o.append(xaxis(fx(-3.6), fx(3.6), base, [-3, -1.96, 0, 1.96, 3], fx, 'z', fmt=lambda v: neg(f'{v:g}')))
    o.append(T(20, 304, 'SE = 10 ÷ √25 = 2 g, so z = (504.8 − 500) ÷ 2 = 2.40.  p = 2 × 0.0082 = 0.0164.', 14, 'start'))
    o.append(T(20, 328, 'At α = 0.05: 2.40 > 1.96, reject H₀.  At α = 0.01: 2.40 < 2.576, do not reject.', 14, 'start', LV, True))
    return 342, ''.join(o)


FIG[4] = (f4, 'Under H₀ the statistic z follows the standard normal curve. The observed 2.40 lies beyond 1.96, so H₀ is rejected at the 5% level, but not beyond 2.576, so it stands at 1%.',
          'A standard normal curve with light orange rejection tails beyond ±1.96 and darker tails beyond ±2.40 for the p-value. A blue line marks z = 2.40 and a dashed green line marks 2.576 for α = 0.01.')


# ---- 4.5 one-sample t-test on battery life ----
def f5():
    vals = [9.2, 9.8, 10.1, 9.5, 9.0, 9.7, 9.9, 9.4, 9.6, 9.3]
    fx = lambda v: 80 + (v - 8.9) * 400
    o = [T(20, 26, 'battery life of 10 phones (hours)', 14, 'start', MUT, True)]
    o.append(xaxis(fx(8.9), fx(10.2), 110, [9.0, 9.2, 9.4, 9.6, 9.8, 10.0, 10.2], fx, None, lambda v: f'{v:.1f}'))
    for v in vals: o.append(C(fx(v), 96, 6, NX))
    o += [L(fx(10), 40, fx(10), 110, LV, 2, '6 4'), T(fx(10) + 6, 48, 'claim 10', 13, 'start', LV, True),
          L(fx(9.55), 80, fx(9.55), 110, AC, 2.5), T(fx(9.55), 48, 'x̄ = 9.55', 13, fill=AC, bold=True)]
    o += [L(fx(9.31), 72, fx(9.79), 72, AC, 4), L(fx(9.31), 64, fx(9.31), 80, AC, 2), L(fx(9.79), 64, fx(9.79), 80, AC, 2),
          Tb(fx(9.55), 66, '95% CI 9.31 to 9.79', 13, fill=AC, bold=True)]
    gx = lambda t: 360 + t * 60
    yb = 250
    tpdf = lambda t: (1 + t * t / 9) ** -5
    gy = lambda h: yb - 70 * h
    o += [area(tpdf, -5.2, -1.833, gx, gy, yb, LV, 0.3), P(curve(tpdf, -5.2, 5.2, gx, gy), INK, 2)]
    o.append(xaxis(gx(-5.2), gx(5.2), yb, [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], gx, 't with 9 degrees of freedom', neg))
    o += [L(gx(-1.833), 170, gx(-1.833), yb, LV, 1.8, '5 4'), T(gx(-1.833) + 4, 166, 'critical −1.833', 13, 'start', LV, True),
          L(gx(-4.22), 196, gx(-4.22), yb, AC, 2.5), T(gx(-4.22), 190, 't = −4.22', 14, fill=AC, bold=True)]
    o.append(T(20, 326, 's = 0.3375, SE = 0.3375 ÷ √10 = 0.1067, t = (9.55 − 10) ÷ 0.1067 = −4.22 < −1.833: reject H₀.', 14, 'start', INK, True))
    return 340, ''.join(o)


FIG[5] = (f5, 'The ten phones average 9.55 hours and their 95% interval, 9.31 to 9.79, stays below the claimed 10. On the t curve with 9 degrees of freedom, t = −4.22 lies far past the critical −1.833.',
          'Top: ten dots of battery life between 9.0 and 10.1 hours, a blue line at the mean 9.55, a blue interval 9.31 to 9.79 and a dashed orange line at the claim 10. Bottom: a t curve with 9 degrees of freedom, the left tail beyond −1.833 shaded, and t = −4.22 marked further left.')


# ---- 4.6 chi-square: observed against expected ----
def f6():
    cells = [('Under 30', 'UPI', 60, 50, '2.000'), ('Under 30', 'Card', 25, 30, '0.833'), ('Under 30', 'Cash', 15, 20, '1.250'),
             ('30 and over', 'UPI', 40, 50, '2.000'), ('30 and over', 'Card', 35, 30, '0.833'), ('30 and over', 'Cash', 25, 20, '1.250')]
    y1 = 230
    fy = lambda v: y1 - v * 2.6
    o = [L(40, y1, 700, y1, L2, 1.5)]
    for v in (0, 20, 40, 60):
        o += [L(40, fy(v), 700, fy(v), LN, 1), T(34, fy(v) + 4.5, str(v), 13, 'end', MUT)]
    for i, (g, m, ob, ex, c) in enumerate(cells):
        x = 70 + i * 104 + (20 if i >= 3 else 0)
        o += [R(x, fy(ob), 30, y1 - fy(ob), ACS if ob > ex else LVS, AC if ob > ex else LV, 0, 1.5),
              R(x + 34, fy(ex), 30, y1 - fy(ex), 'none', MUT, 0, 1.5, '4 3'),
              T(x + 15, fy(ob) - 6, str(ob), 13, fill=AC if ob > ex else LV, bold=True), T(x + 49, fy(ex) - 6, str(ex), 13, fill=MUT),
              T(x + 32, y1 + 20, m, 13, bold=True), T(x + 32, y1 + 38, c, 13, fill=MUT)]
    o += [T(206, 294, 'under 30', 14, fill=INK, bold=True), T(538, 294, '30 and over', 14, fill=INK, bold=True),
          brace(70, 342, 274, INK, up=True), brace(402, 674, 274, INK, up=True)]
    o += [R(470, 20, 14, 14, ACS, AC, 0, 1.5), T(490, 32, 'observed', 13, 'start'), R(570, 20, 14, 14, 'none', MUT, 0, 1.5, '4 3'), T(590, 32, 'expected', 13, 'start')]
    o.append(T(20, 330, 'χ² = 2 × (2.000 + 0.833 + 1.250) = 8.17 > 5.991 (df 2): reject independence, p = 0.017.', 14, 'start', INK, True))
    o.append(T(20, 352, 'Small numbers under the bars are each cell\'s (O − E)² ÷ E. Cramér\'s V = 0.20, a modest link.', 13, 'start', MUT))
    return 366, ''.join(o)


FIG[6] = (f6, 'Each cell\'s observed count beside the count expected if payment and age were independent. Younger shoppers use UPI more and cash less; the six gaps add up to χ² = 8.17, past 5.991.',
          'Paired bars for six cells: under 30 UPI 60 against 50, card 25 against 30, cash 15 against 20; 30 and over UPI 40 against 50, card 35 against 30, cash 25 against 20. Each pair has its contribution 2.000, 0.833 or 1.250 below.')


# ---- 4.7 one-way ANOVA ----
def f7():
    G = [('A notes', [5, 7, 6, 8, 4], 6, AC), ('B past papers', [8, 9, 7, 10, 11], 9, NX), ('C videos', [6, 5, 7, 4, 8], 6, LV)]
    x0, x1, y0, y1 = 70, 420, 30, 270
    fy = lambda v: y1 - (v - 3) * (y1 - y0) / 9
    o = [L(x0, y0, x0, y1, L2, 1.5), L(x0, y1, x1, y1, L2, 1.5)]
    for v in (3, 6, 9, 12):
        o += [L(x0 - 5, fy(v), x0, fy(v), L2, 1.5), T(x0 - 9, fy(v) + 4.5, str(v), 13, 'end', MUT)]
    o.append(L(x0, fy(7), x1, fy(7), INK, 1.8, '6 4'))
    o.append(T(x1 + 4, fy(7) + 5, 'grand 7', 13, 'start', INK, True))
    for g, (nm, vs, m, c) in enumerate(G):
        cx = x0 + 60 + g * 115
        o += [L(cx - 34, fy(m), cx + 34, fy(m), c, 3.5), T(cx, y1 + 20, nm, 13, fill=c, bold=True)]
        for k, v in enumerate(vs):
            px = cx - 20 + k * 10
            o += [L(px, fy(v), px, fy(m), c, 1, '2 2'), C(px, fy(v), 5, c)]
        o.append(T(cx + 40, fy(m) + 5, f'mean {m}', 13, 'start', c, True) if g < 2 else T(cx + 40, fy(m) + 18, f'mean {m}', 13, 'start', c, True))
    rows = [('source', 'SS', 'df', 'MS'), ('between', '30', '2', '15'), ('within', '30', '12', '2.5'), ('total', '60', '14', '')]
    for i, r in enumerate(rows):
        for j, (s, w) in enumerate(zip(r, [80, 46, 40, 50])):
            x = 494 + sum([80, 46, 40, 50][:j])
            o += [R(x, 40 + i * 30, w, 30, PANEL if i == 0 else 'var(--fig)', L2, 0, 1.2), T(x + w / 2, 60 + i * 30, s, 13, bold=i == 0)]
    o.append(boxt(494, 172, 216, 60, ['F = 15 ÷ 2.5 = 6.00', '> 3.885: reject H₀'], NXS, NX, 14, True))
    o.append(T(20, 324, 'SSB = 5 × (1 + 4 + 1) = 30 from the spread of the means; SSW = 10 + 10 + 10 = 30 inside the groups.', 13, 'start'))
    o.append(T(20, 346, 'Past papers (mean 9) stand out; η² = 30 ÷ 60 = 0.50.', 14, 'start', NX, True))
    return 360, ''.join(o)


FIG[7] = (f7, 'Quiz scores of the three groups with their means 6, 9 and 6 and the grand mean 7. The means spread as much as the scores inside groups (30 each), so F = 15 ÷ 2.5 = 6.00, past 3.885.',
          'Three groups of five dots: A notes and C videos around a mean of 6, B past papers around 9, with dotted lines from each dot to its group mean and a dashed grand mean at 7. A small ANOVA table gives SS 30, 30, 60 and a box gives F = 6.00 > 3.885.')

spec = make_spec(FIG)
