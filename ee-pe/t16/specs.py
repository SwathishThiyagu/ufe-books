"""t16 split blueprint thumbnails for Power Electronics (ee-pe), EEE look.
One spec per lesson, each built from a worked example in that lesson's own chapters of the library unit book
(books/eee/ee-pe/ee-pe-u<N>.html). Every number is computed here and matches the book's answer.
Build: python3 t16_split.py build specs.py <out dir>   (run from the t16_split tool folder)."""
import math, os, sys
for _d in (os.environ.get('T16_TOOL', ''), os.path.dirname(os.path.abspath(sys.argv[0])), os.path.dirname(os.path.abspath(__file__))):
    if _d and os.path.exists(os.path.join(_d, 't16_split.py')):
        sys.path.insert(0, _d)
        break
import t16_split as T
B = T.B

GO, CY = T.DEPTS['eee']['acc'], T.DEPTS['eee']['acc2']
CU = '#C98A4B'
WH = '#F1F4F7'
INK = '#0B1520'
pi, sq2, sq3 = math.pi, math.sqrt(2), math.sqrt(3)
rad, deg = math.radians, math.degrees
SUBJECT = 'POWER ELECTRONICS'


def f(v, n=2):
    """fixed decimals with a real minus sign"""
    return f'{v:.{n}f}'.replace('-', '−')


def g(v):
    return f'{v:g}'.replace('-', '−')


def S(text, cls):
    return f'<span class="{cls}">{text}</span>'


# ================================================================ isometric board pieces (board units, slab 8 x 8)
# the board: a 6.6 x 6.6 slab at 40 px per unit; lessons place parts in frame coordinates, shifted by (DX, DY)
UNIT, ORIGIN, SLAB, DX, DY = 40, (980, 300), 6.6, 2.0, .6


def setup():
    B.U, (B.OX, B.OY) = UNIT, ORIGIN


def P(x, y, z=0):
    return B.P(x - DX, y - DY, z)


setup()


def pts(*p):
    return B.pts(*p)


def box(x, y, w, d, h, top, left, right, z0=0):
    return B.box(x - DX, y - DY, w, d, h, top, left, right, z0)


def lab(x, y, z, text, col=WH, size=15, dy=0, dx=0, anchor='middle'):
    px, py = P(x, y, z)
    return (f'<text x="{px + dx:.1f}" y="{py + dy:.1f}" text-anchor="{anchor}" fill="{col}" stroke="{INK}" stroke-width="4" '
            f'paint-order="stroke" style="font:700 {size}px \'IBM Plex Sans\'">{text}</text>')


def trace(path, col=CU, w=3.5, z=.01):
    return (f'<polyline points="{pts(*[P(a, b, z) for a, b in path])}" fill="none" stroke="{col}" stroke-width="{w}" '
            'stroke-linejoin="round" stroke-linecap="round" opacity=".95"/>')


def flow(path, col=CY, w=4.5, z=.03, arrows=True):
    pl = [P(a, b, z) for a, b in path]
    o = (f'<g filter="url(#gl)"><polyline points="{pts(*pl)}" fill="none" stroke="{col}" stroke-width="{w}" '
         'stroke-linejoin="round" stroke-linecap="round"/></g>')
    if arrows:
        for (x1, y1), (x2, y2) in zip(pl, pl[1:]):
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            L = math.hypot(x2 - x1, y2 - y1)
            if L < 40:
                continue
            ux, uy = (x2 - x1) / L, (y2 - y1) / L
            o += T.arrow(mx - ux * 8, my - uy * 8, mx + ux * 10, my + uy * 10, col, 3)
    return o


def pad(x, y):
    px, py = P(x, y)
    return f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="5" ry="3" fill="#1A222A" stroke="{CU}" stroke-width="2"/>'


def dev(cx, cy, name, glow=None, w=1.2):
    """a switching device (SCR, IGBT, MOSFET, TRIAC): a dark power package with a metal tab and its name on top"""
    x, y = cx - w / 2, cy - w / 2
    o = box(x - .05, y - .25, w + .1, .25, .12, '#B9C3CC', '#7E8994', '#98A3AE')
    o += box(x, y, w, w, .55, '#2F3A45', '#151B21', '#1F262E')
    if glow:
        a, b, c, d = P(x, y, .56), P(x + w, y, .56), P(x + w, y + w, .56), P(x, y + w, .56)
        o += f'<polygon points="{pts(a, b, c, d)}" fill="none" stroke="{glow}" stroke-width="2.5" filter="url(#gl)"/>'
    if name:
        o += lab(cx, cy, .56, name, WH if not glow else glow, 18 if len(name) < 5 else 16, dy=6)
    return o


def diode(cx, cy, name='D', along='x', col=WH):
    """a small diode: black body, silver cathode band"""
    if along == 'x':
        o = box(cx - .6, cy - .36, 1.2, .72, .42, '#2A323A', '#12171C', '#1B2127')
        o += box(cx + .3, cy - .36, .18, .72, .43, '#D3DAE0', '#8B959F', '#A8B2BC')
    else:
        o = box(cx - .36, cy - .6, .72, 1.2, .42, '#2A323A', '#12171C', '#1B2127')
        o += box(cx - .36, cy + .3, .72, .18, .43, '#D3DAE0', '#8B959F', '#A8B2BC')
    return o + lab(cx, cy, .44, name, col, 16, dy=-12)


def res(cx, cy, name, along='x', col=WH, L=2.0):
    """a ceramic power resistor with colour bands"""
    if along == 'x':
        o = box(cx - L / 2, cy - .36, L, .72, .62, '#DCCBA2', '#9E8C63', '#BCA97E')
        for k, c in enumerate(('#8A4B2A', '#1D1D1D', '#C8901E')):
            o += box(cx - L / 2 + .4 + k * .36, cy - .37, .13, .74, .63, c, c, c)
    else:
        o = box(cx - .36, cy - L / 2, .72, L, .62, '#DCCBA2', '#9E8C63', '#BCA97E')
        for k, c in enumerate(('#8A4B2A', '#1D1D1D', '#C8901E')):
            o += box(cx - .37, cy - L / 2 + .4 + k * .36, .74, .13, .63, c, c, c)
    return o + lab(cx, cy, .62, name, col, 17, dy=-14)


def cyl_at(cx, cy, rx, ry, h, body, top, z=0):
    px, py = P(cx, cy, z)
    return T.cyl(px, py, rx, ry, h, body, top)


def capcan(cx, cy, name, h=84, col=WH, r=28):
    px, py = P(cx, cy)
    o = f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{r + 8}" ry="{r * .55 + 4:.1f}" fill="#000" opacity=".35"/>'
    o += T.cyl(px, py, r, r * .55, h, '#35506D', '#C9D3DC')
    o += (f'<path d="M{px - r:.1f},{py - h + 9:.1f} A{r},{r * .55:.1f} 0 0 0 {px + r:.1f},{py - h + 9:.1f}" fill="none" stroke="#9FB2C6" stroke-width="2" opacity=".6"/>'
          f'<path d="M{px - 9:.1f},{py - h:.1f}H{px + 9:.1f}M{px:.1f},{py - h - 5:.1f}V{py - h + 5:.1f}" stroke="#6B7785" stroke-width="2"/>')
    o += (f'<text x="{px:.1f}" y="{py - h - r * .55 - 8:.1f}" text-anchor="middle" fill="{col}" stroke="{INK}" stroke-width="4" paint-order="stroke" '
          f'style="font:700 17px \'IBM Plex Sans\'">{name}</text>')
    return o


def toroid(cx, cy, name, col=WH, rx=50, z=.35, n=46):
    tx, ty = P(cx, cy, z)
    ry = rx * .56
    o = f'<ellipse cx="{tx:.1f}" cy="{ty + 8:.1f}" rx="{rx}" ry="{ry:.1f}" fill="#5A3414"/><ellipse cx="{tx:.1f}" cy="{ty:.1f}" rx="{rx}" ry="{ry:.1f}" fill="#B8692C"/>'
    o += '<g stroke="#E8A464" stroke-width="2.4" stroke-linecap="round">' + ''.join(
        f'<line x1="{tx + rx * .4 * math.cos(a):.1f}" y1="{ty + ry * .4 * math.sin(a):.1f}" x2="{tx + (rx - 1) * math.cos(a):.1f}" y2="{ty + (ry - 1) * math.sin(a):.1f}"/>'
        for a in [k * 2 * pi / n for k in range(n)]) + '</g>'
    o += f'<ellipse cx="{tx:.1f}" cy="{ty:.1f}" rx="{rx * .36:.1f}" ry="{ry * .36:.1f}" fill="#1A222A"/>'
    o += (f'<text x="{tx:.1f}" y="{ty - ry - 8:.1f}" text-anchor="middle" fill="{col}" stroke="{INK}" stroke-width="4" paint-order="stroke" '
          f'style="font:700 17px \'IBM Plex Sans\'">{name}</text>')
    return o


def dcsrc(cx, cy, name, w=2.0, d=1.5, h=1.0, col='#F6D285'):
    o = box(cx - w / 2, cy - d / 2, w, d, h, '#3A4A5C', '#1C2530', '#26313D')
    o += cyl_at(cx - w / 2 + .35, cy - d / 2 + .3, 7, 4, 9, '#8E1E1E', '#E04848', h)
    o += cyl_at(cx + w / 2 - .3, cy - d / 2 + .3, 7, 4, 9, '#151515', '#4A4A4A', h)
    return o + lab(cx, cy + .15, h, name, col, 18, dy=6)


def battery(cx, cy, name, w=2.1, d=1.5, h=1.2):
    o = box(cx - w / 2, cy - d / 2, w, d, h, '#F1C64E', '#9C7418', '#C0922A')
    o += cyl_at(cx - w / 2 + .35, cy - d / 2 + .3, 7, 4, 9, '#8E1E1E', '#E04848', h)
    o += cyl_at(cx + w / 2 - .3, cy - d / 2 + .3, 7, 4, 9, '#151515', '#4A4A4A', h)
    px, py = P(cx, cy + .2, h)
    return o + f'<text x="{px:.1f}" y="{py + 5:.1f}" text-anchor="middle" fill="#1A1D20" style="font:700 18px \'IBM Plex Sans\'">{name}</text>'


def acsrc(cx, cy, name, col='#F6D285', h=58, r=38):
    px, py = P(cx, cy)
    o = f'<ellipse cx="{px:.1f}" cy="{py + 2:.1f}" rx="{r + 6}" ry="{r * .55 + 3:.1f}" fill="#000" opacity=".35"/>'
    o += T.cyl(px, py, r, r * .55, h, '#24405E', '#4D7398')
    wv = ' '.join(f'{px - 20 + k:.1f},{py - h - 6 * math.sin(k / 40 * 2 * pi):.1f}' for k in range(41))
    o += f'<polyline points="{wv}" fill="none" stroke="{CY}" stroke-width="3" stroke-linecap="round"/>'
    o += (f'<text x="{px:.1f}" y="{py - h - r * .55 - 9:.1f}" text-anchor="middle" fill="{col}" stroke="{INK}" stroke-width="4" paint-order="stroke" '
          f'style="font:700 17px \'IBM Plex Sans\'">{name}</text>')
    return o


def lamp(cx, cy, name, col=WH, bright=1.0):
    px, py = P(cx, cy)
    o = T.cyl(px, py, 14, 8, 24, '#8C98A6', '#C9D2DA')
    o += f'<circle cx="{px:.1f}" cy="{py - 50:.1f}" r="34" fill="{GO}" opacity="{.25 * bright:.2f}" filter="url(#gl)"/>'
    o += f'<circle cx="{px:.1f}" cy="{py - 50:.1f}" r="26" fill="#FFE7A0" opacity="{.55 + .4 * bright:.2f}"/>'
    o += f'<path d="M{px - 8:.1f},{py - 32:.1f} l4,-18 l4,10 l4,-10 l4,18" fill="none" stroke="#B07A12" stroke-width="2.2"/>'
    o += (f'<text x="{px:.1f}" y="{py - 88:.1f}" text-anchor="middle" fill="{col}" stroke="{INK}" stroke-width="4" paint-order="stroke" '
          f'style="font:700 17px \'IBM Plex Sans\'">{name}</text>')
    return o


def machine(cx, cy, letter, name, col=WH, r=36, h=54):
    px, py = P(cx, cy)
    o = f'<ellipse cx="{px:.1f}" cy="{py + 2:.1f}" rx="{r + 6}" ry="{r * .55 + 3:.1f}" fill="#000" opacity=".35"/>'
    o += T.cyl(px, py, r, r * .55, h, '#4F5C69', '#9AA6B2')
    o += f'<circle cx="{px:.1f}" cy="{py - h:.1f}" r="6" fill="#2B333B"/>'
    o += f'<text x="{px:.1f}" y="{py - 16:.1f}" text-anchor="middle" fill="#E6ECF1" style="font:700 24px \'IBM Plex Sans\'">{letter}</text>'
    o += (f'<text x="{px:.1f}" y="{py - h - r * .55 - 10:.1f}" text-anchor="middle" fill="{col}" stroke="{INK}" stroke-width="4" paint-order="stroke" '
          f'style="font:700 17px \'IBM Plex Sans\'">{name}</text>')
    return o


def bigarrow(a, b, c, d, col, z=.6, w=7):
    (x0, y0), (x1, y1) = P(a, b, z), P(c, d, z)
    return f'<g filter="url(#gl)">{T.arrow(x0, y0, x1, y1, col, w)}</g>'


def board(parts):
    return T.iso_board('eee', parts, top='#1E2B39', left='#0C131A', right='#131C26', X=SLAB, Y=SLAB, origin=ORIGIN, unit=UNIT)


# ================================================================ card pieces (470 x 144 SVG)
AX = '#6B7B8A'


def svg(inner):
    return f'<svg width="470" height="144" viewBox="0 0 470 144">{inner}</svg>'


def ttl(x, text, col):
    return f'<text x="{x}" y="18" text-anchor="middle" class="pt" fill="{col}">{text}</text>'


def ax(x, y, text, anchor='middle', col=None):
    fill = f' fill="{col}"' if col else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="ax"{fill}>{text}</text>'


