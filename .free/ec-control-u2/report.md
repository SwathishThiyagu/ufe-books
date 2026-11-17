# ec-control-u2: free-model run

- Book: `books/eie/ec-control/ec-control-u2.html`
- Status: ok
- Model calls so far: 28 (137,121 tokens in, 236,755 out), 5.7 minutes

## Checker

```
ec-control-u2.html: 7 chapters, 13620 words, 8 figures, 148 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, formula block: The transform integral is printed as '∫₀∞ f(t)e−stdt'. The exponent is not raised, so a student reads it as e minus s times t times dt instead of e raised to −st.
- ch 1 [low] Section 2, last sentence: 'A is the amplitude or strength, in the same units as the signal' is true only for the step. For A·t·1(t), A is the slope (signal units per second); for A·(t²/2)·1(t), A is an acceleration-like constant (signal units per second squared); for A·δ(t), A is area (signal units times seconds). A student may write the wrong units in an answer.
- ch 2 [high] Section 1, definitions of z and p: Writing G(s)=K(s+z₁)(s+z₂)…/[sᴺ(s+p₁)(s+p₂)…], the text then says z₁, z₂, … are 'zeros, values of s that make G(s)=0' and p₁, p₂, … are 'values of s that make the denominator zero'. With the factor (s+z₁) the zero sits at s = −z₁ and the pole at s = −p₁, so z and p are magnitudes, not locations. This contradicts the worked example, which correctly says 'zero at s = −3' from (s+3), and step 5 'pole at s = −1' from (s+1). A student will read z₁ = 3 as a zero at s = +3.
- ch 2 [low] Section 1, non-unity feedback paragraph, and Quiz Q6: 'Reduce the block diagram to one equivalent forward block Geq(s) with unity negative feedback' is not defined and does not give the standard answer. For G in the forward path and H in the feedback path the error is E(s) = R(s)/[1 + G(s)H(s)], so the counts come from the loop gain G(s)H(s). Block-diagram reduction to a true unity-feedback forward block gives a different Geq = G/(1 + GH − G), and its origin-pole count can differ from the loop-gain count.
- ch 2 [low] Section 1 and Section 2 formulas: The factor is written 'sN(s+p₁)(s+p₂)…' and 'sN(1+sTa)(1+sTb)…'. A phone reader sees the letters s and N side by side and can read it as a product s × N or as a variable named sN, not as s raised to the power N.
- ch 2 [low] Section 3, first paragraph: 'Adding an integrator in a PI controller raises type by one and removes steady-state error to a step' is true only when the plant was type 0. On an already type-1 plant the step error is already zero, and adding the integral action removes the ramp error instead. As written it reads like a general rule.
- ch 3 [high] Section 1 (One pole, one time constant): "The same system can be written K/(s + a) with a = 1/τ" is not equal to K/(1 + τs). Dividing the denominator by τ also divides the numerator by τ, so the constant in front changes. As written, a student will copy a form that gives the wrong gain.
- ch 3 [high] Quiz Q7: "The exact 2% settling time is 4τ" is a wrong number stated as exact. At 4τ the output is 98.2% of final, an error of 1.8%, which is inside the 2% band; the exact 2% time is τ ln 50 ≈ 3.9τ, not 4τ.
- ch 3 [low] Section 2 (ramp paragraph): "So τ is a time delay, not a vertical offset in seconds" mixes two different quantities. A delay has units of seconds; a vertical offset has units of output. The sentence as written is easy to misread.
- ch 3 [low] Section 1 (initial-condition response), Worked example step 2, Quiz Q6 answer, Quiz Q7 answer: Several exponents are written without a superscript, for example "c₀e−t/τ", "10(1 − e−t/2)", "4e−2t". On a phone screen these read as e minus t over τ, not e to the power minus t over τ.
- ch 3 [low] Section 3, last sentence: "Some syllabi call the step curve the transient response" is loose. Transient response means the whole time-varying part of any response (step, ramp or impulse), not the step curve only. A student may take the two as synonyms.
- ch 4 [high] Beyond: The text ties ζ ≈ 0.7 to 'quarter-amplitude damping'. Quarter-amplitude damping means each successive peak is a quarter of the previous one, which corresponds to a logarithmic decrement of ln 4 ≈ 1.386 and ζ ≈ 0.22, not 0.7. Students will repeat the wrong number as a fact.
- ch 4 [high] Quiz Q2: The answer is broken: 'ζ = 0 undamped; 0  1 overdamped.' The underdamped, critically damped and overdamped ranges have disappeared, so the answer does not list four classes or their ranges as the question asks.
- ch 4 [low] Section 3: θ is defined as an angle 'in radians', but the next sentence switches to degrees ('a pole at 45°, ζ = cos 45° = 0.707'). Mixing the two units in one passage invites the very degree-mode calculator error the exam traps warn about.
- ch 4 [low] Section 1: 'Any second-order transfer function without zeros then falls into one template' is not true as written: normalising the s² coefficient leaves a numerator equal to ωn² only when the DC gain is 1. The correction appears a paragraph later, but the claim itself is too strong.
- ch 5 [high] Section 1, definition of settling time ts: The definition says ts is 'the last time the response leaves a band of ±2% or ±5%', then adds 'After ts it stays inside'. These two halves contradict each other. For the chapter's own case (ζ = 0.5, ωn = 1 rad/s) the response leaves the 2% band for the last time near 6.55 s, dips to about 0.973, and only re-enters near 8 s. So the stated definition gives about 6.55 s, which clashes with the formula ts ≈ 4/(ζωn) = 8 s, the worked example (ts = 2 s), and the figure caption ('enters that band for the last time near 8 s'). Standard textbooks define ts as the time to reach and stay within the band.
- ch 5 [high] Worked example 1 and Quiz Q5: Both call the given transfer function the forward path of a 'unity-feedback system'. With unity feedback the closed-loop function is G/(1+G): for G = 16/(s²+4s+16) it is 16/(s²+4s+32), giving ωn = √32 = 5.657 rad/s and ζ = 0.354, not the ωn = 4, ζ = 0.5 used in the solution. A careful student who follows the words gets different numbers from the printed answer. The standard-form formulas apply to the closed-loop transfer function, so the wording is wrong even though the arithmetic matches the intended closed-loop function.
- ch 5 [low] Section 1, list of assumptions: The assumption list (unit step, unity DC gain, no zeros, 0<ζ<1) leaves out zero initial conditions, which every one of these formulas needs.
- ch 6 [high] Section 2, formula note on input scaling (repeated in Exam traps, fourth bullet): The scaling statement for the parabola is wrong by a factor of 2. The chapter defines the unit parabola as R(s) = 1/s³ (i.e. r(t) = t²/2), so a parabola r(t) = A t²/2 has R(s) = A/s³ and ess = lim s→0 s(A/s³)/(1 + G) = A/lim s²G = A/Ka, not 2A/Ka. The same wrong factor is repeated in the exam trap.
- ch 6 [high] Quiz Q7 answer: The last sentence 'the error measured at the output differs by the factor 1/H' is false. With G = 50/(s+5), H = 2, the comparator error is 1/21 ≈ 0.0476, but the output error R − C is not E/H: C(∞) = G(0)·E = 10/21 ≈ 0.476, so R − C = 1 − 10/21 = 11/21 ≈ 0.524. Dividing E by H gives 0.0238, which matches neither. For non-unity feedback R − C = R(1 + GH − G)/(1 + GH), which has no simple 1/H factor.
- ch 6 [low] Worked examples 1 and 2, 'output:' blocks: Bare numbers (0.0 / 10.0 / 0.1 and 10.0 / 0.4545…) appear with no code and no labels, so the reader cannot tell which quantity each line is. In example 1 the parabola error is also missing from the block.
- ch 7 [high] Section 1, after the generalized error series formula: "It gives the whole error, transient included, while the series converges" is technically wrong and contradicts Quiz Q7. The term-by-term inversion of M(s) reproduces only the forced (steady-state) part of the error; the natural response from the closed-loop poles drops out. Example: M(s) = 1/(1 + Ts) with a step input gives the series answer 1, while the true error is 1 − e^(−t/T).
- ch 7 [high] Section 3, last bullet before the figure: "A step input has an infinite derivative at t = 0, so use C₀ and the static constants for it" gives a wrong reason. The derivative of a step is zero for t > 0 (an impulse at t = 0), so the higher terms vanish; the series does not break down. The wording also suggests the series cannot be used for a step at all.
- ch 7 [low] Worked example 1, step 3: "u² = 0.01s² (its next term is s³)" is loose: the next term of u² is 0.01s³, not s³. A student may read it as the whole coefficient being 1.
