"""Claude's hand-drawn figures for ee-pe-u3 (Power Electronics: DC-DC converters), one per chapter, drawn from each
chapter's own worked example and numbers: the circuits with their component values, and the waveforms and curves computed
from the examples (pulse trains, inductor ramps, the boost gain with winding resistance, switching overlap power).
The circuit helpers are reused by the model answers in the question bank (circuit_svg). Colours are the shell's CSS
variables only."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """V_o, T_on, i_L ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔℓ])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


FIG = {}


# ---------------------------------------------------------------- circuit symbols
def _frame(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    pt = lambda s, t: (x1 + ux * s - uy * t, y1 + uy * s + ux * t)
    return n, pt


def wire(*pts, c=INK, w=2):
    return P(list(pts), c, w)


def dot(x, y, c=INK, r=4):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c}"/>'


def res(x1, y1, x2, y2, c=AC, body=44):
    n, pt = _frame(x1, y1, x2, y2)
    a = (n - body) / 2
    zz = [pt(0, 0), pt(a, 0)]
    for i in range(6):
        zz.append(pt(a + (2 * i + 1) * body / 12, -8 if i % 2 == 0 else 8))
    zz += [pt(a + body, 0), pt(n, 0)]
    return P(zz, c, 2.2)


def ind(x1, y1, x2, y2, c=AC, body=52, humps=4, flip=False):
    n, pt = _frame(x1, y1, x2, y2)
    a = (n - body) / 2
    w = body / humps
    s0, s1 = pt(0, 0), pt(a, 0)
    d = f'M{s0[0]:.1f},{s0[1]:.1f} L{s1[0]:.1f},{s1[1]:.1f}'
    for i in range(humps):
        e = pt(a + (i + 1) * w, 0)
        d += f' A{w / 2:.1f},{w / 2:.1f} 0 0 {0 if flip else 1} {e[0]:.1f},{e[1]:.1f}'
    e = pt(n, 0)
    d += f' L{e[0]:.1f},{e[1]:.1f}'
    return f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:2.4"/>'


def cap(x1, y1, x2, y2, c=AC, gap=9, plate=30):
    n, pt = _frame(x1, y1, x2, y2)
    m = n / 2
    o = [L(*pt(0, 0), *pt(m - gap / 2, 0), INK, 2), L(*pt(m + gap / 2, 0), *pt(n, 0), INK, 2)]
    o += [L(*pt(m - gap / 2, -plate / 2), *pt(m - gap / 2, plate / 2), c, 3), L(*pt(m + gap / 2, -plate / 2), *pt(m + gap / 2, plate / 2), c, 3)]
    return ''.join(o)


def diode(x1, y1, x2, y2, c=NX, size=13):
    """diode from anode (x1, y1) to cathode (x2, y2): triangle points to the cathode bar"""
    n, pt = _frame(x1, y1, x2, y2)
    m = n / 2
    a, b = m - size * 0.6, m + size * 0.6
    tri = [pt(a, -size * 0.75), pt(a, size * 0.75), pt(b, 0)]
    o = [L(*pt(0, 0), *pt(a, 0), INK, 2), L(*pt(b, 0), *pt(n, 0), INK, 2)]
    o.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in tri)}" style="fill:{c};stroke:{c};stroke-width:1.5"/>')
    o.append(L(*pt(b, -size * 0.75), *pt(b, size * 0.75), c, 3))
    return ''.join(o)


def sw(x1, y1, x2, y2, c=AC, closed=False):
    """switch between two terminals: two contacts and a blade (open unless closed)"""
    n, pt = _frame(x1, y1, x2, y2)
    a, b = n * 0.25, n * 0.75
    o = [L(*pt(0, 0), *pt(a, 0), INK, 2), L(*pt(b, 0), *pt(n, 0), INK, 2)]
    o.append(f'<circle cx="{pt(a, 0)[0]:.1f}" cy="{pt(a, 0)[1]:.1f}" r="3.5" style="fill:var(--fig);stroke:{c};stroke-width:2"/>')
    o.append(f'<circle cx="{pt(b, 0)[0]:.1f}" cy="{pt(b, 0)[1]:.1f}" r="3.5" style="fill:var(--fig);stroke:{c};stroke-width:2"/>')
    end = pt(b - 3, -3) if closed else pt(b - 2, -16)
    o.append(L(*pt(a + 2, -1), *end, c, 3))
    return ''.join(o)


