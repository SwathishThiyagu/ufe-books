"""Hand-drawn figures for ce-rcc-u6 (Introduction to Prestressed Concrete), drawn from each chapter's worked example."""
import os, sys; sys.path.insert(0, os.path.dirname(__file__)); from kit import *

FIG = {}


def SUB(t):
    return f'<tspan dy="4" font-size="13">{t}</tspan><tspan dy="-4"> </tspan>'
spec = make_spec(FIG)


def stress_diag(xa, yt, yb, vt, vb, s, col=AC, soft=ACS, fmt=None, size=14):
    """linear stress diagram on a vertical axis at xa: compression (positive) to the right"""
    fmt = fmt or (lambda v: neg(f'{v:.2f}'.rstrip('0').rstrip('.')))
    o = [f'<polygon points="{xa:.1f},{yt:.1f} {xa + vt * s:.1f},{yt:.1f} {xa + vb * s:.1f},{yb:.1f} {xa:.1f},{yb:.1f}" '
         f'style="fill:{soft};stroke:{col};stroke-width:2;stroke-linejoin:round"/>']
    o.append(L(xa, yt - 10, xa, yb + 10, INK, 2))
    o.append(T(xa + vt * s + (6 if vt >= 0 else -6), yt - 8, fmt(vt), size, 'start' if vt >= 0 else 'end', INK, True))
    o.append(T(xa + vb * s + (6 if vb >= 0 else -6), yb + 20, fmt(vb), size, 'start' if vb >= 0 else 'end', INK, True))
    return ''.join(o)


# ---- 6.1 the four stress blocks of the worked example (eccentric tendon, 56 kN·m) ----
def f1():
    o = []
    yt, yb = 100, 300
    # section sketch
    o.append(R(30, yt, 64, yb - yt, PANEL, INK, 2))
    o.append(L(22, (yt + yb) / 2, 102, (yt + yb) / 2, L2, 1.5, '5 4'))
    o.append(C(62, (yt + yb) / 2 + 50, 7, AC))
    o.append(T(62, yt - 30, '200 × 400', 13, fill=MUT))
    o.append(T(62, yt - 12, 'section', 13, fill=MUT))
    o.append(T(62, yb + 24, 'e = 100', 13, fill=AC, bold=True))
    s = 4.2
    cols = [(195, 'P/A', 5, 5, AC, ACS), (345, 'P·e/Z', -7.5, 7.5, AC, ACS), (520, 'load M/Z', 10.5, -10.5, NX, NXS), (640, 'final', 8, 2, LV, LVS)]
    for x, lab, vt, vb, c, sc in cols:
        o.append(T(x, 44, lab, 15, bold=True))
        o.append(stress_diag(x, yt, yb, vt, vb, s, c, sc))
    for x, op in ((262, '+'), (425, '+'), (590, '=')):
        o.append(T(x, 208, op, 26, bold=True, fill=MUT))
    o.append(T(360, 360, 'N/mm², compression to the right, tension to the left', 14, fill=MUT))
    return 380, ''.join(o)


FIG[1] = (f1, 'Stresses in the 200 mm × 400 mm beam of the worked example with the 400 kN tendon 100 mm below the centroid. '
              'The tendon alone leaves 2.5 N/mm² tension at the top and 12.5 N/mm² compression at the bottom; the 56 kN·m load then gives 8 N/mm² at the top and still 2 N/mm² compression at the bottom.',
          'Four stress diagrams over the section depth: uniform 5, then minus 7.5 at the top and plus 7.5 at the bottom from the tendon, then plus 10.5 and minus 10.5 from the load, adding to 8 at the top and 2 at the bottom, all in newtons per square millimetre.')


