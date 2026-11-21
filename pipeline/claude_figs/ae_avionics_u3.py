"""Claude's hand-drawn figures for ae-avionics-u3 (Aircraft Electrical and Electronics Systems: aircraft electrical systems and
instruments), one per chapter, drawn from each chapter's own worked example and numbers. Plotted curves are computed (the breaker
and wire time-current curves, the generator droop lines, the fuel-probe capacitance line). Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """V_out, R_th ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔΦ0-9])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def arrow(x1, y1, x2, y2, c=AC, w=2.5, a='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash=dash, arrow=a)


def bar(x, y, w, h, frac, fill=ACS, stroke=AC, back=PANEL):
    return R(x, y, w, h, back, L2, 4) + (R(x, y, w * frac, h, fill, stroke, 4) if frac > 0 else '')


def resistor_h(x, y, w=50, c=AC):
    """horizontal zig-zag from (x, y) to (x + w, y)"""
    pts = [(x, y), (x + 6, y)]
    n = 6; step = (w - 12) / n
    for i in range(n):
        pts.append((x + 6 + step * (i + 0.5), y + (-8 if i % 2 == 0 else 8)))
    pts += [(x + w - 6, y), (x + w, y)]
    return P(pts, c, 2.2)


FIG = {}


# ---- 3.1 one generator channel, and the worked example's load shedding ----
def f1():
    o = []
    # channel: generator -> GCB -> bus -> loads, GCU to the side
    o.append(boxt(20, 70, 120, 54, ['GEN 1', '28 V, 200 A'], ACS, AC, 14, bold_first=True))
    o.append(arrow(140, 97, 186, 97))
    o.append(boxt(190, 74, 90, 46, ['GCB 1'], PANEL, AC, 14, bold_first=True))
    o.append(arrow(280, 97, 326, 97))
    o.append(R(330, 72, 22, 150, ACS, AC, 3))
    o.append(T(341, 240, 'BUS 1', 13, bold=True))
    o.append(arrow(352, 110, 392, 110, AC, 2)); o.append(boxt(396, 92, 120, 36, ['non-essential'], PANEL, AC, 13))
    o.append(arrow(352, 176, 392, 176, AC, 2)); o.append(boxt(396, 158, 120, 36, ['essential'], PANEL, LV, 13))
    o.append(T(530, 115, '180 A', 14, 'start', INK, bold=True)); o.append(T(530, 181, '60 A', 14, 'start', INK, bold=True))
    # GCU beside the path
    o.append(boxt(120, 6, 120, 40, ['GCU'], PANEL, NX, 14, bold_first=True, dash='5 4'))
    o.append(L(150, 46, 100, 70, NX, 2, dash='5 4', arrow='x')); o.append(T(84, 56, 'field', 13, 'end', NX))
    o.append(L(210, 46, 235, 74, NX, 2, dash='5 4', arrow='x')); o.append(T(248, 60, 'trip', 13, 'start', NX))
    o.append(T(20, 150, 'GCU senses and controls;', 13, 'start', MUT)); o.append(T(20, 168, 'it carries no load current', 13, 'start', MUT))
    # load-shedding bars
    x0, y0, W = 120, 282, 440
    fx = lin(0, 260, x0, x0 + W)
    o.append(T(20, 272, 'GEN 2 fails: one 200 A generator left', 14, 'start', INK, bold=True))
    o.append(T(20, 306, 'before', 13, 'start', MUT))
    o.append(R(x0, 290, fx(180) - x0, 26, PANEL, AC, 3)); o.append(T((x0 + fx(180)) / 2, 308, 'non-essential 180 A', 13))
    o.append(R(fx(180), 290, fx(240) - fx(180), 26, LVS, LV, 3)); o.append(T(fx(222), 308, '60 A', 13))
    o.append(T(20, 348, 'after shed', 13, 'start', MUT))
    o.append(R(x0, 332, fx(60) - x0, 26, LVS, LV, 3)); o.append(T((x0 + fx(60)) / 2, 350, '60 A', 13))
    o.append(L(fx(200), 280, fx(200), 368, NX, 2.2, dash='6 4'))
    o.append(T(fx(200), 384, 'rating 200 A', 13, 'middle', NX, bold=True))
    o.append(T(fx(244) + 6, 308, '240 A: shed ≥ 40 A', 13, 'start', INK, bold=True))
    o.append(T(fx(64) + 6, 350, '30 % of rating', 13, 'start', LV, bold=True))
    return 396, ''.join(o)


FIG[1] = (f1, 'One generator channel: the power goes generator → GCB → busbar → loads, while the GCU beside it controls the field and trips the GCB. '
              'In the worked example the surviving 200 A generator faces 240 A, so at least 40 A must go; dropping all 180 A of non-essential load leaves 60 A, 30 % of its rating.',
          'Block diagram: generator 1, 28 volts 200 amps, feeds GCB 1 and bus 1, which feeds non-essential loads of 180 amps and essential loads of 60 amps. A dashed GCU '
          'box beside it sends field control to the generator and a trip line to the GCB. Below, two bars: 240 amps before shedding against a 200 amp rating line, and 60 amps after shedding.')


# ---- 3.2 conversion between the buses, and the auto-transformer of worked example 2 ----
def f2():
    o = []
    o.append(R(20, 30, 24, 230, ACS, AC, 3)); o.append(T(32, 280, 'AC bus', 13, bold=True)); o.append(T(32, 296, '115/200 V', 13, fill=MUT))
    o.append(arrow(44, 70, 90, 70)); o.append(T(67, 60, '17.6 A', 13, fill=MUT))
    o.append(boxt(94, 44, 110, 52, ['TRU', '92 %'], PANEL, AC, 14, bold_first=True))
    o.append(T(149, 116, '6087 W in → 5600 W out', 13, fill=MUT))
    o.append(arrow(204, 70, 250, 70)); o.append(T(227, 60, '200 A', 13, fill=MUT))
    o.append(R(254, 30, 24, 230, LVS, LV, 3)); o.append(T(266, 280, 'DC bus', 13, bold=True)); o.append(T(266, 296, '28 V', 13, fill=MUT))
    o.append(boxt(94, 150, 110, 44, ['battery'], PANEL, LV, 14, bold_first=True))
    o.append(L(204, 172, 254, 172, LV, 2.5))
    o.append(T(149, 214, 'charged by, and', 13, fill=MUT)); o.append(T(149, 230, 'holds up, the DC bus', 13, fill=MUT))
    o.append(arrow(278, 140, 316, 140, LV))
    o.append(boxt(320, 116, 104, 48, ['inverter'], PANEL, LV, 14, bold_first=True))
    o.append(arrow(424, 140, 452, 140, LV))
    o.append(boxt(320, 184, 104, 46, ['standby AC', '115 V 400 Hz'], PANEL, LV, 13, bold_first=True))
    o.append(P([(456, 140), (470, 140), (470, 207), (424, 207)], LV, 2.2))
    # auto-transformer
    X = 590
    o.append(T(X, 26, 'auto-transformer', 14, bold=True))
    o.append(L(X, 44, X, 250, AC, 3))
    for i in range(9):
        o.append(f'<path d="M{X:.1f},{52 + i * 20:.1f} a10,10 0 0 1 0,20" style="fill:none;stroke:var(--accent);stroke-width:2.2"/>')
    o.append(L(X, 44, 520, 44, AC, 2.2)); o.append(C(520, 44, 4.5, AC)); o.append(T(510, 40, '115 V', 13, 'end', INK, bold=True))
    o.append(L(X, 250, 520, 250, AC, 2.2)); o.append(C(520, 250, 4.5, AC)); o.append(T(510, 256, '0 V', 13, 'end', INK))
    o.append(L(X + 10, 202, 690, 202, LV, 2.2)); o.append(C(690, 202, 4.5, LV)); o.append(T(690, 190, '26 V', 13, 'end', LV, bold=True))
    o.append(arrow(532, 44, 572, 44, AC, 2)); o.append(T(552, 66, '0.452 A in', 13, 'middle', MUT))
    o.append(arrow(628, 202, 668, 202, LV, 2)); o.append(T(648, 224, '2 A out', 13, 'middle', LV, bold=True))
    o.append(T(X - 10, 214, 'common turns', 13, 'end', MUT)); o.append(T(X - 10, 230, '1.548 A', 13, 'end', MUT))
    o.append(T(600, 286, 'ratio 26 ÷ 115 = 0.226', 13, 'middle', INK))
    o.append(T(600, 304, 'one winding: no isolation', 13, 'middle', NX, bold=True))
    return 316, ''.join(o)


FIG[2] = (f2, 'Left: the TRU of Worked example 1 turns 6087 W from the 115/200 V AC bus (17.6 A per line) into 200 A at 28 V; the battery sits on the DC bus, and the inverter '
              'remakes 115 V 400 Hz for the standby bus from it. Right: Worked example 2\'s auto-transformer: 0.452 A in at 115 V, 2 A out at 26 V, and only the 1.548 A difference '
              'in the common turns.',
          'Left: an AC bus feeds a 92 per cent TRU drawing 17.6 amps per line and delivering 200 amps to a 28 volt DC bus. A battery connects to the DC bus, which feeds an inverter '
          'and a 115 volt 400 hertz standby AC bus. Right: one coil tapped at 26 volts from a 115 volt supply, with 0.452 amps in, 2 amps out and 1.548 amps in the common section.')


# ---- 3.3 cells per battery, and the worked examples' capacity bars ----
def f3():
    o = []
    rows = [('lead-acid', 12, '2 V', '24 V', AC, ACS), ('NiCd', 20, '1.2 V', '24 V', LV, LVS), ('lithium-ion', 8, '3.7 V', '29.6 V', NX, NXS)]
    o.append(T(20, 24, 'cells in series', 14, 'start', MUT, bold=True))
    for j, (name, n, v, tot, c, cs) in enumerate(rows):
        y = 40 + j * 54
        o.append(T(20, y + 22, name, 14, 'start', INK, bold=True))
        cw = min(17, 300 / n)
        for i in range(n):
            o.append(R(120 + i * cw, y + 6, cw - 3, 24, cs, c, 2, sw=1.5))
        o.append(T(120 + n * cw + 10, y + 23, f'{n} × {v} = {tot}', 14, 'start', INK))
    # capacity bars
    x0, W = 140, 420
    o.append(T(20, 222, 'Worked example 1: 40 Ah battery, 40 A for 30 min', 14, 'start', INK, bold=True))
    o.append(R(x0, 236, W, 30, PANEL, L2, 4))
    o.append(R(x0, 236, W * 0.5, 30, ACS, AC, 4)); o.append(T(x0 + W * 0.25, 256, 'used 20 Ah', 13, bold=True))
    o.append(T(x0 + W * 0.75, 256, 'left 20 Ah = 1 h at 20 A', 13))
    o.append(T(20, 256, 'DoD 50 %', 13, 'start', AC, bold=True))
    o.append(T(20, 300, 'Worked example 2: NiCd capacity check, 40 A to 20 V in 51 min', 14, 'start', INK, bold=True))
    o.append(R(x0, 314, W, 30, PANEL, L2, 4))
    o.append(R(x0, 314, W * 0.85, 30, LVS, LV, 4)); o.append(T(x0 + W * 0.42, 334, '34 Ah delivered', 13, bold=True))
    o.append(T(x0 + W * 0.85 + 6, 360, 'rated 40 Ah', 13, 'middle', MUT))
    o.append(L(x0 + W, 310, x0 + W, 348, MUT, 1.5, dash='4 3'))
    o.append(T(20, 334, '85 %', 13, 'start', LV, bold=True))
    return 372, ''.join(o)


FIG[3] = (f3, 'Top: a 24 V battery needs 12 lead-acid cells or 20 NiCd cells; eight lithium-ion cells give about 29.6 V. Below: Worked example 1 takes 20 Ah from a 40 Ah battery '
              '(50 % depth of discharge), and Worked example 2\'s capacity check finds 34 Ah, 85 % of the rating.',
          'Three rows of cells: 12 lead-acid cells of 2 volts making 24 volts, 20 nickel-cadmium cells of 1.2 volts making 24 volts, and 8 lithium-ion cells of 3.7 volts making '
          '29.6 volts. Below, a bar half filled showing 20 ampere-hours used of 40, and a bar 85 per cent filled showing 34 ampere-hours delivered in a capacity check.')


# ---- 3.4 the emergency changeover and the worked example's battery time ----
def f4():
    o = []
    steps = [('all generators', 'lost', NX, NXS), ('battery holds', 'essential DC', LV, LVS), ('RAT deploys', 'spins up', AC, PANEL), ('emergency AC', '+ essential TRU', AC, ACS)]
    x = 14
    for i, (a, b, c, cs) in enumerate(steps):
        o.append(boxt(x, 20, 156, 56, [a, b], cs, c, 14, bold_first=True))
        if i < 3: o.append(arrow(x + 156, 48, x + 176, 48))
        x += 176
    o.append(T(270, 98, 'seconds', 13, 'middle', MUT)); o.append(L(200, 92, 228, 92, MUT, 1.5)); o.append(L(312, 92, 340, 92, MUT, 1.5))
    # numbers
    o.append(T(20, 136, 'essential DC bus 2.8 kW at 28 V → I = 100 A', 14, 'start', INK, bold=True))
    o.append(T(20, 158, 'battery 40 Ah, 50 % usable = 20 Ah → t = 20 ÷ 100 = 0.2 h = 12 min', 14, 'start', INK))
    x0, x1 = 60, 680
    fx = lin(0, 120, x0, x1)
    o.append(xaxis(x0, x1, 240, [0, 20, 40, 60, 80, 100, 120], fx, 'minutes after losing all generators'))
    o.append(R(fx(0), 196, fx(12) - fx(0), 30, LVS, LV, 3)); o.append(T(fx(12) + 8, 216, 'battery alone: 12 min', 13, 'start', LV, bold=True))
    o.append(L(fx(120), 186, fx(120), 240, NX, 2.4, dash='6 4'))
    o.append(T(fx(120), 180, 'ETOPS 120: 840 nm at 420 kt', 13, 'end', NX, bold=True))
    o.append(T(370, 310, 'the RAT or the APU generator must carry the essential loads long before 120 min', 13, 'middle', MUT))
    return 322, ''.join(o)


FIG[4] = (f4, 'The changeover after all generators are lost: the battery holds the essential DC bus for the seconds until the RAT is on line. In the worked example the battery alone '
              'would last 12 minutes at 100 A, a tenth of an ETOPS 120 diversion, so it can only bridge.',
          'Four boxes in a row: all generators lost, battery holds essential DC, RAT deploys, emergency AC plus essential TRU. Below, a time axis from 0 to 120 minutes with a short '
          'bar for the battery lasting 12 minutes and a dashed line at 120 minutes for ETOPS 120.')


# ---- 3.5 navigation light arcs and the worked example's emergency pack ----
def wedge(cx, cy, r, a0, a1, fill, stroke):
    """sector from bearing a0 to a1 (degrees clockwise from the nose, nose = up)"""
    p0 = (cx + r * math.sin(math.radians(a0)), cy - r * math.cos(math.radians(a0)))
    p1 = (cx + r * math.sin(math.radians(a1)), cy - r * math.cos(math.radians(a1)))
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return (f'<path d="M{cx:.1f},{cy:.1f} L{p0[0]:.1f},{p0[1]:.1f} A{r},{r} 0 {large} 1 {p1[0]:.1f},{p1[1]:.1f} Z" '
            f'style="fill:{fill};stroke:{stroke};stroke-width:1.6;fill-opacity:0.55"/>')


def f5():
    o = []
    cx, cy = 200, 190
    # aircraft plan view, nose up
    o.append(wedge(cx - 100, cy, 84, 250, 360, PANEL, INK))   # red, left wingtip: dead ahead to 110 deg left
    o.append(wedge(cx + 100, cy, 84, 0, 110, PANEL, INK))     # green, right wingtip
    o.append(wedge(cx, cy + 116, 70, 110, 250, PANEL, INK))   # white, tail: 70 deg either side of aft
    o.append(f'<path d="M{cx},{cy - 120} C{cx + 14},{cy - 100} {cx + 14},{cy + 90} {cx + 6},{cy + 116} L{cx - 6},{cy + 116} C{cx - 14},{cy + 90} {cx - 14},{cy - 100} {cx},{cy - 120} Z" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    o.append(P([(cx - 12, cy - 10), (cx - 100, cy + 16), (cx - 100, cy + 28), (cx - 12, cy + 18)], INK, 2, fill=PANEL))
    o.append(P([(cx + 12, cy - 10), (cx + 100, cy + 16), (cx + 100, cy + 28), (cx + 12, cy + 18)], INK, 2, fill=PANEL))
    o.append(C(cx - 100, cy, 6, INK)); o.append(C(cx + 100, cy, 6, INK)); o.append(C(cx, cy + 116, 6, INK))
    o.append(T(cx - 140, cy - 100, 'RED 110°', 14, 'middle', INK, bold=True)); o.append(T(cx - 140, cy - 82, 'left (port)', 13, 'middle', MUT))
    o.append(T(cx + 156, cy - 100, 'GREEN 110°', 14, 'middle', INK, bold=True)); o.append(T(cx + 156, cy - 82, 'right (starboard)', 13, 'middle', MUT))
    o.append(T(cx, cy + 212, 'WHITE 140° at the tail', 14, 'middle', INK, bold=True))
    o.append(T(cx, 26, 'nose', 13, 'middle', MUT)); o.append(arrow(cx, 38, cx, 64, MUT, 1.6, 'm'))
    # pack
    px = 420
    o.append(T(px, 30, 'emergency pack: 24 V, 4 Ah, 6 A max', 14, 'start', INK, bold=True))
    o.append(T(px, 60, '12 exit signs × 6 W = 72 W', 13, 'start')); o.append(T(px, 80, '20 floor lights × 3 W = 60 W', 13, 'start'))
    o.append(T(px, 104, 'total 132 W ÷ 24 V = 5.5 A', 14, 'start', INK, bold=True))
    o.append(T(px, 140, 'current against the 6 A limit', 13, 'start', MUT))
    o.append(bar(px, 150, 280, 24, 5.5 / 6, LVS, LV)); o.append(T(px + 140, 167, '5.5 A of 6 A', 13, bold=True))
    o.append(T(px, 206, 'charge in 12 min: 5.5 × 0.2 = 1.1 Ah', 13, 'start', MUT))
    o.append(bar(px, 216, 280, 24, 1.1 / 4, ACS, AC)); o.append(T(px + 180, 233, '1.1 of 4 Ah (27.5 %)', 13, bold=True))
    o.append(T(px, 274, 'both limits met: the pack holds', 14, 'start', LV, bold=True))
    o.append(T(px, 298, 'energy 1.1 Ah × 24 V = 26.4 Wh', 13, 'start', MUT))
    return 420, ''.join(o)


FIG[5] = (f5, 'Left: the navigation lights seen from above: red on the left wingtip and green on the right, each through 110° from dead ahead, and white at the tail through 140°. '
              'Right: the worked example\'s emergency pack: 132 W of lamps draw 5.5 A against its 6 A limit and use 1.1 Ah, 27.5 % of its 4 Ah, in 12 minutes.',
          'Plan view of an aircraft, nose up, with a red sector from the left wingtip covering 110 degrees from ahead, a green sector from the right wingtip, and a white sector of '
          '140 degrees behind the tail. Beside it, the pack sums: 72 watts plus 60 watts is 132 watts, 5.5 amps against a 6 amp limit, and 1.1 of 4 ampere-hours used.')


# ---- 3.6 the heat path of the two worked examples ----
def f6():
    o = []
    x0, y0, y1 = 120, 40, 330
    fy = lin(20, 130, y1, y0)
    o.append(L(x0, y0 - 6, x0, y1, L2, 1.5))
    for v in (20, 40, 60, 80, 100, 120):
        o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 9, fy(v) + 4.5, str(v), 13, 'end', MUT))
        o.append(L(x0, fy(v), 700, fy(v), 'var(--line)', 1))
    o.append(T(x0, y0 - 16, 'temperature, °C', 14, 'start', MUT))
    cols = [(280, 'full airflow', 0.15, AC, ACS), (520, 'half airflow', 0.30, NX, NXS)]
    for cx, name, rth, c, cs in cols:
        tc = 30 + 120 * rth; tj = tc + 10
        o.append(T(cx, y1 + 22, name, 14, 'middle', c, bold=True))
        o.append(T(cx, y1 + 40, f'R_th = {rth:.2f} K/W', 13, 'middle', MUT))
        for t, lab in ((30, 'air 30'), (tc, f'case {tc:g}'), (tj, f'junction {tj:g}')):
            o.append(C(cx, fy(t), 6, c))
            o.append(Tb(cx + 12, fy(t) + 5, lab + ' °C', 13, 'start', INK, bold=(t != 30)))
        o.append(L(cx, fy(30) - 6, cx, fy(tc) + 6, c, 4)); o.append(L(cx, fy(tc) - 6, cx, fy(tj) + 6, LV, 4))
        o.append(T(cx - 12, (fy(30) + fy(tc)) / 2 + 5, f'+{120 * rth:g} K', 13, 'end', c, bold=True))
        o.append(Tb(cx - 12, (fy(tc) + fy(tj)) / 2 + 5, '+10 K', 13, 'end', LV, bold=True))
    o.append(L(x0, fy(70), 700, fy(70), NX, 2, dash='6 4')); o.append(Tb(x0 + 8, fy(70) - 6, 'case limit 70 °C', 13, 'start', NX, bold=True))
    o.append(L(x0, fy(125), 700, fy(125), NX, 2, dash='6 4')); o.append(Tb(x0 + 8, fy(125) - 6, 'junction limit 125 °C', 13, 'start', NX, bold=True))
    o.append(T(410, 400, 'LRU 120 W: rise = P × R_th;  chip 5 W × R_jc 2.0 K/W = 10 K', 13, 'middle', MUT))
    return 412, ''.join(o)


