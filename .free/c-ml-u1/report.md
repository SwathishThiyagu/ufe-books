# c-ml-u1: free-model run

- Book: `books/cse/c-ml/c-ml-u1.html`
- Status: problems
- Model calls so far: 20 (68,148 tokens in, 66,879 out), 3.7 minutes

## Checker

```
c-ml-u1.html: 7 chapters, 9604 words, 8 figures, 120 KB
PROBLEMS:
 - page is wider than the screen at 390px (414>390): a table, figure or long word overflows
```

## For the reviewer

- chapter 1: a c program's shown output was replaced by its real output; check the text around it
- chapter 7: a python program's shown output was replaced by its real output; check the text around it
- chapter 6: a python program's shown output was replaced by its real output; check the text around it
- checker: page is wider than the screen at 390px (414>390): a table, figure or long word overflows

## Reviewer notes (after any revision)

- ch 1 [low] Section 1: The set notation for the training data is unclear: "D = { (x i , y i ) } i=1…N ."
- ch 1 [low] Worked example 1, step 1: The feature vector is shown as "(5,000, 22, 3)" which may be read as four numbers because of the comma.
- ch 1 [low] Quiz Q1: The answer only defines f : X → Y but does not clarify that Y is the prediction (label) space.
- ch 1 [low] Section 2: The description of the feature matrix X does not mention its dimensions.
- ch 1 [low] Worked example 1 (weights): Units for w2 and w3 are written as "hour⁻¹" and "code⁻¹", which are unconventional and may confuse students.
- ch 2 [low] section 1: Zero‑one loss is mentioned but not defined, which may confuse students who have not seen this loss function before.
- ch 2 [low] section 3: The return G is given without the expectation operator, which is standard in the definition of expected return.
- ch 2 [low] exam trap 1: The trap says RL does not need any data, but RL also requires experience (state‑action‑reward tuples) to learn.
- ch 2 [low] quiz Q4: The answer computes Euclidean distance with a square‑root and then squares it, which is unnecessary and may confuse readers.
- ch 2 [low] beyond paragraph: Terms "self‑supervised learning" and "offline reinforcement learning" are mentioned without any brief explanation.
- ch 2 [low] figure spec: The JSON‑style figure specification includes internal keys (e.g., "_d", "_x") that are irrelevant to the text and may distract readers.
- ch 3 [low] Section 1, formula block: The accuracy formula is written using LaTeX syntax \frac, which is not allowed by the allowed inline tags.
- ch 3 [low] Section 1, hypothesis space definition: The term “hypothesis” (a single model) is used later but never defined when first introduced.
- ch 4 [high] Section 2: Bias‑Variance Trade‑off: The bias‑variance formula writes E[(y‑f̂)²] = (Bias)² + Variance + σ² but defines "Bias" as "the error from wrong assumptions" without indicating that the term in the formula is the squared bias.
- ch 4 [low] Worked example 1: The term "overfitting ratio" is used without being defined earlier in the chapter.
- ch 4 [low] Section 1: Data and Model Issues, bullet list: The description of overfitting says "zero training error" which is too strict; overfitting can occur with very low but non‑zero training error.
- ch 4 [low] Figure spec (Venn diagram): The claim that concept drift belongs to all three categories (Data, Model, Ethical) may confuse readers because concept drift is primarily a data/temporal issue.
- ch 4 [low] Quiz Q2: The answer "A situation where training error is much lower than test error" is vague and does not match the chapter’s definition that overfitting is when training error is zero (or near zero) while test error is high.
- ch 5 [high] Exam traps, bullet about variance: The statement "Confusing variance Var(X) with standard deviation √Var(X) will double the error magnitude" is incorrect. Standard deviation is the square root of variance, not twice the variance.
- ch 5 [low] Section 1, vector notation: The description "We write a column vector as v = [v₁, v₂, …, vₙ]ᵀ" may confuse readers because the transpose symbol on a row‑vector notation is unusual for beginners.
- ch 5 [low] Quiz Q7 explanation: The arrow "y = (w·x) + b → y = w·(x + b)" suggests a correct transformation, but the intention is to show a common mistake.
- ch 6 [high] Section 2 (Find‑S algorithm description): The algorithm is said to start with the most general hypothesis ⟨?, ?, …, ?⟩, but Find‑S should start with the most specific hypothesis (all ⊥ or a special “null” value).
- ch 6 [high] Section 2 (Find‑S algorithm description, bullet step): The sentence “replaces ‘?’ in positions where the example differs from the current hypothesis with the attribute value from the example” is incorrect.
- ch 6 [high] Section 2 (Find‑S Python code): The code initializes S with ‘?’ for every attribute, i.e., the most general hypothesis, contradicting the correct algorithm.
- ch 6 [high] Section 3 (Candidate Elimination initialization): It states “Initialize S = ⟨?, ?, …, ?⟩ and G = ⟨⟩ (the set of all most general hypotheses)”, which swaps the correct roles of S and G.
- ch 6 [high] Section 3 (Candidate Elimination bullet list): The bullet “Initialize S = ⟨?, ?, …, ?⟩ and G = ⟨⟩” repeats the same mistake as above.
- ch 6 [high] Worked example 1 – step 1: The example starts with S = ⟨?, ?⟩, which is the most general hypothesis, not the most specific as required by Candidate Elimination.
- ch 6 [high] Quiz Q5 (apply, 5 marks): The answer gives G = {⟨Sunny, Cold⟩, ⟨Rainy, ?⟩}, which is not the minimal set of specializations after a negative example (Sunny, Hot) → No. The correct G should be {⟨Rainy, ?⟩, ⟨?, Cold⟩}. Also the reasoning assumes G already contains ⟨Sunny, ?⟩ and ⟨?, Cold⟩, which is inconsistent with the earlier steps.
- ch 6 [low] Section 3 (Generalization description): The phrase “Generalization replaces ‘?’ with the attribute value from the example” is misleading; generalization of S replaces a specific value with ‘?’ when it conflicts with a positive example.
- ch 7 [high] Section 3 (Bias, VC dimension and the generalisation bound): The VC generalisation bound is missing the standard additive constant (e.g., +1 inside the log term or a log(2) factor). The commonly used bound is √((h (log(2n/h)+1) + log(2/δ))/n). Omitting the constant makes the bound slightly optimistic.
- ch 7 [high] Quiz Q4 (apply, 5 marks): The term for h = 10 is computed as 48.0477, but the correct calculation is 10·log(1000/10) + log(20) = 10·4.6052 + 2.9957 = 49.0477. Consequently the bound value (0.310) is slightly off.
- ch 7 [high] Quiz Q5 (analyze, 6 marks): Logarithm values are incorrect:
- For Model X, log(500/4) is written as 5.5215 (ln 250) instead of ln 125 ≈ 4.8283.
- For Model Y, log(500/9) is written as 4.6052 (ln 100) instead of ln 55.56 ≈ 4.016.
These errors give wrong terms and bounds.
Correct terms:
  X: term = 4·ln(125) + ln(100) ≈ 4·4.8283 + 4.6052 = 23.9184 → bound ≈ √(23.9184/250) ≈ 0.309.
  Y: term = 9·ln(55.56) + ln(100) ≈ 9·4.016 + 4.6052 = 40.7492 → bound ≈ √(40.7492/250) ≈ 0.404.
- ch 7 [low] Figure specification (plot spec): The y‑axis maximum is set to 100 while the plotted values range only up to about 10, making the plot look empty.
- ch 7 [low] Section 2, bullet 1 (Simplicity bias): The sentence suggests that linear regression “prefers” a straight line over a high‑degree polynomial, which may confuse students because the preference comes from the chosen hypothesis class, not an internal preference.
- ch 7 [low] Lead paragraph: The phrase “against fitting noise” is slightly vague.
