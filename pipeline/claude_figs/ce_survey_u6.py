"""Hand-drawn figures for ce-survey-u6 (Remote Sensing and Image Interpretation), drawn from each chapter's worked example."""
import math, os, sys; sys.path.insert(0, os.path.dirname(__file__)); from kit import *

FIG = {}
spec = make_spec(FIG)


def SUB(t):
    return f'<tspan dy="4" font-size="12">{t}</tspan><tspan dy="-4"> </tspan>'


# ---- 6.1 the spectrum, with the optical part opened up ----
def f1():
    o = []
    # top strip: whole spectrum, log scale 1e-6 µm .. 1e7 µm
    X0, X1 = 40, 680
    fx = lambda um: X0 + (math.log10(um) + 6) / 13 * (X1 - X0)
    segs = [(1e-6, 1e-5, 'gamma', NXS), (1e-5, 1e-2, 'X-ray', PANEL), (1e-2, 0.4, 'UV', ACS),
            (0.4, 1e3, 'visible + infrared', LVS), (1e3, 1e6, 'microwave', ACS), (1e6, 1e7, 'radio', PANEL)]
    y0, h = 34, 34
    for a, b, lab, fill in segs:
        o.append(R(fx(a), y0, fx(b) - fx(a), h, fill, INK, 0, 1.5))
        o.append(T((fx(a) + fx(b)) / 2, y0 + 22, lab, 13))
    for v, lab in ((1e-3, '1 nm'), (1, '1 µm'), (1e3, '1 mm'), (1e6, '1 m')):
        o.append(L(fx(v), y0 + h, fx(v), y0 + h + 6, INK, 1.5))
        o.append(T(fx(v), y0 + h + 22, lab, 13, fill=MUT))
    # zoom: 0.3 .. 15 µm
    Z0, Z1 = 50, 670
    fz = lambda um: Z0 + (math.log10(um) - math.log10(0.3)) / (math.log10(15) - math.log10(0.3)) * (Z1 - Z0)
    yz, hz = 168, 44
    o.append(L(fx(0.3), y0 + h, Z0, yz, L2, 1.2, '4 4'))
    o.append(L(fx(15), y0 + h, Z1, yz, L2, 1.2, '4 4'))
    bands = [(0.3, 0.4, 'UV', PANEL), (0.4, 0.7, 'visible', LVS), (0.7, 1.3, 'near IR', ACS), (1.3, 3, 'short-wave IR', NXS),
             (3, 8, 'mid IR', ACS), (8, 15, 'thermal IR', NXS)]
    for a, b, lab, fill in bands:
        o.append(R(fz(a), yz, fz(b) - fz(a), hz, fill, INK, 0, 1.5))
        o.append(T((fz(a) + fz(b)) / 2, yz + 27, lab, 13, bold=lab in ('visible', 'thermal IR')))
    for v in (0.4, 0.7, 1.3, 3, 8):
        o.append(L(fz(v), yz + hz, fz(v), yz + hz + 6, INK, 1.5))
        o.append(T(fz(v), yz + hz + 21, f'{v:g}', 13, fill=MUT))
    o.append(T(Z1, yz + hz + 21, '15 µm', 13, 'end', MUT))
    # peaks above the zoom strip
    for um, lab in ((0.50, 'sun peak 0.50 µm (5800 K)'), (9.66, 'earth peak 9.7 µm (300 K)')):
        X = fz(um)
        o.append(L(X, 120, X, yz - 4, AC, 2, arrow='n'))
        o.append(T(X, 112, lab, 13, 'start' if um < 1 else 'end', AC, True))
    # photon energies of the worked example below
    yb = yz + hz + 60
    for um, lab in ((0.55, 'λ = 0.55 µm: photon 2.25 eV'), (10, 'λ = 10 µm: photon 0.124 eV')):
        X = fz(um)
        o.append(L(X, yb - 14, X, yz + hz + 28, LV, 2, arrow='l'))
        o.append(T(X, yb, lab, 13, 'start' if um < 1 else 'end', LV, True))
    o.append(T(360, yb + 30, 'E = 1.24 ÷ λ: ten times the wavelength, one tenth the photon energy', 13, fill=MUT))
    return yb + 46, ''.join(o)


