# m-prob-u5: free-model run

- Book: `books/common/m-prob/m-prob-u5.html`
- Status: ok
- Model calls so far: 16 (62,311 tokens in, 161,691 out), 4.6 minutes

## Checker

```
m-prob-u5.html: 6 chapters, 11087 words, 7 figures, 124 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3, first paragraph: 'SE(x̄) measures the typical distance between x̄ and its own mean μ' is imprecise. The standard error is the standard deviation of the sampling distribution, i.e. a root-mean-square distance from μ, not an average absolute distance.
- ch 1 [low] Section 1, definition of statistic: The definition says a statistic may use x₁, …, xₙ and n only, but Q7 correctly allows known constants. The standard definition should say 'sample values and known constants only'.
- ch 1 [low] Section 2, random sampling: C(N, n) is named but never defined by a formula, so a student cannot compute it from the text alone.
- ch 1 [low] Section 1, sample variance: S² is used without stating its divisor; students may not know whether it uses n or n−1.
- ch 1 [low] Section 3, sampling error: The sentence 'the difference between a statistic and the parameter that comes from looking at only part of the population' can be misread as saying the parameter comes from looking at part of the population.
- ch 2 [high] Quiz Q6: The answer describes the t statistic as a ratio of independent standard normal and chi-square variables. That is not the definition: the t statistic is Z divided by the square root of an independent chi-square variable divided by its degrees of freedom. The square root and division by df are missing, so the explanation is technically wrong.
- ch 3 [low] Lead: The lead says t is 'a standard normal divided by a scaled chi-square'. The denominator is the square root of a scaled chi-square, not the scaled chi-square itself, so the one-line summary is slightly wrong even though the formula later in Section 2 is correct.
- ch 3 [low] Section 1, sample variance sentence: S² is called 'sample variance' but its divisor is not fixed. The statement (n−1)S²/σ² ~ χ²(n−1) is only true when S² = Σ(Xᵢ − X̄)²/(n−1); if a student uses the divisor-n version, the formula fails.
- ch 3 [low] Section 2, sentence on when t is used: 'We use t when σ is unknown and the sample is small' suggests t is only valid for small samples. The definition given just above holds for any sample size n from a normal population; small n is only a rule of thumb for when the difference from z matters.
- ch 3 [low] Figure vs Section 3: The figure names the denominator chi-square of F as W and the numerator as U, while Section 3 writes the same two variables as U and V. V is already used for the chi-square inside t in Section 2, so students may connect the wrong nodes to the F formula.
- ch 4 [low] Worked example 1, step 9: Step 6 computed Var(T1) with the finite population correction, (σ²/n)((N−n)/(N−1)) = 5/3. Step 9 then writes Var(T1) = σ²/n → 0, which is the with-replacement formula and does not match the value 5/3 just obtained. A student may think one of the two formulas is wrong.
- ch 4 [low] Worked example 1, steps 3 and 5; Quiz Q4: Step 3 lists the samples as unordered pairs {2,4}, {2,6}, …, but step 5 and Q4 define T2 as 'the first observation' of the sample. In an unordered sample there is no first observation, so the definition is unclear at the point where it is used.
- ch 4 [low] Section 3 and Exam trap 4: Trap 4 ('An unbiased estimator can be inconsistent if its variance does not go to 0') can be read as the converse rule 'variance not going to 0 means inconsistent', which is false: an estimator can be consistent and still have a variance that does not shrink (rare large errors). Only the direction bias → 0 and Var → 0 is a valid test.
- ch 4 [low] Section 3, Chebyshev sentence: The bound P(|Tn − θ| ≥ ε) ≤ MSE(Tn)/ε² applied to (Tn − θ)² is Markov's inequality; Chebyshev's inequality is the special case where the estimator is unbiased (mean of Tn − θ is 0). Calling it Chebyshev for a biased estimator is loose and contradict marginally with the chapter's own emphasis that bias may be nonzero.
- ch 5 [low] Section 1 and Exam traps (first item): The chapter says L(θ) is 'the chance of seeing this sample'. This is exact for discrete data but wrong for continuous data, where the product of densities is a joint density and the probability of an exact sample is zero. A student can carry away the idea that the likelihood is a probability in every case.
- ch 5 [low] Section 2, procedure bullets: The bullet list tells the reader to drop additive constants only after taking logs, but never states the earlier and equally useful step of dropping factors in L(θ) that do not contain θ. The worked example does this silently (dropping 120), so the rule is applied before it is stated.
- ch 6 [low] Lead: The lead calls the interval 'a range of plausible values for an unknown population parameter'. A student can read this as a probability statement about the parameter, which Section 1 rightly forbids ('It either contains θ or it does not').
- ch 6 [low] Section 2, sample size planning line: The planning formula n = (zσ/E)² is given without saying that σ is usually unknown at the planning stage and must be replaced by a guessed or pilot-study value, and without saying the t critical value is normally used in the formula when the guess is uncertain.
- ch 6 [low] Section 3, variance formula and exam traps: The chi-square symbol χ²p,ν is defined with area p to its right, while z and t in the same chapter are defined with area to the left. The definition is present but easy to skip, and the trap about swapping denominators does not restate it, so a student can plug in the wrong table value.
