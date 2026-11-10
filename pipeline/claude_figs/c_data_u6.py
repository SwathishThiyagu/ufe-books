"""Claude's hand-drawn figures for c-data-u6 (Data Science, unit 6: big data platforms), one per chapter, from each
chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARR = {AC: 'n', L2: 'm', LV: 'l', NX: 'x', MUT: 'm', INK: 'm'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=ARR[c])


def chip(x, y, s, f, st, w=46, h=24, size=13):
    return R(x, y, w, h, f, st, 4, 1.5) + T(x + w / 2, y + h * 0.7, s, size, bold=True)


# ---- 6.1 smart meters: from one reading to nine servers ----
def f1():
    steps = [('2,000,000 meters', '× 96 a day'), ('192,000,000', 'readings a day'), ('48 GB a day', '× 250 B each'),
             ('17.52 TB a year', '× 365'), ('52.56 TB', '× 3 copies'), ('70.08 TB raw', '÷ 0.75 (25% free)')]
    o = []
    for i, (a, b) in enumerate(steps):
        x, y = 20 + (i % 3) * 236, 30 + (i // 3) * 84
        o.append(boxt(x, y, 200, 56, [a, b], ACS if i < 3 else LVS, AC if i < 3 else LV, 14, True))
        if i % 3 < 2: o.append(ar(x + 200, y + 28, x + 234, y + 28, AC if i < 3 else LV))
    o += [P([(692, 58), (706, 58), (706, 98), (14, 98), (14, 142), (18, 142)], AC, 2), ar(12, 142, 18, 142, AC)]
    o.append(boxt(500, 196, 200, 50, ['÷ 8 TB a server', '= 8.76 → 9 servers'], NXS, NX, 14, True))
    o.append(ar(600, 170, 600, 194, NX))
    o.append(T(20, 210, 'readings per second', 14, 'start', MUT, True))
    o += [T(110, 240, 'average', 13, 'end', INK, True), R(120, 226, 2222 / 33333 * 340, 22, ACS, AC, 3, 1.5), T(130 + 2222 / 33333 * 340, 242, '2,222', 14, 'start', AC, True),
          T(110, 276, 'peak', 13, 'end', INK, True), R(120, 262, 340, 22, LVS, LV, 3, 1.5), T(130 + 340, 278, '33,333', 14, 'start', LV, True)]
    o.append(T(20, 320, 'Peak: every meter sends in the first 60 s of a slot, 2,000,000 ÷ 60 = 33,333 a second, 15 times the average.', 13, 'start', INK, True))
    return 334, ''.join(o)


FIG[1] = (f1, 'One 250-byte reading every 15 minutes from 20 lakh meters grows to 17.52 TB a year and 70.08 TB of raw disk, nine servers. Readings arrive in bursts 15 times the average rate.',
          'A chain of boxes: 2,000,000 meters times 96 a day gives 192,000,000 readings, 48 GB a day, 17.52 TB a year, 52.56 TB with 3 copies and 70.08 TB raw with 25% free, which is 9 servers of 8 TB. Bars compare the average 2,222 readings a second with the peak 33,333.')


# ---- 6.2 HDFS blocks and rack-aware replicas ----
def f2():
    o = [T(20, 26, 'sales.csv, 500 MB', 14, 'start', INK, True)]
    cols = [(ACS, AC), (NXS, NX), (LVS, LV), (PANEL, INK)]
    sizes = [128, 128, 128, 116]
    x = 160
    for i, (s, (f, st)) in enumerate(zip(sizes, cols)):
        w = s * 1.1
        o += [R(x, 10, w, 32, f, st, 0, 1.5), T(x + w / 2, 31, f'B{i + 1}: {s} MB', 13, bold=True)]
        x += w
    place = {'DN1': ['B1', 'B4'], 'DN2': ['B2', 'B4'], 'DN3': ['B2', 'B3'], 'DN4': ['B2', 'B3'], 'DN5': ['B1', 'B3'], 'DN6': ['B1', 'B4']}
    cmap = {'B1': cols[0], 'B2': cols[1], 'B3': cols[2], 'B4': cols[3]}
    for r, (rx, nodes) in enumerate([(20, ['DN1', 'DN2', 'DN3']), (370, ['DN4', 'DN5', 'DN6'])]):
        o += [R(rx, 64, 330, 150, 'none', L2, 8, 1.5, '6 4'), T(rx + 12, 84, f'Rack {r + 1}', 14, 'start', MUT, True)]
        for k, dn in enumerate(nodes):
            nx = rx + 14 + k * 106
            o += [R(nx, 96, 96, 104, PANEL, L2, 6, 1.5), T(nx + 48, 116, dn, 14, bold=True)]
            for j, b in enumerate(place[dn]):
                f, st = cmap[b]
                o.append(chip(nx + 25, 128 + j * 34, b, f, st))
    o.append(T(20, 246, 'B1 → DN1, DN5, DN6: one copy in Rack 1 and two in Rack 2, so it survives losing either rack.', 14, 'start', AC, True))
    o.append(T(20, 270, '4 blocks × 3 = 12 replicas, 1,500 MB of disk (B4 is not padded). Any 2 DataNodes may fail.', 14, 'start'))
    o.append(T(20, 294, 'NameNode: 5 objects × 150 B ≈ 750 B; as 50,000 small files it would need about 15 MB.', 13, 'start', MUT))
    o.append(T(20, 318, 'Cluster: 6 × 4 TB = 24 TB, 75% usable = 18 TB, ÷ 3 replicas = 6 TB of data.', 13, 'start', MUT))
    return 332, ''.join(o)


FIG[2] = (f2, 'The 500 MB file becomes blocks of 128, 128, 128 and 116 MB, each stored three times. Every block has copies in both racks, and each DataNode ends up holding two replicas.',
          'A file bar split into B1, B2, B3 of 128 MB and B4 of 116 MB. Two dashed racks with DataNodes DN1 to DN6, each holding two coloured block chips: DN1 B1 and B4, DN2 B2 and B4, DN3 B2 and B3, DN4 B2 and B3, DN5 B1 and B3, DN6 B1 and B4.')


# ---- 6.3 word count: map, combine, shuffle, reduce ----
def f3():
    o = [T(80, 22, 'split', 13, fill=MUT, bold=True), T(250, 22, 'map', 13, fill=MUT, bold=True), T(410, 22, 'combine', 13, fill=MUT, bold=True),
         T(620, 22, 'reduce', 13, fill=MUT, bold=True)]
    o += [boxt(20, 34, 120, 52, ['upi pay upi', 'cricket pay'], PANEL, L2, 13, True),
          boxt(20, 166, 120, 52, ['upi cricket', 'pay upi'], PANEL, L2, 13, True)]
    m1 = ['(upi,1) (pay,1)', '(upi,1)', '(cricket,1) (pay,1)']
    m2 = ['(upi,1) (cricket,1)', '(pay,1) (upi,1)']
    o.append(boxt(160, 30, 180, 62, m1, ACS, AC, 13))
    o.append(boxt(160, 166, 180, 52, m2, ACS, AC, 13))
    o.append(boxt(360, 30, 110, 62, ['(cricket,1)', '(pay,2)', '(upi,2)'], NXS, NX, 13))
    o.append(boxt(360, 160, 110, 62, ['(cricket,1)', '(pay,1)', '(upi,2)'], NXS, NX, 13))
    o += [ar(140, 60, 158, 60, L2), ar(140, 192, 158, 192, L2), ar(340, 60, 358, 60, L2), ar(340, 192, 358, 192, L2)]
    o += [boxt(540, 34, 160, 52, ['R0 (a–m)', 'cricket [1, 1] → 2'], LVS, LV, 13, True),
          boxt(540, 150, 160, 78, ['R1 (n–z)', 'pay [2, 1] → 3', 'upi [2, 2] → 4'], LVS, LV, 13, True)]
    for y1, y2 in [(44, 60), (62, 176), (82, 200), (172, 66), (192, 180), (212, 210)]:
        o.append(ar(470, y1, 538, y2, AC, 1.5))
    o.append(Tb(505, 128, 'shuffle', 13, fill=AC, bold=True))
    o.append(T(20, 266, 'Pairs over the network: 9 without the combiner, 3 + 3 = 6 with it.', 14, 'start', NX, True))
    o.append(T(20, 290, 'Output: cricket 2, pay 3, upi 4 (9 words in, 2 + 3 + 4 = 9 counted).', 14, 'start', LV, True))
    o.append(T(20, 314, 'A 10 GB log: 10,240 ÷ 128 = 80 map tasks; 40 at a time gives 2 waves.', 13, 'start', MUT))
    return 328, ''.join(o)


FIG[3] = (f3, 'Each mapper emits (word, 1), its combiner adds locally, and the shuffle sends every pair for a word to one reducer: cricket to R0, pay and upi to R1. The combiner cuts the shuffle from 9 pairs to 6.',
          'Two splits feed two map boxes of (word, 1) pairs, then combiner boxes with (cricket,1) (pay,2) (upi,2) and (cricket,1) (pay,1) (upi,2). Crossing shuffle arrows lead to reducer R0 giving cricket 2 and R1 giving pay 3 and upi 4.')


# ---- 6.4 the Hive / Pig query and its map waves ----
def f4():
    rows = [('101', 'Chennai', '1200'), ('102', 'Mumbai', '800'), ('103', 'Chennai', '450'), ('104', 'Pune', '300'), ('105', 'Mumbai', '1500'), ('106', 'Chennai', '950')]
    o = [T(20, 22, '/data/sales', 14, 'start', MUT, True)]
    for i, (a, b, c) in enumerate(rows):
        y = 32 + i * 26
        drop = a == '104'
        o += [R(20, y, 180, 26, LVS if drop else PANEL, LV if drop else L2, 0, 1.2),
              T(50, y + 18, a, 13, fill=MUT if drop else INK), T(110, y + 18, b, 13, fill=MUT if drop else INK), T(175, y + 18, c, 13, fill=MUT if drop else INK)]
    o.append(L(24, 32 + 3 * 26 + 13, 196, 32 + 3 * 26 + 13, LV, 2))
    o += [ar(204, 110, 236, 110, AC), T(335, 28, 'filter amount ≥ 400, group by city', 13, fill=AC, bold=True)]
    o += [boxt(240, 40, 190, 50, ['Chennai', '1200, 450, 950'], ACS, AC, 14, True), boxt(240, 110, 190, 50, ['Mumbai', '800, 1500'], ACS, AC, 14, True)]
    o += [ar(430, 65, 468, 65, NX), ar(430, 135, 468, 135, NX), T(450, 104, 'SUM', 13, fill=NX, bold=True)]
    o += [boxt(470, 40, 230, 50, ['Chennai 2,600 (3 orders)'], NXS, NX, 14, True), boxt(470, 110, 230, 50, ['Mumbai 2,300 (2 orders)'], NXS, NX, 14, True)]
    o.append(T(470, 184, 'ORDER BY total DESC; Pune is filtered out', 13, 'start', MUT))
    o.append(T(20, 226, 'full year: 25,600 MB ÷ 128 MB = 200 map tasks; 10 nodes × 12 containers − 1 for the AM = 119 at once', 13, 'start', INK, True))
    o += [T(20, 262, 'wave 1', 13, 'start', AC, True), R(80, 248, 119 * 3, 22, ACS, AC, 3, 1.5), T(80 + 119 * 1.5, 264, '119 maps', 13, fill=AC, bold=True),
          T(20, 292, 'wave 2', 13, 'start', LV, True), R(80, 278, 81 * 3, 22, LVS, LV, 3, 1.5), T(80 + 81 * 1.5, 294, '81 maps', 13, fill=LV, bold=True)]
    o.append(T(20, 324, 'Hive (SQL) and Pig Latin (step by step) give the same result as jobs that YARN runs.', 13, 'start', MUT))
    return 338, ''.join(o)


FIG[4] = (f4, 'The filter drops order 104, grouping leaves Chennai and Mumbai, and the sums are 2,600 and 2,300. For the full-year file, 200 map tasks run in two waves of 119 and 81.',
          'Six sales rows with order 104 (Pune, 300) struck out. Arrows group Chennai 1200, 450, 950 and Mumbai 800, 1500, then sum to Chennai 2,600 from 3 orders and Mumbai 2,300 from 2. Bars show map wave 1 with 119 tasks and wave 2 with 81.')


# ---- 6.5 quorum reads and writes ----
def f5():
    o = []

    def panel(x0, title, W, Rr, ok):
        out = [T(x0, 22, title, 15, 'start', NX if ok else LV, True)]
        for k, n in enumerate(['C', 'D', 'A']):
            x = x0 + 20 + k * 104
            w, r = n in W, n in Rr
            out += [R(x, 84, 80, 70, NXS if (w and r) else (ACS if w else PANEL), NX if (w and r) else (AC if w else L2), 8, 2), T(x + 40, 126, n, 22, bold=True)]
            if w: out += [ar(x + 40, 60, x + 40, 82, AC), T(x + 40, 54, 'write', 13, fill=AC, bold=True)]
            if r: out += [ar(x + 40, 180, x + 40, 156, LV), T(x + 40, 196, 'read', 13, fill=LV, bold=True)]
        return out
    o += panel(20, 'QUORUM / QUORUM: R + W = 4 > 3', 'CD', 'DA', True)
    o += panel(380, 'ONE / ONE: R + W = 2, not > 3', 'C', 'A', False)
    o += [T(20, 228, 'The 2 read always share one (D) with the', 13, 'start', NX),
          T(20, 246, '2 written: reads are current; 1 may be down.', 13, 'start', NX),
          T(380, 228, 'The read can miss the write:', 13, 'start', LV),
          T(380, 246, 'stale data, but the fastest reply.', 13, 'start', LV)]
    o.append(T(20, 286, 'Key hash 37 lies in C\'s range (25, 50], so C owns it and D and A, next clockwise, hold copies (RF = 3).', 13, 'start', INK, True))
    o.append(T(20, 310, 'QUORUM = ⌊3 ÷ 2⌋ + 1 = 2.  A key hashing to 90 goes to A, B and C.', 13, 'start', MUT))
    return 324, ''.join(o)


FIG[5] = (f5, 'The row with key hash 37 lives on C, D and A. With QUORUM writes and reads, 2 + 2 > 3, so the sets always overlap and reads are current; with ONE and ONE they can miss each other.',
          'Two panels of three replicas C, D and A. Left, QUORUM: writes go to C and D and reads come from D and A, overlapping at D. Right, ONE: the write goes to C and the read comes from A, so they do not overlap.')


# ---- 6.6 stages and tasks of the word count ----
def f6():
    o = [R(14, 30, 400, 196, 'none', AC, 8, 1.5, '6 4'), T(24, 50, 'stage 1 (narrow steps run together)', 13, 'start', AC, True),
         R(440, 30, 160, 196, 'none', LV, 8, 1.5, '6 4'), T(450, 50, 'stage 2', 13, 'start', LV, True)]
    steps = ['textFile', 'flatMap', 'map']
    for p in range(2):
        y = 70 + p * 76
        for k, s in enumerate(steps):
            x = 30 + k * 128
            o.append(boxt(x, y, 104, 50, [s, f'partition {p}'], ACS, AC, 13, True))
            if k < 2: o.append(ar(x + 104, y + 25, x + 126, y + 25, AC))
        o.append(boxt(460, y, 120, 50, ['reduceByKey', f'partition {p}'], LVS, LV, 13, True))
    for a in range(2):
        for b in range(2):
            o.append(ar(390, 95 + a * 76, 458, 95 + b * 76, LV, 1.5))
    o.append(Tb(424, 134, 'shuffle', 13, fill=LV, bold=True))
    o.append(boxt(620, 104, 90, 50, ['collect()', 'driver'], NXS, NX, 13, True))
    o += [ar(580, 95, 618, 122, NX, 1.5), ar(580, 171, 618, 138, NX, 1.5)]
    o.append(T(20, 262, 'Transformations are lazy: nothing runs until the action collect() is called.', 14, 'start', INK, True))
    o.append(T(20, 286, 'One wide step (reduceByKey) means one shuffle, so 2 stages; 2 + 2 = 4 tasks.', 14, 'start', LV, True))
    return 300, ''.join(o)


FIG[6] = (f6, 'With 2 input and 2 reduce partitions, the narrow steps textFile, flatMap and map run together as stage 1; the shuffle for reduceByKey starts stage 2. That is 2 stages and 4 tasks, run only when collect() is called.',
          'Two rows of three blue boxes, textFile, flatMap and map for partitions 0 and 1, inside a dashed stage 1. Crossing shuffle arrows lead to two orange reduceByKey boxes in stage 2, which both feed collect() at the driver.')


# ---- 6.7 roll-up, slice and dice on the sales cube ----
def f7():
    cities = [('Chennai', 'TN', [40, 45, 30, 35]), ('Coimbatore', 'TN', [25, 20, 10, 12]), ('Bengaluru', 'KA', [55, 60, 50, 52]), ('Mysuru', 'KA', [15, 18, 8, 9])]
    heads = ['Phones Q1', 'Phones Q2', 'Laptops Q1', 'Laptops Q2']
    x0, cw, rh = 150, 82, 32
    o = [T(20, 22, 'sales, ₹ lakh', 13, 'start', MUT, True)]
    for j, h in enumerate(heads):
        o += [R(x0 + j * cw, 30, cw, rh, PANEL, L2, 0, 1.2), T(x0 + j * cw + cw / 2, 51, h, 13, bold=True)]
    for i, (c, st, vs) in enumerate(cities):
        y = 30 + (i + 1) * rh
        o.append(T(x0 - 8, y + 21, f'{c} ({st})', 13, 'end', INK, True))
        for j, v in enumerate(vs):
            q1 = j in (0, 2)
            dice = c in ('Chennai', 'Bengaluru') and j in (1, 3)
            f = NXS if dice else (ACS if q1 else 'var(--fig)')
            sk = NX if dice else (AC if q1 else L2)
            o += [R(x0 + j * cw, y, cw, rh, f, sk, 0, 1.6 if sk != L2 else 1.2), T(x0 + j * cw + cw / 2, y + 21, str(v), 14, bold=dice)]
    o += [R(490, 30, 14, 14, ACS, AC, 0, 1.5), T(510, 42, 'slice Q1: 135 + 98 = 233', 13, 'start', AC, True),
          R(490, 56, 14, 14, NXS, NX, 0, 1.5), T(510, 68, 'dice: Chennai Q2 80,', 13, 'start', NX, True), T(510, 86, 'Bengaluru Q2 112', 13, 'start', NX, True)]
    o.append(T(20, 216, 'roll-up, phones: city → state', 14, 'start', LV, True))
    for i, (s, a, b) in enumerate([('TN', '40 + 25 = 65', '45 + 20 = 65'), ('KA', '55 + 15 = 70', '60 + 18 = 78')]):
        y = 230 + i * 30
        o += [T(60, y + 20, s, 14, 'end', LV, True), boxt(70, y, 150, 28, [f'Q1 {a}'], LVS, LV, 13, rx=0), boxt(220, y, 150, 28, [f'Q2 {b}'], LVS, LV, 13, rx=0)]
    o.append(T(400, 240, 'fact rows a year:', 13, 'start', MUT, True))
    o.append(T(400, 260, '200 × 5,000 × 365 × 4%', 13, 'start'))
    o.append(T(400, 280, '= 14,600,000 rows ≈ 584 MB', 13, 'start', INK, True))
    return 300, ''.join(o)


FIG[7] = (f7, 'The cube as a table: the blue Q1 columns are the slice (total ₹233 lakh), the green cells the dice for Chennai and Bengaluru in Q2, and adding cities by state is the roll-up.',
          'A table of phone and laptop sales for Chennai, Coimbatore, Bengaluru and Mysuru in Q1 and Q2. The Q1 columns are shaded blue for the slice, and Chennai and Bengaluru Q2 cells green for the dice. Below, a roll-up gives TN 65 and 65, KA 70 and 78.')


# ---- 6.8 generalising to 4-anonymity ----
def f8():
    rows = [(1, 23, 'M', '600017', 'Flu'), (2, 27, 'M', '600020', 'Asthma'), (5, 24, 'M', '600018', 'Diabetes'), (7, 29, 'M', '600011', 'Flu'),
            (3, 31, 'F', '600028', 'Diabetes'), (4, 36, 'F', '600024', 'Flu'), (6, 38, 'F', '600029', 'Asthma'), (8, 33, 'F', '600026', 'Flu')]
    o = [T(20, 22, 'names removed: k = 1', 14, 'start', LV, True), T(400, 22, 'age → decade, PIN → 6000**: k = 4', 14, 'start', NX, True)]
    ws = [30, 44, 30, 76, 80]
    for i, (n, a, g, p, d) in enumerate(rows):
        y = 34 + i * 28
        x = 20
        for w, s in zip(ws, [str(n), str(a), g, p, d]):
            o += [R(x, y, w, 28, LVS if n == 2 else 'var(--fig)', L2, 0, 1), T(x + w / 2, y + 19, s, 13)]
            x += w
        grp = 0 if g == 'M' else 1
        f, st = (ACS, AC) if grp == 0 else (NXS, NX)
        x = 400
        for w, s in zip([30, 64, 30, 76, 80], [str(n), '20–29' if grp == 0 else '30–39', g, '6000**', d]):
            o += [R(x, y, w, 28, f, st, 0, 1), T(x + w / 2, y + 19, s, 13)]
            x += w
    o.append(ar(290, 146, 392, 146, NX))
    o.append(T(20, 280, 'row 2 (27, M, 600020) is unique: Asthma leaks', 13, 'start', LV, True))
    o += [T(700, 280, 'each group of 4 has 3 diseases: 3-diverse', 13, 'end', NX, True)]
    o.append(T(20, 316, 'In a group of 4 the best guess of a person\'s row is 1 in 4 = 25%, against 100% before.', 14, 'start', INK, True))
    return 330, ''.join(o)


FIG[8] = (f8, 'With names removed every row is still unique, so k = 1. Coarsening age to decades and PIN to 6000** leaves two groups of four, so k = 4 and each group holds three different diseases.',
          'Left: eight hospital rows with age, gender, PIN and disease, row 2 shaded as unique. An arrow leads to the generalised table on the right: four men aged 20–29 and four women aged 30–39, all with PIN 6000**, shaded as two groups.')

spec = make_spec(FIG)
