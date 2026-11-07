# c-nlp-u3: free-model run

- Book: `books/cse/c-nlp/c-nlp-u3.html`
- Status: ok
- Model calls so far: 40 (165,567 tokens in, 318,085 out), 8.4 minutes

## Checker

```
c-nlp-u3.html: 8 chapters, 16457 words, 9 figures, 178 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Lead: The lead calls the four components “four sets” and lists the start symbol among them; a CFG has three sets N, Σ, R and one start symbol S, which is not a set.
- ch 1 [high] Section 1, recognition: Recognition is defined as deciding membership “and return the trees”, but the next sentence correctly says a recogniser answers yes/no and a parser returns trees. This is contradictory.
- ch 1 [high] Section 2, recursion examples: The example strings use car, dog, spoon and kitchen as nouns, but the listed N lexicon is only boy | cake | girl, so the grammar as written cannot derive those strings.
- ch 1 [low] Section 3, feature agreement: “State agreement by requiring” is a typo/unclear; the intended instruction is to enforce agreement.
- ch 1 [high] Worked example 1, step 9: To get “the boy ate a cake” from the figure “the boy ate the cake”, you replace the second determiner “the” with “a”, not with “cake”. The instruction as written would give “the boy ate cake cake”.
- ch 1 [low] Quiz Q2: The answer says PP → P NP takes an NP and returns an NP; it returns a PP. The pair of rules expands an NP, but only the NP → NP PP rule returns an NP.
- ch 1 [high] Quiz Q5: The answer says to add PP → P NP, NP → NP PP and P → in and then claims the PP can attach to the VP, but without VP → VP PP only NP attachment is possible. It also omits N → garden, so “garden” cannot be derived.
- ch 2 [high] Section 3, order of the four conversion steps: Removing unit rules before ε rules is the wrong order. Dropping a nullable symbol from a rule leaves a shorter rule, and if that shorter rule has one symbol it is a new unit rule — for example A → B C with C nullable gives A → B. Unit removal has already been done, so this new unit rule survives and the 'CNF' grammar the recipe produces is not in CNF. The same thing happens to the helper nonterminals created by binarising: a nullable X1 leaves a rule such as S → NP behind.
- ch 2 [high] Section 3, last paragraph ('Size grows linearly ... never exponential'): The linear claim is false for the whole conversion. Binarising and terminal isolation are linear, but unit-rule removal copies all of B's rules under every A with A ⇒* B, so the rule count can grow to O(|G|²): a chain of n/2 nonterminals each holding n/2 rules gives about n²/4 rules out of about n rules. Saying 'a grammar of |G| rules becomes O(|G|) rules' is a wrong figure a student will repeat in the exam.
- ch 2 [low] Worked example 1, step 5: 'The four helper nodes of the split' is wrong and confusing. Splitting S → NP VP PP adds exactly one helper nonterminal, X1; there are no four nodes anywhere in the step.
- ch 2 [low] Section 2, table row 'A → Bc | no, isolate c': The example given for the two-symbol shape A → Bc is S → NP VP ., which has three symbols, so it does not illustrate the row it sits in.
- ch 2 [low] Section 2, last sentence: 'Some syllabi call this CNF or Chomsky Normal Form' adds nothing, since the paragraph has just defined CNF as Chomsky normal form; a student may think a second, different form is being named.
- ch 3 [high] Worked example 1, step 4: Wrong split index. The cell (3,5) is built from V in (3,3) and NP in (4,5), which is split k = 3, not k = 4. Split k = 4 would pair (3,4) with (5,5), and (3,4) is empty.
- ch 3 [high] Section 4, comparison table, row 'Left recursion': The entry 'not possible in CNF' is false. A rule A → A B is a two-nonterminal rule and is allowed in CNF, so a CNF grammar can be left recursive. CYK copes because it works bottom-up over spans, not because CNF removes left recursion.
- ch 3 [low] Section 1, top-down parsing paragraph: 'moving the input pointer before the recursive call' is not a general fix for left recursion. Advancing the pointer before recursing can stop the loop but gives wrong parses, so a student may trust a method that does not work.
- ch 3 [low] Section 3, complexity formula, definition of bounded-state grammar: The gloss 'limits how many symbols of a rule can still be unmatched' is not the standard meaning. A bounded-state grammar is one where the number of states in any chart set stays below a fixed constant, independent of sentence length.
- ch 3 [low] Quiz Q1, answer: The answer rules out every form except A → B C and A → a. Standard CNF also permits the special rule S → ε when the empty string is in the language.
- ch 3 [low] Worked example 1, output line: A stray '1' appears on its own line after 'output: 20'. A reader cannot tell what it belongs to.
- ch 4 [low] Section 1, the Catalan count: The list is written without its starting index, so a student can map it wrongly: 1, 1, 2, 5, 14, 42 is the sequence for n = 0, 1, 2, 3, 4, 5 PPs. Read as n = 1, 2, 3, 4, 5 it gives 14 for five phrases, which contradicts the 42 stated in the same sentence and in Quiz Q5.
- ch 4 [low] Exam traps, first trap: 'A word like bank gives lexical ambiguity; the tree changes only after a sense is chosen' is inaccurate. Both senses of 'bank' are nouns, so choosing a sense leaves the parse tree unchanged. A tree can differ only when the category differs, as with 'book' (noun vs verb).
- ch 4 [low] Beyond: 'Attachment accuracy is measured by labelled attachment scores' is loose. Labelled attachment score (LAS) is the share of words whose head and dependency label are both correct; it is not a PP-attachment measure specifically.
- ch 5 [high] Section 2, inside-probability formula: The recursion for β(i, j, A) omits the probability of the rule A → B C. As written it multiplies only the children's inside probabilities, so β(1, n, S) would not equal the sentence probability defined two lines earlier, and the stated relation between the sum (β) and the max (δ) recurrences breaks down: δ includes × P(A → B C) but β does not.
- ch 6 [high] Quiz Q7: The scoring explanation contradicts the definition used in Worked example 1. UAS and LAS divide correct arcs by the number of arcs in the gold tree, so a spurious extra arc in the system output does not enlarge the denominator. With the gold arc ate → quickly still present, UAS stays 5/6 = 0.8333, not lower.
- ch 6 [low] Section 3, definitions of stack: 'Words seen but not yet attached to a head' is inaccurate. After RIGHT-ARC or after being shifted and given a head, a word stays on the stack to collect its own dependents, so stack items can already have a head. This also conflicts with the LEFT-ARC condition that the top of stack has no head yet.
- ch 6 [low] Section 3, arc-standard actions: The legality condition of LEFT-ARC is incomplete. As written, LEFT-ARC may be applied when i is ROOT (ROOT has no head), which would pop ROOT and destroy the tree.
- ch 6 [low] Beyond: The note says Universal Dependencies standardised 'the labels used here', but dobj and prep are Stanford dependency labels. In Universal Dependencies the direct object label is obj, and prepositions are handled with case and obl.
- ch 7 [high] Figure ('Chunks as IOB tags') and Section 1: The IOB row tags 'in the park' as B-PP, B-NP, I-NP. That puts an NP chunk inside a PP chunk, which contradicts the chapter's own rule that chunks are flat and never nest. If 'in the park' is one PP chunk, all three words belong to that PP.
- ch 7 [low] Section 2, numbered steps: The step 'Mark the first word of each chunk B-' omits the type letter, which is the whole point of B-X in IOB2; a student may write a bare 'B'.
- ch 8 [high] Lead, Section 1, Quiz Q2: The chapter says lexicalization lets the grammar use 'telescope' and 'fork' to choose the attachment, but its own head rules make the preposition the head of the PP ('PP takes the preposition'). Under those rules the PP 'with the telescope' is headed by 'with', so 'telescope' and 'fork' are never heads of a child of the deciding rule and never enter P(A → B C | a, b, c). Part (b) of the worked example correctly uses 'saw' and 'man', so the lead and Q2 contradict the rest of the chapter.
- ch 8 [low] Worked example 1, step 4: The reduce is written 'REDUCE-BINARY-RIGHT as NP → [NP(boy)]', with the rule left unfinished; a student cannot see which rule fired.
- ch 8 [low] Worked example 1, step 9: 'REDUCE-BINARY-LEFT as VP → [NP(boy), VP(ate)]' mixes the rule with the stack after the move. Read literally it shows the rule VP → NP VP, which is not in the grammar given.
- ch 8 [low] Figure and worked example dry run: The prose says a shifted word becomes a tagged preterminal (Det(the), V(ate), N(cake)), but the figure and the dry-run table show bare words ('ate', 'the', 'cake'). The trace is also labelled REDUCE-R in the table and REDUCE-BINARY-RIGHT in the prose.
- ch 8 [low] Figure: The caption says the marked cell is the most recent item (the top of the stack), but row 3 ('REDUCE-R NP') carries an unexplained 'accent' mark that is not the top of the stack.
- ch 8 [low] Section 1, head percolation rules: 'Det takes the determiner' presents Det as a phrase that percolates a head from a child. Det is a preterminal, so it has no head child; its head word is the word itself.
- ch 8 [low] Exam traps, trap 4: 'Reading REDUCE-BINARY-LEFT/RIGHT as the side of the stack' is unclear; students may read 'side' as the left or right edge of the stack rather than as which of the two popped subtrees supplies the head.
