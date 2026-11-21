"""t16 split-blueprint thumbnails for Machine Design (me-design), Mech look.
One spec per lesson, each built from a worked example in that lesson's own chapters of
books/mech/me-design/me-design-u<N>.html (main). Every number shown is computed below and matches the book's answer.
Build: python3 t16_split.py build specs.py <out dir>   (run from the tool folder, so t16_split is importable)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t16_split as T
B = T.B
arrow = T.arrow

D = 'mech'
ACC, ACC2 = T.DEPTS[D]['acc'], T.DEPTS[D]['acc2']          # orange, ice blue
SUBJ = 'MACHINE DESIGN'
ORIGIN = (952, 340)                                         # board top corner, as in the approved Mech sample
INK, MUTE, AXC = '#E6ECF1', '#9FB0BF', '#6B7B8A'

TABLE_CSS = """
table{border-collapse:collapse;width:100%;margin-top:6px;font:600 17px 'IBM Plex Sans';color:#E6ECF1}
th{font:600 14px 'IBM Plex Sans';color:#9FB0BF;text-align:center;padding:4px 6px;border-bottom:1.5px solid #3A4A58}
td{text-align:center;padding:6px 6px;border-bottom:1px solid #2A3844;font-size:18px}
td:first-child{text-align:left;font-size:17px;font-weight:700}
tr:last-child td{border-bottom:none}"""


def f(v, n=2):
    """fixed decimals, thin-space thousands like the book (12 732)"""
    s = f'{v:,.{n}f}'
    return s.replace(',', ' ') if abs(v) >= 10000 else s.replace(',', '')


def P(x, y, z=0):
    return B.P(x, y, z)


def pts(*p):
    return B.pts(*p)


def setup():
    B.U, (B.OX, B.OY) = 33, ORIGIN


# ---------------------------------------------------------------- board helpers
GID = [0]
TONES = {  # dark edge, highlight, mid, cap
    'steel': ('#56626E', '#EEF2F5', '#B7C2CC', '#D3DAE1'),
    'dark': ('#1E252C', '#6E7B88', '#3E4954', '#56626E'),
    'orange': ('#8A4A1E', '#FFD0AA', '#FF9E5A', '#FFB988'),
    'blue': ('#2C5A80', '#D6EEFF', '#7CC4FF', '#A9D9FF'),
    'bronze': ('#6B4A22', '#F1CF9C', '#C08A4B', '#DDB179'),
    'iron': ('#3A444E', '#AEB9C4', '#7D8994', '#97A3AE'),
}


def hull(points):
    p = sorted(set((round(a, 2), round(b, 2)) for a, b in points))
    if len(p) < 3:
        return p
    def cr(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for q in p:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], q) <= 0: lo.pop()
        lo.append(q)
    for q in reversed(p):
        while len(up) >= 2 and cr(up[-2], up[-1], q) <= 0: up.pop()
        up.append(q)
    return lo[:-1] + up[:-1]


def pt3(axis, t, c, r, a):
    """a point on the circle of radius r at angle a, at position t along the axis, centred at c (the other two coords)"""
    u, v = c[0] + r * math.cos(a), c[1] + r * math.sin(a)
    return {'x': (t, u, v), 'y': (u, t, v), 'z': (u, v, t)}[axis]


def outline(axis, t, c, r, n=72, prof=None):
    return [P(*pt3(axis, t, c, r * (prof(2 * math.pi * i / n) if prof else 1), 2 * math.pi * i / n)) for i in range(n)]


def grad(p0, p1, tone):
    GID[0] += 1
    gid = f'cg{GID[0]}'
    d, l, m, _ = TONES[tone]
    return gid, (f'<defs><linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{p0[0]:.1f}" y1="{p0[1]:.1f}" x2="{p1[0]:.1f}" y2="{p1[1]:.1f}">'
                 f'<stop offset="0" stop-color="{d}"/><stop offset=".38" stop-color="{l}"/><stop offset=".62" stop-color="{m}"/><stop offset="1" stop-color="{d}"/></linearGradient></defs>')


def cylinder(axis, t0, t1, c, r, tone='steel', hole=0, prof=None, cap=None, stroke=None):
    """a solid (or hollow, hole = inner radius) cylinder along axis from t0 to t1; the t1 end faces the viewer"""
    nn = 480 if prof else 72                                   # enough points to resolve every tooth
    a0, a1 = outline(axis, t0, c, r, prof=prof, n=nn), outline(axis, t1, c, r, prof=prof, n=nn)
    ca, cb = P(*pt3(axis, t0, c, 0, 0)), P(*pt3(axis, t1, c, 0, 0))
    dx, dy = cb[0] - ca[0], cb[1] - ca[1]
    L = math.hypot(dx, dy)
    nx, ny = (-dy / L, dx / L) if L > .5 else (1, 0)
    rs = max(abs((q[0] - cb[0]) * nx + (q[1] - cb[1]) * ny) for q in a1)
    gid, gdef = grad((cb[0] - nx * rs, cb[1] - ny * rs), (cb[0] + nx * rs, cb[1] + ny * rs), tone)
    capc = cap or TONES[tone][3]
    sk = f' stroke="{stroke}" stroke-width="1.2"' if stroke else ''
    o = [gdef]
    if prof:   # toothed: stack slices so the teeth show on the side
        k = max(2, int(L / 1.6))
        for i in range(k):
            t = t0 + (t1 - t0) * i / k
            o.append(f'<polygon points="{pts(*outline(axis, t, c, r, prof=prof, n=nn))}" fill="url(#{gid})"/>')
    else:
        o.append(f'<polygon points="{pts(*hull(a0 + a1))}" fill="url(#{gid})"/>')
    if hole:
        o.append(f'<path d="M{pts(*a1)}Z M{pts(*outline(axis, t1, c, hole))}Z" fill="{capc}" fill-rule="evenodd"{sk}/>')
        o.append(f'<polygon points="{pts(*outline(axis, t1, c, hole))}" fill="{TONES["dark"][0]}"/>')
    else:
        o.append(f'<polygon points="{pts(*a1)}" fill="{capc}"{sk}/>')
    return ''.join(o)


def box(x, y, w, d, h, tone='steel', z0=0):
    dk, l, m, c = TONES[tone]
    return B.box(x, y, w, d, h, c, dk, m, z0)


def ring_on(axis, t, c, r, col, w=3, dash=None, op=1):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polygon points="{pts(*outline(axis, t, c, r))}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"{da}/>'


def helix(xc, yc, z0, z1, r, turns, w, col, back='#3E4954', n=40, hand=1):
    """an upright coil spring; returns (back half, front half) so other parts can sit between them"""
    bk, fr = [], []
    N = int(turns * n)
    for i in range(N):
        a, b = hand * 2 * math.pi * i / n, hand * 2 * math.pi * (i + 1) / n
        p0 = P(xc + r * math.cos(a), yc + r * math.sin(a), z0 + (z1 - z0) * i / N)
        p1 = P(xc + r * math.cos(b), yc + r * math.sin(b), z0 + (z1 - z0) * (i + 1) / N)
        front = math.cos((a + b) / 2) + math.sin((a + b) / 2) > 0
        seg = f'<line x1="{p0[0]:.1f}" y1="{p0[1]:.1f}" x2="{p1[0]:.1f}" y2="{p1[1]:.1f}" stroke="{col if front else back}" stroke-width="{w}" stroke-linecap="round"/>'
        (fr if front else bk).append(seg)
    return ''.join(bk), ''.join(fr)


def lab(x, y, z, text, col=INK, size=16, anchor='middle', dx=0, dy=0):
    px, py = P(x, y, z)
    return (f'<text x="{px + dx:.1f}" y="{py + dy:.1f}" text-anchor="{anchor}" style="font:700 {size}px \'IBM Plex Sans\';paint-order:stroke;'
            f'stroke:#0B1D21;stroke-width:4px;stroke-linejoin:round" fill="{col}">{text}</text>')


def arr3(p0, p1, col, w=6, glow=False):
    a = arrow(*P(*p0), *P(*p1), col, w)
    return f'<g filter="url(#gl)">{a}</g>' if glow else a


def slab_dressing():
    """the approved Mech sample's board: grey plate with a faint grid and four screws"""
    s = ['<defs><linearGradient id="pl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3B4652"/><stop offset="1" stop-color="#252E37"/></linearGradient></defs>']
    g = []
    for k in range(1, 8):
        g.append(f'<polyline points="{pts(P(k, 0), P(k, 8))}"/><polyline points="{pts(P(0, k), P(8, k))}"/>')
    s.append(f'<g fill="none" stroke="{ACC2}" stroke-opacity=".14" stroke-width="1.2">{"".join(g)}</g>')
    for a, b in ((.4, .4), (7.6, .4), (.4, 7.6), (7.6, 7.6)):
        x, y = P(a, b)
        s.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="7" ry="4" fill="#5B6774" stroke="#12171C" stroke-width="1.5"/><path d="M{x - 4:.1f},{y:.1f}H{x + 4:.1f}" stroke="#12171C" stroke-width="1.5"/>')
    return ''.join(s)


def board(parts):
    setup()
    return T.iso_board(D, [slab_dressing()] + parts, top='url(#pl)', left='#161C22', right='#1C232A', origin=ORIGIN)


# ---------------------------------------------------------------- card helpers (470 x 144 SVG)
def svg(inner):
    return f'<svg width="470" height="144" viewBox="0 0 470 144">{inner}</svg>'


def t_(x, y, s, cls='ax', col=None, anchor='start', size=None, weight=None):
    st = []
    if size: st.append(f'font-size:{size}px')
    if weight: st.append(f'font-weight:{weight}')
    sty = f' style="{";".join(st)}"' if st else ''
    fill = f' fill="{col}"' if col else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}"{fill}{sty}>{s}</text>'


def hbars(items, x0, x1, y0, step, vmax, bh=20, limit=None, lw=None, vx=None):
    """horizontal bars: items = (label, value, colour, value text); limit = (value, text) draws a dashed line"""
    o = []
    for i, (lb, v, col, vt) in enumerate(items):
        y = y0 + i * step
        w = (x1 - x0) * v / vmax
        o.append(t_(x0 - 10, y + bh / 2 + 5, lb, 'ax', INK, 'end', 15, 600))
        o.append(f'<rect x="{x0}" y="{y}" width="{w:.1f}" height="{bh}" rx="4" fill="{col}" fill-opacity=".85"/>')
        o.append(t_(vx, y + bh / 2 + 6, vt, 'pt', col, 'end') if vx else t_(x0 + w + 8, y + bh / 2 + 6, vt, 'pt', col))
    if limit:
        lx = x0 + (x1 - x0) * limit[0] / vmax
        yb = y0 + (len(items) - 1) * step + bh + 6
        o.append(f'<line x1="{lx:.1f}" y1="{y0 - 6}" x2="{lx:.1f}" y2="{yb}" stroke="{INK}" stroke-width="2" stroke-dasharray="5 4"/>')
        o.append(t_(lx, yb + 14, limit[1], 'ax', INK, 'middle'))
    return ''.join(o)


def spec(key, title, hook, take, card_title, card, parts, chips, summary, css='', tsize=None):
    if tsize:
        css += f'h1{{font-size:{tsize}px !important}}'
    assert len(card_title.replace('&amp;', '&')) <= 30 or '<' in card_title, (key, card_title)
    return dict(key=key, dept=D, subject=SUBJ, title=title, question=hook, takeaway=take, tag='Book example',
                card_title=card_title, card=card, board=board(parts), chips=chips, summary=summary,
                css=TABLE_CSS + '.sh{white-space:nowrap}' + css, page_title=title.replace('<br>', ' ') + ': Machine Design')


def ch(side, top, kind, text, pointer=True):
    return dict(side=side, top=top, kind=kind, text=text, pointer=pointer)


def g_(s): return f'<span class="gold">{s}</span>'
def c_(s): return f'<span class="cyan">{s}</span>'
def gl(s): return f'<b class="gl">{s}</b>'
def cl(s): return f'<b class="cl">{s}</b>'


# ================================================================ unit 1
def u1_L1():
    """1.2 worked example: tie rod 500 mm, 20 kN, n = 2 on yield, stretch <= 0.6 mm, three materials"""
    F, L, n, dl = 20_000, 500, 2, .6
    mats = [('mild steel', 250, 200_000, 7850, 60, 'iron'), ('Al 6061-T6', 276, 69_000, 2700, 300, 'steel'), ('alloy steel', 650, 200_000, 7850, 120, 'orange')]
    rows = []
    for name, syt, E, rho, cost, tone in mats:
        a_s = n * F / syt
        a_k = F * L / (dl * E)
        a = max(a_s, a_k)
        m = rho * a * 1e-6 * L / 1000
        rows.append(dict(name=name, a_s=a_s, a_k=a_k, a=a, m=m, c=m * cost, tone=tone, E=E))
    ms, al, qt = rows
    assert (f(ms['a_s'], 1), f(al['a_s'], 1), f(qt['a_s'], 1)) == ('160.0', '144.9', '61.5')
    assert (f(qt['a_k'], 1), f(al['a_k'], 1)) == ('83.3', '241.5') and f(qt['m'], 3) == '0.327'
    # board: the three rods standing side by side, each sized to its governing area, pulled upward
    o = []
    short = {'mild steel': 'mild steel', 'Al 6061-T6': 'Al 6061', 'alloy steel': 'alloy steel'}
    for (x, y), r in zip(((2.65, 5.0), (4.35, 3.3), (6.05, 1.6)), rows):
        rad = math.sqrt(4 * r['a'] / math.pi) * .065
        o.append(cylinder('z', 0, .35, (x, y), rad + .35, 'dark'))
        o.append(cylinder('z', .35, 3.6, (x, y), rad, r['tone']))
        o.append(arr3((x, y, 3.75), (x, y, 5.0), ACC if r['tone'] == 'orange' else ACC2, 6, r['tone'] == 'orange'))
        o.append(lab(x, y + rad + .4, 0, short[r['name']], ACC if r['tone'] == 'orange' else INK, 16, dy=26))
    # card: area needed for strength and for stiffness, per material
    vmax, y0, h = 250, 116, 72
    s = [f'<line x1="40" y1="{y0}" x2="456" y2="{y0}" stroke="{AXC}" stroke-width="1.5"/>']
    for i, r in enumerate(rows):
        gx = 70 + i * 140
        for j, (key, col) in enumerate((('a_s', ACC), ('a_k', ACC2))):
            v = r[key]; bh = h * v / vmax; x = gx + j * 46
            gov = abs(v - r['a']) < 1e-9
            s.append(f'<rect x="{x}" y="{y0 - bh:.1f}" width="38" height="{bh:.1f}" rx="3" fill="{col}" fill-opacity="{.9 if gov else .35}"/>')
            s.append(t_(x + 19, y0 - bh - 6, f(v, 1), 'ax', col if gov else MUTE, 'middle', 13, 700 if gov else 500))
        s.append(t_(gx + 42, 134, r['name'], 'ax', INK, 'middle', 14, 600))
    s.append(f'<rect x="40" y="6" width="12" height="12" rx="2" fill="{ACC}"/><rect x="134" y="6" width="12" height="12" rx="2" fill="{ACC2}"/>'
             + t_(58, 17, 'strength', 'ax', ACC, 'start', 13, 700) + t_(152, 17, 'stiffness   (area needed, mm²)', 'ax', ACC2, 'start', 13, 700))
    card = svg(''.join(s))
    return spec('me-design-u1-L1', 'Design Process,<br>Materials<br>&amp; Fits', 'Does heat treatment cut deflection?',
                f'Heat treatment lifts {g_("STRENGTH")}<br>not {c_("STIFFNESS")}: E stays 200 GPa',
                'one tie rod, three materials', card, o,
                [ch('left', 300, 'g', 'F = 20 kN, n = 2'), ch('left', 364, 'c', 'stretch ≤ 0.6 mm'),
                 ch('left', 500, 'c', 'both steels: E = 200 GPa'), ch('right', 500, 'g', f"alloy steel: {f(qt['a_k'], 1)} mm²")],
                f"Alloy steel: strength {cl(f(qt['a_s'], 1) + ' mm²')}, stiffness {gl(f(qt['a_k'], 1) + ' mm²')}<br>"
                f"Same E = 200 GPa as mild steel, so same δ check", tsize=66)


def u1_L2():
    """1.4 worked example: steel tie 250 mm2, 45 kN, Syt 280 MPa, n = 2.5"""
    F, A, syt, n = 45_000, 250, 280, 2.5
    allow = syt / n; sig = F / A; n_act = syt / sig
    A_req = F / allow; d_req = math.sqrt(4 * A_req / math.pi)
    bars = {d: math.pi * d * d / 4 for d in (20, 22, 25)}
    s25 = F / bars[25]; n25 = syt / s25
    assert (f(allow, 0), f(sig, 0), f(n_act, 2), f(A_req, 1), f(d_req, 1), f(s25, 1), f(n25, 2)) == ('112', '180', '1.56', '401.8', '22.6', '91.7', '3.05')
    o = [box(.6, 1.5, .7, 1.2, .9, 'dark'), box(6.9, 1.5, .7, 1.2, .9, 'dark'),
         cylinder('x', 1.0, 7.2, (2.1, .55), .42, 'iron'),
         arr3((7.25, 2.1, .55), (8.3, 2.1, .55), ACC, 6, True), arr3((.95, 2.1, .55), (-.1, 2.1, .55), ACC, 6, True),
         lab(4.1, 2.1, 1.25, '250 mm² tie: 180 MPa', ACC, 15)]
    for x, d in ((3.3, 20), (4.6, 22), (5.9, 25)):
        o.append(cylinder('z', 0, 1.5, (x, 5.4), d * .03, 'orange' if d == 25 else 'steel'))
        o.append(lab(x, 5.4 + d * .03, 0, f'Ø{d}', ACC if d == 25 else INK, 15, dy=24))
    s = hbars([('S<tspan dy="4" font-size="11">yt</tspan>', syt, ACC2, f'{syt} MPa'), ('working', sig, ACC, f'{f(sig, 0)} MPa'),
               ('allowable', allow, ACC2, f'{f(allow, 0)} MPa'), ('Ø25 bar', s25, ACC, f'{f(s25, 1)} MPa')], 120, 380, 8, 33, syt, 22)
    card = svg(s)
    return spec('me-design-u1-L2', 'Factor of<br>Safety, Loads<br>&amp; Stresses', 'Is n = 2.5 a 250 % margin?',
                f'n = 2.5 is a {g_("150 %")} margin,<br>not {c_("250 %")}: margin = n − 1',
                'steel tie on one stress scale', card, o,
                [ch('left', 300, 'g', 'F = 45 kN'), ch('left', 364, 'c', 'S<sub>yt</sub> = 280 MPa'),
                 ch('right', 300, 'g', 'n = 280/180 = 1.56'), ch('right', 500, 'c', f'Ø25: n = {f(n25, 2)}', False)],
                f"σ<sub>allow</sub> = 280/2.5 = {cl('112 MPa')}; σ = {gl('180 MPa')}<br>"
                f"Unsafe: need {f(A_req, 1)} mm² → Ø25 bar, {f(s25, 1)} MPa")


def u1_L3():
    """1.9 worked example: crane hook 20 kN, 30 x 60 section, inner radius 40 mm"""
    Pn, b, h, ri = 20_000, 30, 60, 40
    ro = ri + h; A = b * h; R = ri + h / 2
    Rn = h / math.log(ro / ri); e = R - Rn
    M = Pn * R; pa = Pn / A
    si = M * (Rn - ri) / (A * e * ri); so = -M * (ro - Rn) / (A * e * ro)
    Z = b * h * h / 6; sb = M / Z
    inner, outer, straight = pa + si, pa + so, pa + sb
    assert (f(Rn, 2), f(e, 2), f(inner, 1), f(so, 1), f(outer, 1), f(sb, 1), f(straight, 1)) == ('65.48', '4.52', '120.8', '-59.4', '-48.3', '77.8', '88.9')
    # board: the hook, extruded; scale 1 unit = 45 mm
    sc = 36.0
    Ri, Ro = ri / sc, ro / sc
    xc, zc, y0, th = 5.0, 3.0, 2.9, b / sc

    def ringpoly(y):
        a = [math.radians(d) for d in range(90, 371, 5)]
        outer_ = [(xc + Ro * math.cos(t), y, zc + Ro * math.sin(t)) for t in a]
        inner_ = [(xc + Ri * math.cos(t), y, zc + Ri * math.sin(t)) for t in reversed(a)]
        return [P(*q) for q in outer_ + inner_]

    def shank(y):
        return [P(xc - .45, y, zc + Ri), P(xc + .45, y, zc + Ri), P(xc + .45, y, zc + Ro + .9), P(xc - .45, y, zc + Ro + .9)]
    o = []
    k = 16
    for i in range(k + 1):
        y = y0 + th * i / k
        last = i == k
        for poly in (shank(y), ringpoly(y)):
            o.append(f'<polygon points="{pts(*poly)}" fill="{"#D3DAE1" if last else "#6E7B88"}"{" stroke=\"#8E9AA6\" stroke-width=\"1.5\"" if last else ""}/>')
    o.append(cylinder('z', zc + Ro + .9, zc + Ro + 1.15, (xc, y0 + th / 2), .6, 'dark'))
    # critical section: horizontal through the centre, on the back of the hook (left side)
    yf = y0 + th
    pi_, po_ = P(xc - Ri, yf, zc), P(xc - Ro, yf, zc)
    o.append(f'<line x1="{pi_[0]:.1f}" y1="{pi_[1]:.1f}" x2="{po_[0]:.1f}" y2="{po_[1]:.1f}" stroke="{INK}" stroke-width="2.5" stroke-dasharray="6 4"/>')
    o.append(f'<circle cx="{pi_[0]:.1f}" cy="{pi_[1]:.1f}" r="7" fill="{ACC}"/><circle cx="{po_[0]:.1f}" cy="{po_[1]:.1f}" r="7" fill="{ACC2}"/>')
    o.append(arr3((xc, yf + .2, zc - Ri + 1.4), (xc, yf + .2, zc - Ri + .05), ACC, 7, True))
    o.append(lab(xc, yf + .2, zc - Ri + .7, '20 kN', ACC, 16, 'start', dx=16))
    # card: stress across the section, curved against straight-beam theory
    X = lambda r: 60 + (r - ri) / h * 300
    Y = lambda s_: 82 - s_ * .58
    cur = ' '.join(f'{X(r):.1f},{Y(pa + M * (Rn - r) / (A * e * r)):.1f}' for r in [ri + h * i / 40 for i in range(41)])
    stl = f'{X(ri):.1f},{Y(straight):.1f} {X(ro):.1f},{Y(pa - sb):.1f}'
    s = (f'<line x1="{X(ri)}" y1="{Y(0)}" x2="{X(ro)}" y2="{Y(0)}" stroke="{AXC}" stroke-width="1.5"/>'
         f'<line x1="{X(ri)}" y1="6" x2="{X(ri)}" y2="128" stroke="{AXC}" stroke-width="1.5"/>'
         f'<polyline points="{stl}" fill="none" stroke="{ACC2}" stroke-width="3" stroke-dasharray="8 6"/>'
         f'<polyline points="{cur}" fill="none" stroke="{ACC}" stroke-width="3.5"/>'
         f'<circle cx="{X(ri)}" cy="{Y(inner):.1f}" r="5" fill="{ACC}"/><circle cx="{X(ro)}" cy="{Y(outer):.1f}" r="5" fill="{ACC}"/>'
         + t_(X(ri) + 12, Y(inner) + 4, f'inner fibre {f(inner, 1)} MPa', 'pt', ACC)
         + t_(X(ri) + 12, 112, f'straight beam: {f(straight, 1)}', 'pt', ACC2)
         + t_(X(ro) + 10, Y(outer) - 4, 'outer', 'pt', ACC) + t_(X(ro) + 10, Y(outer) + 15, f(outer, 1), 'pt', ACC)
         + t_(X(ri) - 6, Y(0) + 5, '0', 'ax', MUTE, 'end')
         + t_(X(ri), 142, 'r = 40', 'ax', MUTE, 'middle') + t_(X(ro), 142, 'r = 100 mm', 'ax', MUTE, 'middle'))
    card = svg(s)
    return spec('me-design-u1-L3', 'Combined<br>Stresses &amp;<br>Curved Beams', 'Is a crane hook just a straight beam?',
                f'Stress peaks at the {g_("INNER")} fibre:<br>straight theory is {c_("26 %")} low',
                'crane hook carrying 20 kN', card, o,
                [ch('left', 300, 'g', 'P = 20 kN'), ch('left', 364, 'c', 'inner radius 40 mm'),
                 ch('right', 470, 'g', f'inner {f(inner, 1)} MPa'), ch('right', 530, 'c', f'outer {f(outer, 1)} MPa', False)],
                f"R<sub>n</sub> = 60/ln(100/40) = 65.48 mm, e = {cl(f(e, 2) + ' mm')}<br>"
                f"Inner fibre {gl(f(inner, 1) + ' MPa')} against {f(straight, 1)} straight: ×{f(inner / straight, 2)}")



# ================================================================ unit 2
def u2_L1():
    """2.1 worked example: Syt 400 MPa, sx 100, sy 40, txy 60; Tresca and von Mises"""
    syt, sx, sy, tx = 400, 100, 40, 60
    c = (sx + sy) / 2; R = math.hypot((sx - sy) / 2, tx)
    s1, s2 = c + R, c - R
    n_tr = syt / (s1 - 0)
    seq = math.sqrt(sx ** 2 - sx * sy + sy ** 2 + 3 * tx ** 2); n_vm = syt / seq
    assert (f(R, 2), f(s1, 2), f(s2, 2), f(n_tr, 2), f(seq, 2), f(n_vm, 2)) == ('67.08', '137.08', '2.92', '2.92', '135.65', '2.95')
    # board: the stressed element of the shaft, with its stresses
    o = [box(2.6, 2.6, 2.8, 2.8, 2.8, 'steel', z0=.3)]
    m = 1.7
    o.append(arr3((5.45, 4.0, m), (7.3, 4.0, m), ACC2, 7))
    o.append(arr3((4.0, 5.45, m), (4.0, 6.6, m), ACC2, 5))
    o.append(arr3((5.42, 2.9, 2.75), (5.42, 5.1, 2.75), ACC, 5))
    o.append(arr3((2.9, 5.42, 2.75), (5.1, 5.42, 2.75), ACC, 5))
    o.append(lab(7.3, 4.0, m, 'σ<tspan dy="4" font-size="12">x</tspan>', ACC2, 18, 'start', dx=8, dy=6))
    o.append(lab(4.0, 6.6, m, 'σ<tspan dy="4" font-size="12">y</tspan>', ACC2, 18, 'end', dx=-8, dy=8))
    o.append(lab(5.42, 5.1, 2.75, 'τ', ACC, 20, 'start', dx=6, dy=4))
    # card: Tresca square and von Mises ellipse (first quadrant), point A and its two scale-ups; the two factors
    k = 118 / 480
    X = lambda v: 40 + v * k
    Y = lambda v: 130 - v * k
    ell = []
    for i in range(0, 91):
        t = math.radians(i)
        # points on s1^2 - s1 s2 + s2^2 = syt^2 along direction t
        dx_, dy_ = math.cos(t), math.sin(t)
        r = syt / math.sqrt(dx_ * dx_ - dx_ * dy_ + dy_ * dy_)
        ell.append(f'{X(r * dx_):.1f},{Y(r * dy_):.1f}')
    sq = f'{X(0)},{Y(400)} {X(400)},{Y(400)} {X(400)},{Y(0)}'
    s = (f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(480)}" y2="{Y(0)}" stroke="{AXC}" stroke-width="1.5"/>'
         f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(0)}" y2="{Y(480)}" stroke="{AXC}" stroke-width="1.5"/>'
         f'<polyline points="{sq}" fill="none" stroke="{ACC}" stroke-width="3"/>'
         f'<polyline points="{" ".join(ell)}" fill="none" stroke="{ACC2}" stroke-width="3"/>'
         f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(s1 * n_vm):.1f}" y2="{Y(s2 * n_vm):.1f}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="4 3"/>'
         f'<circle cx="{X(s1):.1f}" cy="{Y(s2):.1f}" r="5" fill="{INK}"/>'
         + t_(X(s1), Y(s2) - 10, 'A', 'pt', INK, 'middle')
         + t_(X(400) + 4, Y(400) + 2, '400', 'ax', MUTE) + t_(X(480), Y(0) + 14, 'σ₁', 'ax', MUTE, 'end') + t_(X(0) + 6, 12, 'σ₂', 'ax', MUTE)
         + hbars([('Tresca', n_tr, ACC, f(n_tr, 2)), ('von Mises', n_vm, ACC2, f(n_vm, 2))], 280, 420, 40, 42, 3.2, 24)
         + t_(330, 22, 'factor of safety n', 'ax', INK, 'middle', 14, 600))
    card = svg(s)
    return spec('me-design-u2-L1', 'Theories of<br>Failure &amp; Stress<br>Concentration', 'Tresca or von Mises: which is safer?',
                f'Tresca gives the {g_("LOWER")} n,<br>so it is the {c_("SAFER")} pick',
                'one point, two theories', card, o,
                [ch('left', 300, 'c', 'σ<sub>x</sub> = 100 MPa'), ch('left', 364, 'c', 'σ<sub>y</sub> = 40 MPa'), ch('left', 470, 'g', 'τ<sub>xy</sub> = 60 MPa'),
                 ch('right', 300, 'g', f'Tresca n = {f(n_tr, 2)}', False), ch('right', 500, 'c', f'von Mises n = {f(n_vm, 2)}')],
                f"σ₁ = 70 + 67.08 = {gl(f(s1, 2) + ' MPa')}, σ₂ = {f(s2, 2)}, σ₃ = 0<br>"
                f"n: Tresca 400/{f(s1, 2)} = {gl(f(n_tr, 2))} · von Mises {cl(f(n_vm, 2))}", tsize=62)


