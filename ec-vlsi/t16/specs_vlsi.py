"""t16 cubes drawings for VLSI Design (ec-vlsi), Stage look.
S['ec-vlsi-uN-Lk'] = fn(f) -> (figure, note), as specs_d.py does. Every number is computed here from the lesson's
own worked example (lesson branches lesson/ec-vlsi-uN-Lk, books/ece/ec-vlsi/ on main).
G[key] = the plain grid block (rows, cols, raised, note) that t16.py checks."""
import math
from h import *
S, G = {}, {}
def sp(k):
    def d(fn): S['ec-vlsi-' + k] = fn; return fn
    return d
WH = '#FFFFFF'
import free16
free16.TONES['w'] = ('linear-gradient(150deg,#FFFFFF,#EEF3FA)', '#8FA9CF', '#A9BCD9', '#FFFFFF', '#7F98BF', '#1F2A44')
# a cube face is a flex box: wrap text that carries <sub>/<sup> in one span so the spaces around the tags survive
_cell = Fig.cell
def _cell_span(s, x, y, w, h, txt='', kind='t', fs=None, D=None, color=None):
    t = str(txt)
    return _cell(s, x, y, w, h, f'<span>{t}</span>' if '<' in t else txt, kind, fs, D, color)
Fig.cell = _cell_span
def wcube(f, x, y, w, h, txt='', D=24, fs=22):
    txt = f'<span>{txt}</span>' if '<' in str(txt) else txt
    f.items.append((1, free16.cube(x, y, w, h, txt, D, 'w', fs))); f._box(x, y, w, h)

def path(f, pts, hot=False, w=None, dash=False, col=None):
    """a polyline (curves, wires) in the figure's coordinates"""
    c = col or ('#FF9A2E' if hot else '#8FB0DD'); sw = w or (7 if hot else 5)
    d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    da = ' stroke-dasharray="12 10"' if dash else ''
    f.lines.append(f'<path d="{d}" fill="none" stroke="#0C2D73" stroke-width="{sw + 8}" stroke-linejoin="round" stroke-linecap="round" opacity=".25"{da}/>'
                   f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"{da}/>')
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    f._box(min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys))

def fmt(v, n=2):
    s = f'{v:.{n}f}'
    return s.rstrip('0').rstrip('.') if '.' in s else s

# ------------------------------------------------------------------ Unit 1
@sp('u1-L1')
def _(f):
    # Worked example 1 (and the exam trap): CMOS inverter, VDD = 1.8 V, VTn = 0.5 V, VTp = −0.5 V, Vin = 0.8 V, Vout = 1.5 V
    VDD, VTn, VTp, Vin, Vout = 1.8, 0.5, 0.5, 0.8, 1.5
    vsg, vsd = VDD - Vin, VDD - Vout; ovp = vsg - VTp
    vgs, ovn = Vin, Vin - VTn
    p_reg = 'linear' if vsd < ovp else 'saturated'; n_reg = 'saturated' if Vout >= ovn else 'linear'
    assert round(vsg, 2) == 1.0 and vsg >= VTp and p_reg == 'linear' and n_reg == 'saturated'
    f.cell(0, 0, 640, 46, 'VDD = 1.8 V', 't', fs=24, color=NV); f.cell(0, 540, 640, 46, 'GND', 't', fs=24, color=NV)
    f.cell(90, 90, 170, 110, 'pMOS', 'o', fs=32); f.cell(90, 390, 170, 110, 'nMOS', 'p', fs=32)
    for a, b in [((175, 46), (175, 90)), ((175, 200), (175, 390)), ((175, 500), (175, 540))]: path(f, [a, b], False, 7)
    path(f, [(175, 295), (300, 295)], False, 7); f.cell(300, 262, 200, 66, 'out 1.5 V', 't', fs=26, color=NV)
    f.text(-60, 270, 'in', 26, GR, 900, 'center'); f.text(-60, 304, '0.8 V', 26, GR, 900, 'center')
    path(f, [(-20, 295), (20, 295), (20, 145), (90, 145)], False, 6); path(f, [(20, 295), (20, 445), (90, 445)], False, 6)
    f.text(300, 120, f'V<sub>SG</sub> = {vsg:.1f} V ≥ 0.5 V', 28, OR, 900); f.text(300, 162, f'ON, {p_reg}', 28, OR, 900)
    f.text(300, 430, f'V<sub>GS</sub> = {vgs:.1f} V', 26, GR, 900); f.text(300, 468, n_reg, 26, GR, 900)
    return 'CMOS inverter at Vin = 0.8 V (worked example 1)', f'V<sub>SG</sub> = {vsg:.1f} V ≥ 0.5 V: the pMOS is <b>on</b>'
G['ec-vlsi-u1-L1'] = dict(rows=2, cols=6, flat='', raised={f'0,{j}': '' for j in range(6)}, note='the channel thins toward the <b>drain</b>')

@sp('u1-L2')
def _(f):
    # Worked example 3: W = 1 µm, L = 0.25 µm, tox = 4 nm, Lov = 0.02 µm, εox = 3.45 × 10⁻¹¹ F/m
    Cox = 3.45e-11 / 4e-9 * 1e3                      # F/m² → fF/µm²: 8.625
    W, L, Lov = 1, 0.25, 0.02
    CWL, Cov = Cox * W * L, Cox * W * Lov
    Cgs, Cgd = 2 / 3 * CWL + Cov, Cov
    assert round(Cgs, 2) == 1.61 and round(Cgd, 2) == 0.17 and round(Cgs + Cgd, 2) == 1.78 and round(CWL, 2) == 2.16
    f.cell(60, 0, 480, 76, 'gate', 'o', fs=30)
    f.cell(-90, 110, 130, 70, 'S', 'p', fs=30); f.cell(560, 110, 130, 70, 'D', 'p', fs=30)
    f.cell(60, 116, 150, 58, '1/3', 'o', fs=24); f.cell(225, 116, 150, 58, '1/3', 'o', fs=24); f.cell(390, 116, 150, 58, 'pinched', 'g', fs=20)
    f.text(60, 214, '2/3 of C<sub>ox</sub>WL → source', 24, OR, 900); f.text(690, 214, 'nothing → drain', 24, GR, 900, 'right')
    f.cell(-90, 270, 780, 72, f'C<sub>gs</sub> = 2/3 × {CWL:.2f} + {Cov:.2f} = {Cgs:.2f} fF', 'o', fs=27)
    f.cell(-90, 370, 780, 66, f'C<sub>gd</sub> = C<sub>ov</sub> = {Cgd:.2f} fF', 't', fs=25, color=NV)
    return 'MOSFET capacitances in saturation (worked example 3)', 'in saturation C<sub>gs</sub> takes <b>two-thirds</b> of C<sub>ox</sub>WL'
