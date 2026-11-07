# c-dl-u6: free-model run

- Book: `books/cse/c-dl/c-dl-u6.html`
- Status: ok
- Model calls so far: 32 (123,906 tokens in, 197,270 out), 4.8 minutes

## Checker

```
c-dl-u6.html: 7 chapters, 12924 words, 8 figures, 145 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Lead: It says autoencoders are used 'as the base of generative models such as VAEs and GANs'. GANs are not built on an autoencoder; a GAN is a generator trained against a discriminator, with no encoder/decoder reconstruction step. A student will carry this wrong link into the generative-model unit.
- ch 1 [low] Exam traps, tied weights bullet: 'Tied weights mean W_d = W_eᵀ only when the dimensions match' is misleading. W_e is m×n, so W_eᵀ is n×m, which is exactly the shape W_d must have. The dimensions always match by construction, so the caveat invents a restriction that does not exist.
- ch 2 [low] Section 2, first paragraph: The sentence gives the wrong reason for the factorization. 'x is independent of other latent causes not connected to it' is a graph statement about x versus other latents; it is not what makes p(x|z) split into a product over the observed dimensions. As written, a student will think the factorization follows from removing other latent causes, which is not the argument.
- ch 2 [low] Section 2, first paragraph: The rule 'a node is independent of all non-neighbouring nodes given its neighbours' is stated for a Markov network (undirected), and the next sentence switches to a directed graph (z has no parent, x is its child). A student will carry the undirected rule over to directed graphs, where it fails at colliders: in z→x←z', the latents z and z' are non-adjacent but become dependent once x is conditioned on.
- ch 2 [low] Section 1, EM sentence: EM is named once and described only as 'iterates between a posterior over z and a parameter update'. The abbreviation is never expanded and the two steps are not stated, so a student cannot use or recognise EM from this.
- ch 2 [low] Section 3, second paragraph: 'The likelihood also penalizes a model that puts high mass on hidden states that rarely produce the observed x' reads like an extra penalty term. There is no penalty term; the marginal is simply an average of p(x|z) weighted by the prior, and prior mass on poorly fitting z lowers that average.
- ch 3 [high] Quiz Q6: The last clause says that at very large β 'the latent dimensions become more independent and easier to interpret'. That contradicts the collapse described in the same answer: once the encoder outputs the prior for every input, z carries no information about x, so there is no attribute left to interpret. A student would write 'large β gives interpretable latents' in the exam, which is false for very large β.
- ch 3 [low] Worked example 1, step 6: 'Training pushes both μ and σ² down' is only true from this starting point. The KL term pulls μ toward 0 and σ² toward 1, so σ² would be pushed up if it were below 1. A student may conclude the VAE drives every variance to zero.
- ch 3 [low] Exam traps, trap 4: 'redrawing σ each step' is unclear and technically wrong: σ is not random, it is computed from the encoder output for each input. The randomness in the reparameterization step sits in ε, which is drawn fresh each pass.
- ch 4 [low] Quiz Q3: The stated value of V is slightly off. ln 0.9 = −0.1054 (the answer truncates it to −0.1053), and −0.10536 − 0.22314 = −0.32850, so V ≈ −0.3285, not −0.3284. The G loss 1.6094 is correct.
- ch 4 [low] Section 3, CycleGAN bullet: The symbol F appears in the cycle loss ‖F(G(a)) − a‖₁ without ever being defined, and G is already used earlier in the chapter for the single GAN generator, so a student can read F(G(a)) as G applied twice. Only the forward cycle is given; the backward cycle that CycleGAN also needs is not mentioned.
- ch 5 [low] Section 2: The sentence "Training feeds a whole image and computes one conditional per pixel in parallel" is written as if it holds for both models. It is exactly true for PixelCNN, but a PixelRNN built from plain recurrent layers still steps through the pixel sequence one position at a time during the forward pass; only the convolutional recurrences in the usual PixelRNN allow the per-position results to be computed in parallel. A student may wrongly conclude that any recurrent autoregressive model trains in one parallel step.
- ch 5 [low] Section 3 (coupling layer) and quiz Q6: "log determinant = Σ s(xA)" does not say what the sum runs over. s(xA) is a vector with one entry per component of xB, and the sum is over those entries; a student may read Σ as summing over the data points or over xA.
- ch 6 [high] Exam traps, third trap: The trap reads 'Do not evaluate on training patches or train only on high-resolution targets.' Read literally, this tells students not to train on high-resolution targets — but the high-resolution image is exactly the supervision in super-resolution training. The real pitfall it is reaching for is a mismatch between the low-resolution images used in training and those seen at test time.
- ch 6 [low] Section 2, the probability expression p(y | x ⊙ (1 − m), m): The symbol y is never defined, and the mask polarity only becomes clear from the surrounding text, so a student reading the formula alone cannot tell what y or m are.
- ch 6 [low] Section 3, last paragraph: The sentence about 3D object generation from voxels or point clouds is a different application and interrupts the super-resolution evaluation point.
- ch 6 [low] Exam traps, first trap: 'PSNR is not “higher is always better” perceptually' is tangled and can be misread as saying higher PSNR is worse. The intended meaning is that a higher PSNR does not guarantee a better-looking image.
- ch 6 [low] Section 3, SSIM sentence: 'it ranges up to 1 for identical images' gives no lower bound, so students cannot say what the scale is.
- ch 7 [low] Section 3, last paragraph: The cross-reference "see Unit 5" is loose and is not a chapter link, so a student reading on a phone cannot jump to it and may not know which chapter is meant. The sentence also implies responsible AI is just another name for LLM ethics, which is broader than that.
- ch 7 [low] Exam traps, last bullet: "A watermark proves origin" is too strong. A watermark shows that the media passed through a particular tool or account; it can be forged, copied onto other media, or stripped, so presence and intactness are not proof of who truly made the content.
