# Glass t16 drawings for Engineering Thermodynamics (me-thermo), one per lesson.
# D[key] = (fn, chip, book figure). Every value is computed here from the lesson's worked example.
from gfx import *
import math
ln = math.log
D = {}
OF = '#FFF6E0'   # warm fill for heat areas

def f1(v): return f'{v:.1f}'
def f2(v): return f'{v:.2f}'
def f3(v): return f'{v:.3f}'
def f4(v): return f'{v:.4f}'

def shade(pts, fill, op=1):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" fill-opacity="{op}" stroke="none"/>'

def arr(x1, y1, x2, y2, c, w=5):
    return line(x1, y1, x2, y2, c, w, arrow=True)

def lbl(x, y, s, c, size=14, anchor='middle'):
    return txt(x, y, s, size, c, 900, anchor)

# ------------------------------------------------------------------ unit 1


def u1L3():
    E_ = 0.50 * 120                       # 60 kJ from the heater
    Wp, Ql = 25, 15
    Wa, Qa = Wp - E_, -Ql                  # (a) heater inside: W = -35, Q = -15
    Qb, Wb = E_ - Ql, Wp                   # (b) gas only: Q = +45, W = +25
    s = defs()
    for x0, head, inside in ((10, 'gas + heater inside', True), (265, 'gas only', False)):
        s += txt(x0 + 120, 12, head, 15, INK, 900)
        s += rect(x0 + 55, 70, 130, 150, GS, G, 2.5, 10)                      # cylinder
        s += rect(x0 + 50, 56, 140, 16, '#C9D3E6', INK, 2, 4)                  # piston
        s += txt(x0 + 120, 175, 'gas', 16, G, 900)
        s += f'<path d="M{x0 + 95},{205} l10,-14 l10,14 l10,-14 l10,14 l10,-14" fill="none" stroke="{O}" stroke-width="4" stroke-linejoin="round"/>'
        if inside: s += rect(x0 + 38, 44, 164, 190, 'none', B, 3, 14, '8 7')
        else: s += rect(x0 + 48, 80, 144, 104, 'none', B, 3, 14, '8 7')
        s += arr(x0 + 120, 54, x0 + 120, 34, INK, 4)
        s += lbl(x0 + 134, 42, f'W {Wp} out', INK, 14, 'start')
        s += arr(x0 + 196, 150, x0 + 240, 150, O, 4) + lbl(x0 + 206, 136, f'Q {Ql} out', O, 14, 'start')
        if inside:
            s += line(x0 + 8, 250, x0 + 105, 210, B, 4) + lbl(x0 + 6, 272, f'electric W {E_:.0f} in', B, 13, 'start')
        else:
            s += arr(x0 + 120, 232, x0 + 120, 190, O, 4) + lbl(x0 + 128, 252, f'Q {E_:.0f} in', O, 13, 'start')
    s += box(18, 290, 230, 52, f'Q = {Qa:+.0f}, W = {Wa:+.0f}', B, 16, fill=BS)
    s += box(273, 290, 230, 52, f'Q = {Qb:+.0f}, W = {Wb:+.0f}', O, 16, fill=OS)
    s += txt(260, 372, f'Q − W = {Qa - Wa:+.0f} kJ both ways', 16, INK, 900)
    return 'Same heater: heat or work?', s
D['me-thermo-u1-L3'] = (u1L3, 'heat out: Q < 0', '1.6.1')

# ------------------------------------------------------------------ unit 2

def u2L2():
    R, T1, p1, g, n = 0.287, 300, 100, 1.4, 1.3
    v1 = R * T1 / p1; v2 = v1 / 8
    pi, pn, pa = p1 * 8, p1 * 8 ** n, p1 * 8 ** g          # 800, 1493, 1838
    pl = Plot(0, 0.9, 0, 2000, L=62, T=24, Wd=420, H=280)
    s = defs() + pl.axes(xt=(0, 0.3, 0.6, 0.9), yt=(0, 500, 1000, 1500, 2000), xl='v (m³/kg) →', yl='p (kPa)', fmt=lambda v: f'{v:g}')
    for k, c in ((1.0, G), (n, B), (g, O)):
        s += pl.curve(lambda v, k=k: p1 * (v1 / v) ** k, v2, v1, c=c, w=5)
    s += dot(*pl.P(v1, p1), 10, INK)
    s += tag(pl.X(v1) - 4, pl.Y(p1) - 26, f'1: {v1:.3f}, {p1} kPa', INK, 13, 'end')
    Ta, Tn = T1 * 8 ** (g - 1), T1 * 8 ** (n - 1)            # 689.2, 559.8 K
    cv = 0.718
    Qa, Qn, Qi = 0.0, cv * (Tn - T1) + R * (T1 - Tn) / (n - 1), R * T1 * ln(1 / 8)   # 0, -62.0, -179.0
    for q, c, lab in ((pa, O, f'adiabatic: {Ta:.0f} K, Q = 0'), (pn, B, f'n = 1.3: {Tn:.0f} K, Q = {Qn:.1f}'), (pi, G, f'isothermal: {T1} K, Q = {Qi:.1f}')):
        s += dot(*pl.P(v2, q), 9, c) + tag(pl.X(v2) + 18, pl.Y(q) + 5, lab, c, 13, 'start')
    s += txt(pl.X(0.62), pl.Y(1250), 'to one-eighth: hotter,', 16, INK, 900) + txt(pl.X(0.62), pl.Y(1250) + 24, 'yet no heat goes in', 16, INK, 900)
    s += arr(pl.X(0.7), pl.Y(430), pl.X(0.45), pl.Y(430), MUT, 3)
    return 'Three squeezes of 1 kg of air', s
D['me-thermo-u2-L2'] = (u2L2, 'hotter, but Q ≤ 0', '2.4.1')

def u2L3():
    claims = [('a', 300, 500, 0), ('b', 200, 250, 0), ('c', 80, 60, 20)]
    pl = Plot(0, 3, 0, 550, L=56, T=34, Wd=440, H=250)
    s = defs() + pl.axes(yt=(0, 100, 200, 300, 400, 500), yl='kW')
    for i, (nm, qin, w, rej) in enumerate(claims):
        cx = i + 0.5
        x1 = pl.X(cx) - 52; x2 = pl.X(cx) + 6
        s += rect(x1, pl.Y(qin), 46, pl.Y(0) - pl.Y(qin), O, 'none', 0, 6) + txt(x1 + 23, pl.Y(qin) - 8, qin, 13)
        s += rect(x2, pl.Y(w), 46, pl.Y(0) - pl.Y(w), B, 'none', 0, 6)
        top = w
        if rej:
            s += rect(x2, pl.Y(w + rej), 46, pl.Y(w) - pl.Y(w + rej), '#9DB0CF', 'none', 0, 6)
            top = w + rej
        s += txt(x2 + 23, pl.Y(top) - 8, f'{w}' + (f'+{rej}' if rej else ''), 13)
        s += txt(pl.X(cx), pl.Y(0) + 22, f'({nm})', 15, MUT, 900)
        made = w + rej - qin
        if made > 0: s += tag(pl.X(cx), pl.Y(0) + 56, f'{made} kW made', O, 13)
        else: s += tag(pl.X(cx), pl.Y(0) + 56, f'η = {w / qin * 100:.0f} %', G, 13)
    s += rect(250, 6, 14, 14, O, 'none', 0, 3) + txt(270, 18, 'heat in', 13, MUT, 800, 'start')
    s += rect(330, 6, 14, 14, B, 'none', 0, 3) + txt(350, 18, 'work out', 13, MUT, 800, 'start')
    s += rect(420, 6, 14, 14, '#9DB0CF', 'none', 0, 3) + txt(440, 18, 'rejected', 13, MUT, 800, 'start')
    return 'Three claimed engines', s
