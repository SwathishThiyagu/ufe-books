# c-quantum-u5: free-model run

- Book: `work/claude_figs/c-quantum-u5/tree/books/cse/c-quantum/c-quantum-u5.html`
- Status: ok
- Model calls so far: 36 (138,952 tokens in, 254,815 out), 7.7 minutes

## Checker

```
c-quantum-u5.html: 8 chapters, 13141 words, 9 figures, 164 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3, block ciphers and key distribution: The reason given for AES and DES lacking perfect secrecy ('one key is reused across blocks') is imprecise: even for a single block the key is shorter than the message, which is what rules out perfect secrecy. A student may conclude that a fresh key per block would give perfect secrecy.
- ch 1 [low] Section 3, key distribution: Diffie–Hellman is listed alongside RSA as a 'public-key method' that is 'slower' and 'usually agrees a private key for AES'. Diffie–Hellman itself does not encrypt data, so the sentence can mislead a student into thinking it is a data-encryption scheme like RSA.
- ch 1 [low] Section 1, shared-key model: The sentence 'Only a few universities teach this as a full topic' sits inside the Kerckhoffs's principle argument and breaks the flow of the definition; the point of the paragraph is that the algorithm is public and only k is secret.
- ch 2 [low] Section 1, last bullet: "Both keep the basis choice; the bit value stays secret until the sample check" reads as if the bit value is hidden from Alice and Bob. The bit is known to both of them after sifting; what is secret is the value as seen by Eve, and only the sample bits are later made public.
- ch 2 [low] Section 2, error estimation paragraph: The chapter never says what happens to the bits that are compared. A student may assume the sample bits stay in the key. Standard BB84 removes them, because they have been announced in public.
- ch 2 [low] Figure caption: "The four qubits reach Bob with Alice's bit and basis" suggests the qubit delivers the basis to Bob. The whole point of BB84 is that the qubit alone does not tell Bob which basis Alice used; he must guess.
- ch 2 [low] Figure, message list (last message): The final message is from Bob to Alice labelled 'sifted key 01'. No key is ever sent over the channel; both sides compute the sifted key independently from their own records.
- ch 3 [low] Section 1, example line: The notation drops the vector: 'p=0.9 gives ρ=diag(0.9,0.1)'. Earlier p is defined as the vector p=(p₀,p₁), and elsewhere p is also used as a single binary probability. A student may read p=0.9 as a number, not a distribution.
- ch 3 [low] Section 2 and Worked example 1 step 8: Writing S(|+⟩)=0 is shorthand: S is defined on a density matrix ρ, not on a ket. A student may think entropy can be taken of |ψ⟩ directly and be confused about which object the formula applies to.
- ch 3 [low] Section 3, first paragraph: 'Quantum systems have a similar quantity for bipartite states' is too vague; the quantity is not named, so the reader cannot connect it to the classical I(X:Y) beside it.
- ch 4 [high] quiz Q7: The question and the answer use different totals. The question says 'store only nS(ρ) − 1 qubits per copy', which for n copies means n(nS(ρ) − 1) qubits — far more than nS(ρ), not fewer. The answer instead assumes nS(ρ) − 1 qubits in total, i.e. a shortfall of only 1/n qubits per copy. Under that reading the fidelity stays bounded away from 1 but does not fall to 0, so 'the error tends to 1' is also wrong.
- ch 4 [low] section 3, theorem statement: Unit slip: 'Using fewer than nS(ρ) qubits per copy cannot give fidelity near 1.' nS(ρ) is the total for n copies, which is S(ρ) per copy. As written the sentence is false, because a rate of, say, 2S(ρ) qubits per copy is 'fewer than nS(ρ) per copy' for n > 2 yet still gives fidelity near 1.
- ch 4 [low] section 3, first bullet: 'n copies, the state ρ^⊗n, which lives in a space of 2ⁿ dimensions' is only true when ρ is a qubit. For a state on a d-dimensional space the dimension is dⁿ. The section has not restricted ρ to two levels at that point.
- ch 5 [low] Section 1, paragraph after the Holevo bound: "Equality is possible in the limit of many copies for some channels" is misleading. The Holevo bound is reached asymptotically for product signal states with collective (joint) measurements on the outputs — this is the achievability part of the HSW theorem and holds for every channel, not only some. As written, a student may conclude most channels never reach χ.
- ch 5 [low] Section 1 formula note and Quiz Q1 answer: χ is described as "the Holevo quantity in bits per channel use". For an ensemble {px, ρx} on its own, χ is just a number of bits. It becomes bits per channel use only when ρx are the outputs of one use of a channel.
- ch 5 [low] Section 2, depolarizing paragraph: The bit-flip paragraph ends by saying χ equals the capacity of a binary symmetric channel, but the depolarizing paragraph gives χ = 1 − H₂(p/2) without saying it is only the one-use value for those two inputs. A reader may carry over the capacity reading by analogy, which is not justified here.
- ch 5 [low] Figure spec, channel node note: The note "χ = 0.531 bits" sits on the channel block, which suggests χ is a property of the channel alone. χ depends on the input ensemble as well as the channel.
- ch 5 [low] Section 1, capacity formula: "limn→∞ (1/n)" is ambiguous on a phone screen; a student can read it as a product or as lim of n only.
- ch 6 [high] Section 3, Hamming(7,4) encoding example: The codeword for message 1011 is printed as 0 1 1 0 1 1 1 = 0110111. With d₂ = 0, position 5 must be 0. Check: substituting 0110111 into the parity checks gives s₁ = 0⊕1⊕1⊕1 = 1 ≠ 0, so 0110111 is not even a valid codeword. Every later step built on this word inherits the error.
- ch 6 [high] Section 3, decoding example (the 'Suppose 0110111 is sent…' paragraph): Three faults in one paragraph. (i) The sent word 0110111 is not a codeword, so the example is invalid. (ii) The arithmetic is inconsistent with the received word 0110101 — it uses d₂ = 0 while 0110101 has d₂ = 1 — and the sentence still contains draft text ('= 0… wait, recompute:'). (iii) The conclusion 'syndrome is 000 and the decoder wrongly accepts' is false, and the reason given, 'd₃ sits in all three circles', is false: d₃ is at position 6, so it is covered by checks 2 and 4 only.
- ch 6 [high] Quiz Q4 answer: The answer states the Hamming(7,4) codeword for 1011 is 0110111. The message has d₂ = 0, so position 5 is 0; 0110111 is wrong.
- ch 6 [high] Quiz Q3 answer: The distance list says d(1001, 0111) = 2. The two words differ in positions 1, 2 and 3 and agree in position 4, so the distance is 3. The final values d_min = 2 and t = 0 happen to stay correct.
- ch 6 [low] Section 2, decoding step list: The step says 'recover the message from the first k bits (for a systematic code)', but the Hamming(7,4) layout used later (p₁ p₂ d₁ p₃ d₂ d₃ d₄) does not put the k data bits first — they sit at positions 3, 5, 6, 7. A student will look for the message in the first four bits and get nonsense.
- ch 6 [low] Worked example 1, step 9: Step 9 says two flips are 'detected as a failure, not corrected', while the exam traps say a double flip gives 'a silently wrong bit'. The two statements pull in opposite directions, and the sentence 'the received block has a 1 majority only if one of the two flips hit the 0' makes no sense for block 111, which contains no 0.
- ch 6 [low] Beyond: 'see 5.7' is plain text, so the reader on a phone cannot tap through to the next chapter.
- ch 7 [high] Section 2, after the encoding bullets: The sentence 'One physical qubit now carries the logical qubit in an entangled way' is false and contradicts the whole idea of encoding. No single physical qubit holds the logical qubit; the information is spread across all three, and measuring any one of them destroys it.
- ch 7 [low] Section 1, sentence on syndrome observables: Saying the parity observables 'commute with ... the encoded state' is loose: a state is not an operator, so it cannot commute with anything. The reason α and β stay hidden is that both codewords give the same fixed outcome for every parity check.
- ch 8 [high] Section 2, transversal gates: The claim that the nine-qubit (Shor) code has transversal Hadamard and phase gates is false. Its stabilizer is not preserved by H on all nine qubits: H maps the code to a different code (X and Z generators swap), so H^⊗9 is not a logical gate for it. The same failure applies to the phase gate S. Only the transversal CNOT holds for that code, so a student would learn a wrong example of transversal Clifford gates.
- ch 8 [high] Section 3, threshold paragraph: The threshold range quoted for concatenated codes, 10⁻² to 10⁻³, is too optimistic and contradicts the chapter's own Beyond note that surface codes tolerate higher error rates than concatenated codes. Standard estimates put concatenated-code thresholds at roughly 10⁻⁶ to 10⁻⁴ under realistic noise, with optimistic ideal-circuit estimates near 10⁻³; surface codes are the ones near 10⁻².
- ch 8 [low] Section 3, first sentence of syndrome extraction: Saying the ancilla is prepared in |0> covers only Z-type stabilizers. For X-type stabilizers the ancilla must be prepared in |+> (Hadamard on |0>), and the coupling is by CNOTs in the other direction. A student meeting a circuit diagram with |+> ancillas will be confused.
- ch 8 [low] Figure caption (after Section 3): The sentence 'The ancilla touches only the syndrome step, not the data path' is misleading: during syndrome extraction the ancilla is coupled to the data qubits by CNOTs, which is exactly how the syndrome is read. What is true is that the ancilla is not a data qubit and carries no logical information.
- ch 8 [low] Quiz Q1, answer: The definition covers only two-block gates. Transversal Hadamard and phase gates act inside one block, applying the physical gate to every qubit of that block. Also 'two code blocks' should allow one or two.
- ch 8 [low] Quiz Q5, answer (and Section 3 wording 'fresh or verified'): 'A fresh or verified ancilla prevents its own error from entering the data' is too strong. Verification and freshness make an ancilla fault unlikely; they do not rule it out, and an undetected ancilla error can still propagate into the data.
- ch 8 [low] Section 2, sentence after transversal CNOT: 'These gates form the Clifford group' is loose: the set of gates that can be done transversally for one code is a subgroup of the Clifford group, usually a small finite set, not the whole group.
