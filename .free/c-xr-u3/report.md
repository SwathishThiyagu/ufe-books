# c-xr-u3: free-model run

- Book: `work/claude_figs/c-xr-u3/tree/books/cse/c-xr/c-xr-u3.html`
- Status: ok
- Model calls so far: 47 (176,109 tokens in, 281,806 out), 7.8 minutes

## Checker

```
c-xr-u3.html: 8 chapters, 14594 words, 9 figures, 166 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: tree is too wide (5 leaves); use fewer leaves or shorter labels
- chapter 6: the figure cannot be drawn: tree is too wide (5 leaves); use fewer leaves or shorter labels
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Worked example 1, step 2: The stereo monitor is listed in the options as 'one user, no head motion', yet step 2 uses it for requirement (a), which is six students viewing one walkthrough together. This contradicts the chapter's own selection number for simultaneous users, the figure (many viewers → large display such as CAVE or dome) and step 4 of Section 4. A six-person walkthrough is not satisfied by a one-user device.
- ch 1 [high] Worked example 1, step 3: Step 3 says 'Requirement (b) needs head motion and fine stereo', but requirement (b) in the question is fine stereo work at a desk with no head motion; head motion belongs to requirement (c), the surgical rehearsal. The HMD is justified with the wrong requirement.
- ch 1 [low] Section 3: The heading says 'Weighted scoring in four steps', but five bullets are listed (list requirements, remove failed candidates, assign weights, score each candidate, compute S). Students counting the steps will be confused, and the exam may ask for the steps by number.
- ch 1 [low] Section 1: 'as 3D sound displays explains' and 'as haptic displays explains' are ungrammatical and read as broken cross-references; the chapter name is used as if it were a singular subject.
- ch 1 [low] Figure: All three branches out of the root are labelled with the same edge text 'yes', so the tree suggests a viewer can take three mutually exclusive branches at once and the labels carry no information.
- ch 2 [high] Quiz Q7: The answer says both oculomotor cues are 'missing' in a photograph. They are not missing: the viewer's eyes still converge and accommodate, but they do so on the flat print at its true distance, so they signal 'flat' and contradict the pictorial depth cues. The answer also ignores motion parallax, which a still photograph does not provide.
- ch 2 [high] Figure caption: 'Only retinal disparity needs two eyes' is wrong: convergence is also a two-eye cue (accommodation is the one-eye oculomotor cue). A student revising from the caption will classify convergence as usable with one eye.
- ch 2 [low] Figure spec: The Monocular branch shows only occlusion, relative size and motion parallax, while the text lists seven monocular cues. A student revising from the figure loses perspective, shading and texture gradient.
- ch 3 [low] Section 1, second paragraph: "For a phone held 10 cm from a magnifying viewer" is ambiguous. It reads as if the phone is 10 cm from the person, but the point being made is the phone's distance behind the lens, which sets u in the lens formula.
- ch 3 [low] Section 1, definition of p and the formula box: The pitch is defined in millimetres ("0.25 mm pitch") but the formula box defines p in metres. A student can plug p = 0.25 straight into p/d and get an answer 1000 times too large. The conversion is shown in the worked numbers but never stated as a rule.
- ch 3 [low] Section 2, first paragraph: "The eye is relaxed when focusing at about 1 to 3 m or beyond" overstates relaxation. An emmetropic eye is fully relaxed (zero accommodation) only at optical infinity; at 1 m it still accommodates about 1 dioptre. The claim contradicts the standard accommodation treatment students meet elsewhere.
- ch 4 [high] Section 1, the sentence beginning "Read the sign": The condition is garbled: "If Z crossed:" is not a condition a student can follow, and the next clause jumps straight to the crossed case without saying Z < D. Since the whole sign convention of the chapter hinges on this sentence, a reader can easily take away the wrong rule.
- ch 4 [low] Worked example 1, step 4: "Two frames for the same eye are one slot apart on either side" is ambiguous — it can be read as 8.33 ms, and "on either side" has no clear referent.
- ch 5 [high] Quiz Q7 (and the matching sentence in Section 3, 'Audio-visual sync is tolerant to tens of milliseconds'): The answer 'No, 80 ms is too large and will be noticed' contradicts the standard lip-sync tolerance, which is asymmetric: viewers notice audio that leads the picture by more than about 45 ms, but tolerate audio that lags the picture by up to about 125 ms. An 80 ms audio lag therefore falls inside the usual broadcast tolerance and is normally not noticed, so the model answer taught to students is wrong.
- ch 5 [low] Section 2, the sentence after the ITD formula: The text fixes the ear spacing at d = 0.175 m and then says the maximum ITD is 'often quoted as about 0.7 ms'. A student who puts θ = 90° into the given formula gets 0.175/343 = 0.51 ms, not 0.7 ms, and will think the formula or the number is wrong.
- ch 5 [low] Figure 'From source to perceived direction': The arrows put 'ITD 0.26 ms' and 'ILD few dB' before the 'HRTF filter' box, so it reads as if the ITD and ILD values are inputs to the HRTF filter. In a binaural renderer it is the other way round: the HRTF filter is what creates the ITD, the ILD and the spectral notches in the two ear signals.
- ch 6 [low] Section 2, vibrotactile paragraph: "ERM and LRA units often run at 100 Hz to 300 Hz with amplitudes of a few µm to hundreds of µm, and update at about 1 kHz" can be read as saying the motor itself responds at 1 kHz. An ERM cannot follow amplitude commands that fast; 1 kHz is the rate of the rendering/control loop, and the mechanical bandwidth of an ERM is far lower (tens of hertz).
- ch 6 [low] Section 2, surface haptics paragraph: "a lateral force of a few mN" understates friction-modulated touchscreens and is vague; readers may think a touchscreen can only produce a barely noticeable push.
- ch 6 [low] Section 3, table: The "Typical maximum" column mixes units (N, N·m, m, mN, °C) and contains the word "large" for the motion platform, so the column cannot be compared or used in a numerical question.
- ch 7 [high] Quiz Q3 (answer): The answer says 'Roughly five times more pins are driven than the skin can resolve'. Pin count scales as 1/pitch², so dropping from a 10 mm palm pitch to a 2 mm pitch multiplies the number of pins by about 25 over the same area, not by 5. The factor 5 is only the ratio along one side. The statement also contradicts the chapter's own formula and worked example, where halving the pitch quadrupled the pin count.
- ch 7 [low] Worked example 1, step 5 and answer: A 5 mm palm pitch is called 'matched to the palm's coarser threshold', but Section 2 states the palm two-point threshold is about 10 mm and gives the rule pitch ≈ threshold, 'around 10 mm for a palm patch'. A student cannot tell whether the palm pitch should be 5 mm or 10 mm, and 5 mm pins are themselves closer than the palm threshold.
- ch 7 [low] Section 2, note under the pin-count formula: 'the +1 counts the pin at each end of that side' reads as if two pins are added, while the formula adds only one. With 5 intervals the 6 pins are the 5 interval points plus the one starting pin.
- ch 8 [high] Section 3, force scaling formula line: The comparison operator has dropped out: the text reads 'α  1 for a tiny surgical tool.', so the student cannot tell whether the scale factor should be below or above 1. This is the one worked guidance on choosing α, and as printed it says nothing.
- ch 8 [low] Figure, node c: The force label uses the symbol xd, which is never defined anywhere in the chapter; the text defines the wall surface position as x_wall. The label also drops the damping term, so it does not match the law in Section 1.
- ch 8 [low] Section 3, architectures paragraph: The name is ambiguous. The architecture described is 'master sends position, slave returns measured force', which most texts call position-force (or force reflection); calling it force-position suggests the opposite flow, master force to slave position.
