"""Claude's hand-drawn figures for c-compiler-u6 (Compiler Design, unit 6: code generation and optimisation), one per
chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def block(x, y, w, name, lines, c=AC, fill=PANEL, size=14):
    h = 34 + 20 * len(lines)
    o = [R(x, y, w, h, fill, c, 8, 1.8), T(x + 10, y + 20, name, 14, 'start', c, True)]
    for i, s in enumerate(lines):
        o.append(TM(x + 12, y + 42 + i * 20, s.replace('  ', '&#160;&#160;'), size, 'start'))
    return ''.join(o), h


def tag(x, y, s, c=NX, fill=NXS, anchor='start'):
    w = tw(s, 13) + 14
    x0 = x if anchor == 'start' else x - w
    return R(x0, y - 13, w, 22, fill, c, 11, 1.3) + T(x0 + w / 2, y + 2, s, 13, fill=c, bold=True)


# ---- 6.1 simple code generator with descriptors ----
def f1():
    rows = [('t1 = a * b', 'LD R0, a', 'a', '—'), ('', 'MUL R0, b', 't1', '—'), ('t2 = c * d', 'LD R1, c', 't1', 'c'), ('', 'MUL R1, d', 't1', 't2'),
            ('t3 = t1 + t2', 'ADD R0, R1', 't3', '—'), ('x = t3', '(no code)', 'x', '—'), ('end of block', 'ST x, R0', 'x', '—')]
    xs = [20, 170, 350, 470, 590, 700]
    heads = ['three-address', 'target code', 'R0 holds', 'R1 holds', 'note']
    o = []
    for j, h in enumerate(heads[:4]): o.append(T((xs[j] + xs[j + 1]) / 2, 28, h, 13, fill=MUT, bold=True))
    notes = ['', '', '', '', 't1, t2 now dead', 'R0 renamed to x', 'memory x updated']
    for i, (src, tgt, r0, r1) in enumerate(rows):
        y = 40 + i * 38
        st = tgt.startswith('ST')
        nc = tgt.startswith('(')
        o.append(R(xs[0], y, xs[5] - xs[0], 34, LVS if st else (ACS if i % 2 == 0 and not nc else PANEL), LV if st else LN, 4, 1.2))
        o.append(TM(xs[0] + 8, y + 22, src, 13, 'start', MUT if src == 'end of block' else INK))
        o.append(TM(xs[1] + 8, y + 22, tgt, 14, 'start', LV if st else (MUT if nc else AC), True))
        o.append(TM((xs[2] + xs[3]) / 2, y + 22, r0, 14, bold=True))
        o.append(TM((xs[3] + xs[4]) / 2, y + 22, r1, 14, fill=MUT if r1 == '—' else INK, bold=r1 != '—'))
        if notes[i]: o.append(T(xs[5] - 8, y + 22, notes[i], 13, 'end', MUT))
    o.append(T(360, 40 + 7 * 38 + 26, '6 target instructions, 2 registers, 1 store.', 15, bold=True))
    return 40 + 7 * 38 + 42, ''.join(o)
FIG[1] = (f1, 'Each three-address instruction becomes one or two target instructions, and the register columns show what R0 and R1 hold after each. x = t3 costs nothing because R0 is simply renamed x; the single store at the end of the block writes x to memory.',
          'A table of the four three-address instructions, the six target instructions they produce, and what registers R0 and R1 hold after each, ending with ST x, R0.')


# ---- 6.2 basic blocks and the flow graph ----
def f2():
    lines = ['i = 1', 't1 = 4 * i', 'if t1 &gt; 100 goto 7', 'A[i] = 0', 'i = i + 1', 'goto 2', 'return']
    leaders = {1, 2, 4, 7}
    o = [T(20, 26, 'Leaders start blocks', 14, 'start', bold=True)]
    for i, s in enumerate(lines):
        n = i + 1
        y = 54 + i * 30
        o.append(T(30, y, str(n), 13, 'start', MUT))
        o.append(TM(52, y, s, 14, 'start'))
        if n in leaders: o.append(tag(14, y - 5, 'L', LV, LVS, 'end') if False else f'<circle cx="16" cy="{y - 5}" r="6" style="fill:var(--live)"/>')
        if n in (2, 4, 7): o.append(L(24, y - 21, 230, y - 21, LV, 1.5, '4 3'))
    o.append(T(20, 280, 'dot = leader: 1, 2, 4, 7', 13, 'start', LV))
    # flow graph
    b1, h1 = block(330, 16, 180, 'B1', ['i = 1'])
    b2, h2 = block(330, 100, 240, 'B2', ['t1 = 4 * i', 'if t1 &gt; 100 goto B4'])
    b3, h3 = block(330, 230, 180, 'B3', ['A[i] = 0', 'i = i + 1', 'goto B2'], LV, LVS)
    b4, h4 = block(600, 230, 100, 'B4', ['return'], NX, NXS)
    o += [b1, b2, b3, b4]
    o.append(L(420, 16 + h1, 420, 96, AC, 2, arrow='n'))
    o.append(L(420, 100 + h2, 420, 226, AC, 2, arrow='n')); o.append(T(428, 205, 'false: i ≤ 25', 13, 'start', AC))
    o.append(L(570, 160, 646, 226, NX, 2, arrow='x')); o.append(T(620, 180, 'true', 13, 'start', NX, True))
    o.append(P([(330, 290), (300, 290), (300, 140), (322, 140)], LV, 2.2))
    o.append(L(300, 140, 326, 140, LV, 2.2, arrow='l'))
    o.append(T(292, 220, 'back', 13, 'end', LV, True)); o.append(T(292, 236, 'edge', 13, 'end', LV, True))
    o.append(T(360, 352, 'B2 → B3 → B2 is the loop: B3 runs 25 times, B2 tests 26 times.', 14, bold=True))
    return 368, ''.join(o)
FIG[2] = (f2, 'Statements 1, 2, 4 and 7 are leaders, so the code splits into four blocks. B2 tests 4 × i &gt; 100, B3 is the body that jumps back to B2, and the loop body runs 25 times before the test sends control to B4.',
          'The seven-line listing cut at leaders 1, 2, 4 and 7, beside the flow graph B1 → B2, B2 → B3 when false, B2 → B4 when true, and the back edge B3 → B2.')


# ---- 6.3 DAG of a basic block ----
def f3():
    N = {'m': (300, 50, '−'), 'x': (420, 140, '*'), 'p': (250, 230, '+'), 'a': (170, 320, 'a'), 'b': (330, 320, 'b'), 'c': (500, 230, 'c')}
    o = []
    for a, b in (('m', 'p'), ('m', 'x'), ('x', 'p'), ('x', 'c'), ('p', 'a'), ('p', 'b')):
        (x1, y1, _), (x2, y2, _) = N[a], N[b]
        k = 22 / ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        o.append(L(x1 + (x2 - x1) * k, y1 + (y2 - y1) * k, x2 - (x2 - x1) * (k + 0.02), y2 - (y2 - y1) * (k + 0.02), L2, 2, arrow='m'))
    for k, (x, y, s) in N.items():
        leaf = k in 'abc'
        if leaf:
            o.append(R(x - 22, y - 16, 44, 32, PANEL, L2, 6, 1.6)); o.append(TM(x, y + 6, s, 15, bold=True))
        else:
            o.append(f'<circle cx="{x}" cy="{y}" r="22" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
            o.append(T(x, y + 6, s, 18, bold=True))
    o.append(tag(330, 52, 'e'))
    o.append(tag(450, 142, 't3, d'))
    o.append(tag(222, 232, 't1, t2', anchor='end'))
    o.append(T(560, 40, 'Built line by line:', 14, 'start', bold=True))
    notes = [('t1 = a + b', 'new + node'), ('t2 = a + b', 'same node: label added'), ('t3 = t1 * c', 'new * node'),
             ('d = t3', 'copy: label added'), ('e = t2 − d', 'new − node')]
    for i, (s, n) in enumerate(notes):
        y = 66 + i * 40
        o.append(TM(560, y, s, 13, 'start'))
        o.append(T(560, y + 17, n, 13, 'start', NX if 'label' in n else MUT))
    o.append(T(360, 376, '6 nodes (3 leaves, 3 operators); 1 common subexpression and 1 copy folded into labels.', 13, bold=True))
    return 392, ''.join(o)
FIG[3] = (f3, 'The second a + b finds the + node already built, so t2 just becomes a second label on it, and d = t3 adds the label d to the * node. The block needs only 6 nodes.',
          'A DAG with leaves a, b and c, a + node labelled t1 and t2, a * node labelled t3 and d with children + and c, and a − node labelled e reading the + and * nodes.')


# ---- 6.4 seven statements to four ----
def f4():
    rows = [('x = 2 * 3', 'fold → x = 6, then never read', None),
            ('y = x + 0', 'propagate, fold → y = 6, never read', None),
            ('a = b + c', 'kept', 'a = b + c'),
            ('d = b + c', 'same b + c → d = a, then unused', None),
            ('e = d * 1', 'd * 1 is d, and d is a → e = a', 'e = a'),
            ('f = i * 2', 'cheaper add instead of multiply', 'f = i + i'),
            ('print(a, e, f)', 'kept', 'print(a, e, f)')]
    o = [T(130, 26, 'before (7)', 14, fill=MUT, bold=True), T(380, 26, 'what happens', 14, fill=MUT, bold=True), T(620, 26, 'after (4)', 14, fill=MUT, bold=True)]
    for i, (a, why, b) in enumerate(rows):
        y = 40 + i * 42
        o.append(T(22, y + 23, str(i + 1), 13, 'start', MUT))
        o.append(R(40, y, 180, 34, PANEL, L2, 5, 1.4)); o.append(TM(52, y + 22, a, 14, 'start'))
        o.append(T(380, y + 22, why, 13, fill=MUT if why == 'kept' else INK))
        if b:
            o.append(R(540, y, 160, 34, NXS, NX, 5, 1.6)); o.append(TM(552, y + 22, b, 14, 'start', bold=True))
        else:
            o.append(R(540, y, 160, 34, FIGBG, LN, 5, 1.2, '4 3')); o.append(T(620, y + 22, 'removed (dead)', 13, fill=LV, bold=True))
    o.append(T(360, 40 + 7 * 42 + 22, 'The printed values never change, so every step is safe.', 14, bold=True))
    return 40 + 7 * 42 + 38, ''.join(o)
FIG[4] = (f4, 'Folding and propagation turn x and y into constants, but nothing reads them, so they are removed as dead code, as is d once e uses a directly. The block shrinks from 7 statements to 4 and prints the same values.',
          'Seven statements on the left, what each pass does to it in the middle, and on the right the four that remain: a = b + c, e = a, f = i + i and print(a, e, f).')


# ---- 6.5 loop optimisation ----
def f5():
    o = []
    b1, h1 = block(20, 40, 300, 'Before', ['for i = 0 to 99 do {', '  t1 = 4 * i', '  t2 = x * y', '  A[t1] = t2', '}'], L2)
    o.append(b1)
    o.append(T(20, 202, 'Inside the loop, 4 * i is a multiply every turn', 13, 'start', LV))
    o.append(T(20, 220, 'and x * y gives the same 3 × 7 = 21 every turn.', 13, 'start', LV))
    o.append(L(330, 110, 396, 110, NX, 2.5, arrow='x'))
    b2, h2 = block(400, 40, 300, 'After', ['t2 = 21   (preheader)', 't1 = 0', 'while t1 ≤ 396 do {', '  A[t1] = t2', '  t1 = t1 + 4', '}'], NX, NXS)
    o.append(b2)
    y = 262
    o.append(T(20, y, 't1 steps by 4:', 14, 'start', bold=True))
    vals = ['0', '4', '8', '12', '…', '392', '396']
    for i, v in enumerate(vals):
        x = 150 + i * 72
        if v == '…':
            o.append(T(x + 30, y + 30, '…', 16, fill=MUT)); continue
        o.append(R(x, y + 8, 60, 34, ACS, AC, 4, 1.4)); o.append(TM(x + 30, y + 30, v, 14, bold=True))
        if i < 6 and vals[i + 1] != '…' and v != '…': o.append(T(x + 66, y + 4, '+4', 13, fill=MUT))
    o.append(T(360, y + 76, '(396 − 0) ÷ 4 + 1 = 100 turns, each storing 21: 100 × 21 = 2100.', 15, bold=True))
    return y + 92, ''.join(o)
FIG[5] = (f5, 'x * y never changes inside the loop, so t2 = 21 moves to the preheader, and the multiply 4 * i becomes a counter t1 that adds 4 each turn. t1 runs 0, 4, …, 396, so the body runs 100 times and stores 2100 in all.',
          'The loop before, with t1 = 4 * i and t2 = x * y inside, and after, with t2 = 21 moved out and t1 stepping by 4 up to 396, above a strip of the values 0, 4, 8, 12, …, 392, 396.')


# ---- 6.6 reaching definitions ----
def f6():
    o = []
    b1, h1 = block(40, 30, 220, 'B1', ['d1: x = 1', 'd2: y = 2'])
    b2, h2 = block(40, 200, 220, 'B2', ['d3: x = 3'])
    b3, h3 = block(420, 120, 240, 'B3', ['d4: z = x + y'], LV, LVS)
    o += [b1, b2, b3]
    o.append(L(150, 30 + h1, 150, 196, AC, 2, arrow='n'))
    o.append(L(260, 70, 416, 140, AC, 2, arrow='n'))
    o.append(L(260, 220, 416, 166, AC, 2, arrow='n'))
    o.append(T(160, 30 + h1 + 30, 'OUT = {d1, d2}', 13, 'start', AC, True))
    o.append(T(318, 86, '{d1, d2}', 13, 'start', AC))
    o.append(T(270, 240, 'OUT[B2] = {d2, d3}', 13, 'start', AC))
    o.append(T(270, 256, 'd3 kills d1', 13, 'start', MUT))
    o.append(T(540, 210, 'IN[B3] = {d1, d2} ∪ {d2, d3}', 13, fill=LV, bold=True))
    o.append(T(540, 228, '= {d1, d2, d3}', 13, fill=LV, bold=True))
    o.append(T(540, 260, 'x comes from d1 (x = 1) or d3 (x = 3),', 13))
    o.append(T(540, 278, 'so x is not a constant at d4.', 13, bold=True))
    o.append(T(40, 300, 'gen: B1 {d1, d2}, B2 {d3}, B3 {d4}', 13, 'start', MUT)); o.append(T(300, 300, 'kill: B1 {d3}, B2 {d1}', 13, 'start', MUT))
    o.append(T(40, 320, 'A second pass changes nothing, so these sets are final.', 13, 'start', MUT))
    return 336, ''.join(o)
FIG[6] = (f6, 'B3 can be reached from B1 directly or through B2, so its IN set is the union of both OUT sets, {d1, d2, d3}. Two different definitions of x reach d4, so x is not a constant there.',
          'A flow graph with B1 defining d1 and d2, B2 defining d3, and both sending their definitions into B3, whose IN set {d1, d2, d3} holds two definitions of x.')


spec = make_spec(FIG)