G['ec-vlsi-u1-L2'] = dict(rows=3, cols=5, flat='', raised={'0,3': '1', '0,4': '1', '1,1': '.75', '1,2': '.9'}, note='I<sub>D</sub> = <b>1 mA</b> once saturated')

@sp('u1-L3')
def _(f):
    # Worked example 2: SS = 80 mV/decade, φt = 26 mV; limit SS = 2.3·φt (n = 1)
    phit = 26.0; lim = 2.3 * phit; SS = 80.0; n = SS / lim
    assert round(lim) == 60 and round(n, 2) == 1.34
    sx, dy, X0, Y0 = 1300, 90, 90, 400                # 1300 px per volt, 90 px per decade
    P = lambda v, dec: (X0 + v * sx, Y0 - dec * dy)
    path(f, [P(0, 0), P(0.36, 0)], False, 4); path(f, [P(0, 0), P(0, 4.3)], False, 4)
    for d, lab in enumerate(['10 nA', '100 nA', '1 µA', '10 µA', '100 µA']):
        f.text(X0 - 14, Y0 - d * dy, lab, 20, GR, 900, 'right')
    path(f, [P(0, 0), P(4 * lim / 1e3, 4)], False, 6, True); path(f, [P(0, 0), P(4 * SS / 1e3, 4)], True, 8)
    f.cell(*[c - 40 for c in P(4 * lim / 1e3, 4)], 80, 50, '60', 'p', fs=24)
    f.cell(P(4 * SS / 1e3, 4)[0] - 10, P(4 * SS / 1e3, 4)[1] - 25, 80, 50, '80', 'o', fs=24)
    f.text(P(0.36, 0)[0], Y0 + 32, 'V<sub>GS</sub>', 24, GR, 900, 'right'); f.text(X0 + 10, Y0 - 4.3 * dy - 10, 'log I<sub>D</sub>', 22, GR, 900)
    f.cell(80, 470, 520, 70, f'2.3 × {phit:.0f} mV = {lim:.0f} mV / decade', 'o', fs=26)
    return 'Subthreshold current on a log scale', f'SS = 2.3·n·φ<sub>t</sub> ≥ <b>{lim:.0f} mV</b>/decade, as n ≥ 1'
G['ec-vlsi-u1-L3'] = dict(rows=2, cols=5, flat='', raised={'0,0': '30', '0,2': '30', '0,4': '30', '1,1': '10'}, note='one fin gives <b>70 nm</b> of width')

# ------------------------------------------------------------------ Unit 2
@sp('u2-L1')
def _(f):
    # Worked example 4: 0.5 µm oxide, 2.0 µm window, 100 nm/min, 20 % over-etch; RIE hole 2.12 µm (book)
    tox, win, rate, over = 0.5, 2.0, 0.1, 0.2
    t = tox / rate * (1 + over)                       # 6.0 min
    wet = win + 2 * rate * t                          # isotropic: lateral = vertical
    rie = 2.12
    assert abs(t - 6.0) < 1e-9 and abs(wet - 3.2) < 1e-9
    U, cw = 120, 4.6 * 120
    for k, (name, hole, y0) in enumerate([('wet etch', wet, 0), ('RIE', rie, 270)]):
        cx = cw / 2; hot = k == 0
        f.text(-20, y0 + 70, name, 28, OR if hot else NV, 900, 'right')
        a, b = cx - win * U / 2, cx + win * U / 2
        f.cell(0, y0, a, 40, '', 'p', D=22); f.cell(b, y0, cw - b, 40, '', 'p', D=22)
        ha, hb = cx - hole * U / 2, cx + hole * U / 2
        wcube(f, 0, y0 + 50, ha, 80, '', 30); wcube(f, hb, y0 + 50, cw - hb, 80, '', 30)
        f.cell(0, y0 + 140, cw, 44, '', 'g')
        path(f, [(ha + 6, y0 + 90), (hb - 6, y0 + 90)], hot, 5)
        f.text(cx, y0 + 116, f'{fmt(hole)} µm', 26, OR if hot else NV, 900, 'center')
    f.text(cw + 60, 20, 'resist', 22, GR, 900); f.text(cw + 60, 90, 'oxide', 22, GR, 900); f.text(cw + 60, 162, 'silicon', 22, GR, 900)
    f.text(cw / 2, -34, f'{win:.1f} µm window', 22, GR, 900, 'center')
    return 'Wet etch against reactive ion etching', f'same {win:.1f} µm window: wet etch opens <b>{fmt(wet)} µm</b>'
G['ec-vlsi-u2-L1'] = dict(rows=2, cols=6, flat='', raised={'1,1': '', '1,2': '', '1,3': '', '1,4': ''}, note='wet etch opens <b>3.2 µm</b>')

