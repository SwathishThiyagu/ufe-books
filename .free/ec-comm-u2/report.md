# ec-comm-u2: free-model run

- Book: `books/ece/ec-comm/ec-comm-u2.html`
- Status: ok
- Model calls so far: 24 (86,304 tokens in, 217,940 out), 6.1 minutes

## Checker

```
ec-comm-u2.html: 8 chapters, 22647 words, 9 figures, 298 KB
OK
```

## Correction pass (Claude, 21 Nov 2026)

- Every chapter rewritten from the draft; every worked example, quiz answer and trap recomputed in Python.
- All 25 reviewer notes below fixed (the five [high] ones first); eight figures hand-drawn from the worked examples
  (pipeline/claude_figs/ec_comm_u2.py); 13 question-bank items with full model answers; cross-unit references named by topic.

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Lead paragraph: The lead says the modulation index m sets 'how much bandwidth the signal uses'. For a single-tone AM signal the bandwidth is 2f_m, which depends only on the message frequency, not on m. Raising m only makes the sidebands taller; it does not widen the occupied band (only overmodulation, m > 1, spreads extra sidebands).
- ch 1 [low] Section 1, paragraph on the envelope: The comparison symbol is missing: 'When m 1 it goes negative' has no meaning as printed, and the whole overmodulation point is lost.
- ch 2 [low] Section 2, Section 3 and Worked example 1 step 5: The unit bookkeeping does not close. A_c is in volts, A_lo is in volts, and the product A_c A_lo m(t) is therefore in volts squared, yet y(t) is declared to be in volts. The worked example inherits the inconsistency: (10 V × 1 V / 2) × 2 V is written as 10 V.
- ch 2 [low] Section 1 formula: The where-list explains W (message bandwidth in hertz), but W does not appear anywhere in S(f) = (A_c/2)[M(f − f_c) + M(f + f_c)]. A student may hunt for a W that is not there.
- ch 2 [low] Quiz Q2: The answer restates the conclusion ('adds no separate carrier term') instead of giving the reason. The real reason no impulse appears at ±f_c is that m(t) has zero mean, so M(f) has no impulse at f = 0 for the shift to carry up to ±f_c.
- ch 2 [low] Exam traps, first bullet: It says the envelope is |m(t)|, while Section 2 correctly says |A_c m(t)|. The two statements do not match.
- ch 3 [low] Section 2, filter method: The sentence 'the filter must change from stop to pass within the width of the message' suggests a transition band as wide as W is acceptable. A transition band equal to W would cut the low-frequency part of the wanted sideband and leak a large part of the unwanted sideband.
- ch 3 [low] Section 2, Hilbert transform sentence and Quiz Q6 answer: The Hilbert transform is described only as 'every frequency component shifted by 90°' with no sign convention. With m(t) = cos 2πfmt, the stated USB formula needs m̂(t) = sin 2πfmt, that is, a delay of 90° at positive frequencies. A student who takes +90° gets m̂ = −sin and the wrong sideband.
- ch 3 [low] Figure 'SSB or VSB by filtering': The filter note says 'USB + 0.5 kHz vestige', which is a VSB signal only, but the output block is labelled 'SSB or VSB'. The figure appears to produce both at once.
- ch 4 [low] Lead and Section 3: DSB-SC is used from the lead onward but never expanded, so a student who has not read chapter 2.2 meets an undefined abbreviation.
- ch 4 [low] Section 2, bullet on the nearest unwanted product: 'The nearest unwanted product is the carrier second harmonic at 2f_c' is imprecise: with f_c = 100 kHz and f_m = 1 kHz, the 1 kHz tone and its 2 kHz harmonic sit about 97–98 kHz below the passband edge, and 2f_c sits 99 kHz above it. In absolute frequency they are all roughly equally far.
- ch 4 [low] Section 3, paragraph after the difference formula: The text first says the carrier is fed in phase to both devices, then says its linear terms are 'equal and opposite in the difference'. A student can read this as the carriers being in antiphase, which contradicts the setup.
- ch 4 [low] Quiz Q3: The parenthetical '(A, A/V, A/V²)' gives three units for a model with only two coefficients shown (i = 2v + 0.1v²); the leading 'A' has nothing to attach to and can confuse.
- ch 4 [low] Quiz Q6 answer: 'an envelope detector at the receiver would then produce output even without a proper carrier, giving distorted or false recovery' is muddled: the residual carrier is exactly what lets a simple envelope detector respond, and the trouble is that it is far weaker than a proper AM carrier.
- ch 5 [high] section 2 and worked example 1 (also the figure note): The chosen design value RC = 10 µs is not a good choice for fc = 100 kHz, because the carrier period is T = 1/fc = 10 µs. With RC = T the capacitor falls to e^(−1) ≈ 0.37 of the peak between carrier peaks, so the ripple is about 63 % of the peak — the output plainly does not 'hold the peak' as the figure claims. The lower limit 1/(2π fc) = 1.59 µs is only a filter-cutoff limit; the ripple limit a designer actually needs is RC ≫ 1/fc = 10 µs.
- ch 5 [low] worked example 1 step 4 and quiz Q7: Powers of ten are typed as plain digits: '1.59 × 10−6 s', '1/(2π × 106)', '1.59 × 10−7 s'. A student can read 106 as one hundred six and 10−7 as 'ten minus seven'.
- ch 6 [low] Section 2 formula: The formulas P_t = P_c(1 + m²/2) and P_sb = P_c m²/2 are presented with m described only as 'modulation index'. They are valid for single-tone sinusoidal modulation; with two or more audio tones a student will get the wrong total power if they insert a single m.
- ch 6 [low] Section 1: Class B push-pull is called the common linear final amplifier, but pure class B has crossover distortion at the point where the devices hand over. Practical low-level AM transmitters use class AB bias (or negative feedback) to keep the envelope linear.
- ch 6 [low] Section 2: 'The modulator is an audio power amplifier and must supply substantial power' is vague. For collector modulation the audio modulator must supply power equal to the total sideband power, P_c m²/2; at m = 1 this is half the carrier power. Without this a student cannot size the modulator or explain the efficiency cost.
- ch 7 [high] Worked example 1, step 4: The image at 1.910 MHz is stated to be 0.900 MHz above the passband centre at 1.000 MHz. The correct distance is 1.910 − 1.000 = 0.910 MHz. The stated number is wrong by 10 kHz and contradicts the 2fIF = 0.910 MHz used earlier in the same example.
- ch 7 [low] Section 2, formula line: The formula block gives fLO = fRF + fIF and fimage = fRF + 2fIF before any mention of high-side injection. A student reading the box first can take these as general formulas, which they are not; the high-side condition is only stated in the next paragraph.
- ch 7 [low] Section 1, second paragraph: "In AM broadcast it is commonly 455 kHz. Some syllabi call this the superhet receiver." placed back to back makes "this" look as if it points to the 455 kHz IF, so the sentence reads like 455 kHz is called the superhet receiver.
- ch 8 [high] Exam traps, third bullet: It says that using DSB instead of SSB doubles each slot. The slot is Bm+Bg for SSB and 2Bm+Bg for DSB, so the guard band is not doubled; for a 3.1 kHz voice signal with a 0.9 kHz guard band the slots are 4 kHz and 7.1 kHz, not 8 kHz.
- ch 8 [high] Quiz Q3: The answer says SSB halves the slot width. SSB halves the message bandwidth (Bm vs 2Bm), but the slot widths are Bm+Bg and 2Bm+Bg, so the slot is not halved when the guard band is included.
- ch 8 [low] Section 3, FM stereo sentence: The wording says the sum and difference signals are placed around a pilot tone. In FM stereo the L+R sum is at baseband, the 19 kHz pilot is separate, and the L-R difference is DSB-SC around a 38 kHz subcarrier.
