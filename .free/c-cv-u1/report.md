# c-cv-u1: free-model run

- Book: `books/cse/c-cv/c-cv-u1.html`
- Status: ok
- Model calls so far: 33 (127,157 tokens in, 255,768 out), 6.7 minutes

## Checker

```
c-cv-u1.html: 9 chapters, 16874 words, 10 figures, 178 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, "Output tells the task apart" (and Exam traps, first bullet): The test contradicts itself. It says "If the output is a word, number, box, mask or motor command, the task is computer vision", then two lines later says "If the output is an image, call it processing." A segmentation mask is a binary image, so a student applying the chapter's own rule to a mask gets "image processing", while the chapter calls it vision. The medical row of the table ("lesion mask") and the sentence "'Mark the tumour region' is segmentation, a vision step" make the clash worse.
- ch 1 [low] Section 1, first paragraph: "Each number is a pixel, a brightness sample" defines a pixel as the number. A pixel is an element of the grid (a position); the number stored there is its intensity. The later line about a 24-bit RGB pixel carrying three bytes also sits badly with this, because then a pixel is three numbers, not one.
- ch 1 [low] Lead and Section 1: Abbreviations appear without being expanded: OCR in the lead, CT and MRI in Section 1, CCTV in the applications table. A second-language reader reading on a phone may not know them.
- ch 2 [low] Worked example 1, problem statement and step 5: The drive is called '4 GiB (sold as 4 GB)', but a pen drive sold as 4 GB holds 4×10⁹ bytes ≈ 3.73 GiB, not 4 GiB. A student may carry the wrong capacity to a real device and get a different frame count.
- ch 2 [low] Quiz Q2 answer: Typo with a missing space: 'Compressing earlierthrows away detail'.
- ch 2 [low] Section 2, last paragraph: 'Those two choices are resolution' is too loose. Sampling and quantization give two different resolutions, and the sentence does not name them.
- ch 2 [low] Whole chapter (Section 1, Section 2, Section 3, figure text): Spelling is mixed: 'color processing' and 'colour cast', 'colour transform' appear in the same chapter.
- ch 3 [low] Section 1 and Quiz Q1: The wording gives the pupil the active role ('the pupil is the aperture that controls how much light enters'), while the iris is described as opening or closing it. A student may write either as 'the part that controls light' and lose the mark. Strictly, the iris is the muscle that sets the pupil's diameter, and the pupil diameter sets the aperture.
- ch 3 [low] Section 3, worked example, Q3, Q4, Q6: The symbol I is called 'intensity' but is measured in cd/m², which is luminance. Textbooks use 'intensity' loosely; a student may carry the word 'intensity' into radiometric questions (W/m²) and be confused about units.
- ch 4 [high] Section 2: The units of R are inconsistent with the formula v ≈ R·E·t. If R is in volts per (W/m²) and E is in W/m², then R·E is in volts, and multiplying by t in seconds leaves an extra second — the equation would give volt-seconds, not volts.
- ch 4 [high] Quiz Q2: A flatbed scanner is listed as an application of the single-sensor arrangement. Flatbed scanners use a line sensor (a row of CCD or contact-image-sensor elements) swept across the page, not a single element. Drum scanners are the classic single-sensor example.
- ch 4 [low] Section 2: Saying the ADC samples 'at fixed positions' blurs the two jobs. In an array camera the spatial sampling positions are fixed by the sensor element spacing, not chosen by the ADC; the ADC mainly quantizes the already-sampled element voltages.
- ch 4 [low] Quiz Q5: 1,024,000 bytes is not really 1 MiB (1 MiB = 1,048,576 bytes); it is 1.024 MB decimal and about 0.977 MiB. The chapter is careful about MB versus MiB elsewhere, so this slips.
- ch 5 [low] Lead paragraph: "a point at camera position (X, Y, Z)" reads as if (X, Y, Z) is where the camera sits. In this chapter (X, Y, Z) are the coordinates of a scene point measured in the camera frame, and the camera is at the origin.
- ch 5 [low] Exam traps, third bullet (Units): The claim that mixing 50 mm with 0.5 m "gives a wrong v by 1000 times" is not what happens. The 1/u term becomes 1000 times too large, but the computed v itself does not come out 1000 times off: with f = 50 and u = 0.5 the equation gives 1/v = 1/50 - 1/0.5 = -1.98, so v = -0.505, a meaningless negative value, not 55.56 × 1000 mm.
- ch 6 [high] Exam traps, fourth bullet: The sentence about dividing the range into 2^b equal cells says the level count is 2^b + 1 "in the first convention", which contradicts the earlier definition. The first convention has 2^b levels, not 2^b + 1. The 2^b + 1 count only appears if you count cell boundaries in the second convention.
- ch 6 [high] Quiz Q3 answer: The statement "Nothing is destroyed; the identity is confused" is misleading. Aliasing is irreversible: the original high-frequency component is folded onto a lower frequency and cannot be recovered after sampling. Also, two sinusoids with frequencies differing by the sampling rate give identical samples only when amplitude and phase match appropriately.
- ch 6 [low] Section 4 and Worked example 2: The example uses 1 MB = 10^6 bytes, but many image-processing courses use 1 MB = 2^20 bytes. Under that common convention, 2 073 600 bytes is about 1.98 MB, not 2.07 MB, and 3 110 400 bytes is about 2.97 MB, not 3.11 MB.
- ch 6 [low] Quiz Q7 answer: The phrase "between the two conventions" is unclear; the comparison is between the 8-bit and 12-bit images. Also, with Δ = L/(2^b − 1), the step shrinks by 4095/255 ≈ 16.06, not exactly 16.
- ch 7 [high] Section 2, m-adjacency bullet, and Exam traps item 3: The formal rule is written as 'q ∈ ND(p) and N4(p) ∩ N4(q) is empty'. The standard definition requires the intersection to contain no pixels whose values are in V, not to be literally empty. In a grey-level or multi-valued image the two side pixels can exist with values outside V, and then the diagonal m-link is still allowed; the rule as written wrongly rejects it.
- ch 7 [low] Section 3, sentence before the worked example: 'None of these distances decides adjacency' contradicts the worked example and the quiz, where D4 = 1 is used to test 4-adjacency and D8 = 1 to test 8-adjacency. A student will not know which statement to trust.
- ch 7 [low] Worked example 1, step 5: Adjacency also requires both intensities to lie in V, but the example never states V or the pixel values, so 'they are 8-adjacent' is only a geometric statement, not the full definition given in Section 2.
- ch 7 [low] Section 2, boundary sentence, and Quiz Q7: 'At least one neighbour outside the region' does not say which neighbourhood. Most textbooks fix the 4-neighbourhood for the boundary, so the loose wording leaves the definition ambiguous.
- ch 8 [high] Section 2, mask definition: A mask is described as 0s and 1s (or 0 and 255). For an 8-bit grey image, bitwise AND with a 0/1 mask keeps only the least significant bit, so 200 AND 1 gives 0, not 200. That is not region selection and contradicts the next sentence about selecting a region.
- ch 8 [low] Section 2, code note: The note says Python's ~ works on integers and to keep values inside the bit width, but it does not warn that ~ is not a fixed-width 8-bit NOT. In Python ~200 is -201, not 55.
- ch 8 [low] Section 1, averaging paragraph: 'removes random noise' is too strong. Averaging M frames leaves noise variance σ²/M, so noise is reduced, not removed.
- ch 8 [low] Section 3, forward mapping: It says forward mapping leaves holes when the output grid is larger. A forward rotation by 30° also leaves holes when the output size is unchanged, as Q4 correctly says.
- ch 8 [low] Section 3, bilinear interpolation formula: The four neighbours f00, f10, f01, f11 are not defined by position. A student cannot apply the formula without knowing which neighbour is which.
- ch 9 [high] Figure 'RGB to HSI' (and its caption): The flow shows RGB → Max/min → Intensity, with the edge carrying the label 'average', and the caption says intensity comes from max and min. Intensity is the average of R, G and B; it cannot be obtained from max and min. A student reading the diagram would compute I = (max + min)/2, which is wrong. Only saturation and hue use max and min.
