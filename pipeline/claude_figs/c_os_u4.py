"""Claude's hand-drawn figures for c-os-u4 (Operating Systems, unit 4: memory management and virtual memory), one per
chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 4.1 base and limit registers ----
def f1():
    o = [T(30, 30, 'If offset &lt; limit (1000): physical = base (14000) + offset. Else: trap.', 14, 'start', bold=True)]
    ytop, ybot = 70, 300
    my = lambda a: ytop + (a - 14000) / 1000 * (ybot - ytop)
    o.append(R(560, 46, 70, 290, PANEL, L2, 4, 1.5))
    o.append(R(560, ytop, 70, ybot - ytop, ACS, AC, 2, 2))
    o.append(T(595, 186, 'process', 13, fill=AC, bold=True))
    o.append(T(640, ytop + 5, '14000', 13, 'start', MUT)); o.append(T(640, ybot + 5, '15000', 13, 'start', MUT))
    o.append(T(595, 352, 'physical memory', 13, fill=MUT))
    rows = [(346, True), (999, True), (1200, False)]
    for i, (a, ok) in enumerate(rows):
        y = 70 + i * 92
        o.append(boxt(20, y, 92, 44, [str(a)], PANEL, INK, 15, bold_first=True))
        o.append(L(112, y + 22, 136, y + 22, AC, 2, arrow='n'))
        o.append(boxt(140, y, 140, 44, [f'{a} &lt; 1000 ?', 'yes' if ok else 'no'], NXS if ok else LVS, NX if ok else LV, 13, fills=[INK, NX if ok else LV]))
        o.append(L(280, y + 22, 304, y + 22, AC if ok else LV, 2, arrow='n' if ok else 'l'))
        if ok:
            p = 14000 + a
            o.append(boxt(308, y, 182, 44, [f'14000 + {a} = {p}'], ACS, AC, 13, bold_first=True))
            o.append(L(490, y + 22, 554, my(p), AC, 2, arrow='n'))
            o.append(f'<circle cx="{560}" cy="{my(p):.1f}" r="4" style="fill:var(--accent)"/>')
        else:
            o.append(boxt(308, y, 182, 44, ['trap: address error'], LVS, LV, 13, bold_first=True))
    o.append(T(66, 20 + 3 * 92 + 54, 'logical address', 13, fill=MUT))
    return 362, ''.join(o)
FIG[1] = (f1, 'Every address is checked against the limit before the base is added: 346 and 999 are below 1000 and land at 14346 and 14999, while 1200 is past the end and traps.',
          'Three logical addresses go through a less-than-1000 check: 346 and 999 pass and are added to base 14000, landing inside the process area; 1200 fails and traps.')


# ---- 4.2 cost of one swap ----
def f2():
    x0, s = 140, 560 / 4.02
    tx = lambda t: x0 + t * s
    o = [T(128, 96, 'Disk', 15, 'end', bold=True), T(128, 196, 'CPU', 15, 'end', bold=True)]
    o.append(R(tx(0), 72, 0.01 * s + 2, 40, LVS, LV, 2, 1.5))
    o.append(boxt(tx(0.01), 72, 2 * s, 40, ['copy out 100 MB: 100 ÷ 50 = 2 s'], LVS, LV, 13, rx=4))
    o.append(R(tx(2.01), 72, 0.01 * s + 2, 40, NXS, NX, 2, 1.5))
    o.append(boxt(tx(2.02), 72, 2 * s, 40, ['copy in 100 MB: 2 s'], NXS, NX, 13, rx=4))
    o.append(L(tx(0.005), 56, tx(0.005), 70, LV, 1.5)); o.append(T(tx(0) - 2, 50, '+ 10 ms latency', 13, 'start', LV))
    o.append(L(tx(2.015), 56, tx(2.015), 70, NX, 1.5)); o.append(T(tx(2.015) - 2, 50, '+ 10 ms latency', 13, 'start', NX))
    o.append(R(tx(0), 172, 4.02 * s, 40, PANEL, L2, 4, 1.5))
    o.append(f'<line x1="{tx(0):.1f}" y1="192" x2="{tx(4.02):.1f}" y2="192" style="stroke:var(--line2);stroke-width:30;stroke-dasharray:1 3"/>')
    o.append(Tb(tx(2.01), 197, 'other processes run: 402 slices of 10 ms', 13))
    o.append(xaxis(x0, tx(4.02), 232, [0, 1, 2.01, 3, 4.02], tx, 'seconds'))
    o.append(brace(tx(0), tx(4.02), 128, INK))
    o.append(T(tx(2.01), 156, 'one complete swap: 2.01 + 2.01 = 4.02 s', 14, bold=True))
    o.append(T(360, 314, '4.02 s ÷ 0.010 s = 402 time slices pass before the swapped process is back.', 14))
    return 330, ''.join(o)
FIG[2] = (f2, 'Swapping a 100 MB process out and another 100 MB back in takes 2.01 s each way at 50 MB/s plus 10 ms latency: 4.02 s in all, which is 402 time slices of 10 ms.',
          'A disk lane with copy out for 2.01 s then copy in for 2.01 s, above a CPU lane running other processes for the same 4.02 seconds.')


# ---- 4.3 first, best and worst fit ----
def f3():
    reqs = [212, 417, 112, 426]
    rows = [('First fit', 'first hole that fits', [('500', '288'), ('600', '183'), ('288', '176'), None]),
            ('Best fit', 'smallest hole that fits', [('300', '88'), ('500', '83'), ('200', '88'), ('600', '174')]),
            ('Worst fit', 'largest hole', [('600', '388'), ('500', '83'), ('388', '276'), None])]
    o = [T(30, 30, 'Holes in address order: 100, 500, 200, 300, 600 KB', 15, 'start', bold=True)]
    cx = lambda j: 250 + j * 120
    o.append(T(30, 72, 'request', 13, 'start', MUT, True))
    for j, r in enumerate(reqs):
        o.append(T(cx(j), 72, f'{r} KB', 14, bold=True))
    for i, (n, rule, cells) in enumerate(rows):
        y = 88 + i * 76
        o.append(R(20, y, 680, 66, ACS if i == 1 else PANEL, AC if i == 1 else LN, 8, 1.5 if i == 1 else 1))
        o.append(T(32, y + 29, n, 15, 'start', bold=True)); o.append(T(32, y + 49, rule, 13, 'start', MUT))
        for j, c in enumerate(cells):
            if c:
                o.append(T(cx(j), y + 29, f'{c[0]} → {c[1]}', 15)); o.append(T(cx(j), y + 49, 'hole → left over', 13, fill=MUT))
            else:
                o.append(T(cx(j), y + 29, 'waits', 15, fill=LV, bold=True)); o.append(T(cx(j), y + 49, 'no hole ≥ 426', 13, fill=LV))
    o.append(T(360, 342, 'Only best fit places all four; it keeps the 600 KB hole whole for the 426 KB request.', 14, bold=True))
    return 358, ''.join(o)
FIG[3] = (f3, 'Each cell gives the hole chosen and what is left over, in KB. First fit and worst fit break up the large holes early, so the 426 KB request waits; best fit keeps the 600 KB hole and places all four.',
          'A table of three strategies against four requests; each cell shows hole size and leftover, and the 426 KB request waits under first fit and worst fit.')


# ---- 4.4 paging address translation ----
def f4():
    o = [T(50, 36, 'logical address 8196', 14, 'start', bold=True), T(600, 126, 'physical address', 14, bold=True)]
    o.append(boxt(50, 56, 100, 46, ['p = 2'], LVS, LV, 16, bold_first=True, rx=4))
    o.append(boxt(150, 56, 100, 46, ['d = 4'], NXS, NX, 16, bold_first=True, rx=4))
    o.append(T(100, 120, '20 bits', 13, fill=MUT)); o.append(T(200, 120, '12 bits', 13, fill=MUT))
    o.append(boxt(490, 56, 100, 46, ['f = 5'], ACS, AC, 16, bold_first=True, rx=4))
    o.append(boxt(590, 56, 100, 46, ['d = 4'], NXS, NX, 16, bold_first=True, rx=4))
    # page table
    o.append(T(340, 150, 'page table', 14, bold=True))
    for i, fr in enumerate(['7', '3', '5', '1']):
        y = 164 + i * 36
        hot = i == 2
        o.append(T(274, y + 23, str(i), 13, 'end', LV if hot else MUT, hot))
        o.append(boxt(284, y, 112, 34, [f'frame {fr}' if hot else '…'], ACS if hot else PANEL, AC if hot else L2, 14, bold_first=hot, rx=2))
    o.append(P([(100, 102), (100, 245), (278, 245)], LV, 2.5)); o.append(L(250, 245, 280, 245, LV, 2.5, arrow='l'))
    o.append(P([(396, 245), (510, 245), (510, 106)], AC, 2.5)); o.append(L(510, 140, 510, 106, AC, 2.5, arrow='n'))
    o.append(f'<path d="M240,56 C270,4 590,4 618,52" style="fill:none;stroke:var(--next);stroke-width:2.5;stroke-dasharray:6 4" marker-end="url(#ar-UID-x)"/>')
    o.append(Tb(420, 22, 'offset copied unchanged', 13, fill=NX, bold=True))
    o.append(T(30, 340, '8196 ÷ 4096 = 2 remainder 4, so p = 2, d = 4', 14, 'start'))
    o.append(T(30, 362, 'physical = 5 × 4096 + 4 = 20480 + 4 = 20484', 14, 'start', AC, True))
    o.append(T(690, 340, 'page = 4 KB = 2¹² B, so 12 offset bits', 13, 'end', MUT))
    o.append(T(690, 362, 'and 32 − 12 = 20 page-number bits', 13, 'end', MUT))
    return 378, ''.join(o)
FIG[4] = (f4, 'Logical address 8196 splits into page 2 and offset 4. The page table says page 2 is in frame 5, so the physical address is 5 × 4096 + 4 = 20484; the offset passes through unchanged.',
          'A logical address split into page 2 and offset 4; page 2 indexes the page table to frame 5, which joins the same offset to form physical address 20484.')


# ---- 4.5 two-level page table ----
def f5():
    o = [T(30, 30, 'address split', 13, 'start', MUT, True)]
    for x, w, lab, f, c in ((130, 150, 'p1: 10 bits', ACS, AC), (280, 150, 'p2: 10 bits', NXS, NX), (430, 180, 'offset: 12 bits', PANEL, L2)):
        o.append(boxt(x, 14, w, 34, [lab], f, c, 14, rx=3))
    o.append(T(110, 86, 'outer table', 14, bold=True)); o.append(T(110, 102, '1024 entries = 4 KB', 13, fill=MUT))
    o.append(R(50, 112, 120, 222, PANEL, AC, 6))
    slots = [(0, True), (1, False), (2, False), (3, True), (4, False), (5, False), (6, True), (7, False)]
    for i, used in slots:
        y = 116 + i * 27
        o.append(R(56, y, 108, 23, ACS if used else PANEL, AC if used else LN, 3, 1.5 if used else 1))
        o.append(T(110, y + 16, 'points to inner' if used else 'empty', 13, fill=INK if used else MUT))
    inner = [116, 197, 278]
    for j, (i, _) in enumerate([s for s in slots if s[1]]):
        y = 116 + i * 27 + 11
        o.append(L(164, y, 262, inner[j] + 26, NX, 2, arrow='x'))
        o.append(boxt(266, inner[j], 150, 52, ['inner table', '1024 × 4 B = 4 KB'], NXS, NX, 13, bold_first=True))
    o.append(T(340, 352, 'one inner table per 4 MB region used', 13, fill=MUT))
    o.append(T(570, 120, 'Flat table:', 14, bold=True)); o.append(T(570, 140, '2²⁰ × 4 B = 4 MB', 14))
    o.append(T(570, 196, 'Two-level, 3 regions:', 14, bold=True)); o.append(T(570, 216, '4 KB + 3 × 4 KB = 16 KB', 14, fill=NX, bold=True))
    o.append(T(570, 272, '4 MB ÷ 16 KB', 14)); o.append(T(570, 294, '= 256 times smaller', 15, bold=True, fill=AC))
    return 366, ''.join(o)
FIG[5] = (f5, 'The 20 page-number bits split 10 + 10. The outer table (4 KB) points only to the inner tables the process needs, here 3 of 4 KB each, so 16 KB replaces a flat 4 MB table: 256 times less.',
          'An outer page table with three used entries pointing to three inner tables of 4 KB each, beside the sums 4 MB for a flat table and 16 KB for two levels.')


# ---- 4.6 segmentation lookups ----
def f6():
    cols = [(20, 90, 'segment'), (110, 90, 'base'), (200, 80, 'limit'), (280, 90, 'offset'), (370, 150, 'offset &lt; limit?'), (520, 180, 'result')]
    rows = [('2', '90', '100', '53', '53 &lt; 100 yes', '90 + 53 = 143', True), ('1', '2300', '14', '500', '500 &lt; 14 no', 'trap', False),
            ('0', '219', '600', '1222', '1222 &lt; 600 no', 'trap', False), ('3', '1327', '580', '580', '580 &lt; 580 no', 'trap (one past the end)', False)]
    o = []
    for x, w, h in cols:
        o.append(T(x + w / 2, 34, h, 13, fill=MUT, bold=True))
    o.append(L(20, 44, 700, 44, L2, 1.5))
    for i, (sg, b, lm, off, chk, res, ok) in enumerate(rows):
        y = 52 + i * 44
        o.append(R(20, y, 680, 38, NXS if ok else PANEL, NX if ok else LN, 6, 1.5 if ok else 1))
        for (x, w, _), v in zip(cols, (sg, b, lm, off, chk, res)):
            c = INK
            if v == chk: c = NX if ok else LV
            if v == res: c = AC if ok else LV
            o.append(T(x + w / 2, y + 25, v, 14, fill=c, bold=(v in (sg, res))))
    # memory strip for segment 2
    s, x0 = 3.0, 120
    mx = lambda a: x0 + (a - 60) * s
    o.append(T(30, 268, 'memory', 13, 'start', MUT))
    o.append(R(mx(60), 248, 450, 32, PANEL, L2, 3, 1))
    o.append(R(mx(90), 248, 100 * s, 32, NXS, NX, 3, 2))
    o.append(T(mx(140), 270, 'segment 2', 13, fill=NX, bold=True))
    for a, lab in ((90, 'base 90'), (190, 'end 90 + 100 = 190')):
        o.append(L(mx(a), 282, mx(a), 296, INK, 1.5)); o.append(T(mx(a), 312, lab, 13, fill=MUT))
    o.append(L(mx(143), 236, mx(143), 252, AC, 2, arrow='n')); o.append(T(mx(143), 230, '143', 14, fill=AC, bold=True))
    o.append(T(360, 346, 'Valid offsets run from 0 to limit − 1, so an offset equal to the limit traps.', 14, bold=True))
    return 362, ''.join(o)
FIG[6] = (f6, 'Each lookup checks the offset against its segment\'s limit before adding the base. Only segment 2, offset 53 passes, landing at 143; the other three trap, including offset 580 against limit 580.',
          'A table of four segment lookups with base, limit, offset, the check and the result, above a memory strip showing segment 2 from 90 to 190 with address 143 marked.')


# ---- 4.7 page-fault rate vs effective access time ----
def f7():
    x0, x1, y0, y1 = 90, 680, 60, 300
    fx = lambda p: x0 + p / 5 * (x1 - x0)
    fy = lambda e: y1 - (e - 200) / 40 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 1, 2, 2.5, 3, 4, 5], [200, 210, 220, 230, 240], fx, fy, 'page-fault rate p (× 10⁻⁶)', 'EAT (ns)', lambda v: f'{v:g}')]
    o.append(f'<polygon points="{fx(0):.1f},{fy(200):.1f} {fx(2.5):.1f},{fy(220):.1f} {fx(2.5):.1f},{fy(200):.1f}" style="fill:var(--next-soft)"/>')
    o.append(R(fx(0), fy(220), fx(2.5) - fx(0), fy(200) - fy(220), NXS, 'none', 0, 0))
    o.append(L(x0, fy(220), x1, fy(220), LV, 2, '7 5'))
    o.append(Tb(x1 - 4, fy(220) - 10, 'limit: 1.10 × 200 = 220 ns', 13, 'end', LV, True))
    o.append(P([(fx(0), fy(200)), (fx(5), fy(200 + 7999800 * 5e-6))], AC, 3))
    o.append(L(fx(2.5), fy(220), fx(2.5), y1, INK, 1.5, '4 4'))
    o.append(C(fx(2.5), fy(220), 6, AC))
    o.append(T(fx(1.25), fy(205), 'allowed', 14, fill=NX, bold=True))
    o.append(Tb(fx(2.5) + 12, fy(214), 'p ≤ 20 ÷ 7,999,800 ≈ 2.5 × 10⁻⁶', 14, 'start', AC, True))
    o.append(Tb(fx(2.5) + 12, fy(210), 'about 1 fault per 399,990 references', 13, 'start'))
    o.append(T(fx(0.3), fy(236), 'EAT = 200 + 7,999,800 p', 14, 'start', AC, True))
    return 356, ''.join(o)
FIG[7] = (f7, 'A page fault costs 8 ms against 200 ns for a normal access, so EAT climbs steeply with the fault rate. To stay within 220 ns, at most about one reference in 399,990 may fault.',
          'A straight line of effective access time against page-fault rate, crossing the 220 ns limit at p of about 2.5 millionths.')


# ---- 4.8 FIFO, LRU and OPT on the same string ----
def sim(refs, pol, n=3):
    fr, cols, faults, last, loaded = [None] * n, [], 0, {}, {}
    for t, p in enumerate(refs):
        hit = p in fr
        if not hit:
            faults += 1
            if None in fr: k = fr.index(None)
            elif pol == 'FIFO': k = min(range(n), key=lambda i: loaded[fr[i]])
            elif pol == 'LRU': k = min(range(n), key=lambda i: last[fr[i]])
            else:
                def nxt(q):
                    try: return refs.index(q, t + 1)
                    except ValueError: return 10 ** 6
                k = max(range(n), key=lambda i: nxt(fr[i]))
            fr[k] = p; loaded[p] = t
        last[p] = t
        cols.append((list(fr), hit, p))
    return cols, faults


def f8():
    refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    x0, cw = 150, 46
    o = [T(138, 34, 'reference', 13, 'end', MUT, True)]
    for t, p in enumerate(refs):
        o.append(T(x0 + t * cw + cw / 2, 34, str(p), 15, bold=True))
    for g, pol in enumerate(('FIFO', 'LRU', 'OPT')):
        cols, nf = sim(refs, pol)
        y = 50 + g * 96
        o.append(T(138, y + 30, pol, 15, 'end', bold=True))
        o.append(T(138, y + 50, f'{nf} faults', 13, 'end', AC if pol == 'OPT' else LV, True))
        for t, (fr, hit, p) in enumerate(cols):
            x = x0 + t * cw
            o.append(R(x + 2, y, cw - 4, 72, PANEL if hit else LVS, LN if hit else LV, 4, 1 if hit else 1.5))
            for r, v in enumerate(fr):
                if v is None: continue
                o.append(T(x + cw / 2, y + 19 + r * 21, str(v), 14, fill=(INK if v == p and not hit else MUT) if not hit else MUT, bold=(v == p and not hit)))
            o.append(T(x + cw / 2, y + 88, 'hit' if hit else 'F', 13, fill=NX if hit else LV, bold=True))
    o.append(T(360, 364, 'Frames after each reference; shaded columns are faults. OPT 7 &lt; FIFO 9 &lt; LRU 10.', 14))
    return 378, ''.join(o)
FIG[8] = (f8, 'Three frames, one reference string, three replacement rules. Each column shows the frames after that reference; OPT has 7 faults, FIFO 9 and LRU 10 because LRU evicts 5 just before it returns.',
          'Three grids of 12 columns for FIFO, LRU and OPT showing three frames after each reference, with fault columns shaded: 9, 10 and 7 faults.')


# ---- 4.9 equal vs proportional frame allocation ----
def f9():
    s = 4
    need = [('P1', 10), ('P2', 30), ('P3', 60)]
    o = [T(40, 30, 'Equal: 100 ÷ 3 → 33 frames each', 15, 'start', bold=True), T(400, 30, 'Proportional: 100 × need ÷ 100', 15, 'start', bold=True)]
    for i, (p, n) in enumerate(need):
        y = 60 + i * 74
        # equal
        x = 70
        o.append(T(56, y + 24, p, 14, 'end', bold=True))
        o.append(R(x, y, n * s, 36, ACS, AC, 4))
        o.append(T(x + 6, y + 56, f'needs {n}', 13, 'start', MUT))
        if n < 33:
            o.append(R(x + n * s, y, (33 - n) * s, 36, PANEL, L2, 4, 1.5, '5 4'))
            o.append(T(x + (n + 33) / 2 * s, y + 23, f'{33 - n} idle', 13, fill=MUT, bold=True) if 33 - n > 10 else T(x + 33 * s + 6, y + 23, f'{33 - n} idle', 13, 'start', MUT, True))
        elif n > 33:
            o.append(R(x + 33 * s, y, (n - 33) * s, 36, LVS, LV, 4, 2, '5 4'))
            o.append(T(x + (33 + n) / 2 * s, y + 23, f'{n - 33} short', 13, fill=LV, bold=True))
        o.append(L(x + 33 * s, y - 6, x + 33 * s, y + 42, INK, 2))
        o.append(T(x + 33 * s + 4, y + 56, 'gets 33', 13, 'start'))
        # proportional
        x = 430
        o.append(T(416, y + 24, p, 14, 'end', bold=True))
        o.append(boxt(x, y, n * s, 36, [str(n)], NXS, NX, 13, rx=4))
        if n < 60: o.append(T(x + n * s + 8, y + 23, 'fits exactly', 13, 'start', NX))
    o.append(T(550, 268, 'fits exactly', 13, fill=NX))
    o.append(T(40, 300, 'Equal shares leave P1 23 frames it cannot use while P3 is 27 short (1 frame', 14, 'start'))
    o.append(T(40, 320, 'stays spare). Proportional shares 10, 30 and 60 match each need.', 14, 'start'))
    return 336, ''.join(o)
FIG[9] = (f9, 'Three processes need 10, 30 and 60 pages from 100 frames. Equal shares of 33 waste 23 frames in P1 and leave P3 27 short; proportional shares give each exactly what it needs.',
          'Left, bars of need against an equal share of 33 frames, with 23 idle frames for P1 and 27 missing for P3. Right, proportional bars of 10, 30 and 60 that fit exactly.')


spec = make_spec(FIG)
