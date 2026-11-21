"""Claude's hand-drawn figures for me-ic-u4 (Automotive Engines: cooling, lubrication, crankcase ventilation, supercharging,
turbocharging and scavenging), one per chapter, drawn from each chapter's own worked example and numbers. Curves are computed
from the examples (the turbo spool curve from E = ½Jω², the oil curves from the Walther relation through two typical
published viscosities). Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """η_s, T_2 ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔ])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


FIG = {}


# ---- 4.1 heat balance of the genset and the liquid cooling loop ----
def f1():
    o = []
    o.append(T(40, 30, 'fuel power 93.3 kW (8 kg/h of diesel), typical split', 14, 'start', bold=True))
    x0, y0, W, H = 40, 42, 640, 40
    segs = [('brake 28.0 kW', 0.30, ACS, AC), ('coolant 28.0 kW', 0.30, LVS, LV), ('exhaust 28.0 kW', 0.30, NXS, NX), ('9.3', 0.10, PANEL, L2)]
    x = x0
    for lab, f, fill, st in segs:
        w = W * f
        o.append(R(x, y0, w, H, fill, st, 4))
        o.append(T(x + w / 2, y0 + 26, lab, 14, bold=lab != '9.3'))
        x += w
    o.append(T(680, y0 + H + 18, 'friction, radiation 9.3 kW', 13, 'end', MUT))
    # coolant share drops into the jacket
    o.append(L(W * 0.45 + x0, y0 + H + 4, 190, 158, LV, 2, dash='5 4', arrow='l'))
    o.append(T(330, 128, '28 kW into the coolant', 13, 'start', LV, bold=True))
    # engine with jacket
    o.append(R(80, 165, 220, 170, PANEL, AC, 10))
    o.append(R(100, 185, 180, 130, LVS, LV, 8))
    for cx in (140, 190, 240):
        o.append(R(cx - 18, 200, 36, 100, PANEL, AC, 4))
    o.append(T(190, 352, 'engine block: jacket round the cylinders', 13, fill=MUT))
    # thermostat and top hose
    o.append(L(300, 195, 340, 195, LV, 3))
    o.append(R(340, 180, 46, 30, NXS, NX, 4)); o.append(T(363, 172, 'thermostat', 13, bold=True))
    o.append(L(386, 195, 466, 195, LV, 3, arrow='l'))
    o.append(T(426, 216, 'hot', 13, fill=LV))
    # radiator
    o.append(R(470, 160, 90, 190, PANEL, AC, 6))
    for yy in range(178, 340, 16):
        o.append(L(476, yy, 554, yy, L2, 1.2))
    o.append(T(515, 150, 'radiator', 14, bold=True))
    # fan
    o.append(f'<ellipse cx="600" cy="255" rx="12" ry="60" style="fill:none;stroke:{MUT};stroke-width:2"/>')
    o.append(T(622, 250, 'fan', 13, 'start', MUT)); o.append(T(622, 268, 'pulls air', 13, 'start', MUT))
    # bottom hose and pump
    o.append(L(470, 320, 404, 320, LV, 3))
    o.append(f'<circle cx="390" cy="320" r="14" style="fill:var(--panel);stroke:{AC};stroke-width:2.5"/>'); o.append(L(376, 320, 304, 320, LV, 3, arrow='l'))
    o.append(T(390, 352, 'pump', 13, bold=True))
    o.append(T(436, 310, '6 K cooler', 13, fill=LV))
    o.append(boxt(330, 372, 350, 30, ['ṁ = 28.0 ÷ (4.18 × 6) = 1.12 kg/s'], ACS, AC, 14))
    return 418, ''.join(o)


FIG[1] = (f1, 'The worked example’s genset: of 93.3 kW of fuel power, about 28 kW goes into the coolant. The pump carries it from the jacket through '
              'the thermostat to the radiator, where the fan’s air takes it away; with a 6 K rise this needs 1.12 kg/s of water.',
          'A stacked bar splits 93.3 kilowatts of fuel power into brake power, coolant and exhaust of 28 kilowatts each and 9.3 kilowatts of friction '
          'and radiation. Below, a cooling loop: engine jacket, thermostat, radiator with fan, and pump. A box gives the coolant flow 1.12 kilograms per second.')


