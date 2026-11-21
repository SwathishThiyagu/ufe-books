# ce-survey-u1: free-model run

- Book: `books/civil/ce-survey/ce-survey-u1.html`
- Status: ok
- Model calls so far: 31 (109,817 tokens in, 224,177 out), 9.3 minutes

## Checker

```
ce-survey-u1.html: 6 chapters, 12114 words, 7 figures, 122 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: note "noise" runs off the right edge; shorten it
- chapter 1: the figure cannot be drawn: tree is too wide (11 leaves); use fewer leaves or shorter labels
- chapter 1: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, two principles: The sentence says a second distance from another known point 'cuts that circle at one point'. Two circles with centres at the two known points generally intersect at two points, not one, so the geometry as stated is wrong and a student will believe two distances always give one answer.
- ch 1 [low] Quiz Q2, answer: The answer says the second independent measurement 'gives a unique position'. As with two distances, two loci can meet at two candidate positions, so 'unique' overstates it.
- ch 1 [low] Figure tree, 'By purpose' branch: The text lists six purpose classes (topographic, cadastral, engineering, control, hydrographic, astronomical) but the tree shows only four, so a reader may think the other two do not belong to the classification.
- ch 2 [high] Section 1, the tape example (100.05 m against a true 100.00 m): The deduction is backwards. A tape that reads 100.05 m for a true 100.00 m is reading too much, which happens when each tape length is shorter than its nominal value. So the tape is short, not long. A tape that is long under-reads. The sentence "the tape is long and over-reads" also contradicts the Q2 answer, where a tape 8 mm too long is correctly said to give readings that are short.
- ch 2 [high] Quiz Q6(a): A worn zero end used as the start mark is answered as a gross error, but Section 2 of the same chapter lists "its zero mark is worn" under instrumental systematic errors. The two statements conflict, and the standard classification is systematic: the worn end gives a constant offset on every measurement, so averaging cannot remove it.
- ch 2 [low] Quiz Q7: The answer gives e_S = 0.036 m and then writes the total as 100.00 ± 0.04 m. The two figures disagree in the last digit.
- ch 2 [low] Section 3, the accuracy/precision paragraph using readings 100.01 to 100.05 m: "The spread is a couple of centimetres" is loose: the readings span 4 cm (range), while the standard deviation is about 1.6 cm. A student may take "spread" to mean either.
- ch 3 [high] Exam traps, third bullet ('Scaling a sloping distance'): The sentence is self-contradictory and the student will get the wrong picture. A sheet carries only horizontal (plan) lengths, so a slope length cannot be 'taken off the sheet'. What actually overestimates the plan length is a slope distance measured in the field or on the ground and then fed into the RF as if it were horizontal. As written, the trap also muddles which quantity is too big.
- ch 3 [low] Section 2 (diagonal scale paragraph) and Quiz Q5: The text says the diagonal gives 'a hundredth of a division' and the answer says 'a hundredth of the base division'. 'Division' is undefined here: in a plain scale the left major division is split into 10 sub-divisions, and the diagonal splits each sub-division into 10 again. Unless the reader knows that 'division' means the major division, the fraction is off by ten.
- ch 3 [low] Exam traps, fourth bullet ('Mixing kilometres and centimetres'): 'Convert before dividing by M, never after' is stated as a hard rule, but converting after the division is equally correct (the worked example itself multiplies first and converts afterwards in part (a)). The real rule is only that both lengths must be in one unit inside the same expression.
- ch 4 [high] Section 3, UTM easting definition: The text says 'Easting is distance east of the zone's central meridian'. That is not the UTM easting. UTM adds a false easting of 500 000 m at the central meridian, so a point on the central meridian has easting 500 000 m, not 0 m. The chapter mentions the false northing but omits the false easting, so a student would get eastings wrong by 500 km (and points west of the central meridian, such as 80.27° E in zone 44 whose central meridian is 81° E, would come out negative).
- ch 4 [low] Section 3, latitude definition: 'Latitude φ (angle north or south of the equatorial plane)' does not say which line the angle is measured along. On a datum the angle is between the ellipsoid normal at the point and the equatorial plane (geodetic latitude); the angle of the radius vector from the earth's centre is a different quantity (geocentric latitude) and differs by up to about 0.2°.
- ch 4 [low] Section 3, UTM zone example: 'for example 44 N' reads like 44° N latitude, and a space before N makes it worse. The hemisphere letter must be tied to the zone, not to the northing.
- ch 4 [low] Exam traps, first bullet: 'many answers lose marks by adding N when it is negative' can be read as saying that adding N raises H. Adding a negative N lowers H; the error is using the wrong formula H = h + N instead of H = h − N.
- ch 5 [low] Section 2, offset booking rules: The chapter says an offset is booked as two numbers, chainage and length. That is true only for perpendicular offsets. For an oblique offset the angle it makes with the chain line is also needed, otherwise the offset cannot be plotted.
- ch 5 [low] Section 2, field-book rules: The vertical line in the field book is the chain line itself, not a divider with all chainages on one side and all offsets on the other. As written, a student will book every offset on the right and lose which side of the line the object lies on.
- ch 5 [low] Exam traps, second bullet: The bullet says to use the measured length 'in the temperature and sag formulas'. In the sag formula the length that enters the cube is the unsupported span l, not the measured length; only the temperature formula uses the measured length M.
- ch 5 [low] Lead and Beyond: EDM and GNSS are used without being expanded, and a reader meeting them for the first time on a phone will not know what they are.
- ch 6 [low] Section 1, last paragraph: "Coarse frequency gives the metre range" is confusing and close to reversed: the coarse (low) modulation frequency gives the long unambiguous range and resolves the whole cycles N, while the fine (high) frequency gives the fine reading. A student can read "metre range" as maximum range in metres.
- ch 6 [low] Section 1, after the phase formula: The sentence "λ = v/f is the modulation wavelength in air" repeats the meaning already given in the term list under the formula, so the reader meets the same definition twice in three lines.
- ch 6 [low] Section 2, accessory list: "Target plate: helps aim in reflectorless mode" is vague and slightly misleading. A target plate or reflective sheet is a physical surface fixed on the object so the beam returns well where the natural surface is poor, and plates with printed patterns are also used for aiming in prism work.
