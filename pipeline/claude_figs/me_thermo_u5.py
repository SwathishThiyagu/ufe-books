"""Claude's hand-drawn figures for me-thermo-u5 (Engineering Thermodynamics: pure substances and gas mixtures), one per chapter, drawn from each
chapter's own worked example and numbers. Property curves are steam-table and reference-data values computed once and stored in DATA (Lee–Kesler
simple-fluid values for the compressibility chart). Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """v_f, h_fg, p_R ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔ])_([A-Za-z0-9₂]+)', r'\1<tspan baseline-shift="sub" font-size="12">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)

FIG = {}
DATA = {"dome": [[0.01, 0.0010002, 205.99], [20, 0.0010018, 57.757], [40, 0.0010079, 19.515], [60, 0.0010171, 7.6672], [80, 0.0010291, 3.4052], [100, 0.0010435, 1.6718], [130, 0.0010697, 0.668], [160, 0.001102, 0.30678], [200, 0.0011565, 0.12721], [240, 0.0012295, 0.059705], [280, 0.0013328, 0.030153], [310, 0.0014479, 0.018335], [340, 0.0016376, 0.010781], [360, 0.0018954, 0.0069493], [370, 0.0022152, 0.0049544], [373, 0.0025083, 0.004045]], "sh1": [[100, 1.6733], [150, 1.9111], [200, 2.1439], [250, 2.3746], [300, 2.6043]], "sg": [[8.2555, 2573.5], [7.9081, 2608.8], [7.6111, 2643.0], [7.3541, 2675.6], [7.1291, 2705.9], [6.8371, 2745.9], [6.584, 2777.2], [6.3563, 2797.3], [6.1423, 2803.0], [5.9304, 2789.7], [5.7059, 2749.6], [5.4422, 2666.0]], "p10": [[5.4733, 2273.5], [6.585, 2777.1], [6.6148, 2790.7], [6.6955, 2828.3], [6.9265, 2943.1], [7.1246, 3051.6], [7.3029, 3158.2], [7.4669, 3264.5]], "p1": [[6.1476, 2223.5], [7.3588, 2674.9], [7.4155, 2696.3], [7.6148, 2776.6], [7.8356, 2875.5], [8.0346, 2974.5], [8.2172, 3074.5]], "t250": [[6.1764, 2829.7], [6.5475, 2903.2], [6.9265, 2943.1], [7.2724, 2961.0], [7.71, 2971.2], [8.0346, 2974.5], [8.3568, 2976.1]], "x09": [[7.2005, 2373.1], [6.9575, 2412.2], [6.7494, 2449.9], [6.4873, 2502.7], [6.2685, 2549.2], [6.0202, 2598.0], [5.7983, 2626.4]], "Z": {"1.1": [[0.05, 0.9874], [0.25, 0.935], [0.5, 0.8634], [0.75, 0.7825], [1.0, 0.688], [1.25, 0.574], [1.5, 0.458], [1.75, 0.4026], [2.0, 0.3953], [2.25, 0.4076], [2.5, 0.4277], [2.75, 0.4515], [3.0, 0.477], [3.25, 0.5034], [3.5, 0.5304], [3.75, 0.5577], [4.0, 0.5851], [4.25, 0.6126], [4.5, 0.6401], [4.75, 0.6676], [5.0, 0.695], [5.25, 0.7223], [5.5, 0.7496], [5.75, 0.7767], [6.0, 0.8038]], "1.3": [[0.05, 0.9926], [0.25, 0.9626], [0.5, 0.924], [0.75, 0.8844], [1.0, 0.8438], [1.25, 0.8029], [1.5, 0.7624], [1.75, 0.7243], [2.0, 0.6908], [2.25, 0.6646], [2.5, 0.6467], [2.75, 0.6371], [3.0, 0.6344], [3.25, 0.6374], [3.5, 0.6446], [3.75, 0.6551], [4.0, 0.6681], [4.25, 0.6831], [4.5, 0.6996], [4.75, 0.7172], [5.0, 0.7358], [5.25, 0.755], [5.5, 0.7748], [5.75, 0.795], [6.0, 0.8156]], "1.6": [[0.05, 0.9964], [0.25, 0.982], [0.5, 0.9644], [0.75, 0.9473], [1.0, 0.9308], [1.25, 0.9149], [1.5, 0.9], [1.75, 0.8863], [2.0, 0.8738], [2.25, 0.8629], [2.5, 0.8537], [2.75, 0.8464], [3.0, 0.841], [3.25, 0.8376], [3.5, 0.8361], [3.75, 0.8365], [4.0, 0.8386], [4.25, 0.8424], [4.5, 0.8475], [4.75, 0.854], [5.0, 0.8617], [5.25, 0.8704], [5.5, 0.88], [5.75, 0.8904], [6.0, 0.9015]], "2.0": [[0.05, 0.9986], [0.25, 0.9931], [0.5, 0.9866], [0.75, 0.9807], [1.0, 0.9754], [1.25, 0.9706], [1.5, 0.9664], [1.75, 0.9628], [2.0, 0.9599], [2.25, 0.9576], [2.5, 0.9561], [2.75, 0.9552], [3.0, 0.955], [3.25, 0.9555], [3.5, 0.9567], [3.75, 0.9585], [4.0, 0.9611], [4.25, 0.9642], [4.5, 0.9679], [4.75, 0.9723], [5.0, 0.9772], [5.25, 0.9826], [5.5, 0.9885], [5.75, 0.9949], [6.0, 1.002]], "2.5": [[0.05, 0.9997], [0.25, 0.9987], [0.5, 0.9977], [0.75, 0.9972], [1.0, 0.9969], [1.25, 0.9971], [1.5, 0.9976], [1.75, 0.9984], [2.0, 0.9996], [2.25, 1.001], [2.5, 1.003], [2.75, 1.005], [3.0, 1.008], [3.25, 1.011], [3.5, 1.014], [3.75, 1.018], [4.0, 1.021], [4.25, 1.026], [4.5, 1.03], [4.75, 1.035], [5.0, 1.039], [5.25, 1.045], [5.5, 1.05], [5.75, 1.056], [6.0, 1.061]]}, "ws": [[10, 0.007632], [12, 0.008733], [14, 0.009973], [16, 0.01137], [18, 0.01294], [20, 0.0147], [22, 0.01667], [24, 0.01889], [26, 0.02136], [28, 0.02412], [30, 0.02721], [32, 0.03066], [34, 0.0345], [36, 0.03879], [38, 0.04357], [40, 0.0489]], "w60": [[10, 0.004557], [12, 0.00521], [14, 0.005946], [16, 0.006772], [18, 0.007699], [20, 0.008737], [22, 0.009898], [24, 0.0112], [26, 0.01264], [28, 0.01425], [30, 0.01605], [32, 0.01804], [34, 0.02025], [36, 0.02271], [38, 0.02543], [40, 0.02844]], "co2": [[0.0002, 14.55, 9.396, 9.755], [0.00022, 13.23, 8.889, 9.166], [0.00025, 11.64, 8.211, 8.403], [0.00028, 10.39, 7.618, 7.755], [0.0003, 9.7, 7.264, 7.374], [0.00035, 8.314, 6.497, 6.564], [0.0004, 7.275, 5.868, 5.911], [0.0005, 5.82, 4.907, 4.925], [0.0006, 4.85, 4.21, 4.219], [0.0007, 4.157, 3.684, 3.688], [0.0008, 3.637, 3.274, 3.275], [0.001, 2.91, 2.676, 2.676], [0.0012, 2.425, 2.262, 2.261]]}


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def sub_(s):
    """x_f style subscripts for svg text"""
    return s