# ---- 4.2 thermosyphon loop with the example's densities and the pressure cap ----
def f2():
    o = []
    # engine jacket low left, radiator high right
    o.append(R(60, 250, 170, 120, PANEL, AC, 10)); o.append(R(78, 268, 134, 84, LVS, LV, 8))
    o.append(T(145, 316, 'engine jacket', 14, bold=True))
    o.append(R(440, 60, 120, 200, PANEL, AC, 6))
    for yy in range(96, 236, 16): o.append(L(448, yy, 552, yy, L2, 1.2))
    o.append(R(440, 60, 120, 26, ACS, AC, 4)); o.append(T(500, 79, 'top tank', 13))
    o.append(T(432, 160, 'radiator', 14, 'end', bold=True))
    # riser: jacket top -> radiator top tank
    o.append(P([(200, 250), (200, 73), (436, 73)], NX, 4))
    o.append(L(200, 200, 200, 150, NX, 4, arrow='x'))
    o.append(T(212, 166, 'riser: 80 °C', 14, 'start', NX, bold=True)); o.append(T(212, 184, 'ρ_h = 971.8 kg/m³', 13, 'start', NX))
    # downcomer: radiator bottom -> jacket bottom
    o.append(P([(500, 260), (500, 400), (100, 400), (100, 370)], AC, 4))
    o.append(L(380, 400, 300, 400, AC, 4, arrow='n'))
    o.append(T(330, 425, 'downcomer: 40 °C, ρ_c = 992.2 kg/m³', 14, 'middle', AC, bold=True))
    # height dimension between centres
    o.append(L(590, 160, 590, 310, MUT, 1.5, arrow='m')); o.append(L(590, 310, 590, 160, MUT, 1.5, arrow='m')); o.append(L(232, 310, 632, 310, MUT, 1.2, dash='4 3'))
    o.append(L(565, 160, 632, 160, MUT, 1.2, dash='4 3'))
    o.append(T(600, 245, 'h = 0.4 m', 14, 'start', MUT, bold=True))
    o.append(T(640, 175, 'radiator', 13, 'start', MUT)); o.append(T(640, 191, 'centre', 13, 'start', MUT))
    o.append(T(640, 315, 'jacket', 13, 'start', MUT)); o.append(T(640, 331, 'centre', 13, 'start', MUT))
    # pressure cap
    o.append(R(480, 34, 40, 18, NXS, NX, 4)); o.append(L(500, 52, 500, 60, NX, 2))
    o.append(T(470, 30, 'cap 100 kPa: boils at 120.4 °C', 13, 'end', NX, bold=True))
    o.append(boxt(250, 196, 170, 50, ['Δp = 20.4 × 9.81 × 0.4', '= 80 Pa, no pump'], ACS, AC, 14))
    return 440, ''.join(o)


FIG[2] = (f2, 'The thermosyphon loop of the first worked example. Hot water at 80 °C rises from the jacket to the radiator top tank, and water cooled to '
              '40 °C falls back; the 20.4 kg/m³ density difference over 0.4 m gives only 80 Pa of driving pressure. The pressure cap lifts the boiling point to 120.4 °C.',
          'A cooling loop with the engine jacket low on the left and the radiator high on the right. A riser carries 80 degree water up to the top tank; '
          'a downcomer returns 40 degree water to the jacket. The height between centres is 0.4 metres and the driving pressure is 80 pascals.')


