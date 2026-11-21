"""Drawing helpers for the ec-circuits t16 specs: isometric parts for the board and small plots for the card.
Board units: the slab is 8 x 8; P(x, y, z) maps to the page (x runs right-down, y left-down, z up)."""
import math, os, sys
TOOL = os.environ.get('T16_TOOL', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tool'))
sys.path.insert(0, os.path.abspath(TOOL))
import t16_split as T
B = T.B
P, pts = B.P, B.pts
GO, CY, CU = '#E8B84A', '#3FE0E6', '#C98A4B'
INK = '#0D1F37'


def g(v, n=4):
    """a number the way the book prints it: up to n significant figures, no trailing zeros"""
    return f'{float(f"{v:.{n}g}"):g}'.replace('-', '−')


def setup(oy=300, ox=1012, u=33):
    B.U, B.OX, B.OY = u, ox, oy
    return (ox, oy), u


# ---------------------------------------------------------------- board parts (each returns SVG)
def lab(x, y, z, text, col='#F1F4F7', size=15, anchor='middle'):
    px, py = P(x, y, z)
    return (f'<text x="{px:.1f}" y="{py:.1f}" text-anchor="{anchor}" class="capl" '
            f'style="font-size:{size}px;paint-order:stroke;stroke:{INK};stroke-width:5px;stroke-linejoin:round" fill="{col}">{text}</text>')


def wire(path, col=CU, w=3, z=.02, op=.95):
    return f'<polyline points="{pts(*[P(a, b, z) for a, b in path])}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round" opacity="{op}"/>'


def chevron(x1, y1, x2, y2, col, s=7):
    a = math.atan2(y2 - y1, x2 - x1); mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    p1 = (mx - s * math.cos(a) + s * .8 * math.sin(a), my - s * math.sin(a) - s * .8 * math.cos(a))
    p2 = (mx - s * math.cos(a) - s * .8 * math.sin(a), my - s * math.sin(a) + s * .8 * math.cos(a))
    return f'<polyline points="{p1[0]:.1f},{p1[1]:.1f} {mx:.1f},{my:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="{col}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'


def glow(path, col=CY, w=4.5, z=.03, arrows=True, dash=None):
    pl = [P(a, b, z) for a, b in path]
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s = f'<g filter="url(#gl)"><polyline points="{pts(*pl)}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"{d}/></g>'
    if arrows:
        for (x1, y1), (x2, y2) in zip(pl, pl[1:]):
            if math.hypot(x2 - x1, y2 - y1) > 40:
                s += chevron(x1, y1, x2, y2, col)
    return s


def pad(x, y, col=CU):
    px, py = P(x, y)
    return f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="6" ry="3.5" fill="#1A222A" stroke="{col}" stroke-width="2"/>'


def post(x, y, name=None, col='#C9D3DB', h=14, ncol=GO):
    px, py = P(x, y)
    s = (f'<path d="M{px - 8:.1f},{py:.1f} V{py - h:.1f} A8,4.6 0 0 0 {px + 8:.1f},{py - h:.1f} V{py:.1f} A8,4.6 0 0 1 {px - 8:.1f},{py:.1f}Z" fill="#6E7C8A"/>'
         f'<ellipse cx="{px:.1f}" cy="{py - h:.1f}" rx="8" ry="4.6" fill="{col}"/>')
    if name:
        s += (f'<text x="{px:.1f}" y="{py - h - 10:.1f}" text-anchor="middle" class="capl" style="font-size:17px;paint-order:stroke;stroke:{INK};stroke-width:5px" fill="{ncol}">{name}</text>')
    return s


def res(x, y, axis='x', label='', L=1.8, w=.62, h=.62, body=('#D9C6A2', '#9A845E', '#B9A27C'), bands=('#8B3A2A', '#2A2A2A', '#C9A227'), lcol='#F1F4F7', lz=1.25, ldx=0, ldy=0):
    """a resistor block centred at (x, y), long along axis 'x' or 'y', with colour bands"""
    if axis == 'x':
        x0, y0, W, D = x - L / 2, y - w / 2, L, w
    else:
        x0, y0, W, D = x - w / 2, y - L / 2, w, L
    s = B.box(x0, y0, W, D, h, *body)
    for k, c in enumerate(bands):
        f = .28 + k * .16
        if axis == 'x':
            a, b = x0 + f * W, x0 + (f + .07) * W
            s += f'<polygon points="{pts(P(a, y0 + D, h), P(b, y0 + D, h), P(b, y0 + D, 0), P(a, y0 + D, 0))}" fill="{c}"/>'
            s += f'<polygon points="{pts(P(a, y0, h), P(b, y0, h), P(b, y0 + D, h), P(a, y0 + D, h))}" fill="{c}"/>'
        else:
            a, b = y0 + f * D, y0 + (f + .07) * D
            s += f'<polygon points="{pts(P(x0 + W, a, h), P(x0 + W, b, h), P(x0 + W, b, 0), P(x0 + W, a, 0))}" fill="{c}"/>'
            s += f'<polygon points="{pts(P(x0, a, h), P(x0 + W, a, h), P(x0 + W, b, h), P(x0, b, h))}" fill="{c}"/>'
    if label:
        s += lab(x + ldx, y + ldy, lz, label, lcol)
    return s


def vsrc(x, y, label='', w=1.2, d=1.0, h=.85, lcol='#F6D285', ac=False):
    """a voltage source block: dark box, + mark, its value on the top face (a sine mark when ac)"""
    s = B.box(x - w / 2, y - d / 2, w, d, h, '#3A4652', '#222B33', '#2C3640')
    px, py = P(x, y, h)
    if ac:
        s += f'<path d="M{px - 16:.1f},{py:.1f} q8,-12 16,0 t16,0" fill="none" stroke="{CY}" stroke-width="2.6"/>'
    else:
        s += f'<path d="M{px - 6:.1f},{py:.1f}h12M{px:.1f},{py - 6:.1f}v12" stroke="#F1F4F7" stroke-width="2.4"/>'
    if label:
        s += lab(x, y, h + .75, label, lcol, 16)
    return s


def isrc(x, y, label='', w=1.2, d=1.1, h=.9, lcol='#F6D285', diamond=False):
    """a current source: yellow block with an arrow; diamond=True marks a dependent source"""
    s = B.box(x - w / 2, y - d / 2, w, d, h, '#F2C94A', '#B88A10', '#C99A18')
    px, py = P(x, y, h)
    if diamond:
        s += f'<polygon points="{pts(P(x - .38, y, h), P(x, y - .38, h), P(x + .38, y, h), P(x, y + .38, h))}" fill="none" stroke="#3A2A04" stroke-width="2.6"/>'
    else:
        s += f'<path d="M{px + 12:.1f},{py + 6:.1f} L{px - 10:.1f},{py - 5:.1f} m0,0 l9,0 m-9,0 l3,7" stroke="#3A2A04" stroke-width="3.4" stroke-linecap="round" fill="none"/>'
    if label:
        s += lab(x, y, h + .75, label, lcol, 16)
    return s


def can(x, y, label='', rx=22, ry=12, h=70, lcol='#F1F4F7'):
    """an electrolytic capacitor can with its value written up the side"""
    cx, cy = P(x, y)
    s = (f'<path d="M{cx - rx:.1f},{cy:.1f} V{cy - h:.1f} A{rx},{ry} 0 0 0 {cx + rx:.1f},{cy - h:.1f} V{cy:.1f} A{rx},{ry} 0 0 1 {cx - rx:.1f},{cy:.1f}Z" fill="url(#can)"/>'
         f'<ellipse cx="{cx:.1f}" cy="{cy - h:.1f}" rx="{rx}" ry="{ry}" fill="url(#lid)"/>'
         f'<path d="M{cx - 9:.1f},{cy - h:.1f}H{cx + 9:.1f}M{cx:.1f},{cy - h - 5:.1f}V{cy - h + 5:.1f}" stroke="#6B7785" stroke-width="2"/>')
    if label:
        s += f'<text transform="translate({cx + 5:.1f} {cy - 10:.1f}) rotate(-90)" class="capl" style="font-size:14px" fill="{lcol}">{label}</text>'
    return s


def toroid(x, y, label='', R=40, r=15, z=.3, lcol='#F1F4F7', lz=1.4):
    tx, ty = P(x, y, z)
    Ry, ry = R * .56, r * .56
    s = (f'<ellipse cx="{tx:.1f}" cy="{ty + 8:.1f}" rx="{R}" ry="{Ry:.1f}" fill="#5A3414"/>'
         f'<ellipse cx="{tx:.1f}" cy="{ty:.1f}" rx="{R}" ry="{Ry:.1f}" fill="#B8692C"/>')
    wind = ''.join(f'<line x1="{tx + (r + 2) * math.cos(a):.1f}" y1="{ty + (ry + 1) * math.sin(a):.1f}" x2="{tx + (R - 1) * math.cos(a):.1f}" y2="{ty + (Ry - .5) * math.sin(a):.1f}"/>'
                   for a in [k * 2 * math.pi / 38 for k in range(38)])
    s += f'<g stroke="#E8A464" stroke-width="2.4" stroke-linecap="round">{wind}</g><ellipse cx="{tx:.1f}" cy="{ty:.1f}" rx="{r}" ry="{ry:.1f}" fill="#1A222A"/>'
    if label:
        s += lab(x, y, lz + z, label, lcol)
    return s


def solenoid(x, y, label='', rx=20, ry=11, h=74, turns=9, lcol='#F1F4F7', dot=None):
    """an upright coil on a former: copper windings round a cylinder; dot=True puts the dot mark on top"""
    cx, cy = P(x, y)
    s = (f'<path d="M{cx - rx:.1f},{cy:.1f} V{cy - h:.1f} A{rx},{ry} 0 0 0 {cx + rx:.1f},{cy - h:.1f} V{cy:.1f} A{rx},{ry} 0 0 1 {cx - rx:.1f},{cy:.1f}Z" fill="#7A4A22"/>')
    for k in range(turns):
        yy = cy - 8 - k * (h - 14) / (turns - 1)
        s += f'<path d="M{cx - rx:.1f},{yy:.1f} A{rx},{ry} 0 0 0 {cx + rx:.1f},{yy - 3:.1f}" fill="none" stroke="#E8A464" stroke-width="3.2"/>'
    s += f'<ellipse cx="{cx:.1f}" cy="{cy - h:.1f}" rx="{rx}" ry="{ry}" fill="#3A4652"/><ellipse cx="{cx:.1f}" cy="{cy - h:.1f}" rx="{rx - 8}" ry="{ry - 4.5}" fill="#1A222A"/>'
    if dot:
        s += f'<circle cx="{cx - rx - 10:.1f}" cy="{cy - h + 6:.1f}" r="6" fill="{dot}"/>'
    if label:
        s += f'<text x="{cx:.1f}" y="{cy + ry + 20:.1f}" text-anchor="middle" class="capl" style="font-size:16px;paint-order:stroke;stroke:{INK};stroke-width:5px" fill="{lcol}">{label}</text>'
    return s


def meter(x, y, name, w=1.3, d=1.2, h=.8, ncol=GO):
    """a meter block with a round dial on its top face and a needle"""
    s = B.box(x - w / 2, y - d / 2, w, d, h, '#DCE3EA', '#7E8B98', '#A3AFBB')
    px, py = P(x, y, h)
    s += (f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="17" ry="10" fill="#F7F9FB" stroke="#3A4652" stroke-width="2"/>'
          f'<line x1="{px:.1f}" y1="{py + 4:.1f}" x2="{px + 10:.1f}" y2="{py - 6:.1f}" stroke="#C0392B" stroke-width="2.4"/>')
    s += lab(x, y, h + .8, name, ncol, 17)
    return s


def block(x, y, w, d, h, label='', cols=('#4A5A6A', '#26313B', '#33404C'), lcol='#F1F4F7', lz=None, size=15):
    s = B.box(x - w / 2, y - d / 2, w, d, h, *cols)
    if label:
        s += lab(x, y, (lz if lz is not None else h + .6), label, lcol, size)
    return s


DEFS_EXTRA = ('<defs><linearGradient id="can" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1C2A3A"/><stop offset=".35" stop-color="#4F6A86"/><stop offset=".6" stop-color="#2E425A"/><stop offset="1" stop-color="#141E2A"/></linearGradient>'
              '<radialGradient id="lid" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#F1F4F7"/><stop offset="1" stop-color="#8C98A6"/></radialGradient></defs>')


def board(parts):
    """the slab with the parts on it, at the origin set by setup()"""
    return T.iso_board('eee', [DEFS_EXTRA] + parts, origin=(B.OX, B.OY), unit=B.U)


# ---------------------------------------------------------------- card plots (470 x 144 SVG)
AXC = '#6B7B8A'


def svg(inner):
    return f'<svg width="470" height="144" viewBox="0 0 470 144">{inner}</svg>'


class Frame:
    """a small plot: x0 is its left edge in the card, w its width; plot area from x0+44 to x0+w, y 34 to 118"""
    def __init__(self, x0, w, title, col, xmin, xmax, ymin, ymax, yt=None, yb=None, tx=None, zero_axis=False, top=34):
        self.x0, self.w, self.xmin, self.xmax, self.ymin, self.ymax = x0, w, xmin, xmax, ymin, ymax
        self.L, self.R, self.T, self.Bt = x0 + 44, x0 + w, top, 118
        s = f'<text x="{tx if tx is not None else x0 + (w + 44) / 2:.0f}" y="18" text-anchor="middle" class="pt" fill="{col}">{title}</text>'
        s += f'<line x1="{self.L}" y1="{self.T}" x2="{self.L}" y2="{self.Bt}" stroke="{AXC}" stroke-width="1.5"/>'
        ya = self.Y(0) if (zero_axis and ymin < 0 < ymax) else self.Bt
        s += f'<line x1="{self.L}" y1="{ya:.1f}" x2="{self.R}" y2="{ya:.1f}" stroke="{AXC}" stroke-width="1.5"/>'
        if yt is not None:
            s += f'<text x="{self.L - 6}" y="{self.T + 6}" text-anchor="end" class="ax">{yt}</text>'
        if yb is not None:
            s += f'<text x="{self.L - 6}" y="{self.Bt + 5}" text-anchor="end" class="ax">{yb}</text>'
        self.s = s

    def X(self, v):
        return self.L + (v - self.xmin) / (self.xmax - self.xmin) * (self.R - self.L)

    def Y(self, v):
        return self.Bt - (v - self.ymin) / (self.ymax - self.ymin) * (self.Bt - self.T)

    def line(self, xs, ys, col, w=3.2, fill=False, dash=None):
        p = ' '.join(f'{self.X(a):.1f},{self.Y(b):.1f}' for a, b in zip(xs, ys))
        d = f' stroke-dasharray="{dash}"' if dash else ''
        s = ''
        if fill:
            s += f'<polygon points="{self.X(xs[0]):.1f},{self.Bt} {p} {self.X(xs[-1]):.1f},{self.Bt}" fill="{col}" opacity=".14"/>'
        self.s += s + f'<polyline points="{p}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"{d}/>'

    def hline(self, v, col, dash='4 4', w=1.4, label=None, lx=None, anchor='end'):
        self.s += f'<line x1="{self.L}" y1="{self.Y(v):.1f}" x2="{self.R}" y2="{self.Y(v):.1f}" stroke="{col}" stroke-width="{w}" stroke-dasharray="{dash}"/>'
        if label:
            self.s += f'<text x="{lx if lx is not None else self.R - 2:.0f}" y="{self.Y(v) - 5:.1f}" text-anchor="{anchor}" class="ax" fill="{col}">{label}</text>'

    def vline(self, v, col, dash='4 4', y_to=None):
        y2 = self.Y(y_to) if y_to is not None else self.T
        self.s += f'<line x1="{self.X(v):.1f}" y1="{self.Bt}" x2="{self.X(v):.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="1.6" stroke-dasharray="{dash}"/>'

    def dot(self, x, y, col, r=4.5):
        self.s += f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="{r}" fill="{col}"/>'

    def xt(self, v, text, col='#C9D3DB', anchor='middle'):
        self.s += f'<text x="{self.X(v):.1f}" y="136" text-anchor="{anchor}" class="ax" fill="{col}">{text}</text>'

    def text(self, x, y, t, col, anchor='middle', cls='ax', dx=0, dy=0):
        self.s += f'<text x="{self.X(x) + dx:.1f}" y="{self.Y(y) + dy:.1f}" text-anchor="{anchor}" class="{cls}" fill="{col}">{t}</text>'


def bars(x0, w, title, tcol, items, vmax, top=34, unit='', vfmt=None, tx=None, base=118, gap=.32):
    """vertical bars: items = [(name, value, colour), ...]; value labels on top, names under the axis"""
    n = len(items)
    L, R = x0 + 8, x0 + w
    bw = (R - L) / n
    s = f'<text x="{tx if tx is not None else x0 + w / 2:.0f}" y="18" text-anchor="middle" class="pt" fill="{tcol}">{title}</text>'
    s += f'<line x1="{L}" y1="{base}" x2="{R}" y2="{base}" stroke="{AXC}" stroke-width="1.5"/>'
    for k, (name, v, c) in enumerate(items):
        hgt = v / vmax * (base - top - 18)
        x = L + k * bw + bw * gap / 2
        s += f'<rect x="{x:.1f}" y="{base - hgt:.1f}" width="{bw * (1 - gap):.1f}" height="{hgt:.1f}" rx="3" fill="{c}" opacity=".85"/>'
        s += f'<text x="{x + bw * (1 - gap) / 2:.1f}" y="{base - hgt - 6:.1f}" text-anchor="middle" class="pt" fill="{c}">{vfmt(v) if vfmt else g(v)}{unit}</text>'
        s += f'<text x="{x + bw * (1 - gap) / 2:.1f}" y="136" text-anchor="middle" class="ax">{name}</text>'
    return s


def matrix(x, y, rows, col='#E6ECF1', cw=46, rh=26, size=17, br=AXC):
    """a 2 x 2 (or n x m) matrix in brackets with its top-left at (x, y)"""
    nr, nc = len(rows), len(rows[0])
    W, H = nc * cw + 10, nr * rh + 6
    s = (f'<path d="M{x + 7},{y} h-7 v{H} h7 M{x + W - 7},{y} h7 v{H} h-7" fill="none" stroke="{br}" stroke-width="2"/>')
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            s += f'<text x="{x + 5 + cw * (j + .5):.1f}" y="{y + 3 + rh * (i + .5) + size * .36:.1f}" text-anchor="middle" style="font:600 {size}px \'IBM Plex Sans\'" fill="{col}">{v}</text>'
    return s, W


def chip(side, top, kind, text, pointer=True):
    return dict(side=side, top=top, kind=kind, text=text, pointer=pointer)
