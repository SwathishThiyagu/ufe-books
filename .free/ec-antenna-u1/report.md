# ec-antenna-u1: free-model run

- Book: `books/ece/ec-antenna/ec-antenna-u1.html`
- Status: ok
- Model calls so far: 29 (116,978 tokens in, 281,178 out), 7.6 minutes

## Checker

```
ec-antenna-u1.html: 8 chapters, 15676 words, 9 figures, 155 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, current equation: "The matching current is I(z) = ..." uses the word 'matching', which in RF already means impedance matching; a student may think the equation applies only to a matched line.
- ch 1 [low] Section 3, power and efficiency: P⁺ = |V⁺|²/(2Z0) is correct only if |V⁺| is the peak amplitude of the phasor; with an RMS phasor the answer is twice too small. The chapter never says which convention it uses. The efficiency η = e^(−2αl) also assumes a matched load, which is not stated.
- ch 1 [low] Exam traps, last trap but one: The clause "which then makes the two waves add instead of travelling opposite ways" is garbled: a sign error makes the forward and backward current terms add, it does not stop the waves travelling in opposite directions.
- ch 1 [low] Quiz Q6: Saying "When R/L > G/C the attenuation rises with frequency" implies that attenuation does not rise with frequency otherwise. For a passive line α increases with frequency for every practical ratio of R/L to G/C; the comparison R/L against G/C decides whether conductor loss or dielectric loss dominates, not whether α rises.
- ch 2 [low] Section 2, the sentence giving V(d) and I(d): Phase reference is self-contradictory. The chapter defines Γ(d) = ΓL e^(−j2βd) with d measured from the load toward the generator, which is the standard form. But with that convention the forward wave must be written e^(+jβd), so the total voltage is V(d) = V+ e^(jβd)[1 + Γ(d)]. Writing V(d) = V+ e^(−jβd)[1 + Γ(d)] makes the reflected term travel in the same direction as the forward term. The magnitude formulas later in the section are correct, so nothing numerical changes, but a student who copies the total-voltage expression gets the phase wrong.
- ch 2 [low] Section 3, the sentence 'Reflection loss is the same decibel measure in many texts': This invites confusion and clashes with the chapter's own exam trap. Many texts use 'reflection loss' for the mismatch loss, −10 log10(1 − |Γ|²) dB, not for −20 log10|Γ| dB. A student may carry the wrong meaning into the exam.
- ch 2 [low] Section 3, the power formula P+ = |V+|²/(2Z0): The factor 2 is correct only if |V+| is the peak amplitude. The chapter calls it 'forward voltage amplitude' without saying peak; if a student takes |V+| as an RMS value the power formula is wrong by a factor of 2.
- ch 3 [high] Section 4, loss and power: The round-trip attenuation of power is given as e^(−2αd). The forward wave travels d and the reflected wave travels another d, so amplitude falls by e^(−α·2d) = e^(−2αd) and power falls by the square of that, e^(−4αd). The sentence also clashes with the correct one-way result PL = Pin e^(−2αd) given two lines later.
- ch 3 [high] Section 2, open and short lines: "Their reactance changes with frequency, so they work as stubs over a band, not at one point only" inverts the cause and effect. Because the reactance changes with frequency, a stub holds its designed value only near the design frequency; stubs are narrowband, not broadband.
- ch 3 [low] Exam traps, first bullet: The trap presents degrees inside tan as an error, but tan of an angle is the same number either way: tan 45° = tan(π/4) = 1. The real error is a calculator left in the wrong mode, for example entering tan(0.785) in degree mode and getting about 0.0139. As written, a student gets a false rule.
- ch 4 [high] Section 3, bandwidth paragraph: The stated bandwidth for a 2:1 quarter-wave transformer is wrong. With the chapter's own criterion |Γ| ≤ 0.2 (VSWR ≤ 1.5), a single-section transformer with ZL/Z0 = 2 matches from about 0.61f0 to 1.39f0, i.e. about 78% bandwidth, not 'a few percent to roughly ten percent'.
- ch 4 [high] Section 1, 'The match is exact only at f0' (also lead/figure): The ideal quarter-wave section also gives Zin = Z0 at odd multiples 3f0, 5f0, ... because βl = (2n+1)π/2 and tan βl tends to infinity there. So 'only at f0' and 'tan βl is finite away from f0' are false.
- ch 4 [low] Figure: The figure says the section is 2.08 cm at 2.4 GHz, but that length assumes vp = 2×10⁸ m/s. The figure does not state vp, so the number is not defined; in air the quarter-wave length at 2.4 GHz would be about 3.13 cm.
- ch 4 [low] Section 2, after 'Choose Bs = −B(d)': 'The line then sees Y0, which is Z0' mixes admittance and impedance: Y0 is 1/Z0, not Z0.
- ch 4 [low] Section 2, shunt-stub procedure: The procedure presents d as unique. In general there are two intersections where Re[Y(d)] = Y0 within λ/2, and the designer must choose one.
- ch 4 [low] Exam traps, first bullet: 'Or the design must use a complex load formula' is misleading; a single real-Z0 λ/4 section cannot match an arbitrary complex load to a real Z0. The standard fix is to cancel the reactance first or use another matching network.
- ch 5 [high] Section 3, final check line ('a short stub is shorter than λ/4 when it supplies positive reactance'): The check is worded for a series stub (reactance). The procedure just above is for a shunt stub, which adds susceptance, and there the rule reverses: a short-circuited shunt stub of length l < λ/4 gives B = −Y0·cot(βl) < 0, i.e. inductive (negative) susceptance. To supply positive susceptance the short stub must be longer than λ/4 (up to λ/2). A student following this check will pick the wrong stub length.
- ch 5 [low] Lead and Section 2: VSWR is used from the first paragraph but never expanded or defined, so a reader meeting the abbreviation for the first time has no full form to attach to the formula.
- ch 6 [low] Section 3 and Quiz Q6: The symbol δ is used twice with two different meanings: skin depth δ = √(2/(ωμσ)) in the same paragraph where dielectric loss is written as tan δ (δ = loss angle). A student can read them as the same quantity.
- ch 6 [low] Section 2, design steps: The loop 'guess W/h … adjust W until Z0 is close to the target' never says how to move W, so a student may adjust in the wrong direction.
- ch 7 [high] Figure caption: The caption says λg/λ0 'falls steeply toward 1 just above cutoff'. It is the opposite: at cutoff λg → ∞, so the ratio is very large just above fc and falls toward 1 only far above cutoff. The plotted curve itself starts at 7.12 near f/fc = 1.01 and reaches 1.03 at f/fc = 4, so the sentence contradicts both the formula and the plot.
- ch 7 [high] Section 1, last paragraph: 'Wall currents follow those field lines' is wrong physics: surface current density is J_s = n̂ × H, so current lines run perpendicular to the tangential magnetic field, not along the E lines drawn in cross-section. The conclusion about broad-wall seams is also misleading: for TE10 the transverse current is zero at the centre of the broad wall (x = a/2) and the current there is purely longitudinal, so a longitudinal centre seam cuts no current — which is why slotted lines and split-block guides work.
- ch 7 [low] Section 1, paragraph on cutoff: 'A waveguide is therefore a high-pass device — it passes a band of frequencies and rejects everything below' mixes two ideas; 'passes a band' suggests a band-pass response, but every mode above its own cutoff propagates without an upper limit.
- ch 7 [low] Quiz Q2 answer: 'with both boundary walls at the same potential' is loose for a hollow pipe: there is one connected conducting wall, not two walls whose potentials must be matched, and the argument depends on the whole boundary being a single equipotential.
- ch 8 [high] Worked example 1, step 6: The reasoning is wrong. Qe = 125 is four times smaller than Q0 = 500, not 'close to Q0 in size'. The resonator is heavily loaded precisely because Qe is well below Q0; the external loss dominates the internal loss. As written, a student could conclude that heavy loading happens when Qe ≈ Q0.
- ch 8 [low] Section 3, surface resistance sentence: The formula Rs = √(πfμ/σ) uses μ and σ without defining them, which breaks the chapter's own rule of defining every symbol.
