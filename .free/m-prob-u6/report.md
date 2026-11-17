# m-prob-u6: free-model run

- Book: `books/common/m-prob/m-prob-u6.html`
- Status: ok
- Model calls so far: 23 (91,586 tokens in, 162,615 out), 5.1 minutes

## Checker

```
m-prob-u6.html: 6 chapters, 12515 words, 7 figures, 127 KB
OK
```

## For the reviewer

- chapter 3: the figure cannot be drawn: note "test differences" runs off the right edge; shorten it

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, sentence defining the alternative hypothesis: The text is garbled: "It can be one-sided, H1: μ 1: μ > 1000 h, or two-sided, H1: μ ≠ 1000 h." A student cannot tell which one-sided alternative is being defined, and the symbols are broken.
- ch 1 [high] Quiz Q1 answer: The answer text is garbled: "such as μ  μ0 or μ ≠ μ0". The one-sided alternatives have lost their inequality signs, so the answer is unreadable and incomplete.
- ch 1 [low] Figure spec, title: The title says "Five steps of a test" but the flowchart has six nodes (state hypotheses, fix α, take sample, compute statistic, find p-value, decide). The worked example also lists six steps.
- ch 1 [low] Section 2, error table: The cell for "H0 true / Fail to reject H0" says only "Correct", while the matching "H0 false / Reject H0" cell gives the probability 1 − β. Leaving out the probability 1 − α loses the symmetry and the useful fact that the two correct decisions have probabilities 1 − α and 1 − β.
- ch 2 [high] Section 2, confidence interval link: The general statement uses 1.96 for a test at level α, but 1.96 is the critical value only for 95% two-sided confidence. For other α the stated equivalence is wrong.
- ch 2 [low] Section 3, two proportions: The normal approximation condition is given for the one-proportion test but not for the two-proportion test.
- ch 3 [high] Section 3, decision-rule bullet: The rule 'Reject H₀ if |t| exceeds the critical value' is wrong for a one-tailed test. With H₁: μ < 250 g in Worked example 1 and critical value 1.833, a sample giving t = +2.5 (x̄ above 250 g) has |t| = 2.5 > 1.833 and the rule tells the student to reject — a rejection in the direction opposite to the alternative. Taking absolute value also throws away the sign that the chapter itself says must be kept.
- ch 3 [low] Exam traps, third bullet ('Losing the sign'): The advice 'Compare |t| with the two-tailed critical value' describes only a two-tailed test and conflicts with the one-tailed procedure used earlier in the chapter; a student applying it to a one-tailed problem will use the wrong column of the t table.
- ch 3 [low] Section 3 assumptions, last bullet ('Confusing the pooled variance with an average of the variances'): The wording is self-contradictory: the pooled variance is weighted by degrees of freedom n − 1, which is close to the sample size, and then the sentence says 'so a small group counts less' — which is the effect of the sample size. A student can read this as saying the two weightings point in opposite directions.
- ch 3 [low] Figure caption: 'The degrees of freedom come from the branch, not from the sample size alone' is misleading: the degrees of freedom come from the branch and the sample sizes together (n − 1; n₁ + n₂ − 2).
- ch 4 [low] Exam traps, item 5: Saying that using divisor n gives "wrong df" is not accurate: the degrees of freedom come from the sample sizes, so they are n1 − 1 and n2 − 1 whatever divisor is used. The real error is that the ratio s1²/s2² built with divisor n is a scaled version of the F statistic and no longer follows F(n1 − 1, n2 − 1), so the table comparison is wrong.
- ch 4 [low] Section 2, procedure bullet for H1: σ1² < σ2²: The bullet says to swap the labels or use F = s2²/s1², but it does not say that the df pair and hence the table entry must also be swapped. A student who only flips the ratio will read the critical value with df in the wrong order, which the same chapter warns about elsewhere.
- ch 4 [low] Worked example 1: The example jumps to the F test without stating the normality assumption that the test needs; the two samples are only described by n and s, and a reader cannot tell whether the test is legitimate here.
- ch 5 [low] Section 1 (and Quiz Q2): The text says dividing by E 'standardizes the gap'. Strictly, the standardized residual is (O − E)/√E, because the variance of a count of size E is about E. Dividing the squared gap by E gives the square of that standardized residual. As written, a student may think the divisor is E in the residual itself, and may miss why E and not E² is used.
- ch 5 [low] Figure (2×2 contingency table): The table is drawn with row labels Coached, Not, Total and three numbers per row, but no column headers. The caption mentions Pass, Fail and Total columns, yet a reader looking at the figure cannot tell which number is which, or verify the expected count (50 × 50)/100 = 25.
- ch 5 [low] Exam traps, third bullet: 'Do not use the chi-square test on very small expected counts without correction' is vague: it does not say what the correction is, and a student may think Yates' correction fixes small expected counts, which it does not.
- ch 6 [low] Section 1, one-way model: The constraint Στi = 0 is stated without qualification. It is the usual constraint only when the group sizes are equal; with unequal ni the standard fixed-effects constraint is Σ ni τi = 0, and the (unweighted) Στi = 0 does not make the group effects add to the overall mean.
- ch 6 [low] Section 2, end of the step list: The four model assumptions (independence, normal errors with equal variance, additive effects, robustness) are printed as a plain continuation of the numbered procedure steps. A student revising quickly can read them as further steps to carry out.
- ch 6 [low] Section 1, first paragraph: 'Ten tests make at least one false alarm likely' overstates the size of the effect. With ten independent 5% tests the chance of at least one false alarm is 1 − 0.95¹⁰ ≈ 0.40, which is substantial but below one half.
