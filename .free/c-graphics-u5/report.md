# c-graphics-u5: free-model run

- Book: `work/claude_figs/c-graphics-u5/tree/books/cse/c-graphics/c-graphics-u5.html`
- Status: ok
- Model calls so far: 41 (153,920 tokens in, 276,671 out), 6.4 minutes

## Checker

```
c-graphics-u5.html: 9 chapters, 16153 words, 10 figures, 198 KB
OK
```

## For the reviewer

- chapter 6: the figure cannot be drawn: tree is too wide (5 leaves); use fewer leaves or shorter labels
- chapter 4: the figure cannot be drawn: tree label "Animation techniques" is too long; shorten it
- chapter 4: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 2 [low] Section 3, shortest-rotation formula: The text says to wrap the difference into the range (−180°, 180°], but the given formula d = ((v₂ − v₁ + 180) mod 360) − 180 returns −180 for a half-turn (for example 0° to 180° gives −180) and never returns +180. So the stated range contradicts the formula.
- ch 2 [low] Section 2 and Exam traps: "Easing changes speed, never the path" is stated as an absolute. It holds only when the same easing is applied to every channel of one object. If x and y are eased with different curves (which the chapter itself allows, since each channel has its own keys and rule), the object does not travel the straight line between the two poses, so the spatial path does change.
- ch 2 [low] Quiz Q2: A hand reaching for a cup starts from rest and also slows as it arrives, so the motion is slow-in and slow-out. Ease-in alone explains only the start, and the question implies ease-in is the right single choice.
- ch 2 [low] Section 3, final sentence on export frame rate: "Exporting at a frame rate different from the timeline's silently changes how fast everything moves" is only true when keys are stored as frame numbers. Many tools store key times in seconds and resample on export, so the motion keeps its duration.
- ch 3 [high] Exam traps, third bullet: The claim that writing the weights as t and t 'doubles the brightness at mid-morph' is wrong. With weights t and t the sum is 2t, which equals 1 exactly at t = 0.5; so mid-morph is the one frame where brightness is correct, and the images darken near t = 0 and t = 1 instead.
- ch 3 [low] Worked example 1, step 5: 'The pencil' is a leftover word from a different example; no pencil exists in this morph. The step also says '70 px left of the target point' while ignoring the vertical offset: the point is 28 px above the target as well.
- ch 3 [low] Section 3, last paragraph: 'One subtraction, one multiply and one add per point' undercounts the arithmetic. Per coordinate the formula needs two multiplies, (1 − t)·P_A and t·P_B, and one add.
- ch 3 [low] Quiz Q6: The stated cause is poor correspondence, but the suggested check asks whether the warp and the dissolve use the same t, which tests a different fault (outline and colour drifting apart), not outline shivering.
- ch 3 [low] Section 3, paragraph on 3D vertex morphing: Says normals are interpolated by the same rule; a linearly interpolated normal is shorter than unit length in the middle frames, so lighting comes out slightly wrong unless it is renormalised after interpolation.
- ch 4 [low] Figure (tree) and Section 4: The tree puts 'Procedural' only under 3D, but the chapter itself treats procedural rules (for example the bobbing float h = A sin 2πft) as a way to drive any motion, 2D or 3D. The tree also mixes two different classifications in one split: 2D/3D are rendering techniques, while keyframe, procedural and mocap are motion drivers that cut across both.
- ch 4 [low] Exam traps, last bullet: 'Rendering is always last' contradicts the chapter's own tool list, where compositors combine renders with live plates after rendering. A student can read this as saying nothing happens after the render.
- ch 4 [low] Section 2, Lighting bullet: The bullet is named Lighting but also assigns camera placement, which is a separate job. Students revising stage order will think cameras are part of lighting.
- ch 4 [low] Worked example 2, step 3: 12.5 frames/s is an instant between two frames, so 'frame 12 or 13' is ambiguous and depends on whether frames are numbered from 0 or from 1. A student cannot tell which frame holds t = 0.5 s.
- ch 5 [low] Section 1: The term 'hot spot' is used without explanation, and a first-time reader may confuse it with a Wi-Fi hot spot.
- ch 5 [low] Section 3: 'Keyframe marks a change' is thin. Between two keyframes the tool calculates the in-between values, which is the whole reason keyframes are powerful; without that, a student reads keyframes as just bookmarks.
- ch 5 [low] Section 3: 'Instances' is used in 'all its instances update' but never defined; the cast/instance pair is the key idea of this metaphor.
- ch 5 [low] Section 2: 'Interactivity is expressed as control flow between icons, not as a button on a page' is too absolute. Icon tools also let an icon contain clickable buttons and hot spots that branch; the difference is that the branch is drawn in the flow, not that buttons are impossible.
- ch 6 [low] Section 1: The brush diameter d is introduced but then the sentence says the brush stamps colour into every pixel its path touches, which describes a zero-width path and leaves d unused. A brush of diameter d covers a disc of pixels around the path.
- ch 6 [low] Section 1: The sentence "Its corner radius cannot be changed afterwards" is confusing for ellipses and text, which have no corner radius at all, and it hides the general point that painted shapes cannot be re-edited.
- ch 6 [low] Exam traps, trap 1: "Resampling throws pixels away and does change it" is true only for downsampling. Upsampling creates new pixels and also changes the byte count, so the trap as written can make a student think all resampling reduces size.
- ch 6 [low] Exam traps, trap 3: "24-bit RGB and 8-bit indexed both hold one byte per channel or per palette index" is ambiguous: a 24-bit RGB pixel is 3 bytes, while an 8-bit indexed pixel is 1 byte. A student may take away the wrong byte count.
- ch 6 [low] Figure caption and Section 4 table: "The third changes the whole bitmap at once" conflicts with the table's own example, crop, which keeps part of the bitmap and discards the rest rather than changing the whole image.
- ch 7 [high] Section 1: The sentence 'painting black hides a blemish' reverses the mask action on a retouch layer: black hides the retouch, so the blemish becomes visible.
- ch 7 [high] Section 2: With the curves adjustment above the retouch layer, the layer directly below is the retouch layer. Clipping curves to the layer below makes it affect the retouch only, not avoid the retouch.
- ch 7 [high] Quiz Q5 and Exam traps: The claim that stacking bright layers sums values above 255 and clips is wrong for the chapter's normal alpha formula. Each normal composite is a weighted average of values already in 0–255, so it cannot overflow; clipping comes from additive blends or adjustments.
- ch 7 [low] Section 2: The unsharp-mask description stops at subtracting the blurred copy. That computes the high-pass edge signal, not the final sharpened image.
- ch 7 [low] Figure: The note 'mask hides blemishes' is misleading; the retouch hides the blemish, while the mask limits where the retouch is visible.
- ch 8 [low] Section 2, last sentence: The sentence 'The trade-off is more computation at render time, not more storage' overstates the case. For artwork with thousands of anchors (a detailed map or an illustration with heavy texture) the path data can be far bigger than a compressed raster of the same picture, so storage is sometimes a real cost.
- ch 8 [low] Quiz Q2, answer: The answer implies that filling requires the path to be closed. Most drawing software will fill an open path by treating it as if a straight line joined its two ends, so 'lets the interior be filled' is misleading as the main effect of closing.
- ch 8 [low] Section 1, sentence on clicking: 'Clicking with no drag gives a straight corner' is vague. A student may read 'straight corner' as a curve that happens to be straight, rather than a corner point that carries no handles.
- ch 9 [high] Quiz Q6: The answer 'ease-in is slower at midpoint, so blur is shorter there' is not generally true, and 'midpoint' is not defined. For a common quadratic ease-in (distance ∝ t²), the instantaneous speed at the time midpoint equals the average speed, so the blur there is the same as for the linear tween, not shorter. For other easing curves the mid-time blur can be shorter, equal or slightly longer than the linear value. A student who writes the given answer would be marked wrong by a careful examiner.
- ch 9 [low] Section 1: 'An empty keyframe starts a new object in that layer' is misleading. An empty (blank) keyframe holds nothing on the stage; the student then draws or places the new object in it.
- ch 9 [low] Figure: The Text lane shows only a shape-tween bar over frames 1 to 12, with no keyframe markers at either end, while the Ball lane shows keyframes. A student may conclude that a shape tween needs no keyframes.
