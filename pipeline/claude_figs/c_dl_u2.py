"""Claude's hand-drawn figures for c-dl-u2 (one per chapter), as raw SVG bodies. The model for the other units.
Every number comes from the chapter's worked example. Colours are the shell's CSS variables."""
import math

INK, MUT, AC, LV, NX, L2 = 'var(--ink)', 'var(--muted)', 'var(--accent)', 'var(--live)', 'var(--next)', 'var(--line2)'

def T(x, y, s, size=14, anchor='middle', fill=INK, bold=False, italic=False):
    w = ' font-weight="700"' if bold else ''
    it = ' font-style="italic"' if italic else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" style="fill:{fill}"{w}{it}>{s}</text>'

def Tb(x, y, s, size=14, anchor='middle', fill=INK, bold=False):
    """text on a small background patch so lines behind it do not cut it"""
    n = len(s.replace('&#8722;', '-'))
    w = n * size * 0.56 + 10
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

def R(x, y, w, h, fill='var(--panel)', stroke=AC, rx=8, sw=2, dash=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}{d}"/>'

def boxt(x, y, w, h, lines, fill='var(--panel)', stroke=AC, size=14, bold_first=False):
    out = [R(x, y, w, h, fill, stroke)]
    lh = size * 1.3
    y0 = y + h / 2 - (len(lines) - 1) * lh / 2 + size * 0.35
    for i, s in enumerate(lines):
        out.append(T(x + w / 2, y0 + i * lh, s, size, bold=(bold_first and i == 0)))
    return ''.join(out)

def axes(x0, x1, y0, y1, xt, yt, fx, fy, xlab, ylab, xfmt=str, yfmt=str):
    o = [L(x0, y1, x1, y1, L2, 1.5), L(x0, y0, x0, y1, L2, 1.5)]
    for v in xt:
        X = fx(v); o += [L(X, y1, X, y1 + 5, L2, 1.5), T(X, y1 + 20, xfmt(v), 13, fill=MUT)]
    for v in yt:
        Y = fy(v); o += [L(x0 - 5, Y, x0, Y, L2, 1.5), L(x0, Y, x1, Y, 'var(--line)', 1), T(x0 - 9, Y + 4.5, yfmt(v), 13, 'end', MUT)]
    o.append(T((x0 + x1) / 2, y1 + 40, xlab, 14, fill=MUT))
    o.append(T(x0, y0 - 12, ylab, 14, 'start', MUT))
    return ''.join(o)

def neg(v):
    return str(v).replace('-', '&#8722;')

FIG = {}

# ---- 2.1 gradient descent on L = theta^2 ----
def f1():
    x0, x1, y0, y1 = 70, 690, 100, 380
    fx = lambda t: x0 + (t + 6.5) / 13 * (x1 - x0)
    fy = lambda l: y1 - l / 40 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [-6, -4, -2, 0, 2, 4, 6], [0, 10, 20, 30, 40], fx, fy, 'parameter θ', 'loss L(θ) = θ²', neg)]
    o.append(P([(fx(t / 10), fy((t / 10) ** 2)) for t in range(-63, 64)], L2, 2))
    good = [4, 3.2, 2.56, 2.048]
    for a, b in zip(good, good[1:]):
        o.append(L(fx(a), fy(a * a), fx(b) + 7, fy(b * b) - 5, AC, 2.5, arrow='n'))
    bad = [4, -4.8, 5.76]
    for a, b in zip(bad, bad[1:]):
        o.append(L(fx(a), fy(a * a), fx(b) + (8 if b < a else -8), fy(b * b) + 3, NX, 2.5, '7 5', arrow='x'))
    for t in good: o.append(C(fx(t), fy(t * t), 5, AC))
    for t in bad[1:]: o.append(C(fx(t), fy(t * t), 6, NX))
    o.append(Tb(fx(4) + 14, fy(16) + 5, 'θ₀ = 4, L = 16', 14, 'start'))
    o.append(Tb(fx(2.048) + 4, fy(4.19) + 26, 'θ₃ = 2.048, L ≈ 4.19', 14, 'start'))
    o.append(Tb(fx(-4.8) - 12, fy(23.04) + 5, 'θ₁ = −4.8, L = 23.04', 14, 'end'))
    o.append(Tb(fx(5.76) - 12, fy(33.18) - 8, 'θ₂ = 5.76, L ≈ 33.18', 14, 'end'))
    # legend
    o += [L(90, 28, 122, 28, AC, 3), T(130, 33, 'η = 0.1: θ × 0.8 each step, L × 0.64 (converges)', 14, 'start')]
    o += [L(90, 50, 122, 50, NX, 3, '7 5'), T(130, 55, 'η = 1.1: θ × (−1.2) each step, sign flips (diverges)', 14, 'start')]
    return 430, ''.join(o)
