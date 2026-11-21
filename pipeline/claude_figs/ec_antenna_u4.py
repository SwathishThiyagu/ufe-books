"""Claude's hand-drawn figures for ec-antenna-u4 (Microwave components, devices and measurements), one per chapter.
Every value comes from that chapter's own worked example; curves are computed, not sketched. Colours are the shell's CSS variables."""
import os, sys, math, cmath
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
SUB = lambda s: f'<tspan font-size="11" baseline-shift="sub">{s}</tspan>'
SUP = lambda s: f'<tspan font-size="11" baseline-shift="super">{s}</tspan>'


def node(x, y, name, fill=PANEL, stroke=AC, r=22):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{fill};stroke:{stroke};stroke-width:2"/>' + T(x, y + 5, name, 15, bold=True)


# ---- 4.1 signal-flow graph of worked example 1 ----
def f1():
    o = []
    o.append(R(150, 40, 420, 230, 'none', L2, 10, 1.5, '6 5'))
    o.append(T(360, 62, 'two-port, Z₀ = 50 Ω, 10 GHz', 13, fill=MUT))
    o.append(L(150, 40, 150, 270, L2, 2.5)); o.append(L(570, 40, 570, 270, L2, 2.5))
    o.append(T(150, 292, 'port 1 plane', 13, fill=MUT)); o.append(T(530, 292, 'port 2 plane', 13, fill=MUT))
    a1, b2, b1, a2 = (110, 110), (610, 110), (110, 220), (610, 220)
    o.append(node(*a1, 'a' + SUB('1'))); o.append(node(*b2, 'b' + SUB('2'), stroke=LV))
    o.append(node(*b1, 'b' + SUB('1'), stroke=LV)); o.append(node(*a2, 'a' + SUB('2')))
    o.append(L(134, 110, 584, 110, AC, 3, arrow='n'))
    o.append(Tb(360, 100, 'S' + SUB('21') + ' = 0.9∠−30°', 15, fill=AC, bold=True))
    o.append(L(110, 134, 110, 194, AC, 2.5, arrow='n'))
    o.append(T(96, 168, 'S' + SUB('11') + ' = 0.2', 14, 'end'))
    o.append(L(610, 196, 610, 136, AC, 2.5, arrow='n'))
    o.append(T(626, 170, 'S' + SUB('22') + ' = 0.1', 14, 'start'))
    o.append(L(586, 220, 136, 220, L2, 2, '7 6', 'm'))
    o.append(Tb(360, 212, 'S' + SUB('12') + ' = 0: no reverse path', 14, fill=MUT))
    o.append(L(30, 110, 84, 110, INK, 2, arrow='n')); o.append(T(30, 96, 'in', 13, 'start', MUT))
    o.append(L(84, 220, 30, 220, LV, 2, arrow='l')); o.append(T(30, 244, 'reflected', 13, 'start', MUT))
    o.append(L(636, 110, 690, 110, LV, 2, arrow='l')); o.append(T(690, 96, 'to load', 13, 'end', MUT))
    o.append(T(610, 262, 'a' + SUB('2') + ' = 0 (matched)', 13, 'middle', MUT))
    o.append(T(360, 330, 'RL = −20 log 0.2 = 13.98 dB  ·  IL = −20 log 0.9 = 0.92 dB', 14))
    o.append(T(360, 354, 'VSWR = 1.2/0.8 = 1.5  ·  reverse isolation = ∞', 14))
    return 376, ''.join(o)


FIG[1] = (f1, 'Each S-parameter is a branch from an incoming wave to an outgoing wave. With port 2 matched only S₁₁ and S₂₁ act, giving the 13.98 dB return loss and 0.92 dB insertion loss of the worked example.',
          'Signal-flow graph with nodes a1, b1 at port 1 and b2, a2 at port 2. Branches: S21 = 0.9 at minus 30 degrees from a1 to b2, S11 = 0.2 from a1 to b1, S22 = 0.1 from a2 to b2, and a dashed S12 = 0. Results: return loss 13.98 dB, insertion loss 0.92 dB, VSWR 1.5.')


