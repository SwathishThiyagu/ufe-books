"""Chapter-by-chapter corrections for ec-signals-u3 (applied by fix.py on top of the draft state)."""
import re

A = {  # chapter anchors
    1: 'fourier-series-trigonometric-and-exponential-forms-properties',
    2: 'fourier-transform-of-aperiodic-signals',
    3: 'fourier-transform-properties-convolution-and-modulation-theorems',
    4: 'parseval-s-theorem-energy-and-power-spectrum',
    5: 'frequency-response-of-lti-systems',
    6: 'distortionless-transmission-ideal-filters-and-realizability',
    7: 'correlation-and-spectral-density-of-signals',
    8: 'hilbert-transform-and-its-properties',
}
def a(k, t): return f'<a href="#{A[k]}">{t}</a>'


def find_block(ch, start):
    for s in ch['sections']:
        for i, b in enumerate(s['blocks']):
            if str(b.get('text', '')).startswith(start) or (b.get('type') == 'table' and start == 'TABLE'):
                return s['blocks'], i
    raise SystemExit(f'block not found: {start[:60]}')


def chapter(k, ch, rep):
    return globals()[f'c{k}'](ch, rep)


# ------------------------------------------------------------------ 3.1
def c1(ch, rep):
    ch['prereq'] = ('You need: periodic signals, even and odd symmetry, and orthogonal signals (see the topics '
                    '<i>Classification: energy, power, periodic, even and odd signals</i> and <i>Signals as vectors: orthogonal signal space</i>).')
    ch = rep(ch, [
        ('The 50 Hz current drawn by a half-controlled rectifier behaves this way: its harmonics sit at 50, 150, 250 Hz, and the even ones are absent.',
         'The square-wave current drawn from a 50 Hz supply by a bridge rectifier with a large inductive load behaves this way: its harmonics sit at 50, 150, 250 Hz, and the even ones are absent.'),
        ('Forgetting that the DC term of the trigonometric form is a₀/2, and that c₀ = a₀/2. Reading a₀ straight off as the average value is off by a factor of two.',
         'Mixing the two DC conventions. With x(t) = a₀/2 + Σ… and a₀ = (2/T₀)∫x(t)dt, as in this book, the DC value is a₀/2 = c₀. Some books write x(t) = a₀ + Σ… with a₀ = (1/T₀)∫x(t)dt, and then a₀ itself is the DC value. Pick one convention and keep it through the answer.'),
        ('Recent syllabi stress the two-sided exponential form because OFDM and digital filters work in complex baseband.',
         'The two-sided exponential form is also the everyday language of OFDM radios, which work with complex baseband signals.'),
        ('Power-quality engineers turn the same coefficients into total harmonic distortion limits, so a rectifier\'s current harmonics can be checked against a standard. ', ''),
    ])
    ch['quiz'] = [q for q in ch['quiz'] if not q['q'].startswith('Why does multiplying by cos(nω₀t)')]
    return ch


