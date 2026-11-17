"""Claude's hand-drawn figures for c-nlp-u7 (NLP, unit 7: speech processing), one per chapter, drawn from each chapter's
worked example, plus a repeated-name sentence in 7.5 and the university-hosted sources to drop. The figure sentence
in 7.4 still matches the new drawing."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}
TEXT = {}


# ---- 7.1 source, filter, samples and frames ----
def f1():
    o = []
    o.append(boxt(20, 20, 150, 60, ['source e[n]', 'vocal folds'], ACS, AC, 14, True))
    o.append(L(174, 50, 226, 50, AC, 2.5, arrow='n'))
    o.append(boxt(230, 20, 150, 60, ['filter h[n]', 'vocal tract'], NXS, NX, 14, True))
    o.append(L(384, 50, 436, 50, AC, 2.5, arrow='n'))
    o.append(boxt(440, 20, 260, 60, ['speech x[n], 2 s', 'sampled at 16 kHz, 16-bit'], PANEL, AC, 14, True))
    o.append(T(20, 118, '16000 samples/s × 2 s = 32000 samples;  32000 × 16 bits = 512000 bits = 64000 bytes (64 kB)', 14, 'start'))
    # frames on a time strip (first 70 ms)
    x0, x1, y = 60, 690, 160
    ms = lambda t: x0 + t / 70 * (x1 - x0)
    o.append(L(x0, y + 120, x1, y + 120, L2, 1.5))
    for t in range(0, 71, 10):
        o.append(L(ms(t), y + 116, ms(t), y + 124, L2, 1.5)); o.append(T(ms(t), y + 142, f'{t} ms', 12, fill=MUT))
    for i in range(5):
        a = i * 10
        yy = y + i * 20
        hl = i < 2
        o.append(R(ms(a), yy, ms(a + 25) - ms(a), 16, ACS if hl else PANEL, AC if hl else L2, 3, 1.5))
        o.append(T(ms(a + 25) + 6, yy + 13, f'frame {i + 1}', 12, 'start', MUT))
    o.append(brace(ms(10), ms(25), y - 6, NX, up=True))
    o.append(T((ms(10) + ms(25)) / 2, y - 14, '15 ms shared', 12, fill=NX, bold=True))
    o.append(T(20, y + 178, 'frame 25 ms = 400 samples, hop 10 ms = 160 samples', 14, 'start', INK, True))
    o.append(T(20, y + 202, 'frames = floor((32000 − 400) ÷ 160) + 1 = 197 + 1 = 198', 14, 'start', AC, True))
    return y + 216, ''.join(o)
FIG[1] = (f1, 'Speech is the source e[n] from the vocal folds shaped by the vocal-tract filter h[n]. Sampled at 16 kHz for 2 s it gives 32000 samples (64 kB), and 25 ms frames every 10 ms give 400-sample frames and 198 frames in all.',
          'Three blocks, source, filter and the sampled speech; below, a time strip with five overlapping 25 millisecond frames starting every 10 milliseconds, two neighbours sharing 15 milliseconds.')


# ---- 7.2 place and manner chart for five first sounds ----
def f2():
    places = ['bilabial', 'labiodental', 'alveolar']
    manners = ['stop', 'nasal', 'fricative']
    cell = {('stop', 'bilabial'): ('p', 'b'), ('nasal', 'bilabial'): ('', 'm'), ('fricative', 'labiodental'): ('f', ''), ('fricative', 'alveolar'): ('s', '')}
    word = {'p': 'pat', 'b': 'bat', 'm': 'mat', 'f': 'fat', 's': 'sat'}
    x0, y0, cw, ch = 150, 50, 180, 84
    o = []
    for j, p in enumerate(places):
        o.append(T(x0 + j * cw + cw / 2, y0 - 14, p, 14, bold=True))
    for i, m in enumerate(manners):
        o.append(T(x0 - 14, y0 + i * ch + ch / 2 + 5, m, 14, 'end', INK, True))
        for j, p in enumerate(places):
            x, y = x0 + j * cw, y0 + i * ch
            o.append(R(x + 3, y + 3, cw - 6, ch - 6, PANEL, LN, 6, 1))
            vl, vd = cell.get((m, p), ('', ''))
            for k_, s in enumerate((vl, vd)):
                if not s: continue
                cx = x + cw * (0.28 if k_ == 0 else 0.72)
                c, cs = (NX, NXS) if k_ == 0 else (AC, ACS)
                o.append(C(cx, y + ch / 2 - 8, 22, c, cs))
                o.append(T(cx, y + ch / 2 - 2, f'/{s}/', 16, bold=True))
                o.append(T(cx, y + ch / 2 + 30, word[s], 12, fill=MUT))
    o.append(L(x0 + cw * 0.28 + 24, y0 + ch / 2 - 8, x0 + cw * 0.72 - 24, y0 + ch / 2 - 8, L2, 1.5, '4 3'))
    o.append(T(x0 + cw / 2, y0 + ch / 2 - 14, 'voicing only', 11, fill=MUT))
    y = y0 + 3 * ch + 20
    o.append(C(40, y, 10, NX, NXS)); o.append(T(58, y + 5, 'voiceless (left in a cell): /p/, /f/, /s/ = 3', 14, 'start'))
    o.append(C(380, y, 10, AC, ACS)); o.append(T(398, y + 5, 'voiced (right): /b/, /m/ = 2', 14, 'start'))
    return y + 22, ''.join(o)
FIG[2] = (f2, 'The five first sounds placed by where they are made (columns) and how (rows), voiceless on the left of a cell and voiced on the right. /p/ and /b/ share a cell, so only voicing tells them apart; 3 of the 5 are voiceless.',
          'A three by three chart with columns bilabial, labiodental, alveolar and rows stop, nasal, fricative; /p/ and /b/ share the bilabial stop cell, /m/ is a bilabial nasal, /f/ a labiodental fricative and /s/ an alveolar fricative.')


# ---- 7.3 frames in time and harmonics in bins ----
def f3():
    o = [T(20, 24, 'fs = 16000 Hz, 25 ms frame (400 samples), 10 ms hop (160 samples), 512-point DFT', 14, 'start', INK, True)]
    # bins axis
    x0, x1, yb = 60, 690, 200
    fx = lambda k: x0 + k / 14 * (x1 - x0)
    o.append(L(x0, yb, x1, yb, L2, 2))
    for k in range(0, 14):
        o.append(L(fx(k), yb - 4, fx(k), yb + 4, L2, 1.2))
        if k % 2 == 0: o.append(T(fx(k), yb + 22, f'{k}', 12, fill=MUT))
    o.append(T(x1, yb + 22, 'bin k', 12, 'end', MUT))
    for k, f in [(4, 125), (8, 250), (12, 375)]:
        o.append(L(fx(k), yb, fx(k), yb - 90, AC, 4))
        o.append(T(fx(k), yb - 98, f'{f} Hz', 14, bold=True))
    o.append(brace(fx(0), fx(1), yb + 34, NX))
    o.append(T(fx(0.5) + 20, yb + 58, 'one bin = 16000 ÷ 512 = 31.25 Hz', 13, 'start', NX, True))
    o.append(T(x0, 62, 'Voiced frame, F0 = 125 Hz: harmonics at 125, 250, 375 Hz', 14, 'start', AC, True))
    o.append(T(x0, 84, 'land on bins 125 ÷ 31.25 = 4, 8 and 12', 14, 'start'))
    y = yb + 92
    o.append(boxt(20, y, 220, 56, ['frames in 1.00 s', 'floor(15600 ÷ 160) + 1 = 98'], PANEL, AC, 13, True))
    o.append(boxt(250, y, 220, 56, ['bins kept: 512 ÷ 2 + 1', '= 257 (256 without DC)'], PANEL, AC, 13, True))
    o.append(boxt(480, y, 220, 56, ['each frame', '= one spectrogram column'], ACS, AC, 13, True))
    return y + 68, ''.join(o)
FIG[3] = (f3, 'One frame\'s DFT on a bin axis: bins are 31.25 Hz apart, so the harmonics of a 125 Hz voice fall on bins 4, 8 and 12. One second of speech gives 98 frames, each one column of the spectrogram.',
          'A frequency axis in DFT bins 0 to 14 with spikes at bins 4, 8 and 12 labelled 125, 250 and 375 hertz, one bin bracketed as 31.25 hertz; boxes give 98 frames and 257 bins.')


# ---- 7.4 the mel curve against hertz ----
def f4():
    mel = lambda f: 2595 * math.log10(1 + f / 700)
    x0, x1, y0, y1 = 80, 640, 40, 330
    fx = lambda f: x0 + f / 8000 * (x1 - x0)
    fy = lambda m: y1 - m / 3000 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 2000, 4000, 6000, 8000], [0, 1000, 2000, 3000], fx, fy, 'frequency (Hz)', 'mel')]
    o.append(L(fx(0), fy(0), fx(3000), fy(3000), L2, 2, '7 5'))
    o.append(Tb(fx(2600), fy(2600) - 14, 'hertz read as mel', 13, 'end', MUT))
    o.append(P([(fx(f), fy(mel(f))) for f in range(0, 8001, 100)], AC, 3))
    for f, m in [(300, 402), (1000, 1000), (8000, 2840)]:
        o.append(C(fx(f), fy(m), 6, NX))
        lab = f'{f} Hz → {m} mel'
        if f == 8000: o.append(Tb(fx(f) - 10, fy(m) - 14, lab, 13, 'end', NX, True))
        elif f == 1000: o.append(Tb(fx(f) + 12, fy(m) + 20, lab, 13, 'start', NX, True))
        else: o.append(Tb(fx(f) + 12, fy(m) + 22, lab, 13, 'start', NX, True))
    o.append(L(fx(1000), fy(1000), fx(1000), y1, NX, 1.2, '3 4'))
    o.append(T(fx(5000), fy(1500), 'first 1000 Hz = 1000 ÷ 2840', 13, 'middle', INK, True))
    o.append(T(fx(5000), fy(1500) + 20, '= 35.2 % of the mel range', 13, 'middle', INK, True))
    return y1 + 50, ''.join(o)
FIG[4] = (f4, 'The mel curve rises steeply below 1 kHz and flattens above it, while the dashed line treats hertz as mel. 300 Hz is 402 mel, 1000 Hz is 1000 mel and 8000 Hz is 2840 mel, so the first 1000 Hz takes 35.2 % of the range.',
          'A plot of mel against frequency from 0 to 8000 hertz: a curve that bends over, a dashed straight line for comparison, and points at 300, 1000 and 8000 hertz.')
AFTER[4] = 3


# ---- 7.5 the MFCC chain with its numbers ----
def f5():
    row1 = [('25 ms frame', '400 samples'), ('Hamming', 'window'), ('DFT', '512 points'), ('mel filters', '26 triangles')]
    row2 = [('log', 'energies'), ('DCT', '13 MFCCs'), ('+ Δ + ΔΔ', '39 numbers'), ('× 100 frames/s', '3900 numbers/s')]
    o = []
    w, gap = 150, 28
    for r, row in enumerate((row1, row2)):
        y = 30 + r * 110
        for i, (a, b) in enumerate(row):
            x = 20 + i * (w + gap)
            last = r == 1 and i >= 2
            o.append(boxt(x, y, w, 60, [a, b], ACS if last else PANEL, AC, 14, True))
            if i < 3: o.append(L(x + w + 3, y + 30, x + w + gap - 3, y + 30, AC, 2, arrow='n'))
    o.append(P([(20 + 3 * (w + gap) + w / 2, 92), (20 + 3 * (w + gap) + w / 2, 112), (20 + w / 2, 112), (20 + w / 2, 136)], AC, 2))
    o.append(L(20 + w / 2, 128, 20 + w / 2, 138, AC, 2, arrow='n'))
    o.append(T(20, 236, 'Raw: 16000 samples/s. Features: 3900 numbers/s, about 4.10 samples per feature number.', 14, 'start'))
    o.append(T(20, 260, 'Coding: 8 kHz × 8 bits = 64 kbps PCM; G.729 at 8 kbps uses 8 times fewer bits; LPC order at 16 kHz = 16 + 2 = 18.', 13, 'start', MUT))
    return 274, ''.join(o)
FIG[5] = (f5, 'The MFCC chain for one 25 ms frame at 16 kHz: 400 samples are windowed, transformed, pooled by 26 mel filters, logged and compressed by the DCT to 13 numbers; deltas make 39, and 100 frames a second give 3900 numbers a second.',
          'Eight blocks in two rows: frame, window, DFT, mel filters, then log, DCT giving 13 MFCCs, deltas giving 39 numbers, and 3900 numbers per second.')
TEXT[5] = [('The most common set is the mel-frequency cepstral coefficient (MFCC); some syllabi call it the mel-frequency cepstral coefficient.',
            'The most common set is the mel-frequency cepstral coefficients (MFCCs).')]


# ---- 7.6 the Bayes rule picks a sentence ----
def f6():
    cands = [('W1', 0.02, 0.001, 2.0e-5), ('W2', 0.01, 0.0005, 5.0e-6), ('W3', 0.008, 0.002, 1.6e-5)]
    o = [T(130, 26, 'P(X | W) acoustic', 13, fill=MUT, bold=True), T(340, 26, 'P(W) language model', 13, fill=MUT, bold=True), T(580, 26, 'product', 13, fill=MUT, bold=True)]
    for i, (w, a, p, prod) in enumerate(cands):
        y = 44 + i * 64
        win = w == 'W1'
        o.append(T(40, y + 30, w, 16, 'middle', NX if win else INK, True))
        o.append(R(70, y + 8, a / 0.02 * 120, 18, PANEL, L2, 3, 1.2)); o.append(T(76 + a / 0.02 * 120, y + 22, f'{a}', 13, 'start'))
        o.append(T(252, y + 22, '×', 16, bold=True))
        o.append(R(272, y + 8, p / 0.002 * 120, 18, PANEL, L2, 3, 1.2)); o.append(T(278 + p / 0.002 * 120, y + 22, f'{p}', 13, 'start'))
        o.append(T(462, y + 22, '=', 16, bold=True))
        o.append(R(490, y + 4, prod / 2.0e-5 * 160, 26, NXS if win else ACS, NX if win else AC, 4, 2 if win else 1.4))
        o.append(T(500, y + 46, f'{prod * 1e5:.1f} × 10⁻⁵' + ('  largest → chosen' if win else ''), 13, 'start', NX if win else INK, True))
    o.append(T(20, 246, 'W2 has better acoustics than W3 (0.01 vs 0.008) but a weaker prior, so W3 beats W2.', 13, 'start', MUT))
    o.append(T(20, 272, 'Word error rate on a 10-word reference: (2 S + 1 D + 1 I) ÷ 10 = 0.40', 14, 'start', INK, True))
    return 286, ''.join(o)
FIG[6] = (f6, 'Each candidate sentence scores acoustic likelihood times language-model prior. W1 has the largest product, 2.0 × 10⁻⁵, and is chosen; W3 beats W2 on the prior although W2 sounds closer.',
          'Three rows W1, W2 and W3 with bars for the acoustic likelihood, the prior and their product; W1 has the longest product bar, 2.0 times ten to the minus 5.')


# ---- 7.7 unit selection cost ----
def f7():
    o = [T(20, 24, 'Target diphone /a-t/: F0 180 Hz, 90 ms. Cost = 0.6 |ΔF0|/100 + 0.4 |Δd|/100 + join', 14, 'start', INK, True)]
    sc = 700
    rows = [('candidate 1', '170 Hz, 100 ms', [0.06, 0.04, 0.20], 0.30), ('candidate 2', '200 Hz, 80 ms', [0.12, 0.04, 0.50], 0.66)]
    cols = [(ACS, AC, 'F0'), (LVS, LV, 'duration'), (NXS, NX, 'join')]
    for i, (n, d, parts, tot) in enumerate(rows):
        y = 56 + i * 90
        o.append(T(150, y + 22, n, 15, 'end', INK, True)); o.append(T(150, y + 42, d, 12, 'end', MUT))
        x = 162
        for (f, c, lab), v in zip(cols, parts):
            o.append(R(x, y + 4, v * sc, 34, f, c, 3, 1.5))
            if v * sc > 44: o.append(T(x + v * sc / 2, y + 26, f'{v:.2f}', 13, bold=True))
            else: o.append(T(x + v * sc / 2, y + 56, f'{v:.2f}', 12, fill=c, bold=True))
            x += v * sc
        o.append(T(x + 10, y + 27, f'= {tot:.2f}' + ('  chosen' if i == 0 else ''), 15, 'start', AC if i == 0 else INK, True))
    y = 250
    for j, (f, c, lab) in enumerate(cols):
        o.append(R(162 + j * 150, y, 18, 14, f, c, 3, 1.5)); o.append(T(186 + j * 150, y + 12, lab + ' term', 13, 'start'))
    return y + 26, ''.join(o)
FIG[7] = (f7, 'Each candidate\'s cost stacks its F0 term, duration term and join cost. Candidate 1 totals 0.06 + 0.04 + 0.20 = 0.30 against 0.12 + 0.04 + 0.50 = 0.66, so the synthesiser picks candidate 1.',
          'Two stacked cost bars: candidate 1 with segments 0.06, 0.04 and 0.20 totalling 0.30, candidate 2 with 0.12, 0.04 and 0.50 totalling 0.66.')


# ---- 7.8 emotion confusion matrix ----
def f8():
    labs = ['angry', 'happy', 'neutral']
    M = [[32, 5, 3], [4, 28, 3], [2, 3, 20]]
    x0, y0, c = 170, 60, 100
    o = [T(x0 + 1.5 * c, 24, 'predicted', 14, fill=MUT)]
    for j, l in enumerate(labs):
        o.append(T(x0 + j * c + c / 2, 50, l, 14, bold=True))
    o.append(T(x0 + 3 * c + 70, 50, 'recall', 14, bold=True, fill=AC))
    for i, l in enumerate(labs):
        o.append(T(x0 - 14, y0 + i * 70 + 40, l, 14, 'end', INK, True))
        for j in range(3):
            d = i == j
            o.append(R(x0 + j * c + 3, y0 + i * 70 + 3, c - 6, 64, ACS if d else PANEL, AC if d else LN, 6, 2 if d else 1))
            o.append(T(x0 + j * c + c / 2, y0 + i * 70 + 42, str(M[i][j]), 20 if d else 16, bold=d, fill=INK if d else MUT))
        tot = sum(M[i])
        o.append(T(x0 + 3 * c + 70, y0 + i * 70 + 42, f'{M[i][i]}/{tot} = 0.80', 15, bold=True, fill=AC))
    o.append(T(40, y0 + 105, 'true', 14, fill=MUT))
    y = y0 + 3 * 70 + 30
    o.append(T(20, y, 'accuracy = (32 + 28 + 20) ÷ 100 = 0.80;  UAR = (0.80 + 0.80 + 0.80) ÷ 3 = 0.80', 14, 'start', INK, True))
    return y + 14, ''.join(o)
FIG[8] = (f8, 'Rows are the true emotions, columns the predictions. The diagonal holds 32, 28 and 20, so each class has recall 0.80, and accuracy and unweighted average recall are both 0.80.',
          'A three by three confusion matrix for angry, happy and neutral with diagonal counts 32, 28 and 20 shaded and a recall column showing 0.80 for each row.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])


def drop_sources():
    # university-hosted pages: the books name no universities
    return ['stanford.edu', 'fon.hum.uva.nl']
