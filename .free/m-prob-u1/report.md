# m-prob-u1: free-model run

- Book: `books/common/m-prob/m-prob-u1.html`
- Status: ok
- Model calls so far: 19 (73,772 tokens in, 171,578 out), 5.0 minutes

## Checker

```
m-prob-u1.html: 7 chapters, 12473 words, 8 figures, 138 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, first paragraph: The endpoint descriptions for exclusive and inclusive classes are swapped. Exclusive classes DO share an endpoint (10–20 and 20–30 both contain the written value 20); inclusive classes do NOT (10–19 and 20–29 leave a gap between 19 and 20). As written, the two sentences contradict the very examples given next to them, and contradict the rest of the chapter (the 0.5 conversion, exam trap 2).
- ch 1 [high] Exam traps, trap 1: Wrong consequence. Drawing inclusive classes 10–19 and 20–29 without adjusting leaves a gap of 1 unit between the bars; it does not make the bars overlap. 'Overlap' is the opposite of what happens, and it also contradicts the standard reason for adjusting (bars must touch).
- ch 1 [high] Quiz Q5, answer: Same error as the trap, plus the phrase 'overlap at the gap' is self-contradictory. With written limits 10–19 and 20–29 the bars are 9 units wide if plotted literally, so a gap appears; nothing overlaps.
- ch 1 [low] Section 3, histogram sentence: Setting height = frequency is correct only when all class widths are equal. If the classes have different widths, a frequency-height histogram misrepresents the data.
- ch 1 [low] Lead: 'It also draws the first picture, the histogram or ogive' says the frequency table draws the picture, which a student may read literally. The table is drawn from, not drawing.
- ch 2 [low] Lead: The lead says the mean 'minimises squared error', which is loose, and it sets up a comparison with the median but never completes it. The median minimises the sum of absolute deviations, not nothing at all, and students remember 'balances the ordered list' as a vague phrase.
- ch 2 [low] Section 3, merits and demerits: 'The mean uses all values and is easy to algebra' is a typo/awkward phrase; it reads as broken English for phone readers.
- ch 2 [low] Worked example 1, step 6: The modal class here has f₀ = 0 and the frequencies fall steadily (10, 8, 6, 4, 2), an extreme J-shape. The grouping formula still gives 8.33, but it is unreliable for such a shape: the empirical relation would give 3(16.25) − 2(18.33) ≈ 12.08. Without a caveat a student takes 8.33 as exact.
- ch 3 [high] Figure (caption, aria, and plotted series): Both plotted curves peak at 1.0 at x = 5. The curve named 'small SD' (exp(-((x-5)²)/1.0)) is narrower but is below the 'large SD' curve everywhere except at the peak. The caption and aria call the smaller-SD curve 'taller'/'tall', which contradicts the plot a student sees. A student gets the wrong picture of how a smaller SD changes a frequency curve.
- ch 3 [low] Section 2, first paragraph: 'Use absolute distances, because signed distances cancel to zero' is exactly true only when the centre A is the mean. For the median the signed deviations do not sum to zero, so the stated reason is incomplete and can confuse a student who chooses the median.
- ch 4 [high] Beyond: The Sharpe ratio is described wrongly. Sharpe divides the average excess return by the SD of returns, that is (mean return − risk-free rate)/SD. The chapter says it divides SD by the average return, which is the inverse of the CV and also drops the risk-free rate.
- ch 4 [low] Exam traps, fourth bullet: "A Gini of 0.372 is a proportion, not 37.2%, unless a percentage is asked" reads as if 37.2% were a different quantity. A proportion and its percentage are the same value, so a student may conclude 0.372 must never be written as 37.2%.
- ch 4 [low] Section 3, Karl Pearson's coefficient: The two forms are joined with "=", but (mean − mode)/SD = 3(mean − median)/SD is an empirical relation that holds only for moderately skewed distributions (it comes from mode ≈ mean − 3(mean − median)), not an exact identity for every distribution.
- ch 4 [low] Section 2, Gini interpretation: The text says G = 1 means one household takes all, but the given grouped formula can never reach 1 with a finite number of groups: with n equal groups its maximum is 1 − 1/n, for example 0.8 with five groups.
- ch 5 [low] Section 4 and Section 3 (notation): The symbol ρ is used twice with different meanings: in Section 3 it is the population correlation coefficient estimated by r, and in Section 4 it is Spearman's rank correlation. A student reading the t-test paragraph and then the rank formula will think the two ρ's are the same quantity.
- ch 5 [low] Section 4, concurrent deviation formula: The symbol n in r_c = ±√(±(2C − n)/n) is never defined, and C is described loosely. With N original observations there are only N − 1 successive changes, so n is not the number of data pairs.
- ch 5 [low] Section 4 (tie correction) and worked example step 8: Adding Σ(m³ − m)/12 to Σd² is a widely taught approximation, but the chapter presents it as the exact formula, and the exam trap treats 0.70 as the only correct value. The exact tie-corrected rank coefficient for these data is about 0.74.
- ch 6 [low] Section 3 and quiz Q4: The regression-to-the-mean sentence 'the predicted y lies closer to ȳ than x lies to x̄' compares a distance in y-units with a distance in x-units. Taken literally it is false: if y varies far more than x (σy much larger than σx) the predicted y can sit numerically further from ȳ than x sits from x̄. The true statement is about standard-deviation units.
- ch 6 [low] Section 3 and quiz Q4: 'The slope is less than the perfect-line slope' uses the term 'perfect-line slope' without ever defining it. A student cannot tell what number is being compared, and 'less than' is ambiguous for negative slopes.
- ch 7 [low] Section 2, repeated in Exam traps and Quiz Q2: The phrase 'R² always rises ... because least squares can always set its coefficient to zero' is self-contradictory: if the coefficient were set to zero the residual sum would be unchanged, so the stated reason explains only why R² does not fall. Least squares also does not 'set' a coefficient; it estimates it by minimising the residual sum. Standard texts say R² never decreases, rising or staying the same.
- ch 7 [low] Worked example 1 (model setup and part b): The fitted model logit p = −4 + 0.05 × income makes the default probability rise with income (positive sign), which is backwards for a bank, and it gives a 50% default probability at ₹80,000 income. A student may take the sign as a rule rather than an invented example.
- ch 7 [low] Section 3, first formula box: 'p is the probability of success' is ambiguous here, because the running example is a default, which most readers would call a failure.
