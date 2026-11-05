# c-ml-u3: free-model run

- Book: `books/cse/c-ml/c-ml-u3.html`
- Status: ok
- Model calls so far: 42 (147,479 tokens in, 159,182 out), 8.0 minutes

## Checker

```
c-ml-u3.html: 9 chapters, 13148 words, 10 figures, 154 KB
OK
```

## For the reviewer

- chapter 1: a python program's shown output was replaced by its real output; check the text around it
- chapter 4: give 6 to 8 quiz questions
- chapter 2: a c program's shown output was replaced by its real output; check the text around it
- chapter 8: a python program's shown output was replaced by its real output; check the text around it
- chapter 8: worked example 1: the worked example states [0.111, 0.333] but recomputing it gives [0.5493061443340549, 0.16666666666666666, 0.16666666666666666, 0.5000000000000001, 0.16666666666666666, 0.8047189562170503, -1.0]; fix the steps and the answer so they match the correct values
- chapter 5: a python program's shown output was replaced by its real output; check the text around it
- chapter 6: a python program's shown output was replaced by its real output; check the text around it
- chapter 6: a c program's shown output was replaced by its real output; check the text around it
- chapter 7: a python program's shown output was replaced by its real output; check the text around it

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, algorithm description: The text says "Some syllabi refer to the same method as CART or C4.5; the core idea of greedy information‑gain selection is common to all." This is incorrect because CART typically uses the Gini impurity (or sometimes entropy) and does not base splits on information gain. Equating CART with information‑gain selection misrepresents the algorithm.
- ch 1 [high] Section 3, applied example (Outlook gain): The example concludes that ID3 would choose Outlook as the root attribute because its gain is positive. In this data set, other attributes (e.g., Temperature) have a much larger information gain (~0.571 bits) than Outlook (0.020 bits). Therefore Outlook is not the best attribute and the statement is factually wrong.
- ch 2 [high] Worked example 1 (question and solution): The example says “Assuming a uniform prior for θ, compute the MAP estimate” but then uses Laplace smoothing (θ̂ = (h+1)/(n+2)). A uniform prior (Beta(1,1)) gives MAP = MLE = h/n = 0.7, not 0.667.
- ch 2 [high] Worked example 1, step 3 explanation: It states “(h+1)/(n+2)=0.8”, which is numerically wrong; (7+1)/(10+2) = 8/12 ≈ 0.667.
- ch 2 [high] Worked example 1, discussion of Laplace smoothing: The text claims “the Laplace rule corresponds to a Beta(1,1) prior and gives (h+1)/(n+2)=0.8”. This is incorrect: Laplace smoothing corresponds to adding one pseudo‑count, i.e., a Beta(2,2) prior, and the MAP formula is (h+1)/(n+2). For a Beta(1,1) prior the MAP equals h/n.
- ch 3 [high] Worked example 1 (code and step 1): Prior probabilities are computed from total word token counts (100 and 200) instead of from the number of documents in each class. Naive Bayes priors must be based on class frequencies of documents, not on token counts.
- ch 3 [high] Quiz Q3: The answer for P(feature|negative) uses the count of false occurrences (2) instead of the count of true occurrences. With "false in 2 out of 20 negative examples", the true count is 18.
- ch 3 [high] Worked example 1 (code variable naming): Variable names P_spam and P_ham suggest they hold class priors, but the values are derived from token totals, which is conceptually wrong and may confuse students.
- ch 3 [low] Section 3, practical tip: Statement "Scale numeric features before using Gaussian NB" is not strictly necessary; Gaussian NB models each feature with its own mean and variance.
- ch 3 [low] Section 3, Gaussian formula description: Phrase "mean and variance of feature xᵢ in class Cⱼ" could be misread as the mean/variance of the whole class.
- ch 3 [low] Section 1, bullet point on high‑dimensional data: Mentions computing the product in log space but does not explain why.
- ch 4 [low] Lead: The sentence "It gives the lowest possible error for any classifier that uses the same posterior" is vague. The Bayes optimal classifier is optimal with respect to the posterior predictive distribution, not merely any classifier that happens to use the same posterior.
- ch 4 [low] Section 1: The phrase "picking the majority class" may be misread as counting the number of hypotheses that predict each class, rather than selecting the class with highest posterior predictive probability.
- ch 4 [low] Section 2: The description "approximates Bayesian model averaging without computing the full weighted vote" suggests that a single draw gives a good approximation, which is misleading. A single draw is a stochastic classifier; many draws are needed to approximate the average.
- ch 4 [low] Section 2, formula explanation: The term "true distribution" in the definition of err(h) is not defined, which may confuse students.
- ch 5 [high] Section 1, parameter count statement: The claim that a network with n binary variables and at most two parents per node needs only about 3n numbers is inaccurate; the worst‑case number of independent parameters is 4n (each node may need 2^k parameters with k ≤ 2, i.e., up to 4 per node).
- ch 5 [low] Figure description: It says “CPT values used in the example are attached to the edge,” but CPTs are associated with the child node, not the edge.
- ch 5 [low] Bullet list after Section 1: The bullet “Joint = product of CPTs” oversimplifies; the joint distribution is the product of conditional probabilities, which are represented by the CPTs.
- ch 5 [low] Section 3, step 1 of variable elimination: The step says to list factors that involve the query variable Q and the evidence variables E only, omitting hidden variables that also appear in CPTs.
- ch 6 [high] Section 2, voting example description: The text says "using weight 1/d makes the two Class B neighbours (distances 1.0 and 2.0) outweigh the single Class A neighbour (distance 2.236)". The actual distances for the plotted points are 1.414, 1.414 and 2.000, not 1.0, 2.0 and 2.236.
- ch 6 [high] Worked example 1, C code: The selection of the three smallest distances uses an out‑of‑bounds access (idx[j] where j can be 3,4,5) and does not correctly keep the three nearest indices.
- ch 6 [high] Worked example 1, shown output: The printed weight for class B is shown as 1.414, but the correct sum of the two B weights (1/1.414 + 1/2.000) is about 1.207.
- ch 6 [high] Exam traps section: It states that "Using squared Euclidean distance (∑(x_i‑y_i)²) instead of the square root can change the neighbour order when dimensions have different ranges." This is false because the square‑root function is monotonic; the ordering of distances is identical for squared and unsquared Euclidean distance.
- ch 6 [low] Section 1, Euclidean distance explanation: The sentence "The square root keeps the distance in the same units as the original features, which matters when features have different scales" mixes two ideas: units and scale. The square root does not address scale differences.
- ch 7 [high] Worked example 1: The solution w = [1, 1], b = 0 does not satisfy the equality constraints (w·x₁ + b = 1 and w·x₂ + b = –1). The constraints are not tight, so the derived w is not the maximum‑margin solution. The margin formula used in the code (1/‖w‖) is the half‑margin, but the text later calls it the full margin, causing contradictory results (0.71 vs √2 ≈ 1.41).
- ch 7 [high] Exam traps: The statement "points with α_i = 0 lie exactly on the margin but are not support vectors" is incorrect. In a hard‑margin SVM points on the margin have α_i > 0 and are support vectors; points with α_i = 0 lie strictly outside the margin.
- ch 7 [high] Quiz Q3 answer: The answer computes the margin as 1/‖w‖ ≈ 1.41 but earlier the chapter defines margin as the full distance between the two margin lines (2/‖w‖). This inconsistency misleads students.
- ch 7 [low] Section 2 description: The phrase "Only α_i > 0 correspond to support vectors" is missing the word "the" before "correspond" and could be clearer.
- ch 7 [low] Quiz Q4 answer: The polynomial kernel is written without the scaling factor γ and offset r that were introduced earlier, which may cause confusion.
- ch 8 [high] Worked example step 8 (normalization): Total weight after applying exponentials is calculated as 1.299, but the correct total is about 0.866 (0.1443*3 + 0.433).
- ch 8 [high] Worked example step 10 (weighted error ε₂): Mis‑classifications are described incorrectly; only sample 2 is mis‑classified, yet ε₂ is given as w₂ ≈ 0.111.
- ch 8 [high] Worked example step 11 (α₂ calculation): α₂ is computed as ≈1.0397 using ε₂ = 0.111, which is wrong.
- ch 8 [high] Answer summary after the worked example: Normalized weights after round 1 are reported as ≈0.111 and 0.333, contradicting the correct values (≈0.1667 and 0.5) and the code output.
- ch 8 [low] Section 1: Bagging: Bagging is described only for classification; no mention of its use for regression.
- ch 8 [low] Section 2: Random Forests: Only the classification default m = √p is given; the common regression default (m = p/3) is omitted.
- ch 8 [low] Section 3: Boosting (AdaBoost): The informal statement "w_j ← w_j · exp(±α)" is vague and may confuse students.
- ch 9 [high] Section 2, bullet point about weight normalisation: It states that weights must be normalised (divide by Σ w_i) to avoid scaling issues. In weighted least squares, multiplying all weights by a constant does not change the fitted coefficients, so normalising is unnecessary and the statement is misleading.
- ch 9 [high] Exam traps section, trap about raw Gaussian values: The trap claims that using raw Gaussian values without normalising by Σ w_i makes the fitted line too steep. This is incorrect because the regression solution is invariant to a common scaling of all weights; normalising does not change the fitted line.
- ch 9 [low] Section 1, step list for weighted linear regression: The step "Form the weighted design matrix Xᵀ W X" does not mention that the design matrix X must include a column of ones to model the intercept term.