# ---- 4.3 wet sump pressure circuit and the motoring-test power split ----
def f3():
    o = []
    top = 40
    boxes = [(30, 'strainer'), (170, 'pump'), (310, 'filter'), (450, 'main gallery')]
    for x, lab in boxes:
        o.append(boxt(x, top, 120 if lab != 'main gallery' else 240, 46, [lab], PANEL if lab != 'pump' else ACS, AC, 14, bold_first=True))
    for x in (150, 290, 430):
        o.append(L(x, top + 23, x + 18, top + 23, AC, 2.5, arrow='n'))
    # bypass over filter
    o.append(arc(320, top, 420, top, 0.22, MUT, 1.6, 'm', dash='5 4'))
    o.append(T(370, top - 26, 'bypass if clogged', 13, fill=MUT))
    # relief valve under pump
    o.append(boxt(170, 120, 120, 40, ['relief valve'], NXS, NX, 13))
    o.append(L(230, top + 46, 230, 116, NX, 2, arrow='x'))
    o.append(L(230, 160, 230, 296, NX, 2, dash='5 4', arrow='x'))
    o.append(T(238, 240, 'surplus oil', 13, 'start', NX))
    # gallery feeds
    feeds = [(380, 'main bearings'), (510, 'camshaft'), (620, 'rockers')]
    for x, lab in feeds:
        o.append(L(x if x > 450 else 470, top + 46, x, 168, AC, 2, arrow='n'))
        o.append(boxt(x - 55, 172, 110, 38, [lab], PANEL, AC, 13))
    o.append(L(380, 210, 380, 228, AC, 2, arrow='n')); o.append(boxt(325, 232, 110, 38, ['big ends'], PANEL, AC, 13))
    o.append(T(470, 120, 'drillings', 13, 'start', MUT))
    # sump
    o.append(R(30, 300, 660, 40, LVS, LV, 8)); o.append(T(360, 325, 'sump: oil returns by gravity', 14, bold=True))
    for x in (380, 510, 620):
        o.append(L(x, 272 if x == 380 else 212, x, 296, LV, 1.8, dash='4 4', arrow='l'))
    o.append(L(90, 296, 90, top + 50, AC, 2.5, arrow='n'))
    o.append(T(100, 200, 'pick-up', 13, 'start', MUT))
    # power split bar from the worked example
    y = 372; fx = lin(0, 30, 30, 690)
    o.append(R(fx(0), y, fx(22.46) - fx(0), 30, ACS, AC, 4)); o.append(T((fx(0) + fx(22.46)) / 2, y + 20, 'brake power 22.46 kW', 14, bold=True))
    o.append(R(fx(22.46), y, fx(30) - fx(22.46), 30, NXS, NX, 4)); o.append(T((fx(22.46) + fx(30)) / 2, y + 20, 'FP 7.54 kW', 14, bold=True))
    o.append(T(30, y - 8, 'motoring test at 3000 rev/min: indicated power 30 kW, η_m = 74.9 %', 13, 'start', MUT))
    return 418, ''.join(o)


FIG[3] = (f3, 'A wet sump pressure circuit: the pump lifts oil through the strainer and sends it through the filter to the main gallery, which feeds the '
              'bearings and valve gear; oil drains back by gravity, and the relief valve returns surplus oil. The bar splits the worked example’s 30 kW of indicated power.',
          'Flow diagram of a wet sump system: strainer, pump with relief valve, filter with bypass, main gallery, drillings to main bearings, big ends, '
          'camshaft and rockers, and drains back to the sump. A bar below shows brake power 22.46 kilowatts and friction power 7.54 kilowatts.')


# ---- 4.4 viscosity against temperature (Walther relation through typical published values) ----
def walther(t40, t100):
    """log log(ν + 0.7) = A − B log T, through two points"""
    T1, T2 = 313.15, 373.15
    y1, y2 = math.log10(math.log10(t40 + 0.7)), math.log10(math.log10(t100 + 0.7))
    B = (y1 - y2) / (math.log10(T2) - math.log10(T1)); A = y1 + B * math.log10(T1)
    return lambda t: 10 ** (10 ** (A - B * math.log10(t + 273.15))) - 0.7


