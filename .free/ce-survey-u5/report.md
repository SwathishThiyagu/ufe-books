# ce-survey-u5: free-model run

- Book: `books/civil/ce-survey/ce-survey-u5.html`
- Status: ok
- Model calls so far: 21 (71,554 tokens in, 149,409 out), 5.5 minutes

## Checker

```
ce-survey-u5.html: 7 chapters, 12136 words, 8 figures, 138 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, Working at the station, sixth bullet: It says 'Compute d = S sin z plus prism constant'. The prism constant is a correction to the measured slope distance, not to the horizontal distance. Applying it afterwards conflicts with Section 1, which correctly says the processor applies the prism constant first and then computes horizontal distance, and it gives the wrong reduction order (a student who copies this drifts from the textbook method, even though the numeric effect is small).
- ch 1 [low] Section 2, sixth bullet and the coordinate formula: The same symbol α is used twice for two different quantities: in the bullet it is the clockwise angle turned from the backsight, and in the formula box it is the azimuth (clockwise from north). A student reading on a phone can plug the raw backsight angle straight into sin α.
- ch 1 [low] Section 1, first paragraph: 'The telescope turns on a horizontal axis on a vertical axis' is ambiguous; it can be read as one axis mounted on the other in a single stack.
- ch 1 [low] Section 3, prism constant bullet: It says every distance shifts by the same amount, but Quiz Q6 correctly shows the horizontal shift is k sin z (about 29.9 mm for a 30 mm constant at z = 85°). The two statements disagree.
- ch 1 [low] Figure spec: The edge edm → prism is labelled 'out and back' (solid) and a second edge prism → edm is labelled 'return' (dashed). The travel is drawn twice and the arrows contradict each other.
- ch 1 [low] Section 1, EDM bullet and figure note: The EDM is described as 'timing' the return of a 'modulated light or microwave' beam. Total-station EDM normally resolves distance by comparing the phase of a modulated light (infrared or laser) beam; pulse timing is a separate, coarser method, and microwave EDM belongs to old separate tellurometers, not to total stations.
- ch 1 [low] Section 1 and worked example: The symbols ′ and ″ (minute and second of arc) are used throughout, for example 1″ and 85°00′00″, but are never defined for a reader meeting them first.
- ch 1 [low] Section 3, closing paragraph: The list of uses (cadastral, construction, tunnel, monitoring) repeats what the lead and Section 2 already say, and sits inside the errors section where it does not belong.
- ch 2 [high] Section 1, pseudorange formula and its symbol list: The formula and the definition of t_r contradict each other, so the bias is counted twice. The text defines t_r as 'the receive time by the receiver clock'. If t_r is the clock reading, then c(t_r − t_s) already contains the receiver clock bias, and adding c δt_r on top makes the pseudorange too long by a second time. The worked example and the exam trap ('a receiver clock ahead gives pseudoranges that are too long; subtract the error') use the correct physics, so a student who reads the formula literally will be confused about sign and size.
- ch 2 [low] Section 3, first paragraph: 'GNSS computes in WGS84' is too broad. Only GPS is defined in WGS84; GLONASS broadcasts in PZ-90 and Galileo in GTRF, and each receiver converts to a common frame for output.
- ch 3 [high] Quiz Q5 answer: The answer tells the student to raise the mask angle in a case where every satellite is low in the north. Raising the mask there deletes the only satellites available and makes HDOP worse. This directly contradicts Section 3 ('A high mask ... may remove spread and raise DOP') and contradicts the Q8 answer, which says a very high mask angle worsens a survey. A student writing 'raise the mask angle' in the exam would be marked down.
- ch 3 [low] Quiz Q5 answer: The sentence 'Low elevation raises noise and may raise VDOP' is misleading. Low elevation raises atmospheric and multipath noise, true, but it is the lack of elevation spread (all satellites at nearly the same u_z) that spoils VDOP. A low-elevation satellite mixed with high-elevation ones improves VDOP by separating height from the clock term.
- ch 3 [low] Worked example 1, steps 2 and 5: Section 1 defines the design matrix row as [-u_x, -u_y, -u_z, 1], but the worked example builds H from +u, e.g. H = [[0,1],[1,0]]. The answer is unchanged because a sign flip leaves HᵀH the same, but a student comparing the two will think one of them is wrong.
- ch 3 [low] Exam trap 1: 'DOP depends on angular spread, not height or signal strength' is ambiguous: 'height' can be read as the satellite's altitude above the ground, and elevation angle is itself part of the angular spread.
- ch 4 [low] Section 1: The line 'One pulse gives one point' contradicts Section 2, which says a discrete-return system records one or more returns (first, last, etc.). A student may think each pulse can only ever produce one point.
- ch 4 [low] Section 1, formula note: The formula uses c as the speed of light in vacuum, but the pulse actually travels through air, where the speed is slightly lower (about 0.03 %). The chapter never says this is an approximation.
- ch 4 [low] Section 2: 'scans buildings, slopes or plant' — 'plant' is ambiguous between vegetation and an industrial plant.
- ch 4 [low] Section 2 and Section 3: Cross-references to 5.5, Unit 6 and Unit 7 are plain text, so a reader on a phone cannot tap through to them.
- ch 5 [high] Section 1, multirotor description: Saying a multirotor "can carry a heavier payload" implies it out-lifts a fixed-wing. In general a fixed-wing drone carries more payload and flies far longer; the multirotor's real advantages are vertical take-off, hovering and precise slow flight.
- ch 5 [low] Figure, node 'dem': The note calls the DEM the "ground surface". In the section text a DEM is any elevation grid, a DSM includes buildings and trees, and only a DTM is bare ground. The note contradicts that.
- ch 5 [low] Beyond: PPK is used without being defined, while RTK is defined earlier.
- ch 6 [low] Quiz Q4: The answer says the peg "shifts mostly perpendicular to the sight", but 'the sight' could mean the backsight line A to B. The induced displacement is perpendicular to the line being laid out, A to the peg, not to the backsight sight.
- ch 6 [low] Section 2, field steps: The symbol β is first defined as the setting-out angle (target azimuth minus backsight azimuth) and then reused as 'set that direction as β = 0°', which reads as if β is now zero.
- ch 7 [low] Section 1 and Worked example 1: The formula defines d as the depth below the transducer, but the worked example calls the same 30.0 m the depth below the water surface, without adding the transducer draft. The transducer sits below the surface, so the two depths differ by that draft.
- ch 7 [low] Section 3, first paragraph: Azimuth is defined as 'the horizontal angle of a line from north'. The direction of measurement is missing, so a student may read it as a plain bearing.
- ch 7 [low] Section 2, last line: 'The chart is final.' is unclear; it does not say what is final or why.
- ch 7 [low] Section 1, last paragraph: The cross-reference to 5.4 LiDAR is written as plain text, so on the phone page it does not link to that chapter.
