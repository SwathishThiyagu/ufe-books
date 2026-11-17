# m-calculus-u2: free-model run

- Book: `books/common/m-calculus/m-calculus-u2.html`
- Status: ok
- Model calls so far: 19 (70,646 tokens in, 142,865 out), 3.7 minutes

## Checker

```
m-calculus-u2.html: 7 chapters, 11588 words, 8 figures, 135 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3, FTC part 2 statement: The statement says only 'If F is any antiderivative of f on [a, b]' and never gives the continuity hypothesis on f, so a student may apply it to a discontinuous integrand; the quiz Q1 asks for continuity but the main statement does not.
- ch 1 [low] Section 3, net change theorem: 'For any differentiable function Q' is too loose; Q′ must be integrable (for instance continuous) on [a, b] for the formula to hold.
- ch 1 [low] Section 1, sentence after the Riemann sum: 'It overestimates where f rises and underestimates where f falls' is vague because the over- or under-estimate depends on where the sample point xᵢ* sits inside each strip, not only on whether f rises or falls.
- ch 1 [low] Exam traps, fourth bullet: The bad-notation example 'd/dx ∫ₐˣ f(x)dt' mixes the variable x with the differential dt, so the expression is not just confusing, it is meaningless; a student may copy it.
- ch 2 [low] Section 1 and Quiz Q3: Quiz Q3 integrates term by term (3x² + 2x → x³ + x² + C), but the sum rule and constant-multiple rule for integrals are never stated anywhere in the chapter. A student meeting Q3 has to assume a rule that was not taught here.
- ch 2 [low] Worked example 1, step 7: Step 6 already shows the derivative of the answer is exactly x e²ˣ. Step 7 then says 'both the derivative of the answer and x e²ˣ equal 7.389…', but those are the same function, so nothing independent is being compared. A student may think two different quantities are being checked against each other.
- ch 2 [low] Whole chapter (table, Sections 2–4, worked example, figure text): Powers are written without superscript markup: 'e2x', 'xn', 'sec2x', 'cos2x', 'x²' is fine but 'e2x' can be misread as 2·e·x, and 'xn' as x·n. The text field allows <sup>.
- ch 3 [high] Section 2, first paragraph (the ∫₁^∞ p-integral): The convergence condition is corrupted: "At R, this tends to 0 when 1−p1, giving value 1/(p−1)." The inequality is missing, so the sentence states no condition and a student cannot tell why the limit is 0. The value 1/(p−1) then appears from nowhere.
- ch 3 [high] Section 2, second paragraph (the ∫₀¹ p-integral): The condition is corrupted and contradicts the table: "∫₀¹ x^(−p) dx converges exactly when p 1 the term c^(1−p) grows." As written, the sentence both drops the inequality and reads as if p > 1 gives convergence, while the table correctly says p < 1 converges.
- ch 3 [low] Section 3, last sentence of the section: The note "Some syllabi call these improper integrals of first and second kind" repeats what Section 1 already said ("Some syllabi call these improper integrals of the first kind"), so the reader wonders whether a new meaning is being introduced.
- ch 4 [high] Section 3, first worked reduction bullet (∫₀¹ x⁴(1−x)³ dx): The denominator is wrong. Here p = 5 and q = 4, so p + q = 9 and Γ(p+q) = Γ(9) = 8!, not 7!. The stated value 1/35 is therefore incorrect; the true value is 1/280.
- ch 4 [low] Quiz Q7: The question asks the student to identify "both mistakes", but the answer correctly lists three separate shift errors (Γ(2), Γ(3) and Γ(5)). The count in the question does not match the answer.
- ch 4 [low] Lead: "Two integrals, both improper" is not always true. The beta integral is a proper integral of a bounded integrand when p ≥ 1 and q ≥ 1 (for example p = 2, q = 3); it is improper only when p < 1 or q < 1.
- ch 4 [low] Section 2, symmetry proof: "the limits 0 to 1 swap back to 0 to 1" hides the actual step. After s = 1 − t the limits become 1 to 0, and it is the minus sign from dt that flips them back to 0 to 1. As written, a student cannot see where the minus sign goes.
- ch 5 [low] Quiz Q3: The integral in the answer is garbled: it reads 'On 001(√x−x)dx' instead of an integral from 0 to 1. The exponent in '2x3/2/3' is also not marked as a power, so a student cannot tell whether it is 2x·3/2/3 or 2x^(3/2)/3. The final value 1/6 is correct.
- ch 5 [low] Section 2, last sentence: The sentence 'use it when vertical slices would split' does not apply to the example x=y² and x=4. That region is not split by vertical slices; a vertical slice simply has top √x and bottom −√x, so horizontal slices are preferred because the data gives x as a function of y, not because vertical slicing splits the region.
- ch 6 [low] Section 1, first paragraph: The sentence 'A smooth curve has a continuous derivative, so it has no sharp corner' is not reliable. A curve whose derivative is continuous can still vanish at a point and have a cusp, for example the astroid x=cos³t, y=sin³t. Under the chapter's own definition such a curve counts as smooth, yet it has sharp points.
- ch 6 [low] Exam traps, last bullet: 'dx, dy, dt and L must use one consistent length unit' is wrong when the parameter t is not a length (for example t is time in seconds). Then dt has the unit of the parameter, and the length comes out right because dx/dt has units of length per unit t.
- ch 6 [low] Quiz Q7: The answer says area adds rectangle heights giving f(x)Δx. For a curve below the x-axis f is negative, and the area between the curve and the x-axis is built from |f(x)|Δx, not f(x)Δx.
- ch 7 [low] Worked example 2, steps 1–3: dy/dx = 1/(2√x) blows up at x = 0, so the surface integral is improper. The steps treat it as an ordinary definite integral and never mention this; a student who substitutes x = 0 first will get infinity and stop.
- ch 7 [low] Exam traps, first bullet: "π(∫R)² is a different, wrong number" is ambiguous — it is not clear whether the square is inside or outside the integral, and the bracket (∫R)² has no dx.
- ch 7 [low] Quiz Q4 answer: The hint u = 1+4x² does not finish the problem: it turns the integral into (1/16)∫₁⁵ √(u²−u) du, which still needs completing the square and a secant substitution. As written it sends students into a harder integral than the standard one.
- ch 7 [low] Section 2, shell formula: The shell formula is stated with conditions missing: x must be the non-negative distance from the axis to the shell, f(x) must be the height measured from the axis, and for a region between two curves the height is the difference. Also a and b are not defined in this formula's line.
