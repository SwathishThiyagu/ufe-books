"""Claude's hand-drawn figures for ce-rcc-u2 (RC design: limit state design of beams), one per chapter, each drawn from
that chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """x_u, A_st ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔε])_([A-Za-z0-9,]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def poly(pts, fill, stroke, sw=2, op=None):
    o = f';fill-opacity:{op}' if op is not None else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}{o};stroke-linejoin:round"/>'


def vdim(x, y1, y2, label, c=MUT, side='left', size=13):
    """vertical dimension line with end ticks and a label beside it"""
    o = [L(x, y1, x, y2, c, 1.4), L(x - 5, y1, x + 5, y1, c, 1.4), L(x - 5, y2, x + 5, y2, c, 1.4)]
    tx = x - 8 if side == 'left' else x + 8
    o.append(T(tx, (y1 + y2) / 2 + 4.5, label, size, 'end' if side == 'left' else 'start', c))
    return ''.join(o)


def hdim(x1, x2, y, label, c=MUT, size=13, above=True):
    o = [L(x1, y, x2, y, c, 1.4), L(x1, y - 5, x1, y + 5, c, 1.4), L(x2, y - 5, x2, y + 5, c, 1.4)]
    o.append(T((x1 + x2) / 2, y - 8 if above else y + 18, label, size, fill=c))
    return ''.join(o)


def bars(xs, y, r, c=INK):
    return ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c};stroke:var(--fig);stroke-width:1.5"/>' for x in xs)


FIG = {}

# ---- 2.1 the 230 x 450 beam of worked example 1: section, strains, stress block and the couple ----
def f1():
    s = 0.62                     # px per mm
    top = 60; yD = top + 450 * s; yd = top + 400 * s; yx = top + 164.2 * s
    x0 = 70; xb = x0 + 230 * s
    o = [T(x0 + 115 * s, 34, 'Section', 15, bold=True)]
    o.append(R(x0, top, 230 * s, 450 * s, PANEL, AC, 2))
    o.append(R(x0, top, 230 * s, 164.2 * s, ACS, AC, 0, 0))
    o.append(bars([x0 + 48 * s, x0 + 115 * s, x0 + 182 * s], yd, 6))
    o.append(L(x0 - 6, yx, 452, yx, L2, 1.5, '6 5'))
    o.append(vdim(x0 - 16, top, yd, 'd = 400'))
    o.append(T(x0 + 115 * s, yD + 22, 'b = 230 mm', 13, fill=MUT))
    o.append(T(x0 + 115 * s, yD + 40, '3 bars of 20 mm', 13, fill=MUT))
    o.append(T(x0 + 115 * s, yD + 58, 'A_st = 942.5 mm²', 13, fill=MUT))
    # strain diagram
    sx = 330; k = 18000           # px per unit strain
    o.append(T(sx, 34, 'Strain', 15, bold=True))
    o.append(L(sx, top, sx, yD, L2, 1.5))
    ec, es = 0.0035, 0.0035 * (400 - 164.2) / 164.2
    o.append(poly([(sx, top), (sx - ec * k, top), (sx, yx)], ACS, AC))
    o.append(poly([(sx, yx), (sx + es * k, yd), (sx, yd)], NXS, NX))
    o.append(T(sx - ec * k, top - 8, '0.0035', 13))
    o.append(T(sx + es * k - 10, yd + 24, 'ε_s = 0.0050', 13, 'middle', NX))
    o.append(Tb(sx + 8, yx + 18, 'neutral axis', 13, 'start', MUT))
    o.append(vdim(sx + 14, top, yx, 'x_u = 164.2', INK, 'right'))
    # stress block and forces
    bx = 520
    o.append(T(bx + 40, 34, 'Stress and forces', 15, bold=True))
    o.append(L(bx, top, bx, yD, L2, 1.5))
    pk = 0.446 * 25 * 3.2           # 0.446 fck scaled
    y2 = top + (164.2 * 3 / 7) * s  # end of flat part
    pts = [(bx, top), (bx - pk, top), (bx - pk, y2)]
    for i in range(1, 21):
        t = i / 20; yy = y2 + t * (yx - y2); pts.append((bx - pk * (1 - t * t), yy))
    pts.append((bx, yx))
    o.append(poly(pts, ACS, AC))
    o.append(T(bx - pk - 4, top - 8, '11.2 N/mm²', 13, 'end'))
    yc = top + 0.42 * 164.2 * s
    o.append(L(bx + 70, yc, bx + 10, yc, AC, 3, arrow='n'))
    o.append(T(bx + 76, yc - 4, 'C = 340 kN', 13, 'start', bold=True))
    o.append(T(bx + 76, yc + 14, '0.42x_u = 69', 13, 'start', MUT))
    o.append(L(bx + 10, yd, bx + 70, yd, NX, 3, arrow='x'))
    o.append(T(bx + 76, yd - 4, 'T = 340 kN', 13, 'start', bold=True))
    o.append(T(bx + 76, yd + 14, '0.87f_y A_st', 13, 'start', MUT))
    o.append(vdim(bx + 40, yc + 4, yd - 4, 'z = 331.0', AC, 'right'))
    o.append(T(380, yD + 92, 'M_u = C × z = 340 kN × 0.331 m = 112.5 kN·m', 14, bold=True))
    return int(yD + 106), ''.join(o)
