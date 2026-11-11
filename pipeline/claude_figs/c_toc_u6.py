"""Claude's hand-drawn figures for c-toc-u6 (Theory of Computation, unit 6: recursive and r.e. languages, reductions,
the halting problem, Rice's theorem, Post's correspondence problem, computable functions, time and space, P and NP),
one per chapter, from each chapter's worked example, plus the sentences in the chapter text that describe a figure."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def chip(x, y, s, c=AC, f=ACS, size=14):
    w = max(40, tw(s, size) + 18)
    return R(x - w / 2, y - 15, w, 30, f, c, 15, 2) + T(x, y + 5, s, size, fill=c, bold=True)


def tape(o, x0, y, cells, head=None, cw=44, h=34, hc=AC, changed=(), size=16):
    for i, s in enumerate(cells):
        ch = i in changed
        o.append(R(x0 + i * cw, y, cw - 3, h, LVS if ch else (ACS if i == head else PANEL), LV if ch else (hc if i == head else L2), 3, 2 if (ch or i == head) else 1.4))
        o.append(T(x0 + i * cw + (cw - 3) / 2, y + h / 2 + 6, s, size, fill=MUT if s == '□' else INK, bold=True))
    if head is not None:
        hx = x0 + head * cw + (cw - 3) / 2
        o.append(f'<polygon points="{hx - 7:.1f},{y - 12:.1f} {hx + 7:.1f},{y - 12:.1f} {hx:.1f},{y - 2:.1f}" style="fill:{hc}"/>')


# ---- 6.1 interleaving M and M′ ----
def f1():
    o = []
    u, x0 = 22, 110
    o.append(R(x0, 14, 22, 16, ACS, AC, 3, 1.4)); o.append(T(x0 + 30, 27, 'one step of M (accepts L)', 13, 'start', AC, True))
    o.append(R(x0 + 260, 14, 22, 16, PANEL, L2, 3, 1.4)); o.append(T(x0 + 290, 27, 'one step of M′ (accepts the complement)', 13, 'start', MUT, True))
    for k in range(1, 7):
        y = 30 + k * 40
        o.append(T(20, y + 18, f'round {k}', 14, 'start', INK, True))
        for i in range(2 * k):
            m = i < k
            hit = k == 6 and i == 5
            o.append(R(x0 + i * u, y, u - 3, 26, NXS if hit else (ACS if m else PANEL), NX if hit else (AC if m else L2), 3, 2 if hit else 1.2))
        o.append(T(x0 + 12 * u + 22, y + 18, f'total {k}·{k + 1} = {k * (k + 1)}', 14, 'start', NX if k == 6 else MUT, k == 6))
    hx = x0 + 5 * u + 9
    o.append(L(hx, 330, hx, 302, NX, 2, arrow='x'))
    o.append(T(hx, 350, 'M accepts 0110 at its 6th step', 13, fill=NX, bold=True))
    o.append(T(20, 384, 'Round k runs each machine for k steps, 2k in all. D stops in round 6, after 42 simulated steps, and prints yes.', 13, 'start', INK))
    return 398, ''.join(o)
FIG[1] = (f1, 'The decider D runs M and M′ in turns, k steps each in round k, so neither machine can block it. On w = 0110, M accepts at its 6th step, so D stops in round 6 after 6 · 7 = 42 simulated steps and prints yes.',
          'Six rows of step cells, round k holding k steps of M then k steps of M′, with running totals 2, 6, 12, 20, 30, 42; the 6th step of M in round 6 is marked as M accepting.')


# ---- 6.2 A_TM ≤m B, B = machines that accept 101 ----
def f2():
    o = []
    o.append(R(20, 30, 130, 50, PANEL, AC, 10, 2)); o.append(T(85, 61, '⟨M, w⟩', 16, fill=INK, bold=True))
    o.append(L(154, 55, 266, 55, AC, 2, arrow='n')); o.append(T(210, 44, 'f builds', 13, fill=AC, bold=True)); o.append(T(210, 76, 'never runs', 13, fill=MUT))
    o.append(R(270, 30, 130, 50, ACS, AC, 10, 2)); o.append(T(335, 61, '⟨M′⟩', 16, fill=AC, bold=True))
    o.append(L(404, 55, 516, 55, LV, 2, dash='6 4', arrow='l')); o.append(T(460, 44, 'decider for B?', 13, fill=LV, bold=True))
    o.append(R(520, 30, 180, 50, LVS, LV, 10, 2)); o.append(T(610, 52, 'would decide A_TM:', 13, fill=LV, bold=True)); o.append(T(610, 70, 'impossible', 13, fill=LV, bold=True))
    # what M′ does
    o.append(R(20, 110, 680, 170, PANEL, L2, 14, 1.4, '6 4'))
    o.append(T(36, 134, 'M′ on input x:', 14, 'start', AC, True))
    o.append(R(60, 160, 140, 44, ACS, AC, 8, 2)); o.append(T(130, 188, 'x = 101 ?', 15, fill=AC, bold=True))
    o.append(L(130, 206, 130, 238, LV, 2, arrow='l')); o.append(T(142, 228, 'no', 13, 'start', LV, True))
    o.append(R(80, 240, 100, 30, LVS, LV, 8, 2)); o.append(T(130, 260, 'reject', 14, fill=LV, bold=True))
    o.append(L(204, 182, 296, 182, NX, 2, arrow='x')); o.append(T(250, 172, 'yes', 13, fill=NX, bold=True))
    o.append(R(300, 160, 180, 44, PANEL, AC, 8, 2)); o.append(T(390, 188, 'simulate M on w', 15, fill=INK, bold=True))
    o.append(L(484, 182, 556, 182, NX, 2, arrow='x'))
    o.append(R(560, 160, 120, 44, NXS, NX, 8, 2)); o.append(T(620, 180, 'accept if', 13, fill=NX, bold=True)); o.append(T(620, 196, 'M accepts w', 13, fill=NX, bold=True))
    o.append(T(390, 240, 'if M never accepts w, M′ accepts nothing', 13, fill=MUT))
    o.append(T(20, 316, 'M accepts w  ⟺  M′ accepts 101  ⟺  ⟨M′⟩ ∈ B.  So A_TM ≤m B, and B is undecidable.', 14, 'start', NX, True))
    return 332, ''.join(o)
FIG[2] = (f2, 'The map f only writes the machine M′ down. M′ rejects every input except 101, and on 101 it accepts exactly when M accepts w, so M′ is in B exactly when ⟨M, w⟩ is in A_TM; a decider for B would therefore decide A_TM.',
          'Top: ⟨M, w⟩ is mapped by f to ⟨M′⟩, and a decider for B on ⟨M′⟩ would decide A_TM. Below, M′ on input x: if x is not 101 it rejects, otherwise it simulates M on w and accepts if M accepts.')


# ---- 6.3 the diagonal table ----
def f3():
    o = []
    rows = [('M1', 'yes no yes no'), ('M2', 'no no yes yes'), ('M3', 'yes yes no no'), ('M4', 'no yes no yes')]
    cw, ch, x0, y0 = 110, 40, 150, 50
    for j in range(4):
        o.append(T(x0 + j * cw + cw / 2, y0 - 14, f'on ⟨M{j + 1}⟩', 14, fill=MUT, bold=True))
    for i, (m, vals) in enumerate(rows):
        y = y0 + i * ch
        o.append(T(x0 - 16, y + 26, m, 15, 'end', INK, True))
        for j, v in enumerate(vals.split()):
            d = i == j
            o.append(R(x0 + j * cw, y, cw - 4, ch - 4, ACS if d else PANEL, AC if d else L2, 4, 2.2 if d else 1.2))
            o.append(T(x0 + j * cw + (cw - 4) / 2, y + 24, v, 15, fill=AC if d else INK, bold=d))
    yD = y0 + 4 * ch + 26
    o.append(T(x0 - 16, yD + 26, 'D', 15, 'end', LV, True))
    for j, v in enumerate('no yes yes no'.split()):
        o.append(R(x0 + j * cw, yD, cw - 4, ch - 4, LVS, LV, 4, 2))
        o.append(T(x0 + j * cw + (cw - 4) / 2, yD + 24, v, 15, fill=LV, bold=True))
        o.append(L(x0 + j * cw + (cw - 4) / 2, y0 + 4 * ch - 1, x0 + j * cw + (cw - 4) / 2, yD - 3, LV, 1.8, arrow='l'))
    o.append(T(x0 + 4 * cw + 6, yD + 14, 'flip of the', 13, 'start', LV, True))
    o.append(T(x0 + 4 * cw + 6, yD + 31, 'diagonal', 13, 'start', LV, True))
    o.append(T(20, yD + 72, 'D differs from every Mi on ⟨Mi⟩, so D is no row of the table; asking H about D on ⟨D⟩ gives a contradiction.', 13, 'start', INK))
    return yD + 86, ''.join(o)
FIG[3] = (f3, 'Row Mi lists whether Mi halts on each code; the marked diagonal is each machine on its own code: yes, no, no, yes. D does the opposite on the diagonal (no, yes, yes, no), so D differs from every row and cannot be in the table, which is the contradiction behind HALT.',
          'A four by four table of yes and no for M1 to M4 on the codes ⟨M1⟩ to ⟨M4⟩ with the diagonal yes, no, no, yes marked, and below it a row D holding no, yes, yes, no, each cell the flip of the diagonal cell above.')


# ---- 6.4 Rice's theorem on FIN ----
def f4():
    o = []
    o.append(R(150, 20, 420, 56, PANEL, AC, 10, 2))
    o.append(T(360, 44, 'M′ on input x: simulate M on w;', 14, fill=INK, bold=True))
    o.append(T(360, 64, 'if that halts, accept x', 14, fill=INK, bold=True))
    cases = [(185, 'M halts on w', 'M′ accepts every x', 'L(M′) = Σ*, infinite', 'R says no', NX, NXS),
             (535, 'M loops on w', 'M′ accepts nothing', 'L(M′) = ∅, finite', 'R says yes', LV, LVS)]
    for x, a, b, c, d, col, f in cases:
        o.append(L(360 + (x - 360) * 0.3, 78, x, 110, col, 2, arrow='x' if col == NX else 'l'))
        o.append(T(x, 128, a, 14, fill=col, bold=True))
        o.append(R(x - 120, 140, 240, 40, PANEL, col, 8, 2)); o.append(T(x, 166, b, 14, fill=INK, bold=True))
        o.append(L(x, 182, x, 202, col, 2, arrow='x' if col == NX else 'l'))
        o.append(R(x - 120, 206, 240, 40, f, col, 8, 2)); o.append(T(x, 232, c, 14, fill=col, bold=True))
        o.append(L(x, 248, x, 268, col, 2, arrow='x' if col == NX else 'l'))
        o.append(chip(x, 286, d, col, f))
    o.append(T(360, 336, 'R’s answer, flipped, says whether M halts on w. No machine decides that, so no R decides FIN.', 13, fill=INK))
    return 352, ''.join(o)
FIG[4] = (f4, 'Assume R decides FIN. M′ accepts everything if M halts on w and nothing if it loops, so R’s answer on ⟨M′⟩, flipped, decides halting, which is impossible. Finiteness is a nontrivial property of L(M), which is all Rice’s theorem needs.',
          'A machine M′ that simulates M on w and then accepts; two branches: if M halts, L(M′) = Σ*, infinite, and R says no; if M loops, L(M′) = ∅, finite, and R says yes.')


# ---- 6.5 the dominoes and the match 1, 2, 3 ----
def f5():
    o = []
    doms = [('a', 'aab'), ('ab', 'b'), ('bab', 'ab')]
    cols = [(AC, ACS), (NX, NXS), (LV, LVS)]
    for i, ((t, b), (c, f)) in enumerate(zip(doms, cols)):
        x = 90 + i * 200
        o.append(R(x - 60, 20, 120, 84, f, c, 8, 2))
        o.append(L(x - 60, 62, x + 60, 62, c, 1.6))
        o.append(TM(x, 49, t, 17, 'middle', INK, True)); o.append(TM(x, 91, b, 17, 'middle', INK, True))
        o.append(T(x, 126, f'domino {i + 1}', 13, fill=c, bold=True))
    o.append(L(10, 146, 710, 146, LN, 1))
    o.append(T(20, 176, 'Use 1, 2, 3 in that order and join the tops and the bottoms:', 14, 'start', INK, True))
    cw, x0 = 44, 150
    top = [(s, 0) for s in 'a'] + [(s, 1) for s in 'ab'] + [(s, 2) for s in 'bab']
    bot = [(s, 0) for s in 'aab'] + [(s, 1) for s in 'b'] + [(s, 2) for s in 'ab']
    for row, (lab, seq) in enumerate((('top', top), ('bottom', bot))):
        y = 196 + row * 50
        o.append(T(x0 - 14, y + 26, lab, 14, 'end', MUT, True))
        for i, (s, d) in enumerate(seq):
            c, f = cols[d]
            o.append(R(x0 + i * cw, y, cw - 4, 38, f, c, 4, 1.8))
            o.append(TM(x0 + i * cw + 20, y + 26, s, 17, 'middle', INK, True))
        o.append(T(x0 + 6 * cw + 16, y + 26, '= aabbab', 15, 'start', NX, True))
    o.append(T(20, 324, 'Both read aabbab (6 symbols), so 1, 2, 3 is a match. It starts with domino 1, so it also solves MPCP.', 13, 'start', NX, True))
    return 338, ''.join(o)
FIG[5] = (f5, 'The three dominoes of the worked example, and the sequence 1, 2, 3: the tops a·ab·bab and the bottoms aab·b·ab both spell aabbab, so it is a match. The colours show which domino each symbol comes from.',
          'Three dominoes (a over aab, ab over b, bab over ab); below, the joined top a ab bab and joined bottom aab b ab drawn as coloured cells, both reading aabbab.')


# ---- 6.6 f(n) = n + 1 on aaa ----
def f6():
    o = []
    rows = [('start: n = 3 in unary', ['a', 'a', 'a', '□', '□'], 0, ()),
            ('3 moves right over the a’s', ['a', 'a', 'a', '□', '□'], 3, ()),
            ('write a in the blank, halt', ['a', 'a', 'a', 'a', '□'], 3, (3,))]
    for j, (lab, cells, hd, chg) in enumerate(rows):
        y = 40 + j * 78
        last = j == 2
        tape(o, 60, y, cells, hd, 50, 38, NX if last else AC, chg)
        o.append(T(340, y + 25, lab, 14, 'start', NX if last else INK, last))
    for i in range(4):
        o.append(T(60 + i * 50 + 23, 28 + 2 * 78 + 70 + 22, f'cell {i + 1}', 13, fill=MUT))
    o.append(L(10, 296, 710, 296, LN, 1))
    o.append(T(20, 322, 'aaa becomes aaaa: f(3) = 4. The same moves halt for every n, so f is total computable.', 14, 'start', NX, True))
    o.append(T(20, 346, 'Compare g(M, w): simulating M may never stop, so g is only partial computable.', 13, 'start', INK))
    return 360, ''.join(o)
FIG[6] = (f6, 'The machine for f(n) = n + 1 walks right over the three a’s, writes one more a in the first blank cell and halts, so aaa becomes aaaa and 3 maps to 4. It halts on every input, which is what makes f total.',
          'Three tape rows: aaa with the head on cell 1; the head on the blank cell 4 after three moves; aaaa after the head writes a there and halts.')


# ---- 6.7 time on w = 000111 ----
def f7():
    o = []
    u, x0 = 15, 130
    o.append(T(20, 52, 'M₁', 16, 'start', AC, True)); o.append(T(56, 52, 'scan, check', 13, 'start', MUT))
    o.append(R(x0, 34, 7 * u, 28, ACS, AC, 4, 2))
    o.append(T(x0 + 7 * u + 10, 53, '7 steps = n + 1  →  TIME(n)', 14, 'start', AC, True))
    o.append(T(20, 126, 'M₂', 16, 'start', LV, True)); o.append(T(56, 126, 'cross off', 13, 'start', MUT))
    for r in range(3):
        o.append(R(x0 + r * 12 * u, 108, 12 * u - 3, 28, LVS, LV, 4, 2))
        o.append(T(x0 + r * 12 * u + 6 * u, 127, f'round {r + 1}: ≤ 12', 13, fill=LV, bold=True))
    o.append(T(x0 + 36 * u, 160, '36 steps = n²  →  TIME(n²)', 14, 'end', LV, True))
    o.append(xaxis(x0, x0 + 36 * u, 190, [0, 6, 12, 18, 24, 30, 36], lambda v: x0 + v * u, 'steps on w = 000111 (n = 6)'))
    o.append(L(10, 256, 710, 256, LN, 1))
    o.append(T(20, 282, 'Space: both machines use the 6 input cells. Each round of M₂ crosses one 0 and one 1 and scans at most', 13, 'start', INK))
    o.append(T(20, 302, '2n = 12 cells; 3 rounds give 3 × 12 = 36 = n² steps.', 13, 'start', INK))
    return 316, ''.join(o)
FIG[7] = (f7, 'On w = 000111 (n = 6), M₁ finishes in 7 steps while M₂ needs 3 rounds of at most 12 steps, 36 in all; both use the same 6 cells. That puts M₁ in TIME(n) and M₂ in TIME(n²).',
          'Two bars on one step axis from 0 to 36: M₁ is 7 steps long; M₂ is three rounds of 12 steps, ending at 36.')


# ---- 6.8 checking a Hamiltonian-cycle certificate ----
def f8():
    o = []
    cx, cy, r = 170, 170, 115
    P_ = {k: (cx + r * math.sin(2 * math.pi * (k - 1) / 5), cy - r * math.cos(2 * math.pi * (k - 1) / 5)) for k in range(1, 6)}
    for a, b in ((1, 3), (2, 4)):
        o.append(L(*P_[a], *P_[b], L2, 1.8, '6 4'))
    for a, b in ((1, 2), (2, 3), (3, 4), (4, 5), (5, 1)):
        o.append(edge(P_[a], P_[b], r=20, c=NX if (a, b) != (5, 1) else AC, w=2.4, arrow='x' if (a, b) != (5, 1) else 'n'))
    for k, (x, y) in P_.items():
        o.append(state(x, y, str(k), r=20, fill=PANEL, stroke=INK, size=15))
    o.append(T(cx, 318, 'dashed: edges 13 and 24, not used', 13, fill=MUT))
    x = 360
    o.append(T(x, 40, 'Certificate y = (1, 2, 3, 4, 5)', 15, 'start', INK, True))
    checks = [('5 vertices distinct?', '10 comparisons', NX), ('edges 12, 23, 34, 45?', '4 lookups', NX),
              ('closing edge 51?', '1 lookup', AC)]
    for i, (q, c, col) in enumerate(checks):
        y = 80 + i * 52
        o.append(R(x, y, 340, 40, PANEL, col, 8, 1.8))
        o.append(T(x + 12, y + 25, '✓  ' + q, 14, 'start', col, True))
        o.append(T(x + 328, y + 25, c, 13, 'end', MUT, True))
    o.append(T(x, 260, '5 lookups + 10 comparisons ≤ n² = 25', 14, 'start', INK, True))
    o.append(T(x, 284, 'polynomial time, so the verifier puts', 13, 'start', NX, True))
    o.append(T(x, 302, 'HAMILTONIAN CYCLE in NP', 13, 'start', NX, True))
    return 334, ''.join(o)
FIG[8] = (f8, 'The verifier is handed the cycle 1, 2, 3, 4, 5 and only checks it: 10 comparisons show the vertices are distinct and 5 lookups find the edges 12, 23, 34, 45 and 51. That is O(n²) work, which puts HAMILTONIAN CYCLE in NP.',
          'A five-vertex graph with the certificate cycle 1 to 2 to 3 to 4 to 5 and back to 1 drawn as arrows and edges 13 and 24 dashed, beside three ticked checks: distinct vertices, the four consecutive edges and the closing edge.')


spec = make_spec(FIG)


def text_fixes(k):
    """sentences in the chapter text that describe the figure, rewritten to match the drawing above"""
    return {
        8: [('The figure places P inside NP inside PSPACE.',
             'The figure shows a verifier at work on the worked example’s graph: it checks a cycle it is given and never searches for one. What is known so far is P ⊆ NP ⊆ PSPACE.')],
    }.get(k, [])
