"""Claude's hand-drawn figures for ec-antenna-u3 (antenna arrays, types and propagation), one per chapter.
Every curve and marked value is computed from that chapter's own worked example; colours are the shell's CSS variables."""
import os, sys, math, cmath
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
SUB = lambda s: f'<tspan dy="4" font-size="11">{s}</tspan><tspan dy="-4">​</tspan>'
D2R = math.pi / 180


def af(N, d, alpha, th, amps=None):
    a = amps or [1] * N
    psi = 2 * math.pi * d * math.cos(th) + alpha
    s = sum(a[n] * cmath.exp(1j * n * psi) for n in range(N))
    return abs(s) / sum(a)


def m(v):
    return str(v).replace('-', '−')


def polar_grid(cx, cy, r, rings=(0.5, 1.0), spokes=(0, 30, 60, 90, 120, 150, 180)):
    o = []
    for k in rings:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r * k:.1f}" style="fill:none;stroke:var(--line);stroke-width:1"/>')
    for a in spokes:
        x, y = cx + r * math.cos(a * D2R), cy - r * math.sin(a * D2R)
        o.append(L(cx, cy, x, y, LN, 1))
        x2, y2 = cx + (r + 18) * math.cos(a * D2R), cy - (r + 18) * math.sin(a * D2R)
        o.append(T(x2, y2 + 5, f'{a}°', 13, 'middle', MUT))
    return ''.join(o)


# ---- 3.1 two sources, d = λ/2, element 2 leads by 90° (worked example 1) ----
def f1():
    o = []
    cx, cy, r = 330, 215, 165
    o.append(polar_grid(cx, cy, r, spokes=(30, 60, 90, 120, 150)))
    pts = []
    for i in range(0, 361):
        th = i * D2R if i <= 180 else (360 - i) * D2R
        f = af(2, 0.5, math.pi / 2, th)
        ang = i * D2R
        pts.append((cx + r * f * math.cos(ang), cy - r * f * math.sin(ang)))
    o.append(P(pts, AC, 3, fill=ACS, op=0.55))
    o.append(L(cx - r - 40, cy, cx + r + 40, cy, L2, 1.5, arrow='m'))
    o.append(T(cx + r + 22, cy - 10, '0°', 13, 'middle', MUT)); o.append(T(cx + r + 30, cy + 22, 'z', 14, 'middle', MUT, False, True))
    o.append(T(cx - r - 40, cy - 10, '180°', 13, 'start', MUT))
    o.append(C(cx - 20, cy, 6, INK)); o.append(C(cx + 20, cy, 6, INK))
    o.append(T(cx - 20, cy + 24, '1', 13, 'middle', INK, True)); o.append(T(cx + 20, cy + 24, '2', 13, 'middle', INK, True))
    # max at 120
    mx, my = cx + r * math.cos(120 * D2R), cy - r * math.sin(120 * D2R)
    o.append(C(mx, my, 6, LV)); o.append(Tb(mx - 14, my + 22, 'maximum at 120°', 14, 'end', LV, True))
    nx, ny = cx + (r * 0.55) * math.cos(60 * D2R), cy - (r * 0.55) * math.sin(60 * D2R)
    o.append(C(cx + 2, cy - 3, 4, NX))
    o.append(Tb(nx + 12, ny, 'null at 60°', 14, 'start', NX, True))
    o.append(L(nx + 8, ny + 4, cx + 6, cy - 8, NX, 1.5, arrow='x'))
    f0 = af(2, 0.5, math.pi / 2, 0)
    o.append(C(cx + r * f0, cy, 5, AC)); o.append(Tb(cx + r * f0 + 4, cy + 26, '0.707 at 0°', 13, 'start', AC))
    # side panel
    x0 = 560
    o += [T(x0, 70, 'd = λ/2, α = +90°', 14, 'start', INK, True), T(x0, 96, 'ψ = π cosθ + π/2', 14, 'start'),
          T(x0, 130, 'ψ = 0 → cosθ = −0.5', 13, 'start', LV), T(x0, 150, 'θ = 120°', 13, 'start', LV, True),
          T(x0, 184, 'ψ = π → cosθ = 0.5', 13, 'start', NX), T(x0, 204, 'θ = 60°', 13, 'start', NX, True),
          T(x0, 240, 'rings: 0.5 and 1.0', 13, 'start', MUT), T(x0, 260, 'of the peak field', 13, 'start', MUT)]
    return 410, ''.join(o)


