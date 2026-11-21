"""t16 split blueprint thumbnails for Engineering Thermodynamics (me-thermo), Mech look.
One spec per lesson, each drawn from that lesson's own book worked example (books/mech/me-thermo/me-thermo-u<N>.html),
every number computed here and matched to the book's answer.
Build: python3 t16_split.py build specs.py <out dir>   (run from the tool folder, or set T16_TOOL to it)."""
import html as H, math, os, re, sys
try:
    import t16_split as T
except ImportError:
    sys.path.insert(0, os.environ.get('T16_TOOL', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tool')))
    import t16_split as T
B = T.B
ln = math.log

D = 'mech'
ACC, AC2 = T.DEPTS[D]['acc'], T.DEPTS[D]['acc2']          # orange, ice blue
INK, AXC, DARK = '#E6ECF1', '#6B7B8A', '#12171C'
HOT, COLD, WATER = '#FF7A45', '#5FB2F0', '#4FA3D9'
U, OX, OY = 33, 952, 336


def P(x, y, z=0):
    return OX + (x - y) * U * .866, OY + (x + y) * U * .5 - z * U


def pts(*p):
    return ' '.join(f'{a:.1f},{b:.1f}' for a, b in p)


def box(x, y, w, d, h, top, left, right, z0=0):
    B.U, B.OX, B.OY = U, OX, OY
    return B.box(x, y, w, d, h, top, left, right, z0)


# ---------------------------------------------------------------- board pieces
DEFS = ('<defs>'
        '<linearGradient id="pl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3B4652"/><stop offset="1" stop-color="#252E37"/></linearGradient>'
        '<linearGradient id="tk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6E7B88"/><stop offset=".38" stop-color="#E9EEF2"/><stop offset=".62" stop-color="#B7C2CC"/><stop offset="1" stop-color="#56626E"/></linearGradient>'
        '<linearGradient id="tv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#56626E"/><stop offset=".3" stop-color="#E9EEF2"/><stop offset=".55" stop-color="#B7C2CC"/><stop offset="1" stop-color="#4A5560"/></linearGradient>'
        '<radialGradient id="dm" cx=".4" cy=".3" r=".8"><stop offset="0" stop-color="#F4F7F9"/><stop offset="1" stop-color="#8E9AA6"/></radialGradient>'
        '<linearGradient id="hot" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFB37A"/><stop offset="1" stop-color="#E0652A"/></linearGradient>'
        '<linearGradient id="cold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#A9DBFF"/><stop offset="1" stop-color="#3F8FD0"/></linearGradient>'
        '<linearGradient id="wt" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2F6E9C"/><stop offset=".4" stop-color="#7CC4FF"/><stop offset="1" stop-color="#2A5F88"/></linearGradient>'
        '<radialGradient id="bulb" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#9AA8B6"/></radialGradient>'
        f'<marker id="ao" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{ACC}"/></marker>'
        f'<marker id="ab" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{AC2}"/></marker>'
        '<marker id="ak" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="3.5" markerHeight="3.5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#3A444E"/></marker>'
        f'<linearGradient id="mix" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{HOT}"/><stop offset=".46" stop-color="{HOT}"/><stop offset=".54" stop-color="{COLD}"/><stop offset="1" stop-color="{COLD}"/></linearGradient>'
        '<linearGradient id="cng" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2E6B44"/><stop offset=".4" stop-color="#7FD39B"/><stop offset=".65" stop-color="#4FA86E"/><stop offset="1" stop-color="#245638"/></linearGradient>'
        '</defs>')


def plate():
    """slab grid and the four screws of the approved sample"""
    s = f'<g fill="none" stroke="{AC2}" stroke-opacity=".14" stroke-width="1.2">'
    for k in range(1, 8):
        s += f'<polyline points="{pts(P(k, 0), P(k, 8))}"/><polyline points="{pts(P(0, k), P(8, k))}"/>'
    s += '</g>'
    for a, b in ((.4, .4), (7.6, .4), (.4, 7.6), (7.6, 7.6)):
        x, y = P(a, b)
        s += f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="7" ry="4" fill="#5B6774" stroke="{DARK}" stroke-width="1.5"/><path d="M{x - 4:.1f},{y:.1f}H{x + 4:.1f}" stroke="{DARK}" stroke-width="1.5"/>'
    return s


def board(parts):
    return T.iso_board(D, [DEFS, plate()] + parts, top='url(#pl)', left='#161C22', right='#1C232A', origin=(OX, OY), unit=U)


def lab(x, y, t, fill=INK, size=16, anchor='middle', w=700):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="bl" style="font-size:{size}px;font-weight:{w}" fill="{fill}">{t}</text>'


def ucyl(x, y, r, h, z0=0, body='url(#tk)', top='url(#dm)', bands=()):
    """upright cylinder standing on iso point (x, y) at height z0; r and h in board units"""
    cx, cy = P(x, y, z0)
    rx, ry, hp = r * U * 1.2247, r * U * .7071, h * U
    s = f'<ellipse cx="{cx:.1f}" cy="{cy + 5:.1f}" rx="{rx + 4:.1f}" ry="{ry + 3:.1f}" fill="#000" opacity=".35"/>' if z0 == 0 else ''
    s += T.cyl(cx, cy, round(rx, 1), round(ry, 1), hp, body, top)
    for f in bands:
        s += f'<path d="M{cx - rx:.1f},{cy - hp * f:.1f} A{rx:.1f},{ry:.1f} 0 0 0 {cx + rx:.1f},{cy - hp * f:.1f}" fill="none" stroke="#5E6A76" stroke-width="2"/>'
    return s


def ring(x, y, z, r, axis='z', n=40):
    out = []
    for k in range(n):
        a = 2 * math.pi * k / n
        c, s_ = r * math.cos(a), r * math.sin(a)
        out.append(P(x, y + c, z + s_) if axis == 'x' else P(x + c, y, z + s_) if axis == 'y' else P(x + c, y + s_, z))
    return out


def hull(p):
    p = sorted(set((round(a, 1), round(b, 1)) for a, b in p))
    def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for q in p:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], q) <= 0: lo.pop()
        lo.append(q)
    for q in reversed(p):
        while len(up) >= 2 and cross(up[-2], up[-1], q) <= 0: up.pop()
        up.append(q)
    return lo[:-1] + up[:-1]


def tube(axis, a, b, c0, c1, r, body='url(#tv)', cap='url(#dm)', capend=None):
    """a cylinder lying along the x or y axis: from coordinate a to b on that axis, centre (c0, c1) = (other horizontal, z)"""
    if axis == 'x':
        r0, r1 = ring(a, c0, c1, r, 'x'), ring(b, c0, c1, r, 'x')
    else:
        r0, r1 = ring(c0, a, c1, r, 'y'), ring(c0, b, c1, r, 'y')
    s = f'<polygon points="{pts(*hull(r0 + r1))}" fill="{body}"/>'
    end = r1 if (capend is None or capend == 'b') else r0
    s += f'<polygon points="{pts(*end)}" fill="{cap}" stroke="#5E6A76" stroke-width="1.5"/>'
    return s


def pipe(path, z, col='#8E9AA6', w=10):
    pp = pts(*[P(a, b, z) for a, b in path])
    return (f'<polyline points="{pp}" fill="none" stroke="#3A444E" stroke-width="{w + 4}" stroke-linejoin="round" stroke-linecap="round"/>'
            f'<polyline points="{pp}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'
            f'<polyline points="{pp}" fill="none" stroke="#E9EEF2" stroke-opacity=".5" stroke-width="{w * .3:.1f}" stroke-linejoin="round" stroke-linecap="round" transform="translate(0 -{w * .25:.1f})"/>')


def wave(x, y, col=ACC, n=3, gap=34, flip=False):
    m = 'ao' if col == ACC else 'ab'
    s = ''
    for k in range(n):
        yy = y + k * gap
        d = f'M{x:.1f},{yy:.1f} q-10,-8 -20,0 t-20,0 t-20,0' if flip else f'M{x:.1f},{yy:.1f} q10,-8 20,0 t20,0 t20,0'
        s += f'<path d="{d}" fill="none" stroke="{col}" stroke-width="3.5" stroke-linecap="round" marker-end="url(#{m})" opacity=".95"/>'
    return s


def garrow(x0, y0, x1, y1, col=ACC, w=7):
    return f'<g style="filter:drop-shadow(0 0 6px {col})">{T.arrow(x0, y0, x1, y1, col, w)}</g>'


def gauge(x, y, r=20, frac=.65, col=ACC):
    a = math.pi * (1.25 - 1.5 * frac)
    s = f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r + 3}" fill="#56626E"/><circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#F1F4F7"/>'
    for k in range(7):
        t = math.pi * (1.25 - 1.5 * k / 6)
        s += f'<line x1="{x + .72 * r * math.cos(t):.1f}" y1="{y - .72 * r * math.sin(t):.1f}" x2="{x + .9 * r * math.cos(t):.1f}" y2="{y - .9 * r * math.sin(t):.1f}" stroke="#3A444E" stroke-width="1.6"/>'
    s += f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x + .78 * r * math.cos(a):.1f}" y2="{y - .78 * r * math.sin(a):.1f}" stroke="{col}" stroke-width="3" stroke-linecap="round"/><circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="#3A444E"/>'
    return s


def thermo(x, y, h=70, frac=.6, col=ACC):
    """a glass thermometer standing with its bulb at (x, y)"""
    return (f'<rect x="{x - 6:.1f}" y="{y - h:.1f}" width="12" height="{h}" rx="6" fill="#E9EEF2" stroke="#56626E" stroke-width="1.5"/>'
            f'<rect x="{x - 2.5:.1f}" y="{y - h * frac:.1f}" width="5" height="{h * frac:.1f}" fill="{col}"/>'
            f'<circle cx="{x:.1f}" cy="{y + 4:.1f}" r="10" fill="{col}" stroke="#56626E" stroke-width="1.5"/>')


def flame(x, y, s=1.0):
    return (f'<g style="filter:drop-shadow(0 0 8px {ACC})"><path d="M{x:.1f},{y:.1f} c{-14 * s:.1f},{-8 * s:.1f} {-12 * s:.1f},{-26 * s:.1f} 0,{-42 * s:.1f} c{2 * s:.1f},{12 * s:.1f} {14 * s:.1f},{14 * s:.1f} {10 * s:.1f},{28 * s:.1f} c{-2 * s:.1f},{9 * s:.1f} {-6 * s:.1f},{14 * s:.1f} {-10 * s:.1f},{14 * s:.1f}Z" fill="{ACC}"/>'
            f'<path d="M{x:.1f},{y - 4 * s:.1f} c{-6 * s:.1f},{-4 * s:.1f} {-5 * s:.1f},{-13 * s:.1f} 0,{-20 * s:.1f} c{4 * s:.1f},{7 * s:.1f} {6 * s:.1f},{14 * s:.1f} 0,{20 * s:.1f}Z" fill="#FFE1B8"/></g>')


def piston_cyl(x, y, r, h, piston_at, gas=AC2, glass=True, rod=1.2):
    """a see-through upright cylinder with gas below a piston at height piston_at (board units)"""
    cx, cy = P(x, y)
    rx, ry = r * U * 1.2247, r * U * .7071
    hp, pp = h * U, piston_at * U
    s = f'<ellipse cx="{cx:.1f}" cy="{cy + 5:.1f}" rx="{rx + 6:.1f}" ry="{ry + 4:.1f}" fill="#000" opacity=".35"/>'
    s += f'<path d="M{cx - rx:.1f},{cy:.1f} V{cy - hp:.1f} A{rx:.1f},{ry:.1f} 0 0 0 {cx + rx:.1f},{cy - hp:.1f} V{cy:.1f} A{rx:.1f},{ry:.1f} 0 0 1 {cx - rx:.1f},{cy:.1f}Z" fill="#2C3A44"/>'
    s += f'<path d="M{cx - rx:.1f},{cy:.1f} V{cy - pp:.1f} A{rx:.1f},{ry:.1f} 0 0 0 {cx + rx:.1f},{cy - pp:.1f} V{cy:.1f} A{rx:.1f},{ry:.1f} 0 0 1 {cx - rx:.1f},{cy:.1f}Z" fill="{gas}" fill-opacity=".30"/>'
    # piston
    s += T.cyl(cx, cy - pp, round(rx - 2, 1), round(ry - 1, 1), 14, 'url(#tk)', 'url(#dm)')
    s += f'<rect x="{cx - 6:.1f}" y="{cy - pp - 14 - rod * U:.1f}" width="12" height="{rod * U:.1f}" fill="url(#tk)"/>'
    # glass walls
    s += (f'<path d="M{cx - rx:.1f},{cy:.1f} V{cy - hp:.1f} M{cx + rx:.1f},{cy:.1f} V{cy - hp:.1f}" stroke="#C9D3DB" stroke-width="3" opacity=".9"/>'
          f'<ellipse cx="{cx:.1f}" cy="{cy - hp:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="none" stroke="#C9D3DB" stroke-width="2.5" opacity=".9"/>'
          f'<path d="M{cx - rx:.1f},{cy:.1f} A{rx:.1f},{ry:.1f} 0 0 0 {cx + rx:.1f},{cy:.1f}" fill="none" stroke="#C9D3DB" stroke-width="3"/>'
          f'<path d="M{cx - rx + 8:.1f},{cy - 10:.1f} V{cy - hp + 12:.1f}" stroke="#FFFFFF" stroke-opacity=".35" stroke-width="5" stroke-linecap="round"/>')
    return s


def vessel(x, y, r, h, fill, op=.35, rim='#C9D3DB', z0=0, shadow=True):
    """a see-through upright vessel filled with fill"""
    cx, cy = P(x, y, z0)
    rx, ry, hp = r * U * 1.2247, r * U * .7071, h * U
    s = f'<ellipse cx="{cx:.1f}" cy="{cy + 5:.1f}" rx="{rx + 6:.1f}" ry="{ry + 4:.1f}" fill="#000" opacity=".35"/>' if shadow else ''
    s += f'<path d="M{cx - rx:.1f},{cy:.1f} V{cy - hp:.1f} A{rx:.1f},{ry:.1f} 0 0 0 {cx + rx:.1f},{cy - hp:.1f} V{cy:.1f} A{rx:.1f},{ry:.1f} 0 0 1 {cx - rx:.1f},{cy:.1f}Z" fill="#22303A"/>'
    s += f'<path d="M{cx - rx:.1f},{cy:.1f} V{cy - hp:.1f} A{rx:.1f},{ry:.1f} 0 0 0 {cx + rx:.1f},{cy - hp:.1f} V{cy:.1f} A{rx:.1f},{ry:.1f} 0 0 1 {cx - rx:.1f},{cy:.1f}Z" fill="{fill}" fill-opacity="{op}"/>'
    s += (f'<path d="M{cx - rx:.1f},{cy:.1f} V{cy - hp:.1f} M{cx + rx:.1f},{cy:.1f} V{cy - hp:.1f}" stroke="{rim}" stroke-width="3"/>'
          f'<ellipse cx="{cx:.1f}" cy="{cy - hp:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" fill-opacity="{op * .8:.2f}" stroke="{rim}" stroke-width="2.5"/>'
          f'<path d="M{cx - rx:.1f},{cy:.1f} A{rx:.1f},{ry:.1f} 0 0 0 {cx + rx:.1f},{cy:.1f}" fill="none" stroke="{rim}" stroke-width="3"/>'
          f'<path d="M{cx - rx + 8:.1f},{cy - 8:.1f} V{cy - hp + 10:.1f}" stroke="#FFFFFF" stroke-opacity=".3" stroke-width="5" stroke-linecap="round"/>')
    return s


