# Glass t16 drawings for Power Electronics (ee-pe). Every number is computed here from the lesson's own worked examples.
from gfx import *
import math, re
D = {}
pi, rad, deg = math.pi, math.radians, math.degrees
f1 = lambda v: f'{v:.1f}'.replace('-', '−')
f2 = lambda v: f'{v:.2f}'.replace('-', '−')
f0 = lambda v: f'{v:.0f}'.replace('-', '−')


# ---------- rich text: x_{sub}, x^{sup} ----------
def R(s):
    out, i = '', 0
    for m in re.finditer(r'([_^])\{([^}]*)\}', s):
        sh = 'sub' if m.group(1) == '_' else 'super'
        out += E(s[i:m.start()]) + f'<tspan baseline-shift="{sh}" font-size="70%">{E(m.group(2))}</tspan>'
        i = m.end()
    return out + E(s[i:])

def plen(s):
    sub = sum(len(m) for m in re.findall(r'[_^]\{([^}]*)\}', s))
    return len(re.sub(r'[_^]\{[^}]*\}', '', s)) + 0.72 * sub

def rt(x, y, s, size=16, fill=INK, w=800, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" {F} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{R(s)}</text>'

def rtag(x, y, s, c, size=14, anchor='middle', bg=W):
    w = plen(s) * size * 0.58 + 18
    x0 = x - w / 2 if anchor == 'middle' else (x - w if anchor == 'end' else x)
    return (f'<rect x="{x0:.1f}" y="{y - size - 5:.1f}" width="{w:.1f}" height="{size + 13}" rx="{(size + 13) / 2}" fill="{bg}" stroke="{c}" stroke-width="2"/>'
            + rt(x0 + w / 2, y + 1, s, size, c))

def rbox(x, y, w, h, s, c, size=15, fill=W, sub=None, subc=None, sw=2.5, r=14, tc=INK, ss=None):
    o = f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="{fill}" stroke="{c}" stroke-width="{sw}"/>'
    if sub is None:
        return o + rt(x + w / 2, y + h / 2 + size * 0.36, s, size, tc)
    return o + rt(x + w / 2, y + h / 2 - 3, s, size, tc) + rt(x + w / 2, y + h / 2 + (ss or size - 2) + 4, sub, ss or size - 2, subc or c, 800)


import gfx as _gfx
_gfx.txt = rt
txt = rt
tag = rtag

# ---------- circuit symbols ----------
def wire(pts, c=INK, w=3):
    return poly(pts, c, w)

def _g(x, y, ang, body):
    return f'<g transform="translate({x:.1f},{y:.1f}) rotate({ang})">{body}</g>'

ANG = {'r': 0, 'd': 90, 'l': 180, 'u': -90}

def diode(x, y, d='r', s=11, c=INK):
    b = (f'<polygon points="{-s},{-s} {-s},{s} {s},0" fill="{c}"/>'
         f'<line x1="{s}" y1="{-s}" x2="{s}" y2="{s}" stroke="{c}" stroke-width="3.5" stroke-linecap="round"/>')
    return _g(x, y, ANG[d], b)

def scr(x, y, d='r', s=11, c=INK):
    b = (f'<polygon points="{-s},{-s} {-s},{s} {s},0" fill="{c}"/>'
         f'<line x1="{s}" y1="{-s}" x2="{s}" y2="{s}" stroke="{c}" stroke-width="3.5" stroke-linecap="round"/>'
         f'<line x1="{s * .4:.1f}" y1="{s * .45:.1f}" x2="{s * 1.2:.1f}" y2="{s * 1.45:.1f}" stroke="{c}" stroke-width="3" stroke-linecap="round"/>')
    return _g(x, y, ANG[d], b)

def res(x1, y1, x2, y2, c=INK, n=6, a=7):
    L = math.hypot(x2 - x1, y2 - y1); ang = deg(math.atan2(y2 - y1, x2 - x1))
    pts = [(0, 0)] + [((i + .5) * L / n, a * (1 if i % 2 == 0 else -1)) for i in range(n)] + [(L, 0)]
    return _g(x1, y1, f'{ang:.1f}', poly(pts, c, 3))

def ind(x1, y1, x2, y2, c=INK, n=4):
    L = math.hypot(x2 - x1, y2 - y1); ang = deg(math.atan2(y2 - y1, x2 - x1)); r = L / n / 2
    d = 'M0,0 ' + ' '.join(f'a{r:.1f},{r:.1f} 0 0 1 {2 * r:.1f},0' for _ in range(n))
    return _g(x1, y1, f'{ang:.1f}', f'<path d="{d}" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"/>')

def cap(x, y, d='v', w=24, gap=8, c=INK):
    # plates across a wire running in direction d ('v' wire vertical, 'h' horizontal) centred at x,y
    if d == 'v':
        return line(x - w / 2, y - gap / 2, x + w / 2, y - gap / 2, c, 3.5) + line(x - w / 2, y + gap / 2, x + w / 2, y + gap / 2, c, 3.5)
    return line(x - gap / 2, y - w / 2, x - gap / 2, y + w / 2, c, 3.5) + line(x + gap / 2, y - w / 2, x + gap / 2, y + w / 2, c, 3.5)

def acsrc(x, y, r=18, c=INK):
    p = ' '.join(f'{x - r * .6 + i * r * 1.2 / 20:.1f},{y - r * .35 * math.sin(i / 20 * 2 * pi):.1f}' for i in range(21))
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{W}" stroke="{c}" stroke-width="3"/><polyline points="{p}" fill="none" stroke="{c}" stroke-width="2.5"/>'

def dcsrc(x, y, c=INK):
    # battery, wire vertical through x; + plate on top
    return (line(x - 16, y - 5, x + 16, y - 5, c, 3.5) + line(x - 8, y + 5, x + 8, y + 5, c, 5)
            + txt(x + 24, y - 4, '+', 15, c, 900))

def sw(x, y, lab='S', c=INK, sz=30):
    return rbox(x - sz / 2, y - sz / 2, sz, sz, lab, c, 13, fill=W, sw=2.5, r=7)

def node(x, y, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{c}"/>'


def wave(p, f, a, b, n=240, c=G, w=4, dash=None):
    return p.curve(f, a, b, n, c, w, dash)

def triac(x, y, s=11, c=INK, gate=True):
    # vertical TRIAC/DIAC between y - s and y + s: two antiparallel triangles between two bars
    o = line(x - 18, y - s, x + 18, y - s, c, 3.5) + line(x - 18, y + s, x + 18, y + s, c, 3.5)
    o += f'<polygon points="{x - 17},{y - s} {x - 1},{y - s} {x - 9},{y + s}" fill="{c}"/>'
    o += f'<polygon points="{x + 1},{y + s} {x + 17},{y + s} {x + 9},{y - s}" fill="{c}"/>'
    if gate:
        o += line(x + 9, y + s, x + 26, y + s + 14, c, 3)
    return o

def lamp(x, y, r=15, c=INK):
    d = r * .7
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFF6D6" stroke="{c}" stroke-width="3"/>'
            + line(x - d, y - d, x + d, y + d, c, 2.5) + line(x - d, y + d, x + d, y - d, c, 2.5))

def stepline(p, f, a, b, n=2000):
    pts = []; prev = None
    for k in range(n + 1):
        x = a + (b - a) * k / n; y = f(x)
        if prev is not None and y != prev: pts.append(p.P(x, prev))
        pts.append(p.P(x, y)); prev = y
    return pts

def ptstr(pts):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)

