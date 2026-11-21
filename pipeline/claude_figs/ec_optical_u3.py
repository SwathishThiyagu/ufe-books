"""Claude's hand-drawn figures for ec-optical-u3 (Optical sources and transmitters), one per chapter, plus two drawings used
by model answers in the question bank (ANSWER_SVG). Every number comes from the chapter's own worked example: the 850 nm
transition, the dome-LED efficiency chain, the 300 µm Fabry-Perot cavity, the 20 mA / 0.30 W/A L-I line, the 10 nm GaAs
well, the 100 µm LED on a 50 µm core, the joint-loss examples and the Vπ = 4 V modulator. Colours are the shell's CSS
variables only."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
sb = lambda t: f'<tspan baseline-shift="sub" font-size="11">{t}</tspan>'
MK = {AC: 'n', L2: 'm', LV: 'l', NX: 'x'}


def wave(x1, y1, x2, y2, c=LV, amp=5, per=13, w=2.2, arrow=True):
    """a photon: a sine wiggle from (x1, y1) to (x2, y2) ending in a short straight arrow"""
    n = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / n, (y2 - y1) / n
    body = n - 12
    pts = []
    steps = max(8, int(body / 2))
    for i in range(steps + 1):
        s = body * i / steps
        o = amp * math.sin(2 * math.pi * s / per)
        pts.append((x1 + ux * s - uy * o, y1 + uy * s + ux * o))
    pts.append((x2, y2))
    m = f' marker-end="url(#ar-UID-{MK.get(c, "n")})"' if arrow else ''
    return f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:none;stroke:{c};stroke-width:{w};stroke-linejoin:round"{m}/>'


def dot(x, y, r=6, c=AC, hollow=False):
    if hollow:
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2;stroke-dasharray:3 2"/>'
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c};stroke:var(--fig);stroke-width:1.5"/>'


def poly(pts, fill, stroke=AC, sw=2, op=None):
    o = f';fill-opacity:{op}' if op is not None else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}{o}"/>'


def arrowL(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=MK.get(c, 'n'))


# ---------------------------------------------------------------- 3.1 the three processes
def levels(top=26):
    o = []
    W = 224; G = 24
    names = [('Absorption', 'photon lost'), ('Spontaneous emission', 'one photon, random direction'), ('Stimulated emission', 'two identical photons')]
    y2, y1 = top + 52, top + 150
    for i, (nm, note) in enumerate(names):
        x0 = 12 + i * (W + G); x1 = x0 + W; cx = (x0 + x1) / 2
        o.append(R(x0, top, W, 224, FIGBG, L2, 8, 1))
        o.append(T(cx, top + 24, nm, 15, bold=True))
        o.append(L(x0 + 60, y2, x1 - 16, y2, INK, 2.5)); o.append(L(x0 + 60, y1, x1 - 16, y1, INK, 2.5))
        o.append(T(x0 + 52, y2 + 5, 'E2', 14, 'end', bold=True)); o.append(T(x0 + 52, y1 + 5, 'E1', 14, 'end', bold=True))
        ex = x0 + 128
        if i == 0:
            o.append(wave(x0 + 14, y1 - 56, ex - 16, y1 - 56, LV))
            o.append(dot(ex, y1, hollow=True)); o.append(dot(ex, y2))
            o.append(arrowL(ex, y1 - 8, ex, y2 + 10, AC))
        elif i == 1:
            o.append(dot(ex - 20, y2, hollow=True)); o.append(dot(ex - 20, y1))
            o.append(arrowL(ex - 20, y2 + 8, ex - 20, y1 - 10, AC))
            o.append(wave(ex - 8, y2 + 44, x1 - 14, y2 + 6, LV))
            o.append(T(ex + 40, y1 - 14, 'after τ' + sb('sp'), 13, fill=MUT))
        else:
            o.append(wave(x0 + 14, y2 + 36, ex - 12, y2 + 36, LV))
            o.append(dot(ex, y2, hollow=True)); o.append(dot(ex, y1))
            o.append(arrowL(ex, y2 + 8, ex, y1 - 10, AC))
            o.append(wave(ex + 12, y2 + 30, x1 - 12, y2 + 30, LV)); o.append(wave(ex + 12, y2 + 50, x1 - 12, y2 + 50, LV))
        o.append(T(cx + 10, y1 + 30, note, 13, fill=MUT))
        o.append(T(cx + 10, y1 + 52, ['rate B12ρN1', 'rate A21N2', 'rate B21ρN2'][i], 13))
    return o


def f1():
    o = levels()
    o.append(T(360, 280, 'For 850 nm: E2 − E1 = hf = 1.46 eV.  τ' + sb('sp') + ' = 5 ns gives A21 = 2.0×10⁸ s⁻¹.', 14))
    o.append(T(360, 304, 'At 300 K, N2/N1 = exp(−hf/kT) = 2.8×10⁻²⁵: absorption wins until the medium is pumped.', 14, fill=MUT))
    return 318, ''.join(o)


FIG[1] = (f1, 'The three ways light meets a two-level atom, for the 850 nm (1.46 eV) transition of the worked examples. A filled dot is where the electron ends up, '
              'a dashed ring where it started. Only stimulated emission adds a photon that copies the one that came in.',
          'Three panels with levels E2 and E1. Absorption: a photon arrives and the electron rises. Spontaneous emission: the electron falls after tau sp and '
          'one photon leaves in a random direction. Stimulated emission: a photon arrives, the electron falls and two identical photons leave. '
          'Notes: 1.46 electron volts, A21 equals 2 times 10 to the 8 per second, N2 over N1 equals 2.8 times 10 to the minus 25 at 300 kelvin.')


# ---------------------------------------------------------------- 3.2 dome LED and its efficiency chain
def f2():
    o = []
    # planar chip: escape cone versus trapped ray
    o.append(T(88, 26, 'Flat chip', 15, bold=True))
    o.append(R(18, 50, 140, 96, PANEL, AC, 4))
    o.append(L(24, 112, 152, 112, NX, 4))
    o.append(T(88, 166, 'active layer', 13, fill=NX))
    o.append(arrowL(96, 112, 104, 40, LV))
    o.append(P([(46, 112), (96, 50), (146, 112)], MUT, 2, '5 4'))
    o.append(T(88, 192, 'rays past 16° stay inside', 13, fill=MUT))
    # dome
    o.append(T(250, 26, 'Dome', 15, bold=True))
    o.append(R(184, 112, 132, 34, PANEL, AC, 4))
    o.append(f'<path d="M190,112 A60,60 0 0 1 310,112" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
    o.append(L(190, 112, 310, 112, NX, 4))
    for ang in (35, 90, 145):
        a = math.radians(ang)
        o.append(arrowL(250, 112, 250 + 84 * math.cos(a), 112 - 84 * math.sin(a), LV))
    o.append(T(250, 166, 'rays meet it square on,', 13, fill=MUT))
    o.append(T(250, 192, 'so most escape', 13, fill=MUT))
    # efficiency chain (worked example 1)
    x0, w = 350, 352
    rows = [('50 mA drive', '3.13×10¹⁷ electrons/s', PANEL), ('photons made', '2.19×10¹⁷ /s', ACS), ('photons escaping', '4.38×10¹⁶ /s', LVS), ('optical power', '9.8 mW', NXS)]
    mult = ['× η<tspan baseline-shift="sub" font-size="11">int</tspan> = 0.70', '× η<tspan baseline-shift="sub" font-size="11">extraction</tspan> = 0.20', '× 1.4 eV = 2.24×10⁻¹⁹ J']
    y = 16
    for i, (a, b, fl) in enumerate(rows):
        o.append(R(x0, y, w, 40, fl, AC, 8))
        o.append(T(x0 + 12, y + 26, a, 14, 'start', bold=True))
        o.append(T(x0 + w - 12, y + 26, b, 14, 'end'))
        if i < 3:
            o.append(arrowL(x0 + 40, y + 40, x0 + 40, y + 66, AC))
            o.append(T(x0 + 56, y + 58, mult[i], 13, 'start', MUT))
        y += 66
    o.append(T(x0 + w / 2, 286, 'η<tspan baseline-shift="sub" font-size="11">ext</tspan> = 0.70 × 0.20 = 0.14', 14, bold=True))
    o.append(T(176, 240, 'A flat chip in air keeps all but', 13, fill=MUT))
    o.append(T(176, 260, '1/[n(n + 1)²] = 1.3% for n = 3.6', 13, fill=MUT))
    return 300, ''.join(o)


FIG[2] = (f2, 'Left: in a flat chip only rays within about 16° of the normal escape; a dome makes rays meet the surface square on. Right: worked example 1 '
              'step by step: of the 3.13×10¹⁷ electrons injected each second, 14% end as escaping photons, which carry 9.8 mW.',
          'Left, a flat LED chip with one ray escaping and one ray trapped by total internal reflection, and a dome LED whose rays all leave. Right, a chain of boxes: '
          '50 milliamps is 3.13 times 10 to the 17 electrons per second, times 0.70 gives 2.19 times 10 to the 17 photons made, times 0.20 gives 4.38 times 10 to the 16 '
          'photons escaping, times 1.4 electron volts gives 9.8 milliwatts.')


# ---------------------------------------------------------------- 3.3 the cavity and its loss budget
def f3():
    o = []
    # cavity
    xa, xb, yt, yb = 150, 570, 40, 124
    o.append(R(xa, yt + 14, xb - xa, yb - yt - 28, ACS, AC, 4))
    o.append(T((xa + xb) / 2, yt + 38, 'gain medium: modal gain Γg, internal loss α' + sb('i'), 14))
    o.append(T((xa + xb) / 2, yt + 60, 'Γ = 0.30, α' + sb('i') + ' = 10 cm⁻¹', 14, fill=MUT))
    for x in (xa - 8, xb + 2):
        o.append(R(x, yt, 6, yb - yt, NX, NX, 1))
    o.append(T(xa - 14, yt + 46, 'R1 = 0.32', 14, 'end', bold=True)); o.append(T(xb + 18, yt + 46, 'R2 = 0.32', 14, 'start', bold=True))
    o.append(arrowL(xa + 20, yb - 6, xb - 20, yb - 6, LV)); o.append(arrowL(xb - 20, yt + 6, xa + 20, yt + 6, LV))
    o.append(arrowL(xb + 10, yb + 2, xb + 70, yb + 2, LV)); o.append(arrowL(xa - 12, yb + 2, xa - 72, yb + 2, LV))
    o.append(T(xb + 40, yb + 22, 'output', 13, fill=MUT)); o.append(T(xa - 42, yb + 22, 'output', 13, fill=MUT))
    o.append(P([(xa, yb + 30), (xa, yb + 40), (xb, yb + 40), (xb, yb + 30)], INK, 1.5))
    o.append(Tb((xa + xb) / 2, yb + 45, 'L = 300 µm = 0.03 cm', 14))
    # loss budget bar
    y0 = 214; x0, x1 = 120, 660
    fx = lambda v: x0 + (x1 - x0) * v / 50
    o.append(T(20, y0 - 18, 'Loss to beat (cm⁻¹)', 14, 'start', bold=True))
    o.append(R(fx(0), y0, fx(10) - fx(0), 34, LVS, LV, 3))
    o.append(R(fx(10), y0, fx(47.98) - fx(10), 34, NXS, NX, 3))
    o.append(T((fx(0) + fx(10)) / 2, y0 + 22, 'α' + sb('i') + ' = 10', 14))
    o.append(T((fx(10) + fx(47.98)) / 2, y0 + 22, 'mirror loss α' + sb('m') + ' = ln(1/0.1024)/0.06 = 37.98', 14))
    o.append(xaxis(x0, x1, y0 + 46, [0, 10, 20, 30, 40, 50], fx))
    o.append(L(fx(47.98), y0 - 8, fx(47.98), y0 + 46, AC, 2, '5 3'))
    o.append(T(fx(47.98), y0 - 14, 'Γg' + sb('th') + ' = 47.98', 14, 'end', AC, bold=True))
    o.append(T(360, y0 + 102, 'At threshold the modal gain equals this total; the material gain is 47.98/0.30 = 159.9 cm⁻¹.', 14, fill=MUT))
    o.append(T(360, y0 + 126, 'Resonance 2nL = mλ: for a group index of 3.6 the modes are 139 GHz apart.', 14, fill=MUT))
    return 356, ''.join(o)


FIG[3] = (f3, 'The worked example’s cavity: two cleaved facets with R = 0.32 around a 300 µm gain medium. Light runs back and forth and part leaves '
              'each facet. The bar shows the loss the gain must beat: 10 cm⁻¹ inside the medium plus 37.98 cm⁻¹ through the mirrors.',
          'A Fabry-Perot cavity: two mirror facets with reflectance 0.32, 300 micrometres apart, with arrows bouncing between them and output leaving both ends. '
          'Below, a bar from 0 to 50 per centimetre: internal loss 10 and mirror loss 37.98, total 47.98 per centimetre threshold modal gain.')


# ---------------------------------------------------------------- 3.4 the L-I line
def f4():
    o = []
    X0, X1, Y0, Y1 = 80, 560, 40, 290
    fx = lambda i: X0 + (X1 - X0) * i / 70
    fy = lambda p: Y1 - (Y1 - Y0) * p / 15
    o.append(axes(X0, X1, Y0, Y1, [0, 10, 20, 30, 40, 50, 60, 70], [0, 3, 6, 9, 12, 15], fx, fy, 'drive current I (mA)', 'optical power P (mW)'))
    # spontaneous region (drawn just above zero) and lasing line
    o.append(P([(fx(i), fy(0.06 * i / 20)) for i in range(0, 21)], MUT, 2.5))
    o.append(P([(fx(20), fy(0.06)), (fx(70), fy(15))], AC, 3.2))
    o.append(L(fx(20), Y1, fx(20), fy(4.5), L2, 1.5, '5 4'))
    o.append(Tb(fx(20), fy(5.0), 'I' + sb('th') + ' = 20 mA', 14, bold=True))
    o.append(T(fx(9), fy(1.9), 'LED-like:', 13, fill=MUT)); o.append(T(fx(9), fy(1.0), 'a few µW', 13, fill=MUT))
    for i, p in ((40, 6), (60, 12)):
        o.append(L(fx(i), Y1, fx(i), fy(p), L2, 1.5, '4 4')); o.append(L(X0, fy(p), fx(i), fy(p), L2, 1.5, '4 4'))
        o.append(C(fx(i), fy(p), 6, NX))
    o.append(Tb(fx(40) - 10, fy(6) - 12, '40 mA → 6.0 mW', 13, 'end'))
    o.append(Tb(fx(60) - 10, fy(12) - 14, '60 mA → 12.0 mW', 13, 'end'))
    # slope triangle
    o.append(P([(fx(40), fy(6)), (fx(60), fy(6)), (fx(60), fy(12))], LV, 2, '6 3'))
    o.append(Tb(fx(50), fy(6) + 20, 'ΔI = 20 mA', 13, fill=LV))
    o.append(Tb(fx(60) + 8, fy(9) + 4, 'ΔP = 6 mW', 13, 'start', LV))
    # notes
    bx = 590
    o.append(T(bx, 70, 'slope', 14, 'start', bold=True))
    o.append(T(bx, 92, '6 mW / 20 mA', 14, 'start'))
    o.append(T(bx, 114, '= 0.30 W/A', 14, 'start', AC, bold=True))
    o.append(T(bx, 158, 'at 1.31 µm:', 14, 'start', bold=True))
    o.append(T(bx, 180, 'hν/q = 0.947 V', 14, 'start'))
    o.append(T(bx, 202, 'η' + sb('d') + ' = 0.30/0.947', 14, 'start'))
    o.append(T(bx, 224, '= 0.317', 14, 'start', AC, bold=True))
    return 340, ''.join(o)


FIG[4] = (f4, 'Output power against current for the worked example’s laser: almost nothing below the 20 mA threshold, then a straight line of slope '
              '0.30 W/A, so 40 mA gives 6.0 mW and 60 mA gives 12.0 mW. Always subtract the threshold before multiplying by the slope.',
          'A light-current plot from 0 to 70 milliamps and 0 to 15 milliwatts. The output stays near zero up to 20 milliamps, then rises in a straight line. '
          'Points at 40 milliamps, 6 milliwatts and 60 milliamps, 12 milliwatts, with a slope triangle of 6 milliwatts over 20 milliamps, 0.30 watts per amp. '
          'A note gives the differential quantum efficiency 0.317 at 1.31 micrometres.')


# ---------------------------------------------------------------- 3.5 the quantum-well band diagram
def f5():
    o = []
    xa, xb, xc, xd = 60, 300, 420, 660      # cladding | well | cladding
    cb_c, cb_w, vb_w, vb_c = 50, 120, 236, 280  # y of band edges (cladding conduction, well conduction, well valence, cladding valence)
    o.append(R(xb, 30, xc - xb, 270, ACS, ACS, 0, 0))
    o.append(T((xa + xb) / 2, 24, 'p-Al₀.₃Ga₀.₇As', 14, bold=True)); o.append(T((xb + xc) / 2, 24, 'GaAs well', 14, bold=True)); o.append(T((xc + xd) / 2, 24, 'n-Al₀.₃Ga₀.₇As', 14, bold=True))
    o.append(P([(xa, cb_c), (xb, cb_c), (xb, cb_w), (xc, cb_w), (xc, cb_c), (xd, cb_c)], AC, 3))
    o.append(P([(xa, vb_c), (xb, vb_c), (xb, vb_w), (xc, vb_w), (xc, vb_c), (xd, vb_c)], LV, 3))
    o.append(T(xa + 4, cb_c - 8, 'conduction band', 13, 'start', AC)); o.append(T(xa + 4, vb_c + 20, 'valence band', 13, 'start', LV))
    # confined levels
    e1, h1 = cb_w - 22, vb_w + 8
    o.append(L(xb + 6, e1, xc - 6, e1, AC, 2, '6 4')); o.append(L(xb + 6, h1, xc - 6, h1, LV, 2, '6 4'))
    o.append(T(xc + 24, e1 + 4, 'E' + sb('1e') + ' = +0.056 eV', 14, 'start'))
    o.append(T(xc + 24, h1 + 12, 'E' + sb('1h') + ' = 0.0075 eV', 14, 'start'))
    o.append(arrowL(xb + 26, e1 + 4, xb + 26, h1 - 6, AC))
    o.append(wave(xb + 34, 160, xb + 112, 160, NX, 5, 13))
    o.append(T(xb + 70, 190, '1.488 eV', 14, fill=NX, bold=True))
    o.append(T(xb + 70, 210, '833 nm', 14, fill=NX, bold=True))
    # gap annotations
    o.append(L(xa + 150, cb_c + 3, xa + 150, vb_c - 3, L2, 1.5)); o.append(Tb(xa + 150, 170, '1.828 eV', 14))
    o.append(L(xc + 14, cb_w + 3, xc + 14, vb_w - 3, L2, 1.5)); o.append(T(xc + 24, 170, 'bulk GaAs gap', 13, 'start', MUT)); o.append(T(xc + 24, 190, '1.424 eV (871 nm)', 13, 'start', MUT))
    o.append(T((xb + xc) / 2, 318, 'L = 10 nm (drawn wide)', 13, fill=MUT))
    o.append(T((xa + xb) / 2, 318, 'wide gap, low index', 13, fill=MUT)); o.append(T((xc + xd) / 2, 318, 'wide gap, low index', 13, fill=MUT))
    return 334, ''.join(o)


FIG[5] = (f5, 'Band edges across the worked examples’ structure: a 10 nm GaAs well between Al₀.₃Ga₀.₇As claddings. The 1.828 eV cladding gap traps the '
              'carriers; inside the well the lowest levels sit 0.056 eV and 0.0075 eV beyond the band edges, so the photon has 1.488 eV (833 nm) instead of bulk GaAs’s 871 nm.',
          'Energy band diagram: conduction band high in the two AlGaAs claddings and low in the GaAs well, valence band the reverse. Dashed confined levels inside the well, '
          'E1e 0.056 electron volts above the conduction edge and E1h 0.0075 below the valence edge. A photon arrow of 1.488 electron volts, 833 nanometres, '
          'between them. The cladding gap is 1.828 and the bulk GaAs gap 1.424 electron volts.')


# ---------------------------------------------------------------- 3.6 large LED on a small core
def f6():
    o = []
    cy = 150
    s = 1.0                                   # 1 µm = 1 px
    # LED emitting face (radius 100 µm) at x = 150
    xl = 150
    o.append(R(60, cy - 112, xl - 60, 224, PANEL, AC, 4))
    o.append(L(xl, cy - 100 * s, xl, cy + 100 * s, NX, 6))
    o.append(L(xl + 4, cy - 50 * s, xl + 4, cy + 50 * s, LV, 6))
    o.append(T(104, cy - 120, 'LED', 15, bold=True))
    o.append(P([(xl - 14, cy - 100), (xl - 22, cy - 100), (xl - 22, cy), (xl - 14, cy)], INK, 1.5))
    o.append(T(xl - 30, cy - 56, 'r' + sb('s') + ' =', 14, 'end'))
    o.append(T(xl - 30, cy - 36, '100 µm', 13, 'end', MUT))
    # Lambertian fan from one point
    for ang in (-70, -40, -11.5, 0, 11.5, 40, 70):
        a = math.radians(ang); ln = 90 * math.cos(a) + 20
        c = LV if abs(ang) <= 11.5 else L2
        o.append(arrowL(xl + 8, cy, xl + 8 + ln * math.cos(a), cy - ln * math.sin(a), c, 2))
    # fiber at x = 330
    xf = 330
    o.append(R(xf, cy - 92, 360, 184, PANEL, L2, 2))
    o.append(R(xf, cy - 50 * s, 360, 100 * s, ACS, AC, 2))
    o.append(T(xf + 250, cy - 100, 'cladding', 13, fill=MUT))
    o.append(T(xf + 250, cy + 6, 'core, radius 50 µm', 14, bold=True))
    # acceptance cone at the fiber face
    t = math.tan(math.radians(11.54))
    o.append(poly([(xf, cy - 50), (xf - 150, cy - 50 - 150 * t), (xf - 150, cy + 50 + 150 * t), (xf, cy + 50)], LVS, LV, 1.5, 0.6))
    o.append(T(xf - 110, cy - 112, 'acceptance cone', 13, fill=LV))
    o.append(T(xf - 110, cy - 94, 'θ' + sb('a') + ' = 11.5°', 13, fill=LV))
    # numbers
    o.append(T(360, 290, 'area factor (50/100)² = 0.25   ×   NA² = 0.20² = 0.04   →   η = 0.01', 14, bold=True))
    o.append(T(360, 314, '2.0 mW from the LED  ×  0.01  =  20 µW in the fiber;  light outside the cone or off the core is lost', 14, fill=MUT))
    return 330, ''.join(o)


FIG[6] = (f6, 'The worked example to scale: a Lambertian LED face of radius 100 µm butted against a 50 µm-radius core with NA 0.20. Only the central '
              'quarter of the face lies over the core, and only rays inside the 11.5° acceptance cone are guided, so 1% of the 2.0 mW, 20 µW, is launched.',
          'Side view: an LED face 200 micrometres tall emitting a wide fan of rays, of which only those within 11.5 degrees are highlighted, facing a fiber whose core is '
          '100 micrometres tall inside a cladding. The acceptance cone is shaded at the fiber face. Text: area factor 0.25 times NA squared 0.04 gives 0.01, '
          'so 2.0 milliwatts becomes 20 microwatts.')


# ---------------------------------------------------------------- 3.7 the three misalignments
def fib(x0, x1, cy, a, tilt=0.0, piv=None, fill=ACS):
    """a fiber core drawn as a band of half-height a from x0 to x1, optionally tilted about piv (degrees)"""
    if not tilt:
        return R(x0, cy - a, x1 - x0, 2 * a, fill, AC, 2)
    px, py = piv
    return f'<g transform="rotate({-tilt:.1f} {px:.1f} {py:.1f})">' + R(x0, cy - a, x1 - x0, 2 * a, fill, AC, 2) + '</g>'


def f7():
    o = []
    W = 224; G = 24
    heads = ['Lateral offset', 'Tilt', 'End gap']
    for i in range(3):
        x0 = 12 + i * (W + G)
        o.append(R(x0, 8, W, 300, FIGBG, L2, 8, 1))
        o.append(T(x0 + W / 2, 32, heads[i], 15, bold=True))
    cy = 132
    # lateral: a = 50 µm drawn as 40 px, d = 10 µm as 8 px
    x0 = 12
    o.append(fib(x0 + 14, x0 + 110, cy, 40)); o.append(fib(x0 + 112, x0 + 210, cy + 8, 40, fill=LVS))
    o.append(L(x0 + 111, cy - 40, x0 + 111, cy + 48, NX, 2))
    o.append(T(x0 + 112, cy + 70, 'd = 10 µm, a = 50 µm', 13))
    o.append(T(x0 + 112, cy + 96, 'x = d/(2a) = 0.1', 13, fill=MUT))
    o.append(T(x0 + 112, cy + 120, 'η = 0.873', 13, fill=MUT))
    o.append(T(x0 + 112, cy + 150, '0.59 dB', 16, fill=AC, bold=True))
    # tilt: 1° drawn exaggerated as 6°
    x0 = 12 + W + G
    o.append(fib(x0 + 14, x0 + 110, cy, 30)); o.append(fib(x0 + 112, x0 + 210, cy, 30, tilt=6, piv=(x0 + 112, cy), fill=LVS))
    o.append(L(x0 + 112, cy, x0 + 205, cy, L2, 1.5, '4 3'))
    o.append(T(x0 + 186, cy - 2, 'θ', 14, fill=NX, bold=True))
    o.append(T(x0 + 112, cy + 70, 'θ = 1° (drawn larger)', 13))
    o.append(T(x0 + 112, cy + 96, 'a = 25 µm, NA = 0.20', 13, fill=MUT))
    o.append(T(x0 + 112, cy + 120, '1 − θ/(π NA) = 0.972', 13, fill=MUT))
    o.append(T(x0 + 112, cy + 150, '0.12 dB', 16, fill=AC, bold=True))
    # gap: s = 10 µm drawn as 24 px, cone spreads
    x0 = 12 + 2 * (W + G)
    o.append(fib(x0 + 14, x0 + 98, cy, 30)); o.append(fib(x0 + 122, x0 + 210, cy, 30, fill=LVS))
    t = math.tan(math.radians(11.54)) * 2.6
    o.append(poly([(x0 + 98, cy - 30), (x0 + 122, cy - 30 - 24 * t), (x0 + 122, cy + 30 + 24 * t), (x0 + 98, cy + 30)], NXS, NX, 1.5, 0.7))
    o.append(P([(x0 + 98, cy + 44), (x0 + 98, cy + 50), (x0 + 122, cy + 50), (x0 + 122, cy + 44)], INK, 1.5))
    o.append(T(x0 + 112, cy + 70, 's = 10 µm in air', 13))
    o.append(T(x0 + 112, cy + 96, 'cone 11.5°, kept 0.855', 13, fill=MUT))
    o.append(T(x0 + 112, cy + 120, 'two faces add 0.33 dB', 13, fill=MUT))
    o.append(T(x0 + 112, cy + 150, '0.68 dB', 16, fill=AC, bold=True))
    return 318, ''.join(o)


FIG[7] = (f7, 'The three alignment errors of the worked examples, each with its loss. A 10 µm sideways shift of a 100 µm core costs 0.59 dB; a 1° tilt '
              'of a 50 µm, NA 0.20 core costs 0.12 dB; a 10 µm air gap lets the light spread past the far core for 0.68 dB, plus 0.33 dB of Fresnel loss.',
          'Three panels of two fiber cores meeting. Lateral offset: the second core shifted down by d equals 10 micrometres, loss 0.59 decibels. '
          'Tilt: the second core tilted by theta, 1 degree, loss 0.12 decibels. End gap: a 10 micrometre gap with a spreading cone of light, loss 0.68 decibels, '
          'and two faces adding 0.33 decibels.')


# ---------------------------------------------------------------- 3.8 the modulator and its transfer curve
def f8():
    o = []
    # layout
    y0, ya, yb = 92, 62, 122
    o.append(T(18, 20, 'Push-pull Mach-Zehnder modulator', 15, 'start', bold=True))
    o.append(P([(30, y0), (130, y0), (190, ya), (450, ya), (510, y0), (690, y0)], AC, 5))
    o.append(P([(130, y0), (190, yb), (450, yb), (510, y0)], AC, 5))
    o.append(R(220, ya - 22, 200, 12, NXS, NX, 2)); o.append(R(220, yb + 10, 200, 12, NXS, NX, 2))
    o.append(R(220, y0 - 7, 200, 14, LVS, LV, 2))
    o.append(T(430, ya - 12, '+V/2', 13, 'start', NX)); o.append(T(430, yb + 22, '−V/2', 13, 'start', NX))
    o.append(T(320, y0 + 5, 'ground', 12, fill=LV))
    o.append(T(32, y0 + 26, 'P' + sb('in') + ' = 2.0 mW', 14, 'start'))
    o.append(T(690, y0 + 26, 'P' + sb('out') + ' = P' + sb('in') + 'cos²(Δφ/2)', 14, 'end'))
    o.append(T(160, ya - 6, 'φ1', 13, fill=MUT)); o.append(T(160, yb + 18, 'φ2', 13, fill=MUT))
    # curve
    X0, X1, Y0, Y1 = 80, 560, 206, 356
    fx = lambda v: X0 + (X1 - X0) * v / 8
    fy = lambda p: Y1 - (Y1 - Y0) * p / 2
    o.append(axes(X0, X1, Y0, Y1, [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 0.5, 1.0, 1.5, 2.0], fx, fy, 'drive voltage V (V)', '', lambda v: f'{v:g}', lambda v: f'{v:.1f}'))
    o.append(T(X0 - 60, Y0 - 24, 'P' + sb('out') + ' (mW)', 14, 'start', MUT))
    o.append(P([(fx(v / 20), fy(2 * math.cos(math.pi * (v / 20) / 8) ** 2)) for v in range(0, 161)], AC, 3))
    for v, p, lab, anc, dx in ((0, 2.0, 'V = 0: 2.0 mW', 'start', 14), (2, 1.0, 'quadrature, 2 V: 1.0 mW', 'start', 12), (4, 0.0, 'Vπ = 4 V: null', 'start', 10)):
        o.append(C(fx(v), fy(p), 6, NX))
        o.append(Tb(fx(v) + dx, fy(p) - 10 if p > 0 else fy(p) - 14, lab, 13, anc))
    bx = 590
    o.append(T(bx, 236, 'Δφ = πV/Vπ', 14, 'start', bold=True))
    o.append(T(bx, 262, 'P' + sb('out') + ' =', 14, 'start'))
    o.append(T(bx, 286, 'P' + sb('in') + ' cos²(πV/8)', 14, 'start'))
    o.append(T(bx, 326, 'period 2Vπ = 8 V', 13, 'start', MUT))
    return 410, ''.join(o)


FIG[8] = (f8, 'Top: the light splits into two arms whose electrodes are driven with opposite voltages, and the arms recombine. Bottom: the worked '
              'example’s transfer curve for Vπ = 4 V and 2.0 mW input: full output at 0 V, 1.0 mW at the 2 V quadrature point, and a null at 4 V.',
          'Top, a Mach-Zehnder waveguide: input splits into two arms with electrodes at plus V over 2 and minus V over 2, then recombines to the output. '
          'Bottom, output power against drive voltage from 0 to 8 volts: a cosine-squared curve from 2 milliwatts at 0 volts, through 1 milliwatt at 2 volts, '
          'to zero at 4 volts and back to 2 milliwatts at 8 volts.')


# ---------------------------------------------------------------- drawings for model answers
def leds_svg():
    o = []
    # surface emitter (Burrus): fiber in an etched well above a small active disc
    o.append(T(170, 22, 'Surface emitter (Burrus)', 15, bold=True))
    o.append(R(40, 100, 260, 70, PANEL, AC, 4))
    o.append(R(40, 60, 100, 40, PANEL, AC, 2)); o.append(R(200, 60, 100, 40, PANEL, AC, 2))
    o.append(R(146, 36, 48, 64, ACS, AC, 2))
    o.append(T(170, 54, 'fiber', 13))
    o.append(L(150, 104, 190, 104, NX, 5))
    o.append(T(170, 194, 'small active disc, light up', 13, fill=MUT))
    o.append(T(250, 86, 'substrate', 13, fill=MUT))
    o.append(R(150, 172, 40, 6, LV, LV, 1)); o.append(T(170, 214, 'contact', 13, fill=LV))
    o.append(arrowL(170, 100, 170, 72, LV))
    # edge emitter: stripe, light out of the edge
    o.append(T(530, 22, 'Edge emitter', 15, bold=True))
    o.append(R(400, 60, 220, 110, PANEL, AC, 4))
    o.append(R(400, 104, 220, 22, ACS, AC, 1))
    o.append(L(400, 115, 620, 115, NX, 4))
    o.append(R(470, 52, 80, 8, LV, LV, 1)); o.append(T(510, 46, 'stripe contact', 13, fill=LV))
    o.append(arrowL(624, 115, 700, 115, LV)); o.append(arrowL(624, 115, 690, 95, L2)); o.append(arrowL(624, 115, 690, 135, L2))
    o.append(T(510, 194, 'guide layers carry light to the edge', 13, fill=MUT))
    o.append(T(660, 160, '≈ 30° wide', 13, fill=MUT))
    return {'h': 226, 'body': ''.join(o), 'aria': 'Two LED cross-sections. Left, a Burrus surface emitter: a fiber sits in a well etched in the substrate, right above a small active disc. '
                                                  'Right, an edge emitter: a stripe contact over guide layers, with light leaving the cleaved edge in a narrower beam.'}


ANSWER_SVG = {
    'LEVELS': {'h': 252, 'body': ''.join(levels(top=8)), 'aria': 'Energy-level diagrams for absorption, spontaneous emission and stimulated emission between levels E1 and E2.'},
    'LEDS': leds_svg(),
}

spec = make_spec(FIG)


def text_fixes(k):
    return {4: [('Below threshold the idealised curve of the figure is zero; a real diode still shows a weak spontaneous tail of a few microwatts.',
                 'Below threshold the curve in the figure sits almost on the axis: the diode gives only a weak spontaneous tail of a few microwatts.')]}.get(k, [])
