import json
from u import *
old = json.load(open('ch1.json'))
A2 = '<a href="#aliasing-and-anti-aliasing-filters">aliasing and anti-aliasing filters</a>'
A3 = '<a href="#low-pass-band-pass-and-practical-sampling">low-pass, band-pass and practical sampling</a>'
ch = {
'lead': "A continuous signal can be replaced by a list of numbers if it has no frequency above f_max and we sample faster than 2f_max. The samples then keep all the information, and an ideal low-pass filter turns them back into the smooth waveform. This is the bridge from continuous-time to discrete-time processing: phone audio, ECG recorders and digital controllers all store samples instead of a continuous voltage. Sampling too slowly loses information for good; that failure is the next chapter, " + A2 + ".",
'prereq': "You need: the Fourier transform, the sinc spectrum and ideal filters (see Fourier series and Fourier transform); the impulse and standard signals (see Classification of signals and systems).",
'sections': [
 sec("The sampling theorem and its numbers",
  p("A signal is <b>band-limited</b> when its Fourier transform X(f) is zero for |f| > f_max, where f_max is the highest frequency in hertz. <b>Sampling</b> takes its values at the instants t = nT_s, where n = …, −2, −1, 0, 1, 2, … is any integer and T_s is the <b>sampling interval</b> in seconds. The <b>sampling rate</b> is f_s = 1/T_s samples per second, written in hertz."),
  p("<b>Sampling theorem.</b> A signal band-limited to f_max is completely determined by its samples x(nT_s) if f_s > 2f_max. The rate 2f_max is the <b>Nyquist rate</b>, a property of the signal. The longest allowed spacing, 1/(2f_max), is the <b>Nyquist interval</b>. Half the sampling rate, f_s/2, is the <b>Nyquist frequency</b>, a property of the sampler: components below it are kept as they are, and a component above it folds onto a lower frequency."),
  F("f_s = 1/T_s > 2f_max", "Here f_s is the sampling rate in Hz, T_s the sampling interval in s and f_max the highest frequency in the signal in Hz."),
  p("The inequality is strict. At f_s = 2f_max, a cosine exactly at f_max is sampled twice per period at the same two phases. Sampled at its peaks it looks fine, but sampled at its zero crossings every sample is 0, so its amplitude and phase cannot be recovered. Some syllabi call the result the Nyquist–Shannon or Whittaker–Kotelnikov–Shannon theorem.")),
 sec("Impulse-train model and the repeated spectrum",
  p("To see why the theorem holds, model the sampler as multiplication by an impulse train p(t) = Σ δ(t − nT_s), the sum running over all integers n. Each impulse in the product carries one sample value as its area."),
  F("x_s(t) = Σ x(nT_s) δ(t − nT_s)", "Here x_s(t) is the impulse-sampled signal and x(nT_s) the sample at t = nT_s."),
  p("The Fourier transform of the impulse train is another impulse train, of strength 1/T_s at every multiple of f_s. Multiplication in time becomes convolution in frequency, and convolving X(f) with an impulse at kf_s simply shifts it there. So the spectrum of the samples is the original spectrum repeated every f_s hertz:"),
  F("X_s(f) = (1/T_s) Σ X(f − kf_s)", "Here X_s(f) is the spectrum of the samples, X(f) the original spectrum, and k runs over all integers. Every copy is scaled by 1/T_s = f_s."),
  p("The copy at k = 0 is the <b>baseband</b> copy; it runs from −f_max to f_max. The next copy starts at f_s − f_max. The copies stay apart when f_s − f_max > f_max, which is exactly f_s > 2f_max. The empty gap between them, from f_max to f_s − f_max, is the <b>guard band</b>, of width f_s − 2f_max. If the copies overlap, high frequencies land on low ones: that is aliasing, the subject of " + A2 + ".")),
 sec("Ideal reconstruction and sinc interpolation",
  p("An ideal low-pass filter with cutoff f_s/2 and passband gain T_s keeps the baseband copy and removes all the others. The gain T_s cancels the 1/T_s scaling, so the output is x(t) with its original amplitude. Any cutoff inside the guard band works; f_s/2 is the usual choice because it sits in the middle."),
  F("H(f) = T_s for |f| < f_s/2, and 0 outside", "Here H(f) is the frequency response of the reconstruction filter."),
  p("In time, this filter's impulse response is h(t) = sinc(t/T_s), the inverse transform of a rectangle of height T_s and width f_s. Passing the impulse train through it replaces each impulse by a sinc pulse of height x(nT_s) centred at nT_s. Adding the pulses gives the <b>interpolation formula</b>:"),
  F("x(t) = Σ x(nT_s) sinc((t − nT_s)/T_s)", "Here sinc(u) = sin(πu)/(πu) with sinc(0) = 1, and the sum runs over all integers n."),
  p("Each sinc is 1 at its own sampling instant and 0 at every other sampling instant, so at t = nT_s the sum returns exactly the sample x(nT_s); between instants the pulses fill in the smooth curve. This filter is ideal: it is non-causal and has a vertical edge. Real circuits hold each sample and then smooth the staircase, which droops at high frequencies; that practical side and the band-pass case are in " + A3 + ".")),
],
'examples': [ex(
 "A voltage x(t) = 3 cos(2π·200t) + 2 cos(2π·450t) volts is sampled at f_s = 1000 Hz. Find f_max, the Nyquist rate, the Nyquist interval, T_s and the reconstruction filter. List the spectral lines between 0 and 1500 Hz, and find the guard band.",
 ["The frequency of each cosine is the number multiplying t inside 2π(…): 200 Hz and 450 Hz. So f_max = 450 Hz.",
  "Nyquist rate = 2f_max = 2 × 450 = 900 Hz. Nyquist interval = 1/900 s ≈ 1.11 ms. Since 1000 Hz > 900 Hz, the condition f_s > 2f_max holds.",
  "T_s = 1/f_s = 1/1000 = 0.001 s = 1 ms.",
  "Reconstruction filter: ideal low-pass, cutoff f_s/2 = 500 Hz, passband gain T_s = 0.001.",
  "Spectral lines on the positive axis: baseband at 200 and 450 Hz; the copy at 1000 Hz gives 1000 − 450 = 550, 1000 − 200 = 800, 1000 + 200 = 1200 and 1000 + 450 = 1450 Hz.",
  "Guard band: from f_max = 450 Hz up to the lowest copy line 550 Hz, width 550 − 450 = 100 Hz = f_s − 2f_max. The 500 Hz cutoff sits in the middle of it.",
  "The filter passes 200 and 450 Hz and stops 550 Hz and above, so the output is the original x(t)."],
 "f_max = 450 Hz, Nyquist rate = 900 Hz, Nyquist interval ≈ 1.11 ms, T_s = 1 ms, filter cutoff 500 Hz with gain 0.001, copy lines at 550, 800, 1200 and 1450 Hz, guard band 100 Hz; sampling at 1000 Hz is safe.")],
'traps': [
 "Nyquist rate (2f_max, fixed by the signal) and Nyquist frequency (f_s/2, fixed by the sampler) are different ideas. They are equal only when f_s = 2f_max, the borderline case.",
 "Dropping the gain T_s of the reconstruction filter: the output is then scaled by 1/T_s.",
 "Writing f_s ≥ 2f_max. A sinusoid exactly at f_max is not safe at f_s = 2f_max; the condition is strict.",
 "Unit slips: T_s in seconds, f_s in hertz; 1 ms = 0.001 s, and 1/(1 kHz) = 1 ms, not 1 s.",
 "Guard band is f_s − 2f_max, the gap between the top of the baseband and the bottom of the first copy, not f_s − f_max."],
'quiz': [
 Q('remember', 2, "Define Nyquist rate and Nyquist frequency.", "Nyquist rate is the minimum sampling rate 2f_max for a signal band-limited to f_max. Nyquist frequency is half the sampling rate, f_s/2. For f_max = 450 Hz and f_s = 1000 Hz they are 900 Hz and 500 Hz."),
 Q('understand', 3, "Why is f_s > 2f_max written with a strict inequality?", "At f_s = 2f_max a cosine at f_max is sampled at the same two phases every period. If those are its zero crossings, every sample is 0, so amplitude and phase are lost."),
 Q('apply', 4, "x(t) = 5 cos(2π·300t) is sampled at 800 Hz. Is it safe? Give T_s, the filter cutoff and the guard band.", "f_max = 300 Hz, Nyquist rate 600 Hz, and 800 > 600, so it is safe. T_s = 1/800 = 1.25 ms; cutoff f_s/2 = 400 Hz; guard band = 800 − 600 = 200 Hz (from 300 to 500 Hz)."),
 Q('analyze', 4, "A 450 Hz component is sampled at 1200 Hz. Find the lowest copy line and the guard band.", "The first copy line is 1200 − 450 = 750 Hz. Guard band = 750 − 450 = 300 Hz = f_s − 2f_max."),
 Q('understand', 3, "What do the cutoff and the gain of the ideal reconstruction filter each do?", "The cutoff f_s/2 keeps the baseband copy and removes the copies centred at ±f_s, ±2f_s, …. The gain T_s cancels the 1/T_s scaling that sampling put on every copy."),
 Q('remember', 2, "Write the interpolation formula and say what each sinc pulse does at the sampling instants.", "x(t) = Σ x(nT_s) sinc((t − nT_s)/T_s). Each pulse is 1 at its own instant nT_s and 0 at every other sampling instant."),
 Q('analyze', 5, "A signal has 200 Hz and 450 Hz components and is sampled at 900 Hz. Is exact reconstruction guaranteed?", "No. The Nyquist rate is 900 Hz and the condition is strict. The 450 Hz component sits exactly at f_s/2, where its samples depend on its phase, so its amplitude and phase cannot be recovered in general.")],
'beyond': "Audio codecs and software-defined radios choose f_s from the band of interest and use steep digital filters when they lower the rate. Medical recorders and vibration monitors use the same theorem to set their sampling rates. Compressive sensing samples fewer values when a signal is sparse, and sigma-delta converters sample very fast at low resolution and filter digitally. Search next: sinc interpolation, oversampling, compressive sensing."
}
ch = save(1, ch, old)
import sys; sys.path.insert(0, '../../pipeline'); import render as R; print(R.word_count(ch))
