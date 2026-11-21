"""Claude's hand-drawn figures for ec-vlsi-u3 (CMOS inverters and logic styles), one per chapter. Every number comes from
that chapter's own worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


# ---- circuit symbols ----
def mos(x, y, kind='n', gate='left', lab=None, lab_side='right', gl=26, c=INK, size=14):
    """MOSFET with a vertical channel at x, centred at y. Drain/source terminals at (x+14, y-30) and (x+14, y+30);
    the gate lead runs to (x-7-gl, y) (or to the right when gate='right', mirrored). pMOS gets a bubble."""
    s = 1 if gate == 'left' else -1
    o = [L(x, y - 18, x, y + 18, c, 2.5),
         L(x - 7 * s, y - 14, x - 7 * s, y + 14, c, 2)]
    if kind == 'p':
        o.append(f'<circle cx="{x - 11 * s:.1f}" cy="{y:.1f}" r="4" style="fill:var(--fig);stroke:{c};stroke-width:2"/>')
        o.append(L(x - 15 * s, y, x - (7 + gl) * s, y, c, 2))
    else:
        o.append(L(x - 7 * s, y, x - (7 + gl) * s, y, c, 2))
    o += [P([(x, y - 14), (x + 14 * s, y - 14), (x + 14 * s, y - 30)], c, 2),
          P([(x, y + 14), (x + 14 * s, y + 14), (x + 14 * s, y + 30)], c, 2)]
    if lab:
        if lab_side == 'right':
            o.append(T(x + 14 * s + 8 * s, y + 5, lab, size, 'start' if s == 1 else 'end'))
        else:
            o.append(T(x - (7 + gl) * s, y - 8, lab, size, 'start' if s == 1 else 'end'))
    return ''.join(o)


def gnd(x, y, c=INK):
    return L(x, y, x, y + 8, c, 2) + L(x - 12, y + 8, x + 12, y + 8, c, 2) + L(x - 7, y + 13, x + 7, y + 13, c, 2) + L(x - 3, y + 18, x + 3, y + 18, c, 2)


def rail(x1, x2, y, lab, c=INK):
    return L(x1, y, x2, y, c, 2.5) + T(x1 - 8, y + 5, lab, 14, 'end', MUT)


def res_v(x, y1, y2, c=INK, n=5, a=7):
    lead = (y2 - y1) * 0.2
    ys = y1 + lead; ye = y2 - lead; st = (ye - ys) / (2 * n)
    pts = [(x, y1), (x, ys)] + [(x + (a if i % 2 == 0 else -a), ys + st * (2 * i + 1)) for i in range(n)] + [(x, ye), (x, y2)]
    return P(pts, c, 2)


def res_h(x1, x2, y, c=INK, n=5, a=7):
    lead = (x2 - x1) * 0.2
    xs = x1 + lead; xe = x2 - lead; st = (xe - xs) / (2 * n)
    pts = [(x1, y), (xs, y)] + [(xs + st * (2 * i + 1), y + (a if i % 2 == 0 else -a)) for i in range(n)] + [(xe, y), (x2, y)]
    return P(pts, c, 2)


def cap_v(x, y, c=INK, w=14):
    """capacitor to ground hanging from (x, y): two plates then ground"""
    return L(x, y, x, y + 14, c, 2) + L(x - w, y + 14, x + w, y + 14, c, 2.5) + L(x - w, y + 21, x + w, y + 21, c, 2.5) + L(x, y + 21, x, y + 30, c, 2) + gnd(x, y + 30, c)


def dot(x, y, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" style="fill:{c}"/>'


def inv_sym(x, y, w=36, c=INK, fill=PANEL):
    """inverter triangle from x to x+w centred at y, with output bubble; returns (svg, x_out)"""
    h = w * 0.9
    o = f'<path d="M{x:.1f},{y - h / 2:.1f} L{x + w:.1f},{y:.1f} L{x:.1f},{y + h / 2:.1f} Z" style="fill:{fill};stroke:{c};stroke-width:2"/>'
    o += f'<circle cx="{x + w + 5:.1f}" cy="{y:.1f}" r="5" style="fill:var(--fig);stroke:{c};stroke-width:2"/>'
    return o, x + w + 10


def nand_sym(x, y, w=46, h=44, c=INK, fill=PANEL):
    r = h / 2
    o = f'<path d="M{x:.1f},{y - r:.1f} L{x + w - r:.1f},{y - r:.1f} A{r:.1f},{r:.1f} 0 0 1 {x + w - r:.1f},{y + r:.1f} L{x:.1f},{y + r:.1f} Z" style="fill:{fill};stroke:{c};stroke-width:2"/>'
    o += f'<circle cx="{x + w + 5:.1f}" cy="{y:.1f}" r="5" style="fill:var(--fig);stroke:{c};stroke-width:2"/>'
    return o, x + w + 10


def plot_axes(x0, x1, y0, y1, xs, ys, fx, fy, xlab, ylab, xfmt=str, yfmt=str, grid=True):
    o = [L(x0, y1, x1, y1, L2, 1.5), L(x0, y0, x0, y1, L2, 1.5)]
    for v in xs:
        X = fx(v); o += [L(X, y1, X, y1 + 5, L2, 1.5), T(X, y1 + 20, xfmt(v), 13, fill=MUT)]
    for v in ys:
        Y = fy(v); o += [L(x0 - 5, Y, x0, Y, L2, 1.5), T(x0 - 9, Y + 4.5, yfmt(v), 13, 'end', MUT)]
        if grid: o.append(L(x0, Y, x1, Y, LN, 1))
    o.append(T((x0 + x1) / 2, y1 + 40, xlab, 14, fill=MUT))
    o.append(T(x0 - 4, y0 - 12, ylab, 14, 'start', MUT))
    return ''.join(o)


# ---- 3.1 VTC of the matched 3.3 V inverter (computed) ----
def vtc(vin, r2=1.0, vt=0.6, vdd=3.3):
    """long-channel VTC, kn/kp = r2"""
    if vin <= vt: return vdd
    if vdd - vin <= vt: return 0.0
    def f(vo):
        vov = vin - vt
        In = r2 * ((vov * vo - vo * vo / 2) if vo < vov else vov * vov / 2)
        vsd = vdd - vo; ovp = vdd - vin - vt
        Ip = (ovp * vsd - vsd * vsd / 2) if vsd < ovp else ovp * ovp / 2
        return In - Ip
    a, b = 0.0, vdd
    fa = f(a)
    for _ in range(80):
        m = (a + b) / 2; fm_ = f(m)
        if fa * fm_ <= 0: b = m
        else: a, fa = m, fm_
    return (a + b) / 2


def f1():
    x0, x1, y0, y1 = 80, 470, 50, 350
    fx = lambda v: x0 + v / 3.3 * (x1 - x0); fy = lambda v: y1 - v / 3.3 * (y1 - y0)
    o = [plot_axes(x0, x1, y0, y1, [0, 0.6, 1.0, 1.65, 2.0, 2.7, 3.3], [0, 1.0, 2.0, 3.3], fx, fy,
                   'input V<tspan baseline-shift="sub" font-size="11">in</tspan> (V)', 'output V<tspan baseline-shift="sub" font-size="11">out</tspan> (V)', lambda v: f'{v:g}', lambda v: f'{v:g}')]
    # noise-margin bands on the input axis
    o.append(f'<rect x="{fx(0):.1f}" y="{y1 - 14:.1f}" width="{fx(1.3875) - fx(0):.1f}" height="10" style="fill:var(--live-soft)"/>')
    o.append(f'<rect x="{fx(1.9125):.1f}" y="{y1 - 14:.1f}" width="{fx(3.3) - fx(1.9125):.1f}" height="10" style="fill:var(--next-soft)"/>')
    # diagonal Vout = Vin
    o.append(L(fx(0), fy(0), fx(3.3), fy(3.3), L2, 1.5, '5 5'))
    # second curve: equal sizes, r^2 = 2.5
    pts2 = []
    for i in range(0, 331):
        v = i / 100; pts2.append((fx(v), fy(vtc(v, 2.5))))
    o.append(P(pts2, MUT, 2, '6 4'))
    pts = []
    for i in range(0, 331):
        v = i / 100; pts.append((fx(v), fy(vtc(v))))
    o.append(P(pts, AC, 3))
    # marks
    o.append(L(fx(1.3875), fy(3.3) - 4, fx(1.3875), y1, LV, 1.5, '4 3')); o.append(C(fx(1.3875), fy(3.0375), 5, LV))
    o.append(T(fx(1.3875), y0 - 14, 'V<tspan baseline-shift="sub" font-size="11">IL</tspan> = 1.39 V', 14, 'middle', LV, True))
    o.append(L(fx(1.9125), fy(0.2625), fx(1.9125), y1, LV, 1.5, '4 3')); o.append(C(fx(1.9125), fy(0.2625), 5, LV))
    o.append(L(fx(1.9125), fy(0.2625), fx(2.05), fy(0.7), LV, 1))
    o.append(Tb(fx(2.05) + 4, fy(0.7) - 4, 'V<tspan baseline-shift="sub" font-size="11">IH</tspan> = 1.91 V', 14, 'start', LV, True))
    o.append(C(fx(1.65), fy(1.65), 6, NX))
    o.append(Tb(fx(1.65) + 12, fy(1.65) + 22, 'V<tspan baseline-shift="sub" font-size="11">M</tspan> = 1.65 V', 14, 'start', NX, True))
    o.append(C(fx(1.414), fy(1.414), 5, MUT))
    o.append(T(fx(1.414) - 10, fy(1.414) + 22, '1.41 V', 13, 'end', MUT))
    # legend / notes on the right
    lx = 500
    o.append(L(lx, 70, lx + 30, 70, AC, 3)); o.append(T(lx + 38, 75, 'matched pair', 14, 'start'))
    o.append(T(lx + 38, 93, 'k<tspan baseline-shift="sub" font-size="11">n</tspan> = k<tspan baseline-shift="sub" font-size="11">p</tspan>', 14, 'start', MUT))
    o.append(L(lx, 120, lx + 30, 120, MUT, 2, '6 4')); o.append(T(lx + 38, 125, 'equal widths', 14, 'start'))
    o.append(T(lx + 38, 143, 'k<tspan baseline-shift="sub" font-size="11">n</tspan> = 2.5 k<tspan baseline-shift="sub" font-size="11">p</tspan>', 14, 'start', MUT))
    o.append(T(lx, 190, 'V<tspan baseline-shift="sub" font-size="11">DD</tspan> = 3.3 V', 14, 'start'))
    o.append(T(lx, 210, 'V<tspan baseline-shift="sub" font-size="11">tn</tspan> = |V<tspan baseline-shift="sub" font-size="11">tp</tspan>| = 0.6 V', 14, 'start'))
    o.append(T(lx, 248, 'slope = −1 at', 14, 'start', LV))
    o.append(T(lx, 266, 'V<tspan baseline-shift="sub" font-size="11">IL</tspan> and V<tspan baseline-shift="sub" font-size="11">IH</tspan>', 14, 'start', LV))
    o.append(f'<rect x="{lx}" y="290" width="22" height="10" style="fill:var(--live-soft)"/>'); o.append(T(lx + 30, 300, 'valid 0 input', 14, 'start'))
    o.append(f'<rect x="{lx}" y="312" width="22" height="10" style="fill:var(--next-soft)"/>'); o.append(T(lx + 30, 322, 'valid 1 input', 14, 'start'))
    o.append(T(lx, 350, 'NM<tspan baseline-shift="sub" font-size="11">L</tspan> = NM<tspan baseline-shift="sub" font-size="11">H</tspan> = 1.39 V', 14, 'start', INK, True))
    return 400, ''.join(o)
FIG[1] = (f1, 'The computed transfer curve of the matched 3.3 V inverter: the slope is −1 at V<sub>IL</sub> = 1.39 V and V<sub>IH</sub> = 1.91 V, and the curve crosses V<sub>out</sub> = V<sub>in</sub> at V<sub>M</sub> = 1.65 V. With equal widths (dashed) the stronger nMOS pulls V<sub>M</sub> down to 1.41 V.',
          'Plot of output voltage against input voltage for a 3.3 volt CMOS inverter. The solid matched curve crosses the diagonal at 1.65 volts and has slope minus one at 1.39 and 1.91 volts; a dashed curve for equal widths crosses at 1.41 volts.')


# ---- 3.2 the four NMOS loads ----
def f2():
    o = []
    cols = [(90, 'Resistor', 'R<tspan baseline-shift="sub" font-size="11">L</tspan> = 100 kΩ', 'V<tspan baseline-shift="sub" font-size="11">OH</tspan> = 5 V', 'V<tspan baseline-shift="sub" font-size="11">OL</tspan> = 0.57 V'),
            (265, 'Enhancement', 'gate at V<tspan baseline-shift="sub" font-size="11">DD</tspan>', 'V<tspan baseline-shift="sub" font-size="11">OH</tspan> = 4.2 V', 'V<tspan baseline-shift="sub" font-size="11">OL</tspan> = 0.22 V'),
            (440, 'Depletion', 'V<tspan baseline-shift="sub" font-size="11">GS</tspan> = 0', 'V<tspan baseline-shift="sub" font-size="11">OH</tspan> = 5 V', 'V<tspan baseline-shift="sub" font-size="11">OL</tspan> = 0.048 V'),
            (615, 'Pseudo-nMOS', 'pMOS, gate at 0 V', 'V<tspan baseline-shift="sub" font-size="11">OH</tspan> = 5 V', 'V<tspan baseline-shift="sub" font-size="11">OL</tspan> by k<tspan baseline-shift="sub" font-size="11">n</tspan>/k<tspan baseline-shift="sub" font-size="11">p</tspan>')]
    for i, (cx, name, sub, voh, vol) in enumerate(cols):
        hl = AC if i != 3 else LV
        o.append(T(cx, 26, name, 15, bold=True, fill=hl))
        o.append(L(cx - 40, 50, cx + 40, 50, INK, 2.5)); o.append(T(cx + 44, 55, 'V<tspan baseline-shift="sub" font-size="11">DD</tspan>', 13, 'start', MUT))
        # load from rail (y=50) to output node (y=150)
        lx = cx  # load terminal line x
        if i == 0:
            o.append(res_v(lx, 50, 150, hl))
        elif i in (1, 2):
            # nMOS load: channel at lx-14 so that terminals are at lx
            o.append(mos(lx - 14, 100, 'n', 'left', gl=18, c=hl))
            o.append(L(lx, 50, lx, 70, hl, 2)); o.append(L(lx, 130, lx, 150, hl, 2))
            if i == 1:
                o.append(P([(lx - 39, 100), (lx - 50, 100), (lx - 50, 50)], hl, 2)); o.append(dot(lx - 50, 50))
            else:
                o.append(P([(lx - 39, 100), (lx - 50, 100), (lx - 50, 140), (lx, 140)], hl, 2)); o.append(dot(lx, 140))
                o.append(f'<rect x="{lx - 13:.1f}" y="84" width="4" height="32" style="fill:{hl}"/>')
        else:
            o.append(mos(lx - 14, 100, 'p', 'left', gl=18, c=hl))
            o.append(L(lx, 50, lx, 70, hl, 2)); o.append(L(lx, 130, lx, 150, hl, 2))
            o.append(L(lx - 39, 100, lx - 39, 112, hl, 2)); o.append(gnd(lx - 39, 112, hl))
        # output node
        o.append(dot(lx, 150)); o.append(L(lx, 150, lx + 36, 150, INK, 2)); o.append(T(lx + 40, 155, 'out', 13, 'start', MUT))
        # driver nMOS
        o.append(mos(lx - 14, 190, 'n', 'left', gl=22, c=INK))
        o.append(L(lx, 150, lx, 160, INK, 2)); o.append(L(lx, 220, lx, 226, INK, 2)); o.append(gnd(lx, 226))
        o.append(T(lx - 45, 195, 'in', 13, 'end', MUT))
        o.append(T(cx, 274, sub, 13, fill=MUT))
        o.append(T(cx, 300, voh, 14)); o.append(T(cx, 322, vol, 14))
    o.append(T(360, 356, 'All four draw current from V<tspan baseline-shift="sub" font-size="11">DD</tspan> while the output is low (driver on).', 14, fill=INK))
    return 372, ''.join(o)
FIG[2] = (f2, 'The four pull-ups of an NMOS inverter over the same nMOS driver, with the levels from this chapter\'s examples at V<sub>DD</sub> = 5 V. Only the enhancement load loses a threshold at the top; every one fights the driver when the output is low.',
          'Four circuits side by side: a resistor, an enhancement nMOS with gate at VDD, a depletion nMOS with gate tied to its source, and a pMOS with gate grounded, each above an nMOS driver, with their output high and low levels written underneath.')


# ---- 3.3 step response of the example inverter ----
def f3():
    CL, kn, VDD, Vt = 50e-15, 200e-6, 1.8, 0.5
    def I(v):
        vov = VDD - Vt
        return kn / 2 * vov * vov if v > vov else kn * (vov * v - v * v / 2)
    t0 = 0.1e-9
    ts, vs = [0, t0], [VDD, VDD]
    t, v, dt = t0, VDD, 2e-13
    marks = {}
    while t < 1.0e-9:
        v -= I(v) / CL * dt; t += dt
        ts.append(t); vs.append(v)
        for lev in (0.9 * VDD, 0.5 * VDD, 0.1 * VDD, VDD - Vt):
            if lev not in marks and v <= lev: marks[lev] = t
    x0, x1, y0, y1 = 80, 640, 50, 300
    fx = lambda s: x0 + s / 1.0e-9 * (x1 - x0); fy = lambda u: y1 - u / 2.0 * (y1 - y0)
    o = [plot_axes(x0, x1, y0, y1, [0, 0.2e-9, 0.4e-9, 0.6e-9, 0.8e-9, 1.0e-9], [0, 0.9, 1.3, 1.8], fx, fy,
                   'time (ns)', 'voltage (V)', lambda s: f'{s * 1e9:.1f}', lambda u: f'{u:g}')]
    # input step
    o.append(P([(fx(0), fy(0)), (fx(t0), fy(0)), (fx(t0), fy(VDD)), (fx(1.0e-9), fy(VDD))], LV, 2.5, '7 4'))
    o.append(T(fx(0.92e-9), fy(VDD) - 10, 'V<tspan baseline-shift="sub" font-size="11">in</tspan>', 14, 'middle', LV, True))
    o.append(P([(fx(a), fy(b)) for a, b in zip(ts[::5], vs[::5])], AC, 3))
    o.append(T(fx(0.8e-9), fy(0.4), 'V<tspan baseline-shift="sub" font-size="11">out</tspan>', 14, 'middle', AC, True))
    # 50% marker
    t50 = marks[0.9]
    o.append(L(fx(t0), fy(0.9), fx(t50), fy(0.9), NX, 1.5, '4 3'))
    o.append(C(fx(t50), fy(0.9), 5, NX))
    o.append(L(fx(t0), fy(0.9) + 26, fx(t50), fy(0.9) + 26, NX, 2))
    o.append(L(fx(t0), fy(0.9) + 20, fx(t0), fy(0.9) + 32, NX, 2)); o.append(L(fx(t50), fy(0.9) + 20, fx(t50), fy(0.9) + 32, NX, 2))
    o.append(T((fx(t0) + fx(t50)) / 2 + 60, fy(0.9) + 50, f't<tspan baseline-shift="sub" font-size="11">PHL</tspan> = {(t50 - t0) * 1e9:.2f} ns', 14, 'middle', NX, True))
    # saturation boundary
    ts_ = marks[VDD - Vt]
    o.append(C(fx(ts_), fy(VDD - Vt), 5, MUT))
    o.append(T(fx(ts_) + 12, fy(VDD - Vt) - 8, 'saturation ends at 1.3 V (0.15 ns)', 13, 'start', MUT))
    tf = marks[0.1 * VDD] - marks[0.9 * VDD]
    o.append(T(450, 160, f'90% → 10% fall: {tf * 1e9:.2f} ns', 14, 'start'))
    o.append(T(450, 182, 'C<tspan baseline-shift="sub" font-size="11">L</tspan> = 50 fF, k<tspan baseline-shift="sub" font-size="11">n</tspan> = 200 µA/V²', 13, 'start', MUT))
    o.append(T(450, 200, 'V<tspan baseline-shift="sub" font-size="11">DD</tspan> = 1.8 V, V<tspan baseline-shift="sub" font-size="11">tn</tspan> = 0.5 V', 13, 'start', MUT))
    return 350, ''.join(o)
FIG[3] = (f3, 'The output of the example inverter after an input step at 0.1 ns, computed from the nMOS equations. It falls at a constant rate while the nMOS is saturated, then more slowly, and crosses 0.9 V 0.27 ns after the step.',
          'Plot of voltage against time: the input steps from 0 to 1.8 volts at 0.1 nanoseconds; the output falls from 1.8 volts, leaves saturation at 1.3 volts, and crosses 0.9 volts 0.27 nanoseconds after the step.')


# ---- 3.4 the sized path ----
def f4():
    o = []
    y = 110
    o.append(L(30, y, 70, y, INK, 2)); o.append(T(30, y - 12, 'in', 13, 'start', MUT))
    s1, xo1 = inv_sym(70, y, 40); o.append(s1)
    o.append(L(xo1, y, 260, y, INK, 2))
    o.append(L(225, y + 22, 260, y + 22, INK, 2)); o.append(T(220, y + 27, 'B', 13, 'end', MUT))
    s2, xo2 = nand_sym(260, y + 11, 56, 52); o.append(s2)
    o.append(L(xo2, y + 11, 480, y + 11, INK, 2))
    s3, xo3 = inv_sym(480, y + 11, 44); o.append(s3)
    o.append(L(xo3, y + 11, 600, y + 11, INK, 2))
    o.append(cap_v(600, y + 11))
    o.append(T(622, y + 40, '64C', 15, 'start', LV, True)); o.append(T(622, y + 58, 'load', 13, 'start', MUT))
    # Cin labels
    for x, lab in ((90, 'C<tspan baseline-shift="sub" font-size="11">in</tspan> = 1.00C'), (288, 'C<tspan baseline-shift="sub" font-size="11">in</tspan> = 4.40C'), (502, 'C<tspan baseline-shift="sub" font-size="11">in</tspan> = 14.54C')):
        o.append(T(x, 50, lab, 14, bold=True, fill=AC))
    for x, g in ((90, 'g = 1, p = 1'), (288, 'g = 4/3, p = 2'), (502, 'g = 1, p = 1')):
        o.append(T(x, 70, g, 13, fill=MUT))
    # stage efforts below
    yb = 230
    for x, h, f, d in ((90, 'h = 4.40', 'f = 4.40', 'd = 5.40τ'), (288, 'h = 3.30', 'f = 4.40', 'd = 6.40τ'), (502, 'h = 4.40', 'f = 4.40', 'd = 5.40τ')):
        o.append(boxt(x - 72, yb - 20, 144, 74, [h, f, d], size=14))
    o.append(T(360, 330, 'F = (4/3) × 64 = 85.3,  f̂ = 85.3<tspan baseline-shift="super" font-size="10">1/3</tspan> = 4.40,  D = 3 × 4.40 + 4 = 17.2τ', 15, bold=True))
    o.append(T(360, 356, 'NAND2 transistors about 6.6 units wide; last inverter nMOS 14.5, pMOS 29.1', 14, fill=MUT))
    return 376, ''.join(o)
FIG[4] = (f4, 'The inverter → NAND2 → inverter path of the worked example, sized for equal stage effort: every stage has f = 4.40, so the input capacitances grow 1C, 4.40C, 14.54C towards the 64C load and the path delay is 17.2τ.',
          'Three gates in a row, an inverter, a NAND2 and an inverter, driving a 64C load; above each its input capacitance 1.00C, 4.40C and 14.54C, below each its electrical effort, stage effort 4.40 and delay.')


# ---- 3.5 wire cross-section and pi model ----
def f5():
    o = []
    # cross-section on the left
    gy = 280
    o.append(f'<rect x="30" y="{gy}" width="330" height="22" style="fill:var(--line2)"/>')
    o.append(T(195, gy + 16, 'layer below (ground)', 13, fill=INK))
    wy, wh = 150, 70
    o.append(R(40, wy, 70, wh, PANEL, MUT, 3)); o.append(T(75, wy - 8, 'neighbour', 13, fill=MUT))
    o.append(R(280, wy, 70, wh, PANEL, MUT, 3)); o.append(T(315, wy - 8, 'neighbour', 13, fill=MUT))
    o.append(R(155, wy, 80, wh, 'var(--accent-soft)', AC, 3))
    o.append(T(195, wy + 30, 'wire', 14, bold=True, fill=AC)); o.append(T(195, wy + 50, 't = 0.4 µm', 13))
    # width dimension above the wire
    o.append(L(155, wy - 12, 235, wy - 12, INK, 1.5)); o.append(L(155, wy - 18, 155, wy - 6, INK, 1.5)); o.append(L(235, wy - 18, 235, wy - 6, INK, 1.5))
    o.append(T(195, wy - 20, 'W = 0.2 µm', 13))
    # height dimension
    o.append(L(132, wy + wh, 132, gy, INK, 1.5, '3 3')); o.append(L(126, wy + wh, 150, wy + wh, INK, 1, '2 2'))
    o.append(T(126, 258, 'h = 0.3 µm', 13, 'end'))
    # plate capacitance
    o.append(L(185, wy + wh + 2, 185, gy - 3, LV, 2.5, arrow='l'))
    o.append(T(193, 244, 'C<tspan baseline-shift="sub" font-size="11">pp</tspan>', 14, 'start', LV, True)); o.append(T(193, 271, '23 fF', 14, 'start', LV, True))
    # fringe from the right corner
    o.append(arc(235, wy + wh - 4, 288, gy - 3, -0.35, NX, 2, 'x'))
    o.append(T(300, 252, 'fringe', 13, 'start', NX)); o.append(T(300, 270, '80 fF', 14, 'start', NX, True))
    # coupling arrows
    o.append(L(155, wy + 35, 113, wy + 35, AC, 2, arrow='n')); o.append(L(235, wy + 35, 277, wy + 35, AC, 2, arrow='n'))
    o.append(T(195, 100, 'coupling: 50 fF to each neighbour', 14, 'middle', AC, True))
    o.append(T(195, 72, 'L = 1 mm,  R<tspan baseline-shift="sub" font-size="11">□</tspan> = 0.055 Ω/□', 13, fill=MUT))
    # pi model on the right
    x1, x2, y = 440, 640, 140
    o.append(T(540, 40, 'π model of the same wire', 14, bold=True))
    o.append(L(400, y, x1, y, INK, 2)); o.append(T(398, y - 10, 'driver', 13, 'end', MUT))
    o.append(dot(x1, y)); o.append(res_h(x1, x2, y)); o.append(dot(x2, y)); o.append(L(x2, y, 690, y, INK, 2)); o.append(T(692, y - 10, 'load', 13, 'end', MUT))
    o.append(T(540, y - 18, 'R<tspan baseline-shift="sub" font-size="11">w</tspan> = 275 Ω', 14, bold=True))
    o.append(cap_v(x1, y)); o.append(cap_v(x2, y))
    o.append(T(x1 + 20, y + 24, '101 fF', 14, 'start')); o.append(T(x2 - 20, y + 24, '101 fF', 14, 'end'))
    o.append(T(540, 240, 'C<tspan baseline-shift="sub" font-size="11">w</tspan> = 23 + 80 + 100 = 203 fF', 14))
    o.append(T(540, 264, 'own delay 0.38 R<tspan baseline-shift="sub" font-size="11">w</tspan>C<tspan baseline-shift="sub" font-size="11">w</tspan> = 21 ps', 14))
    o.append(T(540, 288, 'at 5 mm: 0.53 ns (25 ×)', 14, fill=LV, bold=True))
    return 316, ''.join(o)
FIG[5] = (f5, 'Left: the 1 mm example wire in cross-section, with its plate, fringe and coupling capacitances. Right: the same wire as a π model, half its 203 fF at each end of its 275 Ω.',
          'Cross-section of a wire between two neighbours above a ground layer, labelled with width 0.2 micrometre, thickness 0.4 micrometre and height 0.3 micrometre, and its plate, fringe and coupling capacitances; beside it a pi model with 275 ohms between two 101 femtofarad capacitors.')


# ---- 3.6 the RC tree ----
def f6():
    o = []
    y = 120
    o.append(T(40, y - 30, 'driver', 13, 'start', MUT))
    o.append(L(30, y, 60, y, INK, 2))
    o.append(res_h(60, 150, y, LV)); o.append(T(105, y - 16, '1 kΩ', 14, 'middle', LV, True))
    o.append(dot(150, y, LV))
    o.append(T(150, y - 18, 'node 1', 13, fill=MUT))
    o.append(cap_v(150, y)); o.append(T(170, y + 26, '20 fF', 14, 'start'))
    # upper branch to node 2 and 4
    o.append(L(150, y, 190, y, LV, 2)); o.append(res_h(190, 300, y, LV)); o.append(T(245, y - 16, '2 kΩ', 14, 'middle', LV, True))
    o.append(dot(300, y, LV)); o.append(T(300, y - 18, 'node 2', 13, fill=MUT))
    o.append(cap_v(300, y)); o.append(T(320, y + 26, '30 fF', 14, 'start'))
    o.append(L(300, y, 340, y, LV, 2)); o.append(res_h(340, 450, y, LV)); o.append(T(395, y - 16, '1 kΩ', 14, 'middle', LV, True))
    o.append(dot(450, y, LV)); o.append(T(450, y - 18, 'node 4', 13, fill=LV, bold=True))
    o.append(cap_v(450, y)); o.append(T(470, y + 26, '40 fF', 14, 'start'))
    # lower branch to node 3
    yb = 250
    o.append(P([(150, y + 50), (150, y + 50)], INK))
    o.append(P([(165, y), (165, yb), (190, yb)], INK, 2)); o.append(dot(165, y))
    o.append(res_h(190, 300, yb)); o.append(T(245, yb - 16, '3 kΩ', 14, bold=True))
    o.append(dot(300, yb)); o.append(T(300, yb - 18, 'node 3', 13, fill=MUT))
    o.append(cap_v(300, yb)); o.append(T(320, yb + 26, '10 fF', 14, 'start'))
    # sums
    o.append(T(500, 210, 'τ<tspan baseline-shift="sub" font-size="11">D4</tspan> = 20·1 + 30·3 + 10·1 + 40·4', 14, 'start', LV, True))
    o.append(T(500, 232, '= 280 ps → 0.69τ ≈ 193 ps', 14, 'start', LV, True))
    o.append(T(500, 280, 'τ<tspan baseline-shift="sub" font-size="11">D3</tspan> = 20·1 + 30·1 + 10·4 + 40·1', 14, 'start'))
    o.append(T(500, 302, '= 130 ps → 0.69τ ≈ 90 ps', 14, 'start'))
    o.append(T(500, 336, '(fF × kΩ = ps)', 13, 'start', MUT))
    return 360, ''.join(o)
FIG[6] = (f6, 'The RC tree of the first worked example. The path to node 4 is highlighted: each capacitor is multiplied by the resistance it shares with that path, so the 10 fF on the side branch sees only the first 1 kΩ.',
          'An RC tree: a 1 kilohm resistor to node 1 with 20 femtofarads, then 2 kilohms to node 2 with 30 femtofarads and 1 kilohm to node 4 with 40 femtofarads; a side branch of 3 kilohms goes to node 3 with 10 femtofarads. The sums give 280 picoseconds at node 4 and 130 at node 3.')


# ---- 3.7 power versus frequency (log-log) ----
def f7():
    x0, x1, y0, y1 = 90, 520, 40, 300
    lf0, lf1, lp0, lp1 = 4, 9, -6, -2  # 10 kHz .. 1 GHz ; 1 uW .. 10 mW
    fx = lambda f: x0 + (math.log10(f) - lf0) / (lf1 - lf0) * (x1 - x0)
    fy = lambda p: y1 - (math.log10(p) - lp0) / (lp1 - lp0) * (y1 - y0)
    names = {4: '10k', 5: '100k', 6: '1M', 7: '10M', 8: '100M', 9: '1G'}
    pn = {-6: '1 µW', -5: '10 µW', -4: '100 µW', -3: '1 mW', -2: '10 mW'}
    o = [plot_axes(x0, x1, y0, y1, [10 ** e for e in range(4, 10)], [10 ** e for e in range(-6, -1)], fx, fy,
                   'clock frequency f (Hz)', 'power', lambda f: names[round(math.log10(f))], lambda p: pn[round(math.log10(p))])]
    k = 1.62e-3 / 1e8
    o.append(L(fx(1e4), fy(k * 1e4), fx(1e9), fy(k * 1e9) if k * 1e9 < 1e-2 else fy(1e-2), AC, 3))
    # clip: k*1e9 = 16.2 mW > 10 mW, so end at P = 10 mW
    o[-1] = L(fx(1e-6 / k), fy(1e-6), fx(1e-2 / k), fy(1e-2), AC, 3)
    o.append(L(fx(1e4), fy(18e-6), fx(1e9), fy(18e-6), LV, 2.5))
    o.append(L(fx(1e4), fy(180e-6), fx(1e9), fy(180e-6), NX, 2.5, '7 4'))
    o.append(C(fx(1.111e6), fy(18e-6), 6, LV)); o.append(C(fx(1.111e7), fy(180e-6), 6, NX))
    o.append(L(fx(1.111e6), fy(18e-6), fx(1.111e6), y1, LV, 1.5, '3 3'))
    o.append(L(fx(1.111e7), fy(180e-6), fx(1.111e7), y1, NX, 1.5, '3 3'))
    o.append(C(fx(1e8), fy(1.62e-3), 6, AC))
    o.append(T(fx(1e8) - 10, fy(1.62e-3) - 12, '1.62 mW at 100 MHz', 14, 'end', AC, True))
    lx = 545
    o.append(L(lx, 80, lx + 28, 80, AC, 3)); o.append(T(lx + 34, 85, 'switching', 14, 'start'))
    o.append(T(lx + 34, 103, 'α = 0.1, 50 pF', 13, 'start', MUT))
    o.append(L(lx, 135, lx + 28, 135, LV, 2.5)); o.append(T(lx + 34, 140, 'leakage 18 µW', 14, 'start'))
    o.append(T(lx + 34, 158, 'equal at 1.11 MHz', 13, 'start', LV))
    o.append(L(lx, 190, lx + 28, 190, NX, 2.5, '7 4')); o.append(T(lx + 34, 195, 'V<tspan baseline-shift="sub" font-size="11">t</tspan> −100 mV:', 14, 'start'))
    o.append(T(lx + 34, 213, 'leakage 180 µW', 13, 'start', NX))
    o.append(T(lx + 34, 231, 'equal at 11.1 MHz', 13, 'start', NX))
    return 350, ''.join(o)
FIG[7] = (f7, 'Power of the example block against clock frequency on log scales. Switching power rises in proportion to f and passes 1.62 mW at 100 MHz; leakage is flat, so below the crossover (1.11 MHz, or 11.1 MHz with the lower-threshold transistors) leakage is the larger part.',
          'Log-log plot of power against clock frequency: a rising line for switching power through 1.62 milliwatts at 100 megahertz, a flat line for 18 microwatts of leakage crossing it at 1.11 megahertz, and a dashed flat line for 180 microwatts crossing at 11.1 megahertz.')


# ---- 3.8 power gating and break-even ----
def f8():
    o = []
    # left: header switch
    o.append(rail(70, 300, 40, 'V<tspan baseline-shift="sub" font-size="11">DD</tspan>'))
    o.append(mos(156, 80, 'p', 'left', gl=40, c=LV))
    o.append(L(170, 40, 170, 50, LV, 2))
    o.append(T(105, 85, 'sleep', 14, 'end', LV, True)); o.append(T(186, 76, 'high-V<tspan baseline-shift="sub" font-size="11">t</tspan> header', 13, 'start', MUT))
    o.append(L(170, 110, 170, 122, LV, 2))
    o.append(L(60, 122, 290, 122, LV, 2.5, '6 3')); o.append(T(60, 140, 'virtual V<tspan baseline-shift="sub" font-size="11">DD</tspan>', 13, 'start', LV))
    o.append(L(170, 122, 170, 150, INK, 2))
    o.append(boxt(70, 150, 200, 70, ['logic block', 'leaks 0.5 mW'], size=14, bold_first=True))
    o.append(boxt(70, 236, 96, 44, ['retention', 'flip-flops'], size=13, fill=ACS))
    o.append(boxt(176, 236, 94, 44, ['isolation', 'cells'], size=13, fill=NXS, stroke=NX))
    o.append(L(270, 258, 300, 258, INK, 2, arrow='n')); o.append(T(304, 263, 'out', 13, 'start', MUT))
    o.append(L(170, 220, 170, 236, INK, 1.5))
    o.append(T(170, 312, 'ground', 13, fill=MUT)); o.append(L(60, 296, 290, 296, INK, 2.5))
    o.append(L(118, 280, 118, 296, INK, 1.5)); o.append(L(223, 280, 223, 296, INK, 1.5))
    # right: energy saved vs idle time
    x0, x1, y0, y1 = 400, 680, 60, 290
    fx = lambda t: x0 + t / 10 * (x1 - x0); fy = lambda e: y1 - e / 5 * (y1 - y0)
    o.append(plot_axes(x0, x1, y0, y1, [0, 2, 3, 6, 10], [0, 1, 1.5, 3, 5], fx, fy, 'idle time (µs)', 'energy (nJ)', lambda t: f'{t:g}', lambda e: f'{e:g}'))
    o.append(L(fx(0), fy(0), fx(10), fy(5), AC, 3)); o.append(T(fx(7.2), fy(3.6) - 12, 'leakage saved', 14, 'end', AC, True))
    o.append(L(fx(0), fy(1.5), fx(10), fy(1.5), LV, 2.5)); o.append(T(fx(10), fy(1.5) + 20, 'wake cost 1.5 nJ', 14, 'end', LV, True))
    o.append(C(fx(3), fy(1.5), 6, NX)); o.append(L(fx(3), fy(1.5), fx(3), y1, NX, 1.5, '3 3'))
    o.append(T(fx(3) + 8, fy(1.5) - 28, 'break-even 3 µs', 14, 'start', NX, True))
    o.append(C(fx(2), fy(1.0), 5, MUT)); o.append(C(fx(10), fy(5), 5, MUT))
    return 348, ''.join(o)
FIG[8] = (f8, 'Left: a power-gated block behind a high-V<sub>t</sub> header switch, with retention flip-flops to keep its state and isolation cells on its outputs. Right: the second worked example; the 0.5 mW of leakage saved overtakes the 1.5 nJ wake-up cost after 3 µs of idle time.',
          'Left, a block diagram: VDD, a pMOS header driven by a sleep signal, a virtual VDD rail feeding a logic block with retention flip-flops and isolation cells. Right, a plot of energy against idle time: a rising line for leakage saved crosses a flat 1.5 nanojoule wake cost at 3 microseconds.')


# ---- 3.9 the compound gate Y = NOT(A(B + C)) ----
def f9():
    o = []
    o.append(rail(120, 460, 34, 'V<tspan baseline-shift="sub" font-size="11">DD</tspan>'))
    # PUN: pMOS A (width 2) in parallel with series (pMOS B, pMOS C) (width 4)
    # branch 1: A at x=200 ; branch 2: B over C at x=380
    o.append(mos(186, 90, 'p', 'left', gl=30, lab='A (2)', c=AC)); o.append(L(200, 34, 200, 60, AC, 2))
    o.append(mos(366, 76, 'p', 'left', gl=30, lab='B (4)', c=AC)); o.append(L(380, 34, 380, 46, AC, 2))
    o.append(mos(366, 136, 'p', 'left', gl=30, lab='C (4)', c=AC))
    o.append(L(380, 106, 380, 106, AC, 2))
    o.append(L(200, 120, 200, 180, AC, 2)); o.append(L(380, 166, 380, 180, AC, 2))
    o.append(L(200, 180, 380, 180, INK, 2)); o.append(dot(290, 180))
    o.append(L(290, 180, 560, 180, INK, 2)); o.append(T(566, 186, 'Y', 16, 'start', INK, True))
    # PDN: nMOS A (2) in series with parallel (nMOS B, nMOS C) (2 each)
    o.append(L(290, 180, 290, 204, INK, 2))
    o.append(mos(276, 234, 'n', 'left', gl=30, lab='A (2)', c=LV))
    o.append(L(290, 264, 290, 280, LV, 2)); o.append(L(220, 280, 360, 280, LV, 2)); o.append(dot(290, 280, LV))
    o.append(L(220, 280, 220, 286, LV, 2)); o.append(L(360, 280, 360, 286, LV, 2))
    o.append(mos(206, 316, 'n', 'left', gl=30, lab='B (2)', c=LV))
    o.append(mos(346, 316, 'n', 'left', gl=30, lab='C (2)', c=LV))
    o.append(L(220, 346, 220, 356, LV, 2)); o.append(L(360, 346, 360, 356, LV, 2)); o.append(L(220, 356, 360, 356, LV, 2))
    o.append(gnd(290, 356))
    # notes
    o.append(T(470, 70, 'pull-up (pMOS):', 14, 'start', AC, True)); o.append(T(470, 90, 'A ∥ (B then C)', 14, 'start'))
    o.append(T(470, 250, 'pull-down (nMOS):', 14, 'start', LV, True)); o.append(T(470, 270, 'A then (B ∥ C)', 14, 'start'))
    o.append(T(470, 320, 'g<tspan baseline-shift="sub" font-size="11">A</tspan> = (2 + 2)/3 = 4/3', 14, 'start'))
    o.append(T(470, 342, 'g<tspan baseline-shift="sub" font-size="11">B</tspan> = g<tspan baseline-shift="sub" font-size="11">C</tspan> = (2 + 4)/3 = 2', 14, 'start'))
    o.append(T(470, 130, '(number) = width', 13, 'start', MUT)); o.append(T(470, 148, '(unit inverter: n 1, p 2)', 13, 'start', MUT))
    return 384, ''.join(o)
FIG[9] = (f9, 'The six-transistor gate Y = NOT(A·(B + C)) of the worked example, with each width chosen for the drive of a unit inverter. The pull-up is the dual of the pull-down: the series pair B, C becomes a parallel pair below the output.',
          'Transistor schematic: between VDD and Y, a pMOS A in parallel with pMOS B and C in series; between Y and ground, an nMOS A in series with nMOS B and C in parallel. Widths 2 for A in both networks, 4 for pMOS B and C, 2 for nMOS B and C.')


# ---- 3.10 nMOS switch versus transmission gate ----
def f10():
    o = []
    # left panel: nMOS switch, vertical channel turned sideways is awkward; draw horizontal symbol
    def hswitch(x1, x2, y, kind, c):
        mx = (x1 + x2) / 2
        out = [L(x1, y, mx - 20, y, c, 2), L(mx + 20, y, x2, y, c, 2),
               L(mx - 20, y, mx - 20, y - 10, c, 2), L(mx + 20, y, mx + 20, y - 10, c, 2),
               L(mx - 24, y - 10, mx + 24, y - 10, c, 2.5), L(mx - 20, y - 17, mx + 20, y - 17, c, 2)]
        if kind == 'p':
            out.append(f'<circle cx="{mx:.1f}" cy="{y - 21:.1f}" r="4" style="fill:var(--fig);stroke:{c};stroke-width:2"/>')
            out.append(L(mx, y - 25, mx, y - 40, c, 2))
        else:
            out.append(L(mx, y - 17, mx, y - 40, c, 2))
        return ''.join(out)
    def hswitch_dn(x1, x2, y, kind, c):
        mx = (x1 + x2) / 2
        out = [L(x1, y, mx - 20, y, c, 2), L(mx + 20, y, x2, y, c, 2),
               L(mx - 20, y, mx - 20, y + 10, c, 2), L(mx + 20, y, mx + 20, y + 10, c, 2),
               L(mx - 24, y + 10, mx + 24, y + 10, c, 2.5), L(mx - 20, y + 17, mx + 20, y + 17, c, 2)]
        if kind == 'p':
            out.append(f'<circle cx="{mx:.1f}" cy="{y + 21:.1f}" r="4" style="fill:var(--fig);stroke:{c};stroke-width:2"/>')
            out.append(L(mx, y + 25, mx, y + 40, c, 2))
        else:
            out.append(L(mx, y + 17, mx, y + 40, c, 2))
        return ''.join(out)
    o.append(T(180, 28, 'nMOS switch', 15, bold=True, fill=LV))
    y = 130
    o.append(hswitch(70, 290, y, 'n', LV))
    o.append(T(180, y - 48, 'C = 1.8 V', 14))
    o.append(T(66, y + 5, 'A = 1.8 V', 14, 'end'))
    o.append(dot(290, y)); o.append(cap_v(290, y))
    o.append(T(300, y - 10, 'Y', 15, 'start', INK, True))
    o.append(T(180, 230, 'Y stops at 1.8 − V<tspan baseline-shift="sub" font-size="11">tn</tspan>', 14))
    o.append(T(180, 254, 'no body effect: 1.30 V', 14, fill=MUT))
    o.append(T(180, 278, 'with body effect: 1.10 V', 15, bold=True, fill=LV))
    o.append(T(180, 300, '(V<tspan baseline-shift="sub" font-size="11">tn</tspan> rises to 0.70 V)', 13, fill=MUT))
    # right panel: TG
    o.append(T(550, 28, 'transmission gate', 15, bold=True, fill=AC))
    xa, xb, yt, ybn = 455, 645, 110, 170
    o.append(T(400, 145, 'A = 1.8 V', 14, 'end'))
    o.append(L(406, 140, xa, 140, INK, 2)); o.append(L(xa, yt, xa, ybn, INK, 2)); o.append(dot(xa, 140))
    o.append(hswitch(xa, xb, yt, 'p', AC)); o.append(hswitch_dn(xa, xb, ybn, 'n', LV))
    o.append(L(xb, yt, xb, ybn, INK, 2)); o.append(dot(xb, 140)); o.append(L(xb, 140, 672, 140, INK, 2))
    o.append(T(550, yt - 48, 'C̄ = 0 V', 14, fill=AC)); o.append(T(550, ybn + 58, 'C = 1.8 V', 14, fill=LV))
    o.append(T(678, 132, 'Y', 15, 'start', INK, True))
    o.append(T(550, 278, 'pMOS carries the top of the swing:', 14))
    o.append(T(550, 300, 'Y = 1.8 V', 15, bold=True, fill=AC))
    return 320, ''.join(o)
FIG[10] = (f10, 'Passing a 1 at 1.8 V. Left: an nMOS switch alone stops one (body-raised) threshold short, at 1.10 V in the worked example. Right: in a transmission gate the parallel pMOS, driven by C̄, keeps conducting and Y reaches 1.8 V.',
          'Two circuits. Left, an nMOS pass transistor with gate and input at 1.8 volts charging an output capacitor to only 1.10 volts. Right, a transmission gate of a pMOS driven by C bar and an nMOS driven by C in parallel, passing the full 1.8 volts.')


# ---- 3.11 domino AND gate ----
def f11():
    o = []
    o.append(rail(120, 420, 34, 'V<tspan baseline-shift="sub" font-size="11">DD</tspan>'))
    # precharge pMOS at x=200 (terminal)
    o.append(mos(186, 76, 'p', 'left', gl=30, lab='precharge', c=AC)); o.append(L(200, 34, 200, 46, AC, 2))
    o.append(T(148, 66, 'φ', 15, 'end', AC, True))
    # keeper at x=330 (gate on the right side)
    o.append(mos(344, 76, 'p', 'right', gl=26, c=NX)); o.append(L(330, 34, 330, 46, NX, 2))
    o.append(T(340, 124, 'keeper', 13, 'start', NX))
    o.append(L(200, 106, 200, 140, INK, 2)); o.append(L(330, 106, 330, 140, NX, 2))
    o.append(L(200, 140, 450, 140, INK, 2.5)); o.append(dot(200, 140)); o.append(dot(330, 140))
    o.append(T(212, 160, 'X', 15, 'start', INK, True))
    o.append(L(260, 140, 260, 150, INK, 2)); o.append(cap_v(260, 150))
    o.append(T(280, 178, 'C<tspan baseline-shift="sub" font-size="11">X</tspan> = 50 fF', 14, 'start', AC, True))
    # inverter
    s, xo = inv_sym(450, 140, 38); o.append(s)
    o.append(L(xo, 140, 620, 140, INK, 2)); o.append(T(626, 146, 'out', 14, 'start', INK, True))
    o.append(P([(560, 140), (560, 76), (377, 76)], NX, 2)); o.append(dot(560, 140))
    # PDN: A then B then foot
    o.append(L(200, 140, 200, 196, INK, 2))
    o.append(mos(186, 226, 'n', 'left', gl=30, lab='A', c=LV))
    o.append(L(200, 256, 200, 262, LV, 2)); o.append(dot(200, 262))
    o.append(L(200, 262, 250, 262, MUT, 1.5)); o.append(cap_v(250, 262, MUT, 10))
    o.append(T(268, 290, 'C<tspan baseline-shift="sub" font-size="11">int</tspan> = 10 fF', 14, 'start', MUT, True))
    o.append(mos(186, 292, 'n', 'left', gl=30, lab='B', c=LV))
    o.append(L(200, 322, 200, 328, INK, 2))
    o.append(mos(186, 358, 'n', 'left', gl=30, lab='foot', c=AC)); o.append(T(148, 350, 'φ', 15, 'end', AC, True))
    o.append(gnd(200, 388))
    # notes
    o.append(T(420, 250, 'A on, B off: 90 fC shared over 60 fF', 14, 'start'))
    o.append(T(420, 272, 'V<tspan baseline-shift="sub" font-size="11">X</tspan> = 1.8 → 1.50 V', 15, 'start', LV, True))
    o.append(T(420, 296, 'safe only if C<tspan baseline-shift="sub" font-size="11">int</tspan> ≤ 10 fF', 14, 'start'))
    o.append(T(420, 330, 'leak 10 nA: holds 0.3 V for 1.5 µs', 14, 'start', MUT))
    return 416, ''.join(o)
FIG[11] = (f11, 'The domino AND gate of the worked examples. When φ is low the precharge pMOS charges X to 1.8 V; when φ is high the foot turns on. If A turns on while B stays off, X shares its charge with the 10 fF internal node and falls to 1.50 V; the weak keeper, driven from the output, tops it back up.',
          'A domino AND gate: a precharge pMOS and a keeper pMOS from VDD to the dynamic node X of 50 femtofarads, an output inverter whose output drives the keeper gate, and below X an nMOS for A, an internal node of 10 femtofarads, an nMOS for B and a clocked foot transistor to ground.')


spec = make_spec(FIG)