# ---- 4.2 magic tee, worked example 2: 8 W and 2 W in phase ----
def f2():
    o = []
    cx, cy = 360, 190
    # collinear guide
    o.append(R(60, cy - 28, 600, 56, PANEL, AC, 4))
    # E-arm (up) and H-arm (down)
    o.append(R(cx - 46, 40, 92, cy - 28 - 40 + 2, PANEL, LV, 4))
    o.append(R(cx - 22, cy + 26, 44, 120, PANEL, NX, 4))
    o.append(R(cx - 46, cy - 28, 92, 56, PANEL, 'none', 0))
    o.append(T(cx, cy + 5, 'junction', 13, fill=MUT))
    o.append(T(cx + 60, 70, 'port 4: E-arm', 14, 'start', LV, True))
    o.append(T(cx + 60, 90, '(branch on broad wall)', 13, 'start', MUT))
    o.append(T(cx + 34, cy + 120, 'port 3: H-arm', 14, 'start', NX, True))
    o.append(T(cx + 34, cy + 140, '(branch on narrow wall)', 13, 'start', MUT))
    # inputs
    o.append(L(20, cy, 110, cy, AC, 3, arrow='n')); o.append(T(60, cy - 40, 'port 1: 8 W in', 14, bold=True))
    o.append(T(60, cy + 50, 'a' + SUB('1') + ' = √8 = 2.828', 13, fill=MUT))
    o.append(L(700, cy, 610, cy, AC, 3, arrow='n')); o.append(T(660, cy - 40, 'port 2: 2 W in', 14, bold=True))
    o.append(T(660, cy + 50, 'a' + SUB('2') + ' = √2 = 1.414', 13, fill=MUT))
    # outputs
    o.append(L(cx, 120, cx, 26, LV, 3, arrow='l'))
    o.append(Tb(cx - 60, 30, 'P' + SUB('4') + ' = 1 W', 14, 'end', LV, True))
    o.append(T(cx - 60, 52, '(a₁ − a₂)/√2 = 1.0', 13, 'end', MUT))
    o.append(L(cx, cy + 60, cx, cy + 172, NX, 3, arrow='x'))
    o.append(Tb(cx - 36, cy + 120, 'P' + SUB('3') + ' = 9 W', 14, 'end', NX, True))
    o.append(T(cx - 36, cy + 140, '(a₁ + a₂)/√2 = 3.0', 13, 'end', MUT))
    o.append(T(360, 400, 'in phase: sum (9 W) at the H-arm, difference (1 W) at the E-arm, nothing reflected', 13))
    return 416, ''.join(o)


FIG[2] = (f2, 'The magic tee of worked example 2. The 8 W and 2 W in-phase waves add at the H-arm, giving 9 W, and subtract at the E-arm, giving 1 W; ports 1 and 2 reflect nothing.',
          'Magic tee with collinear ports 1 and 2 left and right, E-arm port 4 above, H-arm port 3 below. Inputs 8 W at port 1 and 2 W at port 2 in phase. Outputs 9 W at the H-arm, (a1 + a2)/root 2 = 3.0, and 1 W at the E-arm, (a1 minus a2)/root 2 = 1.0.')


