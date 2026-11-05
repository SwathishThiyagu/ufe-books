# c-ml-u5: free-model run

- Book: `books/cse/c-ml/c-ml-u5.html`
- Status: ok
- Model calls so far: 38 (133,834 tokens in, 132,706 out), 5.1 minutes

## Checker

```
c-ml-u5.html: 9 chapters, 12482 words, 10 figures, 148 KB
OK
```

## For the reviewer

- chapter 6: a c program's shown output was replaced by its real output; check the text around it
- chapter 1: a python program's shown output was replaced by its real output; check the text around it
- chapter 8: a python program's shown output was replaced by its real output; check the text around it
- chapter 8: a c program's shown output was replaced by its real output; check the text around it
- chapter 4: a c program's shown output was replaced by its real output; check the text around it
- chapter 2: a python program's shown output was replaced by its real output; check the text around it
- chapter 2: a c program's shown output was replaced by its real output; check the text around it
- chapter 9: the reviewer found 1 serious problem(s) and the revision did not pass the checks; read the review in the state folder

## Reviewer notes (after any revision)

- ch 1 [high] Section 2: From biology to the McCulloch‑Pitts model: The text calls θ a "bias term" and says it is subtracted from the sum. In the MP model θ is the threshold, not a bias. A bias is usually added to the weighted sum (or defined as b = –θ). Calling θ a bias and saying it is subtracted can mislead students.
- ch 2 [high] Section 2, Python example: The comment says the code prints "[2, 2] 1" but the actual output shown is "[0.0, 0.0] 0.0", which is correct for the given inputs.
- ch 2 [low] Worked example 1, step 2: The wording is contradictory: it states "y₁ = 0 because s₁ < 0 is false" and then says "y₁ = 1".
- ch 3 [high] Section 2 (Mathematical description of a two‑layer example): The weight notation is inconsistent. For a network with two inputs and one hidden unit the weights should be w_{1,1} and w_{2,1}. The text uses w₁₁ and w₁₂, which suggests a second hidden unit that does not exist.
- ch 3 [low] Quiz Q4: The question asks for the final output given an output bias of 0.3 and a hidden unit output of 0, but does not specify the weight from the hidden unit to the output. The answer assumes a weight of 1, which is not stated.
- ch 4 [high] Worked example 1 – dry‑run table: The loss value shown in the table (0.3566749439) does not match the correct cross‑entropy loss for the given probabilities. It corresponds to -log(0.7) instead of -log(0.690). This inconsistency can mislead students.
- ch 5 [low] Section 1: Mean‑squared error is defined without the usual averaging factor (1/N).
- ch 5 [low] Section 1, bullet list: Bullet "Subtract the target from the output" can be read as t‑ŷ, which contradicts the formula.
- ch 5 [low] Matrix notation in Section 3: The description does not explicitly state that δ is a column vector and A is a column vector, so the outer product δ·Aᵀ may be unclear.
- ch 6 [high] Section 3 (Regularisation): The description of dropout scaling is incorrect. It says that at inference time activations are scaled by (1‑p). In standard (inverted) dropout, scaling by 1/(1‑p) is applied during training, so no scaling is needed at inference.
- ch 6 [low] Exam traps paragraph: The trap description says using the same learning rate η for both the momentum update and weight‑decay without multiplying λ by η leads to too large decay, but the worked example actually uses η for both steps (Δ = η·λ·w₁). This creates confusion about the correct practice.
- ch 7 [high] Section 2 (Vanishing gradient and the ReLU remedy): The text says each sigmoid layer multiplies the gradient by at most 0.5, but the derivative of sigmoid is σ(z)(1‑σ(z)) ≤ 0.25. Using 0.5 contradicts the correct maximum factor of 0.25 (and saturated sigmoid derivative is near 0, not 0.5).
- ch 7 [high] Worked example 1 (Python and C code): Both code snippets use sigmoid_factor = 0.5, which is inconsistent with the correct sigmoid derivative bound of 0.25.
- ch 7 [high] Quiz Q2 (understand, 3 marks): Answer states each sigmoid layer multiplies the gradient by a factor ≤0.5, which is incorrect.
- ch 7 [high] Quiz Q5 (analyze, 6 marks): Gradient calculation for a ten‑layer sigmoid network uses 0.5¹⁰, giving 0.00078, which is based on the wrong per‑layer factor.
- ch 7 [low] Section 2 text: Phrase “a typical saturated value” for the sigmoid factor 0.5 is misleading; saturated sigmoid derivatives are near zero, and the maximum derivative is 0.25.
- ch 7 [low] Formula y = σ(Wᴸ·σ(...)) in Section 1: The same symbol σ is used for all layers, which may confuse readers about the output activation (often linear or softmax).
- ch 8 [high] Worked example 1 – description and steps: The example claims the convolution output is [-2, -2, -2] and shows three steps, but with input [1,2,3,4], kernel [1,0,-1], stride 1 and no padding the correct output length is 2 and the values are [-2, -2]. The calculations in steps 1‑3 are also wrong (they multiply the wrong input elements and treat missing values incorrectly).
- ch 8 [high] Worked example 1 – C code: The C code declares conv[3] and loops i from 0 to 2 (i<3). For i=2 it accesses x[i+j] with j up to 2, which reads x[4] and x[5] beyond the array bounds. The code also assumes zero‑padding without actually adding it, producing incorrect results.
- ch 8 [low] Section 1 – formula description: The convolution formula shown does not include the effect of padding, even though padding is discussed in the text. This may confuse students about how padding changes the index range.
- ch 8 [low] Section 3 – dilated convolution description: The bullet "Insert d‑1 zeros between consecutive kernel coefficients" can be misinterpreted; dilation actually inserts zeros between the *applied* kernel positions on the input, not physically into the kernel coefficients.
- ch 9 [high] Section 2, Python code bptt: The gradient for Wh is computed using the new hidden state h instead of the previous hidden state h_prev. In BPTT the derivative ∂hₜ/∂Wₕ involves the hidden state from the previous time step, not the current one.
- ch 9 [low] Section 2, Python code bptt: The code uses numpy functions but does not import the numpy module.
