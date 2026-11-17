# ec-circuits-u2: free-model run

- Book: `books/ece/ec-circuits/ec-circuits-u2.html`
- Status: ok
- Model calls so far: 24 (91,059 tokens in, 218,938 out), 5.4 minutes

## Checker

```
ec-circuits-u2.html: 7 chapters, 13609 words, 8 figures, 137 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1: Mesh currents and KVL: R₁₂ = R₂₁ is defined as the positive shared resistance, but the equations use R₁₁i₁ − R₁₂i₂ = v₁ and −R₂₁i₁ + R₂₂i₂ = v₂. Section 2 and the exam trap define the matrix off-diagonal R_kj = −(shared resistance). The same symbol R₁₂ has opposite signs in the two places, so a student will use the wrong sign.
- ch 1 [high] Quiz Q3: The figure contains a 5 A source in branch 2-3, so the circuit forces i₁ − i₂ = 5 A. The question gives i₁ = 5 A and i₂ = 1 A, which gives 4 A in that branch and contradicts the source. The arithmetic answer 4 A is correct for the numbers but impossible for the circuit shown.
- ch 1 [high] Section 3: Supermesh: 'If three meshes meet at a current source' is topologically impossible in mesh analysis. A current source is a two-terminal branch and can be shared by at most two meshes, or lie in one outer mesh.
- ch 1 [high] Beyond: SPICE uses modified nodal analysis (nodal equations), not mesh equations. Power-system load-flow software normally uses nodal bus equations (Ybus), not loop equations. The aside gives two wrong examples of where mesh/loop equations are used.
- ch 1 [low] Section 3: Supermesh, first paragraph: 'KVL through that branch is impossible' is misleading. KVL is not impossible; it introduces the unknown voltage across the ideal current source, so it cannot be used alone without another equation.
- ch 2 [high] Section 2, supernode voltage constraint definition: The symbols vₐ and v_b are defined as 'the node at the positive/negative terminal', not as the voltage at those nodes. The formula vₐ − v_b = V_s then appears to subtract nodes, and a student can misread what vₐ and v_b mean.
- ch 2 [low] Section 2, dependent-source sentence: The text writes a VCCS as gₘvₓ and then adds gₘ(vₐ − v_b) without stating that a and b are the control nodes or that vₓ = vₐ − v_b. The substitution is not true for every VCCS.
- ch 2 [low] Section 3, matrix-form paragraph: 'A voltage source between non-reference nodes changes one row' is imprecise. The supernode replaces the two individual KCL rows by one supernode KCL row plus one voltage-constraint row, so two rows are affected.
- ch 2 [low] Exam traps, reversing the constraint: The statement that using v₂ − v₁ = 5 V would 'flip both answers' is not numerically correct for the worked circuit; it gives different values, not sign-flipped or swapped values.
- ch 3 [low] Section 1, paragraph on linear elements: Saying v = L di/dt and i = C dv/dt are "straight lines through the origin" is right for the resistor's v–i graph but loose for L and C: the straight-line relation is between v and di/dt (or dv/dt), not between v and i. A student may think an inductor's v–i plot is a line.
- ch 3 [low] Section 2, worked-example derivation paragraph beginning "Why it works" in Section 1: "Such a set has exactly one solution" is stated without a condition. A nodal or mesh system has exactly one solution only when the coefficient matrix is nonsingular; some circuits (certain dependent-source and ideal-source combinations) have no solution or many. The superposition argument does not need uniqueness.
- ch 3 [low] Quiz Q3 answer: "Zeroing its gain deletes a real contribution" is confusing. Superposition switches off a source by making its value 0, not by touching the gain constant μ, g, r or β.
- ch 3 [low] Quiz Q4 answer: The sentence "as long as the group runs and the single-source runs together cover every source exactly once" is hard to follow and makes it sound as if both group runs and single-source runs are needed.
- ch 4 [high] Worked example 1, step 1 (and steps 2–3, answer): Step 1 changes the circuit that the question states. The question says the 12 V + 4 Ω combination 'feeds a 6 Ω resistor connected across the output terminals a-b', which makes the 6 Ω the load sitting across a-b. Step 1 declares the 6 Ω part of the network because 'the terminals a-b are the two ends of the 6 Ω resistor' — but every element across the terminals has its ends at a-b, so that reasoning is circular. With the 6 Ω as the load, the open-circuit voltage is 12 V (no current, no drop across 4 Ω) and R_th is 4 Ω, not 7.2 V and 2.4 Ω. The chapter's numbers are self-consistent, but they answer a different circuit from the one written.
- ch 4 [high] Quiz Q4: Same misreading as Worked example 1. 'A 10 V source is in series with 5 Ω and feeds 5 Ω across the output terminals' makes the second 5 Ω the load across a-b. With it removed, V_th = 10 V and R_th = 5 Ω, not 5 V and 2.5 Ω. The given answer only holds if the 5 Ω is inside the network.
- ch 4 [low] Section 2 (last paragraph) and Exam traps, 'Sign of I_N': 'A sign slip here is the commonest way to report a negative R_th' overstates the case and blurs the cause. A wrong sign in I_N makes the two forms disagree in direction. It produces a negative R_th only if you then compute R_th = V_th/I_sc with that wrong-signed I_sc. A genuinely negative R_th comes from dependent sources, as Section 1 correctly says.
- ch 4 [low] Section 3, test-source example: The phrase 'a dependent voltage source 2V_x from c to b' does not state which end is positive, yet the whole solution rests on V_c − V_b = 2V_x. A student who reads the arrow the other way gets V_c = 2V_t and a different R_th.
- ch 5 [high] Section 2: The sentence giving the sign of the derivative is broken: 'The derivative is positive when RL th and negative when RL > Rth'. The first inequality has lost its '< Rth' part (the '<' has been swallowed as markup), so the condition is unreadable and a student cannot follow the max/min argument.
- ch 5 [low] Section 3: The pointer to the AC case is written as plain text 'see 2.7', not as a link to the other chapter, so a reader on a phone cannot jump to it.
- ch 6 [high] Section 1 (Reciprocity theorem), second paragraph: The statement is incomplete: it says only 'take a network with no dependent sources', but reciprocity as written (I_1 = I_2, I_2/V_s = I_1/V_s) is false if other independent sources are still active in the network. Total currents then contain a superposition of the other sources' response, which does not swap.
- ch 6 [low] Section 1, current-source form: It says a current source in branch 1 'produces voltage V_2 at branch 2' without saying branch 2 must be open-circuited; a student may leave a load connected and get a different voltage after the swap.
- ch 6 [low] Section 2, after the branch-current formulas: 'At node A, Σ J_k = 0' holds only because the parallel branches are the sole connections to node A. A reader could apply it with an extra load or source also attached to A.
- ch 6 [low] Section 3, third paragraph: 'It survives nonlinear resistors, time-varying elements and dependent sources' is loose: with time-varying elements the balance holds at each instant of time, not over an interval of changing currents and voltages.
- ch 7 [low] Section 3, conjugate-match formula box: The box states Z_L = Z_th* without saying this is the condition for maximum average power transfer. A student skimming may read it as a general rule for any load.
- ch 7 [low] Section 2, superposition formula and step list: The formula defines |V_k| as a peak amplitude, but the chapter's phasors (and the worked example) are RMS. The step 'Write the time waveform for that frequency' does not say to multiply an RMS phasor magnitude by √2, so a student can get the amplitude wrong by √2.
- ch 7 [low] Figure caption and first block: The caption says the flow starts from a 'time-domain AC circuit', but the first block is labelled with the phasor V_s = 10∠0° V RMS, not a time-domain waveform.
