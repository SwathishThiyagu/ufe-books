# m-prob-u3: free-model run

- Book: `books/common/m-prob/m-prob-u3.html`
- Status: ok
- Model calls so far: 23 (88,010 tokens in, 179,368 out), 4.4 minutes

## Checker

```
m-prob-u3.html: 7 chapters, 12415 words, 8 figures, 137 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, paragraph on shape: The sentence reads "If p0.5 it has a longer left tail." The comparison sign has been lost, so the sentence states no condition, and as printed it also leaves out the rule for p<0.5 — which is exactly the case (p=0.2) used in the worked example and quiz. A student would carry away a wrong or empty skew rule.
- ch 1 [low] Section 1, second paragraph: "point binomial" is normally the name for the single-trial Bernoulli distribution, not for Bin(n, p). Listing it as another name for the binomial count can confuse a student who meets the term elsewhere.
- ch 1 [low] Figure, node b note: The note "success = fail" reads like a contradiction on its own: it means the trial's "success" is defined as a failed payment, but the wording does not say so.
- ch 2 [high] Section 3, the sentence justifying the addition rule: It says adding counts works 'because the probabilities multiply: e^−λ₁ e^−λ₂ = e^−(λ₁+λ₂)'. That product is only P(X=0 and Y=0), i.e. the k=0 case. For general k, P(X+Y=k) = Σ P(X=i)P(Y=k−i), not P(X=k)P(Y=k). As written, a student will conclude the sum distribution is found by multiplying individual probabilities, which is false.
- ch 2 [low] Quiz Q2, answer: 'The binomial coefficient factor tends to 1/k!' is loosely worded: C(n,k) itself grows without limit, so a student may write C(n,k) → 1/k! in an exam and lose marks. It is the combination C(n,k)p^k that tends to λ^k/k!.
- ch 3 [high] Section 1 (sum of pmf), Section 2 (pattern probability and Y pmf), Section 3 (proof), Exam trap 1, Q1 answer, Q7 answer: Exponents are written without <sup> tags, so the displayed text reads as multiplication. For example '(1 − p)k − 1p', '(1 − p)yp', 'pr − 1(1 − p)k − r', 'P(T > m) = (1 − p)m and P(T > m + n) = (1 − p)m + n; their ratio is (1 − p)n' all say something mathematically false when read literally. A student copying these will get wrong formulas.
- ch 3 [low] Section 1: The summation 'Σk=1∞ (1 − p)k − 1 p = 1' has its limits run together with the summand, which is hard to read on a phone screen.
- ch 3 [low] Lead: Listed among the uses: 'call-centre arrivals'. Arrivals in a call centre are normally modelled as Poisson counts; the geometric and negative binomial describe waiting for successes in trials, not arrival counts, so the example does not fit the chapter's theme and may mislead.
- ch 4 [high] Exam traps, second bullet: The relation is broken: 'P(X ≤ c) = P(X  c)' has a missing symbol, so the sentence reads as nonsense and students cannot tell which inequality is meant. The whole point of the bullet is that the two probabilities agree.
- ch 4 [low] Figure: The caption and figure text say the strip from 0 to 3 minutes is shown with area 0.3, but the plot spec draws only the full rectangle; no shaded 0-to-3 strip appears, so the caption describes something the reader cannot see.
- ch 4 [low] Section 3: It says simulation 'is not developed here', but the Beyond section then develops inverse transform sampling with uniform draws. The two statements pull against each other.
- ch 5 [low] Section 3, uniform bus comparison: The average remaining wait is wrong. If the bus is uniform on [0, 10] minutes and 9 minutes have passed, the remaining wait is uniform on [0, 1], so the mean remaining wait is 0.5 minutes, not 1 minute. The sentence says "1 minute on average".
- ch 5 [low] Exam traps, first bullet: The quoted slip does not match the described mistake. Using the mean 2 as if it were the rate gives λ = 2 and hence e^(−2×3) = e^(−6), not e^(−3). A student reading this may be confused about which wrong number the error produces.
- ch 6 [low] Quiz Q6: The answer says P(X≤45) "includes the whole block at 45", then says using 45.5 "includes half the block that would otherwise be missed". Read together the two sentences look contradictory, and a student may think the correction adds only half of the mass at 45 rather than the whole block (44.5 to 45.5).
- ch 7 [high] Figure caption: The caption says 'the Weibull starts lower and rises later'. For Weibull(2,1) the density near 0 behaves like 2t, while Gamma(2,1) behaves like t, so the Weibull is actually the highest of the three at small t (0.198 against 0.090 for gamma and 0.0002 for log-normal at t = 0.1). The Weibull also peaks earliest, at t = 1/√2 ≈ 0.707, while gamma peaks at t = 1 and log-normal at about t = 0.779. The sentence reverses the shapes.
- ch 7 [high] Figure (plot spec): The y-axis maximum is 0.7, but the Weibull(2,1) density reaches about 0.858 at t ≈ 0.707 and Log-normal(0,0.5) reaches about 0.904 at t ≈ 0.779. Every sampled point above 0.7 has been dropped, so both plotted curves have gaps (Weibull jumps from x = 0.39 to x = 1.07, log-normal from x = 0.54 to x = 1.12) and their peaks are missing. The picture therefore shows the wrong shape for two of the three densities.
- ch 7 [low] Lead and Sections 1-3: The lead says all three distributions are defined on t > 0, but Sections 1 and 2 write t ≥ 0, and here 0 is genuinely in the support of the gamma and Weibull (the density is 0, finite or infinite at t = 0 depending on k or β). Only the log-normal excludes 0.
