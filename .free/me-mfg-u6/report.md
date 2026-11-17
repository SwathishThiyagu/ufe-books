# me-mfg-u6: free-model run

- Book: `books/mech/me-mfg/me-mfg-u6.html`
- Status: problems
- Model calls so far: 35 (138,507 tokens in, 256,947 out), 6.0 minutes

## Checker

```
me-mfg-u6.html: 7 chapters, 15048 words, 8 figures, 152 KB
PROBLEMS:
 - chapter "abrasive-water-jet-machining": 1938 words is too long (keep under 1900; 900-1600 is the target)
```

## For the reviewer

- checker: chapter "abrasive-water-jet-machining": 1938 words is too long (keep under 1900; 900-1600 is the target)

## Reviewer notes (after any revision)

- ch 1 [high] Exam traps, last bullet: The trap ends with 'that is why the tape, not the tool, set the pace of an NC shop.' This reverses the chapter's own argument, and the worked example: the reader is idle 99 % of the time because the cutter is slow, so the tool sets the pace and the tape does not. A student reading this will learn the opposite of the correct conclusion.
- ch 1 [low] Section 1 and Quiz Q1: Section 1 says the classic NC chain has four parts: tape reader, MCU, axis drives and a feedback device (if fitted). Q1's answer gives tape reader, MCU, axis drives and 'the slide with its leadscrew', and then adds the feedback device as an extra. The text and the model answer list different four parts.
- ch 1 [low] Worked example 1, step 4 (and Quiz Q3): The step says 'idle percentage = idle time ÷ total cycle time', but the denominator used is 25 s, which is only the machining time. The cycle is reading plus machining = 0.2 + 25 = 25.2 s, so by the stated formula the answer is 24.8 ÷ 25.2 = 98.4 %, not 99.2 %. Q3 has the same slip (19.8 ÷ 20.2 = 98.0 %, not 99.0 %).
- ch 1 [low] Section 2, paragraph after the bullet list: 'In hard-wired NC each one would have needed new hardware, so none of them existed' contradicts the earlier statement in Section 1 that a canned cycle in hard-wired NC 'needed new boards'. It also overstates the case: simple fixed cycles and tool offsets did exist on some hard-wired controls, wired in as hardware.
- ch 1 [low] Section 3, opening paragraph: The instruction 'State which one you mean.' sits inside the definition text, and the two definitions (Direct … and Distributed …) run together with no line break, so the reader sees a single dense block.
- ch 1 [low] Quiz Q6, answer: 'the wrong revision is not loaded from a operator's pen drive' — wrong article, and the phrasing is clumsy.
- ch 2 [low] Section 1, paragraph on the machining centre: The sentence 'the table carries the work in X and Y' is correct for a vertical machining centre but wrong for a horizontal one. On a horizontal machining centre the table normally gives X (and often Z), while Y is the vertical movement of the spindle head on the column.
- ch 2 [low] Section 2, first paragraph: 'must not deflect more than a few micrometres' is tighter than a general-purpose machine tool. A machining centre with a stiffness of about 100–200 N/µm deflects roughly 5–10 µm under a 1 kN cut; a few micrometres is a precision-machine figure.
- ch 3 [high] Quiz Q6: The question states as fact that 'contouring needs a sampled interpolator but point-to-point does not'. That is wrong on both sides. Contouring is regularly done with reference-pulse (incremental) interpolators driving steppers, as Section 3 itself says, and point-to-point servo drilling or punching tables commonly run a reference-word sampled position loop with no interpolation of a path. The real difference is coordination of the path, not sampled versus pulse.
- ch 3 [low] Worked example 1, steps 4 to 6: The machining time is rounded to 3.61 s and then reused, so the axis pulse rates come out as 1662 and 1108 pulses/s and the check gives 1998 pulses/s. The check is written as if it 'matches' 2000, but the 2 pulses/s gap is only rounding, which can puzzle a student who recomputes.
- ch 3 [low] Section 2, closed loop paragraph: The text says the position loop 'decides the following error' but never says what following error is, so the term arrives undefined.
- ch 4 [high] Section 3, Figure: The figure's directed edges run A(0,0) → B(80,0) → C(80,50) → D(0,50) → A, a counter-clockwise traversal, with the first move from A labelled G01 X80. The worked program traverses the same rectangle clockwise: N60 to X0 Y0, then N70 Y50, N80 X80, N90 Y0, N100 X0. Its first move from A is Y50, not X80. With the figure's counter-clockwise direction, G41 (left of travel) would put the tool centre inside the part, contradicting the caption that the tool runs 5 mm outside.
- ch 4 [low] Section 1, Block and word format: "R is a plane or cycle value" is vague. A student may read it as R selecting the working plane, which is done by G17/G18/G19, not R. R has two separate uses and neither is stated.
- ch 4 [low] Worked example 1, steps 3 to 5: The cutting time counts only the 300 mm offset rectangle. The program also has a lead-in from X-10 Y-10 to X0 Y0 (about 14.1 mm) and a lead-out back to X-10 Y-10 (about 14.1 mm), so the stated 2.00 min is not the full path time.
- ch 4 [low] Exam traps, third bullet: "A lathe feed of 150 means 150 mm per revolution" uses a value no lathe would run; a student may take 150 mm/rev as a normal turning feed.
- ch 5 [low] Lead: The lead says CAM decides where the 'tool centre' goes, but Section 1 correctly says the cutter location is the tool tip, not the tool centre or spindle face. Two different points in one chapter will confuse a student.
- ch 5 [low] Section 1: 'one file can be post-processed for a three-axis mill, a turning centre or another control' overstates neutrality. A CL file generated from a milling setup cannot be turned into lathe code; turning needs CL data written for a lathe (with tool-nose radius records).
- ch 5 [low] Section 2: The block marked [shown output] after the APT-like pseudo code is empty, so the reader never sees what the statements produce.
- ch 5 [low] Section 2: The block 'G01 X80.0 Y0.0 Z-3.0 F200' merges two separate CL moves into one three-axis block, which makes the tool ramp diagonally from (0,0,0) to (80,0,-3) instead of moving to X80 at Z0 and then plunging 3 mm. F200 is also never defined in the pseudo code.
- ch 5 [low] Section 2: C1 = CIRCLE/CENTER, P1, RADIUS, 25 is defined but never used by any motion statement, so a student cannot see why geometry statements exist.
- ch 5 [low] Section 3, formula: r_max = R_pocket − r_cutter holds only for a circular pocket; the surrounding text says 'for a pocket' in general, and a rectangular or contoured pocket has no R_pocket.
- ch 5 [low] Worked example 1 (code): n = int((R-r)//step) truncates. If (R-r) is not an exact multiple of the stepover, the last ring lands short of the wall and no finishing cut at the wall is counted, while the hand steps still claim the largest radius R-r.
- ch 5 [low] Figure, post-processor node: The note 'one machine type' is loose: a post-processor is written for a specific machine and control version, not a generic type.
- ch 6 [low] Section 3, die-sinking description: 'The tool electrode is a mirror shape of the cavity wanted' can mislead. The electrode is a positive replica of the cavity: the shape it has is the shape the cavity takes, not a reversed image.
- ch 6 [low] Section 3, overcut sentence: 'The cut is wider than the wire by the spark gap on each side; that extra width is the overcut' blurs radial overcut with total extra width. The quiz later uses overcut as the gap on one side (kerf = d + 2 × overcut), so the two statements look inconsistent.
- ch 6 [low] Section 2, energy per spark formula: E<sub>s</sub> = V<sub>g</sub> × I<sub>p</sub> × t<sub>on</sub> is only exact if voltage and current stay flat for the whole pulse. Real pulses rise and fall, so the value is an estimate.
- ch 6 [low] Quiz Q3, answer: 'f = 1 ÷ 200 × 10⁻⁶' read left to right gives 5 × 10⁻⁹, not 5000. The missing brackets invite a calculation slip.
- ch 6 [low] Quiz Q4, answer: 'The machine can only arc or do nothing' is loose. With an insulating work plate no spark and no arc can strike at all, and the servo, seeing open-circuit gap voltage, keeps feeding the electrode down until it touches the glass.
- ch 7 [high] Section 1, and repeated in Quiz Q3: The taper direction is stated wrongly. The chapter says the top of the kerf is narrower than the bottom because the jet spreads and widens the cut. In metals cut by AWJ the entry kerf is normally wider than the exit kerf: the energy of the jet falls as it goes deeper, so only the central, high-speed core still erodes material, and the cut narrows with depth. The spreading of the jet is a small effect compared with this loss of erosive power.
- ch 7 [high] Section 2 table, row 'Traverse rate': The stated effect is backwards. Increasing traverse rate makes the jet dwell less, so the cut gets shallower, the lag increases, the taper gets worse and the cut face gets rougher. It does not give 'less taper, better finish'.
- ch 7 [high] Quiz Q7 (question statement and answer): The premise 'Increasing traverse rate improves finish but reduces depth of cut' is wrong. A faster traverse gives a rougher face and more taper, not a better finish. The rest of the answer (slow traverse gives full penetration, less taper, smoother face) is correct but contradicts the question.
- ch 7 [high] Figure, node 'Intensifier': The note 'smooths the flow' gives the intensifier the job of the accumulator. The intensifier multiplies the pressure; the gas-charged accumulator is what absorbs the pulses and steadies the flow, as Section 2 and Quiz Q1 both say.
- ch 7 [low] Section 2, safety paragraph: 'Water is incompressible, so the stored energy at these pressures is enormous' is self-contradictory: a truly incompressible liquid would store no energy. The danger comes from the high pressure itself, the small compression of water, and the gas charge in the accumulator.
- ch 7 [low] Lead versus Section 3: The lead says 'there is no cutting force' while the advantages list says 'Very small cutting force on the work'. The jet does exert a small force.
- ch 7 [low] Quiz Q1: The question asks for 'the two components that raise and then smooth the water pressure', but the answer correctly names three (pump, intensifier, accumulator). A student cannot tell which two are wanted.
- ch 7 [low] Section 1, cut face paragraph: 'no burr of the welded kind lasering produces' is awkward and unclear, and 'lasering' is not a standard term.
