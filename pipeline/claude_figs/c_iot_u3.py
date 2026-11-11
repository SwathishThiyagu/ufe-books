"""Claude's hand-drawn figures for c-iot-u3 (Internet of Things, unit 3: IoT communication protocols),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {1: 2, 4: 2, 5: 2, 7: 1}


# ---- 3.1 headers added on the way down a 4-layer stack ----
def f1():
    o = [T(20, 24, 'Sending: each layer puts its header in front of what it receives', 14, 'start', bold=True)]
    s = 530 / 134
    x0 = 100
    rows = [('application', [], '100 B'), ('layer 4', [20], '120 B'), ('layer 3', [8, 20], '128 B'), ('layer 2', [4, 8, 20], '132 B'), ('layer 1', [2, 4, 8, 20], '134 B')]
    for i, (name, hs, tot) in enumerate(rows):
        y = 44 + i * 50
        o.append(T(x0 - 10, y + 22, name, 13, 'end', MUT, True))
        x = x0
        for j, h in enumerate(hs):
            new = j == 0
            o.append(R(x, y, h * s, 32, NXS if new else 'var(--line)', NX if new else L2, 2, 1.3))
            if new and h >= 8: o.append(T(x + h * s / 2, y + 21, f'+{h}', 13, fill=NX, bold=True))
            x += h * s
        if hs and hs[0] < 8: o.append(T(x0 - 4, y - 5, f'+{hs[0]}', 13, 'start', NX, True))
        o.append(R(x, y, 100 * s, 32, ACS, AC, 2, 1.5))
        o.append(T(x + 50 * s, y + 21, 'payload 100 B', 13))
        o.append(T(x + 100 * s + 8, y + 21, tot, 13, 'start', bold=True))
    o.append(T(20, 316, 'Headers: 2 + 4 + 8 + 20 = 34 B.  Packet: 100 + 34 = 134 B.', 14, 'start'))
    o.append(T(20, 340, 'Overhead = 34 ÷ 134 = 25.4% of the final packet (divide by 134, not by 100).', 14, 'start', NX, True))
    return 356, ''.join(o)
FIG[1] = (f1, 'On the way down the stack each layer adds its header in front: 20 B, then 8, 4 and 2, so the 100 B payload leaves as a 134 B packet and the 34 header bytes are 25.4% of it.',
          'Five stacked bars: the 100-byte payload, then layer 4 adds 20 bytes, layer 3 adds 8, layer 2 adds 4 and layer 1 adds 2, growing the bar to 134 bytes; text gives the overhead 34 over 134 as 25.4 percent.')


# ---- 3.2 time on air of an 802.15.4 frame ----
def f2():
    o = [T(20, 24, 'One frame on air: 6 B of PHY overhead + 127 B PSDU = 133 B', 14, 'start', bold=True)]
    x0, W = 40, 640
    s = W / 133
    segs = [('preamble', 4, NXS, NX), ('SFD', 1, NXS, NX), ('length', 1, NXS, NX), ('PSDU (MAC frame) 127 B', 127, ACS, AC)]
    x = x0
    for name, b, f, st in segs:
        o.append(R(x, 56, b * s, 40, f, st, 2, 1.5))
        if b > 50: o.append(T(x + b * s / 2, 81, name, 14, bold=True))
        x += b * s
    o.append(L(x0 + 2 * s, 54, x0 + 2 * s, 40, MUT, 1.2)); o.append(T(x0 + 2 * s + 6, 44, 'preamble 4 B, SFD 1 B, length 1 B', 13, 'start', MUT))
    # the same bar as a time axis
    o.append(xaxis(x0, x0 + W, 112, [], lambda v: v))
    for b, lab in ((0, '0'), (6, '0.192 ms'), (133, '4.256 ms')):
        X = x0 + b * s
        o.append(L(X, 112, X, 118, L2, 1.5))
        o.append(T(X, 134, lab, 13, 'start' if b == 6 else ('end' if b == 133 else 'middle'), MUT))
    o.append(T(20, 178, 'Bits and time at 250 kbps', 15, 'start', bold=True))
    o.append(boxt(20, 194, 200, 56, ['133 B × 8', '= 1,064 bits'], PANEL, AC, 14, True))
    o.append(L(222, 222, 262, 222, AC, 2, arrow='n'))
    o.append(boxt(266, 194, 200, 56, ['each bit lasts', '1 ÷ 250,000 = 4 µs'], PANEL, AC, 14, True))
    o.append(L(468, 222, 508, 222, AC, 2, arrow='n'))
    o.append(boxt(512, 194, 188, 56, ['time on air', '1,064 × 4 µs = 4.256 ms'], NXS, NX, 14, True))
    return 266, ''.join(o)
FIG[2] = (f2, 'The PHY adds a 4 B preamble, 1 B SFD and 1 B length to the 127 B PSDU, so 133 B (1,064 bits) go on air; at 250 kbps each bit lasts 4 µs and the frame takes 4.256 ms.',
          'A bar of 133 bytes with three thin overhead fields and a long 127-byte PSDU, doubling as a time axis from 0 to 4.256 milliseconds; three boxes give 1,064 bits, 4 microseconds a bit, 4.256 milliseconds.')


# ---- 3.3 ZigBee parents and child slots ----
def f3():
    o = []
    def panel(x0, title, parents, filled, failed, orphans):
        o.append(T(x0, 24, title, 15, 'start', bold=True))
        for i, name in enumerate(parents):
            y = 42 + i * 44
            dead = name in failed
            o.append(boxt(x0, y, 54, 34, [name], NXS if name == 'C' else PANEL, L2 if dead else (NX if name == 'C' else AC), 14, True, dash='5 4' if dead else None))
            for j in range(6):
                cx = x0 + 70 + j * 32
                if dead:
                    o.append(R(cx, y + 5, 24, 24, 'none', L2, 4, 1.2, '3 3'))
                else:
                    on = j < filled[i]
                    o.append(R(cx, y + 5, 24, 24, ACS if on else PANEL, AC if on else L2, 4, 1.5))
                    if on: o.append(C(cx + 12, y + 17, 5, AC))
            if dead: o.append(T(x0 + 70 + 6 * 32 + 4, y + 22, 'failed', 13, 'start', MUT))
        for j in range(orphans):
            o.append(C(x0 + 82 + j * 32, 42 + len(parents) * 44 + 10, 7, LV))
        if orphans: o.append(T(x0 + 82 + orphans * 32, 42 + len(parents) * 44 + 15, f'{orphans} end devices, no parent', 13, 'start', LV, True))
    panel(10, 'Start: 5 parents × 6 = 30 slots', ['C', 'R1', 'R2', 'R3', 'R4'], [4, 4, 4, 4, 4], [], 0)
    panel(372, 'After 2 routers fail: 3 × 6 = 18', ['C', 'R1', 'R2', 'R3', 'R4'], [6, 6, 6, 0, 0], ['R3', 'R4'], 2)
    o.append(T(10, 312, '20 end devices fit in 30 slots; 10 stay free.', 14, 'start'))
    o.append(T(372, 312, '20 − 18 = 2 end devices lose their parent.', 14, 'start', LV, True))
    o.append(C(16, 340, 5, AC)); o.append(T(28, 345, 'end device in a slot', 13, 'start', MUT))
    o.append(R(180, 334, 14, 14, PANEL, L2, 3, 1.5)); o.append(T(200, 345, 'free slot', 13, 'start', MUT))
    o.append(T(290, 345, 'C = coordinator, R = router (each takes up to 6 children)', 13, 'start', MUT))
    return 360, ''.join(o)
FIG[3] = (f3, 'With a coordinator and 4 routers taking 6 children each there are 30 slots, so all 20 end devices join and 10 slots stay free; when 2 routers fail only 18 slots remain and 2 end devices are left without a parent.',
          'Two panels of parent rows, each with six child slots. Left: coordinator and four routers with 20 slots filled and 10 free. Right: two routers failed, the remaining three parents full with 18 devices and two orphan devices below.')


# ---- 3.4 BLE throughput from connection events ----
def f4():
    o = [T(20, 24, 'One second of a BLE link: a connection event every 50 ms', 14, 'start', bold=True)]
    x0, x1 = 40, 680
    fx = lambda t: x0 + t / 1000 * (x1 - x0)
    o.append(L(x0, 76, x1, 76, L2, 1.5))
    for i in range(20):
        o.append(R(fx(i * 50) + 1, 52, 9, 24, ACS if i else NXS, AC if i else NX, 2, 1.3))
    for t in (250, 500, 750, 1000):
        o.append(L(fx(t), 76, fx(t), 82, L2, 1.5)); o.append(T(fx(t), 98, f'{t} ms', 13, fill=MUT))
    o.append(T(x1, 46, '1 ÷ 0.050 s = 20 events', 13, 'end', AC, True))
    # zoom on event 1
    o.append(L(fx(0) + 3, 106, 120, 140, NX, 1.3, '4 4')); o.append(L(fx(0) + 12, 106, 600, 140, NX, 1.3, '4 4')); o.append(L(fx(0) + 5, 78, fx(0) + 5, 106, NX, 1.3, '4 4'))
    o.append(R(40, 140, 640, 96, PANEL, NX, 8, 1.5))
    o.append(T(56, 162, 'inside one event: 4 packets, 20 B of data each', 13, 'start', NX, True))
    lab = ['central → peripheral', 'peripheral → central', 'central → peripheral', 'peripheral → central']
    for i in range(4):
        x = 56 + i * 154
        o.append(boxt(x, 176, 140, 46, ['20 B = 160 bits', lab[i]], ACS, AC, 13, True))
    o.append(T(20, 266, '4 × 160 = 640 bits per event', 14, 'start'))
    o.append(T(20, 290, '640 bits × 20 events a second = 12,800 bps = 12.8 kbps', 15, 'start', NX, True))
    return 306, ''.join(o)
FIG[4] = (f4, 'A 50 ms connection interval gives 20 connection events a second; each event exchanges 4 packets of 20 B (640 bits), so the link carries 640 × 20 = 12,800 bps, or 12.8 kbps, of application data.',
          'A one-second timeline with 20 small connection events, the first zoomed to show four 20-byte packets alternating between central and peripheral; text multiplies 640 bits by 20 events to get 12.8 kbps.')


# ---- 3.5 fragmenting a 1280-byte IPv6 packet ----
def f5():
    o = [T(20, 24, 'One 802.15.4 frame: 127 B, of which 25 B are 6LoWPAN and MAC overhead', 14, 'start', bold=True)]
    s = 600 / 127
    o.append(R(40, 40, 25 * s, 34, NXS, NX, 3, 1.5)); o.append(T(40 + 12.5 * s, 62, '25 B', 13, fill=NX, bold=True))
    o.append(R(40 + 25 * s, 40, 102 * s, 34, ACS, AC, 3, 1.5)); o.append(T(40 + 25 * s + 51 * s, 62, 'usable 127 − 25 = 102 B', 14, bold=True))
    o.append(T(20, 114, 'The 1,280 B IPv6 packet cut into 102 B pieces', 14, 'start', bold=True))
    x0, W = 40, 640
    ps = W / 1280
    x = x0
    for i in range(13):
        b = 102 if i < 12 else 56
        o.append(R(x, 128, b * ps, 40, ACS if i < 12 else LVS, AC if i < 12 else LV, 2, 1.3))
        o.append(T(x + b * ps / 2, 153, str(i + 1), 13, fill=INK if i < 12 else LV, bold=i == 12))
        x += b * ps
    o.append(brace(x0, x0 + 1224 * ps, 178, AC))
    o.append(T(x0 + 612 * ps, 200, '12 full fragments × 102 B = 1,224 B', 13, fill=AC, bold=True))
    o.append(L(x0 + 1252 * ps, 172, x0 + 1252 * ps, 214, LV, 1.3))
    o.append(T(x0 + 1280 * ps, 232, 'last: 1,280 − 1,224 = 56 B', 13, 'end', LV, True))
    o.append(T(20, 270, '1,280 ÷ 102 = 12.55, and a part-filled frame still needs a frame: round up to 13 fragments.', 14, 'start', NX, True))
    return 286, ''.join(o)
FIG[5] = (f5, 'Each 127 B frame keeps 102 B for data after 25 B of overhead, so a 1,280 B IPv6 packet needs 12 full fragments of 102 B and a 13th carrying the last 56 B.',
          'A frame bar split into 25 bytes of overhead and 102 usable bytes; below, a 1,280-byte packet cut into 12 pieces of 102 bytes and a short 13th piece of 56 bytes.')


# ---- 3.6 MQTT fan-out at QoS 1 ----
def f6():
    o = []
    o.append(boxt(20, 110, 150, 64, ['Sensor', 'publishes every 10 s'], PANEL, AC, 13, True))
    o.append(L(172, 142, 262, 142, AC, 2.5, arrow='n'))
    o.append(Tb(217, 132, 'PUBLISH', 13, fill=AC, bold=True))
    o.append(boxt(266, 104, 150, 76, ['Broker', 'topic home/room1/temp', '3 subscribers'], ACS, AC, 13, True))
    for i in range(3):
        y = 30 + i * 112
        o.append(L(418, 142, 520, y + 26, AC, 2, arrow='n'))
        o.append(boxt(524, y, 176, 52, [f'Subscriber {i + 1}', 'receives 22 B'], PANEL, AC, 13, True))
    # message layout
    s = 8
    o.append(T(20, 222, 'one PUBLISH:', 13, 'start', MUT))
    o.append(R(20, 230, 2 * s, 26, NXS, NX, 2, 1.3)); o.append(R(20 + 2 * s, 230, 20 * s, 26, ACS, AC, 2, 1.3))
    o.append(T(20 + 12 * s, 248, '20 B payload', 13, bold=True)); o.append(T(16 + 22 * s + 10, 248, '+ 2 B header = 22 B', 13, 'start', NX, True))
    o.append(T(20, 300, 'Per message: 3 × 22 = 66 B.   Per hour: 3,600 ÷ 10 = 360 messages.', 14, 'start'))
    o.append(T(20, 324, 'Broker sends 360 × 66 = 23,760 B = 23.76 kB an hour (ACKs not counted).', 14, 'start', NX, True))
    return 340, ''.join(o)
FIG[6] = (f6, 'Each 20 B reading leaves the broker as three 22 B PUBLISH messages, one per subscriber, so 360 readings an hour make the broker send 360 × 66 = 23,760 B, about 23.76 kB.',
          'A sensor sends one PUBLISH to the broker, which copies it to three subscribers; a small bar shows the 2-byte header and 20-byte payload; text gives 66 bytes per message and 23.76 kB per hour.')


# ---- 3.7 LoRa time on air ----
def f7():
    o = [T(20, 24, 'SF9 at 125 kHz: one symbol = 2⁹ ÷ 125,000 = 512 ÷ 125,000 s = 4.096 ms', 14, 'start', bold=True)]
    x0, W = 40, 640
    fx = lambda t: x0 + t / 196.608 * W
    for i in range(48):
        pre = i < 8
        o.append(R(fx(i * 4.096) + 0.5, 50, W / 48 - 1.5, 40, LVS if pre else ACS, LV if pre else AC, 2, 1.1))
    o.append(brace(fx(0), fx(32.768), 100, LV))
    o.append(T(fx(0), 124, '8 preamble symbols', 13, 'start', LV, True))
    o.append(T(fx(0), 142, '8 × 4.096 = 32.768 ms', 13, 'start', LV))
    o.append(brace(fx(32.768), fx(196.608), 100, AC))
    o.append(T(fx(114), 124, '40 payload symbols', 13, fill=AC, bold=True))
    o.append(T(fx(114), 142, '40 × 4.096 = 163.84 ms', 13, fill=AC))
    o.append(xaxis(x0, x0 + W, 170, [0, 50, 100, 150], fx, None, lambda v: f'{v} ms'))
    o.append(L(fx(196.608), 170, fx(196.608), 176, L2, 1.5))
    o.append(T(fx(196.608), 192, '196.6', 13, 'end', MUT))
    o.append(T(20, 230, 'Time on air = (8 + 40) × 4.096 ms = 48 × 4.096 = 196.608 ms ≈ 196.6 ms', 15, 'start', NX, True))
    o.append(T(20, 254, 'Each step up in SF doubles the symbol time, so the same packet at SF10 takes twice as long.', 13, 'start', MUT))
    return 270, ''.join(o)
FIG[7] = (f7, 'At SF9 and 125 kHz each LoRa symbol lasts 4.096 ms, so the 8 preamble symbols take 32.768 ms, the 40 payload symbols take 163.84 ms, and the whole packet is on air for 196.608 ms.',
          'A row of 48 equal symbol cells along a time axis to 196.6 milliseconds, the first 8 shaded as preamble and the other 40 as payload, with brackets giving 32.768 and 163.84 milliseconds.')


# ---- 3.8 WirelessHART slots and effective rate ----
def f8():
    o = []
    x0, W = 40, 640
    fx = lambda t: x0 + t / 1000 * W
    def strip(y, n, mine, title, note, rep=1, ndy=56):
        o.append(T(20, y - 12, title, 14, 'start', bold=True))
        for r in range(rep):
            for i in range(n):
                t = r * n * 10 + i * 10
                on = i in mine
                o.append(R(fx(t) + 0.4, y, W / 100 - 0.8, 34, NXS if on else PANEL, NX if on else 'var(--line)', 1, 1.6 if on else 0.8))
        o.append(T(20, y + ndy, note, 13, 'start', NX, True))
    strip(44, 100, {12, 45, 78}, 'Device 1: superframe of 100 slots × 10 ms = 1,000 ms; it owns 3 slots of 80 B',
          '3 × 80 = 240 B = 1,920 bits each second → 1,920 bps', ndy=82)
    o.append(xaxis(x0, x0 + W, 82, [0, 250, 500, 750, 1000], fx, None, lambda v: f'{v} ms'))
    strip(172, 50, {10, 35}, 'Device 2: superframe of 50 slots = 500 ms; it owns 2 slots of 60 B (shown twice)',
          '2 × 60 = 120 B = 960 bits every 0.5 s → 960 ÷ 0.5 = 1,920 bps', rep=2)
    o.append(L(fx(500), 166, fx(500), 212, INK, 2, '4 3'))
    o.append(T(20, 268, 'The radio runs at 250 kbps, but each device gets only its own slots: 1.92 kbps here.', 14, 'start', MUT))
    return 284, ''.join(o)
FIG[8] = (f8, 'A superframe of 100 slots of 10 ms repeats every second; a device that owns 3 slots of 80 B sends 240 B, or 1,920 bits, a second. A second device with 2 slots of 60 B in a 500 ms superframe also gets 1,920 bps.',
          'Two strips of timeslots over one second: the first has 100 slots with 3 highlighted, the second has two 50-slot superframes each with 2 highlighted; both give 1,920 bits per second.')


# ---- 3.9 mDNS / DNS-SD browsing and TTLs ----
def f9():
    o = []
    steps = [['PTR query', '_ipp._tcp.local'], ['PTR answer', 'MyPrinter instance'], ['SRV + TXT', 'printer.local : 631'], ['A record', '192.168.1.20'], ['TCP to 631', 'printing starts']]
    w, gap = 128, 14
    for i, lines in enumerate(steps):
        x = 10 + i * (w + gap)
        o.append(boxt(x, 18, w, 56, lines, NXS if i == 4 else PANEL, NX if i == 4 else AC, 13, True))
        if i < 4: o.append(L(x + w + 1, 46, x + w + gap - 2, 46, AC, 2, arrow='n'))
    o.append(T(10, 100, 'SRV gives a host name, not an address: the A record is a separate lookup.', 13, 'start', MUT))
    # TTL timeline
    o.append(T(10, 140, 'Cache after the answers at t = 0', 15, 'start', bold=True))
    x0, x1 = 90, 690
    fx = lambda t: x0 + t / 300 * (x1 - x0)
    rows = [('PTR', 4500, '4,500 − 200 = 4,300 s left'), ('SRV', 120, 'expired 80 s ago'), ('TXT', 4500, '4,500 − 200 = 4,300 s left')]
    for i, (n, ttl, note) in enumerate(rows):
        y = 160 + i * 42
        o.append(T(x0 - 10, y + 19, n, 14, 'end', bold=True))
        end = min(ttl, 300)
        o.append(R(fx(0), y, fx(end) - fx(0), 26, ACS if ttl > 300 else LVS, AC if ttl > 300 else LV, 3, 1.5))
        if ttl > 300:
            o.append(L(fx(290), y + 13, fx(300) + 2, y + 13, AC, 2, arrow='n'))
            o.append(T(fx(205), y + 18, note, 13, 'start'))
        else:
            o.append(T(fx(12), y + 18, 'TTL 120 s', 13, 'start'))
            o.append(T(fx(205), y + 18, note, 13, 'start', LV, True))
    o.append(xaxis(x0, x1, 290, [0, 60, 120, 180, 240, 300], fx, 'time since the answers (s)', lambda v: str(v)))
    o.append(L(fx(200), 152, fx(200), 290, NX, 2.5, '6 4'))
    o.append(Tb(fx(200), 150, 't = 200 s', 13, 'middle', NX, True))
    o.append(T(10, 360, 'At t = 200 s use the cached instance name and TXT, but ask for SRV again before connecting.', 13, 'start', MUT))
    return 374, ''.join(o)
FIG[9] = (f9, 'Browsing goes PTR, then SRV and TXT, then the A record, then TCP to port 631. At t = 200 s the PTR and TXT records still have 4,300 s left, but the 120 s SRV record expired 80 s earlier and must be asked again.',
          'Five boxes from the PTR query through SRV and TXT and the A record to a TCP connection on port 631; below, cache bars on a 0 to 300 second axis: PTR and TXT run past the end, SRV stops at 120 seconds, and a dashed line marks t equals 200 seconds.')


TEXT = {
    1: [('Figure 3.1 shows a five-layer IoT stack.', 'A common IoT stack has five layers, described here from the top down.')],
    5: [('The figure shows RPL\'s tree view: a root at rank 0, routers at rank 1, and end devices deeper.',
         'In RPL\'s tree view the root sits at rank 0, routers at rank 1, and end devices deeper.')],
    7: [('Figure 3.7.1 shows the chain.', 'Data passes along that chain in order: end device, gateway, network server, application server.')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
