"""t16 split-blueprint thumbnails for Circuit Theory (ec-circuits, EEE), one spec per lesson.
Every spec is drawn from one worked example of the lesson's own chapters in books/ece/ec-circuits/ec-circuits-u<N>.html;
every number on it is computed here and matches the book's answer (the asserts check it).
Build: python3 t16_split.py build specs.py <out dir>   (lib.py, beside this file, holds the drawing helpers)."""
import cmath, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

SUBJ = 'CIRCUIT THEORY'


def near(a, b, tol=.0051):
    assert abs(a - b) <= tol * max(1, abs(b)), (a, b)


def spec(key, title, hook, take, card_title, card, board_svg, chips, summary, page, css='', fs=76):
    if fs != 76:
        css += f'h1{{font-size:{fs}px !important}}'
    assert len(card_title.replace('<sub>', '').replace('</sub>', '')) <= 26, card_title
    return dict(key=f'ec-circuits-{key}', subject=SUBJ, title=title, question=hook, takeaway=take, tag='Book example',
                card_title=card_title, card=card, board=board_svg, chips=chips, summary=summary, page_title=page, css=css)


# ================================================================ u1 L1: chapter 1.1, worked example 2 (the approved EEE sample)
def u1_L1():
    C, I, T_ = 20e-6, 10e-3, 20e-3            # (a) uncharged 20 uF fed 10 mA for 20 ms, then zero current
    Q = I * T_; V = Q / C; W = .5 * C * V ** 2
    L, VL, TL = .2, 6, .1                     # (b) 0.2 H from 0 A, 6 V for 0.1 s
    IL = VL * TL / L; WL = .5 * L * IL ** 2
    near(V, 10); near(W, 1e-3); near(IL, 3); near(WL, .9)
    for a, b in ((B.C, C), (B.I, I), (B.T, T_), (B.LH, L), (B.VL, VL), (B.TL, TL)):
        assert a == b                         # the sample's own numbers are this example's
    setup(288, 952)
    bd = B.board()
    chips = [chip('left', 300, 'g', f'{g(I * 1e3)} mA for {g(T_ * 1e3)} ms'), chip('left', 364, 'g', f'{g(V)} V at {g(T_ * 1e3)} ms'),
             chip('left', 428, 'g', f'still {g(V)} V at 1 s'), chip('right', 300, 'c', f'{g(L)} H · {g(VL)} V for {g(TL)} s'),
             chip('right', 500, 'c', f'{g(IL)} A at {g(TL)} s', False)]
    summ = (f'<b class="gl">(a)</b> v = Q/C = {Q * 1e4:g}×10⁻⁴ C ÷ {g(C * 1e6)} µF = <b class="gl">{g(V)} V</b>, ½Cv² = <b class="gl">{g(W * 1e3)} mJ</b><br>'
            f'<b class="cl">(b)</b> i = (1/L)∫v dt = {g(VL * TL)} ÷ {g(L)} = <b class="cl">{g(IL)} A</b>, ½Li² = <b class="cl">{g(WL)} J</b>')
    return spec('u1-L1', 'Circuit<br>Elements &amp;<br>Sources', "Can a capacitor's voltage jump?",
                'Capacitor voltage <span class="gold">CANNOT</span><br>jump, its current <span class="cyan">CAN</span>',
                'constant feed into C and L', B.plots_book(), bd, chips, summ, 'Circuit Elements &amp; Sources')


# ================================================================ u1 L2: chapter 1.4, worked example 1 (the bridge: counting)
def u1_L2():
    nodes = 'ABCD'
    branches = {1: 'AB', 2: 'AC', 3: 'BC', 4: 'BD', 5: 'CD', 6: 'DA'}
    n, b = len(nodes), len(branches)
    tree = n - 1; chords = b - n + 1; m = b - n + 1
    # loops: every closed path through 3 or 4 of the nodes
    import itertools
    adj = {frozenset(v) for v in branches.values()}
    loops = set()
    for k in (3, 4):
        for perm in itertools.permutations(nodes, k):
            cyc = list(perm) + [perm[0]]
            if all(frozenset((cyc[i], cyc[i + 1])) in adj for i in range(k)):
                loops.add(frozenset(frozenset((cyc[i], cyc[i + 1])) for i in range(k)))
    nl = len(loops)
    assert (n, b, tree, chords, m, nl) == (4, 6, 3, 3, 3, 7) and m + (n - 1) == b
    setup(306)
    A, Bn, Cn, D = (2.0, 1.6), (6.6, 1.6), (2.0, 6.2), (6.6, 6.2)      # B on the right, so the source runs round it
    parts = [wire([A, Bn, D, Cn, A]), wire([Bn, Cn]), wire([D, (7.6, 6.2), (7.6, .6), (2.0, .6), A])]
    # the outer loop {6, 2, 5}: source, A-C, C-D, glowing cyan (a loop, not a mesh: B, 1, 3, 4 lie inside)
    parts.append(glow([(2.0, .6), A, Cn, D, (7.6, 6.2), (7.6, .6), (2.0, .6)], CY, 4.5))
    parts.append(glow([A, Bn, Cn, A], GO, 3.2, arrows=False, dash='8 6'))
    parts += [res(4.3, 1.6, 'x', '20 Ω', L=1.4), res(2.0, 3.9, 'y', '20 Ω', L=1.4), res(6.6, 3.9, 'y', '2 Ω', L=1.4),
              res(4.3, 6.2, 'x', '8 Ω', L=1.4), res(4.3, 3.9, 'x', '10 Ω', L=1.2)]
    parts.append(vsrc(7.6, 4.9, '36 V', w=.9, d=1.3))
    parts += [post(*A, 'A'), post(*Bn, 'B'), post(*Cn, 'C'), post(*D, 'D')]
    bd = board(parts)
    card = svg(bars(0, 470, 'nodes, branches, meshes, loops', '#E6ECF1',
                    [('nodes', n, CY), ('branches', b, CY), ('tree', tree, '#9FB2C6'), ('chords', chords, '#9FB2C6'), ('meshes', m, GO), ('loops', nl, CY)], 7, top=30))
    chips = [chip('left', 300, 'c', f'n = {n} nodes'), chip('left', 364, 'c', f'b = {b} branches'), chip('left', 428, 'g', f'{m} meshes'),
             chip('right', 252, 'c', f'{nl} loops in all'), chip('right', 536, 'g', f'{n - 1} KCL + {m} KVL = {b}', False)]
    summ = (f'm = b − n + 1 = {b} − {n} + 1 = <b class="gl">{m} meshes</b>, but <b class="cl">{nl} loops</b><br>'
            f'Outer loop {{6, 2, 5}} has 1, 3, 4 inside: <b class="cl">not a mesh</b>')
    return spec('u1-L2', "Kirchhoff's<br>Laws &amp;<br>Network Terms", 'Is the outer loop a mesh?',
                f'{nl} loops, only {m} <span class="gold">MESHES</span>:<br>the outer loop is <span class="cyan">NOT</span> one',
                'counting the bridge', card, bd, chips, summ, "Kirchhoff's Laws &amp; Network Terms")


# ================================================================ u1 L3: chapter 1.5, worked example 1 (current divider)
def u1_L3():
    E, R1, R2, R3 = 12, 6, 12, 6
    R23 = R2 * R3 / (R2 + R3); Req = R1 + R23; I = E / Req
    V1, V23 = I * R1, I * R23
    I2, I3 = I * R3 / (R2 + R3), I * R2 / (R2 + R3)
    near(Req, 10); near(I, 1.2); near(V1, 7.2); near(V23, 4.8); near(I2, .4); near(I3, .8)
    setup(306)
    parts = [wire([(1.4, 2.0), (6.6, 2.0), (6.6, 6.4), (1.4, 6.4), (1.4, 2.0)]), wire([(4.6, 2.0), (4.6, 6.4)]), wire([(6.6, 2.0), (6.6, 6.4)])]
    parts.append(glow([(1.4, 5.0), (1.4, 2.0), (4.6, 2.0), (6.6, 2.0), (6.6, 6.4), (1.4, 6.4), (1.4, 5.0)], GO, 5.5))
    parts.append(glow([(4.6, 2.0), (4.6, 6.4)], CY, 3, arrows=True))
    parts += [vsrc(1.4, 4.2, f'{E} V', w=1.0, d=1.3), res(3.0, 2.0, 'x', f'R₁ {R1} Ω'),
              res(4.6, 4.2, 'y', f'R₂ {R2} Ω'), res(6.6, 4.2, 'y', f'R₃ {R3} Ω')]
    bd = board(parts)
    s = bars(0, 215, 'voltage divider', CY, [('R₁', V1, CY), ('pair', V23, CY)], 7.2, unit=' V')
    s += bars(250, 220, 'current divider', GO, [(f'{R2} Ω', I2, GO), (f'{R3} Ω', I3, GO)], .8, unit=' A')
    chips = [chip('left', 300, 'g', f'R<sub>eq</sub> = {g(Req)} Ω'), chip('left', 364, 'g', f'I = {g(I)} A'), chip('left', 428, 'c', f'{g(V1)} V across R₁'),
             chip('right', 252, 'c', f'I₂ = {g(I2)} A in {R2} Ω'), chip('right', 536, 'g', f'I₃ = {g(I3)} A in {R3} Ω', False)]
    summ = (f'I₂ = I × R₃/(R₂ + R₃) = {g(I)} × {R3}/{R2 + R3} = <b class="gl">{g(I2)} A</b><br>'
            f'I₃ = I × R₂/(R₂ + R₃) = {g(I)} × {R2}/{R2 + R3} = <b class="cl">{g(I3)} A</b>')
    return spec('u1-L3', 'Series-parallel<br>Circuits &amp;<br>Star-delta', 'Current divider: which R on top?',
                'The <span class="gold">OTHER</span> R goes on top;<br>the <span class="cyan">SMALLER</span> R takes more',
                f'{R1} Ω, then {R2} Ω ∥ {R3} Ω', svg(s), bd, chips, summ, 'Series-parallel Circuits &amp; Star-delta')