def vsrc(cx, cy, r=18, c=LV, label=None, side='left', plus='up'):
    o = [f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2.4"/>']
    sgn = -1 if plus == 'up' else 1
    o.append(T(cx, cy + sgn * r * 0.42 + 5, '+', 15, bold=True, fill=c))
    o.append(T(cx, cy - sgn * r * 0.42 + 5, '−', 15, bold=True, fill=c))
    if label:
        if side == 'left': o.append(T(cx - r - 7, cy + 5, label, 14, 'end', bold=True))
        else: o.append(T(cx + r + 7, cy + 5, label, 14, 'start', bold=True))
    return ''.join(o)


def path_hi(pts, c, w=9):
    """a soft wide band behind wires showing where current flows"""
    return f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:none;stroke:{c};stroke-width:{w};stroke-opacity:0.28;stroke-linejoin:round;stroke-linecap:round"/>'


def coil_v(x, y1, y2, c=AC, right=True, humps=4):
    """vertical winding drawn as humps bulging right (or left)"""
    return ind(x, y1, x, y2, c, body=(y2 - y1) - 8, humps=humps, flip=not right)


# ---------------------------------------------------------------- reusable circuits (chapter figures and bank answers)
def buck_circuit(ox, oy, vals=None, h=110, show_paths=False):
    """buck: source, S on top, D_f down to the return rail, L, C and R. Returns svg parts and the width used (about 400)."""
    v = {'Vs': 'V_s', 'S': 'S', 'D': 'D_f', 'L': 'L', 'C': 'C', 'R': 'R', 'Vo': 'V_o'}
    v.update(vals or {})
    yt, yb = oy, oy + h
    xs, x1, x2, xa, xl2, xc, xr = ox + 30, ox + 70, ox + 140, ox + 170, ox + 270, ox + 300, ox + 380
    o = []
    if show_paths:
        o.append(path_hi([(xs, yb - 20), (xs, yt), (xl2, yt), (xr, yt), (xr, yb), (xs, yb)], LV, 10))
        o.append(path_hi([(xa + 6, yb - 6), (xa + 6, yt + 6), (xr - 6, yt + 6), (xr - 6, yb - 6), (xa + 6, yb - 6)], NX, 8))
    o.append(wire((xs, yt), (x1, yt))); o.append(sw(x1, yt, x2, yt)); o.append(wire((x2, yt), (xa, yt)))
    o.append(ind(xa, yt, xl2, yt)); o.append(wire((xl2, yt), (xr, yt)))
    o.append(wire((xs, yb), (xr, yb)))
    o.append(wire((xs, yt), (xs, oy + h / 2 - 18))); o.append(wire((xs, oy + h / 2 + 18), (xs, yb)))
    o.append(vsrc(xs, oy + h / 2, label=v['Vs']))
    o.append(diode(xa, yb, xa, yt))
    o.append(cap(xc, yt, xc, yb)); o.append(res(xr, yt, xr, yb))
    for x in (xa, xc, xr): o.append(dot(x, yt)); o.append(dot(x, yb))
    o.append(T((x1 + x2) / 2, yt - 22, v['S'], 14, bold=True))
    o.append(T(xa - 14, oy + h / 2 + 5, v['D'], 14, 'end', bold=True, fill=NX))
    o.append(T((xa + xl2) / 2, yt - 18, v['L'], 14, bold=True))
    o.append(T(xc - 20, oy + h / 2 + 5, v['C'], 14, 'end', bold=True))
    o.append(T(xr + 14, oy + h / 2 + 5, v['R'], 14, 'start', bold=True))
    o.append(T(xr + 10, yt - 8, '+', 15, 'start', bold=True, fill=LV)); o.append(T(xr + 10, yb + 16, '−', 15, 'start', bold=True, fill=LV))
    o.append(T(xr - 6, yb + 26, v['Vo'], 14, 'end', bold=True, fill=LV))
    return ''.join(o)


def boost_circuit(ox, oy, vals=None, h=110):
    v = {'Vs': 'V_s', 'L': 'L', 'S': 'S', 'D': 'D1', 'C': 'C', 'R': 'R', 'Vo': 'V_o'}
    v.update(vals or {})
    yt, yb = oy, oy + h
    xs, xl1, xl2, xa, xd2, xc, xr = ox + 30, ox + 60, ox + 150, ox + 180, ox + 260, ox + 290, ox + 370
    o = []
    o.append(wire((xs, yt), (xl1, yt))); o.append(ind(xl1, yt, xl2, yt)); o.append(wire((xl2, yt), (xa, yt)))
    o.append(diode(xa, yt, xd2, yt)); o.append(wire((xd2, yt), (xr, yt)))
    o.append(wire((xs, yb), (xr, yb)))
    o.append(wire((xs, yt), (xs, oy + h / 2 - 18))); o.append(wire((xs, oy + h / 2 + 18), (xs, yb)))
    o.append(vsrc(xs, oy + h / 2, label=v['Vs']))
    o.append(sw(xa, yt, xa, yb)); o.append(cap(xc, yt, xc, yb)); o.append(res(xr, yt, xr, yb))
    for x in (xa, xc, xr): o.append(dot(x, yt)); o.append(dot(x, yb))
    o.append(T((xl1 + xl2) / 2, yt - 18, v['L'], 14, bold=True))
    o.append(T((xa + xd2) / 2, yt - 18, v['D'], 14, bold=True, fill=NX))
    o.append(T(xa + 14, oy + h / 2 + 5, v['S'], 14, 'start', bold=True))
    o.append(T(xc - 20, oy + h / 2 + 5, v['C'], 14, 'end', bold=True))
    o.append(T(xr + 14, oy + h / 2 + 5, v['R'], 14, 'start', bold=True))
    o.append(T(xr + 10, yt - 8, '+', 15, 'start', bold=True, fill=LV)); o.append(T(xr + 10, yb + 16, '−', 15, 'start', bold=True, fill=LV))
    o.append(T(xr - 6, yb + 26, v['Vo'], 14, 'end', bold=True, fill=LV))
    return ''.join(o)


def buckboost_circuit(ox, oy, vals=None, h=110, state=None):
    """inverting buck-boost: S from the source to node A, L from A down to the return rail, the diode from the output
    node (anode) to A (cathode), C and R from the output node to the rail. state 'on' or 'off' shades the current path."""
    v = {'Vs': 'V_s', 'S': 'S', 'L': 'L', 'D': 'D', 'C': 'C', 'R': 'R', 'Vo': 'V_o'}
    v.update(vals or {})
    yt, yb = oy, oy + h
    xs, x1, x2, xa, xd2, xc, xr = ox + 30, ox + 60, ox + 120, ox + 150, ox + 230, ox + 255, ox + 315
    o = []
    if state == 'on':
        o.append(path_hi([(xs, yb), (xs, yt), (xa, yt), (xa, yb), (xs, yb)], LV, 10))
    if state == 'both':
        o.append(path_hi([(xs, yb), (xs, yt), (xa - 5, yt), (xa - 5, yb), (xs, yb)], LV, 10))
        o.append(path_hi([(xa + 5, yb - 5), (xa + 5, yt + 5), (xr - 5, yt + 5), (xr - 5, yb - 5), (xa + 5, yb - 5)], NX, 8))
    if state == 'off':
        o.append(path_hi([(xa, yb), (xa, yt), (xd2, yt), (xr, yt), (xr, yb), (xa, yb)], NX, 10))
    o.append(wire((xs, yt), (x1, yt))); o.append(sw(x1, yt, x2, yt, closed=(state == 'on'))); o.append(wire((x2, yt), (xa, yt)))
    o.append(diode(xd2, yt, xa, yt)); o.append(wire((xd2, yt), (xr, yt)))
    o.append(wire((xs, yb), (xr, yb)))
    o.append(wire((xs, yt), (xs, oy + h / 2 - 18))); o.append(wire((xs, oy + h / 2 + 18), (xs, yb)))
    o.append(vsrc(xs, oy + h / 2, label=v['Vs']))
    o.append(ind(xa, yt, xa, yb)); o.append(cap(xc, yt, xc, yb)); o.append(res(xr, yt, xr, yb))
    for x in (xa, xc, xr): o.append(dot(x, yt)); o.append(dot(x, yb))
    o.append(T((x1 + x2) / 2, yt - 22, v['S'], 14, bold=True))
    o.append(T(xc - 20, oy + h / 2 + 5, v['C'], 14, 'end', bold=True))
    o.append(T(xa - 4, yt - 12, 'A', 14, 'end', bold=True, fill=MUT))
    o.append(T(xa + 18, oy + h / 2 + 5, v['L'], 14, 'start', bold=True))
    o.append(T((xa + xd2) / 2, yt - 18, v['D'], 14, bold=True, fill=NX))
    o.append(T(xr + 12, oy + h / 2 + 5, v['R'], 14, 'start', bold=True))
    o.append(T(xr + 10, yt - 8, '−', 15, 'start', bold=True, fill=LV)); o.append(T(xr + 10, yb + 16, '+', 15, 'start', bold=True, fill=LV))
    o.append(T(xr - 4, yb + 26, v['Vo'], 14, 'end', bold=True, fill=LV))
    return ''.join(o)


def circuit_svg(kind, vals=None):
    """a stand-alone circuit for a model answer, drawn 1.55 times larger so it reads on a phone: returns {h, body, aria}"""
    if kind == 'buck':
        body = buck_circuit(30, 40, vals); aria = 'Buck converter: source, switch S, freewheeling diode to the return rail, inductor L, capacitor C and load R.'
    elif kind == 'boost':
        body = boost_circuit(30, 40, vals); aria = 'Boost converter: source, inductor L, switch S to the return rail, diode D1 to capacitor C and load R.'
    else:
        body = buckboost_circuit(60, 40, vals); aria = 'Buck-boost converter: switch S from the source to node A, inductor L from A to the rail, diode from the output to A, capacitor and load.'
    return {'h': 300, 'body': f'<g transform="scale(1.55)">{body}</g>', 'aria': aria}


def three_cells_svg():
    """buck, boost and buck-boost stacked for the comparison question, drawn 1.55 times larger"""
    o = []
    for j, (fn, name) in enumerate([(buck_circuit, 'Buck: V_o = D·V_s'), (boost_circuit, 'Boost: V_o = V_s/(1 − D)'), (buckboost_circuit, 'Buck-boost: V_o = −D·V_s/(1 − D)')]):
        y0 = 22 + j * 186
        o.append(T(225, y0, name, 14, bold=True))
        o.append(fn(30 if fn is not buckboost_circuit else 60, y0 + 52, h=90))
    return {'h': 912, 'body': '<g transform="scale(1.55)">' + ''.join(o) + '</g>', 'aria': 'Three circuits stacked: the buck, the boost and the inverting buck-boost converter, each with its gain.'}


# ---------------------------------------------------------------- 3.1 chopper circuit and the two pulse trains of the example
def f1():
    o = []
    # circuit, left
    yt, yb = 70, 200
    xs, x1, x2, xa, xl = 50, 90, 150, 190, 270
    o.append(T(160, 30, 'Chopper with R-L load', 14, bold=True))
    o.append(wire((xs, yt), (x1, yt))); o.append(sw(x1, yt, x2, yt)); o.append(wire((x2, yt), (xl, yt)))
    o.append(wire((xs, yb), (xl, yb)))
    o.append(wire((xs, yt), (xs, 117))); o.append(wire((xs, 153), (xs, yb)))
    o.append(vsrc(xs, 135)); o.append(T(xs + 24, 140, '200 V', 14, 'start', bold=True))
    o.append(diode(xa, yb, xa, yt)); o.append(dot(xa, yt)); o.append(dot(xa, yb))
    o.append(res(xl, yt, xl, 135)); o.append(ind(xl, 135, xl, yb))
    o.append(T(120, yt - 22, 'S', 14, bold=True)); o.append(T(120, yt + 26, 'f_s, T_on', 13, fill=MUT))
    o.append(T(xa + 14, 140, 'D_f', 14, 'start', bold=True, fill=NX))
    o.append(T(xl + 14, 107, 'R = 10 Ω', 14, 'start', bold=True)); o.append(T(xl + 14, 172, 'L large', 14, 'start', bold=True))
    o.append(T(xl + 14, 190, 'i_o smooth', 13, 'start', MUT))
    o.append(T(160, 250, 'switch on: v_o = 200 V', 13, fill=LV)); o.append(T(160, 270, 'switch off: D_f carries i_o and v_o ≈ 0', 13, fill=NX))
    # waveforms, right
    fx = lin(0, 3, 390, 700)
    for j, (f, D, Vo, Po) in enumerate([(1, 0.4, 80, 640), (2, 0.8, 160, 2560)]):
        top = 84 + j * 150
        fy = lin(0, 200, top + 90, top)
        o.append(L(fx(0), fy(0), fx(3), fy(0), L2, 1.5)); o.append(L(fx(0), fy(0), fx(0), fy(220), L2, 1.5))
        o.append(T(fx(0) - 6, fy(200) + 5, '200', 13, 'end', MUT)); o.append(T(fx(0) - 6, fy(0) + 5, '0', 13, 'end', MUT))
        Tp = 1 / f
        pts = [(fx(0), fy(0))]
        t = 0
        while t < 3 - 1e-9:
            pts += [(fx(t), fy(0)), (fx(t), fy(200)), (fx(t + 0.4), fy(200)), (fx(t + 0.4), fy(0))]
            t += Tp
        pts.append((fx(3), fy(0)))
        o.append(P(pts, AC, 2.4))
        o.append(L(fx(0), fy(Vo), fx(3), fy(Vo), LV, 2, dash='6 4'))
        o.append(Tb(fx(3) - 4, fy(Vo) - 6, f'average {Vo} V', 13, 'end', LV, bold=True))
        o.append(T(fx(0), top - 14, f'f_s = {f} kHz (T = {Tp:g} ms): D = {D}, P_o = {Po} W', 13, 'start', bold=True))
    for t in (0, 1, 2, 3): o.append(T(fx(t), 346, str(t), 13, fill=MUT))
    o.append(T(545, 366, 'time (ms); every pulse is 200 V for T_on = 0.4 ms', 13, fill=MUT))
    o.append(T(545, 36, 'load voltage v_o (V)', 13, fill=MUT, bold=True))
    return 380, ''.join(o)


FIG[1] = (f1, 'The worked example’s chopper and its load voltage. With the on-time fixed at 0.4 ms, going from 1 kHz to 2 kHz raises D '
              'from 0.4 to 0.8, so the average output rises from 80 V to 160 V.',
          'Left: a chopper circuit with a 200 volt source, switch S, freewheeling diode and a 10 ohm resistor in series with a large '
          'inductor. Right: two pulse trains of 200 volt pulses 0.4 milliseconds wide, one with a 1 millisecond period and average 80 volts, '
          'one with a 0.5 millisecond period and average 160 volts.')


# ---------------------------------------------------------------- 3.2 series pass regulator and the two power splits
def f2():
    o = []
    o.append(T(190, 26, 'Series linear regulator, 12 V to 5 V at 1 A', 14, bold=True))
    yt, yb = 70, 250
    # input
    o.append(wire((40, yt), (115, yt))); o.append(wire((40, yb), (345, yb)))
    o.append(wire((40, yt), (40, 142))); o.append(wire((40, 178), (40, yb))); o.append(vsrc(40, 160, label='', side='left'))
    o.append(T(60, 128, '12 V', 14, 'start', bold=True))
    # pass transistor as a labelled series element: 12 V in, 5 V out
    bx = 160
    o.append(boxt(bx - 45, yt - 18, 90, 36, ['pass device'], NXS, NX, 13))
    o.append(wire((bx + 45, yt), (300, yt)))
    o.append(wire((bx, yt + 18), (bx, 160)))
    o.append(T(bx, yt - 30, '7 V across, 7 W of heat', 13, fill=NX, bold=True))
    o.append(T(bx + 8, 128, 'drive', 13, 'start', MUT))
    # error amplifier (triangle pointing up into the base)
    ex, ey = bx, 188
    o.append(P([(ex - 30, ey + 28), (ex + 30, ey + 28), (ex, ey - 28), (ex - 30, ey + 28)], AC, 2.2, fill=PANEL))
    o.append(T(ex - 12, ey + 22, '+', 14, bold=True)); o.append(T(ex + 12, ey + 22, '−', 14, bold=True))
    o.append(T(ex - 26, 170, 'error', 13, 'end', MUT)); o.append(T(ex - 26, 186, 'amplifier', 13, 'end', MUT))
    # reference to + input (left), divider tap to − input (right)
    o.append(wire((ex - 12, ey + 28), (ex - 12, 233), (140, 233)))
    o.append(boxt(80, 222, 60, 24, ['V_ref'], NXS, NX, 13))
    o.append(wire((110, 246), (110, yb)))
    # divider on output feeds - input
    o.append(wire((300, yt), (300, 120))); o.append(res(300, 120, 300, 175)); o.append(res(300, 190, 300, yb))
    o.append(wire((300, 175), (300, 190)))
    o.append(wire((300, 182), (205, 182), (205, 234), (ex + 12, 234), (ex + 12, ey + 28)))
    o.append(dot(300, 182)); o.append(T(308, 152, 'R1', 13, 'start')); o.append(T(308, 225, 'R2', 13, 'start'))
    o.append(wire((300, yt), (345, yt))); o.append(dot(300, yt)); o.append(dot(300, yb))
    o.append(T(345, yt - 10, '5 V, 1 A', 14, 'end', bold=True, fill=LV))
    o.append(T(190, 284, 'feedback holds βV_o = V_ref with β = R2/(R1 + R2)', 13, fill=MUT))
    # power bars
    fx = lin(0, 12, 400, 700)
    o.append(T(550, 26, 'Where the input power goes', 14, bold=True))
    rows = [(80, 'linear: 12 W in, η = 41.7 %', 5, 7), (190, 'switcher at 85 %: 5.88 W in', 5, 0.88)]
    for y, lab, out, heat in rows:
        o.append(T(400, y - 10, lab, 13, 'start', bold=True))
        o.append(R(fx(0), y, fx(out) - fx(0), 36, LVS, LV, 4)); o.append(T((fx(0) + fx(out)) / 2, y + 23, '5 W to load', 13, bold=True))
        o.append(R(fx(out), y, fx(out + heat) - fx(out), 36, NXS, NX, 4))
        if heat > 2: o.append(T((fx(out) + fx(out + heat)) / 2, y + 23, f'{heat:g} W heat', 13, bold=True))
        else: o.append(T(fx(out + heat) + 6, y + 23, f'{heat:g} W heat', 13, 'start', NX, bold=True))
    o.append(xaxis(400, 700, 254, [0, 4, 8, 12], fx, 'power (W)'))
    return 310, ''.join(o)


FIG[2] = (f2, 'The worked example’s 12 V to 5 V, 1 A supply. The linear regulator holds 5 V by dropping 7 V across its pass transistor, so 7 W of '
              'the 12 W input becomes heat; an 85 % switcher draws 5.88 W and wastes only 0.88 W.',
          'Left: a series linear regulator with a 12 volt input, a pass transistor carrying 7 volts, an error amplifier comparing a divider '
          'sample with a reference, and a 5 volt 1 amp output. Right: two power bars, 12 watts split into 5 watts to the load and 7 watts of '
          'heat, and 5.88 watts split into 5 watts and 0.88 watts.')


# ---------------------------------------------------------------- 3.3 buck circuit, inductor voltage and current
def f3():
    o = []
    o.append(buck_circuit(150, 40, {'Vs': '50 V', 'L': 'L = 100 µH', 'C': '220 µF', 'R': '5 Ω', 'Vo': 'V_o = 20 V'}, h=100, show_paths=True))
    o.append(T(40, 30, 'on: source → L → load', 13, 'start', LV, bold=True))
    o.append(T(680, 30, 'off: L → load → D_f', 13, 'end', NX, bold=True))
    fx = lin(0, 20, 120, 660)
    # v_L
    fyv = lin(-20, 30, 300, 210)
    o.append(L(fx(0), fyv(0), fx(20), fyv(0), L2, 1.5)); o.append(L(fx(0), fyv(34), fx(0), fyv(-24), L2, 1.5))
    o.append(T(fx(0) - 8, 210, 'v_L', 14, 'end', MUT, bold=True))
    for t0 in (0, 10):
        o.append(R(fx(t0), fyv(30), fx(t0 + 4) - fx(t0), fyv(0) - fyv(30), LVS, LV, 0))
        o.append(R(fx(t0 + 4), fyv(0), fx(t0 + 10) - fx(t0 + 4), fyv(-20) - fyv(0), NXS, NX, 0))
    o.append(T(fx(2), fyv(15) + 5, '+30 V', 13, bold=True)); o.append(T(fx(7), fyv(-10) + 5, '−20 V', 13, bold=True))
    o.append(T(fx(2), fyv(30) - 6, '120 V·µs', 13, fill=LV)); o.append(T(fx(7), fyv(-20) + 18, '−120 V·µs', 13, fill=NX))
    # i_L
    fyi = lin(3, 5, 440, 360)
    o.append(L(fx(0), fyi(3), fx(20), fyi(3), L2, 1.5)); o.append(L(fx(0), fyi(3), fx(0), fyi(5.1), L2, 1.5))
    o.append(T(fx(0) - 8, 360, 'i_L', 14, 'end', MUT, bold=True))
    for v in (3.4, 4.0, 4.6):
        o.append(T(fx(0) - 6, fyi(v) + 5, f'{v} A', 13, 'end', MUT)); o.append(L(fx(0) - 4, fyi(v), fx(0), fyi(v), L2, 1.5))
    o.append(L(fx(0), fyi(4), fx(20), fyi(4), MUT, 1.5, dash='5 4'))
    o.append(P([(fx(0), fyi(3.4)), (fx(4), fyi(4.6)), (fx(10), fyi(3.4)), (fx(14), fyi(4.6)), (fx(20), fyi(3.4))], AC, 2.8))
    o.append(T(fx(20) + 6, fyi(4) + 5, 'I_o', 13, 'start', MUT, bold=True))
    o.append(T(fx(4), fyi(4.6) - 8, 'peak 4.6 A', 13, bold=True))
    o.append(L(fx(10), fyi(4.6), fx(10), fyi(3.5), MUT, 1.5, arrow='m'))
    o.append(T(fx(10) - 8, fyi(4.3) + 5, 'ΔI_L = 1.2 A', 13, 'end', MUT, bold=True))
    for t in (0, 4, 10, 14, 20):
        o.append(T(fx(t), 462, f'{t}', 13, fill=MUT))
    o.append(T(400, 482, 'time (µs): on 4 µs, off 6 µs, T = 10 µs', 13, fill=MUT))
    return 494, ''.join(o)


FIG[3] = (f3, 'The worked example’s buck at D = 0.4. The inductor sees +30 V for 4 µs and −20 V for 6 µs; the two volt-second areas cancel, so '
              'its current ramps between 3.4 A and 4.6 A around the 4 A load current.',
          'Top: buck circuit with a 50 volt source, switch, freewheeling diode, 100 microhenry inductor, 220 microfarad capacitor and 5 ohm '
          'load at 20 volts; shaded paths show the on-state and off-state currents. Middle: inductor voltage, +30 volts for 4 microseconds then '
          '−20 volts for 6. Bottom: inductor current ramping between 3.4 and 4.6 amps around a 4 amp average.')


# ---------------------------------------------------------------- 3.4 boost circuit and its gain with and without winding resistance
def f4():
    o = []
    o.append(boost_circuit(150, 36, {'Vs': '24 V', 'L': 'L = 300 µH', 'C': '470 µF', 'R': '100 Ω', 'Vo': 'V_o = 60 V'}, h=100))
    fx = lin(0, 1, 110, 470)
    fy = lin(0, 10, 470, 230)
    o.append(axes(110, 470, 230, 470, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 2, 4, 6, 8, 10], fx, fy, 'duty ratio D', _sub('gain V_o/V_s'),
                  xfmt=lambda v: f'{v:g}', yfmt=str))
    ideal = [(fx(d / 100), fy(1 / (1 - d / 100))) for d in range(0, 91)]
    real = [(fx(d / 100), fy((1 - d / 100) / ((1 - d / 100) ** 2 + 0.01))) for d in range(0, 100)]
    o.append(P(ideal, AC, 2.8)); o.append(P(real, LV, 2.8, dash='7 4')); o.append(P([(fx(0), fy(0)), (fx(1), fy(1))], MUT, 2))
    o.append(T(fx(0.86), fy(9.6), 'ideal 1/(1 − D)', 13, 'end', AC, bold=True))
    o.append(Tb(fx(0.86), fy(5.4), 'peak 5 at D = 0.9', 13, 'end', LV, bold=True))
    o.append(T(fx(0.97), fy(0.55), 'buck D', 13, 'end', MUT))
    o.append(C(fx(0.6), fy(2.5), 5, AC)); o.append(C(fx(0.6), fy(0.4 / 0.17), 5, LV))
    o.append(Tb(fx(0.6) - 10, fy(2.5) - 10, '2.5 (60 V)', 13, 'end', AC, bold=True))
    o.append(R(492, 236, 216, 172, PANEL, LV, 8))
    for i, s_ in enumerate(['winding resistance r_L = 1 Ω,', 'load R = 100 Ω, x = 1 − D:', 'V_o/V_s = x/(x² + r_L/R)', 'D = 0.6: 2.35 (56.5 V)', 'D = 0.9: 5.0, the most', 'D = 0.95: 4.0']):
        o.append(T(504, 262 + i * 26, s_, 13, 'start', INK, bold=(i == 2)))
    o.append(T(600, 432, 'solid: ideal; dashed: with r_L', 13, fill=MUT))
    return 520, ''.join(o)


