"""t16 split-blueprint thumbnails for ec-antenna (Antennas, RF and Microwave Engineering), ECE look.
One spec per lesson, each from that lesson's own book worked example (books/ece/ec-antenna/ec-antenna-u<N>.html).
Every number on a card, chip or summary is computed below from the example's data.
Build: python3 t16_split.py build specs.py <out dir>   (t16_split.py from the data pack, thumbs/t16_split/)."""
import cmath, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.environ.get('T16_TOOL', ''), os.path.join(HERE, '..', 'tool'), HERE):
    if p and os.path.exists(os.path.join(p, 't16_split.py')):
        sys.path.insert(0, p)
        break
import t16_split as T

B = T.B
P, pts, box, cyl, arrow = B.P, B.pts, B.box, T.cyl, T.arrow
D = 'ece'
AC, AC2 = T.DEPTS[D]['acc'], T.DEPTS[D]['acc2']          # violet ("gold" role), mint ("cyan" role)
SUBJ = 'ANTENNAS, RF AND MICROWAVE'
AX, GRID, INK = '#8C86B8', '#4A4480', '#E6ECF1'
METAL = ('#D7DCE4', '#8E97A6', '#B4BCC8')                 # top, left, right faces
DARK = ('#3A3470', '#1A1640', '#262058')
c0 = 299792458 / 1e0
C = 3e8                                                   # the book uses c = 3 x 10^8 m/s throughout


def f(v, n=2):
    """round to n decimals and drop trailing zeros"""
    s = f'{v:.{n}f}'
    return s.rstrip('0').rstrip('.') if '.' in s else s


def neg(s):
    return s.replace('-', '−')


def reset():
    B.U, B.OX, B.OY = 33, 952, 318


def Bp(px, py):
    """the board point (x, y) at z = 0 that lands on page point (px, py) with the standard origin"""
    a, b = (px - 952) / (33 * .866), (py - 318) / (33 * .5)
    return (a + b) / 2, (b - a) / 2


def at(dx=0, dy=0):
    """draw the board's parts shifted on the page by (dx, dy) px; the slab itself stays put (iso_board resets the origin)"""
    B.U, B.OX, B.OY = 33, 952 + dx, 318 + dy


# ------------------------------------------------------------------ small drawing helpers
def ln(a, b, col, w=3, extra=''):
    (x0, y0), (x1, y1) = P(*a), P(*b)
    return f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round" {extra}/>'


def rod(a, b, col, w=8, hi='#FFFFFF'):
    """a round rod or wire between two board points, with a highlight"""
    (x0, y0), (x1, y1) = P(*a), P(*b)
    return (f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<line x1="{x0:.1f}" y1="{y0 - w * .22:.1f}" x2="{x1:.1f}" y2="{y1 - w * .22:.1f}" stroke="{hi}" stroke-opacity=".45" stroke-width="{max(1.2, w * .25):.1f}" stroke-linecap="round"/>')


def poly(ps, fill, stroke='none', sw=2, extra=''):
    return f'<polygon points="{pts(*[P(*p) for p in ps])}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" {extra}/>'


def pline(ps, col, w=3, extra=''):
    return f'<polyline points="{pts(*[P(*p) for p in ps])}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'


def glow(s):
    return f'<g filter="url(#gl)">{s}</g>'


def lab(p, text, col=INK, size=15, anchor='middle', dy=0):
    x, y = P(*p)
    return f'<text x="{x:.1f}" y="{y + dy:.1f}" text-anchor="{anchor}" class="capl" style="font-size:{size}px;fill:{col}">{text}</text>'


def arr3(a, b, col, w=5):
    (x0, y0), (x1, y1) = P(*a), P(*b)
    return arrow(x0, y0, x1, y1, col, w)


def circ(c, r, plane='xy', n=48, a0=0, a1=2 * math.pi):
    """points of a circle (or arc) of radius r around board point c in a board plane"""
    out = []
    for i in range(n + 1):
        a = a0 + (a1 - a0) * i / n
        u, v = r * math.cos(a), r * math.sin(a)
        x, y, z = c
        out.append((x + u, y + v, z) if plane == 'xy' else (x + u, y, z + v) if plane == 'xz' else (x, y + u, z + v))
    return out


def block(x, y, w, d, h, cols=DARK, label=None, lcol=INK, size=15, z0=0):
    s = box(x, y, w, d, h, *cols, z0=z0)
    if label:
        s += lab((x + w / 2, y + d / 2, z0 + h), label, lcol, size, dy=5)
    return s


def board(parts):
    reset()
    return T.iso_board(D, parts)


# ------------------------------------------------------------------ card helpers (470 x 144)
def svg(inner):
    return f'<svg width="470" height="144" viewBox="0 0 470 144">{inner}</svg>'


def t(x, y, s, cls='ax', anchor='middle', col=None, extra=''):
    import re
    st = f'fill:{col};' if col else ''
    m = re.match(r'\s*style="([^"]*)"(.*)', extra)
    if m:
        st, extra = st + m.group(1), m.group(2)
    st = f' style="{st}"' if st else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}"{st} {extra}>{s}</text>'


def axes(x0, y0, x1, y1):
    return (f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{AX}" stroke-width="1.5"/>'
            f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{AX}" stroke-width="1.5"/>')


def curve(xy, col, w=3, extra=''):
    return f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in xy)}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" {extra}/>'


def hline(x0, x1, y, col, dash='5 5', w=1.6):
    return f'<line x1="{x0:.1f}" y1="{y:.1f}" x2="{x1:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="{w}" stroke-dasharray="{dash}"/>'


def vline(x, y0, y1, col, dash='5 5', w=1.6):
    return f'<line x1="{x:.1f}" y1="{y0:.1f}" x2="{x:.1f}" y2="{y1:.1f}" stroke="{col}" stroke-width="{w}" stroke-dasharray="{dash}"/>'