def u2_L2():
    """2.5 worked examples 1 and 2: 500 N falls 50 mm on a 20 mm rod 1 m long; then onto a 2000 N/mm spring"""
    W, h, d, L, E, ks = 500, 50, 20, 1000, 200_000, 2000
    A = math.pi * d * d / 4
    dst = W * L / (A * E); k1 = 1 + math.sqrt(1 + 2 * h / dst); sig1 = E * k1 * dst / L
    krod = A * E / L; keq = 1 / (1 / krod + 1 / ks); dst2 = W / keq; k2 = 1 + math.sqrt(1 + 2 * h / dst2)
    sig2 = k2 * W / A; s_st = W / A
    assert (f(dst, 6), f(k1, 2), f(sig1, 1), f(keq, 1), f(k2, 2), f(sig2, 2), f(s_st, 2)) == ('0.007958', '113.10', '180.0', '1938.3', '20.71', '32.97', '1.59')
    o = [box(2.3, 3.6, .55, .8, 5.6, 'dark'), box(5.15, 3.6, .55, .8, 5.6, 'dark'), box(2.3, 3.6, 3.4, .8, .5, 'iron', z0=5.6)]
    x0, y0 = 4.0, 4.0
    o.append(cylinder('z', .55, .85, (x0, y0), .62, 'dark'))
    bk, fr = helix(x0, y0, .85, 2.25, .48, 5.5, 5, ACC2, '#2C5A80')
    o.append(bk)
    o.append(cylinder('z', .85, 2.6, (x0, y0), .17, 'steel'))
    o.append(fr)
    o.append(cylinder('z', 2.6, 3.5, (x0, y0), .78, 'orange', hole=.2))
    o.append(cylinder('z', 3.5, 5.6, (x0, y0), .17, 'steel'))
    o.append(arr3((x0 + 1.05, y0 + 1.05, 3.9), (x0 + 1.05, y0 + 1.05, 2.9), ACC, 6, True))
    o.append(lab(x0 + 1.05, y0 + 1.05, 3.4, 'h = 50 mm', ACC, 15, 'start', dx=14))
    s = hbars([('static', s_st, ACC2, f'{f(s_st, 2)} MPa'), ('on the rod', sig1, ACC, f'{f(sig1, 1)} MPa'),
               ('on a spring', sig2, ACC2, f'{f(sig2, 1)} MPa')], 120, 370, 16, 40, 190, 24)
    card = svg(s)
    return spec('me-design-u2-L2', 'Fatigue,<br>Fluctuating Stress<br>&amp; Impact', 'Does a stiffer rod lower impact stress?',
                f'A stiffer rod {g_("RAISES")} the stress;<br>a soft {c_("SPRING")} cuts it',
                'same 500 N drop, rod stress', card, o,
                [ch('left', 300, 'g', 'W = 500 N, h = 50 mm'), ch('left', 364, 'c', 'rod Ø20 × 1 m'), ch('left', 470, 'c', 'spring 2000 N/mm'),
                 ch('right', 300, 'g', f'no spring: {f(sig1, 0)} MPa', False), ch('right', 500, 'c', f'spring: {f(sig2, 1)} MPa')],
                f"δ<sub>st</sub> = {f(dst, 6)} mm → factor {f(k1, 2)} → {gl(f(sig1, 1) + ' MPa')}<br>"
                f"k<sub>eq</sub> = {f(keq, 1)} N/mm → factor {f(k2, 2)} → {cl(f(sig2, 1) + ' MPa')}", tsize=62)