FIG[4] = (f4, 'The worked example’s boost: 24 V in, D = 0.6, 60 V out. The ideal gain 1/(1 − D) climbs without limit, but with only 1 Ω of winding '
              'resistance against the 100 Ω load the real gain peaks at 5 at D = 0.9 and then falls.',
          'Top: boost circuit with a 24 volt source, 300 microhenry inductor, switch to the return rail, diode D1, 470 microfarad capacitor '
          'and 100 ohm load at 60 volts. Bottom: gain against duty ratio, the ideal curve 1 over 1 minus D rising steeply, a dashed real curve '
          'peaking at 5 at D = 0.9, and the buck line D for comparison; the example point is marked at D = 0.6, gain 2.5.')


# ---------------------------------------------------------------- 3.5 buck-boost in its two states, and the Cuk circuit
def cuk_circuit(ox, oy, h=100):
    yt, yb = oy, oy + h
    xs, xl1a, xl1b, xa, xb, xl2a, xl2b, xc, xr = ox + 30, ox + 55, ox + 135, ox + 160, ox + 250, ox + 270, ox + 350, ox + 380, ox + 440
    o = []
    o.append(wire((xs, yt), (xl1a, yt))); o.append(ind(xl1a, yt, xl1b, yt)); o.append(wire((xl1b, yt), (xa, yt)))
    o.append(cap(xa, yt, xb, yt, NX)); o.append(wire((xb, yt), (xl2a, yt))); o.append(ind(xl2a, yt, xl2b, yt)); o.append(wire((xl2b, yt), (xr, yt)))
    o.append(wire((xs, yb), (xr, yb)))
    o.append(wire((xs, yt), (xs, oy + h / 2 - 18))); o.append(wire((xs, oy + h / 2 + 18), (xs, yb))); o.append(vsrc(xs, oy + h / 2, label='12 V'))
    o.append(sw(xa, yt, xa, yb)); o.append(diode(xb, yt, xb, yb))
    o.append(cap(xc, yt, xc, yb)); o.append(res(xr, yt, xr, yb))
    for x in (xa, xb, xc, xr): o.append(dot(x, yt)); o.append(dot(x, yb))
    o.append(T((xl1a + xl1b) / 2, yt - 18, 'L1', 14, bold=True)); o.append(T((xl2a + xl2b) / 2, yt - 18, 'L2', 14, bold=True))
    o.append(T((xa + xb) / 2, yt - 24, 'C1: 30 V', 14, bold=True, fill=NX))
    o.append(T(xa - 4, yt - 10, 'A', 13, 'end', MUT, bold=True)); o.append(T(xb + 4, yt - 10, 'B', 13, 'start', MUT, bold=True))
    o.append(T(xa + 12, oy + h / 2 + 5, 'S', 14, 'start', bold=True)); o.append(T(xb + 14, oy + h / 2 + 5, 'D', 14, 'start', bold=True, fill=NX))
    o.append(T(xc - 18, oy + h / 2 + 5, 'C2', 14, 'end', bold=True))
    o.append(T(xr + 10, yt - 8, '−', 15, 'start', bold=True, fill=LV)); o.append(T(xr + 10, yb + 16, '+', 15, 'start', bold=True, fill=LV))
    o.append(T(xr + 14, oy + h / 2 + 5, '−18 V', 14, 'start', bold=True, fill=LV))
    return ''.join(o)


