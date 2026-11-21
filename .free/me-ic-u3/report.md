# me-ic-u3: free-model run

- Book: `work/me-ic-u3/tree/books/mech/me-ic/me-ic-u3.html`
- Status: ok
- Model calls so far: 30 (104,584 tokens in, 228,388 out), 6.8 minutes

## Checker

```
me-ic-u3.html: 9 chapters, 22154 words, 15 figures, 340 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, first paragraph: The motoring curve is defined as "the pressure with fuel but no ignition". Standard usage is the pressure trace recorded while the engine is turned over without combustion; the presence of fuel is not part of the definition, and a student may think fuel must always be in the charge when the motoring curve is taken.
- ch 1 [low] Section 2 and Exam traps, last bullet: Section 2 puts peak pressure at 10°–15° aTDC but the end of the main flame sweep at 40°–45° aTDC, while the trap says "peak pressure belongs to the end of flame propagation". The two statements pull against each other and a student can conclude that pressure peaks at 42° aTDC.
- ch 1 [low] Section 2, formula line: The symbol θ is first defined as crank position measured from TDC (negative before TDC), then reused in θ = 6 N t as a crank-angle interval. The same symbol for a position and a duration is confusing.
- ch 1 [low] Section 1, second paragraph: "A reaction zone perhaps a millimetre thick" states only the upper end. Flame-front thickness in SI engines is usually quoted as a fraction of a millimetre up to about a millimetre.
- ch 2 [low] Section 2, mass burning rate formula: The unburnt charge density just before the spark is given as roughly 10 to 15 kg/m³. In a naturally aspirated petrol engine the spark fires at about 10–15 bar and 600–700 K, so ρu = p/(RT) works out to roughly 5–8 kg/m³. The quoted range is high by about a factor of two and does not fit the plain naturally aspirated case the sentence describes.
- ch 2 [low] Section 1, comparison table and the ST ≈ SL + u′ formula: The table gives turbulent flame speed ST = 10 to 30 m/s, but the chapter's own model ST ≈ SL + u′ with a realistic engine turbulence intensity u′ of 1 to 2 m/s gives only about 2 to 3 m/s. A student who uses the formula and the table together gets answers two orders of magnitude apart. The 10–30 m/s figure is the apparent flame velocity seen from the cylinder head, which includes the unburnt gas being pushed ahead of the front, not the burning velocity relative to the unburnt gas.
- ch 2 [low] Section 3, first-law formula: The chapter works in bar per degree of crank angle, but the instantaneous formula is written as dp/dt in Pa/s, and no link between the two is given. A student cannot get from the heat release formula to a dp/dθ value without knowing the conversion.
- ch 2 [low] Worked example 1 and figure: The illustrative pressures (30 bar at 10° aTDC rising to 60 bar at 25° aTDC) keep climbing well past the usual peak location of about 15° aTDC, and their average slope of 2 bar/°CA over 15° equals the peak value quoted in Section 3 ('about 1 to 2 bar/°CA'). The arithmetic is right, but the numbers describe an unrealistically late, very fast burn.
- ch 4 [low] Lead: The opening definition 'Abnormal combustion is any burning that does not follow the spark-plug flame front' is too broad and can mislead. In ordinary knock, most of the charge still burns normally from the spark flame front; only the end gas burns abnormally. A student may conclude that in knock nothing burns from the plug.
- ch 4 [low] Section 2 (knock paragraph): The chapter presents knock only as a petrol-engine event ('You meet it in petrol engines ...'). Compression-ignition engines also knock, from a long ignition delay and a sudden pressure rise, and students often lose marks by writing 'knock occurs only in SI engines'.
- ch 5 [high] Section 1, mixture strength paragraph: The numbers and the description contradict each other and the chapter's own definition of φ. With φ = (F/A) ÷ (F/A)stoich, a value of 0.85 is a lean mixture (85 % of the stoichiometric fuel-air ratio), not rich. So "φ = 0.85 to 1.0, that is, slightly rich to stoichiometric" is wrong, and it also clashes with the exam trap that says knock is worst at a slightly rich mixture. Standard textbooks place maximum knock on the rich side of stoichiometric.
- ch 5 [low] Section 1, first line of mixture strength paragraph: "Mixture strength is the ratio of fuel to air" is loose. Mixture strength normally means how the actual fuel-air ratio compares with the stoichiometric one, which is exactly the equivalence ratio defined in the next sentence, so the sentence is circular.
- ch 6 [low] Section 1, ignition delay definition: The sentence 'the delay ends when heat release becomes visible on the pressure trace' is imprecise: heat release is not directly visible on a pressure trace, and a student may confuse the pressure trace with a heat-release curve.
- ch 6 [low] Section 2, stage list: 'The third is the main phase and controls torque' is imprecise. Torque is set mainly by the fuel quantity; the main phase releases most of the heat and does most of the work.
- ch 6 [low] Section 3, engine speed bullet: The bullet says the same delay in milliseconds covers more crank degrees at higher speed, but it does not say that the delay in milliseconds itself usually falls as speed rises, so a student may misread it as a simple scaling rule.
- ch 6 [low] Quiz Q1: The answer gives ignition delay only as a time, but the chapter itself uses both milliseconds and crank degrees; the definition is incomplete for exam use.
- ch 7 [low] Section 1, last paragraph: The sentence 'Pre-ignition also starts before the spark' appears in a diesel-knock chapter with no subject or context, so a student may wrongly link pre-ignition to diesel knock.
- ch 7 [low] Section 2, 'Warmer intake air' bullet: The heading says intake air, but a glow plug heats the air inside the combustion chamber near the injector, not the intake air. The two devices are grouped as if they do the same thing.
- ch 7 [low] Section 2, formula box: The constant 0.006 appears without explanation, so a student cannot check it or recall it in the exam.
- ch 7 [low] Section 2, opening list of factors: The list omits engine speed and load, yet the worked example shows delay in crank degrees grows with speed, so a student may think delay is independent of speed.
- ch 8 [low] Lead: The lead lists squish among the "large, organised rotations", but squish is a radial inward flow, not a rotation. Section 1 and exam trap 2 say exactly the opposite, so the first sentence a student reads contradicts the rest of the chapter.
- ch 8 [low] Section 3, squish paragraph: The sentence "Some syllabi call squish flow by that name" says nothing: it names squish flow as squish flow. The same point was already made correctly in Section 1.
- ch 8 [low] Section 2, Section 3 and Beyond: Cross-references ("See Chapter 3.8", "See Chapter 3.2", "see Unit 6", "see Unit 4") are plain text, so a student reading on a phone cannot tap through to the linked chapter as the book format requires.
- ch 9 [high] Section 2, hemispherical chamber bullet: It says the hemispherical chamber has "the largest surface area, so heat loss and unburnt hydrocarbon are higher". This contradicts the standard textbook result: for a given clearance volume a dome has the smallest surface-to-volume ratio of the three shapes, so it has the least heat loss and the best thermal efficiency. A student who writes the chapter's version in an exam loses marks.
- ch 9 [low] Section 3, last paragraph: "Some syllabi call indirect injection IDI" is redundant and slightly confusing: IDI is already defined in the heading and used throughout the section, so a reader wonders whether it is a different thing.
- ch 9 [low] Worked example 1, step 7: Saying "a bowl that fills about 61 % of the clearance volume is normal for DI" is misleading. In a real DI engine the bowl is nearly the whole clearance volume; the rest is only the thin squish gap, so 61 % is on the low side.
- ch 9 [low] Worked example 2, step 5: "A shallow bowl holds the same fraction here as a deeper bowl of smaller diameter" is a coincidence of the two sets of numbers, because the clearance volumes differ (70 cm³ against 55 cm³). As written it reads like a general rule.

## Correction pass (Claude, 21 Nov 2026)

- New chapter 3.3 "Gasoline fuel properties and cycle-to-cycle variations" (exam course topic); later chapters moved to 3.4–3.9.
- Every chapter rewritten from the draft; every example recomputed. Pressure traces, heat release and IMEP values come from a single-zone first-law model of two engines (SI 86 × 86 mm, r = 9; CI 100 × 110 mm, r = 17) in pipeline/claude_figs/me_ic_u3.py.
- Reviewer flags fixed: motoring curve definition; stage II ends at peak pressure; ρu at the spark (about 6 kg/m³) versus mid-burn (12–13); laminar, turbulent and flame-travel speeds separated; φ = 0.85 is lean and knock is worst near φ ≈ 1.1; CI knock mentioned; delay versus speed and injection timing; glow plug versus intake heater; squish not a rotation; hemispherical chamber has the lowest S/V (now with a worked comparison).
- Nine hand-drawn figures; twelve long questions with full model answers; cross-references by topic; MIT link dropped.