# ================================================================ unit 3
def u3_L1():
    """3.1 worked example: pulley 400 mm at 300 mm from A, bearings 900 mm apart, 10 kW at 500 rpm, T1/T2 = 3"""
    Pw, N, D_, ratio, a_, span = 10_000, 500, .4, 3, .3, .9
    T = 60 * Pw / (2 * math.pi * N)
    dT = T / (D_ / 2); T2 = dT / (ratio - 1); T1 = ratio * T2; W = T1 + T2
    RA = W * (span - a_) / span; RB = W * a_ / span; M = RA * a_
    Te = math.hypot(1.5 * M, 1.0 * T); tau = .75 * min(.3 * 380, .18 * 640)
    d = (16 * Te * 1000 / (math.pi * tau)) ** (1 / 3)
    assert (f(T, 2), f(T1, 2), f(T2, 2), f(W, 2), f(RA, 2), f(RB, 2), f(M, 2), f(Te, 2), f(d, 1)) == ('190.99', '1432.39', '477.46', '1909.86', '1273.24', '636.62', '381.97', '603.95', '33.0')
    yc, zc, r = 4.0, 2.2, .3
    xa, xb = 1.0, 7.0
    xp = xa + (xb - xa) * a_ / span
    rp = (xb - xa) * (D_ / span) / 2
    o = [box(xa - .35, yc - .7, .7, 1.4, zc - .55, 'dark'), cylinder('x', xa - .3, xa + .3, (yc, zc), .6, 'iron'),
         cylinder('x', .3, xp - .3, (yc, zc), r, 'steel')]
    o.append(box(xp - .2, yc - rp - .08, .4, .16, zc, 'orange'))
    o.append(cylinder('x', xp - .3, xp + .3, (yc, zc), rp, 'iron'))
    o.append(box(xp - .2, yc + rp - .08, .4, .16, zc, 'orange'))
    o.append(cylinder('x', xp + .3, xb - .3, (yc, zc), r, 'steel'))
    o.append(box(xb - .35, yc - .7, .7, 1.4, zc - .55, 'dark'))
    o.append(cylinder('x', xb - .3, xb + .3, (yc, zc), .6, 'iron'))
    o.append(cylinder('x', xb + .3, xb + .8, (yc, zc), r, 'steel'))
    o.append(arr3((xp, yc + rp + .5, 1.5), (xp, yc + rp + .5, .2), ACC, 6, True))
    o.append(arr3((xp, yc - rp - .5, 1.5), (xp, yc - rp - .5, .2), ACC, 5))
    o.append(lab(xp, yc + rp + .5, .9, 'T₁', ACC, 18, 'end', dx=-12))
    o.append(lab(xp, yc - rp - .5, .9, 'T₂', ACC, 18, 'end', dx=-12))
    o.append(lab(xa, yc, zc + .6, 'A', INK, 17, dy=-6) + lab(xb, yc, zc + .6, 'B', INK, 17, dy=-6))
    # card: free body (left) and bending moment (right)
    bx0, bx1, by = 30, 210, 70
    xw = bx0 + (bx1 - bx0) * a_ / span
    s = (f'<line x1="{bx0}" y1="{by}" x2="{bx1}" y2="{by}" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
         + arrow(xw, 20, xw, by - 6, ACC, 4) + arrow(bx0, 122, bx0, by + 6, ACC2, 4) + arrow(bx1, 122, bx1, by + 6, ACC2, 4)
         + t_(xw + 8, 30, f'{f(W, 0)} N', 'pt', ACC) + t_(bx0 + 8, 134, f'{f(RA, 0)}', 'pt', ACC2) + t_(bx1 - 8, 134, f'{f(RB, 0)}', 'pt', ACC2, 'end')
         + t_((bx0 + xw) / 2, by - 8, '300', 'ax', MUTE, 'middle') + t_((xw + bx1) / 2, by - 8, '600 mm', 'ax', MUTE, 'middle'))
    mx0, mx1, my = 250, 450, 118
    mp = mx0 + (mx1 - mx0) * a_ / span
    s += (f'<polygon points="{mx0},{my} {mp:.1f},{my - 80} {mx1},{my}" fill="{ACC}" fill-opacity=".16" stroke="{ACC}" stroke-width="3" stroke-linejoin="round"/>'
          f'<line x1="{mx0}" y1="{my}" x2="{mx1}" y2="{my}" stroke="{AXC}" stroke-width="1.5"/>'
          f'<circle cx="{mp:.1f}" cy="{my - 80}" r="5" fill="{ACC}"/>' + t_(mp + 10, my - 74, f'M = {f(M, 0)} N·m', 'pt', ACC)
          + t_((mx0 + mx1) / 2, 140, 'bending moment', 'ax', MUTE, 'middle'))
    card = svg(s)
    return spec('me-design-u3-L1', 'Shaft Design<br>for Strength<br>&amp; Rigidity', 'What load does a belt put on a shaft?',
                f'The shaft is pulled by {g_("T₁ + T₂")},<br>turned by the {c_("DIFFERENCE")}',
                'pulley shaft on two bearings', card, o,
                [ch('left', 300, 'g', f'T₁ = {f(T1, 0)} N'), ch('left', 470, 'g', f'T₂ = {f(T2, 0)} N'),
                 ch('right', 300, 'c', '10 kW at 500 rpm', False), ch('right', 500, 'c', f'd = {f(d, 1)} → 35 mm')],
                f"(T₁ − T₂) × 0.2 = {f(T, 2)}, T₁ = 3T₂ → {gl('W = ' + f(W, 2) + ' N')}<br>"
                f"M = {f(RA, 2)} × 0.3 = {cl(f(M, 2) + ' N·m')} under the pulley")


