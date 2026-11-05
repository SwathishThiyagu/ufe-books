# c-toc-u1: free-model run

- Book: `books/cse/c-toc/c-toc-u1.html`
- Status: ok
- Model calls so far: 37 (124,833 tokens in, 126,133 out), 5.3 minutes

## Checker

```
c-toc-u1.html: 9 chapters, 12075 words, 10 figures, 138 KB
OK
```

## For the reviewer

- chapter 5: a python program's shown output was replaced by its real output; check the text around it
- chapter 8: a c program's shown output was replaced by its real output; check the text around it
- chapter 1: a python program's shown output was replaced by its real output; check the text around it
- chapter 4: worked example 1: the example's "check" code printed no numbers

## Reviewer notes (after any revision)

- ch 1 [high] Section 1: The sentence "The empty string ε belongs to every language that contains no symbols" is factually incorrect and confusing. Languages are sets of strings, not symbols, and ε does not automatically belong to every language.
- ch 1 [low] Quiz Q3: The answer says "Any language L ⊆ Σ* can therefore include ε" which suggests ε is always included.
- ch 1 [low] Quiz Q5: The question asks for the size of Σ* and the number of strings of length exactly 4, but the answer only gives the latter (16) and does not mention that Σ* is infinite.
- ch 1 [low] Worked example 1, step description: The step label repeats "step 1: Step 1:" which is redundant and may confuse readers.
- ch 2 [high] Section 3 (Design example): The transition from state q₂ is defined to stay in q₂ for both input symbols. This makes the DFA accept any string that contains the suffix 01 anywhere, not only strings that end with 01.
- ch 2 [high] Section 3 (Design example) – transition table: The table shows q₂ → q₂ on both 0 and 1, matching the wrong transition definition.
- ch 2 [high] Section 3 (Design example) – trace for w = 11001: The trace lists q₁ → q₀ after reading the second ‘0’, but with the correct transition q₁ on ‘0’ stays in q₁.
- ch 2 [high] Worked example 1 – Python code: The simulation code implements the same wrong self‑loop on q₂, so it accepts strings that only contain 01 as a substring.
- ch 2 [high] Quiz Q4: The answer says the string 0010 is accepted, but it ends with 10, so it should be rejected.
- ch 2 [high] Quiz Q6: The justification claims adding a self‑loop on q₀ for symbol 0 would change the language to all strings. In fact it would make the language empty because the DFA could never reach the accept state.
- ch 2 [low] Section 2 (Components of a DFA): Procedural steps (read symbol, look up, move) are mixed with component definitions, which may confuse beginners.
- ch 2 [low] Section 1 (Formal definition) – acceptance condition: The indexing in qᵢ₊₁ = δ(qᵢ, aᵢ₊₁) can be unclear for students.
- ch 3 [low] Quiz Q4: The answer is vague – it tells the student to look up the DFA definition but does not give the concrete state that should appear in the table.
- ch 3 [low] Section 1, bullet about start state: The wording "The start state has an incoming arrow from nowhere" can be misread as an arrow that exists but comes from nowhere.
- ch 4 [high] Section 3 (Acceptance example): The text says the computation tree splits after the third symbol, but the NFA has only one possible transition at each step for the input 110101, so no branching occurs.
- ch 4 [high] Figure specification after the example: The graph description lists edges p→q and p→r both labeled '0' and omits state s, which does not match the NFA defined in the text.
- ch 4 [high] Quiz Q3: The answer states the resulting set after reading "01" is {p,r}, but the correct set is {p,q}. The transition from q on input 1 goes to q, not r.
- ch 5 [high] Worked example 1, steps 2‑4: The example claims to add ε‑moves labelled with the symbol 0, which is impossible because ε‑moves have no input label. Later it says there are no ε‑edges and the epsilon_closure function returns only the state itself, contradicting the earlier description.
- ch 5 [high] Quiz Q6 (design a tiny ε‑NFA for a?b): The provided NFA has self‑loops on both states and omits the required ε‑transition from the state after reading ‘a’ to the state that reads ‘b’. This does not recognise the language a?b.
- ch 5 [low] Section 1, algorithm bullet list: Bullet says “Pop a state r from the stack and add r to ε‑closure(s)”. This wording suggests adding r to the ε‑closure of s, which is incorrect.
- ch 5 [low] Section 1, algorithm bullet list: Bullet says “Put the start state s in a stack.” The algorithm is generic for any state q, not necessarily the start state s.
- ch 6 [high] Section 1 formula: The definition of ε‑closure only adds states reachable by a single ε‑move, missing the transitive closure over any number of ε‑moves.
- ch 6 [high] Section 3 table: The transition for DFA state {p,r} on input symbol 1 is shown as ∅, but according to the NFA it should go to {p,r}. This contradicts the worked example.
- ch 6 [low] Worked example step 6: It states that the empty set ∅ is added as a dead state for missing transitions, but all transitions for symbols 0 and 1 are already defined, so the dead state is unnecessary for completeness.
- ch 7 [low] Section 3: The sentence "Collect all unmarked pairs into equivalence classes" is ambiguous because equivalence classes are formed from states, not from pairs. The algorithm must group states that are mutually unmarked (i.e., none of the pairs among them are marked) and then take the transitive closure.
- ch 7 [low] Worked example step 3: The phrase "the successor pair (q2,q2) which is trivially identical and unmarked" may confuse readers because (q2,q2) is not an entry in the table; same‑state pairs are considered indistinguishable by definition, not merely "unmarked".
- ch 7 [low] Worked example – dry run placeholder: The line "dry run: {'head': [], 'rows': []}" is a stray placeholder that adds no value and may distract students.
- ch 8 [high] Quiz Q5: The answer claims that converting the Mealy machine from the worked example requires four Moore states (q0_0, q0_1, q1_0, q1_1). In this specific machine each state receives incoming transitions with a single output value, so only two Moore states are needed: one with output 1 (representing last bit 0) and one with output 0 (representing last bit 1). The four‑state construction is unnecessary and incorrect.
- ch 8 [high] Quiz Q6: The answer argues that a two‑state Mealy machine cannot generate the output sequence 0 0 1 0, claiming a third state is needed. This reasoning is incorrect; a two‑state Mealy machine can produce that sequence by appropriate choice of transition outputs and next‑state mapping.
- ch 9 [high] Section 1: Definition and transition function: The automaton is described as a 6‑tuple but seven components are listed (Q, Σ, δ, q₀, F, ⊢, ⊣). Either the end‑markers are not counted as separate components, making it a 6‑tuple, or the description should say 7‑tuple.
- ch 9 [high] Section 1: Definition and transition function: The acceptance condition says the automaton accepts if it enters an accepting state while the head is on either end‑marker. Standard definitions accept when the automaton enters an accepting state and halts, regardless of head position. Requiring the head to be on an end‑marker changes the recognised language.
- ch 9 [high] Section 3: Two‑way automaton for the palindrome 10101: The described head‑visit order shows 11 positions (⊢ → 1 → 0 → 1 → 0 → 1 → ⊣ → 1 → 0 → 1 → ⊢) which corresponds to 10 moves, but the text claims "Nine moves are performed before acceptance". The count is inconsistent.
- ch 9 [low] Section 3: Two‑way automaton for the palindrome 10101: State names contain typographical symbols: qₐccept and q₍reject). These are unclear and may confuse readers.
- ch 9 [low] Worked example 1 (steps): The step description mixes states q₁ and q₂ inconsistently. Steps 2‑5 keep the automaton in q₁, while step 6 says it moves to q₂ after comparison, but the transition for q₂ moving left back to ⊢ is never defined.
- ch 9 [low] Quiz Q4: The answer does not directly point out the flaw asked for. The question asks to identify the flaw in the claim that a 2DFA can recognise the language of all strings containing substring 101. The answer should state that the claim is not a flaw about power because the language is regular, but the unnecessary use of a two‑way model is the flaw.
- ch 9 [low] Quiz Q5: The provided crossing‑sequence is incomplete. A crossing‑sequence lists the sequence of states the automaton is in each time it crosses the same boundary, not just a single transition each way.
