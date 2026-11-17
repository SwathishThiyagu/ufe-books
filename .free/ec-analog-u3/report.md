# ec-analog-u3: free-model run

- Book: `books/ece/ec-analog/ec-analog-u3.html`
- Status: ok
- Model calls so far: 29 (121,461 tokens in, 255,343 out), 6.9 minutes

## Checker

```
ec-analog-u3.html: 8 chapters, 15164 words, 9 figures, 161 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Worked example 1, step 4 (and answer): The gain at 10 Hz is found from the dominant corner alone, 100×(10/31.8)/√(1+(10/31.8)²) = 30.0. Section 2 of the chapter itself says every capacitor multiplies the gain by its high-pass factor, and at 10 Hz the input coupling capacitor is far from a short (its factor is 0.532, not 1). Ignoring it makes the stated gain roughly twice the correct value; a student who follows the chapter's own rule will get a different number and lose marks either way.
- ch 1 [low] Worked example 1, step 3: Two problems. (a) 'Overall fL ≈ 31.8 Hz' is the largest corner, but with corners only a factor of two apart the combined response is 0.63 (−4.0 dB) at 31.8 Hz, not 0.707; the true overall fL is about 38 Hz, roughly 20% higher. (b) The clause 'while the input capacitor at 15.9 Hz is already above its corner' is garbled — it is the frequency 31.8 Hz that is above the input corner, not the capacitor.
- ch 1 [low] Lead: IF strips do not carry signals 'down to tens of hertz'. An IF amplifier is a fixed-frequency bandpass stage (455 kHz in AM receivers, 10.7 MHz in FM), so low-frequency response is not what limits it. The example misleads.
- ch 1 [low] Lead: 'bypass capacitors set the emitter or source voltage' is vague and can be read as saying the bypass capacitor fixes the DC emitter voltage. The bias is set by the resistors; the bypass capacitor only holds the emitter (or source) at AC ground.
- ch 1 [low] Quiz Q5: Answering 'about 75 Hz' takes the largest corner as the overall fL. With corners at 12, 40 and 75 Hz, the gains at 75 Hz already lose about 1.2 dB, so the combined −3 dB point is noticeably higher, near 90 Hz. The one-line answer hides that error.
- ch 2 [low] Section 3 (why the CE stage is slow): The arithmetic does not support the stated result. "Hundreds of pF times a few kΩ" gives about 1–2 μs, so 1/(2πτ) is roughly 100–160 kHz, which is in the hundreds of kHz, not "tens of kHz". A student who checks the numbers will think the estimate is wrong.
- ch 2 [low] Section 3 (common-base sentence): "Only a few pF load the input" understates the CB input. In CB the input is the emitter and Cπ (10–200 pF by this chapter's own numbers) sits from emitter to ground, so it does load the input. What CB avoids is the Miller multiplication of Cμ, not capacitive loading altogether.
- ch 2 [low] Figure spec: The edge from C_M to the gain stage labelled "drives" makes C_M look like a series element carrying the signal into the amplifier. C_M is a shunt capacitance at the input node; the amplifier input is that same node. A student can misread the block diagram.
- ch 3 [low] Section 2: Calling f_T the 'cut-off frequency' contradicts the very next sentence, which reserves the −3 dB point (the usual meaning of cut-off frequency) for f_p. A student can carry the wrong label into the exam.
- ch 3 [low] Figure and its caption: The plotted curve is the asymptote A = 2×10⁶/f, so below the pole it exceeds the low-frequency gain: at 2 Hz it shows a gain of 10⁶, five times A₀ = 2×10⁵. The caption's 'at 10 Hz it is still at 2×10⁵, the low-frequency gain A₀' also conflicts with the formula in Section 1, which gives 0.707A₀ = 1.41×10⁵ at f = f_p.
- ch 4 [low] Section 2, emitter peaking paragraph: The bypass capacitor is called C<sub>E</sub>, but CE is used everywhere else in the chapter as the short form of common emitter (CE stage, CE-CE, CC-CE). A student can read 'CE across RE' as a transistor, not a capacitor. R<sub>E</sub> also sits next to R, which Section 3 uses for the coil's series resistance.
- ch 4 [low] Worked example 1 (steps 1–5) and Quiz Q3 answer: Powers of ten are printed with a plain minus and no superscript: '100×10−6 H', '1.0×10−14 s2', '1.591549×106 Hz'. On a phone this reads as a subtraction, and 's2' is not a unit.
- ch 4 [low] Section 1, second paragraph: 'Stop the internal capacitances from forming a low-frequency pole' can be misread as a pole near the lower cut-off f<sub>L</sub>. The intended meaning is a pole at a low frequency, which drags the upper cut-off f<sub>H</sub> down.
- ch 4 [low] Section 2, Darlington paragraph: 'The current gain is β1β2' is stated as exact. The exact value is β1β2 + β1 + β2.
- ch 4 [low] Beyond: 'Isolates the input matching network from the local oscillator' describes the effect loosely. The cascode gives reverse isolation from output back to input, which is what limits signal leaking back from the mixer and the local-oscillator port into the input match.
- ch 4 [low] Exam traps, first bullet: The wording is easy to misread as 'never use Q = f<sub>0</sub>/BW'. The real point is that BW is not given in such a question, so the formula would be circular.
- ch 5 [high] Quiz Q7: The answer contradicts itself: 'Halving the peak voltage halves P_out to one quarter of its maximum'. Halving the peak voltage quarters the power, since P_out goes as V_p². The final figure of about 6% is right, but the sentence in between teaches the wrong step.
- ch 5 [low] Figure table (class D row): The distortion column gives 'high' for class D. A class D stage switches, and with a proper output filter its distortion is low; its real drawbacks are EMI and the output filter, not distortion.
- ch 5 [low] Figure table (class B row): The distortion cell reads 'yes'. A distortion column should hold a distortion description, not a yes/no mark; only the caption explains it.
- ch 5 [low] Figure caption / table column: The caption calls the middle column 'maximum conversion efficiency', but the class AB entry (60%) and class C entry (85%) are typical values. Class AB can reach 78.5% at zero bias and class C efficiency keeps rising as the conduction angle shrinks. The label does not match the numbers.
- ch 5 [low] Section 3, class C: 'A tuned load rings at the signal frequency and restores the sine ... at the cost of heavy distortion' reads as a contradiction. The tuned tank removes the harmonics, so the output is close to a sine; the real limitation is that class C is nonlinear and only works for constant-envelope signals.
- ch 6 [low] Section 3 and Quiz Q2: The text says the output has "a flat step of about ±0.7 V around zero". The ±0.7 V figure is the width of the input dead band, not a step in the output. While |Vin| < 0.7 V the output does not step by 0.7 V; it stays flat at 0 V (held there by the load), so the input must move through a band about 1.4 V wide before either device conducts. A student can read the present wording as the output jumping by 0.7 V.
- ch 6 [low] Section 3, V_BE multiplier: The formula V_BB = V_BE(1 + R1/R2) is given but R1 and R2 are never placed in the circuit, so a student cannot tell which resistor is which or check the formula.
- ch 6 [low] Section 1, OTL naming: Calling the split-supply, direct-coupled complementary stage OTL is loose. Many textbooks use OTL for the single-supply, capacitor-coupled output (the case the chapter mentions a sentence later) and call the dual-supply direct-coupled version OCL (output capacitor-less).
- ch 6 [low] Quiz Q6: The answer gives emitter resistors as one of "two fixes" for the zero-crossing kink. Emitter resistors do not remove the dead band; they stabilise the quiescent current that the class AB bias sets. Presenting them as a cure for the kink blurs cause and cure.
- ch 6 [low] Exam traps, rms trap: "The formula already handles the rms conversion" is unclear. The factor 2 in V²/(2RL) is the peak-to-rms step, so the sentence needs to say plainly which voltage form each formula wants.
- ch 7 [high] Section 1, last paragraph of the class C discussion: The text says 'the output is rich in harmonics' immediately after explaining that the tank gives 'a voltage across it [that] is almost a pure sine at f₀'. These two statements contradict each other, and a student can end up believing the sine is not really restored. The harmonic-rich waveform is the transistor current (a narrow pulse train), not the tuned output; the tank suppresses those harmonics, leaving only a small residual.
- ch 7 [low] Lead: 'Class C and class D both raise efficiency by making the transistor conduct for less time than class A does' gives the wrong reason for class D. A class D device may conduct for most of the cycle; its low loss comes from having almost zero voltage across it while it conducts, not from short conduction time.
- ch 7 [low] Section 1, efficiency comparison: 'a class A stage sits near 25 % to 30 %' quotes an upper figure above the standard maximum. A series-fed class A stage has a maximum ideal efficiency of 25 % (50 % only with transformer coupling), so '30 %' overstates it.
- ch 8 [low] Section 2, second sentence: The sentence repeats itself: "THD stands for total harmonic distortion. Some syllabi call it total harmonic distortion; the words are the same." The second sentence adds nothing and a student will think a word was misprinted or that two different quantities exist.
- ch 8 [low] Figure, item notes: The figure notes use Tc and Ts, but the chapter never defines them; only Tj and Ta are defined. A student may not know what the case and sink temperatures are called.