@sp('u2-L2')
def _(f):
    # n-well process (Worked example 3): µn = 500, µp = 200 cm²/V·s, Wn = 2 µm → Wp/Wn = 2.5, Wp = 5 µm
    mun, mup, Wn = 500, 200, 2
    Wp = Wn * mun / mup
    assert Wp == 5
    f.cell(0, 200, 760, 170, '', 'g')
    f.text(160, 330, 'p-substrate', 24, '#6B7487', 900, 'center')
    wcube(f, 400, 170, 340, 170, '', 16); f.text(570, 310, 'n-well', 26, OR, 900, 'center')
    f.cell(40, 150, 100, 70, 'n<sup>+</sup>', 'p', fs=26); f.cell(220, 150, 100, 70, 'n<sup>+</sup>', 'p', fs=26); wcube(f, 145, 110, 70, 50, '', 30)
    f.cell(430, 140, 100, 70, 'p<sup>+</sup>', 'o', fs=26); f.cell(610, 140, 100, 70, 'p<sup>+</sup>', 'o', fs=26); wcube(f, 535, 100, 70, 50, '', 30)
    f.text(180, 50, f'NMOS · W = {Wn} µm', 26, NV, 900, 'center'); f.text(570, 40, f'PMOS · W = {Wp:.0f} µm', 26, OR, 900, 'center')
    return 'n-well CMOS inverter in cross-section', 'only the <b>PMOS</b> sits in the n-well'
G['ec-vlsi-u2-L2'] = dict(rows=2, cols=5, flat='', raised={f'{i // 5},{i % 5}': str(i + 1) for i in range(10)}, note='<b>10</b> masks for one CMOS chip')

@sp('u2-L3')
def _(f):
    # Worked example 3: λ = 0.5 µm, metal 1 width 3λ, spacing 3λ; pitch centre to centre
    lam = 0.5; wid, sp_ = 3, 3
    pitch = wid + sp_; wrong = wid + 2 * sp_
    assert pitch * lam == 3.0 and wrong * lam == 4.5
    U = 40
    for i in range(3):
        f.cell(i * pitch * U, 80, wid * U, 340, 'metal 1' if i == 1 else '', 'o' if i < 2 else 'p', fs=20, D=34)
    c0, c1 = wid * U / 2, pitch * U + wid * U / 2
    path(f, [(c0, 40), (c1, 40)], True, 6); path(f, [(c0, 22), (c0, 58)], True, 5); path(f, [(c1, 22), (c1, 58)], True, 5)
    f.text((c0 + c1) / 2, 4, f'pitch = {pitch}λ = {pitch * lam:.1f} µm', 28, OR, 900, 'center')
    f.text(wid * U / 2, 460, '3λ', 26, NV, 900, 'center'); f.text(wid * U + sp_ * U / 2, 460, '3λ', 26, GR, 900, 'center')
    f.text(wid * U / 2, 500, 'width', 20, GR, 900, 'center'); f.text(wid * U + sp_ * U / 2, 500, 'spacing', 20, GR, 900, 'center')
    return 'Metal 1 width, spacing and pitch (λ = 0.5 µm)', f'pitch = width + spacing = <b>{pitch}λ = {pitch * lam:.1f} µm</b>'
G['ec-vlsi-u2-L3'] = dict(rows=4, cols=6, flat='', raised={'0,2': 'L', '1,2': '', '2,2': '', '3,2': ''}, note='W = 8λ, L = 2λ: C<sub>g</sub> = <b>9.2 fF</b>')

@sp('u2-L4')
def _(f):
    # Worked example 2: 2 mA spike into the substrate, npn needs 0.7 V; βnpn = 50, βpnp = 20
    I, Vbe, bn, bp = 2e-3, 0.7, 50, 20
    V = {R: I * R for R in (200, 500)}
    assert round(V[200], 2) == 0.4 and round(V[500], 2) == 1.0 and V[200] < Vbe <= V[500] and bn * bp == 1000
    f.cell(0, 0, 220, 100, f'pnp · β {bp}', 'p', fs=26); f.cell(0, 300, 220, 100, f'npn · β {bn}', 'o', fs=26)
    path(f, [(220, 60), (290, 60), (290, 330), (226, 330)], True, 8); path(f, [(0, 360), (-60, 360), (-60, 40), (-6, 40)], True, 8)
    f.text(-80, 200, 'loop gain 1000', 22, OR, 900, 'right')
    f.cell(320, 20, 200, 60, 'R<sub>well</sub> 1 kΩ', 't', fs=22, color=NV); f.cell(320, 320, 200, 60, 'R<sub>sub</sub>', 't', fs=22, color=NV)
    wcube(f, 0, 470, 560, 64, f'200 Ω × 2 mA = {V[200]:.1f} V: off', 22, 24)
    f.cell(0, 560, 560, 70, f'500 Ω × 2 mA = {V[500]:.1f} V ≥ 0.7 V: on', 'o', fs=25)
    return 'The latch-up loop (worked example 2)', 'it starts once the drop reaches <b>0.7 V</b>: 500 Ω does it'
G['ec-vlsi-u2-L4'] = dict(rows=3, cols=3, flat='', raised={'0,0': 'c', '0,1': 'a', '0,2': 'b', '2,0': 'c', '2,1': 'a', '2,2': 'b'}, note='one poly order <b>c, a, b</b>')