# ================================================================ u1 L4: chapter 1.8, worked example 1 (tree {4, 5, 6})
def u1_L4():
    R = {1: 20, 2: 20, 3: 10, 4: 2, 5: 8}; E = 36
    # tie-set equations in the link currents I1, I2, I3 (the book's three equations)
    import numpy as np
    Amat = np.array([[R[1] + R[4], 0, R[4]], [0, R[2] + R[5], -R[5]], [R[4], -R[5], R[3] + R[4] + R[5]]], float)
    I1, I2, I3 = np.linalg.solve(Amat, [E, E, 0])
    i = {1: I1, 2: I2, 3: I3, 4: I1 + I3, 5: I2 - I3, 6: I1 + I2}
    for k, v in zip(range(1, 7), (1.6, 1.4, .4, 2, 1, 3)):
        near(i[k], v)
    n, b = 4, 6
    twigs, links = n - 1, b - n + 1
    near(-i[1] - i[3] + i[4], 0); near(-i[2] + i[3] + i[5], 0); near(-i[1] - i[2] + i[6], 0)    # cut-set check
    setup(306)
    A, Bn, Cn, D = (2.2, 1.6), (2.2, 6.0), (6.6, 1.6), (6.6, 6.0)
    # graph: twigs 4 (B-D), 5 (C-D), 6 (D-A, round the back) gold; links 1, 2, 3 cyan dashed
    parts = [glow([Bn, D], GO, 7, arrows=False), glow([Cn, D], GO, 7, arrows=False),
             glow([D, (7.5, 6.0), (7.5, .5), (2.2, .5), A], GO, 7, arrows=False)]
    parts += [glow([A, Bn], CY, 5, arrows=False, dash='10 8'), glow([A, Cn], CY, 5, arrows=False, dash='10 8'), glow([Cn, Bn], CY, 5, arrows=False, dash='10 8')]
    parts += [lab(1.7, 3.8, .2, '1', CY, 20), lab(4.4, 1.1, .2, '2', CY, 20), lab(4.7, 4.1, .4, '3', CY, 20),
              lab(4.4, 6.6, .2, '4', GO, 20), lab(7.1, 3.8, .2, '5', GO, 20), lab(8.0, 3.2, .2, '6', GO, 20)]
    parts += [post(*A, 'A', h=30), post(*Bn, 'B', h=30), post(*Cn, 'C', h=30), post(*D, 'D', h=30)]
    bd = board(parts)
    items = [(f'i{"₁₂₃₄₅₆"[k - 1]}', i[k], CY if k <= 3 else GO) for k in range(1, 7)]
    card = svg(bars(0, 470, 'branch currents: links cyan, twigs gold', '#E6ECF1', items, 3, unit=' A', top=30))
    chips = [chip('left', 300, 'g', f'n − 1 = {twigs} twigs'), chip('left', 364, 'c', f'b − n + 1 = {links} links'), chip('left', 428, 'c', f'I₃ = {g(I3)} A'),
             chip('right', 252, 'g', f'source i₆ = {g(i[6])} A'), chip('right', 536, 'c', 'cut-sets check: 0', False)]
    summ = (f'Twigs n − 1 = <b class="gl">{twigs}</b> (4, 5, 6), links b − n + 1 = <b class="cl">{links}</b> (1, 2, 3)<br>'
            f'Tie-sets: I₁ = {g(I1)} A, I₂ = {g(I2)} A, I₃ = {g(I3)} A')
    return spec('u1-L4', 'Source<br>Transformation &amp;<br>Network Topology', 'How many twigs and links?',
                f'Twigs = n − 1 = <span class="gold">{twigs}</span>,<br>links = b − n + 1 = <span class="cyan">{links}</span>',
                'the bridge, tree {4, 5, 6}'.replace('the bridge, ', 'bridge: '), card, bd, chips, summ, 'Source Transformation &amp; Network Topology', fs=64)




# ================================================================ u2 L1: chapter 2.2, worked example 2 (supernode)
def u2_L1():
    import numpy as np
    v1 = 12.0                                   # the 12 V source fixes node 1
    # supernode {2, 3}: (v2 - 12)/2 + v2/3 + v3/4 = 2 with v3 - v2 = 6
    A = np.array([[1 / 2 + 1 / 3, 1 / 4], [-1, 1]]); rhs = [2 + v1 / 2, 6]
    v2, v3 = np.linalg.solve(A, rhs)
    i2o, i3o, i4o = (v1 - v2) / 2, v2 / 3, v3 / 4
    isrc6 = i2o - i3o                            # leaves node 2 through the 6 V source
    pdel = 12 * (i2o) + 2 * v3 + 6 * isrc6; pabs = i2o ** 2 * 2 + v2 ** 2 / 3 + v3 ** 2 / 4
    near(v2, 6); near(v3, 12); near(isrc6, 1); near(pdel, 66); near(pabs, 66)
    setup(306)
    n1, n2, n3 = (1.3, 2.0), (3.9, 2.0), (6.3, 2.0)
    parts = [wire([n1, n3, (7.5, 2.0), (7.5, 6.6), (1.3, 6.6), n1]), wire([n2, (3.9, 6.6)]), wire([n3, (6.3, 6.6)])]
    parts.append(glow([(3.2, 1.2), (7.0, 1.2), (7.0, 2.8), (3.2, 2.8), (3.2, 1.2)], GO, 3.5, arrows=False, dash='9 7'))
    parts.append(glow([n2, n3], CY, 4))
    parts += [vsrc(1.3, 4.3, '12 V', w=1.0, d=1.2), res(2.6, 2.0, 'x', '2 Ω', L=1.4), res(3.9, 4.3, 'y', '3 Ω', L=1.5),
              res(6.3, 3.8, 'y', '4 Ω', L=1.5, ldx=-.6, ldy=.4, lz=.9), isrc(7.5, 5.3, '2 A', w=1.0, d=1.0, h=.8), vsrc(5.1, 2.0, '6 V', w=1.1, d=.9, h=.7)]
    parts += [post(*n1, '1', h=20), post(*n2, '2', h=20), post(*n3, '3', h=20)]
    bd = board(parts)
    s = bars(0, 225, 'node voltages', GO, [('v₁', v1, CY), ('v₂', v2, GO), ('v₃', v3, GO)], 12, unit=' V')
    s += bars(245, 225, 'branch currents', CY, [('2 Ω', i2o, CY), ('3 Ω', i3o, CY), ('4 Ω', i4o, CY), ('6 V', isrc6, GO)], 3, unit=' A')
    chips = [chip('left', 300, 'g', f'v₃ − v₂ = {g(v3 - v2)} V'), chip('left', 364, 'c', f'v₁ = {g(v1)} V'), chip('left', 428, 'g', f'v₂ = {g(v2)} V, v₃ = {g(v3)} V'),
             chip('right', 252, 'g', 'supernode {2, 3}'), chip('right', 536, 'c', f'{g(isrc6)} A through the 6 V', False)]
    summ = (f'Supernode KCL: (v₂ − 12)/2 + v₂/3 + v₃/4 = 2<br>'
            f'with v₃ = v₂ + 6: <b class="gl">v₂ = {g(v2)} V</b>, <b class="cl">v₃ = {g(v3)} V</b>, {g(pdel)} W in = out')
    return spec('u2-L1', 'Mesh &amp;<br>Nodal<br>Analysis', 'When is it a supernode?',
                'A <span class="gold">FLOATING</span> voltage source<br>makes a <span class="cyan">SUPERNODE</span>',
                'floating 6 V source', svg(s), bd, chips, summ, 'Mesh &amp; Nodal Analysis')


# ================================================================ u2 L2: chapter 2.4, worked example 2 (Thevenin with a CCCS)
def u2_L2():
    E, R6, R12, k = 12, 6, 12, .5
    # open circuit: 1.5 (12 - v)/6 = v/12
    v = (1 + k) * E / R6 / ((1 + k) / R6 + 1 / R12); Vth = v
    ix_sc = E / R6; Isc = (1 + k) * ix_sc; Rth = Vth / Isc
    Rt_test = 1 / (1 / R12 + (1 + k) / R6)       # test source: I_t = V_t/12 + 1.5 V_t/6
    wrong = R6 * R12 / (R6 + R12); IL6 = Vth / (Rth + 6)
    near(Vth, 9); near(Isc, 3); near(Rth, 3); near(Rt_test, 3); near(wrong, 4); near(IL6, 1)
    setup(306)
    a, b_ = (4.4, 2.0), (4.4, 6.4)
    parts = [wire([(1.3, 6.4), (1.3, 2.0), (7.6, 2.0)]), wire([(1.3, 6.4), (7.6, 6.4)]), wire([a, b_]), wire([(6.2, 2.0), (6.2, 6.4)])]
    parts.append(glow([(1.3, 3.4), (1.3, 2.0), (4.2, 2.0)], CY, 4.5))
    parts += [vsrc(1.3, 4.3, f'{E} V', w=1.0, d=1.2), res(2.85, 2.0, 'x', f'{R6} Ω  iₓ →', L=1.6), res(4.4, 4.0, 'y', f'{R12} Ω', L=1.6, ldy=1.4, lz=.9),
              isrc(6.2, 5.0, f'{g(k)}iₓ', w=.95, d=.95, h=.75, diamond=True)]
    parts += [post(7.6, 2.0, 'a', h=24), post(7.6, 6.4, 'b', h=24)]
    bd = board(parts)
    f = Frame(0, 230, 'terminal line at a-b', CY, 0, 3.4, 0, 10, yt=f'{g(Vth)} V', yb='0')
    f.line([0, Isc], [Vth, 0], CY, 3.5); f.dot(0, Vth, GO); f.dot(Isc, 0, GO)
    f.xt(0, '0'); f.xt(Isc, f'I<tspan dy="3" font-size="10">sc</tspan><tspan dy="-3"> = {g(Isc)} A</tspan>', GO)
    f.text(1.7, 5.2, f'slope R<tspan dy="3" font-size="10">th</tspan><tspan dy="-3"> = {g(Rth)} Ω</tspan>', '#E6ECF1', 'start', 'ax', 4)
    s = f.s + bars(255, 215, 'R<tspan dy="3" font-size="12">th</tspan>', GO, [('kept on', Rth, GO), ('switched off', wrong, '#7E8B98')], 4, unit=' Ω')
    chips = [chip('left', 300, 'g', f'V<sub>oc</sub> = {g(Vth)} V'), chip('left', 364, 'g', f'I<sub>sc</sub> = {g(Isc)} A'), chip('left', 428, 'c', f'{g(k)}iₓ stays ON'),
             chip('right', 252, 'g', f'R<sub>th</sub> = {g(Rth)} Ω, not {g(wrong)}'), chip('right', 536, 'c', f'6 Ω load: {g(IL6)} A', False)]
    summ = (f'R<sub>th</sub> = V<sub>oc</sub>/I<sub>sc</sub> = {g(Vth)} V ÷ {g(Isc)} A = <b class="gl">{g(Rth)} Ω</b><br>'
            f'Test source: I<sub>t</sub> = V<sub>t</sub>/{g(Rt_test)}; switched off gives <b class="cl">{g(wrong)} Ω</b>')
    return spec('u2-L2', 'Superposition,<br>Thevenin &amp;<br>Norton', 'Rth with a dependent source?',
                '<span class="gold">KEEP</span> the dependent source<br>on: R<sub>th</sub> = <span class="cyan">3 Ω</span>, not 4',
                '12 V, 6 Ω, 12 Ω, 0.5iₓ', svg(s), bd, chips, summ, 'Superposition, Thevenin &amp; Norton', fs=70)