def line(x1, y1, x2, y2, col=AX, w=1.5, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}"{da}/>'


def curve(xy, col, w=3.2, fill=None, base=None, op=.16):
    s = ' '.join(f'{a:.1f},{b:.1f}' for a, b in xy)
    o = ''
    if fill and base is not None:
        o += f'<polygon points="{xy[0][0]:.1f},{base:.1f} {s} {xy[-1][0]:.1f},{base:.1f}" fill="{fill}" opacity="{op}"/>'
    return o + f'<polyline points="{s}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"/>'


def plot(x0, x1, y0, y1, fn, a, b, lo, hi, n=240):
    """sample fn on [a, b] into the box x0..x1, y1 (bottom)..y0 (top) with value range lo..hi; None breaks the line"""
    segs, cur = [], []
    for k in range(n + 1):
        t = a + (b - a) * k / n
        v = fn(t)
        if v is None:
            if cur:
                segs.append(cur); cur = []
            continue
        cur.append((x0 + (x1 - x0) * k / n, y1 - (v - lo) / (hi - lo) * (y1 - y0)))
    if cur:
        segs.append(cur)
    return segs


def hbars(x0, y0, rows, vmax, wmax, h=20, gap=10, unit='', lw=92):
    """horizontal bars: rows of (label, value, colour, text)"""
    o = ''
    for k, (lbl, v, col, txt) in enumerate(rows):
        y = y0 + k * (h + gap)
        w = max(2, v / vmax * wmax)
        o += ax(x0 + lw - 8, y + h / 2 + 5, lbl, 'end')
        o += f'<rect x="{x0 + lw}" y="{y}" width="{w:.1f}" height="{h}" rx="4" fill="{col}" opacity=".85"/>'
        o += f'<text x="{x0 + lw + w + 6:.1f}" y="{y + h / 2 + 6:.1f}" class="pt" fill="{col}">{txt}</text>'
    return o


def vbars(x0, base, rows, vmax, hmax, bw=44, gap=26):
    """vertical bars: rows of (label, value, colour, text on top)"""
    o = line(x0 - 6, base, x0 + len(rows) * (bw + gap) - gap + 6, base)
    for k, (lbl, v, col, txt) in enumerate(rows):
        x = x0 + k * (bw + gap)
        hh = max(2, v / vmax * hmax)
        o += f'<rect x="{x}" y="{base - hh:.1f}" width="{bw}" height="{hh:.1f}" rx="4" fill="{col}" opacity=".85"/>'
        o += f'<text x="{x + bw / 2}" y="{base - hh - 6:.1f}" text-anchor="middle" class="pt" fill="{col}">{txt}</text>'
        o += ax(x + bw / 2, base + 16, lbl)
    return o


def chip(side, top, kind, text, pointer=True):
    return dict(side=side, top=top, kind=kind, text=text, pointer=pointer)


def spec(key, title, question, takeaway, card_title, card, parts, chips, summary, css=''):
    setup()
    return dict(key=key, subject=SUBJECT, title=title, question=question, takeaway=takeaway, tag='Book example',
                card_title=card_title, card=card, board=board(parts), chips=chips, summary=summary,
                page_title=f'{title.replace("<br>", " ")}: Power Electronics', css=css)


SMALL = 'h1{font-size:66px !important}'


# ---------------------------------------------------------------- more board helpers
def cable(a, b, z0, c, d, z1, col='#9AA4AE', w=4, lift=1.2):
    (x0, y0), (x1, y1) = P(a, b, z0), P(c, d, z1)
    mx, my = P((a + c) / 2, (b + d) / 2, max(z0, z1) + lift)
    return f'<path d="M{x0:.1f},{y0:.1f} Q{mx:.1f},{my:.1f} {x1:.1f},{y1:.1f}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'


def block(cx, cy, w, d, h, name, top='#3A4652', left='#222B33', right='#2C3640', col=WH, size=16, sub=None):
    o = box(cx - w / 2, cy - d / 2, w, d, h, top, left, right)
    o += lab(cx, cy, h, name, col, size, dy=6 if not sub else -2)
    if sub:
        o += lab(cx, cy, h, sub, '#C9D3DB', 13, dy=14)
    return o


def legs(xs, ytop, ybot, names, glow=None, w=1.25):
    """converter legs along y: a device at each end, rails joining the tops and the bottoms"""
    o = trace([(xs[0], ytop), (xs[-1], ytop)]) + trace([(xs[0], ybot), (xs[-1], ybot)])
    for x in xs:
        o += trace([(x, ytop), (x, ybot)])
    devs = []
    for k, x in enumerate(xs):
        devs.append(dev(x, ytop + .2, names[2 * k], glow[2 * k] if glow else None, w))
        devs.append(dev(x, ybot - .2, names[2 * k + 1], glow[2 * k + 1] if glow else None, w))
    return o, devs


def house(cx, cy, name):
    o = box(cx - .9, cy - .8, 1.8, 1.6, 1.1, '#D9E1E8', '#8C98A6', '#AAB5C0')
    a, b, c2, d = P(cx - .95, cy - .85, 1.1), P(cx + .95, cy - .85, 1.1), P(cx + .95, cy + .85, 1.1), P(cx - .95, cy + .85, 1.1)
    ra, rb = P(cx, cy - .85, 2.0), P(cx, cy + .85, 2.0)
    o += f'<polygon points="{pts(b, c2, rb, ra)}" fill="#B8692C"/><polygon points="{pts(d, c2, rb)}" fill="#7A3E14"/>'
    dx, dy_ = P(cx - .2, cy + .8, .0)
    o += box(cx - .25, cy + .8, .5, .02, .6, '#5A3414', '#5A3414', '#5A3414')
    return o + lab(cx, cy, 2.0, name, WH, 16, dy=-12)


def panel(x, y, w=1.15, d=1.0):
    """a solar panel tilted up towards the back"""
    a, b, c, e = P(x, y, .9), P(x + w, y, .9), P(x + w, y + d, .25), P(x, y + d, .25)
    o = f'<polygon points="{pts(a, b, c, e)}" fill="#1D4E89" stroke="#C9D3DC" stroke-width="2"/>'
    for k in range(1, 4):
        p1, p2 = P(x + w * k / 4, y, .9), P(x + w * k / 4, y + d, .25)
        o += f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="#7FB2E5" stroke-width="1"/>'
    for k in range(1, 3):
        p1, p2 = P(x, y + d * k / 3, .9 - .65 * k / 3), P(x + w, y + d * k / 3, .9 - .65 * k / 3)
        o += f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="#7FB2E5" stroke-width="1"/>'
    m1, m2 = P(x + w / 2, y + d - .1, 0), P(x + w / 2, y + d - .1, .3)
    return f'<line x1="{m1[0]:.1f}" y1="{m1[1]:.1f}" x2="{m2[0]:.1f}" y2="{m2[1]:.1f}" stroke="#8C98A6" stroke-width="3"/>' + o


def tower(cx, cy, h=2.4):
    o = ''
    for dx in (-.25, .25):
        a, b = P(cx + dx, cy, 0), P(cx, cy, h)
        o += f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#AAB5C0" stroke-width="2.5"/>'
    a, b = P(cx - .55, cy, h - .5), P(cx + .55, cy, h - .5)
    return o + f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#AAB5C0" stroke-width="3"/>'


def wave2(x0, w, title, col, fn, lo, hi, a=0, b=2 * pi, n=360, zero=True, fillop=.18):
    xa, xb, y0, y1 = x0 + 42, x0 + w, 30, 122
    Yz = y1 - (0 - lo) / (hi - lo) * (y1 - y0)
    o = ttl(x0 + w / 2 + 12, title, col) + line(xa, y0, xa, y1)
    if zero:
        o += line(xa, Yz, xb, Yz)
    for seg in plot(xa, xb, y0, y1, fn, a, b, lo, hi, n):
        o += curve(seg, col, fill=col, base=Yz, op=fillop)
    return o, (xa, xb, y0, y1, Yz)


# ================================================================ the lessons
HOOK = {
    'ee-pe-u1-L1': 'Does removing the gate turn off an SCR?',
    'ee-pe-u1-L2': 'Does a DIAC carry the lamp current?',
    'ee-pe-u1-L3': 'Does a snubber cut the total loss?',
    'ee-pe-u2-L1': 'Is half-wave DC really 0.637 Vm?',
    'ee-pe-u2-L2': 'Does cos α work for a resistive load?',
    'ee-pe-u2-L3': 'Where is α measured in three phase?',
    'ee-pe-u2-L4': 'Does DC current reverse in inversion?',
    'ee-pe-u2-L5': 'Does a big capacitor fix power factor?',
    'ee-pe-u3-L1': 'Is duty ratio on-time or off-time?',
    'ee-pe-u3-L2': 'Which gain formula fits a boost?',
    'ee-pe-u3-L3': 'Is flyback output just Vs·D·N2/N1?',
    'ee-pe-u3-L4': 'Size the inductor from average current?',
    'ee-pe-u4-L1': 'Is the fundamental peak just Vdc?',
    'ee-pe-u4-L2': 'How far can SVM push the voltage?',
    'ee-pe-u4-L3': 'What does each NPC switch block?',
    'ee-pe-u5-L1': 'Does a + gate pulse always mean Q1?',
    'ee-pe-u5-L2': 'Is chopper rms output just D·Vs?',
    'ee-pe-u5-L3': 'Can two matrix switches feed one output?',
    'ee-pe-u6-L1': 'How long does a UPS battery really last?',
    'ee-pe-u6-L2': 'What current flows in a ±500 kV link?',
    'ee-pe-u6-L3': 'How big must a home battery be?',
}
SUBX = '<tspan baseline-shift="sub" font-size="70%">{}</tspan>'


def sb(t):
    return SUBX.format(t)


def bridge_parts(names, src, right_load, front_load, glow=None, xl=4.6, xr=6.6, yt=1.4, yb=3.6, w=1.0, cable_src=True):
    """a single-phase bridge: legs at xl and xr between the + rail (yt) and the - rail (yb); the AC side (src, at the left
    of the bridge) feeds the two leg midpoints; the DC side runs from the + rail round the right edge (right_load) and the
    front edge (front_load) back to the - rail"""
    ym = (yt + yb) / 2
    o = [trace([(xl, yt), (xr, yt)]), trace([(xl, yb), (xr, yb)]), trace([(xl, yt), (xl, yb)]), trace([(xr, yt), (xr, yb)]),
         trace([(xr, yt), (7.6, yt), (7.6, 5.6), (3.6, 5.6), (3.6, yb), (xl, yb)]),
         flow([(xr + .3, yt), (7.6, yt), (7.6, 5.6), (3.6, 5.6), (3.6, yb), (xl - .3, yb)])]
    if cable_src:
        o += [trace([(3.0, ym), (xl, ym)])]
    o += [dev(xl, yt + .05, names[0], glow, w), dev(xr, yt + .05, names[2], glow, w), src]
    if cable_src:
        o += [cable(3.0, ym - .3, .5, xr, ym, .05, '#9AA4AE', 4, 1.0)]
    return o + [dev(xl, yb - .05, names[1], glow, w), dev(xr, yb - .05, names[3], glow, w)] + right_load + front_load


# ---------------------------------------------------------------- 1.2, worked example 2: SCR latching, minimum gate pulse
def u1L1():
    k = 'ee-pe-u1-L1'
    V, R, L, IL = 100, 20, .5, .05
    tau = L / R                                   # 0.025 s
    tmin = -tau * math.log(1 - IL * R / V)        # 251 us
    i = lambda t: V / R * (1 - math.exp(-t / tau))
    i10 = i(10e-6)                                # 2.0 mA when a 10 us pulse ends
    assert round(tmin * 1e6) == 251
    x0, x1, y0, y1 = 64, 448, 34, 112
    X = lambda t: x0 + (x1 - x0) * t / 500e-6
    Y = lambda a: y1 - a / .1 * (y1 - y0)
    c = line(x0, y0 - 4, x0, y1) + line(x0, y1, x1, y1)
    c += line(x0, Y(IL), x1, Y(IL), GO, 1.5, '5 5') + ax(x0 - 6, Y(IL) + 5, 'I' + sb('L'), 'end', GO)
    c += ax(x0 - 6, y1 + 5, '0', 'end') + ax(x0 - 6, Y(.1) + 5, '100 mA', 'end')
    for seg in plot(x0, x1, y0, y1, lambda t: i(t), 0, 500e-6, 0, .1):
        c += curve(seg, CY, fill=CY, base=y1, op=.10)
    c += f'<circle cx="{X(tmin):.1f}" cy="{Y(IL):.1f}" r="6" fill="{GO}"/>' + line(X(tmin), Y(IL), X(tmin), y1, GO, 1.5, '4 4')
    c += f'<text x="{X(tmin) + 12:.1f}" y="{Y(IL) + 22:.1f}" class="pt" fill="{GO}">{tmin * 1e6:.0f} µs: I{sb("L")} reached</text>'
    c += f'<circle cx="{X(10e-6):.1f}" cy="{Y(i10):.1f}" r="5" fill="{CY}"/>'
    c += line(X(10e-6), Y(i10), X(10e-6) + 14, Y(IL) - 16, CY, 1.2) + f'<text x="{X(10e-6) + 18:.1f}" y="{Y(IL) - 14:.1f}" class="pt" fill="{CY}">10 µs: only {i10 * 1e3:.1f} mA</text>'
    for t in (0, 100, 200, 300, 400, 500):
        c += ax(X(t * 1e-6), 132, f'{t}')
    c += f'<text x="240" y="16" text-anchor="middle" class="pt" fill="{WH}">anode current after the gate fires</text>' + ax(x1, 100, 't, µs', 'end')
    parts = [trace([(3.4, 1.4), (7.6, 1.4), (7.6, 5.6), (3.4, 5.6), (3.4, 1.4)]),
             trace([(6.2, 1.4), (6.2, .5), (7.0, .5)], GO, 2.5),
             flow([(5.3, 1.4), (7.6, 1.4), (7.6, 5.6), (3.4, 5.6), (3.4, 1.4), (3.7, 1.4)]),
             box(6.9, .15, 1.0, .7, .5, '#3A4652', '#222B33', '#2C3640'),
             lab(7.4, .5, .5, '⎍ gate', GO, 15, dy=6),
             dcsrc(4.4, 1.4, f'{V} V'),
             dev(6.2, 1.4, 'SCR', GO, 1.3),
             toroid(7.6, 3.5, f'{g(L)} H'),
             res(5.5, 5.6, f'{R} Ω', 'x', WH, 1.8)]
    return spec(k, 'Power Diodes<br>&amp; Thyristors', HOOK[k],
                f'Hold the gate till i passes {S("I<sub>L</sub>", "gold")} —<br>then the SCR stays {S("ON", "cyan")} alone',
                'SCR on 100 V, 20 Ω, 0.5 H', svg(c), parts,
                [chip('left', 300, 'c', f'{V} V DC supply'), chip('left', 364, 'c', f'R = {R} Ω, L = {g(L)} H'),
                 chip('left', 428, 'g', f'I<sub>L</sub> = {IL * 1e3:.0f} mA'),
                 chip('right', 290, 'g', f'gate ≥ {tmin * 1e6:.0f} µs'), chip('right', 538, 'c', '10 µs pulse: drops out', False)],
                f'τ = L/R = {g(L)} ÷ {R} = <b class="cl">{tau * 1e3:g} ms</b>; {IL} = {g(V / R)}(1 − e<sup>−t/τ</sup>)<br>'
                f't = −{tau} × ln {1 - IL * R / V:g} = <b class="gl">{tmin * 1e6:.0f} µs</b> minimum gate pulse')


