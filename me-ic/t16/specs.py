"""t16 split-blueprint specs for Internal Combustion Engines (me-ic, Auto look), one per lesson.
Every number is computed here from that lesson's own book worked example (books/mech/me-ic/me-ic-u<N>.html on main),
in the book's units and wording. Build: python3 t16_split.py build specs.py <out dir>."""
import math, os, sys
TOOL = os.environ.get('T16_TOOL', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tool'))
sys.path.insert(0, os.path.abspath(TOOL))
import t16_split as T
B = T.B
P, pts, box, cyl, arrow = T.P, T.pts, T.box, T.cyl, T.arrow

D = 'auto'
AC, AC2 = T.DEPTS[D]['acc'], T.DEPTS[D]['acc2']          # silver (class gold), sky blue (class cyan)
SUBJ = 'IC ENGINES'
DIM, AX, INK = '#9AA6B2', '#6B7B8A', '#E6ECF1'
HOT, FLAME = '#FFB06A', '#FF8A4C'                          # heat / flame on the board only


def g(v, n=None):
    return f'{v:g}' if n is None else f'{v:.{n}f}'


def hu(v, n):
    """round half up, as the book does (5.625 -> 5.63)"""
    from decimal import Decimal, ROUND_HALF_UP
    return f'{Decimal(repr(v)).quantize(Decimal(1).scaleb(-n), ROUND_HALF_UP)}'


def setup():
    B.U, B.OX, B.OY = 33, 952, 318


DEFS = ('<defs>'
        '<linearGradient id="al" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6B7682"/><stop offset=".4" stop-color="#E4E9EE"/>'
        '<stop offset=".65" stop-color="#AEB8C2"/><stop offset="1" stop-color="#525C67"/></linearGradient>'
        '<linearGradient id="dk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#262C33"/><stop offset=".45" stop-color="#4A535D"/>'
        '<stop offset="1" stop-color="#1B2026"/></linearGradient>'
        '<linearGradient id="hz" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5C6672"/><stop offset=".5" stop-color="#C9D2DA"/>'
        '<stop offset="1" stop-color="#4A535D"/></linearGradient>'
        '<radialGradient id="fl" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFE2A8"/><stop offset=".6" stop-color="#FF9A4C" stop-opacity=".8"/>'
        '<stop offset="1" stop-color="#FF7A30" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="bl" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#BFE8FF"/><stop offset=".6" stop-color="#6FCBFF" stop-opacity=".7"/>'
        '<stop offset="1" stop-color="#6FCBFF" stop-opacity="0"/></radialGradient>'
        '</defs>')


# ------------------------------------------------------------------ board drawing helpers (page coordinates)
def lbl(x, y, t, col=INK, size=15, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="capl" fill="{col}" style="font-size:{size}px">{t}</text>'


def shadow(cx, cy, rx, ry):
    return f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx}" ry="{ry}" fill="#000" opacity=".4"/>'


def can(cx, cy, rx, ry, h, fill='url(#al)', top='#D7DEE4', rings=0, ring_col='#5E6974'):
    s = shadow(cx, cy + 4, rx + 6, ry + 4) + cyl(cx, cy, rx, ry, h, fill, top)
    for k in range(rings):
        y = cy - h * (k + 1) / (rings + 1)
        s += f'<path d="M{cx - rx:.1f},{y:.1f} A{rx},{ry} 0 0 0 {cx + rx:.1f},{y:.1f}" fill="none" stroke="{ring_col}" stroke-width="1.8"/>'
    return s


def barrel(cx, cy, rx, ry, h, crown=.35, fins=0, glow=None):
    """an engine cylinder: a metal barrel open at the top, the piston crown visible inside at depth crown*h"""
    s = can(cx, cy, rx, ry, h, rings=fins)
    s += f'<ellipse cx="{cx:.1f}" cy="{cy - h:.1f}" rx="{rx - 4}" ry="{ry - 2}" fill="#14181D"/>'
    s += f'<ellipse cx="{cx:.1f}" cy="{cy - h + crown * h * .25:.1f}" rx="{rx - 7}" ry="{ry - 4}" fill="#7B8692"/>'
    if glow:
        s += f'<ellipse cx="{cx:.1f}" cy="{cy - h:.1f}" rx="{rx - 6}" ry="{ry - 3}" fill="url(#{glow})" opacity=".95"/>'
    return s


def plug(cx, y, s=1.0):
    """a spark plug standing with its tip at y"""
    return (f'<rect x="{cx - 3 * s:.1f}" y="{y - 10 * s:.1f}" width="{6 * s:.1f}" height="{10 * s:.1f}" fill="#8C96A0"/>'
            f'<polygon points="{cx - 9 * s:.1f},{y - 10 * s:.1f} {cx + 9 * s:.1f},{y - 10 * s:.1f} {cx + 9 * s:.1f},{y - 20 * s:.1f} {cx - 9 * s:.1f},{y - 20 * s:.1f}" fill="#AEB8C2"/>'
            f'<rect x="{cx - 6 * s:.1f}" y="{y - 46 * s:.1f}" width="{12 * s:.1f}" height="{26 * s:.1f}" rx="{4 * s:.1f}" fill="#F1F4F7"/>'
            f'<rect x="{cx - 2.5 * s:.1f}" y="{y - 54 * s:.1f}" width="{5 * s:.1f}" height="{9 * s:.1f}" fill="#7B8692"/>')


def injector(cx, y, s=1.0, col='#AEB8C2'):
    """a slim injector body with its nozzle tip at y"""
    return (f'<rect x="{cx - 7 * s:.1f}" y="{y - 58 * s:.1f}" width="{14 * s:.1f}" height="{40 * s:.1f}" rx="{3 * s:.1f}" fill="{col}"/>'
            f'<rect x="{cx - 4 * s:.1f}" y="{y - 20 * s:.1f}" width="{8 * s:.1f}" height="{18 * s:.1f}" fill="#7B8692"/>'
            f'<polygon points="{cx - 4 * s:.1f},{y - 2 * s:.1f} {cx + 4 * s:.1f},{y - 2 * s:.1f} {cx:.1f},{y + 3 * s:.1f}" fill="#5E6974"/>'
            f'<rect x="{cx - 10 * s:.1f}" y="{y - 66 * s:.1f}" width="{20 * s:.1f}" height="{10 * s:.1f}" rx="{3 * s:.1f}" fill="#3A424C"/>')


def pipe3(path, z, col='#6B7682', w=12, glow=None, gw=4):
    pl = pts(*[P(a, b, z) for a, b in path])
    s = f'<polyline points="{pl}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'
    if glow:
        s += f'<g filter="url(#gl)"><polyline points="{pl}" fill="none" stroke="{glow}" stroke-width="{gw}" stroke-linejoin="round" stroke-linecap="round"/></g>'
    return s


def flow_arrow(a, b, z, col, w=4):
    (x0, y0), (x1, y1) = P(*a, z), P(*b, z)
    return f'<g filter="url(#gl)">{arrow(x0, y0, x1, y1, col, w)}</g>'


def bolts():
    s = ''
    for a, b in ((.35, .35), (7.65, .35), (.35, 7.65), (7.65, 7.65)):
        x, y = P(a, b)
        s += f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="7" ry="4" fill="#5A504D" stroke="#120F0E" stroke-width="1.5"/>'
    return s


def board(parts):
    setup()
    return T.iso_board(D, [DEFS, bolts()] + parts)


# ------------------------------------------------------------------ card helpers (470 x 144 SVG)
def svg(s):
    return f'<svg width="470" height="144" viewBox="0 0 470 144">{s}</svg>'


def vbars(items, top_val, x0=40, x1=440, base=118, h=88, bw=86, note=''):
    """items: (axis label, value, value text, colour, dashed)"""
    s = f'<line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="{AX}" stroke-width="1.5"/>'
    n = len(items)
    for i, (lab, v, vt, col, dash) in enumerate(items):
        cx = x0 + (x1 - x0) * (i + .5) / n
        bh = h * v / top_val
        y = base - bh
        if dash:
            s += f'<rect x="{cx - bw / 2:.1f}" y="{y:.1f}" width="{bw}" height="{bh:.1f}" rx="8" fill="none" stroke="{col}" stroke-width="2" stroke-dasharray="6 5"/>'
        else:
            s += f'<rect x="{cx - bw / 2:.1f}" y="{y:.1f}" width="{bw}" height="{bh:.1f}" rx="8" fill="{col}" opacity=".92"/>'
        s += f'<text x="{cx:.1f}" y="{y - 7:.1f}" text-anchor="middle" class="pt" fill="{col}">{vt}</text>'
        s += f'<text x="{cx:.1f}" y="{base + 18}" text-anchor="middle" class="ax">{lab}</text>'
    return s + note


TABLE_CSS = """
.scope table{border-collapse:collapse;width:100%;margin-top:4px;font:600 17px 'IBM Plex Sans';color:#E6ECF1}
.scope th{font:600 14px 'IBM Plex Sans';color:#AEB8C2;text-align:center;padding:3px 6px;border-bottom:1.5px solid rgba(200,214,226,.3)}
.scope td{text-align:center;padding:6px 6px;border-bottom:1px solid rgba(200,214,226,.16);font-size:18px}
.scope td:first-child{text-align:left;font-weight:700}.scope tr:last-child td{border-bottom:none}"""


def table(head, rows):
    h = '<table><tr>' + ''.join(f'<th>{c}</th>' for c in head) + '</tr>'
    for r, col in rows:
        h += '<tr>' + ''.join(f'<td style="color:{col}">{c}</td>' if i in (0, len(r) - 1) else f'<td>{c}</td>' for i, c in enumerate(r)) + '</tr>'
    return h + '</table>'


def chip(side, top, kind, text, pointer=True):
    return dict(side=side, top=top, kind=kind, text=text, pointer=pointer)


def spec(key, title, takeaway, card_title, card, brd, chips, summary, extra_css=''):
    return dict(key=key, title=title, takeaway=takeaway, card_title=card_title, card=card, board=brd, chips=chips,
                summary=summary, css=extra_css, tag='Book example', page_title=title.replace('<br>', ' ') + ': Auto')


# ================================================================== unit 1
def u1L1():
    # 1.1 scooter engine: SI, two-stroke, one cylinder of 150 cm3; power strokes in 1000 revolutions
    rev, vol = 1000, 150
    two, four = rev * 1, rev // 2
    # card: power strokes over 8 crank revolutions, one per rev (two-stroke) vs one per 2 rev (four-stroke)
    n = 8
    x0, x1 = 118, 452
    s = ''
    for k in range(n + 1):
        x = x0 + (x1 - x0) * k / n
        s += f'<line x1="{x:.1f}" y1="34" x2="{x:.1f}" y2="112" stroke="{AX}" stroke-width="1" stroke-dasharray="3 4"/>'
    for row, (name, every, col, y) in enumerate((('two-stroke', 1, AC, 52), ('four-stroke', 2, AC2, 92))):
        s += f'<text x="108" y="{y + 5}" text-anchor="end" class="pt" fill="{col}">{name}</text>'
        s += f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{AX}" stroke-width="1.5"/>'
        for k in range(0, n, every):
            x = x0 + (x1 - x0) * (k + .5) / n
            s += f'<circle cx="{x:.1f}" cy="{y}" r="9" fill="{col}"/>'
    s += f'<text x="{x0}" y="132" class="ax">crank revolutions: 1 power stroke per rev, or per 2 rev</text>'
    s += f'<text x="{x1}" y="22" text-anchor="end" class="ax">● = power stroke</text>'
    setup()
    cx, cy = P(5.0, 3.6)
    parts = [barrel(cx, cy, 46, 25, 118, fins=6, crown=.2), plug(cx, cy - 118 - 8, 1.1),
             lbl(cx, cy - 46, f'{vol} cm³', '#1A2028', 16)]
    # crank disc in front of the barrel, rotation arrow
    kx, ky = P(6.0, 6.4, .35)
    parts.append(f'<ellipse cx="{kx:.1f}" cy="{ky:.1f}" rx="34" ry="19" fill="url(#hz)"/><ellipse cx="{kx:.1f}" cy="{ky:.1f}" rx="8" ry="4.5" fill="#2A3038"/>')
    parts.append(f'<path d="M{kx - 40:.1f},{ky - 4:.1f} A40,23 0 0 1 {kx + 34:.1f},{ky - 16:.1f}" fill="none" stroke="{AC2}" stroke-width="3" stroke-dasharray="6 4"/>')
    return spec('me-ic-u1-L1', 'IC Engines:<br>Types &amp; Parts',
                'Two <span class="gold">STROKES</span> per cycle,<br>not two <span class="cyan">CYLINDERS</span>',
                'scooter engine, 1000 rev', svg(s), board(parts),
                [chip('left', 300, 'g', 'SI · petrol · two-stroke'), chip('left', 364, 'c', 'one cylinder, air-cooled'),
                 chip('right', 300, 'g', f'{two} power strokes'), chip('right', 470, 'c', f'four-stroke: {four}', False)],
                f'two-stroke: {rev} × 1 = <b class="gl">{two} power strokes</b><br>'
                f'four-stroke: {rev} ÷ 2 = <b class="cl">{four}</b> in {rev} rev')


def u1L2():
    # 1.3 worked example 2: two 150 cm3 singles at 5000 rev/min, imep 6 bar (4S) and 4.5 bar (2S)
    Vs, N, m4, m2 = 150e-6, 5000, 6e5, 4.5e5
    W4, W2 = m4 * Vs, m2 * Vs
    P4, P2 = W4 * N / 120 / 1000, W2 * N / 60 / 1000
    Peq = m4 * Vs * N / 60 / 1000
    ratio = P2 / P4
    assert hu(P4, 2) == '3.75' and hu(P2, 2) == '5.63' and round(ratio, 1) == 1.5 and round(Peq, 1) == 7.5
    card = svg(vbars([('four-stroke · 6 bar', P4, f'{P4:.2f} kW', DIM, False), ('two-stroke · 4.5 bar', P2, f'{hu(P2, 2)} kW', AC, False),
                      ('two-stroke if 6 bar', Peq, f'{Peq:.1f} kW', AC2, True)], Peq, h=84))
    setup()
    a, b = P(3.0, 5.0), P(5.4, 2.6)
    parts = [barrel(*a, 38, 21, 104, fins=0, crown=.35), barrel(*b, 38, 21, 104, fins=0, crown=.35, glow='bl'),
             plug(a[0], a[1] - 104 - 6), plug(b[0], b[1] - 104 - 6),
             lbl(a[0], a[1] + 34, 'four-stroke'), lbl(b[0], b[1] + 34, 'two-stroke', AC2)]
    return spec('me-ic-u1-L2', 'Four-stroke,<br>Two-stroke,<br>SI &amp; CI',
                'Not 2×: only <span class="gold">1.5×</span>, because<br>ports cut the <span class="cyan">mep</span>',
                '150 cm³ at 5000 rev/min', card, board(parts),
                [chip('left', 300, 'g', 'imep 6 bar'), chip('left', 470, 'g', f'{P4:.2f} kW'),
                 chip('right', 330, 'c', 'imep 4.5 bar'), chip('right', 470, 'c', f'{hu(P2, 2)} kW, {ratio:.1f}×')],
                f'4S: {g(W4)} J × {N / 120:.2f}/s = <b class="gl">{P4:.2f} kW</b>; 2S: {g(W2)} J × {N / 60:.2f}/s<br>'
                f'= <b class="cl">{hu(P2, 2)} kW</b>, {ratio:.1f}× (equal mep: {Peq:.1f} kW)')


def u1L3():
    # 1.6: four-cylinder four-stroke, firing order 1-3-4-2, 2400 rev/min
    n, N = 4, 2400
    th = 720 / n
    t_ms = (th / 360) / (N / 60) * 1000
    order = [1, 3, 4, 2]
    fire = {c: k * th for k, c in enumerate(order)}           # crank angle at which each cylinder fires
    strokes = ['power', 'exhaust', 'intake', 'compr.']
    cols = {'power': AC2, 'exhaust': '#6E7984', 'intake': '#3E5466', 'compr.': '#A7B2BD'}

    def stroke_at(c, ang):       # stroke the cylinder is on during [ang, ang+180)
        k = int(((ang - fire[c]) % 720) // 180)
        return strokes[k]
    first = {c: stroke_at(c, 0) for c in (1, 2, 3, 4)}
    assert first == {1: 'power', 3: 'compr.', 4: 'intake', 2: 'exhaust'} and th == 180 and t_ms == 12.5
    x0, w = 96, 88
    s = ''.join(f'<text x="{x0 + w * (k + .5):.0f}" y="16" text-anchor="middle" class="ax">{int(k * th)}–{int((k + 1) * th)}°</text>' for k in range(4))
    for r, c in enumerate((1, 2, 3, 4)):
        y = 24 + r * 27
        s += f'<text x="{x0 - 10}" y="{y + 18}" text-anchor="end" class="pt" fill="{INK}">cyl {c}</text>'
        for k in range(4):
            st = stroke_at(c, k * th)
            s += (f'<rect x="{x0 + w * k + 2}" y="{y}" width="{w - 4}" height="23" rx="5" fill="{cols[st]}" opacity="{1 if st == "power" else .85}"/>'
                  f'<text x="{x0 + w * (k + .5):.0f}" y="{y + 17}" text-anchor="middle" class="ax" fill="{"#10151A" if st in ("power", "compr.") else INK}">{st}</text>')
    s += f'<text x="{x0 + 4 * w}" y="140" text-anchor="end" class="ax">fires at 0°, 180°, 360°, 540°: 1, 3, 4, 2</text>'
    setup()
    parts = []
    # crankshaft along x, four barrels standing on it, cylinder 1 at the back
    parts.append(pipe3([(.8, 4.2), (7.8, 4.2)], .35, '#7B8692', 10))
    for i, c in enumerate((1, 2, 3, 4)):
        x, y = P(1.6 + i * 1.9, 3.4)
        st = first[c]
        parts.append(barrel(x, y, 24, 13, 80, crown=.3, glow='fl' if st == 'power' else None))
        parts.append(lbl(x, y - 96, f'{c} · {st}', AC2 if st == 'power' else INK, 15))
    return spec('me-ic-u1-L3', 'Valve Timing<br>&amp; Firing Order',
                'Four-stroke, 4 cylinders:<br><span class="gold">720°</span> ÷ 4 = <span class="cyan">180°</span>',
                'firing order 1-3-4-2', svg(s), board(parts),
                [chip('left', 430, 'g', 'firing order 1-3-4-2'), chip('left', 520, 'c', f'{N} rev/min'),
                 chip('right', 300, 'g', f'θf = {int(th)}°'), chip('right', 540, 'c', f'{g(t_ms)} ms apart', False)],
                f'θf = 720° ÷ {n} = <b class="gl">{int(th)}°</b> = 0.5 rev at {N // 60} rev/s<br>'
                f'0.5 ÷ {N // 60} = <b class="cl">{g(t_ms)} ms</b> between firings')


def u1L4():
    # 1.7: Otto r = 8, 1800 K; Diesel r = 16, cut-off 2; both from 1 bar, 300 K
    gam, cv, cp, R, T1, p1 = 1.4, .718, 1.005, .287, 300, 1.0
    r_o, T3o = 8, 1800
    T2o = T1 * r_o ** .4; p2o = p1 * r_o ** 1.4; p3o = p2o * T3o / T2o; p4o = p3o / r_o ** 1.4
    eta_o = 1 - 1 / r_o ** .4
    r_d, rho = 16, 2
    T2d = T1 * r_d ** .4; p2d = p1 * r_d ** 1.4; T3d = rho * T2d; T4d = T3d * (rho / r_d) ** .4
    qin = cp * (T3d - T2d); qout = cv * (T4d - T1); eta_d = (qin - qout) / qin
    qin_b, qout_b = round(qin, 1), round(qout, 1)        # 914.0 and 353.0 as the book prints them
    eta_o16 = 1 - 1 / r_d ** .4
    assert round(eta_o * 100, 1) == 56.5 and round(eta_d * 100, 1) == 61.4 and round(eta_o16 * 100, 1) == 67.0
    assert round(p3o, 1) == 48.0 and round(p2d, 1) == 48.5
    v1 = R * T1 / p1 / 100                                    # m3/kg (p in bar -> kPa)
    # card: p-v loops of both cycles, drawn to scale (v linear, p linear to 50 bar)
    X = lambda v: 46 + v / v1 * 400
    Y = lambda p: 124 - p / 50 * 104

    def poly(vs, ps):
        return ' '.join(f'{X(v):.1f},{Y(p):.1f}' for v, p in zip(vs, ps))
    N_ = 40
    vo2 = v1 / r_o
    comp_o = [vo2 + (v1 - vo2) * k / N_ for k in range(N_ + 1)]
    otto = ([v for v in reversed(comp_o)], [p1 * (v1 / v) ** gam for v in reversed(comp_o)])
    expo = (comp_o, [p3o * (vo2 / v) ** gam for v in comp_o])
    vd2 = v1 / r_d; vd3 = rho * vd2
    comp_d = [vd2 + (v1 - vd2) * k / N_ for k in range(N_ + 1)]
    exp_d = [vd3 + (v1 - vd3) * k / N_ for k in range(N_ + 1)]
    d_c = ([v for v in reversed(comp_d)], [p1 * (v1 / v) ** gam for v in reversed(comp_d)])
    d_e = (exp_d, [p2d * (vd3 / v) ** gam for v in exp_d])
    s = f'<line x1="46" y1="124" x2="450" y2="124" stroke="{AX}" stroke-width="1.5"/><line x1="46" y1="16" x2="46" y2="124" stroke="{AX}" stroke-width="1.5"/>'
    s += f'<polygon points="{poly(*d_c)} {poly(*d_e)}" fill="{AC2}" fill-opacity=".22" stroke="{AC2}" stroke-width="3" stroke-linejoin="round"/>'
    s += f'<polygon points="{poly(*otto)} {poly(*expo)}" fill="none" stroke="{AC}" stroke-width="2.6" stroke-dasharray="7 4" stroke-linejoin="round"/>'
    s += f'<text x="40" y="{Y(48) + 5:.1f}" text-anchor="end" class="ax">48</text><text x="40" y="128" text-anchor="end" class="ax">1</text>'
    s += f'<text x="52" y="14" class="ax">p, bar</text><text x="450" y="140" text-anchor="end" class="ax">v, m³/kg →</text>'
    s += f'<line x1="200" y1="44" x2="222" y2="44" stroke="{AC2}" stroke-width="4"/><text x="230" y="50" class="pt" fill="{AC2}">Diesel, r = 16: {eta_d * 100:.1f} %</text>'
    s += f'<line x1="200" y1="72" x2="222" y2="72" stroke="{AC}" stroke-width="4"/><text x="230" y="78" class="pt" fill="{AC}">Otto, r = 8: {eta_o * 100:.1f} %</text>'
    setup()
    a, b = P(3.4, 5.2), P(5.2, 3.4)
    parts = [barrel(*a, 34, 19, 112, crown=.55), barrel(*b, 34, 19, 112, crown=.12, glow='bl'),
             lbl(a[0], a[1] - 44, 'r 8', '#1A2028', 17), lbl(b[0], b[1] - 44, 'r 16', '#1A2028', 17)]
    return spec('me-ic-u1-L4', 'Engine Cycles:<br>Ideal to Actual',
                'Same r: <span class="gold">Otto</span> wins.<br>Same peak p: <span class="cyan">Diesel</span> wins',
                'Otto r 8 vs Diesel r 16', svg(s), board(parts),
                [chip('left', 300, 'g', f'Otto {eta_o * 100:.1f} %'), chip('left', 400, 'g', f'peak {p3o:.1f} bar'),
                 chip('right', 300, 'c', f'Diesel {eta_d * 100:.1f} %'), chip('right', 400, 'c', f'peak {p2d:.1f} bar'),
                 chip('right', 540, 'g', f'Otto at r 16: {eta_o16 * 100:.1f} %', False)],
                f'Otto, r 8: 1 − 1/8<sup>0.4</sup> = <b class="gl">{eta_o * 100:.1f} %</b> at {p3o:.1f} bar<br>'
                f'Diesel, r 16: {qin_b - qout_b:.1f} ÷ {qin_b:.1f} = <b class="cl">{eta_d * 100:.1f} %</b> at {p2d:.1f}')


# ================================================================== unit 2
def u2L1():
    # 2.1 worked example 2: simple carburettor, 7.2 kg/h petrol at A/F 15
    mf = 7.2 / 3600; AF = 15; ma = AF * mf
    p, Tk, dp, z = 101300, 300, 6500, .005
    rho_a = p / (287 * Tk)
    ua = math.sqrt(2 * dp / rho_a); At = ma / (.85 * rho_a * ua); dt = math.sqrt(4 * At / math.pi) * 1000
    dpf = dp - 750 * 9.81 * z; uf = math.sqrt(2 * dpf / 750); Af = mf / (.70 * 750 * uf); df = math.sqrt(4 * Af / math.pi) * 1000
    assert round(dt, 2) == 19.06 and round(df, 3) == 1.081 and round(ua, 1) == 105.1 and round(uf, 3) == 4.152
    card = table(['', 'flow', 'speed', 'diameter'],
                 [((f'air', f'{ma:.3f} kg/s', f'{ua:.1f} m/s', f'{dt:.1f} mm'), AC2),
                  ((f'petrol', f'{mf:.3f} kg/s', f'{uf:.2f} m/s', f'{df:.2f} mm'), AC)])
    card += f'<div style="font:600 16px IBM Plex Sans;color:#AEB8C2;padding:6px 8px 2px">air ÷ fuel = {ma:.3f} ÷ {mf:.3f} = {ma / mf:g} : 1</div>'
    setup()
    # venturi: a vertical tube pinched at the throat, a float bowl beside it, the jet into the throat
    cx, cy = P(4.6, 3.6)
    top, mid, h = 46, 22, 190
    prof = (f'M{cx - top:.1f},{cy - h:.1f} C{cx - top:.1f},{cy - h * .7:.1f} {cx - mid:.1f},{cy - h * .62:.1f} {cx - mid:.1f},{cy - h * .5:.1f} '
            f'C{cx - mid:.1f},{cy - h * .38:.1f} {cx - top:.1f},{cy - h * .3:.1f} {cx - top:.1f},{cy:.1f} L{cx + top:.1f},{cy:.1f} '
            f'C{cx + top:.1f},{cy - h * .3:.1f} {cx + mid:.1f},{cy - h * .38:.1f} {cx + mid:.1f},{cy - h * .5:.1f} '
            f'C{cx + mid:.1f},{cy - h * .62:.1f} {cx + top:.1f},{cy - h * .7:.1f} {cx + top:.1f},{cy - h:.1f}Z')
    parts = [shadow(cx, cy + 4, 56, 24), f'<path d="{prof}" fill="url(#al)"/>',
             f'<ellipse cx="{cx:.1f}" cy="{cy - h:.1f}" rx="{top}" ry="16" fill="#14181D" stroke="#C9D2DA" stroke-width="2"/>']
    for k in range(4):
        x = cx - 18 + k * 12
        parts.append(f'<g filter="url(#gl)">{arrow(x, cy - h - 34, x, cy - h - 4, AC2, 3)}</g>')
    fx, fy = P(2.0, 5.6)
    parts.append(box(1.3, 4.9, 1.5, 1.5, 1.9, '#AEB8C2', '#5E6974', '#7B8692'))
    jy = cy - h * .5
    parts.append(f'<path d="M{fx + 10:.1f},{fy - 30:.1f} L{cx - mid - 2:.1f},{jy + 2:.1f}" stroke="{AC}" stroke-width="4" fill="none"/>')
    parts.append(f'<g filter="url(#gl)"><path d="M{cx - mid + 2:.1f},{jy:.1f} q14,-10 22,-34" stroke="{AC}" stroke-width="3" fill="none"/></g>')
    parts.append(lbl(fx, fy + 26, 'float bowl'))
    parts.append(lbl(cx + 34, jy + 6, 'throat', INK, 14, 'start'))
    return spec('me-ic-u2-L1', 'Carburettors<br>&amp; Fuel<br>Injection',
                '18:1 means more <span class="gold">AIR</span><br>than 15:1, so it is <span class="cyan">LEAN</span>',
                'sizing a simple carburettor', card, board(parts),
                [chip('left', 300, 'g', '7.2 kg/h at A/F 15'), chip('left', 470, 'c', 'Δp 0.065 bar'),
                 chip('right', 330, 'c', f'throat {dt:.1f} mm'), chip('right', 470, 'g', f'jet {df:.2f} mm', False)],
                f'ρ<sub>a</sub> = {rho_a:.3f}, √(2Δp/ρ<sub>a</sub>) = {ua:.1f} m/s → <b class="cl">d<sub>t</sub> = {dt:.2f} mm</b><br>'
                f'fuel: √(2 × {dpf:.0f}/750) = {uf:.3f} m/s → <b class="gl">d<sub>f</sub> = {df:.3f} mm</b>', TABLE_CSS)


def u2L2():
    # 2.4 worked example 2: rail 1200 -> 1800 bar, cylinder 60 bar, 1.0 ms -> same 30 mm3
    pr1, pr2, pc, t1, Q = 1200, 1800, 60, 1.0, 30
    t2 = t1 * math.sqrt((pr1 - pc) / (pr2 - pc))
    Qover = Q * math.sqrt((pr2 - pc) / (pr1 - pc)); over = Qover / Q - 1
    assert round(t2, 3) == .809 and round(Qover, 1) == 37.1 and round(over * 100) == 24
    # card: open time for 30 mm3 against rail pressure
    X = lambda p: 60 + (p - 800) / 1200 * 380
    Y = lambda t: 124 - (t - .6) / .7 * 100
    curve = ' '.join(f'{X(p):.1f},{Y(t1 * math.sqrt((pr1 - pc) / (p - pc))):.1f}' for p in range(800, 2001, 25))
    s = (f'<line x1="60" y1="124" x2="446" y2="124" stroke="{AX}" stroke-width="1.5"/><line x1="60" y1="18" x2="60" y2="124" stroke="{AX}" stroke-width="1.5"/>'
         f'<polyline points="{curve}" fill="none" stroke="{AC}" stroke-width="3.2"/>')
    for p, t, col, txt, dx, dy in ((pr1, t1, AC, f'{t1:.1f} ms at {pr1}', 10, -10), (pr2, t2, AC2, f'{t2:.2f} ms at {pr2}', -10, 26)):
        s += (f'<line x1="{X(p):.1f}" y1="124" x2="{X(p):.1f}" y2="{Y(t):.1f}" stroke="{col}" stroke-width="1.6" stroke-dasharray="5 4"/>'
              f'<circle cx="{X(p):.1f}" cy="{Y(t):.1f}" r="6" fill="{col}"/>'
              f'<text x="{X(p) + dx:.1f}" y="{Y(t) + dy:.1f}" text-anchor="{"start" if dx > 0 else "end"}" class="pt" fill="{col}">{txt}</text>')
    s += (f'<text x="54" y="{Y(1.2) + 5:.1f}" text-anchor="end" class="ax">1.2</text><text x="54" y="{Y(.6) + 5:.1f}" text-anchor="end" class="ax">0.6</text>'
          f'<text x="66" y="16" class="ax">open time, ms, for {Q} mm³</text>'
          + ''.join(f'<text x="{X(p):.1f}" y="140" text-anchor="middle" class="ax">{p}</text>' for p in (800, 1200, 1600, 2000))
          + '<text x="446" y="116" text-anchor="end" class="ax">rail, bar</text>')
    setup()
    parts = [pipe3([(.6, 3.6), (6.4, 3.6)], 2.2, '#AEB8C2', 22), pipe3([(.6, 3.6), (6.4, 3.6)], 2.2, '#E4E9EE', 6)]
    for i in range(4):
        x, y = P(1.2 + i * 1.4, 3.6, 2.2)
        parts.append(f'<line x1="{x:.1f}" y1="{y + 6:.1f}" x2="{x:.1f}" y2="{y + 30:.1f}" stroke="#7B8692" stroke-width="5"/>')
        parts.append(injector(x, y + 96, .95))
        parts.append(f'<g filter="url(#gl)"><path d="M{x:.1f},{y + 99:.1f} l-9,22 M{x:.1f},{y + 99:.1f} l9,22 M{x:.1f},{y + 99:.1f} l0,24" stroke="{AC2}" stroke-width="2.4"/></g>')
    sx, sy = P(6.4, 3.6, 2.2)
    parts.append(box(6.3, 3.35, .7, .5, .5, '#6FCBFF', '#2E6F92', '#3F88B0', z0=2.0))
    parts.append(lbl(sx + 24, sy - 34, 'rail sensor', AC2, 14))
    return spec('me-ic-u2-L2', 'Diesel Injection:<br>Pumps &amp;<br>Common Rail',
                'The <span class="gold">open time</span> sets the dose;<br>higher rail p needs <span class="cyan">less</span>',
                'same 30 mm³, higher rail', svg(s), board(parts),
                [chip('left', 300, 'g', 'rail 1200 → 1800 bar'), chip('left', 470, 'c', 'cylinder 60 bar'),
                 chip('right', 330, 'c', f'{t2:.2f} ms'), chip('right', 470, 'g', f'1.0 ms → {Qover:.1f} mm³', False)],
                f't₂ = 1.0 × √({pr1 - pc} ÷ {pr2 - pc}) = <b class="cl">{t2:.3f} ms</b> for {Q} mm³<br>'
                f'left at 1.0 ms: <b class="gl">{Qover:.1f} mm³</b>, a {over * 100:.0f} % overdose', 'h1{font-stretch:86%}')


def u2L3():
    # 2.6 worked example 2: stratified mode, 2000 rpm, 12 mg at 10 mg/ms, end 35 deg bTDC
    N, mfuel, rate, end = 2000, 12, 10, 35
    t = mfuel / rate; ca = 6 * N * t / 1000; start = end + ca
    left_ms = end / (6 * N) * 1000
    assert t == 1.2 and round(ca, 1) == 14.4 and round(start, 1) == 49.4 and round(left_ms, 1) == 2.9
    X = lambda a: 440 - a / 60 * 400          # a in degrees before TDC
    s = f'<line x1="{X(60)}" y1="80" x2="{X(0)}" y2="80" stroke="{AX}" stroke-width="2"/>'
    for a in range(0, 61, 10):
        s += f'<line x1="{X(a):.1f}" y1="74" x2="{X(a):.1f}" y2="86" stroke="{AX}" stroke-width="1.5"/><text x="{X(a):.1f}" y="110" text-anchor="middle" class="ax">{a}°</text>'
    s += f'<rect x="{X(start):.1f}" y="62" width="{X(end) - X(start):.1f}" height="32" rx="6" fill="{AC}" opacity=".9"/>'
    s += f'<text x="{(X(start) + X(end)) / 2:.1f}" y="50" text-anchor="middle" class="pt" fill="{AC}">inject {t:g} ms = {ca:.1f}°</text>'
    s += f'<rect x="{X(end):.1f}" y="66" width="{X(0) - X(end):.1f}" height="28" rx="6" fill="{AC2}" opacity=".25"/>'
    s += f'<text x="{(X(end) + X(0)) / 2:.1f}" y="50" text-anchor="middle" class="pt" fill="{AC2}">cloud forms</text>'
    s += f'<text x="{X(0):.1f}" y="124" text-anchor="middle" class="pt" fill="{INK}">TDC</text><text x="{X(60):.1f}" y="124" text-anchor="start" class="ax">degrees before TDC</text>'
    setup()
    cx, cy = P(4.6, 4.6)
    h = 104
    parts = [barrel(cx, cy, 64, 34, h, crown=.15)]
    # lean haze over the whole bore, a rich cloud at the plug
    parts.append(f'<ellipse cx="{cx:.1f}" cy="{cy - h:.1f}" rx="58" ry="29" fill="{AC2}" opacity=".16"/>')
    parts.append(f'<ellipse cx="{cx + 16:.1f}" cy="{cy - h - 10:.1f}" rx="32" ry="18" fill="url(#bl)"/>')
    parts.append(injector(cx - 34, cy - h - 2, 1.15))
    parts.append(f'<g filter="url(#gl)"><path d="M{cx - 32:.1f},{cy - h + 2:.1f} q22,8 40,-10" stroke="{AC}" stroke-width="3.5" fill="none"/></g>')
    parts.append(plug(cx + 16, cy - h - 26, 1.25))
    parts.append(lbl(cx + 16, cy - h + 22, 'rich', '#0E2233', 15))
    parts.append(lbl(cx, cy - 40, 'lean overall', '#1A2028', 16))
    return spec('me-ic-u2-L3', 'Petrol<br>Injection:<br>EFI &amp; GDI',
                '<span class="gold">RICH</span> at the plug,<br><span class="cyan">LEAN</span> overall',
                'stratified at 2000 rpm', svg(s), board(parts),
                [chip('left', 300, 'g', f'{mfuel} mg petrol'), chip('left', 470, 'c', f'{rate} mg per ms'),
                 chip('right', 300, 'g', f'{t:g} ms = {ca:.1f}°'), chip('right', 470, 'c', f'start {start:.1f}° bTDC', False)],
                f'{mfuel} ÷ {rate} = <b class="gl">{t:g} ms</b>; 6 × {N} × {t / 1000:g} = <b class="gl">{ca:.1f}°</b><br>'
                f'start = {end}° + {ca:.1f}° = <b class="cl">{start:.1f}° bTDC</b>, {left_ms:.1f} ms to TDC')


def u2L4():
    # 2.7: nozzle, 5 holes of 0.25 mm, Cd 0.7, 700 bar into 60 bar
    n, d, Cd, rho, rho_a = 5, .25e-3, .7, 830, 20
    dp = (700 - 60) * 1e5
    A1 = math.pi * d ** 2 / 4; A = n * A1
    m = Cd * A * math.sqrt(2 * rho * dp); u = m / (rho * A)
    tb = 28.65 * rho * d / math.sqrt(rho_a * dp)
    S = 2.95 * (dp / rho_a) ** .25 * math.sqrt(d * .5e-3) * 1000
    A_wrong = n * math.pi * d ** 2
    assert round(A * 1e6, 3) == .245 and round(m, 4) == .056 and round(u) == 275 and round(S, 1) == 44.1 and round(tb * 1e3, 3) == .166
    s = vbars([('π d²/4 × 5', A * 1e6, f'{A * 1e6:.3f} mm²', AC, False), ('π d² × 5 (wrong)', A_wrong * 1e6, f'{A_wrong * 1e6:.3f} mm²', DIM, True)],
              A_wrong * 1e6, x0=20, x1=250, bw=70, h=78)
    # right half: tip penetration vs the bowl radius
    s += (f'<line x1="270" y1="118" x2="460" y2="118" stroke="{AX}" stroke-width="1.5"/>'
          f'<rect x="280" y="74" width="{S / 50 * 170:.1f}" height="20" rx="5" fill="{AC2}"/>'
          f'<line x1="{280 + 35 / 50 * 170:.1f}" y1="62" x2="{280 + 35 / 50 * 170:.1f}" y2="112" stroke="{AC}" stroke-width="2.5" stroke-dasharray="5 4"/>'
          f'<text x="280" y="54" class="pt" fill="{AC2}">tip {S:.0f} mm at 0.5 ms</text>'
          f'<text x="{280 + 35 / 50 * 170:.1f}" y="136" text-anchor="middle" class="ax">bowl wall 35 mm</text>')
    setup()
    cx, cy = P(4.0, 4.0, .3)
    parts = [shadow(cx, cy + 10, 120, 62),
             f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="118" ry="60" fill="url(#hz)"/>',
             f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="76" ry="39" fill="#20262D" stroke="{AC}" stroke-width="2" stroke-dasharray="6 4"/>']
    for k in range(n):
        a = math.pi * 2 * k / n + .5
        ex, ey = cx + 96 * math.cos(a), cy + 49 * math.sin(a)
        parts.append(f'<g filter="url(#gl)"><line x1="{cx:.1f}" y1="{cy - 6:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{AC2}" stroke-width="4" stroke-linecap="round"/></g>')
    parts.append(injector(cx, cy - 6, 1.1))
    parts.append(lbl(cx, cy + 82, 'bowl radius 35 mm', AC))
    return spec('me-ic-u2-L4', 'Nozzles,<br>Sprays &amp;<br>Governors',
                'One hole is <span class="gold">πd²/4</span>;<br>then times <span class="cyan">5</span> holes',
                '5-hole nozzle at 700 bar', svg(s), board(parts),
                [chip('left', 300, 'g', f'{n} holes × 0.25 mm'), chip('left', 470, 'c', 'Δp = 640 bar'),
                 chip('right', 300, 'g', f'{m:.3f} kg/s'), chip('right', 470, 'c', f'{u:.0f} m/s jets', False)],
                f'A = {n} × π(0.25)²/4 = <b class="gl">{A * 1e6:.3f} mm²</b>; ṁ = <b class="gl">{m:.3f} kg/s</b><br>'
                f'tip {S:.0f} mm at 0.5 ms passes the <b class="cl">35 mm</b> bowl wall')


def u2L5():
    # 2.9 worked example 2: coil L 6 mH, R 3 ohm, 12 V; dwell 54 deg per cylinder, 4-lobe cam
    L, R, V, dwell = 6e-3, 3, 12, 54
    I, tau = V / R, L / R
    res = {}
    for N in (3000, 6000):
        td = dwell / (6 * N / 2)
        i = I * (1 - math.exp(-td / tau)); E = .5 * L * i ** 2
        res[N] = (td * 1e3, i, E * 1e3)
    assert [round(res[3000][1], 2), round(res[3000][2], 1), round(res[6000][1], 2), round(res[6000][2], 1)] == [3.80, 43.3, 3.11, 29.0]
    X = lambda t: 50 + t / 8 * 380
    Y = lambda i: 122 - i / 4 * 96
    curve = ' '.join(f'{X(t / 10):.1f},{Y(I * (1 - math.exp(-t / 10 / (tau * 1e3)))):.1f}' for t in range(0, 81))
    s = (f'<line x1="50" y1="122" x2="440" y2="122" stroke="{AX}" stroke-width="1.5"/><line x1="50" y1="18" x2="50" y2="122" stroke="{AX}" stroke-width="1.5"/>'
         f'<line x1="50" y1="{Y(4):.1f}" x2="440" y2="{Y(4):.1f}" stroke="{AX}" stroke-width="1" stroke-dasharray="4 4"/>'
         f'<text x="44" y="{Y(4) + 5:.1f}" text-anchor="end" class="ax">4 A</text><text x="44" y="126" text-anchor="end" class="ax">0</text>'
         f'<polyline points="{curve}" fill="none" stroke="{AC}" stroke-width="3.2"/>')
    for N, col, dy, dx, anc in ((6000, AC2, 26, 10, 'start'), (3000, AC, 30, 10, 'start')):
        td, i, E = res[N]
        s += (f'<line x1="{X(td):.1f}" y1="122" x2="{X(td):.1f}" y2="{Y(i):.1f}" stroke="{col}" stroke-width="1.6" stroke-dasharray="5 4"/>'
              f'<circle cx="{X(td):.1f}" cy="{Y(i):.1f}" r="6" fill="{col}"/>'
              f'<text x="{X(td) + dx:.1f}" y="{Y(i) + dy:.1f}" text-anchor="{anc}" class="pt" fill="{col}">{N} rpm: {i:.2f} A</text>'
              f'<text x="{X(td):.1f}" y="139" text-anchor="middle" class="ax">{td:g} ms</text>')
    s += '<text x="440" y="139" text-anchor="end" class="ax">dwell time</text><text x="58" y="16" class="ax">primary current</text>'
    setup()
    parts = []
    # battery (left), coil (centre), breaker (front right), plug (back right); the primary loop glows
    parts.append(box(.9, 4.6, 1.6, 2.2, 1.2, '#3A424C', '#1B2026', '#262C33'))
    bx, by = P(1.7, 5.7, 1.2)
    parts.append(lbl(bx, by + 6, '12 V', AC))
    loop = [(2.5, 5.7), (3.9, 5.7), (3.9, 4.6), (6.0, 4.6), (6.0, 6.4), (2.5, 6.4)]
    parts.append(pipe3(loop, .05, '#3A424C', 7, glow=AC, gw=4))
    cx, cy = P(3.9, 3.9)
    parts.append(can(cx, cy, 30, 16, 110, rings=8, ring_col='#B07A40'))
    parts.append(lbl(cx - 40, cy - 40, 'coil', INK, 15, 'end'))
    kx, ky = P(6.0, 5.4, .1)
    parts.append(f'<rect x="{kx - 30:.1f}" y="{ky - 10:.1f}" width="60" height="16" rx="4" fill="#C9D2DA"/>'
                 f'<circle cx="{kx - 6:.1f}" cy="{ky - 12:.1f}" r="4" fill="#5E6974"/>'
                 f'<line x1="{kx - 4:.1f}" y1="{ky - 12:.1f}" x2="{kx + 26:.1f}" y2="{ky - 30:.1f}" stroke="{AC2}" stroke-width="5" stroke-linecap="round"/>')
    parts.append(lbl(kx + 30, ky + 20, 'breaker', AC2, 14, 'start'))
    px, py = P(6.4, 1.6, .2)
    ht = [(cx, cy - 110), ((cx + px) / 2, cy - 140), (px, py - 56)]
    parts.append(f'<path d="M{ht[0][0]:.1f},{ht[0][1]:.1f} Q{ht[1][0]:.1f},{ht[1][1]:.1f} {ht[2][0]:.1f},{ht[2][1]:.1f}" fill="none" stroke="#B9C3CC" stroke-width="3" stroke-dasharray="2 5"/>')
    parts.append(plug(px, py, 1.1))
    return spec('me-ic-u2-L5', 'Ignition<br>Systems &amp;<br>Spark Timing',
                'The breaker cuts the <span class="gold">PRIMARY</span>,<br>not the <span class="cyan">secondary</span>',
                'coil dwell at two speeds', svg(s), board(parts),
                [chip('left', 300, 'g', 'L 6 mH, R 3 Ω'), chip('left', 470, 'c', 'dwell 54°'),
                 chip('right', 300, 'g', f'{res[3000][2]:.1f} mJ'), chip('right', 470, 'c', f'{res[6000][2]:.1f} mJ at 6000', False)],
                f'i = 4(1 − e<sup>−t/2 ms</sup>): {res[3000][0]:g} ms → <b class="gl">{res[3000][1]:.2f} A, {res[3000][2]:.1f} mJ</b><br>'
                f'6000 rpm: {res[6000][0]:g} ms → <b class="cl">{res[6000][1]:.2f} A, {res[6000][2]:.1f} mJ</b>, a third less')


# ================================================================== unit 3
def u3L1():
    # 3.2 worked example 2: cylindrical flame r 35 mm, disc 10.75 mm deep, 6 m/s into 12 kg/m3
    r, h, rho, St, N = .035, .01075, 12, 6, 3000
    Af = 2 * math.pi * r * h; mb = rho * Af * St
    per_deg = mb / (6 * N) * 1e6                    # mg per degree
    fuel = per_deg / 15.7; Q = fuel * 1e-6 * 44e6
    dpdth = .35 * Q / 62.4e-6 / 1e5
    assert round(Af * 1e3, 3) == 2.364 and round(mb, 3) == .170 and round(per_deg, 2) == 9.46 and round(fuel, 3) == .602
    assert round(Q, 1) == 26.5 and round(dpdth, 2) == 1.49
    steps = [('A, 10⁻³ m²', f'{Af * 1e3:.3f}', INK), ('ṁ, kg/s', f'{mb:.3f}', AC), ('fuel, mg/°', f'{fuel:.3f}', INK),
             ('heat, J/°CA', f'{Q:.1f}', AC), ('bar/°CA', f'{dpdth:.2f}', AC2)]
    s = ''
    for k, (a, b, col) in enumerate(steps):
        x = 8 + k * 92
        s += (f'<rect x="{x}" y="34" width="84" height="72" rx="10" fill="rgba(255,255,255,.05)" stroke="{col}" stroke-width="1.6"/>'
              f'<text x="{x + 42}" y="58" text-anchor="middle" class="ax">{a}</text>'
              f'<text x="{x + 42}" y="88" text-anchor="middle" class="pt" fill="{col}" style="font-size:19px">{b}</text>')
        if k < len(steps) - 1:
            s += f'<path d="M{x + 85} 70h6" stroke="{AX}" stroke-width="2"/>'
    s += f'<text x="235" y="128" text-anchor="middle" class="ax">per degree: {mb:.3f} ÷ 18 000 °/s = {per_deg:.2f} mg of charge</text>'
    setup()
    cx, cy = P(4.0, 4.0, .2)
    parts = [shadow(cx, cy + 8, 150, 78), cyl(cx, cy + 14, 142, 74, 14, 'url(#hz)', '#2A3038'),
             f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="96" ry="50" fill="url(#fl)" opacity=".9"/>',
             f'<g filter="url(#gl)"><ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="96" ry="50" fill="none" stroke="{FLAME}" stroke-width="4"/></g>',
             plug(cx, cy - 4, 1.1)]
    for a in (.3, 1.4, 2.6, 3.9, 5.1):
        x0, y0 = cx + 100 * math.cos(a), cy + 52 * math.sin(a)
        parts.append(arrow(x0, y0, cx + 128 * math.cos(a), cy + 66 * math.sin(a), AC2, 3.5))
    parts.append(lbl(cx, cy + 96, 'flame r = 35 mm, 10.75 mm deep'))
    return spec('me-ic-u3-L1', 'SI Combustion<br>&amp; Flame Speed',
                'The front moves <span class="gold">6 m/s</span>:<br><span class="cyan">26.5 J</span> each crank degree',
                'flame front near TDC', svg(s), board(parts),
                [chip('left', 300, 'g', f'S = {St} m/s'), chip('left', 470, 'c', f'unburnt {rho} kg/m³'),
                 chip('right', 300, 'g', f'{mb:.3f} kg/s burns'), chip('right', 470, 'c', f'{dpdth:.2f} bar/°CA', False)],
                f'ṁ = {rho} × {Af * 1e3:.3f}×10⁻³ × {St} = <b class="gl">{mb:.3f} kg/s</b><br>'
                f'<b class="gl">{Q:.1f} J/°CA</b> of heat → dp/dθ = <b class="cl">{dpdth:.2f} bar/°CA</b>')


def u3L2():
    # 3.4: flame 20 mm from the end gas at 25 m/s; delay 0.6 ms (present fuel) and 1.0 ms (higher octane)
    N, dist, Sf, bore, c = 3000, .020, 25, .086, 950
    dpm = .006 * N
    t_fl = dist / Sf * 1000; a_fl = t_fl * dpm
    a_A, a_B = .6 * dpm, 1.0 * dpm
    f = 1.84 * c / (math.pi * bore); per = 1 / f * 1000 * dpm
    assert round(a_fl, 1) == 14.4 and round(a_A, 1) == 10.8 and a_B == 18 and round(f, -1) == 6470 and round(per, 1) == 2.8
    X = lambda a: 30 + a / 20 * 420
    s = f'<line x1="{X(0)}" y1="78" x2="{X(20)}" y2="78" stroke="{AX}" stroke-width="2"/>'
    for a in range(0, 21, 5):
        s += f'<line x1="{X(a):.1f}" y1="72" x2="{X(a):.1f}" y2="84" stroke="{AX}" stroke-width="1.5"/><text x="{X(a):.1f}" y="102" text-anchor="middle" class="ax">{a}°</text>'
    s += f'<rect x="{X(0)}" y="70" width="{X(a_fl) - X(0):.1f}" height="16" rx="4" fill="{FLAME}" opacity=".35"/>'
    for a, col, txt, y in ((a_A, AC2, f'end gas fires {a_A:.1f}°', 30), (a_fl, FLAME, f'flame {a_fl:.1f}°', 54), (a_B, AC, f'95: {a_B:g}°', 30)):
        s += (f'<line x1="{X(a):.1f}" y1="{y + 6}" x2="{X(a):.1f}" y2="78" stroke="{col}" stroke-width="2.4"/><circle cx="{X(a):.1f}" cy="78" r="6" fill="{col}"/>'
              f'<text x="{X(a):.1f}" y="{y}" text-anchor="middle" class="pt" fill="{col}">{txt}</text>')
    s += f'<text x="{X(0)}" y="126" class="ax">degrees after TDC · {N} rev/min = {dpm:g} °/ms</text>'
    s = s.replace('95: ', 'high octane ')
    setup()
    cx, cy = P(4.0, 4.0, .2)
    parts = [shadow(cx, cy + 8, 150, 78), cyl(cx, cy + 14, 142, 74, 14, 'url(#hz)', '#2A3038')]
    # flame from the plug (left) and end gas (right), 20 mm apart
    px = cx - 70
    parts.append(f'<ellipse cx="{px + 10:.1f}" cy="{cy:.1f}" rx="92" ry="54" fill="url(#fl)"/>')
    parts.append(f'<g filter="url(#gl)"><path d="M{px + 70:.1f},{cy - 44:.1f} Q{px + 104:.1f},{cy:.1f} {px + 70:.1f},{cy + 44:.1f}" fill="none" stroke="{FLAME}" stroke-width="4"/></g>')
    parts.append(f'<ellipse cx="{cx + 100:.1f}" cy="{cy:.1f}" rx="34" ry="30" fill="url(#bl)"/>')
    parts.append(f'<g filter="url(#gl)">{arrow(px + 108, cy, cx + 62, cy, INK, 3)}</g>')
    parts.append(plug(px - 30, cy - 4, 1.0))
    parts.append(lbl(cx + 100, cy + 52, 'end gas', AC2))
    parts.append(lbl(cx + 8, cy - 22, '20 mm', INK, 14))
    return spec('me-ic-u3-L2', 'Gasoline,<br>Cycle Scatter<br>&amp; Knock',
                'End gas fires <span class="gold">before</span> the<br>flame arrives: <span class="cyan">knock</span>',
                'flame race in the bore', svg(s), board(parts),
                [chip('left', 300, 'g', f'{dist * 1000:g} mm at {Sf} m/s'), chip('left', 470, 'c', 'delay 0.6 ms'),
                 chip('right', 300, 'g', f'{f / 1000:.1f} kHz ringing'), chip('right', 470, 'c', 'higher octane: no knock', False)],
                f'flame: {dist * 1000:g} ÷ {Sf} = {t_fl:g} ms = <b class="gl">{a_fl:.1f}°</b> after TDC<br>'
                f'end gas: 0.6 ms = <b class="cl">{a_A:.1f}°</b>, first: it knocks')


def u3L3():
    # 3.5 worked example 1: five changes and their effect on knock
    rows = [('r 8 → 10', 'density', '↑', AC), ('spark 15° → 25° bTDC', 'density', '↑', AC),
            ('1500 → 3000 rev/min', 'time', '↓', AC2), ('φ 1.1 → 0.85', 'composition', '↓', AC2), ('91 → 95 RON', 'composition', '↓', AC2)]
    up = [r for r in rows if r[2] == '↑']
    assert len(up) == 2 and len(rows) == 5
    s = ''
    for k, (ch, grp, eff, col) in enumerate(rows):
        y = 10 + k * 26
        s += (f'<rect x="6" y="{y}" width="458" height="23" rx="5" fill="{col}" fill-opacity="{.16 if eff == "↑" else .06}"/>'
              f'<text x="16" y="{y + 17}" class="pt" fill="{INK}" style="font-size:16px">({"abcde"[k]}) {ch}</text>'
              f'<text x="268" y="{y + 17}" class="ax">{grp}</text>'
              f'<text x="410" y="{y + 18}" text-anchor="middle" class="pt" fill="{col}">knock {eff}</text>')
    setup()
    cx, cy = P(5.2, 3.2)
    h = 110
    parts = [barrel(cx, cy, 48, 26, h, crown=.25), plug(cx, cy - h - 8, 1.1)]
    # crank-angle dial in front: TDC mark, 15 and 25 deg bTDC marks, advance arrow
    dx, dy = P(4.4, 7.0, .2)
    R, ry = 70, 38
    parts.append(f'<ellipse cx="{dx:.1f}" cy="{dy:.1f}" rx="{R}" ry="{ry}" fill="url(#hz)"/><ellipse cx="{dx:.1f}" cy="{dy:.1f}" rx="8" ry="5" fill="#2A3038"/>')

    def mark(deg, col):
        a = math.radians(-90 - deg)
        x, y = dx + R * math.cos(a), dy + ry * math.sin(a)
        return f'<line x1="{dx:.1f}" y1="{dy:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="3.5" stroke-linecap="round"/>'
    parts += [mark(0, INK), mark(15, DIM), mark(25, AC)]
    a0, a1 = math.radians(-90 - 15), math.radians(-90 - 25)
    parts.append(f'<path d="M{dx + 1.2 * R * math.cos(a0):.1f},{dy + 1.2 * ry * math.sin(a0):.1f} A{1.2 * R},{1.2 * ry} 0 0 0 {dx + 1.2 * R * math.cos(a1):.1f},{dy + 1.2 * ry * math.sin(a1):.1f}" '
                 f'fill="none" stroke="{AC2}" stroke-width="3"/>')
    parts.append(lbl(dx + 8, dy - ry - 18, 'TDC', INK, 13, 'start'))
    parts.append(lbl(dx - 1.3 * R * .55, dy - ry - 12, '15° → 25°', AC2, 13, 'end'))
    return spec('me-ic-u3-L3', 'Knock Factors<br>&amp; CI<br>Combustion',
                'Advancing the spark <span class="gold">RAISES</span><br>knock; <span class="cyan">retard</span> cures it',
                'five changes and knock', svg(s), board(parts),
                [chip('left', 300, 'g', 'spark 15° → 25°: knock ↑'), chip('left', 390, 'g', 'r 8 → 10: knock ↑'),
                 chip('right', 300, 'c', 'faster: knock ↓'), chip('right', 470, 'c', '95 RON: knock ↓', False)],
                '<b class="gl">Increase:</b> (a) r 8 → 10, (b) spark to 25° bTDC<br>'
                '<b class="cl">Decrease:</b> (c) faster, (d) φ 0.85, (e) 95 RON', '')


def u3L4():
    # 3.7: fuel A delay 0.9 ms, fuel B 0.5 ms; 2000 rev/min; 1.6 mg/deg from 15 deg bTDC
    N, rate, inj = 2000, 1.6, 15
    dpm = .006 * N
    res = {}
    for f_, tau in (('A', .9), ('B', .5)):
        th = dpm * tau; res[f_] = (th, inj - th, rate * th)
    cut_fuel = 1 - res['B'][2] / res['A'][2]; cut_rise = 1 - 6.3 / 8.8
    assert round(res['A'][2], 1) == 17.3 and round(res['B'][2], 1) == 9.6 and round(cut_fuel * 100) == 44 and round(cut_rise * 100) == 28
    s = vbars([('fuel A · 0.9 ms', res['A'][2], f'{res["A"][2]:.1f} mg', AC, False), ('fuel B · 0.5 ms', res['B'][2], f'{res["B"][2]:.1f} mg', AC2, False)],
              res['A'][2], x0=10, x1=250, bw=78, h=70)
    s += vbars([('A', 8.8, '8.8', AC, False), ('B', 6.3, '6.3', AC2, False)], 8.8, x0=270, x1=460, bw=56, h=70)
    s += '<text x="130" y="14" text-anchor="middle" class="ax">fuel in before ignition</text><text x="365" y="14" text-anchor="middle" class="ax">steepest rise, bar/°CA</text>'
    setup()
    cx, cy = P(4.2, 3.6)
    h = 118
    parts = [barrel(cx, cy, 52, 28, h, crown=.1)]
    parts.append(f'<ellipse cx="{cx:.1f}" cy="{cy - h + 6:.1f}" rx="26" ry="12" fill="#2A3038"/>')
    for a in (-.9, -.3, .3, .9, math.pi):
        parts.append(f'<g filter="url(#gl)"><line x1="{cx:.1f}" y1="{cy - h - 6:.1f}" x2="{cx + 34 * math.sin(a):.1f}" y2="{cy - h + 4 + 10 * math.cos(a):.1f}" stroke="{AC}" stroke-width="3"/></g>')
    parts.append(injector(cx, cy - h - 6, 1.1))
    for k, (f_, col) in enumerate((('A', AC), ('B', AC2))):
        x, y = P(5.0 + k * 1.2, 7.2 - k * .6)
        parts.append(can(x, y, 20, 11, 48, fill='url(#dk)', top=col))
        parts.append(lbl(x, y + 24, f'fuel {f_}', col, 14))
    return spec('me-ic-u3-L4', 'Diesel Knock,<br>Air Motion &amp;<br>Chambers',
                'Diesel knock comes at the<br><span class="gold">START</span>: a long <span class="cyan">delay</span>',
                'two fuels, same injection', svg(s), board(parts),
                [chip('left', 300, 'g', f'A: {res["A"][0]:.1f}° delay'), chip('left', 470, 'c', f'B: {res["B"][0]:.1f}° delay'),
                 chip('right', 300, 'g', f'{rate} mg/° from {inj}°'), chip('right', 470, 'c', f'{cut_fuel * 100:.0f} % less waiting fuel', False)],
                f'A: 0.9 ms = {res["A"][0]:.1f}° → <b class="gl">{res["A"][2]:.1f} mg</b> before ignition<br>'
                f'B: 0.5 ms = {res["B"][0]:.1f}° → <b class="cl">{res["B"][2]:.1f} mg</b>; rise 8.8 → 6.3')


# ================================================================== unit 4
def u4L1():
    # 4.2 worked example 2: cap 100 kPa gauge; sea level 101.3 kPa; 2000 m 79.5 kPa (water tables)
    cap, p0, p2k = 100, 101.3, 79.5
    pa, pb, pc = p0 + cap, p2k, p2k + cap
    Ta, Tb, Tc = 120.4, 93.3, 116.8                 # saturation temperatures read from the water tables
    assert round(pa, 1) == 201.3 and round(pc, 1) == 179.5
    base = 80                                       # bars start at 80 °C so the differences show
    s = vbars([(f'cap, sea level', Ta - base, f'{Ta} °C', AC, False), ('open, 2000 m', Tb - base, f'{Tb} °C', DIM, False),
               ('cap, 2000 m', Tc - base, f'{Tc} °C', AC2, False)], 45, x1=396, h=86, bw=76)
    yr = 118 - 86 * (95 - base) / 45
    s += f'<line x1="40" y1="{yr:.1f}" x2="400" y2="{yr:.1f}" stroke="{FLAME}" stroke-width="1.8" stroke-dasharray="6 4"/>'
    s += f'<text x="406" y="{yr + 5:.1f}" class="ax" fill="{FLAME}">95 °C</text><text x="406" y="{yr + 21:.1f}" class="ax" fill="{FLAME}">running</text>'
    s += f'<text x="40" y="132" class="ax"></text><text x="460" y="14" text-anchor="end" class="ax">bars from {base} °C</text>'
    setup()
    parts = [box(1.0, 3.2, 2.8, 3.0, 1.9, '#5E6974', '#262C33', '#3A424C')]
    ex, ey = P(2.4, 4.7, 1.9)
    parts.append(lbl(ex, ey + 6, 'engine'))
    # radiator: a tall finned panel at the back right
    parts.append(box(5.6, 1.0, .6, 4.2, 3.6, '#AEB8C2', '#4A535D', '#7B8692'))
    for k in range(9):
        a, b = P(5.6, 1.3 + k * .45, .3), P(5.6, 1.3 + k * .45, 3.3)
        parts.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#2A3038" stroke-width="2"/>')
    cx, cy = P(5.9, 1.6, 3.6)
    parts.append(can(cx, cy, 16, 9, 16, fill='url(#hz)', top=AC2))
    parts.append(lbl(cx + 24, cy - 22, 'cap 100 kPa', AC2, 14, 'start'))
    parts.append(pipe3([(3.8, 3.8), (5.6, 3.8)], 1.6, '#7B8692', 10, glow=FLAME, gw=3))
    parts.append(pipe3([(3.8, 5.6), (5.6, 4.9)], .4, '#7B8692', 10, glow=AC2, gw=3))
    return spec('me-ic-u4-L1', 'Cooling &amp;<br>Lubrication',
                'The cap raises the <span class="gold">BOILING</span><br>point; the <span class="cyan">radiator</span> cools',
                'a 100 kPa radiator cap', svg(s), board(parts),
                [chip('left', 300, 'g', 'sea level 101.3 kPa'), chip('left', 470, 'c', '2000 m: 79.5 kPa'),
                 chip('right', 380, 'g', f'{Ta} °C'), chip('right', 470, 'c', f'{Tc} °C at 2000 m', False)],
                f'{p0} + {cap} = {pa:.1f} kPa → <b class="gl">{Ta} °C</b> at sea level<br>'
                f'2000 m: open {Tb} °C, capped <b class="cl">{Tc} °C</b>')


def u4L2():
    # 4.4 worked example 2: oil at 100 C, mu 12.0 mPa s, rho 840 kg/m3
    mu, rho = .0120, 840
    nu = mu / rho * 1e6
    bands = [(30, 9.3, 12.5), (40, 12.5, 16.3), (50, 16.3, 21.9)]
    band = [b for b, lo, hi in bands if lo <= nu < hi][0]
    assert round(nu, 1) == 14.3 and band == 40
    X = lambda v: 30 + (v - 8) / 15 * 410
    s = ''
    for b, lo, hi in bands:
        on = b == band
        s += (f'<rect x="{X(lo):.1f}" y="56" width="{X(hi) - X(lo) - 3:.1f}" height="34" rx="6" fill="{AC if on else "#4A535D"}" opacity="{.9 if on else .8}"/>'
              f'<text x="{(X(lo) + X(hi)) / 2:.1f}" y="79" text-anchor="middle" class="pt" fill="{"#10151A" if on else INK}">SAE {b}</text>'
              f'<text x="{X(lo):.1f}" y="110" text-anchor="middle" class="ax">{lo}</text>')
    s += f'<text x="{X(21.9):.1f}" y="110" text-anchor="middle" class="ax">21.9</text>'
    s += (f'<line x1="{X(nu):.1f}" y1="34" x2="{X(nu):.1f}" y2="54" stroke="{AC2}" stroke-width="3"/><polygon points="{X(nu) - 7:.1f},46 {X(nu) + 7:.1f},46 {X(nu):.1f},56" fill="{AC2}"/><circle cx="{X(nu):.1f}" cy="34" r="6" fill="{AC2}"/>'
          f'<text x="{X(nu) + 12:.1f}" y="30" class="pt" fill="{AC2}">ν = {nu:.1f} mm²/s</text>'
          f'<text x="30" y="132" class="ax">kinematic viscosity at 100 °C, mm²/s (hot grade bands)</text>')
    setup()
    bx, by = P(4.2, 4.4)
    parts = [shadow(bx, by + 4, 60, 30),
             f'<path d="M{bx - 50:.1f},{by - 120:.1f} V{by:.1f} A50,26 0 0 0 {bx + 50:.1f},{by:.1f} V{by - 120:.1f}" fill="rgba(200,214,226,.16)" stroke="#C9D2DA" stroke-width="2.5"/>',
             f'<path d="M{bx - 50:.1f},{by - 60:.1f} V{by:.1f} A50,26 0 0 0 {bx + 50:.1f},{by:.1f} V{by - 60:.1f} A50,26 0 0 1 {bx - 50:.1f},{by - 60:.1f}Z" fill="#B8862E" opacity=".9"/>',
             f'<ellipse cx="{bx:.1f}" cy="{by - 60:.1f}" rx="50" ry="26" fill="#D9A646"/>',
             f'<ellipse cx="{bx:.1f}" cy="{by - 120:.1f}" rx="50" ry="26" fill="none" stroke="#E4E9EE" stroke-width="2.5"/>']
    tx = bx + 18
    parts.append(f'<rect x="{tx - 5:.1f}" y="{by - 178:.1f}" width="10" height="150" rx="5" fill="#F1F4F7"/><rect x="{tx - 2.5:.1f}" y="{by - 110:.1f}" width="5" height="78" fill="{FLAME}"/>'
                 f'<circle cx="{tx:.1f}" cy="{by - 28:.1f}" r="9" fill="{FLAME}"/>')
    parts.append(lbl(tx - 12, by - 160, '100 °C', FLAME, 15, 'end'))
    parts.append(lbl(bx, by + 46, 'engine oil sample'))
    return spec('me-ic-u4-L2', 'Lubricants,<br>PCV &amp;<br>Supercharging',
                'W = <span class="gold">WINTER</span>; the 40 is<br>the <span class="cyan">hot</span> band at 100 °C',
                'used oil at 100 °C', svg(s), board(parts),
                [chip('left', 300, 'g', 'μ = 12.0 mPa·s'), chip('left', 470, 'c', 'ρ = 840 kg/m³'),
                 chip('right', 300, 'c', f'ν = {nu:.1f} mm²/s'), chip('right', 470, 'g', f'SAE {band} band', False)],
                f'ν = μ ÷ ρ = 0.0120 ÷ 840 = <b class="cl">{nu:.1f} mm²/s</b> (12.0 ÷ 0.84)<br>'
                f'12.5 ≤ {nu:.1f} &lt; 16.3: still the <b class="gl">SAE {band}</b> hot band')


def u4L3():
    # 4.8: compressor rp 1.6, eta 0.70, intercooler effectiveness 0.80 with 303 K air
    T1, rp, eta, eps, Tc = 300, 1.6, .70, .80, 303
    T2 = T1 * (1 + (rp ** (.4 / 1.4) - 1) / eta)
    d0 = rp * T1 / T2; T3 = T2 - eps * (T2 - Tc); d1 = rp * T1 / T3; gain = d1 / d0 - 1
    assert round(T2, 1) == 361.6 and round(d0, 3) == 1.327 and round(T3, 1) == 314.7 and round(d1, 3) == 1.525 and round(gain * 100) == 15
    s = vbars([(f'no intercooler · {T2:.1f} K', d0, f'{d0:.3f}', DIM, False), (f'intercooled · {T3:.1f} K', d1, f'{d1:.3f}', AC2, False)],
              1.6, h=88, bw=110)
    s += f'<text x="40" y="16" class="ax">density ratio at {rp} boost</text>'
    setup()
    parts = []
    parts.append(pipe3([(2.2, 2.2), (4.2, 2.2)], .9, '#7B8692', 12, glow=FLAME, gw=4))      # hot air to the cooler
    parts.append(pipe3([(4.9, 2.7), (4.9, 4.8)], .9, '#7B8692', 12, glow=AC2, gw=4))        # cool air to the engine
    cx, cy = P(1.8, 3.2, .1)
    parts.append(shadow(cx, cy + 6, 52, 26))
    parts.append(f'<circle cx="{cx:.1f}" cy="{cy - 40:.1f}" r="44" fill="url(#al)"/>')
    parts.append(f'<circle cx="{cx:.1f}" cy="{cy - 40:.1f}" r="18" fill="#2A3038"/><circle cx="{cx:.1f}" cy="{cy - 40:.1f}" r="7" fill="#9AA4AE"/>')
    parts.append(lbl(cx, cy + 22, f'compressor ×{rp}'))
    parts.append(box(4.2, 1.7, 1.4, 1.0, 1.8, '#AEB8C2', '#4A535D', '#7B8692'))
    for k in range(6):
        a, b = P(4.4 + k * .2, 2.7, .2), P(4.4 + k * .2, 2.7, 1.6)
        parts.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#2A3038" stroke-width="2"/>')
    ix, iy = P(4.9, 2.2, 1.8)
    parts.append(lbl(ix, iy - 14, 'intercooler'))
    parts.append(box(4.0, 4.8, 1.8, 1.8, 1.4, '#5E6974', '#262C33', '#3A424C'))
    gx, gy = P(4.9, 5.7, 1.4)
    parts.append(lbl(gx, gy + 6, 'engine'))
    return spec('me-ic-u4-L3', 'Turbochargers,<br>Intercoolers &amp;<br>Scavenging',
                'Same <span class="gold">1.6</span> boost, but<br><span class="cyan">denser</span> air: 15 % more',
                'intercooler, same boost', svg(s), board(parts),
                [chip('left', 300, 'g', f'T₂ = {T2:.1f} K'), chip('left', 470, 'c', f'ε = {eps}, air {Tc} K'),
                 chip('right', 300, 'c', f'T₃ = {T3:.1f} K'), chip('right', 470, 'g', f'+{gain * 100:.0f} % air mass', False)],
                f'T₃ = {T2:.1f} − {eps} × ({T2:.1f} − {Tc}) = <b class="cl">{T3:.1f} K</b><br>'
                f'{rp} × {T1}/{T3:.1f} = {d1:.3f} vs {d0:.3f}: <b class="gl">{d1 / d0:.3f}×</b> the air')


# ================================================================== unit 5
def u5L1():
    # 5.1: single-cylinder four-stroke 100 x 120 mm, 1500 rpm, bmep 6 bar, 2.4 kg/h, CV 43 MJ/kg, eta_m 0.85
    D_, L, N, bmep, mf_h, CV, etam = .100, .120, 1500, 6e5, 2.4, 43e6, .85
    Vd = math.pi / 4 * D_ ** 2 * L
    BP = bmep * Vd * (N / 60) / 2 / 1000
    Tq = BP * 1000 / (2 * math.pi * N / 60)
    Pf = mf_h / 3600 * CV / 1000
    eta_b = BP / Pf; IP = BP / etam; FP = IP - BP; bsfc = mf_h / BP * 1000
    assert round(BP, 2) == 7.07 and round(Tq, 1) == 45.0 and round(Pf, 2) == 28.67 and round(eta_b * 100, 1) == 24.7
    assert round(IP, 2) == 8.32 and round(FP, 2) == 1.25 and round(bsfc, 1) == 339.5
    rows = [('fuel power', Pf, DIM), ('indicated', IP, AC), ('brake', BP, AC2)]
    s = ''
    for k, (n, v, col) in enumerate(rows):
        y = 18 + k * 36
        w = v / Pf * 250
        s += (f'<text x="112" y="{y + 19}" text-anchor="end" class="pt" fill="{col}">{n}</text>'
              f'<rect x="122" y="{y}" width="{w:.1f}" height="26" rx="6" fill="{col}" opacity=".9"/>'
              f'<text x="{128 + w:.1f}" y="{y + 19}" class="pt" fill="{col}">{v:.2f} kW</text>')
    s += f'<text x="122" y="136" class="ax">friction {FP:.2f} kW · BSFC {bsfc:.1f} g/kWh · η<tspan font-size="11">b</tspan> {eta_b * 100:.1f} %</text>'
    setup()
    cx, cy = P(4.4, 3.8)
    h = 140
    parts = [barrel(cx, cy, 50, 27, h, crown=.4)]
    kx, ky = P(4.6, 6.8, .35)
    parts.append(f'<ellipse cx="{kx:.1f}" cy="{ky:.1f}" rx="40" ry="22" fill="url(#hz)"/><ellipse cx="{kx:.1f}" cy="{ky:.1f}" rx="9" ry="5" fill="#2A3038"/>')
    parts.append(f'<path d="M{kx - 46:.1f},{ky - 2:.1f} A46,26 0 1 1 {kx + 20:.1f},{ky + 25:.1f}" fill="none" stroke="{AC2}" stroke-width="3" stroke-dasharray="6 4"/>')
    parts.append(lbl(kx + 56, ky + 8, '2 rev / power stroke', AC2, 13, 'start'))
    parts.append(lbl(cx, cy - h - 34, '100 × 120 mm'))
    return spec('me-ic-u5-L1', 'Engine Power<br>&amp; Efficiency',
                'One power stroke every<br><span class="gold">2</span> revolutions: use <span class="cyan">N/2</span>',
                'single cylinder at 1500 rpm', svg(s), board(parts),
                [chip('left', 300, 'g', 'bmep 6 bar'), chip('left', 400, 'c', f'V<sub>d</sub> = {Vd * 1e3:.4f} L'),
                 chip('right', 300, 'c', f'BP {BP:.2f} kW'), chip('right', 400, 'g', f'T = {Tq:.1f} N·m', False)],
                f'BP = 6×10⁵ × {Vd * 1e4:.3f}×10⁻⁴ × (25 ÷ <b class="cl">2</b>) = <b class="gl">{BP:.2f} kW</b><br>'
                f'IP = {BP:.2f} ÷ {etam} = {IP:.2f} kW; FP = {FP:.2f} kW')


def u5L2():
    # 5.4: hydraulic dynamometer, arm 0.5 m, balance 120 N, 1500 rev/min, 1.0 L four-stroke
    arm, W, N, Vd = .5, 120, 1500, 1e-3
    Tq = W * arm; w = 2 * math.pi * N / 60; BP = Tq * w / 1000; bmep = 2 * math.pi * 2 * Tq / Vd / 1e5
    assert Tq == 60 and round(BP, 2) == 9.42 and round(bmep, 2) == 7.54
    # card: the arm as a lever, from the shaft centre to the balance
    s = (f'<circle cx="64" cy="66" r="34" fill="none" stroke="{DIM}" stroke-width="2.5"/><circle cx="64" cy="66" r="6" fill="{INK}"/>'
         f'<line x1="64" y1="66" x2="340" y2="66" stroke="{AC}" stroke-width="7" stroke-linecap="round"/>'
         f'<g>{arrow(340, 128, 340, 74, AC2, 4)}</g>'
         f'<path d="M64 40V30M340 40V30M64 35H340" stroke="{AC}" stroke-width="1.6"/>'
         f'<text x="202" y="26" text-anchor="middle" class="pt" fill="{AC}">L = {arm} m from the shaft centre</text>'
         f'<text x="354" y="112" class="pt" fill="{AC2}">W = {W} N</text>'
         f'<text x="64" y="126" text-anchor="middle" class="ax">shaft</text>'
         f'<text x="202" y="104" text-anchor="middle" class="pt" fill="{INK}">T = {W} × {arm} = {g(Tq)} N·m</text>')
    setup()
    parts = [pipe3([(.4, 4.0), (2.4, 4.0)], .9, '#7B8692', 12)]                     # shaft from the engine side
    parts.append(box(2.4, 3.0, 2.0, 2.0, 1.8, '#C9D2DA', '#5E6974', '#8C96A0'))     # casing
    hx, hy = P(3.4, 4.0, 1.8)
    parts.append(f'<ellipse cx="{hx:.1f}" cy="{hy:.1f}" rx="30" ry="16" fill="#3A424C"/><ellipse cx="{hx:.1f}" cy="{hy:.1f}" rx="10" ry="5.5" fill="#9AA4AE"/>')
    parts.append(lbl(hx, hy + 40, 'casing', '#1A2028', 15))
    parts.append(pipe3([(3.4, 4.0), (7.0, 4.0)], 1.8, AC, 8))                        # torque arm
    bx, by = P(7.0, 4.0, 1.8)
    parts.append(box(6.75, 3.75, .5, .5, 1.3, '#E4E9EE', '#8C96A0', '#B9C3CC'))      # spring balance under the arm end
    parts.append(f'<g filter="url(#gl)">{arrow(bx + 20, by - 40, bx + 20, by + 4, AC2, 4)}</g>')
    parts.append(lbl(bx - 10, by + 86, 'spring balance', INK, 14, 'end'))
    return spec('me-ic-u5-L2', 'Fuel, Air &amp;<br>Dynamometers',
                'Torque = force × the <span class="gold">ARM</span><br>from the <span class="cyan">shaft centre</span>',
                'hydraulic dynamometer', svg(s), board(parts),
                [chip('left', 300, 'g', f'arm {arm} m'), chip('left', 470, 'c', f'{N} rev/min'),
                 chip('right', 300, 'c', f'balance {W} N'), chip('right', 540, 'g', f'BP {BP:.2f} kW', False)],
                f'T = W × L = {W} × {arm} = <b class="gl">{g(Tq)} N·m</b>; ω = {w:.2f} rad/s<br>'
                f'BP = {g(Tq)} × {w:.2f} = <b class="cl">{BP:.2f} kW</b>; bmep = {bmep:.2f} bar')


def u5L3():
    # 5.5: heat balance, 3.0 kg/h at 42 MJ/kg, 10.5 kW brake, 90 kg/h air, water 8 kg/min +18 C, exhaust +400 K
    mf, CV, BPk, ma, mw, dTw, dTg, cpg = 3.0, 42, 10.5, 90, 8, 18, 400, 1.05
    Pf = mf * CV / 3.6
    Pc = mw / 60 * 4.18 * dTw
    Pe = (ma + mf) / 3600 * cpg * dTg
    Pu = Pf - BPk - Pc - Pe
    pc = [x / Pf * 100 for x in (BPk, Pc, Pe, Pu)]
    assert round(Pf, 1) == 35.0 and round(Pc, 2) == 10.03 and round(Pe, 2) == 10.85 and round(Pu, 2) == 3.62
    assert [round(x, 1) for x in pc] == [30.0, 28.7, 31.0, 10.3]
    WATER = '#4FA3D9'
    items = [('brake', BPk, pc[0], AC), ('water', Pc, pc[1], WATER), ('exhaust', Pe, pc[2], FLAME), ('other', Pu, pc[3], DIM)]
    s = ''
    x = 16
    for n, v, p, col in items:
        w = p / 100 * 438
        s += f'<rect x="{x:.1f}" y="38" width="{w - 3:.1f}" height="42" rx="6" fill="{col}" opacity=".92"/>'
        s += f'<text x="{x + w / 2:.1f}" y="65" text-anchor="middle" class="pt" fill="#10151A" style="font-size:{12 if p < 15 else 17}px">{p:.1f} %</text>'
        s += f'<text x="{x + w / 2:.1f}" y="100" text-anchor="middle" class="ax">{n}</text><text x="{x + w / 2:.1f}" y="118" text-anchor="middle" class="ax">{v:.2f} kW</text>'
        x += w
    s += f'<text x="16" y="26" class="pt" fill="{INK}">fuel power {Pf:.1f} kW = 100 %</text>'
    setup()
    parts = [pipe3([(5.0, 3.6), (7.4, 3.6)], 1.6, '#7B8692', 10, glow=FLAME, gw=4),          # exhaust (right)
             pipe3([(4.0, 5.0), (4.0, 7.2)], .6, '#7B8692', 8, glow=WATER, gw=3),            # cooling water (front right)
             pipe3([(2.4, 5.0), (1.4, 6.6)], .9, '#7B8692', 12)]                             # shaft to the brake (front left)
    parts.append(box(2.0, 2.6, 3.0, 2.4, 2.0, '#5E6974', '#262C33', '#3A424C'))
    ex, ey = P(3.5, 3.8, 2.0)
    parts.append(lbl(ex, ey + 6, 'engine'))
    parts.append(box(.9, 6.2, 1.0, 1.0, 1.4, '#C9D2DA', '#5E6974', '#8C96A0'))
    for (a, b, c), t, col, anc in (((7.5, 3.6, 1.6), 'exhaust', FLAME, 'start'), ((4.0, 7.4, .6), 'water', WATER, 'start')):
        x, y = P(a, b, c)
        parts.append(lbl(x + (8 if anc == 'start' else 0), y + (4 if anc == 'start' else -10), t, col, 14, anc))
    return spec('me-ic-u5-L3', 'Heat Balance<br>&amp; Performance<br>Variables',
                'Only <span class="gold">30 %</span> reaches the shaft;<br><span class="cyan">70 %</span> leaves as heat',
                'heat balance of a diesel', svg(s), board(parts),
                [chip('left', 300, 'c', f'fuel {Pf:.1f} kW'), chip('left', 520, 'g', f'brake {BPk} kW'),
                 chip('right', 300, 'c', f'exhaust {Pe:.2f} kW'), chip('right', 470, 'c', f'water {Pc:.2f} kW', False)],
                f'fuel {mf} × {CV} ÷ 3.6 = <b class="cl">{Pf:.1f} kW</b>: brake <b class="gl">{pc[0]:.1f} %</b><br>'
                f'water {pc[1]:.1f} %, exhaust {pc[2]:.1f} %, other {pc[3]:.1f} %')


def u5L4():
    # 5.8: piezo + encoder, 100 cycles, 1.5 L four-stroke, 2000 rpm, imep 8.2 bar, sigma 0.21 bar
    imep, Vd, N, sd = 8.2e5, 1.5e-3, 2000, .21
    IP = imep * Vd * N / 120 / 1000; cov = sd / 8.2 * 100
    assert round(IP, 1) == 20.5 and round(cov, 2) == 2.56
    X = lambda c: 40 + c / 6 * 400
    s = (f'<rect x="40" y="56" width="{X(5) - 40:.1f}" height="30" rx="6" fill="{AC2}" opacity=".18"/>'
         f'<rect x="{X(5):.1f}" y="56" width="{X(6) - X(5):.1f}" height="30" rx="6" fill="{FLAME}" opacity=".25"/>'
         f'<rect x="40" y="62" width="{X(cov) - 40:.1f}" height="18" rx="5" fill="{AC2}"/>'
         f'<line x1="{X(5):.1f}" y1="44" x2="{X(5):.1f}" y2="98" stroke="{FLAME}" stroke-width="2.5" stroke-dasharray="5 4"/>'
         f'<text x="{X(5):.1f}" y="38" text-anchor="middle" class="pt" fill="{FLAME}">5 % limit</text>'
         f'<text x="{X(cov):.1f}" y="38" text-anchor="middle" class="pt" fill="{AC2}">COV {cov:.2f} %</text>'
         + ''.join(f'<text x="{X(c):.1f}" y="114" text-anchor="middle" class="ax">{c}</text>' for c in range(0, 7))
         + f'<text x="40" y="136" class="ax">COV of imep = σ ÷ mean over 100 cycles, %</text>')
    setup()
    cx, cy = P(4.4, 3.8)
    h = 140
    parts = [barrel(cx, cy, 50, 27, h, crown=.3)]
    # piezo transducer flush in the head, cable to the amplifier; encoder disc on the crank
    parts.append(f'<rect x="{cx + 14:.1f}" y="{cy - h - 40:.1f}" width="14" height="36" rx="4" fill="{AC2}"/><rect x="{cx + 11:.1f}" y="{cy - h - 48:.1f}" width="20" height="10" rx="3" fill="#E4E9EE"/>')
    ax_, ay_ = P(6.6, 0.8, .1)
    parts.append(box(6.0, 0.2, 1.2, 1.2, .8, '#3A424C', '#1B2026', '#262C33'))
    parts.append(f'<path d="M{cx + 21:.1f},{cy - h - 48:.1f} Q{cx + 90:.1f},{cy - h - 100:.1f} {ax_:.1f},{ay_ - 30:.1f}" fill="none" stroke="{AC2}" stroke-width="2.5"/>')
    parts.append(lbl(ax_, ay_ + 18, 'logger', INK, 14))
    kx, ky = P(5.6, 7.0, .3)
    parts.append(f'<ellipse cx="{kx:.1f}" cy="{ky:.1f}" rx="42" ry="23" fill="url(#hz)"/>')
    for k in range(36):
        a = k * math.pi / 18
        parts.append(f'<line x1="{kx + 34 * math.cos(a):.1f}" y1="{ky + 18.6 * math.sin(a):.1f}" x2="{kx + 41 * math.cos(a):.1f}" y2="{ky + 22.4 * math.sin(a):.1f}" stroke="#2A3038" stroke-width="1.5"/>')
    parts.append(lbl(kx + 50, ky + 6, 'crank encoder', INK, 13, 'start'))
    parts.append(lbl(cx + 40, cy - h - 52, 'piezo', AC2, 14, 'start'))
    return spec('me-ic-u5-L4', 'Improving &amp;<br>Testing<br>Engines',
                'Piezo reads <span class="gold">CHANGES</span>:<br><span class="cyan">peg</span> it before you trust it',
                '100 cycles on a piezo chain', svg(s), board(parts),
                [chip('left', 300, 'g', 'imep 8.2 bar, σ 0.21'), chip('left', 400, 'c', '1.5 L at 2000 rpm'),
                 chip('right', 300, 'g', f'IP {IP:.1f} kW'), chip('right', 540, 'c', 'peak 62 bar, 14° ATDC', False)],
                f'IP = 8.2×10⁵ × 1.5×10⁻³ × {N / 120:.2f} = <b class="gl">{IP:.1f} kW</b><br>'
                f'COV = 0.21 ÷ 8.2 = <b class="cl">{cov:.2f} %</b>, inside 5 %: stable')


# ================================================================== unit 6
def u6L1():
    # 6.1 worked example 2: 10 kg/h at phi 0.9, 40 kW, 2000 ppm NO, exhaust 28.6 kg/kmol, NOx as NO2
    mf, phi, AFs, BPk, ppm, M, MNO2 = 10, .9, 14.7, 40, 2000, 28.6, 46.0
    AF = AFs / phi; ma = AF * mf; mex = ma + mf; nex = mex / M
    nNO = ppm * 1e-6 * nex; mNOx = nNO * MNO2 * 1000; bs = mNOx / BPk
    assert round(AF, 2) == 16.33 and round(mex, 1) == 173.3 and round(nex, 3) == 6.061 and round(mNOx, 1) == 557.6 and round(bs, 1) == 13.9
    steps = [('exhaust, kg/h', f'{mex:.1f}', INK), ('kmol/h', f'{nex:.3f}', INK), ('NO, kmol/h', f'{nNO:.5f}', AC2),
             ('NOx, g/h', f'{mNOx:.1f}', AC), ('g/kWh', f'{bs:.1f}', AC)]
    s = ''
    for k, (a, b, col) in enumerate(steps):
        x = 8 + k * 92
        s += (f'<rect x="{x}" y="30" width="84" height="72" rx="10" fill="rgba(255,255,255,.05)" stroke="{col}" stroke-width="1.6"/>'
              f'<text x="{x + 42}" y="54" text-anchor="middle" class="ax" style="font-size:12px">{a}</text>'
              f'<text x="{x + 42}" y="84" text-anchor="middle" class="pt" fill="{col}" style="font-size:{17 if len(b) < 7 else 15}px">{b}</text>')
        if k < len(steps) - 1:
            s += f'<path d="M{x + 85} 66h6" stroke="{AX}" stroke-width="2"/>'
    s += f'<text x="235" y="126" text-anchor="middle" class="ax">A/F 14.7 ÷ 0.9 = {AF:.2f}; air {ma:.1f} + fuel {mf} = {mex:.1f} kg/h exhaust</text>'
    setup()
    parts = [pipe3([(4.6, 2.4), (6.8, 2.4), (6.8, 6.8)], .9, '#7B8692', 14, glow=FLAME, gw=4)]
    parts.append(box(2.4, 1.2, 2.2, 2.4, 2.0, '#5E6974', '#262C33', '#3A424C'))
    ex, ey = P(3.5, 2.4, 2.0)
    parts.append(lbl(ex, ey + 6, 'engine · φ 0.9'))
    px, py = P(6.8, 4.8, .9)
    ax_, ay_ = P(5.0, 5.8, 1.4)
    parts.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{ax_:.1f}" y2="{ay_:.1f}" stroke="{AC2}" stroke-width="3"/>')
    parts.append(box(4.2, 5.6, 1.4, 1.4, 1.4, '#C9D2DA', '#5E6974', '#7B8692'))
    sx, sy = P(4.9, 7.0, .8)
    parts.append(lbl(sx - 6, sy + 30, 'analyser', INK, 14))
    return spec('me-ic-u6-L1', 'How Engines<br>Make CO, HC,<br>NOx &amp; Soot',
                'NOx peaks slightly <span class="gold">LEAN</span>,<br>near <span class="cyan">φ = 0.9</span>, not rich',
                'NOx from a petrol engine', svg(s), board(parts),
                [chip('left', 300, 'g', f'φ = {phi}, A/F {AF:.2f}'), chip('left', 540, 'g', f'{mf} kg/h fuel, {BPk} kW'),
                 chip('right', 330, 'c', f'{ppm} ppm NO'), chip('right', 470, 'c', f'{bs:.1f} g/kWh', False)],
                f'{mex:.1f} kg/h ÷ {M} = {nex:.3f} kmol/h × {ppm} ppm<br>'
                f'× 46.0 = <b class="gl">{mNOx:.1f} g/h</b> ÷ {BPk} kW = <b class="cl">{bs:.1f} g/kWh</b>')


def u6L2():
    # 6.3: CO2 0.04 % ambient, 1.80 % intake, 12.0 % exhaust
    amb, intake, exh = .04, 1.80, 12.0
    x = (intake - amb) / (exh - amb); per = x / (1 - x)
    assert round(x * 100, 1) == 14.7 and round(per, 3) == .173
    s = f'<text x="10" y="16" class="ax">CO₂ by volume</text>'
    for k, (n, v, t, col) in enumerate((('ambient', amb, f'{amb} %', DIM), ('intake', intake, f'{intake:.2f} %', AC2), ('exhaust', exh, f'{exh:.1f} %', AC))):
        y = 26 + k * 30
        w = max(v / exh * 280, 3)
        s += (f'<text x="84" y="{y + 17}" text-anchor="end" class="pt" fill="{col}">{n}</text>'
              f'<rect x="94" y="{y}" width="{w:.1f}" height="22" rx="5" fill="{col}" opacity=".92"/>'
              f'<text x="{102 + w:.1f}" y="{y + 17}" class="pt" fill="{col}">{t}</text>')
    s += f'<text x="10" y="132" class="ax">EGR share = (intake − ambient) ÷ (exhaust − ambient) = {intake - amb:.2f} ÷ {exh - amb:.2f}</text>'
    setup()
    parts = [pipe3([(6.4, 3.4), (6.4, 6.6), (1.6, 6.6), (1.6, 3.4)], 1.4, '#6B7682', 9, glow=AC, gw=3)]   # EGR loop round the front
    parts.append(box(2.6, 2.6, 2.8, 2.8, 2.0, '#5E6974', '#262C33', '#3A424C'))
    ex, ey = P(4.0, 4.0, 2.0)
    parts.append(lbl(ex, ey + 6, 'diesel engine'))
    parts.append(pipe3([(5.4, 3.4), (7.4, 3.4)], 1.4, '#7B8692', 12, glow=FLAME, gw=4))           # exhaust out (right)
    parts.append(pipe3([(.4, 3.4), (2.6, 3.4)], 1.4, '#7B8692', 12, glow=AC2, gw=4))              # intake (left)
    vx, vy = P(4.0, 6.6, 1.4)
    parts.append(can(vx, vy + 10, 16, 9, 30, fill='url(#hz)', top=AC))
    parts.append(lbl(vx, vy + 38, 'EGR valve', AC, 14))
    return spec('me-ic-u6-L2', 'Emission<br>Control &amp;<br>Measurement',
                'Let <span class="gold">CO₂</span> do the counting:<br><span class="cyan">14.7 %</span> is exhaust',
                'EGR rate from CO₂ readings', svg(s), board(parts),
                [chip('left', 300, 'c', f'intake {intake:.2f} %'), chip('right', 330, 'g', f'exhaust {exh:.1f} %'),
                 chip('right', 440, 'c', f'EGR {x * 100:.1f} %', False), chip('right', 540, 'g', f'{per:.3f} kg per kg air', False)],
                f'x = {intake - amb:.2f} ÷ {exh - amb:.2f} = <b class="cl">{x * 100:.1f} %</b> of the intake charge<br>'
                f'{x:.3f} ÷ {1 - x:.3f} = <b class="gl">{per:.3f} kg</b> per kg of fresh air')


def u6L3():
    # 6.6: CO2 per MJ, petrol as C8H18 (114.2 g/mol, 44 MJ/kg) vs CH4 (16.04 g/mol, 50 MJ/kg)
    p_kg = 8 * 44.0 / 114.2; p_mj = p_kg / 44
    m_kg = 44.0 / 16.04; m_mj = m_kg / 50
    save = (p_mj - m_mj) / p_mj
    assert round(p_kg, 2) == 3.08 and round(p_mj, 4) == .0701 and round(m_kg, 2) == 2.74 and round(m_mj, 4) == .0549 and round(save * 100) == 22
    s = vbars([('petrol · C₈H₁₈', p_mj, f'{p_mj:.4f}', AC, False), ('methane · CH₄', m_mj, f'{m_mj:.4f}', AC2, False)], p_mj, h=80, bw=110)
    s += f'<text x="440" y="16" text-anchor="end" class="ax">kg CO₂ per MJ</text>'
    setup()
    parts = []
    # petrol can (left) and CNG cylinder (right), each with a CO2 puff whose area follows kg CO2 per MJ
    parts.append(box(3.0, 4.2, 1.2, .8, 1.6, '#AEB8C2', '#4A535D', '#6B7682'))
    cx, cy = P(3.6, 4.6, 1.6)
    parts.append(f'<rect x="{cx - 6:.1f}" y="{cy - 20:.1f}" width="12" height="16" rx="3" fill="#7B8692"/>')
    a, b = P(3.6, 5.2, 0)
    parts.append(lbl(a, b + 22, 'petrol', AC))
    gx, gy = P(6.0, 3.0)
    parts.append(can(gx, gy, 28, 15, 100))
    parts.append(f'<rect x="{gx - 6:.1f}" y="{gy - 118:.1f}" width="12" height="18" fill="#7B8692"/>')
    parts.append(lbl(gx, gy + 30, 'CNG', AC2))
    for (x, y, r, col) in ((cx, cy - 66, 32 * math.sqrt(p_mj / p_mj), AC), (gx, gy - 160, 32 * math.sqrt(m_mj / p_mj), AC2)):
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{col}" opacity=".16" stroke="{col}" stroke-width="2" stroke-dasharray="5 4"/>')
        parts.append(lbl(x, y + 6, 'CO₂', col, 15))
    return spec('me-ic-u6-L3', 'Emission Norms<br>&amp; Alternative<br>Fuels',
                'H₂ has <span class="gold">no carbon</span>, but<br>air still makes <span class="cyan">NOx</span>',
                'CO₂ per MJ of fuel', svg(s), board(parts),
                [chip('left', 300, 'g', f'C₈H₁₈: {p_kg:.2f} kg/kg'), chip('left', 470, 'c', f'CH₄: {m_kg:.2f} kg/kg'),
                 chip('right', 300, 'g', '44 vs 50 MJ/kg'), chip('right', 470, 'c', f'{save * 100:.0f} % less CO₂', False)],
                f'petrol: {p_kg:.2f} ÷ 44 = <b class="gl">{p_mj:.4f} kg CO₂/MJ</b><br>'
                f'methane: {m_kg:.2f} ÷ 50 = <b class="cl">{m_mj:.4f}</b>, {save * 100:.0f} % less', 'h1{font-stretch:86%}')


def u6L4():
    # 6.8 worked example 3: 0.5 MW/m2 through 0.5 mm zirconia (k 1.0) and 10 mm aluminium (k 150)
    q, tc, kc, ta, ka = .5e6, .0005, 1.0, .010, 150
    dTc = q * tc / kc; dTa = q * ta / ka
    assert dTc == 250 and round(dTa) == 33
    # card: temperature through the crown, the coating drawn 10x thicker than to scale so it shows
    X0, xc, xa = 60, 60 + 80, 60 + 80 + 300
    T0 = 140
    Y = lambda d: 20 + d / 300 * 100
    s = (f'<rect x="{X0}" y="14" width="80" height="112" fill="{AC2}" opacity=".14"/><rect x="{xc}" y="14" width="300" height="112" fill="{DIM}" opacity=".12"/>'
         f'<polyline points="{X0},{Y(0):.1f} {xc},{Y(dTc):.1f} {xa},{Y(dTc + dTa):.1f}" fill="none" stroke="{FLAME}" stroke-width="3.5"/>'
         f'<circle cx="{X0}" cy="{Y(0):.1f}" r="5" fill="{FLAME}"/><circle cx="{xc}" cy="{Y(dTc):.1f}" r="5" fill="{FLAME}"/><circle cx="{xa}" cy="{Y(dTc + dTa):.1f}" r="5" fill="{FLAME}"/>'
         f'<text x="{X0 + 46}" y="{Y(dTc / 2) - 4:.1f}" class="pt" fill="{AC2}">−{dTc:g} K</text>'
         f'<text x="{(xc + xa) / 2:.1f}" y="{Y(dTc + dTa / 2) - 12:.1f}" text-anchor="middle" class="pt" fill="{INK}">−{dTa:.0f} K</text>'
         f'<text x="{X0 + 40}" y="140" text-anchor="middle" class="ax">0.5 mm ZrO₂</text><text x="{(xc + xa) / 2:.1f}" y="140" text-anchor="middle" class="ax">10 mm aluminium</text>'
         f'<text x="54" y="24" text-anchor="end" class="ax">T</text><text x="440" y="30" text-anchor="end" class="ax">not to scale</text>')
    setup()
    cx, cy = P(4.2, 4.2)
    parts = [can(cx, cy, 74, 40, 120)]
    for k in range(3):
        y = cy - 26 - k * 14
        parts.append(f'<path d="M{cx - 74:.1f},{y:.1f} A74,40 0 0 0 {cx + 74:.1f},{y:.1f}" fill="none" stroke="#3A424C" stroke-width="3"/>')
    parts.append(f'<path d="M{cx - 74:.1f},{cy - 120:.1f} v-10 A74,40 0 0 0 {cx + 74:.1f},{cy - 130:.1f} v10 A74,40 0 0 1 {cx - 74:.1f},{cy - 120:.1f}Z" fill="#E8EEF3"/>')
    parts.append(f'<ellipse cx="{cx:.1f}" cy="{cy - 130:.1f}" rx="74" ry="40" fill="#F4F7F9"/>')
    for k in range(5):
        x = cx - 40 + k * 20
        parts.append(f'<g filter="url(#gl)">{arrow(x, cy - 214, x, cy - 146, FLAME, 4)}</g>')
    parts.append(f'<text x="{cx:.1f}" y="{cy - 125:.1f}" text-anchor="middle" style="font:700 15px IBM Plex Sans,sans-serif;fill:#1A2028">ZrO₂ coating</text>')
    parts.append(f'<text x="{cx:.1f}" y="{cy - 40:.1f}" text-anchor="middle" style="font:700 15px IBM Plex Sans,sans-serif;fill:#1A2028">aluminium</text>')
    return spec('me-ic-u6-L4', 'Dual Fuel,<br>Stratified &amp;<br>LHR Engines',
                'Most saved heat goes out<br>the <span class="gold">EXHAUST</span>, not the <span class="cyan">shaft</span>',
                'coated piston crown', svg(s), board(parts),
                [chip('left', 300, 'g', 'q = 0.5 MW/m²'), chip('left', 470, 'c', 'k: 1.0 vs 150 W/(m·K)'),
                 chip('right', 300, 'c', f'coating {dTc:g} K'), chip('right', 470, 'g', f'metal {dTa:.0f} K', False)],
                f'ΔT = q t ÷ k: 0.5×10⁶ × 0.0005 ÷ 1.0 = <b class="cl">{dTc:g} K</b><br>'
                f'aluminium: 0.5×10⁶ × 0.010 ÷ 150 = <b class="gl">{dTa:.0f} K</b>')


def u6L5():
    # 6.9: HCCI, tau = A exp(E/RT), E/R = 15 000 K, 900 K vs 950 K
    ER, Ta, Tb = 15000, 900, 950
    ratio = math.exp(ER * (1 / Ta - 1 / Tb))
    assert round(ratio, 2) == 2.40
    X = lambda T: 50 + (T - 880) / 90 * 390
    Y = lambda r: 122 - (r - 1) / 2.4 * 100 if r >= 1 else 122
    curve = ' '.join(f'{X(T):.1f},{122 - (math.exp(ER * (1 / T - 1 / Tb)) - .6) / 3.0 * 100:.1f}' for T in range(880, 971, 2))
    YY = lambda r: 122 - (r - .6) / 3.0 * 100
    s = (f'<line x1="50" y1="122" x2="446" y2="122" stroke="{AX}" stroke-width="1.5"/><line x1="50" y1="18" x2="50" y2="122" stroke="{AX}" stroke-width="1.5"/>'
         f'<polyline points="{curve}" fill="none" stroke="{AC}" stroke-width="3.2"/>')
    for T, r, col, txt, dx in ((Ta, ratio, AC, f'{Ta} K: {ratio:.2f}×', 10), (Tb, 1.0, AC2, f'{Tb} K: 1×', 10)):
        s += (f'<line x1="{X(T):.1f}" y1="122" x2="{X(T):.1f}" y2="{YY(r):.1f}" stroke="{col}" stroke-width="1.6" stroke-dasharray="5 4"/>'
              f'<circle cx="{X(T):.1f}" cy="{YY(r):.1f}" r="6" fill="{col}"/><text x="{X(T) + dx:.1f}" y="{YY(r) - 8:.1f}" class="pt" fill="{col}">{txt}</text>')
    s += ('<text x="58" y="16" class="ax">ignition delay τ ÷ τ at 950 K, against charge T (K)</text>'
          + ''.join(f'<text x="{X(T):.1f}" y="139" text-anchor="middle" class="ax">{T}</text>' for T in (880, 900, 920, 940, 960)))
    setup()
    cx, cy = P(4.4, 3.8)
    h = 150
    parts = [barrel(cx, cy, 52, 28, h, crown=.2)]
    import random
    rnd = random.Random(7)
    dots = ''.join(f'<circle cx="{cx + rnd.uniform(-40, 40):.1f}" cy="{cy - h + rnd.uniform(-10, 10):.1f}" r="2.4" fill="{AC2}"/>' for _ in range(40))
    parts.append(f'<g opacity=".9">{dots}</g>')
    parts.append(f'<rect x="{cx - 8:.1f}" y="{cy - h - 50:.1f}" width="16" height="30" rx="4" fill="#3A424C"/>'
                 f'<line x1="{cx - 14:.1f}" y1="{cy - h - 58:.1f}" x2="{cx + 14:.1f}" y2="{cy - h - 12:.1f}" stroke="{FLAME}" stroke-width="4"/>')
    parts.append(lbl(cx - 26, cy - h - 34, 'no spark plug', FLAME, 14, 'end'))
    parts.insert(0, pipe3([(4.4, .4), (4.4, 3.0)], 4.0, '#7B8692', 12, glow=FLAME, gw=4))
    ix, iy = P(4.4, .6, 4.0)
    parts.append(lbl(ix, iy - 16, 'intake 900 / 950 K', AC, 14))
    return spec('me-ic-u6-L5', 'HCCI, RCCI<br>&amp; Optical<br>Engines',
                'No <span class="gold">spark</span>: the charge<br><span class="cyan">temperature</span> times the burn',
                'HCCI delay at 900 vs 950 K', svg(s), board(parts),
                [chip('left', 300, 'g', f'E/R = {ER:,} K'.replace(',', ' ')), chip('left', 470, 'c', '50 K warmer'),
                 chip('right', 300, 'g', f'{ratio:.1f}× sooner'), chip('right', 470, 'c', 'same pressure', False)],
                f'τ<sub>900</sub> ÷ τ<sub>950</sub> = exp[15 000 × (1/900 − 1/950)]<br>'
                f'= exp({ER * (1 / Ta - 1 / Tb):.3f}) = <b class="gl">{ratio:.2f}</b>: hold intake T within a few K')


HOOKS = {
    'me-ic-u1-L1': 'Is a two-stroke engine two cylinders?',
    'me-ic-u1-L2': 'Does a two-stroke give twice the power?',
    'me-ic-u1-L3': 'Firing interval: 90° or 180°?',
    'me-ic-u1-L4': 'Is Otto always better than Diesel?',
    'me-ic-u2-L1': 'Is 18:1 a rich or a lean mixture?',
    'me-ic-u2-L2': 'Does rail pressure set the fuel dose?',
    'me-ic-u2-L3': 'Is a stratified charge rich or lean?',
    'me-ic-u2-L4': 'Nozzle hole area: πd² or πd²/4?',
    'me-ic-u2-L5': 'Which circuit does the breaker cut?',
    'me-ic-u3-L1': 'How fast does a flame really burn?',
    'me-ic-u3-L2': 'Is it knock or pre-ignition?',
    'me-ic-u3-L3': 'Does advancing the spark cause knock?',
    'me-ic-u3-L4': 'When does a diesel engine knock?',
    'me-ic-u4-L1': 'Does the pressure cap cool the coolant?',
    'me-ic-u4-L2': 'What does the W in 10W-40 mean?',
    'me-ic-u4-L3': 'Does an intercooler raise the boost?',
    'me-ic-u5-L1': 'Why divide by 2 for a four-stroke?',
    'me-ic-u5-L2': 'Which arm gives the dynamometer torque?',
    'me-ic-u5-L3': 'Where does the fuel power go?',
    'me-ic-u5-L4': 'Is a piezo pressure reading absolute?',
    'me-ic-u6-L1': 'Is NOx highest in a rich mixture?',
    'me-ic-u6-L2': 'How much EGR is in the charge?',
    'me-ic-u6-L3': 'Is a hydrogen engine zero-emission?',
    'me-ic-u6-L4': "Where does the LHR engine's heat go?",
    'me-ic-u6-L5': 'Does HCCI need a spark?',
}


def specs():
    out = [f() for f in (u1L1, u1L2, u1L3, u1L4, u2L1, u2L2, u2L3, u2L4, u2L5, u3L1, u3L2, u3L3, u3L4,
                         u4L1, u4L2, u4L3, u5L1, u5L2, u5L3, u5L4, u6L1, u6L2, u6L3, u6L4, u6L5)]
    for s in out:
        s['subject'] = SUBJ
        s['question'] = HOOKS[s['key']].replace("'", '&#39;')
    for s in out:
        s.setdefault('subject', SUBJ)
        s['dept'] = D
    return out
