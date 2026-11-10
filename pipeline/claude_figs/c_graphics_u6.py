"""Claude's hand-drawn figures for c-graphics-u6 (Computer Graphics and Multimedia, unit 6: multimedia systems,
servers, databases, hypermedia, QoS, streaming, real-time support, applications and watermarking), one per chapter,
from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 6.1 one clip through the architecture ----
def f1():
    o = []
    o.append(boxt(30, 40, 170, 64, ['capture', '640 × 480, 30 frame/s'], PANEL, INK, 13, True))
    o.append(boxt(30, 150, 170, 64, ['microphones', '44.1 kHz, stereo'], PANEL, INK, 13, True))
    o.append(L(203, 72, 247, 72, AC, 2, arrow='n')); o.append(L(203, 182, 247, 182, NX, 2, arrow='x'))
    o.append(boxt(250, 30, 220, 84, ['video codec', '640 × 480 × 24 = 7,372,800 bit', '× 30 = 221.184 Mbit/s'], ACS, AC, 13, True))
    o.append(boxt(250, 140, 220, 84, ['audio codec', '44,100 × 16 × 2', '= 1.4112 Mbit/s'], NXS, NX, 13, True))
    o.append(P([(472, 72), (500, 72), (500, 115)], AC, 2)); o.append(L(500, 115, 516, 115, AC, 2, arrow='n'))
    o.append(P([(472, 182), (500, 182), (500, 139)], NX, 2)); o.append(L(500, 139, 516, 139, NX, 2, arrow='x'))
    o.append(boxt(520, 86, 180, 82, ['buffer and sync', 'one clock', '222.5952 Mbit/s'], LVS, LV, 13, True))
    o.append(L(610, 170, 610, 254, LV, 2, arrow='l'))
    o.append(boxt(430, 258, 270, 84, ['storage, 2 min = 120 s', '222,595,200 × 120 ÷ 8', '= 3,338,928,000 B ≈ 3.34 GB'], PANEL, INK, 13, True))
    o.append(L(426, 300, 296, 300, INK, 2, arrow='m'))
    o.append(boxt(110, 268, 182, 64, ['delivery', 'and playout'], PANEL, INK, 13, True))
    o.append(T(30, 380, 'the two streams stay separate until the buffer and sync stage joins them on one clock', 13, 'start', MUT))
    return 396, ''.join(o)
FIG[1] = (f1, 'The clip flows through the stack: the video codec carries 221.184 Mbit/s and the audio codec 1.4112 Mbit/s, and only the buffer and sync stage joins them on one clock at 222.5952 Mbit/s. Two minutes of that needs 3.34 GB on disk before delivery.',
          'Boxes joined by arrows: camera capture into a video codec at 221.184 Mbit/s and microphones into an audio codec at 1.4112 Mbit/s, both merging into a buffer and sync box at 222.5952 Mbit/s, then storage of 3.34 GB for 2 minutes, then delivery and playout.')


# ---- 6.2 clients on one 100 Mbit/s link ----
def f2():
    o = []
    x0, W = 40, 640
    sc = W / 100
    for k, (rate, ov, n, f, c, y, lab) in enumerate(((2, 0.5, 40, ACS, AC, 70, 'average: 2 Mbit/s × 1.25 = 2.5 Mbit/s per client'),
                                                      (4, 1.0, 20, NXS, NX, 200, 'peak: 4 Mbit/s × 1.25 = 5 Mbit/s per client'))):
        o.append(T(x0, y - 16, lab, 14, 'start', c, True))
        step = rate + ov
        for i in range(n):
            xa = x0 + i * step * sc
            o.append(R(xa, y, rate * sc, 40, f, c, 0, 1))
            o.append(R(xa + rate * sc, y, ov * sc, 40, LVS, 'none', 0, 0))
        o.append(R(x0, y, W, 40, 'none', INK, 0, 1.8))
        o.append(T(x0 + W, y + 62, f'100 ÷ {step:g} = {n} clients', 14, 'end', c, True))
        o.append(brace(x0, x0 + step * sc, y + 48, c))
        o.append(T(x0, y + 66, f'one client: {rate} + {ov:g} overhead', 13, 'start', MUT))
    o.append(xaxis(x0, x0 + W, 300, [0, 20, 40, 60, 80, 100], lambda v: x0 + v * sc, 'link capacity used (Mbit/s)'))
    o.append(R(x0, 360, 16, 14, LVS, 'none', 0, 0)); o.append(T(x0 + 24, 372, '25% protocol overhead in each slot', 13, 'start', LV, True))
    return 386, ''.join(o)
FIG[2] = (f2, 'The 100 Mbit/s link sliced into client slots. Adding the 25% overhead turns each stream into 2.5 Mbit/s at the average rate and 5 Mbit/s at the peak, so the same link carries 40 clients or 20.',
          'Two bars of 100 Mbit/s: the first cut into 40 slots of 2 Mbit/s plus 0.5 overhead, the second into 20 slots of 4 Mbit/s plus 1 overhead, with the divisions 100 ÷ 2.5 = 40 and 100 ÷ 5 = 20.')


# ---- 6.3 histogram distance and precision / recall ----
def f3():
    o = []
    hs = [('query q', [0.40, 0.30, 0.20, 0.10], INK, PANEL), ('image A', [0.50, 0.20, 0.20, 0.10], AC, ACS), ('image B', [0.10, 0.10, 0.30, 0.50], NX, NXS)]
    bw, gap, H = 30, 8, 180
    for k, (lab, h, c, f) in enumerate(hs):
        X0 = 50 + k * 170
        base = 200
        o.append(L(X0 - 6, base, X0 + 4 * (bw + gap), base, L2, 1.6))
        for i, v in enumerate(h):
            x = X0 + i * (bw + gap)
            o.append(R(x, base - v * H * 1.6, bw, v * H * 1.6, f, c, 0, 1.8))
            o.append(T(x + bw / 2, base - v * H * 1.6 - 6, f'{v:.2f}', 13, 'middle', c, True))
            o.append(T(x + bw / 2, base + 18, str(i + 1), 13, 'middle', MUT))
        o.append(T(X0 + 2 * (bw + gap) - 4, 40, lab, 14, 'middle', c, True))
    o.append(T(560, 190, 'bin', 13, 'start', MUT))
    y = 250
    o.append(T(40, y, 'L1(q, A) = 0.10 + 0.10 + 0.00 + 0.00 = 0.20', 14, 'start', AC, True))
    o.append(T(40, y + 24, 'L1(q, B) = 0.30 + 0.20 + 0.10 + 0.40 = 1.00', 14, 'start', NX, True))
    o.append(T(40, y + 48, 'smaller distance ranks first: A, then B', 14, 'start', INK, True))
    # precision / recall
    yp = y + 90
    s = 14
    o.append(T(40, yp - 10, 'returned 20, relevant among them 12, relevant in the database 30', 13, 'start', MUT, True))
    o.append(R(40, yp, 20 * s, 26, PANEL, INK, 0, 1.6)); o.append(R(40, yp, 12 * s, 26, LVS, LV, 0, 1.6))
    o.append(T(40 + 6 * s, yp + 18, '12 relevant', 13, 'middle', LV, True)); o.append(T(40 + 16 * s, yp + 18, '8 not', 13, 'middle', MUT))
    o.append(T(40 + 20 * s + 12, yp + 18, 'precision = 12 / 20 = 0.60', 14, 'start', LV, True))
    o.append(R(40, yp + 40, 30 * s, 26, PANEL, INK, 0, 1.6)); o.append(R(40, yp + 40, 12 * s, 26, LVS, LV, 0, 1.6))
    o.append(T(40 + 6 * s, yp + 58, '12 found', 13, 'middle', LV, True)); o.append(T(40 + 21 * s, yp + 58, '18 missed', 13, 'middle', MUT))
    o.append(T(40 + 30 * s + 12, yp + 58, 'recall = 12 / 30 = 0.40', 14, 'start', LV, True))
    return yp + 80, ''.join(o)
FIG[3] = (f3, 'Bin by bin, image A differs from the query by 0.10, 0.10, 0 and 0, an L1 distance of 0.20, while image B differs by 1.00, so A ranks first. Of the 20 images returned, 12 are relevant (precision 0.60), and they are 12 of the 30 relevant ones (recall 0.40).',
          'Three four-bin histograms side by side, the query, image A and image B, with bar heights labelled; below, the two L1 sums 0.20 and 1.00, then bars showing 12 relevant of 20 returned for precision 0.60 and 12 of 30 relevant for recall 0.40.')


# ---- 6.4 fewest clicks from Home to Notes ----
def f4():
    o = []
    Nd = {'Home': (90, 170, 0), 'Courses': (280, 60, 1), 'Contact': (280, 170, 1), 'FAQ': (280, 280, 1), 'Unit6': (470, 60, 2), 'Notes': (620, 220, 2)}
    best = {('Home', 'FAQ'), ('FAQ', 'Notes')}
    E = [('Home', 'Courses'), ('Courses', 'Unit6'), ('Unit6', 'Notes'), ('Home', 'Contact'), ('Contact', 'FAQ'), ('FAQ', 'Notes'), ('Home', 'FAQ')]
    w, h = 96, 40
    for a, b in E:
        (x1, y1, _), (x2, y2, _) = Nd[a], Nd[b]
        dx, dy = x2 - x1, y2 - y1
        d = math.hypot(dx, dy)
        # clip to box edges
        def cut(x, y, ux, uy):
            t = min((w / 2 + 4) / abs(ux) if ux else 1e9, (h / 2 + 4) / abs(uy) if uy else 1e9)
            return x + ux * t, y + uy * t
        ux, uy = dx / d, dy / d
        sx, sy = cut(x1, y1, ux, uy)
        ex, ey = cut(x2, y2, -ux, -uy)
        hot = (a, b) in best
        o.append(L(sx, sy, ex, ey, NX if hot else L2, 3 if hot else 1.8, arrow='x' if hot else 'm'))
    for k, (x, y, d) in Nd.items():
        hot = k in ('Home', 'FAQ', 'Notes')
        o.append(boxt(x - w / 2, y - h / 2, w, h, [k], NXS if hot else PANEL, NX if hot else INK, 14, True))
        ly = y - h / 2 - 8 if k == 'Contact' else y + h / 2 + 18
        o.append(T(x, ly, f'{d} click' + ('s' if d != 1 else ''), 13, 'middle', NX if hot else MUT, True))
    o.append(T(40, 360, 'Home → FAQ → Notes: 3 nodes but 2 links, so 2 clicks', 14, 'start', NX, True))
    o.append(T(40, 384, 'Home → Courses → Unit6 → Notes and Home → Contact → FAQ → Notes each take 3', 13, 'start', MUT))
    return 400, ''.join(o)
FIG[4] = (f4, 'The number under each node is its fewest clicks from Home, found breadth first. FAQ is one click away and links straight to Notes, so Notes is 2 clicks; the Courses route needs 3 links across 4 nodes.',
          'A directed link graph: Home links to Courses, Contact and FAQ; Courses to Unit6; Unit6 to Notes; Contact to FAQ; FAQ to Notes. The path Home, FAQ, Notes is highlighted, and each node shows its click count: Home 0, Courses, Contact and FAQ 1, Unit6 and Notes 2.')


# ---- 6.5 delay, jitter and the playout buffer ----
def f5():
    o = []
    x0, x1 = 120, 680
    fx = lambda t: x0 + t / 90 * (x1 - x0)
    S = [0, 20, 40, 60, 80]; A = [0, 22, 45, 60, 85]
    rows = [('sent', S, INK, 60), ('arrived', A, AC, 130), ('played, send + 5 ms', [s + 5 for s in S], NX, 200)]
    for lab, ts, c, y in rows:
        o.append(L(x0, y, x1, y, LN, 1))
        o.append(T(x0 - 12, y + 5, lab.split(',')[0], 13, 'end', c, True))
    o.append(T(x0 - 12, 220, 'send + 5 ms', 13, 'end', NX))
    for i in range(5):
        o.append(L(fx(S[i]), 60, fx(A[i]), 130, L2, 1.4, '4 3'))
        o.append(L(fx(A[i]), 130, fx(S[i] + 5), 200, NX, 1.4, '4 3'))
        o.append(C(fx(S[i]), 60, 6, INK)); o.append(C(fx(A[i]), 130, 6, AC)); o.append(C(fx(S[i] + 5), 200, 6, NX))
        o.append(T(fx(S[i]), 46, f'{S[i]}', 13, 'middle', INK, True))
        o.append(Tb(fx(A[i]) + 2, 152, f'd = {A[i] - S[i]}', 13, 'middle', AC, True))
    o.append(xaxis(x0, x1, 240, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90], fx, 'time (ms)'))
    y = 320
    o.append(T(40, y, 'delays 0, 2, 5, 0, 5 ms: mean 12 ÷ 5 = 2.4 ms', 14, 'start', AC, True))
    o.append(T(40, y + 24, 'jitter = mean |d − 2.4| = (2.4 + 0.4 + 2.6 + 2.4 + 2.6) ÷ 5 = 2.08 ms', 14, 'start', INK, True))
    o.append(T(40, y + 48, 'spread 5 − 0 = 5 ms, so a 5 ms buffer: every packet arrives at or before its play time', 14, 'start', NX, True))
    return y + 64, ''.join(o)
FIG[5] = (f5, 'Packets sent every 20 ms arrive 0, 2, 5, 0 and 5 ms later and are played 5 ms after they were sent. Packets 3 and 5 arrive exactly at their play slots, so a 5 ms buffer, the worst delay, plays every packet on time.',
          'Three time rows from 0 to 90 ms: send times 0, 20, 40, 60, 80; arrival times 0, 22, 45, 60, 85 with each delay labelled; play times 5, 25, 45, 65, 85; dashed lines join each packet across the rows.')


# ---- 6.6 segments and the client buffer ----
def f6():
    o = []
    x0, x1 = 40, 680
    fx = lambda t: x0 + t / 120 * (x1 - x0)
    y = 70
    o.append(T(x0, y - 18, '120 s at 3 Mbit/s, cut every 4 s: 120 ÷ 4 = 30 segments', 14, 'start', INK, True))
    for i in range(30):
        o.append(R(fx(i * 4), y, fx(4) - fx(0), 40, ACS if i % 2 == 0 else PANEL, AC, 0, 1.2))
    o.append(xaxis(x0, x1, y + 40, [0, 20, 40, 60, 80, 100, 120], fx, 'video time (s)'))
    yb = y + 120
    o.append(T(x0, yb, 'one segment: 3 Mbit/s × 4 s = 12 Mbit ÷ 8 = 1.5 MB', 14, 'start', AC, True))
    o.append(T(x0, yb + 24, 'whole file: 30 × 1.5 MB = 45 MB  (check: 3 × 120 = 360 Mbit = 45 MB)', 14, 'start', INK, True))
    yc = yb + 64
    o.append(T(x0, yc - 10, 'client buffer: 3 segments held ahead of the playhead', 14, 'start', NX, True))
    bx, bw = 160, 110
    o.append(L(bx, yc, bx, yc + 50, LV, 2.6))
    o.append(T(bx - 10, yc + 30, 'playhead', 13, 'end', LV, True))
    for i in range(3):
        o.append(R(bx + bw * i, yc + 6, bw, 38, NXS, NX, 0, 1.8))
        o.append(T(bx + bw * i + bw / 2, yc + 30, f'segment {10 + i}, 4 s', 13, 'middle', NX, True))
    o.append(brace(bx, bx + 3 * bw, yc + 52, NX))
    o.append(T(bx + 1.5 * bw, yc + 72, '3 × 4 s = 12 s in reserve', 13, 'middle', NX, True))
    o.append(T(bx + 3 * bw + 16, yc + 30, '(drawn larger)', 13, 'start', MUT))
    return yc + 86, ''.join(o)
FIG[6] = (f6, 'The 120 s video cut into 30 segments of 4 s; at 3 Mbit/s each segment is 12 Mbit, or 1.5 MB, and the whole file is 45 MB. The client keeps three segments ahead of the playhead, 12 s of playout in reserve.',
          'A row of 30 alternating segment cells along a 0 to 120 second axis, the size sums below, and a short lane of three buffered segments ahead of a playhead with a brace marked 12 s in reserve.')


# ---- 6.7 CPU utilisation against the two tests ----
def f7():
    o = []
    x0, W = 60, 600
    fx = lambda u: x0 + u * W
    y = 100
    parts = [(0.40, 'audio 4/10 = 0.40', ACS, AC), (0.25, 'video 10/40 = 0.25', NXS, NX), (0.25, 'network 5/20 = 0.25', LVS, LV)]
    u = 0
    for v, lab, f, c in parts:
        o.append(R(fx(u), y, v * W, 50, f, c, 0, 2))
        o.append(T(fx(u + v / 2), y + 30, lab, 13, 'middle', c, True))
        u += v
    o.append(R(fx(0), y, W, 50, 'none', L2, 0, 1.2, '4 4'))
    o.append(xaxis(fx(0), fx(1), y + 50, [0, 0.2, 0.4, 0.6, 0.8, 1.0], fx, 'CPU utilisation U', lambda v: f'{v:g}'))
    o.append(T(fx(0.35), y - 36, 'U = 0.40 + 0.25 + 0.25 = 0.90', 14, 'middle', INK, True))
    for v, lab, c in ((0.7798, 'RM bound 0.7798', AC), (1.0, 'EDF limit 1', NX)):
        o.append(L(fx(v), y - 30, fx(v), y, c, 2.2, '6 4'))
        o.append(T(fx(v), y - 36, lab, 13, 'middle', c, True))
    o.append(L(fx(0.9), y + 54, fx(0.9), y + 66, INK, 2))
    yt = y + 136
    o.append(T(40, yt, 'RM bound for n = 3: 3(2^(1/3) − 1) = 3 × 0.259921 = 0.7798', 14, 'start', AC, True))
    o.append(T(40, yt + 24, '0.90 > 0.7798: the RM test cannot guarantee every deadline', 13, 'start', AC))
    o.append(T(40, yt + 50, '0.90 ≤ 1: EDF guarantees every deadline', 14, 'start', NX, True))
    return yt + 66, ''.join(o)
FIG[7] = (f7, 'The three tasks fill 0.40 + 0.25 + 0.25 = 0.90 of the CPU. That is past the rate-monotonic bound of 0.7798 for three tasks but inside the EDF limit of 1, so only EDF guarantees every deadline.',
          'A bar from 0 to 1 of CPU utilisation filled by audio 0.40, video 0.25 and network 0.25 up to 0.90, with a dashed line at the RM bound 0.7798 inside the filled part and another at the EDF limit 1 beyond it.')


# ---- 6.8 CCTV storage against retention ----
def f8():
    o = []
    x0, x1, y0, y1 = 80, 470, 30, 310
    fx = lambda d: x0 + d / 30 * (x1 - x0)
    fy = lambda v: y1 - v / 90 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 5, 10, 15, 20, 25, 30], [0, 20, 40, 60, 80], fx, fy, 'days kept', 'storage (TB)'))
    o.append(L(fx(0), fy(0), fx(30), fy(82.944), AC, 2.6))
    o.append(L(fx(0), fy(0), fx(30), fy(16.589), NX, 2.6))
    o.append(C(fx(30), fy(82.944), 6, AC)); o.append(C(fx(30), fy(16.589), 6, NX))
    o.append(T(fx(30) - 10, fy(82.944) - 12, '24 h: 82.9 TB', 13, 'end', AC, True))
    o.append(T(fx(30) - 10, fy(16.589) - 12, 'motion only, 20%: 16.6 TB', 13, 'end', NX, True))
    o.append(C(fx(1), fy(2.7648), 4.5, AC))
    o.append(Tb(fx(1) + 10, fy(2.7648) - 30, '1 day: 2.76 TB', 13, 'start', AC, True))
    xr = 500
    lines = [('one camera, one day', INK, True), ('4 × 10⁶ bit/s × 86,400 s', MUT, False), ('= 3.456 × 10¹¹ bit', MUT, False), ('÷ 8 = 43.2 GB', AC, True), ('', 0, 0),
             ('64 cameras: 2,764.8 GB', AC, True), ('≈ 2.76 TB a day', AC, False), ('', 0, 0), ('30 days: 82,944 GB', AC, True), ('≈ 82.9 TB', AC, True), ('', 0, 0),
             ('motion gate, 20%:', NX, True), ('0.2 × 82.9 ≈ 16.6 TB', NX, True)]
    for i, (t, c, b) in enumerate(lines):
        if t: o.append(T(xr, 44 + i * 21, t, 13, 'start', c, b))
    return 360, ''.join(o)
FIG[8] = (f8, 'Storage grows in a straight line with the days kept. Sixty-four cameras at 4 Mbit/s fill 2.76 TB a day, so 30 days of round-the-clock recording needs 82.9 TB; with a motion gate recording 20% of the time it is about 16.6 TB.',
          'A graph of storage in terabytes against days kept from 0 to 30 with two straight lines from the origin, round-the-clock recording reaching 82.9 TB and motion-gated recording reaching 16.6 TB, beside the per-camera and per-day sums.')


# ---- 6.9 hiding three bits in the LSBs ----
def f9():
    o = []
    rows = [(150, 1, 151), (152, 0, 152), (155, 1, 155)]
    cw, X0 = 24, 110
    o.append(T(40, 30, 'pixel', 13, 'start', MUT, True))
    o.append(T(X0 + 4 * cw, 30, 'binary, bit 7 … bit 0', 13, 'middle', MUT, True))
    o.append(T(X0 + 8 * cw + 50, 30, 'bit', 13, 'middle', MUT, True))
    o.append(T(X0 + 8 * cw + 100 + 4 * cw, 30, 'stego pixel', 13, 'middle', MUT, True))
    o.append(T(690, 30, 'error²', 13, 'end', MUT, True))
    for r, (v, bit, nv) in enumerate(rows):
        y = 46 + r * 64
        o.append(T(40, y + 26, str(v), 16, 'start', INK, True))
        for k, b in enumerate(format(v, '08b')):
            last = k == 7
            o.append(R(X0 + k * cw, y, cw, 38, ACS if last else PANEL, AC if last else L2, 0, 1.4 if last else 1))
            o.append(TM(X0 + k * cw + cw / 2, y + 25, b, 15, 'middle', AC if last else INK, last))
        o.append(boxt(X0 + 8 * cw + 34, y + 4, 32, 30, [str(bit)], LVS, LV, 15, True))
        o.append(L(X0 + 8 * cw + 70, y + 19, X0 + 8 * cw + 96, y + 19, LV, 2, arrow='l'))
        x2 = X0 + 8 * cw + 100
        changed = nv != v
        for k, b in enumerate(format(nv, '08b')):
            last = k == 7
            o.append(R(x2 + k * cw, y, cw, 38, (NXS if changed else ACS) if last else PANEL, (NX if changed else AC) if last else L2, 0, 1.4 if last else 1))
            o.append(TM(x2 + k * cw + cw / 2, y + 25, b, 15, 'middle', (NX if changed else AC) if last else INK, last))
        o.append(T(x2 + 8 * cw + 10, y + 26, str(nv), 15, 'start', NX if changed else INK, True))
        o.append(T(690, y + 26, str((nv - v) ** 2), 15, 'end', NX if changed else MUT, True))
    y = 46 + 3 * 64 + 20
    o.append(T(40, y, 'only 150 changes, to 151; 152 already ends in 0 and 155 already ends in 1', 13, 'start', MUT))
    o.append(T(40, y + 28, 'MSE = (1 + 0 + 0) ÷ 3 = 1/3 ≈ 0.333', 14, 'start', INK, True))
    o.append(T(40, y + 54, 'PSNR = 10 log₁₀(255² ÷ 1/3) = 10 log₁₀(195,075) ≈ 52.9 dB', 14, 'start', NX, True))
    return y + 70, ''.join(o)
FIG[9] = (f9, 'Each message bit replaces bit 0 of one pixel. Only 150 has to change, to 151, so the squared errors are 1, 0 and 0, MSE = 1/3 and PSNR = 10 log₁₀(255² ÷ 1/3) ≈ 52.9 dB, far too small a change to see.',
          'Three rows: the pixels 150, 152 and 155 in eight binary cells with bit 0 highlighted, the message bits 1, 0 and 1, and the stego pixels 151, 152 and 155 with squared errors 1, 0 and 0; below, MSE 1/3 and PSNR 52.9 dB.')


spec = make_spec(FIG)
