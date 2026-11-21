"""Claude's hand-drawn figures for ee-pe-u6 (Power Electronics: applications), one per chapter, drawn from each
chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """V_dc, I_d ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωδ])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def path(d, c=AC, w=2, dash=None, arrow=None, fill='none'):
    ds = f';stroke-dasharray:{dash}' if dash else ''
    m = f' marker-end="url(#ar-UID-{arrow})"' if arrow else ''
    return f'<path d="{d}" style="fill:{fill};stroke:{c};stroke-width:{w}{ds}"{m}/>'


def ground(x, y, c=INK):
    return L(x, y, x, y + 10, c, 2) + L(x - 12, y + 10, x + 12, y + 10, c, 2) + L(x - 8, y + 15, x + 8, y + 15, c, 2) + L(x - 4, y + 20, x + 4, y + 20, c, 2)


def reactor(x, y, n=3, r=7, c=AC):
    """series inductor drawn as n bumps from (x, y) to the right, width 2rn"""
    d = f'M{x},{y}' + ''.join(f' a{r},{r} 0 0 1 {2 * r},0' for _ in range(n))
    return path(d, c, 2.2)


# ---- 6.1 on-line UPS with the worked example's numbers ----
def f1():
    o = []
    y0, h = 150, 64
    B = [(16, 100, ['Mains', '230 V, 50 Hz'], PANEL, AC), (146, 120, ['Rectifier', 'and charger'], PANEL, AC),
         (296, 110, ['DC bus', '48 V'], ACS, AC), (436, 110, ['Inverter', 'η = 0.9'], PANEL, AC),
         (586, 118, ['Load', '640 W, 800 VA'], LVS, LV)]
    for x, w, lines, fl, st in B:
        o.append(boxt(x, y0, w, h, lines, fl, st, 14, bold_first=True))
    for (xa, wa, *_), (xb, *_r) in zip(B, B[1:]):
        o.append(L(xa + wa, y0 + h / 2, xb - 4, y0 + h / 2, AC, 2, arrow='n'))
    # battery under the bus
    o.append(L(351, y0 + h, 351, 262, AC, 2))
    o.append(boxt(286, 262, 130, 50, ['Battery', '48 V, 100 Ah'], PANEL, AC, 14, bold_first=True))
    o.append(T(430, 280, 'on mains failure the battery', 13, 'start', MUT))
    o.append(T(430, 298, 'gives 640 ÷ 0.9 = 711 W,', 13, 'start', MUT))
    o.append(T(430, 316, '711 ÷ 48 = 14.8 A', 13, 'start', MUT))
    # static bypass
    o.append(path(f'M66,{y0} L66,108 L645,108 L645,{y0 - 4}', LV, 2, dash='7 5', arrow='l'))
    o.append(Tb(356, 112, 'static bypass (thyristor switch): inverter overload or fault', 13, fill=LV))
    # maintenance bypass
    o.append(path(f'M46,{y0} L46,52 L665,52 L665,{y0 - 4}', L2, 2, dash='3 5', arrow='m'))
    o.append(Tb(356, 56, 'maintenance bypass (manual switch): isolates the UPS for service', 13, fill=MUT))
    o.append(T(360, 350, 'Usable energy = 48 V × 100 Ah × 0.8 = 3840 Wh;   backup = 3840 ÷ 711 = 5.4 h', 14, bold=True))
    return 368, ''.join(o)


