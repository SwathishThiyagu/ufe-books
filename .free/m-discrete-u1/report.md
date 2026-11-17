# m-discrete-u1: free-model run

- Book: `books/common/m-discrete/m-discrete-u1.html`
- Status: ok
- Model calls so far: 26 (87,107 tokens in, 200,436 out), 5.0 minutes

## Checker

```
m-discrete-u1.html: 9 chapters, 14025 words, 10 figures, 158 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, rows rule and fill rule: The row count is written as "2n rows" and "all 2n assignments". Read literally this means 2 times n, which is wrong: a formula with n variables has 2ⁿ rows (worked example 1 itself writes 2² = 4). A student copying "2n" will lose marks.
- ch 2 [high] Figure (blocks diagram), node b 'Remove implication': The note on node b is '¬p∨q', but only the p→q part is rewritten. The whole formula after removing the implication is (¬p∨q)∧(p∨q). As drawn, the box silently drops the (p∨q) factor, so it is not equivalent to the box above it, and the caption 'Every box is logically equivalent to the one above it' becomes false.
- ch 2 [low] Worked example 1, step 6: 'The formula is true in 2 of 4 rows' is ambiguous: 'the formula' was used earlier for the expression being simplified, and the reader may think it means the simplified formula q. The check is clearer if the original expression is named.
- ch 3 [low] Quiz Q2 answer: The answer says 'every other row has at least one true maxterm'. On any row other than row i, the maxterm Mᵢ is true, so in fact every listed maxterm is true there. 'At least one' is true but weak, and a student may take it to mean one true maxterm is enough to make the whole AND true.
- ch 3 [low] Worked example 1, steps 5 and 8, and Quiz Q3–Q6: The shorthand Σm(1,2) and ΠM(0,3) is used but never defined anywhere in the chapter. A student meeting it for the first time cannot tell what Σ and Π stand for here.
- ch 3 [low] Figure: The table has three unlabelled cells per row, so the reader must guess that the third column is the output f.
- ch 3 [low] Lead: 'Two formulas are equivalent exactly when their principal forms match' is only true when both formulas are written over the same set of variables; otherwise the minterm indices differ.
- ch 4 [high] Worked example 1, part (b), steps 7–8: Step 7 miscounts. With p true there are 4 rows (q and r free), and p→q forces q = T in 2 of them, not 1. Saying '1 row sets q true' gives the right final answer of 1 row by accident and teaches a wrong counting step.
- ch 4 [low] Section 3 (last paragraph) and Exam traps, first bullet: 'Only MP and MT squeeze information out of an implication' and 'only modus ponens and modus tollens are valid for an implication' contradict the chapter's own table, where hypothetical syllogism, constructive dilemma and destructive dilemma are valid forms built on implications. A student can read this as saying HS is invalid.
- ch 4 [low] Section 1, modus tollens sentence: 'the contrapositive of p→q used backwards' is vague and can be misread as using the converse, which is invalid.
- ch 5 [low] Section 1, second test: The derivation test is introduced as "a second test" alongside the truth-table test, but a derivation can only prove inconsistency; finding no contradiction does not prove consistency. A student may think the two tests work both ways.
- ch 5 [low] Section 3, first paragraph: "¬C must then be false, so C holds" sounds unconditional. The contradiction shows only that no assignment makes Γ true and C false; C holds relative to Γ.
- ch 5 [low] Quiz Q5 answer: "It is valid for every C" uses "valid" for a formula. Validity belongs to arguments; the point is that C is a logical consequence of Γ.
- ch 5 [low] Section 2 and Worked example 1, step 5: The rule says to cite the assumption line and the line where Q appeared, but step 5 cites "lines 3 to 5", including line 4. This is a small inconsistency in citation practice.
- ch 5 [low] Section 1, first paragraph: "Satisfiable" is used for a single formula without definition, although only "consistent" was defined for sets.
- ch 5 [low] Exam traps, third bullet: "A valid argument may have inconsistent premises; anything then follows from them" can be misread as "any conclusion is true". What follows is validity, not truth.
- ch 6 [low] Exam traps, fourth bullet: The bullet reads 'with P(Ravi) gives Q(Ravi) ... it does not give P(Ravi)', but P(Ravi) is already assumed, so saying it 'does not give P(Ravi)' is vacuous and hides the real trap (affirming the consequent). A student may misread it as a claim about the converse.
- ch 6 [low] Figure: The figure caption states as fact that the BTech set sits inside the discrete-math set, i.e. every BTech student studies discrete mathematics. That is only an assumed premise of Worked example 1, not a true statement about students, and the caption does not say so.
- ch 7 [low] Section 1, figure introduction: The sentence 'The figure proves n odd → n² odd' overstates the figure. The figure uses n = 7 as a check and ends with '49 is odd', so it illustrates the proof rather than proving the universal claim by itself. This can blur the line between an example and a proof.
- ch 7 [low] Exam traps, universe bullet: The phrase 'may fail for all real numbers' is ambiguous and can read as 'fails for every real number'. The intended meaning is that a claim true on the integers may fail when the domain is all real numbers, i.e. for some real number.
- ch 8 [high] Section 2, well-ordering proof: The proof supposes P(n) fails for some n≥0, but the induction claim starts at n₀. If n₀ > 0, the least counterexample m could lie below n₀, where neither the base-case case m=n₀ nor the inductive-step case m>n₀ applies. The proof is therefore incomplete for general n₀.
- ch 8 [low] Section 1 and Exam traps: The sentences 'A claim about n≥3 with base n=1 is incomplete' and 'A claim from n=2 with base n=1 does not start' are too absolute. If P(1) is meaningful and the inductive step is proved for all k≥1, starting at 1 proves the claim for n≥3 or n≥2 (and more). The real issue is using a base outside the domain where P(n) is stated, or failing to bridge the gap.
- ch 9 [high] Section 2, quantifier removal: The two steps are given in the wrong order: the text says to drop ∀ first and only then handle ∃y. If a student follows that order, the ∀x has already been removed when ∃y is reached, so the condition 'if no ∀ surrounds it' is always satisfied and ∀x∃y Loves(x,y) becomes Loves(x,a) instead of Loves(x,f(x)). That is exactly the error the paragraph itself warns against.
- ch 9 [low] Section 1, resolution rule formula: The symbol ⊢ is used to mean 'the right side is the resolvent'. In standard logic notation ⊢ means 'is derivable from', and the chapter itself uses 'entails' elsewhere, so a student can read the line as a derivability claim rather than as the definition of the resolvent.
- ch 9 [low] Section 2, unification paragraph: The chapter never states that two predicate clauses being resolved must have no variables in common; without renaming apart, resolving {P(x)} with {¬P(x)} looks legal and yields □, which is wrong.
