"""Claude's hand-drawn figures for c-dist-u6 (Parallel and Distributed Computing, unit 6: naming and file systems,
distributed queries and transactions, cloud, virtualization, scaling, grids and the web), one per chapter, from each
chapter's worked example, plus text fixes (no university names in the books)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def seg(x, y, w, h, s, f, st, size=13):
    o = R(x, y, w, h, f, st, 4)
    if s and tw(s, size) < w - 6: o += T(x + w / 2, y + h / 2 + size * 0.36, s, size)
    return o


def proc(y, name, x0=110, x1=690):
    return T(x0 - 14, y + 5, name, 14, 'end', bold=True) + L(x0, y, x1, y, L2, 2, arrow='m')


def arrow(x1, y1, x2, y2, c=AC, dash=None, a='n'):
    d = 1 if y2 > y1 else -1
    return L(x1, y1, x2, y2 - 8 * d, c, 1.8, dash, a)


# ---- 6.1 resolving a path across a mount point ----
def f1():
    parts = [('/', 'local'), ('home', 'local'), ('ravi', 'local'), ('remote', 'mount point'), ('notes.txt', 'on server S')]
    o = [T(20, 24, 'open("/home/ravi/remote/notes.txt")', 15, 'start', bold=True)]
    x = 20
    for i, (n, k) in enumerate(parts):
        w = 104 if i < 3 else 150
        f, st = (PANEL, L2) if i < 3 else ((ACS, AC) if i == 3 else (LVS, LV))
        o.append(boxt(x, 46, w, 46, [n], f, st, 15, bold_first=True))
        o.append(T(x + w / 2, 112, k, 12, fill=MUT))
        if i < 4: o.append(L(x + w + 2, 69, x + w + 18, 69, L2, 2, arrow='m'))
        x += w + 22
    o.append(brace(20, 20 + 3 * 126 - 22, 128, INK))
    o.append(T(20 + (3 * 126 - 22) / 2, 150, '3 lookups on the client, no network', 13))
    o.append(R(380, 170, 320, 120, PANEL, LV, 10, dash='6 4'))
    o.append(T(540, 276, 'server S exports /export/ravi', 13, bold=True))
    o.append(L(470, 120, 470, 194, AC, 2, arrow='n')); o.append(T(462, 164, 'cached mount handle', 12, 'end', AC))
    o.append(L(620, 120, 604, 194, LV, 2, arrow='l')); o.append(T(628, 164, '1 RPC: lookup', 12, 'start', LV))
    o.append(boxt(400, 198, 280, 52, ['notes.txt → file handle'], LVS, LV, 14))
    o.append(T(20, 318, 'First open: 1 round trip to S. Second open, both handles cached: 0 round trips.', 14, 'start', bold=True))
    return 334, ''.join(o)
FIG[1] = (f1, 'The client walks /, home and ravi on its own disk; remote is a mount point for S:/export/ravi, so looking up notes.txt is one RPC to S. Once both file handles are cached, the second open needs no round trip.',
          'The path split into five boxes: three local directories, the remote mount point, and notes.txt on server S, reached by one lookup RPC.')


# ---- 6.2 three plans for R ⋈ S ----
def f2():
    o = [boxt(20, 30, 200, 56, ['site A: R', '100,000 × 100 B = 10 MB'], ACS, AC, 13, bold_first=True)]
    o.append(boxt(500, 30, 200, 56, ['site B: S', '500 × 60 B = 30 KB'], LVS, LV, 13, bold_first=True))
    o.append(L(498, 46, 222, 46, LV, 2, arrow='l')); o.append(Tb(360, 40, 'π_sid(S): 500 × 4 B = 2 KB', 13, fill=LV))
    o.append(L(222, 72, 498, 72, AC, 2, arrow='n')); o.append(Tb(360, 86, 'R′: 10,000 × 100 B = 1 MB', 13, fill=AC))
    o.append(T(360, 116, 'semi-join, then join R′ with S at B', 12, fill=MUT))
    fx = lambda b: 230 + b / 10e6 * 440
    plans = [('(a) ship R to B', 10e6, '10 MB, 80 s', PANEL, L2), ('(b) S to A, result to B', 1.63e6, '1.63 MB, 13.04 s', PANEL, L2),
             ('(c) semi-join', 1.002e6, '1.002 MB, 8.016 s', NXS, NX)]
    o.append(T(20, 160, 'bytes on the 125 KB/s link', 14, 'start', bold=True))
    for i, (n, b, s, f, st) in enumerate(plans):
        y = 176 + i * 40
        o.append(T(220, y + 20, n, 13, 'end'))
        o.append(R(fx(0), y, fx(b) - fx(0), 26, f, st, 4))
        if b > 5e6: o.append(T((fx(0) + fx(b)) / 2, y + 18, s, 13, bold=True))
        else: o.append(T(fx(b) + 8, y + 18, s, 13, 'start', bold=True))
    o.append(T(20, 316, 'Only 10 % of R joins, so the semi-join keeps 90 % of R off the link.', 14, 'start', NX))
    return 330, ''.join(o)
FIG[2] = (f2, 'The semi-join sends only S\'s 500 join keys (2 KB) to A and brings back the 10,000 matching tuples of R (1 MB). It moves 1,002,000 bytes in 8.016 s, against 10 MB and 80 s for shipping all of R.',
          'Sites A and B with the 2 kilobyte key list going to A and the 1 megabyte reduced relation coming back; below, three bars comparing bytes moved by the three plans.')


# ---- 6.3 two-phase commit, one no vote ----
def f3():
    y = {'coord': 50, 'A': 130, 'B': 200, 'C': 270}
    o = [proc(y[k], k if k != 'coord' else 'coordinator') for k in y]
    for k, x in (('A', 150), ('B', 162), ('C', 174)):
        o.append(arrow(x, y['coord'], x + 40, y[k], AC))
    o.append(T(160, 34, 'prepare ×3', 12, fill=AC))
    votes = {'A': ('yes', AC), 'B': ('yes', AC), 'C': ('no', NX)}
    for i, k in enumerate('ABC'):
        x = 290 + i * 18
        o.append(arrow(x, y[k], x + 46, y['coord'], votes[k][1], '5 4', 'x' if k == 'C' else 'n'))
    o.append(T(330, 34, 'votes yes, yes, no', 12, fill=NX))
    o.append(R(390, 38, 64, 24, NXS, NX, 4)); o.append(T(422, 55, 'abort', 12, bold=True))
    for k, x in (('A', 470), ('B', 482), ('C', 494)):
        o.append(arrow(x, y['coord'], x + 40, y[k], NX, None, 'x'))
    o.append(T(500, 34, 'abort ×3', 12, fill=NX))
    for i, k in enumerate('ABC'):
        x = 580 + i * 18
        o.append(arrow(x, y[k], x + 40, y['coord'], L2, '5 4', 'm'))
    o.append(T(620, 34, 'ack ×3', 12, fill=MUT))
    o.append(T(20, 306, 'A debits and B credits ₹5,000 in private workspaces and vote yes; C cannot lock the audit table: no.', 13, 'start'))
    o.append(T(20, 328, 'After abort all three discard their changes, release locks and acknowledge.', 13, 'start'))
    o.append(T(20, 356, '3 prepare + 3 votes + 3 abort + 3 ack = 12 messages; net movement 5000 − 5000 = ₹0.', 14, 'start', bold=True))
    o.append(T(20, 380, 'Only a COMMIT decision must be forced to the log before it is sent; an abort needs no forced record.', 13, 'start', MUT))
    return 394, ''.join(o)
FIG[3] = (f3, 'The coordinator asks A, B and C to prepare; A and B vote yes but C votes no, so the coordinator sends abort, every site discards its change and acknowledges: 12 messages and no money moved.',
          'Four time lines, coordinator, A, B and C: prepare messages go out, A and B vote yes and C votes no, abort messages go out and all three acknowledge.')


# ---- 6.4 IaaS vs PaaS: who manages what, and the bill ----
def f4():
    layers = ['application', 'runtime', 'operating system', 'virtual machine', 'hardware']
    o = []
    for c, (x, name, yours) in enumerate([(30, 'IaaS', 3), (260, 'PaaS', 1)]):
        o.append(T(x + 90, 26, name, 16, bold=True))
        for i, n in enumerate(layers):
            mine = i < yours
            o.append(boxt(x, 38 + i * 40, 180, 34, [n], ACS if mine else PANEL, AC if mine else L2, 13))
        o.append(T(x + 90, 252, f'you manage the top {yours}' if yours > 1 else 'you manage only the app', 12, fill=AC))
    o.append(R(500, 40, 20, 14, ACS, AC, 3)); o.append(T(526, 52, 'you', 13, 'start'))
    o.append(R(570, 40, 20, 14, PANEL, L2, 3)); o.append(T(596, 52, 'provider', 13, 'start'))
    fx = lambda r: 500 + r / 4200 * 200
    o.append(T(500, 96, 'monthly bill', 14, 'start', bold=True))
    o.append(T(500, 122, 'IaaS: 730 h × ₹2.5', 12, 'start', MUT))
    o.append(seg(500, 128, fx(1825) - 500, 28, '₹1,825', ACS, AC))
    o.append(T(500, 182, 'PaaS: ₹1,500 + 3,000 × ₹0.9', 12, 'start', MUT))
    o.append(seg(500, 188, fx(1500) - 500, 28, '₹1,500', PANEL, L2))
    o.append(seg(fx(1500), 188, fx(4200) - fx(1500), 28, '+ ₹2,700', LVS, LV))
    o.append(T(700, 234, '= ₹4,200', 13, 'end', bold=True))
    o.append(T(20, 292, 'IaaS is ₹2,375 cheaper a month, but the team patches the OS and runtime itself.', 14, 'start', bold=True))
    return 306, ''.join(o)
FIG[4] = (f4, 'With IaaS the team runs the application, runtime and operating system on a rented VM for ₹1,825 a month; PaaS takes all but the application off its hands but costs ₹1,500 plus ₹2,700 for 3 million requests, ₹4,200.',
          'Two five-layer stacks, IaaS with three layers shaded as yours and PaaS with only the application shaded, beside bars for monthly bills of 1,825 and 4,200 rupees.')


# ---- 6.5 pre-copy live migration ----
def f5():
    rounds = []
    d = 4096.0
    while True:
        rounds.append(d); t = d / 100; d = 40 * t
        if d < 64: break
    fx = lambda mb: 170 + mb / 4096 * 500
    o = [T(20, 24, '4096 MB VM, link 100 MB/s, guest dirties 40 MB/s: each round copies 40 % of the last', 14, 'start', bold=True)]
    for i, mb in enumerate(rounds + [d]):
        y = 44 + i * 40
        last = i == len(rounds)
        o.append(T(160, y + 20, 'stop-and-copy' if last else f'round {i + 1}', 13, 'end', bold=last))
        o.append(R(fx(0), y, max(fx(mb) - fx(0), 3), 26, NXS if last else ACS, NX if last else AC, 4))
        lab = f'{mb:,.2f} MB, {mb / 100:.2f} s'
        if fx(mb) - fx(0) > 200: o.append(T((fx(0) + fx(mb)) / 2, y + 18, lab, 13, bold=True))
        else: o.append(T(fx(mb) + 8, y + 18, lab, 13, 'start', NX if last else INK, bold=last))
    o.append(L(fx(64), 36, fx(64), 44 + 6 * 40 - 8, LV, 2, '5 4'))
    o.append(T(fx(64) + 6, 44 + 6 * 40 + 6, 'stop when < 64 MB is left', 12, 'start', LV))
    o.append(T(20, 330, '5 pre-copy rounds; total 6,798.70 MB in 67.99 s; the VM pauses only for the last 0.42 s.', 14, 'start', bold=True))
    return 344, ''.join(o)
FIG[5] = (f5, 'The VM keeps running while 4096 MB is copied; it dirtied 1638.4 MB meanwhile, which is copied next, and so on, each round 40 % of the last. After 5 rounds only 41.94 MB is left, so the VM pauses just 0.42 s for the final copy.',
          'Six shrinking bars: pre-copy rounds of 4096, 1638.4, 655.36, 262.14 and 104.86 megabytes, then a stop-and-copy of 41.94 megabytes, with a dashed line at 64 megabytes.')


# ---- 6.6 elastic vs fixed servers ----
def f6():
    x0, x1, y0, y1 = 70, 470, 50, 250
    fx = lambda h: x0 + h / 24 * (x1 - x0)
    fy = lambda n: y1 - n / 20 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 6, 12, 18, 24], [0, 5, 10, 15, 20], fx, fy, 'hour of the day', 'servers')]
    o.append(L(x0, fy(18), x1, fy(18), NX, 2.5, '8 5'))
    o.append(Tb(fx(1), fy(18) - 10, 'fixed: 18 all day', 13, 'start', NX))
    pts = [(fx(0), fy(1)), (fx(16), fy(1)), (fx(16), fy(18)), (fx(20), fy(18)), (fx(20), fy(1)), (fx(24), fy(1))]
    o.append(P([(fx(0), y1)] + pts + [(fx(24), y1)], AC, 2.5, fill=ACS))
    o.append(Tb(fx(18), fy(9), '4 h peak', 13))
    o.append(Tb(fx(8), fy(1) - 12, 'elastic: 1 server', 13, fill=AC))
    o.append(T(500, 60, 'peak sizing', 14, 'start', bold=True))
    for i, s in enumerate(['1 core: 1 ÷ 0.05 s = 20 req/s', '8 cores: 160 req/s', 'at 70 %: 112 req/s', '2000 ÷ 112 = 17.86 → 18']):
        o.append(T(500, 84 + i * 22, s, 13, 'start'))
    o.append(T(500, 200, 'per month at ₹6/server-hour', 13, 'start', MUT))
    o.append(T(500, 224, 'elastic: 600 × 1 × 6 + 120 × 18 × 6', 12, 'start'))
    o.append(T(500, 242, '= ₹16,560', 14, 'start', AC, bold=True))
    o.append(T(500, 268, 'fixed: 720 × 18 × 6 = ₹77,760', 13, 'start', NX))
    o.append(T(20, 312, 'Elastic scaling saves ₹77,760 − ₹16,560 = ₹61,200 a month.', 14, 'start', bold=True))
    return 326, ''.join(o)
FIG[6] = (f6, '2,000 requests a second at 112 per server needs 18 servers, but only for 4 hours a day. Scaling to 1 server for the other 20 hours costs ₹16,560 a month instead of ₹77,760 for 18 fixed servers, saving ₹61,200.',
          'Servers against hour of day: a dashed line at 18 for fixed servers and a shaded elastic curve at 1 server that rises to 18 for a 4-hour peak; the sizing and monthly costs are listed beside it.')


# ---- 6.7 grid broker schedule ----
def f7():
    x0, x1, y0, y1 = 80, 640, 50, 250
    fx = lambda h: x0 + h / 12 * (x1 - x0)
    fy = lambda c: y1 - c / 170 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 2, 4, 6, 8, 10, 12], [0, 40, 80, 120, 160], fx, fy, 'hours', 'free CPUs in use')]
    band = [('C: 20 CPUs', 0, 20, LVS, LV, 6.67), ('A: 40 CPUs', 20, 60, ACS, AC, 6.67), ('B: 100 CPUs', 60, 160, NXS, NX, 4)]
    for n, a, b, f, st, end in band:
        o.append(f'<rect x="{fx(0):.1f}" y="{fy(b):.1f}" width="{fx(end) - fx(0):.1f}" height="{fy(a) - fy(b):.1f}" style="fill:{f};stroke:{st};stroke-width:1.5"/>')
        o.append(T((fx(0) + fx(min(end, 4))) / 2, (fy(a) + fy(b)) / 2 + 5, n, 13, bold=True))
    o.append(T((fx(0) + fx(4)) / 2, (fy(60) + fy(160)) / 2 + 26, '160 × 4 h = 640 CPU-h', 13))
    o.append(Tb((fx(4) + fx(6.67)) / 2 - 4, fy(60) - 12, '60 × 2.67 h = 160', 13))
    o.append(L(fx(6.67), y0, fx(6.67), y1, INK, 2, '5 4')); o.append(Tb(fx(6.67) + 6, y0 + 14, 'done at 6.67 h', 13, 'start', bold=True))
    o.append(L(fx(12), y0, fx(12), y1, NX, 2)); o.append(Tb(fx(12) - 6, y0 + 14, 'deadline 12 h', 13, 'end', NX))
    o.append(T(20, 316, 'Free capacity 320 + 400 + 240 = 960 CPU-hours; the job uses 640 + 160 = 800 of them.', 14, 'start', bold=True))
    return 330, ''.join(o)
FIG[7] = (f7, 'For the first 4 hours all 160 free CPUs work, giving 640 CPU-hours; then B leaves and A and C\'s 60 CPUs supply the last 160 CPU-hours in 2.67 h. The 800 CPU-hour job finishes at 6.67 h, well before the 12 h deadline.',
          'Stacked bands of CPUs against hours: sites C, A and B together give 160 CPUs for 4 hours, then C and A give 60 CPUs until 6.67 hours; the deadline line is at 12 hours.')


# ---- 6.8 edge cache: hit, miss and average ----
def f8():
    fx = lambda ms: 170 + ms * 1.8
    o = [T(20, 24, '300 KB page at 2 MB/s = 150 ms of transfer', 14, 'start', bold=True)]
    rows = [('hit (92 %)', [(20, 'edge 20', LVS, LV), (150, 'transfer 150 ms', ACS, AC)], '170 ms'),
            ('miss (8 %)', [(120, 'origin 120 ms', NXS, NX), (150, 'transfer 150 ms', ACS, AC)], '270 ms')]
    for i, (lab, segs, tot) in enumerate(rows):
        y = 44 + i * 50
        o.append(T(160, y + 22, lab, 14, 'end'))
        t = 0
        for d, s, f, st in segs:
            o.append(seg(fx(t), y, fx(t + d) - fx(t), 32, s, f, st)); t += d
        o.append(T(664, y + 22, tot, 14, 'start', bold=True))
    o.append(T(fx(10), 40, 'edge 20 ms', 12, fill=LV))
    o.append(L(fx(178), 36, fx(178), 150, INK, 2, '5 4'))
    o.append(T(fx(178), 168, 'average 0.92 × 170 + 0.08 × 270 = 178 ms', 13, bold=True))
    o.append(T(20, 210, 'Against 270 ms with no cache, each request saves 270 − 178 = 92 ms.', 14, 'start'))
    o.append(T(20, 242, 'Origin traffic: 8 % of 1,000,000 = 80,000 misses a day', 14, 'start'))
    o.append(T(20, 266, '80,000 × 300 KB = 24 GB/day leave the origin instead of 300 GB.', 14, 'start', bold=True))
    return 282, ''.join(o)
FIG[8] = (f8, 'A hit costs a 20 ms edge round trip plus 150 ms of transfer, 170 ms; a miss goes to the origin, 270 ms. With 92 % hits the average is 178 ms, and only the 80,000 daily misses, 24 GB, leave the origin.',
          'Two bars: a cache hit of 20 plus 150 milliseconds and a miss of 120 plus 150 milliseconds, with a dashed line at the 178 millisecond average.')


TEXT = {
    1: [('NFS, AFS and HDFS all make this trade. Only a few universities teach this chapter, so keep the mechanism clear.',
         'NFS, AFS and HDFS all make this trade.')],
    7: [('Grids suit large batch jobs needing many CPU-hours (one CPU busy for one hour). Only a few universities teach this chapter.',
         'Grids suit large batch jobs needing many CPU-hours (one CPU busy for one hour).')],
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
    return [('A name plus the set of sites where that name can be resolved, so any site in the set gives the same answer',
             'The set of nodes visited while a name is resolved, from the starting directory to the object')]