FIG[1] = (f1, 'The electromagnetic spectrum on a log scale, with the part used for optical and thermal remote sensing opened up below. '
              'The sun peaks at 0.50 µm and the earth at 9.7 µm (Wien\'s law in the second worked example); a green photon carries 2.25 eV and a 10 µm photon only 0.124 eV.',
          'A long strip from gamma rays through X-rays, ultraviolet, visible and infrared, microwave to radio, with ticks at 1 nanometre, 1 micrometre, 1 millimetre and 1 metre. Below it, the range 0.3 to 15 micrometres is enlarged into ultraviolet, visible, near, short-wave, mid and thermal infrared, with arrows for the sun peak at 0.50 and the earth peak at 9.7 micrometres and photon energies 2.25 and 0.124 electron volts.')


# ---- 6.2 the hazy-day beam of the worked example ----
def f2():
    o = []
    # atmosphere band and ground
    o.append(R(20, 120, 680, 90, ACS, AC, 0, 0))
    o.append(T(690, 140, 'atmosphere', 13, 'end', AC, True))
    o.append(R(20, 290, 680, 14, PANEL, INK, 0, 1.5))
    o.append(T(30, 322, 'ground: field with ρ = 0.157', 13, 'start', INK, True))
    # sun
    o.append(f'<circle cx="70" cy="58" r="24" style="fill:var(--next-soft);stroke:var(--next);stroke-width:2"/>')
    o.append(T(70, 63, 'sun', 13, bold=True))
    # downward beam
    o.append(L(92, 76, 250, 286, NX, 3, arrow='x'))
    o.append(Tb(205, 252, 'E = 400 W/m²', 13, 'end', NX, True))
    o.append(T(196, 270, 'at the ground', 13, 'end', MUT))
    # haze particles
    for x, y in ((420, 150), (450, 178), (488, 146), (520, 172), (470, 196), (395, 182)):
        o.append(C(x, y, 4, MUT))
    # upward beam to sensor
    o.append(L(262, 286, 560, 76, LV, 3, arrow='l'))
    o.append(Tb(330, 258, 'leaves ground: ρE/π = 20.0', 13, 'start', LV, True))
    o.append(Tb(418, 112, 'after the climb: × T 0.9 = 18.0', 13, 'end', LV, True))
    # path radiance from the haze
    o.append(L(470, 160, 560, 86, AC, 2.5, '6 4', arrow='n'))
    o.append(Tb(540, 192, 'haze adds L' + SUB('p') + ' = 4.0', 13, 'start', AC, True))
    # sensor
    o.append(R(560, 40, 120, 40, PANEL, INK, 6))
    o.append(T(620, 65, 'sensor', 13, bold=True))
    o.append(T(620, 30, 'reads L = 22.0', 13, fill=INK, bold=True))
    # result box
    o.append(R(20, 340, 680, 62, PANEL, L2, 8, 1.5))
    o.append(T(360, 364, 'no correction: π × 22.0 ÷ 400 = 0.173 (too high)', 13))
    o.append(T(360, 388, 'corrected: π × (22.0 − 4.0) ÷ (0.9 × 400) = 0.157', 13, bold=True, fill=AC))
    o.append(T(360, 428, 'radiances in W m⁻² sr⁻¹', 13, fill=MUT))
    return 440, ''.join(o)


FIG[2] = (f2, 'The hazy-day beam of the worked example. The field sends 20.0 W m⁻² sr⁻¹ upwards, the climb keeps 90 percent of it and the haze adds 4.0, so the sensor reads 22.0; only removing both effects gives back the true reflectance 0.157.',
          'Sunlight of 400 watts per square metre reaches a field through a shaded atmosphere band. An upward beam leaves the field at 20.0 and arrives at 18.0; a dashed arrow from haze particles adds 4.0, so the sensor reads 22.0. A box below compares the uncorrected reflectance 0.173 with the corrected 0.157.')