# ================================================================ u2 L3: chapter 2.5, worked example 1 (maximum power, really)
def u2_L3():
    E, Rs, Rp, R1 = 32, 4, 12, 1
    Vth = E * Rp / (Rs + Rp); Rth = R1 + Rs * Rp / (Rs + Rp)
    RL = Rth; Pmax = Vth ** 2 / (4 * Rth); eta_eq = Pmax / (Vth * Vth / (Rth + RL))
    Rload_branch = R1 + RL; Rpar = Rload_branch * Rp / (Rload_branch + Rp); Is = E / (Rs + Rpar)
    Psrc = E * Is; IL = Is * Rp / (Rp + Rload_branch); eta = IL ** 2 * RL / Psrc
    near(Vth, 24); near(Rth, 4); near(Pmax, 36); near(eta_eq, .5); near(Psrc, 136, .01); near(IL, 3); near(eta, .265, .01)
    setup(306)
    parts = [wire([(1.3, 6.4), (1.3, 2.0), (6.9, 2.0), (6.9, 6.4), (1.3, 6.4)]), wire([(4.3, 2.0), (4.3, 6.4)])]
    parts.append(glow([(4.3, 2.0), (6.9, 2.0), (6.9, 6.4), (4.3, 6.4)], GO, 5))
    parts += [vsrc(1.3, 4.3, f'{E} V', w=1.0, d=1.2), res(2.8, 2.0, 'x', f'{Rs} Ω', L=1.5), res(4.3, 4.2, 'y', f'{Rp} Ω', L=1.6),
              res(5.6, 2.0, 'x', f'{R1} Ω', L=1.2)]
    # the load: a glowing block, R_L = R_th
    parts.append(f'<g filter="url(#gl)">{B.box(6.5, 3.3, .8, 1.8, .7, "#F6D285", "#B8860B", "#D9A520")}</g>')
    parts.append(lab(6.9, 5.7, 1.1, f'R<tspan dy="4" font-size="11">L</tspan><tspan dy="-4"> = {g(RL)} Ω</tspan>', GO, 17))
    bd = board(parts)
    f = Frame(0, 270, 'load power against R<tspan dy="3" font-size="11">L</tspan>', GO, 0, 16, 0, 40, yt='36 W', yb='0', tx=150)
    rs = [i * .1 for i in range(161)]
    f.line(rs, [Vth ** 2 * r / (Rth + r) ** 2 for r in rs], GO, 3.5, fill=True)
    f.hline(Pmax, GO); f.vline(RL, GO, y_to=Pmax); f.dot(RL, Pmax, GO)
    f.xt(0, '0'); f.xt(RL, f'{g(RL)} Ω', GO); f.xt(16, '16 Ω')
    s = f.s.replace(f'y="{f.T + 6}" text-anchor="end" class="ax">36 W', f'y="{f.Y(36) + 5:.1f}" text-anchor="end" class="ax">36 W')
    s += bars(290, 180, 'efficiency', CY, [('equivalent', eta_eq * 100, '#7E8B98'), ('real', eta * 100, CY)], 50, unit=' %', vfmt=lambda v: f'{v:.3g}')
    chips = [chip('left', 300, 'c', f'V<sub>th</sub> = {g(Vth)} V'), chip('left', 364, 'g', f'R<sub>L</sub> = R<sub>th</sub> = {g(RL)} Ω'),
             chip('left', 428, 'g', f'P<sub>max</sub> = {g(Pmax)} W'), chip('right', 252, 'c', f'source gives {g(Psrc, 3)} W'),
             chip('right', 536, 'c', f'η = {eta * 100:.3g} %, not 50 %', False)]
    summ = (f'P<sub>max</sub> = V<sub>th</sub>²/4R<sub>th</sub> = {g(Vth)}² ÷ {g(4 * Rth)} = <b class="gl">{g(Pmax)} W</b><br>'
            f'Real network: {g(Pmax)} W ÷ {g(Psrc, 3)} W = <b class="cl">{eta * 100:.3g} %</b>')
    return spec('u2-L3', 'Maximum<br>Power &amp; Three<br>More Theorems', 'What is the maximum power, really?',
                f'Max power is <span class="gold">{g(Pmax)} W</span>, but<br>only <span class="cyan">{eta * 100:.3g} %</span> efficient',
                '32 V, 4 Ω, 12 Ω, 1 Ω', svg(s), bd, chips, summ, 'Maximum Power &amp; Three More Theorems')


# ================================================================ u2 L4: chapter 2.8, worked examples 1 and 2 (AC Thevenin, conjugate match)
def u2_L4():
    Vs, R, Zc, Zload = 20, 4, -4j, 4 + 4j
    Vth = Vs * Zc / (R + Zc); Zth = R * Zc / (R + Zc)
    I2 = Vth / (Zth + Zload); P_orig = abs(I2) ** 2 * Zload.real
    ZL = Zth.conjugate(); Pmax = abs(Vth) ** 2 / (4 * Zth.real)
    near(Vth.real, 10); near(Vth.imag, -10); near(Zth.real, 2); near(Zth.imag, -2); near(abs(I2 - (1 - 2j)), 0); near(P_orig, 20); near(Pmax, 25)
    setup(306)
    parts = [wire([(1.3, 6.4), (1.3, 2.0), (6.9, 2.0), (6.9, 6.4), (1.3, 6.4)]), wire([(4.4, 2.0), (4.4, 6.4)])]
    parts.append(glow([(4.4, 2.0), (6.9, 2.0), (6.9, 6.4), (4.4, 6.4)], GO, 5))
    parts += [vsrc(1.3, 4.3, f'{Vs}∠0° V', w=1.1, d=1.2, ac=True), res(2.85, 2.0, 'x', f'{R} Ω', L=1.5), can(4.4, 4.4, '−j4 Ω', rx=24, ry=13, h=78),
              res(6.9, 3.4, 'y', '2 Ω', L=1.3), toroid(6.9, 5.3, 'j2 Ω', R=30, r=11, lz=1.0)]
    bd = board(parts)
    f = Frame(0, 250, 'Z<tspan dy="3" font-size="11">th</tspan><tspan dy="-3"> and the load, Ω</tspan>', '#E6ECF1', -.5, 4.5, -3, 3, zero_axis=True, tx=135)
    o = (f.X(0), f.Y(0))
    for (z, c, t) in ((Zth, CY, f'Z<tspan dy="3" font-size="10">th</tspan><tspan dy="-3"> = 2 − j2</tspan>'), (ZL, GO, f'Z<tspan dy="3" font-size="10">L</tspan><tspan dy="-3"> = 2 + j2</tspan>')):
        f.s += arrow(o[0], o[1], f.X(z.real), f.Y(z.imag), c, 3)
        f.text(z.real, z.imag, t, c, 'start', 'ax', 8, 5)
    f.text(-.4, 2.6, 'j', '#C9D3DB', 'start'); f.text(4.4, -.25, 'R', '#C9D3DB', 'end', 'ax', 0, 16)
    s = f.s + bars(275, 195, 'load power', GO, [('4 + j4 Ω', P_orig, '#7E8B98'), ('2 + j2 Ω', Pmax, GO)], 25, unit=' W')
    chips = [chip('left', 300, 'c', f'V<sub>th</sub> = {g(Vth.real)} − j{g(-Vth.imag)} V'), chip('left', 364, 'c', f'Z<sub>th</sub> = {g(Zth.real)} − j{g(-Zth.imag)} Ω'),
             chip('left', 428, 'g', f'Z<sub>L</sub> = Z<sub>th</sub>* = {g(ZL.real)} + j{g(ZL.imag)} Ω'), chip('right', 252, 'g', f'P<sub>max</sub> = {g(Pmax)} W'),
             chip('right', 536, 'c', f'4 + j4 Ω takes {g(P_orig)} W', False)]
    summ = (f'Z<sub>th</sub> = 4 ∥ (−j4) = 2 − j2 Ω, so the load is <b class="gl">2 + j2 Ω</b><br>'
            f'P<sub>max</sub> = |V<sub>th</sub>|²/4R<sub>th</sub> = {g(abs(Vth) ** 2)} ÷ {g(4 * Zth.real)} = <b class="cl">{g(Pmax)} W</b>')
    return spec('u2-L4', 'Compensation<br>&amp; AC Network<br>Theorems', 'Zth or its conjugate for max power?',
                'Use the <span class="gold">CONJUGATE</span>:<br>the reactances <span class="cyan">CANCEL</span>',
                '20∠0° V, 4 Ω and −j4 Ω', svg(s), bd, chips, summ, 'Compensation &amp; AC Network Theorems', fs=70)


# ================================================================ u3 L1: chapter 3.1, worked example 1 (heater on 325 sin 314t)
def u3_L1():
    Vm, w = 325, 314
    f0 = w / (2 * math.pi); Vrms = Vm / math.sqrt(2); Vavg = 2 * Vm / math.pi
    FF = Vrms / Vavg; PF = Vm / Vrms
    near(f0, 49.97); near(Vrms, 229.8); near(Vavg, 206.9); near(FF, 1.11); near(PF, 1.414)
    setup(306)
    parts = [wire([(2.6, 2.6), (2.6, 1.6), (5.6, 1.6), (5.6, 3.4)]), wire([(2.6, 4.6), (2.6, 6.6), (5.6, 6.6), (5.6, 5.8)])]
    parts.append(glow([(2.6, 1.6), (5.6, 1.6), (5.6, 3.3)], CY, 4))
    parts.append(vsrc(2.6, 3.6, f'{Vm} sin {w}t V', w=1.3, d=2.0, h=1.0, ac=True))
    # the heater: a box with glowing elements on top
    parts.append(B.box(4.5, 3.4, 2.2, 2.4, .8, '#3A4652', '#222B33', '#2C3640'))
    for k in range(5):
        yy = 3.75 + k * .42
        parts.append(f'<g filter="url(#gl)">{wire([(4.75, yy), (6.45, yy)], "#FF8A3D", 5, z=.82)}</g>')
    parts.append(lab(5.6, 4.6, 1.75, 'heater', '#FFB27A', 17))
    parts.append(meter(2.6, 7.2 - .9, f'{Vrms:.1f} V', ncol=CY))
    bd = board(parts)
    fr = Frame(0, 460, f'v(t) = {Vm} sin({w}t) V, one cycle', '#E6ECF1', 0, 20, -360, 400, zero_axis=True, tx=250)
    ts = [i * .1 for i in range(201)]
    fr.line(ts, [Vm * math.sin(w * t / 1000) for t in ts], CY, 3.2)
    fr.hline(Vm, GO); fr.hline(Vrms, CY)
    fr.text(16, Vm, f'peak {Vm} V', GO, 'middle', 'pt', 0, -5); fr.text(16, Vrms, f'RMS {Vrms:.1f} V', CY, 'middle', 'pt', 0, 17)
    fr.xt(0, '0'); fr.xt(10, '10 ms'); fr.xt(20, '20 ms', anchor='end')
    chips = [chip('left', 300, 'g', f'V<sub>m</sub> = {Vm} V'), chip('left', 364, 'c', f'V<sub>rms</sub> = {Vrms:.1f} V'), chip('left', 428, 'c', f'f = {w}/2π ≈ {f0:.0f} Hz'),
             chip('right', 252, 'c', f'form factor {FF:.2f}'), chip('right', 536, 'g', f'peak factor {PF:.3f}', False)]
    summ = (f'V<sub>rms</sub> = V<sub>m</sub>/√2 = {Vm} ÷ 1.414 = <b class="cl">{Vrms:.1f} V</b> ≈ 230 V<br>'
            f'V<sub>avg</sub> = 2V<sub>m</sub>/π = <b class="gl">{Vavg:.1f} V</b>, form factor {FF:.2f}')
    return spec('u3-L1', 'Sinusoids<br>&amp; Phasors', 'Is 230 V the peak or the RMS?',
                '230 V is the <span class="cyan">RMS</span>;<br>the <span class="gold">PEAK</span> is 325 V',
                'heater on the mains', svg(fr.s), bd, chips, summ, 'Sinusoids &amp; Phasors')


def arrow(x0, y0, x1, y1, col, w=3):
    return T.arrow(x0, y0, x1, y1, col, w)


def phasor_box(x0, w, title, col):
    s = f'<text x="{x0 + w / 2:.0f}" y="18" text-anchor="middle" class="pt" fill="{col}">{title}</text>'
    return s