FIG[1] = (f1, 'Three steps on L(θ) = θ² from θ₀ = 4: with η = 0.1 the steps 4 → 3.2 → 2.56 → 2.048 slide down the bowl; with η = 1.1 the run jumps 4 → −4.8 → 5.76 and the loss climbs 16 → 23.04 → 33.18.',
          'Parabola L equals theta squared with two runs of gradient descent: small steps sliding to the bottom and large steps bouncing outward.')

# ---- 2.2 batch vs mini-batch ----
def f2():
    o = [T(40, 30, 'Mini-batch, B = 100: one epoch of N = 1000 samples', 15, 'start', bold=True)]
    x, w = 40, 64
    for i in range(10):
        o.append(R(x + i * w, 44, w - 4, 38, 'var(--accent-soft)', AC, 6))
        o.append(T(x + i * w + (w - 4) / 2, 68, '100', 13))
        cx = x + i * w + (w - 4) / 2
        o.append(L(cx, 84, cx, 108, AC, 2, arrow='n'))
        o.append(C(cx, 116, 6, AC))
    o.append(T(40, 150, '10 batches → 10 weight updates per epoch → 20 epochs = 200 updates', 14, 'start'))
    o.append(T(40, 200, 'Full batch: the same epoch', 15, 'start', bold=True))
    o.append(R(40, 214, 636, 38, 'var(--next-soft)', NX, 6))
    o.append(T(358, 238, 'all 1000 samples, one gradient', 14))
    o.append(L(358, 254, 358, 278, NX, 2, arrow='x'))
    o.append(C(358, 286, 6, NX))
    o.append(T(40, 320, '1 weight update per epoch → 20 epochs = 20 updates', 14, 'start'))
    o.append(T(40, 372, 'Gradient noise (spread of one gradient estimate)', 15, 'start', bold=True))
    s = 520 / 0.7
    o.append(R(250, 388, 0.632 * s, 24, 'var(--next-soft)', NX, 4))
    o.append(T(240, 405, 'one sample', 14, 'end'))
    o.append(T(250 + 0.632 * s - 8, 405, 'σ = √0.4 ≈ 0.632', 14, 'end'))
    o.append(R(250, 422, 0.0632 * s, 24, 'var(--accent-soft)', AC, 4))
    o.append(T(240, 439, 'batch of 100', 14, 'end'))
    o.append(T(250 + 0.0632 * s + 10, 439, 'σ = √(0.4/100) ≈ 0.063, ten times smaller', 14, 'start'))
    return 460, ''.join(o)
FIG[2] = (f2, 'With N = 1000 and B = 100, one epoch gives 10 updates instead of 1, so 20 epochs give 200 updates against 20; averaging 100 samples shrinks the gradient spread from about 0.632 to about 0.063.',
          'One epoch cut into ten batches of 100, each giving an update, compared with one full-batch update; bars compare gradient spread.')

