"""Claude's hand-drawn figures for me-thermo-u2 (Engineering Thermodynamics: first law of thermodynamics), one per
chapter, drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sub(base, s):
    return f'{base}<tspan dy="4" font-size="12">{s}</tspan><tspan dy="-4"></tspan>'


def harrow(x1, y, x2, c=AC, w=3, arrow='n'):
    return L(x1, y, x2, y, c, w, arrow=arrow)


def piston(x, y, w, h, gas_h, c=AC):
    """cylinder open at the top with a piston at height gas_h above the bottom; returns svg and piston top y"""
    o = [P([(x, y), (x, y + h), (x + w, y + h), (x + w, y)], INK, 2.5)]
    py = y + h - gas_h
    o.append(f'<rect x="{x + 3:.1f}" y="{py:.1f}" width="{w - 6:.1f}" height="{gas_h - 3:.1f}" style="fill:var(--accent-soft)"/>')
    o.append(R(x + 3, py - 16, w - 6, 16, PANEL, INK, 2, 2))
    o.append(L(x + w / 2, py - 16, x + w / 2, py - 46, INK, 3))
    return ''.join(o), py


# ---- 2.1 a closed system: one process and the cycle it belongs to ----
def f1():
    o = []
    # left: piston-cylinder for process 1 -> 2
    o.append(T(170, 30, 'Process 1 → 2 (closed system)', 15, bold=True))
    s, py = piston(110, 110, 120, 170, 105)
    o.append(s)
    o.append(R(96, 56, 148, 238, 'none', MUT, 10, 1.5, '6 5'))
    o.append(T(170, 222, 'gas', 14, fill=MUT))
    o.append(T(170, 250, 'ΔU = +50 kJ', 15, bold=True))
    o.append(harrow(14, 240, 104, LV, 3, 'l'))
    o.append(T(52, 228, 'Q₁₂ = 80 kJ', 14, fill=LV, bold=True))
    o.append(L(170, 120, 170, 70, NX, 3, arrow='x'))
    o.append(T(250, 84, 'W₁₂ = 30 kJ', 14, 'start', NX, True))
    o.append(T(250, 102, 'by the gas', 13, 'start', MUT))
    o.append(T(170, 318, '80 − 30 = 50 kJ stays inside', 14, fill=MUT))
    # right: p-V loop
    x0, y0, x1, y1 = 430, 60, 690, 290
    o.append(T(560, 30, 'The full cycle on a p-V diagram', 15, bold=True))
    o.append(L(x0, y1, x1, y1, L2, 1.5, arrow='m')); o.append(L(x0, y1, x0, y0, L2, 1.5, arrow='m'))
    o.append(T(x1, y1 + 22, 'V', 14, 'end', MUT)); o.append(T(x0 - 8, y0 + 6, 'p', 14, 'end', MUT))
    A, B = (470, 105), (660, 255)
    bez = lambda p0, c, p1, t: ((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t * t * p1[0], (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t * t * p1[1])
    up = [bez(A, (650, 95), B, i / 30) for i in range(31)]
    dn = [bez(B, (470, 265), A, i / 30) for i in range(31)]
    o.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in up + dn)}" style="fill:var(--accent-soft);stroke:none"/>')
    o.append(P(up, AC, 2.5)); o.append(P(dn, NX, 2.5, '7 5'))
    a1, a2 = up[14], up[16]; o.append(L(a1[0], a1[1], a2[0], a2[1], AC, 2.5, arrow='n'))
    b1, b2 = dn[14], dn[16]; o.append(L(b1[0], b1[1], b2[0], b2[1], NX, 2.5, arrow='x'))
    o.append(C(*A, 6, INK)); o.append(C(*B, 6, INK))
    o.append(T(A[0] - 12, A[1] - 6, '1', 15, 'end', bold=True)); o.append(T(B[0] + 10, B[1] + 4, '2', 15, 'start', bold=True))
    o.append(T(690, 72, '1 → 2: Q = +80, W = +30', 13, 'end', AC, True))
    o.append(T(440, 282, '2 → 1: Q = −70, W = −20', 13, 'start', NX, True))
    o.append(T(565, 178, 'loop area', 13, fill=INK))
    o.append(T(565, 195, '= 10 kJ', 13, fill=INK, bold=True))
    o.append(T(560, 318, 'net heat = net work = 10 kJ', 14, fill=MUT))
    return 335, ''.join(o)


FIG[1] = (f1, 'Left: in process 1 → 2 the gas takes in 80 kJ of heat and does 30 kJ of work, so 50 kJ stays as internal energy. '
              'Right: the return path 2 → 1 rejects 70 kJ while 20 kJ of work is done on the gas; the loop encloses the net work, 10 kJ, which equals the net heat.',
          'Left: a piston-cylinder with a dashed boundary; 80 kJ of heat enters, 30 kJ of work leaves through the piston rod, and the gas gains 50 kJ of internal energy. '
          'Right: a p-V loop from state 1 to state 2 along an upper expansion path and back along a lower dashed path; the shaded loop is labelled 10 kJ.')


# ---- 2.2 internal energy plus flow work gives enthalpy ----
def f2():
    o = []
    def stack(x, y_base, parts, scale, title, total):
        oo = [T(x + 55, 34, title, 15, bold=True)]
        y = y_base
        for val, lab, fill, stroke in parts:
            h = val * scale
            oo.append(R(x, y - h, 110, h, fill, stroke, 3))
            oo.append(T(x + 122, y - h / 2 + 5, lab, 14, 'start', INK))
            y -= h
        oo.append(L(x - 14, y, x - 14, y_base, INK, 1.8))
        oo.append(L(x - 20, y, x - 8, y, INK, 1.8)); oo.append(L(x - 20, y_base, x - 8, y_base, INK, 1.8))
        oo.append(T(x - 22, (y + y_base) / 2 + 5, total, 14, 'end', INK, True))
        return ''.join(oo)
    # air, 2 kg heated 300 -> 400 K at constant p: dU 143.6 + d(pV) 57.4 = dH 201.0
    o.append(stack(150, 300, [(143.6, 'ΔU = 143.6 kJ', ACS, AC), (57.4, 'Δ(pV) = 57.4 kJ', LVS, LV)], 1.2,
                   '2 kg of air, 300 → 400 K', 'ΔH = 201.0 kJ'))
    # steam, 1 MPa dry saturated: u 2582.8 + pv 194.4 = h 2777.2 (per kg), scale 0.087
    o.append(stack(500, 300, [(2582.8, 'u = 2582.8', ACS, AC), (194.4, 'pv = 194.4', LVS, LV)], 0.087,
                   'Dry steam, 1 MPa (kJ/kg)', 'h = 2777.2'))
    o.append(T(205, 330, 'drawn to scale', 13, fill=MUT))
    o.append(T(555, 330, 'drawn to scale (per kg)', 13, fill=MUT))
    return 345, ''.join(o)


FIG[2] = (f2, 'Enthalpy is internal energy plus flow work. Left: heating 2 kg of air at constant pressure, ΔU = 143.6 kJ and Δ(pV) = 57.4 kJ add to ΔH = 201.0 kJ. '
              'Right: for dry steam at 1 MPa, u = 2582.8 kJ/kg and pv = 194.4 kJ/kg add to h = 2777.2 kJ/kg; the steam table lists 2777.1.',
          'Two stacked bars drawn to scale. Left bar for 2 kg of air: a 143.6 kJ block for the change in internal energy under a 57.4 kJ block for the change in pV, totalling 201.0 kJ of enthalpy change. '
          'Right bar for dry saturated steam at 1 MPa: u of 2582.8 kJ/kg under pv of 194.4 kJ/kg, totalling h of 2777.2 kJ/kg.')


# ---- 2.3 the same 20 K rise in a rigid tank and in a constant-pressure cylinder ----
def f3():
    o = []
    sc = 2.6
    # left: rigid tank
    o.append(T(170, 30, 'Rigid tank: V fixed', 15, bold=True))
    o.append(R(105, 70, 130, 110, ACS, INK, 6, 2.5))
    o.append(T(170, 120, '2 kg air', 14)); o.append(T(170, 140, '+20 K', 14, bold=True))
    o.append(harrow(20, 150, 100, LV, 3, 'l')); o.append(T(58, 138, 'Q = 28.72 kJ', 13, fill=LV, bold=True))
    o.append(R(120, 300 - 28.72 * sc, 100, 28.72 * sc, ACS, AC, 3))
    o.append(T(170, 300 - 28.72 * sc / 2 + 5, 'ΔU 28.72', 14))
    o.append(T(170, 322, 'all the heat raises U', 13, fill=MUT))
    # right: piston at constant p
    o.append(T(520, 30, 'Cylinder: p fixed, piston rises', 15, bold=True))
    s, py = piston(455, 60, 130, 120, 92)
    o.append(s)
    o.append(T(520, 150, '2 kg air  +20 K', 14, bold=True))
    o.append(harrow(370, 150, 450, LV, 3, 'l')); o.append(T(408, 138, 'Q = 40.20 kJ', 13, fill=LV, bold=True))
    o.append(L(520, 68, 520, 44, NX, 3, arrow='x')); o.append(T(530, 56, 'W = 11.48 kJ', 13, 'start', NX, True))
    o.append(R(470, 300 - 28.72 * sc, 100, 28.72 * sc, ACS, AC, 3))
    o.append(T(520, 300 - 28.72 * sc / 2 + 5, 'ΔU 28.72', 14))
    o.append(R(470, 300 - 40.20 * sc, 100, 11.48 * sc, NXS, NX, 3))
    o.append(T(520, 300 - 40.20 * sc + 11.48 * sc / 2 + 5, 'W 11.48', 14))
    o.append(T(520, 322, 'part of the heat leaves as work', 13, fill=MUT))
    o.append(L(40, 300, 680, 300, L2, 1.5))
    return 335, ''.join(o)


FIG[3] = (f3, 'Warming 2 kg of air by 20 K. In the rigid tank all 28.72 kJ of heat (mc<sub>v</sub>ΔT) raises U. In the cylinder the same rise in U '
              'needs 40.20 kJ (mc<sub>p</sub>ΔT), because 11.48 kJ (mRΔT) leaves as work on the piston.',
          'Left: a closed rigid tank receives 28.72 kJ of heat; a bar shows all of it as internal energy. Right: a piston-cylinder at constant pressure receives 40.20 kJ; '
          'its bar shows 28.72 kJ of internal energy plus 11.48 kJ of work lifting the piston.')


# ---- 2.4 the three compression paths of the worked examples, computed ----
def f4():
    o = []
    x0, x1, y0, y1 = 90, 680, 40, 330
    Vmax, pmax = 0.9, 2000.0
    fx = lambda v: x0 + v / Vmax * (x1 - x0)
    fy = lambda p: y1 - p / pmax * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8], [0, 500, 1000, 1500, 2000], fx, fy, 'volume V (m³)', 'pressure p (kPa)'))
    V1, p1 = 0.861, 100.0
    V2 = V1 / 8
    def curve(n):
        pts = []
        for i in range(61):
            V = V2 + (V1 - V2) * i / 60
            pts.append((fx(V), fy(p1 * (V1 / V) ** n)))
        return pts
    o.append(P(curve(1.0), LV, 2.5))
    o.append(P(curve(1.3), AC, 2.5, '8 5'))
    o.append(P(curve(1.4), NX, 2.5))
    o.append(C(fx(V1), fy(p1), 6, INK)); o.append(T(fx(V1), fy(p1) - 14, '1: 0.861 m³, 100 kPa', 13, 'end', INK, True))
    o.append(T(400, 62, 'end state at V₂:', 14, 'start', INK, True))
    for i, (n, c, lab, dash) in enumerate(((1.4, NX, 'adiabatic, n = 1.4: 1838 kPa', None), (1.3, AC, 'polytropic, n = 1.3: 1493 kPa', '8 5'),
                                        (1.0, LV, 'isothermal, n = 1: 800 kPa', None))):
        p2 = p1 * 8 ** n
        o.append(C(fx(V2), fy(p2), 5, c))
        y = 88 + i * 24
        o.append(L(400, y - 5, 436, y - 5, c, 2.5, dash)); o.append(T(444, y, lab, 13, 'start', c, True))
    o.append(T(fx(V2), y1 + 56, 'V₂ = 0.108 m³', 13, 'start', MUT))
    o.append(L(fx(V2), y1, fx(V2), y1 + 42, L2, 1.2, '4 4'))
    return 395, ''.join(o)


FIG[4] = (f4, 'The worked examples’ three compressions of 1 kg of air from 0.861 m³ and 100 kPa to one-eighth of the volume, plotted from pVⁿ = C. '
              'The adiabatic (n = 1.4) climbs steepest, to 1838 kPa; the polytropic n = 1.3 ends at 1493 kPa and the isothermal at 800 kPa. The area under each curve is the work put in: 279.5, 248.6 and 179.0 kJ.',
          'Pressure against volume for three compression curves from V = 0.861 cubic metres at 100 kPa to V = 0.108 cubic metres: '
          'isothermal ending at 800 kPa, polytropic with n = 1.3 ending at 1493 kPa, and adiabatic ending at 1838 kPa, the steepest.')


# ---- 2.5 testing three claimed engines with the cycle balance ----
def f5():
    o = []
    sc = 0.8
    x0 = 150
    rows = [('(a)', 300, 0, 500, 'work exceeds heat by 200 kW: PMM-1'),
            ('(b)', 200, 0, 250, 'work exceeds heat by 50 kW: PMM-1'),
            ('(c)', 80, 20, 60, '60 + 20 = 80 kW: balance closes, allowed')]
    # legend
    for i, (lab, fill, stroke, dash) in enumerate((('heat in', LVS, LV, None), ('work out', NXS, NX, None), ('heat rejected', PANEL, NX, '4 3'))):
        x = 150 + i * 170
        o.append(R(x, 18, 26, 18, fill, stroke, 3, dash=dash)); o.append(T(x + 34, 32, lab, 14, 'start'))
    def bar(x, y, val, fill, stroke, lab, dash=None):
        w = val * sc
        oo = [R(x, y, w, 26, fill, stroke, 3, dash=dash)]
        if lab: oo.append(T(x + 8, y + 18, lab, 13, 'start') if w > tw(lab, 13) + 14 else T(x + w + 8, y + 18, lab, 13, 'start'))
        return ''.join(oo)
    for i, (name, qin, qout, w, verdict) in enumerate(rows):
        y = 62 + i * 102
        o.append(T(x0 - 14, y + 36, name, 16, 'end', INK, True))
        o.append(bar(x0, y, qin, LVS, LV, f'{qin} kW'))
        if qout:
            o.append(bar(x0, y + 32, w, NXS, NX, ''))
            o.append(bar(x0 + w * sc, y + 32, qout, PANEL, NX, '', '4 3'))
            o.append(T(x0 + (w + qout) * sc + 8, y + 50, f'{w} kW + {qout} kW', 13, 'start'))
        else:
            o.append(bar(x0, y + 32, w, NXS, NX, f'{w} kW'))
            o.append(L(x0 + qin * sc, y - 4, x0 + qin * sc, y + 62, INK, 1.5, '4 3'))
            o.append(f'<rect x="{x0 + qin * sc:.1f}" y="{y + 32:.1f}" width="{(w - qin) * sc:.1f}" height="26" style="fill:none;stroke:var(--ink);stroke-width:2.5"/>')
        o.append(T(x0, y + 80, verdict, 13, 'start', NX if not qout else INK, True))
    return 365, ''.join(o)


FIG[5] = (f5, 'The three claims of the worked example as energy bars. In (a) and (b) the work bar is longer than the heat bar, by 200 kW and 50 kW (outlined), so energy would be created. '
              'In (c) 60 kW of work plus 20 kW rejected equals the 80 kW supplied, so the first law is satisfied.',
          'Three pairs of horizontal bars. Claim a: heat in 300 kW, work out 500 kW, the extra 200 kW outlined. Claim b: heat in 200 kW, work out 250 kW, extra 50 kW outlined. '
          'Engine c: heat in 80 kW, work 60 kW plus 20 kW of heat rejected, which balances.')


# ---- 2.6 the turbine of the worked example as a control volume ----
def f6():
    o = []
    poly = [(250, 120), (470, 70), (470, 300), (250, 250)]
    o.append(f'<polygon points="{" ".join(f"{x},{y}" for x, y in poly)}" style="fill:var(--panel);stroke:var(--accent);stroke-width:2.5"/>')
    o.append(R(225, 50, 270, 280, 'none', MUT, 10, 1.5, '6 5'))
    o.append(T(360, 190, 'turbine', 15, bold=True)); o.append(T(360, 210, 'ṁ = 2 kg/s', 14, fill=MUT))
    o.append(T(360, 44, 'control volume', 13, fill=MUT))
    # inlet
    o.append(harrow(40, 185, 248, LV, 4, 'l'))
    o.append(T(40, 120, 'inlet 1', 14, 'start', LV, True))
    o.append(T(40, 140, 'h₁ = 3200 kJ/kg', 13, 'start')); o.append(T(40, 158, 'V₁ = 60 m/s, z₁ = 5 m', 13, 'start'))
    o.append(T(40, 218, 'carries 3200 + 1.80', 13, 'start', MUT)); o.append(T(40, 236, '+ 0.05 kJ/kg', 13, 'start', MUT))
    # outlet
    o.append(harrow(472, 230, 690, NX, 4, 'x'))
    o.append(T(690, 160, 'outlet 2', 14, 'end', NX, True))
    o.append(T(690, 180, 'h₂ = 2600 kJ/kg', 13, 'end')); o.append(T(690, 198, 'V₂ = 150 m/s, z₂ = 0', 13, 'end'))
    o.append(T(690, 262, 'carries 2600 + 11.25 kJ/kg', 13, 'end', MUT))
    # shaft work
    o.append(L(470, 118, 640, 118, AC, 5, arrow='n')); o.append(Tb(565, 98, 'w = 570.6 kJ/kg', 14, 'middle', AC, True))
    # heat loss
    o.append(L(360, 270, 360, 352, MUT, 3, arrow='m')); o.append(T(372, 360, 'q = −20 kJ/kg (lost)', 13, 'start', MUT, True))
    o.append(T(360, 396, 'in 3201.85 = out 2611.25 + 570.6 + 20 (kJ per kg)', 14, 'middle', INK, True))
    return 412, ''.join(o)


FIG[6] = (f6, 'The turbine of the worked example drawn as a control volume. Each kilogram brings 3201.85 kJ (enthalpy, kinetic and potential energy) and leaves with 2611.25 kJ; '
              'the difference goes out as 570.6 kJ of shaft work and 20 kJ of heat lost through the casing.',
          'A turbine inside a dashed control-volume boundary. Steam enters at h 3200 kJ/kg, 60 m/s, 5 m and leaves at h 2600 kJ/kg, 150 m/s, 0 m; '
          'shaft work of 570.6 kJ/kg leaves to the right and 20 kJ/kg of heat leaves downward.')


# ---- 2.7 filling an evacuated tank from a line ----
def f7():
    o = []
    o.append(R(20, 70, 230, 56, LVS, LV, 6))
    o.append(T(135, 92, 'supply line', 14, bold=True)); o.append(T(135, 112, '500 kPa, 300 K', 14))
    o.append(L(250, 98, 300, 98, LV, 4, arrow='l'))
    # valve symbol
    o.append(f'<polygon points="300,84 330,98 300,112" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    o.append(f'<polygon points="360,84 330,98 360,112" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    o.append(T(330, 72, 'valve', 13, fill=MUT))
    o.append(L(360, 98, 430, 98, LV, 4, arrow='l'))
    o.append(R(430, 50, 260, 150, ACS, AC, 14, 2.5))
    o.append(T(560, 84, 'rigid insulated tank, 0.2 m³', 13, fill=MUT))
    o.append(T(560, 112, 'start: empty', 14)); o.append(T(560, 140, 'end: 500 kPa, 420 K', 14, bold=True))
    o.append(T(560, 166, 'm₂ = 0.830 kg', 14, bold=True))
    o.append(T(560, 190, 'Q = 0, W = 0', 13, fill=MUT))
    # energy per kg bars
    sc = 1.05
    o.append(T(20, 242, 'per kg of line air:', 14, 'start', INK, True))
    bx = 210
    o.append(R(bx, 258, 215.4 * sc, 30, ACS, AC, 3)); o.append(T(bx + 8, 278, 'u = 215.4', 13, 'start'))
    o.append(R(bx + 215.4 * sc, 258, 86.1 * sc, 30, LVS, LV, 3)); o.append(T(bx + 215.4 * sc + 6, 278, 'pv 86.1', 13, 'start'))
    o.append(T(bx - 10, 278, 'arrives with', 13, 'end', MUT))
    o.append(R(bx, 302, 301.5 * sc, 30, ACS, AC, 3)); o.append(T(bx + 8, 322, 'u₂ = 301.5', 13, 'start'))
    o.append(T(bx - 10, 322, 'inside the tank', 13, 'end', MUT))
    o.append(T(bx + 301.5 * sc + 10, 278, '= h = 301.5 kJ/kg', 13, 'start', INK, True))
    o.append(T(bx + 301.5 * sc + 10, 322, '→ T₂ = 420 K', 13, 'start', NX, True))
    return 345, ''.join(o)


FIG[7] = (f7, 'Filling the empty insulated tank of the first worked example. Each kilogram of line air brings u = 215.4 kJ plus 86.1 kJ of flow work, h = 301.5 kJ; '
              'inside the closed tank all of it becomes internal energy, u₂ = h = 301.5 kJ/kg, so the air ends at 420 K although the line is at 300 K.',
          'A supply line at 500 kPa and 300 K feeds through a valve into a rigid insulated 0.2 cubic metre tank that ends at 500 kPa, 420 K, holding 0.830 kg. '
          'Bars below: per kilogram, u of 215.4 kJ plus flow work of 86.1 kJ arrives, and 301.5 kJ of internal energy ends up inside.')


# ---- 2.8 both directions balance energy; only one raises entropy ----
def f8():
    o = []
    def cup(x, y, hot):
        oo = [P([(x - 30, y - 40), (x - 24, y + 20), (x + 24, y + 20), (x + 30, y - 40)], INK, 2.5)]
        oo.append(f'<path d="M{x + 30},{y - 28} q22,10 0,30" style="fill:none;stroke:var(--ink);stroke-width:2.5"/>')
        oo.append(f'<polygon points="{x - 28},{y - 30} {x - 24},{y + 18} {x + 24},{y + 18} {x + 28},{y - 30}" style="fill:{"var(--next-soft)" if hot else "var(--accent-soft)"}"/>')
        return ''.join(oo)
    for i, (title, ok) in enumerate((('Happens: the cup cools', True), ('Never on its own: the cup re-heats', False))):
        x0 = 20 + i * 355
        o.append(R(x0, 20, 325, 300, PANEL, LV if ok else NX, 12, 2.5, None if ok else '7 5'))
        o.append(T(x0 + 162, 48, title, 15, bold=True))
        cx = x0 + 80
        o.append(cup(cx, 150, True))
        o.append(T(cx, 196, '0.2 kg water', 13, fill=MUT))
        o.append(T(cx, 214, '80 °C ↔ 25 °C', 13, fill=MUT))
        o.append(T(x0 + 250, 110, 'room', 14, bold=True)); o.append(T(x0 + 250, 128, '25 °C', 14))
        if ok: o.append(L(cx + 50, 150, x0 + 222, 150, LV, 3.5, arrow='l'))
        else: o.append(L(x0 + 222, 150, cx + 50, 150, NX, 3.5, '7 5', arrow='x'))
        o.append(T(x0 + 180, 134, '46.0 kJ', 14, 'middle', LV if ok else NX, True))
        o.append(T(x0 + 162, 250, 'first law: balances ✓', 14, 'middle', INK))
        o.append(T(x0 + 162, 278, f'total ΔS = {"+" if ok else "−"}0.0127 kJ/K', 14, 'middle', LV if ok else NX, True))
        o.append(T(x0 + 162, 302, 'second law: allowed' if ok else 'second law: forbidden', 14, 'middle', INK, True))
    return 335, ''.join(o)


FIG[8] = (f8, 'The cup of the worked example. Cooling passes 46.0 kJ from the water to the room; the reverse passes the same 46.0 kJ back, so the first law accepts both. '
              'Only cooling raises the total entropy of cup and room (by 0.0127 kJ/K), so only cooling happens.',
          'Two panels. Left, solid border: heat of 46.0 kJ flows from a cup of water at 80 °C to a room at 25 °C; the first law balances and total entropy rises by 0.0127 kJ/K, allowed. '
          'Right, dashed border: the same 46.0 kJ flows back from the room into the cup; the first law still balances but total entropy would fall by 0.0127 kJ/K, forbidden.')

spec = make_spec(FIG)
