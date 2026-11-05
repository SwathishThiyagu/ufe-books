# c-ml-u4: free-model run

- Book: `books/cse/c-ml/c-ml-u4.html`
- Status: ok
- Model calls so far: 44 (153,954 tokens in, 172,704 out), 7.8 minutes

## Checker

```
c-ml-u4.html: 9 chapters, 11412 words, 10 figures, 148 KB
OK
```

## For the reviewer

- chapter 3: a python program's shown output was replaced by its real output; check the text around it
- chapter 3: a python program prints
Merge {'A'} and {'B'} at 10
Merge {'C'} and {'D'} at 12
Merge {'B', 'A'} and {'D', 'C'} at 15
but the chapter shows
Merge {'A'} and {'B'} at 10
Merge {'C'} and {'D'} at 12
Merge {'A', 'B'} and {'D', 'C'} at 15
Make the shown output and any explanation match what the program really prints
- chapter 8: a python program's shown output was replaced by its real output; check the text around it
- chapter 6: a python program's shown output was replaced by its real output; check the text around it
- chapter 1: give 6 to 8 quiz questions
- chapter 1: the figure cannot be drawn: label "Agglomerative" is too long for its box; use a shorter label
- chapter 4: a python program's shown output was replaced by its real output; check the text around it
- chapter 7: worked example 1: the example's "check" code failed: Traceback (most recent call last):
  File "/tmp/tmpd3mpusjc/check.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
- chapter 5: worked example 1: the example's "check" code failed: Traceback (most recent call last):
  File "/tmp/tmp3r683l53/check.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
- chapter 9: a python program does not run (runtime error: Traceback (most recent call last):
  File "/tmp/tmpxkm2z5l2/p.py")
