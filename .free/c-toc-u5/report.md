# c-toc-u5: free-model run

- Book: `work/claude_figs/c-toc-u5/tree/books/cse/c-toc/c-toc-u5.html`
- Status: ok
- Model calls so far: 27 (99,132 tokens in, 251,436 out), 7.8 minutes

## Checker

```
c-toc-u5.html: 7 chapters, 12205 words, 8 figures, 161 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, ID definition: The sentence "Cells past the last non-blank are all □, so we never write them" is stated for the whole ID, but a blank cell can lie between the last non-blank and the head. If those blanks are left out of α, the head position is lost and two different snapshots get the same ID. Example: tape 1, head on cell 2 in state q0 must be 1□q0; written as 1q0 it wrongly says the head is on cell 1.
- ch 1 [low] Worked example 1, step 3 (and Quiz Q5): Step 3 gives the ID as 10q2□ and then says it is "written 10q2 when the trailing blanks are dropped". The □ there is the scanned cell, not a trailing blank, and the exam trap in the same chapter says the scanned □ must not be dropped. Step 3, the answer line (which uses 10q2□) and the trap contradict each other, so a student cannot tell which form to write in the exam.
- ch 1 [low] Section 2, transition diagram: "Several labels may share one arrow when they differ only in the symbol read" is too narrow. Two labels may also differ in the symbol written and still use one arrow, provided the destination state and the direction are the same.
- ch 1 [low] Beyond: "the number of distinct IDs a small machine visits is the object of study" misdescribes busy-beaver search. That search maximises the number of steps (and of 1s left on the tape) before halting; the count of distinct IDs is only the bound used to conclude that a machine has entered a loop.
- ch 1 [low] Exam traps, last bullet: The chapter says a left move from the leftmost cell is "not allowed" but never says what the model does when a transition asks for one, so the definition of a move is incomplete at the left end of the tape.
- ch 3 [high] Section 3 (the line 'The order matters; erase first and the count is wrong') and Exam trap 3: This claim is false. The two steps act on the count in opposite directions. Overwriting the separator 1 with 0 adds one zero (+1). Erasing one zero removes one zero (−1). The net is m+n zeros whether the erase comes before or after the merge. So for m=2, n=1, input 0010, erasing the last 0 first gives 001, and merging then gives 000 — still three zeros. The count is right either way, so a student who checks with a small example will think the chapter is wrong.
- ch 3 [high] Quiz Q4 and its answer: The answer describes a wrong result. It says that erasing first and merging afterwards 'no longer has m+n zeros in one block' and that the machine 'can halt with the wrong count'. The count is correct: −1 for the erase, +1 for the merge, total m+n. On the empty-argument case m=2, n=0, erasing and then merging the separator gives exactly two zeros, not a wrong count.
- ch 3 [low] Figure (aria text): The screen-reader description says the separator is removed and 'a third 0 added, changing 0010 into 000'. The 'Before' tape already has three zeros, so adding one and changing nothing else cannot produce 000. The description leaves out the erase, and a student who cannot see the rows gets the wrong procedure.
- ch 4 [high] Section 1 and Worked example step 10: Section 1 states that each tape is infinite to the right, but step 10 moves head 2 left from cell 0 onto a cell left of cell 0. On a one-way infinite tape that move is not defined, so the trace of moves 6–7 (and the 2n+3 count that depends on them) is illegal under the chapter's own model. A student will not know which convention is in force.
- ch 4 [high] Section 3, paragraph on the nondeterministic simulation: 'On an input where every branch rejects, the search never stops' is wrong. If every branch halts and rejects, the configuration tree is finite, breadth-first search exhausts its queue and the deterministic machine halts and rejects. The simulation runs forever only when some branch runs forever.
- ch 4 [low] Section 3, Section 1 formula, Section 2 formula, Quiz Q1 answer: Superscripts are lost in several formulas, so students see 'b + b² + … + bt' (reads as b times t), 'Γk' (reads as one symbol Γk rather than a k-tuple), and '2Q × Γ × {L, R, S}' (reads as 2 times Q).
- ch 4 [low] Worked example, step 5 and answer: The listed transitions do not halt on inputs with more 1s than 0s. On 011, after the single 0 is erased, δ(q1, 1, B) keeps moving head 2 left with head 1 stuck on a 1, so the machine loops forever instead of rejecting. The machine does accept exactly L, but calling step 5 the 'halting rules' suggests it decides L.
- ch 5 [high] Worked example 1, steps 1–5 and answer (and quiz Q3 that depends on it): The machine M is called a machine that accepts strings ending in 1, but its accept state q1 also has outgoing transitions (q1,1 → q1,R and q1,0 → q0,R). Under the standard textbook convention a Turing machine halts the moment it enters the accept state, so M halts after only 1 move on 101, and the same machine would also accept 10, 100 and every other string starting with 1 — it does not accept exactly the strings ending in 1. The run of 3 moves is only valid under the other convention (a state may be final and still move; M accepts if it halts in q1), and the chapter never says which convention it uses.
- ch 5 [low] Figure, edges from 'Simulated state' and 'Simulated tape' to 'Accept or reject': Both edges are labelled 'decides', which clashes with Section 3's point that U is a recognizer, not a decider, and may loop.
- ch 6 [low] Section 3 and Exam trap 5: 'Turing-complete' is defined as being able to 'simulate a Turing machine'. Under that wording a language that simulates one particular machine would qualify, which is not the standard meaning; Turing completeness means simulating any Turing machine.
- ch 6 [low] Section 1, the statement and the formula: The thesis is stated only for total functions from natural numbers to natural numbers. Standard treatments state it for partial functions too, and for functions on strings as well as numbers. A student may conclude the thesis says nothing about procedures that loop on some inputs, which is exactly the case undecidability arguments need.
- ch 6 [low] Worked example 1, steps 1-5: Each step shows the number twice ('step 1: 1. The term applies...'), which reads like a formatting error.
- ch 6 [low] Worked example 1, step 2: n+1 is not a pure lambda term; pure lambda calculus has only variables, application and abstraction, and needs Church numerals and a successor function to add. The substitution step is correct only as a shorthand, and a sharp student may object.
- ch 7 [high] Section 1, paragraph 1: The formula says the control needs mk states for alphabet size m and k remembered symbols. As written this means m×k, not m^k; for example m=3, k=2 gives 6 instead of 9. The correct number of tuples is m^k.
- ch 7 [low] Worked example 1: The example says the machine starts in q00 but also says inputs shorter than two bits are rejected by a separate start state. This is inconsistent about whether q00 is the start state or a memory state reached after a separate start state.