# ---------------------------------------------------------------- 1.5, worked example: TRIAC dimmer at 90 degrees
def u1L2():
    k = 'ee-pe-u1-L2'
    Vs, a, R = 230, rad(90), 100
    Vr = Vs * math.sqrt(1 - a / pi + math.sin(2 * a) / (2 * pi))     # 162.6 V
    Pw, Pf = Vr ** 2 / R, Vs ** 2 / R                                  # 264.5 W, 529 W
    assert f(Vr, 1) == '162.6' and f(Pw, 1) == '264.5'
    Vm = Vs * sq2
    x0, x1, y0, y1 = 40, 250, 30, 126
    mid = (y0 + y1) / 2
    c = line(x0, y0, x0, y1) + line(x0, mid, x1, mid)
    for seg in plot(x0, x1, y0, y1, lambda t: Vm * math.sin(t), 0, 2 * pi, -Vm, Vm):
        c += f'<polyline points="{" ".join(f"{p:.1f},{q:.1f}" for p, q in seg)}" fill="none" stroke="{AX}" stroke-width="1.5" stroke-dasharray="4 4"/>'
    for seg in plot(x0, x1, y0, y1, lambda t: Vm * math.sin(t) if (t % pi) >= a else 0, 0, 2 * pi, -Vm, Vm, 480):
        c += curve(seg, GO, fill=GO, base=mid, op=.2)
    for t, s_ in ((pi / 2, '90°'), (3 * pi / 2, '270°')):
        c += ax(x0 + (x1 - x0) * t / (2 * pi), y1 + 14, s_, col=GO)
    c += ttl(150, 'lamp voltage, fired at 90°', GO)
    c += vbars(312, 122, [('α = 0°', Pf, AX, f'{Pf:.0f} W'), ('α = 90°', Pw, CY, f'{Pw:.1f} W')], Pf, 66, bw=52, gap=30)
    c += ttl(378, 'lamp power', CY)
    parts = [trace([(3.4, 1.4), (7.6, 1.4), (7.6, 5.6), (3.4, 5.6), (3.4, 1.4)]),
             flow([(5.0, 1.4), (7.6, 1.4), (7.6, 5.6), (3.4, 5.6), (3.4, 1.4), (3.8, 1.4)]),
             acsrc(4.4, 1.4, f'{Vs} V'),
             dev(7.6, 3.2, 'TRIAC', GO, 1.5),
             lamp(5.6, 5.6, f'{R} Ω lamp', bright=.7)]
    return spec(k, 'Commutation<br>&amp; Power<br>Switches', HOOK[k],
                f'The {S("TRIAC", "gold")} carries the lamp —<br>a DIAC only {S("fires", "cyan")} the gate',
                'TRIAC dimmer at α = 90°', svg(c), parts,
                [chip('left', 300, 'c', f'{Vs} V, 50 Hz'), chip('left', 364, 'g', 'α = 90° each half'),
                 chip('left', 428, 'c', f'lamp {R} Ω'),
                 chip('right', 290, 'g', f'V<sub>rms</sub> = {f(Vr, 1)} V'), chip('right', 538, 'c', f'P = {f(Pw, 1)} W', False)],
                f'V<sub>rms</sub> = {Vs} × √(1 − 0.5 + 0) = <b class="gl">{f(Vr, 1)} V</b><br>'
                f'P = {Vs}² × 0.5 ÷ {R} = <b class="cl">{f(Pw, 1)} W</b>, half of {Pf:.0f} W')


# ---------------------------------------------------------------- 1.7, worked example: R-C turn-off snubber for an IGBT
def u1L3():
    k = 'ee-pe-u1-L3'
    I, V, fs, dvdt, Imax, Dmin = 10, 400, 20e3, 500e6, 2, .25
    Cs = I / dvdt                      # 20 nF
    E = .5 * Cs * V ** 2               # 1.6 mJ
    Pr = E * fs                        # 32 W
    Rs = V / Imax                      # 200 ohm
    tdis = 3 * Rs * Cs                 # 12 us
    ton = Dmin / fs                    # 12.5 us
    assert round(Cs * 1e9) == 20 and round(Pr) == 32 and round(tdis * 1e6) == 12
    trise = V / dvdt                   # 0.8 us
    c, (xa, xb, y0, y1, Yz) = wave2(0, 220, 'v' + sb('CE') + ' at turn-off', GO,
                                    lambda t: V * min(t / trise, 1), 0, V * 1.1, 0, 2e-6, 200, False, .14)
    c += line(xa, y1, xb, y1) + ax(xa - 4, y1 - (V / (V * 1.1)) * (y1 - y0) + 5, f'{V} V', 'end')
    xr = xa + (xb - xa) * trise / 2e-6
    c += line(xr, y1, xr, y0 + 10, GO, 1.2, '4 4') + ax(xr, 138, f'{g(trise * 1e6)} µs') + ax(xa, 138, '0')
    c += f'<text x="{xr + 8:.1f}" y="{y1 - 22:.1f}" class="pt" fill="{GO}">{g(dvdt / 1e6)} V/µs</text>'
    c += ttl(352, 'capacitor empties in time', CY)
    c += hbars(232, 44, [('3R' + sb('s') + 'C' + sb('s'), tdis * 1e6, CY, f'{g(round(tdis * 1e6, 1))} µs'),
                         ('min on', ton * 1e6, GO, f'{g(ton * 1e6)} µs')], 12.5, 80, h=24, gap=18, lw=66)
    parts = [trace([(3.4, 1.4), (7.6, 1.4), (7.6, 5.6), (3.4, 5.6), (3.4, 1.4)]),
             trace([(7.6, 2.3), (5.6, 2.3), (5.6, 4.8), (7.6, 4.8)]),
             flow([(5.6, 1.4), (7.6, 1.4), (7.6, 5.6), (3.4, 5.6), (3.4, 1.4), (3.8, 1.4)]),
             lab(7.6, 5.0, .05, f'{I} A', CY, 16, dx=22),
             dcsrc(4.6, 1.4, f'{V} V'),
             res(5.6, 2.95, f'{g(Rs)} Ω', 'y', CY, 1.2),
             capcan(5.6, 4.15, f'{g(round(Cs * 1e9))} nF', 66, CY, 25),
             dev(7.6, 3.45, 'IGBT', GO, 1.3)]
    return spec(k, 'Protection,<br>Heat &amp; Wide<br>Band-gap Devices', HOOK[k],
                f'A snubber {S("moves", "gold")} the loss —<br>32 W lands in {S("R<sub>s</sub>", "cyan")}, not saved',
                'R-C snubber on an IGBT', svg(c), parts,
                [chip('left', 300, 'c', f'{I} A off {V} V, 20 kHz'), chip('left', 364, 'g', f'C<sub>s</sub> = {g(round(Cs * 1e9))} nF'),
                 chip('left', 428, 'c', f'R<sub>s</sub> = {g(Rs)} Ω'),
                 chip('right', 290, 'g', f'{g(round(Pr))} W in R<sub>s</sub>'), chip('right', 538, 'c', f'{g(E * 1e3)} mJ per cycle', False)],
                f'C<sub>s</sub> = {I} ÷ {g(dvdt / 1e6)} V/µs = <b class="cl">{g(round(Cs * 1e9))} nF</b>, E = ½C<sub>s</sub>V² = {g(E * 1e3)} mJ<br>'
                f'P = {g(E * 1e3)} mJ × 20 kHz = <b class="gl">{g(round(Pr))} W</b> in R<sub>s</sub> = {g(Rs)} Ω', SMALL)


# ---------------------------------------------------------------- 2.1, worked example 2: half-wave R-L, with and without a freewheeling diode
def u2L1():
    k = 'ee-pe-u2-L1'
    Vs, R, beta = 230, 10, 225.8
    Vm = sq2 * Vs
    v_nofw = Vm / (2 * pi) * (1 - math.cos(rad(beta)))     # 87.86 V
    v_fw = Vm / pi                                           # 103.54 V
    assert f(v_nofw) == '87.86' and f(v_fw) == '103.54'
    c = ''
    for n, (x0, title, col, fn) in enumerate(((0, f'no FWD: on to β = {beta}°', CY, lambda t: Vm * math.sin(t) if t <= rad(beta) else 0),
                                             (236, 'with FWD: clamped at 0', GO, lambda t: Vm * math.sin(t) if t <= pi else 0))):
        w, (xa, xb, y0, y1, Yz) = wave2(x0, 214, title, col, fn, -.75 * Vm, Vm, 0, 2 * pi, 360)
        c += w + ax(xa + (xb - xa) * .5, Yz + 16, '180°') + ax(xa - 4, y0 + 10, 'V' + sb('m'), 'end')
        if n == 0:
            xb_ = xa + (xb - xa) * beta / 360
            c += line(xb_, Yz, xb_, y1, CY, 1.5, '3 3') + ax(xb_ + 10, y1 + 14, 'β')
    parts = [trace([(3.4, 1.4), (7.6, 1.4), (7.6, 5.6), (3.4, 5.6), (3.4, 1.4)]),
             trace([(6.4, 1.4), (6.4, 5.6)]),
             flow([(5.0, 1.4), (7.6, 1.4), (7.6, 5.6), (3.4, 5.6), (3.4, 1.4), (3.8, 1.4)]),
             acsrc(4.3, 1.4, f'{Vs} V'),
             diode(5.6, 1.4, 'D'),
             diode(6.4, 3.5, 'FWD', 'y', GO),
             res(7.6, 3.2, f'{R} Ω', 'y', WH, 1.7),
             toroid(7.05, 5.6, '31.8 mH', rx=46)]
    return spec(k, 'Diode<br>Rectifiers<br>&amp; Filters', HOOK[k],
                f'Half-wave: {S("V<sub>m</sub>/π", "gold")} = 0.318 V<sub>m</sub> —<br>0.637 V<sub>m</sub> is {S("full-wave", "cyan")}',
                'Half-wave R-L, ωL = 10 Ω', svg(c), parts,
                [chip('left', 300, 'c', f'{Vs} V, 50 Hz'), chip('left', 364, 'c', f'R = {R} Ω, L = 31.8 mH'),
                 chip('left', 428, 'c', f'β = {beta}°'),
                 chip('right', 290, 'c', f'no FWD: {f(v_nofw)} V'), chip('right', 538, 'g', f'FWD: {f(v_fw)} V', False)],
                f'No FWD: {f(Vm / (2 * pi))} × (1 − cos {beta}°) = <b class="cl">{f(v_nofw)} V</b><br>'
                f'With FWD: V<sub>m</sub>/π = {f(Vm)} ÷ π = <b class="gl">{f(v_fw)} V</b>')


# ---------------------------------------------------------------- 2.4, worked example: full bridge at 60 degrees, R load and continuous current
def u2L2():
    k = 'ee-pe-u2-L2'
    Vs, a, R = 230, rad(60), 10
    Vm = sq2 * Vs
    VR = round(Vm / pi, 2) * (1 + math.cos(a))    # 103.54 x 1.5 = 155.31 V, as the book rounds
    VL = 2 * Vm / pi * math.cos(a)                 # 103.54 V
    assert f(VR) == '155.31' and f(VL) == '103.54'
    lo, hi = -.9 * Vm, Vm
    c, (xa, xb, y0, y1, Yz) = wave2(0, 220, 'R only: 1 + cos α', GO,
                                    lambda t: Vm * abs(math.sin(t)) if (t % pi) >= a else 0, lo, hi)
    yv = y1 - (VR - lo) / (hi - lo) * (y1 - y0)
    c += line(xa, yv, xb, yv, GO, 1.5, '5 4') + f'<text x="{xb:.1f}" y="{yv - 6:.1f}" text-anchor="end" class="pt" fill="{GO}">{f(VR)} V</text>'
    c2, (xa2, xb2, _, _, Yz2) = wave2(236, 220, 'large L: cos α', CY,
                                     lambda t: Vm * math.sin(t) * (1 if ((t - a) % (2 * pi)) < pi else -1), lo, hi)
    yv2 = y1 - (VL - lo) / (hi - lo) * (y1 - y0)
    c += c2 + line(xa2, yv2, xb2, yv2, CY, 1.5, '5 4') + f'<text x="{xb2:.1f}" y="{yv2 - 6:.1f}" text-anchor="end" class="pt" fill="{CY}">{f(VL)} V</text>'
    c += ax(xa2 + (xb2 - xa2) * (rad(210) / (2 * pi)), Yz2 + 30, '− slice', col=CY)
    parts = bridge_parts(['T1', 'T4', 'T3', 'T2'], acsrc(3.0, 2.5, f'{Vs} V', r=34, h=50),
                         [res(7.6, 3.5, f'{R} Ω', 'y', WH, 1.7)], [toroid(5.8, 5.6, 'large L', rx=46)])
    return spec(k, 'Doublers &amp;<br>Controlled<br>Rectifiers', HOOK[k],
                f'With R alone use 1 + {S("cos α", "gold")} —<br>plain cos α needs {S("continuous", "cyan")} i',
                'Full bridge, α = 60°, 10 Ω', svg(c), parts,
                [chip('left', 300, 'c', f'{Vs} V, 50 Hz'), chip('left', 364, 'g', 'α = 60°'), chip('left', 428, 'c', f'R = {R} Ω'),
                 chip('right', 290, 'g', f'R only: {f(VR)} V'), chip('right', 538, 'c', f'with L: {f(VL)} V', False)],
                f'(a) {f(Vm / pi)} × (1 + cos 60°) = <b class="gl">{f(VR)} V</b>, {f(VR / R)} A<br>'
                f'(b) {f(2 * Vm / pi)} × cos 60° = <b class="cl">{f(VL)} V</b>, {f(VL / R)} A')


