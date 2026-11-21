"""Claude's hand-drawn figures for me-ic-u1 (Automotive / IC Engines: engine fundamentals, components and cycles), one per chapter,
drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables only."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


# ---- 1.1 classification of IC engines, the scooter of the worked example picked out ----
def f1():
    o = []
    cols = [('Ignition', ['SI', 'CI'], 0), ('Strokes', ['four-stroke', 'two-stroke'], 1), ('Cycle', ['Otto', 'Diesel', 'dual'], 0),
            ('Fuel', ['petrol', 'diesel', 'CNG, LPG'], 0), ('Cooling', ['air', 'water'], 0),
            ('Air supply', ['natural', 'supercharged', 'turbocharged'], 0), ('Cylinders', ['single', 'inline', 'V', 'opposed'], 0)]
    o.append(boxt(290, 14, 140, 40, ['IC engine'], ACS, AC, 15, bold_first=True))
    w, gap = 94, 7
    x0 = (720 - (7 * w + 6 * gap)) / 2
    o.append(L(360, 54, 360, 74, AC, 2))
    o.append(L(x0 + w / 2, 74, x0 + 6 * (w + gap) + w / 2, 74, AC, 2))
    for i, (head, leaves, pick) in enumerate(cols):
        x = x0 + i * (w + gap); cx = x + w / 2
        o.append(L(cx, 74, cx, 92, AC, 2))
        o.append(boxt(x, 92, w, 34, [head], PANEL, AC, 14, bold_first=True))
        o.append(L(cx, 126, cx, 140 + 40 * (len(leaves) - 1), L2, 1.5))
        for j, s in enumerate(leaves):
            y = 140 + 40 * j
            hit = j == pick
            o.append(boxt(x + 4, y, w - 8, 30, [s], ACS if hit else PANEL, AC if hit else L2, 13, bold_first=hit))
    o.append(R(150, 318, 26, 20, ACS, AC, 4))
    o.append(T(186, 333, 'the scooter of the worked example: one label from every list', 13, 'start', MUT))
    return 352, ''.join(o)


FIG[1] = (f1, 'Seven independent ways to classify an IC engine. The shaded boxes are the worked example’s scooter: SI, two-stroke, Otto cycle, petrol, '
              'air-cooled, naturally aspirated, single cylinder. Any box can be combined with any box in another column.',
          'A tree from IC engine to seven classification bases: ignition, strokes, cycle, fuel, cooling, air supply and cylinders, each with its types. '
          'SI, two-stroke, Otto, petrol, air, natural and single are highlighted for the scooter.')


# ---- 1.2 one cylinder of the worked example: bore 80, stroke 90, Vc 62.8 cm3 ----
def f2():
    o = []
    s = 1.6  # px per mm
    cx = 232; d = 80 * s; xl, xr = cx - d / 2, cx + d / 2
    ytop = 76; tdc = ytop + 20; bdc = tdc + 90 * s   # 20 px clearance space
    # block walls and coolant jacket
    o.append(R(xl - 34, ytop, 24, bdc + 64 - ytop, NXS, NX, 4, 1.5))
    o.append(R(xr + 10, ytop, 24, bdc + 64 - ytop, NXS, NX, 4, 1.5))
    o.append(L(xl, ytop, xl, bdc + 64, INK, 3)); o.append(L(xr, ytop, xr, bdc + 64, INK, 3))
    # head with valves and plug
    o.append(R(xl - 34, ytop - 38, d + 68, 38, PANEL, INK, 4, 2))
    for vx in (cx - 34, cx + 34):
        o.append(L(vx, ytop - 52, vx, ytop - 4, INK, 3))
        o.append(f'<path d="M{vx - 15:.1f},{ytop:.1f} L{vx + 15:.1f},{ytop:.1f} L{vx + 4:.1f},{ytop - 7:.1f} L{vx - 4:.1f},{ytop - 7:.1f} Z" style="fill:{PANEL};stroke:{INK};stroke-width:2"/>')
    o.append(R(cx - 6, ytop - 58, 12, 52, LVS, LV, 3, 2))
    # clearance and swept volume
    o.append(R(xl + 2, ytop + 1, d - 4, tdc - ytop - 1, LVS, LVS, 0, 0))
    o.append(R(xl + 2, tdc, d - 4, bdc - tdc, ACS, ACS, 0, 0))
    o.append(L(xl - 50, tdc, xr + 50, tdc, MUT, 1.5, dash='6 4')); o.append(L(xl - 50, bdc, xr + 50, bdc, MUT, 1.5, dash='6 4'))
    o.append(T(xl - 48, tdc - 5, 'TDC', 13, 'start', MUT, bold=True)); o.append(T(xl - 48, bdc - 5, 'BDC', 13, 'start', MUT, bold=True))
    # stroke dimension
    o.append(L(xl - 70, tdc + 3, xl - 70, bdc - 3, AC, 2, arrow='n')); o.append(L(xl - 70, bdc - 3, xl - 70, tdc + 3, AC, 2, arrow='n'))
    o.append(T(xl - 78, (tdc + bdc) / 2 - 4, 'stroke', 13, 'end', AC, bold=True)); o.append(T(xl - 78, (tdc + bdc) / 2 + 13, 'L = 90 mm', 13, 'end', AC, bold=True))
    # bore dimension
    yb = tdc + 60
    o.append(L(xl + 4, yb, xr - 4, yb, AC, 2, arrow='n')); o.append(L(xr - 4, yb, xl + 4, yb, AC, 2, arrow='n'))
    o.append(Tb(cx, yb - 8, 'bore d = 80 mm', 13, 'middle', AC, True))
    o.append(T(cx, tdc + 110, 'V<tspan baseline-shift="sub" font-size="11">s</tspan> = 452.4 cm³', 14, 'middle', AC, True))
    # piston at BDC
    ph = 56
    o.append(R(xl + 3, bdc, d - 6, ph, PANEL, INK, 4, 2))
    for k in range(3): o.append(L(xl + 3, bdc + 8 + 7 * k, xr - 3, bdc + 8 + 7 * k, INK, 1.2))
    pin = bdc + 36
    o.append(C(cx, pin, 7, PANEL)); o.append(f'<circle cx="{cx}" cy="{pin:.1f}" r="7" style="fill:none;stroke:{INK};stroke-width:2"/>')
    # connecting rod and crank (rod drawn shorter than scale)
    a = 45 * s
    cpin = pin + 190; ccy = cpin - a   # crank pin at the bottom of the circle at BDC
    o.append(f'<circle cx="{cx}" cy="{ccy:.1f}" r="{a:.1f}" style="fill:none;stroke:{L2};stroke-width:1.5;stroke-dasharray:5 4"/>')
    o.append(L(cx, pin, cx, cpin, INK, 9)); o.append(L(cx, pin, cx, cpin, PANEL, 5))
    o.append(L(cx, ccy, cx, cpin, LV, 4))
    o.append(C(cx, ccy, 6, LV)); o.append(C(cx, cpin, 6, INK))
    o.append(T(cx + 10, ccy + (cpin - ccy) / 2 + 4, 'a = 45 mm', 13, 'start', LV, True))
    # labels on the right
    X = 440
    def lab(y, text, px, py, col=INK):
        o.append(L(px, py, X - 6, y - 4, L2, 1.2)); o.append(T(X, y, text, 13, 'start', col))
    lab(ytop - 46, 'spark plug', cx + 6, ytop - 46)
    lab(ytop - 22, 'inlet and exhaust valves', cx + 40, ytop - 30)
    lab(ytop - 2, 'cylinder head', xr + 34, ytop - 16)
    lab(tdc - 6, 'clearance volume V<tspan baseline-shift="sub" font-size="11">c</tspan> = 62.8 cm³', xr - 6, tdc - 10, LV)
    lab(tdc + 34, 'coolant jacket in the block', xr + 30, tdc + 30, NX)
    lab(bdc + 12, 'piston (at BDC) and rings', xr - 6, bdc + 15)
    lab(pin + 4, 'gudgeon pin', cx + 8, pin)
    lab(pin + 60, 'connecting rod', cx + 6, pin + 64)
    lab(ccy + 4, 'crankshaft centre', cx + 8, ccy)
    lab(cpin + 4, 'crank pin', cx + 8, cpin)
    o.append(T(X, cpin + 40, 'r = (452.4 + 62.8)/62.8 = 8.20', 14, 'start', AC, True))
    o.append(T(xl - 34, cpin + 40, 'connecting rod shortened to fit', 13, 'start', MUT))
    return cpin + 56, ''.join(o)


FIG[2] = (f2, 'One cylinder of the worked example, piston at BDC. The piston sweeps 452.4 cm³ between TDC and BDC (stroke 90 mm, twice the 45 mm crank '
              'radius); the 62.8 cm³ clearance volume stays above it at TDC, so r = 515.2/62.8 = 8.20.',
          'Section of one cylinder with head, two valves and a spark plug, coolant jacket, piston at bottom dead centre with rings and gudgeon pin, '
          'connecting rod and crank. Dimension lines show bore 80 millimetres and stroke 90 millimetres; the clearance volume is 62.8 and the swept volume 452.4 cubic centimetres.')


# ---- 1.3 crankcase-scavenged two-stroke, piston near BDC ----
def f3():
    o = []
    xl, xr = 220, 360; cx = (xl + xr) / 2
    # head and plug
    o.append(R(xl - 10, 40, xr - xl + 20, 30, PANEL, INK, 4, 2))
    o.append(R(cx - 6, 22, 12, 44, LVS, LV, 3, 2)); o.append(T(xr + 20, 46, 'spark plug', 13, 'start', MUT))
    o.append(L(cx + 8, 40, xr + 14, 42, L2, 1.2))
    # cylinder walls with the two port gaps
    o.append(L(xl, 70, xl, 165, INK, 3)); o.append(L(xl, 195, xl, 300, INK, 3))
    o.append(L(xr, 70, xr, 150, INK, 3)); o.append(L(xr, 185, xr, 300, INK, 3))
    # exhaust duct
    o.append(L(xr, 150, xr + 60, 150, INK, 2.5)); o.append(L(xr, 185, xr + 60, 185, INK, 2.5))
    o.append(L(xr - 30, 168, xr + 74, 168, LV, 3, arrow='l'))
    o.append(T(xr + 84, 163, 'exhaust port', 13, 'start', LV, True)); o.append(T(xr + 84, 180, 'opens first, 60° before BDC', 13, 'start', MUT))
    # transfer passage, crankcase
    o.append(f'<path d="M{xl},165 L{xl - 40},165 L{xl - 40},420 Q{xl - 40},445 {xl - 15},445 L{xr + 15},445 Q{xr + 40},445 {xr + 40},420 L{xr + 40},300 L{xr},300" style="fill:none;stroke:{INK};stroke-width:2.5"/>')
    o.append(f'<path d="M{xl - 37},300 L{xr + 37},300 L{xr + 37},420 Q{xr + 37},442 {xr + 15},442 L{xl - 15},442 Q{xl - 37},442 {xl - 37},420 Z" style="fill:{NXS};stroke:none"/>')
    o.append(f'<path d="M{xl - 20},310 L{xl - 20},180 L{xl + 10},180 Q{cx},150 {cx + 30},92" style="fill:none;stroke:{AC};stroke-width:3" marker-end="url(#ar-UID-n)"/>')
    o.append(T(xl - 50, 172, 'transfer port', 13, 'end', AC, True)); o.append(T(xl - 50, 189, '45° before BDC', 13, 'end', MUT))
    o.append(T(xl - 50, 240, 'fresh charge', 13, 'end', AC)); o.append(T(xl - 50, 257, 'from the crankcase', 13, 'end', AC))
    o.append(T(xl - 50, 274, 'sweeps the cylinder', 13, 'end', AC))
    # piston near BDC
    crown = 205
    o.append(R(xl + 3, crown, xr - xl - 6, 70, PANEL, INK, 4, 2))
    o.append(L(xl + 3, crown + 8, xr - 3, crown + 8, INK, 1.2)); o.append(L(xl + 3, crown + 15, xr - 3, crown + 15, INK, 1.2))
    o.append(T(xl + 36, crown + 48, 'piston', 14, 'middle', INK, True))
    # crank
    ccy = 382
    o.append(f'<circle cx="{cx}" cy="{ccy}" r="32" style="fill:none;stroke:{L2};stroke-width:1.5;stroke-dasharray:5 4"/>')
    o.append(L(cx, crown + 40, cx, ccy + 32, INK, 6)); o.append(C(cx, ccy, 6, LV)); o.append(C(cx, ccy + 32, 6, INK))
    o.append(T(xl - 22, 400, 'crankcase', 13, 'start', NX, True)); o.append(T(xl - 22, 417, '(the pump)', 13, 'start', NX))
    # inlet port into the crankcase
    o.append(L(xr + 40, 335, xr + 90, 335, INK, 2.5)); o.append(L(xr + 40, 365, xr + 90, 365, INK, 2.5))
    o.append(L(xr + 90, 350, xr + 46, 350, NX, 3, arrow='x'))
    o.append(T(xr + 100, 346, 'inlet port into the crankcase:', 13, 'start', NX, True)); o.append(T(xr + 100, 363, 'open near TDC, covered now', 13, 'start', MUT))
    o.append(boxt(xr + 100, 220, 250, 74, ['at 3000 rev/min:', 'four-stroke: power every 40 ms', 'two-stroke: power every 20 ms'], ACS, AC, 13, bold_first=True))
    return 462, ''.join(o)


FIG[3] = (f3, 'A crankcase-scavenged two-stroke with the piston near BDC. The exhaust port has opened and the burnt gas is leaving; the transfer port has '
              'just opened and the charge compressed in the crankcase flows up and sweeps the cylinder. Every revolution has a power stroke, every '
              '20 ms at 3000 rev/min.',
          'Section of a two-stroke engine: cylinder with spark plug, exhaust port on the right, transfer passage on the left from the crankcase, '
          'piston near bottom dead centre, crankcase with crank, and an inlet port into the crankcase. Arrows show fresh charge looping up and exhaust leaving.')


# ---- 1.4 end-of-compression temperature against compression ratio ----
def f4():
    o = []
    x0, x1, y0, y1 = 90, 680, 40, 360
    fx = lin(4, 24, x0, x1); fy = lin(400, 1100, y1, y0)
    o.append(R(fx(8), y0, fx(12) - fx(8), y1 - y0, NXS, NXS, 0, 0)); o.append(R(fx(16), y0, fx(22) - fx(16), y1 - y0, LVS, LVS, 0, 0))
    o.append(axes(x0, x1, y0, y1, [4, 8, 12, 16, 20, 24], [400, 500, 600, 700, 800, 900, 1000, 1100], fx, fy, 'compression ratio r', 'T₂ (K)'))
    o.append(T((fx(8) + fx(12)) / 2, y1 - 12, 'SI range', 13, 'middle', NX, True)); o.append(T((fx(16) + fx(22)) / 2, y1 - 12, 'CI range', 13, 'middle', LV, True))
    pts = [(fx(r / 2), fy(300 * (r / 2) ** 0.4)) for r in range(8, 49)]
    o.append(P(pts, AC, 3)); o.append(T(fx(22.5), fy(300 * 22.5 ** 0.4) - 12, 'T₂ = 300 r⁰·⁴', 13, 'end', AC, True))
    o.append(L(x0, fy(523), x1, fy(523), MUT, 1.5, dash='6 4'))
    o.append(T(fx(13), fy(523) + 20, 'diesel self-ignition in still air, about 520 K', 13, 'middle', MUT))
    for r, t, s, dy in ((9, 722.5, 'r = 9: 722 K, 21.7 bar', 26), (18, 953.3, 'r = 18: 953 K, 57.2 bar', 30)):
        o.append(C(fx(r), fy(t), 6.5, AC))
        o.append(T(fx(r) + 10, fy(t) + dy, s, 13, 'start', INK, True))
    return 410, ''.join(o)


FIG[4] = (f4, 'Ideal end-of-compression temperature from 300 K, T₂ = 300 r⁰·⁴. The worked example’s SI engine (r = 9) reaches 722 K and its CI engine '
              '(r = 18) 953 K; both lie above diesel’s self-ignition temperature, but only the CI air is hot and dense enough to ignite the spray within a millisecond.',
          'Plot of end-of-compression temperature against compression ratio from 4 to 24. A rising curve passes 722 kelvin at ratio 9 in the shaded SI range '
          'and 953 kelvin at ratio 18 in the shaded CI range. A dashed line at 520 kelvin marks diesel self-ignition.')


# ---- 1.5 valve timing circle (example 1) and port timing circle (example 2) ----
def _pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.sin(a), cy - r * math.cos(a)


def _arc(cx, cy, r, d0, d1, c, w=7, arrow=None):
    x0, y0 = _pt(cx, cy, r, d0); x1, y1 = _pt(cx, cy, r, d1)
    large = 1 if (d1 - d0) % 360 > 180 or d1 - d0 >= 360 else 0
    m = f' marker-end="url(#ar-UID-{arrow})"' if arrow else ''
    return f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f}" style="fill:none;stroke:{c};stroke-width:{w};stroke-linecap:butt"{m}/>'


def _circle(o, cx, cy, title):
    o.append(f'<circle cx="{cx}" cy="{cy}" r="72" style="fill:none;stroke:{L2};stroke-width:1.5"/>')
    o.append(L(cx, cy - 140, cx, cy + 140, L2, 1.2, dash='4 4'))
    o.append(T(cx, cy - 146, 'TDC', 14, 'middle', INK, True)); o.append(T(cx, cy + 158, 'BDC', 14, 'middle', INK, True))
    o.append(_arc(cx, cy, 50, 30, 120, MUT, 2, 'm')); o.append(T(cx, cy + 5, 'crank turns', 13, 'middle', MUT)); o.append(T(cx, cy + 21, 'clockwise', 13, 'middle', MUT))
    o.append(T(cx, 22, title, 14, 'middle', INK, True))


def f5():
    o = []
    cx, cy = 178, 205
    _circle(o, cx, cy, 'Four-stroke valve timing')
    o.append(_arc(cx, cy, 96, -10, 220, AC, 8))     # inlet open
    o.append(_arc(cx, cy, 120, 135, 370, LV, 8))     # exhaust open
    o.append(Tb(*_pt(cx, cy, 96, 95), 'inlet 230°', 13, 'middle', AC, True))
    o.append(Tb(*_pt(cx, cy, 120, 262), 'exhaust 235°', 13, 'middle', LV, True))
    x, y = _pt(cx, cy, 122, -10); o.append(T(x - 6, y - 4, 'IVO 10°', 13, 'end', AC, True))
    x, y = _pt(cx, cy, 122, 10); o.append(T(x + 6, y - 4, 'EVC 10°', 13, 'start', LV, True))
    x, y = _pt(cx, cy, 132, 222); o.append(T(x - 2, y + 12, 'IVC 40°', 13, 'end', AC, True))
    x, y = _pt(cx, cy, 120, 135); o.append(T(x + 4, y + 18, 'EVO 45°', 13, 'start', LV, True))
    o.append(T(cx, cy - 162, 'overlap 20°', 13, 'middle', NX, True))
    o.append(T(cx, 400, 'IVO, IVC: inlet valve opens, closes', 13, 'middle', MUT))
    o.append(T(cx, 418, 'EVO, EVC: exhaust valve opens, closes', 13, 'middle', MUT))
    # port timing
    cx2 = 540
    _circle(o, cx2, cy, 'Two-stroke port timing')
    o.append(_arc(cx2, cy, 120, 120, 240, LV, 8))    # exhaust 60 before to 60 after BDC
    o.append(_arc(cx2, cy, 96, 135, 225, AC, 8))     # transfer 45/45
    o.append(_arc(cx2, cy, 108, 305, 415, NX, 8))    # inlet 55 before to 55 after TDC
    x, y = _pt(cx2, cy, 124, 120); o.append(T(x + 4, y + 4, 'EPO 60°', 13, 'start', LV, True))
    x, y = _pt(cx2, cy, 124, 240); o.append(T(x - 4, y + 4, 'EPC 60°', 13, 'end', LV, True))
    x, y = _pt(cx2, cy, 96, 135); o.append(T(x - 6, y - 8, 'TPO 45°', 13, 'end', AC, True))
    x, y = _pt(cx2, cy, 96, 225); o.append(T(x + 6, y - 8, 'TPC 45°', 13, 'start', AC, True))
    x, y = _pt(cx2, cy, 112, 305); o.append(T(x - 6, y, 'IPO 55°', 13, 'end', NX, True))
    x, y = _pt(cx2, cy, 112, 55); o.append(T(x + 6, y, 'IPC 55°', 13, 'start', NX, True))
    o.append(T(cx2, 400, 'E, T, I: exhaust, transfer, inlet port', 13, 'middle', MUT))
    o.append(T(cx2, 418, 'PO, PC: port opens, closes', 13, 'middle', MUT))
    return 432, ''.join(o)


FIG[5] = (f5, 'Left: the first worked example’s valve timing. The inlet is open for 230° and the exhaust for 235°; both are open for the 20° around TDC, '
              'the overlap. Right: the second example’s port timing, symmetric about BDC for exhaust (120°) and transfer (90°) and about TDC for the inlet (110°).',
          'Two timing circles with TDC at the top and BDC at the bottom. Left: an inlet arc from 10 degrees before TDC to 40 degrees after BDC and an exhaust '
          'arc from 45 degrees before BDC to 10 degrees after TDC, overlapping at the top. Right: exhaust port arc 60 degrees each side of BDC, transfer arc 45 '
          'degrees each side of BDC and inlet arc 55 degrees each side of TDC.')


# ---- 1.6 flat four-throw crankshaft and the stroke chart for 1-3-4-2 ----
def f6():
    o = []
    # crankshaft side view
    o.append(T(140, 26, 'Flat crankshaft', 14, 'middle', INK, True))
    ys, yu, yd = 130, 80, 180
    o.append(L(20, ys, 260, ys, INK, 6))
    for i, (x, up) in enumerate(((50, True), (110, False), (170, False), (230, True))):
        y = yu if up else yd
        o.append(L(x - 12, ys, x - 12, y, INK, 5)); o.append(L(x + 12, ys, x + 12, y, INK, 5)); o.append(L(x - 12, y, x + 12, y, AC, 7))
        o.append(T(x, (y - 14) if up else (y + 24), str(i + 1), 15, 'middle', AC, True))
    o.append(T(140, 236, '1 and 4 at TDC together;', 13, 'middle', MUT)); o.append(T(140, 254, '2 and 3 at TDC 180° later', 13, 'middle', MUT))
    # stroke chart
    X0, Y0, cw, rh = 330, 70, 92, 44
    o.append(T(X0 + 2 * cw, 26, 'Firing order 1-3-4-2', 14, 'middle', INK, True))
    for j, s in enumerate(('0–180°', '180–360°', '360–540°', '540–720°')):
        o.append(T(X0 + cw * j + cw / 2, Y0 - 10, s, 13, 'middle', MUT))
    rows = {1: 'PEIC', 2: 'EICP', 3: 'CPEI', 4: 'ICPE'}
    name = {'P': 'power', 'E': 'exhaust', 'I': 'intake', 'C': 'compress'}
    fill = {'P': ACS, 'E': PANEL, 'I': PANEL, 'C': NXS}
    for i, cyl in enumerate((1, 2, 3, 4)):
        y = Y0 + rh * i
        o.append(T(X0 - 12, y + rh / 2 + 5, f'cyl {cyl}', 13, 'end', INK, True))
        for j, c in enumerate(rows[cyl]):
            o.append(R(X0 + cw * j, y, cw, rh, fill[c], AC if c == 'P' else L2, 0, 1.5))
            o.append(T(X0 + cw * j + cw / 2, y + rh / 2 + 5, name[c], 13, 'middle', AC if c == 'P' else INK, c == 'P'))
    o.append(T(X0 + 2 * cw, Y0 + 4 * rh + 26, 'one power stroke every 180°: 12.5 ms apart at 2400 rev/min', 13, 'middle', MUT))
    return Y0 + 4 * rh + 44, ''.join(o)


FIG[6] = (f6, 'The inline four’s flat crankshaft puts pistons 1 and 4 at TDC together and 2 and 3 half a turn later. With the order 1-3-4-2 the chart '
              'shows which stroke each cylinder is on: in every half-turn exactly one cylinder is on power, as the worked example found for the first one.',
          'Left: side view of a four-throw crankshaft with throws 1 and 4 up and 2 and 3 down. Right: a table of four cylinders by four half-turns. '
          'Cylinder 1 runs power, exhaust, intake, compression; cylinder 2 exhaust, intake, compression, power; cylinder 3 compression, power, exhaust, '
          'intake; cylinder 4 intake, compression, power, exhaust.')


# ---- 1.7 p-v diagrams of the two worked examples, to scale ----
def f7():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 380
    fx = lin(0, 0.9, x0, x1); fy = lin(0, 50, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], [0, 10, 20, 30, 40, 50], fx, fy,
                  'specific volume v (m³/kg)', 'p (bar)', lambda v: f'{v:.1f}' if v else '0'))
    v1 = 0.861
    def isen(pa, va, vb, n=60):
        vs = [va * (vb / va) ** (i / n) for i in range(n + 1)]
        return [(fx(v), fy(pa * (va / v) ** 1.4)) for v in vs]
    # Diesel r = 16, rho = 2
    vd2 = v1 / 16; vd3 = 2 * vd2
    dz = isen(1.0, v1, vd2) + [(fx(vd3), fy(48.50))] + isen(48.50, vd3, v1) + [(fx(v1), fy(1.0))]
    o.append(P(dz, LV, 3, fill=LVS, op=0.55))
    # Otto r = 8
    vo2 = v1 / 8
    oz = isen(1.0, v1, vo2) + [(fx(vo2), fy(48.0))] + isen(48.0, vo2, v1) + [(fx(v1), fy(1.0))]
    o.append(P(oz, AC, 2.5, dash='7 4'))
    o.append(C(fx(v1), fy(1.0), 5, INK)); o.append(Tb(fx(v1) - 14, fy(1.0) + 4, '1: 1 bar, 300 K', 13, 'end'))
    o.append(C(fx(vo2), fy(18.38), 5, AC)); o.append(Tb(fx(vo2) + 10, fy(18.38) + 4, 'Otto 2: 18.4 bar, 689 K', 13, 'start', AC, True))
    o.append(C(fx(vo2), fy(48.0), 5, AC))
    o.append(C(fx(vd2), fy(48.5), 5, LV)); o.append(C(fx(vd3), fy(48.5), 5, LV))
    o.append(L(fx(0.068), fy(37), fx(0.2), fy(40), L2, 1.2)); o.append(T(fx(0.205), fy(40) + 4, 'Diesel compresses to 0.054 m³/kg', 13, 'start', LV, True))
    o.append(Tb(fx(vd3) + 12, fy(48.5) + 4, '2→3 Diesel at 48.5 bar; Otto peak 48.0 bar at 3', 13, 'start', INK, True))
    o.append(C(fx(v1), fy(2.64), 5, LV)); o.append(T(fx(v1) - 8, fy(2.64) - 22, '4: 2.6 bar (both cycles)', 13, 'end', INK))
    o.append(boxt(430, 120, 250, 92, ['Otto, r = 8 (dashed): 56.5 %', 'w = 450 kJ/kg, mep 5.98 bar', 'Diesel, r = 16 (shaded): 61.4 %', 'w = 561 kJ/kg, mep 6.95 bar'],
                  PANEL, L2, 13, fills=[AC, AC, LV, LV]))
    return 430, ''.join(o)


FIG[7] = (f7, 'The two worked examples drawn to scale from 1 bar and 300 K. Both peak near 48 bar, and from v = 0.108 m³/kg they share almost the same expansion '
              'line, but the Diesel cycle compresses to half the volume first, so its loop (shaded) encloses 561 kJ/kg against the Otto cycle’s 450 kJ/kg.',
          'Pressure against specific volume. A dashed Otto loop compresses from 0.861 to 0.108 cubic metres per kilogram, rises at constant volume to 48 bar '
          'and expands back. A shaded Diesel loop compresses to 0.054, adds heat at 48.5 bar to 0.108 and expands along nearly the same line.')


# ---- 1.8 indicator diagram of a real SI engine over the ideal Otto cycle (sketch) ----
def f8():
    o = []
    x0, x1, y0, y1 = 70, 640, 40, 360
    o.append(L(x0, y1, x1 + 20, y1, L2, 1.5, arrow='m')); o.append(L(x0, y1, x0, y0 - 10, L2, 1.5, arrow='m'))
    o.append(T(x1 + 20, y1 + 22, 'V', 14, 'end', MUT)); o.append(T(x0 + 8, y0 - 4, 'p', 14, 'start', MUT))
    o.append(T(x1 + 20, y0 + 6, 'sketch, not to scale', 13, 'end', MUT))
    patm = y1 - 40
    fxv = lambda v: 120 + 500 * (v - 1) / 7     # volume ratio 1 (TDC) .. 8 (BDC)
    fyp = lambda p: patm - (p - 1) * 5.6
    o.append(L(x0, patm, x1, patm, MUT, 1, dash='3 4')); o.append(T(x1 + 4, patm + 4, 'atm', 13, 'start', MUT))
    geo = lambda a, b, n=40: [a * (b / a) ** (i / n) for i in range(n + 1)]
    ideal = [(fxv(v), fyp(8 ** 1.4 / (8 / v) ** 0 * (1 / v) ** 1.4 * 1)) for v in geo(8, 1)]
    ideal = [(fxv(v), fyp((8 / v) ** 1.4)) for v in geo(8, 1)] + [(fxv(v), fyp(48 / v ** 1.4)) for v in geo(1, 8)] + [(fxv(8), fyp(1))]
    o.append(P(ideal, MUT, 2, dash='7 5'))
    o.append(L(430, 80, 470, 80, MUT, 2, dash='7 5')); o.append(T(478, 85, 'ideal Otto cycle', 13, 'start', MUT, True))
    o.append(L(430, 104, 470, 104, AC, 3)); o.append(T(478, 109, 'actual indicator diagram', 13, 'start', AC, True))
    # actual: polytropic compression to the spark, rounded burning peak after TDC, lower expansion, blowdown from EVO
    comp = [(fxv(v), fyp(0.95 * (8 / v) ** 1.32)) for v in geo(8, 1.6, 30)]
    burn = [(1.45, 11.5), (1.3, 13.5), (1.18, 17), (1.08, 22), (1.02, 27), (1.03, 31), (1.08, 33), (1.15, 33.5), (1.3, 31), (1.5, 25)]
    expn = [(v, 25 * (1.5 / v) ** 1.4) for v in geo(1.5, 6.4, 25)[1:]]
    blow = [(6.9, 2.4), (7.4, 1.6), (7.8, 1.25), (8, 1.15)]
    act = comp + [(fxv(v), fyp(pp)) for v, pp in burn + expn + blow]
    o.append(P(act, AC, 3))
    # pumping loop (enlarged): exhaust stroke above atm, intake stroke below
    o.append(P([(fxv(8), patm - 6), (fxv(1), patm - 6), (fxv(1), patm + 7), (fxv(8), patm + 7), (fxv(8), patm - 6)], LV, 2.2, fill=LVS, op=0.8))
    sp = (fxv(1.6), fyp(0.95 * 5 ** 1.32))
    o.append(C(*sp, 6, NX)); o.append(L(sp[0] + 4, sp[1] + 6, 206, 374, L2, 1.2)); o.append(T(210, 382, 'spark, before TDC', 13, 'start', NX, True))
    o.append(L(fxv(1.12), fyp(38), fxv(1.7), fyp(41), L2, 1.2))
    o.append(T(fxv(1.75), fyp(41) + 4, 'time loss: the top is rounded and lower', 13, 'start', INK, True))
    o.append(L(fxv(2.3), fyp(14.6), fxv(2.9), fyp(20), L2, 1.2))
    o.append(T(fxv(2.95), fyp(20) + 4, 'heat loss to the walls lowers expansion', 13, 'start', INK, True))
    ev = (fxv(6.4), fyp(25 * (1.5 / 6.4) ** 1.4)); o.append(C(*ev, 6, NX))
    o.append(T(ev[0] - 10, ev[1] - 14, 'EVO: blowdown loss', 13, 'end', INK, True))
    o.append(T(fxv(4.5), patm + 28, 'pumping loop, negative work (enlarged)', 13, 'middle', LV, True))
    o.append(T(fxv(1), y1 + 20, 'TDC', 13, 'middle', MUT)); o.append(T(fxv(8), y1 + 20, 'BDC', 13, 'middle', MUT))
    return 400, ''.join(o)


FIG[8] = (f8, 'An SI engine’s indicator diagram (solid) over its ideal Otto cycle (dashed). Finite burning rounds and lowers the top, wall heat loss lowers the '
              'expansion line, early exhaust opening cuts the corner at BDC, and the small negative loop at atmospheric pressure is the pumping work. '
              'In the second worked example the main loop gave 380 J and the pumping loop 18 J.',
          'Sketch of pressure against volume. A dashed ideal Otto loop with a sharp top; inside it a solid actual loop with a rounded, lower peak, a lower '
          'expansion line and a cut-off corner at bottom dead centre. At the bottom a thin shaded pumping loop near atmospheric pressure. Labels mark the '
          'spark, time loss, heat loss, exhaust valve opening and the pumping loop.')

spec = make_spec(FIG)
