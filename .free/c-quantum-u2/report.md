# c-quantum-u2: free-model run

- Book: `books/cse/c-quantum/c-quantum-u2.html`
- Status: ok
- Model calls so far: 30 (110,140 tokens in, 229,426 out), 5.5 minutes

## Checker

```
c-quantum-u2.html: 9 chapters, 14857 words, 10 figures, 162 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, Postulate 1: H is defined only as 'a vector space with an inner product'. The standard definition of a Hilbert space also requires completeness (it is a complete inner-product space), and an examiner will expect that word.
- ch 1 [low] Section 2, Postulate 2: U(t)=e^{-iHt/ħ} is written without saying it holds only when the Hamiltonian H does not depend on time. With a time-dependent H the exponent becomes an integral and students who copy this blindly lose marks.
- ch 1 [low] Section 1, paragraph on amplitudes: The sentence 'Amplitudes are not probabilities; their modulus squared are' has broken grammar and can be misread as saying the amplitudes themselves are squares.
- ch 1 [low] Section 2, Postulate 3, first sentence: 'A projective measurement uses Hermitian operators' can be misread as saying the measurement itself is an operator; the operato is the observable being measured.
- ch 2 [high] Section 4 (Where the advantage comes from: interference): The numbers mix amplitudes with probabilities. Two paths of amplitude 1/2 each have probability 1/4 each, so ordinary probabilities add to 1/4 + 1/4 = 1/2, not to 1/2 + 1/2 = 1. As written, the sentence 'Ordinary probabilities would simply add to 1/2 + 1/2 = 1' treats the amplitude 1/2 as if it were a probability, and it contradicts the correct treatment in Quiz Q7.
- ch 2 [low] Section 2, paragraph after the normalisation formula: 'A real bit picks one corner of a square' is misleading: a single bit has two values, while a square has four corners (four corners would fit two bits). A student may think a bit has four choices.
- ch 3 [high] Quiz Q7 (question and answer): The question says both students 'measure in the computational basis, then both apply H', but the answer then says H turns the states into |0⟩ and |1⟩ with certainty. After a real measurement the superposition is destroyed and the state collapses to |0⟩ or |1⟩; applying H to a collapsed state gives |+⟩ or |−⟩, so no certain outcome is possible. The certain outcomes only happen if no measurement is made. The answer also mixes up which amplitudes cancel: for (1/√2, 1/√2) the |1⟩ amplitudes cancel and the |0⟩ amplitudes add, while for (1/√2, −1/√2) it is the other way round.
- ch 3 [low] Lead: 'their squares give the measurement probabilities' is wrong wording for complex amplitudes: the square of a complex number is not a probability. The rest of the chapter correctly uses the modulus squared.
- ch 3 [low] Exam traps, bullet 4: 'the matrix multiplies the whole state, and both amplitudes change' is inaccurate: a gate can leave one amplitude unchanged, for example Z acting on |+⟩ keeps α = 1/√2 and only flips the sign of β. A student may think every gate must change both entries.
- ch 4 [high] Section 3, final paragraph: The sentence is broken: "A mixed state has r Chapter 2.6." Words are missing, so the key statement (mixed states have vector length less than 1 and sit inside the sphere) never reaches the student.
- ch 4 [low] Section 1 and Exam traps (also Quiz Q2, Quiz Q3 answer): Exponentials are written without superscript in the running text: "r₀eiγ₀", "eiδ", "eiφsin(θ/2)", "eiα|ψ⟩", "eiπ sin(π/4)". A phone reader can misread e·i·γ₀ as a product of three symbols instead of e raised to iγ₀, and the formula block uses <sup> while the text does not, so the notation looks inconsistent.
- ch 4 [low] Section 1, 'Why θ/2?': The stated reason ("The two basis states must be orthogonal") does not by itself explain why the angle on the sphere is twice the Hilbert-space angle. Orthogonality is what makes the poles antipodal, but the doubling needs to be said: orthogonal states are 90° apart as state vectors yet 180° apart on the sphere.
- ch 4 [low] Section 3, formula 'where' line and the paragraph after it: The symbol r is used both for the vector, r = (sinθ cosφ, sinθ sinφ, cosθ), and for its length, "Bloch vector length r = 1". Students can confuse the vector with the scalar length.
- ch 5 [low] Section 1, paragraph 1 (and Section 3, paragraph 1): Superscripts are missing: the text writes "P_m2=P_m" where it means P_m²=P_m. Read on a phone, P_m2 can look like P_m times 2, and it contradicts the same book's own use of P_m² in the exam traps and Q8.
- ch 5 [low] Section 2, paragraph 2: "p(+)=|(a+b)/√2|2 and p(−)=|(a−b)/√2|2" — the modulus is closed but the square is written as a plain 2, so the formulas read as if the probability equals a number times 2.
- ch 5 [low] Exam traps, last bullet: "Writing a probability greater than 1 after ... dropping the modulus" mixes two different mistakes: dropping the modulus leaves a complex amplitude, not a number above 1.
- ch 6 [low] Section 1: The formula ρ = Σ p_i |ψ_i⟩⟨ψ_i| reads as if the state fixes the probabilities p_i and the kets |ψ_i⟩. Many different ensembles give the same ρ, and the |ψ_i⟩ need not be orthogonal, so a student may think the decomposition is unique.
- ch 6 [low] Section 1: The sentence 'A mixed state has at least two nonzero eigenvalues' can be confused with the number of terms in the ensemble. An ensemble can have several terms and still give a pure ρ if the kets coincide.
- ch 6 [low] Section 1: 'Some syllabi call this topic density operators' comes after the section has already defined density operators, so the sentence is redundant and its placement is confusing.
- ch 6 [low] Section 2: 'When A and B are separate' can be misread as spatial separation, which is not what defines a composite system; two qubits in the same trap are still A and B.
- ch 6 [low] Worked example 1, step 4: The step states the diagonal blocks but never shows why the off-diagonal entries ρ_{00,10} and ρ_{01,11} vanish, so the reader has to trust the jump.
- ch 7 [high] Section 1, paragraph starting 'Non-factorability is the definition': The claim 'Tracing out Bob leaves Alice with the mixed state I/2, the maximally mixed state' is presented as a general property of entangled states. It holds only for the maximally entangled (Bell) states. A general entangled state such as (|00⟩+|11⟩)/√(2−ε)... i.e. any state with unequal Schmidt coefficients, gives a reduced state that is mixed but not I/2; for example √0.9|00⟩+√0.1|11⟩ leaves Alice with diag(0.9, 0.1). A student will carry away the wrong rule that every entangled qubit looks locally maximally mixed.
- ch 7 [low] Section 2, last paragraph: No-cloning is stated for 'an unknown entangled qubit', which wrongly suggests the restriction is special to entangled qubits. The theorem applies to any unknown quantum state.
- ch 8 [low] Section 1 (why the classical bound is 3/4): The reason given ('making a = b always fails at (1,1), and making a ≠ b always fails at the other three') only covers the two special strategies where the answers match everywhere or differ everywhere. A general deterministic strategy is a fixed pair of functions a(x) and b(y), so a and b can match on some input pairs and differ on others; the stated argument does not by itself prove that no such strategy wins all four rows.
- ch 8 [low] Exam traps, third bullet (the (1,1) row): The clause 'even if this state hides the error' is confusing and is not true as written. For |Φ+⟩, E(1,1) = −1/√2, so wrongly using Pwin = (1 + E)/2 on the (1,1) row gives (1 − 0.7071)/2 ≈ 0.1464, not 0.8536 — the mistake is glaring, not hidden.
- ch 9 [high] Section 3, last sentence of the section: 'measuring one part of a pair fixes the other part's axis' reads as if the measurement on one particle reaches across and changes the distant particle. That is not what entanglement does, and a student will come away with an action-at-a-distance picture.
- ch 9 [low] Section 1 and Section 2: The chapter writes μ = -g(e/2m)S, so S_z = +ħ/2 gives a negative μ_z, and with dB/dz > 0 those atoms are pushed toward the weaker-field side. Yet Section 2 calls the upper spot 'spin-up along z' without fixing the sign convention. A student who follows the algebra will place spin-up at the lower spot.
- ch 9 [low] Section 1, first use of ħ: ħ appears in 'S_z = +ħ/2 or S_z = -ħ/2' with no definition. It is defined only in the answer to Q8.
- ch 9 [low] Beyond: 'the Schrödinger form ... is tighter for mixed states' is not right. The extra covariance term is nonzero whenever the two observables are correlated in the state, and that happens for pure states too (a squeezed state, for example). Mixedness is not the condition.
- ch 9 [low] Section 1, definition of g: 'g ≈ 2 is the Landé factor' is loose. In μ = -g(e/2m)S acting on a single electron spin, g is the electron spin g-factor (2.0023); the Landé g-factor is the factor for atomic fine structure, which happens to equal 2 for a pure-spin state like this one.