# ------------------------------------------------------------------ Unit 3
@sp('u3-L1')
def _(f):
    # Worked example 1: matched inverter, VDD = 3.3 V, Vtn = |Vtp| = 0.6 V, kn = kp
    VDD, Vt = 3.3, 0.6
    def i_n(vi, vo):
        v = vi - Vt
        return 0 if v <= 0 else (v * vo - vo * vo / 2 if vo < v else v * v / 2)
    def i_p(vi, vo):
        v = VDD - vi - Vt; vsd = VDD - vo
        return 0 if v <= 0 else (v * vsd - vsd * vsd / 2 if vsd < v else v * v / 2)
    def vout(vi):
        lo, hi = 0.0, VDD
        for _ in range(60):
            m = (lo + hi) / 2
            if i_n(vi, m) > i_p(vi, m): hi = m
            else: lo = m
        return (lo + hi) / 2
    VM = VDD / 2; VIL = (3 * VDD + 2 * Vt) / 8; VIH = (5 * VDD - 2 * Vt) / 8
    NML = VIL - 0; NMH = VDD - VIH
    assert abs(VM - 1.65) < 1e-9 and round(NML, 2) == 1.39 and round(NMH, 2) == 1.39 and round(VIH, 2) == 1.91
    s, X0, Y0 = 120, 60, 440
    P = lambda a, b: (X0 + a * s, Y0 - b * s)
    path(f, [P(0, 0), P(3.4, 0)], False, 4); path(f, [P(0, 0), P(0, 3.45)], False, 4)
    pts = [P(v / 200, vout(v / 200)) for v in range(0, 661)]
    path(f, pts, True, 7)
    for v, lab in [(VIL, 'V<sub>IL</sub>'), (VIH, 'V<sub>IH</sub>')]:
        x, y = P(v, vout(v)); path(f, [(x, y), (x, Y0)], False, 3, True)
        f.cell(x - 22, y - 22, 44, 44, '', 'p', D=22)
        f.text(x, Y0 + 32, lab, 24, GR, 900, 'center')
    x, y = P(VM, VM); f.cell(x - 26, y - 26, 52, 52, '', 'o', D=30)
    f.text(x + 46, y - 6, 'V<sub>M</sub> = 1.65 V', 28, OR, 900)
    f.text(X0 + 3.4 * s, Y0 + 30, 'V<sub>in</sub>', 24, GR, 900, 'right'); f.text(X0 - 12, Y0 - 3.45 * s, 'V<sub>out</sub>', 24, GR, 900, 'right')
    f.text(P(2.3, 3.05)[0], P(2.3, 3.05)[1], 'slope −1 at V<sub>IL</sub>, V<sub>IH</sub>', 22, GR, 900, 'center')
    return 'CMOS inverter transfer curve, VDD = 3.3 V', f'matched k<sub>n</sub> = k<sub>p</sub>: it switches at <b>V<sub>M</sub> = {VM:.2f} V</b>'
G['ec-vlsi-u3-L1'] = dict(rows=4, cols=4, flat='', raised={'0,0': '1', '0,1': '1', '1,1': '', '2,2': '', '3,2': '0', '3,3': '0'}, note='both noise margins <b>1.39 V</b>')

@sp('u3-L2')
def _(f):
    # Worked example 1: inverter → NAND2 → inverter, input C, load 64C
    g = [1, 4 / 3, 1]; p = [1, 2, 1]; H = 64
    F = math.prod(g) * H; fh = F ** (1 / 3); D = 3 * fh + sum(p)
    cin3 = H * g[2] / fh; cin2 = cin3 * g[1] / fh
    assert round(fh, 2) == 4.40 and round(D, 1) == 17.2 and round(cin3, 2) == 14.54 and round(cin2, 2) == 4.40
    names = ['INV', 'NAND2', 'INV']; caps = ['1C', f'{cin2:.2f}C', f'{cin3:.2f}C']
    for i in range(3):
        x = 60 + i * 190
        f.cell(x, 100, 140, 110, names[i], 'o' if i == 1 else 'p', fs=24)
        f.text(x + 70, 60, f'g = {"4/3" if i == 1 else "1"}', 20, GR, 900, 'center')
        f.cell(x - 10, 250, 160, 56, caps[i], 't', fs=22, color=NV)
        if i: arrow(f, x - 46, 155, x - 6, 155)
    f.cell(640, 110, 110, 90, '64C', 't', fs=26, color=NV); arrow(f, 586, 155, 634, 155)
    f.text(-10, 155, 'C', 26, GR, 900, 'right')
    f.text(390, 350, 'input C of each stage', 18, GR, 900, 'center')
    f.cell(60, 400, 660, 70, f'f̂ = F<sup>1/3</sup> = ∛{F:.1f} = {fh:.2f}', 'o', fs=26)
    return 'Every stage bears the same effort', f'f̂ = F<sup>1/N</sup> = <b>{fh:.2f}</b>, not F/N = {F / 3:.1f}'
G['ec-vlsi-u3-L2'] = dict(rows=2, cols=4, flat='', raised={'0,0': '1', '0,1': '4.4', '0,2': '15', '0,3': '64'}, note='each stage bears <b>4.40</b>')

@sp('u3-L3')
def _(f):
    # Worked example 1: RC tree; R in kΩ, C in fF → kΩ·fF = ps
    R = {'1': 1, '2': 2, '4': 1, '3': 3}; C = {'1': 20, '2': 30, '4': 40, '3': 10}
    up = {'1': None, '2': '1', '4': '2', '3': '1'}
    def anc(n):
        s = set()
        while n: s.add(n); n = up[n]
        return s
    def tau(i): return sum(C[k] * sum(R[r] for r in anc(i) & anc(k)) for k in C)
    t4, t3 = tau('4'), tau('3')
    assert (t4, t3) == (280, 130)
    N = {'drv': (0, 60, 't', 'in'), 'n1': (190, 60, 'p', '1'), 'n2': (380, 60, 'p', '2'), 'n4': (570, 60, 'o', '4'), 'n3': (190, 300, 't', '3')}
    graph(f, N, [('drv', 'n1', '1k', True), ('n1', 'n2', '2k', True), ('n2', 'n4', '1k', True), ('n1', 'n3', '3k', False)], 90)
    shared = lambda k: sum(R[r] for r in anc('4') & anc(k))
    prods = {k: C[k] * shared(k) for k in C}
    assert [prods[k] for k in '1234'] == [20, 90, 10, 160]
    for n, (x, y, k, t) in N.items():
        if n == 'drv': continue
        lab = f'{C[t]} fF × {shared(t)}k'
        if n == 'n3': f.text(x + 112, y + 45, lab, 22, OR, 900)
        else: f.text(x + 45, y + 128, lab, 21, OR if t == '3' else GR, 900, 'center')
    f.cell(170, 400, 500, 90, f'τ<sub>D4</sub> = 20 + 90 + 10 + 160 = {t4} ps', 'o', fs=26)
    return 'An RC tree, path to node 4', f'each C × the R it <b>shares</b> with the path: {t4} ps'