# ---------------------------------------------------------------- 2.5, worked example: six-pulse bridge at 30 degrees
def legs3(xs, yt, yb, names, w=.85):
    ym = (yt + yb) / 2
    o = [trace([(xs[0], yt), (xs[-1], yt)]), trace([(xs[0], yb), (xs[-1], yb)])] + [trace([(x, yt), (x, yb)]) for x in xs]
    top = [dev(x, yt + .05, names[2 * n], None, w) for n, x in enumerate(xs)]
    bot = [dev(x, yb - .05, names[2 * n + 1], None, w) for n, x in enumerate(xs)]
    return o, top, bot, ym


def u2L3():
    k = 'ee-pe-u2-L3'
    VL, a, fr = 400, rad(30), 50
    VLm = sq2 * VL
    Vd0 = 3 * VLm / pi                       # 540.19 V
    Vdc = round(Vd0, 2) * math.cos(a)        # 467.82 V
    Vph = VL / sq3; Vm = sq2 * Vph
    V3 = 3 * sq3 * Vm / (2 * pi) * math.cos(a)  # 233.91 V
    assert f(Vd0) == '540.19' and f(Vdc) == '467.82' and f(V3) == '233.91'
    x0, x1, y0, y1 = 30, 232, 30, 122
    span = pi
    c = ttl(130, 'output, α from the crossing', GO) + line(x0, y0, x0, y1) + line(x0, y1, x1, y1)
    for kk in range(6):
        for seg in plot(x0, x1, y0, y1, lambda t, kk=kk: VLm * math.cos(t - kk * pi / 3) if VLm * math.cos(t - kk * pi / 3) > .55 * VLm else None, 0, span, 0, VLm, 300):
            c += f'<polyline points="{" ".join(f"{p:.1f},{q:.1f}" for p, q in seg)}" fill="none" stroke="{AX}" stroke-width="1.3" stroke-dasharray="3 3"/>'
    fn = lambda t: VLm * math.cos(((t - a + pi / 6) % (pi / 3)) - pi / 6 + a)
    for seg in plot(x0, x1, y0, y1, fn, 0, span, 0, VLm, 600):
        c += curve(seg, GO, fill=GO, base=y1, op=.14)
    X = lambda t: x0 + (x1 - x0) * t / span
    c += line(X(pi / 6), y1, X(pi / 6), y0 + 6, CY, 1.2, '3 3') + line(X(pi / 6 + a), y1, X(pi / 6 + a), y0 + 6, GO, 1.5)
    c += ax(X(pi / 6) - 4, 138, 'crossing', 'end', CY) + ax(X(pi / 6 + a) + 4, 138, '+30° = α', 'start', GO)
    c += ttl(352, 'same supply, same α', CY)
    c += hbars(240, 44, [('6-pulse', Vdc, GO, f'{f(Vdc, 1)} V'), ('3-pulse', V3, CY, f'{f(V3, 1)} V')], Vdc, 84, h=24, gap=18, lw=62)
    o, top, bot, ym = legs3([3.4, 4.8, 6.2], 1.9, 4.7, ['T1', 'T4', 'T3', 'T6', 'T5', 'T2'])
    o, top, bot, ym = legs3([3.9, 5.3, 6.7], .9, 3.1, ['T1', 'T4', 'T3', 'T6', 'T5', 'T2'])
    o, top, bot, ym = legs3([4.3, 5.6, 6.9], 1.3, 3.5, [''] * 6)
    parts = o + [trace([(6.9, 1.3), (7.7, 1.3), (7.7, 5.6), (3.7, 5.6), (3.7, 3.5), (4.3, 3.5)]),
                 flow([(7.2, 1.3), (7.7, 1.3), (7.7, 5.6), (3.7, 5.6), (3.7, 3.5), (4.0, 3.5)]),
                 block(3.0, 1.2, 1.4, 1.0, .6, '3φ 400 V', size=14)] + top + [
                 cable(3.2, 1.7, .6, 4.3, ym, .05, '#E06666', 3.5, .8), cable(3.0, 1.7, .6, 5.6, ym, .05, '#F6D285', 3.5, 1.1),
                 cable(2.8, 1.7, .6, 6.9, ym, .05, '#7FB2E5', 3.5, 1.4)] + bot + [
                 res(7.7, 3.4, 'R', 'y', WH, 1.7), toroid(5.8, 5.6, 'L', rx=43, n=36)]
    return spec(k, 'Three-phase<br>Rectifiers &amp;<br>Power Factor', HOOK[k],
                f'α counts from the {S("crossing", "gold")} of two<br>phases, {S("30°", "cyan")} after the phase zero',
                'Six-pulse bridge, α = 30°', svg(c), parts,
                [chip('left', 300, 'c', f'{VL} V, 50 Hz line'), chip('left', 364, 'g', 'α = 30°'), chip('left', 428, 'c', f'ripple 6 × 50 = {6 * fr} Hz'),
                 chip('right', 290, 'g', f'V<sub>dc</sub> = {f(Vdc, 1)} V'), chip('right', 538, 'c', f'3-pulse: {f(V3, 1)} V', False)],
                f'V<sub>d0</sub> = 3√2 × {VL} ÷ π = <b class="cl">{f(Vd0)} V</b><br>'
                f'V<sub>dc</sub> = {f(Vd0)} × cos 30° = <b class="gl">{f(Vdc)} V</b>, ripple {6 * fr} Hz')


# ---------------------------------------------------------------- 2.8, worked example: regenerative braking at 120 degrees
def u2L4():
    k = 'ee-pe-u2-L4'
    Vs, a, E, R = 230, rad(120), -120, 2
    Vm = sq2 * Vs
    Vdc = 2 * Vm / pi * math.cos(a)          # -103.54 V
    Id = (Vdc - E) / R                       # 8.23 A
    Pac = abs(Vdc) * Id                      # 852 W
    Pm = abs(E) * Id; Pr = Id ** 2 * R       # 988 W, 136 W
    assert f(Vdc) == '−103.54' and f(Id) == '8.23' and round(Pac) == 852 and round(Pm) == 988 and round(Pr) == 136
    lo, hi = -Vm, Vm
    c, (xa, xb, y0, y1, Yz) = wave2(0, 226, 'v' + sb('o') + ' at α = 120°', CY,
                                    lambda t: Vm * math.sin(t) * (1 if ((t - a) % (2 * pi)) < pi else -1), lo, hi, 0, 2 * pi, 480)
    yv = y1 - (Vdc - lo) / (hi - lo) * (y1 - y0)
    c += line(xa, yv, xb, yv, GO, 1.8, '5 4') + f'<text x="{xb:.1f}" y="{yv + 20:.1f}" text-anchor="end" class="pt" fill="{GO}">{f(Vdc)} V</text>'
    c += ttl(352, 'where the power goes', GO)
    c += hbars(240, 34, [('machine', Pm, CY, f'{Pm:.0f} W'), ('to supply', Pac, GO, f'{Pac:.0f} W'), ('lost in R', Pr, AX, f'{Pr:.0f} W')],
               Pm, 92, h=20, gap=10, lw=70)
    parts = bridge_parts(['T1', 'T4', 'T3', 'T2'], acsrc(3.0, 2.5, f'{Vs} V', r=34, h=50),
                         [machine(7.6, 3.9, 'E', 'E = −120 V')],
                         [res(5.4, 5.6, f'{R} Ω', 'x', WH, 1.7), bigarrow(6.6, 6.4, 4.2, 6.4, GO, .1, 6), lab(5.4, 6.4, .1, 'power back', GO, 15, dy=26)])
    return spec(k, 'Overlap &amp;<br>Inversion', HOOK[k],
                f'V<sub>dc</sub> turns {S("negative", "gold")} —<br>I<sub>d</sub> stays {S("positive", "cyan")}: power flows back',
                'Bridge inverting at 120°', svg(c), parts,
                [chip('left', 300, 'g', 'α = 120°'), chip('left', 364, 'c', f'E = −120 V, R = {R} Ω'), chip('left', 428, 'c', f'{Vs} V, 50 Hz'),
                 chip('right', 290, 'c', f'I<sub>d</sub> = +{f(Id)} A'), chip('right', 538, 'g', f'{Pac:.0f} W to the supply', False)],
                f'V<sub>dc</sub> = {f(2 * Vm / pi)} × cos 120° = <b class="cl">{f(Vdc)} V</b><br>'
                f'I<sub>d</sub> = ({f(Vdc)} + 120) ÷ {R} = {f(Id)} A → <b class="gl">{Pac:.0f} W</b> returned')


# ---------------------------------------------------------------- 2.10, worked example: 500 W boost PFC rectifier
def u2L5():
    k = 'ee-pe-u2-L5'
    Pw, Vs, Vo = 500, 230, 400
    Is = Pw / Vs; Ipk = sq2 * Is              # 2.174 A, 3.074 A
    Re = Vs ** 2 / Pw                         # 105.8 ohm
    Vm = sq2 * Vs
    Dpk = 1 - Vm / Vo                         # 0.187
    D100 = 1 - 100 / Vo                       # 0.75
    Io = Pw / Vo                              # 1.25 A
    assert f(Is, 3) == '2.174' and f(Ipk, 3) == '3.074' and f(Dpk, 3) == '0.187' and f(Re, 1) == '105.8'
    x0, x1, y0, y1 = 30, 220, 30, 122
    mid = (y0 + y1) / 2
    c = ttl(130, 'i' + sb('s') + ' follows v' + sb('s'), CY) + line(x0, y0, x0, y1) + line(x0, mid, x1, mid)
    for seg in plot(x0, x1, y0, y1, lambda t: math.sin(t), 0, 2 * pi, -1.1, 1.1):
        c += f'<polyline points="{" ".join(f"{p:.1f},{q:.1f}" for p, q in seg)}" fill="none" stroke="{GO}" stroke-width="2" stroke-dasharray="5 4"/>'
    for seg in plot(x0, x1, y0, y1, lambda t: .72 * math.sin(t), 0, 2 * pi, -1.1, 1.1):
        c += curve(seg, CY, fill=CY, base=mid, op=.14)
    c += ax(x1, y0 + 2, f'v{sb("s")} {f(Vm, 0)} V pk', 'end', GO) + ax(x0 + 4, y1 + 14, f'i{sb("s")} {f(Ipk, 2)} A pk', 'start', CY)
    xa, xb = 284, 448
    c += ttl(370, 'duty over a half cycle', GO) + line(xa, y0, xa, y1) + line(xa, y1, xb, y1)
    Y = lambda d: y1 - d * (y1 - y0)
    for seg in plot(xa, xb, y0, y1, lambda t: 1 - Vm * abs(math.sin(t)) / Vo, 0, pi, 0, 1):
        c += curve(seg, GO)
    t100 = math.asin(100 / Vm)
    for t, d, txt in ((pi / 2, Dpk, f'{f(Dpk, 3)}'), (t100, D100, f'{g(D100)} at 100 V')):
        xx = xa + (xb - xa) * t / pi
        c += f'<circle cx="{xx:.1f}" cy="{Y(d):.1f}" r="5" fill="{CY}"/><text x="{xx + 8:.1f}" y="{Y(d) - 6:.1f}" class="pt" fill="{CY}">{txt}</text>'
    c += ax(xa - 4, Y(1) + 5, '1', 'end') + ax(xa - 4, y1 + 5, '0', 'end') + ax((xa + xb) / 2, 138, 'peak') + ax(xa, 138, '0°') + ax(xb, 138, '180°')
    parts = [trace([(3.0, 1.4), (7.6, 1.4)]), trace([(4.2, 1.4), (4.2, 5.2), (7.6, 5.2)]),
             trace([(6.3, 1.4), (6.3, 5.2)]), trace([(7.6, 1.4), (7.6, 5.2)]),
             flow([(4.8, 1.4), (7.4, 1.4)]),
             acsrc(3.0, 1.4, f'{Vs} V'),
             block(4.2, 1.4, 1.1, 1.1, .5, 'bridge', '#2F3A45', '#151B21', '#1F262E', size=14),
             toroid(5.35, 1.4, 'L', rx=41),
             diode(7.0, 1.4, 'D'),
             dev(6.3, 3.3, 'FET', None, 1.15),
             capcan(7.6, 3.4, f'{Vo} V', 76, GO, 26)]
    return spec(k, 'Dual<br>Converters &amp;<br>PFC Rectifiers', HOOK[k],
                f'A boost PFC draws a {S("sine", "cyan")} —<br>a big capacitor draws {S("spikes", "gold")}',
                '500 W boost PFC stage', svg(c), parts,
                [chip('left', 300, 'c', f'{Pw} W from {Vs} V'), chip('left', 364, 'g', f'I<sub>s</sub> = {f(Is, 2)} A rms'),
                 chip('left', 428, 'c', f'R<sub>e</sub> = {f(Re, 1)} Ω'),
                 chip('right', 290, 'c', f'I<sub>o</sub> = {g(Io)} A'), chip('right', 538, 'g', f'D = {f(Dpk, 3)} at the peak', False)],
                f'I<sub>s</sub> = {Pw} ÷ {Vs} = <b class="cl">{f(Is, 3)} A</b>, I<sub>pk</sub> = √2 I<sub>s</sub> = {f(Ipk, 3)} A<br>'
                f'D = 1 − {f(Vm)} ÷ {Vo} = <b class="gl">{f(Dpk, 3)}</b> at the peak', SMALL)