FIG[1] = (f1, 'The field pattern of the first worked example in a plane through the array axis. With element 2 leading by 90°, the beam swings to 120°, back toward the lagging element 1, and the null sits at 60°; along the axis at 0° the field is 0.707 of the peak.',
          'Polar plot of a two-element array pattern: elements 1 and 2 on a horizontal axis, a lobe pointing up-left at 120 degrees, a null at 60 degrees, and the field 0.707 along the axis to the right.')


# ---- 3.2 four elements broadside, d = λ/2 (worked example 1) ----
def f2():
    o = []
    x0, x1, y0, y1 = 80, 650, 50, 300
    fx = lambda t: x0 + (x1 - x0) * t / 180
    fy = lambda v: y1 - (y1 - y0) * v
    o.append(axes(x0, x1, y0, y1, [0, 30, 60, 90, 120, 150, 180], [0, 0.25, 0.5, 0.75, 1.0], fx, fy,
                  'θ from the array axis (degrees)', 'normalized |AF|', xfmt=lambda v: f'{v}°'))
    pts = [(fx(i / 4), fy(af(4, 0.5, 0, i / 4 * D2R))) for i in range(0, 721)]
    o.append(P(pts, AC, 3))
    yh = fy(0.7071)
    o.append(L(x0, yh, x1, yh, LV, 1.6, '5 4'))
    o.append(Tb(x0 + 6, yh - 8, 'half power, 0.707', 13, 'start', LV))
    o.append(L(fx(76.8), yh, fx(76.8), y1, LV, 1.4, '3 3')); o.append(L(fx(103.2), yh, fx(103.2), y1, LV, 1.4, '3 3'))
    o.append(Tb(fx(90), fy(0.55), 'HPBW 26.3°', 13, 'middle', LV, True))
    for t in (60, 120):
        o.append(C(fx(t), y1, 6, NX))
    o.append(Tb(fx(60) - 4, y1 - 14, 'null 60°', 13, 'end', NX, True)); o.append(Tb(fx(120) + 4, y1 - 14, 'null 120°', 13, 'start', NX, True))
    for t in (42.9, 137.1):
        o.append(C(fx(t), fy(0.272), 5, INK))
    o.append(Tb(fx(30), fy(0.272) - 14, '−11.3 dB sidelobe', 13, 'middle', INK))
    o.append(Tb(fx(150), fy(0.272) - 14, '−11.3 dB sidelobe', 13, 'middle', INK))
    o.append(T(fx(90), y0 - 14, 'beam at 90° (broadside)', 13, 'middle', AC, True))
    return 360, ''.join(o)


FIG[2] = (f2, 'The array factor of the 4-element broadside array of the first worked example, d = λ/2. The beam at 90° falls to half power at 76.8° and 103.2°, to zero at 60° and 120°, and the first sidelobes rise only to 0.272 of the peak (−11.3 dB).',
          'Graph of normalized array factor against angle from 0 to 180 degrees: a main lobe centred on 90 degrees with half-power points at 76.8 and 103.2 degrees, nulls at 60 and 120 degrees, sidelobes of 0.272 at about 43 and 137 degrees.')


# ---- 3.3 five elements: uniform, Dolph-Chebyshev −20 dB, binomial (worked example 1) ----
CHEB = [1, 1.6085, 1.9319, 1.6085, 1]


def f3():
    o = []
    x0, x1, y0, y1 = 80, 650, 50, 310
    fx = lambda t: x0 + (x1 - x0) * t / 180
    fy = lambda db: y0 + (y1 - y0) * (-max(db, -40)) / 40
    o.append(axes(x0, x1, y0, y1, [0, 30, 60, 90, 120, 150, 180], [0, -10, -20, -30, -40], fx, fy,
                  'θ from the array axis (degrees)', 'pattern (dB)', xfmt=lambda v: f'{v}°', yfmt=m))
    def curve(amps, c, w, dash=None):
        pts = []
        for i in range(0, 721):
            v = af(5, 0.5, 0, i / 4 * D2R, amps)
            pts.append((fx(i / 4), fy(20 * math.log10(max(v, 1e-3)))))
        return P(pts, c, w, dash)
    o.append(curve(None, MUT, 2, '6 4'))
    o.append(curve([1, 4, 6, 4, 1], NX, 2.4))
    o.append(curve(CHEB, AC, 3))
    o.append(L(x0, fy(-20), x1, fy(-20), LV, 1.4, '3 3'))
    o.append(Tb(fx(55), fy(-12.0) - 10, 'uniform −12.0 dB', 13, 'middle', MUT))
    o.append(Tb(fx(36), fy(-20) + 22, 'Chebyshev: every sidelobe −20 dB', 13, 'start', AC, True))
    o.append(Tb(fx(130), fy(-33), 'binomial: no sidelobes', 13, 'start', NX, True))
    o.append(T(fx(90), y0 - 14, 'HPBW: uniform 20.8°, Chebyshev 23.7°, binomial 30.3°', 13, 'middle', INK))
    return 370, ''.join(o)


