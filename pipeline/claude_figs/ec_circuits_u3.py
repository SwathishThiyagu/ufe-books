"""Claude's hand-drawn figures for ec-circuits-u3 (Sinusoidal steady state and AC power), one per chapter.
Every curve and phasor is computed from that chapter's own worked example; colours are the shell's CSS variables."""
import os, sys, math, cmath
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
W = 720


def curve(f, a, b, fx, fy, n=240, c=AC, w=2.5, dash=None):
    return P([(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


def vec(x0, y0, mag, ang, sc, c=AC, w=3, arrow='n', dash=None):
    """phasor of magnitude mag at angle ang (degrees, anticlockwise) from (x0, y0); returns svg and the tip"""
    x1 = x0 + mag * sc * math.cos(math.radians(ang)); y1 = y0 - mag * sc * math.sin(math.radians(ang))
    return L(x0, y0, x1, y1, c, w, dash, arrow), (x1, y1)


def angarc(x0, y0, r, a0, a1, c=NX, w=1.8):
    """arc of radius r from angle a0 to a1 (degrees, anticlockwise positive)"""
    p0 = (x0 + r * math.cos(math.radians(a0)), y0 - r * math.sin(math.radians(a0)))
    p1 = (x0 + r * math.cos(math.radians(a1)), y0 - r * math.sin(math.radians(a1)))
    sweep = 0 if a1 > a0 else 1
    large = 1 if abs(a1 - a0) > 180 else 0
    return f'<path d="M{p0[0]:.1f},{p0[1]:.1f} A{r},{r} 0 {large},{sweep} {p1[0]:.1f},{p1[1]:.1f}" style="fill:none;stroke:{c};stroke-width:{w}"/>'


SUB = lambda s: f'<tspan font-size="11" baseline-shift="sub">{s}</tspan>'


# ---- 3.1 one cycle of 325 sin(314t) with its RMS and half-cycle average ----
def f1():
    o = []
    x0, x1, yc, A = 80, 680, 190, 130          # 0..20 ms across, 325 V = 130 px
    fx = lambda t: x0 + t / 20 * (x1 - x0)
    fy = lambda v: yc - v / 325 * A
    # shaded positive half and the equal-area rectangle
    pts = [(fx(0), yc)] + [(fx(10 * i / 120), fy(325 * math.sin(math.pi * i / 120))) for i in range(121)] + [(fx(10), yc)]
    o.append(P(pts, 'none', 0, fill=ACS))
    o.append(L(x0, yc, x1, yc, L2, 1.5)); o.append(L(x0, fy(345), x0, fy(-345), L2, 1.5))
    for t in (0, 5, 10, 15, 20):
        o.append(L(fx(t), yc, fx(t), yc + 5, L2, 1.5)); o.append(T(fx(t) - (14 if t == 20 else 0), yc + 20, str(t) + (' ms' if t == 20 else ''), 13, fill=MUT))
    for v in (325, -325):
        o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 9, fy(v) + 4.5, neg(v), 13, 'end', MUT))
    o.append(curve(lambda t: 325 * math.sin(2 * math.pi * t / 20), 0, 20, fx, fy, 300, AC, 2.8))
    o.append(L(x0, fy(229.8), x1, fy(229.8), LV, 2.2, '8 5'))
    o.append(L(fx(0), fy(206.9), fx(10), fy(206.9), NX, 2.4))
    o.append(C(fx(5), fy(325), 5, AC))
    o.append(Tb(fx(5), fy(325) - 12, 'peak V' + SUB('m') + ' = 325 V', 14))
    o.append(Tb(fx(13.2), fy(229.8) - 8, 'RMS = 325/√2 = 229.8 V', 14, 'start', LV))
    o.append(Tb(fx(5), fy(206.9) + 22, 'half-cycle average = 2 × 325/π = 206.9 V', 13, 'middle', NX))
    o.append(Tb(fx(5), fy(80), 'shaded area = area', 13, 'middle', INK))
    o.append(Tb(fx(5), fy(80) + 18, 'under the average line', 13, 'middle', INK))
    o.append(T(fx(15), fy(-325) - 14, 'second half: same shape below the axis', 13, 'middle', MUT))
    o.append(brace(fx(0), fx(20), fy(-345) + 24, INK))
    o.append(T(fx(10), fy(-345) + 48, 'one period T = 1/f = 20 ms (f = 314/2π ≈ 50 Hz)', 14, 'middle', INK))
    o.append(T(x0 + 6, 26, 'v(t) = 325 sin(314t) V', 14, 'start', INK, True))
    return 400, ''.join(o)


FIG[1] = (f1, 'The supply of the worked example over one 20 ms period. The RMS line (229.8 V) is the steady value that heats a resistor equally; '
              'the shorter line is the half-cycle average (206.9 V), whose rectangle has the same area as the shaded hump.',
          'One cycle of 325 sin 314t from 0 to 20 ms with peak 325 V, a dashed RMS line at 229.8 V across the period and a half-cycle average line at 206.9 V over the first 10 ms.')


# ---- 3.2 tip-to-tail addition 20∠0° + 15∠60° ----
def f2():
    o = []
    ox, oy, sc = 80, 300, 14.5
    o.append(L(ox - 20, oy, 690, oy, L2, 1.2)); o.append(L(ox, oy + 16, ox, 40, L2, 1.2))
    o.append(T(690, oy + 20, 'real axis', 13, 'end', MUT)); o.append(T(ox + 8, 52, 'j axis', 13, 'start', MUT))
    s, a1 = vec(ox, oy, 20, 0, sc); o.append(s)
    s, tip = vec(a1[0], a1[1], 15, 60, sc, LV, arrow='l'); o.append(s)
    # parallelogram sides
    s, b = vec(ox, oy, 15, 60, sc, L2, 1.6, None, '5 5'); o.append(s)
    o.append(L(b[0], b[1], tip[0], tip[1], L2, 1.6, '5 5'))
    s, r = vec(ox, oy, 30.41, 25.28, sc, NX, 3, 'x', '9 5'); o.append(s)
    o.append(angarc(ox, oy, 70, 0, 25.28)); o.append(T(ox + 78, oy - 12, '25.3°', 13, 'start', NX))
    o.append(angarc(a1[0], a1[1], 40, 0, 60, MUT)); o.append(T(a1[0] + 44, a1[1] - 20, '60°', 13, 'start', MUT))
    o.append(Tb((ox + a1[0]) / 2, oy + 24, 'V' + SUB('1') + ' = 20∠0° V', 14, 'middle', AC))
    o.append(Tb(a1[0] + 70, (a1[1] + tip[1]) / 2 + 10, 'V' + SUB('2') + ' = 15∠60° V', 14, 'start', LV))
    o.append(Tb(ox + 150, oy - 116, 'V = 30.4∠25.3° V', 14, 'middle', NX, True))
    o.append(T(tip[0] + 10, tip[1] - 6, '27.5 + j13.0', 13, 'start', MUT))
    o.append(T(690, 40, 'sine reference, peak values', 13, 'end', MUT))
    return 340, ''.join(o)


FIG[2] = (f2, 'The worked example on the complex plane: V<sub>2</sub> is drawn from the tip of V<sub>1</sub>, and the dashed resultant from the origin is the sum, 30.4 V at 25.3°. '
              'The dashed sides complete the parallelogram; the sum is not 20 + 15 = 35 V because the two arrows point in different directions.',
          'Phasor diagram: V1 of 20 volts along the real axis, V2 of 15 volts at 60 degrees drawn from its tip, and the resultant of 30.4 volts at 25.3 degrees from the origin to the point 27.5 plus j13.0.')


# ---- 3.3 impedance triangle of the series coil and capacitor ----
def f3():
    o = []
    ox, oy, sc = 120, 64, 10
    o.append(L(ox - 30, oy, ox + 140, oy, L2, 1.2)); o.append(L(ox, oy - 34, ox, oy + 280, L2, 1.2))
    o.append(T(ox + 140, oy - 8, 'R', 13, 'end', MUT)); o.append(T(ox - 8, oy - 22, '+jX', 13, 'end', MUT)); o.append(T(ox - 8, oy + 278, '−jX', 13, 'end', MUT))
    xr = ox + 8 * sc; yb = oy + 25.55 * sc
    o.append(P([(ox, oy), (xr, oy), (xr, yb), (ox, oy)], 'none', 0, fill=ACS))
    o.append(L(ox, oy, xr, oy, AC, 3, arrow='n'))
    o.append(L(xr, oy, xr, yb, NX, 3, arrow='x'))
    o.append(L(ox, oy, xr, yb, LV, 3, arrow='l'))
    o.append(T((ox + xr) / 2, oy - 10, 'R = 8 Ω', 14, 'middle', AC, True))
    o.append(T(xr + 10, (oy + yb) / 2 - 8, 'X = 6.28 − 31.83', 14, 'start', NX, True))
    o.append(T(xr + 10, (oy + yb) / 2 + 12, '= −25.55 Ω', 14, 'start', NX, True))
    o.append(Tb(ox - 6, yb - 60, '|Z| = 26.77 Ω', 14, 'end', LV, True))
    o.append(angarc(ox, oy, 46, 0, -72.6)); o.append(T(ox + 34, oy + 62, '−72.6°', 13, 'start', NX))
    # the three element impedances
    bx = 380
    o.append(boxt(bx, 40, 310, 62, ['Resistor: Z = 8 Ω', 'angle 0°'], PANEL, AC, 14, True))
    o.append(boxt(bx, 116, 310, 62, ['Coil: X' + SUB('L') + ' = ωL = 314.16 × 0.02', '= +6.28 Ω, angle +90°'], PANEL, AC, 14, True))
    o.append(boxt(bx, 192, 310, 62, ['Capacitor: X' + SUB('C') + ' = 1/(ωC)', '= 31.83 Ω, enters as −j31.83'], PANEL, NX, 14, True))
    o.append(boxt(bx, 268, 310, 62, ['I = 230/26.77 = 8.59 A', 'leads V by 72.6°'], 'var(--live-soft)', LV, 14, True))
    return 352, ''.join(o)


FIG[3] = (f3, 'Impedance triangle of the worked example: 8 Ω across, a net reactance of −25.55 Ω down, so Z = 26.77 Ω at −72.6°. '
              'A triangle that points down means a capacitive circuit, so the current leads the voltage.',
          'Impedance triangle with R = 8 ohm horizontal, net reactance minus 25.55 ohm downward and hypotenuse 26.77 ohm at minus 72.6 degrees; boxes list the resistor, coil reactance 6.28 ohm, capacitor reactance 31.83 ohm and current 8.59 A leading.')


# ---- 3.4 phasor diagram of the series RLC example, current as reference ----
def f4():
    o = []
    ox, oy, sc = 100, 226, 0.62
    o.append(L(ox - 30, oy, ox + 230, oy, L2, 1.2)); o.append(L(ox, oy - 186, ox, oy + 224, L2, 1.2))
    s, rt = vec(ox, oy, 212.5, 0, sc); o.append(s)
    s, lt = vec(ox, oy, 250.4, 90, sc, AC); o.append(s)
    s, ct = vec(ox, oy, 338.3, -90, sc, NX, 3, 'x'); o.append(s)
    o.append(L(ox, oy - 12, ox + 80, oy - 12, LV, 4, arrow='l'))
    o.append(T(ox + 8, oy - 30, 'I = 5.31 A', 13, 'start', LV, True))
    net = (rt[0], oy + 87.9 * sc)
    o.append(L(rt[0], oy, net[0], net[1], MUT, 2, '5 4', 'm'))
    o.append(L(ox, oy, net[0], net[1], AC, 3.4, arrow='n'))
    o.append(angarc(ox, oy, 52, 0, -22.5)); o.append(T(ox + 62, oy + 16, '22.5°', 13, 'start', NX))
    o.append(Tb(rt[0] + 6, oy - 10, 'V' + SUB('R') + ' = 212.5 V', 14, 'start', AC))
    o.append(T(lt[0] + 10, lt[1] + 14, 'V' + SUB('L') + ' = 250.4 V', 14, 'start', AC))
    o.append(T(ct[0] + 10, ct[1] - 4, 'V' + SUB('C') + ' = 338.3 V', 14, 'start', NX))
    o.append(T(net[0] + 10, net[1] + 4, 'V' + SUB('L') + ' − V' + SUB('C') + ' = −87.9 V', 13, 'start', MUT))
    o.append(Tb(ox + 120, net[1] + 30, 'V = 230 V', 14, 'middle', AC, True))
    bx = 420
    o.append(boxt(bx, 50, 270, 74, ['R = 40 Ω, X' + SUB('L') + ' = 47.12 Ω', 'X' + SUB('C') + ' = 63.66 Ω', 'Z = 43.28∠−22.5° Ω'], PANEL, AC, 14))
    o.append(boxt(bx, 140, 270, 54, ['I = 230/43.28 = 5.31 A', 'reference, at 0°'], 'var(--live-soft)', LV, 14))
    o.append(boxt(bx, 210, 270, 74, ['V' + SUB('R') + ' along I', 'V' + SUB('L') + ' 90° ahead of I', 'V' + SUB('C') + ' 90° behind I'], PANEL, L2, 14))
    o.append(boxt(bx, 300, 270, 74, ['√(212.5² + 87.9²) = 230 V', 'V lags I by 22.5°:', 'the current leads'], PANEL, NX, 14))
    return 456, ''.join(o)


FIG[4] = (f4, 'Phasor diagram of the series RLC worked example with the current as reference. V<sub>L</sub> and V<sub>C</sub> are each larger than the 230 V supply, '
              'but they point in opposite directions; their small difference (87.9 V) and V<sub>R</sub> rebuild the supply, which sits 22.5° behind the current.',
          'Current 5.31 A along the reference axis; V_R 212.5 V along it, V_L 250.4 V straight up, V_C 338.3 V straight down, net reactive voltage minus 87.9 V and the supply 230 V at minus 22.5 degrees.')


# ---- 3.5 the motor: instantaneous power, and the power triangle before and after correction ----
def f5():
    o = []
    x0, x1, y0, y1 = 80, 680, 52, 214
    fx = lambda t: x0 + t / 20 * (x1 - x0)
    fy = lambda p: y1 - (p + 800) / 5000 * (y1 - y0)
    w = 2 * math.pi * 50
    p = lambda t: 325.27 * math.sin(w * t / 1000) * 14.142 * math.sin(w * t / 1000 - math.radians(36.87))
    o.append(L(x0, fy(0), x1, fy(0), L2, 1.5)); o.append(L(x0, y0 - 6, x0, y1 + 4, L2, 1.5))
    for v in (-460, 1840, 4140):
        o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 9, fy(v) + 4.5, neg(v), 13, 'end', MUT))
    for t in (0, 5, 10, 15, 20):
        o.append(T(fx(t) - (14 if t == 20 else 0), fy(0) + 20, str(t) + (' ms' if t == 20 else ''), 13, fill=MUT))
    o.append(L(x0, fy(1840), x1, fy(1840), LV, 2, '8 5'))
    o.append(curve(p, 0, 20, fx, fy, 300, AC, 2.6))
    tm = 1000 * (math.radians(36.87) / 2) / w  # first minimum near ωt = φ/2
    o.append(C(fx(1.024), fy(-460), 5, NX)); o.append(C(fx(11.024), fy(-460), 5, NX))
    o.append(Tb(fx(11.024) + 10, fy(-460) + 20, 'dips to −460 W: energy goes back', 13, 'start', NX))
    o.append(Tb(fx(15.5), fy(1840) - 8, 'average P = 1840 W', 14, 'middle', LV))
    o.append(Tb(fx(5.5) + 8, fy(4140) + 4, 'peak 4140 W', 13, 'start', INK))
    o.append(T(x0, 30, 'p(t) = v(t) i(t) in W, 230 V, 10 A, φ = 36.87°', 14, 'start', INK, True))
    # power triangles
    bx, by, sc = 110, 432, 0.11
    xp = bx + 1840 * sc
    o.append(L(bx, by, xp, by, AC, 3, arrow='n'))
    o.append(L(xp, by, xp, by - 1380 * sc, NX, 3, arrow='x'))
    o.append(L(bx, by, xp, by - 1380 * sc, INK, 2.2, '7 4'))
    o.append(L(bx, by, xp - 6, by - 604.8 * sc, LV, 3, arrow='l'))
    o.append(T((bx + xp) / 2, by + 22, 'P = 1840 W (unchanged)', 14, 'middle', AC, True))
    y1q, y2q = by - 1380 * sc, by - 604.8 * sc
    o.append(T(xp + 12, y1q + 6, 'Q' + SUB('1') + ' = 1380 var', 14, 'start', NX))
    o.append(T(xp + 12, y1q + 24, 'before: 2300 VA, pf 0.80', 13, 'start', MUT))
    o.append(T(xp + 12, y2q + 6, 'Q' + SUB('2') + ' = 604.8 var', 14, 'start', LV))
    o.append(T(xp + 12, y2q + 24, 'after: 1937 VA, pf 0.95', 13, 'start', MUT))
    xc = 530
    o.append(L(xc, y1q, xc, y2q - 2, MUT, 2.4, None, 'm'))
    o.append(T(xc + 12, y1q + 30, 'the capacitor', 13, 'start', MUT))
    o.append(T(xc + 12, y1q + 48, 'supplies', 13, 'start', MUT))
    o.append(T(xc + 12, y1q + 68, 'Q' + SUB('C') + ' = 775.2 var', 14, 'start', INK, True))
    o.append(T(700, 432, 'C = 775.2/(314.16 × 230²) = 46.6 µF', 14, 'end', INK, True))
    o.append(T(700, 454, 'supply current falls from 10 A to 8.42 A', 13, 'end', MUT))
    return 470, ''.join(o)