# ---- 4.3 rat-race to scale (1.5 lambda_g = 360 degrees) ----
def f3():
    o = []
    cx, cy, r = 250, 215, 122
    ang = {1: 150, 2: 90, 3: -90, 4: 210}  # arcs: 1-2 60 deg (lg/4), 2-3 180 deg (3lg/4), 3-4 60, 4-1 60
    pt = lambda a, rr=r: (cx + rr * math.cos(math.radians(a)), cy - rr * math.sin(math.radians(a)))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:{AC};stroke-width:5"/>')
    # the 3lg/4 arc highlighted: from 90 down the right side to -90
    p0, p1 = pt(90), pt(-90)
    o.append(f'<path d="M{p0[0]:.1f},{p0[1]:.1f} A{r},{r} 0 0,1 {p1[0]:.1f},{p1[1]:.1f}" style="fill:none;stroke:{LV};stroke-width:5"/>')
    for k, a in ang.items():
        x, y = pt(a); x2, y2 = pt(a, r + 46)
        o.append(L(x, y, x2, y2, INK, 4))
        o.append(C(x, y, 6, INK))
        lx, ly = pt(a, r + 66)
        o.append(T(lx, ly + 5, f'port {k}', 14, 'middle', INK, True))
    for a, lab in ((120, 'λg/4'), (180, 'λg/4'), (240, 'λg/4')):
        x, y = pt(a, r - 26); o.append(T(x, y + 5, lab, 13, fill=MUT))
    x, y = pt(0, r - 40); o.append(T(x, y + 5, '3λg/4', 14, fill=LV, bold=True))
    o.append(T(cx, cy - 8, 'circumference', 13, fill=MUT)); o.append(T(cx, cy + 12, '1.5λg = 60.2 mm', 13, fill=MUT))
    o.append(T(cx, cy + 32, '(3 GHz, alumina)', 13, fill=MUT))
    # table on the right
    x0 = 470
    o.append(T(x0, 50, '10 mW into port 1 (sum port)', 14, 'start', INK, True))
    rows = [('to port 2:', 'λg/4 and 5λg/4', 'add, 5 mW'), ('to port 4:', 'λg/4 and 5λg/4', 'add, 5 mW'), ('to port 3:', 'λg/2 and λg', 'cancel, 0')]
    for i, (a, b, c) in enumerate(rows):
        y = 82 + i * 50
        o.append(T(x0, y, a, 14, 'start')); o.append(T(x0 + 80, y, b, 13, 'start', MUT))
        o.append(T(x0 + 80, y + 20, c, 14, 'start', LV if i == 2 else AC, True))
    o.append(T(x0, 250, 'ports 2 and 4 in phase', 14, 'start'))
    o.append(T(x0, 280, 'Fed at port 3 instead:', 14, 'start', INK, True))
    o.append(T(x0, 302, '2 and 4 get 5 mW each,', 13, 'start'))
    o.append(T(x0, 322, '180° apart; port 1 gets 0', 13, 'start'))
    return 440, ''.join(o)


FIG[3] = (f3, 'The rat-race drawn to scale: each λg/4 arc is 60° of the ring and the 3λg/4 arc is 180°. From the sum port 1 the two ways round to port 3 differ by λg/2 and cancel, while the paths to ports 2 and 4 differ by λg and add.',
          'Ring with four ports: arcs port 1 to 2 a quarter guide wavelength, 2 to 3 three quarters, 3 to 4 and 4 to 1 a quarter each; circumference 1.5 guide wavelengths, 60.2 mm. Table: 10 mW into port 1 gives 5 mW at ports 2 and 4 in phase and 0 at port 3; fed at port 3, ports 2 and 4 get 5 mW each 180 degrees apart.')


# ---- 4.4 Wilkinson, worked example 2 ----
def f4():
    o = []
    # input line
    o.append(L(40, 190, 170, 190, AC, 4))
    o.append(T(60, 176, 'port 1', 14, 'start', INK, True)); o.append(T(60, 214, '50 Ω', 13, 'start', MUT))
    # branches
    o.append(P([(170, 190), (230, 90), (470, 90)], AC, 4)); o.append(P([(170, 190), (230, 290), (470, 290)], AC, 4))
    o.append(Tb(345, 78, '70.7 Ω, λg/4 = 21.65 mm', 13, fill=AC))
    o.append(Tb(345, 318, '70.7 Ω, λg/4 = 21.65 mm', 13, fill=AC))
    o.append(L(470, 90, 660, 90, AC, 4)); o.append(L(470, 290, 660, 290, AC, 4))
    o.append(T(680, 80, 'port 2', 14, 'end', INK, True)); o.append(T(680, 280, 'port 3', 14, 'end', INK, True))
    # resistor zigzag between output ends
    zz = [(470, 90), (470, 140)] + [(470 + (14 if i % 2 else -14), 148 + i * 10) for i in range(9)] + [(470, 240), (470, 290)]
    o.append(P(zz, NX, 3))
    o.append(T(492, 184, 'R = 100 Ω', 14, 'start', NX, True))
    # example 2 flows: fed at port 2
    o.append(L(690, 112, 600, 112, LV, 3, arrow='l')); o.append(T(700, 136, '10 mW in', 14, 'end', LV, True))
    o.append(L(300, 112, 220, 150, LV, 2.5, '7 5', 'l'))
    o.append(T(40, 250, '5 mW reaches', 14, 'start', LV, True)); o.append(T(40, 270, 'port 1', 14, 'start', LV, True))
    o.append(T(492, 206, '5 mW heats R', 14, 'start', NX, True))
    o.append(T(560, 320, '0 mW at port 3', 14, 'start', MUT, True))
    o.append(T(360, 370, 'design at 2 GHz, 50 Ω, εeff = 3.0', 13, fill=MUT))
    return 390, ''.join(o)


