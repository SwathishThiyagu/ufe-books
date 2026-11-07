# c-dl-u2: free-model run

- Book: `books/cse/c-dl/c-dl-u2.html`
- Status: ok
- Model calls so far: 26 (95,134 tokens in, 312,072 out), 13.9 minutes

## Checker

```
c-dl-u2.html: 9 chapters, 13921 words, 10 figures, 161 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q5 answer: The answer misclassifies w = 1. It says J''(1) = −3 and then calls it a local minimum, but a negative second derivative means w = 1 is a local maximum. It also never identifies w = 4 as the other local minimum, even though the question asks which of the three stationary points are minima.
- ch 1 [low] Figure vs Worked example 1: The plotted expression uses the rounded coefficient 1.6667, giving J(4) ≈ −7.6688, while the worked example uses the exact coefficient 5/3 and reports J(4) = −7.6667. The same function is shown with two slightly different values.
- ch 2 [low] Section 1: The sentence 'If N is 1 000 000, one update needs 1 000 000 forward and backward passes' counts passes per sample. In vectorized deep learning frameworks one full-batch update is one large forward/backward pass over all samples or several chunked passes, not necessarily N separate passes.
- ch 2 [low] Section 2 algorithm and Q1: The algorithm uses a fixed mini-batch size m and divides by m, but Q1 says an epoch has ⌈N/m⌉ updates, which implies a final incomplete mini-batch when N is not divisible by m. Dividing by m for a smaller final batch would not compute the proper average gradient.
- ch 3 [high] Lead: The lead says both momentum and NAG appear inside algorithms such as Adam. Standard Adam uses a momentum-like first moment, but it does not use Nesterov's lookahead. NAG appears only in variants such as Nadam.
- ch 3 [high] Exam traps, first bullet: It uses θ_t for the old weights and lookahead, but the chapter defines θ_t as the updated weights. Before the update at step t the current weights are θ_{t−1}. This notation error can mislead.
- ch 3 [low] Quiz Q7 answer: The phrase 'NAG is slightly further because it saw a better gradient at the lookahead point' is vague and may imply NAG should have improved. In the example, the lookahead gradient 0.81 is smaller than the current gradient 0.90, so NAG moves slightly less.
- ch 3 [low] Section 2, first paragraph: The text says NAG 'first takes a step along the old velocity' before computing the gradient. This can be read as a real weight update, but NAG only forms a temporary lookahead point.
- ch 4 [high] Section 3, Adam bias-correction formulas: The denominators are written as 1−β1t and 1−β2t. The t is not shown as an exponent, so the formula reads like β₁ times t instead of β₁ to the power t.
- ch 4 [high] Exam traps, first bullet: The trap says forgetting Adam bias correction makes the first few steps too small. This is wrong for the standard defaults. Without bias correction, the first update is η(1−β₁)/√(1−β₂) = 0.1×0.1/√0.001 ≈0.316, much larger than the bias-corrected 0.1.
- ch 4 [high] Figure caption: The caption says Adam's first two steps match AdaGrad then slow slightly. Only the first update matches; at iteration 2 Adam's w is 0.800 while AdaGrad's is 0.833, so Adam took a larger step, not a slower one.
- ch 5 [high] Section 1 formula: The vector chain rule is written in the wrong order and without transposes. The expression g_l = g_L × J_{l+1} × ... × J_L is not the standard backpropagation expression. For column gradients it should be g_l = J_{l+1}^T J_{l+2}^T ... J_L^T g_L; for row gradients it should be g_l = g_L J_L J_{L-1} ... J_{l+1}.
- ch 5 [high] Section 1 text, Worked example 1 step 1, Q3 answer: The multiplier uses L factors, but from the output of layer L to the output of layer 1 there are L−1 Jacobians. So for ten layers the 0.25 product should be 0.25^9 ≈ 3.81×10^-6, and for five layers the 0.5 product should be 0.5^4 = 0.0625. If the intended reference is the gradient for layer-1 weights, the text must explicitly include layer 1's own derivative and use L factors.
- ch 5 [low] Section 2 weight initialization paragraph: Saying a weight matrix with entries around 0.1 gives a product 0.1^L treats a matrix like one scalar. Actual matrix growth depends on singular values or spectral norm, and activation derivatives also change the product.
- ch 6 [high] Section 1: Why initialization matters: The sentence 'Backprop gives the same gradient to every weight in a unit' is wrong. For a fixed hidden unit, incoming weights from different input features generally have different gradients x_j δ_k. The actual symmetry is that the same input index across different hidden units has the same gradient.
- ch 6 [low] Section 2: Xavier/Glorot initialization for tanh and sigmoid: The claim 'sigmoid saturates faster than tanh' is technically incorrect as a general statement. For large |x|, tanh saturates faster because its derivative decays roughly as e^{-2|x|}, while sigmoid's derivative decays roughly as e^{-|x|}. Sigmoid has a smaller maximum derivative, but that is not the same as faster saturation.
- ch 6 [low] Section 3: He/Kaiming initialization for ReLU: GELU is not a ReLU variant. Also, for leaky ReLU and PReLU the exact He-style variance includes the negative slope a: σ² = 2 / ((1 + a²) fan_in). Saying plain He normal initialization is the standard default for PReLU can mislead.
- ch 7 [low] Section 3, identity statement: It says the network can learn γ = √(σ²_B + ε) and β = μ_B to recover the original value. Since σ²_B and μ_B are mini-batch statistics that vary per batch, learned constants γ and β cannot use them to reconstruct identity across all mini-batches. This can mislead students.
- ch 7 [low] Section 2, running variance update: The running variance is updated with the biased mini-batch variance σ²_B (denominator m). Standard implementations often use an unbiased variance estimate m/(m−1) σ²_B for the running variance; otherwise the saved variance is slightly too small at inference.
- ch 8 [low] Exam traps, first bullet: The phrase "using λ or 2λw is a sign/slope slip" is inaccurate. Using λ or 2λw instead of λw is a factor/magnitude error, not a sign or slope error; this wording may confuse students about the common mistake.
- ch 8 [low] Section 2, Dropout, initial bullets and test-time rule: The bullet "At test time, every unit is active" is true but incomplete for standard dropout, where activations are also scaled by p. The text later specifies inverted dropout needs no scaling, but the earlier statement may confuse a student who uses the initial standard-dropout description.
- ch 9 [high] Section 1: The formula uses "2m copies" (2 × m), but the number of combinations from m independent binary augmentations is 2^m. For m=2 the result is coincidentally 4, but for m=3 it would give 6 instead of the correct 8.
- ch 9 [low] Section 3: The sentence "Use early stopping from regularization and early stopping inside each run to save time" is unclear and repeats early stopping; it reads as if early stopping comes from regularization.
