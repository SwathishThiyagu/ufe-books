# c-ml-u2: free-model run

- Book: `books/cse/c-ml/c-ml-u2.html`
- Status: ok
- Model calls so far: 27 (95,369 tokens in, 95,312 out), 4.8 minutes

## Checker

```
c-ml-u2.html: 7 chapters, 9908 words, 8 figures, 131 KB
OK
```

## For the reviewer

- chapter 7: a c program's shown output was replaced by its real output; check the text around it

## Reviewer notes (after any revision)

- ch 1 [high] Exam traps bullet 1: The statement says that omitting the intercept forces the line through the origin and gives a slope of –1200 ₹/month for the data. For the given data the slope through the origin is +667 ₹/month, not negative and not –1200.
- ch 1 [high] Exam traps bullet 2: The bullet claims that swapping numerator and denominator in the slope formula yields a tiny slope of –0.025. The correct swapped value is 40 ÷ (‑40000) = –0.001, not –0.025.
- ch 1 [low] Assumptions of ordinary least squares section: The text says that violating the assumptions can lead to “biased or inefficient estimates.” Violation of homoscedasticity leads to inefficient (but still unbiased) estimates, while violation of linearity or exogeneity can cause bias.
- ch 2 [high] Quiz Q8: The answer says that halving the learning rate does not change the variance of the SGD update. In fact, the variance of the parameter update scales with the square of the learning rate, so halving η reduces the variance by a factor of ¼.
- ch 2 [low] Section 1: The sentence "A negative gradient means the loss decreases if w is increased, and vice‑versa" can be misread.
- ch 3 [low] Section 2, likelihood expression: The likelihood is written as “pⁿʸ (1‑p)¹⁻ʸ”, which is a formatting error and can be misread.
- ch 3 [low] Section 2, loss formula: The loss formula uses log without specifying the base. Students may wonder whether it is natural log or log₂.
- ch 3 [low] Section 3, one‑vs‑rest explanation: The sentence “The approach works because probabilities are comparable across classifiers.” is misleading; probabilities from independent binary classifiers are not automatically calibrated relative to each other.
- ch 3 [low] Quiz Q5: The answer suggests lowering the threshold to meet a false‑negative rate requirement, but does not mention that the actual rate must be evaluated on validation data and that threshold selection is a design choice.
- ch 4 [high] Section 3 (Relation to the perceptron algorithm): The text says that a closed‑form least‑squares solution can replace the perceptron update. Least‑squares gives a regression solution and is not a standard optimizer for binary classification with the perceptron loss; it can produce poor classification performance and is not equivalent to a perceptron update.
- ch 4 [low] Worked example 1: The description says "weight vectors (including bias b=0)" which is inaccurate because the bias is a separate scalar, not part of the weight vector.
- ch 4 [low] Section 1 (Binary linear discriminant) – bullet list: Bullet "Only linear boundaries can be learned" is overly restrictive; linear classifiers can learn non‑linear decision boundaries after applying a feature mapping.
- ch 5 [low] Section 1 (Error decomposition): The true function f(x) is used in the bias definition but never defined, which may confuse students.
- ch 5 [low] Lead: Bias is described as "average prediction of the model" without stating that the average is over many possible training sets.
- ch 5 [low] Quiz Q7: Cross‑validation is presented as a method that directly reduces variance, which is not precise.
- ch 5 [low] Quiz Q3: The answer rounds Bias² to 3.33 without stating the rounding rule, which could lead to inconsistency.
- ch 6 [high] Section 2 (Ridge regression): The ridge loss is written with a (1/n) factor but the closed‑form solution ŵ = (XᵀX + λ I)⁻¹ Xᵀy omits the corresponding n·λ term. With the loss as given, the correct solution is ŵ = (XᵀX + n·λ I)⁻¹ Xᵀy.
- ch 6 [high] Worked example 1 (used‑car price model): The example states that the training data have been standardised, yet it treats the raw age = 3 and mileage = 40 (thousands of km) as if they were already standardised. This contradicts the standardisation step and gives a misleading prediction.
- ch 6 [low] Section 1 (The idea of penalising coefficients): The sentence "In ordinary least squares we minimise the mean‑squared error (MSE)" is slightly inaccurate; OLS traditionally minimises the sum of squared errors, not the mean.
- ch 6 [low] Section 2 (Ridge regression) bullet list: It does not mention that the intercept term is typically left unpenalised when standardising features.
- ch 6 [low] Section 3 (Lasso regression) bullet list: The step "Initialize all w_j to zero" could be clarified that the intercept is usually initialised separately and not penalised.
- ch 7 [high] Section 3, bullet point "Select the candidate with the smallest metric": The statement is true for error metrics (e.g., RMSE, MAE) but false for score metrics (e.g., accuracy, F1). It can mislead students to pick the wrong model for classification tasks.
- ch 7 [low] Section 2, sentence "Some syllabi label these as \"evaluation metrices\"": Typographical error: "metrices" is misspelled.
- ch 7 [low] Exam traps, bullet "In leave‑one‑out CV, the computation time grows linearly with n": The description is misleading. LOOCV requires training a model n times, so the total cost grows roughly proportional to n times the cost of training on n‑1 samples, which can be O(n²) for many algorithms.
