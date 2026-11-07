# c-toc-u6: free-model run

- Book: `books/cse/c-toc/c-toc-u6.html`
- Status: ok
- Model calls so far: 34 (137,718 tokens in, 261,857 out), 7.2 minutes

## Checker

```
c-toc-u6.html: 8 chapters, 14761 words, 9 figures, 162 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1, output line: The output shows only 6 and 42, but part (c) asks for the final answer and the answer line says the machine prints yes. A student cannot match the shown output to the three-part question.
- ch 1 [low] Quiz Q4: The phrase before it answers is ambiguous. The answer 20 counts the whole of round 4, but if the decider answers as soon as M accepts in round 4, it has used 2(1+2+3)+4 = 16 simulated steps. The worked example avoids this by asking for the count by the end of that round.
- ch 1 [low] Section 2, recursive closure under Kleene star: The phrase only finitely many splits exist, and each split is tested is vague for Kleene star. For star you must test all decompositions of w into any number of factors from L, not just one split into two parts.
- ch 1 [low] Section 2, complement row paragraph: The sentence that is exactly why the complement cannot be accepted by the same machine only shows that one particular r.e. machine fails on the complement. It does not prove that no machine accepts the complement. The non-closure of r.e. under complement needs the complement theorem and L_u.
- ch 1 [low] Figure aria text: The aria says the halting language's complement is outside, but the outer item shown is co-L_u, the complement of the universal language, not the complement of HALT. The figure and the spoken description do not match exactly.
- ch 2 [high] Section 2, end of the undecidable-for-CFG paragraph: The text lists only three undecidable questions for context-free grammars (is L(G) = Σ*, are two CFGs equivalent, is G ambiguous) but then says "for a DFA all four of these are decidable". The count contradicts the list, and no fourth question exists, so a student counting the items gets confused about what was claimed.
- ch 2 [low] Section 2, P_TM bullet: P_TM = {⟨M⟩ : M ever writes a stated symbol a on its tape} leaves the starting tape and the status of a undefined. If a already sits on the input tape the answer is trivially yes, and the undecidability claim only holds when the machine starts on a blank tape and a is a fixed non-blank tape symbol. As written a student may read the problem as decidable.
- ch 3 [low] Section 1 (after the A_TM formula): The sentence 'No Turing machine halts on every coded pair and answers yes or no correctly' states decidability only for valid codes. A decider for HALT must halt with the right answer on every string, including strings that are not codes of any (M,w), which it must reject.
- ch 3 [low] Section 1 (last paragraph of the section): 'HALT is the cleaner set ... because halts has only two outcomes, while accepts also has a rejecting halt' reads as if a machine has three possible answers. The real difference is that a no answer for HALT always means looping forever, while a no answer for A_TM merges rejecting and looping.
- ch 3 [low] Section 2 (the D construction and the line after it): D is defined only for inputs of the form ⟨M⟩. What D does when its input is not the code of a Turing machine is left unstated, so D is not fully defined as a machine. Also, the step 'By the construction, that happens exactly when D loops on ⟨D⟩' is justified by the assumed correctness of H, not by the construction of D.
- ch 3 [low] Section 3 (variant bullets): The symbol ε is used in HALT_ε without being defined for this chapter.
- ch 4 [low] section 2: The halting set is named A_TM. In standard textbooks A_TM means acceptance ({⟨M,w⟩ : M accepts w}), while the halting problem is usually called HALT (or K). A student who has memorised A_TM as acceptance will be confused, and may lose marks writing this name in an exam.
- ch 4 [low] worked example 1: The example is titled 'Use Rice's theorem', but steps 3–6 do a full reduction from halting instead of applying the theorem. Steps 1–2 already prove FIN undecidable by Rice, so the rest reads like a contradiction of the title and can make students think every Rice application needs a fresh reduction.
- ch 4 [low] figure caption: 'The dashed path is the case ∅ ∉ P' is misleading: the whole diagram is drawn under the assumption ∅ ∉ P, so the dashed edge does not mark that case. The dashed edge is only the branch where M′ loops and accepts ∅, which is outside P precisely because ∅ ∉ P.
- ch 5 [high] Section 3, proof outline: It says 'A match in the MPCP instance corresponds to a halting computation of M on w.' A computation that halts but rejects does not give a match. The closing dominoes of the encoding can only be applied when the machine is in the accepting state, so the correspondence is with an accepting computation, not with any halting one. The chapter's own opening line of Section 3 (the acceptance problem) contradicts this sentence.
- ch 5 [low] Worked example 1, after the dry run table: The block 'output: 6 / 6 / 1' appears with no explanation of what the three numbers are, so a student cannot tell whether it is a program output, a length, or a flag. The answer later uses '6' for the length and '1' for the equality check, but only there.
- ch 6 [high] Section 2, Gödel numbering formula: The exponents are lost in the display: '2n₁3n₂⋯pkn_k' reads as 2×n₁×3×n₂×⋯×p_k×n_k, which is plain multiplication, not the prime-power code. A student copying this gets the wrong number.
- ch 6 [high] Exam traps, first trap: It says that for r.e. languages that are not recursive 'χ_L is partial'. This contradicts Section 3, which correctly states χ_L is always total (it is 1 or 0 on every string). For a non-recursive r.e. language χ_L is total but not computable; what is partial computable is the semi-characteristic function, 1 on L and undefined outside.
- ch 6 [high] Worked example 1, step 6: It says a total machine for g could be used 'by computing g and reading 1 or undefined'. A total computable g never outputs undefined; on inputs where M does not halt it must output some defined value, taken as 0. As written the step contradicts the word 'total' and the reasoning does not hold.
- ch 6 [low] Section 1, boxed formula: The 'where' line mentions 'the loop branch', but the formula above it defines the total case, where no loop branch exists. The mismatch makes the definition look self-contradictory.
- ch 7 [low] Section 2, hierarchy theorem paragraph: The sentence 'with more time or space, strictly more languages are decidable' is loose. Because TIME and SPACE are defined with O(), doubling the bound gives the same class; for time the theorem needs the larger bound to exceed the smaller by about a log factor, and 'decidable' suggests decidability rather than membership in the class.
- ch 7 [low] Worked example 1, steps 3 and 4 and the dry-run table: Step 3 counts 'cells scanned' and step 4 turns that into 'total steps', and the table repeats the same number under both columns. Time counts head moves, which can exceed distinct cells scanned when the head revisits cells; the two are only equal here because each round is one sweep right and one sweep left. A student may take 'steps = cells scanned' as a general rule.
- ch 7 [low] Section 2, second bullet: The bullet TIME(f(n)) ⊆ SPACE(f(n)) 'for f(n) ≥ n' sits inside the discussion of the read-only input tape model. In that model the condition f(n) ≥ n is unnecessary: a machine running f steps touches at most f + 1 work cells for any f. The condition belongs only to the single-tape model where input cells count as space.
- ch 8 [high] Worked example 1, step 5 and answer: The comparison count is wrong. Checking that 5 vertices are pairwise distinct by comparing sequence entries needs 10 comparisons (4+3+2+1), not 5. Comparing only 5 times cannot prove distinctness unless the verifier uses an extra marking array, which is not what the step describes. The total work is therefore 5 edge lookups plus 10 comparisons = 15 operations for n=5.
- ch 8 [low] Figure caption: "nobody knows whether the two inner containments are strict" can mislead a student into thinking P = NP = PSPACE is still possible. It is known that P ≠ PSPACE (space hierarchy theorem), so at least one of the two containments must be strict; only which one is unknown.
