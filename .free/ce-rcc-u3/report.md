# ce-rcc-u3: free-model run

- Book: `books/civil/ce-rcc/ce-rcc-u3.html`
- Status: ok
- Model calls so far: 23 (80,125 tokens in, 222,769 out), 6.4 minutes

## Checker

```
ce-rcc-u3.html: 7 chapters, 19982 words, 9 figures, 201 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, principal stress formula: The formula σ₁ = σ/2 + √((σ/2)² + τ²) is written with σ defined as positive in compression, but that expression is the largest principal stress in the compressive sense, not the principal tensile stress. With compression positive, the tensile principal stress is −σ/2 + √((σ/2)² + τ²). As printed, a student applying it to the compression zone gets a tension far above the real value.
- ch 1 [high] Section 3, sentence 'Three checks follow': The second check is broken: 'If τ_c  τ_c,max, enlarge the section' has no comparison operator, and the middle case (stirrups needed) is missing although three checks are announced. A reader cannot tell which limit triggers which action.
- ch 1 [high] Section 2, stirrup effectiveness paragraph: The mechanics are stated backwards: 'a vertical stirrup meets a 45° crack at 45°, so it carries only the component along its own axis, about 0.707 T'. The stirrup tension T is already along its own axis; the useful part is the component across (perpendicular to) the crack, T sin 45° ≈ 0.707 T.
- ch 1 [low] Worked example, step 7: The arithmetic shown does not reproduce the stated answer: (1.09 − 0.62) × 165,000 = 77,550 N, not 77,700 N. The printed 77,700 N comes from the unrounded τ_v = 1.0909 MPa, which is not what step 7 displays.
- ch 1 [low] Section 3, 'For M25 with the steel of the example below, τ_c = 0.62 MPa': The worked example never gives the tension steel area A_st or the percentage p_t, so the reader cannot check or reproduce τ_c = 0.62 MPa from IS 456 Table 19 as claimed.
- ch 1 [low] Section 3 and Worked example, symbol V_us: V_us appears in step 7 and in the answer without ever being defined, and it is not in the symbol list under the τ_v formula.
- ch 2 [low] Section 1, paragraph 3: The sentence on the 'two strengths' is confusing. It says the second strength is 'τc plus the steel term', but IS 456's second tabulated strength is τc,max, and many books call τc,max the design shear strength of concrete with shear reinforcement. A student can leave this paragraph thinking τc,max is the value to subtract when finding Vus, which the Exam traps later warn against.
- ch 2 [low] Section 3, bent-up bars bullet: α appears in 0.87 fy Asv sin α without being defined. The reader cannot tell it is the angle of the bent-up bar to the beam axis, and sin α is dimensionless so the term is in N only if fy is in MPa and Asv in mm².
- ch 2 [low] Worked example 1, data line: τc = 0.62 MPa is stated as data but the tension steel percentage it corresponds to is not given. Table 19 makes τc depend on both grade and pt, so a reader who assumes a small pt for M25 will look up something near 0.49 MPa and think 0.62 MPa is wrong.
- ch 2 [low] Worked example 1, after step 8: The step list in Section 2 asks for a minimum-steel check as well as the maximum-spacing check, but the example checks only the maximum spacing. The minimum-steel limit is the one that actually governs here and its omission teaches the wrong habit.
- ch 3 [high] Figure and its caption: The figure shows T_u = 30 kN·m directly becoming V_e = 280 kN. But 1.6T_u/b gives only 160 kN for b = 300 mm. The 280 kN also includes V_u = 120 kN from the worked example. A student will think torque alone produces 280 kN.
- ch 3 [high] Section 1, first paragraph: It calls a plain rectangle an 'open section'. In torsion, an open section means a thin-walled open section such as an I-section or channel. A solid rectangle is a closed section and is much stiffer in torsion.
- ch 3 [high] Worked example 1, step 4: It writes τve = 280 × 103 / (300 × 550) = 1.70 N/mm². Read literally, 280 × 103 gives 0.175 N/mm², not 1.70. The numerator must be 280 × 10³.
- ch 3 [low] Quiz Q1 answer: The question asks to define every symbol, but the answer only gives the formulas and units. It does not define V_u, T_u, b, D and M_t.
- ch 3 [low] Section 3: It gives the spacing formula for closed stirrups but omits the IS 456 limit on maximum spacing for torsion stirrups. A student may design a spacing that satisfies strength but violates the code detailing limit.
- ch 3 [low] Worked example 1, step 4: It says to compare τve with τc,max for the chosen concrete grade, but no concrete grade is stated in the example. The check cannot be completed as written.
- ch 4 [low] Worked example 1, answer line: The final answer reads "τve c,max = 3.1 MPa", which is garbled and can be read as a single quantity. The check result is what should be shown.
- ch 4 [low] Section 1, equivalent load formulas: b appears in both formulas with different units (mm in the Mt formula, m in the Ve formula), and Ve is defined in kN there but in N in the τve check two sentences later. A student can miss which unit to use in which formula.
- ch 4 [low] Section 2, first bullet: The bullet only tells the student to use b in metres for Ve. The Mt step that comes next needs b in millimetres, so the instruction is incomplete at the point where it is needed.
- ch 4 [low] Section 2, stirrup design bullet: It says to design closed stirrups for Ve but does not say that, as in ordinary shear design, the concrete contribution τc·b·d is first deducted from Ve to get the steel shear Vus. A student may design stirrups for the whole of Ve.
- ch 4 [low] Section 1 or Section 2, torsion threshold: The chapter never mentions that IS 456 permits torsion arising from compatibility in statically indeterminate members to be ignored when the factored torque is below a small threshold. Students then apply the equivalent-load machinery to every small torsional moment.
- ch 5 [high] Section 1: It states that for M25 concrete and deformed bars in tension τ_bd = 1.4 N/mm². In IS 456, 1.4 N/mm² is the plain-bar value for M25; the deformed-bar value is 1.4 × 1.6 = 2.24 N/mm².
- ch 5 [high] Worked example 1: The example uses τ_bd = 1.4 N/mm² for a 16 mm Fe415 deformed bar in M25 concrete. That is the plain-bar value, so L_d = 1032 mm is too long by a factor of 1.6.
- ch 5 [high] Figure: The plot expression 64.4732*x and the marked point (16 mm, 1031.6 mm) are based on τ_bd = 1.4 N/mm², so the figure represents plain bars, not the deformed bar in the worked example.
- ch 5 [high] Quiz Q2: The answer 1.4 N/mm² is the IS 456 plain-bar design bond stress for M25. The question asks for deformed bars in tension, for which the value is higher.
- ch 5 [high] Quiz Q4: The question gives τ_bd = 1.5 N/mm² for M30 deformed bars. That is the M30 plain-bar value; the deformed-bar value is 2.4 N/mm². The arithmetic 1450 mm is correct only for the assumed 1.5 N/mm².
- ch 5 [low] Section 2: The sentence says two 12 mm bars of the same total area as one 20 mm bar have more surface. Their areas are not equal: two 12 mm bars give 226.2 mm², while one 20 mm bar gives 314.2 mm².
- ch 6 [high] Section 1 and Exam traps: The chapter says to use the smaller bar when diameters differ, and the exam traps call using the larger diameter a mistake. This is reversed: lap length is governed by the larger diameter (the greater development length), and the 30φ minimum also uses the larger φ.
- ch 6 [low] Section 1 (compression lap): The compression lap code minimum is not stated; 'meets its code minimum' leaves students without the value. IS 456 gives 24φ, not the tension minimum 30φ.
- ch 6 [low] Section 2 and Worked example 1: The extension beyond the theoretical cut-off is given as Ld only. IS 456 also requires at least 12φ, so the extension should be max(Ld, 12φ).
- ch 7 [high] Quiz Q7: The situation and the answer contradict each other and contradict the chapter's own spacing formula. If stirrups are moved inward, the space inside them shrinks, so clear spacing between main bars decreases, not 'improves'; and the cover to the stirrup outside increases, so 'cover fails first' does not follow. A student cannot tell which check actually fails.
- ch 7 [low] Figure and Worked example 1, given data: Section 1 defines the cover to the outside of the stirrup as nominal cover, and exam trap 1 repeats this. The figure labels that same 25 mm as 'Clear cover', and example 1 calls it '25 mm clear cover to the outside of the stirrup'. The same quantity is given two different names, so a student cannot tell which definition to use.
- ch 7 [low] Section 1, two layers of bars: 'Use the same idea vertically when bars are in two layers' suggests the horizontal minimum applies vertically. For bars in two layers the code minimum vertical clear gap is smaller: the greater of 15 mm and the nominal maximum size of coarse aggregate, not aggregate + 5 mm.
