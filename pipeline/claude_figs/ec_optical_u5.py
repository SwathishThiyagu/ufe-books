"""Claude's hand-drawn figures for ec-optical-u5 (Link design and fiber measurements), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
sub = lambda s: f'<tspan font-size="11" dy="4">{s}</tspan><tspan dy="-4">\u200b</tspan>'


def arrow(x1, y1, x2, y2, c=AC, w=2, a='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, a)


# ---- 5.1 the link chain and where its three noises come from (worked example at -10 dBm) ----
def f1():
    o = []
    names = [('Driver +', 'laser'), ('Fiber +', 'joints'), ('Photodiode', 'ℛ = 0.6 A/W'), ('Preamp +', 'filter 6 MHz'), ('Decision', 'or CNR meter')]
    xs = [16 + i * 142 for i in range(5)]
    for i, (a, b) in enumerate(names):
        o.append(boxt(xs[i], 36, 120, 64, [a, b], ACS if i in (0, 4) else PANEL, AC, 14, bold_first=True))
        if i < 4: o.append(arrow(xs[i] + 120, 68, xs[i + 1] - 4, 68))
    o.append(T(76 + 142, 122, '−10 dBm arrives', 13, fill=MUT))
    o.append(T(76 + 284, 122, 'I' + sub('p') + ' = 60 µA', 13, fill=MUT))
    # bars
    y0, sc, bx = 196, 150, 250
    o.append(T(16, 168, 'Noise power at the receiver (× 10⁻¹⁶ A²)', 15, 'start', bold=True))
    bars = [('RIN (from the laser)', 1.08, NX, xs[0] + 60), ('Shot (photodiode)', 1.15, LV, xs[2] + 60), ('Thermal (preamp)', 2.65, AC, xs[3] + 60)]
    for j, (lab, v, c, xsrc) in enumerate(bars):
        y = y0 + j * 46
        o.append(T(bx - 12, y + 19, lab, 14, 'end'))
        o.append(R(bx, y + 2, v * sc, 26, c, c, 4, 1))
        o.append(T(bx + v * sc + 8, y + 20, f'{v:.2f}', 14, 'start', bold=True))
    o.append(L(bx, y0 - 4, bx, y0 + 3 * 46, L2, 1.5))
    o.append(T(bx, y0 + 3 * 46 + 24, 'total noise 4.88 × 10⁻¹⁶ A²', 14, 'start'))
    o.append(T(bx, y0 + 3 * 46 + 46, 'signal ½(mI' + sub('p') + ')² = 4.50 × 10⁻¹⁰ A²', 14, 'start'))
    o.append(T(bx, y0 + 3 * 46 + 72, 'CNR = 9.22 × 10⁵ = 59.6 dB', 15, 'start', fill=AC, bold=True))
    return 422, ''.join(o)

FIG[1] = (f1, 'The worked example\'s link: −10 dBm reaches a 0.6 A/W photodiode, giving 60 µA. Of the three noises, the preamplifier\'s thermal noise is the largest, and together they set the CNR at 59.6 dB.',
          'Five blocks in a row: driver and laser, fiber and joints, photodiode, preamplifier and filter, decision or CNR meter. Below, bars of noise power: RIN 1.08, shot 1.15 and thermal 2.65 times ten to the minus 16 amperes squared, total 4.88, giving a CNR of 59.6 dB.')


# ---- 5.2 power level diagram of the 60 km budget ----
def f2():
    x0, x1, ytop = 80, 540, 46
    fx = lambda z: x0 + z / 60 * (x1 - x0)
    fy = lambda p: ytop + (-p) * 10.5
    o = [axes(x0, x1, ytop, fy(-30), [0, 10, 20, 30, 40, 50, 60], [0, -10, -20, -30], fx, fy, 'distance along the link (km)', 'power (dBm)', yfmt=neg)]
    pts = [(fx(0), fy(0)), (fx(0), fy(-0.5))]
    p = -0.5
    for z in range(0, 60, 10):
        p -= 2.2; pts.append((fx(z + 10), fy(p)))
        if z + 10 < 60: p -= 0.1; pts.append((fx(z + 10), fy(p)))
    p -= 0.5; pts.append((fx(60), fy(p)))
    o.append(P(pts, AC, 3))
    o.append(T(fx(6), fy(0) + 12, '0 dBm launched', 13, 'start'))
    o.append(T(fx(3), fy(-16), 'fiber 0.22 dB/km; 5 splices of 0.1 dB', 13, 'start', fill=MUT))
    o.append(T(fx(3), fy(-18), 'one 0.5 dB connector at each end', 13, 'start', fill=MUT))
    # levels at the right
    xr = fx(60)
    o.append(L(x0, fy(-28), x1 + 10, fy(-28), NX, 2, '7 5'))
    o.append(Tb(fx(14), fy(-28) - 8, 'sensitivity −28 dBm', 13, fill=NX))
    o.append(L(x0, fy(-8), x1 + 10, fy(-8), L2, 1.5, '3 4'))
    o.append(Tb(fx(14), fy(-8) - 8, 'overload −8 dBm', 13, fill=MUT))
    o.append(C(xr, fy(-14.7), 6, AC))
    o.append(R(x1 + 14, fy(-14.7), 22, fy(-20.7) - fy(-14.7), LVS, LV, 3, 1.5))
    o.append(R(x1 + 14, fy(-20.7), 22, fy(-28) - fy(-20.7), ACS, AC, 3, 1.5))
    o.append(T(x1 + 44, fy(-14.7) + 5, '−14.7 dBm received', 13, 'start', bold=True))
    o.append(T(x1 + 44, fy(-17.7) + 5, 'margin 6 dB', 13, 'start', fill=LV))
    o.append(T(x1 + 44, fy(-24.35) + 5, 'spare 7.3 dB', 13, 'start', fill=AC, bold=True))
    return 420, ''.join(o)

FIG[2] = (f2, 'Power along the 60 km link: 0.5 dB at each connector, 2.2 dB per 10 km reel and 0.1 dB at each splice bring 0 dBm down to −14.7 dBm. Above the −28 dBm sensitivity, 6 dB is held as margin and 7.3 dB is spare.',
          'Graph of power in dBm against distance from 0 to 60 kilometres. The line falls from 0 dBm to minus 14.7 dBm with small steps at five splices. Dashed lines mark the sensitivity at minus 28 dBm and overload at minus 8 dBm. A stacked bar at the end shows 6 dB margin and 7.3 dB spare.')


# ---- 5.3 attenuation and dispersion limits against bit rate (log-log) ----
def f3():
    x0, x1, y0, y1 = 90, 560, 50, 350
    lx = lambda b: x0 + (math.log10(b) + 1) / 2 * (x1 - x0)          # 0.1 .. 10 Gbit/s
    ly = lambda l: y1 - math.log10(l) / 3 * (y1 - y0)                 # 1 .. 1000 km
    o = [L(x0, y1, x1, y1, L2, 1.5), L(x0, y0, x0, y1, L2, 1.5)]
    for b, s in ((0.1, '0.1'), (1, '1'), (10, '10')):
        o += [L(lx(b), y1, lx(b), y1 + 5, L2, 1.5), T(lx(b), y1 + 20, s, 13, fill=MUT)]
    for l, s in ((1, '1'), (10, '10'), (100, '100'), (1000, '1000')):
        o += [L(x0 - 5, ly(l), x0, ly(l), L2, 1.5), L(x0, ly(l), x1, ly(l), LN, 1), T(x0 - 9, ly(l) + 4.5, s, 13, 'end', MUT)]
    o.append(T((x0 + x1) / 2, y1 + 42, 'bit rate B (Gbit/s, NRZ)', 14, fill=MUT))
    o.append(T(x0, y0 - 16, 'maximum length (km)', 14, 'start', MUT))
    o.append(L(x0, ly(127.3), x1, ly(127.3), AC, 3))
    o.append(T(x1 + 8, ly(127.3) + 5, 'loss 127 km', 13, 'start', fill=AC, bold=True))
    bs = [10 ** (-1 + i / 100) for i in range(201)]
    o.append(P([(lx(b), ly(20.59 / b)) for b in bs], NX, 2.5))
    o.append(T(x1 + 8, ly(2.06) + 5, 'FP 2 nm', 13, 'start', fill=NX, bold=True))
    o.append(P([(lx(b), ly(411.8 / b)) for b in bs if 411.8 / b <= 1000], LV, 2.5, '8 5'))
    o.append(T(x1 + 8, ly(41.2) + 5, 'DFB 0.1 nm', 13, 'start', fill=LV, bold=True))
    o.append(C(lx(0.1618), ly(127.3), 6, NX)); o.append(T(lx(0.1618) + 4, ly(127.3) - 12, '0.16 Gbit/s', 13, 'start'))
    o.append(C(lx(3.235), ly(127.3), 6, LV)); o.append(T(lx(3.235) - 12, ly(127.3) - 12, '3.2 Gbit/s', 13, 'end'))
    o.append(C(lx(1), ly(20.6), 6, NX)); o.append(T(lx(1) + 10, ly(20.6) - 8, '20.6 km', 13, 'start'))
    o.append(C(lx(1), ly(16.2), 6, INK)); o.append(T(lx(1) - 10, ly(16.2) + 18, '16.2 km with t' + sub('tx') + 'and t' + sub('rx'), 13, 'end'))
    return 410, ''.join(o)

FIG[3] = (f3, 'The loss limit (127 km for 28 dB at 0.22 dB/km) against the dispersion limits 0.7/(B|D|σ<sub>λ</sub>) at D = 17 ps/(nm·km). A 2 nm Fabry–Perot laser crosses the loss line at 0.16 Gbit/s; at 1 Gbit/s it allows 20.6 km, and 16.2 km once the transmitter and receiver rise times are counted.',
          'Log-log graph of maximum length in kilometres against bit rate from 0.1 to 10 gigabits per second. A flat line at 127 km for the loss limit, a falling line for a 2 nanometre Fabry-Perot laser and a dashed falling line for a 0.1 nanometre DFB laser. Crossings at 0.16 and 3.2 gigabits per second; points at 20.6 and 16.2 km at 1 gigabit per second.')


# ---- 5.4 cut-back set-up with the worked example's readings ----
def f4():
    o = []
    rows = [(40, 'full length L' + sub('1') + '= 2.0 km', 'P' + sub('1') + '= 6.3 µW'), (180, 'cut back to L' + sub('2') + '= 2 m', 'P' + sub('2') + '= 20.0 µW')]
    for i, (y, flab, plab) in enumerate(rows):
        o.append(boxt(16, y, 96, 56, ['Source', '850 nm'], ACS, AC, 13, bold_first=True))
        o.append(boxt(132, y, 116, 56, ['Mode', 'scrambler'], PANEL, AC, 13))
        o.append(boxt(448, y, 112, 56, ['Cladding-mode', 'stripper'], PANEL, AC, 13))
        o.append(boxt(580, y, 124, 56, ['Detector', plab], LVS, LV, 13, bold_first=True))
        o.append(arrow(112, y + 28, 128, y + 28))
        o.append(arrow(560, y + 28, 576, y + 28))
        if i == 0:
            for c in range(3):
                o.append(f'<circle cx="{318 + c * 22:.1f}" cy="{y + 28}" r="24" style="fill:none;stroke:{AC};stroke-width:2"/>')
            o.append(L(248, y + 28, 296, y + 28, AC, 2)); o.append(L(386, y + 28, 444, y + 28, AC, 2, arrow='n'))
        else:
            o.append(L(248, y + 28, 444, y + 28, AC, 2, arrow='n'))
            o.append(L(300, y + 12, 300, y + 44, NX, 2.5)); o.append(T(300, y + 6, 'cut', 13, fill=NX, bold=True))
        o.append(T(346, y + 76, flab, 13, fill=MUT))
    o.append(R(10, 32, 246, 220, 'none', L2, 10, 1.5, '6 5'))
    o.append(Tb(133, 140, 'launch left untouched', 13, fill=MUT))
    o.append(T(360, 300, 'α = 10 log₁₀(20.0 ÷ 6.3) ÷ (2.0 − 0.002) km = 5.02 dB ÷ 1.998 km = 2.51 dB/km', 14, bold=True, fill=AC))
    return 322, ''.join(o)

FIG[4] = (f4, 'The cut-back method with the worked example\'s readings: 6.3 µW through 2.0 km, then 20.0 µW after cutting to 2 m with the launch untouched. The 5.02 dB difference over 1.998 km gives 2.51 dB/km.',
          'Two rows of the same set-up: source, mode scrambler, fiber, cladding-mode stripper and detector. Top row through 2.0 km of coiled fiber reads 6.3 microwatts; bottom row, cut to 2 metres, reads 20.0 microwatts. A dashed box around the source and scrambler says the launch is left untouched. The result line gives 2.51 dB per km.')


# ---- 5.5 trigonometric far-field NA measurement ----
def f5():
    o = []
    ex, cy, D, half = 130, 210, 410, 94.3     # 41 px per cm: D = 10.0 cm, A/2 = 2.3 cm
    sx = ex + D
    o.append(R(20, cy - 10, ex - 20, 20, ACS, AC, 4))
    o.append(T(75, cy + 40, 'fiber', 14, fill=MUT))
    o.append(f'<polygon points="{ex},{cy - 6} {sx},{cy - half} {sx},{cy + half} {ex},{cy + 6}" style="fill:var(--accent-soft);stroke:none"/>')
    o.append(L(ex, cy - 6, sx, cy - half, AC, 2)); o.append(L(ex, cy + 6, sx, cy + half, AC, 2))
    o.append(L(ex, cy, sx, cy, L2, 1.5, '6 5'))
    o.append(L(sx, cy - 150, sx, cy + 150, INK, 3))
    o.append(T(sx, cy + 168, 'screen', 13, fill=MUT))
    r = 120
    a = math.atan(half / D)
    o.append(f'<path d="M{ex + r:.1f},{cy:.1f} A{r},{r} 0 0 0 {ex + r * math.cos(a):.1f},{cy - r * math.sin(a):.1f}" style="fill:none;stroke:{NX};stroke-width:2"/>')
    o.append(T(ex + r + 14, cy - 10, 'θ' + sub('a') + '= 12.95°', 14, 'start', fill=NX, bold=True))
    o.append(brace(ex, sx, cy + 130, INK, up=True))
    o.append(T((ex + sx) / 2, cy + 152, 'D = 10.0 cm', 14, bold=True))
    o.append(L(sx + 26, cy - half, sx + 26, cy + half, LV, 2))
    o.append(L(sx + 18, cy - half, sx + 34, cy - half, LV, 2)); o.append(L(sx + 18, cy + half, sx + 34, cy + half, LV, 2))
    o.append(T(sx + 40, cy - 6, 'A = 4.6 cm', 14, 'start', fill=LV, bold=True))
    o.append(T(sx + 40, cy + 14, 'at 5 % of', 13, 'start', fill=MUT))
    o.append(T(sx + 40, cy + 30, 'peak intensity', 13, 'start', fill=MUT))
    o.append(T(330, 30, 'NA = A ÷ √(A² + 4D²) = 4.6 ÷ √(21.16 + 400) = 0.224', 15, bold=True, fill=AC))
    return 400, ''.join(o)

FIG[5] = (f5, 'The trigonometric NA test of the worked example: the far-field cone from the fiber end makes a 4.6 cm spot (at the 5 % intensity edge) on a screen 10.0 cm away, so NA = 0.224 and the acceptance half-angle is 12.95°.',
          'A fiber on the left sends a cone of light to a screen 10.0 centimetres away. The spot on the screen is 4.6 centimetres across, measured at 5 percent of peak intensity. The half-angle of the cone is 12.95 degrees, and the formula at the top gives NA equals 0.224.')

spec = make_spec(FIG)