def f4():
    o = []
    x0, x1, y0, y1 = 90, 620, 40, 370
    fx = lin(20, 120, x0, x1)
    fy = lambda v: y1 - (math.log10(v) - math.log10(5)) / (math.log10(500) - math.log10(5)) * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for t in (20, 40, 60, 80, 100, 120):
        X = fx(t); o += [L(X, y1, X, y1 + 5, L2, 1.5), T(X, y1 + 20, str(t), 13, fill=MUT)]
    for v in (5, 10, 20, 50, 100, 200, 500):
        Y = fy(v); o += [L(x0 - 5, Y, x0, Y, L2, 1.5), L(x0, Y, x1, Y, LN, 1), T(x0 - 9, Y + 4.5, str(v), 13, 'end', MUT)]
    o.append(T((x0 + x1) / 2, y1 + 40, 'oil temperature (°C)', 14, fill=MUT))
    o.append(T(x0, y0 - 14, 'kinematic viscosity ν (mm²/s, log scale)', 14, 'start', MUT))
    mono, multi = walther(150, 14.5), walther(95, 14.3)
    ts = [20 + 2.5 * i for i in range(41)]
    o.append(P([(fx(t), fy(mono(t))) for t in ts], NX, 3))
    o.append(P([(fx(t), fy(multi(t))) for t in ts], AC, 3))
    o.append(Tb(fx(30) + 6, fy(mono(30)) - 10, 'single grade SAE 40', 13, 'start', NX, bold=True))
    o.append(Tb(fx(30) - 6, fy(multi(30)) + 24, 'multigrade 10W-40', 13, 'start', AC, bold=True))
    # the SAE 40 band at 100 C and the example oil
    X = fx(100)
    o.append(R(X - 7, fy(16.3), 14, fy(12.5) - fy(16.3), LVS, LV, 3))
    o.append(T(X + 14, fy(16.3) - 30, 'SAE 40 band at 100 °C:', 13, 'start', LV, bold=True))
    o.append(T(X + 14, fy(16.3) - 14, '12.5 to 16.3 mm²/s', 13, 'start', LV))
    o.append(C(X, fy(14.3), 6, LV))
    o.append(T(X - 12, fy(14.3) + 36, 'example oil 14.3 mm²/s', 13, 'end', LV, bold=True))
    o.append(T(fx(40) + 8, fy(150) - 8, '150', 13, 'start', NX)); o.append(C(fx(40), fy(150), 4.5, NX))
    o.append(T(fx(40) - 10, fy(95) + 18, '95', 13, 'end', AC)); o.append(C(fx(40), fy(95), 4.5, AC))
    return 420, ''.join(o)


FIG[4] = (f4, 'Viscosity falls steeply as oil warms, so it is plotted on a log scale. Both oils are about 14.4 mm²/s at 100 °C, inside the SAE 40 band, but the '
              'multigrade (high viscosity index) is far thinner when cold. The second worked example’s oil, 14.3 mm²/s, sits in the band.',
          'Kinematic viscosity on a log scale against temperature from 20 to 120 degrees Celsius for a single grade SAE 40 oil, 150 at 40 degrees, '
          'and a 10W-40 multigrade, 95 at 40 degrees. Both meet near 14 at 100 degrees, where a bar marks the SAE 40 band and a dot the example oil.')