# ---- 5.1 T-v diagram of water at 101.325 kPa (log v) ----
def f1():
    o = []
    x0, x1, y0, y1 = 90, 690, 40, 380
    fx = lambda v: x0 + (math.log10(v) + 3.3) / 3.8 * (x1 - x0)
    fy = lin(0, 400, y1, y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v, s in ((0.001, '0.001'), (0.01, '0.01'), (0.1, '0.1'), (1, '1')):
        X = fx(v); o += [L(X, y1, X, y1 + 5, L2, 1.5), T(X, y1 + 20, s, 13, fill=MUT)]
    for t in (0, 100, 200, 300, 400):
        Y = fy(t); o += [L(x0 - 5, Y, x0, Y, L2, 1.5), T(x0 - 9, Y + 4.5, str(t), 13, 'end', MUT)]
    o.append(T((x0 + x1) / 2, y1 + 40, 'v (m³/kg, log scale)', 14, fill=MUT))
    o.append(T(x0, y0 - 14, 'T (°C)', 14, 'start', MUT))
    dome = DATA['dome']
    left = [(fx(vf), fy(t)) for t, vf, vg in dome]
    right = [(fx(vg), fy(t)) for t, vf, vg in dome]
    crit = (fx(0.003106), fy(373.95))
    o.append(P(left + [crit] + right[::-1], MUT, 2))
    o.append(C(*crit, 5, MUT))
    o.append(T(crit[0] + 10, crit[1] - 6, 'critical point, 374 °C', 13, 'start', MUT))
    # the 101.325 kPa path
    pts = [(fx(0.001002), fy(20)), (fx(0.001043), fy(100)), (fx(1.673), fy(100))] + [(fx(v), fy(t)) for t, v in DATA['sh1'][1:]]
    o.append(P(pts, AC, 3))
    o.append(C(fx(0.001002), fy(20), 6, AC)); o.append(T(fx(0.001002) + 12, fy(20) + 5, '1: compressed liquid, 20 °C', 13, 'start'))
    o.append(C(fx(0.001043), fy(100), 6, AC)); o.append(T(fx(0.001043) - 4, fy(100) - 14, '2: saturated liquid', 13, 'start'))
    o.append(T(fx(0.001043) + 10, fy(100) + 22, 'v_f = 0.001043', 13, 'start', MUT))
    o.append(C(fx(0.419), fy(100), 7, NX)); o.append(Tb(fx(0.419), fy(100) - 14, '3: wet, x = 0.25, v = 0.419', 13, 'middle', NX, bold=True))
    o.append(C(fx(1.673), fy(100), 6, AC)); o.append(T(fx(1.673) - 10, fy(100) + 24, '4: v_g = 1.673', 13, 'end', MUT))
    o.append(C(fx(2.144), fy(200), 6, LV)); o.append(T(fx(2.144) - 12, fy(200) + 5, '5: superheated, 200 °C', 13, 'end', LV))
    o.append(T(fx(0.06), fy(30), 'wet region under the dome', 13, 'middle', MUT))
    o.append(T(fx(0.06), fy(100) + 26, 'boiling at 100 °C, p = 101.325 kPa', 13, 'middle', AC, bold=True))
    return 440, ''.join(o)


FIG[1] = (f1, 'Water at 101.325 kPa heated from 20 °C: the compressed liquid (1) reaches saturated liquid (2), boils at 100 °C across the dome, where the '
              'worked example’s mixture with x = 0.25 sits at v = 0.419 m³/kg (3), reaches saturated vapour (4) and then superheats (5).',
          'T-v diagram of water with specific volume on a log scale. The saturation dome peaks at the critical point, 374 degrees Celsius. A constant pressure '
          'line at 101.325 kilopascals rises through compressed liquid, runs flat at 100 degrees from 0.001043 to 1.673 cubic metres per kilogram, '
          'and rises again in superheated vapour.')


# ---- 5.2 p-T phase diagram of water (not to scale) with the example's paths ----
def f2():
    o = []
    x0, x1, y0, y1 = 70, 690, 40, 400
    o.append(L(x0, y1, x1, y1, L2, 1.5, arrow='m')); o.append(L(x0, y1, x0, y0, L2, 1.5, arrow='m'))
    o.append(T(x1, y1 + 22, 'T', 14, 'end', MUT)); o.append(T(x0 + 8, y0 + 4, 'p', 14, 'start', MUT))
    o.append(T(x1, y0 + 4, 'not to scale', 13, 'end', MUT))
    tp = (250, 300); cp = (560, 110)
    # sublimation, vaporisation, melting curves
    o.append(f'<path d="M90,392 Q190,370 {tp[0]},{tp[1]}" style="fill:none;stroke:{AC};stroke-width:2.5"/>')
    o.append(f'<path d="M{tp[0]},{tp[1]} Q430,250 {cp[0]},{cp[1]}" style="fill:none;stroke:{AC};stroke-width:2.5"/>')
    o.append(L(tp[0], tp[1], 236, 52, AC, 2.5))
    o.append(C(*tp, 6, NX)); o.append(C(*cp, 6, NX))
    o.append(Tb(tp[0] + 12, tp[1] + 22, 'triple point 0.01 °C, 0.6117 kPa', 13, 'start', NX, bold=True))
    o.append(Tb(cp[0] - 12, cp[1] + 4, 'critical point 373.95 °C, 22.064 MPa', 13, 'end', NX, bold=True))
    o.append(T(140, 120, 'solid', 15, bold=True)); o.append(T(380, 172, 'liquid', 15, bold=True)); o.append(T(560, 330, 'vapour', 15, bold=True))
    o.append(T(645, 70, 'supercritical', 13, 'middle', MUT))
    o.append(L(cp[0], cp[1], 690, cp[1], MUT, 1.5, dash='5 4')); o.append(L(cp[0], cp[1], cp[0], 52, MUT, 1.5, dash='5 4'))
    # paths
    ya, yb = 340, 205
    o.append(L(110, yb, 470, yb, LV, 2.5, arrow='l')); o.append(T(110, yb - 9, '(b) 101.325 kPa: −20 °C → 20 °C', 13, 'start', LV, bold=True))
    o.append(C(243, yb, 5, LV)); o.append(T(232, yb + 22, 'melts 0 °C', 13, 'end', LV))
    o.append(C(368, yb, 4, MUT)); o.append(T(372, yb + 22, 'boils at 100 °C', 13, 'start', MUT))
    o.append(L(110, ya, 470, ya, LV, 2.5, arrow='l')); o.append(T(470, ya + 22, '(a) 0.4 kPa: −20 °C → 20 °C', 13, 'end', LV, bold=True))
    o.append(C(208, ya, 5, LV)); o.append(T(196, ya - 9, 'sublimes −5 °C', 13, 'end', LV))
    o.append(L(500, 80, 680, 80, AC, 2.5, arrow='n')); o.append(T(495, 85, '(c) 25 MPa', 13, 'end', AC, bold=True))
    return 430, ''.join(o)


FIG[2] = (f2, 'The p-T diagram of water, not to scale: the sublimation, melting and boiling curves meet at the triple point, and the boiling curve ends at the '
              'critical point. Path (a) at 0.4 kPa crosses only the sublimation curve; path (b) at 101.325 kPa melts and stays liquid; path (c) above 22.064 MPa never boils.',
          'Phase diagram of water: solid region on the left, liquid at the top middle, vapour at the bottom right. Three heating paths from the worked example: '
          '0.4 kilopascals subliming at minus 5 degrees, 101.325 kilopascals melting at 0 degrees, and 25 megapascals passing above the critical point.')


# ---- 5.3 phase rule: one, two and three phases of water ----
def f3():
    o = []
    cols = [(130, 'P = 1', 'F = 2'), (360, 'P = 2', 'F = 1'), (590, 'P = 3', 'F = 0')]
    top, bot, w = 70, 250, 150
    for cx, pl, fl in cols:
        x = cx - w / 2
        o.append(T(cx, 40, pl + ',  ' + fl, 16, bold=True, fill=AC if fl != 'F = 0' else NX))
        o.append(R(x, top, w, bot - top, PANEL, L2, 6))
    # 1: vapour only
    x = 130 - w / 2
    o.append(R(x + 4, top + 4, w - 8, 14, ACS, AC, 3)); o.append(T(130, top + 44, 'piston', 13, fill=MUT))
    o.append(T(130, 170, 'superheated', 14)); o.append(T(130, 188, 'vapour', 14))
    # 2: vapour over liquid
    x = 360 - w / 2
    o.append(R(x + 4, top + 4, w - 8, 14, ACS, AC, 3))
    o.append(T(360, 140, 'vapour', 14)); o.append(R(x + 2, 190, w - 4, bot - 192, LVS, LV, 3)); o.append(T(360, 225, 'liquid', 14))
    # 3: sealed cell with ice floating
    x = 590 - w / 2
    o.append(T(590, 130, 'vapour', 14)); o.append(R(x + 2, 175, w - 4, bot - 177, LVS, LV, 3)); o.append(R(x + 25, 168, 60, 26, NXS, NX, 3))
    o.append(T(x + 55, 186, 'ice', 13, bold=True)); o.append(T(620, 228, 'liquid', 14))
    o.append(T(590, top + 22, 'sealed cell', 13, fill=MUT))
    lines = [(130, ['choose p and T', 'e.g. 10 bar, 250 °C']), (360, ['choose p only:', '10 bar → T = 179.9 °C']), (590, ['nothing to choose:', '0.01 °C, 0.6117 kPa'])]
    for cx, ls in lines:
        o.append(T(cx, 280, ls[0], 14, bold=True)); o.append(T(cx, 300, ls[1], 13, fill=MUT))
    o.append(T(360, 340, 'pure water, C = 1:  F = C − P + 2 = 3 − P', 15, bold=True))
    return 360, ''.join(o)


FIG[3] = (f3, 'Water as one, two and three phases. Each extra phase adds an equilibrium condition and removes one free choice: superheated vapour has F = 2, '
              'boiling water F = 1, and the triple-point cell F = 0.',
          'Three containers of water. Left: vapour only, P equals 1, F equals 2. Middle: vapour over liquid, P equals 2, F equals 1, so 10 bar fixes 179.9 degrees. '
          'Right: ice, liquid and vapour in a sealed cell, P equals 3, F equals 0, fixed at 0.01 degrees and 0.6117 kilopascals.')


# ---- 5.4 T-h at 1 atm and at 10 bar ----
def f4():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 370
    fx = lin(0, 3200, x0, x1); fy = lin(0, 280, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 800, 1600, 2400, 3200], [0, 70, 140, 210, 280], fx, fy, 'h (kJ/kg)', 'T (°C)'))
    a = [(84, 20), (419, 100), (2676, 100), (2776, 150)]
    b = [(105, 25), (763, 179.9), (2778, 179.9), (2943, 250)]
    o.append(P([(fx(h), fy(t)) for h, t in a], AC, 3)); o.append(P([(fx(h), fy(t)) for h, t in b], LV, 3))
    for h, t in a: o.append(C(fx(h), fy(t), 4.5, AC))
    for h, t in b: o.append(C(fx(h), fy(t), 4.5, LV))
    o.append(T(fx(2776) + 8, fy(150) + 5, '1 atm', 14, 'start', AC, bold=True))
    o.append(T(fx(2943) + 8, fy(250) + 5, '10 bar', 14, 'start', LV, bold=True))
    o.append(T(fx(1547), fy(100) + 20, 'h_fg = 2257 kJ/kg at 100 °C', 13, 'middle', AC))
    o.append(T(fx(1770), fy(179.9) - 10, 'h_fg = 2015 kJ/kg at 179.9 °C', 13, 'middle', LV))
    o.append(C(fx(2450.3), fy(100), 7, NX)); o.append(Tb(fx(2450.3), fy(100) + 44, 'x = 0.9: h = 2450.3', 13, 'middle', NX, bold=True))
    o.append(T(fx(419) + 14, fy(100) + 20, 'h_f = 419', 13, 'start', MUT))
    o.append(T(fx(763) + 16, fy(179.9) - 34, 'h_f = 763', 13, 'start', MUT)); o.append(L(fx(763) + 8, fy(179.9) - 28, fx(763) + 2, fy(179.9) - 6, MUT, 1.2))
    o.append(T(fx(2943) - 6, fy(250) - 14, '250 °C: 2943', 13, 'end', LV))
    return 430, ''.join(o)


