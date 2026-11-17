# c-xr-u1: free-model run

- Book: `work/claude_figs/c-xr-u1/tree/books/cse/c-xr/c-xr-u1.html`
- Status: ok
- Model calls so far: 35 (132,149 tokens in, 192,345 out), 7.2 minutes

## Checker

```
c-xr-u1.html: 6 chapters, 11755 words, 7 figures, 133 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2 (last paragraph) and the figure caption: It says 'AR and VR are two ends of one line' and captions AR and VR as 'the two ends'. This contradicts the same section, which correctly puts the real environment at the left end and the virtual environment at the right end. AR sits near the real end; it is not an end of the line. A student could reproduce this wrong statement in an exam.
- ch 1 [low] Section 1, AR definition: 'Lays virtual content over a live view of the real world' reads as if a camera view is always required. In optical see-through AR the user looks straight through the glass and there is no camera image on a screen.
- ch 2 [high] Section 3, paragraph 3 (and the Wave 3 bullet): The sentence 'From 2016, inside-out tracking placed cameras on the headset itself, so the headset watched the room and needed no external boxes' follows the 2016 shop-shelf paragraph, so a student will conclude the 2016 consumer headsets had no external trackers. They did: the Rift used external cameras and the Vive used base stations. Inside-out tracking existed in some 2016 devices and became standard a few years later.
- ch 2 [high] Quiz Q6: The answer says the 2016 wave 'had a low entry price'. The 2016 consumer headsets were expensive compared with the 1995 Virtual Boy; the cheap entry into VR came from the 2014 phone-based viewers, not from the 2016 headsets. The cost comparison in the answer is backwards.
- ch 2 [low] Section 2, NASA VIEW paragraph: The sentence lists three items (head-mounted display, glove, head tracking) but then says 'all four parts of 1.5 together'. A student counts three and is confused.
- ch 2 [low] Section 1, first sentence: Wheatstone's 1838 stereoscope was a table-top instrument using mirrors, not a box held to the eyes; the hand-held lens stereoscope is Brewster's later design. The sentence names the wrong physical form for the device it is describing.
- ch 2 [low] Section 2, Sutherland 1968 paragraph, and the first exam trap: 'The first head-mounted display that was tracked' is slightly strong. Head-mounted displays with head tracking existed before 1968 (helicopter and military work in the early 1960s); what Sutherland's rig first did was combine head tracking with a computer-generated view.
- ch 3 [high] Lead, Section 1 first line, Quiz Q1 answer: Immersion is defined as 'the feeling of being inside the virtual world', which is the definition of presence. Two paragraphs later the chapter correctly says immersion is a system property and presence is the user's feeling. A student who memorises the first definition and the quiz answer will contradict the rest of the chapter and the standard textbooks.
- ch 3 [low] Figure caption, Section 1: The caption says immersion is on the system side, but Section 1 says mental immersion comes from the story, the task and engagement, which are content. The figure then disagrees with the text.
- ch 3 [low] Worked example 1, step 5: 'Hand and head disagree' points at the wrong conflict. The mismatch that causes sickness in head-lag is between the eyes (the late image) and the inner ear (the true head motion). The hands are not involved.
- ch 3 [low] Quiz Q5: The answer blames imagination for the missing task, but Section 1 lists 'a clear goal, a believable world, and a task that holds attention' as the source of mental immersion. A student cannot tell whether a missing task damages immersion or imagination.
- ch 3 [low] Lead: 'the first unit of most VR courses' is an unverifiable count of syllabi.
- ch 4 [low] Section 2 (frame budget paragraph), against Worked example 1: The text says 'All tracking, simulation and rendering for that frame must fit inside this budget', but the worked example has 2 ms simulation + 7 ms rendering + 4 ms tracker-to-display path = 13 ms, which is larger than the 11.1 ms budget, and still passes. A student will read this as a contradiction and may think the 11.1 ms budget is violated in a correct system.
- ch 4 [low] Section 1, second paragraph, last sentence: 'The loop from components is now closed' is unclear: 'components' has no meaning here and the reader cannot tell what was closed.
- ch 4 [low] Section 3, limits paragraph: 'A headset costs more than a monitor' is stated as a general fact but is not always true (a standalone headset can cost about the same as a mid-range monitor).
- ch 5 [low] worked example 1, step 5 and answer: Part (d) asks which part limits immersion, and the step names only the output part, but the justification then gives an input limitation (the 3-DoF tracker cannot sense position, so leaning forward does nothing). A student copying this cannot tell which single part the examiner wants, and the answer states 'output' while its own reasoning points at the tracker.
- ch 5 [low] lead: 'the human at the end of both' is ambiguous — both of what? The reader has to guess whether it means input and output, or sensing and stimulation.
- ch 5 [low] section 1: Output devices are said to stimulate the senses 'eyes, ears, skin and muscles'. Muscles are not a sense; the sense that force feedback drives is the position and movement sense (proprioception) built from receptors in muscles, tendons and joints.
- ch 5 [low] figure caption: The caption says the engine layer and the I/O hardware layer are the two the rest of the chapter names, but the chapter also names the content/application layer (training task, game, scene) and the runtime layer (tracking, rendering, drivers). The claim is not true as written.
- ch 6 [high] Quiz Q3 (and Section 1, Test 2): The quiz asks 'Why does VR not need SLAM while AR does?' and the answer states VR never has to know the room. Six-degree-of-freedom VR headsets without base stations (standalone and inside-out tracked ones) compute their own head pose with visual-inertial SLAM. What VR does not need is a map of the room or registration of content to real surfaces. A student who writes 'VR never uses SLAM' in an exam will be marked wrong.
- ch 6 [low] Section 1, 'The definition used in this chapter': The definition says MR anchors virtual objects to real surfaces and occludes them, but plain phone AR also anchors content to a detected plane (the table itself says AR knows 'a plane'). Anchoring alone therefore does not separate AR from MR, and a student may think it does.
- ch 6 [low] Section 3: The occlusion formula (hidden if z_v > z_r) is dropped in the middle of the content, interaction, mobility, cost and safety bullets, after Safety. It belongs with Test 3, where occlusion is explained. The section heading also omits mobility, which has its own bullet.
- ch 6 [low] Worked example 1, output line: The output gives bare numbers 0.3 and 0.15 without units, though the answer line carries metres.
- ch 6 [low] Quiz Q4 answer: 'it cannot run the test hidden if z_v > z_r' reads as broken English and can confuse a second-language reader.
- ch 6 [low] Section 3, Cost bullet: 'A headset with the depth sensing that MR occlusion needs costs the most of the three' is stated as a general rule, but some high-end VR headsets cost more than depth-sensing AR/MR headsets.