# ---- 6.2 CC-CV charge of worked example 1: the charge is the area under the current ----
def f2():
    o = []
    x0, x1, yt, yb = 80, 690, 96, 312
    fx = lin(0, 7, x0, x1); fy = lin(0, 12, yb, yt)
    t1, t2 = 4.444, 6.296
    o.append(axes(x0, x1, yt, yb, [0, 1, 2, 3, 4, 5, 6, 7], [0, 2, 4, 6, 8, 10, 12], fx, fy, 'time (h)', 'charge current (A)'))
    o.append(P([(fx(0), fy(0)), (fx(0), fy(10)), (fx(t1), fy(10)), (fx(t1), fy(0))], AC, 0.1, fill=ACS))
    o.append(P([(fx(t1), fy(0)), (fx(t1), fy(10)), (fx(t2), fy(2)), (fx(t2), fy(0))], LV, 0.1, fill=LVS))
    o.append(P([(fx(0), fy(10)), (fx(t1), fy(10)), (fx(t2), fy(2))], AC, 3))
    o.append(L(fx(t2), fy(2), fx(t2), fy(0), AC, 2, dash='4 4'))
    o.append(T(fx(t1 / 2), fy(6), 'CC: 10 A × 4.44 h', 14, bold=True))
    o.append(T(fx(t1 / 2), fy(4.6), '= 44.4 Ah', 14))
    o.append(T(fx(5.15), fy(3.7), '11.1 Ah', 14, bold=True))
    o.append(T(fx(5.15), fy(2.3), '1.85 h', 13, fill=MUT))
    o.append(T(fx(t2) + 8, fy(2) - 8, 'stop at 2 A', 13, 'start', MUT))
    o.append(T(fx(t1), fy(10) - 10, '14.4 V reached', 13, 'middle', MUT))
    # voltage band
    o.append(R(fx(0), 40, fx(t1) - fx(0), 26, FIGBG, L2, 4))
    o.append(T((fx(0) + fx(t1)) / 2, 58, 'voltage rises towards 14.4 V', 13, fill=MUT))
    o.append(R(fx(t1), 40, fx(t2) - fx(t1), 26, LVS, LV, 4))
    o.append(T((fx(t1) + fx(t2)) / 2, 58, 'held at 14.4 V', 13, fill=LV))
    o.append(T(385, 372, '44.4 + 11.1 = 55.6 Ah = 50 Ah ÷ 0.90, delivered in 4.44 + 1.85 = 6.30 h', 14, bold=True))
    return 388, ''.join(o)