FIG[3] = (f3, 'Five elements with d = λ/2 and three tapers. The uniform array has sidelobes at −12.0 dB; the Dolph-Chebyshev currents 1 : 1.609 : 1.932 : 1.609 : 1 of the worked example hold every sidelobe at −20 dB for a beam only 2.9° wider; the binomial currents 1 : 4 : 6 : 4 : 1 remove the sidelobes but widen the beam to 30.3°.',
          'Graph in decibels of three five-element array patterns against angle: a dashed uniform pattern with minus 12 dB sidelobes, a solid Chebyshev pattern with all sidelobes at minus 20 dB, and a binomial pattern with a broad main lobe and no sidelobes.')


# ---- 3.4 LPDA of worked example 2, drawn to scale ----
def f4():
    o = []
    tau, sig = 0.9, 0.15
    Ls = [750 * tau ** n for n in range(12)]
    ta = (1 - tau) / (4 * sig)
    R = [l / (2 * ta) for l in Ls]            # distance from apex, mm
    s = 0.24                                   # px per mm
    ax, cy = 660, 190                          # apex position
    X = lambda r: ax - r * s
    o.append(L(X(R[0]) - 10, cy, ax, cy, INK, 3))
    o.append(L(ax, cy, X(R[0]) - 10, cy - (Ls[0] / 2 + 12 * ta * 0) * s - 16, L2, 1.2, '5 4'))
    o.append(L(ax, cy, X(R[0]) - 10, cy + (Ls[0] / 2) * s + 16, L2, 1.2, '5 4'))
    for i, (l, r) in enumerate(zip(Ls, R)):
        x = X(r); act = i in (3, 4)
        o.append(L(x, cy - l / 2 * s, x, cy + l / 2 * s, LV if act else AC, 4 if act else 2.6))
    o.append(Tb(X(R[0]), cy - Ls[0] / 2 * s - 14, 'L₁ = 750 mm', 13, 'middle', AC, True))
    o.append(Tb(X(R[11]), cy - Ls[11] / 2 * s - 14, 'L₁₂ = 235 mm', 13, 'middle', AC, True))
    o.append(Tb((X(R[3]) + X(R[4])) / 2, cy + Ls[3] / 2 * s + 26, 'active at 300 MHz', 13, 'middle', LV, True))
    o.append(brace(X(R[0]), X(R[1]), cy + Ls[0] / 2 * s + 12, INK))
    o.append(T((X(R[0]) + X(R[1])) / 2, cy + Ls[0] / 2 * s + 32, 'd₁ = 225 mm', 13, 'middle', INK))
    o.append(brace(X(R[0]), X(R[11]), 345, INK, up=True))
    o.append(T((X(R[0]) + X(R[11])) / 2, 365, 'boom 1544 mm, 12 dipoles, τ = 0.9, σ = 0.15', 13, 'middle', INK))
    o.append(T(ax - 6, cy - 16, 'apex', 13, 'end', MUT))
    o.append(T(ax - 70, cy - 52, 'α = 9.5°', 13, 'middle', MUT))
    o.append(L(X(R[11]) + 12, cy + 34, ax - 4, cy + 34, NX, 2.2, arrow='x'))
    o.append(T((X(R[11]) + ax) / 2 + 6, cy + 56, 'feed and beam', 13, 'middle', NX, True))
    o.append(T(40, 40, 'top view, to scale', 13, 'start', MUT))
    return 380, ''.join(o)