# ------------------------------------------------------------------ 3.2
def c2(ch, rep):
    ch['prereq'] = f'You need: {a(1, "Fourier series")}, the standard signals (impulse, step, exponential, signum) and limits from first-year calculus.'
    ch = rep(ch, [
        ('Define X<sub>n</sub>=c_nT₀.', 'Define X<sub>n</sub>=c<sub>n</sub>T₀.'),
        ('Here X(ω) is the spectrum; dω is an infinitesimal frequency step; the factor 1/2π converts an ω integral to an f integral.',
         'Here X(ω) is the spectrum and dω is a small step of angular frequency. The 1/2π comes from the line spacing: the sum (1/T₀)Σ… becomes (1/2π)Σ…Δω, and Δω becomes dω. If you work with f in hertz (ω = 2πf, dω = 2π df), the factor cancels and x(t) = ∫X(f)e<sup>j2πft</sup>df.'),
        ('The integral converges if ∫|x(t)|dt<∞. Finite jumps and finite peaks are allowed. X(ω) is then continuous in ω. Some syllabi write X(jω) for the same function.',
         'The transform exists when x(t) meets the Dirichlet conditions: ∫|x(t)|dt<∞, and only finitely many maxima, minima and finite jumps in any finite interval. X(ω) is then continuous in ω. These conditions are sufficient, not necessary: the constant 1, the step u(t), sgn(t) and cos ω₀t fail them, yet they get transforms that contain impulses (the table below). Some syllabi write X(jω) for the same function.'),
        ('The table lists pairs to memorise; each follows from the defining integral.',
         'Some syllabi call this part "Fourier transform of standard signals and periodic signals". The table lists the pairs to memorise. The pulse, the impulse and the two exponentials follow from the defining integral; the constant, the signum, the step and the sinusoids need a limit or duality, and their transforms contain impulses.'),
        ('This trade is why a short UPI confirmation burst needs more bandwidth than a steady carrier.',
         'This trade is why a short pulse needs more bandwidth than a long one: a 1 μs pulse has its first spectral zero at ω = 2π×10⁶ rad/s (1 MHz), a 1 ms pulse at 2π×10³ rad/s (1 kHz).'),
        ('Assuming a time-limited pulse has a finite spectrum. A rectangular pulse has sinc tails for all ω.',
         'Assuming a time-limited pulse is band-limited. A rectangular pulse has sinc tails that never end, so its spectrum is nonzero at arbitrarily high ω.'),
        ('Here τ=2, so X(ω)=2Sa(ω). At ω=0, Sa(0)=1, so X(0)=2.',
         'Here τ=2, so X(ω)=2Sa(ω). Sa(y)=sin y/y tends to 1 as y→0 (the limit, since 0/0 is undefined), so X(0)=2. Check: X(0)=∫x(t)dt is the pulse area, 2×1=2.'),
        ('Practical software computes the DFT, which samples this transform; see Unit 6.',
         'Practical software computes the discrete Fourier transform (DFT), which samples this transform.'),
    ])
    blocks, i = find_block(ch, 'TABLE')
    blocks[i]['rows'] += [
        ['sgn(t)', '2/(jω)', '+1 for t>0, −1 for t<0; no DC'],
        ['u(t)', 'πδ(ω) + 1/(jω)', 'u(t) = ½ + ½ sgn(t)'],
        ['e<sup>jω₀t</sup>', '2πδ(ω−ω₀)', 'one line at +ω₀'],
        ['cos ω₀t', 'π[δ(ω−ω₀) + δ(ω+ω₀)]', 'two lines, real and even'],
        ['sin ω₀t', '−jπ[δ(ω−ω₀) − δ(ω+ω₀)]', 'two lines, imaginary and odd'],
    ]
    ch['examples'].append({
        'question': 'Find the Fourier transforms of the signum function sgn(t) and the unit step u(t). Check the signum result numerically at ω = 2 rad/s.',
        'steps': [
            'sgn(t) is not absolutely integrable (∫|sgn t|dt is infinite), so write it as a limit of a signal that is: sgn(t) = lim<sub>a→0</sub> [e<sup>−at</sup>u(t) − e<sup>at</sup>u(−t)], with a > 0.',
            'Transform the bracket: e<sup>−at</sup>u(t) ↔ 1/(a+jω), and e<sup>at</sup>u(−t) ↔ ∫<sub>−∞</sub><sup>0</sup>e<sup>at</sup>e<sup>−jωt</sup>dt = 1/(a−jω).',
            'Difference: 1/(a+jω) − 1/(a−jω) = [(a−jω) − (a+jω)]/(a²+ω²) = −2jω/(a²+ω²).',
            'Let a → 0: −2jω/ω² = −2j/ω = 2/(jω). So sgn(t) ↔ 2/(jω).',
            'Numerical check at ω = 2 rad/s with a = 0.1: −2j(2)/(0.01+4) = −j0.998, already within 0.3% of 2/(j2) = −j1.',
            'Unit step: u(t) = ½ + ½ sgn(t). The constant ½ transforms to ½·2πδ(ω) = πδ(ω), and ½ sgn(t) to ½·2/(jω) = 1/(jω).',
            'So u(t) ↔ πδ(ω) + 1/(jω). The impulse carries the average value ½ of the step; the 1/(jω) part carries the jump.',
        ],
        'answer': 'sgn(t) ↔ 2/(jω), with |2/(jω)| = 1 at ω = 2 rad/s; u(t) ↔ πδ(ω) + 1/(jω).',
    })
    return ch