FIG[6] = (f6, 'The heat path of the worked examples. With full airflow the 120 W LRU sits 18 K above the 30 °C air (case 48 °C) and the 5 W chip 10 K above that; halving the airflow '
              'doubles the rise to 36 K (case 66 °C, 4 K under its limit; junction 76 °C).',
          'A temperature scale from 20 to 130 degrees with two columns. Full airflow: air 30, case 48, junction 58 degrees. Half airflow: air 30, case 66, junction 76 degrees. '
          'Dashed lines mark the case limit at 70 and the junction limit at 125 degrees.')


# ---- 3.7 pitot-static plumbing and the worked example ----
def f7():
    o = []
    # pitot head
    o.append(P([(20, 70), (110, 70)], AC, 6)); o.append(T(20, 56, 'pitot: P_0', 14, 'start', AC, bold=True))
    o.append(arrow(10, 100, 40, 100, MUT, 1.6, 'm')); o.append(T(12, 120, 'airflow', 13, 'start', MUT))
    o.append(P([(110, 70), (200, 70)], AC, 3))
    # static port
    o.append(R(20, 180, 90, 18, PANEL, LV, 3)); o.append(T(20, 172, 'static port: P', 14, 'start', LV, bold=True))
    o.append(P([(110, 189), (200, 189)], LV, 3))
    o.append(P([(170, 189), (170, 320), (230, 320)], LV, 3)); o.append(P([(170, 254), (230, 254)], LV, 3))
    # instruments
    o.append(boxt(230, 42, 150, 64, ['ASI', 'capsule: P_0 − P'], PANEL, AC, 14, bold_first=True))
    o.append(P([(200, 70), (230, 70)], AC, 3)); o.append(P([(200, 189), (205, 189), (205, 96), (230, 96)], LV, 3))
    o.append(boxt(230, 226, 150, 56, ['altimeter', 'aneroid: P only'], PANEL, LV, 14, bold_first=True))
    o.append(boxt(230, 298, 150, 44, ['VSI'], PANEL, LV, 14, bold_first=True))
    # results
    rx = 410
    o.append(T(rx, 40, 'q = P_0 − P = 2500 Pa', 14, 'start', INK, bold=True))
    o.append(T(rx, 62, 'V = √(2 × 2500 ÷ 1.225)', 13, 'start'))
    o.append(T(rx, 82, '= 63.9 m/s = 124 kt (IAS)', 14, 'start', AC, bold=True))
    o.append(T(rx, 230, 'subscale 1013.25 hPa, outside 950 hPa', 13, 'start'))
    o.append(T(rx, 250, '63.25 hPa × 27 ft/hPa', 13, 'start'))
    o.append(T(rx, 272, '≈ 1708 ft pressure altitude', 14, 'start', LV, bold=True))
    o.append(T(rx, 140, 'pitot blocked: ASI acts like an altimeter', 13, 'start', NX))
    o.append(T(rx, 160, 'static blocked: altimeter freezes, VSI 0', 13, 'start', NX))
    return 356, ''.join(o)