# ---- 4.5 positive crankcase ventilation layout ----
def f5():
    o = []
    # cylinder, head and rocker cover
    o.append(R(250, 70, 200, 34, PANEL, AC, 6)); o.append(T(350, 92, 'rocker cover', 13, bold=True))
    o.append(R(250, 104, 200, 36, PANEL, AC, 2)); o.append(T(350, 127, 'head', 13, fill=MUT))
    o.append(L(270, 140, 270, 280, AC, 2.5)); o.append(L(430, 140, 430, 280, AC, 2.5))
    o.append(R(276, 196, 148, 60, PANEL, AC, 4)); o.append(T(350, 232, 'piston', 13, bold=True))
    o.append(L(276, 204, 424, 204, NX, 2)); o.append(L(276, 212, 424, 212, NX, 2))
    o.append(T(350, 168, 'combustion chamber', 13, fill=MUT))
    # crankcase
    o.append(f'<path d="M270,280 L220,300 L220,400 Q350,430 480,400 L480,300 L430,280" style="fill:none;stroke:{AC};stroke-width:2.5"/>')
    o.append(T(350, 330, 'crankcase', 14, bold=True)); o.append(T(350, 395, 'oil in the sump', 13, fill=MUT))
    # blow-by arrows past the rings
    for x in (282, 418):
        o.append(L(x, 190, x, 272, NX, 2.5, arrow='x'))
    o.append(T(470, 238, 'blow-by past the rings', 13, 'start', NX, bold=True))
    o.append(T(470, 256, '25 L/min = 1.31 % of', 13, 'start', NX))
    o.append(T(470, 274, '1912.5 L/min intake air', 13, 'start', NX))
    # air cleaner, throttle, manifold
    o.append(boxt(30, 40, 130, 46, ['air cleaner'], PANEL, AC, 14, bold_first=True))
    o.append(L(95, 86, 95, 150, AC, 3)); o.append(R(80, 150, 30, 22, ACS, AC, 3)); o.append(T(118, 166, 'throttle', 13, 'start'))
    o.append(P([(95, 172), (95, 210), (244, 210)], AC, 3)); o.append(L(200, 210, 244, 210, AC, 3, arrow='n'))
    o.append(T(140, 230, 'intake manifold', 13, 'middle', MUT))
    # fresh air hose: clean side of cleaner -> rocker cover
    o.append(P([(160, 50), (420, 50), (420, 70)], LV, 2.5, dash='6 4')); o.append(L(330, 50, 370, 50, LV, 2.5, arrow='l'))
    o.append(T(300, 40, 'filtered fresh air from the clean side', 13, 'middle', LV, bold=True))
    # PCV valve: rocker cover -> manifold below throttle
    o.append(R(212, 74, 34, 22, NXS, NX, 4)); o.append(L(246, 85, 250, 85, NX, 2))
    o.append(T(206, 112, 'PCV valve and', 13, 'end', NX, bold=True)); o.append(T(206, 128, 'oil separator', 13, 'end', NX, bold=True))
    o.append(L(229, 96, 229, 202, NX, 2.5, arrow='x'))
    o.append(T(470, 150, 'vacuum draws the gas into', 13, 'start', NX)); o.append(T(470, 168, 'the manifold: burnt in', 13, 'start', NX)); o.append(T(470, 186, 'the cylinders', 13, 'start', NX))
    return 430, ''.join(o)


FIG[5] = (f5, 'A closed PCV system. Blow-by from the worked example, 25 L/min or 1.31 per cent of the intake air, leaks past the rings into the crankcase; '
              'filtered air sweeps it out, and manifold vacuum draws it through the oil separator and PCV valve into the intake below the throttle.',
          'Section of an engine with rocker cover, head, piston and crankcase. Arrows show blow-by passing the rings into the crankcase. A fresh air hose runs '
          'from the air cleaner to the rocker cover, and a hose from the PCV valve runs to the intake manifold below the throttle.')


# ---- 4.6 roots blower and what 1.6 bar of boost really buys ----
def lobe(cx, cy, ang, r=36, w=16, c=AC):
    """a two-lobe rotor as two overlapping round lobes"""
    a = math.radians(ang)
    dx, dy = math.cos(a) * (r - w / 2) * 0.62, math.sin(a) * (r - w / 2) * 0.62
    return (f'<line x1="{cx - dx:.1f}" y1="{cy - dy:.1f}" x2="{cx + dx:.1f}" y2="{cy + dy:.1f}" '
            f'style="stroke:{c};stroke-width:{w * 1.9:.1f};stroke-linecap:round"/>')