FIG[4] = (f4, 'The 2 GHz Wilkinson of worked example 2: two 70.7 Ω quarter-wave lines and a 100 Ω resistor. Fed at output port 2, half the power reaches port 1, half heats the resistor, and port 3 gets none.',
          'Wilkinson divider: port 1 50 ohm line splitting into two 70.7 ohm quarter-wave lines of 21.65 mm to ports 2 and 3, with a 100 ohm resistor across the output ends. 10 mW fed into port 2: 5 mW reaches port 1, 5 mW heats the resistor, 0 at port 3.')


# ---- 4.5 circulator duplexer, worked example 2 ----
def f5():
    o = []
    cx, cy, r = 330, 215, 58
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:{PANEL};stroke:{AC};stroke-width:3"/>')
    o.append(f'<path d="M{cx - 28},{cy - 12} A30,30 0 1,1 {cx - 20},{cy + 22}" style="fill:none;stroke:{AC};stroke-width:2.5" marker-end="url(#ar-UID-n)"/>')
    pt = lambda a, rr: (cx + rr * math.cos(math.radians(a)), cy - rr * math.sin(math.radians(a)))
    for a in (180, 60, -60):
        x1, y1 = pt(a, r); x2, y2 = pt(a, r + 80)
        o.append(L(x1, y1, x2, y2, INK, 5))
    x1, y1 = pt(180, r + 80)
    o.append(R(x1 - 170, cy - 30, 170, 60, PANEL, AC, 8)); o.append(T(x1 - 85, cy - 4, 'transmitter (1)', 14, bold=True)); o.append(T(x1 - 85, cy + 16, '60 dBm (1 kW)', 13))
    x2, y2 = pt(60, r + 80); o.append(R(x2, y2 - 40, 190, 56, PANEL, LV, 8)); o.append(T(x2 + 95, y2 - 16, 'antenna (2)', 14, bold=True)); o.append(T(x2 + 95, y2 + 4, 'VSWR 1.5, |Γ| = 0.2', 13))
    x3, y3 = pt(-60, r + 80); o.append(R(x3, y3 - 16, 190, 56, PANEL, NX, 8)); o.append(T(x3 + 95, y3 + 8, 'receiver (3)', 14, bold=True)); o.append(T(x3 + 95, y3 + 28, 'needs a limiter', 13))
    o.append(T(cx, cy + 5, 'rotation', 13, fill=MUT))
    o.append(Tb(cx + 22, 140, '59.5 dBm to the antenna', 13, 'end', AC, True))
    o.append(Tb(cx + 76, 178, '45.5 dBm reflected back', 13, 'start', LV, True))
    o.append(Tb(cx + 22, 304, 'leak 1 → 3: 35 dBm', 13, 'end', MUT, True))
    o.append(Tb(cx + 76, 256, 'reflection 2 → 3: 45.0 dBm', 13, 'start', NX, True))
    o.append(T(360, 410, 'loss 0.5 dB with the rotation (1 → 2 → 3 → 1), isolation 25 dB against it', 13, fill=MUT))
    return 428, ''.join(o)


FIG[5] = (f5, 'The duplexer of worked example 2. The transmitter pulse reaches the receiver twice: 35 dBm by leakage against the rotation, and 45.0 dBm by reflection from the antenna, which then circulates on to port 3.',
          'Three-port circulator rotating 1 to 2 to 3: transmitter 60 dBm on port 1, antenna with VSWR 1.5 on port 2, receiver on port 3. 59.5 dBm reaches the antenna, 45.5 dBm reflects, 45.0 dBm reaches the receiver by reflection and 35 dBm by leakage.')


