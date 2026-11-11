# c-toc-u3: free-model run

- Book: `work/claude_figs/c-toc-u3/tree/books/cse/c-toc/c-toc-u3.html`
- Status: ok
- Model calls so far: 33 (124,619 tokens in, 316,705 out), 8.6 minutes

## Checker

```
c-toc-u3.html: 9 chapters, 16221 words, 10 figures, 180 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Exam traps, first bullet: The trap says {aⁿbⁿ} is generated both by S → aSb | ε and by S → ab | aSb. The second grammar can never produce ε, so it generates only {aⁿbⁿ : n ≥ 1}. This directly contradicts the answer to Q5, which correctly says G2 gives n ≥ 1 and cannot produce ε. A student revising from the trap will write the wrong language in the exam.
- ch 1 [low] Section 1, why the model exists: It says the single rule S → aSb keeps the two counts equal. That rule alone never produces a terminal string; the base case S → ε is what ends the derivation.
- ch 1 [low] Section 2, balanced round brackets bullet: Section 2 has just defined round brackets as a grouping shorthand on right sides. The very next bullet uses ( and ) as terminals in S → (S)S | ε, so a reader can mistake them for the grouping shorthand.
- ch 1 [low] Worked example 1, output block: The first output line is the repr of the empty string, printed as '' on the same line as the label, so it reads as 'output: empty'. On a phone the four printed lines also lose their indentation.
- ch 1 [low] Quiz Q5 answer: 'They differ by ε only, so they are different grammars' draws the wrong conclusion. Two grammars with different rule lists can generate the same language; what matters is that the two languages differ.
- ch 1 [low] Lead and Beyond: 'the same 4-tuple is what yacc, bison and ANTLR read as input' is loose. These tools read a grammar specification file (BNF or EBNF plus declarations and actions), not the 4-tuple itself.
- ch 1 [low] Exam traps, third bullet: 'marks leak away quietly there' is unclear for a reader with English as a second language.
- ch 1 [low] Section 1, definition: The definition does not say that V and T are nonempty, which standard textbooks require together with finiteness and disjointness.
- ch 2 [low] Worked example 1, step 5: It says the tree is 'shown in the figure after Section 1', but the figure actually sits after Section 3, between the exam traps and the worked example. A student turning pages to find it will be confused.
- ch 2 [low] Figure spec (tree labels): Edge labels are attached to the child to name the production used at the parent: the depth-1 E carries 'E → E + T', which is the root's production. But the depth-1 T (also a child of the root) carries 'T → T × F', which is not the root's production; the root's production is E → E + T. The labeling convention is inconsistent within one figure.
- ch 2 [low] Section 3, first paragraph: 'The number of derivations of a string grows with the number of variables' is vague: it is the number of variables still present in the sentential form at a given step (i.e. how many independent expansions are pending) that multiplies the orders, not the number of variables in the grammar.
- ch 2 [low] Beyond: 'leftmost derivation parser' is not a standard name; a reader who searches for it will find nothing useful.
- ch 3 [low] Section 2, bullet list: The bullet 'If one rule is needed in two places, add a new start symbol and keep the old variable for the inner use' does not belong to this conversion and can mislead. In the layered grammar the variable E is used in two places (as the start symbol and inside F → ( E )) and no new start symbol is added. A student may think the grammar shown is incomplete.
- ch 3 [low] Section 2, after the layered grammar: The line 'Some syllabi call this conversion ambiguous CFG to unambiguous CFG' can be read as a general method. In general no method exists that turns an arbitrary ambiguous CFG into an unambiguous one; the layering only works because of operator precedence in expression grammars.
- ch 3 [low] Figure caption and figure: The caption says the two groupings give 7 and 9, but neither the caption nor the figure states the id values, so a reader has no way to check these numbers from the figure alone.
- ch 3 [low] Section 3, second formula: The clause after the second language is tagged 'where:' but it explains instead of defining symbols, and it writes 'when n = m' while n and m already have fixed roles in the two parts. The reader must work out which n and m are being compared.
- ch 3 [low] Quiz Q5 answer: 'Fix the given grammar and test again' suggests that testing a grammar for ambiguity is always possible, which contradicts Q7 and Section 3 (it is undecidable).
- ch 3 [low] Beyond paragraph: Shift/reduce and reduce/reduce conflicts are LR-parser (yacc/bison) terms. ANTLR is not an LR parser and reports ambiguity or alternative-matching warnings, not shift/reduce conflicts.
- ch 3 [low] Section 3, cross-references: '(see 3.6)' and 'Unit 6 covers that result' are plain text, so on a phone the student cannot jump to those units.
- ch 4 [high] Section 1, epsilon-rule removal bullet: The instruction is contradictory when S appears on a right side: it says keep S → ε and also add S₀ → S and S₀ → ε. That leaves two ε-rules, and S is no longer the start but still nullable, so the grammar does not meet the stated normal form.
- ch 4 [high] Worked example 1, final answer/output: The final grammar S → AB | a | bB | b; A → aA | a; B → bB | b has no ε-rule and no unit rule, so it has 0 nullable variables and 0 non-reflexive unit pairs, not 1 and 1. The values 1 and 1 belong to the original grammar: A was nullable and S → B was a unit rule.
- ch 4 [low] Section 3, theorem: The theorem as stated fails when L(G) is empty: then the start symbol cannot be generating, so no equivalent grammar can have no useless symbols.
- ch 4 [low] Quiz Q3: The answer suggests a fresh start alone fixes S appearing on the right side, but it does not say to remove the old S → ε. Keeping both S₀ → ε and S → ε leaves an ε-rule for the non-start variable S.
- ch 5 [high] Section 1 (third conversion step) and Exam traps, 5th bullet: The chapter says splitting can create a unit rule ('Third remove any unit rules the splitting created', 'Splitting can create a unit rule such as A → X'). Splitting a right side of length 3 or more always produces binary rules such as A → X₁Z₁; it never produces a one-variable rule. Unit rules come from the original grammar or from ε-elimination, not from splitting, so the reason given is wrong and a student will hunt for unit rules that cannot appear.
- ch 5 [low] Lead paragraph: 'Both forms describe the same context-free languages' is not exact. GNF covers every context-free language that does not contain ε; CNF covers all of them because of the S → ε exception. The lead contradicts the caveat given later in Section 3.
- ch 5 [low] Section 1, first conversion step: 'Replace each terminal that sits beside a variable' is narrower than the actual rule and clashes with the wording in Section 2. A right side such as A → ab has no terminal beside a variable, yet both terminals must still be replaced, and the next sentence has to patch this.
- ch 6 [high] Quiz Q7: The answer says the context-free lemma is weaker partly because it 'cannot prove that a language is context-free; it is only a necessary condition'. The regular-language pumping lemma is also one-way and also cannot prove regularity, so this does not distinguish the two. A student will walk away thinking a language that passes the regular lemma is regular.
- ch 6 [low] Worked example 1, steps 5-7: Step 4 concludes only that vwx misses at least one letter block, but steps 5-7 then say 'Suppose the untouched block is c' and finish the proof. The cases where a or b is the untouched block are never mentioned, so the proof looks incomplete.
- ch 6 [low] Section 2, first paragraph: The proof takes a Chomsky normal form grammar for L, but CNF rules A → BC and A → a cannot derive the empty string, so a CFL containing ε has no CNF grammar as written. A careful student will notice the proof does not cover that case.
- ch 6 [low] Section 1, formula line: The formula line lists four items (the split s = uvwxy plus three conditions), but the next paragraph calls the conditions (1), (2) and (3). A student can number the split as condition (1) and shift every reference.
- ch 7 [low] Section 2, grammar version of the intersection-with-regular construction: The construction lists only the terminal rule A → a and the binary rule A → BC. It never gives the case of an ε-rule A → ε, and it never says which triple is the start variable. A student who applies it to the chapter's own grammars (G1 has A → ε and C → ε) gets a grammar that misses strings of L ∩ R.
- ch 7 [low] Section 4, decision table, row 'Is w in L(G)?': CYK runs in about n³ steps only after the grammar is in Chomsky normal form; the row does not say this, so a student may feed a general CFG straight into CYK.
- ch 8 [high] Quiz Q5: 640 is not the number of worst-case rule checks. For n = 4 and |P| = 10 the number of (split, rule) checks is |P| × Σ over ℓ=2..n of (n−ℓ+1)(ℓ−1) = 10 × (3·1 + 2·2 + 1·3) = 10 × 10 = 100. The value 640 is just n³·|P| = 64 × 10, a loose upper bound, and writing 'O(n³|P|) = 640' misuses O as an equality. A student copying this answer gives a wrong count.
- ch 8 [low] Lead / Section 1 (CNF definition): The definition 'every rule is A → BC or A → a' leaves out the standard exception S → ε (the start variable may derive the empty string). Because of this, the chapter never says what CYK does with w = ε, yet it claims CYK answers whether any string w is in L(G). As written, CYK would reject ε even when ε ∈ L(G).
- ch 8 [low] Lead (cost sentence): The lead says membership costs 'about n³ rule checks', but Section 2 correctly gives O(n³·|P|) with |P| the number of rules. The two statements disagree, and the lead's version is only right for a fixed grammar.
- ch 8 [low] Beyond paragraph: Earley and GLR are not asymptotically faster than CYK: both also run in O(n³) time in the worst case (O(n²) or O(n) for restricted/unambiguous grammars). Calling them simply 'faster' can mislead a student into thinking CYK is outclassed in the worst case.
- ch 8 [low] Figure: The cell V[1,1] (row 'len 1', cell 0, holding A) is marked 'live', but nothing in the text explains what 'live' means. A reader cannot tell whether it signals the base case or a rule being used.
- ch 9 [low] Worked example 1 step 1 and quiz Q3: The grammar S → aS | B, B → bB | ε is called right-linear, but under the type 3 shape given in Section 1 (A → aB or A → a, and A → Ba or A → a) it contains two rules that do not fit: the unit rule S → B (left side one variable, right side a bare variable, no terminal) and B → ε, an ε-rule on a non-start variable, which the chapter's definition never allows. The language a*b* is indeed regular, so the classification is right, but the grammar as written is not of the stated shape and the quiz answer's reason 'B → ε ends the string' is not in the definition.
- ch 9 [low] Quiz Q2: The answer says 'The only ε rule needed is S → ε, and type 1 allows it when S is not on a right side.' That condition can fail: in S → aSb | ε the start symbol S does appear on a right side, so the reason given does not cover every type 2 grammar with ε in its language.
- ch 9 [low] Figure: The aria text says each ring holds a witness 'that belongs to it and not to the class inside it', but the innermost ring (type 3) has no class inside it, so the description does not fit its witness a* b*.
