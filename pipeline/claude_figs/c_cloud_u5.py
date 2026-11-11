"""Claude's hand-drawn figures for c-cloud-u5 (Cloud Computing, unit 5: parallel and task programming, MapReduce,
Spark, AWS, Google Cloud, Azure, open-source clouds and CloudSim), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def hbar(x, y, w, h, fill, c, label=None, size=13, fc=INK, bold=False):
    o = R(x, y, w, h, fill, c, 4, 2)
    if label: o += T(x + w / 2, y + h / 2 + size * 0.36, label, size, fill=fc, bold=bold)
    return o


# ---- 5.1 four threads: 40 ms of work, 10 ms of overhead ----
def f1():
    X0, X1 = 130, 650
    fx = lambda ms: X0 + ms / 160 * (X1 - X0)
    o = [T(40, 24, 'Adding 8,000,000 numbers', 15, 'start', bold=True)]
    o.append(T(X0 - 12, 64, '1 thread', 14, 'end', bold=True))
    o.append(hbar(fx(0), 44, fx(160) - fx(0), 32, PANEL, L2, '160 ms', 13))
    y = 100
    o.append(hbar(fx(0), y, fx(5) - fx(0), 4 * 30 - 6, LVS, LV))
    o.append(hbar(fx(45), y, fx(50) - fx(45), 4 * 30 - 6, LVS, LV))
    for i in range(4):
        o.append(T(X0 - 12, y + i * 30 + 18, f'thread {i + 1}', 13, 'end'))
        o.append(hbar(fx(5), y + i * 30, fx(45) - fx(5), 24, ACS, AC, '40 ms', 13))
    o.append(T(fx(2.5), y + 140, 'create 5', 13, 'end', LV, True))
    o.append(T(fx(47.5), y + 140, 'merge 5', 13, 'start', LV, True))
    o.append(T(fx(50) + 40, y + 50, 'each thread adds 2,000,000 numbers', 13, 'start')); o.append(T(fx(50) + 40, y + 76, 'T(4) = 5 + 40 + 5 = 50 ms', 15, 'start', bold=True))
    o.append(xaxis(X0, X1, y + 160, [0, 40, 80, 120, 160], fx, 'milliseconds'))
    o.append(T(40, y + 222, 'Ideal 160 ÷ 40 = 4×. Actual 160 ÷ 50 = 3.2×. Efficiency 3.2 ÷ 4 = 80%.', 14, 'start', bold=True))
    o.append(T(40, y + 244, 'The 10 ms of creating and merging runs on one thread, outside the parallel stretch.', 13, 'start'))
    return y + 260, ''.join(o)
FIG[1] = (f1, 'One thread takes 160 ms; four threads each add 2,000,000 numbers in 40 ms, but 5 ms to create them and 5 ms to merge the sums make it 50 ms, so the speedup is 3.2×, not 4×.',
          'A long 160 ms bar for one thread above four parallel 40 ms bars framed by a 5 ms creation block and a 5 ms merge block, ending at 50 ms.')


# ---- 5.2 600 tasks on 12 workers ----
def f2():
    X0, X1 = 120, 600
    fx = lambda m: X0 + m / 240 * (X1 - X0)
    o = [T(40, 24, '600 tasks of 4 min on 12 workers: 50 tasks each', 15, 'start', bold=True)]
    y = 44
    for i in range(12):
        yy = y + i * 20
        o.append(T(X0 - 10, yy + 13, f'worker {i + 1}', 12 if False else 13, 'end', MUT))
        o.append(R(fx(0), yy, fx(200) - fx(0), 16, ACS, AC, 3, 1.5))
        o.append(R(fx(200), yy, fx(225) - fx(200), 16, LVS, LV, 3, 1.5))
    yb = y + 12 * 20
    o.append(L(fx(200), y - 6, fx(200), yb + 4, AC, 1.5, '4 4')); o.append(L(fx(225), y - 6, fx(225), yb + 4, LV, 1.5, '4 4'))
    o.append(T(fx(100), y + 6 * 20 - 6, '50 × 4 = 200 min of work', 14, bold=True))
    o.append(T(fx(225) + 8, y + 5 * 20 + 2, '50 × 0.5', 13, 'start', LV, True))
    o.append(T(fx(225) + 8, y + 6 * 20 + 2, '= 25 min overhead', 13, 'start', LV, True))
    o.append(xaxis(X0, X1, yb + 10, [0, 60, 120, 180, 225], fx, 'minutes'))
    o.append(T(40, yb + 74, 'Ideal makespan 200 min; actual 225 min. Throughput 600 ÷ 225 ≈ 2.67 tasks a minute.', 14, 'start', bold=True))
    return yb + 92, ''.join(o)
FIG[2] = (f2, 'Each of the 12 workers runs 50 tasks, 200 minutes of work plus 25 minutes of scheduling overhead, so the run ends at 225 minutes and the throughput is about 2.67 tasks a minute.',
          'Twelve worker lanes, each a 200-minute work bar followed by a 25-minute overhead bar, all ending together at 225 minutes.')


# ---- 5.3 word count through map, combine, shuffle, reduce ----
def f3():
    cols = [('input', 30), ('map', 160), ('combine', 320), ('shuffle', 460), ('reduce', 590)]
    o = [T(x + 55, 24, n, 14, bold=True) for n, x in cols]
    lines = [('cat dog cat', ['(cat,1)', '(dog,1)', '(cat,1)'], ['cat 2', 'dog 1']), ('dog', ['(dog,1)'], ['dog 1']), ('cat', ['(cat,1)'], ['cat 1'])]
    ys = [44, 154, 214]
    hs = [96, 46, 46]
    for (ln, mp, cb), y, h in zip(lines, ys, hs):
        o.append(boxt(30, y, 110, h, [ln], PANEL, L2, 13))
        o.append(R(160, y, 130, h, ACS, AC, 6))
        for i, m in enumerate(mp):
            o.append(TM(225, y + 22 + i * 26 if len(mp) > 1 else y + h / 2 + 5, m, 13))
        o.append(R(320, y, 110, h, NXS, NX, 6))
        for i, m in enumerate(cb):
            o.append(T(375, y + h / 2 + 5 + (i - (len(cb) - 1) / 2) * 24, m, 13, bold=True))
        o.append(L(142, y + h / 2, 156, y + h / 2, AC, 2, arrow='n')); o.append(L(292, y + h / 2, 316, y + h / 2, AC, 2, arrow='n'))
    o.append(boxt(460, 64, 110, 50, ['cat → [2, 1]'], LVS, LV, 13))
    o.append(boxt(460, 174, 110, 50, ['dog → [1, 1]'], LVS, LV, 13))
    for (yf, yt) in [(80, 86), (104, 190), (177, 200), (237, 104)]:
        o.append(L(432, yf, 456, yt, L2, 1.5, arrow='m'))
    o.append(boxt(590, 64, 100, 50, ['cat 3'], ACS, AC, 15))
    o.append(boxt(590, 174, 100, 50, ['dog 2'], ACS, AC, 15))
    o.append(L(572, 89, 586, 89, AC, 2, arrow='n')); o.append(L(572, 199, 586, 199, AC, 2, arrow='n'))
    o.append(T(40, 300, 'The combiner adds inside each map task first, so line 1 sends cat 2 instead of two (cat,1) pairs.', 13, 'start'))
    o.append(T(40, 322, 'Shuffle groups by key; reduce adds the lists: 2 + 1 = 3 and 1 + 1 = 2, 5 words in all.', 14, 'start', bold=True))
    return 338, ''.join(o)
FIG[3] = (f3, 'Each line becomes (word, 1) pairs, the combiner adds them inside each map task, the shuffle groups cat [2, 1] and dog [1, 1], and the reducer outputs cat 3 and dog 2.',
          'Five columns, input, map, combine, shuffle and reduce, following three lines of words to the final counts cat 3 and dog 2.')


# ---- 5.4 the Spark lineage of word count ----
def f4():
    o = []
    stages = [('lines', ['a b a', 'b c'], PANEL, L2, None),
              ('flatMap(split)', ['a', 'b', 'a', 'b', 'c'], ACS, AC, None),
              ('map(w → (w,1))', ['(a,1)', '(b,1)', '(a,1)', '(b,1)', '(c,1)'], ACS, AC, None),
              ('reduceByKey(add)', ['(a,2)', '(b,2)', '(c,1)'], LVS, LV, 'shuffle'),
              ('collect()', ['[(a,2), (b,2),', ' (c,1)]'], NXS, NX, 'action')]
    xs = [20, 156, 282, 428, 570]
    ws = [116, 100, 120, 118, 140]
    for (name, items, f, c, tag), x, w in zip(stages, xs, ws):
        o.append(T(x + w / 2, 30, name, 13, bold=True))
        h = 18 + 26 * len(items)
        o.append(R(x, 44, w, h, f, c, 8))
        for i, it in enumerate(items):
            o.append(TM(x + w / 2, 66 + i * 26, it, 13))
        if tag: o.append(T(x + w / 2, 44 + h + 20, tag, 13, fill=c, bold=True))
    for x, w, nx in zip(xs, ws, xs[1:]):
        o.append(L(x + w + 2, 100, nx - 4, 100, AC, 2, arrow='n'))
    o.append(R(20, 210, 540, 26, 'none', AC, 6, 1.5, '6 4'))
    o.append(T(290, 228, 'lazy transformations: only a plan (the lineage) is built', 13, fill=AC, bold=True))
    o.append(T(20, 266, 'Nothing runs until collect(); then 2 lines → 5 words → 5 pairs → 3 keys, returned as [(a,2), (b,2), (c,1)].', 13, 'start'))
    return 284, ''.join(o)
FIG[4] = (f4, 'The transformations only build a plan; collect() runs it: 2 lines become 5 words and 5 pairs, reduceByKey shuffles and adds them, and the job returns [(a,2), (b,2), (c,1)].',
          'Five stages left to right, lines, flatMap, map, reduceByKey and collect, each showing its records, with the first four marked lazy and the shuffle and action labelled.')


# ---- 5.5 the AWS design: two subnets and the security-group rules ----
def f5():
    o = [R(20, 40, 520, 330, 'none', AC, 12, 2)]
    o.append(T(36, 62, 'VPC 10.0.0.0/16 (65,536 addresses)', 14, 'start', bold=True))
    o.append(R(40, 76, 480, 150, ACS, AC, 10, 1.5))
    o.append(T(56, 98, 'public subnet 10.0.1.0/24: 251 usable', 13, 'start', bold=True))
    o.append(boxt(160, 110, 110, 40, ['web 1'], PANEL, AC, 13)); o.append(boxt(160, 164, 110, 40, ['web 2'], PANEL, AC, 13))
    o.append(boxt(380, 136, 130, 44, ['load balancer'], PANEL, AC, 13))
    o.append(L(378, 150, 274, 132, AC, 2, arrow='n')); o.append(L(378, 166, 274, 182, AC, 2, arrow='n'))
    o.append(T(405, 212, 'web-sg: 443 from anywhere', 13, fill=AC, bold=True))
    o.append(R(40, 236, 480, 120, NXS, NX, 10, 1.5))
    o.append(boxt(160, 262, 140, 40, ['database'], PANEL, NX, 13))
    o.append(L(215, 206, 215, 258, NX, 2.5, arrow='x')); o.append(Tb(224, 236, '3306', 13, 'start', bold=True))
    o.append(T(320, 276, 'db-sg: 3306 only from web-sg', 13, 'start', NX, True))
    o.append(T(56, 342, 'private subnet 10.0.2.0/24: 251 usable, no internet route', 13, 'start', bold=True))
    o.append(boxt(580, 60, 120, 40, ['internet'], PANEL, L2, 14))
    o.append(boxt(580, 136, 120, 40, ['internet gateway'], PANEL, L2, 13))
    o.append(L(640, 102, 640, 132, AC, 2, arrow='n'))
    o.append(L(578, 158, 514, 158, AC, 2.5, arrow='n')); o.append(Tb(546, 150, '443', 13, bold=True))
    o.append(P([(600, 178), (600, 294), (304, 294)], LV, 2, '6 4'))
    o.append(T(610, 222, '3306 from', 13, 'start', LV, True)); o.append(T(610, 240, 'internet:', 13, 'start', LV, True)); o.append(T(610, 258, 'dropped ×', 13, 'start', LV, True))
    o.append(boxt(580, 318, 120, 34, ['S3: 100 GB'], LVS, LV, 13))
    o.append(boxt(580, 360, 120, 34, ['SQS queue'], LVS, LV, 13))
    o.append(T(20, 400, 'S3 and SQS sit outside the VPC as regional services, reached over HTTPS.', 13, 'start', MUT))
    return 414, ''.join(o)
FIG[5] = (f5, 'Users reach the load balancer and the two web servers in the public subnet on port 443; the database in the private subnet accepts 3306 only from web-sg, so a 3306 attempt from the internet is dropped. Each /24 has 251 usable addresses.',
          'A VPC box with a public subnet holding a load balancer and two web servers and a private subnet holding a database; arrows show 443 from the internet gateway and 3306 from web to database, with a dashed blocked path from the internet.')


# ---- 5.6 App Engine instances at a 50% CPU target ----
def f6():
    s = 8.5
    o = [T(40, 24, 'CPU-seconds per minute: demand against instances at the 50% target', 15, 'start', bold=True)]
    def row(y, title, demand, n):
        r = [T(40, y + 22, title, 14, 'start', bold=True)]
        r.append(hbar(200, y, demand * s, 30, LVS, LV, f'demand {demand}', 13))
        for i in range(n):
            r.append(hbar(200 + i * 30 * s, y + 38, 30 * s, 30, ACS, AC, f'instance {i + 1}: 30', 13))
        r.append(T(40, y + 58, f'⌈{demand} ÷ 30⌉ = {n}', 14, 'start', AC, True))
        return ''.join(r)
    o.append(row(44, '900 req/min', 27, 1))
    o.append(row(140, '1,800 req/min', 54, 2))
    o.append(T(40, 250, 'Demand = requests × 0.030 CPU-s. One instance gives 60 × 0.50 = 30 CPU-s a minute at the target.', 13, 'start'))
    o.append(T(40, 272, 'Trap: dividing by the full 60 gives ⌈54 ÷ 60⌉ = 1 and leaves the doubled load short.', 14, 'start', LV, True))
    return 288, ''.join(o)
FIG[6] = (f6, 'At a 50% target each instance supplies 30 CPU-seconds a minute. 900 requests need 27, so 1 instance; 1,800 requests need 54, so 2. Dividing by the full 60 would wrongly give 1.',
          'Two rows: a demand bar of 27 fitting inside one 30-unit instance block, and a demand bar of 54 needing two instance blocks.')


# ---- 5.7 the Azure resource group ----
def f7():
    o = [R(20, 20, 680, 340, 'none', L2, 12, 2, '8 5'), T(36, 42, 'resource group rg-web-prod: 9 resources', 14, 'start', bold=True)]
    o.append(R(40, 56, 470, 230, 'none', AC, 10, 2))
    o.append(T(56, 78, '1 VNet 10.0.0.0/16: 2¹⁶ = 65,536 addresses', 13, 'start', bold=True))
    o.append(R(60, 100, 200, 174, ACS, AC, 8, 1.5)); o.append(T(160, 120, 'web subnet /24', 13, bold=True)); o.append(T(160, 138, '256, 251 usable', 13, fill=MUT))
    o.append(boxt(76, 152, 78, 36, ['VM 1'], PANEL, AC, 13)); o.append(boxt(166, 152, 78, 36, ['VM 2'], PANEL, AC, 13))
    o.append(boxt(90, 222, 140, 34, ['NSG: allow 443'], LVS, LV, 13))
    o.append(R(290, 100, 200, 174, NXS, NX, 8, 1.5)); o.append(T(390, 120, 'DB subnet /24', 13, bold=True)); o.append(T(390, 138, '256, 251 usable', 13, fill=MUT))
    o.append(boxt(320, 152, 140, 36, ['Azure SQL Database'], PANEL, NX, 13))
    o.append(boxt(320, 222, 140, 34, ['NSG: allow 1433'], LVS, LV, 13))
    o.append(L(246, 170, 316, 170, NX, 2.5, arrow='x')); o.append(Tb(281, 164, '1433', 13, bold=True))
    o.append(boxt(540, 70, 140, 40, ['internet'], PANEL, L2, 13))
    o.append(P([(538, 90), (250, 90)], AC, 2.5)); o.append(L(250, 90, 250, 98, AC, 2.5, arrow='n'))
    o.append(Tb(400, 94, '443', 13, bold=True))
    o.append(boxt(540, 190, 140, 60, ['storage account', '100 GB blob, ₹150/mo'], NXS, NX, 13))
    o.append(T(40, 310, 'Count: VNet 1 + subnets 2 + NSGs 2 + VMs 2 + SQL 1 + storage 1 = 9 (the blob container sits inside its account).', 13, 'start'))
    o.append(T(40, 334, 'Two flows only: internet → web on 443, web subnet → DB on 1433. The database has no internet path.', 13, 'start', bold=True))
    return 372, ''.join(o)
FIG[7] = (f7, 'The resource group holds 9 resources: a /16 VNet with two /24 subnets (251 usable addresses each), two NSGs, two web VMs, Azure SQL Database and a storage account. Only 443 into web and 1433 from web to the database are allowed.',
          'A dashed resource group containing a VNet with a web subnet of two VMs and a DB subnet with Azure SQL Database, each with an NSG, plus a storage account; arrows show 443 from the internet and 1433 from web to the database.')


# ---- 5.8 how many VMs fit on the private cloud ----
def f8():
    s = 2.6
    o = [T(40, 24, '7 usable hosts (1 of 8 kept for control): 224 vCPU, 896 GB RAM', 15, 'start', bold=True)]
    def pair(y, title, cpu, ram):
        r = [T(40, y + 6, title, 14, 'start', bold=True)]
        r.append(T(40, y + 36, 'CPU allows', 13, 'start'))
        r.append(hbar(150, y + 18, cpu * s, 28, ACS if cpu < ram else NXS, AC if cpu < ram else NX, f'{cpu} VMs', 13, bold=True))
        r.append(T(40, y + 70, 'RAM allows', 13, 'start'))
        r.append(hbar(150, y + 52, ram * s, 28, NXS, NX, f'{ram} VMs', 13, bold=True))
        return ''.join(r)
    o.append(pair(56, '1:1 CPU', 56, 112))
    o.append(T(150 + 56 * s + 12, 56 + 37, '224 ÷ 4 = 56: CPU is the limit', 13, 'start', AC, True))
    o.append(T(150 + 112 * s + 12, 56 + 71, '896 ÷ 8', 13, 'start', MUT))
    o.append(pair(170, '2:1 CPU', 112, 112))
    o.append(T(150 + 112 * s + 12, 170 + 37, '448 ÷ 4', 13, 'start', MUT))
    o.append(T(150 + 112 * s + 12, 170 + 71, '896 ÷ 8', 13, 'start', MUT))
    o.append(T(40, 292, 'The smaller limit wins: 56 VMs at 1:1, 112 at 2:1, where RAM is now fully used too.', 14, 'start', bold=True))
    return 310, ''.join(o)
FIG[8] = (f8, 'With 224 vCPU and 896 GB, CPU allows 56 VMs and RAM 112 at 1:1, so 56 fit. At 2:1 CPU overcommit both limits are 112, so 112 fit.',
          'Two pairs of bars for 1:1 and 2:1 CPU overcommit, showing VMs allowed by CPU and by RAM: 56 and 112, then 112 and 112.')


# ---- 5.9 CloudSim SJF on one VM ----
def f9():
    X0, X1 = 90, 660
    fx = lambda t: X0 + t / 31 * (X1 - X0)
    o = [T(40, 24, 'Five cloudlets, shortest first, on one 1,000 MIPS VM', 15, 'start', bold=True)]
    jobs = [('C4', 2), ('C2', 5), ('C5', 6), ('C3', 8), ('C1', 10)]
    fills = [(NXS, NX), (ACS, AC), (ACS, AC), (ACS, AC), (LVS, LV)]
    t = 0
    for (n, d), (f, c) in zip(jobs, fills):
        o.append(hbar(fx(t), 48, fx(d) - fx(0), 40, f, c, n if d < 3 else f'{n} {d} s', 13, bold=True))
        t += d
        o.append(T(fx(t), 108, str(t), 13, bold=True))
    o.append(T(X0 - 10, 108, 'ends', 13, 'end', MUT))
    o.append(xaxis(X0, X1, 124, [0, 5, 10, 15, 20, 25, 31], fx, 'seconds'))
    y = 196
    o.append(T(40, y, 'cloudlet', 13, 'start', bold=True))
    heads = ['C4', 'C2', 'C5', 'C3', 'C1']
    waits = [0, 2, 7, 13, 21]
    for i, (h, w) in enumerate(zip(heads, waits)):
        o.append(T(170 + i * 80, y, h, 13, bold=True)); o.append(T(170 + i * 80, y + 22, f'{w} s', 13))
    o.append(T(40, y + 22, 'waits', 13, 'start', bold=True))
    o.append(T(40, y + 58, 'Mean wait 43 ÷ 5 = 8.6 s, mean turnaround 74 ÷ 5 = 14.8 s, makespan 31 s.', 14, 'start', bold=True))
    return y + 74, ''.join(o)
FIG[9] = (f9, 'Run time is length ÷ 1,000 MIPS, so shortest first gives C4, C2, C5, C3, C1 finishing at 2, 7, 13, 21 and 31 s; waits average 8.6 s and the makespan is 31 s.',
          'A Gantt bar of five touching cloudlets C4 2 s, C2 5 s, C5 6 s, C3 8 s and C1 10 s ending at 31 seconds, above a row of waiting times.')


spec = make_spec(FIG)


def text_fixes(k):
    return []
