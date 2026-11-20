# me-thermo-u2: free-model run

- Book: `books/mech/me-thermo/me-thermo-u2.html`
- Status: ok
- Model calls so far: 20 (75,536 tokens in, 163,914 out), 3.3 minutes

## Checker

```
me-thermo-u2.html: 7 chapters, 12892 words, 8 figures, 130 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1 (process form of the first law): The chapter states the closed-system first law only as Q₁₂ − W₁₂ = U₂ − U₁. The general textbook form also carries the changes of kinetic and potential energy of the system as a whole: Q − W = ΔU + ΔKE + ΔPE. A student meeting a moving piston or a falling mass problem can wrongly apply the shorter form.
- ch 1 [low] Section 3, paragraph on path dependence: "Two different paths between the same states enclose different areas" is misleading. A given pair of paths encloses one fixed area; what differs is the area under each curve. Only the difference of those two areas, W_A − W_B, is the enclosed area.
- ch 1 [low] Beyond (not for the exam): Two loose claims. CFD codes solve the differential conservation equations (mass, momentum, energy) over each control volume; they do not solve δQ − δW = dU cell by cell. A battery pack's heat out equals electrical work in only when its stored internal energy is unchanged.
- ch 2 [low] Section 3 table, row 'Steady-flow device, no shaft work': The row states q = Δh for any steady-flow device with no shaft work. That is only true when changes in kinetic and potential energy are negligible, as in a heat exchanger. For a nozzle or diffuser there is no shaft work, yet q = 0 while Δh = −Δke ≠ 0, so a student could apply q = Δh to a nozzle and get a wrong answer. The text in Section 2 correctly limits this to a heat exchanger, but the table generalizes it.
- ch 2 [low] Section 1, first paragraph of the text block: The sentence 'once pressure, temperature and phase are fixed, U is fixed' is imprecise. Pressure and temperature are not independent inside a two-phase region: at a given p and T a wet mixture can have any quality, so U is not fixed. Mentioning 'phase' does not repair this, because 'two-phase' is itself the phase.
- ch 3 [low] Figure (aria text): The aria says the difference between the two heats is R. Heats have units of kJ, while R is a specific-heat difference in kJ/kg·K; for 1 kg the heats differ by RΔT, and only when ΔT = 1 K does the number equal R. A screen-reader user gets a dimensionally wrong statement.
- ch 3 [low] Beyond: 'Real gases have cp and cv that change with temperature' suggests that temperature dependence is a real-gas effect, which contradicts Section 2 ('At high temperature cp rises' for an ideal gas). For real gases the extra feature is pressure dependence and departure from cp − cv = R.
- ch 4 [low] Section 3, sentence after the adiabatic work formula: The sentence reads "In compression W  0 and T rises." The comparison sign is missing, so the statement is unreadable and could be taken either way.
- ch 4 [low] Beyond paragraph: Polytropic efficiency is said to compare a real compressor with a reversible adiabatic one. That describes isentropic (adiabatic) efficiency; polytropic efficiency is the isentropic efficiency of an infinitesimal stage and does not depend on pressure ratio.
- ch 4 [low] Lead: Gas pipelines are flow systems, but this chapter is about non-flow (closed-system) paths; the mention can confuse a reader who then tries to apply the closed-system formulas to a pipeline.
- ch 5 [high] Section 2, second paragraph: 'Compute Qnet and Wnet. If they differ, the difference is created or destroyed energy, so declare the claim impossible. The machine is PMM-1.' This would make a student reject a perfectly legal engine. A real engine always has Wnet = Qnet because Qnet = Qin − Qout; a claim of Qin = 300 kW with W = 200 kW is normal (100 kW is rejected), not a first-law violation. Only Wnet greater than Qin (energy created) is PMM-1.
- ch 5 [high] Section 2, first paragraph: 'A claim of 125 percent means 25 percent of output is created, not converted' is numerically wrong. With Qin = 100 kJ and Wnet = 125 kJ, the created 25 kJ is 25 percent of the input but only 20 percent of the output (25/125).
- ch 5 [low] Section 1, Form 2: 'Gives more net work than its net heat input' is imprecise. Net heat input means Qin − Qout, and no cycle can have Wnet greater than that. The PMM-1 claim is that work exceeds the heat supplied, Qin.
- ch 5 [low] Lead: 'Only a few universities teach PMM-1 as a named topic' is inaccurate. PMM-1 is a standard named topic in most engineering thermodynamics syllabi, usually next to the first-law statement and the Kelvin–Planck statement.
- ch 5 [low] Section 1, Form 2: The symbol η is used ('so η > 1') before it is defined. The definition only arrives in Section 2.
- ch 6 [high] Worked example 1: The turbine is called 'insulated' in the very first line, yet the problem then gives a casing heat loss of 20 kJ per kg and uses q = −20 kJ/kg in the solution. The two statements contradict each other, and a student cannot tell whether q = 0 or q = −20.
- ch 6 [low] Worked example 1, step 3: The step writes V₁² − V₂² = −18900 'J/kg' and then divides by 2. The square of a velocity is not energy per kg; V²/2 is. Combined with the /2000 already inside the formula, the extra '÷2' reads like a second division and can confuse a student about where the 2000 comes from.
- ch 6 [low] Figure spec: The inlet and outlet notes read 'h₁ + V₁²/2 + gz₁' and 'h₂ + V₂²/2 + gz₂', which is in J/kg, while the equation in the text uses V²/2000 and gz/1000 so that every term is in kJ/kg. Two different unit systems in the same chapter.
- ch 6 [low] Section 3, heat exchanger: The relation ṁ_hot Δh_hot + ṁ_cold Δh_cold = 0 is only correct if Δh means h_out − h_in for each stream. Δh is not defined, and a student who reads Δh as 'enthalpy drop' gets the opposite sign.
- ch 6 [low] Section 3, throttle: 'Pressure falls and, for a real fluid, temperature falls too' overstates the rule. Most real gases cool on throttling at room temperature, but hydrogen and helium warm up, and any gas warms up if its Joule–Thomson coefficient is negative at that state.
- ch 7 [low] Section 3: The paragraph says 'For the cup in the worked example' before Worked example 1 appears, so the reader meets a forward reference and may not know which cup is meant.
- ch 7 [low] Section 2, fourth bullet: 'It can balance a state that never occurs on its own' is unclear: a state is not balanced; a process is.
- ch 7 [low] Section 3: 'In an isolated system, the entropy of an irreversible process increases' treats entropy as belonging to a process; entropy is a state property, and what increases is the entropy of the isolated system during an irreversible process.
- ch 7 [low] Section 3 and Worked example 1, step 6: 'would decrease entropy' and 'it would reduce entropy' do not say whose entropy. The cup's own entropy increases when it warms, so a student may think the statement is wrong.
- ch 7 [low] Section 2, fifth bullet: 'the same end states and the same energy balance' can be read as the same Q and W for both paths, which is false: the reversible and irreversible paths have different Q and W even though Q − W = ΔU holds for both.
- ch 7 [low] Section 2, PMM paragraph: 'See Chapter 2.5 for PMM-1' is plain text, not an internal chapter link in the book's style.

## Claude correction pass (20 Nov 2026)

- Packet on main has 8 chapters: new chapter 2.7 Unsteady flow processes (filling and emptying of vessels); the old chapter 7 (limitations) is now ch8.json.
- Every worked example and quiz answer recomputed; steam (3 MPa/350 °C, 20 kPa) and R-134a (800/200 kPa) values checked against property libraries.
- Fixed: path-area sentence, energy forms and Q − W = ΔE added, free-expansion work, PMM-1 tests, nozzle q ≠ Δh row, carets and underscores set as super/subscripts, cross-unit references named by topic.
- Wrong outlines fixed: closed-system adiabatic compression to the same pressure needs less boundary work than isothermal; free expansion T₂ = T₁ only for an ideal gas; refrigerant named (R-134a).
- Figures redrawn by hand (pipeline/claude_figs/me_thermo_u2.py); 15 long questions with full model answers (two new: tank filling, and the compressor-cooler-throttle chain now has numbers).
