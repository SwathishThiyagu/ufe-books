"""Claude's hand-drawn figures for me-thermo-u1 (Engineering Thermodynamics: basic concepts, zeroth law, work and heat),
one per chapter, drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sub(s):
    return s


# ---- 1.1 the continuum: density read from smaller and smaller cubes of room air ----
def f1():
    o = []
    x0, x1, y0, y1 = 100, 690, 50, 330
    lo, hi = math.log10(10e-9), math.log10(10e-6)
    fx = lambda s: x0 + (math.log10(s) - lo) / (hi - lo) * (x1 - x0)
    ymin, ymax = 0.85, 1.50
    fy = lambda r: y1 - (r - ymin) / (ymax - ymin) * (y1 - y0)
    rho, n = 1.177, 2.446e25
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (0.9, 1.0, 1.1, 1.2, 1.3, 1.4):
        o += [L(x0 - 5, fy(v), x0, fy(v), L2, 1.5), T(x0 - 9, fy(v) + 4.5, f'{v:.1f}', 13, 'end', MUT)]
    for s, lab in ((10e-9, '10 nm'), (100e-9, '100 nm'), (1e-6, '1 µm'), (10e-6, '10 µm')):
        o += [L(fx(s), y1, fx(s), y1 + 5, L2, 1.5), T(fx(s), y1 + 20, lab, 13, fill=MUT)]
    o.append(T((x0 + x1) / 2, y1 + 42, 'side of the sample cube (log scale)', 14, fill=MUT))
    o.append(T(x0 - 80, y0 - 18, 'δm/δV read in the cube (kg/m³)', 14, 'start', MUT))
    # band rho(1 ± 1/sqrt(N)) with N = n s³
    ss = [10 ** (lo + (hi - lo) * i / 120) for i in range(121)]
    top = [(fx(s), fy(rho * (1 + 1 / math.sqrt(n * s ** 3)))) for s in ss]
    bot = [(fx(s), fy(rho * (1 - 1 / math.sqrt(n * s ** 3)))) for s in reversed(ss)]
    top = [(x, max(y, y0)) for x, y in top]
    o.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in top + bot)}" style="fill:var(--next-soft);stroke:var(--next);stroke-width:1.5"/>')
    o.append(L(x0, fy(rho), x1, fy(rho), AC, 2.5, '8 5'))
    o.append(Tb(x1 - 4, fy(rho) - 10, 'continuum value ρ = 1.177 kg/m³', 14, 'end', AC, bold=True))
    # mean free path marker
    lam = 67.2e-9
    o.append(L(fx(lam), y0 + 30, fx(lam), y1, MUT, 1.5, '3 4'))
    o.append(Tb(fx(lam) + 6, y0 + 40, 'mean free path 67 nm', 13, 'start', MUT))
    o.append(Tb(fx(14e-9) + 4, fy(1.47) + 4, '±20 % at 10 nm', 13, 'start', NX, bold=True))
    o.append(Tb(fx(1e-6), fy(1.03), 'at 1 µm: 2.45 × 10⁷ molecules, ±0.02 %', 13, 'middle', INK))
    return 390, ''.join(o)


FIG[1] = (f1, 'Room air at 300 K and 101.325 kPa, sampled with cubes of shrinking size. The shaded band is the spread ρ(1 ± 1/√N) '
              'for N molecules in the cube: above about 1 µm every cube gives the same density, so the continuum holds; near 10 nm the '
              'reading jumps by about 20 %.',
          'A plot of measured density against cube side from 10 nanometres to 10 micrometres. A shaded band is wide on the left, about 20 percent '
          'at 10 nm, and shrinks to a thin line at the continuum value 1.177 kilograms per cubic metre on the right. A dotted line marks the mean free path, 67 nm.')


# ---- 1.2 one tank, two boundaries ----
def tank(cx, top, fill_h, label_lines, col):
    o = [R(cx - 80, top, 160, 150, PANEL, INK, 14, 2.5)]
    o.append(R(cx - 74, top + 150 - fill_h - 6, 148, fill_h, ACS if col == AC else LVS, 'none', 10, 0))
    o.append(L(cx + 80, top + 40, cx + 120, top + 40, INK, 6))
    o.append(R(cx + 104, top + 30, 14, 20, PANEL, INK, 3, 2))
    for i, s in enumerate(label_lines):
        o.append(T(cx, top + 72 + i * 19, s, 14, bold=(i == 0)))
    return ''.join(o)


def f2():
    o = []
    # left: boundary A = the tank (control volume)
    cx, top = 175, 70
    o.append(T(cx + 20, 30, 'Boundary A: the tank wall and valve', 14, bold=True, fill=AC))
    o.append(T(cx + 20, 50, 'open system (control volume)', 13, fill=MUT))
    o.append(tank(cx, top, 120, ['air', '2.0 kg → 1.5 kg'], AC))
    o.append(R(cx - 92, top - 12, 222, 174, 'none', AC, 16, 2.2, '7 5'))
    o.append(L(cx + 120, top + 40, cx + 190, top + 40, NX, 3, arrow='x'))
    o.append(T(cx + 164, top + 25, '0.50 kg', 13, fill=NX, bold=True))
    o.append(T(cx + 164, top + 62, 'mass out', 13, fill=NX))
    o.append(L(cx, top + 162, cx, top + 212, NX, 3, arrow='x'))
    o.append(T(cx + 16, top + 196, 'Q = 30 kJ out', 14, 'start', NX, bold=True))
    # right: boundary B = the air that stays (control mass)
    cx2 = 520
    o.append(T(cx2 + 10, 30, 'Boundary B: the 1.5 kg that stays', 14, bold=True, fill=LV))
    o.append(T(cx2 + 10, 50, 'closed system (control mass)', 13, fill=MUT))
    o.append(tank(cx2, top, 120, ['air', '1.5 kg stays'], LV))
    o.append(R(cx2 - 70, top + 28, 140, 108, 'none', LV, 30, 2.2, '7 5'))
    o.append(T(cx2, top + 22, 'boundary moves', 13, fill=LV))
    o.append(T(cx2, top + 129, 'and expands', 13, fill=LV))
    o.append(L(cx2, top + 162, cx2, top + 212, NX, 3, arrow='x'))
    o.append(T(cx2 + 16, top + 196, 'heat out', 14, 'start', NX, bold=True))
    o.append(T(360, 318, 'No mass crosses boundary B, but its volume grows as the air pushes the escaping 0.50 kg out.', 13, fill=MUT))
    o.append(T(360, 338, 'Isolated would need no mass, no heat and no work across the boundary: neither choice is isolated.', 13, fill=MUT))
    return 352, ''.join(o)


FIG[2] = (f2, 'The worked example’s rigid tank seen with two boundaries. Drawn around the tank (A), the boundary is fixed and 0.50 kg of air '
              'crosses it, so the system is open. Drawn around the 1.5 kg that stays (B), no mass crosses, so it is a closed system whose boundary moves.',
          'Two drawings of the same tank with a valve. Left: a dashed boundary around the whole tank, with 0.50 kg of air leaving through the valve '
          'and 30 kJ of heat leaving through the wall. Right: a dashed boundary around only the air that stays, 1.5 kg, which grows as the air expands.')


# ---- 1.3 the rectangle cycle on a p-V diagram ----
def f3():
    o = []
    x0, x1, y0, y1 = 110, 520, 60, 330
    fx = lambda V: x0 + (V - 0.15) / 0.20 * (x1 - x0)
    fy = lambda p: y1 - (p - 50) / 200 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0.15, 0.20, 0.25, 0.30, 0.35], [50, 100, 150, 200, 250], fx, fy,
                  'V (m³)', 'p (kPa)', xfmt=lambda v: f'{v:.2f}'))
    pts = {1: (0.20, 100), 2: (0.20, 200), 3: (0.30, 200), 4: (0.30, 100)}
    X = {k: (fx(v), fy(p)) for k, (v, p) in pts.items()}
    o.append(f'<rect x="{X[2][0]:.1f}" y="{X[2][1]:.1f}" width="{X[3][0] - X[2][0]:.1f}" height="{X[1][1] - X[2][1]:.1f}" style="fill:var(--accent-soft);stroke:none"/>')
    o.append(T((X[1][0] + X[3][0]) / 2, (X[1][1] + X[3][1]) / 2 + 5, 'net work 10 kJ', 14, bold=True, fill=AC))
    o.append(L(*X[1], *X[2], LV, 3, arrow='l'))
    o.append(L(*X[2], *X[3], LV, 3, arrow='l'))
    o.append(L(*X[3], *X[4], NX, 3, arrow='x'))
    o.append(L(*X[4], *X[1], NX, 3, arrow='x'))
    lab = {1: ('1', '300 K', -14, 22), 2: ('2', '600 K', -14, -12), 3: ('3', '900 K', 14, -12), 4: ('4', '450 K', 14, 22)}
    for k, (n, t, dx, dy) in lab.items():
        o.append(C(*X[k], 7, INK))
        o.append(T(X[k][0] + dx, X[k][1] + dy, f'{n}: {t}', 14, 'end' if dx < 0 else 'start', bold=True))
    # side panel
    o.append(boxt(548, 70, 162, 108, ['path 1→2→3', 'W = 0 + 20', '= 20 kJ'], LVS, LV, 14, True))
    o.append(boxt(548, 196, 162, 108, ['path 1→4→3', 'W = −10 + 0', '= −10 kJ'], NXS, NX, 14, True))
    o.append(T(629, 330, 'both: ΔT = +600 K', 14, bold=True))
    return 390, ''.join(o)


FIG[3] = (f3, 'The worked example’s cycle for 0.2323 kg of air: four states, each a point fixed by p and V, with its temperature from pV = mRT. '
              'The two routes from state 1 to state 3 give the same temperature rise but different work, and the loop encloses a net work of 10 kJ.',
          'A pressure–volume diagram with a rectangle: state 1 at 0.20 cubic metres and 100 kPa (300 K), state 2 at 0.20 and 200 kPa (600 K), '
          'state 3 at 0.30 and 200 kPa (900 K), state 4 at 0.30 and 100 kPa (450 K). The enclosed area, 10 kJ, is shaded.')


# ---- 1.4 piston in equilibrium and the sand-grain compression ----
def f4():
    o = []
    # left: piston sketch with force balance
    cx = 130
    o.append(T(cx, 26, 'Forces on the piston', 14, bold=True))
    o.append(P([(cx - 70, 70), (cx - 70, 290), (cx + 70, 290), (cx + 70, 70)], INK, 3))
    o.append(R(cx - 66, 170, 132, 116, ACS, 'none', 2, 0))
    o.append(R(cx - 68, 150, 136, 20, PANEL, INK, 3, 2.5))
    o.append(R(cx - 40, 120, 80, 30, LVS, LV, 4, 2))
    o.append(T(cx, 141, 'sand', 13, fill=LV, bold=True))
    o.append(T(cx, 232, 'gas  p', 14, bold=True, fill=AC))
    o.append(L(cx - 30, 205, cx - 30, 176, AC, 2.5, arrow='n'))
    o.append(L(cx + 30, 205, cx + 30, 176, AC, 2.5, arrow='n'))
    o.append(L(cx, 44, cx, 112, MUT, 2.5, arrow='m'))
    o.append(T(cx + 8, 56, 'pₐₜₘA + (m + mₛ)g', 13, 'start', MUT))
    o.append(T(cx, 312, 'piston D = 100 mm, m = 50 kg', 13, fill=MUT))
    o.append(T(cx, 332, 'pA = pₐₜₘA + (m + mₛ)g', 14, bold=True))
    # right: p-V plot
    x0, x1, y0, y1 = 340, 690, 50, 290
    fx = lambda V: x0 + (V - 0.80) / 0.24 * (x1 - x0)
    fy = lambda p: y1 - (p - 150) / 55 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0.80, 0.85, 0.90, 0.95, 1.00], [160, 170, 180, 190, 200], fx, fy, 'V (litres)', 'p (kPa)', xfmt=lambda v: f'{v:.2f}'))
    C0 = 163.7774
    A = math.pi * 0.1 ** 2 / 4
    pts = []
    for m in range(0, 30, 5):
        p = 101.325 + (50 + m) * 9.81 / A / 1000
        pts.append((C0 / p, p))
    (va, pa), (vb, pb) = pts[0], pts[5]
    o.append(arc(fx(va), fy(pa), fx(vb), fy(pb), -0.3, NX, 2, None, '3 5'))
    o.append(P([(fx(v / 1000), fy(C0 / (v / 1000))) for v in range(830, 1011)], AC, 2.5))
    for i, (v, p) in enumerate(pts):
        o.append(C(fx(v), fy(p), 6, LV if 0 < i < 5 else NX))
    o.append(Tb(fx(va), fy(pa) + 24, '1: 163.78 kPa, 1.000 L', 13, 'end', NX, bold=True))
    o.append(Tb(fx(vb) - 16, fy(pb) - 16, '2: 195.00 kPa, 0.840 L', 13, 'start', NX, bold=True))
    o.append(T(x0 + 12, fy(168), 'dots: one equilibrium state', 13, 'start', LV))
    o.append(T(x0 + 12, fy(168) + 18, 'per 5 kg of sand, on pV = 163.8 J', 13, 'start', LV))
    for i, s_ in enumerate(('all 25 kg at once:', 'no single p', 'between 1 and 2')):
        o.append(Tb(640, fy(191) + i * 18, s_, 13, 'middle', NX))
    return 350, ''.join(o)


FIG[4] = (f4, 'Left: the piston is at rest when the gas force pA balances the atmosphere, the piston and the sand. Right: the worked example’s '
              'states. Adding sand 5 kg at a time gives equilibrium points on the curve pV = constant; dumping all 25 kg at once links the same '
              'end states 1 and 2 by states that have no single pressure, so no line can be drawn.',
          'Left: a cylinder with a piston carrying sand; arrows show the gas pressure pushing up and the atmosphere, piston and sand weight pushing down. '
          'Right: a p–V plot with six dots from 163.78 kPa at 1.000 litre to 195.00 kPa at 0.840 litre lying on a smooth curve, and a dotted wiggle for the sudden process.')


# ---- 1.5 zeroth law and the thermocouple calibration ----
def f5():
    o = []
    # top: A, B, thermometer C
    o.append(boxt(40, 40, 140, 56, ['body A', '25.0 °C'], ACS, AC, 14, True))
    o.append(boxt(290, 40, 140, 56, ['body B', '25.0 °C'], ACS, AC, 14, True))
    o.append(boxt(165, 140, 140, 56, ['thermometer C'], LVS, LV, 14, True))
    o.append(L(120, 98, 190, 138, LV, 2.5)); o.append(L(350, 98, 280, 138, LV, 2.5))
    o.append(T(126, 128, 'equilibrium', 13, 'end', LV)); o.append(T(344, 128, 'equilibrium', 13, 'start', LV))
    o.append(L(182, 68, 288, 68, NX, 2.5, '7 5'))
    o.append(Tb(235, 62, 'so A ~ B', 13, 'middle', NX, bold=True))
    o.append(T(470, 60, 'Zeroth law:', 14, 'start', bold=True))
    o.append(T(470, 82, 'A ~ C and B ~ C', 14, 'start'))
    o.append(T(470, 104, 'give A ~ B,', 14, 'start'))
    o.append(T(470, 126, 'so no heat flows', 14, 'start'))
    o.append(T(470, 148, 'when A touches B.', 14, 'start'))
    # bottom: thermocouple emf against gas-thermometer temperature
    x0, x1, y0, y1 = 100, 600, 250, 470
    fx = lambda t: x0 + t / 100 * (x1 - x0)
    fy = lambda e: y1 - e / 20 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 25, 50, 75, 100], [0, 5, 10, 15, 20], fx, fy, 'gas-thermometer temperature t (°C)', 'emf e (mV)'))
    e = lambda t: 0.20 * t - 5e-4 * t * t
    o.append(P([(fx(t), fy(e(t))) for t in range(0, 101)], AC, 3))
    o.append(P([(fx(0), fy(0)), (fx(100), fy(15))], MUT, 2, '7 5'))
    o.append(C(fx(50), fy(8.75), 6, NX)); o.append(C(fx(58.33), fy(8.75), 6, LV))
    o.append(L(fx(50), fy(8.75), fx(58.33), fy(8.75), NX, 2))
    o.append(L(fx(58.33), fy(8.75), fx(58.33), y1, LV, 1.5, '3 4'))
    o.append(Tb(fx(50) - 10, fy(8.75) - 12, 'true 50 °C: 8.75 mV', 13, 'end', NX, bold=True))
    o.append(Tb(fx(58.33) + 8, fy(8.75) + 24, 'meter shows 58.33 °C', 13, 'start', LV, bold=True))
    o.append(Tb(fx(100) - 4, fy(19.0), 'e = 0.20t − 0.0005t²', 13, 'end', AC, bold=True))
    o.append(Tb(fx(78), fy(8.2), 'linear scale through 0 and 15 mV', 13, 'start', MUT))
    o.append(C(fx(100), fy(15), 5, INK)); o.append(T(fx(100) + 10, fy(15) + 5, '15 mV', 13, 'start', MUT))
    return 520, ''.join(o)


FIG[5] = (f5, 'Top: the zeroth law as the worked example uses it; one thermometer agrees with A and with B, so A and B are at the same temperature. '
              'Bottom: the thermocouple of the second worked example. Its emf curves, but its meter is scaled by a straight line through the ice and steam points, '
              'so at a true 50 °C it shows 58.33 °C.',
          'Top: boxes for body A and body B, each linked to a thermometer C, both reading 25.0 °C, with a dashed link between A and B. '
          'Bottom: a curved plot of thermocouple emf against temperature from 0 to 100 °C, reaching 15 mV at 100 °C, with a straight dashed scale line; at 50 °C the emf is 8.75 mV, which the straight scale reads as 58.33 °C.')


# ---- 1.6 one cylinder, two boundaries: the heater counts as work or as heat ----
def cyl(x):
    o = [P([(x, 90), (x, 250), (x + 200, 250), (x + 200, 90)], INK, 3)]
    o.append(R(x + 4, 120, 192, 126, ACS, 'none', 2, 0))
    o.append(R(x + 2, 100, 196, 20, PANEL, INK, 3, 2.5))
    o.append(L(x + 100, 100, x + 100, 52, INK, 5))
    o.append(T(x + 100, 172, 'gas', 14, bold=True, fill=AC))
    o.append(R(x + 20, 230, 160, 14, NXS, NX, 3, 2))
    o.append(T(x + 208, 242, 'heater', 13, 'start', NX))
    o.append(L(x + 40, 244, x + 40, 300, NX, 2))
    return ''.join(o)


def f6():
    o = []
    xs = (60, 420)
    titles = ('Boundary: gas and heater', 'Boundary: gas only')
    for i, x in enumerate(xs):
        o.append(T(x + 100, 24, titles[i], 14, bold=True))
        o.append(cyl(x))
    x = xs[0]
    o.append(R(x + 8, 121, 184, 132, 'none', LV, 10, 2.2, '7 5'))
    o.append(L(x + 100, 96, x + 100, 36, AC, 3, arrow='n')); o.append(T(x + 112, 50, 'W = +25 kJ', 13, 'start', AC, bold=True))
    o.append(L(x + 204, 170, x + 262, 170, NX, 3, arrow='x')); o.append(T(x + 210, 196, 'Q = −15 kJ', 13, 'start', NX, bold=True))
    o.append(L(x + 40, 296, x + 40, 260, NX, 3, arrow='x'))
    o.append(T(x + 52, 290, 'electrical work: W = −60 kJ', 13, 'start', NX, bold=True))
    o.append(T(x + 120, 330, 'Q = −15 kJ, W = 25 − 60 = −35 kJ', 14, bold=True))
    o.append(T(x + 120, 352, 'Q − W = −15 + 35 = +20 kJ', 14, bold=True, fill=LV))
    x = xs[1]
    o.append(R(x + 8, 121, 184, 103, 'none', LV, 10, 2.2, '7 5'))
    o.append(L(x + 100, 96, x + 100, 36, AC, 3, arrow='n')); o.append(T(x + 112, 50, 'W = +25 kJ', 13, 'start', AC, bold=True))
    o.append(L(x + 70, 236, x + 70, 196, NX, 3, arrow='x')); o.append(Tb(x + 80, 206, 'Q = +60 kJ', 13, 'start', NX, bold=True))
    o.append(L(x + 204, 150, x + 262, 150, NX, 3, arrow='x')); o.append(T(x + 210, 176, 'Q = −15 kJ', 13, 'start', NX, bold=True))
    o.append(T(x + 52, 290, 'heater sits outside', 13, 'start', MUT))
    o.append(T(x + 100, 330, 'Q = 60 − 15 = +45 kJ, W = +25 kJ', 14, bold=True))
    o.append(T(x + 100, 352, 'Q − W = 45 − 25 = +20 kJ', 14, bold=True, fill=LV))
    return 370, ''.join(o)


FIG[6] = (f6, 'The worked example’s cylinder with the sign convention Q > 0 into the system and W > 0 out of it. With the heater inside the boundary, '
              'its 60 kJ crosses as electrical work; with the heater outside, the same 60 kJ crosses as heat. The labels change, but Q − W = +20 kJ either way.',
          'Two drawings of a gas cylinder with a piston and an electric heater coil. Left: the dashed boundary encloses the heater, and the arrows show '
          '60 kJ of electrical work in, 25 kJ of piston work out and 15 kJ of heat out. Right: the boundary encloses only the gas, and the heater gives 60 kJ of heat in.')


# ---- 1.7 three paths from the same state ----
def f7():
    o = []
    x0, x1, y0, y1 = 100, 520, 50, 330
    fx = lambda V: x0 + V / 0.22 * (x1 - x0)
    fy = lambda p: y1 - p / 900 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.05, 0.10, 0.15, 0.20], [0, 200, 400, 600, 800], fx, fy, 'V (m³)', 'p (kPa)', xfmt=lambda v: f'{v:.2f}'))
    poly = [(0.05 + i * 0.0015, 800 * (0.05 / (0.05 + i * 0.0015)) ** 1.3) for i in range(101)]
    iso = [(0.05 + i * 0.0015, 40 / (0.05 + i * 0.0015)) for i in range(101)]
    area = [(fx(0.05), fy(0))] + [(fx(v), fy(p)) for v, p in poly] + [(fx(0.20), fy(0))]
    o.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in area)}" style="fill:var(--live-soft);stroke:none"/>')
    o.append(P([(fx(0.05), fy(800)), (fx(0.20), fy(800))], MUT, 2.5, '8 5'))
    o.append(P([(fx(v), fy(p)) for v, p in iso], AC, 3))
    o.append(P([(fx(v), fy(p)) for v, p in poly], LV, 3))
    o.append(C(fx(0.05), fy(800), 7, INK)); o.append(T(fx(0.05) + 4, fy(800) - 12, '1: 800 kPa, 0.05 m³', 14, 'start', bold=True))
    o.append(C(fx(0.20), fy(200), 6, AC)); o.append(C(fx(0.20), fy(131.95), 6, LV))
    o.append(T(fx(0.20) + 10, fy(200) + 1, '200 kPa', 13, 'start', AC, bold=True))
    o.append(T(fx(0.20) + 10, fy(131.95) + 9, '131.95 kPa', 13, 'start', LV, bold=True))
    o.append(Tb(fx(0.12), fy(60), 'area under pV¹·³ = C: 45.37 kJ', 14, 'middle', LV, bold=True))
    # legend panel
    o.append(boxt(578, 56, 132, 74, ['p = 800 kPa', 'W = 120 kJ'], PANEL, MUT, 14, True))
    o.append(boxt(578, 146, 132, 74, ['pV = C', 'W = 55.45 kJ'], ACS, AC, 14, True))
    o.append(boxt(578, 236, 132, 74, ['pV¹·³ = C', 'W = 45.37 kJ'], LVS, LV, 14, True))
    return 390, ''.join(o)


FIG[7] = (f7, 'The worked example’s gas expanding from state 1 to 0.20 m³ along three quasi-static paths. Work is the area under each path, '
              'so the same start and the same final volume give 120 kJ, 55.45 kJ or 45.37 kJ.',
          'A pressure–volume plot starting at 800 kPa and 0.05 cubic metres. A dashed horizontal line stays at 800 kPa; a curve pV = C falls to 200 kPa; '
          'a steeper curve pV to the power 1.3 = C falls to 131.95 kPa at 0.20 cubic metres, with the area under it shaded. Boxes give the three works: 120, 55.45 and 45.37 kJ.')


spec = make_spec(FIG)
