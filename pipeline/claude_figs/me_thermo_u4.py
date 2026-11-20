"""Claude's hand-drawn figures for me-thermo-u4 (Engineering Thermodynamics: availability and thermodynamic relations),
one per chapter, each drawn from that chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sub(base, s, size=14):
    """base text with a lowered subscript (no underscore on screen)"""
    return f'{base}<tspan dy="5" font-size="13">{s}</tspan><tspan dy="-5"> </tspan>'


def poly_fill(pts, fill, stroke='none', sw=0):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}"/>'


# ---- 4.1 available energy of 10 kg of water cooling from 360 K to 300 K ----
def f1():
    x0, x1, y0, y1 = 80, 660, 60, 380
    fx = lambda S: x0 + S / 8 * (x1 - x0)
    fy = lambda T: y1 - T / 400 * (y1 - y0)
    mc, T0, dS = 41.8, 300, 7.621
    curve = [(fx(S), fy(T0 * math.exp(S / mc))) for S in [dS * i / 40 for i in range(41)]]
    o = [axes(x0, x1, y0, y1, [0, 2, 4, 6, 8], [0, 100, 200, 300, 400], fx, fy,
              'entropy S, measured from the final state (kJ/K)', 'temperature T (K)')]
    o.append(R(fx(0), fy(T0), fx(dS) - fx(0), fy(0) - fy(T0), NXS, NX, 0, 1.5))
    o.append(poly_fill(curve + [(fx(dS), fy(T0)), (fx(0), fy(T0))], ACS, AC, 1))
    o.append(P(curve, AC, 3))
    o.append(L(x0, fy(T0), x1, fy(T0), INK, 1.5, '6 5'))
    o.append(Tb(x0 + 60, fy(T0) + 22, 'T₀ = 300 K', 14))
    o.append(C(fx(dS), fy(360), 6, AC)); o.append(T(fx(dS) + 10, fy(360) - 8, '360 K', 14, 'start', bold=True))
    o.append(C(fx(0), fy(T0), 6, AC))
    # direction of cooling along the curve
    a, b = curve[16], curve[8]
    o.append(L(a[0], a[1] - 12, b[0], b[1] - 12, AC, 2, arrow='n'))
    o.append(T(b[0] - 8, b[1] - 18, 'cooling', 13, 'end', AC))
    # available energy: the sliver above T0
    o.append(L(fx(4.2), 90, fx(4.2), fy(312), INK, 1.2))
    o.append(T(fx(4.2), 84, 'AE = 221.7 kJ (8.8 % of Q)', 15, 'middle', AC, bold=True))
    # unavailable energy: the rectangle below T0
    o.append(T(fx(dS / 2), fy(190), 'UE = T₀ΔS = 300 × 7.621', 15, bold=True))
    o.append(T(fx(dS / 2), fy(190) + 22, '= 2286.3 kJ', 15, bold=True))
    o.append(T(fx(dS / 2), fy(190) + 46, 'heat that must go to the surroundings', 14, fill=MUT))
    yb = fy(40)
    o.append(L(fx(0) + 4, yb, fx(dS) - 6, yb, INK, 1.5, arrow='l'))
    o.append(L(fx(dS) - 4, yb, fx(0) + 6, yb, INK, 1.5, arrow='l'))
    o.append(Tb(fx(dS / 2), yb + 5, 'ΔS = 41.8 × ln 1.2 = 7.621 kJ/K', 14))
    o.append(T(x1, 30, 'Q = 2508 kJ = AE + UE', 15, 'end', bold=True))
    return 440, ''.join(o)
FIG[1] = (f1, 'Heat from 10 kg of water cooling from 360 K to 300 K, on a T–s diagram: only the thin band above the T₀ line, 221.7 kJ, can become work; the rectangle below it, T₀ΔS = 2286.3 kJ, must go to the surroundings.',
          'A temperature-entropy diagram. A curve falls from 360 K to 300 K over an entropy width of 7.621 kJ/K. The thin band between the curve and the 300 K line is the available energy, 221.7 kJ; the large rectangle below the line is the unavailable energy, 2286.3 kJ.')


# ---- 4.2 energy and exergy accounts of the turbine example ----
def f2():
    x0, W = 60, 600
    k = W / 660
    o = []
    o.append(T(x0, 40, 'Energy account (first law)', 15, 'start', bold=True))
    o.append(R(x0, 52, 600 * k, 44, ACS, AC, 4))
    o.append(T(x0 + 300 * k, 80, 'enthalpy drop h₁ − h₂ = 600 kJ/kg → work 600 kJ/kg', 14))
    o.append(T(x0, 140, 'Exergy account (second law)', 15, 'start', bold=True))
    o.append(brace(x0, x0 + W, 162, INK, up=False))
    o.append(T(x0 + W / 2, 154, 'exergy drop ψ₁ − ψ₂ = (h₁ − h₂) + T₀(s₂ − s₁) = 600 + 60 = 660 kJ/kg', 14))
    o.append(R(x0, 176, 600 * k, 44, ACS, AC, 4))
    o.append(R(x0 + 600 * k, 176, 60 * k, 44, NXS, NX, 4))
    o.append(T(x0 + 300 * k, 204, 'work w = 600 kJ/kg', 15, bold=True))
    o.append(T(x0 + 630 * k, 204, '60', 15, bold=True))
    o.append(L(x0 + 630 * k, 222, x0 + 630 * k, 250, NX, 2, arrow='x'))
    o.append(T(x0 + W, 274, 'exergy destroyed i = T₀(s₂ − s₁)', 14, 'end', NX, bold=True))
    o.append(T(x0 + W, 294, '= 300 × (7.00 − 6.80) = 60 kJ/kg', 14, 'end', NX))
    o.append(T(x0, 274, 'The enthalpy drop is not the whole story:', 14, 'start'))
    o.append(T(x0, 294, 'the entropy rise adds 60 kJ/kg of exergy', 14, 'start'))
    o.append(T(x0, 314, 'that friction destroyed.', 14, 'start'))
    o.append(R(x0, 334, W, 40, PANEL, INK, 6, 1.5))
    o.append(T(x0 + W / 2, 360, 'second law efficiency = 600 ÷ 660 = 0.909', 15, bold=True))
    return 392, ''.join(o)
FIG[2] = (f2, 'The turbine of the first worked example in two accounts: by energy all of the 600 kJ/kg enthalpy drop becomes work, but by exergy the stream gave up 660 kJ/kg, so 60 kJ/kg was destroyed and the second law efficiency is 0.909.',
          'Two bars. The energy bar is 600 kJ/kg of enthalpy drop, all of it work. The exergy bar is 660 kJ/kg, split into 600 kJ/kg of work and 60 kJ/kg destroyed, equal to 300 K times an entropy rise of 0.20 kJ/(kg K). Second law efficiency 600 over 660 equals 0.909.')


# ---- 4.3 two paths between the same states: heat differs, entropy does not ----
def f3():
    x0, x1, y0, y1 = 90, 640, 60, 360
    fx = lambda v: x0 + (v - 0.6) / 1.4 * (x1 - x0)
    fy = lambda t: y1 - (t - 250) / 400 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0], [300, 400, 500, 600], fx, fy,
              'specific volume v (m³/kg)', 'temperature T (K)', lambda v: f'{v:.1f}')]
    p1, pa, p2, pb = (fx(0.861), fy(300)), (fx(0.861), fy(600)), (fx(1.722), fy(600)), (fx(1.722), fy(300))
    o.append(L(p1[0], p1[1] - 7, pa[0], pa[1] + 9, AC, 3, arrow='n'))
    o.append(L(pa[0] + 7, pa[1], p2[0] - 9, p2[1], AC, 3, arrow='n'))
    o.append(L(p1[0] + 7, p1[1], pb[0] - 9, pb[1], NX, 3, '8 5', arrow='x'))
    o.append(L(pb[0], pb[1] - 7, p2[0], p2[1] + 9, NX, 3, '8 5', arrow='x'))
    for (x, y), lab, dx, dy in ((p1, '1', -14, 20), (pa, 'a', -14, -8), (p2, '2', 14, -8), (pb, 'b', 14, 20)):
        o.append(C(x, y, 6, INK)); o.append(T(x + dx, y + dy, lab, 16, bold=True))
    o.append(T(pa[0] - 12, fy(450), 'q = 215.4', 14, 'end', AC, bold=True))
    o.append(T(pa[0] - 12, fy(450) + 18, '(constant v)', 13, 'end', AC))
    o.append(T((pa[0] + p2[0]) / 2, pa[1] - 12, 'q = 119.4 (isothermal, 600 K)', 14, fill=AC, bold=True))
    o.append(T((p1[0] + pb[0]) / 2, p1[1] + 22, 'q = 59.7 (isothermal, 300 K)', 14, fill=NX, bold=True))
    o.append(T(pb[0] + 12, fy(450), 'q = 215.4', 14, 'start', NX, bold=True))
    o.append(T(pb[0] + 12, fy(450) + 18, '(constant v)', 13, 'start', NX))
    cx = (p1[0] + pb[0]) / 2
    o.append(T(cx, fy(500), 'Path A, 1 → a → 2: q = 334.8 kJ/kg', 15, fill=AC, bold=True))
    o.append(T(cx, fy(500) + 24, 'Path B, 1 → b → 2: q = 275.1 kJ/kg', 15, fill=NX, bold=True))
    o.append(T(cx, fy(500) + 56, 'Δs = 0.6966 kJ/(kg·K) on both paths', 15, bold=True))
    o.append(T(cx, fy(500) + 78, 'heat: path function · entropy: property', 14, fill=MUT))
    return 420, ''.join(o)
FIG[3] = (f3, 'Two reversible paths for 1 kg of air from state 1 (300 K, 0.861 m³/kg) to state 2 (600 K, 1.722 m³/kg): the heat is 334.8 kJ/kg on one path and 275.1 kJ/kg on the other, but the entropy change is 0.6966 kJ/(kg·K) on both, because ds is exact and δq is not.',
          'A temperature-volume diagram with four corners 1, a, 2 and b. Path A rises at constant volume from 300 to 600 K, taking 215.4 kJ/kg, then expands at 600 K, taking 119.4. Path B expands at 300 K, taking 59.7, then rises at constant volume, taking 215.4. Totals 334.8 and 275.1 kJ/kg; entropy change 0.6966 on both.')


# ---- 4.4 Gibbs function of ice and liquid water near the freezing point ----
def f4():
    x0, x1, y0, y1 = 90, 630, 90, 370
    fx = lambda t: x0 + (t - 258.15) / 30 * (x1 - x0)
    Tm, Y0, k = 273.15, 230, 4.0     # k = px per kJ/kg
    si, sw = 1.0, 1.0 + 1.2209       # rough absolute slopes; their difference is the real 1.2209 kJ/(kg K)
    gy = lambda t, s: Y0 + k * s * (t - Tm)
    o = [L(x0, y1, x1, y1, L2, 1.5), L(x0, y0, x0, y1, L2, 1.5)]
    for t in (263.15, 273.15, 283.15):
        X = fx(t); o += [L(X, y1, X, y1 + 5, L2, 1.5), T(X, y1 + 20, f'{t:.2f}', 13, fill=MUT)]
    o.append(T((x0 + x1) / 2, y1 + 42, 'temperature T (K), at 1 atm', 14, fill=MUT))
    o.append(T(x0, y0 - 24, 'Gibbs function g (kJ/kg); each line falls with slope −s', 14, 'start', MUT))
    o.append(L(fx(Tm), y0, fx(Tm), y1, INK, 1.3, '5 5'))
    ta, tb = 259.65, 286.65
    o.append(L(fx(ta), gy(ta, si), fx(tb), gy(tb, si), AC, 3))
    o.append(L(fx(ta), gy(ta, sw), fx(tb), gy(tb, sw), NX, 3))
    o.append(T(fx(ta) + 6, gy(ta, sw) - 12, 'liquid water (steeper)', 14, 'start', NX, bold=True))
    o.append(T(fx(tb), gy(tb, si) - 12, 'ice', 14, 'end', AC, bold=True))
    for t in (263.15, 283.15):
        ya, yb = gy(t, si), gy(t, sw)
        o.append(L(fx(t), min(ya, yb) + 3, fx(t), max(ya, yb) - 3, INK, 1.8))
        o.append(C(fx(t), ya, 5, AC)); o.append(C(fx(t), yb, 5, NX))
    o.append(T(100, 228, 'ice lower by 12.2 kJ/kg:', 14, 'start', bold=True))
    o.append(T(100, 246, 'water freezes', 14, 'start'))
    o.append(T(x1, 150, 'water lower by 12.2 kJ/kg:', 14, 'end', bold=True))
    o.append(T(x1, 168, 'ice melts', 14, 'end'))
    o.append(C(fx(Tm), Y0, 6, INK))
    o.append(Tb(fx(Tm) + 12, Y0 - 30, 'equal g: Δg = 0', 14, 'start', bold=True))
    return 430, ''.join(o)
FIG[4] = (f4, 'The Gibbs function of ice and of liquid water against temperature: the lines cross at 273.15 K, where freezing has Δg = 0. Ten kelvin either side the gap is 12.2 kJ/kg, and the phase with the lower g is the one that forms. The slopes are drawn only roughly; the gaps carry the numbers.',
          'Two falling straight lines, ice and liquid water, crossing at 273.15 K. Water falls more steeply. At 263.15 K ice is 12.2 kJ/kg lower, so water freezes; at 283.15 K water is 12.2 kJ/kg lower, so ice melts.')


# ---- 4.5 van der Waals isochores of CO2: slope = (ds/dv) at constant T ----
def f5():
    x0, x1, y0, y1 = 100, 560, 60, 360
    fx = lambda t: x0 + (t - 295) / 55 * (x1 - x0)
    fy = lambda p: y1 - (p - 1.0) / 1.8 * (y1 - y0)
    Ru, a, b = 8.314, 0.364, 4.27e-5
    pv = lambda T, v: (Ru * T / (v - b) - a / v ** 2) / 1e6
    o = [axes(x0, x1, y0, y1, [300, 310, 320, 330, 340, 350], [1.0, 1.4, 1.8, 2.2, 2.6], fx, fy,
              'temperature T (K)', 'pressure p (MPa)', str, lambda p: f'{p:.1f}')]
    for v, c, lab, sl in ((0.001, AC, 'v = 0.001 m³/mol', '8.68'), (0.002, NX, 'v = 0.002 m³/mol', '4.25')):
        o.append(L(fx(300), fy(pv(300, v)), fx(350), fy(pv(350, v)), c, 3))
        o.append(T(fx(350) + 10, fy(pv(350, v)) + 5, lab, 14, 'start', c, bold=True))
        o.append(T(fx(350) + 10, fy(pv(350, v)) + 25, f'slope {sl} kPa/K', 14, 'start', c))
        o.append(C(fx(300), fy(pv(300, v)), 6, c))
    X = fx(300)
    o.append(T(X + 12, fy(pv(300, 0.001)) + 24, 'state 1: 2.24 MPa', 14, 'start', AC, bold=True))
    o.append(T(X + 12, fy(pv(300, 0.002)) - 14, 'state 2: 1.18 MPa', 14, 'start', NX, bold=True))
    o.append(L(X, fy(pv(300, 0.001)) + 10, X, fy(pv(300, 0.002)) - 12, INK, 2, arrow='l'))
    o.append(T(X + 12, fy(1.75), 'expand', 13, 'start', MUT)); o.append(T(X + 12, fy(1.75) + 17, 'at 300 K', 13, 'start', MUT))
    o.append(R(250, 200, 300, 62, PANEL, INK, 6, 1.2))
    o.append(T(400, 224, sub('slope of an isochore = R/(v − b) = (∂s/∂v)', 'T'), 14))
    o.append(T(400, 248, 'Δs from 1 to 2 = 5.946 J/(mol·K)', 14, bold=True))
    return 410, ''.join(o)
FIG[5] = (f5, 'Constant-volume lines of carbon dioxide as a van der Waals gas: each is straight, and by the Maxwell relation its slope R/(v − b), 8.68 kPa/K at 0.001 m³/mol and 4.25 kPa/K at 0.002 m³/mol, is the rate at which entropy grows with volume at fixed temperature.',
          'Pressure against temperature from 300 to 350 K for two volumes of carbon dioxide, 0.001 and 0.002 cubic metres per mole. Both lines are straight, with slopes 8.68 and 4.25 kPa per kelvin. At 300 K the pressures are 2.24 and 1.18 MPa; expanding from the first state to the second raises entropy by 5.946 J per mol K.')


# ---- 4.6 saturation pressure of water: integrated Clausius-Clapeyron against the steam tables ----
def f6():
    x0, x1, y0, y1 = 90, 640, 60, 360
    fx = lambda t: x0 + (t - 318) / 60 * (x1 - x0)
    fy = lambda p: y1 - p / 110 * (y1 - y0)
    model = lambda t: 101.3 * math.exp(-2257 / 0.4615 * (1 / t - 1 / 373))
    o = [axes(x0, x1, y0, y1, [320, 330, 340, 350, 360, 370], [0, 20, 40, 60, 80, 100], fx, fy,
              'saturation temperature T (K)', 'saturation pressure p (kPa)')]
    o.append(P([(fx(t), fy(model(t))) for t in [318 + i * 0.5 for i in range(115)]], AC, 3))
    table = [(323.15, 12.35), (333.15, 19.95), (343.15, 31.20), (353.15, 47.42), (363.15, 70.18), (373.15, 101.42)]
    for t, pp in table:
        o.append(f'<rect x="{fx(t) - 5:.1f}" y="{fy(pp) - 5:.1f}" width="10" height="10" style="fill:var(--next);stroke:var(--fig);stroke-width:1.5"/>')
    o.append(C(fx(373), fy(101.3), 6, AC))
    o.append(T(fx(373) - 14, fy(101.3) - 8, 'input: 101.3 kPa at 373 K', 14, 'end', bold=True))
    o.append(C(fx(323), fy(13.31), 5, AC))
    o.append(L(fx(323) + 4, fy(13.31) - 8, fx(326), fy(54), INK, 1.2))
    o.append(T(fx(322), fy(72), 'at 323 K:', 14, 'start', bold=True))
    o.append(T(fx(322), fy(72) + 18, 'estimate 13.31 kPa', 14, 'start', AC))
    o.append(T(fx(322), fy(72) + 36, 'steam table 12.35 kPa', 14, 'start', NX))
    o += [L(110, 92, 140, 92, AC, 3), T(148, 97, 'integrated equation, h fixed at 2257 kJ/kg', 14, 'start')]
    o.append(f'<rect x="120" y="108" width="10" height="10" style="fill:var(--next)"/>')
    o.append(T(148, 118, 'steam-table values', 14, 'start'))
    return 420, ''.join(o)
FIG[6] = (f6, 'Saturation pressure of water: the curve is the integrated Clausius-Clapeyron equation started from 101.3 kPa at 373 K with the latent heat held at 2257 kJ/kg, and the squares are steam-table values. The curve lies a little high at low temperature (13.31 against 12.35 kPa at 323 K), because the real latent heat grows as the temperature falls.',
          'Saturation pressure against temperature from 318 to 378 K. A rising curve from the Clausius-Clapeyron equation passes through 101.3 kPa at 373 K. Square markers show steam-table values 12.35, 19.95, 31.20, 47.42, 70.18 and 101.42 kPa at 323 to 373 K. At 323 K the curve gives 13.31 kPa.')


# ---- 4.7 van der Waals estimate of the Joule-Thomson coefficient of nitrogen ----
def f7():
    x0, x1, y0, y1 = 90, 650, 60, 340
    fx = lambda t: x0 + (t - 200) / 800 * (x1 - x0)
    lo, hi = -0.1, 0.5
    fy = lambda m: y1 - (m - lo) / (hi - lo) * (y1 - y0)
    a, b, cp, Ru = 0.137, 3.87e-5, 29.1, 8.314
    mu = lambda t: (2 * a / (Ru * t) - b) / cp * 1e5
    o = [axes(x0, x1, y0, y1, [200, 300, 400, 500, 600, 700, 800, 900, 1000], [-0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5], fx, fy,
              'temperature T (K)', 'Joule-Thomson coefficient (K/bar)', str, lambda m: neg(f'{m:.1f}'))]
    o.append(L(x0, fy(0), x1, fy(0), INK, 1.5))
    o.append(P([(fx(t), fy(mu(t))) for t in range(200, 1001, 10)], AC, 3))
    o.append(C(fx(300), fy(mu(300)), 6, AC))
    o.append(T(fx(300) + 12, fy(mu(300)) - 8, '300 K: 0.245 K/bar', 14, 'start', bold=True))
    o.append(T(fx(300) + 12, fy(mu(300)) + 12, '20 → 1 bar: about −4.6 K', 14, 'start'))
    Ti = 2 * a / (Ru * b)
    o.append(C(fx(Ti), fy(0), 6, NX))
    o.append(L(fx(Ti), fy(0) - 8, fx(Ti), fy(0.16), NX, 1.3, '4 4'))
    o.append(T(fx(Ti), fy(0.16) - 22, 'inversion', 14, fill=NX, bold=True))
    o.append(T(fx(Ti), fy(0.16) - 4, 'T = 2a/(Rb) = 852 K', 14, fill=NX, bold=True))
    o.append(T(fx(640), fy(0.13), 'positive: the gas cools in a throttle', 14, 'middle', AC))
    o.append(T(fx(930), fy(-0.065), 'negative: warms', 14, 'middle', NX))
    return 400, ''.join(o)
FIG[7] = (f7, 'The low-pressure van der Waals estimate of the Joule-Thomson coefficient of nitrogen: 0.245 K/bar at 300 K, so throttling from 20 bar to 1 bar cools the gas by about 4.6 K; the coefficient falls with temperature and changes sign at the estimated inversion temperature of 852 K.',
          'A falling curve of the Joule-Thomson coefficient of nitrogen from about 0.43 K per bar at 200 K, through 0.245 at 300 K, to zero at 852 K and slightly negative above. Above the axis the gas cools when throttled; below it, it warms.')


spec = make_spec(FIG)
