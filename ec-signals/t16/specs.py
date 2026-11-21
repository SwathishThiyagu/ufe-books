"""t16 split blueprint thumbnails for Signals and Systems (ec-signals), ECE look.
One spec per lesson, each built from that lesson's own book worked example (books/ece/ec-signals/ec-signals-u<N>.html).
Every number on a card, chip, board or summary is computed here.
Build: python3 t16_split.py build specs.py <out dir>"""
import cmath, json, math, os, sys

_here = os.path.dirname(os.path.abspath(__file__))
for _p in (os.environ.get('T16_TOOL', ''), os.path.join(_here, '..', 'tool'), _here):
    if _p and os.path.exists(os.path.join(_p, 't16_split.py')) and _p not in sys.path:
        sys.path.insert(0, _p)
import t16_split as T

B = T.B
P, pts, box, cyl, arrow = T.P, T.pts, T.box, T.cyl, T.arrow
D = 'ece'
ACC, ACC2 = T.DEPTS[D]['acc'], T.DEPTS[D]['acc2']     # violet ("gold" class), mint ("cyan" class)
INK, AX, MUT = '#E6ECF1', '#6B7B8A', '#C9D3DB'
GOLD = '#D9B45A'                                     # PCB copper traces
SUBJECT = 'SIGNALS AND SYSTEMS'
PI = math.pi


def g(v, nd=4):
    """number text: up to nd significant digits, true minus sign"""
    s = f'{v:.{nd}g}'
    return s.replace('-', '−')


def f2(v, nd=3):
    return f'{v:.{nd}f}'.replace('-', '−')


def sup(s):
    return f'<sup>{s}</sup>'


def ssup(s):
    """a superscript inside SVG text (an HTML sup would break the SVG out)"""
    return f'<tspan baseline-shift="super" font-size="70%">{s}</tspan>'


# ================================================================ isometric board helpers (board units, 8 x 8 slab)
BDEFS = ('<defs><linearGradient id="pcb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#17463C"/><stop offset="1" stop-color="#0D2A24"/></linearGradient>'
         '<linearGradient id="ic" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2A2E36"/><stop offset="1" stop-color="#121418"/></linearGradient>'
         '<linearGradient id="xt" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8E99A6"/><stop offset=".4" stop-color="#F2F5F8"/><stop offset="1" stop-color="#7C8794"/></linearGradient></defs>')


def setup(origin=(952, 300), unit=33):
    B.U, (B.OX, B.OY) = unit, origin


def board(parts, origin=(952, 300), unit=33, top='url(#pcb)'):
    return T.iso_board(D, [BDEFS] + parts, top=top, left='#0A1F1A', right='#0E2822', origin=origin, unit=unit)


def label(x, y, z, text, col=INK, size=15, anchor='middle'):
    a, b = P(x, y, z)
    return f'<text x="{a:.1f}" y="{b:.1f}" text-anchor="{anchor}" class="capl" fill="{col}" style="font-size:{size}px">{text}</text>'


def trace(xy, col=GOLD, w=2.6, op=.85, z=0):
    return f'<polyline points="{pts(*[P(x, y, z) for x, y in xy])}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round" opacity="{op}"/>'


def glow(points, col=ACC2, w=4):
    return f'<g filter="url(#gl)"><polyline points="{pts(*points)}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"/></g>'


def wave(f, x0, x1, y, z0, zs, col=ACC2, n=90, w=3.5):
    """a signal drawn standing on the board: runs along x at depth y, height z0 + zs * f(x)"""
    return glow([P(x0 + (x1 - x0) * i / n, y, z0 + zs * f(x0 + (x1 - x0) * i / n)) for i in range(n + 1)], col, w)


def wave_xy(f, s0, s1, a, b, z0, zs, col=ACC2, n=90, w=3.5):
    """a signal standing along the line from board point a to b, parameter s0..s1"""
    o = []
    for i in range(n + 1):
        t = i / n; s = s0 + (s1 - s0) * t
        o.append(P(a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, z0 + zs * f(s)))
    return glow(o, col, w)


def pad(x, y):
    a, b = P(x, y)
    return f'<ellipse cx="{a:.1f}" cy="{b:.1f}" rx="4.5" ry="2.6" fill="#0D2A24" stroke="{GOLD}" stroke-width="1.8"/>'


def ic(x, y, w, d, text='', h=.42, col=ACC2, size=17, pins=True):
    o = box(x, y, w, d, h, 'url(#ic)', '#0B0D10', '#1A1D22')
    if pins:
        n = max(2, int(round(w / .45)))
        for k in range(n):
            px = x + (k + .5) * w / n - .09
            o += box(px, y + d, .18, .16, .12, '#C9D0D6', '#7D8792', '#9AA4AE')
        m = max(2, int(round(d / .45)))
        for k in range(m):
            py = y + (k + .5) * d / m - .09
            o += box(x + w, py, .16, .18, .12, '#C9D0D6', '#7D8792', '#9AA4AE')
    if text:
        o += label(x + w / 2, y + d / 2, h + .02, text, col, size)
    return o


def smd(x, y, w=.55, d=.28, h=.14, body='#1C1E22', cap='#D9DEE2'):
    """a small two-terminal part (resistor or capacitor chip)"""
    return (box(x, y, w, d, h, body, '#0E0F12', '#16181B') + box(x - .08, y - .02, .1, d + .04, h + .02, cap, '#9AA4AE', '#B9C1C9')
            + box(x + w - .02, y - .02, .1, d + .04, h + .02, cap, '#9AA4AE', '#B9C1C9'))


def column(x, y, v, scale, col, w=.42, base=0, text=None, tcol=INK, size=15):
    """a sample value as a raised column (negative values hang below as a recess outline)"""
    h = v * scale
    if h >= 0:
        o = box(x, y, w, w, max(h, .03), col, shade(col, .45), shade(col, .65), z0=base)
        ty = h + base + .35
    else:
        o = box(x, y, w, w, -h, shade(col, .75), shade(col, .4), shade(col, .55), z0=base + h)
        ty = base + .35
    if text is not None:
        o += label(x + w / 2, y + w / 2, ty, text, tcol, size)
    return o


def shade(hexcol, k):
    h = hexcol.lstrip('#')
    r, gg, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return '#%02X%02X%02X' % (int(r * k), int(gg * k), int(b * k))


def slabp(x0, x1, y, h, col, d=.5, z0=0):
    """a rectangular pulse as a raised block from x0 to x1 (board units) at depth y"""
    return box(x0, y, x1 - x0, d, h, col, shade(col, .5), shade(col, .7), z0=z0)


def plane_line(xy, col, w=2, op=.6, dash=''):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polyline points="{pts(*[P(x, y) for x, y in xy])}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"{da}/>'


def plane_poly(xy, col, op=.25):
    return f'<polygon points="{pts(*[P(x, y) for x, y in xy])}" fill="{col}" opacity="{op}"/>'


def pole(x, y, col=ACC, h=.9, r=9):
    """a pole: an x mark on the plane with a glowing post"""
    a, b = P(x, y); c, d = P(x, y, h)
    return (f'<line x1="{a:.1f}" y1="{b:.1f}" x2="{c:.1f}" y2="{d:.1f}" stroke="{col}" stroke-width="3" opacity=".8"/>'
            f'<g filter="url(#gl)"><path d="M{a - r:.1f},{b - r * .55:.1f}L{a + r:.1f},{b + r * .55:.1f}M{a - r:.1f},{b + r * .55:.1f}L{a + r:.1f},{b - r * .55:.1f}" stroke="{col}" stroke-width="4" stroke-linecap="round"/></g>'
            f'<circle cx="{c:.1f}" cy="{d:.1f}" r="5" fill="{col}"/>')


def zero_mark(x, y, col=ACC2, r=8):
    a, b = P(x, y)
    return f'<ellipse cx="{a:.1f}" cy="{b:.1f}" rx="{r}" ry="{r * .58:.1f}" fill="none" stroke="{col}" stroke-width="3.5"/>'


def crystal(x, y, text):
    return box(x, y, 1.1, .5, .35, 'url(#xt)', '#6E7884', '#9AA4AE') + label(x + .55, y + .25, .38, text, '#1A1F26', 11)


def screen(x0, x1, y, z0, H, f, s0, s1, vmin, vmax, col, n=120, frame=INK, dots=(), fill=False, zero=True, w=3.6, extra=()):
    """an upright scope screen standing on the board along x (time runs right-down), with the curve f(s), s0..s1"""
    o = (f'<polygon points="{pts(P(x0, y, z0), P(x1, y, z0), P(x1, y, z0 + H), P(x0, y, z0 + H))}" fill="#0A0D1C" fill-opacity=".88" stroke="{frame}" stroke-opacity=".55" stroke-width="2"/>'
         + box(x0 + .1, y - .08, .12, .16, z0, '#3A3F48', '#22262C', '#2C3038') + box(x1 - .22, y - .08, .12, .16, z0, '#3A3F48', '#22262C', '#2C3038'))
    Z = lambda v: z0 + .12 * H + (v - vmin) / (vmax - vmin) * .76 * H
    X = lambda s: x0 + .06 * (x1 - x0) + (s - s0) / (s1 - s0) * .88 * (x1 - x0)
    if zero and vmin < 0 < vmax:
        o += f'<line x1="{P(X(s0), y, Z(0))[0]:.1f}" y1="{P(X(s0), y, Z(0))[1]:.1f}" x2="{P(X(s1), y, Z(0))[0]:.1f}" y2="{P(X(s1), y, Z(0))[1]:.1f}" stroke="{INK}" stroke-opacity=".35" stroke-width="1.5"/>'
    elif zero:
        o += f'<line x1="{P(X(s0), y, Z(vmin))[0]:.1f}" y1="{P(X(s0), y, Z(vmin))[1]:.1f}" x2="{P(X(s1), y, Z(vmin))[0]:.1f}" y2="{P(X(s1), y, Z(vmin))[1]:.1f}" stroke="{INK}" stroke-opacity=".35" stroke-width="1.5"/>'
    pp = [P(X(s0 + (s1 - s0) * i / n), y, Z(f(s0 + (s1 - s0) * i / n))) for i in range(n + 1)]
    if fill:
        base = Z(max(vmin, 0))
        o += f'<polygon points="{pts(P(X(s0), y, base), *pp, P(X(s1), y, base))}" fill="{col}" opacity=".22"/>'
    o += glow(pp, col, w)
    for fe, ce, we in extra:
        o += glow([P(X(s0 + (s1 - s0) * i / n), y, Z(fe(s0 + (s1 - s0) * i / n))) for i in range(n + 1)], ce, we)
    for s in dots:
        a, b = P(X(s), y, Z(f(s)))
        o += f'<circle cx="{a:.1f}" cy="{b:.1f}" r="4.2" fill="{col}"/>'
    return o


def varrow(a, b, col, w=5, z=.1):
    (x0, y0), (x1, y1) = P(a[0], a[1], z), P(b[0], b[1], z)
    return f'<g filter="url(#gl)">{arrow(x0, y0, x1, y1, col, w)}</g>'


# ================================================================ card helpers (470 x 144 SVG)
def card_svg(inner, h=144):
    return f'<svg width="470" height="{h}" viewBox="0 0 470 {h}">{inner}</svg>'


