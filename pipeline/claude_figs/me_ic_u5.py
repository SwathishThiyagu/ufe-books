"""Claude's hand-drawn figures for me-ic-u5 (Internal Combustion Engines: engine testing and performance), one per chapter,
drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """eta_mech, V_d ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔṁ])_([A-Za-z0-9,]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def fmt(v):
    return neg(f'{v:g}')


# ---- 5.1 where the fuel power goes (worked example: 28.67 kW fuel, 8.32 kW IP, 7.07 kW BP) ----
def f1():
    o = []
    x0, W = 150, 540
    s = W / 28.667
    ip, bp, fp = 8.316 * s, 7.069 * s, 1.247 * s
    o.append(T(16, 76, 'Fuel power', 14, 'start', bold=True))
    o.append(R(x0, 50, W, 40, PANEL, AC, 4))
    o.append(T(x0 + W / 2, 76, '28.67 kW = 2.4 kg/h × 43 MJ/kg', 14))
    o.append(T(16, 166, 'Indicated', 14, 'start', bold=True))
    o.append(R(x0, 140, ip, 40, ACS, AC, 4))
    o.append(T(x0 + ip / 2, 166, '8.32 kW', 14, bold=True))
    o.append(R(x0 + ip, 140, W - ip, 40, FIGBG, L2, 4, dash='6 5'))
    o.append(T(x0 + ip + (W - ip) / 2, 166, 'heat to coolant and exhaust: 20.35 kW', 14, fill=MUT))
    o.append(T(16, 256, 'Brake', 14, 'start', bold=True))
    o.append(R(x0, 230, bp, 40, LVS, LV, 4))
    o.append(T(x0 + bp / 2, 256, '7.07 kW', 14, bold=True))
    o.append(R(x0 + bp, 230, fp, 40, NXS, NX, 2))
    o.append(T(x0 + ip + 10, 256, 'friction 1.25 kW', 14, 'start', fill=NX))
    o.append(L(x0 + 40, 92, x0 + 40, 136, AC, 2, arrow='n'))
    o.append(T(x0 + 52, 120, '× η_ith = 8.32 ÷ 28.67 = 0.290', 14, 'start'))
    o.append(L(x0 + 40, 182, x0 + 40, 226, AC, 2, arrow='n'))
    o.append(T(x0 + 52, 210, '× η_mech = 0.85', 14, 'start'))
    o.append(T(360, 302, 'η_bth = η_ith × η_mech = 0.290 × 0.85 = 0.247 = 24.7 %', 14, bold=True))
    o.append(T(360, 326, 'BSFC = 2.4 kg/h ÷ 7.07 kW = 339.5 g/kWh', 14, fill=MUT))
    return 342, ''.join(o)


# ---- 5.2 Willans line (worked example 2) ----
def f2():
    o = []
    x0, x1, y0, y1 = 90, 690, 46, 300
    fx = lin(-5, 25, x0, x1); fy = lin(0, 6.5, y1, y0)
    o.append(axes(x0, x1, y0, y1, [-5, 0, 5, 10, 15, 20, 25], [0, 1, 2, 3, 4, 5, 6], fx, fy,
                  'brake power BP (kW)', 'fuel flow (kg/h)', fmt, fmt))
    o.append(L(fx(0), y0, fx(0), y1, L2, 1.5, dash='4 4'))
    line = lambda b: 0.90 + 0.24 * b
    o.append(L(fx(5), fy(line(5)), fx(22), fy(line(22)), AC, 2.5))
    o.append(L(fx(-3.75), fy(0), fx(5), fy(line(5)), AC, 2, dash='7 5'))
    for b, m in ((5, 2.10), (10, 3.30), (15, 4.50), (20, 5.70)):
        o.append(C(fx(b), fy(m), 6, AC))
    o.append(C(fx(-3.75), fy(0), 6, NX))
    o.append(brace(fx(-3.75), fx(0), y1 - 26, NX, up=False))
    o.append(Tb((fx(-3.75) + fx(0)) / 2, y1 - 34, 'FP = 3.75 kW', 14, fill=NX, bold=True))
    o.append(Tb(fx(9), fy(5.9), 'measured: ṁ_f = 0.90 + 0.24 BP', 14, 'middle'))
    o.append(Tb(fx(1.2), fy(1.55), 'extended to zero fuel', 13, 'start', fill=MUT))
    o.append(Tb(fx(11), fy(2.3), 'at 20 kW: IP = 20 + 3.75 = 23.75 kW', 13, 'start', fill=LV))
    o.append(Tb(fx(11), fy(1.8), 'η_mech = 20 ÷ 23.75 = 84.2 %', 13, 'start', fill=LV))
    return 350, ''.join(o)


# ---- 5.3 the test rig of the worked example ----
def f3():
    o = []
    # air box with orifice and manometer
    o.append(R(60, 120, 160, 120, PANEL, AC, 6))
    o.append(T(140, 170, 'air box', 14, bold=True))
    o.append(T(140, 192, 'ṁ_a = 0.052 kg/s', 14))
    o.append(L(60, 172, 60, 188, FIGBG, 5))
    o.append(L(16, 180, 56, 180, LV, 2.5, arrow='l'))
    o.append(T(20, 166, 'air', 13, 'start', fill=LV))
    o.append(f'<path d="M40,30 V100 Q40,114 55,114 Q70,114 70,100 V30 H120 V120" style="fill:none;stroke:{L2};stroke-width:2"/>')
    o.append(f'<path d="M40,80 V100 Q40,114 55,114 Q70,114 70,100 V56" style="fill:none;stroke:{AC};stroke-width:5"/>')
    o.append(L(76, 56, 98, 56, L2, 1)); o.append(L(46, 80, 98, 80, L2, 1))
    o.append(L(92, 60, 92, 76, NX, 1.6, arrow='x')); o.append(L(92, 76, 92, 60, NX, 1.6, arrow='x'))
    o.append(T(100, 73, 'h', 14, 'start', fill=NX, bold=True))
    o.append(T(132, 62, 'U-tube manometer: Δp = 9.81 × h (h in mm of water)', 13, 'start', fill=MUT))
    o.append(T(140, 262, 'orifice, C_d about 0.6', 13, fill=MUT))
    # pipe and engine
    o.append(L(220, 180, 296, 180, LV, 2.5, arrow='l'))
    o.append(boxt(300, 130, 170, 100, ['Engine', '2.0 L four-stroke', '3000 rpm'], ACS, AC, 14, True))
    # burette, cock and tank
    o.append(R(560, 40, 30, 150, PANEL, AC, 4))
    o.append(L(552, 70, 598, 70, INK, 2)); o.append(L(552, 160, 598, 160, INK, 2))
    o.append(T(604, 120, '50 mL', 14, 'start', bold=True))
    o.append(T(604, 140, 'in 25 s', 14, 'start'))
    o.append(C(575, 214, 9, NX))
    o.append(L(575, 190, 575, 205, AC, 2))
    o.append(T(560, 245, 'three-way cock', 13, 'end', fill=MUT))
    o.append(R(630, 196, 74, 40, PANEL, L2, 4))
    o.append(T(667, 221, 'tank', 13))
    o.append(L(630, 214, 584, 214, L2, 2))
    o.append(L(566, 214, 474, 214, NX, 2.5, arrow='x'))
    o.append(T(520, 206, 'fuel', 13, fill=NX))
    # results
    o.append(boxt(16, 286, 210, 66, ['Fuel', '0.0415 kg in 25 s', 'ṁ_f = 5.98 kg/h'], PANEL, NX, 13, True))
    o.append(boxt(238, 286, 200, 66, ['Air-fuel ratio', '0.052 ÷ 0.00166', 'AFR = 31.3'], PANEL, AC, 13, True))
    o.append(boxt(450, 286, 254, 66, ['Volumetric efficiency', 'ideal 1.18 × 0.002 × 25 = 0.0590', 'η_vol = 0.052 ÷ 0.0590 = 88.1 %'], PANEL, LV, 13, True))
    return 370, ''.join(o)


# ---- 5.4 hydraulic dynamometer with torque arm (worked example 1) ----
def f4():
    o = []
    cx, cy = 290, 180
    o.append(boxt(16, 145, 120, 70, ['Engine', '1.0 L four-stroke'], PANEL, AC, 13, True))
    o.append(L(136, 180, cx, 180, INK, 4))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="88" style="fill:{PANEL};stroke:{AC};stroke-width:2.5"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="38" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
    o.append(T(cx, cy + 5, 'rotor', 13))
    o.append(T(cx, cy - 52, 'casing', 13, fill=MUT))
    o.append(T(cx, cy + 112, 'casing swings on trunnions; water absorbs the power', 13, fill=MUT))
    o.append(arc(cx - 60, cy + 64, cx + 60, cy + 64, -0.35, LV, 2, 'l'))
    o.append(T(cx - 94, cy + 84, '1500 rev/min', 13, 'end', fill=LV))
    arm_end = cx + 250
    o.append(L(cx + 88, cy, arm_end, cy, INK, 5))
    o.append(R(arm_end - 22, cy + 34, 44, 26, NXS, NX, 4))
    o.append(T(arm_end, cy + 80, 'load cell', 13, fill=MUT))
    o.append(L(arm_end, cy + 4, arm_end, cy + 30, NX, 2.5, arrow='x'))
    o.append(T(arm_end + 12, cy + 24, 'W = 120 N', 14, 'start', fill=NX, bold=True))
    o.append(L(cx, 70, cx, 86, L2, 1.5)); o.append(L(arm_end, 70, arm_end, cy - 8, L2, 1.5))
    o.append(L(cx + 4, 78, arm_end - 4, 78, L2, 1.5, arrow='m'))
    o.append(L(arm_end - 4, 78, cx + 4, 78, L2, 1.5, arrow='m'))
    o.append(Tb((cx + arm_end) / 2, 70, 'arm L = 0.5 m from the shaft centre', 13))
    o.append(boxt(16, 316, 688, 80, ['T = W × L = 120 × 0.5 = 60 N·m', 'BP = 2π × 1500 × 60 ÷ 60 = 9425 W = 9.42 kW',
                                     'bmep = 2π × 2 × 60 ÷ (1.0 × 10⁻³ m³) = 7.54 × 10⁵ Pa = 7.54 bar'], PANEL, AC, 14))
    return 412, ''.join(o)


# ---- 5.5 heat balance bar (worked example) ----
def f5():
    o = []
    x0, W = 40, 640
    parts = [('Brake power', 10.5, 'dynamometer', LVS, LV), ('Cooling water', 10.032, '0.1333 × 4.18 × 18', ACS, AC),
             ('Exhaust gas', 10.85, '0.02583 × 1.05 × 400', NXS, NX), ('Rest', 3.618, 'by difference', PANEL, L2)]
    o.append(brace(x0, x0 + W, 84, INK, up=False))
    o.append(T(x0 + W / 2, 70, 'Fuel power 35.0 kW = 3.0 kg/h × 42 MJ/kg ÷ 3.6', 15, bold=True))
    x = x0
    for i, (name, kw, how, f, c) in enumerate(parts):
        w = kw / 35.0 * W
        o.append(R(x, 130, w, 60, f, c, 3))
        o.append(T(x + w / 2, 166, f'{kw / 35 * 100:.1f} %', 14, bold=True))
        o.append(T(x + w / 2, 120, name if w > 90 else name, 14, fill=c if c != L2 else INK, bold=True))
        o.append(T(x + w / 2, 214, f'{kw:.2f} kW' if kw != 10.5 else '10.50 kW', 14))
        if w > 90: o.append(T(x + w / 2, 236, how, 13, fill=MUT))
        x += w
    o.append(T(x0 + W - 34, 236, 'difference', 13, fill=MUT))
    o.append(T(360, 272, 'exhaust gas flow = air + fuel = 90 + 3 = 93 kg/h = 0.02583 kg/s', 13, fill=MUT))
    return 290, ''.join(o)


# ---- 5.6 brake power against intake air temperature at two pressures (worked example) ----
def f6():
    o = []
    x0, x1, y0, y1 = 90, 600, 46, 300
    fx = lin(15, 45, x0, x1); fy = lin(32, 42, y1, y0)
    o.append(axes(x0, x1, y0, y1, [15, 20, 25, 30, 35, 40, 45], [32, 34, 36, 38, 40, 42], fx, fy,
                  'intake air temperature (°C)', 'brake power (kW)'))
    for p, c, lab in ((1.00, AC, '1.00 bar'), (0.90, NX, '0.90 bar')):
        pts = [(fx(t), fy(40 * p * 298 / (t + 273))) for t in range(15, 46)]
        o.append(P(pts, c, 2.5))
        o.append(T(x1 + 10, pts[-1][1] + 5, lab, 14, 'start', fill=c, bold=True))
    o.append(L(fx(25), fy(40), fx(40) - 4, fy(34.27) - 5, L2, 1.8, dash='5 4', arrow='m'))
    o.append(C(fx(25), fy(40), 6, AC)); o.append(C(fx(40), fy(34.27), 6, NX))
    o.append(Tb(fx(25) + 10, fy(40) - 14, 'reference 25 °C, 1.00 bar: 40.0 kW', 13, 'start'))
    o.append(Tb(fx(40) - 10, fy(34.27) + 26, 'hot afternoon 40 °C, 0.90 bar: 34.27 kW', 13, 'end'))
    o.append(T(360, 372, 'brake power = 40 kW × (p ÷ 1.00 bar) × (298 K ÷ T)', 13, fill=MUT))
    return 386, ''.join(o)


# ---- 5.7 four levers and what each changes (worked examples 1 and 2) ----
def f7():
    o = []
    rows = [(['More air', 'turbocharger + intercooler'], ['trapped air mass up', 'density × 1.4: 80 → 112 kW']),
            (['Better mixture', 'CRDI spray, swirl, timing'], ['faster, more complete burn', 'indicated efficiency up']),
            (['Less friction', 'low-friction oil and rings'], ['friction power down', 'FP 12 → 10.2 kW, same IP']),
            (['Better control', 'ECU, lambda and knock sensors'], ['engine held near its best point', 'BSFC down across the map'])]
    for i, (a, b) in enumerate(rows):
        y = 16 + i * 74
        o.append(boxt(16, y, 300, 60, a, PANEL, AC, 14, True))
        o.append(L(316, y + 30, 382, y + 30, AC, 2, arrow='n'))
        o.append(boxt(386, y, 318, 60, b, ACS if i != 2 else NXS, AC if i != 2 else NX, 14, True))
    o.append(T(360, 330, 'Prove every change on the same test, before and after:', 14, bold=True))
    o.append(T(360, 352, 'brake power, BSFC and emissions at the same speed and load points.', 14, fill=MUT))
    return 366, ''.join(o)


# ---- 5.8 the pressure chain and the p-θ record of the worked example ----
def _ptheta():
    r, lam = 10.0, 0.30
    V = lambda th: 1 + (r - 1) / 2 * (1 + 1 / lam - math.cos(th) - math.sqrt(1 / lam ** 2 - math.sin(th) ** 2))

    def run(Q, start, dur=50.0, motored=False):
        p, g, out = 0.95, 1.33, []
        th = -180.0
        while th <= 120:
            v0 = V(math.radians(th)); v1 = V(math.radians(th + 0.5))
            xb = lambda a: 0 if a < start else 1 - math.exp(-5 * ((a - start) / dur) ** 3)
            dq = 0 if motored else Q * (xb(th + 0.5) - xb(th))
            p = (p * (v0 / v1) ** g) + (g - 1) / v1 * dq
            th += 0.5
            out.append((th, p))
        return out
    best = None
    for start in [-24 + 0.5 * i for i in range(24)]:
        lo, hi = 1.0, 600.0
        for _ in range(40):
            Q = (lo + hi) / 2
            pk = max(p for _, p in run(Q, start))
            lo, hi = (Q, hi) if pk < 62 else (lo, Q)
        tr = run(Q, start)
        th_pk = max(tr, key=lambda t: t[1])[0]
        if best is None or abs(th_pk - 14) < abs(best[0] - 14): best = (th_pk, tr)
    return best[1], run(0, 0, motored=True)


def f8():
    o = []
    boxes = [(16, ['Piezo transducer', 'flush in the head']), (200, ['Charge amplifier', 'charge → volts']),
             (384, ['Data logger', '100 cycles']), (568, ['Crank encoder', '1 pulse per degree'])]
    for x, lines in boxes:
        o.append(boxt(x, 16, 136 if x == 568 else 160, 60, lines, PANEL, AC, 13, True))
    o.append(L(176, 46, 196, 46, AC, 2, arrow='n')); o.append(L(360, 46, 380, 46, AC, 2, arrow='n'))
    o.append(L(568, 46, 548, 46, AC, 2, arrow='n'))
    fired, mot = _ptheta()
    x0, x1, y0, y1 = 90, 690, 120, 360
    fx = lin(-60, 60, x0, x1); fy = lin(0, 70, y1, y0)
    o.append(axes(x0, x1, y0, y1, [-60, -40, -20, 0, 20, 40, 60], [0, 10, 20, 30, 40, 50, 60, 70], fx, fy,
                  'crank angle (degrees, 0 = TDC)', 'cylinder pressure (bar)', fmt))
    sel = lambda tr: [(fx(t), fy(p)) for t, p in tr if -60 <= t <= 60]
    o.append(P(sel(mot), L2, 2, dash='6 5'))
    o.append(P(sel(fired), AC, 2.5))
    th, pk = max(fired, key=lambda t: t[1])
    o.append(C(fx(th), fy(pk), 6, NX))
    o.append(Tb(fx(th) + 12, fy(pk) + 4, f'peak 62 bar at {th:.0f}° ATDC', 14, 'start', fill=NX, bold=True))
    o.append(Tb(fx(-32), fy(30), 'firing', 14, 'middle', fill=AC, bold=True))
    o.append(Tb(fx(38), fy(9) - 4, 'motored', 13, 'middle', fill=MUT))
    o.append(T(390, 432, 'mean imep 8.2 bar, σ = 0.21 bar over 100 cycles → COV = 2.56 %', 14, bold=True))
    return 446, ''.join(o)


FIG = {
    1: (f1, 'Where the fuel power of the worked example goes. Indicated efficiency turns 28.67 kW of fuel power into 8.32 kW at the piston, friction takes 1.25 kW of that, and 7.07 kW reaches the shaft.',
        'Three bars to scale: fuel power 28.67 kW, indicated power 8.32 kW with 20.35 kW lost as heat, brake power 7.07 kW with friction 1.25 kW; brake thermal efficiency 24.7 per cent.'),
    2: (f2, 'Willans line for worked example 2. The four measured points lie on a straight line; extended back to zero fuel flow it cuts the power axis at −3.75 kW, so the friction power is 3.75 kW.',
        'Plot of fuel flow against brake power with four points on a straight line, extended to zero fuel at minus 3.75 kilowatts.'),
    3: (f3, 'The test rig of the worked example: the engine breathes from an air box and drinks from a burette. The two flows give the air-fuel ratio and, against the ideal air flow, the volumetric efficiency.',
        'Air box with orifice and manometer feeding the engine, burette with three-way cock and tank, and three result boxes for fuel flow, air-fuel ratio and volumetric efficiency.'),
    4: (f4, 'The hydraulic dynamometer of worked example 1. Water drag on the rotor tries to turn the casing; the arm holds it against the load cell, so torque is the cell force times the arm length.',
        'Engine shaft driving a rotor inside a swinging casing; a 0.5 metre arm presses a load cell with 120 newtons; torque 60 newton metres and brake power 9.42 kilowatts.'),
    5: (f5, 'Heat balance of the worked example as one bar of fuel power. Brake power, cooling water and exhaust each take close to a third; the remainder is found by difference.',
        'Bar of 35 kW fuel power split into brake power 30.0 per cent, cooling water 28.7 per cent, exhaust 31.0 per cent and the rest 10.3 per cent.'),
    6: (f6, 'Brake power of the worked example\'s engine if power follows air density. Hotter air or lower pressure means less air per stroke, so the hot afternoon test reads 34.27 kW instead of 40.0 kW.',
        'Two falling lines of brake power against intake temperature for 1.00 and 0.90 bar, with the reference point at 40 kW and the hot-day point at 34.27 kW.'),
    7: (f7, 'The four levers and the measured quantity each one moves, with the numbers of the two worked examples.',
        'Four rows: more air raises trapped mass, better mixture speeds the burn, less friction cuts friction power, better control holds the best point.'),
    8: (f8, 'The measuring chain and the record it produces for the worked example. The firing trace rises above the motored one after ignition and peaks after top dead centre.',
        'Block chain from piezo transducer to charge amplifier to data logger with a crank encoder, above a pressure against crank angle plot with firing and motored traces.'),
}
spec = make_spec(FIG)