G['ec-vlsi-u3-L3'] = dict(rows=2, cols=4, flat='', raised={'0,0': '1k', '0,1': '2k', '0,2': '1k', '1,0': '3k'}, note='τ<sub>D4</sub> = <b>280 ps</b>')

@sp('u3-L4')
def _(f):
    # Worked example 2: the block leaks 0.5 mW; one sleep and wake-up costs 1.5 nJ
    Pl, E = 0.5e-3, 1.5e-9
    tbe = E / Pl
    assert round(tbe * 1e6, 6) == 3 and round((Pl * 10e-6 - E) * 1e9, 3) == 3.5
    table(f, [['-off', '*0.5 mW'], ['-off', '-off']], 0, 0, 200, 90, 16, rowh=['clock gating', 'power gating'], hfs=26)
    f.text(100, -60, 'dynamic', 26, GR, 900, 'center'); f.text(316, -60, 'leakage', 26, OR, 900, 'center')
    f.cell(-280, 260, 712, 76, f'power gating pays after 1.5 nJ ÷ 0.5 mW = {tbe * 1e6:.0f} µs', 'p', fs=25)
    return 'Clock gating against power gating', 'clock gating stops switching; the block still <b>leaks</b>'
G['ec-vlsi-u3-L4'] = dict(rows=2, cols=3, flat='', raised={'0,0': '2', '0,1': '4', '0,2': '4', '1,0': '2', '1,1': '2', '1,2': '2'}, note='B and C get <b>g = 2</b>')

@sp('u3-L5')
def _(f):
    # Worked example 1: nMOS switch, VDD = 1.8 V, Vt0 = 0.5 V, γ = 0.4 √V, 2φF = 0.7 V
    VDD, Vt0, gam, p2 = 1.8, 0.5, 0.4, 0.7
    v0 = VDD - Vt0
    v = v0
    for _ in range(200): v = VDD - (Vt0 + gam * (math.sqrt(p2 + v) - math.sqrt(p2)))
    assert round(v0, 2) == 1.30 and round(v, 1) == 1.1
    f.cell(0, 60, 120, 70, '1.8 V', 't', fs=24, color=NV); f.cell(220, 50, 130, 90, 'nMOS', 'p', fs=24); f.cell(470, 60, 130, 70, f'{v:.2f} V', 'o', fs=26)
    arrow(f, 124, 95, 214, 95); arrow(f, 356, 95, 464, 95, True)
    f.text(285, 14, 'gate 1.8 V', 19, GR, 900, 'center'); f.text(535, 170, 'weak 1', 20, OR, 900, 'center')
    f.cell(0, 300, 120, 70, '1.8 V', 't', fs=24, color=NV)
    f.cell(220, 250, 130, 70, 'nMOS', 'p', fs=22); f.cell(220, 340, 130, 70, 'pMOS', 'p', fs=22)
    f.cell(470, 300, 130, 70, '1.8 V', 't', fs=26, color=NV)
    arrow(f, 124, 335, 214, 290); arrow(f, 124, 335, 214, 375); arrow(f, 356, 290, 464, 330); arrow(f, 356, 375, 464, 340)
    f.text(285, 450, 'transmission gate', 20, GR, 900, 'center'); f.text(535, 410, 'full 1', 20, GR, 900, 'center')
    return 'Pass transistor against transmission gate', f'an nMOS passes a weak 1: <b>{v:.2f} V</b>, not 1.8 V'
G['ec-vlsi-u3-L5'] = dict(rows=2, cols=3, flat='', raised={'0,0': '1.8', '0,2': '1.1', '1,0': '1.8', '1,2': '1.8'}, note='an nMOS passes a weak 1: <b>1.10 V</b>')

# ------------------------------------------------------------------ Unit 4
@sp('u4-L1')
def _(f):
    # Worked example 2: 32-bit ripple, carry-in to carry-out 2 gate delays, sum one XOR after its carry-in, 40 ps a gate
    n, tg = 32, 40
    carry = lambda i: 2 * i                 # c_i settles at 2i gate delays
    s31, c32 = carry(31) + 1, carry(32)
    assert (s31, c32) == (63, 64) and c32 * tg == 2560
    bits = [0, 1, 2, None, 30, 31]
    for k, b in enumerate(bits):
        x = k * 120
        if b is None: f.text(x + 45, 140, '…', 40, GR, 900, 'center'); continue
        f.cell(x, 100, 90, 90, f'FA {b}', 'o' if b == 31 else 'p', fs=22)
        f.text(x + 45, 60, f'c<sub>{b + 1}</sub>: {carry(b + 1)}', 22, OR if b == 31 else GR, 900, 'center')
        if k < len(bits) - 1 and bits[k + 1] is not None: arrow(f, x + 94, 145, x + 116, 145, b == 30)
    f.cell(0, 260, 330, 70, f's<sub>31</sub> at {s31}', 't', fs=26, color=NV)
    f.cell(360, 250, 330, 90, f'c<sub>32</sub> at {c32}', 'o', fs=30)
    f.text(345, 400, f'{c32} × {tg} ps = {c32 * tg / 1e3:.2f} ns', 28, OR, 900, 'center')
    return '32-bit ripple-carry timing (worked example 2)', f'the carry-out c<sub>32</sub> is last: <b>{c32 * tg / 1e3:.2f} ns</b>'
G['ec-vlsi-u4-L1'] = dict(rows=2, cols=5, flat='0', raised={'0,1': '1', '0,2': '1', '0,3': '1', '1,0': '1', '1,4': '1'}, note='11 + 6 = <b>10001</b>')

