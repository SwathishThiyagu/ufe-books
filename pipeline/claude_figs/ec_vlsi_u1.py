"""Claude's hand-drawn figures for ec-vlsi-u1 (MOS transistor theory), one per chapter.
Every curve is computed from that chapter's own worked example; colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
W = 720
SUB = lambda s: f'<tspan font-size="11" baseline-shift="sub">{s}</tspan>'
SUP = lambda s: f'<tspan font-size="11" baseline-shift="super">{s}</tspan>'


def curve(f, a, b, fx, fy, n=200, c=AC, w=2.5, dash=None):
    return P([(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


# ---- 1.1 nMOS cross-section, channel thick at the source and thin at the drain (worked example 2) ----
def f1():
    o = []
    bx0, bx1, by0, by1 = 60, 660, 150, 330           # p body
    o.append(R(bx0, by0, bx1 - bx0, by1 - by0, 'var(--next-soft)', NX, 4))
    o.append(T(360, 318, 'p-type body (holes), N' + SUB('A'), 14, 'middle', INK))
    o.append(P([(240, by0 + 50), (480, by0 + 58)], MUT, 1.6, '6 5'))
    o.append(T(360, by0 + 74, 'depletion edge', 13, 'middle', MUT))
    o.append(R(90, by0, 150, 70, 'var(--live-soft)', LV, 10)); o.append(T(165, 192, 'n⁺ source', 14, 'middle', INK, True))
    o.append(R(480, by0, 150, 70, 'var(--live-soft)', LV, 10)); o.append(T(555, 192, 'n⁺ drain', 14, 'middle', INK, True))
    # channel: thickness drawn in proportion to the local overdrive, 1.0 V at the source and 0.6 V at the drain
    t0, t1 = 34, 34 * 0.6
    o.append(f'<polygon points="240,{by0} 480,{by0} 480,{by0 + t1:.1f} 240,{by0 + t0:.1f}" style="fill:var(--accent-soft);stroke:none"/>')
    o.append(L(240, by0 + t0, 480, by0 + t1, AC, 2.5))
    o.append(R(230, by0 - 14, 260, 14, FIGBG, MUT, 1, 1.5)); o.append(T(225, by0 - 3, 'oxide', 13, 'end', MUT))
    o.append(R(230, 70, 260, 52, PANEL, AC, 6)); o.append(T(360, 101, 'gate (G)', 15, 'middle', INK, True))
    o.append(L(360, 70, 360, 40, INK, 2)); o.append(T(360, 30, 'V' + SUB('GS') + ' = 1.5 V', 14, 'middle', INK, True))
    o.append(L(120, by0, 120, 40, INK, 2)); o.append(T(120, 30, 'S: 0 V', 14, 'middle', INK, True))
    o.append(L(600, by0, 600, 40, INK, 2)); o.append(T(600, 30, 'D: V' + SUB('DS') + ' = 0.4 V', 14, 'middle', INK, True))
    o.append(T(300, by0 + 22, '8.6 fC/µm²', 13, 'middle', AC, True))
    o.append(T(425, by0 + 14, '5.16 fC/µm²', 13, 'middle', AC, True))
    o.append(Tb(190, 258, 'source end: 1.5 − 0.5 = 1.0 V', 13, 'middle', INK))
    o.append(Tb(520, 258, 'drain end: 1.5 − 0.4 − 0.5 = 0.6 V', 13, 'middle', INK))
    o.append(T(360, 282, 'local overdrive V' + SUB('GS') + ' − V(x) − V' + SUB('T') + ' sets the channel charge', 13, 'middle', MUT))
    o.append(T(360, 358, 'Raise V' + SUB('DS') + ' to 1.0 V and the drain end thins to zero: pinch-off.', 14, 'middle', INK))
    return 376, ''.join(o)


FIG[1] = (f1, 'The nMOS of worked example 2 at V<sub>GS</sub> = 1.5 V and V<sub>DS</sub> = 0.4 V. The electron channel is thickest at the source, where the local overdrive is 1.0 V, '
              'and thinner at the drain, where only 0.6 V is left; at V<sub>DS</sub> = 1.0 V the drain end pinches off.',
          'Cross-section of an nMOS: gate on a thin oxide over a p body, n-plus source and drain, and a channel that tapers from 8.6 femtocoulomb per square micrometre at the source to 5.16 at the drain.')


# ---- 1.2 threshold voltage against source-to-body voltage for the worked device ----
G2, PF2 = 0.21151, 0.81706


def vt2(v):
    return 0.45 + G2 * (math.sqrt(PF2 + v) - math.sqrt(PF2))


def f2():
    o = []
    x0, x1, y0, y1 = 90, 620, 50, 300
    fx = lambda v: x0 + v / 3 * (x1 - x0)
    fy = lambda t: y1 - (t - 0.4) / 0.35 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 1, 1.5, 2, 2.5, 3], [0.4, 0.5, 0.6, 0.7], fx, fy,
                  'source-to-body voltage V' + SUB('SB') + ' (V)', 'threshold V' + SUB('T') + ' (V)', lambda v: f'{v:g}', lambda v: f'{v:.1f}'))
    o.append(L(x0, fy(0.45), x1, fy(0.45), L2, 1.5, '6 5'))
    o.append(T(x1, fy(0.45) + 18, 'V' + SUB('T0') + ' = 0.45 V (source tied to body)', 13, 'end', MUT))
    o.append(curve(vt2, 0, 3, fx, fy, 150, AC, 3))
    for v, lab in ((0, '0.450'), (1, '0.544'), (2, '0.614'), (3, '0.672')):
        o.append(C(fx(v), fy(vt2(v)), 5, AC))
        o.append(Tb(fx(v) + (14 if v < 3 else -10), fy(vt2(v)) - 12, lab + ' V', 13, 'start' if v < 3 else 'end', INK, True))
    o.append(L(fx(1), fy(0.45), fx(1), fy(vt2(1)), LV, 2.5, None, 'l'))
    o.append(Tb(fx(1) + 10, fy(0.497) + 4, 'ΔV' + SUB('T') + ' = 0.094 V', 13, 'start', LV, True))
    o.append(T(x0 + 14, y0 + 6, 'γ = 0.21 √V,  2φ' + SUB('F') + ' = 0.817 V', 14, 'start', INK))
    o.append(T(x0 + 14, y0 + 26, 'steepest at small V' + SUB('SB') + ', then grows as a square root', 13, 'start', MUT))
    return 360, ''.join(o)


FIG[2] = (f2, 'Threshold voltage of the worked device as its source rises above the body. At V<sub>SB</sub> = 1 V the body effect has added 0.094 V; '
              'each further volt adds less (0.070 V, then 0.058 V).',
          'Plot of threshold voltage against source-to-body voltage from 0 to 3 volts for gamma 0.21 root volt: 0.450, 0.544, 0.614 and 0.672 volts at 0, 1, 2 and 3 volts.')


# ---- 1.3 output characteristics of the worked device, kn'(W/L) = 2000 uA/V^2, VT = 0.5 V ----
def id3(vgs, vds, k=2.0):          # mA
    vov = vgs - 0.5
    if vov <= 0: return 0.0
    return k * (vov * vds - vds * vds / 2) if vds < vov else 0.5 * k * vov * vov


def f3():
    o = []
    x0, x1, y0, y1 = 90, 600, 40, 300
    fx = lambda v: x0 + v / 2.5 * (x1 - x0)
    fy = lambda i: y1 - i / 2.5 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 1, 1.5, 2, 2.5], [0, 0.5, 1, 1.5, 2, 2.5], fx, fy,
                  'drain-source voltage V' + SUB('DS') + ' (V)', 'I' + SUB('D') + ' (mA)', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    # region boundary ID = 0.5 k VDS^2
    o.append(curve(lambda v: 0.5 * 2.0 * v * v, 0, 1.58, fx, fy, 80, MUT, 1.8, '6 5'))
    o.append(Tb(fx(1.52), fy(2.38), 'V' + SUB('DS') + ' = V' + SUB('ov') + ' (pinch-off)', 13, 'end', MUT))
    o.append(T(fx(0.22), fy(1.75), 'linear', 14, 'middle', MUT, True))
    o.append(T(fx(2.05), fy(1.75), 'saturation', 14, 'middle', MUT, True))
    for vgs, c in ((1.0, NX), (1.5, AC), (2.0, LV)):
        o.append(curve(lambda v, g=vgs: id3(g, v), 0, 2.5, fx, fy, 200, c, 2.8))
        o.append(T(x1 + 8, fy(id3(vgs, 2.5)) + 5, 'V' + SUB('GS') + f' = {vgs:.1f} V', 13, 'start', c, True))
    for v, i, lab, anc in ((0.5, 0.75, '0.75 mA at 0.5 V', 'start'), (2.0, 1.0, '1 mA at 2 V', 'end')):
        o.append(C(fx(v), fy(i), 6, AC))
        o.append(Tb(fx(v) + (12 if anc == 'start' else -4), fy(i) + 22, lab, 13, anc, INK, True))
    o.append(T(fx(2.5), fy(0.25) - 10, '0.25', 13, 'end', NX))
    o.append(T(fx(2.5), fy(2.25) - 10, '2.25', 13, 'end', LV))
    return 350, ''.join(o)


FIG[3] = (f3, 'Output characteristics of the first worked example (k<sub>n</sub>′W/L = 2000 µA/V², V<sub>T</sub> = 0.5 V). Each curve is linear at low V<sub>DS</sub>, bends where it meets the dashed pinch-off parabola and then stays flat; '
              'the flat levels 0.25, 1 and 2.25 mA grow as the square of the overdrive. The two dots are the answers of the example.',
          'Drain current against drain-source voltage for gate voltages 1.0, 1.5 and 2.0 volts, flat at 0.25, 1 and 2.25 milliamps beyond a dashed pinch-off parabola; dots at 0.75 milliamp for 0.5 volt and 1 milliamp for 2 volts.')


# ---- 1.4 square law against the velocity-saturated model for the worked device (Vov = 2 V) ----
K4, EL4, VD4, I4 = 1.72, 0.5, 1.0, 0.86        # mA/V^2, V, V, mA


def vs4(v):
    return K4 * (2 * v - v * v / 2) / (1 + v / EL4) if v < VD4 else I4


def sq4(v):
    return K4 * (2 * v - v * v / 2) if v < 2 else 0.5 * K4 * 4


def f4():
    o = []
    x0, x1, y0, y1 = 90, 600, 40, 300
    fx = lambda v: x0 + v / 2.5 * (x1 - x0)
    fy = lambda i: y1 - i / 4.0 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 1, 1.5, 2, 2.5], [0, 1, 2, 3, 4], fx, fy,
                  'drain-source voltage V' + SUB('DS') + ' (V)', 'I' + SUB('D') + ' (mA)', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    o.append(curve(sq4, 0, 2.5, fx, fy, 200, MUT, 2.4, '8 5'))
    o.append(curve(vs4, 0, 2.5, fx, fy, 200, AC, 3))
    o.append(L(fx(1.0), fy(0.86), fx(2.5), fy(0.86 * (1 + 0.1 * 1.5)), LV, 2.2, '3 4'))
    o.append(C(fx(2.0), fy(3.44), 5, MUT)); o.append(C(fx(1.0), fy(0.86), 6, AC))
    o.append(Tb(fx(1.9), fy(3.44) - 12, 'square law: 3.44 mA at V' + SUB('DS') + ' = 2 V', 13, 'end', INK, True))
    o.append(Tb(fx(1.06), fy(0.86) + 24, 'velocity-saturated: 0.86 mA at V' + SUB('DSsat') + ' = 1.0 V', 13, 'start', AC, True))
    o.append(Tb(fx(2.3), fy(0.97) - 12, 'with λ = 0.1 V⁻¹: slope λI' + SUB('D'), 13, 'end', LV))
    o.append(L(fx(2.42), fy(3.44) + 6, fx(2.42), fy(1.0) - 4, NX, 2, None, 'x'))
    o.append(Tb(fx(2.38), fy(2.2), '4 times less', 13, 'end', NX, True))
    o.append(T(fx(1.1), fy(1.7), 'W/L = 1 µm / 0.25 µm, V' + SUB('ov') + ' = 2 V, E' + SUB('c') + 'L = 0.5 V', 13, 'start', MUT))
    return 350, ''.join(o)


FIG[4] = (f4, 'The device of the first worked example at an overdrive of 2 V. The dashed square law would reach 3.44 mA; with velocity saturation the current stops at 0.86 mA once V<sub>DS</sub> reaches 1.0 V. '
              'The dotted line is the small upward slope that channel length modulation adds in saturation.',
          'Drain current against drain voltage: a dashed square-law curve rising to 3.44 milliamps at 2 volts, and a solid velocity-saturated curve flattening at 0.86 milliamp from 1.0 volt, with a dotted line of slope lambda times I D beyond it.')


# ---- 1.5 where the capacitances and resistances sit, with the worked values in saturation ----
def cap(x, y1, y2, c=AC, w=2.2, dash=None):
    m = (y1 + y2) / 2
    return (L(x, y1, x, m - 5, c, w, dash) + L(x - 13, m - 5, x + 13, m - 5, c, 3) +
            L(x - 13, m + 5, x + 13, m + 5, c, 3) + L(x, m + 5, x, y2, c, w, dash))


def zig(x, y1, y2, c=LV):
    n, pts, h = 6, [(x, y1)], (y2 - y1) / 6
    for i in range(n):
        pts.append((x + (8 if i % 2 == 0 else -8), y1 + h * (i + 0.5)))
    pts.append((x, y2))
    return P(pts, c, 2.2)


def f5():
    o = []
    by0 = 210
    o.append(R(40, by0, 640, 130, 'var(--next-soft)', NX, 4))
    o.append(T(360, by0 + 118, 'p body (B)', 14, 'middle', INK, True))
    o.append(R(110, by0, 150, 56, 'var(--live-soft)', LV, 10)); o.append(T(185, by0 + 34, 'n⁺ source', 14, 'middle', INK, True))
    o.append(R(460, by0, 150, 56, 'var(--live-soft)', LV, 10)); o.append(T(535, by0 + 34, 'n⁺ drain', 14, 'middle', INK, True))
    o.append(R(240, by0 - 12, 240, 12, FIGBG, MUT, 1, 1.5))
    o.append(R(240, 150, 240, 46, PANEL, AC, 6)); o.append(T(360, 178, 'gate (G)', 15, 'middle', INK, True))
    o.append(P([(262, by0 + 4), (458, by0 + 2)], AC, 3))
    o.append(T(360, by0 + 30, 'C' + SUB('gb') + ' = 0 in saturation', 13, 'middle', MUT))
    # Cgs and Cgd from the gate sides down to the wells
    o.append(L(240, 166, 205, 166, AC, 2)); o.append(cap(205, 166, by0))
    o.append(T(196, 120, 'C' + SUB('gs') + ' = 1.61 fF', 14, 'end', AC, True))
    o.append(T(196, 139, '⅔C' + SUB('ox') + 'WL + C' + SUB('ov'), 13, 'end', AC))
    o.append(L(480, 166, 515, 166, AC, 2)); o.append(cap(515, 166, by0))
    o.append(T(524, 120, 'C' + SUB('gd') + ' = 0.17 fF', 14, 'start', AC, True))
    o.append(T(524, 139, 'overlap only', 13, 'start', AC))
    # junction capacitances
    o.append(cap(185, by0 + 56, by0 + 100, NX)); o.append(T(205, by0 + 86, 'C' + SUB('sb'), 13, 'start', NX, True))
    o.append(cap(535, by0 + 56, by0 + 100, NX)); o.append(T(555, by0 + 86, 'C' + SUB('db') + ' = 0.57 fF', 13, 'start', NX, True))
    # series resistances to the terminals
    o.append(zig(75, 50, 170)); o.append(P([(75, 170), (75, by0 + 28), (110, by0 + 28)], LV, 2.2)); o.append(T(90, 112, 'R' + SUB('s'), 14, 'start', LV, True))
    o.append(zig(645, 50, 170)); o.append(P([(645, 170), (645, by0 + 28), (610, by0 + 28)], LV, 2.2)); o.append(T(632, 78, 'R' + SUB('d') + ' = 45 Ω', 13, 'end', LV, True))
    o.append(T(75, 38, 'S', 14, 'middle', INK, True)); o.append(T(645, 38, 'D', 14, 'middle', INK, True))
    o.append(L(360, 150, 360, 50, INK, 2)); o.append(T(360, 38, 'G', 14, 'middle', INK, True))
    o.append(T(360, 366, 'C' + SUB('db') + ' at 1.8 V reverse bias; R' + SUB('d') + ' = 50 Ω × 0.5 square + 20 Ω contact', 13, 'middle', MUT))
    return 380, ''.join(o)


FIG[5] = (f5, 'Where the parasitics of the worked transistor sit, with their values in saturation. The gate charge goes mostly to the source (1.61 fF); the drain sees only the overlap (0.17 fF), '
              'the junctions add C<sub>sb</sub> and C<sub>db</sub>, and the diffusions and contacts put resistance in series with the channel.',
          'Cross-section of an nMOS with capacitors drawn from gate to source (1.61 femtofarad), gate to drain (0.17), drain to body (0.57), source to body, and series resistors of 45 ohm at the drain and source.')


# ---- 1.6 the worked gate before and after constant-field scaling by S = 2 ----
def dev(x, y, sc, lab_l, lab_t, lab_v):
    """simplified nMOS: body, two wells, oxide and gate, all lengths times sc; x is the left edge, y the silicon surface"""
    o = []
    wb, hw, lg, hg = 300 * sc, 50 * sc, 110 * sc, 40 * sc
    o.append(R(x, y, wb, 110 * sc, 'var(--next-soft)', NX, 4))
    o.append(R(x + 20 * sc, y, (wb - lg) / 2 - 20 * sc, hw, 'var(--live-soft)', LV, 6))
    o.append(R(x + (wb + lg) / 2, y, (wb - lg) / 2 - 20 * sc, hw, 'var(--live-soft)', LV, 6))
    o.append(R(x + (wb - lg) / 2, y - 10 * sc, lg, 10 * sc, FIGBG, MUT, 1, 1.3))
    o.append(R(x + (wb - lg) / 2, y - 10 * sc - hg, lg, hg, PANEL, AC, 4))
    cx = x + wb / 2
    o.append(brace(x + (wb - lg) / 2, x + (wb + lg) / 2, y + 110 * sc + 14, INK))
    o.append(T(cx, y + 110 * sc + 34, lab_l, 13, 'middle', INK, True))
    o.append(T(x + (wb + lg) / 2 + 6, y - 14 * sc - hg - 4, lab_t, 13, 'start', MUT))
    o.append(T(cx, y - 10 * sc - hg - 12, lab_v, 14, 'middle', AC, True))
    return ''.join(o)


def f6():
    o = []
    o.append(T(170, 28, 'before', 14, 'middle', INK, True)); o.append(T(530, 28, 'after, S = 2', 14, 'middle', INK, True))
    o.append(dev(20, 120, 1.0, 'L = 0.25 µm', 't' + SUB('ox') + ' = 5 nm', 'V' + SUB('DD') + ' = 2.5 V'))
    o.append(dev(455, 150, 0.5, 'L = 0.125 µm', '2.5 nm', '1.25 V'))
    o.append(L(340, 160, 420, 160, AC, 2.5, None, 'n'))
    o.append(T(380, 148, '÷ 2', 14, 'middle', AC, True))
    o.append(T(390, 196, 'field V' + SUB('DD') + '/L', 13, 'middle', MUT)); o.append(T(390, 214, '10 V/µm in both', 13, 'middle', MUT))
    rows = [('load C', '10 fF', '5 fF'), ('clock f', '100 MHz', '200 MHz'), ('power C·V' + SUB('DD') + '²·f', '6.25 µW', '1.56 µW'),
            ('area per gate', '1', '¼'), ('power density', '1', '1')]
    y = 300
    o.append(L(60, y - 18, 660, y - 18, L2, 1.2))
    for i, (a, b, c) in enumerate(rows):
        yy = y + i * 24
        o.append(T(70, yy, a, 13, 'start', INK)); o.append(T(380, yy, b, 13, 'middle', INK, True)); o.append(T(560, yy, c, 13, 'middle', AC, True))
    return 420, ''.join(o)


FIG[6] = (f6, 'The gate of the first worked example before and after constant-field scaling by S = 2. Length, oxide and supply all halve, so the field stays at 10 V/µm; '
              'the load halves, the clock doubles, the power per gate falls by four and so does its area, leaving the power density unchanged.',
          'Two nMOS cross-sections, the second half the size: L 0.25 to 0.125 micrometre, oxide 5 to 2.5 nanometre, supply 2.5 to 1.25 volt; a table below gives load 10 to 5 femtofarad, clock 100 to 200 megahertz, power 6.25 to 1.56 microwatt, area 1 to one quarter, power density 1 to 1.')


# ---- 1.7 subthreshold current on a log scale for VT = 0.3 V and 0.4 V, SS = 80 mV/decade ----
def f7():
    o = []
    x0, x1, y0, y1 = 100, 560, 40, 320
    fx = lambda v: x0 + v / 0.5 * (x1 - x0)
    fy = lambda lg: y1 - (lg + 11) / 8 * (y1 - y0)       # log10 of amps per micrometre, from 1e-11 to 1e-3
    lab = {-11: '10⁻¹¹', -10: '10⁻¹⁰', -9: '1 nA', -8: '10 nA', -7: '100 nA', -6: '1 µA', -5: '10 µA', -4: '100 µA', -3: '1 mA'}
    o.append(axes(x0, x1, y0, y1, [0, 0.1, 0.2, 0.3, 0.4, 0.5], list(range(-11, -2)), fx, fy,
                  'gate-source voltage V' + SUB('GS') + ' (V)', 'I' + SUB('D') + ' per µm of width (log scale)', lambda v: f'{v:g}', lambda v: lab[v]))
    i_vt = math.log10(10e-9) + 0.3 / 0.08               # current at threshold, the same for both devices
    for vt, c in ((0.3, AC), (0.4, LV)):
        o.append(P([(fx(v), fy(i_vt + (v - vt) / 0.08)) for v in (0, vt)], c, 3))
        o.append(f'<path d="M{fx(vt):.1f},{fy(i_vt):.1f} Q{fx(vt + 0.06):.1f},{fy(i_vt + 0.6):.1f} {fx(min(vt + 0.12, 0.5)):.1f},{fy(i_vt + 0.85 - (0.1 if vt > 0.35 else 0)):.1f}" style="fill:none;stroke:{c};stroke-width:3"/>')
        o.append(C(fx(0), fy(i_vt - vt / 0.08), 6, c))
        o.append(C(fx(vt), fy(i_vt), 4, c))
    o.append(T(fx(0.3) - 10, fy(i_vt) - 8, 'V' + SUB('T') + ' = 0.3 V', 13, 'end', AC, True))
    o.append(T(fx(0.4) + 10, fy(i_vt) + 22, 'V' + SUB('T') + ' = 0.4 V', 13, 'start', LV, True))
    # one decade of the swing, on the second line
    i2 = math.log10(0.562e-9)
    xa, xb = fx(0.22), fx(0.30)
    ya, yb = fy(i2 + 0.22 / 0.08), fy(i2 + 0.30 / 0.08)
    o.append(P([(xa, ya), (xb, ya), (xb, yb)], NX, 2, '4 3'))
    o.append(T((xa + xb) / 2, ya + 18, '80 mV', 13, 'middle', NX, True))
    o.append(T(xb + 6, (ya + yb) / 2 + 12, '× 10', 13, 'start', NX, True))
    o.append(T(fx(0.17), fy(-9.9), 'at V' + SUB('GS') + ' = 0 (dots):', 13, 'start', MUT))
    o.append(T(fx(0.17), fy(-9.9) + 20, 'V' + SUB('T') + ' = 0.3 V: I' + SUB('off') + ' = 10 nA/µm', 13, 'start', AC, True))
    o.append(T(fx(0.17), fy(-9.9) + 40, 'V' + SUB('T') + ' = 0.4 V: I' + SUB('off') + ' = 0.56 nA/µm', 13, 'start', LV, True))
    o.append(T(575, 130, 'raising V' + SUB('T'), 13, 'start', INK))
    o.append(T(575, 148, 'by 100 mV shifts', 13, 'start', INK))
    o.append(T(575, 166, 'the line right and', 13, 'start', INK))
    o.append(T(575, 184, 'cuts I' + SUB('off') + ' 17.8 ×', 13, 'start', INK, True))
    return 380, ''.join(o)


FIG[7] = (f7, 'Subthreshold current of the first worked example on a log scale. With a swing of 80 mV per decade the current falls tenfold for every 80 mV below threshold, '
              'so moving V<sub>T</sub> from 0.3 V to 0.4 V lowers the off current at V<sub>GS</sub> = 0 from 10 nA/µm to 0.56 nA/µm.',
          'Log drain current per micrometre against gate voltage: two straight lines with 80 millivolts per decade slope, reaching threshold at 0.3 and 0.4 volt, crossing zero gate voltage at 10 nanoamps and 0.56 nanoamp per micrometre.')


# ---- 1.8 planar and fin cross-sections across the channel, with the worked fin (10 nm x 30 nm) ----
def f8():
    o = []
    # planar: gate on top of a flat channel
    o.append(T(170, 30, 'planar: gate on top only', 14, 'middle', INK, True))
    o.append(R(40, 180, 260, 110, 'var(--next-soft)', NX, 4)); o.append(T(170, 274, 'silicon body', 13, 'middle', INK))
    o.append(R(60, 170, 220, 10, FIGBG, MUT, 1, 1.3))
    o.append(R(60, 120, 220, 50, PANEL, AC, 6)); o.append(T(170, 150, 'gate', 14, 'middle', INK, True))
    o.append(P([(64, 183), (276, 183)], AC, 4)); o.append(T(195, 208, 'channel: one surface', 13, 'middle', AC, True))
    o.append(L(80, 248, 80, 192, LV, 2, '4 3', 'l')); o.append(T(88, 240, 'drain field', 13, 'start', LV))
    o.append(T(88, 256, 'reaches under', 13, 'start', LV))
    # fin: gate wraps top and both sides
    s = 4.0                                  # px per nm
    fx0, fy0 = 520, 270                      # fin base centre
    wf, hf = 10 * s, 30 * s
    o.append(T(530, 30, 'FinFET: gate on three sides', 14, 'middle', INK, True))
    o.append(R(380, fy0, 300, 20, 'var(--next-soft)', NX, 2))
    o.append(T(530, fy0 + 15, 'oxide (isolation)', 13, 'middle', MUT))
    gx0, gx1, gt = fx0 - wf / 2 - 34, fx0 + wf / 2 + 34, fy0 - hf - 56
    o.append(R(gx0, gt, gx1 - gx0, fy0 - gt, PANEL, AC, 6))
    o.append(R(fx0 - wf / 2 - 6, fy0 - hf - 6, wf + 12, hf + 6, FIGBG, MUT, 2, 1.3))
    o.append(R(fx0 - wf / 2, fy0 - hf, wf, hf, 'var(--next-soft)', NX, 1))
    o.append(P([(fx0 - wf / 2 + 2, fy0 - 2), (fx0 - wf / 2 + 2, fy0 - hf + 2), (fx0 + wf / 2 - 2, fy0 - hf + 2), (fx0 + wf / 2 - 2, fy0 - 2)], AC, 3.5))
    o.append(T(fx0, gt + 26, 'gate', 14, 'middle', INK, True))
    # dimensions
    o.append(brace(fx0 - wf / 2, fx0 + wf / 2, gt - 12, INK, up=True))
    o.append(T(fx0, gt - 28, 'W' + SUB('fin') + ' = 10 nm', 13, 'middle', INK, True))
    o.append(P([(gx1 + 14, fy0 - hf), (gx1 + 20, fy0 - hf), (gx1 + 20, fy0), (gx1 + 14, fy0)], INK, 1.8))
    o.append(T(gx1 + 26, fy0 - hf / 2 + 5, 'H' + SUB('fin') + ' = 30 nm', 13, 'start', INK, True))
    o.append(T(gx0 - 8, fy0 - hf / 2 - 8, 'fin', 13, 'end', NX, True))
    o.append(T(gx0 - 8, fy0 - hf / 2 + 10, '(silicon)', 13, 'end', NX))
    o.append(T(530, 336, 'channel on top and both sides: W' + SUB('eff') + ' = 2 × 30 + 10 = 70 nm', 14, 'middle', AC, True))
    o.append(T(530, 358, '10 fins → 700 nm, 0.7 mA at 1 mA/µm', 13, 'middle', MUT))
    return 376, ''.join(o)


FIG[8] = (f8, 'Cross-sections across the channel. The planar gate touches the channel on one surface, and the drain field can reach the body underneath. '
              'In the worked FinFET the gate wraps a 10 nm wide, 30 nm tall fin, so the channel runs along three faces: W<sub>eff</sub> = 70 nm per fin.',
          'Left: planar transistor with the gate above a flat channel. Right: a fin 10 nanometres wide and 30 tall with the gate wrapped over its top and both sides, effective width 70 nanometres.')


spec = make_spec(FIG)
