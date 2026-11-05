# c-compiler-u4: free-model run

- Book: `books/cse/c-compiler/c-compiler-u4.html`
- Status: ok
- Model calls so far: 21 (72,618 tokens in, 204,658 out), 5.4 minutes

## Checker

```
c-compiler-u4.html: 7 chapters, 13325 words, 8 figures, 138 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, the number grammar and the walk-through of 3 4 5: The rules give the leftmost digit weight 10⁰ and the rightmost digit weight 10², so the string 3 4 5 is computed as 3×10⁰ + 4×10¹ + 5×10² = 543. A reader takes '3 4 5' to be the number 345; the SDD as printed computes its digit reversal, and the text then presents 543 as the answer without noticing.
- ch 1 [high] Quiz Q5: The arithmetic follows the reversed place values of Section 2, so the digit string 4 0 7 is answered as 704 (4×10⁰ + 0×10¹ + 7×10²). The correct value of the number 4 0 7 is 407; a student copying this answer writes the digits backwards in the exam.
- ch 1 [low] Section 2, dependency graph paragraph: 'one node per attribute instance at one tree node' suggests the graph lives inside a single tree node, but the graph covers every attribute instance in the whole parse tree, with edges crossing between tree nodes.
- ch 1 [low] Section 2, second bullet of the number grammar: The formula is printed as 'digit.lexval × 10D.pos + D1.val'. Without the exponent mark 10D.pos reads as 10 times D.pos.
- ch 1 [low] Exam traps, first trap: 'A rule that gives an inherited attribute of a node a value taken from that node's own child' is muddled: an attribute computed from the node's own children is a synthesized attribute by definition, so the sentence never says clearly which mistake it is warning against.
- ch 2 [high] Section 3, third paragraph: The sentence 'Every DAG can be expanded into a syntax tree by copying a shared node once for each parent. The reverse is not always possible.' is false in the second half. Folding a syntax tree into a DAG is always possible: walk the tree bottom-up and merge any node whose operator and children are identical to an existing one (hash-consing). The fold may not shrink the graph if no subtree repeats, but it can always be done.
- ch 2 [high] Exam trap 2, with Section 2 ('The plus node is shared and has two parents'), the figure and worked example 1 step 6: The chapter confuses 'number of parents' with 'number of uses'. In the chapter's own example, (a + b) * (a + b) - c, the shared + node has only one parent (the * node), which uses it twice; the figure draws two edges P→S from a single parent. So the trap's test 'if your drawing has no node with two parents, you drew a syntax tree' fails on the chapter's own figure, and the statements that the plus node 'has two parents' are wrong in graph terms. Sharing means indegree ≥ 2 (two uses), not two distinct parents.
- ch 2 [low] Quiz Q4: The answer says 'The same subexpression is used by three parents'. Indegree counts edges (uses), not distinct parents; one parent can produce three edges, as the chapter's own figure shows (one parent, two edges). The evaluation advice is right, but the wording contradicts the figure.
- ch 2 [low] Section 3, last paragraph: 'You can list its nodes in postfix order, then emit three-address code or postfix' is circular: the output is described as postfix after already listing in postfix order.
- ch 3 [low] Section 1, type expression formula: The same arrow symbol → is used twice with different meanings in one line: first as the metalinguistic 'is defined as' in τ → int | real | ..., and then as the function-type constructor in τ₁ → τ₂. A student can read the whole line as function types.
- ch 3 [low] Section 1 and Worked example, step 1: Calling n the 'bound' invites confusion with the upper index n−1; in int a[10] the bound students see in code is 9, but n is 10.
- ch 3 [low] Section 2, addition formula: The text says the result of E1 + E2 has 'the common numeric type', but the formula only gives the int case, so real + real and int + real have no rule.
- ch 3 [low] Section 2, expression checking rule: The rule 'for E1 + E2, both operands need numeric type' is contradicted by C, which the lead names: p + 1 with p a pointer is legal and means address arithmetic.
- ch 3 [low] Section 4, last sentence: The pointer to 'runtime environments in Unit 5' is a bare cross-reference to another unit; readers on a phone cannot follow it and it is not linked like other chapter references.
- ch 4 [high] Section 3, the counting check sentence: The rule is stated wrongly: "in every prefix read so far the operands outnumber the operators by one". For 3 4 2 * + the prefix "3 4" has 2 operands and 0 operators, a difference of 2, not 1, so a correct string would look invalid under this test.
- ch 5 [high] Lead: The lead says the three tables differ in how the result is written down, and lists for indirect triples 'a row number reached through a pointer list'. That is not how indirect triples work. The triple table is unchanged: inside a triple the result is still the triple number, e.g. (0). Only the execution order goes through the separate pointer list. As written the sentence contradicts Section 3 ('Indirect triples keep the triple table unchanged') and can make a student think a result is stored as a pointer entry.
- ch 5 [low] Section 2, paragraph on rearranging quadruples: The illustration is a reordering that is not legal: row 1 (+, a, t1, t2) uses t1, which row 0 defines, so no optimizer may move row 1 above row 0. A student may take this as an allowed transformation.
- ch 5 [low] Section 3 and worked example, step 7: The operand order of an assignment is opposite in the two tables: the quadruple is (=, t3, blank, x) with the source in arg1, while the triple is (=, x, (2)) with the target in arg1. Both forms are stated, but the difference is never pointed out, so students mix them up in the quiz.
- ch 5 [low] Quiz Q3: The quadruples are written with the row number inside the tuple, (0, *, r, s, t1), but everywhere else in the chapter the row number is a label outside the four fields, e.g. 'row 0 is (*, b, c, t1)'. The same table is written two ways, and a student may read the leading 0 as the op field.
- ch 5 [low] Quiz Q5: The question asks what breaks when the first triple is moved below the second, but in the table given the move is illegal in the first place, because triple 1 uses (0). The answer explains only the renumbering cost and never says the move must also respect data dependences.
- ch 5 [low] Figure: The figure prints the temporaries as T1, T2, T3 while the text and worked example use t1, t2, t3. Case is the only difference, but a reader may treat them as different names.
- ch 6 [low] Quiz Q4: The code in the answer uses base address 1000 and index i, but the question gives neither. A student reading only Q4 cannot tell where 1000 came from or which value of i is used.
- ch 6 [low] Section 3: Only the load form t = *addr is shown. Assignment to an array element (the l-value case, id[E1] = E) never gets its store instruction, so the reader sees how a[i] is read but not how a[i] is written.
- ch 6 [low] Section 1: The declaration action list has no check for a name that already exists in the current scope, so a duplicate declaration would silently overwrite the old entry.
- ch 6 [low] Section 3: The text refers to 'the types from 4.3' as plain text. Other chapters are meant to be linked so a phone reader can jump there.
- ch 7 [high] Section 1, rule for E1 && E2: The truelist/falselist rule and explanation are wrong. It says to backpatch E1.truelist to E2 so a false E1 jumps past E2, and gives truelist = merge(E1.truelist, E2.truelist), falselist = E2.falselist. For short-circuit &&, true jumps of E1 must go to the start of E2; overall truelist is E2.truelist; overall falselist is merge(E1.falselist, E2.falselist).
- ch 7 [high] Section 1, rule for E1 || E2: The mirror rule is also stated incorrectly. It says keep E1.truelist and merge the two falselists. For short-circuit ||, a false E1 goes to E2, a true E1 is a true exit, and E2's true exits are also true exits. The overall falselist should be E2.falselist.
- ch 7 [high] Worked example 1, step 5: After combining a < b && c > d, the falselist is given as {103}. It must also contain the false jump from E1, instruction 101. The correct falselist is {101, 103}.
- ch 7 [high] Worked example 1, final answer: The final code is missing instructions 101 and 102, and instruction 100 is shown jumping to 104. That would skip the c > d test when a < b is true, so the code is not the short-circuit if-else.
- ch 7 [low] Worked example 1, statement and step 1: The condition is printed as 'if (a  d)' and 'E1 = a  d', with the operators missing. The intended condition is if (a < b && c > d), with E1 = a < b and E2 = c > d.
- ch 7 [low] Section 2, if-else steps: The bullet order omits emitting S1 before the end-of-then goto. As written, a student may emit the goto immediately after B and put S1 after the goto.
- ch 7 [high] Section 3, marker M: M.instr is called an inherited attribute. In the standard marker-nonterminal construction, M -> ε sets M.instr = nextinstr, so M.instr is a synthesized attribute, not inherited.
- ch 7 [high] Quiz Q7: The last sentence is false in general. For a non-nested procedure, the static link points to the enclosing (usually global) scope record, not necessarily to the caller's record. It equals the control link only when the caller is that same enclosing scope. In languages without nested procedures the static link may be omitted.