def area(p, f, a, b, fill, n=120, base=0, op=.55):
    pts = [p.P(a, base)] + [p.P(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)] + [p.P(b, base)]
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" fill-opacity="{op}" stroke="none"/>'



# =====================================================================
# Unit 1
# =====================================================================
def u1L1():
    # hook: does removing the gate turn off an SCR?  SCR into R = 20 ohm, L = 0.5 H from 100 V; IL = 50 mA
    V, Rr, Ll, IL = 100, 20, 0.5, 0.05
    tau = Ll / Rr
    i = lambda t_us: V / Rr * (1 - math.exp(-t_us * 1e-6 / tau)) * 1000  # mA
    tmin = -tau * math.log(1 - IL * Rr / V) * 1e6  # us, 251
    s = defs()
    y0, y1 = 18, 92
    s += wire([(20, 50), (20, y0), (128, y0)]) + dcsrc(20, 55) + wire([(20, 60), (20, y1), (300, y1), (300, y0), (262, y0)])
    s += scr(140, y0, 'r') + wire([(152, y0), (180, y0)]) + res(180, y0, 220, y0) + ind(222, y0, 262, y0)
    s += txt(48, 62, f'{V} V', 13, INK, 800, 'start') + txt(200, y0 + 30, f'{Rr} Ω', 12, MUT, 800) + txt(242, y0 + 30, f'{Ll} H', 12, MUT, 800)
    s += txt(152, y0 + 40, 'gate', 12, O, 900, 'start')
    s += rtag(486, 44, 'latch at I_{L} = 50 mA', B, 13, 'end')
    p = Plot(0, 400, 0, 80, L=56, T=128, Wd=420, H=180)
    s += p.axes(xt=(0, 100, 200, 300, 400), yt=(0, 20, 40, 60, 80), xl='t in µs →', yl='anode current (mA)')
    s += rect(p.X(0), p.T + p.H - 26, p.X(tmin) - p.X(0), 24, OS, O, 2, 5) + txt((p.X(0) + p.X(tmin)) / 2, p.T + p.H - 9, 'gate pulse on', 12, O, 900)
    s += txt((p.X(tmin) + p.X(400)) / 2, p.T + p.H - 9, 'gate off', 12, MUT, 900)
    s += line(p.L, p.Y(50), p.L + p.W, p.Y(50), B, 2.5, '7 7')
    s += wave(p, i, 0, 400, c=G, w=5)
    s += line(p.X(tmin), p.Y(50), p.X(tmin), p.T + p.H, O, 2.5, '5 6') + dot(*p.P(tmin, i(tmin)), 9, O)
    s += tag(p.X(tmin) - 8, p.Y(50) - 14, f'{tmin:.0f} µs', O, 13, 'end')
    s += txt(p.X(352), p.Y(i(352)) - 18, 'still on', 15, G, 900)
    return 'Gate off, current keeps going', s
D['ee-pe-u1-L1'] = (u1L1, 'gate off, still on', '1.2.1')


def u1L2():
    # hook: does a DIAC carry the lamp current?  230 V dimmer, alpha = 90, 100 ohm lamp
    Vs, a, Rl = 230, 90, 100
    Vo = Vs * math.sqrt(1 - rad(a) / pi + math.sin(2 * rad(a)) / (2 * pi))
    Il = Vo / Rl; P = Vo ** 2 / Rl
    s = defs()
    xL, xR, xRC, yT, yB = 30, 330, 200, 26, 200
    yG = 150
    s += wire([(xL, 93), (xL, yT), (130, yT)]) + lamp(150, yT) + wire([(165, yT), (xR, yT), (xR, 80)])
    s += acsrc(xL, 111) + wire([(xL, 129), (xL, yB), (xR, yB), (xR, 128)])
    s += triac(xR, 104, 18, O, gate=False) + line(xR - 9, 122, xR - 24, 136, O, 3) + wire([(xR - 24, 136), (xR - 24, yG)], O)
    s += node(xR, 52) + wire([(xR, 52), (xRC, 52), (xRC, 64)]) + res(xRC, 64, xRC, 112) + wire([(xRC, 112), (xRC, yG)]) + node(xRC, yG)
    s += wire([(xRC, yG), (xRC, 168)]) + cap(xRC, 172) + wire([(xRC, 176), (xRC, yB)]) + node(xRC, yB) + node(xR, yB)
    s += wire([(xRC, yG), (232, yG)], B) + f'<g transform="rotate(-90 250 {yG})">{triac(250, yG, 13, B, gate=False)}</g>' + wire([(268, yG), (xR - 24, yG)], B)
    s += txt(150, yT + 32, 'lamp', 12, MUT, 800) + txt(xRC - 16, 92, 'R', 13, MUT, 900, 'end') + txt(xRC - 18, 178, 'C', 13, MUT, 900, 'end')
    s += txt(250, yG + 32, 'DIAC', 12, B, 900) + txt(xR + 26, 110, 'TRIAC', 13, O, 900, 'start')
    s += rtag(492, 60, f'lamp: {Il:.2f} A', O, 13, 'end') + rtag(492, 190, '30 V pulse only', B, 13, 'end')
    p = Plot(0, 360, -340, 340, L=40, T=236, Wd=450, H=110)
    sup = lambda th: math.sqrt(2) * Vs * math.sin(rad(th))
    on = lambda th: sup(th) if (th % 180) >= a else 0
    s += wave(p, sup, 0, 360, c=MUT, w=2, dash='5 6') + area(p, on, 0, 360, GS, n=720, op=1) + wave(p, on, 0, 360, n=720, c=G, w=4)
    s += line(p.L, p.Y(0), p.L + p.W, p.Y(0), MUT, 1.5)
    s += txt(p.X(45), p.Y(-120), f'α = {a}°', 13, O, 900) + txt(p.X(270), p.Y(170), f'lamp {Vo:.1f} V, {P:.1f} W', 13, G, 900)
    return 'The TRIAC carries the lamp', s
D['ee-pe-u1-L2'] = (u1L2, 'DIAC only triggers', '1.5.1')