def dot(x, y, col, r=5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>'


def rect(x, y, w, h, col, op=1, rx=3, stroke='none'):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{col}" fill-opacity="{op}" stroke="{stroke}"/>'


def chips(*c):
    return [dict(side=s, top=tp, kind=k, text=tx, **({'pointer': False} if len(x) > 4 and x[4] is False else {}))
            for x in c for s, tp, k, tx in [x[:4]]]


def spec(key, title, takeaway, card_title, card, brd, ch, summary, css=''):
    import json
    th = THUMBS[key]
    return dict(key=key, subject=th['subject'], title=title, question=th['hook'], takeaway=takeaway, tag='Book example',
                card_title=card_title, card=card, board=brd, chips=ch, summary=summary, css=css,
                page_title=f'{th["topic"].replace("&", "&amp;")}: ECE')


def _load_thumbs():
    import json
    for p in (os.path.join(HERE, 'thumbs.json'), os.path.join(HERE, '..', 'thumbnail', 'thumbs.json')):
        if os.path.exists(p):
            return json.load(open(p, encoding='utf-8'))['lessons']
    raise SystemExit('thumbs.json (from deliver/ec-antenna: ec-antenna/thumbnail/thumbs.json) not found next to specs.py')


THUMBS = _load_thumbs()
TABLE_CSS = """
.scope table{border-collapse:collapse;width:100%;margin-top:4px;font:600 17px 'IBM Plex Sans';color:#E6ECF1}
.scope th{font:600 14px 'IBM Plex Sans';color:#B9B2E6;text-align:center;padding:3px 6px;border-bottom:1.5px solid rgba(195,184,255,.3)}
.scope td{text-align:center;padding:6px 6px;border-bottom:1px solid rgba(195,184,255,.16);font-size:18px}
.scope td:first-child{text-align:left;font-weight:700}.scope tr:last-child td{border-bottom:none}"""


# ================================================================== unit 1
def u1_l1():
    """1.2 worked example: 50 ohm line, ZL = 100 + j50 ohm -> Gamma, VSWR, return loss, Vmax/Vmin positions"""
    Z0, ZL = 50, complex(100, 50)
    G = (ZL - Z0) / (ZL + Z0)
    g, th = abs(G), math.degrees(cmath.phase(G))
    S = (1 + g) / (1 - g)
    RL = -20 * math.log10(g)
    refl = g ** 2
    dmax = th / 720
    dmin = dmax + .25
    assert (f(G.real, 1), f(G.imag, 1), f(g, 3), f(S, 2), f(RL, 2)) == ('0.4', '0.2', '0.447', '2.62', '6.99')
    assert (f(dmax, 3), f(dmin, 3), round(refl * 100)) == ('0.037', '0.287', 20)
    env = lambda d: abs(1 + G * cmath.exp(-1j * 4 * math.pi * d))      # |V(d)|/|V+|, d in wavelengths from the load
    # board: generator, a two-wire line along x, the load ZL; the standing-wave envelope rises above the line
    at(30, 0)
    parts = [rod((1.2, 3.65, .45), (6.3, 3.65, .45), '#C9CED8', 6), rod((1.2, 4.35, .45), (6.3, 4.35, .45), '#C9CED8', 6),
             block(6.3, 3.3, 1.3, 1.4, 1.0, (AC, '#5B45B0', '#7A62D6'))]
    L0, L1 = 6.3, 1.2                                                     # load at x = 6.3; the line shown is 0.6 wavelength
    env_pts = [(L0 - (L0 - L1) * i / 120, 4.0, .45 + 1.5 * env(.6 * i / 120)) for i in range(121)]
    base = [(p[0], 4.0, .45) for p in env_pts]
    parts.append(f'<polygon points="{pts(*[P(*p) for p in env_pts + base[::-1]])}" fill="{AC}" fill-opacity=".16"/>')
    parts.append(glow(pline(env_pts, AC, 3.5)))
    xm = L0 - (L0 - L1) * dmax / .6
    xn = L0 - (L0 - L1) * dmin / .6
    parts += [ln((xm, 4, .45), (xm, 4, .45 + 1.5 * (1 + g)), AC2, 2, 'stroke-dasharray="4 4"'),
              ln((xn, 4, .45), (xn, 4, .45 + 1.5 * (1 - g)), AC2, 2, 'stroke-dasharray="4 4"'),
              lab((6.95, 4.0, 1.0), 'Z<tspan font-size="11">L</tspan>', '#17112E', 17, dy=6),
              arr3((2.0, 2.8, .4), (4.6, 2.8, .4), AC, 5), arr3((5.4, 5.4, .4), (3.2, 5.4, .4), AC2, 4)]
    brd = board(parts)
    # card: left |V| along the line, right the VSWR scale
    X = lambda d: 44 + d / .5 * 196
    Y = lambda v: 122 - v / 1.6 * 96
    xy = [(X(.5 - .5 * i / 100), Y(env(.5 * i / 100))) for i in range(101)]
    left = (t(140, 16, 'standing wave |V|', 'pt', col=AC) + axes(44, 26, 244, 122) + curve(xy, AC, 3)
            + hline(44, 244, Y(1 + g), AC2, '4 4', 1.2) + hline(44, 244, Y(1 - g), AC2, '4 4', 1.2)
            + t(38, Y(1 + g) + 5, f(1 + g, 3), anchor='end') + t(38, Y(1 - g) + 5, f(1 - g, 3), anchor='end')
            + t(244, 138, 'load', anchor='end') + t(44, 138, '0.5λ', anchor='start'))
    sx = lambda v: 290 + (1 - 1 / v) * 170                                # VSWR 1..inf mapped by 1 - 1/S
    right = (t(375, 16, 'VSWR scale', 'pt', col=AC2) + rect(290, 58, 170, 22, '#2E2862', 1, 6)
             + rect(290, 58, sx(S) - 290, 22, AC2, .5, 6) + dot(sx(S), 69, AC2, 7)
             + t(290, 102, '1', anchor='middle') + t(460, 102, '∞', anchor='middle') + t(sx(S), 48, f(S, 2), 'pt', col=AC2)
             + t(290, 122, 'matched', anchor='start') + t(460, 122, 'short', anchor='end') + t(375, 140, 'nothing below 1', col='#B9B2E6'))
    card = svg(left + right)
    return spec('ec-antenna-u1-L1', 'Line Constants,<br>Reflection<br>&amp; VSWR',
                f'VSWR runs from <span class="gold">1</span> to ∞:<br>it is <span class="cyan">NEVER</span> below 1',
                f'{f(ZL.real, 0)} + j{f(ZL.imag, 0)} Ω on {Z0} Ω', card, brd,
                chips(('left', 300, 'g', f'Z<sub>L</sub> = {f(ZL.real, 0)} + j{f(ZL.imag, 0)} Ω'), ('left', 364, 'c', f'Γ = {f(G.real, 1)} + j{f(G.imag, 1)}'),
                      ('left', 520, 'c', f'|Γ| = {f(g, 3)}'), ('right', 300, 'g', f'VSWR = {f(S, 2)}'),
                      ('right', 530, 'c', f'{round(refl * 100)} % reflected', False)),
                f'Γ = (Z<sub>L</sub> − Z₀)/(Z<sub>L</sub> + Z₀) = {f(G.real, 1)} + j{f(G.imag, 1)}, <b class="cl">|Γ| = {f(g, 3)}</b><br>'
                f'VSWR = (1 + |Γ|)/(1 − |Γ|) = {f(1 + g, 3)} ÷ {f(1 - g, 3)} = <b class="gl">{f(S, 2)}</b>')


def u1_l2():
    """1.4 worked example 1: quarter-wave transformer, 100 ohm load to a 50 ohm line at 2.4 GHz"""
    Z0, ZL, f0, vp = 50, 100, 2.4e9, 2e8
    Zq = math.sqrt(Z0 * ZL)
    lam = vp / f0
    l = lam / 4

    def gam(fr):
        th = math.pi / 2 * fr / f0
        if abs(math.cos(th)) < 1e-12:
            Zin = Zq ** 2 / ZL
        else:
            tn = math.tan(th)
            Zin = Zq * (ZL + 1j * Zq * tn) / (Zq + 1j * ZL * tn)
        return abs((Zin - Z0) / (Zin + Z0))
    # band where |Gamma| <= 0.2 (VSWR <= 1.5), found numerically and checked against the book's 1.46 to 3.34 GHz
    fs = [f0 * (.3 + 1.4 * i / 20000) for i in range(20001)]
    ok = [x for x in fs if gam(x) <= .2]
    lo, hi = ok[0] / 1e9, ok[-1] / 1e9
    assert (f(Zq, 2), f(lam * 100, 2), f(l * 100, 2), f(lo, 2), f(hi, 2)) == ('70.71', '8.33', '2.08', '1.46', '3.34')
    # board: 50 ohm line, the lit quarter-wave section, the 100 ohm resistor load
    at(40, 0)
    parts = [rod((1.0, 3.6, .3), (2.6, 3.6, .3), '#C9CED8', 6), rod((1.0, 4.4, .3), (2.6, 4.4, .3), '#C9CED8', 6),
             lab((1.8, 2.9, .3), '50 Ω', AC2, 16),
             box(2.6, 3.35, 2.4, 1.3, .55, AC, '#5B45B0', '#7A62D6'),
             lab((3.8, 4.0, .55), '70.71 Ω', '#17112E', 16, dy=6),
             rod((5.0, 3.6, .3), (5.6, 3.6, .3), '#C9CED8', 6), rod((5.0, 4.4, .3), (5.6, 4.4, .3), '#C9CED8', 6)]
    # resistor body standing on the board with colour bands (brown black brown = 100 ohm)
    x, y = P(6.3, 4.0)
    parts.append(cyl(x, y, 20, 11, 84, '#D9C9A3', '#EADDBD'))
    for k, col in enumerate(('#6B3E1E', '#111111', '#6B3E1E')):
        parts.append(f'<path d="M{x - 20},{y - 22 - k * 16} A20,11 0 0 0 {x + 20},{y - 22 - k * 16} v-6 A20,11 0 0 1 {x - 20},{y - 28 - k * 16}Z" fill="{col}"/>')
    parts.append(lab((6.3, 4.0, 3.4), '100 Ω', AC2, 16))
    brd = board(parts)
    X = lambda fr: 44 + fr / 4.8e9 * 410
    Y = lambda gv: 124 - gv / .4 * 96
    xy = [(X(x_), Y(min(gam(x_), .4))) for x_ in [4.8e9 * i / 300 for i in range(1, 301)]]
    card = svg(t(250, 16, '|Γ| seen by the 50 Ω line against frequency', 'pt', col=AC) + axes(44, 26, 454, 124)
               + rect(X(lo * 1e9), 28, X(hi * 1e9) - X(lo * 1e9), 96, AC2, .12, 0)
               + curve(xy, AC, 3) + hline(44, 454, Y(.2), AC2, '5 4', 1.6) + dot(X(f0), Y(0), AC, 6)
               + t(38, Y(.2) + 5, '0.2', anchor='end') + t(38, Y(.4) + 10, '0.4', anchor='end')
               + t(X(lo * 1e9), 140, f(lo, 2)) + t(X(hi * 1e9), 140, f(hi, 2)) + t(X(f0), 140, '2.4', col=AC)
               + t(454, 140, 'GHz', anchor='end') + t((X(lo * 1e9) + X(hi * 1e9)) / 2, 44, 'VSWR ≤ 1.5', 'pt', col=AC2))
    return spec('ec-antenna-u1-L2', 'Input<br>Impedance<br>&amp; Matching',
                'Matches a <span class="gold">REAL</span> load,<br>over a <span class="cyan">BAND</span> of f',
                f'{ZL} Ω to {Z0} Ω, 2.4 GHz', card, brd,
                chips(('left', 300, 'c', f'Z₀ = {Z0} Ω'), ('left', 364, 'g', f'Z₀′ = {f(Zq, 2)} Ω'), ('left', 520, 'g', f'l = λ/4 = {f(l * 100, 2)} cm'),
                      ('right', 300, 'c', f'Z<sub>L</sub> = {ZL} Ω, real'), ('right', 530, 'c', f'{f(lo, 2)} to {f(hi, 2)} GHz', False)),
                f'Z₀′ = √(Z₀Z<sub>L</sub>) = √({Z0} × {ZL}) = <b class="gl">{f(Zq, 2)} Ω</b>, λ = {f(lam * 100, 2)} cm<br>'
                f'l = λ/4 = <b class="cl">{f(l * 100, 2)} cm</b>; VSWR ≤ 1.5 from {f(lo, 2)} to {f(hi, 2)} GHz')


def u1_l3():
    """1.5 worked example: Smith chart, zL = 2 + j1, shorted shunt stub"""
    Z0, ZL = 50, complex(100, 50)
    z = ZL / Z0
    G = (z - 1) / (z + 1)
    g = abs(G)
    S = (1 + g) / (1 - g)
    y = 1 / z
    Gy = -G                                                   # yL plotted on the chart: diametrically opposite
    G11 = (complex(1, 1) - 1) / (complex(1, 1) + 1)           # the point y = 1 + j1 on the g = 1 circle
    rot = (math.degrees(cmath.phase(Gy)) - math.degrees(cmath.phase(G11))) % 360   # clockwise turn
    d = rot / 720
    wtg_y, wtg_11 = .5 - math.degrees(cmath.phase(Gy)) % 360 / 720, None
    assert (f(z.real, 0), f(z.imag, 0), f(y.real, 1), f(y.imag, 1), f(S, 2), f(d, 3)) == ('2', '1', '0.4', '-0.2', '2.62', '0.199')
    ls = .125                                                 # stub: g = 0 circle from y = inf (0.250) to b = -1 (0.375)
    # board: a Smith chart lying flat on the board, the VSWR circle, z_L, y_L and the turn to g = 1
    at(20, 0)
    c, R = (4.0, 4.0, .05), 3.1
    Q = lambda gm: (c[0] + R * gm.real * .97, c[1] - R * gm.imag * .97, .05)   # Gamma plane -> board (Im up the chart = -y)
    parts = [poly(circ(c, R + .15), '#EDEAF8', '#B79CFF', 2), poly(circ(c, R), '#F7F6FC', '#8C86B8', 1.5)]
    for r in (.5, 1, 2):                                      # constant-r circles: centre r/(1+r), radius 1/(1+r)
        parts.append(pline(circ((c[0] + R * r / (1 + r), c[1], .05), R / (1 + r)), '#B5AEDC', 1.4))
    for x in (.5, 1, 2):                                      # constant-x arcs inside the chart
        arc = []
        for i in range(161):
            rr = 10 ** (-2 + 4 * i / 160) - .01
            gm = (complex(rr, x) - 1) / (complex(rr, x) + 1)
            arc.append(gm)
        parts.append(pline([Q(a) for a in arc], '#CFC9EA', 1.2))
        parts.append(pline([Q(a.conjugate()) for a in arc], '#CFC9EA', 1.2))
    parts.append(ln(Q(-1), Q(1), '#8C86B8', 1.5))
    parts.append(pline(circ((c[0], c[1], .06), R * .97 * g), AC2, 2.5, 'stroke-dasharray="7 5"'))
    a0 = cmath.phase(Gy)
    turn = [Q(g * cmath.exp(1j * (a0 - math.radians(rot) * i / 60))) for i in range(61)]
    parts.append(glow(pline(turn, AC, 5)))
    parts.append(ln(Q(G), Q(Gy), '#5B45B0', 2.5, 'stroke-dasharray="5 5"'))
    for gm, col in ((G, AC2), (Gy, AC), (G11, AC)):
        x_, y_ = P(*Q(gm))
        parts.append(f'<ellipse cx="{x_:.1f}" cy="{y_:.1f}" rx="9" ry="5.5" fill="{col}" stroke="#17112E" stroke-width="2"/>')
    parts += [lab(Q(G), 'z<tspan font-size="11">L</tspan>', '#0E5A4E', 17, dy=26), lab(Q(Gy), 'y<tspan font-size="11">L</tspan>', '#3E2A99', 17, dy=24),
              lab(Q(G11), '1 + j1', '#3E2A99', 15, dy=-12)]
    brd = board(parts)
    # card: left the chart angle against line length, right the wavelength readings of the example
    X = lambda dd: 44 + dd / .5 * 196
    Y = lambda deg: 124 - deg / 360 * 96
    left = (t(140, 16, 'turn on the chart', 'pt', col=AC) + axes(44, 26, 244, 124) + curve([(X(0), Y(0)), (X(.5), Y(360))], AC, 3)
            + vline(X(.25), Y(180), 124, AC, '4 4') + hline(44, X(.25), Y(180), AC, '4 4') + dot(X(.25), Y(180), AC, 6)
            + vline(X(d), Y(rot), 124, AC2, '4 4') + dot(X(d), Y(rot), AC2, 5)
            + t(38, Y(180) + 5, '180°', anchor='end', col=AC) + t(38, Y(360) + 10, '360°', anchor='end')
            + t(X(.25), 140, 'λ/4', col=AC) + t(X(d) - 4, 140, f'{f(d, 3)}λ', col=AC2, anchor='end') + t(244, 140, 'λ/2', anchor='end'))
    rows = [('y<tspan font-size="11">L</tspan> = 0.4 − j0.2', '0.463λ'), ('to 1 + j1', '0.162λ'), ('d', f'{f(d, 3)}λ'), ('stub l<tspan font-size="11">s</tspan>', '0.125λ')]
    right = t(362, 16, 'chart readings', 'pt', col=AC2)
    for k, (a, b) in enumerate(rows):
        right += t(270, 44 + k * 27, a, 'ax', 'start', INK, 'style="font-size:15px"') + t(460, 44 + k * 27, b, 'pt', 'end', AC2 if k >= 2 else INK)
    card = svg(left + right)
    return spec('ec-antenna-u1-L3', 'Smith Chart<br>&amp; Microstrip',
                'λ/4 turns it <span class="gold">HALF</span> a turn;<br>a full turn is <span class="cyan">λ/2</span>',
                f'z<sub>L</sub> = {f(z.real, 0)} + j{f(z.imag, 0)} on the chart', card, brd,
                chips(('left', 300, 'c', f'z<sub>L</sub> = {f(z.real, 0)} + j{f(z.imag, 0)}'), ('left', 364, 'g', f'y<sub>L</sub> = {f(y.real, 1)} − j{f(-y.imag, 1)}'),
                      ('left', 520, 'c', f'VSWR circle {f(S, 2)}'), ('right', 300, 'g', f'd = {f(d, 3)}λ'), ('right', 530, 'c', f'stub {ls}λ', False)),
                f'λ/4 turns the point <b class="gl">180°</b>: z<sub>L</sub> → y<sub>L</sub> = 0.4 − j0.2<br>'
                f'to g = 1: d = 0.037λ + 0.162λ = <b class="cl">{f(d, 3)}λ</b>')


def u1_l4():
    """1.7 worked example 1: air-filled X-band guide a = 2.286 cm, b = 1.016 cm"""
    a, b, fr, eta = .02286, .01016, 10e9, 377
    fc10, fc20, fc01 = C / (2 * a), C / a, C / (2 * b)
    k = math.sqrt(1 - (fc10 / fr) ** 2)
    lg = C / fr / k
    Zte = eta / k
    assert (f(fc10 / 1e9, 2), f(fc20 / 1e9, 2), f(fc01 / 1e9, 2), f(lg * 100, 2), f(Zte, 0)) == ('6.56', '13.12', '14.76', '3.98', '500')
    # board: a length of rectangular guide; broad wall a across, narrow wall b up; TE10 E-field arrows across the mouth
    at(10, 0)
    A, Bh, L = 3.6, 3.6 * b / a, 3.4                           # a : b drawn to scale (2.286 : 1.016)
    x0, y0 = 2.0, 2.0
    parts = [box(x0, y0, L, A, Bh, '#C9CED8', '#7F8898', '#A5AEBC')]
    # the open mouth on the front (y = y0 + A face is the left face; the mouth is the x = x0 + L face)
    m = [(x0 + L, y0 + .18, .18), (x0 + L, y0 + A - .18, .18), (x0 + L, y0 + A - .18, Bh - .18), (x0 + L, y0 + .18, Bh - .18)]
    parts.append(poly(m, '#1A1640'))
    for i in range(1, 8):                                     # E field: vertical, strength sin(pi x / a) across the broad wall
        u = i / 8
        h = (Bh - .5) * math.sin(math.pi * u)
        yy = y0 + .18 + (A - .36) * u
        zc = Bh / 2
        parts.append(glow(arr3((x0 + L + .02, yy, zc - h / 2), (x0 + L + .02, yy, zc + h / 2), AC2, 2.4 + 2.2 * math.sin(math.pi * u))))
    parts += [ln((x0 + L + .1, y0, Bh + .25), (x0 + L + .1, y0 + A, Bh + .25), AC, 2.5),
              lab((x0 + L + .1, y0 + A / 2, Bh + .25), 'a', AC, 18, dy=-8),
              ln((x0 + L + .1, y0 + A + .3, 0), (x0 + L + .1, y0 + A + .3, Bh), AC2, 2.5),
              lab((x0 + L + .1, y0 + A + .4, Bh / 2), 'b', AC2, 17, 'end', dy=6),
              glow(arr3((x0 + .3, y0 - .6, .5), (x0 + L - .2, y0 - .6, .5), AC, 5))]
    brd = board(parts)
    X = lambda fq: 30 + fq / 18e9 * 424
    card = (t(30, 18, 'cutoffs on the frequency axis', 'pt', 'start', AC)
            + rect(X(fc10), 52, X(fc20) - X(fc10), 34, AC2, .18, 4) + t((X(fc10) + X(fc20)) / 2, 74, 'one mode: TE10 only', 'pt', col=AC2)
            + f'<line x1="30" y1="104" x2="454" y2="104" stroke="{AX}" stroke-width="1.5"/>')
    for fq, name, col in ((fc10, 'TE10', AC), (fc20, 'TE20', INK), (fc01, 'TE01', INK)):
        an, dx = {'TE20': ('end', -3), 'TE01': ('start', 3)}.get(name, ('middle', 0))
        card += vline(X(fq), 44, 108, col, 'none', 2.4) + t(X(fq) + dx, 124, f(fq / 1e9, 2), anchor=an, col=col) + t(X(fq) + dx, 140, name, anchor=an, col=col, extra='style="font-size:12px"')
    card += dot(X(fr), 104, AC, 6) + t(X(fr), 124, '10', col=AC) + t(30, 124, '0', anchor='start') + t(454, 140, 'GHz', anchor='end')
    card = svg(card)
    return spec('ec-antenna-u1-L4', 'Waveguides<br>&amp; Resonators',
                'The <span class="gold">BROAD</span> wall sets it:<br>f<sub>c</sub> = c/2a = <span class="cyan">6.56</span> GHz',
                'X-band guide cutoffs', card, brd,
                chips(('left', 300, 'g', f'a = {f(a * 100, 3)} cm'), ('left', 364, 'c', f'b = {f(b * 100, 3)} cm'), ('left', 520, 'g', f'f<sub>c10</sub> = {f(fc10 / 1e9, 2)} GHz'),
                      ('right', 300, 'c', f'λ<sub>g</sub> = {f(lg * 100, 2)} cm at 10 GHz'), ('right', 530, 'c', f'Z<sub>TE</sub> = {f(Zte, 0)} Ω', False)),
                f'f<sub>c10</sub> = c/2a = 3×10⁸ ÷ {f(2 * a, 5)} = <b class="gl">{f(fc10 / 1e9, 2)} GHz</b><br>'
                f'TE20 {f(fc20 / 1e9, 2)}, TE01 {f(fc01 / 1e9, 2)}: one mode <b class="cl">{f(fc10 / 1e9, 2)}–{f(fc20 / 1e9, 2)} GHz</b>')


# ================================================================== unit 2
def u2_l1():
    """2.2 worked example 1: F(theta) = sin(theta), HPBW, beam solid angle, D and G"""
    th_h = math.degrees(math.asin(math.sqrt(.5)))
    hp = 180 - 2 * th_h
    n = 20000
    omega = 2 * math.pi * sum(math.sin((i + .5) * math.pi / n) ** 3 for i in range(n)) * math.pi / n
    Dd = 4 * math.pi / omega
    G = .9 * Dd
    assert (f(th_h, 0), f(hp, 0), f(omega, 2), f(Dd, 2), f(10 * math.log10(Dd), 2), f(G, 2), f(10 * math.log10(G), 2)) == ('45', '90', '8.38', '1.5', '1.76', '1.35', '1.3')
    # board: a short vertical dipole with its field (violet) and power (mint) patterns in the vertical plane
    at(30, 0)
    cx, cy = 4.0, 3.6
    parts = [poly(circ((cx, cy, 0), 1.0), '#2E2862', '#5B52A0', 1.5)]
    for sgn in (1, -1):
        fld = [(cx + sgn * 2.6 * math.sin(math.radians(a)) ** 2, cy, 2.4 + 2.6 * math.sin(math.radians(a)) * math.cos(math.radians(a))) for a in range(0, 181, 3)]
        pw = [(cx + sgn * 2.6 * math.sin(math.radians(a)) ** 3, cy, 2.4 + 2.6 * math.sin(math.radians(a)) ** 2 * math.cos(math.radians(a))) for a in range(0, 181, 3)]
        parts.append(poly(fld, AC, AC, 3, 'fill-opacity=".14"'))
        parts.append(glow(poly(pw, AC2, AC2, 3, 'fill-opacity=".18"')))
        for a in (45, 135):                                   # half-power directions
            r = 2.6 * math.sin(math.radians(a))
            parts.append(ln((cx, cy, 2.4), (cx + sgn * r * math.sin(math.radians(a)), cy, 2.4 + r * math.cos(math.radians(a))), '#FFFFFF', 1.6, 'stroke-dasharray="4 4" stroke-opacity=".7"'))
    parts += [rod((cx, cy, 1.85), (cx, cy, 2.3), '#E8EBF2', 7), rod((cx, cy, 2.5), (cx, cy, 2.95), '#E8EBF2', 7),
              rod((cx, cy, 0), (cx, cy, 1.85), '#6E6A92', 3)]
    brd = board(parts)
    X = lambda a: 44 + a / 180 * 230
    Y = lambda v: 124 - v * 96
    fld = [(X(a), Y(math.sin(math.radians(a)))) for a in range(0, 181, 2)]
    pw = [(X(a), Y(math.sin(math.radians(a)) ** 2)) for a in range(0, 181, 2)]
    left = (t(160, 16, 'field and power against θ', 'pt', col=AC) + axes(44, 26, 274, 124) + curve(fld, AC, 3) + curve(pw, AC2, 3)
            + hline(44, X(135), Y(.7071), AC, '4 4', 1.3) + hline(44, X(135), Y(.5), AC2, '4 4', 1.3)
            + vline(X(45), Y(.7071), 124, '#FFFFFF', '3 4', 1.2) + vline(X(135), Y(.7071), 124, '#FFFFFF', '3 4', 1.2)
            + t(38, Y(.7071) + 2, '0.707', anchor='end', col=AC) + t(38, Y(.5) + 12, '0.5', anchor='end', col=AC2)
            + t(X(45), 140, '45°') + t(X(135), 140, '135°') + t(X(90), 140, 'HPBW 90°', col=INK))
    right = t(372, 16, 'one shape, four numbers', 'pt', col=AC2)
    for k, (a, b, col) in enumerate((('HPBW', f'{f(hp, 0)}°', AC), ('Ω<tspan font-size="11">A</tspan>', f'{f(omega, 2)} sr', INK),
                                     ('D', f'{f(Dd, 2)} ({f(10 * math.log10(Dd), 2)} dBi)', AC2), ('G', f'{f(G, 2)} ({10 * math.log10(G):.2f} dBi)', INK))):
        right += t(290, 46 + k * 27, a, 'ax', 'start', '#B9B2E6', 'style="font-size:15px"') + t(462, 46 + k * 27, b, 'pt', 'end', col)
    card = svg(left + right)
    return spec('ec-antenna-u2-L1', 'Radiation<br>&amp; Antenna<br>Parameters',
                'Half power: field <span class="gold">0.707</span>,<br>power <span class="cyan">0.5</span> (−3 dB)',
                'pattern F(θ) = sin θ', card, brd,
                chips(('left', 300, 'c', 'F(θ) = sin θ'), ('left', 364, 'g', 'field 0.707 at 45°'), ('left', 520, 'c', 'power 0.5, −3 dB'),
                      ('right', 300, 'g', f'HPBW = {f(hp, 0)}°'), ('right', 530, 'c', f'D = {f(Dd, 2)}, {f(10 * math.log10(Dd), 2)} dBi', False)),
                f'sin²θ = 0.5 → sin θ = <b class="gl">0.707</b>, θ = 45° and 135°<br>'
                f'HPBW = 135° − 45° = <b class="gl">{f(hp, 0)}°</b>; D = 4π ÷ {f(omega, 2)} = <b class="cl">{f(Dd, 2)}</b>')


def u2_l2():
    """2.4 worked example 1: 0.6 m DTH dish at 12 GHz; reactive edge, far-field start, a 20 m terrace test"""
    Dm, fr, r_test = .6, 12e9, 20
    lam = C / fr
    r1 = .62 * math.sqrt(Dm ** 3 / lam)
    r2 = 2 * Dm ** 2 / lam
    assert (f(lam, 3), f(r1, 2), f(r2, 1)) == ('0.025', '1.82', '28.8') and r1 < r_test < r2
    # board: the dish at the back, a ground strip in three regions (log-spaced, not to scale), the test antenna at 20 m
    lg = lambda r: .8 + 6.6 * (math.log10(r) + .3) / (math.log10(60) + .3)     # distance -> board x (log)
    at(20, 0)
    parts = []
    for (ra, rb, col, op) in ((.5, r1, '#5B45B0', .55), (r1, r2, AC2, .22), (r2, 60, AC, .3)):
        parts.append(poly([(lg(ra), 2.2, .01), (lg(rb), 2.2, .01), (lg(rb), 3.8, .01), (lg(ra), 3.8, .01)], col, 'none', 0, f'fill-opacity="{op}"'))
    # dish: a circle in the y-z plane facing +x, on a post
    dc = (1.0, 3.0, 1.9)
    parts += [rod((1.0, 3.0, 0), (1.0, 3.0, 1.2), '#8E97A6', 7),
              poly(circ(dc, 1.15, 'yz'), '#D9DDE6', '#9AA3B2', 2), poly(circ(dc, .8, 'yz'), '#C3C9D4', 'none'),
              rod((1.0, 3.0, 1.2), (1.9, 3.0, 1.9), '#8E97A6', 3), block(1.85, 2.85, .35, .3, .3, ('#F0F2F6', '#9AA3B2', '#C3C9D4'), z0=1.75)]
    # test antenna on a tripod at 20 m
    tx = lg(r_test)
    parts += [rod((tx, 3.0, 0), (tx, 3.0, 1.4), '#8E97A6', 4), rod((tx - .35, 3.4, 0), (tx, 3.0, .9), '#8E97A6', 3),
              box(tx - .25, 2.75, .5, .5, .45, AC2, '#1E8F7F', '#2BB5A1', z0=1.4), lab((tx, 3.0, 2.4), '20 m', AC2, 16)]
    parts.append(glow(arr3((2.4, 1.8, 1.9), (tx - .5, 1.8, 1.9), AC, 4)))
    brd = board(parts)
    X = lambda r: 30 + (math.log10(r) - math.log10(.1)) / (math.log10(100) - math.log10(.1)) * 424
    card = (t(30, 18, 'distance from the dish (log scale)', 'pt', 'start', AC)
            + rect(X(.1), 44, X(r1) - X(.1), 40, '#5B45B0', .55, 0) + rect(X(r1), 44, X(r2) - X(r1), 40, AC2, .2, 0) + rect(X(r2), 44, X(100) - X(r2), 40, AC, .28, 0)
            + t((X(.1) + X(r1)) / 2, 69, 'reactive', 'pt', col=INK) + t((X(r1) + X(r2)) / 2, 69, 'radiating near', 'pt', col=AC2)
            + t((X(r2) + X(100)) / 2, 69, 'far', 'pt', col=AC)
            + f'<line x1="30" y1="96" x2="454" y2="96" stroke="{AX}" stroke-width="1.5"/>')
    for r, s in ((.1, '0.1'), (1, '1'), (10, '10'), (100, '100 m')):
        card += t(X(r), 140, s, anchor='end' if r == 100 else 'middle')
    card += (vline(X(r1), 40, 100, INK, 'none', 2) + t(X(r1), 116, f'{f(r1, 2)} m', col=INK) + vline(X(r2), 40, 100, AC, 'none', 2.5) + t(X(r2) + 6, 116, f'{f(r2, 1)} m', 'pt', 'start', AC)
             + dot(X(r_test), 96, AC2, 6) + t(X(r_test) - 6, 116, '20 m', 'pt', 'end', AC2))
    card = svg(card)
    return spec('ec-antenna-u2-L2', 'Efficiency,<br>Aperture &amp;<br>Far Field',
                'Far field from <span class="gold">2D²/λ</span>:<br>it moves <span class="cyan">OUT</span> as f rises',
                f'{f(Dm, 1)} m dish at {f(fr / 1e9, 0)} GHz', card, brd,
                chips(('left', 300, 'g', f'D = {f(Dm, 1)} m, {f(fr / 1e9, 0)} GHz'), ('left', 364, 'c', f'λ = {f(lam, 3)} m'), ('left', 520, 'c', f'reactive to {f(r1, 2)} m'),
                      ('right', 300, 'g', f'far field from {f(r2, 1)} m'), ('right', 530, 'c', '20 m: not enough', False)),
                f'0.62√(D³/λ) = 0.62 × {f(math.sqrt(Dm ** 3 / lam), 3)} = <b class="cl">{f(r1, 2)} m</b> reactive<br>'
                f'2D²/λ = {f(2 * Dm ** 2, 2)} ÷ {f(lam, 3)} = <b class="gl">{f(r2, 1)} m</b> > 20 m terrace')


def u2_l3():
    """2.5 worked example 1: half-wave dipole for 100 MHz cut to 0.47 lambda, 1 A peak feed; the folded version from the same chapter"""
    fr, I0, Rr, r = 100e6, 1.0, 73, 1000
    lam = C / fr
    l = .47 * lam
    Prad = .5 * I0 ** 2 * Rr
    E = 60 * I0 / r
    Rf = 4 * Rr                                               # folded: two wires, same feed current, field x2, power x4
    assert (f(l, 2), f(Prad, 1), f(E * 1e3, 0), Rf) == ('1.41', '36.5', '60', 292)
    # board: a half-wave dipole held level on a mast, its cosine current drawn above the wire, the broadside field arrow
    at(0, 0)
    cx, cy, zw, half = 4.0, 4.0, 2.1, 2.5                    # wire along y, centre fed
    parts = [rod((cx, cy, 0), (cx, cy, zw - .1), '#6E6A92', 6), block(cx - .4, cy - .4, .8, .8, .3, DARK),
             rod((cx, cy - half, zw), (cx, cy - .12, zw), '#E8EBF2', 7), rod((cx, cy + .12, zw), (cx, cy + half, zw), '#E8EBF2', 7)]
    cur = [(cx, cy + u, zw + .25 + 1.4 * math.cos(math.pi * u / (2 * half))) for u in [-half + 2 * half * i / 60 for i in range(61)]]
    parts.append(poly(cur + [(cx, cy + half, zw + .25), (cx, cy - half, zw + .25)], AC, 'none', 0, 'fill-opacity=".16"'))
    parts.append(glow(pline(cur, AC, 3.5)))
    parts.append(lab((cx, cy, zw + 1.95), 'I₀ = 1 A', AC, 16, dy=-4))
    parts.append(glow(arr3((cx + .6, cy, zw - .2), (7.6, cy, zw - .2), AC2, 5)))
    parts.append(lab((6.4, cy + .6, zw - .2), 'to 1 km', AC2, 15, dy=22))
    brd = board(parts)
    Y = lambda zz: 124 - zz * 96
    xs = [44 + 200 * i / 80 for i in range(81)]
    left = (t(144, 16, 'current on the 1.41 m wire', 'pt', col=AC) + axes(44, 26, 244, 124)
            + curve([(x, Y(math.cos(math.pi * (i / 80 - .5)))) for i, x in enumerate(xs)], AC, 3)
            + t(144, 140, 'feed') + t(44, 140, 'tip', anchor='start') + t(244, 140, 'tip', anchor='end') + t(38, Y(1) + 10, '1 A', anchor='end', col=AC))
    H = lambda R: R / 360 * 96
    right = (t(362, 16, 'input resistance', 'pt', col=AC2) + f'<line x1="276" y1="124" x2="456" y2="124" stroke="{AX}" stroke-width="1.5"/>'
             + rect(296, 124 - H(Rr), 56, H(Rr), AC, .8, 4) + rect(380, 124 - H(Rf), 56, H(Rf), AC2, .8, 4)
             + hline(276, 456, 124 - H(300), '#FFFFFF', '4 4', 1.2) + t(278, 124 - H(300) - 5, '300 Ω twin-lead', anchor='start', col='#B9B2E6')
             + t(324, 124 - H(Rr) - 6, f'{Rr} Ω', 'pt', col=AC) + t(408, 124 - H(Rf) + 22, f'{Rf} Ω', 'pt', col='#17112E')
             + t(324, 140, 'dipole') + t(408, 140, 'folded'))
    card = svg(left + right)
    return spec('ec-antenna-u2-L3', 'Dipoles,<br>Monopoles &amp;<br>Small Loops',
                'Two wires: field <span class="gold">×2</span>,<br>power and R<sub>in</sub> <span class="cyan">×4</span>',
                f'λ/2 dipole at {f(fr / 1e6, 0)} MHz', card, brd,
                chips(('left', 300, 'c', f'l = 0.47λ = {f(l, 2)} m'), ('left', 364, 'g', f'I₀ = {f(I0, 0)} A peak'), ('left', 520, 'c', f'R<sub>r</sub> = {Rr} Ω'),
                      ('right', 300, 'g', f'P<sub>rad</sub> = {f(Prad, 1)} W'), ('right', 530, 'c', f'folded: {Rf} Ω', False)),
                f'P<sub>rad</sub> = ½ × 1² × {Rr} = <b class="gl">{f(Prad, 1)} W</b>, 60 mV/m at 1 km<br>'
                f'folded: power ×4, R<sub>in</sub> = 4 × {Rr} = <b class="cl">{Rf} Ω</b>')


def u2_l4():
    """2.8 worked example 2: 6 GHz, 40 km hop, 1.2 m dishes (eap 0.55), 2 dB feeders, 1 W, -75 dBm sensitivity"""
    fr, d, Dm, eap, Lf, Pt, sens = 6e9, 40e3, 1.2, .55, 2, 30, -75
    lam = C / fr
    G = 10 * math.log10(eap * (math.pi * Dm / lam) ** 2)
    fspl = 32.44 + 20 * math.log10(fr / 1e6) + 20 * math.log10(d / 1e3)
    eirp = Pt - Lf + G
    Pr = eirp - fspl + G - Lf
    M = Pr - sens
    assert (f(G, 2), f(fspl, 2), f(eirp, 2), f(Pr, 2), f(M, 2)) == ('34.95', '140.04', '62.95', '-44.14', '30.86')
    # board: two dishes on masts at far corners, the 40 km path between them
    at(0, 0)
    parts = []
    A_, B_ = Bp(870, 450), Bp(1075, 505)
    ux, uy = B_[0] - A_[0], B_[1] - A_[1]
    n = math.hypot(ux, uy)
    ux, uy = ux / n, uy / n                                   # the path direction on the board
    for (x, y), sg in ((A_, 1), (B_, -1)):
        parts += [rod((x, y, 0), (x, y, 2.2), '#8E97A6', 7), block(x - .4, y - .4, .8, .8, .25, DARK)]
        cx, cy = x + sg * .25 * ux, y + sg * .25 * uy        # each dish turned to face the other
        disc = [(cx - uy * .95 * math.cos(a), cy + ux * .95 * math.cos(a), 2.7 + .95 * math.sin(a)) for a in [2 * math.pi * i / 48 for i in range(49)]]
        parts.append(poly(disc, '#D9DDE6', '#9AA3B2', 2))
        parts.append(rod((cx, cy, 2.7), (cx + sg * .7 * ux, cy + sg * .7 * uy, 2.7), '#8E97A6', 3))
    parts.append(glow(arr3((A_[0] + 1.0 * ux, A_[1] + 1.0 * uy, 2.7), (B_[0] - 1.0 * ux, B_[1] - 1.0 * uy, 2.7), AC, 5)))
    mx, my = (A_[0] + B_[0]) / 2, (A_[1] + B_[1]) / 2
    parts.append(lab((mx, my, 2.7), '40 km', AC, 17, dy=-16))
    brd = board(parts)
    steps = [('P<tspan font-size="10">t</tspan>', Pt), ('feeder', Pt - Lf), ('dish', eirp), ('path', eirp - fspl), ('dish', eirp - fspl + G), ('feeder', Pr)]
    Y = lambda v: 42 + (70 - v) / 160 * 74
    xs = [44 + k * 62 for k in range(6)]
    pl = []
    for k, (nm, v) in enumerate(steps):
        pl += [(xs[k] - 22, Y(v)), (xs[k] + 22, Y(v))]
    card = (t(30, 16, 'level along the hop, dBm', 'pt', 'start', AC) + hline(30, 456, Y(sens), AC2, '6 4', 1.8)
            + t(30, Y(sens) + 16, f'needs {neg(str(sens))}', anchor='start', col=AC2) + curve(pl, AC, 3))
    for k, (nm, v) in enumerate(steps):
        card += dot(xs[k], Y(v), AC, 4) + t(xs[k], 140, nm)
        card += t(xs[k], Y(v) - 8, neg(f(v, 1 if k in (2, 3, 5) else 0)), col=INK, extra='style="font-size:13px"')
    card += (f'<line x1="{xs[5] + 34}" y1="{Y(Pr):.1f}" x2="{xs[5] + 34}" y2="{Y(sens):.1f}" stroke="{AC2}" stroke-width="2.5"/>'
             + t(xs[5] + 42, (Y(Pr) + Y(sens)) / 2 + 6, f'{f(M, 1)} dB', 'pt', 'start', AC2))
    card = svg(card)
    return spec('ec-antenna-u2-L4', 'Receiving<br>Antennas &amp;<br>Link Budget',
                f'Yes: <span class="gold">31 dB</span> to spare<br>above <span class="cyan">−75 dBm</span>',
                f'{f(fr / 1e9, 0)} GHz hop, {f(d / 1e3, 0)} km', card, brd,
                chips(('left', 300, 'c', '1 W = 30 dBm'), ('left', 364, 'g', f'G = {f(G, 2)} dBi'), ('left', 520, 'c', f'FSPL = {f(fspl, 1)} dB'),
                      ('right', 300, 'g', f'P<sub>r</sub> = {neg(f(Pr, 1))} dBm'), ('right', 530, 'c', f'margin {f(M, 1)} dB', False)),
                f'P<sub>r</sub> = {f(eirp, 2)} − {f(fspl, 2)} + {f(G, 2)} − 2 = <b class="cl">{neg(f(Pr, 2))} dBm</b><br>'
                f'M = {neg(f(Pr, 2))} − (−75) = <b class="gl">{f(M, 2)} dB</b> of fade margin')


# ================================================================== unit 3
def u3_l1():
    """3.1 worked example 1: two isotropic radiators, d = lambda/2 on the z axis, element 2 leads by 90 degrees"""
    bd, al = math.pi, math.pi / 2
    psi = lambda th: bd * math.cos(th) + al
    AF = lambda th: abs(math.cos(psi(th) / 2))                # normalised field
    th_max = math.degrees(math.acos(-al / bd))
    th_null = math.degrees(math.acos((math.pi - al) / bd))
    f0 = AF(0)
    assert (f(th_max, 0), f(th_null, 0), f(f0, 3), f(f0 ** 2, 1)) == ('120', '60', '0.707', '0.5')
    # board: the z axis as a vertical mast, two glowing point sources lambda/2 apart, the pattern in the vertical plane
    at(40, 0)
    cx, cy, zc, s = 4.0, 4.0, 2.0, .9                         # sources at zc -+ s/2 ... element 1 below, element 2 above
    R = 2.8
    parts = [rod((cx, cy, 0), (cx, cy, 3.9), '#6E6A92', 3)]
    for sgn in (1, -1):
        pat = [(cx + sgn * R * AF(math.radians(a)) * math.sin(math.radians(a)), cy, zc + R * AF(math.radians(a)) * math.cos(math.radians(a))) for a in range(0, 181, 2)]
        parts.append(glow(poly(pat, AC, AC, 3, 'fill-opacity=".16"')))
        a = math.radians(th_max)
        parts.append(ln((cx, cy, zc), (cx + sgn * R * math.sin(a), cy, zc + R * math.cos(a)), '#FFFFFF', 1.6, 'stroke-dasharray="4 4" stroke-opacity=".75"'))
    for zz, col, tag in ((zc - s / 2, AC2, '1: 0°'), (zc + s / 2, AC, '2: +90°')):
        x, y = P(cx, cy, zz)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="{col}" stroke="#17112E" stroke-width="2"/>')
        parts.append(lab((cx, cy, zz), tag, col, 15, 'end', dy=5).replace(f'x="{x:.1f}"', f'x="{x - 16:.1f}"'))
    parts.append(lab((cx, cy, 4.15), 'z', '#B9B2E6', 15))
    brd = board(parts)
    X = lambda a: 44 + a / 180 * 400
    Y = lambda v: 124 - v * 92
    xy = [(X(a), Y(AF(math.radians(a)))) for a in range(0, 181)]
    pw = [(X(a), Y(AF(math.radians(a)) ** 2)) for a in range(0, 181)]
    card = (t(250, 16, 'array field and power against θ', 'pt', col=AC) + axes(44, 26, 444, 124) + curve(xy, AC, 3) + curve(pw, AC2, 2.5)
            + dot(X(th_max), Y(1), AC, 6) + dot(X(th_null), Y(0), AC2, 6) + dot(X(0), Y(f0), AC, 5) + dot(X(0), Y(f0 ** 2), AC2, 5)
            + t(X(th_max) + 10, Y(1) + 4, 'max', anchor='start', col=AC) + t(38, Y(f0) + 5, f(f0, 3), anchor='end', col=AC) + t(38, Y(.5) + 12, '0.5', anchor='end', col=AC2)
            + t(X(0), 140, '0°') + t(X(th_null), 140, f'{f(th_null, 0)}°', col=AC2) + t(X(90), 140, '90°') + t(X(th_max), 140, f'{f(th_max, 0)}°', col=AC) + t(X(180), 140, '180°'))
    card = svg(card)
    return spec('ec-antenna-u3-L1', 'Antenna<br>Arrays',
                'Add <span class="gold">FIELDS</span>, then square:<br><span class="cyan">4×</span> the power of one',
                'two sources, λ/2 apart', card, brd,
                chips(('left', 300, 'c', 'd = λ/2'), ('left', 364, 'c', 'α = 90° lead'), ('left', 520, 'g', f'θ = 0°: field {f(f0, 3)}'),
                      ('right', 300, 'g', f'max at θ = {f(th_max, 0)}°'), ('right', 530, 'c', f'null at θ = {f(th_null, 0)}°', False)),
                f'ψ = π cos θ + π/2: ψ = 0 at <b class="gl">{f(th_max, 0)}°</b>, ψ = π at <b class="cl">{f(th_null, 0)}°</b><br>'
                f'at {f(th_max, 0)}° the fields add: (E + E)² = <b class="gl">4E²</b>, four times one')


def u3_l2():
    """3.4 worked example 1: 3-element Yagi for 500 MHz (and worked example 2's LPDA band for contrast)"""
    fr = 500e6
    lam = C / fr * 1000                                       # mm
    Lr, Ld, Ldir = .50 * lam, .47 * lam, .45 * lam
    sr, sd = .25 * lam, .20 * lam
    boom = sr + sd
    band = (fr * .98 / 1e6, fr * 1.02 / 1e6)                  # 2 % either side reading of "2 to 5 %": 490 to 510 MHz
    assert (f(lam, 0), f(Lr, 0), f(Ld, 0), f(Ldir, 0), f(sr, 0), f(sd, 0), f(boom, 0), f(band[0], 0), f(band[1], 0)) == ('600', '300', '282', '270', '150', '120', '270', '490', '510')
    # board: the boom along x, three elements across (y), drawn to scale at 1 unit = 60 mm
    at(30, 0)
    u = 60
    xb = 1.6
    xs = [xb, xb + sr / u, xb + boom / u]
    cy, zz = 4.0, 1.2
    parts = [rod((xb - .5, cy, zz), (xs[2] + .5, cy, zz), '#8E97A6', 7), rod((4.0, cy, 0), (4.0, cy, zz - .1), '#6E6A92', 6)]
    for x, L, col in zip(xs, (Lr, Ld, Ldir), ('#C9CED8', AC, '#C9CED8')):
        if col == AC:
            parts.append(rod((x, cy - L / u / 2, zz + .12), (x, cy - .1, zz + .12), AC, 7))
            parts.append(rod((x, cy + .1, zz + .12), (x, cy + L / u / 2, zz + .12), AC, 7))
        else:
            parts.append(rod((x, cy - L / u / 2, zz + .12), (x, cy + L / u / 2, zz + .12), col, 7))
    parts += [lab((xs[0], cy - Lr / u / 2 - .3, zz + .3), 'reflector', INK, 14), lab((xs[2], cy + Ldir / u / 2 + .35, zz), 'director', INK, 14, dy=16),
              glow(arr3((xs[2] + .7, cy, zz + .1), (7.6, cy, zz + .1), AC2, 5))]
    brd = board(parts)
    H = lambda mm: mm / 320 * 76
    left = t(118, 16, 'element lengths, mm', 'pt', col=AC) + f'<line x1="20" y1="122" x2="222" y2="122" stroke="{AX}" stroke-width="1.5"/>'
    for k, (nm, L, col) in enumerate((('refl.', Lr, '#C9CED8'), ('driven', Ld, AC), ('dir.', Ldir, '#C9CED8'))):
        x = 34 + k * 64
        left += rect(x, 122 - H(L), 44, H(L), col, .85, 3) + t(x + 22, 122 - H(L) - 6, f(L, 0), 'pt', col=col) + t(x + 22, 140, nm)
    X = lambda mhz: 250 + (mhz - 150) / 500 * 210
    right = (t(355, 16, 'band covered, MHz', 'pt', col=AC2) + f'<line x1="250" y1="104" x2="460" y2="104" stroke="{AX}" stroke-width="1.5"/>'
             + rect(X(band[0]), 40, X(band[1]) - X(band[0]), 22, AC, 1, 2) + t(X(band[0]) - 8, 57, 'Yagi 490–510', 'pt', 'end', AC)
             + rect(X(200), 72, X(600) - X(200), 22, AC2, .7, 3) + t((X(200) + X(600)) / 2, 88, 'LPDA 200–600', 'pt', col='#0E2A26'))
    for m in (200, 400, 600):
        right += t(X(m), 122, str(m))
    card = svg(left + right)
    return spec('ec-antenna-u3-L2', 'Yagi, Horn<br>&amp; Dish<br>Antennas',
                'A Yagi is <span class="gold">NARROW</span>, 2–5 %;<br>wide band needs an <span class="cyan">LPDA</span>',
                '3-element Yagi, 500 MHz', card, brd,
                chips(('left', 300, 'c', f'λ = {f(lam, 0)} mm'), ('left', 364, 'c', f'reflector {f(Lr, 0)} mm'), ('left', 520, 'g', f'driven {f(Ld, 0)} mm'),
                      ('right', 300, 'c', f'director {f(Ldir, 0)} mm'), ('right', 530, 'g', 'about 7 dBi', False)),
                f'0.50λ, 0.47λ, 0.45λ = <b class="gl">{f(Lr, 0)}, {f(Ld, 0)}, {f(Ldir, 0)} mm</b><br>'
                f'2 to 5 % band: <b class="cl">about {f(band[0], 0)} to {f(band[1], 0)} MHz</b>')


def u3_l3():
    """3.7 worked example 1: rectangular patch for 2.4 GHz on FR-4, er = 4.4, h = 1.6 mm"""
    fr, er, h = 2.4e9, 4.4, 1.6
    half = C / (2 * fr) * 1000                                # mm
    W = half * math.sqrt(2 / (er + 1))
    ee = (er + 1) / 2 + (er - 1) / 2 / math.sqrt(1 + 12 * h / W)
    dL = .412 * h * (ee + .3) * (W / h + .264) / ((ee - .258) * (W / h + .8))
    lg2 = half / math.sqrt(ee)
    L = lg2 - 2 * dL
    fchk = C / (2 * (L + 2 * dL) / 1000 * math.sqrt(ee))
    assert (f(W, 1), f(ee, 2), f(dL, 2), f(lg2, 2), f(L, 1), f(fchk / 1e9, 2), f(half, 1)) == ('38', '4.09', '0.74', '30.92', '29.4', '2.4', '62.5')
    # board: FR-4 board with copper ground, the patch to scale (1 unit = 8 mm), a 50 ohm feed line
    at(10, 0)
    u = 8
    x0, y0 = 1.3, 1.5
    pw, pl = L / u, W / u                                     # patch length along x (resonant), width along y
    parts = [box(.6, .8, 6.8, 6.4, .12, '#C98A4B', '#8A5A2E', '#A86F3A'),
             box(.6, .8, 6.8, 6.4, .42, '#3E7A55', '#244A33', '#2E5E41', z0=.12)]
    zt = .55
    parts.append(poly([(x0, y0, zt), (x0 + pw, y0, zt), (x0 + pw, y0 + pl, zt), (x0, y0 + pl, zt)], '#E7B46A', '#FFD79A', 2))
    for xe in (x0, x0 + pw):                                  # the two radiating edges, fringing glow
        parts.append(glow(ln((xe, y0, zt), (xe, y0 + pl, zt), AC2, 4)))
    fy = y0 + pl / 2
    parts.append(poly([(x0 + pw, fy - .19, zt), (7.4, fy - .19, zt), (7.4, fy + .19, zt), (x0 + pw, fy + .19, zt)], '#E7B46A', '#FFD79A', 1.5))
    parts += [ln((x0, y0 - .45, zt), (x0 + pw, y0 - .45, zt), AC, 2.5), lab((x0 + pw / 2, y0 - .7, zt), f'L = {f(L, 1)} mm', AC, 16),
              lab((x0 - .1, y0 + pl / 2, zt + .1), f'W = {f(W, 1)}', INK, 15, 'end')]
    brd = board(parts)
    Hh = lambda mm: mm / 70 * 300
    left = t(30, 16, 'length, mm', 'pt', 'start', AC)
    for k, (nm, v, col) in enumerate((('λ₀/2 in air', half, '#8C86B8'), ('λg/2 on the board', lg2, AC2), ('patch L', L, AC))):
        y = 34 + k * 36
        left += rect(30, y, Hh(v), 24, col, .85, 4) + t(30 + Hh(v) + 8, y + 18, f(v, 2 if k == 1 else 1), 'pt', 'start', col) + t(36, y + 17, nm, 'ax', 'start', '#17112E', 'style="font-weight:700"')
    card = svg(left + t(440, 140, f'f = {f(fchk / 1e9, 2)} GHz', 'ax', 'end', INK))
    return spec('ec-antenna-u3-L3', 'Patch<br>Antennas &amp;<br>Propagation',
                f'About <span class="gold">29.4 mm</span>: the<br>board <span class="cyan">SLOWS</span> the wave',
                '2.4 GHz patch, FR-4', card, brd,
                chips(('left', 300, 'c', 'ε<sub>r</sub> = 4.4, h = 1.6 mm'), ('left', 364, 'c', f'W = {f(W, 1)} mm'), ('left', 520, 'c', f'ε<sub>eff</sub> = {f(ee, 2)}'),
                      ('right', 300, 'g', f'L = {f(L, 1)} mm'), ('right', 530, 'c', f'ΔL = {f(dL, 2)} mm', False)),
                f'λ<sub>g</sub>/2 = 62.5 ÷ √{f(ee, 3)} = {f(lg2, 2)} mm, ΔL = {f(dL, 3)} mm<br>'
                f'L = {f(lg2, 2)} − 2 × {f(dL, 3)} = <b class="gl">{f(L, 2)} mm</b>, not <b class="cl">{f(half, 1)} mm</b>')


# ================================================================== unit 4
def u4_l1():
    """4.1 worked example 1: two-port with S11 = 0.2, S21 = 0.9 at -30 deg, S12 = 0, S22 = 0.1"""
    S11, S21, S12, S22 = .2, .9, 0, .1
    RL = -20 * math.log10(S11)
    IL = -20 * math.log10(S21)
    vs = (1 + S11) / (1 - S11)
    assert (f(RL, 2), f(IL, 2), f(vs, 1)) == ('13.98', '0.92', '1.5')
    # board: the two-port box with ports 1 and 2; a1 in, b1 back (0.2), b2 out (0.9), nothing from 2 back to 1
    at(30, 0)
    parts = [rod((.5, 4.0, .9), (2.5, 4.0, .9), '#C9CED8', 9), rod((5.5, 4.0, .9), (7.5, 4.0, .9), '#C9CED8', 9),
             box(2.5, 2.9, 3.0, 2.2, 1.8, '#3A3470', '#1A1640', '#262058'),
             lab((4.0, 4.0, 1.8), '[S]', AC, 22, dy=8), lab((1.4, 5.0, .2), 'port 1', INK, 14), lab((6.5, 5.0, .2), 'port 2', INK, 14)]
    parts += [glow(arr3((.4, 3.2, 1.6), (2.3, 3.2, 1.6), AC, 6)), lab((1.0, 2.6, 1.9), 'a₁', AC, 17),
              arr3((2.3, 4.8, 1.3), (1.0, 4.8, 1.3), '#B9B2E6', 3), lab((1.4, 5.5, 1.0), 'b₁: 0.2', '#B9B2E6', 14),
              glow(arr3((5.7, 3.2, 1.6), (7.7, 3.2, 1.6), AC2, 6)), lab((6.7, 2.6, 2.3), 'b₂: 0.9', AC2, 17)]
    brd = board(parts)
    tbl = ('<table><tr><th></th><th>in at port 1</th><th>in at port 2</th></tr>'
           f'<tr><td>out at port 1</td><td>S₁₁ = 0.2∠0°</td><td>S₁₂ = 0</td></tr>'
           f'<tr><td>out at port 2</td><td style="color:{AC};font-weight:700">S₂₁ = 0.9∠−30°</td><td>S₂₂ = 0.1∠0°</td></tr></table>')
    return spec('ec-antenna-u4-L1', 'S-parameters,<br>Tees &amp;<br>Couplers',
                '<span class="gold">S₂₁</span>: out at 2, in at 1:<br>read the indices <span class="cyan">BACKWARD</span>',
                'a 50 Ω two-port', tbl, brd,
                chips(('left', 300, 'c', 'S₁₁ = 0.2∠0°'), ('left', 364, 'c', 'S₁₂ = 0'), ('left', 520, 'c', f'VSWR {f(vs, 1)}'),
                      ('right', 300, 'g', 'S₂₁ = 0.9∠−30°'), ('right', 530, 'g', f'IL = {f(IL, 2)} dB', False)),
                f'S₂₁ = b₂/a₁ = 0.9: IL = <b class="gl">{f(IL, 2)} dB</b><br>'
                f'RL = <b class="cl">{f(RL, 2)} dB</b>; S₁₂ = 0 ≠ S₂₁: not reciprocal', TABLE_CSS)


def u4_l2():
    """4.4 worked example 1: 20 dBm source, matched 6 dB pad, equal Wilkinson divider"""
    Pin = 10 ** (20 / 10)
    Pp = Pin * 10 ** (-6 / 10)
    heat = Pin - Pp
    each = Pp / 2
    dbm = 10 * math.log10(each)
    both = 10 * math.log10(Pin + Pin)                          # 100 mW + 100 mW, the hook's sum
    assert (f(Pin, 0), f(Pp, 2), f(heat, 2), f(each, 2), f(dbm, 2), f(both, 0)) == ('100', '25.12', '74.88', '12.56', '10.99', '23')
    # board: source, the 6 dB pad, a Wilkinson (two lambda/4 arms and the 100 ohm resistor), two matched loads
    at(0, 0)
    parts = []
    x, y = Bp(820, 455)
    parts.append(block(x - .7, y - .7, 1.4, 1.4, 1.0, DARK, '20 dBm', AC, 14))
    parts.append(rod((*Bp(850, 455), .3), (*Bp(880, 455), .3), '#E7B46A', 6))
    x, y = Bp(905, 455)
    parts.append(block(x - .6, y - .6, 1.2, 1.2, .8, ('#6E6A92', '#3A3470', '#4E4888'), '6 dB', INK, 16))
    parts.append(rod((*Bp(930, 455), .3), (*Bp(965, 455), .3), '#E7B46A', 6))
    for sgn in (-1, 1):
        arm = [Bp(965 + 85 * math.sin(math.pi / 2 * i / 30), 455 + sgn * 42 * (1 - math.cos(math.pi / 2 * i / 30))) for i in range(31)]
        parts.append(glow(pline([(x_, y_, .3) for x_, y_ in arm], AC, 6)))
        parts.append(rod((*Bp(1050, 455 + sgn * 42), .3), (*Bp(1095, 455 + sgn * 42), .3), '#E7B46A', 6))
        px, py = P(*Bp(1110, 455 + sgn * 42))
        parts.append(cyl(px, py, 15, 8, 40, '#8E97A6', '#C9CED8'))
    parts.append(ln((*Bp(1050, 413), .35), (*Bp(1050, 497), .35), '#120F31', 9))
    parts.append(lab((*Bp(1050, 455), .4), '100 Ω', AC2, 14, 'start', dy=5).replace('text-anchor="start"', 'text-anchor="start" dx="10"'))
    brd = board(parts)
    W = lambda mw: mw / 100 * 300
    card = t(30, 16, 'power, mW', 'pt', 'start', AC)
    for k, (nm, v, col) in enumerate((('source', Pin, '#8C86B8'), ('after pad', Pp, AC), ('each output', each, AC2), ('pad heat', heat, '#5B52A0'))):
        y = 28 + k * 28
        card += rect(110, y, W(v), 20, col, .9, 3) + t(104, y + 15, nm, 'ax', 'end') + t(110 + W(v) + 6, y + 15, f(v, 2), 'pt', 'start', col)
    card = svg(card)
    return spec('ec-antenna-u4-L2', 'Dividers,<br>Ferrites &amp;<br>Tubes',
                'dBm do not <span class="gold">ADD</span>:<br>double the power, <span class="cyan">+3 dB</span>',
                '20 dBm, pad, Wilkinson', card, brd,
                chips(('left', 300, 'g', f'20 dBm = {f(Pin, 0)} mW'), ('left', 364, 'c', '6 dB pad: 14 dBm'), ('left', 520, 'c', f'pad heat {f(heat, 1)} mW'),
                      ('right', 300, 'g', f'{f(each, 2)} mW each'), ('right', 530, 'c', f'{f(dbm, 2)} dBm = 14 − 3', False)),
                f'20 − 6 = 14 dBm = {f(Pp, 2)} mW → <b class="gl">{f(each, 2)} mW</b> each<br>'
                f'−3 dB halves; 100 + 100 mW = 200 mW = <b class="cl">{f(both, 0)} dBm</b>')


def u4_l3():
    """4.7 worked example 1: GaAs Gunn diode, transit-time mode at 10 GHz"""
    fr, vd, Eth, Vb, I, Prf = 10e9, 1e5, 3.2e5, 8, .5, .1       # vd in m/s, Eth in V/m
    L = vd / fr
    Vth = Eth * L
    Eb = Vb / L
    n0 = 1e12 / (L * 100)
    eta = Prf / (Vb * I)
    assert (f(L * 1e6, 0), f(Vth, 1), f(Eb / 1e5, 0), f(eta * 100, 1), n0) == ('10', '3.2', '8', '2.5', 1e15)
    # board: a bulk n-GaAs slab between two metal contacts, the bias, a travelling domain
    at(40, 10)
    parts = [box(1.2, 2.6, .5, 2.8, 2.0, *METAL), box(1.7, 2.6, 4.4, 2.8, 2.0, '#4E7FA8', '#264A6B', '#335D84'),
             box(6.1, 2.6, .5, 2.8, 2.0, *METAL)]
    parts.append(glow(poly([(4.2, 2.6, 2.0), (4.7, 2.6, 2.0), (4.7, 5.4, 2.0), (4.2, 5.4, 2.0)], AC, AC, 1, 'fill-opacity=".55"')))
    parts.append(glow(poly([(4.2, 5.4, 2.0), (4.7, 5.4, 2.0), (4.7, 5.4, 0), (4.2, 5.4, 0)], AC, AC, 1, 'fill-opacity=".45"')))
    parts += [lab((3.9, 4.0, 2.0), 'n-GaAs', '#E6F2FF', 17, dy=6), glow(arr3((4.9, 6.0, .4), (6.0, 6.0, .4), AC2, 4)),
              ln((1.7, 2.2, 2.0), (6.1, 2.2, 2.0), AC, 2.5), lab((3.9, 2.2, 2.0), 'L = 10 µm', AC, 16, dy=-10),
              rod((.9, 4.0, 1.0), (.2, 4.0, 1.0), '#E7B46A', 4), rod((6.9, 4.0, 1.0), (7.6, 4.0, 1.0), '#E7B46A', 4)]
    brd = board(parts)
    X = lambda e: 44 + e / 12 * 200
    vE = lambda e: (2 * e / 3.2 if e <= 3.2 else 1 + 1 * math.exp(-(e - 3.2) / 1.6))   # GaAs shape: rise, peak at threshold, fall
    left = (t(150, 16, 'GaAs drift velocity against E', 'pt', col=AC) + axes(44, 26, 244, 124)
            + curve([(X(e), 124 - vE(e) / 2.1 * 92) for e in [12 * i / 120 for i in range(121)]], AC, 3)
            + vline(X(3.2), 34, 124, AC2, '4 4') + vline(X(8), 50, 124, AC, '4 4') + dot(X(8), 124 - vE(8) / 2.1 * 92, AC, 6)
            + t(X(3.2), 140, '3.2', col=AC2) + t(X(8), 140, '8', col=AC) + t(244, 140, 'kV/cm', anchor='end') + t(38, 34, 'v', anchor='end')
            + t(X(5.6), 56, 'falls: −R', col=INK))
    right = t(362, 16, 'the 10 GHz diode', 'pt', col=AC2)
    for k, (a, b, col) in enumerate((('active length', '10 µm', AC), ('threshold', f'{f(Vth, 1)} V', INK), ('doping', 'n₀ > 10¹⁵ cm⁻³', INK), ('efficiency', f'{f(eta * 100, 1)} %', AC2))):
        right += t(270, 46 + k * 27, a, 'ax', 'start', '#B9B2E6', 'style="font-size:15px"') + t(462, 46 + k * 27, b, 'pt', 'end', col)
    card = svg(left + right)
    return spec('ec-antenna-u4-L3', 'Diode<br>Sources &amp;<br>MMICs',
                '<span class="gold">NO</span> junction: a bulk<br>n-GaAs slab, <span class="cyan">two</span> valleys',
                '10 GHz Gunn diode', card, brd,
                chips(('left', 300, 'c', 'v<sub>d</sub> = 10⁷ cm/s'), ('left', 364, 'g', f'L = {f(L * 1e6, 0)} µm'), ('left', 520, 'c', f'V<sub>th</sub> = {f(Vth, 1)} V'),
                      ('right', 300, 'g', '8 V → 8 kV/cm'), ('right', 530, 'c', f'η = {f(eta * 100, 1)} %', False)),
                f'L = v<sub>d</sub>/f = 10⁵ ÷ 10¹⁰ = <b class="gl">10 µm</b>, V<sub>th</sub> = {f(Vth, 1)} V<br>'
                f'8 V across 10 µm: <b class="cl">8 kV/cm</b>, past the 3.2 peak')


# ================================================================== unit 5
def u5_l1():
    """5.2 worked example 1: LNA (15 dB, 2 dB), mixer (10 dB, 12 dB), IF amp (20 dB, 10 dB)"""
    G1, G2 = 10 ** 1.5, 10 ** 1.0
    F1, F2, F3 = 10 ** .2, 10 ** 1.2, 10 ** 1.0
    t1, t2, t3 = F1, (F2 - 1) / G1, (F3 - 1) / (G1 * G2)
    F = t1 + t2 + t3
    NF = 10 * math.log10(F)
    Te = (F - 1) * 290
    floor = -174 + 70 + NF
    assert (f(t1, 3), f(t2, 3), f(t3, 4), f(F, 3), f(NF, 2), f(Te, 0), f(floor, 1), f(floor + 10, 1)) == ('1.585', '0.47', '0.0285', '2.083', '3.19', '314', '-100.8', '-90.8')
    # board: three stages in a chain, LNA - mixer (with LO) - IF amplifier, laid across the board
    at(0, 0)
    a0, a1 = Bp(790, 470), Bp(1115, 470)
    parts = [rod((*a0, .5), (*a1, .5), '#E7B46A', 4)]
    for px, nm, col in ((840, 'LNA', (AC, '#5B45B0', '#7A62D6')), (955, 'mixer', DARK), (1070, 'IF amp', DARK)):
        x, y = Bp(px, 470)
        parts.append(block(x - .75, y - .75, 1.5, 1.5, 1.1, col, nm, '#17112E' if col[0] == AC else INK, 16))
    lx, ly = Bp(1000, 545)
    mx, my = Bp(955, 470)
    parts += [rod((lx, ly, .35), (mx + .5, my + .5, .35), AC2, 4), block(lx - .5, ly - .5, 1.0, 1.0, .7, DARK, 'LO', AC2, 15)]
    brd = board(parts)
    W = lambda v: v / 1.7 * 270
    card = t(30, 16, 'share of the noise factor F = 2.083', 'pt', 'start', AC)
    for k, (nm, v, col, pc) in enumerate((('LNA', t1, AC, 76), ('mixer', t2, AC2, 23), ('IF amp', t3, '#8C86B8', 1))):
        y = 32 + k * 32
        card += rect(100, y, max(W(v), 3), 22, col, .9, 3) + t(92, y + 17, nm, 'ax', 'end') + t(100 + max(W(v), 3) + 8, y + 17, f'{f(v, 3)} ({pc} %)', 'pt', 'start', col)
    card += t(100, 140, 'the LNA’s 15 dB gain divides the rest by 31.6', 'ax', 'start', '#B9B2E6')
    card = svg(card)
    return spec('ec-antenna-u5-L1', 'Q, Noise<br>Figure &amp; IIP3',
                'Add <span class="gold">LINEAR</span> F, not dB:<br>the <span class="cyan">LNA</span> sets the noise',
                'three-stage receiver', card, brd,
                chips(('left', 300, 'g', 'LNA: 15 dB, NF 2 dB'), ('left', 364, 'c', 'mixer: 10 dB, NF 12 dB'), ('left', 520, 'c', 'IF: 20 dB, NF 10 dB'),
                      ('right', 300, 'g', f'NF = {f(NF, 2)} dB'), ('right', 530, 'c', f'T<sub>e</sub> = {f(Te, 0)} K', False)),
                f'F = {f(t1, 3)} + 14.85/31.62 + 9/316.2 = <b class="cl">{f(F, 3)}</b><br>'
                f'NF = 10 log {f(F, 3)} = <b class="gl">{f(NF, 2)} dB</b>, not 2 + 12 = 14 dB')


def u5_l2():
    """5.4 worked example 1: 900 MHz receiver, 45 MHz IF, high-side LO, one Q = 50 preselector"""
    frf, fif, Q = 900, 45, 50
    flo = frf + fif
    fim = flo + fif
    rho = fim / frf - frf / fim
    rej = 20 * math.log10(math.sqrt(1 + (Q * rho) ** 2))
    left_ = -20 - rej - (-80)
    assert (flo, fim, f(rej, 1), f(left_, 1)) == (945, 990, '19.6', '40.4')
    # board: the frequency plan standing on the board: wanted 900, LO 945, image 990 before and after the preselector
    at(0, 0)
    F = lambda mhz: Bp(845 + (mhz - 870) / 140 * 290, 505)
    H = lambda dbm: (dbm + 100) / 22                         # bar height in board units above a -100 dBm floor
    parts = [rod((*F(865), .02), (*F(1012), .02), '#8C86B8', 3)]
    for mhz in range(880, 1011, 10):
        parts.append(ln((*F(mhz), 0), (*F(mhz), .25), '#8C86B8', 2))
    x, y = F(fim)
    parts.append(box(x - .2, y - .2, .4, .4, H(-20), 'none', 'none', 'none'))
    parts.append(poly([(x - .2, y + .2, 0), (x + .2, y + .2, 0), (x + .2, y + .2, H(-20)), (x - .2, y + .2, H(-20))], 'none', AC2, 2, 'stroke-dasharray="5 4" opacity=".8"'))
    parts.append(box(x - .2, y - .2, .4, .4, H(-20 - rej), AC2, '#1E8F7F', '#2BB5A1'))
    parts.append(glow(arr3((x + .5, y - .5, H(-20) - .05), (x + .5, y - .5, H(-20 - rej) + .15), AC2, 3)))
    x, y = F(frf)
    parts.append(glow(box(x - .2, y - .2, .4, .4, H(-80), AC, '#5B45B0', '#7A62D6')))
    x, y = F(flo)
    parts.append(ln((x, y, 0), (x, y, 3.2), INK, 2.5, 'stroke-dasharray="6 5"'))
    parts += [lab((*F(frf), 0), '900', AC, 17, dy=24), lab((*F(flo), 0), 'LO 945', INK, 16, dy=24), lab((*F(fim), 0), '990', AC2, 17, dy=24),
              lab((*F(flo), 3.2), '±45', '#B9B2E6', 15, dy=-8)]
    brd = board(parts)
    X = lambda mhz: 30 + (mhz - 860) / 150 * 424
    Y = lambda db: 34 + -db / 30 * 84
    resp = [(X(m), Y(max(-30, -20 * math.log10(math.sqrt(1 + (Q * (m / frf - frf / m)) ** 2))))) for m in [860 + 150 * i / 300 for i in range(301)]]
    card = (t(30, 16, 'frequency plan, MHz', 'pt', 'start', AC) + curve(resp, '#8C86B8', 2.5)
            + f'<line x1="30" y1="122" x2="454" y2="122" stroke="{AX}" stroke-width="1.5"/>'
            + vline(X(frf), 30, 122, AC, 'none', 4) + vline(X(flo), 54, 122, INK, '6 4', 2) + vline(X(fim), Y(-rej), 122, AC2, 'none', 4)
            + dot(X(fim), Y(-rej), AC2, 5) + t(X(fim) - 10, 114, f'−{f(rej, 1)} dB', 'pt', 'end', AC2)
            + t(X(frf), 140, '900', col=AC) + t(X(flo), 140, 'LO 945', col=INK) + t(X(fim), 140, '990', col=AC2)
            + f'<path d="M{X(frf):.1f} 50H{X(flo):.1f}M{X(flo):.1f} 50H{X(fim):.1f}" stroke="#B9B2E6" stroke-width="1.5"/>'
            + t((X(frf) + X(flo)) / 2, 46, '45', col='#B9B2E6') + t((X(flo) + X(fim)) / 2, 46, '45', col='#B9B2E6'))
    card = svg(card)
    return spec('ec-antenna-u5-L2', 'Receivers,<br>Transmitters<br>&amp; LNAs',
                'Image sits <span class="gold">2 IF</span> away,<br>beyond the <span class="cyan">LO</span>',
                '900 MHz, 45 MHz IF', card, brd,
                chips(('left', 300, 'c', f'f<sub>RF</sub> = {frf} MHz'), ('left', 364, 'c', f'f<sub>LO</sub> = {flo} MHz'), ('left', 520, 'c', f'Q = {Q}: −{f(rej, 1)} dB'),
                      ('right', 300, 'g', f'image {fim} MHz'), ('right', 530, 'g', f'still +{f(left_, 1)} dB', False)),
                f'f<sub>LO</sub> = {flo} MHz; image = {flo} + 45 = <b class="gl">{fim} MHz</b><br>'
                f'Q = 50 rejects <b class="cl">{f(rej, 1)} dB</b>: still {f(left_, 1)} dB above')


def u5_l3():
    """5.9 worked example 2: the 2 GHz VCO in a PLL with a 10 MHz crystal reference"""
    f0, F, Ps, QL, fc, T0 = 2e9, 2, 1e-3, 8, 100e3, 290
    k = 1.380649e-23
    leeson = lambda df: 10 * math.log10(2 * F * k * T0 / Ps * (1 + (f0 / (2 * QL * df)) ** 2) * (1 + fc / df))
    N = f0 / 10e6
    add = 20 * math.log10(N)
    ref = -155 + add
    assert (N, f(add, 1), f(ref, 1), f(leeson(10e3), 1), f(leeson(100e3), 1), f(leeson(1e6), 1)) == (200, '46', '-109', '-75.6', '-103', '-125.6')
    # board: crystal, phase detector, loop filter, VCO, and the divide-by-200 in the feedback path
    at(0, 0)
    blocks = [(878, 440, '10 MHz', DARK, AC2, 13), (954, 440, 'PD', DARK, INK, 16), (1030, 440, 'filter', DARK, INK, 14),
              (1106, 440, 'VCO', (AC, '#5B45B0', '#7A62D6'), '#17112E', 16)]
    parts = []
    for px, py, nm, cols, lc, sz in blocks:
        x, y = Bp(px, py)
        parts.append(block(x - .6, y - .6, 1.2, 1.2, .8, cols, nm, lc, sz))
    for a, b in ((898, 934), (974, 1010), (1050, 1086)):
        parts.append(rod((*Bp(a, 440), .4), (*Bp(b, 440), .4), '#E7B46A', 4))
    path = [Bp(1106, 455), Bp(1106, 525), Bp(1050, 525)]
    parts.append(pline([(x, y, .3) for x, y in path], '#E7B46A', 4))
    parts.append(pline([(x, y, .3) for x, y in (Bp(985, 525), Bp(954, 525), Bp(954, 455))], '#E7B46A', 4))
    x, y = Bp(1015, 525)
    parts.append(block(x - .8, y - .8, 1.6, 1.6, .9, (AC2, '#1E8F7F', '#2BB5A1'), '÷ 200', '#0E2A26', 18))
    parts.append(glow(arr3(*[(*Bp(px, 440), 1.2) for px in (1128, 1172)], AC, 4)))
    brd = board(parts)
    X = lambda df: 62 + (math.log10(df) - 4) / 3 * 392
    Y = lambda db: 28 + (-70 - db) / 65 * 96
    vco = [(X(10 ** e), Y(leeson(10 ** e))) for e in [4 + 3 * i / 120 for i in range(121)]]
    out = [(X(10 ** e), Y(ref if 10 ** e < 176e3 else leeson(10 ** e))) for e in [4 + 3 * i / 120 for i in range(121)]]
    card = (t(250, 16, 'phase noise, dBc/Hz, against offset', 'pt', col=AC) + axes(62, 24, 454, 124)
            + curve(vco, '#8C86B8', 2, 'stroke-dasharray="6 4"') + hline(62, 454, Y(ref), AC2, '4 4', 1.6) + curve(out, AC, 3.5)
            + t(56, Y(ref) + 5, neg(f(ref, 0)), anchor='end', col=AC2) + t(56, Y(leeson(1e6)) + 5, neg(f(leeson(1e6), 1)), anchor='end', col=AC)
            + dot(X(1e6), Y(leeson(1e6)), AC, 5) + t(X(1.5e4), Y(leeson(1.5e4)) - 4, 'free VCO', 'ax', 'start')
            + t(X(1.2e4), Y(ref) + 18, 'PLL output', 'pt', 'start', AC)
            + t(X(1e4), 140, '10 kHz') + t(X(1e5), 140, '100 kHz') + t(X(1e6), 140, '1 MHz') + t(454, 140, '10 MHz', anchor='end'))
    card = svg(card)
    return spec('ec-antenna-u5-L3', 'Mixers, PAs<br>&amp; Oscillators',
                'Noise grows <span class="gold">20 log N</span>:<br><span class="cyan">46 dB</span> for ×200',
                '2 GHz PLL, 10 MHz ref', card, brd,
                chips(('left', 300, 'g', f'N = 2000/10 = {f(N, 0)}'), ('left', 364, 'c', 'ref −155 dBc/Hz'), ('left', 520, 'c', 'loop ≈ 180 kHz'),
                      ('right', 300, 'g', f'+{f(add, 1)} dB'), ('right', 530, 'c', f'{neg(f(leeson(1e6), 1))} at 1 MHz', False)),
                f'20 log₁₀ 200 = <b class="gl">{f(add, 1)} dB</b> (phase × N), not 23<br>'
                f'ref −155 + {f(add, 0)} = <b class="cl">{neg(f(ref, 0))} dBc/Hz</b> in the loop')


# ================================================================== unit 6
def radar_dish(x, y, z=1.7, r=1.0, plane='yz'):
    return [rod((x, y, 0), (x, y, z - .4), '#8E97A6', 8), block(x - .45, y - .45, .9, .9, .3, DARK),
            poly(circ((x + (.15 if plane == 'yz' else 0), y + (.15 if plane == 'xz' else 0), z), r, plane), '#D9DDE6', '#9AA3B2', 2),
            poly(circ((x + (.15 if plane == 'yz' else 0), y + (.15 if plane == 'xz' else 0), z), r * .65, plane), '#C3C9D4')]


def jet(cx, cy, cz, col='#E6EAF2'):
    """a small aircraft seen from above: fuselage along -y, wings along x"""
    body = [(cx, cy - 1.0, cz), (cx + .16, cy - .6, cz), (cx + .16, cy + .9, cz), (cx, cy + 1.05, cz), (cx - .16, cy + .9, cz), (cx - .16, cy - .6, cz)]
    wing = [(cx - 1.1, cy + .15, cz), (cx + 1.1, cy + .15, cz), (cx + 1.1, cy + .4, cz), (cx, cy - .2, cz), (cx - 1.1, cy + .4, cz)]
    tail = [(cx - .45, cy + .85, cz), (cx + .45, cy + .85, cz), (cx, cy + .65, cz)]
    return poly(wing, col, '#9AA3B2', 1.5) + poly(tail, col, '#9AA3B2', 1.5) + poly(body, '#F4F6FA', '#9AA3B2', 1.5)


def u6_l1():
    """6.1 worked example 1: 1 us pulse, echo after 124 us"""
    t_, tau = 124e-6, 1e-6
    R = C * t_ / 2
    cl = C * tau
    dR = cl / 2
    assert (f(R / 1e3, 1), f(cl, 0), f(dR, 0), f(C * t_ / 1e3, 1)) == ('18.6', '300', '150', '37.2')
    at(30, 0)
    parts = radar_dish(1.8, 5.6, 1.8, 1.0, 'yz')
    parts += [jet(6.0, 1.8, 3.2), glow(arr3((2.6, 4.6, 2.6), (5.3, 2.1, 3.2), AC, 6)), glow(arr3((5.6, 3.1, 2.6), (3.0, 5.5, 1.9), AC2, 4)),
              lab((4.6, 4.3, 3.4), 'out', AC, 16), lab((4.4, 5.1, 1.4), 'back', AC2, 16)]
    brd = board(parts)
    X = lambda us: 30 + us / 150 * 424
    card = (t(30, 16, 'what the receiver sees, µs', 'pt', 'start', AC) + f'<line x1="30" y1="100" x2="454" y2="100" stroke="{AX}" stroke-width="1.5"/>'
            + rect(X(0), 40, max(X(1) - X(0), 5), 60, AC, 1, 1) + rect(X(124), 74, max(X(125) - X(124), 5), 26, AC2, 1, 1)
            + t(X(0) + 10, 56, 'pulse, 1 µs', 'pt', 'start', AC) + t(X(124) - 8, 90, 'echo', 'pt', 'end', AC2)
            + f'<path d="M{X(0):.1f} 116H{X(124):.1f}M{X(0):.1f} 110V122M{X(124):.1f} 110V122" stroke="{INK}" stroke-width="2"/>'
            + t((X(0) + X(124)) / 2, 112, '124 µs, out and back', 'ax', col=INK)
            + t(X(0), 140, '0') + t(X(124), 140, '124', col=AC2) + t(X(150), 140, '150', anchor='end'))
    card = svg(card)
    return spec('ec-antenna-u6-L1', 'Radar Range<br>&amp; Cross<br>Section',
                'The echo goes <span class="gold">OUT</span><br>and comes <span class="cyan">BACK</span>: halve it',
                'echo at 124 µs', card, brd,
                chips(('left', 300, 'g', 't = 124 µs'), ('left', 364, 'c', 'τ = 1 µs'), ('left', 520, 'c', f'cτ = {f(cl, 0)} m'),
                      ('right', 300, 'g', f'R = {f(R / 1e3, 1)} km'), ('right', 530, 'c', f'ΔR = {f(dR, 0)} m', False)),
                f'R = ct/2 = {f(C * t_ / 1e3, 1)} km ÷ 2 = <b class="gl">{f(R / 1e3, 1)} km</b><br>'
                f'out and back; ΔR = cτ/2 = <b class="cl">{f(dR, 0)} m</b>')


def u6_l2():
    """6.5 worked example 1 (a): 10.525 GHz police CW radar, car closing at 100 km/h"""
    f0, vk = 10.525e9, 100
    lam = C / f0
    v = vk / 3.6
    fd = 2 * v / lam
    per = fd / vk
    assert (f(lam * 100, 2), f(v, 2), f(fd, 0), f(per, 1)) == ('2.85', '27.78', '1949', '19.5')
    # board: the radar on a tripod, a car driving at it, out and back arrows
    at(60, 0)
    parts = [rod((1.2, 6.2, 0), (1.2, 6.2, 1.3), '#8E97A6', 5), rod((.8, 6.7, 0), (1.2, 6.2, .9), '#8E97A6', 4), rod((1.7, 6.6, 0), (1.2, 6.2, .9), '#8E97A6', 4),
             box(.8, 5.7, .8, 1.0, .7, '#3A3470', '#1A1640', '#262058', z0=1.3), poly(circ((1.62, 6.2, 1.65), .32, 'yz'), AC, '#5B45B0', 2)]
    cx, cy = 5.4, 2.4                                          # car: body and cabin, wheels
    parts += [box(cx - 1.4, cy - .7, 2.8, 1.4, .6, '#C64B5A', '#7A2632', '#9C3341', z0=.25),
              box(cx - .7, cy - .6, 1.5, 1.2, .5, '#9FC3E6', '#5E7E9E', '#7A9CBE', z0=.85)]
    for (wx, wy) in ((cx - .9, cy + .72), (cx + .9, cy + .72)):
        x, y = P(wx, wy, .25)
        parts.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="9" ry="13" fill="#111" transform="rotate(-30 {x:.1f} {y:.1f})"/>')
    parts += [glow(arr3((2.0, 5.2, 1.7), (4.0, 3.6, 1.0), AC, 5)), glow(arr3((4.2, 4.3, .8), (2.3, 6.0, 1.4), AC2, 4)),
              arr3((cx + .2, cy - 1.0, .1), (cx - 1.6, cy + .8, .1), '#FFFFFF', 3)]
    brd = board(parts)
    X = lambda kmh: 44 + kmh / 150 * 400
    Y = lambda hz: 124 - hz / 3000 * 96
    card = (t(250, 16, 'Doppler shift against speed', 'pt', col=AC) + axes(44, 24, 444, 124)
            + curve([(X(0), Y(0)), (X(150), Y(per * 150))], AC, 3.5) + curve([(X(0), Y(0)), (X(150), Y(per * 75))], '#8C86B8', 2, 'stroke-dasharray="6 5"')
            + vline(X(vk), Y(fd), 124, AC2, '4 4') + hline(44, X(vk), Y(fd), AC2, '4 4') + dot(X(vk), Y(fd), AC2, 6)
            + t(38, Y(fd) + 5, f(fd, 0), anchor='end', col=AC2) + t(X(150) - 6, Y(per * 150) + 22, '2v/λ', 'pt', 'end', AC)
            + t(X(150) - 4, Y(per * 75) + 18, 'v/λ, one way only', 'ax', 'end', '#B9B2E6')
            + t(X(0), 140, '0') + t(X(vk), 140, f'{vk} km/h', col=AC2) + t(X(150), 140, '150', anchor='end') + t(50, 34, 'f<tspan font-size="10">d</tspan>, Hz', anchor='start'))
    card = svg(card)
    return spec('ec-antenna-u6-L2', 'PRF, Doppler<br>&amp; MTI Radar',
                'Shifted <span class="gold">TWICE</span>, out<br>and back, so <span class="cyan">2v/λ</span>',
                '100 km/h at 10.525 GHz', card, brd,
                chips(('left', 300, 'c', f'f₀ = {f(f0 / 1e9, 3)} GHz'), ('left', 364, 'c', f'λ = {f(lam * 100, 2)} cm'), ('left', 520, 'g', f'v = {f(v, 2)} m/s'),
                      ('right', 300, 'g', f'f<sub>d</sub> = {f(fd, 0)} Hz'), ('right', 530, 'c', f'{f(per, 1)} Hz per km/h', False)),
                f'f<sub>d</sub> = 2v/λ = 2 × {f(v, 2)} ÷ {f(lam, 5)} = <b class="gl">{f(fd, 0)} Hz</b><br>'
                f'shifted once going out and <b class="cl">again</b> coming back')


def u6_l3():
    """6.7 worked example: monopulse, delta = 1.2 V, sum = 10 V, slope 1.8 per degree, target at 20 km"""
    dlt, sm, k, R = 1.2, 10, 1.8, 20e3
    ratio = dlt / sm
    th = ratio / k
    off = R * math.radians(th)
    assert (f(ratio, 2), f(th, 4), f(math.radians(th) * 1e3, 3), f(off, 1)) == ('0.12', '0.0667', '1.164', '23.3')
    # board: four horns in a 2 x 2 cluster facing +x, the comparator behind with sum and difference outputs, two squinted beams
    at(40, 0)
    parts = [block(.8, 3.0, 1.6, 2.0, 1.2, DARK, 'Σ Δ', AC, 18)]
    for (yy, zz) in ((3.1, 1.7), (4.0, 1.7), (3.1, 2.6), (4.0, 2.6)):
        parts.append(box(2.5, yy, 1.1, .85, .85, '#C9CED8', '#7F8898', '#A5AEBC', z0=zz - .45))
        parts.append(poly([(3.6, yy + .1, zz - .35), (3.6, yy + .75, zz - .35), (3.6, yy + .75, zz + .3), (3.6, yy + .1, zz + .3)], '#1A1640'))
    for dy_, col in ((-.55, AC), (.55, AC2)):
        lobe = [(3.8 + 3.6 * math.sin(math.pi * i / 40), 4.0 + dy_ * 1.0 + dy_ * 2.2 * (i / 40) * math.sin(math.pi * i / 40) + 1.1 * math.sin(math.pi * i / 40) * (-1 if i < 20 else 1) * .0, 2.15)
                for i in range(41)]
        beam = [(3.8 + 3.8 * s * math.cos(a), 4.0 + 3.8 * s * math.sin(a), 2.15)
                for a, s in [(math.radians(9 * (1 if dy_ > 0 else -1)) + math.radians(14) * math.cos(math.pi * i / 40), math.sin(math.pi * i / 40)) for i in range(41)]]
        parts.append(glow(poly(beam, col, col, 2.5, 'fill-opacity=".14"')))
    parts += [ln((3.8, 4.0, 2.15), (7.8, 4.0, 2.15), '#FFFFFF', 1.6, 'stroke-dasharray="5 5" stroke-opacity=".7"'), jet(7.2, 4.6, 2.15, '#E6EAF2')]
    brd = board(parts)
    X = lambda a: 44 + (a + 3) / 6 * 190
    Y = lambda v: 76 - v * 46
    beam = lambda a, s: math.exp(-((a - s) / 1.6) ** 2)
    A_ = [(X(a), Y(beam(a, -.9))) for a in [-3 + 6 * i / 120 for i in range(121)]]
    B_ = [(X(a), Y(beam(a, .9))) for a in [-3 + 6 * i / 120 for i in range(121)]]
    left = (t(140, 16, 'two squinted beams', 'pt', col=AC) + f'<line x1="44" y1="{Y(0)}" x2="234" y2="{Y(0)}" stroke="{AX}" stroke-width="1.5"/>'
            + curve(A_, AC, 2.5) + curve(B_, AC2, 2.5) + vline(X(0), 26, 124, '#FFFFFF', '4 4', 1.2) + t(X(0), 140, 'boresight'))
    X2 = lambda a: 270 + (a + .15) / .3 * 180
    Y2 = lambda r: 76 - r / .3 * 50
    right = (t(360, 16, 'Δ/Σ against angle', 'pt', col=AC2) + f'<line x1="270" y1="76" x2="450" y2="76" stroke="{AX}" stroke-width="1.5"/>'
             + f'<line x1="{X2(0)}" y1="24" x2="{X2(0)}" y2="128" stroke="{AX}" stroke-width="1.5"/>'
             + curve([(X2(-.15), Y2(-.15 * k)), (X2(.15), Y2(.15 * k))], AC2, 3) + dot(X2(th), Y2(ratio), AC, 6)
             + hline(X2(0), X2(th), Y2(ratio), AC, '3 3', 1.4) + vline(X2(th), Y2(ratio), 76, AC, '3 3', 1.4)
             + t(X2(0) - 6, Y2(ratio) + 4, f(ratio, 2), anchor='end', col=AC) + t(X2(th) + 4, 94, f'{f(th, 4)}°', 'ax', 'start', AC)
             + t(450, 140, f'slope k = {f(k, 1)} per degree', 'ax', 'end'))
    card = svg(left + right)
    return spec('ec-antenna-u6-L3', 'Tracking,<br>Detection &amp;<br>Hardware',
                'Mono = <span class="gold">ONE</span> pulse, read<br>on <span class="cyan">SQUINTED</span> beams',
                'monopulse, one pulse', card, brd,
                chips(('left', 300, 'c', f'Δ = {dlt} V'), ('left', 364, 'g', f'Σ = {sm} V'), ('left', 520, 'c', f'k = {k} per degree'),
                      ('right', 300, 'g', f'θ = {f(th, 4)}°'), ('right', 530, 'c', f'{f(off, 1)} m at 20 km', False)),
                f'Δ/Σ = {f(ratio, 2)}; θ = {f(ratio, 2)} ÷ {k} = <b class="gl">{f(th, 4)}°</b><br>'
                f'20 km × {f(math.radians(th) * 1e3, 3)}×10⁻³ rad = <b class="cl">{f(off, 1)} m</b> off')


def specs():
    return [u1_l1(), u1_l2(), u1_l3(), u1_l4(), u2_l1(), u2_l2(), u2_l3(), u2_l4(), u3_l1(), u3_l2(), u3_l3(),
            u4_l1(), u4_l2(), u4_l3(), u5_l1(), u5_l2(), u5_l3(), u6_l1(), u6_l2(), u6_l3()]
