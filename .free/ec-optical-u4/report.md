# ec-optical-u4: free-model run

- Book: `books/ece/ec-optical/ec-optical-u4.html`
- Status: ok
- Model calls so far: 18 (67,739 tokens in, 167,322 out), 5.5 minutes

## Checker

```
ec-optical-u4.html: 6 chapters, 10642 words, 7 figures, 120 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1, answer line: The answer line says photon rate ≈ 4.28 × 10¹² s⁻¹, but step 2 computes and states 4.27 × 10¹² s⁻¹. A student checking the arithmetic will think one of the two numbers is wrong.
- ch 1 [low] Section 2, hard ceiling statement and exam trap 3: The chapter says R ≤ λ/1.24 A/W is a hard ceiling and calls pushing R above it a mistake. That is true only for the primary (unity-gain) responsivity defined here. An avalanche photodiode multiplies the primary current by gain M, so its measured external responsivity Mηλ/1.24 does exceed the ceiling. As written, the sentence and the trap read as if no detector can ever show R above λ/1.24.
- ch 1 [low] Section 1, second paragraph: 'Facet reflection loses a fraction ρ' uses laser terminology. In a photodiode the light enters through the illuminated surface or window, not a laser facet; the term can confuse a student meeting 'facet' for the first time here.
- ch 1 [low] Section 1 versus Worked example 1, step 4: The formula block gives q = 1.6 × 10⁻¹⁹ C but step 4 uses q = 1.602 × 10⁻¹⁹ C. Two values for the same constant in one chapter invite an error in the exam.
- ch 2 [low] Section 2, sentence about typical i-layer widths ("Typical values are a few micrometres to about ten micrometres..."): This width range is typical for InGaAs at 1.3–1.55 µm, where α is about 10⁴ cm⁻¹. Silicon at 0.85 µm has a much smaller absorption coefficient (about 10³ cm⁻¹), so a 10 µm i layer absorbs only roughly half the light; it cannot give η near 1. A student could wrongly infer that a 10 µm Si PIN is efficient.
- ch 2 [low] Worked example 1, step 3 and answer: The computed external quantum efficiency η = 0.952 at 1.55 µm corresponds to a responsivity of about 1.2 A/W (R = ηλ/1.24). Section 2 quotes a typical InGaAs responsivity of about 0.9 A/W. The two numbers are not wrong individually, but the mismatch can confuse a student who converts between them.
- ch 2 [low] Section 3, "The smaller ... controls the diode" sentence and Worked example 1 step 8: The overall 3-dB bandwidth is not exactly the smaller of ft and fRC. The two limits combine, so the actual bandwidth is lower than either one. Calling the smaller limit the one that "controls" is a rule of thumb that can overestimate performance.
- ch 2 [low] Section 1, "A photon with energy hν at least the bandgap Eg..." and "the movement is photocurrent": The wording is grammatically incomplete and slightly unclear for second-language readers.
- ch 3 [low] Section 2 and worked example 1, step 5: The symbol on the left side of the shot-noise formula is missing: the text reads '_shot = 2q I_ph M² F(M) B' and ' = 2q I_ph M² F B'. A student sees a formula with no quantity on the left and cannot tell what is being computed.
- ch 3 [low] worked example 1, step 7: The result is called simply 'SNR', but only shot noise was included; receiver thermal noise is ignored, and at M = 10 with a 1 GHz bandwidth thermal noise is usually larger than 108 nA. A student may carry away the wrong idea that this is the total SNR of an APD receiver.
- ch 4 [high] Section 2 (dark current paragraph) and Quiz Q7: It says both parts of the dark current are multiplied by M in an APD. Standard photodiode theory splits dark current into a bulk part, which does see the avalanche gain, and a surface-leakage part, which does not see the gain because it bypasses the multiplication region. The quiz answer repeats the same wrong claim, so a student would lose marks and would also over-estimate APD noise.
- ch 4 [low] Section 2 (NEP formula) and Quiz Q6: The formula gives σrms the unit of amperes, but NEP is then said to be in W/√Hz. With σrms in A, σrms/R comes out in W, not W/√Hz. The unit is right only if the noise current is a spectral density in A/√Hz, that is, noise per 1 Hz of bandwidth.
- ch 4 [low] Figure (SNR out node): The note on the output node reads 'Iph / σ', an amplitude ratio, but the text defines SNR as the power ratio Iph²/σ². A student may copy the wrong ratio into the exam.
- ch 4 [low] Section 2, first line: The total noise is written 'σ² = ish2 + ith2', with plain digits instead of superscripts and without the subscript markup used in the rest of the chapter. It reads like a different quantity from ish² and ith².
- ch 5 [low] Section 1, low-pass filter bullet: "Its bandwidth is set near the bit rate" is misleading. In receiver design the post-detection filter bandwidth is normally taken as roughly half the bit rate (Nyquist) up to about 0.7B; a filter as wide as B passes much more noise and costs sensitivity. A student may read this as 'filter bandwidth = B'.
- ch 5 [low] Section 2, table row 'Low impedance': The noise entry 'about 4kT/R_L' has no units and gives a mean-square spectral density, while the transimpedance text two paragraphs later gives the rms value √(4kT/R_f). The same quantity appears in two different forms, which confuses students comparing the rows.
- ch 5 [low] Section 3, derivation paragraph before the P ≈ Qσ/R formula: 'The signal photocurrent is then about Qσ' is loose. The on-level photocurrent is 2Qσ if the off-level is taken as zero and the levels are 2Qσ apart; Qσ is the average (midpoint) photocurrent, which is what the formula P ≈ Qσ/R actually uses.
- ch 5 [low] Section 3, practical PIN sensitivity sentence: The range '−25 to −40 dBm at a few hundred Mbit/s' is optimistic at the low end; around −40 dBm is reached by low-capacitance high-impedance front ends at much lower bit rates, not at a few hundred Mbit/s.
- ch 5 [low] Quiz Q5: 'The thermal noise current falls by √2' can be read as 'falls by an amount √2' instead of 'falls by a factor of √2'.
- ch 6 [high] Section 3, BER floor sentence: APD excess noise is listed as a cause of a BER floor. In standard treatments APD excess noise is a signal-dependent multiplicative noise that inflates σ₁ and σ₀ (and shifts the optimum threshold); it does not flatten the BER curve, because more signal still improves the error rate. Floors come from non-Gaussian disturbances such as interference, modal noise, mode-partition noise or timing jitter with pattern effects. Listing APD excess noise here also contradicts the exam trap that treats APD noise as unequal σ₁, σ₀.
- ch 6 [low] Worked example 1: The data use equal noise currents, σ₁ = σ₀ = 0.075 µA, while I₁ = 1.0 µA and I₀ = 0.10 µA, yet the example calls the noise shot-limited. Shot noise gives σ ∝ √I, so with these means σ₁/σ₀ = √10 ≈ 3.2, not 1.
- ch 6 [low] Lead: 'Q turns into BER, links to the eye diagram, and measures the extra optical power needed to repair a degraded receiver' is garbled: Q does not measure power. The power penalty, computed from Q, is what expresses extra optical power.
- ch 6 [low] Section 1, after the Q formula: 'Q is dimensionless' is stated twice, once in the formula note and again in 'Q is dimensionless. Large Q means...'. A student may look for a difference between the two statements.
- ch 6 [low] Section 2, eye diagram paragraph: 'The vertical opening at the sampling instant is I₁−I₀ minus noise margins' muddles two ideas. The eye opening is I₁−I₀; the noise margins are what must fit inside it for a given Q.
- ch 6 [low] Figure and its caption text: The plotted curve uses the large-Q approximation log10(e^(−Q²/2)/(√(2π)Q)) over the whole range Q = 2 to 8, but the text says the approximation is only good for Q above about 3. At Q = 2 the plot shows log10 BER = −1.57 while the exact value is 2.3×10⁻², that is −1.64.
