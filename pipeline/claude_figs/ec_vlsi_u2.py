"""Claude's hand-drawn figures for ec-vlsi-u2 (VLSI Design: CMOS fabrication and layout), one per chapter, drawn from each
chapter's own worked example and numbers. Colours are the shell's CSS variables. stick() is also used by a model answer."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """C_s, x_j ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωβΔ])_([A-Za-z0-9,]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def zig(x1, y1, x2, y2, c=INK, n=6, amp=7):
    """a resistor between two points (straight leads, zigzag in the middle)"""
    dx, dy = x2 - x1, y2 - y1; Ln = math.hypot(dx, dy); ux, uy = dx / Ln, dy / Ln; px, py = -uy, ux
    a, b = 0.3 * Ln, 0.7 * Ln
    pts = [(x1, y1), (x1 + ux * a, y1 + uy * a)]
    for i in range(1, 2 * n):
        t = a + (b - a) * i / (2 * n); s = amp if i % 2 else -amp
        pts.append((x1 + ux * t + px * s, y1 + uy * t + py * s))
    pts += [(x1 + ux * b, y1 + uy * b), (x2, y2)]
    return P(pts, c, 2)


SUP = str.maketrans('0123456789−', '⁰¹²³⁴⁵⁶⁷⁸⁹⁻')


# ---- 2.1 drive-in profile of the worked example ----
def f1():
    o = []
    x0, x1, y0, y1 = 100, 560, 40, 300
    fx = lin(0, 0.8, x0, x1); fy = lin(15, 19, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8], [15, 16, 17, 18, 19], fx, fy,
                  'depth x (μm)', 'phosphorus concentration (cm⁻³, log scale)', lambda v: f'{v:g}', lambda v: '10' + str(v).translate(SUP)))
    Cs, Lr = 5.43e18, 0.2078
    pts = [(fx(x), fy(math.log10(Cs * math.exp(-(x / Lr) ** 2)))) for x in [i * 0.01 for i in range(0, 81)] if Cs * math.exp(-(x / Lr) ** 2) > 1e15]
    o.append(P(pts, AC, 3))
    o.append(L(x0, fy(16), x1, fy(16), NX, 2, dash='7 5'))
    o.append(T(x1 + 8, fy(16) + 5, 'wafer N_B = 10¹⁶', 13, 'start', fill=NX, bold=True))
    o.append(C(fx(0), fy(math.log10(Cs)), 6, AC))
    o.append(T(x0 + 14, fy(math.log10(Cs)) - 8, 'C_s = 5.43 × 10¹⁸ at the surface', 14, 'start', bold=True))
    cL = Cs / math.e
    o.append(C(fx(Lr), fy(math.log10(cL)), 6, LV))
    o.append(L(fx(Lr), fy(math.log10(cL)), fx(Lr), y1, LV, 1.5, dash='4 4'))
    o.append(Tb(fx(Lr) + 12, fy(math.log10(cL)) + 22, 'x = L = 0.21 μm: C_s/e = 2.0 × 10¹⁸', 13, 'start', fill=LV, bold=True))
    xj = 0.5216
    o.append(C(fx(xj), fy(16), 6, NX))
    o.append(L(fx(xj), fy(16), fx(xj), y1, NX, 1.5, dash='4 4'))
    o.append(Tb(fx(xj) + 10, fy(16.55), 'junction x_j = 0.52 μm', 14, 'start', fill=NX, bold=True))
    o.append(T(fx(0.12), fy(15.4), 'n-type', 14, fill=AC, bold=True))
    o.append(T(fx(0.70), fy(15.4), 'p-type', 14, fill=NX, bold=True))
    o.append(T(330, 362, 'Q = 10¹⁴ cm⁻², D = 3 × 10⁻¹⁴ cm²/s, 1 hour at 1000 °C: x_j = 2.51 L', 14, fill=MUT))
    return 376, ''.join(o)