# ------------------------------------------------------------------ 3.3
def c3(ch, rep):
    ch['prereq'] = f'You need: the {a(2, "Fourier transform and its standard pairs")} and the convolution integral (see <i>Convolution integral and its evaluation</i>).'
    ch = rep(ch, [
        ('Here a and b are constants, t₀ is a time shift in seconds, a is nonzero, ω₀ is a frequency shift in rad/s, and δ is the unit impulse.',
         'Here a and b are constants (in the scaling row a is any nonzero real number), t₀ is a time shift in seconds, ω₀ is a frequency shift in rad/s, and δ is the unit impulse. Each row is proved by putting the left side into the defining integral and substituting.'),
        ('So X(0)=½×4/104=2/104=0.019230769230769232 V·s.',
         'So X(0)=½×4/104=2/104=1/52≈0.0192 V·s. Direct check: ∫<sub>0</sub><sup>∞</sup>e<sup>−2t</sup>cos(10t)dt = 2/(2²+10²) = 2/104, the same value.'),
        ('and at ω=0, X(0)=0.019230769230769232 V·s.', 'and at ω=0, X(0)=1/52≈0.0192 V·s.'),
    ])
    blocks, i = find_block(ch, 'TABLE')
    rows = blocks[i]['rows']
    rows.insert(4, ['Time reversal', 'x(−t)', 'X(−ω)'])
    rows.insert(6, ['Frequency derivative', 't x(t)', 'j dX(ω)/dω'])
    rows += [['Convolution', 'x(t)*h(t)', 'X(ω)H(ω)'], ['Multiplication', 'x(t)y(t)', '(1/2π)X(ω)*Y(ω)']]
    ch['examples'].append({
        'question': 'Use the convolution theorem to find y(t) = x(t)*h(t) for x(t) = e<sup>−t</sup>u(t) and h(t) = e<sup>−2t</sup>u(t). Give y(1 s) and the peak of y(t).',
        'steps': [
            'Transforms: X(ω) = 1/(1+jω) and H(ω) = 1/(2+jω).',
            'Convolution theorem: Y(ω) = X(ω)H(ω) = 1/[(1+jω)(2+jω)].',
            'Partial fractions in s = jω: 1/[(1+s)(2+s)] = A/(1+s) + B/(2+s). At s = −1: A = 1/(2−1) = 1. At s = −2: B = 1/(1−2) = −1.',
            'So Y(ω) = 1/(1+jω) − 1/(2+jω), and from the standard pair, y(t) = (e<sup>−t</sup> − e<sup>−2t</sup>)u(t).',
            'At t = 1 s: y(1) = e<sup>−1</sup> − e<sup>−2</sup> = 0.3679 − 0.1353 = 0.2325.',
            'Peak: dy/dt = −e<sup>−t</sup> + 2e<sup>−2t</sup> = 0 gives e<sup>−t</sup> = ½, t = ln 2 = 0.693 s, and y = ½ − ¼ = 0.25.',
            'Check in time: ∫<sub>0</sub><sup>t</sup>e<sup>−τ</sup>e<sup>−2(t−τ)</sup>dτ = e<sup>−2t</sup>(e<sup>t</sup> − 1) = e<sup>−t</sup> − e<sup>−2t</sup>. Also Y(0) = ½ equals the area ∫y dt = 1 − ½ = ½.',
        ],
        'answer': 'y(t) = (e<sup>−t</sup> − e<sup>−2t</sup>)u(t); y(1) = 0.2325, and the peak is 0.25 at t = ln 2 ≈ 0.693 s.',
    })
    return ch


