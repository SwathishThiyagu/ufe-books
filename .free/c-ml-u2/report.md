# c-ml-u2: free-model run

- Book: `books/cse/c-ml/c-ml-u2.html`
- Status: ok
- Model calls so far: 28 (127,180 tokens in, 174,442 out), 5.3 minutes

## Checker

```
c-ml-u2.html: 7 chapters, 12927 words, 8 figures, 153 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, multiple regression paragraph: Calling many-inputs-one-output regression 'multivariate regression' clashes with the usual textbook meaning, where multivariate regression means several output variables at once. The clarifying clause helps, but a student can still carry the wrong label into an exam.
- ch 1 [low] Section 2, end of the section: 'other losses need iterative search' is too strong. Least-absolute-deviation regression is solved exactly as a linear program, not by iterative search, so the sentence can mislead.
- ch 1 [low] Section 3, normal equation paragraph and the term list under w = (XᵀX)⁻¹Xᵀy: The transpose is written as plain 'XTX' and 'XTy' in the running text and in the term definitions, while the displayed formula uses a proper superscript. On a phone a student can read XTX as X times T times X.
- ch 2 [low] Figure caption and aria label (Section 4 / worked example figure): The caption says 'five descent steps from w = 0', but the plotted update series has five points: the starting point (0, 11) plus four updated points (1.2, 5.24), (1.92, 3.1664), (2.352, 2.4199), (2.6112, 2.1512). That is four steps, matching the worked example's four updates. A student counting points against steps will be confused.
- ch 2 [low] Section 2, batch gradient descent paragraph: It says batch gradient descent is 'which some syllabi call steepest descent'. Steepest descent normally means gradient descent with an exact line search for the step length along the negative gradient, so the two are not the same thing; the plain fixed-α method described here is not steepest descent.
- ch 3 [low] Quiz Q4: The chapter defines the loss L as the average over n examples, L = −(1/n) Σ [...]. Q4 asks for 'this example's contribution to the binary cross-entropy loss' and the answer −ln(0.8) = 0.223 is the per-example term, not its contribution to L, which is −ln(0.8)/n. A student may not see which of the two is wanted.
- ch 3 [low] Section 3, last sentence: '2.4 studies such linear boundaries directly' comes straight after the softmax/K-class sentences, so 'such' appears to point at multi-class or non-linear boundaries rather than at linear decision boundaries. The forward reference is unclear.
- ch 4 [high] Section 1, last sentence: The sign rule is corrupted: it reads 'Predict class + if g(x)>0 and class − if g(x)2.3.' The text is cut off and the threshold is lost, so the core binary rule of the chapter cannot be read.
- ch 4 [high] Worked example 1, question statement: The example statement is garbled: 'with class + if g(x)>0 and class − if g(x)1=0.2, g2=1.1, g3=−0.4. Which class does argmax choose?' Two different questions are merged, so a student cannot tell what is being asked. The three-class score comparison also appears again in step 4, out of place in a binary example.
- ch 4 [high] Quiz Q3: The answer is wrong twice. g(2,1)=−3(2)+2(1)+1=−6+2+1=−3, not −30, and −3<0 so the prediction is class −, not class +. The second test point (0,0), which the question also asks about, is not answered: g(0,0)=1>0, so class +.
- ch 4 [low] Section 1: The chapter never says what happens when g(x)=0 exactly, although the boundary discussion later depends on that case being a tie.
- ch 5 [high] Quiz Q7: The answer says training error 'may rise slightly' after collecting 100 times more data. With a fixed-capacity degree-9 polynomial and about 800 points instead of 8, the model can no longer come close to interpolating the data, so training MSE rises a lot — from about 0.01 up to roughly the level of the validation error (the bias level), not slightly. The stated reason ('cannot fit every new point's noise as cheaply') also hides the real mechanism: capacity is now small compared with the sample size, so noise fitting is impossible and the training error moves down to meet the generalisation error.
- ch 5 [low] Worked example 1: Degree 1 and degree 3 have the same gap (0.3), so a student can read this as 'gap size is the diagnostic'. The gap alone would wrongly rank the underfitting degree-1 model as equally healthy as degree 3; you also need the levels of both errors.
- ch 6 [low] Section 3 (lasso derivation): The negative branch is presented as a valid solution: 'If w<0, derivative is (w−3)−λ=0, so w=3+λ'. But with λ ≥ 0, 3+λ ≥ 3 > 0, so this contradicts the assumption w<0 and the branch has no solution. A student may think w=3+λ is an answer that can be used.
- ch 6 [low] Quiz Q4: The answer says the ridge penalty 'has derivative 2λw', but the chapter defines the ridge penalty as ½λΣ w_j², whose derivative is λw. The factor 2 contradicts the chapter's own convention and clashes with the λI in the closed form.
- ch 6 [low] Section 4 (elastic net formula): The L2 part of the elastic net penalty is λ(1−α)Σ w_j², but the chapter's ridge objective uses ½λΣ w_j². At α=0 the same λ therefore means twice the penalty in the elastic net formula as in the ridge formula.
- ch 7 [low] Section 2, R² formula: The sentence 'R² = 0 means predicting ȳ' is a shorthand a student can read as an exact equivalence. R² = 0 really means the model's squared error equals that of always predicting the mean; the model itself need not output the constant ȳ.
- ch 7 [low] Section 3, ROC and AUC: The axes are not named. 'Plots recall against 1−specificity' leaves students unsure which quantity goes on which axis, and the usual exam point (TPR on the vertical axis, FPR on the horizontal axis) is missing.
- ch 7 [low] Section 3, AUC sentence: Only 0.5 and 1.0 are described. A student may not know that an AUC below 0.5 means the scores rank the classes in the wrong order (worse than random), not just 'bad'.
- ch 7 [low] Section 1, averaging step: Telling students to 'report the mean and the standard deviation' without a caution invites them to treat this SD as the uncertainty of the mean CV score. The spread of k fold scores is not the standard error of the mean and is itself noisy when k is 5.
- ch 7 [low] Figure caption and spec: The figure shows a single train/test pair, while five-fold CV repeats the split five times. The '5 scores' edge from one test box can mislead a reader into thinking one held-out fold produces all five scores.
- ch 7 [low] Quiz Q6: The answer says AUC 'does not reward a model that always predicts the majority class' without giving the value, so the student cannot see why. Such a constant-score model gets AUC 0.5.
