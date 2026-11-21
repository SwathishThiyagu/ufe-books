# Glass t16 drawings for Optical Fiber Communication (ec-optical). Every value is computed here from the lesson's own numbers.
from dhelp import *
import math
D = {}
deg = math.degrees
CORE, CLAD = '#D9F0FF', '#EEF3F9'


def rays_fiber(x0, x1, yc, h, s=''):
    """a fiber in long section: core of half-height h around yc, cladding bands above and below"""
    s += rect(x0, yc - h - 26, x1 - x0, 26, CLAD, '#C8D3E2', 2, 4) + rect(x0, yc + h, x1 - x0, 26, CLAD, '#C8D3E2', 2, 4)
    s += rect(x0, yc - h, x1 - x0, 2 * h, CORE, 'none', 0, 0)
    s += line(x0, yc - h, x1, yc - h, '#8FB4D9', 2) + line(x0, yc + h, x1, yc + h, '#8FB4D9', 2)
    s += line(x0, yc, x1, yc, MUT, 1.5, '3 6')
    return s


def arc(cx, cy, r, a0, a1, c=INK, w=2.5):
    """arc from angle a0 to a1 in degrees (math angles, y up)"""
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
    sweep = 0 if a1 > a0 else 1
    return f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 0 {sweep} {x1:.1f},{y1:.1f}" fill="none" stroke="{c}" stroke-width="{w}"/>'


# ---------------- unit 1 ----------------
def u1L1():
    # n1 = 1.50, n2 = 1.45, air: theta_c = 75.16 deg (at the wall, from the normal); NA = 0.3841, theta_a = 22.59 deg (at the end, from the axis)
    n1, n2 = 1.50, 1.45
    thc = deg(math.asin(n2 / n1))
    NA = math.sqrt(n1 * n1 - n2 * n2)
    tha = deg(math.asin(NA))
    thr = deg(math.asin(NA / n1))
    s = defs()
    x0, yc, h = 160, 205, 58
    s = rays_fiber(x0, 515, yc, h, s)
    s += txt(505, yc + h - 10, f'core {n1:.2f}', 13, B, 800, 'end') + txt(500, yc + h + 19, f'cladding {n2:.2f}', 13, MUT, 800, 'end')
    s += line(x0, yc - h - 30, x0, yc + h + 30, INK, 3)
    # incoming ray from air
    L = 150
    xa, ya = x0 - L * math.cos(math.radians(tha)), yc + L * math.sin(math.radians(tha))
    s += line(xa, ya, x0, yc, O, 5)
    s += line(x0 - 140, yc, x0, yc, MUT, 2, '6 6')
    s += arc(x0, yc, 70, 180, 180 + tha, O) + txt(x0 - 82, yc + 18, f'θa = {tha:.1f}°', 15, O, 900, 'end')
    # refracted ray inside, to the top wall
    xw = x0 + h / math.tan(math.radians(thr))
    s += line(x0, yc, xw, yc - h, O, 5)
    s += arc(x0, yc, 46, 0, thr, INK) + txt(x0 + 52, yc - 4, f'{thr:.1f}°', 13, INK, 800, 'start')
    # reflected, stopped at the end of the drawn fiber
    xe = 505; ye = yc - h + (xe - xw) * math.tan(math.radians(thr))
    s += line(xw, yc - h, xe, ye, O, 5, arrow=True)
    # normal at the wall and the critical angle
    s += line(xw, yc - h - 40, xw, yc - h + 60, G, 2.5, '6 5')
    xr = xw - 50 * math.sin(math.radians(thc)); yr = yc - h + 50 * math.cos(math.radians(thc))
    s += f'<path d="M{xw:.1f},{yc - h + 50:.1f} A50,50 0 0 1 {xr:.1f},{yr:.1f}" fill="none" stroke="{G}" stroke-width="3"/>'
    s += tag(xw, yc - h - 44, f'θc = {thc:.1f}° at the wall', G, 14)
    s += txt(30, 60, 'air', 16, MUT, 900, 'start')
    s += txt(20, 350, f'NA = √(n₁² − n₂²) = {NA:.4f}', 14, INK, 900, 'start')
    return 'Two angles, two places', s
D['ec-optical-u1-L1'] = (u1L1, 'θa = 22.6°, θc = 75.2°', '1.2.1')


def u1L2():
    # n1 1.48, n2 1.46: NA = 0.2425 -> 14.03 deg; the wrong n1 - n2 = 0.02 -> 1.15 deg
    n1, n2 = 1.48, 1.46
    NA = math.sqrt(n1 * n1 - n2 * n2); th = deg(math.asin(NA))
    bad = n1 - n2; thb = deg(math.asin(bad))
    s = defs()
    x0, yc = 330, 190
    s += rect(x0, yc - 70, 185, 140, CLAD, '#C8D3E2', 2, 6) + rect(x0, yc - 40, 185, 80, CORE, '#8FB4D9', 2, 0)
    s += txt(x0 + 92, yc + 6, 'fiber end', 14, B, 900)
    Lc = 300
    for t, c, dash, wdt in ((th, G, None, 4), (thb, O, '7 6', 4)):
        dy = Lc * math.tan(math.radians(t))
        pts = [(x0, yc), (x0 - Lc, yc - dy), (x0 - Lc, yc + dy)]
        s += poly(pts, c, wdt, dash, fill=(GS if c == G else 'none'), close=True)
    s += tag(x0 - 160, yc - 52, f'NA {NA:.4f}: {th:.1f}°', G, 15)
    s += tag(x0 - 160, yc + 60, f'n₁ − n₂ = {bad:.2f}: {thb:.2f}°', O, 14)
    s += txt(20, 330, f'n₁ = {n1}, n₂ = {n2}', 14, MUT, 800, 'start')
    s += txt(20, 356, f'NA = √(n₁² − n₂²) = √{n1 * n1 - n2 * n2:.4f}', 14, INK, 900, 'start')
    return 'The cone a fiber accepts', s
D['ec-optical-u1-L2'] = (u1L2, 'NA = √(n₁² − n₂²)', '1.3.1')


