"""Claude's hand-drawn figures for ec-optical-u1 (Optical Fiber Communication: light propagation in fibers), one per
chapter, drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
D = math.degrees; Rd = math.radians


def sub(base, s, size=13):
    return f'{base}<tspan dy="4" font-size="{size - 2}">{s}</tspan><tspan dy="-4"> </tspan>'


# ---- 1.1 the link and its power levels ----
def f1():
    o = []
    bx = [(14, 'Input', 'electrical data'), (150, 'Source', 'LED or laser'), (300, 'Fiber, 20 km', '0.2 dB/km'),
          (466, 'Detector', 'PIN or APD'), (602, 'Output', 'amplified')]
    ws = [116, 126, 142, 116, 104]
    for (x, a, b), w in zip(bx, ws):
        st = LV if a.startswith('Fiber') else (AC if a in ('Source', 'Detector') else MUT)
        fl = LVS if a.startswith('Fiber') else (ACS if a in ('Source', 'Detector') else PANEL)
        o.append(boxt(x, 30, w, 62, [a, b], fl, st, 14, bold_first=True, fills=[INK, MUT]))
    for (x, _, _), w, (nx, _, _) in zip(bx[:-1], ws[:-1], bx[1:]):
        o.append(L(x + w + 2, 61, nx - 4, 61, MUT, 2, arrow='m'))
    o.append(T(213, 116, 'E/O', 13, fill=MUT)); o.append(T(524, 116, 'O/E', 13, fill=MUT))
    # power against distance
    x0, x1, y0, y1 = 110, 650, 160, 330
    fx = lambda z: x0 + z / 20 * (x1 - x0)
    fy = lambda p: y0 + (0 - p) / 5 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 5, 10, 15, 20], [0, -1, -2, -3, -4, -5], fx, fy, 'distance along the fiber (km)', 'power (dBm)', yfmt=neg))
    o.append(P([(fx(0), fy(0)), (fx(20), fy(-4))], LV, 3))
    o.append(C(fx(0), fy(0), 6, AC)); o.append(C(fx(20), fy(-4), 6, NX))
    o.append(Tb(fx(0.6), fy(-1.7), 'launch 1 mW = 0 dBm', 14, 'start', AC, bold=True))
    o.append(Tb(fx(19.4), fy(-4.55), 'received −4 dBm = 0.398 mW', 14, 'end', NX, bold=True))
    o.append(Tb(fx(11.5), fy(-3.1), 'loss 0.2 × 20 = 4 dB', 14, 'middle', LV))
    return 380, ''.join(o)

FIG[1] = (f1, 'The link of the worked example: the source turns the electrical input into 1 mW of light (0 dBm), the 20 km fiber '
              'loses 0.2 dB in every kilometre, and the detector receives −4 dBm, which is 0.398 mW.',
          'Five blocks in a row: input, source, 20 km fiber, detector, output. Below, a straight line of power falling from 0 dBm at 0 km to −4 dBm at 20 km.')


# ---- 1.2 a ray at the acceptance limit ----
def f2():
    o = []
    yt, yb = 120, 250          # core walls
    xf = 150                   # end face
    o.append(R(xf, 70, 560, 50, PANEL, L2, 0, 1.5)); o.append(R(xf, yb, 560, 50, PANEL, L2, 0, 1.5))
    o.append(R(xf, yt, 560, yb - yt, ACS, AC, 0, 1.5))
    o.append(L(xf, 70, xf, 300, INK, 2))
    o.append(T(xf + 14, 100, 'cladding n₂ = 1.45', 14, 'start', MUT)); o.append(T(690, 280, 'cladding n₂ = 1.45', 14, 'end', MUT))
    o.append(T(690, 238, 'core n₁ = 1.50', 14, 'end', AC, bold=True))
    o.append(T(20, 60, 'air, n₀ = 1', 14, 'start', MUT))
    yax = (yt + yb) / 2
    o.append(L(40, yax, 700, yax, L2, 1.2, '6 5')); o.append(T(46, yax + 18, 'axis', 13, 'start', MUT))
    # incoming ray at 22.59 deg hitting end face at axis
    ta, tr = 22.585, 14.835
    sx = xf - 110; sy = yax + 110 * math.tan(Rd(ta))
    o.append(L(sx, sy, xf, yax, NX, 2.8))
    # inside the core: rises at tr until the top wall
    hx = xf + (yax - yt) / math.tan(Rd(tr))
    o.append(L(xf, yax, hx, yt, NX, 2.8))
    o.append(L(hx, yt, hx + (yb - yt) / math.tan(Rd(tr)) * 0.62, yt + (yb - yt) * 0.62, NX, 2.8, arrow='x'))
    # angle arcs
    o.append(f'<path d="M{xf - 60:.1f},{yax:.1f} A60,60 0 0,0 {xf - 60 * math.cos(Rd(ta)):.1f},{yax + 60 * math.sin(Rd(ta)):.1f}" style="fill:none;stroke:var(--next);stroke-width:1.8"/>')
    o.append(Tb(xf - 12, yax - 12, 'θₐ = 22.6°', 14, 'end', NX, bold=True))
    o.append(f'<path d="M{xf + 70:.1f},{yax:.1f} A70,70 0 0,0 {xf + 70 * math.cos(Rd(tr)):.1f},{yax - 70 * math.sin(Rd(tr)):.1f}" style="fill:none;stroke:var(--next);stroke-width:1.8"/>')
    o.append(Tb(xf + 82, yax - 6, 'θr = 14.8°', 14, 'start', NX))
    # normal at hit point
    o.append(L(hx, yt - 40, hx, yt + 95, INK, 1.5, '4 4'))
    o.append(T(hx - 6, yt - 26, 'normal', 13, 'end', MUT))
    o.append(f'<path d="M{hx:.1f},{yt + 55:.1f} A55,55 0 0,0 {hx + 55 * math.sin(Rd(90 - tr)):.1f},{yt + 55 * math.cos(Rd(90 - tr)):.1f}" style="fill:none;stroke:var(--live);stroke-width:1.8"/>')
    o.append(Tb(hx + 12, yt + 72, 'φ = 75.2° = θc', 14, 'start', LV, bold=True))
    o.append(T(hx + 30, yt - 8, 'TIR: reflected back into the core', 13, 'start', INK))
    o.append(T(360, 336, 'launch at θₐ → 14.8° inside → meets the wall at exactly θc; any steeper launch leaks out', 14))
    return 352, ''.join(o)

FIG[2] = (f2, 'The worked example’s limiting ray: launched from air at θₐ = 22.6°, it bends to 14.8° inside the core and meets '
              'the wall at 90° − 14.8° = 75.2°, exactly the critical angle, so it is just reflected. A steeper launch would meet the wall below θ<sub>c</sub> and leak.',
          'Side view of a step-index fiber with core index 1.50 and cladding 1.45. A ray from air enters at 22.6 degrees to the axis, travels at 14.8 degrees inside and strikes the top wall at 75.2 degrees from the normal, then reflects.')


# ---- 1.3 meridional and skew rays seen end-on ----
def f3():
    o = []
    for cx, title, col in ((180, 'Meridional ray: γ = 0', AC), (540, 'Skew ray: γ = 45°', NX)):
        R0 = 120; cy = 190
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{R0 + 26}" style="fill:{PANEL};stroke:{L2};stroke-width:1.5"/>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{R0}" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
        o.append(C(cx, cy, 4, INK))
        o.append(T(cx, 36, title, 15, bold=True, fill=col))
    # meridional: along a diameter, bouncing back and forth
    cx, cy, R0 = 180, 190, 120
    a1 = Rd(30)
    p1 = (cx + R0 * math.cos(a1), cy - R0 * math.sin(a1)); p2 = (cx - R0 * math.cos(a1), cy + R0 * math.sin(a1))
    o.append(L(p1[0], p1[1], p2[0], p2[1], AC, 3))
    o.append(T(cx, cy + 22, 'axis', 13, fill=MUT))
    o.append(T(cx, 356, 'passes through the axis', 14, fill=MUT))
    o.append(T(cx, 376, 'θₐ = 14.0°', 14, bold=True, fill=AC))
    # skew: square path (each chord meets the radius at 45 deg)
    cx = 540
    pts = [(cx + R0 * math.cos(Rd(a)), cy - R0 * math.sin(Rd(a))) for a in (90, 0, 270, 180, 90)]
    for (xa, ya), (xb, yb) in zip(pts[:-1], pts[1:]):
        o.append(L(xa, ya, xb, yb, NX, 3, arrow='x' if (xa, ya) == pts[2] else None))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R0 / math.sqrt(2):.1f}" style="fill:none;stroke:{L2};stroke-width:1.5;stroke-dasharray:5 5"/>')
    # gamma at the top point: radius and chord
    tx, ty = pts[0]
    o.append(L(cx, cy, tx, ty, INK, 1.5, '4 4'))
    o.append(f'<path d="M{tx:.1f},{ty + 34:.1f} A34,34 0 0,1 {tx + 34 * math.sin(Rd(45)):.1f},{ty + 34 * math.cos(Rd(45)):.1f}" style="fill:none;stroke:var(--live);stroke-width:2"/>')
    o.append(Tb(tx + 22, ty + 60, 'γ', 15, 'start', LV, bold=True))
    o.append(T(tx - 10, ty + 82, 'radius', 13, 'end', MUT))
    o.append(T(cx, 356, 'never crosses the axis', 14, fill=MUT))
    o.append(T(cx, 376, sub('θ', 'as', 14) + '= sin⁻¹(0.2425/cos 45°) = 20.1°', 14, bold=True, fill=NX))
    return 392, ''.join(o)

FIG[3] = (f3, 'The fiber seen end-on (n₁ = 1.48, n₂ = 1.46, NA = 0.2425). A meridional ray runs along a diameter and is accepted up to 14.0°. '
              'A skew ray with γ = 45° traces a square round the axis, meeting every reflection at the same angle, and is accepted up to 20.1°.',
          'Two circles showing a fiber end-on. Left: a ray along a diameter through the axis, acceptance 14.0 degrees. Right: a ray tracing a square that never crosses the axis, with the angle gamma of 45 degrees between the chord and the radius marked; acceptance 20.1 degrees.')


# ---- 1.4 TE0 and TE1 field profiles of the slab ----
def f4():
    o = []
    k0 = 2 * math.pi / 1.3; n1, n2, d = 1.50, 1.48, 5.0
    modes = [(1.4968988911, 0, LV, 'TE₀', 'n_eff 1.4969', '1/γ = 0.92 µm'), (1.4882333273, 1, NX, 'TE₁', 'n_eff 1.4882', '1/γ = 1.32 µm')]
    xs = [-8 + i * 0.05 for i in range(321)]
    yc = 240; sy = lambda x: yc - x * 20      # 1 µm = 20 px (x across the slab drawn vertically)
    # layers
    o.append(R(40, sy(8), 640, 20 * 5.5, PANEL, L2, 0, 1)); o.append(R(40, sy(-2.5), 640, 20 * 5.5, PANEL, L2, 0, 1))
    o.append(R(40, sy(2.5), 640, 100, ACS, AC, 0, 1.5))
    o.append(T(52, sy(2.5) + 20, 'core n₁ = 1.50, d = 5 µm', 14, 'start', AC, bold=True))
    o.append(T(52, sy(8) + 20, 'cladding n₂ = 1.48', 14, 'start', MUT)); o.append(T(52, sy(-8) - 10, 'cladding n₂ = 1.48', 14, 'start', MUT))
    for i, (ne, m, col, name, l1, l2) in enumerate(modes):
        kap = k0 * math.sqrt(n1 ** 2 - ne ** 2); g = k0 * math.sqrt(ne ** 2 - n2 ** 2)
        def E(x):
            if abs(x) <= d / 2: return math.cos(kap * x) if m == 0 else math.sin(kap * x)
            edge = math.cos(kap * d / 2) if m == 0 else math.sin(kap * d / 2) * (1 if x > 0 else -1)
            return edge * math.exp(-g * (abs(x) - d / 2))
        xb = 380 + i * 170; amp = 70
        o.append(L(xb, sy(8), xb, sy(-8), L2, 1.5, '4 4'))
        o.append(P([(xb + amp * E(x), sy(x)) for x in xs], col, 3))
        o.append(T(xb, 34, name + ': n<tspan dy="4" font-size="11">eff</tspan><tspan dy="-4"> = ' + l1.split()[-1] + '</tspan>', 14, bold=True, fill=col))
        o.append(T(xb, 426, l2, 13, fill=col))
    o.append(T(52, 426, 'field E across the slab (x drawn upwards)', 13, 'start', MUT))
    return 440, ''.join(o)

FIG[4] = (f4, 'The two TE modes of the worked example’s slab (d = 5 µm, n₁ = 1.50, n₂ = 1.48, λ = 1.3 µm, V = 5.90), drawn from the solved '
              'eigenvalue equation. TE₀ has no zero and decays within 0.92 µm of the wall; TE₁ has one zero and, being nearer cutoff, reaches 1.32 µm into the cladding.',
          'A slab with a 5 micrometre core between claddings, drawn with x vertical. Two field curves: TE0, a single hump with short tails; TE1, one positive and one negative lobe with longer tails into the cladding.')


# ---- 1.5 index profiles ----
def f5():
    o = []
    n1, n2, a = 1.48, 1.46, 25.0
    De = (n1 ** 2 - n2 ** 2) / (2 * n1 ** 2)
    x0, x1, y0, y1 = 100, 680, 60, 320
    fx = lambda r: x0 + (r + 40) / 80 * (x1 - x0)
    fy = lambda n: y1 - (n - 1.455) / 0.03 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [-40, -25, -10, 0, 10, 25, 40], [1.46, 1.47, 1.48], fx, fy, 'r (µm), core radius a = 25 µm', 'n(r)',
                  xfmt=neg, yfmt=lambda v: f'{v:.2f}'))
    o.append(P([(fx(-40), fy(n2)), (fx(-25), fy(n2)), (fx(-25), fy(n1)), (fx(25), fy(n1)), (fx(25), fy(n2)), (fx(40), fy(n2))], AC, 3))
    gr = [(fx(r), fy(n1 * math.sqrt(1 - 2 * De * (abs(r) / a) ** 2) if abs(r) < a else n2)) for r in [i * 0.5 - 40 for i in range(161)]]
    o.append(P(gr, LV, 3))
    n10 = n1 * math.sqrt(1 - 2 * De * 0.16)
    o.append(C(fx(10), fy(n10), 6, NX))
    o.append(Tb(fx(10) + 12, fy(n10) + 26, f'n(10 µm) = {n10:.4f}', 14, 'start', NX, bold=True))
    o.append(Tb(fx(-24), fy(n1) - 12, 'step: V = 29.3, M ≈ V²/2 = 429', 14, 'start', AC, bold=True))
    o.append(Tb(fx(0), fy(1.4655), 'parabolic: M ≈ V²/4 = 215', 14, 'middle', LV, bold=True))
    return 372, ''.join(o)

FIG[5] = (f5, 'Index against radius for the worked example’s two fibers, n₁ = 1.48 and n₂ = 1.46 with a 25 µm core radius. The step profile '
              'drops at r = ±25 µm; the parabolic profile falls smoothly to meet n₂ there, passing 1.4768 at 10 µm, and carries half as many modes.',
          'Plot of refractive index against radius from −40 to 40 micrometres. A rectangular step at 1.48 inside ±25 micrometres and 1.46 outside, and a parabola from 1.48 at the axis down to 1.46 at ±25 micrometres; the point 1.4768 at 10 micrometres is marked.')


# ---- 1.6 V against wavelength ----
def f6():
    o = []
    K = 2 * math.pi * 4.0 * 0.11
    x0, x1, y0, y1 = 90, 680, 50, 320
    fx = lambda l: x0 + (l - 0.7) / 1.0 * (x1 - x0)
    fy = lambda v: y1 - v / 4.4 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0.7, 0.85, 1.0, 1.15, 1.31, 1.55, 1.7], [0, 1, 2, 3, 4], fx, fy, 'wavelength λ (µm)', 'V',
                  xfmt=lambda v: f'{v:g}'))
    o.append(f'<rect x="{fx(K / 2.405):.1f}" y="{fy(2.405):.1f}" width="{x1 - fx(K / 2.405):.1f}" height="{y1 - fy(2.405):.1f}" style="fill:var(--live-soft)"/>')
    o.append(L(x0, fy(2.405), x1, fy(2.405), LV, 2, '7 5')); o.append(Tb(x1 - 4, fy(2.405) - 8, 'V = 2.405 (LP₁₁ cutoff)', 13, 'end', LV, bold=True))
    o.append(L(x0, fy(3.832), x1, fy(3.832), L2, 1.5, '4 4')); o.append(Tb(x1 - 4, fy(3.832) - 8, 'V = 3.832 (LP₂₁, LP₀₂)', 13, 'end', MUT))
    o.append(P([(fx(l / 100), fy(K / (l / 100))) for l in range(70, 171)], AC, 3))
    for l, lab, anc, dy in ((0.85, 'V = 3.25 at 0.85 µm', 'start', -6), (K / 2.405, sub('λ', 'c', 14) + '= 1.15 µm', 'start', -10), (1.31, 'V = 2.11', 'start', 22), (1.55, 'V = 1.78', 'start', 22)):
        v = K / l
        o.append(C(fx(l), fy(v), 6, NX if l > 1.2 else AC))
        o.append(Tb(fx(l) + 10, fy(v) + dy, lab, 14, anc, NX if l > 1.2 else AC, bold=True))
    o.append(T(fx(1.42), fy(0.9), 'single-mode (λ &gt; ' + sub('λ', 'c', 14) + ')', 14, fill=LV, bold=True))
    o.append(T(fx(0.85), fy(0.9), 'multimode (λ &lt; ' + sub('λ', 'c', 14) + ')', 14, fill=MUT, bold=True))
    return 370, ''.join(o)

FIG[6] = (f6, 'V = 2.765/λ for the worked example’s fiber (a = 4 µm, NA = 0.11). The curve crosses 2.405 at the cutoff wavelength 1.15 µm; '
              'at 1.31 and 1.55 µm it lies below the line (single-mode), while at 0.85 µm, V = 3.25 and LP₁₁ is also guided.',
          'Plot of V against wavelength from 0.7 to 1.7 micrometres, a falling curve. A dashed line at V = 2.405 meets it at 1.15 micrometres; points at 0.85 (V 3.25), 1.31 (2.11) and 1.55 micrometres (1.78) are marked, with the region right of 1.15 shaded as single-mode.')


# ---- 1.7 phase and group delay ----
def f7():
    o = []
    # a wave packet at two times
    for row, (yc, xc, lab) in enumerate(((95, 230, 'at time t'), (215, 470, 'a little later'))):
        o.append(L(40, yc, 690, yc, L2, 1.2))
        pts = []
        for i in range(0, 401):
            x = 40 + i * 650 / 400
            env = math.exp(-((x - xc) / 70) ** 2)
            ph = (x - 40) / 18 - row * 2.2
            pts.append((x, yc - 45 * env * math.cos(ph)))
        o.append(P(pts, AC, 2.2))
        o.append(P([(40 + i * 650 / 200, yc - 45 * math.exp(-((40 + i * 650 / 200 - xc) / 70) ** 2)) for i in range(201)], LV, 2, '6 4'))
        o.append(T(44, yc - 52, lab, 13, 'start', MUT))
        o.append(L(xc, yc - 58, xc, yc + 50, LV, 1.5, '3 3'))
    o.append(L(234, 290, 466, 290, LV, 2.5, arrow='l'))
    o.append(T(350, 310, 'envelope moves at ' + sub('v', 'g', 14) + '= c/' + sub('N', 'g', 14), 14, fill=LV, bold=True))
    # delays over 10 km
    x0, x1 = 130, 650
    fx = lambda t: x0 + (t - 48.4) / 1.1 * (x1 - x0)
    yb = 370
    o.append(L(x0, yb, x1, yb, L2, 1.5))
    for t in (48.5, 49.0, 49.5):
        o.append(L(fx(t), yb, fx(t), yb + 5, L2, 1.5))
        o.append(T(fx(t), yb + 20, f'{t:.1f}' + (' µs' if t == 49.5 else ''), 13, fill=MUT))
    o.append(C(fx(48.67), yb, 6, AC)); o.append(Tb(fx(48.67), yb - 14, 'crests: 48.67 µs (' + sub('n', 'eff') + '1.46)', 13, 'middle', AC, bold=True))
    o.append(C(fx(49.33), yb, 6, LV)); o.append(Tb(fx(49.33), yb - 14, 'pulse: 49.33 µs (' + sub('N', 'g') + '1.48)', 13, 'middle', LV, bold=True))
    o.append(T(20, yb + 4, 'over 10 km', 13, 'start', MUT))
    o.append(T(fx(49.0), yb + 50, 'lag = 10 km × 0.02/c = 0.67 µs', 14, bold=True))
    return 432, ''.join(o)

FIG[7] = (f7, 'Top: a pulse is a carrier inside an envelope; the crests (solid) slide forward through the envelope (dashed), which moves at the group velocity. '
              'Bottom: over the worked example’s 10 km, crests would take 48.67 µs and the pulse takes 49.33 µs, 0.67 µs longer.',
          'Two snapshots of a wave packet, the second shifted to the right, with the envelope peak marked. Below, a time axis with crests arriving at 48.67 microseconds and the pulse at 49.33 microseconds.')


# ---- 1.8 buried channel guide and the effective index method ----
def f8():
    o = []
    # cross-section, 1 um = 70 px
    s = 70; cx, cy = 190, 200
    o.append(R(30, 70, 320, 260, PANEL, L2, 6, 1.5))
    o.append(R(cx - s, cy - 0.25 * s, 2 * s, 0.5 * s, ACS, AC, 2, 2))
    o.append(T(cx, cy + 6, 'core n₁ = 1.50', 14, bold=True, fill=AC))
    o.append(T(cx, 96, 'cladding n₂ = 1.45 all round', 14, fill=MUT))
    o.append(L(cx - s, cy + 0.25 * s + 22, cx + s, cy + 0.25 * s + 22, INK, 1.5)); o.append(T(cx, cy + 0.25 * s + 42, 'w = 2 µm', 14))
    o.append(L(cx + s + 18, cy - 0.25 * s, cx + s + 18, cy + 0.25 * s, INK, 1.5)); o.append(T(cx + s + 26, cy + 5, 't = 0.5 µm', 14, 'start'))
    o.append(T(190, 312, 'λ = 1.55 µm', 14, fill=MUT))
    # steps
    o.append(boxt(390, 70, 310, 110, ['1. vertical slab, thickness t', 'V = 2.027 × 0.3841 = 0.778 &lt; π', 'one mode: ' + sub('n', 'eff,1', 14) + '= 1.4564'], PANEL, AC, 14, True))
    o.append(L(545, 182, 545, 216, MUT, 2, arrow='m'))
    o.append(boxt(390, 220, 310, 110, ['2. lateral slab, width w', 'core ' + sub('n', 'eff,1', 14) + ', sides n₂ = 1.45', sub('V', 'w', 14) + '= 8.107 × 0.1364 = 1.11 &lt; π'], PANEL, LV, 14, True))
    o.append(T(545, 360, 'single-mode both ways; guide ' + sub('n', 'eff', 14) + '≈ 1.4514', 14, bold=True, fill=NX))
    return 380, ''.join(o)

FIG[8] = (f8, 'The worked examples’ buried channel guide, 2 µm wide and 0.5 µm thick, and the two slab checks of the effective index method: '
              'the thickness gives V = 0.778 and n_eff = 1.4564, and that index against the side cladding gives V = 1.11, so the guide is single-mode.'.replace('n_eff', 'n<sub>eff</sub>'),
          'Left: a rectangle of core index 1.50, 2 micrometres wide and 0.5 thick, in cladding of 1.45. Right: two boxes. Step 1, vertical slab, V 0.778, effective index 1.4564. Step 2, lateral slab, V 1.11. Single-mode in both directions.')


# ---- 1.9 reflectance of the quarter-wave stack ----
def f9():
    import numpy as np
    nH, nL, l0 = 2.0, 1.45, 1550.0
    dH, dL = l0 / (4 * nH), l0 / (4 * nL)
    def Rf(lam, N=8, n0=1.0, ns=1.45):
        M = np.eye(2, dtype=complex)
        for _ in range(N):
            for n, d in ((nH, dH), (nL, dL)):
                dl = 2 * math.pi * n * d / lam
                M = M @ np.array([[math.cos(dl), 1j * math.sin(dl) / n], [1j * n * math.sin(dl), math.cos(dl)]])
        B, Cc = M @ np.array([1, ns])
        r = (n0 * B - Cc) / (n0 * B + Cc)
        return abs(r) ** 2
    o = []
    x0, x1, y0, y1 = 90, 690, 78, 320
    fx = lambda l: x0 + (l - 1200) / 700 * (x1 - x0)
    fy = lambda r: y1 - r * (y1 - y0)
    o.append(f'<rect x="{fx(1407):.1f}" y="{y0}" width="{fx(1726) - fx(1407):.1f}" height="{y1 - y0}" style="fill:var(--accent-soft)"/>')
    o.append(axes(x0, x1, y0, y1, [1200, 1300, 1407, 1550, 1726, 1900], [0, 0.5, 1.0], fx, fy, 'wavelength (nm)', 'reflectance R',
                  yfmt=lambda v: f'{v:.1f}'))
    o.append(P([(fx(l), fy(Rf(l))) for l in range(1200, 1901, 4)], AC, 2.8))
    o.append(C(fx(1550), fy(Rf(1550)), 6, NX))
    o.append(Tb(fx(1550), fy(Rf(1550)) + 26, 'R = 98.4 % at 1550 nm (8 pairs)', 14, 'middle', NX, bold=True))
    o.append(Tb(fx(1566), fy(0.42), 'stop band 1407–1726 nm', 14, 'middle', AC, bold=True))
    o.append(T(x0, 26, 'Si₃N₄ (n 2.0, 193.8 nm) and SiO₂ (n 1.45, 267.2 nm); period a = 461.0 nm', 14, 'start', MUT))
    return 372, ''.join(o)

FIG[9] = (f9, 'Reflectance of the worked example’s mirror, 8 quarter-wave pairs of silicon nitride and silica on silica, computed by the transfer-matrix '
              'method. Inside the shaded stop band (1407 to 1726 nm) light cannot pass and R reaches 98.4 % at 1550 nm; outside it most light gets through.',
          'Plot of reflectance against wavelength from 1200 to 1900 nanometres. A flat-topped high band near 0.98 between about 1407 and 1726 nanometres, shaded, with low ripples on either side; the point 98.4 percent at 1550 nanometres is marked.')


spec = make_spec(FIG)
