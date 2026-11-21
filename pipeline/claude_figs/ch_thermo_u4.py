"""Claude's hand-drawn figures for ch-thermo-u4 (Thermodynamic property relations), one per chapter, each drawn from that
chapter's own worked example. Steam data from IAPWS-IF97 and CO2 data from CoolProp, frozen below. Colours are the
shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def sp(base, s, size=11):
    return f'{base}<tspan baseline-shift="super" font-size="{size}">{s}</tspan>'


def path(pts, c=AC, w=2.5, dash=None, fill='none'):
    da = f';stroke-dasharray:{dash}' if dash else ''
    d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    return f'<path d="{d}" style="fill:{fill};stroke:{c};stroke-width:{w}{da};stroke-linejoin:round"/>'


# frozen data
LIQ = [(0.0, 0.01), (0.367, 25), (0.704, 50), (1.016, 75), (1.307, 100), (1.582, 125), (1.842, 150), (2.091, 175), (2.331, 200), (2.564, 225), (2.793, 250), (3.022, 275), (3.255, 300), (3.5, 325), (3.778, 350), (4.001, 365), (4.376, 373.9)]
VAP = [(9.155, 0.01), (8.557, 25), (8.075, 50), (7.681, 75), (7.354, 100), (7.077, 125), (6.837, 150), (6.624, 175), (6.43, 200), (6.249, 225), (6.072, 250), (5.894, 275), (5.706, 300), (5.491, 325), (5.211, 350), (4.948, 365), (4.45, 373.9)]
SUP10 = [(6.585, 179.9), (6.696, 200), (6.927, 250), (7.125, 300), (7.303, 350)]
ZCO2 = [(5, 0.9854), (10, 0.9706), (15, 0.9556), (20, 0.9404), (25, 0.9249), (30, 0.9092)]
PSAT = [(330, 17.21), (340, 27.19), (350, 41.68), (360, 62.19), (373.12, 101.31)]


# ---- 4.1 the four potentials and the boiling-water numbers ----
def f1():
    o = []
    o.append(T(170, 22, 'How the potentials are built', 15, bold=True))
    bx = {'U': (40, 50), 'H': (210, 50), 'A': (40, 190), 'G': (210, 190)}
    sub = {'U': 'internal energy', 'H': 'H = U + PV', 'A': 'A = U − TS', 'G': 'G = H − TS'}
    for k, (x, y) in bx.items():
        col = LV if k == 'G' else (AC if k == 'A' else L2)
        o.append(R(x, y, 100, 64, PANEL, col, 8))
        o.append(T(x + 50, y + 28, k, 20, bold=True)); o.append(T(x + 50, y + 50, sub[k], 12, fill=MUT))
    o.append(L(140, 82, 206, 82, AC, 2, arrow='n')); o.append(Tb(173, 76, '+PV', 13))
    o.append(L(140, 222, 206, 222, AC, 2, arrow='n')); o.append(Tb(173, 216, '+PV', 13))
    o.append(L(90, 114, 90, 186, AC, 2, arrow='n')); o.append(Tb(90, 154, '−TS', 13))
    o.append(L(260, 114, 260, 186, AC, 2, arrow='n')); o.append(Tb(260, 154, '−TS', 13))
    o.append(T(170, 290, 'fixed T, V: A falls to a minimum', 13, fill=MUT))
    o.append(T(170, 310, 'fixed T, P: G falls to a minimum', 13, fill=MUT))
    # bars, worked example 2
    o.append(L(352, 30, 352, 330, 'var(--line)', 1.5, '4 4'))
    o.append(T(540, 22, 'Boiling 1 mol of water at 1 atm', 15, bold=True))
    x0, x1 = 470, 690
    fx = lambda v: x0 + v / 45 * (x1 - x0)
    zero = fx(0)
    rows = [('ΔH', 40.65, L2), ('TΔS', 40.65, L2), ('ΔU', 37.60, AC), ('ΔG', 0.0, LV), ('ΔA', -3.05, NX)]
    fxa = lambda v: zero + v / 45 * (x1 - zero)
    for i, (lab, v, col) in enumerate(rows):
        y = 48 + i * 50
        o.append(T(460, y + 22, lab, 15, 'end', bold=True))
        if v >= 0:
            if v > 0: o.append(R(zero, y + 6, fxa(v) - zero, 24, ACS if col == AC else ('var(--line)' if col == L2 else LVS), col, 3))
            o.append(T(max(fxa(v), zero) + (-8 if v > 20 else 8), y + 23, f'{v:.2f} kJ' if v else '0 (equilibrium)', 13, 'end' if v > 20 else 'start', bold=True))
        else:
            w = 3.05 / 45 * (x1 - zero) * 4
            o.append(R(zero - w, y + 6, w, 24, NXS, NX, 3))
            o.append(T(zero + 8, y + 23, '−3.05 kJ = −PΔV', 13, 'start', NX, True))
    o.append(L(zero, 44, zero, 300, INK, 1.5))
    o.append(T(560, 322, 'ΔA bar drawn 4 × longer to be seen', 12, fill=MUT))
    return 340, ''.join(o)
FIG[1] = (f1, 'Left: adding PV turns U into H and A into G, and subtracting TS turns U into A and H into G. Right: the boiling-water example. At the normal boiling point TΔS equals ΔH, so ΔG = 0; ΔU is smaller than ΔH by the expansion work, and ΔA = −PΔV = −3.05 kJ is the only work available.',
          'A two-by-two box diagram of U, H, A and G joined by arrows labelled plus PV and minus TS, beside a bar chart for one mole of water boiling at 1 atm: ΔH and TΔS 40.65 kJ, ΔU 37.60 kJ, ΔG zero and ΔA minus 3.05 kJ.')


# ---- 4.2 internal energy of a van der Waals gas along the 300 K isotherm ----
def f2():
    o = []
    x0, x1, y0, y1 = 90, 470, 40, 300
    fx = lambda v: x0 + (v - 0) / 10.5 * (x1 - x0)
    fy = lambda u: y0 + (u - 0) / -400 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6, 8, 10], [0, -100, -200, -300, -400], fx, fy, 'molar volume V (L/mol)', 'U − U<tspan baseline-shift="super" font-size="11">ig</tspan> = −a/V (J/mol)', str, neg))
    pts = [(fx(v), fy(-364 / v)) for v in [0.91 + 0.05 * i for i in range(190)]]
    o.append(P(pts, AC, 3))
    o.append(L(x0, fy(0), x1, fy(0), L2, 2, '6 4')); o.append(T(x1 - 4, fy(0) + 18, 'ideal gas: ΔU = 0', 13, 'end', MUT))
    p1, p2 = (fx(1), fy(-364)), (fx(10), fy(-36.4))
    o.append(C(*p1, 6, AC)); o.append(C(*p2, 6, AC))
    o.append(T(p1[0] + 12, p1[1] - 10, '1: V = 1 L, −364 J/mol', 13, 'start', bold=True))
    o.append(T(fx(9.7), p2[1] + 24, '2: V = 10 L, −36.4 J/mol', 13, 'end', bold=True))
    o.append(L(fx(10.3), fy(-364), fx(10.3), fy(-40), LV, 2.5, arrow='l'))
    o.append(L(fx(1) + 6, fy(-364), fx(10.3), fy(-364), LV, 1.2, '3 3'))
    o.append(Tb(fx(10.1), fy(-200), 'ΔU = +327.6 J/mol', 14, 'end', LV, True))
    o.append(boxt(500, 50, 205, 230, ['CO₂ at 300 K', '(∂U/∂V)' + '<tspan baseline-shift="sub" font-size="11">T</tspan> = a/V²', 'ΔU = a(1/V₁ − 1/V₂)', '= 327.6 J/mol', 'ΔS = 19.47 J/(mol·K)', 'ideal: 19.14', 'ΔA = −5514 J/mol'], PANEL, L2, 14, True))
    return 350, ''.join(o)
FIG[2] = (f2, 'The worked example on one isotherm. A van der Waals gas has U − U<sup>ig</sup> = −a/V, so expanding CO<sub>2</sub> at 300 K from 1 L/mol to 10 L/mol raises its internal energy by 327.6 J/mol as the molecules move apart against their attraction; an ideal gas would show no change.',
          'A curve of minus a over V against molar volume from 1 to 10 litres per mole, rising from minus 364 to minus 36.4 joules per mole, with the rise of 327.6 joules per mole marked and the flat ideal-gas line at zero.')


# ---- 4.3 enthalpy of liquid water with pressure ----
def f3():
    o = []
    x0, x1, y0, y1 = 90, 470, 40, 300
    fx = lambda p: x0 + (p - 0) / 105 * (x1 - x0)
    fy = lambda h: y1 - h / 200 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [1, 20, 40, 60, 80, 100], [0, 50, 100, 150, 200], fx, fy, 'pressure P (bar), at 25 °C', 'H − H(1 bar) (J/mol)'))
    V, a, T0 = 18.07e-6, 2.573e-4, 298.15
    o.append(P([(fx(1), fy(0)), (fx(100), fy(V * 99e5))], L2, 2.5, '7 5'))
    o.append(P([(fx(1), fy(0)), (fx(100), fy(V * (1 - T0 * a) * 99e5))], AC, 3))
    o.append(C(fx(100), fy(178.9), 5, L2)); o.append(C(fx(100), fy(165.2), 6, AC)); o.append(C(fx(100), fy(164.5), 4, LV))
    o.append(T(fx(100) - 8, fy(178.9) - 10, 'VΔP = 178.9', 13, 'end', MUT))
    o.append(T(fx(98), fy(45), 'V(1 − Tα)ΔP = 165.2', 13, 'end', AC, True))
    o.append(T(fx(98), fy(22), 'gap TVαΔP is the Maxwell term', 13, 'end', MUT))
    o.append(boxt(500, 50, 205, 240, ['Water, 1 → 100 bar', '(∂S/∂P)' + '<tspan baseline-shift="sub" font-size="11">T</tspan> = −Vα', 'ΔS = −0.0460 J/(mol·K)', 'tables: −0.0469', '(∂H/∂P)' + '<tspan baseline-shift="sub" font-size="11">T</tspan> = V(1 − Tα)', 'ΔH = 165.2 J/mol', 'tables: 164.5'], PANEL, L2, 14, True))
    return 350, ''.join(o)
FIG[3] = (f3, 'Pumping liquid water at 25 °C from 1 to 100 bar. The Maxwell relation (∂S/∂P)<sub>T</sub> = −Vα gives the entropy term, which pulls the enthalpy rise down from VΔP = 178.9 J/mol to 165.2 J/mol, close to the steam-table value of 164.5 J/mol.',
          'Two straight lines of enthalpy rise against pressure from 1 to 100 bar: a dashed line reaching 178.9 joules per mole for V times delta P and a solid line reaching 165.2 joules per mole after the Maxwell-relation correction, with the table value 164.5 marked.')


# ---- 4.4 compressibility of CO2 at 350 K ----
def f4():
    o = []
    x0, x1, y0, y1 = 90, 470, 40, 300
    fx = lambda p: x0 + p / 32 * (x1 - x0)
    fy = lambda z: y1 - (z - 0.90) / 0.11 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 5, 10, 15, 20, 25, 30], [0.90, 0.92, 0.94, 0.96, 0.98, 1.00], fx, fy, 'pressure P (bar)', 'compressibility factor Z', str, lambda v: f'{v:.2f}'))
    o.append(L(fx(0), fy(1), fx(31), fy(1), L2, 2, '6 4')); o.append(T(fx(31), fy(1) - 8, 'ideal gas, Z = 1', 13, 'end', MUT))
    BPR = -0.24441891 / 1.15055884 / 73.83
    o.append(P([(fx(0), fy(1)), (fx(30), fy(1 + BPR * 30))], AC, 3))
    for p, z in ZCO2:
        o.append(C(fx(p), fy(z), 4.5, LV))
    o.append(C(fx(20), fy(0.9425), 6, AC))
    o.append(T(fx(20) - 10, fy(0.9425) - 12, 'virial: Z = 0.9425', 13, 'end', AC, True))
    o.append(T(fx(20) + 14, fy(0.9404) + 28, 'accurate: 0.9404', 13, 'start', LV, True))
    o.append(T(fx(6), fy(0.915), 'virial line Z = 1 + BP/RT', 13, 'start', AC))
    o.append(T(fx(6), fy(0.905), 'dots: accurate equation of state', 13, 'start', LV))
    o.append(boxt(500, 45, 205, 250, ['At 350 K, 20 bar', 'Gᴿ = RT ln φ = −167.5 J/mol', 'φ = 0.944', 'Hᴿ = −598.4 J/mol', 'Sᴿ = −1.231 J/(mol·K)', 'check: Hᴿ − TSᴿ', '= −167.5 J/mol'], PANEL, L2, 14, True))
    return 350, ''.join(o)
FIG[4] = (f4, 'The worked example for CO<sub>2</sub> at 350 K. The two-term virial equation with the Abbott correlation gives a straight line Z = 1 + BP/RT that runs just above the accurate values; at 20 bar Z = 0.9425 against 0.9404, and the residuals G<sup>R</sup>, H<sup>R</sup> and S<sup>R</sup> follow from B and dB/dT.',
          'Compressibility factor against pressure from 0 to 30 bar for carbon dioxide at 350 K: a dashed ideal-gas line at Z equals 1, a straight virial line falling to about 0.914 at 30 bar, and dots for accurate values close to it; the 20 bar point is marked with its residual properties.')


# ---- 4.5 T-s diagram of water with the two example states ----
def f5():
    o = []
    x0, x1, y0, y1 = 80, 500, 40, 320
    fx = lambda s: x0 + s / 9.4 * (x1 - x0)
    fy = lambda t: y1 - t / 400 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6, 8], [0, 100, 200, 300, 400], fx, fy, 'specific entropy s (kJ/(kg·K))', 'T (°C)'))
    dome = [(fx(s), fy(t)) for s, t in LIQ] + [(fx(s), fy(t)) for s, t in reversed(VAP)]
    o.append(P(dome, INK, 2.2))
    sf, sg, ts = 2.138, 6.585, 179.9
    o.append(P([(fx(sf), fy(ts)), (fx(sg), fy(ts))] + [(fx(s), fy(t)) for s, t in SUP10], AC, 3))
    o.append(T(fx(7.31) + 6, fy(350) + 4, '10 bar', 13, 'start', AC, True))
    s1 = sf + 0.9 * (sg - sf)
    o.append(C(fx(s1), fy(ts), 6, LV)); o.append(T(fx(s1) - 6, fy(ts) + 22, '1: x = 0.90', 13, 'end', LV, True))
    o.append(C(fx(6.840), fy(231.2), 6, NX)); o.append(T(fx(6.840) - 10, fy(231.2) - 8, '2: 231 °C', 13, 'end', NX, True))
    o.append(T(fx(3.7), fy(110), 'wet mixture', 13, fill=MUT))
    o.append(T(fx(4.37), fy(390), 'critical point 374 °C', 12, fill=MUT))
    o.append(T(fx(0.4), fy(120), 'liquid', 13, 'start', MUT))
    o.append(boxt(520, 50, 190, 260, ['Example 1 (wet)', 'h = 762.8 + 0.90 × 2015.3', '= 2576.6 kJ/kg', 'v = 0.1751 m³/kg', 'Example 2 (superheated)', 'h = 2900 kJ/kg', 'T = 231.2 °C', 's = 6.840 kJ/(kg·K)'], PANEL, L2, 13, True, fills=[INK, INK, INK, INK, INK, INK, INK, INK]))
    return 380, ''.join(o)
FIG[5] = (f5, 'Water on temperature–entropy axes with the saturation dome from IAPWS-IF97. The 10 bar line is flat at 179.9 °C across the dome and rises in the superheated region; state 1 is the wet steam of worked example 1 (x = 0.90) and state 2 the superheated steam of worked example 2 (231 °C).',
          'A temperature–entropy diagram of water with the saturation dome up to the critical point at 374 °C, the 10 bar line running flat at 179.9 °C across the dome then rising, a point at quality 0.90 on the flat part and a point at 231 °C in the superheated region.')


# ---- 4.6 ln P against 1/T for water ----
def f6():
    o = []
    x0, x1, y0, y1 = 90, 470, 40, 300
    fx = lambda r: x0 + (r - 2.65) / (3.08 - 2.65) * (x1 - x0)
    fy = lambda lp: y1 - (lp - 2.6) / (4.9 - 2.6) * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [2.7, 2.8, 2.9, 3.0], [3.0, 3.5, 4.0, 4.5], fx, fy, '1000/T (K⁻¹)', 'ln(P/kPa)', lambda v: f'{v:.1f}', lambda v: f'{v:.1f}'))
    lp1, r1 = math.log(101.325), 1000 / 373
    line = lambda r: lp1 - 4889.3 * (r - r1) / 1000
    o.append(P([(fx(2.66), fy(line(2.66))), (fx(3.06), fy(line(3.06)))], AC, 3))
    for t, p in PSAT:
        o.append(C(fx(1000 / t), fy(math.log(p)), 5, LV))
    o.append(T(fx(2.67), fy(2.85), 'slope = −ΔH/R = −4889 K', 13, 'start', AC, True))
    r2 = 1000 / 350
    o.append(L(fx(r2), fy(line(r2)), fx(r2) + 70, fy(line(r2)) - 50, L2, 1.2))
    o.append(Tb(fx(r2) + 74, fy(line(r2)) - 54, 'estimate 42.8 kPa', 13, 'start', AC, True))
    o.append(T(fx(r2) - 12, fy(math.log(41.68)) + 20, 'tables: 41.7 kPa at 350 K', 13, 'end', LV, True))
    o.append(T(fx(1000 / 373.12) + 12, fy(math.log(101.3)) - 10, '1 atm, 373 K', 13, 'start', INK))
    o.append(boxt(500, 50, 205, 230, ['Worked example 1', 'ΔH/R = 40 650/8.314', '= 4889.3 K', 'ln(P₂/P₁) = −0.8614', 'P₂ = 42.8 kPa', 'dots: steam tables', '330–373 K'], PANEL, L2, 14, True))
    return 350, ''.join(o)
FIG[6] = (f6, 'The Clausius–Clapeyron line for water, ln P against 1/T with slope −ΔH<sub>vap</sub>/R = −4889 K, drawn through the normal boiling point. Dots are steam-table pressures from 330 K to 373 K; the line predicts 42.8 kPa at 350 K against the true 41.7 kPa, because ΔH<sub>vap</sub> grows as the temperature falls.',
          'A straight falling line of the natural log of pressure in kilopascals against 1000 over T from 2.66 to 3.06, with five steam-table dots lying just below it at low temperature; the estimate of 42.8 kilopascals and the table value of 41.7 kilopascals at 350 K are labelled.')


# ---- 4.7 Cp - Cv for three fluids ----
def f7():
    o = []
    x0, x1 = 230, 600
    fx = lambda v: x0 + v / 16 * (x1 - x0)
    rows = [('liquid water, 300 K', 0.91, 'Tvα²/κ = 0.91', AC), ('ideal gas', 8.314, 'R = 8.314', L2), ('CO₂, van der Waals', 11.35, '11.35 = 1.37 R', AC), ('CO₂, accurate', 14.6, '14.6', LV)]
    o.append(T(360, 24, sb('C', 'P') + ' − ' + sb('C', 'V') + ' (J mol⁻¹ K⁻¹)', 15, bold=True))
    for i, (lab, v, txt, col) in enumerate(rows):
        y = 50 + i * 62
        o.append(T(x0 - 12, y + 26, lab, 14, 'end', bold=True))
        o.append(R(x0, y + 8, fx(v) - x0, 30, ACS if col == AC else ('var(--line)' if col == L2 else LVS), col, 3))
        o.append(T(fx(v) + 8, y + 28, txt, 13, 'start', bold=True))
    o.append(L(fx(8.314), 48, fx(8.314), 300, L2, 1.5, '5 4'))
    o.append(xaxis(x0, x1, 302, [0, 4, 8, 12, 16], fx))
    o.append(T(360, 350, 'CO₂ at 300 K and 1.00 L/mol (22.4 bar); water at 1 bar', 13, fill=MUT))
    return 370, ''.join(o)
FIG[7] = (f7, 'The two worked examples side by side with the ideal-gas value. Liquid water barely expands, so C<sub>P</sub> − C<sub>V</sub> is only 0.91 J mol⁻¹ K⁻¹; dense CO<sub>2</sub> gas exceeds R, 11.35 J mol⁻¹ K⁻¹ from the van der Waals equation and 14.6 from an accurate equation of state.',
          'A horizontal bar chart of Cp minus Cv: liquid water 0.91, ideal gas 8.314, carbon dioxide by van der Waals 11.35 and carbon dioxide accurate 14.6 joules per mole per kelvin, with a dashed line at R.')


# ---- 4.8 the Jacobian recipe for (dT/dP)_S ----
def f8():
    o = []
    def box(x, y, w, h, lines, col=AC, fill=PANEL):
        o.append(boxt(x, y, w, h, lines, fill, col, 14))
    S = lambda b, s: b + '<tspan baseline-shift="sub" font-size="11">' + s + '</tspan>'
    box(250, 16, 220, 48, ['target: (∂T/∂P)' + '<tspan baseline-shift="sub" font-size="11">S</tspan>'], AC, ACS)
    o.append(L(360, 64, 360, 86, AC, 2, arrow='n'))
    box(230, 90, 260, 48, ['ratio: J(T, S) / J(P, S)'])
    o.append(L(320, 138, 190, 176, AC, 2, arrow='n')); o.append(L(400, 138, 530, 176, AC, 2, arrow='n'))
    o.append(Tb(360, 166, 'expand both in (T, P)', 13, fill=MUT))
    box(40, 180, 300, 64, ['J(T, S) = (∂S/∂P)' + '<tspan baseline-shift="sub" font-size="11">T</tspan>', '= −(∂V/∂T)' + '<tspan baseline-shift="sub" font-size="11">P</tspan>  (Maxwell)'])
    box(380, 180, 300, 64, ['J(P, S) = −(∂S/∂T)' + '<tspan baseline-shift="sub" font-size="11">P</tspan>', '= −C' + '<tspan baseline-shift="sub" font-size="11">P</tspan>/T'])
    o.append(L(190, 244, 320, 280, AC, 2, arrow='n')); o.append(L(530, 244, 400, 280, AC, 2, arrow='n'))
    box(230, 284, 260, 48, ['(∂T/∂P)' + '<tspan baseline-shift="sub" font-size="11">S</tspan> = TVα / C' + '<tspan baseline-shift="sub" font-size="11">P</tspan>'], LV, LVS)
    o.append(L(360, 332, 360, 352, LV, 2, arrow='l'))
    o.append(T(360, 374, 'water, 25 °C: 1.84 × 10⁻⁸ K/Pa, so 1 → 100 bar warms it by 0.182 K', 14, bold=True))
    return 390, ''.join(o)
FIG[8] = (f8, 'Worked example 2 as a recipe. The target derivative is written as a ratio of two Jacobians with the held variable S in both, each Jacobian is expanded in (T, P), a Maxwell relation and C<sub>P</sub> = T(∂S/∂T)<sub>P</sub> remove the entropy, and the result TVα/C<sub>P</sub> is evaluated for water.',
          'A flow chart: the target derivative of T with respect to P at constant S becomes the ratio J of T and S over J of P and S; the two Jacobians expand to minus dV/dT at constant P and minus Cp over T; they combine to T V alpha over Cp, which gives 0.182 kelvin for water pumped from 1 to 100 bar.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
