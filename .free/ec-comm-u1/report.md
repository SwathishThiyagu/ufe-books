# ec-comm-u1: free-model run

- Book: `books/ece/ec-comm/ec-comm-u1.html`
- Status: ok
- Model calls so far: 24 (105,436 tokens in, 247,961 out), 7.1 minutes

## Checker

```
ec-comm-u1.html: 7 chapters, 14757 words, 8 figures, 154 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3, first bullet (antenna size): The speed of light is written as 'c = 3×108 m/s'. As printed this reads as three hundred and eight, not 3×10⁸. The worked example two paragraphs later writes 3×10⁸ correctly, so the two forms disagree.
- ch 1 [low] Quiz Q1: The answer lists six blocks (source, transducer, transmitter, channel, receiver, destination), but the figure and Section 1 describe five blocks with the transducer sitting inside the source ('The source produces the message. The transducer converts it...'). A student copying the Q1 answer will draw a chain that does not match the figure.
- ch 1 [low] Quiz Q7: 'Both need roughly the same bandwidth' is loose. The baseband cable system needs about B = 5 kHz, while AM on the carrier needs Bs ≈ 2B = 10 kHz. Saying they are roughly the same hides the factor of two that the chapter itself defines in Section 2.
- ch 1 [low] Section 3, noise and interference bullet (and the sentence after it): Bs is defined in Section 2 as the full width of the modulated spectrum, so the occupied band is fc − Bs/2 to fc + Bs/2. Writing 'everything outside fc ± Bs' doubles the rejected band and can mislead a student into drawing the filter twice as wide as the signal.
- ch 2 [high] Exam traps, trap 2: The trap contradicts the chapter's own (correct) density rule. A density of 2×10⁻³ V/Hz multiplied by a 1 Hz filter width gives exactly 2×10⁻³ V = 2 mV, so the sentence 'A value of 2×10−3 V/Hz is not 2 mV at the output of a 1 Hz filter' is false. A student who follows the instruction 'multiply by the filter width' gets 2 mV and then reads that this is wrong.
- ch 2 [high] Section 3, distortionless condition: 'A system is distortionless when every frequency gets the same gain and a delay that grows linearly with frequency' is wrong as written: in a distortionless system the time delay is the same for every frequency. What grows linearly with frequency is the phase lag in radians, θ(f) = −2πf t_d. The sentence teaches the opposite of the formula given two lines later.
- ch 2 [high] Worked example 1, step 8: The 3-dB bandwidth is quoted as 0.443/T. That number is only the offset of one half-power point from f = 0; the full 3-dB bandwidth, the width between the two half-power points, is 2 × 0.443/T = 0.886/T. Since the whole chapter insists on naming the bandwidth definition, giving the half-width as 'the 3-dB bandwidth' is a wrong number students will memorise.
- ch 2 [low] Section 4, why bother paragraph: 'Sampling x_I and x_Q needs only B samples per second' is ambiguous. Each component has bandwidth B/2, so each needs B samples per second; the two together need 2B real samples per second. As written it suggests the total is B.
- ch 2 [low] Section 2, frequency shift property: The property line shifts the spectrum by one complex exponential, but the next sentence says a carrier moves it to ±f_c. Multiplication by e^(j2πf_c t) moves the spectrum to +f_c only; the two-sided shift comes from multiplying by cos(2πf_c t). A student can carry away the wrong rule.
- ch 2 [low] Figure and caption: The plotted copy at 10 kHz peaks at 1 mV/Hz, half the 2 mV/Hz of the baseband sinc, yet the caption says the shifted copy 'keeps the same shape and width' and the aria text calls it an 'identical sinc'. The halved height is the correct result of modulation by a unit-amplitude cosine, but the caption never says so and the aria text contradicts the data.
- ch 2 [low] Whole chapter (Section 1, 2, 3, worked example 1, quizzes): Exponents and powers are typed as plain characters in the running text, so 'ej2πft', 'e−j2πf t₀', 'ejθ(f)', 'sinc(103 f)' and '2×10−3' read as multiplications (e times j2πft, 10 to the 3 times f). Several formulas in the same chapter do use <sup>, so the page looks inconsistent.
- ch 3 [high] Quiz Q2, answer: The answer text is broken: it reads "For f  0, H(f) = −j, so the spectrum is X(f) + X(f) = 2X(f)". The comparison signs are lost, and the negative-frequency half of the argument — the part that actually explains why negative frequencies cancel — is missing. A student copying this learns only half the reason and cannot see why the negative side vanishes.
- ch 3 [low] Section 3, low-pass equivalent formula: The symbol h̃(t) is defined only as "the low-pass equivalent impulse response". The chapter never states how h̃ relates to the real band-pass impulse response h(t), so the factor 1/2 in the formula cannot be checked by the reader.
- ch 3 [low] Section 1, first sentence: "Real band-pass signals have matching positive and negative frequencies" is vague; the technical property that makes the Hilbert transform work is conjugate symmetry of the spectrum.
- ch 4 [low] Section 1, first paragraph of conditioning: Typo 'Conditonal' in the sentence that introduces conditional probability; a student scanning quickly may read it as a different term.
- ch 4 [low] Section 1, independence sentence: The statement 'which makes P(A|B) = P(A)' silently assumes P(B) > 0; with P(B) = 0 the conditional is undefined.
- ch 4 [low] Section 4, CLT sentence and Exam trap 5: The CLT is stated for 'many independent random variables, each with finite mean and variance'. Finite variance alone is not sufficient in general; the standard versions also need identical distributions or a condition such as Lindeberg's on the tail sizes.
- ch 4 [low] Quiz Q7 answer: 'Gaussian variables are a special case where zero correlation does imply independence' is imprecise. The implication needs the variables to be jointly Gaussian; two variables that are each Gaussian but not jointly Gaussian can be uncorrelated and dependent.
- ch 5 [high] Figure spec, series 'Rx(τ)': The plotted autocorrelation does not match the rectangular PSD shown. The inverse transform of a two-sided PSD of height S = 1 µW/Hz over |f| ≤ B is RX(τ) = 2SB·sinc(2Bτ) = 20 mW·sin(2πτB)/(2πτB). The figure plots 20·sin(πx)/(πx) with x = τB, which is the same curve stretched by a factor of 2 in τ. Its zeros fall at τB = 1, 2, 3 instead of the correct τB = 0.5, 1.5, 2.5, and near the first zero it reads 12.7 mW at τB = 0.5 where the true value is 0.
- ch 5 [low] Section 3, first sentence: 'A random signal has no ordinary Fourier transform because each realization differs' gives the wrong reason. A single finite-energy realization can be transformed; the process itself has no transform because a stationary process is a power signal (finite average power, infinite energy), so the Fourier integral does not converge.
- ch 5 [low] Section 1, cross-correlation: 'It is not even in general: RXY(τ) is not the same as RYX(τ)' is loosely worded. RXY and RYX are different functions, but they are related by a time reversal, which the reader is not told.
- ch 5 [low] Worked example 1, output line: The output shows two bare numbers ('0.02' and '1e-06') with no labels, so the reader cannot tell that the first is the power in watts and the second the PSD height in W/Hz.
- ch 6 [low] Section 1, shot noise bullet: The symbol i in i² = 2qIB is never defined, so a student cannot tell whether it is a current, a current density or the RMS noise current. Every other symbol in the chapter is defined.
- ch 6 [low] Section 2, first sentence: The abbreviation PSD is used from the heading onwards but never expanded, even though AWGN, SNR and dBm are all spelled out.
- ch 6 [low] Section 3, Gaussian PDF formula block: 'σ² is the average noise power (in watts across 1 Ω)' mixes units: σ² is a mean-square voltage in V², which only equals a power in watts when the resistance is 1 Ω.
- ch 7 [high] Figure spec, stage notes: The notes label the stage noise figures as 'F1 = 3 dB' and 'F2 = 6 dB'. The chapter defines F as the linear noise factor (no unit) and NF as the dB value. Attaching dB to F contradicts the chapter's own definition and can make a student use 3 and 6 as linear factors in Friis.
- ch 7 [low] Section 2, equivalent noise temperature: The sentence 'The added noise power is k Te B' does not say that this is the noise power referred to the device input. For a device with gain G, the added noise at the output is G k Te B, so a student may apply k Te B at the output by mistake.
- ch 7 [low] Quiz Q5: The answer evaluates the 6 dB attenuator as Te ≈ 3 × 290 = 870 K. The exact value is (3.981 − 1) × 290 = 864.5 K; using 3 instead of 2.981 hides the exact calculation.
