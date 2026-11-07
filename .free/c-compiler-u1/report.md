# c-compiler-u1: free-model run

- Book: `books/cse/c-compiler/c-compiler-u1.html`
- Status: ok
- Model calls so far: 35 (131,339 tokens in, 241,889 out), 6.1 minutes

## Checker

```
c-compiler-u1.html: 9 chapters, 15865 words, 10 figures, 174 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1: Grammar slip: "A assembler is also a translator" — wrong article before a vowel sound; small but it is the kind of error a student copies into an answer sheet.
- ch 1 [low] Quiz Q3 answer: The inequality chain is broken: "Solve 3 + 0.20r  1.667" is missing the comparison with 2r and the direction of r, so the student cannot see how 1.667 was obtained even though the final numbers are right.
- ch 2 [low] Section 3 and the front end/back end table: The text says the back end 'depends on the target machine and not on the source language' but puts ordinary (machine-independent) optimization in the back end. Optimization on three-address code is the phase that does not depend on the target machine, so the table contradicts its own definition. Some syllabi put machine-independent optimization with the front end or in a middle layer.
- ch 2 [low] Figure note: The sentence 'A correct compiler may skip only the optimizer' is too strong. A compiler can also skip intermediate code generation and emit target code directly from the parse tree, so intermediate code is not compulsory for correctness, only the optimizer is optional in the sense of leaving the output slower.
- ch 2 [low] Figure: The pipeline diagram stops at the optimizer and code generator, so the machine-dependent optimization stage listed in Section 1 and in Quiz Q1 has no place in the figure. A student copying the diagram will lose a phase the exam asks for.
- ch 3 [low] worked example 1, step 3: The wording "the scanner returns one token code at a time for the 16 patterns and 42 keywords" suggests a token code is produced per pattern. A scanner returns one token each time it is called, for the lexeme it has just matched; the 16 rules and 42 keywords are alternatives inside the specification, not things that each produce a token per call.
- ch 3 [low] quiz Q2, answer: "which only a context-free grammar describes" is too absolute. Regular expressions cannot describe nesting, but other formalisms can; the point being made is about regular expressions versus context-free grammars.
- ch 4 [low] Worked example 1 (steps 1–14 vs dry-run table rows 1–12): The text numbers 14 steps but the table numbers 12 rows. Text step 1 is a preamble (skip spaces) and steps 2–13 are the twelve tokens, while table row 1 is the token if. A student matching text step 4 (count → ID) against table row 4 (<= → LE) gets the wrong row.
- ch 4 [low] Section 1 and Quiz Q2 ('lets one lexer serve a parser generator'): The phrase is unclear and slightly off: a parser generator produces a parser; it does not consume a lexer. The intended point is that lexing can be generated separately and reused, and that hand-written lexers can be swapped between tools.
- ch 4 [low] Section 3, Figure, token-stream note: The note reads 'IF ID LE NUM', which drops LPAREN and RPAREN. Parentheses are ordinary tokens, and Section 3's own token list includes them, so the figure contradicts the text and may make students think brackets are skipped like whitespace.
- ch 4 [low] Exam traps, fourth bullet: 'Apply the longest-match rule before rule order in hand-written lexers' assumes the reader knows what rule order means; in a hand-written lexer there are no ordered rules to speak of, only the scan loop.
- ch 5 [high] Section 3, the five-step scanning loop, step 3: Step 3 ends with 'Otherwise go to step 2'. Taken literally, a character that is not a sentinel sends the scanner back to step 2, which re-reads the same character at forward forever. The loop never reaches step 4, so no lexeme is ever built. It also never tells the reader where to go after a switch/refill.
- ch 5 [high] Section 2, third paragraph, and worked example step 8: The rule says 'If that half is already full, the scanner refills it with the next block', but the worked example says the opposite: step 8 states 'No refill is needed because Buffer B already holds the next input'. In the standard scheme the other half is normally full of characters that have already been scanned, and that is exactly when it must be refilled; a half that already holds the new block (the initial fill case) is not refilled. As written, the rule and the example contradict each other.
- ch 5 [high] Section 2, second paragraph: 'Both are indices into the current half-buffer' is wrong and contradicts the rest of the chapter. lexemeBegin often points into the other half-buffer, which is precisely what lets a lexeme cross a boundary; only forward is always inside the half-buffer being scanned.
- ch 5 [low] Worked example 1, dry run table: The dry-run Step column runs 1 to 9, but the numbered steps run 1 to 10, because the buffer-layout step 1 is left out of the table. A student cross-checking 'step 6' against the dry run will land on the wrong row.
- ch 6 [low] Section 1, first paragraph: Regular expressions are introduced only through the three operations (union, concatenation, closure). The base cases are never stated, so the definition is formally incomplete: students cannot tell what the smallest regular expressions are, and the empty language is never mentioned at all.
- ch 6 [low] Section 2, paragraph on keywords: The sentence 'Longest match first, then rule order, prefers the keyword if over the identifier if' can be read as saying longest match decides between the keyword and the identifier. For the lexeme if both rules match exactly two characters, so longest match has nothing to choose; only rule order decides.
- ch 6 [low] Section 2, floating-point paragraph: exp is described only in running prose ('E or e, an optional sign, then digits'). Every other part of the pattern is given as a named definition, so students cannot see exp as one piece of the specification.
- ch 7 [high] Section 2, relational operators: The text of the operator diagram is broken: characters and diagram states are missing, so the sentence reads "For : q0 on  goes to an accepting state for NE; any other character leaves q1 as an accepting state for LT." A student cannot tell what the start state, the q1 branches, or the LE/NE/LT states are.
- ch 7 [high] Quiz Q7: The question asks for two traces but the answer is garbled ("For , so back up to q1 and accept LT"). The <= trace is missing entirely, and the diagram it refers to is not given correctly in the text, so the answer is unusable.
- ch 7 [high] Quiz Q8: The question is truncated: "A diagram for . What goes wrong without backup?" The operator set the diagram handles is missing, so the question cannot be answered as written.
- ch 7 [low] Section 1: "A diagram recognises one token class only" contradicts Section 2 and the figure, where one diagram recognises both identifiers and unsigned integers from a single start state.
- ch 7 [low] Figure (aria text): The accessible description says q0 branches "on a letter", but the edge label is L,_ so underscore is also allowed.
- ch 8 [high] Section 1, Section 2, Exam traps, Quiz Q6: The powerset is written as 2Q and the bound as 2n. Read literally, 2Q is a set name and 2n means 2 times n, which is false for n ≥ 3 (an NFA with 5 states can give 32 DFA states, not 10). A student will copy the wrong bound.
- ch 8 [high] Worked example 1, step 7: Step 7 separates A from B and E from B, but never separates A from E. In the first round A and E look identical: on a, b, c both go to non-final states. So the jump to the groups {A}, {B}, {C,D}, {E} does not follow from what is shown, and a student may conclude A and E are equivalent and merge them, giving a wrong minimal DFA.
- ch 8 [low] Worked example 1, answer line: "The DFA before minimisation has 4 states A, B, C, D" contradicts step 6, where the dead state E was added to make the DFA complete before minimising; the automaton that was actually minimised has 5 states.
- ch 8 [low] Section 3, partition refinement bullet 3: "If for some symbol a their transitions land in different groups, split them into separate groups" suggests splitting every differing pair apart. Two states with identical behaviour can then be pushed into separate groups, and refinement never re-merges them, so the result would not be minimal.
- ch 9 [low] Section 2 first paragraph (and Q2 answer): It says that with rules 'if' and [a-z]+, if the input starts with 'if', both match length 2. That is only true when the keyword ends at a non-letter or at end of input. On input like 'ifx', [a-z]+ matches 3 characters and wins regardless of rule order, so a student may believe [a-z]+ can never beat the keyword by length.
- ch 9 [low] Section 1, rules section description: 'Each action is C code inside braces' contradicts the chapter's own whitespace rule [ \t\n]+ ;, where the action is a bare semicolon, not a braced block. A student may think the bare ';' form is invalid.
- ch 9 [low] Section 1, empty action sentence: 'Skips the match because the action does nothing' can be read as if the matched characters are not consumed. The characters are consumed; only no token is returned.
