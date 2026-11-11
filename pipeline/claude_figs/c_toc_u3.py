"""Claude's hand-drawn figures for c-toc-u3 (Theory of Computation, unit 3: grammars, derivations and parse trees,
ambiguity, simplification, CNF, the pumping lemma for CFLs, closure, CYK and the Chomsky hierarchy), one per chapter,
from each chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def node(x, y, s, c=AC, f=PANEL, r=20, size=15):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{f};stroke:{c};stroke-width:2"/>' + T(x, y + size * 0.36, s, size, fill=c, bold=True)


def leaf(x, y, s, c=NX, size=15):
    w = max(34, tw(s, size) + 14)
    return R(x - w / 2, y - 15, w, 30, NXS, c, 6, 1.6) + T(x, y + 5, s, size, fill=c, bold=True)


def tree(o, N, E, r=20):
    """N: name -> (x, y, label, kind) with kind 'v' (variable) or 't' (terminal); E: (parent, child) pairs"""
    for a, b in E:
        xa, ya = N[a][:2]; xb, yb = N[b][:2]
        o.append(L(xa, ya + r, xb, yb - (15 if N[b][3] == 't' else r), L2, 1.8))
    for k, (x, y, s, kind) in N.items():
        o.append(node(x, y, s) if kind == 'v' else leaf(x, y, s))


def chipm(x, y, s, c=AC, f=ACS, size=15):
    w = max(40, tw(s, size) * 1.08 + 20)
    return R(x - w / 2, y - 17, w, 34, f, c, 8, 2) + TM(x, y + 5, s, size, 'middle', c, True)


# ---- 3.1 S → aSb | ε derives aabb ----
def f1():
    o = []
    o.append(T(20, 32, 'Grammar G:', 14, 'start', MUT, True))
    o.append(TM(110, 32, 'S → aSb | ε', 16, 'start', INK, True))
    steps = ['S', 'a<tspan style="fill:var(--accent)">S</tspan>b', 'aa<tspan style="fill:var(--accent)">S</tspan>bb', 'aabb']
    rules = ['S → aSb', 'S → aSb', 'S → ε']
    xs = [70, 263, 456, 649]
    for i, (x, s) in enumerate(zip(xs, steps)):
        last = i == 3
        w = 104
        o.append(R(x - w / 2, 70, w, 44, NXS if last else PANEL, NX if last else AC, 8, 2))
        o.append(TM(x, 98, s, 18, 'middle', NX if last else INK, True))
        o.append(T(x, 134, 'start' if i == 0 else f'step {i}', 13, fill=MUT))
    for i, r in enumerate(rules):
        x1, x2 = xs[i] + 52, xs[i + 1] - 52
        o.append(L(x1 + 4, 92, x2 - 4, 92, AC, 2, arrow='n'))
        o.append(TM((x1 + x2) / 2, 82, r, 13, 'middle', AC, True))
    o.append(T(649, 156, 'no variable left:', 13, fill=NX, bold=True))
    o.append(T(649, 173, 'aabb is in L(G)', 13, fill=NX, bold=True))
    o.append(L(20, 196, 700, 196, LN, 1))
    o.append(T(20, 224, 'Each step adds one a in front and one b behind, so L(G) = { aⁿbⁿ : n ≥ 0 }.', 14, 'start', INK, True))
    o.append(T(20, 254, 'Strings of length at most 6:', 13, 'start', MUT, True))
    for i, (s, n) in enumerate((('ε', 0), ('ab', 2), ('aabb', 4), ('aaabbb', 6))):
        x = 90 + i * 150
        o.append(chipm(x, 288, s, NX, NXS))
        o.append(T(x, 324, f'length {n}', 13, fill=MUT))
    o.append(T(20, 354, 'That is 4 strings. The next one, aaaabbbb, already has length 8.', 13, 'start', INK))
    return 368, ''.join(o)
FIG[1] = (f1, 'Each rewriting step replaces the one variable S by a rule’s right side; after three steps no variable is left and aabb is in L(G). Each use of S → aSb adds a matching a and b, so the strings of length at most 6 are ε, ab, aabb and aaabbb.',
          'A derivation S, aSb, aaSbb, aabb with each arrow labelled by the rule used, then the four strings ε, ab, aabb, aaabbb with their lengths 0, 2, 4 and 6.')


# ---- 3.2 parse tree for id + id × id in the layered grammar ----
def f2():
    o = []
    N = {'E0': (330, 40, 'E', 'v'), 'E1': (170, 110, 'E', 'v'), 'p': (330, 110, '+', 't'), 'T1': (490, 110, 'T', 'v'),
         'T2': (170, 180, 'T', 'v'), 'F2': (170, 250, 'F', 'v'), 'i1': (170, 320, 'id', 't'),
         'T3': (410, 180, 'T', 'v'), 'm': (490, 180, '×', 't'), 'F4': (570, 180, 'F', 'v'),
         'F3': (410, 250, 'F', 'v'), 'i2': (410, 320, 'id', 't'), 'i3': (570, 250, 'id', 't')}
    E = [('E0', 'E1'), ('E0', 'p'), ('E0', 'T1'), ('E1', 'T2'), ('T2', 'F2'), ('F2', 'i1'), ('T1', 'T3'), ('T1', 'm'),
         ('T1', 'F4'), ('T3', 'F3'), ('F3', 'i2'), ('F4', 'i3')]
    o.append(R(370, 145, 250, 205, ACS, AC, 14, 1.6, '6 4'))
    o.append(T(612, 312, '× is deeper,', 13, 'end', AC, True))
    o.append(T(612, 330, 'so done first', 13, 'end', AC, True))
    tree(o, N, E)
    o.append(T(30, 44, 'E → E + T | T', 14, 'start', MUT, True))
    o.append(T(30, 64, 'T → T × F | F', 14, 'start', MUT, True))
    o.append(T(30, 84, 'F → ( E ) | id', 14, 'start', MUT, True))
    o.append(T(20, 392, 'Read the leaves left to right: id + id × id.', 14, 'start', NX, True))
    o.append(T(20, 416, 'The leftmost and the rightmost derivation (8 steps each) both build this one tree.', 13, 'start', INK))
    return 430, ''.join(o)
FIG[2] = (f2, 'The parse tree for id + id × id: variables are circles, terminals are boxes. The × node sits inside the T below the +, so the multiplication is grouped first, and the leaves read left to right give back the string.',
          'A parse tree with root E → E + T; the left E goes down through T and F to id, the right T → T × F has F → id on both sides; the T × F subtree is boxed as the part done first.')


# ---- 3.3 two parse trees, two values ----
def f3():
    o = []
    def val(x, y, s, c):
        o.append(Tb(x + 34, y + 5, s, 13, 'start', c, True))
    A = {'r': (170, 50, 'E', 'v'), 'a': (70, 125, 'E', 'v'), 'p': (170, 125, '+', 't'), 'b': (270, 125, 'E', 'v'),
         'a1': (70, 205, 'id₁', 't'), 'b1': (205, 205, 'E', 'v'), 'm': (270, 205, '×', 't'), 'b2': (335, 205, 'E', 'v'),
         'i2': (205, 280, 'id₂', 't'), 'i3': (335, 280, 'id₃', 't')}
    EA = [('r', 'a'), ('r', 'p'), ('r', 'b'), ('a', 'a1'), ('b', 'b1'), ('b', 'm'), ('b', 'b2'), ('b1', 'i2'), ('b2', 'i3')]
    B = {'r': (550, 50, 'E', 'v'), 'a': (450, 125, 'E', 'v'), 'm': (550, 125, '×', 't'), 'b': (660, 125, 'E', 'v'),
         'a1': (385, 205, 'E', 'v'), 'p': (450, 205, '+', 't'), 'a2': (515, 205, 'E', 'v'), 'i3': (660, 205, 'id₃', 't'),
         'i1': (385, 280, 'id₁', 't'), 'i2': (515, 280, 'id₂', 't')}
    EB = [('r', 'a'), ('r', 'm'), ('r', 'b'), ('a', 'a1'), ('a', 'p'), ('a', 'a2'), ('b', 'i3'), ('a1', 'i1'), ('a2', 'i2')]
    o.append(L(360, 30, 360, 330, LN, 1.2))
    tree(o, A, EA); tree(o, B, EB)
    val(170, 50, '= 7', NX); val(270, 125, '= 6', AC)
    val(550, 50, '= 9', LV); val(450, 125, '= 3', AC)
    o.append(T(170, 330, 'Tree A: root rule E → E + E', 14, fill=NX, bold=True))
    o.append(T(170, 352, '1 + (2 × 3) = 7', 14, fill=NX, bold=True))
    o.append(T(550, 330, 'Tree B: root rule E → E × E', 14, fill=LV, bold=True))
    o.append(T(550, 352, '(1 + 2) × 3 = 9', 14, fill=LV, bold=True))
    o.append(T(20, 392, 'id₁ = 1, id₂ = 2, id₃ = 3. One string, two trees, two values: E → E + E | E × E | ( E ) | id is ambiguous.', 13, 'start', INK))
    return 408, ''.join(o)
FIG[3] = (f3, 'The same string id + id × id has two parse trees in the grammar E → E + E | E × E | ( E ) | id. With id₁ = 1, id₂ = 2, id₃ = 3, tree A groups 1 + (2 × 3) = 7 and tree B groups (1 + 2) × 3 = 9, so the grammar is ambiguous.',
          'Two parse trees side by side for id + id × id: tree A with E → E + E at the root and value 7, tree B with E → E × E at the root and value 9.')


# ---- 3.4 simplifying the grammar in three passes ----
def f4():
    o = []
    cols = [
        ('Start', [('S → AB | a', 0), ('A → aA | ε', 0), ('B → bB | b', 0), ('C → cC | c', 0), ('D → aDb', 0)], 'nullable set: {A}'),
        ('1 · drop ε-rules', [('S → AB | B | a', 1), ('A → aA | a', 1), ('B → bB | b', 0), ('C → cC | c', 0), ('D → aDb', 0)], 'A erased in place'),
        ('2 · drop unit rules', [('S → AB | a | bB | b', 1), ('A → aA | a', 0), ('B → bB | b', 0), ('C → cC | c', 0), ('D → aDb', 0)], 'S → B copied out'),
        ('3 · drop useless', [('S → AB | a | bB | b', 0), ('A → aA | a', 0), ('B → bB | b', 0), ('C → cC | c', 2), ('D → aDb', 2)], 'C and D deleted'),
    ]
    w, g, x0 = 160, 20, 10
    for i, (h, rows, note) in enumerate(cols):
        x = x0 + i * (w + g)
        last = i == 3
        o.append(R(x, 20, w, 36, NXS if last else ACS, NX if last else AC, 8, 2))
        o.append(T(x + w / 2, 43, h, 13, fill=NX if last else AC, bold=True))
        if i < 3: o.append(L(x + w + 2, 38, x + w + g - 3, 38, AC, 2, arrow='n'))
        o.append(R(x, 66, w, 190, PANEL, L2, 8, 1.4))
        for j, (s, kind) in enumerate(rows):
            y = 98 + j * 34
            c = INK if kind == 0 else (AC if kind == 1 else MUT)
            o.append(T(x + 12, y, s, 14, 'start', c, kind == 1))
            if kind == 2:
                o.append(L(x + 8, y - 4.5, x + 14 + tw(s, 14) * 0.95, y - 4.5, LV, 2))
        o.append(T(x + w / 2, 280, note, 13, fill=LV if i == 3 else MUT, bold=i == 3))
    o.append(T(10, 318, 'D never finishes a string (not generating) and C is never reached from S, so both go.', 13, 'start', INK))
    o.append(T(10, 340, 'Bold rules changed in that pass. The result: 8 productions, no ε-rules, no unit rules,', 13, 'start', INK))
    o.append(T(10, 360, 'no useless symbols, and the same language as at the start.', 13, 'start', INK))
    return 374, ''.join(o)
FIG[4] = (f4, 'The worked example’s grammar goes through the three passes in their fixed order: ε-rules first, unit rules second, useless symbols last. The final grammar keeps 8 productions and generates the same language.',
          'Four columns of rules: the start grammar, then after removing the ε-rule (A nullable), after replacing the unit rule S → B, and after deleting the useless C and D rules.')


# ---- 3.5 S → aSb | ab to Chomsky normal form ----
def f5():
    o = []
    cols = [('Start', ['S → aSb | ab'], 'terminals inside long rules'),
            ('1 · terminals get variables', ['A → a,  B → b', 'S → A S B | A B'], 'S → A S B has 3 symbols'),
            ('2 · split with new X', ['S → A X | A B', 'X → S B', 'A → a,  B → b'], '5 productions, all CNF')]
    w, g, x0 = 220, 20, 10
    for i, (h, rows, note) in enumerate(cols):
        x = x0 + i * (w + g)
        last = i == 2
        o.append(R(x, 20, w, 36, NXS if last else ACS, NX if last else AC, 8, 2))
        o.append(T(x + w / 2, 43, h, 14, fill=NX if last else AC, bold=True))
        if i < 2: o.append(L(x + w + 2, 38, x + w + g - 3, 38, AC, 2, arrow='n'))
        o.append(R(x, 66, w, 112, PANEL, L2, 8, 1.4))
        y0 = 122 - (len(rows) - 1) * 15
        for j, s in enumerate(rows):
            o.append(TM(x + w / 2, y0 + j * 30, s, 15, 'middle', INK, True))
        o.append(T(x + w / 2, 200, note, 13, fill=MUT, bold=True))
    o.append(L(10, 222, 710, 222, LN, 1))
    # before / after trees of the long rule
    B = {'S': (170, 262, 'S', 'v'), 'A': (100, 342, 'A', 'v'), 'S2': (170, 342, 'S', 'v'), 'B': (240, 342, 'B', 'v')}
    tree(o, B, [('S', 'A'), ('S', 'S2'), ('S', 'B')])
    o.append(T(170, 392, 'S → A S B: three on the right', 13, fill=LV, bold=True))
    A_ = {'S': (520, 262, 'S', 'v'), 'A': (460, 330, 'A', 'v'), 'X': (580, 330, 'X', 'v'), 'S2': (530, 398, 'S', 'v'), 'B': (630, 398, 'B', 'v')}
    o.append(f'<circle cx="580" cy="330" r="27" style="fill:none;stroke:var(--next);stroke-width:2;stroke-dasharray:4 3"/>')
    tree(o, A_, [('S', 'A'), ('S', 'X'), ('X', 'S2'), ('X', 'B')])
    o.append(L(300, 330, 400, 330, AC, 2, arrow='n'))
    o.append(T(350, 318, 'split', 13, fill=AC, bold=True))
    o.append(T(640, 334, 'new X', 13, 'start', NX, True))
    o.append(T(530, 440, 'S → A X and X → S B: two each', 13, fill=NX, bold=True))
    return 456, ''.join(o)
FIG[5] = (f5, 'Converting S → aSb | ab: first every terminal inside a long rule gets its own variable, then the three-symbol rule S → A S B is split with a fresh X. The result, S → A X | A B, X → S B, A → a, B → b, has 5 productions.',
          'Three boxes of rules from S → aSb | ab to the final CNF grammar, and below, the tree S → A S B split into S → A X with X → S B.')


# ---- 3.6 pumping a⁵b⁵c⁵ ----
def f6():
    o = []
    cw, x0, y = 40, 60, 40
    s = 'aaaaabbbbbccccc'
    fills = {'a': (ACS, AC), 'b': (NXS, NX), 'c': (LVS, LV)}
    for i, ch in enumerate(s):
        f, c = fills[ch]
        o.append(R(x0 + i * cw, y, cw - 4, 40, f, c, 4, 1.6))
        o.append(TM(x0 + i * cw + 18, y + 26, ch, 17, 'middle', c, True))
    o.append(T(x0 - 12, y + 26, 's =', 15, 'end', INK, True))
    o.append(T(x0 + 15 * cw, y + 26, '|s| = 15', 14, 'start', MUT, True))
    # span last a .. first c = 7 cells
    xa, xc = x0 + 4 * cw, x0 + 10 * cw + 36
    o.append(brace(xa, xc, y + 56, LV))
    o.append(T((xa + xc) / 2, y + 82, 'to touch both a and c, vwx needs at least 7 cells', 13, fill=LV, bold=True))
    # a legal window of 5
    wa, wb = x0 + 3 * cw, x0 + 7 * cw + 36
    o.append(R(wa - 3, y - 6, wb - wa + 6, 52, 'none', INK, 6, 2.2, '6 4'))
    o.append(T((wa + wb) / 2, y - 14, 'one window vwx, |vwx| ≤ 5', 13, fill=INK, bold=True))
    o.append(L(20, 160, 700, 160, LN, 1))
    o.append(T(20, 190, 'So every window misses a whole block. Example: v = one a, x = one b, c untouched.', 14, 'start', INK, True))
    rows = [('i = 1', 'a⁵ b⁵ c⁵', '5, 5, 5', 'in L', NX), ('i = 2', 'a⁶ b⁶ c⁵', '6, 6, 5', 'not in L', LV)]
    for j, (i, w, cnt, verdict, c) in enumerate(rows):
        yy = 230 + j * 40
        o.append(T(40, yy, i, 14, 'start', MUT, True))
        o.append(T(120, yy, 'u vⁱ w xⁱ y = ' + w, 16, 'start', INK, True))
        o.append(T(460, yy, 'counts ' + cnt, 14, 'start', MUT, True))
        o.append(T(600, yy, verdict, 14, 'start', c, True))
    o.append(T(20, 316, 'The untouched block keeps 5 while another grows, so pumping always leaves L: L is not context-free.', 13, 'start', INK))
    return 330, ''.join(o)
FIG[6] = (f6, 'In s = a⁵b⁵c⁵ the window vwx holds at most 5 symbols, but reaching from the last a to the first c takes 7, so every window misses one block. Pumping with i = 2 grows the other counts while that block stays at 5, and the string leaves L.',
          'Fifteen cells aaaaabbbbbccccc with a dashed five-cell window, a bracket showing that the last a to the first c spans 7 cells, and the pumped string a⁶b⁶c⁵ marked not in L.')


# ---- 3.7 union stays context-free, intersection does not ----
def f7():
    o = []
    o.append(f'<ellipse cx="260" cy="170" rx="210" ry="120" style="fill:var(--accent-soft);fill-opacity:0.7;stroke:var(--accent);stroke-width:2"/>')
    o.append(f'<ellipse cx="460" cy="170" rx="210" ry="120" style="fill:var(--next-soft);fill-opacity:0.7;stroke:var(--next);stroke-width:2"/>')
    o.append(T(150, 36, 'L1 = aⁿbⁿcᵐ', 15, fill=AC, bold=True))
    o.append(T(570, 36, 'L2 = aᵐbⁿcⁿ', 15, fill=NX, bold=True))
    for x, y, s in ((140, 150, 'ab'), (140, 190, 'aabbc'), (140, 230, 'abccc')):
        o.append(TM(x, y, s, 15, 'middle', AC, True))
    for x, y, s in ((580, 150, 'bc'), (580, 190, 'abbcc'), (580, 230, 'aaabc')):
        o.append(TM(x, y, s, 15, 'middle', NX, True))
    o.append(T(360, 126, 'overlap', 13, fill=LV, bold=True))
    for y, s in ((154, 'ε'), (180, 'abc'), (206, 'aabbcc'), (232, '…')):
        o.append(TM(360, y, s, 15, 'middle', LV, True))
    o.append(T(360, 314, 'L1 ∩ L2 = { aⁿbⁿcⁿ }: not context-free (pumping lemma, 3.6)', 14, fill=LV, bold=True))
    o.append(L(20, 334, 700, 334, LN, 1))
    o.append(T(20, 362, 'Union: S → S1 | S2 joins the two grammars, 7 variables and 12 productions, still context-free.', 13, 'start', INK))
    o.append(T(20, 384, 'Concatenation: S → S1 S2, 11 productions. Intersection has no such rule, and here it leaves the family.', 13, 'start', INK))
    return 398, ''.join(o)
FIG[7] = (f7, 'L1 and L2 each have a context-free grammar, and a new start rule joins them for the union or the concatenation. Their overlap is aⁿbⁿcⁿ, which is not context-free, so context-free languages are not closed under intersection.',
          'Two overlapping ovals: L1 with ab, aabbc, abccc; L2 with bc, abbcc, aaabc; the overlap holds ε, abc, aabbcc, the language aⁿbⁿcⁿ, marked not context-free.')


# ---- 3.8 CYK table for aab ----
def f8():
    o = []
    cw, ch, gap = 150, 54, 10
    xs0 = 135
    rows = {1: [(1, 1, '{A}'), (2, 2, '{A}'), (3, 3, '{B}')], 2: [(1, 2, '{A}'), (2, 3, '{S}')], 3: [(1, 3, '{S}')]}
    Y = {1: 250, 2: 170, 3: 90}
    pos = {}
    for ln, cells in rows.items():
        for j, (i, k, s) in enumerate(cells):
            x = xs0 + j * (cw + gap) + (ln - 1) * (cw + gap) / 2
            pos[(i, k)] = (x, Y[ln])
            hi = (i, k) in ((1, 2), (3, 3))
            top = (i, k) == (1, 3)
            f, c = (NXS, NX) if top else ((ACS, AC) if hi else (PANEL, L2))
            o.append(R(x, Y[ln], cw, ch, f, c, 6, 2 if (hi or top) else 1.4))
            o.append(T(x + cw / 2, Y[ln] + 22, f'V[{i},{k}]', 13, fill=MUT))
            o.append(TM(x + cw / 2, Y[ln] + 44, s, 16, 'middle', NX if top else (AC if hi else INK), True))
    for j, chs in enumerate('aab'):
        x = xs0 + j * (cw + gap) + cw / 2
        o.append(TM(x, 332, chs, 20, 'middle', INK, True))
        o.append(T(x, 354, f'position {j + 1}', 13, fill=MUT))
    for ln, lab in ((1, 'length 1'), (2, 'length 2'), (3, 'length 3')):
        o.append(T(xs0 - 14, Y[ln] + 33, lab, 13, 'end', MUT, True))
    (x1, y1), (x2, y2), (xt, yt) = pos[(1, 2)], pos[(3, 3)], pos[(1, 3)]
    o.append(L(x1 + cw / 2 + 20, y1, xt + cw / 2 - 20, yt + ch + 3, AC, 2, arrow='n'))
    o.append(L(570, y2, 570, yt + ch / 2, AC, 2))
    o.append(L(570, yt + ch / 2, xt + cw + 4, yt + ch / 2, AC, 2, arrow='n'))
    o.append(T(582, 150, 'split k = 2: A · B', 13, 'start', AC, True))
    o.append(T(582, 168, 'S → AB puts S here', 13, 'start', AC, True))
    o.append(T(xt - 14, yt + 20, 'split k = 1: A · S', 13, 'end', MUT, True))
    o.append(T(xt - 14, yt + 38, 'no rule matches', 13, 'end', MUT, True))
    o.append(T(20, 392, 'S → AB, A → AA | a, B → b.  S is in the top cell V[1,3], so aab is in L(G). 6 cells in all.', 13, 'start', NX, True))
    return 406, ''.join(o)
FIG[8] = (f8, 'CYK fills the table from the bottom: single letters, then pairs, then the whole string aab. In the top cell the split k = 2 pairs V[1,2] = {A} with V[3,3] = {B}, and S → AB puts S there, so aab is accepted.',
          'A triangular table over a, a, b: bottom row {A}, {A}, {B}; middle row V[1,2] = {A}, V[2,3] = {S}; top cell V[1,3] = {S}, with arrows from V[1,2] and V[3,3] showing the split k = 2.')


# ---- 3.9 the four grammar types with one witness each ----
def f9():
    o = []
    rings = [
        (10, 10, 700, 330, PANEL, L2, 'Type 0 · unrestricted, α → β', 'Turing machine', '⟨M, w⟩ with M halting on w', INK),
        (40, 70, 640, 260, ACS, AC, 'Type 1 · context-sensitive, |α| ≤ |β|', 'linear bounded automaton', 'aⁿbⁿcⁿ', AC),
        (70, 130, 580, 190, NXS, NX, 'Type 2 · context-free, A → γ', 'pushdown automaton', 'aⁿbⁿ', NX),
        (100, 190, 520, 120, PANEL, LV, 'Type 3 · regular, A → aB | a', 'finite automaton', 'aᵐbⁿ', LV)]
    for x, y, w, h, f, c, name, mach, wit, tc in rings:
        o.append(R(x, y, w, h, f, c, 18, 2))
        o.append(T(x + 16, y + 26, name, 14, 'start', tc, True))
        o.append(T(x + 16, y + 46, mach, 13, 'start', MUT))
        o.append(TM(x + w - 16, y + 34, wit, 15, 'end', tc, True))
    o.append(T(360, 290, 'each witness sits in its ring and not in the ring inside it', 13, fill=MUT, bold=True))
    return 350, ''.join(o)
FIG[9] = (f9, 'Each ring is one grammar type, with the machine that accepts it; outer rings allow more. The worked example’s four languages are the witnesses: aᵐbⁿ is regular, aⁿbⁿ is context-free but not regular, aⁿbⁿcⁿ is context-sensitive but not context-free, and the halting set is type 0 only.',
          'Four nested rings: type 3 regular with aᵐbⁿ, type 2 context-free with aⁿbⁿ, type 1 context-sensitive with aⁿbⁿcⁿ, type 0 unrestricted with the halting set, each labelled with its rule shape and machine.')


spec = make_spec(FIG)


def text_fixes(k):
    """sentences in the chapter text that describe the figure, rewritten to match the drawing above"""
    return {
        5: [('The figure shows this split.',
             'The figure shows the same split on the worked example’s rule S → A S B, which becomes S → A X and X → S B.')],
    }.get(k, [])
