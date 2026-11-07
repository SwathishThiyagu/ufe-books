# c-dl-u3: free-model run

- Book: `books/cse/c-dl/c-dl-u3.html`
- Status: ok
- Model calls so far: 37 (148,058 tokens in, 257,853 out), 6.2 minutes

## Checker

```
c-dl-u3.html: 9 chapters, 15599 words, 10 figures, 183 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, formula for y[i,j]: The index X[iS+u, jS+v, c] ignores padding, but Section 2 then introduces padding P. A student applying this formula to a padded input will read the wrong pixels and never be told how the index changes.
- ch 1 [low] Worked example 1, step 2: 'Row products' is misleading. Each number like 1−3=−2 is the sum of element-wise products of one image row with one kernel row (a row dot product), not a product.
- ch 1 [low] Exam traps, first trap: '4×4 with K=3, S=2 gives floor(0.5)+1=1, not 1.5' is garbled: it does not say which wrong method produces 1.5, so the reader cannot see what is being contrasted.
- ch 2 [low] Section 2, average-pooling gradient paragraph and Exam traps bullet 5: The rule 'each cell gets output gradient / (p × p)' is exact only for one non-overlapping window. If pooling uses stride s < p, windows overlap and an input cell receives the sum of contributions from every window that contains it. The text does not state this.
- ch 2 [low] Section 1, first paragraph: 'the map shrinks by the same factor on each side' is not exact when the input side n is not divisible by the pool size p; the exact output side is given by the floor formula.
- ch 3 [low] Section 1: The sentence 'so H and W halve' is only exact when the input height and width are even. With the general formula a 7×7 map pools to 3×3, not 3.5×3.5.
- ch 3 [low] Section 2 table: The table lists Conv, MaxPool, Flatten, Dense and Softmax but leaves out the ReLU layers that appear in the figure. A student matching table to figure may think ReLU is missing from the network.
- ch 3 [low] Figure spec: The first pooling node carries the note 'stride 2' but the second pooling node 'pool2' has no note, so the figure looks inconsistent.
- ch 3 [low] Section 3: The cross-reference 'see 3.4' is plain text, so on a phone the reader cannot jump to that chapter the way other links work.
- ch 4 [low] Section 1, paragraph 2: "ReLU trains faster and avoids flat gradients" is imprecise. ReLU's gradient is exactly zero for negative inputs, so it does have a flat region; what it avoids is the saturation of sigmoid and tanh, whose gradients shrink toward zero for large positive or negative inputs (vanishing gradient). A student can read this sentence backwards.
- ch 4 [low] Section 1, paragraph 2, last sentence: "These choices reduce overfitting on a large network" lumps ReLU in with the regularizers. ReLU is there for faster, better-conditioned training, not to fight overfitting; dropout, data augmentation and pooling are the anti-overfitting choices.
- ch 4 [low] Section 4, first-convolution parameter comparison: The three numbers are not a like-for-like comparison. AlexNet and ZFNet use 96 filters in the first convolution, while VGG uses 64. So part of the fall from 14,208 to 1,792 comes from the smaller filter count, not only from the smaller kernel, and the sentence "Smaller first kernels spend fewer weights on raw pixels" hides this.
- ch 4 [low] Sections 1–4 and Beyond (cross-references): References to other chapters (3.3, 3.5, 3.6, 3.7) are written as plain text, so they are not clickable in the book's phone reader.
- ch 5 [low] Lead vs Section 1: The lead says very deep CNNs fail because 'gradients vanish', but Section 1 correctly says the failure is the degradation problem, a separate optimization issue. Section 1 then says the shortcut 'is separate from the vanishing-gradient fixes', yet also says gradients flow through the addition. A student can end up unsure whether ResNet fixes vanishing gradients or not.
- ch 5 [low] Section 1, formula note: The formula is y = F(x) + x, but the note says y is the output 'after the addition and ReLU'. The ReLU comes after the addition, so the symbol y in the formula does not match the description.
- ch 5 [low] Section 2, bottleneck sentence: 'so a 5×5 conv does not cost C×25×C_out' reads as if a 5×5 conv never costs that. Without the 1×1 bottleneck, a 5×5 conv from C to C_out does cost 25×C×C_out; the saving comes from the reduced channel count.
- ch 5 [low] Section 2, first paragraph: Subject-verb agreement: 'A 1×1, 3×3 and 5×5 kernel see different scales.'
- ch 5 [low] Section 3, comparison paragraph: 'All three improve gradient flow and feature mixing' is loose for Inception. Its parallel branches widen the block rather than giving one short path back through depth, which is the ResNet and DenseNet story.
- ch 6 [low] Section 1, bullet list: The step says 'Freeze every convolution and pooling layer'. Batch-normalization layers are neither convolution nor pooling, so a student following this literally would leave the BN parameters trainable. Section 2 later says BN must be handled carefully, so the two parts do not join up.
- ch 6 [low] Section 1, bullet list and Figure: The step 'Add global pooling and a new K-way fully connected layer' suggests a pooling layer is being added. ResNet-50 already ends with global average pooling before its fully connected layer, so the usual move is to keep the existing pooling and replace only the FC layer.
- ch 6 [low] Section 2 table, first row (2,000 images): The table gives 1e-3 for the new head, while the text says fine-tuning uses a rate 'often 10 to 100 times smaller than training from scratch'. The two statements look contradictory unless the reader knows the small-rate rule applies only to unfrozen pretrained layers, not to the brand-new head.
- ch 6 [low] Lead, Section 1, worked example step 6: Terms central to the numbers are used without definition: 'global average pooling' (never explained as averaging each feature map to one number), 'ResNet-50' and 'residual block' (step 6). A reader on a phone who has not met ResNet cannot picture what is frozen.
- ch 6 [low] Figure spec vs body text: The same number is written two ways: '2048 features' in the figure note and '2,048' in the text. Small, but inconsistent number formatting in a unit book is distracting.
- ch 6 [low] Quiz Q5: The answer '1e-4 to 1e-5' is right for the unfrozen last block, but a student may carry it over to the new head, which still needs a normal rate near 1e-3.
- ch 7 [high] Quiz Q8: The answer says unpooling loses exact positions. This contradicts Section 1, which correctly says unpooling uses switch positions saved during max pooling. Max pooling discards non-maximum values, not the positions of the selected maxima.
- ch 7 [high] Section 3, CAM definition and Exam traps: CAM is defined with a ReLU: L^c = ReLU(Σ_k w_k^c A^k). In the standard CAM formulation, the class activation map is the weighted sum Σ_k w_k^c A^k. The ReLU belongs to Grad-CAM, or is an optional display post-process; the trap repeats it as required for CAM.
- ch 7 [low] Section 1, first paragraph: “Deconvolution, also called transposed convolution or backprop-to-image” conflates a layer with a visualization method. Backprop-to-image is the gradient of an activation with respect to the input; deconvolution is transposed convolution used inside a deconvnet.
- ch 7 [low] Quiz Q4 answer: Says CAM needs “a specific pooling layer and retraining.” CAM needs a global average pooling layer; retraining is needed only if the trained model does not already have one.
- ch 8 [low] Section 1, mAP sentence: The sentence defines mAP as averaging precision-recall scores over IoU thresholds only. In standard textbooks, average precision (AP) is the area under the precision-recall curve for one class at one IoU threshold, and mAP is the mean of AP over classes (COCO also averages over IoU thresholds). As written, a student would think the averaging is only over thresholds.
- ch 8 [low] Section 1, NMS description: NMS is described as sorting all boxes by score together. In a multi-class detector, boxes of different classes must not suppress each other, so NMS is run separately for each class.
- ch 9 [high] Exam traps, second bullet: The trap says 'U-Net and FCN skip connections concatenate channels (64 + 64 = 128)'. The original FCN fuses its coarse score map with the earlier, finer prediction by element-wise addition, not concatenation. Only U-Net concatenates. The trap therefore contradicts Section 1, which correctly allows 'add it or concatenate it', and it would make students write the wrong fusion rule for FCN.
- ch 9 [low] Section 2 (ROIPool sentence) and Quiz Q6 answer: 'Shifting features by up to one pixel' is measured on the feature map, not on the image. At stride 16 one feature-map pixel is 16 image pixels, so the misalignment a student pictures is wrong.