# ---- 2.3 momentum ----
def f3():
    v, th, vs, ths = 0, 0, [0], [0]
    for _ in range(6):
        v = 0.9 * v + 0.2; th += v; vs.append(v); ths.append(th)
    x0, x1, y0, y1 = 60, 400, 100, 350
    fx = lambda s: x0 + s / 6 * (x1 - x0)
    fy = lambda t: y1 - t / 4 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, range(7), [0, 1, 2, 3, 4], fx, fy, 'step', 'position θ')]
    o.append(P([(fx(s), fy(0.2 * s)) for s in range(7)], NX, 2.5, '7 5'))
    o.append(P([(fx(s), fy(ths[s])) for s in range(7)], AC, 3))
    for s in range(7):
        o.append(C(fx(s), fy(0.2 * s), 4.5, NX)); o.append(C(fx(s), fy(ths[s]), 5, AC))
    o.append(Tb(fx(3) - 10, fy(1.122) - 10, 'θ₃ = 1.122', 14, 'end'))
    o.append(Tb(fx(3) + 6, fy(0.6) + 24, 'plain θ₃ = 0.6', 14, 'start'))
    o.append(T(fx(6) - 4, fy(ths[6]) - 14, 'momentum', 14, 'end'))
    o.append(T(fx(6), fy(1.2) + 34, 'plain GD', 14, 'end'))
    # velocity panel
    X0, X1 = 470, 700
    gy = lambda q: y1 - q / 2.4 * (y1 - y0)
    o.append(L(X0, y1, X1, y1, L2, 1.5)); o.append(L(X0, y0, X0, y1, L2, 1.5))
    for q in [0, 0.5, 1, 1.5, 2]:
        o += [L(X0 - 5, gy(q), X0, gy(q), L2, 1.5), T(X0 - 9, gy(q) + 4.5, str(q), 13, 'end', MUT)]
    o.append(L(X0, gy(2), X1, gy(2), LV, 2, '7 5'))
    o.append(Tb(X1 - 2, gy(2) - 10, 'limit ηg/(1 − β) = 2.0', 14, 'end'))
    bw = 28
    for s in range(1, 7):
        bx = X0 + 10 + (s - 1) * 36
        h = y1 - gy(vs[s])
        o.append(f'<rect x="{bx}" y="{gy(vs[s]):.1f}" width="{bw}" height="{h:.1f}" rx="4" style="fill:var(--accent-soft);stroke:{AC};stroke-width:2"/>')
        o.append(T(bx + bw / 2, y1 + 20, str(s), 13, fill=MUT))
    for s, lab in ((1, '0.2'), (2, '0.38'), (3, '0.542')):
        bx = X0 + 10 + (s - 1) * 36
        o.append(T(bx + bw / 2, gy(vs[s]) - 7, lab, 13))
    o.append(T((X0 + X1) / 2, y1 + 40, 'step', 14, fill=MUT))
    o.append(T(X0, y0 - 12, 'velocity v', 14, 'start', MUT))
    o += [L(70, 26, 102, 26, AC, 3), T(110, 31, 'momentum: v ← 0.9v + 0.1 × 2,  θ ← θ + v', 14, 'start')]
    o += [L(70, 48, 102, 48, NX, 3, '7 5'), T(110, 53, 'plain gradient descent: θ ← θ + 0.2', 14, 'start')]
    return 400, ''.join(o)
FIG[3] = (f3, 'With a constant descent direction g = 2, η = 0.1 and β = 0.9, momentum reaches θ₃ = 1.122 while plain descent reaches 0.6; the velocity grows 0.2, 0.38, 0.542 and levels off toward ηg/(1 − β) = 2.0.',
          'Left: position against step for momentum and plain gradient descent. Right: velocity bars rising toward a dashed limit of 2.')

