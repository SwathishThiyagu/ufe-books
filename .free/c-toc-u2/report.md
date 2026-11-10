# c-toc-u2: free-model run

- Book: `work/claude_figs/c-toc-u2/tree/books/cse/c-toc/c-toc-u2.html`
- Status: ok
- Model calls so far: 39 (153,763 tokens in, 278,963 out), 7.7 minutes

## Checker

```
c-toc-u2.html: 9 chapters, 16702 words, 10 figures, 188 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] worked example 1, dry run table: The table is presented as a complete check but shows only 6 of the 14 binary strings of length ≤ 3; strings such as 00, 000, 001, 010 are silently missing, so a student may think the table is the full enumeration and wonder why some strings were skipped.
- ch 1 [low] section 2, precedence rules: 'Operators of equal precedence group from left to right' is stated for all three operators, but star is unary and cannot be grouped with anything; the rule only makes sense for + and ·.
- ch 1 [low] section 3, atoms ∅ and ε: 'Star on ∅ never creates 0 or 1' is vague; the reader is not told what star on ∅ actually produces (only ε).
- ch 1 [low] section 1, third formula: The sentence 'The set L(r) is also called a regular set' sits inside the explanation of L(r*), where r is the operand of the star; it reads as a claim about L(r*) only.
- ch 1 [low] section 1, notation note: 'A centred dot is not standard for concatenation here' is too strong; several textbooks do write 0·1 for concatenation, so the wording can mislead.
- ch 2 [low] Figure (caption and aria): The caption says "Four rewrites reduce (ε + a)* to a*" and the aria says "Four simplification steps", but the diagram has four nodes and only three rewrite edges. The worked example needs four law applications because the figure merges two of them into one arrow, so the count in the caption does not match what is drawn.
- ch 2 [low] Figure, node c note: The arrow from (ε* a*)* to (a*)* is labelled only "ε* = ε". Applying ε* = ε alone gives (ε a*)*, not (a*)*; the step also needs the concatenation identity εr = r with r = a*. A student reading only the label may think ε* = ε removes the whole ε block by itself.
- ch 3 [low] Figure and Section 3: The pipeline orders the operators as union, concatenation, star, and the caption says the final machine is 'the 10-state machine of the worked example'. But the worked example a(b+c)* applies union, then star, then concatenation. A student following the figure order will not get the same step sequence.
- ch 3 [low] Quiz Q7: The answer says merging the first machine's final with the second machine's start 'can add or remove paths through other ε-links'. In Thompson's construction both states are freshly created: f₁ has no outgoing edge other than the ε we add, and s₂ has no incoming edge, so for this construction the merge preserves the language. The stated reason is not the real reason.
- ch 3 [low] Section 2, star rule: The union rule states explicitly that the old finals stop being accepting, but the star rule only says 'Start q, final f'. A reader may keep f₁ accepting alongside f.
- ch 4 [high] Worked example 1, step 5: The chapter defines + as union (Section 1), and * as zero or more repetitions. Step 5 then writes 0 0* 1 + 1 = 0+1 + 1, using 0+ to mean 'one or more zeros', an operator that is never defined in this chapter. In the same line + is also used for union, so '0+1 + 1' can be misread as '(0 or 1) or 1' and the factoring into (0+ + ε)1 becomes impossible to follow.
- ch 4 [low] Section 3, the formula and its 'where' line: Rqq is described only as 'the self-loop on q'. When q has no self-loop, Rqq is ∅ (as the definition of Rab says), and the student needs ∅* = ε to use the formula. This is not stated, so a state with no self-loop looks like a special case.
- ch 4 [low] Worked example 1, step 8: The identity used, (0*1)* 0* = (0+1)*, is attributed to 'Chapter 2.2' in plain text; the book style asks for an inline chapter link so the reader can jump to it.
- ch 4 [low] Quiz Q1: The answer says the equation 'has solution X = P* Q'. The standard statement is that the solution is unique when ε ∉ P; without 'unique' a student can lose the mark and can also believe other solutions exist.
- ch 5 [high] Section 3, third bullet (closure properties): It says closure under complement and intersection 'comes from product constructions on DFAs'. Intersection is a product construction, but complement is not. Complement is done by swapping final and non-final states in a complete DFA; the product construction plays no part.
- ch 5 [low] Quiz Q6, answer: The answer claims 'no definite conclusion' for all three, but for L·M it only shows the regular case (L = Σ*). No example is given where L·M is non-regular, so the claim is not justified.
- ch 5 [low] Quiz Q2, answer: The answer says Arden's method and state elimination 'start from a DFA'. That is too strong: both work directly on an NFA or ε-NFA (state elimination only needs the equations of the transition graph). The ε-NFA → DFA step is the book's chosen route, not a logical necessity.
- ch 5 [low] Section 2, first bullet, and Exam traps, fourth bullet: The bound 'at most 2m states' uses m without defining it. If a student takes m as the number of input symbols only, the bound is false: a* has m = 1 symbol but needs 4 states.
- ch 6 [low] Worked example 1, steps 3–5: The exponent expressions are written without superscripts: 'z = 0p−a−k1p', 'xy⁰z = 0p−k1p', 'xy²z = 0p+k1p'. A student can misread these as products of symbols rather than powers, especially since the same paragraph writes 0ᵖ1ᵖ with a superscript elsewhere.
- ch 6 [low] Figure: In the spec, z starts at cell 2 but only cell 2 carries a mark ('muted'); cells 3–5, which are also part of z, look unmarked, so the picture does not show where z ends.
- ch 7 [high] Section 3, last paragraph: 'A missing transition is a dead state ... Without that state, swapping finals can accept strings that should be rejected.': The direction of the error is backwards for a DFA. In an incomplete DFA a missing transition kills the run, so the string is rejected both before and after swapping finals. Completing is needed because the swapped machine wrongly rejects strings that belong to the complement, not because it wrongly accepts strings outside it. Over-acceptance after swapping finals is the NFA failure, not the incomplete-DFA failure. A student will learn the wrong reason for the construction.
- ch 7 [low] Worked example 1, steps 6 and 7 and the answer line: Step 5 already shows (E,N) --1→ (E,F), so the string 1 (length 1) is already a witness. Step 6 instead reaches (E,F) through a length-3 detour, and the answer states 'witness length is 3'. That is true but misleads a reader into thinking 3 is the shortest witness.
- ch 7 [low] Section 3, membership paragraph: 'For an NFA, track the set of possible states or convert to DFA; time is O(|w| × number of states)' mixes two very different costs. Tracking state sets costs O(|w| × |Q| × |Σ|) (or O(|w| × number of transitions)), while converting to a DFA can blow up to 2^|Q| states.
- ch 7 [low] Section 1, Complement bullet: 'Take a complete DFA for L, add a dead state for every missing transition, then swap' contradicts itself: a complete DFA has no missing transitions, so the instruction to add dead states has nothing to attach to.
- ch 7 [low] Section 2, product construction paragraph: Completeness is demanded only for B in the difference case. Union and intersection through the product also need both machines complete, otherwise δ_P((p,q),a) is undefined for a string that one machine accepts, and the product wrongly rejects it.
- ch 8 [high] Exam traps, 4th bullet: The bullet says equivalent strings can "still differ, because a longer suffix may separate them". This contradicts the definition: if x ≡_L y, no suffix separates them at all, by definition. A student reading this will think two strings can be equivalent and still distinguishable, which destroys the whole idea of the theorem.
- ch 8 [low] Section 1, right-congruence sentence: "because any suffix after a is a suffix after xa" is muddled and does not show the step. The reason is that a suffix z tested on xa means testing the suffix az on x.
- ch 8 [low] Worked example 1, code block: The code block is print(4) with output 4. It shows nothing about distinguishability and teaches the reader nothing; the answer is simply restated in code form.
- ch 9 [high] Quiz Q6: The answer says 'Nothing is wrong with the observation about Python'. The premise is false: Python's re module with plain backreferences cannot match aⁿbⁿ for arbitrary n. Backreferences match a repeated copy of a captured substring (so (ab)\1 gives abab, or (.*)\1 gives {ww}), but that says nothing about counting a's against b's. Engines that do match aⁿbⁿ need recursion or balancing groups (PCRE recursion, .NET balancing groups), not plain backreferences.
- ch 9 [low] Section 1 and Section 2 (references 'subset construction (Unit 1)' and 'Moore and Mealy machines are covered in Unit 1'): Elsewhere the chapter points to precise chapters (2.1, 2.3, 2.5, 2.6), but here it switches to a whole-unit reference. A student revising subset construction right after chapter 2.3 will not know which chapter to open.
- ch 9 [low] Figure (caption and spec): The caption says 'notice that + is matched as a separate fixed-string token', but the diagram has no node for the + token: the edge goes straight from id(x12) to DFA num labelled 'next', as if the + disappeared. Also the step list names the token class 'integer' while the figure emits num(7).
- ch 9 [low] Section 2, validation paragraph: 'the answer is yes only if the machine ends in an accepting state and never entered the dead state' is redundant and slightly misleading: the dead state is non-accepting and absorbing, so ending in an accepting state already proves it was never entered, and a DFA does not have to draw a dead state at all.
- ch 9 [low] Worked example 1 step 4 and Quiz Q4: 'One extra dead state absorbs a bad first digit and wrong characters'. Over the alphabet Σ = {0,1,...,9} there are no wrong characters, and from q1 to q9 every digit is accepted, so the dead state here absorbs only a first digit in 0–5.