# ---- 4.6 Applegate diagram of worked example 1, drawn in the frame of an unmodulated electron ----
def f6():
    o = []
    e, m = 1.602e-19, 9.109e-31
    V0, f, L_ = 1200, 4e9, 0.03
    v0 = math.sqrt(2 * e * V0 / m); w = 2 * math.pi * f
    k = 1.841 / (w * L_ / v0)  # beta_i V1 / (2 V0) for X = 1.841
    T_ = 1 / f
    x0, x1, y0, y1 = 90, 640, 50, 290
    fx = lambda t: x0 + (t + 0.1 * T_) / (2.3 * T_) * (x1 - x0)
    fy = lambda z: y1 - z / L_ * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0 - 10, x0, y1, L2, 1.5))
    for c in (0, 1, 2):
        X = fx(c * T_); o.append(L(X, y1, X, y1 + 5, L2, 1.5)); o.append(T(X, y1 + 20, f'{c * 250} ps', 13, fill=MUT))
    o.append(T((x0 + x1) / 2, y1 + 42, 'time relative to an unmodulated electron (one RF cycle = 250 ps)', 13, fill=MUT))
    for cm in (0, 1, 2, 3):
        Y = fy(cm / 100); o.append(L(x0 - 5, Y, x0, Y, L2, 1.5)); o.append(T(x0 - 9, Y + 4.5, f'{cm} cm', 13, 'end', MUT))
    o.append(L(x0, fy(L_), x1, fy(L_), NX, 2, '7 5'))
    o.append(Tb(x1, fy(L_) - 10, 'output gap at 3 cm: bunches', 13, 'end', NX, True))
    o.append(T(x0, 30, 'distance from the input gap', 13, 'start', MUT))
    n = 24
    for i in range(n + 1):
        t0 = i * 2 * T_ / n
        v = v0 * (1 + k * math.sin(w * t0))
        tr = lambda z: t0 + z / v - z / v0
        ref = i % 12 == 0
        o.append(L(fx(t0), fy(0), fx(tr(L_)), fy(L_), LV if ref else AC, 2.6 if ref else 1.5))
    o.append(T(650, 120, 'reference', 13, 'start', LV, True)); o.append(T(650, 138, 'electrons', 13, 'start', LV, True))
    o.append(T(360, 366, 'v₀ = 2.054 × 10⁷ m/s, drift transit 1.46 ns, V₁ = 128 V gives X = 1.841', 13))
    return 384, ''.join(o)


FIG[6] = (f6, 'An Applegate diagram computed for the klystron of worked example 1, drawn relative to an unmodulated electron. Evenly spaced electrons leave the input gap; slowed ones drift back, speeded ones forward, and at the 3 cm output gap they crowd into one bunch per cycle.',
          'Distance from the input gap (0 to 3 cm) against time relative to an unmodulated electron over two 250 ps RF cycles at 4 GHz. 25 electrons leave evenly spaced; their lines tilt by their velocity modulation (X = 1.841) and crowd together at the 3 cm output gap. Reference electrons are highlighted.')


# ---- 4.7 GaAs velocity-field curve and the Gunn example ----
def f7():
    o = []
    E0 = 3600.0
    v = lambda E: (8500 * E + 1e7 * (E / E0) ** 4) / (1 + (E / E0) ** 4)  # cm/s, E in V/cm (empirical two-valley fit)
    x0, x1, y0, y1 = 90, 680, 50, 290
    fx = lambda E: x0 + E / 12000 * (x1 - x0)
    fy = lambda vv: y1 - vv / 2.4e7 * (y1 - y0)
    Epk = max(range(0, 12001, 10), key=v)
    # NDR band
    o.append(R(fx(Epk), y0, fx(12000) - fx(Epk), y1 - y0, LVS, 'none', 0))
    o.append(axes(x0, x1, y0, y1, [0, 2000, 4000, 6000, 8000, 10000, 12000], [0, 0.5e7, 1e7, 1.5e7, 2e7], fx, fy,
                  'electric field E (kV/cm)', 'drift velocity (10⁷ cm/s)', xfmt=lambda e: f'{e // 1000}', yfmt=lambda vv: f'{vv / 1e7:g}'))
    o.append(P([(fx(E), fy(v(E))) for E in range(0, 12001, 60)], AC, 3))
    o.append(C(fx(Epk), fy(v(Epk)), 6, AC))
    o.append(Tb(fx(Epk) - 8, fy(v(Epk)) - 12, f'threshold ≈ {Epk / 1000:.1f} kV/cm', 13, 'end', AC, True))
    o.append(T(fx(9000), y0 + 22, 'negative slope (NDR):', 13, fill=LV, bold=True))
    o.append(T(fx(9000), y0 + 40, 'electrons move to the slow valley', 13, fill=LV))
    o.append(L(fx(8000), y1, fx(8000), fy(v(8000)), NX, 2, '6 4'))
    o.append(C(fx(8000), fy(v(8000)), 6, NX))
    o.append(Tb(fx(8000) + 10, fy(v(8000)) - 14, 'bias 8 V on 10 µm = 8 kV/cm', 13, 'start', NX, True))
    o.append(T(fx(300), fy(1.75e7), 'low field:', 13, 'start', MUT)); o.append(T(fx(300), fy(1.75e7) + 18, 'v = μE', 13, 'start', MUT))
    return 340, ''.join(o)