FIG[4] = (f4, 'The 12-dipole log-periodic array of the second worked example, drawn to scale: the dipoles shrink by τ = 0.9 from 750 mm to 235 mm, their tips lie on two lines from the apex 9.5° either side of the boom, and the boom is 1544 mm long. At 300 MHz dipoles 4 and 5, near half a wavelength, do the radiating; the cable connects at the short end and the beam leaves that way.',
          'Top view of a log-periodic dipole array: twelve vertical dipoles along a horizontal boom, longest on the left, shortest on the right, tips touching two dashed lines from an apex at the right; two middle dipoles marked active at 300 MHz; an arrow to the right labelled feed and beam.')


# ---- 3.5 H-plane section of the optimum horn of worked example 1 ----
def f5():
    o = []
    s = 2.4          # px per mm
    ax, cy = 120, 200
    lH, A, a = 111.1, 100.0, 22.86
    X = lambda z: ax + z * s
    za = lH * a / A
    # waveguide
    o.append(R(X(za) - 70, cy - a / 2 * s, 70, a * s, PANEL, AC, 0, 2))
    o.append(T(X(za) - 35, cy + a / 2 * s + 20, 'waveguide', 13, 'middle', MUT))
    o.append(T(X(za) - 35, cy + a / 2 * s + 38, 'a = 22.9 mm', 13, 'middle', MUT))
    o.append(L(X(za), cy - a / 2 * s, X(lH), cy - A / 2 * s, AC, 3)); o.append(L(X(za), cy + a / 2 * s, X(lH), cy + A / 2 * s, AC, 3))
    o.append(L(ax, cy, X(za), cy - a / 2 * s, L2, 1.2, '4 4')); o.append(L(ax, cy, X(za), cy + a / 2 * s, L2, 1.2, '4 4'))
    o.append(C(ax, cy, 4, MUT)); o.append(T(ax - 8, cy + 5, 'apex', 13, 'end', MUT))
    # aperture plane and spherical front
    o.append(L(X(lH), cy - A / 2 * s - 12, X(lH), cy + A / 2 * s + 12, L2, 1.5, '6 4'))
    rr = lH * s; edge = math.atan((A / 2) / lH)
    pts = [(ax + rr * math.cos(t), cy + rr * math.sin(t)) for t in [(-edge + 2 * edge * i / 40) for i in range(41)]]
    o.append(P(pts, LV, 2.5))
    xe = ax + rr * math.cos(edge); ye = cy - rr * math.sin(edge)
    o.append(L(xe, ye, X(lH), ye, NX, 3))
    o.append(Tb(X(lH) - 8, ye - 16, 'δ ≈ A²/(8ℓ) = 11 mm = 0.375λ', 13, 'end', NX, True))
    o.append(T(X(lH) - 40, cy + 5, 'wavefront', 13, 'end', LV, True))
    o.append(brace(ax, X(lH), cy + A / 2 * s + 30, INK))
    o.append(T((ax + X(lH)) / 2, cy + A / 2 * s + 52, 'ℓ = A²/(3λ) = 111 mm', 13, 'middle', INK))
    o.append(L(X(lH) + 150, cy - A / 2 * s, X(lH) + 150, cy + A / 2 * s, INK, 1.4))
    o.append(T(X(lH) + 160, cy - 6, 'A = 100 mm', 13, 'start', INK, True))
    o.append(T(X(lH) + 160, cy + 14, '= 3.33λ', 13, 'start', INK))
    o.append(L(X(lH) + 20, cy + 70, X(lH) + 130, cy + 70, AC, 2.4, arrow='n'))
    o.append(T(X(lH) + 20, cy + 98, 'H-plane beam 20.1°', 13, 'start', AC, True))
    o.append(T(40, 36, 'H-plane section at 10 GHz (λ = 30 mm)', 13, 'start', MUT))
    return 400, ''.join(o)


FIG[5] = (f5, 'The H-plane section of the optimum horn of the first worked example, to scale. The wave spreads from the apex, so its front is curved: at the edge of the 100 mm opening it lags the centre by δ ≈ 11 mm, 0.375λ, the most an optimum H-plane flare allows. A longer horn would be flatter; a shorter one would lose gain.',
          'Cross-section of a horn: a waveguide on the left flaring to a 100 millimetre opening, a curved wavefront that reaches the edge of the opening 11 millimetres behind the centre, the length 111 millimetres from the apex marked below, and a beam arrow to the right.')


