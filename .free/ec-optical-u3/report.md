# ec-optical-u3: free-model run

- Book: `books/ece/ec-optical/ec-optical-u3.html`
- Status: ok
- Model calls so far: 25 (81,353 tokens in, 183,308 out), 5.6 minutes

## Checker

```
ec-optical-u3.html: 8 chapters, 12150 words, 9 figures, 140 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, the thermal-equilibrium line: The sentence is broken: "In thermal equilibrium N2/N1 = exp(−hf/kT)  N1, an inverted population." Part of the argument (that N2 < N1 at equilibrium, and that inversion means N2 > N1) has dropped out, so the reader cannot follow why pumping is needed.
- ch 1 [low] Exam traps, first bullet: "it happens after τ_sp" reads as if the atom waits exactly τ_sp before dropping. τ_sp is only the average delay; single atoms decay at random times.
- ch 1 [low] Section 2: Two symbols are used without definition: ρ(f), the spectral energy density, and k, T in exp(−hf/kT). A student cannot check units.
- ch 2 [low] Section 2, opening line: The text says "Three efficiencies are easy to mix" but then defines four quantities: internal quantum efficiency, extraction efficiency, external quantum efficiency and power efficiency. A student counting will be confused about which three are meant.
- ch 2 [low] Section 2 (I-P curve) and quiz Q6: "Above turn-on it is almost linear" and "a current of 30 mA above turn-on" use "turn-on" for an LED, where it normally means the forward voltage (about 1 V), not a current. The reader cannot tell whether 30 mA is the total current or the current measured above a threshold, and the answer silently treats it as the total current.
- ch 2 [low] Lead: The list "planar, dome, surface-emitter and edge-emitter LEDs" puts planar and dome side by side with surface emitter, although a planar LED and a dome LED are both surface emitters. The categories overlap, which contradicts the figure where planar and dome sit under surface emitter.
- ch 2 [low] Quiz Q4 answer: The second reason is stated as the bandgap shrinking and "reducing emission at the design wavelength", which does not actually explain why the optical power falls. The power falls because a smaller bandgap gives a lower photon energy E, so each escaping photon carries less energy even at the same photon rate.
- ch 2 [low] Figure (tree diagram): The text calls the Burrus LED an important higher-radiance surface emitter, but the figure leaves it out, so the two paths mentioned in the caption do not show it.
- ch 3 [high] Section 2, feedback and threshold — 'It falls with lower αi, longer L, higher R1R2, or higher Γ': The trend for L is stated for threshold current, but it is threshold current density that falls when L grows. With fixed stripe width W, I_th = J_th × L × W, and J_th ∝ (αi + (1/2L)ln(1/R1R2))/Γ. Substituting gives I_th ∝ (W/Γ)(αi·L + ½ln(1/R1R2)), which rises with L. So a longer cavity lowers mirror loss and current density but raises the total threshold current.
- ch 3 [low] Section 1, first sentence: k_B and T appear in exp[−(E2−E1)/(kBT)] without being defined, though the chapter defines every other symbol.
- ch 3 [low] Quiz Q6: 1.5% per °C is far gentler than a real laser diode, whose threshold current typically rises by roughly a factor of 2 over 20–30 °C. A student may take 1.5%/°C as a realistic device value.
- ch 3 [low] Section 2, mode spacing: Δν = c/(2nL) uses the phase index n; the actual spacing between longitudinal modes is set by the group index.
- ch 4 [high] Section 2, second paragraph: The claim that a double heterostructure 'pushes Γ close to 1' is wrong. In a bulk double-heterostructure laser with an active layer of about 0.1 µm the confinement factor is only a few tenths (typically 0.1–0.4). Γ ≈ 1 needs an active layer several wavelengths thick. What really lowers J_th in a DH laser is that the heterobarriers confine the carriers, so the gain coefficient β (gain per A/m²) rises sharply, and α_i falls.
- ch 4 [high] Quiz Q4: The answer repeats the incorrect statement that 'the confinement factor Γ approaches 1'. A student who writes this loses marks: in a DH laser Γ is typically a few tenths, and the drop in J_th comes mainly from carrier confinement increasing β and from low α_i.
- ch 4 [low] Section 2, after the J_th formula: 'A shorter cavity raises α_m, so length trades low threshold against low mirror loss' is ambiguous. Raising α_m raises J_th, yet shortening the cavity lowers the threshold current I_th because the active volume shrinks. As written the student cannot tell which threshold is meant.
- ch 4 [low] Section 1, first paragraph: 'Injected carriers pile up faster than they recombine' suggests the carrier density grows without limit. It builds only until recombination (spontaneous, then stimulated) balances the injection.
- ch 5 [low] Section 1, end of the paragraph on confinement: The sentence "Both raise gain per unit volume and lower threshold current" is loose. Carrier confinement raises the gain per unit volume, because it packs carriers into a small active region. Optical confinement does not change the gain per unit volume; it raises the fraction of the optical mode that overlaps the active layer (the confinement factor Γ), which raises the modal gain Γg. A student can read this sentence as saying the index step also multiplies the material gain.
- ch 5 [low] Section 2, photon-energy sentence: The term E₁h in "E_g + E₁e + E₁h" is never defined. The student has seen only the electron mass in the formula and may not know that the hole level uses the hole effective mass.
- ch 6 [high] Section 2, sentence 'A lens can shrink the source image to the core and turn rays toward the axis': For a source larger than the core the image must be demagnified, and demagnification widens the ray cone at the fiber face, it does not turn rays toward the axis. As written, the sentence contradicts the figure caption (the lens cannot recover light outside the acceptance cone) and suggests a lens can beat the (r_c/r_s)² NA² limit, which the étendue argument forbids.
- ch 6 [low] Section 1, sentence 'The NA² result comes from accepted solid angle divided by π': Only an approximation. The exact fraction of a Lambertian source's power inside the acceptance cone is sin²θ_a = NA², while the accepted solid angle of the cone is 2π(1 − cos θ_a), so dividing it by π gives 2(1 − cos θ_a), which equals NA² only for small angles. The student is left with a rule that looks exact but is not.
- ch 6 [low] Lead and Section 1, 'Only a few universities teach the full calculation': The same sentence appears twice within a few lines, which reads as filler.
- ch 6 [low] Section 1, Fresnel loss sentence and exam trap 5: The near-4% figure is quoted without its assumption; it holds for a glass-air interface of refractive index about 1.5. A student meeting a fibre of different index cannot check the number.
- ch 7 [high] Section 2, intrinsic loss, core-diameter mismatch: The direction of the core-size loss is stated backwards. Light from the smaller core (50 μm) falls entirely inside the larger core (62.5 μm), so with equal NA there is almost no core-size loss in the small-to-large direction; the chapter claims this direction 'loses the fraction outside the smaller core'. The reverse (62.5 μm into 50 μm) loss is geometric overlap, roughly the area ratio, not an angular effect: with equal NA the smaller fiber accepts all angles that the larger one emits.
- ch 7 [low] Quiz Q1 answer: The question asks for one place each connector is used, but the ST answer gives 'older installations', which is a time period, not a place.
- ch 7 [low] Section 3: The longitudinal gap is introduced and given the symbol s, but s is never used again and no gap-loss relation or typical value is given.
- ch 8 [low] Section 1, last sentence: "Some syllabi call the resulting device a Mach-Zehnder modulator (MZM)" makes the standard name sound like an optional local usage. A student may think MZM is a non-standard alias.
- ch 8 [low] Section 1, Vπ definition, and Quiz Q1: The text defines Vπ as "the voltage that gives a phase shift of π radians", but Q1 defines it as the voltage that gives a phase difference of π between the two arms. In push-pull drive each arm only shifts π/2 when V = Vπ, so the two wordings disagree by a factor of two and can lead a student to double the arm phase.
- ch 8 [low] Section 1, Pockels effect sentence: The sentence "The modulator works by the electro-optic or Pockels effect" is written for all external modulators, yet Section 3 describes the EAM, which works by field-induced absorption, not the Pockels effect. A student may assume every external modulator uses the Pockels effect.
- ch 8 [low] Section 3 and Beyond: The travelling-wave electrode point (electrical and optical waves travel together, low drive voltage at high bit rates) is stated in full twice, once in Section 3 and again in Beyond.