# ---- 2.2 wet etch against RIE, the second worked example ----
def f2():
    o = []
    s = 46  # px per micrometre across; the 0.5 μm oxide is drawn 60 px tall
    def panel(x0, under, title, top, wet):
        cx = x0 + 165
        ox_t, ox_b = 150, 210
        hw, u = 1.0 * s, under * s
        o.append(T(cx, 30, title, 15, bold=True))
        o.append(R(x0, ox_b, 330, 60, LVS, LV, 0, 1.5))
        o.append(T(x0 + 290, 250, 'silicon', 13, fill=LV))
        if wet:  # isotropic: the sidewall is a rounded bowl reaching 0.6 μm under the resist
            o.append(f'<path d="M{x0},{ox_t} H{cx - hw - u:.1f} Q{cx - hw - u:.1f},{ox_b} {cx - hw:.1f},{ox_b} H{x0} Z" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
            o.append(f'<path d="M{x0 + 330},{ox_t} H{cx + hw + u:.1f} Q{cx + hw + u:.1f},{ox_b} {cx + hw:.1f},{ox_b} H{x0 + 330} Z" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
        else:
            o.append(f'<path d="M{x0},{ox_t} H{cx - hw - u:.1f} L{cx - hw:.1f},{ox_b} H{x0} Z" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
            o.append(f'<path d="M{x0 + 330},{ox_t} H{cx + hw + u:.1f} L{cx + hw:.1f},{ox_b} H{x0 + 330} Z" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
        o.append(T(x0 + 290, 186, 'oxide', 13, fill=AC))
        o.append(R(x0, 124, cx - hw - x0, 26, PANEL, INK, 2, 1.5))
        o.append(R(cx + hw, 124, x0 + 330 - cx - hw, 26, PANEL, INK, 2, 1.5))
        o.append(T(x0 + 44, 116, 'resist', 13, fill=MUT))
        o.append(brace(cx - hw, cx + hw, 100, INK, up=False))
        o.append(T(cx, 92, 'window 2.0 μm', 13))
        for xx in (cx - hw - u, cx + hw + u): o.append(L(xx, ox_t, xx, 288, INK, 1, dash='3 3'))
        o.append(brace(cx - hw - u, cx + hw + u, 290, INK, up=True))
        o.append(T(cx, 312, top, 14, bold=True))
        if wet:
            o.append(brace(cx - hw - u, cx - hw, 222, LV))
            o.append(T(cx - hw - u - 6, 258, 'undercut 0.6 μm', 13, 'end', fill=LV, bold=True))
    panel(20, 0.6, 'Wet etch (isotropic)', 'top of hole 3.2 μm', True)
    panel(370, 0.06, 'RIE, A = 0.9', 'top of hole 2.12 μm', False)
    o.append(T(360, 346, 'both: 0.5 μm oxide, 6.0 min with over-etch, 120 nm of resist lost', 14, fill=MUT))
    return 360, ''.join(o)


# ---- 2.3 the ten masks of the worked example ----
def f3():
    o = []
    fe = [('1 n-well', 'PMOS body'), ('2 active', 'islands, field oxide'), ('3 poly', 'gates'), ('4 n+ S/D', 'NMOS source, drain'), ('5 p+ S/D', 'PMOS source, drain')]
    be = [('6 contact', 'holes to Si, poly'), ('7 metal 1', 'first wiring'), ('8 via', 'metal 1 to 2'), ('9 metal 2', 'second wiring'), ('10 pad', 'bond openings')]
    w, g, x0 = 128, 13, 16
    o.append(T(x0, 30, 'Front end: transistors', 14, 'start', fill=AC, bold=True))
    o.append(T(704, 160, 'Back end: wiring', 14, 'end', fill=LV, bold=True))
    for row, (items, y, st, fill) in enumerate(((fe, 42, AC, ACS), (be, 172, LV, LVS))):
        for i, (a, b) in enumerate(items):
            x = x0 + i * (w + g)
            o.append(boxt(x, y, w, 66, [a, b], fill if (row, i) != (0, 2) else PANEL, st, 13, True))
            if i < 4: o.append(L(x + w + 1, y + 33, x + w + g - 1, y + 33, st, 2, arrow='n' if row == 0 else 'l'))
    o.append(P([(x0 + 4 * (w + g) + w / 2, 108), (x0 + 4 * (w + g) + w / 2, 130), (x0 + w / 2, 130), (x0 + w / 2, 168)], L2, 2))
    xv = x0 + 2 * (w + g) - 6
    o.append(R(xv, 166, 2 * w + g + 12, 78, 'none', NX, 10, 2, dash='6 5'))
    o.append(T(xv + (2 * w + g + 12) / 2, 268, 'drop metal 2 and its via goes too: 10 − 2 = 8 masks', 14, fill=NX, bold=True))
    o.append(T(360, 300, '0.5 cm² die, D = 1 defect/cm²: Y = e⁻⁰·⁵ = 61 %', 14))
    o.append(T(360, 322, '300 mm wafer: 1319 whole dies × 0.607 = about 800 good dies', 14, fill=MUT))
    return 336, ''.join(o)


def mos(o, x, y, sd, sdfill, sdst, label):
    """a MOSFET in a cross-section: two source/drain diffusions and a poly gate on thin oxide; x = left edge"""
    o.append(R(x, y, 44, 22, sdfill, sdst, 3, 1.5)); o.append(T(x + 22, y + 16, sd, 13, bold=True))
    o.append(R(x + 84, y, 44, 22, sdfill, sdst, 3, 1.5)); o.append(T(x + 106, y + 16, sd, 13, bold=True))
    o.append(R(x + 48, y - 22, 32, 18, LVS, LV, 2, 2)); o.append(L(x + 46, y - 2, x + 82, y - 2, INK, 2))
    o.append(T(x + 64, y - 28, 'in', 13, fill=LV, bold=True)); o.append(T(x + 64, y + 40, label, 13, bold=True))


# ---- 2.4 twin-tub inverter: which body each transistor sits in ----
def f4():
    o = []
    o.append(T(360, 24, 'one poly input drives both gates; the two drains are the output', 13, fill=MUT))
    o.append(R(16, 130, 688, 190, PANEL, L2, 0, 1.5))
    o.append(T(360, 306, 'p-substrate, N_A = 10¹⁵ cm⁻³ (an NMOS here would have γ = 0.053 V<tspan baseline-shift="super" font-size="10">½</tspan>)', 13, fill=MUT))
    o.append(f'<path d="M40,130 V236 Q40,250 54,250 H326 Q340,250 340,236 V130 Z" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
    o.append(f'<path d="M380,130 V236 Q380,250 394,250 H666 Q680,250 680,236 V130 Z" style="fill:{NXS};stroke:{NX};stroke-width:2"/>')
    o.append(T(190, 222, 'n-well: PMOS body', 14, fill=AC, bold=True))
    o.append(T(530, 204, 'p-well, N_A = 10¹⁷ cm⁻³', 14, fill=NX, bold=True))
    o.append(T(530, 224, 'NMOS body: γ = 0.53 V<tspan baseline-shift="super" font-size="10">½</tspan>', 13, fill=NX))
    mos(o, 80, 130, 'p+', PANEL, AC, 'PMOS')
    mos(o, 430, 130, 'n+', PANEL, NX, 'NMOS')
    o.append(R(264, 130, 44, 22, PANEL, AC, 3, 1.5)); o.append(T(286, 146, 'n+', 13, bold=True))
    o.append(R(604, 130, 44, 22, PANEL, NX, 3, 1.5)); o.append(T(626, 146, 'p+', 13, bold=True))
    o.append(T(286, 172, 'well tap', 13, fill=MUT)); o.append(T(626, 172, 'well tap', 13, fill=MUT))
    for xs, lab, c in ((102, 'VDD', AC), (286, 'VDD', AC), (452, 'VSS', NX), (626, 'VSS', NX)):
        o.append(L(xs, 130, xs, 112, c, 2.5)); o.append(T(xs, 106, lab, 13, fill=c, bold=True))
    o.append(P([(186, 130), (186, 62), (536, 62), (536, 130)], INK, 2))
    o.append(Tb(360, 67, 'out', 13, bold=True))
    return 330, ''.join(o)


# ---- 2.5 the vertical NPN and its collector path ----
def f5():
    o = []
    o.append(R(16, 250, 688, 70, PANEL, L2, 0, 1.5)); o.append(T(560, 304, 'p-substrate', 14, fill=MUT))
    o.append(R(16, 90, 688, 160, ACS, AC, 0, 1.5))
    o.append(T(430, 214, 'n-epi: lightly doped collector', 14, fill=AC, bold=True))
    o.append(R(16, 90, 46, 170, PANEL, L2, 0, 1.5)); o.append(R(658, 90, 46, 170, PANEL, L2, 0, 1.5))
    o.append(T(39, 285, 'p isolation', 13, 'start', fill=MUT))
    o.append(R(90, 236, 560, 32, NXS, NX, 6, 2)); o.append(T(370, 263, 'n+ buried layer', 14, fill=NX, bold=True))
    o.append(R(560, 90, 46, 150, NXS, NX, 2, 2)); o.append(T(583, 80, 'C', 15, fill=NX, bold=True))
    o.append(T(552, 170, 'n+ sinker', 13, 'end', fill=NX, bold=True))
    o.append(f'<path d="M110,90 V160 Q110,176 126,176 H350 Q366,176 366,160 V90 Z" style="fill:{LVS};stroke:{LV};stroke-width:2"/>')
    o.append(T(300, 166, 'p base', 14, fill=LV, bold=True))
    o.append(R(190, 90, 90, 30, PANEL, NX, 3, 2)); o.append(T(235, 110, 'n+ emitter', 13, bold=True)); o.append(T(235, 80, 'E', 15, bold=True))
    o.append(R(310, 90, 40, 26, PANEL, LV, 3, 2)); o.append(T(330, 108, 'p+', 13, bold=True)); o.append(T(330, 80, 'B', 15, fill=LV, bold=True))
    o.append(L(235, 122, 235, 230, INK, 2.5, arrow='m'))
    o.append(L(250, 246, 556, 246, INK, 2.5, arrow='m'))
    o.append(L(583, 236, 583, 96, INK, 2.5, arrow='m'))
    o.append(Tb(160, 210, 'electrons', 13, 'middle', fill=INK))
    o.append(T(360, 30, 'I_C = 2 mA, β = 100: I_B = 20 μA', 14, bold=True))
    o.append(T(360, 52, 'g_m = I_C/V_T = 2 mA ÷ 26 mV = 76.9 mA/V (nMOS at V_ov = 0.5 V: 8 mA/V)', 14, fill=MUT))
    return 330, ''.join(o)


# ---- 2.6 the rules of the worked example on a drawn transistor and two wires (λ = 0.5 μm) ----
def f6():
    o = []
    u = 12  # px per λ
    ax, ay = 110, 70  # active 12λ long (5λ source, 2λ gate, 5λ drain) and 8λ wide
    o.append(T(ax + 6 * u, 20, 'one transistor', 14, bold=True))
    o.append(R(ax, ay, 12 * u, 8 * u, NXS, NX, 0, 2))
    o.append(R(ax + 5 * u, ay - 2 * u, 2 * u, 12 * u, LVS, LV, 0, 2))
    for c0 in (ax + 1 * u, ax + 9 * u):
        o.append(R(c0 - u, ay + 1 * u, 4 * u, 4 * u, 'none', AC, 0, 2))
        o.append(R(c0, ay + 2 * u, 2 * u, 2 * u, INK, INK, 0, 1))
    o.append(T(ax + 6 * u, 40, 'poly L = 2λ = 1 μm', 13, fill=LV, bold=True))
    o.append(L(ax - 14, ay, ax - 14, ay + 8 * u, INK, 1.5, arrow='x')); o.append(L(ax - 14, ay + 8 * u, ax - 14, ay, INK, 1.5, arrow='x'))
    o.append(T(ax - 20, ay + 4 * u - 6, 'W = 8λ', 13, 'end', bold=True)); o.append(T(ax - 20, ay + 4 * u + 12, '= 4 μm', 13, 'end'))
    o.append(T(ax + 6 * u, ay + 10 * u + 22, 'poly runs 2λ past the active', 13, fill=MUT))
    o.append(T(ax + 6 * u, ay + 10 * u + 42, 'C_g = 2.3 fF/μm² × 4 μm² = 9.2 fF', 13, bold=True))
    o.append(T(ax + 12 * u + 20, ay + 2 * u + 10, '← contact 2λ, metal 1λ round it:', 13, 'start'))
    o.append(T(ax + 12 * u + 36, ay + 2 * u + 28, '4λ × 4λ = 2.0 μm square', 13, 'start', fill=AC, bold=True))
    mx, w = 300, 360
    y1 = 176; y2 = y1 + 3 * u; y3 = y2 + 3 * u; y4 = y3 + 3 * u
    o.append(T(mx + w / 2, 160, 'two metal 1 wires', 14, bold=True))
    o.append(R(mx, y1, w, 3 * u, ACS, AC, 0, 2)); o.append(R(mx, y3, w, 3 * u, ACS, AC, 0, 2))
    o.append(L(mx + w + 16, y1, mx + w + 16, y2, INK, 1.5, arrow='x')); o.append(L(mx + w + 16, y2, mx + w + 16, y1, INK, 1.5, arrow='x'))
    o.append(T(mx + 120, (y1 + y2) / 2 + 5, 'width 3λ = 1.5 μm', 13, bold=True))
    o.append(L(mx + 236, y2, mx + 236, y3, NX, 1.5, arrow='l')); o.append(L(mx + 236, y3, mx + 236, y2, NX, 1.5, arrow='l'))
    o.append(T(mx + 248, (y2 + y3) / 2 + 5, 'space 3λ = 1.5 μm', 13, 'start', fill=NX, bold=True))
    o.append(L(mx + 30, (y1 + y2) / 2, mx + 30, (y3 + y4) / 2, LV, 2, dash='4 3'))
    o.append(C(mx + 30, (y1 + y2) / 2, 4, LV)); o.append(C(mx + 30, (y3 + y4) / 2, 4, LV))
    o.append(T(mx + 30, y4 + 24, 'pitch = 3λ + 3λ = 6λ = 3.0 μm, centre to centre', 13, 'start', fill=LV, bold=True))
    return 322, ''.join(o)


def stick(o, x0, cols, p_nodes, n_nodes, gates, p_contacts, n_contacts, metal, ytop=40, gap=66, legend=True):
    """a CMOS stick diagram. Node slots sit at even positions, gates at odd ones. p_nodes / n_nodes: node names per slot;
    p_contacts / n_contacts: slots that get a contact; metal: list of polylines (lists of points) for signal wires."""
    yv, yp, yn, yg = ytop, ytop + 70, ytop + 70 + 160, ytop + 70 + 220
    xs = lambda i: x0 + i * gap / 2
    xr = xs(cols - 1)
    o.append(L(x0 - 30, yv, xr + 30, yv, AC, 6)); o.append(T(x0 - 30, yv - 12, 'VDD', 14, 'start', fill=AC, bold=True))
    o.append(L(x0 - 30, yg, xr + 30, yg, AC, 6)); o.append(T(x0 - 30, yg + 24, 'VSS', 14, 'start', fill=AC, bold=True))
    o.append(L(x0 - 18, yp, xr + 18, yp, NX, 7)); o.append(L(x0 - 18, yn, xr + 18, yn, NX, 7))
    for i, g in gates.items():
        o.append(L(xs(i), yp - 26, xs(i), yn + 22, LV, 4))
        o.append(T(xs(i), yn + 40, g, 15, fill=LV, bold=True))
    for i in p_contacts:
        if p_nodes[i] == 'VDD': o.append(L(xs(i), yv, xs(i), yp, AC, 4))
        o.append(C(xs(i), yp, 6, INK))
    for i in n_contacts:
        if n_nodes[i] == 'VSS': o.append(L(xs(i), yn, xs(i), yg, AC, 4))
        o.append(C(xs(i), yn, 6, INK))
    for pts in metal: o.append(P(pts, AC, 4))
    for i, nm in p_nodes.items(): o.append(T(xs(i) + 10, yp + 22, nm, 13, 'start', fill=MUT))
    for i, nm in n_nodes.items(): o.append(T(xs(i) + 10, yn - 10, nm, 13, 'start', fill=MUT))
    return xs, yv, yp, yn, yg


# ---- 2.7 stick diagram of y = ¬(a·b + c), the worked example ----
def f7():
    o = []
    x0, gap = 70, 140
    xs = lambda i: x0 + i * gap / 2
    yp, yn = 110, 270
    h1, h2 = 150, 210
    metal = [[(xs(2), yp), (xs(2), h1), (xs(6), h1), (xs(6), yp)],
             [(xs(0), yp), (xs(0), h2), (xs(2) - 16, h2), (xs(2) - 16, yn - 24), (xs(2), yn - 24), (xs(2), yn)]]
    stick(o, x0, 7, {0: 'y', 2: 'n2', 4: 'VDD', 6: 'n2'}, {0: 'VSS', 2: 'y', 4: 'n1', 6: 'VSS'},
          {1: 'c', 3: 'a', 5: 'b'}, [0, 2, 4, 6], [0, 2, 6], metal, gap=gap)
    o.append(T(xs(0) + 8, h2 - 8, 'y (out)', 13, 'start', fill=AC, bold=True))
    o.append(Tb(xs(4) + 28, h1 + 18, 'n2 to n2', 13, 'middle', fill=AC))
    lx = 560
    o.append(T(lx, 70, 'Layers', 14, 'start', bold=True))
    for j, (c, w, lab) in enumerate(((NX, 7, 'diffusion'), (LV, 4, 'poly'), (AC, 4, 'metal'))):
        o.append(L(lx, 96 + 26 * j, lx + 40, 96 + 26 * j, c, w)); o.append(T(lx + 50, 101 + 26 * j, lab, 13, 'start'))
    o.append(C(lx + 20, 174, 6, INK)); o.append(T(lx + 50, 179, 'contact', 13, 'start'))
    o.append(T(lx, 220, 'order c, a, b', 14, 'start', bold=True))
    o.append(T(lx, 242, 'on both strips', 13, 'start', fill=MUT))
    o.append(T(lx, 266, '6 poly–diffusion', 13, 'start', fill=MUT)); o.append(T(lx, 284, 'crossings = 6 FETs', 13, 'start', fill=MUT))
    return 366, ''.join(o)


# ---- 2.8 the latch-up loop with the worked example's numbers ----
def bjt(o, x, y, kind, d, label):
    """transistor symbol with its base lead entering at (x, y); d = +1 puts the body to the right, -1 to the left.
    The leads leave at x + 32d, up to y - 40 and down to y + 40. npn: collector up, emitter down (arrow out);
    pnp: emitter up (arrow in), collector down."""
    X = lambda v: x + d * v
    o.append(f'<circle cx="{X(24):.1f}" cy="{y}" r="26" style="fill:{PANEL};stroke:{INK};stroke-width:1.6"/>')
    o.append(L(x, y, X(14), y, INK, 2)); o.append(L(X(14), y - 14, X(14), y + 14, INK, 3))
    if kind == 'npn':
        o.append(L(X(14), y - 7, X(32), y - 22, INK, 2)); o.append(L(X(14), y + 7, X(32), y + 22, INK, 2, arrow='m'))
    else:
        o.append(L(X(32), y - 22, X(15), y - 8, INK, 2, arrow='m')); o.append(L(X(14), y + 7, X(32), y + 22, INK, 2))
    o.append(L(X(32), y - 22, X(32), y - 40, INK, 2)); o.append(L(X(32), y + 22, X(32), y + 40, INK, 2))
    o.append(T(X(62), y + 5, label, 14, 'start' if d > 0 else 'end', bold=True))


def f8():
    o = []
    o.append(L(40, 30, 450, 30, AC, 3)); o.append(T(44, 22, 'VDD', 14, 'start', fill=AC, bold=True))
    o.append(L(40, 330, 450, 330, NX, 3)); o.append(T(44, 352, 'VSS', 14, 'start', fill=NX, bold=True))
    bjt(o, 300, 120, 'pnp', -1, 'pnp, β = 20')       # leads at x = 268
    o.append(L(268, 80, 268, 30, INK, 2)); o.append(T(260, 58, 'E: p+ source', 13, 'end', fill=MUT))
    bjt(o, 330, 250, 'npn', 1, 'npn, β = 50')        # leads at x = 362
    o.append(L(362, 290, 362, 330, INK, 2)); o.append(T(370, 316, 'E: n+ source', 13, 'start', fill=MUT))
    # n-well node: pnp base and npn collector, R_well up to VDD
    o.append(P([(362, 210), (362, 120), (300, 120)], INK, 2)); o.append(C(330, 120, 4, INK))
    o.append(zig(330, 120, 330, 30, INK)); o.append(T(342, 70, 'R_well = 1 kΩ', 13, 'start', bold=True))
    o.append(T(372, 160, 'n-well', 13, 'start', fill=AC, bold=True))
    # substrate node: pnp collector and npn base, R_sub down to VSS
    o.append(P([(268, 160), (268, 250), (330, 250)], INK, 2)); o.append(C(300, 250, 4, INK))
    o.append(zig(300, 250, 300, 330, INK)); o.append(T(284, 300, 'R_sub', 13, 'end', bold=True))
    o.append(T(230, 274, 'p-substrate', 13, fill=NX, bold=True))
    o.append(L(190, 215, 294, 246, LV, 2.5, arrow='l')); o.append(T(186, 212, '2 mA spike', 13, 'end', fill=LV, bold=True))
    bx = 486
    o.append(boxt(bx, 40, 220, 80, ['Substrate 200 Ω', '2 mA × 200 Ω = 0.4 V', 'below 0.7 V: npn off'], PANEL, NX, 13, True))
    o.append(boxt(bx, 134, 220, 80, ['Substrate 500 Ω', '2 mA × 500 Ω = 1.0 V', 'above 0.7 V: npn on'], LVS, LV, 13, True))
    o.append(boxt(bx, 270, 220, 56, ['loop gain 50 × 20 = 1000', '> 1: regenerative'], ACS, AC, 13, True))
    return 362, ''.join(o)


FIG = {
    1: (f1, 'The drive-in profile of the worked example on a log scale. The phosphorus falls only to C<sub>s</sub>/e at one diffusion length, 0.21 μm; the junction sits where it meets the wafer doping, 0.52 μm down.',
        'Gaussian profile of phosphorus concentration against depth, starting at 5.43 times ten to the eighteen per cubic centimetre, crossing the wafer doping of ten to the sixteen at 0.52 micrometres.'),
    2: (f2, 'The etch of worked example 2. In the same 6.0 minutes the wet etch eats 0.6 μm sideways under the resist on each side, while RIE moves only 0.06 μm.',
        'Two cross-sections of resist on oxide on silicon: the wet etch leaves a rounded hole 3.2 micrometres wide at the top, the RIE hole is 2.12 micrometres wide with near-vertical walls.'),
    3: (f3, 'The ten masks of the worked example in order. Five front-end masks build the transistors and five back-end masks wire them; dropping metal 2 also drops its via.',
        'Two rows of five boxes: n-well, active, poly, n+ and p+ source/drain masks, then contact, metal 1, via, metal 2 and pad masks, with the yield and good-die count.'),
    4: (f4, 'A twin-tub CMOS inverter. The PMOS body is the n-well, tied to VDD by an n<sup>+</sup> tap; the NMOS body is the p-well, tied to VSS by a p<sup>+</sup> tap, and its doping sets the body effect of the worked example.',
        'Cross-section with an n-well holding a PMOS and an n+ tap to VDD, and a p-well holding an NMOS and a p+ tap to VSS, in a p-substrate; one poly input drives both gates and the drains form the output.'),
    5: (f5, 'The vertical NPN of a BiCMOS process. Electrons go down from the emitter through the thin base, along the n<sup>+</sup> buried layer and up the sinker to the collector contact, so the collector resistance stays small.',
        'Cross-section with n+ emitter inside a p base, in a lightly doped n epitaxial collector over an n+ buried layer, with an n+ sinker to the collector contact and p isolation at the sides; arrows show the current path.'),
    6: (f6, 'The rules of the worked example drawn to scale with λ = 0.5 μm: one transistor with its contacts, and two minimum metal 1 wires with their width, spacing and pitch.',
        'Layout of a transistor 8 lambda wide with a 2 lambda poly gate and two contacts in 4 lambda metal squares, beside two metal wires 3 lambda wide and 3 lambda apart with a 6 lambda pitch.'),
    7: (f7, 'Stick diagram of y = ¬(a·b + c). Both diffusion strips use the column order c, a, b; on the p-strip the two n2 ends are joined in metal, and on the n-strip both ends go to VSS. Poly is drawn orange here; many books draw it red.',
        'Stick diagram with VDD and VSS rails, a p diffusion strip and an n diffusion strip, three poly columns c, a and b, contacts and metal links for n2 and the output y.'),
    8: (f8, 'The latch-up loop of the worked example. The npn collector drives the pnp base through the n-well, and the pnp collector drives the npn base through the substrate; R<sub>sub</sub> decides whether a 2 mA spike turns the npn on.',
        'Equivalent circuit with a pnp from VDD and an npn to VSS, the well resistor of 1 kilohm and the substrate resistor, a 2 milliamp spike into the substrate, and boxes with 0.4 volt, 1.0 volt and a loop gain of 1000.'),
}
spec = make_spec(FIG)
AFTER = {2: 2, 5: 1, 6: 4, 8: 1}
_spec = spec
def spec(k):
    d = _spec(k)
    if k in AFTER: d['after_section'] = AFTER[k]
    return d
