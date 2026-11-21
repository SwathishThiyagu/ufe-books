# ch-thermo-u2: free-model run

- Book: `books/chem/ch-thermo/ch-thermo-u2.html`
- Status: error
- Model calls so far: 24 (102,177 tokens in, 193,748 out), 7.9 minutes

## For the reviewer

- chapter 1: the figure cannot be drawn: series name "isobar" is too long; shorten it
- chapter 1: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 4, compressibility factor sentence: The sentence reads "Z = 1 for an ideal gas, Z  1 when their size pushes them apart". The inequality sign is missing, so the sentence cannot be read, and the case Z < 1 (attraction dominating) is never stated. A student cannot tell which side of 1 means attraction and which means repulsion.
- ch 1 [high] Worked example 1, step 1: The saturation temperature of water at exactly 1 bar (100 kPa) is 99.6 °C, not 99.97 °C. The value 99.97 °C belongs to about 1 atm. The step also calls 1 bar the "normal boiling pressure", but the normal boiling point is defined at 1 atm = 1.01325 bar, where water boils at 100.0 °C.
- ch 1 [low] Section 3, phase rule formula: The symbol P is used for pressure throughout the chapter and then reused for the number of phases in F = C − P + 2 = 3 − P. A student skimming the formula can read it as "3 minus pressure".
- ch 1 [low] Exam traps, first trap: The trap mixes the two diagrams. On a P–T diagram a point on the vaporisation curve is a two-phase state (saturated liquid and saturated vapour together), not "saturated liquid or saturated vapour". The wording "inside the dome two phases coexist" only applies to the P–V diagram.
- ch 1 [low] Quiz Q5: "A rigid vessel" fixes the total volume, so within that vessel P and T cannot be varied independently. The answer then says both P and T are free (F = 2), which reads as a contradiction. The degrees of freedom are a property of the pure fluid, not of the container.
- ch 1 [low] Figure: The pressure axis is linear from 0 to 250 bar, so the triple point (0.006 bar) and the whole low-pressure part of the vaporisation curve sit on the y-axis and are invisible. The figure does not show the steep shape of the curve or where the 1 bar line crosses it.
- ch 2 [high] Worked example 1, step 5: The explanation says the adiabatic final pressure is higher because 'the gas also cools'. This is a compression, so the gas is heated by the work done on it, not cooled. Here T₂ = 300 × 2^0.4 ≈ 396 K, above 300 K. A student will carry away the wrong physics: cooling lowers pressure at fixed volume.
- ch 2 [low] Section 2 paragraph after the table, and the table polytropic row ('PVk fixed', 'PVγ', 'TVγ−1', 'TP(1−γ)/γ'): The exponents are written without superscripts. 'PVk' can be read as P × V × k, and 'TP(1−γ)/γ' reads as T × P × (1−γ)/γ, which is a different (wrong) expression. The book already uses <sub>/<sup> elsewhere, so the notation is inconsistent.
- ch 2 [low] Quiz Q6: The question wording is tangled: 'A student uses Q = ΔU + W with W on the gas positive, then writes W = PΔV for an expansion. What sign error follows if the text uses W by gas positive?' Two conventions are named in one sentence and the answer only says 'reverses the sign', so a student cannot see which quantity ends up wrong or by how much.
- ch 2 [low] Section 2 ('is in Unit 1') and Section 3 ('Chapter 2.4', 'Chapter 2.3', 'Unit 5'): Cross-references to other chapters and units are given as plain text, so on a phone the reader cannot jump to them; the links convention used by the rest of the book is missing.
- ch 3 [high] Section 3, sentence on Redlich-Kwong: The attraction term is written a/[T0.5V(V + b)]. Read as printed, 'T0.5' means T × 0.5, so the student divides by half the temperature instead of the square root of the temperature. The value then differs by a factor of 2 and the RK term is wrong.
- ch 3 [low] Figure caption and aria text: Molar volume is quoted as 'V = 1 L', but V here is molar volume; the unit must be L/mol. The same slip appears in the aria description ('at 1 L'). The data points themselves are at 1 L/mol.
- ch 3 [low] Section 2, critical-point conditions: '(∂P/∂V) at Tc = 0 and (∂²P/∂V²) at Tc = 0' can be misread as differentiating with respect to Tc, or as conditions holding anywhere on the Tc isotherm. Both derivatives are zero only at one point: T = Tc, P = Pc, V = Vc.
- ch 3 [low] Quiz Q6 answer: The answer says the gas is 'dense' and 'near saturation' at 0.5 L/mol. With the chapter's own numbers the van der Waals pressure there is about 40 bar, giving Z = PV/RT ≈ 0.80: a moderately non-ideal superheated vapour, not a near-saturated dense fluid. The stated reason overstates the case.
- ch 3 [low] Section 2, formula glossary: Every symbol in the van der Waals formula is given with units except R ('R is the gas constant'), although the trap list later depends on knowing which R matches which units.
- ch 4 [low] Figure caption: The caption and node f state 'at Tr = 1.2 and Pr = 2.0 read Z = 0.65, then V = 0.195 L/mol', which suggests V follows from Tr and Pr alone. The number 0.195 L/mol only holds for the specific gas and conditions of Worked example 1 (Tc = 300 K, Pc = 50 bar, T = 360 K, P = 100 bar). A student could try to reproduce it from the chart path and fail.
- ch 4 [low] Quiz Q7 answer: The percent excess is computed from rounded volumes (0.299 and 0.195 L/mol) and reported as 53.3%. Using the unrounded values gives (0.29930 − 0.19455)/0.19455 × 100 = 53.8%. The two answers differ in the first decimal place, and a student checking with a calculator will get a different number.
- ch 4 [low] Section 3, mixture formula: The Kay's-rule formula is introduced with no name and no warning that it is only an approximation. Ppc = Σ yi Pc,i in particular can be poor when the components differ greatly in size or polarity, and students may apply it blindly to a natural-gas mixture containing CO2 or H2S.
- ch 5 [low] Figure and its caption: On an H against T plot the latent-heat portions are vertical jumps at fixed temperature, but the caption calls them 'flat steps', which describes a T against Q plot. A student matching the caption to the drawing may look for a horizontal line that is not there.
- ch 5 [low] Figure, y-axis and first point: The enthalpy scale starts at 0 for ice at −10 °C, but the figure never says that H is measured relative to that state, so the absolute-looking numbers (354.9, 3032.9) can be misread as steam-table enthalpies.
- ch 5 [low] Section 1, first formula: Q = ∫ n Cp dT is written without limits, while the text then talks about 'the range'.
- ch 5 [low] Section 3, definition of standard heat of formation: The definition gives the pressure (1 bar) but not the temperature at which ΔH°f values are tabulated, which is needed before a student can use a data table correctly.
- ch 5 [low] Lead: 'wrong by a factor of five' is an unsupported number; depending on which term is dropped the error can be far smaller or larger.