# ------------------------------------------------------------------ 3.4
def c4(ch, rep):
    ch['prereq'] = (f'You need: energy and power signals (see <i>Classification: energy, power, periodic, even and odd signals</i>), '
                    f'{a(1, "Fourier series")}, the {a(2, "Fourier transform")} and its {a(3, "properties")}.')
    ch = rep(ch, [
        ('For x(t)=e<sup>−3t</sup>u(t), compute the total energy E from the time waveform. Then verify Parseval\'s theorem using X(ω)=1/(3+jω).',
         'For x(t)=e<sup>−3t</sup>u(t), compute the total energy E from the time waveform. Then verify Parseval\'s theorem using X(ω)=1/(3+jω), and find the band |ω| ≤ B that holds 90% of the energy.'),
        ('(1/2π)(π/3)=1/6 J. Both methods give 0.1667 J.',
         '(1/2π)(π/3)=1/6 J. Both methods give 0.1667 J.'),
        ('E = 1/6 J ≈ 0.1667 J, and the Parseval integral gives the same value, so the theorem is verified.',
         'E = 1/6 J ≈ 0.1667 J from both sides, so the theorem is verified; 90% of the energy lies in |ω| ≤ 18.94 rad/s.'),
        ('A periodic signal has c0=0, c1=0.5, c−1=0.5, and all other cₙ=0.', 'A periodic signal has c₀=0, c₁=0.5, c₋₁=0.5, and all other cₙ=0.'),
    ])
    ex = ch['examples'][0]
    ex['steps'] += [
        'Energy inside |ω| ≤ B: (1/2π)∫<sub>−B</sub><sup>B</sup>dω/(9+ω²) = (1/2π)(2/3)tan<sup>−1</sup>(B/3). As a fraction of E = 1/6 this is (2/π)tan<sup>−1</sup>(B/3).',
        'Set (2/π)tan<sup>−1</sup>(B/3) = 0.9: tan<sup>−1</sup>(B/3) = 0.45π rad = 81°, so B = 3 tan 81° = 3 × 6.314 = 18.94 rad/s (about 3.0 Hz).',
    ]
    ch['examples'].append({
        'question': 'The pulse train of the Fourier series chapter (height 1, high for |t| < 1 s, period T₀ = 4 s) has c₀ = 0.5 and cₙ = sin(nπ/2)/(nπ). Find its average power from the waveform and from the coefficients, and the fraction of power in the DC term plus the first harmonic.',
        'steps': [
            'Time side: P = (1/T₀)∫<sub>T₀</sub>|x(t)|²dt = (1/4)∫<sub>−1</sub><sup>1</sup>1 dt = 2/4 = 0.5 W (1 Ω reference).',
            'Coefficient side: |c₀|² = 0.25. Only odd n are nonzero, with |cₙ|² = 1/(n²π²) for both +n and −n.',
            'Sum over ±n: 2 × (1/π²)(1 + 1/9 + 1/25 + …) = (2/π²)(π²/8) = 0.25, using the known series 1 + 1/3² + 1/5² + … = π²/8.',
            'Total: 0.25 + 0.25 = 0.5 W, equal to the time-domain value, as Parseval requires.',
            'DC plus first harmonic: 0.25 + 2/π² = 0.25 + 0.2026 = 0.4526 W, which is 0.4526/0.5 = 90.5% of the power.',
            'Adding the 3rd and 5th harmonics: 0.25 + (2/π²)(1 + 1/9 + 1/25) = 0.4833 W, or 96.7%.',
        ],
        'answer': 'P = 0.5 W from both sides; the DC term and the fundamental carry 0.4526 W, about 90.5% of it.',
    })
    return ch