def u1L3():
    # hook: does a snubber cut the total loss?  10 A off a 400 V link, 20 kHz, dv/dt <= 500 V/us, 2 A discharge
    I, V, f, dvdt = 10, 400, 20e3, 500e6
    Cs = I / dvdt; Rs = V / 2; E_ = .5 * Cs * V ** 2; P = E_ * f
    s = defs()
    xs, xn, yT, yB = 60, 160, 30, 216
    s += wire([(xs, yT), (xs, 102)]) + sw(xs, 124, 'IGBT', INK, 44) + wire([(xs, 146), (xs, yB)])
    s += wire([(xs, yT), (xn, yT), (xn, 56)]) + cap(xn, 60) + wire([(xn, 64), (xn, 92)]) + node(xn, 92)
    s += wire([(xn, 92), (xn - 24, 92), (xn - 24, 102)]) + res(xn - 24, 102, xn - 24, 150) + wire([(xn - 24, 150), (xn - 24, 162), (xn + 24, 162), (xn + 24, 140)])
    s += diode(xn + 24, 127, 'd') + wire([(xn + 24, 114), (xn + 24, 92), (xn, 92)]) + node(xn, 162)
    s += wire([(xn, 162), (xn, yB), (xs, yB)])
    s += txt(xn + 20, 66, f'C_{{s}} {Cs * 1e9:.0f} nF', 13, B, 900, 'start') + txt(xn - 36, 124, 'R_{s}', 13, O, 900, 'end') + txt(xn - 36, 142, f'{Rs:.0f} Ω', 12, O, 800, 'end')
    s += txt(xs - 6, yT - 8, f'{V} V link', 13, INK, 900, 'start') + txt(xs + 8, yB - 12, f'{I} A off', 12, MUT, 800, 'start')
    p = Plot(0, 1.6, 0, 440, L=290, T=40, Wd=200, H=140)
    s += p.axes(xt=(0, .8, 1.6), yt=(0, 400), xl='t in µs', yl='v_{switch}', fmt=lambda v: f'{v:g}')
    s += wave(p, lambda t: min(V, dvdt * t * 1e-6), 0, 1.6, c=B, w=5)
    s += tag(p.X(1.6), p.Y(150), f'{dvdt / 1e6:.0f} V/µs', B, 12, 'end')
    s += rbox(14, 246, 220, 64, f'{E_ * 1e3:.1f} mJ', B, 20, fill=BS, sub='½ C_{s}V² each turn-off', ss=13)
    s += line(238, 278, 262, 278, MUT, 3, arrow=True)
    s += rbox(266, 246, 226, 64, f'{P:.0f} W', O, 20, fill=OS, sub=f'× {f / 1e3:.0f} kHz, burnt in R_{{s}}', ss=13)
    s += txt(250, 346, 'moved out of the switch, not saved:', 14, INK, 900) + txt(250, 370, 'the total loss does not drop', 14, O, 900)
    return 'Where the snubber puts the loss', s
D['ee-pe-u1-L3'] = (u1L3, '32 W lands in Rs', '1.7.1')


# =====================================================================
# Unit 2
# =====================================================================
Vm230 = math.sqrt(2) * 230

def u2L1():
    # hook: is half-wave DC really 0.637 Vm?  230 V, 50 Hz
    Vm = Vm230
    hw, fw = Vm / pi, 2 * Vm / pi
    p = Plot(0, 40, -340, 340, L=58, T=14, Wd=420, H=300)
    s = defs() + p.axes(xt=(0, 10, 20, 30, 40), yt=(-325, 0, 104, 207, 325), xl='t in ms →', yl='volts', fmt=lambda v: f'{v}'.replace('-', '−'))
    sup = lambda t: Vm * math.sin(2 * pi * 50 * t / 1000)
    half = lambda t: max(0, sup(t))
    s += wave(p, sup, 0, 40, c=MUT, w=2.5, dash='6 6')
    s += area(p, half, 0, 40, GS, n=400, op=1) + wave(p, half, 0, 40, n=400, c=G, w=5)
    s += line(p.L, p.Y(fw), p.L + p.W, p.Y(fw), B, 2.5, '8 6') + line(p.L, p.Y(hw), p.L + p.W, p.Y(hw), O, 3.5)
    s += tag(p.X(40), p.Y(fw) - 12, f'full-wave 2V_{{m}}/π = {fw:.0f} V', B, 13, 'end')
    s += tag(p.X(40), p.Y(hw) + 30, f'half-wave V_{{m}}/π = {hw:.1f} V', O, 13, 'end')
    s += txt(p.X(15), p.Y(-150), 'diode blocks', 13, MUT, 900)
    return 'Half-wave: one hump a cycle', s
D['ee-pe-u2-L1'] = (u2L1, '0.318 Vm, not 0.637', '2.1.1')


def u2L2():
    # hook: does cos(alpha) work for a resistive load?  full bridge 230 V, R = 10 ohm, alpha = 60
    Vm = Vm230; a = 60
    vR = Vm / pi * (1 + math.cos(rad(a))); vL = 2 * Vm / pi * math.cos(rad(a))
    p = Plot(0, 360, -340, 340, L=58, T=16, Wd=420, H=230)
    s = defs() + p.axes(xt=(0, 60, 180, 240, 360), yt=(-325, 0, 104, 155, 325), xl='ωt in degrees →', fmt=lambda v: f'{v}'.replace('-', '−'))
    rl = lambda th: abs(Vm * math.sin(rad(th))) if (th % 180) >= a else 0
    ll = lambda th: Vm * math.sin(rad(th)) * (1 if ((th - a) % 360) < 180 else -1)
    s += area(p, rl, 0, 360, GS, n=720, op=1) + wave(p, rl, 0, 360, n=720, c=G, w=5)
    s += poly(stepline(p, ll, 0, 360, 1440), O, 3, '8 6')
    s += line(p.L, p.Y(0), p.L + p.W, p.Y(0), MUT, 1.5)
    s += line(p.L, p.Y(vR), p.L + p.W, p.Y(vR), G, 3) + line(p.L, p.Y(vL), p.L + p.W, p.Y(vL), O, 3, '8 6')
    s += line(20, 316, 52, 316, G, 4) + rt(60, 321, f'R load: (V_{{m}}/π)(1 + cos α) = {vR:.1f} V', 14, G, 900, 'start')
    s += line(20, 348, 52, 348, O, 3, '8 6') + rt(60, 353, f'large L: (2V_{{m}}/π) cos α = {vL:.1f} V', 14, O, 900, 'start')
    return 'Same α = 60°, two loads', s
D['ee-pe-u2-L2'] = (u2L2, 'R load: 1 + cos α', '2.4.1')


def u2L3():
    # hook: where is alpha measured in three phase?  400 V line, alpha = 30
    Vph = 400 / math.sqrt(3) * math.sqrt(2); a = 30
    Vdc = 3 * math.sqrt(2) * 400 / pi * math.cos(rad(a))
    p = Plot(0, 360, -360, 400, L=44, T=20, Wd=446, H=270)
    s = defs() + p.axes(xt=(0, 30, 90, 180, 270, 360), yt=(), xl='ωt in degrees →')
    s += line(p.L, p.Y(0), p.L + p.W, p.Y(0), GRID, 2)
    for k, (c, n) in enumerate(((B, 'v_{a}'), (MUT, 'v_{b}'), (MUT, 'v_{c}'))):
        s += wave(p, lambda th, k=k: Vph * math.sin(rad(th - 120 * k)), 0, 360, c=c, w=4 if k == 0 else 2.5, dash=None if k == 0 else '6 6')
    s += txt(p.X(96), p.Y(Vph) - 10, 'v_{a}', 15, B, 900) + txt(p.X(216), p.Y(Vph) - 10, 'v_{b}', 14, MUT, 900) + txt(p.X(336), p.Y(Vph) - 10, 'v_{c}', 14, MUT, 900)
    x30 = Vph * math.sin(rad(30))
    s += line(p.X(30), p.T + p.H, p.X(30), p.Y(x30), G, 2.5, '5 5') + ring(*p.P(30, x30), 9)
    s += line(p.X(30), p.Y(x30) - 52, p.X(30 + a), p.Y(x30) - 52, O, 3, arrow=True) + line(p.X(60), p.Y(x30) - 64, p.X(60), p.T + p.H, O, 2.5, '5 5')
    s += txt(p.X(45), p.Y(x30) - 62, f'α = {a}°', 14, O, 900)
    s += tag(p.X(30) + 6, p.Y(-120), 'α = 0 here: v_{a} = v_{c}', G, 13, 'start')
    s += tag(p.X(0) + 2, p.Y(-300), 'not at the zero crossing', MUT, 12, 'start')
    s += tag(p.X(360), p.Y(-300), f'V_{{dc}} = {Vdc:.1f} V', INK, 13, 'end')
    return 'α starts at the crossing', s
