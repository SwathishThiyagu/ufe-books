import json
from u import *
old = json.load(open('ch3.json'))
A1 = '<a href="#sampling-theorem-and-reconstruction-of-signals">sampling theorem and reconstruction</a>'
A2 = '<a href="#aliasing-and-anti-aliasing-filters">aliasing and anti-aliasing filters</a>'
A4 = '<a href="#quantization-of-sampled-signals">quantization of sampled signals</a>'
ch = {
'lead': "The sampling theorem of the first chapter is the <b>low-pass sampling theorem</b>: a signal from 0 to f_max needs f_s > 2f_max. A signal that occupies only a band from f_L to f_H, with nothing near zero, can be sampled far below 2f_H, because the empty space below f_L gives the copies room. Real samplers also take samples of finite width, and a held sample flattens the top of the band: that droop is the <b>aperture effect</b>. Radio receivers use band-pass sampling; every practical converter has to live with the aperture effect.",
'prereq': "You need: the repeated spectrum from " + A1 + " and the folding rule from " + A2 + ", plus the Fourier transform of a rectangular pulse (see Fourier transform of aperiodic signals).",
'sections': [
 sec("Band-pass sampling: use the empty gaps",
  p("Let a real signal have energy only between f_L and f_H, with bandwidth B = f_H − f_L. Sampling repeats the band (and its mirror image at negative frequencies) every f_s. The copies do not overlap if the whole band fits inside one <b>Nyquist zone</b>, a strip of width f_s/2 between (m − 1)f_s/2 and mf_s/2 for some integer m. Writing that condition for both band edges gives the <b>band-pass sampling theorem</b>:"),
  F("2f_H/m ≤ f_s ≤ 2f_L/(m − 1)", "Here m is an integer with 1 ≤ m ≤ ⌊f_H/B⌋. Each allowed m gives a range of valid rates; m = 1 is the low-pass case f_s ≥ 2f_H."),
  p("The largest m gives the lowest rate, f_s = 2f_H/m, which equals 2B when f_H is an exact multiple of B. At the ends of a range the copies touch, with no guard band, so a real design picks a rate inside a range. A band in an odd zone (m odd) lands near zero the right way round; in an even zone it lands mirrored, with high and low frequencies swapped. To rebuild the original signal, filter the samples with a band-pass filter from f_L to f_H; for digital processing, the copy near zero already holds all the information.")),
 sec("Natural and flat-top sampling",
  p("A real sampler cannot take an impulse. <b>Natural sampling</b> multiplies x(t) by a train of narrow pulses of width τ, so each pulse top follows the signal. Its spectrum is a set of copies of X(f) at kf_s with constant weights (τ/T_s) sinc(kτ/T_s): each copy keeps its shape, and a low-pass filter still recovers x(t) exactly."),
  p("<b>Flat-top sampling</b>, done by a sample-and-hold circuit, holds each sample value constant for τ seconds. The held train is the impulse train convolved with a rectangle of width τ, so its spectrum is X_s(f) multiplied by the rectangle's transform:"),
  F("H(f) = τ sinc(fτ) e^{−jπfτ}", "Here τ is the hold time in s, f the frequency in Hz and sinc(u) = sin(πu)/(πu). The factor e^{−jπfτ} is a delay of τ/2; it changes no amplitude."),
  p("The magnitude |sinc(fτ)| is 1 at 0 Hz, falls across the band and reaches zero at f = 1/τ. This frequency-dependent loss is the <b>aperture effect</b>: unlike natural sampling, the baseband copy itself is distorted. For a full-period hold (τ = T_s, the zero-order hold used to drive a DAC), the gain at f_s/2 is sinc(0.5) = 2/π ≈ 0.637, about −3.9 dB."),
  p("Two remedies are used. Make τ small compared with T_s, so that fτ stays near zero across the band. Or follow the hold with an <b>equalizer</b> of gain 1/|sinc(fτ)| over the signal band, often called an inverse-sinc filter. The equalizer also boosts noise near the band edge, so it is used only up to f_max. The held values are then rounded to a fixed number of levels, which is the next chapter, " + A4 + ".")),
],
'examples': [
 ex("A signal has components only between 5 kHz and 6 kHz. Find every range of valid sampling rates, the lowest rate, and a practical rate with a guard band. For the practical rate, find where the band lands between 0 and f_s/2.",
  ["f_L = 5 kHz, f_H = 6 kHz, B = 1 kHz, so m runs from 1 to ⌊6/1⌋ = 6. Low-pass sampling would need f_s > 2f_H = 12 kHz.",
   "Ranges 2f_H/m ≤ f_s ≤ 2f_L/(m − 1): m = 2 gives 6 to 10 kHz; m = 3 gives 4 to 5 kHz; m = 4 gives 3 to 3.33 kHz; m = 5 gives 2.4 to 2.5 kHz; m = 6 gives 2 to 2 kHz.",
   "Lowest rate: m = 6 gives f_s = 12/6 = 2 kHz = 2B, but only that single value works, with the copies touching at both edges.",
   "Practical rate: take m = 5 and f_s = 2.45 kHz, inside 2.4 to 2.5 kHz. Zone 5 runs from 4 × 2.45/2 = 4.9 kHz to 5 × 2.45/2 = 6.125 kHz, and 5 to 6 kHz lies inside it.",
   "The band lands at 5 − 2 × 2.45 = 0.1 kHz to 6 − 4.9 = 1.1 kHz, inside 0 to f_s/2 = 1.225 kHz, the right way round because m = 5 is odd.",
   "Margins: 0.1 kHz below the band image and 1.225 − 1.1 = 0.125 kHz above it."],
  "Valid ranges are 6–10, 4–5, 3–3.33, 2.4–2.5 kHz and exactly 2 kHz. The lowest rate is 2 kHz (no margin); 2.45 kHz is a practical choice, and the band then appears at 0.1–1.1 kHz, against 12 kHz for low-pass sampling."),
 ex("Speech up to 3.4 kHz is sampled at 8 kHz with flat-top pulses. Find the aperture gain at 3.4 kHz and the equalizer gain needed there (a) for a full-period hold τ = T_s, (b) for τ = 10 μs.",
  ["(a) τ = T_s = 1/8000 = 125 μs. fτ = 3400 × 125 × 10⁻⁶ = 0.425.",
   "sinc(0.425) = sin(0.425π)/(0.425π) = sin(1.335)/1.335 = 0.9724/1.335 = 0.728, which is 20 log₁₀ 0.728 = −2.75 dB.",
   "Equalizer gain at 3.4 kHz = 1/0.728 = 1.37, a boost of 2.75 dB.",
   "(b) τ = 10 μs: fτ = 3400 × 10 × 10⁻⁶ = 0.034, and sinc(0.034) = 0.998, only −0.017 dB.",
   "So a pulse 10 μs wide, 8% of the period, makes the aperture effect negligible."],
  "(a) Gain 0.728 (−2.75 dB), equalizer gain 1.37 at 3.4 kHz. (b) Gain 0.998 (−0.017 dB), no equalizer needed.")],
'traps': [
 "Rejecting a valid band-pass rate because it is below 2f_H. The low-pass condition is not the band-pass condition.",
 "Taking f_s = 2B and stopping there. It works only when f_H is a multiple of B, and even then the copies touch; check 2f_H/m ≤ f_s ≤ 2f_L/(m − 1).",
 "Saying natural sampling causes the aperture effect. Natural sampling only scales each copy; flat-top (sample-and-hold) sampling distorts the band.",
 "Confusing the hold time τ with the sampling period T_s. The first zero of sinc(fτ) is at 1/τ, which is f_s only for a full-period hold.",
 "Forgetting that 0.637 at f_s/2 is for τ = T_s; at the top of a real signal band (below f_s/2) the droop is smaller."],
'quiz': [
 Q('remember', 2, "State the low-pass and the band-pass sampling conditions.", "Low-pass: f_s > 2f_max. Band-pass: 2f_H/m ≤ f_s ≤ 2f_L/(m − 1) for an integer m with 1 ≤ m ≤ ⌊f_H/B⌋, where B = f_H − f_L."),
 Q('understand', 3, "Why can a band-pass signal be sampled below 2f_H?", "The spectrum from 0 to f_L is empty. The copies repeat every f_s, and with the right rate they fall into that empty space without overlapping the band or each other."),
 Q('apply', 4, "A signal occupies 20 kHz to 24 kHz. Find the lowest valid band-pass rate.", "B = 4 kHz, ⌊24/4⌋ = 6, so m = 6 and f_s = 2 × 24/6 = 8 kHz. Upper limit 2f_L/(m − 1) = 40/5 = 8 kHz, so 8 kHz is valid, with no margin."),
 Q('analyze', 4, "A 7–9 kHz band is sampled at 4 kHz, which equals 2B. Show that the copies overlap.", "Zones have width f_s/2 = 2 kHz: 6–8, 8–10 kHz. The band 7–9 kHz straddles 8 kHz, so it does not fit in one zone. In the formula, m can be at most ⌊9/2⌋ = 4, and m = 4 needs f_s ≥ 18/4 = 4.5 kHz (lower m needs even more), so 4 kHz is not allowed."),
 Q('apply', 3, "A full-period hold runs at f_s = 8 kHz. Find the aperture gain at 4 kHz and at 2 kHz.", "τ = 125 μs. At 4 kHz, fτ = 0.5 and the gain is 2/π ≈ 0.637. At 2 kHz, fτ = 0.25 and the gain is sin(π/4)/(π/4) ≈ 0.900."),
 Q('understand', 3, "What is the difference between natural and flat-top sampling?", "Natural sampling keeps the signal shape on each pulse top; its spectrum copies are only scaled. Flat-top sampling holds a constant value; the spectrum is multiplied by τ sinc(fτ), which droops at high frequency (the aperture effect)."),
 Q('analyze', 4, "If τ = 0.5T_s, find the aperture gain at f_s/2.", "fτ = (f_s/2)(0.5/f_s) = 0.25, so the gain is sinc(0.25) ≈ 0.900, about −0.9 dB, against 0.637 for a full-period hold.")],
'beyond': "Band-pass sampling is the basis of intermediate-frequency sampling in software-defined radios, where a fast converter digitises a narrow radio band far above zero. At such high input frequencies, random timing errors of the sampling clock (aperture jitter) start to limit the signal-to-noise ratio. Inverse-sinc filters are built into many high-speed DACs. Search next: undersampling, IF sampling, aperture jitter, sinc compensation."
}
ch = save(3, ch, old)
import sys; sys.path.insert(0, '../../pipeline'); import render as R; print(R.word_count(ch))