def f6():
    o = []
    # casing and rotors
    o.append(R(40, 70, 230, 130, PANEL, AC, 40))
    o.append(lobe(110, 135, 90)); o.append(lobe(200, 135, 0))
    o.append(C(110, 135, 5, INK)); o.append(C(200, 135, 5, INK))
    o.append(T(112, 300, 'roots blower: two rotors,', 13, 'start', bold=True)); o.append(T(112, 318, 'no compression inside', 13, 'start', bold=True))
    o.append(L(155, 250, 155, 205, LV, 3, arrow='l')); o.append(T(155, 268, 'air in: 1.0 bar, 300 K', 13, fill=LV, bold=True))
    o.append(L(155, 66, 155, 30, NX, 3, arrow='x'))
    o.append(T(165, 24, 'to manifold: 1.6 bar, 361.6 K', 13, 'start', NX, bold=True))
    # belt drive
    o.append(C(70, 300, 22, PANEL)); o.append(f'<circle cx="70" cy="300" r="22" style="fill:none;stroke:{MUT};stroke-width:2"/>')
    o.append(L(52, 287, 92, 140, MUT, 2)); o.append(L(88, 312, 128, 150, MUT, 2))
    o.append(T(70, 342, 'crank pulley', 13, fill=MUT)); o.append(T(70, 360, 'drive 7.15 kW', 13, fill=MUT, bold=True))
    # bars: pressure, density, net power ratios
    fx = lin(0, 1.7, 330, 690); base = fx(1.0)
    rows = [(80, 'pressure ratio', 1.60, MUT, PANEL), (160, 'air density ratio', 1.327, AC, ACS), (240, 'net power ratio', 92.4 / 75, LV, LVS)]
    for y, lab, v, c, fill in rows:
        o.append(T(330, y - 10, lab, 14, 'start', bold=True))
        o.append(R(fx(0), y, fx(v) - fx(0), 30, fill, c, 4))
        o.append(T(fx(v) + 8, y + 21, f'× {v:.2f}', 14, 'start', c, bold=True))
    o.append(L(base, 60, base, 286, INK, 1.5, dash='5 4')); o.append(T(base, 304, 'naturally aspirated = 1', 13, fill=MUT))
    o.append(T(330, 336, '1.6 × 300 ÷ 361.6 = 1.33;  net power 99.6 − 7.15 = 92.4 kW', 13, 'start', MUT))
    o.append(T(330, 356, 'from 75 kW: a gain of 23 %, not 60 %', 13, 'start', MUT, bold=True))
    return 376, ''.join(o)


FIG[6] = (f6, 'The worked example’s belt-driven roots blower. It raises the pressure 1.6 times, but the air leaves at 361.6 K, so its density rises only 1.33 '
              'times; after the 7.15 kW it takes from the crank, net power rises 1.23 times.',
          'Left: a roots blower with two rotors in a casing, air in at 1.0 bar and 300 kelvin and out at 1.6 bar and 361.6 kelvin, belt driven from the '
          'crank pulley. Right: three bars against the naturally aspirated value of 1: pressure ratio 1.60, density ratio 1.33 and net power ratio 1.23.')


# ---- 4.7 turbo spool-up after a throttle step, from E = 1/2 J w^2 ----
def f7():
    o = []
    x0, x1, y0, y1 = 90, 670, 40, 360
    fx = lin(0, 1.6, x0, x1); fy = lin(0, 160, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.4, 0.8, 1.2, 1.6], [0, 40, 80, 120, 160], fx, fy, 'time after the throttle step (s)', 'rotor speed (1000 rev/min)', lambda v: f'{v:.1f}'))
    w1 = 30000 * 2 * math.pi / 60; P = 1800.0
    for J, c, lab in ((2.0e-5, AC, 'J = 2.0 × 10⁻⁵ kg·m²'), (1.4e-5, LV, 'lighter rotor, J 30 % less')):
        pts = []
        for i in range(0, 161):
            t = i * 0.01
            w = math.sqrt(w1 ** 2 + 2 * P * t / J)
            n = w * 60 / (2 * math.pi) / 1000
            if n > 150: n = 150
            pts.append((fx(t), fy(n)))
        o.append(P_(pts, c))
    o.append(L(x0, fy(150), x1, fy(150), MUT, 1.2, dash='5 4')); o.append(T(x1, fy(150) - 8, 'full boost speed 150 000', 13, 'end', MUT))
    o.append(L(fx(1.316), fy(150), fx(1.316), y1, AC, 1.5, dash='4 4')); o.append(Tb(fx(1.316), y1 - 12, '1.32 s', 14, 'middle', AC, bold=True))
    o.append(L(fx(0.921), fy(150), fx(0.921), y1, LV, 1.5, dash='4 4')); o.append(Tb(fx(0.921), y1 - 12, '0.92 s', 14, 'middle', LV, bold=True))
    o.append(Tb(fx(0.62), fy(100) + 40, 'J = 2.0 × 10⁻⁵ kg·m²', 13, 'start', AC, bold=True))
    o.append(Tb(fx(0.36), fy(118), 'J 30 % less', 13, 'end', LV, bold=True))
    o.append(C(fx(0), fy(30), 5, INK)); o.append(T(fx(0) + 10, fy(30) + 20, 'start 30 000', 13, 'start', MUT))
    o.append(T(fx(0.8), fy(20), '1.8 kW surplus turbine power fills ½Jω²', 13, 'middle', MUT))
    return 420, ''.join(o)


