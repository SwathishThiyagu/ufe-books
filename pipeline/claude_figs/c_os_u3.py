"""Claude's hand-drawn figures for c-os-u3 (Operating Systems, unit 3: synchronization and deadlocks), one per chapter,
from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def num(x, y, n, c=AC):
    return f'<circle cx="{x}" cy="{y}" r="12" style="fill:var(--panel);stroke:{c};stroke-width:2"/>' + T(x, y + 5, str(n), 13, fill=c, bold=True)


# ---- 3.1 lost update ----
def f1():
    xr1, xm, xr2 = 210, 410, 610
    o = [T(xr1, 34, 'P1 register R1', 14, bold=True), T(xm, 34, 'shared x in memory', 14, bold=True), T(xr2, 34, 'P2 register R2', 14, bold=True)]
    rows = [('start', None, 5, None, None), ('P1 loads', 5, 5, None, ('m', 1)), ('P2 loads', 5, 5, 5, ('m', 2)),
            ('P1 stores 6', 6, 6, 5, ('s', 1)), ('P2 stores 6', 6, 6, 6, ('s', 2))]
    for i, (lab, r1, x, r2, act) in enumerate(rows):
        y = 58 + i * 56
        o.append(num(24, y + 20, i))
        o.append(T(42, y + 25, lab, 13, 'start', MUT))
        last = i == 4
        o.append(boxt(xm - 45, y, 90, 40, [f'x = {x}'], LVS if last else PANEL, LV if last else INK, 15, bold_first=True))
        for xx, v, k in ((xr1, r1, 1), (xr2, r2, 2)):
            if v is not None:
                stale = (k == 2 and i >= 2)
                o.append(boxt(xx - 40, y, 80, 40, [str(v)], ACS if k == 1 else NXS, AC if k == 1 else NX, 15, bold_first=True))
        if act:
            kind, who = act
            xx = xr1 if who == 1 else xr2
            side = 1 if who == 1 else -1
            a, b = (xm - 45 * side, xx + 40 * side) if kind == 'm' else (xx + 40 * side, xm - 45 * side)
            o.append(L(a - 4 * side if kind == 'm' else a, y + 20, b + (4 * side if kind == 'm' else -4 * side), y + 20, LV if (i == 4) else AC, 2.5, arrow='l' if i == 4 else 'n'))
            o.append(Tb((a + b) / 2, y + 14, 'load' if kind == 'm' else 'store', 13, fill=MUT))
    o.append(T(xr2 + 50, 58 + 2 * 56 + 25, 'old 5', 13, 'start', LV, True))
    o.append(T(xm, 58 + 4 * 56 + 58, "overwrites P1's 6", 13, fill=LV, bold=True))
    o.append(T(360, 372, 'Should be 5 + 1 + 1 = 7, but x ends at 6: 7 − 6 = 1 update lost.', 15, bold=True, fill=LV))
    return 390, ''.join(o)
FIG[1] = (f1, 'Both processes load x while it is still 5, so each computes 6 and the second store overwrites the first. x ends at 6 instead of 7: one update is lost.',
          'Five rows showing P1 and P2 each loading 5 from shared x into their registers, adding 1 and storing 6, so x ends at 6.')


# ---- 3.2 Peterson trace ----
def f2():
    cols = [(20, 36, '#'), (56, 286, 'step'), (342, 66, 'flag[0]'), (408, 66, 'flag[1]'), (474, 56, 'turn'), (530, 170, 'result')]
    rows = [('start', '0', '0', '0', '', None),
            ('P0: flag[0] = 1, turn = 1', '1', '0', '1', '', None),
            ('P1: flag[1] = 1, turn = 0', '1', '1', '0', '', None),
            ('P0 tests: turn == 1 is false', '1', '1', '0', 'P0 enters', AC),
            ('P1 tests: flag[0] and turn == 0', '1', '1', '0', 'P1 spins', LV),
            ('P0 exits: flag[0] = 0', '0', '1', '0', '', None),
            ('P1 tests: flag[0] is 0', '0', '1', '0', 'P1 enters', NX)]
    o = []
    y0, rh = 20, 40
    for x, w, h in cols:
        o.append(T(x + w / 2 if h != 'step' else x + 10, y0 + 22, h, 14, 'middle' if h != 'step' else 'start', MUT, True))
    o.append(L(20, y0 + 34, 700, y0 + 34, L2, 1.5))
    prev = None
    for i, (st, a, b, t, res, c) in enumerate(rows):
        y = y0 + 38 + i * rh
        if c: o.append(R(20, y, 680, rh - 4, ACS if c == AC else (LVS if c == LV else NXS), 'none', 6, 0))
        o.append(T(38, y + 24, str(i + 1), 13, fill=MUT))
        o.append(T(66, y + 24, st, 14, 'start'))
        for (x, w, _), v, j in zip(cols[2:5], (a, b, t), range(3)):
            ch = prev is not None and prev[j] != v
            o.append(T(x + w / 2, y + 24, v, 15, fill=AC if ch else INK, bold=ch))
        if res: o.append(T(615, y + 24, res, 14, bold=True, fill=c))
        prev = (a, b, t)
    o.append(T(360, y0 + 38 + 7 * rh + 26, 'At the moment P1 enters: flag[0] = 0, flag[1] = 1, turn = 0', 15, bold=True))
    return y0 + 38 + 7 * rh + 44, ''.join(o)
FIG[2] = (f2, 'The worked trace of Peterson\'s algorithm, one row per step; changed values are bold. turn = 0 lets P0 in while P1 spins, and P1 enters once P0 clears flag[0].',
          'A seven-row table tracing flag[0], flag[1] and turn: P0 enters at step 4, P1 spins at step 5 and enters at step 7.')


# ---- 3.3 counting semaphore ----
def f3():
    ev = [('start', 1, [], '—'), ('P1: wait', 0, [], 'P1'), ('P2: wait', -1, ['P2'], 'P1'), ('P3: wait', -2, ['P2', 'P3'], 'P1'), ('P1: signal', -1, ['P3'], 'P2')]
    o = [T(14, 104, 'S', 15, 'start', bold=True), T(14, 170, 'blocked', 13, 'start', MUT), T(14, 252, 'in critical', 13, 'start', MUT), T(14, 268, 'section', 13, 'start', MUT)]
    for i, (lab, s, blk, cs) in enumerate(ev):
        cx = 140 + i * 132
        o.append(T(cx, 40, lab, 14, bold=True))
        neg_ = s < 0
        o.append(f'<circle cx="{cx}" cy="{98}" r="30" style="fill:{LVS if neg_ else ACS};stroke:{LV if neg_ else AC};stroke-width:2.5"/>')
        o.append(T(cx, 106, neg(s), 22, bold=True, fill=LV if neg_ else AC))
        o.append(R(cx - 56, 146, 112, 64, PANEL, L2, 8, 1.5))
        if blk:
            for j, p in enumerate(blk):
                o.append(boxt(cx - 50 + j * 52, 158, 48, 40, [p], LVS, LV, 13, rx=6))
        else:
            o.append(T(cx, 184, 'none', 13, fill=MUT))
        o.append(boxt(cx - 40, 236, 80, 36, [cs], NXS if cs != '—' else PANEL, NX if cs != '—' else L2, 14, bold_first=True))
    o.append(T(360, 310, 'A negative S counts the waiters: −2 means 2 blocked. signal raises S to −1', 14))
    o.append(T(360, 332, 'and wakes the first waiter, P2; P3 stays blocked.', 14))
    return 348, ''.join(o)
FIG[3] = (f3, 'S starts at 1 and each wait subtracts 1: P1 gets in, then P2 and P3 block as S falls to −1 and −2. P1\'s signal raises S to −1 and wakes P2.',
          'Five columns, one per event, each showing the value of S, the blocked queue and who is in the critical section.')


# ---- 3.4 bounded buffer in a monitor ----
def f4():
    ev = [('P inserts A', ['A', ''], 1, [], ''), ('P inserts B', ['A', 'B'], 2, [], ''), ('P tries C', ['A', 'B'], 2, ['P'], 'full: P waits'),
          ('K removes A', ['', 'B'], 1, [], 'signal: P ready'), ('P inserts C', ['C', 'B'], 2, [], '')]
    o = [T(14, 104, 'buffer', 13, 'start', MUT), T(14, 160, 'count', 13, 'start', MUT), T(14, 214, 'waiting on', 13, 'start', MUT), T(14, 230, 'notFull', 13, 'start', MUT)]
    for i, (lab, buf, cnt, nf, note) in enumerate(ev):
        cx = 150 + i * 130
        o.append(num(cx - 50, 38, i + 1))
        o.append(T(cx + 8, 43, lab, 13, bold=True))
        for j, v in enumerate(buf):
            o.append(boxt(cx - 48 + j * 50, 80, 46, 44, [v], ACS if v else PANEL, AC if v else L2, 15, bold_first=True, rx=4, dash=None if v else '4 4'))
        o.append(T(cx, 164, str(cnt), 18, bold=True, fill=LV if cnt == 2 else INK))
        if nf: o.append(boxt(cx - 24, 200, 48, 36, nf, LVS, LV, 14, bold_first=True))
        else: o.append(T(cx, 222, 'none', 13, fill=MUT))
        if note: o.append(T(cx, 266, note, 13, fill=LV if i == 2 else NX, bold=True))
    o.append(T(360, 310, 'count after each event: 1, 2, 2, 1, 2 (capacity 2). Under Mesa rules K keeps', 14))
    o.append(T(360, 332, 'running after its signal; P runs later and inserts C.', 14))
    return 348, ''.join(o)
FIG[4] = (f4, 'The two-slot buffer after each of the five events. When it is full P waits on notFull; K\'s removal and signal make P ready, and P later inserts C. The count goes 1, 2, 2, 1, 2.',
          'Five columns showing a two-slot buffer, the count and who waits on notFull, as P inserts A and B, waits, K removes A and P inserts C.')


# ---- 3.5 resource-allocation graph with a cycle ----
def f5():
    P = {'P1': (190, 80), 'P2': (450, 260)}
    Rr = {'R2': (450, 80), 'R1': (190, 260)}
    o = []
    def pc(n):
        x, y = P[n]; return f'<circle cx="{x}" cy="{y}" r="32" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2.5"/>' + T(x, y + 6, n, 16, bold=True)
    def rb(n):
        x, y = Rr[n]
        return R(x - 40, y - 30, 80, 60, PANEL, INK, 6, 2.5) + T(x, y - 8, n, 15, bold=True) + f'<circle cx="{x}" cy="{y + 12}" r="6" style="fill:var(--ink)"/>'
    # request edges (dashed): P1 -> R2, P2 -> R1 ; assignment edges (solid): R2 -> P2, R1 -> P1
    o.append(L(224, 80, 406, 80, LV, 2.5, '7 5', 'l')); o.append(Tb(320, 70, 'P1 wants R2', 13, fill=LV, bold=True))
    o.append(L(450, 112, 450, 224, AC, 2.5, arrow='n')); o.append(Tb(456, 172, 'R2 held by P2', 13, 'start', AC, True))
    o.append(L(416, 260, 234, 260, LV, 2.5, '7 5', 'l')); o.append(Tb(320, 250, 'P2 wants R1', 13, fill=LV, bold=True))
    o.append(L(190, 228, 190, 116, AC, 2.5, arrow='n')); o.append(Tb(184, 172, 'R1 held by P1', 13, 'end', AC, True))
    o.append(f'<path d="M290,140 A40,40 0 1,1 350,140" style="fill:none;stroke:var(--ink);stroke-width:1.5" marker-end="url(#ar-UID-m)"/>')
    o.append(T(320, 182, 'cycle', 13, fill=MUT))
    for n in P: o.append(pc(n))
    for n in Rr: o.append(rb(n))
    # legend and counts
    o.append(L(540, 70, 580, 70, AC, 2.5, arrow='n')); o.append(T(590, 75, 'holds', 13, 'start'))
    o.append(L(540, 96, 580, 96, LV, 2.5, '7 5', 'l')); o.append(T(590, 101, 'wants', 13, 'start'))
    o.append(f'<circle cx="560" cy="124" r="5" style="fill:var(--ink)"/>'); o.append(T(590, 129, '1 instance', 13, 'start'))
    o.append(T(30, 334, 'Edges: 2 request + 2 assignment = 4, forming P1 → R2 → P2 → R1 → P1. Each resource', 14, 'start'))
    o.append(T(30, 356, 'has 1 instance and it is taken, so no request can be granted: 0 processes can finish.', 14, 'start', bold=True))
    return 372, ''.join(o)
FIG[5] = (f5, 'Each resource has one instance and both are held, so each process waits for the one the other holds. The four edges close one cycle and 0 processes can finish: deadlock.',
          'A square resource-allocation graph: P1 holds R1 and wants R2, P2 holds R2 and wants R1, with the four edges forming a cycle.')


# ---- 3.6 resource ordering ----
def f6():
    o = [T(360, 30, 'Rule: ask for resources only in increasing number', 15, bold=True)]
    xs = {1: 150, 2: 360, 3: 570}
    for n, x in xs.items():
        o.append(boxt(x - 50, 140, 100, 52, [f'R{n}', f'number {n}'], PANEL if n == 3 else ACS, L2 if n == 3 else AC, 14, bold_first=True))
    o.append(T(570, 214, 'not used here', 13, fill=MUT))
    # P1 above R1
    o.append(f'<circle cx="150" cy="76" r="26" style="fill:var(--next-soft);stroke:var(--next);stroke-width:2.5"/>' + T(150, 82, 'P1', 15, bold=True))
    o.append(L(150, 102, 150, 136, NX, 2.5)); o.append(T(142, 124, 'holds', 13, 'end', NX))
    o.append(L(176, 82, 316, 136, NX, 2.5, '7 5', 'x')); o.append(Tb(268, 92, 'asks R2: 2 > 1, allowed', 13, 'start', NX, True))
    # P2 below R2
    o.append(f'<circle cx="360" cy="270" r="26" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2.5"/>' + T(360, 276, 'P2', 15, bold=True))
    o.append(L(360, 244, 360, 196, AC, 2.5)); o.append(T(368, 228, 'holds', 13, 'start', AC))
    o.append(L(334, 264, 196, 196, LV, 2.5, '7 5', 'l'))
    o.append(T(242, 236, '✗', 22, bold=True, fill=LV))
    o.append(Tb(200, 282, 'asks R1: 1 is not > 2, refused', 13, 'middle', LV, True))
    o.append(T(360, 334, 'P2 must first release R2 (holds 1 − 1 = 0) and then ask for R1.', 14))
    o.append(T(360, 358, 'Waits can only point up the numbers, so no wait can loop back: no cycle.', 14, bold=True))
    return 374, ''.join(o)
FIG[6] = (f6, 'With R1 < R2 < R3, P1 may ask for R2 because 2 > 1, but P2 may not ask for R1 while holding R2. P2 must release R2 first, so the wait cycle can never close.',
          'Three numbered resources in a row; P1 holding R1 asks for R2 and is allowed, P2 holding R2 asks for R1 and is refused.')


# ---- 3.7 banker's safety algorithm ----
def f7():
    procs = [('P0', '0,1,0', '7,4,3', 4), ('P1', '2,0,0', '1,2,2', 1), ('P2', '3,0,2', '6,0,0', 5), ('P3', '2,1,1', '0,1,1', 2), ('P4', '0,0,2', '4,3,1', 3)]
    o = [T(40, 40, 'process', 13, fill=MUT, bold=True), T(120, 40, 'Allocation', 13, fill=MUT, bold=True), T(220, 40, 'Need', 13, fill=MUT, bold=True),
         T(300, 40, 'order', 13, fill=MUT, bold=True), L(14, 50, 336, 50, L2, 1.5)]
    for i, (p, a, n, k) in enumerate(procs):
        y = 58 + i * 46
        o.append(R(14, y, 322, 38, ACS if k == 1 else PANEL, AC if k == 1 else LN, 6, 1.5 if k == 1 else 1))
        o.append(T(40, y + 25, p, 14, bold=True)); o.append(T(120, y + 25, f'({a})', 14)); o.append(T(220, y + 25, f'({n})', 14))
        o.append(num(300, y + 19, k, NX))
    o.append(T(175, 312, 'Need = Max − Allocation', 13, fill=MUT))
    o.append(T(530, 26, 'Work (free instances of A, B, C)', 14, bold=True))
    work = ['3,3,2', '5,3,2', '7,4,3', '7,4,5', '7,5,5', '10,5,7']
    steps = [('P1', '1,2,2', '2,0,0'), ('P3', '0,1,1', '2,1,1'), ('P4', '4,3,1', '0,0,2'), ('P0', '7,4,3', '0,1,0'), ('P2', '6,0,0', '3,0,2')]
    for i, w in enumerate(work):
        y = 40 + i * 54
        o.append(boxt(372, y, 100, 32, [f'({w})'], NXS if i == 5 else (ACS if i == 1 else PANEL), NX if i == 5 else AC, 14, bold_first=True, rx=6))
        if i < 5:
            p, n, a = steps[i]
            o.append(L(422, y + 32, 422, y + 52, AC, 2, arrow='n'))
            o.append(T(484, y + 47, f'{p} fits ({n}), gives back ({a})', 13, 'start', MUT))
    o.append(T(484, 40 + 54 + 22, '← after P1: (5,3,2)', 13, 'start', AC, True))
    o.append(T(360, 362, 'Safe sequence: P1 → P3 → P4 → P0 → P2. All five can finish, so the state is safe.', 14, bold=True))
    return 378, ''.join(o)
FIG[7] = (f7, 'Starting from Work = (3,3,2), the safety test keeps picking a process whose Need fits and adds back its Allocation: P1, P3, P4, P0, P2. Every process can finish, so the state is safe.',
          'Left, a table of Allocation and Need for P0 to P4 with their finishing order. Right, Work growing from (3,3,2) to (10,5,7) as each process finishes.')


# ---- 3.8 deadlock detection ----
def f8():
    o = [T(150, 26, 'Detection: Work starts at free = [0,0,0]', 14, bold=True)]
    work = [('[0,0,0]', ''), ('[1,0,0]', 'P2 asks [0,0,0]: fits, frees [1,0,0]'), ('[2,0,0]', 'P4 asks [0,0,0]: fits, frees [1,0,0]')]
    for i, (w, lab) in enumerate(work):
        y = 44 + i * 74
        if i:
            o.append(L(80, y - 30, 80, y - 4, AC, 2, arrow='n'))
            o.append(T(100, y - 12, lab, 13, 'start', MUT))
        o.append(boxt(30, y, 100, 34, [w], ACS if i < 2 else NXS, AC if i < 2 else NX, 14, bold_first=True, rx=6))
    o.append(boxt(30, 250, 330, 56, ['P1 asks C, P3 asks B: Work has 0 of each,', 'so neither fits and the scan stops'], LVS, LV, 13, rx=8))
    o.append(T(530, 26, 'Who waits for whom', 14, bold=True))
    for n, x, y in (('P1', 450, 150), ('P3', 630, 150)):
        o.append(f'<circle cx="{x}" cy="{y}" r="30" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2.5"/>' + T(x, y + 6, n, 16, bold=True))
    o.append(f'<path d="M474,132 C510,92 570,92 604,130" style="fill:none;stroke:var(--live);stroke-width:2.5" marker-end="url(#ar-UID-l)"/>')
    o.append(T(540, 82, 'P1 waits for C, held by P3', 13, fill=LV, bold=True))
    o.append(f'<path d="M606,170 C570,208 510,208 476,170" style="fill:none;stroke:var(--live);stroke-width:2.5" marker-end="url(#ar-UID-l)"/>')
    o.append(T(540, 226, 'P3 waits for B, held by P1', 13, fill=LV, bold=True))
    for j, n in enumerate(('P2', 'P4')):
        o.append(boxt(440 + j * 110, 254, 90, 44, [n, 'finished'], NXS, NX, 13, bold_first=True))
    o.append(T(360, 346, 'Unfinished after the scan: P1 and P3, so 2 processes are deadlocked.', 15, bold=True))
    return 362, ''.join(o)
FIG[8] = (f8, 'The detector finishes P2 and P4, which ask for nothing, and Work grows to [2,0,0]. P1 and P3 each wait for the single instance the other holds, so these 2 are deadlocked.',
          'Left, Work growing from [0,0,0] to [2,0,0] as P2 and P4 finish. Right, P1 and P3 with arrows each way: each waits for a resource the other holds.')


spec = make_spec(FIG)
