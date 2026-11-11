"""Claude's hand-drawn figures for c-iot-u1 (Internet of Things, unit 1: IoT concepts and architecture),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


def chain(y, boxes, ops, x0=20, w=140, gap=40, h=58, last=NXS, laststroke=NX):
    """boxes left to right joined by arrows; ops[i] is the label on the arrow after box i"""
    o = []
    for i, lines in enumerate(boxes):
        x = x0 + i * (w + gap)
        f, s = (last, laststroke) if i == len(boxes) - 1 else (PANEL, AC)
        o.append(boxt(x, y, w, h, lines, f, s, 14, bold_first=True))
        if i < len(boxes) - 1:
            o.append(L(x + w + 2, y + h / 2, x + w + gap - 4, y + h / 2, AC, 2, arrow='n'))
            o.append(Tb(x + w + gap / 2, y - 8, ops[i], 13, fill=AC, bold=True))
    return ''.join(o)


# ---- 1.1 raw data from 2,000 water meters ----
def f1():
    o = [T(20, 26, 'One meter, one day: a 40-byte reading every hour', 15, 'start', bold=True)]
    x0, x1, y = 40, 680, 92
    fx = lambda hr: x0 + hr / 24 * (x1 - x0)
    o.append(L(x0, y, x1, y, L2, 1.5))
    for hr in range(25):
        o.append(L(fx(hr), y, fx(hr), y + (7 if hr % 6 == 0 else 4), L2, 1.5))
        if hr % 6 == 0: o.append(T(fx(hr), y + 22, f'{hr} h', 13, fill=MUT))
    for hr in range(24):
        cx = fx(hr + 0.5)
        o.append(R(cx - 9, y - 24, 18, 18, ACS, AC, 3, 1.5))
    o.append(L(fx(0.5), y - 30, fx(0.5) + 26, y - 44, MUT, 1.2))
    o.append(T(fx(0.5) + 30, y - 42, '40 B', 13, 'start', MUT))
    o.append(T(20, 146, 'One meter: 24 readings × 40 B = 960 B a day. Now count all 2,000 meters:', 14, 'start'))
    o.append(chain(186, [['2,000', 'meters'], ['48,000', 'readings/day'], ['1,920,000', 'bytes/day'], ['1,920 kB', 'per day']],
                   ['× 24', '× 40 B', '÷ 1000']))
    o.append(T(20, 280, 'Check: 960 B per meter × 2,000 meters = 1,920,000 B, the same total.', 14, 'start', MUT))
    return 296, ''.join(o)
FIG[1] = (f1, 'Each meter sends 24 readings of 40 B a day, so 2,000 meters send 48,000 readings, which is 1,920,000 bytes or 1,920 kB of raw data per day.',
          'A 24-hour timeline with one small 40-byte packet each hour, then four boxes: 2,000 meters, times 24 gives 48,000 readings, times 40 bytes gives 1,920,000 bytes, divided by 1000 gives 1,920 kB per day.')


# ---- 1.2 power budget of the soil-moisture node ----
def f2():
    o = [T(20, 24, 'Current drawn in one hour (not to scale: the burst is 2 s of the 3,600 s)', 14, 'start', MUT)]
    x0, x1, yb, yt = 60, 690, 200, 56
    o.append(L(x0, yb, x1, yb, L2, 1.5)); o.append(L(x0, yt - 10, x0, yb, L2, 1.5))
    o.append(T(x0 - 8, yt + 5, '30 mA', 13, 'end', MUT)); o.append(T(x0 - 8, yb + 5, '0', 13, 'end', MUT))
    o.append(L(x0 - 4, yt, x0, yt, L2, 1.5))
    # burst
    o.append(R(x0 + 4, yt, 26, yb - yt, ACS, AC, 2, 2))
    o.append(T(x0 + 40, yt + 22, 'awake: 30 mA × 2 s = 60 mA·s', 14, 'start', AC, True))
    # sleep floor (drawn thicker than true scale so it can be seen)
    o.append(R(x0 + 30, yb - 12, x1 - x0 - 34, 12, LVS, LV, 2, 1.5))
    o.append(Tb(x0 + 330, yb - 26, 'asleep: 20 µA = 0.02 mA, × 3,598 s = 71.96 mA·s', 14, 'middle', LV, True))
    o.append(T(x0 + 17, yb + 20, '2 s', 13, fill=MUT)); o.append(T(x1 - 4, yb + 20, '3,600 s', 13, 'end', MUT))
    # charge comparison bars
    s = 380 / 72
    o.append(T(20, 256, 'Charge used per hour', 15, 'start', bold=True))
    o.append(T(170, 286, 'awake', 14, 'end')); o.append(R(180, 270, 60 * s, 24, ACS, AC, 4))
    o.append(T(180 + 60 * s + 8, 287, '60 mA·s', 14, 'start'))
    o.append(T(170, 320, 'asleep', 14, 'end')); o.append(R(180, 304, 71.96 * s, 24, LVS, LV, 4))
    o.append(T(180 + 71.96 * s + 8, 321, '71.96 mA·s', 14, 'start'))
    o.append(T(20, 356, 'The tiny sleep current over a whole hour uses more charge than the burst.', 14, 'start', MUT))
    o.append(boxt(20, 372, 330, 58, ['average current', '131.96 mA·s ÷ 3,600 s ≈ 0.0367 mA'], PANEL, AC, 14, True))
    o.append(L(352, 401, 380, 401, AC, 2, arrow='n'))
    o.append(boxt(384, 372, 316, 58, ['battery life', '2,000 mAh ÷ 0.0367 mA ≈ 54,500 h'], NXS, NX, 14, True))
    o.append(T(542, 452, '54,500 h ÷ 8,760 h a year ≈ 6.2 years', 14, fill=NX, bold=True))
    return 466, ''.join(o)
FIG[2] = (f2, 'In each hour the 2 s burst at 30 mA uses 60 mA·s and the 3,598 s of sleep at 0.02 mA uses 71.96 mA·s; the average of 0.0367 mA makes the 2,000 mAh battery last about 54,500 h, or 6.2 years.',
          'A current-time sketch of one hour: a tall narrow 30 mA burst for 2 seconds and a long low 0.02 mA sleep floor; two bars compare 60 and 71.96 milliamp-seconds; boxes give the average current 0.0367 mA and battery life 54,500 hours.')


# ---- 1.3 cold-chain van: blocks and path ----
def f3():
    o = [T(20, 24, 'Van: 6 temperature + 1 GPS + 2 door = 9 sources, one item every 300 s each', 14, 'start', bold=True),
         T(20, 46, 'D = 9 × 86,400 ÷ 300 = 9 × 288 = 2,592 data items a day', 14, 'start')]
    names = [('Identification', 'van ID, address'), ('Sensing', 'reads 9 °C'), ('Processing', '9 °C > 8 °C limit'),
             ('Communication', '2,592 items/day'), ('Services', 'phone alert')]
    w, gap, y, h = 124, 20, 76, 60
    xs = [10 + i * (w + gap) for i in range(5)]
    for i, ((a, b), x) in enumerate(zip(names, xs)):
        hot = i == 2
        o.append(boxt(x, y, w, h, [a, b], NXS if hot else PANEL, NX if hot else AC, 13, True))
        if i < 4: o.append(L(x + w + 2, y + h / 2, x + w + gap - 3, y + h / 2, AC, 2, arrow='n'))
    # actuation return path
    px = xs[2] + w / 2
    o.append(boxt(px - 105, 186, 210, 52, ['Actuation', 'restart the cooling unit'], LVS, LV, 13, True))
    o.append(L(px, y + h + 2, px, 182, LV, 2.5, arrow='l'))
    o.append(Tb(px + 8, 164, 'decide: too warm', 13, 'start', LV, True))
    o.append(T(px, 258, 'Actuation is a return path back to the van, not a step after services.', 13, 'middle', MUT))
    # cross-cutting blocks
    o.append(R(10, 276, 700, 34, PANEL, L2, 6, 1.5, '6 5'))
    o.append(T(20, 298, 'Management: sets T = 300 s and checks that 2,592 items arrive each day', 13, 'start'))
    o.append(R(10, 318, 700, 34, PANEL, L2, 6, 1.5, '6 5'))
    o.append(T(20, 340, 'Security: proves the van is genuine, encrypts the link, controls who reads the data', 13, 'start'))
    return 364, ''.join(o)
FIG[3] = (f3, 'The van\'s 9 sources, read every 300 s, give 2,592 data items a day along the path from identification to services; processing finds 9 °C above the 8 °C limit, sends the phone alert and, through actuation, restarts the cooling.',
          'Five blocks in a row from identification, sensing, processing, communication to services, with processing highlighted for the 9 degree reading; an arrow down from processing to an actuation box; two dashed bars for management and security under all of them.')
AFTER[3] = 3


# ---- 1.4 one REST poll, then the hourly traffic ----
def f4():
    xs = {'Client': 110, 'API server': 360, 'Device 17': 610}
    o = []
    for n, x in xs.items():
        o.append(boxt(x - 70, 14, 140, 38, [n], ACS if n != 'Device 17' else LVS, AC if n != 'Device 17' else LV, 14, True))
        o.append(L(x, 54, x, 236, L2, 1.5, '5 5'))
    def msg(a, b, y, lab, dash=None, c=AC, arrow='n'):
        xa, xb = xs[a], xs[b]
        d = 1 if xb > xa else -1
        return L(xa + d * 3, y, xb - d * 6, y, c, 2.2, dash, arrow) + Tb((xa + xb) / 2, y - 9, lab, 13)
    o.append(msg('Client', 'API server', 86, 'GET /devices/17 · 300 B'))
    o.append(msg('API server', 'Device 17', 126, 'read sensor', c=LV, arrow='l'))
    o.append(msg('Device 17', 'API server', 166, '31.5 °C', '6 4', LV, 'l'))
    o.append(msg('API server', 'Client', 206, '200 OK {"value": 31.5} · 500 B', '6 4'))
    o.append(T(360, 258, 'The client never talks to the device: the API server reads it.', 13, fill=MUT))
    o.append(chain(296, [['one poll', '300 + 500 = 800 B'], ['one client', '288,000 B/h'], ['50 clients', '14.4 MB/h']],
                   ['× 360 polls', '× 50'], x0=20, w=170, gap=75))
    o.append(T(40, 382, '360 polls an hour because 3,600 s ÷ 10 s = 360;  14,400,000 B ÷ 10⁶ = 14.4 MB', 13, 'start', MUT))
    return 396, ''.join(o)
FIG[4] = (f4, 'One poll is a 300 B GET and a 500 B reply, 800 B in all; a client polling every 10 s makes 360 polls an hour, so 50 clients move 14.4 MB an hour.',
          'A sequence diagram: the client sends GET /devices/17 of 300 bytes to the API server, the server reads device 17 and gets 31.5 degrees, and returns 200 OK of 500 bytes; below, boxes multiply 800 bytes by 360 polls and by 50 clients to reach 14.4 MB per hour.')


# ---- 1.5 aggregation in the network layer ----
def f5():
    o = []
    o.append(boxt(150, 14, 420, 46, ['Application layer: receives 200 uplinks a minute'], PANEL, AC, 14))
    o.append(R(150, 128, 420, 58, ACS, AC))
    o.append(T(360, 152, 'Network layer: gateway', 14, bold=True))
    o.append(T(360, 172, 'packs 20 packets into 1 uplink', 14))
    o.append(L(360, 126, 360, 64, NX, 4, arrow='x'))
    o.append(Tb(372, 98, '1 uplink per group', 13, 'start', NX, True))
    # perception layer: one group of 20 sensors
    o.append(R(40, 252, 640, 70, PANEL, L2, 8, 1.5))
    xs = [72 + i * 30 for i in range(20)]
    for x in xs:
        o.append(L(x, 262, 210 + (x - 72) / (xs[-1] - 72) * 300, 190, L2, 1.2, arrow='m'))
        o.append(C(x, 270, 7, AC))
    o.append(T(360, 304, 'Perception layer: one group of 20 sensors, 1 packet a minute each', 13))
    o.append(Tb(592, 226, '20 packets', 13, 'middle', MUT))
    o.append(T(20, 352, '4,000 sensors = 200 groups of 20', 14, 'start', bold=True))
    o.append(T(20, 376, '4,000 packets a minute ÷ 20 packets per uplink = 200 uplinks a minute', 14, 'start'))
    o.append(T(20, 400, 'The sensors still send all 4,000 packets; only what travels upward shrinks.', 13, 'start', MUT))
    return 414, ''.join(o)
FIG[5] = (f5, 'Each group of 20 sensors sends 20 packets a minute and the gateway packs them into 1 uplink, so 4,000 sensors (200 groups) give 4,000 packets but only 200 uplinks a minute.',
          'Three layers stacked: a row of 20 sensors at the bottom sends 20 arrows into the network-layer gateway, which sends one thick arrow up to the application layer; text below gives 4,000 divided by 20 equals 200 uplinks a minute.')


# ---- 1.6 uplink per day for 10,000 narrowband sensors ----
def f6():
    o = [T(20, 24, 'One sensor, one day: a 512-byte sample every 30 minutes', 15, 'start', bold=True)]
    x0, cw = 40, 640 / 48
    for c in range(48):
        o.append(R(x0 + c * cw + 1, 44, cw - 3, 34, ACS, AC, 2, 1.2))
    o.append(L(x0, 84, x0 + 640, 84, L2, 1.5))
    for hr in range(0, 25, 6):
        o.append(L(x0 + hr * 2 * cw, 84, x0 + hr * 2 * cw, 90, L2, 1.5))
        o.append(T(x0 + hr * 2 * cw, 108, f'{hr:02d}:00', 13, fill=MUT))
    o.append(T(20, 146, '24 × 60 ÷ 30 = 48 samples (48 boxes above), 48 × 512 B = 24,576 B per sensor', 14, 'start'))
    o.append(chain(186, [['one sensor', '24,576 B/day'], ['10,000 sensors', '245,760,000 B'], ['whole fleet', '245.76 MB/day']],
                   ['× 10,000', '÷ 10⁶'], x0=20, w=170, gap=75))
    o.append(T(20, 282, 'A narrowband radio such as NB-IoT carries this easily; the load is in the cloud storing it.', 13, 'start', MUT))
    return 296, ''.join(o)
FIG[6] = (f6, 'A sensor that sends 512 B every 30 minutes makes 48 samples, 24,576 B a day; 10,000 of them upload 245,760,000 B, which is 245.76 MB a day.',
          'Two rows of 24 small boxes, one per half hour, each a 512-byte sample; then three boxes: 24,576 bytes for one sensor, times 10,000 gives 245,760,000 bytes, divided by a million gives 245.76 MB per day.')


# ---- 1.7 M2M versus IoT for 800 trucks ----
def f7():
    o = []
    rows = [(30, 'M2M', ['SMS of 140 B', 'every hour'], ['24 × 140 B', '= 3.36 kB/day'], ['Control room'], ACS, AC, 'n'),
            (120, 'IoT', ['record of 20 kB', 'every hour'], ['24 × 20 kB', '= 480 kB/day'], ['Cloud platform', 'apps, dashboards'], LVS, LV, 'l')]
    for y, tag, msg, day, dest, f, s, ar in rows:
        o.append(T(20, y + 33, tag, 15, 'start', s, True))
        o.append(boxt(70, y + 6, 110, 48, ['Truck unit'], PANEL, s, 14))
        o.append(L(182, y + 30, 212, y + 30, s, 2, arrow=ar))
        o.append(boxt(216, y, 150, 60, msg, f, s, 13))
        o.append(L(368, y + 30, 398, y + 30, s, 2, arrow=ar))
        o.append(boxt(402, y, 140, 60, day, f, s, 13, True))
        o.append(L(544, y + 30, 574, y + 30, s, 2, arrow=ar))
        o.append(boxt(578, y + 4, 132, 52, dest, PANEL, s, 13, True))
    o.append(T(20, 224, 'Fleet of 800 trucks, data per day', 15, 'start', bold=True))
    sc = 520 / 384
    o.append(T(130, 258, 'M2M', 14, 'end', AC, True)); o.append(R(140, 244, max(2.688 * sc, 4), 22, AC, AC, 2))
    o.append(T(152, 260, '800 × 3.36 kB = 2.688 MB', 14, 'start'))
    o.append(T(130, 296, 'IoT', 14, 'end', LV, True)); o.append(R(140, 282, 384 * sc, 22, LVS, LV, 3))
    o.append(T(148, 298, '800 × 480 kB = 384 MB', 14, 'start'))
    o.append(T(20, 336, '384 MB ÷ 2.688 MB ≈ 143: the IoT design sends about 143 times more data.', 14, 'start', NX, True))
    return 352, ''.join(o)
FIG[7] = (f7, 'The same truck unit on two paths: hourly 140 B SMS messages give 3.36 kB per truck and 2.688 MB for the fleet each day, while hourly 20 kB records give 480 kB per truck and 384 MB, about 143 times more.',
          'Two rows: M2M truck sends a 140-byte SMS each hour to a control room, 3.36 kB a day; IoT truck sends a 20 kB record each hour to a cloud platform, 480 kB a day. Below, a hair-thin bar of 2.688 MB against a long bar of 384 MB.')


# ---- 1.8 firmware update in batches ----
def f8():
    o = [T(20, 24, 'Step 1: gateway rate in bytes (the bits-to-bytes trap)', 15, 'start', bold=True),
         T(20, 48, '2 Mbps = 2,000,000 bits/s ÷ 8 = 250,000 B/s = 250 kB/s', 14, 'start', NX, True)]
    o.append(T(20, 86, 'Step 2: one batch of 50 sensors, 250 kB each', 15, 'start', bold=True))
    for i in range(50):
        r, c = divmod(i, 25)
        o.append(R(20 + c * 17, 100 + r * 17, 13, 13, ACS, AC, 2, 1.2))
    o.append(T(460, 116, '50 × 250 kB = 12,500 kB', 14, 'start'))
    o.append(T(460, 136, '12,500 kB ÷ 250 kB/s = 50 s', 14, 'start', AC, True))
    o.append(T(20, 176, 'Step 3: 5,000 ÷ 50 = 100 batches, one after another', 15, 'start', bold=True))
    x0, x1, y = 30, 690, 212
    bw = (x1 - x0) / 100
    for i in range(100):
        o.append(R(x0 + i * bw, y, bw - 1, 26, ACS if i else AC, AC, 1, 0.6))
    o.append(xaxis(x0, x1, y + 30, [0, 1000, 2000, 3000, 4000, 5000], lambda t: x0 + t / 5000 * (x1 - x0), 'time in seconds',
                   lambda v: f'{v:,}'))
    o.append(Tb(x0 + 6, y - 10, 'batch 1: 50 s', 13, 'start', AC, True))
    o.append(T(20, 330, '100 × 50 s = 5,000 s = 83.33 min ≈ 1.39 h', 15, 'start', NX, True))
    return 346, ''.join(o)
FIG[8] = (f8, 'The 2 Mbps gateway moves 250 kB/s, so a batch of 50 updates of 250 kB (12,500 kB) takes 50 s; 100 such batches take 5,000 s, about 1.39 h.',
          'Top: 2 Mbps divided by 8 is 250 kB per second. Middle: 50 small squares for one batch of devices, 12,500 kB taking 50 seconds. Bottom: a time axis to 5,000 seconds filled by 100 thin batch blocks.')


# ---- 1.9 revenue, cost and margin of a smart-meter service ----
def f9():
    o = [T(20, 26, 'Revenue = 25,000 meters × ₹80 = ₹20,00,000 a month', 15, 'start', bold=True)]
    x0, W, y = 40, 640, 70
    s = W / 2000000
    segs = [('connectivity', '25,000 × ₹15', 375000, '₹3,75,000', NXS, NX), ('platform (fixed)', '', 500000, '₹5,00,000', NXS, NX),
            ('margin', '56.25%', 1125000, '₹11,25,000', LVS, LV)]
    x = x0
    for name, sub, v, lab, f, st in segs:
        w = v * s
        o.append(R(x, y, w, 56, f, st, 4))
        o.append(T(x + w / 2, y + 26, lab, 14, bold=True))
        if sub: o.append(T(x + w / 2, y + 45, sub, 13, fill=MUT))
        o.append(T(x + w / 2, y + 78, name, 14, fill=st, bold=True))
        x += w
    o.append(brace(x0, x0 + 875000 * s, y + 98, NX))
    o.append(T(x0 + 875000 * s / 2, y + 124, 'total cost ₹3,75,000 + ₹5,00,000 = ₹8,75,000', 14, fill=NX))
    o.append(T(20, 236, 'Margin = ₹20,00,000 − ₹8,75,000 = ₹11,25,000', 14, 'start'))
    o.append(T(20, 260, 'Margin % = 11,25,000 ÷ 20,00,000 × 100 = 56.25% of revenue', 14, 'start', LV, True))
    o.append(T(20, 290, 'The ₹5,00,000 platform fee is the largest single cost, and it is the same however many meters there are.', 13, 'start', MUT))
    return 304, ''.join(o)
FIG[9] = (f9, 'The ₹20,00,000 a month of revenue splits into ₹3,75,000 of connectivity, ₹5,00,000 of platform cost and ₹11,25,000 of margin, which is 56.25% of revenue.',
          'One long bar for monthly revenue of 20 lakh rupees, divided into connectivity 3.75 lakh, platform 5 lakh and margin 11.25 lakh; a bracket marks the total cost of 8.75 lakh and the margin is labelled 56.25 percent.')


TEXT = {
    1: [('IoT platforms made device management practical: registration, dashboards, rules, APIs and billing. A platform is the highlighted stage in the figure.',
         'IoT platforms made device management practical: registration, dashboards, rules, APIs and billing. A platform is where daily data like the 1,920 kB in the figure is stored and analysed.')],
    9: [('Name the six main roles shown in the IoT value chain figure.', 'Name the six main roles in the IoT value chain.')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