FIG[5] = (f5, 'Top: instantaneous power of the worked example\'s motor. It pulses at 100 Hz between −460 W and 4140 W and averages P = 1840 W. '
              'Bottom: its power triangle; the 46.6 µF capacitor cancels 775.2 var, so the triangle flattens from pf 0.80 to 0.95 while P stays the same.',
          'Top: p(t) over 20 ms swinging from minus 460 W to 4140 W around an average of 1840 W. Bottom: power triangle with P 1840 W, Q falling from 1380 var to 604.8 var after a 775.2 var capacitor, apparent power from 2300 to 1937 VA.')


# ---- 3.6 phasor diagram of the balanced star example ----
def f6():
    o = []
    ox, oy, sv, si = 240, 236, 0.62, 4.4
    o.append(L(ox - 200, oy, ox + 260, oy, LN, 1)); o.append(L(ox, oy - 210, ox, oy + 210, LN, 1))
    tips = {}
    for name, ang in (('R', 0), ('Y', -120), ('B', 120)):
        s, tips[name] = vec(ox, oy, 230.9, ang, sv); o.append(s)
    for name, ang in (('R', -30.96), ('Y', -150.96), ('B', 89.04)):
        s, t = vec(ox, oy, 19.8, ang, si, LV, 2.6, 'l'); o.append(s); tips['I' + name] = t
    # V_RY = V_R − V_Y, drawn as V_R plus (−V_Y)
    s, mt = vec(tips['R'][0], tips['R'][1], 230.9, 60, sv, L2, 2, 'm', '6 4'); o.append(s)
    s, vry = vec(ox, oy, 400, 30, sv, NX, 3, 'x'); o.append(s)
    o.append(T(tips['R'][0] + 6, tips['R'][1] + 20, 'V' + SUB('R') + ' = 230.9∠0°', 14, 'start', AC))
    o.append(T(tips['Y'][0] - 6, tips['Y'][1] + 18, 'V' + SUB('Y') + ' = 230.9∠−120°', 14, 'middle', AC))
    o.append(T(tips['B'][0] - 6, tips['B'][1] - 10, 'V' + SUB('B') + ' = 230.9∠120°', 14, 'middle', AC))
    o.append(T(vry[0] + 14, vry[1] - 4, 'V' + SUB('RY') + ' = 400∠30°', 14, 'start', NX, True))
    o.append(T(mt[0] - 38, mt[1] + 72, '−V' + SUB('Y'), 13, 'start', MUT))
    o.append(T(tips['IR'][0] + 4, tips['IR'][1] + 20, 'I' + SUB('R') + ' = 19.8∠−31°', 13, 'start', LV))
    o.append(T(tips['IY'][0] - 4, tips['IY'][1] - 10, 'I' + SUB('Y') + ' ∠−151°', 13, 'end', LV))
    o.append(T(tips['IB'][0] + 8, tips['IB'][1] + 4, 'I' + SUB('B') + ' ∠89°', 13, 'start', LV))
    o.append(angarc(ox, oy, 120, 0, 30)); o.append(T(ox + 128, oy - 26, '30°', 13, 'start', NX))
    o.append(angarc(ox, oy, 58, 0, -30.96, LV)); o.append(T(ox + 64, oy + 30, '31°', 13, 'start', LV))
    o.append(T(700, 30, 'Z = 10 + j6 Ω per phase, 400 V', 13, 'end', MUT))
    o.append(T(700, 50, 'R-Y-B sequence', 13, 'end', MUT))
    o.append(T(700, 440, 'three currents 120° apart: I' + SUB('N') + ' = 0', 13, 'end', MUT))
    return 456, ''.join(o)