FIG[4] = (f4, 'Steam formation at constant pressure on a T-h plot. At 1 atm the flat boiling line is 2257 kJ/kg long; at 10 bar it starts higher, at '
              '179.9 °C, and is shorter, 2015 kJ/kg. The first worked example’s wet steam, x = 0.9 at 1 atm, sits at h = 2450.3 kJ/kg.',
          'Temperature against enthalpy for water heated at 1 atmosphere and at 10 bar. Each line rises through the liquid, runs flat while boiling, and rises '
          'again as superheated steam. The boiling line at 10 bar is shorter and higher than at 1 atmosphere.')


# ---- 5.5 Mollier chart: isentropic expansion 10 bar 250 C -> 1 bar ----
def f5():
    o = []
    x0, x1, y0, y1 = 90, 690, 40, 380
    fx = lin(5.6, 8.4, x0, x1); fy = lin(2200, 3300, y1, y0)
    o.append(axes(x0, x1, y0, y1, [5.6, 6.3, 7.0, 7.7, 8.4], [2200, 2475, 2750, 3025, 3300], fx, fy, 's (kJ/kg·K)', 'h (kJ/kg)', lambda v: f'{v:.1f}'))
    o.append(P([(fx(s), fy(h)) for s, h in DATA['sg'] if 5.6 <= s <= 8.4], MUT, 2.5))
    o.append(T(fx(7.95), fy(2600) + 26, 'x = 1 (saturated vapour)', 13, 'middle', MUT))
    o.append(P([(fx(s), fy(h)) for s, h in DATA['x09'] if 5.6 <= s <= 8.4], MUT, 1.5, dash='6 4'))
    o.append(T(fx(5.95), fy(2600) + 30, 'x = 0.9', 13, 'middle', MUT))
    p10 = [(s, h) for s, h in DATA['p10'] if s >= 5.6]
    o.append(P([(fx(s), fy(h)) for s, h in p10], AC, 2.5)); o.append(T(fx(7.47) + 6, fy(3264) - 4, '10 bar', 14, 'start', AC, bold=True))
    o.append(P([(fx(s), fy(h)) for s, h in DATA['p1'] if 5.6 <= s <= 8.4], AC, 2.5)); o.append(T(fx(8.2) - 4, fy(3074) - 10, '1 bar', 14, 'end', AC, bold=True))
    o.append(P([(fx(s), fy(h)) for s, h in DATA['t250'] if 5.6 <= s <= 8.4], LV, 2, dash='3 3')); o.append(T(fx(8.3), fy(2976) - 8, '250 °C', 13, 'end', LV))
    s1, h1, h2 = 6.9265, 2943.1, 2513.7
    o.append(L(fx(s1), fy(h1) + 7, fx(s1), fy(h2) - 9, NX, 3, arrow='x'))
    o.append(C(fx(s1), fy(h1), 6, NX)); o.append(C(fx(s1), fy(h2), 6, NX))
    o.append(Tb(fx(s1) - 12, fy(h1) - 8, '1: 10 bar, 250 °C, h = 2943.1', 13, 'end', NX, bold=True))
    o.append(Tb(fx(s1) + 12, fy(h2) + 22, '2: 1 bar, x = 0.929, h = 2513.7', 13, 'start', NX, bold=True))
    o.append(Tb(fx(s1) - 12, fy(2650), 's constant: Δh = 429.4 kJ/kg', 13, 'end', NX))
    return 440, ''.join(o)