# ---- 6.2 what the same losses leave in mild steel and in strand ----
def f2():
    o = []
    x0, x1 = 150, 670
    sc = (x1 - x0) / 1400
    o.append(xaxis(x0, x1, 250, [0, 200, 400, 600, 800, 1000, 1200, 1400], lambda v: x0 + v * sc, 'tendon stress (N/mm²)'))
    loss = 186.8
    rows = [(80, 'Fe 250 mild steel', 200.0), (170, '12.7 mm strand', 1395.0)]
    for y, lab, f0 in rows:
        o.append(T(x0 - 10, y + 6, lab, 14, 'end', bold=True))
        left = f0 - loss
        o.append(R(x0, y - 16, left * sc, 32, LVS, LV, 3))
        o.append(R(x0 + left * sc, y - 16, loss * sc, 32, NXS, NX, 3))
    o.append(T(x0 - 4, 50, '13.2 left (7 %)', 14, 'start', INK, True))
    o.append(L(x0 + 2, 54, x0 + 2, 62, INK, 1.5))
    o.append(T(x0 + 200 * sc + 8, 86, 'jacked to 200', 13, 'start', MUT))
    o.append(T(x0 + 1208.2 * sc / 2, 176, '1208.2 left (87 %)', 14, 'middle', INK, True))
    o.append(T(x0 + 1395 * sc, 148, 'jacked to 1395', 13, 'end', MUT))
    o.append(T(x0 + 13.2 * sc + 93.4 * sc, 86, 'loss', 13, 'middle', NX, True))
    o.append(T(x0 + 1301.6 * sc, 214, 'loss 186.8', 13, 'middle', NX, True))
    o.append(T(330, 124, 'same loss: elastic 49.3 + creep 78.9 + shrinkage 58.5', 13, 'middle', MUT))
    return 300, ''.join(o)


FIG[2] = (f2, 'The 186.8 N/mm² lost by elastic shortening, creep and shrinkage in the worked example. It wipes out mild steel stretched to 200 N/mm² but takes only 13 percent of a strand jacked to 1395 N/mm².',
          'Two horizontal bars on a stress axis from 0 to 1400. The mild steel bar is 200 long with 186.8 lost and 13.2 left. The strand bar is 1395 long with 186.8 lost at the end and 1208.2 left.')


# ---- 6.3 the two systems ----
def f3():
    o = []
    # pre-tensioning bed
    o.append(T(20, 30, 'Pre-tensioning: stress, cast, cure, release', 15, 'start', bold=True))
    o.append(R(40, 50, 40, 90, ACS, AC, 3)); o.append(R(640, 50, 40, 90, ACS, AC, 3))
    o.append(T(60, 158, 'abutment', 13, fill=MUT)); o.append(T(660, 158, 'abutment', 13, fill=MUT))
    o.append(L(80, 100, 640, 100, AC, 3))
    for x in (130, 290, 450):
        o.append(R(x, 82, 120, 36, PANEL, INK, 4))
    o.append(T(190, 76, 'mould', 13, fill=MUT)); o.append(T(350, 76, 'mould', 13, fill=MUT)); o.append(T(510, 76, 'mould', 13, fill=MUT))
    o.append(T(360, 150, 'tendon stretched first; bond grips it at release', 13, fill=INK))
    o.append(T(360, 172, '100 m bed, 1395 N/mm²: extension 715.4 mm', 13, fill=AC, bold=True))
    # post-tensioning beam
    y0 = 230
    o.append(T(20, y0 - 10, 'Post-tensioning: cast with duct, then stress and grout', 15, 'start', bold=True))
    o.append(R(90, y0 + 10, 500, 90, PANEL, INK, 4))
    pts = [(90 + 500 * i / 40, y0 + 55 + 30 * (1 - ((i - 20) / 20) ** 2)) for i in range(41)]
    o.append(P(pts, LV, 6, fill='none', op=None))
    o.append(P(pts, AC, 2))
    o.append(R(80, y0 + 40, 10, 32, ACS, AC, 2)); o.append(R(590, y0 + 40, 10, 32, ACS, AC, 2))
    o.append(R(600, y0 + 44, 60, 24, NXS, NX, 4))
    o.append(L(640, y0 + 56, 690, y0 + 56, NX, 2.5, arrow='x'))
    o.append(T(630, y0 + 92, 'jack', 13, fill=NX, bold=True))
    o.append(T(52, y0 + 118, 'anchorage', 13, fill=MUT))
    o.append(T(340, y0 + 125, 'duct (grouted after stressing)', 13, fill=LV))
    o.append(T(360, y0 + 150, '30 m tendon, 7 strands, 964 kN: extension 214.6 mm', 13, fill=AC, bold=True))
    return 400, ''.join(o)


FIG[3] = (f3, 'Pre-tensioning stretches the tendon between abutments before casting; post-tensioning stresses it through a duct in hardened concrete and anchors it at the ends. The extensions are those of the worked example.',
          'Top: a long bed with two abutments, a stretched tendon and three moulds in a row. Bottom: a beam with a curved duct, anchorage plates at both ends and a jack pulling at the right end.')


