# m-prob-u4: free-model run

- Book: `books/common/m-prob/m-prob-u4.html`
- Status: ok
- Model calls so far: 21 (83,914 tokens in, 191,106 out), 4.8 minutes

## Checker

```
m-prob-u4.html: 7 chapters, 12706 words, 8 figures, 141 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, support sentence: The support is defined only through the discrete pmf ('the set of pairs with p(x,y)>0'), and the continuous paragraph never says what the support of a joint pdf is. A student may carry the pmf wording over to the continuous case, where a point with f>0 still has probability 0.
- ch 1 [low] Section 2, sentence on limits of the CDF: 'tends to 0 at either -∞' is compressed and can be misread. F is a function of two variables; the two one-variable limits need to be stated separately.
- ch 1 [low] Section 3, bullet 3 ('If J=0 at a point, treat that point separately'): The real condition for the change-of-variables formula is that the map be one-to-one on the region. A vanishing Jacobian means the map is not locally invertible there, so the formula does not apply at that point. Saying 'treat that point separately' is vague and could suggest that a single point where J=0 can be patched up without checking one-to-one-ness.
- ch 1 [low] Lead, last sentence before the sections: It says the joint pmf, pdf 'or joint CDF' lets you compute P((X,Y)∈A). For the CDF this is only practical for orthants and rectangles; for a general region A the pmf or pdf (double sum/integral) is what you use.
- ch 1 [low] Worked example 1, step 3: Step 3 suddenly computes p(0,0) with no link to the question. The reader has to work out that this is the preparation for part (b).
- ch 2 [high] section 2, final sentence before section 3: The sentence is garbled/truncated: 'f(x|y)=1/y in the worked example is valid only for 04.3 Independent random variables.' The support of the conditional density has been lost and replaced by a reference to another chapter, so a student cannot tell the correct range of validity.
- ch 2 [low] lead: 'If you know the value of one variable, you divide the joint by that marginal' — 'that marginal' is ambiguous; it can be read as the marginal of either variable.
- ch 2 [low] section 3: The continuous conditional expectation is written as E[X|Y=y]=∫ x f(x|y) dx with no limits, unlike the discrete sum which names its range; readers may integrate over the wrong set.
- ch 3 [high] Section 1, after 'A triangular support forces dependence': The sentence 'For f(x,y)=2 on 00.9.' is incomplete and has no valid mathematical meaning. The support and the probability statement are missing, so a student cannot tell whether it is an example, a calculation, or a typo.
- ch 3 [high] Section 3, reliability paragraph: The phrase 'If either unit can fail the system' contradicts the formula. 1-(1-p1)(1-p2) is the probability that at least one unit survives (parallel redundancy). If failure of either unit fails the system, the survival probability is p1p2, not 1-(1-p1)(1-p2).
- ch 3 [low] Worked example 1, step 6: The marginal calculation is printed as 'For g(x,y)=2 on 0x1 2 dy = 2(1−x)', which is missing the integral sign and the correct limits. As written it cannot be read as the marginal density of X.
- ch 4 [low] quiz Q6 answer: The clause 'its magnitude stays the same if the scales are positive' is misleading. The magnitude of ρ is unchanged for any a and c with ac ≠ 0, because |ac| appears in both the covariance and the product of standard deviations; only the sign depends on sign(ac). As written, a student may think negative multipliers change the magnitude.
- ch 4 [low] section 2, joint moments paragraph: Superscripts written with the caret inside running text: 'E[X^i Y^j]' and 'M(s,t) = E[e^(sX + tY)]'. The exponent sX + tY inside e^(...) is easy to misread on a phone.
- ch 4 [low] figure spec: The x axis is labelled 'x in standard units' but the y axis is labelled 'y = ρ x', so the figure does not say that y is also in standard units. The lines y = ρx are only the standardised regression lines when both variables are standardised.
- ch 5 [high] Section 4, and Exam traps bullet 4: The claim that the gap H − T 'typically grows like √n' is true only for a fair coin (p = 0.5). For a general coin with heads probability p, H − T = 2H − n has mean n(2p − 1), so it grows linearly like n|2p − 1|; only the fluctuations around that line are of order √n. The chapter's own worked example uses p = 0.4, where H − T grows like 0.2n, so the statement contradicts the example and would mislead a student into thinking counts always differ by √n.
- ch 5 [low] Quiz Q4: The question does not say the coin is fair, and the answer silently assumes P(heads) = 0.5. After 20 heads a fair coin is very unlikely, so the data would actually suggest a bias toward heads, not tails; the answer should acknowledge this.
- ch 5 [low] Section 4, strong law statement: 'P(lim X̄_n = μ) = 1 as n → ∞' puts the limit outside the probability and attaches 'as n → ∞' to the equation; the limit must be taken inside the probability.
- ch 5 [low] Section 2, variance paragraph: 'The spread of the average shrinks like 1/n' is ambiguous: it is the variance that shrinks like 1/n, while the standard deviation (the natural measure of spread) shrinks like 1/√n.
- ch 6 [low] Figure caption (Section 3): The caption says 'Ten dots already sit on the smooth curve', but the plotted binomial has 11 points (k = 0, 1, …, 10).
- ch 6 [low] Worked example 1, step 5 and dry run: Step 5 computes 2(0.9821) − 1 = 0.9642 from the table, then quotes 0.9643 as the exact area. The dry-run row labelled '2Φ(2.1) − 1' shows 0.9643, mixing the table value with the exact value and inviting the student to think the table gives 0.9643.
- ch 6 [low] Section 3, np ≥ 5 and n(1−p) ≥ 5 discussion: 'which keeps the mean about two standard deviations from both ends' implies the two end distances are similar. The distance from the mean to the far end in standard units is √(n(1−p)/p), which with p = 0.05 and n = 100 is about 44 standard deviations, not about two.
- ch 7 [low] Section 3, whitening paragraph: Whitening is written as Z = Σ^(−1/2)(X − μ) with no condition on Σ. If Σ is singular (the case Section 1 itself allows), no inverse square root exists and Z cannot have identity covariance with independent standard normal components.
- ch 7 [low] Section 3, zero covariance paragraph: It says the joint density of two uncorrelated components factors into the product of marginals, but Section 1 already stated that no density exists in ℝⁿ when Σ is singular. The two statements contradict each other in the singular case.
- ch 7 [low] Exam traps, item 3: The trap says only that 'a negative determinant is impossible'. This can mislead a student into thinking any symmetric matrix with a non-negative determinant is a valid covariance matrix, which is false (e.g. [[1, 2], [2, 1]] is indefinite, and other 3×3 cases fail even with positive determinant).
