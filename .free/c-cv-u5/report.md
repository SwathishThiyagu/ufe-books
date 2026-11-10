# c-cv-u5: free-model run

- Book: `work/claude_figs/c-cv-u5/tree/books/cse/c-cv/c-cv-u5.html`
- Status: ok
- Model calls so far: 33 (126,683 tokens in, 215,378 out), 5.1 minutes

## Checker

```
c-cv-u5.html: 9 chapters, 16997 words, 10 figures, 196 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, the Harris response formula box: The stated unit of R is wrong. Ix and Iy are given in grey levels per pixel, so each entry of H is in (grey levels)² per pixel². Then det H and (trace H)² are both in (grey levels)⁴ per pixel⁴, and R = det H − k(trace H)² must carry the same unit. Writing it as 'grey levels squared per pixel squared' is the unit of H, not of R, and contradicts the very formula printed.
- ch 1 [low] Section 2, sentence after the table: The eigenvalues are called the 'average squared intensity change' along the principal directions, but they are an unnormalised sum over the window: in the worked example the four squared gradients add to λ = 16, and the average would be 4. The wording contradicts the example.
- ch 1 [low] Exam traps, last trap: The trap lumps two different mistakes together and gives one wrong consequence. A negative sign on k does make edges score as corners. But k only slightly outside 0.04–0.06, and especially a k that is too large, makes corners score negative (missed corners) rather than making edges score as corners. Only a k that is too small lets edges score positive.
- ch 2 [low] Section 1: Scale space and DoG keypoints: The sentence 'Each octave doubles σ and halves the image size' can be read as if σ doubles between the neighbouring scales inside one octave. Inside an octave, σ grows by the factor k = 2^(1/3); it is only from one octave to the next that σ doubles and the image is downsampled by 2.
- ch 2 [low] Section 2: Orientation and the 128-D SIFT descriptor: The patch size is never stated. A student cannot tell how big the 4×4 cell grid is on the image, which matters when reading implementations.
- ch 2 [low] Section 3: SURF: box filters and Haar wavelets: 'The longest sum vector gives the dominant direction' is vague: it does not say that SURF slides an angular window over the circular region and keeps the window whose summed response vector is longest.
- ch 2 [low] Section 4: Matching with the ratio test: 'See 5.4 for what comes next' is plain text, so it does not work as a cross-chapter link in the book.
- ch 3 [low] Exam traps, second bullet (170° bin): The clause 'With interpolation it also spills toward bin 1' contradicts the chapter's own bin layout. The chapter defines bin 9 as 160° ≤ θ < 180°, so its centre is 170°; a sample at exactly 170° sits at the centre of bin 9 and would not spill into bin 1 under linear interpolation. The spill only happens if bins are centred on 0°, 20°, …, 160° (the original paper's convention), which the chapter does not use.
- ch 3 [low] Worked example 1, answer: The example L2-normalizes a single cell histogram, so a student may conclude that HOG normalizes each cell on its own. The chapter itself says normalization is per block (four cells concatenated), so the example needs one line saying it is practising the norm step only.
- ch 3 [low] Section 1, bin definition: The bins are edge-aligned ((k−1)·20° ≤ θ < k·20°, so 0° is the lower edge of bin 1), while classic HOG implementations centre the bins on multiples of 20° (0°, 20°, …, 160°, with 0° and 180° sharing one bin). A student comparing with OpenCV or the original paper will see 0° land in a different bin.
- ch 4 [low] Section 3 (VLAD paragraph) and section heading 'a compact variant': VLAD is called 'compact', but the chapter itself says its vector has length k·d, which is 128 times longer than the k-length BoVW histogram it is compared with. A student will read 'compact' as 'shorter than BoVW' and then meet a number that contradicts it.
- ch 4 [low] Section 2, formula h_i = n_i / N: The claim 'The entries sum to 1' silently assumes the image gave at least one descriptor. A blank or very smooth image can detect zero keypoints, and then N = 0 and the division is undefined.
- ch 5 [high] Section 3 (distortion): The radial distortion formula u_undist = u·(1 + k1·r² + k2·r⁴) scales the absolute pixel coordinate about the pixel origin (0, 0), not about the principal point. Distortion is radial about (cx, cy), so as written the formula shifts every point sideways even when there is no distortion at the principal point.
- ch 5 [low] Section 3 (distortion): r² is defined as (u − cx)² + (v − cy)² "in normalized pixel units", which is contradictory: (u − cx) is in pixels, not normalized. Mixing pixel offsets with the k1, k2 polynomial makes the units of k1, k2 unclear.
- ch 5 [low] Figure (Pinhole projection): The figure shows an extrinsic step 'world to camera' for the point (1.0, 0.5, 2.0) m, but the caption and worked example treat that point as already in camera coordinates. A student may think an extra transform is being applied and wonder why the numbers still give (720, 440).
- ch 5 [low] Section 3 (reprojection error): "average the Euclidean distance" is not the usual reported figure. Calibration tools report the root-mean-square error over all corners, which is larger than the plain mean and is what is quoted when people say the error is under 1 px.
- ch 6 [low] Section 4, multi-view projective geometry: The sentence 'Two views fix depth only up to the baseline length' reads as if depth stays ambiguous in a two-view reconstruction, which is the opposite of what is meant. With two views and a known baseline, depth is fully determined; what is undetermined is the overall scale when B is unknown.
- ch 6 [low] Section 1, matching pipeline bullet list: RANSAC is listed as a way to 'reject weak matches' along with the ratio test. RANSAC is a robust model-fitting procedure that removes outlier matches while fitting F (or E); it is not a per-match descriptor test.
- ch 6 [low] Figure caption and figure spec: The caption says the dashed lines show that each image point lies on a line through its epipole, but the dashed edges are C2–e1 and C1–e2, which show that e1 is the image of C2 and e2 the image of C1. The lines through the epipoles are the accent edges x1–e1 and x2–e2.
- ch 6 [low] Section 4, last paragraph: 'Some syllabi call F the bifocal tensor' is an odd claim: the term bifocal tensor comes from research literature on multi-view tensors, not from a syllabus convention, and it may confuse a reader who then expects a tensor of a different kind.
- ch 7 [low] Section 2, formula box: The term baseline is used without a plain-word definition, and the sign convention is not stated: B is positive only when camera 2 is displaced by +B along X.
- ch 7 [low] Section 2, PnP paragraph: The text says the minimal P3P case uses 3 points but does not mention that P3P can return up to four possible poses, so 3 points alone are not enough to choose a unique pose.
- ch 7 [low] Section 2, first paragraph: The symbol X is used both for the 3D point and for its X coordinate in u = X/Z, which can confuse a reader.
- ch 8 [low] Section 2, step list, first bullet: 'Compute Ix, Iy and It by finite differences between frames' suggests all three derivatives come from comparing two frames. Only It is a between-frame difference; Ix and Iy are spatial differences inside one frame. A student may try to build Ix from frame differences.
- ch 8 [low] Worked example 1, opening line and steps: 'Two pixels in a 2×2 window' is loose: a 2×2 window holds four pixels, and only two are given. Also the solution divides each equation separately, which works only because pixel A has Iy = 0 (it fixes u alone) and pixel B has Ix = 0 (it fixes v alone). The example never says this, so it looks like it contradicts the earlier rule that one pixel cannot give both components, and it hides that the code is a shortcut for a diagonal A.
- ch 8 [low] Exam traps, bullet 1: The sentence 'cannot give both u and v unless one gradient is zero and you accept the other component as unknown' is hard to parse and can be read as saying a zero gradient helps recover both components.
- ch 8 [low] Lead and Section 3 applications: Saying 'Flow drives video compression' overstates it. MPEG-style coders use block-based motion vectors from matching, which are not the same as optical flow; the chapter itself later says 'motion vectors for blocks'.
- ch 9 [high] Section 3, SSD and NCC formulas: Section 1 defines T as a map from moving-image coordinates to fixed-image coordinates, and the aligned image as M(T⁻¹(x)). The SSD and NCC formulas then write M(T_θ(x)) for a point x on the fixed grid. With the stated direction, T_θ(x) is a coordinate in the fixed image, so sampling M there compares F(x) with the wrong point of M; the two conventions contradict each other inside one chapter.
- ch 9 [low] Section 1 formula, Section 3 resampling and Dice: The symbol A is reused three times: the 2×2 affine matrix in Section 1, the aligned image A(x) in Section 3, and one of the two label masks in the Dice formula. A student skimming will lose track of which A is meant.
- ch 9 [low] Section 2, RANSAC bullet: "RANSAC is robust because one bad match cannot pull the fit far" is misleading. A single bad match inside a minimal sample ruins that whole hypothesis, and a bad match that survives into the final inlier set does bias the refit. RANSAC works because bad hypotheses get few inliers and are thrown away, not because a bad match has little influence.
