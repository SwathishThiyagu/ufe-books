# c-ml-u4: free-model run

- Book: `books/cse/c-ml/c-ml-u4.html`
- Status: problems
- Model calls so far: 24 (85,308 tokens in, 186,879 out), 4.4 minutes

## Checker

```
c-ml-u4.html: 9 chapters, 14834 words, 10 figures, 167 KB
PROBLEMS:
 - page is wider than the screen at 390px (406>390): a table, figure or long word overflows
```

## For the reviewer

- checker: page is wider than the screen at 390px (406>390): a table, figure or long word overflows

## Reviewer notes (after any revision)

- ch 1 [low] Section 3, density-based bullet: The sentence 'Some syllabi list DBSCAN as density-based' is circular: DBSCAN is density-based by definition, not a syllabus variation. A student may think the classification is optional or disputed.
- ch 1 [low] Figure caption and spec: The caption says clustering 'branches into four families', but Section 3 gives three axes with six values (partitional, hierarchical, hard, soft, density-based, model-based). Hard and model-based are missing from the figure, so the caption and the text do not match.
- ch 1 [low] Worked example 1, step 5: The distance is computed on raw spend in rupees and visits together, which Section 2 warns is meaningless: 300 + 1 adds rupees to visits, and the Euclidean value 300.00 is just the rupee gap. Nothing in the worked example says the result is only illustrative.
- ch 1 [low] Section 3, cross-references: 'See hierarchical clustering', 'See fuzzy clustering' and '(see evaluation)' are plain text, so a reader on a phone cannot jump to those chapters.
- ch 2 [high] Section 3, bullet on choosing k: The sentence 'silhouette is another name you will meet in Chapter 4.8' reads as if silhouette is just another name for the elbow method. Silhouette is a different criterion (a per-point score based on within-cluster and nearest-other-cluster distances), not a synonym for the elbow plot.
- ch 2 [low] Quiz Q4: The question says two runs on the same data. The second reason given, different feature scaling or distance choice, changes the data or the algorithm, not just the run, so it does not answer the question asked. Only the initialisation reason actually applies.
- ch 3 [high] Section 3, dendrogram description: It says p8 and p9 join at height 4. In the five-point example the p8-p9 merge happens at height 1 (d(8,9)=1); height 4 is the final merge where {1,2,4} joins {8,9}. A student would read the merge order wrongly.
- ch 3 [high] Figure caption and the figure's aria text: The caption says 'the p8-p9 pair joins at height 4' and the aria text says 'joins the p8-p9 pair at height 4'. Wrong: the p8-p9 pair joins at height 1. Height 4 is where that pair joins the group {1,2,4}. The tree spec itself (node label '1' for the p8-p9 node, root label '4') is right, so the picture and its caption contradict each other.
- ch 3 [low] Worked example 1, dry run table: The table has three numbered rows, but the example states there are four merges (n − 1 = 4). Row 1 packs two separate height-1 merges into one line, so the merge numbering does not match step 6 (heights 1, 1, 2, 4).
- ch 4 [high] Quiz Q7: The premise is impossible. A component with two distinct points cannot have its variance go to 0: its maximum-likelihood variance is (x₁ − x₂)²/4, which is positive, so the likelihood stays finite. The singularity needs a component that is responsible for a single point (or several identical points).
- ch 4 [low] Worked example 1, opening line: 'σ12 = σ22 = 1' reads as σ₁₂ = σ₂₂ because the superscripts are missing, while the rest of the line uses σ₁², σ₂². A student can misread which quantity is fixed.
- ch 4 [low] Section 2, bullet list: The three M-step parameter formulas (πk, μk, Σk) are placed after the log-likelihood/stopping bullet, so a reader can think they belong to the stopping step rather than to the M-step.
- ch 5 [low] Section 2, orthogonality sentence: "Because C is symmetric, its eigenvectors are orthogonal" is not automatic: it is true for eigenvectors of different eigenvalues, and when an eigenvalue repeats, any vector in that eigenspace is an eigenvector, so the orthogonal set has to be chosen. A student may think orthogonality is free in every case.
- ch 5 [low] Quiz Q2, answer: Before centring, the matrix formed is the second-moment matrix XᵀX/(n−1), not a covariance matrix; the phrase "the covariance includes offsets from zero" mixes the two and hides the cause: the mean vector is not removed.
- ch 5 [low] Exam traps, standardisation trap: "A feature measured in rupees can dominate a feature measured in metres only because its variance is larger" reads as if the larger variance were independent of the unit; the point is that the unit itself inflates the variance.
- ch 5 [low] Section 3, SVD paragraph: The SVD statement does not say that X must be the mean-centred matrix; with an uncentred X, s_i²/(n−1) are eigenvalues of the second-moment matrix, not of the covariance matrix.
- ch 6 [low] Section 2, first paragraph: "compute it in two directions" is vague; students may read it as direction of the sign rather than two kinds of pairs.
- ch 6 [low] Worked example 1, step 3: The redundancy check only tests the pair X1–X3. The other two pairs are given in the figure (r(X1,X2)=0.10, r(X2,X3)=−0.05) and are never checked, so the example does not show a complete redundancy scan.
- ch 6 [low] Section 1 (target example) and Section 2: The section says correlation is for numeric variables, but the target example is loan default, which is a 0/1 class. A student may think Pearson r cannot be used at all with a binary target.
- ch 6 [low] Section 3, last paragraph of embedded methods: "See Unit 2, Regularization: ridge and lasso." is plain text, so the cross-chapter pointer does not work the way chapter links do in this book.
- ch 7 [high] Section 2 (rank argument) and Quiz Q3: The justification is mathematically wrong as written: a sum of C rank-one matrices can have rank up to C, not C−1. The bound C−1 comes from the weighted constraint Σ_c n_c (μ_c − μ) = 0, which the text never states. A student who copies 'a sum of C rank-one matrices, so rank ≤ C−1' writes a false statement.
- ch 7 [low] Worked example 1, steps 2–3: Section 1 defined S_B = Σ_c n_c (μ_c − μ)(μ_c − μ)ᵀ, but the example silently uses S_B = (μ2 − μ1)(μ2 − μ1)ᵀ. The two differ by the positive factor n1n2/n, which does not change the eigenvector, but the switch is not explained and can confuse a reader checking the formula.
- ch 7 [low] Worked example 1, step 7: The arithmetic does not match the rounded vector: 0.71×4 + 0.71×4 = 5.68, not 5.66.
- ch 7 [low] Section 3, first paragraph: 'LDA is a projection, not a full classifier by itself' contradicts the same paragraph's later mention of 'the simple LDA classifier'. Two different objects are being described with one name.
- ch 7 [low] Section 1, scatter matrix description: 'S_W is d×d; a large value means a class is wide' — a matrix has no single value, so the sentence is unclear about what is being compared.
- ch 8 [low] Section 1 table and Section 2, adjusted Rand index rows: The table gives the ARI range only as "≤1" and Section 2 says "0 means random, 1 is perfect". A student may conclude ARI can never be negative. ARI can go below 0 (down to about −0.5 for random labelings), which signals agreement worse than chance.
- ch 8 [low] Section 1, silhouette definition: a(i) is defined as the mean distance to the other points in its own cluster, which has no value when a cluster holds a single point. The chapter never says what to do in that case, so students hit an undefined term.
- ch 8 [low] Section 2, purity paragraph: The sentence 'It rises easily when k is large' is stated without saying why, which readers may misread as a rule about k rather than a counting effect.
- ch 9 [low] Section 1 and Figure caption: The example memberships 0.90 and 0.10 do not follow from the stated facts alone. They are only correct for fuzzifier m = 2, and m is not given here (it appears later, in the worked example). A student who tries to check the numbers cannot reproduce them from this section.
- ch 9 [low] Section 1, sentence 'Here c is the number of clusters, and ck is centre k.': The centre symbol c_k is defined here before it is used, and it clashes with c, the number of clusters, used in the same line. A reader can misread 'ck is centre k' as a formula involving c times k.
- ch 9 [low] Figure spec: The node x=1 is drawn at height y=2 while both centres sit at y=0, so the picture shows distances √5 and √13, yet the edge labels say d=1 and d=3. The drawing contradicts its own labels.