FIG[5] = (f5, 'Part of the Mollier (h-s) chart of steam, drawn from steam-table values. The second worked example is the vertical line: from 10 bar and 250 °C '
              'down at constant entropy to the 1 bar line inside the dome, where x = 0.929 and h = 2513.7 kJ/kg.',
          'Enthalpy against entropy for steam. The saturated vapour line curves across the middle, the 10 bar and 1 bar lines rise to the right, and a '
          'vertical arrow at s equal to 6.93 drops from 2943.1 to 2513.7 kilojoules per kilogram.')


# ---- 5.6 throttling calorimeter ----
def f6():
    o = []
    o.append(R(40, 50, 640, 40, PANEL, AC, 6)); o.append(T(360, 76, 'main steam pipe: 10 bar, wet (x₁ unknown)', 14, bold=True))
    o.append(R(130, 90, 18, 70, PANEL, AC, 2)); o.append(T(160, 128, 'sampling tube', 13, 'start', MUT))
    # valve
    o.append(f'<path d="M115,160 L163,190 L163,160 L115,190 Z" style="fill:var(--accent-soft);stroke:{AC};stroke-width:2"/>')
    o.append(T(175, 180, 'throttle valve: h₁ = h₂', 14, 'start', AC, bold=True))
    o.append(R(130, 190, 18, 40, PANEL, AC, 2))
    o.append(R(80, 230, 260, 110, PANEL, AC, 8)); o.append(T(210, 262, 'chamber', 14, bold=True))
    o.append(T(210, 290, 'p₂ = 1 bar', 14, fill=LV, bold=True)); o.append(T(210, 314, 'T₂ = 130 °C (superheated)', 14, fill=LV, bold=True))
    o.append(R(260, 205, 10, 40, LVS, LV, 3)); o.append(T(276, 222, 'thermometer', 13, 'start', MUT))
    o.append(L(340, 300, 420, 300, AC, 2.5, arrow='n')); o.append(T(380, 290, 'to drain', 13, fill=MUT))
    o.append(boxt(432, 130, 266, 220, ['from the tables:', 'h₂ = 2736.7 kJ/kg (1 bar)', 'h_f = 762.5, h_fg = 2014.6 (10 bar)', ' ', 'x₁ = (2736.7 − 762.5)/2014.6', '= 0.980'],
                  ACS, AC, 14, bold_first=True))
    return 370, ''.join(o)


