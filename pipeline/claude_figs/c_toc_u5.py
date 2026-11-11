"""Claude's hand-drawn figures for c-toc-u5 (Theory of Computation, unit 5: Turing machines, acceptance, unary
arithmetic, multitape and nondeterministic machines, the universal machine, the Church-Turing thesis and storage in the
state), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def chip(x, y, s, c=AC, f=ACS, size=14):
    w = max(40, tw(s, size) + 18)
    return R(x - w / 2, y - 15, w, 30, f, c, 15, 2) + T(x, y + 5, s, size, fill=c, bold=True)


def tape(o, x0, y, cells, head=None, cw=40, h=34, hc=AC, changed=(), size=16):
    """a row of tape cells; head = index of the scanned cell (marked with a triangle above it)"""
    for i, s in enumerate(cells):
        ch = i in changed
        o.append(R(x0 + i * cw, y, cw - 3, h, LVS if ch else (ACS if i == head else PANEL), LV if ch else (hc if i == head else L2), 3, 2 if (ch or i == head) else 1.4))
        o.append(T(x0 + i * cw + (cw - 3) / 2, y + h / 2 + 6, s, size, fill=MUT if s == '□' else INK, bold=True))
    if head is not None:
        hx = x0 + head * cw + (cw - 3) / 2
        o.append(f'<polygon points="{hx - 7:.1f},{y - 12:.1f} {hx + 7:.1f},{y - 12:.1f} {hx:.1f},{y - 2:.1f}" style="fill:{hc}"/>')


# ---- 5.1 the run on 00 ----
def f1():
    o = []
    rows = [('start', 'q0', ['0', '0', '□', '□'], 0, (), 'q0 0 0'),
            ('move 1: δ(q0, 0) = (q1, 1, R)', 'q1', ['1', '0', '□', '□'], 1, (0,), '1 q1 0'),
            ('move 2: δ(q1, 0) = (q2, 0, R)', 'q2', ['1', '0', '□', '□'], 2, (), '1 0 q2 □'),
            ('move 3: δ(q2, □) = (qaccept, □, L)', 'qaccept', ['1', '0', '□', '□'], 1, (), '1 qaccept 0')]
    o.append(T(30, 22, 'cell', 13, 'start', MUT));
    for i in range(4): o.append(T(64 + i * 44 + 20, 22, str(i), 13, fill=MUT))
    o.append(T(470, 22, 'instantaneous description', 13, 'start', MUT, True))
    for j, (mv, q, cells, hd, chg, idd) in enumerate(rows):
        y = 52 + j * 82
        fin = q == 'qaccept'
        tape(o, 64, y + 14, cells, hd, 44, 34, NX if fin else AC, chg)
        o.append(chip(470, y + 31, q, NX if fin else AC, NXS if fin else ACS, 13))
        o.append(TM(560, y + 36, idd, 15, 'start', NX if fin else INK, True))
        o.append(T(64, y + 66, mv, 13, 'start', MUT if j == 0 else INK))
    o.append(T(20, 388, 'Three moves, then qaccept halts the machine. The written 1 is highlighted; □ is a blank cell.', 13, 'start', NX, True))
    return 402, ''.join(o)
FIG[1] = (f1, 'The machine on input 00, one row per configuration: the triangle is the head, and the chip is the state in the finite control. Move 1 writes 1 over the first 0, and after three moves the machine halts in qaccept.',
          'Four tape rows for the input 00: q0 on cell 0; q1 on cell 1 after writing 1; q2 on the blank cell 2; qaccept back on cell 1, with the matching instantaneous descriptions q000, 1q10, 10q2□ and 1qaccept0.')


# ---- 5.2 accept 001, reject 000 ----
def f2():
    o = []
    o.append(T(20, 28, 'δ(q0, 0) = (q0, 0, R)  ·  δ(q0, 1) = (qaccept, 1, R)  ·  δ(q0, □) = (qreject, □, R)', 14, 'start', INK, True))
    for j, (w, verdict, c, f) in enumerate((('001', 'qaccept: 001 accepted (1)', NX, NXS), ('000', 'qreject: 000 rejected (0)', LV, LVS))):
        y = 80 + j * 140
        cells = list(w) + ['□', '□']
        stop = w.index('1') if '1' in w else len(w)
        o.append(T(20, y + 22, f'input {w}', 14, 'start', MUT, True))
        tape(o, 130, y, cells, None, 50, 36)
        for i in range(stop + 1):
            x = 130 + i * 50 + 23
            o.append(C(x, y + 58, 6, AC if i < stop else c))
            o.append(T(x, y + 82, f'{i}', 13, fill=MUT))
            if i < stop: o.append(L(x + 8, y + 58, x + 40, y + 58, AC, 2, arrow='n'))
        xe = 130 + stop * 50 + 23
        o.append(R(130 + stop * 50 - 2, y - 4, 51, 44, 'none', c, 5, 2.5))
        o.append(chip(570, y + 18, verdict, c, f, 13))
        o.append(T(130, y + 108, f'0: stay in q0 and move right · move {stop + 1} reads ' + ('1' if '1' in w else '□') + ' and halts', 13, 'start', INK))
    return 344, ''.join(o)
FIG[2] = (f2, 'The machine walks right over 0s. On 001 the first 1 sends it to qaccept after 3 moves; on 000 it reaches the blank after the input and qreject halts it after 4 moves.',
          'Two tapes, 001 and 000, with the head positions 0, 1, 2 (and 3) marked below; 001 stops on its 1 in qaccept, 000 stops on the blank in qreject.')


# ---- 5.3 unary addition 0010 → 000 ----
def f3():
    o = []
    rows = [('start: 2 and 1 in unary, separator 1', 'q0', ['0', '0', '1', '0', '□'], 0, ()),
            ('q0 turns the 1 into 0 and moves on', 'q1', ['0', '0', '0', '0', '□'], 3, (2,)),
            ('q1 hits the blank and steps back', 'q2', ['0', '0', '0', '0', '□'], 3, ()),
            ('q2 erases the last 0 and halts', 'qa', ['0', '0', '0', '□', '□'], 2, (3,))]
    for j, (mv, q, cells, hd, chg) in enumerate(rows):
        y = 40 + j * 74
        fin = q == 'qa'
        tape(o, 70, y, cells, hd, 46, 36, NX if fin else AC, chg)
        o.append(chip(36, y + 18, q, NX if fin else AC, NXS if fin else ACS, 13))
        o.append(T(320, y + 24, mv, 14, 'start', NX if fin else INK, fin))
    o.append(L(10, 340, 710, 340, LN, 1))
    o.append(T(20, 368, '0 0 1 0 means 2 + 1. The tape ends as 0 0 0, the unary code for 3: f(2, 1) = 3.', 14, 'start', NX, True))
    return 384, ''.join(o)
FIG[3] = (f3, 'Adding 2 + 1 in unary: the separator 1 is overwritten by 0, the head runs to the blank and steps back, and the last 0 is erased. The tape 0010 becomes 000, which codes 3.',
          'Four tape rows: 0010 with q0 on cell 0; 0000 with q1 on cell 3 after the 1 became 0; q2 back on cell 3; 000 with qa on cell 2 after the last 0 was erased.')


# ---- 5.4 two tapes on 0011 ----
def f4():
    o = []
    snaps = [('start', 'q0', 0, ['B', 'B', 'B'], 0, ()),
             ('after move 2', 'q0', 2, ['0', '0', 'B'], 2, (0, 1)),
             ('after move 4', 'q1', 2, ['0', '0', 'B'], 1, ()),
             ('after move 5', 'q1', 3, ['0', 'B', 'B'], 0, (1,)),
             ('after move 6', 'q1', 4, ['B', 'B', 'B'], 0, (0,))]
    for i, (lab, q, h1, t2, h2, chg) in enumerate(snaps):
        x0 = 12 + i * 141
        o.append(T(x0 + 64, 24, lab, 13, fill=MUT, bold=True))
        o.append(chip(x0 + 64, 52, q, AC, ACS, 13))
        o.append(T(x0, 96, 'tape 1', 13, 'start', MUT))
        tape(o, x0, 116, ['0', '0', '1', '1', 'B'], h1, 26, 30, AC, (), 14)
        o.append(T(x0, 178, 'tape 2', 13, 'start', MUT))
        tape(o, x0, 198, t2, h2, 26, 30, NX, chg, 14)
    o.append(L(10, 250, 710, 250, LN, 1))
    o.append(T(20, 278, 'Phase 1 copies each 0 onto tape 2. Phase 2 erases one copied 0 for each 1 (head 2 moves left).', 13, 'start', INK))
    o.append(T(20, 300, 'Move 7 sees blanks under both heads and accepts: 0011 is in L, after 2n + 3 = 7 moves.', 13, 'start', NX, True))
    return 314, ''.join(o)
FIG[4] = (f4, 'Snapshots of the two-tape machine on 0011: both heads move in the same step, head 1 over the input and head 2 over the copies. Every 1 erases one copied 0, and when both heads see blanks the machine accepts at move 7.',
          'Five snapshots, each with tape 1 holding 0011 and tape 2 below it: tape 2 goes from blank to 0 0, then 0, then blank again, with each head’s position marked.')


# ---- 5.5 U simulating M on 101 ----
def f5():
    o = []
    o.append(T(20, 26, 'code(M), stored on U’s tape:', 13, 'start', MUT, True))
    rules = ['q0,1 → q1,R', 'q0,0 → q0,R', 'q1,1 → q1,R', 'q1,0 → q0,R']
    for i, r in enumerate(rules):
        o.append(R(20 + i * 172, 38, 160, 32, PANEL, L2, 6, 1.4))
        o.append(TM(100 + i * 172, 59, r, 14, 'middle', INK, True))
    o.append(T(20, 104, 'simulated tape of M', 13, 'start', MUT, True))
    o.append(T(290, 104, 'simulated state', 13, 'middle', MUT, True))
    o.append(T(390, 104, 'rule U finds in code(M)', 13, 'start', MUT, True))
    rows = [(0, 'q0', 'q0,1 → q1,R', 0), (1, 'q1', 'q1,0 → q0,R', 3), (2, 'q0', 'q0,1 → q1,R', 0), (3, 'q1', 'none: M halts in q1', None)]
    for j, (hd, q, r, ri) in enumerate(rows):
        y = 130 + j * 56
        tape(o, 20, y, ['1', '0', '1', '□'], hd, 44, 34)
        fin = ri is None
        o.append(chip(290, y + 17, q, NX if fin else AC, NXS if fin else ACS, 13))
        o.append(TM(390, y + 22, r, 14, 'start', NX if fin else INK, True))
    o.append(L(10, 360, 710, 360, LN, 1))
    o.append(T(20, 386, 'Each cycle: read the simulated state and symbol, look the rule up in code(M), apply it. After 3 moves no rule', 13, 'start', INK))
    o.append(T(20, 406, 'applies; M has halted in its accept state q1, so U accepts ⟨code(M), 101⟩.', 13, 'start', NX, True))
    return 420, ''.join(o)
FIG[5] = (f5, 'U keeps M’s rules, M’s tape and M’s current state on its own tape. Each cycle it looks up the rule for the current state and symbol and applies it; on 101, after 3 moves no rule applies in q1, so M halts accepting and U accepts too.',
          'At the top, M’s four rules as stored in code(M); below, four rows of the simulated tape 101 with the head moving right, the simulated state q0, q1, q0, q1, and the rule U uses at each step.')


# ---- 5.6 the Church-Turing thesis on (λn.n+1) 5 ----
def f6():
    o = []
    xs = [110, 360, 610]
    for x, s, last in zip(xs, ['(λn.n+1) 5', '5 + 1', '6'], [False, False, True]):
        o.append(R(x - 90, 24, 180, 50, NXS if last else PANEL, NX if last else AC, 10, 2))
        o.append(T(x, 56, s, 18, fill=NX if last else INK, bold=True))
    for (a, b), lab in zip(((110, 360), (360, 610)), ('substitute 5 for n', 'add')):
        o.append(L(a + 94, 49, b - 94, 49, AC, 2, arrow='n'))
        o.append(T((a + b) / 2, 96, lab, 13, fill=AC, bold=True))
    o.append(T(360, 124, 'finitely many exact steps, so f is effectively computable', 13, fill=MUT, bold=True))
    o.append(L(10, 144, 710, 144, LN, 1))
    models = ['λ-calculus', 'recursive functions', 'Turing machines']
    for i, m in enumerate(models):
        x = 120 + i * 240
        o.append(R(x - 100, 166, 200, 40, ACS, AC, 8, 2))
        o.append(T(x, 191, m, 14, fill=AC, bold=True))
        o.append(L(x, 208, 360 + (x - 360) * 0.25, 248, AC, 2, arrow='n'))
    o.append(R(150, 252, 420, 44, NXS, NX, 10, 2))
    o.append(T(360, 279, 'the same class: effectively computable functions', 14, fill=NX, bold=True))
    o.append(T(360, 330, 'Thesis: that class is what Turing machines compute. So some Turing machine,', 13, fill=INK))
    o.append(T(360, 350, 'given 5 encoded on its tape, halts with 6 encoded on its tape.', 13, fill=INK))
    return 364, ''.join(o)
FIG[6] = (f6, 'The lambda term reduces to 6 in two exact steps, so the function is effectively computable. Three independent models define the same class of such functions, and the thesis says a Turing machine computes every one of them, including f(5) = 6.',
          'Top: (λn.n+1) 5 reduces to 5 + 1 and then to 6. Bottom: λ-calculus, recursive functions and Turing machines each point to one shared box, the effectively computable functions.')


# ---- 5.7 the state remembers the last two bits ----
def f7():
    o = []
    o.append(T(20, 28, 'input', 13, 'start', MUT, True))
    for i, b in enumerate('1101'):
        o.append(R(140 + i * 130 - 18, 12, 36, 30, PANEL, L2, 3, 1.4))
        o.append(T(140 + i * 130, 33, b, 16, fill=INK, bold=True))
    names = ['q00', 'q01', 'q11', 'q10', 'q01']
    for i, n in enumerate(names):
        x = 75 + i * 130
        last = i == 4
        o.append(state(x, 112, n, accept=False, start=i == 0, r=28, fill=NXS if last else PANEL, stroke=NX if last else AC, size=14))
        if i < 4:
            o.append(edge((x, 112), (x + 130, 112), r=28))
            o.append(Tb(x + 65, 100, f'read {"1101"[i]}', 13, fill=AC, bold=True))
    o.append(T(75, 166, 'after the', 13, fill=MUT)); o.append(T(75, 182, 'length check', 13, fill=MUT))
    o.append(T(595, 166, 'last two bits', 13, fill=NX, bold=True)); o.append(T(595, 182, 'are 0, 1', 13, fill=NX, bold=True))
    o.append(L(623, 112, 690, 112, NX, 2, arrow='x'))
    o.append(T(690, 98, '□', 15, 'end', NX, True))
    o.append(T(700, 140, 'accept', 13, 'end', NX, True))
    o.append(L(10, 206, 710, 206, LN, 1))
    o.append(T(20, 234, 'Rule: in qab, reading c, go to qbc and move right. The name qab means “the last two bits were a, b”.', 13, 'start', INK))
    o.append(T(20, 256, '4 memory states (q00, q01, q10, q11) remember the bits, so the tape never has to be read twice.', 13, 'start', INK))
    return 270, ''.join(o)
FIG[7] = (f7, 'The state’s name stores the last two bits read: qab on input c moves to qbc. Reading 1101 passes through q01, q11 and q10 and ends in q01, so on the blank the machine accepts.',
          'Above, the input 1101; below, the run q00, q01, q11, q10, q01 with each arrow labelled by the bit read, and an arrow from the last q01 on blank to accept.')


spec = make_spec(FIG)


def text_fixes(k):
    """no sentence in this unit's text describes the old drawings in a way the new ones contradict"""
    return []