FIG[1] = (f1, 'The beam of the first worked example at collapse: the top fibre is at 0.0035, the neutral axis is 164.2 mm down, the bars strain to 0.0050 and yield, and the concrete force of 340 kN and the steel force of 340 kN form a couple with a 331 mm lever arm that carries 112.5 kN·m.',
          'Rectangular section 230 by 450 millimetres with three bars, its strain diagram and its curved stress block with the compression and tension forces.')

# ---- 2.2 strain diagrams of the 300 x 500, M30, Fe500 beam: under, balanced and over-reinforced ----
def f2():
    top, s = 70, 0.56
    yd = top + 500 * s
    x0 = 300; k = 26000
    o = [T(x0, 34, 'Strain across the depth (d = 500 mm, Fe500)', 15, bold=True)]
    o.append(L(x0, top - 10, x0, yd + 18, L2, 1.5))
    o.append(L(x0 - 0.0035 * k - 20, top, x0 + 0.0055 * k, top, LN, 1))
    o.append(L(x0 - 0.0035 * k - 20, yd, x0 + 0.0055 * k, yd, LN, 1))
    o.append(T(x0 - 0.0035 * k - 24, top + 5, 'top', 13, 'end', MUT))
    o.append(T(x0 - 0.0035 * k - 24, yd + 5, 'steel', 13, 'end', MUT))
    xl = x0 + 0.004175 * k
    o.append(L(xl, top - 4, xl, yd + 20, LV, 2, '6 5'))
    o.append(T(xl, yd + 36, 'ε_s,lim = 0.00418', 13, fill=LV, bold=True))
    cases = [(201.4, AC, 'under: x_u = 201.4, ε_s = 0.00519', None), (230, LV, 'balanced: x_u = x_u,max = 230', None),
             (302.8, NX, 'over: x_u = 302.8, ε_s = 0.00228', '7 5')]
    for i, (xu, c, lab, dash) in enumerate(cases):
        es = 0.0035 * (500 - xu) / xu
        o.append(P([(x0 - 0.0035 * k, top), (x0 + es * k, yd)], c, 2.6, dash))
        yy = top + xu * s
        o.append(C(x0, yy, 5, c))
        o.append(C(x0 + es * k, yd, 5, c))
        o.append(L(x0 - 132, yy, x0 - 8, yy, c, 1.2, '3 4'))
        o.append(T(x0 - 136, yy + 4.5, lab.split(':')[0] + ' x_u = ' + f'{xu:g}', 13, 'end', c, bold=True))
    o.append(T(x0 - 0.0035 * k, top - 10, '0.0035', 13))
    o.append(T(x0 + 0.00519 * k, yd - 12, '0.00519', 13, 'start', AC))
    o.append(T(x0 + 0.00228 * k - 4, yd + 20, '0.00228', 13, 'end', NX))
    o.append(T(80, yd + 66, 'A_st = 1500 mm²: steel strain beyond the limit, ductile, M_u = 271.1 kN·m', 13, 'start', AC))
    o.append(T(80, yd + 86, 'A_st = 2500 mm²: steel stops at 392 N/mm², brittle; code credits M_u,lim = 300.6 kN·m only', 13, 'start', NX))
    return int(yd + 100), ''.join(o)