FIG[6] = (f6, 'A throttling calorimeter on a 10 bar main. A sample is throttled at constant enthalpy into a chamber at 1 bar; the outlet reads 130 °C, so it is '
              'superheated, and h₂ from the table gives the main steam’s dryness, x₁ = 0.980.',
          'Sketch of a throttling calorimeter: a sampling tube leaves the main steam pipe, passes a throttle valve and enters a chamber with a thermometer at '
          '1 bar and 130 degrees Celsius. A box shows h2 = 2736.7 and x1 = 0.980.')


# ---- 5.7 CO2 at 350 K: ideal, van der Waals and reference data ----
def f7():
    o = []
    x0, x1, y0, y1 = 80, 680, 40, 370
    fx = lin(0.2, 1.2, x0, x1); fy = lin(0, 16, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0.2, 0.4, 0.6, 0.8, 1.0, 1.2], [0, 4, 8, 12, 16], fx, fy, 'v (litre per mol, 10⁻³ m³/mol)', 'p (MPa)', lambda v: f'{v:.1f}'))
    d = DATA['co2']
    o.append(P([(fx(v * 1000), fy(a)) for v, a, b, c in d], MUT, 2.5, dash='7 5'))
    o.append(P([(fx(v * 1000), fy(c)) for v, a, b, c in d], LV, 5, op=None))
    o.append(P([(fx(v * 1000), fy(b)) for v, a, b, c in d], AC, 2.5))
    o.append(T(fx(0.26), fy(14.6), 'ideal gas', 14, 'start', MUT, bold=True))
    o.append(T(fx(0.62), fy(6.0), 'reference data (thick)', 13, 'start', LV, bold=True))
    o.append(T(fx(0.62), fy(7.3), 'van der Waals', 14, 'start', AC, bold=True))
    X = fx(0.3)
    o.append(L(X, fy(0), X, fy(10.4), L2, 1.2, dash='4 4'))
    for p, c in ((9.70, MUT), (7.37, LV), (7.26, AC)):
        o.append(C(X, fy(p), 5.5, c))
    o.append(boxt(fx(0.62), fy(15.4), 240, 96, ['at v = 0.3 L/mol:', 'ideal gas 9.70 MPa', 'reference 7.37 MPa', 'van der Waals 7.26 MPa'],
                  PANEL, L2, 14, bold_first=True, fills=[INK, MUT, LV, AC]))
    o.append(T(X + 8, fy(0.8), 'v = 0.3 L/mol', 13, 'start', MUT))
    return 430, ''.join(o)