# ---- 2.4 Adam ----
def f4():
    o = []
    o.append(boxt(14, 150, 112, 70, ['gradient', 'g = 1'], 'var(--panel)', AC, 14, True))
    o.append(T(170, 34, 'first moment (mean of g)', 14, 'start', MUT))
    o.append(boxt(160, 46, 200, 96, ['m ← 0.9m + 0.1g', 't = 1: m = 0.1', 't = 2: m = 0.19'], 'var(--accent-soft)', AC))
    o.append(T(170, 344, 'second moment (mean of g²)', 14, 'start', MUT))
    o.append(boxt(160, 228, 200, 96, ['v ← 0.999v + 0.001g²', 't = 1: v = 0.001', 't = 2: v = 0.001999'], 'var(--live-soft)', LV))
    o.append(boxt(392, 46, 160, 96, ['m̂ = m / (1 − 0.9ᵗ)', '0.1 / 0.1 = 1', '0.19 / 0.19 = 1'], 'var(--accent-soft)', AC))
    o.append(boxt(392, 228, 160, 96, ['v̂ = v / (1 − 0.999ᵗ)', '0.001 / 0.001 = 1', '0.001999 / 0.001999 = 1'], 'var(--live-soft)', LV, 13))
    o.append(T(472, 34, 'bias correction', 14, 'middle', MUT))
    o.append(boxt(584, 127, 124, 116, ['step', 'η·m̂ / (√v̂ + ε)', '= 0.01 × 1 / 1', '≈ 0.01'], 'var(--next-soft)', NX, 14, True))
    o.append(L(126, 175, 156, 110, AC, 2, arrow='n'))
    o.append(L(126, 195, 156, 260, LV, 2, arrow='l'))
    o.append(L(360, 94, 388, 94, AC, 2, arrow='n'))
    o.append(L(360, 276, 388, 276, LV, 2, arrow='l'))
    o.append(L(552, 100, 580, 150, AC, 2, arrow='n'))
    o.append(L(552, 270, 580, 220, LV, 2, arrow='l'))
    o.append(T(360, 372, 'Both steps are 0.01 = η: after correction the step size does not depend on the size of g.', 14))
    return 390, ''.join(o)
FIG[4] = (f4, 'Adam with η = 0.01 and g = 1 at t = 1 and t = 2: the raw moments m and v start small (0.1 and 0.001), bias correction lifts both to 1, and each step comes out at η = 0.01.',
          'Flow from the gradient into a first-moment and a second-moment average, then bias correction, then the combined Adam step, with the values for steps 1 and 2.')

# ---- 2.5 vanishing / exploding ----
def f5():
    x0, x1, y0, y1 = 80, 540, 60, 330
    fx = lambda k: x0 + k / 10 * (x1 - x0)
    fy = lambda lg: y1 - (lg + 7) / 9 * (y1 - y0)
    yt = [-6, -4, -2, 0, 2]
    o = [axes(x0, x1, y0, y1, range(0, 11, 2), yt, fx, fy, 'layers travelled back from the output', 'gradient size (log scale)', yfmt=lambda e: {0: '1', 2: '100'}.get(e, f'10{"⁻" + "⁰¹²³⁴⁵⁶⁷⁸⁹"[-e]}'))]
    for f, c, dash in ((1.5, LV, None), (1.0, L2, '7 5'), (0.25, NX, None)):
        pts = [(fx(k), fy(math.log10(f ** k))) for k in range(11)]
        o.append(P(pts, c, 3, dash))
        for p in pts: o.append(C(p[0], p[1], 4, c))
    o.append(T(fx(10) + 12, fy(math.log10(57.665)) + 5, '×1.5 → 57.7', 14, 'start'))
    o.append(T(fx(10) + 12, fy(0) + 5, '×1.0 → 1', 14, 'start'))
    o.append(T(fx(10) + 12, fy(math.log10(9.537e-7)) - 4, '×0.25 →', 14, 'start'))
    o.append(T(fx(10) + 12, fy(math.log10(9.537e-7)) + 14, '9.5 × 10⁻⁷', 14, 'start'))
    o.append(T(fx(10) + 12, fy(math.log10(57.665)) + 23, 'exploding', 13, 'start', MUT, italic=True))
    o.append(T(fx(10) + 12, fy(math.log10(9.537e-7)) + 32, 'vanishing', 13, 'start', MUT, italic=True))
    # clipping strip
    Y = 420
    o.append(T(40, Y - 30, 'Gradient clipping with threshold c = 5', 15, 'start', bold=True))
    s = 44
    o.append(L(60, Y, 60 + 12 * s, Y, NX, 4, arrow='x'))
    o.append(Tb(60 + 12 * s + 4, Y + 5, '‖g‖ = 12', 14, 'start'))
    o.append(L(60, Y + 40, 60 + 5 * s, Y + 40, AC, 4, arrow='n'))
    o.append(T(60 + 5 * s + 14, Y + 45, 'clipped: g × 5/12, ‖g‖ = 5, same direction', 14, 'start'))
    o.append(L(60 + 5 * s, Y - 18, 60 + 5 * s, Y + 58, L2, 2, '5 4'))
    o.append(T(60 + 5 * s, Y + 76, 'c = 5', 13, fill=MUT))
    return 510, ''.join(o)
