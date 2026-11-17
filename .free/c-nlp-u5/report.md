# c-nlp-u5: free-model run

- Book: `work/claude_figs/c-nlp-u5/tree/books/cse/c-nlp/c-nlp-u5.html`
- Status: ok
- Model calls so far: 26 (98,034 tokens in, 167,680 out), 4.8 minutes

## Checker

```
c-nlp-u5.html: 7 chapters, 13074 words, 8 figures, 157 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3 (smoothing), repeated in the bullet list: The chapter says add-one smoothing with idf(t) = log((N + 1) ÷ (df(t) + 1)) "avoids zero or infinite values". It does not avoid zero: when a term appears in every document, df = N, so (N + 1)/(N + 1) = 1 and idf = log(1) = 0, exactly as in the unsmoothed case. Smoothing only removes the blow-up for df very small or zero (and the division-by-zero risk), not the zero weight for an everywhere-term. A student will believe the smoothing fixes something it does not.
- ch 1 [low] Section 3, sublinear tf bullet: The chapter lists "log scaling" (tf = 1 + log(count)) and a separate "sublinear tf" (tf = count ÷ (count + k)). In standard NLP texts and in scikit-learn's sublinear_tf option, the name "sublinear tf" means tf = 1 + log(count). Giving the same idea two names and attaching the standard name to a different formula will confuse students who check the library documentation.
- ch 2 [low] Figure (Add-one Naive Bayes scores): The caption tells the reader to notice 'the smoothed zero count for good in the negative class', but the Counts node shows only the positive document (good1 film1). The negative document (bad film) and its counts never appear, so a student cannot trace where the negative score 0.04 and the smoothed 0.2 for good|neg come from.
- ch 2 [low] Section 3, closing comparison paragraph: 'Logistic regression gives calibrated probabilities' is stated as a fact. Calibration is not guaranteed: with sparse text features and few examples the weights can grow large and the probabilities become overconfident.
- ch 2 [low] Section 2, last sentence: The cross-reference 'Use the evaluation metrics in 5.3 to compare classifiers' is written as plain text, so it does not link to the next chapter for a reader on a phone.
- ch 3 [low] Section 3, ROC-AUC paragraph: The sentence 'It is threshold-free but still ignores class balance in the training data' attributes the weakness to the wrong place. AUC is computed from predicted scores on test items, and its known weakness is that it is insensitive to class imbalance — a model can score a high AUC while still missing most of the rare class. Training-set balance is not what AUC 'ignores'.
- ch 3 [low] Exam traps, 'Macro vs micro' bullet: 'A 90/10 imbalance makes micro close to accuracy' understates it. In single-label classification (each document has exactly one class) micro-averaged precision, recall and F1 are all exactly equal to accuracy, so micro gives no extra information under imbalance.
- ch 3 [low] Section 2, chi-square formula box: The chi-square test is quoted without its validity condition. On a 2×2 table built from a rare word, expected counts fall below about 5 and the χ² value becomes unreliable, which is exactly the case for the rare features feature selection is meant to filter.
- ch 3 [low] Figure aria description: '20 false spam' is ambiguous — it can be read as 20 spam messages that are false, whereas the cell is 20 ham emails wrongly marked spam.
- ch 3 [low] Section 1, TF-IDF bullet: 'See 5.1.' is plain text; in this book cross-references are links, so the reader on a phone cannot jump to the earlier chapter.
- ch 4 [low] Exam traps, fourth trap: It says film -2 and songs +3 "average to +1". The average of -2 and +3 is +0.5; +1 is their sum, so the wording is numerically wrong and a student may copy the wrong idea about averaging aspect scores.
- ch 4 [low] Worked example 1 (step 5 and answer), against Section 2: Section 2 states a rule that "but" halves the clause before it, but the worked example and Q3 switch the rule off ("treat but as neutral") without saying why, so one rule is taught and never applied. Also, the sentence "not good but excellent songs" never mentions a film, yet step 5 assigns film -2; the aspect target is asserted, not read from the text.
- ch 5 [high] Exam traps, trap 1 (also Section 1 first paragraph and worked example step 2): The chapter uses the word 'length' for two different things and the trap states the wrong one. It says a one-hot vector's length is |V|, but the Euclidean length (norm) of a one-hot vector is 1, which worked example step 2 correctly computes and the formula box uses (|a| = √(a·a)). |V| is the dimension, i.e. the number of entries. As written, the trap directly contradicts the worked example and the cosine formula, and a student cannot tell which value to substitute for |a| and |b|.
- ch 5 [low] Lead: 'The dense geometry can place cricket near bat and far from ball' is a bad illustration: cricket and ball are strongly related and co-occur constantly, so trained dense vectors put them close, not far apart. The example teaches the opposite of how distributional vectors behave.
- ch 5 [low] Exam traps, trap 4: It says to state whether you use U or UΣ 'before comparing by cosine'. Row w of U_k Σ_k is just row w of U_k multiplied by one scalar (its singular value), and cosine is invariant to per-vector scaling, so the choice cannot change any cosine. It only changes dot products and Euclidean distances.
- ch 5 [low] Section 2, LSA sentence: 'This use of SVD on word-context counts is latent semantic analysis (LSA)' does not match the standard definition: in most textbooks LSA is SVD applied to a term-document matrix (often weighted by tf-idf or log-entropy), and SVD on a word-word PPMI matrix is usually described as a count-based distributional embedding.
- ch 5 [low] Figure (table under Section 3): The one-hot rows have three cells while the dense rows have two, in a table whose title names only two dense columns. Two different vector spaces of different dimension are shown in one grid, so a student may read 0.8 as an entry in dimension 1 of a three-dimensional space, or think the dense vectors lost an entry.
- ch 6 [low] Section 1, negative sampling distribution; Section 2, weighting function: The exponents are printed without a superscript in two places: "Pn(w) ∝ count(w)0.75" and "f(x)=min(1,(x/xmax)0.75)". Read literally this looks like multiplication by 0.75, not a power, and a student copying the formula will get it wrong.
- ch 6 [low] Section 2, second paragraph: "GloVe uses these counts once, not a stream of windows" can be read as saying training makes a single pass. It does not: the count matrix is built once, but gradient descent then sweeps over its nonzero entries many times (later in the same section you say training runs gradient descent on the nonzero entries).
- ch 6 [low] Section 1, symbol list: The letter V names two different things: the matrix of output vectors ("output vectors V, with row vw") and the vocabulary in the softmax denominator and later formulas. The same symbol with two meanings confuses students reading the formula.
- ch 6 [low] Figure and Section 4 example: The toy coordinates make king = man + woman, and the figure labels the man→king arrow "woman" and the woman→queen arrow "woman". The arithmetic is consistent, but a student may take away the false rule that adding the woman vector to man gives king, and the arrow labels carry no stable meaning (the same label appears on two arrows with different positions).
- ch 7 [low] Section 4, purity formula and text: "Purity ranges from 0 to 1" is loose: with non-empty clusters purity can never fall to 0. It is bounded below by 1/(number of gold classes), because every cluster contributes at least its largest class share. Students may state 0 as the minimum in an exam.
- ch 7 [low] Figure spec: The graph is declared directed ('directed': True) and the edges run centroid → document. Cluster membership has no direction; drawn as arrows it suggests the centroid 'points to' or 'produces' the document, which can confuse students about what the edges mean.
