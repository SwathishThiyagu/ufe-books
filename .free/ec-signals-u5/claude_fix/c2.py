import json
from u import *
old = json.load(open('ch2.json'))
A1 = '<a href="#sampling-theorem-and-reconstruction-of-signals">sampling theorem and reconstruction</a>'
ch = {
'lead': "Sampling makes copies of a spectrum every f_s hertz. If the signal has energy above f_s/2, neighbouring copies overlap and a high-frequency component shows up at a low frequency. That false low frequency is an <b>alias</b>, and nothing done to the samples afterwards can tell it from a real low tone. The cure is an analog <b>anti-aliasing filter</b> before the sampler. Every sound card, data-acquisition board and digital radio has one, because once an alias is in the samples it stays there.",
'prereq': "You need: the repeated spectrum and the guard band from " + A1 + ", and the ideal low-pass response (see Distortionless transmission, ideal filters and realizability).",
'sections': [
 sec("Spectral copies overlap",
  p("Sampling at f_s = 1/T_s repeats the spectrum X(f) at every multiple of f_s:"),
  F("X_s(f) = f_s Σ X(f − kf_s)", "Here X_s(f) is the spectrum of the samples, X(f) the spectrum of x(t), f_s the sampling rate in Hz and k any integer."),
  p("If X(f) = 0 for |f| ≥ f_s/2, the copies sit apart and the low-pass filter of the previous chapter rebuilds x(t). If the signal reaches past f_s/2, that is if f_s < 2f_max, a copy reaches into the band from 0 to f_s/2 and adds to the baseband copy. For a component between f_s/2 and f_s, the intruder is the copy centred at f_s, which puts it at f_s − f. For a component above f_s, it is a copy at a higher multiple of f_s; the folding rule below handles every case."),
  p("The overlap is <b>aliasing</b>; some syllabi call it fold-over or frequency folding. It is a permanent mixing of two frequencies in the same numbers, not a rounding error.")),
 sec("The folding rule",
  p("After sampling at f_s, a component at frequency f looks like the frequency |f − kf_s| that is nearest to zero, over all integers k. The result always lies between 0 and f_s/2."),
  table(['Original f (Hz)', 'Nearest kf_s (Hz)', 'Seen as (Hz)'],
        [['300', '0', '300'], ['700', '1000', '300'], ['900', '1000', '100'], ['1300', '1000', '300'], ['1700', '2000', '300'], ['2500', '2000 or 3000', '500']]),
  p("The table uses f_s = 1000 Hz. A 700 Hz tone is above f_s/2 = 500 Hz; its nearest multiple is 1000 Hz, so it is seen at |700 − 1000| = 300 Hz. The identity behind it, with t = n/1000 s:"),
  F("cos(2π·700n/1000) = cos(2πn − 2π·300n/1000) = cos(2π·300n/1000)", "The middle step uses cos(2πn − θ) = cos θ for every integer n. So cos(2π·700t) and cos(2π·300t) give the same samples at 1000 Hz, and so does cos(2π·1300t)."),
  p("For a single cosine the alias keeps its amplitude. For a real signal, several components can fold onto the same frequency and add or cancel there, so the aliased spectrum is not just a shifted copy of the original.")),
 sec("The anti-aliasing filter",
  p("An <b>anti-aliasing filter</b> (also called a prefilter) is an analog low-pass filter placed before the sampler. It must be analog: after sampling, the alias and the real tone are the same numbers, so no digital filter can separate them, and sampling faster later does not help either."),
  p("<b>Strict rule.</b> To stop any folding at all, the filter must remove everything at or above f_s/2. Its passband edge is f_max and its stopband edge is f_s/2, so the transition band is f_s/2 − f_max wide, half the guard band. <b>Usual design rule.</b> A component between f_s/2 and f_s − f_max folds to a frequency between f_max and f_s/2, outside the wanted band, and a digital filter can remove it later. Only components above f_s − f_max fold into the wanted band, so the stopband edge can be put at f_s − f_max, which gives the filter the whole guard band as its transition band."),
  p("A Butterworth low-pass filter of order N and 3 dB cutoff f_c has a flat passband and attenuation that grows with frequency:"),
  F("|H(f)|² = 1/(1 + (f/f_c)^{2N})", "Here |H(f)| is the magnitude response and N the filter order. For attenuation A dB at the stopband edge f_stop, the order is the smallest integer N ≥ log₁₀(10^{A/10} − 1) / (2 log₁₀(f_stop/f_c))."),
  p("A narrow transition band needs a high order; sampling faster widens the guard band and lets a simple filter do the job. This is why most converters oversample.")),
],
'examples': [
 ex("A speech signal occupies 300 Hz to 3400 Hz and is sampled at 8000 Hz. Is it safe from aliasing, and how wide is the guard band? A tone cos(2π·700t) volts is then sampled at 1000 Hz. What tone does the reconstruction filter give, and which other tone gives the same samples?",
  ["Speech: f_max = 3400 Hz, so the Nyquist rate is 2 × 3400 = 6800 Hz. Since 8000 > 6800, the speech does not alias.",
   "The first copy starts at f_s − f_max = 8000 − 3400 = 4600 Hz. Guard band = 4600 − 3400 = 1200 Hz = f_s − 2f_max. The Nyquist frequency 4000 Hz sits in the middle of it.",
   "Tone: f_s/2 = 1000/2 = 500 Hz, and 700 Hz > 500 Hz, so the tone aliases.",
   "Folding: the nearest multiple of 1000 Hz is 1000 Hz, and |700 − 1000| = 300 Hz. The 500 Hz reconstruction filter therefore outputs cos(2π·300t) volts, a 1 V tone at the wrong frequency.",
   "Other tones with the same samples: any f with |f − k·1000| = 300 Hz, for example 1300 Hz (k = 1) or 1700 Hz (k = 2); and the genuine 300 Hz tone itself."],
  "The speech is safe at 8000 Hz with a 1200 Hz guard band (3400 Hz to 4600 Hz). The 700 Hz tone comes out as cos(2π·300t) volts, and a 1300 Hz tone gives the same samples."),
 ex("The same speech (passband edge f_c = 3.4 kHz) needs at least 30 dB of attenuation on every component that would fold into the speech band. Find the Butterworth order needed at f_s = 8 kHz and at f_s = 16 kHz.",
  ["The stopband edge is f_stop = f_s − f_max. At 8 kHz, f_stop = 8 − 3.4 = 4.6 kHz; at 16 kHz, f_stop = 16 − 3.4 = 12.6 kHz.",
   "10^{A/10} − 1 = 10³ − 1 = 999, and log₁₀ 999 = 2.9996.",
   "At 8 kHz: f_stop/f_c = 4.6/3.4 = 1.353, log₁₀ 1.353 = 0.1313, so N ≥ 2.9996/(2 × 0.1313) = 11.42. Take N = 12.",
   "At 16 kHz: f_stop/f_c = 12.6/3.4 = 3.706, log₁₀ 3.706 = 0.5689, so N ≥ 2.9996/(2 × 0.5689) = 2.64. Take N = 3.",
   "Check N = 3 at 12.6 kHz: 10 log₁₀(1 + 3.706⁶) = 10 log₁₀(2593) = 34.1 dB, which is above 30 dB."],
  "N = 12 at f_s = 8 kHz, but only N = 3 at f_s = 16 kHz: doubling the sampling rate turns a 12th-order analog filter into a 3rd-order one.")],
'traps': [
 "Placing the anti-aliasing filter after the sampler. It is then a digital filter, and the alias is already inside the samples.",
 "Thinking a faster sampler can remove an alias that is already in recorded samples; the mixing has already happened.",
 "Reading the alias of 1300 Hz at f_s = 1000 Hz as 1300 − 500. Fold about multiples of f_s, not about f_s/2: |1300 − 1000| = 300 Hz.",
 "Saying every alias keeps its amplitude. That holds for one isolated cosine; components folding onto the same frequency add or cancel.",
 "Mixing up the guard band (f_s − 2f_max) with the strict transition band (f_s/2 − f_max), which is half of it."],
'quiz': [
 Q('remember', 2, "Define aliasing in one sentence.", "Aliasing is the overlap of spectral copies when a signal with energy above f_s/2 is sampled, so a high frequency appears in the samples as a lower one."),
 Q('understand', 3, "Why must the anti-aliasing filter be analog and placed before the sampler?", "After sampling, the alias and the wanted tone are the same sample values, so no digital filter can separate them. The analog filter removes the high frequency before the sampler can fold it."),
 Q('apply', 4, "A tone cos(2π·900t) volts is sampled at 1000 Hz. Find the frequency and amplitude seen after reconstruction.", "f_s/2 = 500 Hz and 900 > 500, so it aliases to |900 − 1000| = 100 Hz. The amplitude stays 1 V: the output is cos(2π·100t) volts."),
 Q('apply', 3, "A signal occupies 0 to 4 kHz and is sampled at 10 kHz. Find f_s/2, the guard band and a valid anti-aliasing cutoff.", "f_s/2 = 5 kHz. Guard band = f_s − 2f_max = 10 − 8 = 2 kHz (from 4 kHz to 6 kHz). The passband must reach 4 kHz; a cutoff of about 4 kHz with the stopband edge at or below 6 kHz works."),
 Q('analyze', 4, "At f_s = 1000 Hz, which frequencies give the same samples as a 700 Hz tone? Give three.", "All f with |f − k·1000| = 300 Hz: 300 Hz, 1300 Hz, 1700 Hz, 2300 Hz, …. Any three of these."),
 Q('analyze', 4, "A 3400 Hz tone is sampled at 6800 Hz. Is it safe? What is seen at f_s = 6000 Hz?", "At 6800 Hz the tone sits exactly at f_s/2, the borderline case, so it is not safe. At 6000 Hz, f_s/2 = 3000 Hz and the tone folds to |3400 − 6000| = 2600 Hz."),
 Q('remember', 2, "State the folding rule.", "A component at f is seen at the frequency |f − kf_s| nearest to zero over all integers k; the result lies between 0 and f_s/2.")],
'beyond': "In real converters anti-aliasing is shared between a simple analog filter and oversampling. Sigma-delta converters sample at many times the final rate and lower the rate with sharp digital filters, which relaxes the analog filter. Radio receivers put band filters before the converter because a strong out-of-band transmitter would otherwise fold onto a weak channel. Search next: oversampling, decimation, sigma-delta ADC, analog front end."
}
ch = save(2, ch, old)
import sys; sys.path.insert(0, '../../pipeline'); import render as R; print(R.word_count(ch))
