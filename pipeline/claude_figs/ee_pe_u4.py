"""Claude's hand-drawn figures for ee-pe-u4 (Power Electronics: DC-AC inverters), one per chapter, drawn from each chapter's
own worked example and numbers. Waveforms are computed (exponential R-L current, PWM comparisons, staircase angles) and
plotted to scale. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt
pi = math.pi
rad = math.radians


def _sub(s):
    """V_dc, I_max ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔ])_([A-Za-z0-9,]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def sw(x, y, name, w=40, h=28, fill=PANEL):
    """a switch box centred at (x, y) with its anti-parallel diode drawn to the right"""
    o = [R(x - w / 2, y - h / 2, w, h, fill, AC, 4), T(x, y + 5, name, 13, bold=True)]
    dx = x + w / 2 + 14
    o.append(f'<polygon points="{dx - 7:.1f},{y + 6:.1f} {dx + 7:.1f},{y + 6:.1f} {dx:.1f},{y - 6:.1f}" style="fill:{L2};stroke:{MUT};stroke-width:1.2"/>')
    o.append(L(dx - 7, y - 6, dx + 7, y - 6, MUT, 1.6))
    o.append(L(x, y - h / 2 - 8, dx, y - h / 2 - 8, MUT, 1.2)); o.append(L(dx, y - h / 2 - 8, dx, y - 6, MUT, 1.2))
    o.append(L(x, y + h / 2 + 8, dx, y + h / 2 + 8, MUT, 1.2)); o.append(L(dx, y + 6, dx, y + h / 2 + 8, MUT, 1.2))
    return ''.join(o)


def coil(x0, x1, y, c=AC, n=4):
    r = (x1 - x0) / (2 * n)
    d = f'M{x0:.1f},{y:.1f} ' + ' '.join(f'a{r:.1f},{r:.1f} 0 0 1 {2*r:.1f},0' for _ in range(n))
    return f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:2.2"/>'


def resistor(x0, x1, y, c=AC):
    w = x1 - x0; pts = [(x0, y)]
    for i in range(1, 8): pts.append((x0 + w * i / 8, y + (-8 if i % 2 else 8)))
    pts.append((x1, y))
    return P(pts, c, 2)


def source(x, ytop, ybot, label):
    o = [L(x, ytop, x, (ytop + ybot) / 2 - 8, INK, 2), L(x - 16, (ytop + ybot) / 2 - 8, x + 16, (ytop + ybot) / 2 - 8, INK, 3),
         L(x - 9, (ytop + ybot) / 2 + 2, x + 9, (ytop + ybot) / 2 + 2, INK, 3), L(x, (ytop + ybot) / 2 + 2, x, ybot, INK, 2)]
    o.append(T(x - 24, (ytop + ybot) / 2 - 12, '+', 14, 'middle', INK, bold=True))
    o.append(T(x - 22, (ytop + ybot) / 2 + 26, label, 14, 'end', INK, bold=True))
    return ''.join(o)


FIG = {}


# ---- 4.1 full bridge with the R-L load of worked example 2: 220 V, 10 ohm, 25 mH, 50 Hz ----
def f1():
    o = []
    top, bot, mid = 40, 210, 125
    o.append(L(70, top, 470, top, INK, 2)); o.append(L(70, bot, 470, bot, INK, 2))
    o.append(source(70, top, bot, '220 V'))
    for x, a, b in ((210, 'S1', 'S2'), (430, 'S3', 'S4')):
        o.append(L(x, top, x, mid - 52, INK, 2)); o.append(sw(x, mid - 38, a)); o.append(L(x, mid - 24, x, mid + 24, INK, 2))
        o.append(sw(x, mid + 38, b)); o.append(L(x, mid + 52, x, bot, INK, 2))
    o.append(C(210, mid, 4, INK)); o.append(C(430, mid, 4, INK))
    o.append(T(198, mid - 8, 'A', 14, 'end', bold=True)); o.append(T(418, mid - 8, 'B', 14, 'end', bold=True))
    o.append(L(210, mid, 262, mid, INK, 2)); o.append(resistor(262, 302, mid)); o.append(L(302, mid, 320, mid, INK, 2))
    o.append(coil(320, 368, mid)); o.append(L(368, mid, 430, mid, INK, 2))
    o.append(T(282, mid - 16, '10 Ω', 13)); o.append(T(344, mid - 16, '25 mH', 13))
    o.append(L(300, mid + 18, 350, mid + 18, LV, 2, arrow='l')); o.append(T(325, mid + 36, 'i_o', 14, fill=LV, bold=True))
    o.append(boxt(500, 52, 200, 136, ['τ = L/R = 2.5 ms', 'I_max = 22 tanh 2', '= 21.21 A', 'diodes conduct', 'for 1.69 ms'], PANEL, L2, 14))
    # waveforms over one 20 ms period
    x0, x1 = 80, 690
    fx = lin(0, 20, x0, x1)
    yv = lin(-220, 220, 330, 250)
    o.append(L(x0, yv(0), x1, yv(0), L2, 1.2))
    o.append(P([(fx(0), yv(220)), (fx(10), yv(220)), (fx(10), yv(-220)), (fx(20), yv(-220))], AC, 2.5))
    o.append(T(x0 - 8, yv(220) + 5, '+220', 13, 'end', MUT)); o.append(T(x0 - 8, yv(-220) + 5, '−220', 13, 'end', MUT))
    o.append(T(x0 - 8, yv(0) + 5, 'v_o', 14, 'end', AC, bold=True))
    tau, Im = 2.5, 21.2086
    yi = lin(-25, 25, 450, 360)
    o.append(L(x0, yi(0), x1, yi(0), L2, 1.2))
    # diode intervals shaded
    for t0, lab in ((0, 'D1 D4'), (10, 'D2 D3')):
        o.append(R(fx(t0), 356, fx(t0 + 1.6875) - fx(t0), 98, NXS, NX, 2, sw=1))
        o.append(T(fx(t0) + 4, 472, lab, 13, 'start', NX, bold=True))
    for t0, lab in ((5.2, 'S1 S4'), (15.2, 'S2 S3')):
        o.append(T(fx(t0), 472, lab, 13, 'middle', AC, bold=True))
    pts = []
    for i in range(201):
        t = 20 * i / 200
        sgn = 1 if t < 10 else -1; tt = t if t < 10 else t - 10
        pts.append((fx(t), yi(sgn * (22 - (22 + Im) * math.exp(-tt / tau)))))
    o.append(P(pts, LV, 2.5))
    o.append(T(x0 - 8, yi(Im) + 5, '+21.2', 13, 'end', MUT)); o.append(T(x0 - 8, yi(-Im) + 5, '−21.2', 13, 'end', MUT))
    o.append(L(x0, yi(Im), x1, yi(Im), 'var(--line)', 1, dash='3 4')); o.append(L(x0, yi(-Im), x1, yi(-Im), 'var(--line)', 1, dash='3 4'))
    o.append(T(x0 - 8, yi(0) + 5, 'i_o', 14, 'end', LV, bold=True))
    for t in (0, 5, 10, 15, 20):
        o.append(T(fx(t), 494, f'{t} ms', 13, fill=MUT))
    return 504, ''.join(o)


FIG[1] = (f1, 'The second worked example: a 220 V full bridge feeding 10 Ω and 25 mH at 50 Hz. The load voltage is a ±220 V square wave; the current '
              'swings exponentially between −21.2 A and +21.2 A, and for the first 1.69 ms after each switching it flows back to the source through the diodes.',
          'A full-bridge circuit: a 220 volt source, switches S1 to S4 each with an anti-parallel diode, and a 10 ohm, 25 millihenry load between midpoints A and B. '
          'Below, the load voltage is a plus and minus 220 volt square wave and the load current an exponential wave between minus and plus 21.2 amperes; the first 1.69 milliseconds of each half cycle are shaded as diode conduction.')


# ---- 4.2 180 degree gating and the phase and line voltages for V_dc = 400 V ----
def f2():
    o = []
    x0, x1 = 90, 690
    fx = lin(0, 360, x0, x1)
    starts = {'S1': 0, 'S2': 60, 'S3': 120, 'S4': 180, 'S5': 240, 'S6': 300}
    for i, (nm, st) in enumerate(starts.items()):
        y = 34 + i * 30
        o.append(T(x0 - 10, y + 14, nm, 13, 'end', bold=True))
        o.append(R(x0, y, x1 - x0, 20, FIGBG, 'var(--line)', 3, sw=1))
        a, b = st, st + 180
        segs = [(a, min(b, 360))] + ([(0, b - 360)] if b > 360 else [])
        for s0, s1 in segs:
            o.append(R(fx(s0), y, fx(s1) - fx(s0), 20, ACS if nm in ('S1', 'S3', 'S5') else LVS, AC if nm in ('S1', 'S3', 'S5') else LV, 3, sw=1.5))
    for d in range(0, 361, 60):
        o.append(L(fx(d), 30, fx(d), 470, L2, 1, dash='3 4'))
    # phase voltage v_AN (six-step) and line voltage v_AB (quasi-square)
    yp = lin(-300, 300, 330, 230)
    vals = [133.3, 266.7, 133.3, -133.3, -266.7, -133.3]
    pts = []
    for k, v in enumerate(vals): pts += [(fx(60 * k), yp(v)), (fx(60 * k + 60), yp(v))]
    o.append(L(x0, yp(0), x1, yp(0), L2, 1.2)); o.append(P(pts, AC, 2.5))
    o.append(T(x0 - 10, yp(0) + 5, 'v_AN', 14, 'end', AC, bold=True))
    o.append(Tb(fx(90), yp(266.7) - 8, '266.7 V', 13)); o.append(Tb(fx(30), yp(133.3) - 8, '133.3 V', 13))
    yl = lin(-450, 450, 460, 350)
    lv = [400, 400, 0, -400, -400, 0]
    pts = []
    for k, v in enumerate(lv): pts += [(fx(60 * k), yl(v)), (fx(60 * k + 60), yl(v))]
    o.append(L(x0, yl(0), x1, yl(0), L2, 1.2)); o.append(P(pts, LV, 2.5))
    o.append(T(x0 - 10, yl(0) + 5, 'v_AB', 14, 'end', LV, bold=True))
    o.append(Tb(fx(60), yl(400) - 8, '+400 V for 120°', 13)); o.append(Tb(fx(240), yl(-400) + 18, '−400 V', 13))
    for d in range(0, 361, 60):
        o.append(T(fx(d), 490, f'{d}°', 13, fill=MUT))
    return 500, ''.join(o)


FIG[2] = (f2, 'Gate signals of the six switches in 180° mode (each 180° long, a new one every 60°), and the result for the first worked example on a 400 V bus: '
              'a six-step phase voltage of ±133.3 V and ±266.7 V, and a line voltage of ±400 V for 120° with 60° zero steps.',
          'Six horizontal bars show the gating of S1 to S6, each 180 degrees long and starting 60 degrees after the previous one. Below, the phase voltage steps through '
          '133.3, 266.7 and 133.3 volts and then the negative values; the line voltage is plus 400 volts for 120 degrees, zero for 60, minus 400 for 120 and zero for 60.')


# ---- 4.3 single pulse (d = 30 deg) and four 10-degree pulses on a 200 V bus, with their fundamentals ----
def f3():
    o = []
    x0, x1 = 90, 690
    fx = lin(0, 360, x0, x1)

    def panel(ytop, pulses, b1, title, lab1):
        fy = lin(-230, 230, ytop + 150, ytop)
        o.append(T(x0, ytop - 10, title, 14, 'start', bold=True))
        o.append(L(x0, fy(0), x1, fy(0), L2, 1.2))
        for sgn, base in ((1, 0), (-1, 180)):
            for c, w in pulses:
                a, b = base + c - w / 2, base + c + w / 2
                o.append(R(fx(a), fy(200) if sgn > 0 else fy(0), fx(b) - fx(a), fy(0) - fy(200), ACS, AC, 1, sw=1.5))
        sine = [(fx(t), fy(b1 * math.sin(rad(t)))) for t in range(0, 361, 4)]
        o.append(P(sine, LV, 2.5))
        o.append(T(x0 - 8, fy(200) + 5, '+200', 13, 'end', MUT)); o.append(T(x0 - 8, fy(-200) + 5, '−200', 13, 'end', MUT))
        o.append(T(fx(200), fy(120), lab1, 13, 'start', LV, bold=True))
    panel(44, [(90, 60)], 127.3, 'Single pulse, 2d = 60°: V_rms = 115.5 V', 'fundamental 127.3 V peak')
    panel(256, [(22.5, 10), (67.5, 10), (112.5, 10), (157.5, 10)], 58.0, 'Four 10° pulses per half cycle: V_rms = 94.3 V', 'fundamental 58.0 V peak')
    for d in range(0, 361, 90):
        o.append(T(fx(d), 430, f'{d}°', 13, fill=MUT))
    return 440, ''.join(o)


FIG[3] = (f3, 'The first worked example on a 200 V bus. Top: one 60° pulse per half cycle gives 115.5 V rms and a 127.3 V peak fundamental. Bottom: four 10° pulses '
              'per half cycle give 94.3 V rms and a 58.0 V fundamental; the pulses are spread over the half cycle, so their strongest harmonics are the 7th and 9th.',
          'Two waveforms over one cycle. In the top one each half cycle has a single 200 volt pulse 60 degrees wide centred on the peak, with a fundamental sine of 127.3 volts drawn over it. '
          'In the bottom one each half cycle has four 10 degree pulses, with a 58 volt fundamental.')


# ---- 4.4 sine-triangle comparison (m_a = 0.8, m_f = 21) and the bipolar and unipolar outputs ----
def tri(x):
    x = x % 1.0
    return 4 * x - 1 if x < 0.5 else 3 - 4 * x


def f4():
    o = []
    x0, x1 = 90, 690
    fx = lin(0, 1, x0, x1)
    fy = lin(-1.1, 1.1, 170, 40)
    N = 2400
    ts = [i / N for i in range(N + 1)]
    car = [tri(21 * t + 0.25) for t in ts]
    ref = [0.8 * math.sin(2 * pi * t) for t in ts]
    o.append(L(x0, fy(0), x1, fy(0), L2, 1.2))
    o.append(P([(fx(t), fy(c)) for t, c in zip(ts[::4], car[::4])], L2, 1.2))
    o.append(P([(fx(t), fy(v)) for t, v in zip(ts, ref)], AC, 2.5))
    o.append(T(x0 - 8, fy(0.8) + 5, '0.8', 13, 'end', MUT))
    o.append(T(x0, 22, 'sine reference m_a = 0.8 at 50 Hz, carrier 1050 Hz (m_f = 21)', 13, 'start', AC, bold=True))

    def wave(vals, ytop, lab, levels, c):
        g = lin(-1, 1, ytop + 80, ytop)
        o.append(L(x0, g(0), x1, g(0), L2, 1.2))
        pts = []; prev = None
        for t, v in zip(ts, vals):
            if prev is not None and v != prev: pts.append((fx(t), g(prev)))
            pts.append((fx(t), g(v))); prev = v
        o.append(P(pts, c, 1.4))
        o.append(T(x0 - 8, g(0) + 5, lab, 14, 'end', c, bold=True))
        for v, s in levels: o.append(T(x1 + 6, g(v) + 5, s, 13, 'start', MUT))
    bip = [1 if r > c else -1 for r, c in zip(ref, car)]
    uni = [(1 if r > c else 0) - (1 if -r > c else 0) for r, c in zip(ref, car)]
    wave(bip, 206, 'bipolar', [(1, '+V'), (-1, '−V')], AC)
    wave(uni, 326, 'unipolar', [(1, '+V'), (0, '0'), (-1, '−V')], LV)
    o.append(T(390, 440, 'V = V_dc = 400 V; both give a 320 V peak fundamental (m_a V_dc)', 13, fill=MUT))
    return 452, ''.join(o)


FIG[4] = (f4, 'The worked example’s modulator over one 20 ms cycle: a 0.8 sine against a 1050 Hz carrier. The bipolar output jumps between +400 V and −400 V; '
              'the unipolar output uses +400 V, 0 and −400 V, so its steps are half as large and its ripple sits near twice the carrier frequency.',
          'Top: a sine reference of amplitude 0.8 and a triangular carrier with 21 cycles in one period. Middle: the bipolar output, a two-level pulse train. '
          'Bottom: the unipolar output, a three-level pulse train whose pulse widths follow the sine.')


# ---- 4.5 hexagon of space vectors with the worked example's reference (600 V, V_m = 300 V, theta = 20 deg) ----
def f5():
    o = []
    cx, cy, Rv = 250, 230, 170          # 400 V (2V_dc/3) drawn as 170 px
    s = Rv / 400.0
    names = ['V1 100', 'V2 110', 'V3 010', 'V4 011', 'V5 001', 'V6 101']
    pts = [(cx + Rv * math.cos(rad(60 * k)), cy - Rv * math.sin(rad(60 * k))) for k in range(6)]
    o.append(P(pts + [pts[0]], L2, 1.6))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{346.4*s:.1f}" style="fill:none;stroke:{MUT};stroke-width:1.2;stroke-dasharray:4 4"/>')
    for k, (x, y) in enumerate(pts):
        o.append(L(cx, cy, x, y, AC if k < 2 else L2, 2.5 if k < 2 else 1.6, arrow='n' if k < 2 else 'm'))
        nm, st = names[k].split()
        dx = math.cos(rad(60 * k)); dy = -math.sin(rad(60 * k))
        lx, ly = x + dx * 30, y + dy * 24
        anc = 'start' if dx > 0.3 else ('end' if dx < -0.3 else 'middle')
        o.append(T(lx, ly, nm, 14, anc, bold=True)); o.append(T(lx, ly + 16, st, 13, anc, MUT))
    for k in range(6):
        a = rad(60 * k + 30)
        rr = 0.45 if k == 0 else 0.62
        o.append(T(cx + rr * Rv * math.cos(a), cy - rr * Rv * math.sin(a) + 5, f'{k+1}', 13, fill=MUT))
    o.append(C(cx, cy, 5, INK)); o.append(T(cx - 10, cy + 22, 'V0, V7', 13, 'end'))
    # reference and its two components
    ax, ay = 222.7 * s, 0
    bx, by = 118.5 * s * 0.5, -118.5 * s * math.sin(rad(60))
    o.append(L(cx, cy, cx + ax, cy, LV, 3))
    o.append(L(cx + ax, cy, cx + ax + bx, cy + by, LV, 3, dash='5 3'))
    o.append(L(cx, cy, cx + ax + bx, cy + by, NX, 3, arrow='x'))
    o.append(Tb(cx + ax / 2, cy + 20, '(T_x/T_s) V1', 13, fill=LV))
    o.append(T(cx + ax + bx + 10, cy + by - 12, 'V_ref', 14, 'start', NX, bold=True))
    o.append(boxt(492, 70, 214, 160, ['|V1| = 2V_dc/3 = 400 V', 'V_ref = 300 V at θ = 20°', 'm = 0.866, T_s = 166.7 μs', 'T_x = 92.8 μs (V1)', 'T_y = 49.4 μs (V2)', 'T_0 = 24.5 μs'], PANEL, L2, 14))
    o.append(T(599, 262, 'dashed circle: linear limit', 13, fill=MUT))
    o.append(T(599, 280, 'V_dc/√3 = 346.4 V', 13, fill=MUT))
    return 440, ''.join(o)


FIG[5] = (f5, 'The six active vectors, each 2V_dc/3 = 400 V long on the 600 V bus, form a hexagon with the zero vectors at its centre. The worked example’s 300 V reference at '
              '20° in sector 1 is made from 92.8 μs of V1 and 49.4 μs of V2 in each 166.7 μs period; the dashed circle is the 346.4 V linear limit.',
          'A hexagon with six vectors V1 to V6 labelled with their switch states, sectors 1 to 6 between them, and the zero vectors at the centre. A reference vector of 300 volts '
          'at 20 degrees is drawn as the sum of a part along V1 and a part along V2. A box lists the dwell times 92.8, 49.4 and 24.5 microseconds.')


# ---- 4.6 quarter-wave patterns and the spectrum of the two-notch wave (V_dc = 220 V) ----
def f6():
    o = []
    # left: one half cycle of the two-notch bipolar wave
    x0, x1 = 60, 330
    fx = lin(0, 180, x0, x1)
    fy = lin(-1.2, 1.2, 190, 50)
    a1, a2 = 23.64, 33.33
    edges = [0, a1, a2, 180 - a2, 180 - a1, 180]
    lev = [1, -1, 1, -1, 1]
    pts = []
    for k in range(5): pts += [(fx(edges[k]), fy(lev[k])), (fx(edges[k + 1]), fy(lev[k]))]
    o.append(L(x0, fy(0), x1, fy(0), L2, 1.2)); o.append(P(pts, AC, 2.4))
    o.append(T(x0, 34, 'Two notches per quarter', 14, 'start', bold=True))
    o.append(T(x0 - 6, fy(1) + 5, '+V', 13, 'end', MUT)); o.append(T(x0 - 6, fy(-1) + 5, '−V', 13, 'end', MUT))
    o.append(L(fx(a1), fy(-1) + 6, fx(a1), 214, MUT, 1, dash='3 3')); o.append(L(fx(a2), fy(-1) + 6, fx(a2), 232, MUT, 1, dash='3 3'))
    o.append(T(fx(a1) - 4, 228, 'α_1 = 23.64°', 13, 'end', MUT)); o.append(T(fx(a2) + 4, 246, 'α_2 = 33.33°', 13, 'start', MUT))
    o.append(T(fx(90), 246, '', 13))
    o.append(T(x1, 214, '180°', 13, 'end', MUT))
    # right: bar spectrum, square wave vs two-notch wave, per unit of 4V_dc/pi
    bx0, bx1, by0, by1 = 400, 700, 50, 230
    g = lambda n: 1 - 2 * math.cos(rad(n * a1)) + 2 * math.cos(rad(n * a2))
    orders = [1, 3, 5, 7, 9, 11]
    fyb = lin(0, 1.0, by1, by0)
    o.append(L(bx0, by1, bx1, by1, L2, 1.5))
    for v in (0.5, 1.0):
        o.append(L(bx0, fyb(v), bx1, fyb(v), 'var(--line)', 1)); o.append(T(bx0 - 6, fyb(v) + 5, f'{v}', 13, 'end', MUT))
    o.append(T(bx0, 34, 'Harmonic peak ÷ (4V_dc/π)', 14, 'start', bold=True))
    W = (bx1 - bx0) / len(orders)
    for i, n in enumerate(orders):
        xc = bx0 + W * (i + 0.5)
        sqv, ntv = 1 / n, abs(g(n)) / n
        o.append(R(xc - 18, fyb(sqv), 16, by1 - fyb(sqv), PANEL, L2, 2, sw=1.5))
        if ntv > 0.004: o.append(R(xc + 2, fyb(ntv), 16, by1 - fyb(ntv), ACS, AC, 2, sw=1.5))
        else: o.append(T(xc + 10, by1 - 6, '0', 13, fill=AC, bold=True))
        o.append(T(xc, by1 + 20, str(n), 13, fill=MUT))
    o.append(T((bx0 + bx1) / 2, by1 + 40, 'harmonic order n', 13, fill=MUT))
    o.append(R(410, 290, 14, 14, PANEL, L2, 2, sw=1.5)); o.append(T(430, 302, 'square wave', 13, 'start'))
    o.append(R(540, 290, 14, 14, ACS, AC, 2, sw=1.5)); o.append(T(560, 302, 'two notches', 13, 'start'))
    o.append(boxt(60, 270, 290, 60, ['b_3 = b_5 = 0', 'b_1 = 0.839 × 280.1 = 235.0 V'], PANEL, L2, 14))
    return 346, ''.join(o)


FIG[6] = (f6, 'The second worked example. Left: one half cycle of the square wave with two notches per quarter at 23.64° and 33.33°. Right: its harmonics against those of a plain '
              'square wave; the 3rd and 5th are gone, the fundamental keeps 84 % of its value, and the 7th, 9th and 11th grow.',
          'Left, a two-level half cycle that is positive except for two narrow negative notches near each end. Right, paired bars for harmonic orders 1 to 11: the square wave falls as 1 over n; '
          'the notched wave has zero 3rd and 5th and larger 7th, 9th and 11th.')


# ---- 4.7 single-phase capacitor-commutated CSI (20 A, 10 ohm, 20 uF, 500 Hz) ----
def f7():
    o = []
    top, bot = 50, 230
    o.append(L(60, top, 520, top, INK, 2)); o.append(L(60, bot, 520, bot, INK, 2))
    o.append(source(60, top, bot, 'DC'))
    o.append(coil(90, 150, top, AC, 4)); o.append(R(88, top - 3, 64, 6, FIGBG, FIGBG, 0, sw=0))
    o.append(coil(90, 150, top, AC, 4)); o.append(T(120, top - 14, 'L_d', 14, bold=True))
    o.append(L(170, top + 18, 230, top + 18, LV, 2, arrow='l')); o.append(T(200, top + 36, 'I_d = 20 A', 13, fill=LV, bold=True))

    def thy(x, y, name):
        return (f'<polygon points="{x - 12:.1f},{y - 8:.1f} {x + 12:.1f},{y - 8:.1f} {x:.1f},{y + 10:.1f}" style="fill:{ACS};stroke:{AC};stroke-width:1.8"/>'
                + L(x - 12, y + 10, x + 12, y + 10, AC, 2.2) + L(x + 6, y + 6, x + 16, y + 16, AC, 1.6) + T(x - 18, y + 6, name, 13, 'end', bold=True))
    mid = 140
    for x, a, b in ((300, 'T1', 'T4'), (480, 'T3', 'T2')):
        o.append(L(x, top, x, mid - 50, INK, 2)); o.append(thy(x, mid - 40, a)); o.append(L(x, mid - 30, x, mid + 30, INK, 2))
        o.append(thy(x, mid + 40, b)); o.append(L(x, mid + 50, x, bot, INK, 2))
        o.append(C(x, mid, 4, INK))
    o.append(L(300, mid, 340, mid, INK, 2)); o.append(L(440, mid, 480, mid, INK, 2))
    o.append(L(340, mid - 30, 340, mid + 30, INK, 2)); o.append(L(440, mid - 30, 440, mid + 30, INK, 2))
    o.append(L(340, mid - 30, 440, mid - 30, INK, 2)); o.append(L(340, mid + 30, 440, mid + 30, INK, 2))
    o.append(resistor(370, 410, mid - 30)); o.append(R(368, mid - 33, 44, 6, FIGBG, FIGBG, 0, sw=0)); o.append(resistor(370, 410, mid - 30))
    o.append(T(390, mid - 44, 'R = 10 Ω', 13))
    o.append(R(375, mid + 26, 30, 8, FIGBG, FIGBG, 0, sw=0))
    o.append(L(385, mid + 18, 385, mid + 42, AC, 3)); o.append(L(395, mid + 18, 395, mid + 42, AC, 3))
    o.append(T(390, mid + 62, 'C = 20 μF', 13))
    o.append(T(390, mid + 5, 'v_C', 14, bold=True, fill=NX))
    o.append(boxt(550, 70, 150, 140, ['RC = 200 μs', 'T/2 = 1 ms', 'V_0 = 197.3 V', 't_c = 137.3 μs', 't_q = 40 μs'], PANEL, L2, 14))
    # load voltage over one period, computed
    x0, x1 = 80, 690
    fx = lin(0, 2.0, x0, x1)
    fy = lin(-220, 220, 420, 290)
    o.append(L(x0, fy(0), x1, fy(0), L2, 1.2))
    V0, RC = 197.32, 0.2
    pts = []
    for i in range(401):
        t = 2.0 * i / 400; sg = 1 if t < 1.0 else -1; tt = t if t < 1.0 else t - 1.0
        pts.append((fx(t), fy(sg * (200 - (200 + V0) * math.exp(-tt / RC)))))
    tc = 0.1373
    o.append(R(fx(1.0), fy(V0), fx(1.0 + tc) - fx(1.0), fy(0) - fy(V0), LVS, LV, 2, sw=1))
    o.append(R(fx(0), fy(0), fx(tc) - fx(0), fy(-V0) - fy(0), LVS, LV, 2, sw=1))
    o.append(P(pts, NX, 2.5))
    o.append(T(fx(1.0 + tc) + 8, fy(150), 't_c = 137.3 μs: T1, T2 reverse-biased', 13, 'start', LV, bold=True))
    o.append(T(fx(tc) + 8, fy(-150), 't_c: T3, T4 reverse-biased', 13, 'start', LV))
    o.append(T(x0 - 8, fy(197.3) + 5, '+197', 13, 'end', MUT)); o.append(T(x0 - 8, fy(-197.3) + 5, '−197', 13, 'end', MUT))
    o.append(T(x0 - 8, fy(0) + 5, 'v_C', 14, 'end', NX, bold=True))
    for t in (0, 0.5, 1.0, 1.5, 2.0):
        o.append(T(fx(t), 444, f'{t:g} ms', 13, fill=MUT))
    o.append(T(fx(0.6), fy(-70), 'T1, T2 carry I_d', 13, 'middle', AC, bold=True)); o.append(T(fx(1.6), fy(60), 'T3, T4 carry I_d', 13, 'middle', AC, bold=True))
    return 454, ''.join(o)


FIG[7] = (f7, 'The second worked example: I_d = 20 A is steered through T1, T2 or T3, T4 into 10 Ω with 20 μF across it. At each switching the capacitor voltage, ±197.3 V, '
              'reverse-biases the outgoing pair; it stays negative across them for t_c = 137.3 μs, more than three times their 40 μs turn-off time.',
          'Circuit of a single-phase current source inverter: a DC source and series inductor feed four thyristors, with a resistor and capacitor in parallel between the bridge midpoints. '
          'Below, the capacitor voltage over one 2 millisecond period rises exponentially to plus 197 volts, jumps sign at each switching, and the shaded turn-off intervals of 137 microseconds are marked.')


# ---- 4.8 three-level NPC leg (600 V) and the three-cell CHB staircase with its angles ----
def f8():
    o = []
    top, bot, mid = 40, 300, 170
    xl = 120
    o.append(L(60, top, xl, top, INK, 2)); o.append(L(60, bot, xl, bot, INK, 2))
    # capacitors on the left
    for y0, lab in ((top, 'C1 300 V'), (mid, 'C2 300 V')):
        cy = (y0 + y0 + 130) / 2
        o.append(L(60, y0, 60, cy - 6, INK, 2)); o.append(L(46, cy - 6, 74, cy - 6, AC, 3)); o.append(L(46, cy + 6, 74, cy + 6, AC, 3)); o.append(L(60, cy + 6, 60, y0 + 130, INK, 2))
        o.append(T(80, cy + 5, lab, 13, 'start'))
    o.append(C(60, mid, 4, INK)); o.append(T(52, mid - 8, 'O', 14, 'end', bold=True))
    xs = 260
    ys = [72, 130, 210, 268]
    o.append(L(xl, top, xs, top, INK, 2)); o.append(L(xl, bot, xs, bot, INK, 2))
    o.append(L(xs, top, xs, ys[0] - 22, INK, 2))
    for i, y in enumerate(ys):
        o.append(sw(xs, y, f'S{i+1}', 40, 26))
        if i < 3: o.append(L(xs, y + 21, xs, ys[i + 1] - 21, INK, 2))
    o.append(L(xs, ys[3] + 21, xs, bot, INK, 2))
    # clamping diodes from O to the nodes between S1-S2 and S3-S4
    n1, n3 = (ys[0] + ys[1]) / 2, (ys[2] + ys[3]) / 2
    o.append(L(60, mid, 180, mid, INK, 2))
    o.append(L(180, n1, 180, n3, INK, 2))
    o.append(L(180, n1, xs, n1, INK, 1.6)); o.append(L(180, n3, xs, n3, INK, 1.6))
    for yy, up in ((n1 + 20, True), (n3 - 20, True)):
        o.append(f'<polygon points="{173:.1f},{yy + 6:.1f} {187:.1f},{yy + 6:.1f} {180:.1f},{yy - 6:.1f}" style="fill:{NXS};stroke:{NX};stroke-width:1.6"/>')
        o.append(L(173, yy - 6, 187, yy - 6, NX, 2))
    o.append(T(170, n1 + 26, 'D1', 13, 'end', NX, bold=True)); o.append(T(170, n3 - 14, 'D2', 13, 'end', NX, bold=True))
    o.append(C(xs, mid, 4, INK)); o.append(L(xs, mid, 330, mid, INK, 2)); o.append(T(338, mid + 5, 'pole A', 13, 'start', bold=True))
    o.append(boxt(400, 60, 300, 104, ['S1 S2 on: +300 V', 'S2 S3 on: 0 (through D1 or D2)', 'S3 S4 on: −300 V', 'each switch blocks 300 V'], PANEL, L2, 14))
    # CHB staircase
    x0, x1 = 400, 700
    fx = lin(0, 180, x0, x1); fy = lin(0, 320, 300, 200)
    al = (11.50, 28.72, 57.11)
    edges = [0, al[0], al[1], al[2], 180 - al[2], 180 - al[1], 180 - al[0], 180]
    lev = [0, 100, 200, 300, 200, 100, 0]
    pts = []
    for k in range(7): pts += [(fx(edges[k]), fy(lev[k])), (fx(edges[k + 1]), fy(lev[k]))]
    o.append(L(x0, fy(0), x1, fy(0), L2, 1.2)); o.append(P(pts, AC, 2.4))
    o.append(P([(fx(t), fy(305.6 * math.sin(rad(t)))) for t in range(0, 181, 3)], LV, 2))
    o.append(T(x0, 190, 'Three-cell CHB, half cycle', 14, 'start', bold=True))
    for v in (100, 200, 300): o.append(T(x0 - 6, fy(v) + 5, str(v), 13, 'end', MUT))
    o.append(T(x0 + 4, 322, 'α = 11.50°, 28.72°, 57.11°', 13, 'start', MUT))
    o.append(T(x1, 340, 'fundamental 305.6 V peak; 5th, 7th = 0', 13, 'end', LV))
    return 352, ''.join(o)


FIG[8] = (f8, 'Left: one leg of the first worked example’s three-level NPC inverter on a 600 V bus; the clamping diodes tie the inner switch nodes to the midpoint O, so every switch '
              'blocks 300 V. Right: half a cycle of the second example’s three-cell staircase, whose step angles remove the 5th and 7th and give a 305.6 V fundamental.',
          'A three-level neutral-point-clamped leg: two 300 volt capacitors in series, four switches S1 to S4 in series, and two clamping diodes from the capacitor midpoint to the nodes '
          'between S1 and S2 and between S3 and S4. A box lists the switch states. On the right, a seven-level staircase rising to 300 volts in steps at 11.5, 28.7 and 57.1 degrees, '
          'with its 305.6 volt fundamental sine.')


# ---- 4.9 grid-tied control loops and the phasor of worked example 2 ----
def f9():
    o = []
    y = 70
    blocks = [(20, 'PV + DC link', '400 V'), (180, 'full bridge', 'unipolar SPWM'), (340, 'LCL filter', 'f_res = 1949 Hz'), (500, 'grid', '230 V, 50 Hz')]
    for x, a, b in blocks:
        o.append(boxt(x, y, 140, 56, [a, b], ACS if a == 'full bridge' else PANEL, AC, 14, bold_first=True))
    for x in (160, 320, 480):
        o.append(L(x, y + 28, x + 18, y + 28, AC, 2.5, arrow='n'))
    o.append(T(660, y + 33, '5 kW', 14, 'start', AC, bold=True))
    # control row
    yc = 200
    o.append(boxt(20, yc, 140, 56, ['DC-link loop', 'sets I* = 30.74 A'], PANEL, NX, 14, bold_first=True))
    o.append(boxt(180, yc, 140, 56, ['current loop', 'i → i*'], PANEL, LV, 14, bold_first=True))
    o.append(boxt(340, yc, 140, 56, ['i* = I* sin θ', 'reference'], PANEL, L2, 14, bold_first=True))
    o.append(boxt(500, yc, 140, 56, ['PLL', 'gives θ'], PANEL, NX, 14, bold_first=True))
    o.append(L(90, y + 56, 90, yc - 4, NX, 2, dash='5 4', arrow='x'))
    o.append(T(98, 168, 'v_dc', 13, 'start', NX))
    o.append(L(570, y + 56, 570, yc - 4, NX, 2, dash='5 4', arrow='x')); o.append(T(578, 168, 'v_g', 13, 'start', NX))
    o.append(L(500, yc + 28, 484, yc + 28, MUT, 2, arrow='m'))
    o.append(P([(160, yc + 40), (170, yc + 40), (170, yc + 76), (410, yc + 76), (410, yc + 60)], MUT, 2))
    o.append(L(340, yc + 28, 324, yc + 28, MUT, 2, arrow='m'))
    o.append(L(250, yc - 2, 250, y + 60, LV, 2, arrow='l')); o.append(T(258, 168, 'duty', 13, 'start', LV))
    o.append(L(410, y + 56, 410, 150, LV, 1.6, dash='4 3')); o.append(L(410, 150, 300, 150, LV, 1.6, dash='4 3')); o.append(L(300, 150, 300, yc - 4, LV, 1.6, dash='4 3', arrow='l'))
    o.append(T(356, 144, 'measured i', 13, 'middle', LV))
    # phasor diagram
    px, py = 80, 380
    s = 1.9
    o.append(L(px, py, px + 230 * s, py, AC, 3, arrow='n')); o.append(T(px + 115 * s, py + 22, 'V_g = 230 V, in phase with I = 21.74 A', 13, fill=AC))
    o.append(L(px + 230 * s, py, px + 230 * s, py - 20.49 * s * 2.2, NX, 3, arrow='x'))
    o.append(T(px + 230 * s + 10, py - 20, 'jXI = 20.49 V', 13, 'start', NX))
    o.append(L(px, py, px + 230 * s, py - 20.49 * s * 2.2, LV, 2.5, arrow='l'))
    o.append(T(px + 40, py - 52, 'V_inv = 230.91 V, δ = 5.09°', 13, 'start', LV, bold=True))
    o.append(T(px + 230 * s + 10, py - 46, '(jXI drawn ×2.2)', 13, 'start', MUT))
    return 430, ''.join(o)


FIG[9] = (f9, 'The worked examples’ 5 kW inverter. Power flows from the 400 V DC link through the bridge and an LCL filter (resonance 1949 Hz) to the 230 V grid. The PLL gives θ, '
              'the DC-link loop sets I* = 30.74 A, and the current loop sets the bridge duty. Below, the inverter must make 230.91 V, 5.09° ahead of the grid, to drive 21.74 A through the 3 mH filter.',
          'Top row: PV and DC link, full bridge, LCL filter and grid, with power arrows. Second row: DC-link loop, current loop, reference generator and PLL, with feedback arrows. '
          'Bottom: a phasor diagram with the grid voltage, a small perpendicular jXI drop, and the inverter voltage at 5.09 degrees.')


spec = make_spec(FIG)


def drop_sources():
    return ['ocw.mit.edu']
