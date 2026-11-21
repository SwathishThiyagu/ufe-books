# Glass t16 drawings for Signals and Systems (ec-signals). Every value is computed here from the lesson's own numbers.
from gfx import *
import math, cmath
D = {}
g = lambda v: f'{v:g}'.replace('-', '−')


import re as _re
def R(s):
    """'e^{-2t}' -> escaped text with a real superscript tspan"""
    out, i = '', 0
    for m in _re.finditer(r'\^\{([^}]*)\}', s):
        out += E(s[i:m.start()]) + f'<tspan baseline-shift="super" font-size="68%">{E(m.group(1))}</tspan>'
        i = m.end()
    return out + E(s[i:])

def plain_len(s):
    sup = sum(len(m) for m in _re.findall(r'\^\{([^}]*)\}', s))
    base = len(_re.sub(r'\^\{[^}]*\}', '', s))
    return base + 0.7 * sup

def rtxt(x, y, s, size=16, fill=INK, w=800, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" {F} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{R(s)}</text>'

def rtag(x, y, s, c, size=14, anchor='middle', bg=W):
    w = plain_len(s) * size * 0.58 + 18
    x0 = x - w / 2 if anchor == 'middle' else (x - w if anchor == 'end' else x)
    return (f'<rect x="{x0:.1f}" y="{y - size - 5:.1f}" width="{w:.1f}" height="{size + 13}" rx="{(size + 13) / 2}" fill="{bg}" stroke="{c}" stroke-width="2"/>'
            + rtxt(x0 + w / 2, y + 1, s, size, c))


def sax(p, xt=(), yt=(), xl='', yl='', fmt=g, xfmt=None, grid_=True):
    """signal axes: grid lines and labels for yt, a zero line with ticks, x labels under the plot"""
    o = ''
    for v in yt:
        if grid_ and v != 0: o += line(p.L, p.Y(v), p.L + p.W, p.Y(v), GRID, 1.5)
        o += txt(p.L - 10, p.Y(v) + 5, fmt(v), 13, MUT, 700, 'end')
    y0 = p.Y(0) if p.y0 <= 0 <= p.y1 else p.T + p.H
    o += line(p.L, y0, p.L + p.W + 10, y0, MUT, 2.5, arrow=True)
    if p.x0 <= 0 <= p.x1: o += line(p.X(0), p.T + p.H + 4, p.X(0), p.T - 8, MUT, 2.5, arrow=True)
    for v in xt:
        o += line(p.X(v), y0 - 5, p.X(v), y0 + 5, MUT, 2)
        o += txt(p.X(v), p.T + p.H + 22, (xfmt or fmt)(v), 13, MUT, 700)
    if xl: o += txt(p.L + p.W + 10, p.T + p.H + 44, xl, 13, MUT, 700, 'end')
    if yl: o += txt(p.L + 6 if p.x0 <= 0 <= p.x1 and p.X(0) < p.L + 20 else p.L - 6, p.T - 10, yl, 13, MUT, 700, 'start')
    return o


def stems(xs, vals, x0, dx, yb, k, c=B, r=7, labels=False, size=12, lc=INK, fmt=g, hollow_zero=False):
    o = ''
    for i, v in enumerate(vals):
        x = x0 + i * dx if xs is None else xs[i]
        y = yb - k * v
        if abs(v) < 1e-12 and hollow_zero:
            o += f'<circle cx="{x:.1f}" cy="{yb:.1f}" r="{r - 1}" fill="{W}" stroke="{c}" stroke-width="2.5"/>'
            continue
        o += line(x, yb, x, y, c, 4) + f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{c}"/>'
        if labels: o += txt(x, y - 12 if v >= 0 else y + 22, fmt(v), size, lc, 800)
    return o


def cross(x, y, c=O, r=10, w=5):
    return line(x - r, y - r, x + r, y + r, c, w) + line(x - r, y + r, x + r, y - r, c, w)


def hollow(x, y, c=B, r=9):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{W}" stroke="{c}" stroke-width="4"/>'


def area(p, f, a, b, c, n=80, op=.35):
    pts = [p.P(a, 0)] + [p.P(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)] + [p.P(b, 0)]
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{c}" fill-opacity="{op}" stroke="none"/>'


# ---------------- unit 1 ----------------
def u1L1():
    # x(t) = 6 cos(200 pi t) + 3 V, t in ms; x[n] = 1, 2, 3
    x = lambda t: 6 * math.cos(200 * math.pi * t / 1000) + 3
    P_ = 6 ** 2 / 2 + 3 ** 2                 # 27 W
    T0 = 2 * math.pi / (200 * math.pi) * 1000  # 10 ms
    Ep = P_ * T0 / 1000                        # 0.27 J
    p = Plot(0, 30, -3, 12, L=46, T=16, Wd=430, H=150)
    s = defs() + rect(p.X(0), p.T, p.X(T0) - p.X(0), p.H, MINT, 'none', 0, 6)
    s += sax(p, xt=(0, 10, 20, 30), yt=(-3, 0, 3, 6, 9), xl='t (ms) →', yl='x(t) V')
    s += p.curve(x, 0, 30, n=180, c=B, w=5)
    s += tag(p.X(T0 / 2), p.Y(10.9), f'one period: {Ep:.2f} J', G, 12)
    s += tag(p.X(30), p.Y(11) + 4, f'P = {6 ** 2 / 2:g} + {3 ** 2} = {P_:g} W, E = ∞', B, 13, 'end')
    v = [0, 1, 2, 3, 0]; E = sum(a * a for a in v)
    yb = 345
    s += line(30, yb, 250, yb, MUT, 2.5, arrow=True)
    s += stems(None, v, 50, 46, yb, 24, O, 7, labels=True, size=13)
    for i, n in enumerate((-1, 0, 1, 2, 3)): s += txt(50 + i * 46, yb + 20, g(n), 12, MUT, 700)
    s += txt(258, 280, f'x[n] = 1, 2, 3, then 0', 15, INK, 800, 'start')
    s += txt(258, 306, f'E = 1 + 4 + 9 = {E}', 15, O, 900, 'start')
    s += txt(258, 332, 'P = 0: energy signal', 15, O, 900, 'start')
    return 'Endless wave or short burst', s
D['ec-signals-u1-L1'] = (u1L1, 'endless → power signal', '1.2.1')


def u1L2():
    # x(t): height 2 on 0..2 s; y = x(2t - 1) lives where 0 <= 2t - 1 <= 2
    a, b = 2, 1
    lo, hi = (0 + b) / a, (2 + b) / a      # 0.5 .. 1.5
    wrong = (1, 2)                          # squeeze, then shift by 1 (the trap)
    p = Plot(-0.5, 2.5, 0, 3, L=50, T=40, Wd=420, H=190)
    s = defs() + sax(p, xt=(0, .5, 1, 1.5, 2), yt=(0, 1, 2), xl='t (s) →', yl='x')
    s += poly([p.P(0, 0), p.P(0, 2), p.P(2, 2), p.P(2, 0)], MUT, 3.5, '8 7')
    s += poly([p.P(lo, 0), p.P(lo, 2), p.P(hi, 2), p.P(hi, 0)], O, 6, fill=OS, close=False)
    s += tag(p.X(1), p.Y(2) - 16, f'x(2t − 1): {g(lo)} to {g(hi)} s', O, 14)
    s += tag(p.X(2.05), p.Y(2.75), 'x(t): 0 to 2 s', MUT, 13, 'end')
    s += ring(p.X(lo), p.Y(0), 10)
    s += txt(p.X(lo) - 12, p.Y(.55), 'start', 14, O, 900, 'end')
    s += tag(250, 340, f'delay = b ÷ a = {b} ÷ {a} = {g(b / a)} s, not {wrong[0]} s', B, 15)
    return 'Squeeze first, then shift', s
D['ec-signals-u1-L2'] = (u1L2, f'starts at 0.5 s', '1.4.1')


def u1L3():
    # x[n] = n u[n]; y[n] = x[n - 1]
    ns = list(range(-1, 6))
    xv = [max(n, 0) for n in ns]
    yv = [max(n - 1, 0) for n in ns]
    x0, dx, k = 100, 62, 19
    s = defs()
    for yb, vals, c, lab in ((140, xv, B, 'input x[n] = n u[n]'), (310, yv, G, 'output y[n] = x[n − 1]')):
        s += line(40, yb, 500, yb, MUT, 2.5, arrow=True)
        s += stems(None, vals, x0, dx, yb, k, c, 7, labels=True, size=13)
        for i, n in enumerate(ns): s += txt(x0 + i * dx, yb + 20, g(n), 12, MUT, 700)
        s += txt(20, yb - 112, lab, 15, c, 900, 'start')
    i2, i3 = ns.index(2), ns.index(3)
    xa, ya = x0 + i2 * dx, 140 - k * xv[i2]
    xb, yb_ = x0 + i3 * dx, 310 - k * yv[i3]
    s += f'<path d="M{xa + 8:.1f},{ya + 30:.1f} C{xa + 30:.1f},{ya + 110:.1f} {xb - 10:.1f},{yb_ - 90:.1f} {xb - 2:.1f},{yb_ - 26:.1f}" fill="none" stroke="{O}" stroke-width="3.5" stroke-dasharray="7 6" marker-end="url(#ao)"/>'
    s += tag(360, 194, f'y[3] = x[2] = {xv[i2]}', O, 14, 'start')
    return 'One sample late', s
D['ec-signals-u1-L3'] = (u1L3, 'past only → causal', '1.5.1')


def u1L4():
    # best multiple of sin t for the square wave on 0..2pi
    num = 2 + 2                       # integral of f sin t over 0..2pi
    K = math.pi                       # ||sin||^2
    c = num / K                       # 1.273
    share = (c ** 2 * K) / (2 * math.pi)   # 0.81
    p = Plot(0, 2 * math.pi, -1.7, 1.7, L=50, T=24, Wd=430, H=230)
    sq = lambda t: 1 if t < math.pi else -1
    best = lambda t: c * math.sin(t)
    pts = [p.P(2 * math.pi * i / 120, best(2 * math.pi * i / 120)) for i in range(121)]
    pts += [p.P(2 * math.pi, -1), p.P(math.pi, -1), p.P(math.pi, 1), p.P(0, 1)]
    s = defs() + f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{GS}" stroke="none"/>'
    s += sax(p, xt=(0, math.pi, 2 * math.pi), yt=(-1, 0, 1), xfmt=lambda v: ['0', 'π', '2π'][round(v / math.pi)], xl='t →')
    s += poly([p.P(0, 1), p.P(math.pi, 1), p.P(math.pi, -1), p.P(2 * math.pi, -1)], B, 5)
    s += p.curve(best, 0, 2 * math.pi, n=120, c=O, w=5)
    s += ring(*p.P(math.pi / 2, c), 9) + tag(p.X(math.pi / 2) + 18, p.Y(c) - 8, f'c = {num} ÷ π = {c:.3f}', O, 14, 'start')
    s += txt(p.X(1.5 * math.pi), p.Y(-.35), 'error', 15, G, 900)
    s += tag(250, 352, f'÷ ‖φ‖² = π, not ÷ ‖φ‖ = {math.sqrt(K):.2f}', B, 14)
    s += txt(p.X(1.5 * math.pi), p.Y(1.05), f'one sine keeps {share * 100:.0f} %', 14, INK, 800)
    return 'Best sine for a square wave', s
D['ec-signals-u1-L4'] = (u1L4, '÷ ‖φ‖², the energy', '1.7.1')


# ---------------- unit 2 ----------------
def u2L1():
    T = lambda v: 3 * v + 2
    x1, x2, a, b = 1, 2, 2, 3
    comb = a * x1 + b * x2                      # 8
    p1 = T(comb)                                # 26
    p2 = a * T(x1) + b * T(x2)                  # 34
    s = defs()
    s += txt(10, 26, 'combine first', 14, MUT, 800, 'start')
    s += box(10, 40, 150, 62, f'{a}·{x1} + {b}·{x2} = {comb}', B, 15)
    s += line(160, 71, 192, 71, MUT, 3, arrow=True)
    s += box(195, 40, 130, 62, '3x + 2', INK, 20, sw=3)
    s += line(325, 71, 357, 71, MUT, 3, arrow=True)
    s += box(360, 40, 140, 62, f'{p1}', G, 26, fill=GS)
    s += txt(10, 146, 'each alone, then combine', 14, MUT, 800, 'start')
    s += box(10, 160, 150, 50, f'T{{{x1}}} = {T(x1)}', B, 16)
    s += box(10, 222, 150, 50, f'T{{{x2}}} = {T(x2)}', B, 16)
    s += line(160, 185, 192, 205, MUT, 3, arrow=True) + line(160, 247, 192, 228, MUT, 3, arrow=True)
    s += box(195, 185, 130, 62, f'{a}·{T(x1)} + {b}·{T(x2)}', INK, 16, sw=3)
    s += line(325, 216, 357, 216, MUT, 3, arrow=True)
    s += box(360, 185, 140, 62, f'{p2}', O, 26, fill=OS)
    s += tag(250, 330, f'{p1} ≠ {p2}: not linear', O, 18)
    s += txt(250, 365, f'0 in → {T(0)} out', 14, MUT, 800)
    return 'The two-path test', s
D['ec-signals-u2-L1'] = (u2L1, f'26 ≠ 34', '2.1.1')


def u2L2():
    h = lambda t: 1 / math.pi if abs(t) < 1e-9 else math.sin(t) / (math.pi * t)
    def absarea(Tm, n=200000):
        dt = 2 * Tm / n
        return sum(abs(h(-Tm + (i + .5) * dt)) for i in range(n)) * dt
    def netarea(Tm, n=200000):
        dt = 2 * Tm / n
        return sum(h(-Tm + (i + .5) * dt) for i in range(n)) * dt
    A20, A200, A2000 = absarea(20, 40000), absarea(200, 200000), absarea(2000, 800000)
    N2000 = netarea(2000, 800000)
    p = Plot(-20, 20, -.12, .36, L=50, T=24, Wd=430, H=210)
    s = defs()
    lobes = [k * math.pi for k in range(-6, 7)] + [-20, 20]
    lobes = sorted(set(min(20, max(-20, v)) for v in lobes))
    for a_, b_ in zip(lobes, lobes[1:]):
        m = h((a_ + b_) / 2)
        s += area(p, h, a_, b_, G if m > 0 else O, 30, .45)
    s += sax(p, xt=(-20, -10, 0, 10, 20), yt=(-.1, 0, .1, .2, .3), xl='t →', yl='h(t)')
    s += p.curve(h, -20, 20, n=240, c=B, w=4.5)
    s += tag(p.X(-19.5), p.Y(.33), f'h = sin t ÷ πt', B, 13, 'start')
    s += tag(p.X(19.5), p.Y(.33), f'net area = {N2000:.2f}', G, 13, 'end')
    s += txt(250, 314, f'∫|h| over ±20: {A20:.1f}  ·  ±200: {A200:.1f}  ·  ±2000: {A2000:.1f}', 14, INK, 800)
    s += tag(250, 354, '∫|h| grows forever: not stable', O, 16)
    return 'The ideal low-pass h(t)', s
D['ec-signals-u2-L2'] = (u2L2, 'net area 1, |area| ∞', '2.5')


def u2L3():
    # y'' + 3y' + 2y = u  ->  x1' = x2, x2' = -2 x1 - 3 x2 + u
    a1, a0 = 3, 2
    A = [[0, 1], [-a0, -a1]]
    s = defs()
    yc = 70
    s += txt(14, yc + 6, 'u', 20, INK, 900)
    s += line(28, yc, 64, yc, INK, 3, arrow=True)
    s += f'<circle cx="84" cy="{yc}" r="20" fill="{W}" stroke="{INK}" stroke-width="3"/>' + txt(84, yc + 7, 'Σ', 20, INK, 900)
    s += line(104, yc, 138, yc, INK, 3, arrow=True)
    s += box(140, yc - 24, 62, 48, '∫', B, 24, fill=BS)
    s += line(202, yc, 278, yc, INK, 3, arrow=True) + txt(240, yc - 12, 'x₂ = y′', 14, B, 900)
    s += box(280, yc - 24, 62, 48, '∫', B, 24, fill=BS)
    s += line(342, yc, 480, yc, INK, 3, arrow=True) + txt(400, yc - 12, 'x₁ = y', 14, B, 900)
    # feedback paths
    s += poly([(240, yc), (240, 140), (84, 140)], O, 3) + box(140, 124, 60, 32, f'× {a1}', O, 15, fill=OS)
    s += poly([(420, yc), (420, 190), (84, 190)], O, 3) + box(280, 174, 60, 32, f'× {a0}', O, 15, fill=OS)
    s += line(84, 190, 84, yc + 22, O, 3, arrow=True)
    s += txt(104, yc + 40, '−', 22, O, 900)
    for x in (240, 420): s += dot(x, yc, 6, INK, W, 2)
    s += txt(120, 292, 'A =', 22, INK, 900, 'end')
    s += grid(136, 240, [[g(v) for v in r] for r in A], cell=58, size=20, gap=6,
              hl={(1, 0): (O, W), (1, 1): (O, W)})
    s += tag(276, 312, 'last row: −2, −3', O, 15, 'start')
    s += rtxt(276, 268, 'B = [0, 1]^{T},  C = [1, 0]', 14, MUT, 800, 'start')
    return "y″ + 3y′ + 2y = u", s
D['ec-signals-u2-L3'] = (u2L3, 'signs flip: −2, −3', '2.7.1')


# ---------------- unit 3 ----------------
def u3L1():
    T0 = 4
    c = lambda n: .5 if n == 0 else math.sin(n * math.pi / 2) / (n * math.pi)
    env = lambda f: .5 if abs(f) < 1e-9 else math.sin(f * math.pi / 2) / (f * math.pi)
    p = Plot(-7.5, 7.5, -.15, .6, L=50, T=30, Wd=430, H=220)
    s = defs() + sax(p, xt=(-6, -4, -2, 0, 2, 4, 6), yt=(-.1, 0, .1, .2, .3, .4, .5), xl='harmonic n →', yl='cₙ')
    s += p.curve(env, -7.5, 7.5, n=200, c=MUT, w=2.5, dash='7 6')
    for n in range(-7, 8):
        v = c(n); x, y = p.P(n, v)
        col = G if v > 1e-9 else (O if v < -1e-9 else B)
        if abs(v) < 1e-9: s += hollow(x, p.Y(0), B, 6)
        else: s += line(x, p.Y(0), x, y, col, 4.5) + dot(x, y, 7, col, W, 2)
    s += tag(p.X(0) + 14, p.Y(.5) + 4, 'c₀ = 1/2', G, 13, 'start')
    s += tag(p.X(1) + 18, p.Y(c(1)) - 14, f'c₁ = 1/π = {c(1):.3f}', G, 13, 'start')
    s += tag(p.X(3), p.Y(c(3)) + 32, f'c₃ = {c(3):.3f}'.replace('-', '−'), O, 13)
    s += tag(250, 362, f'1/T₀ = 1/{T0}: with 2/T₀, c₁ = {2 * c(1):.3f} ✗', B, 14)
    return 'The pulse train’s lines', s
D['ec-signals-u3-L1'] = (u3L1, '1/T₀ in front of cₙ', '3.1.1')


def u3L2():
    X = lambda w: 1 / math.hypot(1, w)      # e^-t u(t)
    H = lambda w: 1 / math.hypot(2, w)      # e^-2t u(t)
    Y = lambda w: X(w) * H(w)
    tpk = math.log(2); ypk = math.exp(-tpk) - math.exp(-2 * tpk)   # 0.25
    p = Plot(0, 6, 0, 1.05, L=50, T=24, Wd=430, H=220)
    s = defs() + sax(p, xt=(0, 1, 2, 3, 4, 5, 6), yt=(0, .25, .5, .75, 1), xl='ω (rad/s) →', yl='magnitude')
    s += p.curve(X, 0, 6, c=G, w=5) + p.curve(H, 0, 6, c=B, w=5) + p.curve(Y, 0, 6, c=O, w=6)
    s += line(p.X(1), p.T, p.X(1), p.Y(0), MUT, 2, '5 6')
    for f, col in ((X, G), (H, B), (Y, O)): s += dot(*p.P(1, f(1)), 8, col)
    s += rtag(p.X(6), p.Y(1) + 4, '|X| of e^{−t}', G, 13, 'end')
    s += rtag(p.X(6), p.Y(.84) + 4, '|H| of e^{−2t}', B, 13, 'end')
    s += tag(p.X(6), p.Y(.68) + 4, '|Y| = |X| × |H|', O, 13, 'end')
    s += tag(250, 316, f'at ω = 1: {X(1):.3f} × {H(1):.3f} = {Y(1):.3f}', O, 14)
    s += rtxt(250, 356, f'back in time: y = e^{{−t}} − e^{{−2t}}, peak {ypk:.2f}', 14, MUT, 800)
    return 'Convolution, seen in ω', s
D['ec-signals-u3-L2'] = (u3L2, '∗ in time = × in ω', '3.3')


def u3L3():
    K, wc, td = 2, 2000, 1e-3
    gain = lambda w: K if abs(w) <= wc else 0
    ph = lambda w: -w * td
    w0 = 1000
    y0 = K * math.cos(-w0 * td)       # value at t = 0: 1.08 V
    p = Plot(-3000, 3000, 0, 2.6, L=50, T=14, Wd=430, H=110)
    s = defs() + sax(p, xt=(), yt=(0, 2), yl='gain')
    s += poly([p.P(-3000, 0), p.P(-2000, 0), p.P(-2000, 2), p.P(2000, 2), p.P(2000, 0), p.P(3000, 0)], G, 5)
    s += tag(p.X(2000) + 6, p.Y(2) + 4, 'flat: 2', G, 13, 'start')
    q = Plot(-3000, 3000, -2.6, 2.6, L=50, T=172, Wd=430, H=150)
    s += sax(q, xt=(-2000, -1000, 0, 1000, 2000), yt=(-2, -1, 0, 1, 2), yl='phase (rad)', xl='ω (rad/s) →',
             xfmt=lambda v: g(v))
    s += poly([q.P(-2000, ph(-2000)), q.P(2000, ph(2000))], B, 5)
    s += line(q.X(w0), q.Y(0), q.X(w0), q.Y(ph(w0)), MUT, 2, '5 6') + dot(*q.P(w0, ph(w0)), 9, O)
    s += tag(q.X(w0) + 14, q.Y(ph(w0)) + 4, f'−{w0 * td:g} rad at {w0}', O, 13, 'start')
    s += tag(q.X(-2950), q.Y(-1.6), 'straight line', B, 13, 'start')
    s += txt(250, 372, f'cos 1000t → 2 cos(1000t − 1): {y0:.2f} V at t = 0', 13, INK, 800)
    return 'Gain AND phase', s
D['ec-signals-u3-L3'] = (u3L3, 'straight phase too', '3.6.1')


# ---------------- unit 4 ----------------
def splane(x0, y0, w, h, s0, s1, w0, w1):
    X = lambda v: x0 + (v - s0) / (s1 - s0) * w
    Y = lambda v: y0 + h - (v - w0) / (w1 - w0) * h
    return X, Y


def u4L1():
    pole = -2
    s = defs()
    s += box(120, 0, 280, 46, 'both: X(s) = 1/(s + 2)', INK, 18, sw=3)
    for i, (sig, side, col, roc) in enumerate((('e^{−2t} u(t)', 1, G, 'Re s > −2'), ('−e^{−2t} u(−t)', -1, O, 'Re s < −2'))):
        x0 = 14 + i * 256; y0 = 92
        X, Y = splane(x0, y0, 236, 190, -4.5, 2, -3, 3)
        if side > 0: s += rect(X(pole), y0, X(2) - X(pole), 190, GS if col == G else OS, 'none', 0, 0)
        else: s += rect(X(-4.5), y0, X(pole) - X(-4.5), 190, OS, 'none', 0, 0)
        s += line(X(pole), y0, X(pole), y0 + 190, col, 2.5, '6 6')
        s += line(x0, Y(0), x0 + 236, Y(0), MUT, 2.5, arrow=True) + line(X(0), y0 + 190, X(0), y0 - 4, MUT, 2.5, arrow=True)
        s += txt(X(0) + 6, y0 + 12, 'jω', 13, MUT, 800, 'start') + txt(x0 + 230, Y(0) + 20, 'σ', 13, MUT, 800, 'end')
        s += cross(X(pole), Y(0), INK, 9, 4.5) + txt(X(pole), Y(0) + 26, '−2', 13, INK, 800)
        s += rtxt(x0 + 118, y0 - 12, sig, 18, col, 900)
        s += tag(x0 + 118, y0 + 228, roc, col, 15)
    return 'One pole, two regions', s
D['ec-signals-u4-L1'] = (u4L1, 'ROC picks the signal', '4.1.1')


def u4L2():
    coeffs = [1, 1, 1, 1]           # s^3 + s^2 + s + 1
    # roots of (s + 1)(s^2 + 1), checked by expanding back
    roots = [-1 + 0j, 1j, -1j]
    expand = [1]
    for r in roots: expand = [a - r * b for a, b in zip(expand + [0], [0] + expand)]
    assert all(abs(a - b) < 1e-12 for a, b in zip(expand, coeffs))
    X, Y = splane(30, 40, 460, 230, -3, 1.6, -1.8, 1.8)
    s = defs() + rect(X(-3), 40, X(0) - X(-3), 230, GS, 'none', 0, 0)
    s += txt(X(-2.4), 64, 'stable side', 14, G, 900)
    s += line(30, Y(0), 490, Y(0), MUT, 2.5, arrow=True) + line(X(0), 270, X(0), 34, MUT, 2.5, arrow=True)
    s += txt(X(0) + 8, 48, 'jω', 14, MUT, 800, 'start') + txt(486, Y(0) + 22, 'σ', 14, MUT, 800, 'end')
    for r in roots:
        on_axis = abs(r.real) < 1e-12
        s += cross(X(r.real), Y(r.imag), O if on_axis else G, 11, 5)
        lab = ('+j' if r.imag > 0 else '−j') if on_axis else g(r.real)
        s += txt(X(r.real) + (18 if on_axis else 0), Y(r.imag) + (6 if on_axis else 30), lab, 15, O if on_axis else G, 900, 'start' if on_axis else 'middle')
    s += tag(X(0) + 52, Y(1) + 6, 'on the jω axis', O, 13, 'start')
    s += box(60, 296, 400, 44, 's³ + s² + s + 1 = (s + 1)(s² + 1)', INK, 17, sw=2.5)
    s += txt(260, 370, 'every coefficient positive, yet poles at ±j', 14, MUT, 800)
    return 'Where the poles really are', s
D['ec-signals-u4-L2'] = (u4L2, '±j poles: not stable', '4.4')


# ---------------- unit 5 ----------------
def u5L1():
    fs = 1000
    base = [(200, 3), (450, 2)]
    fmax = max(f for f, _ in base)
    lines_ = [(f, a / 2, G) for f, a in base] + [(fs - f, a / 2, B) for f, a in base] + [(fs + f, a / 2, B) for f, a in base]
    p = Plot(0, 1600, 0, 2.3, L=40, T=60, Wd=450, H=170)
    s = defs()
    gb0, gb1 = fmax, fs - fmax
    s += rect(p.X(gb0), p.T, p.X(gb1) - p.X(gb0), p.H, OS, 'none', 0, 4)
    s += poly([p.P(0, 1.9), p.P(fs / 2, 1.9), p.P(fs / 2, 0)], INK, 3, '8 6')
    s += sax(p, xt=(0, 200, 450, 1000, 1450), yt=(), xl='f (Hz) →')
    for f, a, c in lines_:
        x, y = p.P(f, a); s += line(x, p.Y(0), x, y, c, 5) + dot(x, y, 7, c, W, 2)
    s += txt(p.X(500), p.Y(1.9) - 10, 'filter to 500', 13, INK, 800)
    s += tag(250, 26, f'Nyquist rate = 2 × {fmax} = {2 * fmax} Hz: the signal', G, 14)
    s += tag(250, 318, f'Nyquist frequency = {fs} ÷ 2 = {fs // 2} Hz: the sampler', B, 14)
    s += txt(250, 358, f'fs = {fs} Hz > {2 * fmax} Hz, guard band {gb0}–{gb1} Hz', 14, INK, 900)
    return 'Spectrum sampled at 1 kHz', s
D['ec-signals-u5-L1'] = (u5L1, 'rate ≠ frequency', '5.1.1')


def u5L2():
    fs, fL, fH = 2.45, 5.0, 6.0
    zw = fs / 2
    zone = math.floor(fL / zw) + 1          # 5
    copies = []
    for k in range(-4, 5):
        for a, b in ((fL, fH), (-fH, -fL)):
            lo, hi = a + k * fs, b + k * fs
            if hi > 0 and lo < 6.3 and not (k == 0 and a > 0): copies.append((max(lo, 0), hi))
    copies.sort()
    for (a, b), (c, d) in zip(copies, copies[1:]): assert b < c + 1e-9
    p = Plot(0, 6.6, 0, 1.4, L=24, T=50, Wd=470, H=170)
    s = defs()
    for z in range(1, 6):
        s += line(p.X(z * zw), p.T - 6, p.X(z * zw), p.Y(0), MUT, 2, '5 6')
        s += txt(p.X((z - .5) * zw), p.T - 12, f'zone {z}' if z == zone else str(z), 13, G if z == zone else MUT, 900)
    s += sax(p, xt=(0, 1, 2, 3, 4, 5, 6), yt=(), xl='f (kHz) →')
    for a, b in copies:
        s += rect(p.X(a), p.Y(.8), p.X(b) - p.X(a), p.Y(0) - p.Y(.8), BS, B, 2.5, 6)
    s += rect(p.X(fL), p.Y(1.1), p.X(fH) - p.X(fL), p.Y(0) - p.Y(1.1), GS, G, 3, 6)
    s += txt(p.X(5.5), p.Y(.55), 'band', 14, G, 900)
    lo0 = copies[0]
    s += tag(p.X(lo0[0]) + 2, p.Y(1.08), f'copy: {lo0[0]:.1f}–{lo0[1]:.1f} kHz', B, 13, 'start')
    s += tag(250, 316, f'fs = {fs} kHz: zone {zone} = {(zone - 1) * zw:.1f} to {zone * zw:.3f} kHz', G, 14)
    s += txt(250, 356, f'below 2 × {fH:g} = {2 * fH:g} kHz, yet nothing overlaps', 14, INK, 800)
    return 'Copies fill the empty gaps', s
D['ec-signals-u5-L2'] = (u5L2, 'band fits one zone', '5.3.1')


def u5L3():
    N = list(range(0, 10))
    Su = [n + 1 for n in N]                                     # sum of |u[k]|
    Sh = [sum(.5 ** k for k in range(n + 1)) for n in N]        # sum of |0.5^k|
    p = Plot(-.5, 9.5, 0, 11, L=46, T=40, Wd=440, H=220)
    s = defs() + sax(p, xt=N, yt=(0, 2, 4, 6, 8, 10), xl='terms added, n →', yl='Σ |h[k]|')
    s += line(p.L, p.Y(2), p.L + p.W, p.Y(2), G, 2, '6 6')
    s += poly([p.P(n, v) for n, v in zip(N, Su)], O, 4) + poly([p.P(n, v) for n, v in zip(N, Sh)], G, 4)
    for n, a, b in zip(N, Su, Sh): s += dot(*p.P(n, a), 7, O) + dot(*p.P(n, b), 7, G)
    s += tag(p.X(5.3), p.Y(9.6), 'h = u[n]: n + 1 → ∞', O, 14, 'end')
    s += rtag(p.X(9.4), p.Y(3.3), 'h = 0.5^{n} u[n]: → 2', G, 14, 'end')
    s += tag(250, 352, 'every term is 1, the sum never stops', O, 14)
    return 'Add up |h[n]|', s
D['ec-signals-u5-L3'] = (u5L3, 'Σ|h| = ∞: not stable', '5.5')


# ---------------- unit 6 ----------------
def u6L1():
    Np = 8
    x = [1, 1, 1, 0, 0, 0, 0, 0]
    X = [sum(x[n] * cmath.exp(-2j * math.pi * k * n / Np) for n in range(Np)) for k in range(Np)]
    mag = [abs(v) for v in X]
    s = defs()
    s += txt(16, 24, 'x[n]: 1, 1, 1, 0, 0, 0, 0, 0 …', 15, B, 900, 'start')
    yb = 92
    s += line(20, yb, 500, yb, MUT, 2.5, arrow=True)
    s += stems(None, [x[n % Np] for n in range(16)], 34, 29, yb, 40, B, 5)
    s += txt(20, 140, '|X[k]|, k = 0 to 11', 15, O, 900, 'start')
    yb2 = 330
    s += line(20, yb2, 500, yb2, MUT, 2.5, arrow=True)
    ks = list(range(12))
    s += stems(None, [mag[k % Np] for k in ks], 40, 38, yb2, 46, O, 7, labels=True, size=12, fmt=lambda v: f'{v:.2f}'.rstrip('0').rstrip('.'))
    for k in ks: s += txt(40 + k * 38, yb2 + 20, str(k), 12, MUT, 700)
    s += tag(108, yb2 - 46 * mag[0] - 4, f'X[0] = {mag[0]:.0f}: the sum', O, 13, 'start')
    s += tag(500, 140, f'1/N = 1/{Np} goes in x[n]', B, 14, 'end')
    return 'A pulse that repeats every 8', s
D['ec-signals-u6-L1'] = (u6L1, 'X[0] = 3, not 0.375', '6.1.1')


def u6L2():
    x, h = [1, 2, 3, 4], [1, 1, 0, 0]
    Nn = 4
    lin = [sum(x[k] * h[n - k] for k in range(len(x)) if 0 <= n - k < len(h)) for n in range(len(x) + 2 - 1)]
    lin = [v for v in lin]                      # 1, 3, 5, 7, 4
    circ = [sum(x[k] * h[(n - k) % Nn] for k in range(Nn)) for n in range(Nn)]   # 5, 3, 5, 7
    assert circ[0] == lin[0] + lin[4]
    s = defs()
    x0, dx, k = 80, 80, 13
    rows = ((150, lin, B, f'linear: {len(lin)} samples'), (330, circ, O, f'{Nn}-point circular'))
    for yb, vals, c, lab in rows:
        s += line(40, yb, 500, yb, MUT, 2.5, arrow=True)
        s += stems(None, vals, x0, dx, yb, k, c, 7, labels=True, size=14)
        for i in range(len(vals)): s += txt(x0 + i * dx, yb + 20, str(i), 12, MUT, 700)
        s += txt(20, yb - 110, lab, 15, c, 900, 'start')
    xa, ya = x0 + 4 * dx, 150 - k * lin[4]
    xb, yb_ = x0, 330 - k * circ[0]
    s += f'<path d="M{xa:.1f},{150 + 26:.1f} C{xa:.1f},{250:.1f} {xb + 60:.1f},{200:.1f} {xb + 12:.1f},{yb_ - 22:.1f}" fill="none" stroke="{O}" stroke-width="3.5" stroke-dasharray="7 6" marker-end="url(#ao)"/>'
    s += tag(xb + 100, 196, f'tail {lin[4]} wraps: {lin[0]} + {lin[4]} = {circ[0]}', O, 13, 'start')
    s += txt(250, 372, 'x = 1, 2, 3, 4  ·  h = 1, 1, 0, 0', 13, MUT, 800)
    return 'The tail that wraps round', s
D['ec-signals-u6-L2'] = (u6L2, 'zero-pad to ≥ 5 points', '6.3')


def u6L3():
    pole, zero = 1.0, 0.0
    hn = [1] * 7                      # h[n] = u[n]
    cx, cy, R = 170, 196, 118
    s = defs()
    # ROC |z| > 1: everything outside the circle (even-odd cut-out)
    s += (f'<path d="M20,46 H330 V352 H20 Z M{cx - R},{cy} a{R},{R} 0 1,0 {2 * R},0 a{R},{R} 0 1,0 {-2 * R},0 Z" '
          f'fill="{OS}" fill-rule="evenodd" stroke="none"/>')
    s += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{B}" stroke-width="3.5"/>'
    s += line(20, cy, 334, cy, MUT, 2.5, arrow=True) + line(cx, 352, cx, 42, MUT, 2.5, arrow=True)
    s += txt(cx + 8, 58, 'Im z', 13, MUT, 800, 'start') + txt(330, cy + 22, 'Re z', 13, MUT, 800, 'end')
    s += hollow(cx + zero * R, cy, B, 9)
    s += cross(cx + pole * R, cy, O, 12, 5.5)
    s += txt(cx + pole * R - 6, cy - 22, 'pole at 1', 14, O, 900, 'end')
    s += txt(cx - 52, cy - 48, '|z| = 1', 14, B, 900)
    s += tag(cx, 26, 'ROC |z| > 1 misses the circle', O, 14)
    s += txt(424, 92, 'H(z) = z ÷ (z − 1)', 14, INK, 900)
    s += txt(424, 124, 'h[n] = u[n]', 14, B, 900)
    yb = 230
    s += line(350, yb, 506, yb, MUT, 2.5, arrow=True)
    s += stems(None, hn, 362, 22, yb, 60, B, 5)
    s += txt(424, 280, f'Σ|h| = 1 + 1 + 1 + …', 14, INK, 800)
    s += tag(424, 324, 'not stable', O, 15)
    return 'A pole on the unit circle', s
D['ec-signals-u6-L3'] = (u6L3, 'pole at 1: not BIBO', '6.7')