class Plot:
    def __init__(s, L, T_, W, H, x0, x1, y0, y1):
        s.L, s.T, s.W, s.H, s.x0, s.x1, s.y0, s.y1 = L, T_, W, H, x0, x1, y0, y1

    def X(s, x):
        return s.L + (x - s.x0) / (s.x1 - s.x0) * s.W

    def Y(s, y):
        return s.T + s.H - (y - s.y0) / (s.y1 - s.y0) * s.H

    def axes(s, xt=(), yt=(), xfmt=g, yfmt=g, xunit='', ylab=''):
        o = ''
        yz = s.Y(0) if s.y0 <= 0 <= s.y1 else s.T + s.H
        o += f'<line x1="{s.L}" y1="{yz:.1f}" x2="{s.L + s.W}" y2="{yz:.1f}" stroke="{AX}" stroke-width="1.5"/>'
        xa = s.X(0) if s.x0 <= 0 <= s.x1 else s.L
        o += f'<line x1="{xa:.1f}" y1="{s.T}" x2="{xa:.1f}" y2="{s.T + s.H}" stroke="{AX}" stroke-width="1.5"/>'
        for v in yt:
            o += f'<text x="{xa - 6:.1f}" y="{s.Y(v) + 5:.1f}" text-anchor="end" class="ax">{yfmt(v)}</text>'
        for i, v in enumerate(xt):
            lab = xfmt(v) + (f' {xunit}' if xunit and i == len(xt) - 1 else '')
            o += f'<text x="{s.X(v):.1f}" y="{s.T + s.H + 17:.1f}" text-anchor="middle" class="ax">{lab}</text>'
        if ylab:
            o += f'<text x="{xa + 6:.1f}" y="{s.T + 10:.1f}" class="ax">{ylab}</text>'
        return o

    def curve(s, f, a=None, b=None, col=ACC, w=3.2, n=160, dash=''):
        a = s.x0 if a is None else a; b = s.x1 if b is None else b
        p = ' '.join(f'{s.X(a + (b - a) * i / n):.1f},{s.Y(f(a + (b - a) * i / n)):.1f}' for i in range(n + 1))
        da = f' stroke-dasharray="{dash}"' if dash else ''
        return f'<polyline points="{p}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"{da}/>'

    def poly(s, xy, col=ACC, w=3.2, fill='none', fop=.15, dash=''):
        p = ' '.join(f'{s.X(x):.1f},{s.Y(y):.1f}' for x, y in xy)
        da = f' stroke-dasharray="{dash}"' if dash else ''
        return f'<polyline points="{p}" fill="{fill}" fill-opacity="{fop}" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"{da}/>'

    def stems(s, ns, vs, col=ACC2, r=5.5, labels=True, fmt=g, lab_col=INK):
        o = ''
        for n, v in zip(ns, vs):
            x, y, yb = s.X(n), s.Y(v), s.Y(0)
            if abs(v) > 1e-12:
                o += f'<line x1="{x:.1f}" y1="{yb:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="3.2"/>'
            o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>'
            if labels and abs(v) > 1e-12:
                ty = y - 9 if v >= 0 else y + 19
                o += f'<text x="{x:.1f}" y="{ty:.1f}" text-anchor="middle" class="ax" fill="{lab_col}">{fmt(v)}</text>'
        return o


def ptitle(x, text, col):
    return f'<text x="{x}" y="16" text-anchor="middle" class="pt" fill="{col}">{text}</text>'


def ctext(x, y, text, col=INK, size=15, anchor='start', weight=600):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{col}" style="font:{weight} {size}px \'IBM Plex Sans\'">{text}</text>'


def chip(side, top, kind, text, pointer=True):
    return dict(side=side, top=top, kind=kind, text=text, pointer=pointer)


CSS = '.col{padding-right:22px !important}'


def spec(key, title, takeaway, card_title, card, board_svg, chips, summary, css=''):
    return dict(key=key, title=title, takeaway=takeaway, tag='Book example', card_title=card_title, card=card,
                board=board_svg, chips=chips, summary=summary, css=CSS + css)


# ================================================================ unit 1
def u1L1():
    """1.2 Worked examples 1 and 2: x(t) = 6 cos(200 pi t) + 3 V (power), x[n] = 1, 2, 3 (energy)"""
    A, w, dc = 6, 200 * PI, 3
    T0 = 2 * PI / w; f0 = 1 / T0
    Pa, Pd = A ** 2 / 2, dc ** 2; Pw = Pa + Pd; Eper = Pw * T0
    xn = [1, 2, 3]; E = sum(v * v for v in xn)
    # card: endless wave and short burst
    p = Plot(44, 30, 170, 92, 0, 3 * T0 * 1000, -3, 9)
    c = ptitle(128, 'endless wave: power', ACC) + f'<rect x="{p.X(0):.1f}" y="30" width="{p.X(T0 * 1000) - p.X(0):.1f}" height="92" fill="{ACC}" opacity=".12"/>'
    c += p.axes(xt=[0, 10, 20, 30], yt=[9, 0, -3], xunit='ms')
    c += p.curve(lambda t: A * math.cos(w * t / 1000) + dc, col=ACC)
    q = Plot(270, 40, 190, 72, -1.5, 3.5, 0, 3.4)
    c += ptitle(365, 'short burst: energy', ACC2) + q.axes(xt=[-1, 0, 1, 2, 3])
    c += q.stems([-1, 0, 1, 2, 3], [0] + xn + [0], ACC2)
    setup()
    o = []
    o.append(trace([(2.4, 4.6), (2.4, 5.6), (2.0, 6.4)]) + trace([(4.4, 2.6), (5.4, 2.6), (5.9, 1.7)]) + trace([(4.4, 4.0), (5.2, 4.0), (5.6, 4.6)], ACC2, 3.2, 1))
    o.append(pad(2.0, 6.4) + pad(5.9, 1.7) + pad(5.6, 4.6))
    o.append(crystal(5.5, .8, f'{g(f0)} Hz'))
    o.append(ic(2.4, 2.4, 2.0, 2.2, 'x(t)', size=19))
    o.append(screen(0.6, 4.4, 6.8, .1, 1.7, lambda t: A * math.cos(w * t) + dc, 0, 3 * T0, -3, 9, ACC, 140, frame=ACC))
    for k, v in enumerate(xn):
        o.append(column(5.6 + k * .62, 5.0, v, .45, ACC2, text=g(v)))
    return spec('ec-signals-u1-L1', 'Signals &amp; How<br>to Sort Them',
                'Endless wave → <span class="gold">POWER</span><br>Short burst → <span class="cyan">ENERGY</span>',
                'power or energy?', card_svg(c), board(o),
                [chip('left', 254, 'g', f'T₀ = {g(T0 * 1000)} ms · f₀ = {g(f0)} Hz'), chip('left', 318, 'g', f'P = {g(Pa)} + {g(Pd)} = {g(Pw)} W'),
                 chip('right', 250, 'g', f'E = {g(Eper)} J per period → ∞', False), chip('right', 420, 'c', 'x[n] = 1, 2, 3'),
                 chip('right', 516, 'c', f'E = {g(E)}, P = 0', False)],
                f'<b class="gl">x(t) = 6 cos(200πt) + 3:</b> P = 6²/2 + 3² = <b class="gl">{g(Pw)} W</b>, E = ∞<br>'
                f'<b class="cl">x[n] = 1, 2, 3:</b> E = 1 + 4 + 9 = <b class="cl">{g(E)}</b>, P = 0')


def u1L2():
    """1.4 Worked example: x(t) = 2 on 0..2 s; y = x(2t - 1), z = x(-t + 1)"""
    amp, a0, a1 = 2, 0, 2
    y0, y1 = (a0 + 1) / 2, (a1 + 1) / 2          # 0 <= 2t - 1 <= 2
    z0, z1 = 1 - a1, 1 - a0                      # 0 <= -t + 1 <= 2
    p = Plot(40, 26, 420, 84, -1.6, 2.6, 0, 2.6)
    c = p.axes(xt=[-1, 0, y0, 1, y1, 2], yt=[2], xunit='s')
    c += p.poly([(z0, 0), (z0, amp), (z1, amp), (z1, 0)], '#8A93A3', 2.4, dash='6 5')
    c += p.poly([(a0, 0), (a0, amp), (a1, amp), (a1, 0)], ACC, 3.2, ACC, .10)
    c += p.poly([(y0, 0), (y0, amp), (y1, amp), (y1, 0)], ACC2, 3.6, ACC2, .22)
    c += f'<text x="{p.X(1.9):.1f}" y="{p.Y(amp) - 6:.1f}" text-anchor="end" class="pt" fill="{ACC}">x(t)</text>'
    c += f'<text x="{p.X(y0) + 2:.1f}" y="{p.Y(amp) - 6:.1f}" text-anchor="start" class="pt" fill="{ACC2}">x(2t − 1)</text>'
    c += f'<text x="{p.X(-1.55):.1f}" y="{p.Y(amp) - 6:.1f}" class="ax">x(−t + 1)</text>'
    setup()
    X = lambda t: 1.3 + (t + 1.5) * 1.6           # t = -1.5 .. 2.5 s on x = 1.3 .. 7.7
    rows = [(2.3, a0, a1, ACC, 'x(t)', ACC), (3.7, y0, y1, ACC2, 'x(2t − 1)', ACC2), (5.1, z0, z1, '#59606E', 'x(−t + 1)', INK)]
    o = [plane_line([(X(-1.5), 6.3), (X(2.5), 6.3)], INK, 2.2, .6)]
    for t in (-1, 0, 1, 2):
        o.append(plane_line([(X(t), 6.15), (X(t), 6.5)], INK, 2, .7) + label(X(t), 6.95, 0, g(t), MUT, 14))
    o.append(label(X(2.5) + .1, 6.95, 0, 't, s', MUT, 13))
    for t in (y0, y1):
        o.append(plane_line([(X(t), 4.3), (X(t), 6.3)], ACC2, 2.4, .9, '5 5'))
    for yy, t0, t1, col, nm, lc in rows:
        o.append(slabp(X(t0), X(t1), yy, amp * .5, col, d=.6))
    for yy, t0, t1, col, nm, lc in rows:
        o.append(label((X(t0) + X(t1)) / 2, yy + .3, amp * .5 + .45, nm, lc, 16))
    return spec('ec-signals-u1-L2', 'Standard<br>Signals &amp; How<br>to Edit Them',
                f'Solve 0 ≤ 2t − 1 ≤ 2: starts<br>at <span class="gold">{g(y0)} s</span>, ends at <span class="cyan">{g(y1)} s</span>',
                'shift and scale a pulse', card_svg(c), board(o),
                [chip('left', 254, 'g', f'x(t) = {amp} on {g(a0)} to {g(a1)} s'), chip('left', 318, 'c', '1 ≤ 2t ≤ 3'),
                 chip('right', 250, 'c', f'width {g(y1 - y0)} s, height {amp}', False), chip('right', 520, 'g', f'x(−t + 1): {g(z0)} to {g(z1)} s', False)],
                f'0 ≤ 2t − 1 ≤ 2 → 1 ≤ 2t ≤ 3 → <b class="cl">{g(y0)} ≤ t ≤ {g(y1)} s</b><br>'
                f'0 ≤ −t + 1 ≤ 2 → <b class="gl">{g(z0)} ≤ t ≤ {g(z1)} s</b>: reverse, then shift')