# ================================================================ u3 L2: chapter 3.3, worked example 1 (series coil and capacitor)
def u3_L2():
    V, f, R, L, C = 230, 50, 8, .02, 100e-6
    w = 2 * math.pi * f; XL = w * L; XC = 1 / (w * C); X = XL - XC
    Z = complex(R, X); th = math.degrees(math.atan2(X, R)); I = V / abs(Z)
    Zc = abs(complex(R, XL)); Vcoil = I * Zc
    near(XL, 6.28); near(XC, 31.83); near(X, -25.55); near(abs(Z), 26.77); near(th, -72.6); near(I, 8.59); near(Vcoil, 87.4)
    setup(306)
    parts = [wire([(1.4, 6.4), (1.4, 2.0), (6.8, 2.0), (6.8, 6.4), (1.4, 6.4)])]
    parts.append(glow([(1.4, 3.0), (1.4, 2.0), (6.8, 2.0), (6.8, 6.4), (4.0, 6.4)], CY, 4.5))
    parts += [vsrc(1.4, 4.3, f'{V} V, {f} Hz', w=1.1, d=1.3, ac=True), toroid(3.6, 2.0, f'coil {R} Ω, {g(L)} H', R=36, r=13, lz=1.2),
              can(6.8, 4.4, f'{g(C * 1e6)} µF', rx=24, ry=13, h=80)]
    bd = board(parts)
    # left: v and i over one cycle (i peaks 72.6 degrees earlier); right: the phasors, V reference, I leading
    fr = Frame(0, 250, 'v and i, one cycle', '#E6ECF1', 0, 360, -1.1, 1.1, zero_axis=True, tx=135)
    xs = list(range(0, 361, 3))
    fr.line(xs, [math.sin(math.radians(x)) for x in xs], GO, 3)
    fr.line(xs, [.62 * math.sin(math.radians(x - th)) for x in xs], CY, 3)
    fr.vline(90, GO, y_to=1); fr.vline(90 + th, CY, y_to=.62)
    fr.text(90, 1, 'v', GO, 'start', 'pt', 6, 10); fr.text(90 + th, .62, 'i', CY, 'start', 'pt', 5, -3)
    fr.xt(90 + th, f'i first, {-th:.1f}°', CY, 'start')
    s = fr.s
    cx, cy, Lv = 285, 118, 150
    s += f'<text x="{cx + 85}" y="18" text-anchor="middle" class="pt" fill="{CY}">phasors: I leads V</text>'
    s += arrow(cx, cy, cx + Lv, cy, GO, 3) + f'<text x="{cx + Lv}" y="{cy + 20}" text-anchor="end" class="pt" fill="{GO}">V = {V} V</text>'
    a_ = math.radians(-th); Li = 84
    ix, iy = cx + Li * math.cos(a_), cy - Li * math.sin(a_)
    s += arrow(cx, cy, ix, iy, CY, 3) + f'<text x="{ix + 8:.0f}" y="{iy + 12:.0f}" class="pt" fill="{CY}">I = {I:.2f} A</text>'
    s += f'<path d="M{cx + 38},{cy} A38,38 0 0 0 {cx + 38 * math.cos(a_):.1f},{cy - 38 * math.sin(a_):.1f}" fill="none" stroke="#E6ECF1" stroke-width="1.6"/>'
    s += f'<text x="{cx + 44}" y="{cy - 14}" class="ax">{-th:.1f}°</text>'
    chips = [chip('left', 300, 'c', f'X<sub>L</sub> = {XL:.2f} Ω'), chip('left', 364, 'c', f'X<sub>C</sub> = {XC:.2f} Ω'), chip('left', 428, 'g', f'|Z| = {abs(Z):.2f} Ω'),
             chip('right', 252, 'g', f'I = {I:.2f} A leading'), chip('right', 536, 'c', f'V<sub>coil</sub> = {Vcoil:.1f} V', False)]
    summ = (f'Z = {R} + j({XL:.2f} − {XC:.2f}) = <b class="gl">{R} − j{-X:.2f} Ω</b><br>'
            f'X &lt; 0, capacitive: the current <b class="cl">leads by {-th:.1f}°</b>')
    return spec('u3-L2', 'Impedance<br>&amp; AC Steady<br>State', 'Does the current lead or lag?',
                'X<sub>C</sub> wins, so the current<br><span class="gold">LEADS</span>; with X<sub>L</sub> it <span class="cyan">LAGS</span>',
                f'coil and {g(C * 1e6)} µF, {f} Hz', svg(s), bd, chips, summ, 'Impedance &amp; AC Steady State')


# ================================================================ u3 L3: chapter 3.6, worked example 1 (balanced star load)
def u3_L3():
    VL, R, X = 400, 10, 6
    Vph = VL / math.sqrt(3); Z = math.hypot(R, X); phi = math.degrees(math.atan2(X, R)); pf = R / Z
    Iph = Vph / Z; IL = Iph; P = 3 * Iph ** 2 * R; P2 = math.sqrt(3) * VL * IL * pf
    IN = abs(sum(cmath.rect(Iph, math.radians(-phi - 120 * k)) for k in range(3)))
    near(Vph, 230.9); near(Z, 11.66); near(phi, 31.0, .01); near(pf, .857); near(Iph, 19.8); near(P, 11760, .01); near(P2, P); near(IN, 0)
    setup(306)
    lines = (2.2, 3.6, 5.0)
    parts = []
    for yy in lines:
        parts.append(wire([(1.9, yy), (6.6, yy), (7.2, 3.6)]))
    parts.append(wire([(7.2, 3.6), (7.2, 6.6), (1.4, 6.6), (1.4, 5.6)], CY, 2.5))
    for yy, nm in zip(lines, 'RYB'):
        parts.append(glow([(1.9, yy), (3.3, yy)], GO, 4))
        parts.append(res(4.0, yy, 'x', '', L=1.3, w=.55, h=.55))
        parts.append(toroid(5.6, yy, '', R=22, r=8, z=.15))
        parts.append(lab(2.5, yy - .25, .3, nm, GO, 16))
    parts.append(block(1.4, 3.6, 1.0, 3.6, 1.0, f'{VL} V, 3-phase', lcol='#F6D285', lz=1.7, size=16))
    parts += [post(7.2, 3.6, 'N', h=22, ncol=CY), lab(4.3, 6.6, .3, f'neutral: I<tspan dy="4" font-size="11">N</tspan><tspan dy="-4"> = 0</tspan>', CY, 15)]
    bd = board(parts)
    # left: the voltage star, phase 230.9 V, line 400 V; right: the numbers
    cx, cy, r = 112, 82, 52
    s = f'<text x="112" y="18" text-anchor="middle" class="pt" fill="{GO}">phase and line voltage</text>'
    tips = []
    for k in range(3):
        a = math.radians(90 - 120 * k)
        tips.append((cx + r * math.cos(a), cy - r * math.sin(a)))
        s += arrow(cx, cy, *tips[-1], CY, 2.6)
    s += f'<line x1="{tips[0][0]:.1f}" y1="{tips[0][1]:.1f}" x2="{tips[1][0]:.1f}" y2="{tips[1][1]:.1f}" stroke="{GO}" stroke-width="3"/>'
    s += f'<text x="{(tips[0][0] + tips[1][0]) / 2 + 10:.0f}" y="{(tips[0][1] + tips[1][1]) / 2 - 2:.0f}" class="pt" fill="{GO}">{VL} V</text>'
    s += f'<text x="{cx - 8}" y="{cy + r + 2:.0f}" text-anchor="end" class="pt" fill="{CY}">{Vph:.1f} V</text>'
    rows = [('V<tspan dy="3" font-size="11">ph</tspan>', f'{VL}/√3 = {Vph:.1f} V', CY), ('|Z|', f'√136 = {Z:.2f} Ω', '#E6ECF1'),
            ('I<tspan dy="3" font-size="11">ph</tspan><tspan dy="-3"> = I</tspan><tspan dy="3" font-size="11">L</tspan>', f'{Iph:.1f} A', GO),
            ('cos φ', f'{pf:.3f} lag', '#E6ECF1'), ('P', f'{P / 1000:.2f} kW', GO)]
    for k, (a_, b_, c) in enumerate(rows):
        y = 36 + k * 22
        s += f'<text x="262" y="{y}" class="ax" style="font-size:16px">{a_}</text><text x="458" y="{y}" text-anchor="end" class="pt" fill="{c}">{b_}</text>'
    chips = [chip('left', 300, 'g', f'V<sub>L</sub> = {VL} V'), chip('left', 364, 'c', f'V<sub>ph</sub> = {Vph:.1f} V'), chip('left', 428, 'c', f'Z = {R} + j{X} Ω'),
             chip('right', 252, 'g', f'I<sub>L</sub> = I<sub>ph</sub> = {Iph:.1f} A'), chip('right', 536, 'c', f'I<sub>N</sub> = {IN:.0f} A', False)]
    summ = (f'I<sub>ph</sub> = {Vph:.1f} V ÷ {Z:.2f} Ω = <b class="cl">{Iph:.1f} A</b> = I<sub>L</sub><br>'
            f'P = 3I²R = 3 × {Iph:.1f}² × {R} = <b class="gl">{P / 1000:.2f} kW</b>')
    return spec('u3-L3', 'AC Power &amp;<br>Three-phase<br>Circuits', 'Delta load: is phase V = line V?',
                f'Delta: V<sub>ph</sub> = V<sub>L</sub> = <span class="gold">{VL} V</span>;<br>star: V<sub>L</sub>/√3 = <span class="cyan">{Vph:.1f} V</span>',
                f'star load, {VL} V', svg(s), bd, chips, summ, 'AC Power &amp; Three-phase Circuits')