FIG[2] = (f2, 'All three strain lines pivot on 0.0035 at the top. With 1500 mm² the neutral axis is at 201.4 mm and the steel strains past the 0.00418 limit; at 230 mm the section is balanced; with 2500 mm² the axis drops to 302.8 mm and the steel reaches only 0.00228.',
          'Three straight strain lines through the depth of a beam, all starting at 0.0035 compression at the top, crossing zero at three neutral axis depths and ending at three steel strains either side of a dashed limit line.')

# ---- 2.3 the doubly reinforced beam of worked example 1 as two couples ----
def f3():
    s = 0.5; top = 64; yD = top + 550 * s; yd = top + 500 * s; ydp = top + 50 * s; yx = top + 240 * s
    x0 = 40; w = 250 * s
    o = [T(x0 + w / 2, 34, 'Section', 15, bold=True)]
    o.append(R(x0, top, w, 550 * s, PANEL, AC, 2))
    o.append(R(x0, top, w, 240 * s, ACS, AC, 0, 0))
    o.append(bars([x0 + 30, x0 + w - 30], ydp, 5))
    o.append(bars([x0 + 22, x0 + 50, x0 + w - 50, x0 + w - 22], yd, 6.5))
    o.append(L(x0 - 4, yx, x0 + w + 4, yx, L2, 1.5, '6 5'))
    o.append(T(x0 + w + 8, ydp + 4, 'A_sc 2 of 12', 13, 'start'))
    o.append(T(x0 + w + 8, yd + 4, 'A_st 1742', 13, 'start'))
    o.append(T(x0 + w + 8, yx - 6, 'x_u,max', 13, 'start', MUT))
    o.append(T(x0 + w + 8, yx + 12, '= 240', 13, 'start', MUT))
    o.append(T(x0 + w / 2 + 20, yD + 20, 'b = 250, d = 500, d′ = 50', 13, fill=MUT))
    # part 1
    p1 = 290
    o.append(T(p1 + 90, 34, 'Part 1: concrete couple', 15, bold=True))
    yc = top + 0.42 * 240 * s
    o.append(R(p1, top, 50, 240 * s, ACS, AC, 0))
    o.append(L(p1 + 120, yc, p1 + 56, yc, AC, 3, arrow='n'))
    o.append(T(p1 + 124, yc + 5, 'C = 540 kN', 13, 'start', bold=True))
    o.append(L(p1 + 56, yd, p1 + 120, yd, NX, 3, arrow='x'))
    o.append(T(p1 + 124, yd - 22, 'A_st,lim = 1496', 13, 'start'))
    o.append(T(p1 + 124, yd + 5, 'T₁ = 540 kN', 13, 'start', bold=True))
    o.append(vdim(p1 + 88, yc + 4, yd - 4, '399.2', AC, 'right'))
    o.append(T(p1 + 90, yD + 20, 'M_u,lim = 215.57 kN·m', 14, bold=True))
    # part 2
    p2 = 520
    o.append(T(p2 + 90, 34, 'Part 2: steel couple', 15, bold=True))
    o.append(L(p2 + 70, ydp, p2 + 10, ydp, AC, 3, arrow='n'))
    o.append(T(p2 + 76, ydp + 5, 'C_s = 76.5 kN', 13, 'start', bold=True))
    o.append(T(p2 + 76, ydp + 23, 'f_sc = 352.1', 13, 'start', MUT))
    o.append(T(p2 + 76, ydp + 41, 'ε_sc = 0.00277', 13, 'start', MUT))
    o.append(L(p2 + 10, yd, p2 + 70, yd, NX, 3, arrow='x'))
    o.append(T(p2 + 76, yd - 22, 'A_st2 = 212', 13, 'start'))
    o.append(T(p2 + 76, yd + 5, 'T₂ = 76.5 kN', 13, 'start', bold=True))
    o.append(vdim(p2 + 40, ydp + 8, yd - 8, '450', AC, 'left'))
    o.append(T(p2 + 90, yD + 20, 'ΔM = 34.43 kN·m', 14, bold=True))
    o.append(T(380, yD + 52, 'M_u = 215.57 + 34.43 = 250 kN·m (areas in mm²)', 14, bold=True))
    return int(yD + 68), ''.join(o)