def f5():
    o = []
    vals = {'Vs': '12 V', 'S': 'S', 'L': 'L', 'R': '10 Ω', 'Vo': 'V_o = −18 V'}
    o.append(buckboost_circuit(170, 56, vals, h=100, state='both'))
    o.append(T(20, 26, 'ON, 0.6 T: source → S → L', 13, 'start', LV, bold=True))
    o.append(T(700, 26, 'OFF, 0.4 T: L → rail → R → D', 13, 'end', NX, bold=True))
    o.append(T(20, 92, 'v_L = +12 V', 13, 'start', LV)); o.append(T(20, 110, 'i_L rises', 13, 'start', LV))
    o.append(T(700, 92, 'v_L = −18 V', 13, 'end', NX)); o.append(T(700, 110, 'i_L falls', 13, 'end', NX))
    o.append(T(360, 200, 'average I_L = I_o/(1 − D) = 1.8/0.4 = 4.5 A; the switch blocks 12 + 18 = 30 V', 13, fill=MUT))
    o.append(L(20, 216, 700, 216, L2, 1.2, dash='4 4'))
    o.append(T(360, 244, 'Cuk: same gain, a capacitor carries the energy, both port currents smooth', 13, bold=True))
    o.append(cuk_circuit(110, 284, h=100))
    o.append(T(360, 420, 'V_C1 = V_s/(1 − D) = 12/0.4 = 30 V; V_o = −12 × 0.6/0.4 = −18 V', 13, fill=MUT))
    return 436, ''.join(o)


