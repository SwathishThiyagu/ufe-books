"""Claude's hand-drawn figures for c-coa-u1 (Computer Organization and Architecture, unit 1: basic structure of computers),
one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 1.1 ENIAC against a phone core, on a powers-of-ten ruler ----
def f1():
    x0, s = 110, 45
    X = lambda lg: x0 + (lg + 2) * s
    o = []
    for lg in range(-2, 11, 2):
        o.append(L(X(lg), 50, X(lg), 258, LN, 1, '3 4'))
    rows = [(38, 80, 'Additions per second', (3.70, '5,000'), (9.68, '4.8 × 10⁹'), '× 960,000 (about a million)'),
            (158, 200, 'Additions per joule of energy', (-1.48, '0.033'), (9.38, '2.4 × 10⁹'), '× 72 billion')]
    for ty, y, title, (le, ve), (lp, vp), fac in rows:
        o.append(T(20, ty, title, 15, 'start', bold=True))
        o.append(L(X(-2), y, X(10), y, LN, 1.5))
        o.append(L(X(le) + 11, y, X(lp) - 13, y, AC, 3, arrow='n'))
        o.append(Tb((X(le) + X(lp)) / 2, y - 14, fac, 14, fill=AC, bold=True))
        o.append(C(X(le), y, 9, LV)); o.append(C(X(lp), y, 9, NX))
        o.append(T(X(le), y + 27, 'ENIAC', 14, bold=True, fill=LV)); o.append(T(X(le), y + 44, ve, 13, fill=MUT))
        o.append(T(X(lp), y + 27, 'phone core', 14, bold=True, fill=NX)); o.append(T(X(lp), y + 44, vp, 13, fill=MUT))
    o.append(L(X(-2), 268, X(10), 268, L2, 1.5))
    labs = {-2: '0.01', 0: '1', 2: '100', 4: '10⁴', 6: '10⁶', 8: '10⁸', 10: '10¹⁰'}
    for lg, lab in labs.items():
        o.append(L(X(lg), 268, X(lg), 274, L2, 1.5)); o.append(T(X(lg), 290, lab, 13, fill=MUT))
    o.append(T(360, 312, 'each grid step is 100 times the one before', 13, fill=MUT))
    o.append(T(360, 342, 'The phone core is a million times faster, and the energy gain is bigger still.', 14, bold=True))
    return 356, ''.join(o)
FIG[1] = (f1, 'ENIAC did 5,000 additions per second at 150 kW; one 2.4 GHz phone core does 4.8 × 10⁹ at 2 W. On a powers-of-ten scale the phone is about a million times faster and about 72 billion times more additions per joule.',
          'Two rows on a powers-of-ten scale: additions per second (ENIAC 5,000, phone 4.8 billion) and additions per joule (ENIAC 0.033, phone 2.4 billion), with an arrow giving the factor between them.')


# ---- 1.2 the five units adding 78 + 64 ----
def f2():
    o = [boxt(20, 96, 120, 64, ['Input', 'keys: 78, 64'], PANEL, AC, 14, bold_first=True)]
    o.append(L(142, 128, 187, 128, AC, 2, arrow='n'))
    o.append(R(190, 40, 170, 140, PANEL, AC))
    o.append(T(275, 62, 'Memory', 15, bold=True))
    for i, (a, v) in enumerate((('1000', '78'), ('1004', '64'), ('1008', '142'))):
        hot = i == 2
        o.append(R(205, 76 + i * 32 + 2, 140, 26, ACS if hot else FIGBG, AC if hot else L2, 5, 1.5))
        o.append(TM(275, 76 + i * 32 + 20, f'{a}:  {v}', 14, bold=hot))
    o.append(L(275, 182, 275, 203, AC, 2, arrow='n'))
    o.append(boxt(190, 206, 170, 52, ['Output', 'display: 142'], PANEL, AC, 14, bold_first=True))
    o.append(R(410, 40, 290, 190, PANEL, L2, 10, 1.5, '6 4'))
    o.append(T(555, 58, 'Processor (CPU)', 13, fill=MUT, bold=True))
    o.append(boxt(425, 66, 120, 92, ['Registers', 'R1 = 78', 'R2 = 64'], ACS, AC, 14, bold_first=True))
    o.append(boxt(575, 66, 110, 92, ['ALU', '78 + 64', '= 142'], NXS, NX, 14, bold_first=True))
    o.append(L(547, 98, 572, 98, AC, 2, arrow='n'))
    o.append(L(573, 128, 549, 128, NX, 2, arrow='x'))
    o.append(boxt(425, 170, 260, 46, ['Control unit: signals every step'], PANEL, AC, 14))
    o.append(L(362, 95, 422, 95, AC, 2, arrow='n'))
    o.append(T(392, 86, 'load', 13, fill=MUT))
    o.append(L(422, 150, 362, 150, AC, 2, arrow='n'))
    o.append(T(392, 141, 'store', 13, fill=MUT))
    o.append(T(20, 290, 'Time for the addition step (memory access 50 ns, register or ALU 1 ns)', 14, 'start', bold=True))
    o.append(T(170, 324, 'A: marks in memory', 14, 'end'))
    o.append(R(180, 305, 151 * 3, 28, LVS, LV, 4))
    o.append(T(640, 324, '151 ns', 14, 'start', LV, True))
    o.append(T(170, 364, 'B: marks in registers', 14, 'end'))
    o.append(R(180, 345, 12, 28, NXS, NX, 3))
    o.append(T(200, 364, '4 ns', 14, 'start', NX, True))
    o.append(T(360, 400, '151 ÷ 4 ≈ 38: with the marks in registers the step is about 38 times faster.', 14, bold=True))
    return 414, ''.join(o)
FIG[2] = (f2, 'The five units adding the marks 78 and 64: input puts them in memory, the registers and ALU make 142, and the total goes back to memory and out to the display. Fetching the marks from memory makes the step take 151 ns; with them already in registers it takes 4 ns.',
          'Block diagram: input, memory with addresses 1000, 1004 and 1008, the processor with registers, ALU and control unit, and output; below, a long 151 ns bar and a short 4 ns bar.')


# ---- 1.3 bus cycles for 10 instructions, 3 of them loads or stores ----
def f3():
    x0, s, h = 150, 36, 36
    o = [T(20, 24, 'Ten instructions; numbers 3, 6 and 9 are loads or stores', 15, 'start', bold=True),
         T(20, 44, 'F = instruction fetch, D = data access; each slot is one 5 ns bus cycle', 13, 'start', MUT)]
    def slot(i, y, lab, data):
        return boxt(x0 + i * s + 1, y, s - 2, h, [lab], LVS if data else ACS, LV if data else AC, 13, rx=4)
    seq = []
    for n in range(1, 11):
        seq.append(('F' + str(n), False))
        if n in (3, 6, 9): seq.append(('D' + str(n), True))
    o += [T(140, 76, 'Von Neumann', 14, 'end', bold=True), T(140, 92, 'one shared bus', 13, 'end', MUT)]
    for i, (lab, d) in enumerate(seq):
        o.append(slot(i, 60, lab, d))
    o.append(T(x0 + 13 * s + 8, 83, '13 cycles', 14, 'start', LV, True))
    o.append(T(20, 130, 'Harvard', 14, 'start', bold=True))
    o.append(T(140, 163, 'instruction bus', 13, 'end'))
    o.append(T(140, 209, 'data bus', 13, 'end'))
    o.append(L(x0, 222, x0 + 10 * s, 222, LN, 1))
    for n in range(10):
        o.append(slot(n, 140, 'F' + str(n + 1), False))
    for n in (3, 6, 9):
        o.append(slot(n, 186, 'D' + str(n), True))
    o.append(L(x0 + 10 * s, 136, x0 + 10 * s, 226, L2, 1.5, '4 4'))
    o.append(T(x0 + 10 * s + 8, 186, '10 cycles', 14, 'start', NX, True))
    o.append(T(20, 262, 'Whole program, 2 × 10⁶ instructions: von Neumann 2.6 × 10⁶ cycles × 5 ns = 13 ms;', 14, 'start'))
    o.append(T(20, 284, 'Harvard 2 × 10⁶ cycles × 5 ns = 10 ms. Speedup 13 ÷ 10 = 1.3.', 14, 'start', bold=True))
    return 298, ''.join(o)
FIG[3] = (f3, 'With one shared bus, the 3 data accesses must wait their turn, so 10 instructions take 13 bus cycles. With separate instruction and data buses they overlap the fetches and the same work takes 10 cycles, a speedup of 1.3.',
          'Two timelines of bus slots: the von Neumann bus has 13 slots in a row (10 fetches and 3 data accesses); the Harvard design has 10 fetch slots on one bus and 3 data slots on a second bus at the same time.')


# ---- 1.4 clock cycles of the three-instruction program ----
def f4():
    x0, s = 170, 50
    o = [R(20, 18, 22, 16, LVS, LV, 3, 1.5), T(50, 31, 'memory access (4 cycles)', 13, 'start'),
         R(250, 18, 22, 16, ACS, AC, 3, 1.5), T(280, 31, 'decode, ALU or register write (1 cycle)', 13, 'start')]
    rows = [('Load R2,5000', '10 cycles', [('fetch', 4, 1), ('decode', 1, 0), ('read M[5000]', 4, 1), ('R2=25', 1, 0)]),
            ('Add R4,R2,R3', '7 cycles', [('fetch', 4, 1), ('decode', 1, 0), ('25+17', 1, 0), ('R4=42', 1, 0)]),
            ('Store R4,5004', '9 cycles', [('fetch', 4, 1), ('decode', 1, 0), ('write M[5004]', 4, 1)])]
    for r, (ins, tot, segs) in enumerate(rows):
        y = 60 + r * 60
        o.append(TM(160, y + 17, ins, 13, 'end', bold=True))
        o.append(T(160, y + 35, tot, 13, 'end', MUT))
        c = 0
        for lab, n, mem in segs:
            o.append(boxt(x0 + c * s + 1, y, n * s - 2, 40, [lab], LVS if mem else ACS, LV if mem else AC, 13, rx=4))
            c += n
    o.append(xaxis(x0, x0 + 10 * s, 248, list(range(0, 11)), lambda v: x0 + v * s, 'clock cycles (1 ns each at 1 GHz)'))
    o.append(T(20, 318, 'Total: 10 + 7 + 9 = 26 cycles = 26 ns.', 14, 'start'))
    o.append(T(20, 340, 'Memory: 5 accesses × 4 = 20 cycles, so 20 ÷ 26 ≈ 77% of the time is spent waiting on memory.', 14, 'start', bold=True))
    return 354, ''.join(o)
FIG[4] = (f4, 'The cycles of the three instructions, each starting with a 4-cycle fetch. Of the 26 cycles in all, 20 are memory accesses, so about 77% of the time goes to memory.',
          'Three rows of coloured blocks, one per instruction: Load takes 10 cycles, Add 7 and Store 9; the 4-cycle memory blocks are much longer than the 1-cycle decode, ALU and register-write blocks.')


# ---- 1.5 the system bus of the worked example ----
def f5():
    o = [boxt(20, 60, 130, 200, ['Processor'], PANEL, AC, 15, bold_first=True),
         boxt(570, 60, 130, 200, ['Memory', 'byte-addressable'], PANEL, AC, 14, bold_first=True)]
    buses = [(105, 'address bus: 32 lines', '2³² bytes = 4 GB can be reached', False),
             (165, 'data bus: 64 lines', '64 ÷ 8 = 8 bytes per transfer', True),
             (225, 'control bus: Read, Write, clock', 'clock 200 MHz, one tick every 5 ns', True)]
    for y, top, bot, both in buses:
        o.append(f'<line x1="156" y1="{y}" x2="564" y2="{y}" style="stroke:var(--accent);stroke-width:3" marker-end="url(#ar-UID-n)"'
                 + (' marker-start="url(#ar-UID-n)"' if both else '') + '/>')
        o.append(T(360, y - 10, top, 14, bold=True))
        o.append(T(360, y + 22, bot, 13, fill=MUT))
    o.append(T(20, 292, 'One read takes 4 clock cycles of 5 ns', 14, 'start', bold=True))
    for r, (lab, cells, res) in enumerate((('no wait', ['T1', 'T2', 'T3', 'T4'], '20 ns: 8 B ÷ 20 ns = 400 MB/s'),
                                           ('2 wait states', ['T1', 'T2', 'Tw', 'Tw', 'T3', 'T4'], '30 ns: 8 B ÷ 30 ns ≈ 266.7 MB/s'))):
        y = 306 + r * 44
        o.append(T(140, y + 21, lab, 13, 'end'))
        for i, c in enumerate(cells):
            w = c == 'Tw'
            o.append(boxt(150 + i * 48 + 1, y, 46, 32, [c], LVS if w else ACS, LV if w else AC, 13, rx=4))
        o.append(T(150 + len(cells) * 48 + 12, y + 21, res, 14, 'start', LV if r else AC, True))
    o.append(T(20, 412, 'A 4 KB block is 4,096 ÷ 8 = 512 reads: 512 × 20 ns = 10.24 µs, or 15.36 µs with wait states.', 14, 'start'))
    return 386, '<g transform="translate(0,-40)">' + ''.join(o) + '</g>'
FIG[5] = (f5, 'The three groups of bus lines with the worked example\'s numbers: 32 address lines reach 4 GB, 64 data lines move 8 bytes at a time, and the 200 MHz clock makes a 4-cycle read 20 ns. Two wait states stretch the read to 30 ns and cut the bandwidth from 400 to about 267 MB/s.',
          'Processor and memory joined by three horizontal buses labelled 32 address lines, 64 data lines and control; below, a read of four 5 ns clock slots and a longer read with two extra wait slots.')


# ---- 1.6 where the cycles per instruction come from ----
def f6():
    x0, s = 170, 250
    fx = lambda v: x0 + v * s
    def bar(y, parts):
        o, c = [], 0
        for lab, v, f, st in parts:
            o.append(boxt(fx(c) + 1, y, v * s - 2, 44, [lab], f, st, 13, rx=4)); c += v
        return ''.join(o), c
    b1, t1 = bar(70, [('ALU 0.5', 0.5, ACS, AC), ('load/store 0.3 × 3 = 0.9', 0.9, LVS, LV), ('branch 0.4', 0.4, NXS, NX)])
    b2, t2 = bar(170, [('ALU 0.5', 0.5, ACS, AC), ('load/store 0.6', 0.6, LVS, LV), ('branch 0.4', 0.4, NXS, NX)])
    o = [T(20, 34, 'Each kind of instruction adds (its share) × (its CPI) to the average', 15, 'start', bold=True),
         T(160, 90, 'Before', 14, 'end', bold=True), T(160, 107, 'loads CPI 3', 13, 'end', MUT),
         T(160, 190, 'Better cache', 14, 'end', bold=True), T(160, 207, 'loads CPI 2', 13, 'end', MUT), b1, b2]
    o.append(T(fx(t1) + 8, 97, 'CPI 1.8', 15, 'start', bold=True))
    o.append(R(fx(t2) + 1, 170, 0.3 * s - 2, 44, 'none', L2, 4, 1.5, '5 4'))
    o.append(T(fx(t2 + 0.15), 197, 'saved', 13, fill=MUT))
    o.append(T(fx(1.8) + 8, 197, 'CPI 1.5', 15, 'start', bold=True))
    o.append(xaxis(x0, fx(2), 240, [0, 0.5, 1, 1.5, 2], fx, 'average cycles per instruction (CPI)'))
    o.append(T(20, 316, 'CPU time = 5 × 10⁸ instructions × CPI ÷ 2 GHz: 1.8 gives 0.45 s, 1.5 gives 0.375 s.', 14, 'start'))
    o.append(T(20, 338, 'Speedup = 0.45 ÷ 0.375 = 1.2', 14, 'start', bold=True))
    return 352, ''.join(o)
FIG[6] = (f6, 'The average CPI is built from each instruction kind\'s share times its CPI: 0.5 + 0.9 + 0.4 = 1.8. A better cache cuts the load/store part to 0.6, the CPI falls to 1.5 and the program runs 1.2 times faster.',
          'Two stacked bars: the first is 0.5 for ALU, 0.9 for loads and stores and 0.4 for branches, total 1.8; the second has a 0.6 load/store part, total 1.5, with the saved 0.3 shown dashed.')


# ---- 1.7 power and throughput of designs A, B and C ----
def f7():
    px, ps = 210, 2.0
    tx, ts = 492, 100
    rows = [('A', '1 core, 3.0 GHz, 1.2 V', 86.4, '86.4 W', 1.0, '1.0'), ('B', '1 core, 2.4 GHz, 1.0 V', 48, '48 W', 0.8, '0.8'),
            ('C', 'two B cores', 96, '96 W', 1.6, '1.6')]
    o = [T(px, 40, 'Dynamic power (W)', 14, 'start', bold=True), T(tx, 40, 'Throughput (A = 1)', 14, 'start', bold=True)]
    for i, (n, d, p, pl, t, tl) in enumerate(rows):
        y = 62 + i * 68
        o.append(T(20, y + 18, 'Design ' + n, 15, 'start', bold=True))
        o.append(T(20, y + 37, d, 13, 'start', MUT))
        o.append(R(px, y + 6, p * ps, 30, LVS, LV, 4))
        o.append(T(px + p * ps + 8, y + 26, pl, 14, 'start', LV, True))
        o.append(R(tx, y + 6, t * ts, 30, NXS, NX, 4))
        o.append(T(tx + t * ts + 8, y + 26, tl, 14, 'start', NX, True))
    o.append(L(px, 52, px, 270, L2, 1.5)); o.append(L(tx, 52, tx, 270, L2, 1.5))
    o.append(T(20, 298, 'P = ½ C V² f.  B: (1.0 ÷ 1.2)² × (2.4 ÷ 3.0) = 0.56, so 86.4 W falls to 48 W.', 14, 'start'))
    o.append(T(20, 320, 'C: 1.6 times A\'s throughput for 96 ÷ 86.4 = 1.11 times the power.', 14, 'start', bold=True))
    return 334, ''.join(o)
FIG[7] = (f7, 'Lowering the voltage from 1.2 V to 1.0 V and the clock to 2.4 GHz cuts the power from 86.4 W to 48 W. Two such cores (C) give 1.6 times A\'s throughput for only 11% more power, if the program can use both.',
          'Paired bars for designs A, B and C: power 86.4, 48 and 96 W, and throughput 1.0, 0.8 and 1.6 times design A.')


spec = make_spec(FIG)
