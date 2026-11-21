"""Claude's hand-drawn figures for au-elec-u6 (Automotive Electrical and Electronics: in-vehicle networks and connected
vehicles), one per chapter, drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

GREY = 'var(--line)'


def title(x, y, s, anchor='middle'):
    return T(x, y, s, 15, anchor, bold=True)


# ---- 6.1 point-to-point mesh versus one bus (worked example 1 counts the same for 12 ECUs) ----
def f1():
    o = [title(180, 24, 'Point to point: 15 links'), title(550, 24, 'One shared bus: 1 pair')]
    names = ['Engine', 'Gearbox', 'ABS', 'Cluster', 'Body', 'Airbag']
    cx, cy, r = 180, 175, 112
    pts = [(cx + r * math.cos(math.radians(-90 + 60 * i)), cy + r * math.sin(math.radians(-90 + 60 * i))) for i in range(6)]
    for i in range(6):
        for j in range(i + 1, 6):
            o.append(L(*pts[i], *pts[j], L2, 1.6))
    for (x, y), n in zip(pts, names):
        o.append(boxt(x - 38, y - 15, 76, 30, [n], PANEL, AC, 13))
    o.append(T(180, 322, 'n(n − 1)/2 = 6 × 5/2 = 15 links', 14, fill=MUT))
    # bus
    y0 = 178
    o.append(L(384, y0 - 4, 706, y0 - 4, AC, 2.5)); o.append(L(384, y0 + 4, 706, y0 + 4, AC, 2.5))
    o.append(R(372, y0 - 14, 12, 28, NXS, NX, 2)); o.append(R(706, y0 - 14, 12, 28, NXS, NX, 2))
    o.append(T(400, y0 + 36, '120 Ω', 13, fill=NX)); o.append(T(690, y0 + 36, '120 Ω', 13, fill=NX))
    xs = [440, 545, 650]
    for i, x in enumerate(xs):
        o.append(L(x, 98, x, y0 - 4, AC, 2)); o.append(boxt(x - 42, 68, 84, 30, [names[i]], PANEL, AC, 13))
        o.append(L(x, y0 + 4, x, 258, AC, 2)); o.append(boxt(x - 42, 258, 84, 30, [names[i + 3]], PANEL, AC, 13))
    o.append(Tb(492, y0 - 12, 'CAN_H', 13, fill=MUT)); o.append(Tb(598, y0 + 22, 'CAN_L', 13, fill=MUT))
    o.append(T(545, 322, '6 transceivers on one twisted pair', 14, fill=MUT))
    o.append(T(360, 352, 'Worked example, 12 ECUs: 66 links and 132 line drivers, or 1 bus and 12 transceivers', 14, bold=True))
    return 368, ''.join(o)


# ---- 6.2 the OSI layers in a CAN network, with the VIN reply of worked example 1 ----
def f2():
    o = [title(110, 24, 'OSI layer'), title(330, 24, 'In a CAN network'), title(590, 24, 'VIN reply (worked example)')]
    rows = [('7 Application', 'OBD service 09: VIN', True), ('6 Presentation', 'empty', False), ('5 Session', 'empty', False),
            ('4 Transport', 'ISO-TP cuts and rebuilds', True), ('3 Network', 'empty (gateway routes IDs)', False),
            ('2 Data link', 'CAN frame, arbitration, CRC', True), ('1 Physical', 'transceiver, twisted pair', True)]
    y = 40; hh = 40; gap = 6
    for i, (a, b, used) in enumerate(rows):
        yy = y + i * (hh + gap)
        o.append(boxt(16, yy, 190, hh, [a], ACS if used else FIGBG, AC if used else L2, 14, bold_first=used))
        o.append(boxt(222, yy, 220, hh, [b], PANEL if used else FIGBG, AC if used else L2, 13, dash=None if used else '5 4',
                      fills=[INK if used else MUT]))
    yy7 = y + 0 * (hh + gap); yy4 = y + 3 * (hh + gap); yy2 = y + 5 * (hh + gap); yy1 = y + 6 * (hh + gap)
    o.append(boxt(470, yy7, 236, hh, ['20 bytes: 3 header + 17 VIN'], LVS, LV, 13))
    w = [70, 76, 76]; x = 470
    for lab, ww in zip(['FF: 6 B', 'CF: 7 B', 'CF: 7 B'], w):
        o.append(boxt(x, yy4, ww, hh, [lab], NXS, NX, 13)); x += ww + 7
    o.append(boxt(470, yy2, 236, hh, ['3 frames, each with CRC'], PANEL, AC, 13))
    o.append(boxt(470, yy1, 236, hh, ['bits on CAN_H and CAN_L'], PANEL, AC, 13))
    for a, b in ((yy7 + hh, yy4), (yy4 + hh, yy2)):
        o.append(L(588, a + 2, 588, b - 3, LV, 2, arrow='l'))
    o.append(T(588, (yy7 + hh + yy4) / 2 + 4, '', 13))
    o.append(T(360, 378, 'Shaded layers are used; layers 3, 5 and 6 are empty in a CAN network.', 14, fill=MUT))
    return 392, ''.join(o)


# ---- 6.3 CAN frame fields and the arbitration of 0x123 against 0x121 (worked example 1) ----
def f3():
    o = [title(360, 22, 'Classic CAN data frame (field and bits)')]
    fields = [('SOF', '1'), ('ID', '11'), ('RTR', '1'), ('IDE', '1'), ('r0', '1'), ('DLC', '4'), ('Data', '0–64'),
              ('CRC', '15+1'), ('ACK', '2'), ('EOF', '7'), ('IFS', '3')]
    x = 16; w = 60
    for i, (f, b) in enumerate(fields):
        hi = f in ('ID',)
        o.append(boxt(x, 34, w, 32, [f], ACS if hi else PANEL, AC, 14, bold_first=hi))
        o.append(T(x + w / 2, 86, b, 13, fill=MUT)); x += w + 2
    o.append(T(16, 112, 'Arbitration: bit by bit, most significant first; dominant 0 beats recessive 1', 14, 'start', bold=True))
    cols = ['SOF'] + [str(b) for b in range(10, -1, -1)]
    A = '0' + '00100100011'; B = '0' + '00100100001'
    x0, cw, y0, rh = 150, 46, 128, 34
    for i, c in enumerate(cols):
        o.append(T(x0 + i * cw + cw / 2, y0 + 16, c, 13, fill=MUT))
    o.append(T(x0 - 10, y0 + 16, 'ID bit', 13, 'end', MUT))
    lose = 10  # column of identifier bit 1 (column 0 is SOF, column 1 is bit 10)
    o.append(R(x0 + lose * cw, y0 + 24, cw, 3 * rh + 6, NXS, NX, 4))
    bus = ''.join(str(min(int(a), int(b))) if i <= lose else b for i, (a, b) in enumerate(zip(A, B)))
    for r, (lab, bits) in enumerate([('Node A 0x123', A), ('Node B 0x121', B), ('Bus reads', bus)]):
        yy = y0 + 28 + r * rh
        o.append(T(x0 - 10, yy + 21, lab, 14, 'end', bold=(r == 2)))
        for i in range(12):
            if r == 0 and i > lose:
                o.append(T(x0 + i * cw + cw / 2, yy + 21, '–', 15, fill=MUT)); continue
            v = bits[i]
            o.append(T(x0 + i * cw + cw / 2, yy + 21, v, 15, fill=AC if v == '0' else MUT, bold=(v == '0')))
    o.append(Tb(x0 + lose * cw + cw / 2, y0 + 28 + 3 * rh + 22, 'A sends 1, reads 0: A stops', 14, fill=NX, bold=True))
    o.append(T(16, 300, 'A = 001 0010 0011 (291), B = 001 0010 0001 (289): B wins and its frame goes on undamaged;', 14, 'start'))
    o.append(T(16, 322, 'A receives B’s frame and tries again when the bus is idle.', 14, 'start'))
    return 338, ''.join(o)


# ---- 6.4 the LIN frame of worked example 1 to scale, and a FlexRay cycle ----
def f4():
    o = [title(16, 22, 'LIN frame, 8 data bytes at 19.2 kbit/s (1 bit = 52.08 µs)', 'start')]
    x0, px = 30, 66.0          # 66 px per ms; 10 ms slot = 660 px
    ms = lambda t: x0 + t * px
    bit = 1 / 19.2
    segs = [('Break', 14, NXS, NX), ('Sync', 10, PANEL, AC), ('PID', 10, PANEL, AC), ('Data: 8 bytes × 10 bits', 80, ACS, AC), ('Chk', 10, PANEL, AC)]
    t = 0; y = 40
    for name, b, f, s in segs:
        w = b * bit * px
        o.append(boxt(ms(t), y, w, 34, [name], f, s, 13)); t += b * bit
    o.append(T(ms(0.73 + 0.52), y + 52, 'header 34 bits', 13, fill=MUT))
    o.append(T(ms(t / 2 + 1.5), y + 52, 'response 90 bits', 13, fill=MUT))
    o.append(xaxis(x0, ms(10), 128, [0, 2, 4, 6, 8, 10], ms, None, lambda v: f'{v} ms'))
    for tt, lab, c in ((6.458, 'nominal 6.46 ms', AC), (9.042, 'max 9.04 ms', NX), (10, 'slot 10 ms', MUT)):
        o.append(L(ms(tt), 34, ms(tt), 124, c, 2, dash='5 4'))
    o.append(Tb(ms(6.458), 172, 'nominal 6.46 ms', 13, fill=AC, bold=True))
    o.append(Tb(ms(8.6), 172, 'max 9.04 ms', 13, fill=NX, bold=True))
    o.append(Tb(ms(10) - 4, 30, 'slot 10 ms', 13, 'end', MUT))
    # FlexRay cycle
    o.append(title(16, 212, 'FlexRay communication cycle (example: 5 ms on channels A and B)', 'start'))
    fx = lambda t: x0 + t * 132
    for ci, ch in enumerate(('A', 'B')):
        yy = 228 + ci * 44
        o.append(T(x0 - 8, yy + 24, ch, 14, 'end', bold=True))
        for s in range(10):
            o.append(R(fx(s * 0.3), yy, 0.3 * 132, 34, ACS if s % 3 == 0 else PANEL, AC, 2, sw=1.5))
        o.append(Tb(fx(1.5), yy + 22, 'static slots 1 … 60', 13))
        o.append(R(fx(3.0), yy, 1.5 * 132, 34, FIGBG, NX, 2, sw=1.5))
        for m in range(1, 15):
            o.append(L(fx(3.0 + m * 0.1), yy + 26, fx(3.0 + m * 0.1), yy + 34, NX, 1.2))
        o.append(R(fx(3.2), yy + 4, 0.55 * 132, 20, NXS, NX, 2, sw=1.5))
        o.append(T(fx(3.475), yy + 19, 'frame', 13, fill=NX))
        o.append(R(fx(4.5), yy, 0.1 * 132, 34, LVS, LV, 1, sw=1.5))
        o.append(R(fx(4.6), yy, 0.4 * 132, 34, FIGBG, L2, 2, sw=1.5, dash='4 3'))
    o.append(T(fx(1.5), 340, 'static 3.0 ms (TDMA)', 13, fill=AC))
    o.append(T(fx(3.75), 340, 'dynamic 1.5 ms (minislots)', 13, fill=NX))
    o.append(T(712, 362, 'symbol window 0.1 ms, idle time 0.4 ms', 13, 'end', MUT))
    o.append(L(fx(4.55), 318, fx(4.55), 346, LV, 1.5))
    return 376, ''.join(o)


# ---- 6.5 the central gateway, its buses and a MOST ring (worked example 2 delay) ----
def f5():
    o = []
    gx, gy, gw, gh = 286, 74, 100, 270
    o.append(boxt(gx, 14, gw, 34, ['OBD socket'], LVS, LV, 13))
    o.append(L(gx + gw / 2, 48, gx + gw / 2, gy, LV, 2))
    o.append(R(gx, gy, gw, gh, ACS, AC, 10))
    for i, s in enumerate(['Central', 'gateway', '', 'routing', 'table,', 'filter,', 'buffers']):
        o.append(T(gx + gw / 2, gy + 40 + i * 20, s, 14 if i < 2 else 13, bold=i < 2, fill=INK if i < 2 else MUT))
    buses = [(112, 'Powertrain CAN 500 kbit/s', ['Engine', 'Gearbox']), (212, 'Chassis CAN or FlexRay', ['ABS/ESP', 'Steering']),
             (312, 'Body CAN 125 kbit/s', ['Body ECU', 'Cluster'])]
    for y, lab, nodes in buses:
        o.append(L(20, y, gx, y, AC, 3))
        for j, n in enumerate(nodes):
            x = 34 + j * 122
            o.append(L(x + 46, y - 14, x + 46, y, AC, 2)); o.append(boxt(x, y - 44, 92, 30, [n], PANEL, AC, 13))
        o.append(T(24, y + 20, lab, 13, 'start', MUT))
    o.append(L(80, 342, 80, 368, NX, 2, dash='5 4'))
    o.append(T(92, 366, 'LIN: doors, seats', 13, 'start', NX))
    # MOST ring
    cx, cy, r = 572, 208, 84
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:var(--next);stroke-width:3"/>')
    for a in (45, 135, 225, 315):
        x1, y1 = cx + r * math.cos(math.radians(a - 8)), cy + r * math.sin(math.radians(a - 8))
        x2, y2 = cx + r * math.cos(math.radians(a + 8)), cy + r * math.sin(math.radians(a + 8))
        o.append(f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 0 1 {x2:.1f},{y2:.1f}" style="fill:none;stroke:var(--next);stroke-width:3" marker-end="url(#ar-UID-x)"/>')
    dev = [(cx - r, cy, ['Head unit', 'timing master'], NXS), (cx, cy - r, ['Amplifier'], PANEL), (cx + r, cy, ['Navigation'], PANEL), (cx, cy + r, ['Rear display'], PANEL)]
    for x, y, lines, f in dev:
        w = 100 if len(lines) > 1 else 92
        h = 42 if len(lines) > 1 else 30
        x = min(x, 712 - w / 2)
        o.append(boxt(x - w / 2, y - h / 2, w, h, lines, f, NX, 13))
    o.append(L(gx + gw, cy, cx - r - 50, cy, NX, 2.5))
    o.append(T(cx, 338, 'MOST ring: frames at 44.1 kHz', 13, fill=NX))
    o.append(T(360, 394, 'Engine frame to the body bus: 0.222 ms in + 0.20 ms gateway + 0.888 ms out = 1.31 ms', 14, bold=True))
    return 410, ''.join(o)


# ---- 6.6 the J1962 socket and the engine-speed request of worked example 1 ----
def f6():
    o = [title(360, 18, 'J1962 diagnostic socket (front view)')]
    o.append(f'<path d="M150,70 L570,70 L548,176 L172,176 Z" style="fill:var(--panel);stroke:var(--accent);stroke-width:2.5;stroke-linejoin:round"/>')
    px = lambda i: 202.5 + 45 * i
    used = {2: 'J1850 +', 4: 'chassis ground', 5: 'signal ground', 6: 'CAN high', 7: 'K-line', 10: 'J1850 −', 14: 'CAN low', 15: 'L-line', 16: 'battery +'}
    for n in range(1, 17):
        i = (n - 1) % 8; y = 100 if n <= 8 else 146
        on = n in used
        f = ACS if on else FIGBG
        if n in (6, 14): f = LVS
        if n == 16: f = NXS
        o.append(f'<circle cx="{px(i):.1f}" cy="{y}" r="15" style="fill:{f};stroke:{AC if on else L2};stroke-width:2"/>')
        o.append(T(px(i), y + 5, str(n), 13, bold=on, fill=INK if on else MUT))
    top = {2: (40, 0), 5: (40, 0), 7: (40, 28), 4: (60, -18), 6: (60, 14)}
    for n, (yl, dx) in top.items():
        x = px(n - 1)
        o.append(L(x, yl + 4, x, 84, L2, 1.5)); o.append(Tb(x + dx, yl, used[n], 13, fill=LV if n == 6 else INK))
    bot = {10: (206, 0), 14: (206, -12), 16: (206, 22), 15: (228, 0)}
    for n, (yl, dx) in bot.items():
        x = px(n - 9)
        o.append(L(x, 162, x, yl - 14, L2, 1.5)); o.append(Tb(x + dx, yl, used[n], 13, fill=LV if n == 14 else (NX if n == 16 else INK)))
    o.append(boxt(16, 262, 120, 64, ['Scan tool'], PANEL, AC, 14, True))
    o.append(boxt(584, 262, 120, 64, ['Engine ECU'], PANEL, AC, 14, True))
    o.append(L(140, 280, 580, 280, AC, 2, arrow='n')); o.append(Tb(360, 274, 'request 01 0C: live engine speed', 14))
    o.append(L(580, 312, 140, 312, LV, 2, arrow='l')); o.append(Tb(360, 306, 'reply 41 0C 1A F0', 14, fill=LV, bold=True))
    o.append(T(360, 352, '(256 × 26 + 240) ÷ 4 = 6896 ÷ 4 = 1724 rpm', 15, bold=True))
    return 368, ''.join(o)


# ---- 6.7 the FTTI budget of worked example 1 and the ASILs of worked example 2 ----
def f7():
    o = [title(16, 22, 'Fault tolerant time interval: 200 ms', 'start')]
    x0, s = 40, 3.2
    X = lambda t: x0 + t * s
    segs = [(0, 20, 'sample', PANEL, AC), (20, 60, 'confirm 40', PANEL, AC), (60, 170, 'detection logic: 110 ms', ACS, AC), (170, 200, 'act 30', NXS, NX)]
    for a, b, lab, f, c in segs:
        o.append(boxt(X(a), 44, (b - a) * s, 40, [lab], f, c, 13))
    o.append(xaxis(X(0), X(200), 100, [0, 20, 60, 170, 200], X, None, lambda v: f'{v} ms'))
    o.append(Tb(X(0) + 4, 148, 'fault occurs', 13, 'start', MUT))
    o.append(Tb(X(170), 148, 'flagged at 170 ms', 13, fill=AC, bold=True))
    o.append(Tb(X(200) - 2, 170, 'safe state by 200 ms', 13, 'end', NX, bold=True))
    o.append(title(16, 214, 'ASIL from severity + exposure + controllability', 'start'))
    rows = [('Unintended steering', 'S3 + E4 + C3 = 10', 'ASIL D', NXS, NX), ('Second hazard', 'S1 + E4 + C2 = 7', 'ASIL A', ACS, AC)]
    for i, (a, b, c, f, st) in enumerate(rows):
        y = 232 + i * 46
        o.append(boxt(16, y, 220, 36, [a], PANEL, AC, 14))
        o.append(boxt(250, y, 220, 36, [b], PANEL, AC, 14))
        o.append(L(474, y + 18, 500, y + 18, AC, 2, arrow='n'))
        o.append(boxt(506, y, 120, 36, [c], f, st, 14, True))
    o.append(T(16, 344, 'Sum 10 → D, 9 → C, 8 → B, 7 → A, 6 or less → QM', 14, 'start', MUT))
    return 360, ''.join(o)


# ---- 6.8 a blind junction: the V2X links and the 104 m warning of worked example 1 ----
def f8():
    o = []
    o.append(R(16, 222, 688, 64, FIGBG, L2, 0, sw=1.5))     # east-west road
    o.append(R(318, 16, 64, 352, FIGBG, L2, 0, sw=1.5))     # north-south road
    o.append(R(16, 222, 688, 64, FIGBG, 'none', 0, sw=0))
    o.append(R(318, 16, 64, 352, FIGBG, 'none', 0, sw=0))
    o.append(L(16, 254, 704, 254, L2, 1.5, dash='10 8')); o.append(L(350, 16, 350, 368, L2, 1.5, dash='10 8'))
    o.append(R(40, 30, 254, 170, PANEL, L2, 6))
    o.append(T(167, 108, 'Building blocks', 14, fill=MUT)); o.append(T(167, 128, 'the view', 14, fill=MUT))
    o.append(boxt(70, 262, 80, 22, ['Car 1'], ACS, AC, 13, True)); o.append(L(152, 273, 186, 273, AC, 2, arrow='n'))
    o.append(boxt(334, 40, 44, 48, ['Car', '2'], ACS, AC, 13, True)); o.append(L(356, 90, 356, 120, AC, 2, arrow='n'))
    o.append(boxt(400, 300, 70, 30, ['RSU'], NXS, NX, 13, True))
    o.append(boxt(404, 180, 92, 30, ['Pedestrian'], PANEL, AC, 13))
    o.append(boxt(574, 40, 128, 48, ['Cell tower', 'and cloud'], FIGBG, L2, 13))
    o.append(L(150, 262, 332, 82, AC, 2.5, dash='7 5'))
    o.append(Tb(224, 176, 'V2V', 14, fill=AC, bold=True))
    o.append(L(150, 280, 398, 312, NX, 2)); o.append(Tb(276, 312, 'V2I', 14, fill=NX, bold=True))
    o.append(L(378, 74, 404, 186, LV, 2)); o.append(Tb(424, 140, 'V2P', 14, fill=LV, bold=True))
    o.append(L(378, 56, 572, 60, MUT, 2, dash='3 4')); o.append(Tb(476, 50, 'V2N', 14, fill=MUT, bold=True))
    o.append(T(560, 252 - 12, 'closing 40 m/s', 13, fill=INK))
    o.append(T(560, 232 + 58 + 18, 'warn at 40 × (2.5 + 0.1)', 13, fill=INK))
    o.append(T(560, 232 + 58 + 38, '= 104 m', 14, fill=NX, bold=True))
    return 384, ''.join(o)


# ---- 6.9 greedy forwarding of worked example 1, to scale ----
def f9():
    o = []
    X = lambda x: 80 + 5 * x
    Y = lambda y: 222 - 5 * y
    o.append(xaxis(X(0), X(100), 366, [0, 20, 40, 60, 80, 100], X, 'x (m)'))
    pts = {'S': (0, 0), 'D': (100, 0), 'A': (40, 10), 'B': (70, -20), 'C': (20, 30)}
    dist = {'A': 60.8, 'B': 36.1, 'C': 85.4}
    for n in 'ACB':
        x, y = pts[n]
        c = NX if n == 'B' else L2
        o.append(L(X(x), Y(y), X(100) - 14 * (100 - x) / dist[n] / 1, Y(0) + 14 * (y / dist[n]), c, 2 if n == 'B' else 1.6, dash=None if n == 'B' else '5 4'))
        mx, my = (X(x) + X(100)) / 2, (Y(y) + Y(0)) / 2
        o.append(Tb(mx + (0 if n != 'C' else 20), my + (18 if n == 'B' else -6), f'{dist[n]} m', 13, fill=NX if n == 'B' else MUT, bold=n == 'B'))
    o.append(L(X(0) + 12, Y(0) + 6, X(70) - 14, Y(-20) - 4, NX, 3, arrow='x'))
    for n, (x, y) in pts.items():
        col = AC if n in 'SD' else (NX if n == 'B' else PANEL)
        o.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="13" style="fill:{col};stroke:var(--accent);stroke-width:2"/>')
        o.append(T(X(x), Y(y) + 5, n, 13, bold=True, fill='var(--panel)' if n in 'SD' else INK))
    o.append(T(X(0), Y(0) - 22, 'sender (0, 0)', 13, fill=MUT)); o.append(T(X(100) - 4, Y(0) - 22, 'destination (100, 0)', 13, fill=MUT))
    o.append(T(X(40) + 4, Y(10) - 20, 'A (40, 10)', 13, fill=MUT)); o.append(T(X(20), Y(30) - 20, 'C (20, 30)', 13, fill=MUT))
    o.append(T(X(70), Y(-20) + 32, 'B (70, −20)', 13, fill=NX, bold=True))
    o.append(T(620, 300, 'greedy choice:', 13, fill=NX)); o.append(T(620, 320, 'B, 36.1 m', 14, fill=NX, bold=True))
    o.append(T(16, 24, 'Distance from each neighbour to the destination; the closest one gets the packet.', 14, 'start'))
    return 412, ''.join(o)


# ---- 6.10 the WAVE stack and the 1609.4 channel rhythm of worked example 1 ----
def f10():
    o = []
    layers = [('Applications: BSM (SAE J2735), 10 per second', PANEL, AC), (None, None, None),
              ('IEEE 1609.4: CCH / SCH switching', ACS, AC), ('802.11p MAC: OCB, EDCA', PANEL, AC),
              ('802.11p PHY: OFDM, 10 MHz', PANEL, AC), ('5.9 GHz radio band', FIGBG, L2)]
    y = 16; h = 38; g = 6
    for i, (lab, f, s) in enumerate(layers):
        yy = y + i * (h + g)
        if lab is None:
            o.append(boxt(16, yy, 200, h, ['1609.3: WSMP'], PANEL, AC, 13))
            o.append(boxt(224, yy, 220, h, ['1609.3: IPv6, UDP / TCP'], PANEL, AC, 13))
        else:
            o.append(boxt(16, yy, 428, h, [lab], f, s, 13, bold_first=(i == 2)))
    o.append(R(456, y, 92, 6 * h + 5 * g, NXS, NX, 8))
    for i, s in enumerate(['IEEE', '1609.2', 'security:', 'signed', 'messages,', 'certificates']):
        o.append(T(502, y + 60 + i * 22, s, 13, bold=i < 2, fill=INK if i < 2 else NX))
    o.append(T(632, 70, 'BSM airtime', 13, fill=MUT)); o.append(T(632, 90, '2400 bits ÷ 6 Mbit/s', 13))
    o.append(T(632, 110, '= 0.4 ms', 14, bold=True))
    o.append(T(632, 160, '45 ÷ 0.4 = 112.5', 13)); o.append(T(632, 180, '→ 112 per', 13)); o.append(T(632, 200, 'CCH interval', 13))
    # channel rhythm
    yb = 330; x0 = 40; s = 6.4
    o.append(title(16, yb - 22, 'One 100 ms sync interval (IEEE 1609.4)', 'start'))
    o.append(R(x0, yb, 50 * s, 40, ACS, AC, 4)); o.append(R(x0 + 50 * s, yb, 50 * s, 40, FIGBG, L2, 4))
    for k in range(0, 112, 4):
        xx = x0 + 2.5 * s + k * 0.4 * s
        o.append(L(xx, yb + 4, xx, yb + 14, AC, 1.2))
    o.append(T(x0 + 25 * s, yb + 32, 'CCH 50 ms: safety messages', 13, bold=True))
    o.append(T(x0 + 75 * s, yb + 26, 'SCH 50 ms: other services', 13, fill=MUT))
    o.append(xaxis(x0, x0 + 100 * s, yb + 46, [0, 50, 100], lambda v: x0 + v * s, None, lambda v: f'{v} ms'))
    o.append(T(x0 + 25 * s, yb + 90, '45 ms usable after 10 per cent for guard and contention', 13, fill=MUT))
    return 434, ''.join(o)


FIG = {
    1: (f1, 'Six ECUs wired point to point need 15 links; on a bus they share one twisted pair, each with its own transceiver and a 120 Ω terminator at each end. The worked example makes the same count for 12 ECUs.',
        'Left: six ECUs joined by 15 crossing links. Right: the same six ECUs tapping one two-wire bus with a terminator at each end.'),
    2: (f2, 'The seven OSI layers and what a CAN network puts in each. In the worked example the 20-byte VIN reply is cut by the transport layer into a first frame of 6 bytes and two consecutive frames of 7.',
        'Seven layer boxes; layers 7, 4, 2 and 1 are used by CAN and 3, 5 and 6 are empty; a side column shows the 20-byte reply split into 6, 7 and 7 bytes.'),
    3: (f3, 'The fields of a classic CAN frame, and the arbitration of the worked example. Both nodes send the same bits until identifier bit 1, where A’s recessive 1 meets B’s dominant 0; A stops and B carries on.',
        'Frame field strip, then a bit table for nodes A and B and the bus from start of frame to identifier bit 0, with bit 1 highlighted.'),
    4: (f4, 'Top: the LIN frame of the worked example to scale in its 10 ms slot; even the maximum frame time fits. Bottom: an example 5 ms FlexRay cycle with static slots, minislots, symbol window and idle time on both channels.',
        'A time bar of a LIN frame with break, sync, PID, eight data bytes and checksum against 0 to 10 ms, and two rows of a FlexRay cycle.'),
    5: (f5, 'A central gateway joins the powertrain, chassis and body buses, a MOST ring for media and the OBD socket. A frame crossing from the powertrain bus to the body bus takes 1.31 ms in the worked example.',
        'Gateway box with three CAN buses on the left, the OBD socket on top and a four-device MOST ring on the right with the head unit as timing master.'),
    6: (f6, 'The 16 pins of the J1962 socket, with the ones the standard fixes labelled, and the engine-speed request and reply of the worked example.',
        'Trapezoid socket with two rows of eight pins; pins 2, 4, 5, 6, 7, 10, 14, 15 and 16 labelled; below, a scan tool sends 01 0C and the ECU replies 41 0C 1A F0, 1724 rpm.'),
    7: (f7, 'Top: the 200 ms budget of the first worked example; the fault must be flagged by 170 ms so the actuator can reach the safe state in time. Bottom: the two ASILs of the second worked example.',
        'Time bar from 0 to 200 ms split into sampling, confirmation, detection and actuation, and two rows adding S, E and C ratings to give ASIL D and ASIL A.'),
    8: (f8, 'A blind junction: a building hides the two cars from each other, but V2V, V2I, V2P and V2N messages do not need a line of sight. In the worked example the warning must go out 104 m before the collision point.',
        'Crossroads with a building at one corner, Car 1 and Car 2 approaching, a roadside unit, a pedestrian and a cell tower, joined by labelled links.'),
    9: (f9, 'The worked example to scale. Of the three neighbours, B is closest to the destination, 36.1 m away, so greedy forwarding sends the packet to B.',
        'Plot with the sender at 0, 0 and the destination at 100, 0; neighbours A, B and C with their distances to the destination; an arrow from the sender to B.'),
    10: (f10, 'The WAVE stack: 802.11p at the bottom, IEEE 1609.3 and 1609.4 above it and 1609.2 security beside every layer. Below, the 100 ms sync interval in which the worked example fits 112 safety messages into the control-channel half.',
         'Layer stack from radio band to applications with a security column, and a bar of a 100 ms interval split into a control-channel half and a service-channel half.'),
}
spec = make_spec(FIG)