def u3_L2():
    """3.3 worked example: 50 mm shaft, 20 kW at 600 rpm, 14 x 9 key, shear 40 MPa, crushing 80 MPa"""
    d, Pw, N, w, hk, tau, sc = 50, 20_000, 600, 14, 9, 40, 80
    T = 60 * Pw / (2 * math.pi * N) * 1000
    F = 2 * T / d; l_s = F / (w * tau); l_c = F / (hk / 2 * sc)
    e = 1 - .2 * w / d - 1.1 * (hk / 2) / d
    assert (f(T, 0), f(F, 0), f(l_s, 1), f(l_c, 1), f(e, 3)) == ('318 310', '12 732', '22.7', '35.4', '0.845')
    yc, zc = 4.0, 2.4
    ru = 1.05; u = ru / (d / 2)
    xf = 5.4
    o = [cylinder('x', .4, xf, (yc, zc), ru, 'steel'), cylinder('x', 3.2, xf, (yc, zc), 2.15, 'iron', hole=ru)]
    o.append(f'<polygon points="{pts(*outline("x", xf, (yc, zc), ru))}" fill="#C9D2DA"/>')
    kw, kh = w * u, hk * u
    key = [P(xf + .01, yc - kw / 2, zc + ru - kh / 2), P(xf + .01, yc + kw / 2, zc + ru - kh / 2), P(xf + .01, yc + kw / 2, zc + ru + kh / 2), P(xf + .01, yc - kw / 2, zc + ru + kh / 2)]
    o.append(f'<polygon points="{pts(*key)}" fill="{ACC}" stroke="#FFD0AA" stroke-width="1.5"/>')
    mid = [P(xf + .02, yc - kw / 2 - .15, zc + ru), P(xf + .02, yc + kw / 2 + .15, zc + ru)]
    o.append(f'<line x1="{mid[0][0]:.1f}" y1="{mid[0][1]:.1f}" x2="{mid[1][0]:.1f}" y2="{mid[1][1]:.1f}" stroke="#1E252C" stroke-width="2"/>')
    arc = [P(xf + .02, yc + 2.55 * math.cos(math.radians(a)), zc + 2.55 * math.sin(math.radians(a))) for a in range(200, 330, 6)]
    o.append(f'<polyline points="{pts(*arc[:-1])}" fill="none" stroke="{ACC2}" stroke-width="5" stroke-linecap="round"/>' + arrow(*arc[-3], *arc[-1], ACC2, 5))
    o.append(lab(xf, yc - .2, zc - 2.75, 'T', ACC2, 20, 'end', dx=-30, dy=8))
    # card: key section (left) and the three lengths (right)
    cx, cy, R = 92, 92, 46
    kw2, kh2 = w * R / 25, hk * R / 25
    s = (f'<circle cx="{cx}" cy="{cy}" r="{R + 30}" fill="#56626E" fill-opacity=".35"/><circle cx="{cx}" cy="{cy}" r="{R}" fill="#B7C2CC" fill-opacity=".55"/>'
         f'<rect x="{cx - kw2 / 2:.1f}" y="{cy - R - kh2 / 2:.1f}" width="{kw2:.1f}" height="{kh2:.1f}" fill="{ACC}"/>'
         f'<line x1="{cx - kw2 / 2:.1f}" y1="{cy - R:.1f}" x2="{cx - kw2 / 2:.1f}" y2="{cy - R + kh2 / 2:.1f}" stroke="{ACC2}" stroke-width="5"/>'
         f'<line x1="{cx - kw2 / 2 - 34:.1f}" y1="{cy - R:.1f}" x2="{cx + kw2 / 2 + 34:.1f}" y2="{cy - R:.1f}" stroke="{INK}" stroke-width="1.2" stroke-dasharray="3 3"/>'
         + t_(cx - kw2 / 2 - 6, cy - R + 16, 'h/2', 'pt', ACC2, 'end') + t_(cx, cy + 6, 'Ø50', 'pt', '#1E252C', 'middle')
         + t_(cx + kw2 / 2 + 6, cy - R - 16, '14 × 9', 'pt', ACC)
         + hbars([('shear', l_s, ACC2, f'{f(l_s, 1)} mm'), ('crushing', l_c, ACC, f'{f(l_c, 1)} mm'), ('key used', 40, INK, '40 mm')], 284, 400, 22, 38, 40, 22))
    card = svg(s)
    return spec('me-design-u3-L2', 'Keys, Splines<br>&amp; Couplings', 'Why does a key crush on half its height?',
                f'Each part holds {g_("HALF")} the key:<br>{c_("CRUSHING")} sets the length',
                'sunk key on a 50 mm shaft', card, o,
                [ch('left', 300, 'c', 'T = 318.31 N·m'), ch('left', 364, 'g', f'F = 2T/d = {f(F, 0)} N'),
                 ch('right', 470, 'g', f'crushing: {f(l_c, 1)} mm', False), ch('right', 530, 'c', f'shear: {f(l_s, 1)} mm', False)],
                f"Shear: l = {f(F, 0)}/(14 × 40) = {cl(f(l_s, 1) + ' mm')}<br>"
                f"Crushing on h/2: {f(F, 0)}/(4.5 × 80) = {gl(f(l_c, 1) + ' mm')}")


def u3_L3():
    """3.5 worked example: single-plate clutch, both sides effective, ro 150, ri 100, mu 0.3, W 5 kN"""
    ro, ri, mu, W, n = .15, .10, .3, 5000, 2
    Tw = mu * W * n * (ro + ri) / 2
    Tp = 2 / 3 * mu * W * n * (ro ** 3 - ri ** 3) / (ro ** 2 - ri ** 2)
    om = 2 * math.pi * 1200 / 60; Pw = Tw * om
    pmax = W / (2 * math.pi * ri * (ro - ri)) / 1e6
    heat = Tw * (2 * math.pi * 600 / 60) / 2 * .5
    assert (f(Tw, 0), f(Tp, 0), f(Pw / 1000, 1), f(pmax, 3), f(heat, 0)) == ('375', '380', '47.1', '0.159', '5890')
    xc = yc = 4.0
    rp = 2.1
    o = [cylinder('z', .2, 1.0, (xc, yc), 2.45, 'iron'), cylinder('z', 1.0, 1.5, (xc, yc), .34, 'steel'),
         cylinder('z', 1.5, 1.7, (xc, yc), rp, 'orange'), cylinder('z', 1.7, 1.86, (xc, yc), rp, 'steel'),
         cylinder('z', 1.86, 2.06, (xc, yc), rp, 'orange', cap='#FFB988'),
         ring_on('z', 2.06, (xc, yc), rp * ri / ro, '#8A4A1E', 2, '5 4'),
         cylinder('z', 2.06, 2.65, (xc, yc), .34, 'steel'), cylinder('z', 2.65, 3.25, (xc, yc), rp, 'steel', hole=.36),
         cylinder('z', 3.25, 4.4, (xc, yc), .34, 'steel')]
    for a in (210, 330, 90):
        x, y = xc + 1.45 * math.cos(math.radians(a)), yc + 1.45 * math.sin(math.radians(a))
        o.append(arr3((x, y, 4.55), (x, y, 3.35), ACC2, 5))
    rows = [('uniform wear', f'{f(Tw, 0)} N·m', f'{f(Pw / 1000, 1)} kW', ACC), ('uniform pressure', f'{f(Tp, 0)} N·m', '', ACC2),
            ('largest pressure', f'{f(pmax, 3)} MPa', 'at r<sub>i</sub>', INK)]
    card = ('<table><tr><th></th><th>torque, n = 2</th><th>at 1200 rpm</th></tr>' + ''.join(
        f'<tr><td style="color:{c}">{a}</td><td style="color:{c};font-weight:700">{b}</td><td>{d}</td></tr>' for a, b, d, c in rows) + '</table>')
    return spec('me-design-u3-L3', 'Clutches,<br>Brakes &amp;<br>Connecting Rods', 'Single-plate clutch: one face or two?',
                f'Both sides lined: {g_("TWO")} faces,<br>so n = 2 {c_("DOUBLES")} the torque',
                'single-plate clutch', card, o,
                [ch('left', 300, 'c', 'W = 5 kN, μ = 0.3'), ch('left', 470, 'c', 'r<sub>o</sub> = 150, r<sub>i</sub> = 100 mm'),
                 ch('right', 300, 'g', 'n = 2 faces', False), ch('right', 500, 'g', f'T = {f(Tw, 0)} N·m')],
                f"T = 0.3 × 5000 × {gl('2')} × 0.25/2 = {gl(f(Tw, 0) + ' N·m')}<br>"
                f"P = 375 × 125.66 = {cl(f(Pw / 1000, 1) + ' kW')} at 1200 rpm", tsize=66)