FIG[7] = (f7, 'Drift velocity against field for GaAs (an empirical two-valley fit, computed). Beyond the 3.2 kV/cm peak the slope is negative; the Gunn diode of worked example 1, 8 V across 10 µm, sits at 8 kV/cm inside that region.',
          'Curve of GaAs electron drift velocity against field from 0 to 12 kV/cm, rising to a peak of about 2 times 10 to the 7 cm/s at 3.2 kV/cm and then falling; the falling part is shaded as negative differential resistance. The bias point 8 kV/cm is marked.')


# ---- 4.8 standing wave of the slotted-line example ----
def f8():
    o = []
    G = 0.4286 * cmath.exp(-1j * math.radians(71.46))
    lg = 39.8
    b = 2 * math.pi / lg
    k = 3.0 / (1 + abs(G))
    V = lambda d: k * abs(1 + G * cmath.exp(-2j * b * d))
    x0, x1, y0, y1 = 90, 680, 50, 280
    D = 50.0
    fx = lambda d: x1 - d / D * (x1 - x0)  # load at the right
    fy = lambda vv: y1 - vv / 3.4 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x1, y0 - 10, x1, y1, INK, 3))
    o.append(T(x1, y0 - 16, 'load', 13, 'middle', INK, True))
    for d in (0, 10, 20, 30, 40, 50):
        X = fx(d); o.append(L(X, y1, X, y1 + 5, L2, 1.5)); o.append(T(X, y1 + 20, f'{d}', 13, fill=MUT))
    o.append(T((x0 + x1) / 2, y1 + 42, 'distance from the load towards the generator (mm)', 13, fill=MUT))
    o.append(L(x0, y0, x0, y1, L2, 1.5))
    for vv in (0, 1.2, 3.0):
        Y = fy(vv); o.append(L(x0 - 5, Y, x0, Y, L2, 1.5)); o.append(T(x0 - 9, Y + 4.5, f'{vv:g}', 13, 'end', MUT))
        if vv: o.append(L(x0, Y, x1, Y, 'var(--line)', 1, '4 4'))
    o.append(T(x0, y0 - 16, 'probe reading', 13, 'start', MUT))
    o.append(P([(fx(D * i / 400), fy(V(D * i / 400))) for i in range(401)], AC, 3))
    for dm in (6.0, 25.9):
        o.append(C(fx(dm), fy(1.2), 6, LV))
    o.append(brace(fx(25.9), fx(6.0), fy(1.2) + 26, INK))
    o.append(Tb((fx(25.9) + fx(6.0)) / 2, fy(1.2) + 48, 'λg/2 = 19.9 mm', 14, 'middle', INK, True))
    o.append(brace(fx(6.0), fx(0), fy(0.25), LV))
    o.append(Tb((fx(6.0) + fx(0)) / 2 - 8, fy(0.25) + 22, 'd = 6.0 mm', 13, 'end', LV, True))
    o.append(Tb(fx(35.9), fy(3.0) - 10, 'V max = 3.0', 13, 'middle', AC, True))
    o.append(Tb(fx(44), fy(1.2) + 22, 'V min = 1.2', 13, 'middle', LV, True))
    return 350, ''.join(o)


FIG[8] = (f8, 'The probe reading along the slotted line of worked example 1, computed from Γ = 0.429∠−71.5°. Minima are 19.9 mm apart (λg/2), the first lies 6.0 mm from the load, and 3.0/1.2 gives VSWR 2.5.',
          'Standing-wave pattern from the load out to 50 mm: maxima 3.0 and minima 1.2, with minima at 6.0 mm and 25.9 mm from the load, 19.9 mm apart.')