@sp('u4-L2')
def _(f):
    # Worked example 3: Booth radix-2, Q = 1101, q−1 = 0, M = 0110 (+6)
    Q, M = '1101', 6
    q = [int(c) for c in reversed(Q)] + [0]          # q0..q3, then q−1 at index 4 (used as q[i-1] for i = 0)
    dig = [(q[i - 1] if i else 0) - q[i] for i in range(4)]
    val = sum(d * 2 ** i for i, d in enumerate(dig)); P = val * M
    assert dig == [-1, 1, -1, 0] and val == -3 and P == -18
    sg = lambda d: {1: '+1', -1: '−1', 0: '0'}[d]
    row(f, list(Q) + ['+0'], 0, 0, 90, 80, 14, idx=['q<sub>3</sub>', 'q<sub>2</sub>', 'q<sub>1</sub>', 'q<sub>0</sub>', 'q<sub>−1</sub>'], ifs=22)
    row(f, [('*' if d else '-') + sg(d) for d in reversed(dig)], 0, 170, 90, 80, 14)
    for i in range(4): f.text(i * 104 + 97, 132, f'{Q[i]}{(Q + "0")[i + 1]}', 18, GR, 900, 'center')
    f.text(-20, 210, 'digits', 22, OR, 900, 'right')
    f.cell(0, 300, 504, 70, f'{val} × (+{M}) = {P}', 'o', fs=28)
    return 'Booth radix-2 recoding of Q = 1101', 'Booth recodes 1101 to <b>0, −1, +1, −1</b> = −3'
G['ec-vlsi-u4-L2'] = dict(rows=2, cols=6, flat='0', raised={'1,0': '1', '1,4': '1', '1,5': '1', '0,2': '1', '0,3': '1'}, note='13 × 11 = <b>143</b>')

@sp('u4-L3')
def _(f):
    # Latch against register: a gated D latch is transparent while CLK = 1; a register samples at the rising edge
    CLK = [0, 1, 1, 1, 0, 0, 1, 1, 0, 0]; D = [0, 1, 0, 1, 1, 1, 1, 0, 0, 1]
    lq, rq, l, r = [], [], 0, 0
    for t in range(10):
        if CLK[t]: l = D[t]
        if CLK[t] and (t == 0 or not CLK[t - 1]): r = D[t]
        lq.append(l); rq.append(r)
    assert lq != rq and lq == [0, 1, 0, 1, 1, 1, 1, 0, 0, 0]
    rows = [[('+1' if v else '-0') for v in CLK], [('1' if v else '0') for v in D], [('*1' if v else '0') for v in lq], [('+1' if v else '0') for v in rq]]
    table(f, rows, 0, 0, 56, 60, 8, rowh=['CLK', 'D', 'latch Q', 'register Q'], hfs=22)
    return 'Gated D latch against master-slave register', 'while CLK = 1 the latch Q <b>follows</b> D: level, not edge'
G['ec-vlsi-u4-L3'] = dict(rows=2, cols=4, flat='0', raised={'0,1': 'Y1', '0,2': 'Y2', '1,1': 'Y5', '1,3': 'Y7'}, note='OR of <b>Y<sub>1</sub> Y<sub>2</sub> Y<sub>5</sub> Y<sub>7</sub></b>')

@sp('u4-L4')
def _(f):
    # Worked example 1: multiply 3.0 ns, add 1.6 ns, tcq 0.2, tsu 0.1
    tm, ta, tcq, tsu = 3.0, 1.6, 0.2, 0.1
    T0 = tcq + tm + ta + tsu; T3 = tcq + max(tm / 2, ta) + tsu
    assert round(T0, 1) == 4.9 and round(T3, 1) == 1.9 and round(3 * T3, 1) == 5.7 and round(1e3 / T3, 1) == 526.3
    U = 110
    def bar(y, parts):
        x = 0
        for lab, w, k in parts:
            if k == 'R': f.cell(x, y, 26, 90, '', 't'); x += 26; continue
            f.cell(x, y + 5, w * U - 6, 80, lab, k, fs=22); x += w * U
        return x
    f.text(0, -30, 'no pipeline', 22, GR, 900)
    x = bar(0, [('', 0, 'R'), ('× 3.0', tm, 'p'), ('+ 1.6', ta, 'p'), ('', 0, 'R')])
    f.text(x + 18, 45, f'T = {T0:.1f} ns', 24, NV, 900)
    f.text(0, 170, 'three stages', 22, OR, 900)
    x = bar(200, [('', 0, 'R'), ('× 1.5', tm / 2, 'p'), ('', 0, 'R'), ('× 1.5', tm / 2, 'p'), ('', 0, 'R'), ('+ 1.6', ta, 'o'), ('', 0, 'R')])
    f.cell(40, 340, 640, 70, f'latency 3 × {T3:.1f} = {3 * T3:.1f} ns', 'o', fs=26)
    f.text(x + 18, 245, f'T = {T3:.1f} ns', 24, OR, 900)
    return 'Pipelining the multiply-add datapath', f'faster clock, yet latency <b>grows</b>: {T0:.1f} → {3 * T3:.1f} ns'
G['ec-vlsi-u4-L4'] = dict(rows=2, cols=6, flat='', raised={'0,1': '3.0', '0,2': '1.6', '1,1': '1.5', '1,3': '1.5', '1,5': '1.6'}, note='three stages: T = <b>1.9 ns</b>')

@sp('u4-L5')
def _(f):
    # Worked example 3: 1 Mbit SRAM, 64K words × 16 bits, square 1024 × 1024 array
    words, bits = 64 * 1024, 16
    side = math.isqrt(words * bits); wpr = side // bits
    rb, cb = int(math.log2(side)), int(math.log2(wpr))
    assert side == 1024 and (rb, cb) == (10, 6) and rb + cb == 16
    for r in range(6):
        for c in range(6):
            f.cell(140 + c * 70, r * 62, 60, 52, '', 'o' if r == 2 else 'g')
    f.cell(0, 0, 110, 6 * 62 - 10, '', 't'); f.text(55, 120, 'row', 24, '#1F2A45', 900, 'center'); f.text(55, 150, 'decoder', 22, '#1F2A45', 900, 'center')
    f.text(55, 210, f'{rb} bits', 26, '#E8590D', 900, 'center')
    f.text(140 + 3 * 70 - 5, -28, f'{side} × {side} cells', 24, GR, 900, 'center')
    f.text(140 + 6 * 70 + 44, 2 * 62 + 26, f'1 of {side} rows', 22, OR, 900)
    f.cell(140, 6 * 62 + 20, 410, 70, f'column mux: {cb} bits, {wpr} → 1', 'p', fs=24)
    return '64K × 16 SRAM folded into a square array', f'16 address bits = <b>{rb} row + {cb} column</b>'