# ================================================================ unit 4
def u4_L1():
    """4.2 worked example 1: two vertical fillet welds 100 long, 100 apart, leg 6 mm, 10 kN at 150 mm from G"""
    Pn, l, gap, hl, ecc = 10_000, 100, 100, 6, 150
    t = .707 * hl; A = 2 * t * l
    tau1 = Pn / A; Tq = Pn * ecc
    J = t * 2 * (l ** 3 / 12 + l * (gap / 2) ** 2)
    r = math.hypot(gap / 2, l / 2); tau2 = Tq * r / J
    comp = tau2 / math.sqrt(2)
    near = math.hypot(comp, comp + tau1); far = math.hypot(comp, comp - tau1)
    assert (f(t, 2), f(A, 1), f(tau1, 1), f(J / 1e6, 2), f(tau2, 1), f(near, 1), f(far, 1)) == ('4.24', '848.4', '11.8', '2.83', '37.5', '46.6', '30.3')
    u = 1.9 / gap                          # board units per mm
    xg, zg = 2.9, 2.6                      # weld-group centroid G on the plate face
    xl, xr = xg - gap / 2 * u, xg + gap / 2 * u
    yf = 2.4                               # plate front face; the column flange stands in front of it
    o = [box(.9, yf - .3, 5.9, .3, 3.0, 'steel', z0=zg - 1.5)]
    o.append(box(xl, yf, xr - xl, .32, 5.3, 'iron'))
    leg = .42
    for xw, side in ((xl, -1), (xr, 1)):
        z0, z1 = zg - l / 2 * u, zg + l / 2 * u
        b_, c = (xw + side * leg, yf, z0), (xw, yf + leg * .75, z0)
        b1, c1 = (xw + side * leg, yf, z1), (xw, yf + leg * .75, z1)
        o.append(f'<polygon points="{pts(P(*b_), P(*c), P(*c1), P(*b1))}" fill="{ACC}" stroke="#FFD0AA" stroke-width="1.5"/>')
        o.append(f'<polygon points="{pts(P(xw, yf, z1), P(*b1), P(*c1))}" fill="#FFD0AA"/>')
    gx, gy = P(xg, yf + .33, zg)
    o.append(f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="6" fill="{INK}"/>' + lab(xg, yf + .33, zg, 'G', INK, 16, 'start', dx=8, dy=-4))
    xp = xg + ecc * u
    o.append(arr3((xp, yf - .15, zg + 3.0), (xp, yf - .15, zg + 1.55), ACC, 7, True))
    o.append(lab(xp, yf - .15, zg + 2.4, '10 kN', ACC, 16, 'start', dx=14))
    pa, pb = P(xg, yf - .15, zg + 1.75), P(xp, yf - .15, zg + 1.75)
    o.append(f'<line x1="{pa[0]:.1f}" y1="{pa[1]:.1f}" x2="{pb[0]:.1f}" y2="{pb[1]:.1f}" stroke="{ACC2}" stroke-width="2.5" stroke-dasharray="5 4"/>')
    o.append(lab((xg + xp) / 2, yf - .15, zg + 1.75, '150 mm', ACC2, 15, dy=-8))
    # card: the fillet weld in section (left), stresses at the two welds (right)
    k = 13
    ox, oy = 50, 116
    s = (f'<polygon points="{ox},{oy} {ox + hl * k},{oy} {ox},{oy - hl * k}" fill="{ACC}" fill-opacity=".85"/>'
         f'<line x1="{ox - 26}" y1="{oy}" x2="{ox + 120}" y2="{oy}" stroke="{AXC}" stroke-width="3"/>'
         f'<line x1="{ox}" y1="{oy + 10}" x2="{ox}" y2="{oy - 100}" stroke="{AXC}" stroke-width="3"/>'
         f'<line x1="{ox}" y1="{oy}" x2="{ox + hl * k / 2:.1f}" y2="{oy - hl * k / 2:.1f}" stroke="{ACC2}" stroke-width="3.5"/>'
         + t_(ox + hl * k / 2 + 6, oy - hl * k / 2 - 4, f'throat {f(t, 2)}', 'pt', ACC2)
         + t_(ox + hl * k / 2, oy + 18, 'leg 6 mm', 'ax', ACC, 'middle', 14, 700)
         + hbars([('near weld', near, ACC, f'{f(near, 1)} MPa'), ('far weld', far, ACC2, f'{f(far, 1)} MPa')], 300, 370, 44, 40, 50, 24, vx=466))
    card = svg(s)
    return spec('me-design-u4-L1', 'Eccentric<br>Bolted &amp;<br>Welded Joints', 'What is the throat of a fillet weld?',
                f'Throat = 0.707 × the {g_("LEG")}:<br>stress acts on the {c_("THROAT")}',
                'two fillet welds, 10 kN', card, o,
                [ch('left', 300, 'g', 'P = 10 kN at 150 mm'), ch('left', 470, 'c', 'two welds, 100 mm long'),
                 ch('right', 300, 'c', 'leg h = 6 mm', False), ch('right', 500, 'g', f'τ<sub>max</sub> = {f(near, 1)} MPa')],
                f"Throat t = 0.707 × 6 = {cl(f(t, 2) + ' mm')}, A = {f(A, 1)} mm²<br>"
                f"τ₁ = {f(tau1, 1)}, τ₂ = {f(tau2, 1)} → {gl(f(near, 1) + ' MPa')} at the near weld")


def u4_L2():
    """4.3 worked example 1: knuckle joint for 50 kN; tension 80, shear 50, crushing 90 MPa"""
    Pn, st, ts = 50_000, 80, 50
    d = math.sqrt(4 * Pn / (math.pi * st)); dr, b, a = 30, 1.25 * 30, .75 * 30
    tau = 2 * Pn / (math.pi * dr ** 2)
    M = Pn / 2 * (b / 4 + a / 3); sb30 = 32 * M / (math.pi * dr ** 3)
    d1 = (32 * M / (math.pi * st)) ** (1 / 3); sb38 = 32 * M / (math.pi * 38 ** 3)
    assert (f(d, 1), f(tau, 1), f(round(M, -2), 0), f(sb30, 0), f(d1, 1), f(sb38, 1)) == ('28.2', '35.4', '421\u2009900', '159', '37.7', '78.3')
    u = 1 / 30
    yc, zc = 4.0, 2.35
    rr, rp, re_, bb, aa = 15 * u * 1.1, 19 * u * 1.1, 33 * u * 1.1, b * u * 1.1, a * u * 1.1
    xpin = 4.3
    zb0 = zc - bb / 2 - .08 - aa; ze0 = zc - bb / 2; zt0 = zc + bb / 2 + .08
    o = [cylinder('x', .3, 2.0, (yc, zc), rr, 'steel'),
         box(2.0, yc - re_, .9, 2 * re_, zt0 + aa - zb0, 'iron', z0=zb0),
         box(2.9, yc - re_, xpin - 2.9, 2 * re_, aa, 'iron', z0=zb0), cylinder('z', zb0, zb0 + aa, (xpin, yc), re_, 'iron'),
         cylinder('z', ze0, ze0 + bb, (xpin, yc), re_, 'orange'),
         box(2.9, yc - re_, xpin - 2.9, 2 * re_, aa, 'iron', z0=zt0), cylinder('z', zt0, zt0 + aa, (xpin, yc), re_, 'iron', hole=rp),
         cylinder('z', zt0 + aa - .05, zt0 + aa + .25, (xpin, yc), rp, 'blue'),
         cylinder('x', xpin + re_ - .1, 7.7, (yc, zc), rr, 'steel')]
    o.append(arr3((7.75, yc, zc), (8.7, yc, zc), ACC, 6, True) + arr3((.25, yc, zc), (-.7, yc, zc), ACC, 6, True))
    o.append(lab(xpin, yc, zt0 + aa + .25, 'pin', ACC2, 16, 'start', dx=26, dy=-4))
    o.append(lab(xpin + re_, yc + re_, zc, 'eye', ACC, 15, 'start', dx=4, dy=4))
    s = hbars([('pin shear', tau, ACC2, f'{f(tau, 1)} ≤ 50'), ('bending, Ø30', sb30, ACC, f'{f(sb30, 0)} > 80'),
               ('bending, Ø38', sb38, ACC2, f'{f(sb38, 1)} ≤ 80')], 130, 360, 14, 40, 170, 24)
    card = svg(s + t_(462, 140, 'MPa', 'ax', MUTE, 'end'))
    return spec('me-design-u4-L2', 'Knuckle, Cotter,<br>Riveted &amp;<br>Bonded Joints', 'Does a knuckle pin shear on one plane?',
                f'{g_("TWO")} shear planes, but<br>{c_("BENDING")} sizes the pin',
                'knuckle joint for 50 kN', card, o,
                [ch('left', 300, 'g', 'P = 50 kN'), ch('left', 470, 'c', 'pin in double shear'),
                 ch('right', 300, 'g', f'σ<sub>b</sub> = {f(sb30, 0)} MPa > 80', False), ch('right', 500, 'c', 'pin Ø30 → Ø38 mm')],
                f"Shear, 2 planes: 2 × 50 000/(π × 30²) = {cl(f(tau, 1) + ' MPa')}<br>"
                f"M = 421 900 N·mm → {gl(f(sb30, 0) + ' MPa')}, so pin {gl('38 mm')}", tsize=64)


def u4_L3():
    """4.5 worked example 1: square thread, dm 24, lead 6, W 20 kN, mu 0.15"""
    dm, lead, W, mu = 24, 6, 20_000, .15
    ta = lead / (math.pi * dm); al = math.degrees(math.atan(ta)); ph = math.degrees(math.atan(mu))
    Tr = W * dm / 2 * (mu + ta) / (1 - mu * ta); Tl = W * dm / 2 * (mu - ta) / (1 + mu * ta)
    eta = W * lead / (2 * math.pi * Tr)
    assert (f(ta, 4), f(al, 2), f(ph, 2), f(round(Tr, -2) / 1000, 1), f(round(Tl, -2) / 1000, 1), f(eta * 100, 1)) == ('0.0796', '4.55', '8.53', '55.8', '16.7', '34.2')
    xc = yc = 4.0
    o = [box(2.7, 2.7, 2.6, 2.6, 1.5, 'iron')]
    o.append(cylinder('z', 1.5, 5.0, (xc, yc), .62, 'steel'))
    turns = 9
    bk, fr = helix(xc, yc, 1.5, 4.9, .63, turns, 3, '#56626E', 'none')
    o.append(fr)
    o.append(cylinder('z', 5.0, 5.35, (xc, yc), 1.1, 'dark'))
    o.append(box(3.1, 3.1, 1.8, 1.8, .7, 'orange', z0=5.35))
    o.append(arr3((xc + .9, yc + .9, 7.6), (xc + .9, yc + .9, 6.15), ACC, 7, True))
    o.append(lab(xc + .9, yc + .9, 7.2, '20 kN', ACC, 16, 'end', dx=-14))
    o.append(lab(xc + 1.3, yc + 1.3, .7, 'nut', INK, 15, dy=6))
    # card: one turn unwrapped, true angles
    x0, y0, base = 28, 116, 300
    hA = base * ta; hF = base * math.tan(math.radians(ph))
    s = (f'<polygon points="{x0},{y0} {x0 + base},{y0} {x0 + base},{y0 - hA:.1f}" fill="{ACC2}" fill-opacity=".25" stroke="{ACC2}" stroke-width="3"/>'
         f'<line x1="{x0}" y1="{y0}" x2="{x0 + base}" y2="{y0 - hF:.1f}" stroke="{ACC}" stroke-width="3" stroke-dasharray="8 5"/>'
         + t_(x0 + base / 2 + 40, y0 + 20, f'πd<tspan dy="4" font-size="11">m</tspan><tspan dy="-4"> = {f(math.pi * dm, 1)} mm</tspan>', 'ax', INK, 'middle', 14, 600)
         + t_(x0 + base + 6, y0 - hA / 2 + 6, 'lead 6', 'ax', ACC2, 'start', 14, 700)
         + t_(x0, y0 + 20, f'α = {f(al, 2)}°', 'pt', ACC2)
         + t_(x0 + base - 10, y0 - hF - 10, f'friction angle φ = {f(ph, 2)}°', 'pt', ACC, 'end')
         + t_(x0 + base + 60, 40, 'φ > α', 'pt', ACC, 'middle', 22, 700) + t_(x0 + base + 60, 64, 'self-locks', 'pt', INK, 'middle'))
    card = svg(s)
    return spec('me-design-u4-L3', 'Power Screws<br>&amp; Helical<br>Springs', 'When does a power screw self-lock?',
                f'Self-locks when the {g_("FRICTION")}<br>angle beats the {c_("HELIX")} angle',
                'one turn of the thread', card, o,
                [ch('left', 300, 'g', 'W = 20 kN'), ch('left', 364, 'c', 'd<sub>m</sub> = 24 mm, lead 6 mm'), ch('left', 470, 'c', 'μ = 0.15'),
                 ch('right', 300, 'c', f'T<sub>r</sub> = {f(round(Tr, -2) / 1000, 1)} N·m', False), ch('right', 500, 'g', f'T<sub>l</sub> = +{f(round(Tl, -2) / 1000, 1)} N·m')],
                f"tan α = 6/(π × 24) → {cl('α = ' + f(al, 2) + '°')} < {gl('φ = ' + f(ph, 2) + '°')}<br>"
                f"T<sub>l</sub> = {f(round(Tl, -2) / 1000, 1)} N·m > 0 → self-locking; η = {f(eta * 100, 1)} %")


def u4_L4():
    """4.7 worked example 1: two concentric springs, 10 kN, C = 6, 600 MPa, G = 81 370 MPa, about 80 mm"""
    W, C, tau, G, dl = 10_000, 6, 600, 81_370, 80
    ratio = C / (C - 2); pr = ratio ** 2
    P1 = W * pr / (1 + pr); P2 = W - P1
    K = (4 * C - 1) / (4 * C - 4) + .615 / C
    d1c = math.sqrt(K * 8 * P1 * C / (math.pi * tau)); d1, D1 = 15, 90; d2, D2 = 10, 60
    clr = (D1 - d1) / 2 - (D2 + d2) / 2
    k1 = G * d1 ** 4 / (8 * D1 ** 3 * 8); k2 = G * d2 ** 4 / (8 * D2 ** 3 * 12); defl = W / (k1 + k2)
    assert (f(P1, 0), f(P2, 0), f(K, 4), f(d1c, 1), f(clr, 1), f(k1, 1), f(k2, 1), f(defl, 1)) == ('6923', '3077', '1.2525', '14.9', '2.5', '88.3', '39.2', '78.4')
    xc = yc = 4.0
    u = 2.0 / (D1 / 2)
    o = [cylinder('z', 0, .35, (xc, yc), 2.35, 'iron')]
    zt = 3.9
    ob, of = helix(xc, yc, .35, zt, D1 / 2 * u, 6, 10, ACC, '#8A4A1E', hand=1)
    ib, if_ = helix(xc, yc, .35, zt, D2 / 2 * u, 9, 7, ACC2, '#2C5A80', hand=-1)
    o += [ob, ib, if_, of]
    o.append(cylinder('z', zt, zt + .35, (xc, yc), 2.35, 'steel'))
    o.append(arr3((xc, yc, zt + 1.9), (xc, yc, zt + .45), INK, 7, True))
    o.append(lab(xc, yc, zt + 1.5, '10 kN', INK, 16, 'start', dx=16))
    rows = [('outer', d1, D1, 8, f'{f(P1, 0)} N', ACC), ('inner', d2, D2, 12, f'{f(P2, 0)} N', ACC2)]
    card = ('<table><tr><th></th><th>wire d</th><th>mean D</th><th>coils</th><th>load</th></tr>' + ''.join(
        f'<tr><td style="color:{c}">{n}</td><td>{a} mm</td><td>{b_} mm</td><td>{k}</td><td style="color:{c};font-weight:700">{ld}</td></tr>'
        for n, a, b_, k, ld, c in rows) + f'<tr><td style="color:{INK}">both</td><td colspan="4">C = 6 · deflection {f(defl, 1)} mm · gap {f(clr, 1)} mm</td></tr></table>')
    return spec('me-design-u4-L4', 'Concentric<br>&amp; Leaf<br>Springs', 'Do nested springs share load equally?',
                f'No: the outer takes {g_("2.25×")}<br>the inner, at the {c_("SAME")} deflection',
                'two springs, one 10 kN load', card, o,
                [ch('left', 300, 'c', 'W = 10 kN'), ch('left', 364, 'c', 'C = 6, τ ≤ 600 MPa'),
                 ch('right', 300, 'g', f'outer {f(P1, 0)} N', False), ch('right', 500, 'c', f'inner {f(P2, 0)} N')],
                f"d₁/d₂ = C/(C − 2) = 1.5 → P₁/P₂ = 1.5² = {gl(f(pr, 2))}<br>"
                f"P₁ = {gl(f(P1, 0) + ' N')}, P₂ = {cl(f(P2, 0) + ' N')}; both deflect {f(defl, 1)} mm")


def u4_L5():
    """4.10 worked example 2: engine flywheel, dE 15 kJ, 600 rpm, Cs 0.02, R 0.6 m, t 120 mm, 6 arms"""
    dE, N, Cs, R, t, rho, z = 15_000, 600, .02, .6, .12, 7200, 6
    w = 2 * math.pi * N / 60; I = dE / (w * w * Cs); m = I / R ** 2
    Ar = m / (rho * 2 * math.pi * R) * 1e6; bw = Ar / (t * 1000)
    v = w * R; st = rho * v * v / 1e6
    sb = 19.74 * rho * v * v * R / (z ** 2 * t) / 1e6
    sc = .75 * st + .25 * sb
    assert (f(I, 0), f(m, 0), f(bw, 0), f(v, 1), f(st, 2), f(sb, 1), f(sc, 1)) == ('190', '528', '162', '37.7', '10.23', '28.1', '14.7')
    yc, zc = 4.0, 2.75
    Ro, Ri = 2.45, 2.45 * (R - t / 2) / (R + t / 2)
    x0, x1 = 3.4, 3.4 + (bw / 1000) / (R + t / 2) * 2.45
    a0, a1 = outline('x', x0, (yc, zc), Ro), outline('x', x1, (yc, zc), Ro)
    cb = P(x1, yc, zc)
    gid, gd = grad((cb[0] - 70, cb[1] - 40), (cb[0] + 70, cb[1] + 40), 'iron')
    o = [gd,
         f'<polygon points="{pts(*hull(a0 + a1))}" fill="url(#{gid})"/>',
         f'<polygon points="{pts(*outline("x", x1, (yc, zc), Ri))}" fill="#1A2128"/>']
    o.append(cylinder('x', .6, (x0 + x1) / 2, (yc, zc), .3, 'steel'))
    xm = (x0 + x1) / 2
    for k in range(z):
        a = math.radians(90 + k * 60)
        p0, p1 = P(xm, yc + .5 * math.cos(a), zc + .5 * math.sin(a)), P(xm, yc + (Ri + .05) * math.cos(a), zc + (Ri + .05) * math.sin(a))
        o.append(f'<line x1="{p0[0]:.1f}" y1="{p0[1]:.1f}" x2="{p1[0]:.1f}" y2="{p1[1]:.1f}" stroke="#97A3AE" stroke-width="13" stroke-linecap="round"/>')
    o.append(cylinder('x', x0 - .1, x1 + .1, (yc, zc), .62, 'steel'))
    o.append(f'<path d="M{pts(*a1)}Z M{pts(*outline("x", x1, (yc, zc), Ri))}Z" fill="#A9B4BF" fill-rule="evenodd"/>')
    seg = [P(x1, yc + (Ro + .25) * math.cos(math.radians(a)), zc + (Ro + .25) * math.sin(math.radians(a))) for a in range(-30, 31, 3)]
    o.append(f'<polyline points="{pts(*seg)}" fill="none" stroke="{ACC}" stroke-width="5" stroke-dasharray="8 5"/>')
    o.append(cylinder('x', x1 + .1, 7.6, (yc, zc), .3, 'steel'))
    sx, sy = seg[len(seg) // 2]
    s = hbars([('hoop ρv²', st, ACC2, f'{f(st, 2)} MPa'), ('bending', sb, ACC, f'{f(sb, 1)} MPa'),
               ('combined', sc, INK, f'{f(sc, 1)} MPa')], 110, 330, 8, 36, 30, 24, limit=(15, 'permissible 15 MPa'), vx=440)
    card = svg(s)
    return spec('me-design-u4-L5', 'Rubber Springs<br>&amp; Flywheels', 'Why check a flywheel rim for bending?',
                f'The rim {g_("BENDS")} between arms:<br>more than the {c_("HOOP")} stress',
                'flywheel rim stresses', card, o,
                [ch('left', 300, 'c', 'ΔE = 15 kJ at 600 rpm'), ch('left', 470, 'c', '6 arms, R = 0.6 m'),
                 ch('right', 300, 'c', f'rim {f(m, 0)} kg', False), ch('right', 500, 'g', f'σ<sub>b</sub> = {f(sb, 1)} MPa')],
                f"σ<sub>t</sub> = ρv² = 7200 × {f(v, 1)}² = {cl(f(st, 2) + ' MPa')}; σ<sub>b</sub> = {gl(f(sb, 1) + ' MPa')}<br>"
                f"0.75 × {f(st, 2)} + 0.25 × {f(sb, 1)} = {f(sc, 1)} MPa ≤ 15")



# ================================================================ unit 5
def poly3(points, fill, extra=''):
    return f'<polygon points="{pts(*[P(*q) for q in points])}" fill="{fill}"{extra}/>'


def u5_L1():
    """5.1 worked example: mu 0.05 Pa s, rho 900 kg/m3; 0.1 mm film, plate 0.01 m2 at 2 m/s"""
    mu, rho, h, A, U = .05, 900, .1e-3, .01, 2
    nu = mu / rho; cst = nu / 1e-6; wrong = mu / .9
    rate = U / h; tau = mu * rate; F = tau * A
    assert (f(nu * 1e5, 3), f(cst, 2), f(wrong, 4), f(rate, 0), f(tau, 0), f(F, 0)) == ('5.556', '55.56', '0.0556', '20\u2009000', '1000', '10')
    o = [box(.8, 1.4, 6.4, 5.2, .55, 'iron')]
    z0, z1 = .55, 1.65                                    # the film, drawn far thicker than 0.1 mm
    o.append(B.box(.8, 1.4, 6.4, 5.2, z1 - z0, 'rgba(255,158,90,.30)', 'rgba(255,158,90,.42)', 'rgba(255,158,90,.36)', z0))
    o.append(box(1.6, 2.0, 4.2, 4.0, .45, 'steel', z0=z1))
    for k in range(5):
        z = z0 + (z1 - z0) * (k + .5) / 5
        L = 2.6 * (k + .5) / 5
        o.append(arr3((1.0, 6.62, z), (1.0 + L, 6.62, z), ACC, 3.5))
    o.append(arr3((3.6, 4.0, z1 + .45), (6.6, 4.0, z1 + .45), ACC2, 7, True))
    o.append(lab(6.6, 4.0, z1 + .45, 'U = 2 m/s', ACC2, 16, 'start', dx=10, dy=-6))
    o.append(lab(1.0, 6.62, z0, 'u = 0', INK, 14, 'end', dx=-8, dy=4))
    rows = [('dynamic μ', '0.05 Pa·s', INK), ('density ρ', '900 kg/m³', INK),
            ('ν = μ/ρ', f'5.556 × 10<sup>−5</sup> m²/s = {f(cst, 1)} cSt', ACC),
            ('ρ as 0.9', f'{f(wrong, 4)}: 1000 × too big', ACC2)]
    card = '<table>' + ''.join(f'<tr><td style="color:{c}">{a}</td><td style="color:{c};text-align:left;font-weight:600">{b_}</td></tr>' for a, b_, c in rows) + '</table>'
    return spec('me-design-u5-L1', 'Lubricants<br>&amp; Bearing<br>Types', 'Is 55.6 cSt the same as 55.6 Pa·s?',
                f'cSt is {g_("KINEMATIC")}, Pa·s is<br>{c_("DYNAMIC")}: ν = μ/ρ',
                'one gearbox oil, two units', card, o,
                [ch('left', 300, 'g', 'μ = 0.05 Pa·s'), ch('left', 364, 'c', 'ρ = 900 kg/m³'),
                 ch('right', 300, 'c', 'film 0.1 mm', False), ch('right', 500, 'g', f'τ = {f(tau, 0)} Pa, F = {f(F, 0)} N')],
                f"ν = 0.05/900 = 5.556 × 10<sup>−5</sup> m²/s = {gl(f(cst, 1) + ' cSt')}<br>"
                f"τ = μU/h = 0.05 × 20 000 = {cl(f(tau, 0) + ' Pa')}; F = τA = {f(F, 0)} N")


def u5_L2():
    """5.3 worked example 1: D 50 mm, radial clearance c 0.05 mm, eccentricity ratio 0.6"""
    D_, c, eps = 50, .05, .6
    e = eps * c; h0 = c - e
    assert (f(e, 2), f(h0, 2), f(h0 * 1000, 0), f(c * (1 - eps), 2)) == ('0.03', '0.02', '20', '0.02')
    yc, zc, Rb = 4.0, 2.6, 1.75
    cx = .34                                              # clearance drawn far larger than life
    ex = eps * cx
    att = math.radians(-60)                               # journal centre sits below and to one side
    jy, jz = yc + ex * math.cos(att), zc + ex * math.sin(att)
    xf = 4.6
    o = [box(3.2, 1.4, xf - 3.2, 5.2, 4.6, 'iron')]
    o.append(f'<polygon points="{pts(*outline("x", xf, (yc, zc), Rb))}" fill="#0E1418"/>')
    o.append(cylinder('x', xf - .4, 7.6, (jy, jz), Rb - cx, 'steel'))
    hp = P(xf, yc + (Rb - .02) * math.cos(att), zc + (Rb - .02) * math.sin(att))
    o.append(f'<circle cx="{hp[0]:.1f}" cy="{hp[1]:.1f}" r="6" fill="{ACC}"/>')
    o.append(lab(xf, yc + Rb * math.cos(att), zc + Rb * math.sin(att), 'h₀', ACC, 18, 'end', dx=-8, dy=26))
    gp = P(xf, yc - Rb * .72, zc + Rb * .72)
    o.append(f'<circle cx="{gp[0]:.1f}" cy="{gp[1]:.1f}" r="6" fill="{ACC2}"/>')
    o.append(arr3((6.2, jy, jz + 3.2), (6.2, jy, jz + 1.55), INK, 6))
    o.append(lab(6.2, jy, jz + 2.6, 'W', INK, 18, 'start', dx=12))
    # card: the end view, gap enlarged
    cx2, cy2, R2, c2 = 82, 70, 58, 16
    e2 = eps * c2
    jx, jy2 = cx2 + e2 * math.cos(math.radians(60)), cy2 + e2 * math.sin(math.radians(60))
    s = (f'<circle cx="{cx2}" cy="{cy2}" r="{R2}" fill="#0E1418" stroke="#97A3AE" stroke-width="4"/>'
         f'<circle cx="{jx:.1f}" cy="{jy2:.1f}" r="{R2 - c2}" fill="#B7C2CC"/>'
         f'<circle cx="{cx2}" cy="{cy2}" r="3" fill="{ACC2}"/><circle cx="{jx:.1f}" cy="{jy2:.1f}" r="3" fill="#1E252C"/>'
         f'<line x1="{cx2}" y1="{cy2}" x2="{jx:.1f}" y2="{jy2:.1f}" stroke="{ACC}" stroke-width="2.5"/>'
         + t_(190, 30, 'c = 0.05 mm', 'pt', ACC2) + t_(316, 30, '(radial: R − r)', 'ax', MUTE, 'start', 13)
         + t_(190, 60, f'e = εc = 0.6 × 0.05 = {f(e, 2)} mm', 'pt', INK)
         + t_(190, 90, f'h₀ = c − e = {f(h0, 2)} mm = {f(h0 * 1000, 0)} μm', 'pt', ACC)
         + t_(190, 120, 'diametral = 2c: never use it as c', 'ax', MUTE, 'start', 14, 600)
         + t_(cx2, 142, 'gap enlarged', 'ax', MUTE, 'middle', 12))
    card = svg(s)
    return spec('me-design-u5-L2', 'Journal Bearings<br>&amp; the Sommerfeld<br>Number', 'Is clearance c radial or diametral?',
                f'c is the {g_("RADIAL")} gap:<br>h₀ = c(1 − ε) = {c_("20 μm")}',
                'journal in its bush', card, o,
                [ch('left', 300, 'c', 'D = 50 mm'), ch('left', 364, 'g', 'c = 0.05 mm, radial'), ch('left', 470, 'c', 'ε = 0.6'),
                 ch('right', 300, 'c', f'e = εc = {f(e, 2)} mm', False), ch('right', 500, 'g', f'h₀ = {f(h0 * 1000, 0)} μm')],
                f"e = εc = 0.6 × 0.05 = {cl(f(e, 2) + ' mm')}<br>"
                f"h₀ = c − e = 0.05 − 0.03 = {gl(f(h0, 2) + ' mm = 20 μm')}", tsize=62)


def u5_L3():
    """5.6 worked example 1: C = 30 kN, P = 6 kN, ball bearing, 1500 rpm"""
    C, Pk, n = 30, 6, 1500
    L10 = (C / Pk) ** 3; Lh = L10 * 1e6 / (60 * n)
    assert (f(L10, 0), f(Lh, 1)) == ('125', '1388.9')
    yc, zc = 4.0, 2.55
    x0, x1 = 3.5, 4.3
    o = [cylinder('x', .5, x0, (yc, zc), .72, 'steel'), cylinder('x', x0, x1, (yc, zc), 2.3, 'steel', hole=1.85),
         cylinder('x', x0, x1, (yc, zc), 1.15, 'iron', hole=.72)]
    rb, nb = .32, 10
    balls = []
    for k in range(nb):
        a = 2 * math.pi * k / nb + .2
        bx, by = P(x1 - .4, yc + 1.5 * math.cos(a), zc + 1.5 * math.sin(a))
        balls.append((by, f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="{rb * 33:.1f}" fill="url(#ball)"/>'))
    o.append('<defs><radialGradient id="ball" cx=".35" cy=".3" r=".75"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".5" stop-color="#C9D2DA"/><stop offset="1" stop-color="#56626E"/></radialGradient></defs>')
    o += [b for _, b in sorted(balls)]
    o.append(f'<path d="M{pts(*outline("x", x1, (yc, zc), 2.3))}Z M{pts(*outline("x", x1, (yc, zc), 1.85))}Z" fill="#D3DAE1" fill-rule="evenodd"/>')
    o.append(f'<path d="M{pts(*outline("x", x1, (yc, zc), 1.15))}Z M{pts(*outline("x", x1, (yc, zc), .72))}Z" fill="#97A3AE" fill-rule="evenodd"/>')
    o.append(cylinder('x', x1, 7.4, (yc, zc), .72, 'steel'))
    o.append(arr3((x0 + .4, yc, zc + 4.1), (x0 + .4, yc, zc + 2.45), ACC, 7, True))
    o.append(lab(x0 + .4, yc, zc + 3.6, 'P = 6 kN', ACC, 16, 'start', dx=14))
    X = lambda p_: 60 + (p_ - 3) / 12 * 380
    Y = lambda l_: 124 - l_ / 1000 * 116
    cur = ' '.join(f'{X(p_):.1f},{Y((C / p_) ** 3):.1f}' for p_ in [3 + i * .1 for i in range(121)])
    s = (f'<line x1="{X(3)}" y1="{Y(0)}" x2="{X(15)}" y2="{Y(0)}" stroke="{AXC}" stroke-width="1.5"/>'
         f'<line x1="{X(3)}" y1="{Y(0)}" x2="{X(3)}" y2="6" stroke="{AXC}" stroke-width="1.5"/>'
         f'<polyline points="{cur}" fill="none" stroke="{ACC2}" stroke-width="3.5"/>'
         f'<line x1="{X(6)}" y1="{Y(0)}" x2="{X(6)}" y2="{Y(L10):.1f}" stroke="{ACC}" stroke-width="2" stroke-dasharray="5 4"/>'
         f'<circle cx="{X(6)}" cy="{Y(L10):.1f}" r="6" fill="{ACC}"/>'
         + t_(X(6) + 12, Y(L10) - 8, f'{f(L10, 0)} million rev at 6 kN', 'pt', ACC)
         + t_(X(3) + 10, 18, '(30/P)³, million rev', 'ax', ACC2, 'start', 14, 600)
         + ''.join(t_(X(v), 140, str(v), 'ax', MUTE, 'middle') for v in (3, 6, 9, 12, 15)) + t_(X(15), Y(0) - 8, 'P, kN', 'ax', MUTE, 'end'))
    card = svg(s)
    return spec('me-design-u5-L3', 'Design Charts<br>&amp; Bearing Life', 'How many hours will this bearing last?',
                f'Life = (C/P)³, then divide<br>by {g_("REVS")} per {c_("HOUR")}',
                'pump bearing, C = 30 kN', card, o,
                [ch('left', 300, 'c', 'C = 30 kN'), ch('left', 364, 'g', 'P = 6 kN'), ch('left', 470, 'c', '1500 rpm'),
                 ch('right', 300, 'c', f'L₁₀ = {f(L10, 0)} M rev', False), ch('right', 500, 'g', f'≈ {f(Lh, 0)} hours')],
                f"L₁₀ = (30/6)³ = 5³ = {cl(f(L10, 0) + ' million rev')}<br>"
                f"125 × 10⁶ ÷ (60 × 1500) = {gl(f(Lh, 1) + ' h')}")


def u5_L4():
    """5.8 worked example 1: gasket ID 300, OD 320, m 2, y 11 MPa, p 2 MPa, bolts 138 MPa"""
    di, do, m, y, p, sb = 300, 320, 2.0, 11, 2, 138
    N = (do - di) / 2; b = N / 2; G = (di + do) / 2
    Wm2 = math.pi * b * G * y; H = math.pi / 4 * G * G * p; Hp = 2 * math.pi * b * G * m * p; Wm1 = H + Hp
    Am = Wm1 / sb; each = Am / 16
    assert (f(Wm2, 0), f(H, 0), f(Hp, 0), f(round(H) + round(Hp), 0), f(Am, 0), f(each, 1)) == ('53\u2009564', '150\u2009954', '38\u2009956', '189\u2009910', '1376', '86.0')
    xc = yc = 4.6                                                  # cover lifted off to show the gasket on the flange
    o = [cylinder('z', 0, 1.0, (xc, yc), 1.9, 'iron'), cylinder('z', 1.0, 1.3, (xc, yc), 2.4, 'iron'),
         cylinder('z', 1.3, 1.45, (xc, yc), 2.0, 'orange', hole=1.72)]
    o.append(lab(xc + 2.0, yc - 1.2, 1.4, 'gasket 300/320', ACC, 15, 'start', dx=10))
    o.append(cylinder('z', 2.35, 2.7, (xc, yc), 2.4, 'steel'))
    heads = []
    for k in range(16):
        a_ = 2 * math.pi * k / 16
        bx, by = xc + 2.18 * math.cos(a_), yc + 2.18 * math.sin(a_)
        heads.append((bx + by, cylinder('z', 2.7, 2.9, (bx, by), .14, 'dark')))
    o += [h_ for _, h_ in sorted(heads)]
    X = lambda v: 120 + v / 225_000 * 290
    s = (f'<rect x="120" y="20" width="{X(Wm2) - 120:.1f}" height="28" rx="4" fill="{ACC2}" fill-opacity=".85"/>'
         f'<rect x="120" y="78" width="{X(H) - 120:.1f}" height="28" rx="4" fill="{ACC}" fill-opacity=".85"/>'
         f'<rect x="{X(H):.1f}" y="78" width="{X(Wm1) - X(H):.1f}" height="28" rx="4" fill="{ACC}" fill-opacity=".45"/>'
         + t_(110, 40, 'seating', 'ax', INK, 'end', 15, 600) + t_(110, 98, 'operating', 'ax', INK, 'end', 15, 600)
         + t_(X(Wm2) + 8, 40, f'W<tspan dy="4" font-size="12">m2</tspan><tspan dy="-4"> = {f(Wm2 / 1000, 1)} kN</tspan>', 'pt', ACC2)
         + t_(X(H) / 2 + 60, 125, f'H = {f(H / 1000, 1)}', 'ax', ACC, 'middle', 13, 700)
         + t_(X(H) + 2, 125, f'+ H<tspan dy="4" font-size="10">p</tspan><tspan dy="-4"> = {f(Hp / 1000, 1)}</tspan>', 'ax', ACC, 'start', 13, 700)
         + t_(462, 98, f'{f(Wm1 / 1000, 1)} kN', 'pt', ACC, 'end'))
    card = svg(s)
    return spec('me-design-u5-L4', 'Choosing<br>Bearings, Seals<br>&amp; Gaskets', 'Which bolt load sizes a gasket joint?',
                f'The {g_("LARGER")} of seating and<br>operating: here {c_("OPERATING")}',
                'bolted cover with a gasket', card, o,
                [ch('left', 300, 'c', 'G = 310 mm, b = 5 mm'), ch('left', 470, 'c', 'm = 2, y = 11 MPa'), ch('right', 364, 'c', 'p = 2 MPa'),
                 ch('right', 300, 'g', f'W<sub>m1</sub> = {f(Wm1 / 1000, 1)} kN', False), ch('right', 500, 'c', '16 × M14 bolts')],
                f"Seating {cl(f(Wm2 / 1000, 1) + ' kN')}, operating {gl(f(Wm1 / 1000, 1) + ' kN')} governs<br>"
                f"A<sub>m</sub> = {f(Am, 0)} mm² → 16 bolts of M14", tsize=66)


# ================================================================ unit 6
def u6_L1():
    """6.3 worked example 2: B-section V-belt, groove 38 deg, mu 0.2, arc 2.462 rad, 0.19 kg/m, 300 N, 10.56 m/s"""
    mu, beta, th, mass, Tmax, v = .2, 19, 2.462, .19, 300, 10.56
    mup = mu / math.sin(math.radians(beta)); ev = math.exp(mup * th); ef = math.exp(mu * th)
    Tc = mass * v * v; T1 = Tmax - Tc; T2 = T1 / ev; Pw = (T1 - T2) * v
    kw = math.floor(Pw / 10) / 100              # book: 2295 W = 2.29 kW (cut, not rounded)
    assert f(Pw, 0) == '2295'
    assert (f(math.sin(math.radians(beta)), 4), f(mup, 3), f(ev, 2), f(ef, 2), f(Tc, 1), f(T1, 1), f(T2, 1), f(kw, 2)) == ('0.3256', '0.614', '4.54', '1.64', '21.2', '278.8', '61.4', '2.29')
    tb = math.tan(math.radians(beta))
    ytop0, ytop1, ztop, depth = 2.75, 5.25, 2.9, 2.1
    half_top = (ytop1 - ytop0) / 2; ym = (ytop0 + ytop1) / 2
    half_bot = half_top - depth * tb
    rim = [(1.4, ztop - 2.9), (1.4, ztop), (ytop0, ztop), (ym - half_bot, ztop - depth), (ym + half_bot, ztop - depth), (ytop1, ztop), (6.6, ztop), (6.6, ztop - 2.9)]
    zb0, zb1 = ztop - depth + .55, ztop + .55                  # belt: clear of the groove bottom, wedged on the sides
    hw = lambda z: half_top - (ztop - z) * tb
    belt = [(ym - hw(zb0), zb0), (ym + hw(zb0), zb0), (ym + hw(zb1), zb1), (ym - hw(zb1), zb1)]
    xs0, xs1 = 1.0, 6.6
    def quad(p0, p1, col, x0=xs0, x1=xs1):
        return f'<polygon points="{pts(P(x0, *p0), P(x0, *p1), P(x1, *p1), P(x1, *p0))}" fill="{col}" stroke="{col}" stroke-width=".8"/>'
    # painter order for a view from +x, +y, above: rim top (near side), groove wall that faces the viewer, groove floor,
    # belt top and its upper +y flank, rim top (far side), rim +y side, then the two front sections
    o = [quad(rim[1], rim[2], '#7D8995'), quad(rim[2], rim[3], '#4E5964'), quad(rim[3], rim[4], '#3A434C'),
         quad(belt[3], belt[2], '#D07A3A', xs0 + .02, xs1 + .02), quad(belt[2], (ym + hw(ztop), ztop), '#9A5526', xs0 + .02, xs1 + .02),
         quad(rim[5], rim[6], '#7D8995'), quad(rim[6], rim[7], '#56626E')]
    o.append(f'<polygon points="{pts(*[P(xs1, a, b_) for a, b_ in rim])}" fill="#C9D2DA" stroke="#8E9AA6" stroke-width="1.5"/>')
    o.append(f'<polygon points="{pts(*[P(xs1 + .02, a, b_) for a, b_ in belt])}" fill="#FFB988" stroke="#B8642A" stroke-width="1.2"/>')
    xf = xs1 + .03
    for side in (-1, 1):                                   # wall reactions, normal to each wall, pushing into the belt
        zz = (zb0 + ztop) / 2 - .15
        yy = ym + side * hw(zz)
        ny, nz = -side * math.cos(math.radians(beta)), math.sin(math.radians(beta))
        o.append(arr3((xf, yy - ny * 1.1, zz - nz * 1.1), (xf, yy + ny * .05, zz + nz * .05), ACC2, 5))
    gb = P(xf, ym, ztop - depth + .27)
    o.append(lab(xf, ym, ztop - depth + .27, 'clear', ACC2, 15, dy=5))
    o.append(lab(xf, ym, zb1, 'V-belt', ACC, 16, dy=-10))
    o.append(lab(xf, ytop1 + .25, ztop - 1.0, '38° groove', INK, 15, 'end', dx=-4))
    s = hbars([('flat belt', ef, ACC2, f'e<tspan dy="-7" font-size="12">μθ</tspan><tspan dy="7"> = {f(ef, 2)}</tspan>'),
               ('V-belt', ev, ACC, f'e<tspan dy="-7" font-size="12">μ′θ</tspan><tspan dy="7"> = {f(ev, 2)}</tspan>')], 110, 330, 20, 44, 5, 26, vx=462)
    s += t_(235, 132, f'μ′ = μ/sin 19° = 0.2/0.3256 = {f(mup, 3)}', 'pt', INK, 'middle')
    card = svg(s)
    return spec('me-design-u6-L1', 'Flat &amp;<br>V-belt Drives', 'Does a V-belt grip on its bottom face?',
                f'It grips on its {g_("SIDES")}:<br>the bottom stays {c_("CLEAR")}',
                'B-section belt in its groove', card, o,
                [ch('left', 300, 'c', 'groove 38°, μ = 0.2'), ch('left', 470, 'c', 'arc θ = 2.462 rad'),
                 ch('right', 300, 'g', f'μ′ = {f(mup, 3)}', False), ch('right', 500, 'g', f'{f(kw, 2)} kW per belt')],
                f"μ′ = 0.2/sin 19° = {gl(f(mup, 3))} → e<sup>μ′θ</sup> = {f(ev, 2)} (flat: {f(ef, 2)})<br>"
                f"({f(T1, 1)} − {f(T2, 1)}) × {v} = {cl(f(kw, 2) + ' kW')} per belt")


def u6_L2():
    """6.4 worked example: 08B chain p 12.7, Z1 19, Z2 38, C about 500 mm"""
    p, Z1, Z2, C0 = 12.7, 19, 38, 500
    d1 = p / math.sin(math.radians(180 / Z1)); d2 = p / math.sin(math.radians(180 / Z2))
    a = 2 * C0 / p; b = (Z1 + Z2) / 2; cc = ((Z2 - Z1) / (2 * math.pi)) ** 2
    Lp = a + b + cc * p / C0
    links = math.ceil(Lp); links += links % 2
    A_ = links - b; C = p / 4 * (A_ + math.sqrt(A_ * A_ - 8 * cc))
    assert (f(d1, 2), f(d2, 2), f(Lp, 2), links, f(C, 1)) == ('77.16', '153.79', '107.47', 108, '503.4')
    sc = 5.0 / C                                        # sprockets drawn larger than to scale
    r1, r2 = .95, 1.9
    c1, c2 = (5.9, 2.4), (2.3, 5.4)
    zc = 1.15
    def prof(z):
        return lambda a_: 1 + .09 * max(0, math.cos(a_ * z)) ** 3
    o = [cylinder('z', 0, zc, c2, .25, 'steel'), cylinder('z', 0, zc, c1, .2, 'steel'),
         cylinder('z', zc - .22, zc, c2, r2, 'iron', prof=prof(Z2)), cylinder('z', zc - .22, zc, c1, r1, 'steel', prof=prof(Z1))]
    # the chain: an open loop around both pitch circles, rollers at equal spacing
    dx, dy = c1[0] - c2[0], c1[1] - c2[1]; Lc = math.hypot(dx, dy)
    ang = math.atan2(dy, dx); al = math.asin((r2 - r1) / Lc)
    path = []
    for t in [i / 60 for i in range(61)]:
        th_ = ang + math.pi / 2 + al - t * (math.pi + 2 * al)
        path.append((c1[0] + r1 * 1.05 * math.cos(th_), c1[1] + r1 * 1.05 * math.sin(th_)))
    for t in [i / 120 for i in range(121)]:
        th_ = ang - math.pi / 2 - al - t * (math.pi - 2 * al)
        path.append((c2[0] + r2 * 1.05 * math.cos(th_), c2[1] + r2 * 1.05 * math.sin(th_)))
    path.append(path[0])
    seg = [P(x, y, zc + .05) for x, y in path]
    o.append(f'<polyline points="{pts(*seg)}" fill="none" stroke="#5E6A76" stroke-width="9" stroke-linejoin="round"/>')
    o.append(f'<polyline points="{pts(*seg)}" fill="none" stroke="{ACC}" stroke-width="5" stroke-dasharray="2 7" stroke-linecap="round"/>')
    o.append(lab(c1[0], c1[1], zc, f'Z₁ = {Z1}', INK, 15, dy=6))
    o.append(lab(c2[0], c2[1], zc, f'Z₂ = {Z2}', INK, 15, dy=6))
    X = lambda v: 40 + (v - 106.5) / 2 * 390
    s = (f'<line x1="{X(106.6)}" y1="64" x2="{X(108.4)}" y2="64" stroke="{AXC}" stroke-width="2"/>'
         f'<circle cx="{X(107)}" cy="64" r="8" fill="{ACC2}" fill-opacity=".5"/><circle cx="{X(108)}" cy="64" r="10" fill="{ACC}"/>'
         f'<line x1="{X(Lp):.1f}" y1="48" x2="{X(Lp):.1f}" y2="80" stroke="{INK}" stroke-width="3"/>'
         + t_(X(Lp), 38, f'L = {f(Lp, 2)} pitches', 'pt', INK, 'middle')
         + t_(X(107), 100, '107: odd', 'pt', ACC2, 'middle') + t_(X(107), 120, 'needs an offset link', 'ax', ACC2, 'middle', 13)
         + t_(X(108), 100, '108: even', 'pt', ACC, 'middle') + t_(X(108), 120, f'C = {f(C, 1)} mm', 'ax', ACC, 'middle', 13)
         + arrow(X(Lp) + 8, 64, X(108) - 14, 64, ACC, 3))
    card = svg(s)
    return spec('me-design-u6-L2', 'Chain Drives<br>&amp; Wire Ropes', 'Odd or even number of chain links?',
                f'Round up to an {g_("EVEN")} count:<br>odd needs an {c_("OFFSET")} link',
                '08B chain, 19 and 38 teeth', card, o,
                [ch('left', 300, 'c', 'p = 12.7 mm'), ch('left', 470, 'c', 'C ≈ 500 mm'),
                 ch('right', 300, 'g', f'{links} links', False), ch('right', 500, 'c', f'C = {f(C, 1)} mm')],
                f"L = 78.74 + 28.5 + 0.23 = {f(Lp, 2)} → {gl(str(links) + ' links')}<br>"
                f"exact centre distance {cl('C = ' + f(C, 1) + ' mm')}")


# ================================================================ unit 7
def gear_prof(z, add=.06, ded=.07):
    def pr(a):
        ph = (a * z / (2 * math.pi)) % 1
        d = abs(ph - .5) * 2                              # 0 at tooth centre, 1 at the gap centre
        return 1 + (add if d < .35 else -ded if d > .65 else add - (d - .35) / .3 * (add + ded))
    return pr


def u7_L1():
    """7.3 worked example 2: Buckingham check of m 4, b 40, z 20/60, 300 BHN; harden to 380 BHN"""
    Sb, Ft, v, Cs, e, Cc, b = 10_896, 1989, 5.027, 1.25, .015, 11_400, 40
    Fd_base = Cc * e * b + Ft
    Fd = 21 * v * Fd_base / (21 * v + math.sqrt(Fd_base)); Feff = Cs * Ft + Fd
    nb = Sb / Feff; Q = 2 * 60 / 80; K3 = .16 * 3 ** 2; Sw = b * Q * 80 * K3; nw = Sw / Feff
    K38 = .16 * 3.8 ** 2; Sw38 = b * Q * 80 * K38; nw38 = Sw38 / Feff
    # book prints F_eff = 7158 N; 1.25 × 1989 + 4671 = 7157.25, so the board shows F_d and the factors only
    assert (f(Fd, 0), f(Feff, 0), f(nb, 2), f(Sw, 0), f(nw, 2), f(K38, 2), f(round(Sw38, -1), 0), f(nw38, 2)) == ('4671', '7157', '1.52', '6912', '0.97', '2.31', '11\u2009090', '1.55')
    rg, rp = 2.15, 2.15 / 3
    cg = (2.5, 5.3)
    dirx, diry = 1 / math.sqrt(2), -1 / math.sqrt(2)
    cp = (cg[0] + (rg + rp) * dirx, cg[1] + (rg + rp) * diry)
    a0 = math.atan2(diry, dirx)
    def rot(pr, ph): return lambda a: pr(a - ph)
    zt0, zt1 = .5, 1.2
    o = [cylinder('z', 0, zt0, cg, .4, 'steel'), cylinder('z', 0, zt0, cp, .3, 'steel'),
         cylinder('z', zt0, zt1, cg, rg, 'steel', prof=rot(gear_prof(60, .045, .055), a0 + math.pi / 60))]
    o.append(cylinder('z', zt0, zt1, cp, rp, 'iron', prof=rot(gear_prof(20, .14, .16), a0 + math.pi)))
    case = outline('z', zt1, cp, rp, prof=rot(gear_prof(20, .14, .16), a0 + math.pi), n=240)
    o.append(f'<polygon points="{pts(*case)}" fill="none" stroke="{ACC}" stroke-width="5" stroke-linejoin="round"/>')
    o.append(lab(cp[0], cp[1], zt1, 'pinion', INK, 15, dy=6))
    o.append(lab(cg[0], cg[1], zt1, 'gear', INK, 16, dy=6))
    o.append(lab(cp[0] + rp, cp[1] + rp, zt1, 'hard case', ACC, 15, 'start', dx=10, dy=20))
    s = hbars([('bending', nb, ACC2, f(nb, 2)), ('wear, 300 BHN', nw, ACC, f(nw, 2)), ('wear, 380 BHN', nw38, ACC2, f(nw38, 2))],
              140, 380, 8, 36, 1.8, 24, limit=(1.5, 'needed 1.5'), vx=462)
    card = svg(s)
    return spec('me-design-u7-L1', 'Gears,<br>Materials &amp;<br>Spur Design', 'Should gear teeth be hard right through?',
                f'Hard {g_("CASE")} for wear,<br>tough {c_("CORE")} for bending',
                'spur pair, m = 4, b = 40 mm', card, o,
                [ch('left', 300, 'c', 'z = 20 and 60'), ch('left', 470, 'c', f'F<sub>d</sub> = {f(Fd, 0)} N'),
                 ch('right', 300, 'g', f'wear {f(nw, 2)} at 300 BHN', False), ch('right', 500, 'c', f'380 BHN: {f(nw38, 2)}')],
                f"Bending factor {cl(f(nb, 2))}, wear factor only {gl(f(nw, 2))}<br>"
                f"At 380 BHN: K = {f(K38, 2)}, wear factor {f(nw38, 2)}")


def u7_L2():
    """7.6 worked example 1: single-start worm, m 5, q 10, 40-tooth wheel, 1440 rpm"""
    z1, m, q, z2, N = 1, 5, 10, 40, 1440
    d1 = q * m; d2 = m * z2; a = (d1 + d2) / 2; L = z1 * math.pi * m; lam = math.degrees(math.atan(z1 / q))
    v1 = math.pi * d1 / 1000 * N / 60; vs = v1 / math.cos(math.radians(lam))
    assert (d1, d2, f(a, 0), f(L, 3), f(lam, 3), f(v1, 3), f(vs, 3)) == (50, 200, '125', '15.708', '5.711', '3.770', '3.789')
    u = 2.1 / (d2 / 2)
    xc, zc = 4.2, 2.35
    rw, rwm = d2 / 2 * u, d1 / 2 * u
    o = [cylinder('y', 3.4, 4.4, (xc, zc), .35, 'steel'),
         cylinder('y', 4.4, 4.4 + 40 * u, (xc, zc), rw, 'bronze', prof=gear_prof(z2, .05, .06)),
         cylinder('y', 4.4 + 40 * u, 6.6, (xc, zc), .35, 'steel')]
    ym, zw = 4.4 + 20 * u, zc + a * u
    o.append(cylinder('x', .8, 7.2, (ym, zw), rwm, 'steel'))
    th = []
    for i in range(int(6.4 / (L * u) * 24)):
        t0 = .8 + i * L * u / 24; a_ = 2 * math.pi * i / 24
        th.append((t0, a_))
    segs = []
    for (t0, a0_), (t1, a1_) in zip(th, th[1:]):
        if math.cos(a0_) + math.sin(a0_) > .15:
            p0 = P(t0, ym + (rwm + .02) * math.cos(a0_), zw + (rwm + .02) * math.sin(a0_))
            p1 = P(t1, ym + (rwm + .02) * math.cos(a1_), zw + (rwm + .02) * math.sin(a1_))
            segs.append(f'<line x1="{p0[0]:.1f}" y1="{p0[1]:.1f}" x2="{p1[0]:.1f}" y2="{p1[1]:.1f}" stroke="#56626E" stroke-width="3"/>')
    o.append(''.join(segs))
    o.append(lab(7.2, ym + rwm, zw - rwm, 'worm', ACC, 16, 'start', dx=6, dy=18))
    o.append(lab(xc, 4.4 + 40 * u, zc, 'wheel', INK, 16, dy=6))
    rows = [('worm', f'd₁ = qm = 10 × 5 = {d1} mm', ACC), ('not', f'm z₁ = 1 × 5 = 5 mm', MUTE),
            ('wheel', f'd₂ = m z₂ = 5 × 40 = {d2} mm', ACC2), ('centres', f'a = (50 + 200)/2 = {f(a, 0)} mm', INK)]
    card = '<table>' + ''.join(f'<tr><td style="color:{c}">{a_}</td><td style="color:{c};text-align:left;font-weight:600{";text-decoration:line-through" if a_ == "not" else ""}">{b_}</td></tr>' for a_, b_, c in rows) + '</table>'
    return spec('me-design-u7-L2', 'Helical,<br>Bevel &amp;<br>Worm Gears', "Is a worm's pitch diameter m times z?",
                f'Worm: d₁ = {g_("q × m")};<br>m × z belongs to the {c_("WHEEL")}',
                'single-start worm drive', card, o,
                [ch('left', 300, 'c', 'z₁ = 1, m = 5 mm'), ch('left', 364, 'c', 'q = 10, z₂ = 40'),
                 ch('right', 300, 'g', f'd₁ = qm = {d1} mm', False), ch('right', 500, 'c', f'd₂ = mz₂ = {d2} mm')],
                f"d₁ = qm = {gl(str(d1) + ' mm')}; d₂ = mz₂ = {cl(str(d2) + ' mm')}<br>"
                f"a = 125 mm · tan λ = 1/10 → λ = {f(lam, 2)}°")


def u7_L3():
    """7.9 worked example 1: six speeds from 100 rpm with phi = 1.41"""
    nmin, phi = 100, 1.41
    sp = [nmin * phi ** k for k in range(6)]
    std = [100, 140, 200, 280, 400, 560]
    rng = sp[-1] / sp[0]
    assert [f(v, 1) for v in sp] == ['100.0', '141.0', '198.8', '280.3', '395.3', '557.3'] and f(rng, 2) == '5.57'
    o = []
    for k, v in enumerate(sp):
        x, y = 1.7 + k * 1.05, 3.4 - k * .35
        h = v / 560 * 3.4
        o.append(box(x, y, .75, .75, h, 'orange' if k in (0, 5) else 'steel'))
    for k in range(5):
        x0_, y0_ = 1.7 + k * 1.05 + .75, 3.4 - k * .35 + .4
        h0 = sp[k] / 560 * 3.4
        o.append(arr3((x0_ - .1, y0_, h0 + .35), (x0_ + .4, y0_ - .2, sp[k + 1] / 560 * 3.4 + .25), ACC2, 3))
    o.append(lab(1.7 + .37, 3.4 + .37, sp[0] / 560 * 3.4, '100', ACC, 16, dy=-8))
    o.append(lab(1.7 + 5 * 1.05 + .37, 3.4 - 5 * .35 + .37, sp[5] / 560 * 3.4, '557.3', ACC, 16, dy=-8))
    o.append(lab(4.4, 5.6, 0, 'five steps of × 1.41', ACC2, 16, dy=10))
    X = lambda n: 40 + (math.log(n) - math.log(90)) / (math.log(620) - math.log(90)) * 400
    s = f'<line x1="{X(92)}" y1="70" x2="{X(610)}" y2="70" stroke="{AXC}" stroke-width="2"/>'
    for k, v in enumerate(sp):
        s += f'<circle cx="{X(v):.1f}" cy="70" r="{9 if k in (0, 5) else 7}" fill="{ACC if k in (0, 5) else ACC2}"/>'
        s += t_(X(v), 98, f(v, 1).replace('.0', '') if k < 2 else f(v, 1), 'pt', ACC if k in (0, 5) else INK, 'middle')
        s += t_(X(v), 118, str(std[k]), 'ax', MUTE, 'middle')
        if k < 5:
            xm = (X(v) + X(sp[k + 1])) / 2
            s += f'<path d="M{X(v) + 8:.1f},60 Q{xm:.1f},34 {X(sp[k + 1]) - 8:.1f},60" fill="none" stroke="{ACC2}" stroke-width="2"/>'
            s += t_(xm, 36, '×1.41', 'ax', ACC2, 'middle', 13, 700)
    s += t_(X(92), 138, 'rpm (log scale); standard values below', 'ax', MUTE, 'start', 12)
    card = svg(s)
    return spec('me-design-u7-L3', 'Gear Trains,<br>Gear Life &amp;<br>Gearboxes', 'Six speeds: five steps or six?',
                f'Six speeds, {g_("FIVE")} steps:<br>range = φ⁵ = {c_("5.57")}',
                'six-speed spindle, φ = 1.41', card, o,
                [ch('left', 300, 'c', 'n<sub>min</sub> = 100 rpm'), ch('left', 364, 'g', 'φ = 1.41'),
                 ch('right', 300, 'g', f'range φ⁵ = {f(rng, 2)}', False), ch('right', 500, 'c', f'n<sub>max</sub> = {f(sp[-1], 1)} rpm')],
                f"n = 100 × 1.41<sup>k</sup>, k = 0 … 5 → {cl(f(sp[-1], 1) + ' rpm')} at the top<br>"
                f"R<sub>n</sub> = 557.3/100 = {gl(f(rng, 2) + ' = φ⁵')}: five steps")


def specs():
    return [u1_L1(), u1_L2(), u1_L3(), u2_L1(), u2_L2(), u3_L1(), u3_L2(), u3_L3(), u4_L1(), u4_L2(), u4_L3(), u4_L4(), u4_L5(),
            u5_L1(), u5_L2(), u5_L3(), u5_L4(), u6_L1(), u6_L2(), u7_L1(), u7_L2(), u7_L3()]
