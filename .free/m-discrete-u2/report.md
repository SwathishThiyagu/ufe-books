# m-discrete-u2: free-model run

- Book: `books/common/m-discrete/m-discrete-u2.html`
- Status: ok
- Model calls so far: 20 (75,045 tokens in, 180,832 out), 5.5 minutes

## Checker

```
m-discrete-u2.html: 7 chapters, 13374 words, 8 figures, 130 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, roster/set-builder definitions: The set-builder example {x : x is even and x < 10} = {2,4,6,8} never states the domain. As written, 0, -2, -4 ... also satisfy the rule, so the listed roster is only correct if x ranges over positive integers. A student copying this into an exam answer loses marks.
- ch 1 [low] Section 1, inductive definition paragraph: "3 ∈ S, and if x ∈ S then x + 3 ∈ S, so S contains all positive multiples of 3" is true but incomplete: the rule alone allows larger sets such as {3,6,9,...} ∪ {100}. Only the smallest set closed under the rule is the multiples of 3.
- ch 1 [low] Section 2, symmetric difference: "Some syllabi call it Boolean sum" is ambiguous: in Boolean algebra the Boolean sum is OR, i.e. union, and students who meet switching algebra later will read the term the other way. Most books call A △ B the ring sum or mod-2 sum.
- ch 1 [low] Section 2, Cartesian product: "A pair is not a set: (2,4) ≠ (4,2)" can be misread as denying that ordered pairs have any set definition, and the real point (order matters) is buried.
- ch 2 [low] worked example 1, dry run: The dry run table is presented as a trace of the code, but the code prints one 0/1 value (not the pair) for all nine ordered pairs, while the trace lists only the three pairs (1,1), (1,2), (1,3) with a 'pair' column the program never prints. A student may think the program outputs pairs or only three lines.
- ch 2 [low] section 3, last sentence: The forward reference to the functions chapter is plain text with no link, so a phone reader cannot jump to it, unlike other chapter links in the series.
- ch 3 [high] Section 3, repeated squaring sentence: The method described is wrong. Computing only R, R², R⁴, … and OR-ing them misses odd powers. Example: on {1,2,3,4}, R = {(1,2),(2,3),(3,4)} has (1,4) in R³, but (1,4) is not in R, R² or R⁴.
- ch 3 [high] Exam traps, fourth trap: It treats 'adding a self-loop because a vertex lies on a cycle of length 2 or more' as a mistake, but that is correct: a cycle through a gives a non-empty path from a back to a, so (a,a) ∈ R⁺. The trap as written contradicts the next sentence.
- ch 3 [high] Section 1 and Exam traps, second trap: The justification 'a shortest path can use up to n−1 edges, so include Rⁿ' is wrong for self-pairs. In a 3-cycle, (1,1) needs a path of length 3 = n. The statement also suggests R^(n−1) would suffice. The conclusion (use powers up to Rⁿ) is right, but the reason is not.
- ch 3 [low] Exam traps, first trap: The clause 'even when i = j is not forced' is unclear and may confuse. k is only an intermediate; i and j are start and end and may be equal or different.
- ch 3 [low] Quiz Q5: The explanation reverses the concatenation order. W[k][i] is a path k→i and W[j][k] is j→k; together they give j→k→i, a path from j to i. The answer's phrase 'k to i followed by j to k' does not chain correctly.
- ch 4 [low] Section 3, last sentence: The forward reference "see Unit 4 for modular arithmetic inside these blocks" is vague: it does not say which chapter, it breaks the book's habit of linking chapters, and "inside these blocks" is loose. Arithmetic modulo m is defined on the classes (the quotient set ℤ/mℤ), not inside a single class.
- ch 5 [high] Section 3, paragraph on upper and lower bounds: The example 'For B = {4, 6} the only upper bound is 12 ... the lower bounds are 1 and 2, so GLB = 2' does not say which poset it is working in. The paragraph just before uses the poset {2, 3, 4, 6}, and in that poset {4, 6} has no upper bound at all and only 2 as a lower bound (1 is not in the set). A student reading straight through gets the wrong numbers.
- ch 5 [low] Worked example 1, step 11: 'Height' appears for the first time in the final step and is not defined anywhere in the chapter; textbooks also differ, some counting elements of the longest chain and some counting its edges.
- ch 5 [low] Section 2, first sentence: The definition of comparable and incomparable is repeated word for word from Section 1, which makes the student think a new distinction is being introduced.
- ch 6 [low] Section 2, surjection formula: The symbol S(n,m) is the standard notation for the Stirling number of the second kind, so a student who meets Stirling numbers later will be confused. The number of surjections is m! times the Stirling number, not the Stirling number itself — so the chapter's S(n,m) does contradict a widely used convention.
- ch 6 [low] Exam traps: The traps cover the size condition for injections (n ≤ m) and for bijections (n = m), but never state the size condition for surjections. A student can wrongly believe a surjection from a 3-element set onto a 5-element set exists.
- ch 6 [low] Beyond: The pointer 'inverse function theorem' names a calculus result about derivatives of inverse functions, not the idea that a bijection has an inverse function. A student searching that term lands on the wrong topic.
- ch 6 [low] Beyond: The sentence 'an injective hash avoids collisions' may leave students thinking real hash functions such as those used in cryptography or databases are injective. A hash that squeezes long inputs into a fixed short output can never be injective; it only keeps collisions rare.
- ch 7 [low] Section 1, order paragraph: "f ∘ g ... exists only when C ⊆ A" states a sufficient condition as if it were necessary. f ∘ g is defined whenever every output of g lies in A, that is, when image(g) ⊆ A; if g is not surjective this can happen even though C is not contained in A.
- ch 7 [low] Quiz Q7, answer: The closing clause "since two elements of B with the same image do not affect g ∘ f" is wrong as written: if both those elements lie in the image of f, they do break injectivity of g ∘ f. The point only holds for elements of B outside the image of f.
- ch 7 [low] Section 1, associativity paragraph: "Composition also carries quality along" is vague wording; a student will not know what "quality" means here.