def u1L3():
    # step 1.48 / 1.46 and parabolic profile, core radius a = 25 um; V = 29.3 -> 429 (step), 215 (graded); diameter gives 58.6
    n1, n2, a = 1.48, 1.46, 25
    NA = math.sqrt(n1 * n1 - n2 * n2); Dl = (n1 * n1 - n2 * n2) / (2 * n1 * n1)
    lam = 1.3
    V = 2 * math.pi * a * NA / lam
    Mst, Mgr = V * V / 2, V * V / 4
    ng = lambda r: n1 * math.sqrt(1 - 2 * Dl * (r / a) ** 2) if abs(r) <= a else n2
    p = Plot(-40, 40, 1.455, 1.485, L=60, T=24, Wd=420, H=190)
    s = defs()
    for v in (1.46, 1.47, 1.48):
        s += line(p.L, p.Y(v), p.L + p.W, p.Y(v), GRID, 1.5) + txt(p.L - 10, p.Y(v) + 5, f'{v:.2f}', 13, MUT, 700, 'end')
    s += line(p.L, p.T + p.H, p.L + p.W + 8, p.T + p.H, MUT, 2.5, arrow=True)
    for v in (-25, 0, 25):
        s += txt(p.X(v), p.T + p.H + 20, g(v), 13, MUT, 700)
    s += txt(p.L + p.W, p.T + p.H + 40, 'radius r (µm) →', 13, MUT, 700, 'end') + txt(p.L + 8, p.T - 8, 'index n', 13, MUT, 700, 'start')
    st = [p.P(-40, n2), p.P(-a, n2), p.P(-a, n1), p.P(a, n1), p.P(a, n2), p.P(40, n2)]
    s += poly(st, B, 4.5)
    s += p.curve(ng, -40, 40, n=200, c=G, w=4.5)
    s += arrow2(p.X(0), p.Y(1.4575), p.X(a), p.Y(1.4575), O, 3) + txt(p.X(a / 2), p.Y(1.4575) - 8, 'a = 25', 14, O, 900)
    s += txt(p.X(-33), p.Y(1.482), 'step', 14, B, 900) + txt(p.X(-12), p.Y(1.466), 'graded', 14, G, 900)
    y = 300
    s += box(10, y, 160, 64, f'V = {V:.1f}', O, 20, sub='radius 25 µm', subc=MUT, fill=OS)
    s += box(185, y, 150, 64, f'{Mst:.0f} modes', B, 18, sub='step index', subc=MUT)
    s += box(350, y, 150, 64, f'{Mgr:.0f} modes', G, 18, sub='graded', subc=MUT)
    return 'Radius in V, not diameter', s
D['ec-optical-u1-L3'] = (u1L3, 'radius 25 µm: V = 29.3', '1.5.1')


def u1L4():
    # buried channel guide: n1 1.50, n2 1.45, t = 0.5 um, lambda 1.55 um: V = 2.027 x 0.3841 = 0.778 < pi
    n1, n2, t0, lam = 1.50, 1.45, 0.5, 1.55
    NA = math.sqrt(n1 * n1 - n2 * n2)
    V = lambda t: 2 * math.pi * t / lam * NA
    tmax = math.pi / (2 * math.pi / lam * NA)
    p = Plot(0, 3, 0, 5, L=50, T=24, Wd=430, H=220)
    s = defs() + sax(p, xt=(0, 0.5, 1, 2, 3), yt=(0, 1, 2, 3, 4, 5), xl='slab thickness t (µm) →', yl='V')
    s += rect(p.X(0), p.Y(math.pi), p.X(tmax) - p.X(0), p.Y(0) - p.Y(math.pi), GS, 'none', 0, 4)
    s += line(p.L, p.Y(math.pi), p.L + p.W, p.Y(math.pi), G, 3) + tag(p.X(2.95), p.Y(math.pi) - 10, 'π: slab limit', G, 13, 'end')
    s += line(p.L, p.Y(2.405), p.L + p.W, p.Y(2.405), O, 2.5, '7 6') + tag(p.X(2.95), p.Y(2.405) + 26, '2.405: round fiber only', O, 12, 'end')
    s += p.curve(V, 0, 3, n=10, c=B, w=5)
    s += dot(*p.P(t0, V(t0)), 10, B) + tag(p.X(t0) + 14, p.Y(V(t0)) + 4, f'{t0} µm: V = {V(t0):.3f}', B, 13, 'start')
    s += line(p.X(tmax), p.Y(0), p.X(tmax), p.Y(math.pi), G, 2, '4 4')
    s += txt(p.X(1.45), p.Y(0.45), 'one mode', 15, G, 900)
    s += txt(p.L, p.T + p.H + 62, f'single-mode while t < {tmax:.2f} µm (n {n1} / {n2}, λ {lam} µm)', 13, MUT, 800, 'start')
    return 'Slab: single-mode below π', s
D['ec-optical-u1-L4'] = (u1L4, 'V = 0.778 < π', '1.8.1')


# ---------------- unit 2 ----------------
def u2L1():
    # Rayleigh 0.14 dB/km at 1550 scaled as 1/lambda^4, IR and UV tails, OH peak 1.10 at 1383 nm on old fiber
    A = 0.14 * 1.55 ** 4
    ray = lambda l: A / l ** 4
    ir = lambda l: 7.81e11 * math.exp(-48.48 / l)
    uv = lambda l: 0.0154 * math.exp(4.63 / l) / 1e3 * 0.5
    base = lambda l: ray(l) + ir(l) + uv(l)
    pk = 1.10 - base(1.383)
    tot = lambda l: base(l) + pk * math.exp(-((l - 1.383) / 0.018) ** 2)
    p = Plot(0.8, 1.7, 0, 2.5, L=50, T=22, Wd=430, H=230)
    s = defs()
    for c0, c1 in ((0.82, 0.88), (1.28, 1.34), (1.53, 1.565)):
        s += rect(p.X(c0), p.T, p.X(c1) - p.X(c0), p.H, MINT, 'none', 0, 6)
    s += sax(p, xt=(0.85, 1.0, 1.31, 1.55), yt=(0, 0.5, 1, 1.5, 2, 2.5), xl='wavelength (µm) →', yl='loss (dB/km)', fmt=lambda v: f'{v:g}')
    s += p.curve(ray, 0.8, 1.7, n=120, c=MUT, w=2.5, dash='6 6')
    s += p.curve(tot, 0.8, 1.7, n=500, c=B, w=4.5)
    s += dot(*p.P(1.383, tot(1.383)), 10, O) + tag(p.X(1.383) - 12, p.Y(1.10) - 14, f'OH peak 1383 nm: {1.10:.2f}', O, 13, 'end')
    s += tag(p.X(1.55), p.Y(0.55), 'lowest ≈ 0.19', G, 13)
    s += txt(p.X(0.9), p.Y(2.05), 'Rayleigh 1/λ⁴', 13, MUT, 800, 'start')
    s += txt(p.L, p.T + p.H + 62, 'shaded: the 850, 1310 and 1550 nm windows', 13, MUT, 800, 'start')
    return 'Loss against wavelength', s
