# c-quantum-u6: free-model run

- Book: `work/claude_figs/c-quantum-u6/tree/books/cse/c-quantum/c-quantum-u6.html`
- Status: ok
- Model calls so far: 28 (112,501 tokens in, 243,260 out), 10.0 minutes

## Checker

```
c-quantum-u6.html: 5 chapters, 10446 words, 6 figures, 124 KB
OK
```

## For the reviewer

- chapter 4: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, 'Why not solve exactly?' and Quiz Q7 answer: The text says quantum phase estimation 'reads an eigenvalue of H bit by bit and returns E₀'. QPE returns an eigenvalue of H drawn according to the overlap of the prepared input state with the eigenvectors; it returns the ground energy only if the input state has large overlap with the ground state and enough ancilla qubits are used. As written, a student concludes QPE always outputs E₀.
- ch 1 [low] Section 1, third paragraph: 'no measurement noise can push ⟨H⟩ below E₀' is true only for the exact expectation value. A finite-shot estimate of ⟨H⟩ can and does land below E₀, which is exactly what the shot noise in Worked example part (e) produces, so the two statements look contradictory.
- ch 1 [low] Exam traps, third bullet (parameter-shift rule): 'gives the exact derivative of the sampled expectation value' is imprecise. With a finite number of shots the shifted combination is a noisy estimate; the exactness of the rule applies to the analytic expectation value (no finite-difference truncation error).
- ch 1 [low] Section 1, 'Why not solve exactly?': Grover search and amplitude amplification do not compute ground-state energies; they speed up searching an unstructured set of candidates. Mentioning them here as the 'exact' alternative to VQE can make a student think Grover solves the ground-state problem.
- ch 1 [low] Section 3, second paragraph: 'a few layers of RY on both qubits and a CNOT between them, so three or four angles' — each such layer contributes two RY angles, so the count is always even (2 per layer); 'three' cannot occur.
- ch 1 [low] Quiz Q7 answer: The abbreviation 'QPEA' is used without being introduced; the chapter calls the method 'quantum phase estimation (QPE)' and gives no '(see Unit 4)' pointer in the quiz answer.
- ch 2 [high] Exam traps, bullet 1: The sentence 'taking a square root can create negative kernel entries' is wrong. p₀ is a measured probability and is never negative, so its square root is also never negative. Nothing in that step can produce a negative kernel entry, and a student will learn the wrong reason for using the squared modulus.
- ch 2 [low] Quiz Q7: The answer's last reason is shaky: 'using it directly can give an invalid kernel'. The state-overlap Gram matrix K_ij = ⟨φ(x_i)|φ(x_j)⟩ is itself positive semidefinite, so the real fault is that hardware does not hand you the amplitude at all, and the entries may be complex, which a standard SVM solver cannot take.
- ch 2 [low] Section 3, loss paragraph: The index k is reused. It first labels the M training pairs in the mean-squared-error sum, then labels the class in the cross-entropy L = −Σ y_k log p_k, with p_k called 'the predicted probability of class k'. A student can read the cross-entropy sum as running over training samples. The 1/M averaging over samples is also missing from the cross-entropy line.
- ch 2 [low] Figure spec: The dashed return edge goes from the classical SVM back to 'Measure overlap'. For each new pair the data must be encoded again, so the loop logically returns to the feature map, not to the SVM step.
- ch 3 [high] Section 2, first lines ('For a 4×4 image in 4 qubits, a 2-qubit U acts like a 2×2 filter'): This contradicts Section 1. In amplitude encoding the 4 qubits store the 16-value index, so no qubit belongs to one pixel or one spatial position. A 2-qubit gate therefore mixes index amplitudes; it does not slide over 2×2 pixel windows. A student will wrongly infer that qubit pairs are image patches, and that a 4×4 image in 4 qubits somehow has 16 spatial positions to filter.
- ch 3 [low] Section 2 ('The reduced state can be mixed, so repeat the circuit to get counts'): The 'so' gives the wrong reason. A mixed reduced state is still a fixed state; you repeat the circuit because a finite number of shots only estimates the outcome probabilities, whether the state is pure or mixed.
- ch 3 [low] Section 3, Status sentence (also echoed in Beyond and Q6): The double negative 'no advantage on a task classical deep learning does not already solve' is easy to misread, and read literally it says the opposite of the intended point.
- ch 4 [high] Lead and Section 1: The chapter says every industrial use is first written in binary variables and turned into a Hamiltonian or QUBO, and that every use follows the same three stages. Option pricing is an expectation estimated by amplitude estimation, and credit/fraud uses a quantum kernel; neither is a QUBO and neither returns a bitstring to repair.
- ch 4 [high] Section 2, grid unit commitment formula: The text says the penalty applies 'whenever supply falls below demand', but the term λΣ(D_t−ΣP_g u_{g,t})² squares the difference and so penalises both shortage and surplus equally. A student will think only shortage is penalised.
- ch 4 [high] Section 2, grid unit commitment formula: a_g u_{g,t} is charged in every slot the generator is on. That is a fixed/no-load on-cost, not a start-up cost; a start-up cost should be charged only when u changes from 0 to 1.
- ch 4 [high] Section 4, docking: With only y_g=1 if 'a ligand atom' sits in cell g, the model cannot say which ligand atom is in which cell. Bond lengths and atom-type contacts need atom-specific assignments. The phrase 'one atom per cell' is also the wrong constraint; standard constraints are one cell per atom and at most one atom per cell.
- ch 4 [high] Section 4, Status: The sentence 'Every instance above is small enough for a laptop to simulate, tens of qubits at most' contradicts the earlier statement that a lithium–air candidate or catalyst surface needs far more qubits than today's hardware holds, and it is false for the full grid, docking and folding instances described.
- ch 4 [high] Exam traps, second bullet: The claim that a portfolio QUBO without the holding-count penalty returns the empty portfolio is false. Holding nothing gives cost 0, but holding assets with positive expected return gives negative cost unless λ is very large, so the unpenalised model may hold many assets or all positive-return assets. The penalty is needed to force exactly K holdings, not to prevent an automatic empty answer.
- ch 4 [low] Figure caption and root note: The figure says all six problems map to a Hamiltonian or QUBO, and includes Option pricing. Option pricing is handled by amplitude estimation, not by a QUBO.
- ch 5 [low] Worked example 1, dry run table: The third column is headed 'bits after Grover', but the first row is RSA-2048, which is broken by Shor's algorithm, not Grover. A student may think Shor is a Grover-style search.
- ch 5 [low] Exam traps, fifth trap: 'Grover gives one square-root step, not repeated squaring' is confusing: repeated squaring is a step inside modular exponentiation, not the mistake being warned about. The mistake is halving the key size again and again.
- ch 5 [low] Section 2, post-quantum cryptography paragraph: 'public-key schemes built on lattice problems and on hash functions' reads like a complete list. Post-quantum public-key schemes also come from error-correcting codes and from multivariate equations, and code-based schemes are part of the standardisation effort.
- ch 5 [low] Worked example 1, code block: The first line prints the literal 0 rather than a computed value, so the code does not actually show the RSA case being calculated.