R2 = [(3.4, 1.4), (7.6, 1.4), (7.6, 5.6), (3.4, 5.6), (3.4, 1.4)]


def tri_wave(x0, x1, y0, y1, T, Ton, lo, hi, vmin, vmax, periods=2):
    """inductor current: rises from lo to hi in Ton, falls back in T - Ton"""
    def fn(t):
        u = t % T
        return lo + (hi - lo) * u / Ton if u < Ton else hi - (hi - lo) * (u - Ton) / (T - Ton)
    return plot(x0, x1, y0, y1, fn, 0, periods * T, vmin, vmax, 400)


# ---------------------------------------------------------------- 3.1, worked example: chopper duty ratio at 1 kHz and 2 kHz
def u3L1():
    k = 'ee-pe-u3-L1'
    Vs, R, Ton = 200, 10, .4e-3
    out = []
    for fsw in (1e3, 2e3):
        T = 1 / fsw; D = Ton / T; Vo = D * Vs; Io = Vo / R; Po = Vo * Io
        out.append((fsw, T, D, Vo, Io, Po))
    (f1, T1, D1, V1, I1, P1), (f2, T2, D2, V2, I2, P2) = out
    assert (D1, V1, I1, P1) == (.4, 80, 8, 640) and (round(D2, 3), round(V2), round(P2)) == (.8, 160, 2560)
    c = ''
    for x0, (fsw, T, D, Vo, Io, Po), col in ((0, out[0], GO), (236, out[1], CY)):
        w, (xa, xb, y0, y1, Yz) = wave2(x0, 214, f'{fsw / 1e3:g} kHz: D = {g(round(D, 2))}', col,
                                        lambda t, T=T: Vs if (t % T) < Ton else 0, 0, Vs * 1.15, 0, 2e-3, 800)
        yv = y1 - Vo / (Vs * 1.15) * (y1 - y0)
        c += w + line(xa, yv, xb, yv, WH, 1.4, '5 4') + f'<text x="{xb:.1f}" y="{yv - 5:.1f}" text-anchor="end" class="pt" fill="{WH}">{g(round(Vo))} V</text>'
        c += ax(xa - 4, y1 - Vs / (Vs * 1.15) * (y1 - y0) + 5, f'{Vs}', 'end') + ax(xa, 138, '0') + ax(xb, 138, '2 ms', 'end')
    parts = [trace(R2), trace([(6.2, 1.4), (6.2, 5.6)]),
             flow([(6.1, 1.4), (7.6, 1.4), (7.6, 5.6), (6.0, 5.6)]),
             dcsrc(4.9, 5.6, f'{Vs} V', 1.6, 1.2, .9),
             dev(5.2, 1.4, 'S', GO, 1.1),
             toroid(6.9, 1.4, 'L', rx=40),
             diode(6.2, 3.5, 'FWD', 'y'),
             res(7.6, 3.6, f'{R} Ω', 'y', WH, 1.7)]
    return spec(k, 'Choppers &amp;<br>Regulated<br>Supplies', HOOK[k],
                f'Duty ratio D = {S("T<sub>on</sub>", "gold")} ÷ T:<br>the share of time switched {S("ON", "cyan")}',
                'Chopper, T<sub>on</sub> = 0.4 ms', svg(c), parts,
                [chip('left', 300, 'c', f'{Vs} V DC'), chip('left', 364, 'g', 'T<sub>on</sub> = 0.4 ms'), chip('left', 428, 'c', f'R = {R} Ω, large L'),
                 chip('right', 290, 'g', f'1 kHz: {g(V1)} V, {g(P1)} W'), chip('right', 538, 'c', f'2 kHz: {g(round(V2))} V, {g(round(P2))} W', False)],
                f'1 kHz: D = 0.4 ÷ 1 = {g(D1)}, V<sub>o</sub> = 0.4 × {Vs} = <b class="gl">{g(V1)} V</b>, {g(I1)} A<br>'
                f'2 kHz: D = 0.4 ÷ 0.5 = {g(round(D2, 2))}, V<sub>o</sub> = <b class="cl">{g(round(V2))} V</b>, {g(round(I2))} A')


# ---------------------------------------------------------------- 3.4, worked example: boost converter 24 V to 60 V
def u3L2():
    k = 'ee-pe-u3-L2'
    Vs, D, fs, L, C, R = 24, .6, 50e3, 300e-6, 470e-6, 100
    T = 1 / fs
    Vo = Vs / (1 - D); Io = Vo / R; IL = Io / (1 - D)
    dI = Vs * D * T / L; imax, imin = IL + dI / 2, IL - dI / 2
    dV = Io * D / (fs * C)
    assert round(Vo, 1) == 60 and round(IL, 2) == 1.5 and round(dI, 2) == .96 and round(imax, 2) == 1.98 and round(imin, 2) == 1.02 and round(dV * 1e3, 1) == 15.3
    x0, x1, y0, y1 = 44, 236, 34, 118
    lo, hi = .8, 2.2
    Y = lambda v: y1 - (v - lo) / (hi - lo) * (y1 - y0)
    c = ttl(140, 'inductor current', CY) + line(x0, y0, x0, y1) + line(x0, y1, x1, y1)
    for seg in tri_wave(x0, x1, y0, y1, T, D * T, imin, imax, lo, hi):
        c += curve(seg, CY)
    c += line(x0, Y(IL), x1, Y(IL), WH, 1.2, '5 4')
    c += ax(x0 - 4, Y(imax) + 5, f'{f(imax)}', 'end', CY) + ax(x0 - 4, Y(imin) + 5, f'{f(imin)}', 'end', CY) + ax(x1, Y(IL) - 6, f'avg {g(round(IL, 2))} A', 'end')
    c += ax(x0, 136, '0') + ax(x0 + (x1 - x0) * .3, 136, f'{g(D * T * 1e6)} µs on') + ax(x1, 136, f'{g(2 * T * 1e6)} µs', 'end')
    c += ttl(360, 'boost: V<tspan baseline-shift="sub" font-size="70%">s</tspan> ÷ (1 − D)', GO)
    c += vbars(300, 120, [('V' + sb('s'), Vs, CY, f'{Vs} V'), ('V' + sb('o'), Vo, GO, f'{g(round(Vo))} V')], Vo, 70, bw=50, gap=40)
    parts = [trace(R2), trace([(6.4, 1.4), (6.4, 5.6)]),
             flow([(5.6, 1.4), (7.6, 1.4), (7.6, 2.6)]),
             dcsrc(4.9, 5.6, f'{Vs} V', 1.6, 1.2, .9),
             toroid(4.7, 1.4, f'{g(L * 1e6)} µH', rx=36),
             diode(7.0, 1.4, 'D'),
             dev(6.4, 4.7, 'FET', None, 1.1),
             capcan(7.6, 3.7, f'{g(C * 1e6)} µF', 58, WH, 24)]
    return spec(k, 'Buck &amp; Boost<br>Converters', HOOK[k],
                f'Boost: V<sub>o</sub> = V<sub>s</sub> ÷ (1 − {S("D", "gold")}) —<br>D·V<sub>s</sub> is the {S("buck", "cyan")} formula',
                'Boost: 24 V in, D = 0.6', svg(c), parts,
                [chip('left', 300, 'c', f'{Vs} V in, {g(fs / 1e3)} kHz'), chip('left', 364, 'g', f'D = {D}'), chip('left', 428, 'c', f'R = {R} Ω'),
                 chip('right', 290, 'g', f'V<sub>o</sub> = {g(round(Vo))} V'), chip('right', 538, 'c', f'i<sub>L</sub>: {f(imin)} to {f(imax)} A', False)],
                f'V<sub>o</sub> = {Vs} ÷ (1 − {D}) = <b class="gl">{f(Vo, 1)} V</b>, I<sub>o</sub> = {g(round(Io, 2))} A, I<sub>L</sub> = {g(round(IL, 2))} A<br>'
                f'ΔI<sub>L</sub> = {Vs} × {D} × {g(T * 1e6)} µs ÷ {g(L * 1e6)} µH = <b class="cl">{f(dI)} A</b>')


# ---------------------------------------------------------------- 3.6, worked example: flyback 48 V, 40 : 20 turns
def u3L3():
    k = 'ee-pe-u3-L3'
    Vs, N1, N2, D = 48, 40, 20, .4
    n = N1 / N2
    Vo = Vs * D / ((1 - D) * n)                  # 16 V
    D12 = 24 / 72                                # from 24(1 - D) = 48 D
    assert abs(Vs * D12 / (n * (1 - D12)) - 12) < 1e-9 and abs(Vo - 16) < 1e-9
    st12, st16 = Vs + n * 12, Vs + n * Vo        # 72 V, 80 V
    x0, x1, y0, y1 = 44, 236, 34, 118
    Dlo, Dhi, Vmax = .1, .55, 32
    X = lambda d: x0 + (x1 - x0) * (d - Dlo) / (Dhi - Dlo)
    Y = lambda v: y1 - v / Vmax * (y1 - y0)
    c = ttl(140, 'V<tspan baseline-shift="sub" font-size="70%">o</tspan> against D', GO) + line(x0, y0, x0, y1) + line(x0, y1, x1, y1)
    for seg in plot(x0, x1, y0, y1, lambda d: Vs * d / ((1 - d) * n), Dlo, Dhi, 0, Vmax):
        c += curve(seg, GO)
    for d, v, col, t in ((D12, 12, CY, '1/3 → 12 V'), (D, Vo, GO, '0.4 → 16 V')):
        c += f'<circle cx="{X(d):.1f}" cy="{Y(v):.1f}" r="5.5" fill="{col}"/>' + line(X(d), Y(v), X(d), y1, col, 1.2, '3 3')
        c += f'<text x="{X(d) - 8:.1f}" y="{Y(v) - 8:.1f}" text-anchor="end" class="pt" fill="{col}">{t}</text>'
    c += ax(x0, 136, '0.1') + ax(x1, 136, '0.55', 'end') + ax(x0 - 4, Y(30) + 5, '30 V', 'end')
    c += ttl(352, 'switch stress V<tspan baseline-shift="sub" font-size="70%">s</tspan> + nV<tspan baseline-shift="sub" font-size="70%">o</tspan>', CY)
    c += hbars(240, 44, [('12 V out', st12, CY, f'{g(st12)} V'), ('16 V out', st16, GO, f'{g(st16)} V')], st16, 84, h=24, gap=18, lw=72)
    core = (box(5.15, 2.4, 1.0, 1.8, 1.25, '#9AA6B2', '#55606B', '#727E8A')
            + box(4.75, 2.65, .5, 1.3, 1.0, '#E8A464', '#8A4E20', '#B8692C', .12)
            + box(6.05, 2.65, .5, 1.3, 1.0, '#E8A464', '#8A4E20', '#B8692C', .12)
            + lab(5.0, 3.3, 1.12, f'{N1} t', WH, 15, dy=5) + lab(6.3, 3.3, 1.12, f'{N2} t', WH, 15, dy=5))
    parts = [trace([(4.3, 1.4), (5.0, 1.4), (5.0, 2.6)]), trace([(5.0, 4.0), (5.0, 5.6), (3.4, 5.6), (3.4, 1.4), (4.3, 1.4)]),
             trace([(6.3, 2.6), (6.3, 1.4), (7.6, 1.4), (7.6, 5.6), (6.3, 5.6), (6.3, 4.0)]),
             flow([(6.3, 2.4), (6.3, 1.4), (7.6, 1.4), (7.6, 2.1)]),
             dcsrc(4.0, 1.4, f'{Vs} V', 1.6, 1.3),
             diode(6.95, 1.4, 'D'),
             core,
             dev(5.0, 4.9, 'FET', None, 1.0),
             capcan(7.6, 3.0, f'{g(Vo)} V', 60, GO, 24)]
    return spec(k, 'Buck-boost,<br>Cuk, Flyback<br>&amp; Forward', HOOK[k],
                f'Flyback divides by {S("(1 − D)", "gold")} too:<br>{S("16 V", "cyan")} at D = 0.4, not D·V<sub>s</sub>/n',
                'Flyback, 48 V, N1 : N2 = 2', svg(c), parts,
                [chip('left', 300, 'c', f'{Vs} V DC, 100 kHz'), chip('left', 364, 'c', f'N1 : N2 = {N1} : {N2}'), chip('left', 428, 'g', f'D = {D}'),
                 chip('right', 290, 'g', f'V<sub>o</sub> = {g(Vo)} V'), chip('right', 538, 'c', '12 V needs D = 1/3', False)],
                f'V<sub>o</sub> = {Vs} × {D} ÷ ({1 - D:g} × {g(n)}) = <b class="gl">{g(Vo)} V</b><br>'
                f'stress = V<sub>s</sub> + nV<sub>o</sub> = {Vs} + {g(n)} × {g(Vo)} = <b class="cl">{g(st16)} V</b>')


