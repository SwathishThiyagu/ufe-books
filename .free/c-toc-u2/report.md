# c-toc-u2: free-model run

- Book: `books/cse/c-toc/c-toc-u2.html`
- Status: ok
- Model calls so far: 33 (105,092 tokens in, 106,143 out), 4.2 minutes

## Checker

```
c-toc-u2.html: 9 chapters, 12433 words, 10 figures, 136 KB
OK
```

## For the reviewer

- chapter 9: a c program's shown output was replaced by its real output; check the text around it
- chapter 7: a python program's shown output was replaced by its real output; check the text around it

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q5: The answer claims that the leading parentheses in (0|1)* are unnecessary. In fact, parentheses are required to group the union before applying the Kleene star; without them the expression would be interpreted as 0|1* which has a different meaning.
- ch 1 [low] Section 3, bullet about A*B*: The statement "Do not write A*B*; write (A*) (B*) if you want two independent repetitions" is misleading. A*B* already denotes two independent repetitions (first A any number of times, then B any number of times). Adding extra parentheses is unnecessary and may confuse students.
- ch 2 [low] Section 1: The union operator ‘|’ is used before it is defined.
- ch 2 [low] Section 2: The second star law a* = ε | a*·a is mentioned in the text but not included in the formula block.
- ch 2 [low] Star law description: The sentence “The law shows that adding one more copy of a does not change the language.” is slightly misleading; a·a* is a subset of a*, not equal to a*.
- ch 3 [high] Worked example 1, step 6 and answer summary: The example claims the minimal ε‑NFA for (a|b)*·a·b·b has 7 states and prints 7, but Thompson’s construction actually yields 14 distinct states (6 for the a|b union, 2 for the star, and 6 for the three literals).
- ch 3 [high] Figure spec for the literal fragment: The graph shows ε‑edges before and after the a‑labeled edge, which contradicts the definition of a literal fragment (only a start state, an a‑labeled edge, and an accept state).
- ch 3 [low] Section 4, practical notes: The sentence “Label start states with an incoming arrow from nowhere.” may be unclear to students.
- ch 4 [high] Section 2 (Arden’s theorem) – generic statement about self‑loop on start state: The text says: “If a DFA has been reduced to two states s and f with a self‑loop on s labelled P and a direct edge s → f labelled Q, then the language is Q·P* by Arden’s theorem.” This reverses the order of concatenation. With a loop on the start state, accepted strings are any number of P repetitions followed by Q, i.e. P*·Q, not Q·P*.
- ch 4 [high] Worked example, step applying Arden’s theorem on state 2: The example defines Q = a·b·ε and P = a, then claims the result is a·b·a*. In the equation for state 2 we have R = ε + R·a, so Q should be ε (the direct ε‑edge to the final state) and P = a (the self‑loop). Using a·b as part of Q is incorrect.
- ch 5 [high] Worked example 1, step 2: The description says "Create a single‑state NFA for a* with a loop on ‘a’ and ε‑edges to start and accept", which is not how Thompson’s construction builds a*; it creates two new states (new start and new accept) with ε‑edges to the inner ‘a’ NFA and an ε‑edge back.
- ch 5 [high] Worked example 1, steps 6‑11: The ε‑closures, subset construction steps and the claim that all DFA states are accepting are incorrect. For the given expression a* (b a*)* the DFA does not have every subset containing an accept state, and the listed subsets (e.g., {s4}) are not derived from the correct NFA.
- ch 5 [high] Section 3 (From DFA to regular expression): The sentence "Arden’s theorem guarantees that solving the resulting system of equations gives the same expression obtained by state elimination" is misleading; Arden’s theorem guarantees a solution to a system of regular‑expression equations, but it does not guarantee that the solution matches the expression produced by state elimination.
- ch 5 [low] Section 2 (From regular expression to NFA): The bullet "The resulting NFA may have many ε‑moves; they are removed by subset construction if a DFA is needed" is inaccurate; subset construction does not remove ε‑moves but uses ε‑closure to handle them.
- ch 5 [low] Section 1 (Statement of Kleene’s theorem): The statement repeats the equivalence twice, making it redundant and slightly confusing for beginners.
- ch 6 [high] Quiz Q5: The answer claims that the pumping lemma cannot be used to prove non‑regularity of the language L = {0^{10^n} | n ≥ 0}. This is false; the pumping lemma can be applied to show this language is not regular.
- ch 6 [high] Quiz Q6: The answer incorrectly states that the language of strings with equal numbers of 0s and 1s is regular and satisfies the pumping lemma. In fact, this language is not regular and does not satisfy the pumping lemma.
- ch 6 [low] Worked example 1, step 3: Step 3 says “Let y be the first two 0s”, but the later decomposition uses y as the last two 0s of the first block (x = 000, y = 00). This inconsistency may confuse students.
- ch 6 [low] Quiz Q5 notation: The language is written as {0¹⁰ⁿ | n ≥ 0}, which can be misread as 0^{10n}. The intended language is strings of 0 whose length is a power of 10.
- ch 6 [low] Quiz Q5 answer wording: The phrase “may still produce a power of 10 for some n” is vague and does not explain why the pumping lemma fails to give a contradiction.
- ch 7 [high] Section 3, example building DFA for (0|1)*01: The text says "two states: q0 start, q1 after seeing a 0, q2 after seeing 01" – that is contradictory. The DFA for (0|1)*01 needs three states, not two.
- ch 7 [high] Worked example 1, step 1 – regular expression for the complement ¬L: The given expression (0|1)*0(0|1)* ∪ (0|1)*1(0|1)* is wrong. It describes all non‑empty strings, not the set of strings that do not end with 01.
- ch 7 [low] Section 2, decision properties: The statement "All four problems are decidable in time linear in the number of states of the automata" is inaccurate for equivalence (and finiteness) which require constructing a product automaton and can take O(n1·n2) time.
- ch 7 [low] Section 1, concatenation description: The description mentions making every final state of D1 non‑accepting and adding ε‑transitions to D2, but does not explicitly state that the final states of D2 remain accepting in the resulting NFA.
- ch 8 [high] Lead paragraph: The text says the Myhill‑Nerode theorem gives a precise way to decide if a language is regular. The theorem provides a characterization, not an effective decision procedure for arbitrary languages.
- ch 8 [high] Worked example step 13: It states that after reading "11" the suffix becomes empty. The suffix is not empty; it is a string that does not end with 0 or 01, which belongs to the class [ε].
- ch 8 [low] Worked example code block: A C program that prints "3" is unrelated to the Myhill‑Nerode discussion and may confuse readers.
- ch 8 [low] Quiz Q3 answer: The class description "[no a seen]" is vague and can be misinterpreted.
- ch 9 [high] Section 1, formula S_total: The formula S_total = Σ_i |Q_i| claims the total number of DFA states after merging equals the sum of the states of each token DFA, which is generally false because merging can share states.
- ch 9 [high] Section 2, description of DFA state count: It says the DFA has ten states (0 … 10), but counting from 0 to 10 inclusive gives eleven states.
- ch 9 [high] Worked example 1: The example says “draw the DFA with ten states”, but the correct DFA for a 10‑digit mobile number needs eleven states (including the start state).
- ch 9 [high] Exam traps: It claims that the character class [6‑9] also matches the hyphen, which is incorrect; the hyphen denotes a range inside the brackets.
- ch 9 [low] Section 1, bullet about merging DFAs: The wording “using a start‑state that branches on the first character” may mislead readers; merging DFAs is usually done by adding a new start state with ε‑transitions to each token DFA before applying the subset construction.