D['ec-optical-u2-L1'] = (u2L1, 'water peak: 1383 nm', '2.2.1')


def u2L2():
    # loss per turn = 8 exp(-R / (5/3 mm)): 0.398 dB at 5 mm, 0.0198 at 10, 0.001 at 15; four turns at 5 mm: 1.59 dB
    C, Rc = 0.398 * math.exp(3), 5 / 3
    lt = lambda r: C * math.exp(-r / Rc)
    p = Plot(4, 16, -3.2, 0.5, L=60, T=22, Wd=420, H=200)
    s = defs()
    for e in (-3, -2, -1, 0):
        s += line(p.L, p.Y(e), p.L + p.W, p.Y(e), GRID, 1.5) + txt(p.L - 10, p.Y(e) + 5, f'{10 ** e:g}', 13, MUT, 700, 'end')
    s += line(p.L, p.T + p.H, p.L + p.W + 8, p.T + p.H, MUT, 2.5, arrow=True) + line(p.L, p.T + p.H, p.L, p.T - 6, MUT, 2.5, arrow=True)
    for r in (5, 10, 15):
        s += txt(p.X(r), p.T + p.H + 20, g(r), 13, MUT, 700)
    s += txt(p.L + p.W, p.T + p.H + 40, 'bend radius (mm) →', 13, MUT, 700, 'end') + txt(p.L + 8, p.T - 8, 'dB per turn (log)', 13, MUT, 700, 'start')
    s += p.curve(lambda r: math.log10(lt(r)), 4, 16, n=60, c=B, w=5)
    for r, c in ((5, O), (10, G), (15, G)):
        s += dot(*p.P(r, math.log10(lt(r))), 9, c)
    s += tag(p.X(5) + 14, p.Y(math.log10(lt(5))) - 4, f'{lt(5):.3f} dB', O, 13, 'start')
    s += tag(p.X(10) + 14, p.Y(math.log10(lt(10))) - 4, f'{lt(10):.4f}', G, 13, 'start')
    s += tag(p.X(15) - 6, p.Y(math.log10(lt(15))) - 18, f'{lt(15):.3f}', G, 12, 'end')
    y = 300; w = 70
    for i in range(4):
        s += rect(60 + i * w, y, w - 4, 40, O, W, 2, 8) + txt(60 + i * w + (w - 4) / 2, y + 26, f'{lt(5):.3f}', 13, W, 900)
    s += txt(60 + 4 * w + 10, y + 27, f'= {4 * lt(5):.2f} dB', 18, INK, 900, 'start')
    return 'Each tight turn costs', s
D['ec-optical-u2-L2'] = (u2L2, '4 × 0.398 = 1.59 dB', '2.4.1')


def u2L3():
    # material D (zero near 1270 nm, 21 at 1550) + waveguide D (-2.88 at 1310, -3.5 at 1550): total 0 at 1310, 17.5 at 1550
    S0 = 21 / ((1550 - 1270 ** 4 / 1550 ** 3) / 4)
    Dm = lambda l: S0 / 4 * (l - 1270 ** 4 / l ** 3)
    w1, w2 = -Dm(1310), -3.5
    Dw = lambda l: w1 + (w2 - w1) * (l - 1310) / (1550 - 1310)
    Dt = lambda l: Dm(l) + Dw(l)
    p = Plot(1200, 1650, -10, 25, L=50, T=22, Wd=430, H=240)
    s = defs() + sax(p, xt=(1310, 1550), yt=(-5, 0, 5, 10, 15, 20, 25), xl='wavelength (nm) →', yl='D ps/(nm·km)')
    s += p.curve(Dm, 1200, 1650, n=100, c=G, w=3.5, dash='8 6') + p.curve(Dw, 1200, 1650, n=10, c=O, w=3.5, dash='3 6')
    s += p.curve(Dt, 1200, 1650, n=100, c=B, w=5)
    s += dot(*p.P(1550, Dm(1550)), 8, G) + tag(p.X(1550) - 12, p.Y(Dm(1550)) - 12, f'material {Dm(1550):.0f}', G, 12, 'end')
    s += dot(*p.P(1550, Dt(1550)), 10, B) + tag(p.X(1550) + 12, p.Y(Dt(1550)) + 30, f'total {Dt(1550):.1f}', B, 13, 'start')
    s += dot(*p.P(1550, w2), 8, O) + tag(p.X(1550) - 12, p.Y(w2) + 28, f'waveguide {g(w2)}', O, 12, 'end')
    s += dot(*p.P(1310, 0), 9, B) + tag(p.X(1310) - 8, p.Y(0) - 14, 'zero at 1310', B, 12, 'end')
    return 'Add D with its sign', s
D['ec-optical-u2-L3'] = (u2L3, '21 − 3.5 = 17.5', '2.6.1')


