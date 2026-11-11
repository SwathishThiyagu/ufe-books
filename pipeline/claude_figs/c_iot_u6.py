"""Claude's hand-drawn figures for c-iot-u6 (Internet of Things, unit 6: IoT applications and industrial IoT),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {1: 4, 2: 2, 3: 3, 4: 2}


# ---- 6.1 a smart home's daily energy ----
def f1():
    o = [T(20, 24, 'Energy = power × hours: each box\'s area is one day\'s energy', 14, 'start', bold=True)]
    x0, x1 = 170, 690
    fx = lambda h: x0 + h / 24 * (x1 - x0)
    ps = 1.1
    rows = [('10 bulbs, 9 W each', 90, 5, '90 W × 5 h = 450 Wh', ACS, AC), ('hub', 3, 24, '3 W × 24 h = 72 Wh', LVS, LV),
            ('2 cameras, 5 W each', 10, 24, '10 W × 24 h = 240 Wh', NXS, NX)]
    y = 44
    for name, p, h, lab, f, st in rows:
        hh = max(p * ps, 4)
        top = y + max(0, 30 - hh)
        o.append(T(x0 - 10, top + hh / 2 + 5, name, 13, 'end', bold=True))
        o.append(R(x0, top, fx(h) - x0, hh, f, st, 2, 1.5))
        o.append(T(fx(h) + 8 if h < 24 else x0 + 8, (top + hh / 2 + 5) if h < 24 else top - 6, lab, 13, 'start', st, True))
        y = top + hh + 30
    o.append(xaxis(x0, x1, y - 14, [0, 6, 12, 18, 24], fx, None, lambda v: f'{v} h'))
    yb = y + 40
    o.append(T(20, yb, 'One day: 450 + 72 + 240 = 762 Wh = 0.762 kWh', 14, 'start', bold=True))
    s = 600 / 762
    x = 40
    for v, f, st in ((450, ACS, AC), (72, LVS, LV), (240, NXS, NX)):
        o.append(R(x, yb + 12, v * s, 26, f, st, 2, 1.3)); o.append(T(x + v * s / 2, yb + 30, f'{v}', 13, bold=True)); x += v * s
    o.append(T(20, yb + 70, '30 days: 0.762 × 30 = 22.86 kWh;  cost 22.86 × ₹7.50 = ₹171.45', 15, 'start', NX, True))
    o.append(T(20, yb + 94, 'The hub and cameras run all 24 h, so they use 312 of the 762 Wh, about 41%.', 13, 'start', MUT))
    return yb + 110, ''.join(o)
FIG[1] = (f1, 'Ten 9 W bulbs for 5 h use 450 Wh, the 3 W hub all day 72 Wh and two 5 W cameras all day 240 Wh, 762 Wh a day; over 30 days that is 22.86 kWh, ₹171.45 at ₹7.50 a unit.',
          'Three boxes whose area is energy: a tall short box for the bulbs, 90 watts for 5 hours, and two long thin boxes for the hub and cameras running 24 hours; a stacked bar of 450, 72 and 240 watt-hours and the monthly cost.')


# ---- 6.2 smart parking uplink ----
def f2():
    o = [T(20, 24, '200 slot sensors, one 60 B message each every 5 minutes', 14, 'start', bold=True)]
    for i in range(200):
        r, c = divmod(i, 40)
        o.append(R(20 + c * 17, 40 + r * 17, 13, 13, ACS, AC, 2, 1))
    o.append(T(20, 148, 'Per hour: 60 ÷ 5 = 12 messages a slot, × 200 slots = 2,400 messages', 14, 'start'))
    o.append(boxt(20, 172, 170, 56, ['per second', '2,400 ÷ 3,600 = 0.6667'], PANEL, AC, 13, True))
    o.append(L(192, 200, 246, 200, AC, 2, arrow='n')); o.append(Tb(219, 188, '× 480', 13, fill=AC, bold=True))
    o.append(boxt(250, 172, 170, 56, ['bits a message', '60 B × 8 = 480 bit'], PANEL, AC, 13, True))
    o.append(L(422, 200, 476, 200, AC, 2, arrow='n')); o.append(Tb(449, 188, '=', 13, fill=AC, bold=True))
    o.append(boxt(480, 172, 160, 56, ['average uplink', '320 bit/s'], NXS, NX, 14, True))
    o.append(T(20, 266, 'A day: 2,400 × 24 = 57,600 messages × 60 B = 3,456,000 B = 3.456 MB', 14, 'start'))
    o.append(T(20, 290, 'Check: 320 bit/s × 86,400 s ÷ 8 = 3,456,000 B, the same.', 14, 'start', NX, True))
    return 306, ''.join(o)
FIG[2] = (f2, '200 slots sending 12 messages an hour make 2,400 messages, 0.6667 a second; at 480 bits a message the average uplink is 320 bit/s, which is 3.456 MB a day.',
          'A grid of 200 small slot squares, then three boxes: 0.6667 messages a second times 480 bits gives 320 bits per second; text gives 57,600 messages and 3.456 MB a day.')


# ---- 6.3 OEE as time lost in three steps ----
def f3():
    o = [T(20, 24, 'A 480-minute shift, losing time at each step', 15, 'start', bold=True)]
    x0 = 200
    s = 380 / 480
    rows = [('planned time', 480, None, '480 min'), ('run time', 432, 'downtime 48', 'A = 432 ÷ 480 = 90.0%'),
            ('ideal time for 800 parts', 400, 'slow 32', 'P = 400 ÷ 432 = 92.6%'), ('ideal time for 760 good', 380, 'scrap 20', 'Q = 760 ÷ 800 = 95.0%')]
    for i, (name, v, loss, note) in enumerate(rows):
        y = 44 + i * 62
        o.append(T(x0 - 10, y + 22, name, 13, 'end', bold=True))
        o.append(R(x0, y, v * s, 32, ACS if i < 3 else NXS, AC if i < 3 else NX, 3, 1.5))
        o.append(T(x0 + 8, y + 21, f'{v} min', 13, 'start', bold=True))
        if loss:
            prev = rows[i - 1][1]
            o.append(R(x0 + v * s, y, (prev - v) * s, 32, 'none', LV, 3, 1.5, '4 3'))
            o.append(T(x0 + prev * s + 6, y + 21, loss, 13, 'start', LV, True))
        if i: o.append(T(x0, y + 50, note, 13, 'start', MUT))
    o.append(T(20, 322, 'OEE = 0.900 × 0.926 × 0.950 = 0.792 = 79.2%, the same as 380 ÷ 480', 15, 'start', NX, True))
    o.append(T(20, 346, 'Ideal cycle 30 s = 0.5 min: 800 × 0.5 = 400 min; 40 bad parts × 0.5 = 20 min of scrap.', 13, 'start', MUT))
    return 362, ''.join(o)
FIG[3] = (f3, 'Of 480 planned minutes, 48 are lost to downtime (A = 90.0%), 32 to running slow (P = 92.6%) and 20 to scrap (Q = 95.0%); the 380 good-part minutes left are 79.2% of 480, the OEE.',
          'Four bars shrinking from 480 planned minutes to 432 run minutes, 400 ideal minutes for 800 parts and 380 minutes for 760 good parts, with dashed losses of 48, 32 and 20 minutes and the three factors.')


# ---- 6.4 ABS wheel-speed sensor ----
def f4():
    o = []
    cx, cy, r = 150, 170, 110
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:var(--panel);stroke:{INK};stroke-width:2.5"/>')
    rt = 70
    for i in range(48):
        a = i * 2 * math.pi / 48
        a1, a2 = a - 0.035, a + 0.035
        o.append(f'<path d="M{cx + rt * math.cos(a1):.1f},{cy + rt * math.sin(a1):.1f} L{cx + (rt + 10) * math.cos(a1):.1f},{cy + (rt + 10) * math.sin(a1):.1f} L{cx + (rt + 10) * math.cos(a2):.1f},{cy + (rt + 10) * math.sin(a2):.1f} L{cx + rt * math.cos(a2):.1f},{cy + rt * math.sin(a2):.1f} Z" style="fill:{AC};stroke:none"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{rt}" style="fill:var(--accent-soft);stroke:{AC};stroke-width:1.5"/>')
    o.append(L(cx, cy, cx + r, cy, INK, 1.5, '4 3')); o.append(Tb(cx + 56, cy - 8, 'r = 0.32 m', 13, 'middle'))
    o.append(T(cx, cy + 40, '48-tooth ring', 13, fill=AC, bold=True))
    o.append(R(cx + rt + 14, cy - 56, 40, 24, LVS, LV, 4))
    o.append(T(cx + rt + 34, cy - 70, 'sensor', 13, fill=LV, bold=True))
    o.append(arc(cx - 30, cy - r - 14, cx + 30, cy - r - 14, -0.25, NX, 2, 'x'))
    o.append(T(cx, cy - r - 30, 'v = 60 km/h', 13, fill=NX, bold=True))
    x = 310
    steps = [('v = 60 ÷ 3.6', '= 16.67 m/s'), ('ω = v ÷ r = 16.67 ÷ 0.32', '= 52.08 rad/s'), ('n = ω ÷ 2π = 52.08 ÷ 6.2832', '= 8.29 rev/s'), ('f = n × 48 teeth', '= 397.9 pulses/s')]
    for i, (a, b) in enumerate(steps):
        y = 30 + i * 62
        o.append(boxt(x, y, 250, 48, [a, b], NXS if i == 3 else PANEL, NX if i == 3 else AC, 13))
        if i < 3: o.append(L(x + 125, y + 50, x + 125, y + 60, AC, 2, arrow='n'))
    # pulse train
    o.append(T(580, 44, 'sensor output', 13, 'start', MUT))
    for i in range(6):
        px = 584 + i * 20
        o.append(P([(px, 100), (px, 70), (px + 10, 70), (px + 10, 100), (px + 20, 100)], LV, 2))
    o.append(T(580, 122, '397.9 Hz at', 13, 'start', LV, True)); o.append(T(580, 140, '60 km/h', 13, 'start', LV, True))
    o.append(T(580, 176, 'faster wheel,', 13, 'start', MUT)); o.append(T(580, 194, 'more pulses', 13, 'start', MUT))
    return 292, ''.join(o)
FIG[4] = (f4, 'At 60 km/h (16.67 m/s) a wheel of radius 0.32 m turns at 52.08 rad/s, 8.29 turns a second, so its 48-tooth ring passes the sensor 397.9 times a second.',
          'A wheel of radius 0.32 metres with a 48-tooth ring passing a sensor; four boxes convert 60 km/h to 16.67 m/s, 52.08 rad/s, 8.29 rev/s and 397.9 pulses per second; a short square pulse train.')


# ---- 6.5 rooftop tank fill, energy and cost ----
def f5():
    o = []
    # isometric tank
    ox, oy, a, b, h = 30, 170, 120, 46, 70
    top = [(ox, oy - h), (ox + a, oy - h - 30), (ox + a + b, oy - h - 10), (ox + b, oy - h + 20)]
    o.append(f'<path d="M{ox},{oy} L{ox},{oy - h} L{ox + b},{oy - h + 20} L{ox + b},{oy + 20} Z" style="fill:var(--accent-soft);stroke:{AC};stroke-width:1.8"/>')
    o.append(f'<path d="M{ox + b},{oy + 20} L{ox + b},{oy - h + 20} L{ox + a + b},{oy - h - 10} L{ox + a + b},{oy - 10} Z" style="fill:var(--accent-soft);stroke:{AC};stroke-width:1.8"/>')
    o.append(f'<path d="M{" L".join(f"{x},{y}" for x, y in top)} Z" style="fill:var(--panel);stroke:{AC};stroke-width:1.8"/>')
    o.append(T(ox + b / 2 + a / 2 + 4, oy + 22, '2 m', 13, fill=MUT)); o.append(T(ox + 6, oy + 18, '1.5 m', 13, 'end', MUT))
    o.append(T(ox + a + b + 6, oy - h / 2 - 6, '1.2 m', 13, 'start', MUT))
    o.append(T(20, 230, 'V = 2 × 1.5 × 1.2 = 3.6 m³', 14, 'start', bold=True))
    o.append(T(20, 252, '= 3.6 × 1,000 = 3,600 L', 14, 'start', AC, True))
    # fill graph
    x0, x1, y0, y1 = 300, 680, 40, 220
    fx = lambda m: x0 + m / 180 * (x1 - x0)
    fy = lambda l: y1 - l / 3600 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 60, 120, 180], [0, 1200, 2400, 3600], fx, fy, 'clock time', 'water in the tank (L)',
                  lambda m: {0: '6:00', 60: '7:00', 120: '8:00', 180: '9:00'}[m], lambda v: f'{v:,}'))
    o.append(L(fx(0), fy(0), fx(180), fy(3600), AC, 3))
    o.append(C(fx(180), fy(3600), 6, NX))
    o.append(Tb(fx(170), fy(3600) - 2, 'full at 9:00', 13, 'end', NX, True))
    o.append(Tb(fx(30), fy(1500), '20 L every minute', 13, 'start', AC, True))
    o.append(T(20, 300, 'Fill time = 3,600 L ÷ 20 L/min = 180 min = 3 h', 14, 'start'))
    o.append(T(20, 324, 'Pump: 0.5 HP × 746 W = 373 W = 0.373 kW (rating taken as power drawn, losses ignored)', 14, 'start'))
    o.append(T(20, 348, 'Energy = 0.373 kW × 3 h = 1.119 kWh;  cost = 1.119 × ₹7 = ₹7.83', 15, 'start', NX, True))
    return 364, ''.join(o)
FIG[5] = (f5, 'The 3,600 L tank fills from 6:00 to 9:00 at 20 L/min, so the 373 W pump uses 1.119 kWh, costing ₹7.83.',
          'A box-shaped tank 2 by 1.5 by 1.2 metres; a straight line of water rising from 0 litres at 6:00 to 3,600 litres at 9:00; text gives 1.119 kWh and 7.83 rupees.')


# ---- 6.6 a 500-node LoRaWAN farm ----
def f6():
    o = [T(20, 24, 'One 80 B reading against the 51 B LoRaWAN payload limit', 14, 'start', bold=True)]
    s = 7
    x0 = 40
    o.append(R(x0, 40, 80 * s, 32, ACS, AC, 3)); o.append(T(x0 + 40 * s, 61, 'reading: 80 B', 14, bold=True))
    o.append(L(x0 + 51 * s, 32, x0 + 51 * s, 128, NX, 2.5, '6 4')); o.append(T(x0 + 51 * s + 6, 40 - 14 + 10, '', 13))
    o.append(T(x0 + 51 * s - 6, 140 - 0, '51 B limit', 13, 'end', NX, True))
    o.append(R(x0, 88, 51 * s, 32, NXS, NX, 3)); o.append(T(x0 + 25.5 * s, 109, 'frame 1: 51 B', 13, bold=True))
    o.append(R(x0 + 51 * s + 8, 88, 29 * s, 32, NXS, NX, 3)); o.append(T(x0 + 51 * s + 8 + 14.5 * s, 109, 'frame 2: 29 B', 13, bold=True))
    o.append(T(20, 172, '80 ÷ 51 = 1.57, round up: 2 frames for every reading', 14, 'start', NX, True))
    rows = [('per node', '1,440 min ÷ 10 = 144 readings a day'), ('farm', '500 × 144 = 72,000 readings a day'),
            ('bytes', '72,000 × 80 B = 5,760,000 B = 5.76 MB a day'), ('mean rate', '5,760,000 × 8 ÷ 86,400 s = 533.33 bit/s'),
            ('frames', '2 × 72,000 = 144,000 frames a day')]
    for i, (a, b) in enumerate(rows):
        y = 212 + i * 26
        o.append(T(130, y, a, 14, 'end', MUT, True)); o.append(T(146, y, b, 14, 'start', NX if i == 4 else INK, i == 4))
    o.append(T(20, 352, 'The mean rate is tiny; the frame count, not the bit rate, is what the network must carry.', 13, 'start', MUT))
    return 368, ''.join(o)
FIG[6] = (f6, 'An 80 B reading exceeds the 51 B payload limit, so it needs two frames: 72,000 readings a day become 144,000 frames, at a mean of only 533.33 bit/s.',
          'An 80-byte reading bar crossed by a dashed 51-byte limit and split into a 51-byte frame and a 29-byte frame; five lines of arithmetic down to 144,000 frames a day.')


TEXT = {
    5: [('Electrical input power P = 0.5 HP × 746 W/HP = 373 W.',
         'Electrical input power (rating taken as power drawn): P = 0.5 HP × 746 W/HP = 373 W.')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
