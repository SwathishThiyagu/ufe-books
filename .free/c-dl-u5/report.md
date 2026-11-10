# c-dl-u5: free-model run

- Book: `work/claude_figs/c-dl-u5/tree/books/cse/c-dl/c-dl-u5.html`
- Status: ok
- Model calls so far: 30 (124,016 tokens in, 222,347 out), 5.6 minutes

## Checker

```
c-dl-u5.html: 7 chapters, 13598 words, 8 figures, 158 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, first paragraph: The sentence 'Keys and query must have the same length d_k so we can compare them' is stated as a general rule, but the chapter itself gives Bahdanau additive attention in the next paragraph, where W_q and W_k map the query and the keys into a common space and the two can have different lengths. Only plain dot-product scoring needs equal lengths.
- ch 1 [low] Section 2, first paragraph: The symbol s_t is used for the decoder hidden state (the query), but s_i was used in Section 1 for the match score. A student skimming can read 'Score s_t with each h_i' as scoring a score.
- ch 1 [low] Section 1, paragraph on scoring variants: The bilinear form s_i = q^T W k_i is labelled 'Luong multiplicative attention'. Luong's three named variants are dot, general and concat; the q^T W k_i form is the one he calls general.
- ch 2 [low] Section 2, positional encoding formula: The text says 'For dimension index i from 0 to d_model−1', but the formulas use 2i and 2i+1, so i must run only up to d_model/2 − 1. A reader who follows the stated range would get feature indices beyond d_model (and a code error when building the encoding).
- ch 2 [low] Section 1, opening paragraph and formula annotation: The three weight matrices are all said to be of size d_model × d_k, so V would be n×d_k, but the formula annotation then defines V as n×d_v with output width d_v. The two statements contradict each other unless d_v = d_k is stated.
- ch 2 [low] Section 1, last sentence: Memory is stated as O(n²d). The score matrix QKᵀ is n×n, so one head stores n² entries; h heads store n²h entries, plus nd for the vectors. Memory grows with n² but not with d in that way, so 'O(n²d) memory' overstates it by a factor of about h.
- ch 3 [high] Exam traps, trap 4 (perplexity): The trap says that feeding perplexity a base-2 loss 'gives 2^L, a different number'. That is wrong. Perplexity is a single number independent of the log base: if L_bits = L_nats / ln 2, then 2^(L_bits) = e^(L_nats). Using 2^L with a bit-loss gives exactly the same perplexity, not a different one. The real mistake is mixing the two, e.g. taking exp() of a bit-loss or 2^L of a nat-loss.
- ch 3 [low] Section 1, bullet list after 'You then reuse it in one of two ways': The same bullet list holds two reuse strategies (fine-tuning, feature extraction) and then three recipe steps (load checkpoint, train with small learning rate, evaluate). A student reads five parallel 'ways' where the last three are actually a fine-tuning procedure.
- ch 3 [low] Section 1, fine-tuning recipe (GLUE): GLUE is called 'the GLUE suite for sentence classification'. GLUE is nine sentence-level tasks covering acceptability, sentiment, inference, paraphrase and similarity; one of them (STS-B) is a similarity-regression task, not classification.
- ch 3 [low] Section 3, last paragraph: 'Attach a head to the [CLS] state' is BERT-specific, but this paragraph covers all families, so a reader may think a GPT-style decoder also has a [CLS] token.
- ch 4 [low] Section 2, scaling laws: The text says 'A power law has the form L = a + bN^−α'. A pure power law has no additive constant: L = bN^−α. The constant a is the irreducible loss floor, so the form given is a power law plus a floor, not a power law.
- ch 4 [low] Section 2, emergent abilities sentence: 'Some abilities, such as multi-step arithmetic or reading a table, appear only past a certain scale' states sharp emergence as settled fact. Whether such abilities jump suddenly or just improve steadily is actively debated; a strict reader may object.
- ch 4 [low] Section 1, loss formula: The formula writes log without giving the base, but Section 3 and Q6 later use perplexity = exp(L), which only works if log is the natural log and L is in nats per token.
- ch 4 [low] Quiz Q7 answer: Listing 'contamination' as a cause of a worse coding score is confusing. Contamination normally pushes a benchmark score up, not down; what it does here is make the held-out loss look better than the model really is.
- ch 5 [low] Section 2, final paragraph: 'That is why pairwise labels beat absolute 1–10 ratings' makes the shift-invariance of the Bradley–Terry reward the reason for using pairwise labels. The reason is human reliability: people agree on which answer is better far more than on a number. Shift-invariance is a property that follows from using pairs, not the cause.
- ch 5 [low] Section 3 and Quiz Q6: Section 3 says the KL penalty is 'summed over tokens', while Q6 says KL 'penalises distance from π_ref, not length'. A per-token KL summed over the sequence does grow as the answer gets longer, so the two statements pull against each other and a student can read Q6 as contradicting Section 3.
- ch 5 [low] Section 3, bullet list: The three failure-mode bullets (reward-model bias, length bias, over-optimisation) appear with no lead-in sentence after the PPO paragraph, so on a phone the reader cannot tell what the list is a list of.
- ch 6 [high] Exam traps, third bullet: "A prompt cannot supply facts the model never learned.": This sentence contradicts Section 4 of the same chapter. RAG works exactly by pasting into the prompt facts the model never learned from its weights, and the model then answers from them. A student who reads both will be confused about what a prompt can and cannot do.
- ch 6 [low] Section 4, after the two fixes (truncate, summarise): "Both lose detail; say so in the system message" is unclear: say what, and to whom? A student cannot tell what sentence to write in the system message.
- ch 7 [high] Section 1, last line: It says a large 'chat model' can become a 'small encoder' for a phone. Chat models are generative/decoder models; an encoder does not chat. Distillation normally preserves the task and architecture family, so this example misleads students.
- ch 7 [high] Figure, node s: The shared final node 'Deployed small model' has note '4x less memory'. All three routes point to this node, but only INT8 quantization gives 4× memory reduction versus FP32. Distillation and pruning give whatever reduction the chosen student or sparsity level gives.