FIG[5] = (f5, 'The worked example: 12 V in, D = 0.6, −18 V out. With the switch on, the source charges L; with it off, L drives its current up '
              'through the load and the diode, so the output node is pulled below the return rail. The Cuk does the same job with C1 at 30 V.',
          'Top: the buck-boost circuit drawn twice. On: shaded loop from the 12 volt source through the closed switch and the inductor. Off: '
          'shaded loop from the inductor through the diode and the 10 ohm load, output minus 18 volts. Bottom: the Cuk circuit with L1, switch, '
          'coupling capacitor C1 at 30 volts, diode, L2, C2 and the load at minus 18 volts.')


# ---------------------------------------------------------------- 3.6 flyback with the example's numbers, and the forward with its reset winding
def winding(x, y1, y2, right, c=AC, humps=4):
    return coil_v(x, y1, y2, c, right, humps)


def f6():
    o = []
    # flyback, left panel
    o.append(T(180, 24, 'Flyback: 48 V, 40 : 20 turns, D = 0.4', 14, bold=True))
    yt, yb = 64, 214
    xs, xp, xsec = 40, 150, 210
    o.append(wire((xs, yt), (xp, yt))); o.append(wire((xs, yb), (xp, yb)))
    o.append(wire((xs, yt), (xs, 121))); o.append(wire((xs, 157), (xs, yb))); o.append(vsrc(xs, 139)); o.append(T(xs + 24, 144, '48 V', 14, 'start', bold=True))
    o.append(winding(xp, yt, 150, right=True)); o.append(wire((xp, 150), (xp, 160)))
    o.append(sw(xp, 160, xp, yb))
    o.append(T(xp - 12, 192, 'S', 14, 'end', bold=True)); o.append(T(xp - 12, 110, 'N1 = 40', 13, 'end', bold=True))
    o.append(L(176, yt + 6, 176, 150, MUT, 2)); o.append(L(184, yt + 6, 184, 150, MUT, 2))
    o.append(T(180, 172, 'gap', 13, fill=MUT))
    o.append(winding(xsec, yt, 150, right=False))
    o.append(dot(xp - 12, yt + 14, AC, 4)); o.append(dot(xsec + 12, 140, AC, 4))
    o.append(T(xsec + 12, 110, 'N2 = 20', 13, 'start', bold=True))
    o.append(wire((xsec, yt), (250, yt))); o.append(diode(250, yt, 300, yt)); o.append(wire((300, yt), (340, yt)))
    o.append(wire((xsec, 150), (xsec, yb), (340, yb)))
    o.append(cap(310, yt, 310, yb)); o.append(dot(310, yt)); o.append(dot(310, yb))
    o.append(T(275, yt - 16, 'D', 14, bold=True, fill=NX))
    o.append(T(344, yt + 4, '16 V', 14, 'start', bold=True, fill=LV))
    o.append(boxt(20, 236, 330, 88, ['V_o = 48 × 0.4/(0.6 × 2) = 16 V', 'switch blocks 48 + 2 × 16 = 80 V', 'plus the leakage spike (RCD clamp)'], PANEL, AC, 13))
    o.append(T(180, 342, 'ON: dots opposite, D blocks, energy goes into the gap', 13, fill=MUT))
    # forward, right panel
    ox = 380
    o.append(T(ox + 165, 24, 'Forward: energy passes while S is on', 14, bold=True))
    xs2, xr_, xp2, xsec2 = ox + 20, ox + 62, ox + 112, ox + 160
    o.append(wire((xs2, yt), (xp2, yt))); o.append(wire((xs2, yb), (xp2, yb)))
    o.append(wire((xs2, yt), (xs2, 121))); o.append(wire((xs2, 157), (xs2, yb))); o.append(vsrc(xs2, 139))
    o.append(T(xs2, 108, 'V_s', 14, bold=True))
    o.append(winding(xp2, yt, 150, right=True)); o.append(wire((xp2, 150), (xp2, 160))); o.append(sw(xp2, 160, xp2, yb))
    o.append(T(xp2 + 12, 196, 'S', 14, 'start', bold=True))
    o.append(dot(xp2 - 12, yt + 14, AC, 4))
    # reset winding with its diode back to the input
    o.append(winding(xr_, 90, 170, right=False, c=NX, humps=3))
    o.append(dot(xr_ + 12, 160, NX, 4))
    o.append(wire((xr_, 90), (xr_, yt))); o.append(dot(xr_, yt))
    o.append(diode(xr_, yb, xr_, 170, NX, 11)); o.append(dot(xr_, yb))
    o.append(T(xr_ + 30, 236, 'reset winding N3 = N1, same core', 13, 'middle', NX, bold=True))
    o.append(L(ox + 136, yt + 6, ox + 136, 150, MUT, 2)); o.append(L(ox + 140, yt + 6, ox + 140, 150, MUT, 2))
    o.append(winding(xsec2, yt, 150, right=False)); o.append(dot(xsec2 + 12, yt + 14, AC, 4))
    o.append(wire((xsec2, yt), (ox + 180, yt))); o.append(diode(ox + 180, yt, ox + 220, yt)); o.append(wire((ox + 220, yt), (ox + 236, yt)))
    o.append(ind(ox + 236, yt, ox + 300, yt)); o.append(wire((ox + 300, yt), (ox + 330, yt)))
    o.append(wire((xsec2, 150), (xsec2, yb), (ox + 330, yb)))
    o.append(diode(ox + 228, yb, ox + 228, yt)); o.append(dot(ox + 228, yt)); o.append(dot(ox + 228, yb))
    o.append(cap(ox + 316, yt, ox + 316, yb)); o.append(dot(ox + 316, yt)); o.append(dot(ox + 316, yb))
    o.append(T(ox + 200, yt - 16, 'D1', 13, bold=True, fill=NX)); o.append(T(ox + 268, yt - 18, 'L_o', 14, bold=True))
    o.append(T(ox + 222, 150, 'D2', 13, 'end', bold=True, fill=NX))
    o.append(boxt(ox + 120, 252, 210, 72, ['V_o = D·V_s·(N2/N1)', 'D < 0.5; S blocks 2V_s'], PANEL, AC, 13))
    o.append(T(ox + 165, 342, 'OFF: N3 returns the core energy to V_s', 13, fill=MUT))
    return 356, ''.join(o)