FIG[6] = (f6, 'Phasor diagram of the balanced star worked example. The phase voltages are 230.9 V, 120° apart; the line voltage V<sub>RY</sub> = V<sub>R</sub> − V<sub>Y</sub> is √3 times longer and 30° ahead of V<sub>R</sub>. '
              'Each 19.8 A current lags its own phase voltage by 31°, and the three currents add to zero.',
          'Phasor diagram: three phase voltages of 230.9 volts at 0, minus 120 and 120 degrees, the line voltage V_RY of 400 volts at 30 degrees built from V_R and minus V_Y, and three currents of 19.8 amperes at minus 31, minus 151 and 89 degrees.')


# ---- 3.7 two-wattmeter connection with the example's readings ----
def f7():
    o = []
    ys = {'R': 80, 'Y': 170, 'B': 260}
    xl, xr = 60, 600
    for n, y in ys.items():
        o.append(L(xl, y, xr, y, AC, 2.4))
        o.append(T(xl - 10, y + 5, n, 15, 'end', INK, True))
    o.append(R(xr, 52, 100, 236, PANEL, AC))
    o.append(T(xr + 50, 160, 'three-wire', 13, 'middle', MUT)); o.append(T(xr + 50, 178, 'load', 14, 'middle', INK, True))
    o.append(T(xl + 6, 32, 'supply', 13, 'start', MUT))
    for i, (n, x, rd) in enumerate((('R', 240, '5.5'), ('Y', 400, '2.5'))):
        y = ys[n]
        o.append(R(x - 34, y - 13, 68, 26, 'var(--live-soft)', LV, 6))
        o.append(T(x, y + 5, 'CC', 13, 'middle', LV, True))
        o.append(f'<circle cx="{x}" cy="{y - 48}" r="24" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
        o.append(T(x, y - 43, 'W' + SUB(str(i + 1)), 15, 'middle', INK, True))
        o.append(L(x, y - 24, x, y - 13, LV, 2))
        o.append(T(x + 30, y - 58, rd + ' kW', 14, 'start', INK, True))
        # voltage coil lead to B
        xv = x + 56
        o.append(P([(x + 24, y - 48), (xv, y - 48), (xv, ys['B'])], NX, 2, '6 4'))
        o.append(C(xv, ys['B'], 5, NX))
        o.append(T(xv + 6, (y + ys['Y']) / 2 + 4 if n == 'R' else (y + ys['B']) / 2 + 30, 'VC to B', 13, 'start', NX))
    o.append(T(360, 310, 'P = W' + SUB('1') + ' + W' + SUB('2') + ' = 5.5 + 2.5 = 8.0 kW', 15, 'middle', INK, True))
    o.append(T(360, 334, 'tan φ = √3 × (5.5 − 2.5)/8.0 = 0.650, so φ = 33.0° and pf = 0.839', 14, 'middle', MUT))
    return 352, ''.join(o)


FIG[7] = (f7, 'The two-wattmeter connection of the worked example: current coils (CC) in lines R and Y, voltage coils (VC) returned to line B. '
              'The readings 5.5 kW and 2.5 kW add to the total power, and for this balanced load their difference gives the power factor.',
          'Three supply lines R, Y and B run to a three-wire load. Wattmeter W1 has its current coil in line R and voltage coil to B, reading 5.5 kW; W2 has its current coil in line Y and voltage coil to B, reading 2.5 kW. Total 8.0 kW, power factor 0.839.')


# ---- 3.8 the distorted voltage of the worked example and its two lines ----
def f8():
    o = []
    x0, x1, yc, A = 70, 470, 180, 120 / 130
    fx = lambda t: x0 + t / 20 * (x1 - x0)
    fy = lambda v: yc - v * A
    w = 2 * math.pi * 50
    v1 = lambda t: 100 * math.sin(w * t / 1000)
    v3 = lambda t: 30 * math.sin(3 * w * t / 1000 + math.radians(30))
    o.append(L(x0, yc, x1, yc, L2, 1.5)); o.append(L(x0, fy(135), x0, fy(-135), L2, 1.5))
    for v in (-100, 100):
        o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 9, fy(v) + 4.5, neg(v), 13, 'end', MUT))
    for t in (0, 10, 20):
        o.append(L(fx(t), yc, fx(t), yc + 5, L2, 1.5)); o.append(T(fx(t) - (14 if t == 20 else 0), fy(-135) + 18, str(t) + (' ms' if t == 20 else ''), 13, fill=MUT))
    o.append(curve(v1, 0, 20, fx, fy, 200, L2, 2.2, '7 5'))
    o.append(curve(v3, 0, 20, fx, fy, 300, LV, 1.8))
    o.append(curve(lambda t: v1(t) + v3(t), 0, 20, fx, fy, 400, AC, 3))
    o.append(T(x0, 32, 'v(t) = 100 sin ωt + 30 sin(3ωt + 30°) V', 14, 'start', INK, True))
    o.append(Tb(fx(15), fy(-100) + 26, 'fundamental (dashed)', 13, 'middle', MUT))
    o.append(Tb(fx(13), fy(48), '3rd harmonic', 13, 'middle', LV))
    o.append(Tb(fx(8.4), fy(104), 'sum', 14, 'start', AC, True))
    # RMS spectrum
    bx0, by = 540, 300
    hs = 2.4
    for n, (r, lab) in enumerate(((70.71, '70.71 V'), (21.21, '21.21 V'))):
        x = bx0 + n * 80
        o.append(R(x - 22, by - r * hs, 44, r * hs, ACS if n == 0 else 'var(--live-soft)', AC if n == 0 else LV, 3))
        o.append(T(x, by - r * hs - 8, lab, 13, 'middle', INK, True))
        o.append(T(x, by + 20, '50 Hz' if n == 0 else '150 Hz', 13, 'middle', MUT))
    o.append(L(bx0 - 40, by, bx0 + 120, by, L2, 1.5))
    o.append(T(bx0 + 40, 66, 'RMS of each line', 13, 'middle', MUT))
    o.append(T(bx0 + 40, by + 44, 'RMS = √(70.71² + 21.21²) = 73.8 V', 13, 'middle', INK))
    o.append(T(bx0 + 40, by + 64, 'THD = 21.21/70.71 = 30 %', 13, 'middle', INK, True))
    return 380, ''.join(o)


FIG[8] = (f8, 'The voltage of the worked example: a 100 V fundamental (dashed) plus a 30 V third harmonic gives the two-humped solid wave. '
              'On the right are the RMS values of the two lines; they combine by root-sum-square to 73.8 V, and their ratio is the 30 % THD.',
          'Left: one 20 ms period of 100 sin omega t dashed, 30 sin(3 omega t plus 30 degrees) thin, and their sum bold. Right: bars of 70.71 V at 50 Hz and 21.21 V at 150 Hz, total RMS 73.8 V and THD 30 percent.')


spec = make_spec(FIG)
