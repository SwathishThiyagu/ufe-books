"""Claude's hand-drawn figures for me-thermo-u6 (Engineering Thermodynamics: power and refrigeration cycles), one per
chapter, drawn from each chapter's own worked example. Every plotted point is computed (ideal-gas relations for air,
IAPWS steam properties and R-134a properties, precomputed below). Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
G, CV, CP, RG = 1.4, 0.718, 1.005, 0.287


def sb(base, s, size=14):
    """text with a subscript, for SVG labels"""
    return f'{base}<tspan dy="4" font-size="{size - 3}">{s}</tspan><tspan dy="-4"> </tspan>'


def frame(x0, x1, y0, y1, fx, fy, xt, yt, xlab, ylab, xfmt=str, yfmt=str, grid=True):
    o = [L(x0, y1, x1, y1, L2, 1.5), L(x0, y0, x0, y1, L2, 1.5)]
    for v in xt:
        X = fx(v); o += [L(X, y1, X, y1 + 5, L2, 1.5), T(X, y1 + 19, xfmt(v), 13, fill=MUT)]
    for v in yt:
        Y = fy(v); o += [L(x0 - 5, Y, x0, Y, L2, 1.5), T(x0 - 8, Y + 4.5, yfmt(v), 13, 'end', MUT)]
        if grid: o.append(L(x0, Y, x1, Y, LN, 1))
    o.append(T((x0 + x1) / 2, y1 + 38, xlab, 13, fill=MUT))
    o.append(T(x0 - 4, y0 - 12, ylab, 13, 'start', MUT))
    return ''.join(o)


def dot(x, y, n, dx=8, dy=-8, c=AC, anchor='start', size=14):
    return C(x, y, 4.5, c) + T(x + dx, y + dy, n, size, anchor, INK, True)


def curve(f, a, b, n=40):
    return [f(a + (b - a) * i / n) for i in range(n + 1)]


# ---- 6.1 Carnot cycle of the worked example: p-v and T-s ----
def f1():
    o = []
    v1, v2 = 0.861, 0.861 / 3 ** 2.5
    v3, v4 = 2 * v2, 2 * 0.861
    p1, p2 = 1.0, 3 ** 3.5
    x0, x1, y0, y1 = 70, 330, 50, 290
    fx = lambda v: x0 + v / 1.8 * (x1 - x0); fy = lambda p: y1 - p / 50 * (y1 - y0)
    o.append(T(x0 - 4, 24, 'p-v diagram', 15, 'start', INK, True))
    o.append(frame(x0, x1, y0, y1, fx, fy, [0, 0.6, 1.2, 1.8], [0, 10, 20, 30, 40, 50], 'v (m³/kg)', 'p (bar)', grid=False))
    pts = [(fx(v), fy(p1 * (v1 / v) ** G)) for v in [v1 - (v1 - v2) * (i / 40) ** 0.35 for i in range(41)]]
    o.append(P(pts, AC, 2.5))
    pts = [(fx(v), fy(p2 * v2 / v)) for v in curve(lambda t: t, v2, v3, 20)]
    o.append(P(pts, LV, 3))
    p3 = p2 / 2
    pts = [(fx(v), fy(p3 * (v3 / v) ** G)) for v in [v3 + (v4 - v3) * (i / 40) ** 2.2 for i in range(41)]]
    o.append(P(pts, AC, 2.5))
    pts = [(fx(v), fy(p1 * v1 / v)) for v in curve(lambda t: t, v1, v4, 20)]
    o.append(P(pts, NX, 3))
    o.append(dot(fx(v1), fy(1), '1', -6, -10, anchor='end'))
    o.append(dot(fx(v2), fy(p2), '2  (46.8 bar)', 9, 4))
    o.append(dot(fx(v3), fy(p3), '3  (23.4 bar)', 10, 5))
    o.append(dot(fx(v4), fy(0.5), '4', 0, -12, anchor='middle'))
    o.append(T(fx(1.0), fy(30), 'volume ratio 31', 13, 'start', MUT))
    o.append(T(fx(1.0), fy(26), 'pressure ratio 94', 13, 'start', MUT))
    # T-s
    a0, a1, b0, b1 = 440, 690, 50, 290
    gx = lambda s: a0 + s / 0.25 * (a1 - a0); gy = lambda t: b1 - t / 1000 * (b1 - b0)
    o.append(T(a0 - 4, 24, 'T-s diagram', 15, 'start', INK, True))
    o.append(frame(a0, a1, b0, b1, gx, gy, [0, 0.1, 0.2], [0, 300, 600, 900], 's − s₁ (kJ/kg·K)', 'T (K)', lambda v: str(v), grid=False))
    ds = 0.1989
    o.append(R(gx(0), gy(900), gx(ds) - gx(0), gy(300) - gy(900), ACS, 'none', 0, 0))
    o.append(R(gx(0), gy(300), gx(ds) - gx(0), gy(0) - gy(300), NXS, 'none', 0, 0))
    o.append(L(gx(0), gy(300), gx(0), gy(900), AC, 2.5)); o.append(L(gx(ds), gy(900), gx(ds), gy(300), AC, 2.5))
    o.append(L(gx(0), gy(900), gx(ds), gy(900), LV, 3)); o.append(L(gx(ds), gy(300), gx(0), gy(300), NX, 3))
    o.append(dot(gx(0), gy(300), '1', -8, 18, anchor='end')); o.append(dot(gx(0), gy(900), '2', 8, 20))
    o.append(dot(gx(ds), gy(900), '3', -8, 20, anchor='end')); o.append(dot(gx(ds), gy(300), '4', 8, 18))
    o.append(T((gx(0) + gx(ds)) / 2, gy(640), 'w', 15, fill=INK, bold=True))
    o.append(T((gx(0) + gx(ds)) / 2, gy(580), '= 119.4', 13, fill=INK))
    o.append(T((gx(0) + gx(ds)) / 2, gy(160), sb('q', 'out') + '= 59.7', 13, fill=INK))
    o.append(T((gx(0) + gx(ds)) / 2, gy(900) - 10, sb('q', 'in') + '= 179.0 kJ/kg at 900 K', 13, 'middle', LV, True))
    o.append(T(360, 340, 'η = 1 − 300/900 = 66.7%; MEP only 0.716 bar', 14, 'middle', INK, True))
    return 356, ''.join(o)


FIG[1] = (f1, 'The worked example’s Carnot cycle between 300 K and 900 K. On the T-s diagram it is a rectangle, and the shaded upper part is the net work; on the p-v diagram the same work is a thin sliver that needs a pressure ratio of 94, which is why its mean effective pressure is so low.',
          'Left: p-v diagram of an air Carnot cycle with states 1 to 4; state 2 at 46.8 bar, state 3 at 23.4 bar, state 4 at 0.5 bar. Right: the same cycle as a rectangle on the T-s diagram between 300 K and 900 K, with heat in 179.0 kJ/kg, heat out 59.7 kJ/kg and net work 119.4 kJ/kg.')


# ---- 6.2 Otto, Diesel and Dual cycles on p-v (shapes sketched, pressures from the worked examples) ----
def f2():
    o = []
    # shape units: v from 0.2 (clearance) to 1.0, p from 1; labels carry the real pressures in bar
    cyc = [
        ('Otto (r = 8)', [(1.0, 1.0, '1', '1'), (0.2, 9.52, '2', '18.4'), (0.2, 19.0, '3', '48.1'), (1.0, 2.0, '4', '2.62')], ['s', 'v', 's', 'v']),
        ('Diesel (r = 15)', [(1.0, 1.0, '1', '1'), (0.2, 9.52, '2', '44.3'), (0.38, 9.52, '3', '44.3'), (1.0, 2.46, '4', '2.35')], ['s', 'p', 's', 'v']),
        ('Dual (r = 14)', [(1.0, 1.0, '1', '1'), (0.2, 9.52, '2', '40.2'), (0.2, 14.3, '3', '60.4'), (0.32, 14.3, '4', '60.4'), (1.0, 2.77, '5', '2.90')], ['s', 'v', 'p', 's', 'v']),
    ]
    W0, gap = 192, 38
    for i, (name, st, kinds) in enumerate(cyc):
        x0 = 56 + i * (W0 + gap); x1 = x0 + W0; y0, y1 = 70, 300
        fx = lambda v, x0=x0, x1=x1: x0 + 8 + v / 1.08 * (x1 - x0 - 8); fy = lambda p: y1 - p / 21 * (y1 - y0)
        o.append(T((x0 + x1) / 2, 30, name, 14, 'middle', INK, True))
        o.append(L(x0, y1, x1, y1, L2, 1.5, arrow='m')); o.append(L(x0, y1, x0, y0 - 10, L2, 1.5, arrow='m'))
        o.append(T(x1 - 2, y1 + 20, 'v', 14, 'end', MUT, italic=True)); o.append(T(x0 + 8, y0 - 6, 'p', 14, 'start', MUT, italic=True))
        for j in range(len(st)):
            va, pa = st[j][:2]; vb, pb = st[(j + 1) % len(st)][:2]
            k = kinds[j]
            if k == 's':
                n = math.log(pb / pa) / math.log(va / vb)
                pts = [(fx(v), fy(pa * (va / v) ** n)) for v in curve(lambda t: t, va, vb, 40)]
                o.append(P(pts, AC, 2.3))
            else:
                heat_in = (k == 'v' and pb > pa) or k == 'p'
                o.append(L(fx(va), fy(pa), fx(vb), fy(pb), LV if heat_in else NX, 3.2))
        flat = [j for j in range(len(st)) if kinds[j] == 'p']
        fj = flat[0] if flat else -1
        for j, (v, p, n, val) in enumerate(st):
            if n == '1': o.append(dot(fx(v), fy(p), f'1 ({val} bar)', 0, 20, anchor='end'))
            elif v > 0.9: o.append(dot(fx(v), fy(p), f'{n} ({val})', 0, -10, anchor='middle'))
            elif j == fj: o.append(dot(fx(v), fy(p), n, -8, 5, anchor='end'))
            elif j == fj + 1 and fj >= 0:
                o.append(dot(fx(v), fy(p), n, 8, 5))
                o.append(T((fx(v) + fx(st[fj][0])) / 2, fy(p) - 12, val, 13, 'middle', INK, True))
            elif n == '2': o.append(dot(fx(v), fy(p), f'{n} ({val})', 8, 16))
            else: o.append(dot(fx(v), fy(p), f'{n} ({val})', -7, -9, anchor='end' if fx(v) - 60 > x0 else 'start'))
    o.append(L(70, 352, 100, 352, LV, 3)); o.append(T(108, 357, 'heat added', 13, 'start', MUT))
    o.append(L(240, 352, 270, 352, NX, 3)); o.append(T(278, 357, 'heat rejected', 13, 'start', MUT))
    o.append(L(420, 352, 450, 352, AC, 2.3)); o.append(T(458, 357, 'isentropic', 13, 'start', MUT))
    o.append(T(360, 386, 'Shapes sketched; numbers in brackets are the worked examples’ pressures in bar.', 13, 'middle', MUT))
    return 402, ''.join(o)


FIG[2] = (f2, 'The three cycles sketched on p-v and labelled with the pressures of this unit’s worked examples (Dual: the example in the next chapter). Otto adds its heat on a vertical (constant-volume) line, Diesel on a horizontal (constant-pressure) line, and Dual on both, one after the other; all three reject heat on the vertical line back to state 1.',
          'Three p-v sketches side by side. Otto: 1 bar, 18.4, 48.1 and 2.62 bar at states 1 to 4, with vertical heat lines. Diesel: 44.3 bar at states 2 and 3 joined by a horizontal heat line, 2.35 bar at state 4. Dual: 40.2 bar at 2, then 60.4 bar at 3 and 4, and 2.90 bar at 5.')


# ---- 6.3 Brayton cycle on T-s and Stirling cycle on p-v ----
def f3():
    o = []
    x0, x1, y0, y1 = 70, 330, 56, 300
    fx = lambda s: x0 + s / 0.9 * (x1 - x0); fy = lambda t: y1 - t / 1300 * (y1 - y0)
    o.append(T(x0 - 4, 26, 'Brayton, T-s, pressure ratio 8', 15, 'start', INK, True))
    o.append(frame(x0, x1, y0, y1, fx, fy, [0, 0.3, 0.6, 0.9], [0, 400, 800, 1200], 's − s₁ (kJ/kg·K)', 'T (K)', grid=False))
    s3 = CP * math.log(1200 / 543.4)
    o.append(L(fx(0), fy(300), fx(0), fy(543.4), AC, 2.5))
    o.append(P([(fx(s), fy(543.4 * math.exp(s / CP))) for s in curve(lambda t: t, 0, s3, 30)], LV, 3))
    o.append(L(fx(s3), fy(1200), fx(s3), fy(662.5), AC, 2.5))
    o.append(P([(fx(s), fy(300 * math.exp(s / CP))) for s in curve(lambda t: t, s3, 0, 30)], NX, 3))
    o.append(dot(fx(0), fy(300), '1  300 K', 8, 16))
    o.append(dot(fx(0), fy(543.4), '2  543 K', 8, 18))
    o.append(dot(fx(s3), fy(1200), '3  1200 K', -8, -8, anchor='end'))
    o.append(dot(fx(s3), fy(662.5), '4  663 K', 8, 5))
    o.append(T(fx(0.5), fy(720), 'p₂ = 8 bar', 13, 'start', LV))
    o.append(T(fx(0.45), fy(330), 'p₁ = 1 bar', 13, 'start', NX))
    o.append(T(fx(0.04), fy(1160), sb('w', 'net') + '= 295.6 kJ/kg', 13, 'start', INK, True))
    o.append(T(fx(0.04), fy(1080), 'η = 44.8%', 13, 'start', MUT))
    # Stirling p-v
    a0, a1, b0, b1 = 440, 690, 56, 300
    gx = lambda v: a0 + (v - 0.3) / 0.65 * (a1 - a0); gy = lambda p: b1 - p / 7 * (b1 - b0)
    o.append(T(a0 - 4, 26, 'Stirling, p-v (air)', 15, 'start', INK, True))
    o.append(frame(a0, a1, b0, b1, gx, gy, [0.4, 0.6, 0.8], [0, 2, 4, 6], 'v (m³/kg)', 'p (bar)', grid=False))
    vmax, vmin = 0.861, 0.4305
    o.append(P([(gx(v), gy(1 * vmax / v)) for v in curve(lambda t: t, vmax, vmin, 30)], NX, 3))
    o.append(L(gx(vmin), gy(2), gx(vmin), gy(6), AC, 2.5, '7 5'))
    o.append(P([(gx(v), gy(6 * vmin / v)) for v in curve(lambda t: t, vmin, vmax, 30)], LV, 3))
    o.append(L(gx(vmax), gy(3), gx(vmax), gy(1), AC, 2.5, '7 5'))
    o.append(dot(gx(vmax), gy(1), '1', 8, 5)); o.append(dot(gx(vmin), gy(2), '2', -8, 5, anchor='end'))
    o.append(dot(gx(vmin), gy(6), '3', -8, 5, anchor='end')); o.append(dot(gx(vmax), gy(3), '4', 8, 5))
    o.append(T(gx(0.56), gy(5.15), '900 K: heat in 179.0', 13, 'start', LV))
    o.append(T(gx(0.47), gy(0.55), '300 K: heat out 59.7', 13, 'start', NX))
    o.append(T(gx(0.645), gy(2.55), 'dashed: heat', 13, 'middle', MUT))
    o.append(T(gx(0.645), gy(2.1), 'via regenerator', 13, 'middle', MUT))
    o.append(T(gx(0.645), gy(1.65), '430.8 kJ/kg', 13, 'middle', MUT))
    return 356, ''.join(o)


FIG[3] = (f3, 'Left: the Brayton example, with heat added along the 8 bar line from 543 K to 1200 K and rejected along the 1 bar line. Right: the Stirling example between 300 K and 900 K; the two dashed constant-volume steps exchange 430.8 kJ/kg through the regenerator instead of with the outside.',
          'Left: T-s diagram of a Brayton cycle with states 1 (300 K), 2 (543 K), 3 (1200 K) and 4 (663 K) on two constant-pressure lines. Right: p-v diagram of a Stirling cycle with isotherms at 300 K and 900 K between 0.43 and 0.86 m³/kg, and dashed constant-volume steps.')


# ---- 6.4 Otto vs Diesel on T-s for the same r and heat input ----
def f4():
    o = []
    x0, x1, y0, y1 = 80, 520, 50, 330
    fx = lambda s: x0 + s / 1.0 * (x1 - x0); fy = lambda t: y1 - t / 2700 * (y1 - y0)
    o.append(frame(x0, x1, y0, y1, fx, fy, [0, 0.25, 0.5, 0.75, 1.0], [0, 500, 1000, 1500, 2000, 2500], 's − s₁ (kJ/kg·K)', 'T (K)', grid=False))
    T2 = 862.1
    so, sd = CV * math.log(2533.4 / T2), CP * math.log(2056.2 / T2)
    # rejected-heat areas under the 4-1 lines
    ao = [(fx(s), fy(300 * math.exp(s / CV))) for s in curve(lambda t: t, 0, so, 25)]
    ad = [(fx(s), fy(300 * math.exp(s / CV))) for s in curve(lambda t: t, so, sd, 10)]
    o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in ao + [(fx(so), fy(0)), (fx(0), fy(0))])}" style="fill:var(--next-soft);stroke:none"/>')
    o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in ad + [(fx(sd), fy(0)), (fx(so), fy(0))])}" style="fill:var(--live-soft);stroke:none"/>')
    o.append(L(fx(0), fy(300), fx(0), fy(T2), AC, 2.5))
    o.append(P([(fx(s), fy(T2 * math.exp(s / CV))) for s in curve(lambda t: t, 0, so, 30)], AC, 3))
    o.append(L(fx(so), fy(2533.4), fx(so), fy(881.6), AC, 2.5))
    o.append(P([(fx(s), fy(T2 * math.exp(s / CP))) for s in curve(lambda t: t, 0, sd, 30)], LV, 3, '8 5'))
    o.append(L(fx(sd), fy(2056.2), fx(sd), fy(1013.0), LV, 2.5, '8 5'))
    o.append(P([(fx(s), fy(300 * math.exp(s / CV))) for s in curve(lambda t: t, 0, sd, 30)], NX, 2.5))
    o.append(dot(fx(0), fy(300), '1', -8, 5, anchor='end')); o.append(dot(fx(0), fy(T2), '2', -8, 0, anchor='end'))
    o.append(dot(fx(so), fy(2533.4), '3 (Otto)', -10, -4, anchor='end'))
    o.append(dot(fx(so), fy(881.6), '4', -9, -6, anchor='end'))
    o.append(dot(fx(sd), fy(2056.2), "3′ (Diesel)", 9, 4, LV))
    o.append(dot(fx(sd), fy(1013.0), "4′", 9, 4, LV))
    o.append(T(fx(0.33), fy(130), 'Otto rejects 417.6', 13, 'middle', INK, True))
    # key
    kx = 560
    o.append(T(kx, 80, 'r = 14,', 14, 'start', INK, True))
    o.append(T(kx, 100, sb('q', 'in') + '= 1200 kJ/kg', 14, 'start', INK, True))
    o.append(L(kx, 136, kx + 28, 136, AC, 3)); o.append(T(kx + 36, 141, 'Otto', 13, 'start', INK))
    o.append(T(kx + 36, 159, 'η = 65.2%', 13, 'start', MUT))
    o.append(L(kx, 190, kx + 28, 190, LV, 3, '8 5')); o.append(T(kx + 36, 195, 'Diesel', 13, 'start', INK))
    o.append(T(kx + 36, 213, 'η = 57.3%', 13, 'start', MUT))
    o.append(R(kx, 238, 22, 14, LVS, 'none', 2, 0)); o.append(T(kx + 30, 250, 'extra heat', 13, 'start', MUT))
    o.append(T(kx + 30, 267, 'Diesel rejects:', 13, 'start', MUT))
    o.append(T(kx + 30, 284, '511.9 − 417.6', 13, 'start', MUT))
    o.append(T(kx + 30, 301, '= 94.3 kJ/kg', 13, 'start', MUT))
    return 386, ''.join(o)


FIG[4] = (f4, 'Otto and Diesel cycles with the same compression ratio (14) and the same heat input (1200 kJ/kg) share states 1 and 2. The steeper constant-volume line takes the heat in with less rise in entropy, so the Otto cycle rejects less heat (the area under its line 4-1) than the Diesel cycle (which adds the right-hand strip).',
          'T-s diagram: Otto cycle 1-2-3-4 climbing to 2533 K and Diesel cycle 1-2-3′-4′ climbing to 2056 K along a flatter constant-pressure line. Shaded areas under the heat-rejection line show 417.6 kJ/kg for Otto and an extra 94.3 kJ/kg for Diesel.')


# ---- steam dome data (IAPWS), T in °C, s in kJ/kg·K ----
DOME = [(0.01, 0.0, 9.155), (20, 0.296, 8.666), (45.81, 0.649, 8.149), (80, 1.076, 7.611), (120, 1.528, 7.129), (160, 1.943, 6.749),
        (200, 2.331, 6.43), (250, 2.794, 6.072), (300, 3.255, 5.706), (340, 3.66, 5.336), (360, 3.917, 5.054), (370, 4.111, 4.801), (373.9, 4.34, 4.483)]


def dome(fx, fy):
    left = [(fx(sf), fy(t)) for t, sf, sg in DOME]
    right = [(fx(sg), fy(t)) for t, sf, sg in reversed(DOME)]
    return P(left + right, MUT, 2)


# ---- 6.5 Rankine cycle on T-s ----
def f5():
    o = []
    x0, x1, y0, y1 = 80, 560, 40, 330
    fx = lambda s: x0 + s / 9 * (x1 - x0); fy = lambda t: y1 - t / 450 * (y1 - y0)
    o.append(frame(x0, x1, y0, y1, fx, fy, [0, 2, 4, 6, 8], [0, 100, 200, 300, 400], 's (kJ/kg·K)', 'T (°C)', grid=False))
    o.append(dome(fx, fy))
    liq = [(0.65, 46), (1.304, 100), (1.838, 150), (2.327, 200), (2.797, 250.35)]
    sup = [(6.070, 250.35), (6.138, 260), (6.364, 300), (6.584, 350), (6.771, 400)]
    o.append(P([(fx(s), fy(t)) for s, t in liq] + [(fx(s), fy(t)) for s, t in sup], LV, 3))
    o.append(L(fx(6.771), fy(400), fx(6.771), fy(45.81), AC, 2.5))
    o.append(L(fx(6.771), fy(45.81), fx(0.649), fy(45.81), NX, 3))
    o.append(dot(fx(6.771), fy(400), '1  40 bar, 400 °C', 9, 4))
    o.append(dot(fx(6.771), fy(45.81), '2  x = 0.816', 9, 16))
    o.append(dot(fx(0.649), fy(45.81), '3, 4', -4, -10, anchor='end'))
    o.append(T(fx(3.9), fy(268), 'boiling at 250.4 °C', 13, 'middle', LV))
    o.append(T(fx(3.6), fy(45.81) + 19, 'condensing at 0.1 bar, 45.8 °C', 13, 'middle', NX))
    o.append(T(fx(6.9), fy(205), sb('w', 'T') + '= 1070.0', 13, 'start', AC, True))
    o.append(T(fx(2.15), fy(110), 'water heating', 13, 'start', MUT))
    o.append(T(fx(2.15), fy(93), 'in the boiler', 13, 'start', MUT))
    o.append(T(fx(4.3), fy(150), 'two-phase', 13, 'middle', MUT))
    o.append(T(fx(4.3), fy(133), 'dome', 13, 'middle', MUT))
    kx = 584
    o += [T(kx, 72, sb('q', 'in') + '= 3018.7', 13, 'start', INK, True), T(kx, 90, 'kJ/kg', 13, 'start', MUT),
          T(kx, 124, sb('w', 'P') + '= 4.03', 13, 'start', INK, True), T(kx, 142, 'kJ/kg', 13, 'start', MUT),
          T(kx, 176, 'η = 35.3%', 14, 'start', INK, True), T(kx, 210, 'SSC =', 13, 'start', MUT), T(kx, 228, '3.38 kg/kWh', 13, 'start', MUT)]
    return 380, ''.join(o)


FIG[5] = (f5, 'The worked example’s Rankine cycle on the T-s diagram of water. Heat goes in along the 40 bar line (water heating, boiling at 250.4 °C, superheating to 400 °C), the turbine expands the steam straight down into the dome to dryness 0.816, and the condenser closes the cycle at 45.8 °C. Points 3 and 4 nearly coincide because the pump work is only 4.03 kJ/kg.',
          'T-s diagram with the saturation dome of water and a Rankine cycle: point 1 at 40 bar and 400 °C, a vertical expansion to point 2 at 45.8 °C with dryness 0.816, a horizontal condensing line to points 3 and 4, and the 40 bar heating line back to point 1.')


# ---- 6.6 reheat on T-s, and the regenerative plant layout ----
def f6():
    o = []
    x0, x1, y0, y1 = 80, 470, 62, 304
    fx = lambda s: x0 + (s - 0) / 9 * (x1 - x0); fy = lambda t: y1 - t / 550 * (y1 - y0)
    o.append(T(x0 - 4, 22, '(a) Reheat cycle on T-s', 15, 'start', INK, True))
    o.append(frame(x0, x1, y0, y1, fx, fy, [0, 3, 6, 9], [0, 250, 500], 's (kJ/kg·K)', 'T (°C)', grid=False))
    o.append(dome(fx, fy))
    hp = [(0.65, 46), (3.028, 275.6), (5.890, 275.6), (6.07, 300), (6.336, 350), (6.543, 400), (6.722, 450), (6.883, 500)]
    o.append(P([(fx(s), fy(t)) for s, t in hp], LV, 3))
    o.append(L(fx(6.883), fy(500), fx(6.883), fy(239.8), AC, 2.5))
    o.append(P([(fx(s), fy(t)) for s, t in [(6.883, 239.8), (7.125, 300), (7.467, 400), (7.764, 500)]], LV, 3))
    o.append(L(fx(7.764), fy(500), fx(7.764), fy(45.81), AC, 2.5))
    o.append(L(fx(6.883), fy(239.8), fx(6.883), fy(45.81), MUT, 1.8, '5 4'))
    o.append(L(fx(7.764), fy(45.81), fx(0.649), fy(45.81), NX, 3))
    o.append(dot(fx(6.883), fy(500), '1', -8, -2, anchor='end')); o.append(dot(fx(6.883), fy(239.8), '2', -8, 4, anchor='end'))
    o.append(dot(fx(7.764), fy(500), '3', 8, -2)); o.append(dot(fx(7.764), fy(45.81), '4', 8, -8))
    o.append(dot(fx(0.649), fy(45.81), '5, 6', -4, -10, anchor='end'))
    o.append(T(fx(6.883) - 6, fy(45.81) - 8, 'x = 0.831', 13, 'end', MUT)); o.append(T(fx(7.764) + 22, fy(45.81) - 8, 'x = 0.949', 13, 'start', AC, True))
    kx = 500
    o += [T(kx, 70, 'Steam 60 bar, 500 °C', 13, 'start', INK, True), T(kx, 90, 'reheat at 10 bar to 500 °C', 13, 'start', MUT),
          T(kx, 124, 'with reheat: η = 40.0%', 13, 'start', INK), T(kx, 142, sb('w', 'net') + '= 1514.6 kJ/kg', 13, 'start', MUT),
          T(kx, 176, 'no reheat (dashed):', 13, 'start', INK), T(kx, 194, 'η = 38.4%', 13, 'start', MUT), T(kx, 212, sb('w', 'net') + '= 1237.1 kJ/kg', 13, 'start', MUT)]
    # (b) layout
    yb = 370
    o.append(T(76, yb, '(b) Regenerative plant, one open heater, bleed at 5 bar', 15, 'start', INK, True))
    bx = lambda x, y, w, h, lines, f=PANEL, s=AC: boxt(x, y, w, h, lines, f, s, 14)
    o.append(bx(40, yb + 40, 120, 60, ['Boiler', '60 bar']))
    o.append(f'<path d="M260,{yb + 30} L380,{yb + 50} L380,{yb + 100} L260,{yb + 120} Z" style="fill:{PANEL};stroke:{AC};stroke-width:2"/>')
    o.append(T(320, yb + 80, 'Turbine', 14))
    o.append(bx(500, yb + 150, 150, 54, ['Condenser', '0.1 bar'], NXS, NX))
    o.append(bx(250, yb + 170, 140, 60, ['Open heater', '5 bar'], LVS, LV))
    o.append(bx(500, yb + 262, 100, 40, ['Pump 1']))
    o.append(bx(70, yb + 262, 100, 40, ['Pump 2']))
    o.append(L(160, yb + 70, 256, yb + 70, AC, 2, arrow='n')); o.append(T(208, yb + 62, '1', 14, bold=True))
    o.append(P([(380, yb + 92), (575, yb + 92), (575, yb + 146)], AC, 2)); o.append(L(575, yb + 120, 575, yb + 146, AC, 2, arrow='n'))
    o.append(T(392, yb + 84, '3', 14, 'start', INK, True)); o.append(T(480, yb + 84, '(1 − m) = 0.827 kg', 13, 'middle', INK))
    o.append(L(320, yb + 112, 320, yb + 166, LV, 2, arrow='l')); o.append(T(330, yb + 134, '2', 14, 'start', INK, True)); o.append(T(330, yb + 152, 'm = 0.173 kg', 13, 'start', LV))
    o.append(L(550, yb + 204, 550, yb + 258, AC, 2, arrow='n')); o.append(T(560, yb + 236, '4', 14, 'start', INK, True))
    o.append(P([(500, yb + 282), (440, yb + 282), (440, yb + 200), (394, yb + 200)], AC, 2)); o.append(L(420, yb + 200, 394, yb + 200, AC, 2, arrow='n'))
    o.append(T(452, yb + 252, '5', 14, 'start', INK, True))
    o.append(P([(250, yb + 200), (200, yb + 200), (200, yb + 282), (174, yb + 282)], AC, 2)); o.append(L(190, yb + 282, 174, yb + 282, AC, 2, arrow='n'))
    o.append(T(212, yb + 250, '6', 14, 'start', INK, True))
    o.append(L(120, yb + 262, 120, yb + 104, AC, 2, arrow='n')); o.append(T(108, yb + 188, '7', 14, 'end', INK, True))
    o.append(T(250, yb + 330, 'h₂ = 2774.8, h₅ = 192.30, h₆ = 640.09 kJ/kg; η = 40.8%', 13, 'start', MUT))
    return yb + 346, ''.join(o)


FIG[6] = (f6, '(a) The reheat example: steam expands from 1 to 2, is reheated at 10 bar from 2 to 3 and expands to 4, ending much drier (0.949) than the simple cycle’s dashed expansion (0.831). (b) The regenerative example: 0.173 kg of each kg is bled at 5 bar into the open heater, and each pressure level has its own pump.',
          'Top: T-s diagram with the water dome, a 60 bar heating line to 500 °C, expansion to 10 bar, reheat to 500 °C and expansion to 0.1 bar with dryness 0.949. Bottom: block diagram of boiler, turbine, condenser, pump 1, open feedwater heater and pump 2 with states 1 to 7, bled fraction 0.173.')


# ---- 6.7 R-134a cycle on the p-h chart ----
R134 = [(-30, 0.844, 160.8, 380.3), (-20, 1.327, 173.6, 386.6), (-10, 2.006, 186.7, 392.7), (0, 2.928, 200.0, 398.6), (10, 4.146, 213.6, 404.3),
        (20, 5.717, 227.5, 409.7), (30, 7.702, 241.7, 414.8), (40, 10.166, 256.4, 419.4), (50, 13.179, 271.6, 423.4), (60, 16.818, 287.5, 426.6),
        (70, 21.168, 304.3, 428.6), (80, 26.332, 322.4, 428.8), (90, 32.442, 342.9, 425.4), (100, 39.724, 373.3, 407.7), (101.06, 40.591, 388.6, 390.7)]
ISEN = [(2.006, 392.7), (3.0, 400.8), (4.0, 406.8), (5.0, 411.4), (6.0, 415.3), (7.0, 418.6), (8.0, 421.4), (9.0, 423.9), (10.166, 426.5)]


def f7():
    o = []
    x0, x1, y0, y1 = 80, 520, 40, 330
    fx = lambda h: x0 + (h - 150) / 300 * (x1 - x0)
    lg = lambda p: math.log10(p)
    fy = lambda p: y1 - (lg(p) - lg(0.8)) / (lg(50) - lg(0.8)) * (y1 - y0)
    o.append(frame(x0, x1, y0, y1, fx, fy, [150, 250, 350, 450], [1, 2, 5, 10, 20, 50], 'h (kJ/kg)', 'p (bar), log scale', grid=True))
    left = [(fx(hf), fy(p)) for t, p, hf, hg in R134]; right = [(fx(hg), fy(p)) for t, p, hf, hg in reversed(R134)]
    o.append(P(left + right, MUT, 2))
    pe, pc = 2.006, 10.166
    o.append(L(fx(256.4), fy(pe), fx(392.66), fy(pe), LV, 3))
    o.append(P([(fx(h), fy(p)) for p, h in ISEN], AC, 2.5))
    o.append(L(fx(426.48), fy(pc), fx(256.41), fy(pc), NX, 3))
    o.append(L(fx(256.41), fy(pc), fx(256.41), fy(pe), AC, 2.5, '7 5'))
    o.append(dot(fx(392.66), fy(pe), '1', 8, 16)); o.append(dot(fx(426.48), fy(pc), '2', 8, -6))
    o.append(dot(fx(256.41), fy(pc), '3', -8, -6, anchor='end')); o.append(dot(fx(256.41), fy(pe), '4', -8, 16, anchor='end'))
    o.append(T(fx(325), fy(pe) - 10, 'evaporator, −10 °C, 2.01 bar', 13, 'middle', LV))
    o.append(T(fx(340), fy(pc) - 10, 'condenser, 40 °C, 10.17 bar', 13, 'middle', NX))
    o.append(T(fx(262), fy(4.6), 'valve', 13, 'start', MUT)); o.append(T(fx(262), fy(3.9), 'h₃ = h₄', 13, 'start', MUT))
    o.append(T(fx(170), fy(25), 'liquid', 13, 'start', MUT)); o.append(T(fx(440), fy(1.3), 'vapour', 13, 'end', MUT))
    o.append(T(fx(330), fy(5), 'liquid +', 13, 'middle', MUT)); o.append(T(fx(330), fy(4.2), 'vapour', 13, 'middle', MUT))
    kx = 548
    o += [T(kx, 70, sb('q', 'L') + '= h₁ − h₄', 13, 'start', INK, True), T(kx, 88, '= 136.25 kJ/kg', 13, 'start', MUT),
          T(kx, 122, 'w = h₂ − h₁', 13, 'start', INK, True), T(kx, 140, '= 33.82 kJ/kg', 13, 'start', MUT),
          T(kx, 174, sb('q', 'H') + '= h₂ − h₃', 13, 'start', INK, True), T(kx, 192, '= 170.07 kJ/kg', 13, 'start', MUT),
          T(kx, 228, 'COP = 4.03', 14, 'start', INK, True), T(kx, 248, '(Carnot 5.26)', 13, 'start', MUT)]
    return 380, ''.join(o)


FIG[7] = (f7, 'The worked example’s R-134a cycle on the pressure-enthalpy chart. Evaporation and condensation are horizontal lines, throttling is a vertical line because h₃ = h₄, and every energy term is a horizontal length: the refrigerating effect is four times the compressor work, so the COP is 4.03.',
          'Pressure-enthalpy chart of R-134a with its saturation dome and a vapour compression cycle: point 1 at 2.01 bar and 392.7 kJ/kg, isentropic compression to point 2 at 10.17 bar and 426.5 kJ/kg, condensation to point 3 at 256.4 kJ/kg and a vertical throttling line to point 4.')


# ---- 6.8 the ammonia-water absorption plant, with the example's heat flows ----
def f8():
    o = []
    o.append(L(20, 196, 700, 196, MUT, 1.5, '6 5'))
    o.append(T(690, 186, 'high pressure', 13, 'end', MUT)); o.append(T(690, 216, 'low pressure', 13, 'end', MUT))
    o.append(boxt(60, 80, 170, 70, ['Generator', '120 °C'], LVS, LV, 14))
    o.append(boxt(470, 80, 170, 70, ['Condenser', '30 °C'], NXS, NX, 14))
    o.append(boxt(60, 260, 170, 70, ['Absorber', '30 °C'], NXS, NX, 14))
    o.append(boxt(470, 260, 170, 70, ['Evaporator', '−10 °C'], ACS, AC, 14))
    o.append(L(230, 115, 466, 115, AC, 2.5, arrow='n')); o.append(T(348, 106, 'ammonia vapour', 13, 'middle', INK))
    o.append(L(555, 150, 555, 256, AC, 2.5, arrow='n'))
    o.append(boxt(510, 182, 90, 30, ['valve'], PANEL, AC, 13))
    o.append(T(612, 238, 'liquid NH₃', 13, 'start', MUT))
    o.append(L(470, 295, 234, 295, AC, 2.5, arrow='n')); o.append(T(352, 286, 'ammonia vapour', 13, 'middle', INK))
    # solution loop
    o.append(L(110, 260, 110, 154, LV, 2.5, arrow='l'))
    o.append(boxt(66, 200, 88, 30, ['pump'], PANEL, LV, 13))
    o.append(T(104, 248, 'strong', 13, 'end', LV))
    o.append(L(180, 154, 180, 256, MUT, 2.5, arrow='m'))
    o.append(boxt(150, 174, 60, 26, ['HX'], PANEL, MUT, 13))
    o.append(T(188, 247, 'weak', 13, 'start', MUT))
    # heat flows
    o.append(L(145, 18, 145, 76, LV, 3, arrow='l')); o.append(T(155, 36, sb('Q', 'G') + '= 16.7 kW in', 14, 'start', LV, True))
    o.append(L(555, 76, 555, 22, NX, 3, arrow='x')); o.append(T(565, 36, sb('Q', 'C') + ' out', 14, 'start', NX, True))
    o.append(L(145, 334, 145, 384, NX, 3, arrow='x')); o.append(T(160, 374, sb('Q', 'A') + ' out', 14, 'start', NX, True))
    o.append(L(555, 386, 555, 334, AC, 3, arrow='n')); o.append(T(565, 374, sb('Q', 'E') + '= 10 kW in', 14, 'start', AC, True))
    o.append(T(360, 420, sb('Q', 'C') + '+ ' + sb('Q', 'A') + '= 16.7 + 10 = 26.7 kW to the cooling water;  COP = 0.6', 13, 'middle', INK, True))
    return 436, ''.join(o)


FIG[8] = (f8, 'The ammonia-water plant of the first worked example. The right half is the same as a compression refrigerator; on the left, the absorber, pump and generator do the compressor’s job, driven by 16.7 kW of heat at 120 °C. The strong solution is pumped up through the heat exchanger (HX) and the weak solution runs back down.',
          'Block diagram: generator and condenser on the high-pressure side, absorber and evaporator on the low-pressure side. Ammonia vapour flows from generator to condenser, liquid through a valve to the evaporator, vapour to the absorber; a pump lifts strong solution to the generator and weak solution returns through a heat exchanger. Heat in: 16.7 kW at the generator and 10 kW at the evaporator.')


spec = make_spec(FIG)
