"""Claude's hand-drawn figures for c-iot-u2 (Internet of Things, unit 2: sensors, actuators and embedded hardware),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


# ---- 2.1 a 4-20 mA temperature transmitter ----
def f1():
    x0, x1, y0, y1 = 70, 440, 40, 330
    fx = lambda t: x0 + t / 100 * (x1 - x0)
    fy = lambda i: y1 - i / 22 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 20, 40, 60, 80, 100], [0, 4, 8, 12, 16, 20], fx, fy, 'temperature (°C)', 'output (mA)')]
    o.append(L(fx(0), fy(4), fx(100), fy(20), AC, 3))
    o.append(C(fx(0), fy(4), 5, AC)); o.append(C(fx(100), fy(20), 5, AC))
    o.append(Tb(fx(0) + 10, fy(4) + 20, '0 °C → 4 mA (live zero)', 13, 'start'))
    o.append(Tb(fx(100) - 6, fy(20) - 12, '100 °C → 20 mA', 13, 'end'))
    # 12 mA read-back
    o.append(L(x0, fy(12), fx(50), fy(12), NX, 2, '6 4')); o.append(L(fx(50), fy(12), fx(50), y1, NX, 2, '6 4', arrow='x'))
    o.append(C(fx(50), fy(12), 6, NX))
    o.append(Tb(fx(50) + 12, fy(6), '12.00 mA → (12 − 4) ÷ 0.16', 13, 'start', NX, True)); o.append(Tb(fx(50) + 12, fy(6) + 19, '= 50.0 °C', 13, 'start', NX, True))
    # zoom box around 60 °C
    o.append(R(fx(60) - 8, fy(13.64) - 8, 16, 16, 'none', LV, 3, 1.8))
    o.append(L(fx(60) + 8, fy(13.64) - 4, 486, 112, LV, 1.5, '4 4'))
    bx, by, bw, bh = 486, 44, 222, 200
    o.append(R(bx, by, bw, bh, PANEL, LV, 8, 1.8))
    o.append(T(bx + bw / 2, by + 22, 'zoom at 60 °C', 13, fill=LV, bold=True))
    zy = lambda i: by + 170 - (i - 13.56) / 0.16 * 130
    o.append(L(bx + 20, zy(13.60), bx + bw - 20, zy(13.60), AC, 2, arrow='n'))
    o.append(L(bx + bw - 20, zy(13.68), bx + 20, zy(13.68), NX, 2, arrow='x'))
    o.append(T(bx + 24, zy(13.60) + 20, 'rising 13.60 mA', 13, 'start', AC, True))
    o.append(T(bx + 24, zy(13.68) - 10, 'falling 13.68 mA', 13, 'start', NX, True))
    o.append(T(bx + bw / 2, by + 192, 'gap 0.08 mA ÷ 0.16 = 0.5 °C', 13, bold=True))
    o.append(T(486, 278, 'span = 20 − 4 = 16 mA', 14, 'start'))
    o.append(T(486, 300, 'sensitivity = 16 ÷ 100', 14, 'start'))
    o.append(T(486, 320, '= 0.16 mA per °C', 14, 'start', AC, True))
    return 386, ''.join(o)
FIG[1] = (f1, 'The transmitter maps 0–100 °C onto 4–20 mA, a span of 16 mA and 0.16 mA/°C, so 12.00 mA reads 50.0 °C; at 60 °C the rising and falling readings differ by 0.08 mA, a hysteresis of 0.5 °C.',
          'A straight line from 4 mA at 0 degrees to 20 mA at 100 degrees, with a dashed read-back from 12 mA down to 50 degrees, and a zoom box at 60 degrees showing the rising reading 13.60 mA and the falling reading 13.68 mA.')


# ---- 2.2 stepper motor on a lead screw ----
def f2():
    o = []
    cx, cy, r = 120, 150, 86
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:var(--panel);stroke:{AC};stroke-width:2"/>')
    for i in range(200):
        a = math.radians(i * 1.8 - 90)
        r1 = r - (10 if i % 25 == 0 else 5)
        o.append(L(cx + r1 * math.cos(a), cy + r1 * math.sin(a), cx + r * math.cos(a), cy + r * math.sin(a), AC if i % 25 == 0 else L2, 1.2))
    a1, a2 = math.radians(-90), math.radians(-90 + 1.8 * 6)
    o.append(f'<path d="M{cx},{cy} L{cx + r * math.cos(a1):.1f},{cy + r * math.sin(a1):.1f} A{r},{r} 0 0 1 {cx + r * math.cos(a2):.1f},{cy + r * math.sin(a2):.1f} Z" style="fill:var(--next-soft);stroke:{NX};stroke-width:1.5"/>')
    o.append(C(cx, cy, 6, AC))
    o.append(T(cx, cy + 34, '200 steps', 14, bold=True)); o.append(T(cx, cy + 52, 'per turn', 13, fill=MUT))
    o.append(T(cx, 40, '360° ÷ 1.8° = 200', 14, bold=True))
    o.append(T(cx, 262, 'one step = 1.8° (wedge drawn 6× wider)', 13, fill=MUT))
    # lead screw
    sx0, sx1, sy = 260, 690, 110
    o.append(R(sx0, sy - 12, sx1 - sx0, 24, PANEL, L2, 4, 1.5))
    for i in range(22):
        x = sx0 + 8 + i * 19.5
        o.append(L(x, sy - 12, x + 10, sy + 12, L2, 1.5))
    o.append(R(430, sy - 24, 60, 48, ACS, AC, 4))
    o.append(T(460, sy + 5, 'nut', 13, bold=True))
    o.append(L(400, sy - 40, 520, sy - 40, AC, 2, arrow='n'))
    o.append(T(460, sy - 48, 'one turn moves the nut 2 mm', 13, fill=AC, bold=True))
    o.append(T(sx0, sy + 40, 'lead screw, pitch 2 mm', 13, 'start', MUT))
    # one step split into microsteps
    rx0, rx1, ry = 280, 680, 220
    o.append(T(rx0, 178, 'one full step: 2 mm ÷ 200 = 0.01 mm = 10 µm', 14, 'start', bold=True))
    o.append(R(rx0, ry - 16, rx1 - rx0, 32, NXS, NX, 4, 1.5))
    for i in range(1, 8):
        x = rx0 + i * (rx1 - rx0) / 8
        o.append(L(x, ry - 16, x, ry + 16, NX, 1.5))
    o.append(T(rx0 + (rx1 - rx0) / 16, ry + 5, '1.25', 13, bold=True))
    o.append(T(rx0, ry + 40, '1/8 microstep: 1.8° ÷ 8 = 0.225°, and 10 µm ÷ 8 = 1.25 µm', 14, 'start'))
    o.append(T(rx0, ry + 62, '(1,600 microsteps a turn: 2,000 µm ÷ 1,600 = 1.25 µm)', 13, 'start', MUT))
    return 300, ''.join(o)
FIG[2] = (f2, 'A 1.8° stepper makes 200 steps a turn and a 2 mm lead screw moves 2 mm a turn, so one full step moves the nut 10 µm; 1/8 microstepping splits that into 0.225° and 1.25 µm.',
          'A motor disc ringed with 200 step marks and one highlighted 1.8 degree wedge; a lead screw whose nut moves 2 mm per turn; a bar for one 10 micrometre step divided into eight microsteps of 1.25 micrometres.')


# ---- 2.3 sensor node duty cycle and battery life ----
def f3():
    o = [T(20, 24, 'One 60 s cycle (not to scale: the burst is 0.2 s)', 14, 'start', MUT)]
    x0, x1, yb, yt = 60, 690, 160, 50
    o.append(L(x0, yb, x1, yb, L2, 1.5)); o.append(L(x0, yt - 8, x0, yb, L2, 1.5))
    o.append(T(x0 - 8, yt + 5, '8 mA', 13, 'end', MUT)); o.append(T(x0 - 8, yb + 5, '0', 13, 'end', MUT))
    o.append(R(x0 + 4, yt, 22, yb - yt, ACS, AC, 2, 2))
    o.append(T(x0 + 36, yt + 20, 'awake: 8 mA for 200 ms (0.003333 of the time)', 14, 'start', AC, True))
    o.append(R(x0 + 26, yb - 10, x1 - x0 - 30, 10, LVS, LV, 2, 1.5))
    o.append(Tb(x0 + 340, yb - 22, 'asleep: 3 µA = 0.003 mA for 59.8 s', 14, 'middle', LV, True))
    o.append(T(x1 - 4, yb + 20, '60 s', 13, 'end', MUT))
    o.append(T(20, 214, 'Average current = each current × its share of the time', 15, 'start', bold=True))
    s = 560 / 0.0297
    o.append(R(40, 228, 0.02667 * s, 34, ACS, AC, 3))
    o.append(T(40 + 0.02667 * s / 2, 250, '8 × 0.003333 = 0.02667 mA', 14, bold=True))
    o.append(R(40 + 0.02667 * s, 228, 0.00299 * s, 34, LVS, LV, 3))
    o.append(L(40 + 0.02966 * s - 30, 276, 40 + 0.02966 * s - 30, 266, LV, 1.5))
    o.append(T(40 + 0.02966 * s - 30, 292, 'sleep 0.00299 mA', 13, 'middle', LV, True))
    o.append(brace(40, 40 + 0.02966 * s, 302, INK))
    o.append(T(40 + 0.02966 * s / 2, 326, 'total ≈ 0.0297 mA', 14, bold=True))
    o.append(boxt(20, 344, 680, 56, ['usable 1,000 × 0.80 = 800 mAh;  800 ÷ 0.02966 = 26,975 h', '26,975 ÷ 24 ≈ 1,124 days ≈ 3.1 years'], NXS, NX, 14))
    return 414, ''.join(o)
FIG[3] = (f3, 'The node is awake at 8 mA for 0.2 s of every 60 s and asleep at 3 µA otherwise, an average of 0.0297 mA, nine tenths of it from the burst; 800 mAh of usable charge then lasts about 26,975 h, or 3.1 years.',
          'A one-minute current sketch with a narrow 8 mA burst and a long 3 microamp floor; a bar splitting the 0.0297 mA average into 0.02667 mA from the burst and 0.00299 mA from sleep; a box giving 26,975 hours, 1,124 days, 3.1 years.')


# ---- 2.4 battery life through a regulator ----
def f4():
    o = []
    o.append(boxt(20, 20, 190, 64, ['Li-ion cell', '3.7 V × 1.2 Ah = 4.44 Wh'], ACS, AC, 13, True))
    o.append(L(212, 52, 262, 52, AC, 2, arrow='n'))
    o.append(boxt(266, 20, 190, 64, ['Regulator, η = 85%', 'draws P_load ÷ 0.85'], PANEL, AC, 13, True))
    o.append(L(458, 52, 508, 52, AC, 2, arrow='n'))
    o.append(boxt(512, 20, 190, 64, ['Load on 3.3 V rail', 'P_load = 3.3 V × I'], PANEL, AC, 13, True))
    hdr = ['average current', 'P_load', 'P_in = P_load ÷ 0.85', 'life = 4.44 Wh ÷ P_in']
    xs = [20, 190, 330, 520]
    for x, h in zip(xs, hdr): o.append(T(x, 122, h, 13, 'start', MUT, True))
    rows = [('30 mA', '99 mW', '116.5 mW', '38.1 h', NX), ('3 mA', '9.9 mW', '11.65 mW', '381.2 h ≈ 15.9 days', LV)]
    for i, (a, b, c, d, col) in enumerate(rows):
        y = 150 + i * 30
        for x, v in zip(xs, (a, b, c, d)): o.append(T(x, y, v, 14, 'start', col if v == d else INK, v == d))
    o.append(T(20, 238, 'Battery life (hours)', 15, 'start', bold=True))
    sc = 560 / 381.2
    o.append(T(110, 270, '30 mA', 14, 'end', NX, True)); o.append(R(120, 255, 38.1 * sc, 24, NXS, NX, 3))
    o.append(T(128 + 38.1 * sc, 272, '38.1 h', 14, 'start'))
    o.append(T(110, 306, '3 mA', 14, 'end', LV, True)); o.append(R(120, 291, 381.2 * sc, 24, LVS, LV, 3))
    o.append(T(128, 308, '381.2 h', 14, 'start'))
    o.append(T(20, 346, 'Ten times less average current gives ten times more life: t ∝ 1 ÷ I_avg.', 14, 'start', MUT))
    return 362, ''.join(o)
FIG[4] = (f4, 'The 4.44 Wh cell feeds the 3.3 V load through an 85% regulator: at 30 mA the input power is 116.5 mW and the cell lasts 38.1 h; sleep scheduling down to 3 mA cuts it to 11.65 mW and stretches life ten times, to 381.2 h.',
          'Three boxes from a 4.44 watt-hour cell through an 85 percent regulator to a 3.3 volt load; a small table for 30 mA and 3 mA; two bars of 38.1 hours and 381.2 hours.')


# ---- 2.5 the Arduino Uno's 10-bit ADC ----
def f5():
    o = [T(20, 24, 'Full range: 5.00 V split into 2¹⁰ = 1,024 steps of 5.00 ÷ 1,024 = 4.88 mV', 14, 'start', bold=True)]
    x0, x1 = 60, 660
    fx = lambda v: x0 + v / 5 * (x1 - x0)
    o.append(R(x0, 42, x1 - x0, 26, PANEL, L2, 3, 1.5))
    for v, c in ((0, '0'), (1.2, '245'), (2.5, '512'), (5, '')):
        o.append(L(fx(v), 38, fx(v), 72, NX if v in (1.2, 2.5) else L2, 2))
        o.append(T(fx(v), 90, f'{v:.2f} V', 13, fill=MUT))
        o.append(T(fx(v), 108, 'code ' + c if c else 'top: code 1,023', 13, fill=NX if v in (1.2, 2.5) else MUT, bold=v in (1.2, 2.5)))
    o.append(T(fx(2.5) + 8, 128, '512 × 4.88 mV = 2.50 V (half the codes, half the volts)', 13, 'start', MUT))
    # zoomed staircase near 1.20 V
    o.append(T(20, 164, 'Zoom near 1.20 V: the converter truncates to the step below', 14, 'start', bold=True))
    q = 5000 / 1024
    zx0, zx1, zy0, zy1 = 110, 640, 186, 380
    lo, hi = 242.5 * q, 248.3 * q
    gx = lambda mv: zx0 + (mv - lo) / (hi - lo) * (zx1 - zx0)
    gy = lambda c: zy1 - (c - 242) / 6 * (zy1 - zy0)
    o.append(L(zx0, zy1, zx1, zy1, L2, 1.5)); o.append(L(zx0, zy0, zx0, zy1, L2, 1.5))
    pts = []
    for c in range(242, 248):
        a, b = max(c * q, lo), min((c + 1) * q, hi)
        pts += [(gx(a), gy(c)), (gx(b), gy(c))]
        o.append(T(zx0 - 8, gy(c) + 5, str(c), 13, 'end', NX if c == 245 else MUT, c == 245))
        if c >= 243:
            o.append(L(gx(c * q), zy1, gx(c * q), zy1 + 5, L2, 1.5))
            o.append(T(gx(c * q), zy1 + 20, f'{c * q:.1f}', 13, fill=MUT))
    o.append(P(pts, AC, 2.5))
    o.append(L(gx(1200), zy1, gx(1200), gy(245), NX, 2, '6 4'))
    o.append(C(gx(1200), gy(245), 6, NX))
    o.append(Tb(gx(1200) + 12, gy(243.3), '1,200 mV ÷ 4.88 = 245.76', 13, 'start', NX, True)); o.append(Tb(gx(1200) + 12, gy(243.3) + 19, '→ code 245', 13, 'start', NX, True))
    o.append(T((zx0 + zx1) / 2, zy1 + 42, 'input (mV); each tread is one 4.88 mV step', 13, fill=MUT))
    o.append(T(zx0 - 50, zy0 - 6, 'code', 13, 'start', MUT))
    return 436, ''.join(o)
FIG[5] = (f5, 'The Uno\'s 10-bit ADC cuts 5.00 V into 1,024 steps of 4.88 mV: an input of 1.20 V is 245.76 steps and is truncated to code 245, and code 512 sits at exactly 2.50 V.',
          'A bar from 0 to 5 volts marked with code 245 at 1.20 volts and code 512 at 2.50 volts; below, a zoomed staircase of codes 242 to 247 with a dashed line at 1,200 millivolts landing on the tread of code 245.')


# ---- 2.6 one long hop or several short hops ----
def f6():
    o = [T(20, 24, 'Radio energy per bit: E = 50 nJ + ε d², with ε = 100 pJ/bit/m²', 14, 'start', bold=True)]
    def path(y, hops, total):
        n = len(hops); x0, x1 = 60, 360
        xs = [x0 + i * (x1 - x0) / n for i in range(n + 1)]
        for i in range(n):
            o.append(L(xs[i] + 10, y, xs[i + 1] - 13, y, AC, 2, arrow='n'))
            o.append(T((xs[i] + xs[i + 1]) / 2, y - 10, hops[i], 13, fill=MUT))
        for i, x in enumerate(xs):
            o.append(C(x, y, 9, NX if i == n else (AC if i == 0 else L2)))
    sc = 230 / 4050
    def bars(y, parts, total, col, fill):
        x = 380
        for e, a in parts:
            o.append(R(x, y - 12, 50 * sc, 24, LVS, LV, 2, 1.2)); x += 50 * sc
            o.append(R(x, y - 12, a * sc, 24, fill, col, 2, 1.2)); x += a * sc
        o.append(T(x + 8, y + 5, total, 14, 'start', col, True))
    rows = [(70, ['100 m'], [(50, 1000)], '1,050 nJ', NX, NXS), (116, ['50 m', '50 m'], [(50, 250)] * 2, '600 nJ', AC, ACS),
            (184, ['200 m'], [(50, 4000)], '4,050 nJ', NX, NXS), (230, ['50 m'] * 4, [(50, 250)] * 4, '1,200 nJ', AC, ACS)]
    for y, hops, parts, tot, col, f in rows:
        path(y, hops, tot); bars(y, parts, tot, col, f)
    o.append(T(380, 150, 'saves 450 nJ/bit (42.9%)', 14, 'start', AC, True))
    o.append(T(380, 264, 'saves 2,850 nJ/bit (70.4%)', 14, 'start', AC, True))
    o.append(L(20, 166, 700, 166, 'var(--line)', 1))
    o.append(R(60, 290, 18, 14, LVS, LV, 2, 1.2)); o.append(T(84, 302, '50 nJ electronics per hop', 13, 'start', MUT))
    o.append(R(290, 290, 18, 14, ACS, AC, 2, 1.2)); o.append(T(314, 302, 'ε d² amplifier: 1,000 at 100 m, 250 at 50 m, 4,000 at 200 m', 13, 'start', MUT))
    o.append(T(20, 336, 'Halving d quarters ε d², so short hops win even though each hop pays the 50 nJ again.', 14, 'start'))
    return 352, ''.join(o)
FIG[6] = (f6, 'Sending 100 m in one hop costs 50 + 1,000 = 1,050 nJ per bit, but two 50 m hops cost 2 × 300 = 600 nJ; over 200 m, four short hops cost 1,200 nJ against 4,050 nJ for one long hop.',
          'Four rows, each a chain of nodes from source to sink with a stacked energy bar: one 100 metre hop at 1,050 nanojoules, two 50 metre hops at 600, one 200 metre hop at 4,050, four 50 metre hops at 1,200.')


# ---- 2.7 passive RFID read range ----
def f7():
    x0, x1, y0, y1 = 80, 690, 70, 330
    fx = lambda d: x0 + (d - 3) / 12 * (x1 - x0)
    fy = lambda p: y1 - p / 600 * (y1 - y0)
    o = [T(20, 24, 'Reader 2 W ERP = 3.28 W EIRP at 866 MHz; tag gain 2, so A_e = 0.0191 m²', 14, 'start', bold=True)]
    o.append(axes(x0, x1, y0, y1, [3, 6, 9, 12, 15], [0, 100, 200, 300, 400, 500, 600], fx, fy, 'distance from the reader (m)', 'power at the tag chip (µW)'))
    o.append(P([(fx(d / 10), fy(554 * (3 / (d / 10)) ** 2)) for d in range(30, 151)], AC, 3))
    o.append(L(x0, fy(30), x1, fy(30), NX, 2, '7 5'))
    o.append(Tb(fx(3.3), fy(30) - 10, 'wake-up level 30 µW', 13, 'start', NX, True))
    o.append(C(fx(3), fy(554), 6, AC))
    o.append(Tb(fx(3) + 12, fy(554) + 5, 'at 3 m: S = 0.0290 W/m², P = 0.0290 × 0.0191 = 554 µW', 13, 'start', AC, True))
    o.append(C(fx(12.9), fy(30), 7, NX))
    o.append(L(fx(12.9), fy(30), fx(12.9), y1, NX, 2, '4 4'))
    o.append(Tb(fx(12.9), fy(30) - 46, 'd_max = 3 × √(554 ÷ 30)', 13, 'middle', NX, True))
    o.append(Tb(fx(12.9), fy(30) - 26, '= 3 × 4.30 = 12.9 m', 13, 'middle', NX, True))
    o.append(T(fx(7), fy(250), 'power falls as 1 ÷ d²', 14, 'start', MUT))
    return 386, ''.join(o)
FIG[7] = (f7, 'The power reaching the tag chip falls as 1/d², from 554 µW at 3 m to the 30 µW the chip needs at 12.9 m, which is the free-space read range.',
          'A falling 1 over d squared curve of tag power against distance, starting at 554 microwatts at 3 metres and meeting a dashed 30 microwatt wake-up line at 12.9 metres.')


TEXT = {}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