# ---------------------------------------------------------------- 3.8, worked example: designing the buck inductor
def u3L4():
    k = 'ee-pe-u3-L4'
    L, Io, dI, Ae, Bmax, J, fs, Vs, Vo = 100e-6, 4, 1.2, 1e-4, .3, 4, 100e3, 50, 20
    Ipk = Io + dI / 2                                   # 4.6 A
    N0 = L * Ipk / (Bmax * Ae)                          # 15.33
    N = math.ceil(N0)                                   # 16
    Bv = L * Ipk / (N * Ae)                             # 0.2875 T
    lg = 4 * pi * 1e-7 * N ** 2 * Ae / L                # 0.32 mm
    Irms = math.sqrt(Io ** 2 + dI ** 2 / 12)            # 4.01 A
    Acu = Io / J                                        # 1.0 mm2
    assert round(N0, 2) == 15.33 and N == 16 and round(Bv, 4) == .2875 and round(lg * 1e3, 2) == .32 and round(Irms, 2) == 4.01
    T = 1 / fs; Ton = Vo / Vs * T
    x0, x1, y0, y1 = 44, 236, 34, 118
    lo, hi = 3.0, 5.0
    Y = lambda v: y1 - (v - lo) / (hi - lo) * (y1 - y0)
    c = ttl(140, 'i<tspan baseline-shift="sub" font-size="70%">L</tspan> in the buck', CY) + line(x0, y0, x0, y1) + line(x0, y1, x1, y1)
    for seg in tri_wave(x0, x1, y0, y1, T, Ton, Io - dI / 2, Ipk, lo, hi):
        c += curve(seg, CY)
    c += line(x0, Y(Io), x1, Y(Io), WH, 1.2, '5 4') + line(x0, Y(Ipk), x1, Y(Ipk), GO, 1.5, '5 4')
    c += ax(x0 - 4, Y(Ipk) + 5, f'{g(Ipk)}', 'end', GO) + ax(x0 - 4, Y(Io) + 5, f'{g(Io)}', 'end') + ax(x0 - 4, Y(Io - dI / 2) + 5, f'{g(Io - dI / 2)}', 'end', CY)
    c += f'<text x="{x1:.1f}" y="{Y(Ipk) - 6:.1f}" text-anchor="end" class="pt" fill="{GO}">peak: size for this</text>'
    c += ax(x1, Y(Io) + 16, 'average 4 A', 'end')
    c += ttl(356, 'the design', GO)
    rows = [('turns', f'{N0:.2f} → {N}', GO), ('flux', f'{Bv:.4f} T < {g(Bmax)} T', CY), ('air gap', f'{lg * 1e3:.2f} mm', CY), ('copper', f'{Acu:.1f} mm²', WH)]
    for n_, (a, b, col) in enumerate(rows):
        y = 44 + n_ * 25
        c += ax(300, y, a, 'end') + f'<text x="310" y="{y}" class="pt" fill="{col}">{b}</text>'
    cu, cl, cr = '#E8A464', '#8A4E20', '#B8692C'
    fe, fl, fr = '#9AA6B2', '#55606B', '#727E8A'
    gx, gy = P(5.6, 2.2, .75)
    parts = [box(4.0, 2.5, 3.2, 1.8, .7, fe, fl, fr),
             f'<g filter="url(#gl)"><polygon points="{pts(P(4.0, 2.5, .76), P(7.2, 2.5, .76), P(7.2, 4.3, .76), P(4.0, 4.3, .76))}" fill="{GO}" opacity=".55"/></g>',
             box(4.0, 2.5, 3.2, 1.8, .7, fe, fl, fr, .9),
             box(4.9, 2.1, 1.4, 2.6, 1.45, cu, cl, cr, .1)]
    for t in range(N):
        a_, b_ = P(4.9 + 1.4 * (t + .5) / N, 4.7, .14), P(4.9 + 1.4 * (t + .5) / N, 4.7, 1.5)
        parts.append(f'<line x1="{a_[0]:.1f}" y1="{a_[1]:.1f}" x2="{b_[0]:.1f}" y2="{b_[1]:.1f}" stroke="#6B3A14" stroke-width="1.6"/>')
    parts += [lab(5.6, 3.4, 1.55, f'{N} turns', WH, 17, dy=6),
              lab(7.2, 3.4, .8, f'gap {lg * 1e3:.2f} mm', GO, 16, dx=12, anchor='start'),
              lab(4.0, 3.4, 1.6, 'A<tspan baseline-shift="sub" font-size="70%">e</tspan> = 1.0 cm²', WH, 15, dy=-6, anchor='end')]
    return spec(k, 'Soft<br>Switching &amp;<br>Magnetics', HOOK[k],
                f'Size the core for the {S("peak", "gold")} 4.6 A —<br>not the {S("average", "cyan")} 4 A',
                'Inductor for the buck', svg(c), parts,
                [chip('left', 300, 'c', f'L = {g(L * 1e6)} µH'), chip('left', 364, 'g', f'I<sub>pk</sub> = {g(Ipk)} A'), chip('left', 428, 'c', f'B<sub>max</sub> = {g(Bmax)} T'),
                 chip('right', 290, 'g', f'{N} turns, {Bv:.2f} T'), chip('right', 538, 'c', f'gap {lg * 1e3:.2f} mm', False)],
                f'N = LI<sub>pk</sub> ÷ (B<sub>max</sub>A<sub>e</sub>) = {N0:.2f} → <b class="gl">{N} turns</b><br>'
                f'B = <b class="cl">{Bv:.4f} T</b> &lt; 0.3 T; gap µ<sub>0</sub>N²A<sub>e</sub>/L = {lg * 1e3:.2f} mm', SMALL)


# ---------------------------------------------------------------- 4.1, worked example: square-wave full bridge, 300 V into 20 ohm
def u4L1():
    k = 'ee-pe-u4-L1'
    Vdc, R = 300, 20
    V1pk = 4 * Vdc / pi; V1 = V1pk / sq2; P = Vdc ** 2 / R; P1 = V1 ** 2 / R; V3 = V1 / 3
    THD = math.sqrt(Vdc ** 2 - V1 ** 2) / V1
    assert f(V1pk) == '381.97' and f(V1) == '270.09' and round(P1, 1) == 3647.6 and f(V3) == '90.03' and round(THD * 100, 1) == 48.3
    x0, x1, y0, y1 = 64, 448, 30, 128
    lo, hi = -400, 400
    mid = y1 - (0 - lo) / (hi - lo) * (y1 - y0)
    Y = lambda v: y1 - (v - lo) / (hi - lo) * (y1 - y0)
    c = line(x0, y0, x0, y1) + line(x0, mid, x1, mid)
    for seg in plot(x0, x1, y0, y1, lambda t: Vdc if (t % (2 * pi)) < pi else -Vdc, 0, 4 * pi, lo, hi, 800):
        c += curve(seg, CY, 3, CY, mid, .10)
    for seg in plot(x0, x1, y0, y1, lambda t: V1pk * math.sin(t), 0, 4 * pi, lo, hi):
        c += curve(seg, GO, 3.4)
    c += line(x0, Y(V1pk), x1, Y(V1pk), GO, 1.2, '4 4') + line(x0, Y(Vdc), x1, Y(Vdc), CY, 1.2, '4 4')
    c += ax(x0 - 6, Y(V1pk) + 4, f'{f(V1pk)}', 'end', GO) + ax(x0 - 6, Y(Vdc) + 12, f'{Vdc}', 'end', CY) + ax(x0 - 6, mid + 5, '0', 'end')
    c += f'<text x="{x0 + (x1 - x0) * .48:.1f}" y="{Y(V1pk) - 6:.1f}" class="pt" fill="{GO}">fundamental peak {f(V1pk)} V</text>'
    c += f'<text x="{x0 + (x1 - x0) * .29:.1f}" y="{Y(-Vdc) + 20:.1f}" class="pt" fill="{CY}">square wave ±{Vdc} V</text>'
    parts = [trace([(4.8, 2.0), (7.4, 2.0)]), trace([(4.8, 4.8), (7.4, 4.8)]), trace([(4.8, 2.0), (4.8, 4.8)]), trace([(7.4, 2.0), (7.4, 4.8)]),
             trace([(4.8, 2.0), (3.5, 2.0), (3.5, 4.8), (4.8, 4.8)]), trace([(4.8, 3.4), (7.4, 3.4)], GO, 3),
             flow([(4.9, 3.4), (5.4, 3.4)], GO), flow([(6.8, 3.4), (7.3, 3.4)], GO),
             dev(4.8, 2.1, 'S1', None, 1.0), dev(7.4, 2.1, 'S3', None, 1.0),
             res(6.1, 3.4, f'{R} Ω', 'x', GO, 1.2),
             dcsrc(3.5, 3.4, f'{Vdc} V', 1.1, 1.2, .8),
             dev(4.8, 4.7, 'S4', None, 1.0), dev(7.4, 4.7, 'S2', None, 1.0)]
    return spec(k, 'Inverter<br>Bridges &amp;<br>Voltage Control', HOOK[k],
                f'Fundamental peak = {S("4V<sub>dc</sub>/π", "gold")},<br>1.27 V<sub>dc</sub>: {S("more", "cyan")} than V<sub>dc</sub>',
                'Square-wave full bridge', svg(c), parts,
                [chip('left', 300, 'c', f'V<sub>dc</sub> = {Vdc} V'), chip('left', 364, 'c', f'R = {R} Ω, 50 Hz'), chip('left', 428, 'c', f'THD = {THD * 100:.1f} %'),
                 chip('right', 290, 'g', f'V<sub>1,pk</sub> = {f(V1pk)} V'), chip('right', 538, 'c', f'V<sub>1</sub> = {f(V1)} V rms', False)],
                f'V<sub>1,pk</sub> = 4 × {Vdc} ÷ π = <b class="gl">{f(V1pk)} V</b>, V<sub>1</sub> = {f(V1)} V rms<br>'
                f'P<sub>1</sub> = {f(V1)}² ÷ {R} = <b class="cl">{P1:.1f} W</b> of {P:.0f} W', SMALL)


# ---------------------------------------------------------------- 4.5, worked example: space vector dwell times in sector 1
def u4L2():
    k = 'ee-pe-u4-L2'
    Vdc, fs, Vm, th = 600, 6e3, 300, 20
    Ts = 1 / fs * 1e6                                   # 166.7 us
    m = sq3 * Vm / Vdc                                  # 0.866
    lim = Vdc / sq3                                     # 346.4 V
    Tx = m * Ts * math.sin(rad(60 - th)); Ty = m * Ts * math.sin(rad(th)); T0 = Ts - Tx - Ty
    la, lb, lc = Tx + Ty + T0 / 2, Ty + T0 / 2, T0 / 2
    assert (f(m, 3), f(lim, 1), f(Tx, 1), f(Ty, 1), f(T0, 1), f(la, 1), f(lb, 1), f(lc, 1)) == ('0.866', '346.4', '92.8', '49.4', '24.5', '154.4', '61.6', '12.3')
    cx, cy, Rh = 112, 80, 56                            # hexagon vertex = 2Vdc/3 = 400 V
    sc = Rh / (2 * Vdc / 3)
    hexp = ' '.join(f'{cx + Rh * math.cos(rad(60 * i)):.1f},{cy - Rh * math.sin(rad(60 * i)):.1f}' for i in range(6))
    c = f'<polygon points="{hexp}" fill="{CY}" fill-opacity=".06" stroke="{CY}" stroke-width="2"/>'
    c += f'<circle cx="{cx}" cy="{cy}" r="{lim * sc:.1f}" fill="none" stroke="{GO}" stroke-width="2" stroke-dasharray="5 4"/>'
    rx_, ry_ = cx + Vm * sc * math.cos(rad(th)), cy - Vm * sc * math.sin(rad(th))
    c += T.arrow(cx, cy, rx_, ry_, GO, 3.2)
    for i, nm in ((0, 'V1 (100)'), (1, 'V2 (110)')):
        vx, vy = cx + Rh * math.cos(rad(60 * i)), cy - Rh * math.sin(rad(60 * i))
        c += f'<circle cx="{vx:.1f}" cy="{vy:.1f}" r="4" fill="{CY}"/><text x="{vx + 8:.1f}" y="{vy + (5 if i == 0 else -2):.1f}" class="ax" fill="{CY}">{nm}</text>'
    c += f'<text x="{cx - 60}" y="18" class="pt" fill="{GO}">limit {f(lim, 1)} V</text>'
    c += ax(cx, 140, f'{Vm} V at {th}°', col=GO)
    c += ttl(352, f'leg on-times in {f(Ts, 1)} µs', CY)
    c += hbars(244, 34, [('leg a', la, GO, f'{f(la, 1)} µs'), ('leg b', lb, CY, f'{f(lb, 1)} µs'), ('leg c', lc, AX, f'{f(lc, 1)} µs')],
               Ts, 84, h=20, gap=10, lw=56)
    o, top, bot, ym = legs3([4.3, 5.6, 6.9], 1.3, 3.5, [''] * 6)
    parts = o + [trace([(4.3, 1.3), (3.3, 1.3), (3.3, 3.5), (4.3, 3.5)]),
                 dcsrc(3.3, 2.4, f'{Vdc} V', 1.2, 1.5)] + top + bot + [
                 cable(4.3, ym, .05, 4.6, 5.4, .45, '#E06666', 3.5, .8), cable(5.6, ym, .05, 5.9, 5.4, .45, '#F6D285', 3.5, .8),
                 cable(6.9, ym, .05, 7.2, 5.4, .45, '#7FB2E5', 3.5, .8)]
    for x, nm in ((4.6, 'a'), (5.9, 'b'), (7.2, 'c')):
        parts += [cyl_at(x, 5.4, 9, 5, 18, '#8C98A6', '#C9D2DA'), lab(x, 5.4, .45, nm, WH, 17, dy=-10)]
    return spec(k, 'PWM<br>Techniques for<br>Inverters', HOOK[k],
                f'SVM stays linear up to {S("V<sub>dc</sub>/√3", "gold")}:<br>{S("346.4 V", "cyan")} on a 600 V bus',
                'SVM, sector 1 at θ = 20°', svg(c), parts,
                [chip('left', 300, 'c', f'V<sub>dc</sub> = {Vdc} V, 6 kHz'), chip('left', 364, 'c', f'V<sub>m</sub> = {Vm} V'), chip('left', 428, 'g', f'm = {f(m, 3)}'),
                 chip('right', 290, 'g', f'limit {f(lim, 1)} V'), chip('right', 538, 'c', f'T<sub>0</sub> = {f(T0, 1)} µs', False)],
                f'm = √3 × {Vm} ÷ {Vdc} = <b class="gl">{f(m, 3)}</b>, below the {f(lim, 1)} V limit<br>'
                f'T<sub>x</sub> = {f(Tx, 1)}, T<sub>y</sub> = {f(Ty, 1)}, T<sub>0</sub> = <b class="cl">{f(T0, 1)} µs</b>', SMALL)


