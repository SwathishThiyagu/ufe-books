# ch-thermo-u5: free-model run

- Book: `books/chem/ch-thermo/ch-thermo-u5.html`
- Status: ok
- Model calls so far: 20 (80,429 tokens in, 177,226 out), 4.7 minutes

## Checker

```
ch-thermo-u5.html: 8 chapters, 14189 words, 9 figures, 159 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, definition sentence: The definition says μi is 'the change in G when one mole of i is added'. Strictly, μi is a derivative (a rate of change per mole); adding a whole mole can itself change μi, so the finite-mole wording is only an approximation and can mislead a student reading it literally.
- ch 1 [low] Section 1, 'Some syllabi call μ the partial molar Gibbs energy or the escaping tendency': Partial molar Gibbs energy is a correct synonym, but 'escaping tendency' is a descriptive phrase usually attached to fugacity, not a second name for μ. Listing the two together as if they are the same label is confusing.
- ch 1 [low] Section 3, last sentence: 'If a small transfer raises G, the phase is stable; if it lowers G, the phase splits or changes' mixes ideas and does not say between which phases the transfer is made. A student can read it as a criterion for phase splitting, which it is not.
- ch 1 [low] Worked example 1 (and Quiz Q3): The calculation treats μliq and μvap as fixed while 0.010 mol moves. In a real mixture μ changes as composition changes, so ΔG = Σ μi Δni is exact only for an infinitesimal transfer; for a finite transfer it is an approximation that must be stated.
- ch 1 [low] Quiz Q1, answer: 'at constant temperature, pressure, and composition of all other species' — the derivative holds the amounts (moles) of the other species fixed, not their composition, which would change if the total moles change.
- ch 1 [low] Quiz Q5, question wording: The question first states 'At equilibrium, μiα = μiβ' and then immediately 'If μiα = μiβ + 2.0 kJ/mol'. The two statements contradict each other, and a student may think equilibrium is being described in both.
- ch 2 [low] Section 1: "M̄_i has the same units as M per mole" reads as "(M per mole)", i.e. units per mole again (for example cm³/mol²), which is wrong. M is already a per-mole quantity, and M̄_i carries exactly the same units as M.
- ch 2 [low] Quiz Q7: The answer writes the tangent as y = M + (M̄₁ − M̄₂)(X − x₁) but never says what X is; a student can confuse X with the mixture property M or with x₁.
- ch 3 [high] Section 3, slope-checking paragraph: The magnitude ratio is reversed. Gibbs–Duhem gives x₁|dM̄₁/dx₁| = x₂|dM̄₂/dx₁|, so |dM̄₁/dx₁| : |dM̄₂/dx₁| = x₂ : x₁, not x₁ : x₂. The chapter's own worked example contradicts the printed ratio: at x₁ = 0.40, x₂ = 0.60 the slopes are 30 and 20 (ratio 3:2), which is x₂ : x₁, whereas x₁ : x₂ would be 2:3.
- ch 3 [low] Figure, node e note: The note reads 'dM̄₁=-30, dM̄₂=20', which looks like values of the partial molar properties themselves, not of their slopes with respect to x₁. That contradicts the chapter's own warning that Σ xᵢ M̄ᵢ is not zero.
- ch 4 [low] Section 2, sentence beginning 'Read the sign': The sentence is garbled: 'If Z  1, φ > 1.' The comparison operator is missing, so the student sees an incomplete condition and cannot tell which case gives φ above 1 and which gives φ below 1.
- ch 4 [low] Section 2, paragraph after the ln φ formula: The integrand (Z − 1)/P does not vanish as P → 0. Since Z − 1 ≈ BP/RT at low pressure, (Z − 1)/P tends to the finite value B/RT. The integral converges because that limit is finite, not because it is zero. As written, a student will believe the integrand goes to zero at the lower limit.
- ch 4 [low] Section 3, generalized correlation paragraph: 'Reliable for non-polar gases up to a few bar' states the validity in absolute pressure. The virial correlation is limited by reduced pressure (roughly Pr below about 0.5) and by Tr above about 0.8. For a gas with a high critical pressure, 'a few bar' is far too cautious and misleads the student about when the formula can be used.
- ch 4 [low] Section 1, sentence after the φ formula: 'Some syllabi call φ the fugacity coefficient and write it as f/p' is confusing: the chapter has just defined φ as the fugacity coefficient, so it reads as if the name were a syllabus variant. The point is only the alternative symbol f/p.
- ch 5 [high] Section 3, sentance beginning 'If pi is less than xiPisat': The text is garbled: 'the deviation is negative, γi i → 0, Raoult's law usually fails even when the solvent follows it.' The activity-coefficient condition for negative deviation (γi < 1) is missing and the fragment 'γi i → 0' is meaningless. The Henry's-law sentence that follows has also lost its subject (the dilute solute), so a student cannot tell which component Raoult's law fails for.
- ch 5 [low] Figure aria text: It says the bubble and dew curves 'meet at 58 kPa for x₁ = 0.30 and y₁ = 0.517'. They do not meet there; at P = 58 kPa the two curves are at two different compositions (a tie line). The curves meet only at the pure-component ends (40 kPa and 100 kPa).
- ch 5 [low] Section 3: Only a positive-deviation example (ethanol + water) is given; negative deviation is defined but never illustrated, so the reader has nothing concrete for γi < 1.
- ch 5 [low] Exam traps (all five) and Section 1: Notation is inconsistent: the traps write ΔH_mix, ΔV_mix, P_i^sat, f_i^pure, x_i with underscores, which print literally in the text field, while the body uses subscripts (ΔHmix, Pisat, fipure).
- ch 6 [low] section 1, note under the ΔS_mix^id formula: The sentence 'The sum is positive, so ΔSmixid is positive' is wrong if 'the sum' means Σ xᵢ ln xᵢ. In a mixture each ln xᵢ ≤ 0, so Σ xᵢ ln xᵢ is negative; only −R Σ xᵢ ln xᵢ is positive. A student may read this as Σ xᵢ ln xᵢ > 0.
- ch 6 [low] exam traps, first bullet: 'Do not set ME = ΔMmix for S or G; that is true only for H and V' is incomplete and contradicts section 1, which lists U among the properties. For an ideal solution U^id = Σ xᵢ Uᵢ^pure, so ΔU_mix^id = 0 and U^E = ΔU_mix as well.
- ch 6 [low] section 1, ideal-solution sentence: 'ΔHmixid = 0 and ΔVmixid = 0 because the interactions are the same as in the pure components' gives one reason for two different facts. Zero heat of mixing comes from equal interactions; zero volume change comes from the molecules being of similar size and packing the same way, so volumes add.
- ch 7 [low] Lead and Section 1: The text says activity 'carries the escaping tendency' and calls it 'the effective amount that fixes escaping tendency'. Fugacity is the escaping tendency; activity is a dimensionless ratio fᵢ/fᵢ°. Calling it an 'amount' invites students to treat activity as a number of moles.
- ch 7 [low] Section 2: 'A value above 1 means positive deviation; below 1 means negative deviation' follows a sentence about both aᵢ and γᵢ, so a student may apply the rule to activity. Activity can be above 1 with no deviation at all (for example a₁ = 1.5 when x₁ = 0.9, γ₁ = 1.67).
- ch 7 [low] Section 3: GE/RT = Σ xᵢ ln γᵢ is stated to hold with 'γᵢ in the chosen standard state'. It is exact only when every component uses the pure-liquid (Raoult) standard. With a Henry standard for a solute, Σ xᵢ ln γᵢ differs from the excess Gibbs energy by a linear term x₂ ln γ₂∞, so it is not the departure from an ideal solution.
- ch 8 [low] Section 2, Wilson paragraph: The interaction energy a₁₂ is introduced without units, so a student cannot tell whether the exponential argument −a₁₂/RT is dimensionless for the right reason.
- ch 8 [low] Section 2, last sentence: 'Margules is symmetric; van Laar and Wilson are asymmetric' reads as if asymmetry were built into the van Laar and Wilson forms. Both reduce to the symmetric two-suffix form when their two constants are equal (A₁₂ = A₂₁, or Λ₁₂ = Λ₂₁).
- ch 8 [low] Section 2 and Quiz Q6: 'Its G^E curve has only one well' is a loose shorthand for why Wilson fails for liquid-liquid equilibrium; a single-well G^E picture alone does not explain the failure.
- ch 8 [low] Section 3, cross-reference sentence: 'It links directly to Unit 6, Phase Equilibria' hard-codes a unit number that may not match the reader's edition, and it is a plain mention rather than a chapter link.
