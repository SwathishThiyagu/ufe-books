# s-physics-u4: free-model run

- Book: `books/common/s-physics/s-physics-u4.html`
- Status: ok
- Model calls so far: 24 (94,985 tokens in, 197,110 out), 5.6 minutes

## Checker

```
s-physics-u4.html: 7 chapters, 12190 words, 8 figures, 130 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, phase rule paragraph: The sentence breaks off mid-clause: "When light reflects from a lower-index medium (rarer medium, n₂ 4.2 and 4.5." The condition n₂ < n₁ and the no-phase-change conclusion are missing, and the cross-references are garbled. A student cannot read the rule that thin-film interference later depends on.
- ch 1 [low] Figure: The reflected wave is labelled "r = i = 30°" while the refracted wave is labelled "r = 19.5°". Section 1 used r′ for the angle of reflection and r for the angle of refraction, so the same symbol r now stands for two different angles in one figure.
- ch 2 [low] Section 3, paragraph on the λ/2 shift: The claim that one reflection is from a denser medium and the other from a rarer medium is stated as always true. It holds for a soap or oil film in air, where the film index is higher than the medium on both sides. For a film whose index lies between the two surrounding media (for example a film on glass with μ_film < μ_glass), both reflections can be from a rarer to a denser medium, so both carry the π shift and the net λ/2 term cancels. A student can apply the λ/2 rule where it does not hold.
- ch 2 [low] Section 3, sentence 'That single reversed reflection adds λ/2': 'Reversed reflection' is not defined anywhere. A student cannot tell whether it means a phase reversal of π or a change of direction of the ray.
- ch 3 [high] Section 1, the two-line formula block: The two conditions that include the λ/2 reflection shift are labelled the wrong way round. 2t + λ/2 = mλ means 2t = (m − ½)λ, which is the BRIGHT condition, not dark; 2t + λ/2 = (2m − 1)λ/2 means 2t = (m − 1)λ, which is DARK. The simplified line printed just after it (dark at 2t = mλ, bright at 2t = (2m − 1)λ/2) is correct, so the block contradicts itself and a student cannot see how the simplified forms follow.
- ch 3 [high] Worked example 1 (and the data reused in Quiz Q4): The quoted ring diameters cannot come from one lens and are inconsistent with the R the example itself obtains. For R = 0.516 m the 5th dark ring must satisfy D₅² = 4×5×R×λ = 6.08 × 10⁻⁶ m², i.e. D₅ = 2.47 mm, not 3.0 mm; likewise the 15th ring is 4.27 mm, not 4.6 mm. Also the ratio test fails: D₁₅²/D₅² must equal 15/5 = 3, but the given numbers give 21.16/9.00 = 2.35. The computed answer D₁ = 1.10 mm (and the figure, D_m = 1.103√m mm) then contradicts the stated D₅ = 3.0 mm, and Quiz Q4 builds on that impossible pair.
- ch 3 [high] Quiz Q4, answer: The answer is garbled and self-contradictory: it first computes 0.90, then writes '… corrected:', then gives 1.33. The 0.90 arises because the substitute values are inconsistent (D₅ = 3.0 mm with R = 0.516 m gives D₅² = 9.0 × 10⁻⁶ m², whereas 4mRλ = 6.08 × 10⁻⁶ m²), so the two routes disagree and a student sees a wrong working printed as if it were a check.
- ch 4 [low] Section 1, paragraph beginning 'The virtual image M₂′': The text says the air-film thickness is 't = d, the mirror separation'. A student reads 'mirror separation' as the physical distance between the two real mirrors, which is not d. d is the gap between M₁ and the virtual image M₂′, i.e. the difference in the two arm lengths.
- ch 4 [low] Section 1 (circular fringes) and Quiz Q4: The chapter states that the fringes are circular without the condition that makes them circular: M₁ and the virtual image M₂′ must be exactly parallel. If the mirrors are slightly tilted, the fringes are straight or curved fringes of equal thickness, not rings. The exam trap 'they are not caused by the mirror shape' can leave a student thinking the alignment does not matter.
- ch 4 [low] Section 1, formula Δ = 2d cos θ: 'θ is the angle of the ray inside the air film' does not say what the angle is measured from. A student may measure it from the mirror surface instead of the normal.
- ch 4 [low] Exam traps, last bullet: 'A count at one point and a count of new rings are different observations' is unclear; the student cannot tell what the two observations are or why only one of them gives d = Nλ/2.
- ch 4 [low] Figure: Section 1 says the compensating plate is part of the instrument and explains its role, but the figure has no compensating plate, so the picture does not match the text.
- ch 5 [low] Lead and Section 1: The lead says the two reflected waves 'arrive half a cycle apart and cancel', which reads as complete cancellation. The two waves have different amplitudes (about 4% at the air–film face, about 1% at the film–glass face for MgF₂), so the half-cycle path difference alone cannot give zero reflection. Students then wonder why Section 2 admits 1.4% remains.
- ch 5 [low] Section 2, last paragraph: 'the surface may look purple or green in white light' is loose and lets a student think either colour is equally likely. A coating designed near 550 nm reflects least green, so the reflected light is missing green and looks magenta or purple.
- ch 5 [low] Exam traps, trap 5: 'the phase rule changes' is too vague to use in an answer. It does not tell the student what actually happens when the film index is above the glass index.
- ch 5 [low] Section 2, last paragraph: Single MgF₂ layers are listed for solar cell covers 'where one design wavelength ... matter[s]'. A solar cell receives the whole solar spectrum, so a one-wavelength coating is a poor match for that application; the sentence undercuts the broadband argument made just before it.
- ch 5 [low] Section 2, first paragraph: The word 'reversed' is used for a reflection phase change without being defined, so a student may read it as a change of direction of the ray.
- ch 6 [low] Section 2, last sentence: The sentence 'Some orders may be weak or absent when the single-slit pattern puts a minimum there; one mention is enough' contains an editorial instruction ('one mention is enough') addressed to the writer, not the student, and it leaves the missing-order idea half-explained.
- ch 6 [low] Section 2 and Exam traps, m_max formula: m_max = floor(d/λ) is stated without the edge case. When d/λ is exactly an integer, the order m = d/λ gives sin θ = 1, that is θ = 90°, a grazing beam that is not seen in practice, so the formula then overcounts by one.
- ch 7 [high] Section 3 (wave plates): The chapter says a quarter-wave plate makes plane polarized light circularly polarized without any condition on the orientation of the incident plane. This is false in general: circular polarization needs the two components to have equal amplitude, which happens only when the incident plane is at 45° to the optic axis. At any other angle the output is elliptically polarized, so a student will write the unconditional statement in the exam and lose marks.
- ch 7 [low] Section 1 (three descriptions): "a number between 0 and 1 gives the fraction that is polarized" is loose. The standard quantity is the degree of polarization, defined from the maximum and minimum intensities seen as the analyser turns, not simply a fraction of the intensity.
- ch 7 [low] Exam traps, fourth bullet (Brewster): "do not add 90° to the incidence angle" is ambiguous — a student cannot tell whether 90° is being added to θ_p or subtracted to get the refraction angle.
- ch 7 [low] Quiz Q4: The answer states the 90° separation as the cause of full polarization without the physical link. The 90° separation and the full polarization both follow from Brewster's condition; the reason the in-plane component vanishes is that the dipoles in the medium oscillate along the refracted ray's direction and cannot radiate along that same direction.
