"""Claude's hand-drawn figures for c-compiler-u4 (Compiler Design, unit 4: syntax-directed translation, type checking and
intermediate code), one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def badge(x, y, n, c=LV, r=10):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c}"/>' + T(x, y + 4.5, str(n), 12, fill='var(--fig)', bold=True)


def pill(x, y, s, c=AC, fill=ACS, size=14, mono=False, w=None):
    w = w or tw(s, size) + 20
    t = TM(x, y + 5, s, size, bold=True) if mono else T(x, y + 5, s, size, bold=True)
    return R(x - w / 2, y - 15, w, 30, fill, c, 15, 1.8) + t


def leaf(x, y, s, c=L2, size=14):
    w = tw(s, size) + 18
    return R(x - w / 2, y - 14, w, 28, PANEL, c, 5, 1.5) + TM(x, y + 5, s, size, bold=True)


def tree(N, E, o, gap=15):
    for a, b in E:
        o.append(L(N[a][0], N[a][1] + gap, N[b][0], N[b][1] - gap, L2, 1.6))


# ---- 4.1 annotated parse tree of 3 * 4 + 5 ----
def f1():
    N = {'E0': (330, 36), 'E1': (200, 100), 'P': (330, 100), 'T5': (470, 100), 'T12': (200, 164), 'F5': (470, 164),
         'T3': (100, 228), 'S': (200, 228), 'F4': (300, 228), 'd5': (470, 228), 'F3': (100, 292), 'd4': (300, 292), 'd3': (100, 356)}
    E = [('E0', 'E1'), ('E0', 'P'), ('E0', 'T5'), ('E1', 'T12'), ('T5', 'F5'), ('T12', 'T3'), ('T12', 'S'), ('T12', 'F4'),
         ('F5', 'd5'), ('T3', 'F3'), ('F4', 'd4'), ('F3', 'd3')]
    o = []
    tree(N, E, o)
    lab = {'E0': ('E.val = 17', 8), 'E1': ('E.val = 12', 5), 'T5': ('T.val = 5', 7), 'T12': ('T.val = 12', 4), 'F5': ('F.val = 5', 6),
           'T3': ('T.val = 3', 2), 'F4': ('F.val = 4', 3), 'F3': ('F.val = 3', 1)}
    for k, (x, y) in N.items():
        if k in lab:
            s, n = lab[k]
            root = k == 'E0'
            o.append(pill(x, y, s, LV if root else AC, LVS if root else ACS, w=112)); o.append(badge(x + 56, y - 14, n, LV if root else AC))
        else:
            o.append(leaf(x, y, {'P': '+', 'S': '*', 'd5': 'digit 5', 'd4': 'digit 4', 'd3': 'digit 3'}[k]))
    xr = 556
    o.append(T(xr, 220, 'Each val is made', 14, 'start', bold=True))
    o.append(T(xr, 240, 'from its children only,', 14, 'start', bold=True))
    o.append(T(xr, 266, 'so the numbers climb', 13, 'start'))
    o.append(T(xr, 284, 'from the leaves (1)', 13, 'start'))
    o.append(T(xr, 302, 'to the root (8).', 13, 'start'))
    o.append(T(xr, 330, '3 × 4 = 12, 12 + 5 = 17', 13, 'start', LV, True))
    return 378, ''.join(o)
FIG[1] = (f1, 'Every node’s val is computed from its children, so evaluation climbs from the digit leaves to the root: F.val = 3 first and E.val = 17 last, at step 8.',
          'The parse tree of 3 * 4 + 5 with the val attribute written in each node, numbered 1 to 8 in evaluation order from F.val = 3 at the bottom left to E.val = 17 at the root.')


# ---- 4.2 syntax tree vs DAG ----
def f2():
    o = [T(180, 28, 'Syntax tree: 9 nodes', 15, bold=True), T(540, 28, 'DAG: 6 nodes', 15, bold=True)]
    N = {'m': (180, 66), 'x': (110, 136), 'c': (260, 136), 'p1': (60, 206), 'p2': (170, 206),
         'a1': (30, 276), 'b1': (90, 276), 'a2': (140, 276), 'b2': (200, 276)}
    tree(N, [('m', 'x'), ('m', 'c'), ('x', 'p1'), ('x', 'p2'), ('p1', 'a1'), ('p1', 'b1'), ('p2', 'a2'), ('p2', 'b2')], o)
    for k, (x, y) in N.items():
        s = {'m': '−', 'x': '*', 'p1': '+', 'p2': '+'}.get(k)
        if s: o.append(pill(x, y, s, LV if k in ('p1', 'p2') else AC, LVS if k in ('p1', 'p2') else ACS, w=40))
        else: o.append(leaf(x, y, k[0]))
    o.append(T(115, 316, 'a + b is built twice', 13, fill=LV))
    o.append(L(360, 46, 360, 330, LN, 1))
    D = {'m': (540, 66), 'x': (480, 136), 'c': (620, 136), 'p': (480, 220), 'a': (440, 290), 'b': (520, 290)}
    tree(D, [('m', 'x'), ('m', 'c'), ('p', 'a'), ('p', 'b')], o)
    o.append(arc(470, 151, 470, 202, -0.45, AC, 2, 'n')); o.append(arc(490, 151, 490, 202, 0.45, AC, 2, 'n'))
    o.append(T(448, 182, 'left', 13, 'end', AC)); o.append(T(512, 182, 'right', 13, 'start', AC))
    for k, (x, y) in D.items():
        s = {'m': '−', 'x': '*', 'p': '+'}.get(k)
        if s: o.append(pill(x, y, s, NX if k == 'p' else AC, NXS if k == 'p' else ACS, w=40))
        else: o.append(leaf(x, y, k))
    o.append(T(600, 226, 'one shared + node', 13, 'start', NX, True))
    o.append(T(540, 330, '9 − 6 = 3 nodes saved', 13, fill=NX))
    return 346, ''.join(o)
FIG[2] = (f2, 'The syntax tree builds a + b twice, 9 nodes in all. The DAG makes one + node and lets the * use it as both its left and its right child, so it needs only 6 nodes.',
          'Left, the syntax tree of (a + b) * (a + b) − c with two separate + subtrees; right, the DAG where both operands of * point to a single + node with leaves a and b.')


# ---- 4.3 type checking x = a[i] + 1 ----
def f3():
    N = {'as': (360, 40), 'x': (200, 116), 'pl': (500, 116), 'ix': (420, 196), 'one': (600, 196), 'a': (330, 276), 'i': (500, 276)}
    o = []
    tree(N, [('as', 'x'), ('as', 'pl'), ('pl', 'ix'), ('pl', 'one'), ('ix', 'a'), ('ix', 'i')], o, 17)
    def node(k, s, t, hot=False, mono=True, side=0):
        x, y = N[k]
        w = max(64, tw(s) + 24)
        o.append(pill(x, y, s, NX if hot else AC, NXS if hot else ACS, 14, mono, w=w))
        if side: o.append(T(x + side * (w / 2 + 10), y + 5, t, 13, 'start' if side > 0 else 'end', NX if hot else MUT, hot))
        else: o.append(T(x, y + 34, t, 13, fill=NX if hot else MUT, bold=hot))
    node('as', '=', 'int = int ✓', True, side=1)
    node('x', 'x', 'int (declared)')
    node('pl', '+', 'int + int → int ✓', True, side=1)
    node('ix', 'a[i]', 'element type: int', side=-1)
    node('one', '1', 'int')
    node('a', 'a', 'array(10, int)')
    node('i', 'i', 'int (index)')
    o.append(T(30, 350, 'Types are worked out from the leaves up; the two green checks pass, so the statement is type-correct.', 13, 'start', bold=True))
    o.append(T(30, 372, 'Run with i = 3, a[3] = 7: x = 7 + 1 = 8.', 13, 'start', MUT))
    return 386, ''.join(o)
FIG[3] = (f3, 'Each node gets its type from its children: a[i] takes the element type int of array(10, int), int + int is int, and the assignment compares that int with x’s declared int, so the statement is type-correct.',
          'The tree of x = a[i] + 1 with a type under every node: a is array(10, int), i is int, a[i] is int, the sum is int, and the assignment of int to int is checked.')


# ---- 4.4 evaluating postfix with a stack ----
def f4():
    o = [T(30, 30, 'Postfix of 3 + 4 * 2:', 14, 'start', bold=True), TM(210, 30, '3 4 2 * +', 16, 'start', AC, True)]
    toks = ['3', '4', '2', '*', '+']
    stacks = [[3], [3, 4], [3, 4, 2], [3, 8], [11]]
    notes = ['push', 'push', 'push', 'pop 4, 2 → push 8', 'pop 3, 8 → push 11']
    yb = 250
    for i, (t, st, n) in enumerate(zip(toks, stacks, notes)):
        x = 40 + i * 136
        op = t in '*+'
        o.append(boxt(x + 20, 52, 60, 40, [t], LVS if op else PANEL, LV if op else L2, 18, bold_first=True))
        o.append(L(x + 50, 94, x + 50, 112, L2, 1.5, arrow='m'))
        o.append(P([(x + 6, 120), (x + 6, yb), (x + 94, yb), (x + 94, 120)], L2, 2))
        for j, v in enumerate(st):
            y = yb - 6 - (j + 1) * 38
            new = j == len(st) - 1
            o.append(boxt(x + 14, y, 72, 34, [str(v)], (LVS if op else ACS) if new else PANEL, (LV if op else AC) if new else L2, 16, bold_first=new, rx=4))
        o.append(T(x + 50, yb + 24, n, 13, fill=LV if op else MUT, bold=op))
    o.append(T(360, yb + 64, 'One value is left on the stack: the expression is 11.', 15, bold=True))
    return yb + 80, ''.join(o)
FIG[4] = (f4, 'Reading 3 4 2 * + from left to right, numbers are pushed; * pops 4 and 2 and pushes 8, then + pops 3 and 8 and pushes 11, the value of the expression.',
          'Five stack snapshots, one per token of 3 4 2 * +: the stack grows to 3, 4, 2, the * replaces 4 and 2 by 8, and the + replaces 3 and 8 by 11.')


# ---- 4.5 quadruples, triples and indirect triples ----
def f5():
    o = [TM(90 + i * 180, 26, c, 14, bold=True) for i, c in enumerate(['t1 = b * c', 't2 = a + t1', 't3 = t2 − d', 'x = t3'])]
    def table(x0, title, head, rows, widths, hot=()):
        o.append(T(x0, 60, title, 14, 'start', bold=True))
        xs = [x0]
        for w in widths: xs.append(xs[-1] + w)
        for j, h in enumerate(head):
            o.append(T((xs[j] + xs[j + 1]) / 2, 84, h, 13, fill=MUT))
        for i, r in enumerate(rows):
            y = 92 + i * 34
            for j, v in enumerate(r):
                h = (i, j) in hot
                o.append(R(xs[j], y, widths[j], 34, LVS if h else (FIGBG if j == 0 else PANEL), LV if h else LN, 0, 1.2))
                o.append(TM((xs[j] + xs[j + 1]) / 2, y + 22, v, 14, fill=LV if h else (MUT if j == 0 else INK), bold=h))
        return xs
    table(16, 'Quadruples', ['', 'op', 'arg1', 'arg2', 'result'], [['0', '*', 'b', 'c', 't1'], ['1', '+', 'a', 't1', 't2'], ['2', '−', 't2', 'd', 't3'], ['3', '=', 't3', '', 'x']],
          [30, 46, 54, 54, 62], hot={(0, 4), (1, 4), (2, 4)})
    xs = table(300, 'Triples (no result column)', ['', 'op', 'arg1', 'arg2'], [['0', '*', 'b', 'c'], ['1', '+', 'a', '(0)'], ['2', '−', '(1)', 'd'], ['3', '=', 'x', '(2)']],
               [30, 46, 58, 58], hot={(1, 3), (2, 2), (3, 3)})
    o.append(T(300, 252, '(0) means “the value made by row 0”', 13, 'start', LV))
    o.append(T(560, 60, 'Indirect', 14, 'start', bold=True))
    o.append(T(586, 84, 'order', 13, fill=MUT))
    for i in range(4):
        y = 92 + i * 34
        o.append(R(560, y, 52, 34, ACS, AC, 0, 1.2)); o.append(TM(586, y + 22, str(i), 14, fill=AC, bold=True))
        o.append(L(614, y + 17, 660, y + 17, AC, 1.8, arrow='n'))
        o.append(T(666, y + 22, f'row {i}', 13, 'start', MUT))
    o.append(T(560, 252, 'reorder this list,', 13, 'start', AC)); o.append(T(560, 270, 'never renumber rows', 13, 'start', AC))
    o.append(T(360, 304, 'With a = 5, b = 2, c = 3, d = 4: t1 = 6, t2 = 11, t3 = 7, so x = 7.', 14, bold=True))
    return 320, ''.join(o)
FIG[5] = (f5, 'Quadruples name every result (t1, t2, t3); triples drop the result column and refer to a row’s value by its number, such as (0). Indirect triples keep a separate list of row numbers, so code can be reordered without renumbering.',
          'Three tables for x = a + b * c − d: a quadruple table with result column t1 to t3 and x, a triple table where (0), (1) and (2) refer to earlier rows, and an indirect list of row numbers 0 to 3.')


# ---- 4.6 symbol table, address and code for x = a[i] + 1 ----
def f6():
    o = [T(20, 28, 'Symbol table', 14, 'start', bold=True)]
    head = ['name', 'type', 'width', 'address']
    rows = [['a', 'array(0..9, int)', '40', '1000'], ['i', 'int', '4', '—'], ['x', 'int', '4', '—']]
    ws = [50, 150, 56, 70]
    xs = [20]
    for w in ws: xs.append(xs[-1] + w)
    for j, h in enumerate(head): o.append(T((xs[j] + xs[j + 1]) / 2, 50, h, 13, fill=MUT))
    for i, r in enumerate(rows):
        y = 58 + i * 32
        for j, v in enumerate(r):
            hot = i == 0 and j in (2, 3)
            o.append(R(xs[j], y, ws[j], 32, ACS if hot else PANEL, AC if hot else LN, 0, 1.2))
            o.append(TM((xs[j] + xs[j + 1]) / 2, y + 21, v, 13, fill=AC if hot else INK, bold=hot or j == 0))
    o.append(T(20, 178, 'int is 4 bytes; i = 4; a[4] holds 20', 13, 'start', MUT))
    xc = 400
    o.append(T(xc, 28, 'Three-address code', 14, 'start', bold=True))
    code = [('t1 = i * 4', '16'), ('t2 = 1000 + t1', '1016'), ('t3 = *t2', '20'), ('t4 = t3 + 1', '21'), ('x = t4', '21')]
    for i, (s, v) in enumerate(code):
        y = 58 + i * 28
        o.append(TM(xc, y + 4, s, 14, 'start'))
        o.append(T(700, y + 4, f'= {v}', 14, 'end', LV if i == 4 else AC, True))
    # memory strip
    y0, x0, cw = 232, 30, 66
    o.append(T(20, y0 - 14, 'array a in memory', 13, 'start', MUT))
    for k in range(10):
        x = x0 + k * cw
        hot = k == 4
        o.append(R(x, y0, cw - 2, 40, ACS if hot else PANEL, AC if hot else L2, 3, 2 if hot else 1.2))
        o.append(TM(x + cw / 2 - 1, y0 + 25, f'a[{k}]' if not hot else '20', 13 if not hot else 15, fill=AC if hot else MUT, bold=hot))
        if k % 2 == 0 or hot: o.append(T(x + cw / 2 - 1, y0 + 60, str(1000 + 4 * k), 13, fill=AC if hot else MUT, bold=hot))
    o.append(P([(704, 94), (712, 94), (712, 206), (x0 + 4.5 * cw - 1, 206)], AC, 2, '5 4'))
    o.append(L(x0 + 4.5 * cw - 1, 206, x0 + 4.5 * cw - 1, y0 - 4, AC, 2, '5 4', arrow='n'))
    o.append(T(360, y0 + 96, 'Address of a[i] = 1000 + 4 × 4 = 1016; the value there is 20, so x = 21.', 14, bold=True))
    return y0 + 112, ''.join(o)
FIG[6] = (f6, 'The symbol table gives a’s base address 1000 and its 4-byte elements, so t1 = 16 and t2 = 1016 locate a[4]. Loading 20 from there and adding 1 stores x = 21.',
          'A symbol table for a, i and x, the five three-address instructions with their values 16, 1016, 20, 21 and 21, and a strip of the ten elements of a with a[4] at address 1016 holding 20.')


# ---- 4.7 backpatched jumps for if (a < b && c > d) ----
def f7():
    code = [('100', 'if a &lt; b goto 102', 'patched'), ('101', 'goto 106', 'patched'), ('102', 'if c &gt; d goto 104', 'patched'),
            ('103', 'goto 106', 'patched'), ('104', 'x = 1', ''), ('105', 'goto 107', 'patched'), ('106', 'x = 0', ''), ('107', 'next', '')]
    y0, lh = 36, 40
    yl = lambda n: y0 + (n - 100) * lh
    o = []
    for n, s, k in code:
        y = yl(int(n))
        o.append(TM(30, y + 5, n, 14, 'start', MUT))
        o.append(R(76, y - 15, 230, 30, PANEL, L2 if not k else AC, 5, 1.4))
        o.append(TM(88, y + 5, s, 14, 'start', bold=bool(k)))
    def jump(a, b, lane, c, lab=None):
        ya, yb = yl(a), yl(b)
        o.append(P([(308, ya), (lane, ya), (lane, yb)], c, 2))
        o.append(L(lane, yb, 312, yb, c, 2, arrow='n' if c == AC else ('x' if c == NX else 'l')))
    jump(100, 102, 334, AC); jump(102, 104, 352, AC)
    jump(101, 106, 380, LV); jump(103, 106, 410, LV)
    jump(105, 107, 334, AC)
    o.append(T(440, 60, 'true exits', 14, 'start', AC, True))
    o.append(T(440, 80, '100 → 102 → 104 (x = 1)', 13, 'start', AC))
    o.append(T(440, 124, 'false exits', 14, 'start', LV, True))
    o.append(T(440, 144, '101 and 103 → 106 (x = 0)', 13, 'start', LV))
    o.append(T(440, 164, 'a false a &lt; b skips the c &gt; d test', 13, 'start', LV))
    o.append(T(440, 214, 'Blue boxes were emitted', 13, 'start', bold=True))
    o.append(T(440, 232, 'with blank targets (goto _)', 13, 'start'))
    o.append(T(440, 250, 'and filled in later:', 13, 'start'))
    o.append(T(440, 268, 'that is backpatching.', 13, 'start'))
    o.append(T(440, 306, 'falselist {101, 103} → 106', 13, 'start', MUT))
    return yl(107) + 30, ''.join(o)
FIG[7] = (f7, 'The jumps of if (a &lt; b &amp;&amp; c &gt; d) are emitted with blank targets and patched later. A false a &lt; b at 101 jumps straight to 106, so c &gt; d is never tested, and both false exits land on x = 0.',
          'Eight numbered instructions 100 to 107 with jump arrows on the right: 100 to 102 and 102 to 104 for true, 101 and 103 to 106 for false, and 105 to 107 past the else part.')


spec = make_spec(FIG)
