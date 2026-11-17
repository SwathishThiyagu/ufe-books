# ec-control-u4: free-model run

- Book: `books/eie/ec-control/ec-control-u4.html`
- Status: ok
- Model calls so far: 23 (88,261 tokens in, 289,597 out), 9.2 minutes

## Checker

```
ec-control-u4.html: 7 chapters, 13013 words, 8 figures, 147 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, the Mr and ωr formula block: The validity note after the formula is corrupted: "where: valid for 0 r is dimensionless; ωr is in rad/s." The condition on ζ has been lost and the sentence cannot be read, so a student cannot tell when Mr and ωr may be used.
- ch 1 [high] Worked example 1: The example calls the system a unity-feedback system but then applies G(jω) directly to the reference input r(t) = 2 sin(9t). With unity feedback the output follows the closed-loop function T(s) = G/(1+G) = 100/(s² + 6s + 200), so the correct steady-state output is about 1.53 sin(9t − 24.4°), not 3.49 sin(9t − 70.6°). As written, the numbers belong to the open-loop plant.
- ch 1 [low] Section 1, formula note for y_ss: "|G(jω)| is dimensionless gain" is true only when input and output have the same units. A motor with voltage input and speed output has a gain in rad/s per volt, and the statement will mislead.
- ch 1 [low] Worked example 1, step 5: M at ω = 9 rad/s comes out as 1.747, the same number as Mr, only because 9 rad/s is close to ωr = 9.06 rad/s. A student may conclude that M equals Mr at any test frequency.
- ch 2 [high] Quiz Q7: The complex pair with ζ=0.4 and ωn=5 rad/s has real part −2 s⁻¹. The extra real pole at −0.5 s⁻¹ is closer to the imaginary axis, so by the standard dominant-pole rule the real pole is dominant, not the complex pair. Calling the complex pair dominant contradicts the definition and can mislead students.
- ch 2 [low] Section 3 and Exam traps: The text says for ζ≥0.707 there is no resonant peak and ωr has no real value. At ζ=0.707 exactly, ωr=0, which is real; the response is maximally flat and has no peak above DC. The 'no real value' wording is only correct for ζ>0.707.
- ch 3 [low] Section 2 table and worked example step 6, exam traps: Exponents and subscripts are typed as plain characters, so the quadratic factor reads (jω/ωn)2 and the phase reads −tan−1(ω), which a student can misread as multiplication or as 'tan minus one'. The same applies to log10.
- ch 3 [low] Quiz Q6: The answer gives the form K(1+s/20)/(s(1+s/2)) but never says how K is fixed, so a student may think the slope pattern alone determines the transfer function.
- ch 4 [low] Section 1, the 'where' line under the formula: The unit 'in rad/s' is attached to the gain: '|G(jω)| is the gain at frequency ω in rad/s'. Gain is not measured in rad/s; rad/s belongs to the frequency ω. A student may copy the wrong unit into an answer.
- ch 4 [low] Section 2, start of the fourth paragraph: 'For a proper system, the magnitude at ω→∞ is 0' is not true for all proper systems. A proper system with as many zeros as poles (m=n) ends at a finite non-zero magnitude; only a strictly proper system (m<n) ends at 0. The very next line uses the no-zero case, so the loose word can confuse.
- ch 5 [high] worked example 1, step 6 and answer: The comparison signs have been lost in the text, so step 6 reads "For K6 the crossing is left of −1, N=2 clockwise, and Z=2" and the answer reads "Closed-loop stability holds for 06 is unstable." As printed the sentences are meaningless, and the correct direction (K>6, not K<6) is exactly what a student must get right: for K<6 the crossing is right of −1 and N=0.
- ch 5 [high] Figure caption (and its aria text): For G(s)H(s)=6/[s(s+1)(s+2)] the branch running down to −j∞ is the positive-frequency branch: at ω=0.2 rad/s, G = −4.29 − j13.99, in the lower half-plane. The branch running up to +j∞ is the negative-frequency mirror. The caption says the reverse ("the lower branch is the negative-frequency mirror", aria: "with its mirror image below"), which will make students think the ω≥0 polar plot is the upper curve and mis-count encirclements.
- ch 5 [low] Figure: The plotted curve is not closed. The image of the small detour around s=0, a large arc of infinite radius that runs from the ω→0− end (+j∞, Re≈−4.5) through the positive real axis to the ω→0+ end (−j∞, Re≈−4.5), is missing. Without that arc the curve has no winding number, even though the count around −1 is unaffected.
- ch 6 [high] Section 1; Quiz Q3; Quiz Q5: The gain-factor formulas are missing the exponent. '106.02/20', '10GM/20' and '108/20' read literally as (106.02/20), (10*GM/20) and (108/20), not 10^(6.02/20), 10^(GM/20) and 10^(8/20); the stated equalities to 2 and 2.51 are then false.
- ch 6 [high] Section 2, Nyquist plot bullet: GM is not the geometric distance from the negative real-axis crossing to −1. For a crossing at −a (a>0), the gain margin is -20 log10(a) dB (allowable factor 1/a); the distance from the crossing to −1 is |1-a| and cannot carry the sign of GM.
- ch 6 [low] Quiz Q4: The answer writes PM = 180° − 150° for a phase of −150°, which contradicts the trap that PM = 180° + phase. The number is right only because 150° is being used as the magnitude of the lag.
- ch 6 [low] Section 1, first paragraph: A closed-loop characteristic root on the jω-axis does not by itself make the closed loop marginally stable; other closed-loop poles can still be in the right half-plane.
- ch 6 [low] Section 2, 'GM can be infinite' paragraph: 'The system still has a PM, read at its 0 dB crossing' is not always true. If the magnitude never crosses 0 dB, there is no gain crossover and PM is undefined.
- ch 7 [high] Worked example 1, prompt and step 6/answer: The chapter defines N=tan φ, but step 6 writes N=atan2(...)=−63.435° and the answer calls N the phase in degrees. This contradicts the definition and the exam trap; N is dimensionless and is not the angle itself.
- ch 7 [high] Worked example 1, step 7: The distance comparison is garbled and uses the wrong radius: it writes '0.3990.267' and compares the M=2 distance to 0.267, which is the M=4 radius, then says outside M=2. This contradicts the figure and final answer.
- ch 7 [low] Section 2, N-circle paragraph: The text says constant tan φ means constant closed-loop phase φ. Since tan has period 180°, one N contour can correspond to φ and φ+180°; the contour labels select the branch.