FIG[7] = (f7, 'The pitot line feeds only the airspeed capsule; the static line feeds the ASI case, the altimeter and the VSI. In the worked example q = 2500 Pa gives 124 kt at '
              'sea level, and 950 hPa outside with 1013.25 hPa set gives about 1708 ft.',
          'A pitot tube facing the airflow feeds the inside of the airspeed indicator capsule. A static port feeds the airspeed indicator case, the altimeter and the vertical speed '
          'indicator. Text beside gives 2500 pascals giving 63.9 metres per second or 124 knots, and 63.25 hectopascals times 27 feet giving about 1708 feet.')


# ---- 3.8 the speed and EGT chains of the worked example ----
def f8():
    o = []
    # toothed wheel
    cx, cy, r = 60, 80, 40
    pts = []
    for i in range(30):
        a0 = 2 * math.pi * i / 30
        for a, rr in ((a0, r), (a0 + 0.06, r + 8), (a0 + 0.15, r + 8), (a0 + 0.21, r)):
            pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    pts.append(pts[0]); o.append(P(pts, AC, 1.6, fill=PANEL))
    o.append(T(cx, cy + 5, '30 teeth', 13, bold=True))
    o.append(R(112, 66, 30, 28, ACS, AC, 3)); o.append(T(127, 116, 'pickup', 13, 'middle', MUT))
    o.append(arrow(142, 80, 176, 80))
    o.append(boxt(180, 54, 150, 52, ['9000 rpm → 150 rev/s', '× 30 = 4500 Hz'], PANEL, AC, 13, bold_first=True))
    o.append(arrow(330, 80, 364, 80)); o.append(boxt(368, 58, 120, 44, ['counter'], PANEL, AC, 14))
    o.append(arrow(488, 80, 532, 80)); o.append(arrow(488, 238, 532, 160, LV, 2.5, 'l'))
    o.append(boxt(536, 70, 168, 100, ['engine display', 'N2 %', 'EGT °C'], ACS, AC, 14, bold_first=True))
    # thermocouple
    o.append(P([(30, 220), (90, 220)], NX, 3)); o.append(P([(30, 226), (90, 226)], LV, 3)); o.append(C(30, 223, 7, NX))
    o.append(T(30, 200, 'hot 700 °C', 13, 'start', NX, bold=True))
    o.append(T(30, 254, 'chromel / alumel', 13, 'start', MUT))
    o.append(arrow(92, 223, 176, 223, LV))
    o.append(boxt(180, 196, 150, 56, ['cold 25 °C: Δ = 675 °C', '41 µV × 675 = 27.7 mV'], PANEL, LV, 13, bold_first=True))
    o.append(arrow(330, 224, 364, 224, LV))
    o.append(boxt(368, 200, 120, 48, ['amplifier ×100', '→ 2.77 V → ADC'], PANEL, LV, 13))
    o.append(T(260, 296, 'cold-junction compensation adds back S × T_cold', 13, 'middle', MUT))
    return 312, ''.join(o)