# ---- 6.4 load balancing of the 10 m beam ----
def f4():
    o = []
    x0, x1, yt, yb = 90, 630, 140, 230
    o.append(R(x0, yt, x1 - x0, yb - yt, PANEL, INK, 2))
    yc = (yt + yb) / 2
    o.append(L(x0 - 10, yc, x1 + 10, yc, L2, 1.2, '5 4'))
    pts = [(x0 + (x1 - x0) * i / 40, yc + 25 * (1 - ((i - 20) / 20) ** 2)) for i in range(41)]
    o.append(P(pts, AC, 3))
    # supports
    for x in (x0, x1):
        o.append(f'<polygon points="{x},{yb} {x - 12},{yb + 20} {x + 12},{yb + 20}" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    # downward load
    for i in range(10):
        x = x0 + 20 + i * (x1 - x0 - 40) / 9
        o.append(L(x, 78, x, yt - 4, NX, 2, arrow='x'))
    o.append(L(x0, 78, x1, 78, NX, 2))
    o.append(T(360, 66, 'load w = 3.75 + 6 = 9.75 kN/m', 14, fill=NX, bold=True))
    # upward equivalent load
    for i in range(10):
        x = x0 + 20 + i * (x1 - x0 - 40) / 9
        o.append(L(x, 300, x, yb + 32, LV, 2, arrow='l'))
    o.append(T(360, 322, 'tendon push w' + SUB('p') + '= 8Pe/L² = 7.2 kN/m', 14, fill=LV, bold=True))
    # end forces
    o.append(L(x0 - 50, yc, x0 - 4, yc, AC, 2.5, arrow='n')); o.append(L(x1 + 50, yc, x1 + 4, yc, AC, 2.5, arrow='n'))
    o.append(T(x0 - 40, yc - 10, '600 kN', 13, fill=AC, bold=True)); o.append(T(x1 + 40, yc - 10, '600 kN', 13, fill=AC, bold=True))
    o.append(Tb(360, yc + 40, 'sag 150 mm', 13, fill=AC))
    o.append(T(360, 360, 'net 2.55 kN/m bends the beam: 6.125 top, 1.875 bottom (N/mm²), deflection 2.3 mm', 14, fill=INK))
    o.append(T(360, 384, 'span 10 m, section 250 × 600', 13, fill=MUT))
    return 400, ''.join(o)


FIG[4] = (f4, 'The parabolic tendon of the worked example pushes up on the 10 m beam with 7.2 kN/m, so only 2.55 kN/m of the 9.75 kN/m load bends it. Superposing that net load on the uniform 4 N/mm² gives the same stresses as the stress and strength concepts.',
          'A simply supported beam with a parabolic tendon. Downward arrows above show the 9.75 kN per metre load; upward arrows below show the 7.2 kN per metre tendon push; 600 kN forces act at each end. A note gives the net 2.55 kN per metre and the resulting stresses.')


# ---- 6.5 tendon force along the 20 m girder ----
def f5():
    import math
    o = []
    x0, x1, y0, y1 = 100, 670, 50, 310
    fx = lambda x: x0 + x / 20 * (x1 - x0)
    fy = lambda P: y1 - (P - 1000) / 220 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 5, 10, 15, 20], [1000, 1050, 1100, 1150, 1200], fx, fy, 'distance from the jack (m)', 'tendon force (kN)'))
    fr = [(fx(x / 4), fy(1200 * math.exp(-0.0044 * x / 4))) for x in range(81)]
    o.append(P(fr, AC, 3))
    ls = 13.889; Pls = 1200 * math.exp(-0.0044 * ls)
    o.append(P([(fx(0), fy(1059.6)), (fx(ls), fy(Pls))], LV, 3))
    o.append(L(fx(ls), fy(Pls), fx(ls), y1, MUT, 1.5, '4 4'))
    o.append(C(fx(0), fy(1200), 5, AC)); o.append(C(fx(20), fy(1098.9), 5, AC)); o.append(C(fx(0), fy(1059.6), 5, LV))
    o.append(Tb(fx(0) + 12, fy(1200) + 4, 'jacked 1200', 13, 'start', AC, True))
    o.append(Tb(fx(20) - 10, fy(1098.9) - 12, 'far end 1098.9 (friction)', 13, 'end', AC, True))
    o.append(Tb(fx(0) + 12, fy(1059.6) + 18, 'after 5 mm draw-in 1059.6', 13, 'start', LV, True))
    o.append(Tb(fx(ls) + 6, y1 - 12, 'setting length 13.89 m', 13, 'start', MUT))
    return 370, ''.join(o)