def reservoir(x, y, w, d, h, hot, text):
    s = box(x, y, w, d, h, 'url(#hot)' if hot else 'url(#cold)', '#B4512A' if hot else '#2F6E9C', '#D0683A' if hot else '#3F86BE')
    tx, ty = P(x + w / 2, y + d / 2, h)
    return s + lab(tx, ty + 6, text, '#4A1A06' if hot else '#0E2238', 18)


def engine(x, y, r=1.0, h=1.4, sym='cycle'):
    """a cyclic device: a metal drum with a cycle arrow on its lid"""
    cx, cy = P(x, y, h)
    rx, ry = r * U * 1.2247 * .55, r * U * .7071 * .55
    s = ucyl(x, y, r, h)
    s += (f'<path d="M{cx + rx:.1f},{cy:.1f} A{rx:.1f},{ry:.1f} 0 1 1 {cx + rx * .2:.1f},{cy - ry * .98:.1f}" fill="none" stroke="#3A444E" stroke-width="3.5" marker-end="url(#ak)"/>')
    return s


# ---------------------------------------------------------------- card pieces (470 x 144)
def svgcard(inner):
    return f'<svg width="470" height="144" viewBox="0 0 470 144">{inner}</svg>'


def t_(x, y, s, cls='ax', anchor='middle', fill=None, extra=''):
    f = f' fill="{fill}"' if fill else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}"{f}{extra}>{s}</text>'