D['ee-pe-u2-L3'] = (u2L3, '30° after the zero', '2.5.1')


def u2L4():
    # hook: does DC current reverse in inversion?  1-phase bridge 230 V, alpha = 120, E = -120 V, R = 2 ohm
    Vm = Vm230; a = 120; E_, Rr = -120, 2
    Vdc = 2 * Vm / pi * math.cos(rad(a)); Id = (Vdc - E_) / Rr; Pb = -Vdc * Id
    p = Plot(0, 360, -340, 340, L=58, T=14, Wd=420, H=196)
    s = defs() + p.axes(xt=(), yt=(-325, -104, 0, 325), fmt=lambda v: f'{v}'.replace('-', '−'))
    vo = lambda th: Vm * math.sin(rad(th)) * (1 if ((th - a) % 360) < 180 else -1)
    s += area(p, vo, 0, 360, OS, n=720, op=.9)
    s += poly(stepline(p, vo, 0, 360, 1440), O, 4)
    s += line(p.L, p.Y(0), p.L + p.W, p.Y(0), MUT, 1.5) + line(p.L, p.Y(Vdc), p.L + p.W, p.Y(Vdc), INK, 3, '8 6')
    s += tag(p.X(360), p.Y(Vdc) + 30, f'V_{{dc}} = {Vdc:.1f} V', INK, 13, 'end') + txt(p.X(30), p.Y(260), f'α = {a}°', 13, O, 900)
    q = Plot(0, 360, -12, 12, L=58, T=234, Wd=420, H=90)
    s += q.axes(xt=(0, 90, 180, 270, 360), yt=(-10, 0, 10), xl='ωt in degrees →', fmt=lambda v: f'{v}'.replace('-', '−'))
    s += line(q.L, q.Y(0), q.L + q.W, q.Y(0), MUT, 1.5)
    s += line(q.L, q.Y(Id), q.L + q.W, q.Y(Id), G, 6)
    s += tag(q.X(180), q.Y(Id) + 34, f'I_{{d}} = +{Id:.2f} A, same way', G, 13)
    return 'V flips, current does not', s
_vd = 2 * Vm230 / pi * math.cos(rad(120)); _id = (_vd + 120) / 2
D['ee-pe-u2-L4'] = (u2L4, f'{-_vd * _id:.0f} W back, I still +', '2.8.1')


def u2L5():
    # hook: does a big capacitor fix power factor?  boost PFC 500 W, 230 V, 400 V bus, L = 1 mH, 65 kHz
    P, Vs, Vb, L, fs = 500, 230, 400, 1e-3, 65e3
    Ipk = math.sqrt(2) * P / Vs; Vm = math.sqrt(2) * Vs
    dI = lambda v: v * (1 - v / Vb) / (L * fs)
    iL = lambda t: Ipk * abs(math.sin(2 * pi * 50 * t / 1000))
    vv = lambda t: Vm * abs(math.sin(2 * pi * 50 * t / 1000))
    p = Plot(0, 20, 0, 4.2, L=50, T=24, Wd=440, H=200)
    s = defs() + p.axes(xt=(0, 5, 10, 15, 20), yt=(0, 1, 2, 3), xl='t in ms →', yl='i_{L} (A)')
    up = [p.P(k / 20, iL(k / 20) + dI(vv(k / 20)) / 2) for k in range(401)]
    dn = [p.P(k / 20, max(0, iL(k / 20) - dI(vv(k / 20)) / 2)) for k in range(400, -1, -1)]
    s += f'<polygon points="{ptstr(up + dn)}" fill="{GS}" stroke="{G}" stroke-width="1.2"/>'
    s += wave(p, iL, 0, 20, c=G, w=4.5)
    s += tag(p.X(10), p.Y(4.0), f'in step with |v_{{s}}|: peak {Ipk:.2f} A', G, 13)
    # capacitor-only inset
    s += rect(14, 270, 230, 96, '#FFF4F0', O, 2, 12) + txt(129, 292, 'capacitor alone: 19° pulses', 13, O, 900)
    q = Plot(0, 360, 0, 1, L=26, T=300, Wd=206, H=54)
    s += wave(q, lambda th: abs(math.sin(rad(th))), 0, 360, c=MUT, w=1.6, dash='4 4')
    for c0 in (90, 270):
        s += poly([q.P(c0 - 19, 0), q.P(c0 - 12, .75), q.P(c0 - 3, .95), q.P(c0, 0)], O, 3.5)
    s += rbox(262, 270, 230, 96, 'PF 0.5 to 0.7', O, 19, fill=W, sub='a capacitor causes it', ss=14)
    return 'Boost PFC follows the sine', s
D['ee-pe-u2-L5'] = (u2L5, 'PFC: PF = 1', '2.10.1')


# =====================================================================
# Unit 3
# =====================================================================
def u3L1():
    # hook: is duty ratio on-time or off-time?  200 V, Ton = 0.4 ms at 1 kHz and 2 kHz
    Vs, ton = 200, .4
    s = defs()
    for row, (T, c, fill) in enumerate(((1.0, G, GS), (0.5, O, OS))):
        p = Plot(0, 2, 0, 200, L=60, T=58 + row * 158, Wd=420, H=84)
        D_ = ton / T; Vo = D_ * Vs
        pts = []; t = 0
        while t < 2 - 1e-9:
            pts += [p.P(t, 0), p.P(t, Vs), p.P(min(t + ton, 2), Vs), p.P(min(t + ton, 2), 0)]
            t += T
        pts.append(p.P(2, 0))
        s += f'<polygon points="{ptstr(pts)}" fill="{fill}" stroke="{c}" stroke-width="3.5" stroke-linejoin="round"/>'
        s += line(p.L, p.Y(Vo), p.L + p.W, p.Y(Vo), INK, 2.5, '7 6')
        s += line(p.L, p.T + p.H, p.L + p.W + 6, p.T + p.H, MUT, 2.5)
        s += txt(p.L - 8, p.Y(200) + 5, '200', 12, MUT, 700, 'end') + txt(p.L - 8, p.Y(0) + 5, '0', 12, MUT, 700, 'end')
        s += rtag(p.L + p.W, p.T - 14, f'V_{{o}} = {Vo:.0f} V', INK, 13, 'end')
        # brackets: on-time over the first pulse, period over the first cycle
        yb = p.T - 12
        s += line(p.X(0), yb, p.X(ton), yb, c, 2.5, arrow=True) + line(p.X(ton), yb, p.X(0), yb, c, 2.5, arrow=True)
        s += txt(p.X(ton / 2), yb - 8, 'T_{on}', 13, c, 900)
        yb2 = p.T + p.H + 20
        s += line(p.X(0), yb2, p.X(T), yb2, MUT, 2.5, arrow=True) + line(p.X(T), yb2, p.X(0), yb2, MUT, 2.5, arrow=True)
        s += txt(p.X(T) + 8, yb2 + 5, f'T = {T:g} ms:  D = {ton}/{T:g} = {D_:.1f}', 13, c, 900, 'start')
    return 'D = on-time ÷ period', s