FIG[6] = (f6, 'Left, the worked example’s flyback: the dots are at opposite ends, so the diode blocks while S is on and the energy waits in the '
              'gapped core; the switch then holds 48 + 2 × 16 = 80 V. Right, the forward converter: the dots match, D1 conducts during the '
              'on-time, and the reset winding returns the core energy to the source.',
          'Left: flyback circuit with a 48 volt source, switch, 40 turn primary and 20 turn secondary on a gapped core with dots at opposite '
          'ends, diode and capacitor at 16 volts; a box gives V o = 16 volts and an 80 volt switch stress. Right: forward circuit with primary, '
          'reset winding and diode back to the source, secondary with D1, freewheeling diode D2, output inductor and capacitor.')


# ---------------------------------------------------------------- 3.7 hard turn-on against ZVS turn-on (200 V, 5 A, 100 ns)
def f7():
    o = []
    for j, title in enumerate(['Hard turn-on: 200 V, 5 A, 100 ns', 'ZVS turn-on: voltage is 0 first']):
        x0 = 60 + j * 350
        fx = lin(0, 200, x0, x0 + 280)
        o.append(T(x0 + 140, 26, title, 14, bold=True))
        # gate lane
        yg = 62
        o.append(T(x0 - 8, yg + 5, 'gate', 13, 'end', MUT))
        g_on = 50 if j == 0 else 140
        o.append(P([(fx(0), yg + 8), (fx(g_on), yg + 8), (fx(g_on), yg - 8), (fx(200), yg - 8)], MUT, 2))
        # voltage lane
        fyv = lin(0, 200, 190, 100)
        o.append(L(fx(0), fyv(0), fx(200), fyv(0), L2, 1.5)); o.append(T(x0 - 8, fyv(200) + 5, '200 V', 13, 'end', MUT)); o.append(T(x0 - 8, fyv(0) + 5, '0', 13, 'end', MUT))
        fyi = lin(-2, 5, 300, 220)
        o.append(L(fx(0), fyi(0), fx(200), fyi(0), L2, 1.5)); o.append(T(x0 - 8, fyi(5) + 5, '5 A', 13, 'end', MUT)); o.append(T(x0 - 8, fyi(0) + 5, '0', 13, 'end', MUT))
        fyp = lin(0, 1000, 420, 330)
        o.append(L(fx(0), fyp(0), fx(200), fyp(0), L2, 1.5)); o.append(T(x0 - 8, fyp(1000) + 5, '1 kW', 13, 'end', MUT)); o.append(T(x0 - 8, fyp(0) + 5, '0', 13, 'end', MUT))
        if j == 0:
            # current rises 50-100 ns at full voltage, then voltage falls 100-150 ns at full current
            o.append(P([(fx(0), fyv(200)), (fx(100), fyv(200)), (fx(150), fyv(0)), (fx(200), fyv(0))], AC, 2.6))
            o.append(P([(fx(0), fyi(0)), (fx(50), fyi(0)), (fx(100), fyi(5)), (fx(200), fyi(5))], LV, 2.6))
            o.append(P([(fx(0), fyp(0)), (fx(50), fyp(0)), (fx(100), fyp(1000)), (fx(150), fyp(0)), (fx(200), fyp(0))], NX, 2.6, fill=NXS))
            o.append(T(fx(100), fyp(1000) - 8, 'v·i peaks at 1000 W', 13, bold=True, fill=NX))
            o.append(T(fx(153), fyp(450), 'E = 50 µJ', 13, 'start', NX, bold=True))
            o.append(brace(fx(50), fx(150), fyi(5) - 10, MUT, up=True)); o.append(T(fx(100), fyi(5) - 16, 'overlap 100 ns', 13, fill=MUT))
        else:
            # resonant current first discharges C_oss: voltage falls 0-80 ns, body diode conducts (negative current) until the gate
            o.append(P([(fx(0), fyv(200))] + [(fx(t), fyv(100 + 100 * math.cos(math.pi * t / 80))) for t in range(0, 81, 5)] + [(fx(200), fyv(0))], AC, 2.6))
            o.append(P([(fx(0), fyi(0)), (fx(20), fyi(-1.5)), (fx(140), fyi(-1.5)), (fx(185), fyi(5)), (fx(200), fyi(5))], LV, 2.6))
            o.append(P([(fx(0), fyp(0)), (fx(200), fyp(0))], NX, 2.6))
            o.append(Tb(fx(70), fyi(-1.5) + 4, 'body diode', 13, fill=LV, bold=True))
            o.append(Tb(fx(100), fyp(500), 'v = 0 while i rises:', 13, fill=NX, bold=True))
            o.append(Tb(fx(100), fyp(500) + 18, 'E ≈ 0, no overlap', 13, fill=NX, bold=True))
            o.append(T(fx(40), fyv(100) - 12, 'C_oss discharged', 13, 'start', fill=MUT))
        o.append(T(x0 - 44, fyv(100) + 5, 'v', 14, 'end', AC, bold=True)); o.append(T(x0 - 44, fyi(2) + 5, 'i', 14, 'end', LV, bold=True))
        o.append(T(x0 - 44, fyp(500) + 5, 'p', 14, 'end', NX, bold=True))
        for t in (0, 100, 200): o.append(T(fx(t), 440, f'{t}', 13, fill=MUT))
    o.append(T(360, 462, 'time (ns). At 100 kHz the 50 µJ of hard turn-on costs 5 W; ZVS saves it.', 13, fill=MUT))
    return 476, ''.join(o)