# ------------------------------------------------------------------ 3.5
def c5(ch, rep):
    ch['prereq'] = (f'You need: the {a(2, "Fourier transform")}, the {a(3, "convolution theorem")}, and impulse response and convolution '
                    '(see <i>Impulse response and step response</i>).')
    ch = rep(ch, [
        ('Here A is input amplitude in volts or another unit; ω₀ is input angular frequency in rad/s; φ is input phase in radians or degrees; y(t) is the steady-state output.',
         'Here A is input amplitude in volts or another unit; ω₀ is input angular frequency in rad/s; φ is input phase in radians or degrees; y(t) is the steady-state output. The rule needs a stable system (h(t) absolutely integrable), so that H(ω) exists and the transient dies away; an unstable system never settles to this sinusoid.'),
        ('Low-pass: |H(0)|=1 and |H| falls as ω rises. High-pass: |H(0)|=0 and |H| rises as ω rises.',
         'Low-pass: |H| is largest near ω = 0 and falls as ω rises (|H(0)| = 1 only when the pass-band gain is normalised; 5/(1+jωRC) is still a low-pass, with |H(0)| = 5). High-pass: |H(0)|=0 and |H| rises as ω rises.'),
        ('For distortionless transmission, |H(ω)| must be constant and ∠H(ω) must be linear in ω. See <a href="#distortionless-transmission-ideal-filters-and-realizability">3.6</a> for ideal filters and realizability.',
         'For distortionless transmission, |H(ω)| must be constant and ∠H(ω) must be a straight line through the origin, ∠H(ω) = −ωt<sub>d</sub>; see ' + a(6, 'distortionless transmission and ideal filters') + '.'),
        ('The figure shows one RC low-pass on linear axes.', 'Figure 3.5.1 shows the RC low-pass of the worked examples on linear axes, with the two input frequencies marked.'),
        ('Confusing low-pass and high-pass from memory. Check H(0): low-pass has |H(0)|=1; high-pass has |H(0)|=0.',
         'Confusing low-pass and high-pass from memory. Check the two ends: a low-pass passes ω = 0 and attenuates large ω; a high-pass has |H(0)| = 0 and passes large ω.'),
    ])
    ch['examples'].append({
        'question': 'The same RC low-pass (RC = 1 ms) receives x(t) = 2 + 3 cos(2000t) V. Find the steady-state output.',
        'steps': [
            'Treat each frequency on its own (superposition). The input has a DC part (ω = 0) and a cosine at ω = 2000 rad/s.',
            'DC: H(0) = 1/(1+0) = 1, so the 2 V passes unchanged.',
            'At ω = 2000 rad/s: ωRC = 2000 × 0.001 = 2, so H = 1/(1+j2).',
            '|H| = 1/√(1+4) = 1/√5 = 0.4472; ∠H = −tan<sup>−1</sup>2 = −63.43°.',
            'Cosine output amplitude: 3 × 0.4472 = 1.342 V, phase −63.4°.',
            'Add the parts: y(t) = 2 + 1.342 cos(2000t − 63.4°) V.',
        ],
        'answer': 'y(t) = 2 + 1.34 cos(2000t − 63.4°) V: the DC passes untouched while the 2000 rad/s part is cut to 44.7% and delayed.',
    })
    return ch


# ------------------------------------------------------------------ 3.6
def c6(ch, rep):
    ch['prereq'] = f'You need: {a(5, "frequency response")} (magnitude and phase of H(ω)) and the rectangular-pulse and sinc pair of the {a(2, "Fourier transform")}.'
    for ex in ch['examples']:
        ex.pop('output', None)
    return ch