FIG[5] = (f5, 'Starting from an output gradient of 1.0, ten layers with factor 0.25 leave about 9.5 × 10⁻⁷ at layer 1, factor 1.0 leaves 1, and factor 1.5 grows it to about 57.7; clipping at c = 5 shortens a norm-12 gradient to 5 without turning it.',
          'Log-scale plot of gradient size over ten layers for factors 0.25, 1 and 1.5, and below it an arrow of length 12 clipped to length 5.')

# ---- 2.6 He vs Xavier ----
def f6():
    x0, x1, y0, y1 = 60, 690, 100, 350
    fx = lambda w: x0 + (w + 0.45) / 0.9 * (x1 - x0)
    fy = lambda p: y1 - p / 3.8 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [-0.4, -0.2, 0, 0.2, 0.4], [0, 1, 2, 3], fx, fy, 'initial weight value', 'density', neg)]
    for sd, c, soft in ((0.115, NX, 'var(--next-soft)'), (0.141, AC, 'var(--accent-soft)')):
        pk = 1 / (sd * math.sqrt(2 * math.pi))
        pts = [(fx(w / 1000), fy(pk * math.exp(-(w / 1000) ** 2 / (2 * sd * sd)))) for w in range(-450, 451, 5)]
        o.append(P([(fx(-0.45), y1)] + pts + [(fx(0.45), y1)], c, 2.5, fill=soft, op=0.55))
    for sd, c, side in ((0.141, AC, 1), (0.115, NX, -1)):
        pk = 1 / (sd * math.sqrt(2 * math.pi)) * math.exp(-0.5)
        o.append(L(fx(side * sd), y1, fx(side * sd), fy(pk) - 30, c, 2, '5 4'))
    o.append(Tb(fx(0.141) + 6, fy(2.82 * math.exp(-0.5)) - 36, 'σ = 0.141', 14, 'start'))
    o.append(Tb(fx(-0.115) - 6, fy(3.47 * math.exp(-0.5)) - 36, 'σ = 0.115', 14, 'end'))
    o += [R(70, 20, 30, 14, 'var(--accent-soft)', AC, 3), T(108, 32, 'He (ReLU): Var = 2/n_in = 2/100 = 0.02, σ ≈ 0.141', 14, 'start')]
    o += [R(70, 44, 30, 14, 'var(--next-soft)', NX, 3), T(108, 56, 'Xavier (tanh): Var = 2/(n_in + n_out) = 2/150 ≈ 0.0133, σ ≈ 0.115', 14, 'start')]
    return 400, ''.join(o)
FIG[6] = (f6, 'For a layer with 100 inputs and 50 outputs, He draws weights with σ ≈ 0.141 and Xavier with σ ≈ 0.115; the He curve is wider by a factor of about 1.22 because ReLU zeroes about half the inputs.',
          'Two bell curves of initial weights centred on zero; the He curve is wider and lower than the Xavier curve, with each standard deviation marked.')