G['ec-vlsi-u4-L5'] = dict(rows=2, cols=3, flat='', raised={'0,1': 'T', '1,1': 'C'}, note='the bitline moves just <b>±60 mV</b>')

# ------------------------------------------------------------------ Unit 5
@sp('u5-L1')
def _(f):
    # Worked example 2: FPGA ₹0 NRE, ₹1,800 a chip; gate array ₹40 lakh NRE, ₹500 a chip (costs in ₹ lakh)
    nre1, c1, nre2, c2 = 0, 1800, 40e5, 500
    N = (nre2 - nre1) / (c1 - c2); cost = (nre1 + c1 * N) / 1e5
    assert round(N) == 3077
    sx, sy, X0, Y0 = 0.095, 3.4, 60, 400
    P = lambda n, lakh: (X0 + n * sx, Y0 - lakh * sy)
    path(f, [P(0, 0), P(6000, 0)], False, 4); path(f, [P(0, 0), P(0, 115)], False, 4)
    path(f, [P(0, 0), P(6000, c1 * 6000 / 1e5)], False, 7); path(f, [P(0, nre2 / 1e5), P(6000, (nre2 + c2 * 6000) / 1e5)], True, 8)
    x, y = P(N, cost); f.cell(x - 22, y - 22, 44, 44, '', 'o', D=30)
    f.cell(x - 70, y + 50, 160, 60, f'{N:,.0f} chips', 'o', fs=24)
    f.text(P(6000, 108)[0] + 12, P(6000, 108)[1], 'FPGA', 24, GR, 900); f.text(P(6000, 70)[0] + 12, P(6000, 70)[1], 'gate array', 24, OR, 900)
    f.text(X0 - 12, P(0, 40)[1], '₹40 L', 20, GR, 900, 'right'); f.text(P(6000, 0)[0], Y0 + 32, 'chips', 22, GR, 900, 'right')
    return 'Cost against volume: FPGA and gate array', f'₹40 lakh ÷ (1,800 − 500) = <b>{N:,.0f}</b> chips'
G['ec-vlsi-u5-L1'] = dict(rows=4, cols=4, flat='', raised={'0,0': '9', '0,3': '9', '2,1': '2.9', '1,2': '3.3'}, note='the <b>gate array</b> wins at 50,000')

@sp('u5-L2')
def _(f):
    # The exam trap: x = 4'b0011; ~x is bitwise, !x is logical (one bit)
    x = 0b0011
    bit, lg = (~x) & 0xF, int(not x)
    assert bit == 12 and lg == 0
    f.cell(0, 0, 560, 64, "x = 4'b0011", 't', fs=26, color=NV)
    row(f, list(format(x, '04b')), 120, 110, 80, 70, 12); f.text(100, 145, 'x', 28, GR, 900, 'right')
    row(f, [('*1' if c == '1' else '0') for c in format(bit, '04b')], 120, 220, 80, 70, 12); f.text(100, 255, '~x', 28, OR, 900, 'right')
    f.cell(120, 330, 80, 70, '0', 'p', fs=30); f.text(100, 365, '!x', 28, OR, 900, 'right')
    f.text(500, 255, f'= {bit}, bitwise', 24, NV, 900); f.text(230, 365, 'one bit: nonzero is true', 24, GR, 900)
    return "Bitwise ~ against logical ! on 4'b0011", "~ flips each bit to 1100; ! gives one bit: <b>0</b>"
G['ec-vlsi-u5-L2'] = dict(rows=3, cols=4, flat='0', raised={'0,0': '1', '0,2': '1', '1,1': '1', '1,2': '1', '2,1': '1', '2,2': '1'}, note='sel = 1: Y = <b>0110</b>')

@sp('u5-L3')
def _(f):
    # Worked example: 4-input LUT for f = A·B + C·D, read at ABCD = 1101
    bit = lambda i: int(((i >> 3) & 1 and (i >> 2) & 1) or ((i >> 1) & 1 and i & 1))
    bits = [bit(i) for i in range(16)]
    hit = 0b1101; assert bits[hit] == 1 and sum(bits) == 7
    for r in range(2):
        cells = []
        for c in range(8):
            i = r * 8 + c
            cells.append(('*' if i == hit else '+' if bits[i] else '') + str(bits[i]))
        row(f, cells, 0, r * 120, 64, 60, 8, idx=[str(r * 8 + c) for c in range(8)], ifs=16)
    f.cell(150, 290, 260, 64, 'ABCD = 1101', 'o', fs=24)
    arrow(f, 280, 286, 5 * 72 + 32, 186, True)
    f.text(450, 322, 'f = 1', 28, OR, 900)
    return "The worked example's LUT, f = AB + CD", 'a 4-input LUT holds 2<sup>4</sup> = <b>16</b> bits'
G['ec-vlsi-u5-L3'] = dict(rows=2, cols=8, flat='0', raised={'0,3': '1', '0,7': '1', '1,3': '1', '1,4': '1', '1,5': '1', '1,6': '1', '1,7': '1'}, note='address 13 reads <b>1</b>')

