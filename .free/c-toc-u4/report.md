# c-toc-u4: free-model run

- Book: `books/cse/c-toc/c-toc-u4.html`
- Status: ok
- Model calls so far: 22 (81,768 tokens in, 228,668 out), 6.7 minutes

## Checker

```
c-toc-u4.html: 5 chapters, 9202 words, 6 figures, 104 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q7: The final stack in the answer is wrong. Changing only δ(q₁,b,A) to {(q₁,AA)} leaves the first b of aabb to be read in q₀, where it still pops A. The second b is read in q₁ and pushes two A's. So the run ends at (q₁, ε, AAZ₀), not (q₁, ε, AAAZ₀). aabb is still rejected because the top is A, so δ(q₁,ε,Z₀) is not enabled.
- ch 1 [low] Quiz Q6: The question asks for the first three IDs for ab, but the answer shows four IDs (the whole trace). The first three IDs are correct; the fourth is extra and can confuse the count.
- ch 2 [low] Figure (final state to empty stack): The dashed edge labelled 'while stack non-empty' runs from the eraser node e back to the 'Final state' node d. In the construction the eraser never returns to the old final state: once control is in qe it loops on qe alone. As drawn, the figure contradicts the caption and the construction, and a student may think control alternates between the final state and the eraser.
- ch 2 [low] Section 2 and Worked example 1: The bullet list of the construction in Section 2 uses one order (1 choose X₀, 2 add q₀′, 3 keep old moves, 4 add qe and the erase moves from final states, 5 set the eraser loop), and the text refers to 'step 4 hands control to qe'. The worked example renumbers the same actions in a different order (step 3 = erase moves from final states, step 4 = eraser loop, step 5 = keep old moves), so a student cross-checking the two numbering schemes gets confused.
- ch 2 [low] Exam traps, second trap: 'The eraser may start only after the old machine has finished' is loose: the erase ε-moves are enabled whenever the machine is in a state of F, even with input still unread (such a run simply dies because the eraser reads no input). Also 'accepts prefixes it should reject' is imprecise, since acceptance always uses up the whole input.
- ch 3 [high] Section 3 (Complement) and Quiz Q5: The complement construction given is wrong. Swapping final and non-final states on a DPDA that can stop before the end of the input does not give the complement, and 'treat a stuck machine as rejecting' makes it fail: if the original machine gets stuck with input left over, it rejects, so the complement must accept that string, but the swapped machine gets stuck in exactly the same place and also rejects. The closure result (DCFLs are closed under complement) is true; only the construction is faulty, and it is repeated in the Q5 answer ('stuck counts as rejecting').
- ch 3 [high] Beyond box: 'The LR and LL families in tools such as yacc, bison and ANTLR accept exactly the deterministic context-free languages' is false. Only LR(1) grammars generate exactly the DCFLs. LL(k) grammars (the family ANTLR belongs to, in its LL(*) form) and LALR(1) grammars (yacc, bison) generate proper subclasses of the DCFLs, so those tools accept fewer languages, not exactly the DCFLs.
- ch 3 [low] Beyond box: 'Grammar conflicts reported by those tools mean the grammar is not deterministic' overstates it. A conflict means the grammar is not in that tool's class (for example LR(1) but not LALR(1)); the language can still be a DCFL.
- ch 3 [low] Quiz Q3 answer: 'each (q, a, X) has exactly one move' is only right for a complete DFA. A DFA may be partial, and then δ(q,a,Z₀) is empty; the DPDA definition allows that.
- ch 3 [low] Section 1, determinism formula: Rule 1 is written as |δ(q, a, X)| ≤ 1 with a an input symbol, so as written it does not cap the ε-entry, while the text says 'Rule 1 caps every set at one move'. A student may think several ε-moves are allowed.
- ch 4 [high] Section 1, worked example step 3, exam traps, quiz Q2 and Q3: The stack convention is contradictory. The start move is explicitly said to use top-left transition notation: δ(q,ε,Z₀) = {(q, S Z₀)} displays as Z₀ S. But then productions push αᴿ, and the trace displays Z₀ b S a after S → aSb. Under top-left transition notation, αᴿ puts the rightmost symbol of α on top, not the leftmost; δ(q,ε,S) = {(q, b S a)} would give display Z₀ a S b and match b first. The example only works if transition strings are read bottom-to-top, which contradicts the start move. Students cannot tell whether to push α or αᴿ.
- ch 4 [high] Section 2 and quiz Q8: The construction adds a new start symbol S, so the grammar has |Q|²|Γ| + 1 variables, not |Q|²|Γ|. Q8's 48 is only the number of [p A q] variables; the grammar also has S, so the total is 49. A student answering 48 would omit the start symbol.
- ch 4 [low] Section 2, simplification order: The order 'remove useless variables, then ε-productions and unit productions' can leave new useless variables after ε-elimination and unit-elimination. Standard simplification removes ε-productions, then unit productions, then useless symbols.
- ch 5 [high] section 1: The LL(1) condition is stated wrongly. 'No two productions of A starting with the same terminal' is not enough. The FIRST sets of the alternatives must be disjoint. Example: S → A | B, A → a, B → a has no two productions of S starting with the same terminal, but it is not LL(1). The sentence 'Such grammars are LL(1)' is therefore false.
- ch 5 [high] section 2: The clause 'the last production a top-down parser applies is the first one undone here' is misleading. The reduction list read backwards is a rightmost derivation, but the first reduction is the last production of that rightmost derivation, not the last production of the leftmost derivation. Example: for S → A B, A → a, B → b, the leftmost derivation ends with B → b but the first reduction is A → a. In the chapter example the same rule F → id appears at both ends, but not the same occurrence.
- ch 5 [low] worked example 1: The example asks for a 'top-down leftmost derivation' of a left-recursive grammar. A top-down parser cannot use this grammar as written. The derivation is a leftmost derivation, not a run of an LL parser. After section 1 says top-down parsers need no left recursion, this can confuse students.
- ch 5 [low] quiz Q6 answer: The explanation 'LL(1) is a property of a grammar, not of the language, unless every grammar for it fails' is unclear. A language is LL(1) if some LL(1) grammar generates it; it is non-LL(1) only if no LL(1) grammar exists.
- ch 5 [low] section 1: 'Vanishing production' is not a standard term; the usual term is 'nullable production' or 'ε-production'. The phrase 'hide the first real symbol' is vague and does not mention FOLLOW sets.
