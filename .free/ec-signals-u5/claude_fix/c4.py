import json
from u import *
old = json.load(open('ch4.json'))
A3 = '<a href="#low-pass-band-pass-and-practical-sampling">practical sampling</a>'
ch = {
'lead': "A held sample can take any value, but a converter stores it in a fixed number of bits, so it must round the sample to one of a finite set of levels. That rounding is <b>quantization</b>. The <b>quantization error</b> e_q = Q(x) − x, the rounded value minus the true sample, behaves like a small added noise. That noise model links the number of bits to accuracy: it predicts the hiss of digital audio, the resolution of a sensor and the dynamic range of a converter. Only a few syllabi list quantization in this subject; where it is listed, exams ask for the step size, one rounded sample and the SQNR.",
'prereq': "You need: where the held samples come from (see " + A3 + "), and the average power of a sinusoid, A²/2 (see Classification: energy, power, periodic, even and odd signals).",
'sections': [
 sec("Levels and step size",
  p("A <b>uniform quantizer</b> with n bits has L = 2ⁿ output levels. If its L steps exactly tile the input range from x_min to x_max, each step has width"),
  F("Δ = (x_max − x_min)/L", "Here Δ is the step size, also called the resolution, in volts; L = 2ⁿ is the number of levels and n the word length in bits."),
  p("This is the <b>mid-rise</b> quantizer: its levels sit at the middle of each step, at x_min + (k + ½)Δ for k = 0, 1, …, L − 1. For a 0 V to 8 V, 3-bit quantizer, L = 8, Δ = 1 V and the levels are 0.5 V, 1.5 V, …, 7.5 V. A <b>mid-tread</b> quantizer instead has a level at zero (levels at kΔ), so a zero input gives an exact zero output; its staircase is shifted by half a step, and a bipolar mid-tread quantizer uses an odd number of levels.")),
 sec("Error, noise power and SQNR",
  p("While the input stays inside the range, rounding to the nearest level gives |e_q| ≤ Δ/2. For a busy signal the error changes from sample to sample in an unpredictable way, so it is modelled as random noise spread uniformly between −Δ/2 and +Δ/2. Its mean is 0 and its power (variance) is"),
  F("P_q = Δ²/12", "Here P_q is the quantization noise power in V². It follows from the mean of e² over a uniform spread: (1/Δ) ∫ e² de from −Δ/2 to Δ/2 = Δ²/12."),
  p("A full-scale sinusoid has amplitude A = (x_max − x_min)/2 = LΔ/2 and power A²/2 = L²Δ²/8. Dividing by Δ²/12 gives SQNR = 1.5L² = 1.5 × 4ⁿ. In decibels:"),
  F("SQNR = 6.02n + 1.76 dB", "This holds for a full-scale sinusoid and uniform error. For a sine of smaller amplitude A, subtract 20 log₁₀(A_fs/A) dB, where A_fs = (x_max − x_min)/2."),
  p("Each extra bit halves Δ and adds about 6 dB. Inputs outside the range <b>overload</b> the quantizer: the output clips and the error can exceed Δ/2, so the noise model fails. <b>Companding</b> (μ-law in North America and Japan, A-law in India and Europe) compresses large amplitudes before a uniform quantizer and expands them after, which gives small signals smaller steps in volts; the SQNR then stays nearly constant over a wide range of input levels.")),
],
'examples': [ex(
 "A 3-bit uniform mid-rise quantizer covers 0 V to 8 V. Find L, Δ, the maximum error, the output and the error for an input sample of 3.4 V, the noise power, and the SQNR for a full-scale sinusoid.",
 ["L = 2³ = 8 levels.",
  "Δ = (8 − 0)/8 = 1 V. The levels are 0.5, 1.5, 2.5, 3.5, …, 7.5 V.",
  "Maximum error inside the range = Δ/2 = 0.5 V.",
  "3.4 V lies in the step from 3 V to 4 V, whose level is 3.5 V. Its distance to 3.5 V is 0.1 V and to 2.5 V is 0.9 V, so Q(3.4) = 3.5 V and e_q = 3.5 − 3.4 = +0.1 V.",
  "Noise power P_q = Δ²/12 = 1/12 = 0.0833 V².",
  "Full-scale sine: A = 4 V, power A²/2 = 8 V². SQNR = 8/(1/12) = 96, and 10 log₁₀ 96 = 19.82 dB. Check with the formula: 6.02 × 3 + 1.76 = 19.82 dB."],
 "L = 8, Δ = 1 V, maximum error 0.5 V, Q(3.4 V) = 3.5 V with e_q = +0.1 V, P_q = 0.0833 V², SQNR = 19.82 dB.")],
'traps': [
 "Using Δ as the maximum error. Inside the range the bound is Δ/2.",
 "Writing L = 2ⁿ − 1. That is the largest code value; the number of levels is 2ⁿ.",
 "Using 6.02n + 1.76 dB for a small or non-sinusoidal signal. It is for a full-scale sine with uniform error.",
 "Mixing up the sign of the error: this book uses e_q = Q(x) − x, so rounding 3.4 V up to 3.5 V gives +0.1 V.",
 "Ignoring overload: outside x_min to x_max the output clips and Δ²/12 no longer describes the error."],
'quiz': [
 Q('remember', 2, "Define quantization and resolution.", "Quantization maps each sample to the nearest of L allowed levels. Resolution is the step size Δ = (x_max − x_min)/L."),
 Q('understand', 3, "Why is quantization error modelled as uniform random noise?", "For a busy signal the error jumps around unpredictably and is spread evenly between −Δ/2 and +Δ/2, so it behaves like noise with zero mean and power Δ²/12."),
 Q('apply', 4, "A 4-bit quantizer covers −2 V to 2 V. Find L, Δ and the maximum error.", "L = 2⁴ = 16; Δ = 4/16 = 0.25 V; maximum error Δ/2 = 0.125 V."),
 Q('apply', 3, "Estimate the SQNR of an ideal 10-bit quantizer for a full-scale sinusoid.", "6.02 × 10 + 1.76 = 61.96 dB, about 62 dB."),
 Q('analyze', 4, "The 3-bit, 0 V to 8 V mid-rise quantizer receives 5.2 V. Find the output and the error. Is there overload?", "5.2 V lies in the 5 V to 6 V step, level 5.5 V. e_q = 5.5 − 5.2 = +0.3 V, within ±0.5 V. The input is inside the range, so there is no overload."),
 Q('analyze', 4, "A sine of amplitude 1 V feeds the 3-bit, 0 V to 8 V quantizer (centred at 4 V). Find its SQNR.", "A_fs = 4 V, so subtract 20 log₁₀(4/1) = 12.04 dB: SQNR = 19.82 − 12.04 = 7.78 dB. Check: (1²/2)/(1/12) = 6, and 10 log₁₀ 6 = 7.78 dB.")],
'beyond': "Real converters add a little random dither so the error really is noise-like, shape the noise out of the signal band, and use sigma-delta modulation for audio. A converter's measured SQNR gives its effective number of bits, ENOB = (SQNR − 1.76)/6.02. Search next: dither, noise shaping, sigma-delta ADC, ENOB."
}
ch = save(4, ch, old)
import sys; sys.path.insert(0, '../../pipeline'); import render as R; print(R.word_count(ch))
