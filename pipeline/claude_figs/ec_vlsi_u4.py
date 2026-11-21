"""Claude's hand-drawn figures for ec-vlsi-u4 (VLSI Design: arithmetic, sequential and memory subsystems), one per chapter,
drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *


def lbl(x, y, s, size=13, anchor='middle', fill=MUT, bold=False):
    return T(x, y, s, size, anchor, fill, bold)


# ---- 4.1 carry look-ahead adder, a = 1011, b = 0110 ----
def f1():
    o = []
    a, b = [1, 0, 1, 1], [0, 1, 1, 0]          # bit 3 .. bit 0
    g = [x & y for x, y in zip(a, b)]; pp = [x ^ y for x, y in zip(a, b)]
    c = {0: 0}
    for i in range(4): c[i + 1] = g[3 - i] | (pp[3 - i] & c[i])
    xs = [170, 300, 430, 560]
    for j, x in enumerate(xs):
        i = 3 - j
        o.append(T(x, 26, f'bit {i}', 14, bold=True))
        o.append(lbl(x, 46, f'a{"₀₁₂₃"[i]} = {a[j]}, b{"₀₁₂₃"[i]} = {b[j]}', 13, fill=INK))
        o.append(boxt(x - 55, 58, 110, 44, [f'g{"₀₁₂₃"[i]} = {g[j]}   p{"₀₁₂₃"[i]} = {pp[j]}'], size=14))
        o.append(L(x, 102, x, 136, AC, 2, arrow='n'))
        o.append(L(x, 186, x, 226, AC, 2, arrow='n'))
        o.append(Tb(x + 26, 212, f'c{"₀₁₂₃"[i]} = {c[i]}', 13, 'middle', fill=AC, bold=True))
        s = pp[j] ^ c[i]
        o.append(boxt(x - 55, 230, 110, 44, [f's{"₀₁₂₃"[i]} = {pp[j]}⊕{c[i]} = {s}'], fill=LVS, stroke=LV, size=14))
        o.append(P([(x + 55, 80), (x + 62, 80), (x + 62, 252), (x + 57, 252)], L2, 1.5, dash='4 4'))
    o.append(boxt(110, 138, 510, 48, ['look-ahead carry unit: every cᵢ from g, p and c₀ at once'], fill=ACS, size=14))
    o.append(L(700, 162, 624, 162, AC, 2, arrow='n')); o.append(T(668, 152, 'c₀ = 0', 13))
    o.append(L(110, 162, 30, 162, AC, 2.5, arrow='n')); o.append(T(68, 152, 'c₄ = 1', 13, bold=True, fill=AC))
    o.append(lbl(690, 92, 'p goes', 13, 'end')); o.append(lbl(690, 108, 'to the XOR', 13, 'end'))
    o.append(T(360, 304, 'Result c₄ s₃ s₂ s₁ s₀ = 1 0001₂ = 17 = 11 + 6', 15, bold=True))
    o.append(lbl(360, 326, 'c₄ = g₃ + p₃g₂ + p₃p₂g₁ + … = 0 + 0 + 1·1·1 = 1, with no carry waiting for another'))
    return 340, ''.join(o)


# ---- 4.2 carry select, two 2-bit blocks ----
def f2():
    o = []
    o.append(T(190, 24, 'High block (bits 3 and 2): 10 + 01', 14, bold=True))
    o.append(T(590, 24, 'Low block (bits 1 and 0)', 14, bold=True))
    o.append(boxt(40, 40, 160, 70, ['ripple adder', 'carry in 0', 'sum 11, carry 0'], size=14))
    o.append(boxt(220, 40, 160, 70, ['ripple adder', 'carry in 1', 'sum 00, carry 1'], fill=ACS, size=14))
    o.append(boxt(500, 40, 180, 70, ['ripple adder', '11 + 10, carry in 0', 'sum 01, carry 1'], size=14))
    o.append(L(120, 110, 120, 160, L2, 2, arrow='m')); o.append(L(300, 110, 300, 160, AC, 2.5, arrow='n'))
    o.append(boxt(80, 162, 260, 56, ['three 2:1 multiplexers', 'pick s₃, s₂ and c₄'], fill=PANEL, size=14))
    o.append(P([(590, 110), (590, 190), (346, 190)], AC, 2.5))
    o.append(L(380, 190, 344, 190, AC, 2.5, arrow='n'))
    o.append(Tb(470, 182, 'real carry c₂ = 1 selects', 13, fill=AC, bold=True))
    o.append(L(210, 218, 210, 262, AC, 2, arrow='n')); o.append(L(590, 110, 590, 262, LV, 2, arrow='l'))
    o.append(boxt(130, 264, 160, 40, ['c₄ s₃ s₂ = 1 00'], fill=LVS, stroke=LV, size=14))
    o.append(boxt(520, 264, 140, 40, ['s₁ s₀ = 01'], fill=LVS, stroke=LV, size=14))
    o.append(T(360, 336, 'Sum = 1 00 01 = 10001₂ = 17. Both high-block answers were ready before c₂ arrived.', 14, bold=True))
    return 352, ''.join(o)


# ---- 4.3 partial products of 1101 x 1011 ----
def f3():
    o = []
    X = lambda w: 250 + (7 - w) * 54
    o.append(lbl(110, 30, 'weight', 13, 'end'))
    for w in range(8):
        o.append(lbl(X(w), 30, f'2{"⁰¹²³⁴⁵⁶⁷"[w]}'))
    rows = [('A = 13', [1, 1, 0, 1], 0, INK), ('× B = 11', [1, 0, 1, 1], 0, INK)]
    y = 58
    for name, bits, sh, col in rows:
        o.append(T(130, y + 5, name, 14, 'end', bold=True))
        for k, v in enumerate(bits): o.append(T(X(3 - k), y + 5, str(v), 15))
        y += 28
    o.append(L(X(3) - 22, y - 12, X(0) + 22, y - 12, INK, 1.5))
    b = [1, 1, 0, 1]   # b0..b3
    a = [1, 1, 0, 1]   # a3..a0
    y += 14
    for j in range(4):
        on = b[j] == 1
        o.append(T(130, y + 5, f'b{"₀₁₂₃"[j]} = {b[j]}', 14, 'end', fill=INK if on else MUT))
        for k in range(4):
            w = (3 - k) + j
            v = a[k] if on else 0
            o.append(R(X(w) - 17, y - 14, 34, 28, ACS if on else FIGBG, AC if on else L2, 5, 1.5))
            o.append(T(X(w), y + 5, str(v), 15, fill=INK if on else MUT))
        o.append(lbl(690, y + 5, ['= 13', '= 26', '= 0', '= 104'][j], 14, 'end', fill=INK if on else MUT))
        y += 36
    o.append(L(X(7) - 22, y - 14, X(0) + 22, y - 14, INK, 2))
    prod = [1, 0, 0, 0, 1, 1, 1, 1]
    for k, v in enumerate(prod):
        o.append(R(X(7 - k) - 17, y - 6, 34, 28, LVS, LV, 5, 1.5)); o.append(T(X(7 - k), y + 13, str(v), 15, bold=True))
    o.append(T(690, y + 13, '= 143', 14, 'end', bold=True))
    o.append(T(130, y + 13, 'product', 14, 'end', bold=True))
    o.append(lbl(360, y + 52, 'Row j is A shifted j places; the b₂ = 0 row adds nothing. 13 + 26 + 0 + 104 = 143.', 14, fill=INK))
    return y + 70, ''.join(o)


# ---- 4.4 Wallace tree, 8 rows to 2 ----
def f4():
    o = []
    counts = [8, 6, 4, 3, 2]
    groups = [[(0, 3), (3, 6)], [(0, 3), (3, 6)], [(0, 3)], [(0, 3)], []]
    xs = [40, 175, 310, 445, 580]
    top = 60; dy = 22
    for lv, (n, x) in enumerate(zip(counts, xs)):
        y0 = top + (8 - n) * dy / 2
        o.append(T(x + 40, 34, f'{n} rows', 14, bold=True))
        gset = {i for a, b2 in groups[lv] for i in range(a, b2)}
        for i in range(n):
            o.append(R(x, y0 + i * dy, 80, 12, ACS if i in gset else FIGBG, AC if i in gset else L2, 3, 1.5))
        for a, b2 in groups[lv]:
            o.append(brace(x + 88, x + 88, 0) if False else P([(x + 86, y0 + a * dy), (x + 92, y0 + a * dy), (x + 92, y0 + (b2 - 1) * dy + 12), (x + 86, y0 + (b2 - 1) * dy + 12)], AC, 1.8))
            o.append(T(x + 112, y0 + (a + b2 - 1) * dy / 2 + 11, 'CSA', 13, fill=AC, bold=True))
        if lv < 4:
            o.append(T(x + 104, 248, f'level {lv + 1}', 13, fill=MUT))
    o.append(boxt(580, 250, 120, 42, ['final CPA'], fill=LVS, stroke=LV, size=14))
    o.append(L(640, 60 + 3 * dy + 30, 640, 246, LV, 2, arrow='l'))
    o.append(T(360, 318, 'Each CSA turns 3 rows into 2 with no carry chain; leftover rows pass straight on.', 14))
    o.append(T(360, 340, '8 → 6 → 4 → 3 → 2 in four levels, then one carry propagate adder (not a level).', 14, bold=True))
    return 356, ''.join(o)


# ---- 4.5 decoder for f = Σm(1,2,5,7) and the comparator chain ----
def f5():
    o = []
    o.append(T(20, 22, 'Decoder plus OR: f(A, B, C) = Σm(1, 2, 5, 7)', 14, 'start', bold=True))
    o.append(boxt(110, 40, 130, 176, ['3-to-8', 'decoder'], size=15))
    for i, s in enumerate(['A', 'B', 'C']):
        y = 80 + i * 48
        o.append(L(40, y, 108, y, AC, 2, arrow='n')); o.append(T(30, y + 5, s, 14, 'end', bold=True))
    sel = {1, 2, 5, 7}
    for i in range(8):
        y = 52 + i * 21
        o.append(T(254, y + 5, f'Y{i}', 13, 'start', fill=AC if i in sel else MUT, bold=i in sel))
        if i in sel:
            o.append(P([(282, y), (330, y), (380, 128)], AC, 2))
        else:
            o.append(L(282, y, 300, y, L2, 1.5))
    o.append(boxt(380, 104, 70, 48, ['OR'], fill=ACS, size=15))
    o.append(L(450, 128, 500, 128, AC, 2.5, arrow='n')); o.append(T(512, 133, 'f', 15, 'start', bold=True))
    o.append(lbl(560, 70, 'ABC = 101 raises Y5', 13, 'start'))
    o.append(lbl(560, 90, 'so f(1, 0, 1) = 1', 13, 'start'))
    o.append(T(20, 254, 'Magnitude chain from the MSB: A = 1011, B = 1010', 14, 'start', bold=True))
    bits = [(1, 1), (0, 0), (1, 1), (1, 0)]
    flags = ['0, 0, 1', '0, 0, 1', '0, 0, 1', '0, 0, 1', '1, 0, 0']
    for k, (ab, bb) in enumerate(bits):
        x = 130 + k * 140
        o.append(boxt(x, 272, 92, 50, [f'bit {3 - k}', f'{ab} vs {bb}'], fill=ACS if k == 3 else PANEL, size=14))
    for k in range(5):
        x = 130 + k * 140 - 24
        o.append(L(x - 20, 297, x + 22, 297, AC, 2, arrow='n') if k < 4 else L(110 + 4 * 140 + 2, 297, 110 + 4 * 140 + 44, 297, AC, 2, arrow='n'))
    o.append(lbl(68, 344, 'G, L, E in', 13)); o.append(T(68, 362, '0, 0, 1', 13))
    for k in range(1, 4):
        o.append(T(130 + k * 140 - 24, 344, flags[k], 13, fill=MUT))
    o.append(T(672, 344, 'G = 1', 14, bold=True, fill=AC)); o.append(T(672, 362, 'A > B', 14, bold=True, fill=AC))
    o.append(lbl(360, 392, 'Bits 3, 2 and 1 are equal; bit 0 differs with A = 1, so G becomes 1 and stays 1.', 13, fill=INK))
    return 406, ''.join(o)


# ---- 4.6 master-slave register and its waveforms ----
def f6():
    o = []
    o.append(T(30, 50, 'D', 15, 'middle', bold=True)); o.append(L(44, 45, 96, 45, AC, 2, arrow='n'))
    o.append(boxt(100, 20, 190, 52, ['master latch', 'open while CLK = 0'], size=14))
    o.append(L(290, 45, 376, 45, AC, 2, arrow='n')); o.append(Tb(333, 40, 'Qm', 13, bold=True))
    o.append(boxt(380, 20, 190, 52, ['slave latch', 'open while CLK = 1'], fill=ACS, size=14))
    o.append(L(570, 45, 640, 45, AC, 2, arrow='n')); o.append(T(656, 50, 'Q', 15, bold=True))
    o.append(P([(195, 72), (195, 92), (475, 92), (475, 72)], L2, 1.5)); o.append(lbl(335, 108, 'CLK'))
    x0, sc = 90, 50.0
    X = lambda t: x0 + t * sc
    lanes = [('CLK', [(0, 0), (2, 1), (4, 0), (6, 1), (8, 0), (10, 1), (12, 1)]),
             ('D', [(0, 0), (1, 1), (7, 0), (12, 0)]),
             ('Qm', [(0, 0), (1, 1), (8, 0), (12, 0)]),
             ('Q', [(0, 0), (2, 1), (10, 0), (12, 0)])]
    for li, (name, pts) in enumerate(lanes):
        yb = 160 + li * 52; hi = 26
        o.append(T(70, yb - 6, name, 14, 'end', bold=True))
        path = []
        for (t, v), (t2, _) in zip(pts, pts[1:] + [pts[-1]]):
            y = yb - hi * v
            if path: path.append((X(t), path[-1][1]))
            path.append((X(t), y)); path.append((X(t2), y))
        o.append(P(path, AC if name in ('CLK', 'D') else LV, 2.2))
    for t in (2, 6, 10):
        o.append(L(X(t), 124, X(t), 326, L2, 1.2, dash='4 4'))
        o.append(lbl(X(t), 344, 'edge'))
    o.append(lbl(X(7) + 20, 124, 'D falls while CLK = 1; Q waits for the next edge', 13))
    o.append(T(360, 372, 'Q changes only just after rising edges: at the first edge to 1, at the third back to 0.', 14))
    return 388, ''.join(o)


# ---- 4.7 pipelining the multiply-accumulate datapath ----
def f7():
    o = []
    sc = 108.0; x0 = 92
    def bar(y, segs):
        x = x0
        for w, lab, fill, st in segs:
            o.append(R(x, y, w * sc, 34, fill, st, 3, 1.5))
            if lab: o.append(T(x + w * sc / 2, y + 22, lab, 13))
            x += w * sc
        return x
    o.append(T(20, 28, 'No pipeline', 14, 'start', bold=True))
    end = bar(40, [(0.2, '', NXS, NX), (3.0, 'multiply 3.0 ns', PANEL, AC), (1.6, 'add 1.6 ns', PANEL, AC), (0.1, '', NXS, NX)])
    o.append(T(end + 8, 63, 'T = 4.9 ns', 14, 'start', bold=True))
    o.append(T(20, 122, 'Three stages', 14, 'start', bold=True))
    x = x0
    for i, (w, lab) in enumerate([(1.5, 'multiply, part 1'), (1.5, 'multiply, part 2'), (1.6, 'add')]):
        o.append(R(x, 134, 0.2 * sc, 34, NXS, NX, 3, 1.5))
        o.append(R(x + 0.2 * sc, 134, w * sc, 34, ACS, AC, 3, 1.5)); o.append(T(x + (0.2 + w / 2) * sc, 156, lab, 13))
        o.append(R(x + (0.2 + w) * sc, 134, 0.1 * sc, 34, NXS, NX, 3, 1.5))
        x += (0.3 + w) * sc
        o.append(lbl(x - (0.3 + w) * sc / 2, 188, f'{0.3 + w:.1f} ns', 13))
    xs3 = x0 + 3.6 * sc
    o.append(P([(xs3, 200), (xs3, 206), (xs3 + 1.9 * sc, 206), (xs3 + 1.9 * sc, 200)], INK, 1.5))
    o.append(T(xs3 + 0.95 * sc - 40, 226, 'slowest stage sets T = 0.2 + 1.6 + 0.1 = 1.9 ns', 14, bold=True))
    o.append(T(20, 262, 'register overhead: t', 13, 'start', fill=NX))
    o.append(R(160, 252, 14, 12, NXS, NX, 2, 1.5)); o.append(T(184, 262, 'clock-to-Q 0.2 ns and setup 0.1 ns in every stage', 13, 'start', fill=MUT))
    o.append(T(360, 296, 'Throughput 204.1 → 526.3 MHz (2.58 times); latency 4.9 → 3 × 1.9 = 5.7 ns', 14, bold=True))
    return 312, ''.join(o).replace('register overhead: t</text>', 'register overhead</text>')


# ---- 4.8 four-phase handshake ----
def f8():
    o = []
    o.append(boxt(30, 24, 150, 96, ['sender', 'stage'], size=15))
    o.append(boxt(540, 24, 150, 96, ['receiver', 'stage'], size=15))
    o.append(L(180, 46, 536, 46, AC, 2.5, arrow='n')); o.append(Tb(360, 42, 'Req', 14, bold=True, fill=AC))
    o.append(L(540, 72, 184, 72, LV, 2.5, arrow='l')); o.append(Tb(360, 68, 'Ack', 14, bold=True, fill=LV))
    o.append(L(180, 100, 536, 100, L2, 6)); o.append(Tb(360, 104, 'data', 13, fill=MUT))
    x0, sc = 110, 56.0
    X = lambda t: x0 + t * sc
    lanes = [('Req', [(0, 0), (1, 1), (5, 0), (9, 0)], AC), ('Ack', [(0, 0), (3, 1), (7, 0), (9, 0)], LV)]
    for li, (name, pts, col) in enumerate(lanes):
        yb = 196 + li * 64; hi = 30
        o.append(T(90, yb - 8, name, 14, 'end', bold=True))
        path = []
        for (t, v), (t2, _) in zip(pts, pts[1:] + [pts[-1]]):
            y = yb - hi * v
            if path: path.append((X(t), path[-1][1]))
            path.append((X(t), y)); path.append((X(t2), y))
        o.append(P(path, col, 2.4))
    yb = 324
    o.append(T(90, yb - 8, 'data', 14, 'end', bold=True))
    o.append(P([(X(0), yb - 14), (X(0.6), yb - 14)], L2, 2)); o.append(P([(X(5.4), yb - 14), (X(9), yb - 14)], L2, 2))
    o.append(f'<polygon points="{X(0.6):.1f},{yb - 14} {X(0.8):.1f},{yb - 26} {X(5.2):.1f},{yb - 26} {X(5.4):.1f},{yb - 14} {X(5.2):.1f},{yb - 2} {X(0.8):.1f},{yb - 2}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:1.5"/>')
    o.append(T(X(3), yb - 9, 'valid', 13))
    for n, (t, txt) in enumerate([(1, 'Req ↑ data valid'), (3, 'Ack ↑ taken'), (5, 'Req ↓'), (7, 'Ack ↓ ready')], 1):
        o.append(L(X(t), 140, X(t), 334, L2, 1.2, dash='4 4'))
        o.append(f'<circle cx="{X(t):.1f}" cy="146" r="11" style="fill:var(--panel);stroke:var(--accent);stroke-width:1.8"/>')
        o.append(T(X(t), 151, str(n), 13, bold=True))
        o.append(lbl(X(t), 356, txt, 13, fill=INK))
    o.append(T(360, 388, 'Four events per transfer; each one waits for the one before, so no clock is needed.', 14))
    return 404, ''.join(o)


# ---- 4.9 the 6T SRAM cell and the 1T1C DRAM cell ----
def inv(x, y, right=True, c=AC):
    if right:
        pts = f'{x},{y - 16} {x},{y + 16} {x + 28},{y}'
        bub = f'<circle cx="{x + 33}" cy="{y}" r="5" style="fill:var(--fig);stroke:{c};stroke-width:2"/>'
    else:
        pts = f'{x},{y - 16} {x},{y + 16} {x - 28},{y}'
        bub = f'<circle cx="{x - 33}" cy="{y}" r="5" style="fill:var(--fig);stroke:{c};stroke-width:2"/>'
    return f'<polygon points="{pts}" style="fill:var(--panel);stroke:{c};stroke-width:2"/>' + bub


def nmos_h(x, y, c=AC):
    """access transistor drawn as a horizontal switch between (x-20,y) and (x+20,y), gate from above"""
    return (L(x - 20, y, x - 12, y, c, 2) + L(x + 12, y, x + 20, y, c, 2) + L(x - 12, y, x - 12, y - 8, c, 2) + L(x + 12, y, x + 12, y - 8, c, 2)
            + L(x - 12, y - 8, x + 12, y - 8, c, 3) + L(x - 12, y - 15, x + 12, y - 15, c, 2) + L(x, y - 15, x, y - 30, c, 2))


def f9():
    o = []
    o.append(T(190, 22, '6T SRAM cell', 15, bold=True))
    o.append(L(30, 40, 30, 250, AC, 2.5)); o.append(T(30, 268, 'BL', 14, bold=True))
    o.append(L(350, 40, 350, 250, AC, 2.5)); o.append(T(350, 268, 'BLB', 14, bold=True))
    o.append(L(30, 62, 350, 62, NX, 2)); o.append(Tb(190, 58, 'WL', 13, bold=True, fill=NX))
    o.append(nmos_h(70, 130)); o.append(L(70, 100, 70, 62, NX, 1.6))
    o.append(nmos_h(310, 130)); o.append(L(310, 100, 310, 62, NX, 1.6))
    o.append(L(30, 130, 50, 130, AC, 2)); o.append(L(330, 130, 350, 130, AC, 2))
    o.append(inv(160, 110, True)); o.append(inv(220, 170, False))
    o.append(P([(90, 130), (120, 130), (120, 110), (160, 110)], AC, 2))
    o.append(P([(198, 110), (250, 110), (250, 130), (290, 130)], AC, 2))
    o.append(P([(120, 130), (120, 170), (182, 170)], AC, 2)); o.append(P([(250, 130), (250, 170), (220, 170)], AC, 2))
    o.append(Tb(106, 152, 'Q', 13, bold=True)); o.append(Tb(268, 152, 'Q̄', 13, bold=True))
    o.append(lbl(190, 214, 'two cross-coupled inverters', 13, fill=INK)); o.append(lbl(190, 232, 'plus two access transistors', 13, fill=INK))
    o.append(lbl(190, 292, 'read: bitlines precharged to V', 13, fill=INK).replace('V</text>', 'V<tspan baseline-shift="sub" font-size="10">DD</tspan></text>'))
    o.append(lbl(190, 310, 'cell ratio above about 1.2 keeps Q at 0', 13))
    o.append(L(392, 20, 392, 320, L2, 1.2, dash='4 4'))
    o.append(T(560, 22, '1T1C DRAM cell', 15, bold=True))
    o.append(L(450, 40, 450, 250, AC, 2.5)); o.append(T(450, 268, 'BL', 14, bold=True))
    o.append(L(450, 62, 700, 62, NX, 2)); o.append(Tb(640, 58, 'WL', 13, bold=True, fill=NX))
    o.append(nmos_h(530, 130)); o.append(L(530, 100, 530, 62, NX, 1.6)); o.append(L(450, 130, 510, 130, AC, 2))
    o.append(P([(550, 130), (600, 130), (600, 160)], AC, 2))
    o.append(L(584, 160, 616, 160, AC, 3)); o.append(L(584, 170, 616, 170, AC, 3)); o.append(L(600, 170, 600, 196, AC, 2))
    o.append(L(588, 196, 612, 196, L2, 2)); o.append(T(630, 170, 'C', 14, 'start', bold=True).replace('C</text>', 'C<tspan baseline-shift="sub" font-size="10">S</tspan> = 30 fF</text>'))
    o.append(L(450, 210, 480, 210, AC, 2)); o.append(L(480, 200, 480, 220, LV, 3)); o.append(L(490, 200, 490, 220, LV, 3)); o.append(L(490, 210, 500, 210, L2, 2))
    o.append(T(508, 215, 'C', 14, 'start', fill=LV, bold=True).replace('C</text>', 'C<tspan baseline-shift="sub" font-size="10">BL</tspan> = 270 fF</text>'))
    o.append(lbl(560, 292, 'ΔV = (V', 13, fill=INK).replace('ΔV = (V</text>', 'ΔV = (1.2 − 0.6) × 30 ÷ 300</text>'))
    o.append(T(560, 312, '= ±60 mV, then restore', 14, bold=True))
    return 330, ''.join(o)


# ---- 4.10 memory architecture of a 64K x 16 SRAM ----
def f10():
    o = []
    o.append(boxt(190, 26, 400, 30, ['precharge and equalise (1024 bitline pairs)'], fill=FIGBG, stroke=L2, size=13))
    o.append(boxt(190, 62, 400, 150, ['core: 1024 × 1024 cells', '1024 wordlines × 1024 bitline pairs', '64 words of 16 bits in every row'], fill=ACS, size=14))
    o.append(boxt(30, 62, 140, 150, ['row decoder', '10 → 1024', '(two 5-to-32', 'predecoders)'], size=14))
    o.append(L(170, 120, 188, 120, AC, 2, arrow='n'))
    o.append(boxt(190, 218, 400, 34, ['16 column multiplexers, 64:1 each'], size=14))
    o.append(boxt(190, 258, 400, 34, ['16 sense amplifiers and write drivers'], fill=LVS, stroke=LV, size=14))
    o.append(boxt(600, 218, 104, 74, ['column', 'decoder', '6 → 64'], size=13))
    o.append(L(600, 235, 592, 235, AC, 2, arrow='n'))
    o.append(L(390, 292, 390, 322, LV, 2.5, arrow='l')); o.append(T(390, 340, 'data in and out: 16 bits', 14, bold=True))
    o.append(L(100, 300, 100, 216, AC, 2, arrow='n')); o.append(T(100, 318, 'A15 to A6', 13, bold=True)); o.append(lbl(100, 336, '10 row bits'))
    o.append(L(652, 336, 652, 296, AC, 2, arrow='n')); o.append(T(652, 354, 'A5 to A0', 13, bold=True)); o.append(lbl(652, 372, '6 column bits'))
    o.append(boxt(600, 62, 104, 76, ['timing', 'control', 'CE, WE'], fill=NXS, stroke=NX, size=13))
    o.append(P([(652, 138), (652, 152), (592, 152)], NX, 1.6, dash='5 4')); o.append(lbl(652, 168, 'SE, WL on', 13))
    o.append(T(360, 400, '16 address bits = 10 row + 6 column; 1024 × 1024 = 1 Mbit = 64K words × 16 bits', 14, bold=True))
    return 414, ''.join(o)


FIG = {
    1: (f1, 'The 4-bit carry look-ahead adder of worked example 1. Each column forms g and p from its own bits; the look-ahead unit makes all four carries at once, and each sum is one XOR of p and its carry.',
        'Four columns with g and p values, a look-ahead carry unit producing carries c0 to c3 and carry-out 1, and four sum boxes, giving 10001 equals 17.'),
    2: (f2, 'Carry select on a = 1011 and b = 0110. The high block adds both ways while the low block works; the real carry c₂ = 1 then picks the carry-in-1 answer.',
        'Two ripple adders for the high block with carry in 0 and 1, a low-block adder whose carry selects the multiplexers, and the result 10001.'),
    3: (f3, 'The partial products of worked example 1. Each row is the multiplicand gated by one multiplier bit and shifted by its place; the array adds the columns to 10001111 = 143.',
        'Partial product grid for 1101 times 1011: rows 1101 shifted by 0, 1 and 3 places and a zero row, summing to 10001111.'),
    4: (f4, 'A Wallace tree on eight partial-product rows. Each carry save adder turns three rows into two, so four levels leave two rows for the one final adder.',
        'Columns of 8, 6, 4, 3 and 2 bars, with groups of three marked CSA, and a final carry propagate adder.'),
    5: (f5, 'Top: a 3-to-8 decoder and one OR gate make f = Σm(1, 2, 5, 7). Bottom: the comparator chain of worked example 1 passes G, L, E from the most significant bit down until bit 0 decides.',
        'Decoder with outputs Y1, Y2, Y5 and Y7 wired to an OR gate; four comparator cells for 1011 against 1010 ending with G equals 1.'),
    6: (f6, 'A master-slave register and its waveforms. The master follows D while the clock is low; the slave copies it while the clock is high, so Q moves only just after a rising edge.',
        'Master and slave latch blocks, then waveforms of CLK, D, Qm and Q over three clock periods with dashed lines at the rising edges.'),
    7: (f7, 'The datapath of worked example 1, drawn to one time scale. Three stages cut the clock period from 4.9 ns to 1.9 ns, but each stage pays 0.3 ns of register overhead.',
        'One long bar of 4.9 nanoseconds above three stage bars of 1.8, 1.8 and 1.9 nanoseconds including register overhead.'),
    8: (f8, 'The four-phase handshake between two self-timed stages: request up, acknowledge up, request down, acknowledge down. Data must stay valid from event 1 until the receiver has taken it.',
        'Sender and receiver blocks joined by Req, Ack and data wires, with waveforms of Req, Ack and data marked with events 1 to 4.'),
    9: (f9, 'The two read-write cells. The 6T SRAM cell holds its bit in two cross-coupled inverters; the DRAM cell holds it as charge on C<sub>S</sub>, and a read shares that charge with the bitline (worked example 2).',
        'Left: 6T SRAM cell with access transistors to BL and BLB and wordline WL. Right: DRAM cell with one access transistor, storage capacitor 30 fF and bitline capacitance 270 fF.'),
    10: (f10, 'The 64K × 16 SRAM of worked example 1. Ten address bits pick one of 1024 wordlines, six pick one word of 16 bits from the row, and sense amplifiers read the 16 selected bitline pairs.',
         'Block diagram: precharge strip, 1024 by 1024 core, row decoder, column multiplexers, sense amplifiers, column decoder and timing control.'),
}
AFTER = {1: 3, 2: 1, 3: 2, 4: 1, 5: 3, 6: 2, 7: 1, 8: 3, 9: 2, 10: 1}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