D['me-thermo-u2-L3'] = (u2L3, 'out > in: PMM-1', '2.5.1')

def u2L4():
    cp, cv, R, Ti, p2, V = 1.005, 0.718, 0.287, 300, 500, 0.2
    ui, fw = cv * Ti, R * Ti                 # 215.4, 86.1
    hi = ui + fw                             # 301.5
    T2 = hi / cv                             # 419.9
    m2 = p2 * V / (R * T2)                   # 0.830
    s = defs()
    s += rect(10, 120, 150, 34, '#C9D3E6', INK, 2, 6) + txt(85, 112, f'line: {p2} kPa, {Ti} K', 13, INK, 800)
    s += arr(30, 137, 140, 137, O, 5)
    s += rect(160, 128, 14, 18, INK, 'none', 0, 2)
    s += rect(174, 40, 150, 200, GS, G, 3, 26) + txt(249, 100, 'tank', 16, G, 900)
    s += txt(249, 140, f'T₂ = {T2:.0f} K', 22, INK, 900) + txt(249, 172, f'm₂ = {m2:.3f} kg', 16, INK, 800)
    s += txt(249, 210, 'rigid, insulated', 13, MUT, 800)
    H = 200 / 320
    x0 = 380; yb = 250
    s += rect(x0, yb - ui * H, 44, ui * H, G, 'none', 0, 6) + rect(x0, yb - hi * H, 44, fw * H, O, 'none', 0, 6)
    s += txt(x0 + 22, yb - ui * H / 2 + 5, f'{ui:.1f}', 13, W, 900) + txt(x0 + 22, yb - ui * H - fw * H / 2 + 5, f'{fw:.1f}', 13, W, 900)
    s += txt(x0 + 52, yb - ui * H / 2 + 5, 'u', 15, G, 900, 'start') + txt(x0 + 52, yb - ui * H - fw * H / 2 + 5, 'pv', 15, O, 900, 'start')
    s += txt(x0 + 22, yb - hi * H - 10, f'h = {hi:.1f}', 14, INK, 900)
    s += txt(x0 + 40, yb + 22, 'kJ per kg', 13, MUT, 800)
    s += box(30, 284, 460, 54, f'u₂ = h: flow work {fw:.1f} kJ/kg heats the tank', O, 15, fill=OS)
    return 'Filling an empty tank', s
D['me-thermo-u2-L4'] = (u2L4, 'T₂ = γT = 420 K', '2.7.1')

# ------------------------------------------------------------------ unit 3
def engine_block(cx, top, bot, Th, Tc, qh, w, qc, rev=False, name='E'):
    s = rect(cx - 90, top, 180, 40, OS, O, 2.5, 10) + txt(cx, top + 26, f'{Th} K', 16, O, 900)
    s += rect(cx - 90, bot, 180, 40, BS, B, 2.5, 10) + txt(cx, bot + 26, f'{Tc} K', 16, B, 900)
    my = (top + 40 + bot) / 2
    s += dot(cx, my, 30, W, INK, 3) + txt(cx, my + 7, name, 18, INK, 900)
    if not rev:
        s += arr(cx, top + 42, cx, my - 34, O, 5) + arr(cx, my + 32, cx, bot - 4, B, 5)
        s += arr(cx + 32, my, cx + 82, my, INK, 5)
    else:
        s += arr(cx, my - 32, cx, top + 46, O, 5) + arr(cx, bot - 2, cx, my + 34, B, 5)
        s += arr(cx + 82, my, cx + 34, my, INK, 5)
    s += lbl(cx - 16, (top + 40 + my - 30) / 2 + 5, f'{qh}', O, 15, 'end')
    s += lbl(cx - 16, (my + 30 + bot) / 2 + 5, f'{qc}', B, 15, 'end')
    s += lbl(cx + 60, my - 16, f'W {w}', INK, 14)
    return s

def u3L1():
    Q1, Q2 = 800, 500
    W_ = Q1 - Q2                              # 300
    eta = W_ / Q1                             # 0.375
    copr = Q2 / W_                            # 1.667
    s = defs()
    s += txt(120, 18, 'engine', 15, INK, 900) + txt(380, 18, 'refrigerator', 15, INK, 900)
    s += engine_block(120, 30, 230, 600, 300, Q1, W_, Q2, name='E')
    s += engine_block(380, 30, 230, 300, 270, Q1, W_, Q2, rev=True, name='R')
    s += box(30, 292, 190, 52, f'η = {W_}/{Q1} = {eta:.3f}', O, 15, fill=OS)
    s += box(290, 292, 200, 52, f'COP = {Q2}/{W_} = {copr:.3f}', B, 15, fill=BS)
    return 'Engine and its reverse, in kJ', s
D['me-thermo-u3-L1'] = (u3L1, 'η = W ÷ heat in', '3.1.1')

def u3L2():
    m, R, T = 0.5, 0.287, 300
    mRT = m * R * T                            # 43.05
    V1, V2 = 0.2, 0.4
    p1, p2 = mRT / V1 + 1e-9, mRT / V2         # 215.3, 107.6 (half up, as the lesson)
    W_ = mRT * ln(V2 / V1)                     # 29.84
    pl = Plot(0.15, 0.45, 0, 250, L=62, T=24, Wd=420, H=280)
    s = defs() + pl.axes(xt=(0.2, 0.3, 0.4), yt=(0, 50, 100, 150, 200, 250), xl='V (m³) →', yl='p (kPa)', fmt=lambda v: f'{v:g}')
    cur = [pl.P(V1 + (V2 - V1) * i / 60, mRT / (V1 + (V2 - V1) * i / 60)) for i in range(61)]
    s += shade(cur + [pl.P(V2, 0), pl.P(V1, 0)], GS)
    s += poly(cur, G, 5)
    s += line(*pl.P(V1, p1), *pl.P(V2, p2), O, 4, '2 10')
    s += dot(*pl.P(V1, p1), 10, INK) + dot(*pl.P(V2, p2), 10, INK)
    s += tag(pl.X(V1) + 14, pl.Y(p1) - 16, f'1: {p1:.1f} kPa', INK, 13, 'start')
    s += tag(pl.X(V2) - 4, pl.Y(p2) - 24, f'2: {p2:.1f} kPa', INK, 13, 'end')
    s += txt(pl.X(0.3), pl.Y(48), f'W = {W_:.2f} kJ', 18, G, 900)
    s += tag(pl.X(0.45), pl.Y(190), 'free expansion (dotted): W = 0', O, 13, 'end')
    return 'Same two states, two paths', s
