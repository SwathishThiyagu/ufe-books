# ce-survey-u6: free-model run

- Book: `work/ce-survey-u6/tree/books/civil/ce-survey/ce-survey-u6.html`
- Status: ok
- Model calls so far: 25 (90,737 tokens in, 183,416 out), 7.4 minutes

## Checker

```
ce-survey-u6.html: 7 chapters, 21540 words, 9 figures, 210 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, last paragraph: The chapter calls 3–15 µm 'the window' for thermal sensing. There is no single atmospheric window running from 3 to 15 µm; water vapour and CO₂ absorb strongly between about 5 and 8 µm and beyond 14 µm. Calling the whole thermal band a window contradicts the 'atmospheric windows' idea used in the Beyond section.
- ch 1 [low] Quiz Q6 answer: A 5 µm photon is labelled 'likely thermal emission'. The 3–5 µm region (mid-infrared) receives both reflected sunlight and emitted radiation, so the answer is misleading for a student who later meets daytime mid-IR images.
- ch 1 [low] Exam traps, trap 4: 'The irradiance at a surface also depends on area and distance' is vague. A student can read it as 'irradiance grows with area', which is the reverse of the definition (irradiance = flux ÷ area).
- ch 1 [low] Exam traps, trap 1: 'An infrared photon is weaker than a visible photon even though infrared feels hot on the skin' can be misread as a statement about beam power, which the same trap is trying to separate from photon energy.
- ch 2 [low] Section 3, atmospheric windows table, mid-infrared row: The row gives the mid-infrared window as 3.5–5.5 µm. The window usually quoted is about 3–5 µm; beyond roughly 5 µm water-vapour absorption takes over (the strong 6.3 µm band), so 5.5 µm sits partly inside an absorption region.
- ch 2 [low] Worked example 1, part (b) and step 8: The example uses haze and then assumes the measured radiance simply halves. Section 4 of the same chapter says the sensor also receives path radiance L_p, and haze increases L_p. So under haze the measured radiance would be more than 12.5 W m⁻² sr⁻¹ and the drop would be less than half. As written, the example contradicts the path-radiance paragraph.
- ch 2 [low] Exam traps, first trap: 'Radiance changes with sun angle, haze and season; reflectance does not' is misleading. Reflectance is free of illumination and atmosphere effects, but it does change with season when the surface itself changes, for example crop growth or snow cover.
- ch 2 [low] Quiz Q4 and its answer: 'No operational sensor band centred on 1.4 µm' is too absolute. Some sensors carry a narrow band near 1.37 µm (for example the cirrus band of the Landsat 8/9 OLI series, 1.36–1.39 µm). It exists precisely because water vapour absorbs there, and it is used only for high-cloud and cirrus detection, not for surface study.
- ch 2 [low] Lead paragraph, last sentence: 'Every comparison of two dates and every classification depends on that conversion' is an overstatement. Classification can be run on calibrated radiance or even on raw digital numbers; reflectance is preferred, not compulsory.
- ch 3 [high] Section 1, second paragraph: It says 'the shortwave infrared is 0.7–2.5 µm'. Standard texts put NIR at about 0.7–1.3 µm and SWIR at about 1.3–2.5 µm, and the chapter itself later uses NIR as 0.7–1.1 µm. A student will be left not knowing where NIR ends and SWIR begins, and the soil and water discussion of features at 1.6 and 2.2 µm is then described as 'shortwave infrared' while the leaf plateau at 0.75–1.1 µm is called 'near-infrared', which contradicts the definition given here.
- ch 3 [low] Worked example 1, step 4 and answer: 'The crop value 0.67 is near +1' overstates the position. NDVI spans −1 to +1, so 0.67 is in the upper part of the range but not close to +1; a student may think 0.67 is a poor value and that only ~0.95 means vegetation.
- ch 3 [low] Section 1, last sentence: 'you classify in Chapter 6.7' names another chapter as plain text instead of a link, so the phone reader cannot jump to it.
- ch 4 [high] Lead, first paragraph: It says 'The sensor fixes the bands, the swath and the pixel size.' The ground pixel size does not belong to the sensor alone: it is the detector field of view multiplied by the platform height. The chapter itself uses p = θH in Worked example 1, where the same 6000-detector array gives 10 m at 600 km and 5 m at 300 km. A student who memorises the lead will write 'pixel size depends only on the sensor' in the exam and lose marks.
- ch 4 [low] Section 2, imaging geometry: 'The swath is the ground width seen at one instant' fits a pushbroom, whose whole line images at once. A whiskbroom sees only one pixel at an instant; its swath is built up over one full sweep of the mirror. The definition as written is loose for the whiskbroom case.
- ch 4 [low] Section 1, orbit paragraph: Inclination is defined as 'the angle between the orbital plane and the equator', but the sun-synchronous value quoted is 98°, which is more than 90°. With the definition given, a student cannot see how the angle exceeds 90°.
- ch 4 [low] Worked example 1, steps 3–5 and answer: Values are printed as 1.6666666666666667 × 10⁻⁵ rad and 16.666666666666668 µrad. The machine-length decimals hide the physical result and are hard to read on a phone.
- ch 4 [low] Quiz Q6 answer: The reason 'it views one hemisphere at fixed angles' is confused. For a given ground point a geostationary view angle never changes, which is an advantage, not a defect. The real limits are the 35,786 km range, which needs a very large aperture for fine pixels, and the poor view of latitudes near and beyond about 81°.
- ch 5 [low] Section 1 (GSD formula): The formula GSD = H × θ is written as exact, but it is the small-angle approximation tan θ ≈ θ. A student who later meets a large IFOV (wide-field sensor) will not know why the formula stops working, and nothing states that θ must be the angular size of one detector element.
- ch 5 [low] Section 1 (mixed pixel definition): 'When one pixel covers two covers, such as field and road' repeats the word 'cover' and reads as a typo; the meaning (two different land covers) is not immediate.
- ch 5 [low] Section 2 (ΔL formula notes): The note says '2ⁿ is the number of levels', but the formula divides by 2ⁿ − 1. The two numbers are different things (levels versus intervals between levels) and the mismatch is unexplained, so a student may think the formula has a typo.
- ch 5 [low] Figure and worked example 1: The figure pointer labels a bright 70-DN cell as 'field', while the text and quiz call the same cells 'bright cover'. Two names for one thing in a figure a student reads quickly.
- ch 5 [low] Quiz Q1 model answer: 'Ground area or ground length' leaves the student unsure which quantity is expected; the usual exam answer gives the ground area of one pixel, with the GSD in metres as its side length.
- ch 6 [low] Section 1, elements list (Size): "Size is the outline measured against the image scale" repeats the word "outline" already used for shape, so the student may think size and shape are the same element. Size is the measured extent of the object, not its outline.
- ch 6 [low] Section 3, scale paragraph: "Measure several known distances and average them if the photo is tilted" is misleading. On a tilted photo the scale changes from place to place, so a single averaged scale is wrong at most points; averaging only smooths random measurement error on a near-vertical photo.
- ch 6 [low] Figure (aria text): The second node is labelled "Shape, size, shadow" but the aria description says "then shape and shadow", so screen-reader users lose the size element that the visible figure shows.
- ch 6 [low] Exam traps, first trap: "Confirm the class from the sun-facing side" is vague. Shadows fall on the side away from the sun, and the interpreter should read the lit side of the object, not a "sun-facing" side.
- ch 7 [high] Exam traps, first trap: The sentence is self-contradictory and will be misread. If 95 per cent of the pixels called class A really are A (the diagonal cell), then most of another class has NOT been wrongly assigned to A — that would push the diagonal percentage down. What the trap means to say is the opposite: a class may be 95 per cent correct as a user's view while many of its own true pixels are labelled as another class, so its producer's accuracy is low.
- ch 7 [low] Section 3, NDVI formula note: 'water and cloud are negative' is too strong for cloud. Thick cloud is bright in both red and near-infrared, so its NDVI sits close to zero; only thin or thin-cirrus cloud and some shadowed cloud give clearly negative values. Water is genuinely negative (also snow and shadow).
- ch 7 [low] Section 2, spatial filter paragraph: With a 3 × 3 kernel of weight 1/9 the output averages the nine values in the window, including the centre pixel — not 'the nine neighbours', which reads as nine other pixels.
- ch 7 [low] Section 1, resampling: 'Bilinear interpolation averages four neighbours' hides the weighting. The four neighbours are weighted by distance from the output point, which is why the result is smoother than nearest neighbour.

## Claude correction pass (21 Nov 2026)

Every chapter was checked against the draft review notes above and every worked example, quiz and bank number was rerun in Python. All seven figures were redrawn by hand (pipeline/claude_figs/ce_survey_u6.py) from the chapters' own numbers, and every long question has a step-by-step model answer (331 to 501 words, each ending in a numerical check). All the review findings above are fixed. The unit is outside CE25C03 (no exam topics to add).

Changed or added worked examples:
- EMR and the spectrum: Wien's law added (sun 0.50 µm, earth 9.66 µm, fire 3.62 µm, energy ratio 19.4); band table fixed (NIR 0.7–1.3, SWIR 1.3–3, mid IR 3–8, TIR 8–14 µm); the 5 µm quiz answer now says reflected and emitted energy mix.
- Energy interactions: the draft's haze example halved the radiance and contradicted its own path-radiance paragraph; rebuilt with T = 0.9 and L<sub>p</sub> = 4.0 (sensor 22.0, uncorrected 0.173, corrected 0.157); mid-IR window 3–5 µm; 1.37 µm cirrus band.
- Spectral reflectance: NDVI of vegetation, soil and water read from the figure (0.818, 0.100, −0.333), plus the shaded crop showing why the ratio removes illumination.
- Platforms: orbital period example added (705 km: 98.9 min, 14.56 orbits, 2752 km track spacing; 35 786 km: 86 164 s); the tree figure that fell back to a box diagram replaced.
- Resolution: 8-bit vs 12-bit quantisation of two close fields (DN 128/128 vs 2049/2056); small-angle GSD and the 2ⁿ − 1 divisor explained.
- Visual interpretation: photo scale from focal length and flying height (1:20 000) and tower height from shadow (25.2 m); tilted-photo scale sentence corrected.
- Digital processing: error-matrix example with user's and producer's accuracy and kappa (0.830, κ = 0.725).

Not verified and therefore left out: sensor-specific resolutions and swaths other than Landsat 8 (705 km, 185 km, 16 days).