# ------------------------------------------------------------------ 3.7
def c7(ch, rep):
    ch['prereq'] = f'You need: the {a(2, "Fourier transform")}, the {a(3, "convolution theorem")} and {a(4, "energy and power spectra")}.'
    ch = rep(ch, [
        ('For a periodic signal of period T<sub>0</sub>, replace the limit by (1/T<sub>0</sub>)∫ over one period.',
         'For a periodic signal of period T₀, replace the limit by (1/T₀)∫ over one period.'),
    ])
    raw = [q for q in ch['quiz'] if q['q'].startswith('Why is R<sub>x</sub>(τ) even')]
    if raw:
        raw[0]['a'] = 'R<sub>x</sub>(−τ)=∫x(t)x(t−τ)dt. Put u=t−τ, so t=u+τ: R<sub>x</sub>(−τ)=∫x(u+τ)x(u)du=R<sub>x</sub>(τ). Swapping the order of a real product changes nothing.'
    return ch


# ------------------------------------------------------------------ 3.8
def c8(ch, rep):
    ch['prereq'] = (f'You need: the cosine pair of the {a(2, "Fourier transform")}, the phase response from {a(5, "frequency response")}, '
                    'and the signum function sgn(ω).')
    import json
    raw = json.dumps(ch, ensure_ascii=False).replace('H{', 'ℋ{')
    ch = json.loads(raw)
    ch = rep(ch, [
        ('Five properties follow from H<sub>H</sub>(ω)=−j sgn(ω).',
         'Write ℋ{x(t)} for the Hilbert transform of x(t). These properties follow from H<sub>H</sub>(ω)=−j sgn(ω).'),
    ])
    blocks, i = find_block(ch, 'Write ℋ{x(t)}')
    blocks[i + 1]['items'] += [
        'Same magnitude spectrum: |X̂(ω)| = |X(ω)| for ω≠0, so x(t) and x̂(t) have the same energy spectral density and the same autocorrelation.',
        'Symmetry: the Hilbert transform of an even signal is odd, and of an odd signal is even (the kernel 1/(πt) is odd).',
        'Modulated signals: if m(t) is low-pass with no spectrum above W and ω<sub>c</sub> > W, then ℋ{m(t)cos ω<sub>c</sub>t} = m(t)sin ω<sub>c</sub>t. Single-sideband modulation relies on this.',
        'More pairs: δ(t) → 1/(πt); 1/(1+t²) → t/(1+t²) (worked example 2).',
    ]
    ch['examples'].append({
        'question': 'Find the Hilbert transform of x(t) = 1/(1+t²). Check that x and x̂ have the same energy and are orthogonal.',
        'steps': [
            'Spectrum: e<sup>−|t|</sup> ↔ 2/(1+ω²); by duality, 2/(1+t²) ↔ 2π e<sup>−|ω|</sup>, so X(ω) = π e<sup>−|ω|</sup>.',
            'Multiply by −j sgn(ω): X̂(ω) = −jπ sgn(ω) e<sup>−|ω|</sup>.',
            'Recognise this with the frequency-derivative rule t x(t) ↔ j dX/dω: j d(πe<sup>−|ω|</sup>)/dω = j·π·(−sgn ω)e<sup>−|ω|</sup> = −jπ sgn(ω)e<sup>−|ω|</sup>. That is exactly X̂(ω).',
            'So x̂(t) = t x(t) = t/(1+t²). At t = 1 s: x(1) = 0.5 and x̂(1) = 0.5; at t = 0: x = 1 and x̂ = 0.',
            'Energy: ∫dt/(1+t²)² = π/2 and ∫t²dt/(1+t²)² = π/2, so both energies are π/2 ≈ 1.571.',
            'Orthogonality: ∫x x̂ dt = ∫t/(1+t²)² dt = 0, because the integrand is odd. An even input gave an odd output, as the symmetry property says.',
        ],
        'answer': 'ℋ{1/(1+t²)} = t/(1+t²); both signals have energy π/2 ≈ 1.571 and their product integrates to zero.',
    })
    return ch


