# c-quantum-u1: free-model run

- Book: `books/cse/c-quantum/c-quantum-u1.html`
- Status: ok
- Model calls so far: 20 (70,881 tokens in, 170,428 out), 5.2 minutes

## Checker

```
c-quantum-u1.html: 7 chapters, 12730 words, 8 figures, 134 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, Deutsch bullet (and repeated in Quiz Q4 answer): "He also gave the first algorithm with a proven quantum speedup" overstates the 1985 paper. The 1985 algorithm succeeds only with probability 1/2 and does not by itself give a proven separation from classical algorithms; the standard first proven (deterministic, single-query) separation is the Deutsch–Jozsa algorithm of 1992.
- ch 1 [low] Section 3, comparison table, Read-out row: The cell text "one result, probability |amplitude|²" contains pipe characters, which are the table's column separators, so the row will break into extra columns and display wrongly.
- ch 1 [low] Figure (gantt spec and its aria text): Bars of several years' length are drawn for one-year results (Deutsch 1985–1994, BB84 1984–1994, Grover 1996–2000). A reader takes the bar ends as the years when the work happened, so Grover appears to run until 2000 and Deutsch until 1994.
- ch 1 [low] Section 3, paragraph after the table: "Unitary gates are reversible, so a quantum circuit has no built-in erasure" can mislead: measurement and reset do discard information, and ancilla qubits are uncomputed and thrown away. Only the gate itself is information-preserving.
- ch 1 [low] Section 3, end of the paragraph after the table: "The last row of the table is the honest summary" has no clear referent; the last row lists extra resources, and the sentence that follows talks about speed, not resources.
- ch 2 [low] Section 3, first paragraph: The chapter says a complex vector space obeys 'nine rules' and then lists what most textbooks give as ten axioms, because closure under addition and closure under scalar multiplication are normally counted separately. A student asked to 'list the axioms' may lose marks for writing nine.
- ch 2 [low] Section 1, division sentence: The division formula z / w = z w̄ / |w|² is given without the condition that makes it valid. A student may apply it with w = 0.
- ch 2 [low] Section 2, formula note: 'the same z also has arguments θ + 2πk for every whole number k' — whole numbers are usually taken as 0, 1, 2, … so negative turns are excluded, and full turns in the clockwise direction are missed.
- ch 2 [low] Section 1, second paragraph: 'Two operations turn z into a usable geometric object' uses the words 'two operations' for conjugation and modulus, while Section 3 uses the same words for vector addition and scalar multiplication. The clash can confuse a reader about what an operation is.
- ch 2 [low] Section 3, C² sentence: The cross-reference '(see Unit 2, Qubits, Postulates and Entanglement)' is written as plain text, so on a phone the reader cannot jump to that chapter as the series format intends.
- ch 3 [low] Quiz Q7: The question asks the student to show cⱼ=⟨j|ψ⟩ 'using completeness Σ|i⟩⟨i|=I', but the given answer never inserts the identity. It goes straight from ⟨j|ψ⟩=⟨j|Σᵢcᵢ|i⟩ to the orthonormality step. A student following the question's instruction will look for a completeness step that is not there, and the exam answer does not match the question asked.
- ch 3 [low] Worked example 1, step 3: The step jumps from ⟨ψ|ψ⟩ to |α|²+|β|² without stating why the cross terms disappear. The reason is that ⟨0|0⟩=⟨1|1⟩=1 and ⟨0|1⟩=⟨1|0⟩=0, which the chapter has covered but the example does not cite. On a phone read the week before the exam, the jump looks like a rule to memorise.
- ch 4 [low] Quiz Q6: The answer jumps to λ²−4λ+3=0 from trace 4 and determinant 3, but the chapter never states the 2×2 characteristic relation λ² − (tr A)λ + det A = 0 or defines trace. A student meeting trace for the first time in a quiz cannot follow the step.
- ch 4 [low] Section 3, last paragraph: "Eigenvalues reveal the scaling directions of an operator" mixes up the two objects: eigenvectors give the directions that are not turned, eigenvalues give the scale factors along them.
- ch 5 [low] Section 4, phase gate S paragraph: The sentence 'S is unitary, because its eigenvalues 1 and i both have modulus 1' uses a necessary condition as if it were a test. Plenty of non-unitary matrices have all eigenvalues of modulus 1 (for example [[1, 1], [0, 1]]), so the 'because' does not actually prove unitarity, even though for this diagonal S the conclusion is true.
- ch 5 [low] Section 4, paragraph after the table: 'A matrix that is both satisfies U² = I' reuses the letter U, which the chapter has just defined as a unitary matrix, for a matrix that is Hermitian and unitary. A careless reader can read it as 'every unitary satisfies U² = I', which is false (S² ≠ I).
- ch 5 [low] Beyond: 'The Solovay–Kitaev theorem says this can be done efficiently to any target accuracy, which is why fault-tolerant designs count gate counts' links the theorem to gate counting too loosely; the counting habit comes from the cost of fault-tolerant gates (T gates and magic states), not directly from the approximation theorem.
- ch 6 [high] Lead: The lead says "Every gate on several qubits is then a matrix formed by the Kronecker product". That is false: a Kronecker product A ⊗ B only builds gates that act on the qubits one at a time. CNOT and other genuinely joint multi-qubit gates are not Kronecker products, and Section 3 of this same chapter says so, so the lead contradicts the body and will mislead a student.
- ch 6 [low] Section 1, dimension formula: "the product space has mn dimensions" reads as if the space has mn different dimensions; the standard wording is that its dimension is mn.
- ch 6 [low] Quiz Q3 answer: "A sum m + n would describe a state that lies in one space or the other, not in both at once" is loose: the direct sum V ⊕ W does have dimension m + n and holds a pair of vectors. What it fails to give is the product amplitudes cij = vi wj, the cross terms between the two systems.
- ch 6 [low] Beyond: "compress the mn-sized vectors of many-body systems" uses mn, the two-factor symbol from earlier. For n qubits the joint vector has 2ⁿ amplitudes, not mn, so the size is understated and the notation is confusing here.
- ch 7 [low] Section 2, the formula box: The formula uses rank-1 projectors |λk⟩⟨λk| but the note says the sum runs over all distinct eigenvalues. For a degenerate operator these two statements cannot both hold: a rank-1 projector does not cover a whole eigenspace, so A = Σ λk|λk⟩⟨λk| over distinct λk is false.
- ch 7 [low] Section 1, sentence on convergence: The claim that the matrix series converges whenever the number series converges at every eigenvalue is only guaranteed for diagonalisable A. A defective matrix (a Jordan block) also needs the differentiated series to converge, so the rule as written can fail.
- ch 7 [low] Section 2, after the formula: "f(A) has the same eigenvectors as A" is not always true. If f takes the same value on two different eigenvalues of A, f(A) has extra eigenvectors; for example f(A) = I when f is constant on the spectrum.
- ch 7 [low] Exam traps, first trap: The trap quotes entries 1 and e but never names the function being applied, so a student cannot tell that the example is about exp.
