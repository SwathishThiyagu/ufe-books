"""Claude's hand-drawn figures for ch-mass-u1 (Mass Transfer Operations: molecular diffusion and diffusivity), one per chapter,
drawn from each chapter's own worked example. Every plotted value is computed here from the example's data. Colours are the
shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG, AFTER = {}, {}


def sb(base, s):
    return f'{base}<tspan baseline-shift="sub" font-size="11">{s}</tspan>'


SUP = str.maketrans('-0123456789', '⁻⁰¹²³⁴⁵⁶⁷⁸⁹')


def sci(v, d=3):
    """1.58e-05 -> 1.58×10⁻⁵"""
    m, e = f'{v:.{d}g}'.split('e') if 'e' in f'{v:.{d}g}' else (f'{v:.{d}g}', None)
    if e is None:
        e = math.floor(math.log10(abs(v))); m = f'{v / 10 ** e:.{d}g}'
    return f'{m}×10{str(int(e)).translate(SUP)}'


_SUBRE = __import__('re').compile(r'(?<![A-Za-z0-9_.#=])([A-Za-z]{1,2})_([A-Za-z0-9]+(?:,[A-Za-z0-9]+)?)')


def capsub(s):
    s = _SUBRE.sub(lambda m: m.group(1) + '<sub>' + m.group(2) + '</sub>', s)
    return s.replace(')lm', ')<sub>lm</sub>')


def logaxis(x0, x1, y, lo, hi, lab):
    """horizontal log axis from 10^lo to 10^hi"""
    fx = lambda v: x0 + (math.log10(v) - lo) / (hi - lo) * (x1 - x0)
    o = [L(x0, y, x1, y, L2, 1.5)]
    for e in range(lo, hi + 1):
        X = fx(10 ** e)
        o += [L(X, y, X, y + 5, L2, 1.5), T(X, y + 20, f'10<tspan baseline-shift="super" font-size="10">{neg(e)}</tspan>', 13, fill=MUT)]
    o.append(T((x0 + x1) / 2, y + 42, lab, 14, fill=MUT))
    return ''.join(o), fx


# ---- 1.1 the four families, and the flue gas of the worked example ----
def f1():
    o = [boxt(250, 12, 220, 38, ['Mass transfer operations'], ACS, AC, 15, True)]
    fams = [('Phase creation', 'heat makes it', ['distillation', 'evaporation', 'crystallization', 'drying']),
            ('Phase addition', 'a solvent is added', ['absorption', 'stripping', 'extraction', 'leaching']),
            ('Barrier', 'a membrane sorts', ['reverse osmosis', 'dialysis', 'gas permeation']),
            ('Solid agent', 'a solid takes it up', ['adsorption', 'ion exchange'])]
    for i, (name, how, ops) in enumerate(fams):
        x = 14 + i * 176
        o.append(L(360, 50, x + 80, 84, AC, 1.8, arrow='n'))
        hi = i == 1
        o.append(R(x, 88, 160, 150, ACS if hi else PANEL, LV if hi else AC, 8, 2.5 if hi else 2))
        o.append(T(x + 80, 110, name, 14, 'middle', INK, True))
        o.append(T(x + 80, 129, how, 13, 'middle', MUT, False, True))
        for j, op in enumerate(ops):
            c = LV if (hi and op == 'absorption') else INK
            o.append(T(x + 80, 154 + j * 21, op, 13, 'middle', c, hi and op == 'absorption'))
    # worked example panel
    o.append(L(270, 238, 270, 268, LV, 2, arrow='l'))
    o.append(T(280, 258, 'CO₂ into an amine solution: absorption', 13, 'start', LV, True))
    o.append(R(14, 272, 692, 138, PANEL, L2, 8, 1.5))
    o.append(T(30, 296, 'Worked example: flue gas at 1 atm and 300 K with 22 mol% CO₂', 14, 'start', INK, True))
    x0, w = 200, 300
    for j, (lab, v, c, f) in enumerate([('mole fraction y', 0.22, NX, NXS), ('mass fraction w', 0.300, AC, ACS)]):
        y = 312 + j * 34
        o.append(T(x0 - 10, y + 17, lab, 13, 'end', INK))
        o.append(R(x0, y, w, 24, FIGBG, L2, 4, 1.2))
        o.append(R(x0, y, w * v, 24, f, c, 4))
        o.append(T(x0 + w * v + 8, y + 17, f'{v:.2f}' if j == 0 else '0.300', 13, 'start', c, True))
    o.append(T(530, 329, 'c = 40.6 mol/m³', 13, 'start', INK))
    o.append(T(530, 351, 'CO₂: 8.93 mol/m³', 13, 'start', INK))
    o.append(T(530, 373, '= 0.393 kg/m³', 13, 'start', INK, True))
    o.append(T(30, 398, 'CO₂ is 22 % of the moles but 30 % of the mass: each molecule (44 g/mol) outweighs the mean (32.3 g/mol).', 13, 'start', MUT))
    return 420, ''.join(o)


FIG[1] = (f1, 'The four families, sorted by how the second phase is obtained, with their usual members. The worked example sits under phase addition: CO₂ leaves the flue gas for an amine solution, and the bars show why its mass fraction (0.300) exceeds its mole fraction (0.22).',
          'Tree from mass transfer operations to four boxes: phase creation (distillation, evaporation, crystallization, drying), phase addition (absorption highlighted, stripping, extraction, leaching), barrier (reverse osmosis, dialysis, gas permeation) and solid agent (adsorption, ion exchange). Below, the flue gas example: mole fraction 0.22, mass fraction 0.300, c 40.6 mol per cubic metre, CO2 8.93 mol per cubic metre or 0.393 kg per cubic metre.')
AFTER[1] = 2


# ---- 1.2 velocities and fluxes of the worked example ----
def f2():
    o = []
    x0, sc = 150, 170  # px per 1e-4 m/s
    o.append(T(20, 28, 'Velocities (×10⁻⁴ m/s)', 14, 'start', INK, True))
    o.append(xaxis(x0, x0 + 3 * sc, 150, [0, 0.5, 1, 1.5, 2, 2.5, 3], lambda v: x0 + v * sc, fmt=lambda v: f'{v:g}'))
    o.append(L(x0, 60, x0 + 0.985 * sc, 60, NX, 2.5, arrow='x'))
    o.append(T(x0 - 10, 65, 'u', 14, 'end', NX, True)); o.append(T(x0 + 0.985 * sc + 10, 65, '0.985 (molar average)', 13, 'start', NX))
    o.append(L(x0, 96, x0 + 2.46 * sc, 96, AC, 2.5, arrow='n'))
    o.append(T(x0 - 10, 101, sb('v', 'A'), 14, 'end', AC, True)); o.append(T(x0 + 2.46 * sc + 8, 101, '2.46', 13, 'start', AC, True))
    o.append(L(x0 + 0.985 * sc, 126, x0 + 2.46 * sc, 126, LV, 2.5, arrow='l'))
    o.append(L(x0 + 0.985 * sc, 70, x0 + 0.985 * sc, 134, L2, 1.2, '4 3'))
    o.append(T(x0 + 0.985 * sc - 8, 131, sb('v', 'A') + ' − u = 1.48', 13, 'end', LV, True))
    # fluxes
    y0 = 214
    o.append(T(20, y0, 'Fluxes (×10⁻³ mol/m²·s): fixed-frame flux = bulk part + diffusion part', 14, 'start', INK, True))
    sc2 = 150
    xa = 150
    o.append(xaxis(xa, xa + 3 * sc2, y0 + 128, [0, 1, 2, 3], lambda v: xa + v * sc2, fmt=lambda v: f'{v:g}'))
    # A: bulk 0 -> 1.2, J_A 1.2 -> 3.0
    ya = y0 + 34
    o.append(L(xa, ya, xa + 1.2 * sc2, ya, NX, 2.5, arrow='x'))
    o.append(L(xa + 1.2 * sc2, ya, xa + 3.0 * sc2, ya, AC, 2.5, arrow='n'))
    o.append(T(xa - 10, ya + 5, 'A', 14, 'end', INK, True))
    o.append(Tb(xa + 0.6 * sc2, ya - 10, 'bulk 0.30 × 4.0 = 1.2', 13, 'middle', NX))
    o.append(Tb(xa + 2.1 * sc2, ya - 10, sb('J', 'A') + ' = 1.8', 13, 'middle', AC, True))
    o.append(T(xa + 3.0 * sc2 + 10, ya + 5, sb('N', 'A') + ' = 3.0', 13, 'start', AC, True))
    # B: bulk 0 -> 2.8, J_B 2.8 -> 1.0
    yb = y0 + 88
    o.append(L(xa, yb, xa + 2.8 * sc2, yb, NX, 2.5, arrow='x'))
    o.append(L(xa + 2.8 * sc2, yb + 12, xa + 1.0 * sc2, yb + 12, LV, 2.5, arrow='l'))
    o.append(T(xa - 10, yb + 10, 'B', 14, 'end', INK, True))
    o.append(Tb(xa + 1.4 * sc2, yb - 10, 'bulk 0.70 × 4.0 = 2.8', 13, 'middle', NX))
    o.append(Tb(xa + 1.9 * sc2, yb + 32, sb('J', 'B') + ' = −1.8', 13, 'middle', LV, True))
    o.append(C(xa + 1.0 * sc2, yb + 12, 5, LV))
    o.append(T(xa + 1.0 * sc2 - 10, yb + 17, sb('N', 'B') + ' = 1.0', 13, 'end', LV, True))
    return y0 + 180, ''.join(o)


FIG[2] = (f2, 'The worked example drawn to scale. Top: A moves at 2.46×10⁻⁴ m/s, the mixture at 0.985×10⁻⁴ m/s, so A drifts through it at 1.48×10⁻⁴ m/s. Bottom: each fixed-frame flux is the bulk part y(N_A + N_B) plus the diffusion part; J_A = 1.8 and J_B = −1.8 cancel, while N_A = 3.0 and N_B = 1.0 do not.',
          'Top, three arrows on a velocity scale in units of 1e-4 m/s: molar average u 0.985, species velocity of A 2.46, and the diffusion velocity 1.48 from the tip of u to the tip of v_A. Bottom, flux scale in units of 1e-3 mol per square metre per second: for A a bulk arrow to 1.2 then a diffusion arrow to 3.0; for B a bulk arrow to 2.8 then a diffusion arrow back to 1.0.')
AFTER[2] = 2


# ---- 1.3 straight profile and the slab balance ----
def f3():
    o = []
    x0, x1, y0, y1 = 80, 380, 50, 270
    fx = lambda z: x0 + z / 4 * (x1 - x0)
    fy = lambda y: y1 - y / 0.35 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3, 4], [0, 0.1, 0.2, 0.3], fx, fy, 'z (mm)', 'mole fraction of A', lambda v: f'{v:g}', lambda v: f'{v:.1f}'))
    o.append(P([(fx(0), fy(0.30)), (fx(4), fy(0.10))], AC, 3))
    o.append(C(fx(0), fy(0.30), 5)); o.append(C(fx(4), fy(0.10), 5))
    o.append(Tb(fx(0) + 12, fy(0.30) - 12, '0.30', 13, 'start', AC, True))
    o.append(Tb(fx(4) - 8, fy(0.10) - 14, '0.10', 13, 'end', AC, True))
    o.append(L(fx(1.2), fy(0.06), fx(2.8), fy(0.06), LV, 3, arrow='l'))
    o.append(Tb(fx(2.0), fy(0.06) - 12, sb('J', 'A') + ' = 3.65×10⁻² mol/m²·s', 13, 'middle', LV, True))
    o.append(T(fx(2.0), fy(0.30) - 4, 'slope −50 per metre', 13, 'start', MUT))
    o.append(T(fx(2.0), fy(0.30) + 14, sb('dc', 'A') + '/dz = −2030 mol/m⁴', 13, 'start', MUT))
    # slab balance
    X0 = 450
    o.append(R(X0 + 70, 70, 90, 170, ACS, AC, 4))
    o.append(T(X0 + 115, 152, 'S Δz', 14, 'middle', INK, True))
    o.append(T(X0 + 115, 172, '∂c/∂t', 14, 'middle', INK, True))
    o.append(L(X0 + 10, 120, X0 + 66, 120, LV, 3, arrow='l'))
    o.append(T(X0 + 38, 108, sb('J', 'A') + '(z)', 13, 'middle', LV, True))
    o.append(L(X0 + 164, 120, X0 + 230, 120, LV, 3, arrow='l'))
    o.append(T(X0 + 200, 108, sb('J', 'A') + '(z + Δz)', 13, 'middle', LV, True))
    o.append(T(X0 + 70, 262, 'z', 13, 'middle', MUT)); o.append(T(X0 + 160, 262, 'z + Δz', 13, 'middle', MUT))
    o.append(T(X0 + 115, 40, 'in − out = gain', 14, 'middle', INK, True))
    o.append(T(X0 + 115, 300, '∂c/∂t = D ∂²c/∂z²', 14, 'middle', AC, True))
    o.append(T(X0 + 115, 320, 'straight line: ∂²c/∂z² = 0', 13, 'middle', MUT))
    return 340, ''.join(o)


FIG[3] = (f3, 'Left: the worked example, a straight profile from y_A = 0.30 to 0.10 over 4 mm, which carries J_A = 3.65×10⁻² mol/(m²·s) towards +z. Right: the slab balance behind the second law; on a straight line the flux in equals the flux out, so nothing accumulates.',
          'Left, plot of mole fraction of A against z from 0 to 4 mm, a straight line from 0.30 to 0.10, with the gradient minus 2030 mol per m4 and the flux 3.65e-2 mol per square metre per second. Right, a thin slab with flux in at z, flux out at z plus delta z, and accumulation S delta z times dc/dt, leading to dc/dt = D d2c/dz2.')
AFTER[3] = 2


# ---- 1.4 equimolar versus stagnant B profiles ----
def f4():
    o = []
    x0, x1, y0, y1 = 80, 420, 50, 290
    fx = lambda z: x0 + z / 5 * (x1 - x0)
    fy = lambda y: y1 - (y - 0.0) / 0.25 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3, 4, 5], [0, 0.05, 0.10, 0.15, 0.20, 0.25], fx, fy, 'z (mm)', 'mole fraction of A', lambda v: f'{v:g}', lambda v: f'{v:.2f}'))
    zs = [i * 5 / 40 for i in range(41)]
    o.append(P([(fx(z), fy(0.20 - 0.15 * z / 5)) for z in zs], NX, 2.5, '7 4'))
    o.append(P([(fx(z), fy(1 - 0.80 * (0.95 / 0.80) ** (z / 5))) for z in zs], AC, 3))
    o.append(C(fx(2.5), fy(0.128), 4.5)); o.append(C(fx(2.5), fy(0.125), 4.5, NX))
    o.append(L(fx(2.5) + 6, fy(0.128) - 2, fx(3.3), fy(0.185), AC, 1.4))
    o.append(T(fx(3.35), fy(0.19), 'stagnant B: 0.128', 13, 'start', AC, True))
    o.append(L(fx(2.5) - 4, fy(0.125) + 6, fx(1.6), fy(0.07), NX, 1.4))
    o.append(T(fx(1.55), fy(0.06), 'equimolar: 0.125', 13, 'end', NX, True))
    o.append(T(fx(0) + 8, fy(0.20) - 10, '0.20', 13, 'start', INK, True))
    o.append(T(fx(5) - 6, fy(0.05) + 22, '0.05', 13, 'end', INK, True))
    # flux bars
    X0, sc = 500, 6000
    o.append(T(600, 70, 'flux of A (mol/m²·s)', 14, 'middle', INK, True))
    for i, (lab, v, c, f) in enumerate([('equimolar', 0.0219, NX, NXS), ('stagnant B', 0.0251, AC, ACS)]):
        y = 100 + i * 70
        o.append(T(X0, y - 6, lab, 13, 'start', c, True))
        o.append(R(X0, y, v * sc, 30, f, c, 4))
        o.append(T(X0 + v * sc + 6, y + 21, f'{v:.4f}', 13, 'start', c, True))
    o.append(T(600, 262, '0.0251 / 0.0219 = 1.146', 13, 'middle', INK))
    o.append(T(600, 282, '= 1/(y_B)lm with (y_B)lm = 0.873'.replace('y_B', sb('y', 'B')).replace(')lm', ')' + '<tspan baseline-shift="sub" font-size="11">lm</tspan>'), 13, 'middle', MUT))
    return 340, ''.join(o)


FIG[4] = (f4, 'The worked example: the same end values, 0.20 and 0.05, across 5 mm. With B stagnant the profile is exponential and bows slightly above the straight equimolar line (0.128 against 0.125 at mid-film), and the flux is 1/(y_B)lm = 1.146 times larger.',
          'Plot of mole fraction of A against z from 0 to 5 mm: a dashed straight line for equimolar counter-diffusion and a solid curve for stagnant B, both from 0.20 to 0.05, with mid-film values 0.125 and 0.128. Beside it, two flux bars: 0.0219 equimolar and 0.0251 stagnant B, ratio 1.146.')
AFTER[4] = 2


# ---- 1.5 shrinking naphthalene ball ----
def f5():
    o = []
    k = 6.1e-6 * (101325 / (8.314 * 298)) * math.log(1 / (1 - 11 / 101325)) * 0.128 / 1140
    tend = 1e-4 / (2 * k) / 86400
    t5 = (1e-4 - 2.5e-5) / (2 * k) / 86400
    x0, x1, y0, y1 = 80, 520, 50, 290
    fx = lambda d: x0 + d / 200 * (x1 - x0)
    fy = lambda r: y1 - r / 10 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 50, 100, 150, 200], [0, 2, 4, 6, 8, 10], fx, fy, 'time (days)', 'radius (mm)', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    pts = []
    for i in range(81):
        d = tend * i / 80
        r2 = 1e-4 - 2 * k * d * 86400
        pts.append((fx(d), fy(math.sqrt(max(r2, 0)) * 1000)))
    o.append(P(pts, AC, 3))
    o.append(L(fx(0), fy(5), fx(t5), fy(5), L2, 1.5, '5 4')); o.append(L(fx(t5), fy(5), fx(t5), y1, L2, 1.5, '5 4'))
    o.append(C(fx(t5), fy(5), 5, LV))
    o.append(Tb(fx(t5) + 10, fy(5) - 10, '5 mm after 143 days', 13, 'start', LV, True))
    o.append(C(fx(tend), fy(0), 4, MUT))
    o.append(T(fx(10), fy(8.0), 'starts at 10 mm', 13, 'start', INK))
    # ball sketch
    cx, cy = 625, 150
    o.append(f'<circle cx="{cx}" cy="{cy}" r="40" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2.5"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="20" style="fill:none;stroke:var(--accent);stroke-width:1.5;stroke-dasharray:4 3"/>')
    for a in range(0, 360, 45):
        r = math.radians(a)
        o.append(L(cx + 44 * math.cos(r), cy + 44 * math.sin(r), cx + 70 * math.cos(r), cy + 70 * math.sin(r), LV, 1.8, arrow='l'))
    o.append(T(cx, 246, sb('y', 's') + ' = 1.09×10⁻⁴ (11 Pa)', 13, 'middle', INK))
    o.append(T(cx, 266, 'k = 3.04×10⁻¹² m²/s', 13, 'middle', INK))
    o.append(T(cx, 286, 'R² = R₁² − 2kt', 13, 'middle', AC, True))
    return 340, ''.join(o)


FIG[5] = (f5, 'The mothball of the worked example: its radius follows R² = R₁² − 2kt, so it shrinks slowly at first and fast at the end. It halves to 5 mm after 143 days and would vanish after about 190 days, because the vapour pressure at the surface is only 11 Pa.',
          'Plot of radius in mm against time in days from 0 to 200: a curve from 10 mm falling slowly then steeply to zero near 190 days, with the point 5 mm at 143 days marked. Beside it, a sphere with vapour arrows leaving it, surface mole fraction 1.09e-4, k 3.04e-12 square metres per second, and R squared = R1 squared minus 2kt.')
AFTER[5] = 3


# ---- 1.6 diffusivities on one log scale ----
def f6():
    o = []
    ax, fx = logaxis(150, 690, 300, -10, -4, 'diffusivity D (m²/s), log scale')
    o.append(ax)
    rows = [('gas: Fuller', 'CO₂ in air, 300 K', 1.58e-5, AC, ACS), ('gas: Winkelmann', 'CCl₄ in air, 321 K', 9.0e-6, AC, ACS),
            ('liquid: Wilke–Chang', 'ethanol in water, 298 K', 1.47e-9, NX, NXS), ('liquid: measured', 'ethanol in water, 298 K', 1.24e-9, NX, NXS),
            ('Stokes–Einstein', '0.5 nm solute, 1 cP', 4.4e-10, LV, LVS)]
    for i, (lab, sub, v, c, f) in enumerate(rows):
        y = 30 + i * 52
        o.append(T(140, y + 14, lab, 13, 'end', INK, True))
        o.append(T(140, y + 31, sub, 12 + 1, 'end', MUT))
        o.append(R(150, y + 4, fx(v) - 150, 26, f, c, 4))
        o.append(T(fx(v) + 6, y + 22, sci(v), 13, 'start', c, True))
    return 350, ''.join(o)


FIG[6] = (f6, 'The chapter\'s values on one log scale. The Fuller estimate for CO₂ in air and the Winkelmann value for CCl₄ sit near 10⁻⁵ m²/s; the Wilke–Chang estimate for ethanol in water (18 % above the measured value) and the Stokes–Einstein estimate sit four orders of magnitude lower.',
          'Horizontal log-scale bar chart of diffusivity from 1e-10 to 1e-4 square metres per second: CO2 in air by Fuller 1.58e-5, CCl4 in air by Winkelmann 9.0e-6, ethanol in water by Wilke-Chang 1.47e-9, measured 1.24e-9, and a 0.5 nm solute by Stokes-Einstein 4.4e-10.')
AFTER[6] = 3


# ---- 1.7 Arrhenius line and the porous pellet ladder ----
def f7():
    o = []
    D0, E = 2.0e-5, 60000
    Dt = lambda T_: D0 * math.exp(-E / (8.314 * T_))
    x0, x1, y0, y1 = 80, 380, 50, 280
    fx = lambda T_: x0 + (T_ - 600) / 250 * (x1 - x0)
    fy = lambda v: y1 - (math.log10(v) + 11) / 3 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for T_ in (600, 650, 700, 750, 800, 850):
        o += [L(fx(T_), y1, fx(T_), y1 + 5, L2, 1.5), T(fx(T_), y1 + 20, str(T_), 13, fill=MUT)]
    for e in (-11, -10, -9, -8):
        o += [L(x0 - 5, fy(10 ** e), x0, fy(10 ** e), L2, 1.5), L(x0, fy(10 ** e), x1, fy(10 ** e), LN, 1),
              T(x0 - 9, fy(10 ** e) + 4.5, f'10<tspan baseline-shift="super" font-size="10">{neg(e)}</tspan>', 13, 'end', MUT)]
    o.append(T((x0 + x1) / 2, y1 + 40, 'temperature (K)', 14, fill=MUT)); o.append(T(x0, y0 - 12, 'D (m²/s), log scale', 14, 'start', MUT))
    o.append(P([(fx(600 + i * 6.25), fy(Dt(600 + i * 6.25))) for i in range(41)], AC, 3))
    for T_, lab, dx in ((673, '673 K: 4.41×10⁻¹⁰', 10), (773, '773 K: 1.76×10⁻⁹', -10)):
        o.append(C(fx(T_), fy(Dt(T_)), 5, LV))
        o.append(Tb(fx(T_) + dx, fy(Dt(T_)) + (24 if dx > 0 else -14), lab, 13, 'start' if dx > 0 else 'end', LV, True))
    # porous pellet ladder
    X0, w = 440, 260
    o.append(T(X0 + w / 2, 40, 'gas in a porous pellet, 500 K', 14, 'middle', INK, True))
    ladder = [('free gas', 5.0e-5), ('Knudsen, 5 nm pores', 2.05e-6), ('both combined', 1.97e-6), ('× ε/τ = 0.4/4', 1.97e-7)]
    gy = lambda v: 70 + (-4 - math.log10(v)) / 3.2 * 200
    o.append(L(X0 + 20, gy(1e-4), X0 + 20, gy(1e-7), L2, 1.5))
    for e in (-4, -5, -6, -7):
        o.append(L(X0 + 15, gy(10 ** e), X0 + 25, gy(10 ** e), L2, 1.5))
        o.append(T(X0 + 10, gy(10 ** e) + 4, f'10<tspan baseline-shift="super" font-size="10">{neg(e)}</tspan>', 13, 'end', MUT))
    for i, (lab, v) in enumerate(ladder):
        y = gy(v)
        o.append(C(X0 + 20, y, 5, AC if i < 3 else LV))
        o.append(T(X0 + 34, y + 5 + (8 if i == 2 else (-6 if i == 1 else 0)), f'{lab}: ' + sci(v), 13, 'start', AC if i < 3 else LV, i == 3))
    return 340, ''.join(o)


FIG[7] = (f7, 'Left: the worked example\'s Arrhenius law, D = 2.0×10⁻⁵ exp(−60 000/RT); a 100 K rise from 673 K to 773 K multiplies D by 4. Right: the porous-pellet example, where Knudsen diffusion in 5 nm pores and the pore geometry bring the free-gas value down 250 times.',
          'Left, D on a log scale against temperature from 600 to 850 K, a rising curve through 4.41e-10 at 673 K and 1.76e-9 at 773 K. Right, a vertical log ladder for gas in a porous pellet at 500 K: free gas 5.0e-5, Knudsen 2.05e-6, combined 1.97e-6, effective 1.97e-7 square metres per second.')
AFTER[7] = 2


# ---- 1.8 ternary triangle and the Wilke resistance sum ----
def f8():
    o = []
    A, B, Cn = (190, 64), (60, 262), (320, 262)
    o.append(L(A[0], A[1], B[0], B[1], AC, 3)); o.append(L(A[0], A[1], Cn[0], Cn[1], AC, 3)); o.append(L(B[0], B[1], Cn[0], Cn[1], L2, 2, '6 4'))
    for (x, y), nm, yv in ((A, 'A', 0.10), (B, 'B', 0.30), (Cn, 'C', 0.60)):
        o.append(f'<circle cx="{x}" cy="{y}" r="26" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
        o.append(T(x, y + 6, nm, 16, 'middle', INK, True))
        o.append(T(x, y + (-36 if nm == 'A' else 46), f'y = {yv:.2f}', 13, 'middle', INK, True))
    o.append(Tb(105, 175, sb('D', 'AB') + ' = 1.0×10⁻⁵', 13, 'end', AC, True))
    o.append(Tb(275, 175, sb('D', 'AC') + ' = 3.0×10⁻⁵', 13, 'start', AC, True))
    o.append(Tb(190, 267, sb('D', 'BC') + ' (not used)', 13, 'middle', MUT))
    # resistance bars
    X0, sc = 430, 4.2e-3
    o.append(T(560, 54, 'resistance y/D (s/m²)', 14, 'middle', INK, True))
    rows = [('B: 0.30 / 1.0×10⁻⁵', 3.0e4, NX, NXS), ('C: 0.60 / 3.0×10⁻⁵', 2.0e4, NX, NXS), ('sum', 5.0e4, AC, ACS)]
    for i, (lab, v, c, f) in enumerate(rows):
        y = 74 + i * 56
        o.append(T(X0, y + 2, lab, 13, 'start', INK))
        o.append(R(X0, y + 8, v * sc, 24, f, c, 4))
        o.append(T(X0 + v * sc + 6, y + 26, f'{v / 1e4:.1f}×10⁴', 13, 'start', c, True))
    o.append(T(560, 262, sb('D', 'A,m') + ' = 0.90 / 5.0×10⁴', 14, 'middle', AC, True))
    o.append(T(560, 284, '= 1.8×10⁻⁵ m²/s', 14, 'middle', AC, True))
    o.append(T(560, 310, 'averaging D instead: 2.33×10⁻⁵ (wrong)', 13, 'middle', LV))
    return 330, ''.join(o)


FIG[8] = (f8, 'The worked example. Wilke\'s formula for A uses only the two pairs that touch A: the resistances y_B/D_AB = 3.0×10⁴ and y_C/D_AC = 2.0×10⁴ s/m² add, giving D_A,m = 0.90/5.0×10⁴ = 1.8×10⁻⁵ m²/s. Averaging the D values instead would give 2.33×10⁻⁵ m²/s.',
          'Triangle of species A, B and C with mole fractions 0.10, 0.30 and 0.60; the A-B edge is labelled 1.0e-5 and the A-C edge 3.0e-5 square metres per second, the B-C edge is dashed and not used. Beside it, bars for the resistances 3.0e4 and 2.0e4 and their sum 5.0e4, giving an effective diffusivity of 1.8e-5, with the wrong average 2.33e-5 noted.')
AFTER[8] = 3


# ---- 1.9 centre and average concentration of the slab ----
def f9():
    o = []
    cen = lambda F: sum(4 / math.pi * (-1) ** n / (2 * n + 1) * math.exp(-(2 * n + 1) ** 2 * math.pi ** 2 * F / 4) for n in range(60))
    avg = lambda F: sum(8 / math.pi ** 2 / (2 * n + 1) ** 2 * math.exp(-(2 * n + 1) ** 2 * math.pi ** 2 * F / 4) for n in range(60))
    one = lambda F: 4 / math.pi * math.exp(-math.pi ** 2 * F / 4)
    x0, x1, y0, y1 = 80, 640, 60, 300
    fx = lambda F: x0 + F / 1.0 * (x1 - x0)
    fy = lambda v: y1 - v / 1.3 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 0.25, 0.5, 0.75, 1.0, 1.25], fx, fy, 'Fourier number Fo = Dt/L²', 'C/C₀', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    Fs = [0.001 + i * 0.999 / 120 for i in range(121)]
    o.append(P([(fx(F), fy(min(one(F), 1.3))) for F in Fs], MUT, 2, '6 4'))
    o.append(P([(fx(0), fy(1.0))] + [(fx(F), fy(cen(F))) for F in Fs], AC, 3))
    o.append(P([(fx(0), fy(1.0))] + [(fx(F), fy(avg(F))) for F in Fs if F > 0.004], NX, 3))
    for F, lab, c in ((0.379, 'centre: Fo 0.379 = 52.6 h', AC), (0.196, 'average: Fo 0.196 = 27.2 h', NX)):
        o.append(L(fx(F), fy(0.5), fx(F), y1, L2, 1.4, '4 3'))
        o.append(C(fx(F), fy(0.5), 5, c))
    o.append(L(x0, fy(0.5), fx(0.379), fy(0.5), L2, 1.4, '4 3'))
    o.append(Tb(fx(0.40) + 8, fy(0.5) - 12, 'centre: Fo 0.379 = 52.6 h', 13, 'start', AC, True))
    o.append(Tb(fx(0.19), fy(0.5) + 32, 'average: Fo 0.196 = 27.2 h', 13, 'end', NX, True))
    o.append(T(fx(0.03), fy(1.27) + 4, 'first term alone (dashed) exceeds 1 at small Fo', 13, 'start', MUT))
    return 360, ''.join(o)


FIG[9] = (f9, 'The 20 mm sheet of the worked examples (L = 10 mm, D = 2.0×10⁻¹⁰ m²/s, so Fo = 1 is 139 h). The average concentration halves at Fo = 0.196 (27.2 h), the centre at Fo = 0.379 (52.6 h). The dashed first term of the centre series is accurate above Fo = 0.2 but rises above 1 at small Fo.',
          'Plot of C over C0 against Fourier number from 0 to 1: the centre curve stays near 1 then falls through 0.5 at Fo 0.379; the average curve falls from the start and passes 0.5 at Fo 0.196; a dashed first-term curve starts at 1.27 and joins the centre curve above Fo 0.2.')
AFTER[9] = 2


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': capsub(cap), 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
