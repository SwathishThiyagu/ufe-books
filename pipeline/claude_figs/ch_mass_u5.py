"""Claude's hand-drawn figures for ch-mass-u5 (Liquid extraction and leaching), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
S3 = math.sqrt(3) / 2


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def smooth(pts):
    """Catmull-Rom spline through pts as an SVG path"""
    d = f'M{pts[0][0]:.1f},{pts[0][1]:.1f}'
    for i in range(len(pts) - 1):
        p0 = pts[max(i - 1, 0)]; p1 = pts[i]; p2 = pts[i + 1]; p3 = pts[min(i + 2, len(pts) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f' C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}'
    return d


def path(d, c=AC, w=2.5, dash=None, fill='none'):
    da = f';stroke-dasharray:{dash}' if dash else ''
    return f'<path d="{d}" style="fill:{fill};stroke:{c};stroke-width:{w}{da}"/>'


def tank(x, y, w, h, fill=PANEL, stroke=AC):
    return R(x, y, w, h, fill, stroke, 6, 2)


# ---- 5.1 the triangle with the worked example's tie line ----
def f1():
    o = []
    side, bx, by = 430, 40, 410            # B corner at (bx, by)

    def pt(a, s):                           # mass fractions of A and S -> svg
        return bx + side * (s + a / 2), by - side * a * S3
    A, B, Sx = pt(1, 0), pt(0, 0), pt(0, 1)
    o.append(f'<polygon points="{A[0]:.1f},{A[1]:.1f} {B[0]:.1f},{B[1]:.1f} {Sx[0]:.1f},{Sx[1]:.1f}" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    for g in (0.1, 0.2, 0.3):               # lines of constant A
        p, q = pt(g, 0), pt(g, 1 - g)
        o.append(L(p[0], p[1], q[0], q[1], 'var(--line)', 1))
        if g < 0.25: o.append(T(p[0] - 8, p[1] + 4, f'{g:.1f}', 13, 'end', MUT))
    o.append(T(pt(0.5, 0)[0] - 14, pt(0.5, 0)[1] + 4, sb('x', 'A') + ' lines', 13, 'end', MUT))
    # binodal (sketch of a model system) through the example's raffinate and extract
    bn = [(0, 0.015), (0.10, 0.03), (0.18, 0.06), (0.245, 0.12), (0.275, 0.20), (0.28, 0.27), (0.27, 0.36),
          (0.24, 0.48), (0.20, 0.62), (0.1543, 0.80), (0.08, 0.91), (0, 0.965)]
    o.append(path(smooth([pt(a, s) for a, s in bn]), LV, 2.5))
    P_ = pt(0.28, 0.27)
    o.append(C(P_[0], P_[1], 4.5, LV))
    o.append(Tb(P_[0], P_[1] - 12, 'plait point', 13, fill=LV))
    o.append(T(pt(0.21, 0.07)[0] - 6, pt(0.21, 0.07)[1] - 6, 'binodal curve', 13, 'end', LV))
    # feed line F-S, mixture, tie line
    F, Sp, M = pt(0.30, 0), pt(0, 1), pt(30 / 220, 120 / 220)
    Rp, Ep = pt(0.10, 0.03), pt(0.1543, 0.80)
    o.append(L(F[0], F[1], Sp[0], Sp[1], L2, 2, '6 4'))
    o.append(L(Rp[0], Rp[1], Ep[0], Ep[1], AC, 3))
    for (p, lab, dx, dy, anc, col) in ((F, 'F (0.30)', -10, 4, 'end', INK), (M, 'M', 0, -12, 'middle', NX), (Rp, 'R', 8, 20, 'start', AC),
                                       (Ep, 'E', 10, -8, 'start', AC)):
        o.append(C(p[0], p[1], 6, col))
        o.append(T(p[0] + dx, p[1] + dy, lab, 15, anc, col, bold=True))
    o.append(T(A[0], A[1] - 10, 'A (acid)', 14, bold=True))
    o.append(T(B[0] - 2, B[1] + 22, 'B (water)', 14, 'start', bold=True))
    o.append(T(Sx[0] + 2, Sx[1] + 22, 'S (solvent)', 14, 'end', bold=True))
    o.append(T(pt(0.55, 0.2)[0], pt(0.55, 0.2)[1], 'one phase', 13, 'middle', MUT))
    o.append(T(pt(0.10, 0.45)[0], pt(0.10, 0.45)[1] + 30, 'two layers', 13, 'middle', MUT))
    # numbers
    o.append(boxt(492, 40, 216, 170, ['F = 100 kg, 30 % A', 'S = 120 kg pure', 'M = 220 kg', sb('x', 'A') + ' = 0.136, ' + sb('x', 'S') + ' = 0.545',
                                     'FM/MS = 120/100'], PANEL, L2, 14))
    o.append(boxt(492, 228, 216, 170, ['tie line through M', 'R: ' + sb('x', 'A') + ' = 0.100 → 72.7 kg', 'E: ' + sb('y', 'A') + ' = 0.154 → 147.3 kg',
                                      'E/M = RM/RE = 0.669', 'K = 1.54, β = 29.4'], ACS, AC, 14))
    return 440, ''.join(o)
FIG[1] = (f1, 'The worked example on the triangle. M lies on the line from F to S with FM/MS = 120/100; the tie line through M ends at the raffinate R and the extract E on the binodal curve (drawn here as a sketch through the two measured layers), and the lever rule gives E = 147.3 kg and R = 72.7 kg.',
          'Equilateral triangle with corners A, B and S, a binodal curve with a plait point, the feed point F on side AB, a dashed line from F to S with the mixture point M on it, and a tie line through M joining the raffinate R and the extract E.')


# ---- 5.2 three cross-current stages ----
def f2():
    o = []
    xs = [120, 310, 500]
    y0, w, h = 120, 104, 70
    o.append(T(20, 28, 'Feed: 375 kg carrier + 125 kg solute (X₀ = 0.333)', 14, 'start', bold=True))
    o.append(L(40, y0 + h / 2, xs[0] - 2, y0 + h / 2, AC, 2.5, arrow='n'))
    Xs, Ex = ['0.1613', '0.0780', '0.0378'], ['64.5', '31.2', '15.1']
    for i, x in enumerate(xs):
        o.append(R(x, y0, w, h, PANEL, AC, 8, 2))
        o.append(T(x + w / 2, y0 + 30, f'Stage {i + 1}', 15, bold=True))
        o.append(T(x + w / 2, y0 + 52, 'ε = 1.067', 13, fill=MUT))
        o.append(L(x + w / 2, y0 - 44, x + w / 2, y0 - 2, LV, 2.5, arrow='l'))
        o.append(T(x + w / 2, y0 - 52, '200 kg solvent', 13, fill=LV))
        o.append(L(x + w / 2, y0 + h, x + w / 2, y0 + h + 40, NX, 2.5, arrow='x'))
        o.append(T(x + w / 2, y0 + h + 58, f'extract: {Ex[i]} kg A', 13, fill=NX))
        nx = xs[i + 1] if i < 2 else 690
        o.append(L(x + w, y0 + h / 2, nx - 2, y0 + h / 2, AC, 2.5, arrow='n'))
        o.append(T((x + w + nx) / 2, y0 + h / 2 - 10, 'X = ' + Xs[i], 13))
    o.append(T(690, y0 + h / 2 + 26, 'raffinate', 13, 'end', AC))
    # bars: solute left
    by, bh, sc = 330, 22, 3.6
    o.append(T(20, 286, 'Solute still in the raffinate (kg)', 14, 'start', bold=True))
    data = [('feed', 125.0, AC), ('after 1', 60.5, AC), ('after 2', 29.3, AC), ('after 3', 14.2, LV), ('one stage, 600 kg', 29.8, NX)]
    for j, (lab, v, c) in enumerate(data):
        y = 300 + j * 32
        o.append(T(150, y + 16, lab, 13, 'end', MUT))
        o.append(R(160, y, v * sc, bh, c, c, 3, 1))
        o.append(T(166 + v * sc, y + 16, f'{v:.1f}', 13, 'start'))
    o.append(T(20, 478, 'Three portions of 200 kg leave 14.2 kg (88.7 % recovered); all 600 kg in one stage leaves 29.8 kg (76.2 %).', 13, 'start', MUT))
    return 492, ''.join(o)
FIG[2] = (f2, 'The worked example: the raffinate passes through three stages, each fed 200 kg of fresh solvent, and each stage leaves 1/2.067 of the solute it receives. The bars compare the solute left after each stage with one stage that uses all 600 kg.',
          'Three stage boxes in a row with the raffinate passing left to right, fresh solvent entering each from above and an extract leaving each below, and a bar chart of the solute left: 125, 60.5, 29.3 and 14.2 kilograms, against 29.8 kilograms for a single stage with all the solvent.')


# ---- 5.3 right-angled triangle with the difference point ----
def f3():
    o = []
    x0, sx, yb, sy = 380, 300, 330, 700      # x_S = 0 at x0; y = yb - sy*x_A
    fx = lambda s: x0 + s * sx
    fy = lambda a: yb - a * sy
    # axes
    o.append(L(fx(-1.2), yb, fx(1.05), yb, L2, 1.5))
    o.append(L(x0, yb, x0, fy(0.42), INK, 2))
    for a in (0.1, 0.2, 0.3, 0.4):
        o.append(L(x0 - 5, fy(a), x0, fy(a), L2, 1.5)); o.append(T(x0 - 8, fy(a) + 4, f'{a:.1f}', 13, 'end', MUT))
    for s in (0.5, 1.0):
        o.append(L(fx(s), yb, fx(s), yb + 5, L2, 1.5)); o.append(T(fx(s), yb + 20, f'{s:.1f}', 13, fill=MUT))
    o.append(T(fx(0.5), yb + 40, sb('x', 'S') + ', mass fraction of solvent', 13, fill=MUT))
    o.append(T(x0 + 8, fy(0.42) + 2, sb('x', 'A') + ' (stretched scale)', 13, 'start', MUT))
    # hypotenuse (extract branch for immiscible B and S)
    o.append(L(fx(0.58), fy(0.42), fx(1.0), fy(0.0), LV, 2.5))
    o.append(T(fx(0.97), fy(0.2), 'extract branch', 13, 'end', LV))
    o.append(T(x0 - 10, fy(0.03), 'raffinate', 13, 'end', LV))
    o.append(T(x0 - 10, fy(0.03) + 15, 'branch', 13, 'end', LV))
    D = (-1.870, 0.2521)
    Fp, S_ = (0, 0.30), (1.0, 0.0)
    Rn = [(0, 0.2367), (0, 0.1663), (0, 0.0879)]
    En = [(0.6825, 0.3175), (0.7697, 0.2303), (0.8738, 0.1262)]
    # Delta lines: Delta-F-E1, Delta-R1-E2, Delta-R2-E3, Delta-R3-S, drawn to the clipped left edge
    xl = -1.2
    def ray(p, q, c=L2):
        # line from the left edge through p to q, along Delta's direction
        t = (xl - D[0]) / (q[0] - D[0])
        yl = D[1] + t * (q[1] - D[1])
        return L(fx(xl), fy(yl), fx(q[0]), fy(q[1]), c, 1.6, '5 4')
    o.append(ray(Fp, En[0])); o.append(ray(Rn[0], En[1])); o.append(ray(Rn[1], En[2])); o.append(ray(Rn[2], S_))
    for i in range(3):
        o.append(L(fx(Rn[i][0]), fy(Rn[i][1]), fx(En[i][0]), fy(En[i][1]), AC, 2.8))
        o.append(Tb((fx(Rn[i][0]) + fx(En[i][0])) / 2 + 10, (fy(Rn[i][1]) + fy(En[i][1])) / 2 - 6, f'stage {i + 1}', 13, fill=AC))
    for p, lab, dx, dy in ((Fp, 'F', 10, -6), (Rn[0], 'R₁', 10, 6), (Rn[1], 'R₂', 10, 14), (Rn[2], 'R₃', 10, 16),
                           (En[0], 'E₁', 8, -8), (En[1], 'E₂', 10, -6), (En[2], 'E₃', 10, -6), (S_, 'S', 6, -10)):
        o.append(C(fx(p[0]), fy(p[1]), 5, NX if lab == 'F' else AC))
        o.append(T(fx(p[0]) + dx, fy(p[1]) + dy, lab, 14, 'start', bold=True))
    # Delta off the drawing
    o.append(L(fx(-0.95), fy(0.37), fx(-1.18), fy(0.37), NX, 2.5, arrow='x'))
    o.append(T(fx(-1.2), fy(0.37) - 12, 'to Δ at (−1.87, 0.252)', 13, 'start', NX, bold=True))
    o.append(T(fx(-1.2), fy(0.37) + 24, 'Δ = F − E₁ = R₃ − S', 13, 'start', NX))
    o.append(T(fx(-1.2), fy(0.37) + 42, '267.4 kg/h: A 67.4, S −500', 13, 'start', NX))
    o.append(boxt(24, 340, 300, 104, ['ε = 1.071, three ideal stages', sb('X', '3') + ' = 0.0963, ' + sb('Y', '1') + ' = 0.4652', 'recovery 77.5 %',
                                      sb('S', 'min') + ' = 362 kg/h'], ACS, AC, 14))
    o.append(T(370, 414, 'Each stage: follow the tie line E → R,', 13, 'start', MUT))
    o.append(T(370, 432, 'then the line from Δ through R to the next E.', 13, 'start', MUT))
    return 456, ''.join(o)
FIG[3] = (f3, 'The worked example on a right-angled diagram (solute axis stretched). All lines from Δ, which lies far to the left at (−1.87, 0.252), pass through F and E₁, R₁ and E₂, R₂ and E₃, R₃ and S; three tie lines take the raffinate from F to R₃.',
          'Right-angled triangular diagram with the solvent fraction across and the solute fraction up, the raffinate branch on the vertical axis and the extract branch on the hypotenuse, three tie lines from R1, R2, R3 to E1, E2, E3, and dashed lines converging on the difference point to the left.')


# ---- 5.4 mixer-settler and packed column ----
def f4():
    o = []
    # mixer
    o.append(T(20, 26, 'Mixer-settler stage', 15, 'start', bold=True))
    mx, my, mw, mh = 40, 70, 120, 140
    o.append(tank(mx, my, mw, mh, ACS))
    o.append(L(mx + mw / 2, my - 30, mx + mw / 2, my + mh - 40, INK, 2.5))
    o.append(R(mx + mw / 2 - 30, my + mh - 46, 60, 10, INK, INK, 2, 1))
    o.append(T(mx + mw / 2, my + 24, 'mixer', 14, bold=True))
    o.append(T(mx + mw / 2, my + 44, '0.5 m³', 13))
    o.append(T(mx + mw / 2, my + mh + 22, 't = 0.5/12 = 2.5 min', 13))
    o.append(L(4, my + 40, mx - 2, my + 40, AC, 2.5, arrow='n')); o.append(T(6, my + 32, 'feed', 13, 'start'))
    o.append(L(4, my + 90, mx - 2, my + 90, LV, 2.5, arrow='l')); o.append(T(6, my + 82, 'solvent', 13, 'start', LV))
    # settler
    sx, sy, sw, sh = 210, 90, 230, 110
    o.append(L(mx + mw, my + 100, sx - 2, sy + 55, INK, 2.5, arrow='n'))
    o.append(T(186, my + 70, '12 m³/h', 13))
    o.append(tank(sx, sy, sw, sh, PANEL))
    o.append(R(sx + 2, sy + 2, sw - 4, 44, LVS, LVS, 4, 0))
    o.append(R(sx + 2, sy + 62, sw - 4, sh - 64, ACS, ACS, 4, 0))
    for k in range(7):
        o.append(C(sx + 30 + k * 26, sy + 54 + (k % 2) * 6, 3.5, NX))
    o.append(T(sx + sw / 2, sy + 28, 'light layer', 13))
    o.append(T(sx + sw / 2, sy + sh - 16, 'heavy layer', 13))
    o.append(L(sx + sw, sy + 20, sx + sw + 40, sy + 20, LV, 2.5, arrow='l'))
    o.append(L(sx + sw, sy + sh - 18, sx + sw + 40, sy + sh - 18, AC, 2.5, arrow='n'))
    o.append(T(sx + sw / 2, sy + sh + 22, 'drops settle at 6.62 m/h', 13))
    o.append(T(sx + sw / 2, sy + sh + 40, 'A = 8/6.62 = 1.21 m²', 13, bold=True))
    # packed column
    cx, cy, cw, ch = 560, 50, 70, 300
    o.append(T(cx + cw / 2, 26, 'Packed column', 15, bold=True))
    o.append(R(cx, cy, cw, ch, PANEL, AC, 4, 2))
    for i in range(14):
        for j in range(3):
            yy = cy + 40 + i * 16
            if yy < cy + ch - 40:
                o.append(f'<circle cx="{cx + 14 + j * 21 + (i % 2) * 8:.1f}" cy="{yy:.1f}" r="5" style="fill:none;stroke:var(--line2);stroke-width:1.5"/>')
    o.append(L(cx + cw + 40, cy + 16, cx + cw + 2, cy + 16, AC, 2.5, arrow='n'))
    o.append(T(cx + cw + 44, cy + 20, 'feed', 13, 'start'))
    o.append(L(cx - 2, cy + ch - 16, cx - 40, cy + ch - 16, AC, 2.5, arrow='n'))
    o.append(T(cx - 44, cy + ch - 12, 'raffinate', 13, 'end'))
    o.append(L(cx + cw + 40, cy + ch - 16, cx + cw + 2, cy + ch - 16, LV, 2.5, arrow='l'))
    o.append(T(cx + cw + 44, cy + ch - 12, 'solvent', 13, 'start', LV))
    o.append(L(cx - 2, cy + 16, cx - 40, cy + 16, LV, 2.5, arrow='l'))
    o.append(T(cx - 44, cy + 20, 'extract', 13, 'end', LV))
    o.append(L(cx - 14, cy + 40, cx - 14, cy + ch - 40, MUT, 1.5)); o.append(L(cx - 20, cy + 40, cx - 8, cy + 40, MUT, 1.5)); o.append(L(cx - 20, cy + ch - 40, cx - 8, cy + ch - 40, MUT, 1.5))
    o.append(Tb(cx - 20, cy + ch / 2, 'Z = 3.74 m', 13, 'end', bold=True))
    o.append(T(cx + cw / 2, cy + ch + 24, 'D = 1.46 m', 13, bold=True))
    o.append(boxt(20, 300, 440, 76, ['column: N = 4.16 transfer units × 0.9 m', 'area (20 + 15)/21 = 1.667 m² at 60 % of flooding'], ACS, AC, 14))
    return 396, ''.join(o)
FIG[4] = (f4, 'Left, the worked mixer-settler: 12 m³/h stays 2.5 min in the 0.5 m³ mixer, and the settler needs 1.21 m² so the drops, settling at 6.62 m/h, reach their layer. Right, the packed column of the second example: 4.16 transfer units of 0.9 m give 3.74 m of packing, 1.46 m across.',
          'A stirred mixer feeding a horizontal settler with a light layer, a drop band and a heavy layer, and a packed column with feed in at the top, solvent in at the bottom, extract and raffinate out, marked with its height and diameter.')


# ---- 5.5 leaching stages ----
def f5():
    o = []
    def stage(x, y, title, lines):
        o.append(R(x, y, 150, 86, PANEL, AC, 8, 2))
        o.append(T(x + 75, y + 26, title, 14, bold=True))
        for i, s in enumerate(lines):
            o.append(T(x + 75, y + 48 + i * 18, s, 13))
    y0 = 90
    o.append(boxt(14, y0 + 10, 130, 66, ['seeds', '800 kg inert', '200 kg oil'], PANEL, L2, 13))
    o.append(L(146, y0 + 43, 196, y0 + 43, AC, 2.5, arrow='n'))
    stage(200, y0, 'Stage 1', ['M = 700 kg', 'y = 0.286'])
    o.append(L(275, y0 - 40, 275, y0 - 2, LV, 2.5, arrow='l')); o.append(T(275, y0 - 48, '500 kg solvent', 13, fill=LV))
    o.append(L(275, y0 + 88, 275, y0 + 130, NX, 2.5, arrow='x'))
    o.append(T(275, y0 + 148, 'overflow 300 kg', 13, fill=NX)); o.append(T(275, y0 + 166, '85.7 kg oil', 13, fill=NX, bold=True))
    o.append(L(352, y0 + 43, 456, y0 + 43, AC, 2.5, arrow='n'))
    o.append(Tb(404, y0 + 30, 'underflow', 13)); o.append(T(404, y0 + 64, '800 + 400 kg', 13)); o.append(T(404, y0 + 80, '114.3 kg oil', 13))
    stage(460, y0, 'Stage 2', ['M = 900 kg', 'y = 0.127'])
    o.append(L(535, y0 - 40, 535, y0 - 2, LV, 2.5, arrow='l')); o.append(T(535, y0 - 48, '500 kg solvent', 13, fill=LV))
    o.append(L(535, y0 + 88, 535, y0 + 130, NX, 2.5, arrow='x'))
    o.append(T(535, y0 + 148, 'overflow 500 kg', 13, fill=NX)); o.append(T(535, y0 + 166, '63.5 kg oil', 13, fill=NX, bold=True))
    o.append(L(612, y0 + 43, 700, y0 + 43, AC, 2.5, arrow='n'))
    o.append(T(700, y0 + 30, 'spent meal', 13, 'end')); o.append(T(700, y0 + 64, '50.8 kg oil', 13, 'end'))
    # oil split bars
    by = 300
    o.append(T(20, by - 14, 'Where the 200 kg of oil goes', 14, 'start', bold=True))
    def bar(y, lab, parts):
        o.append(T(150, y + 17, lab, 13, 'end', MUT))
        x = 160
        for v, c, t in parts:
            w = v * 2.6
            o.append(R(x, y, w, 24, c, c, 2, 1))
            if t: o.append(T(x + w / 2, y + 17, t, 13, fill='var(--fig)' if c in (AC, NX) else INK, bold=True))
            x += w
    bar(by, 'one stage', [(85.7, NX, '85.7 out'), (114.3, LN, '114.3 in meal')])
    bar(by + 36, 'two stages', [(85.7, NX, '85.7'), (63.5, AC, '63.5'), (50.8, LN, '50.8')])
    o.append(T(20, by + 90, 'Recovery 42.9 % in one stage, 74.6 % in two; the wet meal holds 400 kg of solution after every stage.', 13, 'start', MUT))
    return by + 104, ''.join(o)
FIG[5] = (f5, 'The worked examples: in each ideal stage all the oil is dissolved, the overflow and the retained solution leave at the same strength, and the meal always carries 400 kg of solution forward. One stage recovers 85.7 kg of the 200 kg of oil; a second stage with fresh solvent adds 63.5 kg.',
          'Two leaching stages in cross-current: seeds with 800 kilograms of inert and 200 kilograms of oil enter stage 1 with 500 kilograms of solvent; overflows of 85.7 and 63.5 kilograms of oil leave the two stages, and bars show the oil split for one and two stages.')


# ---- 5.6 supercritical CO2 extraction loop ----
def f6():
    o = []
    ex = (250, 70, 90, 200)
    o.append(R(*ex, ACS, AC, 10, 2.5))
    for i in range(9):
        for j in range(3):
            o.append(C(ex[0] + 20 + j * 25 + (i % 2) * 10, ex[1] + 30 + i * 18, 4, 'var(--line2)'))
    o.append(T(ex[0] + ex[2] / 2, ex[1] - 26, 'extractor', 14, bold=True))
    o.append(T(ex[0] + ex[2] / 2, ex[1] - 10, '40 °C, 200 bar', 13))
    o.append(T(ex[0] + ex[2] / 2, ex[1] + ex[3] + 20, '2.0 kg spice, 0.10 kg oil', 13))
    sp = (480, 110, 90, 130)
    o.append(R(*sp, PANEL, NX, 10, 2.5))
    o.append(T(sp[0] + sp[2] / 2 + 62, sp[1] - 8, 'separator', 14, 'start', bold=True))
    o.append(T(sp[0] + sp[2] / 2, sp[1] + 34, 'low', 13)); o.append(T(sp[0] + sp[2] / 2, sp[1] + 50, 'pressure', 13))
    o.append(R(sp[0] + 6, sp[1] + sp[3] - 34, sp[2] - 12, 28, NXS, NXS, 4, 0))
    o.append(T(sp[0] + sp[2] / 2, sp[1] + sp[3] - 14, 'oil', 13, fill=NX, bold=True))
    # valve
    vx, vy = 410, 90
    o.append(f'<polygon points="{vx - 12},{vy - 10} {vx + 12},{vy + 10} {vx + 12},{vy - 10} {vx - 12},{vy + 10}" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    o.append(T(vx, vy + 28, 'valve', 13))
    o.append(L(ex[0] + ex[2], ex[1] + 20, vx - 14, vy, LV, 2.5))
    o.append(L(vx + 14, vy, sp[0] + sp[2] / 2, vy, LV, 2.5))
    o.append(L(sp[0] + sp[2] / 2, vy, sp[0] + sp[2] / 2, sp[1] - 2, LV, 2.5, arrow='l'))
    o.append(T(410, 66, 'CO₂ + 1.5 % oil', 13, fill=LV))
    o.append(L(sp[0] + sp[2] / 2, sp[1] + sp[3] + 2, sp[0] + sp[2] / 2, sp[1] + sp[3] + 34, NX, 2.5, arrow='x'))
    o.append(T(sp[0] + sp[2] / 2 + 8, sp[1] + sp[3] + 26, 'extract out', 13, 'start', NX))
    # recycle loop
    o.append(P([(sp[0] + sp[2], sp[1] + 20), (660, sp[1] + 20), (660, 330), (120, 330), (120, ex[1] + ex[3] - 20), (ex[0] - 2, ex[1] + ex[3] - 20)], AC, 2.5))
    o.append(L(ex[0] - 40, ex[1] + ex[3] - 20, ex[0] - 2, ex[1] + ex[3] - 20, AC, 2.5, arrow='n'))
    o.append(C(390, 330, 18, PANEL)); o.append(f'<circle cx="390" cy="330" r="18" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    o.append(T(390, 335, 'P', 14, bold=True)); o.append(T(390, 362, 'compressor', 13))
    o.append(R(160, 316, 70, 28, PANEL, INK, 4, 2)); o.append(T(195, 335, 'heater', 13))
    o.append(T(660 - 6, 280, 'lean CO₂', 13, 'end', AC))
    o.append(T(128, 300, 'CO₂ 5 kg/h', 13, 'start', AC))
    o.append(boxt(20, 60, 200, 120, ['oil needs 0.100/0.015', '= 6.67 kg of solution', 'CO₂ ≥ 6.57 kg', 'time ≥ 6.57/5 = 1.31 h'], PANEL, L2, 13))
    return 378, ''.join(o)
FIG[6] = (f6, 'The supercritical CO₂ loop of the second worked example. Dense CO₂ at 40 °C and 200 bar dissolves the oil in the extractor; dropping the pressure in the separator makes the oil fall out, and the lean CO₂ is recompressed. At 1.5 % oil in the leaving fluid, 0.10 kg of oil needs at least 6.57 kg of CO₂.',
          'Flow loop: compressor and heater feed CO2 into a packed extractor at 40 degrees and 200 bar; the loaded fluid passes a valve into a low-pressure separator where oil collects at the bottom; lean CO2 returns to the compressor.')


# ---- 5.7 three-tank counter-current battery (Shanks arrangement) ----
def f7():
    o = []
    xs = [100, 290, 480]
    y0, w, h = 110, 125, 120
    names = ['freshest solid', 'middle', 'oldest solid']
    ys = ['0.491', '0.279', '0.119']
    o.append(T(20, 26, 'Liquor path in one cycle (solid stays in its tank)', 15, 'start', bold=True))
    for i, x in enumerate(xs):
        o.append(R(x, y0, w, h, PANEL, AC, 6, 2))
        o.append(R(x + 4, y0 + 40, w - 8, h - 44, ACS, ACS, 4, 0))
        o.append(T(x + w / 2, y0 + 22, names[i], 13, bold=True))
        o.append(T(x + w / 2, y0 + 70, 'solution', 13))
        o.append(T(x + w / 2, y0 + 90, 'y = ' + ys[i], 14, bold=True))
    # liquor: fresh water into tank 3, 3 -> 2 -> 1 -> strong liquor out
    o.append(L(xs[2] + w / 2, y0 - 46, xs[2] + w / 2, y0 - 2, LV, 2.5, arrow='l'))
    o.append(T(xs[2] + w / 2, y0 - 54, 'fresh water 600 kg/h', 13, fill=LV, bold=True))
    for a, b in ((2, 1), (1, 0)):
        o.append(arc(xs[a] + 10, y0 + h + 4, xs[b] + w - 10, y0 + h + 4, -0.25, LV, 2.5, arrow='l'))
    o.append(Tb((xs[2] + xs[1] + w) / 2, y0 + h + 44, '600 kg/h', 13, fill=LV))
    o.append(Tb((xs[1] + xs[0] + w) / 2, y0 + h + 44, '600 kg/h', 13, fill=LV))
    o.append(L(xs[0] + w / 2, y0 - 2, xs[0] + w / 2, y0 - 46, NX, 2.5, arrow='x'))
    o.append(T(xs[0] + w / 2, y0 - 54, 'strong liquor 400 kg/h, y = 0.491', 13, fill=NX, bold=True))
    o.append(T(xs[0] - 6, y0 + h / 2, '250 kg/h', 13, 'end', AC)); o.append(T(xs[0] - 6, y0 + h / 2 + 16, 'solute in', 13, 'end', AC))
    o.append(T(xs[2] + w + 6, y0 + h / 2, 'leaves with', 13, 'start', AC)); o.append(T(xs[2] + w + 6, y0 + h / 2 + 16, '450 kg/h', 13, 'start', AC))
    o.append(T(xs[2] + w + 6, y0 + h / 2 + 32, 'solution', 13, 'start', AC))
    o.append(boxt(20, 316, 330, 92, ['lost: 450 × 0.119 = 53.7 kg/h', 'recovered: 400 × 0.491 = 196.3 kg/h', 'recovery 78.5 % (8 stages for 95 %)'], ACS, AC, 14))
    o.append(boxt(370, 316, 330, 92, ['next cycle: empty the oldest tank,', 'refill it with fresh solid and switch', 'the valves so it is last in line'], PANEL, L2, 13))
    return 424, ''.join(o)
FIG[7] = (f7, 'The worked example as a three-tank battery. Fresh water enters the tank with the oldest solid and the liquor passes to fresher and fresher solid, leaving strong (y = 0.491, 400 kg/h) from the tank just filled. At the end of a cycle the oldest tank is emptied and refilled, and the valves move the inlet and outlet one tank on.',
          'Three tanks in a row labelled freshest solid, middle and oldest solid with solution strengths 0.491, 0.279 and 0.119; fresh water enters the oldest-solid tank, liquor arrows run back to the freshest tank, and strong liquor leaves from it.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}


def drop_sources():
    """university-hosted or university-run pages the book must not list"""
    return ['ocw.mit.edu', 'nptel.ac.in', 'openstax.org']
