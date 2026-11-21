"""Claude's hand-drawn figures for ce-rcc-u4 (Design of slabs and staircases), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}

def sb(base, s, size=11):
    """base letter with a subscript, for SVG text"""
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'

def dim_h(x1, x2, y, label, size=14, c=MUT):
    """horizontal dimension line with end ticks and a centred label above"""
    return (L(x1, y, x2, y, c, 1.5) + L(x1, y - 6, x1, y + 6, c, 1.5) + L(x2, y - 6, x2, y + 6, c, 1.5)
            + Tb((x1 + x2) / 2, y - 6, label, size, fill=INK))

def dim_v(x, y1, y2, label, size=14, c=MUT, anchor='start'):
    o = L(x, y1, x, y2, c, 1.5) + L(x - 6, y1, x + 6, y1, c, 1.5) + L(x - 6, y2, x + 6, y2, c, 1.5)
    dx = 10 if anchor == 'start' else -10
    return o + T(x + dx, (y1 + y2) / 2 + 5, label, size, anchor)

def udl(x1, x2, ytop, ybot, n, c=NX):
    o = [L(x1, ytop, x2, ytop, c, 2)]
    for i in range(n + 1):
        x = x1 + (x2 - x1) * i / n
        o.append(L(x, ytop, x, ybot - 4, c, 1.8, arrow='x'))
    return ''.join(o)

def hatch_support(x, y, w=26, h=34):
    """a wall (support) drawn as a hatched block under the slab"""
    o = [R(x - w / 2, y, w, h, 'var(--line)', L2, 0, 1.5)]
    return ''.join(o)

# ---- 4.1 one-way slab: plan, strip section and moment ----
def f1():
    o = []
    # plan 7.5 m x 3.0 m (40 px per m)
    x0, y0, sx = 40, 46, 40
    o.append(T(x0, 28, 'Plan of the room (clear 7.5 m × 3.0 m)', 15, 'start', bold=True))
    o.append(R(x0 - 9, y0 - 9, 7.5 * sx + 18, 3.0 * sx + 18, 'var(--line)', L2, 2, 1.5))
    o.append(R(x0, y0, 7.5 * sx, 3.0 * sx, PANEL, L2, 0, 1.5))
    sxm = x0 + 3.25 * sx
    o.append(R(sxm, y0, sx, 3.0 * sx, ACS, AC, 0, 2))
    o.append(T(sxm + sx / 2, y0 + 1.5 * sx - 8, '1 m', 14, bold=True))
    o.append(T(sxm + sx / 2, y0 + 1.5 * sx + 10, 'strip', 14, bold=True))
    o.append(L(x0 + 1.3 * sx, y0 + 6, x0 + 1.3 * sx, y0 + 3 * sx - 8, AC, 2.5, arrow='n'))
    o.append(L(x0 + 1.3 * sx, y0 + 3 * sx - 6, x0 + 1.3 * sx, y0 + 8, AC, 2.5, arrow='n'))
    o.append(T(x0 + 1.3 * sx + 10, y0 + 1.5 * sx + 5, 'spans', 13, 'start', AC))
    o.append(T(x0 + 3.75 * sx, y0 + 3 * sx + 32, sb('l', 'y') + ' = 7.5 m', 14))
    o.append(T(x0 + 7.5 * sx + 18, y0 + 1.5 * sx + 5, sb('l', 'x') + ' = 3.0 m', 14, 'start'))
    # numbers box
    o.append(boxt(450, 30, 250, 150, [sb('l', 'y') + ' / ' + sb('l', 'x') + ' = 7.5 / 3.0 = 2.5 &gt; 2', 'so one-way, short span', 'w = 1.5 × 7.50 = 11.25 kN/m', 'M = 13.65 kN·m per m', 'V = 17.52 kN per m'], ACS, AC, 14))
    # elevation of the strip
    ys, th = 290, 34
    xa, xb = 70, 580
    o.append(T(40, 226, 'Section along the strip', 15, 'start', bold=True))
    o.append(udl(xa, xb, ys - 34, ys, 12))
    o.append(Tb((xa + xb) / 2, ys - 40, 'w = 11.25 kN/m', 14, fill=NX, bold=True))
    o.append(R(xa - 22, ys, xb - xa + 44, th, PANEL, AC, 0, 2))
    o.append(hatch_support(xa - 9, ys + th))
    o.append(hatch_support(xb + 9, ys + th))
    # main bar line near the bottom, distribution dots above it
    o.append(L(xa - 16, ys + th - 7, xb + 16, ys + th - 7, AC, 3))
    for i in range(16):
        x = xa + 10 + i * (xb - xa - 20) / 15
        o.append(f'<circle cx="{x:.1f}" cy="{ys + th - 13:.1f}" r="2.6" style="fill:{INK}"/>')
    o.append(dim_v(xb + 40, ys, ys + th, 'D = 140 mm', 14))
    o.append(dim_h(xa, xb, ys + th + 56, 'effective span l = 3.0 + 0.115 = 3.115 m'))
    o.append(T(xa, ys + th + 92, 'bottom: 10 mm @ 220 main bars (line), d = 115 mm', 14, 'start'))
    o.append(T(xa, ys + th + 112, 'above them: 8 mm @ 290 distribution bars (dots)', 14, 'start'))
    # bending moment curve
    yb = ys + th + 128
    pts = [(xa + (xb - xa) * t / 40, yb + 60 * 4 * (t / 40) * (1 - t / 40)) for t in range(41)]
    o.append(L(xa, yb, xb, yb, L2, 1.5))
    o.append(P(pts, LV, 2.5, fill=LVS))
    o.append(Tb((xa + xb) / 2, yb + 60 + 22, 'M = w l² / 8 = 11.25 × 3.115² / 8 = 13.65 kN·m per m', 14, fill=INK, bold=True))
    return yb + 100, ''.join(o)
FIG[1] = (f1, 'The 3.0 m × 7.5 m room spans one way, across 3.0 m. A 1 m strip carries 11.25 kN/m over 3.115 m, so the moment at mid-span is 13.65 kN·m per metre; the main bars sit at the bottom with the distribution bars on top of them.',
          'Plan of a 7.5 by 3.0 metre room with a 1 metre strip across the short span, and a section of the strip with its load, supports, bars and the parabolic bending moment of 13.65 kilonewton metres per metre.')

# ---- 4.2 two-way slab: plan with edge conditions, strips, moments and corner steel ----
def f2():
    o = []
    sc = 80; x0, y0 = 120, 70
    W, H = 4.488 * sc, 3.496 * sc
    x1, y1 = x0 + W, y0 + H
    o.append(T(20, 28, 'Plan of the panel: two adjacent edges discontinuous', 15, 'start', bold=True))
    # next panels beyond continuous edges (bottom and right)
    o.append(R(x0, y1, W, 40, 'var(--line)', L2, 0, 1, '5 4'))
    o.append(R(x1, y0, 40, H, 'var(--line)', L2, 0, 1, '5 4'))
    o.append(R(x0, y0, W, H, PANEL, L2, 0, 1.5))
    # discontinuous edges: thick wall lines top and left; continuous: beam bands bottom and right
    o.append(L(x0, y0, x1, y0, INK, 5)); o.append(L(x0, y0, x0, y1, INK, 5))
    o.append(L(x0, y1, x1, y1, AC, 5)); o.append(L(x1, y0, x1, y1, AC, 5))
    o.append(T((x0 + x1) / 2, y0 - 10, 'discontinuous edge (wall)', 13, fill=MUT))
    o.append(T(x0 - 12, y0 + H / 2 - 8, 'discon-', 13, 'end', MUT)); o.append(T(x0 - 12, y0 + H / 2 + 8, 'tinuous', 13, 'end', MUT))
    o.append(T((x0 + x1) / 2, y1 + 26, 'continuous edge: next panel', 13, fill=AC))
    # middle strip lines (1/8 from each edge)
    for f in (0.125, 0.875):
        o.append(L(x0 + W * f, y0, x0 + W * f, y1, L2, 1.2, '4 4'))
        o.append(L(x0, y0 + H * f, x1, y0 + H * f, L2, 1.2, '4 4'))
    # torsion corners (0.70 m = 56 px)
    c = 0.70 * sc
    o.append(R(x0, y0, c, c, NXS, NX, 0, 2))
    o.append(R(x1 - c, y0, c, c, LVS, LV, 0, 2))
    o.append(R(x0, y1 - c, c, c, LVS, LV, 0, 2))
    o.append(T(x0 + c / 2, y0 + c / 2 + 5, 'full', 13, bold=True))
    o.append(T(x1 - c / 2, y0 + c / 2 + 5, 'half', 13, bold=True))
    o.append(T(x0 + c / 2, y1 - c / 2 + 5, 'half', 13, bold=True))
    # short-span mid moment arrow (vertical) and long-span (horizontal)
    xm, ym = x0 + W * 0.52, y0 + H * 0.5
    o.append(L(xm, y0 + 70, xm, y1 - 64, AC, 2.5, arrow='n'))
    o.append(Tb(xm, ym - 18, sb('M', 'x') + '(+) = 6.20', 14, bold=True))
    o.append(Tb(xm, ym + 4, '8 @ 260 bottom', 14))
    o.append(L(x0 + 80, ym + 48, x1 - 74, ym + 48, LV, 2.5, arrow='l'))
    o.append(Tb(x0 + W * 0.30, ym + 72, sb('M', 'y') + '(+) = 4.49, 8 @ 260', 14))
    o.append(Tb(x0 + W * 0.62, y1 - 16, sb('M', 'x') + '(−) = 8.24: 8 @ 190 top', 14, bold=True, fill=AC))
    # right edge label
    o.append(T(x1 + 52, y0 + H / 2 - 30, sb('M', 'y') + '(−) = 6.03', 14, 'start', AC, bold=True))
    o.append(T(x1 + 52, y0 + H / 2 - 10, '8 @ 250 top', 14, 'start', AC))
    o.append(T(x1 + 52, y0 + H / 2 + 10, 'at the', 14, 'start', AC))
    o.append(T(x1 + 52, y0 + H / 2 + 30, 'continuous edge', 14, 'start', AC))
    # dimensions
    o.append(dim_h(x0, x1, y1 + 66, sb('l', 'y') + ' = 4.488 m'))
    o.append(dim_v(x0 - 92, y0, y1, '', 13))
    o.append(T(x0 - 84, y1 + 22, sb('l', 'x') + ' = 3.496 m', 14, 'start'))
    # key
    ky = y1 + 100
    o.append(R(20, ky, 22, 16, NXS, NX, 0, 2)); o.append(T(50, ky + 13, 'torsion mesh 8 @ 300, 4 layers, 0.70 m square', 13, 'start'))
    o.append(R(20, ky + 26, 22, 16, LVS, LV, 0, 2)); o.append(T(50, ky + 39, 'half mesh (one edge continuous); dashed lines: edge strips of 1/8 width', 13, 'start'))
    o.append(T(20, ky + 66, 'w = 10.5 kN/m², all moments in kN·m per metre, from α × 10.5 × 3.496²', 13, 'start', MUT))
    return ky + 80, ''.join(o)
FIG[2] = (f2, 'The 3.496 m × 4.488 m panel of the worked example. The two continuous edges carry the hogging moments and top steel; the corner where both edges are discontinuous gets the full torsion mesh over 0.70 m, the two mixed corners half of it, and the corner between two continuous edges none.',
          'Plan of a two-way slab panel with walls on the top and left edges and continuous slab beyond the bottom and right edges, showing the mid-span and support moments with their bars, the edge strips and the torsion mesh at three corners.')

# ---- 4.3 cantilever (top steel, anchorage) and continuous slab moments ----
def f3():
    o = [T(20, 26, 'Balcony slab: 1.2 m clear projection, D = 140 mm', 15, 'start', bold=True)]
    sc = 250; yt, th = 96, 30
    xf = 300  # face of beam
    o.append(R(60, yt, xf - 60, th, PANEL, L2, 0, 1.5))           # floor slab behind
    o.append(R(xf - 60, yt, 60, th + 70, 'var(--line)', L2, 0, 1.5))  # beam
    o.append(T(xf - 30, yt + th + 60, 'beam', 13, fill=MUT))
    xt = xf + 1.2 * sc
    o.append(R(xf, yt, xt - xf, th, PANEL, AC, 0, 2))
    o.append(udl(xf, xt, yt - 34, yt, 8))
    o.append(Tb((xf + xt) / 2, yt - 40, 'w = 12.0 kN/m (factored)', 14, fill=NX, bold=True))
    o.append(L(xt - 4, yt - 64, xt - 4, yt - 4, NX, 3, arrow='x'))
    o.append(T(xt + 6, yt - 50, 'railing 1.5 kN/m', 13, 'start', NX))
    # top bar with anchorage
    xa = xf - 0.47 * sc
    o.append(L(xa, yt + 7, xt - 8, yt + 7, AC, 3.5))
    o.append(T(xt + 6, yt + 20, '10 @ 300 top', 14, 'start', AC, bold=True))
    o.append(L(xa, yt - 8, xa, yt + 16, INK, 1.5)); o.append(L(xf, yt - 8, xf, yt + 16, INK, 1.5))
    o.append(dim_h(xa, xf, yt + th + 22, 'L = 470 mm'.replace('L =', 'anchor')))
    # hogging moment of the cantilever, drawn above its base line like the continuous slab below
    yb = yt + th + 120
    pts = [(xf + (xt - xf) * t / 30, yb - 62 * ((1 - t / 30) ** 2 * 7.56 + (1 - t / 30) * 1.8) / 9.9) for t in range(31)]
    o.append(L(xf, yb, xt, yb, L2, 1.5))
    o.append(P([(xf, yb)] + pts, LV, 2.5, fill=LVS))
    o.append(T(xf - 72, yb - 50, 'M at the face', 14, 'end', bold=True))
    o.append(T(xf - 72, yb - 32, '= 12.0 × 1.2²/2 + 1.5 × 1.2', 14, 'end'))
    o.append(T(xf - 72, yb - 14, '= 9.90 kN·m per m', 14, 'end', bold=True))
    # continuous slab
    y0 = 330
    o.append(T(20, y0 - 34, 'Continuous slab, four spans of 3.375 m: Table 12 moments (kN·m per m)', 15, 'start', bold=True))
    xs = [60 + i * 150 for i in range(5)]
    o.append(R(xs[0], y0, xs[-1] - xs[0], 14, PANEL, AC, 0, 2))
    for x in xs:
        o.append(f'<polygon points="{x},{y0 + 15} {x - 10},{y0 + 32} {x + 10},{y0 + 32}" style="fill:var(--line);stroke:var(--line2);stroke-width:1.5"/>')
    sup = [0, -12.96, -11.75, -12.96, 0]; mid = [11.18, 8.81, 8.81, 11.18]
    ya = y0 + 92; k = 3.2
    o.append(L(xs[0], ya, xs[-1], ya, L2, 1.5))
    for i in range(4):
        Ml, Mr = sup[i], sup[i + 1]; amp = mid[i] - (Ml + Mr) / 2
        pts = [(xs[i] + 150 * t / 30, ya + k * ((Ml * (1 - t / 30) + Mr * t / 30) + 4 * amp * (t / 30) * (1 - t / 30))) for t in range(31)]
        o.append(P(pts, LV, 2.5))
        o.append(T(xs[i] + 75, ya + k * mid[i] + 22, f'+{mid[i]:.2f}', 14, bold=True))
    for i in (1, 2, 3):
        o.append(Tb(xs[i], ya + k * sup[i] - 10, f'&#8722;{-sup[i]:.2f}', 14, fill=AC, bold=True))
    o.append(T(20, ya + 92, 'Hogging (top steel) is drawn above the line, sagging (bottom steel) below. The first interior', 13, 'start', MUT))
    o.append(T(20, ya + 110, 'support carries the largest moment, so it gets the closest top bars: 10 mm @ 210.', 13, 'start', MUT))
    return ya + 124, ''.join(o)
FIG[3] = (f3, 'Top: the balcony carries 12.0 kN/m and a 1.5 kN/m railing load at its tip, so the face of the beam takes a hogging moment of 9.90 kN·m per metre; the top bars run 470 mm (47φ) past the face. Bottom: the Table 12 moments of the four-span slab, largest at the first interior supports.',
          'A cantilever slab with its load, top bars anchored behind the beam face and a hogging moment diagram, above a four-span continuous slab with sagging moments 11.18 and 8.81 and support moments of minus 12.96 and minus 11.75 kilonewton metres per metre.')

# ---- 4.4 dog-legged stair: plan inset and section of one flight ----
def f4():
    o = []
    # plan inset, 34 px per m: hall 5.2 m long x 2.5 m wide
    px, py, k = 30, 44, 34
    o.append(T(px, py - 14, 'Plan: dog-legged stair', 14, 'start', bold=True))
    o.append(R(px, py, 5.2 * k, 2.5 * k, PANEL, L2, 0, 1.5))
    fx0, fx1 = px + 1.25 * k, px + 3.95 * k
    for row, yy in enumerate((py + 0.05 * k, py + 1.3 * k)):
        o.append(R(fx0, yy, 2.7 * k, 1.15 * k, ACS, AC, 0, 1.2))
        for i in range(1, 9):
            o.append(L(fx0 + i * 0.3 * k, yy, fx0 + i * 0.3 * k, yy + 1.15 * k, AC, 1))
    o.append(L(fx0 + 6, py + 1.9 * k, fx1 - 6, py + 1.9 * k, NX, 2, arrow='x'))
    o.append(L(fx1 - 6, py + 0.6 * k, fx0 + 6, py + 0.6 * k, NX, 2, arrow='x'))
    o.append(T(px + 5.2 * k + 8, py + 1.25 * k - 3, 'half', 13, 'start')); o.append(T(px + 5.2 * k + 8, py + 1.25 * k + 13, 'landing', 13, 'start'))
    o.append(T(px + 0.62 * k, py + 2.5 * k + 18, 'floor landing', 13, 'start'))
    # section of flight 1, 100 px per m
    sc = 100; x0 = 60; yf = 380
    rise = 1.6 * sc; tr = 0.3 * sc; rr = 0.16 * sc
    xa = x0 + 1.25 * sc; xb = xa + 2.7 * sc; xe = xb + 1.25 * sc
    yh = yf - rise
    tw = 0.18 * sc
    o.append(R(x0, yf - tw, 1.25 * sc, tw, PANEL, L2, 0, 1.5))
    o.append(R(xb, yh - tw, 1.25 * sc, tw, PANEL, L2, 0, 1.5))
    pts = [(xa, yf - tw)]
    x, y = xa, yf - tw
    for i in range(9):
        y -= rr; pts.append((x, y)); x += tr; pts.append((x, y))
    y -= rr; pts.append((x, y))
    o.append(P(pts, INK, 2))
    dy = tw * 1.1333
    ys0 = yf - tw + tw * 1.1333; ys1 = yf - tw - 9 * rr + tw * 1.1333
    o.append(L(xa, ys0, xb, ys1, AC, 2.5))  # soffit, parallel to the line of the step corners
    o.append(L(xa + 8, ys0 - 5 - 8 * rr / tr, xb - 4, ys1 - 5 + 4 * rr / tr, AC, 3.5))  # main bars
    o.append(Tb((xa + xb) / 2 + 70, (yf + yh) / 2 + 40, '12 mm @ 170 along the slope', 14, fill=AC, bold=True))
    # riser / tread labels
    o.append(Tb(xa + 4 * tr + tr / 2, yf - tw - 5 * rr - 14, 'T = 300', 13))
    o.append(Tb(xa + 6 * tr + 14, yf - tw - 6 * rr + 6, 'R = 160', 13, 'start'))
    o.append(Tb(xa + 3.2 * tr - 70, yf - 58, 'waist 180', 13, fill=INK))
    # landing notes
    o.append(T(x0 + 0.62 * sc, yf + 20, 'landing 1.25 m', 13)); o.append(T(xb + 0.62 * sc, yh + 20, 'half landing 1.25 m', 13))
    o.append(T(xb + 0.62 * sc, yh - 48, '(spans into the page', 13)); o.append(T(xb + 0.62 * sc, yh - 32, 'onto the side walls)', 13))
    o.append(dim_v(xe + 22, yh, yf, '1.6 m rise', 13))
    # effective span dimension from the middle of each landing
    o.append(dim_h(x0 + 0.625 * sc, xb + 0.625 * sc, yf + 56, 'span l = 0.625 + 2.70 + 0.625 = 3.95 m'))
    o.append(dim_h(xa, xb, yf + 100, 'going 9 × 300 = 2.70 m'))
    o.append(T(380, 40, 'w = 11.10 kN/m² of plan', 14, 'start', bold=True))
    o.append(T(380, 60, '(waist 5.10 + steps 2.00 + 1 + 3)', 14, 'start'))
    o.append(T(380, 84, 'M = 1.5 × 11.10 × 3.95² / 8', 14, 'start'))
    o.append(T(380, 104, '   = 32.47 kN·m per m', 14, 'start', bold=True))
    return yf + 120, ''.join(o)
FIG[4] = (f4, 'Left: the dog-legged plan, two flights side by side with a half landing. Below: one flight of ten 160 mm risers and nine 300 mm treads; it spans 3.95 m, from the middle of one 1.25 m landing to the middle of the other, so the 180 mm waist takes 32.47 kN·m per metre.',
          'A small plan of a dog-legged stair with two flights and landings, and a section of one flight showing steps, waist slab, bars along the slope, landings and the effective span of 3.95 metres.')

# ---- 4.5 flat slab: strips, drops and punching perimeters of one interior panel ----
def f5():
    o = [T(20, 26, 'Interior panel 6.0 m × 6.0 m between column centre lines,', 15, 'start', bold=True),
         T(20, 46, 'designing the left-right span', 15, 'start', bold=True)]
    k = 46; x0, y0 = 70, 120; S = 6 * k
    o.append(R(x0, y0, S, 1.5 * k, ACS, 'none', 0, 0))
    o.append(R(x0, y0 + 4.5 * k, S, 1.5 * k, ACS, 'none', 0, 0))
    o.append(R(x0, y0, S, S, 'none', L2, 0, 1.5))
    o.append(T(x0 + S / 2, y0 + 0.75 * k + 5, 'half column strip 1.5 m', 13))
    o.append(T(x0 + S / 2, y0 + 5.25 * k + 5, 'half column strip 1.5 m', 13))
    o.append(T(x0 + S / 2, y0 + 3 * k - 6, 'middle strip 3.0 m', 14, bold=True))
    o.append(L(x0 + 60, y0 + 3 * k + 12, x0 + S - 60, y0 + 3 * k + 12, LV, 2, arrow='l'))
    for cx, cy in ((x0, y0), (x0 + S, y0), (x0, y0 + S), (x0 + S, y0 + S)):
        o.append(R(cx - 1.0 * k, cy - 1.0 * k, 2 * k, 2 * k, 'none', NX, 0, 1.5, '6 4'))
        o.append(R(cx - 0.3325 * k, cy - 0.3325 * k, 0.665 * k, 0.665 * k, 'none', AC, 0, 1.5, '3 3'))
        o.append(R(cx - 0.225 * k, cy - 0.225 * k, 0.45 * k, 0.45 * k, INK, INK, 0, 1))
    bx = 450
    o.append(R(bx, 84, 18, 18, 'none', NX, 0, 1.5, '6 4')); o.append(T(bx + 28, 98, 'drop 2.0 m × 2.0 m, 250 mm deep', 13, 'start'))
    o.append(R(bx, 112, 18, 18, 'none', AC, 0, 1.5, '3 3')); o.append(T(bx + 28, 126, 'punching perimeter at d/2 (665 mm)', 13, 'start'))
    o.append(R(bx + 4, 144, 10, 10, INK, INK, 0, 1)); o.append(T(bx + 28, 154, '450 mm column', 13, 'start'))
    o.append(boxt(bx, 176, 250, 100, ['lₙ = 6.0 − 0.45 = 5.55 m', 'w = 15.21 kN/m²', 'M₀ = 15.21 × 6 × 5.55² / 8', '= 351.3 kN·m'], ACS, AC, 14))
    rows = [('kN·m', 'negative', 'positive'), ('share of M₀', '228.4', '123.0'), ('column strip, per m', '57.1', '24.6'), ('middle strip, per m', '19.0', '16.4')]
    for i, r in enumerate(rows):
        yy = 306 + i * 24
        o.append(T(bx, yy, r[0], 13, 'start', MUT if i == 0 else INK, bold=(i == 0)))
        o.append(T(bx + 185, yy, r[1], 13, 'end', INK, bold=(i == 0)))
        o.append(T(bx + 250, yy, r[2], 13, 'end', INK, bold=(i == 0)))
    o.append(T(bx, 412, 'punching τ: 0.95 at the column,', 13, 'start', AC))
    o.append(T(bx, 430, '0.33 outside the drop (N/mm²);', 13, 'start', AC))
    o.append(T(bx, 448, 'limit 0.25√20 = 1.12 N/mm²', 13, 'start', AC))
    return y0 + S + 64, ''.join(o)
FIG[5] = (f5, 'One interior panel of the worked example: the shaded bands are the halves of the column strips along the column lines, the centre band the middle strip. Dashed outlines show the 2.0 m drops and the punching perimeters at d/2 from each column; both punching stresses stay under 1.12 N/mm².',
          'Plan of a square flat slab panel with columns at the corners, drops, punching perimeters, column and middle strips, and a table of the strip moments per metre.')


# ---- 4.6 yield line patterns and the search for the lowest load ----
def f6():
    o = []
    k = 36
    # square 4 m
    x0, y0 = 30, 56
    o.append(T(x0, 30, 'Square 4 m × 4 m', 14, 'start', bold=True))
    o.append(R(x0, y0, 4 * k, 4 * k, PANEL, INK, 0, 3))
    o.append(L(x0, y0, x0 + 4 * k, y0 + 4 * k, NX, 2.5)); o.append(L(x0 + 4 * k, y0, x0, y0 + 4 * k, NX, 2.5))
    o.append(T(x0 + 2 * k, y0 + 4 * k + 24, 'w = 24m/L² = 25.23', 14, bold=True))
    # rectangle 6 x 4 with b = 2.38
    x1 = 220; b = 2.38
    o.append(T(x1, 30, 'Rectangle 6 m × 4 m', 14, 'start', bold=True))
    o.append(R(x1, y0, 6 * k, 4 * k, PANEL, INK, 0, 3))
    ya = y0 + 2 * k
    o.append(L(x1 + b * k, ya, x1 + (6 - b) * k, ya, NX, 2.5))
    for (xx, yy) in ((x1, y0), (x1, y0 + 4 * k)):
        o.append(L(xx, yy, x1 + b * k, ya, NX, 2.5))
    for (xx, yy) in ((x1 + 6 * k, y0), (x1 + 6 * k, y0 + 4 * k)):
        o.append(L(xx, yy, x1 + (6 - b) * k, ya, NX, 2.5))
    o.append(brace(x1, x1 + b * k, y0 + 4 * k + 12))
    o.append(T(x1 + b * k / 2, y0 + 4 * k + 32, 'b = 2.38 m', 13))
    o.append(T(x1 + 3 * k + 40, y0 + 4 * k + 32, 'w = 17.84', 14, bold=True))
    # trial plot
    px0, px1, py0, py1 = 500, 700, 70, 236
    fx = lambda v: px0 + (v - 1.0) / 2.0 * (px1 - px0)
    fy = lambda v: py1 - (v - 17) / 6 * (py1 - py0)
    o.append(axes(px0, px1, py0, py1, [1.0, 2.0, 3.0], [17, 19, 21, 23], fx, fy, 'b (m)', 'w (kN/m²)', lambda v: f'{v:.1f}'))
    pts = [(1.0, 22.08), (1.5, 19.06), (2.0, 18.02), (2.38, 17.84), (3.0, 18.22)]
    o.append(P([(fx(a), fy(v)) for a, v in pts], L2, 1.5, '4 4'))
    for a, v in pts:
        o.append(C(fx(a), fy(v), 5, LV if a == 2.38 else AC))
    o.append(Tb(fx(2.38), fy(17.84) - 14, 'lowest 17.84', 13, fill=LV, bold=True))
    o.append(T(20, 304, 'Yield lines in the span are sagging; the simply supported edges are axes of rotation. m = 16.82 kN·m per m', 13, 'start', MUT))
    o.append(T(20, 322, '(10 mm @ 150 both ways, d = 100 mm). Each trial b gives an upper bound; the lowest is the collapse load.', 13, 'start', MUT))
    return 336, ''.join(o)
FIG[6] = (f6, 'The square slab fails along its diagonals at 25.23 kN/m². For the 6 m × 4 m slab the pattern depends on b; the trials give 22.08 down to 17.84 kN/m² at b = 2.38 m, the lowest, which is the collapse load.',
          'Yield line patterns of a square and a rectangular simply supported slab, and a plot of the collapse load against the pattern dimension b with its minimum at b equals 2.38 metres.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