FIG[5] = (f5, 'Tendon force along the 20 m girder of the second worked example. Friction lowers it from 1200 kN at the jack to 1098.9 kN at the far end; the 5 mm draw-in then lowers the jack end to 1059.6 kN, and its effect dies out 13.89 m from the jack.',
          'A plot of tendon force against distance. A falling curve runs from 1200 kN at zero to 1098.9 kN at 20 m. A second, rising line starts at 1059.6 kN at zero and meets the curve at 13.89 m.')


# ---- 6.6 transfer and service stresses at midspan ----
def f6():
    o = []
    yt, yb = 110, 290; s = 7.5
    cases = [(110, 'Transfer, e = 250', (-2.09, 14.59), (-1.4, 16), False),
             (340, 'Transfer, e = 220', (-0.69, 13.19), (-1.4, 16), True),
             (570, 'Service, e = 220', (6.88, 3.13), (0, 15), True)]
    for x, lab, (vt, vb), (lt, lc), ok in cases:
        o.append(T(x + 50, 48, lab, 15, bold=True))
        c, sc = (AC, ACS) if ok else (LV, LVS)
        o.append(stress_diag(x, yt, yb, vt, vb, s, c, sc))
        for v in (lt, lc):
            X = x + v * s
            o.append(L(X, yt - 28, X, yb + 28, MUT, 1.5, '4 4'))
        o.append(T(x + lc * s - 4, yt - 34, f'limit {lc:g}', 13, 'end', MUT))
        if lt < 0: o.append(T(x + lt * s - 4, yt - 34, f'limit {neg(lt)}', 13, 'end', MUT))
        o.append(T(x + 50, 345, 'fails at the top' if not ok else 'all limits met', 14, fill=c, bold=True))
    o.append(T(360, 375, 'N/mm², compression to the right; dashed lines are the permissible stresses', 13, fill=MUT))
    return 390, ''.join(o)


FIG[6] = (f6, 'Midspan stresses of the 300 mm × 800 mm beam of the first worked example. At e = 250 mm the top tension at transfer, 2.09 N/mm², passes the 1.4 N/mm² limit; at e = 220 mm both transfer and service stresses stay between the dashed limits.',
          'Three stress diagrams over the section depth with dashed limit lines. Transfer at 250 mm eccentricity shows minus 2.09 at the top, beyond the minus 1.4 limit. Transfer at 220 mm shows minus 0.69 and 13.19; service shows 6.88 and 3.13, all inside the limits.')


# ---- 6.7 the end block of the worked example ----
def f7():
    o = []
    sc = 0.5; x0, yt = 120, 70; Dd = 500 * sc; Ln = 760 * sc
    yb = yt + Dd; yc = (yt + yb) / 2
    o.append(R(x0 + 50 * sc - 25, yt + 5, 500 * sc, Dd - 10, NXS, 'none', 4, 0))
    o.append(R(x0, yt, Ln, Dd, 'none', INK, 2))
    o.append(R(x0 - 10, yc - 100 * sc, 10, 200 * sc, ACS, AC, 2))
    o.append(L(x0 - 70, yc, x0 - 14, yc, AC, 3, arrow='n'))
    o.append(T(x0 - 64, yc - 12, '1000 kN', 13, 'start', AC, True))
    for f in (-1, -0.5, 0, 0.5, 1):
        ys = yc + f * 100 * sc * 0.8
        ye = yc + f * Dd / 2 * 0.9
        o.append(f'<path d="M{x0:.1f},{ys:.1f} C{x0 + 140 * sc:.1f},{ys:.1f} {x0 + 300 * sc:.1f},{ye:.1f} {x0 + 520 * sc:.1f},{ye:.1f} L{x0 + Ln:.1f},{ye:.1f}" style="fill:none;stroke:var(--accent);stroke-width:1.6"/>')
    for d in (50, 190, 330, 470):
        X = x0 + d * sc
        o.append(L(X, yt + 6, X, yb - 6, LV, 3))
    o.append(brace(x0 + 50 * sc, x0 + 470 * sc, yb + 14, LV))
    o.append(T(x0 + 260 * sc, yb + 40, '4 closed 10 mm links at 140 mm (50 to 470 mm)', 13, fill=LV, bold=True))
    o.append(L(x0 + 8, yt + 8, x0 + 8, yb - 8, MUT, 2, '3 3'))
    o.append(T(x0 + 12, yt - 10, 'spalling mesh', 13, 'start', MUT))
    o.append(Tb(x0 + 300 * sc, yc - 70, 'bursting zone', 13, fill=NX, bold=True))
    o.append(T(x0 + Ln + 12, yt + 14, '500', 13, 'start', MUT))
    o.append(T(x0 + Ln + 12, yt + 32, 'deep', 13, 'start', MUT))
    o.append(T(20, yc + 44, 'plate', 13, 'start', AC, True)); o.append(T(20, yc + 62, '200 × 200', 13, 'start', AC))
    o.append(T(360, yb + 72, 'F' + SUB('bst') + '= 0.20 × 1000 = 200 kN over the depth; 170 kN across the 400 mm width', 14, fill=INK))
    o.append(T(360, yb + 94, 'bearing 25 N/mm² against 32 N/mm² allowed', 13, fill=MUT))
    return yb + 110, ''.join(o)


