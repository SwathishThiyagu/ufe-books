"""Claude's hand-drawn figures for ce-rcc-u1 (Design of Reinforced Concrete Structures: design philosophies and material
behaviour), one per chapter, drawn from each chapter's own worked example. Every plotted value is computed here from the
example's data (IS 456:2000 values, SP 16 design curve for Fe415). Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt
_SUB = re.compile(r'(?<![A-Za-z])(σcbc|σst|fck|fy|xu|Ast|γf|γm)(?![A-Za-z])')


def _sub(s):
    """fck, xu, σcbc ... drawn with real subscripts"""
    return _SUB.sub(lambda m: m.group(1)[0] + f'<tspan baseline-shift="sub" font-size="12">{m.group(1)[1:]}</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)

FIG = {}
AFTER = {}


def sb(base, s, size=14):
    """text with a subscript, for SVG labels"""
    return f'{base}<tspan dy="4" font-size="{size - 3}">{s}</tspan><tspan dy="-4"> </tspan>'


# ---- 1.1 design stress-strain curves: concrete M25 and steel Fe415 / Fe250 ----
def f1():
    o = []
    # left panel: concrete
    x0, x1, y0, y1 = 80, 330, 60, 290
    fx = lambda e: x0 + e / 0.004 * (x1 - x0)
    fy = lambda s: y1 - s / 20 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.001, 0.002, 0.003], [0, 5, 10, 15, 20], fx, fy,
                  'strain (×10⁻³)', 'stress (N/mm²)', xfmt=lambda v: f'{v * 1000:g}', yfmt=str))
    def conc(peak):
        pts = []
        for i in range(41):
            e = 0.002 * i / 40
            pts.append((fx(e), fy(peak * (2 * e / 0.002 - (e / 0.002) ** 2))))
        pts.append((fx(0.0035), fy(peak)))
        return pts
    o.append(P(conc(16.75), MUT, 2, '6 4'))
    o.append(P(conc(11.17), AC, 3))
    o.append(T(fx(0.0035) + 4, fy(16.75) - 8, '0.67fck = 16.75', 13, 'end', MUT, True))
    o.append(T(fx(0.0035) + 4, fy(11.17) - 8, '0.446fck = 11.15', 13, 'end', AC, True))
    o.append(L(fx(0.002), fy(11.17), fx(0.002), y1, L2, 1.5, '4 3'))
    o.append(L(fx(0.0035), fy(11.17), fx(0.0035), y1, L2, 1.5, '4 3'))
    o.append(Tb(fx(0.002), fy(4), '0.002', 13, 'middle', INK, True))
    o.append(Tb(fx(0.0035), fy(4), '0.0035', 13, 'middle', INK, True))
    o.append(T((x0 + x1) / 2, 28, 'Concrete M25', 15, 'middle', INK, True))
    # right panel: steel
    X0, X1 = 430, 690
    gx = lambda e: X0 + e / 0.005 * (X1 - X0)
    gy = lambda s: y1 - s / 400 * (y1 - y0)
    o.append(axes(X0, X1, y0, y1, [0, 0.001, 0.002, 0.003, 0.004, 0.005], [0, 100, 200, 300, 400], gx, gy,
                  'strain (×10⁻³)', 'stress (N/mm²)', xfmt=lambda v: f'{v * 1000:g}', yfmt=str))
    fyd = 0.87 * 415
    pts = [(0, 0)] + [(f * fyd / 2e5 + ie, f * fyd) for f, ie in
                      [(0.8, 0), (0.85, 1e-4), (0.9, 3e-4), (0.95, 7e-4), (0.975, 1e-3), (1.0, 2e-3)]] + [(0.005, fyd)]
    o.append(P([(gx(e), gy(s)) for e, s in pts], AC, 3))
    for e, s in pts[1:-1]:
        o.append(C(gx(e), gy(s), 3.5, AC))
    o.append(P([(gx(0), gy(0)), (gx(217.5 / 2e5), gy(217.5)), (gx(0.005), gy(217.5))], NX, 2.5))
    o.append(T(gx(0.005), gy(fyd) - 10, 'Fe415: 0.87fy = 361 at 0.0038', 13, 'end', AC, True))
    o.append(T(gx(0.005), gy(217.5) + 22, 'Fe250: 0.87fy = 217.5', 13, 'end', NX, True))
    o.append(L(gx(0.0038), gy(fyd), gx(0.0038), y1, L2, 1.5, '4 3'))
    o.append(Tb(gx(0.00144) - 8, gy(288.8) - 4, '0.8 × 361 = 289', 13, 'end', MUT))
    o.append(T((X0 + X1) / 2, 28, 'Steel: design curves', 15, 'middle', INK, True))
    return 350, ''.join(o)


FIG[1] = (f1, 'The design curves of the worked example. Left: M25 concrete rises as a parabola to a strain of 0.002 and stays flat to 0.0035; the dashed curve is 0.67fck before the material factor. Right: Fe415 leaves the straight line at 0.8 × 0.87fy and reaches 361 N/mm² only at a strain of 0.0038, while Fe250 has a sharp corner at 217.5 N/mm².',
          'Two plots. Left, concrete stress against strain up to 0.0035: a parabola to 0.002 then flat, at 11.15 N/mm² for design and 16.75 dashed. Right, steel design curves: Fe415 straight to 289 N/mm², then curving to 361 at strain 0.0038; Fe250 straight to 217.5 then flat.')
AFTER[1] = 2


# ---- 1.2 WSM: section, strain and stress for the designed beam ----
def f2():
    o = []
    b, D, d, x = 250, 500, 460, 133.9
    s = 0.5
    top = 40
    X = 90
    w = b * s
    o.append(R(X, top, w, D * s, ACS, AC, 2))
    for cx, r in ((X + 22, 7), (X + w / 2, 5.5), (X + w - 22, 7)):
        o.append(C(cx, top + d * s, r, INK))
    yna = top + x * s
    o.append(L(X - 8, yna, 560, yna, NX, 1.5, '6 4'))
    o.append(T(X + w + 8, yna - 7, 'neutral axis', 13, 'start', NX))
    o.append(T(X + w + 8, yna + 18, 'x = 133.9', 13, 'start', NX, True))
    o.append(T(X + w / 2, top + D * s + 22, 'b = 250, D = 500', 14, 'middle', INK, True))
    o.append(T(X + w / 2, top + D * s + 42, '2 bars 16 + 1 bar 12 = 515 mm²', 13, 'middle', MUT))
    o.append(L(X - 16, top, X - 16, top + d * s, L2, 1.5))
    o.append(T(X - 22, top + d * s / 2, 'd = 460', 13, 'end', INK, True))
    # stress diagram
    S0 = 400
    yd = top + d * s
    o.append(L(S0, top, S0, yd, L2, 1.5))
    o.append(P([(S0, top), (S0 + 130, top), (S0, yna), (S0, top)], AC, 2.5, fill=ACS))
    o.append(T(S0 + 138, top + 5, 'σcbc = 6.80 ≤ 7', 13, 'start', AC, True))
    yc = top + x * s / 3
    o.append(L(S0 + 120, yc + 30, S0 + 14, yc, AC, 2, arrow='n'))
    o.append(T(S0 + 126, yc + 40, 'C = 113.8 kN at x/3 from top', 13, 'start', AC))
    o.append(L(S0, yd, S0 + 140, yd, LV, 3, arrow='l'))
    o.append(T(S0 + 148, yd - 6, 'σst = 221 ≤ 230', 13, 'start', LV, True))
    o.append(T(S0 + 148, yd + 18, 'T = 113.8 kN', 13, 'start', LV))
    o.append(L(S0 - 24, yc, S0 - 24, yd, INK, 1.5))
    o.append(L(S0 - 30, yc, S0 - 18, yc, INK, 1.5)); o.append(L(S0 - 30, yd, S0 - 18, yd, INK, 1.5))
    o.append(Tb(S0 - 28, (yc + yd) / 2, 'z = 415.4', 13, 'end', INK, True))
    o.append(T(S0 + 60, top + D * s + 42, 'stresses in N/mm² under M = 47.3 kNm', 13, 'middle', MUT))
    return 340, ''.join(o)


FIG[2] = (f2, 'The beam designed in the worked example under its service moment of 47.3 kNm. The neutral axis sits 133.9 mm down; concrete reaches 6.80 N/mm² at the top and steel 221 N/mm², both under their permissible values, and the equal forces C and T are 415.4 mm apart.',
          'Cross-section 250 by 500 mm with three bars at effective depth 460 mm, a dashed neutral axis at 133.9 mm, and beside it a triangular compression stress of 6.80 N/mm² at the top and a steel stress arrow of 221 N/mm², with C and T of 113.8 kN and lever arm 415.4 mm.')
AFTER[2] = 3


# ---- 1.3 ULM: service, required ultimate and collapse moments ----
def f3():
    o = []
    # beam with UDL
    bx0, bx1, by = 110, 610, 80
    o.append(R(bx0, by, bx1 - bx0, 22, ACS, AC, 3))
    for i in range(11):
        xx = bx0 + 10 + i * (bx1 - bx0 - 20) / 10
        o.append(L(xx, by - 34, xx, by - 3, NX, 1.6, arrow='x'))
    o.append(L(bx0 + 10, by - 34, bx1 - 10, by - 34, NX, 1.6))
    o.append(T((bx0 + bx1) / 2, by - 42, 'service load 12 + 8 = 20 kN/m  →  ultimate 1.5 × 20 = 30 kN/m', 13, 'middle', NX, True))
    o.append(P([(bx0 + 10, by + 22), (bx0, by + 40), (bx0 + 20, by + 40), (bx0 + 10, by + 22)], INK, 2))
    o.append(P([(bx1 - 10, by + 22), (bx1 - 20, by + 40), (bx1, by + 40), (bx1 - 10, by + 22)], INK, 2))
    o.append(T((bx0 + bx1) / 2, by + 44, 'span 6.0 m, simply supported', 13, 'middle', MUT))
    # bars
    x0 = 250; sc = 1.75
    rows = [('service moment', 90.0, MUT, PANEL), ('required ultimate moment', 135.0, NX, NXS), ('collapse moment of section', 226.0, AC, ACS)]
    for i, (lab, v, c, f) in enumerate(rows):
        y = 160 + i * 48
        o.append(T(x0 - 10, y + 20, lab, 14, 'end', INK))
        o.append(R(x0, y, v * sc, 28, f, c, 4))
        o.append(T(x0 + v * sc + 8, y + 20, f'{v:.0f} kNm', 14, 'start', c, True))
    o.append(L(x0, 150, x0, 312, L2, 1.5))
    o.append(T(360, 336, '226 ≥ 135: the section passes; 226 / 90 = 2.5 against collapse at service load', 14, 'middle', INK, True))
    return 352, ''.join(o)


FIG[3] = (f3, 'The beam of the worked examples. The service load is multiplied once by the load factor 1.5, so the 90 kNm service moment becomes a required ultimate moment of 135 kNm; the section, with materials at full strength, can carry 226 kNm.',
          'A simply supported 6 m beam under a uniform load, labelled 20 kN/m service and 30 kN/m ultimate. Below, three bars: service moment 90 kNm, required ultimate moment 135 kNm and collapse moment 226 kNm.')
AFTER[3] = 1


# ---- 1.4 limit states and the deflection checks of the example ----
def f4():
    o = []
    o.append(boxt(250, 14, 220, 40, ['Limit states (IS 456)'], ACS, AC, 15, True))
    o.append(L(330, 54, 190, 82, AC, 2, arrow='n')); o.append(L(390, 54, 530, 82, AC, 2, arrow='n'))
    o.append(boxt(30, 86, 320, 112, ['Collapse: safety', 'flexure · shear · compression · torsion', 'factored loads, γf = 1.5', 'design strengths, γm = 1.5 and 1.15'], PANEL, AC, 14, True))
    o.append(boxt(370, 86, 320, 112, ['Serviceability: use', 'deflection · cracking', 'service loads, γf = 1.0', 'crack width ≤ 0.3 mm (general)'], PANEL, LV, 14, True))
    # deflection gauges for the 6 m beam
    o.append(T(360, 232, 'Worked example: 6 m beam', 14, 'middle', INK, True))
    x0 = 200; sc = 13
    rows = [('final deflection', 22, 24.0, 'limit span/250 = 24 mm', AC, 'passes'), ('after partitions', 19, 17.14, 'limit span/350 = 17.1 mm', LV, 'fails')]
    for i, (lab, v, lim, ltxt, c, res) in enumerate(rows):
        y = 252 + i * 62
        o.append(T(x0 - 10, y + 20, lab, 14, 'end', INK))
        o.append(R(x0, y, v * sc, 28, ACS if v <= lim else LVS, c, 4))
        o.append(L(x0 + lim * sc, y - 6, x0 + lim * sc, y + 36, INK, 2.5, '5 3'))
        o.append(T(x0 + max(v, lim) * sc + 12, y + 20, f'{v} mm: {res}', 14, 'start', c, True))
        o.append(T(x0 + lim * sc, y + 52, ltxt, 13, 'middle', MUT))
    return 392, ''.join(o)


FIG[4] = (f4, 'IS 456 asks two questions of every member: will it stand (collapse, at factored loads) and will it serve (deflection and cracking, at service loads). The bars are the 6 m beam of the first worked example: its final deflection passes, but the deflection after the partitions are built fails.',
          'Tree with collapse limit states (flexure, shear, compression, torsion; factored loads; design strengths) and serviceability limit states (deflection, cracking; service loads). Below, two bars: final deflection 22 mm against a limit of 24 mm, passing, and deflection after partitions 19 mm against 17.1 mm, failing.')
AFTER[4] = 3


# ---- 1.5 cube results: normal curve, 5 % tail, fck ----
def f5():
    o = []
    mu, sg = 32.0, 4.0
    x0, x1, y0, y1 = 70, 680, 50, 280
    fx = lambda v: x0 + (v - 16) / 32 * (x1 - x0)
    pdf = lambda v: math.exp(-0.5 * ((v - mu) / sg) ** 2) / (sg * math.sqrt(2 * math.pi))
    pk = pdf(mu)
    fy = lambda p: y1 - p / pk * (y1 - y0 - 20)
    fck = mu - 1.65 * sg
    tail = [(fx(16), y1)] + [(fx(v), fy(pdf(v))) for v in [16 + i * (fck - 16) / 40 for i in range(41)]] + [(fx(fck), y1)]
    o.append(P(tail, LV, 1, fill=LVS))
    o.append(P([(fx(v), fy(pdf(v))) for v in [16 + i * 0.4 for i in range(81)]], AC, 3))
    o.append(xaxis(x0, x1, y1, [16, 20, 24, 28, 32, 36, 40, 44, 48], fx, 'cube strength at 28 days (N/mm²)'))
    o.append(L(fx(mu), fy(pk) - 4, fx(mu), y1, AC, 1.5, '5 4'))
    o.append(T(fx(mu), y0 + 6, 'mean μ = 32', 14, 'middle', AC, True))
    o.append(L(fx(fck), fy(pdf(fck)) - 60, fx(fck), y1, LV, 2))
    o.append(T(fx(fck) - 6, fy(pdf(fck)) - 66, 'fck = 32 − 1.65 × 4 = 25.4', 14, 'end', LV, True))
    o.append(T(fx(20.6), y1 - 14, '5 %', 14, 'middle', LV, True))
    o.append(L(fx(fck), y1 - 52, fx(mu), y1 - 52, INK, 1.5, arrow='m'))
    o.append(Tb((fx(fck) + fx(mu)) / 2, y1 - 58, '1.65σ = 6.6', 13, 'middle', INK, True))
    o.append(T(fx(44), 110, 'σ = 4 N/mm²', 14, 'middle', MUT))
    o.append(T(fx(44), 132, 'grade chosen: M25', 14, 'middle', INK, True))
    return 330, ''.join(o)


FIG[5] = (f5, 'Cube results of the worked example spread about their mean of 32 N/mm² with a standard deviation of 4 N/mm². The shaded tail holds the weakest 5 %; its edge, 1.65σ below the mean, is the characteristic strength 25.4 N/mm², so the concrete is called M25.',
          'Bell curve of cube strength from 16 to 48 N/mm², peaking at the mean of 32. A shaded left tail of 5 % ends at 25.4 N/mm², marked fck, which is 6.6 N/mm² (1.65 sigma) below the mean.')
AFTER[5] = 1


# ---- 1.6 factored moments of the load-combination example ----
def f6():
    o = []
    rows = [('1.5(DL + LL)', 97.5), ('1.5(DL + WL)', 105.0), ('1.5(DL − WL)', 15.0), ('1.2(DL + LL + WL)', 114.0),
            ('1.2(DL + LL − WL)', 42.0), ('0.9DL + 1.5WL', 81.0), ('0.9DL − 1.5WL', -9.0)]
    zx = 300; sc = 3.0
    o.append(T(20, 26, 'Moments at midspan: DL 40, LL 25, WL ±30 kNm', 15, 'start', INK, True))
    for i, (lab, v) in enumerate(rows):
        y = 48 + i * 38
        big = v == 114.0; neg_ = v < 0
        c = LV if neg_ else (AC if big else MUT)
        f = LVS if neg_ else (ACS if big else PANEL)
        o.append(T(200, y + 19, lab, 14, 'end', INK))
        if v >= 0:
            o.append(R(zx, y, v * sc, 26, f, c, 4))
            o.append(T(zx + v * sc + 8, y + 19, f'{v:g}', 14, 'start', c, True))
        else:
            o.append(R(zx + v * sc, y, -v * sc, 26, f, c, 4))
            o.append(T(zx + v * sc - 8, y + 19, neg(f'{v:g}'), 14, 'end', c, True))
    o.append(L(zx, 40, zx, 48 + 7 * 38, INK, 1.5))
    o.append(T(zx, 48 + 7 * 38 + 20, '0', 13, 'middle', MUT))
    o.append(T(470, 48 + 7 * 38 + 20, 'factored moment (kNm), sagging positive', 13, 'middle', MUT))
    o.append(T(690, 48 + 3 * 38 + 19 + 26, 'largest sagging', 13, 'end', AC, True))
    o.append(T(690, 48 + 6 * 38 + 19, 'reversal: top steel', 13, 'end', LV, True))
    return 360, ''.join(o)


FIG[6] = (f6, 'The seven collapse combinations of the second worked example. The combination with all three loads at 1.2 gives the largest sagging moment, 114 kNm, while 0.9DL with wind lifting gives −9 kNm: the moment reverses, so the beam also needs steel at the top.',
          'Horizontal bar chart of factored midspan moments: 97.5, 105, 15, 114, 42, 81 and minus 9 kNm for the seven IS 456 collapse combinations of dead, live and wind load; 114 is highlighted as the largest and minus 9 as a reversal.')
AFTER[6] = 2


# ---- 1.7 stress block: strain, stress and forces for the analysed beam ----
def f7():
    o = []
    b, D, d, xu = 230, 450, 450, 105.2
    s = 0.62
    top = 46
    X = 40
    o.append(R(X, top, b * s * 0.6, (D + 40) * s, ACS, AC, 2))
    w = b * s * 0.6
    for cx in (X + 18, X + w / 2, X + w - 18):
        o.append(C(cx, top + d * s, 6, INK))
    o.append(T(X + w / 2, top + (D + 40) * s + 22, 'b = 230', 14, 'middle', INK, True))
    o.append(T(X + w / 2, top + (D + 40) * s + 42, '3 bars of 16 mm', 13, 'middle', MUT))
    yna = top + xu * s
    o.append(L(X - 6, yna, 690, yna, NX, 1.5, '6 4'))
    o.append(T(690, yna + 18, 'xu = 105.2', 13, 'end', NX, True))
    # strain diagram
    S0 = 230
    o.append(T(S0 + 40, 26, 'strain', 14, 'middle', INK, True))
    o.append(L(S0, top, S0, top + d * s, L2, 1.5))
    sc = 22000
    o.append(P([(S0 + 0.0035 * sc, top), (S0, yna), (S0 - 0.0035 * sc * 0.55, top + d * s)], AC, 2.5))
    o.append(L(S0, top, S0 + 0.0035 * sc, top, AC, 2))
    o.append(T(S0 + 0.0035 * sc + 4, top + 5, '0.0035', 13, 'start', AC, True))
    y2 = top + (xu * 3 / 7) * s
    o.append(L(S0, y2, S0 + 0.002 * sc, y2, MUT, 1.5, '4 3'))
    o.append(T(S0 + 0.002 * sc + 6, y2 + 5, '0.002', 13, 'start', MUT, True))
    o.append(L(S0, top + d * s, S0 - 0.0035 * sc * 0.55, top + d * s, LV, 2))
    o.append(T(S0 - 0.0035 * sc * 0.55 - 4, top + d * s + 20, '0.0115 > 0.0038: yields', 13, 'start', LV, True))
    # stress block
    B0 = 400
    o.append(T(B0 + 60, 26, 'stress', 14, 'middle', INK, True))
    o.append(L(B0, top, B0, top + d * s, L2, 1.5))
    k = 9.0  # px per N/mm²
    pts = [(B0, top), (B0 + 11.15 * k, top), (B0 + 11.15 * k, y2)]
    for i in range(1, 21):
        t = i / 20  # 0 at the 0.002 level, 1 at the neutral axis
        e = 1 - t
        pts.append((B0 + 11.15 * k * (2 * e - e * e), y2 + t * (yna - y2)))
    pts.append((B0, yna))
    o.append(P(pts, AC, 2.5, fill=ACS))
    o.append(T(B0 + 11.15 * k + 4, top + 5, '0.446fck = 11.15', 13, 'start', AC, True))
    yc = top + 0.42 * xu * s
    o.append(L(B0 + 150, yc, B0 + 4, yc, INK, 2, arrow='n'))
    o.append(T(B0 + 156, yc + 5, 'C = 0.36fck b xu', 13, 'start', INK, True))
    o.append(T(B0 + 156, yc + 27, '= 217.8 kN at 0.42xu', 13, 'start', INK, True))
    o.append(L(B0 + 4, top + d * s, B0 + 150, top + d * s, LV, 3, arrow='l'))
    o.append(T(B0 + 156, top + d * s - 14, 'T = 0.87fy Ast', 13, 'start', LV, True))
    o.append(T(B0 + 156, top + d * s + 12, '= 217.7 kN', 13, 'start', LV, True))
    o.append(L(B0 - 16, yc, B0 - 16, top + d * s, INK, 1.5))
    o.append(L(B0 - 22, yc, B0 - 10, yc, INK, 1.5)); o.append(L(B0 - 22, top + d * s, B0 - 10, top + d * s, INK, 1.5))
    o.append(Tb(B0 - 20, (yc + top + d * s) / 2, 'z = 405.8', 13, 'end', INK, True))
    o.append(T(10 + 0, top + d * s + 4, '', 13))
    o.append(T(X + w + 8, top + d * s + 5, 'd = 450', 13, 'start', INK, True))
    return 400, ''.join(o)


FIG[7] = (f7, 'The beam of the first worked example at collapse. Strain is a straight line from 0.0035 at the top to the steel, which is far past its yield strain of 0.0038. The stress block is flat at 0.446fck down to 3/7 of xu and a parabola below; its force 217.8 kN acts 0.42xu from the top and balances the steel force.',
          'Cross-section 230 mm wide with three 16 mm bars at 450 mm depth, beside its strain diagram (0.0035 at the top, 0.002 at three-sevenths of xu, 0.0115 in the steel) and its stress block (flat at 11.15 N/mm² then parabolic to the neutral axis at 105.2 mm), with C of 217.8 kN at 44.2 mm, T of 217.7 kN and lever arm 405.8 mm.')
AFTER[7] = 1


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