FIG[7] = (f7, 'One mole of carbon dioxide at 350 K. At small volume the ideal law overshoots: at v = 0.3 L/mol it gives 9.70 MPa, while van der Waals gives '
              '7.26 MPa, close to the measured 7.37 MPa. At large volume all three curves merge.',
          'Pressure against molar volume for carbon dioxide at 350 kelvin. The dashed ideal gas curve lies well above the van der Waals curve and the '
          'reference data at small volumes; the three meet at large volumes. At 0.3 litre per mole they give 9.70, 7.26 and 7.37 megapascals.')


# ---- 5.8 generalized compressibility chart ----
def f8():
    o = []
    x0, x1, y0, y1 = 80, 600, 40, 370
    fx = lin(0, 6, x0, x1); fy = lin(0.3, 1.1, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3, 4, 5, 6], [0.3, 0.5, 0.7, 0.9, 1.1], fx, fy, _sub('reduced pressure p_R'), 'Z', lambda v: f'{v:.1f}'))
    o.append(L(x0, fy(1.0), x1, fy(1.0), MUT, 1.2, dash='5 4')); o.append(T(x0 + 6, fy(1.0) - 6, 'ideal gas, Z = 1', 13, 'start', MUT))
    cols = {'1.1': NX, '1.3': MUT, '1.6': AC, '2.0': MUT, '2.5': LV}
    for tr, pts in DATA['Z'].items():
        o.append(P([(fx(a), fy(b)) for a, b in pts], cols[tr], 2.2 if tr in ('1.6', '2.5') else 1.8))
        a, b = pts[-1]
        o.append(T(x1 + 6, fy(b) + 5 + {'1.3': -7, '1.1': 9}.get(tr, 0), f'T_R = {tr}', 13, 'start', cols[tr]))
    o.append(C(fx(4.35), fy(0.83), 7, AC)); o.append(Tb(fx(4.35), fy(0.83) + 28, 'CNG: p_R 4.35, T_R 1.57, Z ≈ 0.83', 13, 'middle', AC, bold=True))
    o.append(C(fx(2.95), fy(1.00), 7, LV)); o.append(Tb(fx(2.95), fy(1.00) - 16, 'N₂: Z ≈ 1.00', 13, 'middle', LV, bold=True))
    return 432, ''.join(o)