- chapter 9: a c program's shown output was replaced by its real output; check the text around it
- chapter 9: worked example 1: the example's "check" code failed: Traceback (most recent call last):
  File "/tmp/tmpz89pwgvz/check.py", line 13, in <module>
    denom = sum((dist[j]/dist[k])**(2/(m-1)) for k in range(2))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/tmpz89pwgvz/check.py", line 13, in <genexpr>
    denom = sum((dist[
- chapter 9: a python program does not run: runtime error: Traceback (most recent call last):
  File "/tmp/tmpxg1vkcrc/p.py", line 14, in <module>
    denom = sum((dist[j]/dist[k])**(2/(m-1)) for k in range(2))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/tmpxg1vkcrc/p.py", line 14, in <genexpr>
    denom = sum((dist[j]/dist[k])**(2/(m-1)) for k in range(2))
                      ^
NameError: name 'j' is not 

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, description of model‑based family: Fuzzy C‑means is listed under the model‑based family, but it is a soft (fuzzy) partitioning method, not a probabilistic mixture‑model approach.
- ch 1 [high] Venn diagram specification: The Venn diagram states that fuzzy clustering belongs to both the model‑based and partitioning families, which contradicts the correct classification of fuzzy C‑means as a soft partitioning method.
- ch 2 [high] Section 2, after the worked example: The text says “The SSE after the first iteration is 30 (see the figure).” The calculated sum of squared errors after the first iteration (using the new centroids (3, 2.5) and (6.25, 6.5)) is 78.75, not 30. The figure shows SSE = 30 after the third iteration, not after the first.
- ch 2 [low] Section 1, objective function definition: The formula is written as Σ ‖xᵢ‑cⱼ‖² without specifying the summation index. This can be confusing because the sum should be over each data point i to its assigned centroid c_{a(i)}.
- ch 3 [high] Section 1, average linkage formula: The description defines |C_i| as the number of points in cluster C_i but does not define |C_j|, which appears in the denominator.
- ch 3 [low] Section 1, average linkage formula: The formula uses LaTeX syntax "\frac" which is not allowed by the allowed inline tags.
- ch 3 [low] Section 2, bullet on efficient implementations: The statement "Efficient implementations use priority queues to achieve O(n² log n)" is not the tightest known bound; many implementations achieve O(n²).
- ch 3 [low] Quiz Q5 answer: The explanation suggests that averaging completely removes the effect of outliers, which is slightly overstated.
- ch 4 [high] Quiz Q4: The responsibility values given (γ_{11}=0.9997, γ_{12}=0.0003, etc.) are incorrect for the described data and parameters.
- ch 4 [low] Worked example code: The variable `sigma2` is defined but never used, which may confuse readers.
- ch 4 [low] Section 1: The mixture density is denoted as L(x), which can be confused with the likelihood function.
- ch 5 [high] Worked example 1, step 4: The second eigenvalue is given as λ₂ = 0.0, which is incorrect. For the covariance matrix [[1.333, -0.667], [-0.667, 1.333]] the eigenvalues are λ₁ ≈ 2.0 and λ₂ ≈ 0.666 (2/3).
- ch 5 [high] Quiz Q3: The answer states the first eigenvalue of [[4,2],[2,3]] is 4, but the correct eigenvalues are (7 ± √17)/2 ≈ 5.56 and 1.44.
- ch 5 [high] Exam traps: The trap claims the second eigenvalue is exactly zero because of the symmetric arrangement, which contradicts the corrected eigenvalue (≈0.666).
- ch 5 [low] Section 2, step 2: The expression “Z = X – μ” may be unclear to students that μ is subtracted from each row (sample).
- ch 5 [low] Section 3, reconstruction statement: The sentence “When k = d, reconstruction is exact because Y W_k^T + μ = X.” does not explain that Y = Z W_k, which justifies the equality.
- ch 6 [high] Section 1, Pearson correlation formula: The formula for Pearson correlation coefficient is missing the division by the number of samples (N) or (N‑1). It should be r = Σ (x_i‑μₓ)(y_i‑μ_y) ÷ ((N‑1) σₓ σ_y) for the sample version.
- ch 6 [high] Section 2, description of forward selection (wrapper): Forward selection is said to have a cost that “grows combinatorially with the number of features”. In reality forward selection evaluates at most d + (d‑1) + … + 1 ≈ d²/2 models, i.e., quadratic, not combinatorial (exponential).
- ch 6 [low] Figure spec (nested sets): The nested‑set description is inconsistent: the inner set is labelled “Discarded” but contains items that are not a subset of the middle “Selected” set, contradicting the nesting.
- ch 6 [low] Section 1, variance formula: Variance is given as Σ (x_i‑μ)² ÷ N, which is the population variance. For a sample of data the unbiased estimator uses N‑1.
- ch 7 [high] Section 2, within‑class scatter for Class A: Only one outer‑product is shown (0.25 matrix) instead of the sum of the two points. The within‑class scatter for A should be the sum of the outer products of both deviations.
- ch 7 [high] Section 2, within‑class scatter for Class B: Same mistake as for Class A. Only one outer‑product is shown.
- ch 7 [high] Section 2, total within‑class scatter matrix S_W: S_W is given as [[0.5,0.5],[0.5,0.5]] which is only one class’s scatter. With both classes it should be doubled.
- ch 7 [high] Section 2, inversion of regularised S_W: The inverse is computed for the wrong S_W (the 0.5 matrix) and the numeric values are off. With the correct S_W = [[1,1],[1,1]] and ε = 1e‑4, the regularised matrix is [[1.0001,1],[1,1.0001]] and its inverse is approximately [[5000,‑5000],[‑5000,5000]].
- ch 7 [low] Section 2, duplicate "Worked example 1" block: The same example is repeated after the main worked example, and a stray placeholder "dry run: {'head': [], 'rows': []}" appears, which may confuse readers.
- ch 7 [low] Quiz Q3 answer: The answer states w = (1,1) after ignoring scale, but the computed vector is (‑1,‑1). Both are correct up to sign, but the explanation should mention that the direction can be either sign.
- ch 8 [high] Section 1, DB bullet: The statement "DB works only with numeric features and Euclidean distance" is too restrictive. The Davies‑Bouldin index can be computed with any distance metric; Euclidean is common but not required.
- ch 8 [high] Section 1, DB formula: The formula for DB omits the condition that the maximum is taken over clusters j ≠ i. Without this, the term (S_i + S_i) / M_ii would involve division by zero.
- ch 8 [low] Section 3, choosing K bullet: The phrase "K = 2 to K = max (e.g., 10)" is unclear because "max" is not defined.
- ch 9 [high] Section 2 – Python code: The membership calculation uses an undefined variable j and computes the same value for both clusters, so the code raises a NameError and would give wrong memberships.
- ch 9 [high] Figure after Python code: Edge labels show memberships 0.8/0.2 for point 1 and 0.1/0.9 for point 5, but point 1 is exactly at centroid c₁ and point 5 at centroid c₂, so their memberships should be (1, 0) and (0, 1) respectively.
- ch 9 [high] Worked example 1 – steps 6 and 7: Centroid values are computed incorrectly as 115.3 and 334.7; the correct centroids after one iteration are about 123.8 and 326.2 (matching the program output).
- ch 9 [low] Section 1 – formulation: The statement "All memberships for a point sum to one: Σ_j u_{ij}=1" does not explicitly mention that the sum is taken for each data point i.
- ch 9 [low] Worked example on a line – square memberships table: The index "u₃₁²" and "u₃₂²" refer to the third data point, which is x=4, but the notation may confuse readers who expect the third point to be x=3.