def u1L3():
    """1.5 Worked example: y(t) = 3x(t) + 2 (CT, memoryless), y[n] = x[n] - x[n - 1] (DT, memory)"""
    yc = 3 * 1 + 2                                    # x = u(t), t = 1
    x = lambda n: n if n >= 0 else 0                  # x[n] = n u[n]
    yd = lambda n: x(n) - x(n - 1)
    ns = list(range(-1, 5))
    p = Plot(36, 34, 180, 76, -1.5, 4.5, 0, 4.4)
    c = ptitle(126, 'x[n] = n u[n]', ACC) + p.axes(xt=ns) + p.stems(ns, [x(n) for n in ns], ACC)
    q = Plot(276, 34, 180, 76, -1.5, 4.5, 0, 4.4)
    c += ptitle(366, 'y[n] = x[n] − x[n − 1]', ACC2) + q.axes(xt=ns) + q.stems(ns, [yd(n) for n in ns], ACC2)
    c += f'<circle cx="{q.X(2):.1f}" cy="{q.Y(yd(2)):.1f}" r="11" fill="none" stroke="{ACC2}" stroke-width="2"/>'
    setup()
    o = []
    o.append(trace([(3.6, 6.1), (4.4, 6.1), (4.4, 4.9)], ACC, 3.4, 1) + trace([(5.4, 3.4), (5.4, 2.0), (5.8, 2.0)], ACC2, 3.4, 1))
    o.append(ic(3.0, 3.4, 3.2, 1.5, 'x[n] − x[n − 1]', size=16))
    for k, n in enumerate((0, 1, 2, 3)):
        o.append(column(1.0 + k * .7, 5.9, x(n), .6, ACC, text=f'{x(n)}'))
    for k, n in enumerate((0, 1, 2, 3)):
        o.append(column(5.0 + k * .7, 1.2, yd(n), .6, ACC2 if n == 2 else shade(ACC2, .7), text=f'{yd(n)}'))
    o.append(label(0.5, 6.4, 0, 'x[n]', ACC, 16, 'end') + label(4.6, 1.4, 0, 'y[n]', ACC2, 16, 'end'))
    return spec('ec-signals-u1-L3', 'Sorting &amp;<br>Testing<br>Systems',
                'Uses x[n − 1]: it has <span class="gold">MEMORY</span><br>but past only, so <span class="cyan">CAUSAL</span>',
                'memory or memoryless?', card_svg(c), board(o),
                [chip('left', 254, 'g', 'y(t) = 3x(t) + 2: CT'), chip('left', 318, 'g', f'y(1) = 3 × 1 + 2 = {yc}'),
                 chip('right', 262, 'c', f'y[2] = 2 − 1 = {yd(2)}', False), chip('left', 520, 'c', 'x[n] = n u[n]')],
                f'y(t) = 3x(t) + 2 uses x(t) only: <b class="gl">memoryless</b><br>'
                f'y[n] = x[n] − x[n − 1] uses x[n − 1]: <b class="cl">memory</b>')


def u1L4():
    """1.7 Worked example: square wave f on (0, 2 pi) approximated by c sin t"""
    num = 2 + 2                 # integral of f sin t over (0, 2 pi)
    den = PI                    # integral of sin^2 t = ||sin t||^2
    c12 = num / den
    Ef = 2 * PI; kept = c12 ** 2 * den; err = Ef - kept; mse = err / (2 * PI); frac = kept / Ef
    wrong = num / math.sqrt(den)
    p = Plot(40, 26, 250, 96, 0, 2 * PI, -1.5, 1.5)
    c = p.axes(xt=[0, PI, 2 * PI], yt=[1, -1], xfmt=lambda v: {0: '0', 1: 'π', 2: '2π'}[round(v / PI)])
    c += p.poly([(0, 0), (0, 1), (PI, 1), (PI, -1), (2 * PI, -1), (2 * PI, 0)], ACC, 3)
    c += p.curve(lambda t: c12 * math.sin(t), col=ACC2, w=3.4)
    c += f'<text x="{p.X(PI / 2):.1f}" y="{p.Y(c12) - 4:.1f}" text-anchor="middle" class="ax" fill="{ACC2}">{g(c12)} sin t</text>'
    bx, bw = 320, 130
    hk = 96 * frac
    c += ptitle(bx + bw / 2, 'energy of f', INK)
    c += f'<rect x="{bx + 30}" y="{26 + 96 - hk:.1f}" width="56" height="{hk:.1f}" fill="{ACC2}" opacity=".85"/>'
    c += f'<rect x="{bx + 30}" y="26" width="56" height="{96 - hk:.1f}" fill="{ACC}" opacity=".35" stroke="{ACC}" stroke-width="1.5"/>'
    c += ctext(bx + 94, 26 + 96 - hk / 2 + 5, f'{frac * 100:.0f} %', ACC2, 16) + ctext(bx + 94, 26 + (96 - hk) / 2 + 5, f'{(1 - frac) * 100:.0f} %', ACC, 16)
    c += ctext(bx + 58, 140, f'2π = {g(Ef)}', MUT, 14, 'middle', 500)
    setup()
    o = []
    # the square wave and its best sine on one scope, and the energy of f split into kept and error
    o.append(screen(2.4, 7.4, 2.6, .1, 2.0, lambda t: 1 if t < PI else -1, 0, 2 * PI, -1.5, 1.5, ACC, 120, frame=ACC, w=3,
                    extra=[(lambda t: c12 * math.sin(t), ACC2, 3.6)]))
    o.append(label(4.9, 2.6, 2.45, f'f and {g(c12)} sin t', INK, 15))
    zk, ze = kept * .3, err * .3
    o.append(box(2.0, 5.2, .9, .9, zk, ACC2, shade(ACC2, .45), shade(ACC2, .65)))
    o.append(box(2.0, 5.2, .9, .9, ze, ACC, shade(ACC, .45), shade(ACC, .65), z0=zk))
    o.append(label(3.3, 5.6, zk * .5, f'kept {f2(kept)}', ACC2, 15, 'start') + label(3.3, 5.6, zk + ze * .5 + .15, f'error {f2(err)}', ACC, 15, 'start'))
    o.append(label(2.45, 6.6, 0, f'energy 2π = {f2(Ef)}', INK, 14))
    return spec('ec-signals-u1-L4', 'Signals as<br>Vectors &amp;<br>Parseval',
                f'Divide by ‖φ‖², the <span class="gold">ENERGY</span><br>c = 4/π, not 4/√π = <span class="cyan">{g(wrong, 3)}</span>',
                'square wave ≈ c sin t', card_svg(c), board(o),
                [chip('left', 254, 'g', f'∫ f sin t dt = 2 + 2 = {num}'), chip('left', 318, 'g', '‖sin t‖² = ∫ sin² t dt = π'),
                 chip('right', 520, 'c', f'c = 4/π ≈ {g(c12)}', False), chip('right', 250, 'c', f'error energy {f2(err)}', False)],
                f'c = ∫ f sin t dt ÷ ‖sin t‖² = 4 ÷ π = <b class="gl">{f2(c12)}</b><br>'
                f'kept 16/π ≈ {f2(kept)} of 2π: <b class="cl">{frac * 100:.0f} %</b>, MSE {f2(mse)}')


# ================================================================ unit 2
def u2L1():
    """2.1 Worked example: y = 3x + 2, x1 = 1, x2 = 2, a = 2, b = 3; delay test x = t, t0 = 2, t = 5"""
    Tsys = lambda v: 3 * v + 2
    x1, x2, a, b = 1, 2, 2, 3
    comb = a * x1 + b * x2; p1 = Tsys(comb)
    y1, y2 = Tsys(x1), Tsys(x2); p2 = a * y1 + b * y2
    t, t0 = 5, 2
    d1 = 3 * (t - t0) + 2; d2 = 3 * (t - t0) + 2
    rows = [('combine, then T', f'T{{{comb}}} = 3({comb}) + 2', f'{p1}', ACC),
            ('T each, then combine', f'{a}({y1}) + {b}({y2})', f'{p2}', ACC2),
            (f'delay {t0} s, at t = {t} s', f'3({t} − {t0}) + 2, both paths', f'{d1} = {d2}', INK)]
    tbl = '<table><tr><th>path</th><th>working</th><th>result</th></tr>' + ''.join(
        f'<tr><td style="color:{c}">{n}</td><td>{w}</td><td style="color:{c};font-weight:700">{r}</td></tr>' for n, w, r, c in rows) + '</table>'
    setup()
    o = []
    # path 1 (back): a x1 and b x2 added, then the system
    o.append(trace([(1.6, 1.3), (2.3, 1.3)], ACC, 3.4, 1) + trace([(1.6, 2.1), (2.3, 2.1)], ACC, 3.4, 1))
    o.append(ic(2.3, 1.1, .9, 1.2, 'Σ', h=.3, col=INK, size=16, pins=False))
    o.append(trace([(3.2, 1.7), (3.8, 1.7)], ACC, 3.4, 1))
    o.append(ic(3.8, 1.1, 2.0, 1.2, '3x + 2', size=16, col=ACC))
    o.append(trace([(5.8, 1.7), (6.6, 1.7)], ACC, 3.4, 1) + label(7.1, 1.75, .1, f'{p1}', ACC, 22))
    # path 2 (front): the system on each input, then the sum
    o.append(ic(1.2, 4.0, 1.9, 1.0, '3x + 2', size=15) + ic(1.2, 5.8, 1.9, 1.0, '3x + 2', size=15))
    o.append(trace([(0.5, 4.5), (1.2, 4.5)], ACC2, 3.4, 1) + trace([(0.5, 6.3), (1.2, 6.3)], ACC2, 3.4, 1))
    o.append(trace([(3.1, 4.5), (4.2, 4.5), (4.2, 5.0)], ACC2, 3.4, 1) + trace([(3.1, 6.3), (4.2, 6.3), (4.2, 5.8)], ACC2, 3.4, 1))
    o.append(ic(3.8, 5.0, .9, .8, 'Σ', h=.3, col=INK, size=16, pins=False))
    o.append(trace([(4.7, 5.4), (6.0, 5.4)], ACC2, 3.4, 1) + label(6.5, 5.45, .1, f'{p2}', ACC2, 22))
    extra = """
.card.scope table{border-collapse:collapse;width:100%;margin-top:4px;font:600 16px 'IBM Plex Sans';color:#E6ECF1}
.card.scope th{font:600 14px 'IBM Plex Sans';color:#B7AEE0;text-align:left;padding:4px 8px;border-bottom:1.5px solid rgba(195,184,255,.3)}
.card.scope td{text-align:left;padding:8px 8px;border-bottom:1px solid rgba(195,184,255,.16)}
.card.scope td:last-child,.card.scope th:last-child{text-align:right}.card.scope tr:last-child td{border-bottom:none}"""
    return spec('ec-signals-u2-L1', 'LTI Systems &amp;<br>the Impulse<br>Response',
                f'{p1} ≠ {p2}: <span class="gold">NOT LINEAR</span><br>but time-<span class="cyan">INVARIANT</span>',
                'test y = 3x + 2', tbl, board(o),
                [chip('left', 254, 'g', f'x₁ = {x1}, x₂ = {x2}, a = {a}, b = {b}'), chip('right', 262, 'g', f'T{{{comb}}} = {p1}', False),
                 chip('left', 318, 'c', f'{a}·{y1} + {b}·{y2} = {p2}'), chip('right', 520, 'c', f'T{{0}} = {Tsys(0)} ≠ 0', False)],
                f'Linear? T{{{a}·{x1} + {b}·{x2}}} = <b class="gl">{p1}</b>, but {a}·{y1} + {b}·{y2} = <b class="gl">{p2}</b><br>'
                f'Delay test at t = {t} s: both paths give <b class="cl">{d1}</b>', extra)


