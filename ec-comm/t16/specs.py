"""t16 split blueprint thumbnails for ec-comm (Analog and Digital Communication), ECE look.

One spec per lesson, each built from that lesson's own book worked example
(books/ece/ec-comm/ec-comm-u<N>.html on main, the chapters the lesson covers).
Every number is computed here and checked against the book's printed answer (the asserts).
Subject, topic and hook come from ec-comm/thumbs.json on deliver/ec-comm.

Build:  python3 t16_split.py build specs.py <out dir>   (t16_split.py from the data pack, thumbs/t16_split/)
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t16_split as T

B = T.B
P, pts, box, cyl, arrow = B.P, B.pts, B.box, T.cyl, T.arrow
D = 'ece'
ACC, ACC2 = T.DEPTS[D]['acc'], T.DEPTS[D]['acc2']      # violet, mint
WHITE, GREY, GOLD = '#E6ECF1', '#6B7B8A', '#D9B45A'
SUBJECT = 'ANALOG AND DIGITAL COMMUNICATION'


def g(v, n=4):
    return f'{v:.{n}g}'


def near(a, b, tol):
    assert abs(a - b) <= tol, (a, b)
    return a


def Q(x):
    return .5 * math.erfc(x / math.sqrt(2))


def sci(v, d=2):
    """3.87×10<sup>−6</sup>"""
    e = math.floor(math.log10(abs(v)))
    m = v / 10 ** e
    return f'{m:.{d}f}×10<sup>{"−" if e < 0 else ""}{abs(e)}</sup>'


# ================================================================ card plots (470 x 144)
class Ax:
    """a plot box: pixel corners (x0, top) to (x1, bottom), data ranges, optional log y"""

    def __init__(s, x0, x1, top, bot, xr, yr, logy=False):
        s.x0, s.x1, s.top, s.bot, s.xr, s.yr, s.logy = x0, x1, top, bot, xr, yr, logy

    def X(s, v):
        return s.x0 + (v - s.xr[0]) / (s.xr[1] - s.xr[0]) * (s.x1 - s.x0)

    def Y(s, v):
        if s.logy:
            v = math.log10(max(v, 1e-30))
            a, b = math.log10(s.yr[0]), math.log10(s.yr[1])
        else:
            a, b = s.yr
        return s.bot - (v - a) / (b - a) * (s.bot - s.top)

    def axes(s, y0=None):
        yb = s.Y(y0) if y0 is not None else s.bot
        return (f'<line x1="{s.x0}" y1="{yb:.1f}" x2="{s.x1}" y2="{yb:.1f}" stroke="{GREY}" stroke-width="1.5"/>'
                f'<line x1="{s.x0}" y1="{s.top - 4}" x2="{s.x0}" y2="{s.bot}" stroke="{GREY}" stroke-width="1.5"/>')

    def line(s, xy, col, w=3, dash=None, op=1):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        return (f'<polyline points="{" ".join(f"{s.X(a):.1f},{s.Y(b):.1f}" for a, b in xy)}" fill="none" stroke="{col}" '
                f'stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round" opacity="{op}"{d}/>')

    def area(s, xy, col, op=.18, base=None):
        b = s.yr[0] if base is None else base
        p = [(xy[0][0], b)] + list(xy) + [(xy[-1][0], b)]
        return f'<polygon points="{" ".join(f"{s.X(a):.1f},{s.Y(c):.1f}" for a, c in p)}" fill="{col}" opacity="{op}"/>'

    def stem(s, x, y, col, w=3.5, r=5, base=0):
        return (f'<line x1="{s.X(x):.1f}" y1="{s.Y(base):.1f}" x2="{s.X(x):.1f}" y2="{s.Y(y):.1f}" stroke="{col}" stroke-width="{w}"/>'
                f'<circle cx="{s.X(x):.1f}" cy="{s.Y(y):.1f}" r="{r}" fill="{col}"/>')

    def dot(s, x, y, col, r=5):
        return f'<circle cx="{s.X(x):.1f}" cy="{s.Y(y):.1f}" r="{r}" fill="{col}"/>'

    def xt(s, x, t, dy=16, anchor='middle', col=None):
        f = f' fill="{col}"' if col else ''
        return f'<text x="{s.X(x):.1f}" y="{s.bot + dy}" text-anchor="{anchor}" class="ax"{f}>{t}</text>'

    def yt(s, y, t):
        return f'<text x="{s.x0 - 6}" y="{s.Y(y) + 5:.1f}" text-anchor="end" class="ax">{t}</text>'

    def tx(s, x, y, t, col=WHITE, anchor='middle', cls='ax', dy=0):
        return f'<text x="{s.X(x):.1f}" y="{s.Y(y) + dy:.1f}" text-anchor="{anchor}" class="{cls}" fill="{col}">{t}</text>'


def title(x, t, col):
    return f'<text x="{x}" y="16" text-anchor="middle" class="pt" fill="{col}">{t}</text>'


def card(inner):
    return f'<svg width="470" height="144" viewBox="0 0 470 144">{inner}</svg>'


def hbar(x, y, w, h, col, op=.85):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(w, 1):.1f}" height="{h}" rx="3" fill="{col}" opacity="{op}"/>'


# ================================================================ isometric board helpers (PCB board as in the ECE sample)
PCB = ('<defs><linearGradient id="pcb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#17463C"/><stop offset="1" stop-color="#0D2A24"/></linearGradient>'
       '<linearGradient id="ic" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2A2E36"/><stop offset="1" stop-color="#121418"/></linearGradient>'
       '<linearGradient id="xt" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8E99A6"/><stop offset=".4" stop-color="#F2F5F8"/><stop offset="1" stop-color="#7C8794"/></linearGradient>'
       '<linearGradient id="can" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#26205A"/><stop offset=".35" stop-color="#6B5BC4"/><stop offset=".6" stop-color="#3E3486"/><stop offset="1" stop-color="#1A1640"/></linearGradient>'
       '</defs>')


def setup():
    B.U, B.OX, B.OY = 33, 952, 318


def board(parts):
    return T.iso_board(D, [PCB] + parts, top='url(#pcb)', left='#0A1F1A', right='#0E2822')


def trace(path, z=.01, col=GOLD, w=2.6, op=.85):
    return (f'<polyline points="{pts(*[P(a, b, z) for a, b in path])}" fill="none" stroke="{col}" stroke-width="{w}" '
            f'stroke-linejoin="round" stroke-linecap="round" opacity="{op}"/>')


def glow(path, col=ACC2, z=.02, w=4):
    return f'<g filter="url(#gl)">{trace(path, z, col, w, 1)}</g>'


def pad(a, b):
    x, y = P(a, b)
    return f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="4.5" ry="2.6" fill="#0D2A24" stroke="{GOLD}" stroke-width="1.8"/>'


def lab(a, b, z, t, col='#F1F4F7', size=15, dy=5):
    x, y = P(a, b, z)
    return f'<text x="{x:.1f}" y="{y + dy:.1f}" text-anchor="middle" class="capl" fill="{col}" style="font-size:{size}px">{t}</text>'


def chip(x, y, w, d, t, h=.42, pins=True, col='#F1F4F7', size=15):
    """a black IC with silver pins on its two visible long sides and a label on top"""
    o = box(x, y, w, d, h, 'url(#ic)', '#0B0D10', '#1A1D22')
    if pins:
        n = max(2, int(w / .55))
        for k in range(n):
            px = x + (k + .5) * w / n
            o = box(px - .1, y + d, .2, .22, .14, '#C9D0D6', '#7D8792', '#9AA4AE', z0=.06) + o
        m = max(2, int(d / .55))
        for k in range(m):
            py = y + (k + .5) * d / m
            o += box(x + w, py - .1, .22, .2, .14, '#C9D0D6', '#7D8792', '#9AA4AE', z0=.06)
    return o + lab(x + w / 2, y + d / 2, h, t, col, size)


def module(x, y, w, d, h, t, top='#3B3478', left='#1E1946', right='#2A245E', col='#F1F4F7', size=15):
    return box(x, y, w, d, h, top, left, right) + lab(x + w / 2, y + d / 2, h, t, col, size)


def crystal(x, y, t, w=1.1, d=.62):
    return box(x, y, w, d, .38, 'url(#xt)', '#6E7884', '#9AA4AE') + lab(x + w / 2, y + d / 2, .38, t, '#1A1F26', 12, 4)


def can(a, b, t, h=70, rx=20, ry=11):
    x, y = P(a, b)
    return (cyl(x, y, rx, ry, h, 'url(#can)', '#C9B3FF') +
            f'<text transform="translate({x + 5:.1f} {y - 12:.1f}) rotate(-90)" class="capl" style="font-size:12px">{t}</text>')


def resistor(x, y, L, t, along='x'):
    """a beige axial resistor lying on the board with colour bands"""
    if along == 'x':
        o = box(x, y, L, .42, .42, '#D9C7A0', '#9C8A64', '#B8A67E', z0=.05)
        for k, c in enumerate(('#7A3B1A', '#111', '#E0A030')):
            o += box(x + L * (.22 + .16 * k), y - .01, .09, .44, .44, c, c, c, z0=.05)
        o += trace([(x - .5, y + .21), (x, y + .21)], .2, '#B8C0C8', 3, 1) + trace([(x + L, y + .21), (x + L + .5, y + .21)], .2, '#B8C0C8', 3, 1)
        return o + lab(x + L / 2, y + .21, .5, t, '#1A1F26', 12, -6)
    o = box(x, y, .42, L, .42, '#D9C7A0', '#9C8A64', '#B8A67E', z0=.05)
    for k, c in enumerate(('#7A3B1A', '#111', '#E0A030')):
        o += box(x - .01, y + L * (.22 + .16 * k), .44, .09, .44, c, c, c, z0=.05)
    return o + lab(x + .21, y + L / 2, .5, t, '#1A1F26', 12, -6)


def antenna(a, b, h=3.4):
    (x0, y0), (x1, y1) = P(a, b, .3), P(a, b, h)
    return (box(a - .3, b - .3, .6, .6, .3, '#5B6470', '#2E343C', '#3E4650') +
            f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#C9D0D6" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M{x1 - 18:.1f},{y1 - 16:.1f} L{x1:.1f},{y1 + 10:.1f} L{x1 + 18:.1f},{y1 - 16:.1f}" fill="none" stroke="#C9D0D6" stroke-width="4" stroke-linecap="round"/>')


def float_wave(x0, x1, y, z0, amp, f, n=160, col='#E8FFFA', w=3):
    """a waveform drawn upright above the line from (x0, y) to (x1, y) at height z0"""
    p = [P(x0 + (x1 - x0) * k / n, y, z0 + amp * f(k / n)) for k in range(n + 1)]
    return f'<g filter="url(#gl)"><polyline points="{pts(*p)}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"/></g>'


def float_wave_d(a0, b0, a1, b1, z0, amp, f, n=160, col='#E8FFFA', w=3):
    """a waveform drawn upright above the board line (a0, b0) to (a1, b1)"""
    p = [P(a0 + (a1 - a0) * k / n, b0 + (b1 - b0) * k / n, z0 + amp * f(k / n)) for k in range(n + 1)]
    return f'<g filter="url(#gl)"><polyline points="{pts(*p)}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"/></g>'


def wave_h(a, b, L, z0, amp, f, n=200, col='#E8FFFA', w=2.6):
    """a waveform floating along the screen-horizontal board direction (+x, -y) from (a, b), L board units long"""
    return float_wave_d(a, b, a + L, b - L, z0, amp, f, n, col, w)


def flow(a0, b0, a1, b1, col=ACC2, z=.6, w=5):
    (x0, y0), (x1, y1) = P(a0, b0, z), P(a1, b1, z)
    return f'<g filter="url(#gl)">{arrow(x0, y0, x1, y1, col, w)}</g>'


def bar3(a, b, h, col_top, col_l, col_r, w=.6, t=None, tcol='#F1F4F7'):
    o = box(a, b, w, w, h, col_top, col_l, col_r)
    if t:
        o += lab(a + w / 2, b + w / 2, h + .35, t, tcol, 13, 0)
    return o


def ring(a, b, z, r, col, w=3, fill='none'):
    x, y = P(a, b, z)
    return f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{r}" ry="{r * .58:.1f}" fill="{fill}" stroke="{col}" stroke-width="{w}"/>'


def chips(*c):
    return [dict(side=s, top=t, kind=k, text=x) for s, t, k, x in c]


def spec(key, topic_title, page, question, take, card_title, card_svg, brd, chip_list, summary, extra_css=''):
    return dict(key=key, dept=D, subject=SUBJECT, title=topic_title, question=question, takeaway=take, tag='Book example',
                card_title=card_title, card=card_svg, board=brd, chips=chip_list, summary=summary, page_title=page, css=extra_css)


def G(t):
    return f'<span class="gold">{t}</span>'


def C(t):
    return f'<span class="cyan">{t}</span>'


def gl(t):
    return f'<b class="gl">{t}</b>'


def cl(t):
    return f'<b class="cl">{t}</b>'


def sinc(x):
    return 1.0 if abs(x) < 1e-12 else math.sin(math.pi * x) / (math.pi * x)


# ================================================================ unit 1
def u1L1():
    """1.2 Worked example 2: the 2 V, 1 ms pulse on a 10 kHz carrier"""
    A, Tp, fc = 2, 1e-3, 10e3
    X0 = A * Tp                                    # 2e-3 V/Hz
    peak = X0 / 2                                  # each copy
    lo, hi = fc - 1 / Tp, fc + 1 / Tp              # 9, 11 kHz
    E = A ** 2 * Tp; Ey = 2 * .25 * E
    near(X0 * 1e3, 2, 1e-9); near(peak * 1e3, 1, 1e-9); near(hi - lo, 2000, 1e-6); near(Ey, 2e-3, 1e-12)
    a = Ax(40, 222, 34, 112, (-3, 3), (-.5, 2.2))
    s = title(131, 'pulse X(f)', ACC) + a.axes(0)
    xy = [(k / 50, 2 * abs(sinc(k / 50))) for k in range(-150, 151)]
    s += a.area(xy, ACC, .16, 0) + a.line(xy, ACC, 3)
    s += a.yt(2, '2') + a.yt(0, '0') + a.xt(-1, '−1') + a.xt(1, '1') + a.xt(3, 'kHz', anchor='end') + a.dot(0, 2, ACC)
    b = Ax(276, 462, 34, 112, (-13, 13), (-.5, 2.2))
    s += title(369, 'on the carrier Y(f)', ACC2) + b.axes(0)
    for c in (-10, 10):
        xy = [(c + k / 50, abs(sinc(k / 50))) for k in range(-150, 151)]
        s += b.area(xy, ACC2, .16, 0) + b.line(xy, ACC2, 3) + b.dot(c, 1, ACC2)
    s += b.line([(-13, 2), (13, 2)], GREY, 1, '4 4') + b.tx(0, 2, '2', GREY, dy=-5)
    s += b.yt(1, '1') + b.xt(-10, '−10') + b.xt(10, '10') + b.xt(0, '0 kHz')
    setup()
    o = [trace([(1.2, 5.6), (3.0, 5.6), (3.0, 4.2)]), trace([(3.4, 1.4), (3.4, 3.4)]), trace([(4.4, 4.0), (6.6, 4.0), (6.6, 2.8)])]
    o += [pad(1.2, 5.6), pad(6.6, 2.8)]
    o.append(module(.9, 4.9, 1.5, 1.2, .55, '2 V · 1 ms', size=13))
    o.append(crystal(2.9, .9, '10 kHz'))
    o.append(chip(2.5, 3.4, 1.9, 1.3, '×', size=22))
    o.append(wave_h(.6, 6.4, 1.6, 1.4, .8, lambda t: 1 if .25 < t < .75 else 0, n=120))
    o.append(wave_h(4.6, 5.4, 3.0, 1.2, .8, lambda t: (math.cos(2 * math.pi * 20 * (t - .25)) if .25 < t < .75 else 0), n=400))
    return spec('ec-comm-u1-L1', 'Modulation &amp;<br>the Spectrum', 'Modulation &amp; the Spectrum',
                'Why does the spectrum split in two?',
                f'A carrier makes {G("TWO")} copies,<br>each at {C("HALF")} height',
                '1 ms pulse on 10 kHz', card(s), board(o),
                chips(('left', 256, 'g', 'X(0) = 2 mV/Hz'), ('left', 534, 'c', 'first null 1 kHz'),
                      ('right', 262, 'g', '1 mV/Hz at ±10 kHz'), ('right', 534, 'c', '9 to 11 kHz: 2 kHz')),
                f'Y(f) = ½X(f − 10 kHz) + ½X(f + 10 kHz)<br>peak 2 → {gl("1 mV/Hz")} each, band {cl("9 to 11 kHz")}')


def u1L2():
    """1.4 Worked example 1: Gaussian noise, sigma 2 mV"""
    mu, sg = 0, 2
    z = (4 - mu) / sg
    p_tail = Q(z); p_band = 1 - 2 * Q(1)
    near(p_tail, .0228, 5e-5); near(p_band, .6827, 5e-5)
    pdf = lambda v: math.exp(-.5 * ((v - mu) / sg) ** 2) / (sg * math.sqrt(2 * math.pi))
    pk = pdf(0)
    def panel(x0, lo, hi, col, ttl, val):
        a = Ax(x0 + 14, x0 + 214, 34, 112, (-7, 7), (0, pk * 1.12))
        xy = [(v / 10, pdf(v / 10)) for v in range(-70, 71)]
        sh = [(v / 10, pdf(v / 10)) for v in range(int(lo * 10), int(hi * 10) + 1)]
        s = title(x0 + 114, ttl, col) + a.axes() + a.area(sh, col, .45) + a.line(xy, WHITE, 2.6)
        s += a.xt(0, '0') + a.xt(-4, '−4') + a.xt(4, '4') + a.xt(-2, '−2') + a.xt(2, '2') + a.xt(7, 'mV', anchor='end')
        mid = (max(lo, -6) + min(hi, 6)) / 2
        s += a.tx(mid if hi < 7 else 5.4, pdf(mid if hi < 7 else 4.6) + pk * .32 if hi >= 7 else pdf(mid) * .45, val, col, cls='pt')
        return s
    s = panel(0, -2, 2, ACC2, 'area −2 to 2 mV', f'{p_band:.4f}') + panel(240, 4, 7, ACC, 'area above 4 mV', f'{p_tail:.4f}')
    setup()
    o = [trace([(1.0, 1.4), (1.0, 3.0), (2.0, 3.0)]), pad(1.0, 1.4)]
    o.append(module(.6, 3.0, 1.4, 1.2, .7, 'noise', size=14))
    o.append(lab(1.3, 3.6, .7, 'σ = 2 mV', ACC2, 12, 20))
    # a histogram of the noise samples: bins of 1 mV from -6 to 6 mV, bar height ~ probability in the bin
    for k in range(-6, 6):
        pbin = Q(k / sg) - Q((k + 1) / sg)
        h = pbin * 9
        a = 3.0 + (k + 6) * .38
        top = '#FFD27A' if k >= 4 else ('#7FF0DC' if -2 <= k < 2 else '#8C7FD6')
        lf = '#B08A2E' if k >= 4 else ('#2E9C88' if -2 <= k < 2 else '#4A3F96')
        rt = '#C99E3A' if k >= 4 else ('#3AB59F' if -2 <= k < 2 else '#5C50AE')
        o.append(box(a, 5.0, .3, .9, max(h, .04), top, lf, rt))
    o.append(trace([(4.52, 4.5), (4.52, 6.4)], .01, ACC2, 2.4, 1) + trace([(6.0, 4.5), (6.0, 6.4)], .01, ACC2, 2.4, 1))
    o.append(trace([(6.76, 4.5), (6.76, 6.4)], .01, '#FFD27A', 2.4, 1))
    o.append(lab(6.76, 4.3, 0, '4 mV', '#FFD27A', 12, 0))
    return spec('ec-comm-u1-L2', 'Complex<br>Envelope &amp;<br>Random Signals', 'Complex Envelope &amp; Random Signals',
                'Is a PDF height a probability?',
                f'Only the {G("AREA")} under a PDF<br>is a {C("PROBABILITY")}',
                'Gaussian noise, σ = 2 mV', card(s), board(o),
                chips(('left', 256, 'c', 'mean 0, σ = 2 mV'), ('left', 534, 'g', 'z = 4/2 = 2'),
                      ('right', 262, 'g', 'P(V > 4 mV) = Q(2)'), ('right', 538, 'c', '1 − 2Q(1) = 0.6827')),
                f'P(V > 4 mV) = Q(2) = {gl("0.0228")}, about 2.3 %<br>P(−2 &lt; V &lt; 2 mV) = 1 − 2(0.1587) = {cl("0.6827")}')


def u1L3():
    """1.6 Worked example 2: noise of 20 kOhm and 50 kOhm"""
    k, Tk, Bw = 1.38e-23, 290, 1e5
    c = 4 * k * Tk * Bw
    v1, v2 = math.sqrt(c * 2e4) * 1e6, math.sqrt(c * 5e4) * 1e6
    vs = math.sqrt(c * 7e4) * 1e6
    Rp = 20 * 50 / 70; vp = math.sqrt(c * Rp * 1e3) * 1e6
    near(v1, 5.66, .005); near(v2, 8.95, .005); near(vs, 10.59, .005); near(vp, 4.78, .005); near(math.hypot(v1, v2), vs, 1e-9)
    wrong = round(v1, 2) + round(v2, 2)
    near(wrong, 14.61, 1e-9)
    s = title(112, 'RMS noise, µV', WHITE)
    rows = [('20 kΩ', v1, ACC, False), ('50 kΩ', v2, ACC, False), ('added', wrong, '#FF9C9C', True), ('series', vs, ACC2, False), ('parallel', vp, ACC2, False)]
    for i, (n, v, col, bad) in enumerate(rows):
        y = 26 + i * 23
        s += f'<text x="66" y="{y + 14}" text-anchor="end" class="ax">{n}</text>'
        if bad:
            s += f'<rect x="72" y="{y + 2}" width="{v * 9:.1f}" height="16" rx="3" fill="none" stroke="{col}" stroke-width="1.6" stroke-dasharray="5 4"/>'
            s += f'<text x="{78 + v * 9:.1f}" y="{y + 15}" class="ax" fill="{col}">not {v:.2f}</text>'
        else:
            s += hbar(72, y + 2, v * 9, 16, col) + f'<text x="{78 + v * 9:.1f}" y="{y + 15}" class="ax" fill="{WHITE}">{v:.2f}</text>'
    # right: the right triangle of the two RMS values
    sc = 8.5
    x0, y0 = 302, 124
    xa, ya = x0 + v2 * sc, y0
    xb, yb = x0 + v2 * sc, y0 - v1 * sc
    s += title(366, 'squares add', ACC2)
    s += f'<polygon points="{x0},{y0} {xa:.1f},{ya} {xb:.1f},{yb:.1f}" fill="{ACC2}" fill-opacity=".10" stroke="none"/>'
    s += f'<line x1="{x0}" y1="{y0}" x2="{xa:.1f}" y2="{ya}" stroke="{ACC}" stroke-width="3.5"/><line x1="{xa:.1f}" y1="{ya}" x2="{xb:.1f}" y2="{yb:.1f}" stroke="{ACC}" stroke-width="3.5"/>'
    s += f'<line x1="{x0}" y1="{y0}" x2="{xb:.1f}" y2="{yb:.1f}" stroke="{ACC2}" stroke-width="4"/>'
    s += f'<path d="M{xa - 10:.1f},{ya} v-10 h10" fill="none" stroke="{GREY}" stroke-width="1.5"/>'
    s += f'<text x="{(x0 + xa) / 2:.1f}" y="{ya + 16}" text-anchor="middle" class="ax">{v2:.2f}</text>'
    s += f'<text x="{xa + 6:.1f}" y="{(ya + yb) / 2 + 5:.1f}" class="ax">{v1:.2f}</text>'
    s += f'<text x="{(x0 + xb) / 2 - 8:.1f}" y="{(y0 + yb) / 2 - 6:.1f}" text-anchor="end" class="pt" fill="{ACC2}">{vs:.2f}</text>'
    setup()
    o = [trace([(1.0, 4.2), (1.6, 4.2)]), trace([(3.9, 4.2), (4.5, 4.2)]), trace([(6.8, 4.2), (7.2, 4.2), (7.2, 2.6)]),
         trace([(1.0, 4.2), (1.0, 2.0), (5.2, 2.0)]), pad(1.0, 4.2), pad(7.2, 2.6)]
    o.append(resistor(1.6, 4.0, 2.3, '20 kΩ'))
    o.append(resistor(4.5, 4.0, 2.3, '50 kΩ'))
    o.append(module(5.2, 1.0, 2.0, 1.6, .9, '10.59 µV', top='#13201C', left='#0B1412', right='#101B18', col=ACC2, size=15))
    o.append(lab(6.2, 1.8, .9, 'RMS', '#9FB8B0', 11, -14))
    o.append(float_wave(1.4, 7.0, 4.2, 1.5, .45, lambda t: math.sin(23 * t) * .5 + math.sin(51 * t + 1) * .3 + math.sin(87 * t + 2) * .2, n=260, w=2.2))
    return spec('ec-comm-u1-L3', 'Noise &amp;<br>Noise Figure', 'Noise &amp; Noise Figure',
                'Do noise voltages simply add?',
                f'Mean {G("SQUARES")} add,<br>not {C("RMS")} volts',
                '20 kΩ and 50 kΩ at 290 K', card(s), board(o),
                chips(('left', 256, 'c', '100 kHz, 290 K'), ('right', 262, 'g', '5.66 µV and 8.95 µV'),
                      ('right', 534, 'c', 'parallel 4.78 µV', ), ('left', 534, 'g', 'not 14.61 µV')),
                f'series 70 kΩ: √(5.66² + 8.95²) = {gl("10.59 µV")}<br>parallel 14.29 kΩ: {cl("4.78 µV")}, below either')


# ================================================================ unit 2
def u2L1():
    """2.1 Worked example 1: AM with 12 V peaks and 4 V dips"""
    Vmax, Vmin, fc, fm, R = 12, 4, 1000, 5, 50
    m = (Vmax - Vmin) / (Vmax + Vmin); Ac = (Vmax + Vmin) / 2; Am = (Vmax - Vmin) / 2
    sb = m * Ac / 2
    Pc = Ac ** 2 / (2 * R); Psb = sb ** 2 / (2 * R); Pt = Pc + 2 * Psb; eta = 2 * Psb / Pt
    near(m, .5, 0); near(Ac, 8, 0); near(sb, 2, 0); near(Pc, .64, 1e-9); near(Pt, .72, 1e-9); near(eta * 100, 11.1, .05)
    a = Ax(40, 222, 30, 116, (0, 2), (-13, 13))
    env = [(t / 100, Ac + Am * math.cos(2 * math.pi * t / 100)) for t in range(201)]
    s = title(131, 'AM wave (2 tone cycles)', ACC) + a.axes(0)
    s += a.area(env, ACC, .14, 0) + a.area([(x, -y) for x, y in env], ACC, .14, 0)
    car = [(t / 400, (Ac + Am * math.cos(2 * math.pi * t / 400)) * math.cos(2 * math.pi * t / 400 * 18)) for t in range(801)]
    s += a.line(car, ACC, 1.4, op=.7)
    s += a.line(env, WHITE, 2.6) + a.line([(x, -y) for x, y in env], WHITE, 2.6)
    s += a.yt(12, '12') + a.yt(4, '4') + a.yt(0, '0') + a.yt(-12, '−12')
    s += a.line([(0, 4), (2, 4)], GREY, 1, '4 4') + a.xt(2, '0.4 ms', anchor='end', dy=14)
    b = Ax(276, 462, 30, 116, (993, 1007), (0, 9))
    s += title(369, 'its spectrum, V', ACC2) + b.axes()
    s += b.stem(1000, 8, ACC, 4) + b.stem(995, 2, ACC2, 4) + b.stem(1005, 2, ACC2, 4)
    s += b.tx(1000, 8, '8', WHITE, dy=-9) + b.tx(995, 2, '2', WHITE, dy=-9) + b.tx(1005, 2, '2', WHITE, dy=-9)
    s += b.xt(995, '995') + b.xt(1000, '1000') + b.xt(1005, '1005') + b.xt(1007, 'kHz', anchor='end', dy=-4)
    setup()
    o = [trace([(1.6, 2.4), (3.0, 2.4), (3.0, 3.2)]), trace([(1.6, 5.6), (2.6, 5.6), (2.6, 4.4)]), trace([(4.6, 4.0), (6.4, 4.0)]), pad(6.4, 4.0)]
    o.append(crystal(.6, 2.0, '1 MHz'))
    o.append(module(.6, 5.0, 1.2, 1.1, .6, '5 kHz', size=14))
    o.append(chip(2.6, 3.2, 2.0, 1.4, 'AM', size=17))
    o.append(resistor(6.4, 3.8, 1.2, '50 Ω'))
    o.append(wave_h(4.6, 4.4, 3.0, 1.5, .9, lambda t: (1 + .5 * math.cos(2 * math.pi * 2 * t)) * math.sin(2 * math.pi * 12 * t) / 1.5, n=420, w=2.4))
    return spec('ec-comm-u2-L1', 'AM &amp;<br>DSB-SC<br>Modulation', 'AM &amp; DSB-SC Modulation',
                'How big is each AM sideband?',
                f'Each sideband gets {G("HALF")}<br>of mA<sub>c</sub>: just {C("2 V")}',
                '12 V peaks, 4 V dips', card(s), board(o),
                chips(('left', 256, 'g', 'm = 8/16 = 0.5'), ('left', 534, 'c', 'A<sub>c</sub> = 8 V'),
                      ('right', 262, 'c', 'P<sub>t</sub> = 0.72 W'), ('right', 534, 'g', 'η = 11.1 %')),
                f'm = (12 − 4)/(12 + 4) = 0.5, A<sub>c</sub> = (12 + 4)/2 = 8 V<br>each sideband mA<sub>c</sub>/2 = {gl("2 V")}, B = 2f<sub>m</sub> = {cl("10 kHz")}')


def u2L2():
    """2.3 Worked example 1: speech 0.3 to 3.4 kHz on 100 kHz"""
    fc, f1, W, fv = 100, .3, 3.4, .5
    dsb = (fc - W, fc + W); usb = (fc + f1, fc + W); vsb = (fc - fv, fc + W)
    Bd, Bs, Bv = dsb[1] - dsb[0], W, W + fv
    Pam, Pdsb, Pssb = 10 * 1.5, 10 * .5, 10 * .25
    near(Bd, 6.8, 1e-9); near(Bv, 3.9, 1e-9); near(vsb[0], 99.5, 1e-9); near(Pssb, 2.5, 0); near((Pam - Pssb) / Pam * 100, 83.3, .05)
    a = Ax(70, 460, 26, 122, (96, 104.2), (0, 3.3))
    s = a.axes() + a.line([(100, 0), (100, 3.15)], GREY, 1.4, '4 4') + a.tx(100, 3.15, 'f<tspan baseline-shift="sub" font-size="70%">c</tspan> 100', GREY, dy=-4)
    rows = [('DSB-SC', [(96.6, 99.7), (100.3, 103.4)], ACC, f'{Bd:g} kHz'), ('SSB (USB)', [usb], ACC, f'{Bs:g} kHz'), ('VSB', [(99.5, 99.7), (100.3, 103.4)], ACC2, f'{Bv:g} kHz')]
    for i, (n, bands, col, bw) in enumerate(rows):
        y = 2.55 - i * .95
        s += f'<text x="64" y="{a.Y(y) + 4:.1f}" text-anchor="end" class="ax">{n}</text>'
        for lo, hi in bands:
            if n == 'VSB' and lo == 99.5:
                s += f'<polygon points="{a.X(99.5):.1f},{a.Y(y - .28):.1f} {a.X(99.7):.1f},{a.Y(y + .28):.1f} {a.X(99.7):.1f},{a.Y(y - .28):.1f}" fill="{col}" opacity=".85"/>'
            else:
                s += f'<rect x="{a.X(lo):.1f}" y="{a.Y(y + .28):.1f}" width="{a.X(hi) - a.X(lo):.1f}" height="{a.Y(y - .28) - a.Y(y + .28):.1f}" rx="3" fill="{col}" opacity=".8"/>'
        s += f'<text x="{a.X(103.5):.1f}" y="{a.Y(y) + 5:.1f}" class="ax" fill="{WHITE}">{bw}</text>'
    for f in (96.6, 99.5):
        s += a.xt(f, f'{f:g}')
    s += a.xt(103.4, '103.4 kHz')
    setup()
    o = [trace([(1.6, 5.4), (2.6, 5.4), (2.6, 4.6)]), trace([(2.0, 1.6), (3.2, 1.6), (3.2, 3.2)]), trace([(4.5, 3.9), (5.0, 3.9)]), trace([(7.0, 3.9), (7.5, 3.9)]), pad(7.5, 3.9)]
    o.append(module(.4, 4.9, 1.3, 1.1, .6, '0.3–3.4 k', size=12))
    o.append(crystal(1.0, 1.3, '100 kHz'))
    o.append(chip(2.4, 3.2, 2.1, 1.4, 'DSB-SC', size=14))
    o.append(module(5.0, 3.2, 2.0, 1.4, .8, '', top='#2B2464'))
    # the VSB filter's response drawn on the filter's top face: a ramp through 0.5 at fc then flat
    resp = [(5.25, 4.35), (5.75, 4.35), (6.1, 3.6), (6.75, 3.6)]
    o.append(trace(resp, .82, ACC2, 3.2, 1))
    o.append(lab(6.0, 4.4, .8, 'VSB filter', '#F1F4F7', 12, 22))
    o.append(float_wave(4.9, 7.4, 2.4, 1.9, .55, lambda t: math.sin(2 * math.pi * 6 * t) * (.6 + .4 * math.sin(2 * math.pi * 1.3 * t)), n=300, w=2.4))
    return spec('ec-comm-u2-L2', 'SSB, VSB &amp;<br>AM Modulators', 'SSB, VSB &amp; AM Modulators',
                'How wide is a VSB signal?',
                f'VSB: one {G("SIDEBAND")}<br>plus a {C("VESTIGE")}',
                'speech on 100 kHz', card(s), board(o),
                chips(('left', 256, 'g', 'vestige 0.5 kHz'), ('left', 534, 'c', 'USB 3.4 kHz'),
                      ('right', 262, 'c', 'DSB-SC 6.8 kHz'), ('right', 534, 'g', 'SSB 2.5 kW of 15')),
                f'VSB runs 99.5 to 103.4 kHz: B = W + f<sub>v</sub><br>= 3.4 + 0.5 = {gl("3.9 kHz")}, against DSB-SC {cl("6.8 kHz")}')


def u2L3():
    """2.5 Worked example 1: envelope detector, m = 0.6, 5 kHz"""
    fc, fm, m, R = 1e6, 5e3, .6, 1e4
    RCmax = math.sqrt(1 - m * m) / (2 * math.pi * fm * m)
    RC = 20e-6; Cc = RC / R
    ripple = 1 - math.exp(-1 / (fc * RC))
    Rac = 10 * 40 / 50
    near(RCmax * 1e6, 42.4, .05); near(Cc * 1e9, 2, 1e-9); near(ripple * 100, 4.9, .05); near(Rac / 10, .8, 1e-9)
    # detector output: peak-hold with RC decay, one step per carrier period, over one tone period
    Tm = 1 / fm; n = int(Tm * fc)
    env = lambda t: 1 + m * math.cos(2 * math.pi * fm * t)
    v, out = env(0), []
    for k in range(n + 1):
        t = k / fc
        v = max(env(t), v * math.exp(-1 / (fc * RC)))
        out.append((t * 1e6, v))
    a = Ax(40, 222, 30, 114, (0, Tm * 1e6), (0, 1.7))
    s = title(131, 'output with RC = 20 µs', ACC2) + a.axes()
    s += a.area([(t * 1e6, env(t)) for t in [k / fc for k in range(0, n + 1, 2)]], ACC, .14)
    s += a.line([(t * 1e6, env(t)) for t in [k / fc for k in range(0, n + 1, 2)]], ACC, 5, op=.55) + a.line(out, ACC2, 2.4)
    s += a.yt(1.6, '1.6') + a.yt(.4, '0.4') + a.xt(0, '0') + a.xt(200, '200 µs', anchor='end')
    s += title(369, 'RC, µs', WHITE)
    for i, (nm, val, col) in enumerate((('carrier', 1, GREY), ('chosen', 20, ACC2), ('limit', RCmax * 1e6, ACC))):
        y = 30 + i * 30
        s += f'<text x="314" y="{y + 15}" text-anchor="end" class="ax">{nm}</text>' + hbar(320, y + 2, val * 2.6, 20, col)
        s += f'<text x="{326 + val * 2.6:.1f}" y="{y + 17}" class="ax" fill="{WHITE}">{val:.3g}</text>'
    s += f'<line x1="{320 + RCmax * 1e6 * 2.6:.1f}" y1="28" x2="{320 + RCmax * 1e6 * 2.6:.1f}" y2="124" stroke="{ACC}" stroke-width="1.4" stroke-dasharray="4 4"/>'
    s += f'<text x="{320 + RCmax * 1e6 * 2.6 + 4:.1f}" y="124" text-anchor="end" class="ax" fill="{ACC}">larger RC clips</text>'
    setup()
    o = [trace([(.8, 3.6), (1.9, 3.6)]), trace([(2.9, 3.6), (4.0, 3.6), (4.0, 2.2)]), trace([(4.0, 3.6), (4.0, 5.0)]),
         trace([(4.0, 3.6), (5.4, 3.6)]), trace([(6.3, 3.6), (6.6, 3.6)]), pad(.8, 3.6), pad(4.0, 3.6)]
    o.append(box(1.9, 3.4, 1.0, .42, .42, '#202228', '#0E0F12', '#16181C', z0=.05) + box(2.6, 3.39, .12, .44, .44, '#C9D0D6', '#9AA4AE', '#B5BEC6', z0=.05))
    o.append(lab(2.4, 3.6, .5, 'diode', '#F1F4F7', 12, -10))
    o.append(resistor(3.8, 4.8, 1.3, '10 kΩ', along='y'))
    o.append(can(4.0, 2.0, '2 nF', h=56, rx=16, ry=9))
    o.append(can(5.75, 3.6, 'C<tspan baseline-shift="sub" font-size="70%">c</tspan>', h=40, rx=13, ry=7))
    o.append(module(6.6, 3.0, 1.2, 1.2, .9, '40 kΩ', size=13))
    o.append(lab(7.2, 3.6, .9, 'audio', '#C9B3FF', 11, 18))
    o.append(wave_h(.4, 3.0, 2.0, 2.0, .7, lambda t: (1 + .6 * math.cos(2 * math.pi * 1.5 * t)) * math.sin(2 * math.pi * 9 * t) / 1.6, n=360, w=2.4))
    o.append(wave_h(4.6, 5.6, 2.6, 1.8, .7, lambda t: (1 + .6 * math.cos(2 * math.pi * 1.5 * t)) / 1.6 - .3, n=120, col=ACC2))
    return spec('ec-comm-u2-L3', 'AM Detectors &amp;<br>Transmitters', 'AM Detectors &amp; Transmitters',
                'What does too large an RC do?',
                f'RC too large: the output<br>{G("LAGS")} the envelope and {C("CLIPS")}',
                'm = 0.6, f<sub>m</sub> = 5 kHz', card(s), board(o),
                chips(('left', 256, 'g', 'RC ≤ 42.4 µs'), ('left', 534, 'c', 'ripple 4.9 %'),
                      ('right', 262, 'c', 'C = 2 nF'), ('right', 534, 'g', 'R<sub>ac</sub>/R<sub>dc</sub> = 0.8')),
                f'RC ≤ √(1 − 0.6²) ÷ (2π × 5000 × 0.6) = {gl("42.4 µs")}<br>C = 20 µs ÷ 10 kΩ = {cl("2 nF")}, ripple 4.9 %')


def u2L4():
    """2.7 Worked example 1: superhet tuned to 1000 kHz, IF 455 kHz, RF Q = 100"""
    fs, IF, Qr = 1000, 455, 100
    flo = fs + IF; fsi = fs + 2 * IF
    rho = fsi / fs - fs / fsi; alpha = math.sqrt(1 + (Qr * rho) ** 2)
    def rej(f, i):
        si = f + 2 * i; r = si / f - f / si
        return 20 * math.log10(math.sqrt(1 + (Qr * r) ** 2))
    d1, d2, d3 = 20 * math.log10(alpha), rej(25e3, 455), rej(25e3, 1500)
    near(flo, 1455, 0); near(fsi, 1910, 0); near(alpha, 138.6, .05); near(d1, 42.8, .05); near(d2, 17.2, .05); near(d3, 27.1, .05)
    a = Ax(44, 226, 30, 112, (700, 2100), (-50, 3))
    resp = [(f, 20 * math.log10(1 / math.sqrt(1 + (Qr * (f / fs - fs / f)) ** 2))) for f in range(700, 2101, 5)]
    s = title(135, 'RF stage, Q = 100, dB', ACC2) + a.axes() + a.line(resp, ACC2, 2.6)
    s += a.stem(1000, 0, ACC, 3, 5, -50) + a.stem(1910, -d1, ACC, 3, 5, -50)
    s += a.line([(1455, -50), (1455, 0)], WHITE, 1.6, '4 4')
    s += a.tx(1910, -d1, f'−{d1:.1f} dB', ACC, anchor='end', dy=-10) + a.tx(1455, -12, 'LO', WHITE, anchor='start').replace('text-anchor="start"', 'text-anchor="start" dx="5"')
    s += a.yt(0, '0') + a.yt(-40, '−40') + a.xt(1000, '1000') + a.xt(1455, '1455') + a.xt(1910, '1910 kHz')
    s += title(366, 'image rejection, dB', WHITE)
    rows = (('1000 kHz', d1, ACC), ('25 MHz', d2, GREY), ('25 MHz, 1.5 MHz IF', d3, ACC2))
    for i, (nm, v, col) in enumerate(rows):
        y = 28 + i * 38
        s += f'<text x="270" y="{y + 12}" class="ax">{nm}</text>' + hbar(270, y + 17, v * 3.8, 14, col)
        s += f'<text x="{276 + v * 3.8:.1f}" y="{y + 29}" class="ax" fill="{WHITE}">{v:.1f}</text>'
    setup()
    o = [trace([(1.0, 4.4), (1.8, 4.4)]), trace([(3.2, 4.4), (3.9, 4.4)]), trace([(5.3, 4.4), (5.9, 4.4)]), trace([(4.6, 2.0), (4.6, 3.6)]), pad(7.6, 4.4), trace([(7.2, 4.4), (7.6, 4.4)])]
    o.append(antenna(.8, 4.4, 3.0))
    o.append(module(1.8, 3.8, 1.4, 1.2, .8, 'RF', top='#2F6B5E', left='#173A33', right='#1F4D43', size=16))
    o.append(lab(2.5, 4.4, .8, 'Q = 100', '#BFF5E8', 11, 20))
    o.append(chip(3.9, 3.6, 1.4, 1.4, 'mixer', size=13))
    o.append(crystal(4.0, 1.2, '1455 kHz', w=1.3))
    o.append(module(5.9, 3.8, 1.3, 1.2, .7, 'IF 455', size=13))
    return spec('ec-comm-u2-L4', 'Superheterodyne<br>Receiver<br>&amp; FDM', 'Superheterodyne Receiver &amp; FDM',
                'Which stage rejects the image?',
                f'Only the {G("RF STAGE")}<br>can reject the {C("IMAGE")}',
                '1000 kHz, IF 455 kHz', card(s), board(o),
                chips(('left', 256, 'g', 'LO at 1455 kHz'), ('left', 534, 'c', 'image at 1910 kHz'),
                      ('right', 534, 'g', 'α = 138.6'), ('right', 262, 'c', '25 MHz: only 17.2 dB')),
                f'image = 1000 + 2 × 455 = {gl("1910 kHz")}, after the mixer<br>it lands on 455 kHz; RF Q = 100 gives {cl("42.8 dB")}')


# ================================================================ unit 3
def besselj(n, x):
    s = 0.0
    for k in range(40):
        s += (-1) ** k * (x / 2) ** (2 * k + n) / (math.factorial(k) * math.factorial(k + n))
    return s


def u3L1():
    """3.2 Worked example 1: broadcast FM, 75 kHz deviation, 15 kHz tone"""
    df, fm = 75, 15
    beta = df / fm; pairs = beta + 1
    BT = 2 * (beta + 1) * fm; sw = 2 * df
    near(beta, 5, 0); near(BT, 180, 0); near(2 * (df + fm), 180, 0); near(sw, 150, 0)
    a = Ax(36, 460, 26, 108, (-135, 135), (0, .45))
    s = a.axes()
    s += f'<rect x="{a.X(-90):.1f}" y="26" width="{a.X(90) - a.X(-90):.1f}" height="82" fill="{ACC}" opacity=".10"/>'
    for n in range(-8, 9):
        J = abs(besselj(abs(n), beta))
        col = ACC if abs(n) <= pairs else GREY
        s += a.stem(n * fm, J, col, 3, 4)
    s += a.line([(-90, 0), (-90, .45)], ACC, 1.6, '5 4') + a.line([(90, 0), (90, .45)], ACC, 1.6, '5 4')
    s += a.line([(-75, .41), (75, .41)], ACC2, 2.4) + a.tx(0, .41, f'swept 2Δf = {sw:g} kHz', ACC2, dy=-6, cls='ax')
    s += a.tx(-90, .3, 'Carson 180', ACC, anchor='end', dy=0).replace('text-anchor="end"', 'text-anchor="end" dx="-6"')
    s += a.xt(-90, '−90') + a.xt(90, '+90') + a.xt(0, 'f<tspan baseline-shift="sub" font-size="70%">c</tspan>')
    s += a.xt(135, 'kHz', anchor='end') + f'<text x="460" y="138" text-anchor="end" class="ax">lines |J<tspan baseline-shift="sub" font-size="70%">n</tspan>(5)| every 15 kHz</text>'
    setup()
    o = [trace([(1.6, 4.4), (2.6, 4.4)]), trace([(4.4, 4.4), (5.8, 4.4)]), pad(5.8, 4.4)]
    o.append(module(.5, 3.8, 1.2, 1.2, .6, '15 kHz', size=13))
    o.append(chip(2.6, 3.7, 1.8, 1.4, 'FM', size=18))
    o.append(lab(3.5, 4.4, .42, 'Δf = 75 kHz', '#C9B3FF', 11, 20))
    o.append(antenna(6.2, 4.4, 3.2))
    o.append(float_wave(1.0, 5.6, 1.8, 1.9, .55, lambda t: math.sin(2 * math.pi * (9 * t + 1.0 * math.sin(2 * math.pi * 1 * t))), n=420, w=2.4))
    return spec('ec-comm-u3-L1', 'Angle<br>Modulation &amp;<br>FM Bandwidth', 'Angle Modulation &amp; FM Bandwidth',
                'How wide is broadcast FM?',
                f'Carson gives {G("180 kHz")},<br>not the {C("150 kHz")} swing',
                'Δf = 75 kHz, f<sub>m</sub> = 15 kHz', card(s), board(o),
                chips(('left', 256, 'g', 'β = 75/15 = 5'), ('left', 534, 'c', '2Δf = 150 kHz'),
                      ('right', 262, 'g', 'β + 1 = 6 pairs'), ('right', 534, 'c', 'B<sub>T</sub> = 180 kHz')),
                f'B<sub>T</sub> = 2(β + 1)f<sub>m</sub> = 2 × 6 × 15 = {gl("180 kHz")}<br>= 2(75 + 15); the swing 2Δf is only {cl("150 kHz")}')


def u3L2():
    """3.4 Worked example 1: slope detector, tank 465 kHz, Q = 50"""
    fr, Qt, fcar, dev = 465, 50, 455, 5
    V = lambda f: 1 / math.sqrt(1 + (2 * Qt * (f - fr) / fr) ** 2)
    v0, vp, vm = V(fcar), V(fcar + dev), V(fcar - dev)
    near(v0, .422, .0005); near(vp, .681, .0005); near(vm, .296, .0005); near(vp - v0, .259, .001); near(v0 - vm, .126, .001)
    a = Ax(60, 460, 28, 112, (435, 495), (0, 1.08))
    curve = [(f / 4, V(f / 4)) for f in range(435 * 4, 495 * 4 + 1)]
    s = a.axes() + a.area(curve, ACC, .12) + a.line(curve, ACC, 3)
    s += f'<rect x="{a.X(450):.1f}" y="28" width="{a.X(460) - a.X(450):.1f}" height="84" fill="{ACC2}" opacity=".10"/>'
    for f, v, c in ((fcar - dev, vm, ACC2), (fcar, v0, WHITE), (fcar + dev, vp, ACC2)):
        pos = {fcar - dev: ('end', 4, -8), fcar: ('end', -10, -4), fcar + dev: ('start', 5, 8)}[f]
        s += a.line([(f, 0), (f, v)], c, 1.4, '4 3') + a.dot(f, v, c, 6) + a.tx(f, v, f'{v:.3f} V', c, anchor=pos[0], dy=pos[1]).replace(f'text-anchor="{pos[0]}"', f'text-anchor="{pos[0]}" dx="{pos[2]}"')
    s += a.line([(fr, 0), (fr, 1)], GREY, 1.4, '4 4') + a.tx(fr, 1, 'f<tspan baseline-shift="sub" font-size="70%">r</tspan> = 465', GREY, dy=-4)
    s += a.yt(1, '1 V') + a.yt(0, '0') + a.xt(450, '450') + a.xt(455, '455') + a.xt(460, '460') + a.xt(495, 'kHz', anchor='end')
    setup()
    o = [trace([(1.5, 4.4), (2.4, 4.4)]), trace([(4.4, 4.4), (5.0, 4.4)]), trace([(6.0, 4.4), (6.6, 4.4), (6.6, 3.2)]), pad(6.6, 3.2)]
    o.append(module(.4, 3.8, 1.2, 1.2, .6, 'IF in', size=13))
    # the tank: a coil (rings on a former) beside a capacitor can
    o.append(box(2.4, 3.6, 2.0, 1.6, .25, '#23544A', '#10302A', '#163B34'))
    for k in range(7):
        o.append(ring(2.75 + k * .2, 4.0 + k * .02, .7, 12, '#E0A050', 3))
    o.append(can(4.0, 4.9, '', h=48, rx=14, ry=8))
    o.append(lab(3.4, 4.4, .25, '465 kHz · Q 50', '#BFF5E8', 11, 34))
    o.append(box(5.0, 4.2, .9, .42, .42, '#202228', '#0E0F12', '#16181C', z0=.05) + box(5.6, 4.19, .12, .44, .44, '#C9D0D6', '#9AA4AE', '#B5BEC6', z0=.05))
    o.append(can(6.8, 2.6, 'RC', h=40, rx=13, ry=7))
    o.append(float_wave(.6, 2.2, 2.3, 1.9, .5, lambda t: math.sin(2 * math.pi * (5 * t + .5 * math.sin(2 * math.pi * 1 * t))), n=260, w=2.4))
    o.append(float_wave(5.2, 7.6, 2.3, 1.9, .5, lambda t: .3 + .45 * math.sin(2 * math.pi * 1.5 * t) * (1 if math.sin(2 * math.pi * 1.5 * t) > 0 else .49), n=200, col=ACC2))
    return spec('ec-comm-u3-L2', 'Making &amp;<br>Detecting FM', 'Making &amp; Detecting FM',
                'Does a slope detector give 0 at fc?',
                f'At f<sub>c</sub> it already gives {G("0.422 V")}:<br>it sits on the {C("FLANK")}',
                'tank 465 kHz, Q = 50', card(s), board(o),
                chips(('left', 256, 'c', 'f<sub>c</sub> = 455 kHz, ±5 kHz'), ('left', 534, 'g', 'Q = 50: 9.3 kHz wide'),
                      ('right', 262, 'g', '+0.259 V at 460'), ('right', 534, 'c', '−0.126 V at 450')),
                f'x = 2Q(f − f<sub>r</sub>)/f<sub>r</sub> = −2.151 → V = {gl("0.422 V")} at f<sub>c</sub><br>swings +0.259 and −0.126 V: {cl("distorted")}')


def u3L3():
    """3.6 Worked examples 1 and 2: FM threshold, beta = 5 against beta = 2"""
    N0, W = 4e-21, 15e3
    def rx(beta):
        BT = 2 * (beta + 1) * W
        N = N0 * BT; Ndbm = 10 * math.log10(N / 1e-3)
        Cth = Ndbm + 10
        imp = 10 * math.log10(3 * beta ** 2 * (beta + 1))
        return BT, Ndbm, Cth, imp
    B5, N5, C5, I5 = rx(5); B2, N2, C2, I2 = rx(2)
    out5, out2 = 10 + I5, 10 + I2
    at = lambda Cdbm, Nd, I: (Cdbm - Nd) + I
    o2_111 = at(C5, N2, I2)
    near(N5, -121.4, .05); near(C5, -111.4, .05); near(out5, 36.5, .05); near(C2, -114.4, .05); near(out2, 25.6, .05); near(o2_111, 28.6, .05)
    a = Ax(50, 460, 26, 112, (-118, -104), (14, 44))
    s = a.axes()
    for Cth, Nd, I, col, nm in ((C5, N5, I5, ACC, 'β = 5'), (C2, N2, I2, ACC2, 'β = 2')):
        up = [(c, at(c, Nd, I)) for c in (Cth, -104)]
        s += a.line(up, col, 3.2)
        y0 = at(Cth, Nd, I)
        s += a.line([(Cth, y0), (Cth - .9, y0 - 6), (Cth - 1.6, y0 - 15)], col, 2.4, '3 5')
        s += a.dot(Cth, y0, col, 6)
        s += a.tx(-104, at(-104, Nd, I), nm, col, anchor='end', dy=-9, cls='pt')
    s += a.tx(C5, out5, f'{out5:.1f} dB', ACC, anchor='end', dy=-6).replace('text-anchor="end"', 'text-anchor="end" dx="-8"')
    s += a.tx(C2, out2, f'{out2:.1f}', ACC2, anchor='start', dy=20).replace('text-anchor="start"', 'text-anchor="start" dx="6"')
    s += a.tx(-116.2, 17, 'clicks', '#FF9C9C')
    s += a.yt(40, '40') + a.yt(20, '20') + a.xt(C5, f'{C5:.1f}') + a.xt(C2, f'{C2:.1f}') + a.xt(-104, 'dBm in', anchor='end')
    s += f'<text x="44" y="22" class="ax">SNR out, dB</text>'
    setup()
    o = [trace([(1.0, 4.4), (1.8, 4.4), (1.8, 2.4), (2.6, 2.4)]), trace([(1.8, 4.4), (1.8, 5.8), (2.6, 5.8)]),
         trace([(4.4, 2.4), (5.0, 2.4)]), trace([(4.4, 5.8), (5.0, 5.8)])]
    o.append(antenna(.8, 4.4, 3.0))
    o.append(module(2.6, 1.8, 1.8, 1.2, .7, '180 kHz', top='#4A3D96', size=14))
    o.append(module(2.6, 5.2, 1.8, 1.2, .7, '90 kHz', top='#1F5A50', left='#0F302A', right='#164038', size=14))
    o.append(chip(5.0, 1.8, 1.4, 1.2, 'β = 5', size=13))
    o.append(chip(5.0, 5.2, 1.4, 1.2, 'β = 2', size=13))
    o.append(float_wave(5.2, 7.6, 2.4, 1.6, .5, lambda t: math.sin(2 * math.pi * 2 * t), n=120, col=ACC))
    o.append(float_wave(6.0, 7.8, 5.8, 1.4, .45, lambda t: math.sin(2 * math.pi * 2 * t), n=120, col=ACC2))
    return spec('ec-comm-u3-L3', 'Noise,<br>Threshold<br>&amp; Capture', 'Noise, Threshold &amp; Capture',
                'What happens below the FM threshold?',
                f'Below a {G("10 dB")} CNR the<br>output breaks into {C("CLICKS")}',
                'β = 5 against β = 2', card(s), board(o),
                chips(('left', 256, 'g', 'knee at 10 dB CNR'), ('left', 534, 'c', 'β = 2: −114.4 dBm'),
                      ('right', 534, 'g', '36.5 against 28.6 dB'), ('right', 262, 'c', 'N = −121.4 dBm')),
                f'N = N<sub>0</sub>B<sub>T</sub> = −121.4 dBm; ρ = 10 dB at {gl("−111.4 dBm")}<br>β = 2 (90 kHz) works down to {cl("−114.4 dBm")}')


def u3L4():
    """3.7 Worked example 1: 75 us pre-emphasis, 15 kHz audio"""
    tau, W = 75e-6, 15e3
    f1 = 1 / (2 * math.pi * tau)
    gdb = lambda f: 20 * math.log10(math.sqrt(1 + (f / f1) ** 2))
    r = W / f1
    I = r ** 3 / (3 * (r - math.atan(r)))
    near(f1, 2122, .5); near(gdb(f1), 3.01, .005); near(gdb(W), 17.07, .005); near(10 * math.log10(I), 13.2, .05); near(I, 20.88, .01)
    a = Ax(44, 222, 30, 112, (2, math.log10(15e3)), (-1, 19))
    fs = [10 ** (2 + k / 60 * (math.log10(15e3) - 2)) for k in range(61)]
    pre = [(math.log10(f), gdb(f)) for f in fs]
    s = title(133, 'pre-emphasis gain, dB', ACC) + a.axes(0) + a.area(pre, ACC, .14, 0) + a.line(pre, ACC, 3.2)
    s += a.dot(math.log10(f1), gdb(f1), WHITE) + a.dot(math.log10(W), gdb(W), ACC, 6)
    s += a.tx(math.log10(W), gdb(W), f'+{gdb(W):.2f}', ACC, anchor='end', dy=4).replace('text-anchor="end"', 'text-anchor="end" dx="-9"')
    s += a.tx(math.log10(f1), gdb(f1), f'+{gdb(f1):.2f}', WHITE, anchor='end', dy=-6)
    s += a.xt(2, '100') + a.xt(math.log10(f1), f'{f1:.0f}') + a.xt(math.log10(W), '15k Hz', anchor='end')
    b = Ax(282, 462, 30, 112, (2, math.log10(15e3)), (-19, 1))
    de = [(math.log10(f), -gdb(f)) for f in fs]
    s += title(372, 'de-emphasis gain, dB', ACC2) + b.axes(0) + b.area(de, ACC2, .14, 0) + b.line(de, ACC2, 3.2)
    s += b.dot(math.log10(W), -gdb(W), ACC2, 6) + b.tx(math.log10(W), -gdb(W), f'−{gdb(W):.2f}', ACC2, anchor='end', dy=4).replace('text-anchor="end"', 'text-anchor="end" dx="-9"')
    setup()
    o = [trace([(1.0, 6.2), (1.0, 4.9)]), trace([(1.0, 3.7), (1.0, 2.6), (2.3, 2.6)]), trace([(3.9, 2.6), (4.7, 2.6), (4.7, 3.6)]),
         trace([(4.7, 4.8), (4.7, 5.4), (5.4, 5.4)]), pad(1.0, 6.2), pad(4.7, 3.6)]
    o.append(module(.3, 3.7, 1.4, 1.2, .8, 'pre 75 µs', top='#6D57C9', left='#3A2D7A', right='#4C3D9C', size=12))
    o.append(chip(2.3, 2.0, 1.6, 1.2, 'FM mod', size=13))
    o.append(chip(4.1, 3.6, 1.2, 1.2, 'disc.', size=12))
    o.append(module(5.4, 4.8, 1.4, 1.2, .8, 'de 75 µs', top='#1F8C78', left='#0F4A40', right='#166A5A', size=12))
    o.append(flow(.6, 7.6, .6, 6.4, ACC, .2))
    o.append(lab(.95, 7.4, 0, 'audio in', '#C9B3FF', 12, 18))
    o.append(float_wave(2.0, 4.0, 1.1, 1.5, .4, lambda t: math.sin(2 * math.pi * (5 * t + .5 * math.sin(2 * math.pi * 1 * t))), n=200, w=2.4))
    return spec('ec-comm-u3-L4', 'Pre-emphasis<br>&amp; FM Stereo', 'Pre-emphasis &amp; FM Stereo',
                'Where does pre-emphasis go?',
                f'Boost the treble {G("BEFORE")}<br>the modulator, cut it {C("AFTER")}',
                '75 µs, 15 kHz audio', card(s), board(o),
                chips(('left', 256, 'g', 'f<sub>1</sub> = 2122 Hz'), ('left', 534, 'c', '+3.01 dB at f<sub>1</sub>'),
                      ('right', 262, 'g', '+17.07 dB at 15 kHz'), ('right', 534, 'c', 'SNR +13.2 dB')),
                f'f<sub>1</sub> = 1/(2π × 75 µs) = {gl("2122 Hz")}, 15 kHz up 17.07 dB<br>noise improvement 20.88 = {cl("13.2 dB")}')


# ================================================================ unit 4
def u4L1():
    """4.1 Worked example 1: 3 cos 2pi1000t + 2 cos 2pi4000t sampled at 7000/s"""
    fs, f1, f2 = 7000, 1000, 4000
    nyq = 2 * f2; fold = fs / 2; alias = fs - f2
    s1 = 2 * math.cos(2 * math.pi * f2 / fs); s2 = 2 * math.cos(2 * math.pi * alias / fs)
    near(nyq, 8000, 0); near(alias, 3000, 0); near(s1, -1.802, .0005); near(s1, s2, 1e-9)
    a = Ax(40, 222, 30, 114, (0, 1e-3), (-2.4, 2.4))
    ts = [k * 1e-3 / 300 for k in range(301)]
    s = title(131, '4 kHz and 3 kHz, same dots', WHITE) + a.axes(0)
    s += a.line([(t, 2 * math.cos(2 * math.pi * f2 * t)) for t in ts], ACC, 2.4)
    s += a.line([(t, 2 * math.cos(2 * math.pi * alias * t)) for t in ts], ACC2, 2.4, '6 4')
    for k in range(8):
        t = k / fs
        if t <= 1e-3:
            s += a.dot(t, 2 * math.cos(2 * math.pi * f2 * t), WHITE, 4.5)
    s += a.yt(2, '2') + a.yt(-2, '−2') + a.xt(0, '0') + a.xt(1e-3, '1 ms', anchor='end')
    b = Ax(276, 462, 30, 114, (0, 12), (0, 3.6))
    s += title(369, 'lines after sampling, kHz', WHITE) + b.axes()
    s += f'<rect x="{b.X(0):.1f}" y="30" width="{b.X(3.5) - b.X(0):.1f}" height="84" fill="{ACC2}" opacity=".10"/>'
    s += b.line([(3.5, 0), (3.5, 3.5)], ACC2, 1.6, '5 4') + b.tx(3.5, 3.5, 'filter', ACC2, dy=-3, anchor='end').replace('text-anchor="end"', 'text-anchor="end" dx="-4"')
    for f, amp, col in ((1, 3, WHITE), (6, 3, GREY), (8, 3, GREY), (4, 2, ACC), (3, 2, ACC2), (11, 2, GREY), (10, 2, GREY)):
        s += b.stem(f, amp * .9, col, 3, 4)
    s += b.xt(1, '1') + b.xt(3, '3', col=ACC2) + b.xt(4, '4', col=ACC) + b.xt(6, '6') + b.xt(8, '8') + b.xt(10.5, '10, 11')
    setup()
    o = [trace([(.8, 4.0), (2.2, 4.0)]), trace([(3.4, 4.0), (4.6, 4.0)]), trace([(2.8, 1.6), (2.8, 3.4)]), trace([(6.2, 4.0), (7.2, 4.0)]), pad(7.2, 4.0)]
    # the sampling switch: two posts and a blade
    o.append(box(2.2, 3.7, .5, .6, .5, '#C9D0D6', '#7D8792', '#9AA4AE') + box(2.9, 3.7, .5, .6, .5, '#C9D0D6', '#7D8792', '#9AA4AE'))
    (xa, ya), (xb, yb) = P(2.45, 4.0, .55), P(3.15, 3.6, 1.0)
    o.append(f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb:.1f}" y2="{yb:.1f}" stroke="#F1F4F7" stroke-width="5" stroke-linecap="round"/>')
    o.append(crystal(2.2, .9, '7 kS/s', w=1.2))
    o.append(module(4.6, 3.4, 1.6, 1.2, .7, 'LPF 3.5k', top='#1F8C78', left='#0F4A40', right='#166A5A', size=13))
    pts_t = [k / 7 for k in range(8)]
    st = []
    for k, t in enumerate(pts_t):
        if t <= 1:
            x, y = P(3.4 + t * 2.6, 2.4, 1.6)
            hv = 2 * math.cos(2 * math.pi * 4 * t) * .4
            st.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{y - hv * 33:.1f}" stroke="#E8FFFA" stroke-width="3"/><circle cx="{x:.1f}" cy="{y - hv * 33:.1f}" r="4.5" fill="#E8FFFA"/>')
    o.append('<g filter="url(#gl)">' + ''.join(st) + '</g>')
    o.append(float_wave_d(3.4, 2.4, 6.0, 2.4, 1.6, .8, lambda t: math.cos(2 * math.pi * 3 * t), n=160, col=ACC2, w=2.4))
    return spec('ec-comm-u4-L1', 'Sampling &amp;<br>Pulse<br>Modulation', 'Sampling &amp; Pulse Modulation',
                'Where does an undersampled tone land?',
                f'7 − 4 = {G("3 kHz")}: the 4 kHz<br>tone comes out {C("FALSE")}',
                'sampled at 7 kS/s', card(s), board(o),
                chips(('left', 256, 'g', 'Nyquist rate 8000/s'), ('left', 534, 'c', 'folds at 3500 Hz'),
                      ('right', 262, 'c', '−1.802 V both'), ('right', 534, 'g', '4 kHz → 3 kHz')),
                f'7000 &lt; 8000 samples/s: 4 kHz folds to 7 − 4 = {gl("3 kHz")}<br>output 3 cos 2π1000t plus a false {cl("2 cos 2π3000t")}')


def u4L2():
    """4.3 Worked example 1: 8-bit uniform quantizer, +-1 V, full-scale sine"""
    n, V = 8, 1
    L = 2 ** n; dlt = 2 * V / L; Pq = dlt ** 2 / 12; Px = V ** 2 / 2
    sq = Px / Pq; sqdb = 10 * math.log10(sq); rule = 6.02 * n + 1.76
    near(L, 256, 0); near(dlt * 1e3, 7.8125, 1e-9); near(Pq * 1e6, 5.086, .0005); near(sq, 98304, .5); near(sqdb, 49.93, .005); near(rule, 49.92, .005)
    a = Ax(48, 222, 30, 112, (-4.5 * dlt * 1e3, 4.5 * dlt * 1e3), (-dlt * 1e3 * .75, dlt * 1e3 * .75))
    xs = [k / 40 * dlt * 1e3 for k in range(-180, 181)]
    err = [(x, x - dlt * 1e3 * (math.floor(x / (dlt * 1e3)) + .5)) for x in xs]
    s = title(135, 'error e = x − x<tspan baseline-shift="sub" font-size="70%">q</tspan>, mV', ACC2) + a.axes(0)
    s += a.line(err, ACC2, 2.4)
    s += a.line([(-4.5 * dlt * 1e3, dlt * 500), (4.5 * dlt * 1e3, dlt * 500)], GREY, 1, '4 4') + a.line([(-4.5 * dlt * 1e3, -dlt * 500), (4.5 * dlt * 1e3, -dlt * 500)], GREY, 1, '4 4')
    s += a.yt(dlt * 500, f'+{dlt * 500:.2f}') + a.yt(-dlt * 500, f'−{dlt * 500:.2f}') + a.xt(0, '0') + a.xt(4.5 * dlt * 1e3, 'input x', anchor='end')
    s += title(369, 'SQNR, dB', WHITE)
    rows = (('6 dB × 8 bits', 6.02 * n, GREY), ('6.02n + 1.76', rule, ACC), ('0.5 ÷ P<tspan baseline-shift="sub" font-size="70%">q</tspan>', sqdb, ACC2))
    for i, (nm, v, col) in enumerate(rows):
        y = 26 + i * 34
        s += f'<text x="276" y="{y + 12}" class="ax">{nm}</text>' + hbar(276, y + 17, (v - 40) * 14, 13, col)
        s += f'<text x="{282 + (v - 40) * 14:.1f}" y="{y + 28}" class="ax" fill="{WHITE}">{v:.2f}</text>'
    s += '<text x="276" y="140" class="ax" fill="#8C9AA8">bars start at 40 dB</text>'
    setup()
    o = [trace([(1.6, 4.0), (2.4, 4.0)]), trace([(3.4, 1.6), (3.4, 2.8)])]
    o.append(module(.4, 3.4, 1.2, 1.2, .6, '±1 V', size=14))
    o.append(module(2.8, .7, 1.2, .9, .5, 'V<tspan baseline-shift="sub" font-size="70%">ref</tspan>', top='#5B6470', left='#2E343C', right='#3E4650', size=13))
    o.append(chip(2.4, 2.8, 2.0, 2.4, '8-bit ADC', size=14))
    bits = '10110011'
    for k, bch in enumerate(bits):
        bb = 2.9 + k * .27
        o.append(trace([(4.4, bb), (6.4, bb)], .01, GOLD, 2, .7))
        col = ACC2 if bch == '1' else '#2E5E56'
        o.append(box(6.4, bb - .1, .3, .2, .3, col, '#0F4A40', '#166A5A'))
    o.append(lab(7.2, 3.8, 0, '8 bits', '#BFF5E8', 12, 0))
    o.append(float_wave(.4, 2.2, 4.6, 1.6, .8, lambda t: math.sin(2 * math.pi * t), n=100))
    return spec('ec-comm-u4-L2', 'Quantization,<br>Companding<br>&amp; PCM', 'Quantization, Companding &amp; PCM',
                'Is SQNR just 6 dB per bit?',
                f'6.02n {G("+ 1.76 dB")}, and that<br>only for a {C("FULL-SCALE")} sine',
                '8 bits, ±1 V, sine', card(s), board(o),
                chips(('left', 256, 'g', 'L = 2<sup>8</sup> = 256'), ('left', 534, 'c', 'Δ = 7.8125 mV'),
                      ('right', 262, 'c', 'P<sub>q</sub> = Δ²/12'), ('right', 534, 'g', 'SQNR 49.93 dB')),
                f'P<sub>q</sub> = Δ²/12, SQNR = 0.5/P<sub>q</sub> = 98 304<br>= {gl("49.93 dB")} ≈ 6.02 × 8 {cl("+ 1.76")}, not 48')


def u4L3():
    """4.6 Worked example 1: delta modulation of a 1 kHz, 2 V sine, step 0.1 V at 32 kHz"""
    f, A, dl, fs = 1000, 2, .1, 32000
    sin_slope = 2 * math.pi * f * A; st_slope = dl * fs
    fs_min = sin_slope / dl; d_min = sin_slope / fs
    near(sin_slope, 12566, .5); near(st_slope, 3200, 0); near(fs_min / 1e3, 125.7, .05); near(d_min, .393, .0005)
    a = Ax(40, 222, 30, 114, (0, 1e-3), (-2.3, 2.3))
    ts = [k * 1e-3 / 300 for k in range(301)]
    s = title(131, 'staircase, Δ = 0.1 V', ACC2) + a.axes(0) + a.line([(t, A * math.sin(2 * math.pi * f * t)) for t in ts], ACC, 3)
    xq, stair = 0.0, []
    for k in range(33):
        t = k / fs
        xq += dl if A * math.sin(2 * math.pi * f * t) >= xq else -dl
        stair += [(t, xq), (min((k + 1) / fs, 1e-3), xq)]
    s += a.line(stair, ACC2, 2.4)
    s += a.yt(2, '2') + a.yt(-2, '−2') + a.xt(0, '0') + a.xt(1e-3, '1 ms', anchor='end')
    s += title(369, 'largest slope, V/s', WHITE)
    for i, (nm, v, col) in enumerate((('input 2πfA', sin_slope, ACC), ('staircase Δf<tspan baseline-shift="sub" font-size="70%">s</tspan>', st_slope, ACC2))):
        y = 32 + i * 46
        s += f'<text x="276" y="{y + 12}" class="ax">{nm}</text>' + hbar(276, y + 18, v / 120, 18, col)
        s += f'<text x="{282 + v / 120:.1f}" y="{y + 32}" class="ax" fill="{WHITE}">{v:,.0f}</text>'.replace(',', ' ')
    s += f'<text x="276" y="140" class="ax" fill="#FF9C9C">input steeper: overload</text>'
    setup()
    o = [trace([(1.6, 4.0), (2.4, 4.0)]), trace([(4.0, 4.0), (5.6, 4.0)]), trace([(4.8, 4.0), (4.8, 6.0), (3.2, 6.0), (3.2, 4.8)]),
         trace([(3.2, 1.5), (3.2, 3.2)]), pad(5.6, 4.0)]
    o.append(module(.4, 3.4, 1.2, 1.2, .6, '1 kHz', size=14))
    o.append(chip(2.4, 3.2, 1.6, 1.6, 'comp', size=14))
    o.append(module(2.5, 5.6, 1.6, 1.1, .7, 'Σ Δ', top='#1F8C78', left='#0F4A40', right='#166A5A', size=14))
    o.append(crystal(2.6, .8, '32 kHz'))
    bits = '11111111110'
    for k, bch in enumerate(bits):
        o.append(box(5.7 + k * .2, 3.8, .14, .4, .55 if bch == '1' else .15, ACC2 if bch == '1' else '#2E5E56', '#0F4A40', '#166A5A'))
    o.append(float_wave(.4, 2.2, 3.2, 1.6, .8, lambda t: math.sin(2 * math.pi * t), n=100))
    o.append(float_wave(5.6, 7.8, 2.0, 1.6, .8, lambda t: (min(round(t * 32) * .1, 2) - 1) * .7, n=200, col=ACC2))
    return spec('ec-comm-u4-L3', 'Differential<br>PCM &amp; Delta<br>Modulation', 'Differential PCM &amp; Delta Modulation',
                'When does delta modulation overload?',
                f'When the input slope<br>beats {G("Δ·f<sub>s</sub>")}: {C("OVERLOAD")}',
                '1 kHz, 2 V, Δ = 0.1 V', card(s), board(o),
                chips(('left', 256, 'g', '2πfA = 12 566 V/s'), ('left', 534, 'c', 'Δf<sub>s</sub> = 3200 V/s'),
                      ('right', 262, 'g', 'f<sub>s</sub> ≥ 125.7 kHz'), ('right', 534, 'c', 'or Δ ≥ 0.393 V')),
                f'input 2π × 1000 × 2 = {gl("12 566 V/s")} &gt; 0.1 × 32 000<br>= {cl("3200 V/s")}: slope overload near every zero')


def u4L4():
    """4.8 Worked example 1: 1 0 1 1 0 at 1 kbit/s in four line codes"""
    Rb = 1000; Tb = 1 / Rb
    bits = [1, 0, 1, 1, 0]
    nrz = [(1 if b else -1, 1 if b else -1) for b in bits]
    man = [(-1, 1) if b else (1, -1) for b in bits]
    trans = sum(1 for i in range(len(man)) for a_, b_ in [man[i]] if a_ != b_) + sum(1 for i in range(1, len(man)) if man[i - 1][1] != man[i][0])
    near(Tb * 1e3, 1, 0); near(trans, 6, 0); near(sum(1 if b else -1 for b in bits) / 5, .2, 1e-9)
    def wave(ax, halves, col, off):
        xy = []
        for k, (h1, h2) in enumerate(halves):
            xy += [(k, off + h1 * .8), (k + .5, off + h1 * .8), (k + .5, off + h2 * .8), (k + 1, off + h2 * .8)]
        return ax.line(xy, col, 2.8)
    a = Ax(78, 222, 22, 122, (0, 5), (-5.2, 1.6))
    s = a.line([(0, .0), (5, 0)], GREY, 1, '3 4') + a.line([(0, -3.2), (5, -3.2)], GREY, 1, '3 4')
    s += wave(a, nrz, ACC, 0) + wave(a, man, ACC2, -3.2)
    for k, b in enumerate(bits):
        s += a.tx(k + .5, 1.6, str(b), WHITE, dy=4)
    s += f'<text x="72" y="{a.Y(0) + 5:.1f}" text-anchor="end" class="ax" fill="{ACC}">NRZ</text>'
    s += f'<text x="72" y="{a.Y(-3.2) + 5:.1f}" text-anchor="end" class="ax" fill="{ACC2}">Manch.</text>'
    b = Ax(266, 462, 30, 112, (0, 3), (0, 1.05))
    fs_ = [k / 100 for k in range(0, 301)]
    psd_n = [(f, sinc(f) ** 2) for f in fs_]
    psd_m = [(f, (sinc(f / 2) ** 2) * math.sin(math.pi * f / 2) ** 2 / .53) for f in fs_]
    s += title(364, 'power spectra', WHITE) + b.axes() + b.area(psd_n, ACC, .12) + b.line(psd_n, ACC, 2.6) + b.area(psd_m, ACC2, .12) + b.line(psd_m, ACC2, 2.6)
    s += b.dot(1, 0, ACC, 6) + b.dot(2, 0, ACC2, 6)
    s += b.xt(0, '0') + b.xt(1, '1', col=ACC) + b.xt(2, '2', col=ACC2) + b.xt(3, 'kHz', anchor='end')
    setup()
    o = [trace([(2.6, 2.7), (2.6, 3.4)]), trace([(4.0, 4.0), (5.0, 4.0)]), pad(5.0, 4.0)]
    for k, b_ in enumerate(bits):
        col = ACC if b_ else '#3A3270'
        o.append(box(.8 + k * .7, 1.9, .55, .7, .55, col, '#2A245E', '#3B3478'))
        o.append(lab(1.075 + k * .7, 2.25, .55, str(b_), '#17112E' if b_ else '#C9B3FF', 14, 5))
    o.append(chip(2.0, 3.4, 2.0, 1.4, 'Manchester', size=13))
    o.append(box(5.0, 3.75, 2.8, .5, .5, '#3E4650', '#1E242B', '#2A3038'))
    o.append(float_wave(5.0, 7.8, 4.0, 1.4, .55, lambda t: [h for b_ in bits for h in ((-1, 1) if b_ else (1, -1))][min(int(t * 10), 9)], n=400, col=ACC2))
    return spec('ec-comm-u4-L4', 'Time Division<br>&amp; Line Codes', 'Time Division &amp; Line Codes',
                'How wide is a Manchester signal?',
                f'Half-bit pulses: {G("2R<sub>b</sub>")},<br>double the {C("NRZ")} width',
                '1 0 1 1 0 at 1 kbit/s', card(s), board(o),
                chips(('left', 256, 'c', 'T<sub>b</sub> = 1 ms'), ('left', 534, 'g', '6 transitions'),
                      ('right', 262, 'g', 'NRZ null at 1 kHz'), ('right', 534, 'c', 'Manchester: 2 kHz')),
                f'Manchester splits each 1 ms bit into {cl("0.5 ms")} halves:<br>first null at 2R<sub>b</sub> = {gl("2 kHz")}, NRZ at 1 kHz')


# ================================================================ unit 5
def u5L1():
    """5.2 Worked example 1: 4800 bit/s, raised cosine alpha = 0.5"""
    Rb, al = 4800, .5
    Rs = Rb; Tsym = 1 / Rs; BN = Rs / 2; Bw = BN * (1 + al); ex = Bw - BN
    near(Tsym * 1e6, 208.3, .05); near(Bw, 3600, 0); near(ex, 1200, 0); near(BN * 2, 4800, 0)
    def rc(f, a_):
        f = abs(f); f1 = BN * (1 - a_)
        if f <= f1:
            return 1
        if f >= BN * (1 + a_):
            return 0
        return .5 * (1 + math.cos(math.pi * (f - f1) / (2 * a_ * BN)))
    a = Ax(40, 222, 30, 114, (0, 5000), (0, 1.15))
    s = title(131, 'raised cosine |P(f)|', WHITE) + a.axes()
    for a_, col, w in ((1, GREY, 2), (.5, ACC, 3.4)):
        s += a.line([(f, rc(f, a_)) for f in range(0, 5001, 25)], col, w)
    s += a.line([(0, 1), (2400, 1), (2400, 0)], ACC2, 2, '5 4')
    s += a.xt(2400, '2400', col=ACC2) + a.xt(3600, '3600', col=ACC) + a.xt(4800, '4800') + a.xt(0, '0') + a.tx(4300, .25, 'α = 1', GREY) + a.tx(3200, .78, 'α = 0.5', ACC, anchor='start')
    b = Ax(270, 462, 30, 114, (-4.2, 4.2), (-.3, 1.1))
    def p(t):
        x = t
        den = 1 - (2 * al * x) ** 2
        if abs(den) < 1e-6:
            return math.pi / 4 * sinc(1 / (2 * al))
        return sinc(x) * math.cos(math.pi * al * x) / den
    s += title(366, 'its pulse, zero at every T', WHITE) + b.axes(0)
    s += b.line([(k / 40, p(k / 40)) for k in range(-168, 169)], ACC, 3)
    for k in range(-4, 5):
        if k:
            s += b.dot(k, 0, ACC2, 4.5)
    s += b.xt(0, '0') + b.xt(1, 'T') + b.xt(4.2, 't', anchor='end') + b.tx(2.2, .55, 'T = 208.3 µs', ACC2)
    setup()
    o = [trace([(3.0, 2.4), (3.0, 3.2)]), trace([(4.6, 4.0), (5.4, 4.0)]), pad(5.4, 4.0)]
    for k, b_ in enumerate([1, 0, 1, 1, 0, 1]):
        o.append(box(.8 + k * .62, 1.7, .5, .6, .45, ACC if b_ else '#3A3270', '#2A245E', '#3B3478'))
    o.append(lab(2.6, 1.0, .4, '4800 bit/s', '#C9B3FF', 12, -2))
    o.append(module(2.0, 3.2, 2.6, 1.6, .7, '', top='#2B2464'))
    o.append(trace([(2.4, 4.5), (2.4, 3.8), (3.7, 3.8), (4.2, 3.4)], .72, ACC2, 3, 1))
    o.append(lab(3.3, 4.0, .7, 'α = 0.5', '#F1F4F7', 13, 26))
    o.append(box(5.4, 3.75, 2.4, .5, .5, '#3E4650', '#1E242B', '#2A3038'))
    o.append(float_wave(5.4, 7.8, 4.0, 1.4, .7, lambda t: sum(sg * p((t * 6 - k)) for k, sg in enumerate([1, -1, 1, 1, -1, 1])) * .8, n=300, col=ACC2))
    return spec('ec-comm-u5-L1', 'ISI, Nyquist<br>&amp; Pulse<br>Shaping', 'ISI, Nyquist &amp; Pulse Shaping',
                'How much bandwidth does roll-off add?',
                f'Roll-off adds {G("αR<sub>s</sub>/2")}:<br>{C("1200 Hz")} at α = 0.5',
                '4800 bit/s, α = 0.5', card(s), board(o),
                chips(('left', 256, 'c', 'R<sub>s</sub> = 4800 baud'), ('left', 534, 'g', 'Nyquist 2400 Hz'),
                      ('right', 262, 'g', 'B = 3600 Hz'), ('right', 534, 'c', 'α = 1: 4800 Hz')),
                f'B = (R<sub>s</sub>/2)(1 + α) = 2400 × 1.5 = {gl("3600 Hz")}<br>excess αR<sub>s</sub>/2 = 0.5 × 2400 = {cl("1200 Hz")}')


def u5L2():
    """5.3 Worked example 1: three-tap zero-forcing equalizer, h = 0.2, 1, 0.3"""
    hm1, h0, h1 = .2, 1, .3
    c0 = 1 / (1 - hm1 * .3 - h1 * .2)
    cm1, c1 = -hm1 * c0, -h1 * c0
    h = {-1: hm1, 0: h0, 1: h1}
    v = {m: sum(c * h.get(m - k, 0) for k, c in ((-1, cm1), (0, c0), (1, c1))) for m in range(-2, 3)}
    Db = (hm1 + h1) / h0; Da = (abs(v[-2]) + abs(v[2])) / v[0]; ng = cm1 ** 2 + c0 ** 2 + c1 ** 2
    near(c0, 1.1364, .00005); near(cm1, -.2273, .00005); near(c1, -.3409, .00005)
    near(v[-2], -.0455, .00005); near(v[2], -.1023, .00005); near(v[0], 1, 1e-9); near(v[1], 0, 1e-9); near(Da, .148, .0005); near(ng, 1.459, .0005)
    def stems(ax, vals, col):
        s_ = ax.axes(0)
        for m, y in vals.items():
            if abs(y) > 1e-9:
                s_ += ax.stem(m, y, col, 3.5, 5)
                s_ += ax.tx(m, y, (f'{y:.4f}'.replace('-', '−')) if abs(y) < 1 else '1', WHITE, dy=-9 if y > 0 else 18)
            else:
                s_ += ax.dot(m, 0, col, 4)
            s_ += ax.xt(m, str(m), dy=28)
        return s_
    a = Ax(30, 220, 34, 96, (-2.5, 2.5), (-.2, 1.1))
    s = title(125, 'channel h, D = 0.5', ACC) + stems(a, {m: h.get(m, 0) for m in range(-2, 3)}, ACC)
    b = Ax(264, 456, 34, 96, (-2.5, 2.5), (-.2, 1.1))
    s += title(360, f'equalized v, D = {Da:.3f}', ACC2) + stems(b, v, ACC2)
    setup()
    o = []
    xs = [1.4, 3.6, 5.8]
    o.append(trace([(.4, 2.0), (7.2, 2.0)]))
    for k, (x, c) in enumerate(zip(xs, (cm1, c0, c1))):
        o.append(trace([(x, 2.0), (x, 4.6)]) + trace([(x, 5.4), (x, 6.2), (4.0, 6.2)]))
        o.append(ring(x, 5.0, .35, 20, ACC, 3, '#1D1849'))
        o.append(lab(x, 5.0, .35, '×', '#F1F4F7', 18, 6))
        o.append(lab(x - .9, 4.6, 0, f'{c:.4f}'.replace('-', '−'), ACC if k != 1 else ACC2, 12, 0))
    for x in (2.2, 4.4):
        o.append(module(x, 1.5, 1.0, 1.0, .7, 'T', size=16))
    o.append(module(3.4, 6.2, 1.2, 1.2, .7, 'Σ', top='#1F8C78', left='#0F4A40', right='#166A5A', size=18))
    o.append(pad(.4, 2.0))
    return spec('ec-comm-u5-L2', 'Equalizers &amp;<br>Signal Space', 'Equalizers &amp; Signal Space',
                'Does a 3-tap equalizer kill all ISI?',
                f'Zero-forcing clears the<br>{G("NEIGHBOURS")}, not {C("ALL")} of it',
                'h = 0.2, 1, 0.3', card(s), board(o),
                chips(('left', 256, 'g', 'c<sub>0</sub> = 1.1364'), ('left', 534, 'c', 'v<sub>±1</sub> = 0'),
                      ('right', 262, 'c', 'D: 0.5 → 0.148'), ('right', 534, 'g', 'noise × 1.459')),
                f'v<sub>±1</sub> = 0, but v<sub>−2</sub> = −0.0455 and v<sub>2</sub> = −0.1023 remain<br>peak distortion {gl("0.5 → 0.148")}, noise power {cl("× 1.459")}')


def u5L3():
    """5.5 Worked example 1: matched filter for a 1 V, 1 ms rectangle"""
    A, Tp, N0 = 1, 1e-3, 2e-6
    E = A ** 2 * Tp; var = N0 / 2 * E; snr = E ** 2 / var
    near(E, 1e-3, 1e-15); near(var, 1e-9, 1e-20); near(snr, 1000, 1e-6); near(2 * E / N0, 1000, 1e-6); near(10 * math.log10(snr), 30, 1e-9)
    a = Ax(40, 222, 34, 112, (-.2, 2.2), (0, 1.3))
    s = title(131, 'pulse s(t), 1 V', ACC) + a.axes()
    s += a.area([(0, 1), (1, 1)], ACC, .16) + a.line([(-.2, 0), (0, 0), (0, 1), (1, 1), (1, 0), (2.2, 0)], ACC, 3)
    s += a.yt(1, '1 V') + a.xt(0, '0') + a.xt(1, '1') + a.xt(2.2, 'ms', anchor='end')
    b = Ax(270, 462, 34, 112, (-.2, 2.2), (0, 1.3))
    s += title(366, 'filter output y(t)', ACC2) + b.axes()
    tri = [(-.2, 0), (0, 0), (1, 1), (2, 0), (2.2, 0)]
    s += b.area(tri, ACC2, .16) + b.line(tri, ACC2, 3) + b.dot(1, 1, ACC2, 6) + b.line([(1, 0), (1, 1)], WHITE, 1.4, '4 4')
    s += b.tx(1, 1, 'E at t = T', ACC2, dy=-8) + b.xt(0, '0') + b.xt(1, 'T = 1') + b.xt(2, '2') + b.xt(2.2, 'ms', anchor='end', dy=-4)
    setup()
    o = [trace([(1.7, 4.0), (2.4, 4.0)]), trace([(4.2, 4.0), (4.9, 4.0)]), trace([(5.9, 4.0), (6.5, 4.0)]), trace([(5.4, 1.6), (5.4, 3.6)]), pad(.6, 4.0), trace([(.6, 4.0), (1.0, 4.0)])]
    o.append(module(2.4, 3.3, 1.8, 1.4, .8, 'h = s(T − t)', size=12))
    o.append(box(4.9, 3.75, .45, .5, .5, '#C9D0D6', '#7D8792', '#9AA4AE') + box(5.5, 3.75, .45, .5, .5, '#C9D0D6', '#7D8792', '#9AA4AE'))
    (xa, ya), (xb, yb) = P(5.12, 4.0, .55), P(5.72, 3.7, .95)
    o.append(f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb:.1f}" y2="{yb:.1f}" stroke="#F1F4F7" stroke-width="5" stroke-linecap="round"/>')
    o.append(crystal(4.8, .9, 't = T', w=1.2))
    o.append(chip(6.5, 3.4, 1.3, 1.2, 'decide', size=12))
    o.append(float_wave(.4, 2.2, 2.4, 1.5, .8, lambda t: 1 if .25 < t < .75 else 0, n=120, col=ACC))
    o.append(float_wave(3.0, 5.0, 2.0, 1.7, .9, lambda t: max(0, 1 - abs(t - .5) / .3), n=120, col=ACC2))
    return spec('ec-comm-u5-L3', 'Matched Filter,<br>Detection<br>&amp; PAM', 'Matched Filter, Detection &amp; PAM',
                'What SNR does a matched filter give?',
                f'SNR = {G("2E/N<sub>0</sub>")}, at its<br>peak exactly at {C("t = T")}',
                '1 V, 1 ms rectangle', card(s), board(o),
                chips(('left', 256, 'g', 'E = A²T = 1 mJ'), ('left', 534, 'c', 'σ² = (N<sub>0</sub>/2)E = 10<sup>−9</sup>'),
                      ('right', 262, 'c', 'N<sub>0</sub> = 2×10<sup>−6</sup> W/Hz'), ('right', 534, 'g', '1000 = 30 dB')),
                f'SNR = 2E/N<sub>0</sub> = 2×10<sup>−3</sup> ÷ 2×10<sup>−6</sup> = {gl("1000")} = {cl("30 dB")}<br>sampled at t = T = 1 ms, where the triangle peaks')


# ================================================================ unit 6
def u6L1():
    """6.3 Worked example 2: four receivers at Eb/N0 = 10 dB"""
    g10 = 10 ** (10 / 10)
    pb = {'BPSK': Q(math.sqrt(2 * g10)), 'DPSK': .5 * math.exp(-g10), 'BFSK': Q(math.sqrt(g10)), 'NC BFSK': .5 * math.exp(-g10 / 2)}
    near(pb['BPSK'] * 1e6, 3.87, .005); near(pb['DPSK'] * 1e5, 2.27, .005); near(pb['BFSK'] * 1e4, 7.83, .005); near(pb['NC BFSK'] * 1e3, 3.37, .005)
    f = {'BPSK': lambda x: Q(math.sqrt(2 * x)), 'DPSK': lambda x: .5 * math.exp(-x), 'BFSK': lambda x: Q(math.sqrt(x)), 'NC BFSK': lambda x: .5 * math.exp(-x / 2)}
    cols = {'BPSK': ACC, 'DPSK': '#C9B3FF', 'BFSK': '#7FE8D6', 'NC BFSK': ACC2}
    a = Ax(56, 340, 24, 116, (0, 12), (1e-7, .5), logy=True)
    s = a.axes() + a.line([(10, 1e-7), (10, .5)], GREY, 1.4, '4 4')
    for k, fn in f.items():
        s += a.line([(x / 4, fn(10 ** (x / 40))) for x in range(0, 49)], cols[k], 2.6)
        s += a.dot(10, pb[k], cols[k], 5)
    s += a.yt(1e-1, '10<tspan baseline-shift="super" font-size="70%">−1</tspan>') + a.yt(1e-4, '10<tspan baseline-shift="super" font-size="70%">−4</tspan>') + a.yt(1e-7, '10<tspan baseline-shift="super" font-size="70%">−7</tspan>')
    s += a.xt(0, '0') + a.xt(10, '10 dB') + a.xt(12, 'E<tspan baseline-shift="sub" font-size="70%">b</tspan>/N<tspan baseline-shift="sub" font-size="70%">0</tspan>', anchor='start', dy=16).replace('text-anchor="start"', 'text-anchor="start" dx="4"')
    s += f'<text x="52" y="18" class="ax">P<tspan baseline-shift="sub" font-size="70%">b</tspan></text>'
    for i, k in enumerate(('BPSK', 'DPSK', 'BFSK', 'NC BFSK')):
        y = 34 + i * 26
        s += f'<rect x="352" y="{y - 12}" width="14" height="14" rx="3" fill="{cols[k]}"/><text x="372" y="{y}" class="ax" fill="{WHITE}">{k if k != "BFSK" else "coh. BFSK"}</text>'
    setup()
    o = [trace([(.8, 6.6), (6.6, .8)], .01, GOLD, 2.6, .6)]
    order = ('NC BFSK', 'BFSK', 'DPSK', 'BPSK')          # a staircase: fewer errors, taller bar
    tops = {'BPSK': ACC, 'DPSK': '#C9B3FF', 'BFSK': '#7FE8D6', 'NC BFSK': ACC2}
    names = {'BPSK': 'BPSK', 'DPSK': 'DPSK', 'BFSK': 'coh. FSK', 'NC BFSK': 'NC FSK'}
    for i, k in enumerate(order):
        a0, b0 = 1.2 + i * 1.5, 5.6 - i * 1.5
        h = (-math.log10(pb[k]) - 1) * .62
        t = sci(pb[k], 2).replace('<sup>', '<tspan baseline-shift="super" font-size="70%">').replace('</sup>', '</tspan>')
        o.append(bar3(a0, b0, h, tops[k], '#2A245E', '#3B3478', w=.9, t=t, tcol=tops[k]))
        o.append(lab(a0 + 1.0, b0 + 1.0, 0, names[k], '#F1F4F7', 13, 4))
    return spec('ec-comm-u6-L1', 'Binary ASK,<br>FSK, BPSK<br>&amp; DPSK', 'Binary ASK, FSK, BPSK &amp; DPSK',
                'Which receiver makes fewer errors?',
                f'{G("BPSK")} wins; non-coherent<br>{C("BFSK")} comes last',
                'four receivers at 10 dB', card(s), board(o),
                chips(('left', 256, 'g', 'E<sub>b</sub>/N<sub>0</sub> = 10'), ('left', 534, 'c', '½e<sup>−5</sup> = 3.37×10<sup>−3</sup>'),
                      ('right', 262, 'g', 'Q(√20) = 3.87×10<sup>−6</sup>'), ('right', 534, 'c', '½e<sup>−10</sup> = 2.27×10<sup>−5</sup>')),
                f'BPSK {gl("3.87×10<sup>−6</sup>")} &lt; DPSK 2.27×10<sup>−5</sup><br>&lt; BFSK 7.83×10<sup>−4</sup> &lt; non-coherent {cl("3.37×10<sup>−3</sup>")}')


def u6L2():
    """6.5 Worked example 1: 16-QAM, Gray labels, 20 Mb/s, Eb/N0 = 10 dB"""
    M, Rb = 16, 20
    k = int(math.log2(M)); Rs = Rb / k; Bw = 2 * Rs; eff = Rb / Bw
    EsN0 = k * 10; arg = math.sqrt(3 * EsN0 / (M - 1)); Ps = 4 * (1 - 1 / math.sqrt(M)) * Q(arg); Pb = Ps / k
    near(k, 4, 0); near(Rs, 5, 0); near(Bw, 10, 0); near(eff, 2, 0); near(arg, 2.828, .0005); near(Ps * 1e3, 7.02, .005); near(Pb * 1e3, 1.75, .005)
    gray = {-3: '00', -1: '01', 1: '11', 3: '10'}
    a = Ax(64, 214, 26, 126, (-4.2, 4.2), (-4.2, 4.2))
    s = a.line([(-4.2, 0), (4.2, 0)], GREY, 1.2) + a.line([(0, -4.2), (0, 4.2)], GREY, 1.2)
    for i in (-3, -1, 1, 3):
        for q in (-3, -1, 1, 3):
            hit = (i, q) == (3, 1)
            s += a.dot(i, q, ACC2 if hit else ACC, 7 if hit else 5)
        s += f'<text x="{a.X(i):.1f}" y="140" text-anchor="middle" class="ax">{gray[i]}</text>'
        s += f'<text x="{a.x0 - 8}" y="{a.Y(i) + 5:.1f}" text-anchor="end" class="ax">{gray[i]}</text>'
    s += f'<circle cx="{a.X(3):.1f}" cy="{a.Y(1):.1f}" r="13" fill="none" stroke="{ACC2}" stroke-width="2.4"/>'
    s += a.tx(3, 2.05, '1011', ACC2, dy=5, cls='pt')
    s += f'<text x="{a.x1 + 6}" y="{a.Y(0) + 4:.1f}" class="ax">I</text><text x="{a.X(0) + 6:.1f}" y="22" class="ax">Q</text>'
    rows = (('k = log₂ 16 = 4 bits', ACC2), ('R<tspan baseline-shift="sub" font-size="70%">s</tspan> = 20 ÷ 4 = 5 Msym/s', WHITE), ('B = 2R<tspan baseline-shift="sub" font-size="70%">s</tspan> = 10 MHz', WHITE), ('20 ÷ 10 = 2 b/s/Hz', ACC))
    for i, (v, col) in enumerate(rows):
        y = 40 + i * 28
        s += f'<text x="252" y="{y}" class="ax" fill="{col}" style="font-weight:600;font-size:16px">{v}</text>'
    setup()
    o = []
    for kk, bch in enumerate('1011'):
        col = ACC if kk < 2 else ACC2
        o.append(box(.8 + kk * .75, 1.4, .6, .7, .6, col if bch == '1' else '#2A245E', '#2A245E', '#3B3478'))
        o.append(lab(1.1 + kk * .75, 1.75, .6, bch, '#17112E' if bch == '1' else '#C9B3FF', 15, 5))
    o.append(trace([(1.5, 2.1), (1.5, 3.4)]) + trace([(3.0, 2.1), (3.0, 5.0)]))
    o.append(module(.9, 3.4, 1.4, 1.0, .6, 'I: +3a', size=13))
    o.append(module(2.4, 5.0, 1.4, 1.0, .6, 'Q: +a', top='#1F8C78', left='#0F4A40', right='#166A5A', size=13))
    o.append(trace([(2.3, 3.9), (4.0, 3.9)]) + trace([(3.8, 5.5), (4.6, 5.5), (4.6, 4.6)]))
    o.append(chip(4.0, 3.2, 1.6, 1.4, 'QAM', size=15))
    o.append(trace([(5.6, 3.9), (6.4, 3.9)]) + pad(6.4, 3.9))
    for i in (-3, -1, 1, 3):
        for q in (-3, -1, 1, 3):
            hit = (i, q) == (3, 1)
            x, y = P(6.9 + i * .13, 2.0 - q * .13, 1.8)
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{6 if hit else 3.5}" fill="{ACC2 if hit else "#C9B3FF"}"{" filter=\"url(#gl)\"" if hit else ""}/>')
    return spec('ec-comm-u6-L2', 'QPSK, QAM<br>&amp; MSK', 'QPSK, QAM &amp; MSK',
                'How many bits ride on a 16-QAM symbol?',
                f'log₂ 16 = {G("4 BITS")}<br>on every {C("SYMBOL")}',
                '16-QAM, Gray, 20 Mb/s', card(s), board(o),
                chips(('left', 256, 'g', '10 → I = +3a'), ('left', 534, 'c', '11 → Q = +a'),
                      ('right', 262, 'c', 'E<sub>s</sub>/N<sub>0</sub> = 4 × 10 = 40'), ('right', 534, 'g', 'P<sub>b</sub> ≈ 1.75×10<sup>−3</sup>')),
                f'k = log<sub>2</sub> 16 = {gl("4 bits")}; R<sub>s</sub> = 20 ÷ 4 = 5 Msymbol/s<br>1011 → (3a, a); B = 10 MHz, so {cl("2 b/s/Hz")}')


def u6L3():
    """6.9 Worked example 1: OFDM, 64 subcarriers in 20 MHz, 16-sample prefix, 64-QAM"""
    N, Bw, ncp = 64, 20e6, 16
    df = Bw / N; Tu = 1 / df; Tcp = ncp / Bw; Tt = Tu + Tcp; ov = Tcp / Tt
    R = N * 6 / Tt; Rw = 48 * 6 * .75 / Tt
    near(df / 1e3, 312.5, 1e-9); near(Tu * 1e6, 3.2, 1e-9); near(Tcp * 1e6, .8, 1e-9); near(Tt * 1e6, 4, 1e-9); near(ov, .2, 1e-9); near(R / 1e6, 96, 1e-6); near(Rw / 1e6, 54, 1e-6)
    a = Ax(30, 222, 40, 112, (0, 4), (-1.4, 1.6))
    sig = lambda t: .55 * math.sin(2 * math.pi * 1.9 * t + .4) + .4 * math.sin(2 * math.pi * 3.3 * t + 1.1) + .25 * math.cos(2 * math.pi * 5.1 * t)
    s = title(126, 'one symbol, 4.0 µs', WHITE)
    s += f'<rect x="{a.X(0):.1f}" y="40" width="{a.X(.8) - a.X(0):.1f}" height="72" fill="{ACC}" opacity=".22"/>'
    s += f'<rect x="{a.X(3.2):.1f}" y="40" width="{a.X(4) - a.X(3.2):.1f}" height="72" fill="{ACC}" opacity=".10"/>'
    s += a.line([(t / 100, sig(t / 100 + 2.4)) for t in range(0, 81)], ACC, 2.6) + a.line([(.8 + t / 100, sig(t / 100)) for t in range(0, 321)], ACC2, 2.6)
    s += f'<path d="M{a.X(3.6):.1f},36 C{a.X(3.4):.1f},22 {a.X(.6):.1f},22 {a.X(.4):.1f},36" fill="none" stroke="{ACC}" stroke-width="1.8" stroke-dasharray="4 3"/>'
    s += a.xt(0, '0') + a.xt(.8, '0.8') + a.xt(4, '4.0 µs', anchor='end') + a.tx(.4, -1.35, 'prefix', ACC, dy=0) + a.tx(2.4, -1.35, 'useful 3.2 µs', ACC2)
    b = Ax(270, 462, 30, 112, (-3.6, 3.6), (-.3, 1.1))
    s += title(366, '312.5 kHz apart', WHITE) + b.axes(0)
    for kk in range(-2, 3):
        col = ACC2 if kk == 0 else ACC
        s += b.line([(x / 40, sinc(x / 40 - kk)) for x in range(-144, 145)], col, 2.2 if kk else 3, op=1 if kk == 0 else .75)
    s += b.xt(0, '0') + b.xt(1, '1') + b.xt(2, '2') + b.xt(3.6, '×Δf', anchor='end', dy=-4)
    setup()
    o = [trace([(1.9, 4.0), (2.6, 4.0)]), trace([(4.4, 4.0), (5.0, 4.0)]), trace([(6.4, 4.0), (7.0, 4.0)])]
    o.append(module(.5, 3.4, 1.4, 1.2, .6, '64-QAM', size=12))
    o.append(chip(2.6, 3.2, 1.8, 1.6, '64 IFFT', size=14))
    o.append(module(5.0, 3.4, 1.4, 1.2, .7, '+ CP', top='#6D57C9', left='#3A2D7A', right='#4C3D9C', size=14))
    o.append(antenna(7.3, 4.0, 3.0))
    for kk in range(5):
        a0 = 2.2 + kk * .35
        o.append(float_wave_d(a0, 1.2 - kk * .1, a0 + 1.8, 1.2 - kk * .1 - 1.8 + 1.8, 1.4 + kk * .0, .45,
                              lambda t, kk=kk: sinc((t - .5) * 4), n=80, col=ACC2 if kk == 2 else '#C9B3FF', w=2.2))
    return spec('ec-comm-u6-L3', 'Constellations,<br>Spread Spectrum<br>&amp; OFDM', 'Constellations, Spread Spectrum &amp; OFDM',
                'What does the cyclic prefix cost?',
                f'{G("20 %")} of the air time<br>carries {C("NO")} new data',
                '64 subcarriers in 20 MHz', card(s), board(o),
                chips(('left', 256, 'c', 'Δf = 312.5 kHz'), ('left', 534, 'g', 'T<sub>cp</sub> = 0.8 µs'),
                      ('right', 262, 'g', '96 Mb/s uncoded'), ('right', 534, 'c', 'Wi-Fi: 54 Mb/s')),
                f'T<sub>cp</sub> = 16 × 50 ns = 0.8 µs of T = 4.0 µs: {gl("20 %")}<br>64 × 6 bits per 4 µs = 96 Mb/s; Wi-Fi {cl("54 Mb/s")}')


# ================================================================ unit 7
def u7L1():
    """7.2 Worked example 1: Huffman code for 0.4, 0.2, 0.2, 0.1, 0.1, two tie choices"""
    p = {'A': .4, 'B': .2, 'C': .2, 'D': .1, 'E': .1}
    H = -sum(v * math.log2(v) for v in p.values())
    l1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 4}; l2 = {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3}
    L1 = sum(p[s_] * l1[s_] for s_ in p); L2 = sum(p[s_] * l2[s_] for s_ in p)
    v1 = sum(p[s_] * (l1[s_] - L1) ** 2 for s_ in p); v2 = sum(p[s_] * (l2[s_] - L2) ** 2 for s_ in p)
    near(H, 2.1219, .00005); near(L1, 2.2, 1e-9); near(L2, 2.2, 1e-9); near(H / L1 * 100, 96.45, .005); near(v1, 1.36, 1e-9); near(v2, .16, 1e-9)
    assert sum(2 ** -l for l in l1.values()) == 1 and sum(2 ** -l for l in l2.values()) == 1
    def tree(nodes, edges, leaves, col):
        s_ = ''.join(f'<line x1="{nodes[a_][0]}" y1="{nodes[a_][1]}" x2="{nodes[b_][0]}" y2="{nodes[b_][1]}" stroke="{col}" stroke-width="2.4"/>' for a_, b_ in edges)
        for n_, (x, y) in nodes.items():
            if n_ in leaves:
                s_ += f'<circle cx="{x}" cy="{y}" r="11" fill="{col}"/><text x="{x}" y="{y + 5}" text-anchor="middle" class="ax" fill="#120F31" style="font-weight:700">{n_}</text>'
            else:
                s_ += f'<circle cx="{x}" cy="{y}" r="5" fill="{WHITE}"/>'
        return s_
    n1 = {'r': (120, 34), 'A': (60, 60), 'x': (170, 60), 'B': (125, 84), 'y': (205, 84), 'C': (170, 108), 'z': (225, 108), 'D': (200, 130), 'E': (246, 130)}
    e1 = [('r', 'A'), ('r', 'x'), ('x', 'B'), ('x', 'y'), ('y', 'C'), ('y', 'z'), ('z', 'D'), ('z', 'E')]
    s = title(125, 'lengths 1, 2, 3, 4, 4', ACC) + tree(n1, e1, 'ABCDE', ACC)
    n2 = {'r': (366, 34), 'u': (310, 64), 'v': (420, 64), 'A': (282, 100), 'w': (338, 100), 'B': (394, 100), 'C': (446, 100), 'D': (316, 130), 'E': (360, 130)}
    e2 = [('r', 'u'), ('r', 'v'), ('u', 'A'), ('u', 'w'), ('w', 'D'), ('w', 'E'), ('v', 'B'), ('v', 'C')]
    s += title(366, 'lengths 2, 2, 2, 3, 3', ACC2) + tree(n2, e2, 'ABCDE', ACC2)
    setup()
    o = []
    # the first tree standing on the board: posts for nodes, joined by bars; leaves as labelled discs
    nodes = {'r': (1.2, 1.2, 2.4), 'A': (1.2, 3.2, .9), 'x': (3.0, 1.6, 2.0), 'B': (2.9, 3.9, .9), 'y': (4.6, 2.2, 1.6), 'C': (4.4, 4.6, .9), 'z': (6.0, 2.9, 1.25), 'D': (5.6, 5.4, .9), 'E': (7.0, 4.9, .9)}
    for a_, b_ in e1:
        (x1, y1), (x2, y2) = P(*nodes[a_]), P(*nodes[b_])
        o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#C9B3FF" stroke-width="4" stroke-linecap="round"/>')
    for n_, (a_, b_, z) in nodes.items():
        x0, y0 = P(a_, b_, 0); x1, y1 = P(a_, b_, z)
        o.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#5C50AE" stroke-width="2" stroke-dasharray="3 4"/>')
        if n_ in 'ABCDE':
            o.append(cyl(x1, y1 + 8, 19, 10, 8, ACC2 if n_ == 'A' else ACC, '#E8FFFA' if n_ == 'A' else '#E2D8FF'))
            o.append(f'<text x="{x1:.1f}" y="{y1 + 4:.1f}" text-anchor="middle" class="capl" fill="#120F31">{n_}</text>')
            o.append(lab(a_, b_, z - .75, f'{p[n_]:g}', '#C9B3FF', 11, 0))
        else:
            o.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="7" fill="#F1F4F7"/>')
    return spec('ec-comm-u7-L1', 'Measuring<br>Information', 'Measuring Information',
                'Is a Huffman code unique?',
                f'Two {G("TREES")}, the same<br>average: {C("2.2 bits")}',
                'Huffman, five symbols', card(s), board(o),
                chips(('left', 256, 'c', 'H = 2.12 bits'), ('left', 534, 'g', 'A = 0, B = 10, C = 110'),
                      ('right', 262, 'g', 'η = 96.45 %'), ('right', 534, 'c', 'σ² 1.36 or 0.16')),
                f'tie broken two ways: lengths 1,2,3,4,4 or 2,2,2,3,3<br>both average {gl("2.2 bits")}; variance 1.36 or {cl("0.16")}')


def u7L2():
    """7.4 Worked example 1: telephone channel 3.1 kHz, 30 dB and 20 dB; BSC p = 0.01"""
    Bw = 3100
    Cap = lambda snr_db: Bw * math.log2(1 + 10 ** (snr_db / 10))
    c30, c20 = Cap(30), Cap(20)
    Hb = lambda p_: -p_ * math.log2(p_) - (1 - p_) * math.log2(1 - p_)
    cb = 1 - Hb(.01)
    near(c30 / 1e3, 30.9, .05); near(c20 / 1e3, 20.6, .05); near(cb, .919, .0005)
    a = Ax(44, 222, 30, 112, (0, 40), (0, 45))
    cur = [(x, Cap(x) / 1e3) for x in range(0, 41)]
    s = title(133, 'C, kbit/s, B = 3.1 kHz', ACC) + a.axes()
    s += f'<polygon points="{" ".join(f"{a.X(x):.1f},{a.Y(y):.1f}" for x, y in cur)} {a.X(40):.1f},{a.Y(45):.1f} {a.X(0):.1f},{a.Y(45):.1f}" fill="#FF6B6B" opacity=".10"/>'
    s += a.area(cur, ACC, .14) + a.line(cur, ACC, 3)
    s += a.dot(30, c30 / 1e3, ACC2, 6) + a.dot(20, c20 / 1e3, ACC, 5)
    s += a.tx(30, c30 / 1e3, f'{c30 / 1e3:.1f}', ACC2, anchor='end', dy=-6).replace('text-anchor="end"', 'text-anchor="end" dx="-6"')
    s += a.tx(20, c20 / 1e3, f'{c20 / 1e3:.1f}', ACC, anchor='end', dy=-6).replace('text-anchor="end"', 'text-anchor="end" dx="-6"')
    s += a.tx(1, 41, 'no code works', '#FF9C9C', anchor='start')
    s += a.yt(40, '40') + a.yt(0, '0') + a.xt(0, '0') + a.xt(20, '20') + a.xt(30, '30') + a.xt(40, 'dB', anchor='end')
    b = Ax(276, 462, 30, 112, (0, .5), (0, 1.05))
    bc = [(x / 200, 1 - Hb(x / 200) if x else 1) for x in range(0, 101)]
    s += title(369, 'BSC: C = 1 − H(p)', ACC2) + b.axes() + b.area(bc, ACC2, .14) + b.line(bc, ACC2, 3) + b.dot(.01, cb, ACC2, 6)
    s += b.tx(.01, cb, f'{cb:.3f} at p = 0.01', WHITE, anchor='start', dy=6).replace('text-anchor="start"', 'text-anchor="start" dx="10"')
    s += b.yt(1, '1') + b.xt(0, '0') + b.xt(.5, 'p = 0.5', anchor='end')
    setup()
    o = [trace([(1.8, 4.0), (2.6, 4.0)]), trace([(4.4, 4.0), (5.0, 4.0)]), trace([(6.0, 4.0), (6.6, 4.0)]), trace([(5.5, 1.8), (5.5, 3.5)])]
    o.append(chip(.4, 3.3, 1.4, 1.4, 'coder', size=13))
    o.append(module(2.6, 3.4, 1.8, 1.2, .7, '3.1 kHz', top='#2B2464', size=14))
    o.append(ring(5.5, 4.0, .4, 20, ACC2, 3, '#1D1849'))
    o.append(lab(5.5, 4.0, .4, '+', ACC2, 20, 7))
    o.append(module(4.9, .8, 1.2, 1.0, .6, 'noise', top='#5B6470', left='#2E343C', right='#3E4650', size=13))
    o.append(chip(6.6, 3.3, 1.2, 1.4, 'dec.', size=13))
    o.append(float_wave(2.6, 4.4, 2.6, 1.6, .5, lambda t: math.sin(2 * math.pi * 3 * t), n=100))
    o.append(float_wave(5.2, 7.6, 1.6, 1.6, .5, lambda t: math.sin(2 * math.pi * 3 * t) + .35 * math.sin(2 * math.pi * 41 * t) * math.cos(2 * math.pi * 17 * t), n=260, col=ACC2))
    return spec('ec-comm-u7-L2', 'Channel<br>Capacity &amp;<br>Coding', 'Channel Capacity &amp; Coding',
                'Can you beat channel capacity?',
                f'Below {G("C")} errors can vanish;<br>above it, {C("NEVER")}',
                'phone line, 3.1 kHz', card(s), board(o),
                chips(('left', 256, 'g', 'S/N = 1000 (30 dB)'), ('left', 534, 'c', '20 dB: 20.6 kbit/s'),
                      ('right', 262, 'g', 'log₂ 1001 = 9.967'), ('right', 534, 'c', 'BSC: 0.919 bit/use')),
                f'C = B log<sub>2</sub>(1 + S/N) = 3100 × 9.967 = {gl("30.9 kbit/s")}<br>at 20 dB only {cl("20.6 kbit/s")}: no code runs faster')


def u7L3():
    """7.8 Worked example 1: K = 3 convolutional code g1 = 111, g2 = 101, message 1011, Viterbi"""
    K = 3; ns = 2 ** (K - 1)
    msg = [1, 0, 1, 1, 0, 0]
    st, out, path = (0, 0), [], [(0, 0)]
    for u in msg:
        s1, s2 = st
        out.append((u ^ s1 ^ s2, u ^ s2))
        st = (u, s1); path.append(st)
    code = ''.join(f'{a_}{b_}' for a_, b_ in out)
    rx = list(code); rx[6] = '1' if rx[6] == '0' else '0'; rx = ''.join(rx)
    assert code == '111000010111' and rx == '111000110111' and ns == 4
    # Viterbi, hard decision
    states = [(0, 0), (1, 0), (0, 1), (1, 1)]
    INF = 99
    pm = {s_: (0 if s_ == (0, 0) else INF) for s_ in states}; prev = []
    for k in range(6):
        r = (int(rx[2 * k]), int(rx[2 * k + 1])); new, bp = {s_: INF for s_ in states}, {}
        for s_ in states:
            if pm[s_] >= INF:
                continue
            for u in ((0, 1) if k < 4 else (0,)):
                o_ = (u ^ s_[0] ^ s_[1], u ^ s_[1]); ns_ = (u, s_[0])
                m_ = pm[s_] + (o_[0] != r[0]) + (o_[1] != r[1])
                if m_ < new[ns_]:
                    new[ns_], bp[ns_] = m_, s_
        pm = new; prev.append(bp)
    final = pm[(0, 0)]
    tb, s_ = [(0, 0)], (0, 0)
    for bp in reversed(prev):
        s_ = bp[s_]; tb.append(s_)
    tb.reverse()
    dec = [p_[0] for p_ in tb[1:]][:4]
    assert final == 1 and dec == [1, 0, 1, 1] and tb == path
    a = Ax(70, 454, 34, 124, (0, 6), (3.3, -.3))
    rowname = {(0, 0): '00', (1, 0): '10', (0, 1): '01', (1, 1): '11'}
    row = {s_: i for i, s_ in enumerate(states)}
    s = ''
    for k in range(6):
        for s_ in states:
            for u in (0, 1):
                ns_ = (u, s_[0])
                s += f'<line x1="{a.X(k):.1f}" y1="{a.Y(row[s_]):.1f}" x2="{a.X(k + 1):.1f}" y2="{a.Y(row[ns_]):.1f}" stroke="{GREY}" stroke-width="1" opacity=".55"/>'
    s += a.line([(k, row[p_]) for k, p_ in enumerate(path)], ACC2, 4)
    for k in range(7):
        for s_ in states:
            s += a.dot(k, row[s_], WHITE if (k, s_) in [(i, p_) for i, p_ in enumerate(path)] else '#5C6B7A', 4.5)
    for s_ in states:
        s += f'<text x="58" y="{a.Y(row[s_]) + 5:.1f}" text-anchor="end" class="ax">{rowname[s_]}</text>'
    for k in range(6):
        pr = rx[2 * k:2 * k + 2]
        s += f'<text x="{(a.X(k) + a.X(k + 1)) / 2:.1f}" y="20" text-anchor="middle" class="ax" fill="{ACC if k == 3 else WHITE}">{pr}</text>'
    s += f'<text x="{a.X(6):.1f}" y="140" text-anchor="end" class="ax" fill="{ACC2}">metric 1 → 1011</text>'
    s += f'<text x="{a.X(3.5):.1f}" y="140" text-anchor="middle" class="ax" fill="{ACC}">flipped bit</text>'
    setup()
    o = [trace([(.6, 3.0), (1.2, 3.0)]), pad(.6, 3.0)]
    regs = [('1', 1.2), ('1', 2.5), ('0', 3.8)]
    for t_, x in regs:
        o.append(module(x, 2.5, 1.1, 1.0, .7, t_, top='#3B3478', size=18))
    o.append(lab(1.75, 3.0, .7, 'u', '#C9B3FF', 11, -18))
    o.append(trace([(2.3, 3.0), (2.5, 3.0)]) + trace([(3.6, 3.0), (3.8, 3.0)]))
    for x in (1.75, 3.05, 4.35):
        o.append(trace([(x, 3.5), (x, 4.8)]))
    o.append(trace([(1.75, 4.8), (4.35, 4.8), (5.4, 4.8)]))
    o.append(trace([(1.75, 3.5), (1.75, 6.2), (4.35, 6.2)]) + trace([(4.35, 4.8), (4.35, 6.2), (5.4, 6.2)]))
    for y, lbl, col in ((4.8, 'v₁', ACC), (6.2, 'v₂', ACC2)):
        o.append(ring(5.7, y, .35, 18, col, 3, '#1D1849'))
        o.append(lab(5.7, y, .35, '+', col, 20, 7))
        o.append(trace([(6.0, y), (6.9, y)]))
        o.append(lab(7.3, y, 0, lbl, col, 15, 5))
    o.append(lab(5.0, 2.4, 0, 'g₁ = 111, g₂ = 101', '#C9B3FF', 12, 0))
    return spec('ec-comm-u7-L3', 'Cyclic,<br>Convolutional<br>&amp; Turbo Codes', 'Cyclic, Convolutional &amp; Turbo Codes',
                'How many states has a K = 3 code?',
                f'2<sup>K−1</sup> = {G("4 STATES")},<br>one {C("SURVIVOR")} each',
                'K = 3, message 1011', card(s), board(o),
                chips(('left', 256, 'g', 'K − 1 = 2 memory bits'), ('left', 534, 'c', 'sent 11 10 00 01 01 11'),
                      ('right', 262, 'c', 'bit 7 flipped'), ('right', 534, 'g', 'final metric 1')),
                f'K = 3 keeps 2 bits: 2<sup>2</sup> = {gl("4 states")} 00, 10, 01, 11<br>the Viterbi traceback gives {cl("1011")}: the error is fixed')


# titles with a word wider than the 535 px column: condense the width axis a little, keep 76 px.
# Every spec sets its own rule because t16_split.css() builds on the previous page's CSS (extra css would leak on).
STRETCH = {'ec-comm-u1-L2': (92, '-.02em'), 'ec-comm-u2-L4': (85, '-.03em'), 'ec-comm-u6-L3': (85, '-.03em')}


def specs():
    out = [u1L1(), u1L2(), u1L3(), u2L1(), u2L2(), u2L3(), u2L4(), u3L1(), u3L2(), u3L3(), u3L4(),
            u4L1(), u4L2(), u4L3(), u4L4(), u5L1(), u5L2(), u5L3(), u6L1(), u6L2(), u6L3(), u7L1(), u7L2(), u7L3()]
    for sp in out:
        st, ls = STRETCH.get(sp['key'], (100, '-.02em'))
        sp['css'] += f"h1{{font-stretch:{st}% !important;letter-spacing:{ls} !important}}"
    return out
