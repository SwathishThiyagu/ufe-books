# c-graphics-u1: free-model run

- Book: `books/cse/c-graphics/c-graphics-u1.html`
- Status: ok
- Model calls so far: 47 (182,436 tokens in, 326,363 out), 9.7 minutes

## Checker

```
c-graphics-u1.html: 9 chapters, 16542 words, 10 figures, 182 KB
OK
```

## For the reviewer

- chapter 1: the figure cannot be drawn: note "UI and games" runs off the right edge; shorten it
- chapter 4: the figure cannot be drawn: tree is too wide (9 leaves); use fewer leaves or shorter labels
- chapter 1: the figure could not be drawn; a plain box diagram stands in for it
- chapter 4: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1, step 6: The justification says the CPU cannot push about 373 MB per second. That rate (373 MB/s) is well inside what a phone CPU and memory bus can move, so the sentence is technically wrong and a student may repeat it as a hard limit.
- ch 1 [low] Figure caption (Section 3 figure): The caption says maps 'start from measured data', but Section 3 describes a metro map as authored vector data (lines, stations, labels), not measured data. This contradicts the text and can confuse the model-versus-measurement distinction.
- ch 1 [low] Section 2, GPU paragraph: 'Many small cores that colour vertices and fragments' is imprecise. The vertex stage computes positions and attributes; only the fragment (pixel) stage produces colours.
- ch 1 [low] Quiz Q7 answer: Segmenting the scan is image processing (finding the tumour region in the captured data), not modelling. Listing it under 'Modelling' blurs the graphics versus image processing line the chapter sets up.
- ch 2 [high] Section 1, bit depth paragraph: The exponents have lost their superscripts, so the text reads '28 = 256' and '224 = 16,777,216'. Taken literally these are false equations and a student will misread the formula for the number of colour values.
- ch 2 [high] Section 1, memory calculation sentence: 'At 106 bytes per MB this is 6.22 MB' drops the exponent: 10⁶ bytes per MB is meant, and '106' is a wrong number that also makes the division wrong.
- ch 2 [low] Section 1, memory calculation sentence: Only the decimal megabyte is given, but many phones and file managers report memory in binary units, so the same 6,220,800 bytes appears as about 5.93 MB and the student thinks a step is wrong.
- ch 3 [low] Section 1, refresh rate definition: "60 Hz means 60 passes per second" can be misread as 60 scan lines per second, since a 'pass' is not a defined term.
- ch 3 [low] Section 1, interlacing: "It halves the signal rate" does not say what it is halved compared with, and 'combing' is really a de-interlacing artefact; the artefact of interlacing itself on motion is edge jaggedness (interline twitter).
- ch 3 [low] Section 1, retrace: Only vertical retrace is named. The beam also has to fly back from the end of each scan line to the start of the next, and students meet this 'horizontal retrace' (and blanking) in exam questions.
- ch 3 [low] Section 1, frame size sentence: 'Frame size' is used loosely for what the formula actually gives: the size of the frame buffer in bytes, not the size of the frame in pixels.
- ch 4 [low] Quiz Q5 answer: It says the two colours are 'equally bright' because both have V = 0.7843. V is only the largest channel value, not perceived brightness. Two colours with the same V can look very different in lightness, so a student may generalise 'same V = same brightness'.
- ch 4 [low] Lead paragraph: It says 'CMY stores the three inks a printer lays down', but the chapter itself explains that printers use four inks (CMYK). A student skimming the lead may think a printer uses only three.
- ch 4 [low] Chapter title vs body: The title spells the word 'Color' while the whole body uses 'colour'. Mixed spelling looks careless in an exam answer.
- ch 5 [high] lead: The lead says vertices are pushed through a 'fixed pipeline'. That is the name of the old fixed-function pipeline, which section 3 says modern core-profile OpenGL removed. A student reading the lead will expect the opposite of what the chapter teaches.
- ch 5 [high] section 3: 'their layout in a vertex array object (VAO), both in GPU memory' is wrong. A VAO is not a data buffer and has no vertex data of its own; it records which buffers are bound and how the attributes are laid out. Only the VBO (and similar buffers) hold data in GPU memory.
- ch 5 [low] section 2 and figure: The text lists eight stages (including clipping and the per-fragment depth/stencil tests) but the figure claims six and drops clipping and the tests. The two contradict each other.
- ch 5 [low] section 2 pipeline list: 'The fragment shader runs per fragment and returns its colour and depth' is misleading. By default the fragment shader outputs colour only; the depth value is interpolated from the vertices by the rasterizer (a shader can override it with gl_FragDepth, but that is not the normal case).
- ch 5 [low] section 2 pipeline list: 'Tests for depth, stencil and blending discard or merge fragments' puts blending in the same bracket as the tests. Depth and stencil are tests that accept or reject a fragment; blending is a merge operation applied to fragments that pass.
- ch 5 [low] worked example 1, step 1: The rule x_screen = 200x is presented as the mapping into the viewport, but OpenGL's actual normalised-device-coordinate to window mapping is x_window = (x_ndc + 1) × width/2, because NDC runs from −1 to +1. A student may memorise the wrong transform.
- ch 6 [low] Section 2 (pseudo code): The pseudo code block ends with an empty '[shown output]' placeholder, so the reader sees a routine with no sample result to check against. A student cannot tell what the routine prints for a sample input.
- ch 6 [low] Exam traps (third bullet) and Section 3: The trap 'Forgetting to plot the final endpoint. The loop stops at x = x₁, and the last pixel is (x₁, y₁)' is confusing as written: in the pseudo code given, plot(x, y) sits inside the loop, so (x₁, y₁) is always plotted and the 'forgotten endpoint' case cannot arise. A student may think the printed algorithm has a bug.
- ch 7 [low] Section 1, heading and second paragraph: The heading says 'compute one octant, copy seven times' but the body says 'Compute one octant and copy it eight times'. A student cannot tell whether the octant is drawn 7 or 8 times.
- ch 7 [low] Worked example 1, step 8 and answer: The list called 'first-octant pixels' ends at (6,5), but there x = 6 is greater than y = 5, so that point lies past the octant boundary (r/√2 ≈ 5.66). It is only the last loop step, and its eight symmetric copies are exactly the pixels already plotted from (5,6), so it adds nothing new. As written it contradicts the chapter's own definition of the octant and can confuse a student checking the list.
- ch 7 [low] Exam traps, second trap: 'if you continue to x = r you draw each octant pixel twice' is vague: what actually happens is that steps past x = y lie in the next octant, and their eight symmetric copies land on pixels already plotted, so pixels are redrawn rather than new arc being covered.
- ch 8 [low] Figure (Filled pixels of the trapezoid): The figure is titled as the filled pixels of the whole trapezoid, but only rows y=2 to y=6 are shown. The polygon also covers y=1: both slanted edges start there, so the span runs from x=1 to x=9 and, under the chapter's own inclusive rule, 9 pixels would be filled at y=1 (y=7 has no crossings because the top edge is horizontal and the slanted edges end there). A student may conclude the polygon has no row at y=1.
- ch 8 [low] Section 2, edge-intersection formula: The formula divides by (y₁ − y₀) without saying that it is undefined when y₁ = y₀. The exclusion of horizontal edges is only mentioned two bullets later, so a student can apply the formula to a horizontal edge and get a division by zero.
- ch 8 [low] Quiz Q7: The question says 'A boundary is 4-connected but has a one-pixel diagonal gap'. These two statements contradict each other: a one-pixel diagonal gap is exactly a place where the boundary is not 4-connected, so the setup is confusing even though the answer given is correct.
- ch 9 [low] Section 1: The grey-level range is written as "0 to 2b − 1", with no exponent on 2. Read literally, 2b − 1 for b = 8 gives 15, which contradicts the next sentence (0 to 255).
- ch 9 [low] Section 1, reconstruction sentence: "a larger pixel looks smoother but hides detail" can mislead. Bigger pixels on a display look more blocky, not smoother. The sentence is about the size of the reconstruction spot over which a sample is spread.