def u2L2():
    """2.5 Worked example: h1 = e^-2t u(t), h2 = e^2t u(-t), h3 = u(t): causality and area under |h|"""
    a1 = 1 / 2                 # integral of e^-2t, 0..inf
    a2 = 1 / 2                 # integral of e^2t, -inf..0
    h2m1 = math.exp(-2)        # h2(-1)
    xb = 5; yb = xb * a1
    fs = [('h₁ = e' + ssup('−2t') + 'u(t)', lambda t: math.exp(-2 * t) if t >= 0 else 0, ACC, g(a1)),
          ('h₂ = e' + ssup('2t') + 'u(−t)', lambda t: math.exp(2 * t) if t <= 0 else 0, ACC, g(a2)),
          ('h₃ = u(t)', lambda t: 1 if t >= 0 else 0, ACC2, '∞')]
    c = ''
    for k, (nm, f, col, ar) in enumerate(fs):
        p = Plot(14 + k * 152, 30, 136, 70, -2, 2, 0, 1.25)
        xy = [(p.X(-2 + 4 * i / 120), p.Y(f(-2 + 4 * i / 120))) for i in range(121)]
        c += ptitle(14 + k * 152 + 68, nm, col)
        c += f'<polygon points="{p.X(-2):.1f},{p.Y(0):.1f} ' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in xy) + f' {p.X(2):.1f},{p.Y(0):.1f}" fill="{col}" opacity=".18"/>'
        c += p.axes(xt=[-2, 0, 2]) + p.poly([(-2 + 4 * i / 120, f(-2 + 4 * i / 120)) for i in range(121)], col, 3)
        c += ctext(14 + k * 152 + 68, 140, f'∫|h| dt = {ar}', col, 15, 'middle', 700)
    setup()
    o = []
    for k, (nm, f, col, ar) in enumerate(fs):
        x0 = 1.0 + k * 2.25
        o.append(screen(x0, x0 + 2.05, 5.8, .1, 1.8, f, -2, 2, 0, 1.1, col, 100, frame=col, fill=True))
        o.append(ic(x0 + .3, 6.4, 1.4, .9, ['h₁', 'h₂', 'h₃'][k], h=.34, col=col, size=17))
    return spec('ec-signals-u2-L2', 'Convolution,<br>Causality &amp;<br>Stability',
                'Stable needs a finite <span class="gold">∫|h|</span><br>sinc: net area 1, |area| <span class="cyan">∞</span>',
                'three impulse responses', card_svg(c), board(o),
                [chip('left', 254, 'g', f'h₁: causal, area {g(a1)}'), chip('left', 318, 'g', f'h₂(−1) = {g(h2m1, 3)}: noncausal'),
                 chip('right', 250, 'c', f'|x| ≤ {xb} V → |y| ≤ {g(yb)} V', False), chip('right', 520, 'c', 'h₃: area ∞, unstable', False)],
                f'h₁, h₂: ∫|h| dt = <b class="gl">{g(a1)}</b>, stable (h₂ noncausal)<br>'
                f'h₃ = u(t): ∫|h| dt = <b class="cl">∞</b>, u(t) in gives t·u(t)')


def u2L3():
    """2.7 Worked examples: y'' + 3y' + 2y = u in phase-variable form; step response by the state model"""
    a1, a0 = 3, 2
    A = [[0, 1], [-a0, -a1]]
    roots = sorted([(-a1 + s * math.sqrt(a1 * a1 - 4 * a0)) / 2 for s in (1, -1)], reverse=True)
    dt, x1, x2 = .001, 0., 0.
    for _ in range(1000):
        d1 = A[0][0] * x1 + A[0][1] * x2
        d2 = A[1][0] * x1 + A[1][1] * x2 + 1
        x1, x2 = x1 + dt * d1, x2 + dt * d2
    exact = .5 - math.exp(-1) + .5 * math.exp(-2)
    y = lambda t: .5 - math.exp(-t) + .5 * math.exp(-2 * t)
    yp = lambda t: math.exp(-t) - math.exp(-2 * t)
    # card: matrix A (last row lit) and the two states
    c = ctext(16, 22, 'A =', INK, 22, 'start', 700)
    c += f'<path d="M66 6 h-8 v66 h8 M176 6 h8 v66 h-8" fill="none" stroke="{INK}" stroke-width="2.5"/>'
    c += ctext(92, 32, f'{A[0][0]}', INK, 24, 'middle', 700) + ctext(150, 32, f'{A[0][1]}', INK, 24, 'middle', 700)
    c += f'<rect x="64" y="40" width="114" height="32" rx="6" fill="{ACC}" opacity=".22"/>'
    c += ctext(92, 64, g(A[1][0]), ACC, 24, 'middle', 700) + ctext(150, 64, g(A[1][1]), ACC, 24, 'middle', 700)
    c += ctext(16, 104, 'B = [0; 1]  C = [1 0]', MUT, 16, 'start', 600) + ctext(16, 130, f'roots {g(roots[0])}, {g(roots[1])}', ACC2, 16, 'start', 700)
    p = Plot(250, 26, 206, 92, 0, 5, 0, .55)
    c += p.axes(xt=[0, 1, 3, 5], yt=[.5], xunit='s') + p.curve(y, col=ACC, w=3.2) + p.curve(yp, col=ACC2, w=3.2)
    c += f'<circle cx="{p.X(1):.1f}" cy="{p.Y(x1):.1f}" r="5.5" fill="{ACC}"/>'
    c += ctext(p.X(5) - 4, p.Y(.5) - 8, 'x₁ = y', ACC, 15, 'end') + ctext(p.X(2.6), p.Y(yp(2.6)) - 8, 'x₂ = y′', ACC2, 15, 'start')
    setup()
    o = []
    # block diagram on the board: u -> sum -> integrator -> x2 -> integrator -> x1 = y, feedback gains -3 and -2
    o.append(trace([(0.4, 1.6), (1.2, 1.6)], INK, 3, .9) + label(0.5, 1.2, .1, 'u', INK, 17))
    o.append(ic(1.2, 1.1, .9, 1.0, 'Σ', h=.3, col=INK, size=16, pins=False))
    o.append(trace([(2.1, 1.6), (2.8, 1.6)], ACC2, 3.4, 1))
    o.append(ic(2.8, 1.0, 1.3, 1.2, '∫', h=.4, col=ACC2, size=22))
    o.append(trace([(4.1, 1.6), (4.9, 1.6)], ACC2, 3.4, 1) + label(4.5, 1.25, .1, 'x₂', ACC2, 16))
    o.append(ic(4.9, 1.0, 1.3, 1.2, '∫', h=.4, col=ACC, size=22))
    o.append(trace([(6.2, 1.6), (7.5, 1.6)], ACC, 3.4, 1) + label(7.1, 1.2, .1, 'y = x₁', ACC, 16))
    o.append(trace([(4.5, 1.6), (4.5, 4.2)], ACC2, 2.6, .8) + trace([(6.9, 1.6), (6.9, 6.2)], ACC, 2.6, .8))
    o.append(ic(3.9, 4.2, 1.2, .9, g(A[1][1]), h=.3, col=ACC, size=17))
    o.append(ic(6.3, 6.2, 1.2, .9, g(A[1][0]), h=.3, col=ACC, size=17))
    o.append(trace([(3.9, 4.65), (1.65, 4.65), (1.65, 2.1)], ACC, 2.6, .8) + trace([(6.3, 6.65), (1.4, 6.65), (1.4, 2.1)], ACC, 2.6, .8))
    return spec('ec-signals-u2-L3', 'Differential<br>Equations &amp;<br>State Models',
                f'Last row = <span class="gold">{g(A[1][0])} {g(A[1][1])}</span>: the<br>coefficients, signs <span class="cyan">FLIPPED</span>',
                "y″ + 3y′ + 2y = u", card_svg(c), board(o),
                [chip('left', 254, 'c', 'x₁ = y, x₂ = y′'), chip('left', 318, 'g', f'x₂′ = {g(A[1][0])}x₁ − {a1}x₂ + u'),
                 chip('right', 250, 'g', f'y(1) = {x1:.4f}', False), chip('right', 520, 'c', f'exact {exact:.4f}', False)],
                f'y″ = −{a0}y − {a1}y′ + u → A = [0 1; <b class="gl">{g(A[1][0])} {g(A[1][1])}</b>], B = [0; 1]<br>'
                f'Roots <b class="cl">{g(roots[0])}, {g(roots[1])}</b>; Euler, 1 ms steps: y(1) = {x1:.4f}')


# ================================================================ unit 3
def u3L1():
    """3.1 Worked example: pulse 1 on |t| < 1 s, period T0 = 4 s"""
    T0, tau = 4, 2
    w0 = 2 * PI / T0
    c0 = tau / T0
    cn = lambda n: c0 if n == 0 else math.sin(n * PI / 2) / (n * PI)
    an = lambda n: 2 * cn(n)
    p = Plot(30, 30, 190, 80, -5, 5, 0, 1.3)
    c = ptitle(125, 'x(t), T₀ = 4 s', ACC) + p.axes(xt=[-4, -1, 1, 4], yt=[1], xunit='s')
    c += p.poly([(t, v) for k in range(-2, 3) for t, v in ((4 * k - 1, 0), (4 * k - 1, 1), (4 * k + 1, 1), (4 * k + 1, 0))
                 if -5 <= t <= 5], ACC, 3)
    q = Plot(262, 30, 190, 80, -5.6, 5.6, -.15, .58)
    ns = list(range(-5, 6))
    c += ptitle(357, 'line spectrum c<tspan baseline-shift="sub" font-size="70%">n</tspan>', ACC2) + q.axes(xt=[-5, -3, -1, 1, 3, 5])
    c += q.stems(ns, [cn(n) for n in ns], ACC2, labels=False)
    c += ctext(q.X(0) - 8, q.Y(cn(0)) + 4, g(cn(0)), INK, 13, 'end', 500) + ctext(q.X(1) + 8, q.Y(cn(1)) + 4, g(cn(1), 3), INK, 13, 'start', 500)
    c += ctext(q.X(3) + 8, q.Y(cn(3)) + 5, g(cn(3), 3), INK, 13, 'start', 500)
    setup()
    X = lambda t: 0.5 + (t + 5) * 0.71
    yy = 4.5
    o = [plane_line([(X(-5), yy + .5), (X(5), yy + .5)], INK, 2.2, .6)]
    for t in (-4, -1, 0, 1, 4):
        o.append(plane_line([(X(t), yy + .4), (X(t), yy + .7)], INK, 2, .7) + (label(X(t), yy + 1.15, 0, g(t), MUT, 14) if t in (-4, 0, 4) else ''))
    for k in (-1, 0, 1):
        o.append(slabp(X(4 * k - 1), X(4 * k + 1), yy - .5, 1.25, ACC if k == 0 else shade(ACC, .82), d=1.0))
    o.append(glow([P(X(-5 + 10 * i / 160), yy, .1 + 1.25 * (c0 + an(1) * math.cos(w0 * (-5 + 10 * i / 160)))) for i in range(161)], ACC2, 4))
    o.append(label(X(0), yy - .5, 1.95, f'c₀ + a₁ cos(πt/2)', ACC2, 15))
    o.append(label(X(5) + .15, yy + 1.15, 0, 't, s', MUT, 13))
    return spec('ec-signals-u3-L1', 'Fourier Series<br>&amp; Transform',
                'c<sub>n</sub> takes <span class="gold">1/T₀</span>;<br>a<sub>n</sub> = 2c<sub>n</sub> takes <span class="cyan">2/T₀</span>',
                'pulse train, T₀ = 4 s', card_svg(c), board(o),
                [chip('left', 254, 'g', 'ω₀ = 2π/4 = π/2 rad/s'), chip('left', 318, 'g', f'c₀ = (1/4)(2) = {g(c0)}'),
                 chip('right', 250, 'c', f'c₁ = 1/π ≈ {g(cn(1))}', False), chip('right', 520, 'c', f'a₁ = 2c₁ = {g(an(1))}', False)],
                f'c<sub>n</sub> = (1/T₀)∫ x e<sup>−jnω₀t</sup> dt = sin(nπ/2)/(nπ): <b class="gl">c₀ = {g(c0)}</b><br>'
                f'a₁ = 2c₁ = <b class="cl">{g(an(1))}</b>, a₃ = {g(an(3))}; even n give zero')