# ---- 2.7 batch normalization ----
def f7():
    ya, yb = 110, 300
    fa = lambda z: 80 + z * 70
    fb = lambda z: 360 + z * 140
    o = [T(40, 40, 'batch of pre-activations z', 15, 'start', bold=True)]
    o.append(L(fa(0), ya, fa(8), ya, L2, 2))
    for z in range(9):
        o += [L(fa(z), ya, fa(z), ya + 6, L2, 1.5), T(fa(z), ya + 24, str(z), 13, fill=MUT)]
    o.append(L(fa(4), ya - 50, fa(4), ya, LV, 2, '5 4'))
    o.append(Tb(fa(4), ya - 54, 'μ = 4', 14))
    o.append(L(fa(4), ya - 22, fa(4 + 2.236), ya - 22, LV, 2, arrow='l'))
    o.append(Tb(fa(5.1), ya - 30, 'σ = √5 ≈ 2.236', 14, 'start'))
    zs, zh = [1, 3, 5, 7], [-1.34, -0.45, 0.45, 1.34]
    for a, b in zip(zs, zh):
        o.append(L(fa(a), ya + 36, fb(b), yb - 28, L2, 1.5, arrow='m'))
    for a in zs:
        o.append(C(fa(a), ya, 7, AC))
    o.append(Tb(360, 206, 'ẑ = (z − μ) / σ = (z − 4) / 2.236', 15))
    o.append(L(fb(-2), yb, fb(2), yb, L2, 2))
    for z in (-2, -1, 0, 1, 2):
        o += [L(fb(z), yb, fb(z), yb + 6, L2, 1.5), T(fb(z), yb + 24, neg(z), 13, fill=MUT)]
    for b in zh:
        o.append(C(fb(b), yb, 7, NX))
        o.append(Tb(fb(b), yb - 14, neg(b), 14))
    o.append(T(40, yb + 56, 'normalized ẑ: mean 0, variance 1; with γ = 1 and β = 0 the output y = γẑ + β equals ẑ', 14, 'start'))
    return 370, ''.join(o)
FIG[7] = (f7, 'The batch z = 1, 3, 5, 7 has μ = 4 and σ² = 5; subtracting 4 and dividing by 2.236 maps it to −1.34, −0.45, 0.45, 1.34, which γ = 1 and β = 0 pass through unchanged.',
          'Two number lines: the batch values 1, 3, 5, 7 on top with the mean and standard deviation marked, and arrows down to the normalized values on the lower line.')

# ---- 2.8 L2 and dropout ----
def f8():
    o = [T(20, 30, 'L2 weight decay, λ = 0.01, η = 0.1', 15, 'start', bold=True)]
    rows = [['weight w = 2.0', 'penalty (λ/2)w² = 0.02'], ['penalty gradient', 'λw = 0.01 × 2.0 = 0.02'],
            ['step (data gradient is 0)', 'η × 0.02 = 0.002'], ['new weight', '2.0 − 0.002 = 1.998 (× 0.999)']]
    for i, r in enumerate(rows):
        y = 46 + i * 82
        o.append(boxt(20, y, 310, 60, r, 'var(--accent-soft)' if i < 3 else 'var(--next-soft)', AC if i < 3 else NX, 14, True))
        if i < 3: o.append(L(175, y + 62, 175, y + 78, AC, 2, arrow='n'))
    o.append(T(380, 30, 'Inverted dropout, p = 0.5', 15, 'start', bold=True))
    o.append(boxt(450, 46, 200, 50, ['hidden activation a = 3.0'], 'var(--panel)', AC))
    o.append(L(510, 98, 445, 168, AC, 2, arrow='n')); o.append(L(590, 98, 655, 168, L2, 2, '6 5', arrow='m'))
    o.append(Tb(470, 134, 'kept, 0.5', 14, 'end')); o.append(Tb(628, 134, 'drop, 0.5', 14, 'start'))
    o.append(boxt(370, 172, 150, 60, ['a / (1 − p)', '3.0 / 0.5 = 6.0'], 'var(--accent-soft)', AC, 14, True))
    o.append(boxt(580, 172, 120, 60, ['output', '0'], 'var(--panel)', L2, 14, True))
    o.append(L(445, 234, 500, 286, AC, 2, arrow='n')); o.append(L(640, 234, 590, 286, L2, 2, arrow='m'))
    o.append(boxt(380, 290, 320, 62, ['expected output', '0.5 × 6.0 + 0.5 × 0 = 3.0'], 'var(--next-soft)', NX, 14, True))
    return 380, ''.join(o)
