"""Claude's hand-drawn figures for c-data-u3 (Data Science, unit 3: descriptive statistics and visualisation), one per
chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARR = {AC: 'n', L2: 'm', LV: 'l', NX: 'x', MUT: 'm', INK: 'm'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=ARR[c])


def sq(x, y, c, filled=True, s=11):
    return f'<rect x="{x - s / 2:.1f}" y="{y - s / 2:.1f}" width="{s}" height="{s}" style="fill:{c if filled else PANEL};stroke:{c};stroke-width:2"/>'


def vtext(x, y, s, size=13, c=MUT):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="middle" transform="rotate(-90 {x} {y})" style="fill:{c}">{s}</text>'


# ---- 3.1 histogram and ogive of 25 marks ----
def f1():
    f = [1, 3, 6, 9, 4, 2]
    x0, x1, y0, y1 = 60, 330, 50, 250
    fx = lambda v: x0 + (v - 30) * (x1 - x0) / 60
    fy = lambda v: y1 - v * 20
    o = [T(x0, 30, 'histogram', 14, 'start', AC, True), axes(x0, x1, y0, y1, range(30, 100, 10), [0, 3, 6, 9], fx, fy, 'marks', '')]
    o.append(vtext(26, 150, 'students'))
    for i, n in enumerate(f):
        a = 30 + 10 * i
        o += [R(fx(a), fy(n), fx(a + 10) - fx(a), y1 - fy(n), ACS if i != 3 else NXS, AC if i != 3 else NX, 0, 1.5),
              T((fx(a) + fx(a + 10)) / 2, fy(n) - 6, str(n), 14, fill=AC if i != 3 else NX, bold=True)]
    X0, X1 = 420, 690
    gx = lambda v: X0 + (v - 30) * (X1 - X0) / 60
    gy = lambda c: y1 - c * 8
    o += [T(X0, 30, 'less-than ogive', 14, 'start', LV, True), axes(X0, X1, y0, y1, range(30, 100, 10), [0, 5, 10, 15, 20, 25], gx, gy, 'upper class boundary', '')]
    cum = [0, 1, 4, 10, 19, 23, 25]
    pts = [(gx(30 + 10 * i), gy(c)) for i, c in enumerate(cum)]
    o.append(P(pts, LV, 2.5))
    for p in pts: o.append(C(*p, 4.5, LV))
    o += [L(X0, gy(12.5), gx(62.8), gy(12.5), NX, 1.8, '5 4'), L(gx(62.8), gy(12.5), gx(62.8), y1, NX, 1.8, '5 4'),
          T(X0 + 6, gy(12.5) - 8, 'n/2 = 12.5', 13, 'start', NX, True), Tb(gx(62.8) + 6, y1 - 30, 'median ≈ 62.8', 13, 'start', NX, True)]
    o.append(T(20, 324, 'Median ≈ 60 + (12.5 − 10) ÷ 9 × 10 = 62.8 marks (the raw median is 62). One peak, at 60 to 70.', 14, 'start'))
    return 338, ''.join(o)


FIG[1] = (f1, 'The 25 marks in six classes of width 10: the histogram peaks at 60 to 70 with 9 students. On the ogive, the level n/2 = 12.5 meets the curve at about 62.8 marks, the median.',
          'Left: a histogram of marks with class frequencies 1, 3, 6, 9, 4, 2 for 30 to 90. Right: the cumulative ogive rising 0, 1, 4, 10, 19, 23, 25, with a dashed line from 12.5 across to the curve and down to 62.8.')


# ---- 3.2 delivery times: centre and spread ----
def f2():
    vals = [18, 22, 24, 25, 25, 27, 29, 31, 34, 36, 59]
    fx = lambda v: 60 + (v - 15) * 14
    ya = 214
    o = [xaxis(fx(15), fx(62), ya, [15, 20, 25, 30, 35, 40, 45, 50, 55, 60], fx, 'delivery time (minutes)')]
    seen = {}
    for v in vals:
        n = seen.get(v, 0); seen[v] = n + 1
        o.append(C(fx(v), ya - 14 - n * 14, 6, LV if v == 59 else NX))
    o.append(T(fx(59), ya - 28, '59', 13, fill=LV, bold=True))
    o += [R(fx(24), 126, fx(34) - fx(24), 34, ACS, AC, 2), T(fx(24) - 8, 148, 'middle half', 13, 'end', AC, True)]
    o += [brace(fx(19.05), fx(40.95), 92, MUT)]
    o += [L(fx(27), 48, fx(27), ya, AC, 2), T(fx(27) - 5, 46, 'median 27', 13, 'end', AC, True),
          L(fx(30), 48, fx(30), ya, LV, 2, '6 3'), T(fx(30) + 5, 46, 'mean 30', 13, 'start', LV, True),
          L(fx(49), 60, fx(49), ya, LV, 1.8, '5 4'), T(fx(49), 54, 'fence 49', 13, fill=LV, bold=True)]
    o += [Tb(fx(29), 118, 'IQR 24 to 34', 13, fill=AC, bold=True), Tb(fx(30), 84, 'mean ± s = 19.05 to 40.95', 13, fill=MUT, bold=True)]
    o.append(T(20, 282, 'The one late order (59) pulls the mean to 30, past the median 27 and the mode 25.', 14, 'start', LV, True))
    o.append(T(20, 306, 's = √(1198 ÷ 10) = 10.95 min, CV = 36.5%. 59 > 34 + 1.5 × 10 = 49, so report median 27 and IQR 10.', 14, 'start'))
    return 320, ''.join(o)


FIG[2] = (f2, 'The single 59-minute order drags the mean to 30, to the right of the median 27, and stretches the standard deviation band; the IQR box from 24 to 34 ignores it. The fence at 49 flags 59.',
          'A dot plot of eleven delivery times from 18 to 59 minutes, with 59 in orange. An IQR box from 24 to 34, a bracket for mean ± s from 19.05 to 40.95, a solid line at the median 27, a dashed line at the mean 30 and a dashed fence at 49.')


# ---- 3.3 the normal curve of marks ----
def f3():
    fx = lambda x: 60 + (x - 30) * 10
    base, peak = 236, 176
    fy = lambda x: base - peak * math.exp(-((x - 62) / 8) ** 2 / 2)

    def area(a, b, fill, op):
        xs = [a + (b - a) * i / 60 for i in range(61)]
        pts = [(fx(a), base)] + [(fx(x), fy(x)) for x in xs] + [(fx(b), base)]
        return P(pts, 'none', 0, None, fill, op)
    o = [area(54, 70, AC, 0.22), area(74, 94, LV, 0.3), area(30, 50, LV, 0.3)]
    curve = [(fx(30 + i * 64 / 160), fy(30 + i * 64 / 160)) for i in range(161)]
    o.append(P(curve, INK, 2.5))
    o += [L(fx(75.16), 50, fx(75.16), base, NX, 2, '6 4'), T(fx(75.16) + 6, 52, 'O grade from 75.16 → 76', 13, 'start', NX, True)]
    o += [T(fx(62), 170, '54 to 70', 14, fill=AC, bold=True), T(fx(62), 190, '68.26%', 15, fill=AC, bold=True),
          T(fx(84), 178, 'above 74', 13, fill=LV, bold=True), T(fx(84), 196, '6.68% ≈ 27', 13, fill=LV, bold=True),
          T(fx(40), 178, 'below 50: fail', 13, fill=LV, bold=True), T(fx(40), 196, '6.68% ≈ 27', 13, fill=LV, bold=True)]
    o.append(L(fx(30), base, fx(94), base, L2, 1.5))
    for k in range(-3, 4):
        x = 62 + 8 * k
        o += [L(fx(x), base, fx(x), base + 5, L2, 1.5), T(fx(x), base + 20, str(x), 13, fill=INK),
              T(fx(x), base + 40, ('z = ' if k == -3 else '') + str(k).replace('-', '−'), 13, fill=MUT)]
    o.append(T(20, 318, 'z = (74 − 62) ÷ 8 = 1.5, and P(X > 74) = 1 − 0.9332 = 0.0668, so about 27 of the 400 students.', 14, 'start'))
    return 332, ''.join(o)


FIG[3] = (f3, 'Marks follow N(62, 8²) with the marks and z scales under one axis. 68.26% lie between 54 and 70, 6.68% (about 27 students) score above 74, the same number fail below 50, and an O needs 76.',
          'A bell curve centred on 62 with a marks scale 38 to 86 and a z scale −3 to 3. The band 54 to 70 is shaded blue and labelled 68.26%; both tails beyond 50 and 74 are shaded orange, 6.68% each. A dashed green line at 75.16 marks the O grade cut.')


# ---- 3.4 covariance and r from six students ----
def f4():
    x0, x1, y0, y1 = 80, 440, 40, 260
    fx = lambda h: x0 + (h - 1) * (x1 - x0) / 9
    fy = lambda m: y1 - (m - 45) * (y1 - y0) / 45
    pts = [(2, 50, '52.5'), (3, 55, '25'), (5, 65, '0'), (6, 60, '−2.5'), (8, 75, '25'), (9, 85, '70')]
    o = [axes(x0, x1, y0, y1, range(1, 11), [50, 60, 70, 80, 90], fx, fy, 'study hours', 'marks')]
    o += [L(fx(5.5), y0, fx(5.5), y1, MUT, 1.5, '5 4'), L(x0, fy(65), x1, fy(65), MUT, 1.5, '5 4'),
          T(fx(5.5) + 4, y0 + 14, 'x̄ = 5.5', 13, 'start', MUT, True), T(x1 - 4, fy(65) - 6, 'ȳ = 65', 13, 'end', MUT, True)]
    o += [T(x1 - 10, 140, 'both above: + product', 13, 'end', NX), T(x0 + 10, 182, 'both below: + product', 13, 'start', NX)]
    for h, m, p in pts:
        c = LV if p.startswith('−') else NX
        o += [C(fx(h), fy(m), 6, c), T(fx(h) + 10, fy(m) + 18 if h == 6 else fy(m) - 8, p, 13, 'start', c, True)]
    o.append(boxt(480, 40, 220, 196, ['Σ products = 170', 'cov = 170 ÷ 5 = 34', 'Σ(x − x̄)² = 37.5', 'Σ(y − ȳ)² = 850',
                                      'r = 170 ÷ √(37.5 × 850)', '= 0.952', 'r² = 0.907'], PANEL, AC, 14, True))
    o.append(T(20, 330, 'Five of the six products are positive, so r is strongly positive; it shows a link, not a cause.', 14, 'start', AC, True))
    return 344, ''.join(o)


FIG[4] = (f4, 'Dashed lines at the means split the plot into four parts; five students fall where both values are above or both below, so their products are positive and r = 0.952.',
          'A scatter of marks against study hours for six students, with dashed mean lines at 5.5 hours and 65 marks. Each point is labelled with its product of deviations: 52.5, 25, 0, −2.5, 25, 70. A side box gives Σ 170, cov 34 and r = 0.952.')


# ---- 3.5 a third variable behind a correlation ----
def f5():
    x0, x1, y0, y1 = 80, 450, 40, 260
    fx = lambda a: x0 + (a - 150) * (x1 - x0) / 500
    fy = lambda m: y1 - (m - 24) * (y1 - y0) / 20
    o = [axes(x0, x1, y0, y1, [200, 300, 400, 500, 600], [24, 28, 32, 36, 40, 44], fx, fy, 'bill amount (₹)', 'delivery minutes')]
    ch = [(240, 31), (180, 26), (310, 27), (290, 30)]
    bl = [(520, 38), (450, 42), (380, 33), (610, 40)]
    for a, m in ch: o.append(C(fx(a), fy(m), 7, AC))
    for a, m in bl: o.append(sq(fx(a), fy(m), LV, True, 13))
    o += [C(500, 52, 7, AC), T(514, 57, 'Chennai', 14, 'start', AC, True), sq(500, 80, LV, True, 13), T(514, 85, 'Bengaluru', 14, 'start', LV, True)]
    o.append(boxt(490, 110, 210, 58, ['all 8 orders', 'r = 0.87'], PANEL, INK, 15, True))
    o.append(boxt(490, 180, 210, 80, ['inside each city', 'Bengaluru r = 0.55', 'Chennai r = 0.29'], PANEL, L2, 14, True))
    o.append(T(20, 330, 'Bengaluru has bigger bills and longer trips (38.25 against 28.50 min), so the city drives much of the 0.87.', 13, 'start', LV, True))
    return 344, ''.join(o)


FIG[5] = (f5, 'Across all eight orders bigger bills go with longer deliveries, r = 0.87. Colour the points by city and the link weakens to 0.55 and 0.29: the city is a third variable behind it.',
          'A scatter of delivery minutes against bill amount: four blue circles for Chennai at low bills and short times, four orange squares for Bengaluru at high bills and long times. Side boxes give r = 0.87 overall and 0.55 and 0.29 within the cities.')


# ---- 3.6 the Matplotlib figure the code draws ----
def f6():
    o = [R(10, 10, 700, 336, 'none', MUT, 6, 1.5, '6 4'), T(20, 30, 'Figure', 13, 'start', MUT, True),
         T(360, 32, 'A Chennai tea stall, Jan–Jun', 15, bold=True)]
    x0, x1, y0, y1 = 80, 380, 74, 280
    fx = lambda i: x0 + (i + 0.5) * (x1 - x0) / 6
    fy = lambda v: y1 - v * (y1 - y0) / 180
    o += [T((x0 + x1) / 2, 64, 'Cups sold per month', 14, bold=True), R(x0, y0, x1 - x0, y1 - y0, 'none', L2, 0, 1.2)]
    for v in (0, 60, 120, 180):
        o += [L(x0 - 5, fy(v), x0, fy(v), L2, 1.5), T(x0 - 9, fy(v) + 4.5, str(v), 13, 'end', MUT)]
    for i, m in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']):
        o.append(T(fx(i), y1 + 18, m, 13, fill=MUT))
    o += [T((x0 + x1) / 2, y1 + 38, 'Month', 13, fill=MUT), vtext(36, (y0 + y1) / 2, 'Cups sold (hundreds)')]
    tea, cof = [120, 135, 150, 110, 95, 140], [80, 85, 90, 100, 105, 98]
    o.append(P([(fx(i), fy(v)) for i, v in enumerate(tea)], LV, 2.5))
    o.append(P([(fx(i), fy(v)) for i, v in enumerate(cof)], AC, 2.5, '7 4'))
    for i, v in enumerate(tea): o.append(C(fx(i), fy(v), 5, LV))
    for i, v in enumerate(cof): o.append(sq(fx(i), fy(v), AC, True, 9))
    o += [T(fx(2.6), fy(40), 'Summer dip', 13, 'start', INK, True), ar(fx(3.3), fy(48), fx(4) - 3, fy(95) + 8, INK, 1.5)]
    o += [R(x0 + 8, y1 - 50, 92, 42, PANEL, L2, 4, 1), L(x0 + 14, y1 - 36, x0 + 34, y1 - 36, LV, 2.5), T(x0 + 40, y1 - 31, 'Tea', 13, 'start'),
          L(x0 + 14, y1 - 18, x0 + 34, y1 - 18, AC, 2.5, '5 3'), T(x0 + 40, y1 - 13, 'Coffee', 13, 'start')]
    o.append(T(x1 - 6, y0 + 16, 'Axes', 13, 'end', MUT, True))
    X0, X1 = 490, 690
    gy = lambda v: y1 - v * (y1 - y0) / 900
    o += [T((X0 + X1) / 2, 64, 'Six-month total', 14, bold=True), R(X0, y0, X1 - X0, y1 - y0, 'none', L2, 0, 1.2)]
    for v in (0, 200, 400, 600, 800):
        o += [L(X0 - 5, gy(v), X0, gy(v), L2, 1.5), T(X0 - 9, gy(v) + 4.5, str(v), 13, 'end', MUT)]
    for i, (nm, v, c, f) in enumerate([('Tea', 750, LV, LVS), ('Coffee', 558, AC, ACS)]):
        bx = X0 + 30 + i * 100
        o += [R(bx, gy(v), 60, y1 - gy(v), f, c, 0, 2), T(bx + 30, gy(v) - 6, str(v), 14, fill=c, bold=True), T(bx + 30, y1 + 18, nm, 13, fill=MUT)]
    o += [vtext(446, (y0 + y1) / 2, 'Cups (hundreds)'), T(X1 - 6, y0 + 16, 'Axes', 13, 'end', MUT, True)]
    return 352, ''.join(o)


FIG[6] = (f6, 'One Figure holding two Axes, as plt.subplots(1, 2) makes it. The left Axes has the two lines, a lower-left legend and the arrow to May\'s 95; the right has bars labelled 750 and 558.',
          'A dashed Figure box titled A Chennai tea stall. Left Axes: a solid tea line 120, 135, 150, 110, 95, 140 and a dashed coffee line 80 to 105 over January to June, y from 0 to 180, a legend at lower left and an arrow labelled Summer dip pointing at May. Right Axes: two bars, tea 750 and coffee 558.')


# ---- 3.7 one batter, two ways to find the quartiles ----
def f7():
    runs = [12, 18, 25, 31, 34, 40, 45, 52, 58, 66, 121]
    fx = lambda v: 60 + v * 4.8
    ya = 250
    o = [xaxis(fx(0), fx(130), ya, [0, 20, 40, 60, 80, 100, 120], fx, 'runs in an innings')]
    for v in runs: o.append(C(fx(v), ya - 10, 5, LV if v == 121 else NX))

    def box(y, q1, q3, fence, c, f, lab, sub):
        return ''.join([L(fx(12), y, fx(q1), y, INK, 2), L(fx(q3), y, fx(66), y, INK, 2), L(fx(12), y - 10, fx(12), y + 10, INK, 2),
                        L(fx(66), y - 10, fx(66), y + 10, INK, 2), R(fx(q1), y - 18, fx(q3) - fx(q1), 36, f, c, 2),
                        L(fx(40), y - 18, fx(40), y + 18, c, 3), C(fx(121), y, 6, LV),
                        L(fx(fence), y - 26, fx(fence), y + 26, LV, 1.8, '5 4'), T(fx(fence), y - 30, f'fence {fence}', 13, fill=LV, bold=True),
                        T(20, y - 30, lab + ': ' + sub, 14, 'start', c, True)])
    o.append(box(80, 25, 58, 107.5, AC, ACS, 'by hand, position (n + 1)p', 'Q1 25, Q3 58, IQR 33'))
    o.append(box(176, 28, 55, 95.5, NX, NXS, 'Matplotlib (NumPy interpolates)', 'Q1 28, Q3 55, IQR 27'))
    o.append(T(20, 316, 'Either way the whiskers end at 12 and 66 and 121 is the only outlier. Mean 45.6 > median 40: right skew.', 14, 'start'))
    return 330, ''.join(o)


FIG[7] = (f7, 'The same 11 innings boxed two ways: by hand the box runs 25 to 58, Matplotlib draws 28 to 55. Both keep the median 40 and the whiskers at 12 and 66, and both flag 121.',
          'Two horizontal box plots over a runs axis from 0 to 130 with the eleven innings as dots. The top box, by hand, runs 25 to 58 with fence 107.5; the lower box, Matplotlib, runs 28 to 55 with fence 95.5. Both have median 40, whiskers 12 and 66, and 121 drawn alone.')


# ---- 3.8 the correlation heatmap ----
def f8():
    names = ['hours', 'attend', 'phone', 'marks']
    Rm = [[1.00, 0.14, -0.51, 0.92], [0.14, 1.00, 0.04, 0.40], [-0.51, 0.04, 1.00, -0.61], [0.92, 0.40, -0.61, 1.00]]
    gx, gy, s = 130, 40, 74
    o = []
    for j, n in enumerate(names):
        o.append(T(gx + j * s + s / 2, gy - 10, n, 14, bold=True))
        o.append(T(gx - 10, gy + j * s + s / 2 + 5, n, 14, 'end', INK, True))
    for i in range(4):
        for j in range(4):
            r = Rm[i][j]
            c = AC if r >= 0 else LV
            o.append(f'<rect x="{gx + j * s}" y="{gy + i * s}" width="{s}" height="{s}" style="fill:{c};fill-opacity:{0.06 + 0.5 * abs(r):.2f};stroke:var(--fig);stroke-width:2"/>')
            o.append(T(gx + j * s + s / 2, gy + i * s + s / 2 + 5, f'{r:.2f}'.replace('-', '−'), 15, bold=abs(r) > 0.5 and i != j))
    for (i, j) in [(0, 3), (2, 3)]:
        o.append(R(gx + j * s + 2, gy + i * s + 2, s - 4, s - 4, 'none', AC if Rm[i][j] > 0 else LV, 2, 2.5))
    cb = 448
    for k in range(9):
        r = 1 - k * 0.25
        c = AC if r >= 0 else LV
        o.append(f'<rect x="{cb}" y="{gy + k * 32}" width="20" height="32" style="fill:{c};fill-opacity:{0.06 + 0.5 * abs(r):.2f}"/>')
    o += [T(cb + 26, gy + 14, '+1', 13, 'start', MUT), T(cb + 26, gy + 4 * 32 + 20, '0', 13, 'start', MUT), T(cb + 26, gy + 9 * 32 - 4, '−1', 13, 'start', MUT)]
    o += [boxt(510, 40, 190, 60, ['(a) strongest with marks', 'hours, r = 0.92'], ACS, AC, 13, True),
          boxt(510, 112, 190, 60, ['(b) negative', 'phone and marks, −0.61'], LVS, LV, 13, True),
          boxt(510, 184, 190, 60, ['(c) pair plot of 3 columns', '3 × 3 = 9 panels'], PANEL, L2, 13, True)]
    o.append(T(20, 360, 'The diagonal is always 1 and the two triangles mirror each other; phone and hours are also negative, −0.51.', 13, 'start'))
    return 374, ''.join(o)


FIG[8] = (f8, 'The correlation matrix as a heatmap: blue for positive, orange for negative, stronger colour for larger |r|. The eye goes to hours and marks (0.92) and phone and marks (−0.61).',
          'A 4 by 4 heatmap for hours, attendance, phone and marks with the r values written in the cells. Hours–marks 0.92 is outlined in blue and phone–marks −0.61 in orange. A colour bar runs from +1 to −1, and side boxes give the answers 0.92, −0.61 and 9 panels.')

spec = make_spec(FIG)
