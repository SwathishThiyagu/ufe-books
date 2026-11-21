"""Claude's hand-drawn figures for ec-optical-u6 (WDM, amplifiers and optical networks), one per chapter.
Every number comes from that chapter's own worked example. Colours are only the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def arrow(x1, y1, x2, y2, c=AC, w=2, key='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, key)


# ---- 6.1 forty channels on one fiber, and the comb in the C-band ----
def fig1():
    o = []
    # top: the link
    o.append(T(20, 30, '40 channels × 10 Gb/s share one fiber', 15, 'start', INK, True))
    xs = [(20, 120, ['40 lasers', 'λ1 … λ40']), (175, 90, ['MUX']), (300, 170, ['one single-mode', 'fiber: 400 Gb/s']), (505, 90, ['DEMUX']), (630, 80, ['40', 'receivers'])]
    for i, (x, w, lab) in enumerate(xs):
        fill = ACS if lab[0] in ('MUX', 'DEMUX') else (LVS if 'fiber' in lab[1] else PANEL)
        o.append(boxt(x, 50, w, 58, lab, fill, AC if fill != LVS else LV, 14))
    for (x, w, _), (x2, _, _) in zip(xs, xs[1:]):
        o.append(arrow(x + w + 2, 79, x2 - 4, 79, L2, 2, 'm'))
    # bottom: comb on a frequency axis
    f0, f1 = 191.5, 196.3
    X = lambda f: 60 + (f - f0) * 125
    yb = 330
    o.append(T(20, 150, 'The comb: 40 channels 100 GHz apart', 15, 'start', INK, True))
    fa, fb = 3e8 / 1565e-9 / 1e12, 3e8 / 1530e-9 / 1e12
    o.append(R(X(fa), 170, X(fb) - X(fa), yb - 170, ACS, ACS, 0, 0))
    o.append(T(X(fa) + 6, 190, 'C-band (1530 to 1565 nm): 4.385 THz, room for 43 slots', 13, 'start', AC))
    chans = [192.1 + 0.1 * i for i in range(40)]
    for i, f in enumerate(chans):
        hh = 62 if i in (0, 1, 39) else 52
        o.append(L(X(f), yb, X(f), yb - hh, NX if i in (0, 1) else LV, 3 if i in (0, 1, 39) else 2))
    o.append(T(X(chans[0]) - 4, yb - 68, 'λ1', 13, 'end', NX))
    o.append(T(X(chans[1]) + 4, yb - 68, 'λ2', 13, 'start', NX))
    o.append(T(X(chans[39]) - 4, yb - 68, 'λ40', 13, 'end', LV))
    o.append(xaxis(50, 700, yb, [192, 193, 194, 195, 196], X, None, lambda v: str(v)))
    o.append(T(700, yb + 64, 'optical frequency (THz); wavelength gets longer to the left', 13, 'end', MUT))
    # spacing call-out between λ1 and λ2
    o.append(L(X(chans[0]), yb + 40, X(chans[1]), yb + 40, NX, 1.5))
    o.append(L(X(chans[0]), yb + 34, X(chans[0]), yb + 46, NX, 1.5) + L(X(chans[1]), yb + 34, X(chans[1]), yb + 46, NX, 1.5))
    o.append(T(X(chans[1]) + 10, yb + 45, 'Δf = 100 GHz = 0.80 nm at 1550 nm', 13, 'start', NX))
    # comb width bracket above the lines
    o.append(brace(X(chans[0]), X(chans[39]), 226, LV))
    o.append(Tb((X(chans[0]) + X(chans[39])) / 2, 222, 'λ1 to λ40: 39 gaps = 3.9 THz = 31.2 nm', 13, 'middle', LV))
    return 410, ''.join(o)
FIG[1] = (fig1, 'Forty 10 Gb/s channels, 100 GHz (0.80 nm) apart, are combined on one fiber for 400 Gb/s. From λ1 to λ40 the comb spans 39 gaps, 3.9 THz or 31.2 nm, and it fits inside the 4.385 THz erbium C-band, which has room for 43 such slots.',
          'Top: 40 lasers feed a multiplexer, one fiber carrying 400 Gb/s, a demultiplexer and 40 receivers. Bottom: 40 thin lines on a frequency axis from 192 to 196 THz inside a shaded C-band, with the first gap marked 100 GHz and a bracket over the whole comb marked 3.9 THz.')


# ---- 6.2 coupler numbers and the two-circulator add-drop node ----
def circulator(cx, cy, name, ports):
    o = [f'<circle cx="{cx}" cy="{cy}" r="34" style="fill:{PANEL};stroke:{AC};stroke-width:2"/>',
         f'<path d="M{cx - 16},{cy - 12} A20,20 0 1 1 {cx - 16},{cy + 12}" style="fill:none;stroke:{AC};stroke-width:1.8" marker-end="url(#ar-UID-n)"/>',
         T(cx + 2, cy + 5, name, 14, 'middle', INK, True)]
    for (px, py, lab, anc) in ports:
        o.append(T(px, py, lab, 13, anc, MUT))
    return ''.join(o)


def fig2():
    o = []
    o.append(T(20, 28, 'A 2×2 fused coupler (worked example)', 15, 'start', INK, True))
    # two fibers that come together in the fused region
    y1, y2, ym = 70, 160, 115
    o.append(P([(140, y1), (270, ym - 9), (430, ym - 9), (560, y1)], AC, 3))
    o.append(P([(140, y2), (270, ym + 9), (430, ym + 9), (560, y2)], AC, 3))
    o.append(R(270, ym - 22, 160, 44, ACS, AC, 20, 1.5, '4 3'))
    o.append(T(350, ym + 5, 'fused taper', 13, 'middle', AC))
    o.append(T(130, y1 + 5, 'port 1: 250 µW in', 13, 'end', INK, True))
    o.append(T(130, y2 + 5, 'port 2: 4.0 nW back', 13, 'end', LV))
    o.append(T(570, y1 + 5, 'port 3: 118 µW', 13, 'start', INK))
    o.append(T(570, y2 + 5, 'port 4: 112 µW', 13, 'start', INK))
    o.append(T(360, 200, 'CR = 118/230 = 51.3 %  ·  excess loss 0.36 dB  ·  directivity 47.96 dB', 13, 'middle', MUT))
    # add-drop node
    o.append(L(20, 225, 700, 225, LN, 1))
    o.append(T(20, 258, 'Two circulators and a Bragg grating: an add-drop node', 15, 'start', INK, True))
    c1, c2, cy = (190, 360), (530, 360), 360
    o.append(circulator(c1[0], cy, 'C1', [(c1[0] - 44, cy - 8, '1', 'end'), (c1[0] + 44, cy - 8, '2', 'start'), (c1[0] + 8, cy + 54, '3', 'start')]))
    o.append(circulator(c2[0], cy, 'C2', [(c2[0] - 44, cy - 8, '2', 'end'), (c2[0] + 44, cy - 8, '3', 'start'), (c2[0] - 8, cy + 54, '1', 'end')]))
    # grating between the circulators
    gx0, gx1 = 290, 430
    o.append(L(c1[0] + 34, cy, gx0, cy, AC, 2.5) + L(gx1, cy, c2[0] - 34, cy, AC, 2.5))
    o.append(R(gx0, cy - 14, gx1 - gx0, 28, PANEL, LV, 3, 1.5))
    for i in range(14):
        x = gx0 + 6 + i * 9.5
        o.append(L(x, cy - 12, x, cy + 12, LV, 3))
    o.append(T((gx0 + gx1) / 2, cy - 24, 'FBG, Λ = 534.5 nm', 13, 'middle', LV, True))
    o.append(T((gx0 + gx1) / 2, cy + 34, 'reflects λ2 = 1550 nm', 13, 'middle', LV))
    # input and output lines
    o.append(arrow(30, cy, c1[0] - 38, cy, AC, 2.5))
    o.append(T(30, cy - 12, 'in: λ1 λ2 λ3 λ4', 13, 'start', INK))
    o.append(arrow(c2[0] + 38, cy, 700, cy, AC, 2.5))
    o.append(T(700, cy - 12, 'out: λ1 λ2′ λ3 λ4', 13, 'end', INK))
    # through and reflected labels
    o.append(arrow(gx1 + 8, cy - 46, c2[0] - 46, cy - 46, AC, 1.8))
    o.append(T((gx1 + c2[0]) / 2 - 10, cy - 54, 'λ1 λ3 λ4', 13, 'middle', AC))
    o.append(arrow(gx0 - 8, cy + 46, c1[0] + 40, cy + 46, LV, 1.8))
    o.append(T((gx0 + c1[0]) / 2 + 20, cy + 64, 'λ2 back', 13, 'middle', LV))
    # drop and add
    o.append(arrow(c1[0], cy + 36, c1[0], 470, NX, 2.5, 'x'))
    o.append(T(c1[0] + 10, 486, 'drop λ2 (port 3)', 13, 'start', NX, True))
    o.append(arrow(c2[0], 470, c2[0], cy + 38, NX, 2.5, 'x'))
    o.append(T(c2[0] - 10, 486, 'add new λ2′ (port 1)', 13, 'end', NX, True))
    o.append(T(360, 512, 'the added λ2′ leaves C2 at port 2, is reflected by the grating and leaves at port 3', 13, 'middle', MUT))
    return 528, ''.join(o)
FIG[2] = (fig2, 'Top: the worked example’s coupler, with 250 µW in, 118 µW and 112 µW out and 4.0 nW back at port 2. Bottom: a grating of pitch 534.5 nm reflects λ2 = 1550 nm, so C1 drops λ2 at its port 3, the other channels pass to C2, and a new λ2 added at C2 port 1 is reflected by the grating and joins them at C2 port 3.',
          'Top: two fibers merging in a fused taper with port powers labelled. Bottom: an input line into circulator C1, a striped grating, circulator C2 and the output line; λ2 is dropped below C1 and a new λ2 is added below C2.')


# ---- 6.3 EDFA parts with the worked example's powers, and the erbium levels ----
def fig3():
    o = []
    o.append(T(20, 28, 'EDFA: parts in signal order', 15, 'start', INK, True))
    y = 100
    parts = [(20, 82, ['signal in', '0.5 mW']), (124, 82, ['isolator']), (228, 92, ['WDM', 'coupler']), (342, 130, ['erbium-doped', 'fiber, 10–30 m']), (494, 82, ['isolator']), (598, 102, ['gain-flat', 'filter'])]
    for x, w, lab in parts:
        fill = LVS if 'erbium' in lab[0] else (PANEL if 'signal' not in lab[0] else FIGBG)
        o.append(boxt(x, y - 26, w, 52, lab, fill, LV if 'erbium' in lab[0] else AC, 13))
    for (x, w, _), (x2, _, _) in zip(parts, parts[1:]):
        o.append(arrow(x + w + 1, y, x2 - 4, y, AC, 2))
    o.append(boxt(206, 180, 136, 48, ['pump laser', '980 nm, 60 mW'], NXS, NX, 13))
    o.append(arrow(274, 178, 274, y + 30, NX, 2, 'x'))
    o.append(arrow(649, y + 28, 649, 168, AC, 2))
    o.append(T(649, 186, 'out: 25 mW', 13, 'middle', INK, True))
    o.append(T(649, 204, 'gain 16.99 dB', 13, 'middle', MUT))
    o.append(T(430, 162, 'isolators stop reflections and', 13, 'middle', MUT))
    o.append(T(430, 180, 'backward ASE from causing lasing', 13, 'middle', MUT))
    o.append(T(500, 222, 'PCE = (25 − 0.5)/60 = 40.8 %', 13, 'middle', MUT))
    # energy levels
    o.append(L(20, 240, 700, 240, LN, 1))
    o.append(T(20, 270, 'Erbium energy levels', 15, 'start', INK, True))
    lx0, lx1 = 140, 520
    y1, y2, y3 = 450, 340, 300
    o.append(L(lx0, y1, lx1, y1, INK, 3) + T(lx0 - 10, y1 + 5, 'level 1 (ground)', 13, 'end', INK))
    o.append(L(lx0, y2, lx1, y2, INK, 3) + T(lx0 - 10, y2 + 5, 'level 2, ~10 ms', 13, 'end', INK))
    o.append(L(lx0, y3, lx1, y3, INK, 3) + T(lx0 - 10, y3 + 5, 'level 3', 13, 'end', INK))
    o.append(R(lx0, y2 - 14, lx1 - lx0, 14, LVS, LVS, 0, 0))
    o.append(arrow(190, y1, 190, y3 + 4, NX, 3, 'x') + T(198, 400, '980 nm pump', 13, 'start', NX))
    o.append(arrow(300, y1, 300, y2 - 10, NX, 3, 'x') + T(308, 420, '1480 nm pump', 13, 'start', NX))
    o.append(L(235, y3, 235, y2 - 2, MUT, 2, '4 3', 'm') + T(232, y3 - 8, 'fast decay', 13, 'middle', MUT))
    o.append(arrow(430, y2, 430, y1 - 4, LV, 3, 'l') + arrow(460, y2, 460, y1 - 4, LV, 3, 'l'))
    o.append(T(472, 392, 'stimulated emission:', 13, 'start', LV))
    o.append(T(472, 410, 'signal 1530–1565 nm', 13, 'start', LV))
    o.append(T(472, 428, 'copied photon by photon', 13, 'start', LV))
    return 470, ''.join(o)
FIG[3] = (fig3, 'Top: a 0.5 mW signal passes an isolator, joins a 60 mW 980 nm pump in the WDM coupler, is amplified in the doped fiber and leaves through a second isolator and the gain-flattening filter at 25 mW, a gain of 16.99 dB and a PCE of 40.8 percent. Bottom: the 980 nm pump lifts ions to level 3, they fall quickly to the long-lived level 2, and the signal stimulates the 2 → 1 transition.',
          'Top: a row of blocks from signal in, isolator, WDM coupler with a pump laser below it, erbium-doped fiber, isolator and filter, to 25 mW out. Bottom: three horizontal energy levels with upward pump arrows at 980 and 1480 nm, a dashed decay from level 3 to level 2 and downward signal arrows from level 2 to level 1.')


# ---- 6.4 SPM chirp on a sech pulse, and width against distance ----
SECH = [(0, 1.0), (2.5, 1.222), (5, 1.539), (7.5, 1.846), (10, 2.144), (12.5, 2.436), (15, 2.725), (17.5, 3.012), (20, 3.299)]


def fig4():
    o = []
    # top: intensity and frequency shift of a sech pulse, T0 = 10 ps
    o.append(T(20, 26, 'SPM: the phase follows the power, so the pulse chirps itself', 15, 'start', INK, True))
    x0, x1, yb = 70, 680, 190
    X = lambda t: (x0 + x1) / 2 + t * (x1 - x0) / 80.0
    o.append(xaxis(x0, x1, yb, [-30, -20, -10, 0, 10, 20, 30], X, None, lambda v: neg(v)))
    o.append(T(x1, yb + 38, 'time T in the pulse frame (ps); the leading edge is on the left', 13, 'end', MUT))
    ts = [i * 0.5 for i in range(-80, 81)]
    pw = [(X(t), yb - 120 / math.cosh(t / 10) ** 2) for t in ts]
    o.append(P(pw, AC, 2.5))
    # frequency shift  -dP/dT, scaled; zero line at yz
    yz = 120
    def dw(t):
        s = 1 / math.cosh(t / 10)
        return 2 * s * s * math.tanh(t / 10) / 10   # -dP/dT for P = sech^2(T/T0)
    m = max(dw(t) for t in ts)
    pf = [(X(t), yz - 55 * dw(t) / m) for t in ts]
    o.append(L(x0, yz, x1, yz, L2, 1.2, '5 4'))
    o.append(P(pf, LV, 2.2))
    o.append(T(X(0) + 8, yb - 126, 'power P(T)', 13, 'start', AC))
    o.append(T(X(-26), yz + 30, 'δω < 0: red shift', 13, 'middle', LV, True))
    o.append(T(X(26), yz - 32, 'δω > 0: blue shift', 13, 'middle', LV, True))
    o.append(T(x0 + 2, yz - 8, 'δω = 0', 13, 'start', MUT))
    # bottom: width / initial width against z
    o.append(L(20, 250, 700, 250, LN, 1))
    o.append(T(20, 278, 'Width against distance: T₀ = 10 ps, β₂ = −20 ps²/km, L_D = 5 km'.replace('L_D', 'L<tspan baseline-shift="sub" font-size="11">D</tspan>'), 15, 'start', INK, True))
    gx0, gx1, gy0, gy1 = 90, 680, 324, 510
    Z = lambda z: gx0 + z * (gx1 - gx0) / 20
    Y = lambda r: gy1 - (r - 0) * (gy1 - gy0) / 3.5
    o.append(axes(gx0, gx1, gy0, gy1, [0, 5, 10, 15, 20], [0, 1, 2, 3], Z, Y, 'distance z (km)', 'FWHM ÷ 17.6 ps'))
    o.append(P([(Z(z), Y(r)) for z, r in SECH], AC, 2.5))
    o.append(L(Z(0), Y(1), Z(20), Y(1), NX, 3))
    o.append(T(Z(13), Y(1) - 10, 'soliton, P₀ = 100 mW: stays at 1', 13, 'start', NX, True))
    o.append(T(Z(15.2), Y(2.725) - 18, 'no nonlinearity', 13, 'end', AC, True))
    for z, r in ((5, 1.539), (10, 2.144)):
        o.append(C(Z(z), Y(r), 5, AC))
        o.append(Tb(Z(z) - 10, Y(r) - 12, f'{r:.2f}', 13, 'end', AC))
    return 560, ''.join(o)
FIG[4] = (fig4, 'Top: across a sech pulse the SPM frequency shift is red on the rising (leading) edge and blue on the falling (trailing) edge. Bottom: with only dispersion the worked example’s 17.6 ps pulse is 1.54 times wider at L<sub>D</sub> = 5 km and 2.14 times at 10 km; at the soliton power of 100 mW it keeps its width.',
          'Top: a bell-shaped power curve over time from minus 30 to 30 ps with a frequency-shift curve that dips below zero on the left and rises above zero on the right. Bottom: a plot of width ratio against distance from 0 to 20 km, a rising curve through 1.54 at 5 km and 2.14 at 10 km, and a flat line at 1 for the soliton.')


# ---- 6.5 physical ring and logical mesh of the worked example ----
NODES = 'ABCDEF'
LAMS = {'A–D': 1, 'A–E': 1, 'D–E': 1, 'B–D': 2, 'B–E': 2, 'A–C': 3, 'A–F': 3, 'C–F': 3, 'B–C': 4, 'B–F': 4, 'C–E': 4, 'E–F': 4, 'A–B': 5, 'C–D': 5, 'D–F': 5}
LCOL = {1: AC, 2: LV, 3: NX, 4: INK, 5: MUT}
LDASH = {1: None, 2: None, 3: None, 4: '6 4', 5: '2 3'}


def fig5():
    o = []
    def pos(cx, cy, r, i):
        a = math.radians(-90 + 60 * i)
        return cx + r * math.cos(a), cy + r * math.sin(a)
    # left: physical ring with link loads
    cx, cy, r = 170, 230, 120
    o.append(T(cx, 36, 'Physical: 6 fiber links', 15, 'middle', INK, True))
    loads = {'AB': 5, 'BC': 4, 'CD': 5, 'DE': 4, 'EF': 5, 'FA': 4}
    for i in range(6):
        p, q = pos(cx, cy, r, i), pos(cx, cy, r, (i + 1) % 6)
        o.append(L(p[0], p[1], q[0], q[1], AC, 4))
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        ox, oy = mx + (mx - cx) * 0.28, my + (my - cy) * 0.28
        key = NODES[i] + NODES[(i + 1) % 6]
        o.append(T(ox, oy + 5, str(loads[key]), 14, 'middle', LV, True))
    for i in range(6):
        x, y = pos(cx, cy, r, i)
        o.append(state(x, y, NODES[i], r=20))
    o.append(T(cx, 400, 'numbers: lightpaths on each link', 13, 'middle', LV))
    o.append(T(cx, 418, 'busiest link carries 5', 13, 'middle', MUT))
    # right: logical mesh, coloured by wavelength
    cx2 = 520
    o.append(T(cx2, 36, 'Logical: 15 lightpaths', 15, 'middle', INK, True))
    P2 = {NODES[i]: pos(cx2, cy, r, i) for i in range(6)}
    for k, lam in LAMS.items():
        a, b = k.split('–')
        (x1, y1), (x2, y2) = P2[a], P2[b]
        o.append(L(x1, y1, x2, y2, LCOL[lam], 2.4, LDASH[lam]))
    for n, (x, y) in P2.items():
        o.append(state(x, y, n, r=20))
    # legend
    lx, ly = 400, 392
    for j in range(1, 6):
        xx = lx + (j - 1) * 64
        o.append(L(xx, ly, xx + 24, ly, LCOL[j], 3, LDASH[j]) + T(xx + 28, ly + 5, f'λ{j}', 13, 'start', INK))
    o.append(T(cx2, 422, 'shortest routes: 5 wavelengths, not 15', 13, 'middle', MUT))
    return 440, ''.join(o)
FIG[5] = (fig5, 'Left: the worked example’s six nodes joined by a ring of six fiber links; the numbers are the lightpaths each link carries on shortest routes. Right: the same nodes as the routers see them, a full mesh of 15 lightpaths, coloured by the five wavelengths that are enough when wavelengths are reused.',
          'Left: a hexagon ring of nodes A to F with each side labelled 5 or 4. Right: the same six nodes with all 15 connecting lines drawn in five line styles, and a legend for λ1 to λ5.')


# ---- 6.6 the STS-1 frame ----
def fig6():
    o = []
    o.append(T(20, 28, 'STS-1 frame: 90 columns × 9 rows = 810 bytes every 125 µs', 15, 'start', INK, True))
    x0, top, rh = 80, 70, 30
    toh, poh = 84, 28             # 3 columns and 1 column, drawn wider than scale so labels fit
    xe = 690
    # transport overhead: section (rows 1-3) and line (rows 4-9)
    o.append(R(x0, top, toh, 3 * rh, ACS, AC, 0, 1.5))
    o.append(R(x0, top + 3 * rh, toh, 6 * rh, NXS, NX, 0, 1.5))
    o.append(T(x0 + toh / 2, top + 1.5 * rh - 4, 'section', 13, 'middle', AC, True))
    o.append(T(x0 + toh / 2, top + 1.5 * rh + 13, 'overhead', 13, 'middle', AC))
    o.append(T(x0 + toh / 2, top + 6.5 * rh - 4, 'line', 13, 'middle', NX, True))
    o.append(T(x0 + toh / 2, top + 6.5 * rh + 13, 'overhead', 13, 'middle', NX))
    # H1 H2 H3 in row 4
    for j, hname in enumerate(['H1', 'H2', 'H3']):
        o.append(R(x0 + j * 28, top + 3 * rh, 28, rh, LVS, LV, 0, 1.5))
        o.append(T(x0 + j * 28 + 14, top + 3 * rh + 20, hname, 13, 'middle', LV, True))
    # SPE: path overhead column and payload
    sx = x0 + toh
    o.append(R(sx, top, poh, 9 * rh, LVS, LV, 0, 1.5))
    for i, ch in enumerate('POH'):
        o.append(T(sx + poh / 2, top + 3.5 * rh + i * 22, ch, 13, 'middle', LV, True))
    o.append(R(sx + poh, top, xe - sx - poh, 9 * rh, PANEL, L2, 0, 1.5))
    for i in range(1, 9):
        o.append(L(sx + poh, top + i * rh, xe, top + i * rh, LN, 1))
    o.append(T((sx + poh + xe) / 2, top + 4.5 * rh - 6, 'payload: 86 columns', 14, 'middle', INK, True))
    o.append(T((sx + poh + xe) / 2, top + 4.5 * rh + 14, '(including 2 columns of fixed stuff)', 13, 'middle', MUT))
    # row numbers
    for i in range(9):
        o.append(T(x0 - 10, top + i * rh + 20, str(i + 1), 13, 'end', MUT))
    o.append(T(x0 - 54, top + 4.5 * rh + 5, '9 rows', 13, 'middle', MUT))
    # column braces
    yb = top + 9 * rh + 14
    o.append(brace(x0, x0 + toh, yb, AC))
    o.append(T(x0 + toh / 2, yb + 26, '3 columns', 13, 'middle', AC))
    o.append(T(x0 + toh / 2, yb + 44, '27 bytes', 13, 'middle', AC))
    o.append(brace(sx, xe, yb, LV))
    o.append(T((sx + xe) / 2, yb + 26, 'SPE: 87 columns × 9 rows = 783 bytes, 50.112 Mb/s', 13, 'middle', LV, True))
    o.append(T((sx + xe) / 2, yb + 44, 'its first column is the path overhead', 13, 'middle', MUT))
    o.append(T(360, yb + 80, '810 bytes × 8 bits × 8000 frames per second = 51.84 Mb/s; sent row by row, left to right', 13, 'middle', INK))
    o.append(T(360, 58, 'column widths not to scale', 13, 'middle', MUT))
    return yb + 100, ''.join(o)
FIG[6] = (fig6, 'The STS-1 frame of the worked example: 3 columns of transport overhead (section overhead in rows 1 to 3, line overhead in rows 4 to 9 with the pointer bytes H1, H2, H3 in row 4) and an 87-column SPE that starts with the path overhead column. 810 bytes 8000 times a second give 51.84 Mb/s.',
          'A wide rectangle of 9 rows. On the left a narrow block split into section overhead above and line overhead below, with H1, H2, H3 marked in row 4; then a one-column path overhead strip, then a wide payload area. Braces below mark 3 columns and the 87-column SPE.')


# ---- 6.7 free wavelengths per link, and the path with one converter ----
def fig7():
    o = []
    o.append(T(20, 28, 'Free wavelengths on each link of A–B–C–D', 15, 'start', INK, True))
    free = {'A–B': {1, 2}, 'B–C': {2, 3}, 'C–D': {1, 3}}
    cols = list(free)
    gx, gy, cw, rh = 170, 56, 150, 34
    for j, ln in enumerate(cols):
        o.append(T(gx + j * cw + cw / 2, gy + 14, ln, 14, 'middle', INK, True))
    for i in range(1, 4):
        y = gy + 26 + (i - 1) * rh
        o.append(T(gx - 20, y + 22, f'λ{i}', 14, 'end', INK, True))
        for j, ln in enumerate(cols):
            ok = i in free[ln]
            o.append(R(gx + j * cw + 8, y + 4, cw - 16, rh - 8, NXS if ok else PANEL, NX if ok else L2, 5, 1.5, None if ok else '4 3'))
            o.append(T(gx + j * cw + cw / 2, y + 22, 'free' if ok else 'busy', 13, 'middle', NX if ok else MUT))
    o.append(T(gx + 1.5 * cw, gy + 26 + 3 * rh + 22, 'no row is free in all three columns: blocked without a converter', 13, 'middle', LV, True))
    # bottom: the path
    yp = 300
    xs = {'A': 80, 'B': 280, 'C': 480, 'D': 650}
    o.append(L(xs['A'], yp, xs['B'], yp, LV, 4))
    o.append(L(xs['B'], yp, xs['C'], yp, AC, 4) + L(xs['C'], yp, xs['D'], yp, AC, 4))
    o.append(T((xs['A'] + xs['B']) / 2, yp - 14, 'λ2', 14, 'middle', LV, True))
    o.append(T((xs['B'] + xs['C']) / 2, yp - 14, 'λ3', 14, 'middle', AC, True))
    o.append(T((xs['C'] + xs['D']) / 2, yp - 14, 'λ3', 14, 'middle', AC, True))
    for n, x in xs.items():
        if n == 'B':
            o.append(R(x - 26, yp - 24, 52, 48, ACS, AC, 8, 2.5) + T(x, yp + 6, 'B', 15, 'middle', INK, True))
        else:
            o.append(state(x, yp, n, r=22))
    o.append(T(xs['B'], yp + 48, 'converter at B: λ2 → λ3', 13, 'middle', AC, True))
    o.append(T(360, yp + 82, 'A–B uses λ2; B–C–D uses λ3, the one wavelength free on both B–C and C–D', 13, 'middle', MUT))
    return yp + 100, ''.join(o)
FIG[7] = (fig7, 'Top: the worked example’s free wavelengths; every link has two free, but no single wavelength is free on all three links, so the lightpath is blocked without conversion. Bottom: with a converter at B the path uses λ2 on A–B and λ3 on B–C and C–D.',
          'Top: a 3 by 3 grid of wavelengths λ1 to λ3 against links A–B, B–C and C–D, each cell marked free or busy. Bottom: nodes A, B, C, D in a line; the A–B link is labelled λ2, the B–C and C–D links λ3, and node B is a square marked as the converter.')


# ---- 6.8 AAL5 segmentation of a 1500-byte packet ----
def fig8():
    o = []
    o.append(T(20, 28, 'AAL5: 1500-byte IP packet into ATM cells', 15, 'start', INK, True))
    x0, x1 = 40, 680
    xp, xt = 500, 610          # pad and trailer drawn wider than scale so they can be read
    y = 60
    o.append(R(x0, y, xp - x0, 40, ACS, AC, 4, 2))
    o.append(T((x0 + xp) / 2, y + 25, 'IP packet 1500 B', 14, 'middle', INK, True))
    o.append(R(xp, y, xt - xp, 40, PANEL, MUT, 0, 1.5, '3 2'))
    o.append(T((xp + xt) / 2, y + 25, 'pad 28 B', 13, 'middle', MUT))
    o.append(R(xt, y, x1 - xt, 40, LVS, LV, 0, 2))
    o.append(T((xt + x1) / 2, y + 25, 'trailer 8 B', 13, 'middle', LV, True))
    o.append(T(x1, y + 60, 'trailer = length and CRC-32; pad and trailer not to scale', 13, 'end', MUT))
    o.append(brace(x0, x1, y + 80, MUT))
    o.append(T((x0 + x1) / 2, y + 104, '1500 + 28 + 8 = 1536 B = 32 × 48 B payloads', 13, 'middle', INK, True))
    # the cells
    yc = 220
    cw = 120
    def cell(x, lab, last=False):
        out = [R(x, yc, 22, 46, NXS, NX, 0, 1.5), T(x + 11, yc + 28, '5', 13, 'middle', NX, True)]
        if not last:
            out += [R(x + 22, yc, cw - 22, 46, ACS, AC, 0, 1.5), T(x + 22 + (cw - 22) / 2, yc + 28, '48 data', 13, 'middle', INK)]
        else:
            w = cw + 70 - 22
            out += [R(x + 22, yc, w * 12 / 48, 46, ACS, AC, 0, 1.5), R(x + 22 + w * 12 / 48, yc, w * 28 / 48, 46, PANEL, MUT, 0, 1.5, '3 2'),
                    R(x + 22 + w * 40 / 48, yc, w * 8 / 48, 46, LVS, LV, 0, 1.5),
                    T(x + 22 + w * 6 / 48, yc + 28, '12', 13, 'middle', INK), T(x + 22 + w * 26 / 48, yc + 28, 'pad 28', 13, 'middle', MUT),
                    T(x + 22 + w * 44 / 48, yc + 28, '8', 13, 'middle', LV, True)]
        out.append(T(x + (cw if not last else cw + 70) / 2, yc + 66, lab, 13, 'middle', MUT))
        return ''.join(out)
    o.append(cell(40, 'cell 1'))
    o.append(cell(170, 'cell 2'))
    o.append(T(392, yc + 29, '… cells 3 to 31 …', 14, 'middle', MUT))
    o.append(cell(490, 'cell 32 (last)', True))
    o.append(T(40, yc - 12, 'header 5 B + payload 48 B = 53 B per cell', 13, 'start', NX))
    o.append(T(360, yc + 104, '32 cells × 53 B = 1696 B on the link; efficiency 1500 ÷ 1696 = 88.4 %', 14, 'middle', INK, True))
    return yc + 124, ''.join(o)
FIG[8] = (fig8, 'The worked example: AAL5 pads the 1500-byte packet with 28 bytes and adds the 8-byte trailer, making 1536 bytes, exactly 32 payloads of 48 bytes. Each cell gets a 5-byte header, so 1696 bytes go on the link, and the last cell holds 12 data bytes, the pad and the trailer.',
          'Top: a long bar for the 1500-byte packet followed by a short pad block and a thin trailer block, with a brace marking 1536 bytes. Bottom: cell 1, cell 2, a gap for cells 3 to 31, and cell 32, each with a 5-byte header; the last cell shows 12 data bytes, 28 pad bytes and the 8-byte trailer.')


_spec = make_spec(FIG)
AFTER = {1: 1, 2: 3, 3: 3, 4: 2, 5: 1, 6: 2, 7: 3, 8: 2}   # the section each figure follows


def spec(k):
    d = _spec(k)
    d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return []
