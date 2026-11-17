# m-prob-u2: free-model run

- Book: `books/common/m-prob/m-prob-u2.html`
- Status: ok
- Model calls so far: 21 (85,446 tokens in, 165,212 out), 4.0 minutes

## Checker

```
m-prob-u2.html: 8 chapters, 13290 words, 9 figures, 152 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3, opening paragraph and table: The text says 'Three rules solve most first-step problems' and then lists three problem-solving steps, but the table that follows has four rules (complement, addition, disjoint addition, monotonicity). The count mismatch may confuse a student about which rules are being referred to.
- ch 1 [low] Section 2, axiom list: 'For every event A in Ω' is imprecise: an event is a subset of Ω, not an element of Ω. A strict reader may misread 'in' as membership.
- ch 2 [low] Section 1, after the multiplication-rule formula: "Use whichever condition is easier to observe" is too compressed. A student may not see that it means choosing between multiplying by P(B) with P(A|B) and multiplying by P(A) with P(B|A).
- ch 2 [low] Lead paragraph: "This chapter builds the formula, tree diagrams ..." is a roadmap sentence of the kind the series style avoids; it tells the reader about the chapter instead of teaching the idea.
- ch 3 [low] Worked example 1, output block: The four loose numbers (0.012, 0.02, 0.032, 0.375) appear with no code and no labels, so a student cannot tell what the 0.02 line is doing there — it merely repeats the M1 defect rate and is not a step result.
- ch 3 [low] Section 3, first sentence: A base rate is defined as 'the prior P(A) when that prior is small'. The base rate is simply the unconditional prior (prevalence) whether it is small or large; only the striking effect needs a small prior.
- ch 4 [high] Worked example 1, answer line: The piecewise CDF in the answer is corrupted: it reads 'The CDF is F(x)=0 for x1' — the middle branches were lost, so a student cannot read the final result.
- ch 4 [low] Quiz Q1: 'Give its type signature' is programming jargon that a first-year student may not connect to the mapping X: Ω → ℝ.
- ch 4 [low] Section 3, bullet on right-continuity: The notation F(x+)=F(x) is used without saying what F(x+) means.
- ch 4 [low] Section 1, last line: 'Exam questions state which type you have' is not always true; many questions give only the support or the wording (counts vs measurements), and a student may freeze when the type is not stated.
- ch 5 [low] Section 3, moments paragraph: The superscripts and subscripts are missing in the body text, so the formulas read as μ′r=E[Xr], μ′r=Σ xrp(x) and μr=Σ (x−μ)rp(x). A student can read 'Xr' as X times r, and 'μ′r' as μ′ times r, which is wrong.
- ch 5 [low] Section 3, last paragraph before the figure: 'The same absolute-convergence caution applies when r is large' suggests convergence is only a worry for high r. In fact each moment needs its own convergence check for every r, and a high moment can fail even when low ones exist (a heavy-tailed distribution may have a mean but no variance).
- ch 5 [low] Section 3, skewness/kurtosis sentence and conditional expectation sentence: The chapter points to 'Unit 1' and 'Chapter 2.2' but neither is written as a link, so a phone reader cannot jump there, and 'Unit 1' is easy to confuse with the chapter numbering used everywhere else.
- ch 6 [low] Section 1 (expansion sentence): The exponential is typed as plain 'etx' instead of e^(tx), so the sentence 'Expand etx=1+tx+…' reads like a product of symbols e, t, x and can confuse a student.
- ch 6 [low] Section 2 (the 'where' clause after the derivative formula): The formula uses M_X<sup>(r)</sup>(0) but the explanation writes 'M_X(r)(0)' in plain text, which reads as M_X multiplied by r, not as the rth derivative.
- ch 6 [low] Section 3 (characteristic function sentence): The characteristic function is typed as 'φ(t)=E[eitX]' with no superscript and no multiplication signs, so 'eitX' is ambiguous and the modulus |eitX|=1 that follows looks inconsistent.
- ch 7 [high] Section 2 (Proof by squaring), the sentence after the proof of the upper-tail form: The sentence is cut off and unreadable: "The complement of |X − μ| ≥ kσ is |X − μ|  0." The event and the conclusion of the inside form are lost, so a student cannot follow the complement step that produces P(|X − μ| < kσ) ≥ 1 − 1/k².
- ch 7 [low] Section 1, last paragraph of the section (moment inequalities remark): It says Chebyshev uses E[X] and E[(X − μ)²], "the first two moments". E[(X − μ)²] is the second central moment, not the second moment E[X²]; Markov alone uses the first moment and Chebyshev alone uses only the second central moment.
- ch 7 [low] Quiz Q6 answer: "Chebyshev gives a lower bound, not an upper bound" is too broad. The chapter itself teaches an upper bound, P(|X − μ| ≥ kσ) ≤ 1/k²; only the inside statement is a lower bound. A student may conclude Chebyshev has no upper-tail form.
- ch 8 [high] Section 3, linear map paragraph: The sentence "The factor 1/|a| widens the density when |a|1, so area stays 1" has lost its comparison, so the condition on a is unreadable and the direction of the effect cannot be checked by a student.
