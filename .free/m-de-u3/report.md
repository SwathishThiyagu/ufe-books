# m-de-u3: free-model run

- Book: `books/common/m-de/m-de-u3.html`
- Status: ok
- Model calls so far: 22 (109,637 tokens in, 249,279 out), 5.9 minutes

## Checker

```
m-de-u3.html: 7 chapters, 14056 words, 8 figures, 153 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, first sentence of standard form: The sentence 'Every second-order linear homogeneous ODE can be written in standard form' hides the condition that the coefficient of y″ must be non-zero. In the worked example the coefficient is x² − 1, so the division is impossible at x = 1 and x = −1, which is exactly why those points are singular. A student may think standard form is valid everywhere.
- ch 1 [low] Section 3, Legendre's equation: The symbol n in n(n+1) is never defined, and the sentence 'At x = 1, both blow up' fails when n = 0, because then Q(x) = 0 and only P blows up. The conclusion (regular singular) is still right, but the stated reason is not.
- ch 1 [low] Quiz Q2 answer: 'Multiplying by (x − x₀)^r with a suitable r absorbs this mild blow-up' says nothing is said about what is multiplied. Nothing is multiplied in the Frobenius method; the solution itself is assumed to carry the factor (x − x₀)^r, which could confuse a student about the procedure.
- ch 2 [low] Section 1, definition of ordinary point: The chapter says a point is ordinary when P(x₀) ≠ 0 and then says p and q 'have Taylor series about x₀'. Standard textbooks also require P, Q, R themselves to be analytic at x₀ (for example polynomials, or functions with convergent Taylor series there). Without that, P(x₀) ≠ 0 alone does not guarantee p = Q/P and q = R/P are analytic.
- ch 2 [low] Exam traps, third trap: 'The lowest power in y″ fixes it' is only true for y″ − xy = 0. For a general y″ + p(x)y′ + q(x)y = 0 the constant term is 2a₂ + p(x₀)a₁ + q(x₀)a₀ = 0, so a₂ depends on a₀ and a₁; for y″ + y = 0 this gives a₂ = −a₀/2, not 0. Read generally, the trap can push a student to write a₂ = 0 wrongly.
- ch 3 [high] Section 1: The text says that after substituting y = (x − x0)^r Σ a_n(x − x0)^n into y″ + P y′ + Q y = 0 the lowest power is (x − x0)^r. In that standard form the lowest power is actually (x − x0)^(r−2), coming from y″ and Q y. The power (x − x0)^r appears only after multiplying the ODE by (x − x0)^2.
- ch 3 [high] Section 3: The bullet says to set the coefficient of (x − x0)^(n+r1) to zero. In the standard form y″ + P y′ + Q y = 0 the recurrence comes from the coefficient of (x − x0)^(n+r1−2); the stated power is correct only after multiplying the ODE by (x − x0)^2.
- ch 3 [high] Section 1: The definition of a regular singular point is given only as finite limits of (x − x0)P(x) and (x − x0)^2Q(x). Standard textbooks require these functions to be analytic at x0 (equivalently, to have convergent power series there). Finite limits alone are not sufficient.
- ch 3 [low] Figure: The recurrence a_n = −a_(n−1)/[n(2n+1)] is correct only for the larger root r1 = 1 in this example. The figure places it after the general assumption y = x^r Σ a_n x^n without saying to take r = 1. For r = 1/2 the recurrence is different.
- ch 3 [low] Section 2: For complex indicial roots, the real logarithmic solution should use ln|x − x0| when x can lie on either side of x0. Writing ln(x − x0) is real only for x > x0.
- ch 3 [low] Quiz Q1: The answer defines p0 and q0 with limits but does not write the limit variable. This can be read as an ordinary product rather than a limit as x → x0.
- ch 4 [low] Section 2 (n = 0 bullet), worked example step 1, parity sentence in Section 2: Powers are not marked up in several prose formulas, so they read as products. The n = 0 bullet shows "P0(x) = 1/(20·0!) d0/dx0[(x²−1)0]", which literally reads 1 divided by 20·0! = 1/20, not 1. Similarly "2nn!", "dn/dxn", "(−x) = (−1)nPn(x)" and the definition line "2n = 2 multiplied n times" read as 2·n, not 2 to the power n. Unicode superscripts are used correctly elsewhere (2², 2³), so the chapter is inconsistent and a student can misread the formula.
- ch 4 [low] Section 1, last two bullets, and Quiz Q2 answer: The test for a regular singular point is stated as if a simple zero of the coefficient of y″ were enough by itself. That is only true when the other two coefficients are analytic at the point. Here the coefficient of y′ is −2x and the coefficient of y is n(n+1), both analytic everywhere, so the conclusion is right but the reasoning as written is incomplete.
- ch 4 [low] Section 3, first paragraph: The chapter calls this a Sturm-Liouville equation with weight 1 on [−1, 1] but does not say that the problem is singular, because p(x) = 1−x² vanishes at both ends. Without that, a student cannot see why the usual Sturm-Liouville boundary conditions are replaced by keeping y finite at x = ±1, and why only n = 0, 1, 2, … gives an acceptable polynomial solution.
- ch 5 [high] Section 1, choice of a0: The text gives a0 = 1/(2νΓ(ν+1)). Without the exponent this is not the standard normalization, so the series does not give the standard Jν for general ν.
- ch 5 [high] Section 2, zeros sentence: The zeros sentence is garbled: 'jν,1 ν,2 0,1 ≈ 2.4048' loses the ordering notation and the label j0,1. A student cannot tell that 2.4048 is the first zero of J0.
- ch 5 [high] Section 3, sector/annulus sentence: The statement 'For a sector or annulus, ν need not be an integer' is wrong for a full annulus. A full annulus still has 2π angular periodicity, so ν must be an integer.
- ch 5 [low] Section 1, J−n identity: The exponent is missing in 'J−n(x) = (−1)nJn(x)'; it can be read as multiplying by n.
- ch 5 [low] Figure, plot ranges: The x-range runs to 8 and the y-range is -0.6 to 1.1, but the truncated series diverge and reach about -64.8 and +57 over that range. The curves will leave the plot area, so the figure does not match the caption about behaviour near x = 0.
- ch 6 [high] Section 1, singular problem bullet: The bullet says a singular problem arises when 'p blows up at an end (Bessel at x = 0)'. For Bessel on (0, 1) the chapter itself gives p = x, so p vanishes at x = 0; it does not blow up. What blows up at x = 0 is q = −ν²/x. As written, this contradicts Section 3 and gives students the wrong picture of why Bessel is singular.
- ch 6 [low] Section 2, paragraph after the Lagrange identity: The sign is flipped. Substituting L y = −λ w y into ∫(u L v − v L u) dx gives (λ_m − λ_n) ∫ w y_m y_n dx = 0, not (λ_n − λ_m) times the integral. The conclusion is unchanged because the right side is zero, but the step as printed is not the one the identity produces.
- ch 6 [low] Section 1, regular problem bullet: The regularity conditions omit w > 0 on [a, b], although the chapter insists on w > 0 earlier. Without w > 0 the weighted inner product and the norm √(∫ w y² dx) can fail.
- ch 6 [low] Section 2, 'the eigenvalues are simple and countable': Simplicity holds for a regular Sturm–Liouville problem with separated boundary conditions. With periodic boundary conditions the same λ can carry two independent eigenfunctions (for example sin nx and cos nx on [−π, π]), so the unqualified claim is too strong.
- ch 6 [low] Section 1, 'Any a(x) y″ + b(x) y′ + c(x) y = 0 reaches this form after one multiplication': The division by a(x) silently assumes a(x) ≠ 0 on the interval, and the reduction only works when λ enters c(x) linearly. Neither condition is stated.
- ch 7 [high] Section 3, Sturm comparison theorem statement: The theorem sentence is corrupted: 'and let a 1 equation has at least one zero in (a, b)' is missing the definition of a and b and the conclusion. Also, the condition q₁ ≥ q₂ is not enough for the stated conclusion for every nontrivial solution: if q₁ = q₂ and v is the same solution u, then v has no zero inside (a, b).
