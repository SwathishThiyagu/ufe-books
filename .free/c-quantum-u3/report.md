# c-quantum-u3: free-model run

- Book: `books/cse/c-quantum/c-quantum-u3.html`
- Status: ok
- Model calls so far: 37 (146,256 tokens in, 230,457 out), 5.0 minutes

## Checker

```
c-quantum-u3.html: 8 chapters, 14284 words, 9 figures, 157 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Exam traps, third bullet (trap 2 on H not being NOT): The claim "only X takes |0⟩ to |1⟩" is not exactly true: Y|0⟩ = i|1⟩, which is the state |1⟩ up to a global phase, so a measurement on Y|0⟩ also gives 1 with certainty. The chapter itself teaches that global phase is unobservable, so this sentence contradicts it and can confuse a student.
- ch 2 [high] Exam traps, second bullet: The trap says the sequence CNOT(2→1), CNOT(1→2), CNOT(2→1) is a common wrong answer that does not swap. That sequence does swap: on (a, b) it gives (a⊕b, b), then (a⊕b, a), then (b, a). It is the same circuit as the listed order with the two qubit names exchanged. A student who checks it will find it works, so the trap teaches a false rule.
- ch 2 [low] Figure, node c2 note: The note on the middle gate reads 'b⊕(a⊕b)=a', but the value produced by that gate is on qubit 1 and equals a⊕(a⊕b)=b. The expression shown belongs to the third gate, so the chain of intermediate values in the figure is inconsistent with the text.
- ch 3 [high] Section 3, first sentence: The sentence 'Exact universality with {H,T,CNOT} is false for every single-qubit rotation' is false. Many single-qubit rotations are exact members of the set — T itself is a rotation by π/8, and Z = T⁴, S = T², X = HZH are all exact finite products of H and T. The very next sentence of the chapter gives the correct claim (failure for angles that are not rational multiples of π), so the first sentence also contradicts it. A student will conclude that no rotation can ever be exact.
- ch 3 [low] Section 3, sentence on global phase: 'a factor eiφ' is written as plain letters, not as e to the power iφ; read literally it looks like e × i × φ. The chapter's own style rule asks for Unicode superscripts, as used elsewhere (e<sup>iπ/4</sup>).
- ch 3 [low] Lead, first sentence: The lead defines a universal gate set as 'a small finite collection of gates', but Section 1 correctly allows continuous (infinite) sets such as arbitrary single-qubit rotations. The narrow definition can confuse a student who then meets continuous universal sets.
- ch 3 [low] Section 2 formula and Worked example step 1: The intermediate powers are typed in LaTeX style, e^{iπ/2} and e^{iπ/4}, with braces, while the chapter otherwise uses Unicode superscripts (e<sup>iπ/4</sup>). Mixed notation looks untidy and braces read as literal characters on a phone.
- ch 4 [high] Section 3, fourth identity bullet: The claim that X before and after a CNOT on the target wire exchanges control and target is false. Pauli-X commutes with the target flip, so (I⊗X) CNOT(q0→q1) (I⊗X) = CNOT(q0→q1) — the circuit is unchanged, not reversed. Control and target are exchanged only by Hadamards on both wires, which the chapter already says in the bullet above, so this bullet also contradicts itself.
- ch 4 [high] Section 3, the HZH formula note: The note says 'the product is read right to left as Z first, then H, then H'. In HZH the rightmost factor is H, so H acts first, then Z, then H (= (HZH)|ψ⟩ means H applied last). The stated order contradicts the chapter's own convention and gives the wrong recipe if a student follows it, even though the final matrix X is correct.
- ch 4 [high] Worked example 1, output block: The shown output is '0.5 / 0.5 / 0.7071', which does not match the four probabilities computed in step 4 (0.5, 0, 0, 0.5) and mixes a probability (0.5) with an amplitude (0.7071). A student copying this will write down a wrong answer for the probabilities of 01 and 10.
- ch 5 [low] Beyond: The sentence 'Some syllabi group it under quantum computational complexity; the complexity classes themselves are in Unit 4' is misleading. No-cloning is a consequence of linearity and unitarity, not a complexity-class topic, and the pointer sends students to material that has nothing to do with the theorem.
- ch 5 [low] Section 2, closing paragraph: 'A unitary gate preserves inner products, so the contradiction is final' comes after the contradiction is already shown by direct comparison of A and B, and a student can read it as though the value 1/√2 itself broke unitarity. The sentence does not say which two states are being compared by unitarity.
- ch 5 [low] Exam traps, third bullet, and Beyond: The no-deleting principle is named twice but never defined, so a student reading only this chapter cannot say what it is.
- ch 5 [low] Section 3, second bullet, and Quiz Q5: 'Bell state' is used without a definition in this chapter; Q5 leans on it to explain why the CNOT output is not a clone.
- ch 5 [low] Section 1, third paragraph: 'For a unitary gate, U(α|0⟩ + β|1⟩)|0⟩ = ...' suggests linearity is a property of unitary gates only. Every quantum gate, unitary or not, acts linearly; unitarity is what is used later for inner products.
- ch 6 [high] Section 1 heading: The heading 'Protocol: two qubits, two bits, one state' miscounts the qubits. The protocol needs three qubits: the unknown qubit q0, Alice's half of the Bell pair q1 and Bob's half q2. The body of the section itself says 'Label the three qubits q0, q1 and q2', so the heading contradicts it and a student revising from headings will get the resource count wrong.
- ch 6 [low] Section 1, starting-state formula: Writing |Ψ₀⟩ = (α|0⟩ + β|1⟩) ⊗ (|00⟩ + |11⟩)/√2 puts the 1/√2 outside the tensor product, so it can be read as dividing the whole product, or as not dividing the second factor. The normalisation is ambiguous on first reading.
- ch 6 [low] Exam traps: The traps switch between correct statements ('Do not say teleportation copies |ψ⟩', 'Bob needs both classical bits') and bare errors ('Mix-up the corrections', 'Forget that the Bell pair is consumed'). The two forms read differently, and 'Mix-up the corrections' can look like advice to mix them up.
- ch 7 [low] Exam traps, last bullet (reversed CNOT): The claim that reversing control and target 'decodes into a different, wrong bit string' is too strong. With the reversed CNOT (Bob's qubit as control, Alice's as target) followed by H on qubit 1, the messages 01 and 11 happen to be recovered correctly; only 00 and 10 give random results. So a student testing message 01 gets 01 and concludes the trap is wrong.
- ch 7 [low] Section 3, comparison with teleportation: 'in both cases the entanglement is destroyed by the decoding step' is inaccurate for teleportation. There the shared pair is used up by Alice's Bell measurement, long before Bob applies his correction gates; Bob's decoding destroys nothing.
- ch 8 [high] Section 2, first two sentences, and Section 3, sentence 'StatevectorSampler is an exact statevector tool': StatevectorSampler (from qiskit.primitives) does not return a statevector or amplitudes. It is a noise-free sampler: it evolves the state exactly on a classical computer and returns sampled bitstrings (counts) for a measured circuit, with shots. A student will expect amplitudes from it and get bitstrings, and the claim 'no shots are involved' is wrong for this tool. Amplitudes come from AerSimulator with save_statevector(), or from Statevector.from_instruction(qc).
- ch 8 [low] Figure, first node: The node is labelled 'Circuit(2)', but the worked example and Section 1 use QuantumCircuit(2, 2). A student may copy the wrong constructor and then have no classical bits for measure().
