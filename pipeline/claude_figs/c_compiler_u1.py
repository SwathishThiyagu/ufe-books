"""Claude's hand-drawn figures for c-compiler-u1 (Compiler Design, unit 1: introduction and lexical analysis), one per
chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 1.1 interpreter vs compiler cost ----
def f1():
    x0, x1, y0, y1 = 80, 660, 50, 290
    fx = lambda r: x0 + r / 5 * (x1 - x0)
    fy = lambda t: y1 - t / 16 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 1, 2, 3, 4, 5], [0, 4, 8, 12, 16], fx, fy, 'number of runs r', 'total cost (s)')]
    o.append(P([(fx(0), fy(0)), (fx(5), fy(15))], LV, 3))
    o.append(P([(fx(0), fy(4)), (fx(5), fy(4.5))], AC, 3))
    for r in range(1, 6):
        o.append(C(fx(r), fy(3 * r), 5, LV)); o.append(C(fx(r), fy(4 + 0.1 * r), 5, AC))
    o.append(T(fx(4.2), fy(13.6), 'interpreter: 3r', 14, 'end', LV, True))
    o.append(T(fx(5), fy(4.5) + 22, 'compiler: 4 + 0.10r', 14, 'end', AC, True))
    xc = fx(4 / 2.9)
    o.append(L(xc, fy(4.14), xc, y1, MUT, 1.5, '4 4'))
    o.append(Tb(xc, fy(1.2), 'cross at 1.38', 13, fill=MUT))
    o.append(boxt(fx(0.3), fy(14.2), 116, 46, ['r = 1', '4.1 s vs 3 s'], PANEL, L2, 13, bold_first=True))
    o.append(L(fx(1), fy(14.2) + 48, fx(1), fy(4.1) - 8, L2, 1.5, '3 3'))
    o.append(boxt(fx(1.4), fy(14.2), 116, 46, ['r = 2', '4.2 s vs 6 s'], ACS, AC, 13, bold_first=True))
    o.append(L(fx(2), fy(14.2) + 48, fx(2), fy(6) - 8, AC, 1.5, '3 3'))
    o.append(T(370, 372, 'From 2 runs on, compiling once is cheaper than interpreting every time.', 14, bold=True))
    return 388, ''.join(o)
FIG[1] = (f1, 'The interpreter pays 3 s on every run, while the compiler pays 4 s once and then 0.10 s a run. The lines cross at r = 1.38, so from 2 runs (4.2 s against 6 s) compiling is cheaper.',
          'Two cost lines against the number of runs: the interpreter line 3r rises steeply, the compiler line 4 + 0.10r stays almost flat, and they cross between runs 1 and 2.')


# ---- 1.2 one statement through every phase ----
def f2():
    o = []
    phases = [('source text', 40), ('lexical analysis', 52), ('syntax analysis', 146), ('semantic analysis', 52),
              ('intermediate code', 76), ('optimisation', 44), ('code generation', 104)]
    y = 14
    rows = []
    for name, h in phases:
        rows.append((name, y, h)); y += h + 18
    for i, (name, y, h) in enumerate(rows):
        hot = i == 0
        o.append(boxt(14, y + h / 2 - 20, 170, 40, [name], ACS if not hot else PANEL, AC if not hot else L2, 14, bold_first=not hot))
        if i: o.append(L(99, rows[i - 1][1] + rows[i - 1][2] / 2 + 20, 99, y + h / 2 - 23, AC, 2, arrow='n'))
        o.append(R(206, y, 500, h, PANEL, LN, 8, 1.2))
    cy = lambda i: rows[i][1] + rows[i][2] / 2
    o.append(TM(456, cy(0) + 5, 'position = initial + rate * 60', 15))
    o.append(TM(400, cy(1) + 5, 'id1  =  id2  +  id3  *  60', 15, fill=AC, bold=True))
    o.append(T(690, cy(1) + 5, '7 tokens', 13, 'end', MUT))
    # tree
    yt = rows[2][1]
    nodes = {'=': (320, yt + 22), 'id1': (260, yt + 56), '+': (380, yt + 56), 'id2': (330, yt + 90), '*': (430, yt + 90),
             'id3': (390, yt + 124), '60': (470, yt + 124)}
    for a, b in (('=', 'id1'), ('=', '+'), ('+', 'id2'), ('+', '*'), ('*', 'id3'), ('*', '60')):
        o.append(L(*nodes[a], *nodes[b], L2, 1.8))
    for n, (x, yy) in nodes.items():
        o.append(f'<circle cx="{x}" cy="{yy}" r="15" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:1.5"/>' if len(n) == 1 else R(x - 22, yy - 12, 44, 24, PANEL, L2, 5, 1.5))
        o.append(TM(x, yy + 5, n, 13 if len(n) > 1 else 14, bold=len(n) == 1))
    o.append(T(690, yt + 70, '* sits below +', 13, 'end', MUT)); o.append(T(690, yt + 88, 'because it binds tighter', 13, 'end', MUT))
    o.append(T(456, cy(3) + 5, 'all three ids are float, so 60 becomes 60.0', 14))
    yi = rows[4][1]
    for j, s in enumerate(['t1 = id3 * 60.0', 't2 = id2 + t1', 'id1 = t2']):
        o.append(TM(240, yi + 24 + j * 20, s, 14, 'start'))
    o.append(T(690, yi + 44, '3 instructions, 2 temporaries', 13, 'end', MUT))
    o.append(T(456, cy(5) + 5, 'nothing to fold or share: code unchanged', 14, fill=MUT))
    yc = rows[6][1]
    for j, s in enumerate(['LD  R1, rate', 'MUL R1, R1, #60.0', 'LD  R2, initial', 'ADD R1, R2, R1', 'ST  position, R1']):
        o.append(TM(240, yc + 22 + j * 18, s, 13, 'start'))
    o.append(T(690, yc + 56, '5 machine instructions', 13, 'end', MUT))
    return rows[-1][1] + rows[-1][2] + 10, ''.join(o)
FIG[2] = (f2, 'The same statement is rewritten by every phase: 7 tokens, a tree with * below +, 60 widened to 60.0, 3 three-address instructions and 5 machine instructions. The optimiser finds nothing to improve.',
          'Seven phases down the left, each with the form the statement position = initial + rate * 60 takes after it: tokens, a parse tree, typed tree, three-address code, unchanged code and five machine instructions.')


# ---- 1.3 LEX and YACC generate the scanner and the parser ----
def f3():
    o = []
    def lane(y, spec, tool, out, c, cs):
        o.append(boxt(14, y, 200, 62, spec, PANEL, L2, 13))
        o.append(L(216, y + 31, 262, y + 31, c, 2.5, arrow='n' if c == AC else 'x'))
        o.append(boxt(266, y + 6, 110, 50, [tool], cs, c, 16, bold_first=True))
        o.append(L(378, y + 31, 424, y + 31, c, 2.5, arrow='n' if c == AC else 'x'))
        o.append(boxt(428, y + 6, 130, 50, [out], cs, c, 15, bold_first=True))
    lane(40, ['16 token patterns', '+ 42 keywords'], 'LEX', 'scanner.c', AC, ACS)
    lane(170, ['grammar of the', 'query language + actions'], 'YACC', 'parser.c', NX, NXS)
    o.append(T(114, 28, 'you write', 13, fill=MUT)); o.append(T(321, 28, 'tool', 13, fill=MUT)); o.append(T(493, 28, 'it writes', 13, fill=MUT))
    o.append(L(493, 98, 493, 172, AC, 2.5, arrow='n'))
    o.append(T(503, 140, 'one token at a time', 13, 'start', AC, True))
    o.append(boxt(300, 270, 400, 66, ['still written by hand:', 'symbol table, type checks, code generation'], PANEL, LV, 13, bold_first=True, dash='6 4'))
    o.append(T(14, 360, '2 generator tools give 2 parts, not a whole compiler.', 14, 'start', bold=True))
    return 376, ''.join(o)
FIG[3] = (f3, 'LEX turns the 16 token patterns and 42 keywords into scanner.c, and YACC turns the grammar into parser.c, which reads the scanner’s tokens. The two generated files are parts, not a complete compiler.',
          'Two lanes: token patterns and keywords go into LEX and come out as scanner.c; the grammar goes into YACC and comes out as parser.c; an arrow passes tokens from scanner.c to parser.c.')


# ---- 1.4 a line becomes 12 tokens ----
def f4():
    o = [TM(360, 34, 'if (count &lt;= 10) count = count + 1;', 17, bold=True)]
    toks = [('if', 'IF', ''), ('(', 'LPAREN', ''), ('count', 'ID', 'count'), ('&lt;=', 'LE', ''), ('10', 'NUM', '10'), (')', 'RPAREN', ''),
            ('count', 'ID', 'count'), ('=', 'ASSIGN', ''), ('count', 'ID', 'count'), ('+', 'PLUS', ''), ('1', 'NUM', '1'), (';', 'SEMI', '')]
    for i, (lx, tn, at) in enumerate(toks):
        x, y = 16 + (i % 6) * 116, 64 + (i // 6) * 112
        kind = {'ID': (ACS, AC), 'NUM': (NXS, NX), 'LE': (LVS, LV)}.get(tn, (PANEL, L2))
        o.append(R(x, y, 106, 92, kind[0], kind[1], 8, 2 if tn in ('ID', 'NUM', 'LE') else 1.5))
        o.append(TM(x + 53, y + 26, lx, 16, bold=True))
        o.append(L(x + 12, y + 38, x + 94, y + 38, LN, 1))
        o.append(T(x + 53, y + 60, tn, 14, fill=kind[1] if kind[1] != L2 else INK, bold=True))
        o.append(T(x + 53, y + 80, f'value: {at}' if at else 'no value', 13, fill=MUT))
        o.append(T(x + 10, y + 14, str(i + 1), 13, 'start', MUT))
    o.append(T(16, 310, '&lt;= is one token (longest match), not &lt; then =. Spaces make no tokens.', 13, 'start', LV))
    o.append(T(360, 344, '12 tokens from 10 distinct lexemes: ID 3 times, NUM 2 times.', 15, bold=True))
    return 360, ''.join(o)
FIG[4] = (f4, 'The lexer turns the line into 12 tokens, each a token name with a value where one is needed. &lt;= is taken as one token, and ID appears 3 times and NUM twice.',
          'Twelve token cards in order, each showing the lexeme, the token name and its value: IF, LPAREN, ID count, LE, NUM 10, RPAREN, ID count, ASSIGN, ID count, PLUS, NUM 1, SEMI.')


# ---- 1.5 buffer pair with sentinels ----
def f5():
    o = []
    A = list('count') + ['$']
    B = ['=', '1', '+', '2', ';', '$']
    cw, y = 50, 120
    xa, xb = 30, 390
    def buf(x0, cells, name, hot):
        o.append(T(x0, 30, f'Buffer {name}', 15, 'start', bold=True))
        for i, ch in enumerate(cells):
            x = x0 + i * cw
            sent = ch == '$'
            h = i in hot
            o.append(R(x, y, cw, 50, ACS if h else PANEL, AC if h else L2, 0, 1.5, '4 3' if sent else None))
            o.append(TM(x + cw / 2, y + 32, ch, 18, fill=MUT if sent else (AC if h else INK), bold=h))
            o.append(T(x + cw / 2, y + 70, f'{name}{i}', 13, fill=MUT))
        o.append(T(x0 + 5.5 * cw, y + 88, 'sentinel', 13, fill=MUT))
    buf(xa, A, 'A', {0, 1, 2, 3, 4})
    buf(xb, B, 'B', set())
    o.append(brace(xa + 2, xa + 5 * cw - 2, y + 98, AC))
    o.append(T(xa + 2.5 * cw, y + 124, 'lexeme count: 5 characters', 14, fill=AC, bold=True))
    o.append(L(xa + cw / 2, 74, xa + cw / 2, y - 4, AC, 2.5, arrow='n'))
    o.append(T(xa + 4, 66, 'lexemeBegin = A0', 14, 'start', AC, True))
    o.append(L(xb + cw / 2, 74, xb + cw / 2, y - 4, LV, 2.5, arrow='l'))
    o.append(T(xb + 4, 66, 'forward = B0', 14, 'start', LV, True))
    o.append(arc(xa + 5.5 * cw, y - 4, xb - 6, y + 12, -0.35, LV, 2, 'l', '6 4'))
    o.append(Tb(xa + 5.5 * cw + 50, y - 34, 'at $: switch to B', 13, fill=LV))
    o.append(T(360, y + 170, 'forward reads =, which cannot continue a name, so count is accepted.', 14))
    return y + 186, ''.join(o)
FIG[5] = (f5, 'Cells A0 to A4 hold count. When forward reaches the sentinel $ at A5 it switches to Buffer B and reads = at B0, which cannot extend a name, so the lexeme count (5 characters) is accepted.',
          'Two half-buffers of five cells and a sentinel each: count$ and =1+2;$, with lexemeBegin at A0, the lexeme count bracketed, and forward moved past the sentinel to B0.')


# ---- 1.6 longest match with id and num ----
def f6():
    o = [T(190, 30, 'id = L(L|D)*: starts with a letter or _', 14, bold=True, fill=AC), T(540, 30, 'num = D+: digits only', 14, bold=True, fill=NX)]
    s = 'sum_1 1sum _a 42'
    toks = [(0, 5, 'id', 'sum_1'), (6, 7, 'num', '1'), (7, 10, 'id', 'sum'), (11, 13, 'id', '_a'), (14, 16, 'num', '42')]
    cw, x0, y = 42, 24, 60
    for i, ch in enumerate(s):
        x = x0 + i * cw
        if ch == ' ':
            o.append(T(x + cw / 2, y + 30, '␣', 15, fill=MUT)); continue
        o.append(R(x, y, cw - 2, 44, PANEL, L2, 4, 1.5))
        o.append(TM(x + cw / 2 - 1, y + 29, ch, 18, bold=True))
    for a, b, kind, lex in toks:
        c = AC if kind == 'id' else NX
        o.append(brace(x0 + a * cw + 2, x0 + b * cw - 4, y + 56, c))
        o.append(T(x0 + (a + b) * cw / 2 - 1, y + 84, f'{kind}({lex})', 14, fill=c, bold=True))
    o.append(boxt(x0 + 6 * cw - 10, y + 108, 240, 52, ['1sum: a digit cannot start an id,', 'so it splits into num(1) and id(sum)'], LVS, LV, 13))
    o.append(L(x0 + 8 * cw, y + 106, x0 + 8 * cw, y + 92, LV, 1.5))
    o.append(T(360, y + 196, '3 identifiers + 2 unsigned integers = 5 tokens, and _a is an identifier.', 15, bold=True))
    return y + 212, ''.join(o)
FIG[6] = (f6, 'Read with longest match, sum_1 1sum _a 42 gives five tokens. 1sum splits into num(1) and id(sum) because an identifier cannot start with a digit, while _a is an identifier because _ counts as a letter.',
          'The characters of sum_1 1sum _a 42 in cells, with brackets underneath grouping them into id(sum_1), num(1), id(sum), id(_a) and num(42).')


# ---- 1.7 transition diagram for ID and NUM ----
def f7():
    q0, q1, q2 = (90, 170), (300, 90), (300, 260)
    o = [state(*q0, 'q0', start=True), state(*q1, 'q1', accept=True), state(*q2, 'q2', accept=True, stroke=NX)]
    o.append(edge(q0, q1, bend=0.1)); o.append(Tb(170, 106, 'letter or _', 13, fill=AC))
    o.append(edge(q0, q2, bend=-0.1, c=NX, arrow='x')); o.append(Tb(170, 244, 'digit', 13, fill=NX))
    o.append(loop(*q1)); o.append(T(300, 20, 'letter, digit, _', 13, fill=AC))
    o.append(loop(*q2, up=False)); o.append(T(300, 340, 'digit', 13, fill=NX))
    o.append(T(334, 95, 'ID', 14, 'start', AC, True)); o.append(T(334, 265, 'NUM', 14, 'start', NX, True))
    o.append(T(560, 34, 'Input: rate2 ␣ 2rate', 15, bold=True))
    rows = [('rate2', 'q0 → q1 → q1 … q1', 'space has no edge', 'ID(rate2)', AC),
            ('2', 'q0 → q2', 'r is not a digit', 'NUM(2)', NX),
            ('rate', 'q0 → q1 … q1', 'input ends', 'ID(rate)', AC)]
    for i, (lex, path, stop, tok, c) in enumerate(rows):
        y = 56 + i * 92
        o.append(R(410, y, 300, 80, PANEL, c, 8, 1.5))
        o.append(TM(424, y + 24, lex, 15, 'start', bold=True))
        o.append(T(696, y + 24, tok, 14, 'end', c, True))
        o.append(T(424, y + 48, path, 13, 'start'))
        o.append(T(424, y + 68, f'stop: {stop}', 13, 'start', MUT))
    return 356, ''.join(o)
FIG[7] = (f7, 'From q0 a letter or _ leads to q1 (ID) and a digit to q2 (NUM), and each state loops while its kind of character continues. On rate2 2rate the lexer stops at the space and at the r, giving ID(rate2), NUM(2) and ID(rate).',
          'A transition diagram with start state q0, an edge on letter to accepting state q1 that loops on letters and digits, and an edge on digit to accepting state q2 that loops on digits, beside a trace of rate2 2rate.')


# ---- 1.8 subset construction and minimisation ----
def f8():
    A, B, Cc, D = (80, 140), (260, 140), (440, 70), (440, 210)
    o = [T(20, 26, 'DFA from subset construction', 14, 'start', bold=True)]
    o.append(state(*A, 'A', start=True, r=26)); o.append(T(A[0], A[1] + 46, '{0}', 13, fill=MUT))
    o.append(state(*B, 'B', r=26)); o.append(T(B[0], B[1] + 46, '{1, 2, 4}', 13, fill=MUT))
    o.append(state(*Cc, 'C', accept=True, r=26, stroke=NX)); o.append(T(Cc[0] + 38, Cc[1] + 5, '{3}', 13, 'start', MUT))
    o.append(state(*D, 'D', accept=True, r=26, stroke=NX)); o.append(T(D[0] + 38, D[1] + 5, '{5}', 13, 'start', MUT))
    o.append(edge(A, B, 26)); o.append(Tb(170, 130, 'a', 14, fill=AC, bold=True))
    o.append(edge(B, Cc, 26)); o.append(Tb(350, 94, 'b', 14, fill=AC, bold=True))
    o.append(edge(B, D, 26)); o.append(Tb(350, 192, 'c', 14, fill=AC, bold=True))
    o.append(f'<rect x="396" y="30" width="136" height="220" rx="60" style="fill:none;stroke:var(--next);stroke-width:2;stroke-dasharray:6 5"/>')
    o.append(T(626, 122, 'C and D act alike:', 13, fill=NX, bold=True)); o.append(T(626, 140, 'both final, no moves', 13, fill=NX))
    o.append(T(626, 162, 'merge: F = {3, 5}', 13, fill=NX, bold=True))
    o.append(L(20, 280, 700, 280, LN, 1))
    o.append(T(20, 306, 'Minimal DFA: 3 states', 14, 'start', bold=True))
    A2, B2, F2 = (250, 350), (420, 350), (590, 350)
    o.append(state(*A2, 'A', start=True)); o.append(state(*B2, 'B')); o.append(state(*F2, 'F', accept=True, stroke=NX))
    o.append(edge(A2, B2)); o.append(Tb(335, 340, 'a', 14, fill=AC, bold=True))
    o.append(edge(B2, F2)); o.append(Tb(505, 340, 'b, c', 14, fill=AC, bold=True))
    o.append(T(360, 404, 'Missing moves go to a dead state, which is left out of the drawing.', 13, fill=MUT))
    return 418, ''.join(o)
FIG[8] = (f8, 'Subset construction for a(b|c) gives A = {0}, B = {1, 2, 4}, C = {3} and D = {5}. C and D are both final with no moves, so minimisation merges them into F, leaving 3 states.',
          'A DFA with A going to B on a, and B going to final states C on b and D on c, with C and D circled for merging; below, the minimal DFA A to B on a, B to F on b or c.')


# ---- 1.9 LEX rule order on "if x 12" ----
def f9():
    rules = [('(1) if', 'IF'), ('(2) [a-z]+', 'ID'), ('(3) [0-9]+', 'NUM')]
    lex = ['if', 'x', '12']
    grid = [[('2, wins: earlier', 1), ('no match', 0), ('no match', 0)],
            [('2, tie, later', 2), ('1, wins', 1), ('no match', 0)],
            [('no match', 0), ('no match', 0), ('2, wins', 1)]]
    x0, y0, rw, cw, rh = 20, 70, 170, 172, 54
    o = [T(x0 + rw + 1.5 * cw, 26, 'Input: if x 12   (cells show the length each rule matches)', 14, bold=True)]
    for j, s in enumerate(lex):
        o.append(TM(x0 + rw + j * cw + cw / 2, y0 - 12, s, 17, bold=True))
    for i, (rname, tok) in enumerate(rules):
        y = y0 + i * rh
        o.append(R(x0, y, rw - 8, rh - 8, PANEL, L2, 6, 1.5))
        o.append(TM(x0 + 12, y + 30, rname, 14, 'start', bold=True))
        for j in range(3):
            s, k = grid[i][j]
            fill, st, col = {1: (NXS, NX, NX), 2: (LVS, LV, LV), 0: (PANEL, LN, MUT)}[k]
            o.append(R(x0 + rw + j * cw, y, cw - 8, rh - 8, fill, st, 6, 1.5))
            o.append(T(x0 + rw + j * cw + (cw - 8) / 2, y + 28, s, 13, fill=col, bold=k == 1))
    yt = y0 + 3 * rh + 18
    o.append(T(x0, yt + 22, 'tokens', 14, 'start', MUT))
    for j, (t, n) in enumerate((('IF', 2), ('ID', 1), ('NUM', 2))):
        o.append(boxt(x0 + rw + j * cw, yt, cw - 8, 36, [f'{t}  (length {n})'], ACS, AC, 14, bold_first=True))
    o.append(T(360, yt + 76, '3 tokens, 2 + 1 + 2 = 5 characters. With rule (2) first, if would become ID.', 14))
    return yt + 92, ''.join(o)
FIG[9] = (f9, 'For if, rules (1) and (2) both match 2 characters, so the earlier rule wins and gives IF. x and 12 each have one matching rule, so the scanner returns 3 tokens covering 5 characters.',
          'A grid of the three LEX rules against the lexemes if, x and 12, showing the match length of each rule, with the winning rule highlighted, and the tokens IF, ID and NUM below.')


spec = make_spec(FIG)
