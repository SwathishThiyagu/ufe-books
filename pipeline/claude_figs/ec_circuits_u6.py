"""Claude's hand-drawn figures for ec-circuits-u6 (Circuit Theory: two-port networks and network synthesis), one per
chapter, each drawn from that chapter's own worked example and numbers. One T network (2 Ω, 3 Ω, 4 Ω) runs through the
unit, so the same circuit appears with its Z, Y, h and ABCD numbers. Both port currents are drawn entering the network."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
W = 2.2  # wire width


# ---------------- circuit pieces ----------------
def wire(*pts, c=INK, w=W):
    return P(list(pts), c, w)


def term(x, y, lab=None, dx=0, dy=-12, anchor='middle'):
    o = f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" style="fill:var(--fig);stroke:var(--ink);stroke-width:2"/>'
    if lab: o += T(x + dx, y + dy, lab, 14, anchor, MUT)
    return o


def dot(x, y):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.8" style="fill:var(--ink)"/>'


def _seg(x1, y1, x2, y2, ln):
    """lead-in and lead-out points around a centred element of length ln on a horizontal or vertical run"""
    if abs(y1 - y2) < 1e-6:
        m = (x1 + x2) / 2; s = 1 if x2 > x1 else -1
        return (m - s * ln / 2, y1), (m + s * ln / 2, y1), 'h'
    m = (y1 + y2) / 2; s = 1 if y2 > y1 else -1
    return (x1, m - s * ln / 2), (x1, m + s * ln / 2), 'v'


def res(x1, y1, x2, y2, c=AC, ln=44, amp=7):
    a, b, o = _seg(x1, y1, x2, y2, ln)
    pts = [(x1, y1), a]
    n = 6
    for i in range(1, n + 1):
        t = (i - 0.5) / n
        s = amp if i % 2 else -amp
        if o == 'h': pts.append((a[0] + (b[0] - a[0]) * t, y1 + s))
        else: pts.append((x1 + s, a[1] + (b[1] - a[1]) * t))
    pts += [b, (x2, y2)]
    return P(pts, c, W)


def ind(x1, y1, x2, y2, c=AC, ln=48, n=4):
    a, b, o = _seg(x1, y1, x2, y2, ln)
    r = ln / n / 2
    o2 = [wire((x1, y1), a), wire(b, (x2, y2))]
    d = f'M{a[0]:.1f},{a[1]:.1f}'
    for i in range(n):
        if o == 'h':
            sx = 1 if b[0] > a[0] else -1
            d += f' a{r:.1f},{r:.1f} 0 0 {1 if sx > 0 else 0} {2 * r * sx:.1f},0'
        else:
            sy = 1 if b[1] > a[1] else -1
            d += f' a{r:.1f},{r:.1f} 0 0 {1 if sy > 0 else 0} 0,{2 * r * sy:.1f}'
    o2.append(f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:{W}"/>')
    return ''.join(o2)


def cap(x1, y1, x2, y2, c=AC, gap=10, plate=26):
    a, b, o = _seg(x1, y1, x2, y2, gap)
    out = [wire((x1, y1), a), wire(b, (x2, y2))]
    if o == 'h':
        out += [L(a[0], a[1] - plate / 2, a[0], a[1] + plate / 2, c, 3), L(b[0], b[1] - plate / 2, b[0], b[1] + plate / 2, c, 3)]
    else:
        out += [L(a[0] - plate / 2, a[1], a[0] + plate / 2, a[1], c, 3), L(b[0] - plate / 2, b[1], b[0] + plate / 2, b[1], c, 3)]
    return ''.join(out)


def vsrc(x, y1, y2, lab, r=20, c=LV):
    """independent voltage source on a vertical run, + at the top"""
    m = (y1 + y2) / 2
    return (wire((x, y1), (x, m - r)) + wire((x, m + r), (x, y2)) +
            f'<circle cx="{x:.1f}" cy="{m:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2.2"/>' +
            T(x, m - 4, '+', 15, fill=c, bold=True) + T(x, m + 13, '−', 15, fill=c, bold=True) + T(x - r - 8, m + 5, lab, 14, 'end'))


def isrc(x, y1, y2, lab, r=20, c=LV, up=True, anchor='end', dx=None):
    """independent current source on a vertical run, arrow up (current pushed upward)"""
    m = (y1 + y2) / 2
    a1, a2 = (m + 11, m - 11) if up else (m - 11, m + 11)
    dx = (-r - 8) if dx is None else dx
    return (wire((x, y1), (x, m - r)) + wire((x, m + r), (x, y2)) +
            f'<circle cx="{x:.1f}" cy="{m:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2.2"/>' +
            L(x, a1, x, a2, c, 2.2, arrow='l') + T(x + dx, m + 5, lab, 14, anchor))


def dep(x, y1, y2, kind, c=NX, r=20):
    """dependent source (diamond) on a vertical run: kind 'v' (+ above −) or 'i' (arrow up)"""
    m = (y1 + y2) / 2
    o = wire((x, y1), (x, m - r)) + wire((x, m + r), (x, y2))
    o += f'<polygon points="{x},{m - r} {x + r},{m} {x},{m + r} {x - r},{m}" style="fill:var(--fig);stroke:{c};stroke-width:2.2"/>'
    if kind == 'v':
        o += T(x, m - 3, '+', 14, fill=c, bold=True) + T(x, m + 14, '−', 14, fill=c, bold=True)
    else:
        o += L(x, m + 10, x, m - 10, c, 2.2, arrow='x')
    return o


def iarrow(x1, y, x2, lab, c=LV, above=True, size=14):
    """current arrow drawn just above (or below) a horizontal wire"""
    yy = y - 13 if above else y + 13
    ty = yy - 8 if above else yy + 20
    return L(x1, yy, x2, yy, c, 2.2, arrow='l') + T((x1 + x2) / 2, ty, lab, size, fill=c, bold=True)


def vlabel(x, ytop, ybot, lab, anchor='start', dx=10):
    """port voltage: + near the top terminal, − near the bottom, value between"""
    s = 1 if anchor == 'start' else -1
    return (T(x + s * dx, ytop + 6, '+', 16, anchor, LV, True) + T(x + s * dx, ybot + 4, '−', 16, anchor, LV, True) +
            T(x + s * dx, (ytop + ybot) / 2 + 5, lab, 14, anchor, LV, True))


def tnet(x0, yt, yb, Z1='2 Ω', Z2='3 Ω', Z3='4 Ω', span=300, c=AC, labels=True, flip=False):
    """T network between terminals at x0 (left) and x0+span (right); series arms on yt, shunt arm down to yb.
    flip=True puts the series arms on yb and the shunt arm up to yt. Returns (svg, centre x)."""
    xc = x0 + span / 2
    ya, yo = (yb, yt) if flip else (yt, yb)
    o = [res(x0, ya, xc, ya, c), res(xc, ya, x0 + span, ya, c), res(xc, ya, xc, yo, c), wire((x0, yo), (x0 + span, yo)), dot(xc, ya), dot(xc, yo)]
    if labels:
        off = 22 if flip else -18
        o += [T((x0 + xc) / 2, ya + off, Z1, 14, bold=True), T((xc + x0 + span) / 2, ya + off, Z2, 14, bold=True),
              T(xc + 14, (ya + yo) / 2 + 5, Z3, 14, 'start', bold=True)]
    return ''.join(o), xc


def mat(x, y, rows, size=14, colw=None, rh=20, c=INK, name=None, unit=None):
    """a 2 x 2 matrix in square brackets, centred at x, first row baseline y"""
    colw = colw or max(tw(v, size) for r in rows for v in r) + 14
    w = 2 * colw + 8
    x0 = x - w / 2
    o = []
    if name: o.append(T(x0 - 8, y + rh / 2 + 4, name, size, 'end', bold=True))
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            o.append(T(x0 + 4 + colw * j + colw / 2, y + i * rh + 5, v, size, fill=c))
    yt, yb = y - rh / 2 - 4, y + rh * 1.5
    o.append(P([(x0 + 6, yt), (x0, yt), (x0, yb), (x0 + 6, yb)], INK, 1.6))
    o.append(P([(x0 + w - 6, yt), (x0 + w, yt), (x0 + w, yb), (x0 + w - 6, yb)], INK, 1.6))
    if unit: o.append(T(x0 + w + 8, y + rh / 2 + 4, unit, size, 'start', MUT))
    return ''.join(o)


# ---- 6.1 the terminated T network: four port variables and the entering convention ----
def f1():
    o = []
    yt, yb = 110, 260
    xs, x1, x2, xl = 60, 220, 500, 650
    o.append(R(x1 + 14, yt - 66, x2 - x1 - 28, yb - yt + 96, 'none', L2, 10, 1.6, '7 6'))
    o.append(T((x1 + x2) / 2, yt - 46, 'the two-port (T network)', 14, fill=MUT))
    s, xc = tnet(x1 + 40, yt, yb, span=x2 - x1 - 80); o.append(s)
    o += [wire((x1, yt), (x1 + 40, yt)), wire((x2 - 40, yt), (x2, yt)), wire((x1, yb), (x1 + 40, yb)), wire((x2 - 40, yb), (x2, yb))]
    o += [vsrc(xs, yt, yb, ''), wire((xs, yt), (x1, yt)), wire((xs, yb), (x1, yb))]
    o.append(T(xs + 28, (yt + yb) / 2 + 5, '12 V', 14, 'start', LV, True))
    o += [res(xl, yt, xl, yb, LV), wire((x2, yt), (xl, yt)), wire((x2, yb), (xl, yb)), T(xl + 14, (yt + yb) / 2 + 5, '1 Ω', 14, 'start', bold=True)]
    o.append(T(xl + 14, (yt + yb) / 2 + 25, 'load', 14, 'start', MUT))
    o += [term(x1, yt, '1', 0, -12), term(x1, yb, '1′', 0, 26), term(x2, yt, '2', 0, -12), term(x2, yb, '2′', 0, 26)]
    o.append(iarrow(x1 - 74, yt, x1 - 16, 'I₁ = 3 A'))
    o.append(iarrow(x2 + 86, yt, x2 + 16, 'I₂ = −1.5 A'))
    o.append(iarrow(x2 + 24, yt, x2 + 80, 'real 1.5 A', c=NX, above=False, size=13))
    o.append(vlabel(x1, yt + 26, yb - 14, 'V₁ = 12 V', 'end', 12))
    o.append(vlabel(x2, yt + 46, yb - 14, 'V₂ = 1.5 V', 'start', 12))
    o.append(T(360, yb + 54, 'P = V₁I₁ + V₂I₂ = 36 − 2.25 = 33.75 W enters the two-port (its resistor losses).', 14))
    o.append(T(360, yb + 76, 'The real 1.5 A leaves terminal 2, so the entering current I₂ is negative.', 14, fill=MUT))
    return yb + 92, ''.join(o)
FIG[1] = (f1, 'The T network as a two-port between a 12 V source and a 1 Ω load. Both arrows I₁ and I₂ point into the network; the real load current leaves terminal 2, so I₂ = −1.5 A and V₂ = −I₂ × 1 Ω = 1.5 V.',
          'A T network of 2, 3 and 4 ohms inside a dashed box with terminals 1, 1 prime, 2, 2 prime. A 12 volt source drives port 1 with I1 = 3 A entering; a 1 ohm load at port 2 carries 1.5 A out, so I2 entering is minus 1.5 A and V2 is 1.5 V.')


# ---- 6.2 the open-circuit test (z) and the short-circuit test (y) on the T network ----
def f2():
    o = []

    def panel(y0, title, mode):
        yt, yb = y0 + 56, y0 + 176
        x1, x2, xs = 170, 420, 90
        o.append(T(30, y0 + 8, title, 15, 'start', bold=True))
        s, xc = tnet(x1, yt, yb, span=x2 - x1); o.append(s)
        o.extend([term(x1, yt, '1', 0, -12), term(x1, yb, '1′', 0, 26), term(x2, yt, '2', 0, -12), term(x2, yb, '2′', 0, 26)])
        if mode == 'z':
            o.append(isrc(xs, yt, yb, '')); o.extend([wire((xs, yt), (x1, yt)), wire((xs, yb), (x1, yb))])
            o.append(T(xs - 26, (yt + yb) / 2 + 5, '1 A', 14, 'end', LV, True))
            o.append(vlabel(x1, yt + 22, yb - 12, 'V₁ = 6 V', 'start', 10))
            o.append(vlabel(x2, yt + 22, yb - 12, 'V₂ = 4 V', 'start', 12))
            o.append(T(x2 + 20, yt + 5, 'open', 14, 'start', MUT))
            o.append(T(530, yt + 30, 'z₁₁ = V₁/I₁ = 6 Ω', 14, 'start', AC, True))
            o.append(T(530, yt + 56, 'z₂₁ = V₂/I₁ = 4 Ω', 14, 'start', AC, True))
            o.append(T(530, yt + 82, 'no current in 3 Ω', 13, 'start', MUT))
        else:
            o.append(vsrc(xs, yt, yb, '1 V')); o.extend([wire((xs, yt), (x1, yt)), wire((xs, yb), (x1, yb))])
            o.extend([wire((x2, yt), (x2 + 44, yt), (x2 + 44, yb), (x2, yb))])
            o.append(T(x2 + 52, yb - 10, 'short', 14, 'start', MUT))
            o.append(iarrow(x1 - 74, yt, x1 - 28, 'I₁ = 0.2692 A', size=13))
            o.append(L(x2 + 6, yt + 13, x2 + 40, yt + 13, NX, 2.2, arrow='x'))
            o.append(T(x2 + 52, yt + 18, '0.1538 A', 13, 'start', NX, True))
            o.append(T(566, yt + 8, 'y₁₁ = I₁/V₁', 14, 'start', AC, True))
            o.append(T(584, yt + 28, '= 0.2692 S', 14, 'start', AC, True))
            o.append(T(566, yt + 56, 'y₂₁ = I₂/V₁', 14, 'start', AC, True))
            o.append(T(584, yt + 76, '= −0.1538 S', 14, 'start', AC, True))
            o.append(T(566, yt + 102, 'real current leaves', 13, 'start', MUT))
            o.append(T(566, yt + 118, 'terminal 2', 13, 'start', MUT))
    panel(10, '(a) Z test: port 2 open, 1 A into port 1', 'z')
    o.append(L(30, 218, 690, 218, LN, 1))
    panel(230, '(b) Y test: port 2 shorted, 1 V at port 1', 'y')
    return 438, ''.join(o)
FIG[2] = (f2, 'The two tests on the T network. With port 2 open, 1 A gives 6 V at port 1 and 4 V at port 2 (z₁₁ = 6 Ω, z₂₁ = 4 Ω). With port 2 shorted, 1 V drives 0.2692 A in and 0.1538 A out of terminal 2 (y₁₁ = 0.2692 S, y₂₁ = −0.1538 S).',
          'Two circuit panels of the 2, 3, 4 ohm T network. Top: a 1 A source at port 1 with port 2 open gives V1 = 6 V and V2 = 4 V. Bottom: a 1 V source with port 2 shorted gives I1 = 0.2692 A and 0.1538 A flowing out of terminal 2 into the short.')


# ---- 6.3 the h-parameter equivalent circuit with the transistor example ----
def f3():
    o = []
    yt, yb = 70, 230
    x1, x2 = 60, 660
    # input loop: terminal 1 - h11 - dependent V source down to 1'
    xr2, xd = 220, 250
    o += [term(x1, yt, '1', -12, 5, 'end'), term(x1, yb, '1′', -12, 5, 'end')]
    o.append(res(x1, yt, xr2, yt, AC))
    o.append(T((x1 + xr2) / 2 + 10, yt + 30, 'h₁₁ = 1 kΩ', 14, bold=True))
    o.append(wire((xr2, yt), (xd, yt)))
    o.append(dep(xd, yt, yb, 'v'))
    o.append(wire((x1, yb), (xd, yb)))
    o.append(T(xd + 28, (yt + yb) / 2 - 6, 'h₁₂V₂', 14, 'start', NX, True))
    o.append(T(xd + 28, (yt + yb) / 2 + 14, '= −0.01 V', 14, 'start', NX))
    o.append(iarrow(x1 + 12, yt, x1 + 56, 'I₁ = 10 μA', size=13))
    o.append(vlabel(x1, yt + 56, yb - 14, 'V₁ = 0 V', 'start', 10))
    # output: dependent I source, 1/h22, terminals 2,2'
    xi, xg = 480, 580
    o.append(wire((xi, yt), (x2, yt))); o.append(wire((xi, yb), (x2, yb)))
    o.append(dep(xi, yb, yt, 'i'))
    o.append(T(xi - 28, (yt + yb) / 2 - 6, 'h₂₁I₁', 14, 'end', NX, True))
    o.append(T(xi - 28, (yt + yb) / 2 + 14, '= 0.5 mA', 14, 'end', NX))
    o.append(res(xg, yt, xg, yb, AC))
    o.append(T(xg + 14, (yt + yb) / 2 - 6, '1/h₂₂', 14, 'start', bold=True))
    o.append(T(xg + 14, (yt + yb) / 2 + 14, '= 50 kΩ', 14, 'start'))
    o += [dot(xg, yt), dot(xg, yb), term(x2, yt, '2', 12, 5, 'start'), term(x2, yb, '2′', 12, 5, 'start')]
    o.append(L(x2 - 8, yt - 13, x2 - 50, yt - 13, LV, 2.2, arrow='l'))
    o.append(T(x2 - 30, yt - 22, 'I₂ = 0.4 mA', 13, fill=LV, bold=True))
    o.append(T(x2 - 4, yb + 44, 'V₂ = −5 V across a 12.5 kΩ load', 14, 'end', LV, True))
    o.append(T(x1, yb + 44, 'V₁ = h₁₁I₁ + h₁₂V₂ = 0.01 − 0.01 = 0 V', 14, 'start'))
    o.append(T(x1, yb + 68, 'I₂ = h₂₁I₁ + h₂₂V₂ = 0.5 − 0.1 = 0.4 mA', 14, 'start'))
    return yb + 84, ''.join(o)
FIG[3] = (f3, 'The h-parameter model: h₁₁ in series with the feedback source h₁₂V₂ at the input, the current source h₂₁I₁ in parallel with 1/h₂₂ at the output. With the example numbers the two input terms cancel and 0.4 mA enters terminal 2.',
          'An equivalent circuit: at the input a 1 kilo-ohm resistor h11 in series with a diamond voltage source h12 V2 = minus 0.01 V; at the output a diamond current source h21 I1 = 0.5 mA in parallel with 50 kilo-ohm 1 over h22. I1 = 10 microamps, V2 = minus 5 V, I2 = 0.4 mA.')


# ---- 6.4 the T network as a cascade of three ABCD blocks ----
def f4():
    o = []
    yt, yb = 60, 190
    xa, xb, xc, xd = 70, 250, 390, 570
    o += [term(xa, yt, '1', 0, -12), term(xa, yb, '1′', 0, 26)]
    o.append(res(xa, yt, xb, yt, AC)); o.append(T((xa + xb) / 2, yt - 18, '2 Ω', 14, bold=True))
    o.append(wire((xb, yt), (xc, yt)))
    o.append(res((xb + xc) / 2, yt, (xb + xc) / 2, yb, AC)); o.append(T((xb + xc) / 2 + 14, (yt + yb) / 2 - 4, '4 Ω', 14, 'start', bold=True)); o.append(T((xb + xc) / 2 + 14, (yt + yb) / 2 + 16, '(0.25 S)', 14, 'start'))
    o += [dot((xb + xc) / 2, yt), dot((xb + xc) / 2, yb)]
    o.append(res(xc, yt, xd, yt, AC)); o.append(T((xc + xd) / 2, yt - 18, '3 Ω', 14, bold=True))
    o.append(wire((xa, yb), (650, yb)))
    o += [term(xd, yt, '2', 0, -12), term(xd, yb)]
    o.append(wire((xd, yt), (650, yt))); o.append(res(650, yt, 650, yb, LV)); o.append(T(664, (yt + yb) / 2 + 5, '10 Ω', 14, 'start', LV, True))
    for x in (xb - 20, xc + 20):
        o.append(L(x, yt - 34, x, yb + 12, L2, 1.4, '5 5'))
    y = yb + 56
    o.append(mat((xa + xb) / 2 - 6, y, [['1', '2'], ['0', '1']]))
    o.append(T((xa + xb) / 2 + 60, y + 15, '×', 18, fill=MUT))
    o.append(mat((xb + xc) / 2 - 4, y, [['1', '0'], ['0.25', '1']]))
    o.append(T((xb + xc) / 2 + 66, y + 15, '×', 18, fill=MUT))
    o.append(mat((xc + xd) / 2, y, [['1', '3'], ['0', '1']]))
    o.append(T((xc + xd) / 2 + 58, y + 15, '=', 18, fill=MUT))
    o.append(mat(xd + 70, y, [['1.5', '6.5'], ['0.25', '1.75']], c=AC))
    o.append(T((xa + xb) / 2 - 6, y + 66, 'series arm', 13, fill=MUT)); o.append(T((xb + xc) / 2 - 4, y + 66, 'shunt arm', 13, fill=MUT)); o.append(T((xc + xd) / 2, y + 66, 'series arm', 13, fill=MUT)); o.append(T(xd + 70, y + 66, 'the T network', 13, fill=AC))
    o.append(T(360, y + 96, 'Zin = (A·ZL + B)/(C·ZL + D) = (15 + 6.5)/(2.5 + 1.75) = 5.06 Ω with the 10 Ω load', 14, bold=True))
    return y + 112, ''.join(o)
FIG[4] = (f4, 'The T network cut into a series 2 Ω arm, a shunt 0.25 S arm and a series 3 Ω arm. Multiplying their ABCD matrices in signal order gives [1.5 6.5; 0.25 1.75], and with a 10 Ω load the input impedance is 5.06 Ω.',
          'The T network drawn as three sections separated by dashed lines, each with its ABCD matrix below: series 2 ohm [1 2; 0 1], shunt 0.25 siemens [1 0; 0.25 1], series 3 ohm [1 3; 0 1], multiplying to [1.5 6.5; 0.25 1.75]. A 10 ohm load gives input impedance 5.06 ohm.')


# ---- 6.5 one network, four matrices ----
def f5():
    o = []
    s, xc = tnet(280, 175, 245, span=160); o.append(s)
    o += [term(280, 175), term(280, 245), term(440, 175), term(440, 245)]
    o.append(T(360, 280, 'the same T network', 13, fill=MUT))
    boxes = [(30, 24, 'Z (Ω)', [['6', '4'], ['4', '7']]),
             (470, 24, 'Y (S)', [['0.2692', '−0.1538'], ['−0.1538', '0.2308']]),
             (30, 300, 'h', [['3.714 Ω', '0.571'], ['−0.571', '0.143 S']]),
             (470, 300, 'ABCD', [['1.5', '6.5 Ω'], ['0.25 S', '1.75']])]
    for x, y, name, rows in boxes:
        o.append(R(x, y, 220, 96, PANEL, AC, 10))
        o.append(T(x + 14, y + 24, name, 15, 'start', AC, True))
        o.append(mat(x + 120, y + 52, rows, 14))
    o.append(L(252, 72, 466, 72, AC, 2, arrow='n')); o.append(Tb(359, 66, 'invert: y₁₁ = z₂₂/Δz', 13))
    o.append(L(140, 122, 140, 296, AC, 2, arrow='n')); o.append(Tb(140, 214, 'h₁₁ = Δz/z₂₂', 13))
    o.append(L(580, 122, 580, 296, AC, 2, arrow='n')); o.append(Tb(580, 214, 'A = −y₂₂/y₂₁', 13))
    o.append(T(360, 424, 'Δz = 26 Ω², Δy = 1/26 S², Δh = 6/7, AD − BC = 1', 14, bold=True))
    o.append(T(360, 446, 'Reciprocal in every form: z₁₂ = z₂₁, y₁₂ = y₂₁, h₁₂ = −h₂₁, AD − BC = 1', 14, fill=MUT))
    return 462, ''.join(o)
FIG[5] = (f5, 'The T network of this unit written in four parameter sets. The arrows name the conversion used; every route gives the same port behaviour, and each set shows the reciprocity test in its own form.',
          'Four boxes around a small T network: Z = [6 4; 4 7] ohms, Y = [0.2692 minus 0.1538; minus 0.1538 0.2308] siemens, h = [3.714 ohm 0.571; minus 0.571 0.143 S], ABCD = [1.5 6.5 ohm; 0.25 S 1.75], with arrows labelled by the conversion formulas.')


# ---- 6.6 series connection with network b turned over ----
def f6():
    o = []
    ya, yj, yb = 60, 196, 336
    x1, x2 = 150, 490
    s, xc = tnet(x1 + 30, ya, yj - 22, span=x2 - x1 - 60); o.append(s)
    o += [wire((x1, ya), (x1 + 30, ya)), wire((x2 - 30, ya), (x2, ya))]
    s, _ = tnet(x1 + 30, yj + 22, yb, span=x2 - x1 - 60, c=NX, flip=True); o.append(s)
    o += [wire((x1, yb), (x1 + 30, yb)), wire((x2 - 30, yb), (x2, yb))]
    o.append(wire((xc + 60, yj - 22), (xc + 60, yj + 22), c=INK, w=3))
    o += [dot(xc + 60, yj - 22), dot(xc + 60, yj + 22)]
    o.append(T(xc + 72, yj + 2, 'common terminals joined', 13, 'start', MUT))
    o.append(R(x1 + 8, ya - 42, x2 - x1 - 16, yj - ya + 26, 'none', AC, 10, 1.4, '6 5'))
    o.append(R(x1 + 8, yj + 8, x2 - x1 - 16, yb - yj + 34, 'none', NX, 10, 1.4, '6 5'))
    o.append(T(x2 + 14, ya + 34, 'network a', 14, 'start', AC, True))
    o.append(T(x2 + 14, yb - 40, 'network b,', 14, 'start', NX, True)); o.append(T(x2 + 14, yb - 22, 'turned over', 14, 'start', NX, True))
    o += [term(x1, ya, '1', -12, 5, 'end'), term(x1, yb, '1′', -12, 5, 'end'), term(x2, ya, '2', 12, 5, 'start'), term(x2, yb, '2′', 12, 5, 'start')]
    o.append(iarrow(x1 - 60, ya, x1 - 14, 'I₁'))
    o.append(T(560, 180, '[Z] = [Z of a] + [Z of b]', 15, 'start', bold=True))
    o.append(mat(612, 214, [['12', '8'], ['8', '14']], 14, unit='Ω'))
    o.append(T(360, yb + 66, 'Check z₁₁: I₁ runs through 2 + 4 Ω of a and 4 + 2 Ω of b, 12 Ω in all.', 14))
    o.append(T(360, yb + 88, 'Without turning b over the true matrix is [11.2 9.2; 9.2 12.2] Ω, so the sum would be wrong.', 14, fill=MUT))
    return yb + 104, ''.join(o)
FIG[6] = (f6, 'Two copies of the T network in series. Network b is turned over so that only the two common terminals meet; each network then still carries I₁ through its port 1 and I₂ through its port 2, and the Z matrices add to [12 8; 8 14] Ω.',
          'Network a, a T network with arms 2, 3 and 4 ohms, sits above network b, the same T network drawn upside down; their common terminals are joined in the middle. The combined ports are 1 to 1 prime and 2 to 2 prime, and the combined Z matrix is [12 8; 8 14] ohms.')


# ---- 6.7 the reciprocity test on the T network ----
def f7():
    o = []

    def panel(x0, drive):
        yt, yb = 70, 190
        xl, xr = x0 + 70, x0 + 270
        s, xc = tnet(xl, yt, yb, span=xr - xl); o.append(s)
        o.extend([term(xl, yt), term(xl, yb), term(xr, yt), term(xr, yb)])
        if drive == 1:
            o.append(isrc(x0 + 22, yt, yb, '', r=16)); o.append(T(x0 + 22, (yt + yb) / 2 + 42, '1 A', 14, fill=LV, bold=True)); o.extend([wire((x0 + 22, yt), (xl, yt)), wire((x0 + 22, yb), (xl, yb))])
            o.append(vlabel(xr, yt + 18, yb - 10, 'V₂ = 4 V', 'start', 12))
            o.append(T(x0 + 170, 30, 'drive port 1, port 2 open', 14, bold=True))
            o.append(T(x0 + 170, yb + 44, 'z₂₁ = V₂/I₁ = 4 Ω', 15, fill=AC, bold=True))
        else:
            o.append(isrc(xr + 48, yt, yb, '', r=16)); o.append(T(xr + 48, (yt + yb) / 2 + 42, '1 A', 14, fill=LV, bold=True)); o.extend([wire((xr, yt), (xr + 48, yt)), wire((xr, yb), (xr + 48, yb))])
            o.append(vlabel(xl, yt + 18, yb - 10, 'V₁ = 4 V', 'end', 12))
            o.append(T(x0 + 170, 30, 'drive port 2, port 1 open', 14, bold=True))
            o.append(T(x0 + 170, yb + 44, 'z₁₂ = V₁/I₂ = 4 Ω', 15, fill=AC, bold=True))
    panel(0, 1)
    panel(370, 2)
    o.append(L(362, 24, 362, 240, LN, 1))
    o.append(T(360, 276, 'Same 4 V both ways: reciprocal. But z₁₁ = 2 + 4 = 6 Ω and z₂₂ = 3 + 4 = 7 Ω: not symmetric.', 14, bold=True))
    return 292, ''.join(o)
FIG[7] = (f7, 'The reciprocity test on the T network: 1 A into either port gives 4 V at the other, open port, so z₁₂ = z₂₁. The open-circuit impedances 6 Ω and 7 Ω differ, so the network is reciprocal but not symmetric.',
          'Two panels of the T network. Left: a 1 A source at port 1 with port 2 open gives V2 = 4 V. Right: a 1 A source at port 2 with port 1 open gives V1 = 4 V. Below, z11 = 6 ohms and z22 = 7 ohms are unequal.')


# ---- 6.8 the LC function: alternating poles and zeros, Foster I and Cauer I ----
def f8():
    o = []
    # pole-zero strip on the j omega axis
    x0, x1, y = 70, 650, 60
    fx = lambda w: x0 + w / 2.2 * (x1 - 90 - x0)
    o.append(L(x0, y, x1, y, L2, 1.6, arrow='m'))
    o.append(T(x1 + 4, y + 5, 'ω', 15, 'start', MUT))
    for w, lab in ((0, '0'), (1, '1'), (1.414, '√2'), (1.732, '√3')):
        X = fx(w); o.append(L(X, y + 12, X, y + 18, L2, 1.4)); o.append(T(X, y + 34, lab, 13, fill=MUT))
    for w in (0, 1.414):
        X = fx(w); o.append(L(X - 7, y - 7, X + 7, y + 7, NX, 2.6)); o.append(L(X - 7, y + 7, X + 7, y - 7, NX, 2.6))
    for w in (1, 1.732):
        X = fx(w); o.append(f'<circle cx="{X:.1f}" cy="{y}" r="7" style="fill:var(--fig);stroke:var(--accent);stroke-width:2.6"/>')
    o.append(T(x1 - 6, y - 14, 'pole at ∞', 13, 'end', NX))
    o.append(T(x0, y - 20, '× pole   ○ zero of Z(s) = (s² + 1)(s² + 3)/[s(s² + 2)]: they alternate', 14, 'start', bold=True))
    # Foster I: series chain L 1H, C 2/3F, tank (1/4 H || 2 F)
    yA, yB = 196, 296
    xs = 60
    o.append(T(30, yA - 66, 'Foster I (partial fractions of Z): elements in series', 14, 'start', bold=True))
    o.append(term(xs, yA)); o.append(term(xs, yB))
    o.append(ind(xs, yA, 190, yA)); o.append(T(125, yA - 16, '1 H', 14, bold=True))
    o.append(cap(190, yA, 290, yA)); o.append(T(240, yA - 20, '2/3 F', 14, bold=True))
    o.append(wire((290, yA), (320, yA)))
    o.append(wire((320, yA - 26), (320, yA + 26)))
    o.append(ind(320, yA - 26, 440, yA - 26)); o.append(T(380, yA - 42, '1/4 H', 14, bold=True))
    o.append(cap(320, yA + 26, 440, yA + 26)); o.append(T(380, yA + 56, '2 F', 14, bold=True))
    o.append(wire((440, yA - 26), (440, yA + 26)))
    o.append(wire((440, yA), (480, yA), (480, yB), (xs, yB)))
    o.append(T(690, yA - 66, 'Z = s + 1.5/s + 0.5s/(s² + 2)', 14, 'end', AC, True))
    # Cauer I ladder: series L1 1H, shunt C2 1/2 F, series L3 4H, shunt C4 1/6F
    yC, yD = 390, 490
    o.append(T(30, yC - 34, 'Cauer I (continued fraction): a ladder', 14, 'start', bold=True))
    o.append(term(xs, yC)); o.append(term(xs, yD))
    o.append(ind(xs, yC, 200, yC)); o.append(T(130, yC - 16, '1 H', 14, bold=True))
    o.append(cap(220, yC, 220, yD)); o.append(T(238, (yC + yD) / 2 + 5, '1/2 F', 14, 'start', bold=True))
    o.append(wire((200, yC), (300, yC))); o.append(dot(220, yC)); o.append(dot(220, yD))
    o.append(ind(300, yC, 420, yC)); o.append(T(360, yC - 16, '4 H', 14, bold=True))
    o.append(cap(440, yC, 440, yD)); o.append(T(458, (yC + yD) / 2 + 5, '1/6 F', 14, 'start', bold=True))
    o.append(wire((420, yC), (440, yC)))
    o.append(wire((xs, yD), (440, yD)))
    o.append(T(690, yC - 34, 'Z = s + 1/(s/2 + 1/(4s + 1/(s/6)))', 13, 'end', AC, True))
    o.append(T(360, yD + 40, 'Both have four elements and the same Z(s): check Z(j1) = 0 in each.', 14, fill=MUT))
    return yD + 56, ''.join(o)
FIG[8] = (f8, 'The LC impedance of the worked example: its poles (×) and zeros (○) alternate along the jω axis, so it is realizable. Partial fractions give the Foster I chain and long division gives the Cauer I ladder; both have four elements.',
          'A frequency axis with poles at 0, root 2 and infinity and zeros at 1 and root 3, alternating. Below, Foster I: 1 H, 2/3 F and a tank of 1/4 H parallel 2 F in series. Below that, Cauer I: series 1 H, shunt 1/2 F, series 4 H, shunt 1/6 F.')


def spec(k):
    fn, cap_, aria = FIG[k]
    h, body = fn()
    return {'caption': cap_, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}


def drop_sources():
    return ['ocw.mit.edu', 'nptel.ac.in']


# ---------------- figures inside the model answers ----------------
def ma_q9():
    """Foster II and Cauer II realizations of Z(s) = (s² + 1)(s² + 4)/[s(s² + 2)]"""
    o = []
    yt, yb = 76, 256
    # Foster II: two series LC branches in parallel
    xs = 50
    o.append(T(30, 30, 'Foster II: two series LC branches in parallel', 14, 'start', bold=True))
    o += [term(xs, yt, '1', -12, 5, 'end'), term(xs, yb, '1′', -12, 5, 'end')]
    o.append(wire((xs, yt), (250, yt))); o.append(wire((xs, yb), (250, yb)))
    for x, l, c in ((140, '3 H', '1/3 F'), (250, '3/2 H', '1/6 F')):
        o.append(ind(x, yt, x, 166)); o.append(cap(x, 166, x, yb))
        o.append(T(x + 16, 126, l, 14, 'start', bold=True)); o.append(T(x + 22, 216, c, 14, 'start', bold=True))
    o += [dot(140, yt), dot(140, yb)]
    o.append(T(165, yb + 36, 'resonates at 1 rad/s and 2 rad/s', 13, fill=MUT))
    # Cauer II ladder: series C, shunt L, series C, shunt L
    o.append(L(352, 20, 352, yb + 50, LN, 1))
    x0 = 400
    o.append(T(380, 30, 'Cauer II: a ladder from the pole at s = 0', 14, 'start', bold=True))
    o += [term(x0, yt, '1', -12, 5, 'end'), term(x0, yb, '1′', -12, 5, 'end')]
    o.append(cap(x0, yt, 490, yt)); o.append(T(445, yt - 22, '1/2 F', 14, bold=True))
    o.append(wire((490, yt), (510, yt))); o.append(ind(510, yt, 510, yb)); o.append(T(524, 172, '3/2 H', 14, 'start', bold=True))
    o.append(cap(510, yt, 620, yt)); o.append(T(565, yt - 22, '1/9 F', 14, bold=True))
    o.append(wire((620, yt), (650, yt))); o.append(ind(650, yt, 650, yb)); o.append(T(664, 172, '3 H', 14, 'start', bold=True))
    o.append(wire((x0, yb), (650, yb))); o += [dot(510, yt), dot(510, yb)]
    o.append(T(540, yb + 36, 'series C, shunt L, series C, shunt L', 13, fill=MUT))
    o.append(T(360, yb + 72, 'Both networks have four elements and give the same Z(s); at s = j1 each gives Z = 0.', 14))
    return yb + 90, ''.join(o)


def ma_q11():
    """two T networks in series: grounded the same way (rule fails) and network b turned over (rule holds)"""
    o = []

    def panel(x0, ok):
        nonlocal o
        xl, xr = x0 + 50, x0 + 290
        ya, yj, yb = 66, 170, 274
        s, xc = tnet(xl + 20, ya, yj - 26, span=xr - xl - 40); o.append(s)
        o += [wire((xl, ya), (xl + 20, ya)), wire((xr - 20, ya), (xr, ya))]
        if ok:
            s, _ = tnet(xl + 20, yj + 26, yb, span=xr - xl - 40, c=NX, flip=True); o.append(s)
            o += [wire((xl, yb), (xl + 20, yb)), wire((xr - 20, yb), (xr, yb))]
            o.append(wire((xc + 44, yj - 26), (xc + 44, yj + 26), c=INK, w=3)); o += [dot(xc + 44, yj - 26), dot(xc + 44, yj + 26)]
            o.append(T(xc + 54, yj + 5, 'commons joined', 13, 'start', MUT))
            o += [term(xl, ya, '1', -10, 5, 'end'), term(xl, yb, '1′', -10, 5, 'end'), term(xr, ya, '2', 10, 5, 'start'), term(xr, yb, '2′', 10, 5, 'start')]
            o.append(T(x0 + 170, 24, 'b turned over: rule holds ✓', 14, fill=AC, bold=True))
            o.append(T(x0 + 170, yb + 56, '[Z] = [6 4; 4 7] + [6 4; 4 7]', 14))
            o.append(T(x0 + 170, yb + 80, '= [12 8; 8 14] Ω', 14, fill=AC, bold=True))
        else:
            s, _ = tnet(xl + 20, yj + 26, yb, span=xr - xl - 40, c=NX); o.append(s)
            # outer wiring: 1'a to 1b on the left, 2'a to 2b on the right
            o += [wire((xl, ya), (xl + 20, ya)), wire((xr - 20, ya), (xr, ya))]
            o.append(wire((xl + 20, yj - 26), (xl + 20, yj + 26), c=NX, w=3)); o.append(wire((xr - 20, yj - 26), (xr - 20, yj + 26), c=NX, w=3))
            o += [dot(xl + 20, yj - 26), dot(xl + 20, yj + 26), dot(xr - 20, yj - 26), dot(xr - 20, yj + 26)]
            o.append(wire((xl, yb), (xl + 20, yb))); o.append(wire((xr - 20, yb), (xr, yb)))
            o += [term(xl, ya, '1', -10, 5, 'end'), term(xl, yb, '1′', -10, 5, 'end'), term(xr, ya, '2', 10, 5, 'start'), term(xr, yb, '2′', 10, 5, 'start')]
            o.append(T(x0 + 170, 24, 'both commons at the bottom: rule fails ✗', 14, fill=NX, bold=True))
            o.append(T(x0 + 170, yb + 36, 'green links: a’s common wire joins 1 and 2 of b,', 13, fill=NX))
            o.append(T(x0 + 170, yb + 56, 'so b becomes 2 Ω ∥ 3 Ω + 4 Ω = 5.2 Ω in the lead', 13, fill=NX))
            o.append(T(x0 + 170, yb + 80, '[Z] = [11.2 9.2; 9.2 12.2] Ω', 14, fill=NX, bold=True))
        o.append(T(xr + 14, (ya + yj) / 2 - 10, 'a', 15, 'start', AC, True)); o.append(T(xr + 14, (yj + yb) / 2 + 18, 'b', 15, 'start', NX, True))
    panel(0, False)
    panel(370, True)
    o.append(L(362, 10, 362, 356, LN, 1))
    return 372, ''.join(o)