# ---- 6.3 spectral signatures with the two NDVI bands ----
VEG = [(0.40, 4), (0.45, 5), (0.55, 12), (0.62, 6), (0.66, 5), (0.69, 8), (0.72, 28), (0.75, 45), (0.83, 50), (1.1, 47), (1.3, 42),
       (1.45, 22), (1.6, 30), (1.8, 26), (1.95, 10), (2.2, 18), (2.4, 12), (2.5, 10)]
SOIL = [(0.40, 8), (0.45, 10), (0.55, 14), (0.66, 18), (0.83, 22), (1.1, 26), (1.3, 28), (1.4, 27), (1.6, 31), (1.9, 28), (2.2, 33), (2.5, 30)]
WATER = [(0.40, 9), (0.45, 8), (0.55, 6), (0.66, 4), (0.75, 2.5), (0.83, 2), (1.1, 1), (1.6, 0.5), (2.5, 0.5)]


def f3():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 300
    fx = lambda v: x0 + (v - 0.4) / 2.1 * (x1 - x0)
    fy = lambda v: y1 - v / 60 * (y1 - y0)
    for a, b, lab in ((0.63, 0.69, 'red'), (0.76, 0.90, 'NIR')):
        o.append(R(fx(a), y0, fx(b) - fx(a), y1 - y0, NXS, NXS, 0, 0))
        o.append(T((fx(a) + fx(b)) / 2 + (0 if lab == 'NIR' else -2), y0 + 16, lab, 13, fill=NX, bold=True))
    o.append(axes(x0, x1, y0, y1, [0.5, 1.0, 1.5, 2.0, 2.5], [0, 20, 40, 60], fx, fy, 'wavelength (µm)', 'reflectance (%)',
                  xfmt=lambda v: f'{v:g}'))
    for pts, c in ((VEG, AC), (SOIL, NX), (WATER, LV)):
        o.append(P([(fx(a), fy(b)) for a, b in pts], c, 2.5))
    o.append(T(fx(1.15), fy(50) - 8, 'vegetation', 14, 'start', AC, True))
    o.append(T(fx(2.05), fy(36) - 4, 'dry soil', 14, 'start', NX, True))
    o.append(T(fx(1.2), fy(1) - 8, 'clear water', 14, 'start', LV, True))
    o.append(T(fx(1.45), fy(22) + 18, 'leaf water', 13, 'middle', MUT))
    o.append(T(fx(1.95), fy(10) + 18, 'leaf water', 13, 'middle', MUT))
    o.append(T(fx(0.72) - 6, fy(28), 'red edge', 13, 'end', AC))
    for v, r_, n_, c in ((0, 5, 50, AC), (0, 18, 22, NX), (0, 4, 2, LV)):
        o.append(C(fx(0.66), fy(r_), 5, c)); o.append(C(fx(0.83), fy(n_), 5, c))
    return 350, ''.join(o)


FIG[3] = (f3, 'Spectral signatures of healthy vegetation, dry soil and clear water, with the red (0.63–0.69 µm) and near-infrared (0.76–0.90 µm) bands shaded. '
              'The dots are the band values used in the worked example: vegetation 5 and 50 percent, soil 18 and 22, water 4 and 2.',
          'Reflectance in percent against wavelength from 0.4 to 2.5 micrometres. Vegetation is low in blue and red with a small green peak, rises steeply at the red edge to about 50 percent, then falls with dips near 1.45 and 1.95 micrometres. Dry soil rises smoothly from 8 to about 33 percent. Clear water falls from 9 percent in blue to almost zero beyond 0.8 micrometre. Two shaded vertical strips mark the red and near-infrared bands, with dots where each curve crosses them.')