D['me-thermo-u3-L2'] = (u3L2, 'lost work: 29.84 kJ', '3.3.1')


def u3L4():
    cp = 4.187
    m1, T1, m2, T2 = 2, 353, 3, 293
    Tf = (m1 * T1 + m2 * T2) / (m1 + m2)           # 317
    dS1 = m1 * cp * ln(Tf / T1); dS2 = m2 * cp * ln(Tf / T2)
    Sg = dS1 + dS2
    pl = Plot(0, 3, -1.25, 1.25, L=62, T=30, Wd=420, H=280)
    s = defs() + pl.axes(yt=(-1, -0.5, 0, 0.5, 1), yl='ΔS (kJ/K)', fmt=lambda v: f'{v:g}')
    s += line(pl.L, pl.Y(0), pl.L + pl.W, pl.Y(0), INK, 2.5)
    for i, (v, c, nm) in enumerate(((dS1, O, f'2 kg at {T1} K'), (dS2, B, f'3 kg at {T2} K'), (Sg, G, 'total'))):
        x = pl.X(i + 0.5) - 40
        y0, y1 = sorted((pl.Y(0), pl.Y(v)))
        s += rect(x, y0, 80, max(y1 - y0, 4), c, 'none', 0, 8)
        s += txt(x + 40, (pl.Y(v) - 10) if v > 0 else (pl.Y(v) + 22), f'{v:+.4f}', 14, INK, 900)
        s += txt(x + 40, pl.Y(0) + (-12 if v < 0 else 22) + (0 if v < 0 else 0), nm, 12, MUT, 800) if v < 0 else txt(x + 40, pl.Y(0) + 22, nm, 12, MUT, 800)
    s += tag(pl.X(2.5), pl.Y(0.55), 'Sgen > 0', G, 14)
    s += txt(pl.X(2.2), pl.Y(-0.7), f'both end at {Tf:.0f} K', 15, INK, 900)
    return 'Hot and cold water mixed', s
D['me-thermo-u3-L4'] = (u3L4, 'one falls, total rises', '3.8.1')


# ------------------------------------------------------------------ unit 4
def u4L1():
    m, c, T1, T0 = 10, 4.18, 360, 300
    mc = m * c
    Q = mc * (T1 - T0)                         # 2508
    dS = mc * ln(T1 / T0)                      # 7.621
    UE = T0 * dS; AE = Q - UE                  # 2286.3, 221.7
    pl = Plot(0, 9, 0, 400, L=62, T=24, Wd=410, H=280)
    s = defs() + pl.axes(xt=(0, 2, 4, 6, 8), yt=(0, 100, 200, 300, 400), xl='S (kJ/K) →', yl='T (K)', fmt=lambda v: f'{v:g}')
    cur = [pl.P(dS * i / 60, T0 * math.exp(dS * i / 60 / mc)) for i in range(61)]
    s += shade([pl.P(0, 0), pl.P(dS, 0), pl.P(dS, T0), pl.P(0, T0)], BS)
    s += shade(cur + [pl.P(dS, T0), pl.P(0, T0)], O)
    s += poly(cur, O, 4)
    s += line(pl.L, pl.Y(T0), pl.L + pl.W, pl.Y(T0), INK, 2.5, '7 7')
    s += dot(*pl.P(dS, T1), 8, O)
    s += tag(pl.X(dS) + 6, pl.Y(T1) - 4, f'{T1} K', O, 13, 'start')
    s += tag(pl.X(dS) + 6, pl.Y(T0) + 24, f'T₀ = {T0} K', INK, 13, 'start')
    s += tag(pl.X(dS / 2), pl.Y(T1) - 20, f'AE = {AE:.1f} kJ', O, 14)
    s += txt(pl.X(dS / 2), pl.Y(150), f'UE = {UE:.1f} kJ', 18, B, 900)
    s += txt(pl.X(dS / 2), pl.Y(150) + 26, 'goes to the surroundings', 13, MUT, 800)
    return 'Cooling water on T–S', s
D['me-thermo-u4-L1'] = (u4L1, 'only 8.8 % is work', '4.1.1')



# ------------------------------------------------------------------ unit 5
SAT_TV = [  # T °C, vf, vg (m3/kg), steam tables
    (20, 0.001002, 57.76), (50, 0.001012, 12.03), (100, 0.001043, 1.6720), (150, 0.001091, 0.3925),
    (200, 0.001157, 0.12721), (250, 0.001252, 0.05008), (300, 0.001404, 0.02166), (340, 0.001638, 0.01080),
    (360, 0.001895, 0.006945), (370, 0.002217, 0.004953), (373.95, 0.003106, 0.003106)]




def u5L4():
    R, T, p, V, Tc, pc, Z = 0.5183, 300, 20000, 0.060, 190.6, 4.60, 0.83
    TR, pR = T / Tc, p / 1000 / pc              # 1.57, 4.35
    vi = R * T / p; vr = Z * vi                 # 0.007775, 0.006453
    mi, mr = V / vi, V / vr                     # 7.72, 9.30
    s = defs()
    H = 230 / 10
    for x, mval, c, f, nm, vv in ((30, mi, B, BS, 'ideal gas', vi), (220, mr, G, GS, f'real, Z = {Z}', vr)):
        s += rect(x, 40, 120, 250, W, c, 3, 34)
        s += f'<rect x="{x + 6}" y="{284 - mval * H:.1f}" width="108" height="{mval * H:.1f}" rx="28" fill="{f}"/>'
        s += rect(x + 40, 26, 40, 16, c, 'none', 0, 4)
        s += txt(x + 60, 284 - mval * H / 2 + 8, f'{mval:.2f} kg', 20, INK, 900)
        s += txt(x + 60, 318, nm, 15, c, 900) + txt(x + 60, 340, f'v = {vv:.6f}', 12, MUT, 800)
    s += arr(156, 284 - mr * H, 214, 284 - mr * H, O, 3)
    s += tag(185, 284 - mr * H - 18, f'+{mr - mi:.2f} kg', O, 13)
    s += box(370, 60, 136, 110, f'Tᵣ = {TR:.2f}', INK, 15, sub=f'pᵣ = {pR:.2f}', subc=INK)
    s += txt(438, 190, 'pᵣ = 20 / 4.60', 13, O, 900) + txt(438, 208, 'both absolute', 12, O, 800)
    s += txt(438, 246, '60 L, 300 K', 13, MUT, 800)
    s += txt(438, 276, f'Z = {Z}:', 14, INK, 900) + txt(438, 296, 'more fits', 13, INK, 800)
    return 'Methane in a CNG cylinder', s
D['me-thermo-u5-L4'] = (u5L4, 'pᵣ from absolute p', '5.8.1')

PSAT = [(10, 1.2282), (15, 1.7057), (20, 2.3392), (21, 2.488), (22, 2.645), (25, 3.1698), (30, 4.247), (35, 5.6291), (38, 6.6990)]


# ------------------------------------------------------------------ unit 6