def P_(pts, c):
    return P(pts, c, 3)


FIG[7] = (f7, 'The second worked example as a curve: with 1.8 kW of surplus turbine power, the rotor takes 1.32 s to climb from 30 000 to 150 000 rev/min. A rotor '
              'with 30 per cent less inertia gets there in 0.92 s.',
          'Rotor speed in thousands of revolutions per minute against time from 0 to 1.6 seconds. Two rising curves start at 30 thousand; the heavier rotor '
          'reaches 150 thousand at 1.32 seconds, the lighter one at 0.92 seconds.')


# ---- 4.8 VGT vanes closed and open, and the intercooler of the worked example ----
def nozzle(cx, cy, closed):
    o = [f'<circle cx="{cx}" cy="{cy}" r="30" style="fill:var(--accent-soft);stroke:{AC};stroke-width:2"/>',
         f'<circle cx="{cx}" cy="{cy}" r="88" style="fill:none;stroke:{L2};stroke-width:1.5;stroke-dasharray:4 4"/>']
    tilt = 72 if closed else 28
    for i in range(10):
        a = math.radians(i * 36)
        px, py = cx + 62 * math.cos(a), cy + 62 * math.sin(a)
        b = a + math.radians(90 - tilt) + math.pi / 2
        dx, dy = 15 * math.cos(b), 15 * math.sin(b)
        o.append(f'<line x1="{px - dx:.1f}" y1="{py - dy:.1f}" x2="{px + dx:.1f}" y2="{py + dy:.1f}" style="stroke:{NX};stroke-width:5;stroke-linecap:round"/>')
    return ''.join(o)


def f8():
    o = []
    o.append(nozzle(130, 125, True)); o.append(nozzle(370, 125, False))
    o.append(T(130, 232, 'low speed: vanes nearly closed', 13, bold=True)); o.append(T(130, 250, 'narrow throat, fast gas, quick spool', 13, fill=MUT))
    o.append(T(370, 232, 'high speed: vanes open', 13, bold=True)); o.append(T(370, 250, 'wide throat, low back pressure', 13, fill=MUT))
    o.append(T(130, 130, 'turbine', 13)); o.append(T(370, 130, 'turbine', 13))
    o.append(boxt(530, 60, 170, 120, ['vane ring', 'the actuator turns', 'all vanes together', 'to set the area'], PANEL, L2, 13, bold_first=True))
    # intercooler chain
    y = 300
    o.append(boxt(20, y, 190, 70, ['compressor out', '1.6 bar, 361.6 K', 'density × 1.33'], NXS, NX, 14, bold_first=True))
    o.append(L(212, y + 35, 252, y + 35, AC, 3, arrow='n'))
    o.append(R(256, y - 6, 190, 82, PANEL, AC, 6))
    for xx in range(270, 440, 14): o.append(L(xx, y + 2, xx, y + 68, L2, 1.2))
    o.append(Tb(351, y + 30, 'intercooler, ε = 0.80', 14, 'middle', bold=True)); o.append(Tb(351, y + 52, 'cooling air 303 K', 13, 'middle', MUT))
    o.append(L(448, y + 35, 488, y + 35, AC, 3, arrow='n'))
    o.append(boxt(492, y, 208, 70, ['to manifold', '1.6 bar, 314.7 K', 'density × 1.53'], LVS, LV, 14, bold_first=True))
    o.append(T(360, y + 104, 'same boost, 15 % more air: 1.525 ÷ 1.327 = 1.15', 14, 'middle', MUT, bold=True))
    return 420, ''.join(o)


FIG[8] = (f8, 'Top: a variable geometry turbine closes its vanes at low flow to speed the gas onto the wheel, and opens them at high flow. Bottom: the worked '
              'example’s intercooler cools the 361.6 K charge to 314.7 K at the same 1.6 bar, lifting the density ratio from 1.33 to 1.53.',
          'Two turbine nozzle rings with ten vanes each: nearly closed for low speed and open for high speed. Below, a chain from the compressor outlet at '
          '361.6 kelvin through an intercooler of effectiveness 0.8 to the manifold at 314.7 kelvin, density ratio rising from 1.33 to 1.53.')