# ---- 6.4 whiskbroom and pushbroom, with the pushbroom numbers of the worked example ----
def f4():
    o = []
    yg = 250
    # whiskbroom (left)
    cx = 180
    o.append(T(cx, 26, 'Whiskbroom', 15, bold=True))
    o.append(R(cx - 30, 44, 60, 30, PANEL, INK, 5))
    o.append(T(cx, 64, 'mirror', 13))
    o.append(L(cx, 74, cx - 30, yg - 4, AC, 2))
    o.append(L(cx, 74, cx - 18, yg - 4, AC, 2))
    o.append(f'<ellipse cx="{cx - 24}" cy="{yg}" rx="9" ry="5" style="fill:var(--accent);stroke:none"/>')
    o.append(arc(cx - 110, yg - 22, cx + 110, yg - 22, -0.12, NX, 2.5, 'x'))
    o.append(arc(cx + 110, yg - 22, cx - 110, yg - 22, -0.12, NX, 2.5, 'x'))
    o.append(L(40, yg, 320, yg, INK, 2))
    o.append(T(cx, yg + 22, 'one spot sweeps across the track', 13, fill=MUT))
    # top view of the strip being built
    for i in range(4):
        y = yg + 44 + i * 16
        o.append(R(70, y, 220, 12, PANEL, L2, 2, 1))
    o.append(L(76, yg + 50, 282, yg + 50, NX, 2, arrow='x'))
    o.append(T(cx, yg + 126, 'line by line, pixel by pixel', 13, fill=MUT))
    # pushbroom (right)
    px = 530
    o.append(T(px, 26, 'Pushbroom', 15, bold=True))
    o.append(R(px - 50, 44, 100, 30, PANEL, INK, 5))
    o.append(T(px, 64, '6000 detectors', 13))
    gx0, gx1 = 400, 660
    for i in range(9):
        X = gx0 + i * (gx1 - gx0) / 8
        o.append(L(px - 40 + i * 10, 74, X, yg - 2, AC, 1.4))
    o.append(L(380, yg, 690, yg, INK, 2))
    o.append(L(gx0, yg + 14, gx1, yg + 14, INK, 1.5))
    o.append(L(gx0, yg + 8, gx0, yg + 20, INK, 1.5)); o.append(L(gx1, yg + 8, gx1, yg + 20, INK, 1.5))
    o.append(Tb(px, yg + 19, 'swath S = 60 km', 13, 'middle', INK, True))
    o.append(L(700, 74, 700, yg, L2, 1.5, '4 4'))
    o.append(T(694, 150, 'H = 600 km', 13, 'end', INK, True))
    for i in range(4):
        y = yg + 44 + i * 16
        o.append(R(gx0, y, gx1 - gx0, 12, ACS if i == 0 else PANEL, AC if i == 0 else L2, 2, 1))
    o.append(T(px, yg + 126, 'a whole row at once: p = 60 000 ÷ 6000 = 10 m', 13, fill=INK, bold=True))
    o.append(T(px, yg + 146, 'one detector sees θ = 10 ÷ 600 000 = 16.7 µrad', 13, fill=MUT))
    o.append(L(360, yg + 140, 360, yg + 44, L2, 2, arrow='m'))
    o.append(T(360, yg + 160, 'flight', 13, fill=MUT))
    return yg + 172, ''.join(o)


FIG[4] = (f4, 'Cross-track scanning seen from behind the satellite. A whiskbroom mirror sweeps one spot from side to side; a pushbroom array of 6000 detectors sees the whole 60 km swath at once, so at 600 km each detector covers a 10 m pixel, an angle of 16.7 µrad.',
          'Left: a mirror sends a single narrow beam to the ground and double arrows show it sweeping across; below, image rows are filled one pixel after another. Right: nine fan lines from a 6000-detector array to a 60 kilometre swath at 600 kilometres height; below, a whole row is filled at once, with the pixel size of 10 metres and the angle of 16.7 microradians written out.')