# ================================================================ u3 L4: chapter 3.7, worked example 1 (two wattmeters)
def u3_L4():
    W1, W2 = 5.5, 2.5
    P = W1 + W2; tphi = math.sqrt(3) * (W1 - W2) / (W1 + W2); phi = math.degrees(math.atan(tphi))
    pf = math.cos(math.radians(phi)); Q = math.sqrt(3) * (W1 - W2); S = P / pf
    near(P, 8); near(tphi, .6495); near(phi, 33.0, .01); near(pf, .839); near(Q, 5.20); near(S, 9.54); near(math.sqrt(S * S - P * P), 5.20)
    setup(306)
    lines = (2.0, 3.8, 5.6)
    parts = [wire([(1.9, yy), (6.2, yy)]) for yy in lines]
    parts += [wire([(4.3, 2.4), (4.3, 5.6)], CY, 2.4, op=.85), wire([(4.6, 4.2), (4.6, 5.6)], CY, 2.4, op=.85)]
    parts.append(glow([(1.9, 2.0), (6.2, 2.0)], GO, 4)); parts.append(glow([(1.9, 3.8), (6.2, 3.8)], GO, 4))
    parts.append(block(1.3, 3.8, 1.0, 4.6, 1.0, '3-phase', lcol='#F6D285', lz=1.5, size=16))
    for yy, nm in zip(lines, 'RYB'):
        parts.append(lab(5.5, yy - .4, .25, nm, '#E6ECF1', 15))
    parts.append(block(6.9, 3.8, 1.2, 4.6, .9, 'load', ('#5A6B7A', '#2E3A46', '#3E4C5A'), lz=1.5, size=16))
    parts += [meter(3.5, 2.0, 'W₁'), meter(3.5, 3.8, 'W₂', ncol=CY)]
    bd = board(parts)
    s = bars(0, 230, 'wattmeter readings', GO, [('W₁', W1, GO), ('W₂', W2, CY), ('P', P, '#E6ECF1')], 8, unit=' kW')
    # power triangle
    x0, y0, sc = 262, 122, 22
    pP, pQ = (x0 + P * sc, y0), (x0 + P * sc, y0 - Q * sc * .72)
    s += f'<text x="365" y="18" text-anchor="middle" class="pt" fill="{CY}">power triangle</text>'
    s += f'<polygon points="{x0},{y0} {pP[0]:.1f},{pP[1]:.1f} {pQ[0]:.1f},{pQ[1]:.1f}" fill="{CY}" opacity=".12"/>'
    s += arrow(x0, y0, *pP, '#E6ECF1', 2.4) + arrow(*pP, *pQ, CY, 2.4) + arrow(x0, y0, *pQ, GO, 2.6)
    s += f'<text x="{x0 + P * sc / 2:.0f}" y="{y0 + 16}" text-anchor="middle" class="ax">P = {g(P)} kW</text>'
    s += f'<text x="{pP[0] - 6:.0f}" y="{(pP[1] + pQ[1]) / 2 + 4:.0f}" text-anchor="end" class="ax" fill="{CY}">Q = {Q:.2f}</text>'
    s += f'<text x="{x0 + 4}" y="{y0 - 44}" class="ax" fill="{GO}">S = {S:.2f} kVA</text><text x="{x0 + 44}" y="{y0 - 6}" class="ax">{phi:.0f}°</text>'
    chips = [chip('left', 300, 'g', f'W₁ = {W1} kW'), chip('left', 364, 'c', f'W₂ = {W2} kW'), chip('left', 428, 'g', f'P = W₁ + W₂ = {g(P)} kW'),
             chip('right', 252, 'c', f'pf = {pf:.3f} lagging'), chip('right', 536, 'g', f'Q = {Q:.2f} kVAR', False)]
    summ = (f'tan φ = <b class="gl">√3</b>(W₁ − W₂)/(W₁ + W₂) = {tphi:.4f}<br>'
            f'φ = {phi:.1f}°, pf = <b class="cl">{pf:.3f} lagging</b>, Q = {Q:.2f} kVAR')
    return spec('u3-L4', 'Two<br>Wattmeters &amp;<br>Harmonics', 'Where does the √3 go?',
                'The <span class="gold">√3</span> multiplies the<br><span class="cyan">DIFFERENCE</span> W₁ − W₂',
                'two-wattmeter method', svg(s), bd, chips, summ, 'Two Wattmeters &amp; Harmonics')


# ================================================================ u4 L1: chapter 4.2, worked example 1 (parallel RLC)
def u4_L1():
    R, L, C, V = 1000, 10e-3, 1e-6, 10
    w0 = 1 / math.sqrt(L * C); f0 = w0 / (2 * math.pi); Q = R / (w0 * L); BW = f0 / Q
    Is = V / R; IL = V / (w0 * L); IC = V * w0 * C
    near(w0, 1e4); near(f0, 1591.55); near(Q, 10); near(BW, 159.15); near(Is, .01); near(IL, .1); near(IC, .1)
    Zf = lambda f: 1 / abs(1 / R + 1j * (2 * math.pi * f * C - 1 / (2 * math.pi * f * L)))
    near(Zf(f0), R)
    setup(306)
    parts = [wire([(1.3, 6.4), (1.3, 2.0), (6.9, 2.0), (6.9, 6.4), (1.3, 6.4)]), wire([(3.3, 2.0), (3.3, 6.4)]), wire([(5.1, 2.0), (5.1, 6.4)])]
    parts.append(glow([(5.1, 4.6), (5.1, 2.0), (6.9, 2.0), (6.9, 6.4), (5.1, 6.4), (5.1, 4.6)], GO, 5.5))
    parts.append(glow([(1.3, 3.2), (1.3, 2.0), (3.3, 2.0), (3.3, 3.0)], CY, 2.5))
    parts += [vsrc(1.3, 4.3, f'{V} V rms', w=1.0, d=1.2, ac=True), res(3.3, 4.3, 'y', '1 kΩ', L=1.6, ldy=1.3, lz=.9),
              toroid(5.1, 4.2, '10 mH', R=32, r=12, lz=1.1), can(6.9, 4.4, '1 µF', rx=22, ry=12, h=70)]
    bd = board(parts)
    fr = Frame(0, 270, '|Z| against f', GO, 1200, 2000, 0, 1100, yt='1 kΩ', yb='0', tx=150)
    fs = [1200 + 4 * k for k in range(201)]
    fr.line(fs, [Zf(f) for f in fs], GO, 3.4, fill=True)
    fr.s = fr.s.replace(f'y="{fr.T + 6}" text-anchor="end" class="ax">1 kΩ', f'y="{fr.Y(1000) + 5:.1f}" text-anchor="end" class="ax">1 kΩ')
    fr.vline(f0, GO, y_to=1000); fr.dot(f0, 1000, GO)
    f1, f2 = f0 - BW / 2, f0 + BW / 2
    fr.s += f'<line x1="{fr.X(f1):.1f}" y1="{fr.Y(707):.1f}" x2="{fr.X(f2):.1f}" y2="{fr.Y(707):.1f}" stroke="{CY}" stroke-width="2.4"/>'
    fr.text(f2, 707, f'BW {BW:.0f} Hz', CY, 'start', 'ax', 6, 4)
    fr.xt(f0, f'{f0:.0f} Hz', GO); fr.xt(1200, '1.2k'); fr.xt(2000, '2k', anchor='end')
    s = fr.s + bars(290, 180, 'currents at f₀, mA', CY, [('I<tspan dy="3" font-size="10">s</tspan>', Is * 1e3, CY), ('I<tspan dy="3" font-size="10">L</tspan>', IL * 1e3, GO), ('I<tspan dy="3" font-size="10">C</tspan>', IC * 1e3, GO)], 100)
    chips = [chip('left', 300, 'g', f'f₀ = {f0:.2f} Hz'), chip('left', 364, 'g', 'Z = R = 1 kΩ'), chip('left', 428, 'c', f'Q = {g(Q)}'),
             chip('right', 252, 'c', f'I<sub>s</sub> = {g(Is * 1e3)} mA'), chip('right', 536, 'g', f'I<sub>L</sub> = I<sub>C</sub> = {g(IL * 1e3)} mA', False)]
    summ = (f'At f₀ the L and C currents cancel: <b class="gl">Z = R = 1 kΩ</b><br>'
            f'I<sub>s</sub> = {V} V ÷ 1 kΩ = <b class="cl">{g(Is * 1e3)} mA</b>; {g(IL * 1e3)} mA circulates')
    return spec('u4-L1', 'Series &amp;<br>Parallel<br>Resonance', 'At parallel resonance, is Z max or min?',
                'Parallel: Z is <span class="gold">MAX</span>;<br>series: Z is <span class="cyan">MIN</span>',
                '1 kΩ ∥ 10 mH ∥ 1 µF', svg(s), bd, chips, summ, 'Series &amp; Parallel Resonance')


# ================================================================ u4 L2: chapter 4.4, worked example 1 (RC low-pass)
def u4_L2():
    R, C, f = 1000, 100e-9, 1000
    fc = 1 / (2 * math.pi * R * C); r = f / fc; H = 1 / math.sqrt(1 + r * r); ph = -math.degrees(math.atan(r)); dB = 20 * math.log10(round(H, 3))
    near(fc, 1591.5); near(r, .6283); near(H, .847); near(ph, -32.1, .01); near(dB, -1.44, .01)
    near(1 / math.sqrt(2), .7071)
    setup(306)
    parts = [wire([(1.3, 6.4), (1.3, 2.0), (7.3, 2.0)]), wire([(1.3, 6.4), (7.3, 6.4)]), wire([(5.4, 2.0), (5.4, 6.4)])]
    parts.append(glow([(5.4, 2.0), (7.3, 2.0)], GO, 4, arrows=False))
    parts += [vsrc(1.3, 4.3, 'v<tspan dy="4" font-size="11">in</tspan>', w=1.0, d=1.2, ac=True), res(3.3, 2.0, 'x', '1 kΩ', L=1.6),
              can(5.4, 4.4, '100 nF', rx=22, ry=12, h=72), post(7.3, 2.0, 'v<tspan dy="4" font-size="11">out</tspan>', h=24), post(7.3, 6.4, None, h=24)]
    bd = board(parts)
    lf = lambda v: math.log10(v)
    fr = Frame(0, 240, 'gain |H|', GO, 2, 4.3, 0, 1.05, yt='1', yb='0', tx=130)
    xs = [2 + k * .023 for k in range(101)]
    fr.line(xs, [1 / math.sqrt(1 + (10 ** x / fc) ** 2) for x in xs], GO, 3.2)
    fr.hline(.7071, GO); fr.text(4.3, .7071, '0.707', GO, 'end', 'pt', -2, -6)
    fr.dot(lf(fc), .7071, GO); fr.dot(lf(f), H, CY); fr.text(lf(f), H, f'{H:.3f}', CY, 'end', 'pt', -8, 0)
    fr.xt(2, '100'); fr.xt(3, '1k'); fr.xt(lf(fc), f'f<tspan dy="3" font-size="10">c</tspan>', GO); fr.xt(4.3, '20k Hz', anchor='end')
    fp = Frame(250, 220, 'phase', CY, 2, 4.3, -90, 0, yt='0°', yb='−90°', tx=370)
    fp.line(xs, [-math.degrees(math.atan(10 ** x / fc)) for x in xs], CY, 3.2)
    fp.dot(lf(f), ph, CY); fp.text(lf(f), ph, f'{g(ph, 3)}°', CY, 'end', 'pt', -8, 4)
    fp.dot(lf(fc), -45, GO); fp.text(lf(fc), -45, '−45°', GO, 'start', 'pt', 8, 4)
    fp.xt(3, '1k'); fp.xt(4.3, '20k', anchor='end')
    chips = [chip('left', 300, 'c', 'R = 1 kΩ, C = 100 nF'), chip('left', 364, 'g', f'f<sub>c</sub> = {fc:.1f} Hz'), chip('left', 428, 'g', '−3 dB: |H| = 0.707'),
             chip('right', 252, 'c', f'|H| = {H:.3f} at 1 kHz'), chip('right', 536, 'c', f'phase {g(ph, 3)}°', False)]
    summ = (f'f<sub>c</sub> = 1/(2πRC) = <b class="gl">{fc:.1f} Hz</b>, |H| = 1/√2 = 0.707<br>'
            f'At 1 kHz: |H| = 1/√(1 + {r:.4f}²) = <b class="cl">{H:.3f}</b> ({g(dB, 3)} dB)')
    return spec('u4-L2', 'Frequency<br>Response, Locus<br>&amp; Coupling', 'Is the −3 dB gain 0.5 or 0.707?',
                '−3 dB is <span class="gold">0.707</span>, not 0.5:<br>it is half the <span class="cyan">POWER</span>',
                'RC low-pass filter', svg(fr.s + fp.s), bd, chips, summ, 'Frequency Response, Locus &amp; Coupling', fs=66)


