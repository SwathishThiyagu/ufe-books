# m-discrete-u3: free-model run

- Book: `books/common/m-discrete/m-discrete-u3.html`
- Status: ok
- Model calls so far: 26 (88,612 tokens in, 179,616 out), 4.4 minutes

## Checker

```
m-discrete-u3.html: 8 chapters, 13081 words, 9 figures, 134 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1, final answer line: The answer says 66 'ticket-building choices', but 6 of the 66 are preset combos that the passenger does not build from class, quota and payment. The wording contradicts step 4 and can confuse a student about what is being counted.
- ch 1 [low] Quiz Q6, answer: 'The sum 7 counts single items only' is loose. A student may read it as 7 outcomes of some kind, when 5 + 2 is simply the count of the separate plans (5) plus the separate add-ons (2), with no pair included.
- ch 1 [low] Beyond: Telling the reader that a web search for two phrases 'leads to industry material' gives no actionable source and reads as filler.
- ch 2 [high] Section 1, formula paragraph: The exponent is lost: the text says "each of the r positions has n choices, so the count is nr" and later "you cannot use nr". Read literally, that is n times r, which is the wrong count for arrangements with repetition.
- ch 2 [high] Exam traps, first bullet: "the count is not 104" reads as one hundred and four. The intended number is 10 to the power 4 = 10000, so the trap loses its meaning as written.
- ch 3 [high] Section 1, paragraph 3: The chapter calls this argument 'a direct proof' and then describes denying the conclusion to reach a contradiction. Denying the conclusion is proof by contradiction (or contrapositive), not direct proof. Section 3 uses the same style of argument and correctly calls it proof by contradiction, so the chapter contradicts itself and students will mislabel the method in exams.
- ch 3 [low] Beyond: 'A probabilistic version, sometimes called the probabilistic method, proves that a random assignment has a good chance of avoiding the worst box' is vague and confuses two things. The probabilistic method is a proof technique for showing that a good assignment exists, not a variant of the pigeonhole principle, and it does not talk about a 'chance of avoiding the worst box'.
- ch 3 [low] Quiz Q7: The question asks for the minimum possible maximum bucket size, and the answer only says the maximum is 'at least 12'. It never shows that 12 can actually be reached, so the word 'minimum' is left unsupported.
- ch 4 [high] Section 4, after the onto formula: The exponents are missing their superscript tags. The text reads "and (n−k)m counts functions into the remaining elements. The k=0 term is nm." Without superscripts these read as the products (n−k)×m and n×m, which is a different (and wrong) quantity. m is already defined as the domain size, so a student will genuinely misread it.
- ch 4 [low] Section 2, sign rule sentence: "add k-fold intersections with sign (−1)k+1" is written without superscript markup, so it reads as (−1)·k + 1 rather than the alternating sign.
- ch 4 [low] Figure (Venn spec): The three circles carry only the totals 50, 33 and 20, so the six overlap regions render empty. A student can read the empty overlaps as zero intersections (16, 10, 6, 3), which contradicts the worked example. The caption also says each circle shows numbers divisible by "2, 3 or 5", but the Even circle shows only multiples of 2.
- ch 4 [low] Section 4, forbidden positions paragraph: "Let Ai be the set of arrangements where item i is in a forbidden position" is loose when one item has several forbidden positions; it is not clear whether Ai is one arrangement-set per item or one per item-position pair.
- ch 5 [high] Section 3, paragraph starting "P and any polynomial coefficients are unknowns": The text says initial conditions fix "any constants in the particular part". This contradicts the sentence just before it and the standard method: the unknown coefficients of the trial particular solution are found by substituting the trial into the recurrence, not from the initial conditions. A student who follows this will try to fit P from a_0 and get a wrong or over-determined system.
- ch 5 [low] Section 3, table row "constant C | P": The table notes the exceptional case only for the K·b^n row. A constant forcing is the case b = 1, so the constant row also needs the adjustment when 1 is a characteristic root; otherwise the table reads as if p_n = P always works for constant forcing.
- ch 6 [high] Section 2, first paragraph: The sentence after 'Three series cover most exam problems' is garbled: 'As a numeric identity they need |x|3.2.' It is unreadable and the condition is incomplete, so a student cannot tell when the series formulas are valid as numbers.
- ch 6 [low] Section 2, Convolution bullet: The symbol b in h_n = Σ_{k=0}^{n} a_k b_{n−k} is never defined. Only a_n has been introduced, and the formula block lists just a, C(n,k) and n.
- ch 6 [low] Section 3, first paragraph: The partial-fraction recipe 'write the fraction as A/(1−αx)+B/(1−βx)+⋯' silently assumes the fraction is proper and that Q(0) ≠ 0. A student who meets P of degree ≥ deg Q, or a factor x in Q, will get stuck.
- ch 6 [low] Lead and Section 1: The remark 'Some syllabi call this simply the generating function' appears twice, in the lead and again in Section 1, which reads as repetition.
- ch 6 [low] Lead: 'adding, shifting and multiplying sequences become algebra on polynomials' is imprecise: G(x) is a power series, not a polynomial, and the point of the chapter is that infinite series behave like polynomials here.
- ch 7 [high] Section 3 (partial fractions and the cover-up shortcut): The cover-up instruction is wrong. If G(x) = P(x)/Q(x) = A₁/(1 − a₁x) + A₂/(1 − a₂x) + ⋯, then multiplying through by Q(x) gives P(x) = A₁Q(x)/(1 − a₁x) + A₂Q(x)/(1 − a₂x) + ⋯. Putting x = 1/aᵢ does not isolate Aᵢ — it gives P(1/aᵢ) = Aᵢ·∏_{j≠i}(1 − a_j/aᵢ). A student following this step in an exam gets an answer off by the factor ∏_{j≠i}(1 − a_j/aᵢ).
- ch 7 [low] Quiz Q2 answer: The last sentence gives the wrong reason. No term is missing because the shifted index k runs from 0 upward, so the sum is over the whole sequence; this is true whatever index the recurrence starts at. A reader can take away that the completeness depends on the recurrence starting at n = 1, which is not so.
- ch 8 [low] Lead: The sentence 'Both show up in testing whether a shuffle fixed anything, in seat-allocation puzzles, in hashing, and in the inclusion–exclusion machinery' attaches all four uses to both topics. Distribution problems have nothing to do with a shuffle fixing something, so a student may misread what each model is for.
- ch 8 [low] Section 1, 'Why the recurrence holds': The sentence 'If letter j avoids envelope 1, then the remaining n − 1 letters carry exactly the original restriction: D_{n−1} ways' skips a step. Letter j is still there and envelope 1 is still free, so it is not obvious that the leftover problem is again a plain derangement of n − 1 objects.
- ch 8 [low] Worked example 1, step 2: The line 'there are C(4, 1) = 4 such sets: 4 × 6 = 24' produces 24, the same number as the total 4!, and a student may think the two 24s in step 6 cancel for a reason other than inclusion–exclusion.
