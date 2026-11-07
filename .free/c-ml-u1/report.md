# c-ml-u1: free-model run

- Book: `books/cse/c-ml/c-ml-u1.html`
- Status: ok
- Model calls so far: 28 (110,949 tokens in, 203,696 out), 7.9 minutes

## Checker

```
c-ml-u1.html: 7 chapters, 12630 words, 8 figures, 140 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1, step 4: Step 4 computes the spam share (200 ÷ 1000 = 20%), but the question never asks for it and no later step uses it. A student may think the class balance is needed for the accuracy calculation, or may report it as part of the answer.
- ch 1 [low] Worked example 1, opening and step 3: The rule 'spam if the word lottery appears at least twice' is simply stated, so the 1000 training emails play no visible part in producing it. The example then shows T, P and E but never shows learning, which can leave students unsure where the 'learning' is.
- ch 2 [low] Section 1, supervised output bullets: Listing 'waiting-list position' as a regression output sits awkwardly beside the lead's 'IRCTC waitlist prediction' and the classification example 'confirmed/waitlisted'. A student may conclude that all waitlist prediction is regression, when the usual task (will the ticket confirm?) is classification. A rank is also an odd numeric target.
- ch 2 [low] Figure: The child under Reinforcement is 'Agent'. The other children (Classification, Regression, Clustering) are task types, but an agent is the learner itself, not a task type. The tree then mixes two kinds of node.
- ch 3 [low] Figure caption: The caption says performance 'is measured before deployment, not after', but step 8 of the design cycle tells the reader to deploy, monitor inputs and errors, and retrain. A student will read these as contradictory: monitoring after deployment is measurement too.
- ch 3 [low] Section 2 formula and Section 3: The symbol P is overloaded. In Section 1 and the formula h* = arg max P(h), P is the performance measure; in Section 3 it is the probability P(y | x). The same letter carries two unrelated meanings in one chapter.
- ch 3 [low] Section 2, first bullet: The instruction 'fix the unit of P, such as accuracy or rupees of cost' mixes a metric (accuracy, unitless) with a cost (rupees). Calling accuracy a 'unit' can confuse students about what a unit of P means.
- ch 4 [low] Section 3: The sentence 'Only a few universities teach domain shift under this name' is an unverifiable claim about syllabi and is placed mid-paragraph where it breaks the flow; domain shift is in fact standard terminology in most machine learning texts.
- ch 4 [low] Section 2: Precision, recall and F1 are used without definition, which breaks the rule of defining every term at first use; a second-language reader may not know what F1 is.
- ch 5 [low] Section 1, dot product paragraph: "||a||2 is the Euclidean length" is unreadable on a phone: without subscript markup a student reads "norm times 2", and the same length has just been defined as ||a||, so the sentence looks contradictory.
- ch 5 [low] Section 1 (Cij = Σk AikBkj, A−1A = I) and Section 3 (P(X=k) = C(n,k)pk(1−p)n−k, σXσY): Subscripts and exponents are left as plain characters, so formulas show as "pk(1−p)n−k", "Cij", "Σk AikBkj", "A−1A", "σXσY". On a phone screen these read as products of separate symbols and the binomial mass function looks wrong.
- ch 6 [high] Section 1, general-to-specific ordering: The sentence More ? means more general is false as a general rule. Two hypotheses can have different numbers of ? and be incomparable, for example (?,Sunny,?) and (Sunny,Warm,?).
- ch 6 [high] Exam traps, first bullet: Positive examples do not only change S, and negative examples do not only change G. A positive example can remove hypotheses from G that do not cover it; a negative example can remove hypotheses from S that cover it. This contradicts quiz Q5.
- ch 6 [high] Section 2, after Find-S example: Calling the Find-S answer a consistent hypothesis is misleading because the next sentence says it can cover a negative example, which means it is not consistent with all training data.
- ch 6 [low] Section 3, candidate elimination negative update: The negative update says to specialize each g minimally but does not say to replace g by all minimal specializations. Candidate elimination needs all of them; one g can yield several.
- ch 6 [low] Quiz Q4: The answer writes S=(Sunny,Warm,?) but S is a set of hypotheses. The worked example uses S={(Sunny,Warm,?)}.
- ch 6 [low] Quiz Q5: The answer says remove s from S, but the negative update removes every hypothesis in S that covers the negative, not just the one named s.
- ch 7 [high] Worked example 1: The example says 'h1 has 30 rules; h2 has 3 rules', but the chapter defines a hypothesis as one rule. A single hypothesis cannot contain 30 rules; this confuses rule complexity with hypothesis count.
- ch 7 [high] Quiz Q6: The answer asserts 'low training error' and calls tree A overfitting, but the question only says both trees have the same training error. If training error is high, a larger test error is not overfitting; the conclusion is not justified.
- ch 7 [high] Figure: The edge from test data to chosen model is backwards. It shows test data feeding the model, but test data is used after training to evaluate the model.
- ch 7 [low] Section 1, Find-S paragraph: 'It never chooses a more general rule that also fits' is ambiguous and can be read as denying that Find-S generalizes when a positive example forces it.
- ch 7 [low] Quiz Q4: The answer treats the general-to-specific ordering as part of candidate elimination's inductive bias. The ordering is a representation tool; the bias is the restricted hypothesis space and the assumption that the target lies in it.