# ================================================================ u4 L3: chapter 4.7, worked example 1 (series coils, aiding and opposing)
def u4_L3():
    L1, L2, M = 2, 3, 1
    aid = L1 + L2 + 2 * M; opp = L1 + L2 - 2 * M; lim = math.sqrt(L1 * L2)
    assert (aid, opp) == (7, 3) and M <= lim; near(lim, 2.449)
    setup(306)
    c1, c2 = (3.1, 4.6), (5.7, 2.4)                    # side by side across the board
    path = [(3.1, 7.0), c1, (5.7, 4.6), c2, (7.4, 2.4)]
    parts = [wire(path), glow([(3.1, 7.0), (3.1, 5.4)], CY, 4.5), glow([(3.1, 4.6), (5.7, 4.6), (5.7, 3.0)], CY, 4.5), glow([(6.4, 2.4), (7.4, 2.4)], CY, 4.5)]
    parts += [post(3.1, 7.0, None, h=22), post(7.4, 2.4, None, h=22)]
    parts += [solenoid(*c1, f'L₁ = {L1} H', rx=26, ry=14, h=100, turns=11, dot=GO), solenoid(*c2, f'L₂ = {L2} H', rx=28, ry=15, h=118, turns=13, dot=GO)]
    (xa, ya), (xb, yb) = P(*c1), P(*c2)
    parts.append(f'<path d="M{xa + 10:.1f},{ya - 112:.1f} Q{(xa + xb) / 2:.1f},{min(ya, yb) - 190:.1f} {xb - 10:.1f},{yb - 132:.1f}" fill="none" stroke="{CY}" stroke-width="3" stroke-dasharray="8 6" filter="url(#gl)"/>')
    parts.append(f'<text x="{(xa + xb) / 2:.1f}" y="{min(ya, yb) - 168:.1f}" text-anchor="middle" class="capl" style="font-size:18px;paint-order:stroke;stroke:{INK};stroke-width:5px" fill="{CY}">M = {M} H</text>')
    bd = board(parts)
    s = bars(0, 470, 'equivalent inductance in series', '#E6ECF1',
             [('L₁', L1, '#9FB2C6'), ('L₂', L2, '#9FB2C6'), ('aiding, +2M', aid, GO), ('opposing, −2M', opp, CY)], 7, unit=' H', top=30)
    chips = [chip('left', 300, 'c', f'L₁ = {L1} H'), chip('left', 364, 'c', f'L₂ = {L2} H'), chip('left', 428, 'g', f'M = {M} H'),
             chip('right', 252, 'g', f'aiding: {aid} H'), chip('right', 536, 'c', f'opposing: {opp} H', False)]
    summ = (f'Aiding: L₁ + L₂ + <b class="gl">2M</b> = {L1} + {L2} + {2 * M} = <b class="gl">{aid} H</b><br>'
            f'Opposing: L₁ + L₂ − 2M = {L1} + {L2} − {2 * M} = <b class="cl">{opp} H</b>')
    return spec('u4-L3', 'Coupled Coils,<br>Transformers &amp;<br>Magnetic Circuits', 'Aiding coils: plus M or plus 2M?',
                f'Add <span class="gold">2M</span>, not M:<br>M = {M} H gives <span class="cyan">{aid} H</span>',
                'two coils in series', svg(s), bd, chips, summ, 'Coupled Coils, Transformers &amp; Magnetic Circuits', fs=60)


# ================================================================ u5 L1: chapter 5.3, worked example 1 (RC step)
def u5_L1():
    E, R, C = 10, 50e3, 2e-6
    tau = R * C; v = lambda t: E * (1 - math.exp(-t / tau)); i = lambda t: E / R * math.exp(-t / tau)
    near(tau, .1); near(v(.1), 6.321); near(i(0) * 1e3, .2); near(math.exp(-1), .3679)
    setup(306)
    parts = [wire([(1.3, 6.4), (1.3, 2.0), (2.4, 2.0)]), wire([(3.4, 2.0), (6.9, 2.0), (6.9, 6.4), (1.3, 6.4)])]
    parts.append(glow([(3.4, 2.0), (6.9, 2.0), (6.9, 3.2)], CY, 4.5))
    parts += [vsrc(1.3, 4.3, f'{E} V', w=1.0, d=1.2), post(2.4, 2.0, None, h=16), post(3.4, 2.0, None, h=16)]
    (x0, y0), (x1, y1) = P(2.4, 2.0, .5), P(3.3, 2.0, .62)
    parts.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#E6ECF1" stroke-width="5" stroke-linecap="round"/>')
    parts.append(lab(2.9, 2.0, 1.4, 't = 0', GO, 16))
    parts += [res(5.0, 2.0, 'x', '50 kΩ', L=1.7), can(6.9, 5.3, '2 µF', rx=25, ry=14, h=74)]
    bd = board(parts)
    fv = Frame(0, 235, 'v<tspan dy="3" font-size="11">C</tspan><tspan dy="-3"> charges</tspan>', GO, 0, .5, 0, 10, yt='10 V', yb='0', tx=130)
    ts = [k * .005 for k in range(101)]
    fv.line(ts, [v(t) for t in ts], GO, 3.4, fill=True); fv.hline(10, GO); fv.vline(tau, GO, y_to=v(tau)); fv.dot(tau, v(tau), GO)
    fv.text(tau, v(tau), f'{v(tau):.2f} V', GO, 'start', 'pt', 8, 14); fv.xt(0, '0'); fv.xt(tau, 'τ = 0.1 s', GO); fv.xt(.5, '0.5 s', anchor='end')
    fi = Frame(245, 225, 'i decays', CY, 0, .5, 0, .2, yb='0', tx=370)
    fi.text(0, .2, '0.2 mA', CY, 'start', 'ax', 8, 6)
    fi.line(ts, [i(t) * 1e3 for t in ts], CY, 3.4, fill=True); fi.vline(tau, CY, y_to=i(tau) * 1e3); fi.dot(tau, i(tau) * 1e3, CY)
    fi.text(tau, i(tau) * 1e3, f'{i(tau) * 1e3:.4f} mA', CY, 'start', 'pt', 8, -8); fi.xt(tau, 'τ', CY); fi.xt(.5, '0.5 s', anchor='end')
    chips = [chip('left', 300, 'g', f'τ = RC = {g(tau)} s'), chip('left', 364, 'c', f'{E} V step'), chip('left', 428, 'g', f'v<sub>C</sub>(τ) = {v(tau):.2f} V'),
             chip('right', 252, 'c', f'i = 0.2e<sup>−10t</sup> mA'), chip('right', 536, 'c', f'{math.exp(-1) * 100:.1f} % still to go', False)]
    summ = (f'τ = 50 kΩ × 2 µF = <b class="gl">{g(tau)} s</b>, v<sub>C</sub> = 10(1 − e<sup>−10t</sup>) V<br>'
            f'At t = τ: 10(1 − {math.exp(-1):.4f}) = <b class="cl">{v(tau):.2f} V</b>, 36.8 % left to go')
    return spec('u5-L1', 'First-order<br>Transients', 'What is left after one time constant?',
                f'After one τ: <span class="gold">63.2 %</span> done,<br><span class="cyan">36.8 %</span> left',
                '10 V into 50 kΩ and 2 µF', svg(fv.s + fi.s), bd, chips, summ, 'First-order Transients')


# ================================================================ u5 L2: chapter 5.4, worked examples 1 and 2 (three dampings)
def u5_L2():
    L, C, E = 1, .01, 10
    w0 = 1 / math.sqrt(L * C)
    cases = {}
    for R in (4, 20, 40):
        a = R / (2 * L); cases[R] = (a, a / w0)
    near(w0, 10); assert [cases[R][0] for R in (4, 20, 40)] == [2, 10, 20] and [cases[R][1] for R in (4, 20, 40)] == [.2, 1, 2]
    a = 2; wd = math.sqrt(w0 ** 2 - a ** 2); A2 = -a * 10 / wd
    v4 = lambda t: E - math.exp(-a * t) * (10 * math.cos(wd * t) - A2 * math.sin(wd * t))
    v20 = lambda t: E - E * (1 + 10 * t) * math.exp(-10 * t)
    s1, s2 = -20 + math.sqrt(400 - 100), -20 - math.sqrt(400 - 100)
    v40 = lambda t: E + (-E * s2 / (s2 - s1)) * math.exp(s1 * t) + (E * s1 / (s2 - s1)) * math.exp(s2 * t)
    tp = math.pi / wd; vp = v4(tp)
    near(wd, 9.80); near(A2, -2.04); near(tp, .321); near(vp, 15.27); near((vp - E) / E, .527, .01); near(v40(0), 0); near(v20(0), 0)
    setup(306)
    parts = [wire([(1.3, 6.4), (1.3, 2.0), (6.9, 2.0), (6.9, 6.4), (1.3, 6.4)])]
    parts.append(glow([(1.3, 3.2), (1.3, 2.0), (6.9, 2.0), (6.9, 3.4)], GO, 4.5))
    parts += [vsrc(1.3, 4.3, f'{E} V step', w=1.0, d=1.2), res(3.0, 2.0, 'x', 'R = 4, 20, 40 Ω', L=1.5),
              toroid(5.0, 2.0, f'{L} H', R=32, r=12, lz=1.3), can(6.9, 5.3, f'{g(C)} F', rx=25, ry=14, h=74)]
    bd = board(parts)
    fr = Frame(0, 470, 'capacitor voltage after the 10 V step', '#E6ECF1', 0, 1.6, 0, 16, yt='15.27', yb='0', tx=250)
    fr.s = fr.s.replace(f'y="{fr.T + 6}" text-anchor="end" class="ax">15.27', f'y="{fr.Y(vp) + 5:.1f}" text-anchor="end" class="ax" fill="{GO}">15.27')
    ts = [k * .008 for k in range(201)]
    fr.hline(10, '#9FB2C6'); fr.text(0, 10, '10', '#C9D3DB', 'end', 'ax', -6, 5)
    fr.line(ts, [v40(t) for t in ts], '#9FB2C6', 3); fr.line(ts, [v20(t) for t in ts], CY, 3); fr.line(ts, [v4(t) for t in ts], GO, 3.4)
    fr.dot(tp, vp, GO); fr.text(tp, vp, f'{vp:.2f} V at {tp:.3f} s', GO, 'start', 'pt', 10, 4)
    for x_, t_, c_ in ((.85, '4 Ω rings', GO), (1.2, '20 Ω', CY), (1.42, '40 Ω', '#9FB2C6')):
        fr.text(x_, 3.2, t_, c_, 'start', 'pt')
    fr.xt(0, '0'); fr.xt(1.6, '1.6 s', anchor='end')
    chips = [chip('left', 300, 'g', f'ω₀ = {g(w0)} rad/s'), chip('left', 364, 'g', '4 Ω: ζ = 0.2, rings'), chip('left', 428, 'c', '20 Ω: ζ = 1, critical'),
             chip('right', 252, 'c', '40 Ω: ζ = 2, overdamped'), chip('right', 536, 'g', f'ω<sub>d</sub> = {wd:.2f} rad/s', False)]
    summ = (f'α = R/2L against ω₀ = <b class="gl">{g(w0)} rad/s</b>: α = 2, 10, 20 s⁻¹<br>'
            f'R = 4 Ω peaks at <b class="cl">{vp:.2f} V</b> at {tp:.3f} s ({(vp - E) / E * 100:.1f} % over)')
    return spec('u5-L2', 'Second-order<br>RLC Circuits', 'Overdamped, or does it ring?',
                'α &lt; ω₀ <span class="gold">RINGS</span>;<br>α &gt; ω₀ is <span class="cyan">OVERDAMPED</span>',
                'series RLC, 1 H, 0.01 F', svg(fr.s), bd, chips, summ, 'Second-order RLC Circuits')