def u3L2():
    """3.3 Worked example 2: x = e^-t u(t), h = e^-2t u(t), y = x * h by the convolution theorem"""
    A = 1 / (2 - 1); Bc = 1 / (1 - 2)
    y = lambda t: A * math.exp(-t) + Bc * math.exp(-2 * t) if t >= 0 else 0
    tp = math.log(2); yp = y(tp); y1 = y(1)
    p = Plot(36, 28, 196, 92, 0, 5, 0, 1.05)
    c = ptitle(134, 'time: y = x * h', ACC) + p.axes(xt=[0, 1, 3, 5], yt=[1, .25], xunit='s')
    c += p.curve(lambda t: math.exp(-t), col='#8A93A3', w=2.4, dash='6 5') + p.curve(lambda t: math.exp(-2 * t), col='#8A93A3', w=2.4, dash='2 4')
    c += p.curve(y, col=ACC, w=3.6) + f'<circle cx="{p.X(tp):.1f}" cy="{p.Y(yp):.1f}" r="5.5" fill="{ACC}"/>'
    q = Plot(270, 28, 180, 92, 0, 6, 0, 1.05)
    c += ptitle(360, 'ω, rad/s: Y = X · H', ACC2) + q.axes(xt=[0, 2, 4, 6], yt=[1, .5])
    c += q.curve(lambda w: 1 / math.hypot(1, w), col='#8A93A3', w=2.4, dash='6 5') + q.curve(lambda w: 1 / math.hypot(2, w), col='#8A93A3', w=2.4, dash='2 4')
    c += q.curve(lambda w: 1 / (math.hypot(1, w) * math.hypot(2, w)), col=ACC2, w=3.6)
    setup()
    o = []
    o.append(screen(1.5, 3.6, 1.5, .1, 1.4, lambda t: math.exp(-t) if t >= 0 else 0, -.5, 4, 0, 1.1, ACC, 90, frame=ACC))
    o.append(screen(4.3, 6.4, 1.5, .1, 1.4, lambda t: math.exp(-2 * t) if t >= 0 else 0, -.5, 4, 0, 1.1, ACC, 90, frame=ACC))
    o.append(label(2.55, 1.5, 1.85, 'x(t) = e' + ssup('−t') + 'u(t)', ACC, 14) + label(5.35, 1.5, 1.85, 'h(t) = e' + ssup('−2t') + 'u(t)', ACC, 14))
    o.append(trace([(2.6, 1.7), (2.6, 3.6), (3.0, 3.6)], ACC, 3.2, 1) + trace([(5.3, 1.7), (5.3, 3.6), (5.0, 3.6)], ACC, 3.2, 1))
    o.append(ic(3.0, 3.0, 2.0, 1.2, 'X(ω) · H(ω)', size=15, col=ACC2))
    o.append(trace([(4.0, 4.2), (4.0, 7.0)], ACC2, 3.4, 1))
    o.append(screen(2.0, 6.4, 7.2, .1, 1.3, lambda t: y(t), -.5, 6, 0, .29, ACC2, 120, frame=ACC2, dots=[tp], fill=True))
    o.append(label(1.6, 7.2, 1.0, f'y(t), peak {g(yp)}', ACC2, 16, 'end'))
    return spec('ec-signals-u3-L2', 'Fourier Rules,<br>Parseval &amp;<br>Frequency<br>Response',
                'Convolve in <span class="gold">TIME</span>,<br><span class="cyan">MULTIPLY</span> in ω',
                'e' + sup('−t') + 'u(t) * e' + sup('−2t') + 'u(t)', card_svg(c), board(o),
                [chip('left', 254, 'g', 'X(ω) = 1/(1 + jω)'), chip('left', 318, 'g', 'H(ω) = 1/(2 + jω)'),
                 chip('left', 520, 'c', f'peak {g(yp)} at ln 2 = {f2(tp)} s', False), chip('right', 520, 'g', f'y(1) = {y1:.4f}', False)],
                'Y = XH = 1/(1 + jω) − 1/(2 + jω): y = (e' + sup('−t') + ' − e' + sup('−2t') + ')u(t)<br>'
                f'y(1) = <b class="gl">{y1:.4f}</b>, peak <b class="cl">{g(yp)}</b> at ln 2 = {f2(tp)} s',
                'h1{font-size:68px !important;line-height:1.0 !important;margin-bottom:16px !important}')


def u3L3():
    """3.6 Worked example: ideal filter K = 2, td = 1 ms, |w| <= 2000; input cos(1000 t)"""
    K, td, wc, w = 2, 1e-3, 2000, 1000
    ph = -w * td; y0 = K * math.cos(ph)
    p = Plot(40, 30, 180, 86, -3000, 3000, -2.4, 2.6)
    c = ptitle(130, '|H| flat, phase −ωt<tspan baseline-shift="sub" font-size="70%">d</tspan>', ACC) + p.axes(xt=[-2000, 0, 2000], yt=[2], xfmt=lambda v: g(v))
    c += p.poly([(-3000, 0), (-wc, 0), (-wc, K), (wc, K), (wc, 0), (3000, 0)], ACC, 3.2)
    c += p.poly([(-wc, wc * td), (wc, -wc * td)], ACC2, 2.6, dash='6 4')
    c += f'<circle cx="{p.X(w):.1f}" cy="{p.Y(ph):.1f}" r="5" fill="{ACC2}"/>' + ctext(p.X(w) - 9, p.Y(ph) + 5, '−1 rad', ACC2, 14, 'end')
    q = Plot(262, 30, 178, 86, 0, 8e-3, -2.4, 2.4)
    c += ptitle(352, 'in and out, 1000 rad/s', ACC2) + q.axes(xt=[0, 4e-3, 8e-3], yt=[2, 1], xfmt=lambda v: g(v * 1000), xunit='ms')
    c += q.curve(lambda t: math.cos(w * t), col='#8A93A3', w=2.4, dash='6 5') + q.curve(lambda t: K * math.cos(w * (t - td)), col=ACC2, w=3.4)
    setup()
    o = []
    o.append(screen(0.6, 3.2, 5.2, .1, 1.5, lambda t: math.cos(w * t), 0, 8e-3, -2.3, 2.3, INK, 120, frame=INK, w=3))
    o.append(label(1.9, 5.2, 1.9, 'cos(1000t) V', INK, 15))
    o.append(trace([(3.2, 5.0), (3.9, 5.0), (3.9, 4.6)], GOLD))
    o.append(ic(3.4, 3.0, 2.4, 1.6, f'K = {K}, t<tspan font-size="70%" baseline-shift="sub">d</tspan> = 1 ms', size=14, col=ACC))
    o.append(trace([(5.8, 3.8), (6.4, 3.8), (6.4, 2.4)], ACC2, 3.4, 1))
    o.append(screen(5.0, 7.7, 1.8, .1, 1.5, lambda t: K * math.cos(w * (t - td)), 0, 8e-3, -2.3, 2.3, ACC2, 120, frame=ACC2))
    o.append(label(6.35, 1.8, 1.9, '2 cos(1000t − 1) V', ACC2, 15))
    return spec('ec-signals-u3-L3', 'Ideal Filters,<br>Correlation<br>&amp; Hilbert',
                'Flat <span class="gold">GAIN</span> and a<br>straight-line <span class="cyan">PHASE</span>',
                'ideal filter, K = 2, 1 ms', card_svg(c), board(o),
                [chip('left', 254, 'g', f'pass band |ω| ≤ {wc} rad/s'), chip('left', 520, 'g', f'|H| = K = {K}'),
                 chip('right', 250, 'c', f'∠H = −ωt<sub>d</sub> = {g(ph)} rad', False), chip('right', 520, 'c', f'y(0) = {y0:.4f} V', False)],
                f'|H({w})| = {K}, ∠H = −({w})(0.001) = <b class="gl">{g(ph)} rad</b><br>'
                f'y = 2 cos(1000t − 1) V, y(0) = <b class="cl">{y0:.4f} V</b>')


# ================================================================ unit 4
def u4L1():
    """4.1 Worked example: x(t) = e^-2t u(t) + e^3t u(-t), X(s) = -5/((s + 2)(s - 3)), ROC -2 < Re s < 3"""
    p1, p2 = -2, 3
    num = (p1) - (p2)                             # (s - 3) - (s + 2) = -5
    X0 = num / ((0 - p1) * (0 - p2))
    area = 1 / 2 + 1 / 3
    x = lambda t: math.exp(-2 * t) if t >= 0 else math.exp(3 * t)
    p = Plot(36, 30, 186, 84, -2, 3, 0, 1.15)
    c = ptitle(129, 'x(t), two-sided', ACC) + p.axes(xt=[-2, 0, 3], yt=[1], xunit='s')
    c += p.curve(x, col=ACC, w=3.4, n=200)
    q = Plot(262, 26, 196, 96, -4, 5, -2, 2)
    c += ptitle(360, 's-plane, ROC strip', ACC2)
    c += f'<rect x="{q.X(p1):.1f}" y="{q.T}" width="{q.X(p2) - q.X(p1):.1f}" height="{q.H}" fill="{ACC2}" opacity=".18"/>'
    c += q.axes(xt=[-2, 0, 3])
    for pv in (p1, p2):
        xx, yy = q.X(pv), q.Y(0)
        c += f'<path d="M{xx - 7:.1f},{yy - 7:.1f}L{xx + 7:.1f},{yy + 7:.1f}M{xx - 7:.1f},{yy + 7:.1f}L{xx + 7:.1f},{yy - 7:.1f}" stroke="{ACC}" stroke-width="3.5" stroke-linecap="round"/>'
    c += ctext(q.X(0) + 6, q.T + 14, 'jω', MUT, 14)
    setup()
    o = []
    S = lambda s: 0.9 + (s + 4) * 6.6 / 9
    Wy = lambda w: 4.2 - w * .95
    o.append(plane_poly([(S(p1), Wy(3.4)), (S(p2), Wy(3.4)), (S(p2), Wy(-3.4)), (S(p1), Wy(-3.4))], ACC2, .28))
    o.append(plane_line([(S(-4), Wy(0)), (S(5), Wy(0))], INK, 2.2, .7) + plane_line([(S(0), Wy(3.6)), (S(0), Wy(-3.6))], INK, 2.2, .7))
    for s in (p1, p2):
        o.append(plane_line([(S(s), Wy(3.4)), (S(s), Wy(-3.4))], ACC2, 2.2, .9, '6 5'))
    o.append(pole(S(p1), Wy(0)) + pole(S(p2), Wy(0)))
    o.append(label(S(p1), Wy(0), 1.35, '−2', ACC, 18) + label(S(p2), Wy(0), 1.35, '3', ACC, 18))
    o.append(label(S(0) - .1, Wy(-3.4) + .5, 0, 'jω', INK, 15) + label(S(5) + .25, Wy(0) + .35, 0, 'σ', INK, 16))
    o.append(label(S(.5), Wy(-1.6), .1, 'ROC', ACC2, 18))
    return spec('ec-signals-u4-L1', 'Laplace<br>Transform, ROC<br>&amp; Properties',
                'Same X(s), other <span class="gold">ROC</span>:<br>a different <span class="cyan">SIGNAL</span>',
                'two-sided signal', card_svg(c), board(o),
                [chip('left', 254, 'g', 'e' + sup('−2t') + 'u(t): Re s > −2'), chip('left', 318, 'g', 'e' + sup('3t') + 'u(−t): Re s < 3'),
                 chip('right', 250, 'c', 'jω axis inside: FT exists', False), chip('right', 520, 'c', 'X(0) = 5/6 = area', False)],
                'X(s) = 1/(s + 2) − 1/(s − 3) = <b class="gl">−5/((s + 2)(s − 3))</b><br>'
                f'ROC <b class="cl">−2 < Re(s) < 3</b>; X(0) = 1/2 + 1/3 = {g(X0, 3)}')


