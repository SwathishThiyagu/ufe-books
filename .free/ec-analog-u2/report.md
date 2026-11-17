# ec-analog-u2: free-model run

- Book: `books/ece/ec-analog/ec-analog-u2.html`
- Status: ok
- Model calls so far: 29 (133,098 tokens in, 282,069 out), 8.4 minutes

## Checker

```
ec-analog-u2.html: 8 chapters, 15846 words, 9 figures, 170 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Figure: Both output-characteristic curves are drawn as perfectly horizontal lines all the way down to V_CE = 0. A real BJT has I_C falling steeply below V_CE ≈ 0.3 V (saturation), and Section 3 of this same chapter says the real curves tilt upward with V_CE. A student may read the plot as meaning r_o is infinite and that the collector current stays at 4.71 mA even at V_CE = 0.
- ch 1 [low] Figure: The curve labelled I_B = 24 µA is placed at 2.36 mA. With β = 100 (the value used in the worked example on the same page) the current should be 2.4 mA; 2.36 mA is exactly half of 4.71 mA, so the label and the ordinate disagree by about 2 %.
- ch 1 [low] Lead: "Temperature and transistor gain drift, so the bias network must hold the point nearly fixed." The verb "drift" is buried at the end and a second-language reader can read the sentence as a list of two nouns with no predicate.
- ch 1 [low] Beyond: "The Early voltage matters more as supply voltages fall, because r_o drops and gain falls with it." Lowering the supply does not by itself lower r_o: r_o ≈ V_A/I_C depends on the bias current, and the (V_A + V_CE) correction is tiny when V_CE is a fraction of a volt. The real reason the Early effect hurts at low supply is the reduced voltage headroom, not a drop in r_o.
- ch 2 [low] Lead and Section 1 (first use of S): The stability factor S is used from the lead onward (S = 1 + β, S = 101, the comparison table, Q1) but is never defined. A student meeting S for the first time cannot tell what is being differentiated with respect to what, so the whole comparison rests on an undefined symbol.
- ch 2 [low] Table, collector feedback row: The row gives only RB = 560 kΩ, but for collector feedback I_C depends on R_C as well as R_B. A reader cannot reproduce 1.44 mA and 2.26 mA from the table alone; R_C = 2.2 kΩ appears only in Section 2.
- ch 2 [low] Worked example 1, steps 6–7 and answer: Step 6 finds I_B = 14.05 µA from the approximate I_C = 1.405 mA, while step 7 finds I_B = 12.86 µA and I_C = 1.286 mA from the exact Thevenin solution, with no comment that these are two different answers for the same quantity. The final answer then quotes only the approximate pair, although the table and figure elsewhere use the exact current.
- ch 2 [low] Section 3, design steps, last bullet: 'Check that V_CE stays above about 1 V, so the transistor never saturates on signal peaks' is not true. A quiescent V_CE of 1 V leaves almost no room for a signal; the transistor will clip on the first large peak. The 1 V check only keeps the DC operating point out of saturation.
- ch 2 [low] Section 3 (last paragraph) and Exam trap 5: The term 'emitter-stabilized bias' is used two ways. Section 3 applies it to the divider circuit with CE removed, while trap 5 warns against calling the circuit with CE across RE 'emitter-stabilized'. In most textbooks the name belongs to the fixed-bias circuit with an unbypassed emitter resistor, so both uses are loose.
- ch 2 [low] Exam traps, second bullet: 'A 0.1 V error in VB is a 7% error in IC' is true only for the worked circuit (V_E = 1.405 V). Stated as a general rule it is misleading, because the percentage error depends on the chosen V_E, which the design steps allow to be anything near 0.1 V_CC.
- ch 2 [low] Worked example 1, part (b) and answer: 'The divider draws 210.5 µA' is imprecise: 210.5 µA is the current through R2 only. R1 carries R2's current plus I_B, about 224.6 µA, so the statement understates the supply current the divider needs.
- ch 3 [low] Section 3, drain-to-gate feedback bias: The sentence 'Two resistors set the whole Q-point' is misleading. Because the gate current is zero, R_G carries no DC current and has no effect on the DC operating point; only R_D and the device parameters set it. A student may believe changing R_G shifts the Q-point.
- ch 3 [low] Section 1, enhancement NMOS square law: K_n is called the transconductance parameter, but many textbooks write the same law as I_D = ½ k_n (V_GS − V_TN)² with k_n = μ_n C_ox (W/L). A student moving between books will use the wrong factor of ½.
- ch 3 [low] Section 3, final saturation check: The saturation condition is given only 'for a JFET' and 'for an enhancement MOSFET'. The n-channel depletion MOSFET, discussed in this same section, uses the same condition with V_P and is left out, so the student may think it follows a different rule.
- ch 3 [low] Exam traps, R1/R2 trap: The trap mixes two ideas: it says R1 and R2 carry no gate current, then mentions R_G may be 1 MΩ. R_G is not part of the divider, so the last clause reads as if it explains the divider.
- ch 4 [high] Exam traps, fifth trap: The compensation direction is wrong. V_T rises with temperature, so g_m = I_C/V_T falls and r_e = V_T/I_E rises at fixed bias. Lowering the bias current makes g_m fall further and r_e rise further; it does not compensate.
- ch 4 [low] Worked example 1, part (b) and step 5: A_v = −g_m(R_L ∥ r_o) is the gain of a loaded stage, not the intrinsic gain. In standard usage the intrinsic gain is g_m r_o, the gain with the output open. Calling the loaded value 'intrinsic' can confuse a student who meets the term g_m r_o later.
- ch 4 [low] Section 2, g_m formula: V_T = kT/q is written without saying what k and q are, though every other symbol is defined.
- ch 5 [low] Section 2, first bullet: The sentence 'base current i_b flows through r_e carrying i_e ≈ β i_b' says the base current flows through r_e. Physically the emitter current flows through r_e; the base current only sees the reflected value. A student can read this as v_i = i_b r_e and then be confused by the next line.
- ch 5 [low] Section 2, table (body) vs figure: The body table gives CB current gain as '≈ 1' while the text of Section 3 says it is α = β/(β+1), always below 1, and the figure says '<1'. The two tables on the same page disagree.
- ch 5 [low] Section 2, last paragraph: 'The CE stage has the highest voltage and current gain of the three' is not exact. The CC stage's current gain is β+1, which is larger than the CE value of β. The real distinguishing feature of CE is the voltage gain (and power gain).
- ch 5 [low] Section 4, R_out formula and worked example step 9: The division should be by (β+1), not β: R_out = r_e + (R1 ∥ R2 ∥ R_S)/(β+1). The chapter states the general rule as 'divided by β' and uses β in the numbers. The answer is only about 1 % off here, but the rule as written is an approximation, not the standard result.
- ch 5 [low] Exam traps, fourth bullet: The symbol 'α_e' clashes with α, which this chapter has already defined as the CB current gain (just below 1). Writing 'α_e ≈ β + 1' invites confusion between the two.
- ch 6 [low] Section 1, square-law paragraph: The warning 'Some books put a factor ½ inside Kn' is backwards and will confuse a student. With the formulas used here, ID = Kn(VGS − VTN)² and gm = 2√(Kn ID), this book's Kn already contains the ½ (Kn = ½μnCox W/L). The sentence suggests the opposite.
- ch 6 [low] Section 2 text and Figure: The figure plots the source follower at 40 dB middle-band, but the chapter states (correctly) that its gain is below one, i.e. below 0 dB. A curve sitting at 40 dB contradicts that, and the y-axis is labelled 'gain (dB)' although the plotted values are not real gains.
- ch 6 [low] Section 3 (CD formula), worked example 1(c) and exam trap 4: The source-follower gain gmRs/(1 + gmRs) and the trap 'use Rs ∥ RL in place of Rs' drop ro, although Section 2 insists ro must be kept whenever it is comparable to the drain-side resistance. A reader with a large Rs (comparable to ro) will get a gain that is too high.
- ch 6 [low] Exam traps, third bullet: Saturation needs two conditions, but only VGS > VTN is mentioned. A student may think VGS > VTN alone puts the device in saturation.
- ch 7 [high] Worked example 1, step 3: The factor is written as r = √(21/2 − 1). That expression equals √9.5 ≈ 3.08, not √0.414214 ≈ 0.643594. The superscript is missing, so the worked step is wrong as printed.
- ch 7 [high] Section 1 bullet and Section 3 table (RC row): The chapter says RC coupling is used in IF strips and lists 'Audio, IF' as its typical use. Standard IF strips use tuned transformer coupling; RC coupling is typical for audio and low-frequency amplifiers.
- ch 7 [low] Section 2 and Section 3 table (Transformer row): The phrases 'There is no DC path' and 'Blocked by coil' can mislead. The primary coil carries the collector bias current; what is blocked is the DC path from primary to secondary by transformer isolation.
- ch 7 [low] Quiz Q3 answer: The answer mentions only the high-frequency roll-off. Cascading also raises f_L, so the bandwidth shrinks from both ends.
- ch 8 [low] Section 1, last paragraph of the cascode explanation: The headroom cost is stated as 'Q1 needs VCE1 plus Q2's VBE, about 1 V extra'. The total minimum voltage from supply rail to output is indeed about 0.9–1 V (VCE1(sat) + VBE2), but the amount of extra headroom compared with a plain CE stage is only Q2's VBE, about 0.7 V. The word 'extra' with 'about 1 V' overstates the penalty and contradicts the table row that gives the cascode 0.7 V.
- ch 8 [low] Section 1, Miller pole sentence: The input pole is given as f = 1/(2π RsCM), as if the source resistance were the only resistance at the input node. The transistor's own rπ (and any base bias resistance) sits in parallel with Rs, so when Rs is large the formula overstates the pole frequency. The chapter itself says later that the input sees rπ of Q1.
- ch 8 [low] Figure caption: The caption says the upper chain 'stacks a common-emitter on a common-base stage', which reverses the physical order. In a cascode the common-base device Q2 sits on top of the common-emitter device Q1, as the lead and Section 1 correctly say.
- ch 8 [low] Section 3, comparison table, 'DC offset' row: The row puts two different quantities side by side. For the Darlington, 1.4 V is the input-to-output base-emitter drop of a buffer. For the cascode, 0.7 V is not an input-output offset at all; it is the extra DC headroom at the output (VBE of Q2). A student will read both as the same kind of offset.
