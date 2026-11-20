"""Claude's hand-drawn figures for ec-signals-u6 (Z-transform and discrete Fourier analysis), one per chapter.
Every number comes from that chapter's own worked example. Colours are only the shell's CSS variables."""
import os, sys, math, cmath
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

PI = math.pi


def stem(x, y0, y, c=AC, r=5, w=2.2):
    """one stem from the axis y0 to y with a dot"""
    return L(x, y0, x, y, c, w) + C(x, y, r, c)


def cross(x, y, s=8, c=NX, w=3):
    return L(x - s, y - s, x + s, y + s, c, w) + L(x - s, y + s, x + s, y - s, c, w)


def ring(x, y, r=7, c=AC, w=2.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:{w}"/>'


def circ(cx, cy, r, c=L2, w=1.8, dash=None, fill='none'):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" style="fill:{fill};stroke:{c};stroke-width:{w}{d}"/>'


def annulus(cx, cy, r1, r2, fill=ACS):
    """shaded ring r1 < |z| < r2 (even-odd fill)"""
    def c(r):
        return f'M{cx + r:.1f},{cy:.1f} A{r:.1f},{r:.1f} 0 1 0 {cx - r:.1f},{cy:.1f} A{r:.1f},{r:.1f} 0 1 0 {cx + r:.1f},{cy:.1f} Z'
    return f'<path d="{c(r2)} {c(r1)}" style="fill:{fill};fill-rule:evenodd;stroke:none"/>'


def zplane(cx, cy, xl, xr, yt, yb):
    """Re and Im axes through the origin (cx, cy)"""
    return (L(xl, cy, xr, cy, L2, 1.5, arrow='m') + L(cx, yb, cx, yt, L2, 1.5, arrow='m')
            + T(xr - 4, cy - 10, 'Re z', 13, 'end', MUT) + T(cx + 8, yt + 12, 'Im z', 13, 'start', MUT))


def f2(v, d=2):
    return neg(f'{v:.{d}f}')


FIG = {}


# ---- 6.1 one period of the pulse train and its DTFS magnitudes (N = 8) ----
def fig1():
    o = []
    x0, dx = 92, 38.5
    X = lambda n: x0 + n * dx
    # top: x[n] over two periods
    ya, ys = 150, 70
    o.append(T(20, 40, 'x[n], period N = 8', 15, 'start', INK, True))
    o.append(xaxis(70, 700, ya, [], X))
    for n in range(16):
        v = 1 if n % 8 < 3 else 0
        o.append(stem(X(n), ya, ya - v * ys, AC if n < 8 else L2) if v else C(X(n), ya, 4, L2))
        o.append(T(X(n), ya + 20, str(n), 13, fill=MUT))
    o.append(T(X(16) - 6, ya + 20, 'n', 13, 'start', MUT))
    o.append(T(52, ya - ys + 5, '1', 13, 'end', MUT) + L(56, ya - ys, 64, ya - ys, L2, 1.5))
    o.append(brace(X(0), X(7), 180, MUT))
    o.append(T((X(0) + X(7)) / 2, 202, 'one period: 1, 1, 1, 0, 0, 0, 0, 0', 13, fill=MUT))
    o.append(T((X(8) + X(15)) / 2, 202, 'the next period repeats it', 13, fill=MUT))
    # bottom: |X[k]| over two periods of k
    mags = [3, 2.4142, 1, 0.4142, 1, 0.4142, 1, 2.4142]
    yb, sc = 430, 52
    o.append(T(20, 245, '|X[k]|, also period 8 in k', 15, 'start', INK, True))
    o.append(xaxis(70, 700, yb, [], X))
    lab = ['3', '2.41', '1', '0.41', '1', '0.41', '1', '2.41']
    for k in range(16):
        m = mags[k % 8]
        c = NX if k % 8 in (1, 7) else (AC if k < 8 else L2)
        o.append(stem(X(k), yb, yb - m * sc, c))
        o.append(T(X(k), yb + 20, str(k), 13, fill=MUT))
        if k < 8:
            o.append(T(X(k), yb - m * sc - 12, lab[k], 13, fill=c if c == NX else INK))
    o.append(T(X(16) - 6, yb + 20, 'k', 13, 'start', MUT))
    o.append(T(X(1), 470, 'X[1] = 1.71 − j1.71', 13, 'middle', NX))
    o.append(T(X(7), 470, 'X[7] = 1.71 + j1.71 = X*[1]', 13, 'middle', NX))
    o.append(T((X(8) + X(15)) / 2, 470, 'X[k + 8] = X[k]', 13, fill=MUT))
    return 492, ''.join(o)
FIG[1] = (fig1, 'The pulse 1, 1, 1, 0, 0, 0, 0, 0 repeats every 8 samples, and so do its coefficients: |X[k]| = 3, 2.41, 1, 0.41, 1, 0.41, 1, 2.41 and then the same again. X[1] and X[7] are conjugates, so their magnitudes match.',
          'Top: two periods of the pulse train x[n] with period 8. Bottom: the DTFS magnitudes for k from 0 to 15, repeating every 8, with k = 1 and k = 7 marked equal.')


# ---- 6.2 |X(e^jw)| for (0.8)^n u[n] and (0.5)^n u[n] over two periods ----
def fig2():
    x0, x1, y0, y1 = 80, 690, 70, 360
    fx = lambda w: x0 + (w + 2 * PI) / (4 * PI) * (x1 - x0)
    fy = lambda v: y1 - v / 5.5 * (y1 - y0)
    tick = [-2 * PI, -PI, 0, PI, 2 * PI]
    names = {-2 * PI: '−2π', -PI: '−π', 0: '0', PI: 'π', 2 * PI: '2π'}
    o = [axes(x0, x1, y0, y1, tick, [0, 1, 2, 3, 4, 5], fx, fy, 'ω (rad/sample)', '|X(e^jω)|', lambda v: names[v])]
    o[0] = o[0].replace('|X(e^jω)|', '|X(e<tspan dy="-6" font-size="11">jω</tspan><tspan dy="6">)|</tspan>')
    m8 = lambda w: 1 / abs(1 - 0.8 * cmath.exp(-1j * w))
    m5 = lambda w: 1 / abs(1 - 0.5 * cmath.exp(-1j * w))
    ws = [-2 * PI + i * 4 * PI / 600 for i in range(601)]
    o.append(P([(fx(w), fy(m5(w))) for w in ws], LV, 2.5))
    o.append(P([(fx(w), fy(m8(w))) for w in ws], AC, 2.8))
    # one period shaded band label
    o.append(L(fx(-PI), y0 + 2, fx(-PI), y1, L2, 1.2, '4 4') + L(fx(PI), y0 + 2, fx(PI), y1, L2, 1.2, '4 4'))
    o.append(Tb(fx(-PI / 2), fy(4.4), 'one period: −π to π', 13, 'middle', MUT))
    # marked values for a = 0.8
    for w, v in ((0, 5), (PI / 2, 0.781), (PI, 0.556)):
        o.append(C(fx(w), fy(v), 5.5, NX))
    o.append(Tb(fx(0) + 14, fy(5) + 5, '5 at ω = 0', 14, 'start', NX))
    o.append(L(fx(PI / 2), fy(1.9) + 6, fx(PI / 2), fy(0.781) - 7, NX, 1.5))
    o.append(Tb(fx(PI / 2), fy(1.9), '0.781 at ω = π/2', 13, 'middle', NX))
    o.append(L(fx(PI) + 30, fy(1.3) + 6, fx(PI) + 4, fy(0.556) - 6, NX, 1.5))
    o.append(Tb(fx(PI) + 12, fy(1.3), '0.556 at ω = π', 13, 'start', NX))
    o.append(C(fx(0), fy(2), 5.5, LV))
    o.append(L(fx(-2.3) + 40, fy(3.0) + 6, fx(0) - 5, fy(2) - 3, LV, 1.5))
    o.append(Tb(fx(-2.3), fy(3.0), 'a = 0.5: 2 at ω = 0', 13, 'middle', LV))
    # legend
    o += [L(440, 30, 472, 30, AC, 3), T(480, 35, 'a = 0.8', 14, 'start')]
    o += [L(560, 30, 592, 30, LV, 3), T(600, 35, 'a = 0.5', 14, 'start')]
    o.append(T(80, 35, 'x[n] = aⁿu[n]', 14, 'start', INK, True))
    return 410, ''.join(o)
FIG[2] = (fig2, 'For x[n] = (0.8)ⁿu[n] the magnitude is 5 at ω = 0, 0.781 at π/2 and 0.556 at π; the pattern repeats every 2π. With a = 0.5 the peak is only 2, so a pole nearer 1 gives a taller, narrower peak.',
          'Two magnitude curves from ω = −2π to 2π, peaking at ω = 0 and at ±2π: the taller one, for a = 0.8, reaches 5; the lower one, for a = 0.5, reaches 2.')


# ---- 6.3 the 4-point DFT of 1, 2, 3, 4 as samples of its DTFT; 8-point zero padding fills in ----
def fig3():
    x = [1, 2, 3, 4]
    D = lambda w: abs(sum(x[n] * cmath.exp(-1j * w * n) for n in range(4)))
    x0, x1, y0, y1 = 80, 690, 70, 350
    fx = lambda w: x0 + w / (2 * PI) * (x1 - x0)
    fy = lambda v: y1 - v / 11 * (y1 - y0)
    names = {0: '0', PI / 2: 'π/2', PI: 'π', 3 * PI / 2: '3π/2', 2 * PI: '2π'}
    o = [axes(x0, x1, y0, y1, list(names), [0, 2, 4, 6, 8, 10], fx, fy, 'ω (rad/sample)', 'magnitude', lambda v: names[v])]
    ws = [i * 2 * PI / 500 for i in range(501)]
    o.append(P([(fx(w), fy(D(w))) for w in ws], L2, 2.2))
    # 8-point samples (zero padding to 8)
    for k in range(8):
        w = 2 * PI * k / 8
        if k % 2: o.append(ring(fx(w), fy(D(w)), 6, LV, 2.5))
    lab = {0: ('|X[0]| = 10', 'start', 12, 4), 1: ('|X[1]| = 2.83', 'middle', 0, -16), 2: ('|X[2]| = 2', 'middle', 0, -16), 3: ('|X[3]| = 2.83', 'middle', 0, -16)}
    for k in range(4):
        w = 2 * PI * k / 4
        o.append(L(fx(w), y1, fx(w), fy(D(w)), AC, 2.2) + C(fx(w), fy(D(w)), 6, AC))
        s, a, ddx, ddy = lab[k]
        o.append(Tb(fx(w) + ddx, fy(D(w)) + ddy, s, 14, a, AC))
    # legend
    o += [L(330, 30, 362, 30, L2, 2.2), T(370, 35, 'DTFT |X(e<tspan dy="-6" font-size="11">jω</tspan><tspan dy="6">)|</tspan>', 13, 'start', MUT)]
    o += [C(500, 30, 6, AC), T(512, 35, '4-point DFT', 13, 'start')]
    o += [ring(612, 30, 6, LV), T(624, 35, '8-point', 13, 'start', LV)]
    o.append(T(80, 35, 'x[n] = 1, 2, 3, 4', 14, 'start', INK, True))
    return 400, ''.join(o)
FIG[3] = (fig3, 'The 4-point DFT of 1, 2, 3, 4 gives |X[k]| = 10, 2.83, 2, 2.83: four samples of the DTFT curve at ω = 0, π/2, π and 3π/2. Zero padding to 8 points adds the hollow samples halfway between, on the same curve.',
          'A grey DTFT magnitude curve over one period from 0 to 2π, with four solid DFT samples at 0, π/2, π and 3π/2 and four hollow 8-point samples between them.')


# ---- 6.4 pole-zero plot and ROC of (1/3)^n u[n] - (1/2)^n u[-n-1] ----
def fig4():
    cx, cy, s = 200, 250, 300
    o = [annulus(cx, cy, s / 3, s / 2)]
    o.append(zplane(cx, cy, 30, 700, 30, 470))
    o.append(circ(cx, cy, s / 3, AC, 1.8, '6 4') + circ(cx, cy, s / 2, AC, 1.8, '6 4'))
    a = math.asin(0.68)
    xa, ya = cx + s * math.cos(a), cy - s * math.sin(a)
    o.append(f'<path d="M{xa:.1f},{ya:.1f} A{s},{s} 0 0 1 {xa:.1f},{cy + s * math.sin(a):.1f}" style="fill:none;stroke:{INK};stroke-width:2"/>')
    o.append(cross(cx + s / 3, cy, 7) + cross(cx + s / 2, cy, 7))
    o.append(ring(cx, cy, 7) + ring(cx + s * 5 / 12, cy, 6))
    o.append(Tb(cx + s / 3 - 8, cy + 30, 'pole 1/3', 13, 'end', NX))
    o.append(L(cx + s / 3 - 10, cy + 20, cx + s / 3 - 3, cy + 9, NX, 1.4))
    o.append(Tb(cx + s / 2 + 12, cy + 34, 'pole 1/2', 13, 'start', NX))
    o.append(L(cx + s / 2 + 12, cy + 24, cx + s / 2 + 4, cy + 9, NX, 1.4))
    o.append(Tb(cx + s * 5 / 12, cy - 44, 'zero 5/12', 13, 'middle', AC))
    o.append(L(cx + s * 5 / 12, cy - 38, cx + s * 5 / 12, cy - 9, AC, 1.4))
    o.append(Tb(cx - 12, cy + 26, 'zero 0', 13, 'end', AC))
    px, py = cx + 0.42 * s * math.cos(2.1), cy - 0.42 * s * math.sin(2.1)
    o.append(Tb(40, 52, 'ROC: 1/3 < |z| < 1/2', 14, 'start', AC, True))
    o.append(L(110, 60, px, py, AC, 1.6, arrow='n'))
    o.append(Tb(xa - 8, ya + 4, 'unit circle |z| = 1', 13, 'end', INK))
    o.append(Tb(cx + s + 14, cy - 64, 'outside the ROC,', 13, 'start', INK))
    o.append(Tb(cx + s + 14, cy - 44, 'so no DTFT', 13, 'start', INK))
    o.append(T(cx + s + 8, cy + 20, '1', 13, 'start', MUT))
    return 490, ''.join(o)
FIG[4] = (fig4, 'Poles × at 1/3 and 1/2 and zeros ○ at 0 and 5/12 for the worked example. The shaded ring 1/3 < |z| < 1/2 is the ROC; the unit circle lies outside it, so this sequence has no DTFT.',
          'A z-plane with poles at one third and one half on the real axis, zeros at the origin and at five twelfths, a shaded ring between radius one third and one half, and an arc of the unit circle well outside the ring.')


# ---- 6.5 multiply by n: (0.5)^n u[n] and n(0.5)^n u[n], single and double pole ----
def fig5():
    o = []
    x0, dx = 70, 42
    X = lambda n: x0 + n * dx
    xs = [0.5 ** n for n in range(8)]
    ys = [n * 0.5 ** n for n in range(8)]
    for row, (vals, top, name, col, labs) in enumerate((
            (xs, 40, 'x[n] = (0.5)ⁿu[n]', AC, ['1', '0.5', '0.25', '0.125']),
            (ys, 270, 'y[n] = n(0.5)ⁿu[n]', LV, ['0', '0.5', '0.5', '0.375', '0.25']))):
        ya, sc = top + 170, 130
        o.append(T(20, top + 8, name, 15, 'start', INK, True))
        o.append(xaxis(50, 400, ya, [], X))
        for n, v in enumerate(vals):
            o.append(stem(X(n), ya, ya - v * sc, col) if v else C(X(n), ya, 5, col))
            o.append(T(X(n), ya + 20, str(n), 13, fill=MUT))
            if n < len(labs):
                o.append(T(X(n) + (14 if row == 1 and n == 1 else 0) - (14 if row == 1 and n == 2 else 0) * 0, ya - v * sc - 12, labs[n], 13, 'middle', col))
        o.append(T(X(8) - 10, ya + 20, 'n', 13, 'start', MUT))
    # z-domain boxes on the right
    o.append(boxt(450, 70, 250, 120, ['X(z) = z/(z − 0.5)', 'one pole at z = 0.5', 'ROC |z| > 0.5'], PANEL, AC, 14, True))
    o.append(boxt(450, 300, 250, 120, ['Y(z) = 0.5z/(z − 0.5)²', 'double pole at z = 0.5', 'ROC |z| > 0.5'], PANEL, LV, 14, True))
    o.append(L(575, 194, 575, 294, AC, 2.2, arrow='n'))
    o.append(Tb(575, 238, 'n·x[n] ↔ −z dX/dz', 14, 'middle', INK, True))
    o.append(Tb(575, 262, 'ROC unchanged', 13, 'middle', MUT))
    o.append(T(575, 450, 'check at z = 2: X = 1.333, Y = 0.444', 13, 'middle', MUT))
    return 470, ''.join(o)
FIG[5] = (fig5, 'Multiplying (0.5)ⁿ by n gives 0, 0.5, 0.5, 0.375, 0.25, …: the samples rise before they decay. In the z-domain the single pole at 0.5 becomes a double pole and the ROC |z| > 0.5 stays the same.',
          'Left: stem plots of (0.5) to the n, starting at 1, and of n times (0.5) to the n, starting at 0 and peaking at 0.5. Right: X(z) with one pole at 0.5 and Y(z) with a double pole at 0.5, linked by the multiply-by-n rule.')


# ---- 6.6 ROC 0.5 < |z| < 2 picks a causal and an anti-causal term ----
def fig6():
    o = []
    cx, cy, s = 175, 220, 66
    o.append(annulus(cx, cy, s * 0.5, s * 2))
    o.append(zplane(cx, cy, 15, 362, 40, 400))
    o.append(circ(cx, cy, s * 0.5, NX, 1.6, '5 4') + circ(cx, cy, s * 2, NX, 1.6, '5 4'))
    # contour C at radius 1 with a counterclockwise arrow
    o.append(circ(cx, cy, s, AC, 2.4))
    o.append(f'<path d="M{cx + s * math.cos(-0.5):.1f},{cy - s * math.sin(-0.5):.1f} A{s},{s} 0 0 0 {cx + s * math.cos(0.5):.1f},{cy - s * math.sin(0.5):.1f}" style="fill:none;stroke:{AC};stroke-width:2.4" marker-end="url(#ar-UID-n)"/>')
    o.append(cross(cx + s * 0.5, cy, 7) + cross(cx + s * 2, cy, 8))
    o.append(Tb(cx + s * 0.5 + 4, cy + 28, '0.5', 13, 'middle', NX))
    o.append(Tb(cx + s * 2 + 4, cy + 28, '2', 13, 'middle', NX))
    o.append(Tb(cx - s * 0.7, cy - s - 14, 'C: |z| = 1', 13, 'middle', AC))
    o.append(T(cx, 432, 'ROC 0.5 < |z| < 2 (shaded)', 14, 'middle', INK, True))
    o.append(T(cx, 454, '0.5 inside C → causal term', 13, 'middle', MUT))
    o.append(T(cx, 474, '2 outside C → anti-causal term', 13, 'middle', MUT))
    # stem plot of x[n] = -(1/3)(0.5)^n u[n] - (4/3) 2^n u[-n-1]
    xv = lambda n: -(1 / 3) * 0.5 ** n if n >= 0 else -(4 / 3) * 2.0 ** n
    X = lambda n: 545 + n * 30
    ya, sc = 120, 300
    o.append(T(380, 40, 'x[n] for n = −5 … 5', 15, 'start', INK, True))
    o.append(xaxis(380, 712, ya, [], X))
    for n in range(-5, 6):
        v = xv(n)
        o.append(stem(X(n), ya, ya - v * sc, LV if n < 0 else AC, 4.5))
        o.append(T(X(n), ya - 10, neg(str(n)), 13, fill=MUT))
    o.append(Tb(X(-1) - 6, ya + 0.667 * sc + 22, '−0.667', 13, 'middle', LV))
    o.append(Tb(X(0) + 10, ya + 0.333 * sc + 22, '−0.333', 13, 'start', AC))
    o.append(T(X(-3), 380, 'n < 0: −(4/3)·2ⁿ', 13, 'middle', LV))
    o.append(T(X(3), 380, 'n ≥ 0: −(1/3)·(0.5)ⁿ', 13, 'middle', AC))
    o.append(T(545, 410, 'both sides decay, so Σ|x[n]| is finite', 13, 'middle', MUT))
    return 492, ''.join(o)
FIG[6] = (fig6, 'For X(z) = 1/((1 − 0.5z⁻¹)(1 − 2z⁻¹)) with ROC 0.5 < |z| < 2, the contour C sits in the ring: the pole at 0.5 is inside C and gives −(1/3)(0.5)ⁿu[n]; the pole at 2 is outside and gives −(4/3)2ⁿu[−n−1].',
          'Left: a z-plane with poles at 0.5 and 2, a shaded ring between them and a counterclockwise contour C at radius 1. Right: the two-sided sequence x[n] for n from −5 to 5, all values negative, largest in size at n = −1.')


# ---- 6.7 y[n] - 0.5y[n-1] = x[n]: pole-zero plot and step response ----
def fig7():
    o = []
    cx, cy, s = 160, 230, 120
    o.append(f'<rect x="20" y="60" width="300" height="340" style="fill:{ACS}"/>')
    o.append(circ(cx, cy, s * 0.5, 'var(--fig)', 0, None, 'var(--fig)'))
    o.append(zplane(cx, cy, 24, 316, 64, 396))
    o.append(circ(cx, cy, s * 0.5, NX, 1.6, '5 4'))
    o.append(circ(cx, cy, s, INK, 2))
    o.append(cross(cx + s * 0.5, cy, 7) + ring(cx, cy, 7))
    o.append(Tb(cx + s * 0.5, cy + 28, 'pole 0.5', 13, 'middle', NX))
    o.append(Tb(cx - 34, cy - 14, 'zero 0', 13, 'middle', AC))
    o.append(Tb(cx + 70, cy - s - 10, '|z| = 1', 13, 'start', INK))
    o.append(T(cx, 30, 'H(z) = z/(z − 0.5)', 15, 'middle', INK, True))
    o.append(T(cx, 50, 'ROC |z| > 0.5 (shaded)', 13, 'middle', MUT))
    o.append(T(cx, 428, 'unit circle inside the ROC:', 13, 'middle', MUT))
    o.append(T(cx, 448, 'causal and BIBO stable', 13, 'middle', INK, True))
    # step response
    X = lambda n: 400 + n * 38
    ya, sc = 380, 140
    o.append(T(380, 30, 'step response y[n] = 2 − (0.5)ⁿ', 15, 'start', INK, True))
    o.append(xaxis(380, 712, ya, [], X))
    o.append(L(380, ya - 2 * sc, 712, ya - 2 * sc, L2, 1.5, '6 4'))
    o.append(T(386, ya - 2 * sc - 8, 'final value 2', 13, 'start', MUT))
    labs = ['1', '1.5', '1.75', '1.875']
    for n in range(8):
        v = 2 - 0.5 ** n
        o.append(stem(X(n), ya, ya - v * sc, LV))
        o.append(T(X(n), ya + 20, str(n), 13, fill=MUT))
        if n < 3: o.append(T(X(n), ya - v * sc - 12, labs[n], 13, 'middle', LV))
    o.append(T(X(8) - 8, ya + 20, 'n', 13, 'start', MUT))
    return 470, ''.join(o)
FIG[7] = (fig7, 'H(z) = z/(z − 0.5) has a zero at 0 and a pole at 0.5; the causal ROC |z| > 0.5 contains the unit circle, so the system is stable. Its step response climbs 1, 1.5, 1.75, 1.875, … to the final value 2.',
          'Left: a z-plane with the region outside radius 0.5 shaded, a pole at 0.5, a zero at the origin and the unit circle inside the shaded region. Right: stem plot of the step response rising from 1 toward the dashed level 2.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        1: [('The worked example computes its coefficients; the figure lists |X[k]| for k=0,…,7. The marked values at k=1 and k=7 are equal because X[7]=X*[1].',
             'The worked example computes its coefficients. Figure 6.1.1 draws two periods of x[n] and of |X[k]|: the coefficients repeat every 8, and the marked values at k=1 and k=7 are equal because X[7]=X*[1].')],
    }.get(k, [])
