# c-xr-u6: free-model run

- Book: `books/cse/c-xr/c-xr-u6.html`
- Status: ok
- Model calls so far: 30 (119,253 tokens in, 195,193 out), 6.4 minutes

## Checker

```
c-xr-u6.html: 7 chapters, 13316 words, 8 figures, 145 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, features paragraph on hands-free use: 'Hands-free use matters when the user is holding a tool or a patient' reads oddly: a user holds a tool, but does not hold a patient; a surgeon's hands are on or near a patient.
- ch 1 [low] Section 2, wireless displays sentence: The example says a tablet shows the overlay while the camera stands on a desk, 'so students pass it around'. If the camera is fixed on the desk, moving the tablet does not change the camera pose, so passing it around does not give new viewpoints. The wording can mislead a student about what the untethered display buys.
- ch 1 [low] Section 1, last line ('taxonomy of AR'): 'Taxonomy of AR' normally means the classification of AR display types (see-through, monitor, projection), not the three tests that define AR. A student may conflate the two.
- ch 2 [high] Section 2, brightness bullet: The reflect/transmit roles are swapped. In an optical see-through combiner the real light is transmitted through the mirror and the virtual light from the microdisplay is reflected off it, so each loses part of its light on its own path. As written ('reflects part of the real light and transmits part of the virtual light') the sentence is physically backwards and contradicts Section 1, which a student may memorise as fact.
- ch 2 [low] Section 1, optical see-through paragraph: 'The computer image is focused into the eye by a combiner' gives the focusing job to the combiner. A combiner is a mirror or waveguide; it overlays, it does not focus. The focusing/collimation is done by the lens optics in front of the microdisplay.
- ch 2 [low] Section 2, eye offset bullet: 'The eye sits a few centimetres behind and below the optics' overstates the distance. Eye relief on a beam-splitter or waveguide display is typically about 15–25 mm, i.e. one to two and a half centimetres, and this number matters when students size the eyebox.
- ch 2 [low] Figure and caption: The caption says monitor-based AR is the fourth case shown, but the tree has only three children (Optical, Video, Projection). A student reading the figure will look for a branch that is not there.
- ch 2 [low] Section 4, vergence–accommodation paragraph: This paragraph is placed inside the projection/choosing section, but it is a property of head-worn fixed-focus displays, not of projection (a projected image lies on the real surface, so accommodation and vergence agree). Sitting where it does, it reads as if it applies to all four routes.
- ch 2 [low] Section 2, 'No occlusion' bullet and Quiz Q3: 'A virtual object cannot hide a real one' and Q3's 'never hide' are stated absolutely, but the Beyond box then describes switchable liquid-crystal shutters and per-pixel dimming that do block real light exactly where the virtual object is drawn. The two statements sit badly together.
- ch 3 [low] Section 1, first bullet defining a fiducial marker: "a black square with a white border and an inner code" reads as if the white ring is the border of the pattern. In standard markers (ArUco/ARToolKit style) the thick black square ring is itself the border that gives the edges, the ID code sits inside that ring, and the white margin outside the ring is only a quiet zone for detection. A student can picture the layers in the wrong order.
- ch 3 [low] Section 1, formula and its meaning: The depth formula Z = f × W ÷ w is stated without its assumption: it holds when the marker face is parallel to the image plane. For a tilted marker the apparent width w shrinks by roughly cos of the tilt angle, so a student applying the formula to a slanted marker gets a distance that is too large.
- ch 3 [low] Section 1, bullet "Decompose H with camera intrinsics into pose R, t": Homography decomposition does not give a single pose. For a planar target the maths returns two candidate (R, t) solutions, and the tracker must pick one. Without this, a student wonders why the same marker sometimes flips or jumps.
- ch 4 [high] Section 3, table row for ARCore and ARKit, column 'Markers': The table says ARCore and ARKit find no markers. Both platforms do detect printed images and patterns: ARCore through Augmented Images, ARKit through image tracking configurations. This contradicts the chapter's own definition of a marker in the Exam traps ('a physical pattern in the world'), so a student reading both will be confused about whether image targets need Vuforia.
- ch 4 [high] Quiz Q7: The answer explains the repaint effect as if a model target were tracked by texture, saying 'feature matches weaken' and 'retrain on the new appearance'. A Vuforia model target is tracked from the 3D geometry taken from the CAD model (shape and edges), not mainly from surface texture. A colour change alone usually keeps tracking working.
- ch 4 [low] Section 3, bullet 'Depth: a per-pixel map from motion': The bullet list is shared by ARCore and ARKit, but a motion-derived depth map describes ARCore's Depth API. ARKit needs a LiDAR scanner or the front TrueDepth camera for scene depth, so the sentence overstates what every ARKit phone can do.
- ch 4 [low] Figure 'AR content pipeline': The arrows run model → import → SDK pose → anchor → build to phone, which mixes build-time steps (model, import, build) with runtime steps (pose, anchor) in one sequence. Read left to right it suggests the SDK pose comes once, before the build.
- ch 5 [low] Section 2 and Quiz Q2: Section 2 calls dwell a fallback to gaze-and-commit, but the Q2 answer lists dwell next to pinch and voice as a way to confirm intent, which reads as if dwell were an equal commit channel.
- ch 5 [low] Quiz Q5: The question asks for four feedback channels, but the answer mixes channels with states: 'hover highlight' and 'visible state change' are both visual feedback, so only three channels (visual, audio, haptic) are actually listed.
- ch 5 [low] Worked example 1, step 6: Raising the pinch confidence threshold would reduce grab trials called pinch (better precision) but also increase missed pinches (worse recall), so the advice is stated without that trade-off.
- ch 5 [low] Section 3, evaluation: 'Report the mean and the spread' leaves the spread undefined for a student writing an exam answer.
- ch 6 [low] Exam traps, third trap: The trap says a marker may be impossible in a sterile operating field, but skin fiducials are normally stuck on before the CT/MRI scan and stay on until surgery, so the student may think markers are placed during the sterile procedure.
- ch 6 [low] Quiz Q6: The answer says the field geometry is tracked. In broadcast graphics the field or pitch model is pre-calibrated once; what is tracked live is the camera pose, and sometimes the ball or players.
- ch 6 [low] Quiz Q1: The standard textbook definition asks for three things: real plus virtual combined, registered in 3D, and interactive in real time. The answer drops the word interactive, which is the part examiners look for.
- ch 7 [low] Exam traps, trap 1: The sentence 'a single-player game has neither' (persistence nor shared state) clashes with the chapter's own definition of persistence: a single-player game does keep its world state after you quit, through a save file. Read literally, the trap is wrong; only shared, cross-user persistence is missing.
- ch 7 [low] Section 3, the formula block: Only ttotal is stated to be in ms. The other three terms are added to it, so a student can lose marks by mixing seconds and milliseconds in the exam.
- ch 7 [low] Worked example 1, steps 1 to 6: Each step is numbered twice ('step 1: 1.'), which reads as a formatting slip in an otherwise clean solution.