# ---- 6.5 nine 10 m pixels into one 30 m pixel ----
def f5():
    o = []
    dn = [10, 10, 10, 10, 70, 70, 10, 70, 70]
    s, x0, y0 = 66, 70, 50
    for i, v in enumerate(dn):
        r, c = divmod(i, 3)
        bright = v == 70
        o.append(R(x0 + c * s, y0 + r * s, s, s, ACS if bright else PANEL, AC if bright else L2, 0, 1.5))
        o.append(T(x0 + c * s + s / 2, y0 + r * s + s / 2 + 6, str(v), 17, bold=bright))
    o.append(T(x0 + 1.5 * s, y0 - 14, 'nine 10 m pixels', 14, bold=True))
    o.append(T(x0 + 1.5 * s, y0 + 3 * s + 24, 'bright cover (DN 70) in 4 of 9', 13, fill=AC, bold=True))
    o.append(T(x0 + 1.5 * s, y0 + 3 * s + 44, 'each pixel 10 m × 10 m = 100 m²', 13, fill=MUT))
    o.append(L(300, y0 + 1.5 * s, 420, y0 + 1.5 * s, INK, 2.5, arrow='m'))
    o.append(T(360, y0 + 1.5 * s - 12, 'same 30 m block', 13, fill=MUT))
    o.append(R(450, y0, 3 * s, 3 * s, LVS, LV, 0, 2))
    o.append(T(450 + 1.5 * s, y0 + 1.5 * s + 10, '37', 30, bold=True))
    o.append(T(450 + 1.5 * s, y0 - 14, 'one 30 m pixel', 14, bold=True))
    o.append(T(450 + 1.5 * s, y0 + 3 * s + 24, '330 ÷ 9 = 36.7 → DN 37', 13, fill=LV, bold=True))
    o.append(T(450 + 1.5 * s, y0 + 3 * s + 44, 'mixed: neither 10 nor 70', 13, fill=MUT))
    return y0 + 3 * s + 60, ''.join(o)


FIG[5] = (f5, 'The block of the first worked example seen at two spatial resolutions. The 10 m sensor separates four bright pixels from five dark ones; the 30 m sensor stores one mixed value, 37, which matches neither cover.',
          'Left: a three by three grid of 10 metre pixels with digital numbers 10 and 70, the four 70s shaded. An arrow leads to a single large 30 metre pixel holding 37, the rounded mean 330 divided by 9.')


# ---- 6.6 the interpretation elements on one photo, with the shadow height ----
def f6():
    o = []
    x0, y0, w, h = 150, 30, 420, 300
    o.append(R(x0, y0, w, h, PANEL, INK, 4, 1.5))
    # river: winding dark band
    o.append(f'<path d="M{x0},{y0 + 230} C{x0 + 80},{y0 + 180} {x0 + 140},{y0 + 290} {x0 + 230},{y0 + 250} S{x0 + 360},{y0 + 190} {x0 + w},{y0 + 220}" style="fill:none;stroke:var(--live);stroke-width:12;stroke-linecap:round"/>')
    # orchard grid
    for i in range(5):
        for j in range(4):
            o.append(C(x0 + 30 + i * 18, y0 + 30 + j * 18, 4, AC))
    # forest texture
    for i, (dx, dy) in enumerate([(0, 0), (14, 6), (28, -4), (6, 18), (22, 20), (38, 12), (12, 34), (30, 34), (46, 26)]):
        o.append(f'<circle cx="{x0 + 250 + dx}" cy="{y0 + 40 + dy}" r="9" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:1.2"/>')
    # tank
    o.append(f'<ellipse cx="{x0 + 110}" cy="{y0 + 150}" rx="34" ry="18" style="fill:var(--live);stroke:var(--live);stroke-width:2"/>')
    # stadium with car park
    o.append(f'<ellipse cx="{x0 + 340}" cy="{y0 + 130}" rx="34" ry="22" style="fill:var(--fig);stroke:var(--ink);stroke-width:2"/>')
    for i in range(3):
        o.append(R(x0 + 386, y0 + 112 + i * 14, 22, 9, PANEL, INK, 1, 1.2))
    # tower and shadow (sun from the right, shadow to the left)
    tx, ty = x0 + 210, y0 + 150
    o.append(R(tx - 3, ty - 4, 6, 8, 'var(--ink)', INK, 0, 1))
    o.append(f'<polygon points="{tx - 3},{ty - 2} {tx - 60},{ty + 2} {tx - 60},{ty + 6} {tx - 3},{ty + 4}" style="fill:var(--muted);stroke:none"/>')
    # labels with leaders
    labs = [((x0 + 66, y0 + 40), (x0 - 10, y0 + 40), 'pattern: orchard grid', 'end'),
            ((x0 + 110, y0 + 150), (x0 - 10, y0 + 150), 'tone: dark smooth tank', 'end'),
            ((x0 + 60, y0 + 214), (x0 - 10, y0 + 240), 'shape: winding river', 'end'),
            ((x0 + 290, y0 + 52), (x0 + w + 10, y0 + 40), 'texture: rough canopy', 'start'),
            ((x0 + 397, y0 + 130), (x0 + w + 10, y0 + 130), 'association: car park', 'start'),
            ((tx - 40, ty + 6), (x0 + w + 10, y0 + 250), 'shadow: tower', 'start')]
    for (ax, ay), (bx, by), t, anc in labs:
        o.append(L(ax, ay, bx + (4 if anc == 'end' else -4), by, L2, 1.4))
        o.append(T(bx, by + 5, t, 13, anc, INK, True))
    o.append(T(360, y0 + h + 26, 'photo scale 1:20 000: shadow 1.5 mm → 30 m on the ground', 13, fill=MUT))
    o.append(T(360, y0 + h + 46, 'sun 40° above the horizon → tower height = 30 × tan 40° = 25.2 m', 13, fill=AC, bold=True))
    return y0 + h + 60, ''.join(o)