SAT_TS = [  # T °C, sf, sg (kJ/kg·K), steam tables
    (45.81, 0.6492, 8.1488), (100, 1.3072, 7.3541), (150, 1.8418, 6.8371), (179.9, 2.1381, 6.5850),
    (200, 2.3305, 6.4302), (250, 2.7935, 6.0721), (275.6, 3.0273, 5.8891), (300, 3.2552, 5.7059),
    (340, 3.6601, 5.3356), (360, 3.9167, 5.0536), (373.95, 4.4070, 4.4070)]

def u6L3():
    s1, s3, sf, sfg = 6.8826, 7.7641, 0.6492, 7.4996
    x4 = (s3 - sf) / sfg                              # 0.949
    xn = (s1 - sf) / sfg                              # 0.831
    pl = Plot(0, 8.6, 0, 560, L=56, T=24, Wd=440, H=280)
    s = defs() + pl.axes(xt=(0, 2, 4, 6, 8), yt=(0, 100, 200, 300, 400, 500), xl='s (kJ/kg·K) →', yl='T (°C)', fmt=lambda v: f'{v:g}')
    L_ = [pl.P(a, t) for t, a, b in SAT_TS]; R_ = [pl.P(b, t) for t, a, b in SAT_TS]
    s += shade(L_ + R_[::-1], MINT) + poly(L_ + R_[::-1], INK, 3)
    for q in (0.8, 0.9):
        s += poly([pl.P(a + q * (b - a), t) for t, a, b in SAT_TS[:7]], MUT, 1.6, '4 6')
    def sup(sa, Ta, sb, Tb, n=30):
        k = (sb - sa) / ln((Tb + 273.15) / (Ta + 273.15))
        return [pl.P(sa + (sb - sa) * i / n, (Ta + 273.15) * math.exp((sb - sa) * i / n / k) - 273.15) for i in range(n + 1)]
    heat = [pl.P(a, t) for t, a, b in SAT_TS if t <= 275.6] + [pl.P(5.8891, 275.6)] + sup(5.8891, 275.6, s1, 500)
    s += poly(heat, O, 4.5)
    s += line(*pl.P(s1, 500), *pl.P(s1, 240), O, 4.5) + poly(sup(s1, 240, s3, 500), O, 4.5)
    s += line(*pl.P(s3, 500), *pl.P(s3, 45.81), O, 4.5) + line(*pl.P(s3, 45.81), *pl.P(sf, 45.81), O, 4.5)
    s += line(*pl.P(s1, 240), *pl.P(s1, 45.81), MUT, 3, '6 6')
    s += dot(*pl.P(s3, 45.81), 9, G) + dot(*pl.P(s1, 45.81), 8, MUT)
    s += rect(70, 30, 190, 70, W, GRID, 2, 12)
    s += dot(88, 52, 8, G) + txt(102, 57, f'reheat: x = {x4:.3f}', 14, G, 900, 'start')
    s += dot(88, 80, 7, MUT) + txt(102, 85, f'no reheat: x = {xn:.3f}', 13, MUT, 900, 'start')
    s += tag(pl.X(s1) - 8, pl.Y(500) - 4, '60 bar, 500 °C', O, 12, 'end')
    s += tag(pl.X(s3) - 10, pl.Y(520) - 12, 'reheat', O, 12, 'end')
    return 'Reheat on T–s', s
D['me-thermo-u6-L3'] = (u6L3, 'η 40.0 % (38.4 %)', '6.6.1')

# ------------------------------------------------------------------ replacements matched to the final hooks
def u1L1():
    m1, me, Q = 2.0, 0.50, 30
    m2 = m1 - me                                   # 1.5 kg
    s = defs()
    s += rect(150, 60, 180, 190, GS, G, 3, 30) + txt(240, 120, 'rigid tank', 14, G, 900)
    s += f'<rect x="175" y="135" width="130" height="100" rx="16" fill="{BS}" stroke="{B}" stroke-width="3" stroke-dasharray="7 6"/>'
    s += txt(240, 180, f'{m2:g} kg left', 16, B, 900) + txt(240, 202, 'boundary B', 12, B, 800)
    s += rect(128, 40, 224, 230, 'none', O, 3, 36, '9 8') + txt(124, 40, 'boundary A', 12, O, 800, 'end')
    s += rect(232, 26, 16, 34, INK, 'none', 0, 3)
    s += arr(240, 24, 240, 2, O, 5) + lbl(258, 18, f'{me:g} kg air out', O, 14, 'start')
    s += arr(334, 190, 430, 190, MUT, 5) + lbl(372, 174, f'Q {Q} kJ out', MUT, 14, 'start')
    s += box(18, 290, 150, 60, 'A: open', O, 16, fill=OS, sub='mass crosses', subc=MUT)
    s += box(185, 290, 150, 60, 'B: closed', B, 16, fill=BS, sub='heat crosses', subc=MUT)
    s += box(352, 290, 150, 60, 'isolated?', INK, 16, sub='no: heat leaves', subc=O)
    s += txt(20, 120, f'{m1:g} kg', 18, INK, 900, 'start') + txt(20, 142, 'at start', 13, MUT, 800, 'start')
    return 'One tank, two boundaries', s
D['me-thermo-u1-L1'] = (u1L1, 'heat crosses: closed', '1.2.1')

def u1L2():
    t_a, t_b = 25.0, 35.0
    K = lambda c: c + 273.15
    bath = 273.16 * 75.00 / 60.00                    # 341.45 K from the gas thermometer
    lo, hi = -10, 80
    Y = lambda c: 330 - (c - lo) / (hi - lo) * 300
    s = defs()
    for x, head, c in ((120, '°C', B), (330, 'K', O)):
        s += rect(x - 26, 20, 52, 316, W, c, 3, 26) + txt(x, 14, head, 16, c, 900)
    for cdeg in range(-10, 81, 10):
        s += line(146, Y(cdeg), 304, Y(cdeg), GRID, 1.5)
        s += txt(84, Y(cdeg) + 5, f'{cdeg}', 12, MUT, 700, 'end') + txt(362, Y(cdeg) + 5, f'{K(cdeg):.2f}', 12, MUT, 700, 'start')
    s += rect(108, Y(t_b), 24, Y(lo) - Y(t_b), B, 'none', 0, 10) + rect(318, Y(t_b), 24, Y(lo) - Y(t_b), O, 'none', 0, 10)
    for cdeg, col in ((t_a, INK), (t_b, INK)):
        s += line(132, Y(cdeg), 318, Y(cdeg), col, 3)
    s += f'<rect x="170" y="{Y(t_b):.1f}" width="110" height="{Y(t_a) - Y(t_b):.1f}" fill="{OS}" stroke="none"/>'
    s += txt(225, (Y(t_a) + Y(t_b)) / 2 + 6, f'Δ = {t_b - t_a:g} K', 16, O, 900)
    s += tag(225, Y(t_a) + 26, f'{t_a:g} °C = {K(t_a):.2f} K', INK, 12)
    s += tag(225, Y(t_b) - 12, f'{t_b:g} °C = {K(t_b):.2f} K', INK, 12)
    s += line(318, Y(bath - 273.15), 342, Y(bath - 273.15), G, 4) + tag(212, Y(bath - 273.15) + 5, f'gas thermometer {bath:.2f} K', G, 12)
    s += box(422, 140, 92, 70, '+273.15', INK, 14, sub='for T only', subc=MUT)
    return 'Two scales, one step size', s