def u4L2():
    """4.4 Worked example: H(s) = 1/(s^2 + 3s + 2), poles -1, -2, h(t), unit-step response"""
    b, c_ = 3, 2
    r = sorted([(-b + s * math.sqrt(b * b - 4 * c_)) / 2 for s in (1, -1)], reverse=True)   # -1, -2
    A = 1 / (r[0] * r[1]); Bc = 1 / (r[0] * (r[0] - r[1])); Cc = 1 / (r[1] * (r[1] - r[0]))
    h = lambda t: (math.exp(r[0] * t) - math.exp(r[1] * t)) if t >= 0 else 0
    y = lambda t: (A + Bc * math.exp(r[0] * t) + Cc * math.exp(r[1] * t)) if t >= 0 else 0
    q = Plot(20, 28, 170, 90, -3, 1, -1.6, 1.6)
    c = ptitle(105, 'poles of H(s)', ACC)
    c += f'<rect x="{q.X(-3):.1f}" y="{q.T}" width="{q.X(0) - q.X(-3):.1f}" height="{q.H}" fill="{ACC2}" opacity=".10"/>'
    c += q.axes(xt=[-2, -1, 0])
    for pv in r:
        xx, yy = q.X(pv), q.Y(0)
        c += f'<path d="M{xx - 7:.1f},{yy - 7:.1f}L{xx + 7:.1f},{yy + 7:.1f}M{xx - 7:.1f},{yy + 7:.1f}L{xx + 7:.1f},{yy - 7:.1f}" stroke="{ACC}" stroke-width="3.5" stroke-linecap="round"/>'
    c += ctext(q.X(-1.5), q.T + 16, 'left half', ACC2, 13, 'middle')
    p = Plot(244, 28, 200, 92, 0, 6, 0, .6)
    c += ptitle(344, 'h(t) and step y(t)', ACC2) + p.axes(xt=[0, 2, 4, 6], yt=[.5, .25], xunit='s')
    c += p.curve(h, col=ACC, w=3.2) + p.curve(y, col=ACC2, w=3.4)
    c += f'<line x1="{p.X(0):.1f}" y1="{p.Y(.5):.1f}" x2="{p.X(6):.1f}" y2="{p.Y(.5):.1f}" stroke="{ACC2}" stroke-width="1.5" stroke-dasharray="5 5" opacity=".7"/>'
    setup()
    o = []
    o.append(screen(5.6, 7.6, 0.9, .1, 1.3, lambda t: 1 if t >= 0 else 0, -1, 4, 0, 1.15, INK, 60, frame=INK, w=3))
    o.append(label(6.6, 0.9, 1.7, 'u(t) in', INK, 15))
    o.append(trace([(5.6, 1.5), (4.6, 1.5), (4.6, 1.9)], GOLD))
    o.append(ic(2.2, 1.9, 3.2, 1.6, '1/(s² + 3s + 2)', size=15, col=ACC))
    o.append(trace([(3.0, 3.5), (3.0, 6.6)], ACC, 3.2, 1) + trace([(4.8, 3.5), (4.8, 5.6), (5.8, 5.6), (5.8, 6.6)], ACC2, 3.2, 1))
    o.append(screen(1.4, 4.0, 6.8, .1, 1.5, h, -.5, 6, 0, .3, ACC, 100, frame=ACC, fill=True))
    o.append(screen(4.6, 7.5, 6.8, .1, 1.5, y, -.5, 6, 0, .6, ACC2, 100, frame=ACC2))
    o.append(label(2.7, 6.8, 1.95, 'h(t)', ACC, 16) + label(6.05, 6.8, 1.95, f'y(t) → {g(A)}', ACC2, 16))
    return spec('ec-signals-u4-L2', 'Inverse Laplace<br>&amp; Transfer<br>Functions',
                f'Check the <span class="gold">POLES</span>:<br>{g(r[0])} and {g(r[1])}, so <span class="cyan">STABLE</span>',
                'H(s) = 1/(s² + 3s + 2)', card_svg(c), board(o),
                [chip('left', 254, 'g', '(s + 1)(s + 2): no zeros'), chip('left', 318, 'g', f'ROC Re(s) > {g(r[0])}'),
                 chip('right', 250, 'c', 'h = (e' + sup('−t') + ' − e' + sup('−2t') + ')u(t)', False), chip('right', 520, 'c', f'y(∞) = {g(A)} = H(0)', False)],
                'H(s) = 1/(s + 1) − 1/(s + 2): poles <b class="gl">−1, −2</b><br>'
                'step: y = (1/2 − e' + sup('−t') + ' + ½e' + sup('−2t') + f')u(t) → <b class="cl">{g(A)}</b>')


# ================================================================ unit 5
def u5L1():
    """5.1 Worked example: 3 cos(2 pi 200 t) + 2 cos(2 pi 450 t) sampled at 1000 Hz"""
    f1, f2_, fs = 200, 450, 1000
    fmax = max(f1, f2_); nyq = 2 * fmax; Ts = 1 / fs; cut = fs / 2; guard = fs - 2 * fmax
    copies = sorted([fs - f2_, fs - f1, fs + f1, fs + f2_])
    xt = lambda t: 3 * math.cos(2 * PI * f1 * t) + 2 * math.cos(2 * PI * f2_ * t)
    p = Plot(26, 26, 430, 92, 0, 1550, 0, 3.6)
    c = p.axes(xt=[0, 200, 450, 550, 800, 1000, 1200, 1450], xfmt=lambda v: g(v))
    c += f'<rect x="{p.X(fmax):.1f}" y="{p.T}" width="{p.X(fs - fmax) - p.X(fmax):.1f}" height="{p.H}" fill="{ACC2}" opacity=".14"/>'
    c += f'<polyline points="{p.X(0):.1f},{p.Y(3.3):.1f} {p.X(cut):.1f},{p.Y(3.3):.1f} {p.X(cut):.1f},{p.Y(0):.1f}" fill="none" stroke="{ACC2}" stroke-width="2.4" stroke-dasharray="7 5"/>'
    amp = {f1: 3, f2_: 2}
    for f in (f1, f2_):
        c += f'<line x1="{p.X(f):.1f}" y1="{p.Y(0):.1f}" x2="{p.X(f):.1f}" y2="{p.Y(amp[f]):.1f}" stroke="{ACC}" stroke-width="5"/>'
    for f in copies:
        a = amp[abs(f - fs)]
        c += f'<line x1="{p.X(f):.1f}" y1="{p.Y(0):.1f}" x2="{p.X(f):.1f}" y2="{p.Y(a):.1f}" stroke="#8A93A3" stroke-width="4"/>'
    c += ctext(p.X(cut) + 4, p.Y(3.3) - 4, f'cutoff {g(cut)} Hz', ACC2, 14, 'middle')
    c += ctext(p.X(1550), p.T + 6, 'Hz', MUT, 14, 'end', 500)
    setup()
    o = []
    # x(t) on a long screen in front, its samples every Ts = 1 ms marked; sampler with its clock and the LPF behind
    o.append(crystal(2.0, .2, '') + label(2.55, .45, .75, f'clock {g(fs)} Hz', GOLD, 13) + trace([(2.55, .7), (2.55, 1.6)], GOLD))
    o.append(ic(1.7, 1.6, 1.8, 1.5, 'sampler', size=14, col=ACC))
    o.append(trace([(3.5, 2.35), (4.5, 2.35)], ACC2, 3.4, 1))
    o.append(ic(4.5, 1.6, 2.2, 1.5, f'LPF {g(cut)} Hz', size=14, col=ACC2))
    o.append(trace([(6.7, 2.35), (7.6, 2.35)], ACC2, 3.4, 1))
    o.append(trace([(2.6, 6.4), (2.6, 3.1)], ACC, 3.2, 1))
    # x(t) on a long screen in front, its samples every Ts = 1 ms marked
    o.append(screen(2.4, 7.6, 6.6, .1, 1.7, xt, 0, 10e-3, -5.4, 5.4, ACC, 300, frame=ACC, w=3, dots=[k * Ts for k in range(11)]))
    o.append(label(2.0, 6.6, 1.3, 'x(t), dots every 1 ms', ACC, 15, 'end'))
    return spec('ec-signals-u5-L1', 'Sampling &amp;<br>Aliasing',
                f'Rate = <span class="gold">2f<sub>max</sub></span> = {g(nyq)} Hz;<br>frequency = <span class="cyan">f<sub>s</sub>/2</span> = {g(cut)} Hz',
                'lines from 0 to 1500 Hz', card_svg(c), board(o),
                [chip('left', 254, 'g', f'f<sub>max</sub> = {g(fmax)} Hz'), chip('left', 318, 'g', f'2 × {g(fmax)} = {g(nyq)} Hz'),
                 chip('right', 250, 'c', f'T<sub>s</sub> = {g(Ts * 1000)} ms', False), chip('right', 520, 'c', f'guard band {g(guard)} Hz', False)],
                f'Nyquist rate 2 × {g(fmax)} = <b class="gl">{g(nyq)} Hz</b> < f<sub>s</sub> = {g(fs)} Hz<br>'
                f'LPF cutoff f<sub>s</sub>/2 = <b class="cl">{g(cut)} Hz</b>, guard band {g(guard)} Hz')