FIG[8] = (f8, 'A generalized compressibility chart: Z against reduced pressure for five reduced temperatures. The CNG cylinder of the worked example sits at '
              'reduced pressure 4.35 and reduced temperature 1.57, where Z ≈ 0.83; nitrogen at 300 K and 10 MPa sits on Z ≈ 1.',
          'Compressibility factor Z against reduced pressure from 0 to 6, with curves for reduced temperatures 1.1, 1.3, 1.6, 2.0 and 2.5. The low curves dip '
          'well below 1; the 2.5 curve stays near 1. Two points mark methane at Z 0.83 and nitrogen at Z 1.00.')


# ---- 5.9 Dalton and Amagat for the O2 + N2 tank ----
def f9():
    o = []
    o.append(boxt(250, 20, 220, 70, ['mixture: 2 m³, 300 K', '0.025 kmol O₂ + 0.100 kmol N₂', 'p = 155.9 kPa'], ACS, AC, 14, bold_first=True))
    o.append(T(40, 128, 'Dalton: each gas alone in the same V and T', 15, 'start', bold=True))
    o.append(boxt(40, 140, 300, 64, ['O₂ alone in 2 m³', 'p_O₂ = 0.2 × 155.9 = 31.2 kPa'], NXS, NX, 14))
    o.append(boxt(380, 140, 300, 64, ['N₂ alone in 2 m³', 'p_N₂ = 0.8 × 155.9 = 124.7 kPa'], LVS, LV, 14))
    o.append(T(360, 228, '31.2 + 124.7 = 155.9 kPa', 14, 'middle', MUT))
    o.append(T(40, 270, 'Amagat: each gas alone at the same p and T', 15, 'start', bold=True))
    x0, W_ = 40, 640
    o.append(boxt(x0, 282, W_ * 0.2, 64, ['O₂', '0.4 m³'], NXS, NX, 14))
    o.append(boxt(x0 + W_ * 0.2, 282, W_ * 0.8, 64, ['N₂ at 155.9 kPa', 'V_N₂ = 0.8 × 2 = 1.6 m³'], LVS, LV, 14))
    o.append(T(360, 370, '0.4 + 1.6 = 2 m³: the shares are the mole fractions 0.2 and 0.8', 14, 'middle', MUT))
    return 390, ''.join(o)


