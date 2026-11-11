"""Claude's hand-drawn figures for c-ml-u6 (Machine Learning, unit 6: reinforcement and analytical learning), one per
chapter, each drawn from that chapter's worked example with its own numbers. The book has no writer branch, so it is
applied with apply_html.py. Only the captions described the old drawings; no chapter sentence needs rewriting."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def circ(x, y, s, r=24, f=PANEL, c=AC, size=14):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{f};stroke:{c};stroke-width:2"/>' + T(x, y + size * 0.35, s, size, bold=True)


# ---- 6.1 discounted return of two routes ----
def f1():
    o = [T(40, 24, 'Which route has the greater return? γ = 0.9', 15, 'start', bold=True)]
    y = 90
    o.append(T(40, y + 5, 'route A', 14, 'start', AC, True))
    xs = [130, 270, 410, 550]
    o.append(circ(xs[0], y, 'start', 26, PANEL, L2, 13))
    for i, (r, d, v) in enumerate([(-2, '1', '−2'), (-2, '0.9', '−1.8'), (10, '0.81', '8.1')]):
        a, b = xs[i], xs[i + 1]
        o.append(L(a + 28, y, b - 30, y, AC, 2.2, arrow='n'))
        o.append(Tb((a + b) / 2, y - 12, f'r = {neg(r) if r < 0 else "+" + str(r)}', 13, bold=True))
        o.append(T((a + b) / 2, y + 26, f'× {d} = {v}', 13, fill=MUT))
        last = i == 2
        o.append(circ(b, y, 'end' if last else '', 22 if not last else 26, ACS if last else PANEL, AC, 13))
    o.append(T(600, y + 5, '', 14))
    o.append(T(xs[3] + 40, y + 5, 'G = 4.3', 15, 'start', AC, True))
    y2 = 190
    o.append(T(40, y2 + 5, 'route B', 14, 'start', LV, True))
    o.append(circ(xs[0], y2, 'start', 26, PANEL, L2, 13))
    o.append(L(xs[0] + 28, y2, xs[1] - 30, y2, LV, 2.2, arrow='l'))
    o.append(Tb((xs[0] + xs[1]) / 2, y2 - 12, 'r = +4', 13, bold=True)); o.append(T((xs[0] + xs[1]) / 2, y2 + 26, '× 1 = 4', 13, fill=MUT))
    o.append(circ(xs[1], y2, 'end', 26, LVS, LV, 13))
    o.append(T(xs[1] + 40, y2 + 5, 'G = 4', 15, 'start', LV, True))
    o.append(T(40, 262, 'A wins by 0.3 despite its worse first reward. With γ = 0.5, A gives −2 − 1 + 2.5 = −0.5 and B wins.', 14, 'start'))
    o.append(T(40, 292, 'TD update after one step of A: target = −2 + 0.9 × V(next) 5 = 2.5; error = 2.5 − 3 = −0.5;', 13, 'start', MUT))
    o.append(T(40, 312, 'V(start) = 3 + 0.2 × (−0.5) = 2.9.', 13, 'start', MUT))
    return 328, ''.join(o)
FIG[1] = (f1, 'Each reward is weighted by γ raised to how many steps away it is. Route A’s late +10 counts as 8.1, so its return 4.3 beats route B’s 4; with γ = 0.5 the same +10 counts only 2.5 and B wins.',
          'Two routes from a start state. Route A has three steps with rewards −2, −2, +10, discounted to −2, −1.8, 8.1, return 4.3. Route B has one step with reward +4, return 4. A note gives the γ = 0.5 case and a TD update to 2.9.')


# ---- 6.2 three Q-learning updates ----
def f2():
    o = [T(40, 24, 'Q-learning on S → T → end, α = 0.5, γ = 0.9', 15, 'start', bold=True)]
    o.append(circ(110, 84, 'S', 26)); o.append(circ(330, 84, 'T', 26)); o.append(circ(550, 84, 'end', 26, ACS, AC, 13))
    o.append(L(138, 84, 300, 84, AC, 2.2, arrow='n')); o.append(Tb(220, 72, 'go, r = −1', 13, bold=True))
    o.append(L(358, 84, 520, 84, AC, 2.2, arrow='n')); o.append(Tb(440, 72, 'finish, r = +10', 13, bold=True))
    o.append(L(96, 108, 96, 136, L2, 1.4)); o.append(T(96, 152, 'wait stays 0', 13, fill=MUT))
    heads = ['update', 'entry', 'target', 'new value']
    cx = [40, 150, 290, 520]
    y = 186
    for x, h in zip(cx, heads): o.append(T(x, y, h, 13, 'start', MUT, True))
    rows = [('1', 'Q(S, go)', '−1 + 0.9 × max Q(T) = −1 + 0 = −1', '0 + 0.5(−1 − 0) = −0.5'),
            ('2', 'Q(T, finish)', '10 (terminal: no max)', '0 + 0.5(10 − 0) = 5'),
            ('3', 'Q(S, go)', '−1 + 0.9 × 5 = 3.5', '−0.5 + 0.5(3.5 + 0.5) = 1.5')]
    for i, r in enumerate(rows):
        yy = y + 14 + i * 36
        o.append(R(30, yy, 660, 32, PANEL if i % 2 == 0 else 'none', 'none', 0, 0))
        for j, (x, v) in enumerate(zip(cx, r)):
            o.append(T(x + (10 if j == 0 else 0), yy + 21, v, 13, 'start', AC if j == 3 else INK, j == 3))
    o.append(T(40, y + 150, 'Update 3 sees the 5 learned in update 2: the reward of +10 is flowing back to S.', 14, 'start'))
    o.append(T(40, y + 172, 'Greedy action at S is go (1.5 > 0); the true value of go is −1 + 0.9 × 10 = 8, not reached yet.', 13, 'start', MUT))
    return y + 188, ''.join(o)
FIG[2] = (f2, 'Each update moves one entry halfway to its target. Q(S, go) first drops to −0.5; after Q(T, finish) learns 5, the next target for go is 3.5 and the entry rises to 1.5, on its way to the true value 8.',
          'A chain S to T to end: action go with reward −1, then finish with reward +10. A table of three updates: Q(S,go) to −0.5, Q(T,finish) to 5, then Q(S,go) to 1.5 using target 3.5.')


# ---- 6.3 two covering rules ----
def f3():
    o = [T(40, 24, 'Sequential covering on 3 positives and 2 negatives', 15, 'start', bold=True)]
    gx, gy, cw, ch = 140, 70, 150, 100
    o.append(T(gx + cw / 2, gy - 10, 'A = yes', 13, fill=MUT, bold=True)); o.append(T(gx + 1.5 * cw, gy - 10, 'A = no', 13, fill=MUT, bold=True))
    o.append(T(gx - 10, gy + ch / 2 + 5, 'B = yes', 13, 'end', MUT, True)); o.append(T(gx - 10, gy + 1.5 * ch + 5, 'B = no', 13, 'end', MUT, True))
    o.append(R(gx - 6, gy - 2, cw + 2, 2 * ch + 4, ACS, AC, 10, 2.2))
    o.append(R(gx - 2, gy - 6, 2 * cw + 8, ch + 2, 'none', LV, 10, 2.2, dash='7 4'))
    for i in range(2):
        for j in range(2):
            o.append(R(gx + j * cw + 6, gy + i * ch + 6, cw - 12, ch - 12, 'none', L2, 6, 1))
    def pt(x, y, lab, pos=True):
        c = AC if pos else NX
        s = (f'<circle cx="{x}" cy="{y}" r="16" style="fill:{c}"/>' + T(x, y + 5, lab, 13, bold=True, fill='var(--fig)')) if pos else \
            (f'<circle cx="{x}" cy="{y}" r="15" style="fill:var(--fig);stroke:{c};stroke-width:2.5"/>' + T(x, y + 5, lab, 13, bold=True, fill=c))
        return s
    o.append(pt(gx + cw / 2, gy + ch / 2, 'P2')); o.append(pt(gx + cw / 2, gy + 1.5 * ch, 'P1'))
    o.append(pt(gx + 1.5 * cw, gy + ch / 2, 'P3'))
    o.append(pt(gx + 1.5 * cw - 26, gy + 1.5 * ch, 'N1', False)); o.append(pt(gx + 1.5 * cw + 26, gy + 1.5 * ch, 'N2', False))
    X = 480
    o.append(T(X, 70, 'empty rule: 3 of 5 positive', 13, 'start')); o.append(T(X, 88, 'precision 0.6', 13, 'start', MUT))
    o.append(T(X, 120, 'rule 1: IF A = yes', 14, 'start', AC, True)); o.append(T(X, 140, 'covers P1, P2; precision 2/2', 13, 'start'))
    o.append(T(X, 158, 'remove P1, P2 from the pool', 13, 'start', MUT))
    o.append(T(X, 190, 'rule 2: IF B = yes', 14, 'start', LV, True)); o.append(T(X, 210, 'covers P3 (and P2 again);', 13, 'start'))
    o.append(T(X, 228, 'no negative', 13, 'start'))
    o.append(T(X, 262, 'positive if A = yes OR B = yes', 13, 'start', bold=True))
    o.append(T(X, 282, 'TP 3, FP 0, FN 0, TN 2', 13, 'start'))
    o.append(T(40, 300, 'P2 sits in both rules: 2 + 2 = 4 coverings, but only 3 distinct positives.', 13, 'start', MUT))
    return 316, ''.join(o)
FIG[3] = (f3, 'Rule 1, A = yes (solid box), covers P1 and P2 with no negative. With those removed, rule 2, B = yes (dashed box), covers the last positive P3. The two rules overlap on P2, and both negatives stay uncovered.',
          'A two by two grid of A yes or no against B yes or no. P2 is at A yes B yes, P1 at A yes B no, P3 at A no B yes, and N1 and N2 at A no B no. A solid box marks rule A = yes over the A yes column; a dashed box marks rule B = yes over the B yes row.')


# ---- 6.4 a shared variable joins two parent facts ----
def f4():
    o = [T(40, 24, 'grandparent(X, Z) ← parent(X, Y) AND parent(Y, Z)', 15, 'start', bold=True)]
    P = {'asha': (110, 90), 'bala': (290, 90), 'chitra': (470, 90), 'dev': (290, 200), 'eesha': (470, 200)}
    for n, (x, y) in P.items():
        o.append(boxt(x - 55, y - 20, 110, 40, [n], ACS if n in ('asha', 'bala', 'chitra') else PANEL, AC if n in ('asha', 'bala', 'chitra') else L2, 14))
    o.append(L(167, 90, 233, 90, AC, 2.2, arrow='n')); o.append(L(347, 90, 413, 90, AC, 2.2, arrow='n'))
    o.append(L(347, 200, 413, 200, L2, 2, arrow='m'))
    o.append(T(200, 78, 'parent', 13, fill=MUT)); o.append(T(380, 78, 'parent', 13, fill=MUT)); o.append(T(380, 222, 'parent', 13, fill=MUT))
    o.append(T(110, 134, 'X', 15, bold=True, fill=AC)); o.append(T(290, 134, 'Y = bala', 15, bold=True, fill=AC)); o.append(T(470, 134, 'Z', 15, bold=True, fill=AC))
    o.append(L(120, 112, 410, 196, LV, 1.8, dash='5 4'))
    o.append(T(40, 196, 'no chain: Y = bala', 13, 'start', LV, True)); o.append(T(40, 214, 'and Y = dev at once', 13, 'start', LV, True))
    o.append(T(560, 95, '✓ grandparent', 14, 'start', AC, True)); o.append(T(560, 113, '(asha, chitra)', 13, 'start', AC))
    o.append(T(560, 205, '✗ grandparent', 14, 'start', LV, True)); o.append(T(560, 223, '(asha, eesha)', 13, 'start', LV))
    o.append(T(40, 262, 'One substitution must satisfy both literals. Y = bala works for asha → chitra; for eesha the only parent fact', 13, 'start'))
    o.append(T(40, 282, 'is parent(dev, eesha), and parent(bala, eesha) is absent, so the tuple is not covered (closed world).', 13, 'start'))
    o.append(T(40, 312, 'FOIL-gain example: 3 × [log₂(3/3) − log₂(4/8)] = 3 × [0 − (−1)] = 3', 14, 'start', NX, True))
    return 328, ''.join(o)
FIG[4] = (f4, 'With Y = bala the two parent facts chain asha to chitra, so grandparent(asha, chitra) is covered. No single Y links asha to eesha: parent(dev, eesha) would need Y = dev, which breaks the first literal.',
          'Family facts as arrows: asha to bala to chitra, and separately dev to eesha. X, Y = bala and Z label the first chain, marked as a covered grandparent pair. A dashed line from asha to eesha is marked not covered, because Y would have to be both bala and dev.')


# ---- 6.5 the proof becomes a rule ----
def f5():
    o = [T(40, 24, 'Explanation-based learning: keep what the proof used', 15, 'start', bold=True)]
    o.append(boxt(210, 44, 260, 40, ['eligible(p, r)'], ACS, AC, 15))
    o.append(boxt(60, 132, 260, 50, ['mass(p) ≤ capacity(r)', '3 kg ≤ 5 kg ✓'], PANEL, AC, 14))
    o.append(boxt(360, 132, 200, 50, ['route_clear(r)', 'true ✓'], PANEL, AC, 14))
    o.append(L(190, 130, 290, 86, AC, 2, arrow='n')); o.append(L(460, 130, 390, 86, AC, 2, arrow='n'))
    o.append(boxt(590, 132, 110, 50, ['colour(p)', 'blue'], 'none', L2, 13, dash='5 4', fills=[MUT, MUT]))
    o.append(T(645, 200, 'not used', 13, fill=MUT)); o.append(T(645, 216, 'by the proof', 13, fill=MUT))
    o.append(L(340, 196, 340, 230, NX, 2.2, arrow='x')); o.append(T(352, 218, 'replace p, r by variables; keep ≤', 13, 'start', NX))
    o.append(boxt(60, 236, 600, 46, ['eligible(P, R) ← mass(P) ≤ capacity(R) AND route_clear(R)'], NXS, NX, 15))
    o.append(T(60, 312, 'new 4 kg parcel, capacity 5 kg, clear route: rule fires.', 13, 'start', AC))
    o.append(T(60, 332, '6 kg parcel: 6 ≤ 5 is false, so this sufficient condition is not met.', 13, 'start', LV))
    return 348, ''.join(o)
FIG[5] = (f5, 'The proof that parcel p is eligible used only the mass check (3 kg ≤ 5 kg) and the clear route. Turning p and r into variables gives a reusable rule; the parcel’s colour never entered the proof, so it is left out.',
          'A proof tree: eligible(p, r) supported by mass(p) ≤ capacity(r), 3 kg ≤ 5 kg, and route_clear(r), true. A dashed box colour(p) blue is marked not used. An arrow leads to the general rule eligible(P, R) ← mass(P) ≤ capacity(R) AND route_clear(R).')


spec = make_spec(FIG)


def text_fixes(k):
    return []
