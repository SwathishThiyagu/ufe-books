"""Claude's hand-drawn figures for ec-circuits-u1 (Circuit Theory: circuit elements and laws), one per chapter, drawn
from each chapter's own worked example and numbers. Colours are the shell's CSS variables only.

The bridge circuit of chapters 4, 6 and 8 is one circuit: A top, B left, C right, D bottom; branches
1 = A-B 20 ohm, 2 = A-C 20 ohm, 3 = B-C 10 ohm, 4 = B-D 2 ohm, 5 = C-D 8 ohm, 6 = the 36 V source from D up to A."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
OHM = 'Ω'


# ---------------------------------------------------------------- circuit symbols
def _frame(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    pt = lambda s, t: (x1 + ux * s - uy * t, y1 + uy * s + ux * t)
    return n, pt


def wire(*pts, c=INK, w=2):
    return P(list(pts), c, w)


def res(x1, y1, x2, y2, c=AC, body=48):
    """resistor (zigzag) between two terminals, leads drawn"""
    n, pt = _frame(x1, y1, x2, y2)
    a = (n - body) / 2
    zz = [pt(0, 0), pt(a, 0)]
    for i in range(6):
        zz.append(pt(a + (2 * i + 1) * body / 12, -8 if i % 2 == 0 else 8))
    zz += [pt(a + body, 0), pt(n, 0)]
    return P(zz, c, 2.2)


def ind(x1, y1, x2, y2, c=AC, body=52):
    """inductor (four humps) between two terminals"""
    n, pt = _frame(x1, y1, x2, y2)
    a = (n - body) / 2
    w = body / 4
    d = f'M{pt(0, 0)[0]:.1f},{pt(0, 0)[1]:.1f} L{pt(a, 0)[0]:.1f},{pt(a, 0)[1]:.1f}'
    for i in range(4):
        e = pt(a + (i + 1) * w, 0)
        d += f' A{w / 2:.1f},{w / 2:.1f} 0 0 1 {e[0]:.1f},{e[1]:.1f}'
    e = pt(n, 0)
    d += f' L{e[0]:.1f},{e[1]:.1f}'
    return f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:2.2"/>'


def cap(x1, y1, x2, y2, c=AC, gap=10, plate=32):
    n, pt = _frame(x1, y1, x2, y2)
    m = n / 2
    o = [L(*pt(0, 0), *pt(m - gap / 2, 0), INK, 2), L(*pt(m + gap / 2, 0), *pt(n, 0), INK, 2)]
    o += [L(*pt(m - gap / 2, -plate / 2), *pt(m - gap / 2, plate / 2), c, 3), L(*pt(m + gap / 2, -plate / 2), *pt(m + gap / 2, plate / 2), c, 3)]
    return ''.join(o)


def vsrc(cx, cy, r=20, plus='up', c=LV, label=None, lab_side='left'):
    """independent voltage source, + on the side named by plus"""
    o = [f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2.4"/>']
    dx, dy = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}[plus]
    o.append(T(cx + dx * r * 0.45, cy + dy * r * 0.45 + 5, '+', 15, bold=True, fill=c))
    o.append(T(cx - dx * r * 0.45, cy - dy * r * 0.45 + 5, '−', 15, bold=True, fill=c))
    if label:
        if lab_side == 'left': o.append(T(cx - r - 8, cy + 5, label, 14, 'end', bold=True))
        else: o.append(T(cx + r + 8, cy + 5, label, 14, 'start', bold=True))
    return ''.join(o)


def isrc(cx, cy, r=20, to='up', c=LV, label=None, lab_side='left'):
    """independent current source, arrow pointing to the side named by to"""
    o = [f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2.4"/>']
    dx, dy = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}[to]
    o.append(L(cx - dx * r * 0.6, cy - dy * r * 0.6, cx + dx * r * 0.55, cy + dy * r * 0.55, c, 2.4, arrow='l'))
    if label:
        if lab_side == 'left': o.append(T(cx - r - 8, cy + 5, label, 14, 'end', bold=True))
        else: o.append(T(cx + r + 8, cy + 5, label, 14, 'start', bold=True))
    return ''.join(o)


def diamond(cx, cy, r=22, kind='v', c=NX):
    """dependent source: kind 'v' carries + and -, kind 'i' an arrow (both pointing up)"""
    pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r)]
    o = [P(pts, c, 2.4, fill='var(--fig)')]
    if kind == 'v':
        o.append(T(cx, cy - 4, '+', 15, bold=True, fill=c)); o.append(T(cx, cy + 15, '−', 15, bold=True, fill=c))
    else:
        o.append(L(cx, cy + r * 0.55, cx, cy - r * 0.5, c, 2.4, arrow='x'))
    return ''.join(o)


def dot(x, y, c=INK, r=4.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c}"/>'


def iarrow(x, y, d, c=AC, size=8):
    """a filled arrowhead on a wire at (x, y) pointing in direction d"""
    dx, dy = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}[d]
    tip = (x + dx * size, y + dy * size)
    b1 = (x - dx * size - dy * size * 0.8, y - dy * size + dx * size * 0.8)
    b2 = (x - dx * size + dy * size * 0.8, y - dy * size - dx * size * 0.8)
    return f'<polygon points="{tip[0]:.1f},{tip[1]:.1f} {b1[0]:.1f},{b1[1]:.1f} {b2[0]:.1f},{b2[1]:.1f}" style="fill:{c}"/>'


def node(x, y, name, dx=0, dy=-12, anchor='middle'):
    return dot(x, y) + T(x + dx, y + dy, name, 15, anchor, bold=True)


def loopmark(cx, cy, r, label, c=MUT):
    """clockwise loop arrow with a label in the middle"""
    a0, a1 = math.radians(-150), math.radians(150)
    x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    p = f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 1 1 {x1:.1f},{y1:.1f}" style="fill:none;stroke:{c};stroke-width:1.8" marker-end="url(#ar-UID-m)"/>'
    return p + T(cx, cy + 5, label, 14, fill=c, bold=True)


# ---------------------------------------------------------------- 1.1 the three element laws with the example's numbers
def f1():
    o = []
    o.append(T(360, 26, 'Passive sign convention: the current arrow enters the + terminal', 14, bold=True))
    panels = [
        ('Resistor', res, 'R = 12 Ω', ['i = 2 A', 'v = iR = 2 × 12', '= 24 V', 'p = i²R = 48 W, all heat'], AC),
        ('Inductor', ind, 'L = 0.5 H', ['i = 2 A, di/dt = 40 A/s', 'v = L di/dt = 0.5 × 40', '= 20 V', 'stores ½Li² = 1 J'], AC),
        ('Capacitor', cap, 'C = 100 μF', ['v = 10 V, dv/dt = 200 V/s', 'i = C dv/dt = 10⁻⁴ × 200', '= 0.02 A = 20 mA', 'stores ½Cv² = 5 mJ'], AC),
    ]
    for j, (name, fn, val, lines, col) in enumerate(panels):
        x0 = 20 + j * 233
        o.append(R(x0, 44, 214, 268, PANEL, L2, 10, 1.5))
        o.append(T(x0 + 107, 70, name, 15, bold=True))
        y = 128
        o.append(wire((x0 + 22, y), (x0 + 50, y)))
        o.append(fn(x0 + 50, y, x0 + 164, y))
        o.append(wire((x0 + 164, y), (x0 + 192, y)))
        o.append(dot(x0 + 22, y)); o.append(dot(x0 + 192, y))
        o.append(T(x0 + 30, y - 22, '+', 16, bold=True, fill=LV)); o.append(T(x0 + 184, y - 22, '−', 16, bold=True, fill=LV))
        o.append(T(x0 + 107, y - 24, 'v', 15, bold=True, fill=LV, italic=True))
        o.append(iarrow(x0 + 38, y, 'right', NX))
        o.append(T(x0 + 34, y + 24, 'i', 15, bold=True, fill=NX, italic=True))
        o.append(T(x0 + 120, y + 34, val, 14, bold=True))
        for i, s in enumerate(lines):
            o.append(T(x0 + 107, 200 + i * 24, s, 13 if i != 2 else 14, fill=INK if i != 3 else MUT, bold=(i == 2)))
    return 330, ''.join(o)


FIG[1] = (f1, 'The worked example on the three elements. Each law ties v to i in its own way: the resistor to the present '
              'current, the inductor to the rate of change of current, the capacitor to the rate of change of voltage.',
          'Three panels: a 12 ohm resistor with 2 A gives 24 V; a 0.5 H inductor with current rising at 40 A per second gives 20 V; '
          'a 100 microfarad capacitor with voltage rising at 200 V per second takes 20 mA. Energy stored: 1 J and 5 mJ.')


# ---------------------------------------------------------------- 1.2 symbols, then the V-I lines of an ideal and a practical source
def f2():
    o = []
    o.append(T(20, 28, 'Symbols', 15, 'start', bold=True))
    sy = 82
    items = [('ideal voltage', 'source', lambda x: vsrc(x, sy, 22, 'up', LV)),
             ('ideal current', 'source', lambda x: isrc(x, sy, 22, 'up', LV)),
             ('dependent voltage', 'source: μvₓ or r iₓ', lambda x: diamond(x, sy, 24, 'v', NX)),
             ('dependent current', 'source: g vₓ or β iₓ', lambda x: diamond(x, sy, 24, 'i', NX))]
    for i, (a, b, fn) in enumerate(items):
        x = 95 + i * 177
        o.append(L(x, sy - 40, x, sy + 40, INK, 2))
        o.append(fn(x))
        o.append(T(x, sy + 62, a, 13)); o.append(T(x, sy + 80, b, 13, fill=MUT))
    # plot: terminal voltage against load current, 12 V, Rs = 0.5 ohm
    x0, x1, y0, y1 = 110, 520, 220, 450
    fx = lambda i: x0 + i / 8 * (x1 - x0)
    fy = lambda v: y1 - v / 14 * (y1 - y0)
    o.append(T(20, 202, 'Terminal voltage against load current (12 V battery)', 15, 'start', bold=True))
    o.append(axes(x0, x1, y0 + 14, y1, [0, 2, 4, 6, 8], [0, 4, 8, 12], fx, fy, 'load current i (A)', 'terminal voltage v (V)'))
    o.append(L(fx(0), fy(12), fx(8), fy(12), LV, 2.5, '7 5'))
    o.append(T(fx(8) + 6, fy(12) + 5, 'ideal: v = 12 V', 13, 'start', LV, bold=True))
    o.append(L(fx(0), fy(12), fx(8), fy(8), AC, 2.8))
    o.append(T(fx(8) + 6, fy(8) + 5, 'practical:', 13, 'start', AC, bold=True))
    o.append(T(fx(8) + 6, fy(8) + 23, 'v = 12 − 0.5i', 13, 'start', AC, bold=True))
    for i_, v_, dy in ((1, 11.5, 28), (2, 11, 52), (6, 9, 28)):
        o.append(C(fx(i_), fy(v_), 6, NX))
        o.append(Tb(fx(i_) + (14 if i_ == 2 else 0), fy(v_) + dy, f'{i_} A, {v_:g} V', 13, 'middle', NX, True))
    o.append(T(x0 + 10, y1 + 62, 'The practical line falls 0.5 V for every ampere and would reach 0 V at i = 12/0.5 = 24 A (short circuit).', 13, 'start', MUT))
    return 530, ''.join(o)


FIG[2] = (f2, 'Top: the four source symbols; a circle is independent, a diamond is dependent. Bottom: an ideal source keeps 12 V '
              'at any current, while the practical battery of the second worked example (12 V with 0.5 Ω inside) sags along v = 12 − 0.5i; '
              'the dots are its three loads.',
          'Four symbols: circle with plus and minus, circle with an arrow, diamond with plus and minus, diamond with an arrow. '
          'Below, a graph of terminal voltage against current: a flat dashed line at 12 V and a falling line from 12 V to 8 V at 8 A, '
          'with points at 1 A 11.5 V, 2 A 11 V and 6 A 9 V.')


# ---------------------------------------------------------------- 1.3 a 12 V supply charging a 4 V cell and feeding a load
def f3():
    o = []
    yt, yb = 70, 250
    xl, xa, xr = 90, 360, 630
    # left source and R1
    o.append(wire((xl, yt), (xl, 135))); o.append(vsrc(xl, 160, 24, 'up', LV, '12 V'))
    o.append(wire((xl, 185), (xl, yb)))
    o.append(wire((xl, yt), (150, yt))); o.append(res(150, yt, 280, yt)); o.append(wire((280, yt), (xa, yt)))
    o.append(T(215, yt - 18, 'R₁ = 2 Ω', 14, bold=True))
    # middle R3
    o.append(res(xa, yt, xa, yb)); o.append(T(xa + 18, 165, 'R₃ = 8 Ω', 14, 'start', bold=True))
    # right R2 and source
    o.append(wire((xa, yt), (440, yt))); o.append(res(440, yt, 570, yt)); o.append(wire((570, yt), (xr, yt)))
    o.append(T(505, yt - 18, 'R₂ = 4 Ω', 14, bold=True))
    o.append(wire((xr, yt), (xr, 135))); o.append(vsrc(xr, 160, 24, 'up', LV, '4 V', 'right'))
    o.append(wire((xr, 185), (xr, yb)))
    o.append(wire((xl, yb), (xr, yb)))
    o.append(node(xa, yt, 'A', 0, -14)); o.append(node(xa, yb, 'B (0 V)', 0, 24))
    # currents
    o.append(iarrow(125, yt, 'right', NX)); o.append(T(125, yt + 26, 'I₁ = 2 A', 14, fill=NX, bold=True))
    o.append(iarrow(xa, 215, 'down', NX)); o.append(T(xa - 14, 222, 'I₃ = 1 A', 14, 'end', NX, bold=True))
    o.append(iarrow(600, yt, 'left', NX)); o.append(T(612, yt + 26, 'I₂ = −1 A', 14, 'end', NX, True))
    o.append(loopmark(225, 165, 34, 'loop 1')); o.append(loopmark(495, 165, 34, 'loop 2'))
    o.append(Tb(xa, 30, 'V_A = 8 V', 14, 'middle', AC, True).replace('V_A', 'V<tspan font-size="11" dy="3">A</tspan><tspan dy="-3"></tspan>'))
    o.append(T(360, 300, 'KCL at A: I₁ + I₂ = I₃, so 2 + (−1) = 1. I₂ came out negative: 1 A really flows right, into the + of the 4 V cell.', 13, fill=MUT))
    o.append(T(360, 322, 'Power: 12 V source gives 24 W = 8 W (R₁) + 4 W (R₂) + 8 W (R₃) + 4 W taken by the 4 V cell.', 13, fill=MUT))
    return 338, ''.join(o)


FIG[3] = (f3, 'The first worked example: a 12 V supply charges a 4 V cell and feeds an 8 Ω load. One KCL equation at node A and one KVL '
              'equation round each window give I₁ = 2 A, I₂ = −1 A and I₃ = 1 A, and the powers balance.',
          'Circuit: 12 V source on the left, 2 ohm resistor to node A, 8 ohm resistor from A down to the bottom wire, 4 ohm resistor '
          'from A to a 4 V source on the right. Currents: 2 A right through the 2 ohm, 1 A down through the 8 ohm, minus 1 A from the 4 V source toward A.')


# ---------------------------------------------------------------- the bridge circuit, shared by 1.4, 1.6 and 1.8
def bridge(ox=0, oy=0, s=1.0, delta_col=AC, labels=True, nums=True, src_right=False):
    A, B, Cn, D = (ox + 300 * s, oy + 60 * s), (ox + 180 * s, oy + 180 * s), (ox + 420 * s, oy + 180 * s), (ox + 300 * s, oy + 300 * s)
    o = []
    o.append(res(*A, *B, delta_col)); o.append(res(*A, *Cn, delta_col)); o.append(res(*B, *Cn, delta_col))
    o.append(res(*B, *D)); o.append(res(*Cn, *D))
    xs = ox + 70 * s
    o.append(wire(A, (A[0], oy + 30 * s), (xs, oy + 30 * s), (xs, oy + 155 * s)))
    o.append(vsrc(xs, oy + 180 * s, 24, 'up', LV))
    o.append(wire((xs, oy + 205 * s), (xs, oy + 330 * s), (D[0], oy + 330 * s), D))
    if labels:
        o.append(node(*A, 'A', 16, -6, 'start')); o.append(node(*B, 'B', -12, 5, 'end'))
        o.append(node(*Cn, 'C', 12, 5, 'start')); o.append(node(*D, 'D', 16, 14, 'start'))
    if nums:
        o.append(T(xs + 30, oy + 185 * s, '36 V', 14, 'start', bold=True) if src_right else T(xs - 30, oy + 185 * s, '36 V', 14, 'end', bold=True))
        o.append(T(ox + 222 * s, oy + 108 * s, '20 Ω', 14, 'end', bold=True))
        o.append(T(ox + 378 * s, oy + 108 * s, '20 Ω', 14, 'start', bold=True))
        o.append(T(ox + 300 * s, oy + 180 * s - 14, '10 Ω', 14, bold=True))
        o.append(T(ox + 222 * s, oy + 262 * s, '2 Ω', 14, 'end', bold=True))
        o.append(T(ox + 378 * s, oy + 262 * s, '8 Ω', 14, 'start', bold=True))
    return ''.join(o), (A, B, Cn, D, xs)


def f4():
    body, (A, B, Cn, D, xs) = bridge(40, 10)
    o = [body]
    tag = lambda x, y, n: f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:1.5"/>' + T(x, y + 5, n, 13, bold=True)
    o += [tag(298, 148, '1'), tag(382, 148, '2'), tag(340, 213, '3'), tag(298, 232, '4'), tag(382, 232, '5'), tag(xs + 30, 222, '6')]
    o.append(loopmark(192, 104, 24, 'M1', AC)); o.append(loopmark(340, 138, 20, 'M2', AC)); o.append(loopmark(340, 250, 22, 'M3', AC))
    xt = 520
    lines = [('n = 4 nodes: A, B, C, D', True), ('every node meets 3 branches,', False), ('so all four are junctions', False),
             ('b = 6 branches (numbered)', True), ('tree: n − 1 = 3 branches', False), ('chords: b − n + 1 = 3', False),
             ('meshes M1, M2, M3: m = 3', True), ('loops: 7 (every closed path)', False), ('KCL equations: n − 1 = 3', True)]
    for i, (s_, b_) in enumerate(lines):
        o.append(T(xt, 50 + i * 30, s_, 14 if b_ else 13, 'start', INK if b_ else MUT, b_))
    return 355, ''.join(o)


FIG[4] = (f4, 'The bridge circuit of the worked example, with its six branches numbered and its three meshes M1, M2 and M3 marked '
              '(the window panes of the drawing). The same circuit returns in the star-delta and network-topology chapters.',
          'A bridge circuit: node A at the top, B on the left, C on the right, D at the bottom. Resistors 20 ohm A to B, 20 ohm A to C, '
          '10 ohm B to C, 2 ohm B to D, 8 ohm C to D, and a 36 V source on the left from D up to A. Three meshes are marked. '
          'Counts beside it: 4 nodes, 6 branches, 3 meshes, 7 loops, 3 KCL equations.')


# ---------------------------------------------------------------- 1.5 series-parallel reduction with numbers
def f5():
    o = []
    yt, yb = 70, 250
    o.append(wire((70, yt), (70, 135))); o.append(vsrc(70, 160, 24, 'up', LV, '12 V'))
    o.append(wire((70, 185), (70, yb)))
    o.append(wire((70, yt), (110, yt))); o.append(res(110, yt, 230, yt)); o.append(wire((230, yt), (390, yt)))
    o.append(T(170, yt - 30, 'R₁ = 6 Ω', 14, bold=True))
    o.append(T(170, yt + 32, '7.2 V', 14, fill=LV, bold=True))
    o.append(iarrow(92, yt, 'right', NX)); o.append(T(96, yt - 14, '1.2 A', 13, fill=NX, bold=True))
    for x, r_, i_ in ((300, '12 Ω', '0.4 A'), (390, '6 Ω', '0.8 A')):
        o.append(res(x, yt, x, yb)); o.append(T(x + 16, 150, r_, 14, 'start', bold=True))
        o.append(iarrow(x, 220, 'down', NX)); o.append(T(x + 16, 226, i_, 13, 'start', NX, bold=True))
    o.append(wire((70, yb), (390, yb)))
    o.append(dot(300, yt)); o.append(dot(300, yb))
    o.append(T(286, 182, '4.8 V', 14, 'end', LV, bold=True))
    # reduction steps
    bx = 470
    steps = [('12 Ω ∥ 6 Ω', '= 72/18 = 4 Ω'), ('6 Ω + 4 Ω', '= 10 Ω'), ('I = 12 V / 10 Ω', '= 1.2 A'), ('V = 1.2 A × 4 Ω', '= 4.8 V')]
    for i, (a, b) in enumerate(steps):
        y = 40 + i * 62
        o.append(boxt(bx, y, 220, 46, [a, b], ACS if i == 0 else PANEL, AC, 14))
        if i: o.append(L(bx + 110, y - 16, bx + 110, y - 2, MUT, 1.8, arrow='m'))
    o.append(T(360, 300, 'Checks: 7.2 V + 4.8 V = 12 V (KVL) and 0.4 A + 0.8 A = 1.2 A (KCL).', 13, fill=MUT))
    return 320, ''.join(o)


FIG[5] = (f5, 'The first worked example: the 12 Ω and 6 Ω branches share one voltage, so they combine to 4 Ω; that 4 Ω is in series with R₁, '
              'giving 10 Ω and 1.2 A. The pair’s 4.8 V then splits the current 0.4 A and 0.8 A, the smaller resistor taking more.',
          'Circuit: 12 V source, 6 ohm series resistor, then 12 ohm and 6 ohm resistors in parallel. Labels show 1.2 A, 7.2 V, 4.8 V, '
          '0.4 A and 0.8 A. Four boxes on the right: 12 parallel 6 is 4 ohm; 6 plus 4 is 10 ohm; 1.2 A; 4.8 V.')


# ---------------------------------------------------------------- 1.6 the bridge before and after delta-to-star
def f6():
    o = []
    body, _ = bridge(0, 30, 0.82, AC, src_right=True)
    o.append(body)
    o.append(T(180, 22, 'Before: delta A-B-C has no series or parallel pair', 13, bold=True))
    # after: star N with 8, 4, 4
    ox = 400
    A, N, B, Cn, D = (ox + 190, 80), (ox + 190, 150), (ox + 110, 220), (ox + 270, 220), (ox + 190, 318)
    o.append(res(*A, *N)); o.append(res(*N, *B)); o.append(res(*N, *Cn))
    o.append(res(*B, B[0], 268)); o.append(wire((B[0], 268), (B[0], 300), (D[0], 300), D))
    o.append(res(*Cn, Cn[0], 268)); o.append(wire((Cn[0], 268), (Cn[0], 300), (D[0], 300)))
    xs = ox + 40
    o.append(wire(A, (A[0], 58), (xs, 58), (xs, 165))); o.append(vsrc(xs, 190, 24, 'up', LV))  # source of the reduced circuit
    o.append(wire((xs, 215), (xs, 340), (D[0], 340), D))
    o.append(T(xs - 28, 195, '36 V', 14, 'end', bold=True))
    o += [node(*A, 'A', 14, -4, 'start'), node(*N, 'N', 16, 5, 'start'), node(*B, 'B', -12, 5, 'end'), node(*Cn, 'C', 12, 5, 'start'), node(*D, 'D', 14, 16, 'start')]
    o.append(T(A[0] - 14, 120, '8 Ω', 14, 'end', AC, True))
    o.append(T(ox + 130, 178, '4 Ω', 14, 'end', AC, True)); o.append(T(ox + 252, 178, '4 Ω', 14, 'start', AC, True))
    o.append(T(B[0] - 14, 250, '2 Ω', 14, 'end', bold=True)); o.append(T(Cn[0] - 14, 250, '8 Ω', 14, 'end', bold=True))
    o.append(T(ox + 160, 22, 'After: star N, then series and parallel', 13, bold=True))
    o.append(T(360, 376, 'N–B–D: 4 + 2 = 6 Ω;  N–C–D: 4 + 8 = 12 Ω;  6 ∥ 12 = 4 Ω;  R_eq = 8 + 4 = 12 Ω;  I = 36/12 = 3 A'.replace('R_eq', 'R<tspan font-size="11" dy="3">eq</tspan><tspan dy="-3"></tspan>'), 13, fill=INK, bold=True))
    o.append(T(360, 398, 'Delta to star: R_A = 20 × 20/50 = 8 Ω, R_B = 20 × 10/50 = 4 Ω, R_C = 10 × 20/50 = 4 Ω', 13, fill=MUT)
             .replace('R_A', 'R<tspan font-size="11" dy="3">A</tspan><tspan dy="-3"></tspan>')
             .replace('R_B', 'R<tspan font-size="11" dy="3">B</tspan><tspan dy="-3"></tspan>')
             .replace('R_C', 'R<tspan font-size="11" dy="3">C</tspan><tspan dy="-3"></tspan>'))
    return 412, ''.join(o)


FIG[6] = (f6, 'The second worked example. Left: the delta A-B-C (20 Ω, 10 Ω, 20 Ω) blocks series-parallel reduction. Right: the same '
              'three terminals with the equivalent star 8 Ω, 4 Ω, 4 Ω; now the circuit reduces to 12 Ω and the source gives 3 A.',
          'Left: bridge with a 36 V source, delta of 20, 10 and 20 ohm between A, B and C, and 2 ohm and 8 ohm to D. Right: star with '
          'centre N, 8 ohm to A, 4 ohm to B and 4 ohm to C, then 2 ohm and 8 ohm to D. The result line reads 12 ohm and 3 A.')


# ---------------------------------------------------------------- 1.7 two practical sources merged by source transformation
def f7():
    o = []
    o.append(T(20, 24, '(a) Two practical sources share one load', 14, 'start', bold=True))
    yt, yb = 60, 200
    # source 1
    for xs, v, r_, lab in ((60, '12 V', '3 Ω', 'left'), (250, '18 V', '6 Ω', 'right')):
        o.append(wire((xs, yb), (xs, 160))); o.append(vsrc(xs, 136, 22, 'up', LV, v, lab))
        o.append(res(xs, 114, xs, yt)); o.append(T(xs + (16 if lab == 'left' else -16), 92, r_, 14, 'start' if lab == 'left' else 'end', bold=True))
    o.append(wire((60, yt), (360, yt))); o.append(wire((60, yb), (360, yb)))
    o.append(res(360, yt, 360, yb)); o.append(T(376, 135, '2 Ω load', 14, 'start', bold=True))
    o.append(dot(250, yt)); o.append(dot(250, yb))
    # arrow to (b)
    o.append(L(468, 100, 520, 100, MUT, 2, arrow='m'))
    o.append(T(494, 84, 'I = V/R', 13, fill=MUT))
    # (b) one current source
    o.append(T(540, 24, '(b) 4 A + 3 A, 3 ∥ 6 Ω', 14, 'start', bold=True))
    o.append(wire((560, yt), (690, yt))); o.append(wire((560, yb), (690, yb)))
    o.append(isrc(560, 130, 22, 'up', LV)); o.append(wire((560, yt), (560, 108))); o.append(wire((560, 152), (560, yb)))
    o.append(T(530, 136, '7 A', 14, 'end', LV, True))
    o.append(res(625, yt, 625, yb)); o.append(T(637, 140, '2 Ω', 14, 'start', bold=True))
    o.append(res(690, yt, 690, yb)); o.append(T(690, 230, 'load', 13, fill=MUT))
    o.append(dot(625, yt)); o.append(dot(625, yb))
    # (c) back to a voltage source
    o.append(T(20, 290, '(c) Back to the voltage form: 7 A × 2 Ω = 14 V in series with 2 Ω', 14, 'start', bold=True))
    y2t, y2b = 320, 440
    o.append(wire((80, y2b), (80, 405))); o.append(vsrc(80, 380, 22, 'up', LV, '14 V'))
    o.append(wire((80, 358), (80, y2t), (120, y2t))); o.append(res(120, y2t, 240, y2t)); o.append(T(180, y2t - 16, '2 Ω', 14, bold=True))
    o.append(wire((240, y2t), (300, y2t))); o.append(res(300, y2t, 300, y2b)); o.append(T(316, 385, '2 Ω load', 14, 'start', bold=True))
    o.append(wire((80, y2b), (300, y2b)))
    o.append(iarrow(270, y2t, 'right', NX)); o.append(T(270, y2t - 14, '3.5 A', 13, fill=NX, bold=True))
    o.append(T(420, 350, 'I = 14 / (2 + 2) = 3.5 A', 14, 'start', AC, True))
    o.append(T(420, 376, 'V = 3.5 × 2 = 7 V', 14, 'start', AC, True))
    o.append(T(420, 404, 'check in (a): (12 − 7)/3 + (18 − 7)/6', 13, 'start', MUT))
    o.append(T(420, 424, '= 1.667 + 1.833 = 3.5 A', 13, 'start', MUT))
    return 460, ''.join(o)


FIG[7] = (f7, 'The second worked example in three steps: each practical voltage source becomes a current source (12/3 = 4 A, 18/6 = 3 A), '
              'the two current sources and the two resistors merge, and the result goes back to a 14 V source with 2 Ω in series.',
          'Panel a: a 12 V source with 3 ohm and an 18 V source with 6 ohm in parallel across a 2 ohm load. Panel b: one 7 A current source, '
          '2 ohm and the load in parallel. Panel c: a 14 V source with 2 ohm in series and the 2 ohm load, carrying 3.5 A at 7 V.')


# ---------------------------------------------------------------- 1.8 oriented graph of the bridge, tree and chords
def f8():
    o = []
    A, B, Cn, D = (270, 60), (130, 190), (410, 190), (270, 320)
    def br(p, q, n, tree, lab_dx, lab_dy, bend=0.0):
        col = AC if tree else NX
        w = 3.2 if tree else 2.2
        dash = None if tree else '7 5'
        o.append(edge(p, q, 15, bend, col, w, 'n' if tree else 'x', dash))
        mx, my = (p[0] + q[0]) / 2 + lab_dx, (p[1] + q[1]) / 2 + lab_dy
        o.append(T(mx, my, n, 15, fill=col, bold=True))
    br(A, B, '1', False, -14, -8)
    br(A, Cn, '2', False, 14, -8)
    br(Cn, B, '3', False, 0, -10)
    br(B, D, '4', True, -14, 16)
    br(Cn, D, '5', True, 14, 16)
    o.append(edge(D, A, 15, 1.615, AC, 3.2, 'n'))
    o.append(T(40, 196, '6', 15, fill=AC, bold=True))
    for (x, y), nm in ((A, 'A'), (B, 'B'), (Cn, 'C'), (D, 'D')):
        o.append(f'<circle cx="{x}" cy="{y}" r="14" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>' + T(x, y + 5, nm, 14, bold=True))
    xt = 478
    o.append(L(xt, 46, xt + 40, 46, AC, 3.2)); o.append(T(xt + 50, 51, 'tree: 4, 5, 6', 14, 'start', AC, True))
    o.append(L(xt, 74, xt + 40, 74, NX, 2.2, '7 5')); o.append(T(xt + 50, 79, 'chords: 1, 2, 3', 14, 'start', NX, True))
    rows = [('tie-set 1: chord 1 + 4, 6', 'loop A-B-D-A'), ('tie-set 2: chord 2 + 5, 6', 'loop A-C-D-A'), ('tie-set 3: chord 3 + 4, −5', 'loop C-B-D-C'),
            ('cut-set 4: 4, −1, −3', 'isolates B'), ('cut-set 5: 5, −2, 3', 'isolates C'), ('cut-set 6: 6, −1, −2', 'isolates A')]
    for i, (a, b) in enumerate(rows):
        y = 118 + i * 36 + (14 if i >= 3 else 0)
        o.append(T(xt, y, a, 13, 'start', INK, True)); o.append(T(xt + 12, y + 16, b, 13, 'start', MUT))
    o.append(T(360, 372, 'Branch arrows give the positive current directions; branch 6 is the 36 V source, from D to A.', 13, fill=MUT))
    return 388, ''.join(o)


FIG[8] = (f8, 'The oriented graph of the bridge circuit: four nodes, six branches. The chosen tree (solid) joins every node to D with no loop; '
              'each dashed chord closes one fundamental loop (tie-set), and cutting each tree branch isolates one node (cut-set).',
          'A graph with nodes A top, B left, C right, D bottom. Solid tree branches: 4 from B to D, 5 from C to D, 6 from D to A on the left. '
          'Dashed chords with arrows: 1 from A to B, 2 from A to C, 3 from C to B. A list gives the three tie-sets and the three cut-sets.')


spec = make_spec(FIG)
