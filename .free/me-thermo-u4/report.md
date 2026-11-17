# me-thermo-u4: free-model run

- Book: `books/mech/me-thermo/me-thermo-u4.html`
- Status: ok
- Model calls so far: 22 (91,274 tokens in, 190,114 out), 5.9 minutes

## Checker

```
me-thermo-u4.html: 5 chapters, 10565 words, 6 figures, 112 KB
OK
```

## For the reviewer

- checker: text contains "TODO"

## Reviewer notes (after any revision)

- ch 1 [low] Section 1 (Dead state first): The dead state is defined only by T₀ and p₀. The standard definition also requires the system to be at rest (zero velocity, at datum elevation) and in chemical equilibrium with the environment. Without that, a student may think a moving or chemically reacting system at T₀, p₀ already has zero availability.
- ch 1 [low] Section 3 (Availability is not a property): Many syllabi define a single-state 'availability function' U + p₀V − T₀S, which <i>is</i> a property of the system at fixed T₀ and p₀. Saying flatly 'availability is not a property' can collide with that usage.
- ch 1 [low] Quiz Q3: The question sets T₀ΔS against 'just Q/T', but Q/T is entropy (kJ/K), not energy (kJ), so the two are not comparable quantities and a student may read the question as a unit slip.
- ch 1 [low] Beyond: Chemical exergy is presented as something 'researchers extend the idea to'. It is standard textbook material with tabulated standard chemical exergies and is examined in many syllabi.
- ch 2 [high] Section 3 (last paragraph) and Quiz Q5: The claim that a turbine can have a high isentropic efficiency and a lower second-law efficiency is wrong for an adiabatic turbine whose whole expansion stays above T0. There the entropy generated is produced at temperatures above T0, so T0·S_gen is smaller than the isentropic lost work (h1 − h2s) − (h1 − h2). Hence w + T0·S_gen < h1 − h2s and η_II = w/(w + T0·S_gen) comes out greater than η_is = w/(h1 − h2s). Example: air expanding from 1500 K, 10 bar to 1 bar with η_is = 0.90 gives S_gen ≈ 0.09 kJ/kg·K, T0·S_gen ≈ 27 kJ/kg against w ≈ 651 kJ/kg, so η_II ≈ 0.96, not lower. Q5's pair (η_is = 0.90, η_II = 0.80) is therefore not achievable in a normal turbine, and its answer 'Yes' teaches a reversed ordering.
- ch 2 [low] Section 1, sentence after the first formula: 'For a closed system of mass m, the specific exergy is Φ' says nothing new and does not use m. The specific exergy is Φ whatever the mass; what depends on m is the total exergy.
- ch 2 [low] Section 2, formula boxes and following text: The first box gives I in 'kJ or kW' while the text two lines later fixes I in kJ/kg for a unit mass, and the second box does not say which. A student copying units into an exam can mix total, rate and specific forms.
- ch 3 [high] Exam traps, fourth trap: The units are given wrongly: s is in kJ/(kg·K) but u and h are in kJ/kg, not kJ/kg K. Writing 'use s, u, h in kJ/kg K' tells students that enthalpy and internal energy carry a per-kelvin unit, which is false and will cost marks in the exam.
- ch 3 [low] Worked example 1, step 6: 'Both functions are unchanged, as they must be' overstates the case. At a phase change at equilibrium temperature and pressure only ΔG is exactly zero; in general ΔA = −pΔV at constant T and p, so it is zero here only because the volume change of freezing water is negligible.
- ch 3 [low] Section 3, last paragraph of the bullet list: A turbine shaft is not a constant-temperature, constant-pressure device; a real turbine is adiabatic and its shaft work is bounded by the change in availability (exergy), not by −ΔG. Listing it next to a battery and a fuel cell may confuse the condition under which −ΔG is the bound.
- ch 4 [low] Worked example 2, step 5: The sentence 'A gas at the hot end of the bracket gets no temperature change on throttling' is garbled — 'hot end of the bracket' has no meaning, and a student will stall on it.
- ch 4 [low] Section 3, van der Waals result: Unit conflict: the earlier formula declares μJK in K/kPa with cp in kJ/(kg·K), but the van der Waals form uses cp in J/(mol·K) with a and b per mole. With those units the bracket is in m³/mol, so the result comes out in K/Pa, not K/kPa — a factor of 1000. The formula also does not state the value of R to use.
- ch 4 [low] Exam traps, wrong subscript bullet: '(∂s/∂p)h is a different quantity used in throttling' is misleading: throttling is constant enthalpy but the coefficient used there is (∂T/∂p)h, not (∂s/∂p)h.
- ch 5 [high] Section 3, melting line of water: The symbol and unit are wrong. The temperature drop per atmosphere is dT/dp ≈ −0.0074 K per atmosphere, not dp/dT. dp/dT itself is the slope in Pa/K and is about −1.3 × 10⁷ Pa/K for ice-water, so a student who reads '−0.0074 K per atmosphere' as a value of dp/dT gets the quantity and its units confused.
- ch 5 [low] Section 2, after the Clausius-Clapeyron form: 'Plot ln p against 1/T for a liquid and you get a straight line' is stated too strongly; the chapter has just said h_fg is only 'nearly constant for a short range'. Over a wide band the plot is a gentle curve.
- ch 5 [low] Figure caption and aria: The point 13.3 kPa at 323 K is the model's own prediction, not an input or a measured data point, and the plotted curve passes through it by construction. A student reading the figure sees perfect agreement, which contradicts the worked example saying the estimate is about 8 per cent above the steam-table value of about 12.3 kPa.
- ch 5 [low] Quiz Q8 answer: 'The saturation curve meets the critical isotherm with a finite slope' is unclear. On a p-T diagram the critical isotherm is the vertical line T = T_c and is not something the curve meets with a slope; the intended point is simply that the slope stays finite at the critical point.
- ch 5 [low] Lead and Section 3, skate blade example: Pressure melting is now considered only a minor part of why a skate glides; friction and the natural liquid-like surface layer of ice do most of the work, and pressure alone lowers the melting point by well under a kelvin. The claim in the lead is a simplification presented as fact.