# ---- 4.9 cross, loop and uniflow scavenging ----
def cyl(x, label):
    o = [L(x, 60, x, 300, AC, 2.5), L(x + 150, 60, x + 150, 300, AC, 2.5), L(x, 60, x + 150, 60, AC, 2.5)]
    o.append(R(x + 4, 250, 142, 46, PANEL, MUT, 4))
    o.append(T(x + 75, 330, label, 15, bold=True))
    return o


def f9():
    o = []
    # cross: transfer left, exhaust right, deflector on the crown
    x = 70; o += cyl(x, 'cross')
    o.append(R(x - 14, 200, 14, 44, LVS, LV, 2)); o.append(R(x + 150, 180, 14, 50, NXS, NX, 2))
    o.append(f'<path d="M{x + 20},250 L{x + 20},222 L{x + 40},250 Z" style="fill:{AC};stroke:{AC};stroke-width:2"/>')
    o.append(f'<path d="M{x + 6},226 C{x + 30},120 {x + 120},70 {x + 140},200" style="fill:none;stroke:{LV};stroke-width:3" marker-end="url(#ar-UID-l)"/>')
    o.append(L(x + 10, 238, x + 140, 228, NX, 2, dash='5 4', arrow='x'))
    o.append(T(x + 75, 350, 'deflector crown; some', 13, fill=MUT)); o.append(T(x + 75, 368, 'charge short-circuits', 13, fill=MUT))
    # loop: transfer ports flank the exhaust, aimed at the far wall
    x = 305; o += cyl(x, 'loop (Schnürle)')
    o.append(R(x + 150, 160, 14, 50, NXS, NX, 2)); o.append(R(x + 150, 214, 14, 30, LVS, LV, 2))
    o.append(f'<path d="M{x + 146},236 C{x + 40},236 {x + 6},200 {x + 14},130 C{x + 20},70 {x + 120},70 {x + 140},170" style="fill:none;stroke:{LV};stroke-width:3" marker-end="url(#ar-UID-l)"/>')
    o.append(T(x + 75, 350, 'charge loops up the far', 13, fill=MUT)); o.append(T(x + 75, 368, 'wall, over the head', 13, fill=MUT))
    # uniflow: inlet ports at the bottom, exhaust valve in the head
    x = 545; o += cyl(x, 'uniflow')
    o.append(R(x - 14, 214, 14, 30, LVS, LV, 2)); o.append(R(x + 150, 214, 14, 30, LVS, LV, 2))
    o.append(f'<path d="M{x + 55},60 L{x + 55},76 L{x + 95},76 L{x + 95},60" style="fill:{NXS};stroke:{NX};stroke-width:2"/>')
    o.append(L(x + 75, 60, x + 75, 30, NX, 3, arrow='x'))
    for xx in (x + 40, x + 110):
        o.append(L(xx, 236, xx, 96, LV, 3, arrow='l'))
    o.append(T(x + 75, 350, 'one direction; needs a', 13, fill=MUT)); o.append(T(x + 75, 368, 'blower and exhaust valve', 13, fill=MUT))
    o.append(T(8, 178, 'transfer', 13, 'start', LV)); o.append(T(8, 194, 'port', 13, 'start', LV))
    o.append(T(238, 200, 'exhaust', 13, 'start', NX))
    o.append(T(x + 62, 30, 'exhaust valve', 13, 'end', NX))
    o.append(T(360, 402, 'worked example: D = 0.80, η_t = 0.80, so η_s = 0.64 (mixing model 0.55, displacement 0.80)', 13, 'middle', MUT, bold=True))
    return 418, ''.join(o)


FIG[9] = (f9, 'The three scavenging layouts. Cross flow turns the charge up with a deflector crown but lets some short-circuit; loop flow sends it up the far '
              'wall and over the head; uniflow moves it one way, from inlet ports to an exhaust valve.',
          'Three two-stroke cylinders. Cross: transfer port left, exhaust right, a deflector on the piston turns the charge up and a dashed arrow shows '
          'short-circuiting. Loop: ports on one side, the charge loops round the far wall. Uniflow: inlet ports at the bottom, an exhaust valve in the head.')

spec = make_spec(FIG)