FIG[9] = (f9, 'The worked example’s tank seen two ways. Dalton keeps V and T and splits the pressure, 31.2 + 124.7 = 155.9 kPa; Amagat keeps p and T and '
              'splits the volume, 0.4 + 1.6 = 2 m³. Both shares are the mole fractions 0.2 and 0.8.',
          'A mixture box of oxygen and nitrogen at 155.9 kilopascals. Below, Dalton: oxygen alone gives 31.2 and nitrogen 124.7 kilopascals. Amagat: oxygen '
          'takes 0.4 and nitrogen 1.6 cubic metres of the 2 cubic metre tank.')


# ---- 5.10 psychrometric chart sketch ----
def f10():
    o = []
    x0, x1, y0, y1 = 90, 680, 40, 370
    fx = lin(10, 35, x0, x1); fy = lin(0, 0.04, y1, y0)
    o.append(axes(x0, x1, y0, y1, [10, 15, 20, 25, 30, 35], [0, 0.01, 0.02, 0.03, 0.04], fx, fy, 'dry-bulb temperature (°C)', 'w (kg/kg dry air)', yfmt=lambda v: f'{v:.2f}'))
    ws = [(t, w) for t, w in DATA['ws'] if t <= 34]
    o.append(P([(fx(t), fy(w)) for t, w in ws], AC, 3)); o.append(T(fx(31.5), fy(0.0345), 'φ = 100% (saturation)', 13, 'end', AC, bold=True))
    w6 = [(t, w) for t, w in DATA['w60'] if t <= 35]
    o.append(P([(fx(t), fy(w)) for t, w in w6], MUT, 2, dash='6 4')); o.append(T(fx(34.6), fy(0.0216) - 8, 'φ = 60%', 13, 'end', MUT))
    A = (fx(30), fy(0.01605)); D_ = (fx(21.4), fy(0.01605))
    o.append(L(A[0] - 8, A[1], D_[0] + 8, D_[1], NX, 2.5, arrow='x'))
    o.append(C(*A, 7, NX)); o.append(C(*D_, 6, LV))
    o.append(Tb(A[0] + 4, A[1] + 26, 'A: 30 °C, φ = 60%, w = 0.0160', 13, 'middle', NX, bold=True))
    o.append(Tb(D_[0] - 10, D_[1] - 12, 'dew point 21.4 °C', 13, 'end', LV, bold=True))
    o.append(T(fx(25.7), fy(0.01605) - 10, 'cool at constant w', 13, 'middle', NX))
    o.append(L(fx(30), fy(0.01605) + 8, fx(30), fy(0), L2, 1.2, dash='4 4'))
    return 430, ''.join(o)


FIG[10] = (f10, 'A psychrometric chart sketch at 101.325 kPa, drawn from saturation pressures. State A is the worked example’s air, 30 °C and 60 per cent; '
                'cooling it at constant w moves left until it meets the saturation curve at the dew point, 21.4 °C.',
           'Humidity ratio against dry-bulb temperature from 10 to 35 degrees Celsius. A rising saturation curve and a lower 60 percent curve. State A at '
           '30 degrees and w 0.0160 moves left along a horizontal line to the dew point at 21.4 degrees.')

spec = make_spec(FIG)
