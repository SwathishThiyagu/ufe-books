"""Claude's hand-drawn figures for c-toc-u2 (Theory of Computation, unit 2: regular expressions, Thompson, Arden, Kleene,
pumping lemma, closure, Myhill-Nerode and scanners), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def lab(x, y, s, c=AC, size=14):
    return Tb(x, y, s, size, fill=c, bold=True)


def node(x, y, s, c=AC, f=PANEL, r=22, size=16):
    return f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:{f};stroke:{c};stroke-width:2"/>' + T(x, y + 6, s, size, fill=c, bold=True)


def cell(x, y, w, h, s, c=INK, fill=PANEL, stroke=L2, size=15):
    return R(x, y, w, h, fill, stroke, 3, 1.6) + TM(x + w / 2, y + h / 2 + 5, s, size, fill=c, bold=True)


# ---- 2.1 precedence as a parse tree ----
def f1():
    o = []
    N = {'u': (220, 50, '+', LV), 'z': (110, 140, '0', INK), 'c': (330, 140, '·', NX), 'one': (250, 230, '1', INK),
         's': (410, 230, '*', AC), 'c2': (410, 310, '·', AC), 'a': (350, 390, '0', INK), 'b': (470, 390, '1', INK)}
    E = [('u', 'z'), ('u', 'c'), ('c', 'one'), ('c', 's'), ('s', 'c2'), ('c2', 'a'), ('c2', 'b')]
    for a, b in E:
        o.append(L(N[a][0], N[a][1], N[b][0], N[b][1], L2, 2))
    for k, (x, y, s, c) in N.items():
        o.append(node(x, y, s, c, ACS if c == AC else (NXS if c == NX else (LVS if c == LV else PANEL)), 22, 18))
    o.append(T(250, 54, 'pass 3: union, last, at the root', 13, 'start', LV, True))
    o.append(T(360, 144, 'pass 2: concatenation 1 · (…)', 13, 'start', NX, True))
    o.append(T(440, 234, 'pass 1: star, first', 13, 'start', AC, True))
    o.append(T(440, 314, 'brackets (01) = 0 · 1', 13, 'start', AC, True))
    o.append(T(150, 270, 'the leading 1 stays', 13, 'middle', MUT, True)); o.append(T(150, 288, 'outside the star', 13, 'middle', MUT, True))
    o.append(R(590, 340, 112, 74, PANEL, L2, 8, 1.4))
    o.append(T(646, 362, 'length ≤ 3', 13, fill=MUT, bold=True))
    o.append(TM(646, 392, '0, 1, 101', 15, 'middle', NX, True))
    return 420, ''.join(o)
FIG[1] = (f1, 'The parse tree for 0 + 1(01)*: the star is applied first and wraps only the bracketed 0·1, so the leading 1 stays outside it; the union is applied last, at the root. The strings of length at most 3 are 0, 1 and 101.',
          'A parse tree with + at the root over 0 and a concatenation node, whose children are 1 and a star node over the concatenation 0·1, with the three precedence passes labelled and the strings 0, 1, 101.')


# ---- 2.2 simplifying (ε + a)* ----
def f2():
    o = []
    steps = ['(ε + a)*', '(ε* a*)*', '(ε a*)*', '(a*)*', 'a*']
    laws = ['(r + s)* = (r* s*)*', 'ε* = ε', 'ε r = r', '(r*)* = r*']
    y = 40
    for i, s in enumerate(steps):
        first, last = i == 0, i == 4
        f, c = (NXS, NX) if last else ((ACS, AC) if first else (PANEL, L2))
        o.append(R(60, y, 180, 42, f, c, 8, 2)); o.append(TM(150, y + 27, s, 17, 'middle', NX if last else INK, True))
        if i < 4:
            o.append(L(150, y + 44, 150, y + 66, AC, 2.2, arrow='n'))
            o.append(T(170, y + 60, laws[i], 14, 'start', AC, True))
        y += 70
    o.append(T(330, 125, 'Each arrow applies one law', 14, 'start', INK, True))
    o.append(T(330, 150, 'and keeps the language the same.', 14, 'start', INK, True))
    o.append(T(330, 200, 'a* = zero or more a’s:', 14, 'start', NX, True))
    o.append(TM(330, 226, 'ε, a, aa, aaa, …', 15, 'start', NX, True))
    o.append(T(330, 270, 'Adding ε inside a star never', 13, 'start', MUT))
    o.append(T(330, 288, 'changes it: the star already gives ε.', 13, 'start', MUT))
    return y - 10, ''.join(o)
FIG[2] = (f2, 'Four laws turn (ε + a)* into a*: the union-star law gives (ε* a*)*, then ε* = ε, ε drops out of the concatenation, and the double star collapses, leaving zero or more a’s.',
          'A vertical chain of five expressions from (ε + a)* to a*, each arrow labelled with the law it uses: (r + s)* = (r* s*)*, ε* = ε, ε r = r and (r*)* = r*.')


# ---- 2.3 Thompson's construction for a(b+c)* ----
def f3():
    o = []
    P_ = {0: (60, 190), 1: (128, 190), 8: (200, 190), 6: (278, 190), 2: (362, 130), 3: (455, 130), 4: (362, 250), 5: (455, 250),
          7: (540, 190), 9: (660, 190)}
    r = 20
    def e(a, b, s, bend=0.0, eps=True, lx=None, ly=None):
        o.append(edge(P_[a], P_[b], r=r, bend=bend, c=LV if eps else AC, arrow='l' if eps else 'n', dash='5 4' if eps else None))
        if s:
            mx, my = (P_[a][0] + P_[b][0]) / 2, (P_[a][1] + P_[b][1]) / 2
            o.append(lab(lx if lx is not None else mx, ly if ly is not None else my - 8, s, LV if eps else AC, 13))
    e(0, 1, 'a', eps=False); e(1, 8, 'ε'); e(8, 6, 'ε')
    e(6, 2, 'ε', lx=305, ly=152); e(6, 4, 'ε', lx=305, ly=236); e(2, 3, 'b', eps=False); e(4, 5, 'c', eps=False)
    e(3, 7, 'ε', lx=510, ly=152); e(5, 7, 'ε', lx=510, ly=236); e(7, 9, 'ε')
    e(7, 6, '', bend=-1.0); o.append(lab(409, 40, 'ε: repeat', LV, 13))
    e(8, 9, '', bend=-0.42); o.append(lab(430, 312, 'ε: skip the star (zero times)', LV, 13))
    for k, (x, y) in P_.items():
        fin = k == 9
        o.append(state(x, y, f'q{k}', accept=fin, start=k == 0, r=r, fill=NXS if fin else PANEL, stroke=NX if fin else AC, size=13))
    o.append(T(20, 352, '10 states q0 to q9, start q0, final q9; 3 symbol edges (solid) and 9 ε-edges (dashed).', 14, 'start', INK, True))
    return 368, ''.join(o)
FIG[3] = (f3, 'Thompson’s construction on a(b+c)* gives 10 states, start q0 and final q9, with 9 ε-moves (dashed). The ε from q7 back to q6 lets the star repeat, and the ε from q8 straight to q9 lets it run zero times.',
          'An ε-NFA: q0 to q1 on a, then ε-edges into a star around a choice of q2 to q3 on b or q4 to q5 on c, with a dashed ε back-edge q7 to q6 above and a dashed bypass q8 to q9 below.')


# ---- 2.4 state equations and Arden's theorem ----
def f4():
    o = []
    q0, q1 = (90, 110), (250, 110)
    o.append(state(*q0, 'q0', start=True)); o.append(state(*q1, 'q1', accept=True, fill=NXS, stroke=NX))
    o.append(loop(*q0)); o.append(lab(90, 52, '0')); o.append(loop(*q1)); o.append(lab(250, 52, '1'))
    o.append(edge(q0, q1, bend=0.15)); o.append(lab(170, 86, '1'))
    o.append(edge(q1, q0, bend=0.15)); o.append(lab(170, 146, '0'))
    o.append(T(170, 196, 'Arden: X = Q + P X gives X = P* Q', 13, fill=LV, bold=True))
    o.append(T(170, 214, '(when ε is not in P)', 13, fill=MUT))
    x = 330
    lines = [('q0 = 0 q0 + 1 q1', INK, False), ('q1 = 0 q0 + 1 q1 + ε', INK, False),
             ('P = 0:      q0 = 0*1 q1', LV, True), ('substitute: q1 = ε + 0*1 q1', INK, False),
             ('P = 0*1:   q1 = (0*1)*', LV, True), ('back into q0: (0*1)* 0*1 = (0+1)*1', NX, True)]
    for i, (s, c, b) in enumerate(lines):
        o.append(TM(x, 50 + i * 34, s, 15, 'start', c, True))
    o.append(T(x, 270, 'Binary strings that end in 1.', 14, 'start', NX, True))
    return 288, ''.join(o)
FIG[4] = (f4, 'Write one equation per state, then apply Arden twice, each time finding the loop term P X and starring P: with P = 0, q0 = 0*1 q1; with P = 0*1, q1 = (0*1)*. Putting q0 back gives (0+1)*1.',
          'A two-state DFA with q0 looping on 0 and q1 looping on 1, crossing on 1 and 0, beside the state equations and the two Arden steps ending in (0+1)*1.')


# ---- 2.5 Kleene's round trip for even parity ----
def f5():
    o = []
    o.append(boxt(20, 70, 170, 60, ['expression', '0*(10*10*)*'], ACS, AC, 14, bold_first=True))
    o.append(boxt(270, 70, 170, 60, ['ε-NFA', 'Thompson’s rules'], PANEL, L2, 14, bold_first=True))
    q0, q1 = (550, 100), (660, 100)
    o.append(state(*q0, 'q0', accept=True, start=False, fill=NXS, stroke=NX)); o.append(state(*q1, 'q1'))
    o.append(loop(*q0)); o.append(lab(550, 42, '0')); o.append(loop(*q1)); o.append(lab(660, 42, '0'))
    o.append(edge(q0, q1, bend=0.2)); o.append(lab(605, 76, '1')); o.append(edge(q1, q0, bend=0.2)); o.append(lab(605, 138, '1'))
    o.append(T(550, 152, 'even', 13, fill=NX, bold=True)); o.append(T(660, 152, 'odd', 13, fill=AC, bold=True))
    o.append(L(192, 100, 266, 100, AC, 2.2, arrow='n')); o.append(L(442, 100, 510, 100, AC, 2.2, arrow='n'))
    o.append(T(476, 90, 'subsets', 13, fill=AC, bold=True))
    o.append(P([(605, 166), (605, 196), (105, 196), (105, 136)], LV, 2.2, '6 4'))
    o.append(L(105, 150, 105, 134, LV, 2.2, arrow='l'))
    o.append(T(355, 188, 'Arden / state elimination gives the same expression back', 13, fill=LV, bold=True))
    o.append(T(20, 240, 'Same language at every stop: strings with an even number of 1s.', 14, 'start', INK, True))
    rows = [('0', 'ε'), ('1', '0'), ('2', '00, 11'), ('3', '000, 011, 101, 110')]
    for i, (n, s) in enumerate(rows):
        o.append(T(40 + i * 170, 270, f'length {n}', 13, 'start', MUT, True))
        o.append(TM(40 + i * 170, 292, s, 14, 'start', NX, True))
    o.append(T(20, 326, '1 + 1 + 2 + 4 = 8 strings of length at most 3', 14, 'start', NX, True))
    return 342, ''.join(o)
FIG[5] = (f5, 'Kleene’s theorem as a loop: the expression 0*(10*10*)* becomes an ε-NFA, then the two-state parity DFA (q0 even and final), and Arden’s rule reads the same expression back. The language holds 8 strings of length at most 3.',
          'A cycle from the expression 0*(10*10*)* to an ε-NFA to a two-state DFA q0 even and q1 odd, with a dashed return arrow to the expression, and the 8 short strings listed below.')


# ---- 2.6 pumping 000111 ----
def f6():
    o = [T(20, 26, 'p = 3, w = 000111 = x y z with x = 0, y = 0, z = 0111  (|xy| = 2 ≤ 3, |y| = 1)', 14, 'start', bold=True)]
    x0, cw = 170, 44
    rows = [('i = 0:  x z', '0' + '' + '0111', -1, '2 zeros, 3 ones', False), ('i = 1:  x y z', '000111', 1, '3 zeros, 3 ones', True),
            ('i = 2:  x y y z', '0' + '00' + '0111', 2, '4 zeros, 3 ones', False)]
    for r, (name, s, ny, cnt, ok) in enumerate(rows):
        y = 60 + r * 70
        o.append(T(x0 - 14, y + 26, name, 14, 'end', INK, True))
        for k, ch in enumerate(s):
            isy = 1 <= k <= ny if ny > 0 else False
            c, f, st = (LV, LVS, LV) if isy else ((AC, ACS, AC) if ch == '1' else (INK, PANEL, L2))
            o.append(cell(x0 + k * cw, y, cw - 4, 40, ch, c, f, st, 16))
        o.append(T(x0 + 7 * cw + 6, y + 18, cnt, 13, 'start', NX if ok else LV, True))
        o.append(T(x0 + 7 * cw + 6, y + 36, 'in L' if ok else 'not in L', 13, 'start', NX if ok else LV, True))
    o.append(brace(x0 + cw, x0 + 2 * cw - 4, 124, LV, up=True)); o.append(T(x0 + 1.5 * cw - 2, 114, 'y', 14, fill=LV, bold=True))
    o.append(T(20, 268, 'y lies inside the first p symbols, so it is all zeros: pumping changes the zeros but never the ones.', 13, 'start', INK, True))
    return 284, ''.join(o)
FIG[6] = (f6, 'Pumping y = 0 in w = 000111 with p = 3: deleting y leaves 00111 (2 zeros, 3 ones) and doubling it gives 0000111 (4 zeros, 3 ones). The zeros move but the ones stay at 3, so neither pumped string is in L.',
          'Three rows of bit cells: 00111 for i = 0, 000111 for i = 1 and 0000111 for i = 2, the pumped y cells highlighted, with zero and one counts and whether each string is in L.')


# ---- 2.7 product DFA for L1 ∩ L2 ----
def f7():
    o = []
    P_ = {'EN': (150, 90), 'EF': (420, 90), 'ON': (150, 260), 'OF': (420, 260)}
    names = {'EN': '(E,N)', 'EF': '(E,F)', 'ON': '(O,N)', 'OF': '(O,F)'}
    r = 30
    o.append(edge(P_['EN'], P_['EF'], r=r)); o.append(lab(285, 82, '1', NX))
    o.append(edge(P_['EN'], P_['ON'], r=r, bend=0.15)); o.append(lab(178, 175, '0'))
    o.append(edge(P_['ON'], P_['EN'], r=r, bend=0.15)); o.append(lab(122, 175, '0'))
    o.append(edge(P_['EF'], P_['ON'], r=r)); o.append(lab(330, 150, '0'))
    o.append(edge(P_['ON'], P_['OF'], r=r)); o.append(lab(285, 252, '1'))
    o.append(edge(P_['OF'], P_['EN'], r=r)); o.append(lab(330, 210, '0'))
    o.append(loop(420, 90, r=r)); o.append(lab(420, 26, '1'))
    o.append(loop(420, 260, r=r, up=False)); o.append(lab(420, 326, '1'))
    for k, (x, y) in P_.items():
        fin = k == 'EF'
        o.append(state(x, y, names[k], accept=fin, start=k == 'EN', r=r, fill=NXS if fin else PANEL, stroke=NX if fin else AC, size=13))
    xr = 500
    o.append(T(xr, 120, 'E/O: even/odd 0s (L₁)', 13, 'start', MUT, True))
    o.append(T(xr, 140, 'N/F: ends in 1? (L₂)', 13, 'start', MUT, True))
    o.append(T(xr, 180, 'final only if both are:', 13, 'start', NX, True))
    o.append(T(xr, 198, '(E,F)', 13, 'start', NX, True))
    o.append(T(xr, 238, '(E,N) on 1 → (E,F),', 13, 'start', NX, True))
    o.append(T(xr, 256, 'so the string 1 is a witness:', 13, 'start', NX, True))
    o.append(T(xr, 274, 'L₁ ∩ L₂ is not empty', 13, 'start', NX, True))
    return 344, ''.join(o)
FIG[7] = (f7, 'The product DFA pairs a state of each machine, 2 × 2 = 4 states. The start pair (E,N) reaches the only final pair (E,F) directly on 1, so L₁ ∩ L₂ is not empty and its shortest witness is 1.',
          'Four pair states (E,N), (E,F), (O,N), (O,F) in a square with their 0 and 1 transitions, (E,N) the start and (E,F) double-circled as the only final state.')


# ---- 2.8 Myhill-Nerode table for 0ⁿ1ⁿ ----
def f8():
    o = [T(20, 26, 'Is 0ⁱ followed by 1ʲ in L = {0ⁿ1ⁿ}?', 14, 'start', bold=True)]
    x0, y0, cw, ch = 170, 70, 90, 46
    pre = ['ε', '0', '00', '000']; suf = ['ε', '1', '11', '111']
    o.append(T(x0 + 4 * cw + 6, 66, 'suffix 1ʲ', 13, 'start', MUT, True))
    for j, s in enumerate(suf):
        o.append(TM(x0 + j * cw + cw / 2, y0 - 4 + 0, s, 15, 'middle', AC, True))
    for i, p in enumerate(pre):
        y = y0 + 10 + i * ch
        o.append(TM(x0 - 14, y + 29, p, 15, 'end', AC, True))
        for j in range(4):
            ok = i == j
            o.append(R(x0 + j * cw, y, cw - 4, ch - 4, NXS if ok else PANEL, NX if ok else LN, 3, 2 if ok else 1))
            o.append(T(x0 + j * cw + (cw - 4) / 2, y + 27, 'in L' if ok else 'no', 14 if ok else 13, fill=NX if ok else MUT, bold=ok))
    o.append(T(60, y0 + 10 + 2 * ch, 'prefix 0ⁱ', 13, 'middle', MUT, True))
    o.append(T(20, 290, 'Only the diagonal is in L, so suffix 1ⁱ separates 0ⁱ from every other 0ʲ: 4 strings, 4 classes.', 13, 'start', INK, True))
    o.append(T(20, 312, 'The same holds for every i, so there are infinitely many classes and L is not regular.', 13, 'start', LV, True))
    return 328, ''.join(o)
FIG[8] = (f8, 'Rows are the strings 0ⁱ and columns the suffixes 1ʲ. Only the diagonal entries are in L, so each 0ⁱ is separated from every other 0ʲ by its own suffix 1ⁱ, and the four strings fill 4 classes.',
          'A 4 by 4 table with prefixes ε, 0, 00, 000 as rows and suffixes ε, 1, 11, 111 as columns, marked in L only on the diagonal.')


# ---- 2.9 a DFA for a 10-digit mobile number ----
def f9():
    o = [T(20, 26, 'R = [6-9][0-9]{9}', 15, 'start', AC, True)]
    r, y = 17, 100
    xs = [40 + k * 64 for k in range(11)]
    for k, x in enumerate(xs):
        fin = k == 10
        if k < 10:
            o.append(L(x + r, y, xs[k + 1] - r - 3, y, AC, 2, arrow='n') if k < 10 else '')
        o.append(state(x, y, f'q{k}', accept=fin, r=r, fill=NXS if fin else PANEL, stroke=NX if fin else AC, size=12))
    o.append(lab(72, 92, '6–9', AC, 13))
    o.append(brace(xs[1], xs[10], 62, AC, up=True)); o.append(T((xs[1] + xs[10]) / 2, 52, 'nine more digits, each any 0–9', 13, fill=AC, bold=True))
    o.append(state(40, 200, 'd', r=r, fill=LVS, stroke=LV))
    o.append(L(40, y + r, 40, 200 - r - 3, LV, 2, arrow='l')); o.append(lab(64, 152, '0–5', LV, 13))
    o.append(loop(40, 200, r=r, up=False, c=LV)); o.append(T(80, 250, '0–9, dead state', 13, 'start', LV, True))
    o.append(T(250, 186, '9876543210: first digit 9 → q1 … → q10, accept', 14, 'start', NX, True))
    o.append(T(250, 214, '1234567890: first digit 1 → d, stays there, reject', 14, 'start', LV, True))
    o.append(T(20, 290, '11 live states q0 to q10 plus the dead state d = 12 states.', 14, 'start', INK, True))
    return 306, ''.join(o)
FIG[9] = (f9, 'The DFA for [6-9][0-9]{9} reads ten digits from q0 to the accepting q10. 9876543210 ends at q10 and is accepted; 1234567890 leaves q0 on its first digit 1 into the dead state d and is rejected.',
          'A chain of states q0 to q10, the first edge labelled 6–9 and the rest braced as any digit 0–9, with q0 dropping to a dead state d on 0–5, and the two test numbers below.')


spec = make_spec(FIG)


def text_fixes(k):
    """sentences in the chapter text that describe the figure, rewritten to match the drawing above"""
    return {
        9: [('The figure follows one short run on x12+7.',
             'The figure shows a small scanner-style DFA of the same kind: the 10-digit mobile-number checker built in the worked example below, with one number accepted and one rejected.')],
    }.get(k, [])