# ---- 3.6 the 3 m dish with f/D = 0.4 (worked examples 1 and 2), to scale ----
def f6():
    o = []
    s = 95.0          # px per m
    vx, cy = 120, 200
    f = 1.2
    X = lambda z: vx + z * s
    pts = [(X(r * r / (4 * f)), cy - r * s) for r in [(-1.5 + 3 * i / 60) for i in range(61)]]
    o.append(P(pts, AC, 4))
    fxp = X(f)
    o.append(C(fxp, cy, 6, NX)); o.append(Tb(fxp + 10, cy - 14, 'feed at focus', 13, 'start', NX, True))
    for r in (1.5, 0.9, 0.35, -0.6, -1.2):
        zx = X(r * r / (4 * f)); zy = cy - r * s
        o.append(L(fxp, cy, zx, zy, LV, 1.4))
        o.append(L(zx, zy, X(2.05), zy, LV, 1.4, arrow='l'))
    rim = X(1.5 ** 2 / 4.8)
    o.append(L(rim, cy - 150 * s / 100 * 0 - 1.5 * s, rim, cy + 1.5 * s, L2, 1.4, '6 4'))
    o.append(L(vx, cy, X(2.1), cy, L2, 1.2, '3 3'))
    o.append(brace(vx, fxp, cy + 1.5 * s + 18, INK))
    o.append(T((vx + fxp) / 2, cy + 1.5 * s + 40, 'f = 1.2 m', 13, 'middle', INK))
    o.append(T(rim + 6, cy + 1.5 * s + 4, 'depth 0.47 m', 13, 'start', MUT))
    o.append(L(X(2.25), cy - 1.5 * s, X(2.25), cy + 1.5 * s, INK, 1.4))
    o.append(T(X(2.25) + 10, cy - 6, 'D = 3 m', 13, 'start', INK, True))
    o.append(T(X(2.25) + 10, cy + 14, '= 40λ at 4 GHz', 13, 'start', INK))
    o.append(Tb(fxp + 10, cy + 38, 'rim at ±64°', 13, 'start', NX))
    o.append(T(X(2.05), cy - 1.5 * s - 16, 'plane wave: 39.8 dBi, HPBW 1.75°', 13, 'end', LV, True))
    return 400, ''.join(o)


FIG[6] = (f6, 'The 3 m dish of the worked examples, to scale. Rays from the feed at the focus, 1.2 m in front of the vertex, leave the dish parallel and in phase; the feed must light ±64° to reach the rim of a dish 0.47 m deep. At 4 GHz the 40λ mouth gives 39.8 dBi and a 1.75° beam.',
          'Side view of a parabolic dish opening to the right with a feed at the focus; five rays go from the feed to the dish and leave parallel to the axis; labels give focal length 1.2 metres, depth 0.47 metres, diameter 3 metres and the 64 degree rim angle.')


