"""Claude's hand-drawn figures for ei-sensor-u6 (signal conditioning, data acquisition, actuators, bridges, amplifiers, displays), one per chapter.
Every number comes from that chapter's worked examples. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
AFTER = {1: 1, 2: 1, 3: 2, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 2}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


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


def res_d(x1, y1, x2, y2, c=INK, n=6, amp=7, t0=0.25, t1=0.75):
    """resistor zig-zag along any line, between fractions t0 and t1 of its length"""
    dx, dy = x2 - x1, y2 - y1
    ln = math.hypot(dx, dy); nx, ny = -dy / ln, dx / ln
    pts = [(x1, y1), (x1 + dx * t0, y1 + dy * t0)]
    for i in range(n):
        t = t0 + (t1 - t0) * (i + 0.5) / n; s = amp if i % 2 == 0 else -amp
        pts.append((x1 + dx * t + nx * s, y1 + dy * t + ny * s))
    pts += [(x1 + dx * t1, y1 + dy * t1), (x2, y2)]
    return P(pts, c, 1.8)


def ind_d(x1, y1, x2, y2, c=INK, n=4, t0=0.25, t1=0.75):
    """inductor: n bumps along a line"""
    dx, dy = x2 - x1, y2 - y1
    ln = math.hypot(dx, dy); ux, uy = dx / ln, dy / ln; nx, ny = uy, -ux
    pts = [(x1, y1), (x1 + dx * t0, y1 + dy * t0)]
    seg = (t1 - t0) * ln / n; r = seg / 2
    for i in range(n):
        cx0 = x1 + dx * t0 + ux * (seg * i + r); cy0 = y1 + dy * t0 + uy * (seg * i + r)
        for j in range(13):
            a = math.pi - math.pi * j / 12
            pts.append((cx0 + ux * r * math.cos(a) + nx * r * math.sin(a), cy0 + uy * r * math.cos(a) + ny * r * math.sin(a)))
    pts += [(x1 + dx * t1, y1 + dy * t1), (x2, y2)]
    return P(pts, c, 1.8)


def cap_d(x1, y1, x2, y2, t, c=INK, gap=7, half=11):
    """capacitor plates across a line at fraction t (the line is broken there)"""
    dx, dy = x2 - x1, y2 - y1
    ln = math.hypot(dx, dy); ux, uy = dx / ln, dy / ln; nx, ny = -uy, ux
    mx, my = x1 + dx * t, y1 + dy * t
    a = (mx - ux * gap / 2, my - uy * gap / 2); b = (mx + ux * gap / 2, my + uy * gap / 2)
    return (L(x1, y1, a[0], a[1], c, 1.8) + L(b[0], b[1], x2, y2, c, 1.8)
            + L(a[0] - nx * half, a[1] - ny * half, a[0] + nx * half, a[1] + ny * half, c, 2.4)
            + L(b[0] - nx * half, b[1] - ny * half, b[0] + nx * half, b[1] + ny * half, c, 2.4))


def battery_v(x, y, c=INK, label=None):
    """vertical cell centred at (x, y): long plate (+) on top"""
    o = [L(x - 16, y - 5, x + 16, y - 5, c, 2.4), L(x - 9, y + 5, x + 9, y + 5, c, 3.2)]
    if label: o.append(T(x - 24, y + 5, label, 13, 'end', bold=True))
    return ''.join(o)


def dot(x, y, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" style="fill:{c}"/>'


def poly(pts, fill, stroke, w=2):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{w}"/>'


def logx(x0, x1, d0, d1):
    return lambda f: x0 + (x1 - x0) * (math.log10(f) - d0) / (d1 - d0)


# ---- signal conditioning: the chain of the worked example and its low-pass response ----
def f1():
    o = [T(20, 26, 'Each block repairs one defect of the raw signal', 15, 'start', bold=True)]
    xs = [12, 152, 292, 432, 572]
    boxes = [['Bridge sensor', '2 mV at', 'full load'], ['In-amp', 'G = 100 k / 200', '= 500 (54.0 dB)'], ['RC low-pass', '10 kΩ, 1 µF', sb('f', 'c') + ' = 15.9 Hz'],
             ['Linearise', 'table or', 'breakpoints'], ['Isolation', 'barrier', 'then ADC']]
    fills = [PANEL, ACS, ACS, PANEL, LVS]; strokes = [L2, AC, AC, L2, LV]
    for x, b, f, s in zip(xs, boxes, fills, strokes):
        o.append(boxt(x, 44, 124, 78, b, f, s, 13, bold_first=True))
    for x in xs[:-1]:
        o.append(L(x + 126, 83, x + 138, 83, AC, 2, arrow='n'))
    o.append(T(74, 144, 'weak: millivolts', 12, fill=MUT))
    o.append(T(214, 144, 'out 2 mV × 500 = 1.0 V', 12, fill=AC, bold=True))
    o.append(T(354, 144, '50 Hz hum × 0.303', 12, fill=AC))
    o.append(T(494, 144, 'output ∝ input', 12, fill=MUT))
    o.append(T(634, 144, 'ground loop broken', 12, fill=LV))
    # filter response
    x0, x1, y0, y1 = 100, 500, 196, 376
    fx = logx(x0, x1, 0, 3); fy = lambda g: y1 - (y1 - y0) * g
    o.append(axes(x0, x1, y0, y1, [1, 10, 100, 1000], [0, 0.25, 0.5, 0.75, 1.0], fx, fy, 'frequency f (Hz, log scale)', 'gain |H|', yfmt=lambda v: f'{v:.2f}'))
    fc = 15.9
    pts = [(fx(10 ** (i / 40)), fy(1 / math.sqrt(1 + (10 ** (i / 40) / fc) ** 2))) for i in range(0, 121)]
    o.append(P(pts, AC, 2.6))
    o.append(L(fx(fc), fy(0.707), fx(fc), fy(0), AC, 1.4, '5 4')); o.append(L(fx(1), fy(0.707), fx(fc), fy(0.707), AC, 1.4, '5 4'))
    o.append(C(fx(fc), fy(0.707), 5.5, AC))
    o.append(Tb(fx(fc) + 12, fy(0.707) - 10, sb('f', 'c') + ' = 15.9 Hz: 0.707', 12, 'start', AC, True))
    g50 = 1 / math.sqrt(1 + (50 / fc) ** 2)
    o.append(L(fx(50), fy(g50), fx(50), fy(0), LV, 1.4, '5 4'))
    o.append(C(fx(50), fy(g50), 5.5, LV))
    o.append(Tb(fx(50) + 10, fy(g50) - 10, '50 Hz: 0.303 (−10.4 dB)', 12, 'start', LV, True))
    o.append(Tb(fx(1.6), fy(1.0) + 18, 'slow strain passes', 12, 'start', MUT))
    o.append(T(530, 220, 'Signal path', 14, 'start', bold=True))
    o.append(T(530, 246, '2 mV × 500 = 1.0 V', 13, 'start'))
    o.append(T(530, 270, sb('f', 'c') + ' = 1/(2πRC)', 13, 'start'))
    o.append(T(530, 292, '= 1/(2π × 10⁴ × 10⁻⁶)', 13, 'start'))
    o.append(T(530, 314, '= 15.9 Hz', 13, 'start', AC, True))
    o.append(T(530, 340, 'hum: 1 V → 0.303 V', 13, 'start', LV))
    o.append(T(530, 362, 'a notch removes the rest', 12, 'start', MUT))
    return 420, ''.join(o)
FIG[1] = (f1, 'Top: a 2 mV bridge signal leaves the in-amp (gain 500, 54.0 dB) at 1.0 V, then passes a 10 kΩ, 1 µF low-pass, linearisation and an isolation barrier before the ADC. Below: the low-pass has fc = 15.9 Hz, so slow strain passes while 50 Hz hum is cut to 0.303 of its size.',
          'Five blocks in a row: bridge sensor 2 millivolts, in-amp of gain 500 giving 1.0 volt, RC low-pass with cutoff 15.9 hertz, linearise, and isolation barrier; below, the low-pass gain curve on a log frequency axis, 0.707 at 15.9 hertz and 0.303 at 50 hertz.')


# ---- data acquisition: one multiplexed converter and its time slots ----
def f2():
    o = [T(20, 26, 'Four channels share one 12-bit converter', 15, 'start', bold=True)]
    ys = [52, 94, 136, 178]
    for i, y in enumerate(ys):
        o.append(boxt(16, y, 104, 32, [f'CH{i + 1}  ±5 V'], ACS if i == 0 else PANEL, AC if i == 0 else L2, 13))
        o.append(L(122, y + 16, 156, y + 16, INK, 1.6))
    o.append(T(68, 230, 'CH5 to CH8 idle', 12, fill=MUT))
    o.append(poly([(158, 44), (206, 72), (206, 190), (158, 218)], PANEL, AC))
    o.append(T(182, 136, 'MUX', 13, bold=True))
    o.append(L(208, 131, 240, 131, AC, 2, arrow='n'))
    o.append(boxt(244, 104, 100, 54, ['Sample and', 'hold'], PANEL, AC, 13))
    o.append(L(346, 131, 378, 131, AC, 2, arrow='n'))
    o.append(boxt(382, 98, 124, 66, ['12-bit ADC', 'span 10 V'], ACS, AC, 13, bold_first=True))
    o.append(L(508, 131, 540, 131, AC, 2, arrow='n'))
    o.append(boxt(544, 98, 156, 66, ['Processor', 'scale, store, display'], PANEL, L2, 13, bold_first=True))
    o.append(P([(622, 96), (622, 40), (182, 40), (182, 50)], NX, 1.6, '5 4'))
    o.append(L(182, 46, 182, 58, NX, 1.6, arrow='x'))
    o.append(Tb(420, 44, 'channel select and convert', 12, 'middle', NX))
    o.append(T(444, 192, 'step = 10 V / 4096', 13, fill=AC))
    o.append(T(444, 212, '= 2.44 mV', 13, fill=AC, bold=True))
    # time slots
    X0, X1, Y = 70, 670, 316
    fx = lambda t: X0 + (X1 - X0) * t / 1250
    for i in range(5):
        ch = i % 4 + 1
        o.append(R(fx(250 * i) + 1, Y - 34, fx(250) - fx(0) - 2, 30, ACS if ch == 1 else PANEL, AC if ch == 1 else L2, 4))
        o.append(T((fx(250 * i) + fx(250 * i + 250)) / 2, Y - 14, f'CH{ch}', 13, bold=(ch == 1)))
    o.append(xaxis(X0, X1, Y, [0, 250, 500, 750, 1000, 1250], fx, 'time (µs)'))
    o.append(brace(fx(0), fx(250), Y - 44, INK, up=True))
    o.append(T(fx(125), Y - 54, '250 µs per conversion', 12, bold=True))
    o.append(brace(fx(0), fx(1000), Y + 62, LV))
    o.append(T(fx(500), Y + 88, 'CH1 is sampled every 1 ms: 1 kS/s per channel, 4 kS/s in total', 13, fill=LV, bold=True))
    o.append(T(fx(500), Y + 108, 'Nyquist: each channel may carry signals up to 1000 / 2 = 500 Hz', 13, fill=LV))
    return 436, ''.join(o)
FIG[2] = (f2, 'Four of the eight channels pass through the multiplexer and the sample-and-hold to one 12-bit converter of 10 V span, so one step is 2.44 mV. The converter takes the channels in turn, 250 µs each, so every channel is sampled once per millisecond (1 kS/s) and may carry signals up to 500 Hz.',
          'Four channel boxes feed a multiplexer, a sample-and-hold, a 12-bit ADC and a processor, with a dashed channel-select line back to the multiplexer; below, a time line of 250 microsecond slots labelled CH1 to CH4 and CH1 again, with a bracket showing CH1 repeats every millisecond.')


# ---- signal transmission: the 4-20 mA loop and its voltage budget ----
def f3():
    o = [T(20, 26, 'The loop current is the signal; the voltages share 24 V', 15, 'start', bold=True)]
    xl, xr, yt, yb = 80, 560, 80, 250
    o.append(L(xl, yt, 250, yt, INK, 1.8)); o.append(L(390, yt, xr, yt, INK, 1.8))
    o.append(boxt(250, 52, 140, 56, ['2-wire transmitter', 'needs ≥ 10 V'], ACS, AC, 13, bold_first=True))
    o.append(L(xl, yt, xl, 150, INK, 1.8)); o.append(battery_v(xl, 160, INK, '24 V')); o.append(L(xl, 170, xl, yb, INK, 1.8))
    o.append(T(xl - 24, 147, '+', 13, 'end', MUT))
    o.append(L(xr, yt, xr, 125, INK, 1.8)); o.append(res_v(xr, 125, 205, INK)); o.append(L(xr, 205, xr, yb, INK, 1.8))
    o.append(T(xr - 16, 170, '250 Ω', 13, 'end', bold=True))
    o.append(dot(xr, 125)); o.append(dot(xr, 205))
    o.append(L(xr, 125, 610, 125, INK, 1.4)); o.append(L(xr, 205, 610, 205, INK, 1.4))
    o.append(boxt(610, 120, 96, 90, ['ADC', 'V = 250 I', '1 V to 5 V'], LVS, LV, 13, bold_first=True))
    o.append(L(xl, yb, 230, yb, INK, 1.8)); o.append(res_h(230, 400, yb, MUT)); o.append(L(400, yb, xr, yb, INK, 1.8))
    o.append(T(315, yb + 26, 'cable: both leads, up to 450 Ω', 12, fill=MUT))
    o.append(L(430, yt - 12, 500, yt - 12, AC, 2, arrow='n')); o.append(T(465, yt - 20, 'I = 4 to 20 mA', 13, fill=AC, bold=True))
    o.append(L(xr + 14, 222, xr + 14, 240, AC, 2, arrow='n'))
    o.append(T(320, 172, 'the same current flows', 12, fill=MUT)); o.append(T(320, 188, 'in every part of the loop', 12, fill=MUT))
    # budget bar at 20 mA
    X0, X1, Y = 80, 640, 314
    fx = lambda v: X0 + (X1 - X0) * v / 24
    parts = [(0, 10, ACS, AC, 'transmitter 10 V'), (10, 15, LVS, LV, '250 Ω × 20 mA = 5 V'), (15, 24, PANEL, L2, 'cable up to 450 Ω: 9 V')]
    for a, b, f, s, lab in parts:
        o.append(R(fx(a), Y, fx(b) - fx(a), 34, f, s, 4)); o.append(T((fx(a) + fx(b)) / 2, Y + 22, lab, 12, bold=True))
    o.append(T(X0, Y - 10, 'At full scale, 20 mA:', 13, 'start', bold=True))
    o.append(xaxis(X0, X1, Y + 40, [0, 10, 15, 24], fx, None, lambda v: f'{v} V'))
    o.append(T(360, Y + 86, '(24 − 10) V / 0.020 A = 700 Ω for the whole loop, 250 Ω of it the sense resistor', 13, fill=AC))
    o.append(T(360, Y + 108, 'RTD example: 12.4 mA → 3.1 V → (12.4 − 4)/16 = 52.5 % of 0–150 °C = 78.75 °C', 13, fill=LV))
    return 432, ''.join(o)
FIG[3] = (f3, 'A 24 V supply, the transmitter, the cable and a 250 Ω sense resistor form one series loop, so the same 4 to 20 mA flows everywhere and the ADC reads 1 to 5 V. At 20 mA the transmitter needs 10 V and the resistor takes 5 V, which leaves 9 V for the cable: 700 Ω for the whole loop.',
          'A series loop with a 24 volt cell, a two-wire transmitter needing 10 volts, a 250 ohm sense resistor read by an ADC as 1 to 5 volts, and a cable resistance; below, a bar dividing 24 volts into 10 volts for the transmitter, 5 volts for the resistor and 9 volts for the cable.')


# ---- pneumatic and hydraulic actuators: the circuit and the force comparison ----
def f4():
    o = [T(20, 26, 'The 5/2 valve is where the electrical signal meets the air', 15, 'start', bold=True)]
    # supply and FRL
    o.append(f'<circle cx="40" cy="220" r="18" style="fill:var(--panel);stroke:var(--ink);stroke-width:1.8"/>')
    o.append(T(40, 225, 'air', 12, bold=True)); o.append(T(40, 256, '6 bar', 12, fill=AC, bold=True))
    o.append(L(58, 220, 86, 220, INK, 1.8))
    o.append(boxt(86, 196, 92, 48, ['FRL unit', 'filter, regulator,'], PANEL, L2, 12, bold_first=True))
    o.append(T(132, 262, 'lubricator', 12, fill=MUT))
    o.append(P([(178, 220), (196, 220), (196, 256), (260, 256), (260, 236)], INK, 1.8))
    # valve: two squares
    vx, vy, vw, vh = 240, 176, 70, 60
    o.append(R(vx, vy, vw, vh, LVS, LV, 2)); o.append(R(vx + vw, vy, vw, vh, PANEL, L2, 2))
    o.append(L(vx + 20, vy + vh - 6, vx + 20, vy + 8, LV, 1.8, arrow='l')); o.append(L(vx + 50, vy + 8, vx + 50, vy + vh - 6, LV, 1.8, arrow='l'))
    o.append(L(vx + vw + 50, vy + vh - 6, vx + vw + 50, vy + 8, MUT, 1.6, arrow='m')); o.append(L(vx + vw + 20, vy + 8, vx + vw + 20, vy + vh - 6, MUT, 1.6, arrow='m'))
    o.append(R(vx - 30, vy + 14, 30, 32, ACS, AC, 3)); o.append(L(vx - 30, vy + 46, vx, vy + 14, AC, 1.6))
    o.append(T(vx - 15, vy - 8, 'coil', 12, fill=AC, bold=True))
    o.append(P([(vx + 2 * vw, vy + 30), (vx + 2 * vw + 6, vy + 22), (vx + 2 * vw + 12, vy + 38), (vx + 2 * vw + 18, vy + 22), (vx + 2 * vw + 24, vy + 38), (vx + 2 * vw + 30, vy + 30)], INK, 1.6))
    o.append(T(vx + 2 * vw + 16, vy - 8, 'spring', 12, fill=MUT))
    o.append(T(vx + 70, vy + vh + 46, '5/2 solenoid valve', 13, bold=True))
    o.append(T(vx + 26, vy + vh + 14, 'P', 12, 'start', MUT)); o.append(T(vx + 56, vy + vh + 14, 'exhaust', 12, 'start', MUT))
    # lines to the cylinder
    ax, bx = vx + 20, vx + 50
    o.append(P([(ax, vy), (ax, 150), (445, 150), (445, 134)], LV, 2)); o.append(T(ax - 8, 162, 'A', 13, 'end', LV, True))
    o.append(P([(bx, vy), (bx, 160), (605, 160), (605, 134)], INK, 1.8)); o.append(T(bx + 8, 172, 'B', 13, 'start', bold=True))
    # cylinder
    o.append(R(430, 70, 190, 64, PANEL, INK, 3, 2))
    o.append(R(500, 72, 12, 60, ACS, AC, 2))
    o.append(R(512, 95, 188, 14, PANEL, INK, 2, 1.6))
    o.append(L(640, 82, 700, 82, LV, 2.4, arrow='l')); o.append(T(670, 70, 'extend', 12, fill=LV, bold=True))
    o.append(T(466, 108, 'air', 12, fill=LV)); o.append(T(525, 60, 'bore 50 mm, rod 20 mm', 12, fill=MUT))
    # forces
    o.append(T(380, 312, 'Extend: F = p A η = 0.6 N/mm² × 1963.5 mm² × 0.9 = 1060 N', 13, fill=LV, bold=True))
    o.append(T(380, 334, 'Retract: annulus π(50² − 20²)/4 = 1649.3 mm², so 0.6 × 1649.3 × 0.9 = 890.6 N', 13))
    X0, X1 = 170, 660
    fx = lambda f: X0 + (X1 - X0) * f / 30
    o.append(T(X0 - 10, 372, 'pneumatic 6 bar', 12, 'end', bold=True)); o.append(R(X0, 360, fx(1.178) - X0, 16, LVS, LV, 3))
    o.append(T(fx(1.178) + 8, 373, '1.18 kN (theoretical)', 12, 'start', LV))
    o.append(T(X0 - 10, 402, 'hydraulic 150 bar', 12, 'end', bold=True)); o.append(R(X0, 390, fx(29.45) - X0, 16, ACS, AC, 3))
    o.append(T(fx(29.45) - 8, 403, '29.4 kN: 25 times more', 12, 'end', INK, True))
    o.append(xaxis(X0, X1, 414, [0, 10, 20, 30], fx, None, lambda v: f'{v} kN'))
    return 446, ''.join(o)
FIG[4] = (f4, 'Air at 6 bar passes the FRL unit to a solenoid-operated 5/2 valve; with the coil on, port A feeds the cap end and the 50 mm cylinder extends with 1060 N, and the spring returns the valve to feed port B for 890.6 N of retraction. The same bore on 150 bar oil gives 29.4 kN, 25 times the air cylinder.',
          'Pneumatic circuit: an air supply at 6 bar, an FRL unit, a two-square 5/2 valve with a coil on one side and a spring on the other, lines A and B to the two ends of a cylinder with a 20 millimetre rod; below, the extend and retract force sums and two bars comparing 1.18 kilonewtons pneumatic with 29.4 kilonewtons hydraulic.')


# ---- electrical actuators: the DC motor's equivalent circuit and power flow, and peak-and-hold drive ----
def f5():
    o = [T(20, 26, 'Where a DC motor\'s 24 W go, and how a solenoid is driven', 15, 'start', bold=True)]
    o.append(L(50, 70, 50, 120, INK, 1.8)); o.append(battery_v(50, 130, INK)); o.append(T(30, 168, '12 V', 13, 'middle', INK, True)); o.append(L(50, 140, 50, 200, INK, 1.8))
    o.append(L(50, 70, 110, 70, INK, 1.8)); o.append(res_h(110, 220, 70, INK)); o.append(L(220, 70, 290, 70, INK, 1.8))
    o.append(T(165, 56, sb('R', 'a') + ' = 1 Ω', 13, bold=True))
    o.append(L(290, 70, 290, 105, INK, 1.8))
    o.append(f'<circle cx="290" cy="135" r="30" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(290, 140, 'M', 15, bold=True))
    o.append(L(290, 165, 290, 200, INK, 1.8)); o.append(L(50, 200, 290, 200, INK, 1.8))
    o.append(T(166, 130, sb('E', 'b') + ' = 10 V', 13, fill=AC, bold=True))
    o.append(L(70, 86, 100, 86, AC, 2, arrow='n')); o.append(T(85, 104, 'I = 2 A', 12, fill=AC, bold=True))
    o.append(T(166, 226, '12 = 10 + 2 × 1', 13)); o.append(T(166, 246, sb('E', 'b') + ' = V − I' + sb('R', 'a'), 13, fill=MUT))
    # power flow
    o.append(boxt(360, 60, 96, 46, ['24 W in', 'V I'], PANEL, L2, 13, bold_first=True))
    o.append(L(458, 83, 480, 83, AC, 2, arrow='n'))
    o.append(boxt(484, 60, 104, 46, ['20 W', sb('E', 'b') + ' I'], ACS, AC, 13, bold_first=True))
    o.append(L(590, 83, 612, 83, AC, 2, arrow='n'))
    o.append(boxt(616, 60, 92, 46, ['18 W shaft', 'output'], LVS, LV, 13, bold_first=True))
    o.append(L(408, 108, 408, 140, NX, 2, arrow='x')); o.append(T(408, 160, '4 W copper', 12, fill=NX, bold=True)); o.append(T(408, 176, 'I²R = 2² × 1', 12, fill=NX))
    o.append(L(536, 108, 536, 140, NX, 2, arrow='x')); o.append(T(536, 160, '2 W friction', 12, fill=NX, bold=True)); o.append(T(536, 176, 'and iron', 12, fill=NX))
    o.append(T(662, 160, 'η = 18 / 24', 13, bold=True)); o.append(T(662, 178, '= 75 %', 13, fill=LV, bold=True))
    # peak and hold
    X0, X1, Y0, Y1 = 100, 640, 300, 410
    fx = lambda t: X0 + (X1 - X0) * t / 22; fy = lambda i: Y1 - (Y1 - Y0) * i / 2.0
    o.append(axes(X0, X1, Y0, Y1, [0, 2, 10, 20, 22], [0, 0.5, 1.0, 1.5, 2.0], fx, fy, 'time (s); the pull-in pulse is drawn wider than it is', 'coil current (A)', yfmt=lambda v: f'{v:.1f}'))
    pk = 0.35
    pts = [(fx(0), fy(0)), (fx(0), fy(2.0)), (fx(pk), fy(2.0)), (fx(pk), fy(0.5)), (fx(2), fy(0.5)), (fx(2), fy(0)), (fx(20), fy(0)), (fx(20), fy(2.0)), (fx(20 + pk), fy(2.0)), (fx(20 + pk), fy(0.5)), (fx(22), fy(0.5))]
    o.append(P(pts, AC, 2.6))
    o.append(Tb(fx(pk) + 8, fy(2.0) + 4, 'pull-in: 24 V / 12 Ω = 2.0 A, 48 W', 12, 'start', AC, True))
    o.append(Tb(fx(2) + 10, fy(0.5) + 4, 'hold at 6 V: 0.5 A, 3.0 W', 12, 'start', LV, True))
    o.append(Tb(fx(11), fy(0) - 12, 'off for 18 s: duty 2/20 = 10 %', 12, 'middle', MUT))
    return 470, ''.join(o)
FIG[5] = (f5, 'Top: the motor of the first example draws 2 A from 12 V through 1 Ω, so its back emf is 10 V; of the 24 W taken in, 4 W heat the armature and 2 W go in friction and iron loss, leaving 18 W at the shaft (75 %). Below: the solenoid valve pulls in at 2.0 A (48 W) and holds at 0.5 A (3.0 W) for 2 s in every 20 s.',
          'Equivalent circuit of a DC motor: a 12 volt cell, armature resistance 1 ohm and a motor of back emf 10 volts carrying 2 amperes; a power flow from 24 watts in through 20 watts converted to 18 watts at the shaft with 4 and 2 watt losses; below, a coil current trace stepping to 2.0 amperes, down to 0.5 amperes, then off until 20 seconds.')


# ---- stepper and servo: full-step sequence and the lead screw ----
def f6():
    o = [T(20, 26, 'One pulse, one step: pulses set the position', 15, 'start', bold=True)]
    cx, cy, r = 130, 150, 84
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:var(--panel);stroke:var(--line2);stroke-width:2"/>')
    poles = [('A', 0, -1), ('B', 1, 0), ('C', 0, 1), ('D', -1, 0)]
    for name, ux, uy in poles:
        on = name == 'A'
        px, py = cx + ux * 58, cy + uy * 58
        w, h = (26, 40) if ux == 0 else (40, 26)
        o.append(R(px - w / 2, py - h / 2, w, h, ACS if on else PANEL, AC if on else L2, 3))
        o.append(T(cx + ux * 104, cy + uy * 104 + 5, name, 14, fill=AC if on else INK, bold=True))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="24" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2"/>')
    o.append(L(cx, cy + 14, cx, cy - 20, LV, 3, arrow='l')); o.append(T(cx + 6, cy + 8, 'N', 12, 'start', LV, True))
    o.append(T(cx, 286, 'Full step: A → B → C → D → A', 13, bold=True))
    o.append(T(cx, 304, 'one phase on at a time', 12, fill=MUT))
    o.append(T(cx, 322, 'A is on: rotor lines up with A', 12, fill=AC))
    # lead screw
    o.append(boxt(270, 112, 70, 60, ['motor', '1.8°'], ACS, AC, 13, bold_first=True))
    o.append(L(340, 142, 360, 142, INK, 3))
    pts = []
    for i in range(29):
        pts.append((360 + i * 11.4, 142 + (10 if i % 2 == 0 else -10)))
    o.append(P(pts, INK, 1.8))
    o.append(R(360, 128, 320, 28, 'none', L2, 2, 1.2))
    o.append(R(480, 92, 90, 30, LVS, LV, 4)); o.append(T(525, 112, 'table', 13, bold=True))
    o.append(R(492, 122, 66, 40, 'var(--fig)', LV, 3, 1.6)); o.append(T(525, 147, 'nut', 12, fill=LV))
    o.append(L(574, 104, 640, 104, LV, 2.4, arrow='l')); o.append(T(606, 92, '25 mm/s', 12, fill=LV, bold=True))
    o.append(brace(371.4, 394.2 + 34.2 - 11.4, 180, INK))
    o.append(T(394, 206, 'lead 5 mm per rev', 12, bold=True))
    o.append(T(490, 236, '1000 pulses/s ÷ 200 steps/rev = 5 rev/s = 300 rpm', 13, fill=AC))
    o.append(T(490, 256, '5 rev/s × 5 mm = 25 mm/s;  5 mm / 200 = 0.025 mm per step', 13, fill=AC))
    # staircase
    X0, X1, Y0, Y1 = 280, 660, 290, 400
    fx = lambda n: X0 + (X1 - X0) * n / 8; fy = lambda mm: Y1 - (Y1 - Y0) * mm / 0.2
    o.append(axes(X0, X1, Y0, Y1, list(range(0, 9)), [0, 0.1, 0.2], fx, fy, 'pulses sent', 'table position (mm)', yfmt=lambda v: f'{v:.1f}'))
    pts = [(fx(0), fy(0))]
    for n in range(8):
        pts += [(fx(n + 0.15), fy(0.025 * n)), (fx(n + 0.3), fy(0.025 * (n + 1))), (fx(n + 1), fy(0.025 * (n + 1)))]
    o.append(P(pts, AC, 2.4))
    o.append(Tb(fx(4.6), fy(0.185), '8 pulses: 8 × 0.025 = 0.2 mm', 12, 'end', AC, True))
    o.append(T(cx, 364, 'No sensor is needed', 13, bold=True))
    o.append(T(cx, 382, 'while load torque stays', 12, fill=MUT))
    o.append(T(cx, 398, 'below the pull-in torque', 12, fill=MUT))
    return 450, ''.join(o)
FIG[6] = (f6, 'Left: in full-step drive one stator phase is on at a time, and the rotor lines up with it. Right: the 1.8° motor turns a 5 mm lead screw, so 1000 pulses/s give 5 rev/s (300 rpm) and 25 mm/s, and each pulse moves the table 0.025 mm. Phases are drawn simplified; a real 1.8° motor has many rotor teeth.',
          'A four-pole stator with phases A, B, C and D and a magnet rotor pointing to the energised phase A; a motor turning a lead screw with a nut and table moving at 25 millimetres per second; below, a staircase of table position rising 0.025 millimetres per pulse to 0.2 millimetres after 8 pulses.')


# ---- micro actuators: the parallel-plate actuator and pull-in ----
def f7():
    o = [T(20, 26, 'An electrostatic plate is stable only for the first third of the gap', 15, 'start', bold=True)]
    # structure
    o.append(R(40, 54, 26, 20, PANEL, INK, 2)); o.append(R(304, 54, 26, 20, PANEL, INK, 2))
    for x in (78, 292):
        o.append(P([(x, 74), (x, 82)] + [(x + (8 if i % 2 == 0 else -8), 86 + i * 5) for i in range(6)] + [(x, 116), (x, 124)], INK, 1.6))
    o.append(L(66, 64, 78, 74, INK, 1.4)); o.append(L(304, 64, 292, 74, INK, 1.4))
    o.append(T(185, 66, 'spring k', 12, fill=MUT))
    o.append(R(60, 124, 250, 12, ACS, AC, 2)); o.append(T(185, 120, 'movable plate', 12, fill=AC, bold=True))
    o.append(R(60, 206, 250, 12, PANEL, INK, 2)); o.append(T(185, 236, 'fixed electrode', 12, fill=MUT))
    o.append(L(60, 159.3, 310, 159.3, LV, 1.6, '6 4'))
    o.append(Tb(185, 164, 'pull-in after 0.667 µm', 12, 'middle', LV, True))
    o.append(L(330, 138, 330, 204, INK, 1.4)); o.append(L(324, 136, 336, 136, INK, 1.4)); o.append(L(324, 206, 336, 206, INK, 1.4))
    o.append(T(340, 176, sb('g', '0') + ' = 2 µm', 12, 'start', bold=True))
    o.append(P([(60, 130), (28, 130), (28, 160)], INK, 1.6)); o.append(battery_v(28, 170, INK)); o.append(P([(28, 180), (28, 212), (60, 212)], INK, 1.6))
    o.append(T(34, 192, '30 V', 12, 'start', bold=True))
    o.append(T(185, 266, 'A = 200 µm × 200 µm = 4 × 10⁻⁸ m²', 12))
    o.append(T(185, 286, 'C = ε₀A/g = 0.177 pF', 12))
    o.append(T(185, 306, 'F = ε₀AV²/(2g²) = 39.8 µN', 12, fill=AC, bold=True))
    # force plot
    x0, x1, y0, y1 = 450, 690, 70, 300
    fx = lambda f: x0 + (x1 - x0) * f; fy = lambda F: y1 - (y1 - y0) * F / 1.0
    o.append(axes(x0, x1, y0, y1, [0, 1 / 3, 2 / 3, 1], [0, 0.5, 1.0], fx, fy, 'travel x / g₀', 'force / (k g₀)',
                  lambda v: ['0', '1/3', '2/3', '1'][round(v * 3)], lambda v: f'{v:.1f}'))
    o.append(L(fx(0), fy(0), fx(1), fy(1), INK, 2.2)); o.append(Tb(fx(0.86), fy(0.86) + 22, 'spring kx', 12, 'middle', INK, True))
    api = 4 / 27
    for a, c, lab in ((0.6 * api, LV, 'below'), (api, AC, 'at'), (1.6 * api, NX, 'above')):
        pts = []
        for i in range(0, 200):
            f = i / 200
            F = a / (1 - f) ** 2
            if F > 1.0: break
            pts.append((fx(f), fy(F)))
        o.append(P(pts, c, 2.4))
    o.append(L(fx(1 / 3), fy(0.66), fx(1 / 3), fy(0), AC, 1.4, '5 4'))
    o.append(C(fx(1 / 3), fy(1 / 3), 5.5, AC))
    pi_ = '<tspan baseline-shift="sub" font-size="10">PI</tspan>'
    for j, (c, lab) in enumerate(((NX, 'above V' + pi_), (AC, 'at V' + pi_), (LV, 'below V' + pi_))):
        yy = 92 + 20 * j
        o.append(L(x0 + 10, yy - 4, x0 + 30, yy - 4, c, 2.6)); o.append(T(x0 + 36, yy, lab, 12, 'start', c, True))
    # stroke comparison
    o.append(T(20, 372, 'Other micro actuators, from the second example:', 13, 'start', bold=True))
    o.append(T(20, 396, 'Piezo stack: 100 V across 0.1 mm = 1.0 MV/m; 500 pm/V × 100 V = 50 nm per layer;', 12, 'start', AC))
    o.append(T(20, 414, '100 layers give 5.0 µm, a strain of 0.05 %', 12, 'start', AC))
    o.append(T(20, 438, 'NiTi wire: 4 % of 50 mm = 2.0 mm, 400 times the stack, but it must be heated and cools slowly', 12, 'start', LV))
    return 452, ''.join(o)
FIG[7] = (f7, 'A 200 µm square plate 2 µm above a fixed electrode feels 39.8 µN at 30 V. The electric force rises as 1/(g₀ − x)², the spring force in a straight line; at the pull-in voltage they touch at x = g₀/3, so past 0.667 µm the plate snaps down.',
          'A movable plate hung on two springs above a fixed electrode with a 30 volt cell between them, a 2 micrometre gap and a dashed pull-in line after 0.667 micrometres; a graph of normalised force against travel with a straight spring line and three electric force curves, below, at and above the pull-in voltage, the middle one tangent at one third of the gap.')


# ---- bridges: Wheatstone and Hay with the worked values ----
def diamond(cx, cy, s):
    return {'A': (cx, cy - s), 'B': (cx - s, cy), 'C': (cx + s, cy), 'D': (cx, cy + s)}


def f8():
    o = [T(20, 26, 'Balance: product of opposite arms equal, detector at zero', 15, 'start', bold=True)]
    # Wheatstone
    n = diamond(200, 200, 110)
    o.append(res_d(*n['A'], *n['B'])); o.append(res_d(*n['A'], *n['C'])); o.append(res_d(*n['B'], *n['D'])); o.append(res_d(*n['C'], *n['D'], AC))
    o.append(L(n['B'][0], 200, 182, 200, INK, 1.6)); o.append(L(218, 200, n['C'][0], 200, INK, 1.6))
    o.append(f'<circle cx="200" cy="200" r="17" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2"/>'); o.append(T(200, 205, 'G', 14, fill=LV, bold=True))
    o.append(T(200, 232, '0 at balance', 12, fill=LV))
    for k, (x, y) in n.items():
        o.append(dot(x, y)); o.append(T(x + (12 if k in 'AD' else (-14 if k == 'B' else 14)), y + (16 if k == 'A' else (-8 if k == 'D' else 5)), k, 13, 'start' if k in 'AD' else ('end' if k == 'B' else 'start'), bold=True))
    o.append(T(130, 132, 'R₁ = 100 Ω', 12, 'end', bold=True)); o.append(T(270, 132, 'R₂ = 200 Ω', 12, 'start', bold=True))
    o.append(T(130, 278, 'R₃ = 150 Ω', 12, 'end', bold=True)); o.append(T(270, 278, 'Rₓ = 300 Ω', 12, 'start', AC, True))
    o.append(P([n['A'], (200, 64), (40, 64), (40, 180)], INK, 1.6)); o.append(battery_v(40, 190, INK)); o.append(P([(40, 200), (40, 336), (200, 336), n['D']], INK, 1.6))
    o.append(T(34, 160, 'DC', 12, 'end', MUT))
    o.append(T(200, 368, 'R₁ Rₓ = R₂ R₃:  Rₓ = 200 × 150 / 100 = 300 Ω', 13, fill=AC, bold=True))
    o.append(T(200, 390, 'check: 100/150 = 200/300 = 0.667', 12, fill=MUT))
    # Hay
    m = diamond(540, 200, 110)
    o.append(res_d(*m['A'], *m['B'], INK, t0=0.18, t1=0.5)); o.append(cap_d(m['A'][0] + (m['B'][0] - m['A'][0]) * 0.5, m['A'][1] + (m['B'][1] - m['A'][1]) * 0.5, *m['B'], 0.5, AC))
    o.append(res_d(*m['A'], *m['C'])); o.append(res_d(*m['B'], *m['D']))
    o.append(ind_d(*m['C'], *m['D'], AC, 4, 0.2, 0.62)); o.append(res_d(m['C'][0] + (m['D'][0] - m['C'][0]) * 0.62, m['C'][1] + (m['D'][1] - m['C'][1]) * 0.62, *m['D'], AC, 4, 6, 0.2, 0.8))
    o.append(L(m['B'][0], 200, 522, 200, INK, 1.6)); o.append(L(558, 200, m['C'][0], 200, INK, 1.6))
    o.append(f'<circle cx="540" cy="200" r="17" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2"/>'); o.append(T(540, 205, 'D', 14, fill=LV, bold=True))
    o.append(T(540, 232, 'null', 12, fill=LV))
    for x, y in m.values():
        o.append(dot(x, y))
    o.append(T(466, 128, 'R₁ = 100 Ω', 12, 'end', bold=True)); o.append(T(466, 144, 'C₁ = 0.1 µF', 12, 'end', AC, True))
    o.append(T(610, 132, 'R₂ = 1 kΩ', 12, 'start', bold=True))
    o.append(T(470, 278, 'R₃ = 10 kΩ', 12, 'end', bold=True)); o.append(T(610, 270, 'coil Lₓ, Rₓ', 12, 'start', AC, True))
    o.append(P([m['A'], (540, 64), (700, 64), (700, 176)], INK, 1.6))
    o.append(f'<circle cx="700" cy="200" r="16" style="fill:var(--panel);stroke:var(--ink);stroke-width:1.6"/>')
    o.append(P([(690, 200), (695, 193), (700, 200), (705, 207), (710, 200)], INK, 1.6))
    o.append(P([(700, 216), (700, 336), (540, 336), m['D']], INK, 1.6))
    o.append(T(694, 160, '1 kHz', 12, 'end', MUT))
    o.append(T(540, 368, 'Q = 1/(ωR₁C₁) = 15.9', 13, fill=AC, bold=True))
    o.append(T(540, 390, 'Lₓ = R₂R₃C₁/(1 + 1/Q²) = 0.996 H, Rₓ = 393 Ω', 12))
    o.append(T(200, 50, 'Wheatstone (DC)', 14, bold=True)); o.append(T(540, 50, 'Hay (AC, high-Q coil)', 14, bold=True))
    return 410, ''.join(o)
FIG[8] = (f8, 'Left: a Wheatstone bridge with the DC source across A and D and the galvanometer between B and C; with R₁ = 100 Ω, R₂ = 200 Ω and R₃ = 150 Ω it balances at Rₓ = 300 Ω. Right: a Hay bridge at 1 kHz with R₁ = 100 Ω in series with C₁ = 0.1 µF opposite the coil gives Q = 15.9 and Lₓ = 0.996 H.',
          'Two bridges in diamond form. Left: resistors 100, 200 and 150 ohms and an unknown 300 ohms, a cell from A to D and a galvanometer between B and C reading zero. Right: a series resistor and capacitor, resistors of 1 and 10 kilohms and a coil, an AC source at 1 kilohertz and a null detector.')


# ---- filters and amplifiers: first-order responses and the value of CMRR ----
def f9():
    o = [T(20, 26, 'A filter picks the band; CMRR decides how much hum gets through', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 450, 66, 290
    fx = logx(x0, x1, 1, 5); fy = lambda g: y1 - (y1 - y0) * g
    o.append(axes(x0, x1, y0, y1, [10, 100, 1000, 10000, 100000], [0, 0.25, 0.5, 0.707, 1.0], fx, fy, 'frequency (Hz, log scale)', 'gain |H|',
                  lambda v: {10: '10', 100: '100', 1000: '1 k', 10000: '10 k', 100000: '100 k'}[v], lambda v: f'{v:g}'))
    fc = 1591.55
    lp = [(fx(10 ** (1 + i / 40)), fy(1 / math.sqrt(1 + (10 ** (1 + i / 40) / fc) ** 2))) for i in range(161)]
    hp = [(fx(10 ** (1 + i / 40)), fy((10 ** (1 + i / 40) / fc) / math.sqrt(1 + (10 ** (1 + i / 40) / fc) ** 2))) for i in range(161)]
    o.append(P(lp, AC, 2.6)); o.append(P(hp, LV, 2.6))
    o.append(L(fx(fc), fy(1.0), fx(fc), fy(0), INK, 1.3, '5 4'))
    o.append(C(fx(fc), fy(0.707), 5.5, INK))
    o.append(Tb(fx(fc), fy(0.707) - 14, sb('f', 'c') + ' = 1592 Hz', 12, 'middle', INK, True))
    g = 1 / math.sqrt(1 + (10000 / fc) ** 2)
    o.append(C(fx(10000), fy(g), 5.5, AC)); o.append(Tb(fx(10000) + 9, fy(g) - 8, '0.157', 12, 'start', AC, True))
    o.append(Tb(fx(18), fy(1.0) + 18, 'low-pass', 13, 'start', AC, True)); o.append(Tb(fx(15000), fy(1.0) + 18, 'high-pass', 13, 'middle', LV, True))
    o.append(T(265, 356, 'R = 1 kΩ, C = 0.1 µF: fc = 1591.55 Hz; at 10 kHz, 0.157 (−16.1 dB)', 13))
    o.append(T(265, 378, 'ECG high-pass: 3.3 MΩ, 1 µF gives 0.048 Hz', 13, fill=LV))
    # CMRR bars
    B0, s = 290, 176
    o.append(T(600, 56, 'ECG amplifier, gain 1000', 13, bold=True))
    o.append(T(600, 74, '1 mV heart, 0.5 V common mode', 12, fill=MUT))
    bars = [(520, 1.0, ACS, AC, 'signal', '1.0 V'), (600, 0.5, NXS, NX, 'hum, 60 dB', '0.5 V'), (680, 0.005, LVS, LV, 'hum, 100 dB', '5 mV')]
    for x, v, f, c, lab, val in bars:
        hgt = max(v * s, 2)
        o.append(R(x - 24, B0 - hgt, 48, hgt, f, c, 3))
        o.append(T(x, B0 - hgt - 8, val, 12, fill=c, bold=True))
        o.append(T(x, B0 + 20, lab, 12, fill=INK))
    o.append(L(490, B0, 712, B0, L2, 1.5))
    o.append(T(600, 334, 'A꜀ₘ = A' + '<tspan baseline-shift="sub" font-size="10">d</tspan>' + ' / 10^(CMRR/20)', 12, fill=MUT).replace('A꜀ₘ', 'A<tspan baseline-shift="sub" font-size="10">cm</tspan>').replace('10^(CMRR/20)', '10<tspan baseline-shift="super" font-size="10">CMRR/20</tspan>'))
    return 392, ''.join(o)
FIG[9] = (f9, 'Left: first-order low-pass and high-pass responses for R = 1 kΩ, C = 0.1 µF; both pass 0.707 at fc = 1592 Hz, and the low-pass is down to 0.157 (−16.1 dB) at 10 kHz. Right: an ECG amplifier of gain 1000 makes 1.0 V of signal; 0.5 V of common-mode hum leaves at 0.5 V with 60 dB CMRR but only 5 mV with 100 dB.',
          'Two gain curves on a log frequency axis from 10 hertz to 100 kilohertz, a falling low-pass and a rising high-pass crossing at 0.707 at 1592 hertz, with a point at 10 kilohertz at 0.157; three bars comparing a 1.0 volt signal with 0.5 volt hum at 60 decibels and 5 millivolt hum at 100 decibels.')


# ---- display instruments: CRO signal path, CRT deflection and reading the screen ----
def f10():
    o = [T(20, 26, 'The CRO: two signal paths steer one electron beam', 15, 'start', bold=True)]
    row = [(16, 'input'), (110, 'attenuator'), (230, 'vertical amp'), (360, 'delay line')]
    for x, s in row:
        o.append(boxt(x, 44, 104 if s != 'input' else 74, 38, [s], PANEL if s == 'input' else ACS, L2 if s == 'input' else AC, 13))
    o.append(L(92, 63, 108, 63, AC, 2, arrow='n')); o.append(L(216, 63, 228, 63, AC, 2, arrow='n')); o.append(L(336, 63, 358, 63, AC, 2, arrow='n'))
    o.append(L(466, 63, 500, 63, AC, 2, arrow='n')); o.append(T(506, 68, 'Y plates: volts/div', 13, 'start', AC, True))
    o.append(boxt(230, 100, 104, 38, ['trigger'], LVS, LV, 13)); o.append(boxt(360, 100, 104, 38, ['time base'], LVS, LV, 13))
    o.append(P([(282, 84), (282, 98)], LV, 1.6)); o.append(L(282, 84, 282, 97, LV, 1.6, arrow='l'))
    o.append(L(336, 119, 358, 119, LV, 2, arrow='l')); o.append(L(466, 119, 500, 119, LV, 2, arrow='l')); o.append(T(506, 124, 'X plates: time/div', 13, 'start', LV, True))
    # CRT geometry
    yb = 286
    o.append(R(16, yb - 20, 54, 40, PANEL, INK, 4)); o.append(T(43, yb + 36, 'gun', 12, fill=MUT))
    o.append(L(92, yb - 30, 92, yb - 6, INK, 2.4)); o.append(L(92, yb + 6, 92, yb + 30, INK, 2.4)); o.append(T(96, yb + 58, 'anode 2000 V', 12, fill=MUT))
    px0, px1, gap = 150, 186, 18
    o.append(L(px0, yb - gap, px1, yb - gap, AC, 3)); o.append(L(px0, yb + gap, px1, yb + gap, AC, 3))
    o.append(T((px0 + px1) / 2, yb - gap - 10, 'l = 2 cm', 12, fill=AC, bold=True))
    o.append(T(px1 + 6, yb + gap + 14, 'd = 5 mm', 12, 'start', AC, True))
    sx = 470
    o.append(L(sx, yb - 110, sx, yb + 40, INK, 3)); o.append(T(sx + 8, yb + 86, 'screen', 12, 'middle', MUT))
    dpx = 66  # deflection drawn
    beam = [(70, yb), (px0, yb)] + [(px0 + (px1 - px0) * t / 10, yb - 6 * (t / 10) ** 2) for t in range(1, 11)]
    beam += [(sx, yb - dpx)]
    o.append(P(beam, LV, 2.2))
    o.append(L(px1, yb - 6, sx, yb, MUT, 1, '3 4'))
    o.append(L(px0, yb, sx, yb, L2, 1, '2 4'))
    o.append(L(sx - 14, yb, sx - 14, yb - dpx, NX, 1.6)); o.append(T(sx - 20, yb - 28, 'D', 13, 'end', NX, True))
    o.append(brace(168, sx, yb + 44, INK)); o.append(T(320, yb + 66, 'L = 20 cm, plate centre to screen', 12))
    o.append(T(20, 188, 'S = L l / (2 d Vₐ) = (0.2 × 0.02)/(2 × 0.005 × 2000)', 12, 'start').replace('Vₐ', 'V<tspan baseline-shift="sub" font-size="10">a</tspan>'))
    o.append(T(20, 208, '= 0.2 mm/V;  D = 1 cm needs 10 mm / 0.2 = 50 V', 12, 'start', AC, True))
    # screen grid
    gx0, gy0, cw, nx_, ny_ = 510, 196, 24, 8, 6
    o.append(R(gx0, gy0, cw * nx_, cw * ny_, 'var(--fig)', L2, 2, 1.6))
    for i in range(1, nx_):
        o.append(L(gx0 + cw * i, gy0, gx0 + cw * i, gy0 + cw * ny_, 'var(--line)', 1))
    for j in range(1, ny_):
        o.append(L(gx0, gy0 + cw * j, gx0 + cw * nx_, gy0 + cw * j, 'var(--line)', 1))
    pts = [(gx0 + t, gy0 + cw * 3 - 50 * math.sin(2 * math.pi * t / (4 * cw))) for t in range(0, cw * nx_ + 1, 2)]
    o.append(P(pts, LV, 2.4))
    o.append(brace(gx0, gx0 + 4 * cw, gy0 + cw * ny_ + 10, NX))
    o.append(T(gx0 + 2 * cw, gy0 + cw * ny_ + 32, '4 div', 12, fill=NX, bold=True))
    o.append(T(gx0 + 4 * cw, gy0 + cw * ny_ + 56, '4 × 0.2 ms = 0.8 ms', 12, fill=INK))
    o.append(T(gx0 + 4 * cw, gy0 + cw * ny_ + 74, 'f = 1/0.8 ms = 1250 Hz', 12, fill=LV, bold=True))
    return 430, ''.join(o)
FIG[10] = (f10, 'Top: the vertical path (attenuator, amplifier, delay line) drives the Y plates and the triggered time base drives the X plates. Below: in the CRT of the second example, plates 2 cm long and 5 mm apart, 20 cm from the screen at 2000 V, give S = 0.2 mm/V, so 50 V moves the spot 1 cm; on the screen one cycle over 4 divisions at 0.2 ms/div is 1250 Hz.',
          'Block diagram of a CRO with input, attenuator, vertical amplifier and delay line to the Y plates, and trigger and time base to the X plates; a CRT side view with gun, anode at 2000 volts, deflection plates 2 centimetres long and 5 millimetres apart and a beam bending up to the screen 20 centimetres away; a screen grid with one sine cycle over 4 divisions.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}


def drop_sources():
    return ['mit.edu', 'openstax.org']