FIG[7] = (f7, 'Turn-on of the worked example’s MOSFET. Hard-switched, current and voltage overlap for 100 ns and the triangle of v·i holds 50 µJ, '
              'which is 5 W at 100 kHz. With ZVS the resonant current has already brought the voltage to zero, so the gate turns the channel on '
              'with no overlap.',
          'Two panels with gate, voltage, current and power lanes over 200 nanoseconds. Left, hard turn-on: current rises to 5 amps while the '
          'voltage stays at 200 volts, then the voltage falls; the power triangle peaks at 1000 watts and holds 50 microjoules. Right, ZVS: '
          'the voltage falls to zero first, the body diode carries a small negative current, the gate then turns on and the current rises '
          'with zero voltage, so the power stays at zero.')


# ---------------------------------------------------------------- 3.8 the example's gapped E-core inductor
def f8():
    o = []
    o.append(T(200, 26, 'E-core inductor for the buck example', 14, bold=True))
    x0, y0, W, H = 40, 60, 320, 260
    # core outline: outer frame, two windows; centre leg gap
    o.append(R(x0, y0, W, H, ACS, AC, 4))
    o.append(R(x0 + 60, y0 + 50, 70, H - 100, FIGBG, AC, 2))
    o.append(R(x0 + W - 130, y0 + 50, 70, H - 100, FIGBG, AC, 2))
    gy = y0 + H / 2
    o.append(R(x0 + 130, gy - 7, 60, 14, FIGBG, NX, 1, 2))
    o.append(T(x0 + 160, gy + 34, 'gap', 13, fill=NX, bold=True))
    # windings in the windows
    for wx in (x0 + 66, x0 + W - 124):
        for r_ in range(8):
            for c_ in range(2):
                o.append(f'<circle cx="{wx + 14 + c_ * 30:.1f}" cy="{y0 + 66 + r_ * 18.5:.1f}" r="7" style="fill:var(--next-soft);stroke:var(--next);stroke-width:1.5"/>')
    o.append(T(x0 + 160, y0 + H + 22, 'N = 16 turns in both windows', 13, bold=True, fill=NX))
    # flux loops
    o.append(f'<path d="M{x0 + 160},{y0 + 40} L{x0 + 160},{y0 + 20} L{x0 + 30},{y0 + 20} L{x0 + 30},{y0 + H - 20} L{x0 + 160},{y0 + H - 20} L{x0 + 160},{y0 + H - 44}" '
             f'style="fill:none;stroke:var(--live);stroke-width:2;stroke-dasharray:6 4" marker-end="url(#ar-UID-l)"/>')
    o.append(T(x0 + 160, y0 - 8, 'centre leg: A_e = 1.0 cm²', 13, bold=True))
    o.append(Tb(x0 + 95, y0 + 25, 'flux path', 13, fill=LV, bold=True))
    # calculation panel
    bx = 400
    lines = ['L = 100 µH, I_o = 4 A, ΔI_L = 1.2 A',
             'I_pk = 4 + 0.6 = 4.6 A',
             'N = L·I_pk/(B_max·A_e) = 15.3 → 16',
             'B = 4.6 × 10⁻⁴/(16 × 10⁻⁴) = 0.29 T',
             'gap ℓ_g = µ₀N²A_e/L = 0.32 mm',
             'A_cu = 4 A ÷ 4 A/mm² = 1.0 mm²',
             '8 strands of 0.40 mm (skin 0.21 mm)']
    o.append(R(bx, 60, 300, 236, PANEL, AC, 10))
    for i, s in enumerate(lines):
        o.append(T(bx + 14, 92 + i * 30, s, 13, 'start', INK, bold=(i in (2, 4))))
    o.append(T(bx + 150, 322, 'the gap, not the ferrite, sets L and I_sat', 13, fill=MUT))
    return 350, ''.join(o)


FIG[8] = (f8, 'The worked example’s inductor: 16 turns on the centre leg of an E core with a 0.32 mm gap carry the 4.6 A peak at 0.29 T, just '
              'under the 0.3 T ferrite limit. The winding is split into thin strands because the skin depth at 100 kHz is only 0.21 mm.',
          'Cross-section of an E core: two windows filled with 16 turns of wire around the centre leg, a gap in the centre leg, and a dashed '
          'flux path round the outer leg. A panel lists the design steps: peak current 4.6 amps, 16 turns, 0.29 tesla, a 0.32 millimetre gap, '
          '1.0 square millimetre of copper as eight strands of 0.40 millimetre.')

spec = make_spec(FIG)


def text_fixes(k):
    return []
