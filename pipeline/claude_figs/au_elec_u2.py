"""Claude's hand-drawn figures for au-elec-u2 (Automotive Electrical and Electronics: ignition, lighting and body electronics),
one per chapter, drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def path(d, c=AC, w=2, fill='none', dash=None):
    ds = f';stroke-dasharray:{dash}' if dash else ''
    return f'<path d="{d}" style="fill:{fill};stroke:{c};stroke-width:{w}{ds};stroke-linejoin:round;stroke-linecap:round"/>'


def earth(x, y, c=INK):
    return L(x, y, x, y + 8, c, 2) + L(x - 10, y + 8, x + 10, y + 8, c, 2) + L(x - 6, y + 13, x + 6, y + 13, c, 2) + L(x - 2, y + 18, x + 2, y + 18, c, 2)


def coil_h(x, y, n, r, c=AC, w=2.5):
    """a winding drawn as n humps along x, starting at (x, y), humps upward"""
    d = f'M{x},{y}' + ''.join(f' a{r},{r} 0 0 1 {2 * r},0' for _ in range(n))
    return path(d, c, w)


def zig(x1, x2, y, c=INK, n=6, a=7):
    pts = [(x1, y)]
    step = (x2 - x1) / (2 * n)
    for i in range(2 * n):
        pts.append((x1 + step * (i + 0.5), y + (a if i % 2 == 0 else -a)))
    pts.append((x2, y))
    return P(pts, c, 2)


# ---- 2.1 battery-and-coil ignition: the circuit, and the dwell of the worked example ----
def f1():
    o = []
    # battery
    o.append(L(40, 70, 40, 104, INK, 2))
    o.append(L(28, 104, 52, 104, INK, 3)); o.append(L(34, 114, 46, 114, INK, 3))
    o.append(L(40, 114, 40, 128, INK, 2)); o.append(earth(40, 128))
    o.append(T(62, 112, 'Battery 12 V', 13, 'start'))
    # feed: switch, ballast
    o.append(L(40, 70, 120, 70, INK, 2))
    o.append(C(124, 70, 4, INK)); o.append(L(126, 68, 156, 56, INK, 2)); o.append(C(160, 70, 4, INK))
    o.append(T(142, 46, 'ignition switch', 13))
    o.append(L(164, 70, 206, 70, INK, 2))
    o.append(zig(206, 262, 70))
    o.append(T(234, 98, 'ballast resistor', 13))
    o.append(L(262, 70, 316, 70, INK, 2))
    # coil
    o.append(R(316, 34, 156, 150, FIGBG, L2, 8, dash='5 4'))
    o.append(T(394, 26, 'ignition coil', 13, bold=True))
    o.append(L(330, 112, 458, 112, MUT, 4))
    o.append(T(394, 128, 'iron core', 13, fill=MUT))
    o.append(coil_h(334, 100, 4, 8, AC, 3))
    o.append(T(366, 80, 'primary', 13, fill=AC))
    o.append(coil_h(402, 100, 8, 3.5, LV, 1.8))
    o.append(T(430, 80, 'secondary', 13, fill=LV))
    o.append(L(316, 70, 334, 70, INK, 2)); o.append(L(334, 70, 334, 100, INK, 2))
    o.append(L(398, 100, 398, 150, INK, 2)); o.append(L(398, 150, 398, 200, INK, 2))
    o.append(L(458, 100, 458, 70, LV, 2)); o.append(L(458, 70, 520, 70, LV, 2.5))
    # contact breaker and capacitor
    o.append(L(398, 200, 380, 200, INK, 2))
    o.append(C(376, 200, 4, INK)); o.append(L(376, 200, 340, 212, INK, 2.5)); o.append(C(372, 214, 4, INK))
    o.append(L(372, 218, 372, 240, INK, 2)); o.append(earth(372, 240))
    o.append(T(316, 196, 'points', 13, 'end', bold=True))
    o.append(T(316, 214, 'opened by cam', 13, 'end', fill=MUT))
    o.append(L(398, 200, 440, 200, NX, 2)); o.append(L(440, 200, 440, 214, NX, 2))
    o.append(L(428, 214, 452, 214, NX, 3)); o.append(L(428, 222, 452, 222, NX, 3))
    o.append(L(440, 222, 440, 240, NX, 2)); o.append(earth(440, 240, NX))
    o.append(T(462, 222, 'capacitor 0.2–0.3 µF', 13, 'start', fill=NX))
    # distributor and plugs
    o.append(f'<circle cx="560" cy="110" r="40" style="fill:{PANEL};stroke:{LV};stroke-width:2"/>')
    o.append(L(520, 70, 560, 70, LV, 2.5)); o.append(L(560, 70, 560, 110, LV, 2.5))
    o.append(L(560, 110, 586, 96, LV, 3, arrow='l'))
    for a in (45, 135, 225, 315):
        x, y = 560 + 40 * math.cos(math.radians(a)), 110 - 40 * math.sin(math.radians(a))
        o.append(C(x, y, 4, LV))
    o.append(T(560, 168, 'distributor', 13, bold=True))
    o.append(T(560, 186, 'rotor sends HT', 13, fill=MUT))
    o.append(T(560, 202, 'in order 1-3-4-2', 13, fill=MUT))
    o.append(L(588, 82, 648, 82, LV, 2)); o.append(L(648, 82, 648, 98, LV, 2))
    o.append(R(640, 98, 16, 22, PANEL, INK, 3))
    o.append(L(648, 120, 648, 128, INK, 2)); o.append(L(654, 132, 662, 132, INK, 2))
    o.append(T(672, 112, 'plug', 13, 'start'))
    o.append(L(658, 134, 658, 146, INK, 2)); o.append(earth(658, 146))
    o.append(T(648, 70, 'to 4 plugs', 13, fill=MUT))
    # dwell strip of the worked example
    x0, W = 70, 600
    fx = lin(0, 180, x0, x0 + W)
    o.append(T(16, 290, 'One spark interval at 3000 rpm: 180° of crank, 10 ms', 14, 'start', bold=True))
    o.append(R(fx(0), 304, fx(108) - fx(0), 34, ACS, AC, 4))
    o.append(T((fx(0) + fx(108)) / 2, 326, 'points closed: 108° = 6 ms', 14, bold=True))
    o.append(R(fx(108), 304, fx(180) - fx(108), 34, FIGBG, L2, 4, dash='5 4'))
    o.append(T((fx(108) + fx(180)) / 2, 326, 'open: 72° = 4 ms', 14))
    o.append(L(fx(108), 296, fx(108), 352, LV, 2.5))
    o.append(T(fx(108), 370, 'points open → field collapses → spark', 13, fill=LV, bold=True))
    o.append(xaxis(x0, x0 + W, 386, [0, 45, 90, 135, 180], fx, None, lambda v: f'{v}°'))
    return 420, ''.join(o)


# ---- 2.2 firing voltage against gap, with the coil of the worked example ----
def f2():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 300
    fx = lin(0.5, 1.2, x0, x1); fy = lin(0, 40, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2], [0, 10, 20, 30, 40], fx, fy,
                  'plug gap g (mm)', 'voltage (kV)', lambda v: f'{v:.1f}', str))
    full = lambda g: 10 + 22 * g
    light = lambda g: 5 + 12 * g
    o.append(L(fx(0.5), fy(full(0.5)), fx(1.2), fy(full(1.2)), NX, 2.5))
    o.append(L(fx(0.5), fy(light(0.5)), fx(1.2), fy(light(1.2)), AC, 2.5))
    o.append(L(fx(0.5), fy(25), fx(1.2), fy(25), LV, 2.5, dash='8 5'))
    o.append(Tb(fx(1.19), fy(39.5), 'needed at full load: 10 + 22g', 13, 'end', NX, True))
    o.append(Tb(fx(1.19), fy(light(1.2)) + 40, 'needed at light load: 5 + 12g', 13, 'end', AC, True))
    o.append(Tb(fx(0.51), fy(25) - 10, 'coil gives 25 kV', 13, 'start', LV, True))
    # 0.9 mm point
    o.append(L(fx(0.9), fy(full(0.9)), fx(0.9), fy(25), NX, 2, dash='3 3'))
    o.append(C(fx(0.9), fy(full(0.9)), 6, NX))
    o.append(Tb(fx(0.9) - 10, fy(full(0.9)) - 12, '0.9 mm needs 29.8 kV', 13, 'end', NX))
    o.append(Tb(fx(0.9) + 10, fy(27.4) + 4, 'short by 4.8 kV: misfire', 13, 'start', NX))
    o.append(C(fx(0.9), fy(light(0.9)), 6, AC))
    o.append(Tb(fx(0.9) - 4, fy(light(0.9)) + 34, '15.8 kV: fires', 13, 'end', AC))
    # largest gap
    g = 15 / 22
    o.append(C(fx(g), fy(25), 6, LV))
    o.append(L(fx(g), fy(25), fx(g), y1, LV, 1.5, dash='3 3'))
    o.append(Tb(fx(g) + 8, fy(4), 'largest gap at full load: 0.68 mm', 13, 'start', LV, True))
    return 350, ''.join(o)


# ---- 2.3 constant dwell against constant energy (worked example 2) ----
def f3():
    o = []
    # the programmed-ignition chain
    xs = [16, 186, 356, 476, 596]
    labs = [['sensors', 'crank, MAP, knock'], ['ECU', 'map + corrections'], ['igniter'], ['coil'], ['plugs']]
    ws = [150, 150, 100, 100, 108]
    for x, w, lb in zip(xs, ws, labs):
        o.append(boxt(x, 30, w, 56, lb, ACS if lb[0] == 'ECU' else PANEL, AC, 13, True))
    for a, b in zip(xs[:-1], xs[1:]):
        i = xs.index(a)
        o.append(L(a + ws[i] + 2, 58, b - 4, 58, AC, 2, arrow='n'))
    o.append(T(408, 108, 'dwell pulse: rising edge starts current, falling edge fires', 13, 'middle', MUT))
    # bars on 0..180 crank degrees
    x0, W = 200, 490
    fx = lin(0, 180, x0, x0 + W)
    rows = [(160, '1000 rpm', 'constant dwell', 108, '108° = 18 ms', AC, ACS),
            (204, '', 'constant energy', 18, '18° = 3 ms', LV, LVS),
            (270, '6000 rpm', 'constant dwell', 108, '108° = 3 ms', AC, ACS),
            (314, '', 'constant energy', 108, '108° = 3 ms', LV, LVS)]
    o.append(T(16, 140, 'Dwell in one spark interval (180° of crank)', 14, 'start', bold=True))
    for y, sp, name, deg, lab, c, cs in rows:
        if sp: o.append(T(16, y + 44, sp, 14, 'start', bold=True))
        o.append(T(x0 - 8, y + 22, name, 13, 'end', c))
        o.append(R(x0, y + 4, W, 28, FIGBG, L2, 4, dash='4 4'))
        o.append(R(fx(180 - deg), y + 4, fx(180) - fx(180 - deg), 28, cs, c, 4))
        lx = fx(180 - deg) - 8 if deg < 60 else (fx(180 - deg) + fx(180)) / 2
        o.append(T(lx, y + 23, lab, 13, 'end' if deg < 60 else 'middle', INK, True))
    o.append(T(fx(180), 372, 'spark', 13, 'middle', NX, True))
    o.append(L(fx(180), 158, fx(180), 356, NX, 2.5))
    o.append(xaxis(x0, x0 + W, 356, [0, 45, 90, 135], fx, None, lambda v: f'{v}°'))
    o.append(T(16, 398, 'Constant energy keeps 3 ms of dwell, so its angle grows from 18° to 108°.', 13, 'start', MUT))
    return 412, ''.join(o)


# ---- 2.4 waste-spark firing over one 720° cycle at 4000 rpm ----
def f4():
    o = []
    x0, W = 150, 530
    fx = lin(0, 720, x0, x0 + W)
    o.append(T(x0 + W / 2, 30, 'One 720° cycle at 4000 rpm = 30 ms (firing order 1-3-4-2)', 14, 'middle', INK, True))
    lanes = [(80, 'coil 1 & 4', AC, ACS, [(0, '1', '4'), (360, '4', '1')]),
             (190, 'coil 2 & 3', LV, LVS, [(180, '3', '2'), (540, '2', '3')])]
    for y, name, c, cs, fires in lanes:
        o.append(T(16, y + 34, name, 14, 'start', c, True))
        o.append(L(x0, y + 30, x0 + W, y + 30, L2, 1.5))
        for a, comp, exh in fires:
            X = fx(a)
            o.append(L(X, y, X, y + 60, c, 3.5))
            o.append(R(X + 6, y + 2, 104, 26, cs, c, 4))
            o.append(T(X + 58, y + 20, f'{comp}: compression', 13, 'middle', INK, True))
            o.append(R(X + 6, y + 34, 104, 26, FIGBG, L2, 4, dash='4 3'))
            o.append(T(X + 58, y + 52, f'{exh}: exhaust', 13, 'middle', MUT))
    o.append(xaxis(x0, x0 + W, 280, [0, 180, 360, 540, 720], fx, None, lambda v: f'{v}°'))
    for v, ms in ((0, '0'), (180, '7.5'), (360, '15'), (540, '22.5'), (720, '30 ms')):
        o.append(T(fx(v), 318, ms, 13, 'middle', MUT))
    o.append(T(16, 300, 'crank angle', 13, 'start', MUT))
    o.append(T(16, 318, 'time', 13, 'start', MUT))
    o.append(T(16, 350, 'Each coil fires once per revolution (66.7 times a second) and sparks both of its plugs.', 13, 'start'))
    return 366, ''.join(o)


# ---- 2.5 efficacy of the light sources, with the two lamps of the worked example ----
def f5():
    o = []
    x0, x1 = 190, 690
    fx = lin(0, 120, x0, x1)
    o.append(xaxis(x0, x1, 300, [0, 20, 40, 60, 80, 100, 120], fx, 'luminous efficacy (lm/W)', str))
    rows = [(50, 'tungsten', 'incandescence', 10, 15, None, AC),
            (110, 'halogen', 'halogen cycle', 20, 30, 27.3, AC),
            (170, 'HID xenon', 'gas discharge', 80, 90, None, NX),
            (230, 'LED', 'electroluminescence', 90, 110, 100, LV)]
    for v in (20, 40, 60, 80, 100, 120):
        o.append(L(fx(v), 36, fx(v), 300, 'var(--line)', 1))
    for y, name, how, a, b, ex, c in rows:
        o.append(T(16, y + 14, name, 14, 'start', INK, True))
        o.append(T(16, y + 32, how, 13, 'start', MUT))
        o.append(R(fx(a), y, fx(b) - fx(a), 30, PANEL, c, 4))
        o.append(T(fx(b) + 8, y + 20, f'{a}–{b}', 13, 'start', c))
        if ex:
            o.append(C(fx(ex), y + 15, 7, c))
    o.append(Tb(fx(27.3) + 4, 102, '55 W, 1500 lm → 27.3 lm/W', 13, 'start', AC, True))
    o.append(Tb(fx(100) - 4, 222, '20 W, 2000 lm → 100 lm/W', 13, 'end', LV, True))
    return 350, ''.join(o)


# ---- 2.6 the lamp circuit of the worked example ----
def f6():
    o = []
    # battery and feed
    o.append(L(40, 60, 40, 92, INK, 2)); o.append(L(28, 92, 52, 92, INK, 3)); o.append(L(34, 102, 46, 102, INK, 3))
    o.append(L(40, 102, 40, 116, INK, 2)); o.append(earth(40, 116))
    o.append(T(40, 160, 'battery', 13)); o.append(T(40, 176, '13.2 V', 13))
    o.append(L(40, 60, 96, 60, INK, 2))
    o.append(R(96, 50, 52, 20, PANEL, NX, 4)); o.append(T(122, 40, 'fuse 15 A', 13, 'middle', NX, True))
    o.append(L(148, 60, 200, 60, INK, 2))
    o.append(C(204, 60, 4, INK)); o.append(L(206, 58, 232, 46, INK, 2)); o.append(C(236, 60, 4, INK))
    o.append(T(220, 88, 'light switch', 13))
    o.append(L(240, 60, 300, 60, INK, 2))
    # bus and branches
    o.append(L(300, 60, 300, 330, INK, 2.5))
    o.append(T(300, 350, 'total 10.08 A', 14, 'middle', NX, True))
    br = [(80, 'headlamps 2 × 55 W', '8.33 A', AC), (150, 'tail lamps 2 × 5 W', '0.76 A', LV),
          (220, 'plate lamps 2 × 5 W', '0.76 A', LV), (290, 'instrument lamps 3 W', '0.23 A', LV)]
    for y, name, amp, c in br:
        o.append(L(300, y, 520, y, c, 2.5 if c == AC else 2))
        o.append(f'<circle cx="540" cy="{y}" r="16" style="fill:{PANEL};stroke:{c};stroke-width:2"/>')
        o.append(L(529, y - 11, 551, y + 11, c, 1.6)); o.append(L(529, y + 11, 551, y - 11, c, 1.6))
        o.append(L(556, y, 600, y, INK, 2)); o.append(earth(600, y - 8))
        o.append(T(318, y - 10, name, 13, 'start'))
        o.append(T(318, y + 20, amp, 13, 'start', c, True))
    o.append(T(640, 56, 'earth', 13, 'middle', MUT)); o.append(T(640, 72, 'return', 13, 'middle', MUT))
    o.append(T(16, 214, 'lamps in', 13, 'start', MUT)); o.append(T(16, 230, 'parallel:', 13, 'start', MUT))
    o.append(T(16, 246, 'currents add', 13, 'start', MUT))
    o.append(T(360, 384, '133 W ÷ 13.2 V = 10.08 A; with 25% margin 12.6 A → 15 A fuse', 13, 'middle'))
    return 400, ''.join(o)


# ---- 2.7 levelling and swivel (worked example) ----
def f7():
    o = []
    # side view: body tilted nose-up about the front axle (angle exaggerated)
    o.append(T(16, 26, 'Side view (angle exaggerated)', 14, 'start', INK, True))
    o.append(L(16, 150, 704, 150, L2, 1.5))
    fa, ra = (330, 136), (90, 136)
    o.append(f'<circle cx="{fa[0]}" cy="{fa[1]}" r="14" style="fill:{PANEL};stroke:{INK};stroke-width:2"/>')
    o.append(f'<circle cx="{ra[0]}" cy="{ra[1] + 4}" r="14" style="fill:{PANEL};stroke:{INK};stroke-width:2"/>')
    o.append(path('M60,124 L60,92 L140,86 L190,58 L290,54 L340,78 L370,84 L372,112 Z', AC, 2, PANEL))
    o.append(path('M60,120 L60,88 L140,80 L190,50 L290,48 L340,74 L370,82 L372,110', L2, 1.5, 'none', '5 4'))
    o.append(T(60, 50, 'rear down 20 mm', 13, 'start', NX))
    o.append(L(90, 166, 330, 166, INK, 1.5)); o.append(L(90, 160, 90, 172, INK, 1.5)); o.append(L(330, 160, 330, 172, INK, 1.5))
    o.append(T(210, 184, 'wheelbase 2.5 m', 13))
    lx, ly = 368, 96
    o.append(C(lx, ly, 5, LV))
    o.append(L(lx, ly, 700, ly + 22, LV, 2, dash='6 4'))
    o.append(L(lx, ly, 700, ly + 6, NX, 2.5))
    o.append(T(700, ly + 40, 'aim −1.0%', 13, 'end', LV))
    o.append(T(700, ly - 6, 'loaded: −0.2%', 13, 'end', NX, True))
    o.append(T(540, 66, 'tilt 0.46° → +0.20 m at 25 m', 13, 'middle', NX, True))
    # top view: swivel
    o.append(T(16, 230, 'Top view: swivel', 14, 'start', INK, True))
    o.append(R(60, 260, 150, 70, PANEL, AC, 10))
    o.append(T(135, 300, 'car', 13, 'middle', MUT))
    o.append(C(210, 272, 5, LV))
    o.append(L(210, 272, 470, 272, L2, 2, dash='6 4'))
    a = math.radians(13.5)
    o.append(L(210, 272, 210 + 270 * math.cos(a), 272 + 270 * math.sin(a), LV, 2.5, arrow='l'))
    a2 = math.radians(15)
    o.append(L(210, 272, 210 + 270 * math.cos(a2), 272 + 270 * math.sin(a2), NX, 1.5, dash='3 3'))
    o.append(T(480, 276, 'straight ahead', 13, 'start', MUT))
    o.append(T(486, 345, '13.5° at 90° of steering', 13, 'start', LV, True))
    o.append(T(486, 366, 'cap 15° (reached at 100°)', 13, 'start', NX))
    o.append(T(486, 388, 'swivel = 0.15 × steering-wheel angle', 13, 'start', MUT))
    return 404, ''.join(o)


# ---- 2.8 speed from wheel pulses (worked example 1) ----
def f8():
    o = []
    cx, cy, r = 110, 150, 70
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:{PANEL};stroke:{INK};stroke-width:2.5"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="30" style="fill:{FIGBG};stroke:{L2};stroke-width:2"/>')
    for a in (0, 90, 180, 270):
        x, y = cx + 30 * math.cos(math.radians(a)), cy - 30 * math.sin(math.radians(a))
        o.append(f'<rect x="{x - 5:.1f}" y="{y - 5:.1f}" width="10" height="10" style="fill:{AC}"/>')
    o.append(R(cx + 26, cy - 66, 30, 22, ACS, AC, 3))
    o.append(T(cx + 64, cy - 72, 'sensor', 13, 'start', AC, True))
    o.append(T(cx, cy + 96, 'C = 1.90 m', 13, 'middle', INK, True))
    o.append(T(cx, cy + 114, '4 pulses per turn', 13, 'middle', MUT))
    o.append(T(cx, cy + 132, 'd = 0.475 m each', 13, 'middle', MUT))
    o.append(L(cx + 56, cy - 55, 248, 110, AC, 1.5, dash='4 3'))
    # pulse train and gate
    x0, x1 = 250, 690
    fx = lin(0, 0.5, x0 + 10, x1 - 10)
    o.append(R(x0, 60, x1 - x0, 110, FIGBG, L2, 6))
    o.append(T((x0 + x1) / 2, 50, 'gate T = 0.5 s at a true 100 km/h', 14, 'middle', INK, True))
    per = 1 / 58.48
    pts = [(fx(0), 150)]
    t = 0.004
    n = 0
    while t + per * 0.4 < 0.5:
        pts += [(fx(t), 150), (fx(t), 90), (fx(t + per * 0.4), 90), (fx(t + per * 0.4), 150)]
        t += per; n += 1
    pts.append((fx(0.5), 150))
    o.append(P(pts, AC, 1.6))
    o.append(T((x0 + x1) / 2, 196, f'{n} whole pulses counted (58.48 pulses/s × 0.5 s = 29.24)', 13, 'middle'))
    o.append(boxt(x0, 220, x1 - x0, 62, ['v = 3.6 × n × d ÷ T = 3.6 × 29 × 0.475 ÷ 0.5 = 99.2 km/h',
                                          'one pulse = 3.42 km/h, so the part pulse costs 0.8 km/h'], ACS, AC, 13))
    return 300, ''.join(o)


# ---- 2.9 wiper motor with three brushes and park switch; the sweep of the worked example ----
def f9():
    o = []
    # +12 V rail
    o.append(T(16, 34, '+12 V (fused)', 13, 'start', NX, True))
    o.append(L(40, 44, 40, 330, NX, 2.5))
    # stalk contacts HIGH and LOW
    for y, lab in ((80, 'HIGH'), (150, 'LOW')):
        o.append(L(40, y, 96, y, NX, 2)); o.append(C(100, y, 4, INK)); o.append(L(102, y - 2, 128, y - 12, INK, 2)); o.append(C(132, y, 4, INK))
        o.append(T(116, y - 18, 'stalk ' + lab, 13, 'middle', INK, True))
    # motor and brushes
    mx, my = 330, 190
    o.append(f'<circle cx="{mx}" cy="{my}" r="46" style="fill:{PANEL};stroke:{AC};stroke-width:2.5"/>')
    o.append(T(mx, my + 6, 'M', 16, 'middle', AC, True))
    o.append(R(mx - 7, my - 62, 14, 16, ACS, AC, 2)); o.append(R(mx + 24, my - 56, 14, 16, ACS, AC, 2)); o.append(R(mx - 7, my + 46, 14, 16, ACS, AC, 2))
    o.append(L(136, 80, mx + 31, 80, INK, 2)); o.append(L(mx + 31, 80, mx + 31, my - 56, INK, 2))
    o.append(T(mx + 44, 76, 'high-speed brush', 13, 'start', AC))
    o.append(L(136, 150, mx - 30, 150, INK, 2)); o.append(L(mx - 30, 150, mx - 30, my - 70, INK, 2)); o.append(L(mx - 30, my - 70, mx, my - 70, INK, 2)); o.append(L(mx, my - 70, mx, my - 62, INK, 2))
    o.append(T(mx - 40, 112, 'low-speed brush', 13, 'end', AC))
    o.append(L(mx, my + 62, mx, 268, INK, 2)); o.append(earth(mx, 268))
    o.append(T(mx + 14, 262, 'common brush', 13, 'start', AC))
    # stalk OFF joins the low brush to the park switch
    o.append(L(200, 150, 200, 200, INK, 2)); o.append(C(200, 204, 4, INK)); o.append(L(202, 206, 214, 228, INK, 2)); o.append(C(200, 236, 4, INK))
    o.append(T(190, 224, 'stalk OFF', 13, 'end', INK, True))
    o.append(L(200, 240, 200, 290, INK, 2))
    # park switch: changeover, run contact to +12 V, park contact to earth
    o.append(C(200, 294, 4, LV)); o.append(L(200, 294, 160, 322, LV, 3))
    o.append(C(156, 326, 4, INK)); o.append(L(156, 326, 40, 326, NX, 2))
    o.append(C(244, 326, 4, INK)); o.append(L(244, 330, 244, 344, INK, 2)); o.append(earth(244, 344))
    o.append(T(140, 348, 'run', 13, 'end', NX)); o.append(T(262, 334, 'park: armature shorted', 13, 'start', INK))
    o.append(T(200, 382, 'park switch (cam in the gearbox)', 13, 'middle', LV, True))
    # sweep of the worked example
    px, py, rr = 590, 320, 100
    o.append(T(590, 130, 'arm 500 mm, sweep 120°', 13, 'middle', INK, True))
    a1, a2 = math.radians(30), math.radians(150)
    o.append(path(f'M{px + rr * math.cos(a1):.1f},{py - rr * math.sin(a1):.1f} A{rr},{rr} 0 0 0 {px + rr * math.cos(a2):.1f},{py - rr * math.sin(a2):.1f}', LV, 2.5))
    o.append(L(px, py, px + rr * math.cos(a1), py - rr * math.sin(a1), INK, 2))
    o.append(L(px, py, px + rr * math.cos(a2), py - rr * math.sin(a2), INK, 2))
    o.append(C(px, py, 5, INK))
    o.append(T(590, 156, '45 wipes a minute', 13, 'middle', MUT))
    o.append(T(590, 176, 'average tip 1.57 m/s', 13, 'middle', LV, True))
    o.append(T(590, 196, 'peak 2.47 m/s mid-sweep', 13, 'middle', LV))
    o.append(T(590, 344, 'pivot', 13, 'middle', MUT))
    return 396, ''.join(o)


FIG = {
    1: (f1, 'The primary and secondary circuits share one iron core. In the worked example the points stay closed for 108° of every 180°, and the spark comes when they open.',
        'Battery-and-coil ignition circuit with ballast resistor, contact breaker and capacitor, distributor and plug, and a dwell strip of 108 degrees closed and 72 degrees open in a 180 degree spark interval'),
    2: (f2, 'The voltage the plug needs rises with the gap and is far higher at full load. The worked example\'s 25 kV coil fires a 0.9 mm gap at light load but is 4.8 kV short at full load; 0.68 mm is the widest gap it can fire then.',
        'Firing voltage against plug gap: full-load line 10 plus 22 g, light-load line 5 plus 12 g, coil output 25 kV, 29.8 kV needed at 0.9 mm and a largest gap of 0.68 mm'),
    3: (f3, 'The ECU turns sensor signals into a dwell pulse for the igniter. Below, the worked examples: constant dwell keeps the angle, so its time falls to 3 ms at 6000 rpm; constant energy keeps 3 ms, so its angle grows from 18° to 108°.',
        'Block chain of programmed ignition, then dwell bars in a 180 degree spark interval for constant-dwell and constant-energy systems at 1000 and 6000 rpm'),
    4: (f4, 'Each line is one coil firing. Coil 1 & 4 fires at 0° and 360°, coil 2 & 3 at 180° and 540°; at every firing one of the pair is on compression and the other on exhaust.',
        'Waste-spark firing over a 720 degree cycle at 4000 rpm: coil 1 and 4 at 0 and 360 degrees, coil 2 and 3 at 180 and 540 degrees, with compression and exhaust cylinders marked and times of 0, 7.5, 15, 22.5 and 30 ms'),
    5: (f5, 'Each bar is the usual range of a source\'s efficacy; the dots are the two lamps of the worked example. The LED gives almost four times the light per watt of the halogen bulb.',
        'Bar chart of luminous efficacy: tungsten 10 to 15, halogen 20 to 30, HID 80 to 90, LED 90 to 110 lumens per watt, with the halogen lamp at 27.3 and the LED at 100'),
    6: (f6, 'All the lamps of the worked example hang in parallel from one fused feed, and each returns through the body to earth. Their currents add to 10.08 A, so a 15 A fuse protects the wire.',
        'Lamp circuit: battery, 15 A fuse and light switch feed four parallel lamp branches, headlamps 8.33 A, tail 0.76 A, plate 0.76 A and instruments 0.23 A, each to earth, total 10.08 A'),
    7: (f7, 'A 20 mm drop at the rear tilts the whole body 0.46° about the front axle, lifting the cut-off 0.20 m at 25 m; the level motor tilts the lamp back down. Seen from above, the swivel turns the beam 13.5° for 90° of steering and stops at 15°.',
        'Side view of a car with the rear 20 mm down over a 2.5 m wheelbase and the beam aim changing from minus 1.0 to minus 0.2 percent, and a top view of the headlamp beam swivelled 13.5 degrees with a 15 degree cap'),
    8: (f8, 'Four magnets on the wheel give a pulse every 0.475 m. At 100 km/h the gate catches 29 whole pulses, so the cluster shows 99.2 km/h.',
        'Wheel with four magnets and a sensor, a pulse train of 29 pulses in a 0.5 second gate, and the speed calculation giving 99.2 km/h'),
    9: (f9, 'The stalk switch feeds the low-speed or the high-speed brush; in OFF the park cam keeps the motor running until the blade is down, then shorts it to brake. Right: the worked example\'s 500 mm arm sweeping 120°.',
        'Wiper motor circuit with stalk switch, low-speed, high-speed and common brushes and a park cam switch, and a 500 mm wiper arm sweeping 120 degrees'),
}

spec = make_spec(FIG)
