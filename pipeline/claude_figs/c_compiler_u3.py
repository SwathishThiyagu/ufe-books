"""Claude's hand-drawn figures for c-compiler-u3 (Compiler Design, unit 3: bottom-up parsing), one per chapter, from each
chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def itembox(x, y, w, name, items, c=AC, fill=PANEL, size=13):
    h = 28 + 19 * len(items)
    o = [R(x, y, w, h, fill, c, 8, 1.8), T(x + 10, y + 19, name, 14, 'start', c, True)]
    for i, s in enumerate(items):
        o.append(TM(x + 10, y + 39 + i * 19, s, size, 'start'))
    return ''.join(o), h


# ---- 3.1 shift-reduce: stack before each move ----
def f1():
    stacks = [['$'], ['$', 'id'], ['$', 'F'], ['$', 'T'], ['$', 'E'], ['$', 'E', '+'], ['$', 'E', '+', 'id'], ['$', 'E', '+', 'F'],
              ['$', 'E', '+', 'T'], ['$', 'E', '+', 'T', '*'], ['$', 'E', '+', 'T', '*', 'id'], ['$', 'E', '+', 'T', '*', 'F'],
              ['$', 'E', '+', 'T'], ['$', 'E']]
    acts = ['shift', 'F→id', 'T→F', 'E→T', 'shift', 'shift', 'F→id', 'T→F', 'shift', 'shift', 'F→id', 'T→T*F', 'E→E+T', 'accept']
    hand = {1: 1, 2: 1, 3: 1, 6: 1, 7: 1, 10: 1, 11: 3, 12: 3}
    x0, cw, yb, chh = 12, 50, 230, 26
    o = [T(20, 24, 'Stack before each move (bottom $ at the foot); orange = the handle about to be reduced', 13, 'start', MUT)]
    for i, (st, a) in enumerate(zip(stacks, acts)):
        x = x0 + i * cw
        n = hand.get(i, 0)
        for j, s in enumerate(st):
            y = yb - (j + 1) * chh
            h = j >= len(st) - n
            o.append(R(x + 3, y, cw - 6, chh - 2, LVS if h else (PANEL if s != '$' else FIGBG), LV if h else L2, 3, 1.5))
            o.append(TM(x + cw / 2, y + 17, s, 13, fill=LV if h else (MUT if s == '$' else INK), bold=h))
        o.append(T(x + cw / 2, yb + 22, a, 13, fill=LV if n else (NX if a == 'accept' else AC), bold=True))
        o.append(T(x + cw / 2, yb + 42, str(i + 1), 13, fill=MUT))
    o.append(L(x0, yb + 2, x0 + 14 * cw, yb + 2, L2, 1.5))
    o.append(brace(x0 + 10 * cw + 4, x0 + 11 * cw - 4, yb - 6 * chh - 8, LV, up=True))
    o.append(T(x0 + 10.5 * cw, yb - 6 * chh - 16, 'depth 6', 13, fill=LV, bold=True))
    o.append(T(360, yb + 76, '5 shifts and 8 reductions; T * F and then E + T are each reduced as one handle.', 14, bold=True))
    return yb + 92, ''.join(o)
FIG[1] = (f1, 'Each column is the stack just before one move. A shift pushes the next token; a reduction replaces the handle on top (orange) by the left side of its rule, so id + id * id needs 5 shifts and 8 reductions.',
          'Fourteen stack snapshots side by side for parsing id + id * id, with the handle cells marked before each of the eight reductions and the move written under each column.')


# ---- 3.2 LR(0) automaton ----
def f2():
    o = []
    b0, h0 = itembox(20, 116, 140, 'I0', ['S′→.S', 'S→.CC', 'C→.cC', 'C→.d'])
    b1, _ = itembox(250, 14, 120, 'I1 accept', ['S′→S.'], NX, NXS)
    b2, h2 = itembox(250, 116, 140, 'I2', ['S→C.C', 'C→.cC', 'C→.d'])
    b5, _ = itembox(520, 130, 140, 'I5 reduce 1', ['S→CC.'], NX, NXS)
    b3, h3 = itembox(250, 290, 140, 'I3', ['C→c.C', 'C→.cC', 'C→.d'])
    b4, _ = itembox(520, 232, 140, 'I4 reduce 3', ['C→d.'], NX, NXS)
    b6, _ = itembox(520, 330, 140, 'I6 reduce 2', ['C→cC.'], NX, NXS)
    o += [b0, b1, b2, b5, b3, b4, b6]
    def lab(x, y, s): o.append(Tb(x, y, s, 14, fill=AC, bold=True))
    o.append(L(160, 140, 246, 50, AC, 2, arrow='n')); lab(196, 88, 'S')
    o.append(L(160, 160, 246, 160, AC, 2, arrow='n')); lab(203, 165, 'C')
    o.append(L(110, 214, 246, 318, AC, 2, arrow='n')); lab(160, 270, 'c')
    o.append(L(160, 206, 516, 254, AC, 2, arrow='n')); lab(470, 254, 'd')
    o.append(L(390, 160, 516, 160, AC, 2, arrow='n')); lab(455, 165, 'C')
    o.append(L(330, 189, 330, 286, AC, 2, arrow='n')); lab(345, 270, 'c')
    o.append(L(390, 186, 516, 244, AC, 2, arrow='n')); lab(448, 208, 'd')
    o.append(L(390, 310, 516, 262, AC, 2, arrow='n')); lab(450, 300, 'd')
    o.append(L(390, 350, 516, 352, AC, 2, arrow='n')); lab(455, 356, 'C')
    o.append(f'<path d="M270,{290 + h3:.1f} C255,{290 + h3 + 44:.1f} 315,{290 + h3 + 44:.1f} 300,{290 + h3 + 3:.1f}" style="fill:none;stroke:var(--accent);stroke-width:2" marker-end="url(#ar-UID-n)"/>')
    lab(286, 290 + h3 + 42, 'c')
    o.append(T(20, 420, '7 states, no conflict: LR(0)', 14, 'start', bold=True))
    return 436, ''.join(o)
FIG[2] = (f2, 'Closure of S′ → .S gives I0, and goto on S, C, c and d reaches the other six item sets. The green states hold one finished item each, so they reduce on every symbol without a conflict.',
          'Seven LR(0) item sets I0 to I6 joined by goto arrows labelled S, C, c and d, with I1 the accept state and I4, I5 and I6 the reduce states.')


# ---- 3.3 SLR(1) table ----
def f3():
    cols = ['id', '+', '$', 'E', 'T']
    tab = {0: {'id': 's3', 'E': '1', 'T': '2'}, 1: {'+': 's4', '$': 'acc'}, 2: {'+': 'r2', '$': 'r2'}, 3: {'+': 'r3', '$': 'r3'},
           4: {'id': 's3', 'T': '5'}, 5: {'+': 'r1', '$': 'r1'}}
    x0, y0, cw, ch = 70, 60, 78, 38
    o = [T(x0 + 1.5 * cw, 24, 'ACTION', 14, bold=True), T(x0 + 4 * cw, 24, 'GOTO', 14, bold=True)]
    for j, c in enumerate(cols): o.append(TM(x0 + j * cw + cw / 2, y0 - 10, c, 15, bold=True))
    for i in range(6):
        y = y0 + i * ch
        o.append(T(x0 - 12, y + ch / 2 + 5, f'I{i}', 14, 'end', bold=True))
        for j, c in enumerate(cols):
            v = tab[i].get(c, '')
            kind = 'r' if v.startswith('r') else ('s' if v.startswith('s') else ('a' if v == 'acc' else ('g' if v else '')))
            fill, st = {'r': (NXS, NX), 's': (ACS, AC), 'a': (LVS, LV), 'g': (PANEL, L2), '': (PANEL, LN)}[kind]
            o.append(R(x0 + j * cw, y, cw, ch, fill, st, 0, 1.2))
            if v: o.append(TM(x0 + j * cw + cw / 2, y + ch / 2 + 5, v, 14, fill=INK, bold=kind in 'ra'))
    o.append(L(x0 + 3 * cw, y0 - 30, x0 + 3 * cw, y0 + 6 * ch, INK, 2))
    xr = 500
    o.append(T(xr, 70, 'Rules', 14, 'start', bold=True))
    for i, s in enumerate(['1  E → E + T', '2  E → T', '3  T → id']):
        o.append(TM(xr, 96 + i * 22, s, 14, 'start'))
    o.append(T(xr, 180, 'FOLLOW(E) = {+, $}', 14, 'start', NX, True))
    o.append(T(xr, 200, 'FOLLOW(T) = {+, $}', 14, 'start', NX, True))
    o.append(T(xr, 226, 'so every reduce (green)', 13, 'start'))
    o.append(T(xr, 244, 'goes under + and $ only', 13, 'start'))
    o.append(T(x0, y0 + 6 * ch + 32, '6 states: 3 shifts, 6 reduces, 1 accept, 3 gotos, and no cell holds two moves.', 14, 'start', bold=True))
    return y0 + 6 * ch + 48, ''.join(o)
FIG[3] = (f3, 'SLR puts a reduce only under the tokens in FOLLOW of the rule’s left side. FOLLOW(E) and FOLLOW(T) are both {+, $}, so r1, r2 and r3 sit under + and $ only and no cell gets two moves.',
          'An SLR(1) table for states I0 to I5 with ACTION columns id, +, $ and GOTO columns E, T, showing shifts, reduces r1 to r3 under + and $, and accept in I1 under $.')


# ---- 3.4 the conflict SLR has and LR(1) does not ----
def f4():
    o = []
    def panel(x, title, items, eq, eqc, dl):
        o.append(T(x + 165, 28, title, 15, bold=True))
        b, h = itembox(x + 20, 42, 290, 'state I2', items, AC, PANEL, 14)
        o.append(b)
        y = 42 + h + 20
        o.append(T(x + 30, y + 14, 'next token', 13, 'start', MUT))
        for i, (tok, txt, c, cs) in enumerate((('=', eq, eqc, LVS if eqc == LV else ACS), ('$', dl, NX, NXS))):
            yy = y + 24 + i * 56
            o.append(TM(x + 46, yy + 28, tok, 18, bold=True))
            o.append(boxt(x + 80, yy, 230, 46, txt, cs, c, 13, bold_first=True))
    panel(10, 'SLR', ['S → L . = R', 'R → L .'], ['shift 6  AND  reduce R → L', 'because = is in FOLLOW(R)'], LV, ['reduce R → L'])
    panel(370, 'LR(1)', ['[S → L . = R, $]', '[R → L ., $]'], ['shift 6 only'], AC, ['reduce R → L', 'its lookahead is $'])
    o.append(L(360, 20, 360, 280, LN, 1))
    o.append(T(175, 298, '1 shift/reduce conflict', 14, fill=LV, bold=True))
    o.append(T(545, 298, '0 conflicts', 14, fill=NX, bold=True))
    return 314, ''.join(o)
FIG[4] = (f4, 'SLR reduces R → L on every token in FOLLOW(R) = {=, $}, which clashes with the shift on =. The LR(1) item carries only the lookahead $, so the reduce moves to the $ column and = is a plain shift.',
          'Two versions of state I2: under SLR the = entry holds both shift 6 and reduce R → L, a conflict; under LR(1) the items carry lookahead $, so = only shifts and the reduce is under $.')


# ---- 3.5 merging two LR(1) states into one LALR state ----
def f5():
    o = []
    b, _ = itembox(20, 30, 210, 'I5 (after a, c)', ['A → c. , d', 'B → c. , e'], AC); o.append(b)
    b, _ = itembox(20, 150, 210, 'I8 (after b, c)', ['B → c. , d', 'A → c. , e'], AC); o.append(b)
    o.append(T(125, 254, 'same core {A → c., B → c.}', 13, fill=MUT))
    o.append(T(125, 272, 'no conflict in either', 13, fill=NX, bold=True))
    o.append(L(234, 70, 300, 120, AC, 2.5, arrow='n')); o.append(L(234, 186, 300, 136, AC, 2.5, arrow='n'))
    o.append(T(268, 82, 'merge', 13, 'start', AC, True))
    b, _ = itembox(306, 88, 196, 'LALR state I58', ['A → c. , d/e', 'B → c. , d/e'], LV, LVS); o.append(b)
    xt = 530
    o.append(T(xt + 85, 50, 'what I58 does', 13, fill=MUT))
    for i, tok in enumerate(('d', 'e')):
        y = 70 + i * 74
        o.append(TM(xt + 8, y + 36, tok, 18, bold=True))
        o.append(boxt(xt + 30, y, 150, 60, ['reduce A → c', 'reduce B → c'], LVS, LV, 13))
    o.append(T(xt + 105, 238, '2 reduce/reduce', 14, fill=LV, bold=True))
    o.append(T(xt + 105, 256, 'conflict cells', 14, fill=LV, bold=True))
    o.append(T(360, 306, 'Merging joins the lookaheads: 4 reduce entries, 2 in each of the d and e cells.', 14, bold=True))
    return 322, ''.join(o)
FIG[5] = (f5, 'I5 and I8 have the same core, so LALR merges them and unites their lookaheads. Each item now reduces on both d and e, which puts two reductions in each of those cells: 2 reduce/reduce conflicts.',
          'Two LR(1) states with items A → c. and B → c. carrying different lookaheads merge into one LALR state with lookaheads d/e, whose d and e entries each hold two reductions.')


# ---- 3.6 building and running the calculator ----
def f6():
    o = []
    o.append(boxt(14, 30, 110, 40, ['calc.y'], PANEL, L2, 14, bold_first=True))
    o.append(L(126, 50, 160, 50, AC, 2, arrow='n'))
    o.append(boxt(164, 30, 100, 40, ['yacc -d'], ACS, AC, 14, bold_first=True))
    o.append(L(266, 50, 300, 50, AC, 2, arrow='n'))
    o.append(boxt(304, 14, 120, 34, ['y.tab.c'], PANEL, AC, 13))
    o.append(boxt(304, 54, 120, 34, ['y.tab.h'], PANEL, AC, 13))
    o.append(boxt(14, 112, 110, 40, ['calc.l'], PANEL, L2, 14, bold_first=True))
    o.append(L(126, 132, 160, 132, AC, 2, arrow='n'))
    o.append(boxt(164, 112, 100, 40, ['lex'], ACS, AC, 14, bold_first=True))
    o.append(L(266, 132, 300, 132, AC, 2, arrow='n'))
    o.append(boxt(304, 114, 120, 36, ['lex.yy.c'], PANEL, AC, 13))
    o.append(L(364, 88, 364, 112, L2, 1.5, '3 3'))
    o.append(T(372, 104, 'token codes', 13, 'start', MUT))
    o.append(L(426, 31, 470, 76, AC, 2, arrow='n')); o.append(L(426, 132, 470, 96, AC, 2, arrow='n'))
    o.append(boxt(474, 66, 80, 40, ['cc'], ACS, AC, 14, bold_first=True))
    o.append(L(556, 86, 590, 86, AC, 2, arrow='n'))
    o.append(boxt(594, 66, 110, 40, ['./calc'], NXS, NX, 15, bold_first=True))
    o.append(R(20, 180, 330, 124, 'var(--ink)', 'var(--ink)', 8, 1))
    for i, (s, c) in enumerate((('$ ./calc', 'var(--fig)'), ('2+3*4', 'var(--fig)'), ('14', 'var(--next-soft)'), ('(2+3)*4', 'var(--fig)'), ('20', 'var(--next-soft)'))):
        o.append(TM(36, 204 + i * 21, s, 14, 'start', c, c != 'var(--fig)'))
    o.append(T(380, 200, 'Why 2+3*4 is 14:', 14, 'start', bold=True))
    o.append(T(380, 224, 'after 2+3 the next token is *.', 13, 'start'))
    o.append(T(380, 244, '%left * has level 2, above + at level 1,', 13, 'start'))
    o.append(T(380, 264, 'so the parser shifts and does 3*4 first.', 13, 'start'))
    o.append(T(380, 292, '(2+3)*4: the brackets force 5 × 4 = 20.', 13, 'start', NX, True))
    return 320, ''.join(o)
FIG[6] = (f6, 'yacc -d turns calc.y into y.tab.c and y.tab.h, lex turns calc.l into lex.yy.c, and cc links them into ./calc. Because * is declared above +, the line 2+3*4 prints 14, and (2+3)*4 prints 20.',
          'A build chain from calc.y through yacc -d and calc.l through lex, joined by cc into ./calc, beside a terminal where 2+3*4 prints 14 and (2+3)*4 prints 20.')


spec = make_spec(FIG)