FIG[6] = (f6, 'A sketched photo patch at 1:20 000 with one example of each element: the orchard grid is pattern, the canopy is texture, the river is shape, the tank is tone, the car park beside the stadium is association. '
              'The tower\'s 1.5 mm shadow gives its height, 25.2 m, as in the second worked example.',
          'A rectangle standing for an aerial photo. Inside: a grid of dots for an orchard, a cluster of round crowns for forest, a dark winding river, a dark oval tank, an oval stadium with small rectangles beside it, and a tower with a long thin shadow. Leader lines name pattern, tone, shape, texture, association and shadow. Below: the shadow 1.5 millimetres at 1 to 20 000 is 30 metres, and with the sun 40 degrees up the tower is 25.2 metres high.')


# ---- 6.7 the linear stretch of the worked example ----
def f7():
    o = []
    x0, x1, y0, y1 = 90, 660, 40, 320
    fx = lambda v: x0 + v / 120 * (x1 - x0)
    fy = lambda v: y1 - v / 255 * (y1 - y0)
    # histogram of the input band (narrow) under the axis region
    o.append(R(fx(40), y0, fx(90) - fx(40), y1 - y0, ACS, ACS, 0, 0))
    o.append(T((fx(40) + fx(90)) / 2 - 40, y0 + 18, 'raw band uses DN 40–90 only', 13, fill=AC, bold=True))
    o.append(axes(x0, x1, y0, y1, [0, 20, 40, 60, 80, 100, 120], [0, 64, 128, 192, 255], fx, fy, 'input DN', 'output DN'))
    o.append(P([(fx(0), fy(0)), (fx(40), fy(0)), (fx(90), fy(255)), (fx(120), fy(255))], LV, 3))
    o.append(L(fx(30), fy(0), fx(40), fy(0), NX, 3))
    pts = [(40, 0, '40 → 0', 'start', 30, -8), (65, 127.5, '65 → 127.5, stored 128', 'start', 14, 4), (90, 255, '90 → 255', 'start', 12, 20)]
    for a, b, lab, anc, dx, dy in pts:
        o.append(C(fx(a), fy(b), 6, LV))
        o.append(Tb(fx(a) + dx, fy(b) + dy, lab, 13, anc, INK, True))
    o.append(C(fx(30), fy(0), 6, NX))
    o.append(Tb(fx(30), fy(0) - 42, '30 → −51, clipped to 0', 13, 'middle', NX, True))
    o.append(L(fx(30), fy(0) - 36, fx(30), fy(0) - 8, NX, 1.5))
    o.append(T(fx(98), fy(150), 'slope 255 ÷ 50 = 5.1', 13, 'start', MUT))
    return 380, ''.join(o)


FIG[7] = (f7, 'The linear stretch of the first worked example. Input DNs 40 to 90 are spread over the whole 0 to 255 display with slope 5.1; values below 40 are clipped to 0 and values above 90 to 255.',
          'A graph of output DN against input DN. The line is flat at 0 up to 40, rises straight to 255 at 90, then stays flat. Dots mark 40 to 0, 65 to 127.5, 90 to 255, and 30 clipped to 0. A shaded band between input 40 and 90 shows the range the raw image used.')