D['ee-pe-u3-L1'] = (u3L1, 'D = Ton / T', '3.1.1')


def u3L2():
    # hook: which gain formula fits a boost?  24 V, D = 0.6 -> 60 V, R = 100 ohm
    Vs, Dd = 24, .6
    Vo = Vs / (1 - Dd)
    s = defs()
    y0, y1 = 22, 94
    s += wire([(24, 50), (24, y0), (60, y0)]) + dcsrc(24, 57) + wire([(24, 62), (24, y1)])
    s += ind(60, y0, 120, y0) + wire([(120, y0), (172, y0)]) + node(150, y0) + diode(184, y0, 'r') + wire([(196, y0), (300, y0)])
    s += wire([(150, y0), (150, 42)]) + sw(150, 58, 'S', O) + wire([(150, 74), (150, y1)])
    s += node(240, y0) + wire([(240, y0), (240, 53)]) + cap(240, 57) + wire([(240, 61), (240, y1)])
    s += wire([(300, y0), (300, 37)]) + res(300, 37, 300, 77) + wire([(300, 77), (300, y1)]) + wire([(24, y1), (300, y1)])
    s += txt(50, 64, f'{Vs} V', 13, INK, 800, 'start') + txt(90, y0 - 10, '300 µH', 12, MUT, 800) + txt(320, 61, f'{Vo:.0f} V', 15, O, 900, 'start')
    p = Plot(0, .8, 0, 5.4, L=52, T=124, Wd=430, H=196)
    s += p.axes(xt=(0, .2, .4, .6, .8), yt=(0, 1, 2.5, 5), xl='duty ratio D →', yl='V_{o} / V_{s}', fmt=lambda v: f'{v:g}')
    s += line(p.L, p.Y(1), p.L + p.W, p.Y(1), MUT, 2, '6 6')
    s += wave(p, lambda d: 1 / (1 - d), 0, .8, c=O, w=6) + wave(p, lambda d: d, 0, .8, c=B, w=3, dash='7 6')
    s += line(p.X(Dd), p.Y(Vo / Vs), p.X(Dd), p.T + p.H, O, 2.5, '5 5') + dot(*p.P(Dd, Vo / Vs), 10, O)
    s += tag(p.X(Dd) - 12, p.Y(Vo / Vs) - 14, f'1/(1 − {Dd}) = {Vo / Vs:g}', O, 13, 'end')
    s += tag(p.X(.8), p.Y(.8) + 30, 'buck: D', B, 12, 'end')
    return 'Boost: 1 ÷ (1 − D)', s
D['ee-pe-u3-L2'] = (u3L2, '24 V → 60 V', '3.4.1')


def u3L3():
    # hook: is flyback output just Vs*D*N2/N1?  48 V, N1 = 40, N2 = 20, D = 0.4
    Vs, N1, N2, Dd = 48, 40, 20, .4
    Vo = Vs * Dd / (1 - Dd) * N2 / N1; wrong = Vs * Dd * N2 / N1
    s = defs()
    # primary loop
    s += wire([(24, 70), (24, 24), (130, 24), (130, 38)]) + dcsrc(24, 80) + wire([(24, 90), (24, 196), (130, 196), (130, 178)])
    s += ind(130, 40, 130, 120, n=4) + wire([(130, 120), (130, 146)]) + sw(130, 162, 'S', O)
    s += line(150, 36, 150, 124, INK, 2.5) + line(158, 36, 158, 124, INK, 2.5)
    s += ind(178, 120, 178, 40, n=4) + f'<circle cx="118" cy="44" r="4.5" fill="{INK}"/><circle cx="190" cy="116" r="4.5" fill="{INK}"/>'
    s += wire([(178, 40), (178, 24), (230, 24)]) + diode(242, 24, 'r') + wire([(254, 24), (330, 24), (330, 58)])
    s += wire([(178, 120), (178, 136), (330, 136), (330, 98)]) + node(290, 24) + wire([(290, 24), (290, 72)]) + cap(290, 76) + wire([(290, 80), (290, 136)]) + node(290, 136)
    s += res(330, 58, 330, 98)
    s += txt(46, 86, f'{Vs} V', 13, INK, 800, 'start') + txt(118, 142, f'N_{{1}} = {N1}', 12, MUT, 900, 'end') + txt(196, 84, f'N_{{2}} = {N2}', 12, MUT, 900, 'start')
    s += txt(346, 84, f'{Vo:.0f} V', 16, G, 900, 'start')
    s += rbox(14, 222, 230, 92, f'{wrong:.1f} V', O, 24, fill=OS, sub='V_{s}·D·N_{2}/N_{1}', ss=15)
    s += rbox(262, 222, 230, 92, f'{Vo:.0f} V', G, 24, fill=GS, sub='V_{s}·D/(1 − D)·N_{2}/N_{1}', ss=15)
    s += txt(129, 340, '✗ that is the forward', 14, O, 900) + txt(377, 340, '✓ flyback, D = 0.4', 14, G, 900)
    s += txt(250, 370, 'stores energy while S is on, delivers while off', 13, MUT, 800)
    return 'Flyback has the (1 − D)', s
D['ee-pe-u3-L3'] = (u3L3, '16 V, not 9.6 V', '3.6.1')


