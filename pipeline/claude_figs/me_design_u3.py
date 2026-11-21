"""Claude's hand-drawn figures for me-design-u3 (Design of Machine Elements: shafts, keys, couplings, clutches and brakes,
connecting rods and crankshafts), one per chapter, each drawn from that chapter's own worked example and numbers. Curves are
computed (the whirl curve from y/e = r²/√((1 − r²)² + (2ζr)²), the clutch pressures from the example's W and radii).
Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    return re.sub(r'([A-Za-zα-ωΔσ])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def dim(x1, y1, x2, y2, c=MUT):
    """dimension line with arrowheads both ends"""
    return L(x1, y1, x2, y2, c, 1.4, arrow='m') + L(x2, y2, x1, y1, c, 1.4, arrow='m')


FIG = {}


# ---- 3.1 the pulley shaft of worked example 1: loads and bending moment ----
def f1():
    o = []
    xa, xb = 110, 630
    s = (xb - xa) / 900.0
    xc = xa + 300 * s
    ys = 96
    o.append(T(360, 26, 'Pulley shaft: 10 kW at 500 rpm, T = 191 N·m', 15, bold=True))
    o.append(R(xa - 20, ys - 8, xb - xa + 40, 16, PANEL, AC, 4))
    o.append(R(xc - 14, ys - 46, 28, 92, ACS, AC, 4))
    o.append(T(xc + 22, ys - 30, 'pulley Ø400', 13, 'start', INK))
    # belt pull down from the pulley
    o.append(L(xc, ys + 48, xc, ys + 112, NX, 3, arrow='x'))
    o.append(T(xc + 12, ys + 80, 'T_1 + T_2 = 1910 N', 14, 'start', NX, bold=True))
    o.append(T(xc + 12, ys + 100, '(T_1 = 1432 N, T_2 = 477 N)', 13, 'start', MUT))
    # bearings with upward reactions
    for x, lab, r in ((xa, 'A', 'R_A = 1273 N'), (xb, 'B', 'R_B = 637 N')):
        o.append(P([(x - 14, ys + 34), (x, ys + 10), (x + 14, ys + 34), (x - 14, ys + 34)], AC, 2, fill=PANEL))
        o.append(T(x - 22, ys + 30, lab, 14, 'end', bold=True))
        o.append(L(x, ys + 104, x, ys + 40, LV, 3, arrow='l'))
        o.append(T(x + (10 if lab == 'A' else -10), ys + 100, r, 13, 'start' if lab == 'A' else 'end', LV, bold=True))
    yd = ys + 138
    o.append(dim(xa, yd, xc, yd)); o.append(Tb((xa + xc) / 2, yd + 5, '300 mm', 13, fill=MUT))
    o.append(dim(xc, yd, xb, yd)); o.append(Tb((xc + xb) / 2, yd + 5, '600 mm', 13, fill=MUT))
    y0 = 390; hpk = 100
    o.append(L(xa, y0, xb, y0, L2, 1.5))
    o.append(P([(xa, y0), (xc, y0 - hpk), (xb, y0), (xa, y0)], AC, 2.5, fill=ACS))
    o.append(T(xc, y0 - hpk - 10, 'M = 382 N·m', 14, bold=True))
    o.append(T(xa - 8, y0 + 4, '0', 13, 'end', MUT)); o.append(T(xb + 8, y0 + 4, '0', 13, 'start', MUT))
    o.append(T(480, y0 - 60, 'bending moment', 13, fill=MUT))
    o.append(boxt(100, 410, 520, 52, ['T_e = √((1.5 × 382)² + 191²) = 604 N·m', 'τ = 85.5 MPa (keyway), so d = 33.0 mm: use 35 mm'], PANEL, AC, 14))
    return 474, ''.join(o)


FIG[1] = (f1, 'The shaft of the first worked example. The belt pulls the shaft down with T₁ + T₂ = 1910 N, the bearings push up with '
              '1273 N and 637 N, and the bending moment peaks at 382 N·m under the pulley. With the torque of 191 N·m this gives d = 33 mm.',
          'A shaft on bearings A and B, 900 millimetres apart, with a pulley 300 millimetres from A. The belt pulls down 1910 newtons; '
          'reactions are 1273 newtons at A and 637 newtons at B. Below, a triangular bending moment diagram peaking at 382 newton metres under the pulley. '
          'A box gives the equivalent torque 604 newton metres and the diameter 33 millimetres, rounded to 35.')


# ---- 3.2 critical speed of the worked example: rotor sag and whirl curve ----
def f2():
    o = []
    # left: the shaft with its rotor and static sag
    o.append(T(150, 26, '60 mm shaft, 1.2 m span', 14, bold=True))
    xa, xb, ys = 30, 270, 92
    pts = [(xa + i * (xb - xa) / 40, ys + 22 * math.sin(math.pi * i / 40)) for i in range(41)]
    o.append(L(xa, ys, xb, ys, L2, 1.5, dash='5 4'))
    o.append(P(pts, AC, 4))
    o.append(R(140, ys + 2, 20, 42, ACS, AC, 3))
    o.append(T(150, ys + 64, 'rotor 25 kg', 13))
    for x in (xa, xb):
        o.append(P([(x - 10, ys + 22), (x, ys + 4), (x + 10, ys + 22), (x - 10, ys + 22)], AC, 2, fill=PANEL))
    o.append(dim(196, ys, 196, ys + 21, NX)); o.append(T(204, ys + 16, 'δ', 14, 'start', NX, bold=True))
    o.append(boxt(20, 180, 260, 136, ['rotor alone: N_1 = 3590 rpm', 'shaft alone: N_s = 4956 rpm', 'Dunkerley:', '1/N_c² = 1/N_1² + 1/N_s²', 'N_c = 2908 rpm'],
                  PANEL, AC, 14))
    # right: whirl curve y/e against speed
    x0, x1, y0, y1 = 360, 690, 50, 300
    Nc, z = 2908.0, 0.1
    fx = lin(0, 6000, x0, x1); fy = lin(0, 6, y1, y0)
    lo, hi = 0.75 * Nc, 1.25 * Nc
    o.append(R(fx(lo), y0, fx(hi) - fx(lo), y1 - y0, NXS, NXS, 0, 0))
    o.append(axes(x0, x1, y0, y1, [0, 2000, 4000, 6000], [0, 2, 4, 6], fx, fy, 'shaft speed, rpm', 'whirl y / e'))
    curve = []
    for i in range(0, 301):
        N = 6000 * i / 300; r = N / Nc
        y = r * r / math.sqrt((1 - r * r) ** 2 + (2 * z * r) ** 2)
        curve.append((fx(N), fy(min(y, 6))))
    o.append(P(curve, AC, 3))
    o.append(L(fx(Nc), y0, fx(Nc), y1, NX, 1.5, dash='4 3'))
    o.append(L(fx(0), fy(1), fx(6000), fy(1), L2, 1.2, dash='3 4'))
    o.append(T(fx(5900), fy(1) + 18, 'y tends to e', 13, 'end', MUT))
    o.append(Tb(fx(Nc), y0 - 8, 'N_c = 2908', 13, fill=NX, bold=True))
    o.append(T(fx(1050), fy(4.6), 'keep out:', 13, fill=NX))
    o.append(T(fx(1050), fy(4.6) + 17, '2180 to 3630', 13, fill=NX))
    return 350, ''.join(o)


FIG[2] = (f2, 'The second worked example. The rotor alone gives 3590 rpm and the shaft’s own mass 4956 rpm; Dunkerley combines them to 2908 rpm. '
              'The curve (damping ratio 0.1) shows the whirl peak there and the shaded band to keep the running speed out of; far above it the deflection tends to e.',
          'Left: a shaft on two bearings sagging under a central 25 kilogram rotor, with critical speeds 3590 rpm for the rotor, 4956 rpm for the shaft and 2908 rpm combined. '
          'Right: whirl amplitude over eccentricity against speed from 0 to 6000 rpm, peaking at 2908 rpm, with a shaded band from 2180 to 3630 rpm, and tending to 1 at high speed.')


# ---- 3.3 the sunk key of the worked example: shear plane and crushing face ----
def f3():
    o = []
    cx, cy, sc = 200, 205, 3.0
    rs, rh = 25 * sc, 50 * sc
    w, h = 14 * sc, 9 * sc
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{rh}" style="fill:{PANEL};stroke:{AC};stroke-width:2"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{rs}" style="fill:{ACS};stroke:{AC};stroke-width:2.5"/>')
    o.append(T(cx, cy + 6, 'shaft Ø50', 14, bold=True))
    o.append(T(cx, cy + rh - 22, 'hub', 14, fill=MUT))
    top = cy - rs
    o.append(R(cx - w / 2, top - h / 2, w, h, NXS, NX, 2))
    # shear plane at the shaft surface
    o.append(L(cx - w / 2 - 30, top, cx + w / 2 + 30, top, LV, 2, dash='5 3'))
    # force on the key from the hub (left face) and shaft (right face)
    o.append(L(cx - w / 2 - 54, top - h / 4, cx - w / 2 - 3, top - h / 4, NX, 2.5, arrow='x'))
    o.append(L(cx + w / 2 + 54, top + h / 4, cx + w / 2 + 3, top + h / 4, NX, 2.5, arrow='x'))
    o.append(T(cx - w / 2 - 58, top - h / 4 - 8, 'F', 14, 'end', NX, bold=True))
    o.append(T(cx + w / 2 + 58, top + h / 4 + 18, 'F', 14, 'start', NX, bold=True))
    # key dimension labels
    o.append(dim(cx - w / 2, top - h / 2 - 16, cx + w / 2, top - h / 2 - 16))
    o.append(T(cx, top - h / 2 - 24, 'w = 14', 13, fill=MUT))
    o.append(T(cx + rh + 14, top - h / 2 + 4, 'key 14 × 9', 14, 'start', NX, bold=True))
    o.append(L(cx + w / 2 + 4, top - h / 2 + 2, cx + rh + 10, top - h / 2 + 2, MUT, 1, dash='3 3'))
    o.append(T(cx + rh + 14, top + 20, 'shear plane at the', 13, 'start', LV))
    o.append(T(cx + rh + 14, top + 36, 'shaft surface', 13, 'start', LV))
    # working on the right
    o.append(boxt(440, 210, 260, 136, ['F = 2T/d = 12 732 N', 'shear: l ≥ F/(wτ) = 22.7 mm', 'crushing on h/2 = 4.5 mm:', 'l ≥ F/(4.5 σ_c) = 35.4 mm', 'adopt l = 40 mm', 'σ_c = 70.7 MPa ≤ 80'], PANEL, AC, 14))
    return 360, ''.join(o)


FIG[3] = (f3, 'Section through the keyed shaft of the worked example. The torque pushes the hub and shaft against opposite sides of the key: the key can shear on '
              'the plane at the shaft surface (area w × l) or crush on the half height h/2 that sits in the hub. Crushing needs the longer key, 35.4 mm.',
          'Cross-section of a 50 millimetre shaft in a hub with a 14 by 9 millimetre key at the top, half in the shaft and half in the hub. Opposite forces F act on its sides; '
          'a dashed shear plane runs along the shaft surface. A box gives F 12 732 newtons, shear length 22.7 millimetres, crushing length 35.4 millimetres and the adopted 40 millimetres.')


# ---- 3.4 the protected flange coupling of the worked example ----
def f4():
    o = []
    s = 1.15
    ax, jx = 230, 360          # axis y, joint x
    rs, rhub, rpc, rod = 25 * s, 50 * s, 75 * s, 100 * s
    hl, ft, rim = 80 * s, 25 * s, 12.5 * s
    o.append(L(40, ax, 680, ax, L2, 1.2, dash='10 4 2 4'))
    for sg in (-1, 1):  # left and right halves
        # shaft
        x0 = jx - sg * (hl + 70)
        o.append(R(min(x0, jx), ax - rs, abs(jx - x0), 2 * rs, ACS, AC, 2))
        # hub
        hx = jx - sg * hl
        o.append(R(min(hx, jx), ax - rhub, hl, 2 * rhub, PANEL, AC, 2, sw=2))
        # flange
        fx = jx - sg * ft
        o.append(R(min(fx, jx), ax - rod, ft, 2 * rod, PANEL, AC, 2, sw=2.5))
        # protecting rim on the outer side of the flange
        rx = fx - sg * 22
        o.append(R(min(rx, fx), ax - rod, 22, rim, PANEL, AC, 2))
        o.append(R(min(rx, fx), ax + rod - rim, 22, rim, PANEL, AC, 2))
    # bolts through both flanges at the pitch circle
    for sg in (-1, 1):
        y = ax + sg * rpc
        o.append(R(jx - ft - 14, y - 5.75, 2 * ft + 28, 11.5, NXS, NX, 2))
        for xx in (jx - ft - 14, jx + ft + 4):
            o.append(R(xx, y - 10, 10, 20, NXS, NX, 2))
    # labels
    o.append(T(jx, ax - rod - 14, 'joint face', 13, fill=MUT))
    o.append(L(jx + ft + 18, ax - rpc, 520, ax - rpc, MUT, 1, dash='3 3')); o.append(T(524, ax - rpc + 5, 'M10 bolt on PCD 150', 13, 'start', NX, bold=True))
    o.append(L(jx + ft + 24, ax - rod + 6, 520, ax - rod + 6, MUT, 1, dash='3 3')); o.append(T(524, ax - rod + 11, 'rim 12.5 covers nut', 13, 'start'))
    o.append(L(jx + hl - 10, ax - rhub + 12, 520, ax - 40, MUT, 1, dash='3 3')); o.append(T(524, ax - 35, 'hub Ø100 × 80', 13, 'start'))
    o.append(T(jx + hl + 74, ax + 46, 'shaft Ø50', 13, 'end', AC, bold=True))
    o.append(T(524, ax + rpc + 5, 'flange t = 25', 13, 'start'))
    o.append(L(jx + ft + 4, ax + rpc - 18, 520, ax + rpc, MUT, 1, dash='3 3'))
    o.append(T(524, ax + rod - 2, 'outer Ø200', 13, 'start'))
    o.append(L(jx + ft + 2, ax + rod - 4, 520, ax + rod - 6, MUT, 1, dash='3 3'))
    o.append(boxt(30, 22, 230, 44, ['bolt force F = 2T/(n D_1)', '= 2387 N each'], PANEL, NX, 13))
    o.append(T(40, ax + rod + 40, 'torque path: shaft → key → hub → flange → bolts → flange → hub → key → shaft', 13, 'start', MUT))
    return ax + rod + 56, ''.join(o)


FIG[4] = (f4, 'Half-section of the protected flange coupling designed in the first worked example (to scale). Torque passes through the keyed hubs to the flanges '
              'and across the joint by the four M10 fitted bolts on the 150 mm circle; the rims cover the bolt heads and nuts.',
          'Section of a flange coupling joining two 50 millimetre shafts. Each shaft has a hub of 100 millimetres diameter and 80 millimetres length and a flange 25 millimetres thick '
          'and 200 millimetres across, with a protecting rim. Bolts cross both flanges at a 150 millimetre pitch circle. A box gives the bolt force 2387 newtons.')


# ---- 3.5 single-plate clutch of the worked example and its pressure under the two theories ----
def f5():
    o = []
    # left: the plate stack
    yc = 210
    o.append(T(160, 28, 'single plate, two pairs', 14, bold=True))
    o.append(R(40, 60, 46, 270, PANEL, AC, 4)); o.append(T(63, 380, 'flywheel', 13))
    o.append(R(98, 90, 12, 210, NXS, NX, 2)); o.append(R(122, 90, 12, 210, NXS, NX, 2))
    o.append(R(110, 80, 12, 230, ACS, AC, 2)); o.append(T(116, 70, 'plate', 13))
    o.append(R(146, 70, 40, 260, PANEL, AC, 4)); o.append(T(170, 380, 'pressure plate', 13))
    for y in (110, 200, 290):
        o.append(L(240, y, 192, y, LV, 3, arrow='l'))
    o.append(T(246, 170, 'W = 5 kN', 14, 'start', LV, bold=True))
    o.append(T(246, 188, '(springs)', 13, 'start', LV))
    o.append(T(92, 350, '1', 14, 'middle', NX, bold=True)); o.append(T(140, 350, '2', 14, 'middle', NX, bold=True))
    o.append(T(116, 404, 'rubbing pairs 1 and 2: n = 2', 13, fill=NX))
    # right: pressure against radius
    x0, x1, y0, y1 = 400, 690, 60, 330
    fx = lin(90, 160, x0, x1); fy = lin(0, 0.18, y1, y0)
    o.append(axes(x0, x1, y0, y1, [100, 125, 150], [0, 0.06, 0.12, 0.18], fx, fy, 'radius r, mm', 'pressure p, MPa', yfmt=lambda v: f'{v:.2f}'))
    W, ri, ro = 5000.0, 100.0, 150.0
    pu = W / (math.pi * (ro ** 2 - ri ** 2))
    C = W / (2 * math.pi * (ro - ri))
    o.append(L(fx(ri), fy(pu), fx(ro), fy(pu), NX, 3))
    o.append(P([(fx(r), fy(C / r)) for r in range(100, 151, 2)], AC, 3))
    o.append(T(fx(ri) + 6, fy(C / ri) - 8, 'wear: p r = const, 0.159 at r_i', 13, 'start', AC, bold=True))
    o.append(T(fx(ri) + 6, fy(pu) + 22, 'uniform pressure 0.127', 13, 'start', NX, bold=True))
    o.append(T(fx(ro) - 4, fy(C / ro) + 20, '0.106 at r_o', 13, 'end', AC))
    o.append(boxt(400, 392, 290, 46, ['T = μ W n (r_o + r_i)/2', '= 0.3 × 5000 × 2 × 0.125 = 375 N·m'], PANEL, AC, 13))
    return 452, ''.join(o)


FIG[5] = (f5, 'The clutch of the worked example. The spring force of 5 kN clamps one lined plate between the flywheel and the pressure plate, so two pairs rub. '
              'After running in, p × r is constant and the pressure falls from 0.159 MPa at r<sub>i</sub> to 0.106 MPa at r<sub>o</sub>; a new lining carries a uniform 0.127 MPa.',
          'Left: a clutch stack of flywheel, a plate lined on both faces and a pressure plate pushed by springs with 5 kilonewtons, giving two rubbing pairs. '
          'Right: pressure against radius from 100 to 150 millimetres; the uniform-wear curve falls from 0.159 to 0.106 megapascals, the uniform-pressure line is flat at 0.127. '
          'A box gives the torque 375 newton metres.')


# ---- 3.6 connecting rod of the worked example: I-section and the two buckling planes ----
def f6():
    o = []
    s = 4.0
    t, B, H = 8 * s, 32 * s, 40 * s
    cx, cy = 175, 210
    xl, yt = cx - B / 2, cy - H / 2
    # I-section outline
    pts = [(xl, yt), (xl + B, yt), (xl + B, yt + t), (cx + t / 2, yt + t), (cx + t / 2, yt + H - t), (xl + B, yt + H - t), (xl + B, yt + H),
           (xl, yt + H), (xl, yt + H - t), (cx - t / 2, yt + H - t), (cx - t / 2, yt + t), (xl, yt + t), (xl, yt)]
    o.append(P(pts, AC, 2.5, fill=ACS))
    o.append(L(xl - 26, cy, xl + B + 26, cy, NX, 1.4, dash='6 3')); o.append(T(xl + B + 30, cy + 5, 'x', 14, 'start', NX, bold=True))
    o.append(L(cx, yt - 22, cx, yt + H + 22, LV, 1.4, dash='6 3')); o.append(T(cx + 6, yt - 26, 'y', 14, 'start', LV, bold=True))
    o.append(dim(xl, yt + H + 34, xl + B, yt + H + 34)); o.append(T(cx, yt + H + 54, 'B = 4t = 32', 13, fill=MUT))
    o.append(dim(xl - 34, yt, xl - 34, yt + H)); o.append(T(xl - 42, cy - 40, 'H = 5t', 13, 'end', MUT)); o.append(T(xl - 42, cy - 22, '= 40', 13, 'end', MUT))
    o.append(T(xl + B + 8, yt + t - 6, 't = 8', 13, 'start', INK, bold=True))
    o.append(T(cx, 30, 'I-section, t = 8 mm', 14, bold=True))
    o.append(T(cx, 52, 'A = 11t² = 704 mm²', 13, fill=MUT))
    # rod elevation, horizontal: small end left, big end right
    ys = 150; xs, xb = 410, 656
    o.append(f'<circle cx="{xs}" cy="{ys}" r="30" style="fill:{PANEL};stroke:{AC};stroke-width:2.5"/>')
    o.append(f'<circle cx="{xs}" cy="{ys}" r="16" style="fill:{FIGBG};stroke:{AC};stroke-width:2"/>')
    o.append(f'<circle cx="{xb}" cy="{ys}" r="44" style="fill:{PANEL};stroke:{AC};stroke-width:2.5"/>')
    o.append(f'<circle cx="{xb}" cy="{ys}" r="26" style="fill:{FIGBG};stroke:{AC};stroke-width:2"/>')
    o.append(P([(xs + 28, ys - 10), (xb - 42, ys - 16), (xb - 42, ys + 16), (xs + 28, ys + 10), (xs + 28, ys - 10)], AC, 2.5, fill=ACS))
    o.append(T(xs, ys - 40, 'pin Ø36', 13)); o.append(T(xb, ys - 54, 'crankpin Ø56', 13))
    o.append(dim(xs, ys + 62, xb, ys + 62)); o.append(Tb((xs + xb) / 2, ys + 67, 'L = 240 mm', 13, fill=MUT))
    o.append(L(xs - 86, ys, xs - 34, ys, NX, 3, arrow='x')); o.append(T(xs - 60, ys - 12, 'F_p', 14, fill=NX, bold=True))
    o.append(T(xs - 60, ys + 26, '31.4 kN', 13, fill=NX))
    o.append(boxt(330, 252, 360, 120, ['in plane of motion: pinned, length L', 'about x: Rankine, k_xx² = 3.17t²', 'out of plane: ends fixed, length L/2',
                                       'P_cr = 223.9 kN = 7.1 × F_p'], PANEL, AC, 14))
    return 386, ''.join(o)


FIG[6] = (f6, 'The connecting rod of the first worked example. The I-section with t = 8 mm has B = 32 mm and H = 40 mm; the rod is a 240 mm strut carrying the '
              '31.4 kN gas force. Pinned in the plane of motion, it is designed for buckling about x, and Rankine’s formula gives 223.9 kN, 7.1 times the gas force.',
          'Left: an I-section 32 millimetres wide and 40 millimetres deep with flange and web 8 millimetres thick, area 704 square millimetres, with x and y axes. '
          'Right: the rod between a 36 millimetre piston pin and a 56 millimetre crankpin, 240 millimetres apart, pushed by a 31.4 kilonewton gas force. '
          'A box notes the pinned and fixed end conditions and the buckling load 223.9 kilonewtons.')


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


spec_ = make_spec(FIG)


def spec(k):
    if k not in FIG: raise KeyError(k)
    d = spec_(k)
    d['after_section'] = {1: 1, 2: 3, 3: 2, 4: 1, 5: 2, 6: 1}[k]
    return d


def drop_sources():
    return ['nptel.ac.in', 'ocw.mit.edu']