# ---------------------------------------------------------------- 4.8, worked example: three-level NPC leg on 600 V
def u4L3():
    k = 'ee-pe-u4-L3'
    Vdc, m = 600, 3
    dV = Vdc / (m - 1)                                  # 300 V
    pole = [Vdc / 2 - j * dV for j in range(m)]         # +300, 0, -300
    lines = 2 * m - 1                                   # 5
    line_lv = [Vdc - j * dV for j in range(lines)]      # +600 ... -600
    dV5 = Vdc / 4; sw5, dio5, cap5 = 2 * 4, 4 * 3, 4
    assert dV == 300 and lines == 5 and (dV5, sw5, dio5, cap5) == (150, 8, 12, 4)
    c = ''
    for x0, title, lv, col in ((20, 'pole levels', pole, GO), (250, 'line levels', line_lv, CY)):
        c += ttl(x0 + 100, title, col)
        top, bot = 34, 126
        span = max(lv) - min(lv)
        for v in lv:
            y = top + (max(lv) - v) / span * (bot - top) if span else top
            c += f'<rect x="{x0 + 60}" y="{y - 4:.1f}" width="120" height="8" rx="4" fill="{col}" opacity=".85"/>'
            c += ax(x0 + 52, y + 5, f'{"+" if v > 0 else ""}{f(v, 0)} V', 'end')
        c += line(x0 + 60, top, x0 + 60, bot, col, 2) + line(x0 + 180, top, x0 + 180, bot, col, 2)
    X = 6.6
    parts = [trace([(4.4, .55), (X, .55), (X, 5.45), (4.4, 5.45), (4.4, .55)]),
             trace([(4.4, 2.95), (5.5, 2.95)]), trace([(5.5, 2.95), (5.5, 1.75), (X, 1.75)]), trace([(5.5, 2.95), (5.5, 4.15), (X, 4.15)]),
             trace([(X, 2.95), (7.9, 2.95)]),
             flow([(X, 2.95), (7.9, 2.95)], GO),
             capcan(4.4, 1.7, 'C1 300 V', 62, WH, 22),
             dev(X, 1.15, 'S1', GO, .8), dev(X, 2.3, 'S2', GO, .8),
             diode(5.5, 2.35, 'D1', 'y', CY),
             capcan(4.4, 4.2, 'C2 300 V', 62, WH, 22),
             diode(5.5, 3.55, 'D2', 'y', CY),
             dev(X, 3.6, 'S3', GO, .8), dev(X, 4.75, 'S4', GO, .8),
             lab(7.9, 2.95, .05, 'pole', GO, 16, dx=10, anchor='start'),
             lab(4.4, 2.95, .05, 'N', WH, 16, dx=-14, anchor='end')]
    return spec(k, 'Multilevel,<br>CSI &amp; Grid-tied<br>Inverters', HOOK[k],
                f'Each NPC switch blocks {S("V<sub>dc</sub>/2", "gold")}:<br>300 V, not the full {S("600 V", "cyan")}',
                'Three-level NPC on 600 V', svg(c), parts,
                [chip('left', 300, 'c', f'V<sub>dc</sub> = {Vdc} V'), chip('left', 364, 'c', '2 caps × 300 V'), chip('left', 428, 'c', '4 switches, 2 diodes'),
                 chip('right', 290, 'g', f'each blocks {g(dV)} V'), chip('right', 538, 'c', f'{lines} line levels', False)],
                f'ΔV = {Vdc} ÷ ({m} − 1) = <b class="gl">{g(dV)} V</b> per switch<br>'
                f'pole ±300 V and 0; line 2m − 1 = <b class="cl">{lines} levels</b>', SMALL)


# ---------------------------------------------------------------- 5.2, worked example 2: the dimmer's R-C and DIAC trigger
def u5L1():
    k = 'ee-pe-u5-L1'
    Vs, f0, R, C, Vbo = 230, 50, 100e3, .1e-6, 30
    Xc = 1 / (2 * pi * f0 * C)                                   # 31.83 kohm
    lag = deg(math.atan(R / Xc))                                 # 72.3 deg
    vc = Vs * Xc / math.hypot(R, Xc); vpk = vc * sq2             # 69.8 V rms, 98.7 V peak
    extra = deg(math.asin(Vbo / vpk))                            # 17.7 deg
    alpha = lag + extra                                          # 90.0 deg
    R2_ = 10e3
    lag2 = deg(math.atan(R2_ / Xc)); vpk2 = Vs * Xc / math.hypot(R2_, Xc) * sq2
    alpha2 = lag2 + deg(math.asin(Vbo / vpk2))                   # 23.0 deg
    assert (f(Xc / 1e3), f(lag, 1), f(vc, 1), f(vpk, 1), f(extra, 1), f(alpha, 1), f(alpha2, 1)) == ('31.83', '72.3', '69.8', '98.7', '17.7', '90.0', '23.0')
    Vm = Vs * sq2
    x0, x1, y0, y1 = 44, 240, 30, 126
    lo, hi = -Vm, Vm
    mid = (y0 + y1) / 2
    X = lambda d: x0 + (x1 - x0) * d / 360
    Y = lambda v: y1 - (v - lo) / (hi - lo) * (y1 - y0)
    c = line(x0, y0, x0, y1) + line(x0, mid, x1, mid)
    for seg in plot(x0, x1, y0, y1, lambda t: Vm * math.sin(t), 0, 2 * pi, lo, hi):
        c += f'<polyline points="{" ".join(f"{p:.1f},{q:.1f}" for p, q in seg)}" fill="none" stroke="{AX}" stroke-width="1.6" stroke-dasharray="4 4"/>'
    for seg in plot(x0, x1, y0, y1, lambda t: vpk * math.sin(t - rad(lag)), 0, 2 * pi, lo, hi):
        c += curve(seg, CY, 3)
    c += line(x0, Y(Vbo), x1, Y(Vbo), GO, 1.3, '3 3') + line(x0, Y(-Vbo), x1, Y(-Vbo), GO, 1.3, '3 3')
    c += f'<circle cx="{X(alpha):.1f}" cy="{Y(Vbo):.1f}" r="5.5" fill="{GO}"/>'
    c += f'<circle cx="{X(alpha + 180):.1f}" cy="{Y(-Vbo):.1f}" r="5.5" fill="{GO}"/>'
    c += ax(X(alpha), y1 + 14, f'α = {f(alpha, 1)}°', col=GO) + ax(x0 - 4, Y(Vbo) + 4, '±30', 'end', GO)
    c += f'<text x="{X(150):.1f}" y="{Y(vpk) - 6:.1f}" class="pt" fill="{CY}">v{sb("C")} lags {f(lag, 1)}°</text>'
    c += ttl(150, 'supply and capacitor voltage', WH)
    c += ttl(366, 'firing angle', GO)
    c += hbars(264, 44, [('100 kΩ', alpha, GO, f'{f(alpha, 1)}°'), ('10 kΩ', alpha2, CY, f'{f(alpha2, 1)}°')], 90, 80, h=24, gap=18, lw=58)
    parts = [trace(R2), trace([(7.6, 2.2), (5.4, 2.2), (5.4, 5.0), (7.6, 5.0)]), trace([(5.4, 3.6), (7.6, 3.6)], GO, 2.5),
             flow([(6.0, 1.4), (7.6, 1.4), (7.6, 5.6), (3.4, 5.6), (3.4, 4.2)]),
             lamp(5.0, 1.4, '529 Ω lamp', bright=.6),
             res(5.4, 2.8, '100 kΩ', 'y', CY, 1.1),
             acsrc(3.4, 3.2, f'{Vs} V', r=34, h=50),
             capcan(5.4, 4.45, '0.1 µF', 56, CY, 22),
             diode(6.5, 3.6, 'DIAC', 'x', GO),
             dev(7.6, 4.3, 'TRIAC', GO, 1.3)]
    return spec(k, 'Single-phase<br>AC Voltage<br>Controllers', HOOK[k],
                f'A + pulse fires {S("Q1", "gold")} when MT2 is +,<br>but {S("Q4", "cyan")} when MT2 is −',
                'R-C and DIAC trigger', svg(c), parts,
                [chip('left', 300, 'c', 'R = 100 kΩ, C = 0.1 µF'), chip('left', 364, 'g', f'DIAC V<sub>BO</sub> = {Vbo} V'),
                 chip('left', 428, 'c', f'X<sub>C</sub> = {f(Xc / 1e3)} kΩ'),
                 chip('right', 290, 'g', f'α = {f(alpha, 1)}°'), chip('right', 538, 'c', f'10 kΩ: α = {f(alpha2, 1)}°', False)],
                f'lag = tan<sup>−1</sup>(100 ÷ {f(Xc / 1e3)}) = <b class="cl">{f(lag, 1)}°</b>, v<sub>C</sub> peak {f(vpk, 1)} V<br>'
                f'30 V reached {f(extra, 1)}° later: α = {f(lag, 1)}° + {f(extra, 1)}° = <b class="gl">{f(alpha, 1)}°</b>', SMALL)


# ---------------------------------------------------------------- 5.4, worked example: PWM AC chopper at D = 0.6
def u5L2():
    k = 'ee-pe-u5-L2'
    Vs, R, fsw, D = 230, 50, 10e3, .6
    T = 1 / fsw; ton = D * T
    Vo = Vs * math.sqrt(D); P = Vo ** 2 / R
    V1 = D * Vs; P1 = V1 ** 2 / R; Psb = P - P1
    fsb = fsw - 50
    assert (round(ton * 1e6), f(Vo, 1), f(P, 1), f(V1, 1), f(P1, 1), f(Psb, 1), fsb) == (60, '178.2', '634.8', '138.0', '380.9', '253.9', 9950)
    x0, x1, y0, y1 = 44, 236, 34, 116
    c = ttl(140, 'switch S1: one period', GO) + line(x0, y0, x0, y1) + line(x0, y1, x1, y1)
    for seg in plot(x0, x1, y0, y1, lambda t: 1 if (t % T) < ton else 0, 0, 2 * T, 0, 1.15, 800):
        c += curve(seg, GO, 3, GO, y1, .14)
    xo = x0 + (x1 - x0) * ton / (2 * T)
    c += ax((x0 + xo) / 2, 136, f'on {round(ton * 1e6)} µs', col=GO) + ax(xo + (x1 - x0) * .1, 136, f'{round((T - ton) * 1e6)} µs off') + ax(x1, 136, '', 'end')
    c += ax(x0 - 4, y0 + 18, 'on', 'end') + ax(x0 - 4, y1, 'off', 'end')
    c += ttl(352, 'rms output vs fundamental', CY)
    c += vbars(262, 120, [('V' + sb('s'), Vs, AX, f'{Vs}'), ('V' + sb('o') + ' rms', Vo, GO, f'{f(Vo, 1)}'), ('V' + sb('1'), V1, CY, f'{f(V1, 1)}')],
               Vs, 66, bw=50, gap=24)
    parts = [trace(R2), trace([(6.4, 1.4), (6.4, 5.6)]),
             flow([(5.0, 1.4), (7.6, 1.4), (7.6, 5.6), (3.4, 5.6), (3.4, 1.4), (3.8, 1.4)]),
             acsrc(4.2, 1.4, f'{Vs} V'),
             dev(5.4, 1.4, 'S1', GO, 1.1),
             dev(6.4, 3.6, 'S2', None, 1.1),
             res(7.6, 3.6, f'{R} Ω', 'y', WH, 1.7)]
    return spec(k, 'Three-phase<br>&amp; PWM AC<br>Controllers', HOOK[k],
                f'Rms output is {S("√D", "gold")}·V<sub>s</sub> = 178.2 V —<br>D·V<sub>s</sub> is only the {S("fundamental", "cyan")}',
                'PWM AC chopper, D = 0.6', svg(c), parts,
                [chip('left', 300, 'c', f'{Vs} V, 50 Hz'), chip('left', 364, 'g', f'D = {D}, 10 kHz'), chip('left', 428, 'c', f'R = {R} Ω'),
                 chip('right', 290, 'g', f'V<sub>o</sub> = {f(Vo, 1)} V rms'), chip('right', 538, 'c', f'V<sub>1</sub> = {f(V1, 1)} V', False)],
                f'V<sub>o</sub> = {Vs} × √{D} = <b class="gl">{f(Vo, 1)} V</b>, P = {f(P, 1)} W<br>'
                f'V<sub>1</sub> = {D} × {Vs} = <b class="cl">{f(V1, 1)} V</b>, carrying {f(P1, 1)} W')


