"""Claude's hand-drawn figures for c-coa-u4 (Computer Organization and Architecture, unit 4: processor datapath and control
unit), one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 4.1 the fetch, cycle by cycle, from memory and from a cache ----
def f1():
    x0, s = 170, 40
    X = lambda ns: x0 + ns * s
    o = []
    rows = [(52, 'Memory, 7 ns', '5 cycles = 12.5 ns', [('1', 'MAR ← PC'), ('2', 'PC ← PC + 4'), ('3', 'wait'), ('4', 'wait'), ('5', 'IR ← MDR')], 7, 'memory busy 7 ns'),
            (176, 'Cache, 2 ns', '3 cycles = 7.5 ns', [('1', 'MAR ← PC'), ('2', 'PC + 4, wait'), ('3', 'IR ← MDR')], 2, 'cache 2 ns')]
    for y, name, tot, steps, busy, blab in rows:
        o.append(T(160, y + 20, name, 14, 'end', bold=True)); o.append(T(160, y + 38, tot, 13, 'end', MUT))
        for i, (n, lab) in enumerate(steps):
            w8 = lab in ('wait', 'PC + 4, wait')
            o.append(boxt(X(i * 2.5) + 2, y, 2.5 * s - 4, 46, [n, lab], PANEL if w8 else ACS, L2 if w8 else AC, 13, bold_first=True, dash='5 3' if w8 else None))
        o.append(R(X(2.5), y + 54, busy * s, 22, LVS, LV, 4, 1.5))
        o.append(T(X(2.5 + busy / 2), y + 70, blab, 13, fill=LV, bold=True))
        mfc = 2.5 + busy
        o.append(L(X(mfc), y + 50, X(mfc), y + 92, LV, 2))
        o.append(T(X(mfc) + 6, y + 92, f'MFC at {mfc:g} ns', 13, 'start', LV))
    o.append(xaxis(x0, X(12.5), 296, [0, 2.5, 5, 7.5, 10, 12.5], X, 'time (ns), one clock cycle = 2.5 ns', fmt=lambda v: f'{v:g}'))
    o.append(T(20, 366, 'With 2 execute cycles: 7 × 2.5 ns = 17.5 ns per instruction, 57.1 million per second.', 14, 'start'))
    o.append(T(20, 388, 'With the cache: 5 × 2.5 ns = 12.5 ns per instruction, 80 million per second (1.4 times faster).', 14, 'start', bold=True))
    return 402, ''.join(o)
FIG[1] = (f1, 'The fetch waits for memory: MAR gets the address in cycle 1, memory answers 7 ns later (MFC at 9.5 ns), and IR is loaded in cycle 5. A 2 ns cache cuts the fetch to 3 cycles.',
          'Two rows of clock-cycle boxes on a 0 to 12.5 ns axis: five cycles with a 7 ns memory wait, and three cycles with a 2 ns cache wait, each marked where MFC arrives.')


# ---- 4.2 the seven steps of Add (R3), R1 ----
def f2():
    o = [T(20, 24, 'Add (R3), R1 with R1 = 25, R3 = 1500 and memory[1500] = 17', 15, 'start', bold=True),
         T(36, 50, 'step', 13, fill=MUT), T(70, 50, 'control signals', 13, 'start', MUT), T(565, 50, 'what changes', 13, fill=MUT)]
    steps = [('PCout, MARin, Read, Select4, Add, Zin', 'MAR = 2000, Z = 2004'), ('Zout, PCin, Yin, WMFC', 'PC = 2004'),
             ('MDRout, IRin', 'IR = Add (R3), R1'), ('R3out, MARin, Read', 'MAR = 1500'), ('R1out, Yin, WMFC', 'Y = 25, MDR = 17'),
             ('MDRout, SelectY, Add, Zin', 'Z = 25 + 17 = 42'), ('Zout, R1in, End', 'R1 = 42')]
    for i, (sig, eff) in enumerate(steps):
        ex = i >= 3
        y = 60 + i * 36 + (32 if ex else 0)
        o.append(C(36, y + 15, 12, AC if ex else L2, ACS if ex else PANEL))
        o.append(T(36, y + 20, str(i + 1), 13, bold=True))
        o.append(TM(70, y + 20, sig, 13, 'start'))
        last = i == 6
        o.append(boxt(430, y, 270, 30, [eff], NXS if last else (ACS if ex else PANEL), NX if last else (AC if ex else L2), 13, bold_first=last, rx=5))
    o.append(L(20, 181, 60, 181, L2, 1.5, '4 3'))
    o.append(T(70, 186, 'steps 1–3 fetch the instruction (the same every time); steps 4–7 execute it', 13, 'start', MUT))
    o.append(T(20, 372, 'Final R1 = 42 and PC = 2004, ready for the next instruction.', 14, 'start', bold=True))
    return 386, ''.join(o)
FIG[2] = (f2, 'Each step is one clock cycle of register transfers. Steps 1 to 3 fetch the instruction; steps 4 to 7 read memory[1500] = 17, add it to R1 = 25 through Y and Z, and write 42 back to R1.',
          'Seven numbered rows, each with the control signals of one step and the register value it changes, divided into the fetch (steps 1 to 3) and the execute part (steps 4 to 7).')


# ---- 4.3 single bus against three buses ----
def f3():
    x0, s = 190, 38
    fx = lambda ns: x0 + ns * s
    o = [R(20, 18, 22, 16, ACS, AC, 3, 1.5), T(50, 31, 'register adds (50%)', 13, 'start'),
         R(220, 18, 22, 16, LVS, LV, 3, 1.5), T(250, 31, 'loads (30%)', 13, 'start'),
         R(370, 18, 22, 16, NXS, NX, 3, 1.5), T(400, 31, 'branches (20%)', 13, 'start')]
    rows = [('Single bus', '5.8 steps × 2.0 ns', [6.0, 3.6, 2.0], '11.6 ns'), ('Three buses', '4.6 steps × 2.2 ns', [4.4, 3.96, 1.76], '10.12 ns')]
    for r, (name, sub, parts, tot) in enumerate(rows):
        y = 64 + r * 84
        o.append(T(180, y + 20, name, 14, 'end', bold=True)); o.append(T(180, y + 38, sub, 13, 'end', MUT))
        c = 0
        for v, (f, st) in zip(parts, ((ACS, AC), (LVS, LV), (NXS, NX))):
            o.append(boxt(fx(c) + 1, y, v * s - 2, 44, [f'{v:g}'], f, st, 13, rx=4)); c += v
        o.append(T(fx(c) + 8, y + 28, tot, 15, 'start', bold=True))
    o.append(xaxis(x0, fx(12), 236, [0, 2, 4, 6, 8, 10, 12], fx, 'average time per instruction (ns)'))
    o.append(T(20, 312, '200 million instructions: 2.32 s against 2.024 s, a speedup of 1.15.', 14, 'start', bold=True))
    o.append(T(20, 334, 'Not 6 ÷ 4 = 1.5: loads still take 6 steps, and the longer wires slow the clock to 2.2 ns.', 14, 'start'))
    return 348, ''.join(o)
FIG[3] = (f3, 'Average time per instruction, split by instruction kind. Three buses cut adds and branches to fewer steps but leave loads alone and slow the clock, so 11.6 ns only falls to 10.12 ns, a speedup of 1.15.',
          'Two stacked bars in nanoseconds: single bus 6.0 for adds, 3.6 for loads and 2.0 for branches, total 11.6; three buses 4.4, 3.96 and 1.76, total 10.12.')


# ---- 4.4 lw $t0, 8($s1) through the single-cycle datapath ----
def f4():
    o = [boxt(20, 120, 62, 50, ['PC', '400'], PANEL, AC, 14, bold_first=True),
         boxt(110, 96, 124, 96, ['Instruction', 'memory', '0x8E280008'], PANEL, AC, 13, bold_first=True),
         boxt(270, 96, 122, 96, ['Registers', 'read reg 17', '= 1000'], PANEL, AC, 13, bold_first=True),
         boxt(428, 96, 94, 96, ['ALU', '1000 + 8', '= 1008'], ACS, AC, 13, bold_first=True),
         boxt(558, 96, 142, 96, ['Data memory', 'read [1008]', '= 55'], ACS, AC, 13, bold_first=True),
         boxt(110, 26, 124, 40, ['PC + 4 = 404'], PANEL, L2, 13),
         boxt(272, 222, 118, 38, ['sign-extend 8'], PANEL, L2, 13)]
    o.append(P([(51, 118), (51, 46), (106, 46)], L2, 2)); o.append(L(100, 46, 107, 46, L2, 2, arrow='m'))
    o.append(L(84, 145, 107, 145, AC, 2, arrow='n'))
    o.append(L(236, 145, 267, 145, AC, 2, arrow='n'))
    o.append(P([(172, 194), (172, 241), (262, 241)], AC, 2)); o.append(L(260, 241, 269, 241, AC, 2, arrow='n'))
    o.append(L(394, 130, 425, 130, AC, 2, arrow='n'))
    o.append(P([(392, 241), (475, 241), (475, 202)], AC, 2)); o.append(L(475, 204, 475, 195, AC, 2, arrow='n'))
    o.append(Tb(452, 226, '8', 13, fill=MUT))
    o.append(L(524, 145, 555, 145, AC, 2, arrow='n'))
    o.append(P([(629, 94), (629, 78), (331, 78), (331, 86)], NX, 2.5)); o.append(L(331, 84, 331, 93, NX, 2.5, arrow='x'))
    o.append(Tb(480, 78, 'write back: $t0 = 55', 13, fill=NX, bold=True))
    o.append(T(20, 292, 'Control signals for lw', 14, 'start', bold=True))
    sig = [('RegDst', 0), ('ALUSrc', 1), ('MemRead', 1), ('MemtoReg', 1), ('RegWrite', 1), ('MemWrite', 0), ('Branch', 0)]
    for i, (n, v) in enumerate(sig):
        o.append(boxt(14 + i * 100, 302, 94, 46, [n, f'= {v}'], ACS if v else PANEL, AC if v else L2, 13, bold_first=bool(v), rx=5))
    o.append(T(20, 378, 'Branch = 0, so the next PC is 404. ALUSrc = 1 sends the sign-extended 8 to the ALU instead of a register.', 13, 'start', MUT))
    return 392, ''.join(o)
FIG[4] = (f4, 'lw $t0, 8($s1) flows left to right: register 17 gives 1000, the ALU adds the offset 8 to get the address 1008, data memory returns 55, and it is written back into $t0. The control signals that are 1 are shaded.',
          'A left-to-right datapath of PC 400, instruction memory, registers reading 1000, the ALU computing 1008, and data memory returning 55, with a write-back path to $t0 and a row of seven control signals below.')


# ---- 4.5 when BRN ends, for N = 0 and N = 1 ----
def f5():
    x0, w = 176, 106
    o = [T(x0 + i * w + 52, 30, f'T{i + 1}', 14, fill=MUT, bold=True) for i in range(5)]
    for r, (lab, sub, n) in enumerate((('N = 0: not taken', '4 cycles, PC = 3004', 0), ('N = 1: taken', '5 cycles, PC = 2964', 1))):
        y = 44 + r * 80
        o.append(T(166, y + 22, lab, 14, 'end', bold=True)); o.append(T(166, y + 40, sub, 13, 'end', MUT))
        o.append(boxt(x0 + 1, y, 3 * w - 4, 52, ['fetch', 'Y = 3004'], PANEL, L2, 13, bold_first=True))
        o.append(boxt(x0 + 3 * w + 1, y, w - 4, 52, ['Z = 2964', 'End' if n == 0 else 'Zin'], LVS if n == 0 else ACS, LV if n == 0 else AC, 13, bold_first=n == 0))
        if n == 0:
            o.append(boxt(x0 + 4 * w + 1, y, w - 4, 52, ['not', 'reached'], PANEL, LN, 13, dash='4 4'))
        else:
            o.append(boxt(x0 + 4 * w + 1, y, w - 4, 52, ['PC = 2964', 'End'], LVS, LV, 13))
    o.append(T(20, 222, 'End = T7·ADD + T5·BR + (T5·N + T4·N̄)·BRN', 15, 'start', bold=True))
    o.append(T(20, 246, 'Zin = T1 + T6·ADD + T4·(BR + BRN)', 15, 'start'))
    o.append(T(20, 290, '12 steps at most: a 4-bit step counter and a 4-to-16 step decoder (T1 to T12 used).', 14, 'start'))
    o.append(T(20, 312, '40 instructions: a 6-bit opcode and a 6-to-64 instruction decoder.', 14, 'start'))
    return 326, ''.join(o)
FIG[5] = (f5, 'BRN at 3000 with offset −40: step T4 always forms Z = 3004 − 40 = 2964. When N = 0 the T4·N̄ term ends the instruction at once; when N = 1 step T5 loads 2964 into PC and ends there.',
          'Two rows of control steps T1 to T5: both share the fetch in T1 to T3 and form 2964 in T4; for N equal to 0 End comes in T4, for N equal to 1 T5 loads PC with 2964 and ends.')


# ---- 4.6 horizontal against field-encoded microinstructions ----
def f6():
    x0, b = 50, 15
    groups = [('source', 9), ('dest A', 7), ('B', 4), ('ALU function', 16), ('', 2), ('', 2), ('', 1), ('', 1)]
    fields = [('F1', 4, True), ('F2', 3, True), ('F3', 3, True), ('F4', 4, False), ('F5', 2, False), ('F6', 1, False), ('F7', 1, True), ('F8', 1, False)]
    o = [T(20, 30, 'Horizontal: 42 bits, one per control signal', 14, 'start', bold=True)]
    c = 0; gx = []
    for name, n in groups:
        o.append(R(x0 + c * b, 40, n * b, 34, PANEL, AC, 0, 1.5))
        for k in range(1, n):
            o.append(L(x0 + (c + k) * b, 40, x0 + (c + k) * b, 74, LN, 1))
        if name: o.append(T(x0 + (c + n / 2) * b, 92, name, 13, fill=MUT))
        gx.append((x0 + c * b, x0 + (c + n) * b)); c += n
    c = 0
    for (name, n, used), (g0, g1) in zip(fields, gx):
        f0, f1 = x0 + c * b, x0 + (c + n) * b
        o.append(f'<polygon points="{g0:.1f},100 {g1:.1f},100 {f1:.1f},144 {f0:.1f},144" style="fill:var(--accent-soft);fill-opacity:0.45;stroke:var(--line2);stroke-width:1"/>')
        o.append(R(f0, 146, n * b, 34, NXS if used else PANEL, NX if used else AC, 0, 1.5))
        if n > 1: o.append(T((f0 + f1) / 2, 168, name, 13, bold=True))
        o.append(T((f0 + f1) / 2, 198, str(n), 13, fill=MUT))
        c += n
    o.append(T(20, 222, 'Field-encoded: 19 bits (field widths below each field)', 14, 'start', bold=True))
    o.append(T(370, 156, 'Fetch step 2 needs Zout (F1), PCin (F2),', 13, 'start'))
    o.append(T(370, 174, 'Yin (F3) and WMFC (F7): one per field,', 13, 'start'))
    o.append(T(370, 192, 'so it can be coded (green fields).', 13, 'start'))
    o.append(boxt(20, 244, 42 * b, 30, ['control store 1024 × 42 = 43,008 bits'], PANEL, AC, 13))
    o.append(boxt(20, 282, 19 * b, 30, ['1024 × 19 = 19,456 bits'], NXS, NX, 13))
    o.append(T(20 + 19 * b + 12, 302, 'saving 1 − 19/42 = 55%', 14, 'start', NX, True))
    o.append(T(20, 340, 'The price: one small decoder per field and a little decoding delay in every step.', 13, 'start', MUT))
    return 354, ''.join(o)
FIG[6] = (f6, 'Grouping the 42 control signals into fields that can never be on together lets each field hold a short code: 19 bits instead of 42, which shrinks a 1024-word control store by 55%.',
          'A 42-cell horizontal microinstruction grouped into signal sets, each funnelling down into one field of a 19-bit encoded microinstruction; below, two bars comparing 43,008 and 19,456 bits of control store.')


spec = make_spec(FIG)
