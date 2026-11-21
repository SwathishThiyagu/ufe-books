"""t16 split blueprint thumbnails for VLSI Design (ec-vlsi), ECE look (indigo sheet, violet and mint accents).
One spec per lesson, each built from that lesson's own book worked example (books/ece/ec-vlsi/ec-vlsi-u<N>.html on main,
the chapters the lesson covers). Every number shown is computed below and checked against the book's answer with assert.
Build: python3 t16_split.py build specs.py <out dir>"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t16_split as T
B = T.B
P, pts, box, cyl, arrow = B.P, B.pts, B.box, T.cyl, T.arrow
D = 'ece'
VI, MI = T.DEPTS[D]['acc'], T.DEPTS[D]['acc2']          # violet ("gold" class), mint ("cyan" class)
TX, AXC, CU = '#E6ECF1', '#6B7B8A', '#D9B45A'
SUBJ = 'VLSI DESIGN'


def g(v, n=3):
    s = f'{v:.{n}f}'
    return s.rstrip('0').rstrip('.') if '.' in s else s


def close(a, b, tol=1e-6):
    return abs(a - b) <= tol


# ================================================================ board (isometric PCB) helpers
PCBDEF = ('<defs><linearGradient id="pcb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#17463C"/><stop offset="1" stop-color="#0D2A24"/></linearGradient>'
          '<linearGradient id="icg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2A2E36"/><stop offset="1" stop-color="#121418"/></linearGradient></defs>')
ICC = ('url(#icg)', '#0B0D10', '#1A1D22')
SIL = ('#C9D0D6', '#7D8792', '#9AA4AE')
VIO = ('#C9B3FF', '#5E44B0', '#7F5FE0')
MNT = ('#8FF3E2', '#167A6C', '#25A592')
GLD = ('#F2D27A', '#8E6C22', '#BE9640')
SIG = ('#7C8696', '#3A414C', '#555E6B')     # silicon
OXC = ('#9FC2EA', '#4C6E96', '#6D90B8')     # oxide
RES = ('#F4F1EA', '#A09A8C', '#C8C2B4')     # photoresist


def setup(oy=318):
    B.U, B.OX, B.OY = 33, 952, oy


def board(parts):
    return T.iso_board(D, [PCBDEF] + parts, top='url(#pcb)', left='#0A1F1A', right='#0E2822', origin=(B.OX, B.OY))


def lab(x, y, z, t, col=TX, fs=15, anchor='middle', dy=0):
    a, b = P(x, y, z)
    return f'<text x="{a:.1f}" y="{b + dy:.1f}" text-anchor="{anchor}" class="capl" style="fill:{col};font-size:{fs}px">{t}</text>'


def trace(path, col=CU, w=3, z=.01, glow=False, op=.9):
    s = f'<polyline points="{pts(*[P(a, b, z) for a, b in path])}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round" opacity="{op}"/>'
    return f'<g filter="url(#gl)">{s}</g>' if glow else s


def pad(x, y, col=CU):
    a, b = P(x, y)
    return f'<ellipse cx="{a:.1f}" cy="{b:.1f}" rx="5" ry="3" fill="#0D2A24" stroke="{col}" stroke-width="2"/>'


def ic(x, y, w, d, h, text, col=TX, fs=15, pins=4, c=ICC):
    """an IC body with silver pins on its two front faces and a label on top"""
    o = [box(x, y, w, d, h, *c)]
    for i in range(pins):
        px = x + (i + .5) * w / pins - .09
        o.append(box(px, y + d, .18, .22, .1, *SIL))
    for i in range(max(1, round(pins * d / w))):
        py = y + (i + .5) * d / max(1, round(pins * d / w)) - .09
        o.append(box(x + w, py, .22, .18, .1, *SIL))
    o.append(lab(x + w / 2, y + d / 2, h, text, col, fs, dy=5))
    return ''.join(o)


def glow_arrow(a, b, c, col, w=5):
    (x0, y0), (x1, y1) = a, b
    return f'<g filter="url(#gl)">{arrow(x0, y0, x1, y1, col, w)}</g>' if c else arrow(x0, y0, x1, y1, col, w)


def prism(x, y, w, d, h, c, z0=0):
    """an inverter body: a triangular prism pointing along +x, with a bubble cylinder at the tip"""
    t, l, r = c
    A0, A1, A2 = P(x, y, z0), P(x, y + d, z0), P(x + w, y + d / 2, z0)
    T0, T1, T2 = P(x, y, z0 + h), P(x, y + d, z0 + h), P(x + w, y + d / 2, z0 + h)
    return (f'<polygon points="{pts(A1, A2, T2, T1)}" fill="{l}"/>'
            f'<polygon points="{pts(T0, T1, T2)}" fill="{t}"/>')


# ================================================================ card (2D) helpers, 470 x 144
def svg(inner, h=144):
    return f'<svg width="470" height="{h}" viewBox="0 0 470 {h}">{inner}</svg>'


def ln(x1, y1, x2, y2, col=AXC, w=1.5, dash=None, op=1):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}"{d} opacity="{op}"/>'


def tx(x, y, s, cls='ax', anchor='middle', fill=None, fs=None, fw=None):
    st = (f'fill:{fill};' if fill else '') + (f'font-size:{fs}px;' if fs else '') + (f'font-weight:{fw};' if fw else '')
    st = f' style="{st}"' if st else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}"{st}>{s}</text>'


def pl(points, col, w=3, fill='none', op=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in points)}" fill="{fill}" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" opacity="{op}"{d}/>'


def dot(x, y, col, r=5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>'


def rect(x, y, w, h, col, op=1, stroke=None, rx=3):
    s = f' stroke="{stroke}" stroke-width="1.5"' if stroke else ''
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{col}" opacity="{op}"{s}/>'


TABLE = """
.scope table{border-collapse:collapse;width:100%;margin-top:4px;font:600 17px 'IBM Plex Sans';color:#E6ECF1}
.scope th{font:600 14px 'IBM Plex Sans';color:#B9B0E6;text-align:center;padding:3px 6px;border-bottom:1.5px solid rgba(195,184,255,.3)}
.scope td{text-align:center;padding:5px 6px;border-bottom:1px solid rgba(195,184,255,.16);font-size:17px;white-space:nowrap}
.scope td:first-child{text-align:left;color:#C9D3DB}.scope tr:last-child td{border-bottom:none}"""


def chip(side, top, kind, text, pointer=True):
    return dict(side=side, top=top, kind=kind, text=text, pointer=pointer)


def spec(key, title, hook, take, ctitle, card, board_, chips, summary, css='', h1=None):
    s = dict(key=f'ec-vlsi-{key}', dept=D, subject=SUBJ, title=title, question=hook, takeaway=take, tag='Book example',
             card_title=ctitle, card=card, board=board_, chips=chips, summary=summary,
             page_title=title.replace('<br>', ' ') + ': VLSI Design', css=css + (f'h1{{font-size:{h1}px !important}}' if h1 else ''))
    return s


# ================================================================ Unit 1
def u1_l1():
    # Ch 1.1 worked example: CMOS inverter, VDD = 1.8 V, VTn = 0.5 V, VTp = -0.5 V, Vin = 0.8 V, Vout = 1.5 V
    VDD, VTn, VTp, Vin, Vout = 1.8, 0.5, 0.5, 0.8, 1.5
    vgs, ovn, vds = Vin, Vin - VTn, Vout
    vsg, ovp, vsd = VDD - Vin, VDD - Vin - VTp, VDD - Vout
    n_reg = 'saturated' if vds >= ovn else 'linear'
    p_reg = 'linear' if vsd < ovp else 'saturated'
    assert close(ovn, .3) and close(vsg, 1.0) and close(ovp, .5) and close(vsd, .3) and (n_reg, p_reg) == ('saturated', 'linear')
    tbl = ('<table><tr><th></th><th style="color:#3FE0C8">nMOS</th><th style="color:#B79CFF">pMOS</th></tr>'
           f'<tr><td>gate drive</td><td>V<sub>GS</sub> = {g(vgs)} V</td><td>V<sub>SG</sub> = {vsg:.1f} V</td></tr>'
           f'<tr><td>overdrive</td><td>{g(ovn)} V</td><td>{g(ovp)} V</td></tr>'
           f'<tr><td>channel</td><td>V<sub>DS</sub> = {g(vds)} V</td><td>V<sub>SD</sub> = {g(vsd)} V</td></tr>'
           f'<tr><td>region</td><td style="color:#3FE0C8;font-weight:700">{n_reg}</td><td style="color:#B79CFF;font-weight:700">{p_reg}</td></tr></table>')
    setup()
    o = [trace([(1.2, .8), (7.6, .8)], CU, 7), trace([(3.0, 7.0), (7.4, 7.0)], CU, 7),
         trace([(5.5, .8), (5.5, 1.6)], CU, 4), trace([(5.5, 5.4), (5.5, 7.0)], CU, 4),
         trace([(5.5, 3.0), (5.5, 4.0)], MI, 4, glow=True), trace([(5.5, 3.5), (7.9, 3.5)], MI, 4, glow=True),
         trace([(3.6, 7.6), (3.6, 2.3), (4.6, 2.3)], VI, 4, glow=True), trace([(3.6, 4.7), (4.6, 4.7)], VI, 4, glow=True),
         ic(4.6, 1.6, 1.8, 1.4, .8, 'pMOS', '#F3EEFF', 16, 3, VIO), ic(4.6, 4.0, 1.8, 1.4, .8, 'nMOS', '#0C2A26', 16, 3, MNT),
         lab(3.6, 7.6, 0, f'in {g(Vin)} V', VI, 15, dy=24), lab(8.0, 3.5, 0, f'out {g(Vout)} V', MI, 15, 'start', dy=5),
         lab(7.7, .8, 0, f'V<tspan dy="4" font-size="11">DD</tspan><tspan dy="-4"> {g(VDD)} V</tspan>', CU, 14, 'start', dy=5), lab(6.6, 7.0, 0, 'GND', CU, 14, dy=24)]
    return spec('u1-L1', 'The MOS<br>Transistor &amp;<br>Its Threshold', 'Is this pMOS really off?',
                'Measure a pMOS from its <span class="cyan">source</span>:<br>V<sub>SG</sub> = 1.0 V, so it is <span class="gold">ON</span>',
                f'inverter at V<sub>in</sub> = {g(Vin)} V', tbl, board(o),
                [chip('left', 296, 'c', f'V<sub>DD</sub> = {g(VDD)} V, |V<sub>T</sub>| = 0.5 V'), chip('left', 360, 'c', f'V<sub>out</sub> = {g(Vout)} V'),
                 chip('left', 424, 'g', f'V<sub>SG</sub> = {vsg:.1f} V ≥ 0.5 V'), chip('right', 318, 'g', 'pMOS: ON, linear'),
                 chip('right', 532, 'c', 'nMOS: saturated', False)],
                f'<b class="gl">pMOS:</b> V<sub>SG</sub> = {g(VDD)} − {g(Vin)} = {vsg:.1f} V, V<sub>SD</sub> = {g(vsd)} V → <b class="gl">{p_reg}</b><br>'
                f'<b class="cl">nMOS:</b> overdrive {g(ovn)} V, V<sub>DS</sub> = {g(vds)} V → <b class="cl">{n_reg}</b>', TABLE)


def u1_l2():
    # Ch 1.5 worked example: W = 1 um, L = 0.25 um, tox = 4 nm, Lov = 0.02 um, eps_ox = 3.45e-11 F/m
    Cox = 3.45e-11 / 4e-9 * 1e3                      # fF/um^2
    W, L, Lov = 1, .25, .02
    CWL, Cov = Cox * W * L, Cox * W * Lov
    Cgs, Cgd = 2 / 3 * CWL + Cov, Cov
    assert close(Cox, 8.625) and round(CWL, 3) == 2.156 and close(Cov, .1725) and round(Cgs, 2) == 1.61 and round(Cgs + Cgd, 2) == 1.78
    # card: gate capacitances in saturation and in cutoff (bars), C_oxWL as the reference line
    y0, sc = 118, 92 / 2.4
    Y = lambda c: y0 - c * sc
    o = [ln(40, y0, 460, y0), ln(40, 22, 40, y0), tx(34, Y(2.0) + 5, '2', 'ax', 'end'), tx(34, y0 + 5, '0', 'ax', 'end'), tx(34, Y(1.0) + 5, '1', 'ax', 'end'),
         ln(40, Y(CWL), 460, Y(CWL), TX, 1.5, '6 5', .7), tx(458, Y(CWL) - 6, f'C<tspan dy="3" font-size="10">ox</tspan><tspan dy="-3">WL = {CWL:.2f} fF</tspan>', 'ax', 'end', TX)]
    groups = [('saturation', [('C<tspan dy="3" font-size="10">gs</tspan>', Cgs, VI), ('C<tspan dy="3" font-size="10">gd</tspan>', Cgd, MI)], 70),
              ('cutoff', [('C<tspan dy="3" font-size="10">gs</tspan>', Cov, VI), ('C<tspan dy="3" font-size="10">gd</tspan>', Cov, MI)], 270)]
    for name, bars, x0 in groups:
        for k, (n, v, c) in enumerate(bars):
            x = x0 + k * 74
            o.append(rect(x, Y(v), 52, y0 - Y(v), c, .85, rx=2))
            o.append(tx(x + 26, Y(v) - 6, f'{v:.2f}', 'pt', 'middle', c))
            o.append(tx(x + 26, y0 + 16, n, 'ax'))
        o.append(tx(x0 + 63, y0 + 34, name, 'ax', 'middle', TX))
    card = svg(''.join(o), 156)
    setup(312)
    b = [box(3.0, .4, 4.8, 3.6, .9, *SIG), box(3.0, .4, 1.3, 3.6, .18, *MNT, z0=.9), box(6.5, .4, 1.3, 3.6, .18, *MNT, z0=.9),
         box(4.2, .4, 2.4, 3.6, .08, *OXC, z0=.9), box(4.3, .4, 2.2, 3.6, .55, *VIO, z0=.98),
         lab(3.65, 2.2, 1.08, 'S', '#0C2A26', 22, dy=8), lab(7.15, 2.2, 1.08, 'D', '#0C2A26', 22, dy=8), lab(5.4, 2.2, 1.53, 'G', '#F3EEFF', 22, dy=8),
         lab(5.4, 4.0, .3, 'p-substrate', '#DDE3EA', 14, dy=4)]
    return spec('u1-L2', 'MOSFET<br>Current &amp;<br>Capacitance', 'Half or two-thirds: Cgs in saturation?',
                'In saturation C<sub>gs</sub> takes <span class="gold">⅔</span><br>of C<sub>ox</sub>WL; C<sub>gd</sub> only <span class="cyan">overlap</span>',
                'C<sub>gs</sub> and C<sub>gd</sub> of one nMOS', card, board(b),
                [chip('left', 296, 'c', f'W = {W} µm, L = {L} µm'), chip('left', 360, 'c', 't<sub>ox</sub> = 4 nm, L<sub>ov</sub> = 0.02 µm'),
                 chip('left', 424, 'c', f'C<sub>ox</sub> = {Cox:.3f} fF/µm²'), chip('right', 318, 'g', f'C<sub>gs</sub> = {Cgs:.2f} fF'),
                 chip('right', 500, 'c', f'C<sub>gd</sub> = {Cgd:.2f} fF', False)],
                f'C<sub>ox</sub>WL = {Cox:.3f} × {W} × {L} = {CWL:.3f} fF, C<sub>ov</sub> = {Cov:.4f} fF<br>'
                f'C<sub>gs</sub> = ⅔ × {CWL:.3f} + {Cov:.4f} = <b class="gl">{Cgs:.2f} fF</b>, C<sub>gd</sub> = <b class="cl">{Cgd:.2f} fF</b>')


def u1_l3():
    # Ch 1.7 worked example: SS = 80 mV/decade, Ioff = 10 nA/um at VT = 0.3 V, VT raised by 100 mV; 10 mm off width at 1 V
    SS, Ioff, dVT, Wum, phit = 80, 10, 100, 1e4, 26
    fac = 10 ** (dVT / SS); Ioff2 = Ioff / fac
    I1, I2 = Ioff * Wum / 1e3, Ioff2 * Wum / 1e3        # uA
    n = SS / (2.3 * phit)
    assert round(fac, 1) == 17.8 and round(Ioff2, 3) == .562 and round(I1) == 100 and round(I2, 2) == 5.62 and round(n, 2) == 1.34
    # card: log I_D against V_GS for both thresholds, 80 mV per decade
    X = lambda v: 60 + v / .2 * 380
    Y = lambda i_na: 120 - (math.log10(i_na) + 1) / 5 * 100      # 0.1 nA .. 10 uA
    o = [ln(60, 120, 450, 120), ln(60, 18, 60, 120)]
    for d_, s in ((-1, '0.1 nA'), (1, '10 nA'), (3, '1 µA')):
        o.append(tx(54, Y(10 ** d_) + 5, s, 'ax', 'end'))
        o.append(ln(60, Y(10 ** d_), 450, Y(10 ** d_), AXC, 1, '2 5', .5))
    for v in (0, .1, .2):
        o.append(tx(X(v), 138, g(v), 'ax'))
    o.append(tx(450, 112, 'V<tspan dy="3" font-size="10">GS</tspan><tspan dy="-3">, V</tspan>', 'ax', 'end'))
    for i0, c, name in ((Ioff, VI, f'V<tspan dy="3" font-size="10">T</tspan><tspan dy="-3"> = 0.3 V</tspan>'), (Ioff2, MI, f'V<tspan dy="3" font-size="10">T</tspan><tspan dy="-3"> = 0.4 V</tspan>')):
        vs = [k * .2 / 20 for k in range(21)]
        o.append(pl([(X(v), Y(i0 * 10 ** (v * 1000 / SS))) for v in vs], c, 3.2))
        o.append(dot(X(0), Y(i0), c, 5.5))
        o.append(tx(X(.2) - 4, Y(i0 * 10 ** (200 / SS)) + (-8 if c == VI else 18), name, 'pt', 'end', c))
    o.append(tx(X(0) + 12, Y(Ioff) - 8, f'{Ioff} nA', 'pt', 'start', VI))
    o.append(tx(X(0) + 12, Y(Ioff2) + 18, f'{Ioff2:.2f} nA', 'pt', 'start', MI))
    o.append(tx(X(.13), Y(Ioff) + 34, f'÷ {fac:.1f} at V<tspan dy="3" font-size="10">GS</tspan><tspan dy="-3"> = 0</tspan>', 'pt', 'middle', TX))
    card = svg(''.join(o))
    setup(320)
    b = [box(2.2, .8, 5.4, 4.4, .5, *SIG), box(2.5, 1.6, 4.8, 2.8, .1, *MNT, z0=.5)]
    for k in range(6):
        b.append(box(2.8 + k * .8, 1.1, .32, 3.8, .35, *VIO, z0=.5))
    for k in range(6):
        x, y = P(2.96 + k * .8, 5.2, .2)
        b.append(f'<g filter="url(#gl)">{arrow(x, y + 4, x, y + 42, MI, 4)}</g>')
    b += [lab(7.4, 5.2, 0, f'{Wum / 1e3:g} mm of off width at 1 V', '#DDE3EA', 14, 'start', dy=44)]
    return spec('u1-L3', 'Scaling,<br>Leakage &amp;<br>FinFETs', 'Can a bulk MOSFET beat 60 mV/decade?',
                'No bulk MOSFET beats <span class="gold">60 mV</span>/dec;<br>this one swings <span class="cyan">80 mV</span>/dec',
                'raise V<sub>T</sub> by 100 mV', card, board(b),
                [chip('left', 296, 'c', f'SS = {SS} mV/decade'), chip('left', 360, 'g', f'V<sub>T</sub> + {dVT} mV'),
                 chip('left', 424, 'g', f'10<sup>100/80</sup> = {fac:.1f}×'), chip('right', 318, 'c', f'{I1:.0f} µA → {I2:.1f} µA'),
                 chip('right', 500, 'c', f'n = {n:.2f}', False)],
                f'I<sub>off</sub> = {Ioff} ÷ {fac:.1f} = <b class="cl">{Ioff2:.2f} nA/µm</b>; block {I1:.0f} → {I2:.1f} µA<br>'
                f'SS = 2.3nφ<sub>t</sub> ≥ 2.3 × {phit} ≈ <b class="gl">60 mV</b>/dec; here n = {n:.2f}')


# ================================================================ Unit 2
def u2_l1():
    # Ch 2.2 worked example 2: 0.5 um oxide, 2.0 um window, 100 nm/min, 20 % over-etch, RIE anisotropy 0.9, selectivity 5:1
    tox, win, rate, over, A, sel = .5, 2.0, 100, .2, .9, 5
    t = tox * 1e3 / rate * (1 + over)
    wet = win + 2 * rate * t / 1e3
    rie = win + 2 * (1 - A) * rate * t / 1e3
    rloss = rate / sel * t
    assert close(t, 6.0) and close(wet, 3.2) and close(rie, 2.12) and close(rloss, 120)
    # card: the two holes in section, 50 px per um across
    s = 50
    o = []
    for k, (name, hole, c) in enumerate((('wet etch', wet, VI), ('RIE', rie, MI))):
        cx = 118 + k * 236
        top, ox_h, res_h = 50, tox * s, 9
        o.append(rect(cx - 110, top + ox_h, 220, 34, '#4A515C', 1, rx=0))
        a, b2 = cx - hole * s / 2, cx + hole * s / 2
        wa, wb = cx - win * s / 2, cx + win * s / 2
        if k == 0:     # isotropic: a quarter-round undercut to the window edge at the bottom
            o.append(f'<path d="M{cx - 110},{top} H{a:.1f} Q{wa:.1f},{top:.1f} {wa:.1f},{top + ox_h:.1f} H{cx - 110}Z" fill="#6D90B8"/>')
            o.append(f'<path d="M{cx + 110},{top} H{b2:.1f} Q{wb:.1f},{top:.1f} {wb:.1f},{top + ox_h:.1f} H{cx + 110}Z" fill="#6D90B8"/>')
        else:
            o.append(f'<path d="M{cx - 110},{top} H{a:.1f} L{wa + 1:.1f},{top + ox_h:.1f} H{cx - 110}Z" fill="#6D90B8"/>')
            o.append(f'<path d="M{cx + 110},{top} H{b2:.1f} L{wb - 1:.1f},{top + ox_h:.1f} H{cx + 110}Z" fill="#6D90B8"/>')
        o.append(rect(cx - 110, top - res_h, wa - (cx - 110), res_h, '#E9E4D8', 1, rx=0))
        o.append(rect(wb, top - res_h, cx + 110 - wb, res_h, '#E9E4D8', 1, rx=0))
        o.append(ln(a, top - 18, b2, top - 18, c, 2.5)); o.append(ln(a, top - 24, a, top - 12, c, 2.5)); o.append(ln(b2, top - 24, b2, top - 12, c, 2.5))
        o.append(tx(cx, top - 26, f'{name}: {g(hole)} µm', 'pt', 'middle', c))
        o.append(tx(cx, top + ox_h + 24, 'silicon', 'ax', 'middle', '#C9D3DB'))
    o.append(tx(235, 140, f'resist window {win:.1f} µm · oxide {tox} µm · {t:.1f} min', 'ax', 'middle', TX))
    card = svg(''.join(o))
    setup(312)
    hw, ww = wet / 2, win / 2
    cx, x0, x1, y0, dy_ = 5.4, 2.8, 7.6, .6, 5.6
    b = [box(x0, y0, x1 - x0, dy_, .9, *SIG),
         box(x0, y0, cx - hw - x0, dy_, .7, *OXC, z0=.9), box(cx + hw, y0, x1 - cx - hw, dy_, .7, *OXC, z0=.9),
         box(x0, y0, cx - ww - x0, dy_, .22, *RES, z0=1.6), box(cx + ww, y0, x1 - cx - ww, dy_, .22, *RES, z0=1.6)]
    for k in range(4):
        x, y = P(cx, 1.6 + k * 1.1, 1.8)
        b.append(f'<g filter="url(#gl)">{arrow(x, y - 64, x, y - 6, MI, 4)}</g>')
    b += [lab(x1, 1.2, 1.72, 'resist', '#F4F1EA', 14, 'start', dy=4), lab(x1, 3.6, 1.25, 'oxide', '#BFD6F2', 14, 'start', dy=8),
          lab(5.0, y0 + dy_, .3, 'silicon', '#DDE3EA', 14, dy=12)]
    return spec('u2-L1', 'Growing,<br>Doping &amp;<br>Printing Silicon', 'Why is a wet-etched hole wider?',
                'Wet etch eats <span class="gold">sideways</span>;<br>RIE cuts <span class="cyan">straight down</span>',
                'one window, two etches', card, board(b),
                [chip('left', 296, 'c', f'{tox} µm oxide, {win:.1f} µm window'), chip('left', 360, 'c', f'{rate} nm/min, +20 %: {t:.1f} min'),
                 chip('left', 424, 'c', f'resist loses {rloss:.0f} nm'), chip('right', 318, 'g', f'wet: {g(wet)} µm'),
                 chip('right', 500, 'c', f'RIE: {g(rie)} µm', False)],
                f'Wet: undercut {rate} × {t:.1f} = 600 nm a side → <b class="gl">{g(wet)} µm</b><br>'
                f'RIE, A = {A}: 10 nm/min → {win:.1f} + 2 × 0.06 = <b class="cl">{g(rie)} µm</b>')


def u2_l2():
    # Ch 2.4 worked example 2: n-well process, mu_n = 500, mu_p = 200 cm^2/V.s, Wn = 2 um
    mun, mup, Wn = 500, 200, 2
    r = mun / mup; Wp = r * Wn
    assert close(r, 2.5) and close(Wp, 5)
    # card: the inverter in cross-section
    o = [rect(10, 70, 450, 56, '#5E5590', 1, rx=4), tx(80, 116, 'p-substrate', 'ax', 'middle', '#E6E1FF'),
         f'<path d="M232,70 V112 Q232,124 244,124 H448 Q460,124 460,112 V70Z" fill="#1E8C7C"/>', tx(420, 116, 'n-well', 'ax', 'middle', '#D8FFF7')]
    for x, w_, lb, c, fc in ((40, 44, 'n⁺', '#3FE0C8', '#0C2A26'), (146, 44, 'n⁺', '#3FE0C8', '#0C2A26'), (262, 50, 'p⁺', '#B79CFF', '#1A1238'), (390, 50, 'p⁺', '#B79CFF', '#1A1238')):
        o.append(rect(x, 70, w_, 22, c, 1, rx=3)); o.append(tx(x + w_ / 2, 87, lb, 'pt', 'middle', fc, 15))
    for x0, x1 in ((84, 146), (312, 390)):
        o.append(rect(x0 + 2, 62, x1 - x0 - 4, 7, '#9FC2EA', 1, rx=1)); o.append(rect(x0 + 2, 44, x1 - x0 - 4, 18, '#8F6BF0', 1, rx=2))
    o.append(tx(115, 34, f'NMOS · W<tspan dy="3" font-size="10">n</tspan><tspan dy="-3"> = {Wn} µm</tspan>', 'pt', 'middle', MI))
    o.append(tx(351, 34, f'PMOS · W<tspan dy="3" font-size="10">p</tspan><tspan dy="-3"> = {g(Wp)} µm</tspan>', 'pt', 'middle', VI))
    o.append(tx(235, 140, f'W<tspan dy="3" font-size="10">p</tspan><tspan dy="-3">/W</tspan><tspan dy="3" font-size="10">n</tspan><tspan dy="-3"> = µ</tspan><tspan dy="3" font-size="10">n</tspan><tspan dy="-3">/µ</tspan><tspan dy="3" font-size="10">p</tspan><tspan dy="-3"> = {mun}/{mup} = {g(r)}</tspan>', 'ax', 'middle', TX))
    card = svg(''.join(o))
    setup(312)
    b = [box(.6, .6, 6.8, 6.8, .8, '#6A62A0', '#2B2550', '#3E3770'),
         box(4.2, .6, 3.2, 6.8, .06, *MNT, z0=.8),
         # NMOS (in the p-substrate): width Wn along y
         box(2.2, .9, .6, Wn, .1, *MNT, z0=.8), box(3.2, .9, .6, Wn, .1, *MNT, z0=.8), box(2.8, .9, .4, Wn, .4, *VIO, z0=.85),
         # PMOS (in the n-well): width Wp along y
         box(4.6, 1.0, .8, Wp, .1, *VIO, z0=.86), box(5.8, 1.0, .8, Wp, .1, *VIO, z0=.86), box(5.4, 1.0, .4, Wp, .4, '#E8E0FF', '#8C7BC8', '#B5A6EE', z0=.9),
         lab(3.0, .9 + Wn, .4, 'NMOS', '#F3EEFF', 16, dy=22), lab(5.6, 1.0 + Wp, .9, 'PMOS', '#1A1238', 16, dy=26),
         lab(7.4, 4.6, .4, 'n-well', '#D8FFF7', 14, 'start', dy=8), lab(3.9, 7.2, .8, 'p-substrate', '#E6E1FF', 14, dy=18)]
    return spec('u2-L2', 'How a CMOS<br>Chip Is Built', 'Does the NMOS sit in the n-well?',
                'The <span class="gold">PMOS</span> sits in the n-well,<br>the NMOS in the <span class="cyan">p-substrate</span>',
                'symmetric n-well inverter', card, board(b),
                [chip('left', 296, 'c', f'µ<sub>n</sub> = {mun} cm²/V·s'), chip('left', 360, 'c', f'µ<sub>p</sub> = {mup} cm²/V·s'),
                 chip('left', 424, 'c', f'W<sub>n</sub> = {Wn} µm'), chip('right', 318, 'g', f'W<sub>p</sub> = {g(r)} × {Wn} = {g(Wp)} µm'),
                 chip('right', 532, 'g', 'PMOS in the n-well', False)],
                f'µ<sub>n</sub>(W/L)<sub>n</sub> = µ<sub>p</sub>(W/L)<sub>p</sub>: W<sub>p</sub>/W<sub>n</sub> = {mun}/{mup} = <b class="cl">{g(r)}</b><br>'
                f'W<sub>p</sub> = {g(r)} × {Wn} µm = <b class="gl">{g(Wp)} µm</b>; electrons set the speed')


def u2_l3():
    # Ch 2.6 worked example: lambda = 0.5 um; metal 1 width 3 lambda, spacing 3 lambda; W = 8 lambda, L = 2 lambda; Cox = 2.3 fF/um^2
    lam, mw, ms, W, L, Cox = .5, 3, 3, 8, 2, 2.3
    pitch = mw + ms
    area = W * lam * L * lam; Cg = Cox * area
    assert close(mw * lam, 1.5) and close(pitch * lam, 3.0) and close(area, 4) and close(Cg, 9.2)
    # card: metal lines top view with width / spacing / pitch; a transistor W x L on the right
    s = 13          # px per lambda
    o = []
    x0, y0 = 26, 36
    for i in range(3):
        o.append(rect(x0 + i * pitch * s, y0, mw * s, 84, VI if i < 2 else '#7F5FE0', .9 if i < 2 else .6, rx=2))
    c0, c1 = x0 + mw * s / 2, x0 + pitch * s + mw * s / 2
    o += [ln(c0, y0 - 12, c1, y0 - 12, VI, 2.5), ln(c0, y0 - 18, c0, y0 - 6, VI, 2.5), ln(c1, y0 - 18, c1, y0 - 6, VI, 2.5),
          tx((c0 + c1) / 2, y0 - 18, f'pitch {pitch}λ = {pitch * lam:.1f} µm', 'pt', 'middle', VI),
          ln(c0, y0, c0, y0 + 84, TX, 1, '3 4', .7), ln(c1, y0, c1, y0 + 84, TX, 1, '3 4', .7),
          tx(x0 + mw * s / 2, 136, '3λ', 'pt', 'middle', TX), tx(x0 + (mw + ms / 2) * s, 136, '3λ', 'pt', 'middle', MI),
          tx(x0 + (mw + ms / 2) * s, 92, 'gap', 'ax', 'middle', MI)]
    tx0, ty0 = 256, 34
    o += [rect(tx0, ty0, 24 * 2, W * 11, '#25A592', .9, rx=2), rect(tx0 - 16, ty0 + W * 11 / 2 - L * 6, 80, L * 12, '#E07A7A', .9, rx=2),
          tx(tx0 + 76, ty0 + 16, f'W = {W}λ = {g(W * lam)} µm', 'ax', 'start', MI), tx(tx0 + 76, ty0 + W * 11 / 2 + 5, f'L = {L}λ = {g(L * lam)} µm', 'ax', 'start', '#F2A0A0'),
          tx(tx0 + 76, ty0 + W * 11 - 6, f'C<tspan dy="3" font-size="10">g</tspan><tspan dy="-3"> = {g(Cg)} fF</tspan>', 'ax', 'start', TX)]
    card = svg(''.join(o))
    setup(316)
    u = .4          # board units per lambda: width 3 lambda = 1.2, pitch 6 lambda = 2.4
    b = [box(1.6, .3, 6.2, 7.0, .25, '#2E3A6A', '#151B36', '#1F2850')]
    for i in range(3):
        y = .6 + i * pitch * u
        b.append(box(2.2, y, 5.4, mw * u, .3, *(VIO if i != 1 else ('#E2D6FF', '#6A4FC0', '#9C80F2')), z0=.25))
    ya, yb = .6 + mw * u / 2, .6 + pitch * u + mw * u / 2
    a1, a2 = P(7.75, ya, .55), P(7.75, yb, .55)
    b.append(f'<g filter="url(#gl)"><line x1="{a1[0]:.1f}" y1="{a1[1]:.1f}" x2="{a2[0]:.1f}" y2="{a2[1]:.1f}" stroke="{MI}" stroke-width="4"/></g>')
    for yy in (ya, yb):
        c1, c2 = P(7.55, yy, .55), P(7.95, yy, .55)
        b.append(f'<line x1="{c1[0]:.1f}" y1="{c1[1]:.1f}" x2="{c2[0]:.1f}" y2="{c2[1]:.1f}" stroke="{MI}" stroke-width="3"/>')
    b += [lab(5.0, .6, .55, 'metal 1', '#F3EEFF', 14, dy=-6), lab(7.9, (ya + yb) / 2, .55, f'{pitch}λ', MI, 16, 'start', dy=6),
          lab(5.6, .6 + 2 * pitch * u + mw * u, .55, f'{mw}λ wide, {ms}λ apart', '#E2D6FF', 14, dy=34)]
    return spec('u2-L3', 'BiCMOS &amp;<br>Layout Design<br>Rules', 'Is metal pitch width + 2 spacings?',
                'Pitch is width + <span class="gold">one</span> spacing,<br>centre to <span class="cyan">centre</span>',
                f'λ rules at λ = {lam} µm', card, board(b),
                [chip('left', 296, 'c', f'λ = {lam} µm'), chip('left', 360, 'c', f'width 3λ = {mw * lam} µm'),
                 chip('left', 424, 'c', f'spacing 3λ = {ms * lam} µm'), chip('right', 318, 'g', f'pitch 6λ = {pitch * lam:.1f} µm'),
                 chip('right', 500, 'c', f'C<sub>g</sub> = {g(Cg)} fF', False)],
                f'pitch = width + spacing = 3λ + 3λ = <b class="gl">6λ = {pitch * lam:.1f} µm</b><br>'
                f'gate {g(W * lam)} µm × {g(L * lam)} µm = {g(area)} µm² → C<sub>g</sub> = <b class="cl">{g(Cg)} fF</b>')


def u2_l4():
    # Ch 2.8 worked example: 2 mA into the substrate; R_sub = 200 or 500 ohm; npn needs 0.7 V; beta_npn = 50, beta_pnp = 20
    I, Vbe, bn, bp = 2e-3, .7, 50, 20
    V = {R: I * R for R in (200, 500)}
    assert close(V[200], .4) and close(V[500], 1.0) and V[200] < Vbe < V[500] and bn * bp == 1000
    y0, sc = 120, 90 / 1.2
    Y = lambda v: y0 - v * sc
    o = [ln(46, y0, 270, y0), ln(46, 22, 46, y0), tx(40, Y(1.0) + 5, '1.0', 'ax', 'end'), tx(40, y0 + 5, '0', 'ax', 'end'),
         ln(46, Y(Vbe), 270, Y(Vbe), TX, 2, '7 5'), tx(40, Y(Vbe) + 5, f'{Vbe}', 'ax', 'end', '#F3EEFF', None, 700)]
    for k, (R, c) in enumerate(((200, MI), (500, VI))):
        x = 80 + k * 100
        o += [rect(x, Y(V[R]), 60, y0 - Y(V[R]), c, .85, rx=2), tx(x + 30, Y(V[R]) - 7, f'{V[R]:.1f} V', 'pt', 'middle', c), tx(x + 30, 138, f'{R} Ω', 'ax')]
    o += [tx(375, 46, 'loop gain', 'ax', 'middle', TX), tx(375, 76, f'{bn} × {bp} = {bn * bp}', 'pt', 'middle', VI, 21),
          tx(375, 104, '&gt; 1: regenerative', 'ax', 'middle', VI)]
    card = svg(''.join(o))
    setup(316)
    b = [box(.6, .6, 6.8, 6.8, .7, '#5E5590', '#2B2550', '#3E3770'), box(.6, .6, 6.8, 2.8, .08, *MNT, z0=.7),
         lab(7.4, 1.6, .78, 'n-well', '#D8FFF7', 14, 'start', dy=4), lab(4.4, 7.4, .7, 'p-substrate', '#E6E1FF', 14, dy=18)]
    for (x, y, z, nm) in ((3.4, 1.75, .78, 'well'), (5.0, 6.6, .7, 'sub')):
        b.append(box(x, y, 1.6, .5, .35, *RES, z0=z))
        for k in range(3):
            b.append(box(x + .3 + k * .45, y, .12, .5, .36, '#8E6C22', '#6E5418', '#8E6C22', z0=z))
        b.append(lab(x, y + .25, z + .2, f'R<tspan dy="3" font-size="10">{nm}</tspan>', TX, 15, 'end', dy=4))
    nx, ny = P(6.8, 5.0, .7); px_, py_ = P(6.0, 1.8, .78)
    b += [cyl(nx, ny, 26, 14, 38, '#3A2F72', VI), lab(6.8, 5.0, 1.85, 'npn', '#F3EEFF', 14, dy=4),
          cyl(px_, py_, 26, 14, 38, '#0F5A50', MI), lab(6.0, 1.8, 1.93, 'pnp', '#0C2A26', 14, dy=4)]
    sx, sy = P(5.0, 5.0, .7)
    b.append(f'<g filter="url(#gl)">{arrow(sx, sy - 80, sx, sy - 4, VI, 6)}</g>')
    b.append(f'<text x="{sx - 8:.1f}" y="{sy - 60:.1f}" text-anchor="end" class="capl" style="fill:{VI};font-size:16px">2 mA</text>')
    a, b_ = P(6.8, 5.0, 1.9), P(6.0, 1.8, 1.9)
    b.append(f'<path d="M{a[0]:.1f},{a[1] - 30:.1f} Q{(a[0] + b_[0]) / 2 + 60:.1f},{(a[1] + b_[1]) / 2 - 60:.1f} {b_[0]:.1f},{b_[1] - 30:.1f}" fill="none" stroke="{MI}" stroke-width="3" stroke-dasharray="7 6"/>')
    return spec('u2-L4', 'Stick<br>Diagrams &amp;<br>Latch-up', 'When does latch-up start?',
                'It starts once the drop<br>passes <span class="gold">0.7 V</span>: gain <span class="cyan">1000</span> &gt; 1',
                '2 mA spike, two R<sub>sub</sub>', card, board(b),
                [chip('left', 296, 'g', f'I<sub>inj</sub> = {I * 1e3:g} mA'), chip('left', 360, 'c', f'R<sub>sub</sub> 200 Ω → {g(V[200])} V'),
                 chip('left', 424, 'g', f'R<sub>sub</sub> 500 Ω → {V[500]:.1f} V'), chip('right', 318, 'c', f'β<sub>npn</sub> = {bn}, β<sub>pnp</sub> = {bp}'),
                 chip('right', 532, 'g', f'β<sub>npn</sub>β<sub>pnp</sub> = {bn * bp}', False)],
                f'0.002 A × 200 Ω = <b class="cl">{g(V[200])} V</b> &lt; 0.7 V: the npn stays off<br>'
                f'0.002 A × 500 Ω = <b class="gl">{V[500]:.1f} V</b> &gt; 0.7 V: the npn turns on')


# ================================================================ Unit 3
def vtc(VDD, Vt, Vin):
    """matched CMOS inverter (kn = kp, Vtn = |Vtp|): Vout from equal currents, square law, by bisection"""
    def In(vo):
        ov = Vin - Vt
        if ov <= 0: return 0
        return ov * ov / 2 if vo >= ov else ov * vo - vo * vo / 2
    def Ip(vo):
        ov = VDD - Vin - Vt; vsd = VDD - vo
        if ov <= 0: return 0
        return ov * ov / 2 if vsd >= ov else ov * vsd - vsd * vsd / 2
    lo, hi = 0.0, VDD
    for _ in range(60):
        m = (lo + hi) / 2
        if In(m) > Ip(m): hi = m
        else: lo = m
    return (lo + hi) / 2


def u3_l1():
    # Ch 3.1 worked example: matched inverter, VDD = 3.3 V, Vtn = |Vtp| = 0.6 V, kn = kp
    VDD, Vt = 3.3, .6
    VM = (VDD + Vt - Vt) / 2
    VIL = (3 * VDD + 2 * Vt) / 8; VIH = (5 * VDD - 2 * Vt) / 8
    NML, NMH = VIL - 0, VDD - VIH
    assert close(VM, 1.65) and round(VIL, 2) == 1.39 and round(VIH, 2) == 1.91 and round(NML, 2) == 1.39 and round(NMH, 2) == 1.39
    X = lambda v: 56 + v / VDD * 250
    Y = lambda v: 126 - v / VDD * 100
    vs = [k * VDD / 120 for k in range(121)]
    curve = [(X(v), Y(vtc(VDD, Vt, v))) for v in vs if abs(v - VM) > 1e-9]
    o = [ln(56, 124, 312, 124), ln(56, 14, 56, 124), tx(50, Y(VDD) + 5, '3.3', 'ax', 'end'), tx(50, 129, '0', 'ax', 'end'),
         tx(312, 140, 'V<tspan dy="3" font-size="10">in</tspan>', 'ax', 'end'), tx(62, 13, 'V<tspan dy="3" font-size="10">out</tspan>', 'ax', 'start'),
         pl(curve, VI, 3.4)]
    for v, c, name in ((VIL, MI, '1.39'), (VM, VI, '1.65'), (VIH, MI, '1.91')):
        o.append(ln(X(v), 124, X(v), 24, c, 1.6, '4 4', .8))
    o.append(tx(X(VIL) - 3, 140, '1.39', 'ax', 'end', MI)); o.append(tx(X(VM), 140, '1.65', 'ax', 'middle', VI)); o.append(tx(X(VIH) + 3, 140, '1.91', 'ax', 'start', MI))
    o.append(dot(X(VM), Y(VM), VI, 6))
    o += [tx(330, 40, f'V<tspan dy="3" font-size="10">M</tspan><tspan dy="-3"> = {VM:.2f} V</tspan>', 'pt', 'start', VI),
          tx(330, 70, f'V<tspan dy="3" font-size="10">IL</tspan><tspan dy="-3"> = {VIL:.2f} V</tspan>', 'pt', 'start', MI),
          tx(330, 96, f'V<tspan dy="3" font-size="10">IH</tspan><tspan dy="-3"> = {VIH:.2f} V</tspan>', 'pt', 'start', MI),
          tx(330, 126, f'NM = {NML:.2f} V each', 'pt', 'start', TX)]
    card = svg(''.join(o))
    setup(318)
    b = [trace([(2.4, 1.2), (2.4, 3.2), (3.6, 3.2)], MI, 5, glow=True), trace([(6.4, 3.2), (7.8, 3.2)], VI, 5, glow=True),
         trace([(4.6, .8), (4.6, 2.5)], CU, 4), trace([(4.6, 3.9), (4.6, 7.0)], CU, 4),
         prism(3.6, 2.0, 2.6, 2.4, 1.4, ('#C9B3FF', '#5E44B0', '#7F5FE0'))]
    bx, by = P(6.35, 3.2, 0)
    b += [cyl(bx, by, 15, 9, 46, '#5E44B0', '#E2D6FF'), pad(2.4, 1.2, MI), pad(7.8, 3.2, VI),
          lab(4.6, .8, 0, 'V<tspan dy="3" font-size="10">DD</tspan><tspan dy="-3"> 3.3 V</tspan>', CU, 14, dy=-8), lab(4.6, 7.0, 0, 'GND', CU, 14, dy=22),
          lab(2.4, 1.2, 0, 'V<tspan dy="3" font-size="10">in</tspan>', MI, 16, dy=-10), lab(7.9, 3.2, 0, 'V<tspan dy="3" font-size="10">out</tspan>', VI, 16, 'start', dy=5)]
    return spec('u3-L1', 'Inverter DC<br>&amp; Switching', 'Where does the inverter switch?',
                'A matched inverter switches<br>at <span class="gold">V<sub>DD</sub>/2</span>, both FETs <span class="cyan">saturated</span>',
                'matched CMOS inverter', card, board(b),
                [chip('left', 296, 'c', f'V<sub>DD</sub> = {VDD} V'), chip('left', 360, 'c', f'V<sub>tn</sub> = |V<sub>tp</sub>| = {Vt} V'),
                 chip('left', 424, 'c', 'k<sub>n</sub> = k<sub>p</sub>'), chip('right', 318, 'g', f'V<sub>M</sub> = {VM:.2f} V'),
                 chip('right', 532, 'c', f'NM<sub>L</sub> = NM<sub>H</sub> = {NML:.2f} V', False)],
                f'V<sub>M</sub> = (3.3 + 0.6 − 0.6)/2 = <b class="gl">{VM:.2f} V</b>, both saturated<br>'
                f'V<sub>IL</sub> = {VIL:.2f} V, V<sub>IH</sub> = {VIH:.2f} V → NM = <b class="cl">{NML:.2f} V</b> each')


def u3_l2():
    # Ch 3.4 worked example: inverter -> NAND2 -> inverter, input C, load 64C
    G, H, Bf, N = 4 / 3, 64, 1, 3
    F = G * Bf * H; fh = F ** (1 / N); Pp = 1 + 2 + 1; Dd = N * fh + Pp
    c3 = 64 / fh; c2 = 4 / 3 * c3 / fh; c1 = c2 / fh
    assert round(F, 2) == 85.33 and round(fh, 3) == 4.403 and round(Dd, 1) == 17.2 and round(c3, 2) == 14.54 and round(c2, 2) == 4.40 and round(c1, 2) == 1.0
    # card: input capacitance of each stage on a log scale, stage effort between them
    Y = lambda c: 120 - (math.log2(c) + 1) / 7 * 96
    o = [ln(30, 120, 460, 120)]
    items = [('INV', c1, MI), ('NAND2', c2, VI), ('INV', c3, MI), ('load', 64, TX)]
    for k, (n_, c, col) in enumerate(items):
        x = 46 + k * 104
        o += [rect(x, Y(c), 64, 120 - Y(c), col, .85 if col != TX else .35, rx=2),
              tx(x + 32, min(Y(c), 114) - 7, f'{c:.2f}C' if k < 3 else '64C', 'pt', 'middle', col), tx(x + 32, 138, n_, 'ax')]
        if k < 3:
            o.append(tx(x + 84, 138, f'×{fh:.2f}', 'ax', 'middle', VI))
    card = svg(''.join(o))
    setup(318)
    b = [trace([(1.4, 2.4), (1.9, 2.4)], MI, 4, glow=True), trace([(2.8, 2.4), (3.4, 2.4)], MI, 4, glow=True),
         trace([(4.7, 2.4), (5.2, 2.4)], VI, 4, glow=True), trace([(6.8, 2.4), (7.3, 2.4)], MI, 4, glow=True),
         prism(1.9, 1.95, .95, .9, .5, ('#8FF3E2', '#167A6C', '#25A592')),
         box(3.4, 1.6, 1.3, 1.6, .9, *VIO), lab(4.05, 2.4, .9, 'NAND2', '#1A1238', 14, dy=5),
         prism(5.2, 1.6, 1.6, 1.6, 1.1, ('#8FF3E2', '#167A6C', '#25A592'))]
    cx, cy = P(7.5, 2.4, 0)
    b += [cyl(cx, cy, 30, 17, 56, '#3E4652', '#9AA4AE'), lab(7.5, 2.4, 1.7, '64C', '#1A1D22', 15, dy=6),
          lab(5.6, 2.4, 1.1, f'{c3:.2f}C', '#0C2A26', 13, dy=6)]
    return spec('u3-L2', 'Logical<br>Effort &amp;<br>Wire Models', 'Stage effort: F/N or F^(1/N)?',
                'Each stage bears <span class="gold">F<sup>1/N</sup></span>,<br>never <span class="cyan">F/N</span>',
                'INV, NAND2, INV → 64C', card, board(b),
                [chip('left', 296, 'c', 'G = 4/3, H = 64'), chip('left', 360, 'c', f'F = {F:.2f}'),
                 chip('left', 424, 'g', f'f̂ = {F:.2f}<sup>1/3</sup> = {fh:.2f}'), chip('right', 318, 'g', f'D = {Dd:.1f}τ'),
                 chip('right', 532, 'c', f'not F/N = {F / N:.1f}', False)],
                f'F = GBH = 4/3 × 64 = {F:.2f}, f̂ = F<sup>1/3</sup> = <b class="gl">{fh:.3f}</b><br>'
                f'D = 3 × {fh:.3f} + 4 = <b class="gl">{Dd:.1f}τ</b>; C<sub>in</sub> = 1, {c2:.2f}, <b class="cl">{c3:.2f}C</b>')


def u3_l3():
    # Ch 3.6 worked example: driver 1 k -> node1 (20 fF); 2 k -> node2 (30 fF), 1 k -> node4 (40 fF); 3 k -> node3 (10 fF)
    C = {1: 20, 2: 30, 3: 10, 4: 40}
    R = {1: 1, 2: 2, 4: 1, 3: 3}          # resistance into each node from its parent
    up = {1: [1], 2: [1, 2], 4: [1, 2, 4], 3: [1, 3]}
    shared = lambda i, k: sum(R[n] for n in up[i] if n in up[k])
    t4 = sum(C[i] * shared(i, 4) for i in C); t3 = sum(C[i] * shared(i, 3) for i in C)
    terms4 = [C[i] * shared(i, 4) for i in (1, 2, 3, 4)]; terms3 = [C[i] * shared(i, 3) for i in (1, 2, 3, 4)]
    assert (t4, t3) == (280, 130) and terms4 == [20, 90, 10, 160] and terms3 == [20, 30, 40, 40] and round(.69 * t4) == 193 and round(.69 * t3) == 90
    # card: the two Elmore sums as stacked bars, one segment per capacitor
    sx = 330 / 300
    o = []
    cols = ['#5E44B0', VI, '#7F5FE0', '#C9B3FF']
    for row, (name, terms, tot, col) in enumerate((('node 4', terms4, t4, VI), ('node 3', terms3, t3, MI))):
        y = 30 + row * 62; x = 66
        o.append(tx(58, y + 23, name, 'ax', 'end', col))
        for k, v in enumerate(terms):
            w = v * sx
            o.append(rect(x, y, w - 2, 34, cols[k] if row == 0 else ['#167A6C', MI, '#25A592', '#8FF3E2'][k], .9, rx=2))
            if w > 30:
                o.append(tx(x + w / 2, y + 23, str(v), 'pt', 'middle', '#120F31', 15))
            x += w
        o.append(tx(x + 8, y + 23, f'{tot} ps', 'pt', 'start', col))
    o.append(tx(235, 142, 'C<tspan dy="3" font-size="10">i</tspan><tspan dy="-3"> × shared R, in fF × kΩ = ps</tspan>', 'ax', 'middle', TX))
    card = svg(''.join(o))
    setup(318)
    nodes = {1: (4.2, 1.1), 2: (5.7, 1.1), 4: (7.2, 1.1), 3: (5.6, 3.6)}
    b = [ic(1.8, .6, 1.2, 1.0, .6, 'drv', TX, 13, 3), trace([(3.0, 1.1), (7.2, 1.1)], CU, 4),
         trace([(4.2, 1.1), (4.2, 3.6), (5.6, 3.6)], CU, 4), trace([(3.0, 1.1), (7.2, 1.1)], VI, 4, glow=True, op=.8)]
    for (x, y, lbl, hor) in ((3.6, 1.1, '1k', True), (4.95, 1.1, '2k', True), (6.45, 1.1, '1k', True), (4.2, 2.4, '3k', False)):
        b.append(box(x - (.4 if hor else .2), y - (.2 if hor else .4), .8 if hor else .4, .4 if hor else .8, .3, *RES))
        b.append(lab(x, y, .3, lbl, '#3A3426', 12, dy=4))
    for k in (1, 2, 3, 4):
        x, y = nodes[k]; y -= .75; cx, cy = P(x, y, 0)
        hot = k == 4
        b.append(trace([(x, y + .75), (x, y)], CU, 3))
        b.append(cyl(cx, cy, 15, 9, 18 + C[k] * .9, '#3A2F72' if hot else '#2B323C', VI if hot else '#9AA4AE'))
        b.append(lab(x, y, (18 + C[k] * .9) / 33, f'{C[k]}', '#120F31' if hot else '#1A1D22', 12, dy=4))
        b.append(lab(x, y, 0, f'n{k}', VI if hot else TX, 14, 'start', dy=24))
    return spec('u3-L3', 'Elmore Delay<br>&amp; Power<br>Dissipation', 'Which R multiplies each C?',
                'Each C × the R it <span class="gold">shares</span><br>with the <span class="cyan">path</span> to the node',
                'RC tree, nodes 4 and 3', card, board(b),
                [chip('left', 296, 'c', 'driver 1 kΩ, C<sub>1</sub> = 20 fF'), chip('left', 360, 'c', 'path to n4: 1 + 2 + 1 kΩ'),
                 chip('left', 424, 'g', 'C<sub>2</sub> sees 1 + 2 = 3 kΩ'), chip('right', 318, 'g', f'τ<sub>D4</sub> = {t4} ps'),
                 chip('right', 500, 'c', f'τ<sub>D3</sub> = {t3} ps', False)],
                f'τ<sub>D4</sub> = 20×1 + 30×3 + 10×1 + 40×4 = <b class="gl">{t4} ps</b><br>'
                f'τ<sub>D3</sub> = 20×1 + 30×1 + 10×4 + 40×1 = <b class="cl">{t3} ps</b>')


def u3_l4():
    # Ch 3.8 worked example 2: block leaks 0.5 mW; one sleep and wake costs 1.5 nJ; idle 2 us and 10 us
    Pl, E = .5e-3, 1.5e-9
    tbe = E / Pl
    net = {t: Pl * t * 1e-6 - E for t in (2, 10)}
    assert round(tbe * 1e6, 6) == 3 and round(net[2] * 1e9, 3) == -.5 and round(net[10] * 1e9, 3) == 3.5
    X = lambda t: 50 + t / 12 * 370
    Y = lambda e: 122 - e / 6 * 100
    o = [ln(50, 122, 430, 122), ln(50, 18, 50, 122), tx(44, Y(6) + 5, '6', 'ax', 'end'), tx(44, Y(0) + 5, '0', 'ax', 'end'), tx(44, Y(3) + 5, '3', 'ax', 'end'),
         tx(60, 24, 'nJ', 'ax', 'start'), tx(438, 140, 'µs', 'ax', 'start')]
    for t in (0, 3, 6, 9, 12):
        o.append(tx(X(t), 140, str(t), 'ax'))
    o += [pl([(X(0), Y(0)), (X(12), Y(Pl * 12e-6 * 1e9))], MI, 3.2), ln(X(0), Y(E * 1e9), X(12), Y(E * 1e9), VI, 3, '8 5'),
          tx(X(5.5), Y(4.6), 'leakage 0.5 mW × t', 'ax', 'end', MI), tx(X(12) - 2, Y(1.5) + 18, 'wake cost 1.5 nJ', 'ax', 'end', VI),
          ln(X(3), Y(1.5), X(3), 122, TX, 1.5, '3 4'), dot(X(3), Y(1.5), VI, 6), tx(X(3) + 8, Y(1.5) - 10, '3 µs', 'pt', 'start', VI)]
    for t, c in ((2, '#F28B8B'), (10, MI)):
        o.append(dot(X(t), Y(Pl * t * 1e-6 * 1e9), c, 5.5))
    o.append(tx(X(10) + 10, Y(5) + 22, '+3.5 nJ', 'pt', 'start', MI))
    card = svg(''.join(o))
    setup(318)
    b = [trace([(1.2, .8), (7.6, .8)], CU, 7), lab(7.7, .8, 0, 'V<tspan dy="3" font-size="10">DD</tspan>', CU, 15, 'start', dy=5),
         trace([(4.9, .8), (4.9, 1.4)], CU, 4),
         ic(4.2, 1.4, 1.4, 1.0, .7, 'sleep', '#F3EEFF', 14, 3, VIO),
         trace([(4.9, 2.4), (4.9, 3.2)], VI, 4, glow=True),
         ic(3.6, 3.2, 3.4, 2.4, .9, 'logic block', TX, 16, 6),
         lab(5.9, 2.5, 0, 'virtual V<tspan dy="3" font-size="9">DD</tspan>', VI, 13, 'start', dy=6)]
    for k in range(4):
        x, y = P(4.2 + k * .8, 5.6, .3)
        b.append(f'<g filter="url(#gl)">{arrow(x, y + 2, x, y + 40, MI, 3.5)}</g>')
    b.append(lab(4.2, 5.6, 0, 'leaks 0.5 mW', MI, 14, 'end', dy=44))
    return spec('u3-L4', 'Low-power<br>Design &amp; Static<br>CMOS Logic', 'Does clock gating stop leakage?',
                'Clock gating leaves the <span class="gold">leak</span>;<br>power gating pays after <span class="cyan">3 µs</span>',
                'when does gating pay?', card, board(b),
                [chip('left', 296, 'c', 'leakage 0.5 mW'), chip('left', 360, 'c', 'sleep + wake = 1.5 nJ'),
                 chip('left', 424, 'c', '2 µs idle: −0.5 nJ'), chip('right', 318, 'g', 'break-even 3 µs'),
                 chip('right', 532, 'c', '10 µs idle: +3.5 nJ', False)],
                f'break-even = 1.5 nJ ÷ 0.5 mW = <b class="gl">3 µs</b><br>'
                f'idle 10 µs: <b class="cl">+3.5 nJ</b>; idle 2 µs: −0.5 nJ', h1=68)


def u3_l5():
    # Ch 3.10 worked example: nMOS pass gate, gate = input = 1.8 V; Vt0 = 0.5 V, gamma = 0.4, 2phiF = 0.7 V
    VDD, Vt0, gam, phi2 = 1.8, .5, .4, .7
    v0 = VDD - Vt0
    vtn = lambda vy: Vt0 + gam * (math.sqrt(phi2 + vy) - math.sqrt(phi2))
    seq = [v0]
    for _ in range(3):
        seq.append(VDD - vtn(seq[-1]))
    v = seq[-1]
    assert round(v0, 2) == 1.30 and [round(s, 3) for s in seq[1:3]] == [1.069, 1.103] and round(v, 2) == 1.10 and round(vtn(v), 2) == .70
    y0, sc = 118, 92 / 2.0
    Y = lambda x: y0 - x * sc
    o = [ln(40, y0, 460, y0), ln(40, 20, 40, y0), tx(34, Y(1.8) + 5, '1.8', 'ax', 'end'), tx(34, y0 + 5, '0', 'ax', 'end'),
         ln(40, Y(VDD), 460, Y(VDD), TX, 1.5, '6 5', .7)]
    bars = [('nMOS, no body effect', v0, '#7F5FE0', .45), ('nMOS, body effect', v, VI, .9), ('transmission gate', VDD, MI, .9)]
    for k, (n_, val, c, op) in enumerate(bars):
        x = 70 + k * 136
        o += [rect(x, Y(val), 76, y0 - Y(val), c, op, rx=2), tx(x + 38, Y(val) - 7, f'{val:.2f} V' if k < 2 else f'{g(val)} V', 'pt', 'middle', c), tx(x + 38, 136, n_, 'ax')]
    card = svg(''.join(o), 144)
    setup(318)
    b = [trace([(2.6, 1.2), (3.4, 1.2)], CU, 4), trace([(4.8, 1.2), (6.4, 1.2)], VI, 4, glow=True),
         trace([(3.0, 6.6), (3.0, 4.4), (3.4, 4.4)], CU, 4), trace([(4.8, 4.4), (6.4, 4.4)], MI, 4, glow=True),
         ic(3.4, .6, 1.4, 1.2, .7, 'nMOS', '#0C2A26', 14, 3, MNT),
         ic(3.4, 3.5, 1.4, .9, .6, 'nMOS', '#0C2A26', 12, 3, MNT), ic(3.4, 4.4, 1.4, .9, .6, 'pMOS', '#F3EEFF', 12, 3, VIO)]
    for (y, lv, c) in ((1.2, v / VDD, VI), (4.4, 1.0, MI)):
        cx, cy = P(6.8, y, 0); h = 52
        b.append(cyl(cx, cy, 22, 12, h, '#2B323C', '#55606E'))
        b.append(f'<path d="M{cx - 22:.1f},{cy - h * lv:.1f} A22,12 0 0 0 {cx + 22:.1f},{cy - h * lv:.1f} V{cy:.1f} A22,12 0 0 1 {cx - 22:.1f},{cy:.1f}Z" fill="{c}" opacity=".75"/>')
    b += [lab(2.6, 1.2, 0, 'in 1.8 V', CU, 14, 'end', dy=5), lab(3.0, 6.6, 0, 'in 1.8 V', CU, 14, dy=22),
          lab(6.8, 1.2, 0, 'Y', VI, 15, 'start', dy=30), lab(6.8, 4.4, 0, 'Y', MI, 15, 'start', dy=30)]
    return spec('u3-L5', 'Pass<br>Transistors &amp;<br>Dynamic Logic', 'Does an nMOS pass a full 1?',
                'An nMOS passes a <span class="gold">weak 1</span>;<br>a TG passes the <span class="cyan">full</span> 1.8 V',
                'passing a 1 at V<sub>DD</sub> = 1.8 V', card, board(b),
                [chip('left', 296, 'c', 'gate = input = 1.8 V'), chip('left', 360, 'c', 'V<sub>t0</sub> = 0.5 V, γ = 0.4 √V'),
                 chip('left', 424, 'g', f'V<sub>tn</sub> rises to {vtn(v):.2f} V'), chip('right', 318, 'g', f'nMOS: {v:.2f} V'),
                 chip('right', 500, 'c', 'TG: full 1.8 V', False)],
                f'V<sub>Y</sub> = 1.8 − V<sub>tn</sub>(V<sub>Y</sub>): 1.30 → 1.069 → 1.103 → <b class="gl">{v:.2f} V</b><br>'
                f'TG: the pMOS stays on, so Y reaches <b class="cl">1.8 V</b>')


# ================================================================ Unit 4
def u4_l1():
    # Ch 4.1 worked example 2: 32-bit ripple; carry 2 gate delays a bit, sum one XOR after its carry-in; 40 ps a gate
    n, tg = 32, 40
    c = lambda i: 2 * i
    s31, c32 = c(31) + 1, c(32)
    assert (s31, c32) == (63, 64) and s31 * tg == 2520 and c32 * tg == 2560
    X = lambda d: 70 + (d - 56) / 8 * 370
    o = [ln(70, 112, 440, 112), tx(14, 55, 'carry', 'ax', 'start'), tx(14, 97, 'sum', 'ax', 'start'), tx(14, 132, 'delay', 'ax', 'start')]
    for d in (56, 58, 60, 62, 64):
        o += [ln(X(d), 108, X(d), 116, AXC), tx(X(d), 132, str(d), 'ax')]
    o.append(pl([(X(c(i)), 50) for i in range(28, 33)], VI, 3))
    for i in range(28, 33):
        o += [dot(X(c(i)), 50, VI, 7 if i == 32 else 5), tx(X(c(i)), 34, f'c<tspan dy="3" font-size="10">{i}</tspan>', 'pt', 'middle', VI if i == 32 else TX)]
    o += [ln(X(c(31)), 50, X(s31), 92, MI, 2, '5 4'), dot(X(s31), 92, MI, 6),
          tx(X(s31) - 12, 97, f's<tspan dy="3" font-size="10">31</tspan><tspan dy="-3">: {s31} → {s31 * tg / 1e3:.2f} ns</tspan>', 'pt', 'end', MI),
          tx(462, 76, f'{c32 * tg / 1e3:.2f} ns', 'pt', 'end', VI)]
    card = svg(''.join(o))
    setup(318)
    b = []
    xs = [1.4, 2.8, 4.2, 5.8]
    names = ['FA0', 'FA1', 'FA2', 'FA31']
    for k, (x, nm) in enumerate(zip(xs, names)):
        b.append(trace([(x + .55, 2.4), (x + .55, 3.8)], MI, 3, glow=True))
        b.append(ic(x, 1.0, 1.1, 1.4, .7, nm, '#F3EEFF' if k == 3 else TX, 13, 2, VIO if k == 3 else ICC))
    for x0, x1 in ((2.5, 2.8), (3.9, 4.2), (5.3, 5.8)):
        b.append(trace([(x0, 1.7), (x1, 1.7)], VI, 4, glow=True))
    b.append(lab(5.0, 1.7, .2, '…', VI, 22, dy=4))
    b += [trace([(6.9, 1.7), (7.7, 1.7)], VI, 5, glow=True), lab(7.8, 1.7, 0, 'c<tspan dy="3" font-size="10">32</tspan>', VI, 16, 'start', dy=5),
          lab(6.35, 3.8, 0, 's<tspan dy="3" font-size="10">31</tspan>', MI, 15, dy=22), lab(4.75, 3.8, 0, 's<tspan dy="3" font-size="10">2</tspan>', MI, 15, dy=22)]
    return spec('u4-L1', 'Fast Adders<br>&amp; the Carry<br>Chain', 'Which bit of a ripple adder is last?',
                'The carry-out <span class="gold">c<sub>32</sub></span> is last,<br>one gate after <span class="cyan">s<sub>31</sub></span>',
                '32-bit ripple-carry adder', card, board(b),
                [chip('left', 296, 'c', f'{tg} ps per gate delay'), chip('left', 360, 'c', 'carry: 2 gate delays a bit'),
                 chip('left', 424, 'c', f's<sub>31</sub> at {s31} → {s31 * tg / 1e3:.2f} ns'), chip('right', 318, 'g', f'c<sub>32</sub> at {c32} → {c32 * tg / 1e3:.2f} ns'),
                 chip('right', 532, 'g', f'adder needs {c32 * tg / 1e3:.2f} ns', False)],
                f'c<sub>31</sub> at 62; s<sub>31</sub> = p<sub>31</sub> XOR c<sub>31</sub> at {s31} × 40 ps = <b class="cl">{s31 * tg / 1e3:.2f} ns</b><br>'
                f'c<sub>32</sub> at {c32} × 40 ps = <b class="gl">{c32 * tg / 1e3:.2f} ns</b>: the carry-out is last')


def u4_l2():
    # Ch 4.4 worked example: Booth radix-2, Q = 1101, q-1 = 0, M = 0110 (+6)
    M, Q = 6, '1101'
    q = [int(ch) for ch in reversed(Q)]                # q0..q3
    prev = [0] + q[:3]                                  # q(i-1)
    dig = [prev[i] - q[i] for i in range(4)]            # (q_i, q_i-1): (1,0) -> -1, (0,1) -> +1
    val = sum(d * 2 ** i for i, d in enumerate(dig)); prod = M * val
    assert dig == [-1, 1, -1, 0] and val == -3 and prod == -18 and format(prod & 0xFF, '08b') == '11101110'
    sg = lambda d: {1: '+1', -1: '−1', 0: '0'}[d]
    pp = lambda d, i: ('0' if d == 0 else ('+6' if d > 0 else '−6')) + f' × {2 ** i}'
    rows = ''.join(f'<tr><td>{i}</td><td>({q[i]}, {prev[i]})</td><td style="color:{VI if d else TX};font-weight:700">{sg(d)}</td><td>{pp(d, i)}</td></tr>' for i, d in enumerate(dig))
    tbl = f'<table><tr><th>i</th><th>(q<sub>i</sub>, q<sub>i−1</sub>)</th><th>digit</th><th>partial product</th></tr>{rows}</table>'
    setup(318)
    b = []
    bits = list(Q) + ['0']
    qn = ['3', '2', '1', '0', '−1']
    for k, bt in enumerate(bits):
        x = 2.0 + k * 1.15
        c = (MNT if k == 4 else VIO) if bt == '1' else (('#5D6878', '#2A313B', '#3C4552') if k < 4 else ('#4E8F86', '#1D4A44', '#2A6159'))
        b.append(box(x, 1.2, 1.0, 1.0, 1.0, *c))
        b.append(lab(x + .5, 1.7, 1.0, bt, '#120F31' if bt == '1' else TX, 22, dy=8))
        b.append(lab(x + .5, 2.2, 0, f'q<tspan dy="3" font-size="10">{qn[k]}</tspan>', TX, 15, dy=24))
    for i, d in enumerate(dig):         # digit i sits between the q_i and q_i-1 cubes
        x = 2.0 + (3 - i) * 1.15 + 1.075
        b.append(lab(x, 1.7, 1.9, sg(d), VI if d else TX, 20, dy=0))
    mn = lambda v: str(v).replace('-', '−')
    return spec('u4-L2', 'Array, Wallace<br>&amp; Booth<br>Multipliers', 'What does Booth recode 1101 to?',
                '1101 recodes to <span class="gold">−1, +1, −1, 0</span><br>(LSB first): Q = <span class="cyan">−3</span>',
                'Booth radix-2, M = 0110', tbl, board(b),
                [chip('left', 296, 'c', 'M = 0110 = +6'), chip('left', 360, 'c', 'Q = 1101, q<sub>−1</sub> = 0'),
                 chip('left', 424, 'g', 'digits −1, +1, −1, 0'), chip('right', 318, 'c', 'Q = −3'),
                 chip('right', 500, 'g', f'6 × (−3) = {mn(prod)}', False)],
                f'd<sub>0</sub>..d<sub>3</sub> = −1, +1, −1, 0 → −1 + 2 − 4 + 0 = <b class="cl">{mn(val)}</b><br>'
                f'M × Q = 6 × (−3) = <b class="gl">{mn(prod)}</b> = 11101110 in 8 bits', TABLE, h1=70)


def u4_l3():
    # Ch 4.6 worked example: 4-bit SIPO shift register, rising-edge, start 0000, Din = 1, 0, 1, 1
    Din = [1, 0, 1, 1]
    Q = [0, 0, 0, 0]
    hist = [Q[:]]
    for d in Din:
        Q = [d] + Q[:3]
        hist.append(Q[:])
    word = ''.join(str(b_) for b_ in reversed(Q))
    assert [''.join(map(str, h)) for h in hist[1:]] == ['1000', '0100', '1010', '1101'] and word == '1011'
    o = [tx(52, 18, 'edge', 'ax', 'middle'), tx(110, 18, 'D<tspan dy="3" font-size="10">in</tspan>', 'ax', 'middle')]
    for j in range(4):
        o.append(tx(176 + j * 40, 18, f'Q<tspan dy="3" font-size="10">{j}</tspan>', 'ax', 'middle'))
    for r_, h in enumerate(hist):
        y = 28 + r_ * 23
        o.append(tx(52, y + 16, 'start' if r_ == 0 else str(r_), 'ax', 'middle', TX))
        o.append(tx(110, y + 16, '–' if r_ == 0 else str(Din[r_ - 1]), 'pt', 'middle', MI))
        for j, b_ in enumerate(h):
            hot = r_ == 4
            o.append(rect(158 + j * 40, y, 36, 20, (VI if b_ else '#3A3466') if hot else ('#7F5FE0' if b_ else '#2C2654'), .95 if hot else .7, rx=3))
            o.append(tx(176 + j * 40, y + 15, str(b_), 'ax', 'middle', '#120F31' if b_ else TX, 14, 700))
    o += [tx(350, 60, 'read Q<tspan dy="3" font-size="10">3</tspan><tspan dy="-3">..Q</tspan><tspan dy="3" font-size="10">0</tspan>', 'ax', 'start', TX),
          tx(350, 92, word, 'pt', 'start', MI, 26, 700), tx(350, 116, 'the order sent', 'ax', 'start', MI)]
    card = svg(''.join(o), 144)
    setup(318)
    b = [trace([(1.8, 3.8), (7.7, 3.8)], MI, 4, glow=True), lab(7.8, 3.8, 0, 'CLK ↑', MI, 14, 'start', dy=5),
         trace([(1.2, .4), (1.2, 2.4), (1.8, 2.4)], VI, 4, glow=True), lab(1.2, .4, 0, 'D<tspan dy="3" font-size="10">in</tspan>', VI, 15, 'end', dy=-2)]
    for j in range(4):
        x = 1.8 + j * 1.5
        b.append(trace([(x + .6, 3.2), (x + .6, 3.8)], MI, 2.5))
        if j:
            b.append(trace([(x - .3, 2.4), (x, 2.4)], VI, 4, glow=True))
        hot = Q[j] == 1
        b.append(ic(x, 1.6, 1.2, 1.6, .9, str(Q[j]), '#120F31' if hot else TX, 24, 2, VIO if hot else ICC))
        if j:
            b.append(lab(x + .6, 1.6, .9, f'Q<tspan dy="3" font-size="10">{j}</tspan>', TX, 14, dy=-6))
    return spec('u4-L3', 'Decoders,<br>Comparators<br>&amp; Latches', 'Is a D latch edge-triggered?',
                'A register moves at the <span class="gold">edge</span>;<br>a D latch is <span class="cyan">level</span>-sensitive',
                '4-bit serial-in shift register', card, board(b),
                [chip('left', 296, 'c', 'rising-edge stages'), chip('left', 360, 'c', 'D<sub>in</sub> = 1, 0, 1, 1'),
                 chip('left', 424, 'g', 'Q<sub>0</sub>Q<sub>1</sub>Q<sub>2</sub>Q<sub>3</sub> = 1101'), chip('right', 318, 'g', f'word {word}'),
                 chip('right', 532, 'c', 'all stages move at once', False)],
                'each edge: Q<sub>3</sub>←Q<sub>2</sub>, Q<sub>2</sub>←Q<sub>1</sub>, Q<sub>1</sub>←Q<sub>0</sub>, Q<sub>0</sub>←D<sub>in</sub><br>'
                f'1000 → 0100 → 1010 → <b class="gl">1101</b>; Q<sub>3</sub>..Q<sub>0</sub> = <b class="cl">{word}</b>')


def u4_l4():
    # Ch 4.7 worked example: tmult = 3.0 ns, tadd = 1.6 ns, tcq = 0.2 ns, tsu = 0.1 ns
    tm, ta, tcq, tsu = 3.0, 1.6, .2, .1
    T0 = tcq + tm + ta + tsu; T2 = tcq + tm + tsu; T3 = tcq + max(tm / 2, ta) + tsu
    lat = {1: T0, 2: 2 * T2, 3: 3 * T3}; per = {1: T0, 2: T2, 3: T3}
    f3 = 1e3 / T3
    assert close(T0, 4.9) and close(T2, 3.3) and close(T3, 1.9) and close(lat[2], 6.6) and close(lat[3], 5.7) and round(f3, 1) == 526.3 and round(1e3 / T0, 1) == 204.1
    y0, sc = 116, 92 / 7
    Y = lambda t: y0 - t * sc
    o = [ln(36, y0, 300, y0), ln(36, 20, 36, y0), tx(30, Y(6) + 5, '6', 'ax', 'end'), tx(30, y0 + 5, '0', 'ax', 'end'), tx(44, 24, 'ns', 'ax', 'start')]
    for k, st in enumerate((1, 2, 3)):
        x = 56 + k * 82
        o += [rect(x, Y(per[st]), 30, y0 - Y(per[st]), MI, .85, rx=2), rect(x + 33, Y(lat[st]), 30, y0 - Y(lat[st]), VI, .85, rx=2),
              tx(x + 15, Y(per[st]) - 5, g(per[st]), 'ax', 'middle', MI), tx(x + 48, Y(lat[st]) - 5, g(lat[st]), 'ax', 'middle', VI),
              tx(x + 32, 134, ['none', '2 stages', '3 stages'][k], 'ax')]
    o += [rect(318, 40, 14, 14, MI, .85), tx(338, 52, 'clock period', 'ax', 'start', TX), rect(318, 66, 14, 14, VI, .85), tx(338, 78, 'latency', 'ax', 'start', TX),
          tx(318, 112, f'{1e3 / T0:.1f} → {f3:.1f} MHz', 'pt', 'start', MI)]
    card = svg(''.join(o))
    setup(318)
    b = [trace([(2.0, 3.4), (7.7, 3.4)], MI, 3, glow=True), lab(7.8, 3.4, 0, 'clk', MI, 14, 'start', dy=5)]
    stages = [('×½', '1.5'), ('×½', '1.5'), ('+', '1.6')]
    x, tl = 2.0, []
    for k in range(4):
        b.append(trace([(x + .17, 2.8), (x + .17, 3.4)], MI, 2))
        b.append(box(x, 1.2, .35, 1.6, .9, *VIO))
        if k < 3:
            b.append(trace([(x + .35, 2.0), (x + .5, 2.0)], VI, 4, glow=True))
            b.append(ic(x + .5, 1.4, 1.0, 1.2, .6, stages[k][0], TX, 18, 2))
            tl.append(lab(x + 1.0, 1.4, .6, stages[k][1] + ' ns', '#F3EEFF', 13, dy=-10))
            b.append(trace([(x + 1.5, 2.0), (x + 1.65, 2.0)], VI, 4, glow=True))
        x += 1.65
    b += tl
    return spec('u4-L4', 'Pipelining<br>&amp; Circuit<br>Timing', 'Does pipelining cut latency?',
                'Pipelining raises the <span class="cyan">clock</span>;<br>the latency <span class="gold">grows</span>',
                'multiply-add, 3 stages', card, board(b),
                [chip('left', 296, 'c', f't<sub>mult</sub> {tm} ns, t<sub>add</sub> {ta} ns'), chip('left', 360, 'c', f't<sub>cq</sub> {tcq} + t<sub>su</sub> {tsu} ns'),
                 chip('left', 424, 'c', f'T = 0.2 + 1.6 + 0.1 = {T3:.1f} ns'), chip('right', 318, 'g', f'latency {T0} → {lat[3]:.1f} ns'),
                 chip('right', 500, 'c', f'{f3:.1f} MHz', False)],
                f'3 stages: T = {T3:.1f} ns, f = <b class="cl">{f3:.1f} MHz</b> (was {1e3 / T0:.1f})<br>'
                f'latency = 3 × {T3:.1f} = <b class="gl">{lat[3]:.1f} ns</b>, more than {T0} ns')


def u4_l5():
    # Ch 4.10 worked example: 1 Mbit SRAM, 64K x 16, square 1024 x 1024 array
    words, M, side = 64 * 1024, 16, 1024
    K = int(math.log2(words)); r = int(math.log2(side)); c = int(math.log2(side // M))
    assert K == 16 and words * M == 2 ** 20 and (r, c) == (10, 6) and r + c == K and 2 ** c == 64
    o = []
    w = 25
    for i in range(16):
        x = 34 + i * (w + 1)
        row = i < r
        o.append(rect(x, 44, w, 30, VI if row else MI, .9, rx=3))
        o.append(tx(x + w / 2, 64, f'{15 - i}', 'ax', 'middle', '#120F31', 12, 700))
    xr0, xr1 = 34, 34 + r * (w + 1) - 1; xc0, xc1 = xr1 + 1, 34 + 16 * (w + 1) - 1
    o += [tx(34, 30, 'address A15 … A0', 'ax', 'start', TX),
          pl([(xr0, 82), (xr0, 90), (xr1, 90), (xr1, 82)], VI, 2), tx((xr0 + xr1) / 2, 110, f'{r} row bits → {side} wordlines', 'pt', 'middle', VI),
          pl([(xc0 + 2, 82), (xc0 + 2, 90), (xc1, 90), (xc1, 82)], MI, 2), tx((xc0 + xc1) / 2, 132, f'{c} column bits → 64:1', 'pt', 'middle', MI)]
    card = svg(''.join(o))
    setup(312)
    b = [box(1.4, 1.8, 4.6, 4.6, .5, '#3A3466', '#1A1640', '#262058')]
    for k in range(1, 9):
        b.append(trace([(1.4 + k * .511, 1.8), (1.4 + k * .511, 6.4)], '#7F5FE0', 1.2, z=.51, op=.7))
        b.append(trace([(1.4, 1.8 + k * .511), (6.0, 1.8 + k * .511)], '#7F5FE0', 1.2, z=.51, op=.7))
    b += [box(6.2, 1.8, 1.0, 4.6, .8, *VIO), lab(6.7, 4.1, .8, 'row', '#1A1238', 14, dy=0), lab(6.7, 4.1, .8, 'decoder', '#1A1238', 12, dy=14),
          trace([(6.2, 3.33), (1.4, 3.33)], VI, 3, z=.52, glow=True),
          box(1.4, 6.6, 4.6, .9, .6, *MNT), lab(3.4, 7.5, 0, '16 × (64:1 mux + sense amp)', MI, 14, dy=50),
          lab(4.6, 3.4, .5, '1024 × 1024', '#E2D6FF', 18, dy=6)]
    return spec('u4-L5', 'Memory Cells<br>&amp; Memory<br>Architecture', 'How is a 64K × 16 SRAM folded?',
                '<span class="gold">10</span> row bits + <span class="cyan">6</span> column bits<br>fold it into a square',
                '64K × 16 into 1024 × 1024', card, board(b),
                [chip('left', 296, 'c', '64K × 16 = 1 Mbit'), chip('left', 360, 'c', f'{side} × {side} cells'),
                 chip('left', 424, 'g', f'row decoder: {r} bits'), chip('right', 318, 'c', f'{c} column bits: 64:1'),
                 chip('right', 532, 'c', '16 sense amplifiers', False)],
                f'64K = 2<sup>16</sup> words; {side} rows = 2<sup>10</sup> → <b class="gl">r = {r}</b><br>'
                f'{side} = 16 × 2<sup>c</sup> → <b class="cl">c = {c}</b>: a 64:1 mux per output bit')


# ================================================================ Unit 5
def u5_l1():
    # Ch 5.2 worked example: FPGA NRE 0, Rs 1,800 a chip; gate array NRE Rs 40 lakh, Rs 500 a chip; standard cell 2 crore / 250; full custom 8 crore / 200
    n1 = 40e5 / (1800 - 500); n2 = (200e5 - 40e5) / (500 - 250); n3 = (800e5 - 200e5) / (250 - 200)
    assert round(n1) == 3077 and n2 == 64000 and n3 == 12e5
    cost = lambda nre, u, N: (nre + u * N) / 1e5       # Rs lakh
    X = lambda N: 52 + N / 6000 * 380
    Y = lambda L: 122 - L / 120 * 100
    o = [ln(52, 122, 440, 122), ln(52, 18, 52, 122), tx(46, Y(100) + 5, '100', 'ax', 'end'), tx(46, Y(50) + 5, '50', 'ax', 'end'), tx(46, 127, '0', 'ax', 'end'),
         tx(60, 24, '₹ lakh', 'ax', 'start'), tx(440, 140, 'chips', 'ax', 'end')]
    for N in (0, 2000, 4000):
        o.append(tx(X(N), 140, f'{N:,}', 'ax'))
    o += [pl([(X(0), Y(cost(0, 1800, 0))), (X(6000), Y(cost(0, 1800, 6000)))], MI, 3.2),
          pl([(X(0), Y(cost(40e5, 500, 0))), (X(6000), Y(cost(40e5, 500, 6000)))], VI, 3.2),
          tx(X(5200), Y(cost(0, 1800, 5200)) - 10, 'FPGA', 'pt', 'end', MI), tx(X(5600), Y(cost(40e5, 500, 5600)) + 22, 'gate array', 'pt', 'end', VI)]
    ce = cost(0, 1800, n1)
    o += [ln(X(n1), Y(ce), X(n1), 122, TX, 1.5, '3 4'), dot(X(n1), Y(ce), TX, 6), tx(X(n1) - 10, Y(ce) - 10, f'{n1:,.0f} chips', 'pt', 'end', TX)]
    card = svg(''.join(o))
    setup(318)
    b = [ic(2.0, .8, 2.4, 2.4, .5, 'FPGA', MI, 17, 6), ic(4.8, 3.6, 2.2, 2.2, .5, 'gate array', VI, 15, 6),
         lab(4.75, 2.0, 0, '₹0 NRE + ₹1,800 a chip', MI, 13, 'start', dy=5), lab(5.9, 5.8, 0, '₹40 lakh NRE + ₹500 a chip', VI, 13, dy=28)]
    return spec('u5-L1', 'Design Flow<br>&amp; ASICs', 'Where do two chip costs break even?',
                'Split the <span class="gold">NRE</span> gap by<br>the <span class="cyan">per-chip</span> gap',
                'FPGA or gate array?', card, board(b),
                [chip('left', 296, 'c', 'FPGA: ₹0 + ₹1,800 a chip'), chip('left', 360, 'g', 'gate array: ₹40 lakh NRE'),
                 chip('left', 424, 'g', 'then ₹500 a chip'), chip('right', 318, 'g', f'break-even {n1:,.0f} chips'),
                 chip('right', 532, 'c', '50,000 → gate array', False)],
                f'₹40,00,000 ÷ (1,800 − 500) = <b class="gl">{n1:,.0f} chips</b><br>'
                f'next: <b class="cl">64,000</b> (standard cell), 12 lakh (full custom)')


def u5_l2():
    # Ch 5.3 worked example: 4-bit unsigned a = 4, b = 3, c = 2, d = 1; y = a + b * c > d ? (a << 1) : ~b
    a, b_, c, d = 4, 3, 2, 1
    m = b_ * c; s = a + m; cond = s > d
    t, f = (a << 1) & 0xF, (~b_) & 0xF
    y = t if cond else f
    assert (m, s, cond, t, f, y) == (6, 10, True, 8, 12, 8) and format(y, '04b') == '1000' and format(f, '04b') == '1100'
    steps = [('b * c', '3 * 2 = 6', TX), ('a + 6', '4 + 6 = 10', TX), ('10 &gt; d', 'true', TX), ('a &lt;&lt; 1', '8 = 1000, taken', VI), ('~b', '1100 = 12, not taken', MI)]
    o = []
    for k, (l, r_, col) in enumerate(steps):
        y0 = 22 + k * 25
        o += [tx(20, y0, f'{k + 1}.', 'ax', 'start'), tx(44, y0, l, 'pt', 'start', TX, 16), tx(140, y0, '→', 'ax', 'start'), tx(164, y0, r_, 'pt', 'start', col, 16)]
    o += [rect(352, 26, 104, 92, 'rgba(183,156,255,.10)', 1, VI, 8), tx(404, 52, 'y =', 'ax', 'middle', TX), tx(404, 86, '4\'b1000', 'pt', 'middle', VI, 20), tx(404, 108, '= 8', 'pt', 'middle', VI)]
    card = svg(''.join(o), 136)
    setup(318)
    bv = []
    rows = [('b', format(b_, '04b'), ('#5D6878', '#2A313B', '#3C4552'), .5), ('~b', format(f, '04b'), MNT, 2.1), ('y', format(y, '04b'), VIO, 3.7)]
    for name, bits, c1, yy in rows:
        for k, bt in enumerate(bits):
            x = 2.6 + k * 1.25
            col = c1 if bt == '1' else ('#3A4150', '#1A1F28', '#262C38')
            bv.append(box(x, yy, 1.0, 1.0, .8, *col))
            bv.append(lab(x + .5, yy + .5, .8, bt, '#120F31' if bt == '1' else TX, 20, dy=7))
        bv.append(lab(7.75, yy + .5, .4, name, MI if name == '~b' else (VI if name == 'y' else TX), 18, 'start', dy=6))
    return spec('u5-L2', 'Verilog<br>Operators &amp;<br>Modelling Levels', "Is !4'b0011 equal to ~4'b0011?",
                '~ flips <span class="cyan">every bit</span>: 1100;<br>! gives <span class="gold">one bit</span>: 0',
                'y = a + b*c &gt; d ? (a&lt;&lt;1) : ~b', card, board(bv),
                [chip('left', 296, 'c', 'a = 4, b = 3, c = 2, d = 1'), chip('left', 360, 'c', '* before +, + before &gt;'),
                 chip('left', 424, 'c', '10 &gt; 1 is true'), chip('right', 318, 'g', "y = 8 = 4'b1000"),
                 chip('right', 532, 'c', "~4'b0011 = 4'b1100", False)],
                f'b*c = 6, a + 6 = 10, 10 &gt; 1 true → y = a&lt;&lt;1 = <b class="gl">8</b><br>'
                f"~b = ~4'b0011 = <b class=\"cl\">4'b1100</b> = 12, the branch not taken", h1=64)


def u5_l3():
    # Ch 5.6 worked example: 4-input LUT for f = A.B + C.D; read at ABCD = 1101; 3,000 functions, 15 % packing loss
    f = lambda A, B_, C, D_: (A & B_) | (C & D_)
    bits = [f((i >> 3) & 1, (i >> 2) & 1, (i >> 1) & 1, i & 1) for i in range(16)]
    hit = 0b1101; need = math.ceil(3000 / .85)
    assert len(bits) == 16 and hit == 13 and bits[hit] == 1 and need == 3530 and round(3000 / .85, 1) == 3529.4
    o = [tx(14, 22, 'ABCD', 'ax', 'start'), tx(14, 76, 'f', 'ax', 'start')]
    w = 24
    for i, bt in enumerate(bits):
        x = 52 + i * (w + 1)
        hot = i == hit
        o.append(tx(x + w / 2, 22, format(i, '04b')[:2], 'ax', 'middle', VI if hot else '#9AA4AE', 10))
        o.append(tx(x + w / 2, 34, format(i, '04b')[2:], 'ax', 'middle', VI if hot else '#9AA4AE', 10))
        o.append(rect(x, 54, w, 30, (VI if hot else (MI if bt else '#2C2654')), .95 if hot else (.75 if bt else .8), stroke='#F3EEFF' if hot else None))
        o.append(tx(x + w / 2, 75, str(bt), 'pt', 'middle', '#120F31' if bt else TX, 16))
    xh = 52 + hit * (w + 1) + w / 2
    o += [ln(xh, 88, xh, 104, VI, 2), tx(xh, 124, 'ABCD = 1101 = 13 → f = 1', 'pt', 'end', VI), tx(52, 140, '16 entries, one bit each', 'ax', 'start', MI)]
    card = svg(''.join(o))
    setup(318)
    b = []
    for i in range(16):
        r_, c_ = divmod(i, 4)
        x, y = 2.6 + c_ * .95, .5 + r_ * .95
        bt = bits[i]; hot = i == hit
        col = VIO if hot else (MNT if bt else ('#3A4150', '#1A1F28', '#262C38'))
        b.append(box(x, y, .8, .8, .45 if not hot else .8, *col))
        b.append(lab(x + .4, y + .4, .45 if not hot else .8, str(bt), '#120F31' if bt else TX, 14, dy=5))
    b += [trace([(6.4, 2.4), (6.7, 2.4)], VI, 3, glow=True), box(6.7, 1.4, 1.0, 2.0, .7, *ICC), lab(7.2, 2.4, .7, 'mux', TX, 15, dy=5),
          trace([(7.2, 3.4), (7.2, 4.6)], VI, 5, glow=True), lab(7.2, 4.6, 0, 'f = 1', VI, 17, dy=24)]
    for k in range(4):
        b.append(trace([(6.9 + k * .2, .1), (6.9 + k * .2, 1.4)], MI, 2.5, glow=True))
    b.append(lab(7.2, .1, 0, 'ABCD = 1101', MI, 14, 'start', dy=-6))
    return spec('u5-L3', 'Test Benches<br>&amp; Programmable<br>Logic', 'How many bits does a 4-input LUT hold?',
                'A 4-input LUT stores <span class="gold">16</span> bits,<br>one per <span class="cyan">input row</span>',
                'LUT for f = A·B + C·D', card, board(b),
                [chip('left', 296, 'g', '2⁴ = 16 config bits'), chip('left', 360, 'c', 'f = A·B + C·D'),
                 chip('left', 424, 'c', 'ABCD = 1101 → 13'), chip('right', 318, 'g', 'f = 1'),
                 chip('left', 488, 'c', f'3,000 ÷ 0.85 → {need} LUTs', False)],
                '4 inputs → 2<sup>4</sup> = <b class="gl">16</b> entries, one bit each<br>'
                f'3,000 ÷ 0.85 = 3529.4 → <b class="cl">{need} LUTs</b>', h1=66)


def u5_l4():
    # Ch 5.7 worked example: core 3.0 x 3.0 mm; blocks 2.0, 1.5, 1.0, 0.5 mm^2; cells 1.8 mm^2; 20 % extra for routing
    core = 3.0 * 3.0; blocks = [2.0, 1.5, 1.0, .5]; cells = 1.8
    used = sum(blocks) + cells; util = used / core; extra = .2 * used; tot = used + extra; spare = core - tot
    assert close(sum(blocks), 5.0) and close(used, 6.8) and round(util * 100, 1) == 75.6 and close(tot, 8.16) and close(spare, .84)
    sx = 420 / core
    o = []
    x = 24
    segs = [('blocks 5.0', sum(blocks), VI, .9), ('cells 1.8', cells, MI, .85), ('+20 % 1.36', extra, '#7F5FE0', .5), ('spare 0.84', spare, '#3A3466', .9)]
    for k, (n_, v, c, op) in enumerate(segs):
        w = v * sx
        o.append(rect(x, 34, w - 2, 40, c, op, rx=3))
        o.append(tx(x + w / 2, 96 + (k % 2) * 20, n_, 'ax', 'middle', c if c != '#3A3466' else TX))
        x += w
    o += [tx(24, 24, 'core 9.0 mm²', 'ax', 'start', TX), tx(444, 24, 'mm²', 'ax', 'end'),
          ln(24 + used * sx, 28, 24 + used * sx, 80, TX, 1.5, '3 3'), tx(24 + used * sx, 140, f'used {used:.1f} = {util * 100:.1f} %', 'pt', 'middle', VI)]
    card = svg(''.join(o))
    setup(316)
    u = 2.0      # board units per mm
    X0, Y0 = 1.8, .2
    b = [box(X0, Y0, 3 * u, 3 * u, .15, '#2E3A6A', '#151B36', '#1F2850')]
    side = {a_: math.sqrt(a_) * u for a_ in blocks}
    place = {2.0: (X0, Y0), 1.5: (X0 + side[2.0] + .1, Y0), 1.0: (X0 + 3 * u - side[1.0], Y0 + side[1.5] + .1), .5: (4.2, Y0 + side[2.0] + .1)}
    for a_ in blocks:
        (x, y), s_ = place[a_], side[a_]
        b.append(box(x, y, s_, s_, .7 if a_ > .6 else .55, *VIO, z0=.15))
        b.append(lab(x + s_ / 2, y + s_ / 2, .85 if a_ > .6 else .7, f'{a_}', '#1A1238', 15, dy=6))
    # standard-cell rows: 4 rows 0.32 deep holding 1.8 mm^2 = 7.2 board units^2, along the front of the core
    nrow, dep = 4, .32
    wrow = cells * u * u / (nrow * dep)
    assert close(nrow * dep * wrow, 7.2) and wrow <= 3 * u
    for k in range(nrow):
        b.append(box(X0 + 3 * u - wrow, 4.86 + k * .335, wrow, dep, .3, *MNT, z0=.15))
    assert 4.86 + (nrow - 1) * .335 + dep <= Y0 + 3 * u
    b.append(lab(X0 + 3 * u - wrow / 2 + 1.0, 5.5, .45, 'cells 1.8', '#0C2A26', 14, dy=6))
    return spec('u5-L4', 'Physical<br>Design &amp;<br>IP Cores', 'Is a DRC-clean layout ready to ship?',
                'DRC checks only <span class="gold">geometry</span>:<br><span class="cyan">LVS</span> and timing still due',
                'a 3.0 × 3.0 mm core', card, board(b),
                [chip('left', 296, 'c', 'core 3.0 × 3.0 mm'), chip('left', 360, 'g', 'blocks 2.0 + 1.5 + 1.0 + 0.5'),
                 chip('left', 424, 'c', 'cells 1.8 mm²'), chip('right', 318, 'g', f'utilization {util * 100:.1f} %'),
                 chip('right', 532, 'c', f'+20 %: {tot:.2f} ≤ 9.0 mm²', False)],
                f'(5.0 + 1.8) ÷ 9.0 = <b class="gl">{util * 100:.1f} %</b>, whitespace {core - used:.1f} mm²<br>'
                f'6.8 × 1.2 = {tot:.2f} mm² fits with <b class="cl">{spare:.2f} mm²</b> spare')


# ================================================================ Unit 6
def u6_l1():
    # Ch 6.1 worked example: yield Y = 0.90; DL = 1 - Y^(1 - T); T = 0.95 and 0.99
    Yd = .90
    DL = lambda T_: (1 - Yd ** (1 - T_)) * 1e6
    a, b2 = DL(.95), DL(.99)
    assert round(a) == 5254 and round(b2) == 1053 and round(a / b2, 2) == 4.99 and DL(1.0) == 0
    X = lambda T_: 60 + (T_ - .9) / .1 * 370
    Yp = lambda d: 122 - d / 11000 * 100
    o = [ln(60, 122, 440, 122), ln(60, 18, 60, 122), tx(54, Yp(10000) + 5, '10,000', 'ax', 'end'), tx(54, Yp(5000) + 5, '5,000', 'ax', 'end'), tx(54, 127, '0', 'ax', 'end'),
         tx(68, 24, 'DPM', 'ax', 'start'), tx(338, 140, 'fault coverage T', 'ax', 'middle')]
    for T_ in (.9, .95, 1.0):
        o.append(tx(X(T_), 140, f'{T_:.2f}', 'ax'))
    o.append(pl([(X(.9 + k * .0025), Yp(DL(.9 + k * .0025))) for k in range(41)], VI, 3.2))
    o += [dot(X(.95), Yp(a), VI, 6), tx(X(.95) + 10, Yp(a) - 8, f'{a:.0f}', 'pt', 'start', VI),
          dot(X(.99), Yp(b2), MI, 6), tx(X(.99) - 8, Yp(b2) - 12, f'{b2:.0f}', 'pt', 'end', MI)]
    card = svg(''.join(o))
    setup(318)
    wx, wy, R, pd = 5.0, 3.4, 2.57, .72          # wafer centre, die circle, die pitch (board units)
    cx, cy = P(wx, wy, 0)
    b = [cyl(cx, cy, 2.85 * 40.4, 2.85 * 23.3, 12, '#7D8792', '#C9D0D6')]
    die = [(i, j) for i in range(-5, 5) for j in range(-5, 5)
           if all((i * pd + a) ** 2 + (j * pd + c) ** 2 <= R * R for a in (0, .62) for c in (0, .62))]
    bad = {(-3, 0), (1, -2), (0, 2)}
    assert len(die) == 30 and bad <= set(die) and round((len(die) - len(bad)) / len(die), 2) == Yd
    for (i, j) in die:
        c = ('#F28B8B', '#8C3E3E', '#B85C5C') if (i, j) in bad else (('#E2D6FF', '#6A4FC0', '#9C80F2') if (i + j) % 2 else ('#D4C6FF', '#5E44B0', '#8F6BF0'))
        b.append(box(wx + i * pd, wy + j * pd, .62, .62, .12, *c, z0=.37))
    b.append(lab(wx, wy + 2.85, 0, f'Y = {Yd:.2f}: {len(die) - len(bad)} of {len(die)} dies good', TX, 14, dy=34))
    return spec('u6-L1', 'Testing Chips<br>&amp; Finding<br>Faults', 'Does 100% coverage ship zero bad chips?',
                '100 % of the <span class="gold">modelled</span> faults<br>still lets <span class="cyan">other</span> defects out',
                'defect level, Y = 0.90', card, board(b),
                [chip('left', 296, 'c', 'yield Y = 0.90'), chip('left', 360, 'g', f'T = 0.95 → {a:.0f} DPM'),
                 chip('left', 424, 'c', f'T = 0.99 → {b2:.0f} DPM'), chip('right', 318, 'g', f'{a / b2:.2f}× fewer escapes'),
                 chip('right', 500, 'c', 'DL = 1 − Y<sup>1−T</sup>', False)],
                f'DL = 1 − 0.90<sup>0.05</sup> = 0.005254 → <b class="gl">{a:.0f} DPM</b><br>'
                f'DL = 1 − 0.90<sup>0.01</sup> = 0.001053 → <b class="cl">{b2:.0f} DPM</b>')


def u6_l2():
    # Ch 6.6 worked example: 4-bit LFSR, shift left, f = b3 xor b0 into b0, seed 0001
    s = 0b0001; seen = []
    while True:
        seen.append(s)
        f = ((s >> 3) & 1) ^ (s & 1)
        s = ((s << 1) & 0xF) | f
        if s == seen[0]: break
    names = [format(v, '04b') for v in seen]
    assert len(seen) == 15 and 0 not in seen and names[:5] == ['0001', '0011', '0111', '1111', '1110'] and names[-1] == '1000'
    o = []
    for k, nm in enumerate(names):
        r_, c_ = divmod(k, 5)
        x, y = 16 + c_ * 92, 14 + r_ * 42
        o.append(rect(x, y, 66, 28, VI if k == 0 else '#2C2654', .95 if k == 0 else .9, stroke=None if k == 0 else '#7F5FE0'))
        o.append(tx(x + 33, y + 20, nm, 'pt', 'middle', '#120F31' if k == 0 else TX, 16))
        if c_ < 4:
            o.append(tx(x + 79, y + 20, '→', 'ax', 'middle', MI))
    o.append(tx(470 - 14, 140, f'{len(seen)} states, then 0001 again; 0000 never', 'ax', 'end', MI))
    card = svg(''.join(o))
    setup(318)
    pos = {3: (3.4, 1.0), 2: (6.6, 1.0), 1: (6.6, 4.2), 0: (3.4, 4.2)}      # b3 b2 b1 b0 round a loop
    z = .45
    def arr(p0, p1, col, w=5):
        a_, b2_ = P(*p0, z), P(*p1, z)
        return f'<g filter="url(#gl)">{arrow(a_[0], a_[1], b2_[0], b2_[1], col, w)}</g>'
    b = [arr((4.5, 4.7), (6.5, 4.7), VI), arr((7.1, 4.1), (7.1, 2.1), VI), arr((6.5, 1.5), (4.5, 1.5), VI),   # shift b0 -> b1 -> b2 -> b3
         arr((3.8, 2.1), (4.6, 2.75), MI, 4), arr((4.3, 4.1), (4.85, 3.45), MI, 4), arr((4.55, 3.35), (3.95, 4.1), '#F3EEFF', 4)]
    xc, yc = P(4.95, 3.05, 0)
    b.append(cyl(xc, yc, 26, 15, 24, '#167A6C', '#8FF3E2'))
    b.append(lab(4.95, 3.05, .73, 'XOR', '#0C2A26', 13, dy=5))
    seed = {3: 0, 2: 0, 1: 0, 0: 1}
    for k, (x, y) in pos.items():
        hot = seed[k] == 1
        b.append(box(x, y, 1.0, 1.0, .9, *(VIO if hot else ('#5D6878', '#2A313B', '#3C4552'))))
        b.append(lab(x + .5, y + .5, .9, str(seed[k]), '#120F31' if hot else TX, 22, dy=8))
        b.append(lab(x + .5, y + 1.0, 0, f'b<tspan dy="3" font-size="10">{k}</tspan>', TX, 15, dy=24) if k != 3 else
                 lab(x, y + .5, 0, 'b<tspan dy="3" font-size="10">3</tspan>', TX, 15, 'end', dy=5))
    b.append(lab(4.2, 3.9, 0, 'f', '#F3EEFF', 15, 'end', dy=4))
    return spec('u6-L2', 'Making Chips<br>Testable', "Is a 4-bit LFSR's period 16?",
                'Period <span class="gold">15</span>, not 16:<br><span class="cyan">0000</span> never appears',
                '4-bit LFSR from seed 0001', card, board(b),
                [chip('left', 296, 'c', 'seed 0001'), chip('left', 360, 'c', 'f = b<sub>3</sub> XOR b<sub>0</sub> into b<sub>0</sub>'),
                 chip('left', 424, 'c', 'shift left each clock'), chip('right', 318, 'g', f'period {len(seen)} = 2⁴ − 1'),
                 chip('right', 532, 'g', '0000 never appears', False)],
                '0001 → 0011 → 0111 → 1111 → … → 1000 → 0001<br>'
                f'<b class="gl">{len(seen)}</b> = 2<sup>4</sup> − 1 states: maximal-length, <b class="cl">not 16</b>')


def u6_l3():
    # Ch 6.7 worked example: March C- on 1024 addresses, 5 ns per access; GALPAT about 4n^2
    els = [('⇕(w0)', 1), ('⇑(r0,w1)', 2), ('⇑(r1,w0)', 2), ('⇓(r0,w1)', 2), ('⇓(r1,w0)', 2), ('⇕(r0)', 1)]
    n, ta = 1024, 5
    k = sum(c for _, c in els); acc = k * n; tm = acc * ta / 1e3; gal = 4 * n * n; tg = gal * ta / 1e6
    assert k == 10 and acc == 10240 and close(tm, 51.2) and gal == 4194304 and round(tg, 2) == 20.97 and round(gal / acc, 1) == 409.6
    o = []
    for i, (nm, c) in enumerate(els):
        x = 10 + i * 76
        o += [rect(x, 22, 70, 46, '#2C2654', .95, stroke='#7F5FE0'), tx(x + 35, 41, nm, 'ax', 'middle', TX, 12), tx(x + 35, 61, str(c), 'pt', 'middle', VI, 17)]
        if i < 5:
            o.append(tx(x + 73, 50, '+', 'ax', 'middle', VI))
    o += [tx(235, 98, f'k = {k} ops per address → {k} × {n} = {acc:,} accesses', 'pt', 'middle', VI, 16),
          tx(235, 128, f'× 5 ns = {tm} µs   ·   GALPAT 4n² = {gal:,}', 'ax', 'middle', MI)]
    card = svg(''.join(o))
    setup(318)
    b = [box(2.6, .8, 3.4, 4.8, .5, '#3A3466', '#1A1640', '#262058')]
    for j in range(1, 12):
        b.append(trace([(2.6, .8 + j * .4), (6.0, .8 + j * .4)], '#7F5FE0', 1.2, z=.51, op=.7))
    b.append(box(2.6, 3.2, 3.4, .4, .56, *VIO))
    b.append(lab(4.3, 3.4, .56, 'address i', '#1A1238', 13, dy=5))
    for (x, y0_, y1_, col) in ((6.5, 1.0, 5.4, MI), (7.3, 5.4, 1.0, VI)):
        p1, p2 = P(x, y0_, .3), P(x, y1_, .3)
        b.append(f'<g filter="url(#gl)">{arrow(p1[0], p1[1], p2[0], p2[1], col, 5)}</g>')
    b += [lab(6.5, 5.4, .3, '⇑ up', MI, 15, 'end', dy=22), lab(7.3, 1.0, .3, '⇓ down', VI, 15, 'start', dy=-8),
          lab(4.3, 5.6, 0, '1024 addresses', TX, 14, dy=26)]
    return spec('u6-L3', 'Memory, SoC<br>&amp; Analog Test', 'Is March C− 10n or 10n² long?',
                'March C− is <span class="gold">10n</span>,<br>GALPAT about <span class="cyan">4n²</span>',
                'March C−, n = 1024', card, board(b),
                [chip('left', 296, 'c', f'{n} addresses'), chip('left', 360, 'g', f'k = {k} ops each'),
                 chip('left', 424, 'c', f'{ta} ns per access'), chip('right', 318, 'g', f'{acc:,} accesses: {tm} µs'),
                 chip('right', 532, 'c', f'GALPAT: {tg:.2f} ms', False)],
                f'March C−: {k} × {n} = <b class="gl">{acc:,}</b> accesses = {tm} µs<br>'
                f'GALPAT: 4 × 1024² = {gal:,}, <b class="cl">{gal / acc:.1f}×</b> longer')


HOOKS = None


def specs():
    out = [u1_l1(), u1_l2(), u1_l3(), u2_l1(), u2_l2(), u2_l3(), u2_l4(), u3_l1(), u3_l2(), u3_l3(), u3_l4(), u3_l5(),
           u4_l1(), u4_l2(), u4_l3(), u4_l4(), u4_l5(), u5_l1(), u5_l2(), u5_l3(), u5_l4(), u6_l1(), u6_l2(), u6_l3()]
    # subject and hook must match thumbs.json when it sits next to this file
    tj = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'thumbs.json')
    if os.path.exists(tj):
        import json, html
        L = json.load(open(tj, encoding='utf-8'))['lessons']
        for s in out:
            t = L[s['key']]
            assert html.unescape(s['question']) == t['hook'], (s['key'], s['question'], t['hook'])
            assert s['subject'] == t['subject'], s['key']
            assert html.unescape(s['title'].replace('<br>', ' ')) == t['topic'], (s['key'], s['title'], t['topic'])
    return out
