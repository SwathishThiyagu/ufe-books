"""Claude's hand-drawn figures for c-coa-u6 (Computer Organization and Architecture, unit 6: memory hierarchy and I/O
organization), one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def bars_pct(o, y0, rows, x0, s, line100=True):
    """horizontal percentage bars; rows = (label, sub, pct, text, colour pair)"""
    for r, (lab, sub, p, txt, (f, st)) in enumerate(rows):
        y = y0 + r * 54
        o.append(T(x0 - 10, y + 18, lab, 14, 'end', bold=True)); o.append(T(x0 - 10, y + 35, sub, 13, 'end', MUT))
        o.append(R(x0, y + 4, max(p * s, 3), 32, f, st, 4))
        o.append(T(x0 + max(p * s, 3) + 8, y + 26, txt, 14, 'start', st, True))
    if line100:
        o.append(L(x0 + 100 * s, y0 - 8, x0 + 100 * s, y0 + len(rows) * 54, INK, 1.5, '5 4'))
        o.append(T(x0 + 100 * s, y0 - 14, '100% = the whole processor', 13, fill=MUT))


# ---- 6.1 what a cache in front of DRAM buys ----
def f1():
    x0, s = 200, 7
    o = [T(20, 26, 'Average access time with a 2 ns cache in front of 60 ns DRAM', 15, 'start', bold=True)]
    rows = [('Cache 2 MB', '₹500 per MB', [(2, ACS, AC)], '2 ns'), ('DRAM 8 GB', '₹0.25 per MB', [(60, LVS, LV)], '60 ns'),
            ('Both, h = 0.97', '₹0.37 per MB', [(2, ACS, AC), (1.8, LVS, LV)], '3.8 ns = 2 + 0.03 × 60'),
            ('Both, h = 0.99', 'same cost', [(2, ACS, AC), (0.6, LVS, LV)], '2.6 ns = 2 + 0.01 × 60')]
    for r, (n, sub, parts, lab) in enumerate(rows):
        y = 46 + r * 56
        o.append(T(190, y + 18, n, 14, 'end', bold=True)); o.append(T(190, y + 35, sub, 13, 'end', MUT))
        c = 0
        for v, f, st in parts:
            o.append(R(x0 + c * s, y + 4, v * s, 32, f, st, 3, 1.5)); c += v
        o.append(T(x0 + c * s + 10, y + 26, lab, 14, 'start', bold=True))
    o.append(xaxis(x0, x0 + 60 * s, 280, [0, 10, 20, 30, 40, 50, 60], lambda v: x0 + v * s, 'access time (ns)'))
    o.append(T(20, 352, 'The pair is 60 ÷ 3.8 = 15.8 times faster than DRAM alone and costs ₹0.37 per MB against ₹0.25.', 14, 'start', bold=True))
    o.append(T(20, 374, 'Green = cache time paid on every access; orange = the misses\' share of the DRAM time.', 13, 'start', MUT))
    return 388, ''.join(o)
FIG[1] = (f1, 'Every access pays the 2 ns cache time, and the 3% that miss also pay 60 ns, so the average is 3.8 ns: almost as fast as the cache at almost the price of DRAM. Raising the hit ratio to 0.99 brings it to 2.6 ns.',
          'Four bars on a 0 to 60 ns scale: cache 2 ns, DRAM 60 ns, and the cache with DRAM at hit ratios 0.97 and 0.99, 3.8 and 2.6 ns, split into the cache time and the miss share.')


# ---- 6.2 a 4M x 32 memory from sixteen 1M x 8 chips ----
def f2():
    o = [T(20, 24, 'Address 0x2ABCDE: A21 A20 = 1 0, so row 2 answers', 15, 'start', bold=True),
         T(20, 44, '22 address lines: 2 pick the row of chips, 20 pick the word inside every chip', 13, 'start', MUT)]
    o.append(T(70, 84, 'A21 A20 = 1 0', 13, bold=True, fill=AC))
    o.append(L(70, 90, 70, 104, AC, 2, arrow='n'))
    o.append(boxt(20, 106, 100, 160, ['2-to-4', 'decoder'], PANEL, AC, 14, bold_first=True))
    for c, lab in enumerate(('D31–24', 'D23–16', 'D15–8', 'D7–0')):
        o.append(T(228 + c * 130, 70, lab, 13, fill=NX, bold=True))
    for r in range(4):
        y = 80 + r * 50
        hot = r == 2
        o.append(L(122, y + 18, 166, y + 18, AC if hot else L2, 2.5 if hot else 1.5))
        o.append(T(144, y + 12, f'CS{r}', 13, fill=AC if hot else MUT, bold=hot))
        for c in range(4):
            o.append(boxt(170 + c * 130, y, 116, 36, ['1M × 8'], ACS if hot else PANEL, AC if hot else L2, 13, bold_first=hot))
    o.append(T(20, 300, 'A0–A19 go to all 16 chips; only the selected row drives the 32 data lines.', 14, 'start'))
    o.append(T(20, 328, 'Refresh: 64 ms ÷ 8,192 rows = 7.8 µs per row; 8,192 × 50 ns = 409.6 µs, 0.64% of the time.', 14, 'start'))
    return 342, ''.join(o)
FIG[2] = (f2, 'Four chips side by side give 32 bits, and four such rows give 4M words: 16 chips. The top two address bits drive a decoder that selects one row, so 0x2ABCDE (A21 A20 = 10) is answered by row 2.',
          'A 2-to-4 decoder whose four chip-select lines CS0 to CS3 each enable a row of four 1M by 8 chips; row 2 is highlighted, and the columns are labelled with their byte of the 32-bit data bus.')


# ---- 6.3 address fields and a small mapping trace ----
def f3():
    x0, bw = 40, 20
    o = []
    rows = [('Direct mapped: 2,048 lines', [('tag 16', 16, PANEL, L2), ('index 11', 11, ACS, AC), ('offset 5', 5, NXS, NX)]),
            ('Fully associative: no index', [('tag 27', 27, PANEL, L2), ('offset 5', 5, NXS, NX)]),
            ('4-way set associative: 512 sets', [('tag 18', 18, PANEL, L2), ('set 9', 9, ACS, AC), ('offset 5', 5, NXS, NX)])]
    for r, (title, fs) in enumerate(rows):
        y = 26 + r * 68
        o.append(T(20, y, title, 14, 'start', bold=True))
        c = 0
        for lab, n, f, st in fs:
            o.append(boxt(x0 + c * bw, y + 10, n * bw, 34, [lab], f, st, 14, rx=3)); c += n
    o.append(T(20, 236, 'Blocks 3, 11, 3, 5, 11, 3 in a cache of 4 lines', 15, 'start', bold=True))
    blocks = [3, 11, 3, 5, 11, 3]
    tr = [('direct (block mod 4)', 'MMMMMM', '6 misses'), ('2-way, LRU', 'MMHMMM', '5 misses'), ('fully associative, LRU', 'MMHMHH', '3 misses')]
    bx = 250
    for i, b in enumerate(blocks):
        o.append(TM(bx + i * 66 + 31, 262, str(b), 15, bold=True))
    for r, (lab, seq, m) in enumerate(tr):
        y = 274 + r * 38
        o.append(T(240, y + 20, lab, 13, 'end', bold=True))
        for i, ch in enumerate(seq):
            hit = ch == 'H'
            o.append(boxt(bx + i * 66 + 2, y, 60, 30, ['hit' if hit else 'miss'], NXS if hit else LVS, NX if hit else LV, 13, rx=4))
        o.append(T(bx + 6 * 66 + 8, y + 20, m, 13, 'start', bold=True))
    o.append(T(20, 410, 'Direct: 3 and 11 both land on line 3 and keep throwing each other out.', 13, 'start', MUT))
    return 424, ''.join(o)
FIG[3] = (f3, 'For 32-bit addresses, a 64 KB cache and 32-byte blocks, the offset is always 5 bits; the index or set field shrinks as associativity grows and the tag takes the rest. On the short trace, more freedom of placement turns 6 misses into 3.',
          'Three 32-bit address strips split into tag 16, index 11, offset 5; tag 27, offset 5; and tag 18, set 9, offset 5; below, hit and miss cells for six block accesses under direct, 2-way and fully associative mapping.')


# ---- 6.4 CPI stack ----
def f4():
    x0, s = 170, 100
    fx = lambda v: x0 + v * s
    o = [R(20, 18, 22, 16, PANEL, L2, 3, 1.5), T(50, 31, 'base CPI', 13, 'start'),
         R(160, 18, 22, 16, LVS, LV, 3, 1.5), T(190, 31, 'instruction-miss stalls', 13, 'start'),
         R(380, 18, 22, 16, ACS, AC, 3, 1.5), T(410, 31, 'data-miss stalls', 13, 'start')]
    rows = [('Perfect cache', [1.2], '1.2'), ('L1 only', [1.2, 2.0, 1.5], '4.7'), ('L1 + L2', [1.2, 0.6, 0.45], '2.25')]
    sty = [(PANEL, L2), (LVS, LV), (ACS, AC)]
    for r, (n, parts, tot) in enumerate(rows):
        y = 56 + r * 60
        o.append(T(160, y + 26, n, 14, 'end', bold=True))
        c = 0
        for v, (f, st) in zip(parts, sty):
            o.append(boxt(fx(c) + 1, y, v * s - 2, 40, [f'{v:g}'], f, st, 13, rx=4)); c += v
        o.append(T(fx(c) + 8, y + 26, tot, 15, 'start', bold=True))
    o.append(xaxis(x0, fx(5), 248, [0, 1, 2, 3, 4, 5], fx, 'cycles per instruction'))
    o.append(T(20, 318, 'L1 only: stalls = 0.02 × 100 + 0.30 × 0.05 × 100 = 3.5 cycles; a perfect cache would be 3.9 times faster.', 13, 'start'))
    o.append(T(20, 340, 'With L2 each L1 miss costs 10 + 0.20 × 100 = 30 cycles, not 100: CPI 2.25, a speedup of 2.09.', 14, 'start', bold=True))
    return 354, ''.join(o)
FIG[4] = (f4, 'With only L1, memory stalls add 3.5 cycles to the 1.2 of useful work, making CPI 4.7. An L2 cache cuts each L1 miss from 100 to 30 cycles, so the stalls shrink to 1.05 and CPI falls to 2.25.',
          'Three stacked bars of cycles per instruction: perfect cache 1.2; L1 only 1.2 plus 2.0 plus 1.5 equals 4.7; L1 and L2 1.2 plus 0.6 plus 0.45 equals 2.25.')


# ---- 6.5 translating 0x00403A7C ----
def f5():
    bw = 20
    o = [T(20, 24, 'Virtual address 0x00403A7C, 4 KB pages', 15, 'start', bold=True)]
    o.append(boxt(40, 54, 20 * bw, 40, ['VPN 0x00403   (20 bits)'], ACS, AC, 14, rx=3))
    o.append(boxt(440, 54, 12 * bw, 40, ['offset 0xA7C   (12 bits)'], NXS, NX, 14, rx=3))
    o.append(L(240, 96, 240, 124, AC, 2, arrow='n'))
    o.append(boxt(110, 126, 260, 52, ['TLB, or the page table on a miss', 'VPN 0x00403 → frame 0x2B1F'], PANEL, AC, 13, bold_first=True))
    o.append(L(240, 180, 240, 208, AC, 2, arrow='n'))
    o.append(L(560, 96, 560, 208, NX, 2, '6 4', arrow='x'))
    o.append(Tb(560, 152, 'copied unchanged', 13, fill=NX, bold=True))
    o.append(boxt(80, 210, 18 * bw, 40, ['frame 0x2B1F   (18 bits)'], ACS, AC, 14, rx=3))
    o.append(boxt(440, 210, 12 * bw, 40, ['offset 0xA7C'], NXS, NX, 14, rx=3))
    o.append(T(680, 274, 'physical address 0x02B1FA7C (30 bits for 1 GB)', 14, 'end', bold=True))
    o.append(T(20, 316, 'EAT = 0.98 × (2 + 80) + 0.02 × (2 + 80 + 80) = 83.6 ns, only 4.5% above one memory access.', 14, 'start'))
    o.append(T(20, 340, 'Page table: 2²⁰ PTEs × 4 B = 4 MB flat; with two levels an 8 MB region needs only 12 KB.', 14, 'start'))
    return 354, ''.join(o)
FIG[5] = (f5, 'The 12-bit offset passes straight through; only the 20-bit page number is translated, here 0x00403 to frame 0x2B1F, giving 0x02B1FA7C. With a 98% TLB hit rate translation costs just 3.6 ns on average.',
          'A 32-bit virtual address split into page number 0x00403 and offset 0xA7C; the page number goes through the TLB to frame 0x2B1F while the offset is copied, forming the physical address 0x02B1FA7C.')


# ---- 6.6 disk access time and RAID parity ----
def f6():
    x0, s = 40, 75
    o = [T(20, 24, 'Reading one 4 KB block from a 7,200 rpm disk', 15, 'start', bold=True)]
    segs = [('seek 4 ms', 4, LVS, LV), ('rotation 4.17 ms (half a turn of 8.33)', 4.17, ACS, AC), ('', 0.02, NXS, NX), ('', 0.2, NXS, NX)]
    c = 0
    for lab, v, f, st in segs:
        o.append(boxt(x0 + c * s, 38, v * s, 40, [lab] if lab else [''], f, st, 13, rx=3)); c += v
    o.append(L(x0 + c * s - 8, 84, x0 + c * s - 8, 92, NX, 1.5))
    o.append(T(x0 + c * s, 106, 'transfer 0.02 + controller 0.2 ms', 13, 'end', NX))
    o.append(T(20, 134, '= 8.39 ms per read, about 119 random reads per second (an SSD manages about 10,000).', 14, 'start', bold=True))
    o.append(T(20, 180, 'RAID 5 parity is the XOR of the stripe', 15, 'start', bold=True))
    def bits(x, y, b, f, st):
        out = []
        for i, d in enumerate(b.replace(' ', '')):
            out.append(R(x + i * 26, y, 24, 28, f, st, 3, 1.2)); out.append(TM(x + i * 26 + 12, y + 19, d, 14, bold=True))
        return ''.join(out)
    left = [('D0', '1011 0010', PANEL, L2), ('D1', '0110 1100', PANEL, L2), ('D2', '1100 0101', PANEL, L2), ('P', '0001 1011', ACS, AC)]
    right = [('D0', '1011 0010', PANEL, L2), ('D2', '1100 0101', PANEL, L2), ('P', '0001 1011', ACS, AC), ('D1', '0110 1100', NXS, NX)]
    o.append(T(90, 204, 'make P = D0 ⊕ D1 ⊕ D2', 13, 'start', MUT, True))
    o.append(T(470, 204, 'D1\'s disk fails: D0 ⊕ D2 ⊕ P', 13, 'start', MUT, True))
    for r in range(4):
        y = 214 + r * 34 + (6 if r == 3 else 0)
        for (n, b, f, st), x in ((left[r], 90), (right[r], 470)):
            o.append(T(x - 10, y + 19, ('= ' if r == 3 else '') + n, 14, 'end', bold=True))
            o.append(bits(x, y, b, f, st))
    o.append(L(90, 316, 298, 316, INK, 1.5)); o.append(L(470, 316, 678, 316, INK, 1.5))
    o.append(T(20, 380, 'XOR of all four blocks is 0, so any one lost block is the XOR of the other three.', 14, 'start'))
    return 394, ''.join(o)
FIG[6] = (f6, 'A random 4 KB read is almost all seek and rotation (8.17 of 8.39 ms); moving the data takes 0.02 ms. RAID 5 stores the XOR of each stripe, so the block on a failed disk can be rebuilt from the others.',
          'A time bar of 4 ms seek, 4.17 ms rotation and a thin transfer and controller part; below, bit rows showing D0, D1 and D2 combined by XOR into parity P, and D0, D2 and P combined to rebuild D1.')


# ---- 6.7 the cost of polling, and a UART frame ----
def f7():
    o = [T(20, 24, 'Share of a 1 GHz processor spent polling (400 cycles per poll)', 15, 'start', bold=True)]
    bars_pct(o, 60, [('mouse', '30 polls per second', 0.0012, '0.0012%', (NXS, NX)),
                     ('fast device', '6.25 million polls/s', 250, '250%', (LVS, LV))], 200, 1.7)
    o.append(T(20, 200, 'UART 8N1 at 115,200 baud: 10 bits on the wire carry one byte', 15, 'start', bold=True))
    cells = [('start', '0', LVS, LV)] + [(f'D{i}', '', ACS, AC) for i in range(8)] + [('stop', '1', LVS, LV)]
    for i, (n, v, f, st) in enumerate(cells):
        o.append(boxt(110 + i * 50, 214, 46, 40, [n] + ([v] if v else []), f, st, 13, rx=4))
    o.append(brace(110 + 50 + 2, 110 + 9 * 50 - 6, 262, AC))
    o.append(T(110 + 5 * 50 - 2, 286, '8 data bits', 13, fill=AC, bold=True))
    o.append(T(20, 322, '115,200 ÷ 10 = 11,520 bytes/s, so a 2 KB file takes 2,048 ÷ 11,520 = 0.178 s = 178 ms.', 14, 'start'))
    return 336, ''.join(o)
FIG[7] = (f7, 'Polling a mouse 30 times a second costs almost nothing, but polling a 100 MB/s device every 16 bytes would need 2.5 processors\' worth of cycles, so it needs DMA. A UART spends 10 bits on the wire for every 8-bit byte.',
          'Two bars against a dashed 100 percent line: mouse polling at 0.0012 percent and fast-device polling at 250 percent; below, a 10-cell UART frame of a start bit, eight data bits and a stop bit.')


# ---- 6.8 the 8086 vector and the cost of interrupts ----
def f8():
    o = [T(20, 24, 'Interrupt type 21h: its vector is at 4 × 21h = 84h', 15, 'start', bold=True)]
    for i, (a, v) in enumerate((('84h', '34'), ('85h', '12'), ('86h', '00'), ('87h', 'A0'))):
        x = 120 + i * 100
        o.append(TM(x + 47, 52, a, 13, fill=MUT))
        o.append(boxt(x, 60, 94, 38, [v], ACS if i < 2 else NXS, AC if i < 2 else NX, 16, bold_first=True))
    o.append(brace(122, 312, 106, AC)); o.append(T(217, 130, 'IP = 1234h (low byte first)', 13, fill=AC, bold=True))
    o.append(brace(322, 512, 106, NX)); o.append(T(417, 130, 'CS = A000h', 13, fill=NX, bold=True))
    o.append(T(20, 166, 'ISR address = CS × 16 + IP = A0000h + 1234h = A1234h', 14, 'start', bold=True))
    o.append(T(20, 214, 'Share of a 2 GHz processor spent on interrupts (1,000 cycles each)', 15, 'start', bold=True))
    bars_pct(o, 250, [('network card', '50,000 per second', 2.5, '2.5%', (NXS, NX)),
                      ('fast device', '6.25 million per second', 312, '312%', (LVS, LV))], 200, 1.4)
    o.append(T(20, 380, 'Interrupts remove the waiting of polling but not the cost per word: a fast device needs DMA.', 14, 'start'))
    return 394, ''.join(o)
FIG[8] = (f8, 'The four bytes at 84h hold IP = 1234h and CS = A000h, so the ISR starts at A1234h. Interrupts are cheap for a network card (2.5% of the processor) but a device interrupting every 16 bytes would need 312%.',
          'Four memory bytes at 84h to 87h holding 34, 12, 00 and A0, grouped into IP 1234h and CS A000h; below, two bars of 2.5 percent and 312 percent against a 100 percent line.')


# ---- 6.9 one DMA block on a time line ----
def f9():
    x0, s = 130, 26
    fx = lambda us: x0 + us * s
    o = [T(20, 24, 'One 4 KB block from a 200 MB/s disk, 1 GHz processor', 15, 'start', bold=True)]
    o.append(T(120, 84, 'processor', 14, 'end', bold=True))
    o.append(R(fx(0), 62, 1 * s, 36, LVS, LV, 3))
    o.append(boxt(fx(1) + 2, 62, 20.48 * s - 4, 36, ['free for other programs'], NXS, NX, 13, rx=3))
    o.append(R(fx(21.48), 62, 0.5 * s, 36, LVS, LV, 2))
    o.append(T(fx(0), 54, 'set-up 1 µs', 13, 'start', LV, True))
    o.append(T(fx(21.98), 54, 'interrupt 0.5 µs', 13, 'end', LV, True))
    o.append(T(120, 140, 'DMA controller', 14, 'end', bold=True))
    o.append(boxt(fx(1), 118, 20.48 * s, 36, ['moves 4,096 bytes: 4,096 ÷ 200 MB/s = 20.48 µs'], ACS, AC, 13, rx=3))
    o.append(xaxis(x0, fx(22), 176, [0, 5, 10, 15, 20], fx, 'time (µs)'))
    o.append(T(20, 250, '48,828 blocks per second × 1,500 cycles = 7.32 × 10⁷ cycles: 7.3% of the processor.', 14, 'start', bold=True))
    o.append(T(20, 272, 'Polling the same disk 16 bytes at a time would need 250% of it.', 14, 'start'))
    o.append(T(20, 304, 'Cycle stealing at 4 MB/s takes 10⁶ × 50 ns = 5% of bus time; a 4 KB burst holds the bus for 51.2 µs.', 13, 'start', MUT))
    return 318, ''.join(o)
FIG[9] = (f9, 'The processor spends 1 µs setting up the transfer and 0.5 µs on the completion interrupt; for the 20.48 µs in between the DMA controller moves the block and the processor is free. That is 7.3% of the processor, against 250% for polling.',
          'Two time lines from 0 to 22 microseconds: the processor busy only for a short set-up and a short interrupt and free in between, and the DMA controller moving the block for 20.48 microseconds.')


spec = make_spec(FIG)