FIG[8] = (f8, 'The worked example\'s two chains. Top: a pickup beside the 30-tooth wheel at 9000 rpm gives 4500 pulses per second for the counter. Bottom: the type K thermocouple '
              'sees 700 °C against a 25 °C cold junction and gives 27.7 mV, which the ×100 amplifier turns into 2.77 V for the ADC.',
          'Top: a toothed wheel with 30 teeth and a magnetic pickup, then 9000 rpm to 150 revolutions per second times 30 equals 4500 hertz, a counter and the engine display. '
          'Bottom: a thermocouple with a hot junction at 700 degrees, cold junction 25 degrees, 27.7 millivolts, an amplifier of gain 100 giving 2.77 volts to an ADC and the display.')


# ---- 3.9 the vibrating-contact regulator and its field current ----
def f9():
    o = []
    # circuit
    o.append(T(20, 24, 'generator output 28 V', 14, 'start', INK, bold=True))
    o.append(L(40, 40, 40, 260, AC, 2.4)); o.append(L(250, 40, 250, 260, AC, 2.4))
    o.append(T(34, 274, '+28 V', 13, 'middle', INK, bold=True)); o.append(T(250, 274, '0 V', 13, 'middle', INK, bold=True))
    # field winding with contact + resistor in series
    o.append(L(40, 90, 80, 90, AC, 2.2))
    o.append(C(84, 90, 4, INK)); o.append(L(88, 90, 124, 78, INK, 2.4)); o.append(C(128, 90, 4, INK))
    o.append(T(106, 70, 'contact', 13, 'middle', NX, bold=True))
    o.append(P([(80, 90), (80, 124), (96, 124)], AC, 2.2)); o.append(resistor_h(96, 124, 50)); o.append(P([(146, 124), (132, 124), (132, 90)], AC, 2.2))
    o.append(T(121, 154, '20 Ω', 13, 'middle', INK, bold=True))
    o.append(L(132, 90, 170, 90, AC, 2.2))
    for i in range(4):
        o.append(f'<path d="M{170 + i * 14:.1f},90 a7,7 0 0 1 14,0" style="fill:none;stroke:var(--accent);stroke-width:2.2"/>')
    o.append(L(226, 90, 250, 90, AC, 2.2)); o.append(T(198, 112, 'field 10 Ω', 13, 'middle', INK, bold=True))
    # voltage coil
    o.append(L(40, 200, 110, 200, LV, 2)); o.append(R(110, 188, 90, 24, LVS, LV, 4)); o.append(T(155, 205, 'voltage coil', 13, bold=True))
    o.append(L(200, 200, 250, 200, LV, 2)); o.append(arrow(155, 186, 112, 100, LV, 1.6, 'l'))
    o.append(T(145, 304, 'coil opens the contact above the setting', 13, 'middle', MUT))
    # waveform
    x0, x1, y0, y1 = 340, 700, 40, 250
    fx, fy = lin(0, 3, x0, x1), lin(0, 3, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3], [0, 1, 2, 3], fx, fy, 'time, cycles', 'field current, A'))
    D = 0.304; pts = []
    for c in range(3):
        pts += [(fx(c), fy(2.8)), (fx(c + D), fy(2.8)), (fx(c + D), fy(0.933)), (fx(c + 1), fy(0.933))]
    o.append(P(pts, AC, 2.6))
    o.append(L(x0, fy(1.5), x1, fy(1.5), LV, 2.2, dash='6 4'))
    o.append(Tb(x1 - 4, fy(1.5) - 8, 'average 1.50 A', 13, 'end', LV, bold=True))
    o.append(Tb(fx(0.33) + 6, fy(2.8) - 8, '2.80 A closed', 13, 'start', AC, bold=True))
    o.append(Tb(fx(1.62), fy(0.933) + 22, '0.933 A open', 13, 'middle', AC, bold=True))
    o.append(T(520, 316, 'D = (1.50 − 0.933) ÷ (2.80 − 0.933) = 30.4 %', 14, 'middle', INK, bold=True))
    return 330, ''.join(o)


