"""Claude's hand-drawn figures for c-coa-u5 (Computer Organization and Architecture, unit 5: pipelining and parallel
processing), one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 5.1 unequal stages set the clock ----
def f1():
    x0, s = 150, 1.35
    fx = lambda ps: x0 + ps * s
    st = [60, 50, 90, 80]
    o = [T(140, 66, 'No pipeline', 14, 'end', bold=True), T(140, 84, '280 ps each', 13, 'end', MUT)]
    c = 0
    for i, w in enumerate(st):
        o.append(boxt(fx(c) + 1, 50, w * s - 2, 40, [f'S{i + 1} {w}'], ACS, AC, 13, rx=4)); c += w
    o += [T(140, 146, 'Pipeline', 14, 'end', bold=True), T(140, 164, 'clock 100 ps', 13, 'end', MUT)]
    for i, w in enumerate(st):
        a = i * 100
        o.append(boxt(fx(a) + 1, 130, w * s - 2, 40, [f'S{i + 1} {w}'], ACS, AC, 13, rx=4))
        if w < 90: o.append(R(fx(a + w), 130, (90 - w) * s, 40, PANEL, L2, 3, 1.2, '4 3'))
        o.append(R(fx(a + 90), 128, 10 * s, 44, L2, L2, 2, 1))
    o.append(Tb(fx(95), 120, 'register +10 ps', 13, fill=MUT))
    o.append(T(fx(100 + 70), 190, 'S2 idle 40 ps', 13, fill=LV, bold=True))
    o.append(xaxis(x0, fx(400), 206, [0, 100, 200, 300, 400], fx, 'time (ps)'))
    o.append(T(20, 278, 'Clock = slowest stage + register = 90 + 10 = 100 ps.', 14, 'start'))
    o.append(T(20, 300, '1000 instructions: 280 ns without the pipeline, (4 + 999) × 100 ps = 100.3 ns with it.', 14, 'start'))
    o.append(T(20, 324, 'Speedup 280 ÷ 100.3 = 2.79, not 4: the 90 ps stage sets the clock for every stage.', 14, 'start', bold=True))
    return 338, ''.join(o)
FIG[1] = (f1, 'Cut into four stages of 60, 50, 90 and 80 ps, every stage must wait for the slowest (90 ps) plus a 10 ps register, so the clock is 100 ps. 1000 instructions then take 100.3 ns instead of 280 ns, a speedup of 2.79 rather than 4.',
          'One 280 ps bar of four stages, and below it four 100 ps pipeline slots, each holding one stage, its idle time to 90 ps and a thin 10 ps register.')


# ---- 5.2 the pipeline registers at the end of cycle 4 ----
def f2():
    o = [T(20, 24, 'End of cycle 4: what each pipeline register holds', 15, 'start', bold=True)]
    regs = [('IF/ID', ['or $13,$6,$7', 'PC + 4 = 416']), ('ID/EX', ['and $12,$4,$5', 'read 15 and 6', 'rd = 12', 'control EX, M, WB']),
            ('EX/MEM', ['sub $11,$2,$3', 'ALU 50 − 8 = 42', 'dest = 11', 'control M, WB']),
            ('MEM/WB', ['lw $10,20($1)', 'data = 77', 'address 1020', 'dest = 10', 'control WB'])]
    for i, (n, lines) in enumerate(regs):
        x = 30 + i * 172
        o.append(R(x, 40, 150, 150, ACS if i == 3 else PANEL, AC, 8))
        o.append(T(x + 75, 62, n, 14, bold=True))
        o.append(TM(x + 75, 86, lines[0], 13, fill=AC, bold=True))
        for j, s in enumerate(lines[1:]):
            o.append(T(x + 75, 110 + j * 20, s, 13, fill=MUT if s.startswith('control') else INK))
    o.append(T(30, 214, 'youngest', 13, 'start', MUT)); o.append(T(694, 214, 'oldest', 13, 'end', MUT))
    o.append(L(100, 210, 630, 210, L2, 1.5, arrow='m'))
    o.append(Tb(365, 214, 'instructions move this way', 13, fill=MUT))
    o.append(T(20, 250, 'Register writes, one per cycle from cycle 5', 14, 'start', bold=True))
    for i, (c, v) in enumerate((('cycle 5', '$10 = 77'), ('cycle 6', '$11 = 42'), ('cycle 7', '$12 = 6'), ('cycle 8', '$13 = 13'), ('cycle 9', '$14 = 8'))):
        o.append(boxt(20 + i * 138, 262, 128, 44, [c, v], NXS, NX, 13))
    o.append(T(20, 334, 'Five instructions finish in 5 + 5 − 1 = 9 cycles; none uses another\'s result, so there is no hazard.', 14, 'start'))
    return 348, ''.join(o)
FIG[2] = (f2, 'At the end of cycle 4 each pipeline register holds a different instruction with the data and control it still needs: lw has its loaded 77, sub its result 42. From cycle 5 one register is written per cycle.',
          'Four boxes for the IF/ID, ID/EX, EX/MEM and MEM/WB registers holding or, and, sub and lw with their fields; below, five chips for the register writes in cycles 5 to 9.')


# ---- 5.3 the same code without and with forwarding ----
def f3():
    x0, cw = 162, 48
    names = ['sub $2,$1,$3', 'and $12,$2,$5', 'or $13,$6,$2', 'add $14,$2,$2', 'sw $15,100($2)']
    st = ['IF', 'ID', 'EX', 'MEM', 'WB']
    def diagram(y0, title, rows, ncyc, extra='', hot=()):
        o = [T(20, y0, title, 14, 'start', bold=True)]
        for c in range(ncyc):
            o.append(T(x0 + c * cw + cw / 2, y0 + 22, str(c + 1), 13, fill=MUT))
        for r, cells in enumerate(rows):
            y = y0 + 30 + r * 26
            o.append(TM(20, y + 16, names[r], 13, 'start'))
            for c, lab, stall in cells:
                f, s_ = (LVS, LV) if stall else ((NXS, NX) if (r, c) in hot else ((ACS, AC) if r == 0 else (PANEL, AC)))
                o.append(R(x0 + c * cw + 1, y, cw - 2, 22, f, s_, 3, 1.3, '4 3' if stall else None))
                o.append(T(x0 + c * cw + cw / 2, y + 16, lab, 13, fill=LV if stall else INK))
        return ''.join(o) + extra
    plain = lambda start: [(start + i, s, False) for i, s in enumerate(st)]
    no_fw = [plain(0),
             [(1, 'IF', False), (2, 'ID', True), (3, 'ID', True), (4, 'ID', False), (5, 'EX', False), (6, 'MEM', False), (7, 'WB', False)],
             [(2, 'IF', False), (3, 'IF', True), (4, 'IF', True), (5, 'ID', False), (6, 'EX', False), (7, 'MEM', False), (8, 'WB', False)],
             plain(5), plain(6)]
    o = [diagram(24, 'Without forwarding: and waits for sub to write $2, so 2 stalls and 11 cycles', no_fw, 11)]
    y2 = 214
    o.append(diagram(y2, 'With forwarding: no stalls, 9 cycles', [plain(i) for i in range(5)], 9, hot={(1, 3), (2, 4)}))
    for r, v in ((0, '$2 = 18'), (1, '= 2'), (2, '= 23'), (3, '= 36'), (4, 'M[118] = 99')):
        o.append(T(x0 + 9 * cw + 8, y2 + 30 + r * 26 + 16, v, 13, 'start', NX if r else AC, True))
    o.append(T(20, 400, 'Green: $2 = 18 is forwarded from EX/MEM into and\'s EX (cycle 4) and from MEM/WB into or\'s EX (cycle 5).', 13, 'start', MUT))
    o.append(T(20, 424, 'Forwarding saves the 2 stalls: speedup 11 ÷ 9 = 1.22.', 14, 'start', bold=True))
    return 438, ''.join(o)
FIG[3] = (f3, 'Five instructions that all read $2 from sub. Without forwarding, and must wait in ID until sub writes $2 (2 stalls, 11 cycles); with forwarding the value 18 is passed straight to the ALU and the code takes 9 cycles.',
          'Two pipeline diagrams of the same five instructions: the first has two dashed stall cycles and ends in cycle 11, the second has none, with forwarding arrows from sub to and and or, and ends in cycle 9.')


# ---- 5.4 branch CPI and the loop predictor ----
def f4():
    x0, s = 240, 260
    fx = lambda v: x0 + v * s
    rows = [('stall on every branch', '1 + 0.20 × 3', 0.60), ('predict not taken, resolve in MEM', '1 + 0.20 × 0.6 × 3', 0.36),
            ('predict not taken, resolve in ID', '1 + 0.20 × 0.6 × 1', 0.12), ('2-bit predictor 90%, with BTB', '1 + 0.20 × 0.1 × 1', 0.02)]
    o = [T(20, 26, 'CPI with 20% branches, 60% of them taken', 15, 'start', bold=True)]
    for r, (n, f, p) in enumerate(rows):
        y = 44 + r * 46
        o.append(T(20, y + 14, n, 13, 'start', bold=True)); o.append(T(20, y + 31, f, 13, 'start', MUT))
        o.append(boxt(x0, y + 2, s - 1, 32, ['base CPI 1'] if r == 0 else [''], PANEL, L2, 13, rx=4))
        o.append(R(fx(1), y + 2, max(p * s, 3), 32, LVS, LV, 3))
        o.append(T(fx(1 + p) + 8, y + 24, f'{1 + p:.2f}', 15, 'start', LV if r == 0 else INK, True))
    o.append(T(20, 246, 'Speedup of the predictor over stalling: 1.60 ÷ 1.02 = 1.57', 14, 'start', bold=True))
    o.append(T(20, 292, 'Loop branch T T T N T T T N: 1-bit against 2-bit prediction', 15, 'start', bold=True))
    out = 'TTTNTTTN'
    preds = [('outcome', out, None), ('1-bit predicts', 'TTTTNTTT', '5 of 8'), ('2-bit predicts', 'TTTTTTTT', '6 of 8')]
    for r, (lab, seq, acc) in enumerate(preds):
        y = 306 + r * 38
        o.append(T(220, y + 20, lab, 13, 'end', bold=True))
        for i, ch in enumerate(seq):
            bad = acc is not None and ch != out[i]
            o.append(R(x0 + i * 52 + 2, y, 48, 30, LVS if bad else (ACS if acc is None else PANEL), LV if bad else (AC if acc is None else L2), 4, 1.5))
            o.append(TM(x0 + i * 52 + 26, y + 20, ch + (' ✗' if bad else ''), 14, fill=LV if bad else INK, bold=True))
        if acc: o.append(T(x0 + 8 * 52 + 10, y + 20, acc, 13, 'start', bold=True))
    o.append(T(20, 438, 'At the exit the 2-bit counter only drops from 11 to 10, which still predicts T, so re-entry is right.', 13, 'start', MUT))
    return 452, ''.join(o)
FIG[4] = (f4, 'Each branch strategy adds less to the base CPI of 1: stalling costs 0.60, a 90% predictor only 0.02, a speedup of 1.57. On a loop branch the 2-bit predictor misses only the exits (6 of 8 right) where the 1-bit one also misses each re-entry.',
          'Four bars of CPI 1.60, 1.36, 1.12 and 1.02 with the branch penalty part shaded; below, a row of branch outcomes T T T N T T T N with the 1-bit and 2-bit predictions and their wrong guesses marked.')


# ---- 5.5 precise exception on overflow ----
def f5():
    o = [T(20, 26, 'Cycle 6: add overflows in EX', 15, 'start', bold=True),
         T(20, 46, '7FFF FFFF + 1 = 8000 0000 hex: two positive operands give a negative result', 13, 'start', MUT)]
    stages = [('IF', '54', 'lw $16,50($7)', 'flushed'), ('ID', '50', 'slt $15,$6,$7', 'flushed'), ('EX', '4C', 'add $1,$2,$1', 'overflow: flushed'),
              ('MEM', '48', 'or $13,$2,$6', 'completes'), ('WB', '44', 'and $12,$2,$5', 'completes')]
    for i, (sname, a, ins, stt) in enumerate(stages):
        x = 18 + i * 140
        done = stt == 'completes'
        fault = i == 2
        o.append(T(x + 65, 74, sname, 14, fill=MUT, bold=True))
        o.append(R(x, 82, 130, 60, NXS if done else LVS, NX if done else LV, 6, 2.5 if fault else 1.5, None if (done or fault) else '5 4'))
        o.append(TM(x + 65, 104, a, 13, fill=MUT))
        o.append(TM(x + 65, 126, ins, 13, bold=True))
        o.append(T(x + 65, 162, stt, 13, fill=NX if done else LV, bold=True))
    o.append(T(18, 190, 'youngest', 13, 'start', MUT)); o.append(T(702, 190, 'oldest', 13, 'end', MUT))
    o.append(L(90, 186, 640, 186, L2, 1.5, arrow='m'))
    for i, (n, v) in enumerate((('EPC', '0000 004C'), ('Cause', '12 (overflow)'), ('PC', '8000 0180'), ('$1', 'stays 1'))):
        o.append(boxt(18 + i * 174, 210, 164, 50, [n, v], ACS, AC, 14, bold_first=True))
    o.append(T(20, 290, 'sub (40) already finished in cycle 5; and and or finish normally.', 14, 'start'))
    o.append(T(20, 312, 'In cycle 7 the processor fetches the handler\'s first instruction from 8000 0180.', 14, 'start'))
    return 326, ''.join(o)
FIG[5] = (f5, 'When add overflows in cycle 6, the two older instructions (or, and) complete and add with the two younger ones is flushed, so $1 keeps its old value. EPC records 4C, Cause 12, and PC jumps to the handler at 8000 0180.',
          'Five stage boxes IF to WB in cycle 6 holding lw, slt, add, or and and; the first three are marked flushed, the last two complete; below, EPC 0000 004C, Cause 12, PC 8000 0180 and $1 unchanged.')


# ---- 5.6 two-issue schedules, rolled and unrolled ----
def f6():
    cw, rh = 152, 28
    def grid(x, title, rows):
        o = [T(x, 28, title, 14, 'start', bold=True), T(x + 18 + cw / 2, 52, 'ALU or branch', 13, fill=MUT), T(x + 18 + cw * 1.5, 52, 'load or store', 13, fill=MUT)]
        for r, (a, b) in enumerate(rows):
            y = 60 + r * rh
            o.append(T(x + 10, y + 18, str(r + 1), 13, fill=MUT))
            for c, s in enumerate((a, b)):
                xx = x + 18 + c * cw
                o.append(R(xx + 1, y + 1, cw - 2, rh - 3, (ACS if c == 0 else NXS) if s else PANEL, (AC if c == 0 else NX) if s else LN, 3, 1.2, None if s else '4 3'))
                if s: o.append(TM(xx + cw / 2, y + 18, s, 13))
        return ''.join(o)
    rolled = [('addi $s1,$s1,-4', 'lw $t0,0($s1)'), ('', ''), ('addu $t0,$t0,$s2', ''), ('bne $s1,$zero,L', 'sw $t0,4($s1)')]
    unrolled = [('addi $s1,$s1,-16', 'lw $t0,0($s1)'), ('', 'lw $t1,12($s1)'), ('addu $t0,$t0,$s2', 'lw $t2,8($s1)'),
                ('addu $t1,$t1,$s2', 'lw $t3,4($s1)'), ('addu $t2,$t2,$s2', 'sw $t0,16($s1)'), ('addu $t3,$t3,$s2', 'sw $t1,12($s1)'),
                ('', 'sw $t2,8($s1)'), ('bne $s1,$zero,L', 'sw $t3,4($s1)')]
    o = [grid(14, 'Rolled: 5 instructions in 4 cycles', rolled), grid(372, 'Unrolled 4 times: 14 in 8 cycles', unrolled)]
    o.append(T(14, 196, 'IPC = 5 ÷ 4 = 1.25', 14, 'start', bold=True))
    o.append(T(14, 218, '1000 passes × 4', 14, 'start'))
    o.append(T(14, 240, '= 4000 cycles', 14, 'start', LV, True))
    o.append(T(20, 316, 'Unrolled: IPC = 14 ÷ 8 = 1.75, and 250 passes × 8 = 2000 cycles, twice as fast.', 14, 'start', bold=True))
    o.append(T(20, 338, 'Dashed slots are wasted; unrolling with four registers ($t0 to $t3) fills most of them.', 13, 'start', MUT))
    return 352, ''.join(o)
FIG[6] = (f6, 'The bonus loop on a two-issue processor: rolled, the load-to-use wait leaves 3 of 8 slots empty (IPC 1.25, 4000 cycles); unrolled four times, 14 instructions fill 14 of 16 slots (IPC 1.75, 2000 cycles).',
          'Two issue-slot grids with an ALU column and a load/store column: the rolled loop in 4 cycles with three empty slots, and the four-times-unrolled loop in 8 cycles with two empty slots.')


# ---- 5.7 SIMD speedup and divergence ----
def f7():
    x0 = 130
    o = [T(20, 24, 'C[i] = A[i] + B[i] for 1024 floats, one instruction per cycle at 3 GHz', 15, 'start', bold=True)]
    s = 560 / 6144
    o.append(T(120, 62, 'scalar', 14, 'end', bold=True))
    o.append(boxt(x0, 40, 6144 * s, 34, ['6144 instructions, 2.05 µs'], LVS, LV, 13))
    o.append(T(120, 108, 'AVX, 8 lanes', 14, 'end', bold=True))
    o.append(R(x0, 86, 768 * s, 34, NXS, NX, 5))
    o.append(T(x0 + 768 * s + 10, 108, '768 instructions, 0.256 µs: 8 times faster', 14, 'start', NX, True))
    o.append(T(20, 164, 'An if-else splits the lanes: SIMD runs both paths, one after the other', 15, 'start', bold=True))
    cs = 50
    fx = lambda c: x0 + c * cs
    o.append(T(fx(2), 188, 'if path: 4 cycles', 13, fill=AC, bold=True))
    o.append(T(fx(7), 188, 'else path: 6 cycles', 13, fill=NX, bold=True))
    for i in range(8):
        y = 196 + i * 20
        o.append(T(120, y + 13, f'lane {i + 1}', 13, 'end', MUT))
        first = i < 4
        o.append(R(fx(0), y, 4 * cs - 2, 16, ACS if first else PANEL, AC if first else LN, 3, 1.2, None if first else '4 3'))
        o.append(R(fx(4), y, 6 * cs, 16, PANEL if first else NXS, LN if first else NX, 3, 1.2, '4 3' if first else None))
    o.append(xaxis(x0, fx(10), 364, [0, 2, 4, 6, 8, 10], fx, 'cycles'))
    o.append(T(20, 436, 'Each lane is busy 4 or 6 of the 10 cycles: on average 5 ÷ 10 = 50% lane efficiency.', 14, 'start', bold=True))
    return 450, ''.join(o)
FIG[7] = (f7, 'With 8 floats per instruction, the AVX loop needs 768 instructions instead of 6144, 8 times fewer. When an if-else splits the lanes, all lanes step through both paths (10 cycles) while each does useful work for only 4 or 6, so half the lane time is wasted.',
          'Two bars, 6144 scalar instructions and 768 AVX instructions; below, eight lane rows over 10 cycles, lanes 1 to 4 busy for the first 4 cycles and lanes 5 to 8 busy for the last 6, idle otherwise.')


# ---- 5.8 DAXPY timing on the vector processor ----
def f8():
    x0, s = 40, 2.6
    o = [T(20, 24, 'One strip of 64 elements: 3 convoys, each = start-up + 64 cycles', 15, 'start', bold=True)]
    segs = [('12 + 7', 19, 0), ('LV, MULVS.D: 64', 64, 1), ('12 + 6', 18, 0), ('LV, ADDVV.D: 64', 64, 1), ('12', 12, 0), ('SV: 64', 64, 1)]
    c = 0
    for lab, n, work in segs:
        o.append(boxt(x0 + c * s + 1, 38, n * s - 2, 44, [lab], ACS if work else LVS, AC if work else LV, 13, rx=4, dash=None if work else '4 3'))
        c += n
    o.append(brace(x0, x0 + c * s, 92, INK))
    o.append(T(x0 + c * s / 2, 118, '49 + 3 × 64 = 241 cycles', 14, bold=True))
    o.append(R(20, 132, 22, 16, LVS, LV, 3, 1.5, '4 3')); o.append(T(50, 145, 'start-up (pipelines filling)', 13, 'start'))
    o.append(R(260, 132, 22, 16, ACS, AC, 3, 1.5)); o.append(T(290, 145, 'one element per cycle', 13, 'start'))
    o.append(T(20, 190, 'All 200 elements: 4 strips of 8, 64, 64 and 64', 15, 'start', bold=True))
    k = 640 / 796
    fx = lambda v: x0 + v * k
    c = 0
    for L_, t in ((8, 73), (64, 241), (64, 241), (64, 241)):
        o.append(boxt(fx(c) + 1, 204, t * k - 2, 38, [f'L = {L_}: {t}' if L_ == 64 else f'{t}'], NXS if L_ == 8 else ACS, NX if L_ == 8 else AC, 13, rx=4))
        c += t
    o.append(T(fx(36), 262, 'L = 8', 13, fill=NX))
    o.append(xaxis(x0, fx(796), 276, [0, 200, 400, 600, 796], fx, 'cycles'))
    o.append(T(20, 348, 'Total = 4 × 49 + 3 × 200 = 796 cycles = 3.98 cycles per element (the ideal is 3).', 14, 'start'))
    o.append(T(20, 370, '400 floating-point operations in 796 ns at 1 GHz = 503 MFLOPS.', 14, 'start', bold=True))
    return 384, ''.join(o)
FIG[8] = (f8, 'Each 64-element strip runs three convoys; each pays a start-up while its pipelines fill and then delivers one element per cycle, 241 cycles in all. Four strips (the first only 8 long) take 796 cycles for 200 elements, 503 MFLOPS at 1 GHz.',
          'A bar for one strip split into three start-up parts of 19, 18 and 12 cycles and three 64-cycle work parts; below, a bar of 796 cycles made of strips of 73, 241, 241 and 241 cycles.')


# ---- 5.9 MSI states of X in two caches ----
def f9():
    cols = [(345, 'P1 cache'), (475, 'P2 cache'), (625, 'memory')]
    o = [T(20, 26, 'Shared X = 5, write-back caches, MSI write-invalidate snooping', 15, 'start', bold=True)]
    o += [T(x, 52, n, 13, fill=MUT, bold=True) for x, n in cols]
    rows = [('1. P1 reads X (miss)', ('S', '5'), ('I', ''), '5'), ('2. P2 reads X (miss)', ('S', '5'), ('S', '5'), '5'),
            ('3. P1 writes 8: invalidate', ('M', '8'), ('I', ''), '5 (stale)'), ('4. P2 reads X: P1 supplies 8', ('S', '8'), ('S', '8'), '8'),
            ('5. P2 writes 10: invalidate', ('I', ''), ('M', '10'), '8 (stale)')]
    sty = {'M': (LVS, LV, None), 'S': (ACS, AC, None), 'I': (PANEL, L2, '4 3')}
    for r, (ev, p1, p2, mem) in enumerate(rows):
        y = 62 + r * 46
        o.append(T(20, y + 22, ev, 14, 'start'))
        for (x, _), (stt, v) in zip(cols[:2], (p1, p2)):
            f, s_, d = sty[stt]
            o.append(R(x - 55, y, 110, 34, f, s_, 6, 1.5, d))
            o.append(T(x, y + 22, stt + (f' · {v}' if v else ''), 15, bold=True, fill=s_ if stt != 'I' else MUT))
        stale = 'stale' in mem
        o.append(R(cols[2][0] - 70, y, 140, 34, PANEL, LN, 6, 1.5))
        o.append(T(cols[2][0], y + 22, mem, 14, fill=LV if stale else INK, bold=not stale))
    y = 62 + 5 * 46 + 20
    o += [R(20, y - 12, 22, 16, LVS, LV, 3, 1.5), T(50, y + 1, 'M: the only up-to-date copy', 13, 'start'),
          R(260, y - 12, 22, 16, ACS, AC, 3, 1.5), T(290, y + 1, 'S: shared, clean', 13, 'start'),
          R(440, y - 12, 22, 16, PANEL, L2, 3, 1.5, '4 3'), T(470, y + 1, 'I: invalid', 13, 'start')]
    return y + 16, ''.join(o)
FIG[9] = (f9, 'A write first invalidates every other copy, so only one cache can hold X in state M, and memory is stale until that cache supplies the value and writes it back (step 4).',
          'Five rows of events with the state of X in each cache and in memory: S 5 and I; S 5 and S 5; M 8 and I with memory stale; S 8 and S 8 with memory 8; I and M 10 with memory stale.')


spec = make_spec(FIG)