def u3L4():
    # hook: size the inductor from average current?  L = 100 uH, Io = 4 A, dI = 1.2 A, Ae = 1 cm2, Bmax = 0.3 T
    L, Io, dI, Ae, Bm = 100e-6, 4, 1.2, 1e-4, .3
    Ipk = Io + dI / 2
    N = math.ceil(L * Ipk / (Bm * Ae)); B_ = L * Ipk / (N * Ae)
    Nav = math.ceil(L * Io / (Bm * Ae)); Bav = L * Ipk / (Nav * Ae)
    gap = 4 * pi * 1e-7 * N * N * Ae / L * 1e3
    s = defs()
    p = Plot(0, 20, 3, 5, L=50, T=40, Wd=210, H=180)
    s += p.axes(xt=(0, 10, 20), yt=(3.4, 4, 4.6), xl='t in µs', yl='i_{L} (A)', fmt=lambda v: f'{v:g}')
    pts = []
    for k in range(2):
        pts += [p.P(k * 10, Io - dI / 2), p.P(k * 10 + 4, Ipk)]
    pts.append(p.P(20, Io - dI / 2))
    s += poly(pts, G, 5) + line(p.L, p.Y(Io), p.L + p.W, p.Y(Io), B, 2.5, '6 6')
    s += ring(*p.P(4, Ipk), 9) + tag(p.X(4) + 14, p.Y(Ipk) - 14, f'peak {Ipk} A', O, 13, 'start')
    s += txt(p.X(10), p.Y(3.17), f'dashed: average {Io} A', 12, B, 900)
    # E core with the winding on the centre leg
    cx, cy = 390, 128
    s += rect(cx - 96, cy - 92, 192, 184, '#D9DEE8', INK, 2.5, 6)
    s += rect(cx - 70, cy - 66, 44, 132, W, INK, 2, 3) + rect(cx + 26, cy - 66, 44, 132, W, INK, 2, 3)
    s += rect(cx - 26, cy - 4, 52, 8, W, O, 0, 0)
    for k in range(8):
        y = cy - 60 + k * 15
        s += line(cx - 32, y, cx + 32, y + 6, O, 3.5)
    s += txt(cx, cy + 106, f'{N} turns, gap {gap:.2f} mm', 13, INK, 900)
    s += tag(cx + 100, cy - 104, f'B = {B_:.2f} T', G, 13, 'end')
    s += rbox(14, 272, 236, 72, f'N = {N}', G, 20, fill=GS, sub=f'from {Ipk} A: B = {B_:.2f} T ✓', ss=14)
    s += rbox(264, 272, 228, 72, f'N = {Nav}', O, 20, fill=OS, sub=f'from {Io} A: B = {Bav:.2f} T ✗', ss=14)
    s += txt(250, 368, f'B_{{max}} = {Bm} T: the peak sets the turns', 13, MUT, 800)
    return 'Size the core at the peak', s
D['ee-pe-u3-L4'] = (u3L4, '4.6 A, not 4 A', '3.8.1')

# =====================================================================
# Unit 4
# =====================================================================
def u4L1():
    # hook: is the fundamental peak just Vdc?  full bridge, 300 V bus, 50 Hz square wave
    V = 300; b1 = 4 * V / pi
    thd = math.sqrt(V ** 2 - (b1 / math.sqrt(2)) ** 2) / (b1 / math.sqrt(2))
    p = Plot(0, 40, -420, 420, L=58, T=16, Wd=420, H=280)
    s = defs() + p.axes(xt=(0, 10, 20, 30, 40), yt=(-300, 0, 300), xl='t in ms →', yl='v_{o}', fmt=lambda v: f'{v}'.replace('-', '−'))
    pts = []
    for k in range(4):
        y = V if k % 2 == 0 else -V
        pts += [p.P(k * 10, y), p.P(k * 10 + 10, y)]
    s += poly(pts, O, 5)
    s += wave(p, lambda t: b1 * math.sin(2 * pi * t / 20), 0, 40, c=B, w=4)
    s += line(p.L, p.Y(0), p.L + p.W, p.Y(0), MUT, 1.5)
    s += dot(*p.P(5, b1), 8, B) + tag(p.X(5) + 14, p.Y(b1) - 4, f'4V_{{dc}}/π = {b1:.0f} V', B, 13, 'start')
    s += tag(p.X(40), p.Y(-360) + 4, f'THD = {thd * 100:.1f} %', INK, 13, 'end')
    s += tag(p.X(20), p.Y(-360) + 4, f'±{V} V square', O, 13)
    return 'The sine inside the square', s
D['ee-pe-u4-L1'] = (u4L1, '1.27 × Vdc, not Vdc', '4.1.1')


def u4L2():
    # hook: how far can SVM push the voltage?  600 V bus; vectors 2Vdc/3; reference 300 V at 20 deg
    Vdc, Vref, th = 600, 300, 20
    Va = 2 * Vdc / 3; Rsv = Vdc / math.sqrt(3); Rsp = Vdc / 2
    Ts = 1e6 / 6000; m = math.sqrt(3) * Vref / Vdc
    T1 = m * Ts * math.sin(rad(60 - th)); T2 = m * Ts * math.sin(rad(th))
    cx, cy, k = 170, 176, 128 / Va
    s = defs()
    hexp = [(cx + Va * k * math.cos(rad(60 * i)), cy - Va * k * math.sin(rad(60 * i))) for i in range(6)]
    s += f'<polygon points="{ptstr(hexp)}" fill="{GS}" stroke="{G}" stroke-width="3"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="{Rsv * k:.1f}" fill="none" stroke="{O}" stroke-width="3.5"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="{Rsp * k:.1f}" fill="none" stroke="{B}" stroke-width="2.5" stroke-dasharray="7 6"/>'
    names = ['100', '110', '010', '011', '001', '101']
    for i, (x, y) in enumerate(hexp):
        s += line(cx, cy, x, y, MUT, 1.8)
        dx, dy = math.cos(rad(60 * i)), -math.sin(rad(60 * i))
        s += dot(x, y, 6, G) + txt(x + dx * 26, y + dy * 20 + 5, names[i], 12, G, 900)
    s += line(cx, cy, cx + Vref * k * math.cos(rad(th)), cy - Vref * k * math.sin(rad(th)), INK, 4, arrow=True)
    s += dot(cx, cy, 6, INK)
    s += tag(500, 40, f'SVM: V_{{dc}}/√3 = {Rsv:.1f} V', O, 13, 'end')
    s += tag(500, 76, f'sine PWM: V_{{dc}}/2 = {Rsp:.0f} V', B, 13, 'end')
    s += tag(500, 112, f'vectors 2V_{{dc}}/3 = {Va:.0f} V', G, 13, 'end')
    s += txt(14, 340, f'SVM reaches {Rsv / Rsp:.3f} × the sine-PWM peak: {100 * (Rsv / Rsp - 1):.1f} % more', 14, INK, 900, 'start')
    s += txt(14, 366, f'arrow: {Vref} V at {th}°, dwell T_{{1}} = {T1:.1f} µs, T_{{2}} = {T2:.1f} µs', 13, MUT, 800, 'start')
    return 'The circle inside the hexagon', s
D['ee-pe-u4-L2'] = (u4L2, 'phase peak Vdc/√3', '4.5.1')


