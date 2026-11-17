# s-physics-u7: free-model run

- Book: `books/common/s-physics/s-physics-u7.html`
- Status: ok
- Model calls so far: 36 (166,858 tokens in, 318,946 out), 8.0 minutes

## Checker

```
s-physics-u7.html: 8 chapters, 14549 words, 9 figures, 166 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 4, bullet 'Wrong — ρ(T)': The claim that the classical model gives 'a much weaker temperature dependence than the measured ρ' is wrong at low temperature. Drude's τ falls as 1/v_rms, so the model predicts ρ ∝ √T. Measured ρ falls as T⁵ at low temperature, which is far faster than √T, so there the model's dependence is much stronger, not weaker. The sentence is only true for the high-temperature part.
- ch 1 [low] Section 4, bullet 'Wrong — heat capacity': '(3/2)k_B of energy' has the wrong units. k_B is joules per kelvin, so (3/2)k_B is a heat capacity per electron, not an energy. The energy per electron is (3/2)k_BT. A student can read this as saying each electron carries a fixed energy (3/2)k_B.
- ch 1 [low] Section 3, paragraph comparing σ with the measured 5.9×10⁷ S/m: The agreement presented as a success of the model is circular: τ = 2.5×10⁻¹⁴ s is itself the value back-calculated from the measured conductivity of copper, so σ must come out close. It is a consistency check, not a prediction.
- ch 1 [low] Quiz Q7, answer: 'Hundreds of times smaller' overstates the gap. For copper at room temperature the ratio of the classical to the measured electronic heat capacity is about 3T/T_F ≈ 80; for silver and sodium it is smaller still (tens, not hundreds).
- ch 2 [high] Section 1: The sentence says Pauli exclusion allows one electron per quantum state, then adds that 'with spin, each momentum state holds one electron'. This contradicts the standard result and the chapter's own density-of-states derivation, which says 'Including two spin states' and gets k³/(3π²). A student will conclude there is no spin degeneracy.
- ch 2 [low] Section 2: Several powers are written without superscripts: 'kF = (3π²n)1/3', 'n = ... (2m/ħ²)3/2EF3/2', and 'Doubling n raises EF by 22/3 = 1.59'. Read literally, '22/3' is 22÷3 and '(3π²n)1/3' is a multiplication by 1/3. Elsewhere the chapter uses <sup> correctly, so the reader sees two different conventions.
- ch 2 [low] Quiz Q3: The answer writes '7.06 × 22/3', which reads as 7.06 × 22 ÷ 3, not two to the power two-thirds.
- ch 2 [low] Figure: The rounding of the curves does not match the values used in the text. The exponent factor is E<sub>F</sub>/k<sub>B</sub>T = T<sub>F</sub>/T, which is about 8.2×10⁴/300 ≈ 273 at 300 K and ≈ 82 at 1000 K for copper. The plotted expressions use 193 and 58, i.e. a Fermi temperature of about 5.8×10⁴ K, which conflicts with the 8×10⁴ K stated in the chapter and in the worked example.
- ch 2 [low] Section 3: The text says 'States within kBT outside are partly occupied', while Section 1 correctly says the step rounds over 'a few kBT' and the caption says 'a width of order kBT/EF'. The three statements should agree.
- ch 2 [low] Quiz Q7: The answer says doping and temperature move the Fermi level in a semiconductor 'by amounts comparable to the gap'. The movement is only a fraction of the gap, and the temperature part is of order kBT, which is far smaller than a typical 1 eV gap.
- ch 3 [high] Quiz Q6: The answer says E_F in an n-type sample lies 'usually between the donor level and E_C'. For normal (non-degenerate) doping this is wrong: at 300 K with, say, N_D ≈ 10¹⁶ cm⁻³ in silicon, E_F sits about 0.2 eV below E_C, while the donor level is only about 0.045 eV below E_C. So E_F lies between the intrinsic level (midgap) and the donor level, below the donor level, not above it.
- ch 3 [low] Figure: The caption puts the 1.1 eV gap at k = 0, i.e. a direct gap, while the 1.1 eV figure quoted throughout the chapter is silicon's indirect gap. In real silicon the minimum of the conduction band is not at k = 0 (the direct gap at k = 0 is about 3.4 eV), so a student may think silicon has a direct gap of 1.1 eV.
- ch 4 [high] Section 1, explanation after the p = N_V exp[−(E_F − E_V)/k_BT] formula: The direction is stated backwards. The text says 'the further E_F is below the valence states, the fewer empty states there are'. In fact, pushing E_F further below E_V makes the exponent −(E_F − E_V)/k_BT large and positive, so p grows: more empty states. A student will take away the opposite trend from the one the formula gives.
- ch 4 [high] Section 3, note under n = (N_D + √(N_D² + 4n_i²))/2: 'At low temperature n → N_D' contradicts the freeze-out bullet just above it, which says n falls as T falls because donors stay unionised. The formula assumes full ionisation (N_D⁺ = N_D), so it cannot describe freeze-out at all; it tends to N_D whenever n_i << N_D (which includes room temperature), and to n_i whenever n_i >> N_D. As written the two statements cannot both be true.
- ch 4 [low] Section 1, symbols listed under n = N_C exp[−(E_C − E_F)/k_BT]: The energies are given in eV but k_B is given as 1.381×10⁻²³ J/K, so the formula as printed mixes units. Only the later remark that k_BT = 0.0259 eV at 300 K saves it.
- ch 4 [low] Section 3, line under the exact-solution formula: The line begins 'where:' but no symbol is being defined; it is a comment on the formula. The 'where:' convention is used everywhere else for symbol meanings, so this reads as a slip.
- ch 4 [low] Section 2, sentence after the table: 'below the conduction band edge by a few k_BT' understates the size: at N_D = 10¹⁶ cm⁻³ the gap is about 0.21 eV, roughly 8k_BT. The phrase can mislead a student into thinking the Fermi level is always a tiny fraction of an eV from the band.
- ch 5 [high] Exam traps, last bullet: The claim 'The two carrier currents add, never subtract, because both are written as conventional current' is false as a general statement. J_n and J_p are both conventional currents, but they can point in opposite directions, so their magnitudes partly cancel. Example: light generates equal excess electrons and holes with the same concentration gradient, so the electron and hole diffusion currents point opposite ways; a signed addition is required.
- ch 5 [low] Section 2, photodiode sentence: 'Diffusion is why a photodiode works with no bias: light builds a gradient and carriers move on their own' overstates diffusion. At zero bias the built-in field of the junction depletion region does the separating; diffusion only delivers carriers generated in the neutral bulk to the junction.
- ch 5 [low] Figure, edge total → ein labelled 'uses': The diagram makes the Einstein relation look like a consequence of the total current density. Einstein links the two coefficients D and μ; it does not follow from J.
- ch 5 [low] Section 3, Einstein relation paragraph: 'Their ratio depends only on temperature' is true only for non-degenerate (Maxwell-Boltzmann) carriers. At the heavy doping levels common in emitters and contacts, degeneracy modifies the relation by a Fermi-Dirac factor.
- ch 6 [high] Lead and Section 1 (also quiz Q2): The chapter uses Φ_M > χ as the condition for electrons to leave the semiconductor and a depletion layer to form. Electron transfer depends on the Fermi levels, so the correct condition for n-type is Φ_M > Φ_s, where Φ_s = χ + (E_C − E_F) is the semiconductor work function. Φ_M > χ only makes Φ_B = Φ_M − χ positive. If χ < Φ_M < χ + (E_C − E_F), then Φ_B is positive but V_bi = Φ_B − (E_C − E_F)/e comes out negative, the bands bend down, electrons accumulate, and the contact is not rectifying. This contradicts the chapter's own V_bi formula.
- ch 6 [low] Section 2, the depletion-width formula: The formula W = √(2ε_s V_bi / (e N_D)) uses ε_s and N_D without defining them, so a student reading on a phone cannot tell what they are. The chapter does not say it applies at zero bias.
- ch 6 [low] Section 2, last line: "Tunnelling is the same quantum process met in Unit 6" is a bare unit reference. It gives no link and no chapter name.
- ch 6 [low] Exam traps, last bullet: "swapping the signs reverses the I–V curve" is unclear: the signs of what?
- ch 7 [high] Exam traps, trap 3: The factor is stated backwards. Leaving μ₀ out of B = μ₀(H + M) makes the computed B too large by 1/μ₀ ≈ 8×10⁵, not 'wrong by a factor of about 1.26×10⁻⁶'. As written, a student would think the answer comes out too small.
- ch 7 [low] Figure caption and y-axis: M is quoted as 'M = 5' and '±0.3' with no unit, while everywhere else M is in A/m. The figure is schematic, so a bare number invites the reader to think it is 5 A/m.
- ch 8 [high] Figure (plot spec): The 'soft' loop is not physically possible. Its points make B rise to 1.0 at H = 1 and then fall to 0.8 at H = 2, so B decreases while H keeps increasing. On the ascending branch B must level off at saturation, never drop, and the loop tip must sit at the largest H. The figure therefore contradicts the text ('B rises steeply, then bends over and saturates'). The soft loop also shows retentivity 0.8 out of a peak B of 1.0, a square-loop shape, which is not what a transformer-core soft material looks like.
- ch 8 [low] Section 1 and Section 2: Saturation and peak flux density appear as plain text 'B_s' and 'B_m' with underscores, while the chapter otherwise writes symbols as proper subscripts (B_r, H_c, P_h, W_h). A student may read B_s as a separate quantity.
