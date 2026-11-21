"""t16 split blueprint thumbnails for Optical Fiber Communication (ec-optical), ECE look.
One spec per lesson, each built from that lesson's own book worked example (books/ece/ec-optical/ec-optical-u<N>.html,
the chapters the lesson covers). Every number on a card, chip, board or summary is computed below and matches the book.
Build: python3 t16_split.py build specs.py <out dir>"""
import math, os, sys

try:
    import t16_split as T
except ImportError:  # run from elsewhere: point T16_TOOL at the folder holding t16_split.py
    sys.path.insert(0, os.environ.get('T16_TOOL', os.path.dirname(os.path.abspath(__file__))))
    import t16_split as T

B = T.B
P, pts, box, cyl, arrow = B.P, B.pts, B.box, T.cyl, T.arrow
D = 'ece'
A, C = T.DEPTS[D]['acc'], T.DEPTS[D]['acc2']          # violet ("gold" class), mint ("cyan" class)
SUBJECT = 'OPTICAL FIBER COMMUNICATION'
HOOK = {'ec-optical-u1-L1': 'Critical angle or acceptance angle?', 'ec-optical-u1-L2': 'Is NA just n₁ minus n₂?',
        'ec-optical-u1-L3': 'Core radius or diameter in V?', 'ec-optical-u1-L4': 'When is a slab guide single-mode?',
        'ec-optical-u2-L1': 'Where does the water peak sit?', 'ec-optical-u2-L2': 'How much loss do four tight turns add?',
        'ec-optical-u2-L3': 'Do material and waveguide D just add?', 'ec-optical-u2-L4': 'Can a short fiber undo 100 km of spread?',
        'ec-optical-u3-L1': "Why can't light alone invert atoms?", 'ec-optical-u3-L2': 'Modal gain or material gain?',
        'ec-optical-u3-L3': 'How much LED power enters a fiber?', 'ec-optical-u3-L4': 'Does gel fix an offset joint?',
        'ec-optical-u4-L1': 'Past cutoff, what is responsivity?', 'ec-optical-u4-L2': 'Does every APD have F = M?',
        'ec-optical-u4-L3': 'Is sensitivity the power of a 1 bit?', 'ec-optical-u5-L1': 'How many splices does 60 km need?',
        'ec-optical-u5-L2': 'Do rise times simply add?', 'ec-optical-u6-L1': 'How wide is a 40-channel WDM comb?',
        'ec-optical-u6-L2': 'Can an EDFA turn all pump into signal?', 'ec-optical-u6-L3': 'How many E1s fit in one STM-1?',
        'ec-optical-u6-L4': 'How many ATM cells for 90 bytes?'}
TOPIC = {'ec-optical-u1-L1': 'Fiber Links & the Acceptance Cone', 'ec-optical-u1-L2': 'Numerical Aperture & Slab Modes',
         'ec-optical-u1-L3': 'Fiber Types, Modes & Two Speeds', 'ec-optical-u1-L4': 'Chip Waveguides & Photonic Crystals',
         'ec-optical-u2-L1': 'Attenuation, Absorption & Scattering', 'ec-optical-u2-L2': 'Bend Loss & Intermodal Dispersion',
         'ec-optical-u2-L3': 'Chromatic & Polarization Mode Dispersion', 'ec-optical-u2-L4': 'Dispersion Compensation & Stimulated Scattering',
         'ec-optical-u3-L1': 'How Atoms & LEDs Make Light', 'ec-optical-u3-L2': 'Laser Threshold & the Laser Diode',
         'ec-optical-u3-L3': 'Quantum-well Lasers & Fiber Coupling', 'ec-optical-u3-L4': 'Fiber Joints & Mach-Zehnder Modulators',
         'ec-optical-u4-L1': 'Photodiodes: from Light to Current', 'ec-optical-u4-L2': 'Avalanche Gain & Receiver Noise',
         'ec-optical-u4-L3': 'Receiver Sensitivity & Bit Error Rate', 'ec-optical-u5-L1': 'Point-to-point Links & the Power Budget',
         'ec-optical-u5-L2': 'Rise Time, Reach & Fiber Tests', 'ec-optical-u6-L1': 'WDM & Passive Optical Devices',
         'ec-optical-u6-L2': 'Optical Amplifiers & Solitons', 'ec-optical-u6-L3': 'Optical Networks & SONET/SDH',
         'ec-optical-u6-L4': 'Optical Nodes, Layers & ATM Cells'}

g = lambda v: f'{v:g}'
f1 = lambda v: f'{v:.1f}'
f2 = lambda v: f'{v:.2f}'
INK, MUTE, GRID = '#E6ECF1', '#C9D3DB', '#6B6F95'
# board materials
GLASS = ('#DCD6FA', '#8C84C4', '#B2AAE6')        # light violet glass/jacket (top, left, right)
METAL = ('#C9CEDB', '#7C8299', '#A2A8BE')
DARK = ('#3A3566', '#1E1A3E', '#2A2552')
CHIP = ('#4B4588', '#24204A', '#332D66')

CSS_TABLE = """
.scope table{border-collapse:collapse;width:100%;margin-top:4px;font:600 17px 'IBM Plex Sans';color:#E6ECF1}
.scope th{font:600 14px 'IBM Plex Sans';color:#C3B8F0;text-align:center;padding:3px 6px;border-bottom:1.5px solid rgba(195,184,255,.3)}
.scope td{text-align:center;padding:2px 6px;border-bottom:1px solid rgba(195,184,255,.16);font-size:17px}
.scope td:first-child{text-align:left}.scope tr:last-child td{border-bottom:none}"""


def setup():
    B.U, B.OX, B.OY = 33, 952, 318


# ---------------------------------------------------------------- card helpers (470 x 144 SVG)
def card(inner, h=144):
    return f'<svg width="470" height="{h}" viewBox="0 0 470 {h}">{inner}</svg>'


def t(x, y, s, cls='ax', fill=None, anchor='middle', extra=''):
    f = f' fill="{fill}"' if fill else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}"{f}{extra}>{s}</text>'


def ln(x0, y0, x1, y1, col=GRID, w=1.5, dash=None, op=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    o = f' stroke-opacity="{op}"' if op else ''
    return f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{col}" stroke-width="{w}"{d}{o}/>'


def poly(ps, col, w=3, fill='none', fop=None, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    fo = f' fill-opacity="{fop}"' if fop is not None else ''
    return f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in ps)}" fill="{fill}"{fo} stroke="{col}" stroke-width="{w}" stroke-linejoin="round"{d}/>'