def u4L3():
    # hook: what does each NPC switch block?  three-level NPC leg on 600 V
    Vdc = 600; dv = Vdc / 2
    s = defs()
    xb, xs, xo = 76, 220, 270
    ys = [56, 116, 196, 256]
    yT, yN, yB = 24, 156, 290
    # bus capacitors
    s += wire([(xb, yT), (xb, 84)]) + cap(xb, 90) + wire([(xb, 94), (xb, yN)]) + wire([(xb, yN), (xb, 218)]) + cap(xb, 222) + wire([(xb, 226), (xb, yB)])
    s += txt(xb - 16, 95, f'{dv:.0f} V', 13, B, 900, 'end') + txt(xb - 16, 227, f'{dv:.0f} V', 13, B, 900, 'end')
    s += wire([(xb, yT), (xs, yT)]) + wire([(xb, yB), (xs, yB)]) + node(xb, yN) + txt(xb - 10, yN + 5, 'N', 15, INK, 900, 'end')
    # switch string
    s += wire([(xs, yT), (xs, yB)])
    for i, y in enumerate(ys):
        s += sw(xs, y, f'S{i + 1}', O, 34) + txt(xs + 30, y + 5, f'blocks {dv:.0f} V', 12, O, 900, 'start')
    s += node(xs, 86) + node(xs, 226) + node(xs, yN)
    # clamping diodes from N to the inner nodes
    s += wire([(xb, yN), (150, yN), (150, 112)]) + diode(150, 100, 'u', 10, B) + wire([(150, 88), (150, 86), (xs, 86)])
    s += wire([(150, yN), (150, 200)]) + diode(150, 212, 'u', 10, B) + wire([(150, 224), (150, 226), (xs, 226)])
    s += txt(136, 104, 'D1', 12, B, 900, 'end') + txt(136, 216, 'D2', 12, B, 900, 'end')
    s += wire([(xs, yN), (300, yN)]) + txt(306, yN + 5, 'out', 13, INK, 900, 'start')
    # state table
    rows = [('S1 S2', f'+{dv:.0f} V', G), ('S2 S3', '0 V', B), ('S3 S4', f'−{dv:.0f} V', O)]
    for i, (a, b, c) in enumerate(rows):
        y = 214 + i * 34
        s += rbox(372, y - 24, 122, 30, f'{a}: {b}', c, 13, fill=W, sw=2, r=10)
    s += txt(432, 180, f'{Vdc} V bus', 14, INK, 900)
    return 'Three levels, half the stress', s
D['ee-pe-u4-L3'] = (u4L3, 'each switch: 300 V', '4.8.1')


# =====================================================================
# Unit 5
# =====================================================================
def u5L1():
    # hook: does a + gate pulse always mean Q1?  TRIAC triggering quadrants (MT2 and gate measured from MT1)
    cx, cy = 250, 176
    s = defs()
    quads = [(1, 1, 'Q1', 'MT2 +, gate +', 'least gate current', G, GS),
             (-1, 1, 'Q2', 'MT2 +, gate −', 'low to medium', MUT, W),
             (-1, -1, 'Q3', 'MT2 −, gate −', 'low to medium', MUT, W),
             (1, -1, 'Q4', 'MT2 −, gate +', 'most: about 2 ×', O, OS)]
    for sx, sy, q, a, b, c, fill in quads:
        x0 = cx + 8 if sx > 0 else cx - 218; y0 = cy - 146 if sy > 0 else cy + 8
        s += rect(x0, y0, 210, 138, fill, c, 2.5 if fill != W else 1.5, 14)
        s += txt(x0 + 105, y0 + 48, q, 30, c if c != MUT else INK, 900)
        s += txt(x0 + 105, y0 + 82, a, 15, INK, 900) + txt(x0 + 105, y0 + 106, b, 13, c, 800)
    s += line(cx - 236, cy, cx + 240, cy, INK, 3, arrow=True) + line(cx, cy + 156, cx, cy - 166, INK, 3, arrow=True)
    s += txt(cx + 236, cy + 24, 'I_{G}', 14, INK, 900, 'end') + txt(cx + 12, cy - 150, 'V_{MT2}', 13, INK, 900, 'start')
    s += txt(cx, 362, 'a + gate pulse fires in Q1 or Q4, set by MT2', 14, INK, 900)
    return 'Four ways to fire a TRIAC', s
D['ee-pe-u5-L1'] = (u5L1, '+ pulse: Q1 or Q4', '5.2.1')


def u5L2():
    # hook: is chopper rms output just D*Vs?  230 V, 10 kHz, D = 0.6, 50 ohm
    Vs, f, Dd, Rr = 230, 10e3, .6, 50
    T = 1e6 / f; ton = Dd * T
    Vo = Vs * math.sqrt(Dd); V1 = Dd * Vs; P = Vo ** 2 / Rr
    Vm = math.sqrt(2) * Vs
    s = defs()
    p = Plot(0, 300, 0, 380, L=54, T=40, Wd=430, H=120)
    s += p.axes(xt=(0, 100, 200, 300), yt=(0, 325), xl='t in µs, at the supply peak', fmt=lambda v: f'{v:g}')
    def v(t):
        return Vm if (t % T) < ton else 0
    s += f'<polygon points="{ptstr([p.P(0, 0)] + stepline(p, v, 0, 300, 3000) + [p.P(300, 0)])}" fill="{GS}" stroke="{G}" stroke-width="3.5" stroke-linejoin="round"/>'
    s += line(p.X(0), p.T - 10, p.X(ton), p.T - 10, G, 2.5, arrow=True) + line(p.X(ton), p.T - 10, p.X(0), p.T - 10, G, 2.5, arrow=True)
    s += txt(p.X(ton / 2), p.T - 18, f'on {ton:.0f} µs', 12, G, 900)
    s += txt(p.X(ton + (T - ton) / 2), p.T + p.H - 10, f'{T - ton:.0f} µs', 11, MUT, 900)
    # bars
    bars = [('supply', Vs, MUT, W), ('D·V_{s} (50 Hz part)', V1, O, OS), ('V_{s}·√D (rms)', Vo, G, GS)]
    for i, (n, val, c, fill) in enumerate(bars):
        y = 226 + i * 46; w = val / Vs * 300
        s += rect(150, y, w, 32, fill, c, 2.5, 8) + rt(142, y + 22, n, 13, c if c != MUT else INK, 900, 'end')
        s += rt(150 + w + 8, y + 22, f'{val:.1f} V', 15, c if c != MUT else INK, 900, 'start')
    return 'The rms comes from √D', s
D['ee-pe-u5-L2'] = (u5L2, '178.2 V, not 138 V', '5.4.1')


def u5L3():
    # hook: can two matrix switches feed one output?  output A from a, b, c over 100 us
    va, vb, vc, Vt, T = 338.9, -169.4, -169.4, 100, 100
    dA = (Vt - vb) / (va - vb); dB = dC = (1 - dA) / 2
    s = defs()
    x0, dx, y0, dy = 160, 100, 46, 62
    ins = [('a', va), ('b', vb), ('c', vc)]
    for r, (n, v) in enumerate(ins):
        y = y0 + r * dy
        s += line(70, y, x0 + 2 * dx + 40, y, INK, 3) + txt(60, y + 5, n, 17, INK, 900, 'end') + txt(76, y - 8, f'{v:+.1f} V'.replace('-', '−'), 12, MUT, 800, 'start')
    for c_, n in enumerate('ABC'):
        x = x0 + c_ * dx
        s += line(x, y0 - 22, x, y0 + 2 * dy + 26, INK if c_ else B, 3)
        s += txt(x, y0 + 2 * dy + 46, n, 17, B if c_ == 0 else INK, 900)
    for r in range(3):
        for c_ in range(3):
            x, y = x0 + c_ * dx, y0 + r * dy
            col = B if c_ == 0 else MUT
            s += f'<circle cx="{x}" cy="{y}" r="13" fill="{BS if c_ == 0 else W}" stroke="{col}" stroke-width="2.5"/>'
    s += tag(x0 + 2 * dx + 42, y0 + 2 * dy + 46, '9 switches', MUT, 12, 'start')
    # timeline for output A
    tl = Plot(0, T, 0, 1, L=40, T=248, Wd=440, H=34)
    segs = [(0, dA, 'a', B), (dA, dA + dB, 'b', G), (dA + dB, 1, 'c', O)]
    for a, b, n, c in segs:
        s += rect(tl.X(a * T) + 1, tl.T, tl.X(b * T) - tl.X(a * T) - 2, tl.H, c, 'none', 0, 6)
        s += txt((tl.X(a * T) + tl.X(b * T)) / 2, tl.T + 23, f'{n}: {(b - a) * T:.1f} µs', 13, W, 900)
    s += txt(tl.L, tl.T - 8, f'output A over {T} µs: one switch at a time, average {Vt} V', 12, MUT, 800, 'start')
    s += txt(250, 330, 'S_{Aa} with S_{Ab} on together', 14, O, 900) + txt(250, 354, 'shorts input a to input b', 14, O, 900)
    return 'One switch per output', s
