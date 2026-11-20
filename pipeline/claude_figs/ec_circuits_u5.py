"""Claude's hand-drawn figures for ec-circuits-u5 (transient analysis and the Laplace transform), one per chapter.
Every number comes from that chapter's own worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
W = INK  # wires


def sb(n, s, after='', size=13):
    """a name with a subscript inside an svg text: v sub C"""
    return f'{n}<tspan dy="4" font-size="{size}">{s}</tspan><tspan dy="-4">{after}</tspan>'


def wire(pts, c=W, w=2):
    return P(pts, c, w)


def dot(x, y, c=W):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" style="fill:{c}"/>'


def _frame(p1, p2, length):
    (x1, y1), (x2, y2) = p1, p2
    d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    s = (mx - ux * length / 2, my - uy * length / 2); e = (mx + ux * length / 2, my + uy * length / 2)
    return ux, uy, -uy, ux, s, e, (mx, my)


def lab(p, txt, side, size=14, fill=INK, off=20, bold=False):
    x, y = p
    if side == 'u': return T(x, y - off + 4, txt, size, fill=fill, bold=bold)
    if side == 'd': return T(x, y + off + 6, txt, size, fill=fill, bold=bold)
    if side == 'l': return T(x - off, y + 5, txt, size, 'end', fill, bold)
    return T(x + off, y + 5, txt, size, 'start', fill, bold)


def res(p1, p2, txt='', side='u', c=W, L_=44, off=20):
    ux, uy, nx, ny, s, e, m = _frame(p1, p2, L_)
    pts = [s]
    for i in range(1, 12):
        t = i / 12; a = 7 * (1 if i % 2 else -1) if i < 12 else 0
        pts.append((s[0] + ux * L_ * t + nx * a, s[1] + uy * L_ * t + ny * a))
    pts.append(e)
    return wire([p1, s], W) + P(pts, c, 2.2) + wire([e, p2], W) + (lab(m, txt, side, off=off) if txt else '')


def ind(p1, p2, txt='', side='u', c=W, n=4, r=6, off=20):
    L_ = 2 * r * n
    ux, uy, nx, ny, s, e, m = _frame(p1, p2, L_)
    d = f'M{s[0]:.1f},{s[1]:.1f}'
    for i in range(n):
        d += f' a{r},{r} 0 0 1 {ux * 2 * r:.1f},{uy * 2 * r:.1f}'
    return wire([p1, s], W) + f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:2.2"/>' + wire([e, p2], W) + (lab(m, txt, side, off=off) if txt else '')


def cap(p1, p2, txt='', side='r', c=W, gap=10, plate=26, off=22):
    ux, uy, nx, ny, s, e, m = _frame(p1, p2, gap)
    pl = lambda q: L(q[0] - nx * plate / 2, q[1] - ny * plate / 2, q[0] + nx * plate / 2, q[1] + ny * plate / 2, c, 3)
    return wire([p1, s], W) + pl(s) + pl(e) + wire([e, p2], W) + (lab(m, txt, side, off=off) if txt else '')


def vsrc(p1, p2, txt='', side='l', c=W, r=15, off=24, ac=False):
    """voltage source; + at the p1 end"""
    ux, uy, nx, ny, s, e, m = _frame(p1, p2, 2 * r)
    o = wire([p1, s], W) + wire([e, p2], W)
    o += f'<circle cx="{m[0]:.1f}" cy="{m[1]:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2.2"/>'
    if ac:
        o += f'<path d="M{m[0] - 8:.1f},{m[1]:.1f} q4,-9 8,0 t8,0" style="fill:none;stroke:{c};stroke-width:2"/>'
    else:
        o += T(m[0] - ux * 6, m[1] - uy * 6 + 5, '+', 14, fill=c, bold=True) + T(m[0] + ux * 7, m[1] + uy * 7 + 5, '−', 14, fill=c, bold=True)
    return o + (lab(m, txt, side, off=off) if txt else '')


def isrc(p1, p2, txt='', side='l', c=W, r=15, off=24, arrow='n'):
    """current source, arrow pointing from p1 to p2"""
    ux, uy, nx, ny, s, e, m = _frame(p1, p2, 2 * r)
    o = wire([p1, s], W) + wire([e, p2], W)
    o += f'<circle cx="{m[0]:.1f}" cy="{m[1]:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2.2"/>'
    o += L(m[0] - ux * 9, m[1] - uy * 9, m[0] + ux * 7, m[1] + uy * 7, c, 2.2, arrow=arrow)
    return o + (lab(m, txt, side, off=off) if txt else '')


def zbox(p1, p2, txt='', side='r', c=AC, l=40, wdt=16, off=18):
    """an impedance drawn as a box"""
    ux, uy, nx, ny, s, e, m = _frame(p1, p2, l)
    w_, h_ = (l, wdt) if abs(ux) > 0.5 else (wdt, l)
    o = wire([p1, s], W) + wire([e, p2], W) + f'<rect x="{m[0] - w_ / 2:.1f}" y="{m[1] - h_ / 2:.1f}" width="{w_:.1f}" height="{h_:.1f}" style="fill:var(--fig);stroke:{c};stroke-width:2.2"/>'
    return o + (lab(m, txt, side, off=off) if txt else '')


def gap(p1, p2, txt='', side='r', c=W, g=18, off=14):
    """an open circuit: two stubs and a gap"""
    ux, uy, nx, ny, s, e, m = _frame(p1, p2, g)
    return wire([p1, s], W) + wire([e, p2], W) + C(s[0], s[1], 3, c) + C(e[0], e[1], 3, c) + (lab(m, txt, side, 13, c, off) if txt else '')


def cur(x1, y1, x2, y2, txt='', side='u', c=AC, size=13, off=14):
    """a current arrow beside a wire"""
    o = L(x1, y1, x2, y2, c, 2, arrow='n' if c == AC else ('l' if c == LV else 'x'))
    return o + (lab(((x1 + x2) / 2, (y1 + y2) / 2), txt, side, size, c, off) if txt else '')


def panel(x, y, w, h, title, sub_=None):
    o = R(x, y, w, h, FIGBG, L2, 8, 1.2) + T(x + w / 2, y + 22, title, 15, bold=True)
    if sub_: o += T(x + w / 2, y + 41, sub_, 13, fill=MUT)
    return o


# ---- 5.1: the circuit before, just after and long after the switch ----
def f1():
    o = []
    # top: the original circuit, t < 0
    o.append(R(8, 8, 704, 196, FIGBG, L2, 8, 1.2))
    yt, yb = 84, 180
    xs, x1, x2, xa, xr = 110, 150, 270, 420, 510
    o.append(vsrc((xs, yt), (xs, yb), '10 V', 'l'))
    o.append(wire([(xs, yt), (x1, yt)]))
    o.append(res((x1, yt), (x2 - 10, yt), 'R₁ = 2 Ω', 'd'))
    o.append(ind((x2 - 10, yt), (xa - 30, yt), 'L = 1 H', 'd'))
    o.append(wire([(xa - 30, yt), (xr, yt)]))
    o.append(cap((xa, yt), (xa, yb), 'C = 0.25 F', 'l', off=20))
    o.append(res((xr, yt), (xr, yb), 'R₂ = 3 Ω', 'r'))
    o.append(wire([(xs, yb), (xr, yb)]))
    o.append(dot(xa, yt) + dot(xa, yb) + T(xa + 5, yt - 9, 'a', 14, 'start', MUT, italic=True))
    # switch S across R1, drawn open above it
    ys = 54
    o.append(wire([(x1 + 4, yt), (x1 + 4, ys), (x1 + 36, ys)]) + wire([(x2 - 50, ys), (x2 - 14, ys), (x2 - 14, yt)]))
    o.append(L(x1 + 36, ys, x2 - 52, ys - 14, AC, 2.5) + C(x1 + 36, ys, 3, AC) + C(x2 - 50, ys, 3, AC))
    o.append(T((x1 + x2) / 2 - 6, 30, 'S closes at t = 0', 13, fill=AC))
    o.append(T(610, 82, 't &lt; 0, steady', 15, 'start', INK, True))
    o.append(T(610, 110, sb('i', 'L', '(0⁻) = 2 A'), 15, 'start', AC, True))
    o.append(T(610, 136, sb('v', 'C', '(0⁻) = 6 V'), 15, 'start', AC, True))
    o.append(T(610, 162, 'L short, C open', 13, 'start', MUT))
    # bottom left: t = 0+
    o.append(panel(8, 214, 348, 236, 't = 0⁺', 'S closed; L and C become sources'))
    yt, yb = 292, 412
    xs, xl, xa, xr = 44, 130, 222, 306
    o.append(vsrc((xs, yt), (xs, yb), '10 V', 'r', off=22))
    o.append(isrc((xs, yt), (xl + 30, yt), '', c=LV))
    o.append(T(xl - 10, yt - 22, sb('i', 'L', ' = 2 A'), 14, fill=LV, bold=True))
    o.append(wire([(xl + 30, yt), (xr, yt)]))
    o.append(vsrc((xa, yt), (xa, yb), '', c=LV))
    o.append(T(xa - 20, (yt + yb) / 2 + 5, '6 V', 14, 'end', LV, True))
    o.append(res((xr, yt), (xr, yb), '3 Ω', 'r', off=14))
    o.append(wire([(xs, yb), (xr, yb)]))
    o.append(dot(xa, yt) + dot(xa, yb))
    o.append(T(xa + 22, yt + 24, sb('i', 'C', ' = 0'), 13, 'start', AC, True))
    o.append(cur(xr - 26, yt + 46, xr - 26, yt + 78, '2 A', 'l', off=8))
    o.append(T(182, 438, sb('v', 'L', '(0⁺) = 10 − 6 = 4 V'), 14, fill=AC, bold=True))
    # bottom right: t -> infinity
    o.append(panel(364, 214, 348, 236, 't → ∞', 'S closed; L short, C open'))
    xs, xl, xa, xr = 400, 470, 578, 662
    o.append(vsrc((xs, yt), (xs, yb), '10 V', 'r', off=22))
    o.append(wire([(xs, yt), (xr, yt)], NX, 3))
    o.append(T(xl + 8, yt - 12, 'L: short', 13, fill=NX, bold=True))
    o.append(gap((xa, yt), (xa, yb), 'C: open', 'l', NX, off=12))
    o.append(res((xr, yt), (xr, yb), '3 Ω', 'r', off=14))
    o.append(wire([(xs, yb), (xr, yb)]))
    o.append(T(538, 438, sb('i', 'L', '(∞) = 3.33 A,  ') + sb('v', 'C', '(∞) = 10 V'), 14, fill=NX, bold=True))
    return 458, ''.join(o)


FIG[1] = (f1, 'Top: the worked example before the switch, with the inductor carrying 2 A and the capacitor holding 6 V. Bottom left: just after S closes, the inductor acts as a 2 A source and the capacitor as a 6 V source, so 4 V appears across L. Bottom right: long after, L is a short and C is open.',
          'Three views of one circuit: a 10 volt source, R1 2 ohms with a switch across it, L 1 henry, and C 0.25 farad in parallel with R2 3 ohms. Before the switch i L is 2 amperes and v C is 6 volts; at 0 plus L is a 2 ampere source and C a 6 volt source; at infinity L is a short, C is open, i L is 3.33 amperes and v C is 10 volts.')


def plot(x0, x1, y0, y1, xr, yr, xt, yt, xlab, ylab, xfmt=lambda v: f'{v:g}', yfmt=lambda v: f'{v:g}'):
    """axes with ticks; returns (svg, fx, fy)"""
    fx = lambda v: x0 + (x1 - x0) * (v - xr[0]) / (xr[1] - xr[0])
    fy = lambda v: y1 - (y1 - y0) * (v - yr[0]) / (yr[1] - yr[0])
    o = [L(x0, fy(0) if yr[0] < 0 < yr[1] else y1, x1, fy(0) if yr[0] < 0 < yr[1] else y1, L2, 1.5), L(x0, y0, x0, y1, L2, 1.5)]
    for v in xt:
        X = fx(v); yb = y1
        o += [L(X, y1, X, y1 + 5, L2, 1.5), T(X, y1 + 20, xfmt(v), 13, fill=MUT)]
    for v in yt:
        Y = fy(v); o += [L(x0 - 5, Y, x0, Y, L2, 1.5), L(x0, Y, x1, Y, LN, 1), T(x0 - 9, Y + 4.5, yfmt(v), 13, 'end', MUT)]
    o.append(T((x0 + x1) / 2, y1 + 40, xlab, 14, fill=MUT))
    o.append(T(x0 - 4, y0 - 12, ylab, 14, 'start', MUT))
    return ''.join(o), fx, fy


def curve(f, a, b, fx, fy, c=AC, w=3, n=200, dash=None):
    return P([(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


# ---- 5.2: the RL decay of the worked example, with its tangent ----
def f2():
    o = []
    ax, fx, fy = plot(80, 690, 40, 250, (0, 25), (0, 2.2), [0, 5, 10, 15, 20, 25], [0, 0.5, 1, 1.5, 2], 't (ms)', 'i (A)')
    o.append(ax)
    o.append(L(fx(0), fy(2), fx(5), fy(0), MUT, 2, '6 4'))
    o.append(curve(lambda t: 2 * math.exp(-t / 5), 0, 25, fx, fy))
    o.append(L(fx(5), fy(0), fx(5), fy(0.7358), LV, 1.5, '3 3') + L(fx(0), fy(0.7358), fx(5), fy(0.7358), LV, 1.5, '3 3'))
    o.append(C(fx(5), fy(0.7358), 5, LV))
    o.append(Tb(fx(5) + 10, fy(0.7358) - 10, 'at t = τ = 5 ms: 0.736 A (36.8 % of 2 A)', 13, 'start', LV, True))
    o.append(L(fx(11.51), fy(0), fx(11.51), fy(0.2), NX, 1.5, '3 3'))
    o.append(C(fx(11.51), fy(0.2), 5, NX))
    o.append(Tb(fx(11.51) + 10, fy(0.2) - 12, '0.2 A at t = τ ln 10 = 11.5 ms', 13, 'start', NX, True))
    o.append(Tb(fx(3.2), fy(1.25), 'tangent at t = 0', 13, 'start', MUT))
    o.append(Tb(fx(1.6), fy(1.9), 'i = 2e⁻²⁰⁰ᵗ A', 14, 'start', AC, True))
    return 296, ''.join(o)


FIG[2] = (f2, 'The worked example: the coil current falls from 2 A as 2e⁻²⁰⁰ᵗ A. The tangent at t = 0 hits zero at t = τ = 5 ms, where the curve itself is at 36.8 % of 2 A; the current reaches 0.2 A at 11.5 ms.',
          'Plot of the current 2 e to the minus 200 t amperes from 0 to 25 milliseconds, with the starting tangent reaching zero at 5 milliseconds, the point 0.736 amperes at 5 milliseconds and 0.2 amperes at 11.5 milliseconds marked.')


# ---- 5.3: forced + natural = complete, for the RC step of the worked example ----
def f3():
    o = []
    ax, fx, fy = plot(80, 690, 36, 266, (0, 0.5), (-10.5, 11.5), [0, 0.1, 0.2, 0.3, 0.4, 0.5], [-10, -5, 0, 5, 10], 't (s)', sb('v', 'C', ' (V)'),
                      yfmt=lambda v: neg(f'{v:g}'))
    o.append(ax)
    o.append(L(fx(0), fy(10), fx(0.5), fy(10), NX, 2.5, '7 4'))
    o.append(curve(lambda t: -10 * math.exp(-10 * t), 0, 0.5, fx, fy, LV, 2.5, dash='4 3'))
    o.append(curve(lambda t: 10 * (1 - math.exp(-10 * t)), 0, 0.5, fx, fy, AC, 3.2))
    o.append(L(fx(0.1), fy(0), fx(0.1), fy(6.321), MUT, 1.2, '3 3') + C(fx(0.1), fy(6.321), 5, AC))
    o.append(Tb(fx(0.1) + 10, fy(6.321) + 18, 'at t = τ = 0.1 s: 6.32 V', 13, 'start', AC, True))
    o.append(Tb(fx(0.36), fy(10) - 12, 'forced part: 10 V', 13, 'middle', NX, True))
    o.append(Tb(fx(0.13), fy(-5.2), 'natural part: −10e⁻¹⁰ᵗ', 13, 'start', LV, True))
    o.append(Tb(fx(0.33), fy(7.3), 'complete: 10(1 − e⁻¹⁰ᵗ)', 13, 'middle', AC, True))
    return 310, ''.join(o)


FIG[3] = (f3, 'The worked example split into its parts: the forced part is the flat 10 V, the natural part −10e⁻¹⁰ᵗ V starts at −10 V and dies away, and their sum, the capacitor voltage, starts at 0 V and reaches 6.32 V at t = τ = 0.1 s.',
          'Plot from 0 to 0.5 seconds of the forced part 10 volts, the natural part minus 10 e to the minus 10 t, and their sum 10 times 1 minus e to the minus 10 t, which passes 6.32 volts at 0.1 seconds.')


# ---- 5.4: the three damping cases of the worked example ----
def f4():
    o = []
    ax, fx, fy = plot(80, 690, 40, 260, (0, 2), (0, 16), [0, 0.5, 1, 1.5, 2], [0, 5, 10, 15], 't (s)', sb('v', 'C', ' (V)'))
    o.append(ax)
    wd = math.sqrt(96); a2 = -20 / wd
    s1, s2 = -20 + math.sqrt(300), -20 - math.sqrt(300); A1 = -10 * s2 / (s2 - s1); A2 = -10 - A1
    o.append(L(fx(0), fy(10), fx(2), fy(10), MUT, 1.5, '6 4'))
    o.append(curve(lambda t: 10 - math.exp(-2 * t) * (10 * math.cos(wd * t) - a2 * math.sin(wd * t)), 0, 2, fx, fy, AC, 3, 400))
    o.append(curve(lambda t: 10 - 10 * (1 + 10 * t) * math.exp(-10 * t), 0, 2, fx, fy, LV, 3))
    o.append(curve(lambda t: 10 + A1 * math.exp(s1 * t) + A2 * math.exp(s2 * t), 0, 2, fx, fy, NX, 3))
    tp = math.pi / wd
    o.append(C(fx(tp), fy(10 + 10 * math.exp(-2 * tp)), 5, AC))
    o.append(Tb(fx(tp) + 12, fy(15.27) - 4, 'R = 4 Ω, ζ = 0.2: underdamped, peak 15.27 V at 0.321 s', 13, 'start', AC, True))
    o.append(L(fx(0.78), fy(12.4), fx(0.47), fy(9.95), LV, 1.2) + T(fx(0.78), fy(12.6), 'R = 20 Ω, ζ = 1: critically damped', 13, 'start', LV, True))
    o.append(L(fx(1.1), fy(4.6), fx(0.9), fy(8.0), NX, 1.2) + T(fx(1.1), fy(3.6), 'R = 40 Ω, ζ = 2: overdamped', 13, 'start', NX, True))
    o.append(Tb(fx(1.9), fy(10) - 10, 'final value 10 V', 13, 'end', MUT))
    return 304, ''.join(o)


FIG[4] = (f4, 'The worked example: the capacitor voltage of the same series circuit (L = 1 H, C = 0.01 F, 10 V step) for three resistances. With 4 Ω it overshoots to 15.27 V and rings; with 20 Ω it rises fastest without overshoot; with 40 Ω it creeps up slowly.',
          'Plot of capacitor voltage against time from 0 to 2 seconds for R equal to 4, 20 and 40 ohms: an underdamped curve peaking at 15.27 volts at 0.321 seconds, a critically damped curve and a slow overdamped curve, all settling to 10 volts.')


def cross(x, y, c=INK, r=7, w=3):
    return L(x - r, y - r, x + r, y + r, c, w) + L(x - r, y + r, x + r, y - r, c, w)


def ring(x, y, r=7, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2.5"/>'


# ---- 5.5: where the poles sit for each damping ratio, omega_n = 1000 rad/s ----
def f5():
    o = []
    k = 0.16  # px per rad/s
    ox, oy = 570, 200
    fx = lambda v: ox + v * k
    fy = lambda v: oy - v * k
    o.append(L(40, oy, 700, oy, L2, 1.5, arrow='m') + L(ox, 380, ox, 24, L2, 1.5, arrow='m'))
    o.append(T(696, oy + 22, 'σ', 15, 'end', MUT, italic=True) + T(ox + 10, 34, 'jω', 15, 'start', MUT, italic=True))
    # circle of radius omega_n in the left half plane
    r = 1000 * k
    o.append(f'<path d="M{ox:.1f},{oy - r:.1f} A{r:.1f},{r:.1f} 0 0 0 {ox:.1f},{oy + r:.1f}" style="fill:none;stroke:{L2};stroke-width:1.5;stroke-dasharray:6 4"/>')
    o.append(Tb(fx(-720), fy(745), 'radius ωₙ = 1000 rad/s', 13, 'end', MUT))
    # zeta = 0.1 (worked example)
    o.append(L(ox, oy, fx(-100), fy(995), AC, 1.5, '4 3'))
    o.append(cross(fx(-100), fy(995), AC) + cross(fx(-100), fy(-995), AC))
    o.append(Tb(fx(-100) - 14, fy(995) - 18, 'ζ = 0.1: −100 ± j995', 13, 'end', AC, True))
    o.append(L(fx(-100), fy(995) + 10, fx(-100), oy, AC, 1.2, '3 3'))
    o.append(Tb(fx(-50), oy - 12, 'ζωₙ = 100', 13, 'middle', AC))
    o.append(Tb(fx(-100) + 30, fy(500), sb('ω', 'd', ' = 995'), 13, 'start', AC))
    # zeta = 0.6
    o.append(cross(fx(-600), fy(800), LV) + cross(fx(-600), fy(-800), LV))
    o.append(Tb(fx(-600) - 12, fy(800) - 8, 'ζ = 0.6: −600 ± j800', 13, 'end', LV, True))
    # zeta = 1
    o.append(cross(fx(-1000), oy, NX))
    o.append(Tb(fx(-1000), oy + 26, 'ζ = 1: −1000 (twice)', 13, 'middle', NX, True))
    # zeta = 1.25
    o.append(cross(fx(-500), oy, INK) + cross(fx(-2000), oy, INK) + L(fx(-2000), oy + 40, fx(-500), oy + 40, MUT, 1.2))
    o.append(Tb(fx(-1250), oy + 60, 'ζ = 1.25: −500 and −2000', 13, 'middle', INK, True))
    o.append(Tb(fx(0) + 12, fy(-995) + 5, 'stable side: σ &lt; 0', 13, 'start', MUT))
    return 392, ''.join(o)


FIG[5] = (f5, 'Poles of a circuit with ωₙ = 1000 rad/s for four damping ratios. Underdamped poles sit on the dashed circle of radius ωₙ: the worked example (ζ = 0.1) has its pair at −100 ± j995, so it decays at 100 s⁻¹ and rings at 995 rad/s. At ζ = 1 the pair meets at −1000; above 1 they split along the real axis.',
          's-plane with a dashed semicircle of radius 1000 in the left half plane, conjugate poles at minus 100 plus or minus j995 for zeta 0.1 and minus 600 plus or minus j800 for zeta 0.6, a double pole at minus 1000 for zeta 1, and real poles at minus 500 and minus 2000 for zeta 1.25.')


# ---- 5.6: steady sine + decaying offset = total current, worked example ----
def f6():
    o = []
    th = math.atan2(3, 4)
    ax, fx, fy = plot(80, 690, 40, 270, (0, 4), (-2.4, 2.4), [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4], [-2, -1, 0, 1, 2], 't (s)', 'i (A)',
                      yfmt=lambda v: neg(f'{v:g}'))
    o.append(ax)
    o.append(curve(lambda t: 2 * math.sin(3 * t - th), 0, 4, fx, fy, MUT, 2, 300, '6 4'))
    o.append(curve(lambda t: 1.2 * math.exp(-4 * t), 0, 4, fx, fy, LV, 2.5, 200, '3 3'))
    o.append(curve(lambda t: 2 * math.sin(3 * t - th) + 1.2 * math.exp(-4 * t), 0, 4, fx, fy, AC, 3.2, 400))
    o.append(C(fx(0), fy(-1.2), 4.5, MUT) + C(fx(0), fy(1.2), 4.5, LV) + C(fx(0), fy(0), 5, AC))
    o.append(Tb(fx(0) + 10, fy(-1.2) + 18, 'steady sine starts at −1.2 A', 13, 'start', MUT, True))
    o.append(T(fx(0.36), fy(0.5), 'offset 1.2e⁻⁴ᵗ', 13, 'start', LV, True))
    o.append(Tb(fx(1.3), fy(2.25), 'total i(t), starts at 0 A', 13, 'start', AC, True))
    o.append(Tb(fx(2.3), fy(-2.25), sb('i', 'ss', ' = 2 sin(3t − 36.9°)'), 13, 'start', MUT))
    o.append(L(fx(1.25), fy(-2.4), fx(1.25), fy(2.4), L2, 1.2, '2 4'))
    o.append(Tb(fx(1.25) + 6, fy(-1.7), '5τ = 1.25 s', 13, 'start', MUT))
    return 314, ''.join(o)


FIG[6] = (f6, 'The worked example: the steady current 2 sin(3t − 36.9°) A starts at −1.2 A, so an offset 1.2e⁻⁴ᵗ A is needed to make the total start at 0 A. After about 5τ = 1.25 s the offset is gone and only the phasor answer is left.',
          'Plot from 0 to 4 seconds of the steady sine 2 sin of 3t minus 36.9 degrees, the decaying offset 1.2 e to the minus 4t, and their sum, which starts at 0 amperes and joins the sine after about 1.25 seconds.')


# ---- 5.7: the RC worked example, in time and in s ----
def f7():
    o = []
    o.append(panel(8, 8, 330, 240, 'Time domain, t ≥ 0'))
    o.append(panel(382, 8, 330, 240, 's-domain'))
    yt, yb = 82, 202
    # left
    xs, xr0, xr1, xc = 54, 96, 176, 246
    o.append(vsrc((xs, yt), (xs, yb), '10 V', 'r', off=22))
    o.append(wire([(xs, yt), (xr0, yt)]))
    o.append(res((xr0, yt), (xr1, yt), '5 Ω', 'u'))
    o.append(wire([(xr1, yt), (xc, yt)]))
    o.append(cap((xc, yt), (xc, yb), '0.1 F', 'r', off=20))
    o.append(T(xc + 20, (yt + yb) / 2 + 26, sb('v', 'C', '(0⁻) = 4 V'), 13, 'start', LV, True))
    o.append(wire([(xs, yb), (xc, yb)]))
    o.append(cur(xr1 + 10, yt + 16, xc - 22, yt + 16, 'i(t)', 'd', off=10))
    o.append(T(173, 234, 'differential equation', 13, fill=MUT))
    o.append(L(342, 128, 376, 128, NX, 2.5, arrow='x'))
    # right
    xs, xr0, xr1, xc = 428, 468, 546, 616
    o.append(vsrc((xs, yt), (xs, yb), '10/s', 'r', off=22))
    o.append(wire([(xs, yt), (xr0, yt)]))
    o.append(res((xr0, yt), (xr1, yt), '5', 'u'))
    o.append(wire([(xr1, yt), (xc, yt)]))
    o.append(zbox((xc, yt), (xc, yt + 60), '10/s', 'r', AC, off=16))
    o.append(vsrc((xc, yt + 60), (xc, yb), '4/s', 'r', LV, r=13, off=20))
    o.append(wire([(xs, yb), (xc, yb)]))
    o.append(cur(xr1 + 8, yt + 16, xc - 20, yt + 16, 'I(s)', 'd', off=10))
    o.append(T(547, 234, '1/(sC) = 10/s;  stored 4 V → 4/s', 13, fill=MUT))
    # result
    o.append(R(8, 260, 704, 100, PANEL, AC, 8, 1.5))
    o.append(T(360, 286, 'KVL:  10/s = 5 I(s) + (10/s) I(s) + 4/s', 14, fill=MUT))
    o.append(T(360, 314, 'I(s) = 6/(5s + 10) = 1.2/(s + 2)   →   i(t) = 1.2e⁻²ᵗ A', 15, bold=True))
    o.append(T(360, 342, sb('V', 'C', '(s) = 10/s − 6/(s + 2)   →   ') + sb('v', 'C', '(t) = 10 − 6e⁻²ᵗ V'), 15, fill=AC, bold=True))
    return 368, ''.join(o)


FIG[7] = (f7, 'The worked example in both domains. The capacitor becomes an impedance 10/s in series with a 4/s source that carries its stored 4 V, and the 10 V step becomes 10/s; one KVL equation then gives I(s) and V<sub>C</sub>(s), which invert to the time answers.',
          'Left: a 10 volt source, 5 ohm resistor and 0.1 farad capacitor holding 4 volts. Right: the same loop in the s-domain with source 10 over s, resistor 5, impedance 10 over s and a source 4 over s. Below: I of s equals 1.2 over s plus 2, i of t equals 1.2 e to the minus 2t, and v C of t equals 10 minus 6 e to the minus 2t.')


# ---- 5.8: poles and |H(jw)| of the series RLC low-pass for R = 2 and 10 ohm ----
def f8():
    o = []
    # s-plane
    k = 13.5
    ox, oy = 250, 176
    fx = lambda v: ox + v * k
    fy = lambda v: oy - v * k
    o.append(L(70, oy, 300, oy, L2, 1.5, arrow='m') + L(ox, 318, ox, 26, L2, 1.5, arrow='m'))
    o.append(T(298, oy + 20, 'σ', 15, 'end', MUT, italic=True) + T(ox + 8, 36, 'jω', 15, 'start', MUT, italic=True))
    r = 10 * k
    o.append(f'<path d="M{ox:.1f},{oy - r:.1f} A{r:.1f},{r:.1f} 0 0 0 {ox:.1f},{oy + r:.1f}" style="fill:none;stroke:{L2};stroke-width:1.5;stroke-dasharray:6 4"/>')
    for w, c in ((9.95, AC), (-9.95, AC)):
        o.append(cross(fx(-1), fy(w), c))
    for w, c in ((8.66, LV), (-8.66, LV)):
        o.append(cross(fx(-5), fy(w), c))
    o.append(Tb(fx(-1) - 12, fy(9.95) - 6, '−1 ± j9.95', 13, 'end', AC, True))
    o.append(Tb(fx(-5) - 12, fy(8.66) + 18, '−5 ± j8.66', 13, 'end', LV, True))
    o.append(Tb(fx(-7.2), fy(-6.6), 'radius ωₙ = 10', 13, 'end', MUT))
    o.append(T(150, 336, 'poles; no finite zeros', 13, fill=MUT))
    # magnitude plot
    ax, gx, gy = plot(390, 700, 40, 262, (0, 20), (0, 5.5), [0, 5, 10, 15, 20], [0, 1, 2, 3, 4, 5], 'ω (rad/s)', '|H(jω)|')
    o.append(ax)
    Hm = lambda w, R: 100 / math.hypot(100 - w * w, R * w)
    o.append(curve(lambda w: Hm(w, 2), 0, 20, gx, gy, AC, 3, 400))
    o.append(curve(lambda w: Hm(w, 10), 0, 20, gx, gy, LV, 3, 200))
    o.append(C(gx(9.9), gy(5.025), 5, AC) + Tb(gx(10.6), gy(5.0), 'R = 2 Ω: peak 5.03', 13, 'start', AC, True))
    o.append(C(gx(7.07), gy(1.155), 5, LV) + Tb(gx(12.4), gy(1.75), 'R = 10 Ω: peak 1.15', 13, 'start', LV, True))
    return 348, ''.join(o)


FIG[8] = (f8, 'The worked example. Left: the poles of H(s) = 100/(s² + (R/L)s + 100) sit on a circle of radius ωₙ = 10 rad/s, close to the jω axis for R = 2 Ω and further left for R = 10 Ω. Right: the pole near the axis gives the tall peak of 5.03 near 9.9 rad/s; the R = 10 Ω curve peaks at only 1.15.',
          'Left: s-plane with poles at minus 1 plus or minus j9.95 and at minus 5 plus or minus j8.66 on a dashed circle of radius 10. Right: magnitude of H against omega from 0 to 20 rad per second, with a peak of 5.03 near 9.9 for R 2 ohms and a peak of 1.15 near 7.07 for R 10 ohms.')


# ---- 5.9: the series RLC of the worked example with its two states, and the matrices ----
def f9():
    o = []
    o.append(R(8, 8, 360, 250, FIGBG, L2, 8, 1.2))
    yt, yb = 76, 206
    xs, x1, x2, x3, xc = 60, 96, 170, 196, 300
    o.append(vsrc((xs, yt), (xs, yb), sb('v', 's'), 'r', off=22))
    o.append(wire([(xs, yt), (x1, yt)]))
    o.append(res((x1, yt), (x2, yt), '2 Ω', 'u'))
    o.append(ind((x2, yt), (xc - 26, yt), '0.5 H', 'u'))
    o.append(wire([(xc - 26, yt), (xc, yt)]))
    o.append(cap((xc, yt), (xc, yb), '0.1 F', 'l', off=20))
    o.append(wire([(xs, yb), (xc, yb)]))
    o.append(cur(206, yt + 18, 262, yt + 18, sb('x', '1', ' = ') + sb('i', 'L'), 'd', AC, 14, 12))
    o.append(T(xc + 18, yt + 52, '+', 15, 'start', LV, True) + T(xc + 18, yb - 26, '−', 15, 'start', LV, True))
    o.append(T(xc + 16, (yt + yb) / 2 + 5, sb('x', '2', ' = ') + sb('v', 'C'), 14, 'start', LV, True))
    o.append(T(188, 240, 'output y = ' + sb('v', 'C'), 13, fill=MUT))
    # matrices
    o.append(R(384, 8, 328, 250, PANEL, AC, 8, 1.5))
    def mat(x, y, rows, w=44, c=INK):
        h = 26 * len(rows)
        out = [P([(x + 6, y - 18), (x, y - 18), (x, y - 18 + h), (x + 6, y - 18 + h)], c, 1.8)]
        cols = len(rows[0])
        out.append(P([(x + w * cols - 6, y - 18), (x + w * cols, y - 18), (x + w * cols, y - 18 + h), (x + w * cols - 6, y - 18 + h)], c, 1.8))
        for i, r in enumerate(rows):
            for j, v in enumerate(r):
                out.append(T(x + w * j + w / 2, y + 26 * i, v, 15, fill=c, bold=True))
        return ''.join(out)
    o.append(T(400, 60, 'A =', 15, 'start', AC, True) + mat(436, 52, [['−4', '−2'], ['10', '0']], c=AC))
    o.append(T(548, 60, 'B =', 15, 'start', AC, True) + mat(584, 52, [['2'], ['0']], c=AC))
    o.append(T(400, 148, 'C = [ 0, 1 ]', 15, 'start', INK, True) + T(560, 148, 'D = [ 0 ]', 15, 'start', INK, True))
    o.append(T(400, 190, 'det(sI − A) = s² + 4s + 20', 14, 'start'))
    o.append(T(400, 218, 'roots −2 ± j4 s⁻¹', 14, 'start', NX, True))
    o.append(T(400, 244, 'ωₙ = 4.47 rad/s, ζ = 0.447', 13, 'start', MUT))
    return 266, ''.join(o)


FIG[9] = (f9, 'The worked example: the inductor current x₁ and the capacitor voltage x₂ are the two states of the series RLC. Its state matrices give det(sI − A) = s² + 4s + 20, whose roots −2 ± j4 are the natural frequencies.',
          'A series circuit of source v s, 2 ohms, 0.5 henry and 0.1 farad with the inductor current marked x1 and the capacitor voltage marked x2, beside the matrices A equal to minus 4, minus 2; 10, 0 and B equal to 2; 0, C equal to 0, 1, D equal to 0, and the roots minus 2 plus or minus j4.')


spec = make_spec(FIG)
