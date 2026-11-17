"""Claude's hand-drawn figures for c-dist-u2 (Parallel and Distributed Computing, unit 2: parallel algorithms), one per
chapter, from each chapter's worked example, plus text fixes (no university names in the books)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def grid(x, y, vals, cs=44, fills=None, size=15, strokes=None):
    o = []
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            f = (fills or {}).get((i, j), PANEL)
            s = (strokes or {}).get((i, j), L2)
            o.append(R(x + j * cs, y + i * cs, cs - 4, cs - 4, f, s, 5))
            o.append(T(x + j * cs + (cs - 4) / 2, y + i * cs + (cs - 4) / 2 + size * 0.36, str(v), size, bold=True))
    return ''.join(o)


# ---- 2.1 transpose by swapping pairs ----
def f1():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    At = [[A[j][i] for j in range(3)] for i in range(3)]
    col = {(0, 1): AC, (1, 0): AC, (0, 2): LV, (2, 0): LV, (1, 2): NX, (2, 1): NX}
    soft = {AC: ACS, LV: LVS, NX: NXS}
    fills = {k: soft[v] for k, v in col.items()}
    o = [T(110, 26, 'A', 16, bold=True), T(560, 26, 'Aᵀ', 16, bold=True)]
    o.append(grid(46, 40, A, 44, fills, strokes=col))
    o.append(grid(496, 40, At, 44, fills, strokes=col))
    o.append(L(200, 106, 470, 106, L2, 2, arrow='m'))
    o.append(T(335, 96, 'one PRAM step', 14, bold=True))
    pairs = [('2 ↔ 4', AC, 'P(0,1)'), ('3 ↔ 7', LV, 'P(0,2)'), ('6 ↔ 8', NX, 'P(1,2)')]
    for i, (s, c, p) in enumerate(pairs):
        y = 136 + i * 26
        o.append(R(250, y - 16, 170, 22, soft[c], c, 5)); o.append(T(335, y, f'{p}: swap {s}', 13))
    o.append(T(110, 196, 'diagonal 1, 5, 9 stays', 13, fill=MUT))
    o.append(T(560, 196, 'row i of Aᵀ = column i of A', 13, fill=MUT))
    o.append(boxt(60, 226, 600, 54, ['3 swapping pairs, each 2 reads + 2 writes:', '6 reads, 6 writes, parallel time 1 step'], PANEL, AC))
    return 300, ''.join(o)
FIG[1] = (f1, 'Each off-diagonal pair gets one processor, and all three pairs, 2 ↔ 4, 3 ↔ 7 and 6 ↔ 8, swap in the same PRAM step while the diagonal stays put: 6 reads and 6 writes in 1 step.',
          'The 3 by 3 matrix A and its transpose side by side, with the three swapped pairs shown in matching colours and the diagonal 1, 5, 9 unchanged.')


# ---- 2.2 one processor per output cell ----
def f2():
    o = [T(20, 26, 'C = A × B with 4 processors, one per cell of C', 15, 'start', bold=True)]
    fA = {(0, 0): ACS, (0, 1): ACS}; sA = {(0, 0): AC, (0, 1): AC}
    fB = {(0, 0): LVS, (1, 0): LVS}; sB = {(0, 0): LV, (1, 0): LV}
    o.append(T(78, 58, 'A', 15, bold=True)); o.append(grid(36, 66, [[2, 1], [3, 4]], 44, fA, strokes=sA))
    o.append(T(140, 112, '×', 20))
    o.append(T(206, 58, 'B', 15, bold=True)); o.append(grid(164, 66, [[5, 6], [7, 8]], 44, fB, strokes=sB))
    o.append(T(268, 112, '=', 20))
    o.append(T(334, 58, 'C', 15, bold=True)); o.append(grid(292, 66, [[17, 20], [43, 50]], 44, {(0, 0): NXS}, strokes={(0, 0): NX}))
    o.append(T(400, 86, 'c₁₁ = row 1 of A · column 1 of B', 14, 'start'))
    o.append(T(400, 108, '= 2×5 + 1×7 = 10 + 7 = 17', 14, 'start', bold=True))
    o.append(T(400, 136, 'each processor: 2 multiplications,', 13, 'start', MUT))
    o.append(T(400, 154, '1 addition → 2 multiply-add steps', 13, 'start', MUT))
    o.append(T(20, 202, 'y = A · x: x is broadcast first, then 2 row processors work at once', 15, 'start', bold=True))
    o.append(boxt(36, 226, 120, 46, ['x = (2, 3)'], NXS, NX, 15))
    for i, (row, s, yv) in enumerate([('row 1: 2, 1', '2×2 + 1×3', 7), ('row 2: 3, 4', '3×2 + 4×3', 18)]):
        y = 216 + i * 54
        o.append(L(158, 249, 268, y + 22, NX, 2, arrow='x'))
        o.append(boxt(272, y, 200, 44, [f'P{i + 1} · {row}'], PANEL, AC, 14))
        o.append(L(474, y + 22, 520, y + 22, AC, 2, arrow='n'))
        o.append(T(528, y + 27, f'y{"₁₂"[i]} = {s} = {yv}', 14, 'start', bold=True))
    return 330, ''.join(o)
FIG[2] = (f2, 'Each of the four processors owns one cell of C and does its own dot product: row 1 of A with column 1 of B gives 2×5 + 1×7 = 17, so C = [[17, 20], [43, 50]] after 2 multiply-add steps. For y = A·x, x = (2, 3) reaches both row processors first, giving y = (7, 18).',
          'Matrices A, B and C with row 1 of A and column 1 of B highlighted to make c11 equals 17; below, the vector x is broadcast to two processors that compute y1 equals 7 and y2 equals 18.')


# ---- 2.3 prefix sums by doubling ----
def f3():
    rows = [[3, 1, 4, 1, 5, 9, 2, 6]]
    for d in (1, 2, 4):
        a = rows[-1]; rows.append([a[i] + (a[i - d] if i >= d else 0) for i in range(8)])
    x0, cw, ch, gap = 130, 66, 34, 72
    o = []
    labels = ['input', 'after d = 1', 'after d = 2', 'after d = 4']
    for r, row in enumerate(rows):
        y = 20 + r * gap
        o.append(T(x0 - 12, y + 16, labels[r], 13, 'end', MUT))
        if r: o.append(T(x0 - 12, y + 33, f'adds a[i − {(1, 2, 4)[r - 1]}]', 12, 'end', MUT))
        for i, v in enumerate(row):
            f = NXS if (r == 3 and i == 7) else (ACS if r and i >= (1, 2, 4)[r - 1] else PANEL)
            o.append(R(x0 + i * cw, y, cw - 8, ch, f, AC if f != PANEL else L2, 5))
            o.append(T(x0 + i * cw + (cw - 8) / 2, y + 22, str(v), 15, bold=True))
        if r:
            d = (1, 2, 4)[r - 1]
            for i in range(d, 8):
                xa = x0 + (i - d) * cw + (cw - 8) / 2; xb = x0 + i * cw + (cw - 8) / 2
                o.append(L(xa, y - gap + ch + 2, xb - 3, y - 3, AC, 1.4, arrow='n'))
    o.append(T(x0, 20 + 4 * gap + 4, '3 steps (log₂ 8). Active additions 7 + 6 + 4 = 17 against 7 sequential: not work-optimal.', 14, 'start'))
    o.append(T(x0 + 7 * cw + (cw - 8) / 2, 20 + 3 * gap + ch + 18, 'total 31', 13, fill=NX, bold=True))
    return 330, ''.join(o)
FIG[3] = (f3, 'Each pass adds the old value d places to the left, with d = 1, 2, 4. After three passes every cell holds its prefix sum and the last cell holds the total, 31.',
          'Four rows of eight cells: the input 3 1 4 1 5 9 2 6, then the array after adding values 1, 2 and 4 places to the left, ending 3 4 8 9 14 23 25 31.')


# ---- 2.4 4-ary search vs binary search ----
def f4():
    a = [3, 8, 12, 17, 21, 25, 29, 34, 38, 42, 47, 51, 55, 60, 66]
    x0, cw = 30, 44
    o = [T(20, 24, 'Find 42 with p = 4 processors (4-ary search)', 15, 'start', bold=True)]

    def row(y, keep=None, probes=(), found=None):
        r = []
        for i, v in enumerate(a):
            inside = keep is None or keep[0] <= i <= keep[1]
            f = NXS if i == found else (ACS if i in probes else PANEL)
            s = NX if i == found else (AC if i in probes else (L2 if inside else LN))
            r.append(R(x0 + i * cw, y, cw - 4, 32, f, s, 4))
            r.append(T(x0 + i * cw + 20, y + 21, str(v), 14, fill=INK if inside else MUT, bold=inside))
            r.append(T(x0 + i * cw + 20, y + 48, str(i), 11, fill=MUT))
        return ''.join(r)
    o.append(T(20, 52, 'step 1: probes at 3, 7, 11 → 17, 34, 51; since 34 < 42 ≤ 51 keep a[8..10]', 13, 'start'))
    o.append(row(62, None, (3, 7, 11)))
    o.append(brace(x0 + 8 * cw, x0 + 11 * cw - 4, 120, NX))
    o.append(T(20, 152, 'step 2: probes at 8, 9 → 38, 42: found at index 9', 13, 'start'))
    o.append(row(162, (8, 10), (8,), 9))
    o.append(T(20, 250, 'Binary search, one processor: 3 comparisons', 15, 'start', bold=True))
    mids = [(7, '34 < 42'), (11, '51 > 42'), (9, '= 42')]
    for j, (m, s) in enumerate(mids):
        x = 40 + j * 220
        o.append(boxt(x, 264, 190, 40, [f'mid {m}: a[{m}] {s}'], NXS if j == 2 else PANEL, NX if j == 2 else L2, 14))
        if j < 2: o.append(L(x + 192, 284, x + 216, 284, L2, 2, arrow='m'))
    o.append(T(20, 336, '4-ary: 2 parallel steps instead of 3, since each step cuts the range into 4 parts, not 2.', 14, 'start'))
    return 350, ''.join(o)
FIG[4] = (f4, 'Four processors probe three positions at once, so one step leaves only a[8..10] and the second step finds 42 at index 9. Binary search with one processor needs 3 comparisons for the same key.',
          'The sorted array of 15 keys drawn twice: first with probes at indexes 3, 7 and 11 and the range 8 to 10 bracketed, then with 42 found at index 9; below, three binary-search comparisons.')


# ---- 2.5 bitonic network on 4 keys ----
def f5():
    ys = [70, 130, 190, 250]
    xs = [120, 260, 420, 580]  # value columns
    vals = [[3, 1, 4, 2], [1, 3, 4, 2], [1, 2, 4, 3], [1, 2, 3, 4]]
    o = []
    for w, y in enumerate(ys):
        o.append(L(70, y, 680, y, L2, 2))
        o.append(T(56, y + 5, f'w{w}', 13, 'end', MUT))
    for c, x in enumerate(xs):
        for w, y in enumerate(ys):
            o.append(f'<circle cx="{x}" cy="{y}" r="17" style="fill:var(--fig);stroke:{L2};stroke-width:1.5"/>')
            o.append(T(x, y + 5, str(vals[c][w]), 15, bold=True))
    o += [T(xs[0], 34, 'input', 13, fill=MUT)] + [T(x, 34, f'after stage {i + 1}', 13, fill=MUT) for i, x in enumerate(xs[1:])]

    def comp(x, a, b, up=False, c=AC):
        y1, y2 = ys[a], ys[b]
        if up: return L(x, y2 - 6, x, y1 + 8, c, 2.5, arrow='l' if c == LV else 'n') + C(x, y2, 5, c)
        return L(x, y1 + 6, x, y2 - 8, c, 2.5, arrow='n') + C(x, y1, 5, c)
    o.append(comp(190, 0, 1)); o.append(comp(190, 2, 3, up=True, c=LV))
    o.append(comp(330, 0, 2)); o.append(comp(352, 1, 3))
    o.append(comp(500, 0, 1)); o.append(comp(500, 2, 3))
    o.append(T(190, 292, 'stage 1', 13, fill=MUT)); o.append(T(341, 292, 'stage 2', 13, fill=MUT)); o.append(T(500, 292, 'stage 3', 13, fill=MUT))
    o.append(T(20, 324, 'arrow = where the larger key goes; the orange comparator on w2, w3 is descending, so 4 stays above 2', 13, 'start'))
    o.append(T(20, 348, 'bitonic: depth 3, 6 comparators · odd-even transposition: depth 4, 6 comparators', 14, 'start', bold=True))
    return 362, ''.join(o)
FIG[5] = (f5, 'Four wires carry the keys left to right through three stages of comparators. Stage 1 makes [1, 3, 4, 2] (the descending comparator keeps 4 above 2), stage 2 makes [1, 2, 4, 3] and stage 3 sorts to [1, 2, 3, 4]: depth 3 with 6 comparators.',
          'A bitonic sorting network on four horizontal wires, with six vertical comparators in three stages and the key values in circles before and after each stage.')


# ---- 2.6 Gaussian elimination: pivot row broadcast, rows update together ----
def f6():
    def mrow(x, y, vals, f=PANEL, s=L2, w=46):
        r = []
        for j, v in enumerate(vals):
            r.append(R(x + j * w + (8 if j == 3 else 0), y, w - 4, 30, f, s, 4))
            r.append(T(x + j * w + (8 if j == 3 else 0) + (w - 4) / 2, y + 20, neg(v), 14, bold=True))
        return ''.join(r)
    o = [T(20, 24, 'Step 1: pivot a₁₁ = 1 is broadcast with row 1; rows 2 and 3 update at the same time', 14, 'start', bold=True)]
    o.append(mrow(40, 46, [1, 1, 1, 6], NXS, NX)); o.append(T(240, 66, 'row 1 (pivot row)', 13, 'start', NX))
    o.append(mrow(40, 92, [2, 1, 3, 13])); o.append(mrow(40, 132, [1, 4, 1, 12]))
    o.append(L(372, 64, 400, 64, NX, 2)); o.append(L(400, 64, 400, 147, NX, 2))
    o.append(L(400, 107, 424, 107, NX, 2, arrow='x')); o.append(L(400, 147, 424, 147, NX, 2, arrow='x'))
    o.append(boxt(428, 90, 120, 34, ['worker 2: m = 2'], ACS, AC, 13)); o.append(boxt(428, 130, 120, 34, ['worker 3: m = 1'], ACS, AC, 13))
    o.append(L(550, 107, 572, 107, AC, 2, arrow='n')); o.append(L(550, 147, 572, 147, AC, 2, arrow='n'))
    o.append(T(578, 112, '0, −1, 1 | 1', 14, 'start', bold=True)); o.append(T(578, 152, '0, 3, 0 | 6', 14, 'start', bold=True))
    o.append(T(20, 204, 'Step 2: pivot a₂₂ = −1, m₃₂ = 3 ÷ (−1) = −3: row 3 + 3 × row 2', 14, 'start', bold=True))
    o.append(mrow(40, 220, [1, 1, 1, 6])); o.append(mrow(40, 256, [0, -1, 1, 1])); o.append(mrow(40, 292, [0, 0, 3, 9], ACS, AC))
    o.append(T(260, 242, 'upper triangle reached', 13, 'start', MUT))
    o.append(T(260, 278, 'back substitution:', 14, 'start', bold=True))
    o.append(T(260, 300, '3z = 9 → z = 3;  −y + 3 = 1 → y = 2;  x + 2 + 3 = 6 → x = 1', 14, 'start'))
    return 330, ''.join(o)
FIG[6] = (f6, 'At step 1 the pivot row (1, 1, 1 | 6) goes to every worker first, then rows 2 and 3 subtract 2 and 1 copies of it in one parallel step. One more step leaves an upper triangle, and back substitution gives z = 3, y = 2, x = 1.',
          'Augmented matrix rows: the pivot row is sent to two workers that update rows 2 and 3 together; below, the triangular matrix after step 2 and the back substitution.')


# ---- 2.7 Borůvka rounds ----
def f7():
    pos = {'A': (70, 90), 'B': (70, 230), 'C': (220, 160), 'D': (330, 80), 'E': (330, 240)}
    E = [('A', 'B', 4), ('A', 'C', 8), ('B', 'C', 11), ('C', 'D', 7), ('C', 'E', 2), ('D', 'E', 9)]
    o = []
    for panel, (dx, title, pick) in enumerate([(0, 'Round 1: every vertex picks its lightest edge', {('A', 'B'), ('C', 'E'), ('C', 'D')}),
                                               (340, 'Round 2: each group picks its lightest edge out', {('A', 'B'), ('C', 'E'), ('C', 'D'), ('A', 'C')})]):
        o.append(T(dx + 20, 24, title, 13, 'start', bold=True))
        if panel == 1:
            o.append(f'<ellipse cx="{dx + 70}" cy="160" rx="38" ry="110" style="fill:var(--live-soft);stroke:{LV};stroke-width:1.5;stroke-dasharray:6 4"/>')
            o.append(f'<ellipse cx="{dx + 280}" cy="160" rx="82" ry="110" style="fill:var(--live-soft);stroke:{LV};stroke-width:1.5;stroke-dasharray:6 4"/>')
        for u, v, w in E:
            (x1, y1), (x2, y2) = pos[u], pos[v]
            new = (u, v) in pick and (panel == 0 or (u, v) == ('A', 'C'))
            old = (u, v) in pick and not new
            c = NX if new else (AC if old else LN)
            o.append(L(dx + x1, y1, dx + x2, y2, c, 4 if new else (3 if old else 1.6), None if (new or old) else '5 4'))
            mx, my = dx + (x1 + x2) / 2, (y1 + y2) / 2
            o.append(Tb(mx + (10 if u == 'A' and v == 'B' else 0), my + 5, str(w), 14, fill=NX if new else (INK if old else MUT), bold=new))
        for n, (x, y) in pos.items():
            o.append(f'<circle cx="{dx + x}" cy="{y}" r="17" style="fill:var(--panel);stroke:{AC};stroke-width:2"/>')
            o.append(T(dx + x, y + 5, n, 15, bold=True))
    o.append(T(20, 300, 'picks A–B 4, C–E 2, C–D 7 → groups {A, B} and {C, D, E}', 13, 'start'))
    o.append(T(360, 300, 'both groups pick A–C 8 → one tree', 13, 'start'))
    o.append(T(20, 330, 'MST = A–B 4 + C–E 2 + C–D 7 + A–C 8 = 21, found in 2 rounds', 14, 'start', bold=True))
    return 345, ''.join(o)
FIG[7] = (f7, 'In round 1 every vertex picks its lightest edge at the same time: A–B 4, C–E 2 and C–D 7, which leaves two groups. In round 2 both groups pick A–C 8, so the spanning tree weighs 21 after 2 rounds.',
          'The same five-vertex weighted graph twice: on the left the three edges picked in round 1, on the right the two groups circled and the edge A to C added in round 2.')


TEXT = {
    4: [('Block split keeps the work near log(n/p), but its speedup', 'Block split keeps the work at O(p log(n/p)), but its speedup')],
    1: [('Only a few universities teach the blocked hypercube version. Assume n = 2<sup>k</sup>.',
         'The blocked hypercube version works on blocks. Assume n = 2<sup>k</sup>.')],
    6: [('Root finding behaves similarly: many intervals or starting points can be tested at once. Only a few universities teach this parallel numerical material.',
         'Root finding behaves similarly: many intervals or starting points can be tested at once.')],
    7: [('This appears in network planning, chip wiring and clustering. Only a few universities teach this at exam depth.',
         'This appears in network planning, chip wiring and clustering.')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}


def text_fixes(k):
    return TEXT.get(k, [])
