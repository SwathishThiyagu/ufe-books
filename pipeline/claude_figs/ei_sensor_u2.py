"""Claude's hand-drawn figures for ei-sensor-u2 (Sensors and Measurements: resistive sensors and thermocouples), one per
chapter, drawn from each chapter's own worked examples and numbers. Colours are the shell's CSS variables only."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
AFTER = {1: 2, 2: 3, 3: 3, 4: 3, 5: 2, 6: 2, 7: 4}


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def arrow(x1, y1, x2, y2, c=AC, w=2, k='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=k)


def sub(s):
    return f'<tspan baseline-shift="sub" font-size="11">{s}</tspan>'


def sup(s):
    return f'<tspan baseline-shift="super" font-size="11">{s}</tspan>'


def res_h(x1, x2, y, c=INK, n=6, amp=8):
    pts = [(x1, y)]
    a, b = x1 + 10, x2 - 10
    for i in range(n * 2):
        pts.append((a + (b - a) * (i + 0.5) / (n * 2), y + (amp if i % 2 == 0 else -amp)))
    pts += [(b, y), (x2, y)]
    return P(pts, c, 2)


def res_v(x, y1, y2, c=INK, n=6, amp=8):
    pts = [(x, y1)]
    a, b = y1 + 10, y2 - 10
    for i in range(n * 2):
        pts.append((x + (amp if i % 2 == 0 else -amp), a + (b - a) * (i + 0.5) / (n * 2)))
    pts += [(x, b), (x, y2)]
    return P(pts, c, 2)


def gauge(x, y, w, h, c=AC, vertical=False):
    """a small foil-gauge grid symbol centred at x, y"""
    o = [R(x - w / 2, y - h / 2, w, h, ACS if c == AC else LVS, c, 2, 1.5)]
    n = 4
    if not vertical:
        pts = []
        for i in range(n * 2 + 1):
            yy = y - h / 2 + 4 + (h - 8) * i / (n * 2)
            pts += [(x - w / 2 + 4, yy), (x + w / 2 - 4, yy)] if i % 2 == 0 else [(x + w / 2 - 4, yy), (x - w / 2 + 4, yy)]
        o.append(P(pts, c, 1.4))
    else:
        pts = []
        for i in range(n * 2 + 1):
            xx = x - w / 2 + 4 + (w - 8) * i / (n * 2)
            pts += [(xx, y - h / 2 + 4), (xx, y + h / 2 - 4)] if i % 2 == 0 else [(xx, y + h / 2 - 4), (xx, y - h / 2 + 4)]
        o.append(P(pts, c, 1.4))
    return ''.join(o)


# ---- 2.1 potentiometer: worked examples 1 and 2 ----
def f1():
    o = []
    X0, X1, Y0, Y1 = 64, 360, 50, 270
    fx = lin(0, 100, X0, X1); fy = lin(0, 10, Y1, Y0)
    o.append(T(212, 22, 'Worked example 1: 10 kΩ track, 10 V, 10 kΩ load', 14, 'middle', INK, True))
    o.append(axes(X0, X1, Y0, Y1, [0, 25, 50, 75, 100], [0, 2, 4, 6, 8, 10], fx, fy, 'wiper position x (mm)', 'output V' + sub('0') + ' (V)'))
    o.append(P([(fx(0), fy(0)), (fx(100), fy(10))], AC, 2.5))
    o.append(P([(fx(x), fy(10 * (x / 100) / (1 + (x / 100) * (1 - x / 100)))) for x in range(0, 101, 2)], LV, 3))
    o.append(C(fx(50), fy(5), 5, AC)); o.append(C(fx(50), fy(4), 5, LV))
    o.append(L(fx(50), fy(5), fx(50), fy(4), INK, 1.5, '4 3'))
    o.append(Tb(fx(50) - 10, fy(5) - 12, 'ideal 5.00 V', 13, 'end', AC, True))
    o.append(Tb(fx(50) + 10, fy(4) + 20, 'loaded 4.00 V', 13, 'start', LV, True))
    o.append(T(fx(56), fy(4.5) + 4, '1.00 V low', 13, 'start', INK))
    o.append(T(fx(4), fy(8.6), 'error is zero at both ends', 13, 'start', MUT))
    # right: electrogoniometer
    o.append(T(545, 22, 'Worked example 2: electrogoniometer', 14, 'middle', INK, True))
    kx, ky = 540, 150
    o.append(L(kx, ky, kx - 10, 52, INK, 10)); o.append(T(kx - 20, 64, 'thigh', 13, 'end', MUT))
    o.append(L(kx, ky, kx + 98, ky + 18, INK, 10)); o.append(T(kx + 100, ky + 46, 'shank', 13, 'middle', MUT))
    o.append(f'<circle cx="{kx}" cy="{ky}" r="26" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2.5"/>')
    o.append(C(kx, ky, 5, AC))
    o.append(T(kx - 34, ky + 4, 'rotary pot', 13, 'end', AC, True))
    o.append(T(kx - 34, ky + 22, '5 kΩ, 340°', 13, 'end', AC))
    # angle arc from thigh line downwards to shank
    a0 = math.atan2(52 - ky, -10); a1 = math.atan2(18, 98)
    r = 44
    pts = [(kx + r * math.cos(a0 + (a1 - a0) * t / 20), ky + r * math.sin(a0 + (a1 - a0) * t / 20)) for t in range(21)]
    o.append(P(pts, NX, 2)); o.append(T(kx + 44, ky - 30, '90°', 14, 'start', NX, True))
    o.append(T(410, 230, 'supply 5 V, amplifier input 50 kΩ', 13, 'start', INK))
    o.append(T(410, 252, 'ideal 5 × 90/340 = 1.324 V', 13, 'start', AC, True))
    o.append(T(410, 274, 'loaded 1.298 V: reads 88.3°, 1.7° low', 13, 'start', LV, True))
    o.append(T(410, 296, 'track power 5 mW against 0.5 W rating', 13, 'start', MUT))
    return 330, ''.join(o)


FIG[1] = (f1, 'Left: the 10 kΩ potentiometer of worked example 1 feeding a 10 kΩ load gives 4.00 V instead of 5.00 V at mid-stroke, '
              'and is exact at both ends. Right: worked example 2, a rotary pot strapped across the knee; at 90° the 50 kΩ amplifier '
              'pulls the 1.324 V ideal output down to 1.298 V, a reading 1.7° low.',
          'Left: graph of output voltage against wiper position from 0 to 100 millimetres; the straight ideal line reaches 5 volts at '
          '50 millimetres while the loaded curve sags to 4 volts there, meeting the ideal at both ends. Right: a leg with a rotary '
          'potentiometer at the knee bent to 90 degrees, with the ideal output 1.324 volts and the loaded output 1.298 volts, 1.7 '
          'degrees low.')


# ---- 2.2 strain gauge: construction and worked example 2 (cantilever half bridge) ----
def f2():
    o = []
    o.append(T(170, 22, 'Bonded foil gauge', 14, 'middle', INK, True))
    o.append(R(30, 40, 280, 190, PANEL, L2, 8, 1.5))
    o.append(T(170, 222, 'polyimide backing (glued to the part)', 13, 'middle', MUT))
    # serpentine grid
    gx0, gx1, gy0, gy1 = 80, 240, 70, 170
    pts = []
    n = 8
    for i in range(n + 1):
        y = gy0 + (gy1 - gy0) * i / n
        pts += [(gx0, y), (gx1, y)] if i % 2 == 0 else [(gx1, y), (gx0, y)]
    o.append(P(pts, AC, 2.2))
    o.append(R(gx1 + 8, gy0 - 8, 34, 22, ACS, AC, 3, 1.5)); o.append(R(gx1 + 8, gy1 - 14, 34, 22, ACS, AC, 3, 1.5))
    o.append(L(gx1, gy0, gx1 + 8, gy0, AC, 2.2)); o.append(L(gx1, gy1, gx1 + 8, gy1, AC, 2.2))
    o.append(T(gx1 + 25, gy0 + 34, 'solder', 12, 'middle', AC)); o.append(T(gx1 + 25, gy0 + 50, 'tabs', 12, 'middle', AC))
    o.append(arrow(gx0 + 4, 192, gx1 - 4, 192, INK, 1.5, 'm')); o.append(arrow(gx1 - 4, 192, gx0 + 4, 192, INK, 1.5, 'm'))
    o.append(Tb(160, 197, 'gauge length', 13, 'middle', INK))
    o.append(arrow(56, 120, 34, 120, LV, 2, 'l')); o.append(arrow(284, 120, 306, 120, LV, 2, 'l'))
    o.append(T(170, 262, 'strain along the grid lines: ΔR/R = GF·ε', 13, 'middle', LV, True))
    o.append(T(170, 284, '120 Ω, GF 2.0, 500 µε → 0.12 Ω (0.1 %)', 13, 'middle', INK))
    o.append(T(170, 306, 'silicon, GF 100 → 6.0 Ω (5 %)', 13, 'middle', MUT))
    # right: cantilever
    o.append(T(530, 22, 'Worked example 2: cantilever half bridge', 14, 'middle', INK, True))
    o.append(R(360, 60, 26, 150, PANEL, INK, 2, 2))
    for yy in range(66, 206, 14): o.append(L(360, yy, 352, yy + 8, MUT, 1.2))
    # bent beam: root at x=386,y=130, tip at x=660, deflected down 26 px
    bx0, bx1, by = 386, 660, 128
    def yb(x): s = (x - bx0) / (bx1 - bx0); return by + 30 * s * s * (3 - s) / 2
    o.append(P([(bx0 + i * (bx1 - bx0) / 30, yb(bx0 + i * (bx1 - bx0) / 30) - 6) for i in range(31)], INK, 2))
    o.append(P([(bx0 + i * (bx1 - bx0) / 30, yb(bx0 + i * (bx1 - bx0) / 30) + 6) for i in range(31)], INK, 2))
    o.append(L(bx0, by, bx1, by, L2, 1, '5 4'))
    o.append(arrow(bx1, 90, bx1, yb(bx1) - 8, NX, 2.5, 'x')); o.append(T(bx1 - 6, 84, 'δ = 1.0 mm', 13, 'end', NX, True))
    o.append(gauge(420, by - 13, 34, 10)); o.append(gauge(420, by + 13, 34, 10, LV))
    o.append(T(440, by - 26, 'gauge 1: +600 µε (tension)', 13, 'start', AC, True))
    o.append(T(440, by + 58, 'gauge 2: −600 µε (compression)', 13, 'start', LV, True))
    o.append(brace(bx0, bx1, 200, MUT)); o.append(T((bx0 + bx1) / 2, 226, 'L = 50 mm, t = 1.0 mm', 13, 'middle', MUT))
    o.append(T(370, 262, 'ε = 3tδ/(2L²) = 3 × 1 × 1/(2 × 2500) = 600 µε', 13, 'start', INK))
    o.append(T(370, 284, 'half bridge: V' + sub('0') + ' = (V' + sub('s') + '/2)·GF·ε = 2.5 × 2 × 600 µε', 13, 'start', INK))
    o.append(T(370, 306, '= 3.0 mV at 5 V, i.e. 3.0 mV/mm', 13, 'start', AC, True))
    return 320, ''.join(o)


FIG[2] = (f2, 'Left: a bonded foil gauge, a serpentine grid on a backing that is glued to the part, sensitive along its grid lines '
              '(worked example 1: 0.12 Ω for a metal gauge, 6.0 Ω for silicon at 500 µε). Right: worked example 2, a 50 mm cantilever '
              'with gauges top and bottom; a 1.0 mm tip deflection gives ±600 µε and 3.0 mV from a half bridge at 5 V.',
          'Left: a strain gauge with a zigzag foil grid on a backing, solder tabs and the gauge length marked. Right: a cantilever '
          'clamped at its left end and deflected 1 millimetre at its tip, with a gauge on top in tension at plus 600 microstrain and '
          'a gauge underneath in compression at minus 600 microstrain, giving 3.0 millivolts from a half bridge.')


# ---- 2.3 load cell column and torque shaft ----
def f3():
    o = []
    o.append(T(170, 22, 'Worked example 1: column load cell', 14, 'middle', INK, True))
    cx = 120
    o.append(R(cx - 36, 70, 72, 190, PANEL, INK, 4, 2))
    o.append(arrow(cx, 34, cx, 66, NX, 3, 'x')); o.append(T(cx + 10, 48, 'F = 10 kN', 13, 'start', NX, True))
    o.append(L(cx - 60, 262, cx + 60, 262, INK, 3))
    o.append(gauge(cx - 14, 130, 14, 36, AC, True)); o.append(T(cx - 14, 104, '1', 12, 'middle', AC, True))
    o.append(gauge(cx + 14, 130, 14, 36, AC, True)); o.append(T(cx + 14, 104, '3', 12, 'middle', AC, True))
    o.append(gauge(cx - 14, 200, 22, 12, LV)); o.append(T(cx - 14, 222, '2', 12, 'middle', LV, True))
    o.append(gauge(cx + 14, 200, 22, 12, LV)); o.append(T(cx + 14, 222, '4', 12, 'middle', LV, True))
    o.append(T(cx + 48, 120, 'axial gauges', 13, 'start', AC, True))
    o.append(T(cx + 48, 138, '−159 µε, ΔR 0.038 Ω', 13, 'start', AC))
    o.append(T(cx + 48, 192, 'transverse gauges', 13, 'start', LV, True))
    o.append(T(cx + 48, 210, '+47.7 µε, ΔR 0.011 Ω', 13, 'start', LV))
    o.append(T(30, 292, 'd = 20 mm steel: σ = 31.8 MPa', 13, 'start', INK))
    o.append(T(30, 314, 'V' + sub('0') + ' = V' + sub('s') + '·GF·ε(1 + ν)/2 = 1.03 mV at 5 V', 13, 'start', AC, True))
    # right: torque shaft
    o.append(T(530, 22, 'Worked example 2: torque shaft', 14, 'middle', INK, True))
    sx0, sx1, sy, r = 380, 680, 150, 34
    o.append(R(sx0, sy - r, sx1 - sx0, 2 * r, PANEL, INK, 4, 2))
    o.append(f'<ellipse cx="{sx0}" cy="{sy}" rx="10" ry="{r}" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    # torque arrows (curved) at ends
    for x, sgn in ((sx0 + 26, 1), (sx1 - 26, -1)):
        pts = [(x + 12 * math.sin(t / 10 * math.pi) * sgn * 0.6, sy - (r + 10) * math.cos(t / 10 * math.pi)) for t in range(0, 9)]
        o.append(P(pts, NX, 2.5))
    o.append(T(sx0 + 4, sy - r - 18, 'T = 100 N·m', 13, 'start', NX, True))
    # +-45 gauges
    gx = 530
    o.append(f'<g transform="rotate(-45 {gx - 22} {sy})">' + gauge(gx - 22, sy, 30, 12) + '</g>')
    o.append(f'<g transform="rotate(45 {gx + 22} {sy})">' + gauge(gx + 22, sy, 30, 12, LV) + '</g>')
    o.append(T(gx - 30, sy + r + 24, '+45°: +204 µε', 13, 'end', AC, True))
    o.append(T(gx + 30, sy + r + 24, '−45°: −204 µε', 13, 'start', LV, True))
    o.append(T(390, 240, 'd = 25 mm, G = 80 GPa: τ = 16T/(πd³) = 32.6 MPa', 13, 'start', INK))
    o.append(T(390, 262, 'ε' + sub('45') + ' = τ/(2G) = 204 µε', 13, 'start', INK))
    o.append(T(390, 292, 'full bridge: V' + sub('0') + ' = V' + sub('s') + '·GF·ε = 4.07 mV at 10 V', 13, 'start', AC, True))
    o.append(T(390, 314, 'at 1500 rev/min: P = 2πNT/60 = 15.7 kW', 13, 'start', MUT))
    return 330, ''.join(o)


FIG[3] = (f3, 'Left: worked example 1, a 20 mm steel column under 10 kN with two axial and two transverse gauges; the strains are '
              '159 µε and 47.7 µε, and the full bridge gives 1.03 mV at 5 V. Right: worked example 2, gauges at ±45° on a 25 mm shaft '
              'under 100 N·m read ±204 µε and 4.07 mV at 10 V.',
          'Left: a vertical steel column loaded by 10 kilonewtons with gauges 1 and 3 along the axis and gauges 2 and 4 across it, '
          'labelled with their strains and the 1.03 millivolt bridge output. Right: a shaft under a torque of 100 newton metres with '
          'two gauges at plus and minus 45 degrees, reading plus and minus 204 microstrain and 4.07 millivolts at 10 volts.')


# ---- 2.4 RTD and thermistor: worked examples 1 and 2 ----
def f4():
    o = []
    X0, X1, Y0, Y1 = 70, 320, 54, 260
    fx = lin(0, 100, X0, X1); fy = lin(90, 140, Y1, Y0)
    o.append(T(195, 22, 'Pt100: R = 100(1 + 0.00385T)', 14, 'middle', INK, True))
    o.append(axes(X0, X1, Y0, Y1, [0, 25, 50, 75, 100], [90, 100, 110, 120, 130, 140], fx, fy, 'temperature (°C)', 'R (Ω)'))
    o.append(P([(fx(0), fy(100)), (fx(100), fy(138.5))], AC, 3))
    o.append(C(fx(50), fy(119.25), 5, AC)); o.append(L(fx(50), fy(119.25), fx(50), Y1, AC, 1.2, '4 3'))
    o.append(Tb(fx(50) - 8, fy(119.25) - 12, '119.25 Ω at 50 °C', 13, 'end', AC, True))
    o.append(T(fx(98), fy(97), 'slope 0.385 Ω/°C', 13, 'end', INK))
    o.append(T(fx(98), fy(93), 'nearly straight', 13, 'end', MUT))
    X0, X1 = 410, 680
    gx = lin(0, 60, X0, X1); gy = lin(0, 32, Y1, Y0)
    o.append(T(545, 22, 'NTC: 10 kΩ at 25 °C, β = 3500 K', 14, 'middle', INK, True))
    o.append(axes(X0, X1, Y0, Y1, [0, 15, 25, 37, 45, 60], [0, 10, 20, 30], gx, gy, 'temperature (°C)', 'R (kΩ)'))
    o.append(P([(gx(t), gy(10 * math.exp(3500 * (1 / (t + 273.15) - 1 / 298.15)))) for t in range(0, 61, 2)], LV, 3))
    for t, s, dx, anc in ((0, '29.3 kΩ at 0 °C', 10, 'start'), (25, '10.0 kΩ at 25 °C', 10, 'start'), (37, '6.35 kΩ at 37 °C', 8, 'start')):
        v = 10 * math.exp(3500 * (1 / (t + 273.15) - 1 / 298.15))
        o.append(C(gx(t), gy(v), 5, LV)); o.append(Tb(gx(t) + dx, gy(v) + (-10 if t == 0 else 22) - (8 if t == 25 else 0), s, 13, anc, LV, True))
    o.append(T(gx(60), gy(31), 'probe divider, 3.3 V:', 13, 'end', INK, True))
    o.append(T(gx(60), gy(28.4), '35 °C → 1.961 V', 13, 'end', INK))
    o.append(T(gx(60), gy(25.8), '37 °C → 2.018 V', 13, 'end', INK))
    o.append(T(gx(60), gy(23.2), '42 °C → 2.156 V', 13, 'end', INK))
    return 310, ''.join(o)


FIG[4] = (f4, 'Left: the Pt100 of worked example 1 rises 0.385 Ω per degree, 119.25 Ω at 50 °C. Right: the 10 kΩ, β = 3500 K '
              'thermistor falls from 29.3 kΩ at 0 °C to 6.35 kΩ at 37 °C; in the clinical divider of worked example 2 it gives '
              '1.961, 2.018 and 2.156 V at 35, 37 and 42 °C.',
          'Left: a straight line of platinum resistance against temperature from 100 ohms at 0 degrees to 138.5 ohms at 100 degrees, '
          'with 119.25 ohms marked at 50 degrees. Right: a falling thermistor curve from 29.3 kilohms at 0 degrees through 10 '
          'kilohms at 25 degrees to 6.35 kilohms at 37 degrees, with divider outputs listed for 35, 37 and 42 degrees.')


# ---- 2.5 constant-temperature anemometer and King's law ----
def f5():
    o = []
    o.append(T(180, 22, 'Constant-temperature bridge', 14, 'middle', INK, True))
    # diamond bridge: top (180,60) left (100,140) right (260,140) bottom (180,220)
    tp, lf, rt, bt = (180, 64), (100, 144), (260, 144), (180, 224)
    o.append(P([tp, lf], INK, 2)); o.append(P([lf, bt], INK, 2)); o.append(P([bt, rt], INK, 2))
    o.append(P([rt, tp], AC, 4)); o.append(T(232, 92, 'hot wire R' + sub('w'), 13, 'start', AC, True))
    o.append(T(126, 92, 'R' + sub('1'), 13, 'end', INK)); o.append(T(126, 200, 'R' + sub('2'), 13, 'end', INK))
    o.append(T(232, 200, 'R' + sub('3'), 13, 'start', INK))
    for p in (tp, lf, rt, bt): o.append(C(p[0], p[1], 4, INK))
    # amplifier triangle at right
    ax = 300
    o.append(P([(ax, 120), (ax, 196), (ax + 54, 158), (ax, 120)], NX, 2, fill='var(--next-soft)'))
    o.append(T(ax + 16, 162, 'amp', 12, 'middle', NX, True))
    o.append(P([lf, (100, 250), (290, 250), (290, 182), (ax, 182)], INK, 1.5))
    o.append(P([rt, (280, 144), (280, 134), (ax, 134)], INK, 1.5))
    o.append(P([(ax + 54, 158), (340, 158), (340, 40), (180, 40), tp], NX, 2.2))
    o.append(arrow(340, 110, 340, 60, NX, 2, 'x'))
    o.append(T(348, 92, 'output', 13, 'start', NX, True)); o.append(T(348, 110, 'E', 13, 'start', NX, True))
    o.append(T(180, 268, 'bottom corner earthed', 12, 'middle', MUT))
    for yy in (70, 98, 126):
        o.append(arrow(20, yy + 140, 70, yy + 140, LV, 2, 'l'))
    o.append(T(20, 196, 'air flow', 13, 'start', LV, True))
    o.append(T(14, 302, 'flow cools R' + sub('w') + ' → bridge unbalances → amp raises E', 13, 'start', LV, True))
    # right: E^2 vs sqrt(u)
    X0, X1, Y0, Y1 = 430, 680, 54, 260
    fx = lin(0, 4.5, X0, X1); fy = lin(0, 14, Y1, Y0)
    o.append(T(555, 22, 'Worked example: E² = 4 + 2√u', 14, 'middle', INK, True))
    o.append(axes(X0, X1, Y0, Y1, [0, 1, 2, 3, 4], [0, 4, 8, 12], fx, fy, '√u ((m/s)' + sup('0.5') + ')', 'E² (V²)'))
    o.append(P([(fx(0), fy(4)), (fx(4.5), fy(13))], AC, 3))
    o.append(C(fx(3), fy(10), 5, AC)); o.append(Tb(fx(3) - 30, fy(10) + 28, '9 m/s → 3.16 V', 13, 'start', AC, True))
    o.append(C(fx(3.99), fy(11.97), 5, LV)); o.append(Tb(fx(3.99) - 10, fy(11.97) - 14, 'E = 3.46 V: u = 15.9 m/s', 13, 'end', LV, True))
    o.append(T(fx(0) + 10, fy(4) + 22, 'A = 4 V² at zero flow', 13, 'start', MUT))
    o.append(T(fx(4.4), fy(1.5), 'slope B = 2', 13, 'end', INK))
    return 320, ''.join(o)


FIG[5] = (f5, 'Left: flow cools the heated wire, the bridge unbalances, and the amplifier raises the bridge voltage E until the wire '
              'is back at its set resistance; E is the reading. Right: the worked example’s King’s law is a straight line of E² against '
              '√u: 3.16 V at 9 m/s, and 3.46 V means 15.9 m/s.',
          'Left: a Wheatstone bridge with the hot wire in one arm and an amplifier whose output feeds the top of the bridge, with flow '
          'arrows cooling the wire. Right: a straight line of E squared against the square root of speed starting at 4 volts squared, '
          'with points at 9 metres per second giving 3.16 volts and at 15.9 metres per second giving 3.46 volts.')


# ---- 2.6 LDR: worked example ----
def f6():
    o = []
    X0, X1, Y0, Y1 = 80, 370, 54, 260
    fx = lambda e: X0 + (math.log10(e) - 1) / 2 * (X1 - X0)
    fy = lambda r: Y1 - (math.log10(r) - 3) / 2 * (Y1 - Y0)
    o.append(T(225, 22, 'R = 10⁶/E on log scales', 14, 'middle', INK, True))
    o.append(L(X0, Y1, X1, Y1, L2, 1.5)); o.append(L(X0, Y0, X0, Y1, L2, 1.5))
    for e, s in ((10, '10'), (100, '100'), (1000, '1000')):
        o.append(L(fx(e), Y1, fx(e), Y1 + 5, L2, 1.5)); o.append(T(fx(e), Y1 + 20, s, 13, 'middle', MUT))
    for r, s in ((1e3, '1 k'), (1e4, '10 k'), (1e5, '100 k')):
        o.append(L(X0 - 5, fy(r), X0, fy(r), L2, 1.5)); o.append(L(X0, fy(r), X1, fy(r), LN, 1)); o.append(T(X0 - 9, fy(r) + 4.5, s, 13, 'end', MUT))
    o.append(T((X0 + X1) / 2, Y1 + 40, 'illuminance E (lux)', 14, 'middle', MUT)); o.append(T(X0, Y0 - 12, 'R (Ω)', 14, 'start', MUT))
    o.append(P([(fx(10), fy(1e5)), (fx(1000), fy(1e3))], AC, 3))
    for e, s in ((100, '10 kΩ at 100 lux'), (500, '2 kΩ at 500 lux'), (1000, '1 kΩ at 1000 lux')):
        o.append(C(fx(e), fy(1e6 / e), 5, AC))
    o.append(Tb(fx(100) + 10, fy(1e4) - 10, '10 kΩ at 100 lux', 13, 'start', AC, True))
    o.append(Tb(fx(500) - 10, fy(2e3) - 12, '2 kΩ at 500 lux', 13, 'end', AC, True))
    o.append(Tb(fx(1000) + 8, fy(1e3) - 14, '1 kΩ', 13, 'start', AC, True))
    o.append(T(fx(12), fy(1.6e3), 'slope −1: γ = 1', 13, 'start', INK))
    # right: divider
    o.append(T(560, 22, 'Divider, output across 10 kΩ', 14, 'middle', INK, True))
    x = 540
    o.append(L(x, 50, x, 70, INK, 2)); o.append(T(x, 46, '+5 V', 13, 'middle', INK, True))
    o.append(R(x - 16, 70, 32, 70, LVS, LV, 4, 2)); o.append(T(x - 24, 100, 'LDR', 13, 'end', LV, True))
    for k in range(3): o.append(arrow(x + 62 - k * 4, 70 + k * 22, x + 22, 84 + k * 22, NX, 1.6, 'x'))
    o.append(T(x + 66, 72, 'light', 13, 'start', NX))
    o.append(L(x, 140, x, 166, INK, 2)); o.append(C(x, 166, 4, INK))
    o.append(res_v(x, 166, 246)); o.append(T(x - 18, 210, '10 kΩ', 13, 'end', INK))
    o.append(L(x, 246, x, 268, INK, 2)); o.append(L(x - 16, 268, x + 16, 268, INK, 2.5)); o.append(T(x, 290, '0 V', 13, 'middle', MUT))
    o.append(L(x, 166, 630, 166, INK, 2)); o.append(C(630, 166, 4, AC)); o.append(T(640, 160, 'V' + sub('out'), 14, 'start', AC, True))
    o.append(T(600, 206, '100 lux: 2.50 V', 13, 'start', AC, True))
    o.append(T(600, 228, '500 lux: 4.17 V', 13, 'start', AC, True))
    o.append(T(600, 250, 'brighter → higher', 13, 'start', MUT))
    return 310, ''.join(o)


FIG[6] = (f6, 'Left: on log scales the worked example’s law R = 10⁶/E is a straight line of slope −1: 10 kΩ at 100 lux, 2 kΩ at 500 '
              'lux, 1 kΩ at 1000 lux. Right: with the output taken across the 10 kΩ resistor, the divider gives 2.50 V at 100 lux and '
              '4.17 V at 500 lux.',
          'Left: a log-log graph of LDR resistance against illuminance, a straight falling line through 10 kilohms at 100 lux, 2 '
          'kilohms at 500 lux and 1 kilohm at 1000 lux. Right: a divider with the LDR from 5 volts to the output node and a 10 kilohm '
          'resistor to ground, giving 2.50 volts at 100 lux and 4.17 volts at 500 lux.')


# ---- 2.7 thermocouple with cold-junction compensation: worked example ----
def f7():
    o = []
    o.append(T(350, 22, 'Type K thermocouple with an isothermal block', 14, 'middle', INK, True))
    # hot junction
    hx, hy = 70, 150
    o.append(f'<circle cx="{hx}" cy="{hy}" r="34" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2"/>')
    o.append(C(hx, hy, 6, LV))
    o.append(T(hx, hy + 56, 'hot junction', 13, 'middle', LV, True)); o.append(T(hx, hy + 74, 'T' + sub('h') + ' = ?', 13, 'middle', LV, True))
    # two wires
    o.append(P([(hx, hy), (130, 110), (300, 110)], AC, 3)); o.append(T(210, 100, 'chromel (+)', 13, 'middle', AC, True))
    o.append(P([(hx, hy), (130, 190), (300, 190)], NX, 3)); o.append(T(210, 214, 'alumel (−)', 13, 'middle', NX, True))
    # isothermal block
    o.append(R(300, 80, 110, 140, PANEL, INK, 6, 2))
    o.append(T(355, 72, 'isothermal block', 13, 'middle', INK, True))
    o.append(C(312, 110, 5, INK)); o.append(C(312, 190, 5, INK))
    o.append(T(355, 132, 'T' + sub('c') + ' = 30 °C', 13, 'middle', INK, True))
    o.append(R(336, 144, 38, 16, ACS, AC, 3, 1.5)); o.append(T(355, 176, 'sensor', 12, 'middle', AC))
    # copper leads to meter
    o.append(L(312, 110, 500, 110, MUT, 2)); o.append(L(312, 190, 500, 190, MUT, 2))
    o.append(T(450, 100, 'copper', 13, 'middle', MUT)); o.append(T(450, 206, 'copper', 13, 'middle', MUT))
    o.append(boxt(500, 90, 120, 120, ['meter', '11.00 mV', '= E(T' + sub('h') + ', 30)'], PANEL, INK, 13, True))
    # sum
    o.append(arrow(355, 222, 355, 262, AC, 1.8))
    o.append(T(30, 290, 'sensor → E(30 °C, 0 °C) = 1.20 mV;  11.00 + 1.20 = 12.20 mV = E(T' + sub('h') + ', 0)', 13, 'start', AC, True))
    o.append(T(30, 314, 'K table: 12.20 mV → T' + sub('h') + ' ≈ 300 °C;  average S = 12.20 mV/300 °C ≈ 40.7 µV/°C', 13, 'start', INK))
    o.append(T(640, 240, 'without the 1.20 mV:', 12, 'end', MUT)); o.append(T(640, 256, '11.00 mV reads ≈ 271 °C', 12, 'end', MUT))
    return 330, ''.join(o)


FIG[7] = (f7, 'The worked example’s circuit. The chromel–copper and alumel–copper junctions sit on one block at 30 °C, so they act as a '
              'single cold junction (law of intermediate metals). The block sensor supplies E(30 °C, 0 °C) = 1.20 mV, which is added to '
              'the measured 11.00 mV: 12.20 mV, about 300 °C.',
          'A type K thermocouple: the hot junction at the left joins chromel and alumel wires that end on two terminals of an '
          'isothermal block at 30 degrees with a temperature sensor; copper leads run to a meter reading 11.00 millivolts. Below, '
          'the sum 11.00 plus 1.20 equals 12.20 millivolts, which the table turns into about 300 degrees.')


spec = make_spec(FIG)
