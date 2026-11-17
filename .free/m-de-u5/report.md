# m-de-u5: free-model run

- Book: `books/common/m-de/m-de-u5.html`
- Status: ok
- Model calls so far: 25 (92,318 tokens in, 216,290 out), 4.9 minutes

## Checker

```
m-de-u5.html: 7 chapters, 12775 words, 8 figures, 139 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1 (heading and step 8): The heading asks to show the residual is zero 'at x = 1, y = 2', but neither the code nor the residual uses x or y. The residual is (m² − 5m + 6)f″, which is zero for every point whenever m is a root, so the chosen point x = 1, y = 2 does no work and a student may think the check is special to that point.
- ch 1 [low] Section 3, paragraph on lower order terms: 'substitute and the three terms cancel' does not match the algebra. Substituting u = e^(kx) f(y + mx) gives four terms: k e^(kx)f plus m e^(kx)f′ from u_x, then minus m e^(kx)f′ from m u_y, then minus k e^(kx)f from k u. Two separate pairs cancel, not three terms.
- ch 1 [low] Exam traps, first trap: 'Using A m² − B m + C = 0 gives m = −2, −3 and a wrong answer' only holds for the numbers of Worked example 1 (A = 1, B = −5, C = 6); read on its own the sentence has no numbers to give those roots.
- ch 2 [high] Section 1, step 4 (same broken line repeated in Quiz Q1 answer and Q4 answer): The three-way classification rule has lost its comparison signs, so it reads 'Δ  0 gives hyperbolic' and 'If Δ  0 hyperbolic'. The elliptic and parabolic cases are never stated at all, so a student cannot classify any equation from this text.
- ch 2 [high] Section 3, variable coefficients (Tricomi-type example y u_xx + u_yy = 0): The regions are assigned to the wrong types. With A = y, B = 0, C = 1, Δ = −4y. For y > 0, Δ = −4y < 0, which is elliptic, not hyperbolic. The hyperbolic region is y < 0.
- ch 2 [high] Quiz Q4: The answer is wrong: Δ = −8 is less than zero, so the equation is elliptic at (2, 1), not hyperbolic. The second point (−1, 0) asked in the question is never evaluated.
- ch 2 [high] Exam traps, first trap: The trap is stated backwards. If the mixed term is written 2B u_xy, then using the full coefficient 2B in Δ = B² − 4AC gives (2B)² − 4AC = 4(B² − AC), which has exactly the right sign. Using B² − 4AC is therefore not a mistake here; the real mistake is halving the coefficient and then still applying B² − 4AC. As written, the trap contradicts the correct explanation in Section 3.
- ch 2 [low] Worked example 2, answer line: 'factors as (u_x − u_y)²-like operator structure' is vague and can be misread as the square of the expression u_x − u_y, which is not the same thing.
- ch 3 [high] Section 2, sentence starting 'If λ0': The condition is garbled: 'If λ0, write λ=k²'. A student cannot tell whether the text means λ>0, λ<0 or λ=0, and the negative and zero cases are never handled, so it looks as if a positive sine solution is the only option.
- ch 3 [low] Worked example 1, step 6: The constant D=1 is called 'the normalized sine mode', but sin 2y with D=1 has norm √(π/2), not 1.
- ch 3 [low] Worked example 1, step 6: The step shows Y(π)=0 is satisfied for any D, which is true only because λ=4 was handed to the student. A reader may not see that in a general problem the same condition is what selects kL=nπ.
- ch 4 [low] Section 2 ("If f = 0, the velocity creates two ramp-shaped waves, one on each side") and Quiz Q6: The two waves produced by the initial velocity are not identical copies. The formula u = (1/2c)[G(x+ct) − G(x−ct)] (with G' = g) shows the left-moving wave and the right-moving wave have opposite signs: one ramp goes up and the other goes down, and for a sharp blow g the pair are step pulses, not two ramps on each side. A student can read the sentence as two equal upward bumps moving apart, which is the f-case, not the g-case.
- ch 4 [low] Figure (D'Alembert split): The node notes give the right wave as f(x−ct) and the left wave as f(x+ct) with no factor, but the formula in Section 2 has ½f(x−ct) and ½f(x+ct). The diagram promises full-amplitude copies while the text says the shape splits into half-size copies, so the two disagree.
- ch 4 [low] Worked example 1 (line "x is in metres and the sine argument is in radians"): sin x needs a dimensionless argument, so "x in metres" and "argument in radians" side by side reads as a contradiction and a strict reader will mark the initial condition as dimensionally unclear.
- ch 5 [high] Beyond: 'With a complex coefficient the same equation becomes the Black–Scholes equation of option pricing' is wrong. Making the coefficient imaginary turns the heat equation into the free Schrödinger equation, not Black–Scholes. Black–Scholes is a backward parabolic equation with variable coefficients that is turned into the heat equation by a change of variables, not by changing the coefficient.
- ch 5 [low] Worked example 1, steps 1–6; exam traps 4 and 5; quiz Q3, Q4: Exponentials are typed in plain text: 'e−λt sin x', 'e−t', 'e−n²t', 'e−9t', 'e+|λ|t'. On a phone these read as subtraction or addition ('e minus lambda t', 'e plus |λ|t') instead of a power, and 'e+|λ|t' is especially misleading.
- ch 5 [low] Section 2, final formula box: The general solution u = Σ b_n sin(nπx/L) e^(−α²n²π²t/L²) is placed after the insulated-ends cosine discussion, with nothing saying it belongs to the zero-end problem. A student can carry the cosine mode (n = 0) into the sine series, or think b_n applies to the insulated rod.
- ch 5 [low] Section 1, formula box: Calling α² itself 'the thermal diffusivity' clashes with many textbooks, which write u_t = α u_xx and call α (units m²/s) the thermal diffusivity. Students moving between books will be confused about which symbol holds the number 1.1 × 10⁻⁴ m²/s.
- ch 5 [low] Figure caption: The peak value is given as 'about 36.8' with no unit, and the rod length (L = π m, the reason the decay factor is e^(−1)) is not stated. The reader cannot check where 36.8 comes from.
- ch 5 [low] Section 2 and final formula box: Cross-references are plain text ('the product guess of 5.3', 'see 5.7'), so a student reading on a phone cannot jump to the chapter that defines the product method and the Fourier coefficients.
- ch 6 [high] Section 3 and Section 4 (also the Section 4 displayed series, the Section 3 building blocks, and the Q4 answer): The exponents and subscripts are lost, so the key formulas read as products instead of powers. 'rn(Ancos nθ+Bnsin nθ)', 'r−n', 'an(Ancos nθ+Bnsin nθ)', 'A0/2', 'Yn' can be read as r times n, a times n, A times 0, and similar. A student can take the disk solution to be linear in r, which is wrong: in a disk the radial factor is r raised to the power n.
- ch 6 [low] Beyond: The sentence 'In polar and cylindrical settings the same separation gives Bessel functions' is misleading. Two-dimensional polar separation gives the Euler equation with rⁿ and r⁻ⁿ, not Bessel functions. Bessel functions appear when a third (z or cylindrical) coordinate is separated. The 'met in Unit 3' cross-reference is also unverifiable here.
- ch 7 [high] Section 1, orthogonality paragraph: The chapter says that on 0 < x < L, 'sine times cosine integrates to 0'. That is false. Sine and cosine modes are mutually orthogonal only over a full period −L < x < L. On the half interval the cross integral does not vanish in general: for L = 1, m = 1, n = 2, ∫₀¹ sin(πx)cos(2πx)dx = −2/(3π) ≠ 0. A student who believes this would think a mixed sine–cosine series can be handled by the same one-mode-at-a-time rule.
- ch 7 [low] Worked example 1, opening line: The domain is garbled: 'Solve u_t=u_xx for 00, with ...'. The reader is never told that 0 < x < 1 and t > 0, even though the rest of the example (L = 1, integration from 0 to 1) depends on that domain.
