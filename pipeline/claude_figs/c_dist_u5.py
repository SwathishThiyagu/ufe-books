"""Claude's hand-drawn figures for c-dist-u5 (Parallel and Distributed Computing, unit 5: mutual exclusion, deadlock
detection, agreement, checkpointing, fault tolerance and replication), one per chapter, from each chapter's worked example,
plus text fixes (no university names in the books)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def proc(y, name, x0=90, x1=690):
    return T(x0 - 14, y + 5, name, 15, 'end', bold=True) + L(x0, y, x1, y, L2, 2, arrow='m')


def arrow(x1, y1, x2, y2, c=AC, dash=None, a='n', lab=None, lx=0, ly=0, size=12):
    d = 1 if y2 > y1 else -1
    o = L(x1, y1, x2, y2 - 8 * d, c, 2, dash, a)
    if lab: o += Tb((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, lab, size, fill=c)
    return o


def cs(x1, x2, y, lab, c=NX, f=NXS):
    return R(x1, y - 11, x2 - x1, 22, f, c, 4) + T((x1 + x2) / 2, y + 5, lab, 12, bold=True)


# ---- 5.1 Ricart–Agrawala ----
def f1():
    y = {1: 80, 2: 180, 3: 280}
    o = [T(20, 24, 'All three send REQUEST(ts) to the other two first: 6 requests', 14, 'start', bold=True)]
    o += [proc(y[1], 'P1'), proc(y[2], 'P2'), proc(y[3], 'P3')]
    for p, ts in ((1, 10), (2, 8), (3, 12)):
        o.append(R(104, y[p] - 12, 70, 24, PANEL, L2, 5)); o.append(T(139, y[p] + 5, f'REQ {ts}', 12, bold=True))
    o.append(arrow(200, y[1], 210, y[2], AC))
    o.append(arrow(225, y[3], 235, y[2], AC))
    o.append(arrow(250, y[3], 262, y[1], AC))
    o.append(cs(280, 350, y[2], 'P2 in CS'))
    o.append(arrow(350, y[2], 380, y[1], LV, '5 4', 'l')); o.append(arrow(356, y[2], 386, y[3], LV, '5 4', 'l'))
    o.append(cs(400, 470, y[1], 'P1 in CS'))
    o.append(arrow(470, y[1], 520, y[3], LV, '5 4', 'l'))
    o.append(cs(540, 610, y[3], 'P3 in CS'))
    o.append(L(30, 318, 60, 318, AC, 2, arrow='n')); o.append(T(68, 323, 'immediate REPLY', 13, 'start'))
    o.append(L(210, 318, 240, 318, LV, 2, '5 4', arrow='l')); o.append(T(248, 323, 'deferred REPLY, sent on exit', 13, 'start'))
    o.append(T(20, 348, 'P2 defers 10 and 12 (its 8 is smaller); P1 defers 12 (its 10 is smaller).', 13, 'start', MUT))
    o.append(T(20, 374, 'Order P2 (8), P1 (10), P3 (12). 6 REQUEST + 6 REPLY = 12 messages = 2(N − 1) = 4 per entry.', 14, 'start', bold=True))
    return 388, ''.join(o)
FIG[1] = (f1, 'The smallest timestamp wins: P2 (8) gets both replies and enters first, while it and P1 defer the later requests. Each exit sends the deferred replies, so P1 (10) and then P3 (12) enter; 12 messages in all, 4 per entry.',
          'Three process lines. All send requests with timestamps 10, 8 and 12; replies go to P2, which enters the critical section, then exit replies let P1 and then P3 enter.')


# ---- 5.2 Suzuki–Kasami token ----
def f2():
    y = {1: 60, 2: 130, 3: 270, 4: 200}
    o = [proc(y[i], f'P{i}') for i in (1, 2, 4, 3)]
    o.append(R(98, y[1] - 13, 60, 26, LVS, LV, 13)); o.append(T(128, y[1] + 5, 'token', 12, bold=True))
    o.append(T(170, 30, 'P2, P4, P3 broadcast REQUEST(sn = 1): 3 × 3 = 9 messages', 13, 'start', MUT))
    o.append(arrow(190, y[1], 230, y[2], LV, None, 'l', 'token, Q = [ ]', lx=-52))
    o.append(cs(240, 340, y[2], 'P2 in CS'))
    o.append(Tb(346, y[2] - 18, 'P4 request arrives: Q = [4]', 12, 'start'))
    o.append(arrow(340, y[2], 380, y[4], LV, None, 'l', 'token', lx=24))
    o.append(cs(390, 490, y[4], 'P4 in CS'))
    o.append(Tb(496, y[4] - 18, 'P3 request arrives: Q = [3]', 12, 'start'))
    o.append(arrow(490, y[4], 530, y[3], LV, None, 'l', 'token', lx=24))
    o.append(cs(540, 640, y[3], 'P3 in CS'))
    o.append(Tb(590, y[3] + 30, 'Q empty: P3 keeps the token', 12))
    o.append(T(20, 330, 'Order P2, P4, P3; LN = [0, 1, 1, 1]. 9 + 3 = 12 messages for 3 entries: N = 4 each.', 14, 'start', bold=True))
    return 346, ''.join(o)
FIG[2] = (f2, 'P1 holds the token and is idle, so P2\'s request gets it at once with an empty queue. Each later request reaches the current holder while it is inside and waits in Q, so the token goes P1 → P2 → P4 → P3: 12 messages, N = 4 per entry.',
          'Four process lines. The token moves from P1 to P2, then to P4, then to P3, each running its critical section; the queue holds the next requester each time.')


# ---- 5.3 probes around a wait-for cycle ----
def f3():
    pos = {1: (180, 80), 2: (540, 80), 3: (360, 270)}
    o = []
    for i, (x, yv) in pos.items():
        o.append(R(x - 70, yv - 34, 140, 68, PANEL, L2, 10))
        o.append(T(x, yv - 10, f'site S{i}', 12, fill=MUT))
        o.append(T(x, yv + 16, f'P{i} blocked', 15, bold=True))
    o.append(L(252, 80, 466, 80, AC, 2.5, arrow='n')); o.append(Tb(360, 70, 'P1 waits for P2', 13, fill=AC))
    o.append(L(500, 116, 410, 232, AC, 2.5, arrow='n')); o.append(Tb(515, 180, 'P2 waits for P3', 13, 'start', AC))
    o.append(L(310, 232, 220, 116, AC, 2.5, arrow='n')); o.append(Tb(205, 180, 'P3 waits for P1', 13, 'end', AC))
    o.append(Tb(360, 112, '① probe(P1, P2, P1)', 13, fill=LV, bold=True))
    o.append(Tb(455, 212, '② probe(P2, P3, P1)', 13, 'start', LV, bold=True))
    o.append(Tb(265, 212, '③ probe(P3, P1, P1)', 13, 'end', LV, bold=True))
    o.append(T(20, 336, 'Probe ③ reaches P1 as the waited-on process (second field P1): cycle closed, deadlock after 3 probes.', 13, 'start'))
    return 350, ''.join(o)
FIG[3] = (f3, 'P1 waits for P2, P2 for P3 and P3 for P1. P1 starts a probe that follows each wait; the third probe, probe(P3, P1, P1), comes back to P1 itself, so P1 declares a deadlock after 3 probes.',
          'Three sites in a triangle with wait-for arrows P1 to P2, P2 to P3 and P3 to P1, each labelled with the probe that travels along it.')


# ---- 5.4 oral messages, f = 1, N = 4 ----
def f4():
    C0 = (360, 50)
    Lp = {1: (130, 200), 2: (360, 200), 3: (590, 200)}
    o = [boxt(310, 30, 100, 40, ['C: 1'], ACS, AC, 15)]
    for i, (x, yv) in Lp.items():
        f, st = (NXS, NX) if i == 3 else (PANEL, AC)
        o.append(boxt(x - 50, yv - 20, 100, 40, [f'L{i}' + (' traitor' if i == 3 else '')], f, st, 14, bold_first=True))
        o.append(L(360, 72, x, yv - 24, AC, 2, arrow='n'))
        o.append(Tb((360 + x) / 2 + (0 if i == 2 else (-14 if i == 1 else 14)), (72 + yv - 24) / 2, '1', 13, fill=AC, bold=True))
    o.append(T(470, 112, 'round 1: C sends 1 to all', 12, 'start', MUT))
    # round 2
    o.append(L(182, 192, 304, 192, AC, 1.8, arrow='n')); o.append(L(308, 208, 186, 208, AC, 1.8, arrow='n'))
    o.append(T(245, 186, '1', 13, fill=AC, bold=True)); o.append(T(245, 226, '1', 13, fill=AC, bold=True))
    o.append(L(538, 200, 416, 200, NX, 2, '6 4', arrow='x')); o.append(T(477, 192, '0', 13, fill=NX, bold=True))
    o.append(arc(570, 222, 150, 224, 0.16, NX, 2, 'x', '6 4')); o.append(Tb(360, 264, 'L3 says "C said 0"', 13, fill=NX, bold=True))
    o.append(T(20, 296, 'L1 collects 1 (C), 1 (L2), 0 (L3)', 14, 'start')); o.append(T(380, 296, 'L2 collects 1 (C), 1 (L1), 0 (L3)', 14, 'start'))
    o.append(T(20, 320, '3 values, majority 2 of 3 → decide 1', 14, 'start', bold=True)); o.append(T(380, 320, '3 values, majority 2 of 3 → decide 1', 14, 'start', bold=True))
    o.append(T(20, 350, 'N = 4 = 3f + 1 for f = 1. With N = 3 each loyal lieutenant would hold only 1 and 0: no majority.', 13, 'start', MUT))
    return 364, ''.join(o)
FIG[4] = (f4, 'C sends 1 to every lieutenant; in round 2 the loyal L1 and L2 pass on 1 while the traitor L3 says 0. Each loyal lieutenant holds 1, 1, 0 and decides 1 by a 2-of-3 majority, which needs N = 3f + 1 = 4.',
          'Commander C sends 1 to three lieutenants; loyal L1 and L2 exchange 1 while traitor L3 sends 0 to both; each loyal lieutenant collects 1, 1, 0 and decides 1.')


# ---- 5.5 checkpoints, orphans and the recovery line ----
def f5():
    fx = lambda t: 90 + t * 42
    y = {1: 60, 2: 150, 3: 240}
    o = [proc(y[p], f'P{p}', 90, 690) for p in (1, 2, 3)]
    ck = {1: [1, 7], 2: [2, 8], 3: [3, 11]}
    for p, ts in ck.items():
        for j, t in enumerate(ts):
            o.append(R(fx(t) - 6, y[p] - 14, 12, 28, NXS if j == 0 else PANEL, NX if j == 0 else L2, 2))
            o.append(T(fx(t), y[p] - 20, f'C{p},{j}', 12, fill=NX if j == 0 else MUT, bold=j == 0))
            if j == 1: o.append(L(fx(t) - 9, y[p] - 12, fx(t) + 9, y[p] + 12, LV, 2) + L(fx(t) - 9, y[p] + 12, fx(t) + 9, y[p] - 12, LV, 2))
    M = [('m1', 1, 4, 2, 5), ('m2', 2, 6, 3, 9), ('m3', 3, 5, 1, 6), ('m4', 1, 7.2, 2, 7.6)]
    for n, s, ts, r, tr in M:
        o.append(arrow(fx(ts), y[s], fx(tr), y[r], AC if n != 'm4' else LV, '5 4', 'n' if n != 'm4' else 'l'))
        lp = {'m1': (fx(4.5) - 8, 105, 'end'), 'm2': (fx(7.5) + 12, 195, 'start'), 'm3': (fx(5.14) + 10, 215, 'start'), 'm4': (fx(7.4) + 10, 105, 'start')}[n]
        o.append(Tb(lp[0], lp[1], n, 12, lp[2], AC if n != 'm4' else LV))
    o.append(T(fx(13), y[1] - 16, 'crash', 13, fill=LV, bold=True))
    o.append(L(fx(13) - 9, y[1] - 9, fx(13) + 9, y[1] + 9, LV, 3) + L(fx(13) - 9, y[1] + 9, fx(13) + 9, y[1] - 9, LV, 3))
    o.append(P([(fx(1), 30), (fx(1), y[1]), (fx(2), y[2]), (fx(3), y[3]), (fx(3), 268)], NX, 2.5, '8 5'))
    o.append(xaxis(fx(0), fx(14), 280, [0, 2, 4, 6, 8, 10, 12, 14], fx, None))
    o.append(T(20, 330, 'm4 orphans C2,1 → P2 to C2,0; then m2 orphans C3,1 → P3 to C3,0; then m3 orphans C1,1 → P1 to C1,0', 13, 'start'))
    o.append(T(20, 352, 'Recovery line at 1, 2, 3 s: 3 rollbacks, lost work 12 + 11 + 10 = 33 s', 14, 'start', NX, bold=True))
    return 364, ''.join(o)
FIG[5] = (f5, 'After P1 crashes at 13 s, m4, then m2, then m3 are each received before a checkpoint but sent after the sender\'s restart point, so every later checkpoint is crossed out in turn. The recovery line falls back to the first checkpoints at 1, 2 and 3 s, losing 33 s of work.',
          'Three process lines with two checkpoints each and four messages; the later checkpoints are crossed out and a dashed recovery line joins the first checkpoints at 1, 2 and 3 seconds.')


# ---- 5.6 duplicate suppression ----
def f6():
    yc, ys = 60, 200
    o = [proc(yc, 'client', 90, 450), proc(ys, 'server', 90, 450)]
    o.append(arrow(120, yc, 160, ys, AC, None, 'n', 'debit ₹500, id 77', lx=-58))
    o.append(R(150, ys + 14, 120, 40, ACS, AC, 6)); o.append(T(210, ys + 30, '2000 → 1500', 12, bold=True)); o.append(T(210, ys + 46, 'table {77: reply}', 11, fill=MUT))
    o.append(L(180, ys, 230, 130, LV, 2, '5 4')); o.append(L(222, 122, 238, 138, LV, 3) + L(222, 138, 238, 122, LV, 3))
    o.append(Tb(246, 148, 'reply lost', 12, 'start', LV))
    for k, x in enumerate((320, 392)):
        o.append(arrow(x, yc, x + 20, ys, AC, None, 'n'))
        o.append(arrow(x + 28, ys, x + 48, yc, NX, '5 4', 'x'))
    o.append(Tb(360, ys + 30, 'retries: id 77 seen,', 12, fill=NX)); o.append(Tb(360, ys + 46, 'stored reply sent again', 12, fill=NX))
    o.append(Tb(380, yc - 16, '2 retries', 12, fill=AC))
    o.append(boxt(480, 40, 220, 80, ['with suppression', '1 debit applied', 'balance ₹1500'], NXS, NX, 14, bold_first=True))
    o.append(boxt(480, 140, 220, 80, ['without suppression', '3 debits applied', 'balance 2000 − 1500 = ₹500'], LVS, LV, 13, bold_first=True))
    o.append(T(20, 300, '3 replicas: majority = ⌊3/2⌋ + 1 = 2, so after one crash the 2 left still form a majority.', 14, 'start'))
    return 316, ''.join(o)
FIG[6] = (f6, 'The server applies the ₹500 debit for id 77 once and records the reply. The reply is lost, so the client retries twice, and both retries get the stored reply: the balance stays ₹1500 instead of falling to ₹500.',
          'Client and server lines: one debit request is applied and logged, its reply is lost, and two retries get the stored reply; boxes compare balances with and without duplicate suppression.')


# ---- 5.7 quorums ----
def f7():
    o = [T(20, 24, 'N = 3, write quorum W = 2: write x = 10 (version 5)', 14, 'start', bold=True)]
    R3 = [(40, 'R1', 'v5, x = 10', ACS, AC), (280, 'R2', 'v5, x = 10', ACS, AC), (520, 'R3', 'v4, x = 7', NXS, NX)]
    for x, n, v, f, st in R3:
        o.append(boxt(x, 120, 160, 56, [n, v], f, st, 14, bold_first=True))
    o.append(boxt(250, 40, 220, 36, ['writer: x = 10'], PANEL, AC, 14))
    o.append(L(300, 78, 130, 116, AC, 2, arrow='n')); o.append(L(360, 78, 360, 116, AC, 2, arrow='n'))
    o.append(L(420, 78, 600, 116, L2, 1.5, '4 4')); o.append(Tb(540, 92, 'missed', 12, fill=MUT))
    # read R=2
    o.append(boxt(200, 240, 260, 44, ['read R = 2: sees v5 and v4 → 10'], LVS, LV, 13))
    o.append(L(330, 238, 360, 180, LV, 2, arrow='l')); o.append(L(420, 238, 580, 180, LV, 2, arrow='l'))
    o.append(T(470, 266, 'read repair: R3 ← v5', 12, 'start', LV))
    o.append(boxt(520, 296, 180, 44, ['read R = 1 at R3 → 7'], NXS, NX, 13))
    o.append(L(610, 294, 610, 180, NX, 2, '5 4', arrow='x'))
    o.append(T(20, 314, 'R + W = 2 + 2 = 4 > 3: quorums overlap,', 13, 'start')); o.append(T(20, 332, 'the newest value is always seen', 13, 'start'))
    o.append(T(20, 360, 'R + W = 1 + 2 = 3, not > 3: a read can miss the write and return the stale 7', 13, 'start', NX))
    return 372, ''.join(o)
FIG[7] = (f7, 'The write reaches R1 and R2 only. A read of 2 replicas must overlap that write quorum (2 + 2 > 3), so it sees version 5 and returns 10, then repairs R3; a read of 1 replica can land on R3 alone and return the stale 7.',
          'Three replica boxes: R1 and R2 at version 5 with x equal 10, R3 still at version 4 with x equal 7; a two-replica read returns 10 and repairs R3, a one-replica read at R3 returns 7.')


TEXT = {
    4: [('synchronous and randomised systems can still always agree.', 'synchronous systems can always agree, and randomised algorithms agree with probability 1.')],
    6: [('Together they keep a wallet or bank balance correct over an unreliable network. Only a few universities teach this advanced chapter.',
         'Together they keep a wallet or bank balance correct over an unreliable network.')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}


def text_fixes(k):
    return TEXT.get(k, [])


def drop_sources():
    return ['csail.mit.edu']


def unit_fixes():
    return [('a process that wants the section and has a lower timestamp replies at once, otherwise it defers the reply.',
             'a receiver replies at once unless it is inside the section or wants it with a lower timestamp, in which case it defers the reply.'),
            ('The token carries a queue Q of waiting processes and an array RN of the largest request number seen from each process.',
             'The token carries a queue Q of waiting processes and an array LN of the last request number served for each process; every process keeps its own RN array of the largest request numbers it has seen.')]