# ------------------------------------------------------------------ unit sections
def unit(us, rep):
    import answers
    us = rep(us, [
        ('x(t) = a₀ + Σ (aₖ cos kω₀t + bₖ sin kω₀t), with a₀ the DC value and aₖ, bₖ the cosine and sine amplitudes.',
         'x(t) = a₀/2 + Σ (aₙ cos nω₀t + bₙ sin nω₀t), with a₀/2 the DC value and aₙ, bₙ the cosine and sine amplitudes.'),
        ('cₖ = (1/T₀) ∫ over T₀ of x(t) e<sup>−jkω₀t</sup> dt; c₀ is the average value and |cₖ| is the amplitude of the k-th harmonic.',
         'cₙ = (1/T₀) ∫ over T₀ of x(t) e<sup>−jnω₀t</sup> dt; c₀ is the average value, and for real x(t) the n-th harmonic has amplitude 2|cₙ|.'),
        ('A periodic signal x(t) with period T₀ written as x(t) = Σ over k of cₖ e<sup>jkω₀t</sup>, a sum of harmonically related sinusoids.',
         'A periodic signal x(t) with period T₀ written as x(t) = Σ over n of cₙ e<sup>jnω₀t</sup>, a sum of harmonically related sinusoids.'),
        ('ω₀ = 2π/T₀ rad/s, where T₀ is the smallest period of x(t); every other frequency in the series is an integer multiple kω₀.',
         'ω₀ = 2π/T₀ rad/s, where T₀ is the smallest period of x(t); every other frequency in the series is an integer multiple nω₀.'),
        ('∫ over T₀ of e<sup>jmω₀t</sup> e<sup>−jkω₀t</sup> dt equals T₀ when m = k and 0 otherwise; this is what lets each cₖ be extracted separately.',
         '∫ over T₀ of e<sup>jmω₀t</sup> e<sup>−jnω₀t</sup> dt equals T₀ when m = n and 0 otherwise; this is what lets each cₙ be extracted separately.'),
        ('E<sub>x</sub>(ω) = |X(ω)|², in joules per hertz; total energy E = (1/2π) ∫ E<sub>x</sub>(ω) dω.',
         '|X(ω)|², in joules per rad/s; total energy E = (1/2π) ∫ |X(ω)|² dω.'),
        ('For a periodic or random signal, S(ω) gives the power per hertz; total average power P = (1/2π) ∫ S(ω) dω.',
         'For a power signal, S<sub>x</sub>(ω) = lim |X<sub>T</sub>(ω)|²/T gives the power per rad/s; total average power P = (1/2π) ∫ S<sub>x</sub>(ω) dω.'),
        ('A magnitude |H(ω)| is realizable by a causal system only if ∫ |ln|H(ω)|| dω is finite, so an exact brick-wall filter is not causal.',
         'A magnitude |H(ω)| with finite energy is realizable by a causal system only if ∫ |ln|H(ω)||/(1+ω²) dω is finite, so an exact brick-wall filter is not causal.'),
        ('R<sub>xx</sub>(τ) = ∫ x(t)x(t + τ) dt, measuring how much a signal resembles a shifted copy of itself; R<sub>xx</sub>(0) is the energy.',
         'R<sub>x</sub>(τ) = ∫ x(t)x(t + τ) dt, measuring how much a signal resembles a shifted copy of itself; R<sub>x</sub>(0) is the energy.'),
        ('The Fourier transform of the autocorrelation R<sub>xx</sub>(τ) is the energy spectral density |X(ω)|².',
         'The Fourier transform of the autocorrelation R<sub>x</sub>(τ) is the energy spectral density |X(ω)|² (for a power signal, the power spectral density).'),
        ('x̂(t) = (1/π) ∫ x(τ)/(t − τ) dτ, a filter with |H(ω)| = 1 and phase −90° for ω > 0 and +90° for ω < 0.',
         'x̂(t) = (1/π) PV∫ x(τ)/(t − τ) dτ, a filter H<sub>H</sub>(ω) = −j sgn(ω) with gain 1 and phase −90° for ω > 0 and +90° for ω < 0.'),
    ])
    for t in us['key_terms']:
        if t['term'] == 'Bandwidth': t['chapter'] = 2
        t['meaning'] = t['meaning'].replace('Σ |cₖ|²', 'Σ |cₙ|²')
    for b in us['textbooks']:
        if b['authors'].startswith('Alan V. Oppenheim'):
            b['pointer'] = 'Chapters 3 and 4 cover the Fourier series and the continuous-time Fourier transform'
    us['key_terms'].insert(10, {'term': 'Standard pairs', 'meaning': 'sgn(t) ↔ 2/(jω); u(t) ↔ πδ(ω) + 1/(jω); cos ω₀t ↔ π[δ(ω−ω₀) + δ(ω+ω₀)]; e<sup>−at</sup>u(t) ↔ 1/(a+jω).', 'chapter': 2})
    us['bank_note'] = ('Most syllabi ask for the transforms of standard and periodic signals (signum, step, cosine, rectangular pulse), the properties with proofs, '
                       'and the Hilbert transform with its properties. Long answers are judged on a derivation from the definition or from orthogonality, '
                       'each property stated with its condition, numbers carried to the end, and a labelled sketch of the magnitude and phase spectra.')
    us['bank'] = answers.BANK
    us['web'] = [x for x in us.get('web', []) if '.edu' not in x['url']]
    us['glossary'] = [g for g in us['glossary'] if g['term'] != 'White noise']
    us['glossary'] += [
        {'term': 'Signum function', 'def': 'sgn(t) = +1 for t > 0 and −1 for t < 0; its Fourier transform is 2/(jω).'},
        {'term': 'Energy spectral density', 'def': '|X(ω)|², the energy per rad/s of an energy signal; (1/2π) times its area is the total energy.'},
        {'term': 'Dirichlet conditions', 'def': 'Sufficient conditions for a Fourier series or transform to converge: absolute integrability and finitely many extrema and finite jumps in any finite interval.'},
    ]
    for g in us['glossary']:
        if g['term'] == 'Pre-envelope':
            g['def'] = 'Another name for the analytic signal x(t) + jx̂(t), whose spectrum is zero for negative frequencies.'
    us['takeaways'][-1] = 'The Hilbert transform is an all-pass 90° phase shifter (−j sgn ω); adding j times it to a real signal gives the analytic signal, with a one-sided spectrum, used in SSB and envelope detection.'
    us['takeaways'].insert(2, 'Signals that are not absolutely integrable, such as sgn(t), u(t) and cos ω₀t, still have Fourier transforms once impulses are allowed: 2/(jω), πδ(ω) + 1/(jω) and π[δ(ω−ω₀) + δ(ω+ω₀)].')
    return us


def plan(p):
    p['about'] = ('The unit starts with the Fourier series: a periodic signal becomes a sum of harmonics, in trigonometric or complex exponential form. '
                  'Letting the period grow gives the Fourier transform for aperiodic signals, with the standard pairs, including the signum, the step and periodic signals. '
                  'The next chapter collects the transform properties, especially convolution and modulation. Parseval\'s theorem then connects time-domain energy or power '
                  'to spectral densities. The frequency response H(ω) applies the transform to LTI systems, and the chapter after it uses H(ω) to define distortionless '
                  'transmission, ideal filters and realizability. Correlation adds a Fourier pair with spectral density, and the Hilbert transform, a −90° phase-shift filter, closes the unit.')
    return p


def web(w):
    # no university-hosted pages in the reading list
    return [x for x in w if 'ocw.mit.edu' not in x['url'] and '.edu' not in x['url']]
