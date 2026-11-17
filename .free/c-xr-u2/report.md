# c-xr-u2: free-model run

- Book: `work/claude_figs/c-xr-u2/tree/books/cse/c-xr/c-xr-u2.html`
- Status: ok
- Model calls so far: 35 (126,391 tokens in, 211,769 out), 6.9 minutes

## Checker

```
c-xr-u2.html: 7 chapters, 12696 words, 8 figures, 149 KB
OK
```

## For the reviewer

- chapter 6: the figure cannot be drawn: note "gaze" runs off the right edge; shorten it
- chapter 6: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, sentence before the measure list: "These numbers compare two devices:" introduces a list of measures, not numbers, and no two devices are named. A student looks for the two devices and does not find them.
- ch 1 [low] Section 4, step 4, and the figure caption: "feedback" appears without a definition, though the chapter defines every other term. A reader cannot tell whether it means haptic/force feedback or display feedback.
- ch 1 [low] Exam traps, trap 1: "a 6-DOF puck has six motions and often no useful button" is a shaky claim: many commercial 3D pucks carry several buttons. The point being made is only that DOF counts motions, not buttons.
- ch 1 [low] Exam traps, trap 2: "it has no absolute position to hand to a tracker" is confusing: the mouse is itself the input device, and 'hand to a tracker' suggests a separate tracker exists.
- ch 1 [low] Quiz Q5: Q5 repeats Worked example 2 with exactly the same numbers, so it tests memory of that example rather than application.
- ch 2 [low] Section 2, ultrasonic tracker: The text says three distances give position 'by triangulation'. Triangulation works from angles; positioning from measured distances is trilateration. The chapter itself uses 'ultrasonic trilateration' in the Beyond search terms, so a student meets two names for one idea.
- ch 2 [low] Section 1, what a tracker reports: 'A 3-DOF tracker reports orientation only' is stated as a definition. Orientation-only is the common case (a phone or cheap headset), but some 3-DOF trackers report position only, so the flat sentence can mislead.
- ch 2 [low] Section 2, magnetic tracker: 'AC and DC forms differ in pulse timing' is vague and slightly wrong: DC trackers use short current pulses so eddy currents die away before sampling, while AC trackers drive a continuous alternating field.
- ch 3 [high] Section 2, sticky finger bullet and the summary line after it: Sticky finger is described as a close-range technique, and the summary says it 'favour[s] small nearby targets'. In the standard description the user points with the finger at an object, often far away; the object nearest the finger line sticks to it and can then be pulled to the hand. It is a pointing technique for distant or small targets, not close work. The stated failure ('grabs the wrong neighbour') should be tied to objects that lie close together along the pointing direction.
- ch 3 [low] Section 2, occlusion bullet: 'The object hidden from the camera is selected' is ambiguous. Any object behind another is also hidden from the camera, and the same bullet lists overlapping objects as the failure case. A student can read the definition as the opposite of what is meant.
- ch 3 [low] Section 1, paragraph after the travel/wayfinding definition: The sentence 'Some syllabi call this navigation and manipulation interfaces or pair it with gesture interfaces' repeats the chapter title and the word 'this' has no clear referent (the travel/wayfinding split? navigation?). It reads as filler and can confuse.
- ch 3 [low] Section 2, Go-Go bullet, and worked example: The formula virtual = D + k(d − D) with constant k is a simplified linear form. The original Go-Go mapping grows faster than linear above the threshold (the gain itself increases with d). The chapter uses its own model consistently and the arithmetic is correct, but a student may believe the linear form is the standard one.
- ch 4 [high] Figure, node a: The note says 'one per finger joint', but Section 4 says a common glove has 10 sensors, about two per finger, while the hand has 14 finger joints plus metacarpals. A student will read this as one sensor covering every joint, which is exactly the mistake the first exam trap warns against.
- ch 4 [low] Worked example 1, part (d), steps 6 and output: The enter and leave thresholds are placed exactly at the jitter limits (143° and 137°). A finger held near 140° still reaches those values, so the event can still repeat now and then.
- ch 4 [low] Section 3 and the figure: Section 3 lists segment and extract features between calibration and classification, but the pipeline figure jumps straight from 'Calibrate to range' to 'Classify gesture', so the figure and the text describe different pipelines.
- ch 5 [high] Worked example 1, step 3 and answer: The scenario says one camera loses 5 markers, then counts those markers as lost 3D samples (300). A marker is triangulated from at least two views, which the chapter states in Section 1. With 12 cameras, one camera losing sight of a marker does not lose that marker's 3D sample at all, so the correct count for that setup is zero. As written, the example teaches the opposite of the triangulation rule.
- ch 5 [low] Section 1, first paragraph: It says the compact state is 'joint angles plus a root position'. The root of a body skeleton needs both position and orientation (6 degrees of freedom); calling it only a position is incomplete and will confuse students when a character turns on the spot with no change in pelvis location.
- ch 6 [high] Section 2, cameras and depth sensors: Front-face headset cameras do inside-out tracking (the cameras look out at the world). 'Outside-in' is the opposite arrangement, where fixed external cameras or base stations look at the headset. The sentence reverses the standard meaning and will confuse students about tracking types.
- ch 6 [low] Figure (tree spec): The tree does not match Section 3. 'Inertial' is noted only 'accel + gyro' although Section 1 puts the magnetometer (heading) in the inertial group, and 'Physiological' is noted only 'gaze' although EMG is the main physiological sensor listed. Touch and flex are labelled 'Environmental' while the chapter's only truly environmental sensor, temperature, is left out.
- ch 6 [low] Section 3, gaze tracking: Saying the vector between pupil centre and corneal spot 'gives gaze direction' hides the calibration step. That vector shifts with head position and eye geometry, so the raw vector is not gaze direction until the system is calibrated for that user.
- ch 7 [high] Section 2, first line (and Section 1 last line): Section 1 defines outside-in as sensors sitting in the room and looking at the headset. Section 2 then calls Lighthouse "outside-in optical timing", but in Lighthouse the base stations only emit beams and the photodiodes are on the headset, so by the chapter's own definition it is not outside-in. A student cannot tell which definition to use, and this contradicts how the rest of the paragraph describes the hardware.
- ch 7 [high] Section 2, paragraph 2 and Lead: "Angles from both stations plus known station geometry fix the 6-DOF pose" and "angles from two stations give 6-DOF pose" are wrong. Each station's X and Y sweeps give two angles from one photodiode, which is a direction, so two stations intersect two rays and fix one point in 3-D. A single photodiode therefore gives position only; orientation needs several photodiodes at known offsets on the headset.
- ch 7 [low] Section 1, sign convention sentence: Positive yaw left and positive pitch up match a right-handed set with x right, y up, z pointing back. In that same set positive roll about the front-to-back axis tilts the top of the head to the left, not to the right, so the stated roll sign is inconsistent with the two signs next to it.
