"""Claude's hand-drawn figures for c-toc-u1 (Theory of Computation, unit 1: languages, finite automata, NFA, ε-NFA,
subset construction, minimisation, Mealy/Moore and two-way machines), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def lab(x, y, s, c=AC, size=14):
    return Tb(x, y, s, size, fill=c, bold=True)


def chip(x, y, s, c=AC, f=ACS, w=None, size=14):
    w = w or tw(s, size) + 22
    return R(x - w / 2, y - 16, w, 32, f, c, 16, 2) + T(x, y + 5, s, size, fill=c, bold=True)


# ---- 1.1 L inside L* inside Σ* ----
def f1():
    o = []
    o.append(R(20, 20, 680, 300, PANEL, L2, 18, 1.6))
    o.append(T(40, 46, 'Σ* : every string over {0, 1}', 14, 'start', INK, True))
    o.append(R(60, 64, 440, 236, ACS, AC, 18, 2))
    o.append(T(80, 90, 'L* : every even-length string, ε included', 14, 'start', AC, True))
    o.append(R(100, 112, 220, 120, NXS, NX, 16, 2))
    o.append(T(120, 138, 'L : length exactly 2', 14, 'start', NX, True))
    for i, s in enumerate(['00', '01', '10', '11']):
        o.append(TM(140 + i * 46, 180, s, 16, 'middle', NX, True))
    o.append(T(210, 216, '|L| = 4', 13, fill=NX, bold=True))
    for x, y, s in ((380, 140, 'ε'), (380, 186, '0000'), (430, 232, '011010')):
        o.append(TM(x, y, s, 16, 'middle', AC, True))
    o.append(T(280, 270, 'L² = all 16 strings of length 4, e.g. 0000', 13, fill=AC, bold=True))
    for x, y, s in ((560, 120, '0'), (600, 180, '010'), (570, 240, '11111')):
        o.append(TM(x, y, s, 16, 'middle', MUT, True))
    o.append(T(600, 290, 'odd lengths: outside L*', 13, fill=MUT, bold=True))
    o.append(T(20, 346, 'The complement of L is everything outside the inner box: ε, 0000 and 010 all belong to it.', 13, 'start', INK))
    return 362, ''.join(o)
FIG[1] = (f1, 'The boxes nest L = {00, 01, 10, 11} inside L*, which is every even-length string, inside Σ*. The string 0000 is in L* (it is in L²) but not in L, while odd strings such as 010 lie outside L*.',
          'Three nested boxes: Σ* containing L*, the even-length strings, containing L = {00, 01, 10, 11}; sample strings ε and 0000 sit in L* only, and 0, 010 and 11111 sit outside L*.')


def dfa_abc(o, P_, edges, finals, start='A'):
    for n, (x, y) in P_.items():
        o.append(state(x, y, n, accept=n in finals, start=n == start, fill=NXS if n in finals else PANEL, stroke=NX if n in finals else AC))
    for e in edges:
        o.append(e)


# ---- 1.2 DFA for strings ending in 01 ----
def f2():
    o = []
    P_ = {'A': (130, 140), 'B': (330, 140), 'C': (530, 140)}
    E = [loop(130, 140), lab(130, 82, '1'), edge(P_['A'], P_['B']), lab(230, 132, '0'), loop(330, 140), lab(330, 82, '0'),
         edge(P_['B'], P_['C'], bend=0.12), lab(430, 116, '1'), edge(P_['C'], P_['B'], bend=0.12), lab(430, 172, '0'),
         edge(P_['C'], P_['A'], bend=0.32), lab(330, 238, '1')]
    dfa_abc(o, P_, E, {'C'})
    o.append(T(130, 184, 'ε', 13, fill=MUT)); o.append(T(330, 184, 'seen 0', 13, fill=MUT)); o.append(T(530, 184, 'seen 01', 13, fill=NX, bold=True))
    o.append(T(20, 290, '1001:  A → A → B → B → C   ends in C, accept', 14, 'start', NX, True))
    o.append(T(20, 316, '110:   A → A → A → B         ends in B, reject', 14, 'start', LV, True))
    return 332, ''.join(o)
FIG[2] = (f2, 'Each state remembers the longest suffix that could still become 01: A for none, B for 0, C for 01, the only accepting state. 1001 ends in C and is accepted; 110 ends in B and is rejected. From C, a 1 goes back to A.',
          'A three-state DFA: A loops on 1 and goes to B on 0; B loops on 0 and goes to C on 1; C, double-circled, goes to B on 0 and back to A on 1, with the runs of 1001 and 110 below.')


# ---- 1.3 δ̂ column by column ----
def f3():
    o = [T(20, 26, 'δ(A,0)=B, δ(A,1)=A, δ(B,0)=B, δ(B,1)=C, δ(C,0)=C, δ(C,1)=C;  start A, final C', 14, 'start', bold=True)]
    def run(x0, w, states, ok):
        y = 70
        o.append(T(x0 - 28, y + 5, 'read', 13, 'end', MUT, True)); o.append(T(x0 - 28, y + 55, 'state', 13, 'end', MUT, True))
        for i, s in enumerate(states):
            x = x0 + i * 62
            o.append(TM(x, y + 5, 'ε' if i == 0 else w[i - 1], 16, 'middle', INK, True))
            fin = s == 'C'
            o.append(state(x, y + 50, s, accept=fin, fill=NXS if fin else PANEL, stroke=NX if fin else AC, r=20))
            if i: o.append(L(x - 40, y + 50, x - 24, y + 50, AC, 2, arrow='n'))
        o.append(T(x0 + (len(states) - 1) * 31, y + 110, ('δ̂(A, ' + w + ') = ' + states[-1]) + (', accept' if ok else ', reject'), 14, fill=NX if ok else LV, bold=True))
    run(80, '1001', ['A', 'A', 'B', 'B', 'C'], True)
    run(470, '110', ['A', 'A', 'A', 'B'], False)
    o.append(T(20, 236, 'Each step applies δ to the state reached so far: δ̂(A, wa) = δ(δ̂(A, w), a).', 13, 'start', MUT, True))
    return 252, ''.join(o)
FIG[3] = (f3, 'Each column is one more symbol read and the state reached after it. For 1001 the run ends in C, a final state, so it is accepted; for 110 it ends in B and is rejected.',
          'Two runs drawn as rows of states under the symbols read: 1001 giving A, A, B, B, C, accepted, and 110 giving A, A, A, B, rejected.')


# ---- 1.4 NFA: third symbol from the right is 1 ----
def f4():
    o = []
    P_ = [(110, 90), (270, 90), (430, 90), (590, 90)]
    for i, (x, y) in enumerate(P_):
        o.append(state(x, y, f'q{i}', accept=i == 3, start=i == 0, fill=NXS if i == 3 else PANEL, stroke=NX if i == 3 else AC))
    o.append(loop(110, 90)); o.append(lab(110, 32, '0, 1'))
    for i, s in enumerate(['1 (guess)', '0, 1', '0, 1']):
        o.append(edge(P_[i], P_[i + 1])); o.append(lab((P_[i][0] + P_[i + 1][0]) / 2, 82, s, LV if i == 0 else AC))
    y = 210
    sets = ['{q0}', '{q0}', '{q0, q1}', '{q0, q1, q2}', '{q0, q2, q3}']
    xs = [50, 170, 300, 460, 630]
    o.append(T(20, y - 50, 'Trace 0110: the machine is in a set of states at once', 14, 'start', bold=True))
    for i, (x, s) in enumerate(zip(xs, sets)):
        last = i == 4
        o.append(chip(x, y, s, NX if last else AC, NXS if last else ACS))
        if i:
            px = xs[i - 1] + (tw(sets[i - 1]) + 22) / 2 + 4
            o.append(L(px, y, x - (tw(s) + 22) / 2 - 4, y, INK, 1.8, arrow='m'))
            o.append(T((px + x - (tw(s) + 22) / 2) / 2, y - 22, '0110'[i - 1], 15, fill=INK, bold=True))
    o.append(T(630, y + 40, 'holds q3: accept', 13, fill=NX, bold=True))
    o.append(T(20, y + 78, 'The third symbol from the right of 0110 is the first 1, the one where q1 was guessed.', 13, 'start', MUT))
    return y + 94, ''.join(o)
FIG[4] = (f4, 'Each box is the set of states the NFA may be in after another symbol of 0110. The guess adds q1 at the first 1, and after the last 0 the set contains q3, so the string is accepted.',
          'An NFA q0 to q3 where q0 loops on 0 and 1 and guesses into q1 on 1, then 0 or 1 to q2 and q3; below, the state sets {q0}, {q0}, {q0, q1}, {q0, q1, q2}, {q0, q2, q3} while reading 0110.')


# ---- 1.5 ε-NFA and its closures ----
def f5():
    o = []
    P_ = [(110, 100), (270, 100), (430, 100), (590, 100)]
    for i, (x, y) in enumerate(P_):
        o.append(state(x, y, f'q{i}', accept=i == 3, start=i == 0, fill=NXS if i == 3 else PANEL, stroke=NX if i == 3 else AC))
    o.append(loop(110, 100)); o.append(lab(110, 42, 'a'))
    o.append(loop(590, 100)); o.append(lab(590, 42, 'a'))
    o.append(edge(P_[0], P_[1], c=LV, arrow='l', dash='6 4')); o.append(lab(190, 92, 'ε', LV))
    o.append(edge(P_[1], P_[2])); o.append(lab(350, 92, 'b'))
    o.append(edge(P_[2], P_[3], c=LV, arrow='l', dash='6 4')); o.append(lab(510, 92, 'ε', LV))
    o.append(T(20, 168, 'ε-closures:', 14, 'start', bold=True))
    for i, s in enumerate(['{q0, q1}', '{q1}', '{q2, q3}', '{q3}']):
        o.append(T(140 + i * 150, 168, f'q{i} → {s}', 14, 'start', LV if i in (0, 2) else MUT, True))
    y = 226
    o.append(T(20, y + 5, 'read ab:', 14, 'start', bold=True))
    xs = [170, 360, 560]
    for i, (x, s, c) in enumerate(zip(xs, ['{q0, q1}', '{q0, q1}', '{q2, q3}'], [AC, AC, NX])):
        o.append(chip(x, y, s, c, NXS if c == NX else ACS))
        if i:
            o.append(L(xs[i - 1] + 50, y, x - 54, y, INK, 1.8, arrow='m'))
            o.append(T((xs[i - 1] + x) / 2, y - 22, 'ab'[i - 1] + ', then close', 13, fill=INK, bold=True))
    o.append(T(560, y + 40, 'q3 is final: accept', 13, fill=NX, bold=True))
    o.append(T(20, y + 76, 'Without the ε-edges the final states become {q2, q3}, since ECLOSE(q2) already reaches q3.', 13, 'start', MUT))
    return y + 92, ''.join(o)
FIG[5] = (f5, 'The two dashed edges read nothing, so the machine starts in {q0, q1}, and the moment it reaches q2 it is also in the final q3. Reading ab therefore ends in {q2, q3} and is accepted.',
          'An ε-NFA q0, q1, q2, q3 with a-loops on q0 and q3, a b-edge from q1 to q2 and dashed ε-edges q0 to q1 and q2 to q3; below, the four closures and the sets {q0, q1}, {q0, q1}, {q2, q3} while reading ab.')


# ---- 1.6 subset construction ----
def f6():
    o = []
    P_ = {'A': (130, 130), 'B': (360, 130), 'C': (590, 130)}
    names = {'A': '{q0}', 'B': '{q0, q1}', 'C': '{q0, q2}'}
    E = [loop(130, 130), lab(130, 72, 'b'), edge(P_['A'], P_['B']), lab(245, 122, 'a'), loop(360, 130), lab(360, 72, 'a'),
         edge(P_['B'], P_['C'], bend=0.12), lab(475, 104, 'b'), edge(P_['C'], P_['B'], bend=0.12), lab(475, 164, 'a'),
         edge(P_['C'], P_['A'], bend=0.3), lab(360, 236, 'b')]
    dfa_abc(o, P_, E, {'C'})
    for n, (x, y) in P_.items():
        o.append(T(x, y + 46, names[n], 14, fill=NX if n == 'C' else AC, bold=True))
    o.append(T(20, 286, 'C is final because it holds q2. Only 3 of the 2³ = 8 subsets are reachable; the DFA accepts strings ending in ab.', 13, 'start', INK, True))
    return 302, ''.join(o)
FIG[6] = (f6, 'Each DFA state is a set of NFA states: A = {q0} is the start and C = {q0, q2} is final because it holds q2. A on b stays at A, B on b goes to C, and C on b returns to A, so the DFA accepts exactly the strings ending in ab.',
          'A three-state DFA with states labelled {q0}, {q0, q1} and {q0, q2}: A loops on b and goes to B on a; B loops on a and goes to C on b; C, double-circled, goes to B on a and to A on b.')


# ---- 1.7 table filling and the quotient ----
def f7():
    o = [T(20, 26, 'Pairs of states: X = marked in pass 0 (final vs non-final), 1 = marked in pass 1', 14, 'start', bold=True)]
    x0, y0, cw = 90, 50, 66
    rows = ['q1', 'q2', 'q3']; cols = ['q0', 'q1', 'q2']
    marks = {('q1', 'q0'): 'X', ('q2', 'q0'): 'X', ('q3', 'q1'): 'X', ('q3', 'q2'): 'X', ('q2', 'q1'): '1', ('q3', 'q0'): ''}
    for i, r in enumerate(rows):
        o.append(T(x0 - 12, y0 + i * 50 + 31, r, 14, 'end', INK, True))
        for j in range(i + 1):
            m = marks[(r, cols[j])]
            x, y = x0 + j * cw, y0 + i * 50
            f, c = (LVS, LV) if m == '1' else ((NXS, NX) if m == '' else (PANEL, L2))
            o.append(R(x, y, cw - 4, 46, f, c, 3, 2 if m != 'X' else 1.2))
            o.append(T(x + (cw - 4) / 2, y + 30, m if m else 'same', 15 if m else 13, fill=c if m else NX, bold=True))
    for j, c in enumerate(cols):
        o.append(T(x0 + j * cw + (cw - 4) / 2, y0 + 3 * 50 + 22, c, 14, fill=INK, bold=True))
    o.append(T(20, 250, 'q1q2 on a → q2q0, already X, so mark it.', 13, 'start', LV, True))
    o.append(T(20, 270, 'q0q3 on a → q1q1, on b → q3q3: never marked.', 13, 'start', NX, True))
    # quotient DFA
    P_ = {'A': (420, 120), 'B': (560, 120), 'C': (490, 230)}
    o.append(state(420, 120, 'A', accept=True, start=True, fill=NXS, stroke=NX))
    o.append(state(560, 120, 'B')); o.append(state(490, 230, 'C'))
    o.append(edge(P_['A'], P_['B'])); o.append(lab(490, 112, 'a'))
    o.append(edge(P_['B'], P_['C'])); o.append(lab(540, 182, 'a'))
    o.append(edge(P_['C'], P_['A'])); o.append(lab(440, 182, 'a'))
    o.append(loop(420, 120)); o.append(lab(420, 62, 'b')); o.append(loop(560, 120)); o.append(lab(560, 62, 'b'))
    o.append(loop(490, 230, up=False)); o.append(lab(490, 296, 'b'))
    o.append(T(620, 200, 'A = {q0, q3}', 13, 'start', NX, True)); o.append(T(620, 220, 'B = {q1}', 13, 'start', AC, True))
    o.append(T(620, 240, 'C = {q2}', 13, 'start', AC, True))
    o.append(T(20, 320, 'Merge q0 and q3: 3 states, accepting strings whose number of a’s is divisible by 3.', 14, 'start', NX, True))
    return 336, ''.join(o)
FIG[7] = (f7, 'Pass 0 marks every final/non-final pair; pass 1 marks q1q2, because on a it reaches the marked q0q2; pass 2 marks nothing. q0q3 is never marked, so q0 and q3 merge, leaving a 3-state DFA that counts a’s mod 3.',
          'A triangular pair table with X in q0q1, q0q2, q1q3, q2q3, a 1 in q1q2 and q0q3 left unmarked, beside the minimal DFA A, B, C cycling on a and looping on b.')


# ---- 1.8 Mealy against Moore on 0101 ----
def f8():
    o = []
    o.append(T(20, 26, 'Mealy: output on the edge', 14, 'start', AC, True))
    S0, S1 = (90, 110), (270, 110)
    o.append(state(*S0, 'S0', start=True)); o.append(state(*S1, 'S1'))
    o.append(loop(*S0)); o.append(lab(90, 52, '1/0'))
    o.append(loop(*S1)); o.append(lab(270, 52, '0/0'))
    o.append(edge(S0, S1, bend=0.15)); o.append(lab(180, 86, '0/0'))
    o.append(edge(S1, S0, bend=0.15, c=LV)); o.append(lab(180, 146, '1/1', LV))
    o.append(T(390, 26, 'Moore: output in the state', 14, 'start', NX, True))
    A, B, C_ = (440, 110), (570, 110), (680, 110)
    o.append(state(*A, 'A/0', start=True, r=26, stroke=NX, size=13)); o.append(state(*B, 'B/0', r=26, stroke=NX, size=13))
    o.append(state(*C_, 'C/1', r=26, stroke=LV, fill=LVS, size=13))
    o.append(loop(*A, r=26)); o.append(lab(440, 50, '1'))
    o.append(loop(*B, r=26)); o.append(lab(570, 50, '0'))
    o.append(edge(A, B, r=26)); o.append(lab(505, 102, '0'))
    o.append(edge(B, C_, r=26, bend=0.2)); o.append(lab(625, 80, '1'))
    o.append(edge(C_, B, r=26, bend=0.2)); o.append(lab(622, 152, '0'))
    o.append(edge(C_, A, r=26, bend=0.3)); o.append(lab(560, 178, '1'))
    # runs
    y = 214
    o.append(T(130, y, 'input', 13, 'end', MUT, True))
    for i, ch in enumerate('0101'):
        o.append(TM(220 + i * 56, y, ch, 16, 'middle', INK, True))
    rows = [('Mealy', ['', '0', '1', '0', '1'], AC, '0101 (4 symbols)'), ('Moore', ['0', '0', '1', '0', '1'], NX, '00101 (5 symbols)')]
    for r, (n, outs, c, tot) in enumerate(rows):
        yy = y + 36 + r * 36
        o.append(T(130, yy, n + ' prints', 13, 'end', c, True))
        for i, v in enumerate(outs):
            if v: o.append(TM(164 + i * 56, yy, v, 16, 'middle', c if not (n == 'Moore' and i == 0) else LV, True))
        o.append(T(460, yy, tot, 14, 'start', c, True))
    o.append(T(164, y + 104, 'extra leading 0 from the start state', 13, 'start', LV, True))
    return y + 120, ''.join(o)
FIG[8] = (f8, 'Both machines read 0101. Mealy prints one symbol per move, 0101; Moore prints on entering each state, so its start state adds an extra leading 0 and it prints 00101.',
          'Left, a Mealy machine S0, S1 with edge labels 0/0, 1/0 and 1/1; right, a Moore machine A/0, B/0, C/1; below, input 0101 with Mealy output 0101 and Moore output 00101.')


# ---- 1.9 a two-way finite automaton ----
def f9():
    o = []
    cells = ['⊢', 'a', 'b', 'a', '⊣']
    x0, cw = 200, 70
    for i, s in enumerate(cells):
        o.append(R(x0 + i * cw, 20, cw - 4, 40, PANEL if i in (0, 4) else ACS, L2 if i in (0, 4) else AC, 3, 1.6))
        o.append(T(x0 + i * cw + (cw - 4) / 2, 46, s, 17, fill=INK, bold=True))
    moves = [('q0', 0), ('q1', 1), ('q1', 2), ('q1', 3), ('q1', 4), ('q2', 3), ('qf', 4)]
    pts = []
    for t, (q, pos) in enumerate(moves):
        x, y = x0 + pos * cw + (cw - 4) / 2, 90 + t * 34
        pts.append((x, y))
        c = LV if q == 'q2' else (NX if q == 'qf' else AC)
        o.append(C(x, y, 7, c))
        o.append(T(x + 14, y + 5, q, 13, 'start', c, True))
        o.append(T(x0 - 20, y + 5, f'move {t}' if t else 'start', 13, 'end', MUT))
    o.append(P(pts, L2, 1.6, '4 3'))
    o.append(T(x0 + 4 * cw + 70, 90 + 5 * 34 - 12, '← the step left', 13, 'start', LV, True))
    o.append(T(x0 + 4 * cw + 70, 90 + 5 * 34 + 6, 'a DFA cannot make', 13, 'start', LV, True))
    y = 90 + 7 * 34
    o.append(T(20, y + 4, 'q1 sweeps right to ⊣, steps back to the last symbol; on a it halts in qf (accept), on b in d (reject).', 13, 'start', INK, True))
    o.append(T(20, y + 26, 'So the machine accepts exactly the non-empty strings over {a, b} that end in a.', 13, 'start', NX, True))
    return y + 42, ''.join(o)
FIG[9] = (f9, 'The head sweeps right through a, b, a in q1, reads ⊣ and steps one cell left into q2, the backward move an ordinary DFA cannot make. q2 then reads the last a and halts in qf, so aba is accepted.',
          'A tape ⊢ a b a ⊣ with the head position drawn below it move by move: q0 on ⊢, q1 on each symbol up to ⊣, q2 back on the last a, then qf.')


spec = make_spec(FIG)


def text_fixes(k):
    """sentences in the chapter text that describe the figure, rewritten to match the drawing above"""
    return {
        3: [('The figure shows δ̂(A, 1001). The rows are prefixes, not separate runs. The last row gives C, a final state, so 1001 is accepted.',
             'The figure draws δ̂(A, 1001) as one row of states, a column for each symbol read, with the run of 110 beside it for contrast. The 1001 row ends in C, a final state, so 1001 is accepted.')],
        9: [('Using the machine in the figure (states q0, q1, q2, qf, d), trace the inputs aba and abb',
             'A 2FA has states q0, q1, q2, qf and d, with F = {qf}: δ(q0, ⊢) = (q1, R), q1 moves R over a and b, δ(q1, ⊣) = (q2, L), δ(q2, a) = (qf, R) and δ(q2, b) = (d, R). The figure draws its run on aba. Trace the inputs aba and abb'),
            ('Trace input ba on the figure\'s machine and give the verdict.',
             'Trace input ba on the 2FA of the worked example (the machine whose run on aba the figure draws) and give the verdict.')],
    }.get(k, [])
