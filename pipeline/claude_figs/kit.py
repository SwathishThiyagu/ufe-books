"""Drawing helpers shared by the hand-drawn figure files (same helpers as c_dl_u2.py, plus a few).
Import from a unit file with:  import os, sys; sys.path.insert(0, os.path.dirname(__file__)); from kit import *
Colours are only the shell's CSS variables; arrowheads are url(#ar-UID-n|m|l|x) (accent, line2, live, next)."""

INK, MUT, AC, LV, NX, L2, LN = 'var(--ink)', 'var(--muted)', 'var(--accent)', 'var(--live)', 'var(--next)', 'var(--line2)', 'var(--line)'
PANEL, ACS, LVS, NXS, FIGBG = 'var(--panel)', 'var(--accent-soft)', 'var(--live-soft)', 'var(--next-soft)', 'var(--fig)'


def T(x, y, s, size=14, anchor='middle', fill=INK, bold=False, italic=False):
    w = ' font-weight="700"' if bold else ''
    it = ' font-style="italic"' if italic else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" style="fill:{fill}"{w}{it}>{s}</text>'


def tw(s, size=14):
    """rough text width"""
    import re
    s = re.sub(r'&[#\w]+;', 'x', re.sub(r'<[^>]+>', '', s))
    return len(s) * size * 0.56


def Tb(x, y, s, size=14, anchor='middle', fill=INK, bold=False):
    """text on a small background patch so lines behind it do not cut it"""
    w = tw(s, size) + 10
    x0 = x - w / 2 if anchor == 'middle' else (x - 5 if anchor == 'start' else x - w + 5)
    return f'<rect x="{x0:.1f}" y="{y - size * 0.95:.1f}" width="{w:.1f}" height="{size * 1.35:.1f}" rx="4" style="fill:var(--fig)"/>' + T(x, y, s, size, anchor, fill, bold)


def L(x1, y1, x2, y2, c=AC, w=2, dash=None, arrow=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    m = f' marker-end="url(#ar-UID-{arrow})"' if arrow else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" style="stroke:{c};stroke-width:{w}{d}"{m}/>'


def P(pts, c=AC, w=2.5, dash=None, fill='none', op=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    o = f';fill-opacity:{op}' if op is not None else ''
    return f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{c};stroke-width:{w}{d}{o};stroke-linejoin:round"/>'


def C(x, y, r=5, c=AC, fill=None):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{fill or c};stroke:var(--fig);stroke-width:2"/>'


def R(x, y, w, h, fill=PANEL, stroke=AC, rx=8, sw=2, dash=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}{d}"/>'


def boxt(x, y, w, h, lines, fill=PANEL, stroke=AC, size=14, bold_first=False, rx=8, dash=None, fills=None):
    out = [R(x, y, w, h, fill, stroke, rx, dash=dash)]
    lh = size * 1.3
    y0 = y + h / 2 - (len(lines) - 1) * lh / 2 + size * 0.35
    for i, s in enumerate(lines):
        out.append(T(x + w / 2, y0 + i * lh, s, size, bold=(bold_first and i == 0), fill=(fills[i] if fills else INK)))
    return ''.join(out)


def brace(x1, x2, y, c=INK, up=False, tick=7):
    """a flat bracket from x1 to x2 at height y with end ticks (pointing down unless up)"""
    t = -tick if up else tick
    return P([(x1, y + t), (x1, y), (x2, y), (x2, y + t)], c, 1.8)


def axes(x0, x1, y0, y1, xt, yt, fx, fy, xlab, ylab, xfmt=str, yfmt=str):
    o = [L(x0, y1, x1, y1, L2, 1.5), L(x0, y0, x0, y1, L2, 1.5)]
    for v in xt:
        X = fx(v); o += [L(X, y1, X, y1 + 5, L2, 1.5), T(X, y1 + 20, xfmt(v), 13, fill=MUT)]
    for v in yt:
        Y = fy(v); o += [L(x0 - 5, Y, x0, Y, L2, 1.5), L(x0, Y, x1, Y, 'var(--line)', 1), T(x0 - 9, Y + 4.5, yfmt(v), 13, 'end', MUT)]
    o.append(T((x0 + x1) / 2, y1 + 40, xlab, 14, fill=MUT))
    o.append(T(x0, y0 - 12, ylab, 14, 'start', MUT))
    return ''.join(o)


def xaxis(x0, x1, y, ticks, fx, lab=None, fmt=str):
    o = [L(x0, y, x1, y, L2, 1.5)]
    for v in ticks:
        X = fx(v); o += [L(X, y, X, y + 5, L2, 1.5), T(X, y + 20, fmt(v), 13, fill=MUT)]
    if lab: o.append(T((x0 + x1) / 2, y + 42, lab, 14, fill=MUT))
    return ''.join(o)


def neg(v):
    return str(v).replace('-', '&#8722;')


def make_spec(FIG):
    def spec(k):
        fn, cap, aria = FIG[k]
        h, body = fn()
        return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    return spec