def u5L2():
    """5.3 Worked example: band 5..6 kHz, band-pass sampling ranges, fs = 2.45 kHz"""
    fL, fH = 5, 6
    Bw = fH - fL
    mmax = int(fH // Bw)
    ranges = [(m, 2 * fH / m, 2 * fL / (m - 1)) for m in range(2, mmax + 1)]
    fs = 2.45; m = 5
    assert any(mm == m and lo <= fs <= hi for mm, lo, hi in ranges)
    zlo, zhi = (m - 1) * fs / 2, m * fs / 2
    ilo, ihi = fL - 2 * fs, fH - 2 * fs
    rng = lambda lo, hi: g(lo, 3) if abs(lo - hi) < 1e-9 else f'{g(lo, 3)}–{g(hi, 3)}'
    tbl = ('<table><tr><th>m</th>' + ''.join(f'<th{" class=on" if mm == m else ""}>{mm}</th>' for mm, lo, hi in ranges) + '</tr>'
           '<tr><td>f<sub>s</sub>, kHz</td>' + ''.join(f'<td{" class=on" if mm == m else ""}>{rng(lo, hi)}</td>' for mm, lo, hi in ranges) + '</tr></table>'
           f'<div class="lp">low-pass sampling needs f<sub>s</sub> &gt; 2 × {g(fH)} = {g(2 * fH)} kHz · pick <b>{g(fs)} kHz</b></div>')
    extra = """
.card.scope table{border-collapse:collapse;width:100%;margin-top:6px;font:600 17px 'IBM Plex Sans';color:#E6ECF1}
.card.scope th{font:600 15px 'IBM Plex Sans';color:#B7AEE0;padding:6px 6px;border-bottom:1.5px solid rgba(195,184,255,.3)}
.card.scope td{text-align:center;padding:10px 6px}.card.scope th:first-child,.card.scope td:first-child{text-align:left;color:#B7AEE0}
.card.scope .on{color:#3FE0C8;background:rgba(63,224,200,.14);font-weight:700}
.card.scope .lp{font:600 15px 'IBM Plex Sans';color:#C9D3DB;padding:8px 8px 6px}.card.scope .lp b{color:#3FE0C8}"""
    setup()
    o = []
    X = lambda f: 0.5 + f * 1.0
    yy = 4.6
    o.append(plane_line([(X(0), yy + .6), (X(7.2), yy + .6)], INK, 2.2, .6))
    for f in range(8):
        o.append(plane_line([(X(f), yy + .45), (X(f), yy + .75)], INK, 2, .7) + label(X(f), yy + 1.2, 0, g(f), MUT, 14))
    o.append(label(X(7.2) + .35, yy + 1.2, 0, 'kHz', MUT, 13))
    o.append(plane_poly([(X(zlo), yy - 1.0), (X(zhi), yy - 1.0), (X(zhi), yy + .6), (X(zlo), yy + .6)], ACC, .18))
    o.append(plane_poly([(X(0), yy - 1.0), (X(fs / 2), yy - 1.0), (X(fs / 2), yy + .6), (X(0), yy + .6)], ACC2, .16))
    o.append(plane_line([(X(fs / 2), yy - 1.0), (X(fs / 2), yy + .6)], ACC2, 2.4, .9, '6 5'))
    o.append(slabp(X(fL), X(fH), yy - .5, 1.2, ACC, d=.7))
    o.append(slabp(X(ilo), X(ihi), yy - .5, 1.2, ACC2, d=.7))
    o.append(label(X(5.5), yy - .2, 1.75, 'band', ACC, 16) + label(X(.6), yy - .2, 1.75, 'image', ACC2, 16))
    return spec('ec-signals-u5-L2', 'Band-pass<br>Sampling &amp;<br>Quantization',
                f'Yes: <span class="gold">{g(fs)} kHz</span> is enough<br>for a 1 kHz-wide <span class="cyan">BAND</span>',
                'valid f<sub>s</sub>, 5–6 kHz band', tbl, board(o),
                [chip('left', 254, 'g', f'band {g(fL)} to {g(fH)} kHz, B = {g(Bw)} kHz'), chip('left', 520, 'c', f'image {g(ilo, 2)} to {g(ihi, 2)} kHz'),
                 chip('right', 262, 'g', f'zone {m}: {g(zlo)} to {g(zhi)} kHz', False), chip('right', 520, 'c', f'f<sub>s</sub>/2 = {g(fs / 2)} kHz', False)],
                f'Zone {m}: {g(zlo)} to <b class="gl">{g(zhi)} kHz</b> holds the 5–6 kHz band<br>'
                f'Image 5 − 2 × 2.45 = {g(ilo, 2)} to <b class="cl">{g(ihi, 2)} kHz</b> < f<sub>s</sub>/2', extra)


def u5L3():
    """5.5 Worked example: x = [2, 1, 3], h = [1, 2], y = x * h; h = (0.5)^n u[n] is stable"""
    x, h = [2, 1, 3], [1, 2]
    y = [sum(x[k] * h[n - k] for k in range(len(x)) if 0 <= n - k < len(h)) for n in range(len(x) + len(h) - 1)]
    sh = 1 / (1 - .5)
    p = Plot(24, 32, 150, 84, -.6, 3.6, 0, 7)
    c = ptitle(99, 'x[n] and h[n]', ACC) + p.axes(xt=[0, 1, 2, 3])
    c += p.stems([0, 1, 2], x, ACC) + p.stems([.25, 1.25], h, '#8A93A3', r=4.5, labels=False)
    q = Plot(196, 32, 130, 84, -.6, 3.6, 0, 7)
    c += ptitle(261, 'y = x * h', ACC2) + q.axes(xt=[0, 1, 2, 3]) + q.stems(range(len(y)), y, ACC2)
    r = Plot(348, 32, 112, 84, -.5, 6.5, 0, 1.25)
    c += ptitle(404, '(0.5)<tspan baseline-shift="super" font-size="70%">n</tspan>u[n]', ACC) + r.axes(xt=[0, 3, 6]) + r.stems(range(7), [.5 ** n for n in range(7)], ACC, 4.5, labels=False)
    c += ctext(404, 140, f'Σ|h| = {g(sh)}', ACC, 15, 'middle', 700)
    setup()
    o = []
    for k, v in enumerate(x):
        o.append(column(2.4 + k * .8, 1.2, v, .4, ACC, text=g(v)))
    o.append(label(2.0, 1.45, 0, 'x[n]', ACC, 16, 'end'))
    o.append(trace([(4.6, 1.4), (5.2, 1.4), (5.2, 3.0)], ACC, 3.2, 1))
    o.append(ic(3.6, 3.0, 2.8, 1.5, 'h[n] = 1, 2', size=16, col=INK))
    o.append(trace([(4.4, 4.5), (4.4, 5.8)], ACC2, 3.4, 1))
    for k, v in enumerate(y):
        o.append(column(2.2 + k * .85, 6.2, v, .32, ACC2, text=g(v)))
    o.append(label(1.8, 6.45, 0, 'y[n]', ACC2, 16, 'end'))
    return spec('ec-signals-u5-L3', 'Convolution Sum<br>&amp; Difference<br>Equations',
                f'(0.5)<sup>n</sup>u[n]: Σ|h| = {g(sh)}, <span class="gold">STABLE</span><br>u[n]: Σ|h| = ∞, <span class="cyan">UNSTABLE</span>',
                'x = [2, 1, 3], h = [1, 2]', card_svg(c), board(o),
                [chip('left', 254, 'g', 'x[n] = 2, 1, 3'), chip('left', 318, 'g', 'h[n] = 1, 2'),
                 chip('right', 250, 'c', 'y[n] = ' + ', '.join(g(v) for v in y), False), chip('right', 520, 'c', f'{sum(y)} = {sum(x)} × {sum(h)}', False)],
                f'y[1] = 2·2 + 1·1 = {y[1]}; y = <b class="cl">' + ', '.join(g(v) for v in y) + '</b><br>'
                f'(0.5)<sup>n</sup>u[n]: Σ|h| = 1/(1 − 0.5) = <b class="gl">{g(sh)}</b>, stable',
                'h1{font-size:72px !important}')


# ================================================================ unit 6
def u6L1():
    """6.1 Worked example: DTFS, N = 8, x = 1, 1, 1, 0, 0, 0, 0, 0"""
    N = 8; x = [1, 1, 1, 0, 0, 0, 0, 0]
    X = [sum(x[n] * cmath.exp(-2j * PI * k * n / N) for n in range(N)) for k in range(N)]
    mag = [abs(v) for v in X]
    assert abs(X[7] - X[1].conjugate()) < 1e-12 and abs(X[2] - (-1j)) < 1e-12
    p = Plot(30, 34, 170, 80, -.5, 7.5, 0, 1.4)
    c = ptitle(115, 'one period, N = 8', ACC) + p.axes(xt=[0, 2, 4, 6]) + p.stems(range(N), x, ACC, labels=False)
    q = Plot(240, 34, 216, 80, -.5, 7.5, 0, 3.4)
    c += ptitle(348, '|X[k]|, no 1/N', ACC2) + q.axes(xt=[0, 1, 2, 3, 4, 5, 6, 7]) + q.stems(range(N), mag, ACC2, labels=False)
    for k in (0, 1, 7):
        c += f'<text x="{q.X(k):.1f}" y="{q.Y(mag[k]) - 9:.1f}" text-anchor="middle" class="ax" fill="{INK}">{g(mag[k], 3)}</text>'
    setup()
    o = []
    for k in range(N):
        o.append(column(2.2 + k * .7, 1.2, x[k], .6, ACC, w=.4))
    o.append(label(1.8, 1.45, 0, 'x[n]', ACC, 16, 'end'))
    o.append(trace([(4.0, 1.9), (4.0, 5.6)], GOLD, 2.6, .9) + label(4.3, 3.8, .05, 'DTFS', INK, 14, 'start'))
    for k in range(N):
        o.append(column(1.3 + k * .8, 6.0, mag[k], .52, ACC2 if k in (0, 1, 7) else shade(ACC2, .72), w=.46,
                        text=(g(mag[k], 3) if k in (0, 1, 7) else None)))
    o.append(label(0.9, 6.25, 0, '|X[k]|', ACC2, 16, 'end'))
    return spec('ec-signals-u6-L1', 'Fourier<br>Analysis in<br>Discrete Time',
                f'1/N goes in <span class="gold">x[n]</span>:<br>X[0] = {g(X[0].real)}, not 3/8 = <span class="cyan">{g(X[0].real / N)}</span>',
                'DTFS of a 3-sample pulse', card_svg(c), board(o),
                [chip('left', 254, 'g', 'X[0] = 1 + 1 + 1 = 3'), chip('left', 318, 'c', f'|X[1]| = {mag[1]:.4f}'),
                 chip('right', 250, 'c', 'X[2] = −j', False), chip('right', 520, 'g', 'X[7] = X*[1]', False)],
                f'X[1] = 1 + e' + sup('−jπ/4') + f' + e' + sup('−jπ/2') + f' = {X[1].real:.4f} − j{-X[1].imag:.4f}<br>'
                f'Synthesis: x[n] = <b class="gl">(1/N)</b> Σ X[k] e' + sup('j2πkn/N') + f', so X[0] = <b class="cl">{g(X[0].real)}</b>')


def u6L2():
    """6.3 Worked example 2: x = [1, 2, 3, 4], h = [1, 1, 0, 0]: circular and linear convolution"""
    x, h = [1, 2, 3, 4], [1, 1, 0, 0]
    N = 4
    yc = [sum(x[m] * h[(n - m) % N] for m in range(N)) for n in range(N)]
    hl = [1, 1]
    yl = [sum(x[k] * hl[n - k] for k in range(len(x)) if 0 <= n - k < len(hl)) for n in range(len(x) + len(hl) - 1)]
    L = len(x) + len(hl) - 1
    assert yc[0] == yl[0] + yl[4] and yc[1:] == yl[1:4]
    p = Plot(26, 34, 170, 80, -.6, 4.6, 0, 8.5)
    c = ptitle(111, f'circular, N = {N}', ACC) + p.axes(xt=[0, 1, 2, 3]) + p.stems(range(N), yc, ACC)
    q = Plot(256, 34, 200, 80, -.6, 4.6, 0, 8.5)
    c += ptitle(356, f'linear, length {L}', ACC2) + q.axes(xt=[0, 1, 2, 3, 4]) + q.stems(range(L), yl, ACC2)
    c += f'<path d="M{q.X(4):.1f},{q.Y(yl[4]) - 22:.1f} Q{(q.X(4) + p.X(0)) / 2:.1f},{q.T - 30:.1f} {p.X(0) + 14:.1f},{p.Y(yc[0]) - 16:.1f}" fill="none" stroke="{INK}" stroke-width="1.6" stroke-dasharray="4 4" opacity=".7"/>'
    setup()
    o = []
    cx, cy, R = 3.4, 2.3, 1.25
    ring = [(cx + R * math.cos(2 * PI * t / 60), cy + R * math.sin(2 * PI * t / 60)) for t in range(61)]
    o.append(plane_line(ring, ACC, 2.6, .8))
    pos = {n: (cx + R * math.cos(PI / 2 + 2 * PI * n / N + PI / 4), cy - R * math.sin(PI / 2 + 2 * PI * n / N + PI / 4)) for n in range(N)}
    for n in sorted(range(N), key=lambda n: pos[n][0] + pos[n][1]):
        o.append(column(pos[n][0] - .21, pos[n][1] - .21, yc[n], .28, ACC, text=f'y[{n}] = {yc[n]}', size=13))
    o.append(label(cx, cy, 0, 'mod 4', INK, 14))
    for n in range(L):
        o.append(column(2.0 + n * 1.05, 6.0, yl[n], .28, ACC2 if n < 4 else '#E6ECF1', text=g(yl[n])))
    o.append(label(1.5, 6.9, 0, 'linear', ACC2, 15))
    return spec('ec-signals-u6-L2', 'The DFT &amp;<br>the Z-transform',
                f'N = 4 <span class="gold">WRAPS</span> the {yl[4]} onto n = 0;<br>pad to {L} for <span class="cyan">LINEAR</span>',
                'x = [1, 2, 3, 4], h = [1, 1]', card_svg(c), board(o),
                [chip('left', 254, 'g', 'circular: ' + ', '.join(map(str, yc))), chip('left', 318, 'g', f'y[0] = 1 + 4 = {yc[0]}'),
                 chip('right', 250, 'c', f'pad to L ≥ {L}', False), chip('right', 520, 'c', 'linear: ' + ', '.join(map(str, yl)), False)],
                f'Circular: y[0] = x[0] + x[3] = 1 + 4 = <b class="gl">{yc[0]}</b>, y = ' + ', '.join(map(str, yc)) + '<br>'
                f'Linear: ' + ', '.join(map(str, yl)) + f' needs length <b class="cl">{L}</b>: zero-pad')


def u6L3():
    """6.7 Worked example: y[n] - 0.5 y[n - 1] = x[n]; H(z) = 1/(1 - 0.5 z^-1); step response"""
    a = .5
    yst = lambda n: (2 - a ** n) if n >= 0 else 0
    fin = 1 / (1 - a)
    q = Plot(56, 22, 120, 104, -1.4, 1.4, -1.25, 1.25)
    cxp, cyp = q.X(0), q.Y(0)
    c = f'<ellipse cx="{cxp:.1f}" cy="{cyp:.1f}" rx="{q.X(1) - q.X(0):.1f}" ry="{q.Y(0) - q.Y(1):.1f}" fill="{ACC2}" fill-opacity=".08" stroke="{INK}" stroke-width="1.8" stroke-dasharray="5 4"/>'
    c += q.axes(xt=[-1, 1])
    c += f'<path d="M{q.X(a) - 7:.1f},{cyp - 7:.1f}L{q.X(a) + 7:.1f},{cyp + 7:.1f}M{q.X(a) - 7:.1f},{cyp + 7:.1f}L{q.X(a) + 7:.1f},{cyp - 7:.1f}" stroke="{ACC}" stroke-width="3.5" stroke-linecap="round"/>'
    c += f'<circle cx="{cxp:.1f}" cy="{cyp:.1f}" r="6" fill="none" stroke="{ACC2}" stroke-width="3"/>'
    c += ctext(q.X(a), cyp - 14, '0.5', ACC, 14, 'middle') + ctext(q.X(1.05), q.T + 10, '|z| = 1', MUT, 13, 'start', 500)
    p = Plot(262, 30, 196, 90, -1.5, 8.5, 0, 2.4)
    c += ptitle(360, 'step response y[n]', ACC2) + p.axes(xt=[0, 2, 4, 6, 8], yt=[2, 1]) + p.stems(range(-1, 9), [yst(n) for n in range(-1, 9)], ACC2, 4.5, labels=False)
    c += f'<line x1="{p.X(-1.5):.1f}" y1="{p.Y(fin):.1f}" x2="{p.X(8.5):.1f}" y2="{p.Y(fin):.1f}" stroke="{ACC2}" stroke-width="1.5" stroke-dasharray="5 5" opacity=".7"/>'
    setup()
    o = []
    cx, cy, R = 4.0, 4.0, 2.9
    circ = lambda r: [(cx + r * math.cos(2 * PI * t / 80), cy + r * math.sin(2 * PI * t / 80)) for t in range(81)]
    o.append(plane_poly(circ(R * 1.28), ACC2, .16))
    o.append(plane_poly(circ(R * a), '#0D2A24', .9))
    o.append(plane_line(circ(R), INK, 2.6, .85) + plane_line(circ(R * a), ACC, 2, .8, '5 5'))
    o.append(plane_line([(cx - R * 1.3, cy), (cx + R * 1.3, cy)], INK, 2, .5) + plane_line([(cx, cy - R * 1.3), (cx, cy + R * 1.3)], INK, 2, .5))
    o.append(zero_mark(cx, cy) + pole(cx + R * a, cy, ACC, 1.1))
    o.append(label(cx + R * a, cy, 1.55, 'pole 0.5', ACC, 16) + label(cx + R * .72, cy - R * .72, .1, '|z| = 1', INK, 15))
    o.append(label(cx + R * .2, cy + R * 1.05, .1, 'ROC |z| > 0.5', ACC2, 15))
    return spec('ec-signals-u6-L3', 'The<br>Z-transform<br>at Work',
                'Pole <span class="gold">INSIDE</span> |z| = 1: stable;<br>a pole at z = 1 is <span class="cyan">NOT</span> BIBO',
                'y[n] − 0.5y[n − 1] = x[n]', card_svg(c), board(o),
                [chip('left', 254, 'g', 'H(z) = 1/(1 − 0.5z' + sup('−1') + ')'), chip('left', 520, 'c', 'h[n] = (0.5)' + sup('n') + 'u[n]'),
                 chip('right', 296, 'g', f'pole z = {g(a)}', False), chip('right', 470, 'c', f'y[n] → {g(fin)}', False)],
                f'Pole <b class="gl">z = {g(a)}</b>, ROC |z| > {g(a)} holds |z| = 1<br>'
                f'Step: y = (2 − 0.5' + sup('n') + f')u[n] = {g(yst(0))}, {g(yst(1))}, {g(yst(2))}, … → <b class="cl">{g(fin)}</b>')


ORDER = [u1L1, u1L2, u1L3, u1L4, u2L1, u2L2, u2L3, u3L1, u3L2, u3L3, u4L1, u4L2, u5L1, u5L2, u5L3, u6L1, u6L2, u6L3]


def specs():
    meta = {}
    tj = os.path.join(_here, 'thumbs.json')
    if not os.path.exists(tj):
        tj = os.path.join(_here, '..', 'thumbs.json')
    if os.path.exists(tj):
        meta = json.load(open(tj, encoding='utf-8'))['lessons']
    out = []
    for fn in ORDER:
        s = fn()
        m = meta.get(s['key'], {})
        s['subject'] = m.get('subject', SUBJECT)
        s['question'] = m.get('hook') or HOOKS[s['key']]
        topic = m.get('topic') or TOPICS[s['key']]
        assert s['title'].replace('<br>', ' ').replace('&amp;', '&') == topic, (s['key'], s['title'], topic)
        s['page_title'] = topic.replace('&', '&amp;') + ': Signals and Systems'
        out.append(s)
    return out


# subject, topic and hook as in ec-signals/thumbs.json on deliver/ec-signals (used when that file is not beside this one)
TOPICS = {
    'ec-signals-u1-L1': 'Signals & How to Sort Them', 'ec-signals-u1-L2': 'Standard Signals & How to Edit Them',
    'ec-signals-u1-L3': 'Sorting & Testing Systems', 'ec-signals-u1-L4': 'Signals as Vectors & Parseval',
    'ec-signals-u2-L1': 'LTI Systems & the Impulse Response', 'ec-signals-u2-L2': 'Convolution, Causality & Stability',
    'ec-signals-u2-L3': 'Differential Equations & State Models', 'ec-signals-u3-L1': 'Fourier Series & Transform',
    'ec-signals-u3-L2': 'Fourier Rules, Parseval & Frequency Response', 'ec-signals-u3-L3': 'Ideal Filters, Correlation & Hilbert',
    'ec-signals-u4-L1': 'Laplace Transform, ROC & Properties', 'ec-signals-u4-L2': 'Inverse Laplace & Transfer Functions',
    'ec-signals-u5-L1': 'Sampling & Aliasing', 'ec-signals-u5-L2': 'Band-pass Sampling & Quantization',
    'ec-signals-u5-L3': 'Convolution Sum & Difference Equations', 'ec-signals-u6-L1': 'Fourier Analysis in Discrete Time',
    'ec-signals-u6-L2': 'The DFT & the Z-transform', 'ec-signals-u6-L3': 'The Z-transform at Work'}
HOOKS = {
    'ec-signals-u1-L1': 'Energy signal or power signal?', 'ec-signals-u1-L2': 'Where does x(2t − 1) start?',
    'ec-signals-u1-L3': 'Is y[n] = x[n − 1] causal?', 'ec-signals-u1-L4': 'Divide by ‖φ‖ or by ‖φ‖²?',
    'ec-signals-u2-L1': 'Is y = 3x + 2 a linear system?', 'ec-signals-u2-L2': 'Is the ideal low-pass stable?',
    'ec-signals-u2-L3': 'What is the last row of A?', 'ec-signals-u3-L1': '1/T₀ or 2/T₀ in front of cₙ?',
    'ec-signals-u3-L2': 'Convolution in time is what in ω?', 'ec-signals-u3-L3': 'Is flat gain enough for no distortion?',
    'ec-signals-u4-L1': 'Is 1/(s + 2) enough without the ROC?', 'ec-signals-u4-L2': 'Are positive coefficients stable?',
    'ec-signals-u5-L1': 'Nyquist rate or Nyquist frequency?', 'ec-signals-u5-L2': 'Can 2.45 kHz sample a 6 kHz band?',
    'ec-signals-u5-L3': 'Is h[n] = u[n] a stable system?', 'ec-signals-u6-L1': 'Does 1/N go in X[k] or in x[n]?',
    'ec-signals-u6-L2': 'Circular or linear convolution?', 'ec-signals-u6-L3': 'Is a pole at z = 1 BIBO stable?'}
