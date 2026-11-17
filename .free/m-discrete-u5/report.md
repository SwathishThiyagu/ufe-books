# m-discrete-u5: free-model run

- Book: `books/common/m-discrete/m-discrete-u5.html`
- Status: ok
- Model calls so far: 21 (75,019 tokens in, 193,845 out), 5.5 minutes

## Checker

```
m-discrete-u5.html: 7 chapters, 10510 words, 8 figures, 122 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, the "Failure" bullet (B = {2, 3, 6, 12}): The argument is wrong: 6 divides 12, so 6 ≤ 12 in the divisibility order and 6 IS the least upper bound of 2 and 3 inside B. So 2 ∨ 3 = 6 exists. The same wrong reasoning is used for the pair 6, 12: their lower bounds in B are 2, 3 and 6, and 6 is the greatest of these, so 6 ∧ 12 = 6 also exists. B is still not a lattice, but for a different reason.
- ch 1 [high] Exam traps, first bullet: "In {2, 3, 6, 12} the elements 6 and 12 are both upper bounds of 2 and 3, and neither is least" is false: 6 divides 12, so 6 is the least upper bound.
- ch 1 [high] Quiz Q7: The answer is wrong. In B = {2, 3, 6, 12}, 6 divides 12, so 6 is the least upper bound of 2 and 3 and 2 ∨ 3 = 6 exists. The statement "the meet 6 ∧ 12 fails for the same reason" is also wrong: the lower bounds of 6 and 12 in B are 2, 3, 6, and 6 is the greatest, so 6 ∧ 12 = 6.
- ch 1 [high] Beyond: "Every finite lattice can be drawn as a family of sets closed under union and intersection, which is Birkhoff's representation theorem" is false. Birkhoff's theorem holds for finite distributive lattices; a general finite lattice such as the diamond M3 is not of this form.
- ch 1 [low] Worked example 1, output: Six quantities are asked for in parts (a)–(c), but the output lists seven numbers (12, 2, 6, 1, 12, 1, 1). The last 1 has no label and a student cannot tell what it refers to.
- ch 1 [low] Worked example 1, step 8: "both stay inside A for all 36 pairs" is ambiguous: earlier the chapter counts unordered pairs ({2, 3} and so on), and six elements give 21 unordered pairs, not 36.
- ch 2 [low] Figure caption: The highlighted set S={1,2,4,12} is called a 'diamond', but in this Hasse diagram 1<2<4<12 is a chain (a single path), not a diamond; 'diamond' also has a technical meaning (M₃/N₅ shape) that does not apply here. A student may look for a four-corner diamond in the picture and get confused.
- ch 2 [low] Section 2, last paragraph: 'Merge point' is data-flow jargon that is only introduced in the Beyond section, so it is undefined here. Also 'the meet can only rise as well' is correct but reads as a surprise; it needs the reason (meet is monotone in the same direction, not the opposite).
- ch 3 [low] Section 1: Section 1 says "The figure shows L×L for L={0,1}", but the figure is placed after Section 3. On a phone the reader has to scroll far to find the picture being described.
- ch 3 [low] Section 2: The sentence "Here a,b are elements of L." repeats what the formula's where-clause already says ("a,b are elements of L").
- ch 3 [low] Section 2: The claim "The converse fails" is left without an example or pointer, so a student cannot see why an order-preserving map may not be a homomorphism. The map f in Section 3 is exactly such an example.
- ch 3 [low] Quiz Q5: The answer "When h is a bijective lattice homomorphism" is correct, but it does not say that for lattices the inverse of a bijective homomorphism is automatically a homomorphism. A student may think the inverse has to be checked separately.
- ch 5 [low] Section 1: The text says 'A lattice with all four properties is a Boolean algebra, and we require 0≠1', but only three properties of the lattice are listed (bounded, distributive, complemented), and the figure counts a different set of four (lattice, bounded, distributive, complemented). A student cannot tell what the four are, and 0≠1 is mentioned twice.
- ch 5 [low] Exam traps, first bullet: The bullet shows the wrong expression (a∨b)∧c but never says the equality fails, so a student may read the mistake as bad bracketing rather than a false identity.
- ch 5 [low] Section 3: After choosing A={1,2} and C={2,3}, the line 'The order in P(S) is subset: A≤C means A⊆C' uses the same letters A and C, and a reader may take it as a claim that A≤C here, which is false since {1,2}⊄{2,3}.
- ch 6 [low] Section 1 and Section 2, the sentence 'Every Boolean function has both forms': The two degenerate functions are not handled. For the constant-0 function no row has f=1, so the canonical DNF is an OR with no terms; for the constant-1 function no row has f=0, so the canonical CNF is an AND with no terms. A student meeting f=0 or f=1 will not know what to write.
- ch 6 [low] Worked example 1, steps 6 and 7: The substitution values are not written down and the dot product sign · appears for AND without being defined earlier (earlier AND was shown by juxtaposition, as in x′y). 'DNF=0·0+1·1' is hard to follow on a phone.
- ch 6 [low] Lead and 'Beyond': The word 'polynomial' is used in two ways: Section 1 defines a Boolean polynomial as any expression using OR, AND and NOT, while 'Beyond' calls the algebraic normal form (XOR and AND over GF(2)) a Boolean polynomial. The same name for two different objects can confuse.
- ch 7 [high] Worked example 1, step 10: The five homomorphism identities are checked only for A={1,2} and C={2,3}. That single pair cannot prove h is a Boolean homomorphism; the sentence 'All five laws hold, so h is a Boolean homomorphism' models an invalid proof method.
- ch 7 [low] Section 1: The symbol U is used in S={∅,{1},{2,3},U} without being defined in that paragraph.
- ch 7 [low] Quiz Q4: The universe U is not specified, and h(U)=1 only if 1∈U.
- ch 7 [low] Worked example 1, answer: The list of ten computed values (1, 0, 1, ...) is not labelled, so a student cannot map each value to the quantity computed.
