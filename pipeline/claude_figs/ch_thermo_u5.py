"""Claude's hand-drawn figures for ch-thermo-u5 (Solution thermodynamics), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def sp(base, s, size=11):
    return f'{base}<tspan baseline-shift="super" font-size="{size}">{s}</tspan>'


def curve(f, x0, x1, fx, fy, n=60, c=AC, w=2.5, dash=None):
    pts = [(fx(x0 + (x1 - x0) * i / n), fy(f(x0 + (x1 - x0) * i / n))) for i in range(n + 1)]
    return P(pts, c, w, dash)


# ---- 5.1 two phases and their chemical potentials ----
def f1():
    o = []
    # vessel with vapour over liquid
    vx, vy, vw, vh = 40, 50, 230, 290
    o.append(R(vx, vy, vw, vh, PANEL, INK, 10, 2))
    o.append(R(vx + 3, vy + 170, vw - 6, vh - 173, ACS, ACS, 6, 0))
    o.append(L(vx + 3, vy + 170, vx + vw - 3, vy + 170, AC, 2.5))
    for i, (x, y) in enumerate(((80, 90), (150, 120), (210, 85), (110, 150), (235, 140), (180, 160))):
        o.append(C(x, y, 5, LV))
    o.append(T(vx + vw / 2, vy + 30, 'vapour A', 15, bold=True))
    o.append(T(vx + vw / 2, vy + 52, 'μ = 101.5 kJ/mol', 14, fill=LV, bold=True))
    o.append(T(vx + vw / 2, vy + 225, 'liquid A', 15, bold=True))
    o.append(T(vx + vw / 2, vy + 247, 'μ = 100.0 kJ/mol', 14, fill=AC, bold=True))
    o.append(L(vx + vw / 2, vy + 105, vx + vw / 2, vy + 190, NX, 3, arrow='x'))
    o.append(Tb(vx + vw / 2 + 4, vy + 140, '0.010 mol', 13, 'start', NX, bold=True))
    o.append(T(vx + vw / 2, vy + vh + 24, '300 K, fixed P', 13, fill=MUT))
    # mu ladder
    ax, top, bot = 390, 70, 330
    fy = lambda m: bot - (m - 99.5) / 2.5 * (bot - top)
    o.append(L(ax, top - 10, ax, bot + 10, L2, 1.5))
    for m in (100.0, 100.5, 101.0, 101.5, 102.0):
        o.append(L(ax - 5, fy(m), ax, fy(m), L2, 1.5)); o.append(T(ax - 9, fy(m) + 4, f'{m:.1f}', 13, 'end', MUT))
    o.append(T(ax - 40, top - 22, 'μ of A (kJ/mol)', 13, 'start', MUT))
    o.append(L(ax, fy(101.5), ax + 120, fy(101.5), LV, 4)); o.append(T(ax + 128, fy(101.5) + 5, 'vapour', 14, 'start', LV, bold=True))
    o.append(L(ax, fy(100.0), ax + 120, fy(100.0), AC, 4)); o.append(T(ax + 128, fy(100.0) + 5, 'liquid', 14, 'start', AC, bold=True))
    o.append(L(ax + 60, fy(101.5) + 4, ax + 60, fy(100.0) - 6, NX, 2.5, arrow='x'))
    o.append(Tb(ax + 66, (fy(101.5) + fy(100.0)) / 2 + 5, 'Δμ = −1.5 kJ/mol', 13, 'start', NX))
    o.append(boxt(400, 352, 300, 64, ['ΔG = (100.0 − 101.5) × 0.010', '= −0.015 kJ = −15 J  → spontaneous'], ACS, AC, 14))
    return 432, ''.join(o)
FIG[1] = (f1, 'The worked example: vapour A sits 1.5 kJ/mol higher in chemical potential than liquid A at the same T and P, so moving 0.010 mol from vapour to liquid lowers G by 15 J. Transfer continues until the two levels are equal.',
          'A closed vessel with vapour A above liquid A, an arrow showing 0.010 mol condensing, and a vertical chemical-potential scale with the vapour level at 101.5 and the liquid level at 100.0 kilojoules per mole; a box gives delta G equals minus 15 joules.')


# ---- 5.2 tangent intercepts ----
def f2():
    o = []
    x0, x1, y0, y1 = 90, 560, 40, 380
    fx = lambda x: x0 + x * (x1 - x0)
    fy = lambda v: y1 - (v - 15) / (45 - 15) * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.25, 0.5, 0.75, 1.0], [15, 20, 25, 30, 35, 40, 45], fx, fy, 'x₁, mole fraction of component 1', 'V (cm³/mol)', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    V = lambda x: 18 + 28 * x - 6 * x * x
    o.append(curve(V, 0, 1, fx, fy, c=AC, w=3))
    tan = lambda x: 18.375 + 25 * x
    o.append(L(fx(0), fy(tan(0)), fx(1), fy(tan(1)), NX, 2.2, '7 4'))
    o.append(L(fx(0.25), fy(15), fx(0.25), fy(V(0.25)), L2, 1.5, '4 4'))
    o.append(C(fx(0.25), fy(V(0.25)), 6, AC))
    o.append(Tb(fx(0.25) + 12, fy(V(0.25)) + 22, 'V = 24.625 at x₁ = 0.25', 13, 'start'))
    o.append(C(fx(0), fy(18.375), 6, NX)); o.append(C(fx(1), fy(43.375), 6, NX))
    o.append(Tb(fx(0) + 12, fy(18.375) - 12, sb('V̄', '2') + ' = 18.375', 14, 'start', NX, bold=True))
    o.append(T(fx(1) + 12, fy(43.375) + 5, sb('V̄', '1') + ' = 43.375', 14, 'start', NX, bold=True))
    o.append(T(fx(1) + 12, fy(V(1)) + 5, 'pure 1: 40', 13, 'start', AC))
    o.append(Tb(fx(0.62), fy(V(0.62)) + 26, 'V = 18 + 28x₁ − 6x₁²', 13, 'middle', AC))
    o.append(Tb(fx(0.55), fy(tan(0.55)) - 12, 'tangent, slope 25.0', 13, 'end', NX))
    return 430, ''.join(o)
FIG[2] = (f2, 'The worked example on the V–x₁ curve. The tangent at x₁ = 0.25 (slope 25.0 cm³/mol) cuts x₁ = 0 at V̄₂ = 18.375 and x₁ = 1 at V̄₁ = 43.375 cm³/mol; pure component 1 has V = 40, less than V̄₁ at this composition.',
          'Plot of molar volume against mole fraction x1 from 0 to 1, a curved line rising from 18 to 40 cubic centimetres per mole, a dashed tangent at x1 = 0.25 whose ends at the two axes are marked 18.375 and 43.375.')


# ---- 5.3 Gibbs-Duhem slopes ----
def f3():
    o = []
    x0, x1, y0, y1 = 80, 440, 40, 330
    fx = lambda x: x0 + x * (x1 - x0)
    fy = lambda v: y1 - v / 26 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 5, 10, 15, 20, 25], fx, fy, 'x₁', 'M̄ᵢ − Mᵢ (kJ/mol)', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    m1 = lambda x: 25 * (1 - x) ** 2
    m2 = lambda x: 25 * x * x
    o.append(curve(m1, 0, 1, fx, fy, c=AC, w=3)); o.append(curve(m2, 0, 1, fx, fy, c=LV, w=3))
    o.append(T(fx(0.06), fy(m1(0.06)) - 6, sb('M̄', '1'), 15, 'start', AC, bold=True))
    o.append(T(fx(0.94), fy(m2(0.94)) - 6, sb('M̄', '2'), 15, 'end', LV, bold=True))
    xa = 0.4
    for f, s, c in ((m1, -30, AC), (m2, 20, LV)):
        d = 0.2
        o.append(L(fx(xa - d), fy(f(xa) - s * d), fx(xa + d), fy(f(xa) + s * d), INK, 1.8, '6 4'))
        o.append(C(fx(xa), fy(f(xa)), 5.5, c))
    o.append(L(fx(xa), fy(0), fx(xa), fy(10), L2, 1.4, '4 4'))
    o.append(Tb(fx(xa) + 50, fy(m1(xa)) - 18, 'slope −30.0', 13, 'start', AC, bold=True))
    o.append(Tb(fx(xa) + 46, fy(m2(xa)) + 30, 'slope +20.0', 13, 'start', LV, bold=True))
    # balance
    bx, by = 470, 150
    o.append(T(bx + 115, 46, 'Gibbs–Duhem at x₁ = 0.40', 14, bold=True))
    o.append(L(bx + 10, by, bx + 220, by, INK, 4))
    o.append(f'<polygon points="{bx + 115},{by + 4} {bx + 101},{by + 30} {bx + 129},{by + 30}" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    o.append(R(bx + 10, by - 50, 86, 46, ACS, AC, 6, 2)); o.append(T(bx + 53, by - 30, '0.40 × (−30)', 13)); o.append(T(bx + 53, by - 12, '= −12.0', 13, bold=True))
    o.append(R(bx + 134, by - 50, 86, 46, LVS, LV, 6, 2)); o.append(T(bx + 177, by - 30, '0.60 × 20', 13)); o.append(T(bx + 177, by - 12, '= +12.0', 13, bold=True))
    o.append(T(bx + 115, by + 56, 'sum = 0: balanced', 14, fill=NX, bold=True))
    o.append(boxt(bx, 238, 230, 92, ['x₁ dM̄₁ + x₂ dM̄₂ = 0', 'dM̄₂/dx₁ = −(x₁/x₂)(dM̄₁/dx₁)', '= −(0.40/0.60)(−30.0) = +20.0'], PANEL, L2, 13))
    return 384, ''.join(o)
FIG[3] = (f3, 'The worked example: partial molar properties that obey Gibbs–Duhem (here M̄₁ − M₁ = 25x₂² and M̄₂ − M₂ = 25x₁², in kJ/mol). At x₁ = 0.40 their slopes are −30.0 and +20.0, and the mole-fraction-weighted slopes cancel exactly, like weights on a balance.',
          'Two curves of partial molar property against x1, one falling from 25 to 0 and one rising from 0 to 25, with tangent lines at x1 = 0.40 labelled slope minus 30 and slope plus 20, and a balance beam with minus 12 on one side and plus 12 on the other.')


# ---- 5.4 fugacity against pressure ----
def f4():
    o = []
    x0, x1, y0, y1 = 80, 470, 40, 360
    fx = lambda p: x0 + p / 10 * (x1 - x0)
    fy = lambda f: y1 - f / 10 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6, 8, 10], [0, 2, 4, 6, 8, 10], fx, fy, 'pressure P (bar)', 'fugacity f (bar)', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    o.append(L(fx(0), fy(0), fx(10), fy(10), L2, 2, '7 4'))
    o.append(Tb(fx(7.4), fy(7.4) - 12, 'ideal gas: f = P', 13, 'end', MUT))
    o.append(L(fx(0), fy(0), fx(1), fy(1), AC, 3))
    o.append(curve(lambda p: p ** 0.9, 1, 10, fx, fy, c=AC, w=3))
    o.append(C(fx(10), fy(7.943), 6, NX)); o.append(C(fx(10), fy(10), 5, L2))
    o.append(Tb(fx(10) - 12, fy(7.943) + 24, 'f = 7.94', 14, 'end', NX, bold=True))
    o.append(Tb(fx(10) - 12, fy(10) + 5, 'P = 10', 13, 'end', MUT))
    o.append(L(fx(10), fy(9.8), fx(10), fy(8.2), NX, 1.8, arrow='x'))
    o.append(Tb(fx(5.2), fy(5.2 ** 0.9) + 26, 'real gas, Z = 0.90', 13, 'start', AC, bold=True))
    o.append(boxt(498, 60, 210, 140, ['ln φ = (Z − 1) ln(P/1 bar)', '= −0.10 × 2.3026', '= −0.2303', 'φ = 0.794 at 10 bar'], ACS, AC, 14))
    o.append(boxt(498, 220, 210, 110, ['ideal below 1 bar', 'Z = 0.90 from 1 to 10 bar', 'f = φP = 7.94 bar'], PANEL, L2, 13))
    return 414, ''.join(o)
FIG[4] = (f4, 'The first worked example: with Z = 0.90 above 1 bar, the fugacity grows as P raised to 0.9 and reaches only 7.94 bar at 10 bar, below the ideal line f = P. The gap is the fugacity coefficient φ = 0.794.',
          'Fugacity against pressure from 0 to 10 bar: a dashed diagonal for the ideal gas and a solid curve for the real gas that leaves the diagonal at 1 bar and ends at 7.94 bar when the pressure is 10 bar.')


# ---- 5.5 Pxy diagram ----
def f5():
    o = []
    x0, x1, y0, y1 = 80, 520, 40, 380
    fx = lambda x: x0 + x * (x1 - x0)
    fy = lambda p: y1 - (p - 30) / 80 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [30, 40, 50, 60, 70, 80, 90, 100, 110], fx, fy, sb('x', '1') + ' or ' + sb('y', '1'), 'P (kPa) at 350 K', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    bub = lambda x: 40 + 60 * x
    o.append(L(fx(0), fy(40), fx(1), fy(100), AC, 3))
    dew = [(fx(y), fy(1 / (y / 100 + (1 - y) / 40))) for y in [i / 60 for i in range(61)]]
    o.append(P(dew, LV, 3))
    o.append(Tb(fx(0.70), fy(bub(0.70)) - 14, 'bubble line (liquid)', 13, 'end', AC, bold=True))
    o.append(Tb(fx(0.78), fy(1 / (0.78 / 100 + 0.22 / 40)) + 30, 'dew curve (vapour)', 13, 'start', LV, bold=True))
    # tie line at 58 kPa
    o.append(L(fx(0.30), fy(58), fx(0.5172), fy(58), NX, 2.5))
    o.append(C(fx(0.30), fy(58), 6, AC)); o.append(C(fx(0.5172), fy(58), 6, LV))
    o.append(L(fx(0.30), fy(58), fx(0.30), fy(30), L2, 1.4, '4 4')); o.append(L(fx(0.5172), fy(58), fx(0.5172), fy(30), L2, 1.4, '4 4'))
    o.append(Tb(fx(0.30) - 8, fy(58) - 12, 'x₁ = 0.30', 13, 'end', AC, bold=True))
    o.append(Tb(fx(0.5172) + 8, fy(58) - 12, 'y₁ = 0.517', 13, 'start', LV, bold=True))
    o.append(Tb(fx(0.41), fy(58) + 22, 'P = 58 kPa', 13, 'middle', NX, bold=True))
    o.append(T(fx(0) + 8, fy(40) + 20, 'pure 2: 40 kPa', 13, 'start', MUT))
    o.append(T(fx(1) - 8, fy(100) - 10, 'pure 1: 100 kPa', 13, 'end', MUT))
    o.append(T(fx(0.22), fy(96), 'liquid', 14, 'middle', MUT)); o.append(T(fx(0.62), fy(40), 'vapour', 14, 'middle', MUT))
    o.append(boxt(540, 70, 168, 150, ['p₁ = 0.30 × 100 = 30', 'p₂ = 0.70 × 40 = 28', 'P = 58 kPa', 'y₁ = 30/58 = 0.517'], ACS, AC, 13))
    o.append(boxt(540, 236, 168, 104, ['dew point of', 'y₁ = 0.50:', 'P = 57.1 kPa, x₁ = 0.286'], PANEL, L2, 13))
    return 430, ''.join(o)
FIG[5] = (f5, 'The worked examples on a P–x–y diagram at 350 K. Raoult\'s law makes the bubble line straight from 40 to 100 kPa; the dew curve bows below it. At 58 kPa the liquid x₁ = 0.30 is in equilibrium with vapour y₁ = 0.517.',
          'Pressure against composition at 350 kelvin: a straight bubble line from 40 to 100 kilopascals, a curved dew line below it, and a horizontal tie line at 58 kilopascals joining liquid x1 = 0.30 to vapour y1 = 0.517.')


# ---- 5.6 excess volume and the Gibbs split ----
def f6():
    o = []
    x0, x1, y0, y1 = 70, 330, 74, 310
    fx = lambda x: x0 + x * (x1 - x0)
    fy = lambda v: y1 - v / 0.6 * (y1 - y0)
    o.append(T(x0 - 20, 24, 'Example 1: excess volume', 14, 'start', bold=True))
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 1.0], [0, 0.2, 0.4, 0.6], fx, fy, 'x₁', 'V<tspan baseline-shift="super" font-size="11">E</tspan> (cm³/mol)', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    o.append(curve(lambda x: 2 * x * (1 - x), 0, 1, fx, fy, c=AC, w=3))
    o.append(L(fx(0), fy(0), fx(1), fy(0), L2, 2, '6 4'))
    o.append(C(fx(0.5), fy(0.5), 6, NX)); o.append(Tb(fx(0.5), fy(0.5) - 14, '0.500 at x₁ = 0.50', 13, 'middle', NX, bold=True))
    o.append(Tb(fx(0.5), fy(0) - 10, 'ideal solution: 0', 13, 'middle', MUT))
    # bars for example 2
    bx, base = 420, 200
    sc = 0.062   # px per J/mol
    o.append(T(bx - 30, 24, 'Example 2: Gibbs energy (J/mol)', 14, 'start', bold=True))
    o.append(L(bx - 10, base, 712, base, L2, 1.5))
    o.append(T(bx - 14, base + 4, '0', 13, 'end', MUT))
    bars = [('ideal', -1679, LV), ('excess', 678, NX), ('mixing', -1001, AC)]
    for i, (lab, v, c) in enumerate(bars):
        x = bx + 10 + i * 96
        h = abs(v) * sc
        y = base - h if v > 0 else base
        o.append(R(x, y, 64, h, c, c, 3, 1))
        o.append(T(x + 32, (y - 8) if v > 0 else (y + h + 18), f'{v:+d}'.replace('-', '−'), 14, 'middle', INK, bold=True))
        o.append(T(x + 32, base + (-12 if v < 0 else 20), lab, 13, 'middle', MUT))
    o.append(T(bx + 140, 60, 'ΔG of mixing = ideal part + ' + sp('G', 'E'), 13, 'middle', MUT))
    o.append(boxt(400, 344, 308, 60, [sp('S', 'E') + ' = (800 − 678)/300 = 0.41 J/(mol·K)', 'Q for 5.0 mol = 5.0 × 800 = +4.0 kJ'], PANEL, L2, 13))
    return 420, ''.join(o)
FIG[6] = (f6, 'Left, the first example: the excess volume 2x₁x₂ peaks at 0.500 cm³/mol, while an ideal solution stays on zero. Right, the second example: the ideal Gibbs energy of mixing (−1679 J/mol) plus the excess Gibbs energy (+678 J/mol) gives ΔG of mixing = −1001 J/mol, so the liquids still mix.',
          'Left: a hump-shaped curve of excess volume against x1 peaking at 0.5 cubic centimetres per mole. Right: three bars, ideal Gibbs energy of mixing minus 1679, excess plus 678, and total mixing minus 1001 joules per mole.')


# ---- 5.7 actual and Raoult partial pressures ----
def f7():
    o = []
    base, top = 330, 60
    fy = lambda p: base - p / 0.6 * (base - top)
    x0 = 90
    o.append(L(x0, base, 560, base, L2, 1.5)); o.append(L(x0, top - 10, x0, base, L2, 1.5))
    for p in (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6):
        o.append(L(x0 - 5, fy(p), x0, fy(p), L2, 1.5)); o.append(T(x0 - 9, fy(p) + 4, f'{p:.1f}', 13, 'end', MUT))
        if p: o.append(L(x0, fy(p), 560, fy(p), LN, 1))
    o.append(T(x0, top - 22, 'partial pressure (bar)', 13, 'start', MUT))
    groups = [('component 1 (x₁ = 0.20)', 0.16, 0.50, 'γ₁ = 3.125'), ('component 2 (x₂ = 0.80)', 0.48, 0.50, 'γ₂ = 1.042')]
    for i, (lab, raoult, real, g) in enumerate(groups):
        gx = 130 + i * 220
        o.append(R(gx, fy(raoult), 60, base - fy(raoult), PANEL, L2, 3, 2, '5 3'))
        o.append(R(gx + 74, fy(real), 60, base - fy(real), AC if i == 0 else LV, AC if i == 0 else LV, 3, 1))
        o.append(T(gx + 30, fy(raoult) - 8, f'{raoult:.2f}', 13, 'middle', MUT))
        o.append(T(gx + 104, fy(real) - 8, f'{real:.2f}', 14, 'middle', INK, bold=True))
        o.append(T(gx + 67, base + 22, lab, 13, 'middle'))
        o.append(T(gx + 67, base + 42, g, 14, 'middle', NX, bold=True))
    o.append(R(590, 80, 18, 14, PANEL, L2, 2, 2, '5 3')); o.append(T(614, 92, 'Raoult: xᵢPᵢˢᵃᵗ', 13, 'start'))
    o.append(R(590, 104, 18, 14, AC, AC, 2, 1)); o.append(T(614, 116, 'measured yᵢP', 13, 'start'))
    o.append(boxt(580, 150, 130, 136, ['P = 1.00 bar', 'a₁ = 0.50/0.80', '= 0.625', 'γ₁ = 0.625/0.20', '= 3.125'], ACS, AC, 13))
    return 392, ''.join(o)
FIG[7] = (f7, 'The worked example: each component\'s measured partial pressure yᵢP (solid) beside what Raoult\'s law would give, xᵢPᵢˢᵃᵗ (dashed). The ratio of the two is the activity coefficient: 0.50/0.16 = 3.125 for the dilute component 1 but only 0.50/0.48 = 1.042 for component 2.',
          'Bar chart of partial pressures at 1 bar total: for component 1, a dashed Raoult bar of 0.16 bar beside a measured bar of 0.50 bar, gamma 1 equals 3.125; for component 2, a dashed bar of 0.48 beside a measured bar of 0.50, gamma 2 equals 1.042.')


# ---- 5.8 Margules curves ----
def f8():
    o = []
    x0, x1, y0, y1 = 80, 500, 40, 360
    fx = lambda x: x0 + x * (x1 - x0)
    fy = lambda g: y1 - (g - 1) / 1.3 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2], fx, fy, 'x₁', 'activity coefficient γ', lambda v: f'{v:g}', lambda v: f'{v:.1f}'))
    A = 0.8
    o.append(curve(lambda x: math.exp(A * (1 - x) ** 2), 0, 1, fx, fy, c=AC, w=3))
    o.append(curve(lambda x: math.exp(A * x * x), 0, 1, fx, fy, c=LV, w=3))
    o.append(T(fx(0.12), fy(math.exp(A * 0.88 ** 2)) - 10, sb('γ', '1') + ' = exp(0.8x₂²)', 13, 'start', AC, bold=True))
    o.append(T(fx(0.88), fy(math.exp(A * 0.88 ** 2)) - 10, sb('γ', '2') + ' = exp(0.8x₁²)', 13, 'end', LV, bold=True))
    o.append(L(fx(0.3), fy(1), fx(0.3), fy(1.48), L2, 1.4, '4 4'))
    o.append(C(fx(0.3), fy(1.480), 6, AC)); o.append(C(fx(0.3), fy(1.075), 6, LV))
    o.append(Tb(fx(0.3) + 10, fy(1.480) + 5, '1.48', 14, 'start', AC, bold=True))
    o.append(Tb(fx(0.3) + 10, fy(1.075) - 8, '1.075', 14, 'start', LV, bold=True))
    o.append(boxt(520, 52, 190, 146, ['A = 0.80, x₁ = 0.30', 'ln γ₁ = 0.8 × 0.49', '= 0.392 → 1.48', 'ln γ₂ = 0.8 × 0.09', '= 0.072 → 1.075', 'ends: ' + sp('e', '0.8') + ' = 2.23'], ACS, AC, 13))
    o.append(boxt(520, 214, 190, 110, ['van Laar fit', '(second example):', 'A₁₂ = 1.417', 'A₂₁ = 0.986'], PANEL, L2, 13))
    return 414, ''.join(o)
FIG[8] = (f8, 'The first worked example: with the one-constant Margules model, A = 0.80, each activity coefficient climbs to e<sup>0.8</sup> = 2.23 as its own component becomes dilute, and the two curves are mirror images. At x₁ = 0.30, γ₁ = 1.48 and γ₂ = 1.075.',
          'Two activity-coefficient curves against x1: gamma 1 falls from 2.23 at x1 = 0 to 1 at x1 = 1, gamma 2 rises from 1 to 2.23; points at x1 = 0.30 are marked 1.48 and 1.075.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
