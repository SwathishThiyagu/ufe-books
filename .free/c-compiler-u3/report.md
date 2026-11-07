# c-compiler-u3: free-model run

- Book: `books/cse/c-compiler/c-compiler-u3.html`
- Status: ok
- Model calls so far: 27 (104,050 tokens in, 245,864 out), 7.0 minutes

## Checker

```
c-compiler-u3.html: 6 chapters, 10863 words, 7 figures, 125 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3 (operator precedence): The chapter says that for E → E + T | T, T → T * F | F, F → id, "all three LEADING and TRAILING sets are {id}". That is false. Because E → E + T, the terminal + appears just after a nonterminal (E) at the start of a derived string, so + is in LEADING(E) as well. The same happens with * in T → T * F. A student who believes the sets are all {id} cannot build or read the matrix that follows, which correctly uses + ⋖ *, * ⋗ *, and so on.
- ch 1 [high] Quiz Q6: The answer gives 4 reductions for id * id. The parse is: shift id, reduce F→id, reduce T→F, shift *, shift id, reduce F→id, reduce T→T * F, reduce E→T, accept. That is 3 shifts but 5 reductions, so the stated number is wrong (the maximum stack depth of 4 is correct).
- ch 1 [high] Quiz Q5: The question text says "The table has +  +", but the question compares the stack-top + with the next input *. The entry + ⋗ + is irrelevant here and does not support the answer given. As written the question contradicts its own answer key and will confuse the student.
- ch 1 [low] Section 3 (relation definitions): Two problems in one paragraph. The symbol for the reduce relation is missing, so "a  b means reduce" appears as two words with a gap, and later "so +  +" has the same gap. Also the condition "B is left of b" is vague; it must mean B immediately precedes b in one production.
- ch 1 [low] Section 3 (definition of LEADING and TRAILING): "LEADING(A) is the set of terminals that can be first in a string derived from A" leaves out the case where a nonterminal comes before the terminal, as in E ⇒ E + T or T ⇒ T * F. Under the literal wording, + could never be in LEADING(E), which makes the matrix look wrong.
- ch 1 [low] Section 3 (relation =·): "a =· b means both are adjacent in one production" misses the common case where exactly one nonterminal sits between them, for example E → E + T gives + =· T, and T in turn gives the needs of the matrix.
- ch 1 [low] Section 3 (operator precedence grammar definition): The definition given omits one standard requirement: no two productions may have the same right-hand side. Without it the grammar can have reduce/reduce conflicts and is not an operator precedence grammar.
- ch 2 [high] Worked example 1, the [code] block, dry run and output: The worked example contains a Python snippet that only prints the constants 7, 6, 9, 1, 4, 0, 1 (the counts of states, shifts, reduces, accept, gotos and conflicts). It computes nothing about items, closure or goto, so a student sees an answer-shaped code listing that has no relation to LR(0) table construction; the 'dry run' table adds to the confusion by labelling the rows 'Printed'.
- ch 2 [low] Worked example 1, step 7 and answer: '6 shift' and '9 reduce' are counts of table entries, not of states, but they sit next to '7 states' with no label, so the numbers look like they are counted in different units.
- ch 3 [low] Quiz Q5 (answer explanation): The answer says "The reduce of S' → S is not allowed on + because FOLLOW(S') = {$}." This implies that a reduce by S' → S is placed on $, which contradicts the chapter's own rule (Section 2) and Exam trap 2: the completed augmented start item gives accept on $ and never a reduce action.
- ch 4 [low] Section 1, LR(1) item definition: The definition says the lookahead a is one terminal, but the chapter also uses $ as a lookahead, for example [S' → . S, $]. $ is the endmarker, not a grammar terminal, so the definition is slightly incomplete and may confuse students.
- ch 5 [high] Section 3, the state-count sentence and table: The state counts are off by one. Including the augmented start state I0, this grammar has 14 canonical LR(1) states and 13 LR(0)/SLR/LALR states. The chapter says 13 and 12. Those numbers correspond to omitting I0, which is nonstandard and not stated.
- ch 5 [low] Quiz Q7 and the sentence 'Canonical LR(1) is stronger but larger' in Section 3: The answer says LALR has fewer states than canonical LR(1). Canonical LR(1) can have the same number of states when no same-core states are split; it is never smaller. 'Fewer' is not universally true.
- ch 5 [low] Section 1 definition and first use in the worked example: The end marker $ is used in items but never defined. The definition also says the lookahead is one terminal, while $ is a special end-of-input marker.
- ch 6 [high] Worked example 1 (code block, dry run and output): The example shows a program with assignments and print calls (a = 2 + 3 * 4; b = (2 + 3) * 4; print(a); print(b)) and an output of 14/20. The calc.y given in Section 3 accepts none of this: there are no identifiers or '=' in the grammar, no print token, main only calls yyparse(), and yyerror is empty. Typing 'a = 2 + 3 * 4' would be a syntax error, and even '2+3*4' produces no output at all because the top-level $$ is never printed. So the shown output does not come from the program shown.
- ch 6 [low] Section 3 code, yyerror: Section 1 says 'yyerror reports errors', but the listing defines 'void yyerror(char *s) { }', which silently swallows every syntax error. A student copying it will see nothing on bad input and think the parser hangs or accepts it.
- ch 6 [low] Worked example 1, step 5: Step 5 answers a question that was not asked (the 5-2-1 subtraction case) and repeats Exam trap 3 word for word in substance, so the example ends on an unrelated hypothetical instead of the '*' conflict.