D['me-thermo-u1-L2'] = (u1L2, 'a rise: 1 °C = 1 K', '1.5.1')

def u2L1():
    m, cv, cp, R, dT = 2, 0.718, 1.005, 0.287, 100
    dU = m * cv * dT; dH = m * cp * dT; W_ = m * R * dT      # 143.6, 201.0, 57.4
    s = defs()
    Hs = 230 / 220; yb = 300
    for x0, name, rigid in ((20, 'rigid tank', True), (270, 'cylinder, constant p', False)):
        s += txt(x0 + 115, 22, name, 15, INK, 900)
        bx = x0 + 20
        s += rect(bx, yb - dU * Hs, 70, dU * Hs, G, 'none', 0, 8) + txt(bx + 35, yb - dU * Hs / 2 + 5, f'{dU:.1f}', 14, W, 900)
        s += txt(bx + 35, yb + 20, 'ΔU', 14, G, 900)
        if rigid:
            s += txt(x0 + 160, yb - dU * Hs / 2 - 6, 'W = 0', 15, MUT, 900) + txt(x0 + 160, yb - dU * Hs / 2 + 16, 'no boundary work', 12, MUT, 800)
            s += tag(x0 + 115, yb - dU * Hs - 26, f'Q = ΔU = {dU:.1f} kJ', G, 14)
        else:
            s += rect(bx, yb - dH * Hs, 70, W_ * Hs, O, 'none', 0, 8) + txt(bx + 35, yb - dU * Hs - W_ * Hs / 2 + 5, f'{W_:.1f}', 14, W, 900)
            s += txt(bx + 82, yb - dU * Hs - W_ * Hs / 2 + 5, 'W = pΔV', 13, O, 900, 'start')
            s += tag(x0 + 115, yb - dH * Hs - 22, f'Q = ΔH = {dH:.1f} kJ', O, 14)
    s += line(250, 40, 250, 330, GRID, 2)
    s += txt(260, 362, f'2 kg of air, 300 K → 400 K', 14, MUT, 800)
    return 'Same heating, two containers', s
D['me-thermo-u2-L1'] = (u2L1, 'rigid: Q = ΔU', '2.2.1')

def u3L3():
    Q1, T1, Q2, T2 = 500, 600, 300, 300
    a, b = Q1 / T1, -Q2 / T2
    tot = a + b                                        # -0.167
    s = defs()
    s += rect(20, 20, 150, 36, OS, O, 2.5, 10) + txt(95, 44, f'{T1} K', 15, O, 900)
    s += rect(20, 160, 150, 36, BS, B, 2.5, 10) + txt(95, 184, f'{T2} K', 15, B, 900)
    s += dot(95, 108, 26, W, INK, 3) + txt(95, 114, 'E', 17, INK, 900)
    s += arr(95, 58, 95, 78, O, 5) + lbl(84, 74, f'{Q1}', O, 14, 'end')
    s += arr(95, 136, 95, 156, B, 5) + lbl(84, 150, f'{Q2}', B, 14, 'end')
    s += arr(123, 108, 160, 108, INK, 5) + lbl(142, 132, f'W {Q1 - Q2}', INK, 13)
    s += box(200, 24, 300, 44, f'+{Q1} / {T1} = {a:+.4f}', O, 16, fill=OS)
    s += box(200, 80, 300, 44, f'−{Q2} / {T2} = {b:+.4f}', B, 16, fill=BS)
    s += box(200, 136, 300, 48, f'∮ δQ/T = {tot:+.3f} kJ/K', INK, 17)
    X = lambda v: 40 + (v + 0.5) / 1.0 * 440
    s += rect(X(-0.5), 236, X(0) - X(-0.5), 34, GS, 'none', 0, 8) + rect(X(0), 236, X(0.5) - X(0), 34, OS, 'none', 0, 8)
    s += line(X(0), 228, X(0), 278, INK, 3)
    s += txt((X(-0.5) + X(0)) / 2, 300, '< 0: irreversible', 14, G, 900) + txt((X(0) + X(0.5)) / 2, 300, '> 0: impossible', 14, O, 900)
    s += txt(X(0), 322, '= 0: reversible', 13, INK, 800)
    s += dot(X(tot), 253, 11, G) + tag(X(tot), 224, f'{tot:+.3f}', G, 13)
    s += txt(260, 356, f'η = {(Q1 - Q2) / Q1 * 100:.0f} % < Carnot {(1 - T2 / T1) * 100:.0f} %', 14, MUT, 800)
    return 'Clausius test of one cycle', s
D['me-thermo-u3-L3'] = (u3L3, 'below 0: irreversible', '3.6.1')

def u3L5():
    a = 0.002                                           # J/(mol·K⁴)
    S = lambda T: a * T ** 3 / 3
    c10 = a * 10 ** 3                                   # 2.0 J/(mol·K)
    Sc = lambda T: S(10) + c10 * ln(T / 10)             # if c stayed constant
    pl = Plot(0, 10, -2, 2.5, L=56, T=24, Wd=430, H=280)
    s = defs() + pl.axes(xt=(0, 2, 4, 6, 8, 10), yt=(-2, -1, 0, 1, 2), xl='T (K) →', yl='J/(mol·K)', fmt=lambda v: f'{v:g}')
    s += line(pl.L, pl.Y(0), pl.L + pl.W, pl.Y(0), MUT, 2)
    s += pl.curve(lambda T: a * T ** 3, 0, 10, c=B, w=4, dash='8 7')
    s += pl.curve(Sc, 10 * math.exp((-2 - S(10)) / c10), 10, c=O, w=4, dash='3 8')
    s += pl.curve(S, 0, 10, c=G, w=6)
    s += dot(*pl.P(0, 0), 10, G) + dot(*pl.P(10, S(10)), 10, G)
    s += tag(pl.X(10) - 6, pl.Y(-0.45), f'S(10 K) = {S(10):.3f}', G, 13, 'end')
    s += tag(pl.X(0) + 16, pl.Y(0) - 22, 'S = 0 at 0 K', G, 13, 'start')
    s += tag(pl.X(10) - 6, pl.Y(c10) - 16, f'cₚ = aT³: {c10:.1f} at 10 K', B, 12, 'end')
    s += tag(pl.X(3.2), pl.Y(-1.7), 'if cₚ stayed 2.0: S → −∞', O, 12, 'start')
    return 'Entropy of a solid near 0 K', s
D['me-thermo-u3-L5'] = (u3L5, 'S = aT³/3, never −∞', '3.10.1')

