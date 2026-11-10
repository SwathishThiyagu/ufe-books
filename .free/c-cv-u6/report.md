# c-cv-u6: free-model run

- Book: `work/claude_figs/c-cv-u6/tree/books/cse/c-cv/c-cv-u6.html`
- Status: ok
- Model calls so far: 39 (161,828 tokens in, 275,163 out), 6.0 minutes

## Checker

```
c-cv-u6.html: 9 chapters, 17005 words, 10 figures, 203 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Exam traps, item 2: The trap says 'Do not call the feature vector the "pattern" when the exam asks for the pattern vector', which is self-contradictory and contradicts standard usage. In the standard textbooks the pattern vector and the feature vector are the same object: the ordered list of measurements x = (x₁, …, xₙ). A student following this trap could refuse to write x when asked for the pattern vector and lose marks.
- ch 1 [low] Exam traps, item 4: 'A feature is useful only if it separates the classes' is stated as a general rule and is too strong. A feature whose ranges overlap can still help when combined with another feature (two features that each overlap can jointly separate the classes). Only in the tomato example is area useless because R already separates perfectly.
- ch 2 [high] Section 3 (also Exam trap 3, Q6 answer, figure caption): The claim that equal covariance matrices and equal priors make the Bayes boundary 'exactly the minimum distance boundary' is false for a general covariance matrix. Equal covariance Σ gives a linear Bayes boundary, but the rule is nearest mean under Mahalanobis distance (x−m_j)ᵀΣ⁻¹(x−m_j). Only when Σ is a scalar multiple of the identity, Σ = σ²I, does that reduce to Euclidean nearest mean, with the boundary as the perpendicular bisector of m₁m₂. Q6 repeats the error ('With equal priors it is the minimum distance line') and so do the figure caption and Exam trap 3.
- ch 2 [low] Section 2: 'Manhattan distance adds absolute coordinate differences' is loose; it is the sum of those differences, not an extra term added to Euclidean distance.
- ch 2 [low] Section 3, confusion matrix sentence: The four counts (true positive, false positive, true negative, false negative) describe a two-class problem; for J classes the confusion matrix is J×J and these counts are taken per class. A student may think a confusion matrix is always 2×2.
- ch 2 [low] Lead: HOG is called a small feature set, but a standard HOG descriptor for one detection window has thousands of components, so the example misleads about when these classifiers are cheap.
- ch 3 [high] Section 2 (AlexNet and VGG): ZFNet is described as having enlarged the first-layer kernels. Zeiler and Fergus did the opposite: they shrank conv1 from 11 × 11 with stride 4 to 7 × 7 with stride 2, and kept the rest of AlexNet's layout roughly the same.
- ch 3 [low] Section 3 (ResNet): 'the family runs from 34 to 152 layers' leaves out ResNet-18, which is a standard published member of the same family and the one most often used for small datasets in this syllabus.
- ch 3 [low] Section 3 (ResNet), paragraph on the shortcut: 'The shortcut carries x with no weights, so the block adds no parameters' is stated flatly, but two sentences later the chapter says a 1 × 1 projection is needed when the shape changes. As written the two sentences contradict each other.
- ch 3 [low] Exam traps, fourth bullet: 'Saying the 3 × 3 kernels cause the size is the wrong answer' is garbled; 'size' should be 'parameter count', otherwise the student cannot tell what claim is being corrected.
- ch 4 [low] Lead: 'proposes a few hundred candidate boxes' contradicts Section 2, which correctly says selective search gives about 2000 proposals per image. A student may carry the wrong number into an exam.
- ch 4 [low] Section 3, anchor labelling: The labelling rule is incomplete. The standard rule also makes the anchor with the highest IoU against each ground-truth box positive, so every object gets at least one positive anchor. Without this, a student can believe an object whose best anchor has IoU 0.6 gets no positive anchor at all.
- ch 4 [low] Section 2, loss formula: The loss as written lets background proposals contribute to L_box. In Fast R-CNN the box loss applies only to proposals that contain an object (c ≥ 1); background RoIs contribute only L_cls.
- ch 4 [low] Figure caption: The caption says the sharing (feature map used for both proposals and heads) is 'the speed gain over R-CNN'. Over R-CNN the gain is convolving the image once instead of 2000 times; sharing the map with the proposal network is the gain over Fast R-CNN.
- ch 4 [low] Beyond: 'RoI Align ... is now the default in every RoI head' is an overstatement; many Faster R-CNN implementations still ship RoI pooling, and RoI Align became standard mainly in segmentation and recent detection codebases.
- ch 5 [low] Section 1, paragraph on responsibility ("Other cells are trained as no-object"): Read literally, this says every cell except the responsible one gets a no-object target for this object. A cell can hold the centre of a second object, and then it is a positive cell for that object. A student may think such a cell is wrongly punished.
- ch 5 [low] Section 1, confidence definition, and worked example 1 part (d): The chapter defines confidence as Pr(object) × IoU with the truth box and then uses 0.8 from the IoU with the truth as if it were available at test time. At test time there is no truth box; the network outputs its own confidence, trained towards that product. Without this line a student may think IoU with ground truth is computed during inference.
- ch 5 [low] Section 1 and worked example 1 part (d): The class score is called a plain "class probability", but YOLO's C class numbers are conditional probabilities, Pr(Class_i | Object). This is exactly why multiplying by confidence gives a valid per-class score; without it the multiplication step looks arbitrary.
- ch 6 [high] Section 1: "Each cell sees a 32×32 pixel region" confuses the stride (the 32×32 patch of the input that maps to each cell) with the receptive field. The receptive field of a cell in the final layer is much larger than 32×32 — it covers most of the image — because it is built from stacked 3×3 convolutions. A student will conclude the network only looks at a small window.
- ch 6 [low] Exam traps, trap 5: "unless skips change the path" is vague and can be read as saying skips change the total upsample factor. In FCN-16s the total factor is still ×32 (×2 then ×16); skips only add detail at intermediate resolution.
- ch 6 [low] Quiz Q5 answer: Grammar error: "The decoder unpool with those indices" — the verb does not agree with the subject.
- ch 7 [high] Section 1 (Video as a stack of frames): The sampling stride is defined as 'the number of frames between kept frames', but the very next sentence keeps 'every r-th frame' and computes N = T/r. The symbol r is never defined, and the two wordings differ by one: if r-th frames are kept, the gap between kept frames is r − 1, not r. The rest of the chapter (worked example, quiz Q3) silently uses stride as the step.
- ch 7 [high] Section 3 (Test-time clips and scores): 'A model trained on 16-frame clips is normally tested with 16-frame clips, because clip length sets the temporal receptive field' contradicts Section 2, where the temporal receptive field is defined as the number of input frames that can affect one output value and is said to grow with network depth. Clip length is an input property; receptive field is a network property.
- ch 7 [low] Section 1 and Section 3: The word 'stride' is used for two different quantities: the step between kept frames, and the step between the start positions of successive clips in M = ⌊(N − L)/s⌋ + 1. Section 1 promises 'the terms clip, frame and stride with these meanings throughout', so a student can plug the frame-sampling stride into the clip-count formula.
- ch 7 [low] Section 2 (Three model families): Cross-references appear as plain text ('from Unit 5, Optical flow and motion estimation', 'A CNN from 6.3'), so they are not clickable and the unit naming is inconsistent with the chapter-id style used elsewhere.
- ch 8 [low] Lead: The lead says both tasks 'put a language decoder after an image encoder', but in this chapter VQA ends in a softmax classifier over a fixed answer list, not a word decoder. A student may think VQA generates sentences.
- ch 8 [low] Section 3, combination list (element-wise product bullet): The chapter's own example sizes are 2048 for the image vector and 1024 for the question vector, so v ⊙ q cannot be computed as written. The bullet 'same length' does not say how the lengths are made equal.
- ch 8 [low] Section 1, beam search sentence: 'Beam search keeps the best 3 to 5 partial sentences by total log-probability' suggests one global set is kept for the whole sentence. Beam search keeps k hypotheses at every step and prunes to k after each word.
- ch 8 [low] Exam traps, fourth trap: 'A fluent generic sentence can score well and still miss the wrong detail' is inverted and confusing: 'miss the wrong detail' literally means it does catch that detail.
- ch 8 [low] Figure, answer node note: The note says '1 of 1000 answers' while the text says the answer vocabulary has about one thousand to three thousand frequent answers. The two numbers should not disagree.
- ch 8 [low] Section 2, attention score formula: The score is written as 'si = ht−1T Wa vi'. The transpose mark on the hidden state is not clearly separated, so a student may read 'ht−1T' as one symbol.
- ch 9 [high] Section 3, the partial-convolution formula and the line after it: The denominator is written as 1ᵀ(x ⊙ M) and is described as counting valid pixels. But 1ᵀ(x ⊙ M) is the sum of the pixel values at valid locations, not their count. Dividing by that sum is not partial convolution, and the sentence 'counts valid pixels in the patch' is false. The count of valid pixels is 1ᵀM (equivalently sum(M)).
- ch 9 [low] Quiz Q3 answer: The answer prints 'log 0.8 = −0.223' twice in a row without saying what the second one is, so a student may read it as a typo instead of the second term of the objective.
- ch 9 [low] Section 2, sentence on the KL term: 'A small KL can mean blurry reconstructions' leaves the mechanism unstated and can be misread (a small KL alone usually means the latent carries little information, i.e. posterior collapse).
