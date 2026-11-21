# ce-rcc-u1: free-model run

- Book: `books/civil/ce-rcc/ce-rcc-u1.html`
- Status: ok
- Model calls so far: 25 (82,716 tokens in, 186,048 out), 6.2 minutes

## Checker

```
ce-rcc-u1.html: 7 chapters, 11377 words, 8 figures, 132 KB
OK
```

## For the reviewer

- chapter 4: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [high] Section 2 (reinforcing steel design curve): It says IS 456 simplifies the design curve as a straight line up to fy and flat beyond. The code's design curve never reaches fy: it rises linearly to 0.87fy (at strain 0.87fy/Es) and stays constant at 0.87fy after that. A student would carry the wrong design stress into beam problems.
- ch 1 [high] Section 3 (creep coefficient): The creep coefficient is given as 1.6 to 2.2 'for load applied at 28 days'. IS 456 Figure 11 gives a single value, 2.2, for loading at 28 days. The value 1.6 belongs to loading at one year, not 28 days.
- ch 1 [low] Section 1 (stress–strain curve): 'Peaks at roughly fck' is loose. The peak stress of the curve measured on a cylinder is the cylinder strength, about 0.8 times the cube strength; the mean cube strength is itself above fck, so the in-member peak falls near fck only by coincidence. Students may read it as a rule.
- ch 1 [low] Section 1 (cylinder strength): 'The statistics are in characteristic strength' is vague and reads oddly for a second-language reader.
- ch 1 [low] Section 1 (minimum grade): 'Normal exposure' is not an IS 456 exposure class. The code names the classes mild, moderate, severe, very severe and extreme, and M20 is the minimum for mild exposure only.
- ch 1 [low] Section 2 (meaning of Fe): 'Fe stands for ferrous' is imprecise; Fe is the chemical symbol for iron (Latin ferrum).
- ch 1 [low] Section 2 (ultimate strength): 'Roughly 10% above yield' does not match the standard values. As per IS 1786 the minimum ultimate tensile strength is well above that for Fe415 and only a little above it for Fe550, so a single 10% figure misleads.
- ch 1 [low] Section 3 (layout): The bullet list of key numbers is dropped in the middle of Section 3, between creep/shrinkage and durability, which breaks the flow of the section for a reader revising on a phone.
- ch 1 [low] Exam trap 2: 'as later shows' is grammatically incomplete and unclear.
- ch 2 [low] Section 1, modular ratio formula and Quiz Q1: The chapter writes m = Es/Ec = 280/(3σcbc) as if the two expressions are the same quantity. They are not: with IS 456 short-term modulus Ec = 5000√fck ≈ 22 360 N/mm² for M20, Es/Ec ≈ 8.9, not 13.33. A student may think the code value is obtained by dividing the real moduli.
- ch 2 [low] Figure, edge from 'Elastic stresses' to 'Compare with permissible': The edge label 'no concrete tension' is an assumption of the analysis, not a description of the step from computing stresses to comparing them with limits. It reads as if the comparison step is about ignoring concrete tension.
- ch 2 [low] Section 3, step 'If M is greater, increase the depth': In WSM a section cannot carry more than the balanced moment with tension steel alone, but depth is not the only remedy; width can be increased, or compression steel added (doubly reinforced). The bullet reads as if depth is the only option and does not say why more tension steel cannot help.
- ch 3 [high] Worked example 1, steps 3–4 and answer; Quiz Q3 answer: The example and Q3 use the symbol Mu for the moment demand from factored loads ('Find the required ultimate moment Mu', 'Mu = 30 × 36 / 8 = 135 kNm'). Section 2 defines Mu as the collapse moment the section can carry, and Mu,req as the moment from factored loads. The same symbol is used for capacity in the check and for demand in the example, so a student cannot tell which side of 'Mu ≥ Mu,req' the 135 kNm belongs to.
- ch 3 [low] Section 2, first paragraph: 'concrete is taken near its cube strength' is vague and can be read as the concrete compressive stress at collapse being equal to fck. Concrete in bending does not reach its cube strength in the section; the ultimate stress block has a maximum stress well below fck.
- ch 3 [low] Exam traps, second bullet: The wording mixes two different mistakes. 'Do not then reduce material strengths by another factor as in limit state design' is not the same error as applying the load factor twice, and 'as in limit state design' sits ambiguously at the end of the sentence.
- ch 3 [low] Lead, Section 3, Exam traps and Beyond (references to Chapters 1.2, 1.4 and 1.6): The cross-references to other chapters are plain text, so a reader on a phone cannot jump to them. The series convention is to make such references links.
- ch 4 [high] Section 1, last sentence of paragraph 2: "Both checks use design values, not raw characteristic values" is wrong for the serviceability check and contradicts Section 3, which correctly says serviceability uses service loads. In IS 456 the serviceability limit state uses characteristic (service) loads with a load factor of 1.0, and deflection is computed from characteristic material strength (for example Ec from fck). A student reading both sentences will not know which is right.
- ch 4 [low] Section 2, flexure paragraph: "without crushing concrete or yielding all tension steel in an unsafe way" can be misread as saying yielding of tension steel is not allowed. Yielding of tension steel is the desirable, ductile behaviour that gives warning; what is unsafe is sudden crushing of concrete in an over-reinforced section.
- ch 5 [low] Section 1, third paragraph: The sentence 'Design only needs the weak tail, because a few low cubes should not make the whole structure unsafe' is muddled: it can be read as saying low cubes are ignored, or that they do make the structure unsafe.
- ch 5 [low] Section 1, last paragraph: 'Some syllabi call these characteristic values' is redundant and confusing — the chapter has already named them characteristic strength.
- ch 5 [low] Section 2, first paragraph: 'in service' is vague; the probability refers to the design life (or other defined reference period) of the structure, not to any instant of service.
- ch 5 [low] Section 3, second paragraph: 'about 5% of the time' reads as a fraction of clock time rather than as a probability over the reference period.
- ch 5 [low] Quiz Q7: The answer omits the test specimen, which the chapter itself specifies for fck.
- ch 6 [low] Section 1, first paragraph: "Some syllabi call these numbers design values" sits before the formulas and does not say which numbers. A reader can take "these numbers" to mean γf and γm, but the partial factors are not design values — the design values are Fd and fd.
- ch 6 [low] Section 2, wind combinations: The wind terms are written with a plus sign only. Wind can act in either direction, and the sign decides whether dead load is added or relieved, which is exactly the point of the 0.9DL case. The missing ± can mislead a student into thinking wind always adds.
- ch 6 [low] Section 3, note under fcd formula: "0.67 converts cube strength to the design value used in the member" is confusing: 0.67fck is not the design value. It is the strength in the actual member (cube strength reduced for the difference between cube and in-situ strength); the design value fcd is that quantity divided again by γm.
- ch 6 [low] Section 3, paragraph after the fcd formula: "The number 0.446 is just 0.67 ÷ 1.5" is not exact: 0.67 ÷ 1.5 = 0.4467. The code value 0.446 is that number rounded down, which is why 0.446 × 25 gives 11.15 while the exact form gives 11.17. The chapter shows the difference but never says why it exists.
- ch 7 [high] Section 1: The sentence 'The peak stress in the block is 0.446fck' contradicts the block just defined. The equivalent rectangular block has a uniform stress of 0.36fck — it has no peak. The value 0.446fck (= 0.67fck/1.5) is the peak of the real curved (parabolic-rectangular) distribution at the extreme compression fibre, before it is replaced by the equivalent block. As written, a student will think the code block varies from 0.446fck to 0.36fck.
- ch 7 [low] Section 1 and Section 2: The chapter says the stress is the average 0.36fck 'over the whole depth xu' and also that C acts at 0.42xu from the top. A uniform stress over xu would put the resultant at 0.5xu. Students notice the mismatch and lose confidence in the model.
- ch 7 [low] Worked example 1: The starting line gives xu = 0.48d with no reason, and the answers carry meaningless precision (Ast = 1238.388 mm², Mu = 160.641 kNm). A student cannot tell whether 0.48 is a code limit or an arbitrary choice.
- ch 7 [low] Exam traps, first bullet: 'Using 0.446fck as the average stress in C = 0.36fck b xu' reads as if the student substitutes into the 0.36 formula; the actual mistake being described is writing the force as 0.446fck b xu.
