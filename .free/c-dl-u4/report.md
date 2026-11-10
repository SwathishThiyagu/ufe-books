# c-dl-u4: free-model run

- Book: `work/claude_figs/c-dl-u4/tree/books/cse/c-dl/c-dl-u4.html`
- Status: ok
- Model calls so far: 33 (134,281 tokens in, 219,142 out), 5.9 minutes

## Checker

```
c-dl-u4.html: 7 chapters, 13625 words, 8 figures, 152 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Quiz Q5: The answer describes the leakage direction wrongly: a random row split does not put only later values in train and earlier values in test. It scatters both early and late points across both sets, so training rows end up later in time than many test rows. As written, a student may think random splitting always puts the future in train and the past in test, which is not what happens.
- ch 1 [low] Quiz Q6: The answer rejects seq2seq on the ground that the output is 'not a new sequence of different length'. Length equality is not the distinguishing feature; seq2seq can produce an output of the same length as the input. The real reason is that each output tag is tied to one input position.
- ch 2 [high] Worked example 1, step 3 and answer: The value of tanh(2.3808) is wrong. tanh(2.3808) ≈ 0.8307, not 0.98332, so h_2 and y_2 are both overstated; a student copying this gets a wrong final answer.
- ch 2 [low] Section 1, last line: "Only a few syllabi use the name vanilla RNN" is misleading: "vanilla RNN" and "simple RNN" are the standard, widespread names for this cell, so students may think the term is obscure and avoid using it in an answer.
- ch 2 [low] Section 2, cost sentence: The count says two matrix products per step and gives O(T·H·(d+H)); the output projection W_hy (H×k) is also multiplied at every step, so the stated cost is a slight undercount.
- ch 3 [high] Section 3, spectral radius paragraph: The sentence reads "It gives local intuition: ρ  1 expands." The inequality signs are missing, so the key rule (contract if ρ < 1, expand if ρ > 1) is unreadable and a student cannot tell which case causes vanishing and which causes exploding.
- ch 3 [low] Section 2, the ∂L/∂W_hh formula note: "the inner product is the identity when k = t" is the wrong term. The inner product is a dot product; here the object that equals the identity matrix when k = t is the product of Jacobians.
- ch 3 [low] Section 2, the ∂L/∂W_hh double-sum formula: The ordering and transposes do not match the column-vector convention used just above (δ_t = ∂L_t/∂h_t + J_{t+1}ᵀ δ_{t+1}). With ∂L_t/∂h_t treated as a column vector, multiplying it on the left of a product of Jacobians is dimensionally inconsistent, and the chain rule gives the path product in the order J_t J_{t-1} ⋯ J_{k+1}, not J_{k+1} ⋯ J_t as Π_{j=k+1}^{t} J_j is normally read.
- ch 4 [low] Section 3, GRU equations: The chapter fixes one convention (z_t near 1 means the candidate is used, z_t near 0 keeps the old state), but many standard implementations, including PyTorch's GRU, use the opposite sign: h_t = (1 − z_t)⊙h~_t + z_t⊙h_{t-1}. A student who checks code after reading this will think the chapter is wrong.
- ch 4 [low] Section 3 and Beyond (peephole LSTM): Saying peepholes let 'the gates see c_{t-1} directly' is only right for the forget and input gates. The peephole into the output gate uses the freshly updated cell state c_t, because h_t is formed after c_t exists.
- ch 4 [low] Section 1, formula block: Only the forget-gate line carries the [formula] tag; the remaining five equations (i_t, c~_t, c_t, o_t, h_t) run together as plain lines. On a phone the cell update and output lines are easy to miss, and the single 'where' clause covers equations that were never tagged.
- ch 4 [low] Section 3, last paragraph: 'Some syllabi call these gated recurrent units' repeats the expansion already given two sentences earlier and reads as if an alternative name exists. A reader may look for a second term that is not there.
- ch 5 [low] Exam traps, first bullet: The sentence 'Feeding the true previous target token at inference is teacher forcing' mislabels the term. Teacher forcing is a training-time procedure; feeding true tokens during inference is a different (and wrong) decoding practice. A student can walk away thinking teacher forcing means 'using true tokens at test time'.
- ch 5 [low] Quiz Q3, answer: The answer calls the logit value 2 a 'score', but the chapter's own trap warns that logits are not probabilities, and 'score' is used later for a sum of log probabilities in beam search. Using 'score' for a raw logit is inconsistent.
- ch 5 [low] Lead: The lead says the decoder feeds 'each produced token back as the next input' with no qualifier. That is inference behaviour only; during training the true previous token is fed. A reader who stops at the lead will carry the wrong picture into Section 2.
- ch 6 [low] Section 3, GloVe sentence: The direction of the GloVe weighting is stated wrongly. GloVe's weighting function f(Xij) gives large counts weight close to 1 and gives small counts a weight below 1, so it mainly down-weights rare co-occurrences and caps the influence of very frequent ones. It does not down-weight very frequent pairs below the others.
- ch 6 [low] Section 3, negative sampling: The value 'k = 5 to 20' is the range for small training sets only. For large corpora the usual value is 2 to 5; giving only the small-data range can mislead a student choosing k.
- ch 6 [low] Section 2, CBOW hidden vector and Quiz Q2 answer: The notation h = (1/2m) Σk ut+k leaves the range of k unstated, so a student cannot tell whether k runs over 1…2m or over the signed offsets −m…m, and whether k = 0 is included.
- ch 7 [low] Section 3, decoder formula: The recurrence h(t) = tanh(W_h h(t−1) + W_x x(t) + b) cannot be evaluated at t = 0, because h(−1) does not exist, yet the text says v (through x0) is the decoder's first input. A student may not see how the image enters the first step.
- ch 7 [low] Section 2, BLEU description: "It counts matching n-grams (single words, pairs, triples)" leaves out 4-grams. Standard BLEU uses n-gram precisions for n = 1 to 4.
- ch 7 [low] Section 1, loss formula note: "exp(L) = eL" reads as e times L; the exponent is lost in plain text, which is exactly the term students must not misread.
- ch 7 [low] Section 3, CNN feature size: "a few hundred to a couple of thousand numbers" understates common choices: a ResNet-50 pooled feature is 2048 and a VGG fully connected feature is 4096. "A couple of thousand" suggests about 2000 as the top end.
- ch 7 [low] Section 4, video models: "Adding time inside the convolution gives 3D CNNs and two-stream models" attributes both architectures to the same idea. Two-stream models do not put time inside the convolution; they run two separate networks, one on RGB frames and one on optical flow.