def axes(x0, x1, y0, y1):
    return (f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{AXC}" stroke-width="1.5"/>'
            f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{AXC}" stroke-width="1.5"/>')


def poly(p, col, w=3.5, fill='none', op=1, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polyline points="{pts(*p)}" fill="{fill}" fill-opacity="{op}" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"{d}/>'


def dot(x, y, col, r=5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>'


def hbars(rows, x0, x1, y0, h, gap, vmax, lw=120):
    """horizontal bars: rows = (label, value, colour, text)"""
    s = ''
    for k, (lb, v, col, tx) in enumerate(rows):
        y = y0 + k * (h + gap)
        w = (x1 - x0 - lw) * v / vmax
        s += t_(x0 + lw - 10, y + h * .72, lb, 'pt', 'end', col)
        s += f'<rect x="{x0 + lw}" y="{y}" width="{w:.1f}" height="{h}" rx="4" fill="{col}" fill-opacity=".85"/>'
        s += t_(x0 + lw + w + 8, y + h * .72, tx, 'pt', 'start', INK)
    return s


TABLE_CSS = """
table{border-collapse:collapse;width:100%;margin-top:6px;font:600 17px 'IBM Plex Sans';color:#E6ECF1}
th{font:600 14px 'IBM Plex Sans';color:#9FB0BF;text-align:center;padding:4px 6px;border-bottom:1.5px solid #3A4A58}
td{text-align:center;padding:7px 6px;border-bottom:1px solid #2A3844;font-size:18px}
td:first-child{text-align:left;font-size:17px;font-weight:700}
tr:last-child td{border-bottom:none}"""
BASE_CSS = ".bl{font-family:'IBM Plex Sans'}.sh .tag{white-space:nowrap}.sh span{white-space:nowrap}" + TABLE_CSS


def table(head, rows):
    h = '<tr>' + ''.join(f'<th>{c}</th>' for c in head) + '</tr>'
    b = ''
    for r in rows:
        b += '<tr>' + ''.join(f'<td{(" style=" + chr(34) + st + chr(34)) if st else ""}>{c}</td>' for c, st in r) + '</tr>'
    return f'<table>{h}{b}</table>'


# ---------------------------------------------------------------- spec assembly
# subject, topic and hook exactly as in me-thermo/thumbnail/thumbs.json
HOOK = {
    'me-thermo-u1-L1': ('Systems, Properties & the Continuum', 'Is a sealed tank an isolated system?'),
    'me-thermo-u1-L2': ('Equilibrium & the Zeroth Law', 'A 10 °C rise: 10 K or 283 K?'),
    'me-thermo-u1-L3': ('Work & Heat', 'Heat rejected: is Q plus or minus?'),
    'me-thermo-u2-L1': ('First Law, Internal Energy & Enthalpy', 'Rigid tank heated: Q = ΔU or ΔH?'),
    'me-thermo-u2-L2': ('Specific Heats & Non-flow Processes', 'Gas got hotter, so heat went in?'),
    'me-thermo-u2-L3': ('Perpetual Motion & the Steady Flow Equation', 'Is a 20 % engine a PMM-1?'),
    'me-thermo-u2-L4': ('Unsteady Flow & the Limits of the First Law', 'Why does a filled tank get hotter?'),
    'me-thermo-u3-L1': ('Heat Engines & the Second Law', 'Efficiency: W over heat in or out?'),
    'me-thermo-u3-L2': ('Reversible Processes & the Carnot Cycle', 'Is a slow process always reversible?'),
    'me-thermo-u3-L3': ('The Kelvin Scale & the Clausius Inequality', 'Impossible cycle, or just irreversible?'),
    'me-thermo-u3-L4': ('Entropy & the Principle of Increase', 'Freezing water: does entropy fall?'),
    'me-thermo-u3-L5': ('Entropy Generation & the Third Law', 'Can entropy run to minus infinity?'),
    'me-thermo-u4-L1': ('Available Energy & Exergy', 'How much of this heat can do work?'),
    'me-thermo-u4-L2': ('Exact Differentials, Gibbs & Helmholtz', 'Slope product: +1 or −1?'),
    'me-thermo-u4-L3': ('Maxwell, Clapeyron & Joule-Thomson', 'Does throttling always cool a gas?'),
    'me-thermo-u5-L1': ('Phase Change, Triple & Critical Points', "Is water's triple point above 1 atm?"),
    'me-thermo-u5-L2': ('Gibbs Phase Rule & Steam Formation', 'How many free choices in wet steam?'),
    'me-thermo-u5-L3': ('Steam Tables & Calorimeters', 'Superheated steam: which table?'),
    'me-thermo-u5-L4': ('Ideal & Real Gases', 'Gauge or absolute in the Z chart?'),
    'me-thermo-u5-L5': ('Gas Mixtures & Moist Air', 'Why divide by dry-air pressure?'),
    'me-thermo-u6-L1': ('Carnot, Otto, Diesel & Dual Cycles', 'Diesel heat in: cp or cv?'),
    'me-thermo-u6-L2': ('Brayton, Stirling & Mean Effective Pressure', 'MEP: total or swept volume?'),
    'me-thermo-u6-L3': ('Rankine, Reheat & Regeneration', 'Does reheat lift efficiency to 47 %?'),
    'me-thermo-u6-L4': ('Refrigeration: Compression & Absorption', 'COP: divide by work or by heat out?'),
}

_FONT = None


def title_css(title):
    """largest title size, at most 76 px, whose widest line fits the 536 px column"""
    global _FONT
    from PIL import ImageFont
    import html as H
    if _FONT is None:
        _FONT = os.path.expanduser('~/.fonts/IBMPlexSans[wdth,wght].ttf')
    lines = [H.unescape(l).replace('\xa0', ' ') for l in title.split('<br>')]
    for size in range(76, 59, -1):
        f = ImageFont.truetype(_FONT, size)
        try:
            f.set_variation_by_axes([700, 100])
        except Exception:
            pass
        w = max(f.getlength(l) - .02 * size * len(l) for l in lines)
        if w <= 520:
            break
    return '' if size == 76 else f'h1{{font-size:{size}px !important}}'


def chip(side, top, kind, text, pointer=True):
    return dict(side=side, top=top, kind=kind, text=text, pointer=pointer)


def make(key, title, takeaway, card_title, card, parts, chips, summary, css=''):
    topic, hook = HOOK[key]
    assert len(re.sub('<[^>]+>', '', card_title)) <= 24, card_title
    return dict(key=key, dept=D, subject='THERMODYNAMICS', title=title, question=hook, takeaway=takeaway, tag='Book example',
                card_title=card_title, card=card, board=board(parts), chips=chips, summary=summary,
                css=BASE_CSS + title_css(title) + css, page_title=f'{H.escape(topic)}: Mech')


def sg(v, fmt='g'):
    """signed number with a true minus sign"""
    return ('+' if v > 0 else '−' if v < 0 else '') + format(abs(v), fmt)


def r1(v): return f'{v + 1e-9:.1f}'
def r2(v): return f'{v + 1e-9:.2f}'


def f2(v): return f'{v:.2f}'
def f1(v): return f'{v:.1f}'


# ================================================================ unit 1
def u1L1():
    """1.2 worked example: rigid tank, 2.0 kg, 0.50 kg escapes, 30 kJ of heat leaves"""
    m1, me, Qout = 2.0, 0.50, 30
    m2 = m1 - me                                          # 1.5 kg
    frac = m2 / m1                                        # 0.75 of the tank at the start
    assert abs(m2 - 1.5) < 1e-9 and abs(frac - .75) < 1e-9
    cx, cy = P(4, 4)
    p = [f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="112" ry="62" fill="none" stroke="{ACC}" stroke-width="3" stroke-dasharray="10 8"/>',
         ucyl(4, 4, 1.43, 3.27, bands=(.25, .70)),
         f'<path d="M{cx - 46:.1f},{cy - 110:.1f} Q{cx:.1f},{cy - 160:.1f} {cx + 46:.1f},{cy - 110:.1f}" fill="url(#dm)" opacity=".9"/>',
         f'<rect x="{cx - 44:.1f}" y="{cy - 91:.1f}" width="88" height="{81 * frac / .75:.1f}" rx="14" fill="{AC2}" fill-opacity=".14" stroke="{AC2}" stroke-width="2.6" stroke-dasharray="8 6"/>',
         lab(cx, cy - 36, f'{m2:g} kg', '#0E2238', 18),
         f'<rect x="{cx - 9:.1f}" y="{cy - 164:.1f}" width="18" height="30" rx="3" fill="#2A323B"/><rect x="{cx - 20:.1f}" y="{cy - 170:.1f}" width="40" height="9" rx="4" fill="{ACC}"/>',
         garrow(cx, cy - 176, cx, cy - 216, ACC, 6),
         wave(cx + 68, cy - 108, ACC, 3, 34)]
    card = table(['', 'mass crosses', 'heat crosses', 'system'],
                 [[('Tank (A)', f'color:{ACC}'), ('yes', ''), ('yes', ''), ('open', f'color:{ACC};font-weight:700')],
                  [(f'{m2:g} kg left (B)', f'color:{AC2}'), ('no', ''), ('yes', ''), ('closed', f'color:{AC2};font-weight:700')],
                  [('Isolated?', ''), ('', ''), ('', ''), ('neither', 'font-weight:700')]])
    return make('me-thermo-u1-L1', 'Systems,<br>Properties &amp;<br>the Continuum',
                'Closed is <span class="gold">NOT</span> isolated —<br>heat still <span class="cyan">CROSSES</span>',
                'one tank, two boundaries', card, p,
                [chip('left', 300, 'c', f'{m1:.1f} kg at start'), chip('left', 364, 'g', f'{me:.2f} kg escapes'),
                 chip('left', 470, 'c', f'{m2:g} kg left'), chip('right', 430, 'g', f'{Qout} kJ heat out'),
                 chip('right', 500, 'c', 'rigid: no wall work', False)],
                f'<b class="gl">(a)</b> m₂ = {m1:.1f} − {me:.2f} = <b class="gl">{m2:g} kg</b>; mass crosses → <b class="gl">open</b><br>'
                f'<b class="cl">(b)</b> no mass crosses → <b class="cl">closed</b> · (c) neither isolated')


def u1L2():
    """1.5 worked example (b): constant-volume gas thermometer, 60.00 kPa at the triple point, 75.00 kPa in the bath"""
    Ttp, ptp, pb = 273.16, 60.00, 75.00
    T = Ttp * pb / ptp                                    # 341.45 K
    t = T - 273.15                                        # 68.30 °C
    riseK, riseC = T - Ttp, t - 0.01                       # the same 68.29 on both scales
    assert f'{T:.2f}' == '341.45' and f'{t:.2f}' == '68.30' and f'{riseK:.2f}' == f'{riseC:.2f}' == '68.29'
    # board: a water bath with the gas bulb in it, a capillary to the pressure gauge
    bx, by = P(2.4, 3.0)
    p = [box(1.6, 2.2, 3.2, 3.0, 2.2, '#5FA9DE', '#1F4E70', '#2A6690'),
         f'<polygon points="{pts(P(1.6, 2.2, 2.2), P(4.8, 2.2, 2.2), P(4.8, 5.2, 2.2), P(1.6, 5.2, 2.2))}" fill="{AC2}" fill-opacity=".55"/>',
         ]
    qx, qy = P(3.2, 3.7, 2.2)
    p += [f'<circle cx="{qx:.1f}" cy="{qy - 2:.1f}" r="30" fill="url(#bulb)" stroke="#56626E" stroke-width="2"/>',
          f'<ellipse cx="{qx:.1f}" cy="{qy - 2:.1f}" rx="44" ry="16" fill="none" stroke="#E9F5FF" stroke-opacity=".6" stroke-width="2"/>',
          lab(qx, qy + 4, 'gas', '#2A3844', 15)]
    # capillary up and over to the gauge on a post
    gx, gy = P(6.2, 2.4, 0)
    p += [f'<path d="M{qx:.1f},{qy - 32:.1f} V{qy - 92:.1f} H{gx:.1f} V{gy - 120:.1f}" fill="none" stroke="#C9D3DB" stroke-width="5" stroke-linejoin="round"/>',
          box(5.9, 2.1, .6, .6, 2.4, '#8E9AA6', '#4A5560', '#5E6A76'),
          gauge(gx, gy - 128, 30, .62, ACC),
          lab(gx, gy - 86, f'{pb:.2f} kPa', INK, 15)]
    p += [thermo(*P(4.3, 2.6, 2.6), 70, .7, ACC)]
    # card: T = 273.16 × p / p_tp (a straight line through 0), and the two scales side by side
    X = lambda v: 50 + v / 80 * 190
    Y = lambda v: 120 - v / 360 * 96
    s = axes(50, 245, 120, 22) + poly([(X(0), Y(0)), (X(80), Y(Ttp * 80 / ptp))], ACC, 3)
    s += dot(X(ptp), Y(Ttp), AC2) + dot(X(pb), Y(T), ACC)
    s += t_(X(ptp) - 8, Y(Ttp) - 8, f'{Ttp} K', 'ax', 'end', AC2) + t_(X(pb) - 8, Y(T) - 8, f'{T:.2f} K', 'ax', 'end', ACC)
    s += t_(X(ptp), 138, f'{ptp:g}', 'ax') + t_(X(pb), 138, f'{pb:g}', 'ax') + t_(245, 112, 'p, kPa', 'ax', 'end') + t_(44, 30, 'T', 'ax', 'end')
    for x0, top, bot, unit, col in ((300, f'{T:.2f}', f'{Ttp}', 'K', AC2), (390, f'{t:.2f}', '0.01', '°C', ACC)):
        s += f'<rect x="{x0}" y="26" width="16" height="96" rx="8" fill="none" stroke="{AXC}" stroke-width="1.5"/>'
        s += f'<line x1="{x0 - 4}" y1="44" x2="{x0 + 20}" y2="44" stroke="{col}" stroke-width="3"/><line x1="{x0 - 4}" y1="104" x2="{x0 + 20}" y2="104" stroke="{col}" stroke-width="3"/>'
        s += t_(x0 + 26, 49, top, 'ax', 'start', col) + t_(x0 + 26, 109, bot, 'ax', 'start', col) + t_(x0 + 8, 18, unit, 'pt', 'middle', col)
    s += t_(370, 138, f'both rise {riseK:.2f}', 'ax', 'middle', INK)
    card = svgcard(s)
    return make('me-thermo-u1-L2', 'Equilibrium &amp;<br>the Zeroth Law',
                'A rise is the <span class="gold">SAME</span> in K and °C;<br>only levels add <span class="cyan">273.15</span>',
                'the gas thermometer', card, p,
                [chip('left', 268, 'c', f'{ptp:.2f} kPa at {Ttp} K'), chip('left', 470, 'g', f'{pb:.2f} kPa in the bath'),
                 chip('right', 248, 'g', f'{T:.2f} K = {t:.2f} °C'), chip('right', 500, 'c', f'rise {riseK:.2f} K = {riseC:.2f} °C', False)],
                f'T = {Ttp} × {pb:.2f} ÷ {ptp:.2f} = <b class="gl">{T:.2f} K</b><br>'
                f't = <b class="cl">{t:.2f} °C</b>; the rise is {riseK:.2f} in K and in °C')


def u1L3():
    """1.6 worked example: 0.50 kW heater for 2.0 min, 25 kJ of piston work, 15 kJ of heat leaks out"""
    E = 0.50 * 2.0 * 60                                   # 60 kJ from the heater
    Wp, Ql = 25, 15
    Wa, Qa = Wp - E, -Ql                                  # (a) heater inside: W = -35, Q = -15
    Qb, Wb = E - Ql, Wp                                   # (b) gas only: Q = +45, W = +25
    assert (Wa, Qa, Qb, Wb) == (-35, -15, 45, 25) and Qa - Wa == Qb - Wb == 20
    cx, cy = P(4.2, 4.2)
    p = [piston_cyl(4.2, 4.2, 1.35, 3.7, 2.5, AC2)]
    # heater coil inside the gas, its leads out to a supply box
    coil = ' '.join(f'{cx - 36 + 9 * k:.1f},{cy - 26 - (12 if k % 2 else 0):.1f}' for k in range(9))
    p += [f'<polyline points="{coil}" fill="none" stroke="{ACC}" stroke-width="4" stroke-linejoin="round" style="filter:drop-shadow(0 0 5px {ACC})"/>']
    sx, sy = P(1.6, 6.0)
    p += [f'<path d="M{cx - 36:.1f},{cy - 26:.1f} L{cx - 60:.1f},{cy - 14:.1f} L{sx + 20:.1f},{sy - 22:.1f}" fill="none" stroke="#2A323B" stroke-width="3"/>',
          box(1.1, 5.5, 1.1, 1.0, .9, '#3A4652', '#222B33', '#2C3640'), lab(*P(1.65, 6.0, .9), f'{0.50:.2f} kW', '#F6D285', 14)]
    # piston work up, heat leak out
    p += [garrow(cx, cy - 2.5 * U - 14 - 1.2 * U - 4, cx, cy - 2.5 * U - 14 - 1.2 * U - 46, ACC, 6),
          wave(cx + 52, cy - 60, AC2, 2, 30)]
    # card: Q and W bars for the two boundaries; Q − W is +20 kJ both times
    Y0, k = 79, .8
    s = f'<line x1="20" y1="{Y0}" x2="460" y2="{Y0}" stroke="{AXC}" stroke-width="1.5"/>'
    for gx, name, Q, W in ((40, '(a) heater inside', Qa, Wa), (260, '(b) gas only', Qb, Wb)):
        s += t_(gx + 85, 13, name, 'pt', 'middle', INK)
        for bx_, v, col, nm in ((gx + 20, Q, AC2, 'Q'), (gx + 100, W, ACC, 'W')):
            h = abs(v) * k
            y = Y0 - h if v > 0 else Y0
            s += f'<rect x="{bx_}" y="{y:.1f}" width="50" height="{h:.1f}" rx="3" fill="{col}" fill-opacity=".85"/>'
            s += t_(bx_ + 25, (y - 6) if v > 0 else (Y0 + h + 15), f'{nm} {sg(v)}', 'pt', 'middle', col)
    s += t_(235, 138, f'Q − W = +{Qa - Wa:g} kJ on both boundaries', 'ax', 'middle', INK)
    card = svgcard(s)
    return make('me-thermo-u1-L3', 'Work &amp;<br>Heat',
                'Heat <span class="gold">OUT</span> is negative,<br>heat <span class="cyan">IN</span> is positive',
                'two boundaries, one gas', card, p,
                [chip('left', 268, 'g', f'heater {E:g} kJ'), chip('left', 470, 'c', f'{Ql} kJ leaks out'),
                 chip('right', 252, 'g', f'{Wp} kJ piston work'), chip('right', 500, 'c', f'Q = {sg(Qa)} kJ in (a)', False)],
                f'<b class="gl">(a)</b> Q = <b class="gl">{sg(Qa)} kJ</b>, W = {Wp} − {E:g} = {sg(Wa)} kJ<br>'
                f'<b class="cl">(b)</b> Q = {E:g} − {Ql} = <b class="cl">+{Qb:g} kJ</b>, W = +{Wb} kJ; Q − W = +20')



# ================================================================ unit 2
def u2L1():
    """2.2 worked example: 2 kg of air heated at constant pressure from 300 K to 400 K"""
    m, R, cv, cp, T1, T2 = 2, .287, .718, 1.005, 300, 400
    dT = T2 - T1
    dU, dH, dpV = m * cv * dT, m * cp * dT, m * R * dT          # 143.6, 201.0, 57.4 kJ
    Q = dU + dpV
    assert (r1(dU), r1(dH), r1(dpV), r1(Q)) == ('143.6', '201.0', '57.4', '201.0')
    cx, cy = P(4.2, 4.0)
    p = [piston_cyl(4.2, 4.0, 1.35, 3.5, 2.0, ACC, rod=.5)]
    # dead weight on the rod keeps the pressure constant; burner underneath
    top = cy - 2.0 * U - 14 - .5 * U
    p += [T.cyl(cx, top, 30, 17, 30, '#4A5560', '#8E9AA6'), lab(cx, top - 12, f'p const', '#1A222B', 13),
          garrow(cx + 44, top - 4, cx + 44, top - 44, ACC, 5)]
    bx, by = P(4.2, 4.0)
    p += [flame(bx - 22, by + 34, .8), flame(bx + 6, by + 40, 1.0), flame(bx + 32, by + 32, .75)]
    p += [lab(cx, cy - 28, f'{m} kg air', '#0E2238', 16)]
    # card: Q = ΔH, split into ΔU and pΔV
    x0, x1, k = 70, 450, 380 / 210
    s = t_(x0 - 10, 46, 'ΔU', 'pt', 'end', AC2) + t_(x0 - 10, 98, 'Q = ΔH', 'pt', 'start', ACC, ' dx="-60"')
    s += f'<rect x="{x0}" y="28" width="{dU * k:.1f}" height="26" rx="4" fill="{AC2}" fill-opacity=".85"/>'
    s += f'<rect x="{x0 + dU * k:.1f}" y="28" width="{dpV * k:.1f}" height="26" rx="4" fill="{ACC}" fill-opacity=".55"/>'
    s += t_(x0 + dU * k / 2, 47, f'{r1(dU)}', 'pt', 'middle', '#0E2238') + t_(x0 + dU * k + dpV * k / 2, 47, f'{r1(dpV)}', 'pt', 'middle', '#0E2238')
    s += t_(x0 + dU * k + dpV * k / 2, 20, 'pΔV', 'ax', 'middle', ACC)
    s += f'<rect x="{x0}" y="80" width="{dH * k:.1f}" height="26" rx="4" fill="{ACC}" fill-opacity=".9"/>'
    s += t_(x0 + dH * k / 2, 99, f'{r1(dH)} kJ', 'pt', 'middle', '#0E2238')
    s += t_(250, 134, f'{r1(dU)} + {r1(dpV)} = {r1(dH)} kJ', 'ax', 'middle', INK)
    card = svgcard(s)
    return make('me-thermo-u2-L1', 'First Law,<br>Internal Energy<br>&amp; Enthalpy',
                'Rigid tank: Q = <span class="gold">ΔU</span>;<br>constant pressure: Q = <span class="cyan">ΔH</span>',
                'air heated at constant p', card, p,
                [chip('left', 262, 'c', f'{T1} K → {T2} K'), chip('left', 470, 'c', f'ΔU = {r1(dU)} kJ'),
                 chip('right', 262, 'g', f'pΔV = {r1(dpV)} kJ'), chip('right', 500, 'g', f'Q = ΔH = {r1(dH)} kJ', False)],
                f'ΔU = {m} × {cv} × {dT} = <b class="cl">{r1(dU)} kJ</b>, ΔH = <b class="gl">{r1(dH)} kJ</b><br>'
                f'Q = ΔU + pΔV = {r1(dU)} + {r1(dpV)} = <b class="gl">{r1(Q)} kJ</b>')


def u2L2():
    """2.4 worked example 2 (with example 1 for the other two paths): 1 kg air, 300 K, 100 kPa, squeezed to 1/8 along pV^1.3"""
    R, cv, g_, n, T1, p1, r = .287, .718, 1.4, 1.3, 300, 100, 8
    V1 = R * T1 / p1; V2 = V1 / r
    p2 = p1 * r ** n; T2 = T1 * r ** (n - 1)                    # 1493 kPa, 559.8 K
    W = R * (T1 - T2) / (n - 1); dU = cv * (T2 - T1); Q = dU + W   # −248.6, +186.6, −62.0 kJ
    p2i, p2a = p1 * r, p1 * r ** g_                              # 800 and 1838 kPa (example 1)
    assert (f'{p2:.0f}', r1(T2), r1(W), r1(dU), r1(Q), f'{p2a:.0f}') == ('1493', '559.8', '-248.6', '186.6', '-62.0', '1838')
    # board: a horizontal cylinder, the piston driven in from the left, heat leaving through the wall
    p = [tube('x', 2.2, 6.6, 4.0, 1.25, 1.05, 'url(#tv)', 'url(#dm)')]
    p += [box(2.0, 3.6, .25, .8, 1.9, '#E9EEF2', '#8E9AA6', '#B7C2CC', z0=.3)]
    (ax_, ay_), (bx_, by_) = P(.4, 4.0, 1.25), P(2.0, 4.0, 1.25)
    p += [f'<line x1="{ax_:.1f}" y1="{ay_:.1f}" x2="{bx_:.1f}" y2="{by_:.1f}" stroke="url(#tk)" stroke-width="10" stroke-linecap="round"/>',
          garrow(*P(-.3, 2.6, 1.9), *P(1.5, 2.6, 1.9), ACC, 6)]
    wx, wy = P(4.6, 3.0, 2.6)
    p += [wave(wx - 10, wy - 26, AC2, 3, 30), thermo(*P(5.8, 4.0, 2.35), 64, .82, ACC)]
    # card: three compressions on the p–V plane (volume falls to the right), the polytropic one bold
    X = lambda v: 40 + (V1 - v) / (V1 - V2) * 290
    Y = lambda pp: 122 - pp / 1900 * 100
    def path(k):
        return [(X(V1 - (V1 - V2) * i / 60), Y(p1 * (V1 / (V1 - (V1 - V2) * i / 60)) ** k)) for i in range(61)]
    s = axes(40, 336, 122, 18)
    s += poly(path(1), '#9FB0BF', 2) + poly(path(g_), AC2, 2.2) + poly(path(n), ACC, 4)
    s += dot(X(V2), Y(p2a), AC2, 4) + dot(X(V2), Y(p2), ACC, 5) + dot(X(V2), Y(p2i), '#9FB0BF', 4)
    s += t_(346, Y(p2a) + 5, f'pV<tspan dy="-6" font-size="10">1.4</tspan><tspan dy="6">: {p2a:.0f}</tspan>', 'ax', 'start', AC2)
    s += t_(346, Y(p2) + 9, f'pV<tspan dy="-6" font-size="11">1.3</tspan><tspan dy="6">: {p2:.0f}</tspan>', 'pt', 'start', ACC)
    s += t_(346, Y(p2i) + 5, f'pV = C: {p2i:.0f}', 'ax', 'start', '#9FB0BF')
    s += t_(X(V1), 138, f'{V1:.3f}', 'ax', 'start') + t_(X(V2), 138, f'{V2:.4f} m³', 'ax', 'end') + t_(34, 26, 'p', 'ax', 'end') + t_(460, 138, 'kPa', 'ax', 'end')
    card = svgcard(s)
    return make('me-thermo-u2-L2', 'Specific Heats<br>&amp; Non-flow<br>Processes',
                'Hotter does <span class="gold">NOT</span> mean heat in:<br>this gas <span class="cyan">REJECTS</span> 62 kJ',
                f'1 kg air squeezed to 1/{r}', card, p,
                [chip('left', 262, 'g', f'W = {sg(float(r1(W)), '.1f')} kJ'), chip('left', 470, 'c', f'Q = {sg(float(r1(Q)), '.1f')} kJ'),
                 chip('right', 262, 'g', f'{T1} K → {r1(T2)} K'), chip('right', 500, 'c', f'ΔU = {sg(float(r1(dU)), '.1f')} kJ', False)],
                f'pV<sup>1.3</sup>: T₂ = {T1} × {r}<sup>0.3</sup> = <b class="gl">{r1(T2)} K</b>, W = {sg(float(r1(W)), '.1f')} kJ<br>'
                f'Q = ΔU + W = {r1(dU)} − {abs(float(r1(W)))} = <b class="cl">{sg(float(r1(Q)), '.1f')} kJ</b>')


def u2L3():
    """2.5 worked example: three claimed cyclic engines"""
    claims = [('(a)', 300, 500, 0), ('(b)', 200, 250, 0), ('(c)', 80, 60, 20)]
    res = []
    for nm, qin, w, qout in claims:
        created = w - (qin - qout)
        res.append((nm, qin, w, qout, created, w / qin))
    assert [x[4] for x in res] == [200, 50, 0] and abs(res[1][5] - 1.25) < 1e-9 and abs(res[2][5] - .75) < 1e-9
    qin, w, qout = 80, 60, 20
    # board: claim (c): an engine block, heat in from a burner, 20 kW to the river, 60 kW on the shaft
    p = [box(3.0, 3.0, 2.4, 2.0, 1.9, '#8E9AA6', '#3F4A55', '#5E6A76'),
         box(3.3, 3.25, 1.8, 1.5, .25, '#B7C2CC', '#6E7B88', '#8E9AA6', z0=1.9)]
    for k in range(4):
        p.append(f'<polyline points="{pts(P(3.0 + .5 + k * .45, 5.0, .35), P(3.0 + .5 + k * .45, 5.0, 1.6))}" stroke="#2C3640" stroke-width="3"/>')
    # river: a strip of water along the right edge
    p += [f'<polygon points="{pts(P(6.4, 0.3), P(7.7, 0.3), P(7.7, 7.7), P(6.4, 7.7))}" fill="{WATER}" fill-opacity=".55"/>']
    for k in range(5):
        p.append(f'<path d="M{P(7.0, 1.0 + k * 1.4)[0]:.1f},{P(7.0, 1.0 + k * 1.4)[1]:.1f} q6,-4 12,0 t12,0" fill="none" stroke="#CFE9FF" stroke-width="2" opacity=".7"/>')
    p += [tube('y', 5.0, 7.4, 3.9, 1.0, .28, 'url(#tv)', 'url(#dm)')]
    sx, sy = P(3.9, 7.4, 1.0)
    p += [f'<path d="M{sx - 30:.1f},{sy + 16:.1f} A32,20 0 1 1 {sx + 26:.1f},{sy + 18:.1f}" fill="none" stroke="{ACC}" stroke-width="4" marker-end="url(#ao)"/>']
    fx, fy = P(2.4, 2.0)
    p += [flame(fx, fy + 6, 1.0), flame(fx + 24, fy + 2, .8), garrow(fx + 30, fy - 46, *P(3.2, 3.0, 1.5), ACC, 5)]
    rx_, ry_ = P(5.4, 3.6, 1.2)
    p += [wave(rx_ + 6, ry_ - 6, AC2, 2, 28)]
    # card: heat in against work out for the three claims
    s = ''
    for k, (nm, qi, ww, qo, cr, eta) in enumerate(res):
        x = 40 + k * 145
        hq, hw = qi / 500 * 92, ww / 500 * 92
        s += f'<rect x="{x}" y="{112 - hq:.1f}" width="40" height="{hq:.1f}" rx="3" fill="{AC2}" fill-opacity=".85"/>'
        s += f'<rect x="{x + 46}" y="{112 - hw:.1f}" width="40" height="{hw:.1f}" rx="3" fill="{ACC}" fill-opacity=".85"/>'
        s += t_(x + 20, 108 - hq, f'{qi}', 'ax', 'middle', AC2) + t_(x + 66, 108 - hw, f'{ww}', 'ax', 'middle', ACC)
        ok = cr == 0
        s += t_(x + 43, 132, f'{nm} {"η " + format(eta * 100, "g") + " %" if ok else "PMM-1"}', 'pt', 'middle', AC2 if ok else ACC)
    s += f'<line x1="30" y1="112" x2="460" y2="112" stroke="{AXC}" stroke-width="1.5"/>'
    s += t_(456, 16, '<tspan fill="#7CC4FF">■ heat in</tspan>  <tspan fill="#FF9E5A">■ work out, kW</tspan>', 'ax', 'end')
    card = svgcard(s)
    return make('me-thermo-u2-L3', 'Perpetual Motion<br>&amp; the Steady<br>Flow Equation',
                'Work <span class="gold">ABOVE</span> heat in = PMM-1;<br>20 % passes the <span class="cyan">first law</span>',
                'three engine claims', card, p,
                [chip('left', 262, 'g', f'{qin} kW heat in'), chip('left', 470, 'g', f'{w} kW shaft work'),
                 chip('right', 380, 'c', f'{qout} kW to the river'), chip('right', 500, 'c', f'η = {w / qin * 100:g} %: allowed', False)],
                f'(a) {res[0][2]} &gt; {res[0][1]} kW, (b) {res[1][2]}/{res[1][1]} = {res[1][5] * 100:g} %: <b class="gl">PMM-1</b><br>'
                f'(c) {qin} − {qout} = {w} kW = W, η = <b class="cl">{w / qin * 100:g} %</b>: allowed')


def u2L4():
    """2.7 worked example: an evacuated, insulated 0.2 m³ tank filled from a 500 kPa, 27 °C line"""
    V, pL, Ti, R, cv, cp = .2, 500, 27 + 273, .287, .718, 1.005
    hi, ui, fw = cp * Ti, cv * Ti, R * Ti                       # 301.5, 215.4, 86.1 kJ/kg
    T2 = hi / cv                                               # 419.9 K ≈ 420 K = γ Ti
    m2 = pL * V / (R * 420)                                    # 0.830 kg
    assert (r1(hi), r1(ui), r1(fw), r1(T2), f'{m2:.3f}') == ('301.5', '215.4', '86.1', '419.9', '0.830')
    # board: a lagged tank lying on two saddles, fed from the line through a valve
    p = [box(3.0, 3.0, .5, 2.4, .7, '#5E6A76', '#2C3640', '#3A4652'), box(5.4, 3.0, .5, 2.4, .7, '#5E6A76', '#2C3640', '#3A4652'),
         tube('x', 2.3, 6.7, 4.2, 1.55, 1.15, 'url(#hot)', '#FFD3AE', None)]
    for a in (3.1, 3.9, 4.7, 5.5, 6.3):
        p.append(f'<polyline points="{pts(*ring(a, 4.2, 1.55, 1.16, "x")[10:31])}" fill="none" stroke="#C2622E" stroke-width="2" stroke-dasharray="5 4"/>')
    p += [lab(*P(6.7, 4.2, 1.45), f'{420} K', '#7A2E0E', 17)]
    p += [pipe([(4.5, 0.2), (4.5, 2.5)], 2.65, '#8E9AA6', 9), pipe([(4.5, 2.5), (4.5, 2.5)], 2.65)]
    vx, vy = P(4.5, 1.5, 2.65)
    p += [f'<circle cx="{vx:.1f}" cy="{vy - 14:.1f}" r="12" fill="none" stroke="#E04848" stroke-width="5"/><line x1="{vx:.1f}" y1="{vy - 2:.1f}" x2="{vx:.1f}" y2="{vy - 10:.1f}" stroke="#E04848" stroke-width="4"/>',
          garrow(*P(4.5, 0.0, 3.3), *P(4.5, 1.2, 3.3), AC2, 5),
          lab(*P(4.5, -.2, 3.55), f'{pL} kPa, {Ti - 273} °C', AC2, 14)]
    # card: energy per kg of the entering air
    x0, k = 110, 330 / 310
    s = t_(x0 - 10, 44, 'line air', 'pt', 'end', INK) + t_(x0 - 10, 98, 'tank air', 'pt', 'end', INK)
    s += f'<rect x="{x0}" y="26" width="{ui * k:.1f}" height="26" rx="4" fill="{AC2}" fill-opacity=".85"/>'
    s += f'<rect x="{x0 + ui * k:.1f}" y="26" width="{fw * k:.1f}" height="26" rx="4" fill="{ACC}" fill-opacity=".9"/>'
    s += t_(x0 + ui * k / 2, 45, f'u<tspan font-size="11" dy="3">i</tspan><tspan dy="-3"> {r1(ui)}</tspan>', 'pt', 'middle', '#0E2238')
    s += t_(x0 + ui * k + fw * k / 2, 45, f'+{r1(fw)}', 'pt', 'middle', '#0E2238') + t_(x0 + ui * k + fw * k / 2, 18, 'flow work', 'ax', 'middle', ACC)
    s += f'<rect x="{x0}" y="80" width="{hi * k:.1f}" height="26" rx="4" fill="{ACC}" fill-opacity=".55"/>'
    s += t_(x0 + hi * k / 2, 99, f'u₂ = h<tspan font-size="11" dy="3">i</tspan><tspan dy="-3"> = {r1(hi)} kJ/kg</tspan>', 'pt', 'middle', INK)
    s += t_(250, 136, f'T₂ = {r1(hi)} ÷ {cv} = {r1(T2)} K', 'ax', 'middle', INK)
    card = svgcard(s)
    return make('me-thermo-u2-L4', 'Unsteady Flow<br>&amp; the Limits of<br>the First Law',
                'The line\'s <span class="gold">FLOW WORK</span> goes in:<br>T₂ = γT<sub>i</sub> = <span class="cyan">420 K</span>',
                'filling an empty tank', card, p,
                [chip('left', 262, 'c', f'{pL} kPa, {Ti} K line'), chip('left', 470, 'g', f'flow work {r1(fw)} kJ/kg'),
                 chip('right', 262, 'g', f'T₂ ≈ 420 K ({420 - 273} °C)'), chip('right', 500, 'c', f'm₂ = {m2:.3f} kg', False)],
                f'u₂ = h<sub>i</sub>: {cv} T₂ = {cp} × {Ti} = {r1(hi)} kJ/kg<br>'
                f'T₂ = {r1(T2)} ≈ <b class="gl">420 K</b>; m₂ = {pL * V:g} ÷ {R * 420:.2f} = <b class="cl">{m2:.3f} kg</b>')



# ================================================================ unit 3
def u3L1():
    """3.1 worked example (a): 800 kJ from 600 K, 500 kJ rejected to 300 K"""
    Q1, Q2, TH, TL = 800, 500, 600, 300
    W = Q1 - Q2; eta = W / Q1; eta_rev = 1 - TL / TH; wrong = W / Q2
    assert W == 300 and abs(eta - .375) < 1e-12 and abs(eta_rev - .5) < 1e-12
    p = [reservoir(.6, .8, 2.6, 2.4, 1.5, True, f'{TH} K'), engine(4.3, 4.1, 1.0, 1.4), reservoir(5.3, 5.5, 2.2, 1.9, .8, False, f'{TL} K')]
    p += [garrow(*P(3.1, 2.6, 1.0), *P(3.7, 3.4, 1.0), ACC, 7), garrow(*P(4.9, 4.9, .6), *P(5.5, 5.6, .9), AC2, 7)]
    sx, sy = P(5.4, 4.1, .8)
    p += [tube('x', 5.2, 6.8, 4.1, .8, .22), garrow(*P(6.9, 4.1, .8), *P(7.9, 4.1, .8), ACC, 6)]
    # card: the heat split; efficiency is W over heat IN
    rows = [('Q₁ in', Q1, ACC, f'{Q1} kJ'), ('W', W, '#FFC79E', f'{W} kJ'), ('Q₂ out', Q2, AC2, f'{Q2} kJ')]
    s = hbars(rows, 0, 460, 10, 24, 10, Q1 * 1.25, 90)
    s += t_(235, 132, f'η = W/Q₁ = {W}/{Q1} = {eta * 100:g} %   (not W/Q₂ = {wrong * 100:g} %)', 'ax', 'middle', INK)
    card = svgcard(s)
    return make('me-thermo-u3-L1', 'Heat Engines<br>&amp; the Second<br>Law',
                'Efficiency = W over heat <span class="gold">IN</span>,<br>never over heat <span class="cyan">OUT</span>',
                'engine, two reservoirs', card, p,
                [chip('left', 262, 'g', f'Q₁ = {Q1} kJ at {TH} K'), chip('left', 470, 'c', f'Q₂ = {Q2} kJ to {TL} K'),
                 chip('right', 300, 'g', f'W = {W} kJ'), chip('right', 500, 'c', f'limit {eta_rev * 100:g} %', False)],
                f'W = {Q1} − {Q2} = <b class="gl">{W} kJ</b>; η = {W} ÷ {Q1} = <b class="gl">{eta * 100:g} %</b><br>'
                f'reversible limit 1 − {TL}/{TH} = <b class="cl">{eta_rev * 100:g} %</b>: allowed')


def u3L2():
    """3.3 worked example: 0.5 kg air at 300 K, 0.2 → 0.4 m³, reversible isothermal against free expansion"""
    m, R, T0, V1, V2 = .5, .287, 300, .2, .4
    mRT = m * R * T0                                         # 43.05 kJ
    Wrev = mRT * ln(V2 / V1)                                  # 29.84 kJ
    pA, pB = mRT / V1, mRT / V2                               # 215.3, 107.6 kPa
    assert (f'{mRT:.2f}', r2(Wrev), r1(pA), r1(pB)) == ('43.05', '29.84', '215.3', '107.6')
    # board: a flask of air joined through a valve to an evacuated flask of the same size
    p = [vessel(2.9, 4.9, 1.05, 2.6, AC2, .45), vessel(5.6, 2.4, 1.05, 2.6, '#0B1418', .7)]
    (ax_, ay_), (bx_, by_) = P(2.9, 4.9, 1.9), P(5.6, 2.4, 1.9)
    mx, my = (ax_ + bx_) / 2, (ay_ + by_) / 2
    p += [f'<line x1="{ax_ + 30:.1f}" y1="{ay_:.1f}" x2="{bx_ - 30:.1f}" y2="{by_:.1f}" stroke="#8E9AA6" stroke-width="10" stroke-linecap="round"/>',
          f'<rect x="{mx - 12:.1f}" y="{my - 14:.1f}" width="24" height="28" rx="4" fill="#3A444E"/><circle cx="{mx:.1f}" cy="{my - 24:.1f}" r="11" fill="none" stroke="#E04848" stroke-width="5"/>',
          garrow(mx - 30, my + 40, mx + 34, my + 4, ACC, 5)]
    p += [lab(*P(2.9, 4.9, 1.1), 'air', '#0E2238', 17), lab(*P(5.6, 2.4, 1.1), 'vacuum', '#9FB0BF', 15)]
    # card: the reversible isotherm and its area; the free expansion delivers nothing
    X = lambda v: 60 + (v - .15) / .3 * 360
    Y = lambda pp: 122 - pp / 240 * 100
    iso = [(X(V1 + (V2 - V1) * i / 40), Y(mRT / (V1 + (V2 - V1) * i / 40))) for i in range(41)]
    s = axes(60, 440, 122, 18)
    s += poly(iso + [(X(V2), Y(0)), (X(V1), Y(0))], ACC, 0, ACC, .25) + poly(iso, ACC, 3.5)
    s += dot(X(V1), Y(pA), ACC) + dot(X(V2), Y(pB), ACC)
    s += t_(X(V1) + 8, Y(pA) - 6, f'{r1(pA)} kPa', 'ax', 'start', ACC) + t_(X(V2) + 8, Y(pB) - 6, f'{r1(pB)}', 'ax', 'start', ACC)
    s += t_((X(V1) + X(V2)) / 2, 108, f'W<tspan font-size="11" dy="3">rev</tspan><tspan dy="-3"> = {r2(Wrev)} kJ</tspan>', 'pt', 'middle', '#FFE1C7')
    s += t_(X(V1), 138, f'{V1}', 'ax') + t_(X(V2), 138, f'{V2} m³', 'ax') + t_(54, 26, 'p', 'ax', 'end')
    s += t_(440, 30, 'free expansion: W = 0', 'pt', 'end', AC2)
    card = svgcard(s)
    return make('me-thermo-u3-L2', 'Reversible<br>Processes &amp; the<br>Carnot Cycle',
                'Slow is not enough: <span class="gold">NO</span> friction,<br><span class="cyan">NO</span> free expansion',
                'one end state, two paths', card, p,
                [chip('left', 262, 'c', f'{m} kg air, {T0} K'), chip('left', 470, 'g', f'W<sub>rev</sub> = {r2(Wrev)} kJ'),
                 chip('right', 262, 'c', f'{V1} → {V2} m³'), chip('right', 500, 'c', 'free: W = 0', False)],
                f'W<sub>rev</sub> = mRT ln 2 = {mRT:.2f} × 0.6931 = <b class="gl">{r2(Wrev)} kJ</b><br>'
                f'free expansion: W = <b class="cl">0</b>, so all {r2(Wrev)} kJ is lost')


def u3L3():
    """3.6 worked example: 500 kJ in at 600 K, 300 kJ out at 300 K, 200 kJ of work"""
    Q1, T1, Q2, T2 = 500, 600, -300, 300
    a, b = Q1 / T1, Q2 / T2
    cyc = a + b                                              # −0.1667 kJ/K
    W = Q1 + Q2; eta = W / Q1; etaC = 1 - T2 / T1
    assert (f'{a:.4f}', f'{b:.4f}', f'{cyc:.3f}', W, eta, etaC) == ('0.8333', '-1.0000', '-0.167', 200, .4, .5)
    # board: the gas in a cylinder runs the cycle between a hot plate and a cold plate; work leaves on the rod
    p = [reservoir(.4, 4.9, 2.4, 2.7, .45, True, f'{T1} K'), reservoir(4.9, .4, 2.7, 2.4, .45, False, f'{T2} K'),
         piston_cyl(4.1, 4.1, 1.15, 3.2, 1.9, '#FFC79E', rod=.9)]
    p += [garrow(*P(2.5, 5.2, .7), *P(3.2, 4.6, 1.0), ACC, 7), garrow(*P(5.0, 3.6, 1.0), *P(5.6, 2.9, .7), AC2, 7)]
    ex, ey = P(4.1, 4.1, 1.9)
    p += [garrow(ex, ey - 14 - .9 * U - 4, ex, ey - 14 - .9 * U - 48, ACC, 6)]
    # card: the two δQ/T terms and their sum
    Y0, k = 66, 50
    s = f'<line x1="30" y1="{Y0}" x2="460" y2="{Y0}" stroke="{AXC}" stroke-width="1.5"/>'
    for x, v, col, lb in ((70, a, ACC, f'{Q1}/{T1}'), (190, b, AC2, f'{Q2}/{T2}'.replace('-', '−')), (330, cyc, '#FFC79E', '∮δQ/T')):
        h = abs(v) * k
        y = Y0 - h if v > 0 else Y0
        s += f'<rect x="{x}" y="{y:.1f}" width="70" height="{h:.1f}" rx="3" fill="{col}" fill-opacity=".85"/>'
        s += t_(x + 35, (y - 6) if v > 0 else (Y0 + h + 16), f'{sg(v, ".3f")}', 'pt', 'middle', col)
        s += t_(x + 35, Y0 - 6 if v < 0 else Y0 + 16, lb, 'ax', 'middle', INK)
    s += t_(456, 16, 'kJ/K', 'ax', 'end')
    card = svgcard(s)
    return make('me-thermo-u3-L3', 'The Kelvin Scale<br>&amp; the Clausius<br>Inequality',
                '∮δQ/T <span class="gold">below 0</span>: irreversible;<br>above 0 would be <span class="cyan">impossible</span>',
                'test one cycle', card, p,
                [chip('left', 262, 'g', f'{Q1} kJ in at {T1} K'), chip('right', 262, 'c', f'{-Q2} kJ out at {T2} K'),
                 chip('left', 470, 'g', f'W = {W} kJ, η = {eta * 100:g} %'), chip('right', 500, 'c', f'Carnot {etaC * 100:g} %', False)],
                f'∮δQ/T = {Q1}/{T1} − {-Q2}/{T2} = <b class="gl">{sg(cyc, ".3f")} kJ/K</b> &lt; 0<br>'
                f'<b class="cl">irreversible</b>, not impossible: {eta * 100:g} % &lt; {etaC * 100:g} %')


def u3L4():
    """3.8 worked example: 2 kg of water at 80 °C mixed with 3 kg at 20 °C in an insulated vessel"""
    m1, T1, m2, T2, cp = 2, 353, 3, 293, 4.187
    Tf = (m1 * T1 + m2 * T2) / (m1 + m2)                     # 317 K
    dS1 = m1 * cp * ln(Tf / T1); dS2 = m2 * cp * ln(Tf / T2); dS = dS1 + dS2
    assert (Tf, f'{dS1:.4f}', f'{dS2:.4f}', f'{dS:.4f}') == (317, '-0.9008', '0.9889', '0.0882')
    cx, cy = P(4.0, 4.0)
    p = [f'<ellipse cx="{cx:.1f}" cy="{cy - 40:.1f}" rx="{1.75 * U * 1.2247:.1f}" ry="{1.75 * U * .7071:.1f}" fill="none" stroke="{AXC}" stroke-width="2" stroke-dasharray="8 6"/>',
         vessel(4.0, 4.0, 1.45, 2.7, 'url(#mix)', .75)]
    p += [f'<line x1="{cx:.1f}" y1="{cy + 22:.1f}" x2="{cx:.1f}" y2="{cy - 2.7 * U + 22:.1f}" stroke="#E6ECF1" stroke-width="2" stroke-dasharray="6 5"/>',
          lab(cx - 30, cy - 30, f'{m1} kg', '#4A1A06', 17), lab(cx + 30, cy - 30, f'{m2} kg', '#0E2238', 17),
          thermo(cx + 4, cy - 2.7 * U - 6, 64, .45, '#FFC79E')]
    # card: entropy changes; one falls, the total rises
    Y0, k = 70, 52
    s = f'<line x1="30" y1="{Y0}" x2="460" y2="{Y0}" stroke="{AXC}" stroke-width="1.5"/>'
    for x, v, col, lb in ((60, dS1, HOT, 'hot water'), (190, dS2, COLD, 'cold water'), (330, dS, '#FFC79E', 'total')):
        h = abs(v) * k
        y = Y0 - h if v > 0 else Y0
        s += f'<rect x="{x}" y="{y:.1f}" width="80" height="{max(h, 3):.1f}" rx="3" fill="{col}" fill-opacity=".9"/>'
        s += t_(x + 40, (y - 6) if v > 0 else (Y0 + h + 16), f'{sg(v, ".4f")}', 'pt', 'middle', col)
        s += t_(x + 40, Y0 - 6 if v < 0 else Y0 + 16, lb, 'ax', 'middle', INK)
    s += t_(456, 16, 'ΔS, kJ/K', 'ax', 'end')
    card = svgcard(s)
    return make('me-thermo-u3-L4', 'Entropy &amp; the<br>Principle of<br>Increase',
                'One part\'s entropy can <span class="gold">FALL</span>;<br>the total still <span class="cyan">RISES</span>',
                'mixing hot and cold', card, p,
                [chip('left', 262, 'g', f'{m1} kg at {T1 - 273} °C'), chip('right', 262, 'c', f'{m2} kg at {T2 - 273} °C'),
                 chip('left', 470, 'g', f'mix: {Tf:g} K = {Tf - 273:g} °C'), chip('right', 500, 'c', f'S<sub>gen</sub> = {sg(dS, ".4f")} kJ/K', False)],
                f'T<sub>f</sub> = ({m1}×{T1} + {m2}×{T2}) ÷ {m1 + m2} = <b class="gl">{Tf:g} K</b> = {Tf - 273:g} °C<br>'
                f'ΔS = {sg(dS1, ".4f")} {sg(dS2, ".4f")} = <b class="cl">{sg(dS, ".4f")} kJ/K</b> &gt; 0')


def u3L5():
    """3.10 worked example: Debye solid, cp = aT³ with a = 0.002 J/(mol·K⁴), S at 10 K"""
    a, Tt = .002, 10
    S = a * Tt ** 3 / 3                                      # 0.667 J/(mol·K)
    cp10 = a * Tt ** 3                                       # 2 J/(mol·K)
    assert f'{S:.3f}' == '0.667'
    # board: a small crystal on a cold stage, a heater wire, a thermometer at 10 K
    p = [box(2.6, 2.6, 2.8, 2.8, .5, '#A9DBFF', '#2F6E9C', '#3F86BE')]
    atoms = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                atoms.append((3.2 + i * .8, 3.2 + j * .8, .9 + k * .8))
    bonds = ''
    for (x, y, z) in atoms:
        for dx, dy, dz in ((.8, 0, 0), (0, .8, 0), (0, 0, .8)):
            if (round(x + dx, 1), round(y + dy, 1), round(z + dz, 1)) in [(round(a_, 1), round(b_, 1), round(c_, 1)) for a_, b_, c_ in atoms]:
                bonds += f'<line x1="{P(x, y, z)[0]:.1f}" y1="{P(x, y, z)[1]:.1f}" x2="{P(x + dx, y + dy, z + dz)[0]:.1f}" y2="{P(x + dx, y + dy, z + dz)[1]:.1f}"/>'
    p.append(f'<g stroke="#9FB0BF" stroke-width="3">{bonds}</g>')
    for (x, y, z) in sorted(atoms, key=lambda q: (q[0] + q[1], q[2])):
        X_, Y_ = P(x, y, z)
        p.append(f'<circle cx="{X_:.1f}" cy="{Y_:.1f}" r="10" fill="url(#bulb)" stroke="#56626E" stroke-width="1.2"/>')
    p += [thermo(*P(6.3, 3.4, .1), 72, .12, AC2), lab(*P(6.3, 3.4, 2.75), f'{Tt} K', AC2, 16)]
    # card: S = aT³/3 and cp = aT³ from 0 to 10 K
    X = lambda T_: 50 + T_ / Tt * 330
    Y = lambda v: 120 - v / 2.2 * 100
    cpc = [(X(i / 4), Y(a * (i / 4) ** 3)) for i in range(41)]
    Sc = [(X(i / 4), Y(a * (i / 4) ** 3 / 3)) for i in range(41)]
    s = axes(50, 400, 120, 18) + poly(cpc, AC2, 2.5, dash='7 5') + poly(Sc, ACC, 4)
    s += dot(X(Tt), Y(S), ACC) + dot(X(Tt), Y(cp10), AC2, 4) + dot(X(0), Y(0), INK, 4)
    s += t_(X(Tt) + 10, Y(S) + 5, f'S = {S:.3f}', 'pt', 'start', ACC) + t_(X(Tt) + 10, Y(cp10) + 5, f'c<tspan font-size="11" dy="3">p</tspan><tspan dy="-3"> = {cp10:g}</tspan>', 'pt', 'start', AC2)
    s += t_(X(0), 138, '0 K', 'ax') + t_(X(Tt), 138, f'{Tt} K', 'ax') + t_(X(0) + 8, 112, 'S = 0', 'ax', 'start', INK)
    s += t_(44, 26, 'J/(mol·K)', 'ax', 'start')
    card = svgcard(s)
    return make('me-thermo-u3-L5', 'Entropy<br>Generation &amp; the<br>Third Law',
                'S starts at <span class="gold">ZERO</span> at 0 K,<br>never <span class="cyan">minus infinity</span>',
                'a solid near 0 K', card, p,
                [chip('left', 262, 'c', 'c<sub>p</sub> = 0.002 T³'), chip('left', 470, 'c', 'S = 0 at 0 K'),
                 chip('right', 262, 'g', f'S = {S:.3f} J/(mol·K)'), chip('right', 500, 'c', 'c<sub>p</sub> → 0 as T → 0', False)],
                f'dS = c<sub>p</sub> dT/T = aT² dT, so S = aT³/3 from 0 K<br>'
                f'S = {a} × {Tt ** 3} ÷ 3 = <b class="gl">{S:.3f} J/(mol·K)</b> at {Tt} K')



# ================================================================ unit 4
def u4L1():
    """4.1 worked example: 10 kg of water at 360 K cooled to the surroundings at 300 K"""
    m, c, T1, T0 = 10, 4.18, 360, 300
    Q = m * c * (T1 - T0)                                    # 2508 kJ
    dS = m * c * ln(T1 / T0)                                 # 7.621 kJ/K
    UE = T0 * dS; AE = Q - UE                                # 2286.3, 221.7 kJ
    share = AE / Q
    assert (f'{Q:.0f}', f'{dS:.3f}', r1(UE), r1(AE), f'{share * 100:.1f}') == ('2508', '7.621', '2286.3', '221.7', '8.8')
    p = [vessel(2.6, 4.4, 1.3, 2.8, HOT, .7), lab(*P(2.6, 4.4, 1.2), f'{m} kg', '#4A1A06', 17), thermo(*P(2.6, 4.4, 3.0), 60, .8, ACC),
         engine(5.3, 3.4, .75, 1.2)]
    p += [garrow(*P(3.7, 4.2, 1.4), *P(4.6, 3.6, 1.0), ACC, 7)]
    ex, ey = P(5.3, 3.4, 1.2)
    p += [garrow(ex, ey - 20, ex, ey - 72, '#FFC79E', 6), wave(*P(6.1, 4.4, .9), AC2, 2, 28)]
    # card: T–s; the strip above T0 is available, the block below is not
    S_ = lambda T_: m * c * ln(T_ / T0)
    X = lambda s_: 70 + s_ / dS * 330
    Y = lambda T_: 124 - T_ / 420 * 104
    cur = [(X(S_(T0 + (T1 - T0) * i / 30)), Y(T0 + (T1 - T0) * i / 30)) for i in range(31)]
    s = axes(70, 440, 124, 16)
    s += f'<rect x="{X(0)}" y="{Y(T0):.1f}" width="{X(dS) - X(0):.1f}" height="{Y(0) - Y(T0):.1f}" fill="{AC2}" fill-opacity=".30"/>'
    s += poly(cur + [(X(dS), Y(T0))], ACC, 0, ACC, .55) + poly(cur, ACC, 3.5)
    s += f'<line x1="70" y1="{Y(T0):.1f}" x2="440" y2="{Y(T0):.1f}" stroke="{AC2}" stroke-width="2" stroke-dasharray="6 4"/>'
    s += t_(64, Y(T1) + 5, f'{T1}', 'ax', 'end', ACC) + t_(64, Y(T0) + 12, f'{T0} K', 'ax', 'end', AC2)
    s += t_(X(dS) - 6, Y(T1) - 8, f'AE {r1(AE)} kJ', 'pt', 'end', ACC) + t_(X(dS / 2), Y(T0 / 2) + 6, f'UE = T₀ΔS = {r1(UE)} kJ', 'pt', 'middle', '#CFE9FF')
    s += t_(X(dS), 140, f'ΔS = {dS:.3f} kJ/K', 'ax', 'end')
    card = svgcard(s)
    return make('me-thermo-u4-L1', 'Available<br>Energy &amp;<br>Exergy',
                'Only <span class="gold">8.8 %</span> of this heat can<br>do work: the rest is <span class="cyan">unavailable</span>',
                'warm water as a source', card, p,
                [chip('left', 262, 'g', f'{m} kg water, {T1} K'), chip('left', 470, 'g', f'Q = {Q:.0f} kJ'),
                 chip('right', 262, 'g', f'AE = {r1(AE)} kJ'), chip('right', 500, 'c', f'T₀ = {T0} K', False)],
                f'ΔS = {m * c:g} ln 1.2 = {dS:.3f} kJ/K; UE = <b class="cl">{r1(UE)} kJ</b><br>'
                f'AE = {Q:.0f} − {r1(UE)} = <b class="gl">{r1(AE)} kJ</b>, about {share * 100:.1f} %')


def u4L2():
    """4.3 worked example: the cyclic relation for air at 300 K and 100 kPa"""
    R, T0, p0 = .287, 300, 100
    v = R * T0 / p0                                          # 0.861 m³/kg
    dpdv, dvdT, dTdp = -R * T0 / v ** 2, R / p0, v / R       # −116.1, 0.00287, 3.000
    prod = dpdv * dvdT * dTdp
    dpdT = R / v
    assert (f'{v:.3f}', r1(dpdv), f'{dvdT:.5f}', f'{dTdp:.3f}', f'{prod:.3f}', f'{dpdT:.4f}') == ('0.861', '-116.1', '0.00287', '3.000', '-1.000', '0.3333')
    cx, cy = P(4.0, 4.2)
    p = [ucyl(4.0, 4.2, 1.25, 2.6, bands=(.2, .8)), lab(cx, cy - 40, 'air', '#0E2238', 18)]
    top = cy - 2.6 * U
    p += [f'<rect x="{cx - 4:.1f}" y="{top - 44:.1f}" width="8" height="44" fill="#8E9AA6"/>', gauge(cx, top - 66, 26, .3, ACC),
          thermo(cx + 46, top + 2, 62, .55, AC2)]
    p += [lab(cx, top - 100, f'{p0} kPa', ACC, 15), lab(cx + 74, top - 40, f'{T0} K', AC2, 15)]
    rows = [[('(∂p/∂v)<sub>T</sub> = −RT/v²', ''), (f'{sg(float(r1(dpdv)), ".1f")}', f'color:{AC2}')],
            [('(∂v/∂T)<sub>p</sub> = R/p', ''), (f'{dvdT:.5f}', f'color:{AC2}')],
            [('(∂T/∂p)<sub>v</sub> = v/R', ''), (f'{dTdp:.3f}', f'color:{AC2}')],
            [('product', f'color:{ACC}'), (f'{sg(prod, ".3f")}', f'color:{ACC};font-weight:700')]]
    card = table(['slope at 300 K, 100 kPa', 'value'], rows)
    return make('me-thermo-u4-L2', 'Exact<br>Differentials,<br>Gibbs &amp; Helmholtz',
                'The three slopes multiply<br>to <span class="gold">−1</span>, never <span class="cyan">+1</span>',
                'the cyclic relation', card, p,
                [chip('left', 300, 'c', f'v = {v:.3f} m³/kg'), chip('left', 470, 'c', 'pv = RT'),
                 chip('right', 330, 'g', f'product = {sg(prod, ".3f")}'), chip('right', 500, 'c', f'{dpdT:.4f} × {dTdp:.3f} = 1', False)],
                f'(−RT/v²)(R/p)(v/R) = −RT/(pv) = <b class="gl">−1</b><br>'
                f'({sg(float(r1(dpdv)), ".1f")}) × {dvdT:.5f} × {dTdp:.3f} = <b class="cl">{sg(prod, ".3f")}</b>', css='.scope td{padding:5px 6px}')


def u4L3():
    """4.7 worked example 2: nitrogen at 300 K throttled from 20 bar to 1 bar (van der Waals estimate)"""
    a, b, cpm, R, T0, p1, p2 = .137, 3.87e-5, 29.1, 8.314, 300, 20, 1
    mu = lambda T_: (2 * a / (R * T_) - b) / cpm * 1e5       # K/bar
    dT = mu(T0) * (p2 - p1)                                  # −4.6 K
    Ti = 2 * a / (R * b)                                     # 852 K
    assert (f'{mu(T0):.4f}', r1(dT), r1(T0 + dT), f'{Ti:.0f}') == ('0.2445', '-4.6', '295.4', '852')
    # board: a line with a throttling valve, gauges and thermometers either side
    p = [tube('y', .5, 7.6, 4.2, 1.0, .45, 'url(#tv)', 'url(#dm)')]
    p += [box(3.7, 3.6, 1.0, .9, 1.3, '#8E9AA6', '#4A5560', '#5E6A76', z0=.4)]
    vx, vy = P(4.2, 4.05, 1.7)
    p += [f'<rect x="{vx - 3:.1f}" y="{vy - 26:.1f}" width="6" height="26" fill="#3A444E"/><ellipse cx="{vx:.1f}" cy="{vy - 28:.1f}" rx="22" ry="12" fill="none" stroke="#E04848" stroke-width="5"/>']
    for yy, txt, col, T_ in ((1.6, f'{p1} bar', ACC, f'{T0} K'), (6.4, f'{p2} bar', AC2, f'{r1(T0 + dT)} K')):
        gx, gy = P(4.2, yy, 1.45)
        p += [f'<rect x="{gx - 3:.1f}" y="{gy - 34:.1f}" width="6" height="34" fill="#8E9AA6"/>', gauge(gx, gy - 50, 18, .8 if col == ACC else .1, col),
              lab(gx, gy - 76, txt, col, 15), thermo(gx + 34, gy + 6, 52, .5, col), lab(gx + 34, gy + 34, T_, col, 14)]
    p += [garrow(*P(4.2, .0, 1.9), *P(4.2, 1.0, 1.9), ACC, 5)]
    # card: μJT against temperature; positive (cooling) below the inversion temperature
    X = lambda T_: 50 + (T_ - 200) / 900 * 390
    Y = lambda u: 70 - u / .5 * 56
    curve = [(X(200 + 900 * i / 60), Y(mu(200 + 900 * i / 60))) for i in range(61)]
    s = axes(50, 440, 124, 12) + f'<line x1="50" y1="{Y(0):.1f}" x2="440" y2="{Y(0):.1f}" stroke="{AXC}" stroke-width="1.2" stroke-dasharray="4 4"/>'
    s += poly(curve, ACC, 3.5) + dot(X(T0), Y(mu(T0)), ACC) + dot(X(Ti), Y(0), AC2)
    s += t_(X(T0) + 10, Y(mu(T0)) - 4, f'{mu(T0):.4f} K/bar at {T0} K', 'pt', 'start', ACC)
    s += t_(X(Ti), Y(0) - 10, f'T<tspan font-size="11" dy="3">i</tspan><tspan dy="-3"> = {Ti:.0f} K</tspan>', 'pt', 'middle', AC2)
    s += t_(150, 112, 'cools', 'ax', 'middle', ACC) + t_(410, 112, 'warms', 'ax', 'middle', AC2) + t_(44, 20, 'μ', 'ax', 'end')
    s += t_(X(200), 140, '200', 'ax') + t_(X(1100), 140, '1100 K', 'ax', 'end')
    card = svgcard(s)
    return make('me-thermo-u4-L3', 'Maxwell,<br>Clapeyron &amp;<br>Joule-Thomson',
                'Throttling cools only <span class="gold">BELOW</span><br>the <span class="cyan">inversion</span> temperature',
                'nitrogen through a valve', card, p,
                [chip('left', 262, 'g', f'{p1} bar → {p2} bar'), chip('left', 470, 'g', f'μ<sub>JT</sub> ≈ {mu(T0):.3f} K/bar'),
                 chip('right', 262, 'c', f'ΔT ≈ {sg(float(r1(dT)), ".1f")} K'), chip('right', 500, 'c', f'T<sub>i</sub> ≈ {Ti:.0f} K', False)],
                f'μ<sub>JT</sub> = (2a/RT − b)/c<sub>p,m</sub> = <b class="gl">{mu(T0):.4f} K/bar</b><br>'
                f'ΔT ≈ {mu(T0):.4f} × ({p2} − {p1}) = <b class="cl">{sg(float(r1(dT)), ".1f")} K</b>; T<sub>i</sub> = {Ti:.0f} K')


# ================================================================ unit 5
def u5L1():
    """5.2 worked example: ice heated at 0.4 kPa and at 101.325 kPa; water heated at 25 MPa"""
    tp_T, tp_p, cp_T, cp_p = .01, .6117, 373.95, 22064
    pa, pb, pc = .4, 101.325, 25000
    assert pa < tp_p < pb and pc > cp_p
    # board: ice in a cylinder under a piston, heat coming in
    cx, cy = P(4.2, 4.2)
    p = [piston_cyl(4.2, 4.2, 1.35, 3.4, 2.3, '#CFE9FF', rod=.6)]
    p += [box(3.7, 3.7, 1.0, 1.0, 1.0, '#F4FBFF', '#A9CDE6', '#C9E3F4', z0=.05), lab(cx, cy - 2.3 * U - 30, 'p fixed', '#1A222B', 13)]
    p += [wave(cx - 150, cy - 50, ACC, 2, 30)]
    # card: the p–T phase diagram of water (log p) with the three heating paths
    L = math.log10
    X = lambda t: 40 + (t + 30) / 60 * 170 if t <= 30 else 210 + (t - 30) / 430 * 230   # the axis is stretched below 30 °C
    Y = lambda pk: 124 - (L(pk) + .7) / 5.5 * 112
    vap = [(.01, .6117), (20, 2.339), (100, 101.325), (373.95, 22064)]
    def vp(t):                                               # ln p linear in 1/T between the book's points
        for (t0, p0_), (t1, p1_) in zip(vap, vap[1:]):
            if t <= t1:
                f = (1 / (t + 273.15) - 1 / (t0 + 273.15)) / (1 / (t1 + 273.15) - 1 / (t0 + 273.15))
                return math.exp(math.log(p0_) + f * (math.log(p1_) - math.log(p0_)))
    sub = lambda t: math.exp(math.log(.402) + (1 / (t + 273.15) - 1 / 268.15) / (1 / 273.16 - 1 / 268.15) * (math.log(.6117) - math.log(.402)))
    s = axes(40, 440, 124, 10)
    s += poly([(X(t), Y(sub(t))) for t in [-30 + 30.01 * i / 20 for i in range(21)]], '#C9D3DB', 2.5)
    s += poly([(X(.01 + (373.95 - .01) * i / 80), Y(vp(.01 + (373.95 - .01) * i / 80))) for i in range(81)], '#C9D3DB', 2.5)
    s += poly([(X(.01), Y(tp_p)), (X(-1.5), Y(1e5))], '#C9D3DB', 2.5)
    for pp, t0, t1, col in ((pa, -20, 20, AC2), (pb, -20, 20, ACC), (pc, 300, 450, '#FFC79E')):
        s += f'<line x1="{X(t0):.1f}" y1="{Y(pp):.1f}" x2="{X(t1):.1f}" y2="{Y(pp):.1f}" stroke="{col}" stroke-width="3" marker-end="url(#{"ab" if col == AC2 else "ao"})"/>'
    s += f'<defs><marker id="ab" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{AC2}"/></marker><marker id="ao" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{ACC}"/></marker></defs>'
    s += dot(X(tp_T), Y(tp_p), AC2, 5) + dot(X(cp_T), Y(cp_p), ACC, 5)
    s += t_(X(tp_T) - 6, Y(tp_p) - 8, f'triple {tp_p} kPa', 'ax', 'end', AC2) + t_(X(cp_T) + 4, Y(cp_p) + 18, f'critical {cp_p / 1000:g} MPa', 'ax', 'middle', ACC)
    s += t_(X(20) + 10, Y(pa) + 12, f'{pa} kPa', 'ax', 'start', AC2) + t_(X(20) + 10, Y(pb) + 5, '1 atm', 'ax', 'start', ACC) + t_(X(300) - 6, Y(pc) + 5, '25 MPa', 'ax', 'end', '#FFC79E')
    s += f'<path d="M206,119 l4,10 M211,119 l4,10" stroke="{AXC}" stroke-width="1.5"/>'
    s += t_(X(-30), 140, '−30', 'ax', 'start') + t_(X(0), 140, '0', 'ax') + t_(X(460), 140, '460 °C', 'ax', 'end') + t_(34, 18, 'p', 'ax', 'end')
    card = svgcard(s)
    return make('me-thermo-u5-L1', 'Phase Change,<br>Triple &amp; Critical<br>Points',
                'The triple point is <span class="gold">0.6117 kPa</span>,<br>far <span class="cyan">BELOW</span> 1 atm',
                'ice heated at three p', card, p,
                [chip('left', 262, 'c', f'{pa} kPa: sublimes at −5 °C'), chip('left', 470, 'g', '1 atm: melts at 0 °C'),
                 chip('right', 330, 'c', f'triple {tp_p} kPa'), chip('right', 500, 'g', '25 MPa: never boils', False)],
                f'{pa} &lt; {tp_p} kPa: ice <b class="cl">sublimes</b>, no liquid ever<br>'
                f'{pb} kPa: <b class="gl">melts</b> at 0 °C · {pc / 1000:g} MPa &gt; p<sub>c</sub>: no boiling')


def u5L2():
    """5.3 worked example: the phase rule F = C − P + 2 for five cases"""
    cases = [('(a) superheated steam', 1, 1), ('(b) wet steam, 10 bar', 1, 2), ('(c) triple-point cell', 1, 3), ('(d) moist air over water', 2, 2), ('(e) four phases', 1, 4)]
    F = {n: c - ph + 2 for n, c, ph in cases}
    assert list(F.values()) == [2, 1, 0, 2, -1]
    # board: a boiler drum, water below and steam above, with a gauge glass, pressure gauge and thermometer
    p = [box(2.6, 3.2, .5, 2.6, .8, '#5E6A76', '#2C3640', '#3A4652'), box(5.6, 3.2, .5, 2.6, .8, '#5E6A76', '#2C3640', '#3A4652'),
         tube('x', 2.0, 6.8, 4.5, 2.0, 1.25, 'url(#tv)', 'url(#dm)')]
    ex, ey = P(6.8, 4.5, 2.0)
    p += [f'<path d="M{ex - 28:.1f},{ey + 6:.1f} A28,40 0 0 0 {ex + 28:.1f},{ey + 6:.1f} Z" fill="{WATER}" fill-opacity=".8"/>',
          f'<path d="M{ex - 28:.1f},{ey + 6:.1f} A28,40 0 0 1 {ex + 28:.1f},{ey + 6:.1f} Z" fill="#F1F4F7" fill-opacity=".55"/>',
          lab(ex, ey - 6, 'steam', '#3A444E', 13), lab(ex, ey + 26, 'water', '#0E2238', 13)]
    gx, gy = P(4.4, 4.5, 3.25)
    p += [f'<rect x="{gx - 4:.1f}" y="{gy - 40:.1f}" width="8" height="40" fill="#8E9AA6"/>', gauge(gx, gy - 58, 22, .45, ACC), lab(gx, gy - 88, '10 bar', ACC, 15),
          thermo(*P(2.6, 4.5, 3.25), 56, .7, ACC), lab(P(2.6, 4.5, 5.35)[0] - 34, P(2.6, 4.5, 5.35)[1] + 10, '179.9 °C', ACC, 14)]
    rows = []
    for n, c, ph in cases:
        f = F[n]
        st = f'color:{ACC};font-weight:700' if n.startswith('(b)') else ''
        rows.append([(n, st), (f'{c}', ''), (f'{ph}', ''), (f'{sg(f) if f < 0 else f}', st or f'color:{AC2}')])
    card = table(['', 'C', 'P', 'F = C − P + 2'], rows)
    return make('me-thermo-u5-L2', 'Gibbs Phase<br>Rule &amp; Steam<br>Formation',
                'Wet steam has <span class="gold">ONE</span> free choice:<br>pick p, and <span class="cyan">T follows</span>',
                'counting free choices', card, p,
                [chip('left', 300, 'g', 'wet steam: F = 1'), chip('left', 470, 'c', 'dryness x still free'),
                 chip('right', 330, 'g', '10 bar → 179.9 °C'), chip('right', 500, 'c', 'triple cell: F = 0', False)],
                f'(b) C = 1, P = 2: F = 1 − 2 + 2 = <b class="gl">1</b> → T<sub>sat</sub> = 179.9 °C<br>'
                f'(c) F = <b class="cl">0</b> · (e) F = −1: four phases impossible',
                css='.scope td{padding:3px 6px;font-size:16px}.scope td:first-child{font-size:15px}.scope th{padding:2px 6px}')


def u5L3():
    """5.5 worked example: steam at 10 bar, 280 °C, by interpolation in the superheated table"""
    Tsat, T, Ta, Tb = 179.9, 280, 250, 300
    ha, hb, va, vb, sa, sb = 2943.1, 3051.6, .2327, .2580, 6.9265, 7.1246
    f = (T - Ta) / (Tb - Ta)
    h, v, s_ = ha + f * (hb - ha), va + f * (vb - va), sa + f * (sb - sa)
    assert (f, r1(h), f'{v:.4f}', f'{s_:.4f}', r1(T - Tsat)) == (.6, '3008.2', '0.2479', '7.0454', '100.1')
    # board: a lagged steam main with a gauge and a thermometer pocket, the open superheated table beside it
    p = [tube('y', .4, 7.6, 3.0, 1.0, .55, 'url(#tv)', 'url(#dm)')]
    for yy in (2.0, 3.4, 4.8, 6.2):
        p.append(f'<polyline points="{pts(*ring(3.0, yy, 1.0, .56, "y")[10:31])}" fill="none" stroke="#5E6A76" stroke-width="2.5"/>')
    gx, gy = P(3.0, 2.6, 1.55)
    p += [f'<rect x="{gx - 3:.1f}" y="{gy - 34:.1f}" width="6" height="34" fill="#8E9AA6"/>', gauge(gx, gy - 52, 20, .45, ACC), lab(gx, gy - 80, '10 bar', ACC, 15)]
    tx, ty = P(3.0, 5.2, 1.55)
    p += [thermo(tx, ty, 62, .75, ACC), lab(tx, ty - 72, f'{T} °C', ACC, 15)]
    p += [box(4.6, 3.4, 2.8, 2.6, .12, '#F1F4F7', '#9FB0BF', '#C9D3DB')]
    for k in range(5):
        p.append(f'<polyline points="{pts(P(4.9, 3.75 + k * .45, .13), P(7.1, 3.75 + k * .45, .13))}" stroke="#8E9AA6" stroke-width="2"/>')
    p.append(f'<polyline points="{pts(P(4.9, 3.75 + 2 * .45, .13), P(7.1, 3.75 + 2 * .45, .13))}" stroke="{ACC}" stroke-width="4"/>')
    # card: linear interpolation between the 250 °C and 300 °C rows
    X = lambda t: 70 + (t - 240) / 70 * 340
    Y = lambda hh: 120 - (hh - 2920) / 150 * 100
    s = axes(70, 440, 120, 14) + poly([(X(Ta), Y(ha)), (X(Tb), Y(hb))], AC2, 3)
    s += dot(X(Ta), Y(ha), AC2) + dot(X(Tb), Y(hb), AC2) + dot(X(T), Y(h), ACC, 6)
    s += f'<path d="M{X(T):.1f},120 V{Y(h):.1f} H70" fill="none" stroke="{ACC}" stroke-width="2" stroke-dasharray="5 4"/>'
    s += t_(X(Ta) + 8, Y(ha) + 16, f'{ha}', 'ax', 'start', AC2) + t_(X(Tb) - 8, Y(hb) - 4, f'{hb}', 'ax', 'end', AC2)
    s += t_(X(T) - 10, Y(h) - 10, f'h = {r1(h)}', 'pt', 'end', ACC)
    s += t_(X(Ta), 138, f'{Ta}', 'ax') + t_(X(T), 138, f'{T}', 'ax', 'middle', ACC) + t_(X(Tb), 138, f'{Tb} °C', 'ax') + t_(64, 22, 'h', 'ax', 'end')
    card = svgcard(s)
    return make('me-thermo-u5-L3', 'Steam Tables<br>&amp; Calorimeters',
                'Above T<sub>sat</sub>: use the <span class="gold">SUPERHEATED</span><br>table and <span class="cyan">interpolate</span>',
                'steam at 10 bar, 280 °C', card, p,
                [chip('left', 262, 'c', f'T<sub>sat</sub> = {Tsat} °C'), chip('left', 470, 'g', f'{r1(T - Tsat)} K of superheat'),
                 chip('right', 262, 'g', f'h ≈ {r1(h)} kJ/kg'), chip('right', 500, 'c', f'v ≈ {v:.4f} m³/kg', False)],
                f'{T} °C &gt; {Tsat} °C → <b class="gl">superheated</b>; f = 30/50 = {f:g}<br>'
                f'h = {ha} + {f:g} × {hb - ha:.1f} = <b class="cl">{r1(h)} kJ/kg</b>')


def u5L4():
    """5.8 worked example: a 60 L CNG cylinder filled with methane to 20 MPa at 300 K"""
    V, p_, T_, Tc, pc, R, Z = .060, 20, 300, 190.6, 4.60, .5183, .83
    TR, pR = T_ / Tc, p_ / pc
    v_id = R * T_ / (p_ * 1000); m_id = V / v_id
    v_re = Z * v_id; m_re = V / v_re
    assert (f'{TR:.3f}', f'{pR:.2f}', f'{v_id:.6f}', f'{m_id:.2f}', f'{v_re:.6f}', f'{m_re:.2f}') == ('1.574', '4.35', '0.007775', '7.72', '0.006453', '9.30')
    cx, cy = P(4.0, 4.4)
    p = [ucyl(4.0, 4.4, .95, 4.6, body='url(#cng)', top='#3E8E5A')]
    top = cy - 4.6 * U
    p += [f'<path d="M{cx - 35:.1f},{top:.1f} Q{cx:.1f},{top - 46:.1f} {cx + 35:.1f},{top:.1f}" fill="url(#cng)"/>',
          f'<rect x="{cx - 9:.1f}" y="{top - 52:.1f}" width="18" height="22" fill="#B7C2CC"/><rect x="{cx - 22:.1f}" y="{top - 60:.1f}" width="44" height="10" rx="4" fill="#E04848"/>',
          lab(cx, cy - 70, 'CH₄', '#0B2A16', 20), lab(cx, cy - 48, f'{V * 1000:g} L', '#0B2A16', 15)]
    gx, gy = P(5.6, 3.2)
    p += [box(5.4, 3.0, .4, .4, 2.6, '#8E9AA6', '#4A5560', '#5E6A76'), gauge(gx, gy - 2.6 * U - 24, 26, .85, ACC),
          lab(gx, gy - 2.6 * U + 18, f'{p_} MPa', ACC, 15), f'<path d="M{cx + 9:.1f},{top - 42:.1f} H{gx:.1f} V{gy - 2.6 * U - 50:.1f}" fill="none" stroke="#C9D3DB" stroke-width="4"/>']
    s = hbars([('ideal gas', m_id, AC2, f'{m_id:.2f} kg'), (f'Z = {Z}', m_re, ACC, f'{m_re:.2f} kg')], 0, 450, 22, 30, 16, m_re * 1.25, 110)
    s += t_(235, 130, f'T<tspan font-size="11" dy="3">R</tspan><tspan dy="-3"> = {TR:.3f},  p</tspan><tspan font-size="11" dy="3">R</tspan><tspan dy="-3"> = {p_}/{pc} = {pR:.2f} (absolute)</tspan>', 'ax', 'middle', INK)
    card = svgcard(s)
    return make('me-thermo-u5-L4', 'Ideal &amp;<br>Real Gases',
                'Use <span class="gold">ABSOLUTE</span> pressure for p<sub>R</sub>;<br>Z adds <span class="cyan">1.58 kg</span> here',
                'filling a CNG cylinder', card, p,
                [chip('left', 300, 'c', f'T<sub>R</sub> = {TR:.3f}'), chip('left', 470, 'c', f'p<sub>R</sub> = {pR:.2f}'),
                 chip('right', 300, 'g', f'Z ≈ {Z}'), chip('right', 500, 'g', f'{m_re:.2f} kg, not {m_id:.2f}', False)],
                f'ideal: m = {V:.3f} ÷ {v_id:.6f} = <b class="cl">{m_id:.2f} kg</b><br>'
                f'Z = {Z}: v = {v_re:.6f} m³/kg → m = <b class="gl">{m_re:.2f} kg</b>')


def u5L5():
    """5.10 worked example: moist air at 30 °C dry bulb, 60 % RH, 101.325 kPa"""
    phi, ps30, p_, t = .60, 4.247, 101.325, 30
    pv = phi * ps30; pa = p_ - pv
    w = .622 * pv / pa
    tdp = 21 + (pv - 2.488) / (2.645 - 2.488)
    assert (f'{pv:.3f}', f'{pa:.3f}', f'{w:.5f}', r1(tdp)) == ('2.548', '98.777', '0.01605', '21.4')
    # board: a duct of moist air with a dry-bulb thermometer and a humidity gauge
    p = [box(1.2, 3.2, 5.6, 1.9, 1.7, '#6FA6C8', '#2C5370', '#3B6B8C')]
    top = [P(1.2, 3.2, 1.7), P(6.8, 3.2, 1.7), P(6.8, 5.1, 1.7), P(1.2, 5.1, 1.7)]
    p += [f'<polygon points="{pts(P(6.8, 3.2, 1.7), P(6.8, 5.1, 1.7), P(6.8, 5.1, 0), P(6.8, 3.2, 0))}" fill="#0E2238"/>']
    p += [f'<polygon points="{pts(P(6.8, 3.4, 1.5), P(6.8, 4.9, 1.5), P(6.8, 4.9, .2), P(6.8, 3.4, .2))}" fill="#16364F"/>']
    import random
    rnd = random.Random(7)
    for k in range(26):
        x, y = P(6.8, 3.45 + rnd.random() * 1.4, .25 + rnd.random() * 1.2)
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{2.5 + rnd.random() * 2:.1f}" fill="#CFE9FF" opacity=".85"/>')
    p += [garrow(*P(7.0, 4.15, .85), *P(8.6, 4.15, .85), AC2, 6)]
    tx, ty = P(2.6, 4.15, 1.7)
    p += [thermo(tx, ty, 66, .62, ACC), lab(tx, ty - 76, f'{t} °C', ACC, 15)]
    gx, gy = P(4.8, 4.15, 1.7)
    p += [f'<rect x="{gx - 3:.1f}" y="{gy - 34:.1f}" width="6" height="34" fill="#8E9AA6"/>', gauge(gx, gy - 52, 20, phi, AC2), lab(gx, gy - 80, f'{phi * 100:g} %', AC2, 15)]
    # card: the total pressure split into dry air and vapour
    x0, k = 20, 430 / p_
    s = f'<rect x="{x0}" y="30" width="{pa * k:.1f}" height="34" rx="4" fill="{ACC}" fill-opacity=".85"/>'
    s += f'<rect x="{x0 + pa * k:.1f}" y="30" width="{max(pv * k, 6):.1f}" height="34" rx="2" fill="{AC2}"/>'
    s += t_(x0 + pa * k / 2, 53, f'dry air p<tspan font-size="11" dy="3">a</tspan><tspan dy="-3"> = {pa:.3f} kPa</tspan>', 'pt', 'middle', '#2A1406')
    s += t_(x0 + pa * k, 20, f'vapour p<tspan font-size="11" dy="3">v</tspan><tspan dy="-3"> = {pv:.3f}</tspan>', 'ax', 'end', AC2)
    s += t_(235, 92, f'total p = {p_} kPa', 'ax', 'middle', INK)
    s += t_(235, 124, f'w = 0.622 p<tspan font-size="11" dy="3">v</tspan><tspan dy="-3"> / p</tspan><tspan font-size="11" dy="3">a</tspan><tspan dy="-3"> = {w:.5f} kg per kg dry air</tspan>', 'pt', 'middle', ACC)
    card = svgcard(s)
    return make('me-thermo-u5-L5', 'Gas Mixtures<br>&amp; Moist Air',
                'w is per kg of <span class="gold">DRY AIR</span>,<br>so divide by <span class="cyan">p<sub>a</sub></span>, not p',
                'moist air, 30 °C, 60 %', card, p,
                [chip('left', 262, 'c', f'p<sub>v</sub> = {pv:.3f} kPa'), chip('left', 470, 'g', f'p<sub>a</sub> = {pa:.3f} kPa'),
                 chip('right', 262, 'g', f'w = {w:.5f} kg/kg'), chip('right', 500, 'c', f'dew point {r1(tdp)} °C', False)],
                f'p<sub>v</sub> = {phi} × {ps30} = {pv:.3f}; p<sub>a</sub> = <b class="cl">{pa:.3f} kPa</b><br>'
                f'w = 0.622 × {pv:.3f} ÷ {pa:.3f} = <b class="gl">{w:.5f} kg/kg</b>')



# ================================================================ unit 6
def otto_pv(v1, r, p1, p2, p3, p4, g_=1.4, n=40):
    v2 = v1 / r
    comp = [(v1 - (v1 - v2) * i / n, p1 * (v1 / (v1 - (v1 - v2) * i / n)) ** g_) for i in range(n + 1)]
    exp_ = [(v2 + (v1 - v2) * i / n, p3 * (v2 / (v2 + (v1 - v2) * i / n)) ** g_) for i in range(n + 1)]
    return comp, exp_


def u6L1():
    """6.2 worked example 2: Diesel cycle, r = 15, cut-off at 6 % of the stroke, 1 bar and 300 K"""
    r, cut, p1, T1, cp, cv, g_, R = 15, .06, 1, 300, 1.005, .718, 1.4, .287
    rc = 1 + cut * (r - 1)                                   # 1.84
    T2 = T1 * r ** (g_ - 1); p2 = p1 * r ** g_               # 886.3 K, 44.31 bar
    T3 = rc * T2; T4 = T1 * rc ** g_                         # 1630.7 K, 704.5 K
    qin = cp * (T3 - T2); qout = cv * (T4 - T1)              # 748.2, 290.4 kJ/kg
    eta = (qin - qout) / qin
    assert (f'{rc:.2f}', r1(T2), f'{p2:.2f}', r1(T3), r1(T4), r1(qin), r1(qout), f'{eta:.3f}') == ('1.84', '886.3', '44.31', '1630.7', '704.5', '748.2', '290.4', '0.612')
    # board: one cylinder, piston, connecting rod and crank, the injector on the head
    cx, cy = P(4.4, 3.8)
    p = [box(3.0, 2.5, 2.8, 2.6, 1.3, '#5E6A76', '#2C3640', '#3A4652')]
    p += [vessel(4.4, 3.8, 1.0, 2.6, '#FFC79E', .25, z0=1.3, shadow=False)]
    pz = cy - 1.3 * U - 1.1 * U
    p += [T.cyl(cx, pz, 37, 21, 18, 'url(#tk)', 'url(#dm)')]
    kx, ky = P(4.4, 5.1, .65)
    p += [f'<line x1="{cx:.1f}" y1="{pz:.1f}" x2="{kx + 14:.1f}" y2="{ky - 10:.1f}" stroke="#B7C2CC" stroke-width="9" stroke-linecap="round"/>',
          f'<circle cx="{kx:.1f}" cy="{ky:.1f}" r="26" fill="#8E9AA6" stroke="#3A444E" stroke-width="3"/><circle cx="{kx + 14:.1f}" cy="{ky - 10:.1f}" r="6" fill="#3A444E"/>']
    hz = cy - 3.9 * U
    p += [f'<ellipse cx="{cx:.1f}" cy="{hz:.1f}" rx="{1.0 * U * 1.2247:.1f}" ry="{1.0 * U * .7071:.1f}" fill="#8E9AA6"/>',
          f'<rect x="{cx - 6:.1f}" y="{hz - 44:.1f}" width="12" height="40" rx="3" fill="#C9D3DB"/>',
          f'<path d="M{cx:.1f},{hz + 6:.1f} l-22,40 h44 z" fill="{ACC}" opacity=".55" style="filter:drop-shadow(0 0 6px {ACC})"/>']
    # card: p–v diagram; heat in along constant p, out along constant v
    v1 = R * T1 / (p1 * 100); v2 = v1 / r; v3 = rc * v2
    comp = [(v1 - (v1 - v2) * i / 40, p1 * (v1 / (v1 - (v1 - v2) * i / 40)) ** g_) for i in range(41)]
    exp_ = [(v3 + (v1 - v3) * i / 40, p2 * (v3 / (v3 + (v1 - v3) * i / 40)) ** g_) for i in range(41)]
    p4 = exp_[-1][1]
    L = math.log10
    X = lambda v: 60 + v / v1 * 280
    Y = lambda pp: 124 - (L(pp) - L(.8)) / (L(60) - L(.8)) * 108
    s = axes(60, 350, 124, 12)
    s += poly([(X(a), Y(b)) for a, b in comp], '#9FB0BF', 2.5) + poly([(X(a), Y(b)) for a, b in exp_], '#9FB0BF', 2.5)
    s += poly([(X(v2), Y(p2)), (X(v3), Y(p2))], ACC, 5) + poly([(X(v1), Y(p4)), (X(v1), Y(p1))], AC2, 5)
    s += dot(X(v2), Y(p2), ACC, 4) + dot(X(v3), Y(p2), ACC, 4) + dot(X(v1), Y(p4), AC2, 4) + dot(X(v1), Y(p1), AC2, 4)
    s += t_(X(v3) + 12, Y(p2) + 6, f'q<tspan font-size="11" dy="3">in</tspan><tspan dy="-3"> = c</tspan><tspan font-size="11" dy="3">p</tspan><tspan dy="-3">ΔT, constant p</tspan>', 'pt', 'start', ACC)
    s += t_(X(v1) + 12, Y(p4) + 2, f'q<tspan font-size="11" dy="3">out</tspan><tspan dy="-3"> = c</tspan><tspan font-size="11" dy="3">v</tspan><tspan dy="-3">ΔT,</tspan>', 'pt', 'start', AC2)
    s += t_(X(v1) + 12, Y(p4) + 22, 'constant v', 'pt', 'start', AC2)
    s += t_(54, Y(p2) + 5, f'{p2:.2f}', 'ax', 'end') + t_(54, Y(p1) + 5, f'{p1}', 'ax', 'end') + t_(54, 140, 'bar, log', 'ax', 'end')
    s += t_(X(v2), 140, f'{v2:.4f}', 'ax', 'start') + t_(X(v1), 140, f'{v1:.3f} m³/kg', 'ax', 'middle')
    card = svgcard(s)
    return make('me-thermo-u6-L1', 'Carnot, Otto,<br>Diesel &amp; Dual<br>Cycles',
                'Heat in at constant <span class="gold">p</span>: c<sub>p</sub>;<br>heat out at constant <span class="cyan">v</span>: c<sub>v</sub>',
                f'Diesel cycle, r = {r}', card, p,
                [chip('left', 262, 'c', f'r<sub>c</sub> = {rc:.2f}'), chip('left', 470, 'c', f'q<sub>out</sub> = {r1(qout)} kJ/kg'),
                 chip('right', 262, 'g', f'q<sub>in</sub> = {r1(qin)} kJ/kg'), chip('right', 500, 'g', f'η = {eta * 100:.1f} %', False)],
                f'q<sub>in</sub> = {cp} × ({r1(T3)} − {r1(T2)}) = <b class="gl">{r1(qin)} kJ/kg</b><br>'
                f'q<sub>out</sub> = {cv} × ({r1(T4)} − {T1}) = <b class="cl">{r1(qout)} kJ/kg</b>')


def u6L2():
    """6.4 worked example 2: a four-cylinder four-stroke petrol engine on the Otto cycle (r = 8, w = 451.8 kJ/kg)"""
    v1, v2, wnet = .861, .1076, 451.8
    pm = wnet / (v1 - v2)                                    # 599.7 kPa
    bore, stroke, rpm, ncyl = .08, .09, 3000, 4
    Vs = math.pi / 4 * bore ** 2 * stroke                    # 4.524e-4 m³
    cyc = rpm / 120
    P_ = pm * Vs * cyc * ncyl                                # 27.1 kW
    assert (r1(pm), f'{Vs * 1e4:.3f}', cyc, r1(P_)) == ('599.7', '4.524', 25, '27.1')
    # board: an in-line four: the block, four bores with their pistons, the crank pulley
    p = [box(1.6, 3.0, 4.8, 1.9, 2.2, '#8E9AA6', '#3F4A55', '#5E6A76'),
         box(1.6, 3.0, 4.8, 1.9, .5, '#5E6A76', '#2C3640', '#3A4652', z0=-.0)]
    for k, h in enumerate((.05, .35, .35, .05)):
        bx_, by_ = P(2.2 + k * 1.2, 3.95, 2.2)
        p.append(f'<ellipse cx="{bx_:.1f}" cy="{by_:.1f}" rx="{.48 * U * 1.2247:.1f}" ry="{.48 * U * .7071:.1f}" fill="#1A222B"/>')
        p.append(f'<ellipse cx="{bx_:.1f}" cy="{by_ + 4 + h * 24:.1f}" rx="{.40 * U * 1.2247:.1f}" ry="{.40 * U * .7071:.1f}" fill="url(#dm)"/>')
    p += [tube('x', 6.4, 7.0, 3.95, 1.1, .7, 'url(#tv)', '#3A444E')]
    px_, py_ = P(7.0, 3.95, 1.1)
    p += [f'<circle cx="{px_:.1f}" cy="{py_:.1f}" r="8" fill="#B7C2CC"/>',
          f'<path d="M{px_ - 34:.1f},{py_ + 6:.1f} A30,34 0 1 1 {px_ + 8:.1f},{py_ + 36:.1f}" fill="none" stroke="{ACC}" stroke-width="4" marker-end="url(#ao)"/>']
    # card: the cylinder volume split into clearance and swept; MEP divides by the swept part only
    vs = v1 - v2
    x0, k = 20, 430 / v1
    s = f'<rect x="{x0}" y="30" width="{v2 * k:.1f}" height="34" rx="4" fill="{AC2}" fill-opacity=".85"/>'
    s += f'<rect x="{x0 + v2 * k:.1f}" y="30" width="{vs * k:.1f}" height="34" rx="4" fill="{ACC}" fill-opacity=".85"/>'
    s += t_(x0 + v2 * k / 2, 52, f'{v2}', 'ax', 'middle', '#0E2238') + t_(x0 + v2 * k / 2, 20, 'clearance', 'ax', 'middle', AC2)
    s += t_(x0 + v2 * k + vs * k / 2, 53, f'swept {vs:.4f} m³/kg', 'pt', 'middle', '#2A1406')
    s += f'<path d="M{x0},76 H{x0 + 430} M{x0},71 V81 M{x0 + 430},71 V81" stroke="{INK}" stroke-width="1.5"/>' + t_(235, 94, f'total {v1} m³/kg', 'ax', 'middle', INK)
    s += t_(235, 126, f'MEP = w<tspan font-size="11" dy="3">net</tspan><tspan dy="-3"> ÷ swept = {wnet} ÷ {vs:.4f} = {r1(pm)} kPa</tspan>', 'pt', 'middle', ACC)
    card = svgcard(s)
    return make('me-thermo-u6-L2', 'Brayton, Stirling<br>&amp; Mean Effective<br>Pressure',
                'MEP = w<sub>net</sub> ÷ <span class="gold">SWEPT</span> volume,<br>not the <span class="cyan">total</span> volume',
                'petrol four at 3000 rpm', card, p,
                [chip('left', 262, 'c', f'bore {bore * 1000:g}, stroke {stroke * 1000:g} mm'), chip('left', 470, 'c', f'V<sub>s</sub> = {Vs * 1e6:.1f} cm³'),
                 chip('right', 262, 'g', f'MEP ≈ {pm / 100:.1f} bar'), chip('right', 500, 'g', f'{r1(P_)} kW', False)],
                f'p<sub>m</sub> = {wnet} ÷ ({v1} − {v2}) = <b class="gl">{r1(pm)} kPa</b><br>'
                f'power = {r1(pm)} × {Vs * 1e4:.3f}×10⁻⁴ × {cyc:g} × {ncyl} = <b class="cl">{r1(P_)} kW</b>')


def u6L3():
    """6.6 worked example: reheat Rankine cycle, 60 bar 500 °C, reheat at 10 bar to 500 °C, condenser 0.1 bar"""
    h1, h2, h3, hf, hfg, sf, sfg, s1, s3, wp, h6 = 3423.1, 2920.4, 3479.1, 191.81, 2392.1, .6492, 7.4996, 6.8826, 7.7641, 6.05, 197.86
    x4 = (s3 - sf) / sfg; h4 = round(hf + x4 * hfg, 1)          # the book carries h to 0.1 kJ/kg
    wT = (h1 - h2) + (h3 - h4); wnet = wT - wp
    qin = (h1 - h6) + (h3 - h2); eta = wnet / qin
    xs = (s1 - sf) / sfg; hs = round(hf + xs * hfg, 1)
    wnet_s = (h1 - hs) - wp; qin_s = h1 - h6; eta_s = wnet_s / qin_s
    assert (f'{x4:.4f}', r1(h4), r1(wnet), r1(qin), f'{eta:.3f}', f'{xs:.3f}', r1(hs), r1(wnet_s), f'{eta_s:.3f}') == \
        ('0.9487', '2461.2', '1514.6', '3783.9', '0.400', '0.831', '2180.0', '1237.1', '0.384')
    # board: boiler with reheater, HP and LP turbines on one shaft, condenser and pump
    p = [box(.6, 4.6, 2.0, 2.4, 3.2, 'url(#hot)', '#B4512A', '#D0683A'), lab(*P(1.6, 5.8, 3.2), 'boiler', '#4A1A06', 15)]
    p += [box(5.0, 5.0, 2.4, 1.8, 1.1, 'url(#cold)', '#2F6E9C', '#3F86BE'), lab(*P(6.2, 5.9, 1.1), 'condenser', '#0E2238', 14)]
    p += [tube('x', 2.8, 4.2, 2.2, 1.6, .45, 'url(#tv)', 'url(#dm)'), tube('x', 4.4, 6.6, 2.2, 1.6, .8, 'url(#tv)', 'url(#dm)')]
    p += [lab(*P(3.5, 2.2, 2.35), 'HP', '#1A222B', 14), lab(*P(5.5, 2.2, 2.7), 'LP', '#1A222B', 14)]
    p += [pipe([(2.0, 4.6), (2.0, 2.2), (2.8, 2.2)], 1.6, '#FFB37A', 7), pipe([(4.0, 2.6), (4.0, 3.8), (2.6, 3.8), (2.6, 5.2)], 2.4, '#FFB37A', 6),
          pipe([(1.0, 4.6), (1.0, 3.2), (4.6, 3.2), (4.6, 2.6)], 2.9, '#FF7A45', 6), pipe([(6.2, 2.9), (6.2, 5.0)], .9, '#9FB0BF', 7),
          pipe([(5.0, 6.6), (3.2, 6.6), (2.6, 6.6)], .3, '#7CC4FF', 6)]
    p += [ucyl(3.6, 6.6, .35, .7)]
    # card: efficiency and exhaust dryness, simple against reheat
    s = hbars([('simple η', eta_s * 100, AC2, f'{eta_s * 100:.1f} %'), ('reheat η', eta * 100, ACC, f'{eta * 100:.1f} %')], 0, 450, 8, 24, 8, 50, 110)
    s += hbars([('simple x', xs * 100, AC2, f'{xs:.3f}'), ('reheat x', x4 * 100, ACC, f'{x4:.3f}')], 0, 450, 76, 24, 8, 125, 110)
    card = svgcard(s)
    return make('me-thermo-u6-L3', 'Rankine,<br>Reheat &amp;<br>Regeneration',
                'Reheat adds just <span class="gold">1.6</span> points;<br>it mainly <span class="cyan">dries</span> the exhaust',
                '60 bar, 500 °C plant', card, p,
                [chip('left', 262, 'g', 'reheat: 10 bar → 500 °C'), chip('left', 520, 'c', f'w<sub>net</sub> {r1(wnet)} kJ/kg'),
                 chip('right', 330, 'g', f'η = {eta * 100:.1f} %, not 47 %'), chip('right', 500, 'c', f'exhaust x = {x4:.3f}', False)],
                f'η = {r1(wnet)} ÷ {r1(qin)} = <b class="gl">{eta * 100:.1f} %</b> vs {eta_s * 100:.1f} % simple<br>'
                f'exhaust dryness {xs:.3f} → <b class="cl">{x4:.3f}</b> with reheat')


def u6L4():
    """6.7 worked example: 1 TR R-134a vapour compression cycle, −10 °C evaporator, 40 °C condenser"""
    h1, h2, h3, TR = 392.66, 426.48, 256.41, 3.517
    qL, w, qH = h1 - h3, h2 - h1, h2 - h3                    # 136.25, 33.82, 170.07 kJ/kg
    cop = qL / w; mdot = TR / qL; Pw = mdot * w
    copC = 263.15 / (313.15 - 263.15)
    wrong = qL / qH
    assert (f'{qL:.2f}', f'{w:.2f}', f'{qH:.2f}', f'{cop:.2f}', f'{mdot:.4f}', f'{Pw:.3f}', f'{copC:.2f}') == \
        ('136.25', '33.82', '170.07', '4.03', '0.0258', '0.873', '5.26')
    # board: compressor, condenser, expansion valve and evaporator in one loop
    p = [box(4.8, .8, 2.4, 1.6, 1.4, '#FFB37A', '#B4512A', '#D0683A'), box(.8, 4.8, 1.6, 2.4, 1.4, '#CFE9FF', '#2F6E9C', '#3F86BE')]
    for k in range(6):
        p.append(f'<polyline points="{pts(P(5.0 + k * .4, 2.4, .2), P(5.0 + k * .4, 2.4, 1.2))}" stroke="#7A2E0E" stroke-width="2.5"/>')
        p.append(f'<polyline points="{pts(P(2.4, 5.0 + k * .4, .2), P(2.4, 5.0 + k * .4, 1.2))}" stroke="#E9F5FF" stroke-width="2.5"/>')
    p += [lab(*P(6.0, 1.6, 1.4), 'condenser', '#4A1A06', 14), lab(*P(1.6, 6.0, 1.4), 'evaporator', '#0E2238', 14)]
    p += [pipe([(2.4, 6.0), (5.2, 6.0), (5.2, 5.2)], .7, '#9FB0BF', 7), pipe([(5.6, 4.6), (6.0, 4.6), (6.0, 2.4)], .7, '#FFB37A', 7),
          pipe([(4.8, 1.6), (1.6, 1.6), (1.6, 4.8)], .7, '#9FB0BF', 7)]
    p += [ucyl(5.6, 5.0, .7, 1.5), lab(*P(5.6, 5.0, .9), 'comp', '#1A222B', 13)]
    vx, vy = P(1.6, 3.2, .7)
    p += [f'<polygon points="{vx - 14:.1f},{vy - 10:.1f} {vx + 14:.1f},{vy + 10:.1f} {vx + 14:.1f},{vy - 10:.1f} {vx - 14:.1f},{vy + 10:.1f}" fill="#E04848"/>']
    ex, ey = P(5.6, 5.0, 1.5)
    p += [garrow(ex, ey - 16, ex, ey - 62, ACC, 6), wave(*P(6.6, 1.0, 1.6), ACC, 2, 26)]
    s = hbars([('q<tspan font-size="12" dy="3">L</tspan><tspan dy="-3"> cooling</tspan>', qL, AC2, f'{qL:.2f}'), ('w work in', w, ACC, f'{w:.2f}'),
               ('q<tspan font-size="12" dy="3">H</tspan><tspan dy="-3"> heat out</tspan>', qH, '#FFC79E', f'{qH:.2f} kJ/kg')], 0, 460, 6, 24, 8, qH * 1.45, 120)
    s += t_(235, 132, f'COP = q<tspan font-size="11" dy="3">L</tspan><tspan dy="-3"> ÷ w = {qL:.2f} ÷ {w:.2f} = {cop:.2f}</tspan>', 'pt', 'middle', ACC)
    card = svgcard(s)
    return make('me-thermo-u6-L4', 'Refrigeration:<br>Compression &amp;<br>Absorption',
                'COP = cooling ÷ <span class="gold">WORK</span>,<br>not ÷ <span class="cyan">heat out</span>',
                '1 TR, R-134a', card, p,
                [chip('left', 262, 'c', '−10 °C evaporator'), chip('left', 470, 'c', f'ṁ = {mdot:.4f} kg/s'),
                 chip('right', 262, 'g', f'COP = {cop:.2f}'), chip('right', 500, 'c', f'Carnot COP {copC:.2f}', False)],
                f'COP = q<sub>L</sub>/w = {qL:.2f} ÷ {w:.2f} = <b class="gl">{cop:.2f}</b><br>'
                f'1 TR: power = {mdot:.4f} × {w:.2f} = <b class="cl">{Pw:.3f} kW</b>')


def specs():
    return [f() for f in (u1L1, u1L2, u1L3, u2L1, u2L2, u2L3, u2L4, u3L1, u3L2, u3L3, u3L4, u3L5, u4L1, u4L2, u4L3,
                          u5L1, u5L2, u5L3, u5L4, u5L5, u6L1, u6L2, u6L3, u6L4)]
