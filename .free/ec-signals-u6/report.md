# ec-signals-u6: free-model run

- Book: `books/ece/ec-signals/ec-signals-u6.html`
- Status: ok
- Model calls so far: 29 (125,080 tokens in, 282,760 out), 6.4 minutes

## Checker

```
ec-signals-u6.html: 7 chapters, 13320 words, 8 figures, 142 KB
OK
```

## For the reviewer

- chapter 5: the figure cannot be drawn: note "x[0] at z = ∞" runs off the right edge; shorten it
- chapter 5: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Section 2 (real signals): "This halves the independent coefficients" is loose. For real x[n] the independent real numbers are X[0], plus X[N/2] when N is even, plus (N/2 − 1) conjugate pairs: that is N/2 + 1 real numbers, not N/2.
- ch 1 [low] Section 3, first line: "Only k = 0, …, N−1 are new" is unclear — 'new' has no meaning here; the point is that these are the only distinct (independent) harmonics.
- ch 1 [low] Section 3, last paragraph (pointer to 6.2): "lets N go to infinity and replaces the finite sum with the DTFT" can leave a student thinking the DTFT only applies to periodic sequences with very large period. The DTFT is the transform of an aperiodic sequence.
- ch 2 [high] Quiz Q7: The prompt uses the same x[n] for two incompatible assumptions: it says x[n] is real and even, then asks for the energy of x[n]=(0.8)^n u[n], which is causal and not even. The real-even proof does not apply to that sequence.
- ch 2 [high] Beyond: The sentence says the STFT, periodogram and cepstrum are all DTFTs of windowed frames. The periodogram is the squared magnitude of such a DTFT, and the cepstrum is the inverse DTFT of the log spectrum, not a DTFT of a windowed frame.
- ch 2 [low] Section 2, Dirichlet-kernel note: The zeros statement is too broad: sin(ωN/2)/sin(ω/2) has removable singularities at ω=2πk, where the periodic extension has value N, not zero. Also the full DTFT of the length-N rectangular pulse includes the phase e^(−jω(N−1)/2); the ratio alone is not 2π-periodic for even N.
- ch 3 [low] Section 1, sentence after the DTFT-sampling paragraph: "The DFT is exact at those points; it says nothing between them" overstates the case. The DTFT between bins is completely fixed by the same N samples (it is the sinc-interpolated curve), so zero padding later in the chapter does reveal values between the N bins. A student can read this sentence and conclude that nothing between bins exists.
- ch 3 [low] Section 3, Parseval formula description: "|X[k]|² is the energy of bin k" contradicts the 1/N in the formula: the energy carried by bin k is |X[k]|²/N, not |X[k]|². The later quiz answer says the bins are divided by N, so the two statements disagree.
- ch 3 [low] Quiz Q3 answer: The steps are compressed to "X[1] = 1 − (−1) = 2" and "X[3] = 1 − (−1) = 2" with no visible substitution. A student cannot see where the −(−1) comes from, because the term x[2] = −1 and W4² = −1 are multiplied without being shown.
- ch 3 [low] Quiz Q1 answer: The sum is typed as "Σn=0N−1 x[n] WNnk", which reads as a product chain, not a summation with limits and a power. Read on a phone, a student may copy the limits wrongly.
- ch 4 [high] Section 2, shape of the ROC: The ROC inequalities are truncated or malformed. The finite-length case reads 'when n1 0'; the left-sided case reads '|z| 1'; the two-sided case reads 'r2 1'. A student cannot get the correct conditions.
- ch 4 [high] Section 3, paragraph after the four standard pairs: The sentence is broken: 'ROC |z| sT connects...' is missing the left-sided bound and the mapping equation.
- ch 4 [high] Worked example 1, step 2: The second term's ROC and transform are garbled: 'with ROC |z| 2(z)' does not state |z| < 1/2 or X2(z).
- ch 4 [high] Exam traps, second bullet: For δ[n−1] the z-transform is z<sup>−1</sup>, not z−1. As printed, the claimed pole at z = 0 is false.
- ch 4 [high] Exam traps, last bullet: The left-sided inequality is missing: 'left-sided gives |z| 1' is not a valid ROC condition.
- ch 4 [low] Section 1 and Quiz Q1: Several exponents are shown without superscripts: r−n, z−n, e−jωn, and z−n in Q1. They read as subtraction in plain text.
- ch 5 [high] Section 3, final value theorem example: The text says that for X(z) = 1/(1 − z⁻¹) there is a pole at z = 1 and 'no limit exists'. This contradicts both the chapter's own stated condition (all poles inside |z| < 1 except at most one simple pole at z = 1) and the sequence itself: x[n] = u[n] has a simple pole at z = 1, the theorem applies, and x[∞] = lim_{z→1}(1 − z⁻¹)/(1 − z⁻¹) = 1. It also contradicts Quiz Q5, which correctly allows a simple pole at z = 1.
- ch 5 [high] Quiz Q3 answer: Y(z) = z⁻³/(1 − 0.8z⁻¹) = z⁻²/(z − 0.8). The zero at z = 0 of 1/(1 − 0.8z⁻¹) cancels one of the three z⁻¹ factors, so z = 0 is a pole of order 2, not order 3. The parenthetical '(triple)' is wrong.
- ch 5 [low] Section 1, z-scaling formula: The constant a is called 'a complex constant' but the degenerate case a = 0 is not excluded; at a = 0 the ROC collapses and X(z/a) is not defined.
- ch 6 [high] Section 1: The left-sided case is garbled and unreadable: "If the ROC is |z| m. Read x[−m] as the coefficient of zm." The condition and the series have lost text, so a student cannot tell what the ROC test is or which series to read.
- ch 6 [high] Section 2, ROC bullet: The second case is garbled: "|z| k| gives −pknu[−n−1]". The inequality has lost its left side and the exponent is unreadable.
- ch 6 [high] Section 3: Garbled sentence about the pole at the origin: "it appears for n n−1 then has a negative power". The condition on n is missing and the reason is cut off.
- ch 6 [high] Quiz Q2 answer: The inside/outside mapping is inverted. The contour C lies inside the ROC, so a pole with |p| < radius of C is inside the contour and gives the right-sided term aⁿu[n] (ROC |z| > |a|); a pole outside C gives the left-sided term. The answer states the opposite.
- ch 6 [high] Quiz Q5: The premise is impossible: a pole at z = 2 cannot lie inside the ROC 1 < |z| < 3, because the ROC never contains a pole. The given answer then also inverts the rule, calling a pole at |z| = 2 with |z| < 3 "outside the contour" and left-sided, when a circle of radius between 2 and 3 puts that pole inside C and makes the term right-sided.
- ch 6 [high] Quiz Q6 answer: Garbled expression: "For n n−1 = zn/(z − 0.5) has a negative power of z". The condition on n and the expression for X(z) zⁿ⁻¹ are both unreadable.
- ch 6 [low] Section 3: The complex-pole pair is written rncos(ωn) and rnsin(ωn), which reads as r·n·cos(ωn).
- ch 6 [low] Section 1: Exponents are left as plain characters: "X(z) = Σ x[n] z−n" and "coefficient of z−n" read as z minus n.
- ch 6 [low] Section 2, bullets and table: The bullet uses "pknu[n]" while the table writes aⁿu[n]; the missing superscript makes the two look like different results.
- ch 7 [high] Section 2, first paragraph: The causality sentence is broken: 'Causality means h[n]=0 for nr, where r is the largest pole magnitude' — the condition 'n < 0' and the start of the ROC sentence have been swallowed (an unescaped '<' character). As printed, the definition of causality and the causal ROC rule are both lost, and 'it includes z=∞' has no antecedent.
- ch 7 [high] Section 2, third paragraph: The second half of the example is garbled: 'With |z|nu[−n−1], non-causal and unstable because |z|=1 is outside the ROC.' The ROC condition and the minus sign of the anti-causal inverse are missing (again an unescaped '<'), so the sentence contradicts itself and teaches the wrong h[n].
- ch 7 [high] Section 1, third paragraph: Wrong attribution of the ROC intersection rule. The chapter says the ROC of H(z) 'is the intersection of the input and output ROCs after pole-zero cancellations'. Standard texts give that intersection for the ROC of the output Y(z), not for H(z); H(z)'s ROC follows from its own poles and the assumed causality.
- ch 7 [low] Sections 1 and 4 (formulas and shift rules): Powers are written with a plain minus in places, e.g. 'z−k', 'z−1Y⁺(z)', '1-0.5z−1'. A reader can mistake z−1 for 'z minus one' instead of z⁻¹.
