# me-thermo-u3: free-model run

- Book: `books/mech/me-thermo/me-thermo-u3.html`
- Status: problems
- Model calls so far: 32 (130,863 tokens in, 272,603 out), 6.5 minutes

## Checker

```
me-thermo-u3.html: 9 chapters, 16162 words, 10 figures, 176 KB
PROBLEMS:
 - text contains "TODO"
```

## For the reviewer

- checker: text contains "TODO"

## Reviewer notes (after any revision)

- ch 1 [high] Worked example 1, steps 4–6: The reversed run keeps the same reservoirs at 600 K and 300 K. For a refrigerator between those two reservoirs the reversible limit is COP_R = T₂/(T₁ − T₂) = 300/(600 − 300) = 1. Steps 5–6 claim COP_R = 1.667 and COP_HP = 2.667 between the same reservoirs, which is above the second-law limit and therefore impossible. The forward engine is irreversible (0.375 against a Carnot value of 0.5), so reversing the same machine with unchanged magnitudes cannot give a Carnot-equal COP either.
- ch 1 [low] Quiz Q7, answer explanation: 'the rest of the heat comes from the room and is only moved uphill' reads as if part of the 5.28 kW cooling comes from the electricity. In fact all 5.28 kW is taken from the room; the 1.65 kW of work is added on top, so 6.93 kW is rejected outdoors.
- ch 2 [low] Figure (spec and caption), node 'free': The cold body node says 'loses 500 kJ' while the only edge into it is labelled 'removes 300 kJ'. The 200 kJ that the 100% engine itself draws from the same 300 K body never appears as an edge. A student tracing the diagram can conclude the cold body loses only 300 kJ and that the figure contradicts its own caption.
- ch 2 [low] Exam traps, trap 5 (COP = T₂/(T₁ − T₂)): The trap says putting T₁ on top gives 'an absurd answer'. For the chapter's own numbers, 500/200 = 2.5, which looks perfectly plausible to a student; it is not absurd, it is simply higher than the correct 1.5, which is the real tell.
- ch 2 [low] Section 1 ('See 3.1 for the picture') and Section 4 ('worked out in 3.4'): Both cross-references are plain text. On a phone the student cannot jump to the engine diagram or to the Carnot-efficiency chapter, which are needed to follow the two places that send them elsewhere.
- ch 2 [low] Section 3, second paragraph ('Assume a free refrigerator, break Kelvin-Planck'): 'Free refrigerator' is used before it is defined; the definition arrives only in the next sentence ('Suppose a device lifts Q₂ ... with no work'). The opening phrase reads as a slogan, not a statement of what is being assumed.
- ch 3 [high] Section 1, sentence after the two conditions: "Both must be absent before we call a process reversible" contradicts the two conditions just listed. The quasi-static condition is something that must be present; only the dissipative effects must be absent. Read literally, the sentence tells a student that a reversible process must not be quasi-static.
- ch 3 [low] Section 3, last sentence of the internal/external paragraph: "when a problem says reversible without qualification, it usually means internally reversible" goes against the standard definition, where reversible without qualification means totally reversible, i.e. both internally and externally reversible. A student may write this in an exam as the definition.
- ch 3 [low] Worked example 1, step 8: "...the whole 29.84 kJ that could have been exported is destroyed as ordered energy" suggests work was turned into heat. Free expansion of an ideal gas is adiabatic and the internal energy and temperature do not change, so no energy is destroyed; only the work potential is lost. The 29.84 kJ is the lost work, equal to T₀ times the entropy generated in the gas (300 × 0.5 × 0.287 × ln 2 ≈ 29.84 kJ).
- ch 4 [high] Section 2, adiabatic relations and the step 'Divide the first by the second': The two adiabatic relations are printed with their sides in opposite order: T₁V₂^(γ−1)=T₂V₃^(γ−1) and T₂V₄^(γ−1)=T₁V₁^(γ−1). Dividing the first equation by the second exactly as printed does not give V₂/V₁ = V₃/V₄. It gives T₁²V₁^(γ−1)V₂^(γ−1) = T₂²V₃^(γ−1)V₄^(γ−1), so a student who follows the instruction gets stuck or concludes the algebra is wrong. (From the printed pair the correct move is to multiply, not divide.)
- ch 5 [low] Exam traps, second bullet: The wording "Substituting 27 for 300 K" is garbled and reads as if 27 and 300 K were the same thing, which is close to the opposite of the intended point.
- ch 5 [low] Section 2, last paragraph: "Gas thermometer readings need no correction when they are treated as thermodynamic temperatures" is misleading for real gases: a real-gas reading has to be corrected by extrapolating to zero pressure before it equals the ideal-gas (and hence thermodynamic) value.
- ch 5 [low] Figure: The T₂ = 600 K series is evaluated from T₁ = 300 K, so the data contain negative efficiencies (down to −1) where the source is colder than the sink. A reversible engine has no meaningful efficiency there, and the curve should not exist in that range.
- ch 6 [low] Quiz Q5: The answer writes Q_H/T_H = Q_C/T_C, which ignores the chapter's own sign rule (heat in positive, heat out negative). With that rule the correct statement is Q_H/T_H − Q_C/T_C = 0, where Q_C is the magnitude rejected. A student who follows the trap about rejected heat being negative will get a sign clash with the answer shown.
- ch 6 [low] Section 3, last sentence: 'The zero case is not a small effect; it is the limit that real machines approach but never reach' is unclear. 'Not a small effect' suggests the zero case produces a physical effect, when the point is that reversibility is an idealising limit, not a small correction.
- ch 7 [high] Section 1, last sentence: The sentence breaks off: "The real path gives ∫δQ/T 3.8)." The comparison and the opening bracket of the cross-reference are missing, so no student can read what the real path gives. The section also never states the important result that the integral along an irreversible path is less than ΔS.
- ch 7 [high] Section 2, Slopes paragraph: The inequality is missing: "Since cv  T/cp, so the constant-volume line is steeper". As printed there is no relation between cv and cp, and the conclusion does not follow.
- ch 7 [high] Quiz Q4 answer: Same missing inequality: "Since cv  T/cp, so the constant-volume line is steeper." The reasoning step needed to earn the marks is absent.
- ch 7 [low] Figure: The plotted curves come from air values (cp = 1.005, cv = 0.718 kJ/kg·K, R = 0.287 kJ/kg·K), but the caption and aria text do not say the gas is air, so a student may think the curves hold for any ideal gas. The horizontal axis is labelled s − s₀ while the text uses s.
- ch 8 [high] Section 3, sentence before the lost-work formula: It says 'Every unit of S_gen is energy that can no longer become work'. S_gen is an entropy, measured in kJ/K, not an energy in kJ. One unit of S_gen is not a unit of energy; the energy actually lost is T₀ times the entropy generated.
- ch 8 [low] Beyond: 'the entropy account is now written in joules per kelvin of waste heat' is unclear: the entropy generated is in J/K, and the phrase 'joules per kelvin of waste heat' mixes entropy and heat into one quantity.
- ch 9 [low] Section 2, last paragraph; repeated in Quiz Q3 answer: The text says "Real cp falls to zero faster than T". That is false for real solids. In a metal at low temperature cp ≈ γT + βT³, so cp falls like T itself (cp/T tends to the finite constant γ) and the integral still converges. Convergence needs only cp → 0, not a rate faster than T.
- ch 9 [low] Section 2, the S(T) formula: The formula S(T) = ∫₀ᵀ (cp/T)dT gives absolute entropy only for a sample heated with no phase change. Real substances melt, boil or change crystal form on the way up from 0 K, and each of those steps adds ΔH_trans/T_trans.
- ch 9 [low] Section 3, sentence "At 0 K any reversible isothermal process has ΔS = 0, so entropy cannot be used to cool the last bit.": The wording is confusing. No process happens at exactly 0 K, and "entropy cannot be used to cool" is vague. The real point is that the entropy change of an isothermal process shrinks to zero as T → 0, so the entropy difference you can exploit between two field strengths disappears, and the temperature drop per adiabatic step shrinks.
