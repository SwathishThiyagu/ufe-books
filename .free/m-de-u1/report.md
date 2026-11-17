# m-de-u1: free-model run

- Book: `books/common/m-de/m-de-u1.html`
- Status: ok
- Model calls so far: 33 (147,650 tokens in, 292,592 out), 6.9 minutes

## Checker

```
m-de-u1.html: 7 chapters, 13232 words, 8 figures, 137 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: series name "s" is too long; shorten it

## Reviewer notes (after any revision)

- ch 1 [high] Section 2 (degree, non-polynomial examples): The example 'ey′ = x' is written without a superscript, so it reads as e × y′ = x. That equation is polynomial in y′ (power 1) and would even be linear, so the sentence 'sin(y′) = x and ey′ = x are not polynomial in y′, so the degree is not defined' is false as printed.
- ch 1 [high] Section 4 (Clairaut's form, formula box): Calling y = px + f(p) 'an equation of degree higher than one in p' contradicts the standard definition. Clairaut's equation is first order; its degree equals the degree of f as a polynomial in p, and it may be 1 (y = xp + p) or undefined (y = xp + sin p).
- ch 1 [low] Section 2 example and Exam traps (first bullet): '(y″)1/2 = y' has no superscript, so it can be read as (y″) × 1/2 = y. The chapter uses proper superscripts elsewhere ((y′)⁴, (y′)⁵), so the slip is avoidable.
- ch 1 [low] Section 3 (linearity): 'x²y′ + cos(x)·y = ex' and the banned list entry 'ey' lose their superscripts, so they read as e·x and e·y. The linearity example then makes no point about the exponential, and the banned-list term no longer illustrates a nonlinear function of y.
- ch 1 [low] Section 3 (three bullets: y′ = f(x, y), M dx + N dy = 0, dy/dx = −M/N): This list arrives with no lead-in and interrupts the discussion of linearity; nothing tells the student these are three ways of writing a first-order ODE. The phrase 'the same equation with the sign carried across' is also vague.
- ch 2 [low] Figure (caption and spec): The figure sits inside Section 3, which is about cooling, decay and growth, and shows y = (1+x)/(1−x) several blocks before Worked example 1 derives that curve. A reader meets the curve with no idea which equation it solves, and the caption never names the equation.
- ch 2 [low] Exam traps, second trap: Saying that a constant on both sides 'creates a false extra parameter' is misleading. The two constants combine into one arbitrary constant (C₂ − C₁) when the sides are brought together, so nothing extra is created; the work is only redundant.
- ch 2 [low] Exam traps, fourth trap: The trap says x + y is not separable and belongs with the methods in 1.5, but Section 2 has just solved an equation in x + y + 1 by the substitution v = x + y + 1. A student can read the two statements as contradicting each other.
- ch 2 [low] Section 2, last paragraph, and Exam traps, fourth trap: The cross-references 'see 1.3' and 'methods in 1.5' are plain text, so on a phone the student cannot tap through to those chapters.
- ch 3 [low] Section 2, the sentence after step 4/5 list ("Step 3 is the payoff…"): The sentence says the right side "now contains x only through the 1/x on the left", but at that stage the equation is x dv/dx = f(v) − v; there is no 1/x anywhere in it. The actual reason separation works is that x survives only as the plain factor multiplying dv/dx, so dv and dx can be moved to opposite sides. As written, a student hunting for a 1/x on the left gets confused.
- ch 3 [low] Worked example 1, step 9 (and the answer line): "tan⁻¹(y/x) = θ" is true only on the branch where x > 0, because tan⁻¹ returns the principal value. For the spiral r = eᶿ this matters: at a point with, say, θ = 2 rad we have x < 0, y > 0, and then tan⁻¹(y/x) = θ − π, not θ. So the implicit form tan⁻¹(y/x) = ½ln(x² + y²) with principal arctan covers only −π/2 < θ < π/2, while θ = ln r covers the whole spiral. The step presents the two forms as identical everywhere.
- ch 3 [low] Exam traps, bullet 2 (M = x² + y, N = xy): "Forcing the substitution gives an integral you cannot do" misdescribes the failure. The substitution does not even reach an integral in v alone: with y = vx the right side still contains x (it becomes −(1 + v/x)/v), so the equation never separates. Saying the integral is merely hard suggests a better integration trick would rescue it.
- ch 3 [low] Section 1, definition of a homogeneous equation: The word "homogeneous" is used here for M dx + N dy = 0 with M, N of the same degree, while a later chapter uses the same word for a linear equation with zero right side (y′ + P(x)y = 0). Nothing in this chapter warns the student that the two meanings are different, and mixing them is a common exam error.
- ch 4 [high] Exam traps, item 4 (Rule 2 numerator order): The trap says reversing the numerator 'changes the sign of S and the integrating factor'. Reversing S gives S′ = −S, so the new factor is e^(−∫S dy) = 1/μ, the reciprocal of the old one. It is never −μ; e^(∫S dy) is always positive. A student reading this can wrongly write μ′ = −μ.
- ch 4 [low] Worked example 1, part (b), step 10 (and Quiz Q5): The integrating factor used is μ = x, which is zero at x = 0. Multiplying by a factor that vanishes can lose (or add) solution curves on the line x = 0, and the chapter says μ must be nonzero but never mentions this exception.
- ch 4 [low] Quiz Q5: Q5 repeats worked example 1(b) word for word, so it tests copying rather than applying the rule.
- ch 5 [high] Section 3, root case bullet: The equation y′ + P√y = Q does not become linear under u = √y. Substituting y = u² gives 2u u′ + P u = Q, which still contains u u′, so it is not of the form u′ + P u = Q. A student following this bullet gets stuck. The error is that the f′(y) factor required by the template f′(y)y′ + P f(y) = Q has been left out of the stated equation.
- ch 5 [high] Section 3, log case bullet: The same missing factor: y′ + P ln y = Q does not become linear under u = ln y. Since y = e^u and y′ = e^u u′, the equation becomes e^u u′ + P u = Q, i.e. u′ + P u e^(−u) = Q e^(−u), which is nonlinear in u. The bullet's claim that it reduces to u′ + P u = Q is false.
- ch 6 [high] Beyond: The note says the same substitution (z = y^(1−n)) turns a Riccati equation into a linear equation once one particular solution is known. That is false. A Riccati equation y′ = P(x)y² + Q(x)y + R(x) with R ≠ 0 is not made linear by z = y^(1−n); the Bernoulli substitution only handles the case R = 0, n = 2. The standard linearisation needs the known solution y₁ and the shifted reciprocal substitution z = 1/(y − y₁). A student will try z = y^(1−n) on a Riccati equation and get stuck.
- ch 6 [low] Section 3: The population model uses the letter P for the population, but P(x) already means the coefficient in y′ + P(x)y = Q(x)yⁿ. A student may read dP/dt = rP − aP² as containing the same P as the linear-equation coefficient. The search phrases in Section 3 also repeat word for word the ones given in Beyond.
- ch 7 [high] section 1, worked example 1 step 5/step 6, section 3, figure caption: The exponential is printed without its superscript: "y = ex", "e0.5 = 1.648721", "the Taylor polynomials of ex", "The limit is ex", "hugging ex". A reader can take "ex" as e·x and "e0.5" as e × 0.5 = 1.359, which contradicts the quoted value 1.648721 and the whole convergence argument.
- ch 7 [high] section 3, after the Picard formula: "The first iterate y₁ is the tangent line at the pin — Euler's method with a variable step" is false in general. y₁(x) = y₀ + ∫ f(t, y₀) dt is a curve that only matches the solution's value and slope at x₀; it is a straight line only in special cases such as f = y. For y′ = x + y, y(0) = 0, y₁ = x²/2, a parabola, not a tangent line. Calling it Euler's method is also loose: y₁ is one sweep of the integral form with y frozen at y₀, not a stepped Euler scheme.