FIG[3] = (f3, 'The doubly reinforced beam of the first worked example split into two couples: concrete with 1496 mm² of steel carries Mu,lim = 215.57 kN·m, and 217 mm² of compression steel at 352 N/mm² with 212 mm² of extra tension steel carries the remaining 34.43 kN·m over a 450 mm arm.',
          'Beam section with top and bottom bars, then two force diagrams: a concrete compression and steel tension couple, and a compression steel and extra tension steel couple.')

# ---- 2.4 the T-beam of worked example 2: neutral axis in the web ----
def f4():
    s = 0.4; top = 70; x0 = 40
    yDf = top + 100 * s; yx = top + 210.6 * s; yd = top + 500 * s; yD = top + 560 * s; yyf = top + 96.6 * s
    xw0 = x0 + 350 * s; xw1 = x0 + 650 * s; xr = x0 + 1000 * s
    o = [T(x0 + 190, 34, 'Section (b_f = 1000, D_f = 100, b_w = 300, d = 500)', 15, bold=True)]
    o.append(poly([(x0, top), (xr, top), (xr, yDf), (xw1, yDf), (xw1, yD), (xw0, yD), (xw0, yDf), (x0, yDf)], PANEL, AC))
    o.append(R(x0, top, xw0 - x0, 96.6 * s, LVS, LV, 0, 0))
    o.append(R(xw1, top, xr - xw1, 96.6 * s, LVS, LV, 0, 0))
    o.append(R(xw0, top, xw1 - xw0, 210.6 * s, ACS, AC, 0, 0))
    o.append(poly([(x0, top), (xr, top), (xr, yDf), (xw1, yDf), (xw1, yD), (xw0, yD), (xw0, yDf), (x0, yDf)], 'none', AC))
    o.append(bars([xw0 + 18, xw0 + 60, xw0 + 102], yd - 6, 5.5))
    o.append(bars([xw0 + 18, xw0 + 60, xw0 + 102], yd + 8, 5.5))
    o.append(L(x0 - 4, yx, xr + 60, yx, L2, 1.5, '6 5'))
    o.append(Tb(xr + 4, yx - 6, 'x_u = 210.6', 13, 'start'))
    o.append(T(x0 + 70, top + 17, 'overhangs', 13, fill=LV, bold=True))
    o.append(T(x0 + 70, top + 33, 'y_f = 96.6', 13, fill=LV))
    o.append(T(xw0 + 60, yx + 22, 'web', 13, fill=AC, bold=True))
    o.append(T(xw1 + 10, yd + 4, '6 bars of 25', 13, 'start'))
    # forces
    fx = 520
    o.append(T(fx + 70, 34, 'Forces', 15, bold=True))
    o.append(L(fx, top + 10, fx, yD, L2, 1.5))
    ycf = top + 48.3 * s; ycw = top + 88.5 * s
    o.append(L(fx + 70, ycf, fx + 6, ycf, LV, 3, arrow='l'))
    o.append(T(fx + 76, ycf - 4, 'C_f = 608.5 kN', 13, 'start', LV, bold=True))
    o.append(L(fx + 70, ycw, fx + 6, ycw, AC, 3, arrow='n'))
    o.append(T(fx + 76, ycw + 14, 'C_w = 454.9 kN', 13, 'start', AC, bold=True))
    o.append(L(fx + 6, yd, fx + 70, yd, NX, 3, arrow='x'))
    o.append(T(fx + 76, yd + 5, 'T = 1063.4 kN', 13, 'start', bold=True))
    o.append(T(fx + 76, ycw + 50, 'lever arms:', 13, 'start', MUT))
    o.append(T(fx + 76, ycw + 68, 'C_f 451.7 mm', 13, 'start', MUT))
    o.append(T(fx + 76, ycw + 86, 'C_w 411.6 mm', 13, 'start', MUT))
    o.append(T(360, yD + 34, 'M_u = 608.5 × 0.4517 + 454.9 × 0.4116 = 462.1 kN·m', 14, bold=True))
    return int(yD + 50), ''.join(o)