# ---- 3.7 the 2.4 GHz FR-4 patch of the worked examples ----
def f7():
    o = []
    s = 5.2           # px per mm
    x0, y0 = 70, 60
    Lp, Wp, dL, y0i, wl = 29.44, 38.04, 0.739, 9.78, 3.0
    o.append(R(x0 - 18, y0 - 18, Lp * s + 36, Wp * s + 36, FIGBG, L2, 6, 1.5, '4 4'))
    o.append(R(x0, y0, Lp * s, Wp * s, ACS, AC, 2, 2.5))
    cyp = y0 + Wp * s / 2
    # inset notch and line, entering from the left radiating edge
    gap = 1.0
    o.append(R(x0 - 1, cyp - (wl / 2 + gap) * s, y0i * s, (wl + 2 * gap) * s, FIGBG, FIGBG, 0, 0))
    o.append(L(x0, cyp - (wl / 2 + gap) * s, x0 + y0i * s, cyp - (wl / 2 + gap) * s, AC, 2))
    o.append(L(x0, cyp + (wl / 2 + gap) * s, x0 + y0i * s, cyp + (wl / 2 + gap) * s, AC, 2))
    o.append(L(x0 + y0i * s, cyp - (wl / 2 + gap) * s, x0 + y0i * s, cyp + (wl / 2 + gap) * s, AC, 2))
    o.append(R(x0 - 50, cyp - wl / 2 * s, 50 + y0i * s, wl * s, ACS, AC, 0, 2))
    o.append(T(x0 - 30, cyp + wl / 2 * s + 18, '50 Ω', 13, 'middle', INK))
    o.append(Tb(x0 + y0i * s / 2 + 8, cyp - (wl / 2 + gap) * s - 10, 'y₀ = 9.8', 13, 'middle', NX, True))
    for xe in (x0, x0 + Lp * s):
        o.append(L(xe, y0 - 6, xe, y0 + Wp * s + 6, LV, 5))
    o.append(brace(x0, x0 + Lp * s, y0 + Wp * s + 30, INK))
    o.append(T(x0 + Lp * s / 2, y0 + Wp * s + 50, 'L = 29.4 mm', 13, 'middle', INK, True))
    o.append(L(x0 + Lp * s + 30, y0, x0 + Lp * s + 30, y0 + Wp * s, INK, 1.4))
    o.append(T(x0 + Lp * s + 38, cyp + 5, 'W = 38.0 mm', 13, 'start', INK, True))
    o.append(T(x0 + Lp * s / 2, y0 - 26, 'top view (mm), radiating edges marked', 13, 'middle', MUT))
    # side view, thickness exaggerated
    sx, sy, sw, hh = 450, 150, 220, 44
    o.append(R(sx - 40, sy, sw + 80, hh, NXS, L2, 0, 1.5))
    o.append(L(sx - 40, sy + hh, sx + sw + 40, sy + hh, INK, 4))
    o.append(L(sx, sy, sx + sw, sy, AC, 5))
    o.append(arc(sx, sy + 3, sx - 30, sy + hh - 3, 0.55, LV, 2, 'l'))
    o.append(arc(sx + sw + 30, sy + hh - 3, sx + sw, sy + 3, 0.55, LV, 2, 'l'))
    o.append(L(sx - 8, sy - 16, sx - 36, sy - 16, LV, 2.4, arrow='l'))
    o.append(L(sx + sw + 36, sy - 16, sx + sw + 8, sy - 16, LV, 2.4, arrow='l'))
    o.append(T(sx - 22, sy + hh + 22, 'E down', 13, 'middle', LV))
    o.append(T(sx + sw + 22, sy + hh + 22, 'E up', 13, 'middle', LV))
    o.append(T(sx + sw / 2, sy - 38, 'horizontal fringing fields', 13, 'middle', LV, True))
    o.append(T(sx + sw / 2, sy - 20, 'point the same way', 13, 'middle', LV, True))
    o.append(T(sx + sw / 2, sy + hh + 22, 'ground plane', 13, 'middle', INK))
    o.append(T(sx + sw / 2, sy + hh + 44, 'FR-4: h = 1.6 mm, εr = 4.4', 13, 'middle', INK))
    o.append(T(sx + sw / 2, sy + hh + 64, 'side view, thickness exaggerated', 13, 'middle', MUT))
    return 340, ''.join(o)


FIG[7] = (f7, 'The 2.4 GHz patch of the worked examples on 1.6 mm FR-4. Top view to scale: 29.4 mm by 38.0 mm, with the 50 Ω line inset 9.8 mm into the radiating edge. Side view: the field points down at one radiating edge and up at the other, yet the fringing field runs from patch to ground on one side and from ground to patch on the other, so seen from above both horizontal parts point the same way and the two edges radiate in phase.',
          'Top view of a rectangular patch 29.4 by 38.0 millimetres with an inset 50 ohm feed line 9.8 millimetres deep and its two radiating edges marked; beside it a side view of the patch on a substrate over a ground plane with curved fringing field lines at both edges and two horizontal arrows above them pointing the same way.')


# ---- 3.8 the gain-substitution range of worked example 1 ----
def f8():
    o = []
    o.append(boxt(30, 140, 120, 58, ['signal', 'generator'], PANEL, MUT, 13))
    o.append(L(150, 169, 200, 169, MUT, 2, arrow='m'))
    o.append(P([(200, 140), (250, 120), (250, 218), (200, 198), (200, 140)], AC, 2.5, fill=ACS))
    o.append(T(225, 245, 'source horn', 13, 'middle', INK))
    o.append(P([(520, 120), (470, 140), (470, 198), (520, 218), (520, 120)], LV, 2.5, fill=LVS))
    o.append(T(495, 245, 'standard horn,', 13, 'middle', INK)); o.append(T(495, 263, 'then test antenna', 13, 'middle', INK))
    for x in (250, 470):
        o.append(L(x, 80, x, 260, L2, 1.2, '3 3'))
    o.append(L(254, 92, 466, 92, INK, 1.8, arrow='m')); o.append(L(466, 92, 254, 92, INK, 1.8, arrow='m'))
    o.append(Tb(360, 86, 'R ≥ 2D²/λ = 6 m', 14, 'middle', INK, True))
    o.append(T(360, 112, '(between phase centres)', 13, 'middle', MUT))
    for x in (290, 330, 370, 410, 450):
        o.append(arc(x, 169 - 30, x, 169 + 30, 0.18, AC, 1.4, None))
    o.append(L(520, 169, 570, 169, MUT, 2, arrow='m'))
    o.append(boxt(570, 132, 130, 74, ['receiver', 'std: −30 dBm', 'test: −25 dBm'], PANEL, LV, 13))
    o.append(T(360, 300, 'G(test) = 15 dBi + (−25 − (−30)) dB = 20 dBi', 14, 'middle', LV, True))
    o.append(T(360, 326, 'same cable, same place, same polarization for both readings', 13, 'middle', MUT))
    return 345, ''.join(o)


