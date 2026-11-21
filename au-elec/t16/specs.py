"""t16 split-blueprint thumbnails for Automotive Electronics (au-elec), department Auto.
One spec per lesson, each built from a worked example in that lesson's own chapters of
books/auto/au-elec/au-elec-u<N>.html; every number on the thumbnail is computed below.
Build: python3 t16_split.py build specs.py <out dir>   (t16_split.py from the data pack, thumbs/t16_split/)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
for _p in (os.environ.get('T16_TOOL', ''), '/home/user/work/t16/tool'):
    if _p and os.path.isdir(_p) and _p not in sys.path:
        sys.path.append(_p)
import t16_split as T
B = T.B

D = 'auto'
SIL, SKY = T.DEPTS[D]['acc'], T.DEPTS[D]['acc2']
AXC = '#6B7B8A'
SUBJECT = 'AUTO ELECTRONICS'
g = lambda v: f'{v:g}'


def f(v, n):
    """round to n decimals and print them all"""
    return f'{round(v + 0.0, n):.{n}f}'


def th(v):
    """thousands with a thin space, as the book writes 20 000"""
    return f'{v:,.0f}'.replace(',', ' ')


# ================================================================ isometric board helpers (board units, slab 8 x 8)
U = 33


def setup():
    B.U, B.OX, B.OY = U, 952, 318


def P(x, y, z=0):
    return B.P(x, y, z)


pts = B.pts
DARK = ('#2E3238', '#14161A', '#1E2126')
MID = ('#3E454D', '#1B1F24', '#2A3037')
STEEL = ('#C9D1D8', '#6E7984', '#9AA6B2')
BRIGHT = ('#E9EEF2', '#8D98A3', '#B7C1CA')
SKYB = ('#9BDBFF', '#2E6F96', '#4E9CC8')
GLASS = ('#5C7C93', '#22313D', '#33485A')

GR = ('<defs><linearGradient id="pl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#343C44"/><stop offset="1" stop-color="#1F252B"/></linearGradient>'
      '<linearGradient id="al" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7B8692"/><stop offset=".4" stop-color="#EEF2F5"/><stop offset=".65" stop-color="#B9C3CC"/><stop offset="1" stop-color="#5E6974"/></linearGradient>'
      '<linearGradient id="dk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1A1E23"/><stop offset=".4" stop-color="#4A535C"/><stop offset=".7" stop-color="#2C3238"/><stop offset="1" stop-color="#121518"/></linearGradient>'
      '<radialGradient id="pu" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#4A4F57"/><stop offset="1" stop-color="#16181C"/></radialGradient></defs>')


def board(parts):
    return T.iso_board(D, [GR] + parts, top='url(#pl)')


def bx(x, y, w, d, h, c, z0=0):
    return B.box(x, y, w, d, h, *c, z0=z0)


def glow(s):
    return f'<g filter="url(#gl)">{s}</g>'


def line3(p, col, w=4, dash=None, op=1):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<polyline points="{pts(*[P(*q) for q in p])}" fill="none" stroke="{col}" stroke-width="{w}" '
            f'stroke-linejoin="round" stroke-linecap="round" opacity="{op}"{da}/>')


def arrow3(a, b, col, w=5):
    return T.arrow(*P(*a), *P(*b), col, w)


def label(x, y, z, text, size=15, col='#E6ECF1', anchor='middle', dx=0, dy=0, halo=True):
    X, Y = P(x, y, z)
    h = ';paint-order:stroke;stroke:#0E1216;stroke-width:4px;stroke-linejoin:round' if halo else ''
    return (f'<text x="{X + dx:.1f}" y="{Y + dy:.1f}" text-anchor="{anchor}" class="capl" '
            f'style="font-size:{size}px;fill:{col}{h}">{text}</text>')


def ucyl(x, y, z, r, h, body, top):
    """upright cylinder of radius r standing on (x, y, z), h board units tall"""
    cx, cy = P(x, y, z)
    return T.cyl(cx, cy, 1.2247 * r * U, .7071 * r * U, h * U, body, top)


def hull(p):
    p = sorted(set((round(a, 2), round(b, 2)) for a, b in p))
    if len(p) < 3:
        return p
    cr = lambda o, a, b: (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for q in p:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], q) <= 0:
            lo.pop()
        lo.append(q)
    for q in reversed(p):
        while len(up) >= 2 and cr(up[-2], up[-1], q) <= 0:
            up.pop()
        up.append(q)
    return lo[:-1] + up[:-1]


def ring(axis, a, c1, c2, r, n=40):
    if axis == 'x':
        return [P(a, c1 + r * math.cos(t), c2 + r * math.sin(t)) for t in (2 * math.pi * k / n for k in range(n))]
    return [P(c1 + r * math.cos(t), a, c2 + r * math.sin(t)) for t in (2 * math.pi * k / n for k in range(n))]


def hcyl(axis, a0, a1, c1, c2, r, body, cap, stroke=None):
    """lying cylinder along the x or y axis from a0 to a1 (a1 the visible end); centre line at (c1, z = c2)"""
    s = f' stroke="{stroke}" stroke-width="1.5"' if stroke else ''
    return (f'<polygon points="{pts(*hull(ring(axis, a0, c1, c2, r) + ring(axis, a1, c1, c2, r)))}" fill="{body}"/>'
            f'<polygon points="{pts(*ring(axis, a1, c1, c2, r))}" fill="{cap}"{s}/>')


def flat_circle(x, y, z, r, n=48):
    return [P(x + r * math.cos(t), y + r * math.sin(t), z) for t in (2 * math.pi * k / n for k in range(n))]


def car(x, y, head, c=STEEL, L=2.4, W=1.2):
    """a simple car: body, cabin and four wheels; head 'x' or 'y' is the direction it drives"""
    o = []
    wr = .3
    if head == 'x':
        far = [hcyl('y', y - .08, y + .16, x + q, wr, wr, '#0B0D10', '#23272C') for q in (.5, L - .5)]
        near = [hcyl('y', y + W - .16, y + W + .08, x + q, wr, wr, '#0B0D10', '#2B3036', '#5E6974') for q in (.5, L - .5)]
        o += far + [bx(x, y, L, W, .42, c, z0=.22), bx(x + .55, y + .08, 1.15, W - .16, .38, GLASS, z0=.64)] + near
    else:
        far = [hcyl('x', x - .08, x + .16, y + q, wr, wr, '#0B0D10', '#23272C') for q in (.5, L - .5)]
        near = [hcyl('x', x + W - .16, x + W + .08, y + q, wr, wr, '#0B0D10', '#2B3036', '#5E6974') for q in (.5, L - .5)]
        o += far + [bx(x, y, W, L, .42, c, z0=.22), bx(x + .08, y + .55, W - .16, 1.15, .38, GLASS, z0=.64)] + near
    return ''.join(o)


def ecu(x, y, w=1.6, d=1.1, h=.5, name='ECU'):
    o = [bx(x, y, w, d, h, MID)]
    for k in range(5):
        o.append(bx(x + .2 + k * (w - .4) / 4 - .05, y + d - .02, .1, .12, .1, BRIGHT, z0=.15))
    o.append(label(x + w / 2, y + d / 2, h, name, size=15, col=SIL, dy=5))
    return ''.join(o)


def battery(x, y, w=1.7, d=1.1, h=.75, name='battery'):
    o = [bx(x, y, w, d, h, DARK),
         ucyl(x + .35, y + .3, h, .13, .14, '#7B8692', '#C9D1D8'), ucyl(x + w - .35, y + .3, h, .13, .14, '#7B8692', '#C9D1D8'),
         label(x + w / 2, y + d, h * .45, name, size=14, dy=6)]
    return ''.join(o)


# ================================================================ card helpers (470 x 144 SVG)
def svg(inner):
    return f'<svg width="470" height="144" viewBox="0 0 470 144">{inner}</svg>'


def tx(x, y, s, cls='ax', anchor='middle', col=None, size=None):
    st = []
    if col:
        st.append(f'fill:{col}')
    if size:
        st.append(f'font-size:{size}px')
    sty = f' style="{";".join(st)}"' if st else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}"{sty}>{s}</text>'


def axes(x0, x1, y0=118, y1=28):
    return (f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{AXC}" stroke-width="1.5"/>'
            f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{AXC}" stroke-width="1.5"/>')


def lin(v, a, b, A, Bv):
    return A + (v - a) / (b - a) * (Bv - A)


def poly(p, col, w=3, dash=None, fill='none', op=1):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in p)}" fill="{fill}" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" opacity="{op}"{da}/>'


def dot(x, y, col, r=5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>'


def vdash(x, y0, y1, col):
    return f'<line x1="{x:.1f}" y1="{y0:.1f}" x2="{x:.1f}" y2="{y1:.1f}" stroke="{col}" stroke-width="1.8" stroke-dasharray="5 4"/>'


def hdash(y, x0, x1, col):
    return f'<line x1="{x0:.1f}" y1="{y:.1f}" x2="{x1:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="1.8" stroke-dasharray="5 4"/>'


TABLE_CSS = """
.scope table{border-collapse:collapse;width:100%;margin-top:2px;font:600 17px 'IBM Plex Sans';color:#E6ECF1}
.scope th{font:600 14px 'IBM Plex Sans';color:#AFC0CE;text-align:center;padding:3px 6px;border-bottom:1.5px solid rgba(200,214,226,.3)}
.scope td{text-align:center;padding:6px 6px;border-bottom:1px solid rgba(200,214,226,.16);font-size:18px}
.scope td:first-child{text-align:left;font-weight:700}.scope tr:last-child td{border-bottom:none}"""


def chip(side, top, kind, text, pointer=True):
    return dict(side=side, top=top, kind=kind, text=text, pointer=pointer)


def spec(key, title, hook, takeaway, card_title, card, board_svg, chips, summary, css='', size=None):
    s = dict(key=key, dept=D, subject=SUBJECT, title=title, question=hook, takeaway=takeaway, tag='Book example',
             card_title=card_title, card=card, board=board_svg, chips=chips, summary=summary,
             page_title=title.replace('<br>', ' ') + ': Automotive Electronics')
    if size:
        css += f'\nh1{{font-size:{size}px !important}}'
    if css:
        s['css'] = css
    assert len(card_title.replace('&amp;', '&')) <= 30, card_title
    return s


def gold(w):
    return f'<span class="gold">{w}</span>'


def cyan(w):
    return f'<span class="cyan">{w}</span>'


# ================================================================ unit 1
def u1_l1():
    """1.1 worked example: 1970 dynamo 35 A vs 2020 alternator 120 A, both at 14.0 V (the owner-approved sample)."""
    V, I1, I2 = 14.0, 35, 120
    P1, P2 = V * I1, V * I2
    inc, ratio = P2 - P1, P2 / P1
    h1 = 90 * P1 / P2
    card = svg(f'<line x1="40" y1="118" x2="440" y2="118" stroke="{AXC}" stroke-width="1.5"/>'
               f'<rect x="90" y="{118 - h1:.1f}" width="90" height="{h1:.1f}" rx="8" fill="#6E7984" opacity=".95"/>'
               + tx(135, 118 - h1 - 8, f'{g(P1)} W', 'pt', col='#9AA6B2') + tx(135, 136, f'1970 · {I1} A')
               + f'<rect x="300" y="28.0" width="90" height="90.0" rx="8" fill="{SIL}" opacity=".9"/>'
               + tx(345, 20, f'{g(P2)} W', 'pt', col=SIL) + tx(345, 136, f'2020 · {I2} A')
               + f'<path d="M192 {118 - h1 - 4:.1f} Q240 22 292 34" fill="none" stroke="{SKY}" stroke-width="2.5" stroke-dasharray="6 5"/>'
               + tx(240, 36, f'× {f(ratio, 1)}', 'pt', col=SKY))
    return spec('au-elec-u1-L1', 'Car Electrics:<br>Evolution &amp;<br>Supply', 'Why is the 12 V bus really 14 V?',
                f"12 V is the battery's {gold('NAME')} —<br>the bus runs at {cyan('14 V')}",
                f'same {f(V, 1)} V, more amps', card, L1_BOARD,
                [chip('left', 300, 'g', f'1970: {I1} A dynamo'), chip('left', 364, 'g', f'2020: {I2} A alternator'),
                 chip('left', 470, 'c', f'both at {f(V, 1)} V'), chip('right', 318, 'g', f'+{g(inc)} W'),
                 chip('right', 500, 'c', 'P = V × I', False)],
                f'<b class="gl">P = V × I:</b> {f(V, 1)} × {I1} = <b class="gl">{g(P1)} W</b> → {f(V, 1)} × {I2} = <b class="cl">{g(P2)} W</b><br>'
                f'increase {g(inc)} W, about <b class="cl">{f(ratio, 1)}×</b> the 1970 value')


def u1_l2():
    """1.4 worked example: six 2.1 V cells in series; one cell shorted."""
    vc, n = 2.1, 6
    good, bad = n * vc, (n - 1) * vc
    setup()
    o = [bx(2.2, 1.2, 4.4, 1.8, 1.5, DARK)]
    for k in range(n):
        c = ('#7A3A30', '#3A1B16', '#5A2620') if k == 3 else STEEL
        o.append(bx(2.3 + k * .72, 1.35, .64, 1.5, .1, c, z0=1.5))
    o.append(ucyl(2.62, 2.1, 1.6, .2, .25, '#8D98A3', SIL))
    o.append(ucyl(6.22, 2.1, 1.6, .2, .25, '#2B3036', '#5E6974'))
    o.append(label(2.62, 2.1, 2.0, '+', size=22, col=SIL, dy=-4))
    o.append(label(6.22, 2.1, 2.0, '−', size=22, col=SKY, dy=-4))
    o.append(label(2.3 + 3 * .72 + .32, 2.1, 1.6, '0 V', size=14, col='#FFB3A6', dy=4))
    # one cell opened: lead dioxide (+, brown) and lead (−, grey) plates alternate
    for k in range(5):
        c = ('#9A633F', '#4A2E1E', '#74482C') if k % 2 == 0 else ('#B9C1C9', '#5E6670', '#8A949E')
        o.append(bx(5.6 + k * .38, 4.0, .14, 1.3, 1.4, c))
    o.append(label(6.4, 5.3, 0, 'brown PbO₂ (+) · grey Pb (−)', size=14, col='#E9C4A8', dx=20, dy=26))
    brd = board(o)
    # card: two stacked bars of 2.1 V blocks
    W = 330 / 13.0
    def bar(y, cells, col, lab):
        s = tx(8, y + 22, lab, 'pt', 'start', col)
        for k in range(cells):
            s += f'<rect x="{78 + k * vc * W:.1f}" y="{y}" width="{vc * W - 3:.1f}" height="32" rx="5" fill="{col}" opacity="{.9 if k % 2 == 0 else .7}"/>'
            s += tx(78 + (k + .5) * vc * W - 1.5, y + 22, f'{vc}', 'ax', col='#10151A')
        return s
    card = svg(bar(14, n, SIL, '6 cells') + tx(78 + good * W + 8, 36, f'{g(good)} V', 'pt', 'start', SIL)
               + bar(66, n - 1, SKY, '1 short') + tx(78 + bad * W + 8, 88, f'{g(bad)} V', 'pt', 'start', SKY)
               + f'<line x1="78" y1="112" x2="458" y2="112" stroke="{AXC}" stroke-width="1.5"/>'
               + ''.join(tx(78 + v * W, 132, f'{v}') for v in (0, 4, 8, 12)) + tx(458, 132, 'V', anchor='end'))
    return spec('au-elec-u1-L2', 'EMC &amp; the<br>Lead-acid<br>Battery', 'Which plate is lead dioxide?',
                f'{gold("PbO₂")} is the positive plate;<br>each cell gives {cyan(f"{vc} V")}',
                f'six {vc} V cells in series', card, brd,
                [chip('left', 300, 'c', f'{vc} V per cell'), chip('left', 364, 'g', f'{n} cells in series'),
                 chip('left', 470, 'c', 'one cell shorted'), chip('right', 300, 'g', f'{g(good)} V'),
                 chip('right', 500, 'c', f'{g(bad)} V', False)],
                f'healthy: <b class="gl">{n} × {vc} V = {g(good)} V</b>, the cells add in series<br>'
                f'one cell shorted: {n - 1} × {vc} V = <b class="cl">{g(bad)} V</b>')


def u1_l3():
    """1.7 worked example 2: self-limiting alternator, I = Imax (1 - n0/n)."""
    n0, Ir, nr, ratio, idle, load = 1000, 120, 6000, 2.5, 800, 70
    Imax = Ir / (1 - n0 / nr)
    nalt = idle * ratio
    Iidle = Imax * (1 - n0 / nalt)
    n70 = n0 / (1 - load / Imax)
    e70 = n70 / ratio
    setup()
    o = []
    R1, R2 = 1.25, 1.25 / ratio
    # alternator body behind its small pulley, engine crank pulley in front; one belt round both
    o.append(hcyl('x', 3.0, 4.5, 1.8, .5 + R2, .9, 'url(#al)', '#C9D1D8', '#6E7984'))
    o.append(hcyl('x', 4.5, 4.75, 1.8, .5 + R2, R2, '#1B1F24', '#3E454D', '#8D98A3'))
    o.append(hcyl('x', 4.3, 4.65, 5.0, .5 + R1, R1, '#1B1F24', '#2A3037', '#8D98A3'))
    o.append(hcyl('x', 4.65, 4.9, 5.0, .5 + R1, .25, '#5E6974', '#9AA6B2'))
    o.append(glow(line3([(4.8, 5.0, .5 + 2 * R1), (4.8, 1.8, .5 + 2 * R2)], SKY, 4)))
    o.append(glow(line3([(4.8, 5.0, .5), (4.8, 1.8, .5)], SKY, 4)))
    o.append(label(4.8, 5.0, 0, f'engine {idle} rpm', size=15, dx=-30, dy=26))
    o.append(label(3.8, 1.8, .5 + 2 * R2 + .4, f'alternator {g(nalt)} rpm', size=15, dy=-14))
    brd = board(o)
    # card: I against alternator speed
    X = lambda n: lin(n, 0, 6500, 50, 455)
    Y = lambda i: lin(i, 0, 150, 118, 22)
    curve = [(X(n), Y(Imax * (1 - n0 / n))) for n in range(n0, 6501, 100)]
    card = svg(axes(50, 458) + poly(curve, SIL, 3.5) + hdash(Y(load), 50, 455, SKY)
               + tx(455, Y(load) + 16, f'loads {load} A', 'ax', 'end', SKY)
               + vdash(X(nalt), 118, Y(Iidle), SKY) + dot(X(nalt), Y(Iidle), SKY) + tx(X(nalt) - 8, Y(Iidle) - 10, f'{g(Iidle)} A at idle', 'pt', 'end', SKY)
               + dot(X(nr), Y(Ir), SIL) + tx(X(nr) - 8, Y(Ir) - 10, f'{Ir} A', 'pt', 'end', SIL)
               + ''.join(tx(X(n), 136, g(n)) for n in (0, 2000, 4000, 6000)) + tx(456, 110, 'rpm', anchor='end')
               + tx(44, 32, 'A', anchor='end') + tx(X(n0), 136, g(n0), col='#9AA6B2'))
    return spec('au-elec-u1-L3', 'Charging<br>System &amp;<br>Alternator', 'Does revving raise the bus voltage?',
                f'Revs raise the {gold("AMPS")};<br>the regulator holds {cyan("14 V")}',
                'alternator current vs speed', card, brd,
                [chip('left', 300, 'c', f'n₀ = {n0} rpm'), chip('left', 364, 'c', f'pulley ratio {ratio}'),
                 chip('left', 470, 'g', f'I<sub>max</sub> = {g(Imax)} A'), chip('right', 318, 'g', f'{g(Iidle)} A at idle'),
                 chip('right', 500, 'c', f'{load} A from {g(round(e70))} rpm', False)],
                f'I<sub>max</sub> = {Ir} ÷ (1 − {n0} ÷ {nr}) = <b class="gl">{g(Imax)} A</b><br>'
                f'idle: {idle} × {ratio} = {g(nalt)} rpm → {g(Imax)} × 0.5 = <b class="cl">{g(Iidle)} A</b>')


def u1_l4():
    """1.10 worked example: a crank draws 250 A at 10.5 V for 2.0 s."""
    I, V, t = 250, 10.5, 2.0
    Q = I * t
    Ah = Q / 3600
    Pw = V * I
    E = Pw * t
    setup()
    o = [bx(4.4, .8, 2.0, 1.4, 1.1, DARK),
         ucyl(4.8, 1.2, 1.1, .16, .16, '#7B8692', '#C9D1D8'), ucyl(6.0, 1.2, 1.1, .16, .16, '#7B8692', '#C9D1D8'),
         label(5.4, 2.2, .5, 'battery', size=15, dy=6)]
    o.append(glow(line3([(4.8, 1.2, 1.3), (4.8, 1.2, 2.0), (3.6, 3.0, 2.0), (3.6, 4.6, 1.65)], SKY, 10)))
    o.append(label(4.2, 2.1, 2.0, f'{I} A', size=18, col=SKY, dy=-14))
    o.append(hcyl('x', 2.0, 4.9, 4.6, .9, .8, 'url(#dk)', '#3E454D', '#8D98A3'))
    o.append(hcyl('x', 4.9, 5.6, 4.6, .9, .45, '#7B8692', '#B7C1CA'))
    o.append(hcyl('x', 5.6, 6.0, 4.6, .9, .24, '#9AA6B2', SIL))
    o.append(label(4.0, 5.4, 0, 'starter motor', size=15, dy=26))
    brd = board(o)
    # card: current pulse and power pulse
    def pulse(x0, title, top, unit, area, col):
        X0, X1 = x0 + 44, x0 + 214
        s = tx(x0 + 129, 18, title, 'pt', col=col) + axes(X0, X1)
        xa = lin(t, 0, 2.6, X0, X1)
        s += f'<rect x="{X0 + 2}" y="40" width="{xa - X0 - 2:.1f}" height="78" fill="{col}" fill-opacity=".18" stroke="{col}" stroke-width="3"/>'
        s += tx((X0 + xa) / 2, 86, area, 'pt', col=col) + tx(X0 - 6, 46, top, anchor='end') + tx(xa, 136, f'{f(t, 1)} s') + tx(X0, 136, '0')
        return s
    card = svg(pulse(0, 'current', f'{I} A', 'A', f'{g(Q)} C', SKY) + pulse(240, 'power', f'{g(Pw)} W', 'W', f'{g(E)} J', SIL))
    return spec('au-elec-u1-L4', 'Starting<br>Systems &amp; Power<br>Distribution', 'Does the key carry 250 A?',
                f'The key works the {gold("SOLENOID")};<br>{I} A takes the {cyan("thick")} cable',
                f'one {f(t, 1)} s crank', card, brd,
                [chip('left', 300, 'g', f'I = {I} A'), chip('left', 364, 'c', f'V = {V} V'),
                 chip('left', 470, 'c', f't = {f(t, 1)} s'), chip('right', 318, 'g', f'{g(Pw)} W'),
                 chip('right', 500, 'c', f'{g(Q)} C = {f(Ah, 3)} Ah', False)],
                f'Q = {I} × {f(t, 1)} = <b class="gl">{g(Q)} C</b> = {f(Ah, 3)} Ah<br>'
                f'P = {V} × {I} = {g(Pw)} W → E = <b class="cl">{g(E)} J</b>', size=66)


# ================================================================ unit 2
def u2_l1():
    """2.2 worked example: 8 mH coil, 6 A, 1:100, 250 V primary emf; firing line Vf = 10 + 22 g."""
    L, I, n, V1 = .008, 6, 100, 250
    E = .5 * L * I ** 2
    V2 = n * V1 / 1000
    gap = .9
    Vf = 10 + 22 * gap
    gmax = (V2 - 10) / 22
    setup()
    o = []
    o.append(ucyl(2.4, 3.4, 0, .95, 2.4, 'url(#dk)', '#3E454D'))
    o.append(ucyl(2.4, 3.4, 2.4, .32, .45, '#B7C1CA', SIL))
    o.append(ucyl(1.75, 2.9, 2.4, .12, .2, '#7B8692', SIL))
    o.append(ucyl(2.0, 2.65, 2.4, .12, .2, '#7B8692', SIL))
    o.append(label(2.4, 3.4, 3.1, 'coil 1 : 100', size=15, dy=-12))
    # spark plug standing on the right: electrode, thread, hex, white insulator, terminal
    px, py = 5.6, 2.3
    o.append(ucyl(px, py, .15, .24, .6, '#8D98A3', '#B7C1CA'))
    o.append(B.box(px - .38, py - .38, .76, .76, .45, *STEEL, z0=.75))
    o.append(ucyl(px, py, 1.2, .22, 1.3, '#EEF2F5', '#FFFFFF'))
    o.append(ucyl(px, py, 2.5, .1, .25, '#7B8692', SIL))
    X, Y = P(px, py, .1)
    o.append(glow(f'<path d="M{X - 12:.1f},{Y + 4:.1f} l7,-9 l5,8 l8,-12" fill="none" stroke="{SKY}" stroke-width="3.5"/>'))
    o.append(glow(f'<path d="M{P(2.4, 3.4, 2.85)[0]:.1f},{P(2.4, 3.4, 2.85)[1]:.1f} Q{P(4.2, 2.6, 4.3)[0]:.1f},{P(4.2, 2.6, 4.3)[1]:.1f} {P(px, py, 2.75)[0]:.1f},{P(px, py, 2.75)[1]:.1f}" fill="none" stroke="{SKY}" stroke-width="4"/>'))
    o.append(label(px, py, 0, 'spark plug', size=15, dy=30))
    brd = board(o)
    Xg = lambda v: lin(v, 0, 1.2, 50, 455)
    Yv = lambda v: lin(v, 0, 40, 118, 22)
    card = svg(axes(50, 458) + poly([(Xg(0), Yv(10)), (Xg(1.2), Yv(10 + 22 * 1.2))], SIL, 3.5)
               + hdash(Yv(V2), 50, 455, SKY) + tx(54, Yv(V2) - 6, f'coil gives {g(V2)} kV', 'ax', 'start', SKY)
               + dot(Xg(gmax), Yv(V2), SKY) + vdash(Xg(gmax), 118, Yv(V2), SKY) + tx(Xg(gmax), 112 - 0, f'{f(gmax, 2)} mm', 'ax', 'middle', SKY)
               + dot(Xg(gap), Yv(Vf), SIL) + tx(Xg(gap) - 10, Yv(Vf) - 4, f'{gap} mm needs {g(round(Vf, 1))} kV', 'pt', 'end', SIL)
               + ''.join(tx(Xg(v), 136, g(v)) for v in (0, .4, .8, 1.2)) + tx(456, 110, 'gap, mm', anchor='end')
               + tx(44, 32, 'kV', anchor='end'))
    return spec('au-elec-u2-L1', 'Coil Ignition<br>&amp; Spark<br>Plugs', 'How does 12 V become a 25 kV spark?',
                f'The coil\'s {gold("1 : 100")} turns<br>step {V1} V up to {cyan(f"{g(V2)} kV")}',
                f'will {g(V2)} kV fire the gap?', card, brd,
                [chip('left', 300, 'c', f'1 : {n} turns'), chip('left', 364, 'c', f'{V1} V primary'),
                 chip('left', 470, 'c', f'{g(L * 1000)} mH, {I} A'), chip('right', 318, 'g', f'{g(V2)} kV'),
                 chip('right', 500, 'g', f'{g(E * 1000)} mJ', False)],
                f'V₂ = {n} × {V1} V = <b class="gl">{g(V2)} kV</b>; E = ½LI² = {g(E * 1000)} mJ<br>'
                f'{gap} mm needs {g(round(Vf, 1))} kV → fires up to <b class="cl">{f(gmax, 2)} mm</b>')


def u2_l2():
    """2.4 worked example: waste spark at 4000 rpm, firing order 1-3-4-2, coils 1 & 4 and 2 & 3."""
    rpm = 4000
    rps = rpm / 60
    cyc = 2 / rps * 1000
    per_coil = rps
    step = 180 * cyc / 720
    fire = {1: 0, 3: 180, 4: 360, 2: 540}
    setup()
    o = []
    xs = [1.4, 2.7, 4.0, 5.3]
    # engine block with 4 cylinders in a row, plug tops; coils bridge 1 & 4 and 2 & 3
    o.append(bx(.8, 3.2, 6.0, 1.6, 1.2, MID))
    for k, x in enumerate(xs):
        o.append(ucyl(x + .25, 4.0, 1.2, .38, .08, '#14161A', '#1E2126'))
        o.append(ucyl(x + .25, 4.0, 1.28, .12, .3, '#EEF2F5', '#FFFFFF'))
        o.append(label(x + .25, 4.8, .6, f'{k + 1}', size=17, col=SIL, dy=8))
    # coil A (1 & 4) and coil B (2 & 3) as boxes above, leads drawn as arcs
    o.append(bx(2.2, 1.3, 1.0, .9, .9, DARK, z0=1.6))
    o.append(bx(4.0, 1.3, 1.0, .9, .9, ('#4E9CC8', '#1E4A66', '#2E6F96'), z0=1.6))
    o.append(line3([(2.4, 2.2, 1.9), (1.65, 4.0, 1.6)], SIL, 3))
    o.append(line3([(3.0, 2.2, 1.9), (5.55, 4.0, 1.6)], SIL, 3))
    o.append(line3([(4.2, 2.2, 1.9), (2.95, 4.0, 1.6)], SKY, 3))
    o.append(line3([(4.8, 2.2, 1.9), (4.25, 4.0, 1.6)], SKY, 3))
    o.append(glow(ucyl(1.65, 4.0, 1.58, .16, .02, SIL, SIL)))
    o.append(glow(ucyl(5.55, 4.0, 1.58, .16, .02, '#8D98A3', '#8D98A3')))
    o.append(label(2.7, 1.75, 2.5, '1 &amp; 4', size=15, col=SIL, dy=5))
    o.append(label(4.5, 1.75, 2.5, '2 &amp; 3', size=15, col='#E8F7FF', dy=5))
    brd = board(o)
    Xa = lambda a: lin(a, 0, 720, 70, 450)
    s = axes(70, 452, 118, 118)
    rows = [('1 &amp; 4', 46, SIL, [(0, 1, 4), (360, 4, 1)]), ('2 &amp; 3', 92, SKY, [(180, 3, 2), (540, 2, 3)])]
    for name, y, col, ev in rows:
        s += tx(8, y + 5, name, 'pt', 'start', col) + f'<line x1="70" y1="{y}" x2="450" y2="{y}" stroke="{AXC}" stroke-width="1" opacity=".5"/>'
        for a, use, waste in ev:
            s += f'<rect x="{Xa(a) - 4:.1f}" y="{y - 18}" width="8" height="30" rx="3" fill="{col}"/>'
            s += tx(Xa(a) + 10, y - 4, f'{use}', 'pt', 'start', col) + tx(Xa(a) + 10, y + 13, f'{waste} exh', 'ax', 'start')
    s += ''.join(tx(Xa(a), 136, f'{a}°') for a in (0, 180, 360, 540, 720))
    card = svg(s)
    return spec('au-elec-u2-L2', 'Electronic &amp;<br>Distributorless<br>Ignition', 'Why does a waste spark fire twice?',
                f'One spark on {gold("COMPRESSION")},<br>its twin on {cyan("exhaust")}',
                f'waste spark at {rpm} rpm', card, brd,
                [chip('left', 300, 'c', 'firing order 1-3-4-2'), chip('left', 364, 'g', 'coil 1 &amp; 4'),
                 chip('left', 470, 'c', 'coil 2 &amp; 3'), chip('right', 300, 'g', f'every {g(step)} ms'),
                 chip('right', 500, 'c', f'{g(round(cyc, 1))} ms cycle', False)],
                f'{rpm} rpm: one 720° cycle = 2 rev = <b class="gl">{g(round(cyc, 1))} ms</b><br>'
                f'each coil fires every 360°: <b class="cl">{f(per_coil, 1)} times/s</b>')


def u2_l3():
    """2.5 worked example 2: a 20 000 cd beam on a sign at 25 m and 50 m."""
    I, d1, d2 = 20000, 25, 50
    E1, E2 = I / d1 ** 2, I / d2 ** 2
    setup()
    o = []
    # beam: a glowing wedge from the lamp to the far sign
    a, b, c = P(1.4, 4.0, 1.1), P(7.1, 2.9, 1.1), P(7.1, 5.1, 1.1)
    o.append(f'<polygon points="{pts(a, b, c)}" fill="{SKY}" opacity=".16"/>')
    o.append(f'<polygon points="{pts(a, P(4.2, 3.45, 1.1), P(4.2, 4.55, 1.1))}" fill="{SKY}" opacity=".14"/>')
    # headlamp
    o.append(bx(.4, 3.3, 1.0, 1.4, 1.3, DARK, z0=.2))
    o.append(hcyl('x', 1.35, 1.45, 4.0, .85, .5, '#9BDBFF', '#E8F7FF'))
    o.append(label(.9, 4.7, .2, 'headlamp', size=13, dy=16))

    def sign(x, lab, col):
        return (bx(x, 3.95, .1, .1, 1.0, STEEL) + bx(x - .05, 3.45, .12, 1.1, .9, (col, '#4A535C', col), z0=1.0)
                + label(x, 4.0, 2.2, lab, size=15, col=col, dy=-6))
    o.append(sign(4.2, f'{d1} m: {g(E1)} lx', SIL))
    o.append(sign(7.1, f'{d2} m: {g(E2)} lx', SKY))
    brd = board(o)
    Xd = lambda d: lin(d, 15, 60, 60, 455)
    Ye = lambda e: lin(e, 0, 90, 118, 24)
    curve = [(Xd(d), Ye(I / d ** 2)) for d in [15 + k * .5 for k in range(91)]]
    card = svg(axes(60, 458) + poly(curve, SIL, 3.5) + vdash(Xd(d1), 118, Ye(E1), SIL) + dot(Xd(d1), Ye(E1), SIL)
               + tx(Xd(d1) + 10, Ye(E1) - 6, f'{g(E1)} lx', 'pt', 'start', SIL)
               + vdash(Xd(d2), 118, Ye(E2), SKY) + dot(Xd(d2), Ye(E2), SKY) + tx(Xd(d2), Ye(E2) - 12, f'{g(E2)} lx', 'pt', 'middle', SKY)
               + ''.join(tx(Xd(d), 136, f'{d}') for d in (25, 50)) + tx(456, 110, 'd, m', anchor='end') + tx(54, 32, 'lx', anchor='end')
               + tx(300, 60, f'E = {th(I)} ÷ d²', 'pt', 'start', '#AFC0CE'))
    return spec('au-elec-u2-L3', 'Vehicle Lighting<br>&amp; Adaptive<br>Headlamps', 'Twice the distance: half the light?',
                f'Twice as far gets a {gold("QUARTER")}<br>of the light: E falls as {cyan("1/d²")}',
                'inverse-square law', card, brd,
                [chip('left', 300, 'g', f'{th(I)} cd'), chip('left', 364, 'c', f'{d1} m: {g(E1)} lx'),
                 chip('left', 470, 'c', '2 × the distance'), chip('right', 318, 'g', f'{d2} m: {g(E2)} lx'),
                 chip('right', 500, 'c', 'E = I ÷ d²', False)],
                f'E = I ÷ d²: {th(I)} ÷ {d1}² = <b class="gl">{g(E1)} lx</b><br>'
                f'{th(I)} ÷ {d2}² = <b class="cl">{g(E2)} lx</b>: a quarter, not a half', size=64)


def u2_l4():
    """2.9 worked example 2: two 4.5 A horns through a relay with an 80 ohm coil."""
    Ih, V, Rc = 4.5, 12, 80
    Ib = 2 * Ih
    Ic = V / Rc
    ratio = Ib / Ic
    Psw = V * Ib
    setup()
    o = []
    # left to right on the page: two horns, the relay, the horn button
    def horn(x, y):
        return (hcyl('y', y - .4, y, x, 1.0, .55, '#1B1F24', '#2A3037') + hcyl('y', y, y + .45, x, 1.0, .68, '#7B8692', '#B7C1CA')
                + hcyl('y', y + .44, y + .46, x, 1.0, .26, '#3E454D', '#5E6974'))
    o.append(glow(line3([(4.8, 3.2, .4), (4.8, 4.4, .4), (2.6, 4.4, .4)], SIL, 7)))
    o.append(horn(2.4, 5.2))
    o.append(horn(4.0, 5.2))
    o.append(label(3.2, 5.6, 1.7, '2 horns', size=15, dy=-6))
    o.append(label(4.8, 4.4, .4, f'{f(Ib, 1)} A', size=16, col=SIL, dx=24, dy=32))
    o.append(bx(4.2, 2.0, 1.2, 1.2, 1.2, MID))
    o.append(label(4.8, 2.6, 1.2, 'relay', size=15, col=SIL, dy=5))
    o.append(glow(line3([(6.6, 1.0, .2), (6.6, 2.6, .2), (5.4, 2.6, .2)], SKY, 3)))
    o.append(label(6.6, 2.0, .2, f'{g(Ic)} A', size=15, col=SKY, dx=26, dy=18))
    o.append(ucyl(6.6, 1.0, 0, .6, .35, '#1E2126', '#3E454D'))
    o.append(ucyl(6.6, 1.0, .35, .38, .2, '#7B8692', SIL))
    o.append(label(6.6, 1.0, .9, 'horn button', size=14, dy=-8))
    brd = board(o)
    Yb = lambda a: lin(a, 0, 10, 118, 26)
    card = svg(f'<line x1="40" y1="118" x2="440" y2="118" stroke="{AXC}" stroke-width="1.5"/>'
               + f'<rect x="80" y="{Yb(Ib):.1f}" width="100" height="{118 - Yb(Ib):.1f}" rx="8" fill="{SIL}" opacity=".9"/>'
               + tx(130, Yb(Ib) - 8, f'{f(Ib, 1)} A', 'pt', col=SIL) + tx(130, 136, 'no relay')
               + f'<rect x="290" y="{Yb(Ic):.1f}" width="100" height="{max(118 - Yb(Ic), 2):.1f}" rx="2" fill="{SKY}"/>'
               + tx(340, Yb(Ic) - 8, f'{g(Ic)} A', 'pt', col=SKY) + tx(340, 136, 'with relay')
               + f'<path d="M190 {Yb(Ib) + 10:.1f} Q250 40 285 100" fill="none" stroke="{SKY}" stroke-width="2.5" stroke-dasharray="6 5"/>'
               + tx(262, 52, f'÷ {g(ratio)}', 'pt', col=SKY))
    return spec('au-elec-u2-L4', 'Dashboards,<br>Wipers &amp; Keys', 'Can an immobilised engine crank?',
                f'Immobilised: it {gold("CRANKS")},<br>but gets no fuel or {cyan("spark")}',
                'current in the horn button', card, brd,
                [chip('left', 300, 'c', f'2 horns × {Ih} A'), chip('left', 364, 'c', f'coil {Rc} Ω'),
                 chip('left', 470, 'g', f'{f(Ib, 1)} A → {g(Ic)} A'), chip('right', 318, 'g', f'{g(ratio)}× less'),
                 chip('right', 500, 'c', f'contacts {g(Psw)} W', False)],
                f'no relay: the button carries 2 × {Ih} = <b class="gl">{f(Ib, 1)} A</b><br>'
                f'with relay: {V} ÷ {Rc} = <b class="cl">{g(Ic)} A</b>, {g(ratio)} times less')


# ================================================================ unit 3
def u3_l1():
    """3.2 worked example: NTC divider (1 kOhm pull-up to 5 V) into a 10-bit ADC."""
    Vs, Rf = 5, 1000
    rows = []
    for T_, Rs in ((25, 2000), (80, 500)):
        V = Vs * Rs / (Rs + Rf)
        rows.append((T_, Rs, V, round(V * 1023 / Vs)))
    res = Vs / 1023 * 1000
    setup()
    o = []
    o.append(ecu(4.4, 1.2, 2.4, 1.8, .8, 'ECU · ADC'))
    o.append(bx(4.8, 1.5, .9, .35, .35, ('#C9A27A', '#6B5236', '#9A7A55'), z0=.8))
    o.append(label(5.25, 1.5, 1.2, '1 kΩ', size=14, col='#E6CBA8', dy=-6))
    o.append(hcyl('x', 1.0, 5.4, 5.0, .55, .5, '#2A3037', '#4A535C'))
    o.append(glow(arrow3((4.2, 5.0, .55), (5.6, 5.0, .55), SKY, 4)))
    o.append(label(5.0, 5.0, 0, 'coolant', size=14, col=SKY, dy=30))
    o.append(B.box(3.3, 4.7, .6, .6, .25, *STEEL, z0=1.0))
    o.append(ucyl(3.6, 5.0, 1.25, .22, .9, '#B7C1CA', SIL))
    o.append(label(3.6, 5.0, 2.2, 'NTC', size=15, col=SIL, dy=-8))
    o.append(glow(line3([(3.6, 5.0, 2.1), (3.6, 3.6, 2.1), (4.4, 2.6, .7)], SKY, 3)))
    brd = board(o)
    tbl = ('<table><tr><th></th><th>R<sub>s</sub></th><th>V<sub>out</sub></th><th>count</th></tr>'
           + ''.join(f'<tr><td style="color:{c}">{T_} °C</td><td>{g(Rs / 1000)} kΩ</td><td>{f(V, 3)} V</td>'
                     f'<td style="color:{c};font-weight:700">{n}</td></tr>' for (T_, Rs, V, n), c in zip(rows, (SIL, SKY)))
           + '</table>')
    (t1, r1, v1, n1), (t2, r2, v2, n2) = rows
    return spec('au-elec-u3-L1', 'ECU Electronics<br>&amp; Sensor<br>Basics', 'How does an ECU read a sensor?',
                f'A {gold("DIVIDER")} makes the voltage,<br>the ADC turns it into {cyan("counts")}',
                'NTC divider, 10-bit ADC', tbl, brd,
                [chip('left', 300, 'c', 'R<sub>f</sub> = 1 kΩ to 5 V'), chip('left', 364, 'c', 'NTC to ground'),
                 chip('left', 470, 'c', f'{f(res, 2)} mV per count'), chip('right', 318, 'g', f'{n1} counts'),
                 chip('right', 500, 'g', f'{n2} counts', False)],
                f'V = 5 × R<sub>s</sub> ÷ (R<sub>s</sub> + 1000): {g(r1 / 1000)} kΩ → <b class="gl">{f(v1, 3)} V</b><br>'
                f'count = V × 1023 ÷ 5 → <b class="cl">{n1}</b> at {t1} °C, {n2} at {t2} °C', css=TABLE_CSS, size=62)


def u3_l2():
    """3.4 worked example: 60-2 crank wheel at 3000 rpm."""
    rpm, teeth = 3000, 60
    rev = 60 / rpm * 1000
    Tt = rev / teeth
    gap = 3 * Tt
    setup()
    o = []
    cx, cy, R, z = 3.8, 4.2, 2.3, .5
    o.append(ucyl(cx, cy, 0, .45, .5, '#2A3037', '#4A535C'))
    # disc and its 58 teeth (two missing)
    o.append(f'<polygon points="{pts(*hull(flat_circle(cx, cy, z, R) + flat_circle(cx, cy, z - .25, R)))}" fill="#1B1F24"/>')
    o.append(f'<polygon points="{pts(*flat_circle(cx, cy, z, R))}" fill="#5E6974"/>')
    o.append(f'<polygon points="{pts(*flat_circle(cx, cy, z, .55))}" fill="#3E454D"/>')
    gap_at = 1.25 * math.pi
    for k in range(teeth):
        a = gap_at + 2 * math.pi * k / teeth
        if k in (1, 2):
            continue
        w = 2 * math.pi / teeth * .27
        q = [P(cx + R * math.cos(a - w), cy + R * math.sin(a - w), z), P(cx + (R + .28) * math.cos(a - w), cy + (R + .28) * math.sin(a - w), z),
             P(cx + (R + .28) * math.cos(a + w), cy + (R + .28) * math.sin(a + w), z), P(cx + R * math.cos(a + w), cy + R * math.sin(a + w), z)]
        o.append(f'<polygon points="{pts(*q)}" fill="{SIL}"/>')
    # sensor pointing at the gap
    a = gap_at + 2 * math.pi * 1.5 / teeth
    sx, sy = cx + (R + 1.1) * math.cos(a), cy + (R + 1.1) * math.sin(a)
    o.append(ucyl(sx, sy, 0, .25, 1.0, '#2E6F96', '#9BDBFF'))
    o.append(glow(line3([(sx, sy, .9), (cx + (R + .35) * math.cos(a), cy + (R + .35) * math.sin(a), .55)], SKY, 3, '4 4')))
    o.append(label(sx, sy, 1.1, 'sensor', size=13, col=SKY, dy=-8))
    o.append(label(cx + R * .2, cy + R * .2, z, '60-2', size=16, col=SIL, dy=4))
    brd = board(o)
    # card: tooth signal with the gap
    x0, px = 30, 13.5
    p, x = [], x0
    seq = [1] * 14 + [0, 0] + [1] * 14
    for k, s in enumerate(seq):
        hi = 40 if s else 96
        p += [(x, 96), (x, hi), (x + px * .5, hi), (x + px * .5, 96), (x + px, 96)]
        x += px
    gx0 = x0 + 13 * px
    gx1 = x0 + 16 * px
    card = svg(poly(p, SIL, 2.5) + f'<path d="M{gx0:.1f} 112H{gx1:.1f}M{gx0:.1f} 106V118M{gx1:.1f} 106V118" stroke="{SKY}" stroke-width="2.2"/>'
               + tx((gx0 + gx1) / 2, 136, f'gap {f(gap, 1)} ms', 'pt', col=SKY)
               + f'<path d="M{x0 + 3 * px:.1f} 26H{x0 + 4 * px:.1f}" stroke="{SIL}" stroke-width="2"/>'
               + tx(x0 + 3.5 * px, 20, f'{f(Tt, 3)} ms', 'pt', col=SIL) + tx(x0 + 3.5 * px, 136, '1 tooth pitch'))
    return spec('au-elec-u3-L2', 'MAP, Air Flow<br>&amp; Crank<br>Sensors', 'How long is the 60-2 gap?',
                f'The gap spans {gold("3")} pitches,<br>so it lasts {cyan("3×")} a tooth',
                f'crank signal at {rpm} rpm', card, brd,
                [chip('left', 300, 'c', '60-2 wheel'), chip('left', 364, 'c', f'{rpm} rpm'),
                 chip('left', 470, 'c', f'{g(rev)} ms per rev'), chip('right', 318, 'g', f'gap {f(gap, 1)} ms'),
                 chip('right', 500, 'g', f'tooth {f(Tt, 3)} ms', False)],
                f'{g(rpm / 60)} rev/s → <b class="gl">{g(rev)} ms</b> per rev ÷ {teeth} = {f(Tt, 3)} ms<br>'
                f'gap = 3 pitches = 3 × {f(Tt, 3)} ms = <b class="cl">{f(gap, 1)} ms</b>')


def u3_l3():
    """3.5 worked example 2: ABS wheel-speed sensor, 48-tooth ring, r = 0.30 m, 72 km/h."""
    z, r, kmh = 48, .30, 72
    v = kmh / 3.6
    w = v / r
    n = w / (2 * math.pi)
    rpm = n * 60
    fr = z * n
    dt = 1 / fr * 1000
    slow = 3.6
    f_slow = fr * slow / kmh
    setup()
    o = []
    # wheel hub with its tone ring standing up (axis along y), sensor above the ring
    cx, cz = 4.0, 2.4
    o.append(hcyl('y', 2.0, 3.6, cx, cz, 1.9, '#0B0D10', '#1E2126'))
    o.append(hcyl('y', 3.6, 4.0, cx, cz, 1.45, '#3E454D', '#5E6974'))
    o.append(f'<polygon points="{pts(*ring("y", 4.0, cx, cz, 1.0))}" fill="#2A3037"/>')
    for k in range(z):
        a = 2 * math.pi * k / z
        wd = math.pi / z * .5
        q = [P(cx + 1.15 * math.cos(a - wd), 4.02, cz + 1.15 * math.sin(a - wd)), P(cx + 1.42 * math.cos(a - wd), 4.02, cz + 1.42 * math.sin(a - wd)),
             P(cx + 1.42 * math.cos(a + wd), 4.02, cz + 1.42 * math.sin(a + wd)), P(cx + 1.15 * math.cos(a + wd), 4.02, cz + 1.15 * math.sin(a + wd))]
        o.append(f'<polygon points="{pts(*q)}" fill="{SIL}"/>')
    o.append(f'<polygon points="{pts(*ring("y", 4.03, cx, cz, .35))}" fill="#8D98A3"/>')
    o.append(bx(cx - .2, 3.85, .4, .4, .9, SKYB, z0=cz + 1.6))
    o.append(glow(line3([(cx, 4.05, cz + 1.6), (cx, 4.05, cz + 1.45)], SKY, 3)))
    o.append(label(cx, 4.05, cz + 2.6, 'VR sensor', size=13, col=SKY, dy=-6))
    brd = board(o)

    def plot(x0, title, col, top, val_slow, lab_hi, lab_lo):
        X = lambda s: lin(s, 0, 80, x0 + 44, x0 + 214)
        Y = lambda q: lin(q, 0, top, 118, 32)
        hi = fr if title.startswith('pulse') else 1
        s = tx(x0 + 129, 18, title, 'pt', col=col) + axes(x0 + 44, x0 + 216)
        s += poly([(X(0), Y(0)), (X(80), Y(hi * 80 / kmh))], col, 3)
        s += dot(X(kmh), Y(hi), col) + tx(X(kmh) - 6, Y(hi) - 8, lab_hi, 'ax', 'end', col)
        s += dot(X(slow), Y(val_slow), SKY if col == SIL else SIL, 4) + tx(X(slow) + 10, Y(val_slow) - 14, lab_lo, 'ax', 'start')
        s += tx(X(0), 136, '0') + tx(X(kmh), 136, f'{kmh}') + tx(x0 + 216, 110, 'km/h', anchor='end')
        return s
    card = svg(plot(0, 'pulse rate', SIL, fr * 1.15, f_slow, f'{f(fr, 1)} Hz', f'{f(f_slow, 1)} Hz')
               + plot(240, 'VR voltage', SKY, 1.15, slow / kmh, 'full', f'1/{g(kmh / slow)}'))
    return spec('au-elec-u3-L3', 'Hall, Throttle<br>&amp; Temperature<br>Sensors', 'Does a VR sensor work at zero speed?',
                f'A VR signal fades to {gold("ZERO")};<br>{cyan("Hall")} sensors work at 0 km/h',
                'wheel-speed sensor output', card, brd,
                [chip('left', 300, 'c', f'{z}-tooth ring'), chip('left', 364, 'c', f'r = {f(r, 2)} m'),
                 chip('left', 470, 'c', f'{kmh} km/h'), chip('right', 318, 'g', f'{f(fr, 1)} Hz'),
                 chip('right', 500, 'g', f'{g(slow)} km/h: {f(f_slow, 1)} Hz', False)],
                f'{kmh} km/h → {f(v, 1)} ÷ {f(r, 2)} = {f(w, 2)} rad/s = <b class="gl">{f(rpm, 1)} rpm</b><br>'
                f'f = {z} × {f(n, 2)} = <b class="cl">{f(fr, 1)} Hz</b>, pulses {f(dt, 2)} ms apart')


def u3_l4():
    """3.7 worked example 2: zirconia cell by the Nernst equation, lean 1 % O2 and rich 1e-20 bar."""
    R, F, Tc = 8.314, 96485, 800
    Tk = Tc + 273.15
    k = R * Tk / (4 * F)
    lean = k * math.log(.21 / .01)
    rich = k * math.log(.21 / 1e-20)
    setup()
    o = []
    o.append(hcyl('x', .6, 6.6, 3.8, .85, .8, 'url(#dk)', '#2A3037', '#5E6974'))
    o.append(f'<polygon points="{pts(*ring("x", 6.6, 3.8, .85, .52))}" fill="#0B0D10"/>')
    o.append(glow(arrow3((5.2, 3.8, .85), (7.4, 3.8, .85), SKY, 5)))
    o.append(label(6.6, 3.8, 0, 'exhaust', size=14, col=SKY, dy=26))
    o.append(B.box(3.6, 3.45, .7, .7, .3, *STEEL, z0=1.6))
    o.append(ucyl(3.95, 3.8, 1.9, .28, 1.5, '#B7C1CA', SIL))
    o.append(ucyl(3.95, 3.8, 3.4, .15, .4, '#3E454D', '#5E6974'))
    o.append(label(3.95, 3.8, 3.9, 'zirconia λ sensor', size=15, dy=-10))
    brd = board(o)
    X = lambda l: lin(l, .9, 1.1, 50, 455)
    Y = lambda v: lin(v, 0, 1.1, 118, 24)
    curve = [(X(l), Y(lean + (rich - lean) / (1 + math.exp((l - 1) / .004)))) for l in [.9 + i * .002 for i in range(101)]]
    card = svg(axes(50, 458) + poly(curve, SIL, 3.5) + vdash(X(1), 118, 24, '#8D98A3') + tx(X(1), 136, 'λ = 1')
               + tx(X(.95), Y(rich) + 22, f'rich: {f(rich, 2)} V', 'pt', 'middle', SIL)
               + tx(X(1.05), Y(lean) - 12, f'lean: {f(lean, 3)} V', 'pt', 'middle', SKY)
               + tx(X(.92), 136, 'rich') + tx(X(1.08), 136, 'lean') + tx(44, 32, 'V', anchor='end'))
    return spec('au-elec-u3-L4', 'Lambda, Knock<br>&amp; Motion<br>Sensors', 'Does 0.9 V mean rich or lean?',
                f'0.9 V means {gold("RICH")};<br>lean reads about {cyan("0.1 V")}',
                'zirconia cell at 800 °C', card, brd,
                [chip('left', 300, 'c', f'{Tc} °C cell'), chip('left', 364, 'c', 'air: 0.21 bar O₂'),
                 chip('left', 470, 'c', 'lean: 0.01 bar O₂'), chip('right', 318, 'g', f'rich ≈ {f(rich, 2)} V'),
                 chip('right', 500, 'c', f'lean ≈ {f(lean, 3)} V', False)],
                f'RT ÷ 4F = 8.314 × {f(Tk, 2)} ÷ 4F = <b class="gl">{f(k, 5)} V</b><br>'
                f'lean: × ln 21 = <b class="cl">{f(lean, 3)} V</b>; rich: × {f(math.log(.21 / 1e-20), 2)} = {f(rich, 2)} V')


def u3_l5():
    """3.9 worked example: 1.8 degree stepper, 400 steps in 0.8 s."""
    beta, steps, t = 1.8, 400, .8
    ang = steps * beta
    revs = ang / 360
    rps = revs / t
    rpm = rps * 60
    setup()
    o = []
    o.append(bx(1.8, 2.6, 2.2, 2.2, 1.8, DARK))
    o.append(bx(1.9, 2.7, 2.0, 2.0, .06, MID, z0=1.8))
    o.append(ucyl(2.9, 3.7, 1.86, .3, .45, '#7B8692', SIL))
    o.append(f'<polygon points="{pts(*flat_circle(2.9, 3.7, 2.35, 1.3))}" fill="#3E454D" stroke="{SIL}" stroke-width="1.5"/>')
    for k in range(0, 200, 10):
        a = 2 * math.pi * k / 200
        o.append(line3([(2.9 + 1.12 * math.cos(a), 3.7 + 1.12 * math.sin(a), 2.35), (2.9 + 1.27 * math.cos(a), 3.7 + 1.27 * math.sin(a), 2.35)], SIL, 1.5))
    o.append(glow(line3([(2.9, 3.7, 2.37), (2.9 + 1.05, 3.7 - .35, 2.37)], SKY, 5)))
    o.append(label(2.9, 4.8, 0, 'stepper motor', size=15, dx=-10, dy=28))
    o.append(glow(line3([(4.0, 3.7, .5), (5.6, 3.7, .5)], SKY, 3)))
    o.append(label(4.8, 3.7, .5, f'{steps} pulses', size=15, col=SKY, dy=-12))
    o.append(ecu(5.6, 3.0, 1.6, 1.4, .7, 'ECU'))
    brd = board(o)
    # card: first five steps (staircase) and the 0.8 s run
    def stair(x0):
        X = lambda s_: lin(s_, 0, 5, x0 + 44, x0 + 210)
        Y = lambda a: lin(a, 0, 9, 118, 32)
        p = []
        for s_ in range(5):
            p += [(X(s_), Y(s_ * beta)), (X(s_ + 1), Y(s_ * beta)), (X(s_ + 1), Y((s_ + 1) * beta))]
        s = tx(x0 + 127, 18, 'first 5 steps', 'pt', col=SKY) + axes(x0 + 44, x0 + 214) + poly(p, SKY, 3)
        s += tx(x0 + 38, Y(9) + 4, '9°', anchor='end') + tx(x0 + 38, Y(beta) + 4, f'{beta}°', anchor='end', col=SKY)
        s += ''.join(tx(X(k), 136, str(k)) for k in range(0, 6))
        return s

    def run(x0):
        X = lambda q: lin(q, 0, t, x0 + 44, x0 + 214)
        Y = lambda a: lin(a, 0, ang, 118, 32)
        s = tx(x0 + 129, 18, f'{steps} steps', 'pt', col=SIL) + axes(x0 + 44, x0 + 216) + poly([(X(0), Y(0)), (X(t), Y(ang))], SIL, 3.5)
        s += dot(X(t), Y(ang), SIL) + tx(X(t) - 8, Y(ang) + 4, f'{g(ang)}°', 'pt', 'end', SIL)
        s += tx(X(0), 136, '0') + tx(X(t), 136, f'{g(t)} s')
        return s
    card = svg(stair(0) + run(240))
    return spec('au-elec-u3-L5', 'Actuators:<br>Electric &amp;<br>Fluid', 'Does microstepping add torque?',
                f'Microsteps add {gold("SMOOTHNESS")},<br>not holding {cyan("torque")}',
                f'a {beta}° stepper on the ECU', card, brd,
                [chip('left', 300, 'c', f'{beta}° per step'), chip('left', 364, 'c', f'{steps} steps'),
                 chip('left', 470, 'c', f'in {g(t)} s'), chip('right', 300, 'g', f'{g(ang)}° = {g(revs)} rev'),
                 chip('right', 500, 'g', f'{g(rpm)} rpm', False)],
                f'θ = {steps} × {beta}° = <b class="gl">{g(ang)}°</b> = {g(revs)} revolutions<br>'
                f'{g(revs)} rev ÷ {g(t)} s = {g(rps)} rev/s = <b class="cl">{g(rpm)} rpm</b>')


def u3_l6():
    """3.11 worked example: 12 V PM blower motor, Ra = 0.2 ohm, k phi = 0.02 V s/rad."""
    V, Ra, k, I = 12, .2, .02, 10
    w0 = V / k
    rpm0 = w0 * 60 / (2 * math.pi)
    E = V - I * Ra
    w = E / k
    rpm = w * 60 / (2 * math.pi)
    Tq = k * I
    Pout, Pin = Tq * w, V * I
    eff = Pout / Pin * 100
    Is = V / Ra
    Ts = k * Is
    setup()
    o = [bx(5.0, .5, 1.8, 1.2, .8, DARK), ucyl(5.4, .9, .8, .14, .15, '#7B8692', '#C9D1D8'), ucyl(6.4, .9, .8, .14, .15, '#7B8692', '#C9D1D8'),
         label(5.9, 1.7, .4, '12 V', size=15, dy=6)]
    o.append(line3([(5.4, .9, .95), (5.4, 1.9, .95), (4.2, 3.4, .4)], SIL, 4))
    cx0, cy0 = 3.2, 4.2
    o.append(ucyl(cx0, cy0, 0, 1.0, 1.4, 'url(#al)', '#C9D1D8'))
    o.append(ucyl(cx0, cy0, 1.4, .25, .3, '#5E6974', '#9AA6B2'))
    o.append(ucyl(cx0, cy0, 1.7, 1.55, 1.1, '#1B1F24', '#2A3037'))
    cx, cy = P(cx0, cy0, 1.7)
    for kk in range(24):
        a = math.pi * (kk + .5) / 24
        xx = cx + 1.2247 * 1.55 * U * math.cos(a)
        yy = cy + .7071 * 1.55 * U * math.sin(a)
        o.append(f'<line x1="{xx:.1f}" y1="{yy:.1f}" x2="{xx:.1f}" y2="{yy - 1.1 * U:.1f}" stroke="#8D98A3" stroke-width="2.2"/>')
    o.append(f'<ellipse cx="{cx:.1f}" cy="{cy - 1.1 * U:.1f}" rx="{1.2247 * 1.55 * U:.1f}" ry="{.7071 * 1.55 * U:.1f}" fill="none" stroke="{SIL}" stroke-width="3"/>')
    o.append(f'<ellipse cx="{cx:.1f}" cy="{cy - 1.1 * U:.1f}" rx="{1.2247 * .7 * U:.1f}" ry="{.7071 * .7 * U:.1f}" fill="#0B0D10"/>')
    o.append(glow(f'<path d="M{cx - 70:.1f},{cy - 1.1 * U - 34:.1f} A86,40 0 0 1 {cx + 70:.1f},{cy - 1.1 * U - 34:.1f}" fill="none" stroke="{SKY}" stroke-width="4"/>'))
    o.append(label(cx0, cy0 + 1.2, 0, 'blower motor', size=15, dy=26))
    brd = board(o)

    def plot(x0, title, col, top, y0v, y1v, mark, lab):
        X = lambda q: lin(q, 0, Ts, x0 + 44, x0 + 196)
        Y = lambda q: lin(q, 0, top, 118, 32)
        s = tx(x0 + 129, 18, title, 'pt', col=col) + axes(x0 + 44, x0 + 200) + poly([(X(0), Y(y0v)), (X(Ts), Y(y1v))], col, 3.5)
        s += vdash(X(Tq), 118, Y(mark), '#8D98A3') + dot(X(Tq), Y(mark), col) + tx(X(Tq) + 10, Y(mark) + (-10 if mark > top / 3 else -14), lab, 'pt', 'start', col)
        s += tx(X(0), 136, '0') + tx(X(Tq), 136, f'{f(Tq, 2)}') + tx(X(Ts), 136, f'{f(Ts, 2)}') + tx(x0 + 228, 110, 'N·m', anchor='end')
        return s
    card = svg(plot(0, 'speed, rad/s', SIL, w0 * 1.1, w0, 0, w, f'{g(w)}') + tx(40, 44, f'{g(w0)}', anchor='end')
               + plot(240, 'current, A', SKY, Is * 1.1, 0, Is, I, f'{I} A') + tx(280, 44, f'{g(Is)}', anchor='end'))
    return spec('au-elec-u3-L6', 'Vehicle Motors<br>&amp; Battery<br>Sensing', 'Why does a running motor draw less?',
                f'{gold("Back EMF")} opposes the supply,<br>so running current is {cyan("low")}',
                '12 V PM blower motor', card, brd,
                [chip('left', 300, 'c', f'R<sub>a</sub> = {Ra} Ω'), chip('left', 364, 'c', f'kΦ = {k} V·s/rad'),
                 chip('left', 470, 'g', f'stall: {g(Is)} A'), chip('right', 318, 'g', f'running: {I} A'),
                 chip('right', 500, 'c', f'{f(eff, 1)} % efficient', False)],
                f'running: E = {V} − {I} × {Ra} = <b class="gl">{g(E)} V</b> back EMF<br>'
                f'stall: E = 0, so I = {V} ÷ {Ra} = <b class="cl">{g(Is)} A</b>')


# ================================================================ unit 4
def u4_l1():
    """4.2 worked example 2: three-way catalyst at lambda 1 and at lambda 1.02."""
    eng = {'CO': 8.0, 'HC': 1.2, 'NOx': 1.0}
    conv = {'CO': .90, 'HC': .92, 'NOx': .95}
    lim = {'CO': 1.0, 'HC': .10, 'NOx': .06}
    tail = {p: eng[p] * (1 - conv[p]) for p in eng}
    pct = {p: tail[p] / lim[p] * 100 for p in eng}
    nox_lean = eng['NOx'] * (1 - .60)
    times = nox_lean / lim['NOx']
    setup()
    o = []
    o.append(hcyl('x', .8, 3.2, 3.4, .9, .4, '#1B1F24', '#2A3037'))
    o.append(B.box(3.2, 2.4, 2.8, 2.0, 1.8, '#C9D1D8', '#6E7984', '#9AA6B2'))
    for i in range(1, 5):
        o.append(line3([(6.0, 2.4 + i * .4, 0), (6.0, 2.4 + i * .4, 1.8)], '#6E7984', 1.4))
    for i in range(1, 5):
        o.append(line3([(6.0, 2.4, i * .36), (6.0, 4.4, i * .36)], '#6E7984', 1.4))
    o.append(label(4.6, 3.4, 1.8, 'catalyst', size=17, col='#1A2028', dy=5, halo=False))
    o.append(hcyl('x', 6.0, 7.5, 3.4, .9, .4, '#1B1F24', '#2A3037'))
    o.append(glow(arrow3((6.3, 4.9, .9), (7.8, 4.9, .9), SKY, 5)))
    brd = board(o)
    X1 = {'CO': 70, 'HC': 120, 'NOx': 170}
    Y = lambda p_: lin(p_, 0, 120, 118, 30)
    s = tx(120, 18, 'λ = 1: % of BS VI', 'pt', col=SIL) + f'<line x1="50" y1="118" x2="210" y2="118" stroke="{AXC}" stroke-width="1.5"/>'
    for p_ in eng:
        s += f'<rect x="{X1[p_] - 18}" y="{Y(pct[p_]):.1f}" width="36" height="{118 - Y(pct[p_]):.1f}" rx="5" fill="{SIL}" opacity=".85"/>'
        s += tx(X1[p_], Y(pct[p_]) + 18, f'{g(round(pct[p_]))}', 'ax', col='#10151A') + tx(X1[p_], 136, p_)
    s += hdash(Y(100), 50, 210, SKY) + tx(214, Y(100) + 4, '100', 'ax', 'start', SKY)
    Y2 = lambda v: lin(v, 0, .45, 118, 30)
    s += tx(360, 18, 'NOx, g/km', 'pt', col=SKY) + f'<line x1="270" y1="118" x2="460" y2="118" stroke="{AXC}" stroke-width="1.5"/>'
    for x, v, lab in ((320, tail['NOx'], 'λ = 1'), (405, nox_lean, 'λ = 1.02')):
        s += f'<rect x="{x - 24}" y="{Y2(v):.1f}" width="48" height="{118 - Y2(v):.1f}" rx="5" fill="{SKY}" opacity=".9"/>'
        s += tx(x, Y2(v) - 6, f'{f(v, 2)}', 'ax', col=SKY) + tx(x, 136, lab)
    s += hdash(Y2(lim['NOx']), 270, 460, '#FF9A8A') + tx(272, Y2(lim['NOx']) - 22, f'limit {lim["NOx"]}', 'ax', 'start', '#FF9A8A')
    card = svg(s)
    return spec('au-elec-u4-L1', 'Emission Norms<br>&amp; Engine<br>Fuelling', 'What does λ = 1 really mean?',
                f'λ = 1 is the {gold("14.7 : 1")} mix;<br>2 % lean and {cyan("NOx")} fails',
                'the catalyst needs λ = 1', card, brd,
                [chip('left', 300, 'c', f'NOx in: {eng["NOx"]} g/km'), chip('left', 364, 'c', 'λ = 1: 95 % converted'),
                 chip('left', 470, 'c', 'λ = 1.02: 60 %'), chip('right', 318, 'g', f'{g(round(tail["NOx"], 3))} g/km: pass'),
                 chip('right', 500, 'g', f'{f(nox_lean, 2)} g/km: {f(times, 1)}× limit', False)],
                f'λ = 1: NOx {eng["NOx"]} × 0.05 = <b class="gl">{g(round(tail["NOx"], 3))} g/km</b>, under 0.06<br>'
                f'λ = 1.02: {eng["NOx"]} × 0.40 = <b class="cl">{f(nox_lean, 2)} g/km</b> = {f(times, 1)}× limit', size=66)


def u4_l2():
    """4.4 worked example: interpolating the injection map at 2000 rpm, 46 kPa."""
    rpm, p0, t0, p1, t1, p = 2000, 40, 4.0, 50, 6.0, 46
    tp = t0 + (t1 - t0) * (p - p0) / (p1 - p0)
    cyc = 2 * 60 / rpm * 1000
    frac = tp / cyc * 100
    setup()
    o = []
    for x, y, v, c, lab in ((3.0, 5.1, t0, STEEL, f'{p0} kPa'), (4.15, 4.05, tp, SKYB, f'{p} kPa'), (5.3, 3.0, t1, STEEL, f'{p1} kPa')):
        hgt = v * .55
        o.append(bx(x, y, .9, .9, hgt, c))
        o.append(label(x + .45, y + .45, hgt, f'{f(v, 1)} ms', size=17, col=SKY if c == SKYB else SIL, dy=-12))
        o.append(label(x + .45, y + .9, 0, lab, size=14, col='#C9D3DB', dy=22))
    brd = board(o)
    X = lambda q: lin(q, 35, 55, 60, 260)
    Y = lambda q: lin(q, 3, 7, 118, 30)
    s = tx(160, 18, 'pulse width', 'pt', col=SIL) + axes(60, 262) + poly([(X(p0), Y(t0)), (X(p1), Y(t1))], SIL, 3)
    s += dot(X(p0), Y(t0), SIL) + dot(X(p1), Y(t1), SIL) + vdash(X(p), 118, Y(tp), SKY) + hdash(Y(tp), 60, X(p), SKY) + dot(X(p), Y(tp), SKY, 6)
    s += tx(X(p) - 8, Y(tp) - 10, f'{g(tp)} ms', 'pt', 'end', SKY) + ''.join(tx(X(q), 136, str(q)) for q in (p0, p, p1)) + tx(262, 110, 'kPa', anchor='end')
    W = 180
    s += tx(380, 18, f'one cycle: {g(cyc)} ms', 'pt', col=SIL)
    s += f'<rect x="290" y="56" width="{W}" height="34" rx="6" fill="none" stroke="{AXC}" stroke-width="1.5"/>'
    s += f'<rect x="290" y="56" width="{W * tp / cyc:.1f}" height="34" rx="6" fill="{SKY}"/>'
    s += tx(290 + W * tp / cyc + 8, 79, f'{f(frac, 1)} % open', 'pt', 'start', SKY) + tx(290, 112, '0', anchor='start') + tx(470, 112, f'{g(cyc)} ms', anchor='end')
    card = svg(s)
    return spec('au-elec-u4-L2', 'Engine Numbers<br>&amp; the ECU', 'Is an ECU map closed loop?',
                f'A map alone is {gold("OPEN")} loop;<br>the λ {cyan("sensor")} closes it',
                'reading the injection map', card, brd,
                [chip('left', 300, 'c', f'{rpm} rpm column'), chip('left', 364, 'c', f'{p0} kPa: {f(t0, 1)} ms'),
                 chip('left', 470, 'c', f'{p1} kPa: {f(t1, 1)} ms'), chip('right', 300, 'g', f'{p} kPa → {g(tp)} ms'),
                 chip('right', 500, 'g', f'{f(frac, 1)} % of {g(cyc)} ms', False)],
                f'{f(t0, 1)} + ({f(t1, 1)} − {f(t0, 1)}) × ({p} − {p0}) ÷ {p1 - p0} = <b class="gl">{g(tp)} ms</b><br>'
                f'cycle = 2 × 60 ÷ {rpm} = {g(cyc)} ms → <b class="cl">{f(frac, 1)} %</b> open')


def u4_l3():
    """4.6 worked example: 3.0 ms dwell, spark at 25 degrees BTDC, at 3000 and 6000 rpm."""
    dwell, adv, spark = 3.0, 25, 1.5
    dpm = {n: .006 * n for n in (3000, 6000, 8000)}
    ang = {n: dwell * dpm[n] for n in (3000, 6000)}
    start = {n: adv + ang[n] for n in ang}
    gap6, gap8 = 180 / dpm[6000], 180 / dpm[8000]
    setup()
    o = []
    cx, cy, R, z = 4.0, 4.0, 2.4, .35
    o.append(f'<polygon points="{pts(*hull(flat_circle(cx, cy, z, R) + flat_circle(cx, cy, 0, R)))}" fill="#1B1F24"/>')
    o.append(f'<polygon points="{pts(*flat_circle(cx, cy, z, R))}" fill="#3E454D"/>')
    o.append(f'<polygon points="{pts(*flat_circle(cx, cy, z, .45))}" fill="#7B8692"/>')
    tdc = -math.pi * .75      # TDC mark direction on the disc (towards the back)

    def arc(r, a0, a1, col, w):
        n = 40
        return [(cx + r * math.cos(tdc + math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(tdc + math.radians(a0 + (a1 - a0) * i / n)), z + .01) for i in range(n + 1)]
    # angles counted before TDC run in the negative sense (the crank turns forward towards TDC)
    o.append(glow(line3(arc(2.0, -start[6000], -adv, SKY, 9), SKY, 9)))
    o.append(line3(arc(1.4, -start[3000], -adv, SIL, 8), SIL, 8))
    o.append(line3([(cx + .5 * math.cos(tdc), cy + .5 * math.sin(tdc), z + .01), (cx + 2.5 * math.cos(tdc), cy + 2.5 * math.sin(tdc), z + .01)], '#FFFFFF', 3))
    o.append(label(cx + 2.7 * math.cos(tdc), cy + 2.7 * math.sin(tdc), z, 'TDC', size=14, dy=-6))
    sa = tdc - math.radians(adv)
    o.append(glow(line3([(cx + .5 * math.cos(sa), cy + .5 * math.sin(sa), z + .02), (cx + 2.4 * math.cos(sa), cy + 2.4 * math.sin(sa), z + .02)], '#FFD27A', 3)))
    e6 = tdc - math.radians(start[6000] - 15)
    o.append(label(cx + 2.0 * math.cos(e6), cy + 2.0 * math.sin(e6), z, f'{g(ang[6000])}°', size=17, col=SKY, dy=-8))
    e3 = tdc - math.radians(start[3000] - 12)
    o.append(label(cx + 1.4 * math.cos(e3), cy + 1.4 * math.sin(e3), z, f'{g(ang[3000])}°', size=15, col=SIL, dy=-6))
    brd = board(o)
    X = lambda n: lin(n, 0, 7000, 50, 220)
    Y = lambda a: lin(a, 0, 130, 118, 30)
    s = tx(140, 18, 'dwell angle', 'pt', col=SIL) + axes(50, 222) + poly([(X(0), Y(0)), (X(7000), Y(dwell * .006 * 7000))], SIL, 3)
    s += dot(X(3000), Y(ang[3000]), SIL) + tx(X(3000) - 6, Y(ang[3000]) - 8, f'{g(ang[3000])}°', 'pt', 'end', SIL)
    s += dot(X(6000), Y(ang[6000]), SKY) + tx(X(6000) - 8, Y(ang[6000]) - 6, f'{g(ang[6000])}°', 'pt', 'end', SKY)
    s += ''.join(tx(X(n), 136, g(n)) for n in (3000, 6000)) + tx(222, 110, 'rpm', anchor='end')
    # time budget between sparks
    Xt = lambda q: lin(q, 0, 6.6, 280, 462)
    s += tx(370, 18, 'gap between sparks', 'pt', col=SKY)
    for y, gap, lab in ((44, gap6, '6000'), (90, gap8, '8000')):
        s += tx(276, y + 18, lab, 'ax', 'end')
        s += f'<rect x="280" y="{y}" width="{Xt(gap) - 280:.1f}" height="26" rx="5" fill="none" stroke="{SIL}" stroke-width="2"/>'
        s += f'<rect x="280" y="{y + 5}" width="{Xt(dwell) - 280:.1f}" height="16" rx="3" fill="{SKY}"/>'
        s += f'<rect x="{Xt(dwell):.1f}" y="{y + 5}" width="{Xt(dwell + spark) - Xt(dwell):.1f}" height="16" rx="3" fill="#FFD27A"/>'
        s += tx(Xt(max(gap, dwell + spark)) + 5, y + 18, f'{g(gap)} ms', 'ax', 'start', SIL)
    s += tx(370, 136, f'dwell {f(dwell, 1)} + spark {f(spark, 1)} ms', 'ax')
    card = svg(s)
    return spec('au-elec-u4-L3', 'Fuel Injection<br>&amp; Spark<br>Timing', 'Why does dwell angle grow with speed?',
                f'The same {gold("3.0 ms")} of dwell<br>spans more {cyan("degrees")} at speed',
                f'{f(dwell, 1)} ms dwell at two speeds', card, brd,
                [chip('left', 300, 'c', f'dwell {f(dwell, 1)} ms'), chip('left', 364, 'c', f'spark {adv}° BTDC'),
                 chip('left', 470, 'g', f'3000 rpm: {g(ang[3000])}°'), chip('right', 300, 'g', f'6000 rpm: {g(ang[6000])}°'),
                 chip('right', 500, 'c', f'start {g(start[6000])}° BTDC', False)],
                f'°/ms = 0.006 × rpm: 3000 → {g(dpm[3000])}, 6000 → <b class="gl">{g(dpm[6000])}</b><br>'
                f'{f(dwell, 1)} ms × {g(dpm[6000])} = <b class="cl">{g(ang[6000])}°</b>, charging from {g(start[6000])}° BTDC')


# ================================================================ unit 5
def u5_l1():
    """5.2 worked example: ACC, host 25 m/s, lead 20 m/s, 60 m, 2.0 s time gap."""
    vh, vl, d, tg = 25, 20, 60, 2.0
    gap_now = d / vh
    dt = tg * vh
    err = d - dt
    close = vh - vl
    a = close ** 2 / (2 * err)
    tb = close / a
    setup()
    o = []
    # a lane strip along x with dashes, the host car behind and the lead car ahead
    o.append(bx(0, 3.0, 8, 2.2, .04, ('#262C32', '#14161A', '#1E2126')))
    for k in range(5):
        o.append(line3([(.3 + k * 1.6, 4.1, .05), (1.1 + k * 1.6, 4.1, .05)], '#8D98A3', 2))
    beam = [P(2.9, 4.1, .6), P(6.6, 3.1, .6), P(6.6, 5.1, .6)]
    o.append(glow(f'<polygon points="{pts(*beam)}" fill="{SKY}" opacity=".2"/>'))
    o.append(car(.4, 3.5, 'x', STEEL))
    o.append(car(5.4, 3.5, 'x', SKYB))
    o.append(label(1.6, 3.5, 1.3, f'host {vh} m/s', size=14, dy=-14))
    o.append(label(6.6, 3.5, 1.3, f'lead {vl} m/s', size=14, col=SKY, dy=-14))
    o.append(line3([(2.8, 5.6, .05), (5.4, 5.6, .05)], SIL, 2))
    o.append(line3([(2.8, 5.45, .05), (2.8, 5.75, .05)], SIL, 2))
    o.append(line3([(5.4, 5.45, .05), (5.4, 5.75, .05)], SIL, 2))
    o.append(label(4.1, 5.6, 0, f'{d} m', size=15, col=SIL, dy=22))
    brd = board(o)
    ts = [tb * i / 40 for i in range(41)]
    gap = [d - (close * t - .5 * a * t * t) for t in ts]
    sp = [vh - a * t for t in ts]

    def plot(x0, title, col, ys, lo, hi, l0, l1):
        X = lambda t: lin(t, 0, tb, x0 + 44, x0 + 210)
        Y = lambda q: lin(q, lo, hi, 118, 32)
        s = tx(x0 + 127, 18, title, 'pt', col=col) + axes(x0 + 44, x0 + 214) + poly([(X(t), Y(q)) for t, q in zip(ts, ys)], col, 3.5)
        s += tx(x0 + 38, Y(ys[0]) + 5, l0, anchor='end') + dot(X(tb), Y(ys[-1]), col) + tx(X(tb) - 10, Y(ys[-1]) + 2, l1, 'pt', 'end', col)
        s += tx(X(0), 136, '0') + tx(X(tb), 136, f'{g(tb)} s')
        return s
    card = svg(plot(0, 'gap, m', SIL, gap, 45, 62, f'{d}', f'{g(dt)} m') + plot(240, 'host speed, m/s', SKY, sp, 19, 26, f'{vh}', f'{vl} m/s'))
    return spec('au-elec-u5-L1', 'Transmission,<br>Cruise &amp; Steering<br>Control', 'How does ACC keep a 2 s gap?',
                f'Gap = {gold("time")} × own speed:<br>{f(tg, 1)} s at {vh} m/s is {cyan(f"{g(dt)} m")}',
                'closing on a slower car', card, brd,
                [chip('left', 300, 'c', f'host {vh} m/s'), chip('left', 364, 'c', f'lead {vl} m/s'),
                 chip('left', 470, 'c', f'{d} m = {g(gap_now)} s now'), chip('right', 318, 'g', f'target {g(dt)} m'),
                 chip('right', 500, 'g', f'brake {g(a)} m/s² for {g(tb)} s', False)],
                f'target = {f(tg, 1)} s × {vh} m/s = <b class="gl">{g(dt)} m</b>; closing {close} m/s<br>'
                f'a = {close}² ÷ (2 × {g(err)} m) = <b class="cl">{g(a)} m/s²</b>, for {g(tb)} s', size=62)


def u5_l2():
    """5.5 worked example: ESP yaw-rate check in a left turn."""
    L, track, K, v, delta, rm = 2.6, 1.5, .0025, 20, .05, .200
    rdes = v * delta / (L + K * v * v)
    e = rdes - rm
    F = 2000
    Mz = F * track / 2
    lim = .9 * 9.81 / v
    setup()
    o = []
    cx0, cy0, Lc, Wc = 3.2, 1.4, 3.4, 1.7
    path = [(cx0 + Wc / 2 + 3.0 * (1 - math.cos(t)), cy0 + Lc + 3.0 * math.sin(t), .02) for t in [i * .045 for i in range(24)]]
    o.append(line3(path, '#8D98A3', 3, '8 6'))
    o.append(label(path[-1][0], path[-1][1], 0, 'left turn', size=14, col='#C9D3DB', dy=22))
    o.append(car(cx0, cy0, 'y', STEEL, L=Lc, W=Wc))
    xw, yw = cx0 + Wc, cy0 + .5
    o.append(glow(hcyl('x', xw - .16, xw + .1, yw, .3, .34, SKY, '#BFE8FF')))
    o.append(glow(arrow3((xw + .3, yw, .3), (xw + .3, yw - 1.6, .3), SKY, 6)))
    o.append(label(xw + .3, yw - 1.6, .3, f'{g(F)} N', size=16, col=SKY, dx=30, dy=6))
    o.append(label(xw, yw, 1.0, 'left rear', size=15, col=SKY, dx=36, dy=-8))
    brd = board(o)
    Y = lambda q: lin(q, 0, .32, 118, 32)
    s = tx(120, 18, 'yaw rate, rad/s', 'pt', col=SIL) + f'<line x1="30" y1="118" x2="220" y2="118" stroke="{AXC}" stroke-width="1.5"/>'
    for x, val, lab, col in ((80, rdes, 'desired', SIL), (170, rm, 'measured', SKY)):
        s += f'<rect x="{x - 30}" y="{Y(val):.1f}" width="60" height="{118 - Y(val):.1f}" rx="6" fill="{col}" opacity=".9"/>'
        s += tx(x, Y(val) - 6, f'{f(val, 3)}', 'pt', col=col) + tx(x, 136, lab)
    # top view: car with the braked wheel
    cxp, cyp = 350, 78
    s += f'<rect x="{cxp - 26}" y="{cyp - 50}" width="52" height="100" rx="14" fill="#3E454D" stroke="{SIL}" stroke-width="2"/>'
    for dx_, dy_ in ((-31, -32), (31, -32), (-31, 32), (31, 32)):
        fill = SKY if (dx_ < 0 and dy_ > 0) else '#9AA6B2'
        s += f'<rect x="{cxp + dx_ - 6}" y="{cyp + dy_ - 12}" width="12" height="24" rx="3" fill="{fill}"/>'
    s += tx(cxp - 46, cyp + 40, 'LR', 'pt', 'end', SKY) + tx(cxp, cyp - 58, 'front', 'ax')
    s += T.arrow(cxp - 70, cyp + 30, cxp - 70, cyp + 62, SKY, 3) + tx(cxp + 40, cyp - 6, f'{g(F)} N', 'pt', 'start', SKY) + tx(cxp + 40, cyp + 18, f'{g(Mz)} N·m', 'pt', 'start', SIL)
    card = svg(s)
    return spec('au-elec-u5-L2', 'ABS, ESP &amp;<br>Active<br>Suspension', 'Understeer: which wheel gets braked?',
                f'Understeer: brake the {gold("INNER")}<br>{cyan("rear")} wheel',
                'ESP in a left turn', card, brd,
                [chip('left', 300, 'c', f'{v} m/s, δ = {delta} rad'), chip('left', 364, 'g', f'r<sub>des</sub> = {f(rdes, 3)} rad/s'),
                 chip('left', 470, 'c', f'measured {f(rm, 3)}'), chip('right', 300, 'g', 'brake left rear'),
                 chip('right', 500, 'c', f'error +{f(e, 3)} rad/s', False)],
                f'r<sub>des</sub> = vδ ÷ (L + Kv²) = {f(v * delta, 1)} ÷ {f(L + K * v * v, 1)} = <b class="gl">{f(rdes, 3)} rad/s</b><br>'
                f'measured {f(rm, 3)}: understeer → brake <b class="cl">left rear</b>')


def u5_l3():
    """5.7 worked example: 50 km/h barrier crash, 0.6 m crush."""
    kmh, s_ = 50, .6
    v = kmh / 3.6
    a = v * v / (2 * s_)
    gs = a / 9.81
    t = v / a * 1000
    setup()
    o = []
    o.append(bx(2.6, .5, 4.2, .9, 2.2, ('#C9D1D8', '#6E7984', '#9AA6B2')))
    for k in range(6):
        o.append(line3([(3.0 + k * .7, 1.4, 2.2), (3.5 + k * .7, 1.4, 0)], '#2A3037', 6))
    o.append(label(4.7, .9, 2.2, 'barrier', size=16, col='#1A2028', dy=5, halo=False))
    o.append(car(3.7, 1.9, 'y', STEEL, L=3.2, W=1.5))
    zz = [(3.7 + .25 * k, 1.9 + .14 * (k % 2), .5) for k in range(7)]
    o.append(line3(zz, '#1A2028', 3))
    bx_, by_ = P(4.45, 2.9, 1.0)
    o.append(glow(f'<ellipse cx="{bx_:.1f}" cy="{by_:.1f}" rx="26" ry="19" fill="#9BDBFF" opacity=".85"/>'))
    o.append(label(4.45, 2.9, 1.4, 'airbag', size=15, col=SKY, dx=-44, dy=-12))
    o.append(line3([(5.5, 1.4, .02), (5.5, 2.0, .02)], SIL, 3))
    o.append(label(5.5, 1.7, 0, f'{g(s_)} m crush', size=14, col=SIL, dx=48, dy=8))
    o.append(arrow3((4.45, 6.8, .4), (4.45, 5.5, .4), '#8D98A3', 5))
    brd = board(o)
    X = lambda q: lin(q, 0, 100, 50, 455)
    Y = lambda q: lin(q, 0, 15, 118, 32)
    s = axes(50, 458) + poly([(X(0), Y(v)), (X(t), Y(0))], SIL, 3.5)
    for ms, lab, col in ((10, 'sense', '#AFC0CE'), (25, 'fire', SKY), (50, 'full', SKY)):
        s += vdash(X(ms), 118, 30, col) + tx(X(ms) + 4, 40 if ms != 25 else 54, lab, 'ax', 'start', col)
        s += tx(X(ms), 136, f'{ms}')
    s += dot(X(t), Y(0), SIL) + tx(X(t), 136, f'{g(round(t))} ms', col=SIL) + tx(44, Y(v) + 4, f'{f(v, 1)}', anchor='end')
    s += tx(X(70), Y(v * .3) - 6, 'car speed, m/s', 'ax', 'start', SIL)
    card = svg(s)
    return spec('au-elec-u5-L3', 'Airbags, Driver<br>Assistance &amp;<br>Speed Control', 'Does an airbag replace the belt?',
                f'The {gold("BELT")} does the stopping;<br>the bag is a {cyan("supplement")}',
                f'a {kmh} km/h barrier crash', card, brd,
                [chip('left', 300, 'c', f'{kmh} km/h = {f(v, 1)} m/s'), chip('left', 364, 'c', f'crush {g(s_)} m'),
                 chip('left', 470, 'c', 'bag full at 50 ms'), chip('right', 318, 'g', f'{f(gs, 1)} g'),
                 chip('right', 500, 'g', f'stops in {g(round(t))} ms', False)],
                f'a = v² ÷ 2s = {g(round(v * v))} ÷ {g(2 * s_)} = <b class="gl">{g(round(a))} m/s²</b> = {f(gs, 1)} g<br>'
                f't = {f(v, 1)} ÷ {g(round(a))} = <b class="cl">{g(round(t))} ms</b>; bag full by about 50 ms')


# ================================================================ unit 6
def u6_l1():
    """6.1 worked example: 12 ECUs, point to point or one bus."""
    n = 12
    links = n * (n - 1) // 2
    drivers = 2 * links
    save = drivers - n
    setup()
    o = []
    # twisted pair along x with six ECUs on each side
    xs = [.9 + k * 1.15 for k in range(6)]
    for x in xs:
        o.append(bx(x - .4, 1.9, .8, .7, .45, MID))
        o.append(line3([(x, 2.6, .2), (x, 3.85, .05)], SIL, 2))
    o.append(glow(line3([(.3, 3.85, .05), (7.7, 3.85, .05)], SKY, 4)))
    o.append(glow(line3([(.3, 4.15, .05), (7.7, 4.15, .05)], SIL, 4)))
    for x in xs:
        o.append(line3([(x + .3, 4.15, .05), (x + .3, 5.4, .2)], SIL, 2))
        o.append(bx(x - .1, 5.4, .8, .7, .45, MID))
    o.append(label(7.7, 4.0, .05, 'one bus', size=14, col=SKY, dx=-10, dy=24))
    brd = board(o)
    cx, cy, R = 120, 76, 50
    nodes = [(cx + R * math.cos(2 * math.pi * k / n), cy + R * math.sin(2 * math.pi * k / n)) for k in range(n)]
    s = tx(120, 18, f'point to point: {links} links', 'pt', col=SIL)
    for i in range(n):
        for j in range(i + 1, n):
            s += f'<line x1="{nodes[i][0]:.1f}" y1="{nodes[i][1]:.1f}" x2="{nodes[j][0]:.1f}" y2="{nodes[j][1]:.1f}" stroke="{SIL}" stroke-width="1" opacity=".55"/>'
    s += ''.join(dot(x, y, SIL, 4.5) for x, y in nodes)
    s += tx(355, 18, 'one bus: 12 transceivers', 'pt', col=SKY)
    s += f'<line x1="255" y1="80" x2="460" y2="80" stroke="{SKY}" stroke-width="3"/><line x1="255" y1="86" x2="460" y2="86" stroke="{SKY}" stroke-width="3" opacity=".6"/>'
    for k in range(n):
        x = 265 + k * 17
        y = 50 if k % 2 == 0 else 116
        s += f'<line x1="{x}" y1="{y}" x2="{x}" y2="{83}" stroke="{SKY}" stroke-width="1.5"/>' + dot(x, y, SKY, 4.5)
    card = svg(s)
    return spec('au-elec-u6-L1', 'Vehicle<br>Networks &amp; the<br>OSI Model', 'How do 12 ECUs share one bus?',
                f'One {gold("twisted pair")} for all,<br>one {cyan("transceiver")} per ECU',
                f'{n} ECUs: mesh or one bus', card, brd,
                [chip('left', 300, 'c', f'{n} ECUs'), chip('left', 364, 'c', f'{links} links'),
                 chip('left', 470, 'c', f'{drivers} line drivers'), chip('right', 300, 'g', f'{n} transceivers'),
                 chip('right', 500, 'g', f'{save} fewer', False)],
                f'point to point: {n} × {n - 1} ÷ 2 = <b class="gl">{links} links</b>, {drivers} drivers<br>'
                f'one bus: <b class="cl">{n} transceivers</b>, {save} fewer')


def u6_l2():
    """6.3 worked example: CAN arbitration, 0x123 against 0x121."""
    a, b = 0x123, 0x121
    ba, bb = format(a, '011b'), format(b, '011b')
    first = next(i for i in range(11) if ba[i] != bb[i])
    bitno = 10 - first
    winner = 'B' if int(bb[first]) < int(ba[first]) else 'A'
    setup()
    o = []
    o.append(glow(line3([(.3, 3.6, .05), (7.7, 3.6, .05)], SKY, 4)))
    o.append(line3([(.3, 3.9, .05), (7.7, 3.9, .05)], SIL, 4))
    o.append(line3([(3.0, 2.4, .2), (3.0, 3.6, .05)], '#8D98A3', 3))
    o.append(bx(2.2, 1.0, 1.6, 1.4, .9, DARK))
    o.append(label(3.0, 1.7, .9, f'A · 0x{a:03X}', size=16, col='#C9D3DB', dy=-14))
    o.append(line3([(5.0, 3.9, .05), (5.0, 4.8, .2)], SKY, 3))
    o.append(bx(4.2, 4.8, 1.6, 1.4, .9, SKYB))
    o.append(label(5.0, 6.2, 0, f'B · 0x{b:03X} wins', size=16, col=SKY, dy=26))
    brd = board(o)
    cw = 30
    x0 = 92
    s = ''.join(tx(x0 + i * cw + cw / 2, 18, str(10 - i), 'ax') for i in range(11))
    bus = ''.join(str(min(int(p), int(q))) for p, q in zip(ba, bb))
    for r_, (name, bits, col) in enumerate((('A', ba, '#AFC0CE'), ('B', bb, SKY), ('bus', bus, SIL))):
        y = 28 + r_ * 34
        s += tx(x0 - 8, y + 22, name, 'pt', 'end', col)
        for i, bit in enumerate(bits):
            hl = i == first
            fill = 'rgba(111,203,255,.22)' if hl else 'rgba(255,255,255,.04)'
            s += f'<rect x="{x0 + i * cw + 1}" y="{y}" width="{cw - 2}" height="30" rx="4" fill="{fill}" stroke="{SKY if hl else "#3A4A58"}" stroke-width="{2 if hl else 1}"/>'
            if name == 'A' and i > first:
                s += tx(x0 + i * cw + cw / 2, y + 21, '·', 'pt', col='#5E6974')
            else:
                s += tx(x0 + i * cw + cw / 2, y + 21, bit, 'pt', col=col)
    card = svg(s)
    return spec('au-elec-u6-L2', 'CAN, LIN,<br>FlexRay &amp;<br>Ethernet', 'Can a CAN FD frame carry 9 bytes?',
                f'No: DLC {gold("9")} is a code<br>for {cyan("12")} bytes in CAN FD',
                f'ID 0x{a:03X} vs ID 0x{b:03X}', card, brd,
                [chip('left', 300, 'c', f'A: 0x{a:03X} = {a}'), chip('left', 364, 'c', f'B: 0x{b:03X} = {b}'),
                 chip('left', 470, 'c', f'bit {bitno}: A 1, B 0'), chip('right', 318, 'g', f'{winner} wins'),
                 chip('right', 500, 'g', 'dominant 0 wins', False)],
                f'bits 10 to {bitno + 1} are equal; at bit {bitno} A sends 1, B sends <b class="cl">0</b><br>'
                f'dominant 0 wins: <b class="gl">B (0x{b:03X})</b> sends, A retries')


def u6_l3():
    """6.6 worked example 2: service 03 reply 43 02 03 01 01 33 and its freeze frame."""
    reply = [0x43, 0x02, 0x03, 0x01, 0x01, 0x33]

    def dtc(hi, lo):
        letter = 'PCBU'[hi >> 6]
        return f'{letter}{(hi >> 4) & 3}{hi & 15:X}{lo >> 4:X}{lo & 15:X}'
    c1, c2 = dtc(reply[2], reply[3]), dtc(reply[4], reply[5])
    cool = 0x7B - 40
    spd = 0x3E
    load = 0x59 * 100 / 255
    setup()
    o = [ecu(4.6, .7, 2.4, 1.6, .8, 'engine ECU')]
    o.append(bx(4.2, 3.2, 1.0, .55, .45, ('#5E6974', '#2A3037', '#3E454D')))
    o.append(label(4.2, 3.75, .2, 'OBD port', size=14, col='#C9D3DB', dx=-58, dy=-20))
    o.append(line3([(5.4, 2.3, .4), (5.4, 3.0, .4), (5.0, 3.3, .4)], SIL, 3))
    o.append(glow(line3([(4.4, 3.75, .3), (4.4, 4.6, .3)], SKY, 4)))
    o.append(bx(2.8, 4.6, 2.6, 2.0, .4, DARK))
    o.append(B.box(3.0, 4.8, 2.2, 1.4, .02, '#0E1A24', '#0E1A24', '#0E1A24', z0=.4))
    o.append(label(4.1, 5.5, .42, c1, size=20, col=SKY, dy=-2))
    o.append(label(4.1, 5.5, .42, c2, size=15, col=SIL, dy=18))
    o.append(label(4.1, 6.6, 0, 'scan tool', size=14, dy=26))
    brd = board(o)
    tbl = ('<table><tr><th>bytes</th><th>decoded</th></tr>'
           f'<tr><td style="color:{SKY}">03 01</td><td style="color:{SKY};font-weight:700">{c1} misfire, cyl 1</td></tr>'
           f'<tr><td>01 33</td><td>{c2} slow O₂ sensor</td></tr>'
           f'<tr><td>7B · 3E</td><td>{cool} °C · {spd} km/h</td></tr></table>')
    return spec('au-elec-u6-L3', 'MOST,<br>Gateways &amp;<br>OBD-II', 'Does clearing codes fix the fault?',
                f'Clearing turns the {gold("LAMP")} off;<br>the {cyan("fault")} comes back',
                'decoding service 03', tbl, brd,
                [chip('left', 300, 'c', ' '.join(f'{x:02X}' for x in reply)), chip('left', 364, 'c', 'service 03'),
                 chip('left', 470, 'c', f'{reply[1]} codes'), chip('right', 318, 'g', f'{c1}: misfire'),
                 chip('right', 500, 'g', f'set at {cool} °C, {spd} km/h', False)],
                f'03 01 → <b class="gl">{c1}</b> misfire; 01 33 → {c2}<br>'
                f'freeze frame: 0x7B − 40 = <b class="cl">{cool} °C</b>, {spd} km/h', css=TABLE_CSS)


def u6_l4():
    """6.7 worked example: brake-by-wire FTTI budget of 200 ms."""
    ftti, samp, conf, act = 200, 20, 40, 30
    det = ftti - samp - conf - act
    flag = samp + conf + det
    setup()
    o = []
    # left to right on the page: pedal with its sensor, the brake ECU, the disc and its caliper (the actuator)
    o.append(bx(1.6, 4.6, 1.0, 1.4, .2, MID))
    o.append(line3([(2.1, 5.6, .2), (2.1, 5.2, 1.6), (2.1, 4.8, 2.0)], SIL, 7))
    o.append(bx(1.8, 4.6, .6, .35, .22, STEEL, z0=1.9))
    o.append(label(2.1, 4.8, 2.3, 'pedal sensor', size=14, dy=-8))
    o.append(glow(line3([(2.6, 5.0, .2), (3.6, 4.2, .2)], SKY, 3)))
    o.append(ecu(3.6, 3.2, 1.8, 1.4, .7, 'ECU'))
    o.append(glow(line3([(5.4, 3.6, .3), (6.0, 3.0, .3)], SKY, 3)))
    o.append(hcyl('x', 6.0, 6.3, 1.9, 1.5, 1.35, '#5E6974', '#B7C1CA', '#E9EEF2'))
    o.append(f'<polygon points="{pts(*ring("x", 6.31, 1.9, 1.5, .45))}" fill="#3E454D"/>')
    o.append(bx(6.3, 1.0, .5, .9, 1.0, SKYB, z0=1.8))
    o.append(label(6.5, 1.9, 0, 'actuator', size=14, col=SKY, dx=30, dy=22))
    brd = board(o)
    X = lambda q: lin(q, 0, ftti, 20, 450)
    segs = [('sample', samp, '#8D98A3'), ('confirm', conf, '#AFC0CE'), ('detect', det, SKY), ('act', act, SIL)]
    s = ''
    t0 = 0
    for name, d, col in segs:
        s += f'<rect x="{X(t0) + 1:.1f}" y="48" width="{X(t0 + d) - X(t0) - 2:.1f}" height="40" rx="5" fill="{col}" opacity=".9"/>'
        s += tx((X(t0) + X(t0 + d)) / 2, 73, f'{d}', 'pt', col='#10151A')
        s += tx((X(t0) + X(t0 + d)) / 2, 38, name, 'ax')
        t0 += d
    s += vdash(X(flag), 26, 112, '#FFD27A') + tx(X(flag), 20, f'flag by {flag} ms', 'pt', col='#FFD27A')
    s += f'<line x1="20" y1="104" x2="450" y2="104" stroke="{AXC}" stroke-width="1.5"/>'
    s += ''.join(tx(X(q), 124, str(q)) for q in (0, samp + conf, flag, ftti)) + tx(450, 140, 'ms after the fault', anchor='end')
    card = svg(s)
    return spec('au-elec-u6-L4', 'Functional<br>Safety &amp; V2X', 'Does MISRA code meet ISO 26262?',
                f'{gold("MISRA")} keeps the code clean;<br>{cyan("ISO 26262")} shows it is safe',
                'brake-by-wire time budget', card, brd,
                [chip('left', 300, 'g', f'FTTI {ftti} ms'), chip('left', 364, 'c', f'sampling {samp} ms'),
                 chip('left', 470, 'c', f'confirm {conf} ms'), chip('right', 300, 'g', f'detect: {det} ms'),
                 chip('right', 500, 'c', f'actuator {act} ms', False)],
                f'detection = {ftti} − ({samp} + {conf} + {act}) = <b class="gl">{det} ms</b><br>'
                f'flag the fault by {samp} + {conf} + {det} = <b class="cl">{flag} ms</b>')


def u6_l5():
    """6.10 worked example: 300-byte BSM at 6 Mbit/s in a 50 ms control-channel interval."""
    nbytes, rate, cch, lost = 300, 6e6, 50, .10
    bits = nbytes * 8
    air = bits / rate * 1000
    usable = cch * (1 - lost)
    msgs = int(usable / air)
    setup()
    o = []
    o.append(bx(0, 1.9, 8, 4.4, .04, ('#262C32', '#14161A', '#1E2126')))
    for k in range(5):
        o.append(line3([(.3 + k * 1.6, 4.0, .05), (1.1 + k * 1.6, 4.0, .05)], '#8D98A3', 2))
    cars = [(.6, 2.4, STEEL), (4.4, 2.4, SKYB), (2.4, 4.7, SKYB)]
    for x, y, c in cars:
        cx, cy = P(x + 1.2, y + .6, 1.1)
        o.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="66" ry="34" fill="none" stroke="{SKY}" stroke-width="2" opacity=".5"/>')
    for x, y, c in cars:
        o.append(car(x, y, 'x', c))
    o.append(label(3.0, 2.4, 1.6, 'one BSM per 100 ms', size=14, col=SKY, dy=-26))
    brd = board(o)
    X = lambda q: lin(q, 0, cch, 20, 450)
    s = tx(20, 20, f'one {cch} ms interval', 'pt', 'start', SIL)
    s += f'<rect x="{X(0):.1f}" y="40" width="{X(cch) - X(0):.1f}" height="44" rx="6" fill="none" stroke="{AXC}" stroke-width="1.5"/>'
    s += f'<rect x="{X(usable):.1f}" y="40" width="{X(cch) - X(usable):.1f}" height="44" rx="6" fill="#5E6974" opacity=".6"/>'
    k = 0
    while (k + 1) * air <= usable:
        s += f'<rect x="{X(k * air):.2f}" y="44" width="{max(X((k + 1) * air) - X(k * air) - .9, .6):.2f}" height="36" fill="{SKY if k % 2 == 0 else "#4E9CC8"}"/>'
        k += 1
    s += tx(X(usable) / 2 + 10, 104, f'{msgs} BSMs × {g(air)} ms', 'pt', 'middle', SKY)
    s += tx((X(usable) + X(cch)) / 2, 104, f'{g(cch - usable)} ms lost', 'ax', 'middle')
    s += tx(X(0), 132, '0', anchor='start') + tx(X(usable), 34, f'{g(usable)} ms', 'ax', 'end') + tx(X(cch), 132, f'{cch} ms', anchor='end')
    card = svg(s)
    return spec('au-elec-u6-L5', 'VANETs,<br>DSRC &amp; WAVE', 'Is WAVE just 802.11p?',
                f'802.11p is the {gold("RADIO")};<br>{cyan("WAVE")} adds IEEE 1609 on top',
                'BSMs in one CCH interval', card, brd,
                [chip('left', 300, 'c', f'BSM {nbytes} bytes'), chip('left', 364, 'c', f'{g(rate / 1e6)} Mbit/s'),
                 chip('left', 470, 'c', f'{g(usable)} ms usable'), chip('right', 318, 'g', f'{g(air)} ms each'),
                 chip('right', 500, 'g', f'{msgs} cars at best', False)],
                f'{nbytes} × 8 = {bits} bits ÷ {g(rate / 1e6)} Mbit/s = <b class="gl">{g(air)} ms</b><br>'
                f'{cch} ms × 0.9 = {g(usable)} ms → {g(usable)} ÷ {g(air)} = <b class="cl">{msgs}</b> BSMs')


L1_BOARD = r'''<svg class="iso" width="1280" height="720"><defs><filter id="gl" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter><filter id="sh" x="-30%" y="-30%" width="160%" height="180%"><feDropShadow dx="0" dy="24" stdDeviation="20" flood-color="#000" flood-opacity=".6"/></filter><linearGradient id="pl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#343C44"/><stop offset="1" stop-color="#1F252B"/></linearGradient><linearGradient id="al" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7B8692"/><stop offset=".4" stop-color="#EEF2F5"/><stop offset=".65" stop-color="#B9C3CC"/><stop offset="1" stop-color="#5E6974"/></linearGradient><radialGradient id="pu" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#4A4F57"/><stop offset="1" stop-color="#16181C"/></radialGradient></defs><ellipse cx="952" cy="448" rx="240" ry="115" fill="#D9E1E8" opacity=".10" filter="url(#gl)"/><g filter="url(#sh)"><polygon points="723.4,450.0 952.0,582.0 952.0,600.1 723.4,468.1" fill="#0F1317"/><polygon points="1180.6,450.0 952.0,582.0 952.0,600.1 1180.6,468.1" fill="#161B20"/><polygon points="952.0,318.0 1180.6,450.0 952.0,582.0 723.4,450.0" fill="url(#pl)"/></g><polyline points="723.4,450.0 952.0,318.0 1180.6,450.0" fill="none" stroke="#FFFFFF" stroke-opacity=".14" stroke-width="2"/><ellipse cx="952.0" cy="331.2" rx="7" ry="4" fill="#5A504D" stroke="#120F0E" stroke-width="1.5"/><ellipse cx="1157.8" cy="450.0" rx="7" ry="4" fill="#5A504D" stroke="#120F0E" stroke-width="1.5"/><ellipse cx="746.2" cy="450.0" rx="7" ry="4" fill="#5A504D" stroke="#120F0E" stroke-width="1.5"/><ellipse cx="952.0" cy="568.8" rx="7" ry="4" fill="#5A504D" stroke="#120F0E" stroke-width="1.5"/><g filter="url(#gl)"><polyline points="1043.4,449.0 980.6,485.3 906.3,442.4 883.4,455.6" fill="none" stroke="#D9E1E8" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/></g><polyline points="832.0,425.9 894.8,389.6 986.3,442.4" fill="none" stroke="#2A2A2E" stroke-width="5" stroke-linejoin="round"/><polygon points="780.5,415.4 860.6,461.6 860.6,496.2 780.5,450.0" fill="#14161A"/><polygon points="912.0,431.9 860.6,461.6 860.6,496.2 912.0,466.5" fill="#1E2126"/><polygon points="832.0,385.7 912.0,431.9 860.6,461.6 780.5,415.4" fill="#2E3238"/><polygon points="819.1,394.1 832.0,401.5 832.0,408.8 819.1,401.3" fill="#5E6974"/><polygon points="844.8,394.1 832.0,401.5 832.0,408.8 844.8,401.3" fill="#7B8692"/><polygon points="832.0,386.6 844.8,394.1 832.0,401.5 819.1,394.1" fill="#9AA4AE"/><polygon points="870.6,423.8 883.4,431.2 883.4,438.5 870.6,431.0" fill="#7D8894"/><polygon points="896.3,423.8 883.4,431.2 883.4,438.5 896.3,431.0" fill="#AEB9C4"/><polygon points="883.4,416.3 896.3,423.8 883.4,431.2 870.6,423.8" fill="#D9E1E8"/><text x="820.5" y="461.6" text-anchor="middle" class="capl" fill="#E6ECF1" style="font-size:15px">12 V battery</text><ellipse cx="1066.3" cy="441.8" rx="50" ry="28" fill="#000" opacity=".4"/><path d="M1022.3,436.8 V366.8 A44,24 0 0 0 1110.3,366.8 V436.8 A44,24 0 0 1 1022.3,436.8Z" fill="url(#al)"/><path d="M1022.3,425.1 A44,24 0 0 0 1110.3,425.1" fill="none" stroke="#5E6974" stroke-width="1.8"/><path d="M1022.3,413.5 A44,24 0 0 0 1110.3,413.5" fill="none" stroke="#5E6974" stroke-width="1.8"/><path d="M1022.3,401.8 A44,24 0 0 0 1110.3,401.8" fill="none" stroke="#5E6974" stroke-width="1.8"/><path d="M1022.3,390.1 A44,24 0 0 0 1110.3,390.1" fill="none" stroke="#5E6974" stroke-width="1.8"/><path d="M1022.3,378.5 A44,24 0 0 0 1110.3,378.5" fill="none" stroke="#5E6974" stroke-width="1.8"/><ellipse cx="1066.3" cy="366.8" rx="44" ry="24" fill="#D7DEE4"/><ellipse cx="1066.3" cy="358.8" rx="27.3" ry="14.9" fill="url(#pu)"/><ellipse cx="1066.3" cy="358.8" rx="27.3" ry="14.9" fill="none" stroke="#5A5F66" stroke-width="2" stroke-dasharray="3 3"/><ellipse cx="1066.3" cy="358.8" rx="7" ry="4" fill="#9AA4AE"/></svg>'''


def specs():
    only = os.environ.get('ONLY', '')
    out = [u1_l1(), u1_l2(), u1_l3(), u1_l4(),
            u2_l1(), u2_l2(), u2_l3(), u2_l4(),
            u3_l1(), u3_l2(), u3_l3(), u3_l4(), u3_l5(), u3_l6(),
            u4_l1(), u4_l2(), u4_l3(),
            u5_l1(), u5_l2(), u5_l3(),
            u6_l1(), u6_l2(), u6_l3(), u6_l4(), u6_l5()]
    return [x for x in out if not only or any(x['key'].endswith(o) for o in only.split(','))]