FIG[4] = (f4, 'The T-beam of the second worked example: the steel needs more compression than the 100 mm slab can give, so the neutral axis drops to 210.6 mm in the web; the overhangs carry 0.45fck over the equivalent depth yf = 96.6 mm and the web carries the usual block.',
          'T-shaped beam section with the flange overhangs and the web compression zone shaded, the neutral axis in the web, and the flange, web and steel forces beside it.')

# ---- 2.5 the design-aid curve pt against Mu/bd² for M25 ----
def f5():
    x0, x1, y0, y1 = 80, 680, 70, 340
    fx = lambda k: x0 + k / 3.6 * (x1 - x0)
    fy = lambda p: y1 - p / 1.3 * (y1 - y0)
    pt = lambda k, fy_: 50 * 25 / fy_ * (1 - math.sqrt(1 - 4.6 * k / 25))
    o = [axes(x0, x1, y0, y1, [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5], [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2], fx, fy,
              _sub('M_u/bd² (N/mm²)'), _sub('p_t (%)'), lambda v: f'{v:.1f}', lambda v: f'{v:.1f}')]
    for fy_, kl, c, dash, lab in [(415, 3.449, AC, None, 'Fe415'), (500, 3.340, NX, '7 5', 'Fe500')]:
        o.append(P([(fx(k / 100 * kl), fy(pt(k / 100 * kl, fy_))) for k in range(0, 101)], c, 2.6, dash))
        o.append(C(fx(kl), fy(pt(kl, fy_)), 5, c))
    o.append(T(fx(2.2), fy(0.80), 'Fe415', 14, 'end', AC, bold=True))
    o.append(T(fx(1.4), fy(0.22), 'Fe500', 14, 'start', NX, bold=True))
    o.append(T(fx(3.5), fy(0.27), 'Fe415 table ends at 3.45, 1.20 %', 13, 'end', AC, bold=True))
    o.append(T(fx(3.5), fy(0.27) + 20, 'Fe500 table ends at 3.34, 0.95 %', 13, 'end', NX, bold=True))
    X, Y = fx(2.0), fy(0.618)
    o.append(L(X, y1, X, Y, LV, 2, '5 4')); o.append(L(X, Y, x0, Y, LV, 2, '5 4', arrow='l'))
    o.append(C(X, Y, 6, LV))
    o.append(Tb(X + 10, Y - 10, 'example: 2.00 → p_t = 0.618 %', 13, 'start', LV, True))
    o.append(T(x0 + 10, 40, 'M25 concrete; one SP 16 table per concrete grade, one column per steel grade', 14, 'start', MUT))
    return 400, ''.join(o)
