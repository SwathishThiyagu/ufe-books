# ec-control-u3: free-model run

- Book: `books/eie/ec-control/ec-control-u3.html`
- Status: ok
- Model calls so far: 21 (108,524 tokens in, 222,901 out), 8.2 minutes

## Checker

```
ec-control-u3.html: 4 chapters, 9128 words, 5 figures, 103 KB
OK
```

## For the reviewer

- chapter 4: worked example 1: the worked example states [300.0] but recomputing it gives [-0.845, -3.155, -0.845, 3.08, -2.0, 60.0, 180.0, -60.0]; fix the steps and the answer so they match the correct values

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, region list discussion of the pole at s = 0: It says a simple pole at s = 0 gives a bounded step response and that a ramp input gives t. The reverse is true for the step: with T(s) = 1/s a step input 1/s makes the pole at the origin double, so y(t) = t, which is unbounded. A ramp input then gives t²/2. The claim 'and so does a sine at the same frequency' is also wrong for a pole at the origin: a sinusoid of any nonzero frequency through 1/s is bounded. The bounded-step-but-unbounded-sinusoid behaviour belongs to a simple pair of poles at s = ±jω₀, not to a pole at s = 0.
- ch 1 [high] Quiz Q3: Both the question and the answer are built on the wrong fact that a simple pole at s = 0 passes a step input. The stated reason ('the pole contributes a constant term, so a step gives a constant output') is false: the step 1/s doubles the origin pole and gives a ramp.
- ch 1 [high] Exam traps, second trap: 'A simple pole at s = 0 passes a step input but fails a ramp, or a sine at that frequency' is wrong twice: a simple pole at s = 0 fails a step input (output is a ramp), and a sine at frequency 0 is not the resonance case. The trap should be about a simple pair at ±jω₀ only.
- ch 1 [low] Section 2, characteristic equation formula: The sentence introduces the formula as the unity-feedback case, but the formula written is the general one, 1 + G(s)H(s) = 0, not 1 + G(s) = 0.
- ch 1 [low] Section 3, last sentence: 'The pair nearest the jω axis decides the speed of the settling' ignores single real poles, and 'as dominant poles explains' is not grammatical.
- ch 1 [low] Section 4, first worked case: G(s) = 1/(s(s + 2)) has a pole at the origin, so the open loop is marginally stable, not simply unstable. The distinction matters because this chapter spends time on it.
- ch 1 [low] Quiz Q7: The Routh array has two sign changes in the first column, not one. Saying 'a sign change, so two roots lie in the right half-plane' mismatches the count with the conclusion.
- ch 2 [high] Section 2, bullet on counting sign changes: It says "Zero sign changes means every root is in the left half plane, so the system is stable." That is false when roots lie on the jω axis. A polynomial with a factor such as s² + 11 gives a row of zeros, and after the auxiliary-row replacement the first column can show no sign changes while the roots are on the imaginary axis. The chapter itself contradicts this line: at K = 66 in the worked example and in Q8 the array has no sign changes yet the system is only marginally stable and oscillates.
- ch 2 [low] Section 3, Special case 1: The sentence "If the whole row is not zero, this is the correct limiting process" is vague; a student may read it as a condition on the ε method rather than as the statement that distinguishes case 1 (one zero in the first column) from case 2 (all-zero row).
- ch 2 [low] Quiz Q6: The question calls the array "completed" and then gives a first column that contains a zero, so the wording contradicts itself; the array is not complete until the ε process is done.
- ch 2 [low] Figure: The s² row has an empty third cell while the s³ row shows an explicit 0 in the same padding position; read against worked example step 1, students may think an entry is missing rather than zero.
- ch 3 [high] Section 3, added pole: The sentence says the dominant pair moves closer to the jω axis and then that overshoot 'often falls'. Moving closer to the axis means lower damping ratio ζ, which raises overshoot. This contradicts the standard rule that an added open-loop pole pulls the locus right, lowers relative stability and makes the response more oscillatory. A student would repeat 'overshoot falls' in an exam and lose marks.
- ch 3 [low] Lead: 'The pair nearest the axis, the dominant poles' assumes dominance always comes from a complex pair. A single real pole nearest the axis is often the dominant pole, as the exam traps and Q5 themselves point out.
- ch 3 [low] Lead: Every closed-loop pole is said to carry a term e^(−σt)cos(ωt). A real pole gives a pure exponential with no cosine, and repeated poles also bring a factor t.
- ch 3 [low] Section 2, second-order approximation: The symbol K in T(s) ≈ Kωn²/(s² + 2ζωn s + ωn²) is never defined.
- ch 4 [high] section 3, 'Two small changes' paragraph (adding a pole at −6): The claim 'the crossing gain falls — the loop becomes less stable' is numerically wrong. With the extra pole the characteristic equation is s⁴ + 12s³ + 44s² + 48s + K = 0. The Routh s¹ row is 48 − 0.3K, so marginal stability comes at K = 160, higher than 48, not lower. The auxiliary equation 40s² + K = 0 gives ω = 2 rad/s at that gain. The extra pole raises the gain needed at every locus point, so the critical gain rises here.
- ch 4 [high] quiz Q6: 'the gain at which the locus crosses the jω axis rises' is wrong. With the zero at s = −1 the characteristic equation is s³ + 6s² + (8 + K)s + K = 0. The Routh s¹ row is (48 + 5K)/6, which is positive for every K > 0, so the locus never crosses the jω axis and there is no finite crossing gain.
- ch 4 [low] section 2, Rule 8: The left-hand side is labelled ∠GH, but the sums already exclude the pole p, so the left-hand side must be the departure angle contributed by p itself. Written as ∠GH the formula adds the departure angle twice and reverses the signs of the other terms.
- ch 4 [low] exam traps, fourth trap: 'the sign and size of K tell you which' is not a correct test. K is positive at both a breakaway and a break-in point, so its sign does not separate them.
- ch 4 [low] section 3, 'Two small changes' paragraph (adding a zero at −1): 'raises the gain that can be used' suggests a finite, larger crossing gain. For this system there is no jω crossing at all, so the sentence leaves the student with the wrong picture.