def u4L2():
    R, T, p = 0.287, 300, 100
    v = R * T / p                                       # 0.861
    d1 = -R * T / v ** 2                                # -116.1 (∂p/∂v)T
    d2 = R / p                                          # 0.00287 (∂v/∂T)p
    d3 = v / R                                          # 3.000 (∂T/∂p)v
    prod = d1 * d2 * d3
    pl = Plot(0.4, 1.6, 0, 220, L=56, T=24, Wd=220, H=250)
    s = defs() + pl.axes(xt=(0.5, 1.0, 1.5), yt=(0, 100, 200), xl='v (m³/kg)', yl='p (kPa)', fmt=lambda x: f'{x:g}')
    s += pl.curve(lambda vv: R * T / vv, 0.4, 1.6, c=G, w=5)
    x0, x1 = v - 0.25, v + 0.25
    s += line(*pl.P(x0, p + d1 * (x0 - v)), *pl.P(x1, p + d1 * (x1 - v)), O, 3.5)
    s += dot(*pl.P(v, p), 9, INK) + tag(pl.X(v) + 14, pl.Y(p) - 22, f'{T} K, {p} kPa', INK, 12, 'start')
    s += txt(pl.X(1.3), pl.Y(80), 'pv = RT', 14, G, 900)
    bx = 300
    for i, (lab, val, c) in enumerate(((f'(∂p/∂v)T', f'{d1:.1f}', O), ('(∂v/∂T)p', f'{d2:.5f}', B), ('(∂T/∂p)v', f'{d3:.3f}', G))):
        y = 20 + i * 78
        s += rect(bx, y, 200, 62, W, c, 2.5, 12) + txt(bx + 14, y + 26, lab, 15, c, 900, 'start') + txt(bx + 186, y + 50, val, 17, INK, 900, 'end')
        if i < 2: s += txt(bx + 100, y + 74, '×', 16, MUT, 900)
    s += box(bx, 262, 200, 56, f'product = {prod:.3f}', INK, 18, fill=OS)
    return 'Three slopes of air', s
D['me-thermo-u4-L2'] = (u4L2, 'the product is −1', '4.3 example')

def u4L3():
    a, b, cpm, Ru = 0.137, 3.87e-5, 29.1, 8.314
    mu = lambda T: (2 * a / (Ru * T) - b) / cpm * 1e5       # K/bar
    Ti = 2 * a / (Ru * b)                                   # 852 K
    m300 = mu(300); dT = m300 * (1 - 20)                    # 0.2445, -4.6
    pl = Plot(200, 1000, -0.15, 0.55, L=62, T=24, Wd=420, H=270)
    s = defs() + pl.axes(xt=(200, 400, 600, 800, 1000), yt=(-0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5), xl='T (K) →', yl='μJT (K/bar)', fmt=lambda v: f'{v:g}')
    s += shade([pl.P(200, 0), pl.P(Ti, 0), pl.P(Ti, 0.55), pl.P(200, 0.55)], GS, 0.6)
    s += shade([pl.P(Ti, 0), pl.P(1000, 0), pl.P(1000, -0.15), pl.P(Ti, -0.15)], OS, 0.8)
    s += line(pl.L, pl.Y(0), pl.L + pl.W, pl.Y(0), INK, 2.5)
    s += pl.curve(mu, 200, 1000, c=B, w=5)
    s += dot(*pl.P(300, m300), 9, B) + tag(pl.X(300) + 14, pl.Y(m300) - 18, f'300 K: {m300:.3f} K/bar', B, 12, 'start')
    s += dot(*pl.P(Ti, 0), 10, O) + tag(pl.X(Ti), pl.Y(0) - 24, f'inversion {Ti:.0f} K', O, 12)
    s += txt(pl.X(560), pl.Y(0.42), 'μ > 0: throttling cools', 14, G, 900)
    s += txt(pl.X(930), pl.Y(-0.1), 'warms', 13, O, 900)
    s += txt(250, 368, f'20 → 1 bar at 300 K: ΔT ≈ {dT:.1f} K', 14, INK, 900)
    return 'Throttling nitrogen', s
D['me-thermo-u4-L3'] = (u4L3, 'above 852 K it warms', '4.7.1')

PSAT_W = [(0.01, 0.6117), (20, 2.339), (50, 12.35), (100, 101.42), (150, 476.2), (200, 1554.9), (250, 3976.2), (300, 8587.9), (350, 16529), (373.95, 22064)]
PSUB = [(-40, 0.01285), (-30, 0.03802), (-20, 0.1035), (-10, 0.2601), (0.01, 0.6117)]

def u5L1():
    lg = math.log10
    pl = Plot(-45, 400, -2.2, 5.2, L=62, T=24, Wd=420, H=270)
    s = defs() + pl.axes(xt=(0, 100, 200, 300, 400), yl='p (kPa), log', xl='T (°C) →', gridlines=False, fmt=lambda v: f'{v:g}')
    for e, lab in ((-2, '0.01'), (0, '1'), (2, '100'), (4, '10⁴')):
        s += line(pl.L, pl.Y(e), pl.L + pl.W, pl.Y(e), GRID, 1.5) + txt(pl.L - 10, pl.Y(e) + 5, lab, 13, MUT, 700, 'end')
    boil = [pl.P(t, lg(p)) for t, p in PSAT_W]
    sub = [pl.P(t, lg(p)) for t, p in PSUB]
    melt = [pl.P(0.01 - (pp - 0.6117) / 13500, lg(pp)) for pp in (0.6117, 10, 1000, 1e5, 1.5e5)]
    s += shade([pl.P(-45, 5.2)] + melt[::-1] + sub[::-1] + [pl.P(-45, -2.2)], BS, 0.7)
    s += shade(melt + [pl.P(373.95, 5.2)] + boil[::-1], GS, 0.7)
    s += poly(sub, B, 4) + poly(melt, B, 4) + poly(boil, G, 4)
    s += line(pl.L, pl.Y(lg(101.325)), pl.L + pl.W, pl.Y(lg(101.325)), O, 3, '8 7')
    s += tag(pl.X(400) - 4, pl.Y(lg(101.325)) - 16, '1 atm = 101.325 kPa', O, 12, 'end')
    s += dot(*pl.P(0.01, lg(0.6117)), 10, INK) + tag(pl.X(0.01) + 16, pl.Y(lg(0.6117)) + 26, 'triple: 0.01 °C, 0.6117 kPa', INK, 12, 'start')
    s += dot(*pl.P(373.95, lg(22064)), 10, INK) + tag(pl.X(373.95) - 4, pl.Y(lg(22064)) - 18, 'critical 22.06 MPa', INK, 12, 'end')
    s += txt(pl.X(-25), pl.Y(3.5), 'ice', 15, B, 900) + txt(pl.X(110), pl.Y(3.8), 'liquid', 15, G, 900) + txt(pl.X(240), pl.Y(0.4), 'vapour', 15, MUT, 900)
    s += txt(250, 368, f'triple point is {101.325 / 0.6117:.0f} times below 1 atm', 14, INK, 900)
    return 'Water on p–T', s
D['me-thermo-u5-L1'] = (u5L1, 'triple point: 0.6117 kPa', '5.2.1')