# ---- 6.3 induction heater of the worked example ----
def f3():
    o = []
    B = [(16, 150, ['DC link', '18.8 kW'], PANEL, AC), (196, 170, ['Full-bridge inverter', 'f = 2 kHz, 47 A'], ACS, AC),
         (396, 150, ['Tank capacitor', '≈ 30 µF, 60 kvar'], PANEL, AC), (576, 128, ['Work coil', '400 V, 157 A'], LVS, LV)]
    for x, w, lines, fl, st in B:
        o.append(boxt(x, 20, w, 60, lines, fl, st, 14, bold_first=True))
    for (xa, wa, *_), (xb, *_r) in zip(B, B[1:]):
        o.append(L(xa + wa, 50, xb - 4, 50, AC, 2, arrow='n'))
    # longitudinal section of the billet in the coil
    bx0, bx1, by0, by1, dl = 150, 450, 170, 320, 37.5
    o.append(R(bx0, by0, bx1 - bx0, by1 - by0, PANEL, INK, 2, sw=2))
    o.append(R(bx0, by0, bx1 - bx0, dl, LVS, LV, 0, sw=0))
    o.append(R(bx0, by1 - dl, bx1 - bx0, dl, LVS, LV, 0, sw=0))
    o.append(R(bx0, by0, bx1 - bx0, by1 - by0, 'none', INK, 2, sw=2))
    o.append(T((bx0 + bx1) / 2, (by0 + by1) / 2 + 5, 'cooler core', 14, fill=MUT))
    for i in range(7):
        x = bx0 + 22 + i * 42.6
        o.append(f'<circle cx="{x:.1f}" cy="{by0 - 22}" r="10" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
        o.append(C(x, by0 - 22, 3, AC))
        o.append(f'<circle cx="{x:.1f}" cy="{by1 + 22}" r="10" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
        o.append(L(x - 5, by1 + 17, x + 5, by1 + 27, AC, 2) + L(x - 5, by1 + 27, x + 5, by1 + 17, AC, 2))
        o.append(T(x, by0 + 24, '×', 15, fill=LV, bold=True))
        o.append(T(x, by1 - 14, '•', 18, fill=LV, bold=True))
    o.append(L(640, 80, 640, by0 - 22, LV, 2))
    o.append(L(640, by0 - 22, bx0 + 22 + 6 * 42.6 + 12, by0 - 22, LV, 2))
    o.append(T(470, by0 + 2, 'coil turns', 13, 'start', MUT))
    # dimension of delta
    o.append(L(bx0 - 18, by0, bx0 - 18, by0 + dl, INK, 1.5))
    o.append(L(bx0 - 24, by0, bx0 - 12, by0, INK, 1.5) + L(bx0 - 24, by0 + dl, bx0 - 12, by0 + dl, INK, 1.5))
    o.append(T(bx0 - 26, by0 + 24, 'δ', 15, 'end', bold=True))
    o.append(L(bx0 - 48, by0, bx0 - 48, by1, INK, 1.5))
    o.append(L(bx0 - 54, by0, bx0 - 42, by0, INK, 1.5) + L(bx0 - 54, by1, bx0 - 42, by1, INK, 1.5))
    o.append(T(bx0 - 56, (by0 + by1) / 2 + 5, '50 mm', 13, 'end'))
    o.append(T(470, 210, 'hot layer: δ = 12.5 mm', 14, 'start', LV, bold=True))
    o.append(T(470, 230, 'at 2 kHz above 770 °C', 13, 'start', MUT))
    o.append(T(470, 262, 'cold steel at 2 kHz:', 13, 'start', MUT))
    o.append(T(470, 280, 'δ ≈ 0.5 mm only', 13, 'start', MUT))
    o.append(T(300, 384, 'billet 50 mm × 100 mm, 1.54 kg, heated 20 → 900 °C in 60 s: 11.3 kW into the metal', 14, bold=True))
    o.append(T(300, 404, '• and × mark current out of and into the page: the eddy current is opposite to the coil current', 13, fill=MUT))
    return 418, ''.join(o)


# ---- 6.4 the ±500 kV bipolar link of the worked example ----
def f4():
    o = []
    yp, yn, ym = 92, 300, 196
    o.append(boxt(16, 156, 84, 80, ['AC', 'system A'], PANEL, AC, 14, bold_first=True))
    o.append(boxt(620, 156, 84, 80, ['AC', 'system B'], PANEL, AC, 14, bold_first=True))
    for (x, lab) in ((136, 'Rectifier'), (468, 'Inverter')):
        o.append(boxt(x, yp - 30, 116, 60, [lab, '+ pole'], ACS, AC, 14, bold_first=True))
        o.append(boxt(x, yn - 30, 116, 60, [lab, '− pole'], ACS, AC, 14, bold_first=True))
        xm = x + 58
        o.append(L(xm, yp + 30, xm, yn - 30, INK, 2))
        o.append(C(xm, ym, 4, INK))
        o.append(L(xm, ym, xm - 34, ym, INK, 2))
        o.append(ground(xm - 34, ym))
    # AC connections
    o.append(L(100, 180, 118, 180, AC, 2) + L(118, yp, 118, yn, AC, 2) + L(118, yp, 136, yp, AC, 2) + L(118, yn, 136, yn, AC, 2))
    o.append(L(620, 212, 602, 212, AC, 2) + L(602, yp, 602, yn, AC, 2) + L(584, yp, 602, yp, AC, 2) + L(584, yn, 602, yn, AC, 2))
    # DC poles with smoothing reactors
    for y, lab in ((yp, '+500 kV, I_d = 2000 A →'), (yn, '−500 kV, 2000 A returns ←')):
        o.append(L(252, y, 262, y, LV, 3))
        o.append(reactor(262, y, 3, 7, LV))
        o.append(L(304, y, 416, y, LV, 3))
        o.append(reactor(416, y, 3, 7, LV))
        o.append(L(458, y, 468, y, LV, 3))
        o.append(Tb(360, y - 16, lab, 13, fill=LV))
    o.append(T(360, yp + 26, 'smoothing reactors at both ends', 13, fill=MUT))
    o.append(T(360, ym - 4, 'pole-to-pole V_d = 1000 kV', 14, bold=True))
    o.append(T(360, ym + 18, 'earth current ≈ 0 when balanced', 13, fill=MUT))
    o.append(T(58, 262, 'filters,', 13, fill=MUT))
    o.append(T(58, 278, 'capacitors', 13, fill=MUT))
    o.append(T(662, 262, 'filters,', 13, fill=MUT))
    o.append(T(662, 278, 'capacitors', 13, fill=MUT))
    o.append(T(360, 360, 'P_d = 1000 kV × 2000 A = 2000 MW;   one pole out: 500 kV × 2000 A = 1000 MW', 14, bold=True))
    o.append(T(360, 382, 'each station absorbs about 1000 MVAr (Q ≈ 0.5 P_d) at full power from its own AC side', 13, fill=MUT))
    return 398, ''.join(o)


# ---- 6.5 TCR reactive power against firing angle, with the 60 MVAr fixed capacitor ----
def _qtcr(a_deg, XL=10.0, V=33e3):
    a = math.radians(a_deg)
    return (2 * (math.pi - a) + math.sin(2 * a)) / (math.pi * XL) * V ** 2 / 1e6


def f5():
    o = []
    x0, x1, yt, yb = 86, 560, 48, 300
    fx = lin(90, 180, x0, x1); fy = lin(0, 120, yb, yt)
    o.append(axes(x0, x1, yt, yb, [90, 105, 120, 135, 150, 165, 180], [0, 20, 40, 60, 80, 100, 120], fx, fy,
                  'firing angle α (degrees)', 'MVAr'))
    pts = [(fx(a), fy(_qtcr(a))) for a in range(90, 181, 2)]
    o.append(P(pts, AC, 3))
    o.append(L(fx(90), fy(60), fx(180), fy(60), LV, 2.5, dash='8 5'))
    a0 = 111.14
    o.append(L(fx(a0), fy(60), fx(a0), fy(0), INK, 1.5, dash='3 3'))
    o.append(C(fx(a0), fy(60), 5, INK))
    o.append(C(fx(90), fy(108.9), 5, AC))
    o.append(C(fx(120), fy(42.58), 5, AC))
    o.append(T(fx(90) + 10, fy(108.9) + 4, '108.9 at 90°', 13, 'start'))
    o.append(T(fx(120) + 10, fy(42.58) + 4, '42.6 at 120°', 13, 'start'))
    o.append(Tb(fx(a0) + 6, fy(60) - 12, 'net zero at α = 111°', 13, 'start', INK, bold=True))
    o.append(T(fx(152), fy(60) + 22, 'fixed capacitor supplies 60', 13, fill=LV))
    o.append(T(fx(160), fy(20), 'TCR absorbs', 13, fill=AC))
    # right panel: what the bus sees
    o.append(R(580, 48, 124, 252, PANEL, L2, 8))
    o.append(T(642, 74, 'SVC output', 14, bold=True))
    o.append(T(642, 92, '= 60 − Q_TCR', 13))
    o.append(T(642, 128, 'α = 180°', 13, bold=True))
    o.append(T(642, 146, '+60 leading', 13, fill=LV))
    o.append(T(642, 182, 'α = 111°', 13, bold=True))
    o.append(T(642, 200, '0', 13))
    o.append(T(642, 236, 'α = 90°', 13, bold=True))
    o.append(T(642, 254, '48.9 lagging', 13, fill=AC))
    o.append(T(330, 362, 'TCR: X_L = 10 Ω per phase on a 33 kV bus; Q = 3 × B_L(α) × V_ph²', 14, bold=True))
    return 378, ''.join(o)


# ---- 6.6 the home PV and battery system of the worked example ----
def f6():
    o = []
    o.append(boxt(16, 30, 150, 64, ['PV array', '4 × 335 = 1340 Wp'], PANEL, AC, 14, bold_first=True))
    o.append(boxt(206, 30, 120, 64, ['MPPT boost', '(P&O)'], PANEL, AC, 14, bold_first=True))
    o.append(boxt(366, 30, 100, 64, ['DC bus'], ACS, AC, 14, bold_first=True))
    o.append(boxt(506, 30, 198, 64, ['Grid-tied inverter', 'η = 0.9, current control'], LVS, LV, 14, bold_first=True))
    o.append(L(166, 62, 202, 62, AC, 2, arrow='n') + L(326, 62, 362, 62, AC, 2, arrow='n') + L(466, 62, 502, 62, AC, 2, arrow='n'))
    o.append(T(91, 116, '1340 × 4.5 h × 0.75', 13, fill=MUT))
    o.append(T(91, 134, '= 4522 Wh a day', 13, bold=True))
    o.append(T(426, 116, 'must give 4000 ÷ 0.9', 13, 'start', MUT))
    o.append(T(426, 134, '= 4444 Wh a day', 13, 'start', bold=True))
    o.append(L(416, 94, 416, 176, AC, 2))
    o.append(boxt(336, 176, 160, 60, ['Bidirectional', 'DC-DC converter'], PANEL, AC, 14, bold_first=True))
    o.append(L(416, 236, 416, 266, AC, 2))
    o.append(boxt(316, 266, 200, 64, ['Battery + BMS', '48 V, 350 Ah'], PANEL, AC, 14, bold_first=True))
    o.append(T(536, 286, 'store 4444 × 2 days', 13, 'start', MUT))
    o.append(T(536, 304, '÷ (0.6 × 0.9) = 16.5 kWh', 13, 'start', MUT))
    o.append(T(536, 322, '= 342.9 Ah at 48 V', 13, 'start', bold=True))
    o.append(L(605, 94, 605, 160, LV, 2, arrow='l'))
    o.append(boxt(556, 164, 148, 52, ['Home 4000 Wh', 'and AC grid'], PANEL, LV, 14, bold_first=True))
    o.append(T(16, 196, 'charge: power into the', 13, 'start', MUT))
    o.append(T(16, 214, 'battery; discharge: out', 13, 'start', MUT))
    o.append(T(16, 232, 'through the same converter', 13, 'start', MUT))
    o.append(T(360, 372, 'Grid lost: the inverter must stop feeding the line (anti-islanding)', 14, bold=True))
    return 388, ''.join(o)


# ---- 6.7 oven temperature loop with the worked example's heater ----
def f7():
    o = []
    o.append(boxt(16, 40, 110, 60, ['Set point', '60 °C'], PANEL, AC, 14, bold_first=True))
    o.append(f'<circle cx="166" cy="70" r="16" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(166, 75, 'Σ', 15, bold=True))
    o.append(boxt(214, 40, 120, 60, ['PID', 'controller'], PANEL, AC, 14, bold_first=True))
    o.append(boxt(376, 40, 150, 60, ['Thyristor pair', 'α = 90°'], ACS, AC, 14, bold_first=True))
    o.append(boxt(566, 40, 138, 60, ['Heater 26.45 Ω', '2 kW at 230 V'], LVS, LV, 14, bold_first=True))
    o.append(L(126, 70, 148, 70, AC, 2, arrow='n') + L(182, 70, 210, 70, AC, 2, arrow='n') + L(334, 70, 372, 70, AC, 2, arrow='n')
             + L(526, 70, 562, 70, AC, 2, arrow='n'))
    o.append(T(196, 60, 'e', 14, italic=True))
    o.append(T(355, 124, '50 %', 13, fill=MUT))
    o.append(T(544, 124, '162.6 V, 6.15 A', 13, fill=MUT))
    o.append(L(355, 100, 355, 110, L2, 1) + L(544, 100, 544, 110, L2, 1))
    o.append(L(635, 100, 635, 180, LV, 2, arrow='l'))
    o.append(boxt(556, 184, 148, 60, ['Oven', 'heater gives 1 kW'], PANEL, LV, 14, bold_first=True))
    o.append(L(556, 214, 470, 214, L2, 2, arrow='m'))
    o.append(boxt(330, 184, 136, 60, ['PT100 and', 'transmitter'], PANEL, L2, 14, bold_first=True))
    o.append(L(330, 214, 166, 214, L2, 2, dash='6 4'))
    o.append(L(166, 214, 166, 90, L2, 2, dash='6 4', arrow='m'))
    o.append(T(248, 236, '4–20 mA', 13, fill=MUT))
    o.append(T(180, 150, '−', 18, 'start', bold=True))
    o.append(T(136, 62, '+', 16, 'start', bold=True))
    o.append(T(360, 290, 'p = (V_rms ÷ V_s)²: 50 % power needs V_rms = 230 × √0.5 = 162.6 V, so α = 90°', 14, bold=True))
    o.append(T(360, 312, '25 % power needs 115 V, so α = 113.8°;  P = V_rms² ÷ R', 13, fill=MUT))
    return 328, ''.join(o)


FIG = {
    1: (f1, 'The on-line UPS of the worked example. The inverter always feeds the load; on a mains failure only the source of the DC bus changes, from the charger to the battery.',
        'Mains, rectifier and charger, 48 volt DC bus with a 100 ampere-hour battery, inverter of 0.9 efficiency and a 640 watt load; a static bypass and a separate maintenance bypass run above.'),
    2: (f2, 'Charging the 100 Ah battery of worked example 1. The charge returned is the area under the current: 44.4 Ah in the constant-current stage and 11.1 Ah while the current tapers.',
        'Plot of charge current against time: 10 amperes for 4.44 hours, then falling to 2 amperes at 6.30 hours; the two shaded areas are 44.4 and 11.1 ampere-hours.'),
    3: (f3, 'The induction heater of the worked example. The inverter drives the work coil at 2 kHz and the capacitor supplies the coil\'s vars; the current flows in a surface layer one skin depth thick.',
        'Chain of DC link, full-bridge inverter, tank capacitor and work coil above a section of a 50 millimetre billet whose top and bottom layers, 12.5 millimetres thick, carry the eddy current.'),
    4: (f4, 'The ±500 kV bipolar link of the worked example. Each pole carries 2000 A; the two currents cancel in the earth, and either pole can run alone with earth return.',
        'Rectifier and inverter stations, each with a plus and a minus pole converter, joined by two DC lines with smoothing reactors; the station midpoints are earthed.'),
    5: (f5, 'Reactive power of the TCR in the worked example as the firing angle moves from 90° to 180°. Against the 60 MVAr fixed capacitor, the SVC output runs from 48.9 MVAr lagging to 60 MVAr leading.',
        'Falling curve of TCR reactive power from 108.9 megavar at 90 degrees to zero at 180 degrees, crossing the 60 megavar capacitor line at 111 degrees.'),
    6: (f6, 'The home system of the worked example. The array covers a day\'s DC energy, the battery holds two days through its own converter, and the inverter is the only path to the home and the grid.',
        'PV array of 1340 watt-peak, MPPT boost, DC bus, grid-tied inverter to the home and grid; a bidirectional converter joins a 48 volt 350 ampere-hour battery to the bus.'),
    7: (f7, 'The oven loop of the worked example. The PID output of 50 % sets α = 90°, so the 2 kW heater gets 162.6 V and gives 1 kW; the PT100 reading closes the loop.',
        'Set point and measured temperature meet at a summing point; the PID controller sets the firing angle of a thyristor pair feeding a 26.45 ohm heater; a PT100 and transmitter feed back 4 to 20 milliamperes.'),
}
spec = make_spec(FIG)