FIG[9] = (f9, 'Left: the vibrating-contact regulator: the voltage coil across the output opens the contact above the setting, putting 20 Ω in series with the 10 Ω field. '
              'Right: the worked example\'s field current switches between 2.80 A and 0.933 A; closed 30.4 % of the time, it averages 1.50 A.',
          'Circuit: a 28 volt supply, a field winding of 10 ohms in series with a contact that has a 20 ohm resistor across it, and a voltage coil across the supply that opens the '
          'contact. Graph: field current switching between 2.8 amps for 30.4 per cent of each cycle and 0.933 amps for the rest, with a dashed average line at 1.5 amps.')


# ---- 3.10 breaker and wire time-current curves ----
def f10():
    o = []
    x0, x1, y0, y1 = 80, 680, 40, 300
    fx = lin(20, 100, x0, x1)
    ly = lambda t: y1 - (math.log10(t) + 1) / 4 * (y1 - y0)   # 0.1 s .. 1000 s
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (20, 40, 60, 80, 100):
        o.append(L(fx(v), y1, fx(v), y1 + 5, L2, 1.5)); o.append(T(fx(v), y1 + 20, str(v), 13, fill=MUT))
    for t, lab in ((0.1, '0.1'), (1, '1'), (10, '10'), (100, '100'), (1000, '1000')):
        o.append(L(x0 - 5, ly(t), x0, ly(t), L2, 1.5)); o.append(L(x0, ly(t), x1, ly(t), 'var(--line)', 1)); o.append(T(x0 - 9, ly(t) + 4.5, lab, 13, 'end', MUT))
    o.append(T((x0 + x1) / 2, y1 + 42, 'current, A', 14, fill=MUT)); o.append(T(x0, y0 - 14, 'time to trip or to damage, s (log scale)', 14, 'start', MUT))
    br = lambda I: 6000 / (I * I - 400); wi = lambda I: 30000 / (I * I - 625)
    def curve(f, a, b, c, w=3):
        pts = []
        for i in range(301):
            I = a + (b - a) * i / 300
            t = f(I)
            if 0.1 <= t <= 1000: pts.append((fx(I), ly(t)))
        return P(pts, c, w)
    o.append(curve(br, 20.05, 100, AC)); o.append(curve(wi, 25.05, 100, NX))
    o.append(Tb(fx(56), ly(br(56)) + 30, '20 A breaker', 14, 'start', AC, bold=True))
    o.append(Tb(fx(32) + 10, ly(wi(32)) - 4, 'wire damage (25 A wire)', 14, 'start', NX, bold=True))
    for I in (40, 80):
        o.append(L(fx(I), ly(wi(I)), fx(I), ly(br(I)), LV, 1.8, dash='5 4'))
        o.append(C(fx(I), ly(br(I)), 6, AC)); o.append(C(fx(I), ly(wi(I)), 6, NX))
    o.append(Tb(fx(40) - 10, ly(br(40)) + 20, '40 A: 5.0 s', 13, 'end', AC, bold=True))
    o.append(Tb(fx(40) + 10, ly(wi(40)) - 10, '30.8 s', 13, 'start', NX, bold=True))
    o.append(Tb(fx(80) - 10, ly(br(80)) + 20, '80 A: 1.0 s', 13, 'end', AC, bold=True))
    o.append(Tb(fx(80) + 10, ly(wi(80)) - 10, '5.2 s', 13, 'start', NX, bold=True))
    o.append(T(380, 362, 'breaker below the wire at every current: the breaker opens first', 13, 'middle', MUT))
    return 374, ''.join(o)


