"""Claude's hand-drawn figures for c-dist-u1 (Parallel and Distributed Computing, unit 1: parallel architectures and
models), one per chapter, from each chapter's worked example, plus text fixes (no university names in the books)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def bar(x, y, w, h, s, fill, st, size=13):
    o = R(x, y, w, h, fill, st, 4)
    if s and tw(s, size) < w - 6: o += T(x + w / 2, y + h / 2 + size * 0.36, s, size)
    return o


def taxis(x0, y, s0, s1, ticks, fx, unit):
    o = [L(fx(s0), y, fx(s1), y, L2, 1.5)]
    for v in ticks:
        o += [L(fx(v), y, fx(v), y + 5, L2, 1.5), T(fx(v), y + 20, str(v), 13, fill=MUT)]
    o.append(T(fx(s1), y + 38, unit, 13, 'end', MUT))
    return ''.join(o)


# ---- 1.1 Amdahl: 20 s serial is the floor ----
def f1():
    fx = lambda t: 150 + t * 5.4
    o = [T(20, 28, 'One program, 100 s on one processor: 20 % serial, 80 % parallel', 15, 'start', bold=True)]
    o.append(T(140, 78, '1 processor', 14, 'end'))
    o.append(bar(fx(0), 58, fx(20) - fx(0), 30, 'serial 20 s', NXS, NX))
    o.append(bar(fx(20), 58, fx(100) - fx(20), 30, 'parallel part 80 s', ACS, AC))
    o.append(T(fx(100), 50, 'T = 100 s', 14, 'end', bold=True))
    o.append(T(140, 128, '16 processors', 14, 'end'))
    o.append(bar(fx(0), 108, fx(20) - fx(0), 30, 'serial 20 s', NXS, NX))
    for i in range(16):
        o.append(R(fx(20), 108 + i * 30 / 16, fx(25) - fx(20), 30 / 16 - 0.4, ACS, AC, 0, 0.8))
    o.append(T(fx(25) + 8, 120, '80 ÷ 16 = 5 s on each of 16 processors', 13, 'start', MUT))
    o.append(T(fx(25) + 8, 138, 'T = 20 + 5 = 25 s', 14, 'start', bold=True))
    o.append(L(fx(20), 156, fx(20), 200, NX, 2, '6 4'))
    o.append(T(fx(20) + 8, 196, 'the serial 20 s never shrinks: T can never drop below 20 s', 14, 'start', NX))
    o.append(taxis(0, 220, 0, 100, [0, 20, 40, 60, 80, 100], fx, 'time (s)'))
    o.append(boxt(40, 284, 300, 66, ['16 processors: S = 100 ÷ 25 = 4', 'E = 4 ÷ 16 = 0.25 (25 %)'], LVS, LV))
    o.append(boxt(380, 284, 300, 66, ['any number of processors:', 'S(max) = 1 ÷ 0.20 = 5'], NXS, NX))
    return 370, ''.join(o)
FIG[1] = (f1, 'The 100 s run is 20 s serial plus 80 s parallel. Sixteen processors cut the parallel part to 5 s, so the run takes 25 s (speedup 4, efficiency 0.25), and the serial 20 s caps the speedup at 5.',
          'Two timelines: one processor runs 20 seconds serial then 80 seconds parallel; sixteen processors run the same 20 seconds serial then 5 seconds parallel, 25 seconds in all.')


# ---- 1.2 Flynn's four classes and dataflow ----
def f2():
    o = [T(250, 26, 'data streams', 14, fill=MUT), T(160, 52, 'one', 14, bold=True), T(360, 52, 'many', 14, bold=True)]
    o.append(f'<text x="14" y="170" font-size="14" text-anchor="middle" style="fill:{MUT}" transform="rotate(-90 14 170)">instruction streams</text>')
    o += [T(62, 122, 'one', 14, 'end', bold=True), T(62, 242, 'many', 14, 'end', bold=True)]
    cells = [(70, 64, 'SISD', ['(c) scalar CPU', 'adds two registers'], PANEL, AC),
             (270, 64, 'SIMD', ['(a) GPU: one add', 'on many lanes'], ACS, AC),
             (70, 184, 'MISD', ['rare, mostly', 'theoretical'], PANEL, L2),
             (270, 184, 'MIMD', ['(b) 8 cores, a different', 'program on each'], LVS, LV)]
    for x, y, n, ls, f, s in cells:
        o.append(R(x, y, 180, 108, f, s, 8))
        o.append(T(x + 90, y + 34, n, 18, bold=True))
        o.append(T(x + 90, y + 62, ls[0], 13)); o.append(T(x + 90, y + 80, ls[1], 13))
    o.append(T(270, 316, 'Flynn: count the streams', 14, fill=MUT))
    # dataflow, outside the grid
    o.append(R(492, 64, 210, 228, NXS, NX, 8, dash='6 4'))
    o.append(T(597, 90, '(d) Dataflow', 16, bold=True))
    o.append(T(597, 110, 'not a Flynn class', 13, fill=NX))
    o.append(C(552, 150, 9, AC)); o.append(T(552, 135, 'a', 13, fill=MUT))
    o.append(C(642, 150, 9, AC)); o.append(T(642, 135, 'b', 13, fill=MUT))
    o.append(L(556, 158, 588, 198, L2, 2, arrow='m')); o.append(L(638, 158, 606, 198, L2, 2, arrow='m'))
    o.append(f'<circle cx="597" cy="216" r="20" style="fill:var(--panel);stroke:{NX};stroke-width:2"/>')
    o.append(T(597, 222, '+', 18, bold=True))
    o.append(T(597, 262, 'fires when both', 13)); o.append(T(597, 279, 'operands arrive', 13))
    return 330, ''.join(o)
FIG[2] = (f2, 'Flynn\'s classes come from counting instruction streams and data streams: the scalar CPU is SISD, the GPU add is SIMD and the 8-core CPU is MIMD. A dataflow adder fires when its operands arrive, so it sits outside the four classes.',
          'A two by two grid of SISD, SIMD, MISD and MIMD by number of instruction and data streams, with a separate dashed box for a dataflow adder that fires when both inputs arrive.')


# ---- 1.3 shared memory vs cluster ----
def f3():
    fx = lambda t: 130 + t * 6.0
    o = [T(20, 26, '4-core shared-memory machine (no message cost)', 15, 'start', bold=True)]
    y = 40
    for i in range(4):
        yy = y + i * 24
        o.append(T(120, yy + 16, f'core {i + 1}', 13, 'end', MUT))
        if i == 0: o.append(bar(fx(0), yy, fx(20) - fx(0), 20, 'serial 20 s', NXS, NX))
        o.append(bar(fx(20), yy, fx(40) - fx(20), 20, '80 ÷ 4 = 20 s', ACS, AC))
    o.append(T(fx(40) + 10, 92, 'T = 40 s, S = 100 ÷ 40 = 2.5', 14, 'start', bold=True))
    o.append(T(20, 172, '2-node cluster (private memory, messages)', 15, 'start', bold=True))
    y = 186
    for i in range(2):
        yy = y + i * 28
        o.append(T(120, yy + 17, f'node {i + 1}', 13, 'end', MUT))
        if i == 0: o.append(bar(fx(0), yy, fx(20) - fx(0), 22, 'serial 20 s', NXS, NX))
        o.append(bar(fx(20), yy, fx(60) - fx(20), 22, '80 ÷ 2 = 40 s', ACS, AC))
        o.append(bar(fx(60), yy, fx(70) - fx(60), 22, '', LVS, LV))
    o.append(T((fx(60) + fx(70)) / 2, 260, 'messages 10 s', 13, fill=LV))
    o.append(T(fx(70) + 10, 214, 'T = 70 s', 14, 'start', bold=True))
    o.append(T(fx(70) + 10, 232, 'S = 100 ÷ 70 ≈ 1.43', 14, 'start', bold=True))
    o.append(taxis(0, 280, 0, 70, [0, 10, 20, 30, 40, 50, 60, 70], fx, 'time (s)'))
    return 330, ''.join(o)
FIG[3] = (f3, 'The same 100 s job: four cores with one memory finish in 20 + 20 = 40 s, while two cluster nodes need 20 + 40 s plus 10 s of messages, 70 s. Here the shared-memory machine wins, 2.5 against 1.43.',
          'Two timelines. Four cores run a 20 second serial part then 20 seconds each, ending at 40 seconds. Two nodes run the serial part, 40 seconds each, then 10 seconds of messages, ending at 70 seconds.')


# ---- 1.4 EREW tree combine vs priority CRCW ----
def f4():
    o = [T(190, 24, 'EREW: one writer per cell per step', 15, bold=True), T(570, 24, 'Priority CRCW', 15, bold=True)]
    xs = [30 + i * 46 for i in range(8)]
    ys = [310, 230, 150, 70]
    lv = [list(range(8))]
    pos = [[x for x in xs]]
    for r in range(3):
        p = pos[-1]; pos.append([(p[2 * i] + p[2 * i + 1]) / 2 for i in range(len(p) // 2)])
    for r in range(3):
        for i, x in enumerate(pos[r + 1]):
            o.append(L(pos[r][2 * i], ys[r] - 14, x - 3, ys[r + 1] + 16, AC, 2, arrow='n'))
            o.append(L(pos[r][2 * i + 1], ys[r] - 14, x + 3, ys[r + 1] + 16, AC, 2, arrow='n'))
        o.append(T(410, (ys[r] + ys[r + 1]) / 2 + 5, f'round {r + 1}', 13, 'end', MUT))
    for i, x in enumerate(xs):
        o.append(R(x - 18, ys[0] - 14, 36, 28, PANEL, AC, 6)); o.append(T(x, ys[0] + 5, f'P{i}', 13, bold=True))
    for r in (1, 2):
        for x in pos[r]: o.append(C(x, ys[r], 9, AC))
    o.append(R(pos[3][0] - 22, ys[3] - 16, 44, 32, LVS, LV, 6)); o.append(T(pos[3][0], ys[3] + 5, 'A', 15, bold=True))
    o.append(T(30 - 18, 356, '8 → 4 → 2 → 1: log₂ 8 = 3 rounds, cost 3 × 8 = 24', 14, 'start', bold=True))
    # CRCW
    cx, cy = 570, 150
    o.append(T(cx, 72, 'all 8 write at once;', 13, fill=MUT)); o.append(T(cx, 90, 'highest index P7 wins', 13, fill=MUT))
    o.append(R(cx - 50, cy - 16, 100, 32, LVS, LV, 6)); o.append(T(cx, cy + 5, 'A', 15, bold=True))
    for i in range(8):
        x = 455 + i * 33
        o.append(R(x - 15, 296, 30, 28, PANEL, AC, 6)); o.append(T(x, 315, f'P{i}', 13, bold=True))
        o.append(L(x, 294, cx + (x - cx) * 0.36, cy + 20, NX if i < 7 else LV, 1.8 if i < 7 else 2.5, arrow='x' if i < 7 else 'l'))
    o.append(T(cx, 356, '1 round, cost 1 × 8 = 8', 14, bold=True))
    return 376, ''.join(o)
FIG[4] = (f4, 'Eight processors want to write cell A. Under EREW a tree combine halves the writers each round, 8 → 4 → 2 → 1, so 3 rounds and cost 24 processor-time units; priority CRCW lets all 8 write in 1 round, cost 8.',
          'Left: eight processors merge pairwise in three rounds into cell A. Right: eight processors all send arrows to cell A in one round, with P7, the highest index, winning.')


# ---- 1.5 three networks on N = 8 ----
def f5():
    o = []
    # mesh 2x4
    pts = {(r, c): (60 + c * 52, 110 + r * 64) for r in range(2) for c in range(4)}
    for (r, c), (x, y) in pts.items():
        if c < 3: o.append(L(x, y, x + 52, y, AC, 2))
        if r < 1: o.append(L(x, y, x, y + 64, AC, 2))
    o.append(L(138, 86, 138, 198, NX, 2.5, '6 4'))
    for (r, c), (x, y) in pts.items(): o.append(C(x, y, 8, AC))
    o.append(T(138, 40, '2 × 4 mesh', 15, bold=True))
    # tree
    tp = {0: (355, 70), 1: (300, 120), 2: (410, 120), 3: (272, 170), 4: (328, 170), 5: (382, 170), 6: (438, 170), 7: (272, 218)}
    for i in range(1, 8):
        a, b = tp[i], tp[(i - 1) // 2]; o.append(L(a[0], a[1], b[0], b[1], AC, 2))
    m = ((tp[0][0] + tp[1][0]) / 2, (tp[0][1] + tp[1][1]) / 2)
    o.append(L(m[0] - 16, m[1] - 14, m[0] + 14, m[1] + 16, NX, 2.5, '6 4'))
    for i, (x, y) in tp.items(): o.append(C(x, y, 8, AC))
    o.append(T(355, 40, 'binary tree, 8 nodes', 15, bold=True))
    # cube
    sq = [(0, 0), (1, 0), (1, 1), (0, 1)]
    fr = [(560 + a * 70, 120 + b * 70) for a, b in sq]
    bk = [(x + 40, y - 40) for x, y in fr]
    for i in range(4):
        o.append(L(*fr[i], *fr[(i + 1) % 4], AC, 2)); o.append(L(*bk[i], *bk[(i + 1) % 4], AC, 2)); o.append(L(*fr[i], *bk[i], AC, 2))
    o.append(L(615, 66, 615, 206, NX, 2.5, '6 4'))
    for p in fr + bk: o.append(C(*p, 8, AC))
    o.append(T(615, 40, '3-cube', 15, bold=True))
    o.append(T(360, 248, 'dashed line: the fewest links cut to split the 8 nodes 4 | 4', 13, fill=NX))
    rows = [('degree d', '3', '3', '3'), ('diameter D', '4 hops', '5 hops', '3 hops (best)'), ('bisection B', '2 links', '1 link (worst)', '4 links')]
    for j, (n, a, b, c) in enumerate(rows):
        y = 284 + j * 26
        o.append(T(20, y, n, 14, 'start', MUT))
        o.append(T(138, y, a, 14)); o.append(T(355, y, b, 14, fill=NX if j == 2 else INK, bold=j == 2))
        o.append(T(615, y, c, 14, fill=LV if j == 1 else INK, bold=j == 1))
    return 360, ''.join(o)
FIG[5] = (f5, 'Three ways to wire 8 nodes. The 3-cube has the shortest worst-case path, 3 hops; the binary tree is split by cutting one link, so every left-to-right message shares it.',
          'A 2 by 4 mesh, an 8-node binary tree and a 3-cube, each with a dashed line showing the fewest links cut to halve the network, above a table of degree, diameter and bisection width.')


# ---- 1.6 Amdahl speedup curve, f = 0.1 ----
def f6():
    x0, x1, y0, y1 = 70, 600, 50, 330
    fx = lambda p: x0 + (p - 1) / 63 * (x1 - x0)
    fy = lambda s: y1 - s / 16 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [1, 8, 16, 24, 32, 40, 48, 56, 64], [0, 4, 8, 12, 16], fx, fy, 'processors p', 'speedup S')]
    o.append(L(fx(1), fy(1), fx(16), fy(16), L2, 2, '6 4'))
    o.append(Tb(fx(13), fy(15), 'ideal S = p', 13, 'end', MUT))
    o.append(L(x0, fy(10), x1, fy(10), NX, 2, '8 5'))
    o.append(Tb(x1, fy(10) - 10, 'ceiling 1 ÷ f = 10', 14, 'end', NX))
    S = lambda p: 1 / (0.1 + 0.9 / p)
    o.append(P([(fx(p / 4), fy(S(p / 4))) for p in range(4, 257)], AC, 3))
    o.append(L(fx(8), fy(4.706), fx(8), y1, AC, 1.5, '4 4'))
    o.append(C(fx(8), fy(4.706), 7, AC))
    o.append(Tb(fx(8) + 14, fy(4.706) + 18, 'p = 8: S = 200 ÷ 42.5 ≈ 4.71, not 8', 14, 'start'))
    o.append(Tb(fx(40), fy(S(40)) + 22, 'S = 1 ÷ (0.1 + 0.9 ÷ p)', 14, 'start', AC))
    return 390, ''.join(o)
FIG[6] = (f6, 'With 20 s serial out of 200 s, f = 0.1. At 8 processors the speedup is 4.71 instead of the ideal 8, and however many processors are added it never passes 10.',
          'Speedup against processors: a dashed ideal line, a curve that bends over and flattens under a dashed ceiling at 10, and a marked point at 8 processors with speedup 4.71.')


# ---- 1.7 block distribution, 8 tasks on 3 processors ----
def f7():
    fx = lambda t: 110 + t * 32
    o = [T(20, 26, 'Static block distribution: 8 tasks of 5 ms each, in task order', 15, 'start', bold=True)]
    loads = [[1, 2, 3], [4, 5, 6], [7, 8]]
    for i, ts in enumerate(loads):
        y = 50 + i * 50
        o.append(T(108, y + 24, f'Proc {i + 1}', 14, 'end'))
        for j, t in enumerate(ts):
            o.append(bar(fx(j * 5), y, fx(5) - fx(0) - 2, 36, f'T{t}', ACS, AC, 14))
        if len(ts) == 2:
            o.append(R(fx(10), y, fx(15) - fx(10) - 2, 36, FIGBG, NX, 4, 1.8, '5 4'))
            o.append(T((fx(10) + fx(15)) / 2, y + 23, 'idle', 14, fill=NX))
        o.append(T(fx(15) + 12, y + 24, f'load {len(ts) * 5} ms', 14, 'start', MUT))
    o.append(L(fx(15) - 1, 40, fx(15) - 1, 206, LV, 2, '6 4'))
    o.append(T(fx(15) - 1, 222, 'makespan 15 ms', 13, fill=LV))
    o.append(taxis(0, 236, 0, 15, [0, 5, 10, 15], fx, 'time (ms)'))
    o.append(T(20, 300, 'work W = 8 × 5 = 40 ms · capacity = 3 × 15 = 45 ms · idle = 45 − 40 = 5 ms', 14, 'start'))
    o.append(T(20, 324, 'efficiency = 40 ÷ 45 ≈ 0.889 · imbalance = (15 − 13.33) ÷ 13.33 = 12.5 %', 14, 'start'))
    return 340, ''.join(o)
FIG[7] = (f7, 'Block distribution gives Proc 1 and Proc 2 three tasks each and Proc 3 only two, so Proc 3 waits from 10 to 15 ms. The run takes 15 ms for 40 ms of work: efficiency about 0.889 and load imbalance 12.5 %.',
          'Gantt chart of three processors: two run three 5 millisecond tasks each to 15 milliseconds, the third runs two tasks then sits idle from 10 to 15 milliseconds.')


# ---- 1.8 data vs model parallelism on 2 GPUs ----
def f8():
    fx = lambda t: 110 + t * 2.6
    o = [T(20, 26, 'Data parallel: each GPU holds the whole 12-layer model', 15, 'start', bold=True)]
    for i in range(2):
        y = 42 + i * 34
        o.append(T(100, y + 19, f'GPU {i}', 14, 'end'))
        o.append(bar(fx(0), y, fx(80) - fx(0), 26, '32 images, 80 ms', ACS, AC))
        o.append(bar(fx(80), y, fx(90) - fx(80), 26, '', LVS, LV))
    o.append(T(fx(90) + 8, 64, 'all-reduce 10 ms', 13, 'start', LV))
    o.append(T(fx(90) + 8, 84, 'step 90 ms: 64 ÷ 90 ≈ 0.711 images/ms', 14, 'start', bold=True))
    o.append(T(20, 150, 'Model parallel: layers 1–6 on GPU 0, layers 7–12 on GPU 1', 15, 'start', bold=True))
    rows = [('GPU 0', 166), ('link', 200), ('GPU 1', 234)]
    for n, y in rows: o.append(T(100, y + 19, n, 14, 'end'))
    for m in range(4):
        s = m * 40
        o.append(bar(fx(s), 166, fx(40) - fx(0) - 2, 26, f'mb {m + 1}', ACS if m == 0 else PANEL, AC))
        if s + 70 <= 250: o.append(bar(fx(s + 40), 200, fx(30) - fx(0) - 2, 26, '30', LVS, LV))
        if s + 110 <= 250: o.append(bar(fx(s + 70), 234, fx(40) - fx(0) - 2, 26, f'mb {m + 1}', ACS if m == 0 else PANEL, AC))
    o.append(L(fx(110), 158, fx(110), 272, NX, 2, '6 4'))
    o.append(T(fx(110) + 6, 286, 'first output at 40 + 30 + 40 = 110 ms', 13, 'start', NX))
    o.append(T(fx(110) + 6, 304, 'then one more every max(40, 30) = 40 ms', 13, 'start', NX))
    o.append(taxis(0, 318, 0, 230, [0, 40, 80, 110, 150, 190, 230], fx, 'time (ms)'))
    return 370, ''.join(o)
FIG[8] = (f8, 'Data parallel: both GPUs train 32 images on the full model for 80 ms, then swap gradients for 10 ms, a 90 ms step. Model parallel: the first micro-batch needs 40 + 30 + 40 = 110 ms, and after that one leaves every 40 ms as the stages overlap.',
          'Two Gantt charts. Top: two GPUs each compute 80 milliseconds then all-reduce 10 milliseconds. Bottom: micro-batches flow from GPU 0 across the link to GPU 1, the first finishing at 110 milliseconds and then one every 40 milliseconds.')


TEXT = {
    2: [('SIMD is a SIMD computer: one control unit', 'A SIMD computer has one control unit:'),
        ('MIMD is a MIMD multiprocessor: each processor', 'In a MIMD multiprocessor, each processor')],
    4: [('Only a few universities teach it in detail; it remains the standard analysis model for shared-memory algorithms.',
         'It remains the standard analysis model for shared-memory algorithms.')],
    5: [('In stage i, node x links to the node differing in bit i in stage i + 1, and to matching nodes in stage i − 1.',
         'In stage i, node x links to two nodes in stage i + 1: node x itself (the straight link) and the node whose address differs from x in bit i (the cross link).')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}


def text_fixes(k):
    return TEXT.get(k, [])


def drop_sources():
    return []
