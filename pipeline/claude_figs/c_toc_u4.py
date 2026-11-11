"""Claude's hand-drawn figures for c-toc-u4 (Theory of Computation, unit 4: pushdown automata, acceptance by final state
and by empty stack, DPDAs and DCFLs, PDA-CFG equivalence, top-down and bottom-up parsing), one per chapter, from each
chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def node(x, y, s, c=AC, f=PANEL, r=20, size=15):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{f};stroke:{c};stroke-width:2"/>' + T(x, y + size * 0.36, s, size, fill=c, bold=True)


def leaf(x, y, s, c=NX, size=15):
    w = max(34, tw(s, size) + 14)
    return R(x - w / 2, y - 15, w, 30, NXS, c, 6, 1.6) + T(x, y + 5, s, size, fill=c, bold=True)


def stack_v(o, x, ybot, syms, w=60, h=30, top_hi=True):
    """a vertical stack, bottom symbol first, drawn upward from ybot (the bottom edge)"""
    o.append(L(x - w / 2 - 6, ybot, x + w / 2 + 6, ybot, L2, 2))
    for i, s in enumerate(syms):
        y = ybot - (i + 1) * h
        top = top_hi and i == len(syms) - 1
        o.append(R(x - w / 2, y, w, h - 2, ACS if top else PANEL, AC if top else L2, 4, 2 if top else 1.4))
        o.append(T(x, y + h / 2 + 5, s, 15, fill=AC if top else INK, bold=True))
    if not syms:
        o.append(T(x, ybot - 12, 'empty', 13, fill=NX, bold=True))


def chip(x, y, s, c=AC, f=ACS, size=14):
    w = max(40, tw(s, size) + 18)
    return R(x - w / 2, y - 15, w, 30, f, c, 15, 2) + T(x, y + 5, s, size, fill=c, bold=True)


# ---- 4.1 the stack while the PDA reads aabb ----
def f1():
    o = []
    cols = [('q₀', 'aabb', ['Z₀'], 'start'), ('q₀', 'abb', ['Z₀', 'A'], 'read a, push A'), ('q₀', 'bb', ['Z₀', 'A', 'A'], 'read a, push A'),
            ('q₁', 'b', ['Z₀', 'A'], 'read b, pop A'), ('q₁', 'ε', ['Z₀'], 'read b, pop A'), ('q₂', 'ε', ['Z₀'], 'ε-move to q₂')]
    for i, (q, inp, st, mv) in enumerate(cols):
        x = 62 + i * 119
        fin = q == 'q₂'
        o.append(chip(x, 36, q, NX if fin else AC, NXS if fin else ACS))
        o.append(T(x, 76, 'input left', 13, fill=MUT))
        o.append(TM(x, 98, inp, 16, 'middle', INK, True))
        stack_v(o, x, 230, st)
        o.append(T(x, 254, mv if i else 'start', 13, fill=LV if i else MUT, bold=bool(i)))
        if i: o.append(L(x - 119 + 34, 36, x - 34, 36, L2, 1.8, arrow='m'))
    o.append(T(10, 158, 'stack', 13, 'start', MUT, True))
    o.append(T(10, 174, '(top up)', 13, 'start', MUT))
    o.append(L(10, 280, 710, 280, LN, 1))
    o.append(T(20, 308, '5 moves: 2 pushes, 2 pops, 1 ε-move. The run ends in q₂, a final state, with only Z₀ left: aabb is accepted.', 13, 'start', NX, True))
    o.append(T(20, 330, 'The control only ever looks at the top cell (highlighted) and the next input symbol.', 13, 'start', INK))
    return 344, ''.join(o)
FIG[1] = (f1, 'Each column is one instantaneous description of the PDA on aabb: the state, the input still to read and the stack. Each a pushes an A, each b pops one, and a final ε-move enters the accepting state q₂ with only Z₀ left.',
          'Six columns from (q₀, aabb, Z₀) to (q₂, ε, Z₀): the stack grows to A A Z₀ while the a’s are read and shrinks back to Z₀ while the b’s are read.')


# ---- 4.2 final state to empty stack ----
def f2():
    o = []
    # state chain
    o.append(state(70, 80, 'q₀′', start=True, r=26, size=14))
    o.append(R(190, 40, 300, 80, PANEL, L2, 14, 1.6, '6 4'))
    o.append(T(340, 34, 'the old PDA of 4.1, moves unchanged', 13, fill=MUT, bold=True))
    for x, n in ((240, 'q₀'), (340, 'q₁'), (440, 'q₂')):
        o.append(state(x, 80, n, accept=n == 'q₂', r=24))
    o.append(edge((240, 80), (340, 80))); o.append(edge((340, 80), (440, 80)))
    o.append(state(630, 80, 'qe', r=26, fill=LVS, stroke=LV))
    o.append(edge((70, 80), (240, 80), r=26, c=AC))
    o.append(Tb(150, 66, 'ε, X₀ / Z₀X₀', 13, fill=AC, bold=True))
    o.append(edge((440, 80), (630, 80), r=26, c=LV, arrow='l'))
    o.append(Tb(540, 66, 'ε, any / ε', 13, fill=LV, bold=True))
    o.append(f'<path d="M620,56 C595,8 665,8 640,56" style="fill:none;stroke:var(--live);stroke-width:2" marker-end="url(#ar-UID-l)"/>')
    o.append(T(630, 18, 'ε, any / ε: pop', 13, fill=LV, bold=True))
    o.append(T(630, 132, 'eraser, not final', 13, fill=LV))
    o.append(L(10, 156, 710, 156, LN, 1))
    # stacks along the run on aabb
    cols = [('q₀′', 'aabb', ['X₀'], 'start'), ('q₀', 'aabb', ['X₀', 'Z₀'], 'push Z₀'), ('q₂', 'ε', ['X₀', 'Z₀'], 'old run, 5 moves'),
            ('qe', 'ε', ['X₀'], 'pop Z₀'), ('qe', 'ε', [], 'pop X₀')]
    for i, (q, inp, st, mv) in enumerate(cols):
        x = 80 + i * 140
        c, f = (LV, LVS) if q == 'qe' else (AC, ACS)
        o.append(chip(x, 186, q, c, f))
        o.append(TM(x, 220, inp, 15, 'middle', MUT, True))
        stack_v(o, x, 312, st)
        o.append(T(x, 336, mv, 13, fill=c, bold=True))
        if i: o.append(L(x - 140 + 34, 186, x - 34, 186, L2, 1.8, arrow='m'))
    o.append(T(20, 372, 'The new bottom X₀ stops the old machine from emptying the stack by accident; the run ends at (qe, ε, ε).', 13, 'start', INK))
    return 386, ''.join(o)
FIG[2] = (f2, 'The new start q₀′ puts Z₀ on top of a fresh bottom X₀ and hands over to the old machine; when the old machine reaches its final state q₂, the eraser qe pops everything. On aabb the stack goes Z₀X₀, then X₀, then empty, so aabb is accepted by empty stack.',
          'Top: q₀′ leads into the old PDA q₀, q₁, q₂, and q₂ leads to an eraser state qe that loops popping any symbol. Bottom: the stack on aabb, X₀, Z₀X₀, Z₀X₀ at q₂, X₀ at qe, then empty.')


# ---- 4.3 regular ⊂ DCFL ⊂ CFL ----
def f3():
    o = []
    o.append(R(10, 10, 700, 300, PANEL, L2, 18, 2))
    o.append(T(30, 38, 'Context-free languages (any PDA)', 15, 'start', INK, True))
    o.append(R(40, 60, 420, 230, ACS, AC, 18, 2))
    o.append(T(60, 88, 'Deterministic CFLs (a DPDA)', 15, 'start', AC, True))
    o.append(R(70, 110, 220, 160, NXS, NX, 16, 2))
    o.append(T(90, 138, 'Regular', 15, 'start', NX, True))
    o.append(TM(180, 200, 'a*b*', 17, 'middle', NX, True))
    o.append(T(375, 170, 'aⁿbⁿ', 18, 'middle', AC, True))
    o.append(T(375, 196, 'L₁: push a, pop b', 13, fill=AC, bold=True))
    o.append(T(375, 214, '2n + 1 moves', 13, fill=AC))
    o.append(T(585, 150, 'aⁿbⁿ ∪ aⁿb²ⁿ', 17, 'middle', LV, True))
    o.append(T(585, 176, 'L₁ ∪ L₂', 13, fill=LV, bold=True))
    o.append(T(585, 210, 'at the first b:', 13, fill=INK))
    o.append(T(585, 228, 'pop 1 A per b,', 13, fill=INK))
    o.append(T(585, 246, 'or 1 A per 2 b’s?', 13, fill=INK))
    o.append(T(585, 272, 'a DPDA cannot guess', 13, fill=LV, bold=True))
    o.append(T(20, 340, 'Both inclusions are strict: aⁿbⁿ is deterministic but not regular, and the union is context-free but not deterministic.', 13, 'start', INK))
    return 354, ''.join(o)
FIG[3] = (f3, 'The deterministic CFLs sit strictly between the regular and the context-free languages. The DPDA of the worked example accepts aⁿbⁿ, but adding aⁿb²ⁿ forces a guess at the first b, so the union is context-free and not deterministic.',
          'Three nested boxes: regular with a*b*, deterministic context-free with aⁿbⁿ, and context-free with the union of aⁿbⁿ and aⁿb²ⁿ, which needs a guess at the first b.')


# ---- 4.4 the one-state PDA from S → aSb | ε on input ab ----
def f4():
    o = []
    rows = [('start move', 'ab', ['Z₀', 'S']), ('expand S → aSb', 'ab', ['Z₀', 'b', 'S', 'a']), ('match a', 'b', ['Z₀', 'b', 'S']),
            ('expand S → ε', 'b', ['Z₀', 'b']), ('match b', 'ε', ['Z₀']), ('pop Z₀', 'ε', [])]
    o.append(T(20, 28, 'move', 13, 'start', MUT, True)); o.append(T(220, 28, 'input left', 13, 'middle', MUT, True))
    o.append(T(300, 28, 'stack, bottom → top', 13, 'start', MUT, True))
    o.append(TM(20, 58, '(q, ab, Z₀)', 14, 'start', MUT, True))
    for j, (mv, inp, st) in enumerate(rows):
        y = 74 + j * 46
        exp = mv.startswith('expand')
        o.append(T(20, y + 22, mv, 14, 'start', AC if exp else (NX if mv.startswith('match') else INK), True))
        o.append(TM(220, y + 22, inp, 16, 'middle', INK, True))
        for i, s in enumerate(st):
            top = i == len(st) - 1
            x = 300 + i * 52
            o.append(R(x, y + 2, 48, 32, ACS if top else PANEL, AC if top else L2, 4, 2 if top else 1.4))
            o.append(T(x + 24, y + 24, s, 15, fill=AC if top else INK, bold=True))
        if not st: o.append(T(300, y + 22, 'empty: ab is accepted', 14, 'start', NX, True))
        else: o.append(T(300 + len(st) * 52 + 4, y + 22, '← top', 13, 'start', AC))
    o.append(L(10, 360, 710, 360, LN, 1))
    o.append(T(20, 386, 'Expanding a variable swaps it on the stack for a rule’s right side (a on top); matching pops a terminal', 13, 'start', INK))
    o.append(T(20, 406, 'that equals the next input symbol. Six moves empty the stack exactly when the input runs out.', 13, 'start', INK))
    return 420, ''.join(o)
FIG[4] = (f4, 'The one-state PDA built from S → aSb | ε, run on ab, with each stack written bottom to top. Expanding S pushes a S b with a on top, the a and b are matched against the input, and after six moves both the input and the stack are empty.',
          'Six rows, one per move: start Z₀ S, expand to Z₀ b S a, match a to Z₀ b S, expand S → ε to Z₀ b, match b to Z₀, pop Z₀ to empty, with the input left beside each row.')


# ---- 4.5 top-down vs bottom-up on id + id * id ----
def f5():
    o = []
    N = {'E0': (360, 50, 'E'), 'E1': (200, 125, 'E'), 'p': (360, 125, '+'), 'T1': (520, 125, 'T'),
         'T2': (200, 200, 'T'), 'F2': (200, 275, 'F'), 'i1': (200, 345, 'id'),
         'T3': (400, 200, 'T'), 'm': (520, 200, '*'), 'F4': (640, 200, 'F'),
         'F3': (400, 275, 'F'), 'i2': (400, 345, 'id'), 'i3': (640, 275, 'id')}
    E = [('E0', 'E1'), ('E0', 'p'), ('E0', 'T1'), ('E1', 'T2'), ('T2', 'F2'), ('F2', 'i1'), ('T1', 'T3'), ('T1', 'm'),
         ('T1', 'F4'), ('T3', 'F3'), ('F3', 'i2'), ('F4', 'i3')]
    term = {'p', 'm', 'i1', 'i2', 'i3'}
    for a, b in E:
        xa, ya = N[a][:2]; xb, yb = N[b][:2]
        o.append(L(xa, ya + 20, xb, yb - (15 if b in term else 20), L2, 1.8))
    down = {'E0': 1, 'E1': 2, 'T2': 3, 'F2': 4, 'T1': 5, 'T3': 6, 'F3': 7, 'F4': 8}
    up = {'F2': 1, 'T2': 2, 'E1': 3, 'F3': 4, 'T3': 5, 'F4': 6, 'T1': 7, 'E0': 8}
    for k, (x, y, s) in N.items():
        if k in term:
            o.append(leaf(x, y, s))
        else:
            o.append(node(x, y, s))
            o.append(chip(x - 46, y, f'↓{down[k]}', AC, ACS, 13))
            o.append(chip(x + 46, y, f'↑{up[k]}', LV, LVS, 13))
    o.append(T(20, 400, '↓n: order of expansion in the top-down (leftmost) parse, root first.', 13, 'start', AC, True))
    o.append(T(20, 422, '↑n: order of reduction in the bottom-up (shift-reduce) parse, root last.', 13, 'start', LV, True))
    o.append(T(20, 444, 'Same tree, 8 productions each way: the reductions read backwards give the rightmost derivation.', 13, 'start', INK))
    return 458, ''.join(o)
FIG[5] = (f5, 'One parse tree for id + id * id, with two orders on each variable: ↓ is when the top-down parser expands it, root first, and ↑ is when the bottom-up parser reduces to it, root last. Both parsers use the same 8 productions.',
          'A parse tree for id + id * id in the grammar E → E + T | T, T → T * F | F, F → id; each variable carries a top-down expansion number 1 to 8 and a bottom-up reduction number 1 to 8.')


spec = make_spec(FIG)


def text_fixes(k):
    """no sentence in this unit's text describes the old drawings in a way the new ones contradict"""
    return []