FIG[10] = (f10, 'A 20 A breaker on a wire rated 25 A, on a log time scale. The breaker curve lies below the wire damage curve at every current: at 40 A it trips in 5.0 s against '
                '30.8 s for the wire, at 80 A in 1.0 s against 5.2 s. Near 20 A it never trips, so normal load does not open it.',
           'Graph of time on a logarithmic scale from 0.1 to 1000 seconds against current from 20 to 100 amps. The breaker curve rises steeply near 20 amps and stays below the '
           'wire damage curve, which rises near 25 amps. Marked points: at 40 amps 5 seconds and 30.8 seconds, at 80 amps 1 second and 5.2 seconds.')


# ---- 3.11 split-parallel layout and the droop sharing of the worked example ----
def diode(x, y, c=LV):
    """small diode pointing down at (x, y)"""
    return P([(x - 8, y - 6), (x + 8, y - 6), (x, y + 6), (x - 8, y - 6)], c, 2, fill=c) + L(x - 8, y + 6, x + 8, y + 6, c, 2.4)


def f11():
    o = []
    o.append(boxt(20, 16, 90, 40, ['GEN 1'], ACS, AC, 14, bold_first=True)); o.append(boxt(220, 16, 90, 40, ['GEN 2'], ACS, AC, 14, bold_first=True))
    o.append(L(65, 56, 65, 82, AC, 2.4)); o.append(L(265, 56, 265, 82, AC, 2.4))
    o.append(boxt(30, 82, 70, 30, ['GCB 1'], PANEL, AC, 13)); o.append(boxt(230, 82, 70, 30, ['GCB 2'], PANEL, AC, 13))
    o.append(L(65, 112, 65, 136, AC, 2.4)); o.append(L(265, 112, 265, 136, AC, 2.4))
    o.append(R(20, 136, 110, 16, ACS, AC, 3)); o.append(R(220, 136, 110, 16, ACS, AC, 3))
    o.append(T(75, 174, 'BUS 1', 13, bold=True)); o.append(T(275, 174, 'BUS 2', 13, bold=True))
    o.append(L(130, 144, 150, 144, NX, 2.4)); o.append(L(200, 144, 220, 144, NX, 2.4))
    o.append(L(152, 144, 192, 134, NX, 2.4)); o.append(C(150, 144, 3.5, NX)); o.append(C(200, 144, 3.5, NX))
    o.append(T(175, 124, 'BTB open', 13, 'middle', NX, bold=True))
    o.append(P([(100, 152), (100, 196)], LV, 2.2)); o.append(diode(100, 204)); o.append(P([(100, 210), (100, 232)], LV, 2.2))
    o.append(P([(250, 152), (250, 196)], LV, 2.2)); o.append(diode(250, 204)); o.append(P([(250, 210), (250, 232)], LV, 2.2))
    o.append(R(80, 232, 190, 16, LVS, LV, 3)); o.append(T(150, 272, 'ESSENTIAL BUS', 13, 'start', LV, bold=True))
    o.append(T(150, 292, 'diodes feed it from either side', 13, 'start', MUT))
    o.append(boxt(20, 300, 90, 34, ['battery'], PANEL, LV, 13)); o.append(P([(110, 317), (130, 317), (130, 248)], LV, 2, dash='5 4'))
    # droop lines
    x0, x1, y0, y1 = 410, 690, 40, 280
    fx, fy = lin(0, 300, x0, x1), lin(27.0, 28.6, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 100, 200, 300], [27.0, 27.4, 27.8, 28.2, 28.6], fx, fy, 'generator current, A', 'terminal voltage, V', yfmt=lambda v: f'{v:.1f}'))
    o.append(P([(fx(0), fy(28.5)), (fx(300), fy(28.5 - 0.004 * 300))], AC, 3))
    o.append(P([(fx(0), fy(28.5)), (fx(250), fy(28.5 - 0.006 * 250))], NX, 3))
    o.append(L(x0, fy(27.78), fx(180), fy(27.78), LV, 1.8, dash='5 4'))
    o.append(L(fx(120), fy(27.78), fx(120), y1, LV, 1.4, dash='4 4')); o.append(L(fx(180), fy(27.78), fx(180), y1, LV, 1.4, dash='4 4'))
    o.append(C(fx(120), fy(27.78), 6, NX)); o.append(C(fx(180), fy(27.78), 6, AC))
    o.append(Tb(x1 - 4, fy(28.35), 'GEN 1: 0.4 V per 100 A', 13, 'end', AC, bold=True))
    o.append(Tb(x0 + 8, fy(27.15), 'GEN 2: 0.6 V per 100 A', 13, 'start', NX, bold=True))
    o.append(Tb(x0 + 6, fy(27.78) - 8, 'bus 27.78 V', 13, 'start', LV, bold=True))
    o.append(T(fx(150), 336, '120 A + 180 A = 300 A', 14, 'middle', INK, bold=True))
    return 348, ''.join(o)


