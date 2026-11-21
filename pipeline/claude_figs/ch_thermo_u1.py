"""Claude's hand-drawn figures for ch-thermo-u1 (Basic concepts and the first law), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def poly(pts, fill, stroke='none', op=None, w=0):
    o = f';fill-opacity:{op}' if op is not None else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{w}{o}"/>'


def arrowL(x1, y1, x2, y2, c=AC, k='n', w=3):
    return L(x1, y1, x2, y2, c, w, arrow=k)


# ---- 1.1 the halving test on the worked example's vessel ----
def f1():
    o = []
    o.append(T(135, 26, 'Whole vessel', 15, bold=True))
    o.append(R(30, 40, 210, 200, PANEL, INK, 10, 2.5))
    rows = [('m = 2.00 kg', AC), ('V = 1.20 m³', AC), ('T = 300 K', LV), ('P = 150 kPa', LV), ('ρ = 1.67 kg/m³', LV), ('v = 0.600 m³/kg', LV)]
    for i, (s, col) in enumerate(rows):
        o.append(T(135, 72 + i * 28, s, 15, fill=col, bold=(col == AC)))
    o.append(arrowL(252, 140, 318, 140, MUT, 'm', 2.5))
    o.append(T(285, 126, 'slide in', 13, fill=MUT))
    o.append(T(285, 162, 'a wall', 13, fill=MUT))
    o.append(T(515, 26, 'Two equal halves', 15, bold=True))
    o.append(R(330, 40, 370, 200, PANEL, INK, 10, 2.5))
    o.append(L(515, 40, 515, 240, INK, 4))
    half = [('m = 1.00 kg', AC), ('V = 0.600 m³', AC), ('T = 300 K', LV), ('P = 150 kPa', LV), ('ρ = 1.67 kg/m³', LV), ('v = 0.600 m³/kg', LV)]
    for xc in (422, 608):
        for i, (s, col) in enumerate(half):
            o.append(T(xc, 72 + i * 28, s, 14, fill=col, bold=(col == AC)))
    o.append(R(30, 262, 330, 48, ACS, AC, 8))
    o.append(T(195, 292, 'halves with the vessel: extensive', 14, fill=AC, bold=True))
    o.append(R(370, 262, 330, 48, LVS, LV, 8))
    o.append(T(535, 292, 'same in each half: intensive', 14, fill=LV, bold=True))
    return 326, ''.join(o)
FIG[1] = (f1, 'The halving test on the worked example. Cutting the 2.00 kg vessel into two equal halves halves m and V, so they are extensive; T, P, ρ and v are the same in each half, so they are intensive.',
          'A gas vessel with m 2.00 kilograms, V 1.20 cubic metres, T 300 kelvin, P 150 kilopascals, density 1.67 and specific volume 0.600, and the same vessel cut into two halves, each with m 1.00 kilogram and V 0.600 cubic metres but the same temperature, pressure, density and specific volume.')


# ---- 1.2 two paths between A and B on a P-V plot ----
def f2():
    o = []
    x0, x1, y0, y1 = 80, 500, 40, 300
    fx = lambda v: x0 + (v - 0.5) / 3.0 * (x1 - x0)
    fy = lambda P: y1 - P / 3.5 * (y1 - y0)
    A_, mA, mB, B_ = (1, 3), (2, 1.5), (2, 2), (3, 1)
    # areas: under path A (accent soft), the extra under path B (next soft)
    o.append(poly([(fx(1), fy(0)), (fx(1), fy(3)), (fx(2), fy(1.5)), (fx(3), fy(1)), (fx(3), fy(0))], ACS))
    o.append(poly([(fx(1), fy(3)), (fx(2), fy(2)), (fx(3), fy(1)), (fx(2), fy(1.5))], NXS))
    o.append(axes(x0, x1, y0, y1, [1, 2, 3], [0, 1, 2, 3], fx, fy, 'Volume V (L)', 'Pressure P (kPa)'))
    o.append(P([(fx(v), fy(p_)) for v, p_ in (A_, mA, B_)], AC, 3))
    o.append(P([(fx(v), fy(p_)) for v, p_ in (A_, mB, B_)], NX, 3, '7 4'))
    for (v, p_), lab, dx, dy, anc in ((A_, 'A (1 L, 3 kPa)', 10, -8, 'start'), (B_, 'B (3 L, 1 kPa)', 8, -12, 'start'),
                                       (mA, '(2, 1.5)', -10, 22, 'end'), (mB, '(2, 2)', 10, -10, 'start')):
        o.append(C(fx(v), fy(p_), 5.5, INK))
        o.append(T(fx(v) + dx, fy(p_) + dy, lab, 13, anc))
    o.append(T(fx(2), fy(0.55), 'area under path A', 13, fill=AC))
    o.append(boxt(520, 60, 190, 64, ['path A (solid)', 'W = 2.25 + 1.25 = 3.50 J'], PANEL, AC, 13, True))
    o.append(boxt(520, 140, 190, 64, ['path B (dashed)', 'W = 2.50 + 1.50 = 4.00 J'], PANEL, NX, 13, True))
    o.append(boxt(520, 220, 190, 64, ['same end states,', 'work differs by 0.50 J'], NXS, NX, 13))
    return 350, ''.join(o)
FIG[2] = (f2, 'The two quasi-static paths of the worked example. The work done by the gas is the area under each path: 3.50 J for path A and 4.00 J for path B, so work depends on the path even though both start at A and end at B.',
          'Pressure against volume with points A at 1 litre and 3 kilopascals and B at 3 litres and 1 kilopascal, joined by a solid path through 2 litres and 1.5 kilopascals and a dashed path through 2 litres and 2 kilopascals; the area under the solid path is shaded and the extra area under the dashed path is shaded in a second colour.')


# ---- 1.3 sign convention, the two steps of the worked example ----
def f3():
    o = []
    for i, (title, qv, qin, wv, wout, du) in enumerate((
            ('Step 1', 'Q₁ = +50 kJ', True, 'W₁ = +20 kJ', True, 'ΔU₁ = 50 − 20 = +30 kJ'),
            ('Step 2', 'Q₂ = −15 kJ', False, 'W₂ = −10 kJ', False, 'ΔU₂ = −15 − (−10) = −5 kJ'))):
        x = 20 + i * 350
        o.append(T(x + 165, 26, title, 15, bold=True))
        o.append(R(x + 95, 60, 140, 110, PANEL, INK, 10, 2.5, '7 5'))
        o.append(T(x + 165, 108, 'system', 15, bold=True))
        o.append(T(x + 165, 132, 'U + KE + PE', 13, fill=MUT))
        # heat on the left
        if qin: o.append(arrowL(x + 10, 100, x + 92, 100, NX, 'x'))
        else: o.append(arrowL(x + 92, 100, x + 10, 100, NX, 'x'))
        o.append(T(x + 50, 80, qv, 13, fill=NX, bold=True))
        o.append(T(x + 50, 122, 'heat in' if qin else 'heat rejected', 13, fill=NX))
        # work on the right
        if wout: o.append(arrowL(x + 238, 130, x + 320, 130, LV, 'l'))
        else: o.append(arrowL(x + 320, 130, x + 238, 130, LV, 'l'))
        o.append(T(x + 280, 110, wv, 13, fill=LV, bold=True))
        o.append(T(x + 280, 152, 'work by system' if wout else 'work done on it', 13, fill=LV))
        o.append(boxt(x + 40, 190, 250, 40, [du], ACS, AC, 14))
    o.append(boxt(70, 256, 580, 52, ['Net over both steps: Q = 35 kJ, W = 10 kJ, ΔU = 35 − 10 = +25 kJ'], PANEL, AC, 15))
    return 324, ''.join(o)
FIG[3] = (f3, 'The sign rule on the worked example: heat into the system and work done by the system are positive, so ΔU = Q − W. Step 1 gives +30 kJ, step 2 gives −5 kJ, and the net change is +25 kJ.',
          'Two panels with a system box. In step 1 a heat arrow of plus 50 kilojoules points in and a work arrow of plus 20 kilojoules points out, giving delta U plus 30. In step 2 a heat arrow of minus 15 points out and a work arrow of minus 10 points in, giving delta U minus 5. A bar below gives the net change of plus 25 kilojoules.')


# ---- 1.4 four temperature scales lined up, with the 27 °C reading ----
def f4():
    o = []
    def fy(K):
        return 330 if K < 100 else 290 - (K - 260) * 2.0
    xs = [170, 300, 430, 560]
    names = ['Kelvin', 'Celsius', 'Fahrenheit', 'Rankine']
    vals = {0: ['0 K', '−273.15 °C', '−459.67 °F', '0 R'], 273.15: ['273.15 K', '0 °C', '32 °F', '491.67 R'],
            300.15: ['300.15 K', '27 °C', '80.6 °F', '540.27 R'], 373.15: ['373.15 K', '100 °C', '212 °F', '671.67 R']}
    rows = [(373.15, 'steam point', L2, INK), (300.15, 'the reading', AC, AC), (273.15, 'ice point', L2, INK), (0, 'absolute zero', L2, INK)]
    for K, lab, col, tcol in rows:
        y = fy(K)
        o.append(L(xs[0] - 10, y, 700, y, col, 2.5 if col == AC else 1.5, None if col == AC else '5 4'))
        o.append(T(20, y + 5, lab, 13, 'start', tcol, bold=(col == AC)))
        for j, x in enumerate(xs):
            o.append(Tb(x + 62, y - 6, vals[K][j], 13, fill=tcol, bold=(col == AC)))
    for j, x in enumerate(xs):
        o.append(T(x + 20, 30, names[j], 14, bold=True))
        o.append(R(x, 48, 16, 290, PANEL, INK, 8, 2))
        o.append(R(x + 3, fy(300.15), 10, 335 - fy(300.15), AC, AC, 4, 0))
    # axis break between 0 K and 260 K
    for x in xs:
        o.append(L(x - 4, 304, x + 20, 298, INK, 2)); o.append(L(x - 4, 312, x + 20, 306, INK, 2))
    return 350, ''.join(o)
FIG[4] = (f4, 'The worked example on four scales: 27 °C is 300.15 K, 80.6 °F and 540.27 R. Kelvin and Rankine start at absolute zero; one Celsius degree equals one kelvin, and one Fahrenheit degree equals one rankine (1/1.8 K).',
          'Four thermometer columns labelled Kelvin, Celsius, Fahrenheit and Rankine with horizontal lines for the steam point, the 27 degree reading, the ice point and absolute zero, each line labelled with its value on every scale; the scale is broken between absolute zero and 260 kelvin.')


# ---- 1.5 Joule's paddle wheel with the worked example's numbers ----
def f5():
    o = []
    # insulated vessel: outer and inner walls
    o.append(R(60, 120, 260, 200, FIGBG, MUT, 6, 2, '6 4'))
    o.append(R(76, 136, 228, 168, NXS, NX, 6, 2))
    o.append(T(190, 286, '1.00 kg water', 14, bold=True))
    o.append(T(190, 340, 'insulation: Q = 0', 13, fill=MUT))
    # paddle shaft and blades
    o.append(L(190, 60, 190, 250, INK, 3))
    for yy in (190, 230):
        o.append(R(150, yy - 5, 80, 10, PANEL, INK, 2, 2))
    # pulley and string to the mass
    o.append(f'<circle cx="190" cy="60" r="22" style="fill:var(--panel);stroke:var(--ink);stroke-width:2.5"/>')
    o.append(L(212, 60, 380, 60, INK, 2))
    o.append(f'<circle cx="390" cy="60" r="10" style="fill:var(--panel);stroke:var(--ink);stroke-width:2.5"/>')
    o.append(L(400, 60, 400, 150, INK, 2))
    o.append(R(370, 150, 60, 50, ACS, AC, 6, 2.5))
    o.append(T(400, 181, '10.0 kg', 14, bold=True))
    o.append(L(400, 210, 400, 290, AC, 2.5, '6 4', 'n'))
    o.append(R(370, 290, 60, 30, PANEL, AC, 6, 1.5, '4 3'))
    o.append(T(384, 250, 'falls', 14, 'end', AC, bold=True))
    o.append(T(384, 270, 'h = 2.00 m', 14, 'end', AC, bold=True))
    o.append(T(400, 340, 'after the fall', 13, fill=MUT))
    o.append(boxt(470, 70, 240, 150, ['W = −mgh', '= −10.0 × 9.81 × 2.00', '= −196.2 J (on the water)', 'ΔU = Q − W = +0.1962 kJ'], PANEL, AC, 14, True))
    o.append(boxt(470, 236, 240, 70, ['ΔT = 0.1962/(1.00 × 4.18)', '= 0.0469 K'], ACS, AC, 14))
    return 356, ''.join(o)
FIG[5] = (f5, 'Joule\'s paddle wheel with the worked example\'s numbers: the 10.0 kg mass falls 2.00 m and stirs 1.00 kg of insulated water. No heat crosses, yet the work done on the water, 196.2 J, raises its temperature by 0.0469 K.',
          'An insulated vessel of water with a paddle shaft, a pulley and a string to a 10.0 kilogram mass falling 2.00 metres, with boxes giving the work of minus 196.2 joules, the internal energy rise of 0.1962 kilojoules and the temperature rise of 0.0469 kelvin.')


# ---- 1.6 the turbine control volume and its energy account ----
def f6():
    o = []
    o.append(R(150, 40, 330, 190, FIGBG, MUT, 10, 2, '8 5'))
    o.append(T(165, 60, 'control volume', 13, 'start', MUT))
    o.append(poly([(230, 110), (230, 160), (400, 200), (400, 70)], PANEL, INK, None, 2.5))
    o.append(T(315, 140, 'turbine', 15, bold=True))
    o.append(arrowL(20, 135, 228, 135, AC, 'n'))
    o.append(T(20, 105, 'ṁ = 2.0 kg/s', 13, 'start', AC, bold=True))
    o.append(T(20, 160, sb('h', '1') + ' = 3200 kJ/kg', 13, 'start', AC))
    o.append(T(20, 180, sb('c', '1') + ' = 60 m/s', 13, 'start', AC))
    o.append(arrowL(402, 135, 700, 135, AC, 'n'))
    o.append(T(560, 160, sb('h', '2') + ' = 2600 kJ/kg', 13, 'start', AC))
    o.append(T(560, 180, sb('c', '2') + ' = 120 m/s', 13, 'start', AC))
    o.append(L(315, 200, 315, 290, LV, 6))
    o.append(arrowL(315, 260, 400, 260, LV, 'l'))
    o.append(T(408, 265, sb('W', 's') + ' = 1139.2 kW (out)', 14, 'start', LV, bold=True))
    o.append(arrowL(330, 72, 330, 12, NX, 'x'))
    o.append(T(340, 26, 'Q = −50 kW (loss)', 13, 'start', NX, bold=True))
    # energy account bars (kW)
    y, sc = 318, 0.09
    o.append(T(20, y - 6, 'Energy account (kW)', 14, 'start', bold=True))
    o.append(T(60, y + 22, 'in', 13, 'end', MUT))
    o.append(R(70, y + 6, 6403.6 * sc, 24, ACS, AC, 3, 1.5)); o.append(T(78, y + 23, 'stream in: 2.0 × (3200 + 1.8) = 6403.6', 13, 'start'))
    o.append(T(60, y + 56, 'out', 13, 'end', MUT))
    xo = 70
    for v, col, fil, lab in ((5214.4, AC, ACS, 'stream out 5214.4'), (1139.2, LV, LVS, '1139.2'), (50, NX, NXS, '')):
        o.append(R(xo, y + 40, v * sc, 24, fil, col, 3, 1.5))
        if lab: o.append(T(xo + 8, y + 57, lab, 13, 'start'))
        xo += v * sc
    o.append(T(xo + 6, y + 57, '+ 50', 13, 'start', NX))
    return 392, ''.join(o)
FIG[6] = (f6, 'The turbine of the worked example as a control volume. Per second the steam brings in 6403.6 kW of enthalpy plus kinetic energy and carries out 5214.4 kW; the difference leaves as 1139.2 kW of shaft power and a 50 kW heat loss.',
          'A turbine inside a dashed control volume with steam entering at 2.0 kilograms per second, 3200 kilojoules per kilogram and 60 metres per second, leaving at 2600 and 120, a shaft arrow of 1139.2 kilowatts and a heat-loss arrow of 50 kilowatts, and two bars showing 6403.6 kilowatts in equal to 5214.4 out plus 1139.2 plus 50.')


# ---- 1.7 the same heating at constant volume and at constant pressure ----
def f7():
    o = []
    # rigid vessel
    o.append(T(170, 26, 'Rigid vessel (V fixed)', 15, bold=True))
    o.append(R(90, 50, 160, 120, NXS, INK, 8, 3))
    o.append(T(170, 104, '2.0 mol', 14, bold=True)); o.append(T(170, 126, '300 → 400 K', 14))
    o.append(arrowL(170, 222, 170, 174, NX, 'x'))
    o.append(T(170, 242, 'Q = 4160 J', 14, fill=NX, bold=True))
    # piston cylinder
    o.append(T(540, 26, 'Free piston (P fixed)', 15, bold=True))
    o.append(P([(460, 62), (460, 170), (620, 170), (620, 62)], INK, 3))
    o.append(R(462, 84, 156, 14, PANEL, INK, 2, 2))
    o.append(R(462, 98, 156, 72, NXS, 'none', 0, 0))
    o.append(T(540, 126, '2.0 mol', 14, bold=True)); o.append(T(540, 148, '300 → 400 K', 14))
    o.append(arrowL(540, 82, 540, 50, LV, 'l'))
    o.append(T(552, 54, 'W = 1662.8 J', 13, 'start', LV, bold=True))
    o.append(arrowL(540, 222, 540, 174, NX, 'x'))
    o.append(T(540, 242, 'Q = 5822.8 J', 14, fill=NX, bold=True))
    # where the heat goes: bars
    sc = 0.05
    for x0, parts, lab in ((40, [(4160, ACS, AC, 'ΔU 4160')], 'Q = ΔU'), (380, [(4160, ACS, AC, 'ΔU 4160'), (1662.8, LVS, LV, 'W 1662.8')], 'Q = ΔH = ΔU + PΔV')):
        xx = x0
        for v, fil, col, t in parts:
            o.append(R(xx, 272, v * sc, 30, fil, col, 3, 1.5)); o.append(T(xx + v * sc / 2, 292, t, 13)); xx += v * sc
        o.append(T(x0, 326, lab, 14, 'start', bold=True))
    o.append(T(20, 360, 'Same ΔT and same ΔU = n C' + sb('', 'v') + ' ΔT; the piston case also pays the expansion work nRΔT.', 13, 'start', MUT))
    return 374, ''.join(o)
FIG[7] = (f7, 'The worked example: heating 2.0 mol from 300 K to 400 K takes 4160 J in a rigid vessel but 5822.8 J under a free piston. ΔU is 4160 J both times; the extra 1662.8 J leaves as the piston\'s expansion work, which is why C<sub>p</sub> − C<sub>v</sub> = R.',
          'A rigid vessel receiving 4160 joules of heat and a piston cylinder receiving 5822.8 joules while its piston does 1662.8 joules of work, with bars showing that the internal energy rise is 4160 joules in both cases and the piston case adds the work.')


# ---- 1.8 compression work as the area to the left of the path (worked example 2) ----
def f8():
    o = []
    x0, x1, y0, y1 = 80, 500, 40, 320
    fx = lambda v: x0 + v / 1.0 * (x1 - x0)
    fy = lambda Pb: y1 - Pb / 5.5 * (y1 - y0)
    Rg, T1 = 0.287, 300.0
    Ps = [1 + 0.25 * i for i in range(17)]
    iso = [(Rg * T1 / (100 * Pb), Pb) for Pb in Ps]
    isen = [(Rg * T1 * Pb ** (-1 / 1.4) / 100, Pb) for Pb in Ps]
    o.append(poly([(fx(0), fy(1))] + [(fx(v), fy(Pb)) for v, Pb in isen] + [(fx(0), fy(5))], NXS))
    o.append(poly([(fx(0), fy(1))] + [(fx(v), fy(Pb)) for v, Pb in iso] + [(fx(0), fy(5))], ACS))
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 1, 2, 3, 4, 5], fx, fy, 'Specific volume v (m³/kg)', 'Pressure P (bar)', lambda v: f'{v:.1f}'))
    o.append(P([(fx(v), fy(Pb)) for v, Pb in iso], AC, 3))
    o.append(P([(fx(v), fy(Pb)) for v, Pb in isen], NX, 3, '7 4'))
    for (v, Pb, lab, dx, dy, anc, col) in ((0.861, 1, '1: 1 bar, 300 K, 0.861 m³/kg', 6, 24, 'end', INK),
                                         (0.1722, 5, '2: 300 K', 8, -10, 'start', AC), (0.2727, 5, '2s: 475.1 K', 12, 16, 'start', NX)):
        o.append(C(fx(v), fy(Pb), 5.5, col))
        o.append(T(fx(v) + dx, fy(Pb) + dy, lab, 13, anc, col, bold=True))
    o.append(T(fx(0.07), fy(3.0), '∫v dP', 14, 'start', AC, bold=True))
    o.append(boxt(520, 50, 190, 64, ['isothermal (solid)', '138.6 kJ/kg'], PANEL, AC, 14, True))
    o.append(boxt(520, 130, 190, 64, ['isentropic (dashed)', '176.0 kJ/kg'], PANEL, NX, 14, True))
    o.append(boxt(520, 210, 190, 86, ['real, η = 0.80:', '220.0 kJ/kg,', 'exit 518.9 K'], NXS, NX, 14))
    return 372, ''.join(o)
FIG[8] = (f8, 'Worked example 2 on a P–v plot: the steady-flow work to compress air from 1 to 5 bar is the area to the left of each path. The isothermal path needs 138.6 kJ/kg, the isentropic path 176.0 kJ/kg; the real compressor needs 220.0 kJ/kg.',
          'Pressure from 0 to 5.5 bar against specific volume from 0 to 1 cubic metre per kilogram, with a solid isothermal curve and a dashed isentropic curve from 1 bar and 0.861 cubic metres per kilogram up to 5 bar; the areas between each curve and the pressure axis are shaded, labelled 138.6 and 176.0 kilojoules per kilogram.')

spec = make_spec(FIG)
