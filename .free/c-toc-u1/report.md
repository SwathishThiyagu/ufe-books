# c-toc-u1: free-model run

- Book: `books/cse/c-toc/c-toc-u1.html`
- Status: ok
- Model calls so far: 39 (156,622 tokens in, 272,894 out), 8.3 minutes

## Checker

```
c-toc-u1.html: 9 chapters, 15691 words, 10 figures, 167 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Figure (nested sets spec): The sample items listed for the outer box Σ* include '11', but 11 is one of the four strings in the inner box L, since L is the set of all length-2 strings. In a nested drawing this puts the same string both inside and outside L.
- ch 1 [low] Section 1 and Worked example 1, step 1: The bars |·| are used with two different meanings: |w|=3 is the length of a string, while |L|=4 in the worked example is the number of elements of a set. A student reading quickly may take |L| as the length of L.
- ch 2 [high] Quiz Q4: The answer says the divisible-by-3 machine accepts ε, aaa, aba. The string aba has only two a's, so its a-count is 2, not divisible by 3, and the run ends in state 2, which is not final. The example contradicts the machine just described.
- ch 2 [low] Section 3, no two consecutive 1s: The states are listed but the chapter never says which ones are final. A student cannot finish the design from this description alone, while the other three designs in the section do mark their final states.
- ch 2 [low] Section 2, the run definition: The run is written as r0, r1, …, rn with ri = δ(ri−1, ai), but the symbols a1a2…an, the indices and ri−1 are left in plain text, so the subscripts do not read clearly on a phone screen.
- ch 3 [low] Beyond: 'Transition tables are the input format for lexer generators and regular-expression engines' is factually wrong: lexer generators take regular-expression specifications as input, and the DFA transition table is what they produce. Regex engines also take patterns, not tables. A student could repeat this in an interview.
- ch 3 [low] Worked example 1, answer line: 'the check prints 2, 1, 1, 0' refers to a program that is never shown in this chapter, and the order of the four numbers (state, accept flag, state, accept flag) is not stated. The reader cannot tell what is being printed or verify it.
- ch 3 [low] Figure (δ̂(A, 1001) step by step): The second cell of each row is just 'no' or 'yes' with no column header, so a student cannot tell that it means 'is this state final?'. In the row 'read 1' the state is A and the cell says 'no', which looks like an answer to an unstated question.
- ch 3 [low] Section 3 heading: The heading says 'column by column', but the trace is built one row per prefix, and the text says the rows are prefixes. The heading and the method it introduces do not match, which can confuse a reader about what to write in the exam.
- ch 4 [low] Section 1 (formula explainer) and Quiz Q1 answer: The power set is written as 2<sup>Q</sup> in the displayed formula but as plain "2Q" in the sentence "2Q is the power set of Q" and in the Q1 answer "δ: Q × Σ → 2Q". A student copying this may write 2Q, which reads as two times Q.
- ch 4 [low] Section 2, extended transition function: The union is written "⋃q ∈ P δ(q, a)" with the index on the same line, so it can be read as multiplying by q. The symbol δ̂ is also the usual notation for the string-extended function on a single state, δ̂(q, w), which the subset-construction chapter uses.
- ch 4 [low] Section 1, third paragraph: "The figure shows q0 looping on 0 and 1..." points to the figure, but the figure is placed after Section 3, far below. On a phone the reader sees the reference before the picture.
- ch 4 [low] Section 1, second paragraph: "The machine may stay in q, move to another state, or have no move at all" reads as if staying is always allowed. Staying in q on symbol a is possible only when q ∈ δ(q, a).
- ch 4 [low] Whole chapter, plus Section 3 "ending in ab" bullet: The start state is written q₀ in the formal tuple and q0 in the traces and tables, so a reader may think these are two different things. The "ending in ab" bullet also uses "δ(q2, ·) = ∅" without saying what the dot · means.
- ch 5 [high] Quiz Q7: The answer is wrong for the machine in the chapter. In the ε-free NFA of step 9, δ'(q0,a) = {q0,q1} and δ'({q0,q1},b) = {q2,q3}, so reading ab ends in the set {q2,q3}, which contains q3. With F = {q3}, ab is still accepted. In fact every set produced after a move is already ε-closed (q2 never appears without q3), so for this machine F = {q3} and F' = {q2,q3} accept exactly the same strings — no string is wrongly rejected. The stated reason ('q2 had a free move to q3') describes deleting edges by hand, not the construction the chapter teaches.
- ch 5 [high] Beyond: lex and flex do not run an ε-NFA by tracking state sets with closures. They build a Thompson NFA, then convert it to a DFA by subset construction, and the generated scanner runs that DFA. The claim that they avoid building a full DFA is false for these two tools.
- ch 5 [low] Section 1, where-clause of the transition formula: The formula writes 2<sup>Q</sup> but the explanation just after it writes '2Q is the set of all subsets of Q'. Without the superscript it reads like an ordinary product.
- ch 5 [low] Exam traps, fifth trap: 'Closing before the move gives a different, wrong set' is misleading. The set you move from must already be closed — that is exactly why the run starts at ECLOSE(q0) — and closing a closed set changes nothing. What actually goes wrong is dropping the closure after the move.
- ch 5 [low] Worked example 1, output block: The output lists five numbers (2, 2, 2, 1, 2) but the steps state four counts: |ECLOSE(q0)| = 2, |ECLOSE(q2)| = 2, |δ̂(q0,ab)| = 2 and |F'| = 2. No reading of the steps gives 2, 2, 2, 1, 2, and the fifth number is unexplained.
- ch 6 [high] Section 3, proof and the acceptance sentence that follows it: The claim is written as δ̂_D({q₀}, w) = δ̂_N(q₀, w), but the DFA start state is q_D0 = ECLOSE({q₀}), not {q₀}. With the usual definition δ̂_D(S, ε) = S, the left side at w = ε is {q₀}, while the base case asserts it is ECLOSE({q₀}). So the stated identity, and the later sentence 'accepted by D exactly when δ̂_D({q₀}, w) contains a final NFA state', are simply false for any NFA that has ε-moves — exactly the case this chapter handles.
- ch 7 [low] Figure (Pairs marked at each pass): The caption says the last row is blank and shows the stopping condition, but the figure spec fills that row with the cell '—'; the caption and the drawing disagree. The row labels also say 'length 0/1/2' while the title and the worked example talk about pass numbers, which can make a student think 'length' counts something other than the round.
- ch 7 [low] Section 2, Why it works: The sentence 'Some syllabi describe the inner test as distinguishing one string from another' says nothing usable: the inner test compares two successor states, not two strings. A student will stop and wonder what it means.
- ch 7 [low] Section 3, last paragraph: The Myhill-Nerode condition is stated one-sidedly: 'no continuation z makes xz accepted and yz rejected'. As written it does not forbid the reverse case (xz rejected, yz accepted). The phrase 'right-invariant equivalence classes of the Myhill-Nerode relation' is also loose; the relation is a right congruence and its classes are classes of strings.
- ch 8 [high] Quiz Q6: The answer runs the machine on the wrong input. It walks 0, 1, 0, 1 instead of the given 0, 1, 1, 0, so the reported output 01100 is wrong. On B with input 1 the machine stays in B and prints 1, but the answer moves to A and prints 0.
- ch 8 [low] Section 3, Mealy to Moore, closing line: "both accept and print the same language behaviour" uses the word accept for a machine that has no final states, and the construction as written does not print the same string: the Moore machine prints the chosen initial symbol c before the Mealy output.
- ch 8 [low] Section 3, Moore to Mealy: The conversion λ′(q, a) = λ(δ(q, a)) silently drops λ(q₀), so the Mealy machine prints n symbols where the Moore machine printed n + 1. A student may think the outputs are identical and be confused when they are not.
- ch 9 [high] Section 1, with worked example 1 step 7 and the third exam trap: The transition function is declared total, δ: Q × (Σ ∪ {⊢, ⊣}) → Q × {L, R}, and an exam trap says δ must be defined on both markers. The machine drawn in the figure has no move for the pair (q2, ⊢). Step 7 of the worked example depends on exactly that missing move: on the empty input the head returns to ⊢ in state q2 and the chapter calls it a 'non-final halt'. Under the stated definition that machine is not a legal 2FA, so the definition and the chapter's own example contradict each other.
- ch 9 [low] Figure, edge q2 → qf: Every other edge carries a direction with its symbol ('⊢ / R', 'a, b / R', '⊣ / L', 'b / R'), but the edge q2 → qf is labelled only 'a'. Worked example 1 step 4 uses δ(q2, a) = (qf, R), so the figure is missing the direction.
- ch 9 [low] Section 2, paragraph 3 (and quiz Q6): Saying the state count of the simulating DFA 'grows like 2ⁿ' fixes an exact rate that is not what the theory gives. The safe statement is that the blow-up is exponential in the worst case; the precise base and exponent are a separate research result and are not simply 2ⁿ.
- ch 9 [low] Section 1 definition and Section 2 theorem: δ is defined as an ordinary function, which makes the machine deterministic, but the theorem then talks about 'nondeterministic two-way FAs' accepting the same class, and that variant is never defined in the chapter. A student cannot tell what changes in the tuple for the nondeterministic case.
