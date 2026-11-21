"""Claude's hand-drawn figures for ae-struct-u1 (Aircraft Structures: construction, materials and loads), one per chapter,
drawn from each chapter's own worked example; every plotted value is computed here. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def arrow(x1, y1, x2, y2, c=AC, w=2, k='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=k)


def sb(base, s):
    return f'{base}<tspan baseline-shift="sub" font-size="11">{s}</tspan>'


# ---- 1.1 the skin panel and the spar root of the two worked examples ----
def f1():
    o = []
    o.append(T(180, 24, 'Worked example 1: one skin panel', 14, 'middle', INK, True))
    x0, y0, w, h = 44, 60, 230, 170
    o.append(R(x0, y0, w, h, ACS, AC, 4, 2))
    for i in range(4):
        y = y0 + 22 + i * (h - 44) / 3
        o.append(L(x0 - 14, y, x0 + w + 14, y, INK, 3))
    o.append(T(x0 + w + 18, y0 + 26, 'stringers (4)', 13, 'start', INK, True))
    for x in (x0, x0 + w):
        o.append(L(x, y0 - 12, x, y0 + h + 12, LV, 4))
    o.append(T(x0, y0 + h + 30, 'rib', 13, 'middle', LV, True)); o.append(T(x0 + w, y0 + h + 30, 'rib', 13, 'middle', LV, True))
    o.append(T(x0 + w / 2, y0 + h + 30, '0.6 m spanwise', 13, 'middle', MUT))
    o.append(Tb(x0 + w / 2, y0 + 49, 'p = 15 kPa on 0.24 m²', 14, 'middle', AC, True))
    o.append(Tb(x0 + w / 2, y0 + 91, 'P = 3600 N', 14, 'middle', AC, True))
    o.append(T(x0 + w + 18, y0 + 112, '900 N each', 13, 'start', INK, True))
    o.append(T(x0 + w + 18, y0 + 130, 'to the ribs', 13, 'start', MUT))
    o.append(T(24, y0 + h / 2 + 4, '0.4 m', 13, 'middle', MUT))
    # spar section
    sx, top, bot = 530, 70, 230
    o.append(T(540, 24, 'Worked example 2: spar at the root', 14, 'middle', INK, True))
    o.append(R(sx - 60, top - 14, 120, 16, NXS, NX, 3, 2)); o.append(R(sx - 60, bot - 2, 120, 16, NXS, NX, 3, 2))
    o.append(R(sx - 4, top + 2, 8, bot - top - 4, PANEL, INK, 1, 1.5))
    o.append(arrow(sx + 104, top - 6, sx + 66, top - 6, NX, 2.5)); o.append(T(sx + 108, top - 1, '720 kN', 13, 'start', NX, True))
    o.append(T(sx + 108, top + 16, 'compression', 13, 'start', MUT))
    o.append(arrow(sx + 66, bot + 6, sx + 104, bot + 6, NX, 2.5)); o.append(T(sx + 108, bot + 11, '720 kN', 13, 'start', NX, True))
    o.append(T(sx + 108, bot + 28, 'tension', 13, 'start', MUT))
    o.append(L(sx - 84, top - 6, sx - 84, bot + 6, L2, 1.5)); o.append(T(sx - 90, (top + bot) / 2 + 4, 'h = 0.40 m', 13, 'end', INK))
    o.append(T(sx + 14, (top + bot) / 2 - 6, 'web 3 mm', 13, 'start', INK))
    o.append(T(sx + 14, (top + bot) / 2 + 12, 'τ = 60 MPa', 13, 'start', LV, True))
    o.append(T(540, 284, 'M = 288 kN·m → F = M/h = 720 kN', 14, 'middle', INK, True))
    o.append(T(540, 302, 'cap area at 400 MPa: 1800 mm²', 13, 'middle', MUT))
    # the chain
    chain = ['air pressure', 'skin', 'stringers', 'ribs', 'spars', 'root fitting', 'fuselage frame']
    y = 340
    for i, s in enumerate(chain):
        x = 14 + i * 101
        o.append(R(x, y - 18, 92, 28, PANEL, AC if i in (0, 4) else L2, 6, 1.6)); o.append(T(x + 46, y + 1, s, 13))
        if i: o.append(arrow(x - 9, y - 4, x - 1, y - 4, AC, 2))
    return 362, ''.join(o)


FIG[1] = (f1, 'Left: the 0.6 m by 0.4 m skin panel at 15 kPa carries 3600 N and hands 900 N to each of its four stringers, which pass it to the ribs. Right: at the spar root, the 288 kN·m moment becomes 720 kN in each cap (h = 0.40 m) and the shear becomes 60 MPa in the web.',
          'Two panels. Left: a rectangular skin panel 0.6 by 0.4 metres between two ribs, crossed by four stringers, with 15 kilopascals giving 3600 newtons, 900 newtons per stringer. Right: an I-shaped spar section with caps 0.40 metres apart, 720 kilonewtons compression in the top cap and tension in the bottom cap, and 60 megapascals shear in the 3 millimetre web. Below, the load path chain from air pressure to the fuselage frame.')


# ---- 1.2 three construction types, in section ----
def f2():
    o = []
    cy = 140
    # truss
    cx = 120
    o.append(T(cx, 28, 'Truss', 15, 'middle', INK, True))
    sq = [(cx - 60, cy - 60), (cx + 60, cy - 60), (cx + 60, cy + 60), (cx - 60, cy + 60)]
    o.append(P(sq + [sq[0]], INK, 3)); o.append(L(sq[0][0], sq[0][1], sq[2][0], sq[2][1], INK, 1.5)); o.append(L(sq[1][0], sq[1][1], sq[3][0], sq[3][1], INK, 1.5))
    for x, y in sq: o.append(C(x, y, 5, INK))
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="82" ry="82" style="fill:none;stroke:{L2};stroke-width:1.5;stroke-dasharray:5 4"/>')
    o.append(T(cx, cy + 108, 'tubes and wires carry load', 13, 'middle', INK)); o.append(T(cx, cy + 126, 'fabric (dashed) only seals', 13, 'middle', MUT))
    # monocoque
    cx = 360
    o.append(T(cx, 28, 'Monocoque', 15, 'middle', INK, True))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="78" style="fill:none;stroke:{AC};stroke-width:12"/>')
    o.append(T(cx, cy - 4, 'thick skin', 13, 'middle', AC, True)); o.append(T(cx, cy + 14, 'carries everything', 13, 'middle', MUT))
    o.append(T(cx, cy + 108, 'no skeleton: heavy,', 13, 'middle', INK)); o.append(T(cx, cy + 126, 'thick to resist buckling', 13, 'middle', MUT))
    # semi-monocoque
    cx = 600
    o.append(T(cx, 28, 'Semi-monocoque', 15, 'middle', INK, True))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="78" style="fill:none;stroke:{AC};stroke-width:2.5"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="68" style="fill:none;stroke:{LV};stroke-width:5;stroke-opacity:0.6"/>')
    for i in range(16):
        a = 2 * math.pi * i / 16
        o.append(f'<rect x="{cx + 73 * math.cos(a) - 3.5:.1f}" y="{cy + 73 * math.sin(a) - 3.5:.1f}" width="7" height="7" style="fill:{INK}"/>')
    o.append(T(cx, cy - 4, 'thin skin 1.5 mm', 13, 'middle', AC, True)); o.append(T(cx, cy + 14, 'D = 2.0 m', 13, 'middle', MUT))
    o.append(T(cx, cy + 108, 'skin + stringers (dots)', 13, 'middle', INK)); o.append(T(cx, cy + 126, '+ frame ring', 13, 'middle', LV, True))
    o.append(T(360, 300, 'At 60 kPa the thin skin carries hoop stress 40 MPa and longitudinal stress 20 MPa;', 13, 'middle', INK))
    o.append(T(360, 318, 'the stringers and frames stop it buckling under bending compression.', 13, 'middle', INK))
    return 332, ''.join(o)


FIG[2] = (f2, 'The three construction types in section. The semi-monocoque shell of the worked example (2.0 m diameter, 1.5 mm skin, 60 kPa) carries 40 MPa hoop and 20 MPa longitudinal stress in its thin skin; stringers and frames keep it from buckling.',
          'Three fuselage cross-sections side by side: a square truss of tubes with diagonal wires inside a dashed fabric outline; a monocoque ring with a thick skin; and a semi-monocoque ring with a thin skin, sixteen small stringer squares and an inner frame ring, labelled 1.5 millimetre skin and 2.0 metre diameter.')


# ---- 1.3 the wing panel of the worked example: spars at 15 % and 60 %, 11 ribs at 0.45 m ----
def f3():
    o = []
    X0, X1 = 70, 650; fx = lin(0, 4.5, X0, X1)
    Y0, Y1 = 50, 230; fy = lin(0, 3.0, Y0, Y1)          # chord runs downward: leading edge at top
    o.append(R(X0, Y0, X1 - X0, Y1 - Y0, 'var(--fig)', L2, 2, 1.5))
    o.append(R(X0, fy(0.45), X1 - X0, fy(1.80) - fy(0.45), ACS, 'none', 0, 0))
    for i in range(11):
        x = fx(0.45 * i)
        o.append(L(x, Y0, x, Y1, INK, 2.5 if i in (0, 10) else 1.6))
    o.append(L(X0, fy(0.45), X1, fy(0.45), AC, 4)); o.append(L(X0, fy(1.80), X1, fy(1.80), AC, 4))
    o.append(T(X1 + 8, fy(0.45) + 5, 'front spar', 13, 'start', AC, True)); o.append(T(X1 + 8, fy(1.80) + 5, 'rear spar', 13, 'start', AC, True))
    o.append(T(X1, Y0 - 8, 'leading edge', 13, 'end', MUT))
    o.append(T(X1 + 8, Y1 - 10, 'trailing', 13, 'start', MUT)); o.append(T(X1 + 8, Y1 + 6, 'edge', 13, 'start', MUT))
    o.append(Tb((X0 + X1) / 2, (fy(0.45) + fy(1.80)) / 2 + 5, 'torsion box 1.35 m wide', 14, 'middle', AC, True))
    o.append(L(40, fy(0), 40, fy(0.45), L2, 1.5)); o.append(T(36, fy(0.225) + 4, '0.45', 13, 'end', MUT))
    o.append(L(40, fy(0.45), 40, fy(1.80), L2, 1.5)); o.append(T(36, fy(1.125) + 4, '1.35', 13, 'end', MUT))
    o.append(L(40, fy(1.80), 40, fy(3.0), L2, 1.5)); o.append(T(36, fy(2.4) + 4, '1.20', 13, 'end', MUT))
    o.append(T(X0, Y1 + 22, 'root rib', 13, 'middle', INK, True)); o.append(T(X1, Y1 + 22, 'tip rib', 13, 'middle', INK, True))
    o.append(T(fx(2.25), Y1 + 22, 'rib pitch 0.45 m', 13, 'middle', MUT))
    o.append(T((X0 + X1) / 2, Y1 + 46, '4.5 m ÷ 0.45 m = 10 bays → 11 ribs (one at each end of every bay)', 14, 'middle', INK, True))
    o.append(T(X0, 26, 'plan view: 4.5 m of wing, chord 3.0 m (distances in m from the leading edge)', 13, 'start', MUT))
    return 292, ''.join(o)


FIG[3] = (f3, 'The wing of the worked example in plan: chord 3.0 m, front spar at 0.45 m and rear spar at 1.80 m from the leading edge, so the torsion box is 1.35 m wide. Ribs at 0.45 m pitch over 4.5 m make 10 bays and 11 ribs, counting the root and tip ribs.',
          'Plan view of a 4.5 metre length of wing with chord 3.0 metres. Front and rear spars run spanwise at 0.45 and 1.80 metres from the leading edge, with the 1.35 metre torsion box shaded between them. Eleven chordwise ribs, including a root rib and a tip rib, are spaced 0.45 metres apart.')


# ---- 1.4 the sandwich of the worked example ----
def f4():
    o = []
    x0, x1 = 40, 360
    yt, yb = 70, 230                     # core 20 mm drawn 160 px; faces exaggerated
    o.append(R(x0, yt - 12, x1 - x0, 12, NXS, NX, 0, 2)); o.append(R(x0, yb, x1 - x0, 12, NXS, NX, 0, 2))
    o.append(R(x0, yt, x1 - x0, yb - yt, PANEL, L2, 0, 1.5))
    for i in range(9):
        x = x0 + 20 + i * 35
        o.append(P([(x, yt), (x + 10, yt + 40), (x, yt + 80), (x + 10, yt + 120), (x, yb)], L2, 1.5))
    o.append(T(x0 + 6, yt - 18, 'face 0.5 mm aluminium, E = 70 GPa', 13, 'start', NX, True))
    o.append(T(x0 + 6, yb + 32, 'face 0.5 mm', 13, 'start', NX, True))
    o.append(Tb((x0 + x1) / 2, (yt + yb) / 2 + 5, 'honeycomb core 20 mm', 14, 'middle', INK, True))
    o.append(L(x1 + 24, yt - 6, x1 + 24, yb + 6, AC, 2)); o.append(L(x1 + 16, yt - 6, x1 + 32, yt - 6, AC, 2)); o.append(L(x1 + 16, yb + 6, x1 + 32, yb + 6, AC, 2))
    o.append(T(x1 + 36, (yt + yb) / 2 - 4, 'd = 20.5 mm', 14, 'start', AC, True)); o.append(T(x1 + 36, (yt + yb) / 2 + 14, 'between face', 13, 'start', MUT))
    o.append(T(x1 + 36, (yt + yb) / 2 + 30, 'mid-planes', 13, 'start', MUT))
    o.append(arrow(x1 - 10, yt - 44, x1 - 70, yt - 44, LV, 2.5)); o.append(arrow(x0 + 10, yt - 44, x0 + 70, yt - 44, LV, 2.5))
    o.append(T((x0 + x1) / 2, yt - 40, 'compression', 13, 'middle', LV, True))
    o.append(arrow(x1 - 70, yb + 50, x1 - 10, yb + 50, LV, 2.5)); o.append(arrow(x0 + 70, yb + 50, x0 + 10, yb + 50, LV, 2.5))
    o.append(T((x0 + x1) / 2, yb + 54, 'tension', 13, 'middle', LV, True))
    o.append(T(360, 304, 'D = E t d²/2 = 7354 N·m per metre width', 14, 'middle', INK, True))
    # bar comparison (log scale is hard to read: show the two numbers side by side)
    o.append(R(520, 70, 180, 60, ACS, AC, 8, 2)); o.append(T(610, 96, 'sandwich', 14, 'middle', INK, True)); o.append(T(610, 116, 'D = 7354 N·m', 14, 'middle', AC, True))
    o.append(R(520, 150, 180, 60, PANEL, L2, 8, 2)); o.append(T(610, 176, 'solid 1.0 mm sheet', 13, 'middle', INK, True)); o.append(T(610, 196, 'D = 5.83 N·m', 14, 'middle', MUT, True))
    o.append(T(610, 240, 'same face mass:', 13, 'middle', MUT)); o.append(T(610, 258, '1261 times stiffer', 14, 'middle', AC, True))
    return 318, ''.join(o)


FIG[4] = (f4, 'The floor panel of the worked example: 0.5 mm faces on a 20 mm core, so the faces sit d = 20.5 mm apart (drawn thicker than scale). In bending one face is squeezed and the other stretched, and the panel is 1261 times stiffer than a solid sheet with the same face metal.',
          'Cross-section of a sandwich panel: two thin aluminium faces, 0.5 millimetres each, on a 20 millimetre honeycomb core, with the 20.5 millimetre distance between the face mid-planes marked. Arrows show compression in the top face and tension in the bottom face. Two boxes compare bending stiffness: 7354 newton metres per metre for the sandwich against 5.83 for a solid 1.0 millimetre sheet.')


# ---- 1.5 specific strength and specific stiffness from the chapter's table ----
def f5():
    o = []
    mats = [('2024-T3 Al', 174.5, 26.3), ('7075-T6 Al', 202.8, 25.3), ('6061-T6 Al', 114.8, 25.6), ('Ti-6Al-4V', 214.4, 25.7),
            ('300M steel', 248.4, 25.5), ('CFRP (fibre)', 937.5, 81.2), ('GFRP', 263.2, 13.2)]
    lx, ax0, ax1 = 122, 132, 400
    fs = lin(0, 1000, ax0, ax1); fe = lin(0, 90, 450, 700)
    o.append(T((ax0 + ax1) / 2, 24, 'σult/ρ (kN·m/kg)', 14, 'middle', INK, True)); o.append(T(575, 24, 'E/ρ (MN·m/kg)', 14, 'middle', INK, True))
    for i, (n, s, e) in enumerate(mats):
        y = 50 + i * 36
        c = AC if n.startswith('CFRP') else (NX if n == 'GFRP' else L2)
        fill = ACS if n.startswith('CFRP') else (NXS if n == 'GFRP' else PANEL)
        o.append(T(lx, y + 15, n, 13, 'end', INK))
        o.append(R(ax0, y, fs(s) - ax0, 22, fill, c, 3, 1.5)); o.append(T(fs(s) + 6, y + 16, f'{s:g}', 13, 'start', INK))
        o.append(R(450, y, fe(e) - 450, 22, fill, c, 3, 1.5)); o.append(T(fe(e) + 6, y + 16, f'{e:g}', 13, 'start', INK))
    o.append(L(fe(25.5), 44, fe(25.5), 300, LV, 1.8, dash='5 4'))
    o.append(T(fe(25.5) + 4, 316, 'metals: all near 25', 13, 'start', LV, True))
    o.append(L(ax0, 300, ax1, 300, L2, 1.5)); o.append(L(450, 300, 700, 300, L2, 1.5))
    return 326, ''.join(o)


FIG[5] = (f5, 'Specific strength and specific stiffness computed from the chapter’s table. CFRP along the fibre wins on both; on stiffness per kilogram aluminium, titanium and steel all sit near 25 MN·m/kg, so changing metal does not help a stiffness-critical part.',
          'Two horizontal bar charts for seven materials. Specific strength in kilonewton metres per kilogram: 2024 aluminium 174.5, 7075 aluminium 202.8, 6061 aluminium 114.8, titanium 214.4, 300M steel 248.4, CFRP 937.5, GFRP 263.2. Specific stiffness in meganewton metres per kilogram: 26.3, 25.3, 25.6, 25.7, 25.5, 81.2 and 13.2, with a dashed line marking that the metals are all near 25.')


# ---- 1.6 the lap joint of worked example 2 and its three checks ----
def f6():
    o = []
    # side view
    o.append(T(180, 24, 'side view (single lap)', 13, 'middle', MUT))
    o.append(R(30, 60, 210, 10, PANEL, INK, 0, 1.5)); o.append(R(130, 70, 210, 10, PANEL, INK, 0, 1.5))
    o.append(R(180, 52, 10, 36, NXS, NX, 2, 1.5))
    o.append(arrow(70, 50, 20, 50, AC, 2.5)); o.append(arrow(300, 92, 350, 92, AC, 2.5))
    o.append(T(46, 44, 'P', 14, 'middle', AC, True)); o.append(T(330, 112, 'P', 14, 'middle', AC, True))
    o.append(T(200, 112, 'rivet in single shear', 13, 'middle', NX, True))
    # plan view of the lower sheet with 3 holes
    x0, y0, wd = 60, 150, 200          # 60 mm wide drawn 200 px high? use horizontal width = sheet width
    o.append(T(170, 140, 'plan: 60 mm wide, t = 2 mm, 3 rivets d = 5 mm', 13, 'middle', MUT))
    o.append(R(70, 150, 200, 110, PANEL, INK, 0, 1.5))
    for i in range(3):
        o.append(C(70 + 200 * (i + 0.5) / 3, 205, 8, NX))
    o.append(L(70, 205, 270, 205, LV, 1.5, dash='5 4'))
    o.append(T(170, 280, 'net width 60 − 3 × 5 = 45 mm (dashed line)', 13, 'middle', LV, True))
    # the three capacities
    fx = lin(0, 40, 400, 690)
    o.append(T(545, 24, 'strength of each mode (kN)', 14, 'middle', INK, True))
    rows = [('rivet shear', 10.603, AC, ACS, '10.6 governs'), ('bearing', 15.0, NX, NXS, '15.0'), ('net section', 27.0, LV, LVS, '27.0'), ('uncut sheet', 36.0, L2, PANEL, '36.0')]
    for i, (n, v, c, f, s) in enumerate(rows):
        y = 50 + i * 54
        o.append(T(400, y, n, 13, 'start', INK, True))
        o.append(R(400, y + 8, fx(v) - 400, 22, f, c, 3, 1.8)); o.append(T(fx(v) + 6 if v < 30 else fx(v) - 6, y + 24, s, 13, 'start' if v < 30 else 'end', INK, True))
    o.append(T(545, 280, 'efficiency 10.6 ÷ 36.0 = 29 %', 14, 'middle', AC, True))
    return 296, ''.join(o)


FIG[6] = (f6, 'The joint of worked example 2: two 2 mm sheets, 60 mm wide, lapped and joined by three 5 mm rivets in one row. Rivet shear (10.6 kN) is weaker than bearing (15.0 kN) and the net section through the holes (27.0 kN), so it sets the strength, 29 % of the uncut sheet.',
          'Left: side view of a single lap joint with one rivet in single shear between two offset sheets pulled by forces P, and a plan view of a 60 millimetre wide sheet with three 5 millimetre rivet holes in one row and the 45 millimetre net width marked. Right: bars for the strength of each mode: rivet shear 10.6 kilonewtons (governs), bearing 15.0, net section 27.0, uncut sheet 36.0.')


# ---- 1.7 from weight to ultimate load, and the engine's inertia relief ----
def f7():
    o = []
    steps = [('weight W = m g', '60 000 × 9.81', '588.6 kN', PANEL, L2), ('limit lift = n W', '× 2.5', '1471.5 kN', ACS, AC), ('ultimate = 1.5 × limit', '× 1.5', '2207.3 kN', LVS, LV)]
    for i, (a, b, v, f, c) in enumerate(steps):
        y = 40 + i * 92
        o.append(R(30, y, 250, 56, f, c, 8, 2)); o.append(T(155, y + 24, a, 14, 'middle', INK, True)); o.append(T(155, y + 44, v, 14, 'middle', c if c != L2 else INK, True))
        if i: o.append(arrow(155, y - 34, 155, y - 4, AC, 2)); o.append(T(165, y - 14, b, 13, 'start', MUT))
    # half-wing front view with lift and engine inertia
    rx, tx, wy = 360, 690, 150
    o.append(R(rx, wy - 6, tx - rx, 12, PANEL, INK, 4, 2)); o.append(R(rx - 20, wy - 40, 20, 80, NXS, NX, 4, 2))
    o.append(T(rx - 10, wy + 60, 'root', 13, 'middle', NX, True))
    for i in range(8):
        x = rx + 20 + i * 40
        o.append(arrow(x, wy - 14, x, wy - 54 + i * 3, AC, 2, 'n'))
    o.append(T((rx + tx) / 2, wy - 74, 'lift: root moment 1800 kN·m', 13, 'middle', AC, True))
    ex = rx + 4.0 / 12 * (tx - rx)
    o.append(R(ex - 16, wy + 8, 32, 22, PANEL, INK, 6, 2)); o.append(arrow(ex, wy + 32, ex, wy + 78, LV, 3))
    o.append(T(ex + 14, wy + 62, 'engine inertia n m g = 49.05 kN', 13, 'start', LV, True))
    o.append(L(rx, wy + 100, ex, wy + 100, L2, 1.5)); o.append(T((rx + ex) / 2, wy + 118, '4.0 m', 13, 'middle', MUT))
    o.append(T((rx + tx) / 2, wy + 146, 'relief 49.05 × 4.0 = 196.2 kN·m → net 1603.8 kN·m', 14, 'middle', INK, True))
    return 310, ''.join(o)


FIG[7] = (f7, 'Left: worked example 1 turns the 588.6 kN weight into a 1471.5 kN limit lift at n = 2.5 and a 2207.3 kN ultimate load. Right: worked example 2, where the engine’s 49.05 kN inertia load 4.0 m from the root removes 196.2 kN·m of the 1800 kN·m lift moment.',
          'Left: three stacked boxes from weight 588.6 kilonewtons, times 2.5 to limit lift 1471.5 kilonewtons, times 1.5 to ultimate load 2207.3 kilonewtons. Right: front view of a half-wing built into a root, with upward lift arrows and an engine 4.0 metres from the root whose inertia load of 49.05 kilonewtons points down, reducing the root moment from 1800 to 1603.8 kilonewton metres.')


# ---- 1.8 the V-n diagram of the two worked examples ----
def f8():
    o = []
    X0, X1, Y0, Y1 = 70, 680, 40, 330
    fx = lin(0, 180, X0, X1); fy = lin(-1.5, 3.2, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 40, 80, 120, 160], [-1, 0, 1, 2, 3], fx, fy, 'equivalent airspeed V (m/s)', 'load factor n', yfmt=neg))
    VS1, VA, VSn, VC, VD = 57.14, 90.35, 78.25, 120, 160
    o.append(L(X0, fy(0), X1, fy(0), INK, 1.2))
    o.append(P([(fx(v), fy((v / VS1) ** 2)) for v in [VA * i / 40 for i in range(41)]], AC, 3))
    o.append(P([(fx(VA), fy(2.5)), (fx(VD), fy(2.5)), (fx(VD), fy(0)), (fx(VC), fy(-1)), (fx(VSn), fy(-1))], AC, 3))
    o.append(P([(fx(v), fy(-(v / VSn) ** 2)) for v in [VSn * i / 30 for i in range(31)]], AC, 3))
    for v, n in ((VC, 2.8375), (VD, 2.225), (VC, -0.8375), (VD, -0.225)):
        o.append(L(fx(0), fy(1), fx(v), fy(n), LV, 2, dash='7 5'))
    o.append(P([(fx(VC), fy(2.8375)), (fx(VD), fy(2.225))], LV, 2, dash='3 3'))
    o.append(C(fx(VA), fy(2.5), 5, AC)); o.append(Tb(fx(VA) - 6, fy(2.5) - 12, 'A (90.4, 2.5)', 13, 'end', AC, True))
    o.append(C(fx(VC), fy(2.8375), 5, LV)); o.append(Tb(fx(VC), fy(2.8375) - 12, 'gust at V_C: 2.84', 13, 'middle', LV, True))
    o.append(C(fx(VD), fy(2.225), 5, LV)); o.append(Tb(fx(VD) + 8, fy(2.225) + 18, '2.23', 13, 'start', LV, True))
    o.append(Tb(fx(VD) + 8, fy(2.5) - 6, 'D', 13, 'start', AC, True))
    o.append(C(fx(VC), fy(-0.8375), 4, LV)); o.append(Tb(fx(VC) - 6, fy(-0.8375) - 8, '−0.84', 13, 'end', LV, True))
    o.append(Tb(fx(VC) + 4, fy(-1) + 20, 'F (120, −1.0)', 13, 'middle', AC, True))
    o.append(Tb(fx(VD) + 8, fy(0) - 6, 'E', 13, 'start', AC, True))
    o.append(C(fx(VS1), fy(1), 4, AC)); o.append(Tb(fx(VS1) + 8, fy(1) + 18, 'V_S1 = 57.1', 13, 'start', AC, True))
    o.append(Tb(fx(30), fy(2.0), 'gust lines start at n = 1', 13, 'middle', LV, True))
    return 380, ''.join(o)


FIG[8] = (f8, 'The V-n diagram of the worked examples: stall line to A (90.4 m/s, 2.5), flat top to D at 160 m/s, negative limit −1.0 to F at 120 m/s and 0 at E. The 15 m/s gust line ends at n = 2.84 at V_C, above the manoeuvre top, so it sizes upward bending.',
          'V-n diagram with speed from 0 to 180 metres per second and load factor from minus 1.5 to 3.2. A parabolic stall line rises from the origin through 1.0 at 57.1 metres per second to corner A at 90.4 and 2.5; the flat top runs to D at 160; the envelope closes at E. The negative side follows a stall curve to minus 1.0, stays flat to F at 120, then rises to zero at 160. Dashed gust lines from n equal 1 at zero speed reach 2.84 and minus 0.84 at 120, and 2.23 and minus 0.23 at 160.')


# ---- 1.9 shear and moment for the uniform wing, and with the engine ----
def f9():
    o = []
    X0, X1 = 80, 660; fx = lin(0, 8, X0, X1)
    xs = [i * 0.1 for i in range(81)]
    fy = lin(0, 80, 170, 40)
    o.append(axes(X0, X1, 40, 170, [], [0, 40, 80], fx, fy, '', 'shear V (kN)'))
    o.append(P([(fx(x), fy(9 * (8 - x))) for x in xs], AC, 3))
    v2 = [(fx(x), fy(9 * (8 - x) - (40 if x < 3 else 0))) for x in xs if x <= 3] 
    o.append(P([(fx(x), fy(9 * (8 - x) - 40)) for x in xs if x <= 3], LV, 2.5, dash='7 5'))
    o.append(L(fx(3), fy(5), fx(3), fy(45), LV, 2.5, dash='7 5'))
    o.append(Tb(fx(0.2), fy(72) - 10, '72', 13, 'start', AC, True)); o.append(Tb(fx(0) + 6, fy(32) + 16, '32', 13, 'start', LV, True))
    o.append(Tb(fx(3) + 8, fy(45) - 4, '45', 13, 'start', INK, True)); o.append(Tb(fx(3) + 8, fy(5) + 4, '5', 13, 'start', LV, True))
    gy = lin(0, 300, 360, 220)
    o.append(axes(X0, X1, 220, 360, [0, 2, 4, 6, 8], [0, 150, 300], fx, gy, 'x from root (m): root at left, tip at right', 'moment M (kN·m)'))
    o.append(P([(fx(x), gy(9 * (8 - x) ** 2 / 2)) for x in xs], AC, 3))
    o.append(P([(fx(x), gy(9 * (8 - x) ** 2 / 2 - (40 * (3 - x) if x < 3 else 0))) for x in xs if x <= 3.01], LV, 2.5, dash='7 5'))
    o.append(Tb(fx(0.6), gy(288) + 4, '288', 13, 'start', AC, True)); o.append(Tb(fx(0) + 6, gy(168) + 16, '168', 13, 'start', LV, True))
    o.append(Tb(fx(2) + 6, gy(162) - 6, '162 at 2 m', 13, 'start', AC, True)); o.append(Tb(fx(3) + 10, gy(112.5) + 4, '112.5', 13, 'start', INK, True))
    o.append(T(X1, 30, 'solid: 9 kN/m only · dashed: with the 40 kN engine at 3 m', 13, 'end', MUT))
    return 412, ''.join(o)


FIG[9] = (f9, 'Shear (top) and bending moment (bottom) along the 8 m semi-span. Solid: the uniform 9 kN/m net load of worked example 1, 72 kN and 288 kN·m at the root. Dashed: with the 40 kN engine at 3 m the shear drops from 45 to 5 kN there and the root values fall to 32 kN and 168 kN·m.',
          'Two stacked plots against distance from the root, 0 to 8 metres. Top: shear falls linearly from 72 kilonewtons at the root to zero at the tip; a dashed line for the engine case drops from 45 to 5 at 3 metres and reaches 32 at the root. Bottom: bending moment curves from 288 kilonewton metres at the root (162 at 2 metres) to zero at the tip; the dashed engine case is 112.5 at 3 metres and 168 at the root.')


# ---- 1.10 the pull-up of worked example 2: tail balancing load and rear-fuselage moment ----
def f10():
    o = []
    fx = lin(-4, 16, 40, 680)
    ya = 110
    o.append(f'<path d="M{fx(-4)},{ya} Q{fx(-4)},{ya - 26} {fx(-2.5)},{ya - 26} L{fx(13)},{ya - 18} L{fx(15.6)},{ya - 70} L{fx(16)},{ya - 70} L{fx(16)},{ya + 12} L{fx(-2.5)},{ya + 26} Q{fx(-4)},{ya + 26} {fx(-4)},{ya} Z" style="fill:{PANEL};stroke:{INK};stroke-width:2"/>')
    o.append(C(fx(0), ya, 6, INK)); o.append(T(fx(0), ya + 44, 'CG', 13, 'middle', INK, True))
    o.append(arrow(fx(0.5), ya - 10, fx(0.5), ya - 84, AC, 3)); o.append(T(fx(0.5) + 8, ya - 72, 'L_w = 1303.45 kN', 13, 'start', AC, True))
    o.append(T(fx(0.5) + 8, ya - 56, 'at a = 0.5 m', 13, 'start', MUT))
    o.append(arrow(fx(0), ya + 52, fx(0), ya + 96, INK, 2.5)); o.append(T(fx(0) + 8, ya + 90, 'n W = 1250 kN', 13, 'start', INK, True))
    o.append(arrow(fx(15), ya + 14, fx(15), ya + 66, LV, 3)); o.append(T(fx(15) - 14, ya + 50, 'P = 53.45 kN down', 13, 'end', LV, True))
    o.append(T(fx(15) - 14, ya + 68, '+ tail inertia 19.62 kN', 13, 'end', LV, True))
    o.append(T(fx(3.4), ya - 40, 'M₀ = 150 kN·m nose-down', 13, 'start', NX, True))
    o.append(L(fx(5), ya - 30, fx(5), ya + 30, NX, 3, dash='6 4')); o.append(T(fx(5), ya + 44, 'frame', 13, 'middle', NX, True))
    o.append(L(fx(0), ya + 116, fx(15), ya + 116, L2, 1.5)); o.append(T(fx(7.5), ya + 132, 'l_t = 15 m', 13, 'middle', MUT))
    # rear-fuselage bending moment from the tail forward
    by = 330; gy = lin(0, 1100, by, by - 80)
    o.append(L(fx(0), by, fx(15), by, L2, 1.5))
    o.append(P([(fx(15), gy(0)), (fx(0), gy(73.07 * 15))], LV, 3))
    o.append(L(fx(5), by, fx(5), gy(730.7), NX, 2, dash='5 4')); o.append(C(fx(5), gy(730.7), 5, NX))
    o.append(Tb(fx(5) + 10, gy(730.7) - 6, 'M = 73.07 × 10 = 730.7 kN·m', 13, 'start', NX, True))
    o.append(T(fx(15), by + 20, '0 at the tail', 13, 'middle', MUT)); o.append(T(fx(0), by + 20, 'largest at the wing', 13, 'middle', MUT))
    return 360, ''.join(o)


FIG[10] = (f10, 'The pull-up of worked example 2 at n = 2.5. Pitch balance about the CG needs a 53.45 kN tailplane download; with the tail’s 19.62 kN inertia load it bends the rear fuselage, with a moment of 730.7 kN·m at the frame 10 m forward of the tail that keeps growing towards the wing.',
           'Side view of a fuselage with the centre of gravity, wing lift 1303.45 kilonewtons acting 0.5 metres behind it, the load n W of 1250 kilonewtons down at the CG, a nose-down wing moment of 150 kilonewton metres, and at the tail, 15 metres behind the CG, a tailplane download of 53.45 kilonewtons plus 19.62 kilonewtons of tail inertia. A dashed frame line sits 10 metres forward of the tail. Below, the rear-fuselage bending moment rises in a straight line from zero at the tail to 730.7 kilonewton metres at the frame and keeps growing to the wing.')

import re as _re
_SUBRX = _re.compile(r'(?<![A-Za-z#.-])([A-Za-zα-ωΔ]{1,2})_([A-Za-z0-9]+(?:,[A-Za-z0-9]+)?)')


def _svgsub(body):
    """V_C, L_w, l_t in labels drawn with real subscripts"""
    return _re.sub(r'(<text[^>]*>)(.*?)(</text>)', lambda m: m.group(1) + _SUBRX.sub(
        lambda n: n.group(1) + '<tspan baseline-shift="sub" font-size="11">' + n.group(2) + '</tspan>', m.group(2)) + m.group(3), body, flags=_re.S)


_spec = make_spec(FIG)


def spec(k):
    d = _spec(k)
    d['spec']['body'] = _svgsub(d['spec']['body'])
    d['caption'] = _SUBRX.sub(lambda n: n.group(1) + '<sub>' + n.group(2) + '</sub>', d['caption'])
    return d