def u5L2():
    C = 1
    cases = [('vapour', 1, 'pick p and T', '10 bar, 250 °C'), ('wet steam', 2, '10 bar fixes T', '179.9 °C'), ('triple cell', 3, 'nothing to pick', '0.01 °C, 0.6117 kPa')]
    s = defs()
    for i, (nm, P, say, val) in enumerate(cases):
        F = C - P + 2
        x0 = 14 + i * 168
        s += rect(x0 + 20, 40, 120, 180, W, INK, 3, 10) + rect(x0 + 14, 40, 132, 16, '#C9D3E6', INK, 2, 4)
        if P == 1:
            s += rect(x0 + 24, 60, 112, 156, BS, 'none', 0, 6)
        if P >= 2:
            s += rect(x0 + 24, 60, 112, 70, BS, 'none', 0, 6) + rect(x0 + 24, 130, 112, 86, GS, 'none', 0, 6)
        if P == 3:
            s += rect(x0 + 44, 120, 72, 34, '#F4F8FF', B, 2.5, 6) + txt(x0 + 80, 143, 'ice', 13, B, 900)
        s += txt(x0 + 80, 92, 'vapour', 13, B, 900)
        if P >= 2: s += txt(x0 + 80, 160 if P == 2 else 190, 'liquid', 13, G, 900)
        s += txt(x0 + 80, 26, nm, 15, INK, 900)
        s += box(x0 + 10, 238, 140, 52, f'F = {C} − {P} + 2 = {F}', O if F == 1 else INK, 15, fill=OS if F == 1 else W)
        s += txt(x0 + 80, 312, say, 13, INK, 900) + txt(x0 + 80, 332, val, 12, MUT, 800)
    s += txt(260, 368, 'F = C − P + 2, water: C = 1', 14, MUT, 800)
    return 'Phase rule, one to three phases', s
D['me-thermo-u5-L2'] = (u5L2, 'wet steam: F = 1', '5.3.1')

def u5L3():
    T1, h1, T2, h2, T, Tsat = 250, 2943.1, 300, 3051.6, 280, 179.9
    f = (T - T1) / (T2 - T1)                            # 0.6
    h = h1 + f * (h2 - h1)                              # 3008.2
    pl = Plot(150, 320, 2700, 3100, L=62, T=24, Wd=420, H=260)
    s = defs() + pl.axes(xt=(150, 200, 250, 300), yt=(2700, 2800, 2900, 3000, 3100), xl='T (°C) at 10 bar →', yl='h (kJ/kg)', fmt=lambda v: f'{v:g}')
    s += shade([pl.P(150, 2700), pl.P(Tsat, 2700), pl.P(Tsat, 3100), pl.P(150, 3100)], BS, 0.8)
    s += line(pl.X(Tsat), pl.T, pl.X(Tsat), pl.T + pl.H, B, 3, '7 6')
    s += txt(pl.X(165), pl.Y(3060), 'saturated', 13, B, 900) + txt(pl.X(165), pl.Y(3060) + 18, 'table', 13, B, 900)
    s += tag(pl.X(Tsat) + 8, pl.Y(2740), f'Tsat = {Tsat} °C', B, 12, 'start')
    s += txt(pl.X(222), pl.Y(2830), 'superheated table', 15, O, 900)
    s += line(*pl.P(T1, h1), *pl.P(T2, h2), O, 5)
    s += dot(*pl.P(T1, h1), 9, O) + dot(*pl.P(T2, h2), 9, O)
    s += tag(pl.X(T1) - 8, pl.Y(h1) + 6, f'250 °C: {h1}', O, 12, 'end')
    s += tag(pl.X(T2) - 4, pl.Y(h2) - 20, f'300 °C: {h2}', O, 12, 'end')
    s += line(pl.X(T), pl.Y(2700), pl.X(T), pl.Y(h), G, 2.5, '5 6')
    s += dot(*pl.P(T, h), 11, G) + tag(pl.X(T) + 16, pl.Y(h) + 30, f'280 °C: {h:.1f}', G, 13, 'start')
    s += txt(250, 372, f'f = (280 − 250)/(300 − 250) = {f:.1f}', 14, INK, 900)
    return '10 bar and 280 °C: which table?', s
D['me-thermo-u5-L3'] = (u5L3, 'T > Tsat: superheated', '5.5 example')

def u5L5():
    p, phi, ps = 101.325, 0.60, 4.247
    pv = phi * ps; pa = p - pv                          # 2.548, 98.777
    w = 0.622 * pv / pa; wwrong = 0.622 * pv / p        # 0.01605 vs 0.01564
    s = defs()
    X = lambda v: 20 + v / p * 480
    s += txt(20, 24, f'total p = {p} kPa', 15, INK, 900, 'start')
    s += rect(X(0), 40, X(pa) - X(0), 52, BS, B, 2.5, 8) + rect(X(pa), 40, X(p) - X(pa), 52, O, 'none', 0, 6)
    s += txt((X(0) + X(pa)) / 2, 72, f'dry air pₐ = {pa:.3f}', 16, B, 900)
    s += line(X(pa) + 6, 96, 470, 118, O, 2.5) + txt(500, 134, f'vapour pᵥ = {pv:.3f}', 14, O, 900, 'end')
    s += box(20, 160, 480, 64, f'w = 0.622 × {pv:.3f} / {pa:.3f} = {w:.5f}', G, 17, fill=GS, sub='kg of vapour per kg of dry air', subc=MUT)
    s += box(20, 240, 480, 52, f'÷ total p instead: {wwrong:.5f} (wrong)', O, 15, fill=OS)
    s += txt(260, 330, 'w counts per kg of dry air,', 15, INK, 900) + txt(260, 352, 'so use the dry air\'s own pressure', 15, INK, 900)
    return 'Moist air at 30 °C, φ = 60 %', s
D['me-thermo-u5-L5'] = (u5L5, 'w = 0.622 pᵥ / pₐ', '5.10 example')

def u6L1():
    R, cp, cv, g, r, k, T1, p1 = 0.287, 1.005, 0.718, 1.4, 15, 0.06, 300, 1.0
    rc = 1 + k * (r - 1)                                 # 1.84
    v1 = R * T1 / 100; v2 = v1 / r; v3 = rc * v2
    T2 = T1 * r ** (g - 1); T3 = rc * T2; T4 = T1 * rc ** g
    p2 = p1 * r ** g; p4 = p1 * T4 / T1
    qin = cp * (T3 - T2); qout = cv * (T4 - T1)          # 748.2, 290.4
    pl = Plot(0, 0.95, 0, 50, L=56, T=24, Wd=430, H=270)
    s = defs() + pl.axes(xt=(0, 0.3, 0.6, 0.9), yt=(0, 10, 20, 30, 40, 50), xl='v (m³/kg) →', yl='p (bar)', fmt=lambda v: f'{v:g}')
    def seg(va, vb, f, n=60): return [pl.P(va * (vb / va) ** (i / n), f(va * (vb / va) ** (i / n))) for i in range(n + 1)]
    c12 = seg(v1, v2, lambda v: p1 * (v1 / v) ** g)
    c34 = seg(v3, v1, lambda v: p2 * (v3 / v) ** g)
    s += shade(c12 + [pl.P(v3, p2)] + c34, GS, 0.9)
    s += poly(c12, B, 4) + poly(c34, B, 4)
    s += line(*pl.P(v2, p2), *pl.P(v3, p2), O, 7) + line(*pl.P(v1, p4), *pl.P(v1, p1), G, 7)
    for nm, v, p in (('1', v1, p1), ('2', v2, p2), ('3', v3, p2), ('4', v1, p4)):
        s += dot(*pl.P(v, p), 8, INK)
    s += tag(pl.X(v3) + 12, pl.Y(p2) + 4, f'2→3 at constant p: cₚ', O, 13, 'start')
    s += tag(pl.X(v3) + 12, pl.Y(p2) + 34, f'heat in = cₚ(T₃ − T₂) = {qin:.1f} kJ/kg', O, 12, 'start')
    s += tag(pl.X(v1) - 8, pl.Y(p4) - 36, f'4→1 at constant v: cᵥ', G, 13, 'end')
    s += tag(pl.X(v1) - 8, pl.Y(p4) - 8, f'heat out = cᵥ(T₄ − T₁) = {qout:.1f}', G, 12, 'end')
    s += txt(pl.X(0.55), pl.Y(26), f'r = {r}, rc = {rc:.2f}', 14, INK, 900) + txt(pl.X(0.55), pl.Y(26) + 22, f'η = {(qin - qout) / qin * 100:.1f} %', 14, INK, 900)
    return 'Diesel cycle, r = 15', s
