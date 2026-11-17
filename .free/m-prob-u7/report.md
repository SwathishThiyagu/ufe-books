# m-prob-u7: free-model run

- Book: `books/common/m-prob/m-prob-u7.html`
- Status: ok
- Model calls so far: 27 (94,798 tokens in, 198,454 out), 4.4 minutes

## Checker

```
m-prob-u7.html: 9 chapters, 14037 words, 10 figures, 158 KB
OK
```

## For the reviewer

- chapter 1: the figure cannot be drawn: note "temp" runs off the right edge; shorten it

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, bullet on the ensemble: The bullet says the ensemble is 'the collection of all possible paths at a fixed time'. Paths run over time, so they cannot sit 'at a fixed time'. The bullet also clashes with the earlier sentence in the same section, which says the ensemble at a fixed t is the set of values of X(t) across outcomes.
- ch 2 [low] Section 1: The justification that X(t)=A is SSS only shows that each single-time value has the distribution of A. Strict stationarity is a statement about every finite-dimensional joint CDF, so the given reason is incomplete and a student may think checking marginals is enough.
- ch 2 [low] Worked example 1, step 5: The time average is evaluated only over a whole number of cycles. That shows the average along a special subsequence of record lengths, not the limit as T→∞ for arbitrary T, so the ergodicity conclusion rests on a special case.
- ch 2 [low] Quiz Q5: The question asks for two properties of R_X(τ) but the answer lists three (R_X(0)=E[X(t)²], evenness, and the Cauchy–Schwarz bound), which does not match the 2-mark demand.
- ch 3 [low] Section 1, 'three defining properties': The list gives only N(0)=0, independent increments and stationary increments. With only these three, a process whose jumps come in twos (a compound Poisson process with jump size 2) also qualifies, yet its count is not Poisson. The 'one at a time' condition is mentioned in the prose above but is dropped from the list of defining properties, so the definition is incomplete and the Poisson pmf does not follow from the three listed properties alone.
- ch 3 [low] Section 3, sentence after the renewal function: 'For general interarrival laws m(t) is not simply t/μ at small t' is misleading. For non-exponential gaps m(t) differs from t/μ at finite t of any size, not only at small t; the two agree only in the limit t → ∞ (the elementary renewal theorem stated just below). A student may conclude m(t) = t/μ for large but finite t.
- ch 3 [low] Worked example step 2; exam traps 1 and 2; quiz Q1 and Q7 answers: Powers have lost their markup, so the expressions cannot be read correctly. Step 2 shows 'e−1×10/0!', where the intended 1 raised to the power 0 appears as the number ten; read literally the value would be 10/e ≈ 3.68, not 0.3679. Exam traps and quiz answers show 'e−λt(λt)k/k!', which reads as a product of plain symbols rather than exponentials.
- ch 3 [low] Beyond paragraph: 'Poisson models size telephony call arrivals' is not clear English; 'size' has no meaning here.
- ch 4 [low] section 1, section 2, section 3: Subscripts and superscripts are written as plain characters: 'Xn+1' can be read as X times n plus 1, 'Pij' and 'Σj Pij' lose the indices, and 'Pn' (used for the n-fold product) can be read as P times n. The chapter also uses P² elsewhere, so the notation is not consistent.
- ch 4 [low] section 3 and exam traps: The definition of accessibility uses n ≥ 0, but the trap on reachability says 'some n ≥ 1'. The same word is defined with two different ranges, which is confusing when students check whether i is accessible from itself.
- ch 4 [low] section 3: The period is defined as gcd{n ≥ 1 : Pii(n) > 0}, but for a state that can never return (a transient state with Pii(n) = 0 for all n ≥ 1) this set is empty and the gcd does not exist. The definition silently assumes the set is non-empty.
- ch 5 [low] Figure (aria description): The accessible description says the sunny probability 'rises from 1 and settles towards 0.6', but the plotted curve and the caption both show it starting at 1 and falling towards 0.6. A screen-reader user gets the opposite shape from the one shown.
- ch 6 [low] Section 1: The sojourn formula is written as 'P(T_i > t)=e−λ_i t', which a phone reader can misread as e minus λ_i times t rather than e raised to −λ_i t.
- ch 6 [low] Section 1 and Exam traps: Section 1 says the sojourn is exponential with rate λ_i > 0, but the traps then allow q_ii = 0 for an absorbing state, where the exit rate is 0 and the chain never jumps. A student will see a contradiction.
- ch 6 [low] Section 3: The cross-reference 'See 7.3' is plain text, so it does not work as a chapter link the way other cross-references in the book do.
- ch 6 [low] Exam traps: The sentence 'Forgetting the sign gives a negative mean sojourn time' is easy to misread: q_ii is already negative, and plugging it into 1/q_ii gives the negative value, not 'forgetting the sign'.
- ch 7 [high] Quiz Q6 (answer): The answer says RXY(τ)=0 for all τ means X(t) and Y(t+τ) are 'uncorrelated at every lag'. That is only true when at least one mean is zero. Uncorrelated means the cross-covariance is zero, i.e. RXY(τ)=μXμY, not RXY(τ)=0. With μX=2, μY=3, RXY(τ)=0 gives CXY(τ)=−6, which is correlation, not absence of it. RXY(τ)=0 is orthogonality.
- ch 7 [low] Lead: 'Their Fourier transforms give power spectral density (PSD)' is loose: the Fourier transform of the cross-correlation is the cross-PSD, not the PSD.
- ch 7 [low] Section 2: The chapter never states the two facts students most often need about the PSD of a real process: that SX(ω) is real and non-negative, and that it is even. Only Q7 touches evenness, and non-negativity is never mentioned, so a student cannot check whether a computed PSD is plausible.
- ch 7 [low] Section 3, last sentence: 'Some syllabi call SX(ω) the spectral density' sits inside the section on the autocorrelation matrix, where SX(ω) has not been introduced, and adds nothing for the reader.
- ch 8 [high] Section 2 (white noise PSD) and Quiz Q5 answer: Unit mismatch. The chapter defines all PSDs as power per rad/s and computes power with (1/2π)∫S(ω)dω. It then writes S_X(ω) = N₀/2 'for every ω' while saying N₀ is in power per Hz. The two-sided density in W/Hz is N₀/2, but converting to rad/s divides by 2π, so the per-rad/s two-sided density is N₀/(4π). Using N₀/2 in the rad/s formula overstates the power by 2π.
- ch 8 [low] Section 1, definition of h(u): Calling h(u) 'the gain applied to the input u seconds earlier' is loose: h(u) is a density, and the weight attached to X(t−u) is h(u)du, not h(u). With h having units of 1/s the word 'gain' is misleading.
- ch 9 [low] Lead: The lead says Gaussian noise has 'zero mean and a flat power spectral density'. A flat PSD is what makes noise white, not what makes it Gaussian. Section 2 states this correctly ('white describes the flat spectrum, Gaussian describes the amplitude distribution'), so the lead contradicts the body and can leave a student thinking Gaussian noise is always white.
- ch 9 [low] Section 3: The output-mean rule μ_Y=H(0)μ_X is written without saying μ_X must be a constant. Applied to a Gaussian process with a time-varying mean function, H(0)μ_X(t) is wrong; the correct rule is that the mean function is passed through the filter, Y's mean is h(t)*μ_X(t).