D['ee-pe-u5-L3'] = (u5L3, 'two at once = a short', '5.6.1')


# =====================================================================
# Unit 6
# =====================================================================
def u6L1():
    # hook: how long does a UPS battery really last?  640 W at 0.8 pf, 90 %, 48 V 100 Ah, 80 % usable
    P, pf, eta, Vb, Ah, use = 640, .8, .9, 48, 100, .8
    Pdc = P / eta; Ib = Pdc / Vb; Et = Vb * Ah * use; t = Et / Pdc; naive = Vb * Ah / P
    s = defs()
    s += acsrc(36, 70) + txt(36, 108, 'mains', 12, MUT, 800)
    s += line(56, 70, 82, 70, MUT, 3, arrow=True)
    s += rbox(86, 44, 108, 52, 'rectifier', B, 15, fill=BS)
    s += line(194, 70, 226, 70, MUT, 3, arrow=True)
    s += rbox(230, 44, 108, 52, 'inverter', G, 15, fill=GS)
    s += line(338, 70, 370, 70, G, 3, arrow=True)
    s += rbox(374, 44, 118, 52, 'load', INK, 15, sub=f'{P} W')
    s += node(212, 70) + wire([(212, 70), (212, 132)], O)
    s += rbox(142, 134, 140, 54, f'{Vb} V, {Ah} Ah', O, 16, fill=OS)
    s += txt(212, 30, f'DC: {Pdc:.0f} W', 13, INK, 900) + tag(292, 168, f'{Ib:.1f} A', O, 13, 'start')
    s += rbox(14, 214, 478, 50, f'{Vb} × {Ah} × {use} = {Et:.0f} Wh  ÷  {Pdc:.0f} W', G, 17, fill=W, sw=2)
    s += rbox(14, 280, 230, 76, f'{t:.1f} h', G, 24, fill=GS, sub='80 % used, 90 % efficient', ss=14)
    s += rbox(262, 280, 230, 76, f'✗ {naive:.1f} h', O, 24, fill=OS, sub=f'{Vb * Ah} Wh ÷ {P} W, too hopeful', ss=14)
    return 'Backup on a 48 V battery', s
D['ee-pe-u6-L1'] = (u6L1, '5.4 h, not 7.5 h', '6.1.1')


def u6L2():
    # hook: what current flows in a +-500 kV link?  2000 MW bipolar
    Vp, P = 500e3, 2000e6
    Id = P / (2 * Vp); naive = P / Vp
    s = defs()
    for row, (y, sign, c, fill) in enumerate(((70, '+', O, OS), (230, '−', B, BS))):
        s += rbox(20, y - 30, 104, 60, 'rectifier', c, 14, fill=fill)
        s += rbox(376, y - 30, 104, 60, 'inverter', c, 14, fill=fill)
        s += line(124, y, 372, y, c, 5, arrow=True) if row == 0 else line(376, y, 128, y, c, 5, arrow=True)
        s += tag(250, y - 12, f'{sign}500 kV pole: {Id:.0f} A', c, 14)
    s += line(72, 100, 72, 200, MUT, 3, '6 6') + line(428, 100, 428, 200, MUT, 3, '6 6')
    s += txt(250, 160, f'earth: {Id:.0f} − {Id:.0f} = 0 A', 14, MUT, 900)
    s += txt(72, 290, 'offshore', 13, MUT, 800) + txt(428, 290, 'shore', 13, MUT, 800)
    s += rtag(250, 336, f'{P / 1e6:.0f} MW ÷ {2 * Vp / 1e3:.0f} kV = {Id:.0f} A', INK, 15)
    s += txt(250, 368, f'not ÷ 500 kV = {naive:.0f} A: the poles are 1000 kV apart', 13, O, 800)
    return 'Two poles, 1000 kV apart', s
D['ee-pe-u6-L2'] = (u6L2, '2000 A, not 4000 A', '6.4.1')


def u6L3():
    # hook: how big must a home battery be?  4 kWh a day, inverter 0.9, 48 V, 2 days, 60 % DoD, 90 % round trip
    Eh, sun, kl, eta, Wp, Vb = 4000, 4.5, .75, .9, 335, 48
    Edc = Eh / eta
    arr = Edc / (sun * kl); n = math.ceil(arr / Wp)
    Est = Edc * 2 / (.6 * .9); Ah = Est / Vb; buy = 50 * math.ceil(Ah / 50)
    s = defs()
    for k in range(n):
        x = 20 + k * 40
        s += rect(x, 20, 34, 46, BS, B, 2.5, 5)
        for r_ in range(1, 4): s += line(x + 2, 20 + r_ * 11.5, x + 32, 20 + r_ * 11.5, B, 1.2)
        s += line(x + 17, 22, x + 17, 64, B, 1.2)
    s += txt(20, 88, f'{n} × {Wp} Wp', 13, B, 900, 'start')
    s += line(182, 43, 212, 43, MUT, 3, arrow=True) + rbox(216, 20, 92, 46, 'MPPT', B, 14)
    s += line(262, 66, 262, 100, MUT, 3, arrow=True) + rect(60, 104, 380, 10, INK, 'none', 0, 5) + txt(446, 113, 'DC bus', 12, INK, 900, 'start')
    s += line(372, 114, 372, 138, G, 3, arrow=True) + rbox(320, 140, 108, 44, 'inverter', G, 14, fill=GS)
    s += line(428, 162, 446, 162, G, 3, arrow=True) + rbox(448, 140, 52, 44, 'home', INK, 11)
    s += line(130, 114, 130, 140, O, 3) + rbox(58, 140, 150, 44, f'{Vb} V battery', O, 14, fill=OS)
    s += rbox(14, 206, 478, 46, f'{Edc:.0f} Wh × 2 days ÷ (0.6 × 0.9) = {Est / 1000:.1f} kWh', O, 16, fill=W, sw=2)
    s += line(250, 252, 250, 270, MUT, 3, arrow=True)
    s += rbox(14, 274, 300, 62, f'÷ {Vb} V = {Ah:.0f} Ah', O, 22, fill=OS)
    s += rbox(330, 274, 162, 62, f'buy {buy} Ah', G, 20, fill=GS)
    s += txt(250, 364, f'{Eh / 1000:.0f} kWh a day at the home, {Edc:.0f} Wh at the bus', 12, MUT, 800)
    return 'Two days of storage', s
D['ee-pe-u6-L3'] = (u6L3, '343 Ah → 350 Ah', '6.6.1')