def dot(x, y, col, r=5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>'


def vbars(x0, w, title, tcol, items, vmax, y_top=34, y_bot=116, vmin=0.0, bw=None):
    """vertical bars in x0..x0+w; items = (label, value, colour, value text)"""
    s = t(x0 + w / 2, 18, title, 'pt', tcol)
    n = len(items); slot = w / n; bw = bw or min(56, slot * .55)
    Y = lambda v: y_bot - (v - vmin) / (vmax - vmin) * (y_bot - y_top)
    s += ln(x0, Y(0), x0 + w, Y(0))
    for i, (lab, v, col, vt) in enumerate(items):
        cx = x0 + slot * (i + .5)
        y0, y1 = sorted((Y(0), Y(v)))
        s += f'<rect x="{cx - bw / 2:.1f}" y="{y0:.1f}" width="{bw:.1f}" height="{max(y1 - y0, 1.5):.1f}" rx="3" fill="{col}" fill-opacity=".85"/>'
        ty = (Y(v) - 6) if v >= 0 else (Y(0) - 6)
        s += t(cx, ty, vt, 'pt', col)
        s += t(cx, 136, lab, 'ax')
    return s


def hbars(x0, x1, rows, vmax, y0=30, rh=26, lw=120):
    """horizontal bars: rows = (label, value, colour, value text); labels right-aligned at x0 + lw - 8"""
    s = ''
    X = lambda v: x0 + lw + v / vmax * (x1 - x0 - lw)
    for i, (lab, v, col, vt) in enumerate(rows):
        y = y0 + i * rh
        s += t(x0 + lw - 8, y + rh / 2 + 4, lab, 'ax', anchor='end')
        s += f'<rect x="{X(0):.1f}" y="{y + 4:.1f}" width="{X(v) - X(0):.1f}" height="{rh - 9}" rx="3" fill="{col}" fill-opacity=".85"/>'
        s += t(X(v) + 6, y + rh / 2 + 5, vt, 'pt', col, 'start')
    return s


# ---------------------------------------------------------------- board helpers
def lab(x, y, z, s, fill=INK, size=15, anchor='middle', dx=0, dy=0):
    px, py = P(x, y, z)
    return (f'<text x="{px + dx:.1f}" y="{py + dy:.1f}" text-anchor="{anchor}" style="font:700 {size}px \'IBM Plex Sans\';letter-spacing:.02em"'
            f' fill="{fill}" stroke="#120F31" stroke-width="3" paint-order="stroke">{s}</text>')


def dev(x, y, w, d, h, mat=METAL, z0=0, label=None, lcol='#17112E', size=14):
    s = box(x, y, w, d, h, *mat, z0=z0)
    if label:
        px, py = P(x + w / 2, y + d / 2, z0 + h)
        s += f'<text x="{px:.1f}" y="{py + 5:.1f}" text-anchor="middle" style="font:700 {size}px \'IBM Plex Sans\'" fill="{lcol}">{label}</text>'
    return s


def tube(a, b, z, w=16, col='#D8D2F7', edge='#6E66A8', core=None, glow=True, cw=3.5):
    """a fiber lying on the board from board point a=(x, y) to b at height z"""
    (x0, y0), (x1, y1) = P(a[0], a[1], z), P(b[0], b[1], z)
    s = (f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{edge}" stroke-width="{w + 4}" stroke-linecap="round"/>'
         f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>')
    if core:
        c = f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{core}" stroke-width="{cw}" stroke-linecap="round"/>'
        s += f'<g filter="url(#gl)">{c}</g>' if glow else c
    return s


def beam(ps, col=C, w=3, op=1):
    return f'<g filter="url(#gl)"><polyline points="{pts(*ps)}" fill="none" stroke="{col}" stroke-width="{w}" stroke-opacity="{op}" stroke-linejoin="round" stroke-linecap="round"/></g>'


def spool(x, y, rx=46, h=40, label=None, sub=None, body='#4F4890', top='#8E86D8', wind=C):
    """an upright fiber reel at board point (x, y): flange, wound fiber band, hub"""
    cx, cy = P(x, y)
    ry = rx * .5
    s = f'<ellipse cx="{cx:.1f}" cy="{cy + 3:.1f}" rx="{rx + 6}" ry="{ry + 4}" fill="#000" opacity=".35"/>'
    s += cyl(cx, cy, rx, ry, 8, '#2A2552', '#5C55A0')                       # bottom flange
    s += cyl(cx, cy - 8, rx * .86, ry * .86, h - 16, body, top)             # wound fibre
    for k in range(1, 4):
        yy = cy - 8 - (h - 16) * k / 4
        s += f'<path d="M{cx - rx * .86:.1f},{yy:.1f} A{rx * .86:.1f},{ry * .86:.1f} 0 0 0 {cx + rx * .86:.1f},{yy:.1f}" fill="none" stroke="{wind}" stroke-opacity=".45" stroke-width="1.5"/>'
    s += cyl(cx, cy - h + 8, rx, ry, 8, '#2A2552', '#6E67B8')               # top flange
    s += f'<ellipse cx="{cx:.1f}" cy="{cy - h:.1f}" rx="{rx * .3:.1f}" ry="{ry * .3:.1f}" fill="#17112E"/>'
    if label:
        s += f'<text x="{cx:.1f}" y="{cy - h - ry - 8:.1f}" text-anchor="middle" style="font:700 15px \'IBM Plex Sans\'" fill="{INK}" stroke="#120F31" stroke-width="3" paint-order="stroke">{label}</text>'
    if sub:
        s += f'<text x="{cx:.1f}" y="{cy + ry + 22:.1f}" text-anchor="middle" style="font:700 14px \'IBM Plex Sans\'" fill="{MUTE}" stroke="#120F31" stroke-width="3" paint-order="stroke">{sub}</text>'
    return s


def board(parts):
    setup()
    return T.iso_board(D, parts)


def mk(key, title, takeaway, card_title, card_html, parts, chips, summary, tag='Book example', css=''):
    return dict(key=key, dept=D, subject=SUBJECT, title=title, question=HOOK[key], takeaway=takeaway, tag=tag,
                card_title=card_title, card=card_html, board=board(parts), chips=chips, summary=summary, css=css,
                page_title=TOPIC[key].replace('&', '&amp;') + ': ECE')


def chip(side, top, kind, text, pointer=True):
    return dict(side=side, top=top, kind=kind, text=text, pointer=pointer)


def gold(s):
    return f'<span class="gold">{s}</span>'


def cyan(s):
    return f'<span class="cyan">{s}</span>'


def deg(r):
    return math.degrees(r)


def face(x, y, z, r, fill, n=36, stroke=None):
    """a circular end face in the plane x = const (it faces +x, so it is seen)"""
    ps = [P(x, y + r * math.cos(2 * math.pi * k / n), z + r * math.sin(2 * math.pi * k / n)) for k in range(n)]
    st = f' stroke="{stroke}" stroke-width="1.5"' if stroke else ''
    return f'<polygon points="{pts(*ps)}" fill="{fill}"{st}/>'


def cone(ax, y, z, x1, half, fill, op=.2, stroke=None):
    """acceptance cone drawn in the x-z plane: apex at (ax, y, z), opening to x1, half-angle `half` in degrees"""
    dz = abs(x1 - ax) * math.tan(math.radians(half))
    tri = [P(x1, y, z + dz), P(ax, y, z), P(x1, y, z - dz)]
    s = f'<polygon points="{pts(*tri)}" fill="{fill}" fill-opacity="{op}"/>'
    if stroke:
        s += f'<polyline points="{pts(*tri)}" fill="none" stroke="{stroke}" stroke-width="2" stroke-dasharray="6 4"/>'
    return s


# ================================================================ unit 1
def u1_l1():
    n1, n2 = 1.50, 1.45
    thc = deg(math.asin(n2 / n1)); NA = math.sqrt(n1 ** 2 - n2 ** 2); tha = deg(math.asin(NA)); thr = deg(math.asin(NA / n1))
    assert (round(thc, 2), round(NA, 4), round(tha, 2), round(thr, 2)) == (75.16, 0.3841, 22.59, 14.84)
    # card: the limiting ray, true angles (book figure 1.2)
    y0, hh, xf = 80, 26, 120
    tr = math.tan(math.radians(thr))
    ray = [(20, y0 - (xf - 20) * math.tan(math.radians(tha))), (xf, y0)]
    x, y, s = xf, y0, 1
    while x < 452:
        ny = y0 + hh * s; nx = x + abs(ny - y) / tr
        if nx > 452:
            ny = y + (452 - x) * tr * (1 if s > 0 else -1); nx = 452
        ray.append((nx, ny)); x, y, s = nx, ny, -s
    w1 = ray[2]
    c = (f'<rect x="{xf}" y="{y0 - hh - 20}" width="{455 - xf}" height="{2 * hh + 40}" fill="{C}" fill-opacity=".10" stroke="{C}" stroke-opacity=".5"/>'
         f'<rect x="{xf}" y="{y0 - hh}" width="{455 - xf}" height="{2 * hh}" fill="{A}" fill-opacity=".16"/>'
         + ln(10, y0, xf, y0, MUTE, 1.2, '5 4') + poly(ray, C, 3.2)
         + f'<path d="M{xf - 46},{y0} A46,46 0 0 1 {xf - 46 * math.cos(math.radians(tha)):.1f},{y0 - 46 * math.sin(math.radians(tha)):.1f}" fill="none" stroke="{C}" stroke-width="2"/>'
         + t(62, y0 + 28, f'θ<tspan baseline-shift="sub" font-size="12">a</tspan> = {f1(tha)}°', 'pt', C)
         + ln(w1[0], w1[1], w1[0], w1[1] - 44, INK, 1.4, '4 3')
         + f'<path d="M{w1[0]},{w1[1] - 30} A30,30 0 0 0 {w1[0] - 30 * math.sin(math.radians(thc)):.1f},{w1[1] - 30 * math.cos(math.radians(thc)):.1f}" fill="none" stroke="{A}" stroke-width="2"/>'
         + t(w1[0] + 74, y0 + hh + 15, f'φ = θ<tspan baseline-shift="sub" font-size="12">c</tspan> = {f1(thc)}°', 'pt', A)
         + t(300, y0 + 20, f'core n₁ = {n1:.2f}', 'ax', INK) + t(300, y0 - hh - 6, f'cladding n₂ = {n2:.2f}', 'ax')
         + t(40, 22, 'air', 'ax'))
    zc, Y = 1.1, 4.2
    zig, x, z, s = [(5.2, zc)], 5.2, zc, -1
    while x > .8:
        nz = zc + .18 * s; nx = x - abs(nz - z) / tr
        if nx < .8:
            nz = z + (x - .8) * tr * s; nx = .8
        zig.append((nx, nz)); x, z, s = nx, nz, -s
    parts = [tube((.6, Y), (5.2, Y), zc, 48, '#B2AAE6', '#5D5596'), tube((.6, Y), (5.2, Y), zc, 18, '#E9E5FF', '#B2AAE6'),
             face(5.2, Y, zc, .74, '#C9C1F4', stroke='#5D5596'), face(5.2, Y, zc, .28, A),
             cone(5.2, Y, zc, 7.9, tha, C, .30, C), face(7.9, Y, zc, 2.7 * math.tan(math.radians(tha)), C, stroke=C).replace('fill="'+C+'"', 'fill="'+C+'" fill-opacity=".16"'),
             beam([P(7.9, Y, zc + 2.7 * math.tan(math.radians(tha))), P(5.2, Y, zc)] + [P(a, Y, b) for a, b in zig], C, 3.4),
             lab(7.0, Y, 0, 'θa', C, 18, dy=-4)]
    chips = [chip('left', 262, 'c', f'n₁ = {n1:.2f}, n₂ = {n2:.2f}'), chip('left', 326, 'c', f'NA = {NA:.3f}'),
             chip('right', 300, 'g', f'θ<sub>a</sub> = {f1(tha)}° at the face'), chip('left', 520, 'g', f'θ<sub>c</sub> = {f1(thc)}° at the wall')]
    summ = (f'sin θ<sub>c</sub> = n₂/n₁ = {n2:.2f}/{n1:.2f} → <b class="gl">θ<sub>c</sub> = {f1(thc)}°</b><br>'
            f'NA = √(n₁² − n₂²) = {NA:.3f} → <b class="cl">θ<sub>a</sub> = {f1(tha)}°</b>')
    return mk('ec-optical-u1-L1', 'Fiber Links &amp;<br>the Acceptance<br>Cone',
              f'θc lives {gold("INSIDE")}, at the wall;<br>θa {cyan("OUTSIDE")}, at the face', 'the limiting ray',
              card(c), parts, chips, summ)


def u1_l2():
    n1, n2 = 1.48, 1.46
    NA = math.sqrt(n1 ** 2 - n2 ** 2); tha = deg(math.asin(NA)); gam = 45
    thas = deg(math.asin(NA / math.cos(math.radians(gam))))
    assert (round(NA, 4), round(tha, 2), round(thas, 2)) == (0.2425, 14.03, 20.06)
    c = (vbars(0, 220, 'NA is not n₁ − n₂', A, [('n₁ − n₂', n1 - n2, C, f'{n1 - n2:.2f}'), ('NA', NA, A, f'{NA:.4f}')], .28)
         + vbars(245, 220, 'acceptance angle', C, [('meridional', tha, C, f'{f1(tha)}°'), ('skew, γ = 45°', thas, A, f'{f1(thas)}°')], 24))
    zc, Y = 1.5, 4.6
    parts = [tube((.6, Y), (4.4, Y), zc, 74, '#B2AAE6', '#5D5596'),
             face(4.4, Y, zc, 1.15, '#C9C1F4', stroke='#5D5596'), face(4.4, Y, zc, .5, A),
             cone(4.4, Y, zc, 8.2, thas, A, .16, A), cone(4.4, Y, zc, 8.2, tha, C, .30, C),
             lab(7.4, Y, zc + 3.8 * math.tan(math.radians(thas)), f'skew {f1(thas)}°', A, 15, dy=-8),
             lab(7.4, Y, zc, f'{f1(tha)}°', C, 15, dy=5),
             face(8.2, Y, zc, 3.8 * math.tan(math.radians(thas)), A, stroke=A).replace('fill="'+A+'"', 'fill="'+A+'" fill-opacity=".12"')]
    chips = [chip('left', 262, 'c', 'n₁ − n₂ = 0.02 ≠ NA'), chip('left', 326, 'g', f'NA = √0.0588 = {NA:.4f}'),
             chip('right', 330, 'c', f'θ<sub>a</sub> = {f1(tha)}°'), chip('right', 500, 'g', f'γ = 45°: {f1(thas)}°', False)]
    summ = (f'n₁² − n₂² = 2.1904 − 2.1316 = 0.0588 → <b class="gl">NA = {NA:.4f}</b><br>'
            f'θ<sub>a</sub> = sin⁻¹ {NA:.4f} = <b class="cl">{f1(tha)}°</b>; skew (γ = 45°): {f1(thas)}°')
    return mk('ec-optical-u1-L2', 'Numerical<br>Aperture &amp;<br>Slab Modes',
              f'NA = {gold("√(n₁² − n₂²)")}:<br>12× the plain {cyan("difference")}', 'n₁ = 1.48, n₂ = 1.46',
              card(c), parts, chips, summ)


def u1_l3():
    a, NA = 4.0, .11
    k = 2 * math.pi * a * NA; lc = k / 2.405; V = k / 1.31
    assert (round(k, 3), round(lc, 3), round(V, 3)) == (2.765, 1.150, 2.110)
    X = lambda l: 50 + (l - 1.0) / .7 * 390
    Yv = lambda v: 118 - (v - 1.4) / 1.6 * 96
    curve = [(X(1 + i * .7 / 40), Yv(k / (1 + i * .7 / 40))) for i in range(41)]
    c = (ln(50, 118, 445, 118) + ln(50, 22, 50, 118)
         + f'<rect x="50" y="22" width="{X(lc) - 50:.1f}" height="96" fill="{A}" fill-opacity=".10"/>'
         + ln(50, Yv(2.405), 445, Yv(2.405), A, 1.8, '6 4') + t(44, Yv(2.405) + 5, '2.405', 'ax', anchor='end')
         + poly(curve, C, 3.4)
         + dot(X(lc), Yv(2.405), A) + t(X(lc) + 10, Yv(2.405) - 12, f'λ<tspan baseline-shift="sub" font-size="12">c</tspan> = {lc:.2f} µm', 'pt', A, 'start')
         + ln(X(1.31), 118, X(1.31), Yv(V), C, 1.6, '4 3') + dot(X(1.31), Yv(V), C)
         + t(X(1.31) + 12, Yv(V) - 12, f'V = {V:.2f} at 1.31 µm', 'pt', C, 'start')
         + t(X(lc) - 8, 112, 'multimode', 'ax', anchor='end') + t(X(lc) + 10, 112, 'single-mode', 'ax', anchor='start')
         + ''.join(t(X(l), 136, g(l), 'ax') for l in (1.0, 1.2, 1.4, 1.6)) + t(445, 136, 'λ, µm', 'ax', anchor='end')
         + t(44, 30, 'V', 'ax', anchor='end'))
    cx, cy = P(4.1, 4.3)
    parts = [f'<ellipse cx="{cx:.1f}" cy="{cy + 6:.1f}" rx="136" ry="70" fill="#000" opacity=".35"/>',
             cyl(cx, cy, 126, 63, 46, '#8C84C4', '#C9C1F4'),
             f'<ellipse cx="{cx:.1f}" cy="{cy - 46:.1f}" rx="50" ry="25" fill="{A}" fill-opacity=".55" stroke="#5D5596" stroke-width="1.5"/>',
             f'<g filter="url(#gl)"><ellipse cx="{cx:.1f}" cy="{cy - 46:.1f}" rx="26" ry="13" fill="{C}"/></g>',
             arrow(cx, cy - 46, cx + 47, cy - 46, '#F7F9FB', 3),
             f'<text x="{cx + 58:.1f}" y="{cy - 40:.1f}" style="font:700 16px \'IBM Plex Sans\'" fill="#F7F9FB" stroke="#120F31" stroke-width="3" paint-order="stroke">a = 4.0 µm</text>',
             f'<text x="{cx:.1f}" y="{cy + 92:.1f}" text-anchor="middle" style="font:700 15px \'IBM Plex Sans\'" fill="{C}" stroke="#120F31" stroke-width="3" paint-order="stroke">LP₀₁ only at 1.31 µm</text>']
    chips = [chip('left', 262, 'g', 'a = 4.0 µm (radius)'), chip('left', 326, 'c', f'NA = {NA}'),
             chip('right', 280, 'g', f'λ<sub>c</sub> = {lc:.2f} µm'), chip('right', 500, 'c', f'V = {V:.2f} &lt; 2.405', False)]
    summ = (f'λ<sub>c</sub> = 2πa·NA/2.405 = {k:.3f}/2.405 = <b class="gl">{lc:.2f} µm</b><br>'
            f'V = {k:.3f}/1.31 = <b class="cl">{V:.2f} &lt; 2.405</b>: single-mode')
    return mk('ec-optical-u1-L3', 'Fiber Types,<br>Modes &amp;<br>Two Speeds',
              f'V takes the {gold("RADIUS")}:<br>{V:.2f} means {cyan("single-mode")}', 'cutoff of a 4.0 µm core',
              card(c), parts, chips, summ)


def u1_l4():
    t_, w, n1, n2, lam = .5, 2, 1.50, 1.45, 1.55
    NA = math.sqrt(n1 ** 2 - n2 ** 2); V = 2 * math.pi * t_ / lam * NA
    ne1 = 1.4564; dl = math.sqrt(ne1 ** 2 - n2 ** 2); Vw = 2 * math.pi * w / lam * dl; wmax = lam / (2 * dl)
    assert (round(NA, 4), round(V, 3), round(Vw, 3), round(wmax, 1)) == (0.3841, 0.778, 1.106, 5.7)
    vmax = 3.6
    x0, lw, x1 = 0, 128, 452
    X = lambda v: x0 + lw + v / vmax * (x1 - x0 - lw)
    c = (hbars(0, 452, [('thickness V', V, A, f'{V:.3f}'), ('width V<tspan baseline-shift="sub" font-size="11">w</tspan>', Vw, C, f'{Vw:.2f}')], vmax, y0=34, rh=34)
         + ln(X(math.pi), 26, X(math.pi), 112, '#FFFFFF', 2, '6 4') + t(X(math.pi) - 8, 128, 'V = π: a 2nd mode', 'pt', INK, 'end')
         + ln(X(0), 30, X(0), 112) + t(X(0) + 4, 18, 'symmetric slab: one mode while V &lt; π', 'ax', anchor='start'))
    parts = [dev(.8, 1.4, 6.4, 5.2, .8, CHIP), dev(.8, 1.4, 6.4, 5.2, .5, ('#5C55A0', '#2A2552', '#3B3478'), z0=.8),
             f'<polygon points="{pts(P(.8, 4, 1.05), P(7.2, 4, 1.05))}" stroke="{C}" stroke-opacity=".35" stroke-width="10"/>',
             f'<g filter="url(#gl)"><polygon points="{pts(P(7.2, 3.4, .87), P(7.2, 4.6, .87), P(7.2, 4.6, 1.17), P(7.2, 3.4, 1.17))}" fill="{C}"/></g>',
             beam([P(7.2, 4, 1.02), P(8.8, 4, 1.02)], C, 5),
             lab(7.2, 5.6, .3, 'w = 2 µm', C, 15, 'start', dx=6, dy=10), lab(7.2, 3.3, 1.0, 't = 0.5 µm', A, 15, 'end', dx=-4, dy=-14),
             lab(3.2, 2.4, 1.3, 'n₁ = 1.50 in n₂ = 1.45', INK, 14)]
    chips = [chip('left', 262, 'g', 't = 0.5 µm, w = 2 µm'), chip('left', 326, 'c', f'NA = {NA:.3f}'),
             chip('right', 280, 'g', f'V = {V:.3f} &lt; π'), chip('right', 470, 'c', f'V<sub>w</sub> = {Vw:.2f} &lt; π', False)]
    summ = (f'V = (2πt/λ)·NA = 2.027 × {NA:.4f} = <b class="gl">{V:.3f}</b> &lt; π<br>'
            f'width: V<sub>w</sub> = 8.107 × 0.1364 = <b class="cl">{Vw:.2f}</b> &lt; π: one mode')
    return mk('ec-optical-u1-L4', 'Waveguides &amp;<br>Photonic<br>Crystals',
              f'A symmetric slab stays<br>single-mode while {gold("V &lt; π")} {cyan("each way")}', 'buried channel at 1.55 µm',
              card(c), parts, chips, summ, tag='Book examples')


def pulse(x, y, z, width, height, col, n=24):
    """a Gaussian pulse standing on the board in the x-z plane, centred at board x; width = 2 sigma in board units"""
    ps = [P(x + (i / n - .5) * width * 3, y, z + height * math.exp(-((i / n - .5) * 3) ** 2 * 2)) for i in range(n + 1)]
    return f'<g filter="url(#gl)"><polyline points="{pts(*ps)}" fill="{col}" fill-opacity=".25" stroke="{col}" stroke-width="3" stroke-linejoin="round"/></g>'


def link(a, b, z=.35, col=C, w=4, op=1):
    return beam([P(a[0], a[1], z), P(b[0], b[1], z)], col, w, op)


# ================================================================ unit 2
def u2_l1():
    old, lwp, L = 1.10, 0.26, 20
    ex = old - lwp; loss = ex * L; kept = 10 ** (-loss / 10); rem = 1 - kept
    assert (round(ex, 2), round(loss, 1), round(kept, 4), round(rem * 100, 1)) == (0.84, 16.8, 0.0209, 97.9)
    x6 = .06
    uv = lambda l: (154.2 * x6 / (46.6 * x6 + 60)) * 1e-2 * math.exp(4.63 / l)
    base = lambda l: .8 / l ** 4 + uv(l) + 7.81e11 * math.exp(-48.48 / l)     # Rayleigh (C = 0.8) + UV + IR tails, l in µm
    assert abs(base(1.383) - lwp) < .005                                      # the low-water-peak fiber's 0.26 dB/km at 1383 nm
    peak = lambda l: (old - base(1.383)) * math.exp(-((l - 1.383) / .012) ** 2 / 2)
    X = lambda nm: 50 + (nm - 1200) / 450 * 395
    Yd = lambda a: 118 - a / 1.25 * 96
    lw = [(X(nm), Yd(base(nm / 1000))) for nm in range(1200, 1651, 5)]
    od = [(X(nm), Yd(base(nm / 1000) + peak(nm / 1000))) for nm in range(1200, 1651, 2)]
    c = (ln(50, 118, 445, 118) + ln(50, 20, 50, 118) + poly(od, A, 3) + poly(lw, C, 3.2)
         + dot(X(1383), Yd(old), A) + t(X(1383) + 10, Yd(old) + 6, f'old cable {old:.2f} dB/km', 'pt', A, 'start')
         + dot(X(1383), Yd(lwp), C) + t(X(1383) + 4, Yd(lwp) + 22, f'low-water-peak {lwp:.2f}', 'pt', C, 'start')
         + ''.join(t(X(nm), 136, str(nm), 'ax') for nm in (1200, 1383, 1550)) + t(445, 136, 'nm', 'ax', anchor='end')
         + t(44, Yd(1) + 5, '1', 'ax', anchor='end') + t(44, 122, '0', 'ax', anchor='end') + t(58, 28, 'dB/km', 'ax', anchor='start'))
    parts = [spool(2.8, 6.4, 50, 52, 'old cable', '20 km'), spool(6.4, 2.8, 50, 52, 'low-water-peak', '20 km'),
             link((4.2, 6.4), (7.0, 6.4), .4, C, 4, .22), link((7.8, 2.8), (8.9, 2.8), .4, C, 6),
             lab(6.4, 6.4, .4, '2.1 % left', MUTE, 14, dy=26)]
    chips = [chip('left', 262, 'g', 'water peak: 1383 nm'), chip('left', 326, 'c', f'{old:.2f} vs {lwp:.2f} dB/km'),
             chip('right', 330, 'g', f'0.84 × 20 = {loss:.1f} dB'), chip('right', 520, 'c', f'{rem * 100:.1f} % removed', False)]
    summ = (f'excess ({old:.2f} − {lwp:.2f}) dB/km × {L} km = <b class="gl">{loss:.1f} dB</b><br>'
            f'kept 10<sup>−1.68</sup> = {kept:.4f} → <b class="cl">{rem * 100:.1f} % removed</b>')
    return mk('ec-optical-u2-L1', 'Attenuation,<br>Absorption &amp;<br>Scattering',
              f'The water peak sits at<br>{gold("1383 nm")}, not at {cyan("1550 nm")}', 'old vs low-water-peak',
              card(c), parts, chips, summ)


def u2_l2():
    al = lambda R: 8 * math.exp(-.6 * R)
    a5, a10, a15 = al(5), al(10), al(15)
    four = 4 * a5; eq_km = four / .2
    assert (round(a5, 3), round(a10, 4), round(four, 2), round(eq_km), round(a15, 5)) == (0.398, 0.0198, 1.59, 8, 0.00099)
    X = lambda R: 50 + (R - 4) / 11 * 190
    Ya = lambda v: 118 - v / .8 * 94
    cur = [(X(4 + i * 11 / 44), Ya(al(4 + i * 11 / 44))) for i in range(45)]
    c = (t(145, 18, 'loss per turn, dB', 'pt', C) + ln(50, 118, 240, 118) + ln(50, 26, 50, 118) + poly(cur, C, 3.2)
         + dot(X(5), Ya(a5), A) + t(X(5) + 10, Ya(a5) + 4, f'{a5:.3f} at 5 mm', 'pt', A, 'start')
         + dot(X(10), Ya(a10), C) + t(X(10), Ya(a10) - 12, f'{a10:.4f}', 'ax', INK)
         + ''.join(t(X(R), 136, str(R), 'ax') for R in (5, 10, 15)) + t(240, 136, 'R, mm', 'ax', anchor='end')
         + vbars(262, 200, 'same loss', A, [('4 turns at 5 mm', four, A, f'{four:.2f} dB'), ('8 km of fiber', 8 * .2, C, f'{8 * .2:.1f} dB')], 2.0))
    cx, cy = P(4.2, 4.0)
    rx, ry, H = 30, 15, 120
    back = front = ''
    for k in range(4):
        yy = cy - 26 - k * 22
        back += f'<path d="M{cx - 44},{yy} A44,22 0 0 1 {cx + 44},{yy}" fill="none" stroke="#B2AAE6" stroke-width="7"/>'
        op = 1 - k * .22
        front += (f'<path d="M{cx - 44},{yy} A44,22 0 0 0 {cx + 44},{yy}" fill="none" stroke="#DCD6FA" stroke-width="7"/>'
                  f'<g filter="url(#gl)"><path d="M{cx - 44},{yy} A44,22 0 0 0 {cx + 44},{yy}" fill="none" stroke="{C}" stroke-opacity="{op:.2f}" stroke-width="2.5"/></g>')
    lin = P(.6, 6.6, .35)
    parts = [f'<ellipse cx="{cx}" cy="{cy + 4}" rx="46" ry="23" fill="#000" opacity=".35"/>', back,
             cyl(cx, cy, rx, ry, H, '#5C55A0', '#8E86D8'), front,
             f'<line x1="{lin[0]:.1f}" y1="{lin[1]:.1f}" x2="{cx - 44}" y2="{cy - 26}" stroke="#DCD6FA" stroke-width="7" stroke-linecap="round"/>',
             beam([lin, (cx - 44, cy - 26)], C, 2.5),
             f'<line x1="{cx + 44}" y1="{cy - 92}" x2="{P(7.6, 1.4, 3.4)[0]:.1f}" y2="{P(7.6, 1.4, 3.4)[1]:.1f}" stroke="#DCD6FA" stroke-width="7" stroke-linecap="round"/>',
             beam([(cx + 44, cy - 92), P(7.6, 1.4, 3.4)], C, 2.5, .35),
             f'<text x="{cx}" y="{cy + 44}" text-anchor="middle" style="font:700 15px \'IBM Plex Sans\'" fill="{INK}" stroke="#120F31" stroke-width="3" paint-order="stroke">R = 5 mm, 4 turns</text>']
    chips = [chip('left', 262, 'c', f'R = 5 mm: {a5:.3f} dB/turn'), chip('left', 326, 'g', f'4 turns: {four:.2f} dB'),
             chip('right', 300, 'c', f'R = 10 mm: {a10:.3f} dB'), chip('right', 500, 'g', '= 8 km of fiber', False)]
    summ = (f'α<sub>r</sub> = 8e<sup>−0.6×5</sup> = 8 × 0.0498 = <b class="cl">{a5:.3f} dB</b> per turn<br>'
            f'4 × {a5:.3f} = <b class="gl">{four:.2f} dB</b>; at R = 10 mm only {a10:.3f} dB')
    return mk('ec-optical-u2-L2', 'Bend Loss &amp;<br>Intermodal<br>Dispersion',
              f'Four tight turns cost<br>{gold("1.6 dB")} = {cyan("8 km")} of fiber', 'α<sub>r</sub> = 8e<sup>−0.6R</sup> dB per turn',
              card(c), parts, chips, summ)


def u2_l3():
    l0, S0, lam, L = 1310, .092, 1550, 80
    Dl = lambda l: S0 / 4 * (l - l0 ** 4 / l ** 3)
    D = Dl(lam); Dw = -3.5; Dm = D - Dw
    dlam = (1.55e-6) ** 2 * 20e9 / 3e8 * 1e9; dtau = round(D, 1) * L * round(dlam, 2)
    assert (round(D, 1), round(Dm, 1), round(dlam, 3), round(dtau)) == (17.5, 21.0, 0.160, 224)
    X = lambda l: 50 + (l - 1200) / 450 * 395
    Yd = lambda v: 112 - (v + 10) / 40 * 92
    tot = [(X(l), Yd(Dl(l))) for l in range(1200, 1651, 10)]
    mat = [(X(l), Yd(Dl(l) - Dw)) for l in range(1200, 1651, 10)]
    wg = [(X(1200), Yd(Dw)), (X(1650), Yd(Dw))]
    c = (ln(50, Yd(0), 445, Yd(0)) + ln(50, 14, 50, 126) + poly(mat, A, 2.6, dash='7 4') + poly(wg, MUTE, 2.6, dash='3 4') + poly(tot, C, 3.4)
         + ln(X(lam), 14, X(lam), 126, '#FFFFFF', 1.2, '3 3', .5)
         + dot(X(lam), Yd(Dm), A) + dot(X(lam), Yd(D), C) + dot(X(lam), Yd(Dw), MUTE)
         + t(140, 18, f'D<tspan baseline-shift="sub" font-size="11">m</tspan> +{Dm:.1f}', 'pt', A, 'start')
         + t(250, 18, f'+ D<tspan baseline-shift="sub" font-size="11">w</tspan> −3.5', 'pt', INK, 'start')
         + t(350, 18, f'= D {D:.1f}', 'pt', C, 'start')
         + ''.join(t(X(l), 138, str(l), 'ax') for l in (1200, 1310)) + t(X(1550) - 30, 138, '1550', 'ax') + t(445, 138, 'nm', 'ax', anchor='end')
         + t(44, Yd(0) + 5, '0', 'ax', anchor='end') + t(44, Yd(20) + 5, '20', 'ax', anchor='end') + t(58, 34, 'ps/(nm·km)', 'ax', anchor='start'))
    parts = [dev(.6, 3.6, 1.5, 1.2, .9, METAL, label='DFB'), link((2.1, 4.2), (3.0, 4.2), .45),
             spool(4.4, 4.2, 58, 58, '80 km', None), link((5.8, 4.2), (7.6, 4.2), .45),
             pulse(2.6, 4.2, .9, .12, 1.6, C), pulse(7.0, 4.2, .9, .5, 1.0, A),
             lab(2.6, 4.2, 2.6, '0.16 nm', C, 14, dy=-4), lab(7.0, 4.2, 2.0, '+224 ps', A, 15, dy=-6)]
    chips = [chip('left', 262, 'g', f'D<sub>m</sub> = +{Dm:.1f}'), chip('left', 326, 'c', 'D<sub>w</sub> = −3.5'),
             chip('right', 280, 'g', f'D = {D:.1f} ps/(nm·km)'), chip('right', 520, 'c', f'0.16 nm × 80 km: {dtau:.0f} ps', False)]
    summ = (f'D = (S₀/4)(λ − λ₀⁴/λ³) = 0.023 × 759.2 = <b class="gl">{D:.1f}</b><br>'
            f'Δτ = {D:.1f} × {L} km × {dlam:.2f} nm = <b class="cl">{dtau:.0f} ps</b>')
    return mk('ec-optical-u2-L3', 'Chromatic<br>Dispersion<br>&amp; PMD',
              f'They add {gold("with signs")}:<br>+21.0 − 3.5 = {cyan("17.5")}', 'D at 1550 nm, 20 GHz DFB',
              card(c, 146), parts, chips, summ)


def u2_l4():
    D1, L1, a1, D2, a2 = 17, 100, .2, -85, .5
    acc = D1 * L1; L2 = acc / -D2; loss = a1 * L1 + a2 * L2; res = acc + D2 * 15; spread = res * .1
    assert (acc, L2, loss, res, spread) == (1700, 20, 30, 425, 42.5)
    X = lambda km: 50 + km / 120 * 390
    Ya = lambda v: 118 - v / 1800 * 92
    c = (ln(50, 118, 445, 118) + ln(50, 20, 50, 118)
         + f'<rect x="{X(100):.1f}" y="20" width="{X(120) - X(100):.1f}" height="98" fill="{A}" fill-opacity=".12"/>'
         + poly([(X(0), Ya(0)), (X(100), Ya(acc)), (X(115), Ya(res))], A, 2.4, dash='6 4')
         + poly([(X(0), Ya(0)), (X(100), Ya(acc)), (X(120), Ya(0))], C, 3.4)
         + dot(X(100), Ya(acc), C) + t(X(100) - 8, Ya(acc) + 4, f'+{acc} ps/nm', 'pt', C, 'end')
         + dot(X(115), Ya(res), A) + t(X(115) - 12, Ya(res) + 6, f'15 km DCF: +{res}', 'ax', A, 'end')
         + t(X(110), 34, 'DCF', 'pt', A) + t(X(50), 104, 'standard fiber', 'ax')
         + ''.join(t(X(k), 136, str(k), 'ax') for k in (0, 50, 100, 120)) + t(445, 118 - 6, 'km', 'ax', anchor='end'))
    parts = [link((.3, 3.0), (1.6, 3.0), .45), spool(3.0, 3.0, 64, 62),
             link((4.4, 3.0), (5.4, 5.2), .45), spool(5.8, 5.6, 36, 40, None, None, body='#6B5FB8', top='#B79CFF', wind='#FFFFFF'),
             link((6.6, 5.6), (8.4, 5.6), .45), lab(5.8, 5.6, 0, '20 km DCF, −85', A, 15, dy=40),
             pulse(.9, 3.0, .9, .12, 1.4, C), pulse(7.6, 5.6, .9, .12, 1.4, C)]
    chips = [chip('left', 262, 'c', f'100 km × 17 = +{acc}'), chip('left', 326, 'g', f'DCF −85 → {L2:g} km'),
             chip('right', 300, 'c', f'span loss {loss:g} dB'), chip('right', 470, 'g', f'15 km: +{res} ps/nm left', False)]
    summ = (f'1700 + (−85)L₂ = 0 → <b class="gl">L₂ = {L2:g} km</b> of DCF<br>'
            f'loss 0.2 × 100 + 0.5 × 20 = <b class="cl">{loss:g} dB</b>')
    return mk('ec-optical-u2-L4', 'Dispersion<br>Compensation<br>&amp; SBS, SRS',
              f'{gold("20 km")} of DCF cancels<br>{cyan("100 km")} of spread', 'dispersion along the span',
              card(c), parts, chips, summ)



def sphere(px, py, r, col='#DCD6FA'):
    return (f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r}" fill="{col}" stroke="#5D5596" stroke-width="1.2"/>'
            f'<circle cx="{px - r * .35:.1f}" cy="{py - r * .35:.1f}" r="{r * .35:.1f}" fill="#FFFFFF" opacity=".7"/>')


def wave(p0, p1, amp=7, waves=4, col=A, w=3):
    (x0, y0), (x1, y1) = p0, p1
    L = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / L, (y1 - y0) / L
    ps = [(x0 + ux * L * k / 60 - uy * amp * math.sin(2 * math.pi * waves * k / 60), y0 + uy * L * k / 60 + ux * amp * math.sin(2 * math.pi * waves * k / 60)) for k in range(61)]
    return beam(ps, col, w)


# ================================================================ unit 3
def u3_l1():
    h, c0, q, k, T_, lam = 6.63e-34, 3.00e8, 1.60e-19, 1.38e-23, 300, 850e-9
    E = h * c0 / lam; EeV = E / q; kT = k * T_; x = E / kT; ratio = math.exp(-x)
    l1 = c0 / (kT * math.log(2) / h)
    assert (round(E * 1e19, 3), round(EeV, 4), round(kT / q, 4), round(x, 2), f'{ratio:.2e}', round(l1 * 1e6)) == (2.34, 1.4625, 0.0259, 56.52, '2.84e-25', 69)
    dots = ''.join(dot(52 + i * 11, 104 - (i % 2) * 9, A, 4.5) for i in range(14))
    c = (ln(40, 40, 206, 40, INK, 2.5) + ln(40, 112, 206, 112, INK, 2.5) + dots
         + t(212, 45, 'E₂', 'pt', INK, 'start') + t(212, 117, 'E₁', 'pt', INK, 'start')
         + t(123, 32, 'N₂ ≈ 0', 'ax', MUTE)
         + arrow(110, 108, 110, 46, C, 3) + t(118, 78, f'hf = {EeV:.2f} eV', 'pt', C, 'start')
         + t(252, 34, 'kT at 300 K = 0.0259 eV', 'ax', MUTE, 'start') + t(252, 62, f'hf/kT = {x:.2f}', 'pt', INK, 'start')
         + t(252, 96, 'N₂/N₁ = 2.84 × 10⁻²⁵', 'pt', A, 'start', ' style="font-size:21px"')
         + t(252, 126, f'R = 1 only near {l1 * 1e6:.0f} µm', 'ax', C, 'start'))
    parts = [dev(.8, .6, 6.6, 2.8, 1.9, CHIP), dev(.8, 3.8, 6.6, 3.6, .3, DARK),
             lab(7.4, 2.0, 1.9, 'E₂ empty', C, 16, 'start', dx=8), lab(7.4, 5.6, .3, 'E₁', INK, 16, 'start', dx=8, dy=8)]
    for i in range(7):
        for j in range(3):
            px, py = P(1.4 + i * .9, 4.4 + j * 1.0, .3)
            parts.append(sphere(px, py - 9, 9))
    parts += [wave(P(-1.2, 1.4, 4.2), P(2.2, 4.6, .9), 7, 5, A, 3), lab(-.4, 2.0, 3.8, '850 nm', A, 15, dy=-10)]
    chips = [chip('left', 262, 'g', f'850 nm: hf = {EeV:.2f} eV'), chip('left', 326, 'c', 'kT = 0.0259 eV'),
             chip('right', 280, 'c', f'hf/kT = {x:.2f}'), chip('right', 500, 'g', 'N₂/N₁ = 2.84 × 10<sup>−25</sup>', False)]
    summ = (f'hf/kT = 2.340 × 10<sup>−19</sup> ÷ 4.14 × 10<sup>−21</sup> = <b class="cl">{x:.2f}</b><br>'
            f'N₂/N₁ = e<sup>−56.52</sup> = <b class="gl">2.84 × 10<sup>−25</sup></b>: pump it')
    return mk('ec-optical-u3-L1', 'How Atoms &amp;<br>LEDs Make<br>Light',
              f'Equilibrium leaves {gold("N₂ ≪ N₁")}:<br>absorption wins, so {cyan("pump")}', '850 nm at 300 K',
              card(c), parts, chips, summ)


def u3_l2():
    L, R, ai, G = .03, .32, 10, .30
    mir = math.log(1 / (R * R)) / (2 * L); modal = ai + mir; mat = modal / G
    dnu = 3e8 / (2 * 3.6 * 300e-6)
    assert (round(mir, 2), round(modal, 2), round(mat, 1), round(dnu / 1e9)) == (37.98, 47.98, 159.9, 139)
    c = (t(235, 18, 'threshold, cm⁻¹', 'pt', C)
         + hbars(0, 400, [('internal α<tspan baseline-shift="sub" font-size="11">i</tspan>', ai, MUTE, f'{ai}'), ('mirror loss', mir, C, f'{mir:.2f}'),
                          ('modal Γg<tspan baseline-shift="sub" font-size="11">th</tspan>', modal, C, f'{modal:.2f}'),
                          ('material g<tspan baseline-shift="sub" font-size="11">th</tspan>', mat, A, f'{mat:.2f}')], 175, y0=28, rh=28, lw=140))
    parts = [dev(1.0, 2.9, 5.8, 2.2, 1.1, CHIP), dev(1.0, 3.75, 5.8, .5, .12, ('#7C73C9', '#3E3680', '#564DA6'), z0=1.1)]
    sw = [P(1.1 + i * 5.6 / 80, 4.0, 1.3 + .22 * math.sin(i / 80 * math.pi * 12)) for i in range(81)]
    parts += [beam(sw, C, 2.4),
              f'<g filter="url(#gl)"><polygon points="{pts(P(6.8, 2.9, 0), P(6.8, 5.1, 0), P(6.8, 5.1, 1.1), P(6.8, 2.9, 1.1))}" fill="{C}" fill-opacity=".28"/></g>',
              beam([P(6.8, 4.0, .7), P(8.9, 4.0, .7)], C, 7),
              lab(3.9, 5.1, 0, 'L = 300 µm', INK, 15, dy=22), lab(6.8, 5.1, 1.1, 'R = 0.32', C, 15, 'start', dx=6, dy=10),
              lab(3.9, 3.0, 1.25, 'Γ = 0.30', A, 15, dy=-8)]
    chips = [chip('left', 262, 'c', 'L = 300 µm, R = 0.32'), chip('left', 326, 'c', f'mirror {mir:.2f} cm<sup>−1</sup>'),
             chip('right', 290, 'g', f'modal Γg = {modal:.2f}'), chip('right', 500, 'g', f'material g = {mat:.2f}', False)]
    summ = (f'Γg<sub>th</sub> = α<sub>i</sub> + mirror = 10 + {mir:.2f} = <b class="cl">{modal:.2f} cm<sup>−1</sup></b><br>'
            f'g<sub>th</sub> = {modal:.2f} ÷ Γ (0.30) = <b class="gl">{mat:.2f} cm<sup>−1</sup></b>')
    return mk('ec-optical-u3-L2', 'Laser<br>Threshold &amp;<br>Laser Diodes',
              f'Modal gain {cyan("48")} ÷ Γ gives<br>material gain {gold("160")} cm⁻¹', 'Fabry-Perot laser, 300 µm',
              card(c), parts, chips, summ)


def u3_l3():
    rs, rc, NA, Ps = 100, 50, .20, 2.0
    area = (rc / rs) ** 2; eta = area * NA ** 2; Pf = eta * Ps
    assert (area, round(eta, 4), round(Pf * 1000, 1)) == (0.25, 0.01, 20.0)
    lg = lambda mw: 118 - (math.log10(mw) + 2) / 2.6 * 92      # 0.01 mW .. 4 mW
    c = (t(95, 18, 'areas', 'pt', A) + f'<circle cx="95" cy="78" r="54" fill="{A}" fill-opacity=".22" stroke="{A}" stroke-width="2"/>'
         + f'<circle cx="95" cy="78" r="27" fill="{C}" fill-opacity=".45" stroke="{C}" stroke-width="2"/>'
         + t(95, 83, 'core', 'ax', INK) + t(95, 46, 'LED', 'ax', INK) + t(95, 142, '(50/100)² = 0.25', 'ax', MUTE)
         + t(330, 18, 'power, log scale', 'pt', C) + ln(210, 118, 450, 118)
         + f'<rect x="232" y="{lg(Ps):.1f}" width="60" height="{118 - lg(Ps):.1f}" rx="3" fill="{A}" fill-opacity=".85"/>' + t(262, lg(Ps) - 6, '2.0 mW', 'pt', A)
         + f'<rect x="380" y="{lg(Pf):.1f}" width="60" height="{118 - lg(Pf):.1f}" rx="3" fill="{C}" fill-opacity=".85"/>' + t(410, lg(Pf) - 6, '20 µW', 'pt', C)
         + arrow(300, 70, 370, 92, INK, 2.5) + t(336, 64, '× 0.01', 'pt', INK) + t(262, 136, 'LED', 'ax') + t(410, 136, 'in the fiber', 'ax'))
    zc, Y = 1.3, 4.2
    parts = [dev(.6, 2.6, 2.0, 3.2, 2.4, METAL), face(2.6, Y, zc, 1.05, A, stroke='#FFFFFF')]
    for ang in (-62, -40, 40, 62):
        a = math.radians(ang)
        parts.append(beam([P(2.6, Y, zc + .5 * math.sin(a)), P(2.6 + 2.4 * math.cos(a), Y, zc + 2.4 * math.sin(a))], A, 2.4, .45))
    parts += [tube((2.6, Y), (8.2, Y), zc, 30, '#B2AAE6', '#5D5596', C, cw=9), face(2.6, Y, zc, .47, C),
              lab(1.6, 2.6, 2.4, 'LED, r = 100 µm', INK, 15, dy=-12), lab(6.8, Y, zc, 'core 50 µm', C, 15, dy=-26)]
    chips = [chip('left', 262, 'c', 'LED r = 100 µm, 2.0 mW'), chip('left', 326, 'c', 'core 50 µm, NA = 0.20'),
             chip('right', 300, 'g', f'η = 0.25 × 0.04 = {eta:g}'), chip('right', 500, 'g', f'P = {Pf * 1000:g} µW', False)]
    summ = (f'η = (r<sub>c</sub>/r<sub>s</sub>)² × NA² = 0.25 × 0.04 = <b class="cl">{eta:g}</b><br>'
            f'P<sub>f</sub> = {eta:g} × {Ps:.1f} mW = <b class="gl">{Pf * 1000:g} µW</b>')
    return mk('ec-optical-u3-L3', 'Quantum-well<br>Lasers &amp;<br>Fiber Coupling',
              f'Only {gold("1 %")} gets in:<br>{cyan("20 µW")} of 2.0 mW', 'Lambertian LED into fiber',
              card(c), parts, chips, summ)


def u3_l4():
    a, d = 50, 10
    x = d / (2 * a); eta = 2 / math.pi * (math.acos(x) - x * math.sqrt(1 - x * x)); Lo = -10 * math.log10(eta)
    Rf = ((1.48 - 1) / (1.48 + 1)) ** 2; Lf = 2 * -10 * math.log10(1 - Rf)
    assert (round(eta, 4), round(Lo, 2), round(Lf, 2)) == (0.8729, 0.59, 0.33)
    c = (t(90, 18, 'cores 10 µm apart', 'pt', C)
         + f'<circle cx="84" cy="78" r="50" fill="{A}" fill-opacity=".18" stroke="{A}" stroke-width="2"/>'
         + f'<circle cx="94" cy="78" r="50" fill="{C}" fill-opacity=".18" stroke="{C}" stroke-width="2"/>'
         + t(89, 83, f'η = {eta:.4f}', 'pt', INK) + t(90, 142, 'd/2a = 0.1', 'ax', MUTE)
         + vbars(190, 275, 'loss, dB', A, [('offset', Lo, A, f'{Lo:.2f}'), ('+ gel', Lo, A, f'{Lo:.2f}'),
                                            ('Fresnel', Lf, C, f'{Lf:.2f}'), ('+ gel', 0, C, '0')], .7, bw=40))
    zc = 1.0
    parts = [tube((.4, 3.8), (4.0, 3.8), zc, 34, '#B2AAE6', '#5D5596', C, cw=11), face(4.0, 3.8, zc, .52, '#C9C1F4', stroke='#5D5596'),
             face(4.0, 3.8, zc, .2, C), tube((4.08, 4.55), (7.9, 4.55), zc, 34, '#B2AAE6', '#5D5596', C, cw=11),
             f'<ellipse cx="{P(4.04, 4.17, zc)[0]:.1f}" cy="{P(4.04, 4.17, zc)[1]:.1f}" rx="34" ry="30" fill="{C}" fill-opacity=".22" stroke="{C}" stroke-opacity=".6" stroke-dasharray="4 3"/>',
             lab(4.0, 4.05, zc, 'gel', C, 15, dy=-38), lab(4.4, 4.6, 0, 'offset d = 10 µm', INK, 15, dy=26)]
    chips = [chip('left', 262, 'c', 'a = 50 µm, d = 10 µm'), chip('left', 326, 'c', 'd/2a = 0.1'),
             chip('right', 300, 'g', f'η = {eta:.4f}'), chip('right', 500, 'g', f'offset loss {Lo:.2f} dB', False)]
    summ = (f'η = (2/π)[arccos 0.1 − 0.1√0.99] = <b class="cl">{eta:.4f}</b><br>'
            f'L = −10 log {eta:.4f} = <b class="gl">{Lo:.2f} dB</b>, with gel or not')
    return mk('ec-optical-u3-L4', 'Fiber Joints &amp;<br>Mach-Zehnder<br>Modulators',
              f'Gel removes {gold("reflection")},<br>not the {cyan("offset")}', 'offset joint, gel or not',
              card(c), parts, chips, summ, tag='Book examples')



def row_x(i, n, x0=-2.6, x1=2.6):
    """positions along the board's horizontal diagonal (page-horizontal row through the board centre)"""
    u = x0 + (x1 - x0) * i / (n - 1)
    return 4 + u, 4 - u


# ================================================================ unit 4
def u4_l1():
    Ip, Pin, lam, Eg = .90, 1.0, 1.55, .75
    R = Ip / Pin; eta = 1.24 * R / lam; lc = 1.24 / Eg; E17 = 1.24 / 1.70
    assert (R, round(eta, 2), round(lc, 2), round(E17, 2)) == (0.9, 0.72, 1.65, 0.73)
    X = lambda l: 50 + (l - 1.0) / .8 * 390
    Yr = lambda r: 118 - r / 1.2 * 92
    ideal = [(X(1.0), Yr(1 / 1.24)), (X(lc), Yr(lc / 1.24))]
    real = [(X(1.0), Yr(eta / 1.24)), (X(lc), Yr(eta * lc / 1.24)), (X(lc), Yr(0)), (X(1.8), Yr(0))]
    c = (ln(50, 118, 445, 118) + ln(50, 20, 50, 118) + poly(ideal, MUTE, 2, dash='6 4') + t(X(1.12), Yr(1.12 / 1.24) - 10, 'η = 1', 'ax', MUTE)
         + poly(real, C, 3.4) + ln(X(lc), 20, X(lc), 118, A, 1.5, '4 3')
         + t(X(lc) - 6, 110, f'λ<tspan baseline-shift="sub" font-size="11">c</tspan> = {lc:.2f} µm', 'pt', A, 'end')
         + dot(X(1.55), Yr(R), C) + t(X(1.55) - 10, Yr(R) + 42, f'{R:.2f} A/W at 1.55 µm', 'pt', C, 'end')
         + dot(X(1.70), Yr(0), A) + t(X(1.70), 108, 'R = 0', 'pt', A)
         + ''.join(t(X(l), 136, g(l), 'ax') for l in (1.0, 1.2, 1.4, 1.6)) + t(445, 136, 'λ, µm', 'ax', anchor='end')
         + t(58, 28, 'R, A/W', 'ax', anchor='start') + t(44, Yr(1) + 5, '1', 'ax', anchor='end'))
    cx, cy = P(3.4, 4.6)
    parts = [f'<ellipse cx="{cx:.1f}" cy="{cy + 4:.1f}" rx="62" ry="31" fill="#000" opacity=".35"/>',
             cyl(cx, cy, 54, 27, 56, '#A2A8BE', '#DDE1EA'),
             f'<ellipse cx="{cx:.1f}" cy="{cy - 56:.1f}" rx="30" ry="15" fill="#17112E"/>',
             f'<g filter="url(#gl)"><ellipse cx="{cx:.1f}" cy="{cy - 56:.1f}" rx="16" ry="8" fill="{C}"/></g>',
             beam([(cx + 110, cy - 236), (cx + 4, cy - 58)], C, 5),              f'<text x="{cx + 116:.1f}" y="{cy - 244:.1f}" style="font:700 15px \'IBM Plex Sans\'" fill="{C}" stroke="#120F31" stroke-width="3" paint-order="stroke">1.55 µm</text>',
             f'<path d="M{cx + 54},{cy - 20} C{cx + 110},{cy - 10} {P(6.2, 3.0, .6)[0]:.1f},{P(6.2, 3.0, .6)[1] + 30:.1f} {P(6.0, 3.4, .6)[0]:.1f},{P(6.0, 3.4, .6)[1]:.1f}" fill="none" stroke="#E8B84A" stroke-width="3"/>',
             dev(5.6, 2.4, 1.6, 1.4, 1.0, DARK), lab(6.4, 3.1, 1.0, '0.90 µA', C, 16, dy=6),
             lab(3.4, 4.6, 0, 'InGaAs, E<tspan baseline-shift="sub" font-size="11">g</tspan> = 0.75 eV', INK, 14, dy=50)]
    chips = [chip('left', 262, 'c', '1.0 µW → 0.90 µA'), chip('left', 326, 'c', f'R = {R:.2f} A/W, η = {eta:.2f}'),
             chip('right', 290, 'g', f'λ<sub>c</sub> = 1.24/0.75 = {lc:.2f} µm'), chip('right', 520, 'g', '1.70 µm: R = 0', False)]
    summ = (f'η = 1.24R/λ = 1.24 × 0.90/1.55 = <b class="cl">{eta:.2f}</b><br>'
            f'λ<sub>c</sub> = {lc:.2f} µm, so at 1.70 µm (0.73 eV) <b class="gl">R = 0</b>')
    return mk('ec-optical-u4-L1', 'Photodiodes:<br>from Light<br>to Current',
              f'Past {gold("1.65 µm")} the diode<br>sees {cyan("nothing")}: R = 0', 'InGaAs photodiode',
              card(c), parts, chips, summ)


def u4_l2():
    q, kB, T_, RL, B_ = 1.602e-19, 1.38e-23, 300, 1000, 1e9
    eta, lam, M, k, P_ = .8, 1.3, 10, .3, 100e-9
    R = eta * lam / 1.24; Ip = R * P_
    F = lambda m: k * m + (1 - k) * (2 - 1 / m)
    th = 4 * kB * T_ * B_ / RL
    snr = lambda m: (m * Ip) ** 2 / (2 * q * Ip * m * m * F(m) * B_ + th)
    s10, s1, s16 = (10 * math.log10(snr(m)) for m in (M, 1, 16))
    assert (round(Ip * 1e9, 1), round(F(M), 2), round(s10, 1), round(s1, 1), round(s16, 1)) == (83.9, 4.33, 14.0, -3.7, 14.9)
    X = lambda m: 50 + (m - 1) / 19 * 170
    Yf = lambda f: 118 - f / 20 * 92
    c = (t(135, 18, 'excess noise F', 'pt', C) + ln(50, 118, 222, 118) + ln(50, 26, 50, 118)
         + poly([(X(1), Yf(1)), (X(20), Yf(20))], MUTE, 2, dash='6 4') + t(X(13), Yf(17), 'F = M (k = 1)', 'ax', MUTE, 'end')
         + poly([(X(1 + i * 19 / 38), Yf(F(1 + i * 19 / 38))) for i in range(39)], C, 3.2)
         + dot(X(10), Yf(F(10)), A) + t(X(10) + 6, Yf(F(10)) + 20, f'{F(10):.2f} at M = 10', 'pt', A, 'start')
         + ''.join(t(X(m), 136, str(m), 'ax') for m in (1, 10)) + t(X(20), 136, 'M = 20', 'ax')
         + vbars(245, 220, 'SNR, dB', A, [('PIN', s1, MUTE, f'{s1:.1f}'.replace('-', '−')), ('APD, M = 10', s10, A, f'{s10:.1f}'), ('M = 16', s16, C, f'{s16:.1f}')],
                 16, y_top=34, y_bot=118, vmin=-5))
    layers = [('n⁺', .0, .35, '#7C73C9'), ('p gain', .35, .55, '#B79CFF'), ('π absorb', .9, .9, '#4B4588'), ('p⁺', 1.8, .3, '#7C73C9')]
    parts = []
    for name, z0, h, col in layers:
        parts.append(box(1.6, 2.4, 4.4, 3.4, h, col, '#1E1A3E', '#2A2552', z0=z0))
        parts.append(lab(6.0, 4.1, z0 + h / 2, name, INK, 14, 'start', dx=8, dy=6))
    parts.append(wave(P(1.2, -.4, 4.6), P(3.8, 4.1, 2.1), 7, 5, A, 3))
    ox, oy = P(3.8, 5.8, .62)
    tree = ''
    for lvl in range(3):
        for j in range(2 ** lvl):
            x0 = ox - 36 + (j + .5) * 72 / 2 ** lvl; y0 = oy - 8 + lvl * 9
            tree += dot(x0, y0, C, 3.2)
    parts += [f'<g filter="url(#gl)">{tree}</g>', lab(3.8, 5.8, 0, 'M = 10, k = 0.3', C, 15, dy=28)]
    chips = [chip('left', 262, 'c', 'M = 10, k = 0.3'), chip('left', 326, 'g', f'F = {F(M):.2f}, not 10'),
             chip('right', 300, 'c', f'I<sub>M</sub> = {M * Ip * 1e9:.0f} nA'), chip('right', 520, 'g', f'SNR {s10:.1f} vs {s1:.1f} dB'.replace('-', '−'), False)]
    summ = (f'F = kM + (1 − k)(2 − 1/M) = 3 + 1.33 = <b class="gl">{F(M):.2f}</b><br>'
            f'SNR = 25.0 = <b class="cl">{s10:.1f} dB</b>; the PIN gets {s1:.1f} dB'.replace('-', '−'))
    return mk('ec-optical-u4-L2', 'Avalanche<br>Gain &amp;<br>Receiver Noise',
              f'F = M only if {gold("k = 1")};<br>here F is just {cyan("4.33")}', 'InGaAs APD at M = 10',
              card(c), parts, chips, summ)


def u4_l3():
    Q, sig, R, loss = 6, 40e-9, .9, 30
    Ps = Q * sig / R; dbm = 10 * math.log10(Ps / 1e-3); I1 = 2 * Q * sig; launch = dbm + loss
    assert (round(Ps * 1e9), round(dbm, 1), round(I1 * 1e9), round(launch, 1)) == (267, -35.7, 480, -5.7)
    Yi = lambda i: 112 - i / 520 * 86
    bits = [1, 0, 1, 1, 0, 1]
    tr = []
    for n, b in enumerate(bits):
        for k in range(9):
            nz = 22 * math.sin(n * 7.1 + k * 2.3) * math.cos(k * 1.7 + n)        # fixed wiggle standing for the noise
            tr.append((40 + n * 30 + k * 30 / 8, Yi(b * 480) + nz * .35))
    gx = lambda i: 270 + i / 520 * 180
    gs = lambda mu: [(gx(mu + (j / 30 - .5) * 8 * 40), 116 - 70 * math.exp(-((j / 30 - .5) * 8) ** 2 / 2)) for j in range(31)]
    c = (t(120, 18, 'bits at the decision', 'pt', C) + ln(36, Yi(0), 226, Yi(0), MUTE, 1) + ln(36, Yi(480), 226, Yi(480), MUTE, 1)
         + poly(tr, C, 2.4) + ln(36, Yi(240), 226, Yi(240), A, 1.8, '6 4')
         + t(230, Yi(480) + 4, '480', 'ax', anchor='start') + t(230, Yi(240) + 4, '240', 'ax', A, 'start') + t(230, Yi(0) + 4, '0 nA', 'ax', anchor='start')
         + t(360, 18, 'σ = 40 nA each side', 'pt', A) + poly(gs(0), C, 2.6, fill=C, fop=.18) + poly(gs(480), C, 2.6, fill=C, fop=.18)
         + ln(gx(240), 26, gx(240), 118, A, 2, '6 4') + ln(gx(-30), 118, gx(520), 118, MUTE, 1)
         + t(gx(120), 60, '6σ', 'pt', INK) + t(gx(360), 60, '6σ', 'pt', INK)
         + t(gx(0), 136, '0', 'ax') + t(gx(240), 136, '240', 'ax', A) + t(gx(480), 136, '480 nA', 'ax'))
    a, b_ = row_x(0, 4, -3.0, 2.6), row_x(1, 4, -3.0, 2.6)
    cx, cy = P(*row_x(1, 4, -3.0, 2.6))
    parts = [tube(row_x(0, 4, -4.4, 2.6), b_, .45, 16, '#B2AAE6', '#5D5596')]
    for n, bt in enumerate(bits):
        if bt:
            p0 = P(*row_x(n, 12, -4.2, -2.4), .45)
            parts.append(f'<g filter="url(#gl)"><circle cx="{p0[0]:.1f}" cy="{p0[1]:.1f}" r="6" fill="{C}"/></g>')
    parts += [cyl(cx, cy, 30, 15, 40, '#A2A8BE', '#DDE1EA'), f'<ellipse cx="{cx:.1f}" cy="{cy - 40:.1f}" rx="12" ry="6" fill="{C}"/>']
    for i, (lb, mat) in enumerate((('amp', DARK), ('decide', CHIP))):
        x, y = row_x(2 + i, 4, -3.0, 2.6)
        parts.append(link((x - 1.6, y + 1.6), (x - .5, y + .5), .45, '#E8B84A', 3))
        parts.append(dev(x - .55, y - .55, 1.1, 1.1, .9, mat, label=None))
        parts.append(lab(x, y, .9, lb, INK, 14, dy=-6))
    parts.append(lab(*row_x(3, 4, -3.0, 2.6), 0, 'threshold 240 nA', A, 15, dy=50))
    chips = [chip('left', 262, 'c', f'R = {R} A/W, σ = 40 nA'), chip('left', 326, 'c', 'Q = 6 for BER 10<sup>−9</sup>'),
             chip('right', 280, 'g', f'P<sub>sens</sub> = {Ps * 1e9:.0f} nW'), chip('right', 520, 'g', f'one level {I1 * 1e9:.0f} nA', False)]
    summ = (f'P<sub>sens</sub> = Qσ/R = 6 × 40 nA ÷ 0.9 = <b class="gl">{Ps * 1e9:.0f} nW</b><br>'
            f'= {dbm:.1f} dBm average; a 1 needs <b class="cl">I₁ = 2Qσ = {I1 * 1e9:.0f} nA</b>')
    return mk('ec-optical-u4-L3', 'Receiver<br>Sensitivity &amp;<br>Bit Error Rate',
              f'Sensitivity is the {gold("average")};<br>a 1 bit needs {cyan("twice")} it', 'PIN receiver at Q = 6',
              card(c), parts, chips, summ)


# ================================================================ unit 5
def u5_l1():
    L, reel, a, sp, cn, Pt, Ps, mar = 60, 10, .22, .1, .5, 0, -28, 6
    reels = L // reel; ns = reels - 1
    fib = a * L; loss = fib + 2 * cn + ns * sp; Pr = Pt - loss; spare = (Pt - Ps) - (loss + mar)
    assert (reels, ns, round(fib, 1), round(loss, 1), round(spare, 1)) == (6, 5, 13.2, 14.7, 7.3)
    X = lambda km: 50 + km / 60 * 380
    Yp = lambda dbm: 24 + -dbm / 30 * 96
    path, p = [(X(0), Yp(0)), (X(0), Yp(-cn))], -cn
    for r in range(reels):
        p -= a * reel; path.append((X((r + 1) * reel), Yp(p)))
        if r < reels - 1:
            p -= sp; path.append((X((r + 1) * reel), Yp(p)))
    p -= cn; path.append((X(L), Yp(p)))
    assert round(p, 1) == round(Pr, 1)
    c = (ln(50, 24, 50, 120) + ln(50, Yp(-28), 440, Yp(-28), A, 2, '6 4') + t(440, Yp(-28) - 6, 'sensitivity −28 dBm', 'ax', A, 'end')
         + ln(50, Yp(-22), 440, Yp(-22), MUTE, 1.5, '3 4') + t(440, Yp(-22) - 6, '+ 6 dB margin', 'ax', MUTE, 'end')
         + poly(path, C, 3.2) + dot(X(L), Yp(Pr), C) + t(X(L) - 6, Yp(Pr) - 10, f'{Pr:.1f} dBm', 'pt', C, 'end')
         + ''.join(dot(X(k), Yp(-cn - a * k - sp * (k // 10 - 1) - sp), '#FFFFFF', 3) for k in range(10, 60, 10))
         + ''.join(t(X(k), 140, str(k), 'ax') for k in (0, 20, 40, 60)) + t(440, 140, 'km', 'ax', anchor='end')
         + t(44, Yp(0) + 5, '0', 'ax', anchor='end') + t(44, Yp(-20) + 5, '−20', 'ax', anchor='end') + t(58, 18, 'dBm', 'ax', anchor='start'))
    parts = []
    xs = [row_x(i, 6, -2.4, 2.4) for i in range(6)]
    parts.append(dev(*[v - .45 for v in row_x(0, 2, -3.7, 3.7)], .9, .9, .9, METAL, label='Tx'))
    parts.append(link(row_x(0, 2, -3.5, 3.7), xs[0], .3, C, 3))
    for i, (x, y) in enumerate(xs):
        if i:
            parts.append(link(xs[i - 1], (x, y), .3, C, 3))
            mx, my = P((x + xs[i - 1][0]) / 2, (y + xs[i - 1][1]) / 2, .3)
            parts.append(f'<g filter="url(#gl)"><circle cx="{mx:.1f}" cy="{my:.1f}" r="5.5" fill="#FFFFFF"/></g>')
    for i, (x, y) in enumerate(xs):
        parts.append(spool(x, y, 22, 26, None, None))
    parts.append(link(xs[-1], row_x(1, 2, -3.7, 3.5), .3, C, 3))
    parts.append(dev(*[v - .45 for v in row_x(1, 2, -3.7, 3.7)], .9, .9, .9, METAL, label='Rx'))
    parts.append(lab(4, 4, 0, '6 reels of 10 km, 5 splices (white)', INK, 14, dy=40))
    chips = [chip('left', 262, 'c', '60 km in 10 km reels'), chip('left', 326, 'g', '6 reels → 5 splices'),
             chip('right', 290, 'c', f'loss {loss:.1f} dB'), chip('right', 520, 'g', f'spare {spare:.1f} dB', False)]
    summ = (f'13.2 + 2 × 0.5 + 5 × 0.1 = <b class="cl">{loss:.1f} dB</b> → {Pr:.1f} dBm<br>'
            f'28 − ({loss:.1f} + 6) = <b class="gl">{spare:.1f} dB</b> spare: it closes')
    return mk('ec-optical-u5-L1', 'Point-to-point<br>Links &amp; the<br>Power Budget',
              f'6 reels need {gold("5")} splices;<br>the two ends are {cyan("connectors")}', '2.5 Gbit/s over 60 km',
              card(c), parts, chips, summ)


def u5_l2():
    ttx, D_, L, dl, B0, qq, Brx, Tb = 12, .090, 5, 40, 500, .7, 30, 50
    tch = D_ * L * dl; tmod = 440 * L ** qq / B0; trx = 350 / Brx
    tsys = math.sqrt(ttx ** 2 + tmod ** 2 + tch ** 2 + trx ** 2); lim = .7 * Tb; nrz = .7 / tsys * 1e3; simple = ttx + tmod + tch + trx
    assert (round(tch, 1), round(tmod, 2), round(trx, 2), round(tsys, 1), round(nrz, 1), round(simple, 1)) == (18.0, 2.71, 11.67, 24.7, 28.3, 44.4)
    items = [('t<tspan baseline-shift="sub" font-size="11">tx</tspan>', ttx, MUTE, '12'), ('t<tspan baseline-shift="sub" font-size="11">mod</tspan>', tmod, MUTE, f'{tmod:.2f}'),
             ('t<tspan baseline-shift="sub" font-size="11">chrom</tspan>', tch, MUTE, f'{tch:.1f}'), ('t<tspan baseline-shift="sub" font-size="11">rx</tspan>', trx, MUTE, f'{trx:.2f}'),
             ('√Σt²', tsys, C, f'{tsys:.1f}'), ('plain sum', simple, A, f'{simple:.1f}')]
    Y = lambda v: 118 - v / 50 * 90
    c = (vbars(0, 460, 'rise times, ns', C, items, 50, y_top=28, bw=40)
         + ln(10, Y(lim), 460, Y(lim), '#FFFFFF', 1.8, '6 4') + t(12, Y(lim) - 6, 'limit 0.7 T<tspan baseline-shift="sub" font-size="11">b</tspan> = 35', 'ax', INK, 'start'))
    pos = [row_x(i, 3, -2.5, 2.5) for i in range(3)]
    parts = [link(pos[0], pos[1], .35), link(pos[1], pos[2], .35),
             dev(pos[0][0] - .55, pos[0][1] - .55, 1.1, 1.1, .9, METAL, label='LED'), spool(*pos[1], 52, 50, None, None),
             dev(pos[2][0] - .55, pos[2][1] - .55, 1.1, 1.1, .9, DARK)]
    for (x, y), tt, col, zt in ((pos[0], '12 ns', MUTE, 2.4), (pos[1], '18.0 ns', MUTE, 3.4), (pos[2], '11.67 ns', MUTE, 2.4)):
        bx, by = P(x, y, zt)
        parts.append(poly([(bx - 26, by + 14), (bx - 10, by + 14), (bx + 10, by - 14), (bx + 26, by - 14)], C, 3))
        parts.append(f'<text x="{bx:.1f}" y="{by - 22:.1f}" text-anchor="middle" style="font:700 14px \'IBM Plex Sans\'" fill="{INK}" stroke="#120F31" stroke-width="3" paint-order="stroke">{tt}</text>')
    parts.append(lab(*pos[1], 0, '5 km graded-index, 850 nm', INK, 14, dy=46))
    chips = [chip('left', 262, 'c', 't<sub>tx</sub> 12, t<sub>rx</sub> 11.67 ns'), chip('left', 326, 'c', f't<sub>chrom</sub> = {tch:.1f} ns'),
             chip('right', 280, 'g', f'not {simple:.1f} ns'), chip('right', 520, 'g', f't<sub>sys</sub> = {tsys:.1f} ns ≤ 35', False)]
    summ = (f't<sub>sys</sub> = √(12² + 2.71² + 18.0² + 11.67²) = <b class="cl">{tsys:.1f} ns</b><br>'
            f'≤ 35 ns: passes; NRZ up to <b class="gl">{nrz:.1f} Mbit/s</b>')
    return mk('ec-optical-u5-L2', 'Rise Time,<br>Reach &amp;<br>Fiber Tests',
              f'Rise times add as {gold("squares")},<br>then take the {cyan("root")}', '20 Mbit/s LED link, 5 km',
              card(c), parts, chips, summ)



# ================================================================ unit 6
def u6_l1():
    N, Bc, df, lam, c0 = 40, 10, 100e9, 1550e-9, 3e8
    cap = N * Bc; dl = lam ** 2 * df / c0 * 1e9; wTHz = (N - 1) * df / 1e12; wnm = (N - 1) * dl
    f1_, f2_ = c0 / 1530e-9 / 1e12, c0 / 1565e-9 / 1e12; band = f1_ - f2_; slots = int(round(band, 3) / .1)
    assert (cap, round(dl, 4), round(wTHz, 1), round(wnm, 2), round(band, 3), slots, slots * Bc) == (400, 0.8008, 3.9, 31.23, 4.385, 43, 430)
    X = lambda nm: 30 + (nm - 1525) / 45 * 420
    st = 1547.5 - wnm / 2
    comb = ''.join(ln(X(st + k * dl), 98, X(st + k * dl), 40 if k % 13 else 32, C if k % 2 else A, 2.2) for k in range(N))
    c = (f'<rect x="{X(1530):.1f}" y="26" width="{X(1565) - X(1530):.1f}" height="84" fill="{A}" fill-opacity=".10" stroke="{A}" stroke-opacity=".4"/>'
         + t(X(1530) + 6, 22, f'C-band 1530 to 1565 nm: {slots} slots of 100 GHz', 'ax', A, 'start')
         + comb + ln(20, 98, 455, 98, MUTE, 1.2)
         + ln(X(st), 112, X(st + wnm), 112, INK, 2) + ln(X(st), 106, X(st), 118, INK, 2) + ln(X(st + wnm), 106, X(st + wnm), 118, INK, 2)
         + t(X(1547.5), 134, f'39 gaps × {dl:.4f} nm = {wnm:.2f} nm', 'pt', INK)
         + t(X(1530), 124, '1530', 'ax') + t(X(1565), 124, '1565', 'ax'))
    parts = []
    for k in range(N):
        y = .7 + k * 6.6 / (N - 1)
        col = C if k % 2 else A
        parts.append(f'<polyline points="{pts(P(.1, y, .7), P(1.6, y, .7), P(3.0, 3.6 + (y - 4) * .15, .7))}" fill="none" stroke="{col}" stroke-width="1.6" stroke-opacity=".85"/>')
    parts += [dev(3.0, 2.8, 1.8, 2.4, 1.4, METAL, label='MUX', size=16), tube((4.8, 4.0), (8.4, 4.0), .7, 18, '#B2AAE6', '#5D5596', C, cw=6),
              lab(.6, 7.4, .7, '40 channels', INK, 15, dy=26), lab(7.2, 4.0, .7, '400 Gb/s', C, 15, dy=-22)]
    chips = [chip('left', 262, 'c', f'40 × 10 Gb/s = {cap} Gb/s'), chip('left', 326, 'c', f'100 GHz = {dl:.2f} nm'),
             chip('right', 290, 'g', '39 gaps, not 40'), chip('right', 520, 'g', f'width {wnm:.2f} nm', False)]
    summ = (f'Δλ = λ²Δf/c = <b class="cl">{dl:.4f} nm</b> per 100 GHz<br>'
            f'39 × 100 GHz = <b class="gl">{wTHz:.1f} THz</b> = 39 × {dl:.4f} = {wnm:.2f} nm')
    return mk('ec-optical-u6-L1', 'WDM &amp;<br>Passive Optical<br>Devices',
              f'40 channels have {gold("39 gaps")}:<br>the comb is {cyan("31.23 nm")} wide', '40 channels at 100 GHz',
              card(c), parts, chips, summ)


def u6_l2():
    Pp, lp, Pin, Pout, ls = 60, 980, .5, 25, 1550
    G = 10 * math.log10(Pout / Pin); pce = (Pout - Pin) / Pp; qce = pce * ls / lp
    pmax = Pin + lp / ls * Pp; gmax = 10 * math.log10(pmax / Pin)
    assert (round(G, 2), round(pce * 100, 1), round(qce * 100, 1), round(pmax, 2), round(gmax, 2)) == (16.99, 40.8, 64.6, 38.44, 18.86)
    c = (vbars(0, 250, 'power, mW', C, [('pump in', Pp, A, f'{Pp}'), ('most out', pmax, MUTE, f'{pmax:.2f}'), ('signal out', Pout, C, f'{Pout}')], 66, bw=46)
         + t(268, 40, 'λ<tspan baseline-shift="sub" font-size="11">p</tspan>/λ<tspan baseline-shift="sub" font-size="11">s</tspan> = 980/1550 = 0.632', 'pt', INK, 'start')
         + t(268, 70, f'PCE = 24.5/60 = {pce * 100:.1f} %', 'pt', C, 'start')
         + t(268, 100, f'QCE = {qce * 100:.1f} %', 'pt', A, 'start') + t(268, 128, f'gain {G:.2f} dB, max {gmax:.2f}', 'ax', MUTE, 'start'))
    parts = [dev(.6, 1.0, 1.6, 1.3, 1.0, METAL, label='980 nm'), dev(2.9, 3.4, 1.0, 1.0, .7, DARK),
             link((1.4, 2.3), (3.4, 3.4), .45, A, 4), link((.2, 3.9), (2.9, 3.9), .45, C, 3),
             spool(5.4, 3.9, 60, 56, None, None, body='#6B5FB8', top='#B79CFF', wind=C), link((3.9, 3.9), (4.4, 3.9), .45, C, 4),
             link((6.5, 3.9), (8.6, 3.9), .45, C, 8),
             lab(1.4, 1.6, 1.0, '60 mW pump', A, 15, dy=-30), lab(.6, 3.9, .45, '0.5 mW', C, 15, dy=26),
             lab(7.8, 3.9, .45, '25 mW', C, 16, dy=-22), lab(5.4, 3.9, 0, 'erbium fiber', INK, 14, dy=46)]
    chips = [chip('left', 262, 'c', 'pump 60 mW at 980 nm'), chip('left', 326, 'c', '0.5 mW in → 25 mW out'),
             chip('right', 300, 'g', f'PCE {pce * 100:.1f} %'), chip('right', 520, 'g', f'max {pmax:.2f} mW', False)]
    summ = (f'P<sub>out</sub> ≤ 0.5 + (980/1550) × 60 = <b class="gl">{pmax:.2f} mW</b><br>'
            f'measured 25 mW: PCE <b class="cl">{pce * 100:.1f} %</b>, QCE {qce * 100:.1f} %')
    return mk('ec-optical-u6-L2', 'Optical<br>Amplifiers &amp;<br>Solitons',
              f'A 980 nm pump photon gives<br>at most {gold("63 %")} of its {cyan("energy")}', 'EDFA pumped at 980 nm',
              card(c), parts, chips, summ)


def u6_l3():
    cols, rows, fps = 270, 9, 8000
    stm1 = cols * rows * 8 * fps / 1e6; e1 = 3 * 7 * 3; e1r = e1 * 2.048; naive = stm1 / 2.048
    assert (stm1, e1, round(e1r, 3), round(naive, 1)) == (155.52, 63, 129.024, 75.9)
    fx, fw = 20, 200
    grid = ''.join(ln(fx, 30 + r * 10, fx + fw, 30 + r * 10, A, 1, op=.3) for r in range(10))
    c = (t(fx + fw / 2, 18, 'STM-1 frame, 125 µs', 'pt', A) + grid
         + f'<rect x="{fx}" y="30" width="{fw}" height="90" fill="{A}" fill-opacity=".12" stroke="{A}" stroke-opacity=".6"/>'
         + f'<rect x="{fx}" y="30" width="{fw * 9 / 270:.1f}" height="90" fill="{C}" fill-opacity=".8"/>'
         + t(fx + fw / 2 + 4, 80, '261 columns of payload', 'ax', INK) + t(fx + fw / 2, 138, '9 rows × 270 columns', 'ax', MUTE)
         + vbars(250, 215, 'E1s in one STM-1', C, [('155.52 ÷ 2.048', naive, A, f'{naive:.1f} ✗'.replace(' ✗', '')), ('3 × 7 × 3', e1, C, f'{e1}')], 85, bw=52))
    cubes = sorted(((i, j, k) for i in range(3) for j in range(7) for k in range(3)), key=lambda v: (v[2], v[0] + v[1]))
    parts = []
    for i, j, k in cubes:
        top = C if k == 2 else '#8E86D8'
        parts.append(box(2.6 + i * .78, 1.3 + j * .78, .66, .66, .62, top, '#2A2552', '#4B4588', z0=k * .74))
    parts += [lab(2.6, 7.0, 0, '3 × 7 × 3 = 63 TU-12s', INK, 15, 'end', dx=-10, dy=10)]
    chips = [chip('left', 262, 'c', f'STM-1 = {stm1:.2f} Mb/s'), chip('left', 326, 'g', f'not {naive:.1f} E1s'),
             chip('right', 290, 'c', '3 × 7 × 3 = 63 E1s'), chip('right', 520, 'g', f'63 × 2.048 = {e1r:.3f}', False)]
    summ = (f'270 × 9 × 8 × 8000 = <b class="cl">{stm1:.2f} Mb/s</b> = 3 × STS-1<br>'
            f'3 × 7 × 3 = <b class="gl">63 E1s</b> = {e1r:.3f} Mb/s')
    return mk('ec-optical-u6-L3', 'Optical<br>Networks &amp;<br>SONET/SDH',
              f'Not 75: only {gold("63")} E1s fit,<br>each in a {cyan("TU-12")}', 'STM-1 and its E1s',
              card(c), parts, chips, summ)


def u6_l4():
    data, trl, pay, cell = 1500, 8, 48, 53
    n = math.ceil((data + trl) / pay); pad = n * pay - (data + trl); link_ = n * cell; eff = data / link_
    us = link_ * 8 / 149.76e6 * 1e6; small = math.ceil((90 + trl) / pay)
    assert (n, pad, link_, round(eff * 100, 1), round(us, 1), small) == (32, 28, 1696, 88.4, 90.6, 3)
    rows_ = [('data + trailer', f'{data} + {trl} = {data + trl} bytes'), ('cells', f'⌈{data + trl}/48⌉ = <b style="color:{C}">{n}</b>'),
             ('pad', f'{n * pay} − {data + trl} = {pad} bytes'), ('on the link', f'{n} × 53 = {link_} bytes'),
             ('efficiency', f'{data}/{link_} = <b style="color:{A}">{eff * 100:.1f} %</b>')]
    tbl = '<table>' + ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in rows_) + '</table>'
    parts = []
    for r in range(4):
        for q in range(8):
            x, y = .5 + q * .9, 1.0 + r * 1.55
            last = (r == 3 and q == 7)
            parts.append(box(x, y, .74, 1.15, .32, '#8E86D8', '#2A2552', '#4B4588'))
            parts.append(box(x, y, .74, 1.15 * 5 / 53, .34, A, '#3E3680', '#564DA6'))
            if last:
                parts.append(box(x, y + 1.15 * (5 + 48 - 28 - 8) / 53, .74, 1.15 * 28 / 53, .34, '#5E5A78', '#2A2552', '#3B3478'))
                parts.append(box(x, y + 1.15 * 45 / 53, .74, 1.15 * 8 / 53, .34, C, '#1E7F70', '#2BAA95'))
    parts += [lab(7.0, 6.2, .4, 'pad + trailer', C, 14, 'start', dx=14, dy=26), lab(4.0, 7.6, 0, '32 cells × 53 bytes', INK, 15, 'end', dx=-20, dy=24)]
    chips = [chip('left', 262, 'c', f'{data} + {trl} = {data + trl} bytes'), chip('left', 326, 'g', f'⌈{data + trl}/48⌉ = {n} cells'),
             chip('right', 290, 'c', f'pad {pad} bytes'), chip('right', 520, 'g', '90 B: 90 + 8 = 98 → 3 cells', False)]
    summ = (f'{n} cells × 53 = <b class="cl">{link_} bytes</b> on the link<br>'
            f'efficiency {data}/{link_} = <b class="gl">{eff * 100:.1f} %</b>, {us:.1f} µs on STM-1')
    return mk('ec-optical-u6-L4', 'Optical Nodes,<br>Layers &amp;<br>ATM Cells',
              f'Add the {gold("8-byte trailer")}<br>before you divide by {cyan("48")}', '1500 bytes on AAL5',
              tbl, parts, chips, summ, css=CSS_TABLE)


def specs():
    return [u1_l1(), u1_l2(), u1_l3(), u1_l4(), u2_l1(), u2_l2(), u2_l3(), u2_l4(), u3_l1(), u3_l2(), u3_l3(), u3_l4(),
            u4_l1(), u4_l2(), u4_l3(), u5_l1(), u5_l2(), u6_l1(), u6_l2(), u6_l3(), u6_l4()]
