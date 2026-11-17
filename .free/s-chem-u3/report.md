# s-chem-u3: free-model run

- Book: `books/common/s-chem/s-chem-u3.html`
- Status: ok
- Model calls so far: 24 (80,166 tokens in, 165,550 out), 5.0 minutes

## Checker

```
s-chem-u3.html: 6 chapters, 9599 words, 7 figures, 110 KB
OK
```

## For the reviewer

- chapter 6: the figure cannot be drawn: series name "PbL" is too long; shorten it
- chapter 6: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, first line after ΔG = ΔH − TΔS: The comparison sign has dropped out: the text reads "ΔG  0 means the forward reaction does not go; the reverse does." With no symbol, a student cannot tell which sign is being described. The criterion for the spontaneous case (ΔG < 0) is also missing entirely.
- ch 1 [high] Section 4, Nernst equation line: The value of RT/F at 298 K is not 0.0592 V. RT/F = 8.314 × 298 ÷ 96500 = 0.0257 V. The factor 0.0592 V is 2.303RT/F, i.e. the value after converting ln to log₁₀.
- ch 1 [low] Section 3: The chapter gives ΔG < 0 and ΔG > 0 but never states the equilibrium condition, so the link between ΔG and K = 1 is left implicit.
- ch 1 [low] Section 1, heat capacity sentence: "Heat capacity is C = q/ΔT, in J K⁻¹" does not say which heat capacity it is, and most reactions here are at constant pressure, where the useful quantity is C_p.
- ch 2 [high] Section 2, first-order integrated law: The exponential is written as "[A] = [A]₀ e−kt", with no superscript. Read literally this is e minus k·t, which is not the integrated rate law and will mislead a student reading on a phone.
- ch 2 [low] Section 1, rate definition: "Instantaneous rate is the slope of the concentration-time graph at one instant." For a reactant that slope is negative, yet the rate was just defined with a minus sign to make it positive; the two statements contradict each other as written.
- ch 2 [low] Section 1, molecularity paragraph: "Some syllabi call order reaction order and molecularity elementary molecularity" is a tautology and adds no information; the second half is not a standard usage and confuses students.
- ch 2 [low] Section 1, molecularity definition: "Molecularity is the number of species colliding in one elementary step" is loose: a unimolecular step has molecularity 1 and involves no collision at all.
- ch 2 [low] Section 3, finding order: Only the method of initial rates is given. Exam questions also ask for order from concentration-time data, and the chapter never says how to get it, even though the three integrated laws are already stated in Section 2.
- ch 3 [low] Section 3, table row 'Favoured at': The table says thermodynamic product C is favoured at 'high temperature'. High temperature only makes interconversion fast; thermodynamic control needs the products to be able to equilibrate, which can also come from long time or a catalyst. A student may read this as 'heat alone always gives C', even when B and C cannot interconvert.
- ch 3 [low] Quiz Q6: The premise 'a catalyst lowers only the barrier to B' conflicts with the answer 'the equilibrium constant is unchanged'. A catalyst lowers the barrier of the forward and the reverse step of the same route; if only A→B were lowered and not B→A, the equilibrium constant would change, which is impossible.
- ch 3 [low] Exam traps, fourth bullet: 'Overall order ... can be zero, fractional, or negative' overstates the negative case. Negative orders are normally quoted for the order with respect to one species (for example, an inhibiting reactant), not for the overall order.
- ch 3 [low] Exam traps, second bullet: The double negative 'The kinetic product is not always impossible to isolate' is hard to parse for a reader with English as a second language.
- ch 3 [low] Quiz Q1: The answer says the kinetic product forms faster 'because its route has the lower activation energy'. Speed depends on both Ea and the pre-exponential factor A, so the lower Ea guarantees the faster route only when the A factors are comparable, as the worked example itself assumes.
- ch 3 [low] Section 1, first paragraph: The cross-reference 'as in 3.2' is plain text, so a phone reader cannot tap through to the order-of-reaction chapter.
- ch 4 [low] Figure: The figure shows the C branch as only S and −R, and the caption says every reaction takes one away from C. Section 3 defines C = S − R − a, including the electroneutrality restriction a, so the figure contradicts the text for ionic systems such as water.
- ch 4 [low] Section 2 and Worked example 1: Section 2 fixes the pressure at 1 atm, while the worked example fixes it at 1 bar. A student may read these as the same number; they differ by about 1.3%.
- ch 5 [high] Figure spec — 'fus' series: The plotted fusion curve goes (273.16 K, 0.611 kPa) → (273.17 K, 5000 kPa) → (273.2 K, 22000 kPa). Temperature rises as pressure rises, so the curve leans right. This contradicts the section text ('the fusion curve of water leans left'), the exam trap, the quiz answer and the figure's own aria description. The numbers are also wrong in size: with dp/dT ≈ −13.6 MPa/K, the melting point at 5 MPa is about 272.8 K and at 22 MPa about 271.5 K.
- ch 5 [low] Lead and Section 1: The sentence 'Only a few universities teach this full diagram' appears twice, once in the lead and again at the end of the first paragraph of Section 1. Repeating it reads as filler and wastes phone-screen space.
- ch 6 [low] Section 1 and Exam trap 5: F is defined as the number of intensive variables you can change 'without losing a phase', and the trap repeats the same phrase. Changing T or composition normally changes the phase compositions, not the number of phases, so the phrase is misleading.
- ch 6 [low] Section 2, lever-rule paragraph: The sentence 'A tie line at 303 °C joins the two solid compositions (pure Pb and pure Ag) and the liquid at 2.5% Ag' mixes a two-phase tie line with a three-phase isotherm. At 303 °C three phases coexist, so a single tie line through solid Pb, liquid and solid Ag does not exist and the lever rule cannot be applied across all three points at once.
- ch 6 [low] Quiz Q5: 350 °C is very close to the liquidus temperature of a 5% Ag alloy (the straight liquidus in the figure gives about 320 °C, but the real Ag-side liquidus is curved upward), so the answer 'all liquid, P = 1, F = 2' is ambiguous and a student could reasonably answer two phases, F = 1.
- ch 6 [low] Quiz Q6: The answer 'Three phases coexist; F = 0' is not the only cause of a flat halt. A pure component freezing (for example pure Pb at 327 °C) also gives a halt with only two phases, because for C = 1, P = 2 the reduced rule gives F = 1 − 2 + 1 = 0.
- ch 6 [low] Section 3, compound formers: 'Zn–Mg is one example' names no compound and gives no melting behaviour, so the student cannot connect the example to the 'peak at the compound's composition' idea.