# ---------------------------------------------------------------- 5.6, worked example 2: matrix converter duty cycles for output A
def u5L3():
    k = 'ee-pe-u5-L3'
    VL, Ts, vA = 415, 100, 100
    va, vb = 338.9, -169.4                                      # book: v_a peak 338.9 V, v_b = v_c = -169.4 V
    dAa = (vA - vb) / (va - vb); dAb = (1 - dAa) / 2            # 0.530, 0.235
    tAa, tAb = dAa * Ts, dAb * Ts
    assert (f(va, 1), f(vb, 1), f(dAa, 3), f(dAb, 3), f(tAa, 1), f(tAb, 1)) == ('338.9', '−169.4', '0.530', '0.235', '53.0', '23.5')
    x0, x1, y0, y1 = 44, 236, 34, 120
    lo, hi = -200, 360
    Y = lambda v: y1 - (v - lo) / (hi - lo) * (y1 - y0)
    c = ttl(140, 'output A over 100 µs', GO) + line(x0, y0, x0, y1) + line(x0, Y(0), x1, Y(0))
    for seg in plot(x0, x1, y0, y1, lambda t: va if t < tAa else vb, 0, Ts, lo, hi, 600):
        c += curve(seg, GO, 3, GO, Y(0), .14)
    c += line(x0, Y(vA), x1, Y(vA), CY, 1.6, '5 4') + f'<text x="{x1:.1f}" y="{Y(vA) - 6:.1f}" text-anchor="end" class="pt" fill="{CY}">average {vA} V</text>'
    c += ax(x0 - 4, Y(va) + 5, f'{f(va, 1)}', 'end', GO) + ax(x0 - 4, Y(vb) + 5, f'{f(vb, 1)}', 'end')
    c += ax(x0 + (x1 - x0) * dAa / 2, 136, f'a: {f(tAa, 1)} µs', col=GO) + ax(x0 + (x1 - x0) * (dAa + 1) / 2, 136, f'b, c: {f(2 * tAb, 1)} µs')
    c += ttl(352, 'one switch at a time', CY)
    bx, bw = 262, 186
    for j, (nm, t, col) in enumerate((('S' + sb('Aa'), tAa, GO), ('S' + sb('Ab'), tAb, CY), ('S' + sb('Ac'), tAb, '#7FB2E5'))):
        xs = bx + bw * sum([tAa, tAb, tAb][:j]) / Ts
        c += f'<rect x="{xs:.1f}" y="52" width="{bw * t / Ts - 2:.1f}" height="30" rx="4" fill="{col}" opacity=".85"/>'
        c += f'<text x="{xs + bw * t / Ts / 2:.1f}" y="72" text-anchor="middle" class="pt" fill="#10202A">{f(t, 1)}</text>'
        c += ax(xs + bw * t / Ts / 2, 102, nm)
    c += ax(bx, 124, '0', 'start') + ax(bx + bw, 124, f'{Ts} µs', 'end')
    xs_, ys_ = (4.8, 6.0, 7.2), (1.6, 2.8, 4.0)
    parts = [trace([(3.8, y), (7.7, y)]) for y in ys_] + [trace([(x, 1.0), (x, 5.0)]) for x in xs_]
    parts += [flow([(3.8, 1.6), (4.8, 1.6), (4.8, 5.0)], GO)]
    for y, nm in zip(ys_, 'abc'):
        parts.append(lab(3.7, y, .05, nm, WH, 18, dx=-6, anchor='end'))
    for iy, y in enumerate(ys_):
        for ix, x in enumerate(xs_):
            col = (GO if iy == 0 else CY) if ix == 0 else None
            parts.append(dev(x, y, ('A' + 'abc'[iy]) if ix == 0 else '', col, .75))
    for x, nm in zip(xs_, 'ABC'):
        parts += [cyl_at(x, 5.2, 9, 5, 16, '#8C98A6', '#C9D2DA'), lab(x, 5.2, .5, nm, GO if nm == 'A' else WH, 18, dy=-10)]
    return spec(k, 'Cycloconverters<br>&amp; Matrix<br>Converters', HOOK[k],
                f'One switch per output at a {S("time", "gold")}:<br>two at once {S("short", "cyan")} two inputs',
                'Matrix converter, output A', svg(c), parts,
                [chip('left', 300, 'g', f'v<sub>a</sub> = {f(va, 1)} V'), chip('left', 364, 'c', f'v<sub>b</sub> = v<sub>c</sub> = {f(vb, 1)} V'),
                 chip('left', 428, 'c', '10 kHz: 100 µs'),
                 chip('right', 290, 'g', f'd<sub>Aa</sub> = {f(dAa, 3)}'), chip('right', 538, 'c', f'd<sub>Ab</sub> = d<sub>Ac</sub> = {f(dAb, 3)}', False)],
                f'100 = d<sub>Aa</sub> × 338.9 + (1 − d<sub>Aa</sub>)(−169.4) → <b class="gl">d<sub>Aa</sub> = {f(dAa, 3)}</b><br>'
                f'{f(tAa, 1)} + {f(tAb, 1)} + {f(tAb, 1)} = <b class="cl">{Ts} µs</b>: output A never open', SMALL)


# ---------------------------------------------------------------- 6.1, worked example: on-line UPS backup time
def u6L1():
    k = 'ee-pe-u6-L1'
    Srate, P, pf, Vb, Ah, eta, dod = 1000, 640, .8, 48, 100, .9, .8
    S_ = P / pf; Pdc = P / eta; I = Pdc / Vb; E = Vb * Ah * dod; t = E / Pdc
    assert (S_, f(Pdc, 1), f(I, 1), E, f(t, 2)) == (800, '711.1', '14.8', 3840, '5.40')
    c = ttl(116, 'power drawn', CY)
    c += hbars(0, 44, [('load', P, GO, f'{P} W'), ('battery DC', Pdc, CY, f'{f(Pdc, 1)} W')], Pdc, 84, h=24, gap=18, lw=82)
    c += ttl(360, 'battery energy', GO)
    c += vbars(286, 122, [('48 × 100', Vb * Ah, AX, f'{Vb * Ah} Wh'), ('80 % usable', E, GO, f'{E:.0f} Wh')], Vb * Ah, 68, bw=58, gap=40)
    parts = [trace([(5.6, 5.0), (5.6, 2.8), (6.6, 2.8)], GO, 4), trace([(6.6, 2.8), (8.2, 2.8), (8.2, 4.8)], CY, 4),
             flow([(5.6, 4.2), (5.6, 2.8), (6.0, 2.8)], GO), flow([(7.3, 2.8), (8.2, 2.8), (8.2, 4.2)]),
             battery(5.6, 5.0, '48 V', 1.5, 1.2, 1.0),
             lab(5.6, 5.0, 1.0, '100 Ah', WH, 15, dy=-24),
             block(6.6, 2.8, 1.4, 1.4, 1.7, 'UPS', '#3A4652', '#222B33', '#2C3640', GO, 18, '1 kVA'),
             block(8.2, 4.8, 1.0, 1.0, 1.0, '640 W', '#2F3A45', '#151B21', '#1F262E', WH, 15),
             lab(8.2, 4.8, 1.0, 'load', '#9FB2C6', 13, dy=24)]
    return spec(k, 'UPS, Chargers<br>&amp; Induction<br>Heating', HOOK[k],
                f'Backup = {S("usable", "gold")} Wh ÷ battery<br>{S("DC", "cyan")} watts: 5.4 h here',
                '1 kVA UPS on a 640 W load', svg(c), parts,
                [chip('left', 300, 'c', f'{Vb} V, {Ah} Ah battery'), chip('left', 364, 'c', f'inverter η = {eta * 100:.0f} %'),
                 chip('left', 428, 'g', f'{dod * 100:.0f} % usable: {E:.0f} Wh'),
                 chip('right', 290, 'c', f'{f(I, 1)} A from the battery'), chip('right', 538, 'g', f'{f(t, 2)} h backup', False)],
                f'P<sub>dc</sub> = {P} ÷ {eta} = <b class="cl">{f(Pdc, 1)} W</b>; I = {f(Pdc, 1)} ÷ {Vb} = {f(I, 1)} A<br>'
                f't = {Vb} × {Ah} × {dod} ÷ {f(Pdc, 1)} = <b class="gl">{f(t, 2)} h</b>, about 5 h 24 min')


# ---------------------------------------------------------------- 6.4, worked example: a ±500 kV, 2000 MW bipolar link
def u6L2():
    k = 'ee-pe-u6-L2'
    Vp, Pw = 500e3, 2000e6
    Vd = 2 * Vp; Id = Pw / Vd; Pmono = Vp * Id; Q50 = .5 * (Pw / 2); Qfull = .5 * Pw
    assert (Id, Pmono / 1e6, Q50 / 1e6, Qfull / 1e6) == (2000, 1000, 500, 1000)
    c = ttl(116, 'power delivered', GO)
    c += vbars(36, 122, [('bipolar', Pw / 1e6, GO, f'{Pw / 1e6:.0f} MW'), ('one pole', Pmono / 1e6, CY, f'{Pmono / 1e6:.0f} MW')], Pw / 1e6, 68, bw=60, gap=44)
    c += ttl(356, 'vars per station', CY)
    c += vbars(276, 122, [('at 50 %', Q50 / 1e6, CY, f'{Q50 / 1e6:.0f} MVAr'), ('at 100 %', Qfull / 1e6, AX, f'{Qfull / 1e6:.0f} MVAr')],
               Qfull / 1e6, 68, bw=60, gap=44)
    A, Bs = (5.1, 5.1), (8.2, 2.0)
    tw = [(6.2, 4.0), (7.25, 2.95)]
    def wire(dz, col):
        pts_ = [P(A[0] + .45, A[1] - .45, .9)] + [P(x, y, 1.6 + dz) for x, y in tw] + [P(Bs[0] - .45, Bs[1] + .45, .9)]
        return f'<polyline points="{pts(*pts_)}" fill="none" stroke="{col}" stroke-width="3.5" stroke-linejoin="round"/>'
    parts = [f'<polyline points="{pts(P(A[0], A[1], .02), P(Bs[0], Bs[1], .02))}" fill="none" stroke="{AX}" stroke-width="2.5" stroke-dasharray="7 6"/>',
             lab(6.7, 3.5, .02, 'ground return', '#9FB2C6', 13, dy=20),
             block(A[0], A[1], 1.2, 1.2, .9, 'station', '#3A4652', '#222B33', '#2C3640', WH, 14)]
    for x, y in tw:
        parts.append(tower(x, y, 1.9))
    parts += [wire(.25, GO), wire(-.25, CY),
              lab(5.65, 4.55, 1.5, '+500 kV', GO, 16, dy=-12), lab(6.75, 3.45, 1.35, '−500 kV', CY, 16, dy=26),
              block(Bs[0], Bs[1], 1.2, 1.2, .9, 'station', '#3A4652', '#222B33', '#2C3640', WH, 14)]
    return spec(k, 'HVDC &amp;<br>Static VAR<br>Compensators', HOOK[k],
                f'Divide by the {S("pole-to-pole", "gold")} 1000 kV:<br>{S("2000 A", "cyan")} in each pole',
                '±500 kV bipolar, 2000 MW', svg(c), parts,
                [chip('left', 300, 'c', '±500 kV bipolar'), chip('left', 364, 'c', '2000 MW'), chip('left', 428, 'g', 'V<sub>d</sub> = 1000 kV'),
                 chip('right', 290, 'g', f'I<sub>d</sub> = {Id:.0f} A per pole'), chip('right', 538, 'c', f'one pole: {Pmono / 1e6:.0f} MW', False)],
                f'I<sub>d</sub> = 2000 MW ÷ 1000 kV = <b class="gl">{Id:.0f} A</b> per pole<br>'
                f'one pole: 500 kV × 2000 A = <b class="cl">{Pmono / 1e6:.0f} MW</b>')


# ---------------------------------------------------------------- 6.6, worked example: sizing a home solar array and battery
def u6L3():
    k = 'ee-pe-u6-L3'
    load, psh, lf, eta, Wp1, Vb, days, dod, rt = 4000, 4.5, .75, .9, 335, 48, 2, .6, .9
    dc = load / eta                                      # 4444.4 Wh
    arr = dc / (psh * lf)                                # 1316.9 Wp
    n = math.ceil(arr / Wp1)                             # 4 panels
    store = dc * days / (dod * rt)                       # 16460.9 Wh
    Ah = store / Vb                                      # 342.9 Ah
    assert (f(dc, 1), f(arr, 1), n, n * Wp1, f(store, 1), f(Ah, 1)) == ('4444.4', '1316.9', 4, 1340, '16460.9', '342.9')
    c = ttl(118, 'battery at 48 V', GO)
    c += hbars(0, 34, [('needed', Ah, GO, f'{f(Ah, 1)} Ah'), ('300 Ah', 300, AX, 'too small'), ('choose', 350, CY, '350 Ah')], 350, 70, h=20, gap=10, lw=64)
    c += ttl(360, 'solar array', CY)
    c += vbars(290, 122, [('needed', arr, CY, f'{f(arr, 1)}'), (f'{n} × {Wp1}', n * Wp1, GO, f'{n * Wp1} Wp')], n * Wp1, 66, bw=56, gap=36)
    parts = [trace([(6.8, 3.4), (5.8, 3.4), (5.8, 3.0)], CY, 3.5), trace([(5.8, 3.0), (5.8, 4.4), (7.3, 4.4), (7.3, 5.4)], GO, 3.5),
             trace([(5.8, 4.4), (5.8, 5.6), (5.2, 5.6)], WH, 3)]
    for x, y in ((6.8, 1.5), (8.0, 1.5), (6.8, 2.8), (8.0, 2.8)):
        parts.append(panel(x, y, 1.1, .9))
    parts += [lab(9.3, 3.9, 0, f'{n} × {Wp1} Wp', CY, 15, dy=14, anchor='start'),
              block(5.8, 3.0, .8, .8, .8, 'inverter', '#3A4652', '#222B33', '#2C3640', WH, 12),
              house(5.2, 5.6, '4 kWh/day'),
              battery(7.3, 5.4, '48 V', 1.2, 1.0, .8)]
    return spec(k, 'Solar, Storage<br>&amp; Process<br>Control', HOOK[k],
                f'Size for {S("2 days", "gold")} at 60 % DoD:<br>342.9 Ah, so choose {S("350 Ah", "cyan")}',
                'Home solar and battery', svg(c), parts,
                [chip('left', 300, 'c', '4 kWh a day, 4.5 sun h'), chip('left', 364, 'c', f'panels {Wp1} Wp'), chip('left', 428, 'g', '2 days, 60 % DoD'),
                 chip('right', 290, 'c', f'{f(arr, 1)} Wp → {n} panels'), chip('right', 538, 'g', f'{f(Ah, 1)} Ah at {Vb} V', False)],
                f'array = {f(dc, 1)} Wh ÷ 3.375 h = <b class="cl">{f(arr, 1)} Wp</b><br>'
                f'{f(dc, 1)} × 2 ÷ 0.54 ÷ 48 = <b class="gl">{f(Ah, 1)} Ah</b>', SMALL)


ORDER = ['u1L1', 'u1L2', 'u1L3', 'u2L1', 'u2L2', 'u2L3', 'u2L4', 'u2L5', 'u3L1', 'u3L2', 'u3L3', 'u3L4',
         'u4L1', 'u4L2', 'u4L3', 'u5L1', 'u5L2', 'u5L3', 'u6L1', 'u6L2', 'u6L3']


def specs():
    only = os.environ.get('ONLY')
    return [globals()[n]() for n in ORDER if n in globals() and (not only or n in only.split(','))]
