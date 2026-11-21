# ce-survey-u2: free-model run

- Book: `books/civil/ce-survey/ce-survey-u2.html`
- Status: ok
- Model calls so far: 24 (93,190 tokens in, 235,454 out), 9.0 minutes

## Checker

```
ce-survey-u2.html: 6 chapters, 12573 words, 7 figures, 131 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3: The back-bearing formula is garbled and its second case is missing entirely: the text reads 'BB = FB + 180° if FB  180°'. A student cannot tell what happens when FB is larger than 180°, which is exactly the case tested in worked example 1 and quiz Q4.
- ch 1 [high] Quiz Q2 answer: The model answer repeats the same broken formula, 'BB = FB + 180° if FB  180°', so an examiner marking by this key would accept an incomplete relation and a student revising from it learns only half the rule.
- ch 1 [low] Section 1: 'An azimuth is the same angle measured clockwise from a north reference' is loose: a bearing may be a reduced bearing measured from the nearer end of the meridian, which is not the same angle as a clockwise azimuth from north.
- ch 1 [low] Section 3: The declination rule is given only as an arithmetic sign. A student can apply it but cannot check it, because the chapter never says that for east declination the magnetic bearing is smaller than the true bearing, so the true meridian lies to the west of magnetic north.
- ch 2 [high] Section 2, the FB = BB ± 180° formula line: The rule that tells the reader which sign to use is cut off: it reads "use + when BB  180°." The two cases are missing, so a student cannot apply the formula and may add 180° to a bearing over 180° and get a value above 360°.
- ch 2 [low] Figure node f (back-check note) and Quiz Q2 answer: "FB − BB = 180°" is not true as written: the difference is +180° for one direction of travel and −180° for the other, so the line fails its own check half the time. The chapter text itself uses the magnitude in worked example 1, step 1.
- ch 2 [low] Quiz Q4 answer: The reasoning calls the result "the interior angle" although PQ and PR do not form a polygon; a student may carry the polygon rule to a case where there is no inside or outside.
- ch 3 [high] Lead (opening paragraph): It says plane tabling 'suits small-scale maps'. That is the opposite of the standard textbook position: the method is used for large-scale, detailed plotting of small areas. Small-scale maps of large extents are exactly what plane tabling is not suited for, because precision falls and the sheet gets crowded.
- ch 3 [high] Worked example 1, step 1 (and steps 3 and 5, which reuse the symbol): Step 1 calls 210° the 'plotted true bearing' and names it θ_true. The data is a magnetic bearing, since it is being compared with a trough-compass needle reading. Comparing a needle reading with a true bearing ignores magnetic declination and teaches the wrong idea.
- ch 3 [high] Quiz Q5 (answer): The answer says the three rays 'become nearly parallel'. On the danger circle they do not become parallel: when P, A, B, C are concyclic, the three rays drawn on the sheet are concurrent for every orientation of the table. That is precisely why no triangle of error appears and the orientation error cannot be detected. The phrase 'does not define a unique point' is also loose — the rays do meet at a point, but the point drifts with the unknown orientation.
- ch 3 [low] Section 4, resection paragraph: It says the fix 'is weak' on the danger circle. It is stronger than weak: the resection is indeterminate there, so the plot may come out of the field wrong without any warning sign.
- ch 3 [low] Section 4, two-point problem sentence: 'an auxiliary point or a previously plotted line' is vague. In the two-point problem you occupy an auxiliary station whose position is found first, and only two known points are on the sheet.
- ch 4 [low] Section 3, first paragraph after the coordinates: The sentence 'Coordinates come from those sums' suggests the column totals give the coordinates. The totals are only the closure check; coordinates come from adding each line's latitude and departure in turn.
- ch 4 [low] Section 3, open traverse sentence: The chapter lists a link traverse as a third type, but Section 3 only says an open traverse has no closure check. A student may conclude a link traverse is also unchecked, though it can be checked against the known end station.
- ch 4 [low] Section 2, example line at 135°: The line length 180 m appears for the first time inside the calculation ('180 cos 135°') without being stated in the sentence.
- ch 5 [high] Section 3 (omitted measurements): The quadrant for the recovered bearing is taken 'from the signs' of ΣL_known and ΣD_known, but the actual components of the missing line are l cos θ = −ΣL_known and l sin θ = −ΣD_known. Using the signs of the known sums puts the bearing 180° wrong whenever those sums are negative. Example: ΣL_known = −0.34 m, ΣD_known = −0.19 m gives a line in the north-east quadrant (tan θ = 0.559, θ = 29.2°), but 'signs of ΣL, ΣD' would put it south-west at 209°.
- ch 5 [high] Section 3, last paragraph: The claim 'If two lengths or two bearings are missing, the two closing equations are not enough' is false. With two unknown lengths (bearings known) the two closing conditions are two linear equations in the two lengths and solve directly; with two unknown bearings (lengths known) they solve as two simultaneous equations for the unknown directions. Two omitted quantities on different lines are standard solvable cases, not cases needing extra data.
- ch 5 [low] Figure and its caption: In the figure A′ is drawn at (0.3, 3), i.e. due east of A at (0, 3), while the worked example puts A′ south-west of A (bearing 209°). A student matching the picture to the numbers will be confused about the quadrant.
- ch 5 [low] Worked example 1, step 3 and answer line: 766 ÷ 0.3895 = 1966.6, so 1966 is truncated, and to three significant figures 1966.6 rounds to 1970, not 1960. The example and the answer therefore state a slightly wrong relative precision.
- ch 5 [low] Section 2, after the Bowditch formulas: 'Then add the adjusted parts station by station' is vague; the reader is not told what is being added to what.
- ch 6 [low] Section 1, table instructions vs the figure: The text tells the student to make a table with five columns — E, N, next N, previous N, and the product — but the figure shows only three columns (E, N, product). A student copying the figure cannot see which next and previous northings produced each product, which is the one thing the table is meant to make visible.
- ch 6 [low] Quiz Q3 answer: At corner A the substitution is written as 0 × (30 − 0), but the rule is E × (N_next − N_prev) and at A the next northing is N_B = 0 and the previous is N_C = 30, so the bracket must be (0 − 30). The value is still 0, so the area is right, but the shown order of subtraction is reversed and a student will copy it.
- ch 6 [low] Section 2, DMD sentence: DMD is called 'the older name for the same job', but double meridian distance is a quantity used inside the DMD method, not a name for a method, and it is never defined. The double-area relation is also stated before the reader knows what DMD means.
- ch 6 [low] Lead: 'Multiply each easting by the change in northing' can be read as the northing change along the line, N_next − N_i, whereas the formula uses N_next − N_prev, the difference between the corners on either side of the corner being processed.