def u2L4():
    # 100 km SMF at D = +17 -> +1700 ps/nm; DCF at -85: 20 km brings it to 0; 15 km leaves +425
    Ds, Ls, Dd = 17, 100, -85
    acc = Ds * Ls
    Ld = acc / -Dd
    left = acc + Dd * 15
    p = Plot(0, 125, -100, 1900, L=60, T=24, Wd=420, H=230)
    s = defs() + sax(p, xt=(0, 50, 100, 120), yt=(0, 425, 1000, 1700), xl='distance (km) →', yl='ps/nm', xfmt=lambda v: g(v))
    s += rect(p.X(Ls), p.T, p.X(Ls + Ld) - p.X(Ls), p.H, OS, 'none', 0, 6)
    s += poly([p.P(0, 0), p.P(Ls, acc), p.P(Ls + Ld, 0)], B, 5)
    s += dot(*p.P(Ls + Ld, 0), 10, G) + tag(p.X(Ls + Ld) - 14, p.Y(0) - 14, 'back to 0', G, 12, 'end')
    s += dot(*p.P(Ls + 15, left), 8, O) + tag(p.X(Ls + 15) - 14, p.Y(left) + 4, f'15 km: +{left:g} left', O, 12, 'end')
    s += tag(p.X(Ls) - 8, p.Y(acc) - 16, f'+{acc:g} after {Ls} km', B, 13, 'end')
    s += txt(p.X(50), p.Y(400), f'fiber D = +{Ds}', 14, B, 900) + txt(p.X(Ls + Ld / 2), p.T + 18, 'DCF', 14, O, 900)
    s += txt(p.L, p.T + p.H + 62, f'DCF length = {acc:g} / {-Dd} = {Ld:g} km', 14, INK, 900, 'start')
    return 'Climb, then cancel', s
D['ec-optical-u2-L4'] = (u2L4, '20 km × −85 = −1700', '2.8.1')


