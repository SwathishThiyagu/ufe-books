# ec-circuits-u4: free-model run

- Book: `work/ec-circuits-u4/tree/books/ece/ec-circuits/ec-circuits-u4.html`
- Status: error
- Model calls so far: 25 (88,139 tokens in, 215,180 out), 6.0 minutes

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, paragraph after the Q formula: The sentence “A high Q gives a tall, narrow peak” is misleading. In the normalised plot the peak height is always 1, and with R fixed the resonant current I₀ = V/R does not depend on Q. High Q sharpens/narrows the curve; it does not by itself make the peak taller.
- ch 2 [low] worked example 1, step 4: The example asks for and computes the bandwidth (f₀/Q = 159.15 Hz), but bandwidth is not defined anywhere in this chapter; the text says chapter 4.3 introduces it, so a student meeting the example first has no definition to use.
- ch 2 [low] exam traps, third trap: "The series formula Q = ω₀L/R is the reciprocal" invites the reading that Q_parallel = 1/Q_series for the same circuit; the two formulas use different resistances (parallel R versus coil/series r).
- ch 2 [low] section 3, fourth bullet: For the practical coil tank the bullet says the coil and capacitor currents are "each about Q times I_s", but this chapter never defines Q for the practical tank, so the symbol is undefined at that point.
- ch 2 [low] quiz Q7: "The phase relation between the two branch currents" is ambiguous after the question mentions the supply current and the inductor current; the answer only addresses I_L versus I_C.
- ch 3 [high] Section 1, energy definition paragraph: The sentence says the inductor and capacitor exchange energy at f₀. The stored energies in L and C vary at twice the resonant frequency; the current and voltage vary at f₀. A student can take the energy-exchange frequency to be f₀.
- ch 3 [low] Section 2, half-power paragraph: V₀ is used in “V₀/√2” without being defined. The chapter defines I₀ but not V₀.
- ch 3 [low] Section 2, after the exact half-power formula: The exact half-power frequencies are not exactly evenly spaced around f₀; they are symmetric about f₀√(1 + 1/(4Q²)). Even spacing around f₀ is only the high-Q approximation.
- ch 3 [low] Quiz Q7: Calling the Q = 8 approximation “poor” is misleading. Q = 8 is outside the stated Q ≥ 10 range, but the numerical error is small; the real point is that the approximation is not guaranteed by the stated rule.
- ch 4 [low] Figure caption and x-axis label: The symbol ω₀ is used twice with two different meanings. For the RC curves ω₀ = 1/RC, but for the RLC curve ω₀ = 1/√(LC) (resonance). A student reading 'ω = ω₀ = 1/RC' next to 'the band-pass peaks at ω/ω₀ = 1' can conclude that the RC cutoff and the RLC resonance are the same physical frequency in the same circuit.
- ch 4 [low] Figure spec, RLC band-pass series: The sample points for the Q = 5 band-pass skip x = 1. The largest point shown is 0.9458 at x = 0.96625, and the next is 0.757 at x = 1.09, so the plotted curve peaks near 0.95 instead of the correct 1.0 at resonance.
- ch 4 [low] Section 2, last sentence after the 0.995 / 0.0995 values: 'These two numbers show the slow first-order rise and the fast approach to 1' pairs the numbers in the wrong order (0.995 is at 10 f_c, 0.0995 is at 0.1 f_c) and does not say which number shows which behaviour.
- ch 6 [low] Figure spec (aria text): The aria description says "A changing current i₁ = 2 A/s in coil 1", which gives a current value in A/s. A screen-reader user hears a current measured in ampere-per-second, contradicting the node note di₁/dt = 2 A/s.
- ch 6 [low] Exam traps, fourth bullet: The trap writes the mutual voltage as "e = M di/dt" without the minus sign, while Section 2 defines e₂ = −M di₁/dt. A student may copy the unsigned form as the full law rather than the magnitude.
- ch 7 [high] Section 2, series opposing paragraph: It says "one mutual term is negative" when the series current enters one dot and leaves the other. With one series current the sign of both mutual terms flips: for coil 1, i₂ enters an undotted terminal, so v₁ = L₁di/dt − M di/dt; for coil 2, i₂ also enters an undotted terminal, so v₂ = −M di/dt + L₂di/dt. A student who carries "one negative" into the two-equation form will get the wrong sign.
- ch 7 [low] Section 1, second paragraph: "Some syllabi call this dot conversion; the standard name is the dot convention." The sentence is attached to the sign flip, but dot conversion (or dot shifting) normally means moving a dot to the other terminal and adjusting the sign. As written, the two ideas get mixed and a student may think flipping the sign and moving a dot are the same operation.
- ch 7 [low] Section 1, formula box: v₁ and v₂ are called "the voltages at the dotted terminals", but a terminal voltage needs a reference. The KVL equations only hold when each voltage is measured from the dotted terminal to the undotted terminal of the same coil.
- ch 7 [low] Section 3, last sentence: "At k = 1 with equal coils, the aiding formula is read as a limit and stays finite" stops short of the value. For L₁ = L₂ = L and M = kL, the aiding fraction is L²(1 − k²)/[2L(1 − k)], which tends to L(1 + k)/2 and gives L at k = 1.
- ch 7 [low] Section 1, end of formula box: The sentence "If a current enters an undotted terminal, the sign of its M term becomes negative" repeats the prose sentence just above the box, so the same point is made twice in two lines.
- ch 8 [low] Exam traps, trap 2: The trap says "Impedance scales as n², not n" but then gives Z_in = (N₁/N₂)²Z_L, which equals Z_L/n² because n = N₂/N₁. The two statements are about opposite directions (primary-to-secondary versus secondary-to-primary reflection), and the student is not told this, so the bullet appears to contradict its own formula.
- ch 8 [low] Section 1 and Section 2: The reference direction of I₂ is defined oppositely in the two sections: in Section 1 I₂ leaves the dotted secondary terminal, in Section 2 I₂ enters the dotted secondary terminal. Each definition is correct on its own, but a student moving from the ideal ratios to the mesh equations can carry the wrong sign.
- ch 8 [low] Section 2, first sentence: The symbol ω is defined inside the sentence that defines M ("Define M = k√(L₁L₂), where k is the coefficient of coupling and ω is the angular frequency in rad/s"), although ω does not appear in that expression. It reads as if ω belonged to the definition of M.
- ch 9 [low] Section 1 (H definition): H = NI/l is presented as a plain definition of field strength. It is only true for a uniform path. In this same chapter the worked example has an iron core plus an air gap, where H is different in the iron and in the air, so a student may wrongly compute H = 1000/0.401 = 2494 A/m for the whole circuit.
- ch 9 [low] Section 1, last line: The forward reference 'treated in 4.5' is plain text, so the reader gets no clickable link to that chapter, unlike the linked cross-references used elsewhere in the book.
- ch 9 [low] Section 1, first sentence: 'A coil on a core is a source of magnetic pressure' introduces a non-standard term (magnetic pressure) that is never defined and is not used again; it can be mistaken for a real quantity.
