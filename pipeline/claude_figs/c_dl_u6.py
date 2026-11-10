"""Claude's hand-drawn figures for c-dl-u6 (Deep Learning, unit 6: autoencoders and generative models), one per chapter,
from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def poly(pts, fill, stroke, w=2):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{w};stroke-linejoin:round"/>'


# ---- 6.1 the bottleneck and its parameter count ----
def f1():
    o = []
    yc = 150
    def layer(x, h, name, sub, c, fill):
        o.append(R(x - 22, yc - h / 2, 44, h, fill, c, 6, 2))
        o.append(T(x, yc + h / 2 + 22, name, 14, fill=c, bold=True))
        o.append(T(x, yc + h / 2 + 40, sub, 13, fill=MUT))
    layer(60, 200, 'input x', '1,000 pixels', AC, ACS)
    layer(360, 40, 'code z', '32 units', LV, LVS)
    layer(660, 200, 'output x̂', '1,000 pixels', NX, NXS)
    o.append(poly([(86, yc - 100), (334, yc - 22), (334, yc + 22), (86, yc + 100)], PANEL, AC))
    o.append(poly([(386, yc - 22), (634, yc - 100), (634, yc + 100), (386, yc + 22)], PANEL, NX))
    o.append(T(210, yc - 6, 'encoder', 14, fill=AC, bold=True))
    o.append(T(210, yc + 14, 'W 1,000 × 32 = 32,000', 13, fill=INK))
    o.append(T(210, yc + 32, '+ 32 biases', 13, fill=INK))
    o.append(T(510, yc - 6, 'decoder', 14, fill=NX, bold=True))
    o.append(T(510, yc + 14, 'W 32 × 1,000 = 32,000', 13, fill=INK))
    o.append(T(510, yc + 32, '+ 1,000 biases', 13, fill=INK))
    o.append(T(360, 26, 'loss ‖x − x̂‖² compares output with input', 13, fill=LV, bold=True))
    o.append(P([(660, yc - 104), (660, 38), (530, 38)], LV, 1.8, '6 4'))
    o.append(P([(190, 38), (60, 38), (60, yc - 104)], LV, 1.8, '6 4'))
    o.append(boxt(60, 330, 600, 52, ['parameters 32,000 + 32 + 32,000 + 1,000 = 65,032',
                                      'compression 1,000 ÷ 32 = 31.25 : 1'], PANEL, INK, 14, bold_first=True))
    return 396, ''.join(o)
FIG[1] = (f1, 'A 1,000-pixel input is squeezed to a 32-unit code and rebuilt. The two weight matrices hold 32,000 values each, so with the biases the model has 65,032 parameters and compresses 31.25 to 1.',
          'An autoencoder drawn as a tall input bar of 1,000 pixels narrowing through the encoder to a 32-unit code and widening through the decoder to a 1,000-pixel output, with the parameter count 65,032 and ratio 31.25 : 1 below.')


# ---- 6.2 a hidden cause and the marginal likelihood ----
def f2():
    o = []
    z1, z2 = (90, 90), (90, 250)
    x1, x0 = (360, 90), (360, 250)
    def nd(p, s, sub, c, fill):
        o.append(f'<circle cx="{p[0]}" cy="{p[1]}" r="38" style="fill:{fill};stroke:{c};stroke-width:2.2"/>')
        o.append(T(p[0], p[1] + 1, s, 15, fill=c, bold=True)); o.append(T(p[0], p[1] + 19, sub, 13, fill=c))
    nd(z1, 'z = 1', 'p 0.6', AC, ACS); nd(z2, 'z = 2', 'p 0.4', AC, ACS)
    nd(x1, 'x = 1', '0.62', NX, NXS); nd(x0, 'x = 0', '0.38', LV, LVS)
    edges = [(z1, x1, '0.6 × 0.9 = 0.54', NX, 'x', (225, 80)), (z2, x1, '0.4 × 0.2 = 0.08', NX, 'x', (273, 141)),
             (z1, x0, '0.6 × 0.1 = 0.06', LV, 'l', (273, 198)), (z2, x0, '0.4 × 0.8 = 0.32', LV, 'l', (225, 270))]
    for (a, b, lab, c, ar, (tx, ty)) in edges:
        dx, dy = b[0] - a[0], b[1] - a[1]; d = math.hypot(dx, dy)
        o.append(L(a[0] + dx / d * 40, a[1] + dy / d * 40, b[0] - dx / d * 44, b[1] - dy / d * 44, c, 2.2, arrow=ar))
        o.append(Tb(tx, ty, lab, 13, fill=c, bold=True))
    o.append(T(90, 32, 'hidden cause', 13, fill=MUT, bold=True)); o.append(T(360, 32, 'what we see', 13, fill=MUT, bold=True))
    xr = 440
    o.append(T(xr, 70, 'p(x = 1) = 0.54 + 0.08 = 0.62', 14, 'start', NX, True))
    o.append(T(xr, 96, 'p(x = 0) = 0.06 + 0.32 = 0.38', 14, 'start', LV, True))
    o.append(T(xr, 150, 'data [1, 1, 0]:', 14, 'start', bold=True))
    o.append(T(xr, 176, 'L = 0.62 × 0.62 × 0.38', 14, 'start'))
    o.append(T(xr, 200, '  = 0.146', 14, 'start', bold=True))
    o.append(T(xr, 236, 'ln L = ln 0.146 = −1.924', 14, 'start', AC, True))
    return 304, ''.join(o)
FIG[2] = (f2, 'Each edge carries a joint term p(z) p(x | z); the two edges into x = 1 add to 0.62 and the two into x = 0 to 0.38. The data [1, 1, 0] then has likelihood 0.62 × 0.62 × 0.38 = 0.146, ln L = −1.924.',
          'Two hidden states z = 1 and z = 2 with priors 0.6 and 0.4, arrows to the outcomes x = 1 and x = 0 labelled 0.54, 0.08, 0.06 and 0.32, and the marginals 0.62 and 0.38 with the likelihood 0.146.')


# ---- 6.3 the code distribution against the prior, and its KL ----
def f3():
    x0, x1, y0, y1 = 60, 440, 50, 290
    fx = lambda z: x0 + (z + 5) / 12 * (x1 - x0)
    fy = lambda p: y1 - p / 0.45 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [-4, -2, 0, 1, 2, 4, 6], [0, 0.2, 0.4], fx, fy, 'code value z', 'density',
              xfmt=neg, yfmt=lambda v: f'{v:.1f}')]
    g = lambda z, m, s: math.exp(-(z - m) ** 2 / (2 * s * s)) / (s * math.sqrt(2 * math.pi))
    zs = [-5 + i * 0.1 for i in range(121)]
    o.append(P([(fx(z), fy(g(z, 1, 2))) for z in zs], LV, 3))
    o.append(P([(fx(z), fy(g(z, 0, 1))) for z in zs], AC, 3, '7 4'))
    o.append(T(fx(0) - 14, fy(0.399) - 8, 'prior N(0, 1)', 13, 'end', AC, True))
    o.append(T(fx(3.4), fy(0.16), 'q(z | x) = N(1, 4)', 13, 'start', LV, True))
    o.append(T(fx(3.4), fy(0.16) + 18, 'shifted and too wide', 13, 'start', LV))
    xr = 470
    o.append(T(xr, 70, 'encoder output: μ = 1, σ² = 4', 14, 'start', bold=True))
    o.append(T(xr, 104, 'KL = ½(σ² + μ² − 1 − ln σ²)', 14, 'start', AC))
    o.append(T(xr, 130, '   = ½(4 + 1 − 1 − 1.3863)', 14, 'start'))
    o.append(T(xr, 156, '   = ½ × 2.6137', 14, 'start'))
    o.append(boxt(xr, 172, 230, 40, ['KL = 1.307 nats'], LVS, LV, 15, bold_first=True))
    o.append(T(xr, 240, 'Training pulls μ toward 0', 13, 'start', MUT, True))
    o.append(T(xr, 258, 'and σ² toward 1, which', 13, 'start', MUT, True))
    o.append(T(xr, 276, 'shrinks the KL toward 0.', 13, 'start', MUT, True))
    return 350, ''.join(o)
FIG[3] = (f3, 'The encoder’s code q(z | x) = N(1, 4) sits to the right of the prior N(0, 1) and is twice as wide. The closed-form KL, ½(4 + 1 − 1 − ln 4) = 1.307 nats, measures that gap.',
          'Two bell curves: the dashed prior N(0, 1) centred on 0 and the wider, lower code distribution N(1, 4) centred on 1, beside the KL calculation giving 1.307 nats.')


# ---- 6.4 one real and one fake sample through the discriminator ----
def f4():
    o = []
    o.append(boxt(20, 40, 90, 44, ['noise z'], PANEL, L2, 14, bold_first=True))
    o.append(boxt(150, 40, 110, 44, ['generator G'], LVS, LV, 14, bold_first=True))
    o.append(boxt(300, 40, 110, 44, ['fake G(z)'], PANEL, LV, 14, bold_first=True))
    o.append(boxt(300, 130, 110, 44, ['real x'], PANEL, NX, 14, bold_first=True))
    o.append(boxt(460, 74, 120, 66, ['discriminator', 'D'], ACS, AC, 14, bold_first=True))
    o.append(L(112, 62, 146, 62, LV, 2.2, arrow='l')); o.append(L(262, 62, 296, 62, LV, 2.2, arrow='l'))
    o.append(L(412, 62, 456, 92, LV, 2.2, arrow='l')); o.append(L(412, 152, 456, 124, NX, 2.2, arrow='x'))
    o.append(T(600, 88, 'D(G(z)) = 0.3', 14, 'start', LV, True))
    o.append(T(600, 132, 'D(x) = 0.8', 14, 'start', NX, True))
    o.append(L(582, 96, 596, 84, LV, 1.6)); o.append(L(582, 118, 596, 128, NX, 1.6))
    # the 0 to 1 scale
    ys, sx0, sx1 = 226, 60, 660
    fx = lambda v: sx0 + v * (sx1 - sx0)
    o.append(T(20, ys - 44, 'D’s score: 0 means “fake”, 1 means “real”', 13, 'start', MUT, True))
    o.append(xaxis(sx0, sx1, ys, [0, 0.5, 1], fx, None, lambda v: str(v)))
    o.append(C(fx(0.3), ys, 8, LV)); o.append(T(fx(0.3), ys - 14, 'fake 0.3', 13, fill=LV, bold=True))
    o.append(C(fx(0.8), ys, 8, NX)); o.append(T(fx(0.8), ys - 14, 'real 0.8', 13, fill=NX, bold=True))
    o.append(boxt(20, 270, 330, 70, ['D maximizes V', 'ln 0.8 + ln(1 − 0.3)', '= −0.223 − 0.357 = −0.580'], ACS, AC, 14, bold_first=True))
    o.append(boxt(370, 270, 330, 70, ['G minimizes L_G = −ln D(G(z))', '−ln 0.3 = 1.204', 'lower as D(G(z)) moves toward 1'], LVS, LV, 14, bold_first=True))
    return 356, ''.join(o)
FIG[4] = (f4, 'The discriminator scores the real sample 0.8 and the fake one 0.3. Those give its objective V = −0.580, which D tries to raise, and the generator loss L_G = −ln 0.3 = 1.204, which G tries to lower.',
          'Noise goes through the generator to a fake sample; the fake and a real sample go into the discriminator, which scores them 0.3 and 0.8 on a 0 to 1 scale, with V = −0.580 and L_G = 1.204 in boxes below.')


# ---- 6.5 autoregressive product over three pixels ----
def f5():
    o = [T(20, 26, 'Pixels are predicted one at a time in a fixed order, each given the ones before it', 14, 'start', bold=True)]
    cells = [('x₁ = 1', 'p(x₁ = 1)', '0.6'), ('x₂ = 1', 'p(x₂ = 1 | x₁ = 1)', '0.7'), ('x₃ = 0', 'p(x₃ = 0 | x₁ = 1, x₂ = 1)', '0.8')]
    for i, (v, lab, p) in enumerate(cells):
        x = 60 + i * 230
        o.append(R(x, 50, 70, 70, INK if v.endswith('1') else PANEL, INK, 4, 2))
        o.append(T(x + 35, 92, v, 15, fill=FIGBG if v.endswith('1') else INK, bold=True))
        o.append(T(x + 35, 144, lab, 13, fill=AC))
        o.append(T(x + 35, 164, p, 15, fill=AC, bold=True))
        if i < 2:
            o.append(L(x + 74, 85, x + 222, 85, L2, 2, '5 4', arrow='m'))
            o.append(T(x + 148, 76, 'given', 13, fill=MUT))
    # running product bars
    yb, sc = 330, 200
    prods = [('after x₁', 0.6, '0.6'), ('× 0.7', 0.42, '0.6 × 0.7 = 0.42'), ('× 0.8', 0.336, '0.42 × 0.8 = 0.336')]
    o.append(L(40, yb, 700, yb, L2, 1.5))
    for i, (lab, v, txt) in enumerate(prods):
        x = 60 + i * 230
        hot = i == 2
        o.append(R(x, yb - v * sc, 70, v * sc, NXS if hot else ACS, NX if hot else AC, 2, 1.6))
        o.append(T(x + 82, yb - v * sc + 16, txt, 13, 'start', NX if hot else AC, True))
        o.append(T(x + 35, yb + 20, lab, 13, fill=MUT, bold=True))
    o.append(T(20, yb + 50, 'p(1, 1, 0) = 0.6 × 0.7 × 0.8 = 0.336', 15, 'start', NX, True))
    return yb + 66, ''.join(o)
FIG[5] = (f5, 'The three conditionals are multiplied in the fixed order x₁, x₂, x₃: the first two give 0.42, and the third factor 0.8 brings the running product to p(1, 1, 0) = 0.336.',
          'Three pixel squares x₁ = 1, x₂ = 1 and x₃ = 0 with their conditional probabilities 0.6, 0.7 and 0.8, above bars of the running product 0.6, 0.42 and 0.336.')


# ---- 6.6 inpainting a masked square and its PSNR ----
def f6():
    o = []
    s, y, hs = 150, 50, 150 * 64 / 256
    titles = [('image with hole', AC), ('mask m', LV), ('composite', NX)]
    for k, (t, c) in enumerate(titles):
        x = 30 + k * 240
        o.append(T(x + s / 2, y - 12, t, 14, fill=c, bold=True))
        hx, hy = x + 60, y + 50
        if k == 0:
            o.append(R(x, y, s, s, ACS, AC, 2, 2)); o.append(R(hx, hy, hs, hs, FIGBG, AC, 0, 1.6, '4 3'))
            o.append(T(x + s / 2, y + s + 20, '256 × 256 = 65,536 px', 13, fill=MUT))
        elif k == 1:
            o.append(R(x, y, s, s, PANEL, L2, 2, 2)); o.append(R(hx, hy, hs, hs, LV, LV, 0, 1.6))
            o.append(T(x + 30, y + 26, 'm = 0', 13, fill=MUT, bold=True))
            o.append(T(hx + hs + 6, hy + hs + 18, 'm = 1', 13, 'start', LV, True))
            o.append(T(x + s / 2, y + s + 20, 'hole 64 × 64 = 4,096 px', 13, fill=MUT))
        else:
            o.append(R(x, y, s, s, ACS, NX, 2, 2)); o.append(R(hx, hy, hs, hs, NXS, NX, 0, 1.6))
            o.append(T(x + s / 2, y + s + 20, 'visible pixels kept, hole filled', 13, fill=MUT))
        if k < 2:
            o.append(L(x + s + 12, y + s / 2, x + 228, y + s / 2, AC, 2.2, arrow='n'))
    o.append(T(20, 258, 'missing fraction 4,096 ÷ 65,536 = 0.0625 = 6.25%', 14, 'start', LV, True))
    o.append(T(20, 286, 'PSNR = 10 log₁₀(255² ÷ MSE) = 10 log₁₀(65,025 ÷ 16)', 14, 'start'))
    o.append(T(62, 312, '= 10 log₁₀(4,064.06) = 10 × 3.609 = 36.09 dB', 14, 'start', NX, True))
    return 330, ''.join(o)
FIG[6] = (f6, 'The mask marks a 64 × 64 hole, 6.25% of the 256 × 256 image, with m = 1 at the missing pixels. The composite keeps the visible pixels and the generator’s fill; an MSE of 16 then gives PSNR 36.09 dB.',
          'Three squares: an image with a dashed hole, the mask with the hole marked m = 1, and the composite with the hole filled, above the 6.25% and PSNR 36.09 dB calculations.')


# ---- 6.7 deepfake detector confusion matrix ----
def f7():
    o = []
    x0, y0, cw, ch = 170, 70, 150, 70
    o.append(T(x0 + cw / 2, y0 - 12, 'flagged fake', 14, fill=AC, bold=True))
    o.append(T(x0 + cw * 1.5, y0 - 12, 'passed as real', 14, fill=AC, bold=True))
    o.append(T(x0 - 14, y0 + ch / 2 + 5, '1,000 real', 14, 'end', bold=True))
    o.append(T(x0 - 14, y0 + ch * 1.5 + 5, '1,000 fake', 14, 'end', bold=True))
    cells = [[('FP', '50', True), ('TN', '950', False)], [('TP', '900', False), ('FN', '100', True)]]
    for i, r in enumerate(cells):
        for j, (n, v, err) in enumerate(r):
            x, y = x0 + j * cw, y0 + i * ch
            o.append(R(x, y, cw, ch, LVS if err else PANEL, LV if err else L2, 0, 2 if err else 1.4))
            o.append(T(x + cw / 2, y + 30, v, 18, fill=LV if err else INK, bold=True))
            o.append(T(x + cw / 2, y + 52, n + (' (wrong)' if err else ''), 13, fill=LV if err else MUT, bold=err))
    o.append(brace(x0 + 4, x0 + cw - 4, y0 + 2 * ch + 10, NX))
    o.append(T(x0 + cw / 2, y0 + 2 * ch + 36, 'flagged: 950', 13, fill=NX, bold=True))
    xr = 500
    o.append(T(xr, 96, 'FPR = 50 ÷ 1,000 = 5%', 14, 'start', LV, True))
    o.append(T(xr, 116, 'real videos wrongly flagged', 13, 'start', MUT))
    o.append(T(xr, 166, 'FNR = 100 ÷ 1,000 = 10%', 14, 'start', LV, True))
    o.append(T(xr, 186, 'fakes that got through', 13, 'start', MUT))
    o.append(T(20, 292, 'precision = TP ÷ flagged = 900 ÷ 950 = 94.7% of flags are real fakes', 14, 'start', NX, True))
    return 310, ''.join(o)
FIG[7] = (f7, 'The detector’s confusion matrix: the two highlighted cells are its errors, 50 real videos flagged (FPR 5%) and 100 fakes missed (FNR 10%). Of the 950 videos it flags, 900 are fakes, a precision of 94.7%.',
          'A 2×2 table with rows 1,000 real and 1,000 fake and columns flagged fake and passed as real, holding 50, 950, 900 and 100, the error cells 50 and 100 highlighted, with FPR 5%, FNR 10% and precision 94.7%.')


spec = make_spec(FIG)