# ---------------- unit 3 ----------------
def u3L1():
    # 1.46 eV photon at 300 K: N2/N1 = exp(-hf/kT) = 2.84e-25; net gain needs pumping into inversion
    hf = 2.340e-19; kT = 1.38e-23 * 300
    r = math.exp(-hf / kT)
    s = defs()
    for i, (cx, head, n1, n2, c) in enumerate(((130, 'in equilibrium', 12, 0, O), (390, 'pumped', 3, 9, G))):
        xL = cx - 100
        s += txt(cx, 28, head, 17, c, 900)
        s += line(xL, 80, xL + 200, 80, INK, 4) + line(xL, 250, xL + 200, 250, INK, 4)
        s += txt(xL - 6, 85, 'E₂', 15, INK, 900, 'end') + txt(xL - 6, 255, 'E₁', 15, INK, 900, 'end')
        for k in range(n2):
            s += dot(xL + 20 + k * 20, 66, 8, B)
        for k in range(n1):
            s += dot(xL + 12 + (k % 12) * 16, 236 - (k // 12) * 18, 7, B)
    s += line(115, 240, 115, 98, O, 4, arrow=True) + txt(125, 175, 'absorbs', 13, O, 900, 'start')
    s += line(375, 98, 375, 236, G, 4, arrow=True) + line(395, 98, 395, 236, G, 4, arrow=True) + txt(405, 175, 'two photons', 13, G, 900, 'start')
    s += line(260, 60, 260, 270, GRID, 2, '6 6')
    s += rtxt(130, 300, 'N₂/N₁ = e^{−hf/kT}', 15, INK, 900)
    s += rtxt(130, 326, f'= {sci(r)}', 15, O, 900)
    s += txt(390, 300, 'N₂ > N₁:', 15, INK, 900) + txt(390, 326, 'stimulated wins', 15, G, 900)
    s += txt(260, 362, f'{1.46} eV photon at 300 K', 12, MUT, 800)
    return 'Light alone cannot invert', s
D['ec-optical-u3-L1'] = (u3L1, 'absorption wins: pump it', '3.1.1')


def u3L2():
    # L = 300 um, R1 R2 = 0.1024, alpha_i = 10 /cm, Gamma = 0.30
    L = 0.03; RR = 0.1024; ai = 10; Gm = 0.30
    am = math.log(1 / RR) / (2 * L)
    gmod = am + ai; gmat = gmod / Gm
    s = defs()
    # cavity with mode and active layer
    x0, x1, yc = 40, 480, 90
    s += rect(x0, yc - 46, x1 - x0, 92, CLAD, '#C8D3E2', 2, 6)
    s += rect(x0, yc - 14, x1 - x0, 28, OS, O, 2, 0) + txt(x0 + 12, yc + 6, 'active layer', 13, O, 900, 'start')
    s += rect(x0 - 10, yc - 54, 10, 108, B, 'none', 0, 2) + rect(x1, yc - 54, 10, 108, B, 'none', 0, 2)
    pts = [(x1 - 70 + 36 * math.exp(-((y - yc) / 22) ** 2), y) for y in range(int(yc - 44), int(yc + 45), 2)]
    s += poly(pts, G, 3.5)
    s += txt(x1 - 74, yc - 22, f'Γ = {Gm:.2f}', 14, G, 900, 'end')
    s += arrow2(x0, yc + 64, x1, yc + 64, MUT, 2) + txt((x0 + x1) / 2, yc + 84, f'L = 300 µm, R₁R₂ = {RR}', 13, MUT, 800)
    # bars
    X = lambda v: 110 + v / 165 * 390
    y = 210
    s += txt(100, y + 24, 'modal', 15, INK, 900, 'end')
    s += rect(110, y, X(am) - 110, 36, B, W, 2, 6) + rect(X(am), y, X(gmod) - X(am), 36, G, W, 2, 6)
    s += txt(X(gmod) + 10, y + 24, f'{am:.2f} + {ai} = {gmod:.2f}', 15, INK, 900, 'start')
    y = 270
    s += txt(100, y + 24, 'material', 15, INK, 900, 'end')
    s += rect(110, y, X(gmat) - 110, 36, O, W, 2, 6) + txt((110 + X(gmat)) / 2, y + 24, f'{gmod:.2f} / {Gm:.2f} = {gmat:.2f}', 15, W, 900)
    s += txt(110, 340, 'gain per cm: mirrors (blue) + internal loss (green)', 12, MUT, 800, 'start')
    return 'The gain the laser must reach', s
D['ec-optical-u3-L2'] = (u3L2, 'g = 47.98 / 0.30', '3.3.1')


def u3L3():
    # LED radius 100 um onto a core of radius 50 um, NA 0.2: (50/100)^2 x 0.2^2 = 1 % of 2 mW = 20 uW
    rL, rc, NA, P = 100, 50, 0.2, 2.0
    fa, fc = (rc / rL) ** 2, NA ** 2
    s = defs()
    cx, cy, k = 140, 170, 1.15
    s += f'<circle cx="{cx}" cy="{cy}" r="{rL * k}" fill="{OS}" stroke="{O}" stroke-width="3"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="{rc * k}" fill="{CORE}" stroke="{B}" stroke-width="3"/>'
    s += txt(cx, cy - rL * k + 26, f'LED r = {rL} µm', 13, O, 900) + txt(cx, cy + 5, f'core {rc} µm', 13, B, 900)
    s += txt(cx, 320, f'area: ({rc}/{rL})² = {fa:g}', 15, INK, 900)
    # side view: LED sprays, the core keeps an 11.5 deg cone
    th = deg(math.asin(NA))
    x0, y0 = 300, 170
    for a in range(-80, 81, 20):
        s += line(x0, y0, x0 + 90 * math.cos(math.radians(a)), y0 - 90 * math.sin(math.radians(a)), '#F7B9A6', 3)
    dy = 180 * math.tan(math.radians(th))
    s += poly([(x0, y0), (x0 + 180, y0 - dy), (x0 + 180, y0 + dy)], G, 3.5, fill=GS, close=True)
    s += rect(x0 - 10, y0 - 40, 10, 80, O, 'none', 0, 2)
    s += txt(x0 + 120, y0 - dy - 14, f'{th:.1f}° cone', 13, G, 900)
    s += txt(x0 + 100, 320, f'cone: {NA}² = {fc:g}', 15, INK, 900)
    s += tag(260, 360, f'{fa * fc * 100:g} % of {P:g} mW = {fa * fc * P * 1000:g} µW', B, 15)
    return 'A sprinkler aimed at a straw', s
D['ec-optical-u3-L3'] = (u3L3, '0.25 × 0.04 = 1 %', '3.6.1')


def u3L4():
    # offset 10 um on a 100 um core: eta = 0.873, 0.59 dB; gel cuts the Fresnel 0.33 dB, not the offset
    a, d = 50, 10
    x = d / (2 * a)
    eta = 2 / math.pi * (math.acos(x) - x * math.sqrt(1 - x * x))
    Lo = -10 * math.log10(eta)
    s = defs()
    cx, cy, k = 140, 160, 1.9
    s += f'<circle cx="{cx}" cy="{cy}" r="{a * k}" fill="{BS}" fill-opacity=".8" stroke="{B}" stroke-width="3"/>'
    s += f'<circle cx="{cx + d * k}" cy="{cy}" r="{a * k}" fill="{OS}" fill-opacity=".6" stroke="{O}" stroke-width="3" stroke-dasharray="7 5"/>'
    s += arrow2(cx, cy + a * k + 16, cx + d * k, cy + a * k + 16, INK, 2.5) + txt(cx + d * k / 2, cy + a * k + 40, f'{d} µm', 14, INK, 900)
    s += txt(cx + d * k / 2, cy + 6, f'η = {eta:.3f}', 17, INK, 900)
    s += txt(cx + 6, 34, f'core {2 * a} µm, offset {d} µm', 13, MUT, 800)
    X0 = 300
    s += txt(X0, 70, 'gel removes', 15, G, 900, 'start')
    s += rect(X0, 82, 0.33 * 250, 34, GS, G, 2.5, 8, '6 5') + txt(X0 + 0.33 * 250 + 8, 105, 'Fresnel 0.33 dB', 13, G, 900, 'start')
    s += txt(X0, 170, 'gel cannot move cores', 15, O, 900, 'start')
    s += rect(X0, 182, Lo * 250, 34, O, W, 2, 8) + txt(X0 + Lo * 125, 205, f'offset {Lo:.2f} dB', 13, W, 900)
    s += txt(X0, 260, f'≈ {(1 - eta) * 100:.0f} % of the light', 14, INK, 900, 'start') + txt(X0, 282, 'still lost', 14, INK, 900, 'start')
    return 'Gel cannot fix an offset', s
D['ec-optical-u3-L4'] = (u3L4, 'offset stays: 0.59 dB', '3.7.1')


# ---------------- unit 4 ----------------
def u4L1():
    # R = eta lambda / 1.24: silicon eta 0.8 to 1.11 um, InGaAs eta 0.72 to 1.65 um; 1.55 -> 0.90 A/W; 1.70 -> 0 (not 0.99)
    Rf = lambda eta, l: eta * l / 1.24
    p = Plot(0.4, 1.9, 0, 1.4, L=50, T=24, Wd=430, H=230)
    s = defs() + sax(p, xt=(0.5, 1.0, 1.11, 1.65), yt=(0, 0.5, 1.0), xl='wavelength (µm) →', yl='R (A/W)', fmt=lambda v: f'{v:g}')
    s += p.curve(lambda l: Rf(1, l), 0.4, 1.74, n=4, c=MUT, w=2.5, dash='7 6') + tag(p.X(1.62), p.Y(Rf(1, 1.62)) - 10, 'η = 1', MUT, 12, 'end')
    s += poly([p.P(0.45, Rf(0.8, 0.45)), p.P(1.11, Rf(0.8, 1.11)), p.P(1.11, 0)], G, 4.5) + txt(p.X(0.8), p.Y(Rf(0.8, 0.8)) + 24, 'Si', 15, G, 900)
    s += poly([p.P(0.9, Rf(0.72, 0.9)), p.P(1.65, Rf(0.72, 1.65)), p.P(1.65, 0), p.P(1.85, 0)], B, 5) + txt(p.X(1.38), p.Y(Rf(0.72, 1.38)) + 26, 'InGaAs', 15, B, 900)
    s += dot(*p.P(1.55, Rf(0.72, 1.55)), 9, B) + tag(p.X(1.55) - 12, p.Y(0.9) - 12, f'1.55 µm: {Rf(0.72, 1.55):.2f}', B, 12, 'end')
    s += dot(*p.P(1.70, 0), 11, O) + tag(p.X(1.70), p.Y(0) - 22, '1.70 µm: 0', O, 13)
    s += cross(p.X(1.70), p.Y(Rf(0.72, 1.70)), O, 9, 4) + txt(p.X(1.70) + 14, p.Y(Rf(0.72, 1.70)) + 5, f'not {Rf(0.72, 1.70):.2f}', 12, O, 800, 'start')
    return 'Responsivity falls off a cliff', s
D['ec-optical-u4-L1'] = (u4L1, 'R = 0 past 1.65 µm', '4.1.1')


def u4L2():
    # F = kM + (1 - k)(2 - 1/M): k = 1 gives F = M; k = 0.3, M = 10 -> 4.33; k = 0.02, M = 100 -> 3.95
    Ff = lambda k, M: k * M + (1 - k) * (2 - 1 / M)
    lg = math.log10
    p = Plot(0, 2, 0, 2, L=50, T=24, Wd=430, H=230)
    s = defs()
    for e in (0, 1, 2):
        s += line(p.L, p.Y(e), p.L + p.W, p.Y(e), GRID, 1.5) + txt(p.L - 10, p.Y(e) + 5, g(10 ** e), 13, MUT, 700, 'end')
        s += txt(p.X(e), p.T + p.H + 20, g(10 ** e), 13, MUT, 700)
    s += line(p.L, p.T + p.H, p.L + p.W + 8, p.T + p.H, MUT, 2.5, arrow=True) + line(p.L, p.T + p.H, p.L, p.T - 6, MUT, 2.5, arrow=True)
    s += txt(p.L + p.W, p.T + p.H + 40, 'gain M (log) →', 13, MUT, 700, 'end') + txt(p.L + 8, p.T - 8, 'excess noise F', 13, MUT, 700, 'start')
    for k, c, lab, xl in ((1, O, 'k = 1: F = M', 1.55), (0.3, B, f'k = 0.3: {Ff(0.3, 10):.2f} at M = 10', 1.75), (0.02, G, f'k = 0.02: {Ff(0.02, 100):.2f} at M = 100', 1.96)):
        s += p.curve(lambda u, k=k: lg(Ff(k, 10 ** u)), 0, 2, n=80, c=c, w=4.5 if k != 1 else 3.5, dash=None if k != 1 else '8 6')
        yl_ = {1: 1.86, 0.3: 1.66, 0.02: 1.46}[k]
        s += line(p.X(0.08), p.Y(yl_), p.X(0.22), p.Y(yl_), c, 5) + txt(p.X(0.27), p.Y(yl_) + 5, lab, 13, c, 900, 'start')
    s += dot(*p.P(1, lg(Ff(0.3, 10))), 9, B) + dot(*p.P(2, lg(Ff(0.02, 100))), 10, G)
    return 'Excess noise depends on k', s
D['ec-optical-u4-L2'] = (u4L2, 'F = M only when k = 1', '4.3.1')


def u4L3():
    # PIN R = 0.9 A/W, preamp noise 40 nA, Q = 6: average current 240 nA -> 267 nW = -35.7 dBm; the 1 level is 480 nA
    Rr, sg, Q = 0.9, 40e-9, 6
    Iav = Q * sg; P = Iav / Rr; I1 = 2 * Iav
    dbm = 10 * math.log10(P / 1e-3)
    bits = [1, 0, 1, 1, 0, 0, 1, 0]
    import random
    rnd = random.Random(7)
    p = Plot(0, 8, -80, 600, L=60, T=24, Wd=420, H=220)
    s = defs() + sax(p, yt=(0, 240, 480), yl='photocurrent (nA)')
    pts = []
    for i, b in enumerate(bits):
        for k in range(13):
            pts.append(p.P(i + k / 12, (I1 if b else 0) * 1e9 + rnd.gauss(0, 30)))
    s += poly(pts, B, 3)
    s += line(p.L, p.Y(240), p.L + p.W, p.Y(240), O, 3, '9 6')
    s += tag(p.X(7.9), p.Y(240) + 30, f'average {Iav * 1e9:.0f} nA = {P * 1e9:.0f} nW', O, 13, 'end')
    s += tag(p.X(2.5), p.Y(I1 * 1e9) - 24, f'a 1: {I1 * 1e9:.0f} nA', B, 13)
    for i, b in enumerate(bits):
        s += txt(p.X(i + 0.5), p.T + p.H + 22, str(b), 14, INK if b else MUT, 900)
    s += txt(p.L, p.T + p.H + 62, f'sensitivity = average power = {dbm:.1f} dBm', 14, INK, 900, 'start')
    return 'Average power, not the 1', s
D['ec-optical-u4-L3'] = (u4L3, 'Q = 6: −35.7 dBm', '4.5.1')


# ---------------- unit 5 ----------------
def u5L1():
    # 60 km of 10 km reels: 6 reels x 2.2 dB, 5 splices x 0.1, 2 connectors x 0.5; 0 dBm in -> -14.7; sensitivity -28, margin 6
    reels, rl, sp, cn = 6, 2.2, 0.1, 0.5
    pts = []; Pw = 0.0
    pts.append((0, Pw)); Pw -= cn; pts.append((0, Pw))
    splices = []
    for i in range(reels):
        Pw -= rl; pts.append(((i + 1) * 10, Pw))
        if i < reels - 1:
            Pw -= sp; pts.append(((i + 1) * 10, Pw)); splices.append(((i + 1) * 10, Pw))
    Pw -= cn; pts.append((60, Pw))
    sens, marg = -28, 6
    p = Plot(0, 64, -30, 2, L=60, T=20, Wd=420, H=240)
    s = defs() + sax(p, xt=(0, 10, 20, 30, 40, 50, 60), yt=(0, -14.7, -20, -28), xl='distance (km) →', yl='dBm', fmt=lambda v: g(v))
    s += rect(p.X(0), p.Y(sens + marg), p.X(64) - p.X(0), p.Y(sens) - p.Y(sens + marg), OS, 'none', 0, 4)
    s += line(p.L, p.Y(sens), p.L + p.W, p.Y(sens), O, 3) + txt(p.X(1), p.Y(sens) - 8, f'sensitivity {sens}, margin {marg} dB above', 12, O, 900, 'start')
    s += poly([p.P(x, y) for x, y in pts], B, 4.5)
    for x, y in splices:
        s += dot(*p.P(x, y), 8, G)
    s += dot(*p.P(60, Pw), 10, B) + tag(p.X(60) - 10, p.Y(Pw) + 34, f'{Pw:.1f} dBm arrives', B, 13, 'end')
    s += txt(p.X(62), p.Y(-3.5), f'{reels} reels, {len(splices)} splices (green),', 13, INK, 900, 'end') + txt(p.X(62), p.Y(-3.5) + 18, '2 connectors', 13, INK, 900, 'end')
    s += txt(p.L, p.T + p.H + 62, f'spare: {Pw - sens:.1f} − {marg} = {Pw - sens - marg:.1f} dB', 14, INK, 900, 'start')
    return 'Six reels, five splices', s
D['ec-optical-u5-L1'] = (u5L1, '6 reels → 5 splices', '5.2.1')


def u5L2():
    # LED link: tx 12, modal 2.71, chromatic 18.0, receiver 11.67 ns; straight sum 44.4 fails, root-sum-square 24.7 passes 35 ns
    terms = [('tx', 12.0, O), ('modal', 2.71, G), ('chromatic', 18.0, B), ('rx', 11.67, '#9B7BEA')]
    lin = sum(t[1] for t in terms)
    rss = math.sqrt(sum(t[1] ** 2 for t in terms))
    lim = 0.7 * 50
    X = lambda v: 130 + v / 48 * 360
    s = defs()
    s += line(X(lim), 30, X(lim), 300, O, 3, '8 6') + tag(X(lim), 28, f'limit {lim:g} ns', O, 13)
    y = 80
    s += txt(120, y + 26, 'added', 15, INK, 900, 'end')
    x = X(0)
    for n, v, c in terms:
        w = X(v) - X(0)
        s += rect(x, y, w, 40, c, W, 2, 6)
        if w > 40: s += txt(x + w / 2, y + 26, f'{v:g}', 13, W, 900)
        x += w
    s += cross(X(lin) + 18, y + 20, O, 9, 4)
    s += txt(X(0), y + 66, f'straight sum {lin:.1f} ns: wrong', 14, O, 900, 'start')
    y = 200
    s += txt(120, y + 26, 'in quadrature', 15, INK, 900, 'end')
    s += rect(X(0), y, X(rss) - X(0), 40, B, W, 2, 6) + txt((X(0) + X(rss)) / 2, y + 26, f'√Σt² = {rss:.1f}', 14, W, 900)
    s += txt(X(rss) + 10, y + 26, 'passes', 14, G, 900, 'start')
    for v in (0, 10, 20, 30, 40):
        s += txt(X(v), 330, g(v), 13, MUT, 700)
    s += txt(490, 354, 'rise time (ns) →', 13, MUT, 700, 'end')
    s += txt(130, 290, 'tx 12, modal 2.71, chromatic 18.0, rx 11.67', 12, MUT, 800, 'start')
    return 'Rise times add in squares', s
D['ec-optical-u5-L2'] = (u5L2, '√(Σt²) = 24.7 ns', '5.3.1')


# ---------------- unit 6 ----------------
def u6L1():
    # 40 channels at 100 GHz in the C band: 39 gaps = 3.9 THz (31.23 nm); spacing 0.8 nm at 1550
    N, df = 40, 100e9
    c = 2.998e8
    width = (N - 1) * df
    lam = 1550e-9
    dl = lam ** 2 * df / c
    f1, f2 = c / 1565e-9, c / 1530e-9
    p = Plot(f1 / 1e12 - 0.15, f2 / 1e12 + 0.15, 0, 1.3, L=30, T=40, Wd=460, H=170)
    s = defs()
    s += rect(p.X(f1 / 1e12), p.T, p.X(f2 / 1e12) - p.X(f1 / 1e12), p.H, MINT, 'none', 0, 8)
    s += line(p.L, p.Y(0), p.L + p.W + 6, p.Y(0), MUT, 2.5, arrow=True)
    start = (f1 + f2) / 2 / 1e12 - width / 2e12
    for i in range(N):
        x = p.X(start + i * df / 1e12)
        s += line(x, p.Y(0), x, p.Y(1), B if i not in (0, N - 1) else O, 4)
    s += txt(p.X(start), p.Y(1) - 10, 'λ1', 14, O, 900) + txt(p.X(start + width / 1e12), p.Y(1) - 10, 'λ40', 14, O, 900)
    yA = p.Y(1.2)
    s += arrow2(p.X(start), p.T - 18, p.X(start + width / 1e12), p.T - 18, INK, 2.5)
    s += tag((p.X(start) + p.X(start + width / 1e12)) / 2, p.T - 24, f'{N - 1} gaps = {width / 1e12:g} THz', INK, 14)
    s += txt(p.X(f1 / 1e12), p.Y(0) + 22, '1565 nm', 12, MUT, 700) + txt(p.X(f2 / 1e12), p.Y(0) + 22, '1530 nm', 12, MUT, 700)
    s += txt(p.X((f1 + f2) / 2e12), p.Y(0) + 22, 'C band', 13, G, 900)
    y = 290
    s += box(10, y, 230, 64, f'{df / 1e9:g} GHz = {dl * 1e9:.2f} nm', B, 17, sub='each gap at 1550 nm', subc=MUT)
    s += box(260, y, 240, 64, f'{N} × 10 Gb/s = {N * 10} Gb/s', G, 17, sub='one fiber', subc=MUT, fill=GS)
    return 'Forty colours, one fiber', s
D['ec-optical-u6-L1'] = (u6L1, '39 × 100 GHz = 3.9 THz', '6.1.1')


def u6L2():
    # erbium levels: 980 pump to level 3, fast drop to level 2 (10 ms), signal at 1550; PCE ceiling 980/1550 = 63.2 %; measured (25 - 0.5)/60 = 40.8 %
    lp, ls = 980, 1550
    ceil = lp / ls
    pce = (25 - 0.5) / 60
    s = defs()
    yl = {1: 310, 2: 160, 3: 60}
    for k, y in yl.items():
        s += line(30, y, 240, y, INK, 4) + txt(240, y - 8 if k != 1 else y + 22, f'level {k}', 13, INK, 900, 'end')
    s += line(70, yl[1] - 4, 70, yl[3] + 6, O, 5, arrow=True) + txt(60, 200, f'{lp} pump', 13, O, 900, 'end')
    s += f'<path d="M90,{yl[3] + 6} C110,{yl[3] + 40} 120,{yl[2] - 40} 130,{yl[2] - 6}" fill="none" stroke="{MUT}" stroke-width="3" stroke-dasharray="5 5" marker-end="url(#am)"/>'
    s += txt(140, 110, 'fast', 12, MUT, 800, 'start')
    s += line(190, yl[2] + 6, 190, yl[1] - 4, B, 5, arrow=True) + line(214, yl[2] + 6, 214, yl[1] - 4, B, 5, arrow=True)
    s += txt(226, 248, f'{ls} signal', 13, B, 900, 'start')
    X = lambda v: 340 + v * 160
    for i, (n, v, c) in enumerate((('ceiling', ceil, G), ('this EDFA', pce, B))):
        y = 90 + i * 90
        s += txt(340, y - 10, n, 14, c, 900, 'start')
        s += rect(340, y, 160, 34, '#EEF1F6', 'none', 0, 8) + rect(340, y, X(v) - 340, 34, c, 'none', 0, 8)
        s += txt(X(v) - 8, y + 23, f'{v * 100:.1f} %', 14, W, 900, 'end')
    s += txt(420, 290, f'{lp}/{ls}', 18, INK, 900) + txt(420, 316, 'one pump photon,', 13, MUT, 800) + txt(420, 336, 'one signal photon', 13, MUT, 800)
    return 'Why pump power is not all signal', s
D['ec-optical-u6-L2'] = (u6L2, 'at most 63.2 %', '6.3.1')


def u6L3():
    # STM-1: 3 TUG-3 x 7 TUG-2 x 3 TU-12 = 63 E1; dividing 155.52 / 2.048 = 75.9 is wrong
    n3, n7, n1 = 3, 7, 3
    tot = n3 * n7 * n1
    s = defs()
    s += box(10, 10, 500, 46, 'STM-1: 155.52 Mb/s', B, 18, fill=BS)
    cols = [G, O, '#9B7BEA']
    for i in range(n3):
        x0 = 10 + i * 168
        s += rect(x0, 70, 160, 250, '#F4F7FB', cols[i], 2.5, 10) + txt(x0 + 80, 92, 'TUG-3', 14, cols[i], 900)
        for j in range(n7):
            y = 104 + j * 30
            s += rect(x0 + 10, y, 140, 24, W, GRID, 2, 6) + txt(x0 + 30, y + 17, 'TUG-2', 11, MUT, 800)
            for k in range(n1):
                s += rect(x0 + 66 + k * 27, y + 4, 22, 16, cols[i], 'none', 0, 4)
    s += txt(260, 350, f'{n3} × {n7} × {n1} = {tot} E1', 22, INK, 900)
    s += txt(500, 372, f'not 155.52 / 2.048 = {155.52 / 2.048:.1f}', 13, O, 900, 'end')
    return 'E1s packed three, seven, three', s
D['ec-optical-u6-L3'] = (u6L3, '3 × 7 × 3 = 63 E1', '6.6.1')


def u6L4():
    # AAL5: 90 data bytes + 8-byte trailer = 98 -> 3 cells of 48; pad 46; 3 x 53 = 159 bytes on the line
    data, tr, pl, hd = 90, 8, 48, 5
    cells = math.ceil((data + tr) / pl)
    pad = cells * pl - data - tr
    s = defs()
    X = lambda b: 20 + b * 5.8
    segs = []
    left = data
    for c in range(cells):
        y = 60 + c * 80
        s += rect(X(0), y, X(hd) - X(0), 50, INK, 'none', 0, 6) + txt((X(0) + X(hd)) / 2, y + 31, 'H', 14, W, 900)
        b = hd; room = pl
        dpart = min(left, room); left -= dpart
        if dpart:
            s += rect(X(b), y, dpart * 5.8, 50, BS, B, 2, 6) + txt(X(b) + dpart * 2.9, y + 31, f'data {dpart}', 14, B, 900)
            b += dpart; room -= dpart
        if c == cells - 1:
            pd = room - tr
            s += rect(X(b), y, pd * 5.8, 50, '#EEF1F6', MUT, 2, 6, '5 5') + txt(X(b) + pd * 2.9, y + 31, f'pad {pd}', 14, MUT, 900)
            b += pd
            s += rect(X(b), y, tr * 5.8, 50, OS, O, 2.5, 6) + txt(X(b) + tr * 2.9, y - 8, 'trailer 8', 13, O, 900)
        elif room:
            s += rect(X(b), y, room * 5.8, 50, '#EEF1F6', MUT, 2, 6, '5 5') + txt(X(b) + room * 2.9, y - 8, f'pad {room}', 13, MUT, 900)
        s += txt(X(hd + pl) + 8, y + 31, f'{c + 1}', 15, MUT, 900, 'start')
    s += txt(20, 30, f'{data} bytes + {tr} trailer = {data + tr} > {2 * pl}', 15, INK, 900, 'start')
    s += txt(20, 360, f'{cells} cells × 53 = {cells * 53} bytes, pad {pad}', 14, INK, 900, 'start')
    return 'Trailer first, then count cells', s
D['ec-optical-u6-L4'] = (u6L4, '98 bytes → 3 cells', '6.8.1')