@sp('u5-L4')
def _(f):
    # Worked example 1: core 3.0 × 3.0 mm, macros 2.0, 1.5, 1.0, 0.5 mm², cells 1.8 mm²
    mac, cells, core = [2.0, 1.5, 1.0, 0.5], 1.8, 3.0 * 3.0
    U = (sum(mac) + cells) / core
    assert round(U * 100, 1) == 75.6
    S = 120
    f.cell(0, 0, 3 * S, 3 * S, '', 't')
    pos = [(10, 10), (200, 10), (10, 200), (150, 200)]
    for (x, y), a in zip(pos, mac):
        s = math.sqrt(a) * S * .95; f.cell(x, y, s, s, f'{a:g} mm²', 'p', fs=20 if a > .6 else 16)
    f.cell(0, 3 * S + 30, 3 * S, 64, f'U = {U * 100:.1f} %', 't', fs=26, color=NV)
    f.text(560, -60, 'sign-off', 26, GR, 900, 'center')
    for i, (t, k) in enumerate([('DRC ✓', 'p'), ('LVS', 'o'), ('timing', 'o'), ('IR drop', 'o')]):
        f.cell(450, i * 100, 220, 76, t, k, fs=26)
    return 'Floorplan and sign-off checks', 'DRC is geometry only: <b>LVS, timing, IR</b> still due'
G['ec-vlsi-u5-L4'] = dict(rows=4, cols=5, flat='', raised={'3,0': 'B', '3,4': 'A', '0,0': 'C', '0,4': 'D'}, note='swap A and B: 21 → <b>13</b>')

# ------------------------------------------------------------------ Unit 6
@sp('u6-L1')
def _(f):
    # Worked example 1: yield Y = 0.90; defect level DL = 1 − Y^(1 − T), in parts per million
    Y = 0.90
    DL = lambda T: (1 - Y ** (1 - T)) * 1e6
    assert round(DL(0.95)) == 5254 and round(DL(0.99)) == 1053
    sx, sy, X0, Y0 = 5000, 0.032, 60, 400
    P = lambda T, d: (X0 + (T - 0.9) * sx, Y0 - d * sy)
    path(f, [P(0.9, 0), P(1.0, 0)], False, 4); path(f, [P(0.9, 0), P(0.9, 11500)], False, 4)
    path(f, [P(0.9 + i / 1000, DL(0.9 + i / 1000)) for i in range(101)], True, 8)
    for T, lab, k in [(0.95, f'{DL(0.95):.0f}', 'p'), (0.99, f'{DL(0.99):.0f}', 'o')]:
        x, y = P(T, DL(T)); f.cell(x - 16, y - 16, 32, 32, '', k, D=24); f.cell(x - 20, y - 86, 110, 52, lab, k, fs=24)
    f.text(P(0.95, 0)[0], Y0 + 32, '95 %', 22, GR, 900, 'center'); f.text(P(0.99, 0)[0], Y0 + 32, '99 %', 22, GR, 900, 'center')
    f.text(P(1.0, 0)[0] + 10, Y0 + 32, 'T', 24, GR, 900); f.text(X0 - 12, Y0 - 11500 * sy, 'DPM', 22, GR, 900, 'right')
    f.cell(X0 + 0.04 * sx, 470, 420, 66, '100 % of modelled faults only', 't', fs=22, color=NV)
    return 'Defect level against fault coverage, Y = 0.90', 'T counts <b>modelled</b> faults: real defects escape'
G['ec-vlsi-u6-L1'] = dict(rows=4, cols=6, flat='', raised={'1,1': '✓', '1,4': '✓', '2,3': '✓', '2,4': '✓', '3,0': '✓', '3,2': '✓', '3,5': '✓'}, note='<b>01, 10, 11</b> catch all six')

@sp('u6-L2')
def _(f):
    # The 4-bit LFSR of the lesson: seed 0001, shift left, new bit 0 = bit 3 XOR bit 0
    s, seen = 0b0001, []
    while s not in seen:
        seen.append(s); s = ((s << 1) & 0b1110) | (((s >> 3) & 1) ^ (s & 1))
    assert len(seen) == 15 and 0 not in seen
    R, cx, cy = 250, 300, 280
    for i, v in enumerate(seen):
        a = 2 * math.pi * i / 15
        x, y = cx + R * math.sin(a) - 46, cy - R * math.cos(a) - 28
        f.cell(x, y, 92, 56, format(v, '04b'), 'o' if i == 0 else 'p', fs=22)
    f.cell(cx - 70, cy - 60, 140, 60, '0000', 'g', fs=26)
    f.text(cx, cy + 30, 'never: locks up', 22, GR, 900, 'center')
    return 'The 4-bit LFSR and its states', f'a ring of <b>{len(seen)}</b> states, not 16: 0000 never appears'
G['ec-vlsi-u6-L2'] = dict(rows=4, cols=4, flat='', raised={f'{r},{c}': 'FF' for r in range(4) for c in range(2)}, note='four chains: <b>0.511 ms</b>')

@sp('u6-L3')
def _(f):
    # Worked example 1: March C− on 1024 addresses, 5 ns per access; GALPAT ≈ 4n²
    els = [('⇕', ['w0']), ('⇑', ['r0', 'w1']), ('⇑', ['r1', 'w0']), ('⇓', ['r0', 'w1']), ('⇓', ['r1', 'w0']), ('⇕', ['r0'])]
    ops = sum(len(o) for _, o in els); n, ta = 1024, 5e-9
    tm = ops * n * ta * 1e6; tg = 4 * n * n * ta * 1e3
    assert ops == 10 and round(tm, 1) == 51.2 and round(tg) == 21
    for i, (d, o) in enumerate(els):
        x = i * 112
        f.text(x + 48, -30, d, 34, OR, 900, 'center')
        for j, op in enumerate(o): f.cell(x, j * 74, 96, 62, op, 'o' if op[0] == 'r' else 'p', fs=24)
    f.cell(0, 200, 660, 70, f'{ops} × 1024 × 5 ns = {tm:.1f} µs', 'o', fs=26)
    f.cell(0, 300, 660, 64, f'GALPAT ≈ 4n² → about {tg:.0f} ms', 't', fs=22, color=NV)
    return 'March C− on a 1024-address SRAM', f'March C− is <b>10n</b> = 10,240 accesses, not 10n²'
G['ec-vlsi-u6-L3'] = dict(rows=2, cols=6, flat='', raised={'0,0': 'w0', '0,1': 'r0', '0,2': 'r1', '0,3': 'r0', '0,4': 'r1', '0,5': 'r0'}, note='March C−: <b>10n</b> accesses')

specs = S
