"""Claude's hand-drawn figures for ch-thermo-u2 (PVT behaviour and equations of state), one per chapter.
Every number comes from that chapter's worked examples. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def poly(pts, fill, stroke='none', op=None, w=0):
    o = f';fill-opacity:{op}' if op is not None else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{w}{o}"/>'


# ---- 2.1 P–T diagram of water, pressure on a log scale ----
VAP = [(0.01, 0.00611), (10, 0.01228), (25, 0.03169), (50, 0.1235), (75, 0.3858), (100, 1.0142), (125, 2.321), (150, 4.76),
       (175, 8.92), (200, 15.54), (225, 25.5), (250, 39.76), (275, 59.5), (300, 85.8), (325, 120.8), (350, 165.2), (374, 220.6)]
SUB = [(-40, 0.000128), (-30, 0.000380), (-20, 0.00103), (-10, 0.00260), (0.01, 0.00611)]


def f1():
    o = []
    x0, x1, y0, y1 = 80, 520, 40, 330
    fx = lambda t: x0 + (t + 60) / 480 * (x1 - x0)
    fy = lambda p: y1 - (math.log10(p) + 4) / 7 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [-50, 0, 100, 200, 300, 400], [0.001, 0.01, 0.1, 1, 10, 100, 1000], fx, fy,
                  'Temperature T (°C)', 'Pressure P (bar), log scale', lambda t: neg(t), lambda p: f'{p:g}'))
    o.append(P([(fx(t), fy(p)) for t, p in SUB], NX, 3))
    o.append(P([(fx(t), fy(p)) for t, p in VAP], AC, 3.5))
    o.append(P([(fx(0.01), fy(0.00611)), (fx(-1), fy(10)), (fx(-3), fy(300)), (fx(-8), fy(1000))], LV, 3))
    # 1 bar line and the example's three states
    o.append(L(fx(-60), fy(1), fx(420), fy(1), INK, 1.6, '6 4'))
    o.append(Tb(fx(410), fy(1) - 8, '1 bar', 13, 'end', INK, True))
    for t, lab, col, dy in ((25, '25 °C liquid', AC, 22), (99.6, '99.6 °C boils', NX, -14), (120, '120 °C vapour', LV, 22)):
        o.append(C(fx(t), fy(1), 6, col))
        o.append(Tb(fx(t) + (8 if t > 100 else (-6 if 50 < t < 100 else 0)), fy(1) + dy, lab, 13, 'start' if t > 100 else 'end', col, True))
    o.append(C(fx(0.01), fy(0.00611), 6, INK))
    o.append(Tb(fx(8), fy(0.00611) + 20, 'triple point 0.01 °C, 0.00611 bar', 13, 'start', INK, True))
    o.append(C(fx(374), fy(220.6), 6, INK))
    o.append(Tb(fx(370), fy(220.6) - 12, 'critical point 374 °C, 221 bar', 13, 'end', INK, True))
    o.append(T(fx(-30), fy(30), 'solid', 15, 'middle', MUT, True))
    o.append(T(fx(90), fy(60), 'liquid', 15, 'middle', MUT, True))
    o.append(T(fx(250), fy(0.05), 'vapour', 15, 'middle', MUT, True))
    o.append(boxt(536, 60, 176, 50, ['vaporisation', 'liquid | vapour'], PANEL, AC, 13, True))
    o.append(boxt(536, 124, 176, 50, ['fusion', 'solid | liquid'], PANEL, LV, 13, True))
    o.append(boxt(536, 188, 176, 50, ['sublimation', 'solid | vapour'], PANEL, NX, 13, True))
    o.append(boxt(536, 252, 176, 66, ['fusion line leans left:', 'ice melts when', 'squeezed'], LVS, LV, 13))
    return 380, ''.join(o)
FIG[1] = (f1, 'The P–T diagram of water with pressure on a log scale, so both the triple point (0.00611 bar) and the critical point (221 bar) fit. Worked example 1 sits on the 1 bar line: 25 °C is liquid, 99.6 °C is on the vaporisation curve where liquid and vapour coexist, and 120 °C is vapour.',
          'Pressure on a log scale from 0.0001 to 1000 bar against temperature from minus 60 to 420 degrees Celsius. The sublimation curve rises to the triple point at 0.01 degrees and 0.00611 bar; from there the vaporisation curve rises to the critical point at 374 degrees and 221 bar, and the nearly vertical fusion line leans slightly left. A dashed line at 1 bar carries three marked states: 25 degrees liquid, 99.6 degrees boiling and 120 degrees vapour.')


# ---- 2.2 three compression paths from 24.94 L to 12.47 L ----
def f2():
    o = []
    x0, x1, y0, y1 = 80, 480, 40, 320
    fx = lambda v: x0 + (v - 10) / 16 * (x1 - x0)
    fy = lambda p: y1 - p / 3 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [10, 12, 14, 16, 18, 20, 22, 24, 26], [0, 0.5, 1, 1.5, 2, 2.5, 3], fx, fy, 'Volume V (L), 1 mol', 'Pressure P (bar)',
                  str, lambda p: f'{p:g}'))
    vs = [12.47 + i * (24.94 - 12.47) / 60 for i in range(61)]
    o.append(P([(fx(v), fy(24.94 / v)) for v in vs], AC, 3))
    o.append(P([(fx(v), fy((24.94 / v) ** 1.4)) for v in vs], NX, 3, '8 4'))
    o.append(P([(fx(12.47), fy(1)), (fx(24.94), fy(1))], LV, 3))
    o.append(C(fx(24.94), fy(1), 6, INK))
    o.append(T(fx(24.94), fy(1) + 24, '1: 24.94 L, 1.00 bar, 300 K', 13, 'end', INK, True))
    for p, lab, col in ((2.64, '2.64 bar, 396 K', NX), (2.00, '2.00 bar, 300 K', AC), (1.00, '1.00 bar, 150 K', LV)):
        o.append(C(fx(12.47), fy(p), 6, col))
        o.append(Tb(fx(12.47) + 10, fy(p) - 9, lab, 13, 'start', col, True))
    o.append(L(fx(12.47), fy(0), fx(12.47), fy(2.9), L2, 1.2, '3 4'))
    o.append(Tb(fx(12.47) + 8, fy(0.25), 'V₂ = 12.47 L', 13, 'start', INK, True))
    o.append(boxt(500, 50, 210, 64, ['adiabatic (dashed)', 'PV<tspan baseline-shift="super" font-size="10">γ</tspan> = const, γ = 1.4'], PANEL, NX, 14, True))
    o.append(boxt(500, 128, 210, 64, ['isothermal', 'PV = const'], PANEL, AC, 14, True))
    o.append(boxt(500, 206, 210, 64, ['isobaric', 'P = 1.00 bar'], PANEL, LV, 14, True))
    o.append(boxt(500, 284, 210, 50, ['halving V doubles P', 'only if T stays fixed'], ACS, AC, 13))
    return 380, ''.join(o)
FIG[2] = (f2, 'Worked example 1 on a P–V plot: 1 mol at 300 K is squeezed from 24.94 L to 12.47 L. The isothermal path ends at 2.00 bar, the adiabatic path at 2.64 bar because compression heats the gas to 396 K, and the isobaric path stays at 1.00 bar because the gas is cooled to 150 K.',
          'Pressure from 0 to 3 bar against volume from 10 to 26 litres. From the start point at 24.94 litres and 1 bar, a solid isothermal curve rises to 2.00 bar at 12.47 litres, a dashed adiabatic curve rises more steeply to 2.64 bar at 396 kelvin, and a flat isobaric line stays at 1.00 bar, ending at 150 kelvin.')


# ---- 2.3 CO2 at 300 K: ideal gas against van der Waals ----
def vdw(V, T=300.0, a=3.640, b=0.04267):
    return 0.08314 * T / (V - b) - a / V ** 2


def f3():
    o = []
    x0, x1, y0, y1 = 80, 480, 40, 320
    fx = lambda v: x0 + (v - 0.3) / 1.7 * (x1 - x0)
    fy = lambda p: y1 - p / 90 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0.3, 0.6, 1.0, 1.4, 1.8, 2.0], [0, 20, 40, 60, 80], fx, fy, 'Molar volume V (L/mol)', 'Pressure P (bar)', lambda v: f'{v:g}'))
    vs = [0.3 + i * 1.7 / 120 for i in range(121)]
    o.append(P([(fx(v), fy(24.942 / v)) for v in vs if 24.942 / v <= 90], AC, 3))
    o.append(P([(fx(v), fy(vdw(v))) for v in vs], NX, 3, '8 4'))
    # example 1: V = 1 L/mol
    o.append(L(fx(1.0), fy(0), fx(1.0), fy(24.94), L2, 1.2, '3 4'))
    o.append(C(fx(1.0), fy(24.94), 6, AC)); o.append(Tb(fx(1.0) + 10, fy(24.94) - 10, 'ideal 24.94 bar', 13, 'start', AC, True))
    o.append(C(fx(1.0), fy(22.41), 6, NX)); o.append(Tb(fx(1.0) - 10, fy(22.41) + 24, 'van der Waals 22.41 bar', 13, 'end', NX, True))
    # example 2: P = 40 bar
    o.append(L(fx(0.3), fy(40), fx(0.95), fy(40), INK, 1.6, '6 4'))
    o.append(T(fx(0.95) + 6, fy(40) + 5, '40 bar', 13, 'start', INK, True))
    o.append(C(fx(0.4996), fy(40), 6, NX)); o.append(Tb(fx(0.4996) - 4, fy(40) + 22, '0.4996', 13, 'middle', NX, True))
    o.append(C(fx(0.6236), fy(40), 6, AC)); o.append(Tb(fx(0.6236) + 8, fy(40) - 12, '0.6236 L/mol', 13, 'start', AC, True))
    o.append(boxt(500, 50, 210, 64, ['ideal gas', 'P = RT/V'], PANEL, AC, 14, True))
    o.append(boxt(500, 128, 210, 80, ['van der Waals (dashed)', 'a = 3.640 L²·bar/mol²', 'b = 0.04267 L/mol'], PANEL, NX, 13, True))
    o.append(boxt(500, 222, 210, 80, ['at 40 bar the real gas', 'takes 20 % less room:', 'Z = 0.801'], NXS, NX, 13))
    return 380, ''.join(o)
FIG[3] = (f3, 'CO₂ at 300 K. At V = 1 L/mol (worked example 1) the ideal-gas law gives 24.94 bar and van der Waals 22.41 bar. At 40 bar (worked example 2) the ideal gas needs 0.6236 L/mol but the van der Waals root is 0.4996 L/mol, so Z = 0.801.',
          'Pressure from 0 to 90 bar against molar volume from 0.3 to 2 litres per mole for carbon dioxide at 300 kelvin. The solid ideal-gas curve lies above the dashed van der Waals curve. At 1 litre per mole the points are 24.94 and 22.41 bar. A dashed line at 40 bar meets the van der Waals curve at 0.4996 and the ideal curve at 0.6236 litres per mole.')


# ---- 2.4 generalized Z at Tr = 1.2: Peng-Robinson against the Pitzer virial line ----
def zpr(Tr, Pr, w=0.2):
    eps, sig, Om, Ps = 1 - 2 ** .5, 1 + 2 ** .5, 0.07780, 0.45724
    al = (1 + (0.37464 + 1.54226 * w - 0.26992 * w * w) * (1 - Tr ** .5)) ** 2
    beta, q, Z = Om * Pr / Tr, Ps * al / (Om * Tr), 1.0
    for _ in range(400):
        Z = 1 + beta - q * beta * (Z - beta) / ((Z + eps * beta) * (Z + sig * beta))
    return Z


def f4():
    o = []
    x0, x1, y0, y1 = 80, 480, 40, 320
    fx = lambda pr: x0 + pr / 3 * (x1 - x0)
    fy = lambda z: y1 - (z - 0.4) / 0.7 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 1, 1.5, 2, 2.5, 3], [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1], fx, fy, 'Reduced pressure P<tspan baseline-shift="sub" font-size="10">r</tspan>',
                  'Compressibility factor Z', lambda v: f'{v:g}', lambda v: f'{v:.1f}'))
    o.append(L(fx(0), fy(1), fx(3), fy(1), MUT, 1.6, '3 4'))
    o.append(T(fx(2.95), fy(1) - 8, 'ideal gas Z = 1', 13, 'end', MUT, True))
    prs = [i * 3 / 90 for i in range(91)]
    o.append(P([(fx(p), fy(zpr(1.2, p))) for p in prs], AC, 3))
    k = (0.083 - 0.422 / 1.2 ** 1.6 + 0.2 * (0.139 - 0.172 / 1.2 ** 4.2)) / 1.2
    o.append(P([(fx(0), fy(1)), (fx(1.2), fy(1 + k * 1.2))], NX, 3, '8 4'))
    o.append(P([(fx(1.2), fy(1 + k * 1.2)), (fx(2.2), fy(1 + k * 2.2))], NX, 1.5, '2 5'))
    o.append(C(fx(0.659), fy(0.879), 6, NX)); o.append(Tb(fx(0.659) + 12, fy(0.879) - 12, 'n-butane: virial 0.879', 13, 'start', NX, True))
    o.append(C(fx(0.659), fy(0.858), 6, AC)); o.append(Tb(fx(0.659) - 10, fy(0.858) + 22, 'PR 0.858', 13, 'end', AC, True))
    o.append(C(fx(2.0), fy(0.61), 6, LV)); o.append(Tb(fx(2.0) + 10, fy(0.61) - 14, 'example 1: Z = 0.61', 13, 'start', LV, True))
    o.append(boxt(500, 50, 210, 80, ['Peng–Robinson', 'T<tspan baseline-shift="sub" font-size="10">r</tspan> = 1.2, ω = 0.20', 'any gas, any P<tspan baseline-shift="sub" font-size="10">r</tspan>'], PANEL, AC, 13, True))
    o.append(boxt(500, 144, 210, 80, ['Pitzer virial (dashed)', 'Z = 1 + (B⁰ + ωB¹)P<tspan baseline-shift="sub" font-size="10">r</tspan>/T<tspan baseline-shift="sub" font-size="10">r</tspan>', 'straight line in P<tspan baseline-shift="sub" font-size="10">r</tspan>'], PANEL, NX, 13, True))
    o.append(boxt(500, 238, 210, 66, ['the line bends away', 'from the curve above', 'P<tspan baseline-shift="sub" font-size="10">r</tspan> ≈ 1: stop using it'], NXS, NX, 13))
    return 380, ''.join(o)
FIG[4] = (f4, 'Z against reduced pressure at T<sub>r</sub> = 1.2 for ω = 0.20, from the generalized Peng–Robinson equation (solid) and the Pitzer virial correlation (dashed). They agree at low P<sub>r</sub>: worked example 2 (n-butane, P<sub>r</sub> = 0.659) gives 0.879 and 0.858. Beyond P<sub>r</sub> ≈ 1 the straight virial line drifts away, and only the chart or the cubic gives example 1\'s Z = 0.61 at P<sub>r</sub> = 2.',
          'Compressibility factor from 0.4 to 1.1 against reduced pressure from 0 to 3 at reduced temperature 1.2. A dotted line at Z equals 1 marks the ideal gas. The solid Peng-Robinson curve falls from 1 to about 0.58 near Pr 2.5 and turns up slightly; the dashed Pitzer virial straight line follows it at low pressure and drifts away from it after Pr 1. Points mark n-butane at Pr 0.659 with Z 0.879 and 0.858, and example 1 at Pr 2 with Z 0.61.')


# ---- 2.5 enthalpy path of 1 kg of water from ice at −10 °C to steam at 120 °C ----
def f5():
    o = []
    x0, x1, y0, y1 = 80, 470, 40, 320
    fx = lambda t: x0 + (t + 20) / 150 * (x1 - x0)
    fy = lambda h: y1 - h / 3200 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 20, 40, 60, 80, 100, 120], [0, 500, 1000, 1500, 2000, 2500, 3000], fx, fy, 'Temperature T (°C)', 'H relative to ice at −10 °C (kJ/kg)', neg))
    pts = [(-10, 0), (0, 20.9), (0, 354.9), (100, 772.9), (100, 3032.9), (120, 3073.1)]
    o.append(P([(fx(t), fy(h)) for t, h in pts[:2]], NX, 3.5))
    o.append(P([(fx(t), fy(h)) for t, h in pts[1:3]], LV, 5))
    o.append(P([(fx(t), fy(h)) for t, h in pts[2:4]], AC, 3.5))
    o.append(P([(fx(t), fy(h)) for t, h in pts[3:5]], LV, 5))
    o.append(P([(fx(t), fy(h)) for t, h in pts[4:6]], NX, 3.5))
    for t, h in pts:
        o.append(C(fx(t), fy(h), 4.5, INK))
    o.append(Tb(fx(4), fy(250), 'melt +334', 13, 'start', LV, True))
    o.append(Tb(fx(52), fy(560) - 18, 'water +418', 13, 'middle', AC, True))
    o.append(Tb(fx(98), fy(1900), 'boil 2260', 13, 'end', LV, True))
    o.append(Tb(fx(4), fy(80), '← ice +20.9', 13, 'start', NX, True))
    o.append(Tb(fx(108), fy(3073) + 22, 'steam +40.2', 13, 'middle', NX, True))
    o.append(boxt(490, 50, 220, 64, ['vertical jump', 'latent heat, T fixed'], PANEL, LV, 14, True))
    o.append(boxt(490, 128, 220, 64, ['sloping stretch', 'sensible heat, T rises'], PANEL, AC, 14, True))
    o.append(boxt(490, 206, 220, 80, ['total 3073.1 kJ/kg', 'latent 2594 kJ/kg', '= 84.4 %'], NXS, NX, 14, True))
    return 380, ''.join(o)
FIG[5] = (f5, 'Worked example 1 as an enthalpy–temperature path for 1 kg of water, with H = 0 for ice at −10 °C (relative values, not steam-table enthalpies). Each vertical jump is latent heat at a fixed temperature and each sloping stretch is sensible heat; boiling alone is 2260 of the 3073.1 kJ/kg.',
          'Enthalpy from 0 to 3200 kilojoules per kilogram against temperature from minus 20 to 130 degrees Celsius. The path rises gently from minus 10 to 0 degrees by 20.9, jumps straight up by 334 at 0 degrees, slopes up by 418 to 100 degrees, jumps straight up by 2260 at 100 degrees, and ends with a short slope of 40.2 to 120 degrees, a total of 3073.1.')

spec = make_spec(FIG)
