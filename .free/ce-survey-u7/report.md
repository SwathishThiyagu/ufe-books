# ce-survey-u7: free-model run

- Book: `books/civil/ce-survey/ce-survey-u7.html`
- Status: ok
- Model calls so far: 19 (64,364 tokens in, 131,448 out), 4.7 minutes

## Checker

```
ce-survey-u7.html: 6 chapters, 11246 words, 7 figures, 123 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, last paragraph: The sentence 'The second word is the one to defend in an exam, because the data is geospatial and the machine only helps' is muddled and will mislead. In 'Geographic Information System' the second word is 'Information', and the reason given ('the data is geospatial and the machine only helps') actually argues for the third word, 'System'. A student repeating this in an exam will write a wrong justification.
- ch 1 [low] Worked example 1, steps 3 to 5: The streets are stored as centre lines. Erasing a 0.300 m band along each water main cuts the street line only where the two coincide, so a street that does carry a main can still leave surviving fragments beyond the erased point and appear in the answer list. The example quietly treats 'streets left over' as whole streets.
- ch 1 [low] Quiz Q6: The answer lists 'people' as missing, but the question says a team owns the images, program and plotter, so people already exist. What is really absent for that component is trained staff with defined roles, not people as such.
- ch 2 [high] Worked example 1, step 3 and the answer (also conflicts with exam trap 4 and Quiz Q5): The chapter defines 'all wells inside ward 7' as a spatial query that tests geometry (exam trap 4, Quiz Q5). The worked example then answers it by testing the stored ward field ('Ward 1 has 7; Ward 2 has 7'), which is an attribute query, not a geometric test. A student cannot tell which rule applies, and step 3 never uses the eastings and northings at all.
- ch 2 [low] Figure spec, easting row: The easting row carries an accent mark on column 1 ('marks': {'0': 'accent'}), but the caption says only the depth cells are marked (the wells deeper than 60 m). The stray highlight has no stated meaning and is on a spatial row, which is exactly the confusion trap 1 warns about.
- ch 2 [low] Worked example 1, steps 1-5: The steps do not follow the order of the question parts. Part (a) (measurement scales) is answered in step 4, after the two queries in steps 2 and 3, and step 1 only restates the given depths. The reader has to jump around to match steps to parts.
- ch 3 [low] Quiz Q4: The answer writes 4 000 000 bytes = 4 MB exactly, but 1 MB is 1 048 576 bytes in the binary convention used by most GIS software, so 4 000 000 bytes is about 3.8 MiB. Section 2 was careful to say 'about 1 MB'; the quiz is not.
- ch 3 [low] Quiz Q5: The answer says proximity 'uses exact coordinates and topology'. Buffers and distance queries are computed from coordinates alone; topology is what gives adjacency, shared boundaries and network tracing, and a 100 m buffer would work on a vector layer with no topology built.
- ch 3 [low] Section 3, comparison table, Storage row: The vector cell gives a qualitative statement ('Small for sparse data') while the raster cell gives a formula ('Rows × columns × bits per cell ÷ 8'). The two halves of the row do not compare the same kind of thing.
- ch 3 [low] Exam traps, second bullet: 'Do not draw a polygon over a raster class and call that area' is easy to misread; a student may take it as a ban on converting raster classes to polygons, which is a normal operation.
- ch 4 [low] Section 2 (Remove slivers) and Quiz Q2: The clause "left in place it steals area from one side and adds it to the other" describes a transfer of area between the two neighbours. A sliver is a separate thin polygon sitting between two boundaries that should coincide; it holds a strip that belongs to neither neighbour, so both neighbours lose area to it and the layer's total area is inflated. The quiz answer repeats the same wrong transfer picture, which a student could carry into an overlay exercise.
- ch 4 [low] Section 1, georeferencing paragraph: "Four points allow an affine fit" is misleading about the minimum: an affine transformation has six unknowns (two shifts, two scales, two rotations/shears), so three control points already give a unique exact fit. Four points give a redundant least-squares affine fit.
- ch 4 [low] Quiz Q4: The answer presents dangle and undershoot as if they were separate kinds of error. The free endpoint left by an undershoot is itself a dangling node in the topology, so a student may think an undershoot does not show up as a dangle.
- ch 5 [low] figure: The bottom stack item is labelled 'Earth surface' but its note is 'geoid, mean sea level'. The geoid is not the ground surface; the section text itself keeps the geoid, the ellipsoid and the real terrain as three different surfaces, so the figure contradicts it.
- ch 5 [low] section 2, worked example 1 step 4, quiz Q4: The scale factor 0.9996 converts an ellipsoid distance to a grid distance. The chapter applies it directly to a 'ground line' (a distance measured on the terrain), skipping the reduction of the ground length to the ellipsoid. For most sites the difference is a few centimetres per kilometre, but the wording teaches the wrong step.
- ch 5 [low] exam traps, last point: 'A mirrored southern-hemisphere grid' is not what happens. Without the false northing, southern-hemisphere northings are simply negative numbers; nothing is mirrored.
- ch 6 [high] Section 1, area rules (last sentence): The sentence 'A flood layer intersected with a ward layer is smaller than either input' contradicts the rule given just before it, intersect area ≤ smaller input. The intersection can equal the smaller layer (a flood polygon lying wholly inside one ward gives an intersection exactly equal to the flood layer), so 'smaller than either input' is false.
- ch 6 [high] Section 2, aspect formula: The sign convention is wrong. With x east and y north, the steepest-descent (downhill) vector is (−∂z/∂x, −∂z/∂y). The printed form atan2(−∂z/∂y, ∂z/∂x) has the east component's sign flipped, so it returns a mirrored direction. Example: a plane rising towards the east (∂z/∂x > 0, ∂z/∂y = 0) faces downhill to the west, but the formula returns zero (north).
- ch 6 [low] Section 2, slope formula: arctan returns radians, but slope in GIS is normally reported in degrees or percent. A student who uses the formula as printed will report slope in radians.
- ch 6 [low] Section 1, point-in-polygon: 'joins the point's attributes to it' does not say which way the attributes travel. A reader cannot tell whether the point gets the polygon's attributes or the polygon gets the point's.
- ch 6 [low] Section 2, local operation: 'Local computes each cell from the same cell' can be read as 'a cell computed from itself', which would change nothing. The intended meaning is the same cell position across input layers.
- ch 6 [low] Section 3, spatial correlation: Moran's I measures spatial autocorrelation of one variable (whether nearby units have similar values), not whether high values of one layer sit with high values of a different layer. Listing it beside 'plot the pairs and use correlation' blurs the two ideas.
- ch 6 [low] Section 3, examples of correlation: 'high population with many children is positive' is close to a tautology, since children are part of the population, so it teaches nothing about reading the sign of a correlation.