D['me-thermo-u6-L1'] = (u6L1, 'heat in at constant p: cₚ', '6.2.1')

def u6L2():
    R, g, r, T1, p1, wnet = 0.287, 1.4, 8, 300, 1.0, 451.8
    v1 = R * T1 / 100; v2 = v1 / r                       # 0.861, 0.1076
    p2 = p1 * r ** g; T3 = T1 * r ** (g - 1) + 800 / 0.718
    p3 = p2 * T3 / (T1 * r ** (g - 1)); p4 = p3 / r ** g
    mep = wnet / (v1 - v2) / 100                         # bar
    pl = Plot(0, 0.95, 0, 52, L=56, T=24, Wd=430, H=226)
    s = defs() + pl.axes(xt=(0, 0.3, 0.6, 0.9), yt=(0, 10, 20, 30, 40, 50), xl='v (m³/kg) →', yl='p (bar)', fmt=lambda v: f'{v:g}')
    def seg(va, vb, f, n=60): return [pl.P(va * (vb / va) ** (i / n), f(va * (vb / va) ** (i / n))) for i in range(n + 1)]
    c12 = seg(v1, v2, lambda v: p1 * (v1 / v) ** g); c34 = seg(v2, v1, lambda v: p3 * (v2 / v) ** g)
    s += shade(c12 + c34, OS, 0.9)
    s += f'<rect x="{pl.X(v2):.1f}" y="{pl.Y(mep):.1f}" width="{pl.X(v1) - pl.X(v2):.1f}" height="{pl.Y(0) - pl.Y(mep):.1f}" fill="{B}" fill-opacity=".25" stroke="{B}" stroke-width="3" stroke-dasharray="7 6"/>'
    s += poly(c12, INK, 3.5) + poly(c34, INK, 3.5) + line(*pl.P(v2, p2), *pl.P(v2, p3), O, 5) + line(*pl.P(v1, p4), *pl.P(v1, p1), INK, 3.5)
    s += tag(pl.X(0.5), pl.Y(mep) - 16, f'MEP = {mep:.2f} bar: same area', B, 13)
    yb = pl.Y(0) + 70
    s += line(pl.X(v2), yb, pl.X(v1), yb, B, 3) + line(pl.X(v2), yb - 8, pl.X(v2), yb + 8, B, 3) + line(pl.X(v1), yb - 8, pl.X(v1), yb + 8, B, 3)
    s += tag((pl.X(v2) + pl.X(v1)) / 2, yb + 6, f'swept v₁ − v₂ = {v1 - v2:.4f}', B, 12)
    s += tag(pl.X(v2) + 10, pl.Y(50), f'v₂ = {v2:.4f}: clearance', MUT, 12, 'start')
    s += txt(pl.X(0.6), pl.Y(32), f'Otto, r = {r}', 14, INK, 900) + txt(pl.X(0.6), pl.Y(32) + 22, f'net work {wnet} kJ/kg', 14, INK, 900)
    return 'MEP of an Otto cycle', s
D['me-thermo-u6-L2'] = (u6L2, 'divide by swept volume', '6.4 example')

def u6L4():
    h1, h2, h3 = 392.66, 426.48, 256.41
    pL, pH = 2.01, 10.17                                 # bar, -10 °C and 40 °C
    qL, w, qH = h1 - h3, h2 - h1, h2 - h3
    lg = math.log10
    pl = Plot(200, 460, lg(1), lg(20), L=56, T=74, Wd=440, H=170)
    s = defs() + pl.axes(xt=(250, 350, 450), xl='h (kJ/kg) →', yl='p (bar), log', gridlines=False, fmt=lambda v: f'{v:g}')
    for v in (1, 2, 5, 10, 20):
        s += line(pl.L, pl.Y(lg(v)), pl.L + pl.W, pl.Y(lg(v)), GRID, 1.5) + txt(pl.L - 10, pl.Y(lg(v)) + 5, v, 13, MUT, 700, 'end')
    s += shade([pl.P(h3, lg(pL)), pl.P(h1, lg(pL)), pl.P(h2, lg(pH)), pl.P(h3, lg(pH))], MINT)
    s += line(*pl.P(h3, lg(pL)), *pl.P(h1, lg(pL)), B, 5) + line(*pl.P(h1, lg(pL)), *pl.P(h2, lg(pH)), INK, 5)
    s += line(*pl.P(h2, lg(pH)), *pl.P(h3, lg(pH)), O, 5) + line(*pl.P(h3, lg(pH)), *pl.P(h3, lg(pL)), MUT, 4, '6 6')
    for nm, h, p in (('1', h1, pL), ('2', h2, pH), ('3', h3, pH), ('4', h3, pL)):
        s += dot(*pl.P(h, lg(p)), 8, INK)
    s += txt(pl.X(320), pl.Y(lg(pH)) - 10, '40 °C, 10.17 bar', 12, O, 800) + txt(pl.X(320), pl.Y(lg(pL)) + 22, '−10 °C, 2.01 bar', 12, B, 800)
    yb = 318
    for (a, b, c, lab, yy) in ((h3, h1, B, '', yb), (h1, h2, INK, '', yb), (h3, h2, O, '', yb + 36)):
        s += line(pl.X(a), yy, pl.X(b), yy, c, 5)
        s += line(pl.X(a), yy - 7, pl.X(a), yy + 7, c, 3) + line(pl.X(b), yy - 7, pl.X(b), yy + 7, c, 3)
    s += txt((pl.X(h3) + pl.X(h1)) / 2, yb - 10, f'qL = {qL:.2f}', 13, B, 900) + txt(pl.X(h2) + 6, yb + 5, f'w = {w:.2f}', 13, INK, 900, 'start')
    s += txt((pl.X(h3) + pl.X(h2)) / 2, yb + 30, f'qH = {qH:.2f} (not the COP)', 13, O, 900)
    s += box(150, 4, 230, 46, f'COP = qL ÷ w = {qL / w:.2f}', G, 16, fill=GS)
    return 'R-134a cycle on p–h', s
D['me-thermo-u6-L4'] = (u6L4, 'COP = qL / w = 4.03', '6.7.1')
