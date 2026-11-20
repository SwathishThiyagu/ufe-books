# me-ic-u1: free-model run

- Book: `books/mech/me-ic/me-ic-u1.html`
- Status: ok
- Model calls so far: 33 (121,359 tokens in, 254,277 out), 5.2 minutes

## Checker

```
me-ic-u1.html: 8 chapters, 15282 words, 9 figures, 160 KB
OK
```

## For the reviewer

- chapter 6: the figure cannot be drawn: lane labels are too long
- chapter 2: the figure cannot be drawn: note "steady" runs off the right edge; shorten it
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Section 1: Four names that made the engine: The four names are not in date order: Clerk (1878) is placed after Diesel (patent 1892, engine 1897). In a history section this reads as if Clerk came after Diesel, and a student revising by sequence will memorise the wrong order.
- ch 1 [low] Section 3, Strokes: "A two-stroke engine uses ports and scavenging" is stated as if it holds for every two-stroke. Large two-stroke diesel engines use an exhaust valve with uniflow scavenging and inlet ports only; piston-controlled ports alone are typical of small engines.
- ch 1 [low] Figure: The chapter calls fuel one of the five classification labels, but the tree has branches only for ignition, stroke and cooling, with aspiration as a root note. Fuel appears nowhere, so the figure and the text do not match.
- ch 1 [low] Section 3, Fuel: "Petrol, diesel, CNG, LPG, alcohol blends and hydrogen are all used in production engines" puts hydrogen on the same footing as the others. Hydrogen IC engines have appeared only in small-series production; most hydrogen vehicles on the road are fuel-cell electric, not IC engines.
- ch 1 [low] Section 1, Section 2, Section 3 (cross-references): Cross-references such as "see four-stroke operation", "See SI and CI working principle", "See Chapter 1.3" and "See Unit 4, Cooling, Lubrication and Supercharging" are plain text, so a student reading on a phone cannot tap through to the chapter.
- ch 2 [low] Section 1, opening line: The text says 'These six words describe the space inside one cylinder', but the bullets name seven terms: bore, stroke, TDC, BDC, swept volume, clearance volume and compression ratio. A student counting them will think a term is missing.
- ch 2 [low] Exam traps, first trap: The reason given, 'the gas is squeezed into the clearance volume plus nothing else, but it starts from the whole cylinder volume', is garbled and can be misread as saying the denominator is Vc plus something.
- ch 2 [low] Section 1, mean effective pressure paragraph: 'one steady pressure that would produce the same work in one stroke' is loose. MEP times swept volume gives the net work per cycle, and in a four-stroke engine a cycle spans four strokes, not one.
- ch 2 [low] Section 3, crankshaft bullet: 'it carries the full torque of every cylinder at once' is misleading; cylinders fire in sequence and the torque builds up along the shaft from the front main journal to the flywheel, it is not applied as one lump.
- ch 3 [low] exam traps, trap 1: The sentence 'Two-stroke does not mean two strokes per cycle in the four-stroke sense' is confusing and partly false: a two-stroke cycle does consist of exactly two strokes (one up, one down). The real point is that each stroke does two jobs, and the wording as written can leave a student thinking a two-stroke cycle has some other number of strokes.
- ch 3 [low] quiz, Q6: The answer says a two-stroke 'fires twice as often per revolution'. A two-stroke fires once per revolution and a four-stroke once per two revolutions; the doubling is per unit time at the same speed, not per revolution.
- ch 4 [high] Quiz Q7, answer: The answer says a compression ratio of 9 leaves the air 'well below the autoignition temperature of diesel'. Using the chapter's own method (Section 2), a ratio of 9 raises air from about 300 K to roughly 300 × 9^0.4 ≈ 720 K, about 450 °C. That is above the 250 °C autoignition figure the chapter itself gives for diesel, so the stated reason contradicts the chapter's numbers and a student can catch it.
- ch 4 [low] Figure: The spec lists all ten nodes (five for SI, five for CI) as one column with direction 'down' and only intra-path edges. As drawn it renders as a single 10-block vertical chain, not the two parallel paths that the caption and aria describe.
- ch 4 [low] Worked example 2: The stem gives a four-cylinder engine, but the question asks for the clearance volume of one cylinder. Students may divide by 4 or wonder whether the cylinder count matters; it is never used.
- ch 5 [high] Section 2, paragraph 2 and the table row 'Overlap': The chapter says a CI engine 'can use more overlap to scavenge the clearance volume with fresh air' and the table says CI overlap is 'Often larger'. Standard textbook practice is the opposite: naturally aspirated diesels run small overlap or none, because the high compression ratio leaves very little piston-to-valve clearance, and with no throttle there is no inlet pressure higher than exhaust pressure to scavenge the clearance volume. Larger overlap appears only in pressure-charged (turbo/blower) diesels where inlet pressure exceeds exhaust pressure. A student writing 'CI overlap is larger' in the exam is likely to be marked wrong.
- ch 5 [low] Section 3, paragraph 2: 'In a simple piston-port engine, each port opens and closes at equal angles around BDC' is not true of the inlet port, which the next two sentences correctly place near TDC. A student can read 'each port' literally and draw the inlet port symmetric about BDC.
- ch 6 [low] Section 1, bullet on 1-2-4-3: The sentence says 'the two cylinders of a piston pair fire in the opposite sequence', but only one pair actually swaps. With cylinder 1 first, the pair 1 and 4 fires 1 then 4 at 360° in both 1-3-4-2 and 1-2-4-3. Only the pair 2 and 3 swaps (3 then 2 becomes 2 then 3).
- ch 6 [low] Quiz Q4 answer: The answer says the order 'decides which cylinder of a pair fires first', which is not true for the pair 1 and 4: cylinder 1 fires first in both orders. Only the 2-3 pair changes hands.
- ch 6 [low] Section 1, first paragraph: 'the pistons share crank throws' is loose. In an inline four each piston usually has its own crankpin; the pistons are paired because throws 1 and 4 and throws 2 and 3 lie in the same plane and reach top dead centre together. Sharing one crankpin happens mainly in V engines.
- ch 7 [high] Worked example 1, steps 2 and 4: The exponents are not marked, so the printed lines read as false arithmetic: 'r(γ−1) = 80.4 = 2.297' and 'ργ = 21.4 = 2.639'. A student sees 80.4 = 2.297.
- ch 7 [low] Quiz Q4 and Q5 answers: Exponents are lost again: '100.4 = 2.512', '1/100.4', 'r0.4 = 3.031', 'ρ1.4 = 2.639'. On a phone these read as plain decimals.
- ch 7 [low] Section 4, MEP formula note: 'kPa = 103 Pa' is wrong as printed; it should be 10³ Pa. Similarly 'swept volume in m3' reads as m3, not cubic metres.
- ch 7 [low] Section 3, Diesel efficiency sentence: The bracket is printed as '((ργ − 1)/(γ(ρ − 1)))' with no superscript, so ργ looks like ρ×γ.
- ch 7 [low] Exam traps, third bullet: 'The cut-off ratio is V3/V2, not V4/V3' contradicts Section 4, where the dual cycle cut-off ratio is defined as ρ = V4/V3 because of the extra state point. The trap states a rule that is only true for the Diesel cycle.
- ch 7 [low] Figure caption and plot: The Diesel series with ρ = 2 is drawn from r = 1, where the cycle is impossible (the cut-off volume V3 = 2V2 exceeds V1 once r < ρ). The plot therefore shows negative and zero efficiencies at low r, which cannot happen in a real cycle.
- ch 8 [high] Section 3, figure spec (nested sets): The figure labels the fuel-air cycle item as 'Variable cp' and the air-standard item as 'Constant cp'. The rest of the chapter defines c_v and the table says 'constant c_v', so the figure names the wrong specific heat for an Otto cycle, where the constant-volume value c_v governs. A student memorising the figure will attach the wrong property to the cycle.
- ch 8 [low] Section 1, first and third paragraphs: The section says the fuel-air cycle 'keeps the same cycle shape' and then also says combustion is finite and the pressure rise is not instantaneous. Finite heat release is not constant-volume heat addition, so the cycle shape is not exactly the same as the air-standard Otto; the two statements pull against each other.