# ================================================================ u5 L3: chapter 5.8, worked example 1 (poles of a series RLC)
def u5_L3():
    L, C = 1, .01
    wn = math.sqrt(1 / (L * C))
    res_ = {}
    for R in (2, 10):
        z = R / (2 * wn)
        p = (-R + cmath.sqrt(R * R - 4 * wn ** 2)) / 2
        wr = wn * math.sqrt(1 - 2 * z * z); Hp = 1 / (2 * z * math.sqrt(1 - z * z))
        res_[R] = (z, p, wr, Hp)
    H = lambda R, w: wn ** 2 / abs(complex(wn ** 2 - w * w, R * w))
    near(res_[2][1].real, -1); near(res_[2][1].imag, 9.9499); near(res_[2][3], 5.0252); near(res_[10][1].real, -5); near(res_[10][1].imag, 8.6603)
    near(res_[10][3], 1.1547); near(H(10, 10), 1); near(H(2, res_[2][2]), res_[2][3]); near(res_[2][2], 9.8995); near(res_[10][2], 7.0711)
    setup(306)
    X = lambda sg: .6 + (sg + 7) / 8.5 * 6.8           # sigma from -7 to 1.5 along the board's x
    Y = lambda w: 4 - w * 3.3 / 11                       # +j omega towards the back
    x0 = X(0)
    parts = [f'<polygon points="{pts(P(.4, .4, .01), P(x0, .4, .01), P(x0, 7.6, .01), P(.4, 7.6, .01))}" fill="{CY}" opacity=".16"/>']
    parts += [wire([(.4, 4), (7.6, 4)], '#9FB2C6', 2.4), wire([(x0, .4), (x0, 7.6)], '#9FB2C6', 2.4)]
    parts += [lab(7.8, 4.4, .1, 'σ', '#E6ECF1', 20), lab(x0 + .5, .2, .1, 'jω', '#E6ECF1', 20), lab(1.3, 1.5, .05, 'left half: stable', CY, 15)]
    for R, col in ((2, GO), (10, CY)):
        p = res_[R][1]
        for sgn in (1, -1):
            cx_, cy_ = P(X(p.real), Y(sgn * p.imag), .02)
            parts.append(f'<g filter="url(#gl)"><path d="M{cx_ - 11:.1f},{cy_ - 7:.1f}L{cx_ + 11:.1f},{cy_ + 7:.1f}M{cx_ + 11:.1f},{cy_ - 7:.1f}L{cx_ - 11:.1f},{cy_ + 7:.1f}" stroke="{col}" stroke-width="5" stroke-linecap="round"/></g>')
        parts.append(lab(X(p.real), Y(p.imag), .9, f'{g(p.real)} ± j{p.imag:.2f}', col, 16))
        parts.append(lab(X(p.real), Y(-p.imag), .9, f'R = {R} Ω', col, 15))
    bd = board(parts)
    fr = Frame(0, 470, '|H(jω)| = 100/|100 − ω² + jRω|', '#E6ECF1', 0, 20, 0, 5.4, yt='5.03', yb='0', tx=250)
    fr.s = fr.s.replace(f'y="{fr.T + 6}" text-anchor="end" class="ax">5.03', f'y="{fr.Y(res_[2][3]) + 5:.1f}" text-anchor="end" class="ax" fill="{GO}">5.03')
    ws = [k * .05 for k in range(401)]
    fr.line(ws, [H(10, w) for w in ws], CY, 3.2); fr.line(ws, [H(2, w) for w in ws], GO, 3.4)
    fr.dot(res_[2][2], res_[2][3], GO); fr.text(res_[2][2], res_[2][3], f'R = 2 Ω, peak {res_[2][3]:.4f}', GO, 'start', 'pt', 10, 6)
    fr.dot(res_[10][2], res_[10][3], CY); fr.text(11.5, 2.1, f'R = 10 Ω, peak {res_[10][3]:.4f}', CY, 'start', 'pt')
    fr.xt(0, '0'); fr.xt(10, '10'); fr.xt(20, '20 rad/s', anchor='end')
    chips = [chip('left', 300, 'c', 'H(s) = 100/(s² + Rs + 100)'), chip('left', 364, 'g', 'no finite zeros'), chip('left', 428, 'g', f'R = 2 Ω: ζ = {res_[2][0]:g}'),
             chip('right', 252, 'c', f'R = 10 Ω: ζ = {res_[10][0]:g}'), chip('right', 536, 'c', 'all poles in the left half', False)]
    summ = (f's² + 2s + 100 = 0: poles <b class="gl">−1 ± j{res_[2][1].imag:.4f}</b><br>'
            f's² + 10s + 100 = 0: poles <b class="cl">−5 ± j{res_[10][1].imag:.4f}</b>')
    return spec('u5-L3', 'Laplace Analysis,<br>Poles &amp; State<br>Variables', 'Do zeros decide stability?',
                '<span class="gold">POLES</span> decide stability;<br>the zeros <span class="cyan">DON\'T</span>',
                'series RLC, output on C', svg(fr.s), bd, chips, summ, 'Laplace Analysis, Poles &amp; State Variables', fs=62)


def tnet(Z1, Z2, Z3):
    """Z parameters of a T network (series arms Z1, Z2, shunt arm Z3)"""
    return [[Z1 + Z3, Z3], [Z3, Z2 + Z3]]


def fm(v, n=4):
    s = g(v, n)
    return s.replace('-', '−')


def t_board(shunt_parts, test=False, open2=False, glow_path=None, shunt_glow=None):
    """the T network on the board: ports 1-1' and 2-2', series arms 2 and 3 ohms, the shunt arm given"""
    parts = [wire([(1.2, 2.0), (7.2, 2.0)]), wire([(1.2, 6.4), (7.2, 6.4)]), wire([(4.2, 2.0), (4.2, 6.4)])]
    if glow_path:
        parts.append(glow(glow_path, CY, 4.5))
    if shunt_glow:
        parts.append(glow(shunt_glow, GO, 5, arrows=False))
    parts += [res(2.7, 2.0, 'x', '2 Ω', L=1.5), res(5.7, 2.0, 'x', '3 Ω', L=1.5)] + shunt_parts
    if test:
        parts.append(wire([(1.2, 2.0), (1.2, 6.4)])); parts.append(isrc(1.2, 4.2, 'I₁', w=1.0, d=1.0, h=.8))
    parts += [post(1.2, 2.0, '1', h=24), post(1.2, 6.4, "1′", h=24), post(7.2, 2.0, '2', h=24), post(7.2, 6.4, "2′", h=24)]
    return parts


# ================================================================ u6 L1: chapter 6.2, worked example 1 (Z and Y of the T network)
def u6_L1():
    Z = tnet(2, 3, 4); d = Z[0][0] * Z[1][1] - Z[0][1] * Z[1][0]
    Y = [[Z[1][1] / d, -Z[0][1] / d], [-Z[1][0] / d, Z[0][0] / d]]
    rin = 2 + 3 * 4 / 7; y11 = 1 / rin; vc = 1 - 2 * y11; y21 = -vc / 3
    assert Z == [[6, 4], [4, 7]] and d == 26
    near(Y[0][0], .2692); near(Y[0][1], -.1538); near(Y[1][1], .2308); near(y11, Y[0][0]); near(y21, Y[1][0])
    setup(306)
    parts = t_board([res(4.2, 4.2, 'y', '4 Ω', L=1.6, ldy=1.3, lz=.9)], test=True, glow_path=[(1.2, 3.0), (1.2, 2.0), (4.2, 2.0), (4.2, 6.4), (1.2, 6.4), (1.2, 5.4)])
    parts.append(lab(7.6, 4.2, .4, 'open', GO, 17))
    bd = board(parts)
    m1, w1 = matrix(18, 46, [[g(v) for v in r] for r in Z], GO, cw=40)
    m2, w2 = matrix(222, 46, [[fm(v) for v in r] for r in Y], CY, cw=104)
    s = (f'<text x="{18 + w1 / 2}" y="18" text-anchor="middle" class="pt" fill="{GO}">[Z], Ω</text>'
         f'<text x="{18 + w1 / 2}" y="132" text-anchor="middle" class="ax">port 2 open</text>' + m1 +
         f'<text x="{222 + w2 / 2}" y="18" text-anchor="middle" class="pt" fill="{CY}">[Y], S</text>'
         f'<text x="{222 + w2 / 2}" y="132" text-anchor="middle" class="ax">port 2 shorted</text>' + m2 +
         f'<text x="{(18 + w1 + 222) / 2:.0f}" y="84" text-anchor="middle" class="ax">Δz = {d}</text>')
    chips = [chip('left', 300, 'g', 'port 2 open: I₂ = 0'), chip('left', 364, 'g', 'z₁₁ = 2 + 4 = 6 Ω'), chip('left', 428, 'c', 'z₂₁ = 4 Ω'),
             chip('right', 252, 'c', f'Δz = {d} Ω²'), chip('right', 536, 'c', f'y₁₁ = {Y[0][0]:.4f} S', False)]
    summ = (f'z₁₁ = V₁/I₁, port 2 <b class="gl">open</b>: 2 + 4 = 6 Ω<br>'
            f'y₁₁ = I₁/V₁, port 2 <b class="cl">shorted</b>: 1 ÷ {rin:.4f} = {y11:.4f} S')
    return spec('u6-L1', 'Two-port<br>Networks: Z &amp;<br>Y Parameters', 'Open or short port 2 for z₁₁?',
                'z: <span class="gold">OPEN</span> the other port;<br>y: <span class="cyan">SHORT</span> it',
                'T network, 2, 3 and 4 Ω', svg(s), bd, chips, summ, 'Two-port Networks: Z &amp; Y Parameters')


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


