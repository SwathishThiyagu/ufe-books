# ce-rcc-u2: free-model run

- Book: `books/civil/ce-rcc/ce-rcc-u2.html`
- Status: ok
- Model calls so far: 26 (93,572 tokens in, 237,457 out), 7.4 minutes

## Checker

```
ce-rcc-u2.html: 7 chapters, 12620 words, 8 figures, 133 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Lead: The lead says the neutral axis depth xu is found from strain compatibility, but the method used in this chapter (Section 2, the worked example) finds xu by force and moment equilibrium, C = T with Mu = 0.36 fck b xu (d − 0.42 xu). Strain compatibility only fixes the limit xu,max that keeps the section ductile. A student will look for a strain calculation that never comes.
- ch 1 [low] Exam trap 2: 'The factor 0.87 is the design strength after the partial safety factor for steel' confuses the factor with the strength. 0.87 is a number; 0.87 fy is the design strength.
- ch 1 [low] Section 1, last sentence: 'Some syllabi call this tension-only reinforcement' invents a non-standard name. The standard name is tension steel or singly reinforced; the odd term may stick in a student's memory and be written in the exam.
- ch 2 [high] Quiz Q7 answer: The direction of the error is stated backwards. Replacing the true steel stress fs (< 0.87 fy) by 0.87 fy makes the tension side too large, so the equation 0.36 fck b xu = 0.87 fy Ast overestimates xu, not underestimates it. For the chapter's own data (b = 300 mm, d = 500 mm, fck = 30, fy = 500, Ast = 2500 mm²) that equation gives xu = 335.6 mm, whereas strain compatibility gives xu ≈ 315.6 mm with fs ≈ 409 N/mm², so the over-reinforced section is still classified as over-reinforced. The claim that it wrongly predicts under-reinforced behaviour is therefore false.
- ch 2 [high] Section 1 (third paragraph), Section 2 (paragraph after the pt,lim formula), Section 3 (comparison bullet), Quiz Q4 answer: The less-than signs have been lost, so the key classification sentences read as nonsense: 'If xu u,max', 'means Ast st,lim', 'If Ast st,lim or pt t,lim', 'Since pt t,lim'. A student cannot tell which side of the limiting value puts the section in which mode.
- ch 2 [low] Section 1, paragraph defining xu,max: The chapter says xu,max is the depth at which 'concrete crushing and steel yielding occur together' and that the tabulated values come from 'a steel strain that ensures yielding'. Yield strain is fy/Es, but the code limit uses the larger strain εs,lim = 0.002 + 0.87 fy/Es, so the steel has already yielded well before xu falls to xu,max. The loose wording can make a student think xu,max is set by εy.
- ch 3 [high] Quiz Q4 answer: The answer is corrupted and never states the conclusion. As printed it reads 'εsc = 0.0035(240−150)/240 = 0.0013125 6/(262.5×350) = 374.8 mm²' — the value of fsc, the comparison with the yield strain and the 'does not yield' conclusion are missing, so a student copying it gets a meaningless line.
- ch 3 [low] Worked example 1 (steps 2 and 5) and Quiz Q3: 10⁶ is typed as '106' (for example '34.43 × 106 N·mm'). On a phone this reads as one hundred six and invites a unit slip, which is exactly the trap the chapter warns about.
- ch 3 [low] Figure caption: The caption says the excess moment 'is first used to fix xu at 240 mm'. The order is backwards: xu,max = 0.48d = 240 mm is fixed by the steel grade and the section, and ΔM is computed from it. A student may think xu depends on ΔM.
- ch 3 [low] Quiz Q1 answer: The definition is restricted to a 'rectangular beam', but a doubly reinforced section can be of any shape; the defining feature is compression steel in addition to tension steel, not the shape.
- ch 4 [high] Section 3, the paragraph beginning 'If xu > Df, the neutral axis is in the web': The final sentence is garbled: 'If 0.42xu f, replace Df by 0.42xu in Cf and in its lever arm.' The condition is missing its comparison and the symbol 0.42xu is written as a product with a stray 'f', so a student cannot tell when the partial-flange case applies. As printed the sentence is meaningless and contradicts nothing but explains nothing.
- ch 4 [low] Section 2, sentence 'Isolated T-beams have smaller limits under IS 456; use the clause for isolated beams.': The sentence refers to a clause that is never named and never gives a limit, so a student cannot apply it. It also sits between the continuous-beam note and the closing advice, breaking the flow.
- ch 4 [low] Section 2, last line before 'Never take the whole slab width': 'Some syllabi call all of these flanged beams' adds no information: the chapter has already named T-beams and L-beams as flanged beams, so the sentence reads as filler.
- ch 5 [high] Section 1, third bullet: The stress block is described wrongly. It says 0.36 fck acts over a depth of 0.42 xu. In IS 456 the average stress 0.36 fck acts over the full compression depth xu; 0.42 xu is only the line of action of the resultant force (which is why the lever arm is d − 0.42 xu). A student reading this would think the compression block is 0.42 xu deep, and would then not see where the d − 0.42 xu in the moment formula comes from.
- ch 5 [low] Exam traps, fourth trap: The 'wrong by 15 %' figure fits the grade mix-up for steel (Fe500 table used for Fe415 gives about 0.83 % instead of 1.00 %, roughly 17 % low), but not for concrete: an M30 table used for M25 at Mu/bd² = 3.00 N/mm² returns about 0.96 % against 1.00 %, only about 4 % off. Quoting one 15 % figure for both cases overstates the concrete error.
- ch 6 [high] Section 2: The direction and reason given for kt are reversed. In IS 456 (Fig. 4) the modification factor for tension reinforcement is largest (about 2.0) for lightly reinforced sections and falls as the tension steel percentage rises; it does not 'grow when tension steel is high'. The stated reason is also wrong: a low steel percentage gives a shallow neutral axis, so for the same service steel stress the curvature and deflection are smaller, which is why a larger span/depth is allowed.
- ch 6 [high] Exam traps, item 3: The 20 mm cap never governs for short spans. The after-partition limit is the lesser of L/350 and 20 mm. Since L/350 = 20 mm at L = 7000 mm, the cap governs only for spans longer than 7 m; for shorter spans L/350 is the smaller value and governs.
- ch 6 [low] Quiz Q8: The answer says factored loads 'overestimate deflection', which suggests the check works from loads. The span/depth check never computes deflection; its modification factor needs the service steel stress fs, which is by definition a service-load quantity. The answer is loose about this.
- ch 7 [high] Section 1, first sentence: 'At service load the beam is usually uncracked' is false. A normally reinforced beam has Mcr below its service moment, so at service load the tension zone is already cracked; that is exactly why cracked-section analysis is used for deflection and steel stress. The statement also contradicts Section 3, which says to switch to the cracked section when Mservice exceeds Mcr.
- ch 7 [high] Section 3, sentence after the Mcr formula: The comparison operator is missing: 'If Mservice  Mcr, use the cracked section'. The criterion cannot be read, and a student may take it either way.
