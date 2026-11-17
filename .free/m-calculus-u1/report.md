# m-calculus-u1: free-model run

- Book: `books/common/m-calculus/m-calculus-u1.html`
- Status: ok
- Model calls so far: 25 (101,397 tokens in, 170,820 out), 3.9 minutes

## Checker

```
m-calculus-u1.html: 8 chapters, 11987 words, 9 figures, 149 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, rule for y = a f(b(x−h)) + k: The sentence 'A common error is to shift before scaling when the formula has b outside' describes b wrongly. In y = a f(b(x−h)) + k the factor b sits inside the argument of f, multiplying (x−h); nothing about b is 'outside'. The sentence also leaves the working order unclear: within the inside, the compression by b must come before the shift by h (shift by h first and then compress gives f(bx − h), a shift of h/b, not h); within the outside, the stretch by a must come before adding k (adding k first and then stretching gives a·f(x) + a·k). Q4 and the earlier example use the right order, but the stated rule does not say it.
- ch 1 [low] Section 2, bullet on y = a f(x): The bullet says 'vertical stretch by |a|' for every a, but when 0 < |a| < 1 the graph is squeezed toward the x-axis, that is a vertical compression, not a stretch. The next bullet correctly separates compression from stretch for b, so the two bullets are inconsistent.
- ch 2 [high] Section 1, second paragraph: The sentence defining the one-sided limits is broken: "The left limit limx→a⁻ f(x) uses x x→a⁺ f(x) uses x > a." The condition for the left limit (x < a) and the words introducing the right limit are missing, so a student cannot tell which side each notation means.
- ch 2 [high] Worked example 1, question line: The definition of the function is garbled and partly missing: "Let f(x) = x² for x x→1⁻ f(x), limx→1⁺ f(x), and f(1)." The case x ≥ 1 and the instruction to find the limits are lost, so the example cannot be followed even though the steps later use f(x) = 3 for x ≥ 1.
- ch 2 [high] Exam traps, third bullet: The bullet is cut off: "each one-sided limit uses x  a, not the value at a". The side conditions are missing, so the trap statement is meaningless as printed.
- ch 2 [low] Section 2, infinite limit paragraph: Typo: "The symbol ∞ is note a real limit value."
- ch 2 [low] Section 2 (Power law) and Section 3 (exponential): Powers are written without superscripts: "lim(fn) = (lim f)n" and "ex is continuous everywhere" read as f·n and e·x, which are different expressions.
- ch 2 [low] Section 1 and Section 2, inline limit notation: Limits in running text are printed flat as "limx→a f(x)" and "limx→∞ 1/x", so the subscript runs into the function name and is easy to misread.
- ch 3 [high] Section 2, cusp sentence: The cusp example is written as y=x2/3, which reads as the parabola y = x²/3. That function is differentiable everywhere, including x=0, so the sentence as printed gives a wrong example of a cusp.
- ch 3 [high] Section 3, chain-rule example and higher-derivative example: Exponents are not marked as superscripts, so the maths reads false: "y=(3x²+1)5, dy/dx=5(3x²+1)4·6x=30x(3x²+1)4" reads as multiplication by 5 and 4, and "the derivative of x3 is 3x2" reads as 3x·2 = 6x. A student copying this on a phone will misread the power rule.
- ch 3 [low] Figure spec: The y-axis starts at 0, but the tangent line y=6x−9 runs from −9 to 21 over the plotted x range, so the lower half of the tangent is cut off and the picture does not show the line meeting the curve cleanly for small x.
- ch 3 [low] Worked example step 5, quiz Q1, quiz Q5: The limit is written as plain "limh→0", which on a phone reads as the product lim·h·→0. The formula fields use a proper subscript, so the notation is also inconsistent.
- ch 4 [high] Quiz Q5 answer: The derivative description is broken: it reads 'The derivative is −1 for x0', so the two cases of the derivative of |x| are lost and the sentence makes no sense to a student.
- ch 4 [low] Section 1, 'Why it is true': 'Otherwise one extreme value occurs inside (a,b)' is ambiguous: in the non-constant case it is not a particular chosen extreme that lies inside, but at least one of the two extremes must.
- ch 5 [high] Worked example 1, step 5: The text says 'Since cc0.1≈1.1052<1.2', which is garbled and mathematically wrong. It does not state the correct inequality needed to justify M=1.2.
- ch 5 [high] Exam traps, fourth bullet: The statement 'It is zero only when f itself is a polynomial of degree at most n' is false. The remainder R_n(x) is zero at x=a for any function, and can be zero at other isolated points. The intended meaning is that the remainder is not identically zero.
- ch 5 [low] Throughout: Section 1, Section 3 table, worked example, quiz Q4, Q6, Q7, exam traps: Exponents are written without superscripts in several places, e.g. 'ex' for e^x, 'e0.1' for e^0.1, 'ec' for e^c, '(1+x)n' for (1+x)^n, '|x−a|n+1' for |x−a|^{n+1}, 'xn+1' for x^{n+1}. This is ambiguous on a phone screen.
- ch 5 [low] Quiz Q5 answer: The answer jumps from |R1| = |f''(c)| x²/2 to |R1| ≤ x²/2 without showing that |f''(c)| ≤ 1 for 0<c<0.1. This step is needed for a complete solution.
- ch 6 [low] Section 1 formula and Section 2 (and Q4 answer, Beyond): Every exponent is written without a superscript, so the forms read as products instead of powers. '1∞', '00', '∞0' and 'y = fg' look like 1 times infinity, 0 times 0 and f times g; the exponentiation step reads 'elimit ln y' and the Beyond formula reads 'e times h minus 1'.
- ch 6 [low] Lead: The claim that only a few universities teach this in first-year calculus is misleading. L'Hôpital's rule sits in almost every Indian first-year calculus syllabus; saying otherwise may make a student skip a standard exam topic.
- ch 6 [low] Worked example 1 step 2 and Quiz Q3: Both use L'Hôpital's rule to find limits that are themselves needed to prove the derivatives used. The derivative d/dx(sin x) = cos x is normally derived from lim(sin h/h) = 1, so using the rule on sin x/x (and on (1−cos x)/x²) is circular reasoning.
- ch 7 [high] Section 2, second derivative test statement: The sentence reads 'If f′(c)=0 and f″(c)0, c is a local minimum.' The comparison sign is missing, so the condition is meaningless, and the companion case for a local maximum is never stated at all, even though step 3 of the worked example uses it (f″(−1)=−6<0 → local maximum).
- ch 7 [low] Section 2, bullet list: The four bullets (find f′, evaluate at critical points, evaluate at endpoints, compare) start with no lead-in sentence, so the reader does not know what procedure is being described until the last bullet.
- ch 7 [low] Section 2, second derivative test: The test is stated without saying that f′ and f″ must exist at c, which is standard in textbooks and matters for functions with corners or vertical tangents.
- ch 8 [high] Section 1, the sentence after 'For y = x²': The sentence is broken: 'For y = −x², f″ = −2  2; the bending changes at x = 2.' The comparison sign is missing, the concave-down conclusion for y = −x² is lost, and the cubic example f″ = 6x − 12 has been cut out, so the sentence jumps from a parabola to 'the bending changes at x = 2' with no function named.
- ch 8 [high] Section 3, second sentence: 'If f″(c) Chapter 1.7.' is a broken sentence. The concave-down case (local maximum) and the inconclusive case f″(c) = 0 are missing, and the chapter reference dangles.
- ch 8 [high] Section 3, classification of the cubic: 'f″(1) = −6  0, so local minimum at (3, 0)' is wrong twice: the sign is missing, and f″(1) < 0 means a local maximum at (1, 4), not a minimum at (3, 0). The test at x = 3 is missing.
- ch 8 [high] Worked example 1, step 4: 'at x = 0, f″(0) = −12  0, so f is concave up on (2, ∞).' The sign is missing and the conclusion contradicts the value: f″(0) = −12 < 0 means concave down on (−∞, 2). The test at x = 3 is missing entirely.
- ch 8 [high] Worked example 1, step 6: 'For x = 1: f″(1) = −6  0, so local minimum at (3, 0)' is wrong: the sign is missing and f″(1) < 0 gives a local maximum at (1, 4). The step also skips the check at x = 3, yet the answer line reports a minimum there.
- ch 8 [high] Quiz Q3, answer: 'f″ = 0 at x = 1. f″  0 for x > 1.' The comparison sign is missing and the concave-down interval (x < 1) is never stated, although the final line claims it.
- ch 8 [low] Section 1, the x⁴ case versus the definition: The definition is stated as f″(x) > 0 at every interior point, but f″ > 0 is only a sufficient test. For f = x⁴, f″ = 12x² is zero at x = 0 while the curve is still concave up everywhere, and Section 2 uses exactly this example.
- ch 8 [low] Section 1, straight-line remark: 'A straight line has f″ = 0 and is neither concave up nor down' conflicts with the f′-increasing definition, under which a line is both concave up and concave down. Students meeting the other convention will be confused.
- ch 8 [low] Figure, aria text: The accessible label calls the curve 'the blue cubic', but the series style is 'accent', so the colour named may not match what is drawn.
