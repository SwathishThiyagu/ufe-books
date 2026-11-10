"""Claude's hand-drawn figures for c-compiler-u5 (Compiler Design, unit 5: run-time environments), one per chapter, from
each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def badge(x, y, n, c=AC, r=10):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c}"/>' + T(x, y + 4.5, str(n), 12, fill='var(--fig)', bold=True)


def pill(x, y, s, c=AC, fill=ACS, w=None, size=14):
    w = w or tw(s, size) + 22
    return R(x - w / 2, y - 15, w, 30, fill, c, 15, 1.8) + TM(x, y + 5, s, size, bold=True)


# ---- 5.1 activation tree ----
def f1():
    N = {'main': (200, 40, 1), 'a1': (110, 120, 2), 'c2': (300, 120, 6), 'b': (60, 200, 3), 'a0': (170, 200, 5), 'c1': (60, 280, 4)}
    names = {'main': 'main', 'a1': 'a(1)', 'c2': 'c', 'b': 'b', 'a0': 'a(0)', 'c1': 'c'}
    hot = {'main', 'a1', 'b', 'c1'}
    o = []
    for a, b in (('main', 'a1'), ('main', 'c2'), ('a1', 'b'), ('a1', 'a0'), ('b', 'c1')):
        h = a in hot and b in hot
        o.append(L(N[a][0], N[a][1] + 15, N[b][0], N[b][1] - 15, LV if h else L2, 3 if h else 1.6))
    for k, (x, y, n) in N.items():
        h = k in hot
        o.append(pill(x, y, names[k], LV if h else AC, LVS if h else ACS, 76)); o.append(badge(x + 38, y - 14, n))
    o.append(T(30, 330, 'Numbers: the order the activations begin', 13, 'start', AC))
    o.append(T(30, 350, '(left to right, top to bottom = preorder).', 13, 'start', AC))
    xs = 470
    o.append(T(xs + 80, 30, 'Control stack at its deepest', 14, bold=True))
    for i, s in enumerate(['c', 'b', 'a(1)', 'main']):
        y = 50 + i * 54
        o.append(R(xs, y, 160, 48, LVS if i == 0 else PANEL, LV, 4, 1.8))
        o.append(TM(xs + 80, y + 30, s, 15, bold=True))
    o.append(T(xs + 170, 76, '← top', 13, 'start', LV))
    o.append(T(xs + 80, 290, '4 records = the 4 nodes on', 13, fill=LV, bold=True))
    o.append(T(xs + 80, 308, 'the longest path main → a(1) → b → c', 13, fill=LV, bold=True))
    o.append(L(400, 40, 400, 340, LN, 1))
    return 364, ''.join(o)
FIG[1] = (f1, 'Six activations begin in the order main, a(1), b, c, a(0), c. The longest path, main → a(1) → b → c, has 4 nodes, so at most 4 records are on the control stack at once.',
          'An activation tree with main at the root, children a(1) and c, a(1) with children b and a(0), and b with child c, numbered 1 to 6 in the order they begin, beside the control stack holding main, a(1), b and c.')


# ---- 5.2 row-major and column-major address of a[2][1] ----
def f2():
    o = [T(20, 28, 'int a[3][4], base 2000, 4 bytes each', 14, 'start', bold=True)]
    gx, gy, gc = 30, 46, 46
    for i in range(3):
        for j in range(4):
            h = (i, j) == (2, 1)
            o.append(R(gx + j * gc, gy + i * 34, gc, 34, LVS if h else PANEL, LV if h else L2, 0, 1.5))
            o.append(TM(gx + j * gc + gc / 2, gy + i * 34 + 22, f'{i},{j}', 13, fill=LV if h else MUT, bold=h))
    o.append(T(gx + 2 * gc, gy + 3 * 34 + 20, 'row, column', 13, fill=MUT))
    def strip(y, title, order, idx, formula, addr):
        o.append(T(250, y - 10, title, 14, 'start', bold=True))
        o.append(T(250 + 18, y - 10 + 0, '', 13))
        for k, (i, j) in enumerate(order):
            x = 250 + k * 38
            h = (i, j) == (2, 1)
            o.append(R(x, y, 36, 34, LVS if h else (ACS if (i if title[0] == 'R' else j) % 2 == 0 else PANEL), LV if h else L2, 2, 1.2))
            o.append(TM(x + 18, y + 22, f'{i}{j}', 13, fill=LV if h else INK, bold=h))
        o.append(T(250, y + 52, formula, 13, 'start'))
        o.append(T(700, y + 52, addr, 14, 'end', LV, True))
    rm = [(i, j) for i in range(3) for j in range(4)]
    cm = [(i, j) for j in range(4) for i in range(3)]
    strip(60, 'Row-major: whole rows in turn', rm, 9, '(2 × 4 + 1) × 4 = 36 bytes in', '2036')
    strip(170, 'Column-major: whole columns in turn', cm, 5, '(1 × 3 + 2) × 4 = 20 bytes in', '2020')
    o.append(T(360, 272, 'The same element a[2][1] sits 9 cells in by rows but only 5 by columns. Whole array: 3 × 4 × 4 = 48 bytes.', 13))
    return 288, ''.join(o)
FIG[2] = (f2, 'Laid out row by row, a[2][1] is cell 9, at 2000 + 36 = 2036; laid out column by column it is cell 5, at 2000 + 20 = 2020. Either way the array takes 48 bytes.',
          'A 3 by 4 grid with element 2,1 marked, and two strips of the 12 elements in memory, in row-major order with 2,1 at position 9 (address 2036) and column-major order with it at position 5 (address 2020).')


# ---- 5.3 three records of f on the stack, and a free list ----
def f3():
    o = [T(150, 26, 'Stack (grows down)', 14, bold=True)]
    x0, w = 60, 180
    o.append(R(x0, 40, w, 40, PANEL, L2, 0, 1.5)); o.append(T(x0 + w / 2, 65, 'main’s frame', 14, fill=MUT))
    sp = [8000, 7952, 7904, 7856]
    for i in range(3):
        y = 80 + i * 56
        o.append(R(x0, y, w, 56, ACS if i < 2 else LVS, AC if i < 2 else LV, 0, 1.8))
        o.append(T(x0 + w / 2, y + 26, f'f, call {i + 1}', 14, bold=True)); o.append(T(x0 + w / 2, y + 44, '48 bytes', 13, fill=MUT))
    for i, v in enumerate(sp):
        y = 80 + i * 56
        o.append(L(x0 - 6, y, x0 - 22, y, L2, 1.5)); o.append(TM(x0 - 26, y + 5, str(v), 13, 'end', LV if i == 3 else MUT, i == 3))
    o.append(L(x0 + w + 40, 80 + 3 * 56, x0 + w + 4, 80 + 3 * 56, LV, 2.5, arrow='l'))
    o.append(T(x0 + w + 44, 80 + 3 * 56 + 5, 'SP = 7856', 14, 'start', LV, True))
    o.append(T(x0 + w / 2, 276, '3 × 48 = 144 bytes', 14, fill=AC, bold=True))
    xh = 400
    o.append(T(xh + 150, 26, 'Free list, request for 300 bytes', 14, bold=True))
    blocks = [(200, ''), (400, 'first-fit'), (300, 'best-fit'), (600, '')]
    for i, (sz, tag) in enumerate(blocks):
        y = 52 + i * 52
        bw = sz / 600 * 230
        c = LV if tag == 'first-fit' else (NX if tag == 'best-fit' else L2)
        cs = LVS if tag == 'first-fit' else (NXS if tag == 'best-fit' else PANEL)
        o.append(R(xh, y, bw, 40, cs, c, 4, 1.8))
        o.append(T(xh + 10, y + 25, str(sz), 14, 'start', bold=True))
        if tag:
            o.append(R(xh, y, 300 / 600 * 230, 40, 'none', c, 4, 1.5, '4 3'))
            o.append(T(xh + bw + 10, y + 18, tag, 13, 'start', c, True))
            o.append(T(xh + bw + 10, y + 34, f'leaves {sz - 300}', 13, 'start', c))
    o.append(T(xh, 276, 'First-fit takes the first block big enough;', 13, 'start'))
    o.append(T(xh, 294, 'best-fit takes the tightest one.', 13, 'start'))
    return 310, ''.join(o)
FIG[3] = (f3, 'Each call of f pushes a 48-byte record, so SP falls from 8000 to 7952, 7904 and 7856, and the three records take 144 bytes. For a 300-byte heap request, first-fit takes the 400 block (100 left) and best-fit the exact 300 block.',
          'Left, a downward-growing stack with main’s frame and three 48-byte records of f, the stack pointer marked at 8000, 7952, 7904 and 7856; right, free blocks of 200, 400, 300 and 600 bytes with first-fit and best-fit marked.')


# ---- 5.4 activation record of f(int a, int b) ----
def f4():
    rows = [('FP + 12', 'parameter b', 'caller', PANEL, L2), ('FP + 8', 'parameter a', 'caller', PANEL, L2),
            ('FP + 4', 'return address', 'call', PANEL, L2), ('FP + 0', 'old FP (control link)', 'callee', ACS, AC),
            ('FP − 4', 'local x', 'callee', PANEL, L2), ('FP − 8', 'padding (4 bytes)', 'align', FIGBG, LN)]
    x0, w, y0, h = 220, 240, 30, 46
    o = [T(x0 - 20, 22, 'higher addresses', 13, 'end', MUT)]
    for i, (off, s, who, f, c) in enumerate(rows):
        y = y0 + i * h
        o.append(R(x0, y, w, h, f, c, 0, 1.6, '4 3' if who == 'align' else None))
        o.append(T(x0 + w / 2, y + 28, s, 14, bold=off == 'FP + 0', fill=MUT if who == 'align' else INK))
        o.append(TM(x0 - 14, y + 28, off, 14, 'end', AC if off == 'FP + 0' else INK, off == 'FP + 0'))
    o.append(L(x0 + w + 60, y0 + 3 * h + 23, x0 + w + 6, y0 + 3 * h + 23, AC, 2.5, arrow='n'))
    o.append(T(x0 + w + 64, y0 + 3 * h + 28, 'FP', 15, 'start', AC, True))
    o.append(P([(x0 + w + 8, y0 + 2), (x0 + w + 18, y0 + 2), (x0 + w + 18, y0 + 2 * h - 2), (x0 + w + 8, y0 + 2 * h - 2)], NX, 1.8))
    o.append(T(x0 + w + 26, y0 + h + 5, 'placed by the caller', 13, 'start', NX))
    o.append(T(x0 - 20, y0 + 6 * h + 20, 'lower addresses', 13, 'end', MUT))
    o.append(T(x0 + w + 26, y0 + 6 * h - 10, 'stack grows down', 13, 'start', MUT))
    o.append(T(x0 + w / 2, y0 + 6 * h + 44, '5 words × 4 = 20 bytes, rounded up to 24 for an 8-byte boundary', 14, bold=True))
    return y0 + 6 * h + 60, ''.join(o)
FIG[4] = (f4, 'With FP pointing at the saved old FP, the parameters lie above it at FP + 8 and FP + 12 and the local x below at FP − 4. The five words make 20 bytes, padded to 24 so the next record starts on an 8-byte boundary.',
          'An activation record drawn as a column of six slots from parameter b at FP + 12 down to padding at FP − 8, with FP pointing at the saved old FP at FP + 0.')


# ---- 5.5 parameter passing ----
def f5():
    o = [T(20, 26, 'swap(x, y) with x = 3, y = 7: values after the call', 14, 'start', bold=True)]
    modes = [('by value', '3', '7', False), ('by reference', '7', '3', True), ('by value-result', '7', '3', True)]
    for i, (m, x, y, ch) in enumerate(modes):
        bx = 20 + i * 232
        o.append(R(bx, 40, 216, 76, NXS if ch else PANEL, NX if ch else L2, 8, 1.6))
        o.append(T(bx + 108, 62, m, 14, bold=True))
        o.append(TM(bx + 108, 94, f'x = {x}, y = {y}', 16, fill=NX if ch else MUT, bold=True))
    o.append(T(20, 152, 'f(A[i]) with i = 1 and A[1..4] = 10, 20, 30, 40; f sets i = 3, then p = p + 1', 14, 'start', bold=True))
    rows = [('by value', None, 'copy changes, A does not'), ('by reference', 0, 'address of A[1] fixed at the call'), ('by name', 2, 'A[i] re-read after i = 3')]
    for r, (m, k, why) in enumerate(rows):
        y = 172 + r * 52
        o.append(T(124, y + 27, m, 14, 'end', bold=True))
        for j, v in enumerate([10, 20, 30, 40]):
            x = 140 + j * 64
            h = j == k
            o.append(R(x, y, 60, 40, LVS if h else PANEL, LV if h else L2, 4, 1.6))
            o.append(TM(x + 30, y + 26, str(v + 1 if h else v), 15, fill=LV if h else INK, bold=h))
        o.append(T(410, y + 26, why, 13, 'start', LV if k is not None else MUT))
    for j in range(4): o.append(TM(170 + j * 64, 340, f'A[{j + 1}]', 13, fill=MUT))
    return 356, ''.join(o)
FIG[5] = (f5, 'swap only changes x and y when it works on them directly: by reference or by value-result. For f(A[i]), reference adds 1 to A[1], fixed at the call, while call by name re-reads A[i] after i = 3 and changes A[3] instead.',
          'Top, the results of swap(x, y) under call by value, reference and value-result; bottom, the array A after f(A[i]) under value (unchanged), reference (A[1] = 11) and name (A[3] = 31).')


# ---- 5.6 hashed symbol table with chaining ----
def f6():
    o = [T(20, 26, 'h(name) = sum of letter positions mod 11', 14, 'start', bold=True)]
    calc = [('sum', '19 + 21 + 13 = 53', 9), ('max', '13 + 1 + 24 = 38', 5), ('min', '13 + 9 + 14 = 36', 3), ('avg', '1 + 22 + 7 = 30', 8), ('tmp', '20 + 13 + 16 = 49', 5)]
    for i, (n, s, b) in enumerate(calc):
        y = 58 + i * 30
        o.append(TM(20, y, n, 14, 'start', bold=True))
        o.append(T(64, y, s, 13, 'start'))
        o.append(T(290, y, f'→ {b}', 14, 'end', LV if n == 'tmp' else AC, True))
    o.append(T(20, 222, 'tmp lands in 5, already used by max,', 13, 'start', LV))
    o.append(T(20, 240, 'so it is chained after max.', 13, 'start', LV))
    xb, y0, bh = 380, 20, 30
    chain = {3: ['min'], 5: ['max', 'tmp'], 8: ['avg'], 9: ['sum']}
    for k in range(11):
        y = y0 + k * bh
        used = k in chain
        o.append(R(xb, y, 44, bh - 2, ACS if used else PANEL, AC if used else LN, 0, 1.2))
        o.append(TM(xb + 22, y + 19, str(k), 13, fill=AC if used else MUT, bold=used))
        if used:
            x = xb + 44
            for n in chain[k]:
                o.append(L(x, y + 14, x + 26, y + 14, AC if n != 'tmp' else LV, 2, arrow='n' if n != 'tmp' else 'l'))
                o.append(R(x + 30, y + 1, 66, bh - 4, LVS if n == 'tmp' else PANEL, LV if n == 'tmp' else AC, 5, 1.5))
                o.append(TM(x + 63, y + 18, n, 13, bold=True))
                x += 100
    o.append(T(xb + 22, y0 + 11 * bh + 18, 'bucket', 13, fill=MUT))
    return y0 + 11 * bh + 32, ''.join(o)
FIG[6] = (f6, 'Each name is hashed by adding its letter positions and taking the remainder mod 11. sum, max, min and avg land in empty buckets 9, 5, 3 and 8; tmp also hashes to 5, so it is chained after max.',
          'The hash of each of the five names written out, beside eleven buckets 0 to 10 where bucket 3 holds min, 5 holds max followed by tmp, 8 holds avg and 9 holds sum.')


spec = make_spec(FIG)
