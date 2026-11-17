"""Claude's hand-drawn figures for c-dist-u4 (Parallel and Distributed Computing, unit 4: distributed systems, messages,
RPC, models, clocks, snapshots and ordered multicast), one per chapter, from each chapter's worked example, plus text fixes
(no university names in the books)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def seg(x, y, w, h, s, f, st, size=13):
    o = R(x, y, w, h, f, st, 4)
    if s and tw(s, size) < w - 6: o += T(x + w / 2, y + h / 2 + size * 0.36, s, size)
    return o


def proc(y, name, x0=90, x1=690):
    return T(x0 - 14, y + 5, name, 15, 'end', bold=True) + L(x0, y, x1, y, L2, 2, arrow='m')


def ev(x, y, lab, above=True, c=AC, size=13, bold=False, fill=None):
    return C(x, y, 7, c, fill) + Tb(x, y - 14 if above else y + 26, lab, size, fill=INK, bold=bold)


def msg(x1, y1, x2, y2, lab=None, c=AC, dash='7 5', arrow='n', lx=0, ly=0, size=13):
    o = L(x1, y1, x2, y2 - (8 if y2 > y1 else -8), c, 2, dash, arrow)
    if lab: o += Tb((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, lab, size, fill=c)
    return o


# ---- 4.1 8 machines on a LAN vs one machine ----
def f1():
    fx = lambda t: 180 + t * 4.7
    o = [T(20, 24, 'A job of 100 s CPU work, split 8 ways', 15, 'start', bold=True)]
    rows = [('1 machine', [(100, 'compute 100 s', PANEL, L2)], '100 s'),
            ('8 machines on a LAN', [(12.5, '', ACS, AC), (10, '', LVS, LV)], '22.5 s'),
            ('ideal 8-core machine', [(12.5, '', ACS, AC)], '12.5 s')]
    for i, (lab, segs, tot) in enumerate(rows):
        y = 46 + i * 56
        o.append(T(170, y + 22, lab, 14, 'end'))
        t = 0
        for d, s, f, st in segs:
            o.append(seg(fx(t), y, fx(t + d) - fx(t), 32, s, f, st)); t += d
        o.append(T(fx(t) + 8, y + 22, tot, 14, 'start', bold=True))
    o.append(T(fx(6.25), 152, '12.5 s', 12, fill=AC)); o.append(T(fx(17.5), 152, '10 s', 12, fill=LV))
    o.append(T(fx(25) + 50, 152, 'compute 12.5 s + messages 5000 × 2 ms = 10 s', 13, 'start', MUT))
    o.append(xaxis(fx(0), fx(100), 222, [0, 20, 40, 60, 80, 100], fx, 'time (s)'))
    o.append(boxt(30, 288, 320, 50, ['8 machines: S = 100 ÷ 22.5 = 4.44', 'E = 4.44 ÷ 8 = 55.6 %'], LVS, LV, 14))
    o.append(boxt(370, 288, 320, 50, ['ideal shared memory: S = 8', 'E = 100 % (no messages)'], ACS, AC, 14))
    return 350, ''.join(o)
FIG[1] = (f1, 'Each of 8 machines computes 12.5 s, but the 5000 messages at 2 ms add 10 s, so the job takes 22.5 s: speedup 4.44 and efficiency 55.6 %. An ideal 8-core shared-memory machine would take 12.5 s.',
          'Three bars: one machine taking 100 seconds, eight machines taking 12.5 seconds of compute plus 10 seconds of messages, and an ideal eight-core machine taking 12.5 seconds.')


# ---- 4.2 startup latency: one big vs many small messages ----
def f2():
    fx = lambda t: 200 + t * 8.2
    o = [T(20, 24, 'Link: 1 Gbps = 125 MB/s, startup latency 50 µs', 15, 'start', bold=True)]
    o.append(T(190, 66, 'one 1 MB message', 14, 'end'))
    o.append(seg(fx(0), 48, fx(8.05) - fx(0), 30, '8.05 ms', ACS, AC))
    o.append(T(fx(8.05) + 8, 62, '0.05 ms startup + 8.0 ms transfer', 12, 'start', MUT))
    o.append(T(190, 122, '1000 messages', 14, 'end')); o.append(T(190, 138, 'of 1 KB', 14, 'end'))
    for i in range(0, 58, 1):
        o.append(R(fx(i), 106, 8.2 * 50 / 58, 30, LVS, LV, 0, 0.6))
        o.append(R(fx(i) + 8.2 * 50 / 58, 106, 8.2 * 8 / 58, 30, ACS, AC, 0, 0.6))
    o.append(T(fx(58) - 4, 158, '1000 × 58 µs = 58.0 ms', 14, 'end', bold=True))
    o.append(xaxis(fx(0), fx(58), 176, [0, 10, 20, 30, 40, 50, 58], fx, 'time (ms)'))
    # zoom of one small message
    o.append(T(20, 258, 'one small message:', 14, 'start', bold=True))
    o.append(seg(170, 240, 400, 30, 'startup 50 µs', LVS, LV, 14))
    o.append(seg(570, 240, 64, 30, '8 µs', ACS, AC, 13))
    o.append(T(644, 260, '= 58 µs', 14, 'start'))
    o.append(T(20, 304, 'Startup dominates small messages: 58.0 ÷ 8.05 ≈ 7.2 times slower than one big send.', 14, 'start'))
    return 320, ''.join(o)
FIG[2] = (f2, 'Sent as one message, 1 MB takes 8.05 ms. Sent as 1000 messages of 1 KB, each pays the 50 µs startup again for only 8 µs of transfer, so the total is 58.0 ms, about 7.2 times slower.',
          'A short bar of 8.05 milliseconds for one large message against a long striped bar of 58 milliseconds for a thousand small ones, with a zoom showing one small message as 50 microseconds startup and 8 microseconds transfer.')


# ---- 4.3 the RPC path ----
def f3():
    names = ['client', 'client stub', 'network', 'server stub', 'server']
    notes = ['calls add(a, b)', 'marshals the call', '', 'unmarshals, calls', 'runs add']
    o = []
    for i, n in enumerate(names):
        x = 20 + i * 140
        f, st = (NXS, NX) if i == 2 else (ACS if i in (1, 3) else PANEL, AC)
        o.append(boxt(x, 46, 120, 56, [n], f, st, 14, bold_first=True))
        if notes[i]: o.append(T(x + 60, 124, notes[i], 12, fill=MUT))
        if i < 4:
            o.append(L(x + 122, 64, x + 138, 64, AC, 2, arrow='n'))
            o.append(L(x + 138, 86, x + 122, 86, LV, 2, '5 4', arrow='l'))
    o.append(T(360, 30, 'request →', 13, fill=AC)); o.append(T(360, 152, '← reply (result marshalled by the server stub)', 13, fill=LV))
    fx = lambda v: 200 + v * 24
    o.append(T(20, 196, '10,000 calls', 15, 'start', bold=True))
    o.append(T(190, 230, 'local, 0.1 µs each', 14, 'end'))
    o.append(R(200, 216, 2, 22, ACS, AC, 0, 1.5)); o.append(T(212, 232, '1 ms (too short to see)', 13, 'start', MUT))
    o.append(T(190, 270, 'RPC, 2 ms each', 14, 'end'))
    o.append(seg(200, 256, fx(20) - 200, 22, '20 s', LVS, LV, 14))
    o.append(T(20, 316, 'Slowdown = 20,000 ms ÷ 1 ms = 20,000: a remote call is not a free local call.', 14, 'start', bold=True))
    return 330, ''.join(o)
FIG[3] = (f3, 'An RPC goes client → client stub → network → server stub → server, and the result comes back the same way. Each round trip costs 2 ms, so 10,000 calls take 20 s where local calls take 1 ms: 20,000 times slower.',
          'Five boxes in a row, client, client stub, network, server stub and server, with request arrows to the right and dashed reply arrows to the left; below, a tiny bar for 1 millisecond against a long bar for 20 seconds.')


# ---- 4.4 synchronous bound on a chain ----
def f4():
    fx = lambda t: 90 + t * 5.6
    o = [T(20, 24, 'Synchronous model: work 5 ms each, every message at most 20 ms', 15, 'start', bold=True)]
    ys = [50, 100, 150, 200]
    for i, y in enumerate(ys):
        o.append(T(80, y + 20, f'P{i + 1}', 15, 'end', bold=True))
        s = i * 25
        o.append(seg(fx(s), y, fx(s + 5) - fx(s), 28, '5', ACS, AC))
        if i < 3:
            o.append(seg(fx(s + 5), y, fx(s + 25) - fx(s + 5), 28, '≤ 20 ms', LVS, LV))
            o.append(L(fx(s + 25), y + 30, fx(s + 25), ys[i + 1] - 2, LV, 2, arrow='l'))
    o.append(L(fx(80), 40, fx(80), 240, NX, 2, '6 4')); o.append(T(fx(80), 258, 'done ≤ 80 ms', 13, fill=NX, bold=True))
    o.append(L(fx(100), 40, fx(100), 240, INK, 2)); o.append(T(fx(100), 258, 'timeout 100 ms', 13, bold=True))
    o.append(brace(fx(80), fx(100), 228, NX, up=True))
    o.append(T(fx(90), 220, 'slack 20', 12, fill=NX))
    o.append(xaxis(fx(0), fx(100), 278, [0, 20, 40, 60, 80, 100], fx, 'time (ms)'))
    o.append(T(20, 344, '4 × 5 + 3 × 20 = 80 ms. Asynchronous model: the 20 ms bound is gone, so 100 ms is only a guess.', 14, 'start'))
    return 360, ''.join(o)
FIG[4] = (f4, 'Four processes in a chain: 4 × 5 ms of work and 3 messages of at most 20 ms finish within 80 ms, so a 100 ms timeout is safe with 20 ms to spare. Without a delay bound the same timeout is only a guess.',
          'Gantt chart of P1 to P4: each works 5 milliseconds and sends a message of up to 20 milliseconds to the next, finishing by 80 milliseconds, before a timeout line at 100 milliseconds.')


# ---- 4.5 NTP exchange ----
def f5():
    fx = lambda t: 110 + (t - 1000) * 4.6
    ys, yc = 70, 210
    o = [proc(ys, 'server', 110, 690), proc(yc, 'client', 110, 690)]
    o.append(msg(fx(1000), yc, fx(1100), ys, None, AC, None))
    o.append(msg(fx(1105), ys, fx(1120), yc, None, LV, None, 'l'))
    o.append(ev(fx(1000), yc, 'T1 = 1000', False)); o.append(C(fx(1100), ys, 7, AC) + Tb(fx(1100) - 8, ys - 14, 'T2 = 1100', 13, 'end'))
    o.append(C(fx(1105), ys, 7, LV) + Tb(fx(1105) + 8, ys - 14, 'T3 = 1105', 13, 'start')); o.append(ev(fx(1120), yc, 'T4 = 1120', False, LV))
    o.append(Tb(fx(1046), 140, 'request', 13, fill=AC)); o.append(Tb(612, 150, 'reply', 13, 'end', LV))
    o.append(T(20, 286, 'offset θ = [(T2 − T1) + (T3 − T4)] ÷ 2 = (100 − 15) ÷ 2 = 42.5 ms', 14, 'start', bold=True))
    o.append(T(20, 310, 'delay δ = (T4 − T1) − (T3 − T2) = 120 − 5 = 115 ms, error bound ±δ/2 = ±57.5 ms', 14, 'start'))
    o.append(T(20, 334, 'θ > 0: the server is ahead, so the client clock moves forward 42.5 ms', 14, 'start', NX))
    return 350, ''.join(o)
FIG[5] = (f5, 'The client sends at T1 = 1000 and the server stamps T2 = 1100; the server replies at T3 = 1105 and the client receives at T4 = 1120. That gives offset 42.5 ms, round-trip delay 115 ms and error bound ±57.5 ms.',
          'Two time lines, server above and client below, with a request from T1 to T2 and a reply from T3 to T4, and the offset and delay worked out below.')


# ---- 4.6 Lamport clocks ----
def f6():
    y = {1: 60, 2: 170, 3: 280}
    o = [proc(y[1], 'P1'), proc(y[2], 'P2'), proc(y[3], 'P3')]
    E = {'a': (140, 1, 1), 's1': (240, 1, 2), 'c': (140, 2, 1), 'r1': (330, 2, 3), 's2': (430, 2, 4), 'f': (140, 3, 1), 'g': (260, 3, 2), 'r2': (540, 3, 5)}
    lab = {'a': 'a', 's1': 'send m1', 'c': 'c', 'r1': 'recv m1', 's2': 'send m2', 'f': 'f', 'g': 'g', 'r2': 'recv m2'}
    o.append(msg(E['s1'][0], y[1], E['r1'][0], y[2], 'm1, t = 2', AC, '7 5', lx=34, ly=-4))
    o.append(msg(E['s2'][0], y[2], E['r2'][0], y[3], 'm2, t = 4', AC, '7 5', lx=34, ly=-4))
    for k, (x, p, t) in E.items():
        hot = k in ('r1', 'r2')
        o.append(C(x, y[p], 8, LV if hot else (NX if t == 1 else AC)))
        o.append(Tb(x, y[p] + 28 if hot else y[p] - 16, f'{lab[k]}: {t}', 14, bold=hot))
    o.append(Tb(E['r1'][0], y[2] + 48, 'max(1, 2) + 1 = 3', 13, 'middle', LV))
    o.append(Tb(E['r2'][0], y[3] + 48, 'max(2, 4) + 1 = 5', 13, 'middle', LV))
    o.append(T(20, 364, 'a, c and f all have 1: equal stamps, so they are concurrent. Different stamps prove nothing on their own.', 13, 'start'))
    return 378, ''.join(o)
FIG[6] = (f6, 'Each event adds 1 to its own clock, and a receive jumps past the stamp it carries: P2 goes to max(1, 2) + 1 = 3 and P3 to max(2, 4) + 1 = 5. Events a, c and f all have stamp 1, so none of them can have caused another.',
          'Space-time diagram of three processes with Lamport timestamps on eight events and two dashed messages m1 and m2; the two receives are highlighted with their max-plus-one rule.')


# ---- 4.7 vector clocks ----
def f7():
    y = {1: 60, 2: 170, 3: 280}
    o = [proc(y[1], 'P1'), proc(y[2], 'P2'), proc(y[3], 'P3')]
    E = {'e11': (150, 1, '(1,0,0)'), 'e12': (270, 1, '(2,0,0)'), 'e21': (150, 2, '(0,1,0)'), 'e22': (370, 2, '(2,2,0)'),
         'e23': (480, 2, '(2,3,0)'), 'e31': (180, 3, '(0,0,1)'), 'e32': (330, 3, '(0,0,2)'), 'e33': (600, 3, '(2,3,3)')}
    o.append(msg(270, y[1], 370, y[2], 'm1 (2,0,0)', AC, '7 5', lx=46, ly=-2))
    o.append(msg(480, y[2], 600, y[3], 'm2 (2,3,0)', AC, '7 5', lx=50, ly=-2))
    for k, (x, p, v) in E.items():
        c = NX if k in ('e12', 'e31') else (LV if k in ('e11', 'e33') else AC)
        o.append(C(x, y[p], 8, c))
        o.append(Tb(x, y[p] + 28 if k in ('e22', 'e33') else y[p] - 16, f'{k} {v}', 13, bold=k in ('e12', 'e31', 'e11', 'e33')))
    o.append(T(20, 340, 'e12 (2,0,0) vs e31 (0,0,1): 2 > 0 but 0 < 1, neither ≤ the other → concurrent', 13, 'start', NX))
    o.append(T(20, 362, 'e11 (1,0,0) vs e33 (2,3,3): every entry ≤, one strictly → e11 happened before e33', 13, 'start', LV))
    return 376, ''.join(o)
FIG[7] = (f7, 'Each process counts its own events in its own entry and takes the entry-wise maximum on a receive, so e33 = (2,3,3). Comparing vectors entry by entry shows e12 and e31 are concurrent, while e11 happened before e33.',
          'Space-time diagram of three processes with a vector timestamp on each of eight events and two messages; e12 and e31 are marked concurrent and e11 and e33 causally ordered.')


# ---- 4.8 consistent and inconsistent cuts ----
def f8():
    ya, yb = 80, 220
    o = [proc(ya, 'A'), proc(yb, 'B')]
    xs, xr = 260, 470
    o.append(msg(xs, ya, xr, yb, '₹30 in transit', AC, None, lx=80, ly=36))
    o.append(ev(xs, ya, 'send ₹30', True)); o.append(ev(xr, yb, 'receive ₹30', False))
    o.append(T(150, ya + 28, '₹100', 13, fill=MUT)); o.append(T(380, ya + 28, '₹70', 13, fill=MUT))
    o.append(T(150, yb - 14, '₹100', 13, fill=MUT)); o.append(T(600, yb - 14, '₹130', 13, fill=MUT))
    # S1: after send on A, before receive on B
    o.append(P([(330, 40), (330, 120), (400, 170), (400, 260)], NX, 2.5, '8 5'))
    o.append(Tb(330, 34, 'S1', 14, fill=NX, bold=True))
    # S2: before send on A, after receive on B
    o.append(P([(200, 40), (200, 120), (540, 170), (540, 260)], LV, 2.5, '8 5'))
    o.append(Tb(200, 34, 'S2', 14, fill=LV, bold=True))
    o.append(boxt(20, 284, 330, 60, ['S1: 70 + 100 + ₹30 in the channel = ₹200', 'send inside, receive outside: consistent'], NXS, NX, 13))
    o.append(boxt(370, 284, 330, 60, ['S2: 100 + 130 + 0 = ₹230 (₹30 invented)', 'receive inside, send outside: inconsistent'], LVS, LV, 13))
    return 356, ''.join(o)
FIG[8] = (f8, 'A cut is a line through both timelines. S1 is after A sends ₹30 but before B receives it, so the ₹30 is counted in the channel and the total stays ₹200. S2 contains the receive but not the send, so it counts ₹230 and invents ₹30.',
          'Two process lines A and B with a ₹30 message from A to B. Dashed cut S1 crosses after the send and before the receive; dashed cut S2 crosses before the send and after the receive. Totals are shown below.')


# ---- 4.9 causal delivery with a buffer ----
def f9():
    y = {1: 50, 2: 140, 3: 240}
    o = [proc(y[1], 'P1'), proc(y[2], 'P2'), proc(y[3], 'P3')]
    o.append(msg(140, y[1], 560, y[3], 'm1 (1,0,0), slow', AC, '7 5', lx=40, ly=-14))
    o.append(msg(140, y[1], 250, y[2], None, AC, '7 5'))
    o.append(msg(300, y[2], 380, y[3], 'm2 (1,1,0)', LV, '7 5', 'l', lx=-56, ly=-4))
    o.append(C(140, y[1], 7, AC)); o.append(C(250, y[2], 7, AC)); o.append(C(300, y[2], 7, LV))
    o.append(R(370, y[3] + 12, 120, 30, LVS, LV, 6, dash='5 4')); o.append(T(430, y[3] + 32, 'm2 buffered', 13, fill=LV))
    o.append(C(380, y[3], 7, LV)); o.append(C(560, y[3], 7, AC)); o.append(C(600, y[3], 7, LV))
    o.append(Tb(560, y[3] + 30, 'deliver m1', 13, fill=AC, bold=True)); o.append(Tb(640, y[3] + 30, 'then m2', 13, fill=LV, bold=True))
    o.append(T(20, 316, 'm2 arrives first: it needs P1 entry 1, but Vdel = (0,0,0) → wait.', 13, 'start'))
    o.append(T(20, 338, 'm1 passes, Vdel = (1,0,0); m2 now passes, Vdel = (1,1,0). Sequencer stamps 1, 2 give the same order.', 13, 'start'))
    return 352, ''.join(o)
FIG[9] = (f9, 'P2 sends m2 only after it has m1, but m2 reaches P3 first. Its vector (1,1,0) says one P1 message is missing, so P3 buffers m2, delivers m1 when it arrives, and then m2; Vdel ends at (1,1,0).',
          'Three process lines: m1 from P1 travels slowly to P3, while m2 from P2 arrives at P3 earlier and waits in a buffer until m1 is delivered.')


TEXT = {
    3: [('RPC is used in web services, microservices, distributed databases and file systems. Only a few universities teach this chapter in detail.',
         'RPC is used in web services, microservices, distributed databases and file systems.')],
    5: [('It matters for logs, banking timestamps, distributed databases, and any protocol that compares times across machines. Only a few universities teach this chapter.',
         'It matters for logs, banking timestamps, distributed databases, and any protocol that compares times across machines.')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}


def text_fixes(k):
    return TEXT.get(k, [])


def drop_sources():
    # a university-hosted course page: the books name no universities
    return ['csail.mit.edu']