FIG[8] = (f8, 'Left: with only the L2 penalty acting, w = 2.0 gets a gradient of 0.02 and moves 0.002 to 1.998. Right: inverted dropout with p = 0.5 doubles a kept activation of 3.0 to 6.0, so its expected value stays 3.0.',
          'Left, four boxes stepping a weight from 2.0 to 1.998 under L2. Right, a tree where an activation of 3.0 is kept and scaled to 6.0 or dropped to 0, averaging 3.0.')

# ---- 2.9 grid search ----
def f9():
    acc = {0.1: [0.71, 0.76, 0.72], 0.01: [0.79, 0.88, 0.85], 0.001: [0.62, 0.70, 0.74]}
    bs = [32, 128, 512]
    gx, gy, cw, chh = 190, 78, 136, 72
    o = [T(gx + 1.5 * cw, 30, 'batch size B', 14, fill=MUT), T(gx - 16, 30, 'learning rate η', 14, 'end', MUT)]
    for j, b in enumerate(bs): o.append(T(gx + j * cw + cw / 2, 62, f'B = {b}', 14, bold=True))
    for i, (lr, row) in enumerate(acc.items()):
        y = gy + i * chh
        o.append(T(gx - 16, y + chh / 2 + 5, f'η = {lr}', 14, 'end', bold=True))
        for j, a in enumerate(row):
            pct = int(8 + (a - 0.62) / 0.26 * 40)
            fill = f'color-mix(in srgb, var(--accent) {pct}%, var(--fig))'
            o.append(f'<rect x="{gx + j * cw + 2}" y="{y + 2}" width="{cw - 4}" height="{chh - 4}" rx="6" style="fill:{fill};stroke:var(--line);stroke-width:1"/>')
            o.append(T(gx + j * cw + cw / 2, y + chh / 2 + 6, f'{a:.2f}', 17, bold=(a == 0.88)))
    bx, by = gx + cw + 2, gy + chh + 2
    o.append(f'<rect x="{bx - 3}" y="{by - 3}" width="{cw + 2}" height="{chh + 2}" rx="8" style="fill:none;stroke:var(--ink);stroke-width:3"/>')
    o.append(T(gx + 3 * cw + 12, by + chh / 2 - 4, 'best 0.88', 14, 'start', bold=True))
    o.append(T(gx + 3 * cw + 12, by + chh / 2 + 16, 'η = 0.01', 14, 'start')); o.append(T(gx + 3 * cw + 12, by + chh / 2 + 34, 'B = 128', 14, 'start'))
    o.append(T(40, 330, 'Row maxima 0.76, 0.88, 0.74 → winner η = 0.01, B = 128 (validation accuracy 88%).', 14, 'start'))
    o.append(T(40, 356, 'Next: a finer grid η = 0.03, 0.01, 0.003 near B = 128; score the test set once at the very end.', 14, 'start'))
    # shade key
    for q in range(5):
        pct = int(8 + q * 10)
        o.append(f'<rect x="{612 + q * 20}" y="{84}" width="20" height="14" style="fill:color-mix(in srgb, var(--accent) {pct}%, var(--fig));stroke:var(--line)"/>')
    o.append(T(612, 116, 'darker =', 13, 'start', MUT)); o.append(T(612, 132, 'higher', 13, 'start', MUT))
    return 372, ''.join(o)
FIG[9] = (f9, 'The 3 × 3 grid of validation accuracies; the best run is 0.88 at η = 0.01 and B = 128, so the next search narrows around that cell before the test set is used once.',
          'A three by three table of validation accuracies, learning rate by batch size, shaded by accuracy, with the cell 0.88 outlined as the best.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
