"""Claude's hand-drawn figures for ei-sensor-u4 (piezoelectric, Hall effect and optical sensors), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
AFTER = {1: 3, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 3, 9: 1, 10: 2, 11: 3}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def sp(base, s, size=11):
    return f'{base}<tspan baseline-shift="super" font-size="{size}">{s}</tspan>'


def cap_v(x, ytop, ybot, c=INK, w=22):
    """vertical capacitor between ytop and ybot at x (plates in the middle)"""
    ym = (ytop + ybot) / 2
    return (L(x, ytop, x, ym - 5, c, 1.8) + L(x, ym + 5, x, ybot, c, 1.8)
            + L(x - w / 2, ym - 5, x + w / 2, ym - 5, c, 3) + L(x - w / 2, ym + 5, x + w / 2, ym + 5, c, 3))


def cap_h(x1, x2, y, c=INK, h=22):
    xm = (x1 + x2) / 2
    return (L(x1, y, xm - 5, y, c, 1.8) + L(xm + 5, y, x2, y, c, 1.8)
            + L(xm - 5, y - h / 2, xm - 5, y + h / 2, c, 3) + L(xm + 5, y - h / 2, xm + 5, y + h / 2, c, 3))


def res_v(x, ytop, ybot, c=INK, n=6, amp=7):
    ym1, ym2 = ytop + (ybot - ytop) * 0.25, ybot - (ybot - ytop) * 0.25
    pts = [(x, ytop), (x, ym1)]
    for i in range(n):
        pts.append((x + (amp if i % 2 == 0 else -amp), ym1 + (ym2 - ym1) * (i + 0.5) / n))
    pts += [(x, ym2), (x, ybot)]
    return P(pts, c, 1.8)


def res_h(x1, x2, y, c=INK, n=6, amp=7):
    xm1, xm2 = x1 + (x2 - x1) * 0.25, x2 - (x2 - x1) * 0.25
    pts = [(x1, y), (xm1, y)]
    for i in range(n):
        pts.append((xm1 + (xm2 - xm1) * (i + 0.5) / n, y + (amp if i % 2 == 0 else -amp)))
    pts += [(xm2, y), (x2, y)]
    return P(pts, c, 1.8)


def gnd(x, y, c=INK):
    return L(x - 12, y, x + 12, y, c, 2) + L(x - 7, y + 5, x + 7, y + 5, c, 2) + L(x - 3, y + 10, x + 3, y + 10, c, 2)


def dot(x, y, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" style="fill:{c}"/>'


def opamp(x, y, w=70, h=76):
    """triangle with inputs on the left at y-h/4 (minus) and y+h/4 (plus); output tip at (x+w, y)"""
    pts = f'{x:.1f},{y - h / 2:.1f} {x + w:.1f},{y:.1f} {x:.1f},{y + h / 2:.1f}'
    return (f'<polygon points="{pts}" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>'
            + T(x + 12, y - h / 4 + 5, '−', 16, bold=True) + T(x + 12, y + h / 4 + 6, '+', 16, bold=True))


# ---- 4.1 the quartz disc of the worked example read by a charge amplifier ----
def f1():
    o = [T(20, 26, 'Quartz disc: A = 2 cm², t = 1 mm, d = 2.3 pC/N', 15, 'start', bold=True)]
    # the disc under force
    o.append(L(95, 52, 95, 98, NX, 3, arrow='x'))
    o.append(T(108, 74, 'F = 10 N', 14, 'start', NX, bold=True))
    o.append(R(45, 104, 100, 8, INK, INK, 1, 1))
    o.append(R(45, 112, 100, 34, ACS, AC, 2, 2))
    o.append(R(45, 146, 100, 8, INK, INK, 1, 1))
    o.append(T(95, 134, 'quartz', 13))
    o.append(T(95, 178, 'q = d F = 23 pC', 14, bold=True))
    o.append(T(95, 198, sb('C', 'c') + ' = 7.97 pF', 14))
    o.append(T(95, 218, 'open circuit: 2.89 V', 14))
    # equivalent circuit
    top, bot = 170, 300
    o.append(T(420, 58, 'Equivalent circuit, cable and charge amplifier', 14, bold=True))
    o.append(L(230, top, 520, top, INK, 1.8))
    o.append(L(230, bot, 520, bot, INK, 1.8))
    # charge source
    o.append(L(230, top, 230, 214, INK, 1.8) + L(230, 256, 230, bot, INK, 1.8))
    o.append(f'<circle cx="230" cy="235" r="20" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
    o.append(L(230, 247, 230, 224, AC, 2, arrow='n'))
    o.append(T(230, 330, 'q', 14, bold=True))
    o.append(cap_v(296, top, bot)); o.append(T(296, 330, sb('C', 'c'), 14))
    o.append(res_v(352, top, bot)); o.append(T(352, 330, 'R', 14))
    o.append(cap_v(430, top, bot, NX)); o.append(T(430, 330, 'cable ' + sb('C', 'k') + ' 100 pF', 13, fill=NX))
    for x in (296, 352, 430):
        o.append(dot(x, top)); o.append(dot(x, bot))
    o.append(gnd(470, bot + 1))
    # op-amp
    ox, oy = 540, 186
    o.append(L(520, top, 540, top, INK, 1.8))
    o.append(opamp(ox, oy))
    o.append(L(540, 205, 528, 205, INK, 1.8) + L(528, 205, 528, bot, INK, 1.8) + L(520, bot, 528, bot, INK, 1.8))
    o.append(dot(520, top))
    # feedback Cf and Rf
    o.append(L(520, top, 520, 118, INK, 1.8))
    o.append(L(520, 118, 520, 84, INK, 1.8))
    o.append(cap_h(520, 640, 118, LV)); o.append(T(580, 146, sb('C', 'f') + ' = 100 pF', 13, fill=LV, bold=True))
    o.append(res_h(520, 640, 84, INK)); o.append(T(580, 66, sb('R', 'f'), 13))
    o.append(L(640, 84, 640, oy, INK, 1.8))
    o.append(L(610, oy, 690, oy, INK, 1.8)); o.append(dot(640, oy))
    o.append(T(700, oy + 34, sb('V', 'out') + ' = −0.23 V', 14, 'end', LV, bold=True))
    # comparison box
    o.append(boxt(20, 352, 330, 66, ['voltage amplifier: 23 pC / (7.97 + 100) pF', '= 0.213 V, set by the cable'], NXS, NX, 14))
    o.append(boxt(370, 352, 330, 66, ['charge amplifier: −q / ' + sb('C', 'f') + ' = −23 / 100', '= −0.23 V, cable has no effect'], LVS, LV, 14))
    return 432, ''.join(o)
FIG[1] = (f1, 'The 10 N force on the quartz disc gives 23 pC on a 7.97 pF crystal. Through 100 pF of cable a voltage amplifier sees only 0.213 V, but the charge amplifier holds its input at virtual ground and gives −q/C<sub>f</sub> = −0.23 V whatever the cable.',
          'A quartz disc under a 10 newton force, its equivalent circuit of charge source, crystal capacitance and leakage resistance, a 100 picofarad cable, and a charge amplifier with a 100 picofarad feedback capacitor giving minus 0.23 volts.')


# ---- 4.2 pulse-echo timing of the parking sensor ----
def burst(x0, y0, w, amp, cycles, c):
    pts = [(x0 + w * i / (cycles * 12), y0 - amp * math.sin(2 * math.pi * i / 12)) for i in range(cycles * 12 + 1)]
    return P(pts, c, 2)


def f2():
    o = [T(20, 26, '40 kHz parking sensor in air, v = 343 m/s', 15, 'start', bold=True)]
    # scene
    o.append(R(30, 60, 64, 70, ACS, AC, 6, 2)); o.append(T(62, 100, 'sensor', 13))
    o.append(R(640, 46, 26, 100, 'var(--line)', L2, 0, 1.5)); o.append(T(653, 166, 'obstacle', 13))
    for r in (16, 30, 44):
        o.append(f'<path d="M{94 + r:.1f},{95 - r * 0.8:.1f} Q{94 + r * 1.35:.1f},95 {94 + r:.1f},{95 + r * 0.8:.1f}" style="fill:none;stroke:var(--accent);stroke-width:2"/>')
    o.append(L(150, 80, 630, 80, AC, 2, arrow='n')); o.append(Tb(390, 75, 'pulse out', 13, fill=AC))
    o.append(L(630, 112, 104, 112, LV, 2, arrow='l')); o.append(Tb(390, 117, 'echo back', 13, fill=LV))
    o.append(L(94, 176, 640, 176, MUT, 1.5)); o.append(L(94, 168, 94, 184, MUT, 1.5)); o.append(L(640, 168, 640, 184, MUT, 1.5))
    o.append(Tb(367, 181, 'd = v t / 2 = 343 × 0.012 / 2 = 2.058 m', 14, fill=INK, bold=True))
    # time axis 0..14 ms
    x0, x1, ya = 60, 670, 340
    fx = lambda ms: x0 + ms / 14 * (x1 - x0)
    o.append(T(20, 222, 'Receiver signal against time (bursts drawn with fewer cycles)', 14, 'start', bold=True))
    o.append(xaxis(x0, x1, ya, [0, 2, 4, 6, 8, 10, 12, 14], fx, 'time (ms)'))
    o.append(burst(fx(0), ya - 32, fx(1) - fx(0), 22, 8, AC)); o.append(T(fx(0.5), ya - 62, 'sent', 13, fill=AC))
    o.append(burst(fx(12), ya - 32, fx(13) - fx(12), 10, 8, LV)); o.append(T(fx(12.5), ya - 62, 'echo', 13, fill=LV))
    o.append(L(fx(0), ya - 32, fx(13.6), ya - 32, L2, 1, '3 4'))
    o.append(L(fx(0), ya - 92, fx(12), ya - 92, INK, 1.6))
    o.append(L(fx(0), ya - 98, fx(0), ya - 86, INK, 1.6)); o.append(L(fx(12), ya - 98, fx(12), ya - 86, INK, 1.6))
    o.append(Tb(fx(6), ya - 87, 'time of flight t = 12 ms', 14, fill=INK, bold=True))
    o.append(brace(fx(0), fx(1), ya + 50))
    o.append(T(fx(0) + 4, ya + 72, 'pulse τ = 1.0 ms: targets closer than v τ / 2 = 0.17 m merge into one echo', 13, 'start', MUT))
    o.append(T(fx(0) + 4, ya + 92, 'wavelength λ = v / f = 343 / 40 000 = 8.58 mm', 13, 'start', MUT))
    return ya + 104, ''.join(o)
FIG[2] = (f2, 'The pulse goes to the obstacle and back, so the 12 ms time of flight covers 2d and the obstacle is 2.058 m away. The 1.0 ms pulse length sets the range resolution of 0.17 m.',
          'A parking sensor sends an ultrasonic pulse to an obstacle 2.058 metres away; below, the received signal against time shows the sent burst at zero and the echo at 12 milliseconds.')


# ---- 4.3 amplitude ratio against frequency ratio, with the two worked examples marked ----
def Hf(r, z):
    return 1 / math.sqrt((1 - r * r) ** 2 + (2 * z * r) ** 2)


def f3():
    o = []
    x0, x1, y0, y1 = 70, 470, 50, 300
    fx = lambda r: x0 + r / 2.0 * (x1 - x0)
    fy = lambda h: y1 - h / 5.2 * (y1 - y0)
    o.append(R(fx(0), y0, fx(0.4) - fx(0), y1 - y0, LVS, 'none', 0, 0))
    o.append(T(fx(0.2), fy(3.6), 'accelerometer', 13, fill=LV, bold=True))
    o.append(T(fx(0.2), fy(3.6) + 16, 'band', 13, fill=LV, bold=True))
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 1.0, 1.5, 2.0], [0, 1, 2, 3, 4, 5], fx, fy, 'frequency ratio r = f / fₙ', 'amplitude ratio H', lambda v: f'{v:.1f}', str))
    for z, col, lab, ly in ((0.1, NX, 'ζ = 0.1', 4.6), (0.7, AC, 'ζ = 0.7', 0.5)):
        pts = [(fx(i / 200 * 2), fy(min(Hf(i / 200 * 2, z), 5.2))) for i in range(201)]
        o.append(P(pts, col, 2.5))
    o.append(T(fx(1.0) + 10, fy(5.0) + 4, 'ζ = 0.1: peak 5.0 at r = 1', 13, 'start', NX, bold=True))
    o.append(T(fx(0.62), fy(0.55), 'ζ = 0.7', 13, 'start', AC, bold=True))
    for r, lab, dy in ((0.1, 'r = 0.1, H = 1.0002', -26), (0.314, 'r = 0.314, H = 0.9971', -12)):
        o.append(C(fx(r), fy(Hf(r, 0.7)), 5, INK))
    o.append(L(fx(0.1), fy(1.0) - 6, fx(0.6), fy(2.1), L2, 1.2))
    o.append(Tb(fx(0.62), fy(2.1) - 4, 'example 1: r = 0.1, H = 1.0002', 13, 'start', INK))
    o.append(L(fx(0.314), fy(1.0) - 6, fx(0.62), fy(1.6), L2, 1.2))
    o.append(Tb(fx(0.64), fy(1.6) + 10, 'example 2: r = 0.314, H = 0.9971', 13, 'start', INK))
    # mass-spring-damper sketch
    bx, by = 520, 60
    o.append(R(bx, by, 170, 230, 'none', INK, 4, 2))
    o.append(T(bx + 85, by - 10, 'case on the machine', 13))
    o.append(R(bx + 45, by + 40, 80, 50, ACS, AC, 4, 2)); o.append(T(bx + 85, by + 70, 'm = 10 g', 14, bold=True))
    sx = bx + 60
    pts = [(sx, by + 90)] + [(sx + (9 if i % 2 == 0 else -9), by + 100 + i * 12) for i in range(8)] + [(sx, by + 196), (sx, by + 230)]
    o.append(P(pts, INK, 2))
    o.append(T(sx - 12, by + 160, 'k', 14, 'end', bold=True))
    dx = bx + 110
    o.append(L(dx, by + 90, dx, by + 140, INK, 2)); o.append(R(dx - 12, by + 140, 24, 40, 'none', INK, 1, 2))
    o.append(L(dx - 8, by + 150, dx + 8, by + 150, INK, 2)); o.append(L(dx, by + 180, dx, by + 230, INK, 2))
    o.append(T(dx + 18, by + 166, 'c', 14, 'start', bold=True))
    o.append(T(bx + 85, by + 260, 'k = 4 × 10⁶ N/m, c = 280 N·s/m', 13))
    o.append(T(bx + 85, by + 278, 'fₙ = 3183 Hz, ζ = 0.7', 13))
    o.append(L(bx + 30, by + 44, bx + 30, by + 86, LV, 2, arrow='l')); o.append(T(bx + 24, by + 70, 'z', 14, 'end', LV, bold=True))
    return 356, ''.join(o)
FIG[3] = (f3, 'The amplitude ratio H against r = f/f<sub>n</sub>. With ζ = 0.7 the curve stays within 1 % of 1 up to r ≈ 0.4, the accelerometer band; both worked examples sit inside it. With ζ = 0.1 the peak at resonance reaches 5.0.',
          'Plot of amplitude ratio against frequency ratio for damping ratios 0.1 and 0.7, with the flat accelerometer band shaded and the two worked example points marked, beside a sketch of a 10 gram seismic mass on a spring and damper inside a case.')


# ---- 4.4 the Hall plate and the clamp-on current sensor ----
def f4():
    o = [T(20, 26, 'InSb plate, t = 0.1 mm, B = 0.2 T into the page', 15, 'start', bold=True)]
    px, py, pw, ph = 90, 70, 260, 130
    o.append(R(px, py, pw, ph, ACS, AC, 4, 2))
    for i in range(4):
        for j in range(2):
            cx, cy = px + 40 + i * 60, py + 38 + j * 54
            o.append(f'<circle cx="{cx}" cy="{cy}" r="9" style="fill:none;stroke:{MUT};stroke-width:1.5"/>')
            o.append(L(cx - 6, cy - 6, cx + 6, cy + 6, MUT, 1.5) + L(cx + 6, cy - 6, cx - 6, cy + 6, MUT, 1.5))
    o.append(L(20, py + ph / 2, px - 4, py + ph / 2, NX, 3, arrow='x'))
    o.append(L(px + pw + 4, py + ph / 2, px + pw + 34, py + ph / 2, NX, 3, arrow='x'))
    o.append(T(20, py + ph / 2 - 12, 'I = 10 mA', 13, 'start', NX, bold=True))
    for i in range(6):
        o.append(T(px + 22 + i * 43, py + 16, '−', 18, fill=AC, bold=True))
        o.append(T(px + 22 + i * 43, py + ph - 4, '+', 16, fill=LV, bold=True))
    o.append(L(px + 130, py + ph / 2 + 22, px + 130, py + 26, AC, 2, '4 3', arrow='n'))
    o.append(T(px + pw - 40, py + ph + 44, 'electrons pushed', 13, 'start', AC))
    o.append(T(px + pw - 40, py + ph + 60, 'to the top edge', 13, 'start', AC))
    o.append(L(px + pw / 2, py, px + pw / 2, py - 18, INK, 1.8)); o.append(L(px + pw / 2, py + ph, px + pw / 2, py + ph + 18, INK, 1.8))
    o.append(boxt(px + 60, py + ph + 24, 120, 40, [sb('V', 'H') + ' = 7.6 mV'], LVS, LV, 14))
    o.append(T(20, py + ph + 96, sb('V', 'H') + ' = ' + sb('R', 'H') + ' I B / t = 3.8×10⁻⁴ × 0.01 × 0.2 / 10⁻⁴', 13, 'start'))
    o.append(T(20, py + ph + 116, 'sensitivity S = ' + sb('V', 'H') + ' / B = 38 mV/T', 13, 'start'))
    # clamp-on current sensor
    cx, cy, rr = 540, 160, 82
    o.append(T(410, 26, 'Clamp-on current sensor', 15, 'start', bold=True))
    gap = 10  # degrees each side of the gap
    a1, a2 = math.radians(gap), math.radians(360 - gap)
    outer, inner = rr, rr - 22
    pth = (f'M{cx + outer * math.cos(a1):.1f},{cy - outer * math.sin(a1):.1f} A{outer},{outer} 0 1 0 {cx + outer * math.cos(a2):.1f},{cy - outer * math.sin(a2):.1f} '
           f'L{cx + inner * math.cos(a2):.1f},{cy - inner * math.sin(a2):.1f} A{inner},{inner} 0 1 1 {cx + inner * math.cos(a1):.1f},{cy - inner * math.sin(a1):.1f} Z')
    o.append(f'<path d="{pth}" style="fill:var(--line);stroke:var(--line2);stroke-width:1.5"/>')
    o.append(R(cx + inner + 4, cy - 7, 14, 14, AC, AC, 1, 1))
    o.append(L(cx + inner + 11, cy - 10, cx + inner + 11, cy - 46, AC, 1.5)); o.append(T(cx + inner + 18, cy - 50, 'Hall plate in', 13, 'start', AC))
    o.append(T(cx + inner + 18, cy - 34, 'the 2 mm gap', 13, 'start', AC))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="16" style="fill:var(--panel);stroke:var(--next);stroke-width:2"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="4" style="fill:var(--next)"/>')
    o.append(T(cx, cy + rr + 20, 'cable: I = 50 A out of the page', 13, fill=NX, bold=True))
    o.append(T(410, 290, 'B = μ₀ I / g = 4π×10⁻⁷ × 50 / 0.002 = 31.4 mT', 13, 'start'))
    o.append(T(410, 310, sb('V', 'H') + ' = 38 mV/T × 0.0314 T = 1.19 mV', 13, 'start'))
    o.append(T(410, 330, 'gain 500: 0.597 V, so 11.9 mV per ampere', 13, 'start', LV, bold=True))
    return 344, ''.join(o)
FIG[4] = (f4, 'Left: with the current to the right and B into the page, the electrons are pushed to the top edge, so the plate of the first example gives V<sub>H</sub> = 7.6 mV across its width. Right: the same plate in the 2 mm gap of a ferrite ring reads a 50 A cable without touching it.',
          'A Hall plate with current flowing to the right in a field into the page, electrons collecting on the top edge and a Hall voltage of 7.6 millivolts across the width; beside it a ferrite ring with a 2 millimetre gap around a cable carrying 50 amperes, giving 31.4 millitesla in the gap.')


# ---- 4.5 the magnetostrictive position sensor of the second example, and the Terfenol-D rod ----
def f5():
    o = [T(20, 26, 'Magnetostrictive position sensor, wave speed 2800 m/s', 15, 'start', bold=True)]
    y = 110
    o.append(R(30, y - 34, 90, 68, ACS, AC, 6, 2)); o.append(T(75, y - 6, 'head:', 13, bold=True)); o.append(T(75, y + 12, 'pickup', 13))
    o.append(R(120, y - 12, 560, 24, PANEL, L2, 12, 1.5))
    o.append(L(120, y, 680, y, INK, 2))
    mx = 120 + 0.70 / 0.85 * 540
    o.append(R(mx - 14, y - 30, 28, 60, NXS, NX, 6, 2)); o.append(T(mx, y + 50, 'ring magnet', 13, fill=NX, bold=True))
    o.append(L(140, y - 50, mx - 30, y - 50, AC, 2, arrow='n')); o.append(Tb((140 + mx) / 2, y - 45, 'current pulse out along the wire', 13, fill=AC))
    pts = [(mx - 20 - i * 3, y + 22 + 5 * math.sin(i / 2.0)) for i in range(0, int((mx - 160) / 3))]
    o.append(P(pts, LV, 2)); o.append(L(pts[-1][0], pts[-1][1], 126, y + 22, LV, 2, arrow='l'))
    o.append(Tb((140 + mx) / 2, y + 48, 'twist pulse back', 13, fill=LV))
    o.append(L(120, y + 78, mx, y + 78, MUT, 1.5)); o.append(L(120, y + 70, 120, y + 86, MUT, 1.5)); o.append(L(mx, y + 70, mx, y + 86, MUT, 1.5))
    o.append(Tb((120 + mx) / 2, y + 83, 'x = v t = 2800 × 250 µs = 0.70 m', 14, fill=INK, bold=True))
    o.append(T(30, y + 112, 'A 100 MHz timer counts 10 ns steps: 2800 m/s × 10 ns = 28 µm per count.', 13, 'start', MUT))
    # Terfenol rod
    y2 = 290
    o.append(T(20, y2 - 34, 'Terfenol-D rod of the first example', 15, 'start', bold=True))
    o.append(R(60, y2, 300, 34, 'var(--line)', L2, 4, 1.5)); o.append(T(210, y2 + 60, 'L = 50 mm', 14, bold=True))
    o.append(R(360, y2, 18, 34, LVS, LV, 2, 1.5))
    for i in range(9):
        xx = 80 + i * 32
        o.append(f'<ellipse cx="{xx}" cy="{y2 + 17}" rx="7" ry="24" style="fill:none;stroke:var(--accent);stroke-width:1.8"/>')
    o.append(T(388, y2 + 14, 'ΔL = λ L', 14, 'start', LV, bold=True))
    o.append(T(388, y2 + 32, '= 1200 × 10⁻⁶ × 50 mm = 60 µm', 14, 'start', LV, bold=True))
    o.append(T(60, y2 + 86, 'coil current sets H (with a bias); the rod grows by 1200 ppm (drawn much enlarged)', 13, 'start', MUT))
    return y2 + 100, ''.join(o)
FIG[5] = (f5, 'Top: the current pulse meets the ring magnet\'s field and the Wiedemann effect sends a twist back along the wire; a 250 µs return at 2800 m/s puts the magnet 0.70 m from the head. Bottom: the 50 mm Terfenol-D rod grows by 60 µm at 1200 ppm.',
          'A magnetostrictive position sensor with a head, a waveguide wire in a tube, a ring magnet 0.70 metres along, a current pulse going out and a twist pulse coming back; below, a 50 millimetre Terfenol-D rod in a coil that lengthens by 60 micrometres.')


# ---- 4.6 the fibre of the second example and the link of the first ----
def f6():
    o = [T(20, 26, 'Fibre: core 1.50, cladding 1.45 (thickness enlarged)', 15, 'start', bold=True)]
    xa, xb, yc, hc = 150, 700, 130, 64
    o.append(R(xa, yc - hc / 2 - 34, xb - xa, hc + 68, PANEL, L2, 0, 1.5))
    o.append(R(xa, yc - hc / 2, xb - xa, hc, ACS, AC, 0, 1.5))
    o.append(T(xb - 8, yc - hc / 2 - 12, 'cladding n₂ = 1.45', 13, 'end', MUT))
    o.append(T(xb - 8, yc + hc / 2 + 24, 'cladding n₂ = 1.45', 13, 'end', MUT))
    o.append(T(xb - 8, yc + 5, 'core n₁ = 1.50', 13, 'end', AC, bold=True))
    o.append(L(40, yc, xb, yc, L2, 1, '5 5'))
    th_in = math.radians(14.8); th_a = math.radians(22.6)
    # incoming ray in air at 22.6 deg, hitting the axis point at the end face
    L0 = 110
    o.append(L(xa - L0 * math.cos(th_a), yc + L0 * math.sin(th_a), xa, yc, LV, 2.5))
    o.append(L(xa - L0 * math.cos(th_a), yc - L0 * math.sin(th_a), xa, yc, LV, 1.5, '6 4'))
    o.append(T(xa - 70, yc + 66, 'acceptance cone', 13, fill=LV))
    o.append(T(xa - 70, yc + 82, sb('θ', 'a') + ' = 22.6°', 13, fill=LV, bold=True))
    # zig-zag inside the core
    x, y, s = xa, yc, -1
    pts = [(x, y)]
    while x < xb - 140:
        dy = (hc / 2) if len(pts) == 1 else hc
        nx = x + dy / math.tan(th_in)
        if nx > xb - 140: nx = xb - 140; ny = y + s * (nx - x) * math.tan(th_in)
        else: ny = y + s * dy
        pts.append((nx, ny)); x, y, s = nx, ny, -s
    o.append(P(pts, LV, 2.5))
    bx, byy = pts[1]
    o.append(L(bx, byy, bx, byy + 46, INK, 1.2, '3 3'))
    o.append(T(bx + 6, byy + 62, 'normal', 13, 'start', MUT))
    o.append(T(bx + 14, byy - 8, 'meets the wall 75.2° from the normal (more than ' + sb('θ', 'c') + ')', 13, 'start', INK))
    o.append(T(40, 232, 'NA = √(1.50² − 1.45²) = 0.384;  ' + sb('θ', 'a') + ' = sin⁻¹ 0.384 = 22.6°;  ' + sb('θ', 'c') + ' = sin⁻¹(1.45 / 1.50) = 75.2°', 13, 'start'))
    # link
    y3 = 300
    o.append(T(20, y3 - 26, 'Link of the first example', 15, 'start', bold=True))
    o.append(boxt(30, y3, 120, 44, ['LED 1 mW'], ACS, AC, 14))
    o.append(L(150, y3 + 22, 560, y3 + 22, AC, 4))
    o.append(Tb(355, y3 + 27, '2 km of fibre', 13, fill=AC))
    o.append(boxt(560, y3, 140, 44, ['received 0.2 mW'], LVS, LV, 14))
    o.append(T(355, y3 + 72, 'loss = 10 log₁₀(1 / 0.2) = 6.99 dB, that is 3.49 dB/km', 14, bold=True))
    return y3 + 88, ''.join(o)
FIG[6] = (f6, 'Light that enters within 22.6° of the axis meets the core wall at 75.2° from the normal, beyond the critical angle, and is trapped by total internal reflection. Below: 1 mW in and 0.2 mW out after 2 km is a 6.99 dB loss.',
          'Longitudinal section of an optical fibre with a ray entering inside the 22.6 degree acceptance cone and reflecting along the core, with the critical angle of 75.2 degrees marked; below, a 2 kilometre link from a 1 milliwatt LED to a 0.2 milliwatt receiver.')


# ---- 4.7 quadrature counting and the Gray code ----
def f7():
    o = [T(20, 26, 'Quadrature: B leads A by a quarter cycle (count up)', 15, 'start', bold=True)]
    x0, pw = 70, 160  # one slot pitch = 160 px
    ya, yb, hh = 80, 150, 34
    def wave(y, shift):
        pts = []
        lvl = None
        xs = [x0 + shift + i * pw / 2 for i in range(-1, 6)]
        cur = 0
        pts.append((x0, y))
        x = x0
        edges = sorted([x0 + shift + i * pw / 2 for i in range(0, 5)])
        state = 0
        for e in edges:
            if e < x0 or e > x0 + 2 * pw + 10: continue
            pts.append((e, y - state * hh)); state = 1 - state; pts.append((e, y - state * hh))
        pts.append((x0 + 2.2 * pw, y - state * hh))
        return P(pts, AC, 2.5)
    o.append(T(x0 - 14, ya - 10, 'A', 15, 'end', bold=True)); o.append(T(x0 - 14, yb - 10, 'B', 15, 'end', bold=True))
    o.append(wave(ya, pw / 4 + pw / 4))
    o.append(wave(yb, pw / 4))
    edges = [x0 + pw / 4 + i * pw / 4 for i in range(8)]
    states = ['00', '01', '11', '10', '00', '01', '11', '10']
    for i, e in enumerate(edges):
        o.append(L(e, 40, e, 196, L2, 1, '3 3'))
        o.append(T(e, 216, str(i + 1), 13, fill=LV, bold=True))
    o.append(T(x0 - 14, 216, 'count', 13, 'end', LV))
    for i in range(8):
        xm = (edges[i] + (edges[i + 1] if i < 7 else edges[i] + pw / 4)) / 2
        o.append(T(xm, 240, states[(i + 1) % 4] if False else ['01', '11', '10', '00', '01', '11', '10', '00'][i], 13, fill=MUT))
    o.append(T(x0 - 14, 240, 'AB', 13, 'end', MUT))
    o.append(L(x0, 260, x0 + pw, 260, INK, 1.5)); o.append(L(x0, 254, x0, 266, INK, 1.5)); o.append(L(x0 + pw, 254, x0 + pw, 266, INK, 1.5))
    o.append(T(x0 + pw / 2, 280, 'one slot: 4 counts', 13, bold=True))
    o.append(T(x0, 306, '1000 slots × 4 = 4000 counts per turn,', 13, 'start')); o.append(T(x0, 324, '360° / 4000 = 0.09° per count', 13, 'start'))
    # Gray code table
    tx = 470
    o.append(T(tx, 52, 'pos', 13, 'start', MUT, bold=True)); o.append(T(tx + 60, 52, 'binary', 13, 'start', MUT, bold=True)); o.append(T(tx + 140, 52, 'Gray', 13, 'start', AC, bold=True))
    for p in range(8):
        g = p ^ (p >> 1)
        yy = 76 + p * 26
        o.append(T(tx + 10, yy, str(p), 14, 'start'))
        o.append(TM(tx + 60, yy, format(p, '03b'), 14, 'start'))
        o.append(TM(tx + 140, yy, format(g, '03b'), 14, 'start', AC, bold=True))
    o.append(R(tx - 8, 60, 220, 212, 'none', L2, 6, 1.2))
    o.append(T(tx - 8, 292, 'binary 011 → 100 flips three bits;', 13, 'start', MUT))
    o.append(T(tx - 8, 310, 'Gray 010 → 110 flips one', 13, 'start', MUT))
    return 338, ''.join(o)
FIG[7] = (f7, 'Left: B rises a quarter cycle before A, so the decoder counts up at every one of the four edges per slot; 1000 slots give 4000 counts and 0.09° per count. Right: the 3-bit Gray code, where neighbouring positions differ in one bit only.',
          'Square waves of encoder channels A and B a quarter cycle apart with eight counted edges and the AB states, and a table of positions 0 to 7 in binary and Gray code.')


# ---- 4.8 frequency-to-voltage conversion of the gear pick-up ----
def f8():
    o = [T(20, 26, 'Gear pick-up to meter: 60 teeth, 250 Hz', 15, 'start', bold=True)]
    names = [('toothed wheel', '60 teeth'), ('pick-up', 'pulse per tooth'), ('monostable', 'T = 200 µs, 5 V'), ('RC average', 'filter'), ('meter', '0.25 V')]
    w, gap, y = 122, 22, 50
    for i, (a, b) in enumerate(names):
        x = 20 + i * (w + gap)
        o.append(boxt(x, y, w, 52, [a, b], LVS if i == 4 else PANEL, LV if i == 4 else AC, 13, bold_first=True))
        if i < 4: o.append(L(x + w, y + 26, x + w + gap - 2, y + 26, AC, 2, arrow='n'))
    # waveform
    x0, x1, yb = 70, 690, 270
    fx = lambda ms: x0 + ms / 16 * (x1 - x0)
    vy = lambda v: yb - v / 5 * 110
    o.append(T(20, 140, 'Monostable output (5 V pulses) and its average', 14, 'start', bold=True))
    o.append(xaxis(x0, x1, yb, [0, 4, 8, 12, 16], fx, 'time (ms)'))
    o.append(L(x0, yb, x0, vy(5.4), L2, 1.5))
    o.append(T(x0 - 8, vy(5) + 5, '5 V', 13, 'end', MUT))
    pts = [(x0, yb)]
    for k in range(4):
        a, b = fx(k * 4 + 1), fx(k * 4 + 1.2)
        pts += [(a, yb), (a, vy(5)), (b, vy(5)), (b, yb)]
    pts.append((x1, yb))
    o.append(P(pts, AC, 2))
    o.append(L(x0, vy(0.25), x1, vy(0.25), LV, 3))
    o.append(T(x1, vy(0.25) - 8, 'average 0.25 V', 13, 'end', LV, bold=True))
    o.append(L(fx(1.2), vy(2.6), fx(5), vy(2.6), INK, 1.5, arrow=None)); o.append(L(fx(5), vy(2.6) - 6, fx(5), vy(2.6) + 6, INK, 1.5))
    o.append(L(fx(1), vy(2.6), fx(1.2), vy(2.6), INK, 1.5))
    o.append(Tb(fx(3.1), vy(2.6) + 5, 'period 4 ms (250 Hz)', 13, fill=INK))
    o.append(T(fx(1.2) + 6, vy(4.0), '200 µs', 13, 'start', AC))
    o.append(T(x0, yb + 64, sb('V', 'out') + ' = ' + sb('V', 'ref') + ' T f = 5 × 200 µs × 250 Hz = 0.25 V;   n = 60 f / z = 60 × 250 / 60 = 250 rpm', 13, 'start', INK, bold=True))
    return yb + 78, ''.join(o)
FIG[8] = (f8, 'Each tooth fires one 200 µs, 5 V pulse, so at 250 Hz the pulses fill 5 % of the time and the filter gives 0.25 V. The pulse width is shorter than the 4 ms period, as the formula needs; the 60-tooth wheel then turns at 250 rpm.',
          'Block chain from a 60 tooth wheel through a pick-up, monostable and RC filter to a meter, and a plot of 5 volt pulses 200 microseconds wide every 4 milliseconds with their average of 0.25 volts.')


# ---- 4.9 the force-balance loop of the worked example ----
def f9():
    o = [T(20, 26, 'Force-balance pressure transmitter (beam barely moves)', 15, 'start', bold=True)]
    # beam
    o.append(R(80, 150, 330, 16, PANEL, INK, 3, 2))
    o.append(f'<polygon points="80,166 64,196 96,196" style="fill:var(--line);stroke:var(--line2);stroke-width:1.5"/>')
    o.append(T(80, 214, 'flexure pivot', 13))
    # diaphragm and input force
    o.append(R(180, 250, 120, 14, ACS, AC, 3, 2)); o.append(T(240, 290, 'diaphragm', 13))
    o.append(L(240, 248, 240, 172, NX, 3, arrow='x')); o.append(T(252, 222, 'F = 2 N', 14, 'start', NX, bold=True))
    # coil and magnet
    o.append(R(330, 70, 70, 50, 'var(--line)', L2, 4, 1.5)); o.append(T(365, 60, 'magnet B = 0.25 T', 13))
    o.append(R(345, 104, 40, 40, LVS, LV, 3, 2)); o.append(T(365, 130, 'coil', 13, fill=LV, bold=True))
    o.append(L(365, 146, 365, 148, LV, 2))
    o.append(L(440, 104, 440, 144, LV, 3, arrow='l')); o.append(T(450, 126, 'B I L = 2 N down', 13, 'start', LV, bold=True))
    # displacement sensor at the beam tip
    o.append(R(395, 176, 40, 26, PANEL, AC, 3, 2)); o.append(T(415, 222, 'gap sensor', 13))
    # amplifier
    o.append(L(435, 189, 500, 189, AC, 2, arrow='n'))
    o.append(f'<polygon points="505,160 565,189 505,218" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(530, 240, 'error amplifier', 13))
    o.append(L(565, 189, 600, 189, AC, 2))
    o.append(L(600, 189, 600, 90, LV, 2)); o.append(L(600, 90, 404, 90, LV, 2, arrow='l'))
    o.append(T(610, 150, 'I = 0.16 A', 14, 'start', LV, bold=True))
    o.append(L(600, 189, 600, 270, LV, 2, arrow='l'))
    o.append(boxt(520, 274, 180, 52, ['transmitter', '16.8 mA on 4 to 20 mA'], LVS, LV, 13, bold_first=True))
    o.append(T(20, 340, 'Balance: I = F / (B L) = 2 / (0.25 × 50) = 0.16 A, that is 0.08 A per newton', 14, 'start', bold=True))
    o.append(T(20, 362, 'Output: 4 + 16 × (2 / 2.5) = 16.8 mA for a 0 to 2.5 N range', 13, 'start', MUT))
    return 376, ''.join(o)
FIG[9] = (f9, 'The diaphragm pushes the beam up with 2 N; the gap sensor sees the first micrometres of motion, and the amplifier drives the coil until B I L also equals 2 N. The balance current of 0.16 A is the measurement, sent on as 16.8 mA.',
          'A pivoted beam pushed up by a diaphragm with 2 newtons, a coil in a 0.25 tesla magnet pulling it back, a gap sensor at the tip feeding an error amplifier, and the 0.16 ampere coil current going to a 4 to 20 milliampere transmitter.')


# ---- 4.10 photomultiplier gain, dynode by dynode ----
def f10():
    o = [T(20, 26, 'PMT of the worked example: 10 dynodes, δ = 4, 100 photoelectrons', 15, 'start', bold=True)]
    o.append(f'<path d="M60,70 Q40,130 60,190" style="fill:none;stroke:var(--accent);stroke-width:5"/>')
    o.append(T(50, 214, 'photocathode', 13))
    o.append(L(8, 100, 50, 118, NX, 2.5, arrow='x')); o.append(T(10, 90, 'light', 13, 'start', NX))
    xs = [110 + i * 52 for i in range(10)]
    ys = [180 if i % 2 == 0 else 80 for i in range(10)]
    prev = (64, 130)
    for i, (x, y) in enumerate(zip(xs, ys)):
        o.append(L(prev[0], prev[1], x, y + (-10 if y > 130 else 10), LV, 1.8, arrow='l'))
        o.append(R(x - 18, y - 6 if y < 130 else y - 6, 36, 12, ACS, AC, 3, 2))
        o.append(T(x, y + (30 if y > 130 else -14), f'D{i + 1}', 13, bold=True))
        prev = (x, y + (-6 if y > 130 else 6))
    o.append(R(640, 110, 14, 50, LVS, LV, 2, 2)); o.append(T(647, 186, 'anode', 13, fill=LV))
    o.append(L(prev[0], prev[1], 638, 130, LV, 1.8, arrow='l'))
    o.append(T(xs[0], 230, '400', 13, fill=MUT)); o.append(T(xs[1], 50, '1600', 13, fill=MUT))
    o.append(T(xs[4], 230, '1.0×10⁵', 13, fill=MUT)); o.append(T(xs[9] - 10, 50, '1.05×10⁸', 13, fill=MUT))
    o.append(T(20, 266, 'electrons leaving each dynode = 100 × 4ᵏ (shown for D1, D2, D5 and D10)', 13, 'start', MUT))
    o.append(T(20, 292, 'gain G = δⁿ = 4¹⁰ = 1 048 576;  anode electrons = 100 × G = 1.05 × 10⁸', 14, 'start', bold=True))
    o.append(T(20, 314, 'anode charge Q = 1.05 × 10⁸ × 1.6 × 10⁻¹⁹ C = 1.68 × 10⁻¹¹ C', 14, 'start', bold=True))
    o.append(T(20, 338, 'each dynode is held about 80 to 150 V above the one before it by a resistor divider', 13, 'start', MUT))
    return 352, ''.join(o)
FIG[10] = (f10, 'Each of the 10 dynodes multiplies the electrons by δ = 4, so the 100 photoelectrons of the example become 400 after D1, 1600 after D2 and 1.05 × 10⁸ at the anode: a gain of 4¹⁰ ≈ 1.05 × 10⁶ in many small steps.',
          'A photomultiplier tube with a curved photocathode, ten dynodes in a zigzag and an anode, with electron numbers growing from 400 after the first dynode to about 100 million at the anode.')


# ---- 4.11 spectrophotometer path, photodiode readout and calibration line ----
def f11():
    o = [T(20, 26, 'Spectrophotometer of the worked examples', 15, 'start', bold=True)]
    y = 46
    items = [('lamp', 'white light', PANEL, AC), ('monochromator', 'one λ', PANEL, AC), ('cuvette', 'l = 1.00 cm', ACS, AC), ('photodiode', '0.45 A/W', PANEL, AC), ('TIA', 'R_f 100 kΩ', LVS, LV)]
    w, gap = 112, 22
    for i, (a, b, f_, s_) in enumerate(items):
        x = 20 + i * (w + gap)
        bb = b.replace('R_f', sb('R', 'f'))
        o.append(boxt(x, y, w, 52, [a, bb], f_, s_, 13, bold_first=True))
        if i < 4: o.append(L(x + w, y + 26, x + w + gap - 2, y + 26, NX, 2.5, arrow='x'))
    o.append(T(20, 130, 'blank: 2.00 V → ' + sb('I', '0') + ' = 20 µA (44.4 µW);  sample: 1.00 V → I = 10 µA', 13, 'start'))
    o.append(T(20, 150, 'T = I / ' + sb('I', '0') + ' = 0.50,  A = −log₁₀ 0.50 = 0.301', 13, 'start', bold=True))
    # calibration line
    x0, x1, y0, y1 = 80, 420, 190, 360
    fx = lambda c: x0 + c / 3.5 * (x1 - x0)
    fy = lambda a: y1 - a / 0.55 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3], [0, 0.15, 0.30, 0.45], fx, fy, 'c (× 10⁻⁴ mol/L)', 'absorbance A', str, lambda v: f'{v:.2f}'))
    o.append(L(fx(0), fy(0), fx(3.5), fy(0.525), AC, 2.5))
    for cc in (1, 2, 3):
        o.append(C(fx(cc), fy(0.15 * cc), 5, AC))
    o.append(L(fx(0), fy(0.30), fx(2), fy(0.30), LV, 1.5, '5 4')); o.append(L(fx(2), fy(0.30), fx(2), fy(0), LV, 1.5, '5 4'))
    o.append(C(fx(2), fy(0.30), 6, LV))
    o.append(Tb(fx(2) + 12, fy(0.30) + 4, 'sample', 13, 'start', LV, bold=True))
    o.append(T(460, 220, 'Beer-Lambert: A = ε c l', 14, 'start', bold=True))
    o.append(T(460, 244, 'slope ε l = 1500 L/mol', 13, 'start'))
    o.append(T(460, 268, 'c = A / (ε l)', 13, 'start'))
    o.append(T(460, 288, '= 0.30 / 1500', 13, 'start'))
    o.append(T(460, 308, '= 2.0 × 10⁻⁴ mol/L', 14, 'start', LV, bold=True))
    return 410, ''.join(o)
FIG[11] = (f11, 'The photodiode current halves from 20 µA to 10 µA when the sample goes in, so T = 0.50 and A = 0.30. On the calibration line of slope ε l = 1500 L/mol that absorbance reads 2.0 × 10⁻⁴ mol/L.',
          'Block path from lamp through monochromator, cuvette, photodiode and transimpedance amplifier, with blank and sample readings, and a straight calibration line of absorbance against concentration where the sample at absorbance 0.30 reads 2.0 times ten to the minus 4 moles per litre.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
