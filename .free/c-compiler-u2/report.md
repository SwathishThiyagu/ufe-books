# c-compiler-u2: free-model run

- Book: `books/cse/c-compiler/c-compiler-u2.html`
- Status: ok
- Model calls so far: 29 (111,199 tokens in, 217,470 out), 7.5 minutes

## Checker

```
c-compiler-u2.html: 7 chapters, 12852 words, 8 figures, 144 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1 and figure: 'It also consults the symbol table for names, shown as a dashed lookup in the figure' presents symbol-table lookup as a routine parser activity. In the standard model the symbol table is filled and read mainly by semantic analysis; only some parsers consult it, for example to tell a type name from an identifier in C.
- ch 1 [low] Section 1 formula and Worked example 1: The grammar writes the terminals as '=' and ';', but the worked example calls the same token kinds 'assign' and 'semi'. A student may think these are two different token kinds.
- ch 1 [low] Section 2: 'A semantic error is a well-formed string with a wrong meaning' is vague: 'string' here means a token sequence, not a character string, and students may confuse it with a string literal.
- ch 1 [low] Quiz Q2 answer: The answer is conditional ('if expression covers a string token') and does not say clearly that the grammar itself must allow a string literal as an expression; the point of the question is lost.
- ch 2 [low] Section 1: The symbol T is overloaded: T is defined as the terminal alphabet in G = (V, T, P, S), and the nonterminal T appears in V = {E, T, F}. This can confuse students about which T is meant.
- ch 2 [low] Exam traps, last bullet: The bullet says changing the grammar changes operator precedence. The specific change E → E + T to E → T + E changes the associativity of +, not the precedence of * over +.
- ch 3 [low] Section 2, the left-recursion formula and its 'where' note: The formula shows only one left-recursive alternative A → Aα | β. A real rule usually has several, e.g. A → Aα₁ | Aα₂ | β, and the single-α form leaves a student unsure what to do with the second α. Every worked example in the chapter happens to have only one.
- ch 3 [low] Beyond: The sentence groups PEG parsers under 'algorithms that accept left recursion'. PEG parsers do not accept left recursion: a left-recursive PEG rule recurses forever. The usual PEG style is to replace the recursion with a repetition operator.
- ch 3 [low] Figure, 'Left recursion removal': The edges run orig → new → rep → eps as one chain, which reads like the derivation A → βA′ → αA′ → ε in sequence. In fact A′ → αA′ and A′ → ε are alternatives of the new nonterminal, not steps after one another.
- ch 3 [low] Section 3, FIRST definition: FIRST(α) is defined only as the terminals that can begin strings derived from α. The standard definition also puts ε in FIRST(α) when α can derive ε, which students will need in 2.5.
- ch 4 [high] Section 2, first paragraph: It says a backtracking recursive descent parser 'accepts any grammar'. That is false as written: a left-recursive grammar sends the parser into infinite recursion, and this same chapter says so in Section 3 and in the first exam trap. A student will trust the stronger sentence and skip removing left recursion.
- ch 4 [low] Section 2, formula box: The condition 'A → α | β is predictive when FIRST(α) ∩ FIRST(β) = ∅' is stated without qualification. It is only sufficient when neither α nor β can derive ε; if one is nullable, the choice of that alternative must also be checked against FOLLOW(A).
- ch 5 [low] lead, first sentence of the chapter: The lead defines FIRST(α) as only the terminals that can begin a derived string. That leaves out the ε case, so a student who reads only the lead gets an incomplete definition that contradicts the rules in Section 1 (for example FIRST(E′) = {+, ε}).
- ch 5 [low] figure (FIRST and FOLLOW for the expression grammar): The caption says the marked cells are ε in FIRST(E′) and $ in FOLLOW(E), but the table also marks cell 0 of FIRST(E) (the '(' cell) with the 'accent' style, which the text never explains. A reader may wonder whether that cell means something special.
- ch 5 [low] Beyond paragraph: Saying yacc computes FIRST and FOLLOW internally is imprecise. yacc builds LALR(1) tables; it computes nullable and FIRST sets while closing items, but it does not compute LL-style FOLLOW sets. Only ANTLR-style LL generators compute FIRST and FOLLOW in the sense of this chapter.
- ch 5 [low] lead, last sentence of the first paragraph: The phrase 'most fold it into LL(1) table construction' is a claim about how many syllabi treat the topic. The book avoids such counting statements.
- ch 6 [high] Section 3, error messages from an empty cell: The claim 'An empty M[X,a] also gives a precise error message: the parser expected something that can follow X, but saw a' is wrong. When M[X,a] is empty, X is a nonterminal and the lookahead cannot start any production of X; the expected tokens are FIRST(X), plus FOLLOW(X) only when X is nullable. For example, M[E,+] is empty because the parser expects id or '(' to begin an E, not because it expects what may follow E. A student who repeats this sentence in an exam loses marks.
- ch 6 [low] Section 1, parser loop (prose and bullet list): The rule says 'read M[X,a] = A → α, pop X, and push α reversed'; the left side of the entry is X, not A, so the symbol names clash with the earlier 'M[A,a] = A → α' notation. The loop also has no rule for X being a terminal with X ≠ a (for example X = $ and a = id), which falls through every bullet.
- ch 6 [low] Figure: LL(1) parser loop: The 'Match terminal' and 'Accept' branches are drawn out of the M[X,a] box, but matching and accepting depend on comparing the stack top X with the lookahead a, not on a table entry. As drawn, a student may think every move starts with a table lookup.
- ch 6 [low] Worked example 1, trace (steps 4–10): The trace does not say whether each listed stack is the state before or after the action in that row. Row 2's stack $E′T is in fact the result of row 1's expansion, so the stacks are shown before the action of their own row; without this note the rows look inconsistent.
- ch 7 [high] Section 4, paragraph on progress ("Every step must change the stack or the input"): It says inserting a token "pushes the right side of a production, which changes the stack". That is the mechanism of an error production (A → error α pushes α). Phrase-level insertion pushes nothing: the parser simply matches the terminal it expected against a token that is not in the input, so that terminal leaves the stack and the input is untouched. The two repairs are mixed up and a student will copy the wrong mechanism onto the stack.
- ch 7 [low] Section 1 ("A wrong token is caught exactly where it sits") and Quiz Q3 answer ("the fault is exactly at a"): The chapter's own recovery example (Q5, missing semicolon) shows an honest token, the id starting y, being reported as the error, so "the fault is exactly at a" contradicts Section 3. LL(1) detects the error at the first token for which no table entry exists; the mistake itself may be an earlier missing token.
- ch 7 [low] Section 2, panic-mode bullets: The rule is stated only for a nonterminal X on top of the stack. When the top of the stack is a terminal b with b ≠ a, FOLLOW(b) is undefined and the student has no rule to apply, even though this is the other error case listed in Section 1.
- ch 7 [low] Section 2, last bullet ("stop skipping when a is in FIRST(Y) for a nonterminal Y still on the stack"): "Y still on the stack" is vague; several nonterminals are on the stack. The check is meaningful only for the topmost nonterminal that can actually start with a, that is, the symbol the parser will reach after popping the ones above it.
- ch 7 [low] Section 3, error productions: "When M[A, a] would be empty, the parser takes this production" is too broad. The error production is entered only for lookaheads that can begin α (or that lie in FOLLOW(A)); for any other lookahead the parser pushes α, finds that α cannot start with a, and reports a second error at the same token.
- ch 7 [low] Worked example 1, answer line: "then parses the remaining id + id and accepts" is misleading: after the stray * is discarded only id $ is left to read. id + id is the repaired sentence, not the remaining input.
- ch 7 [low] Quiz Q6 answer: It offers rule two (never skip a token in FIRST(Y)) as one of the rules that prevents the endless loop. Rule two protects good input from being thrown away; it does nothing about a step that changes neither stack nor input. Only rule one prevents the loop.
- ch 7 [low] Beyond box: "the Rust compiler and the TypeScript parser keep a syntax tree with error nodes and suggest a fix" is loose. Keeping explicit error nodes and suggesting fixes are two separate behaviours and are not uniform across those two front ends.
