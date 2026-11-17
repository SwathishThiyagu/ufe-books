# m-de-u2: free-model run

- Book: `books/common/m-de/m-de-u2.html`
- Status: ok
- Model calls so far: 29 (105,338 tokens in, 269,589 out), 6.0 minutes

## Checker

```
m-de-u2.html: 9 chapters, 15004 words, 10 figures, 161 KB
OK
```

## For the reviewer

- chapter 4: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [low] Section 2 (three root types): The chapter says the n roots, counted with multiplicity, fix the n constants, but only simple complex pairs are covered. A repeated complex pair (for example (D²+4)²y = 0) gives four constants and needs x-multiplied sine and cosine terms. A student meeting this in the exam has no rule here.
- ch 1 [low] Figure: The edges run from the roots node (m = 1, 2, 3) to the repeated-root and complex-pair nodes. The roots 1, 2, 3 are real and distinct, so those edges wrongly suggest the example's roots also produce the repeated and complex forms.
- ch 1 [low] Exam traps (last trap): 'Do not use the characteristic polynomial for variable coefficients' is too broad. Euler (Cauchy–Euler) equations have variable coefficients yet are still solved with an auxiliary polynomial after y = x^m. The wording can make a student reject a method that works there.
- ch 1 [low] Section 3 (last bullet): Cross-references 'see 2.2 and 2.4' and 'see 2.6' are plain text, so a student reading on a phone cannot tap through to those chapters.
- ch 2 [low] Lead: The lead says 'four common shapes' but then lists only three items ('an exponential e^(ax), a sine or cosine, and a polynomial'), so a reader counts three.
- ch 2 [low] Section 2, sine/cosine failure case and Section 3 table: The clash rule for sine/cosine is stated only for a simple pair of roots ±ia. If ±ia are double roots of f (for example f(D) = (D² + a²)²), then f′(D) also vanishes after D² → −a², so 'multiply by x and use f′(D)' gives zero again and the rule silently breaks.
- ch 2 [low] Exam traps, first bullet: The heading 'No factor x when it is needed' reads as an instruction not to add x, not as the name of the mistake.
- ch 2 [low] Worked example 1, output: The output block prints three bare numbers (0.5, 0.5, 0.75) with no labels, so a phone reader cannot tell they are A, B and C.
- ch 2 [low] Beyond: 'Symbolic tools such as SymPy's dsolve apply exactly these inverse-operator rules' overstates it; such solvers mainly use undetermined coefficients, variation of parameters or Laplace transforms, not the inverse-operator rule.
- ch 2 [low] Figure versus lead: The lead says the operator rule 'replaces guessing', but the figure is built entirely on choosing a trial ('trial A e^(ax)', 'Trial already in C.F.?'). The two pictures of the method are never connected.
- ch 3 [high] Exam traps, second bullet: The trap says that writing W = y₁′y₂ − y₁y₂′ is wrong and that 'a sign flip changes every conclusion'. The sign flip does not change any conclusion: zero stays zero and nonzero stays nonzero, so independence verdicts and Abel's formula (written consistently with the chosen convention) are unaffected. Only the sign of the number changes. Calling one order 'correct' is also misleading, since both orders appear in standard textbooks.
- ch 4 [low] Section 1, table row 'R₁R₂ → product of the two trials': The product rule is stated without restriction. It holds when one factor is a polynomial, an exponential or a polynomial-times-exponential, but fails when both factors are trigonometric: for R(x)=sin 2x·cos 3x the product of the trials gives cos², sin² and sin·cos terms, which are not the right family and cannot be matched term by term.
- ch 4 [low] Section 2, trigonometric repair rule: The rule says only 'if ai solves the characteristic equation, multiply the whole trial by x'. For a repeated pair of complex roots ±ai (multiplicity s ≥ 2) a single factor x is not enough, and this contradicts the general x^s rule stated just above it.
- ch 4 [low] Section 2, wording 'Multiplying only the top term is wrong; the whole trial moves.': 'Top term' is not defined anywhere and 'the whole trial moves' is unclear for a reader whose first language is not English.
- ch 4 [low] Figure, polynomial branch: The figure promises repair branches for every trial that already solves the homogeneous equation, but the polynomial branch shows only the full polynomial A₀+…+Aₙxⁿ. The case where 0 is a root of the characteristic equation (for example y″−y′=x, where the trial needs an extra factor x) has no repair box.
- ch 4 [low] Whole chapter, e.g. Section 1 'eaxPn(x)', Section 2 'e3x', 'e2xcos 3x', quiz answers 'e2x': Exponents are typed inline without a marker, so e2x, e3x and eax read as products of symbols e, a, x, 2 on a phone screen, not as powers.
- ch 5 [low] Section 1, first paragraph: The list of admissible right-hand sides for undetermined coefficients (eᵏˣ, sin kx, cos kx, a polynomial) leaves out sums and products of these shapes, such as x²eˣ, x sin 2x or eˣcos x, which the method also handles. A student may wrongly conclude those forcing terms also defeat the trial-function method.
- ch 5 [low] Lead and Section 3 ("needs only that the right-hand side be continuous"): Continuity of R alone is not enough. The coefficients P and Q (that is, a₁/a₀ and a₂/a₀) must also be continuous on the interval, and a₀ must not vanish there, or y₁ and y₂ need not exist on the whole interval.
- ch 5 [low] Section 3, the sentence about R = e^(x²): "The answer is then left as a definite integral" is misleading: a definite integral with fixed limits is a number, not a function of x, so it cannot serve as a particular integral. Also, whether the integrals are elementary depends on y₁ and y₂ as well as on R, so the claim is only typical, not guaranteed.
- ch 6 [high] Section 3 and Quiz Q7: After a+bx=e^t, the text says d/dx = b d/dt. This is false: d/dx = (b/(a+bx)) d/dt. The displayed result (a+bx)y′ = bθy is correct, but the reason given in Section 3 and repeated in Q7 is wrong and will lead students to an extra factor.
- ch 6 [high] Section 1 and Exam traps: The sentence 'For x  0.' is incomplete: the '< 0' condition and the substitution for negative x are missing. The trap 'when x  0' has the same missing condition, so a student cannot tell what case is being described.
- ch 6 [low] Section 3: The definition says 'a and b ≠ 0'. Only b ≠ 0 is needed for a+bx to be genuinely linear; a=0 is allowed and reduces to a Cauchy-Euler equation. The same letter a is also used for the coefficients a_n, which can confuse.
- ch 6 [low] Section 3 shortcut: The phrase 'same indicial equation' is ambiguous. For a Legendre equation with b≠1, substituting y=(a+bx)^m produces b^k factors; the polynomial in m matches the θ-characteristic polynomial only when those factors are included, not the Cauchy-Euler polynomial.
- ch 6 [low] Exam traps: The trap says 'the extra −θ term' but the wrong expression θ² is missing the −θ term; the wording points the student the wrong way.
- ch 7 [high] Quiz Q6: The closing claim 'x is easier because its elimination needs no differentiation' is false. Eliminating y is done by applying D to the first equation (D²x + 2Dy = 3), which does differentiate the known right side 3t into 3. Eliminating x, as the answer itself shows, also needs one application of D (to the second equation). Both routes need exactly one differentiation, so the stated reason is wrong and would mislead a student about when D acts on a known function of t.
- ch 7 [low] Section 3 and Exam traps (zero determinant): Saying a zero operator determinant means 'the equations are dependent' covers only one case. When the determinant is zero the equations may also be inconsistent, for example Dx + y = t and Dx + y = 1 have determinant zero yet no solution at all.
- ch 8 [low] Section 1 (derivation), Section 2 (Abel's identity), Exam traps, Quiz Q4: The exponential factor is written in plain text as "e−∫P dx" in several body paragraphs, for example "w = C e−∫P dx/y₁²" and "W = W₀ e−∫P dx". Rendered on a phone this reads as e minus ∫P dx, not as e raised to the power −∫P dx, so the main formula of the chapter is ambiguous everywhere except in the one formula block that uses <sup>.
- ch 8 [low] Section 2, paragraph on Abel's identity: "W₀ is the value of the Wronskian at any convenient point" conflicts with Section 1, which says the inner ∫P dx is any antiderivative. If the antiderivative is shifted by a constant, the constant W₀ is rescaled, so W₀ equals W(x₀) only when the lower limit of the integral is that point x₀.
- ch 8 [low] Section 2, first paragraph: It calls e<sup>−∫P dx</sup> "the same integrating factor as above". It is the factor inside the reduction-of-order integral, not an integrating factor; the integrating factor of the first-order equation for w is y₁²e<sup>∫P dx</sup>, which is different.
- ch 8 [low] Section 3, first sentence on Cauchy-Euler: The shape x²y″ + a x y′ + b y = f(x) never says that a and b are constants. Without that, the reader cannot see why the substitution gives a constant-coefficient equation.
- ch 9 [high] Section 2: The sign discussion is truncated: 'opposite signs (Δ  0)' and 'or decay (τ < 0)' leave out the cases Δ < 0 and τ > 0, so the stability rule cannot be read correctly.
- ch 9 [high] Section 3 table, unstable spiral row: The condition is incomplete: 'Δ > 0, τ²  0' is missing '< 4Δ' and 'τ > 0'. As printed it does not define an unstable spiral.
- ch 9 [high] Section 3, paragraph after table: It says eigenvectors give two special directions and a node has two stable/unstable directions. For a repeated real eigenvalue, there may be only one independent eigenvector, so this is false for an improper node.
- ch 9 [low] Quiz Q6: The answer adds '(improper node)', but equal eigenvalues do not force an improper node. If the repeated eigenvalue has two independent eigenvectors, it is a proper/star node; only the defective case is improper.
- ch 9 [low] Section 3 table: The table omits the repeated-real-eigenvalue case τ² = 4Δ with Δ > 0. It jumps from τ² > 4Δ to τ² < 4Δ, so students cannot classify Q6 from the table.
