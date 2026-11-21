# Shared helpers for the ECE glass t16 drawings (ec-comm, ec-optical). Taken from d_signals.py.
from gfx import *
import math, re as _re
g = lambda v: f'{v:g}'.replace('-', '−')
f1 = lambda v: f'{v:.1f}'.replace('-', '−')
f2 = lambda v: f'{v:.2f}'.replace('-', '−')


def R(s):
    """'10^{-6}' -> escaped text with a real superscript tspan; '_{x}' -> subscript"""
    out, i = '', 0
    for m in _re.finditer(r'([\^_])\{([^}]*)\}', s):
        sh = 'super' if m.group(1) == '^' else 'sub'
        out += E(s[i:m.start()]) + f'<tspan baseline-shift="{sh}" font-size="68%">{E(m.group(2))}</tspan>'
        i = m.end()
    return out + E(s[i:])


def plain_len(s):
    sup = sum(len(m) for m in _re.findall(r'[\^_]\{([^}]*)\}', s))
    base = len(_re.sub(r'[\^_]\{[^}]*\}', '', s))
    return base + 0.7 * sup


def rtxt(x, y, s, size=16, fill=INK, w=800, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" {F} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{R(s)}</text>'


def rtag(x, y, s, c, size=14, anchor='middle', bg=W):
    w = plain_len(s) * size * 0.58 + 18
    x0 = x - w / 2 if anchor == 'middle' else (x - w if anchor == 'end' else x)
    return (f'<rect x="{x0:.1f}" y="{y - size - 5:.1f}" width="{w:.1f}" height="{size + 13}" rx="{(size + 13) / 2}" fill="{bg}" stroke="{c}" stroke-width="2"/>'
            + rtxt(x0 + w / 2, y + 1, s, size, c))


def sax(p, xt=(), yt=(), xl='', yl='', fmt=g, xfmt=None, grid_=True, yaxis=True):
    """axes: grid lines and labels for yt, a zero line with ticks, x labels under the plot"""
    o = ''
    for v in yt:
        if grid_ and v != 0: o += line(p.L, p.Y(v), p.L + p.W, p.Y(v), GRID, 1.5)
        o += txt(p.L - 10, p.Y(v) + 5, fmt(v), 13, MUT, 700, 'end')
    y0 = p.Y(0) if p.y0 <= 0 <= p.y1 else p.T + p.H
    o += line(p.L, y0, p.L + p.W + 10, y0, MUT, 2.5, arrow=True)
    if yaxis: o += line(p.L, p.T + p.H + 2, p.L, p.T - 8, MUT, 2.5, arrow=True)
    for v in xt:
        o += line(p.X(v), y0 - 5, p.X(v), y0 + 5, MUT, 2)
        o += txt(p.X(v), p.T + p.H + 22, (xfmt or fmt)(v), 13, MUT, 700)
    if xl: o += txt(p.L + p.W + 10, p.T + p.H + 44, xl, 13, MUT, 700, 'end')
    if yl: o += txt(p.L + 8, p.T - 10, yl, 13, MUT, 700, 'start')
    return o


def stems(xs, vals, yb, k, c=B, r=7, labels=False, size=12, lc=INK, fmt=g):
    o = ''
    for x, v in zip(xs, vals):
        y = yb - k * v
        o += line(x, yb, x, y, c, 4) + f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{c}"/>'
        if labels: o += txt(x, y - 12 if v >= 0 else y + 22, fmt(v), size, lc, 800)
    return o


def cross(x, y, c=O, r=10, w=5):
    return line(x - r, y - r, x + r, y + r, c, w) + line(x - r, y + r, x + r, y - r, c, w)


def area(p, f, a, b, c, n=80, op=.35, base=0):
    pts = [p.P(a, base)] + [p.P(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)] + [p.P(b, base)]
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{c}" fill-opacity="{op}" stroke="none"/>'


def pts_curve(pts, c=B, w=4, dash=None):
    return poly(pts, c, w, dash)


def arrow2(x1, y1, x2, y2, c=INK, w=2.5):
    """double-headed dimension arrow"""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{w}" '
            f'marker-start="url(#a{mk(c)})" marker-end="url(#a{mk(c)})"/>')


def sinc(x):
    return 1.0 if abs(x) < 1e-12 else math.sin(math.pi * x) / (math.pi * x)


def Qf(x):
    return 0.5 * math.erfc(x / math.sqrt(2))


def db(x):
    return 10 * math.log10(x)


def sci(v, d=2):
    """3.87×10^{-6} style (use with rtxt / rtag)"""
    e = math.floor(math.log10(abs(v)))
    m = v / 10 ** e
    return f'{m:.{d}f}×10^{{{"−" if e < 0 else ""}{abs(e)}}}'
