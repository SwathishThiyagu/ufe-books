"""Claude's hand-drawn figures for c-compiler-u2 (Compiler Design, unit 2: syntax analysis and top-down parsing), one per
chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def badge(x, y, n, c=LV, r=10):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c}"/>' + T(x, y + 4.5, str(n), 12 if r < 11 else 13, fill='var(--fig)', bold=True)


def nt(x, y, s, c=AC, fill=ACS, w=None):
    """a nonterminal node"""
    w = w or max(40, tw(s, 15) + 18)
    return R(x - w / 2, y - 15, w, 30, fill, c, 15, 1.8) + T(x, y + 5, s, 15, bold=True)


def term(x, y, s, c=INK):
    return R(x - 22, y - 14, 44, 28, PANEL, L2, 5, 1.5) + TM(x, y + 5, s, 14, fill=c, bold=True)


def chips(x, y, items, hot=(), size=14, gap=6):
    """a row of small symbol chips; items in hot are drawn in the live colour"""
    o = []
    for s in items:
        w = max(28, tw(s, size) + 14)
        h = s in hot
        o.append(R(x, y - 17, w, 24, LVS if h else PANEL, LV if h else L2, 12, 1.5))
        o.append(TM(x + w / 2, y, s, size, fill=LV if h else INK, bold=True))
        x += w + gap
    return ''.join(o)


# ---- 2.1 the parser stops at the first wrong token ----
def f1():
    o = [T(30, 30, 'Grammar D → type id = num ;  expects five tokens in this order:', 14, 'start', bold=True)]
    exp = ['type', 'id', '=', 'num', ';']
    x0, cw = 200, 100
    for i, s in enumerate(exp):
        o.append(T(x0 + i * cw + 44, 58, f'position {i + 1}', 13, fill=MUT))
        o.append(boxt(x0 + i * cw, 66, 88, 36, [s], ACS, AC, 15, bold_first=True))
    o.append(T(x0 - 14, 90, 'expected', 14, 'end', AC, True))
    good = [('type', 'int'), ('id', 'x'), ('assign', '='), ('num', '3'), ('semi', ';')]
    bad = [('type', 'int'), ('assign', '='), ('num', '3'), ('semi', ';')]
    def row(y, label, code, toks, err):
        o.append(TM(x0 - 14, y + 22, code, 14, 'end', bold=True))
        o.append(T(x0 - 14, y + 40, label, 13, 'end', MUT))
        for i, (k, lx) in enumerate(toks):
            x = x0 + i * cw
            st = 'ok' if err is None or i < err else ('err' if i == err else 'skip')
            fill, c = {'ok': (NXS, NX), 'err': (LVS, LV), 'skip': (PANEL, LN)}[st]
            o.append(R(x, y, 88, 50, fill, c, 6, 2 if st == 'err' else 1.5))
            o.append(TM(x + 44, y + 22, lx, 15, fill=INK if st != 'skip' else MUT, bold=True))
            o.append(T(x + 44, y + 41, k, 13, fill=MUT))
    row(128, '5 tokens', 'int x = 3;', good, None)
    row(206, '4 tokens', 'int = 3;', bad, 1)
    o.append(T(x0 + 44, 276, 'match', 13, fill=NX, bold=True))
    o.append(T(x0 + cw + 44, 276, 'error: wanted id', 13, fill=LV, bold=True))
    o.append(T(x0 + 2.5 * cw + 44, 276, 'never read', 13, fill=MUT))
    o.append(T(360, 318, 'The first syntax error is reported at token position 2, the = sign.', 15, bold=True))
    return 334, ''.join(o)
FIG[1] = (f1, 'The parser compares each token with what the grammar expects next. int x = 3; matches all five, but in int = 3; the second token is = where an id was expected, so the error is reported at position 2.',
          'Five expected token kinds type, id, =, num and semicolon, above the good stream int x = 3; matching all five and the bad stream int = 3; failing at position 2.')


# ---- 2.2 parse tree numbered by derivation step ----
def f2():
    N = {'E1': (270, 40, 'E', 1), 'E2': (120, 110, 'E', 2), 'P': (270, 110, '+', 0), 'T5': (420, 110, 'T', 5),
         'T3': (120, 180, 'T', 3), 'T6': (340, 180, 'T', 6), 'S': (420, 180, '*', 0), 'F8': (500, 180, 'F', 8),
         'F4': (120, 250, 'F', 4), 'F7': (340, 250, 'F', 7), 'i3': (500, 250, 'id', 0),
         'i1': (120, 320, 'id', 0), 'i2': (340, 320, 'id', 0)}
    E = [('E1', 'E2'), ('E1', 'P'), ('E1', 'T5'), ('E2', 'T3'), ('T3', 'F4'), ('F4', 'i1'), ('T5', 'T6'), ('T5', 'S'), ('T5', 'F8'),
         ('T6', 'F7'), ('F7', 'i2'), ('F8', 'i3')]
    o = []
    for a, b in E:
        o.append(L(N[a][0], N[a][1] + 15, N[b][0], N[b][1] - 15, L2, 1.8))
    for k, (x, y, s, n) in N.items():
        if n:
            o.append(nt(x, y, s)); o.append(badge(x + 22, y - 14, n))
        else:
            o.append(term(x, y, s))
    o.append(T(310, 370, 'Leaves left to right: id + id * id (5 terminals)', 14, bold=True))
    xd = 566
    o.append(T(xd, 30, 'Leftmost derivation', 14, 'start', bold=True))
    steps = ['E + T', 'T + T', 'F + T', 'id + T', 'id + T * F', 'id + F * F', 'id + id * F', 'id + id * id']
    for i, s in enumerate(steps):
        y = 60 + i * 36
        o.append(badge(xd + 10, y - 5, i + 1))
        o.append(T(xd + 28, y, '⇒ ' + s, 13, 'start'))
    o.append(T(xd, 60 + 8 * 36 + 4, '8 steps', 14, 'start', LV, True))
    return 388, ''.join(o)
FIG[2] = (f2, 'Each nonterminal carries the number of the leftmost-derivation step that expands it, 1 to 8. The * sits deeper than the +, under the right T, so multiplication is done before addition.',
          'A parse tree for id + id * id with root E, children E, + and T, the right T expanding to T * F, each nonterminal marked with its step number, beside the eight-step leftmost derivation.')


# ---- 2.3 removing left recursion and left factoring ----
def f3():
    o = [T(160, 28, 'before', 14, fill=MUT, bold=True), T(520, 28, 'after', 14, fill=MUT, bold=True)]
    rows = [('left recursion', ['E → <tspan style="fill:var(--live);font-weight:700">E</tspan> + T | T'], ['E → T E′', 'E′ → + T E′ | ε']),
            ('left recursion', ['T → <tspan style="fill:var(--live);font-weight:700">T</tspan> * F | F'], ['T → F T′', 'T′ → * F T′ | ε']),
            ('common prefix', ['S → <tspan style="fill:var(--live);font-weight:700">i E t S</tspan>', '&#160;&#160;| <tspan style="fill:var(--live);font-weight:700">i E t S</tspan> e S | a'], ['S → i E t S S′ | a', 'S′ → e S | ε']),
            ('no change', ['F → id'], ['F → id'])]
    y = 44
    for why, before, after in rows:
        h = 30 + 22 * max(len(before), len(after))
        o.append(R(20, y, 290, h - 8, PANEL, L2, 8, 1.5))
        for j, s in enumerate(before):
            o.append(TM(36, y + 24 + j * 22, s, 14, 'start'))
        o.append(T(300, y + h - 16, why, 13, 'end', LV if why != 'no change' else MUT))
        o.append(L(318, y + (h - 8) / 2, 372, y + (h - 8) / 2, AC, 2.5, arrow='n'))
        o.append(R(380, y, 320, h - 8, ACS if why != 'no change' else PANEL, AC if why != 'no change' else L2, 8, 1.5))
        for j, s in enumerate(after):
            o.append(TM(396, y + 24 + j * 22, s, 14, 'start', bold=j == 0 and why != 'no change'))
        y += h
    o.append(T(360, y + 22, '11 productions, 3 of them ε, over 7 nonterminals', 15, bold=True))
    return y + 38, ''.join(o)
FIG[3] = (f3, 'E and T lose their left recursion by moving the repeated part into new nonterminals E′ and T′, and S loses its common prefix i E t S into S′. The final grammar has 11 productions, 3 ε-productions and 7 nonterminals.',
          'Four before-and-after rows: E → E + T | T becomes E → T E′ with E′ → + T E′ | ε, the same for T, the two S rules sharing i E t S are factored into S′, and F → id is unchanged.')


# ---- 2.4 recursive descent call tree ----
def f4():
    N = {'E': (360, 30, 'E()'), 'T1': (150, 92, 'T()'), 'Ep1': (530, 92, 'E′()'),
         'F1': (90, 154, 'F()'), 'Tp1': (210, 154, 'T′()'), 'plus': (410, 154, '+'), 'T2': (530, 154, 'T()'), 'Ep2': (660, 154, 'E′()'),
         'id1': (90, 216, 'id'), 'F2': (460, 216, 'F()'), 'Tp2': (600, 216, 'T′()'),
         'id2': (460, 278, 'id'), 'star': (530, 278, '*'), 'F3': (610, 278, 'F()'), 'Tp3': (690, 278, 'T′()'),
         'id3': (610, 340, 'id')}
    E = [('E', 'T1'), ('E', 'Ep1'), ('T1', 'F1'), ('T1', 'Tp1'), ('F1', 'id1'), ('Ep1', 'plus'), ('Ep1', 'T2'), ('Ep1', 'Ep2'),
         ('T2', 'F2'), ('T2', 'Tp2'), ('F2', 'id2'), ('Tp2', 'star'), ('Tp2', 'F3'), ('Tp2', 'Tp3'), ('F3', 'id3')]
    matched = {'id1': 1, 'plus': 2, 'id2': 3, 'star': 4, 'id3': 5}
    eps = {'Tp1', 'Ep2', 'Tp3'}
    o = []
    for a, b in E:
        o.append(L(N[a][0], N[a][1] + 15, N[b][0], N[b][1] - 14, L2, 1.6))
    for k, (x, y, s) in N.items():
        if k in matched:
            o.append(term(x, y, s, NX)); o.append(badge(x + 22, y - 13, matched[k], NX))
        else:
            o.append(nt(x, y, s, AC if k not in eps else L2, ACS if k not in eps else PANEL, 58))
            if k in eps: o.append(T(x, y + 32, 'ε: returns', 13, fill=MUT))
    o.append(T(20, 330, 'Tokens matched in order:', 13, 'start', MUT))
    o.append(T(20, 350, 'id + id * id (5)', 14, 'start', NX, True))
    o.append(T(20, 372, 'No backtracking: the lookahead picks each rule.', 13, 'start'))
    return 388, ''.join(o)
FIG[4] = (f4, 'Each nonterminal is a procedure, and the calls form a tree. E() calls T() and E′(); the green leaves are the five tokens matched in order, and T′() and E′() return at once (ε) when the lookahead does not fit.',
          'A call tree of procedures E, T, E′, F and T′ for the input id + id * id, with the five matched tokens numbered 1 to 5 and three calls marked as returning ε.')


# ---- 2.5 FIRST and FOLLOW sets ----
def f5():
    rows = [('E', ['(', 'id'], [')', '$']), ('E′', ['+', 'ε'], [')', '$']), ('T', ['(', 'id'], ['+', ')', '$']),
            ('T′', ['*', 'ε'], ['+', ')', '$']), ('F', ['(', 'id'], ['*', '+', ')', '$'])]
    x0, xf, xw = 30, 130, 400
    o = [T(xf + 70, 30, 'FIRST', 15, 'start', bold=True), T(xw, 30, 'FOLLOW', 15, 'start', bold=True)]
    o.append(T(xf + 70, 48, 'what a string from it can start with', 13, 'start', MUT))
    o.append(T(xw, 48, 'what can come right after it', 13, 'start', MUT))
    for i, (A, fi, fo) in enumerate(rows):
        y = 92 + i * 50
        nul = 'ε' in fi
        o.append(R(x0, y - 22, 670, 40, ACS if nul else PANEL, LN, 8, 1))
        o.append(T(x0 + 16, y + 4, A, 16, 'start', bold=True))
        if nul: o.append(T(x0 + 46, y + 3, 'nullable', 13, 'start', LV))
        o.append(chips(xf + 70, y + 4, fi, hot=('ε',)))
        o.append(chips(xw, y + 4, fo, hot=('$',)))
    o.append(T(30, 360, 'ε appears only in FIRST of the nullable E′ and T′. Every FOLLOW set holds $, the end marker.', 13, 'start'))
    return 376, ''.join(o)
FIG[5] = (f5, 'FIRST lists the tokens a nonterminal can start with and FOLLOW the tokens that can come right after it. Only the nullable E′ and T′ have ε in FIRST, and every FOLLOW set contains $.',
          'A table of the five nonterminals E, E′, T, T′ and F with their FIRST and FOLLOW sets as rows of symbol chips; ε is highlighted in two FIRST sets and $ in every FOLLOW set.')


# ---- 2.6 LL(1) table ----
def f6():
    cols = ['id', '+', '*', '(', ')', '$']
    M = {('E', 'id'): 'T E′', ('E', '('): 'T E′', ('E′', '+'): '+ T E′', ('E′', ')'): 'ε', ('E′', '$'): 'ε',
         ('T', 'id'): 'F T′', ('T', '('): 'F T′', ('T′', '*'): '* F T′', ('T′', '+'): 'ε', ('T′', ')'): 'ε', ('T′', '$'): 'ε',
         ('F', 'id'): 'id', ('F', '('): '( E )'}
    rows = ['E', 'E′', 'T', 'T′', 'F']
    x0, y0, cw, ch = 74, 56, 104, 46
    o = [T(x0 + 3 * cw, 24, 'lookahead token', 13, fill=MUT)]
    for j, c in enumerate(cols): o.append(TM(x0 + j * cw + cw / 2, y0 - 10, c, 15, bold=True))
    for i, A in enumerate(rows):
        y = y0 + i * ch
        o.append(T(x0 - 14, y + ch / 2 + 5, A, 15, 'end', bold=True))
        for j, c in enumerate(cols):
            v = M.get((A, c))
            first = (A, c) == ('E', 'id')
            if v is None:
                o.append(R(x0 + j * cw, y, cw, ch, PANEL, LN, 0, 1))
            else:
                e = v == 'ε'
                o.append(R(x0 + j * cw, y, cw, ch, LVS if first else (NXS if e else ACS), LV if first else (NX if e else AC), 0, 2 if first else 1.2))
                o.append(T(x0 + j * cw + cw / 2, y + ch / 2 + 5, f'{A} → {v}', 13, fill=NX if e else INK, bold=first))
    yb = y0 + 5 * ch + 30
    o.append(T(x0, yb, 'Row = nonterminal on top of the stack, column = next token, cell = rule to use.', 13, 'start'))
    o.append(T(x0, yb + 22, 'ε rules sit under the tokens in FOLLOW. Empty cells mean a syntax error.', 13, 'start', NX))
    o.append(T(x0, yb + 50, '13 filled cells, no cell with two rules: the grammar is LL(1).', 14, 'start', bold=True))
    o.append(T(x0 + 6 * cw, yb + 50, 'first move: M[E, id]', 13, 'end', LV, True))
    return yb + 66, ''.join(o)
FIG[6] = (f6, 'Each filled cell M[A, a] says which rule to use when A is on top of the stack and a is the next token; the first move of the parse is M[E, id] = E → T E′. The 13 filled cells never hold two rules, so the grammar is LL(1).',
          'An LL(1) parsing table with rows E, E′, T, T′, F and columns id, +, *, (, ), $, holding 13 rules, with the ε rules in green and the cell M[E, id] highlighted.')


# ---- 2.7 panic-mode recovery ----
def f7():
    o = [T(30, 30, 'Input  id + * id $', 15, 'start', bold=True)]
    tape = [('id', 'done'), ('+', 'done'), ('*', 'bad'), ('id', 'next'), ('$', 'next')]
    for i, (s, st) in enumerate(tape):
        x = 200 + i * 66
        fill, c = {'done': (PANEL, LN), 'bad': (LVS, LV), 'next': (ACS, AC)}[st]
        o.append(R(x, 12, 58, 34, fill, c, 5, 2 if st == 'bad' else 1.5))
        o.append(TM(x + 29, 35, s, 16, fill=MUT if st == 'done' else c, bold=st != 'done'))
    o.append(T(200 + 2 * 66 + 29, 64, 'dropped', 13, fill=LV, bold=True))
    o.append(T(200, 64, 'already matched', 13, 'start', MUT))
    o.append(T(530, 30, 'stack: $ E′ T', 14, 'start', bold=True))
    steps = [('1. detect', ['top T, lookahead *', 'M[T, *] is empty', '→ report the error'], LV, LVS),
             ('2. skip', ['* is not in FOLLOW(T)', '= {+, ), $}', '→ throw * away'], LV, PANEL),
             ('3. resume', ['lookahead id', 'M[T, id] = T → F T′', '→ parse on to accept'], NX, NXS)]
    for i, (h, lines, c, cs) in enumerate(steps):
        x = 20 + i * 236
        o.append(R(x, 96, 212, 140, cs, c, 10, 2))
        o.append(T(x + 106, 124, h, 15, fill=c, bold=True))
        for j, s in enumerate(lines):
            o.append(T(x + 106, 154 + j * 24, s, 14, bold=j == 2))
        if i < 2: o.append(L(x + 214, 166, x + 234, 166, AC, 2.5, arrow='n'))
    o.append(T(360, 272, 'One error reported, one token dropped; id + id $ is what gets parsed.', 14, bold=True))
    return 288, ''.join(o)
FIG[7] = (f7, 'With T on top of the stack and * as the next token, the table cell M[T, *] is empty, so the parser reports an error. * is not in FOLLOW(T), so it is thrown away; M[T, id] then has a rule and parsing carries on to accept.',
          'The input id + * id $ with the stray * crossed out, above three boxes: detect the empty cell M[T, *], skip * because it is not in FOLLOW(T), and resume with M[T, id] = T → F T′.')


spec = make_spec(FIG)
