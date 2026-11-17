# m-calculus-u4: free-model run

- Book: `books/common/m-calculus/m-calculus-u4.html`
- Status: ok
- Model calls so far: 28 (110,676 tokens in, 231,574 out), 4.5 minutes

## Checker

```
m-calculus-u4.html: 8 chapters, 15813 words, 9 figures, 151 KB
OK
```

## For the reviewer

- chapter 6: the figure cannot be drawn: note "look deeper" runs off the right edge; shorten it

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, first bullet of the two-path test; also the Exam traps bullet starting 'Straight lines y = mx': The paths y = mx and x = 0 pass through the origin only. The two-path test is stated for a general base point P₀ = (x₀, y₀), but these lines do not pass through P₀ unless P₀ is the origin. A student applying them at a point such as (1, 2) would use the wrong paths.
- ch 1 [low] Section 1, algebra of limits: The quotient rule f/g → L/M is stated only with M ≠ 0. It also needs g ≠ 0 on a punctured disk around P₀, otherwise f/g is not defined near the base point and the rule cannot be applied.
- ch 1 [low] Worked example 1, step 4; also the polar discussion in Section 2: The sentence 'As r → 0, the expression depends on θ' is imprecise. The expression cos θ sin θ does not contain r at all, so the value does not change with r; what depends on θ is the limiting value along the ray.
- ch 1 [low] Section 2, two-path test bullets: The bullets cover two paths with different finite values, but not the case where the one-variable limit along a single path fails to exist (for example, oscillation along that path). That alone also disproves the two-variable limit.
- ch 1 [low] Figure: The plot starts at x = 0.1 and shows only the constant values along the two paths. It does not show the approach to the origin, and the path y = 0 is called 'the x-axis' while the horizontal axis of the plot is also labelled x, which can confuse the reader.
- ch 2 [low] Quiz Q3 and Q4 (and their answers): The function is written as exy, which on a phone reads as e·x·y. A student can easily take the exponential to be a plain product and get different derivatives.
- ch 2 [low] Quiz Q1 answer: The limit is typed as 'limh→0' with no subscript, so the h→0 sits on the baseline and breaks the formula.
- ch 3 [low] Section 2, the 'Do not write dz/dx' paragraph: The reason given is muddled. When x and y both depend on t, z is a function of t alone, so dz/dx has no meaning as a partial. But along the curve the rate with respect to x is well defined and equals (dz/dt)/(dx/dt). Saying that writing dz/dx 'hides a second route and usually gives a wrong answer' can make a student think the correct formula dz/dx = f_x + f_y(dy/dx) (valid when y is a function of x) is wrong.
- ch 3 [low] Figure caption: The caption says 'at t = 1 the two partial rates add to 8', but the figure appears before Worked example 1, which is where the function z = x²y + y³ with x = t², y = t and the number 8 first appear. A reader meets a bare 8 with no context.
- ch 3 [low] Section 1, definition of ρ: Writing ρ = √(Δx² + Δy²) can be read as Δ(x²) rather than (Δx)². The same shorthand recurs in the formula box and in Quiz Q1.
- ch 4 [low] Section 2, third property paragraph: Stray character and broken notation: the text reads "give fuxvy − uyvx = (1)(2) − (1)(2) = 0". The leading "f" is a typo and the partials are not written with subscripts as elsewhere.
- ch 4 [low] Section 2, third property paragraph: "J = 0 exactly where the map loses independence, that is, where u and v are functionally related" reads as a pointwise statement, which clashes with the quiz Q7 answer that J = 0 at a single point does not make u and v dependent everywhere. A student can take away the wrong rule.
- ch 5 [low] Section 2, the boxed third-degree formula and its 'where' line: The formula is printed as 'f = f + (h f_x + k f_y) + …', so the same symbol f stands for two different things in one line: f(a + h, b + k) on the left and f(a, b) on the right. The note underneath repairs it, but a student skimming the box reads a false statement.
- ch 5 [low] Section 3, worked numbers for eˣ sin y: A wrong intermediate value is left standing inside the calculation: '(1.106/6)(0.3)³ = 0.00124? No: …'. The equals sign is followed by a false number and a question mark, which reads like an uncorrected draft note. A student copying the chain can carry 0.00124 away as the bound.
- ch 6 [high] Section 1, the f(x, y) = x² − y² example: The last sentence is broken: 'Along the y-axis f = −y² saddle point at (0, 0).' The reasoning step (that f < 0 for y ≠ 0 along the y-axis, giving a top in that direction) is missing, so a student sees two unrelated fragments and cannot follow why the point is a saddle.
- ch 6 [high] Section 2, the negative-definite case: The condition for a local maximum is truncated: 'exactly when f_xx  0; then f(a, b) is a local maximum.' The required inequalities are missing, so the stated case is wrong as printed and the D > 0 condition is lost.
- ch 6 [low] Quiz Q7: The answer calls (0, 0) 'the only critical point' but it is a corner of the square, not an interior point, which clashes with the three-stage routine that searches interior critical points separately from the boundary.
- ch 7 [high] Quiz Q4: The Lagrange equations are set up correctly (f_x = 2x = λ, f_y = 2y = 2λ, g_x = 1, g_y = 2) but then solved wrongly: the answer says 'so x = λ and y = λ, giving x = y'. From 2x = λ we get x = λ/2, and from 2y = 2λ we get y = λ, so y = 2x, not x = y. The quoted point (5/3, 5/3) is not the closest point: it gives f = 50/9 ≈ 5.56, while the true minimum is smaller.
- ch 8 [low] Section 3, angle between two surfaces: The symbol n₁ is used twice with two different meanings in one sentence. First n₁ and n₂ are the two normal vectors; then the length formula |n| = √(n₁² + n₂² + n₃²) uses n₁, n₂, n₃ as the components of one vector. A student reading quickly will think the length of n₁ is √(n₁² + n₂² + n₃²), which is meaningless.
- ch 8 [low] Figure caption: 'the gradient (2, 4, −1) is the normal' does not say which function is being differentiated, so it reads as if the gradient of z = x² + y² at (1, 2) were (2, 4, −1); the gradient of that two-variable function is (2, 4). The third component appears only for F = x² + y² − z.
