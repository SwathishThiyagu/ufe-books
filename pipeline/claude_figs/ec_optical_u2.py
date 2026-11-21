"""Claude's hand-drawn figures for ec-optical-u2 (signal degradation in optical fibers), one per chapter.
Every curve and marked value is computed from that chapter's own worked example; colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
SUB = lambda s: f'<tspan dy="4" font-size="11">{s}</tspan><tspan dy="-4">\u200b</tspan>'
SUP = lambda s: f'<tspan dy="-6" font-size="11">{s}</tspan><tspan dy="6">\u200b</tspan>'


def curve(fn, a, b, fx, fy, n=160, c=AC, w=2.5, dash=None):
    return P([(fx(a + (b - a) * i / n), fy(fn(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


def logaxes(x0, x1, y0, y1, xt, fx, decades, fy, xlab, ylab, xfmt=str, yfmt=str):
    o = [L(x0, y1, x1, y1, L2, 1.5), L(x0, y0, x0, y1, L2, 1.5)]
    for v in xt:
        X = fx(v); o += [L(X, y1, X, y1 + 5, L2, 1.5), T(X, y1 + 20, xfmt(v), 13, fill=MUT)]
    for v in decades:
        Y = fy(v); o += [L(x0 - 5, Y, x0, Y, L2, 1.5), L(x0, Y, x1, Y, LN, 1), T(x0 - 9, Y + 4.5, yfmt(v), 13, 'end', MUT)]
    o.append(T((x0 + x1) / 2, y1 + 42, xlab, 14, fill=MUT))
    o.append(T(x0, y0 - 14, ylab, 14, 'start', MUT))
    return ''.join(o)


def m(v):
    return str(v).replace('-', '−')


# ---- 2.1 received power along the fiber, in dBm (worked example 1) ----
def f1():
    o = []
    x0, x1, y0, y1 = 90, 640, 50, 300
    fx = lambda d: x0 + (x1 - x0) * d / 160
    fy = lambda p: y0 + (y1 - y0) * (-p) / 35
    o.append(axes(x0, x1, y0, y1, [0, 40, 80, 120, 160], [0, -10, -20, -30], fx, fy,
                  'distance along the fiber (km)', 'power (dBm)', yfmt=m))
    o.append(L(fx(0), fy(0), fx(160), fy(-32), AC, 3))
    o.append(L(fx(0), fy(0), fx(100), fy(-35), LV, 2.5, '7 5'))
    o.append(L(x0, fy(-30), x1, fy(-30), NX, 1.6, '4 4'))
    o.append(Tb(x1 - 4, fy(-30) - 8, 'receiver needs 1 µW = −30 dBm', 13, 'end', NX))
    o.append(C(fx(80), fy(-16), 6, AC)); o.append(Tb(fx(80) + 12, fy(-16) - 12, '80 km: −16 dBm = 25.1 µW', 13, 'start', AC, True))
    o.append(C(fx(150), fy(-30), 6, AC)); o.append(L(fx(150), fy(-30), fx(150), y1, AC, 1.4, '3 3'))
    o.append(T(fx(150) - 6, y1 - 8, '150 km', 13, 'end', AC, True))
    o.append(C(fx(0), fy(0), 6, INK)); o.append(T(fx(20), fy(-1.8), 'launch 1 mW = 0 dBm', 13, 'start', INK))
    o.append(T(fx(108), fy(-19), '1550 nm, 0.2 dB/km', 13, 'start', AC, True))
    o.append(Tb(fx(55), fy(-19.25) + 26, '1310 nm, 0.35 dB/km', 13, 'middle', LV, True))
    o.append(C(fx(85.7), fy(-30), 5, LV)); o.append(T(fx(85.7) - 6, fy(-30) + 22, '85.7 km', 13, 'end', LV))
    return 360, ''.join(o)


FIG[1] = (f1, 'On a dBm scale the power falls in a straight line, 0.2 dB for every kilometre at 1550 nm. The 1 mW launch is 25.1 µW (−16 dBm) after 80 km and reaches the 1 µW receiver limit at 150 km; at 0.35 dB/km (1310 nm) the same limit comes at 85.7 km.',
          'Graph of power in dBm against distance: a solid line from 0 dBm falling 0.2 dB per kilometre reaches minus 16 dBm at 80 km and minus 30 dBm at 150 km; a dashed line for 0.35 dB per kilometre reaches minus 30 dBm at 85.7 km.')


# ---- 2.2 loss spectrum built from the chapter's formulas (worked examples 1 and 2) ----
def a_uv(l, x=0.06): return 154.2 * x / (46.6 * x + 60) * 1e-2 * math.exp(4.63 / l)
def a_ir(l): return 7.81e11 * math.exp(-48.48 / l)
def a_r(l): return 0.8 / l ** 4
def a_oh(l): return 0.839 * math.exp(-((l - 1.383) / 0.018) ** 2)


def f2():
    o = []
    x0, x1, y0, y1 = 100, 650, 50, 310
    lo, hi = -2, 1
    fx = lambda l: x0 + (x1 - x0) * (l - 0.8) / (1.75 - 0.8)
    fy = lambda v: y1 - (y1 - y0) * (math.log10(max(v, 1e-3)) - lo) / (hi - lo)
    o.append(logaxes(x0, x1, y0, y1, [0.8, 1.0, 1.2, 1.4, 1.6], fx, [0.01, 0.1, 1, 10], fy,
                     'wavelength (µm)', 'loss (dB/km, log scale)'))
    tot_new = lambda l: a_uv(l) + a_ir(l) + a_r(l)
    o.append(curve(a_r, 0.8, 1.75, fx, fy, c=MUT, w=2, dash='6 4'))
    o.append(curve(lambda l: max(a_uv(l), 0.01), 0.8, 1.75, fx, fy, c=NX, w=2, dash='3 3'))
    o.append(curve(a_ir, 1.52, 1.75, fx, fy, c=NX, w=2, dash='3 3'))
    o.append(curve(lambda l: tot_new(l) + a_oh(l), 0.8, 1.75, fx, fy, n=400, c=LV, w=2.2))
    o.append(curve(tot_new, 0.8, 1.75, fx, fy, n=200, c=AC, w=3))
    o.append(T(fx(0.86), fy(a_r(0.86)) - 12, 'Rayleigh 0.8/λ⁴', 13, 'start', MUT))
    o.append(T(fx(1.05), fy(a_uv(1.05)) + 20, 'UV tail', 13, 'start', NX, True))
    o.append(T(fx(1.62), fy(0.05) + 4, 'IR tail', 13, 'start', NX, True))
    o.append(Tb(fx(1.383) + 10, fy(1.10) - 6, 'old fiber 1.10 dB/km', 13, 'start', LV, True))
    o.append(C(fx(1.383), fy(1.10), 5, LV))
    o.append(C(fx(1.383), fy(tot_new(1.383)), 5, AC))
    o.append(Tb(fx(1.383) - 8, fy(tot_new(1.383)) + 24, 'low water peak 0.26', 13, 'end', AC, True))
    o.append(C(fx(1.55), fy(tot_new(1.55)), 5, AC))
    o.append(Tb(fx(1.55), fy(tot_new(1.55)) + 24, '1.55 µm: 0.19 dB/km', 13, 'middle', AC, True))
    o.append(C(fx(1.70), fy(a_ir(1.70)), 4, NX))
    return 370, ''.join(o)


FIG[2] = (f2, 'The loss of a germania-doped fiber from the chapter’s formulas: the ultraviolet tail and Rayleigh scattering fall with wavelength, the infrared tail rises steeply past 1.6 µm, and the sum has its minimum, about 0.19 dB/km, near 1.55 µm. The old fiber adds the OH⁻ peak at 1383 nm (1.10 dB/km against 0.26 dB/km).',
          'Log-scale loss spectrum from 0.8 to 1.75 micrometres: dashed Rayleigh and ultraviolet curves falling, a dashed infrared curve rising past 1.6 micrometres, a solid total curve with its minimum near 1.55 micrometres, and a second curve with a sharp water peak at 1.383 micrometres.')


# ---- 2.3 Rayleigh and Mie against wavelength (worked example 1) ----
def f3():
    o = []
    x0, x1, y0, y1 = 90, 640, 50, 300
    fx = lambda l: x0 + (x1 - x0) * (l - 800) / (1650 - 800)
    fy = lambda v: y1 - (y1 - y0) * v / 2.2
    o.append(axes(x0, x1, y0, y1, [800, 1000, 1200, 1400, 1600], [0, 0.5, 1.0, 1.5, 2.0], fx, fy,
                  'wavelength (nm)', 'scattering loss (dB/km)', yfmt=lambda v: f'{v:.1f}'))
    ray = lambda l: 0.14 * (1550 / l) ** 4
    o.append(curve(ray, 800, 1650, fx, fy, c=AC, w=3))
    o.append(curve(lambda l: 0.05 * (1000 / l) ** 2, 800, 1650, fx, fy, c=NX, w=2.2, dash='6 4'))
    for l, v, s, dx, dy in [(850, 1.55, '1.55', 50, 8), (1310, 0.274, '0.27', 0, -12), (1550, 0.14, '0.14', 0, -12)]:
        o.append(C(fx(l), fy(v), 6, AC))
        o.append(Tb(fx(l) + dx + 10, fy(v) + dy, s + ' dB/km', 13, 'start', AC, True))
    o.append(C(fx(850), fy(2.0), 6, LV))
    o.append(Tb(fx(850) + 12, fy(2.0) - 6, 'measured total 2.0 dB/km', 13, 'start', LV, True))
    o.append(P([(fx(850) + 14, fy(2.0)), (fx(850) + 20, fy(2.0)), (fx(850) + 20, fy(1.55)), (fx(850) + 14, fy(1.55))], LV, 1.8))
    o.append(T(fx(850) + 26, fy(1.775) + 5, '0.45 left', 13, 'start', LV, True))
    o.append(T(fx(1080), fy(0.05 * (1000 / 1080) ** 2) - 12, 'Mie model 0.05 × (1 µm/λ)²', 13, 'start', NX))
    o.append(T(fx(1040), fy(ray(1040)) - 14, 'Rayleigh ∝ 1/λ⁴', 14, 'start', AC, True))
    return 350, ''.join(o)


FIG[3] = (f3, 'Rayleigh loss scaled from 0.14 dB/km at 1550 nm: 0.27 dB/km at 1310 nm and 1.55 dB/km at 850 nm, where a measured 2.0 dB/km leaves at most 0.45 dB/km for other terms. The Mie term falls too, but only as 1/λ², and stays small.',
          'Graph of scattering loss against wavelength: a steep Rayleigh curve through 1.55, 0.27 and 0.14 dB per kilometre at 850, 1310 and 1550 nanometres, a low dashed Mie curve, and a measured point of 2.0 dB per kilometre at 850 nanometres with a 0.45 gap marked.')


# ---- 2.4 bend loss per turn on a log scale (worked example 1) ----
def f4():
    o = []
    x0, x1, y0, y1 = 100, 640, 50, 300
    fx = lambda R: x0 + (x1 - x0) * (R - 4) / (16 - 4)
    lo, hi = -4, 0
    fy = lambda v: y1 - (y1 - y0) * (math.log10(v) - lo) / (hi - lo)
    o.append(logaxes(x0, x1, y0, y1, [4, 6, 8, 10, 12, 14, 16], fx, [1e-4, 1e-3, 1e-2, 1e-1, 1], fy,
                     'bend radius R (mm)', 'loss per turn (dB, log scale)', yfmt=lambda v: f'{v:g}'))
    a = lambda R: 8 * math.exp(-0.6 * R)
    o.append(curve(a, 4, 15, fx, fy, c=AC, w=3))
    for R, s, dx, dy in [(5, '5 mm: 0.40 dB', 12, -8), (10, '10 mm: 0.020 dB', -10, 22), (15, '15 mm (30 mm mandrel): 0.001 dB', -10, -14)]:
        o.append(C(fx(R), fy(a(R)), 6, AC))
        o.append(Tb(fx(R) + dx, fy(a(R)) + dy, s, 13, 'start' if dx > 0 else 'end', AC, True))
    o.append(Tb(108, 205, 'four turns at 5 mm: 4 × 0.398 = 1.59 dB', 13, 'start', LV, True))
    o.append(T(fx(8.5), 250, 'α' + SUB('r') + ' = 8 e' + SUP('−0.6R') + ' dB per turn at 1550 nm', 14, 'middle', INK, True))
    o.append(T(fx(8.5), 272, 'a straight line on a log scale: every 1.15 mm more radius cuts the loss in half', 13, 'middle', MUT))
    return 350, ''.join(o)


FIG[4] = (f4, 'The fitted bend loss of the worked example on a log scale: 0.40 dB per turn at 5 mm, 0.020 dB at 10 mm and 0.001 dB at 15 mm (a 30 mm mandrel). Four turns at 5 mm cost 1.59 dB.',
          'Log-scale graph of bend loss per turn against bend radius from 4 to 16 millimetres: a straight falling line through 0.40 decibels at 5 millimetres, 0.020 at 10 and 0.001 at 15.')


# ---- 2.5 rays in step and graded cores, with the 5 km delays (worked example 1) ----
def f5():
    o = []
    def core(y, h, lab):
        o.append(R(40, y, 640, h, 'var(--next-soft)', NX, 4))
        o.append(R(40, y + 22, 640, h - 44, PANEL, AC, 2))
        o.append(T(48, y + h - 6, lab, 13, 'start', MUT))
    # step index
    core(30, 130, 'cladding n₂')
    yc = 30 + 65; top, bot = 30 + 22, 30 + 108
    o.append(L(50, yc, 670, yc, AC, 2.5, arrow='n'))
    pts = [(50, yc)]; x = 50; up = True
    while x < 640:
        x += 70; pts.append((min(x, 670), top if up else bot)); up = not up
    o.append(P(pts, LV, 2.2))
    o.append(Tb(360, yc + 5, 'axial ray: 24.67 µs', 13, 'middle', AC, True))
    o.append(T(676, 30 + 16, 'step index', 13, 'end', INK, True))
    # graded index
    core(190, 130, 'graded core: index highest on the axis')
    yc2 = 190 + 65
    o.append(L(50, yc2, 670, yc2, AC, 2.5, arrow='n'))
    pp = [(50 + i * 2.0, yc2 - 38 * math.sin(i * 2.0 * math.pi / 140)) for i in range(311)]
    o.append(P(pp, LV, 2.2))
    o.append(Tb(360, yc2 + 5, 'axial ray: 24.67 µs', 13, 'middle', AC, True))
    o.append(T(676, 190 + 16, 'graded index', 13, 'end', INK, True))
    o.append(T(360, 352, 'step: steepest ray arrives 247 ns later (δT = Ln₁Δ/c)', 14, 'middle', LV, True))
    o.append(T(360, 374, 'graded: curving ray arrives only 0.31 ns later (δT = Ln₁Δ²/8c)', 14, 'middle', LV, True))
    o.append(T(360, 396, 'L = 5 km, n₁ = 1.48, Δ = 0.01', 13, 'middle', MUT))
    return 410, ''.join(o)


FIG[5] = (f5, 'In the step-index core (top) the steepest ray zig-zags at the critical angle and over 5 km falls 247 ns behind the axial ray. In the graded core (bottom) the off-axis ray curves back smoothly through faster, lower-index glass and falls behind by only 0.31 ns.',
          'Two fiber cores 5 kilometres long. Top: a step-index core with a straight axial ray and a zig-zag ray, 247 nanoseconds apart at the end. Bottom: a graded core with a straight axial ray and a smoothly curving ray, 0.31 nanoseconds apart.')


# ---- 2.6 material, waveguide and total dispersion (worked example 2) ----
def Dsmf(l): return 0.092 / 4 * (l - 1310 ** 4 / l ** 3)
def Dm(l): return 0.0986 / 4 * (l - 1270 ** 4 / l ** 3)


def f6():
    o = []
    x0, x1, y0, y1 = 90, 640, 50, 320
    fx = lambda l: x0 + (x1 - x0) * (l - 1200) / (1650 - 1200)
    fy = lambda d: y0 + (y1 - y0) * (25 - d) / 40
    o.append(axes(x0, x1, y0, y1, [1200, 1300, 1400, 1500, 1600], [-10, 0, 10, 20], fx, fy,
                  'wavelength (nm)', 'dispersion (ps/(nm·km))', yfmt=m))
    o.append(L(x0, fy(0), x1, fy(0), INK, 1.4))
    o.append(curve(Dm, 1200, 1650, fx, fy, c=NX, w=2.2, dash='6 4'))
    o.append(curve(lambda l: Dsmf(l) - Dm(l), 1200, 1650, fx, fy, c=LV, w=2.2, dash='3 3'))
    o.append(curve(Dsmf, 1200, 1650, fx, fy, c=AC, w=3))
    o.append(C(fx(1270), fy(0), 5, NX)); o.append(Tb(fx(1270) - 4, fy(0) - 12, 'D' + SUB('m') + ' = 0 at 1270', 13, 'end', NX, True))
    o.append(C(fx(1310), fy(0), 6, AC)); o.append(T(fx(1310) + 8, fy(0) + 46, 'D = 0 at 1310', 13, 'start', AC, True))
    o.append(C(fx(1550), fy(17.46), 6, AC)); o.append(T(fx(1550) + 8, fy(17.46) + 22, 'D = 17.5', 13, 'start', AC, True))
    o.append(C(fx(1550), fy(20.99), 5, NX)); o.append(Tb(fx(1550) - 10, fy(20.99) - 10, 'D' + SUB('m') + ' = 21.0', 13, 'end', NX, True))
    o.append(C(fx(1550), fy(-3.53), 5, LV)); o.append(Tb(fx(1550), fy(-3.53) + 22, 'D' + SUB('w') + ' = −3.5', 13, 'middle', LV, True))
    o.append(T(fx(1615), fy(Dm(1615)) - 10, 'material', 13, 'end', NX))
    o.append(T(fx(1615), fy(Dsmf(1615)) + 20, 'total', 13, 'end', AC, True))
    o.append(T(fx(1225), fy(-3.9) + 30, 'waveguide', 13, 'start', LV))
    return 380, ''.join(o)


FIG[6] = (f6, 'Material dispersion of the glass crosses zero near 1270 nm; the negative waveguide part pulls the total zero to 1310 nm. At 1550 nm the parts are +21.0 and −3.5, giving D = 17.5 ps/(nm·km), the value of worked example 2.',
          'Graph of dispersion against wavelength from 1200 to 1650 nanometres: a dashed material curve crossing zero at 1270, a dashed waveguide curve near minus 3.5, and the solid total crossing zero at 1310 and reaching 17.5 at 1550.')


# ---- 2.7 mean DGD against length (worked examples 1 and 2) ----
def f7():
    o = []
    x0, x1, y0, y1 = 90, 640, 50, 310
    fx = lambda L_: x0 + (x1 - x0) * L_ / 900
    fy = lambda v: y1 - (y1 - y0) * v / 3.5
    o.append(axes(x0, x1, y0, y1, [0, 200, 400, 600, 800], [0, 1, 2, 3], fx, fy, 'length L (km)', 'mean DGD (ps)'))
    o.append(L(x0, fy(2.5), x1, fy(2.5), LV, 1.8, '6 4'))
    o.append(Tb(fx(330), fy(2.5) - 10, '40 Gbit/s limit: 0.1 × 25 ps = 2.5 ps', 13, 'middle', LV, True))
    o.append(curve(lambda L_: 0.1 * math.sqrt(L_), 0, 900, fx, fy, c=AC, w=3))
    o.append(curve(lambda L_: 0.5 * math.sqrt(L_), 0, 49, fx, fy, n=80, c=NX, w=2.5))
    o.append(C(fx(400), fy(2.0), 6, AC)); o.append(Tb(fx(400) + 10, fy(2.0) + 22, '400 km: 2.0 ps', 13, 'start', AC, True))
    o.append(C(fx(625), fy(2.5), 6, AC)); o.append(L(fx(625), fy(2.5), fx(625), y1, AC, 1.4, '3 3'))
    o.append(T(fx(625) + 6, y1 - 10, '625 km', 13, 'start', AC, True))
    o.append(C(fx(25), fy(2.5), 6, NX)); o.append(T(fx(60), fy(3.3), 'old fiber 0.5 ps/√km: 2.5 ps at 25 km', 13, 'start', NX, True))
    o.append(T(fx(740), fy(3.1), 'new fiber 0.1 ps/√km', 13, 'middle', AC, True))
    return 360, ''.join(o)


FIG[7] = (f7, 'The mean DGD grows as √L. On fiber with 0.1 ps/√km it is 2.0 ps at 400 km and reaches the 2.5 ps limit for 40 Gbit/s at 625 km; on old fiber with 0.5 ps/√km the same limit is reached after only 25 km.',
          'Graph of mean differential group delay against length up to 900 kilometres: a square-root curve for 0.1 picoseconds per root kilometre passing 2.0 picoseconds at 400 km and 2.5 at 625 km, a steep curve for 0.5 reaching 2.5 at 25 km, and a dashed limit line at 2.5 picoseconds.')


# ---- 2.8 accumulated dispersion along the span (worked example 1) ----
def f8():
    o = []
    x0, x1, y0, y1 = 100, 620, 50, 300
    fx = lambda d: x0 + (x1 - x0) * d / 125
    fy = lambda v: y1 - (y1 - y0) * v / 1900
    o.append(axes(x0, x1, y0, y1, [0, 25, 50, 75, 100, 125], [0, 500, 1000, 1500], fx, fy,
                  'distance (km)', 'accumulated dispersion (ps/nm)'))
    o.append(f'<rect x="{fx(100):.1f}" y="{y0:.1f}" width="{fx(120) - fx(100):.1f}" height="{y1 - y0:.1f}" style="fill:var(--live-soft);stroke:none"/>')
    o.append(P([(fx(0), fy(0)), (fx(100), fy(1700)), (fx(120), fy(0))], AC, 3))
    o.append(C(fx(100), fy(1700), 6, AC)); o.append(T(fx(100) - 10, fy(1700) - 8, '+17 × 100 km = 1700 ps/nm', 13, 'end', AC, True))
    o.append(C(fx(120), fy(0), 6, AC)); o.append(T(fx(120) + 8, fy(0) - 10, '0 at 120 km', 13, 'start', AC, True))
    o.append(C(fx(115), fy(425), 6, NX)); o.append(Tb(fx(113), fy(425) + 4, 'only 15 km of DCF: 425 ps/nm left', 13, 'end', NX, True))
    o.append(T(fx(30), fy(1150), 'standard fiber: D = +17, 0.2 dB/km', 13, 'middle', AC))
    o.append(T(fx(110), y0 + 18, 'DCF', 14, 'middle', LV, True))
    o.append(T(fx(98), fy(860), 'DCF: D = −85, 0.5 dB/km', 13, 'end', LV, True))
    o.append(T(fx(55), fy(150), 'span loss: 20 dB + 10 dB = 30 dB', 13, 'middle', INK, True))
    return 350, ''.join(o)


FIG[8] = (f8, 'Dispersion builds up along 100 km of standard fiber to 1700 ps/nm, and 20 km of DCF at −85 ps/(nm·km) brings it back to zero; with only 15 km, 425 ps/nm is left. The DCF cancels dispersion, not loss: the span still loses 30 dB.',
          'Graph of accumulated dispersion against distance: a line rising to 1700 picoseconds per nanometre at 100 km, then falling steeply to zero at 120 km through a shaded DCF section; a dashed branch stops at 425 at 115 km.')


# ---- 2.9 signal power along the span, effective length and the two Stokes waves (worked example 1) ----
def f9():
    o = []
    x0, x1, y0, y1 = 90, 640, 150, 340
    fx = lambda z: x0 + (x1 - x0) * z / 80
    fy = lambda p: y1 - (y1 - y0) * p / 1.05
    o.append(axes(x0, x1, y0, y1, [0, 20, 40, 60, 80], [0, 0.5, 1.0], fx, fy, 'distance z (km)', 'signal power P/P₀', yfmt=lambda v: f'{v:.1f}'))
    a = 0.2 / 4.343
    o.append(f'<rect x="{fx(0):.1f}" y="{fy(1):.1f}" width="{fx(21.17) - fx(0):.1f}" height="{fy(0) - fy(1):.1f}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:1.5;stroke-dasharray:5 4"/>')
    o.append(curve(lambda z: math.exp(-a * z), 0, 80, fx, fy, c=AC, w=3))
    o.append(Tb(fx(10.6), fy(0.5), 'L' + SUB('eff') + ' = 21.2 km', 13, 'middle', AC, True))
    o.append(Tb(fx(50), fy(math.exp(-a * 50)) - 14, 'e' + SUP('−αz') + ', 0.2 dB/km', 13, 'middle', AC))
    o.append(T(fx(80) - 4, fy(0.025) - 10, '80 km: 0.025', 13, 'end', MUT))
    # direction arrows above the graph
    o.append(L(220, 46, 600, 46, LV, 2.5, arrow='l'))
    o.append(T(410, 36, 'SRS Stokes wave: forward, 13 THz below, P' + SUB('th') + ' ≈ 0.86 W', 13, 'middle', LV, True))
    o.append(L(600, 84, 220, 84, NX, 2.5, '7 4', 'x'))
    o.append(T(410, 104, 'SBS Stokes wave: backward, 11 GHz below, P' + SUB('th') + ' ≈ 1.6 mW', 13, 'middle', NX, True))
    o.append(boxt(90, 40, 110, 46, ['signal in', '1550 nm'], size=13))
    return 390, ''.join(o)


FIG[9] = (f9, 'The signal fades along the 80 km span, so only the first part drives nonlinear scattering: the dashed rectangle of the same area is the effective length, 21.2 km. Above it, the Raman Stokes wave runs forward and the Brillouin Stokes wave runs back toward the transmitter.',
          'Graph of signal power falling exponentially along an 80 kilometre span, with a dashed rectangle 21.2 kilometres wide of equal area marking the effective length; above the graph a forward arrow for Raman scattering and a dashed backward arrow for Brillouin scattering.')


spec = make_spec(FIG)