FIG[7] = (f7, 'Side view of the 500 mm deep end block of the worked example. The 1000 kN force fans out from the 200 mm plate to the full depth; across the shaded bursting zone this needs 200 kN of transverse tie, carried by four closed links.',
          'An end block in elevation with a small bearing plate at the left face and a 1000 kN arrow. Curved compression lines fan out to the full depth. A shaded bursting zone holds four vertical links at 50, 190, 330 and 470 millimetres, with a dashed spalling mesh just behind the face.')


# ---- 6.8 straight tendon in a two-span beam: secondary reactions and pressure line ----
def f8():
    o = []
    xa, xb, xc = 70, 360, 650; yc = 130; sc = 0.4
    o.append(R(xa, yc - 60, xc - xa, 120, PANEL, INK, 2))
    o.append(L(xa, yc, xc, yc, L2, 1.2, '5 4'))
    o.append(T(xa + 8, yc - 6, 'centroid', 13, 'start', MUT))
    o.append(L(xa, yc + 100 * sc, xc, yc + 100 * sc, AC, 2.5, '8 5'))
    o.append(P([(xa, yc + 100 * sc), (xb, yc - 50 * sc), (xc, yc + 100 * sc)], LV, 3))
    o.append(Tb(205, yc + 100 * sc + 5, 'tendon, 100 below', 13, 'middle', AC, True))
    o.append(Tb(xb, yc - 50 * sc - 14, 'pressure line, 50 above', 13, 'middle', LV, True))
    for x in (xa, xb, xc):
        o.append(f'<polygon points="{x},{yc + 60} {x - 11},{yc + 78} {x + 11},{yc + 78}" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    ya, yz = yc + 84, yc + 130
    o.append(L(xa, yz, xa, ya, NX, 2.5, arrow='x')); o.append(T(xa + 8, yz - 4, '15 kN', 13, 'start', NX, True))
    o.append(L(xc, yz, xc, ya, NX, 2.5, arrow='x')); o.append(T(xc - 8, yz - 4, '15 kN', 13, 'end', NX, True))
    o.append(L(xb, ya, xb, yz, NX, 2.5, arrow='x')); o.append(T(xb + 8, yz - 4, '30 kN', 13, 'start', NX, True))
    o.append(T(215, yz - 4, 'secondary reactions', 13, fill=NX))
    # moment diagrams, sagging drawn up
    y0 = 370; m = 0.45
    o.append(T(xa, 292, 'moments in kN·m (sagging up)', 13, 'start', MUT))
    o.append(L(xa, y0, xc, y0, L2, 1.5))
    o.append(P([(xa, y0), (xa, y0 + 100 * m), (xc, y0 + 100 * m), (xc, y0)], AC, 2, '6 4'))
    o.append(P([(xa, y0), (xb, y0 - 150 * m), (xc, y0)], NX, 2))
    o.append(P([(xa, y0 + 100 * m), (xb, y0 - 50 * m), (xc, y0 + 100 * m)], LV, 3))
    o.append(T(xb + 10, y0 - 150 * m - 6, '+150', 13, 'start', NX, True))
    o.append(T(xb - 12, y0 - 50 * m - 6, '+50', 13, 'end', LV, True))
    o.append(T(xa - 6, y0 + 100 * m + 5, '−100', 13, 'end', AC, True))
    ly = y0 + 80
    o.append(L(90, ly - 5, 120, ly - 5, AC, 2, '6 4')); o.append(T(126, ly, 'primary Pe', 13, 'start'))
    o.append(L(250, ly - 5, 280, ly - 5, NX, 2)); o.append(T(286, ly, 'secondary', 13, 'start'))
    o.append(L(400, ly - 5, 430, ly - 5, LV, 3)); o.append(T(436, ly, 'resultant (pressure line × P)', 13, 'start'))
    o.append(T(360, ly + 30, 'two spans of 10 m, P = 1000 kN; eccentricities drawn at twice the depth scale', 13, fill=MUT))
    return ly + 45, ''.join(o)


FIG[8] = (f8, 'The straight tendon of the worked example in a two-span beam. The middle support holds the beam down with 30 kN, and the resulting secondary moment of 150 kN·m moves the pressure line from 100 mm below the centroid at the ends to 50 mm above it at the middle support; a tendon placed along that line is concordant.',
          'A two-span beam with a straight dashed tendon 100 millimetres below the centroid and a solid pressure line rising to 50 millimetres above the centroid at the middle support. Arrows show 15 kN up at each end and 30 kN down at the middle. Below, the primary moment of minus 100, the secondary triangle reaching plus 150 and the resultant reaching plus 50.')


# ---- 6.9 where the floor beam sits ----
def f9():
    o = []
    x0, x1 = 90, 650
    fx = lambda v: x0 + v / 1.2 * (x1 - x0)
    o.append(T(20, 32, 'Degree of prestressing λ = M' + SUB('dec') + '/M' + SUB('s'), 15, 'start', bold=True))
    o.append(xaxis(x0, x1, 110, [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2], fx, None, lambda v: f'{v:.1f}'))
    o.append(R(fx(0), 70, fx(1.0) - fx(0), 40, LVS, 'none', 0, 0))
    o.append(R(fx(1.0), 70, fx(1.2) - fx(1.0), 40, ACS, 'none', 0, 0))
    o.append(T(fx(0.5), 64, 'partial (Type 3)', 13, fill=LV, bold=True))
    o.append(T(fx(1.1), 64, 'full', 13, fill=AC, bold=True))
    o.append(C(fx(0), 110, 6, NX)); o.append(T(fx(0) + 2, 150, 'RC', 13, fill=NX, bold=True))
    o.append(C(fx(0.565), 110, 7, LV)); o.append(T(fx(0.565), 150, 'this beam 0.56 (4 strands)', 13, fill=LV, bold=True))
    o.append(C(fx(1.0), 110, 7, AC)); o.append(T(fx(1.0) + 10, 168, '8 strands for λ = 1', 13, 'middle', AC, True))
    # ultimate forces
    o.append(T(20, 215, 'Steel forces at ultimate (kN)', 15, 'start', bold=True))
    sc = (x1 - x0) / 1000
    o.append(R(x0, 235, 638.9 * sc, 40, ACS, AC, 3))
    o.append(R(x0 + 638.9 * sc, 235, 262.4 * sc, 40, NXS, NX, 3))
    o.append(T(x0 + 638.9 * sc / 2, 261, 'strands 638.9', 14, fill=INK, bold=True))
    o.append(T(x0 + 638.9 * sc + 262.4 * sc / 2, 261, 'bars 262.4', 14, fill=INK, bold=True))
    o.append(T(x0, 300, 'PPR = 638.9/901.3 = 0.71; M' + SUB('u') + '= 429.8 kN·m', 14, 'start', MUT))
    return 320, ''.join(o)


FIG[9] = (f9, 'The floor beam of the worked example sits at λ = 0.56 on the scale from reinforced concrete (0) to full prestressing (1 and above). At ultimate its four strands supply 71 percent of the tension and the three bars the rest.',
          'A scale of degree of prestressing from 0 to 1.2 with reinforced concrete at 0, the worked-example beam at 0.56 in the partial band and full prestressing from 1. Below, a stacked bar of ultimate steel forces: strands 638.9 kN and bars 262.4 kN.')
