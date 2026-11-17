# s-chem-u4: free-model run

- Book: `books/common/s-chem/s-chem-u4.html`
- Status: ok
- Model calls so far: 35 (127,203 tokens in, 252,278 out), 6.1 minutes

## Checker

```
s-chem-u4.html: 9 chapters, 15964 words, 10 figures, 169 KB
OK
```

## For the reviewer

- chapter 3: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 3: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Quiz Q7 (answer): The student in the question added the two reduction potentials with their own signs, (−0.76) + (+0.34). The answer says the negative result came from 'subtracting in the wrong order', which misdescribes what the student did and teaches the wrong diagnosis. The real error is signing the anode potential: the anode's reduction potential must be subtracted (i.e. its sign flipped) when it oxidises.
- ch 1 [low] Exam traps, first bullet: The wording 'Do not add the two electrode potentials with their signs and then forget the anode sign' is self-contradictory: it says both 'do not add' and 'do not forget the sign'. A student cannot tell which mistake is being warned against.
- ch 2 [low] Lead: "Read through ΔG = −nFE, the same equation ties cell voltage to Gibbs free energy and to the equilibrium constant K" is garbled: you read through a derivation, not an equation, and "the same equation" has no clear antecedent.
- ch 2 [low] Beyond: "Plotting E against pH and potential" repeats the same quantity twice and reads as if pH and potential were two things being plotted against a third.
- ch 2 [low] Quiz Q2, answer: The coefficient 0.0296 is written without its unit, so a student copying the answer loses the volt.
- ch 3 [low] Section 1, formula line: The term 'log[Cl⁻]²' is ambiguous: a student can read it as (log[Cl⁻])² instead of the log of the squared concentration.
- ch 3 [low] Section 2, advantages: The range is given as 'about pH 1 to 12' with no warning about the errors at the ends of that range, so a student may trust readings near pH 12.
- ch 3 [low] Section 2, cell notation: The cell is written as glass | test solution || KCl (sat) | Hg₂Cl₂, Hg, which leaves out the inner Ag/AgCl reference and the 0.1 M HCl inside the glass bulb, so the notation does not match the parts described just above it.
- ch 4 [high] Figure (plot spec for HCl + NaOH): The plotted points do not form the two straight lines the caption and text promise. From 0 to 20 mL the fall is 1 unit per mL (40 → 30 → 20), but from 20 to 25 mL it falls 2 units per mL (20 → 10). After the minimum the rise is 2 units per mL (10 → 20) and then 1 unit per mL (20 → 30). A student sees a bent curve, not a V of straight lines meeting at 25.0 mL, and the intersection/slope reading being taught is contradicted by the picture.
- ch 4 [low] Exam traps, third bullet: The bullet mixes two different mistakes. Using concentration in mol m⁻³ really does give a 1000-fold error (1 mol m⁻³ = 0.001 mol L⁻¹, so the answer comes out 1000 times too small). Substituting resistance R for κ is simply the wrong quantity, not a 1000-fold error, so the sentence misleads.
- ch 5 [high] Quiz Q5 (answer): The answer says that because the terminal voltage is lower 'the motor also sees a lower voltage, so it may draw more current and heat up'. This teaches a wrong rule. For a given mechanical load, a lower supply voltage makes a DC motor run slower; current stays roughly the same for a constant-torque load and falls for a fan-type load. Current rises mainly when the motor is heavily loaded or stalled. Students will carry away 'low voltage means more current' as a general law.
- ch 5 [low] Section 2, table row for coulombic efficiency: 'Discharge charge divided by charge charge, times 100' is unreadable; 'charge charge' looks like a typo and students may not see it means the charge put in during charging.
- ch 5 [low] Section 2 table (energy density row) and its explanation: The chapter uses one term, energy density, for both Wh kg⁻¹ and Wh L⁻¹. Many textbooks call Wh kg⁻¹ specific energy and reserve energy density for Wh L⁻¹, so a student meeting the other convention may be confused.
- ch 6 [high] Quiz Q4: The formula V_terminal = EMF − I(R_internal + polarization) adds a voltage (polarization) to a resistance, which is dimensionally wrong. Internal resistance drops IR volts, while polarization is itself a voltage drop.
- ch 6 [low] Section 2 and the Lead paragraph: LiFePO₄ is listed as an alternative cathode but the cell voltage is then given as 3.6–3.8 V for any Li-ion cell. LiFePO₄ cells give about 3.2–3.3 V, so a student may apply 3.7 V to an LFP cell.
- ch 6 [low] Section 1, last paragraph: "The lead sulfate is the active change" is vague; students may not see that it means both plates are converted to PbSO₄.
- ch 7 [low] Section 3, first paragraph: The same letter C is used for two different things: capacitance in farads and the unit of charge, coulombs (C). A student reading 'Q is charge in coulombs (C) ... and C is capacitance in farads (F)' can confuse the symbol with the unit.
- ch 7 [low] Section 1, overpotential paragraph: 'Activation overpotential is extra voltage to start the electrode reactions' is loose. Activation overpotential is the extra voltage needed to drive the charge-transfer step at the required current; it exists even when the reaction is already running.
- ch 7 [low] Section 1, formula note: Standard conditions for E° are stated as 25 °C and 1 bar only. The standard potential also requires unit activity (about 1 M) for dissolved species; without this a student may think pressure and temperature alone fix E°.
- ch 7 [low] Section 3, power formula: P = V²/(4R) is presented as 'maximum power' without saying when it applies. It is the power delivered only when the load resistance equals the equivalent series resistance; a student may use it as the power for any load.
- ch 8 [high] Section 2 (Rusting of iron), the reaction chain: The chain '2Fe + O₂ + 2H₂O → 2Fe(OH)₂ → Fe₂O₃·xH₂O' shows the ferrous hydroxide step as if it were a balanced reaction. It is not: converting Fe(OH)₂ to hydrated ferric oxide is an oxidation that consumes more dissolved oxygen, and the printed arrow obeys neither the O nor the H balance. Students will copy this as a single equation and lose marks.
- ch 8 [low] Quiz Q1 answer: The answer defines corrosion as 'the electrochemical oxidation of a metal', which is narrower than the definition given in Section 1 (chemical or electrochemical attack). Dry oxidation at high temperature is chemical, not electrochemical, so the quiz answer contradicts the chapter's own definition.
- ch 8 [low] Worked example 1, steps 2-3: A galvanic current of 10 mA on 1.0 cm² gives 10 mA cm⁻², which for iron corresponds to roughly 100 mm of metal lost per year — a thousand times more than the 0.05-0.5 mm year⁻¹ figures quoted later in the chapter. The arithmetic is right, but the number is physically absurd and can mislead a student about real corrosion current densities.
- ch 9 [high] Section 2, tinning bullet: The area relationship is reversed. A scratch in tinplate exposes a small area of steel (the anode) beside a large area of tin (the cathode). The chapter says the small tin area makes the steel corrode faster, which contradicts the standard explanation and the chapter's own Q7 logic.
- ch 9 [high] Quiz Q4, answer: Same reversed area statement: 'the small tin area makes the exposed steel corrode faster'. The exposed steel, not the tin, is the small area and the anode.
- ch 9 [low] Lead paragraph: 'Corrosion eats steel where an electrolyte, oxygen and an anodic site meet' suggests oxygen is always required. Some corrosion (for example, in waterlogged soil with sulfate-reducing bacteria) occurs with little or no oxygen.
- ch 9 [low] Exam traps, trap 3: 'A tin scratch attacks the steel' is loose; it does not say which area is anode and which is cathode, so a student may repeat the reversed-area mistake.
- ch 9 [low] Figure spec: The root label is 'Corrosion', but the tree, the caption and the aria text all describe corrosion control. A reader can misread it as a classification of corrosion types.
- ch 9 [low] Section 1, anodic reaction: The ion is written 'Mn+' without a superscript, so it can read as a product called Mn+ rather than a metal ion with charge n+.
