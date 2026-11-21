"""Claude's hand-drawn figures for ec-antenna-u2 (Antenna fundamentals and radiation), one per chapter, drawn from each
chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
Rd = math.radians
RECT = R


def sub(base, s, size=14, gap=True):
    return f'{base}<tspan dy="4" font-size="{size - 3}">{s}</tspan><tspan dy="-4">{" " if gap else "&#8203;"}</tspan>'


def polar_lobe(cx, cy, R, fn, th0=0.0, th1=180.0, side=1, step=1.0):
    """points of a pattern r = fn(theta) drawn in a vertical plane; theta from the upward axis, side +1 right, -1 left"""
    pts = []
    t = th0
    while t <= th1 + 1e-9:
        r = fn(Rd(t)) * R
        pts.append((cx + side * r * math.sin(Rd(t)), cy - r * math.cos(Rd(t))))
        t += step
    return pts


def grid(cx, cy, R, rings=(0.5, 1.0), labels=True):
    o = []
    for g in rings:
        o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{g * R:.1f}" style="fill:none;stroke:var(--line);stroke-width:1.2;stroke-dasharray:4 4"/>')
    return ''.join(o)


# ---- 2.1 the Hertzian dipole's E-plane pattern, with the worked example's numbers ----
def f1():
    o = []
    cx, cy, R = 230, 205, 150
    o.append(grid(cx, cy, R))
    o.append(L(cx, cy - R - 26, cx, cy + R + 22, L2, 1.4, '6 5'))
    o.append(T(cx + 8, cy - R - 32, 'wire axis, θ = 0°: null', 14, 'start', MUT))
    o.append(L(cx - R - 20, cy, cx + R + 20, cy, L2, 1.2, '6 5'))
    for side in (1, -1):
        pts = polar_lobe(cx, cy, R, lambda t: abs(math.sin(t)), side=side)
        o.append(P(pts, AC, 3, fill=ACS))
    # the element itself
    o.append(RECT(cx - 5, cy - 22, 10, 44, AC, AC, 2))
    o.append(L(cx + 16, cy + 16, cx + 16, cy - 18, NX, 2.2, arrow='x'))
    o.append(Tb(cx + 26, cy + 4, 'I₀', 14, 'start', NX, bold=True))
    # broadside point
    bx = cx + R
    o.append(C(bx, cy, 6, LV))
    o.append(L(bx, cy + 6, bx - 30, cy + 86, LV, 1.6))
    o.append(Tb(bx - 30, cy + 102, 'θ = 90°: 62.8 mV/m', 14, 'middle', LV, bold=True))
    # 30 degree point
    t = Rd(30); r = math.sin(t) * R
    px, py = cx + r * math.sin(t), cy - r * math.cos(t)
    o.append(L(cx, cy, cx + (R + 6) * math.sin(t), cy - (R + 6) * math.cos(t), NX, 1.6, '5 4'))
    o.append(C(px, py, 6, NX))
    o.append(Tb(px + 12, py - 10, 'θ = 30°: 31.4 mV/m', 14, 'start', NX, bold=True))
    o.append(f'<path d="M{cx:.1f},{cy - 46:.1f} A46,46 0 0,1 {cx + 46 * math.sin(t):.1f},{cy - 46 * math.cos(t):.1f}" style="fill:none;stroke:var(--next);stroke-width:1.8"/>')
    o.append(T(cx + 14, cy - 54, 'θ', 14, 'start', NX))
    o.append(T(cx - R * 0.5 - 6, cy + 18, '0.5', 13, 'end', MUT))
    o.append(T(cx - R - 6, cy + 18, '1', 13, 'end', MUT))
    # numbers panel
    x0 = 430
    o.append(RECT(x0, 52, 272, 206, PANEL, L2, 8, 1.5))
    rows = [('l = 1 cm, I₀ = 1 A, f = 1 GHz', INK, True), ('λ = 0.3 m, l/λ = 0.0333', INK, False),
            (sub('R', 'r', 14) + '= 80π²(l/λ)² = 0.877 Ω', AC, False), (sub('P', 'rad', 14) + '= ½ I₀² ' + sub('R', 'r', 14) + '= 0.439 W', AC, False),
            ('at r = 100 m (βr = 2094):', MUT, False), ('|E| = 62.8 sin θ mV/m', LV, True), ('S = 5.24 µW/m² broadside', LV, False)]
    for i, (s, col, b) in enumerate(rows):
        o.append(T(x0 + 14, 80 + i * 27, s, 14, 'start', col, bold=b))
    o.append(RECT(x0, 276, 272, 92, NXS, NX, 8, 1.5))
    o.append(T(x0 + 14, 302, 'Near terms 1/r², 1/r³ equal the', 14, 'start', INK))
    o.append(T(x0 + 14, 326, '1/r term at r = λ/2π = 4.8 cm;', 14, 'start', INK))
    o.append(T(x0 + 14, 350, 'below 2 % beyond r = 10λ = 3 m', 14, 'start', INK))
    return 392, ''.join(o)

FIG[1] = (f1, 'The worked example’s 1 cm element at 1 GHz, drawn in a plane through the wire: the far field is 62.8 sin θ mV/m at 100 m, '
              'so it is largest broadside, half as large at θ = 30° and zero along the wire.',
          'Polar plot of the field of a short vertical current element: two circles touching at the element, widest to the left and right. '
          'The point at 90 degrees is marked 62.8 millivolts per metre and the point at 30 degrees 31.4. A side panel lists l = 1 cm, 1 GHz, radiation resistance 0.877 ohm and radiated power 0.439 watt.')


# ---- 2.2 two power patterns with the same 90 degree beamwidth but different directivity ----
def f2():
    o = []
    # left: sin^2 theta (dipole), axis vertical
    cx, cy, R = 185, 215, 140
    o.append(T(cx, 34, 'Short dipole: sin²θ', 15, bold=True, fill=AC))
    o.append(grid(cx, cy, R))
    o.append(L(cx, cy - R - 14, cx, cy + R + 14, L2, 1.4, '6 5'))
    for side in (1, -1):
        o.append(P(polar_lobe(cx, cy, R, lambda t: math.sin(t) ** 2, side=side), AC, 3, fill=ACS))
    for th in (45, 135):
        t = Rd(th); r = 0.5 * R
        o.append(L(cx, cy, cx + (R + 4) * math.sin(t), cy - (R + 4) * math.cos(t), LV, 1.8, '5 4'))
        o.append(C(cx + r * math.sin(t), cy - r * math.cos(t), 5, LV))
    o.append(f'<path d="M{cx + 112 * math.sin(Rd(45)):.1f},{cy - 112 * math.cos(Rd(45)):.1f} A112,112 0 0,1 {cx + 112 * math.sin(Rd(135)):.1f},{cy - 112 * math.cos(Rd(135)):.1f}" style="fill:none;stroke:var(--live);stroke-width:2.2"/>')
    o.append(Tb(cx + 92, cy + 106, 'HPBW 90°', 14, 'start', LV, bold=True))
    o.append(Tb(cx + 60, cy - 40, 'half power', 13, 'start', MUT))
    o.append(T(cx, cy + R + 36, 'D = 1.5 (1.76 dBi)', 15, bold=True, fill=AC))
    # right: cos^2 theta upper half space
    cx2, cy2, R2 = 535, 300, 200
    o.append(T(cx2, 34, 'Upper half only: cos²θ', 15, bold=True, fill=NX))
    o.append(f'<path d="M{cx2 - R2 * 0.5:.1f},{cy2:.1f} A{R2 * 0.5:.1f},{R2 * 0.5:.1f} 0 0,1 {cx2 + R2 * 0.5:.1f},{cy2:.1f}" style="fill:none;stroke:var(--line);stroke-width:1.2;stroke-dasharray:4 4"/>')
    o.append(f'<path d="M{cx2 - R2:.1f},{cy2:.1f} A{R2:.1f},{R2:.1f} 0 0,1 {cx2 + R2:.1f},{cy2:.1f}" style="fill:none;stroke:var(--line);stroke-width:1.2;stroke-dasharray:4 4"/>')
    o.append(L(cx2 - R2 - 12, cy2, cx2 + R2 + 12, cy2, INK, 2.5))
    pts = polar_lobe(cx2, cy2, R2, lambda t: math.cos(t) ** 2, 0, 90, 1)[::-1] + polar_lobe(cx2, cy2, R2, lambda t: math.cos(t) ** 2, 0, 90, -1)[1:]
    o.append(P(pts, NX, 3, fill=NXS))
    for side in (1, -1):
        t = Rd(45); r = 0.5 * R2
        o.append(L(cx2, cy2, cx2 + side * (R2 * 0.72) * math.sin(t), cy2 - (R2 * 0.72) * math.cos(t), LV, 1.8, '5 4'))
        o.append(C(cx2 + side * r * math.sin(t), cy2 - r * math.cos(t), 5, LV))
    o.append(f'<path d="M{cx2 - 70 * math.sin(Rd(45)):.1f},{cy2 - 70 * math.cos(Rd(45)):.1f} A70,70 0 0,1 {cx2 + 70 * math.sin(Rd(45)):.1f},{cy2 - 70 * math.cos(Rd(45)):.1f}" style="fill:none;stroke:var(--live);stroke-width:2.2"/>')
    o.append(Tb(cx2, cy2 - 78, 'HPBW 90°', 14, 'middle', LV, bold=True))
    o.append(T(cx2, cy2 + 26, 'no radiation below the plane', 13, fill=MUT))
    o.append(T(cx2, cy2 + 51, 'D = 6.00 (7.78 dBi); estimate 41 253/90² = 5.09', 14, bold=True, fill=NX))
    return 400, ''.join(o)

FIG[2] = (f2, 'The two worked examples drawn as power patterns. Both have a 90° half-power beamwidth, yet the second puts all its power '
              'into the upper half space, so its directivity is 6.00 (7.78 dBi) against the dipole’s 1.5 (1.76 dBi).',
          'Left: the power pattern sine squared theta of a short dipole, two lobes either side of a vertical axis, with half-power points at 45 and 135 degrees and a 90 degree beamwidth arc; directivity 1.5. '
          'Right: a single upward lobe cos squared theta above a ground line, half-power points at 45 degrees either side of vertical, beamwidth 90 degrees, directivity 6.')


# ---- 2.3 radiation efficiency of a short dipole against its length ----
def f3():
    o = []
    x0, x1, y0, y1 = 90, 660, 70, 320
    fx = lambda u: x0 + u / 0.12 * (x1 - x0)
    fy = lambda e: y1 - e * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12], [0, 0.25, 0.5, 0.75, 1.0], fx, fy,
                  'dipole length l/λ', 'radiation efficiency', xfmt=lambda v: f'{v:.2f}', yfmt=lambda v: f'{v:.2f}'))
    for RL, col, lab, ly in ((0.5, AC, sub('R', 'L', 14) + '= 0.5 Ω', 0.43), (0.1, NX, sub('R', 'L', 14) + '= 0.1 Ω', 0.93)):
        pts = []
        for i in range(2, 121):
            u = i / 1000
            Rr = 20 * math.pi ** 2 * u * u
            pts.append((fx(u), fy(Rr / (Rr + RL))))
        o.append(P(pts, col, 3))
    o.append(Tb(fx(0.108), fy(0.71), sub('R', 'L', 14) + '= 0.5 Ω', 14, 'middle', AC, bold=True))
    o.append(Tb(fx(0.016), fy(0.80), sub('R', 'L', 14) + '= 0.1 Ω', 14, 'middle', NX, bold=True))
    for u, lab, dx, anc in ((0.02, 'λ/50: 0.14', 14, 'start'), (0.05, 'λ/20: 0.50 (worked example)', 14, 'start'), (0.10, 'λ/10: 0.80', 0, 'middle')):
        Rr = 20 * math.pi ** 2 * u * u; e = Rr / (Rr + 0.5)
        o.append(L(fx(u), fy(e), fx(u), y1, L2, 1.2, '4 4'))
        o.append(C(fx(u), fy(e), 6, AC))
        o.append(Tb(fx(u) + dx, fy(e) + (5 if dx else -16), lab, 14, anc, INK, bold=(u == 0.05)))
    o.append(T(x1, 36, sub('R', 'r', 14) + '= 20π²(l/λ)², η = ' + sub('R', 'r', 14) + '/(' + sub('R', 'r', 14) + '+ ' + sub('R', 'L', 14, False) + ')', 14, 'end', MUT))
    return 372, ''.join(o)

FIG[3] = (f3, 'Radiation efficiency of a centre-fed short dipole, computed from R<sub>r</sub> = 20π²(l/λ)². With the worked example’s 0.5 Ω '
              'of loss, a λ/20 dipole radiates only half its input, a λ/50 dipole 14 per cent; cutting the loss to 0.1 Ω lifts the whole curve.',
          'Plot of radiation efficiency from 0 to 1 against dipole length from 0 to 0.12 wavelengths, for loss resistances of 0.5 and 0.1 ohm. '
          'On the 0.5 ohm curve the points lambda over 50 at 0.14, lambda over 20 at 0.50 and lambda over 10 at 0.80 are marked.')


# ---- 2.4 the three regions of the DTH dish, on a log distance scale ----
def f4():
    o = []
    x0, x1 = 120, 690
    lo, hi = math.log10(0.3), math.log10(100)
    fx = lambda r: x0 + (math.log10(r) - lo) / (hi - lo) * (x1 - x0)
    yb, yt = 250, 110
    bands = [(0.3, 1.82, NXS, 'reactive', 'near field'), (1.82, 28.8, ACS, 'radiating near field', '(Fresnel)'), (28.8, 100, LVS, 'far field', '(Fraunhofer)')]
    for a, b, fill, t1, t2 in bands:
        o.append(f'<rect x="{fx(a):.1f}" y="{yt}" width="{fx(b) - fx(a):.1f}" height="{yb - yt}" style="fill:{fill}"/>')
        xm = (fx(a) + fx(b)) / 2
        o.append(T(xm, yt + 34, t1, 14, bold=True)); o.append(T(xm, yt + 54, t2, 14, fill=MUT))
    # dish at the left
    o.append(f'<path d="M{x0 - 18:.1f},{yt + 8:.1f} Q{x0 - 70:.1f},{(yt + yb) / 2:.1f} {x0 - 18:.1f},{yb - 8:.1f}" style="fill:none;stroke:var(--ink);stroke-width:4"/>')
    o.append(L(x0 - 52, (yt + yb) / 2, x0 - 10, (yt + yb) / 2, INK, 2))
    o.append(T(x0 - 44, yb + 32, 'D = 0.6 m', 14, 'middle', INK, bold=True))
    o.append(T(x0 - 44, yb + 52, '12 GHz', 14, 'middle', MUT))
    o.append(xaxis(x0, x1, yb, [0.5, 1, 2, 5, 10, 20, 50, 100], fx, 'distance from the dish r (m), log scale',
                   fmt=lambda v: f'{v:g}'))
    for r, lab, col in ((1.82, '0.62√(D³/λ) = 1.82 m', NX), (28.8, '2D²/λ = 28.8 m', LV)):
        o.append(L(fx(r), yt - 34, fx(r), yb, col, 2.5))
        o.append(Tb(fx(r), yt - 40, lab, 14, 'middle', col, bold=True))
    # the technician at 20 m
    xt = fx(20)
    o.append(L(xt, yt + 70, xt, yb - 6, INK, 2, '4 4'))
    o.append(C(xt, yt + 108, 7, INK))
    o.append(Tb(xt - 10, yt + 92, 'terrace at 20 m: still Fresnel', 14, 'end', INK, bold=True))
    o.append(T(x0, 36, 'λ = 0.025 m; the pattern is fixed only beyond 28.8 m', 14, 'start', MUT))
    return 320, ''.join(o)

FIG[4] = (f4, 'The worked example’s 0.6 m DTH dish at 12 GHz. Stored fields dominate out to 1.82 m, the beam is still forming '
              'until 28.8 m, and only beyond that is the pattern fixed, so a check from a terrace 20 m away is too close.',
          'A dish at the left and a horizontal log-scale distance axis from 0.3 to 100 metres split into three shaded bands: reactive near field up to 1.82 m, '
          'radiating near field from 1.82 to 28.8 m, and far field beyond 28.8 m. A point at 20 m is marked as still in the Fresnel region.')


# ---- 2.5 current on the half-wave dipole and the monopole with its image ----
def f5():
    o = []
    # left: dipole, vertical, length 1.41 m drawn as 260 px
    cx, cy, H = 150, 200, 130
    o.append(T(cx + 40, 34, 'Half-wave dipole', 15, bold=True, fill=AC))
    o.append(L(cx, cy - H, cx, cy - 6, INK, 4)); o.append(L(cx, cy + 6, cx, cy + H, INK, 4))
    o.append(C(cx, cy, 5, NX))
    pts = [(cx + 80 * math.cos(math.pi / 2 * (z / H)), cy - z) for z in range(-H, H + 1, 4)]
    o.append(P(pts, AC, 3))
    o.append(P([(cx, cy - H), (cx + 80, cy), (cx, cy + H)], MUT, 2, '6 5'))
    o.append(L(cx, cy, cx + 80, cy, L2, 1.2, '3 3'))
    o.append(T(cx + 88, cy + 5, 'I₀', 14, 'start', AC, bold=True))
    o.append(T(cx + 64, cy - 66, 'I₀ cos βz', 14, 'start', AC))
    o.append(T(cx + 46, cy + 100, 'short dipole', 13, 'start', MUT))
    o.append(T(cx + 46, cy + 117, '(triangle)', 13, 'start', MUT))
    o.append(T(cx - 14, cy - H + 6, 'I = 0', 13, 'end', MUT)); o.append(T(cx - 14, cy + H + 4, 'I = 0', 13, 'end', MUT))
    o.append(L(cx - 58, cy - H, cx - 58, cy + H, L2, 1.5)); o.append(L(cx - 64, cy - H, cx - 52, cy - H, L2, 1.5)); o.append(L(cx - 64, cy + H, cx - 52, cy + H, L2, 1.5))
    o.append(Tb(cx - 58, cy - 6, '1.41 m', 14, 'middle', INK, bold=True))
    o.append(Tb(cx - 58, cy + 14, '(0.47λ)', 13, 'middle', MUT))
    o.append(T(cx + 40, cy + H + 40, '≈ 73 Ω, D = 1.64 (2.15 dBi)', 14, bold=True, fill=AC))
    # right: monopole over ground with image
    mx, gy, Hm = 500, 200, 110
    o.append(T(mx, 34, 'Quarter-wave monopole', 15, bold=True, fill=NX))
    o.append(R(mx - 150, gy, 300, 12, L2, L2, 0, 1))
    o.append(T(mx + 150, gy + 32, 'ground plane', 13, 'end', MUT))
    o.append(L(mx, gy - Hm, mx, gy - 4, INK, 4))
    o.append(L(mx, gy + 16, mx, gy + 12 + Hm, MUT, 3, '7 5'))
    o.append(T(mx - 12, gy + 12 + Hm * 0.7, 'image', 13, 'end', MUT))
    pts = [(mx + 70 * math.cos(math.pi / 2 * (z / Hm)), gy - z) for z in range(0, Hm + 1, 4)]
    o.append(P(pts, NX, 3))
    o.append(T(mx + 78, gy - 8, 'I₀', 14, 'start', NX, bold=True))
    o.append(L(mx + 112, gy - Hm, mx + 112, gy, L2, 1.5)); o.append(L(mx + 106, gy - Hm, mx + 118, gy - Hm, L2, 1.5))
    o.append(Tb(mx + 112, gy - Hm / 2, 'λ/4 = 0.75 m', 14, 'start', INK, bold=True))
    o.append(T(mx, gy + Hm + 56, '36.5 Ω, D = 3.28 (5.16 dBi)', 14, bold=True, fill=NX))
    o.append(T(mx, gy + Hm + 78, 'same power: field × 1.414 (+3 dB)', 13, fill=MUT))
    return 408, ''.join(o)

FIG[5] = (f5, 'Current along the worked examples’ 100 MHz antennas. On the 1.41 m dipole it is a cosine, largest at the feed and zero at the tips '
              '(a short dipole’s falls in a straight line); the 0.75 m monopole carries the top half, and the ground plane supplies the mirror image.',
          'Left: a vertical dipole 1.41 metres long with its cosine current envelope, maximum at the centre feed, zero at the tips, and a dashed triangle for a short dipole; about 73 ohms, directivity 1.64. '
          'Right: a quarter-wave monopole 0.75 metres tall on a ground plane with a dashed image below; 36.5 ohms, directivity 3.28.')


# ---- 2.6 the small loop: moment, pattern and the worked example ----
def f6():
    o = []
    cx, cy, R = 220, 205, 140
    o.append(L(cx, cy - R - 20, cx, cy + R + 20, L2, 1.4, '6 5'))
    o.append(T(cx + 8, cy - R - 26, 'loop axis: null', 14, 'start', MUT))
    for side in (1, -1):
        o.append(P(polar_lobe(cx, cy, R, lambda t: abs(math.sin(t)), side=side), LV, 3, fill=LVS))
    # loop drawn edge-on as an ellipse
    o.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="44" ry="13" style="fill:none;stroke:var(--accent);stroke-width:4"/>')
    o.append(L(cx - 14, cy + 13, cx + 10, cy + 13, AC, 2.5, arrow='n'))
    o.append(Tb(cx - 52, cy + 6, 'I', 14, 'end', AC, bold=True))
    o.append(L(cx, cy - 16, cx, cy - 70, NX, 3, arrow='x'))
    o.append(Tb(cx + 10, cy - 58, 'm = NIA', 14, 'start', NX, bold=True))
    o.append(Tb(cx, cy + R * 0.5 + 40, 'largest in the plane of the loop', 14, 'middle', LV, bold=True))
    o.append(T(cx - R + 4, cy - 14, sub('E', 'φ', 14) + '∝ sin θ', 14, 'start', LV))
    # numbers panel
    x0 = 418
    o.append(RECT(x0, 48, 286, 236, PANEL, L2, 8, 1.5))
    rows = [('N = 10 turns, a = 0.1 m, 10 MHz', INK, True), ('C = 0.628 m < λ/10 = 3 m: small', INK, False),
            ('A = 0.0314 m², NA/λ² = 3.49 × 10⁻⁴', INK, False), (sub('R', 'r', 14) + '= 31 171 × (3.49 × 10⁻⁴)²', AC, False),
            ('      = 3.8 mΩ', AC, True), (sub('R', 'L', 14) + '= 0.05 Ω of copper loss', NX, False), ('efficiency = 3.8/53.8 = 7 %', NX, True)]
    for i, (s, col, b) in enumerate(rows):
        o.append(T(x0 + 14, 78 + i * 29, s, 14, 'start', col, bold=b))
    o.append(T(x0 + 14, 318, 'Halve the radius: ' + sub('R', 'r', 14) + '÷ 16', 14, 'start', MUT))
    return 372, ''.join(o)

FIG[6] = (f6, 'A small loop is a magnetic dipole: its moment m = NIA points along the axis, where the field is zero, and it radiates most in its own plane. '
              'For the worked example’s 10-turn loop at 10 MHz, R<sub>r</sub> is only 3.8 mΩ against 0.05 Ω of loss, so 7 per cent of the power radiates.',
          'A loop seen edge-on with its axis vertical and the moment m = N I A drawn along the axis. Two pattern lobes extend left and right, in the plane of the loop, with nulls along the axis. '
          'A panel gives the worked example: 10 turns of radius 0.1 metre at 10 megahertz, radiation resistance 3.8 milliohm, loss 0.05 ohm, efficiency 7 percent.')


# ---- 2.7 the receiving half-wave dipole as a Thevenin source ----
def f7():
    o = []
    # antenna and wave
    ax, ay = 90, 190
    o.append(L(ax, ay - 110, ax, ay - 8, INK, 4)); o.append(L(ax, ay + 8, ax, ay + 110, INK, 4))
    for i, y in enumerate((ay - 70, ay, ay + 70)):
        o.append(L(20 + 0, y - 0, ax - 20, y, LV, 2, arrow='l'))
    o.append(T(18, 62, 'E = 1 mV/m', 14, 'start', LV, bold=True))
    o.append(T(18, 330, '100 MHz, λ = 3 m', 14, 'start', MUT))
    o.append(L(ax + 4, ay - 4, 150, ay - 40, INK, 1.5)); o.append(L(ax + 4, ay + 4, 150, ay + 40, INK, 1.5))
    o.append(T(ax + 18, 360, sub('l', 'eff', 14) + '= λ/π = 0.955 m', 14, 'start', AC, bold=True))
    o.append(T(196, ay + 6, '≡', 28, 'middle', MUT))
    # circuit: source at left, series Z_A on top, load at right
    xl, xr, yt, yb = 250, 650, 90, 290
    o.append(L(xl, yt, xl, 160, INK, 2)); o.append(L(xl, 220, xl, yb, INK, 2))
    o.append(f'<circle cx="{xl}" cy="190" r="30" style="fill:var(--panel);stroke:var(--accent);stroke-width:2.5"/>')
    o.append(T(xl, 184, '+', 16, bold=True)); o.append(T(xl, 206, '−', 16, bold=True))
    o.append(T(xl + 42, 186, sub('V', 'oc', 14), 15, 'start', AC, bold=True))
    o.append(T(xl + 42, 206, '0.955 mV', 14, 'start', AC))
    o.append(L(xl, yt, 360, yt, INK, 2))
    o.append(R(360, yt - 18, 130, 36, ACS, AC, 4))
    o.append(T(425, yt + 6, sub('Z', 'A', 14) + '= 73 Ω', 14, bold=True))
    o.append(T(425, yt - 28, 'antenna (' + sub('R', 'r', 13, False) + ')', 13, fill=MUT))
    o.append(L(490, yt, xr, yt, INK, 2)); o.append(L(xr, yt, xr, 150, INK, 2)); o.append(L(xr, 230, xr, yb, INK, 2))
    o.append(R(xr - 18, 150, 36, 80, NXS, NX, 4))
    o.append(T(xr - 28, 186, sub('Z', 'L', 14) + '= 73 Ω', 14, 'end', NX, bold=True))
    o.append(T(xr - 28, 206, 'receiver', 13, 'end', MUT))
    o.append(L(xl, yb, xr, yb, INK, 2))
    o.append(L(540, yt - 14, 600, yt - 14, NX, 2, arrow='x'))
    o.append(T(570, yt - 22, 'I', 14, 'middle', NX, bold=True))
    o.append(R(300, 310, 360, 66, PANEL, L2, 8, 1.5))
    o.append(T(480, 336, sub('P', 'L', 14) + '= ' + sub('V', 'oc', 14, False) + '²/(8 × 73) = 1.56 nW', 14, bold=True, fill=NX))
    o.append(T(480, 362, 'same as S × ' + sub('A', 'em', 14) + '= 1.326 nW/m² × 1.175 m²', 14, fill=MUT))
    return 392, ''.join(o)

FIG[7] = (f7, 'The worked example’s half-wave dipole as a receiver: the 1 mV/m wave induces V<sub>oc</sub> = E × λ/π = 0.955 mV behind the antenna’s own '
              '73 Ω, and a matched 73 Ω receiver takes 1.56 nW, the same as power density times effective area.',
          'Left: a vertical dipole with three arrows of an incoming wave of 1 millivolt per metre, effective length 0.955 metre. Right: its equivalent circuit, a source of 0.955 millivolt '
          'in series with the antenna impedance of 73 ohms driving a 73 ohm receiver load; the load power is 1.56 nanowatt.')


# ---- 2.8 the 6 GHz hop as a level diagram ----
def f8():
    o = []
    x0, x1, y0, y1 = 96, 700, 60, 330
    lo, hi = -90, 70
    fy = lambda d: y0 + (hi - d) / (hi - lo) * (y1 - y0)
    for v in range(-80, 71, 20):
        Y = fy(v)
        o.append(L(x0, Y, x1, Y, 'var(--line)', 1)); o.append(T(x0 - 8, Y + 4.5, neg(v), 13, 'end', MUT))
    o.append(L(x0, y0, x0, y1, L2, 1.5))
    o.append(T(x0, y0 - 16, 'level (dBm)', 14, 'start', MUT))
    stages = [('Tx', 30.0), ('feeder', 28.0), ('EIRP', 62.95), ('40 km path', -77.09), ('Rx dish', -42.14), ('Rx in', -44.14)]
    steps = ['', '−2', '+34.95', '−140.04', '+34.95', '−2']
    xs = [x0 + 44 + i * 100 for i in range(len(stages))]
    pts = []
    for i, ((name, v), x) in enumerate(zip(stages, xs)):
        if i: pts.append((x, fy(stages[i - 1][1])))
        pts.append((x, fy(v)))
    o.append(P(pts, AC, 3))
    for i, ((name, v), x) in enumerate(zip(stages, xs)):
        o.append(C(x, fy(v), 6, AC if i not in (2, 5) else NX))
        lab = f'{v:.2f}'.rstrip('0').rstrip('.') if i not in (0, 1) else f'{v:.0f}'
        dy = 24 if (v < -60 or i == 5) else -12
        o.append(Tb(x + (8 if i < 5 else 0), fy(v) + dy, neg(lab), 14, 'start' if i < 5 else 'middle', NX if i in (2, 5) else INK, bold=True))
        o.append(T(x, y1 + 22, name, 13, 'middle', MUT))
        if steps[i] and abs(float(steps[i].replace('−', '-'))) > 5:
            o.append(T(x - 6, (fy(v) + fy(stages[i - 1][1])) / 2 + 4, neg(steps[i]) + ' dB', 13, 'end', MUT))
    ys = fy(-75)
    o.append(L(x0, ys, x1, ys, LV, 2.5, '8 5'))
    o.append(Tb(x0 + 150, ys + 20, 'sensitivity −75 dBm', 14, 'middle', LV, bold=True))
    xm = xs[5] + 30
    o.append(L(xm, fy(-44.14) + 2, xm, ys - 4, LV, 2.2, arrow='l'))
    o.append(Tb(xm - 8, (fy(-44.14) + ys) / 2 + 14, 'margin 30.9 dB', 14, 'end', LV, bold=True))
    return 366, ''.join(o)

FIG[8] = (f8, 'The worked example’s 6 GHz hop as a level diagram: 1 W (30 dBm) loses 2 dB in the feeder, the 34.95 dBi dish lifts it to 62.95 dBm EIRP, '
              '40 km of free space takes 140.04 dB, and the far dish and feeder leave −44.1 dBm, 30.9 dB above the −75 dBm sensitivity.',
          'A staircase of signal level in dBm through the link: transmitter 30, after the feeder 28, EIRP 62.95, after the 40 kilometre path minus 77.09, after the receiving dish minus 42.14, '
          'at the receiver input minus 44.14. A dashed line at minus 75 dBm marks the sensitivity and an arrow marks the 30.9 dB margin.')


spec = make_spec(FIG)
