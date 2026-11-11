"""Claude's hand-drawn figures for c-iot-u5 (Internet of Things, unit 5: IoT cloud, data analytics and security),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {6: 3}


# ---- 5.1 a water-meter sensor cloud ----
def f1():
    o = []
    # meters
    for i in range(10):
        r, c = divmod(i, 5)
        o.append(R(20 + c * 26, 46 + r * 26, 20, 20, PANEL, AC, 4, 1.5))
    o.append(T(85, 116, '200 meters', 13, bold=True))
    o.append(T(85, 134, '64 B every 30 min', 13, fill=MUT))
    o.append(L(152, 70, 192, 70, AC, 2, arrow='n'))
    o.append(boxt(196, 44, 100, 52, ['Gateway'], PANEL, AC, 14, True))
    o.append(L(298, 70, 338, 70, AC, 2, arrow='n'))
    o.append(boxt(342, 30, 180, 80, ['Cloud broker', 'ingests and stores', 'readings + metadata'], ACS, AC, 13, True))
    o.append(L(524, 70, 564, 70, AC, 2, arrow='n'))
    o.append(boxt(568, 30, 140, 80, ['Virtual sensor', 'one per meter,', 'served by an API'], LVS, LV, 13, True))
    o.append(L(638, 112, 638, 146, LV, 2, arrow='l'))
    o.append(boxt(548, 150, 160, 50, ['Billing app', 'asks for history'], PANEL, LV, 13, True))
    o.append(T(530, 222, 'The app talks to the virtual sensor, never to the physical meter.', 13, 'end', MUT))
    # the numbers
    o.append(T(20, 258, 'How much the broker holds', 15, 'start', bold=True))
    rows = [('per meter', '1,440 min ÷ 30 = 48 readings a day'), ('all meters', '200 × 48 = 9,600 readings a day'),
            ('bytes a day', '9,600 × 64 B = 614,400 B = 0.6144 MB'), ('90 days', '614,400 × 90 = 55,296,000 B = 55.296 MB')]
    for i, (a, b) in enumerate(rows):
        y = 286 + i * 26
        o.append(T(150, y, a, 14, 'end', MUT, True)); o.append(T(166, y, b, 14, 'start', NX if i == 3 else INK, i == 3))
    return 382, ''.join(o)
FIG[1] = (f1, '200 meters send a 64 B reading every 30 minutes through a gateway to the cloud broker: 9,600 readings or 0.6144 MB a day, 55.296 MB over 90 days. A billing app reads each meter through its virtual sensor.',
          'Meters feed a gateway, which feeds a cloud broker, which serves one virtual sensor per meter to a billing app; below, four lines of arithmetic from 48 readings per meter to 55.296 MB in 90 days.')


# ---- 5.2 peak and average message rate on an IoT platform ----
def f2():
    o = [T(20, 24, '500 devices, one 200 B message each every 10 minutes', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 70, 680, 64, 250
    fx = lambda t: x0 + t / 1200 * (x1 - x0)
    fy = lambda r: y1 - r / 10 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 300, 600, 900, 1200], [0, 2, 4, 6, 8, 10], fx, fy, 'time (s)', 'messages per second'))
    for t0 in (0, 600):
        o.append(R(fx(t0), fy(8.33), fx(60) - fx(0), fy(0) - fy(8.33), NXS, NX, 2, 2))
    o.append(L(x0, fy(0.833), x1, fy(0.833), AC, 2.5, '8 5'))
    o.append(Tb(fx(60) + 10, fy(8.33) + 5, 'peak: 500 ÷ 60 = 8.33 messages/s', 13, 'start', NX, True)); o.append(Tb(fx(60) + 10, fy(8.33) + 24, '(all in one 60 s window)', 13, 'start', NX))
    o.append(Tb(fx(300), fy(0.833) - 12, 'average: 72,000 ÷ 86,400 = 0.83 messages/s', 13, 'start', AC, True))
    o.append(T(20, 316, 'A day: 1,440 ÷ 10 = 144 messages per device, 500 × 144 = 72,000 messages, × 200 B = 14.4 MB.', 14, 'start'))
    o.append(T(20, 340, 'The burst is ten times the average: size the platform\'s buffers for the peak.', 14, 'start', NX, True))
    return 356, ''.join(o)
FIG[2] = (f2, 'If all 500 devices publish inside the same minute, the platform sees 8.33 messages a second, ten times the daily average of 0.83; over a day the farm sends 72,000 messages, 14.4 MB.',
          'Message rate against time over 20 minutes: a tall block of 8.33 messages per second for the first 60 seconds of each 10-minute period, and a dashed average line at 0.83.')


# ---- 5.3 edge window average for a vibration sensor ----
def f3():
    o = [T(20, 24, 'One minute of raw vibration: 2,000 samples/s × 60 s = 120,000 samples', 14, 'start', bold=True)]
    x0, x1, yc = 40, 460, 90
    pts = [(x0 + i * (x1 - x0) / 400, yc + 30 * math.sin(i * 0.9) * (0.6 + 0.4 * math.sin(i * 0.05))) for i in range(401)]
    o.append(P(pts, L2, 1.2))
    o.append(L(x0, yc, x1, yc, AC, 2.5, '6 4'))
    o.append(brace(x0, x1, 136, MUT)); o.append(T((x0 + x1) / 2, 158, '120,000 samples × 4 B = 480,000 B', 13, fill=MUT))
    o.append(L(470, yc, 540, yc, AC, 2.5, arrow='n')); o.append(T(505, yc - 10, 'edge', 13, fill=AC, bold=True))
    o.append(C(560, yc, 9, AC)); o.append(T(576, yc + 5, '1 value:', 13, 'start', AC, True)); o.append(T(576, yc + 23, 'the average', 13, 'start', AC))
    o.append(T(20, 204, 'One hour', 15, 'start', bold=True))
    o.append(R(140, 218, 560, 30, 'var(--line)', L2, 3, 1.2))
    o.append(T(130, 238, 'raw', 13, 'end', MUT, True))
    o.append(T(420, 238, '2,000 × 3,600 = 7,200,000 samples = 28,800,000 B = 28.8 MB', 13))
    o.append(T(130, 278, 'kept', 13, 'end', AC, True))
    for i in range(60):
        o.append(C(146 + i * 9.4, 274, 3, AC))
    o.append(T(140, 304, '60 values an hour, one a minute, for the dashboard', 13, 'start', AC))
    o.append(T(20, 340, 'Reduction = 7,200,000 ÷ 60 = 120,000 times fewer stored values', 15, 'start', NX, True))
    return 356, ''.join(o)
FIG[3] = (f3, 'The sensor makes 120,000 samples a minute; the edge keeps only their one-minute average, so an hour of 7,200,000 raw samples (28.8 MB) becomes 60 dashboard values, 120,000 times fewer.',
          'A dense wiggly trace for one minute of vibration collapsed by the edge into a single average dot; below, an hour as one long raw bar of 7.2 million samples against a row of 60 kept dots.')


# ---- 5.4 certificate rotation for a smart-lock fleet ----
def f4():
    o = []
    o.append(boxt(270, 14, 180, 46, ['Certificate authority'], ACS, AC, 14, True))
    x0, x1, y = 60, 680, 150
    fx = lambda d: x0 + d / 365 * (x1 - x0)
    o.append(R(x0, y - 16, x1 - x0, 32, PANEL, L2, 4, 1.2))
    for i, d in enumerate((0, 90, 180, 270, 360)):
        if i < 4:
            o.append(R(fx(d) + 2, y - 12, fx(90) - fx(0) - 4, 24, ACS, AC, 3, 1.2))
            o.append(T(fx(d + 45), y + 5, f'cert {i + 1}', 13))
        o.append(L(fx(d), 76, fx(d), y - 18, NX, 1.5, '4 3', arrow='x'))
    o.append(R(fx(360) + 2, y - 12, fx(365) - fx(360) - 2, 24, NXS, NX, 2, 1.2))
    o.append(L(fx(0), 76, fx(360), 76, NX, 1.5)); o.append(L(360, 60, 360, 76, NX, 1.5))
    o.append(T(fx(0), 44, 'renews using its old identity', 13, 'start', NX)); o.append(T(fx(0), 62, 'every 90 days', 13, 'start', NX))
    o.append(xaxis(x0, x1, y + 20, [0, 90, 180, 270, 360], fx, 'one device, one year (days)'))
    o.append(T(20, 250, 'Per device: 365 ÷ 90 = 4.0556 certificates a year (the fifth starts on day 360)', 14, 'start'))
    o.append(T(20, 274, 'Fleet: 10,000 × 4.0556 = 40,555.6 → about 40,556 certificates a year', 14, 'start', NX, True))
    o.append(T(20, 298, 'Storage: only the active one is kept, 10,000 × 1 KB = 10,000 KB = 10 MB', 14, 'start', AC, True))
    return 314, ''.join(o)
FIG[4] = (f4, 'Each lock renews its 1 KB certificate from the CA every 90 days, 365 ÷ 90 = 4.0556 times a year, so the fleet of 10,000 needs about 40,556 certificates a year while only 10 MB of active certificates exist at any time.',
          'A one-year timeline for one device split into 90-day certificate periods, with dashed arrows from a certificate authority at days 0, 90, 180, 270 and 360; text gives 40,556 certificates a year and 10 MB of storage.')


# ---- 5.5 WoT Thing Descriptions on a gateway ----
def f5():
    o = [R(20, 20, 300, 170, PANEL, AC, 10)]
    o.append(T(170, 42, 'gateway servient: 20 Things', 14, bold=True))
    for i in range(20):
        r, c = divmod(i, 10)
        x, y = 36 + c * 28, 60 + r * 58
        o.append(f'<path d="M{x},{y} h16 l6,6 v30 h-22 Z" style="fill:var(--accent-soft);stroke:{AC};stroke-width:1.4"/>')
        o.append(L(x + 4, y + 14, x + 17, y + 14, AC, 1)); o.append(L(x + 4, y + 21, x + 17, y + 21, AC, 1))
    o.append(T(170, 180, 'one Thing Description = 1.2 KB', 13, fill=MUT))
    s = 340 / 24
    x0 = 350
    o.append(T(x0, 48, 'raw: 20 × 1.2 KB', 14, 'start', bold=True))
    o.append(R(x0, 58, 24 * s, 32, ACS, AC, 3)); o.append(T(x0 + 12 * s, 79, '24.0 KB', 14, bold=True))
    o.append(T(x0, 128, 'stored after a 40% cut', 14, 'start', bold=True))
    o.append(R(x0, 138, 14.4 * s, 32, LVS, LV, 3)); o.append(T(x0 + 7.2 * s, 159, '14.4 KB', 14, bold=True))
    o.append(R(x0 + 14.4 * s, 138, 9.6 * s, 32, 'none', L2, 3, 1.5, '5 4')); o.append(T(x0 + 19.2 * s, 159, 'saved 9.6', 13, fill=MUT))
    o.append(T(20, 230, '100% − 40% = 60% stays: 24.0 KB × 0.60 = 14.4 KB', 15, 'start', NX, True))
    return 246, ''.join(o)
FIG[5] = (f5, 'The gateway holds 20 Thing Descriptions of 1.2 KB, 24.0 KB raw; compression removes 40%, so 60% is kept and the descriptions take 14.4 KB.',
          'A gateway box with 20 small document icons; bars compare 24.0 KB raw with 14.4 KB stored, the missing 9.6 KB drawn dashed.')


# ---- 5.6 SDN moves flows off a congested gateway ----
def f6():
    o = [boxt(250, 12, 220, 46, ['SDN controller', 'moves 30% of G1\'s flows'], ACS, AC, 13, True)]
    x0, y1 = 70, 280
    bw, gap = 70, 54
    sc = 3.2
    for i in range(5):
        x = x0 + i * (bw + gap)
        after = 28 if i == 0 else 43
        o.append(L(360, 60, x + bw / 2, 92, L2, 1.3, '4 3', arrow='m'))
        o.append(R(x, y1 - 40 * sc, bw / 2 - 3, 40 * sc, 'var(--line)', L2, 2, 1.2))
        o.append(T(x + bw / 4 - 1, y1 - 40 * sc - 6, '40', 13, fill=MUT))
        o.append(R(x + bw / 2 + 1, y1 - after * sc, bw / 2 - 3, after * sc, LVS if i == 0 else ACS, LV if i == 0 else AC, 2, 1.5))
        o.append(T(x + 3 * bw / 4, y1 - after * sc - 6, str(after), 13, fill=LV if i == 0 else AC, bold=True))
        o.append(T(x + 3 * bw / 4, y1 - after * sc - 24, '−12' if i == 0 else '+3', 13, fill=LV if i == 0 else AC, bold=True))
        o.append(T(x + bw / 2, y1 + 20, f'G{i + 1}', 14, bold=True))
    o.append(L(40, y1, 690, y1, L2, 1.5))
    o.append(R(470, 316, 14, 14, 'var(--line)', L2, 2, 1.2)); o.append(T(490, 328, 'before', 13, 'start', MUT))
    o.append(R(560, 316, 14, 14, ACS, AC, 2, 1.2)); o.append(T(580, 328, 'after', 13, 'start', MUT))
    o.append(T(20, 328, '0.30 × 40 = 12;  12 ÷ 4 = 3;  28 + 4 × 43 = 200 flows', 14, 'start', NX, True))
    return 344, ''.join(o)
FIG[6] = (f6, 'The controller takes 30% of congested gateway G1\'s 40 flows, 12 flows, and gives 3 to each of the other four; G1 falls to 28, the others rise to 43, and the total stays 200.',
          'Five pairs of bars for gateways G1 to G5, before and after: all start at 40; after the move G1 has 28 and the others 43, with arrows from G1 to each other gateway and a controller above.')


# ---- 5.7 clustering cuts gateway traffic ----
def f7():
    o = []
    def cluster(cx, cy, head=True):
        pts = [(cx + 46 * math.cos(a), cy + 30 * math.sin(a)) for a in [i * 2 * math.pi / 10 for i in range(10)]]
        for x, y in pts:
            o.append(L(x, y, cx, cy, L2, 1)); o.append(C(x, y, 4.5, AC))
        if head: o.append(C(cx, cy, 9, NX))
    # direct
    o.append(T(20, 24, 'Direct: every node reports to the gateway', 14, 'start', bold=True))
    o.append(boxt(260, 136, 90, 40, ['Gateway'], PANEL, AC, 13, True))
    for k, (cx, cy) in enumerate(((70, 80), (170, 80), (70, 170))):
        for i in range(10):
            a = i * 2 * math.pi / 10
            x, y = cx + 40 * math.cos(a), cy + 26 * math.sin(a)
            o.append(L(x, y, 260, 156, 'var(--line)', 0.9)); o.append(C(x, y, 4.5, AC))
    o.append(T(20, 226, '30 × 1,440 × 64 B = 2,764,800 B/day', 13, 'start'))
    # clustered
    o.append(T(380, 24, 'Clustered: 3 heads send aggregates', 14, 'start', bold=True))
    o.append(boxt(610, 136, 90, 40, ['Gateway'], PANEL, AC, 13, True))
    for cx, cy in ((440, 80), (540, 80), (440, 170)):
        cluster(cx, cy)
        o.append(L(cx + 9, cy + 3, 606, 156, NX, 2.2, arrow='x'))
    o.append(T(380, 226, '3 × 1,440 × 128 B = 552,960 B/day', 13, 'start'))
    o.append(T(20, 266, 'Gateway inbound per day (1,440 reports in 86,400 s)', 15, 'start', bold=True))
    s = 520 / 2.7648
    o.append(T(120, 298, 'direct', 14, 'end', MUT, True)); o.append(R(130, 284, 2.7648 * s, 22, 'var(--line)', L2, 3))
    o.append(T(140, 300, '2.7648 MB', 13, 'start', bold=True))
    o.append(T(120, 332, 'clustered', 14, 'end', NX, True)); o.append(R(130, 318, 0.55296 * s, 22, NXS, NX, 3))
    o.append(T(140 + 0.55296 * s, 334, '0.55296 MB: one fifth (2,764,800 ÷ 552,960 = 5)', 13, 'start', NX, True))
    o.append(T(20, 366, 'Node-to-head traffic still exists; only what reaches the gateway shrinks.', 13, 'start', MUT))
    return 380, ''.join(o)
FIG[7] = (f7, 'Directly, 30 nodes each send 1,440 readings of 64 B a day to the gateway, 2.7648 MB; clustered, only 3 heads send 1,440 aggregates of 128 B, 0.55296 MB, one fifth as much.',
          'Left, thirty nodes all wired to the gateway; right, three clusters of ten nodes each feeding a head that alone talks to the gateway. Bars compare 2.7648 MB with 0.55296 MB a day.')


TEXT = {}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