# ---- 4.9 MMIC cross-section with the example's parts ----
def f9():
    o = []
    ys, yb = 210, 330  # substrate top and bottom
    o.append(R(40, ys, 640, yb - ys, ACS, 'none', 0))
    o.append(L(40, ys, 680, ys, AC, 1.5))
    o.append(T(360, 268, 'semi-insulating GaAs, about 100 µm thick (εr = 12.9)', 14, 'middle', INK, True))
    o.append(R(40, yb, 640, 10, INK, 'none', 0))
    o.append(T(670, yb + 30, 'back metal = ground', 13, 'end', MUT))
    # via hole at left
    o.append(P([(78, ys), (92, yb), (128, yb), (142, ys)], INK, 3))
    o.append(R(70, ys - 10, 80, 10, INK, 'none', 2))
    o.append(T(110, 370, 'via hole', 13, fill=MUT))
    # HEMT
    o.append(R(180, ys - 6, 140, 6, LVS, LV, 1, 1.5)); o.append(T(250, ys + 20, 'active layer', 13, fill=MUT))
    for x, lab in ((186, 'S'), (238, 'G'), (276, 'D')):
        w = 30 if lab != 'G' else 14
        o.append(R(x, ys - 26, w, 20, INK if lab != 'G' else LV, 'none', 2)); o.append(T(x + w / 2, ys - 34, lab, 13, bold=True))
    o.append(T(250, 132, 'HEMT', 14, 'middle', INK, True))
    # MIM capacitor
    o.append(R(370, ys - 10, 110, 10, INK, 'none', 1))
    o.append(R(370, ys - 18, 110, 8, NXS, NX, 1, 1.5))
    o.append(R(380, ys - 30, 90, 12, INK, 'none', 1))
    o.append(T(425, 132, 'MIM capacitor 2 pF', 14, 'middle', INK, True))
    o.append(T(425, 150, '78 µm square, 0.2 µm nitride', 13, fill=MUT))
    o.append(L(425, 156, 425, ys - 34, L2, 1.5))
    # resistor
    o.append(R(520, ys - 6, 60, 6, NX, 'none', 1))
    o.append(T(550, 176, 'resistor 100 Ω', 13, 'middle', INK, True)); o.append(T(550, 192, '20 × 10 µm', 13, fill=MUT))
    # airbridge over a metal-1 line at right
    o.append(R(618, ys - 10, 22, 10, INK, 'none', 1))
    o.append(P([(596, ys - 10), (602, ys - 46), (656, ys - 46), (662, ys - 10)], LV, 5))
    o.append(R(590, ys - 10, 14, 10, INK, 'none', 1)); o.append(R(654, ys - 10, 14, 10, INK, 'none', 1))
    o.append(T(640, 100, 'airbridge', 14, 'middle', LV, True)); o.append(T(640, 118, '(metal 2, air below)', 13, fill=MUT))
    o.append(L(640, 124, 630, ys - 50, L2, 1.5))
    o.append(T(60, 70, 'black = metal 1 (lines, contacts, lower plates)', 13, 'start', MUT))
    o.append(T(60, 90, 'not to scale', 13, 'start', MUT))
    return 384, ''.join(o)


FIG[9] = (f9, 'A slice through a GaAs MMIC with the parts of worked example 1: a HEMT, the 2 pF MIM capacitor, the 100 Ω thin-film resistor, and an airbridge (the second metal) crossing a first-metal line with air beneath. A via joins top-side ground to the back metal.',
          'Cross-section, not to scale: GaAs substrate about 100 micrometres thick with back metal and a via hole; on top a HEMT with source, gate and drain, a MIM capacitor 2 pF 78 micrometres square with 0.2 micrometre nitride, a 100 ohm resistor 20 by 10 micrometres, and an airbridge of metal 2 crossing a metal 1 line.')


AFTER = {1: 2, 2: 3, 3: 3, 4: 2, 5: 3, 6: 1, 7: 1, 8: 1, 9: 2}
_base = make_spec(FIG)


def spec(k):
    d = _base(k)
    d['after_section'] = AFTER[k]
    return d
