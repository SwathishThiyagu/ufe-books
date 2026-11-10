# c-dl-u1: free-model run

- Book: `work/claude_figs/c-dl-u1/tree/books/cse/c-dl/c-dl-u1.html`
- Status: ok
- Model calls so far: 42 (204,266 tokens in, 300,263 out), 6.4 minutes

## Checker

```
c-dl-u1.html: 9 chapters, 17490 words, 10 figures, 204 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, figure spec: The aria text says 'two example methods in each' ring, but the AI ring in the spec lists three items (Reasoning, Chess engine, Expert systems), so the description contradicts the figure data.
- ch 2 [low] Section 3, the Euclidean distance formula note: The note says d 'is a distance in the same units as the features, here rupees'. That holds only when all D features share one unit. With mixed columns (spend in rupees, age in years, visits per month) the squares add quantities of different units and the distance has no single unit, so the note is misleading as a general definition.
- ch 2 [low] Quiz Q4, answer: 'There is no y to compare against, so no error can be computed directly' clashes with Section 3, where k-means does minimise an objective (total squared distance to centres). A careful student will notice the contradiction.
- ch 2 [low] Section 2, third bullet: 'The search for the minimum is backpropagation plus an optimiser' gives backprop the wrong role. Backpropagation computes the gradients; the optimiser uses those gradients to move θ.
- ch 2 [low] Figure caption and aria text: 'Both paths end at the same test: score on rows held back from fitting' is accurate for the supervised path but loose for clustering. Held-out rows can be assigned to the nearest centre, yet there is no label to score against, so the check is a different one (cluster tightness, silhouette, business sense).
- ch 3 [high] Figure (validation-curve plot): The plotted curves are wrong relative to each other. The validation curve '0.08+0.03*(x-4)**2' lies below the training curve '0.9*exp(-0.35*x)+0.04' at every degree (for example, at degree 1 validation error is 0.35 but training error is 0.67; at degree 4 validation is 0.08 but training is 0.26). Training error is measured on the very data the model was fitted to, so it must stay at or below validation error, and the classic picture shows a small gap at low complexity that widens as complexity grows. As drawn, a student would read that the fitted model does worse on its own training data than on held-out data, which contradicts Section 1 and the traps.
- ch 3 [low] Section 2 and exam traps, bullet 3: 'Test error can never go below σ²' and 'no model can go below it' are stated as absolute facts. The decomposition holds for the expected squared error averaged over training sets and noise, so σ² is the floor of that expectation; any single measured test MSE on a finite test set can fall below σ² by chance.
- ch 4 [high] Worked example 1, step 6: The two key inequalities of the XOR contradiction are missing from the text: it reads "(0,0) → 0 needs 0  0" and "(1,1) → 0 needs w₁ + w₂  0". The chain of reasoning cannot be followed, and the contradiction is never stated.
- ch 4 [high] Quiz Q4 answer: The answer ends with the broken line "(1,1) → 0 needs w₁ + w₂  0" and gives no closing contradiction, so the requested proof is not actually given. A student copying this answer loses marks.
- ch 4 [low] Quiz Q1: The question asks for four parts of a neuron, and the answer counts the synapse as one of them. A synapse is the junction between two neurons, not a part of one neuron, and the chapter itself describes the neuron as having three parts (dendrites, soma, axon).
- ch 4 [low] Section 3, paragraph on XOR: "The worked example proves that no weights and threshold do this" is awkward and slightly unclear about what is being proved.
- ch 5 [low] Beyond: The claim that scikit-learn's Perceptron 'trains in one pass over data' is wrong. It repeats passes until the training loss stops improving or a maximum number of iterations is reached; one pass is only the unit of work, not the stopping rule.
- ch 5 [low] Exam traps (fourth bullet) and Section 4: The statement 'the perceptron rule is not gradient descent on a loss' is too absolute. With labels y in {−1, +1} the rule is exactly stochastic gradient descent on the perceptron criterion max(0, −y·net), which is piecewise linear rather than smooth.
- ch 5 [low] Section 2 convergence theorem and quiz Q7: With a bias b present, the bound must use the augmented input. R is the maximum norm of (x, 1), not of x alone, because the proof folds b into the weight vector by appending a constant input of 1.
- ch 5 [low] Section 4 (XOR paragraph): 'Run the perceptron rule on XOR and it cycles forever' suggests the weights repeat in a periodic cycle. On non-separable data the weights usually keep changing without ever repeating exactly.
- ch 6 [low] Lead: The MLP is described as 'the first stage of almost every deep model'. In real systems the fully connected layers are usually the last stage (the classifier head); the first stages are convolutions or embeddings. A student may take the sentence literally.
- ch 6 [low] Figure caption: The caption calls h₁ 'the upper hidden unit', but the node spec puts h₁ at y = 0.5 and h₂ at y = 3. Whether y = 0.5 is the upper or the lower node depends on the drawing convention, so the caption can contradict the picture.
- ch 6 [low] Section 3, bump picture: 'the difference of two opposite steps is a narrow bump' is misleading. Two opposite steps (one rising, one falling) do not give a bump; what gives a bump is the difference of two shifted versions of the same rising step.
- ch 6 [low] Exam trap 3: 'or the whole stack is one perceptron' is inaccurate: with no non-linearity the stack is a single affine map, which is even weaker than a perceptron (a perceptron at least applies a threshold).
- ch 6 [low] Quiz Q6: With the network's original weights the sigmoid outputs are not 'near but not equal to 0 and 1'. They sit around the middle: for example (0,0) gives roughly 0.43 and (1,1) roughly 0.57. Only after the weights are scaled up do the outputs approach 0 and 1.
- ch 6 [low] Quiz Q2: The answer lists the activation condition as 'bounded, non-constant' and drops 'non-decreasing', which the chapter's own statement of the theorem includes. The question asks to name the condition, so the answer is incomplete against the text.
- ch 7 [high] Quiz Q5: The answer says leaky ReLU gives 'derivative α < 0 on the negative side'. The slope α is a small positive number (0.01 or 0.1 in this chapter), so the derivative on the negative side is α > 0, a small positive value. As written, a student would conclude the gradient is negative and would also contradict the chapter's own leaky ReLU formula and Exam trap.
- ch 7 [low] Section 2, leaky ReLU formula: The definition line gives 'α is a small slope, typically 0.01 or 0.1' but never says α > 0. This is the source of the sign slip later in Q5.
- ch 8 [high] Section 2, 'Two classes' (paragraph on the plain linear unit), and quiz Q3 is built on the same idea: The chapter says a linear unit trained with MSE is bad because 'its gradient fades when the model is confidently wrong'. That is false. With a linear output the gradient of (ŷ − y)² is 2(ŷ − y), which grows as the error grows; nothing saturates. The gradient-fade argument belongs to sigmoid + MSE (correctly given in Q3), not to linear + MSE. A student will carry away a wrong reason for rejecting linear + MSE.
- ch 9 [low] Section 2, output-layer error line: The output-layer start value is written as δ = ∂L/∂ŷ ⊙ f′(z), with no layer superscript on δ or z. δˡ was defined as ∂L/∂zˡ, so the missing superscript (this is δ to the power L, with z to the power L) makes the symbol look like a different quantity, and a student cannot tell how it connects to the hidden-layer formula that follows.
- ch 9 [low] Section 2, sentence about differentiation algorithms: "Some syllabi call this area other differentiation algorithms; the practical answer is automatic differentiation, which differentiates the same graph exactly" is vague. "This area" is never named, and "exactly" overstates what happens in floating point.
- ch 9 [low] Section 3, ReLU gate: The derivative of ReLU is given for z > 0 and z < 0 only. ReLU is not differentiable at z = 0, and a student meeting z = 0 will not know which value backprop uses.
- ch 9 [low] Quiz Q7: The question asks for the three formulas for a layer l, but the first formula, δˡ = (Wˡ⁺¹)ᵀ δˡ⁺¹ ⊙ f′(zˡ), holds only for a hidden layer. Applied to the output layer it refers to a weight matrix Wˡ⁺¹ that does not exist.
- ch 9 [low] Section 2, "In the example, ∂L/∂w² = (ŷ − y)h": This result is quoted before the reader has been told which loss the example uses (the ½(ŷ − y)² loss is only given later, in Worked example 1). The jump from the general chain rule to (ŷ − y)h looks like a missing step.