FIG[5] = (f5, 'The curve behind the M25 flexure table: entering at Mu/bd² = 2.00 N/mm² gives pt = 0.618 % for Fe415. Each curve stops at its limiting point, 3.45 N/mm² and 1.20 % for Fe415, 3.34 N/mm² and 0.95 % for Fe500.',
          'Graph of steel percentage against Mu over b d squared for M25 concrete, with a solid Fe415 curve, a dashed Fe500 curve, their end points and a read-off at 2.00.')

# ---- 2.6 kt against pt (curve fit to IS 456 Fig. 4) with the deflection example ----
def f6():
    x0, x1, y0, y1 = 80, 680, 70, 330
    fx = lambda p: x0 + (p - 0.2) / 2.8 * (x1 - x0)
    fy = lambda k: y1 - (k - 0.6) / 1.5 * (y1 - y0)
    kt = lambda fs, p: min(2.0, 1 / (0.225 + 0.00322 * fs + 0.625 * math.log10(p)))
    o = [axes(x0, x1, y0, y1, [0.2, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6, 3.0], [0.6, 0.9, 1.2, 1.5, 1.8, 2.1], fx, fy,
              _sub('tension steel p_t (%)'), _sub('k_t'), lambda v: f'{v:.1f}', lambda v: f'{v:.1f}')]
    for fs, c, dash in [(169.6, LV, None), (200.8, AC, None), (240.7, NX, '7 5')]:
        pts = [(fx(p / 100), fy(kt(fs, p / 100))) for p in range(20, 301, 2)]
        o.append(P(pts, c, 2.4, dash))
    for i, (fs, c, dash) in enumerate([(169.6, LV, None), (200.8, AC, None), (240.7, NX, '7 5')]):
        yy = fy(2.0) + 4 + i * 22
        o.append(L(fx(2.0), yy, fx(2.0) + 40, yy, c, 2.4, dash))
        o.append(T(fx(2.0) + 48, yy + 5, f'f_s = {fs:g} N/mm²', 13, 'start', c, bold=True))
    o.append(C(fx(1.117), fy(1.248), 6, LV))
    o.append(Tb(fx(1.117) + 12, fy(1.248) - 22, 'd = 450: p_t 1.12, k_t 1.25, allowed 25.0 > 20.0', 13, 'start', LV, True))
    o.append(C(fx(1.257), fy(1.071), 6, AC))
    o.append(L(fx(1.257), fy(1.071) + 6, fx(1.257), fy(0.70) - 14, AC, 1.4, '3 3'))
    o.append(Tb(fx(1.257) - 30, fy(0.70), 'd = 400: p_t 1.26, k_t 1.07, allowed 21.4 < 22.5', 13, 'start', AC, True))
    o.append(T(x0 + 10, 40, 'curve fit to IS 456 Fig. 4; f_s = 0.58 f_y × A_st,req / A_st,prov (N/mm²)', 14, 'start', MUT))
    return 390, ''.join(o)
FIG[6] = (f6, 'The tension-steel factor kt falls as the steel percentage and the service stress rise. The 9 m roof beam with d = 400 mm sits at kt = 1.07 and fails; deepening it to d = 450 mm lowers both pt and fs and lifts kt to 1.25.',
          'Three falling curves of the modification factor kt against steel percentage for service stresses 169.6, 200.8 and 240.7, with two marked points from the worked example.')