FIG[11] = (f11, 'Left: split-parallel layout. Each generator feeds its own bus through its GCB; the bus tie breaker (BTB) stays open in normal flight, and the essential bus is fed '
                'through diodes from either side, with the battery as standby. Right: the worked example\'s droop lines meet the common 27.78 V at 180 A (GEN 1) and 120 A (GEN 2).',
           'Left: generator 1 and generator 2 each feed a bus through a GCB, an open bus tie breaker between the buses, two diodes from the buses into an essential bus, and a battery '
           'connected to the essential bus by a dashed line. Right: graph of terminal voltage against current with two lines from 28.5 volts, crossing the 27.78 volt line at 180 and 120 amps.')


# ---- 3.12 the two architectures and the worked example's currents ----
def f12():
    o = []
    for x, title, c, cs in ((20, 'A320: 115 V, 400 Hz fixed', AC, ACS), (372, 'B787: 235 V, 360 to 800 Hz', NX, NXS)):
        o.append(T(x + 164, 24, title, 14, 'middle', c, bold=True))
    # A320
    o.append(boxt(20, 40, 150, 48, ['2 IDGs', '90 kVA each'], ACS, AC, 13, bold_first=True))
    o.append(boxt(190, 40, 140, 48, ['APU generator', '90 kVA'], PANEL, AC, 13, bold_first=True))
    o.append(arrow(95, 88, 95, 112)); o.append(arrow(260, 88, 260, 112))
    o.append(R(20, 114, 310, 16, ACS, AC, 3)); o.append(T(175, 148, 'AC BUS 1 · AC BUS 2 (115 V AC)', 13, 'middle', INK, bold=True))
    o.append(arrow(95, 156, 95, 178)); o.append(boxt(20, 180, 150, 46, ['TR 1, TR 2, ESS TR', '28 V DC'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(190, 180, 140, 46, ['RAT → hydraulic', 'emergency gen 5 kVA'], PANEL, LV, 13))
    o.append(T(175, 252, 'NiCd batteries, static inverter', 13, 'middle', MUT))
    # B787
    o.append(boxt(372, 40, 160, 48, ['4 VFSGs', '250 kVA each'], NXS, NX, 13, bold_first=True))
    o.append(boxt(548, 40, 152, 48, ['2 APU SGs', '225 kVA each'], PANEL, NX, 13, bold_first=True))
    o.append(arrow(452, 88, 452, 112, NX, 2.5, 'x')); o.append(arrow(624, 88, 624, 112, NX, 2.5, 'x'))
    o.append(R(372, 114, 328, 16, NXS, NX, 3)); o.append(T(536, 148, '235 V AC buses, variable frequency', 13, 'middle', INK, bold=True))
    for i, (a, b) in enumerate((('ATRU', '±270 V DC'), ('ATU', '115 V AC'), ('TRU', '28 V DC'))):
        x = 372 + i * 112
        o.append(arrow(x + 50, 156, x + 50, 178, NX, 2, 'x'))
        o.append(boxt(x, 180, 104, 46, [a, b], PANEL, NX, 13, bold_first=True))
    o.append(T(536, 252, 'Li-ion batteries, RAT, SSPCs', 13, 'middle', MUT))
    # worked example
    o.append(T(20, 290, 'Worked example: 100 kW at unity power factor, same cable', 14, 'start', INK, bold=True))
    x0, W = 190, 380
    fx = lin(0, 300, x0, x0 + W)
    o.append(T(20, 322, '115 V', 14, 'start', AC, bold=True)); o.append(R(x0, 306, fx(289.9) - x0, 24, ACS, AC, 3)); o.append(T(fx(289.9) + 8, 324, '289.9 A', 13, 'start', AC, bold=True))
    o.append(T(20, 356, '235 V', 14, 'start', NX, bold=True)); o.append(R(x0, 340, fx(141.8) - x0, 24, NXS, NX, 3)); o.append(T(fx(141.8) + 8, 358, '141.8 A', 13, 'start', NX, bold=True))
    o.append(T(80, 322, 'I = P ÷ (3V)', 13, 'start', MUT))
    o.append(T(360, 392, 'copper loss ratio (289.9 ÷ 141.8)² = (235 ÷ 115)² = 4.18', 14, 'middle', INK, bold=True))
    return 404, ''.join(o)


FIG[12] = (f12, 'The two architectures side by side: the A320 makes 115 V 400 Hz from two 90 kVA IDGs and 28 V DC from transformer rectifiers; the B787 makes 235 V variable-frequency '
                'AC from four 250 kVA starter-generators and converts it to ±270 V DC, 115 V AC and 28 V DC. Below: the worked example\'s 100 kW load draws 289.9 A at 115 V but 141.8 A '
                'at 235 V, so the copper loss falls by 4.18.',
           'Left column for the A320: two IDGs of 90 kVA and an APU generator of 90 kVA feed two 115 volt AC buses, then transformer rectifiers give 28 volts DC; a RAT drives a '
           '5 kVA hydraulic emergency generator. Right column for the B787: four 250 kVA starter-generators and two 225 kVA APU starter-generators feed 235 volt variable-frequency '
           'buses, then ATRUs give plus and minus 270 volts DC, ATUs 115 volts AC and TRUs 28 volts DC. Below, two bars: 289.9 amps at 115 volts and 141.8 amps at 235 volts.')


# ---- 3.13 the capacitance probe of worked example 1 ----
def f13():
    o = []
    # probe: two tall plates, fuel at half height
    X0, Y0, H = 60, 40, 240
    o.append(R(X0 - 30, Y0 - 10, 200, H + 20, PANEL, L2, 6))
    o.append(R(X0 - 30, Y0 + H / 2, 200, H / 2 + 10, NXS, NX, 0, sw=0))
    o.append(L(X0 - 30, Y0 + H / 2, X0 + 170, Y0 + H / 2, NX, 2, dash='6 4'))
    o.append(R(X0 + 6, Y0, 10, H, ACS, AC, 2)); o.append(R(X0 + 124, Y0, 10, H, ACS, AC, 2))
    o.append(T(X0 + 70, Y0 + 50, 'air', 14, bold=True)); o.append(T(X0 + 70, Y0 + 66, 'ε_r = 1.0', 13, fill=MUT))
    o.append(T(X0 + 70, Y0 + 180, 'fuel', 14, bold=True)); o.append(T(X0 + 70, Y0 + 196, 'ε_r = 2.0', 13, fill=MUT))
    o.append(T(X0 + 70, Y0 + H + 34, 'A = 0.02 m², d = 5 mm', 13, fill=MUT))
    o.append(T(X0 + 70, Y0 + H + 52, 'half full: 53.1 pF', 14, 'middle', LV, bold=True))
    # C against height
    x0, x1, y0, y1 = 340, 690, 40, 280
    fx, fy = lin(0, 100, x0, x1), lin(30, 75, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 25, 50, 75, 100], [30, 40, 50, 60, 70], fx, fy, 'fuel height, % of plate height', 'capacitance, pF'))
    o.append(P([(fx(0), fy(35.416)), (fx(100), fy(70.832))], AC, 3))
    for h, c, lab, dx, anc in ((0, 35.416, 'empty 35.4 pF', 10, 'start'), (50, 53.124, 'half 53.1 pF', 10, 'start'), (100, 70.832, 'full 70.8 pF', -10, 'end')):
        o.append(C(fx(h), fy(c), 6, LV))
        o.append(Tb(fx(h) + dx, fy(c) + (20 if h == 0 else -12), lab, 13, anc, LV, bold=True))
    o.append(T(515, 342, 'C = C_empty + (C_full − C_empty) × h ÷ H: +17.7 pF per half', 13, 'middle', MUT))
    return 356, ''.join(o)


FIG[13] = (f13, 'Worked example 1\'s probe: fuel (ε<sub>r</sub> 2.0) rising between plates 5 mm apart replaces air (ε<sub>r</sub> 1.0), so the capacitance climbs in a straight line with fuel height, '
                'from 35.4 pF empty through 53.1 pF at half height to 70.8 pF full.',
           'Left: two vertical plates in a tank, air above and fuel filling the lower half. Right: graph of capacitance against fuel height, a straight line from 35.4 picofarads '
           'at empty through 53.1 at half height to 70.8 at full.')


spec = make_spec(FIG)
