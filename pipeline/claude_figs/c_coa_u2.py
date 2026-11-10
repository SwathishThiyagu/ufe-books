"""Claude's hand-drawn figures for c-coa-u2 (Computer Organization and Architecture, unit 2: instruction set architecture),
one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 2.1 byte order and alignment ----
def f1():
    o = [T(20, 26, 'The word 0x0A1B2C3D stored at address 2000', 15, 'start', bold=True)]
    x0, w = 200, 110
    for i in range(4):
        o.append(TM(x0 + i * w + 53, 56, str(2000 + i), 13, fill=MUT))
    for r, (name, sub, bs) in enumerate((('Big-endian', 'MSB first', ['0A', '1B', '2C', '3D']),
                                         ('Little-endian', 'LSB first', ['3D', '2C', '1B', '0A']))):
        y = 66 + r * 60
        o.append(T(185, y + 18, name, 14, 'end', bold=True)); o.append(T(185, y + 35, sub, 13, 'end', MUT))
        for i, b in enumerate(bs):
            f, st = (LVS, LV) if b == '0A' else ((NXS, NX) if b == '3D' else (PANEL, AC))
            o.append(R(x0 + i * w, y, w - 4, 42, f, st, 6))
            o.append(TM(x0 + i * w + 53, y + 27, b, 16, bold=True))
    o.append(T(x0, 196, 'orange = most significant byte 0A, green = least significant byte 3D', 13, 'start', MUT))
    o.append(T(20, 236, 'An aligned word starts at an address with address mod 4 = 0', 15, 'start', bold=True))
    bx, bw, by = 90, 36, 282
    for i in range(16):
        o.append(R(bx + i * bw, by, bw, 30, PANEL, LN, 0, 1))
    for (a, b, lab, c, f) in ((0, 4, '2000 aligned', AC, ACS), (6, 10, '2006 not aligned', LV, LVS), (12, 16, '2012 aligned', AC, ACS)):
        o.append(R(bx + a * bw + 2, by + 2, (b - a) * bw - 4, 26, f, c, 4, 1.5, None if c == AC else '5 3'))
        o.append(brace(bx + a * bw + 2, bx + b * bw - 2, by - 8, c))
        o.append(T(bx + (a + b) / 2 * bw, by - 16, lab, 13, fill=c, bold=True))
    for i in (4, 8, 12):
        o.append(L(bx + i * bw, by - 4, bx + i * bw, by + 34, L2, 2.5))
    for i in (0, 4, 6, 8, 12):
        o.append(TM(bx + i * bw + 18, by + 50, str(2000 + i), 13, fill=MUT))
    o.append(T(20, 364, '2006 mod 4 = 2, so that word would cross the boundary at 2008 and need two memory accesses.', 14, 'start'))
    return 378, ''.join(o)
FIG[1] = (f1, 'Big-endian stores the word 0x0A1B2C3D with its most significant byte 0A at address 2000; little-endian puts the least significant byte 3D there. A word is aligned when its address is a multiple of 4, so 2000 and 2012 are aligned and 2006 is not.',
          'Two rows of four byte cells at addresses 2000 to 2003 holding 0A 1B 2C 3D and 3D 2C 1B 0A; below, a row of 16 bytes with aligned words at 2000 and 2012 and a misaligned word at 2006 crossing a word boundary.')


# ---- 2.2 X = (A + B) x (C + D) with 3, 2, 1 and 0 addresses ----
def f2():
    cols = [('Three-address', [('ADD R1,A,B', 'R1 = 5'), ('ADD R2,C,D', 'R2 = 10'), ('MUL X,R1,R2', 'X = 50')]),
            ('Two-address', [('MOV R1,A', 'R1 = 2'), ('ADD R1,B', 'R1 = 5'), ('MOV R2,C', 'R2 = 4'), ('ADD R2,D', 'R2 = 10'),
                             ('MUL R1,R2', 'R1 = 50'), ('MOV X,R1', 'X = 50')]),
            ('One-address', [('LOAD A', 'AC = 2'), ('ADD B', 'AC = 5'), ('STORE T', 'T = 5'), ('LOAD C', 'AC = 4'), ('ADD D', 'AC = 10'),
                             ('MUL T', 'AC = 50'), ('STORE X', 'X = 50')]),
            ('Zero-address', [('PUSH A', '2'), ('PUSH B', '2 3'), ('ADD', '5'), ('PUSH C', '5 4'), ('PUSH D', '5 4 6'), ('ADD', '5 10'),
                              ('MUL', '50'), ('POP X', 'X = 50')])]
    o = [T(360, 24, 'X = (A + B) × (C + D) with A = 2, B = 3, C = 4, D = 6', 15, bold=True)]
    for c, (name, rows) in enumerate(cols):
        x = 12 + c * 177
        o.append(T(x + 84, 54, name, 14, bold=True))
        o.append(T(x + 84, 71, f'{len(rows)} instructions', 13, fill=AC if c == 0 else MUT, bold=c == 0))
        for i, (ins, val) in enumerate(rows):
            y = 82 + i * 32
            last = i == len(rows) - 1
            o.append(R(x, y, 168, 28, ACS if last else PANEL, AC if last else L2, 5, 1.5))
            o.append(TM(x + 7, y + 19, ins, 13, 'start'))
            o.append(T(x + 161, y + 19, val, 13, 'end', AC if last else MUT, bold=last))
    o.append(T(360, 362, 'All four give X = 50: fewer addresses per instruction means shorter instructions, but more of them.', 14, bold=True))
    o.append(T(360, 382, 'zero-address column shows the stack, bottom to top', 13, fill=MUT))
    return 394, ''.join(o)
FIG[2] = (f2, 'The same calculation, X = (2 + 3) × (4 + 6) = 50, written with three, two, one and zero addresses per instruction. The programs take 3, 6, 7 and 8 instructions.',
          'Four columns of instruction boxes, 3, 6, 7 and 8 long, each box showing the instruction and the value it produces, all ending with X = 50.')


# ---- 2.3 encoding sub and addi ----
def f3():
    x0, bw = 40, 20
    def strip(y, title, fields, hexw):
        o = [TM(20, y, title, 15, 'start', bold=True)]
        o.append(T(x0, y + 22, 'bit 31', 13, 'start', MUT)); o.append(T(x0 + 32 * bw, y + 22, 'bit 0', 13, 'end', MUT))
        c = 0
        for name, n, val, bits, kind in fields:
            f, st = {'op': (LVS, LV), 'reg': (ACS, AC), 'imm': (NXS, NX)}[kind]
            xa = x0 + c * bw
            o.append(T(xa + n * bw / 2, y + 42, name, 13, fill=MUT))
            o.append(R(xa + 1, y + 50, n * bw - 2, 38, f, st, 4))
            o.append(T(xa + n * bw / 2, y + 75, val, 15, bold=True))
            o.append(TM(xa + n * bw / 2, y + 108, bits, 13))
            c += n
        o.append(T(x0 + 32 * bw, y + 136, 'hex word: ' + hexw, 15, 'end', AC, True))
        return ''.join(o)
    o = [strip(26, 'sub $s0, $t1, $t2   (R-type)',
               [('op', 6, '0', '000000', 'op'), ('rs = $t1', 5, '9', '01001', 'reg'), ('rt = $t2', 5, '10', '01010', 'reg'),
                ('rd = $s0', 5, '16', '10000', 'reg'), ('shamt', 5, '0', '00000', 'op'), ('funct', 6, '34', '100010', 'op')], '0x012A8022')]
    o.append(L(20, 180, 700, 180, LN, 1))
    o.append(strip(210, 'addi $t1, $t1, −4   (I-type)',
                   [('op', 6, '8', '001000', 'op'), ('rs = $t1', 5, '9', '01001', 'reg'), ('rt = $t1', 5, '9', '01001', 'reg'),
                    ('immediate', 16, '−4', '1111111111111100', 'imm')], '0x2129FFFC'))
    return 360, ''.join(o)
FIG[3] = (f3, 'Each field gets its value and its bits: sub $s0, $t1, $t2 fills the six R-type fields to give 0x012A8022, and addi $t1, $t1, −4 puts −4 in two\'s complement in the 16-bit immediate to give 0x2129FFFC.',
          'Two 32-bit instruction words split into fields: R-type op, rs, rt, rd, shamt and funct with values 0, 9, 10, 16, 0, 34; I-type op, rs, rt and immediate with values 8, 9, 9 and minus 4, with each field\'s binary underneath.')


# ---- 2.4 one instruction, six effective addresses ----
def f4():
    o = [T(20, 24, 'Load R0, 600   with R1 = 100 and PC = 302 after the fetch', 15, 'start', bold=True),
         T(20, 52, 'mode', 13, 'start', MUT), T(190, 52, 'effective address (EA)', 13, 'start', MUT),
         T(565, 52, 'address', 13, fill=MUT), T(655, 52, 'R0 gets', 13, fill=MUT)]
    rows = [('Autodecrement', 'R1 = 99 first, EA = 99', '99', '40'), ('Register indirect', 'EA = [R1] = 100', '100', '75'),
            ('Direct', 'EA = 600', '600', '900'), ('Indexed', 'EA = 600 + R1 = 700', '700', '450'),
            ('Indirect', 'EA = [600] = 900', '900', '250'), ('Relative', 'EA = PC + 600 = 902', '902', '330')]
    for i, (m, ea, a, v) in enumerate(rows):
        y = 62 + i * 46
        o.append(T(20, y + 22, m, 14, 'start', bold=True))
        o.append(TM(190, y + 22, ea, 13, 'start'))
        o.append(L(398, y + 17, 516, y + 17, L2, 1.8, arrow='m'))
        o.append(R(520, y, 180, 34, PANEL, AC, 6))
        o.append(L(610, y, 610, y + 34, AC, 1.5))
        o.append(TM(565, y + 22, a, 14))
        o.append(TM(655, y + 22, v, 15, fill=AC, bold=True))
    o.append(T(20, 358, 'Immediate: R0 = 600, the number inside the instruction. Register: R0 = R1 = 100.', 14, 'start'))
    o.append(T(20, 378, 'These two modes read no memory at all.', 14, 'start', MUT))
    return 392, ''.join(o)
FIG[4] = (f4, 'The same address field 600 leads to six different memory words, depending on the mode: each row works out the effective address and the right-hand cell is the word that lands in R0.',
          'Six rows, one per addressing mode, each with its effective address worked out and an arrow to a memory cell: 99 holds 40, 100 holds 75, 600 holds 900, 700 holds 450, 900 holds 250 and 902 holds 330.')


# ---- 2.5 CPU time of the CISC and RISC versions ----
def f5():
    s = 7.0
    o = []
    for r, (name, fac, t, tl, f, st) in enumerate((('CISC', '50 M instructions × CPI 3.0 ÷ 2 GHz', 75, '75 ms', LVS, LV),
                                                   ('RISC', '80 M instructions × CPI 1.2 ÷ 2.5 GHz', 38.4, '38.4 ms', NXS, NX))):
        y = 36 + r * 92
        o.append(T(20, y, name, 15, 'start', bold=True)); o.append(T(80, y, fac, 14, 'start'))
        o.append(R(20, y + 14, t * s, 40, f, st, 6))
        o.append(T(20 + t * s + 10, y + 40, tl, 15, 'start', st, True))
    o.append(T(20, 236, 'Speedup = 75 ÷ 38.4 = 1.95', 15, 'start', bold=True))
    o.append(T(20, 262, 'Time per instruction: CISC 3.0 × 0.5 ns = 1.5 ns, RISC 1.2 × 0.4 ns = 0.48 ns.', 14, 'start'))
    o.append(T(20, 284, 'RISC runs 1.6 times as many instructions, but each one is about 3 times quicker.', 14, 'start'))
    o.append(T(20, 316, 'MIPS says 2,083 against 667 (3.1 times): too high, because a RISC instruction does less work.', 14, 'start', LV))
    return 330, ''.join(o)
FIG[5] = (f5, 'The RISC version runs 1.6 times as many instructions but at a lower CPI and a faster clock, so it takes 38.4 ms against 75 ms, 1.95 times faster. The MIPS ratio of 3.1 overstates the gain.',
          'Two bars drawn to scale: CISC 75 ms from 50 million instructions at CPI 3.0 and 2 GHz, RISC 38.4 ms from 80 million instructions at CPI 1.2 and 2.5 GHz.')


# ---- 2.6 dry run of the MIPS summing loop ----
def f6():
    x0, w = 130, 116
    o = [T(20, 24, 'Summing 12, 7, 25, 3, 18: one pass of the loop per element', 15, 'start', bold=True)]
    vals, sums = [12, 7, 25, 3, 18], [12, 19, 44, 47, 65]
    o.append(T(120, 84, 'arr', 14, 'end', bold=True))
    for i, v in enumerate(vals):
        x = x0 + i * w
        o.append(TM(x + 54, 52, f'0x100100{i * 4:02X}', 13, fill=MUT))
        o.append(boxt(x, 60, w - 8, 40, [str(v)], ACS, AC, 16, bold_first=True))
        o.append(L(x + 54, 102, x + 54, 140, AC, 2, arrow='n'))
        prev = 0 if i == 0 else sums[i - 1]
        o.append(R(x, 144, w - 8, 38, PANEL, AC, 6))
        o.append(TM(x + 54, 168, f'{prev}+{v}={sums[i]}', 13, bold=i == 4))
        o.append(boxt(x, 196, w - 8, 34, [str(4 - i)], PANEL, L2, 14))
        last = i == 4
        o.append(boxt(x, 244, w - 8, 34, ['not taken' if last else 'taken'], LVS if last else NXS, LV if last else NX, 13))
        o.append(T(x + 54, 298, f'pass {i + 1}', 13, fill=MUT))
    o.append(T(120, 160, '$t2 sum', 13, 'end', bold=True)); o.append(T(120, 176, 'lw then add', 13, 'end', MUT))
    o.append(T(120, 218, '$t1 count', 13, 'end', bold=True))
    o.append(T(120, 266, 'bne', 13, 'end', bold=True))
    o.append(T(20, 334, '$t0 steps by 4 bytes each pass. After pass 5 the count is 0, bne falls through and 65 is printed.', 14, 'start'))
    return 348, ''.join(o)
FIG[6] = (f6, 'Each pass loads one element, adds it to the running sum in $t2 and counts $t1 down by one. After the fifth pass the count reaches 0, bne is not taken and the sum 65 is printed.',
          'Five array cells 12, 7, 25, 3 and 18 at addresses 4 bytes apart, each with an arrow down to the running sum 12, 19, 44, 47 and 65, the count 4 down to 0, and bne taken four times then not taken.')


# ---- 2.7 shifts and masks on hex digits ----
def f7():
    x0, w = 200, 34
    rows = [('$s0', '0000B6C9', 'zzzzaaaa', 'start value'), ('sll 4', '000B6C90', 'zzzaaaaz', 'one digit left'),
            ('srl 8', '000000B6', 'zzzzzzaa', 'two digits dropped'), ('srl 4, andi 0xF', '0000000C', 'zzzzzzza', 'bits 7–4 = 12'),
            ('andi 0xFF00', '0000B600', 'zzzzaazz', 'keeps bits 15–8'), ('ori 0x000F', '0000B6CF', 'zzzzaaan', 'sets bits 3–0'),
            ('nor with $zero', 'FFFF4936', 'nnnnnnnn', 'every bit flipped')]
    o = [T(20, 26, 'One hex digit is 4 bits, so a shift by 4 moves one digit', 15, 'start', bold=True)]
    for r, (op, hx, kind, note) in enumerate(rows):
        y = 48 + r * 44
        o.append(TM(190, y + 21, op, 13, 'end', bold=r == 0))
        for i, (d, k) in enumerate(zip(hx, kind)):
            f, st = {'z': (PANEL, LN), 'a': (ACS, AC), 'n': (LVS, LV)}[k]
            o.append(R(x0 + i * w, y, w - 3, 32, f, st, 4, 1.5))
            o.append(TM(x0 + i * w + 15.5, y + 21, d, 15, bold=k != 'z'))
        o.append(T(x0 + 8 * w + 14, y + 21, note, 13, 'start', MUT))
    y = 48 + 7 * 44 + 18
    o += [R(20, y - 12, 22, 16, ACS, AC, 3, 1.5), T(50, y + 1, 'digit from $s0', 13, 'start'),
          R(200, y - 12, 22, 16, LVS, LV, 3, 1.5), T(230, y + 1, 'digit made by OR or NOR', 13, 'start')]
    return y + 14, ''.join(o)
FIG[7] = (f7, 'Each row is one instruction applied to $s0 = 0x0000B6C9, written as eight hex digits. Shifts slide the digits sideways, AND keeps only the masked digits and OR or NOR writes new ones.',
          'Seven rows of eight hex-digit cells: 0000B6C9 and the results of sll 4, srl 8, srl then andi, andi 0xFF00, ori 0x000F and nor, with the digits that came from the original value shaded.')


# ---- 2.8 memory layout after linking A then B ----
def f8():
    tx, dx, cw = 130, 430, 140
    o = [T(tx + cw / 2, 30, 'Text (code)', 14, bold=True), T(dx + cw / 2, 30, 'Data', 14, bold=True)]
    o.append(boxt(tx, 44, cw, 64, ['A: 0x100 bytes', 'contains jal B'], ACS, AC, 13))
    o.append(boxt(tx, 108, cw, 128, ['B: 0x200 bytes'], NXS, NX, 13))
    for y, a in ((48, '0x00400000'), (112, '0x00400100'), (240, '0x00400300')):
        o.append(TM(tx - 8, y + 9, a, 13, 'end', MUT))
    o.append(arc(tx + cw + 2, 84, tx + cw + 2, 116, 0.7, AC, 2, 'n'))
    o.append(T(tx + cw + 28, 104, 'jal B', 13, 'start', AC, True))
    o.append(boxt(dx, 44, cw, 64, ['X (from A)', '0x20 bytes'], ACS, AC, 13))
    o.append(boxt(dx, 108, cw, 96, ['Y (from B)', '0x30 bytes'], NXS, NX, 13))
    for y, a in ((48, '0x10000000'), (112, '0x10000020')):
        o.append(TM(dx - 8, y + 9, a, 13, 'end', MUT))
    o.append(T(dx + cw / 2, 228, '⋮', 18, fill=MUT))
    o.append(L(dx - 6, 252, dx + cw + 110, 252, L2, 2, '6 4'))
    o.append(TM(dx - 8, 257, '$gp = 0x10008000', 13, 'end', bold=True))
    o.append(L(600, 250, 600, 48, AC, 2, arrow='n'))
    o.append(Tb(600, 156, '−32,768', 13, fill=AC, bold=True))
    o.append(L(656, 250, 656, 112, NX, 2, arrow='x'))
    o.append(Tb(656, 190, '−32,736', 13, fill=NX, bold=True))
    o.append(T(20, 292, 'Fields the linker patches', 14, 'start', bold=True))
    for i, s in enumerate(('jal B           0x00400100 ÷ 4 = 0x100040',
                           'lw $a0, X($gp)  0x10000000 − 0x10008000 = −32,768 → 0x8000',
                           'sw $a1, Y($gp)  0x10000020 − 0x10008000 = −32,736 → 0x8020')):
        o.append(TM(20, 316 + i * 22, s.replace(' ', '&#160;'), 13, 'start'))
    return 372, ''.join(o)
FIG[8] = (f8, 'After linking, B\'s code follows A\'s at 0x00400100 and B\'s variable Y follows A\'s X at 0x10000020. The linker then patches jal B with that address ÷ 4, and the two $gp offsets with the distance from 0x10008000.',
          'Two columns: the text segment with A from 0x00400000 and B from 0x00400100, and the data segment with X at 0x10000000 and Y at 0x10000020, with arrows from the global pointer 0x10008000 up to X and Y.')


spec = make_spec(FIG)