# ---- 2.7 uncracked and cracked transformed sections of the 300 x 500 beam ----
def f7():
    s = 0.5; top = 70; yD = top + 500 * s; yd = top + 450 * s
    o = []
    # uncracked
    x0 = 70; w = 300 * s
    o.append(T(x0 + w / 2 + 40, 36, 'Uncracked (below M_cr)', 15, bold=True))
    o.append(R(x0, top, w, 500 * s, ACS, AC, 2))
    sw = 8400 / 7 * s / 7          # strip width for (m − 1)A_st, drawn 16.8 mm deep
    o.append(R(x0 + w / 2 - 84, yd - 6, 168, 12, NXS, NX, 2))
    o.append(T(x0 + w / 2, yD + 22, '(m − 1)A_st = 8400 mm²', 13, fill=NX, bold=True))
    yb = top + 260.6 * s
    o.append(L(x0 - 6, yb, x0 + w + 60, yb, INK, 1.6, '6 5'))
    o.append(T(x0 + w + 4, yb - 6, 'ȳ = 260.6', 13, 'start', bold=True))
    o.append(T(x0 + w + 4, yb + 34, 'I = 3443 × 10⁶ mm⁴', 13, 'start'))
    o.append(T(x0 + w + 4, yb + 52, 'M_cr = 50.3 kN·m', 13, 'start', bold=True))
    o.append(T(x0 + w / 2, yD + 40, 'whole concrete acts', 13, fill=MUT))
    # cracked
    x2 = 420
    o.append(T(x2 + w / 2 + 40, 36, 'Cracked (M = 60 kN·m)', 15, bold=True))
    xc = top + 140.7 * s
    o.append(R(x2, top, w, 140.7 * s, ACS, AC, 2))
    o.append(R(x2, xc, w, (500 - 140.7) * s, 'none', L2, 1.5, dash='5 4'))
    for i in range(5):
        cx = x2 + 20 + i * 27
        o.append(P([(cx, yD), (cx + 3, yD - 40), (cx - 2, yD - 80), (cx + 2, xc + 18)], L2, 1.3))
    o.append(R(x2 + w / 2 - 96, yd - 6, 192, 12, NXS, NX, 2))
    o.append(T(x2 + w / 2, yD + 22, 'mA_st = 9600 mm²', 13, fill=NX, bold=True))
    o.append(L(x2 - 6, xc, x2 + w + 60, xc, INK, 1.6, '6 5'))
    o.append(T(x2 + w + 4, xc - 6, 'x = 140.7', 13, 'start', bold=True))
    o.append(T(x2 + w + 4, xc + 22, 'I_cr = 1197 × 10⁶', 13, 'start'))
    o.append(T(x2 + w + 4, xc + 40, 'f_c = 7.05, f_s = 124.0', 13, 'start'))
    o.append(T(x2 + w / 2, yD + 40, 'tension concrete ignored', 13, fill=MUT))
    o.append(T(360, yD + 72, 'b = 300, D = 500, d = 450, A_st = 1200 mm², M25, m = 8', 14, fill=MUT))
    return int(yD + 86), ''.join(o)
FIG[7] = (f7, 'The same 300 × 500 beam two ways. Before cracking the whole concrete acts with (m − 1)Ast = 8400 mm² added at the steel, the axis is 260.6 mm down and Mcr = 50.3 kN·m; after cracking only the concrete above x = 140.7 mm and mAst = 9600 mm² remain, and Icr falls to 1197 × 10⁶ mm⁴.',
          'Two beam sections side by side: an uncracked one fully shaded with a thin steel strip, and a cracked one shaded only above a shallow neutral axis, with cracks below.')


_CAP = [('Mu,lim', 'M<sub>u,lim</sub>'), ('Mu/bd²', 'M<sub>u</sub>/bd²'), ('0.45fck', '0.45f<sub>ck</sub>'), ('mAst', 'mA<sub>st</sub>'),
        ('Ast', 'A<sub>st</sub>'), ('Mcr', 'M<sub>cr</sub>'), ('Icr', 'I<sub>cr</sub>'), ('yf', 'y<sub>f</sub>'), ('pt', 'p<sub>t</sub>'),
        ('kt', 'k<sub>t</sub>'), ('fs', 'f<sub>s</sub>')]


def _cap(c):
    for a, b in _CAP:
        c = re.sub(r'(?<![A-Za-z>])' + re.escape(a) + r'(?![A-Za-z<])', b, c)
    return c


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': _cap(cap), 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}


def text_fixes(k):
    return []
