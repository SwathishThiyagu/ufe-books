"""Claude's hand-drawn figures for ch-mass-u7 (Humidification, Cooling Towers and Drying), one per chapter,
drawn from each chapter's own worked example. Saturation pressures come from the IAPWS-IF97 saturation equation,
so the curves are the real air-water curves at 101.325 kPa. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG, AFTER = {}, {}
P0 = 101.325


def sb(base, s):
    return f'{base}<tspan baseline-shift="sub" font-size="11">{s}</tspan>'


_SUBRE = re.compile(r'(?<![A-Za-z0-9_.#=])([A-Za-zλ]{1,2})_([A-Za-z0-9]+)')


def capsub(s):
    return _SUBRE.sub(lambda m: m.group(1) + '<sub>' + m.group(2) + '</sub>', s)


def psat(t):
    """IAPWS-IF97 saturation pressure of water, t in °C, kPa"""
    T = t + 273.15
    n = [0.11670521452767e4, -0.72421316703206e6, -0.17073846940092e2, 0.12020824702470e5, -0.32325550322333e7,
         0.14915108613530e2, -0.48232657361591e4, 0.40511340542057e6, -0.23855557567849, 0.65017534844798e3]
    th = T + n[8] / (T - n[9]); A = th * th + n[0] * th + n[1]; B = n[2] * th * th + n[3] * th + n[4]; Cc = n[5] * th * th + n[6] * th + n[7]
    return (2 * Cc / (-B + math.sqrt(B * B - 4 * A * Cc))) ** 4 * 1000


def Ys(t, rh=1.0):
    p = rh * psat(t)
    return 0.622 * p / (P0 - p)


def hs(t):
    y = Ys(t)
    return 1.005 * t + y * (2500 + 1.88 * t)


def chart(x0, x1, y0, y1, t0, t1, ymax, yt, xt, rhs=(0.2, 0.4, 0.6, 0.8), rhlab=True):
    """a psychrometric chart frame: Y (kg/kg dry air) against dry bulb, saturation and RH curves; returns (svg, fx, fy)"""
    fx = lambda t: x0 + (t - t0) / (t1 - t0) * (x1 - x0)
    fy = lambda y: y1 - y / ymax * (y1 - y0)
    o = [axes(x0, x1, y0, y1, xt, yt, fx, fy, 'dry-bulb temperature (°C)', 'humidity Y (kg water/kg dry air)', lambda v: f'{v:g}', lambda v: f'{v:.3f}')]
    for rh in rhs:
        pts = []
        t = t0
        while t <= t1 + 1e-9:
            y = Ys(t, rh)
            if y <= ymax: pts.append((fx(t), fy(y)))
            t += 0.25
        o.append(P(pts, L2, 1.2, '4 3'))
        if rhlab and pts:
            X, Yp = pts[-1]
            o.append(T(X + 4, Yp + 4, f'{int(rh * 100)} %', 12, 'start', MUT))
    pts = []
    t = t0
    while t <= t1 + 1e-9:
        y = Ys(t)
        if y <= ymax * 1.0001: pts.append((fx(t), fy(y)))
        t += 0.1
    o.append(P(pts, AC, 2.6))
    return ''.join(o), fx, fy


# ---- 7.1 vapour pressure, the state point and its dew point ----
def f1():
    o = []
    x0, x1, y0, y1 = 70, 440, 46, 300
    fx = lambda t: x0 + t / 60 * (x1 - x0)
    fy = lambda p: y1 - p / 20 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 10, 20, 30, 40, 50, 60], [0, 5, 10, 15, 20], fx, fy, 'temperature (°C)', 'vapour pressure of water (kPa)', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    o.append(P([(fx(i * 0.25), fy(psat(i * 0.25))) for i in range(241)], AC, 3))
    o.append(T(fx(51), fy(psat(51)) - 8, sb('p', 'AS') + '(T)', 13, 'end', AC, True))
    pa = 0.20 * psat(40); td = 12.77
    o.append(L(fx(40), fy(psat(40)), fx(40), y1, L2, 1.2, '3 3'))
    o.append(C(fx(40), fy(psat(40)), 5))
    o.append(T(fx(40) - 8, fy(psat(40)) - 8, '7.38 kPa at 40 °C', 13, 'end', AC, True))
    o.append(T(fx(40) - 8, fy(psat(40)) + 10, '(Antoine: 7.36)', 12, 'end', MUT))
    o.append(L(fx(td), fy(pa), fx(40), fy(pa), LV, 2.2, None, 'l'))
    o.append(C(fx(40), fy(pa), 6, LV, 'var(--live)'))
    o.append(C(fx(td), fy(pa), 5, NX, 'var(--next)'))
    o.append(L(fx(td), fy(pa), fx(td), y1, NX, 1.4, '4 3'))
    o.append(Tb(fx(40) + 10, fy(pa) + 4, 'air: ' + sb('p', 'A') + ' = 1.48 kPa', 13, 'start', LV, True))
    o.append(Tb(fx(td) - 6, fy(pa) - 30, 'dew point', 13, 'middle', NX, True))
    o.append(Tb(fx(td) - 6, fy(pa) - 14, '12.7 °C', 13, 'middle', NX, True))
    o.append(T(fx(26), fy(pa) + 18, 'cool at constant Y', 12, 'middle', LV))
    X = 470
    o.append(R(X, 56, 236, 236, PANEL, L2, 8, 1.5))
    rows = [('40 °C, 20 % RH', ''), ('p_A = 0.20 × 7.38', '1.48 kPa'), ('Y = 0.622 p_A/(P − p_A)', '0.00922'), ('dew point', '12.7 °C'),
            ('v_H', '0.90 m³/kg'), ('c_s = 1.005 + 1.88Y', '1.022'), ('H = c_s T + 2500Y', '63.9 kJ/kg')]
    yy = 84
    for a, b in rows:
        a = a.replace('p_A', sb('p', 'A')).replace('v_H', sb('v', 'H')).replace('c_s', sb('c', 's'))
        o.append(T(X + 12, yy, a, 13, 'start', INK, b == ''))
        if b: o.append(T(X + 224, yy, b, 13, 'end', LV if b.startswith('0.009') or b.startswith('63') else INK, True))
        yy += 31
    return 345, ''.join(o)


FIG[1] = (f1, 'The worked example on the vapour-pressure curve of pure water. At 40 °C water could hold 7.38 kPa of vapour; air at 20 % RH holds p_A = 1.48 kPa. Cooling that air at constant humidity meets the curve at 12.7 °C, its dew point. The panel carries the example through to Y = 0.00922 kg/kg dry air and H = 63.9 kJ/kg dry air.',
          'Graph of the vapour pressure of water rising steeply from 0 to 60 degrees Celsius, with 7.38 kPa marked at 40 degrees. The air state at 40 degrees and 1.48 kPa joins horizontally to the curve at 12.7 degrees, the dew point. A side panel lists the example results.')
AFTER[1] = 2


# ---- 7.2 mixing two streams on the chart ----
def f2():
    x0, x1, y0, y1 = 80, 620, 46, 330
    body, fx, fy = chart(x0, x1, y0, y1, 20, 45, 0.030, [0, 0.010, 0.020, 0.030], [20, 25, 30, 35, 40, 45])
    o = [body]
    A, B = (30, 0.010), (40, 0.020)
    M = (33.37, 0.01333)
    o.append(L(fx(A[0]), fy(A[1]), fx(B[0]), fy(B[1]), INK, 1.6, '6 4'))
    for (t, y), nm, col, dx, dy, anc in [(A, 'A: 100 kg/h, 30 °C, Y = 0.010', NX, 10, 22, 'start'), (B, 'B: 50 kg/h, 40 °C, Y = 0.020', LV, -10, -12, 'end'), (M, 'mix: 33.4 °C, Y = 0.0133', AC, 12, 22, 'start')]:
        o.append(C(fx(t), fy(y), 6, col, col.replace(')', ')')))
        o.append(Tb(fx(t) + dx, fy(y) + dy, nm, 13, anc, col, True))
    o.append(Tb(fx(33.0), fy(0.0150) - 22, 'AM : MB = 1 : 2', 13, 'end', INK, True))
    o.append(Tb(fx(33.0), fy(0.0150) - 4, 'h = 67.7 kJ/kg dry air', 13, 'end', INK))
    o.append(T(fx(26.5), fy(Ys(26.5)) - 4, 'saturation (100 %)', 13, 'end', AC, True))
    return 380, ''.join(o)


FIG[2] = (f2, 'The worked example on a 1 atm chart. Stream A (100 kg dry air/h at 30 °C, Y = 0.010) and stream B (50 kg/h at 40 °C, Y = 0.020) mix to Y = 0.0133 and h = 67.7 kJ/kg dry air, which puts the mixture at 33.4 °C on the straight line AB, one-third of the way from A because A is the larger stream. Dashed curves are 20, 40, 60 and 80 % RH.',
          'Psychrometric chart from 20 to 45 degrees with the saturation curve and relative humidity curves. Points A at 30 degrees and B at 40 degrees are joined by a straight line; the mixture point at 33.4 degrees lies one third of the way from A.')
AFTER[2] = 2


# ---- 7.3 the adiabatic saturation line ----
def f3():
    x0, x1, y0, y1 = 80, 520, 46, 330
    body, fx, fy = chart(x0, x1, y0, y1, 10, 45, 0.025, [0, 0.005, 0.010, 0.015, 0.020, 0.025], [10, 15, 20, 25, 30, 35, 40, 45], rhs=(0.2, 0.4))
    o = [body]
    Tas, Yas = 22.0, 0.0167
    o.append(L(fx(40), fy(0.0092), fx(Tas), fy(Yas), LV, 3, None, 'l'))
    o.append(C(fx(40), fy(0.0092), 6, NX, 'var(--next)'))
    o.append(C(fx(Tas), fy(Yas), 6, LV, 'var(--live)'))
    o.append(L(fx(12.7), fy(0.0092), fx(40), fy(0.0092), NX, 1.4, '4 3'))
    o.append(C(fx(12.7), fy(0.0092), 4, NX))
    o.append(Tb(fx(40) + 8, fy(0.0092) + 22, 'air in: 40 °C, Y = 0.0092', 13, 'end', NX, True))
    o.append(Tb(fx(Tas) - 8, fy(Yas) - 12, sb('T', 'as') + ' = ' + sb('T', 'w') + ' = 22 °C, Y = 0.0167', 13, 'end', LV, True))
    o.append(Tb(fx(31), fy(0.0136) - 12, 'slope −c/λ = −0.00042 per K', 13, 'start', LV))
    o.append(Tb(fx(12.7) + 6, fy(0.0092) + 22, 'dew point 12.7 °C', 13, 'start', NX))
    X = 572
    o.append(R(X, 70, 140, 150, PANEL, L2, 8, 1.5))
    for i, (a, b) in enumerate([('dry bulb', '40 °C'), ('wet bulb', '22 °C'), ('dew point', '12.7 °C'), ('pickup', '0.0075'), ('kg per kg dry air', '')]):
        o.append(T(X + 10, 96 + i * 26, a, 13 if b else 12, 'start', INK if b else MUT))
        if b: o.append(T(X + 130, 96 + i * 26, b, 13, 'end', AC, True))
    return 380, ''.join(o)


FIG[3] = (f3, 'The worked example. Air at 40 °C with Y = 0.0092 cools along its adiabatic saturation line, slope −c_s/λ ≈ −0.00042 per K, until it meets the saturation curve at 22 °C with Y = 0.0167. For air–water this end point is also the wet-bulb temperature. The dew point of the same air, 12.7 °C, lies on the horizontal through the start.',
          'Psychrometric chart from 10 to 45 degrees. A straight sloping line runs from the air state at 40 degrees and humidity 0.0092 up to the saturation curve at 22 degrees and 0.0167. A dashed horizontal from the air state meets saturation at the dew point, 12.7 degrees.')
AFTER[3] = 2


# ---- 7.4 the spray chamber, then cooling below the dew point ----
def f4():
    x0, x1, y0, y1 = 80, 600, 46, 330
    body, fx, fy = chart(x0, x1, y0, y1, 10, 40, 0.020, [0, 0.005, 0.010, 0.015, 0.020], [10, 15, 20, 25, 30, 35, 40], rhs=(0.2, 0.4, 0.6))
    o = [body]
    tas, yas = 21.1, 0.0158
    yo = 0.0142; tdp = 19.5
    o.append(L(fx(25), fy(yo), fx(tas), fy(yas), LV, 1.4, '4 3'))
    o.append(L(fx(35), fy(0.010), fx(25), fy(yo), LV, 3, None, 'l'))
    o.append(L(fx(25), fy(yo), fx(tdp), fy(yo), NX, 2.6))
    sat = [(fx(t), fy(Ys(t))) for t in [tdp - i * 0.1 for i in range(46)]]
    o.append(P(sat, NX, 3.6))
    o.append(C(fx(35), fy(0.010), 6, INK, 'var(--ink)'))
    o.append(C(fx(25), fy(yo), 6, LV, 'var(--live)'))
    o.append(C(fx(tas), fy(yas), 4, LV))
    o.append(C(fx(15), fy(0.0106), 6, NX, 'var(--next)'))
    o.append(Tb(fx(35) + 6, fy(0.010) + 30, 'in: 35 °C, Y = 0.010', 13, 'middle', INK, True))
    o.append(Tb(fx(25) + 10, fy(yo) - 12, 'washer out: 25 °C, Y = 0.0142', 13, 'start', LV, True))
    o.append(Tb(fx(tas) - 4, fy(yas) - 10, sb('T', 'as') + ' = 21.1 °C', 13, 'end', LV))
    o.append(Tb(fx(15) + 10, fy(0.0106) + 18, 'cooled to 15 °C: Y = 0.0106', 13, 'start', NX, True))
    o.append(Tb(fx(15) + 10, fy(0.0106) + 36, 'condenses 0.0036 kg/kg', 13, 'start', NX))
    o.append(C(fx(tdp), fy(yo), 4, NX))
    o.append(T(fx(21.6), fy(yo) + 24, 'dew point 19.5 °C', 13, 'middle', NX))
    return 380, ''.join(o)


FIG[4] = (f4, 'The worked example on the chart. In the recirculating spray chamber the air moves up its wet-bulb line from 35 °C, Y = 0.010 to 25 °C, Y = 0.0142, short of its adiabatic saturation point at 21.1 °C; that is 1.27 transfer units. Cooled further, the air runs left at constant Y to its dew point, 19.5 °C, then down the saturation curve to 15 °C, condensing 0.0036 kg of water per kg dry air.',
          'Psychrometric chart from 10 to 40 degrees. An arrow climbs the wet-bulb line from 35 degrees to 25 degrees, short of the saturation point at 21.1 degrees. A second path runs horizontally to the dew point at 19.5 degrees and then down the saturation curve to 15 degrees.')
AFTER[4] = 3


# ---- 7.5 Merkel driving force ----
def f5():
    o = []
    x0, x1, y0, y1 = 80, 470, 46, 320
    fx = lambda t: x0 + (t - 28) / 14 * (x1 - x0)
    fy = lambda h: y1 - (h - 60) / 120 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [28, 30, 32, 34, 36, 38, 40, 42], [60, 80, 100, 120, 140, 160, 180], fx, fy, 'water temperature (°C)', 'enthalpy (kJ/kg dry air)', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    o.append(P([(fx(28 + i * 0.1), fy(hs(28 + i * 0.1))) for i in range(141)], AC, 3))
    hl = lambda t: 72.2 + 4.187 / 0.9 * (t - 30)
    o.append(P([(fx(30), fy(hl(30))), (fx(40), fy(hl(40)))], LV, 3))
    for t, d in [(30, 27.5), (35, 33.6), (40, 47.4)]:
        o.append(L(fx(t), fy(hl(t)), fx(t), fy(hs(t)), NX, 2.2, None))
        o.append(Tb(fx(t) + 6, fy((hl(t) + hs(t)) / 2) + 4, f'{d}', 13, 'start', NX, True))
        o.append(C(fx(t), fy(hs(t)), 4, AC)); o.append(C(fx(t), fy(hl(t)), 4, LV))
    o.append(T(fx(36.6), fy(hs(36.6)) - 10, 'h* (saturated air at the water temperature)', 13, 'end', AC, True))
    o.append(T(fx(41.8), fy(80), 'air operating line', 13, 'end', LV, True))
    o.append(T(fx(41.8), fy(80) + 18, 'h = 72.2 + 4.65(T − 30)', 13, 'end', LV))
    o.append(T(fx(30) + 6, fy(hl(30)) + 20, 'cold end', 12, 'start', MUT))
    X = 492
    o.append(R(X, 56, 214, 230, PANEL, L2, 8, 1.5))
    rows = [('L = 1.0 kg/s, G = 0.9 kg/s', ''), ('range 10 K, approach 6 K', ''), ('Q = 41.9 kW', ''), ('h1 = 72.2, h2 = 118.7', ''),
            ('Simpson, 3 points:', ''), ('4.187 × (10/6) × 0.1765', ''), ('KaV/L = 1.23', 'b'), ('E = 0.0135 kg/s (1.35 %)', '')]
    for i, (a, b) in enumerate(rows):
        o.append(T(X + 12, 82 + i * 27, a.replace('h1', sb('h', '1')).replace('h2', sb('h', '2')), 13, 'start', AC if b else INK, bool(b)))
    return 365, ''.join(o)


FIG[5] = (f5, 'The worked example on an enthalpy–temperature plot. The curve is h*, the enthalpy of air saturated at the water temperature; the straight line is the air, rising from 72.2 to 118.7 kJ/kg dry air with slope L c_p/G = 4.65. The vertical gaps h* − h at 30, 35 and 40 °C, 27.5, 33.6 and 47.4 kJ/kg, are the Merkel driving forces; Simpson\'s rule on their inverses gives KaV/L = 1.23.',
          'Plot of enthalpy against water temperature from 28 to 42 degrees. A rising curve for saturated air lies above a straight air operating line. Vertical bars at 30, 35 and 40 degrees mark driving forces of 27.5, 33.6 and 47.4. A side panel lists the tower data and the result 1.23.')
AFTER[5] = 2


# ---- 7.6 equilibrium isotherm ----
def f6():
    o = []
    x0, x1, y0, y1 = 80, 500, 46, 320
    fx = lambda rh: x0 + rh / 100 * (x1 - x0)
    fy = lambda X: y1 - X / 0.5 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 20, 40, 60, 80, 100], [0, 0.1, 0.2, 0.3, 0.4, 0.5], fx, fy, 'relative humidity of the air (%)', 'moisture X (kg water/kg dry solid)', lambda v: f'{v:g}', lambda v: f'{v:.1f}'))
    K, Cg = 0.85, 10
    g = lambda p: Cg * K * p / ((1 - K * p) * (1 - K * p + Cg * K * p))
    Xm = 0.10 / g(0.4)
    ads = lambda rh: Xm * g(rh / 100)
    des = lambda rh: ads(rh) * (1 + 0.35 * math.sin(math.pi * rh / 100) ** 1.5)
    rr = [i * 0.5 for i in range(0, 193)]
    o.append(P([(fx(r), fy(des(r))) for r in rr if des(r) <= 0.5], LV, 2.2, '6 4'))
    o.append(P([(fx(r), fy(ads(r))) for r in rr if ads(r) <= 0.5], AC, 3))
    o.append(T(fx(76), fy(des(76)) - 12, 'desorption (drying)', 13, 'end', LV, True))
    o.append(T(fx(70), fy(ads(70)) + 22, 'adsorption (wetting)', 13, 'start', AC, True))
    o.append(L(fx(40), fy(0.429), fx(40), fy(0.10) - 7, NX, 2.4, None, 'x'))
    o.append(C(fx(40), fy(0.429), 6, NX, 'var(--next)'))
    o.append(C(fx(40), fy(0.10), 6, AC, 'var(--accent)'))
    o.append(Tb(fx(40) + 10, fy(0.429) + 4, 'start: X = 30/70 = 0.429', 13, 'start', NX, True))
    o.append(Tb(fx(40) - 10, fy(0.26), 'free moisture 0.329', 13, 'end', NX, True))
    o.append(Tb(fx(40) - 10, fy(0.26) + 18, '= 23.0 kg removable', 13, 'end', NX))
    o.append(Tb(fx(40) - 10, fy(0.10) - 10, 'X* = 0.10 at 40 %', 13, 'end', AC, True))
    o.append(Tb(fx(40) - 10, fy(0.10) + 8, '7.0 kg stays', 13, 'end', AC))
    X = 520
    o.append(R(X, 70, 186, 150, PANEL, L2, 8, 1.5))
    for i, a in enumerate(['100 kg wet solid', '30 % water, wet basis', 'dry solid 70 kg', 'water 30 kg', 'air at 40 % RH']):
        o.append(T(X + 12, 98 + i * 27, a, 13, 'start', INK, i == 0))
    return 365, ''.join(o)


FIG[6] = (f6, 'The worked example on the moisture isotherm of the solid. The sample starts at X = 0.429 kg/kg dry solid. Air at 40 % RH can take it down only to the equilibrium value X* = 0.10 on the drying (desorption) curve, so 0.329 kg/kg, 23.0 kg of water, is free and 7.0 kg stays. The wetting (adsorption) branch lies below the drying branch; the gap is hysteresis.',
          'Plot of solid moisture content against relative humidity. A solid adsorption curve rises slowly then steeply, passing 0.10 at 40 percent; a dashed desorption curve lies above it. An arrow at 40 percent drops from the starting moisture 0.429 to 0.10, labelled free moisture 0.329.')
AFTER[6] = 2


# ---- 7.7 drying rate curve ----
def f7():
    o = []
    x0, x1, y0, y1 = 80, 500, 50, 300
    fx = lambda X: x0 + X / 0.45 * (x1 - x0)
    fy = lambda r: y1 - r / 2.0 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45], [0, 0.5, 1.0, 1.5, 2.0], fx, fy, 'moisture X (kg water/kg dry solid)', 'drying rate R (kg/(m²·h))', lambda v: f'{v:.2f}'.rstrip('0').rstrip('.') if v else '0', lambda v: f'{v:.1f}'))
    o.append(R(fx(0.10), y0 + 2, fx(0.40) - fx(0.10), y1 - y0 - 2, ACS, ACS, 0, 0))
    o.append(P([(fx(0.05), fy(0)), (fx(0.20), fy(1.5)), (fx(0.40), fy(1.5))], AC, 3.2))
    o.append(L(fx(0.10), fy(0.5), fx(0.10), y1, NX, 1.6, '4 3'))
    o.append(L(fx(0.20), fy(1.5), fx(0.20), y1, L2, 1.4, '4 3'))
    o.append(C(fx(0.20), fy(1.5), 6, AC, 'var(--accent)'))
    o.append(C(fx(0.05), fy(0), 5, LV, 'var(--live)'))
    o.append(C(fx(0.10), fy(0.5), 5, NX, 'var(--next)'))
    o.append(Tb(fx(0.30), fy(1.5) - 12, 'constant rate 1.5', 13, 'middle', AC, True))
    o.append(Tb(fx(0.30), fy(1.0), sb('t', 'c') + ' = (50/1.5)(0.40 − 0.20)', 13, 'middle', INK))
    o.append(Tb(fx(0.30), fy(1.0) + 18, '= 6.67 h', 13, 'middle', INK, True))
    o.append(Tb(fx(0.20) + 6, fy(1.5) + 22, sb('X', 'c') + ' = 0.20', 13, 'start', AC, True))
    o.append(Tb(fx(0.05) + 6, fy(0) - 10, 'X* = 0.05', 13, 'start', LV, True))
    o.append(Tb(fx(0.10) - 6, fy(0.5) - 12, sb('X', '2') + ' = 0.10', 13, 'end', NX, True))
    o.append(Tb(fx(0.30), fy(0.40), 'falling: ' + sb('t', 'f') + ' = 5.0 ln 3 = 5.49 h', 13, 'middle', INK, True))
    X = 520
    o.append(R(X, 64, 186, 176, PANEL, L2, 8, 1.5))
    for i, (a, b) in enumerate([('m_s = 50 kg, A = 1 m²', False), ('X: 0.40 → 0.10', False), ('constant rate', False), ('  6.67 h', True), ('falling rate', False), ('  5.49 h', True), ('total 12.2 h', True)]):
        o.append(T(X + 12, 88 + i * 23, a.replace('m_s', sb('m', 's')), 13, 'start', AC if b else INK, b))
    return 350, ''.join(o)


FIG[7] = (f7, 'The rate curve of the first worked example. The rate is flat at R_c = 1.5 kg/(m²·h) down to the critical moisture X_c = 0.20, then falls in a straight line to zero at X* = 0.05. The shaded band is the drying asked for, from X = 0.40 to 0.10: 6.67 h at constant rate and 5.49 h on the falling line, 12.2 h in all.',
          'Drying rate against moisture content: a flat line at 1.5 from 0.40 down to 0.20, then a straight line falling to zero at 0.05. The final moisture 0.10 is marked on the falling line, and the times 6.67 hours and 5.49 hours are written on the two parts.')
AFTER[7] = 2


# ---- 7.8 the air path through a through-circulation bed ----
def f8():
    x0, x1, y0, y1 = 80, 470, 46, 320
    body, fx, fy = chart(x0, x1, y0, y1, 20, 65, 0.030, [0, 0.010, 0.020, 0.030], [20, 30, 40, 50, 60], rhs=(0.2, 0.4), rhlab=False)
    o = [body]
    o.append(L(fx(31.5), fy(0.022), fx(27.6), fy(0.0236), LV, 1.4, '4 3'))
    o.append(L(fx(60), fy(0.010), fx(31.5), fy(0.022), LV, 3, None, 'l'))
    o.append(C(fx(60), fy(0.010), 6, NX, 'var(--next)'))
    o.append(C(fx(31.5), fy(0.022), 6, LV, 'var(--live)'))
    o.append(C(fx(27.6), fy(0.0236), 4, LV))
    o.append(Tb(fx(60), fy(0.010) + 22, 'in: 60 °C, Y = 0.010', 13, 'end', NX, True))
    o.append(Tb(fx(31.5) + 10, fy(0.022) - 12, 'out: 31.5 °C, Y = 0.022', 13, 'start', LV, True))
    o.append(Tb(fx(28.6), fy(0.0275), 'limit ' + sb('T', 'as') + ' = 27.6 °C', 13, 'end', LV))
    # the bed
    bx, bw, by, bh = 520, 130, 90, 170
    o.append(R(bx, by, bw, bh, ACS, AC, 4, 1.8))
    import random
    rnd = random.Random(7)
    for i in range(60):
        o.append(C(bx + 10 + rnd.random() * (bw - 20), by + 10 + rnd.random() * (bh - 20), 5, AC))
    o.append(L(bx - 10, by + bh + 4, bx + bw + 10, by + bh + 4, INK, 2))
    for xx in (bx + 30, bx + 65, bx + 100):
        o.append(L(xx, by + bh + 44, xx, by + bh + 10, NX, 2.2, None, 'x'))
        o.append(L(xx, by - 6, xx, by - 40, LV, 2.2, None, 'l'))
    o.append(T(bx + bw / 2, by + bh + 62, '500 kg dry air/h, 60 °C', 13, 'middle', NX, True))
    o.append(T(bx + bw / 2, by - 48, '31.5 °C, 75 % RH', 13, 'middle', LV, True))
    o.append(T(bx + bw + 12, by + 20, 'wet', 13, 'start', MUT))
    o.append(T(bx + bw + 12, by + bh - 12, 'driest', 13, 'start', MUT))
    o.append(Tb(bx + bw / 2, by + bh / 2 + 4, '100 kg dry solid', 13, 'middle', INK, True))
    return 370, ''.join(o)


FIG[8] = (f8, 'The worked example. Air enters the bed at 60 °C with Y = 0.010 and, while the solid is wet, cools along its adiabatic line as it climbs. Picking up 0.012 kg/kg it leaves at 31.5 °C and about 75 % RH, short of its limit, the adiabatic saturation point 27.6 °C with Y = 0.0236; that gap is ln 8.3 = 2.1 heat-transfer units of bed. 20 kg of water at 6 kg/h takes 3.3 h.',
          'Left: psychrometric chart with an arrow from the inlet air at 60 degrees and humidity 0.010 up the adiabatic line to the outlet at 31.5 degrees and 0.022, short of the saturation point at 27.6 degrees. Right: a bed of particles on a perforated floor with air arrows entering below at 60 degrees and leaving above at 31.5 degrees.')
AFTER[8] = 2


# ---- 7.9 the rotary dryer balance ----
def f9():
    o = []
    import math as m
    cx0, cy0, cx1, cy1, r = 150, 130, 560, 170, 40
    ang = m.atan2(cy1 - cy0, cx1 - cx0); nx, ny = -m.sin(ang) * r, m.cos(ang) * r
    o.append(P([(cx0 + nx, cy0 + ny), (cx1 + nx, cy1 + ny), (cx1 - nx, cy1 - ny), (cx0 - nx, cy0 - ny), (cx0 + nx, cy0 + ny)], AC, 2.4, None, 'var(--accent-soft)'))
    for t in [0.12, 0.28, 0.44, 0.60, 0.76, 0.92]:
        xx, yy = cx0 + (cx1 - cx0) * t, cy0 + (cy1 - cy0) * t
        o.append(L(xx - nx * 0.9, yy - ny * 0.9, xx + nx * 0.9, yy + ny * 0.9, L2, 1.2, '3 3'))
    for t in [0.2, 0.36, 0.52, 0.68, 0.84]:
        xx, yy = cx0 + (cx1 - cx0) * t, cy0 + (cy1 - cy0) * t
        for k in range(4):
            o.append(C(xx - 14 + k * 9, yy - 20 + k * 11, 2.6, NX))
    # feed chute
    o.append(L(cx0 + 30, 34, cx0 + 30, cy0 - 44, NX, 2.6, None, 'x'))
    o.append(T(cx0 + 42, 42, 'wet feed 1000 kg/h, 25 % water (S = 750 kg/h)', 13, 'start', NX, True))
    o.append(T((cx0 + cx1) / 2 + 30, 82, 'D = 1.3 m,  L = 6D = 7.8 m', 14, 'middle', AC, True))
    # product
    o.append(L(cx1 - 6, cy1 + 42, cx1 + 40, cy1 + 92, NX, 2.6, None, 'x'))
    o.append(T(cx1 + 60, cy1 + 112, 'product 765.3 kg/h, 2 % water', 13, 'end', NX, True))
    # air
    o.append(L(704, cy1, cx1 + 10, cy1, LV, 2.6, None, 'l'))
    o.append(T(706, cy1 - 34, 'air in', 13, 'end', LV, True))
    o.append(T(706, cy1 - 16, 'Y = 0.010', 13, 'end', LV))
    o.append(L(cx0 - 8, cy0, 26, cy0, LV, 2.6, None, 'l'))
    o.append(T(20, cy0 + 30, 'air out, Y = 0.035', 13, 'start', LV, True))
    o.append(T(20, cy0 + 48, '9388 kg dry air/h', 13, 'start', LV))
    # drive and flights note
    o.append(R(250, 214, 34, 20, PANEL, L2, 3, 1.5))
    o.append(L(267, 214, 267, 180, L2, 1.5))
    o.append(T(267, 252, 'drive 1–8 rpm', 12, 'middle', MUT))
    o.append(T(420, 236, 'flights lift the solid and shower it', 12, 'middle', MUT))
    o.append(T(420, 252, 'through the gas', 12, 'middle', MUT))
    yb = 320
    o.append(R(20, yb, 686, 92, PANEL, L2, 8, 1.5))
    rows = [('water: 250 − 15.3 = 234.7 kg/h evaporated', 'air: 234.7/0.025 = 9388 kg/h = 2.61 kg/s'),
            ('area: 2.61/2.0 = 1.30 m²  →  D = 1.29 m, use 1.3 m', 'heat: 6.07×10⁵ kJ/h useful; 47 % efficiency')]
    for i, (a, b) in enumerate(rows):
        o.append(T(36, yb + 32 + i * 30, a, 13, 'start', INK))
        o.append(T(380, yb + 32 + i * 30, b, 13, 'start', INK))
    return 425, ''.join(o)


FIG[9] = (f9, 'The worked examples on one sketch. 1000 kg/h of feed at 25 % water leaves as 765.3 kg/h at 2 %, so 234.7 kg/h evaporates. Air rising from Y = 0.010 to 0.035 carries it, which needs 9388 kg dry air/h; at 2.0 kg/(m²·s) the shell is 1.3 m across and, at L/D = 6, 7.8 m long. With the air heated from 25 to 150 °C the drying efficiency is 47 %.',
          'Sketch of an inclined rotary dryer shell with internal flights showering solid. Wet feed enters at the high end, product leaves at the low end, and air flows the opposite way. Labels give the feed, product and air rates, and a panel below lists the water, air, diameter and heat results.')
AFTER[9] = 2


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': capsub(cap), 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
