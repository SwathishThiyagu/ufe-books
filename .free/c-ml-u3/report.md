# c-ml-u3: free-model run

- Book: `books/cse/c-ml/c-ml-u3.html`
- Status: ok
- Model calls so far: 38 (149,875 tokens in, 266,331 out), 6.8 minutes

## Checker

```
c-ml-u3.html: 9 chapters, 15076 words, 10 figures, 170 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, second bullet: The bullet 'H=1 bit is the maximum for two balanced classes' can be misread. The maximum over all two-class distributions is 1 bit; balance is the condition that achieves it, not a restriction on the maximum.
- ch 1 [low] Section 3, recursion steps and Section 2 formula: Neither the gain formula nor the recursion says what happens when some value v of the chosen attribute has no examples (Sv empty). Then H(Sv) is undefined and the child node cannot be built, which a student can hit with sparse data such as a Weather value that no training day has.
- ch 1 [low] Section 3, paragraph on attribute bias: 'A high-branch attribute' is unclear wording; students will not know whether it means an attribute high in the tree or one with many branches.
- ch 1 [low] Exam traps, fourth bullet: 'base 10 gives different numbers, though ranking can be the same' understates the fact. Changing the log base multiplies every information gain by the same positive constant 1/log₂10, so the ranking of attributes is always identical at every node and the tree built is the same.
- ch 1 [low] Lead: The lead says the tree below predicts Play from Weather and Wind, but the final tree in the figure and worked example tests only Wind; a student may look for a Weather node that is not there.
- ch 1 [low] Beyond: 'see 3.8' is a plain text cross-reference, not a chapter link in the required form.
- ch 2 [high] Section 3, Beta prior sentence: The chapter says the Beta prior MAP is (h+α)/(n+α+β). That expression is the posterior mean of Beta(h+α, n−h+β), not the mode/MAP. The MAP (mode) is (h+α−1)/(n+α+β−2). The following sentence 'A uniform Beta(1,1) prior gives back h/n' is correct for the MAP but contradicts the formula as printed, because (h+1)/(n+2) is what the printed formula gives for Beta(1,1). A student who memorises the printed formula will get the coin answer wrong whenever a real prior is used.
- ch 2 [low] Exam traps, third bullet: The bullet is about MLE ignoring the prior, but then says 'A rare disease with a strong prior can be missed'. A strong prior toward 'healthy' is what causes a miss under MAP, not under MLE, so the sentence reads as the opposite of the point being made.
- ch 2 [low] Section 3 and Worked example 1: The symbol h is used for a hypothesis in Sections 1 and 2 and then reused for the number of heads in Section 3 and in the worked example ('h = 7 heads', 'h1: p = 0.5'). Students skimming the example can read the two meanings into the same line.
- ch 2 [low] Figure, y-axis label: The y-axis is labelled 'probability' but one series is the unnormalised posterior score P(D|h)P(h), which sums to 0.125 here, not to 1. Calling it a probability invites confusion with the normalised posterior computed in step 7.
- ch 2 [low] Section 2, last paragraph: The cross-reference 'See Unit 2, Regularization: ridge and lasso' and the forward references to 3.3 and 3.4 are plain text, so on a phone they cannot be tapped like the other chapter links.
- ch 3 [low] Section 2, Gaussian Naive Bayes formula: The formula is written as P(xᵢ = v | C), but for a numeric feature a normal density is not a probability of the value v; it is a density. A student can read this as an ordinary probability and wonder why values above 1 appear.
- ch 3 [low] Section 3, normalization formula: score(C) ÷ Σ score(C′) is presented with ≈ and called 'not a guarantee of true probability'. Under the independence assumption this division is exactly the model's posterior; it is only approximate as a description of the real world. The wording blurs the two ideas.
- ch 3 [low] Section 1, last paragraph: The pointer to chapter 3.5 is plain text, so it does not work as a cross-chapter link in the book.
- ch 3 [low] Figure caption: The caption says the values shown match the six-day worked example, but the graph shows only the prior note P(Yes)=4/6; no conditional table values (CPTs) appear. The claim is not true of the figure as drawn.
- ch 3 [low] Quiz Q6 answer: The answer says α controls how much probability is added to every feature value. In the formula α is added to the counts, not to the probabilities; the probability change is a result of smoothing.
- ch 4 [low] Lead: P(h|D) is called 'the probability that h is correct'. That reads like accuracy, but it is the posterior probability that h is the true hypothesis in H given D. A student may mix the two ideas.
- ch 4 [low] Section 1: 'This is averaging over the whole hypothesis space, so it is an ideal' gives the wrong reason. Being an average is not what makes it an ideal; it is ideal (uncomputable in practice) because the sum over H cannot be done for realistic H.
- ch 4 [low] Section 2, bullets: The text says 'In the three-hypothesis example, h1 is drawn with probability 0.5 ...' but that example has not been introduced yet; it appears only in Worked example 1. The reader meets unexplained numbers h1, h2, h3, Yes, No.
- ch 4 [low] Section 3: The standard result that makes Gibbs worth studying is missing: the expected 0-1 error of Gibbs is at most twice the Bayes optimal error. The lead promises Bayesian learning theory 'uses both to reason about optimal and sampled decisions', so the promised link is never made.
- ch 5 [high] Figure caption (and its aria text): The caption says "each node carries a table for its child given its parent", which is backwards and contradicts both the body text (each node stores P(Xi | parents(Xi))) and the figure's own notes: node F carries P(F)=0.3, which is a table for F itself, not for its child S. A student could come away thinking the parent node holds the child's CPT. The aria text makes the same slip, saying the tables are "on the edges", while the tables sit on the nodes.
- ch 5 [low] Lead: "Each node stores a conditional probability table for its parents" can be read as saying the table is about the parents, not about the node given its parents.
- ch 5 [low] Section 2: The five bullets (list the variables, add arrows, check for cycles, write CPTs, read the joint) are a procedure for building a Bayes net, but they appear with no lead-in sentence, right after the example on Study blocking the chain, so the reader is not told what the list is.
- ch 6 [high] Section 3, scale paragraph: The claim that squared salary differences are 'about 108 times larger' (meant as 10⁸, but written without a superscript so it reads as one hundred and eight) than squared age differences is wrong by two orders of magnitude. With the ranges given, the largest salary gap is 90,000, so its square is 8.1 × 10⁹; the largest age gap is 52, so its square is about 2.7 × 10³. The ratio is roughly 3 × 10⁶, not 10⁸, and the number is also mistyped as '108'.
- ch 6 [low] Figure spec: The graph is marked directed: True, but the edges are Euclidean distances, which are symmetric. Rendering the figure with arrowheads suggests Q → B, Q → A, Q → D are one-way relations, which is misleading.
- ch 7 [low] Section 2: It says the soft-margin dual introduces one multiplier α_i ≥ 0 per training point. With slack, the multipliers are also capped: 0 ≤ α_i ≤ C. Stating only α_i ≥ 0 is the hard-margin condition and can make a student think C does not bound the multipliers at all.
- ch 7 [low] Section 3: The pointer 'see Unit 2' is plain text, so a student reading on a phone cannot jump to the cross-validation chapter.
- ch 8 [low] Section 3 (AdaBoost formula discussion): The text covers ε_t = 0.5 (α_t = 0) and ε_t > 0.5 (negative α_t) but never mentions the ε_t = 0 case. There α_t = ½ ln((1 − 0)/0) diverges, and the update multiplies every weight by e^(−α) = 0, so the normalisation step becomes 0/0. A student meeting a perfect weak classifier will not know what to do.
- ch 8 [low] Worked example 1, step 6: With the rounded numbers shown, 0.4330 + 3 × 0.1443 = 0.4330 + 0.4329 = 0.8659, not 0.8660. The stated 0.8660 is the exact value 6/(4√3); the displayed arithmetic does not reproduce it, which a student recalculating on paper will notice.
- ch 9 [high] Exam traps, third bullet: The bullet merges two different effects into one and gets the RBF half wrong. For a Gaussian weight in LWR, a large τ does make all weights nearly 1 and the fit collapses to a global straight line. For an RBF network, a large σ does not give a 'global linear fit' and does not 'miss curvature': with σ large each bump flattens, φ_j(x) ≈ 1 − ||x − μ_j||²/(2σ²), so the network output becomes an almost constant, very smooth global function of x (in effect a constant plus a quadratic term). The failure is over-smoothing and loss of all input dependence, not collapse to a straight line. A student who memorises the sentence will give a wrong answer on σ.