# ================================================================ u6 L2: chapter 6.4, worked example 2 (cascade of three blocks)
def u6_L2():
    T1, T2, T3 = [[1, 2], [0, 1]], [[1, 0], [.25, 1]], [[1, 3], [0, 1]]
    T12 = mul(T1, T2); Tt = mul(T12, T3); ZL = 10
    A, B_, C_, D = Tt[0][0], Tt[0][1], Tt[1][0], Tt[1][1]
    Zin = (A * ZL + B_) / (C_ * ZL + D); gain = ZL / (A * ZL + B_)
    assert T12 == [[1.5, 2], [.25, 1]] and Tt == [[1.5, 6.5], [.25, 1.75]]
    near(Zin, 5.0588); near(2 + (3 + ZL) * 4 / (3 + ZL + 4), Zin); near(gain, .4651)
    near(A * D - B_ * C_, 1)
    setup(306)
    parts = [wire([(.9, 2.4), (7.6, 2.4)]), wire([(.9, 5.6), (7.6, 5.6)])]
    parts.append(glow([(1.0, 6.9), (6.9, 6.9)], GO, 4))
    for k, (x, name) in enumerate(((2.0, '2 Ω'), (4.0, '0.25 S'), (6.0, '3 Ω'))):
        parts.append(B.box(x - .75, 1.9, 1.5, 4.2, .5, '#3A4A5C', '#1E2832', '#2A3642'))
        if k == 1:
            parts.append(res(x, 4.0, 'y', '', L=1.6, w=.5, h=.4) .replace('<polygon', '<polygon transform="translate(0 -16)"'))
        else:
            parts.append(res(x, 2.4, 'x', '', L=1.1, w=.45, h=.4).replace('<polygon', '<polygon transform="translate(0 -16)"'))
        parts.append(lab(x + .1, 5.6, .9, name, '#E6ECF1', 16))
        parts.append(lab(x - .1, 1.4, .8, f'T{"₁₂₃"[k]}', GO, 18))
    parts.append(res(7.6, 4.0, 'y', '10 Ω', L=1.6, ldy=1.3, lz=.9))
    parts += [post(.9, 2.4, None, h=20), post(.9, 5.6, None, h=20)]
    bd = board(parts)
    mats = [T1, T2, T3, Tt]
    s, x = '', 2
    for k, mtx in enumerate(mats):
        col = GO if k == 3 else '#E6ECF1'
        mm, w = matrix(x, 46, [[g(v) for v in r] for r in mtx], col, cw=33 if k < 3 else 46, size=16)
        s += mm
        lbl = f'T{"₁₂₃"[k]}' if k < 3 else '[T]'
        s += f'<text x="{x + w / 2:.0f}" y="34" text-anchor="middle" class="pt" fill="{GO if k < 3 else GO}">{lbl}</text>'
        x += w
        if k < 3:
            s += f'<text x="{x + 9}" y="{46 + 33}" text-anchor="middle" class="pt" fill="#C9D3DB">{"·" if k < 2 else "="}</text>'
            x += 18
    s += f'<text x="235" y="132" text-anchor="middle" class="ax">multiply left to right, port 1 to port 2</text>'
    chips = [chip('left', 300, 'g', '1st: series 2 Ω'), chip('left', 364, 'g', '2nd: shunt 0.25 S'), chip('left', 428, 'g', '3rd: series 3 Ω'),
             chip('right', 252, 'c', f'Z<sub>in</sub> = {Zin:.4f} Ω'), chip('right', 536, 'c', f'V₂/V₁ = {gain:.4f}', False)]
    summ = (f'T₁·T₂·T₃, <b class="gl">port 1 to port 2</b>: [1.5 6.5; 0.25 1.75]<br>'
            f'With 10 Ω: Z<sub>in</sub> = 21.5 ÷ 4.25 = <b class="cl">{Zin:.4f} Ω</b>, AD − BC = 1')
    return spec('u6-L2', 'Hybrid &amp;<br>Transmission<br>Parameters', 'Which order to multiply ABCD?',
                'Multiply in <span class="gold">ORDER</span>, from<br>port 1 to port <span class="cyan">2</span>',
                'three blocks in cascade', svg(s), bd, chips, summ, 'Hybrid &amp; Transmission Parameters')


# ================================================================ u6 L3: chapter 6.6, worked example 1 (two T networks in series)
def u6_L3():
    Za = tnet(2, 3, 4); Zs = [[Za[i][j] * 2 for j in range(2)] for i in range(2)]
    zb_lead = 4 + 2 * 3 / 5; Zwrong = [[Za[i][j] + zb_lead for j in range(2)] for i in range(2)]
    assert Zs == [[12, 8], [8, 14]]; near(zb_lead, 5.2); near(Zwrong[0][0], 11.2); near(Zwrong[0][1], 9.2); near(Zwrong[1][1], 12.2)
    near(2 + 4 + 4 + 2, Zs[0][0])
    setup(306)
    parts = []
    def tsym(yb, flip):
        """a T drawn on a module's top face: two series arms along x, the shunt arm towards the common side"""
        z = .56
        ys, yc = (yb + .45, yb + 1.15) if not flip else (yb + 1.15, yb + .45)
        return (wire([(2.4, ys), (5.6, ys)], '#E6ECF1', 3, z=z) + wire([(4.0, ys), (4.0, yc)], '#E6ECF1', 3, z=z)
                + res(3.1, ys, 'x', '', L=.8, w=.3, h=.25).replace('<polygon', '<polygon transform="translate(0 -18)"')
                + res(4.9, ys, 'x', '', L=.8, w=.3, h=.25).replace('<polygon', '<polygon transform="translate(0 -18)"'))
    parts += [wire([(1.6, 2.3), (2.2, 2.3)]), wire([(5.8, 2.3), (7.2, 2.3)]), wire([(1.6, 5.8), (2.2, 5.8)]), wire([(5.8, 5.8), (7.2, 5.8)])]
    parts.append(glow([(4.0, 3.4), (4.0, 4.6)], GO, 6, arrows=False))
    parts.append(B.box(2.1, 1.8, 3.8, 1.6, .55, '#3A4A5C', '#1E2832', '#2A3642')); parts.append(tsym(1.8, False))
    parts.append(B.box(2.1, 4.6, 3.8, 1.6, .55, '#3A4A5C', '#1E2832', '#2A3642')); parts.append(tsym(4.6, True))
    parts += [lab(4.0, 1.5, 1.0, 'a', '#E6ECF1', 20), lab(4.0, 4.3, 1.3, 'b, turned over', GO, 16)]
    parts += [post(1.6, 2.3, '1', h=22), post(1.6, 5.8, "1′", h=22), post(7.2, 2.3, '2', h=22), post(7.2, 5.8, "2′", h=22)]
    bd = board(parts)
    s, x = '', 4
    for k, (mtx, col) in enumerate(((Za, '#E6ECF1'), (Za, '#E6ECF1'), (Zs, GO))):
        mm, w = matrix(x, 26, [[g(v) for v in r] for r in mtx], col, cw=38, rh=24)
        s += mm; x += w
        if k < 2:
            s += f'<text x="{x + 12}" y="{26 + 33}" text-anchor="middle" class="pt" fill="#C9D3DB">{"+" if k == 0 else "="}</text>'; x += 24
    s += f'<text x="{x + 8}" y="62" class="pt" fill="{GO}">Ω, b flipped</text>'
    mm, w = matrix(190, 88, [[g(v) for v in r] for r in Zwrong], '#9FB2C6', cw=44, rh=24, size=15)
    s += f'<text x="180" y="122" text-anchor="end" class="ax" fill="#9FB2C6">not flipped, rule fails:</text>' + mm
    s += f'<text x="{190 + w + 8}" y="122" class="ax" fill="#9FB2C6">Ω</text>'
    s = s.replace('<text x="4"', '<text x="4"')
    chips = [chip('left', 300, 'c', '[Z<sub>a</sub>] = [6 4; 4 7] Ω'), chip('left', 364, 'c', '[Z<sub>b</sub>] = [6 4; 4 7] Ω'), chip('left', 428, 'g', 'b turned over'),
             chip('right', 252, 'g', '[Z] = [12 8; 8 14] Ω'), chip('right', 536, 'c', 'not flipped: 11.2, 9.2', False)]
    summ = (f'Series: [Z<sub>a</sub>] + [Z<sub>b</sub>] = <b class="gl">[12 8; 8 14] Ω</b><br>'
            f'b not turned over: <b class="cl">[11.2 9.2; 9.2 12.2] Ω</b>, wrong')
    return spec('u6-L3', 'Converting &amp;<br>Connecting<br>Two-ports', 'Cascade: add or multiply ABCD?',
                'Series <span class="gold">ADDS</span> Z; a cascade<br><span class="cyan">MULTIPLIES</span> ABCD',
                'two T networks in series', svg(s), bd, chips, summ, 'Converting &amp; Connecting Two-ports')


# ================================================================ u6 L4: chapter 6.7, worked examples 1 and 2 (reciprocity)
def u6_L4():
    Z = tnet(2, 3, 4)
    # with a CCVS 2 I1 in the shunt arm: Vc = 4(I1 + I2) + 2 I1
    Zd = [[2 + 4 + 2, 4], [4 + 2, 3 + 4]]
    abcd = lambda z: (z[0][0] / z[1][0], (z[0][0] * z[1][1] - z[0][1] * z[1][0]) / z[1][0], 1 / z[1][0], z[1][1] / z[1][0])
    def det(z):
        A, B_, C_, D = abcd(z); return A * D - B_ * C_
    assert Zd == [[8, 4], [6, 7]] and Z == [[6, 4], [4, 7]]
    near(det(Z), 1); near(det(Zd), .667, .01); near(abcd(Z)[0], 1.5); near(abcd(Z)[3], 1.75)
    near(Zd[0][1] / Zd[1][1], .571, .01); near(Zd[1][0] / Zd[1][1], .857, .01)
    setup(306)
    sh = [res(4.2, 3.5, 'y', '4 Ω', L=1.3, ldy=-.2, lz=1.2), isrc(4.2, 5.2, '2I₁', w=1.1, d=1.1, h=.85, diamond=True)]
    parts = t_board(sh, shunt_glow=[(4.2, 2.0), (4.2, 6.4)])
    bd = board(parts)
    rows = [('z₁₂', g(Z[0][1]), g(Zd[0][1])), ('z₂₁', g(Z[1][0]), g(Zd[1][0])), ('AD − BC', g(det(Z)), f'{det(Zd):.3f}'),
            ('z₁₁ vs z₂₂', '6 ≠ 7', '8 ≠ 7'), ('reciprocal?', 'yes', 'no')]
    s = (f'<text x="250" y="18" text-anchor="middle" class="pt" fill="#C9D3DB">plain T</text>'
         f'<text x="400" y="18" text-anchor="middle" class="pt" fill="{GO}">with 2I₁</text>')
    for k, (a_, b_, c_) in enumerate(rows):
        y = 42 + k * 23
        hl = k in (0, 1)
        s += (f'<text x="20" y="{y}" class="pt" fill="#E6ECF1">{a_}</text>'
              f'<text x="250" y="{y}" text-anchor="middle" class="pt" fill="{CY}">{b_}</text>'
              f'<text x="400" y="{y}" text-anchor="middle" class="pt" fill="{GO if hl or k > 1 else "#E6ECF1"}">{c_}</text>')
        if k < 4:
            s += f'<line x1="16" y1="{y + 7}" x2="460" y2="{y + 7}" stroke="#3A4A58" stroke-width="1"/>'
    chips = [chip('left', 300, 'c', f'plain T: z₁₂ = z₂₁ = {Z[0][1]} Ω'), chip('left', 364, 'g', '2I₁ in the shunt arm'), chip('left', 428, 'g', f'z₁₂ = {Zd[0][1]}, z₂₁ = {Zd[1][0]} Ω'),
             chip('right', 252, 'g', f'AD − BC = {det(Zd):.3f}'), chip('right', 536, 'c', 'not symmetric: 8 ≠ 7', False)]
    summ = (f'Reciprocal when <b class="gl">z₁₂ = z₂₁</b> (AD − BC = 1, h₁₂ = −h₂₁)<br>'
            f'With 2I₁: z₁₂ = {Zd[0][1]} ≠ z₂₁ = {Zd[1][0]}, so <b class="cl">not reciprocal</b>')
    return spec('u6-L4', 'Reciprocity,<br>Symmetry &amp;<br>Synthesis', 'Which test means reciprocal?',
                '<span class="gold">z₁₂ = z₂₁</span> means reciprocal;<br>a dependent source can <span class="cyan">BREAK</span> it',
                'T network, then 2I₁ added', svg(s), bd, chips, summ, 'Reciprocity, Symmetry &amp; Synthesis')


def specs():
    return [f() for f in (u1_L1, u1_L2, u1_L3, u1_L4, u2_L1, u2_L2, u2_L3, u2_L4, u3_L1, u3_L2, u3_L3, u3_L4,
                          u4_L1, u4_L2, u4_L3, u5_L1, u5_L2, u5_L3, u6_L1, u6_L2, u6_L3, u6_L4)]