FIG[8] = (f8, 'Gain by substitution, as in the first worked example: a fixed source horn transmits, and the receiver reads −30 dBm with the 15 dBi standard horn and then −25 dBm with the test antenna in its place. The 5 dB difference gives 20 dBi. The range length R, at least 2D²/λ = 6 m here, is taken between the phase centres.',
          'Diagram of an antenna range: a generator feeds a source horn on the left; curved wavefronts cross a distance R of at least 6 metres to a receive horn on the right that is first a standard horn and then the test antenna; the receiver shows minus 30 and minus 25 dBm.')


# ---- 3.9 sky-wave geometry of worked example 1 (flat earth, h = 300 km) ----
def f9():
    o = []
    s = 0.52          # px per km
    gx, gy = 60, 300
    X = lambda d: gx + d * s
    Y = lambda h: gy - h * s
    o.append(R(gx - 20, Y(330), 680, 30 * s * 2, LVS, LVS, 0, 0))
    o.append(T(X(1180), Y(300) + 5, 'F2 layer, h = 300 km', 13, 'end', LV, True))
    o.append(L(gx - 20, gy, 700, gy, INK, 2.5))
    o.append(C(gx, gy, 6, INK)); o.append(T(gx - 2, gy - 12, 'Tx', 13, 'end', INK, True))
    o.append(P([(X(0), gy), (X(500), Y(300)), (X(1000), gy)], AC, 2.6))
    o.append(P([(X(0), gy), (X(334), Y(300)), (X(668), gy)], NX, 2.6, '7 4'))
    o.append(L(X(500), Y(300), X(500), gy, L2, 1.2, '3 3'))
    o.append(Tb(X(500) + 16, Y(240), 'φ = 59°', 13, 'start', AC, True))
    o.append(C(X(1000), gy, 6, AC)); o.append(T(X(1000), gy + 22, '1000 km: MUF 19.5 MHz', 13, 'middle', AC, True))
    o.append(C(X(668), gy, 6, NX)); o.append(T(X(668), gy + 42, '15 MHz returns from 668 km', 13, 'middle', NX, True))
    o.append(R(X(80), gy - 10, (668 - 80) * s, 10, NXS, NXS, 0, 0))
    o.append(T(X(370), gy - 18, 'skip zone at 15 MHz', 13, 'middle', NX))
    o.append(brace(X(0), X(80), gy + 12, INK))
    o.append(T(X(40), gy + 44, 'ground', 13, 'middle', INK)); o.append(T(X(40), gy + 60, 'wave', 13, 'middle', INK))
    o.append(T(gx, Y(330) - 14, 'fc = 10.0 MHz (N = 1.24 × 10¹² m⁻³)', 13, 'start', MUT))
    return 372, ''.join(o)


FIG[9] = (f9, 'The sky-wave paths of the first worked example, with a flat earth and the F2 layer at 300 km. A ray meeting the layer 59° from the vertical lands 1000 km away, and needs a frequency no higher than the MUF of 19.5 MHz; at 15 MHz the steepest ray that still returns lands 668 km out, leaving a skip zone beyond the short ground-wave range.',
          'Side view of the earth surface and an ionospheric layer at 300 kilometres: a solid ray from the transmitter reflects at the layer and lands at 1000 kilometres, a dashed ray lands at 668 kilometres, and a shaded skip zone lies between the ground-wave range and 668 kilometres.')


spec = make_spec(FIG)
