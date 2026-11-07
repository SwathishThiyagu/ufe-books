# c-nlp-u6: free-model run

- Book: `books/cse/c-nlp/c-nlp-u6.html`
- Status: ok
- Model calls so far: 46 (195,778 tokens in, 309,183 out), 8.1 minutes

## Checker

```
c-nlp-u6.html: 8 chapters, 16137 words, 9 figures, 176 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1: The letter w is used for two different things in the same example: step 1 says the filter width is w = 2, while step 3 takes the dot product 'with w' meaning the weight vector. A student can read step 3 as multiplying by the number 2.
- ch 1 [low] Worked example 1, output block: The output shows three bare numbers (2, 0, 2) with no labels, so the reader cannot tell that these are the score of window 1, the score of window 2, and the pooled feature, in that order.
- ch 1 [low] Exam traps, fourth trap: The wording 'Concatenating the two windows instead of the two embeddings' is muddled: in the worked example 'the two windows' are (food, was) and (was, great), each of length 2·d, so it is unclear what mistake is being warned against.
- ch 2 [low] Quiz Q4, answer: "The input gate then adds it ⊙ c̃t" — the word "it" reads as ordinary English and hides the symbol. A student cannot tell whether "it" means i_t, f_t or c_t.
- ch 2 [low] Section 3, GRU update formula: The convention h_t = (1 - z_t) ⊙ h_{t-1} + z_t ⊙ h̃_t is one of two common ones; several textbooks write h_t = z_t ⊙ h_{t-1} + (1 - z_t) ⊙ h̃_t, so the update gate there does the opposite job. Nothing in the text warns the student, and the quiz answer depends on the chapter's choice.
- ch 2 [low] Section 2, LSTM gate formulas: The gate matrices are not given shapes. The text defines k and d in Section 1 but never says W_f, W_i, W_c, W_o are k × (k + d) and b_f, b_i, b_c, b_o are k-vectors, so the concatenation [h_{t-1}, x_t] has no stated length.
- ch 2 [low] Section 3, last paragraph: Cross-references are written as plain text ("see Unit 2 for tags and CRF training", "The encoder side of 6.3") while the book format expects chapter links, so a phone reader cannot tap through.
- ch 3 [low] Section 1, step list (first and second bullets): The steps say to store h₁ … hₙ and then to set the decoder's first state to 'the context vector', but the paragraph just above says plain seq2seq keeps only hₙ. A student following the steps will not know which of the stored states becomes c.
- ch 3 [low] Section 2 versus Section 3: Section 2 scores the current decoder state s_t against the encoder states (eᵢ = score(s_t, hᵢ)), while Section 3 gives the Bahdanau score with s_{t−1}. Both are standard, but the chapter never says why the index differs, so a student may use s_t inside the Bahdanau formula and lose marks.
- ch 3 [low] Worked example 2, step 2: The arithmetic is slightly off: 2.718 + 7.389 = 10.107, not 10.108. Small, but the numbers in a worked example must add up exactly as printed.
- ch 3 [low] Section 3 (cost of Bahdanau) and Quiz Q6 answer: Two cost statements are loose. (a) 'costs one matrix multiply per source position per step' — the projection U_a hᵢ does not depend on the decoder step and can be computed once for all source positions before decoding starts. (b) The claim that additive attention 'earns its keep when the decoder and encoder state sizes differ' is only true against plain dot attention; Luong's general form sᵗWh handles different sizes too, so the stated reason is incomplete.
- ch 4 [low] Section 1, self-attention paragraph and formula note: Q, K and V are all said to be n × dk matrices, but dk is defined as the query/key width. In the standard formulation Q and K are n × dk while V is n × dv, and the attention output has width dv. The chapter never defines dv or says dv = dk, so a student may think the value vectors must share the key width.
- ch 4 [low] Section 2, decoder block: 'The upper triangle of the score matrix is set to −∞' is ambiguous. The diagonal entry (the token attending to itself) must not be masked; if a student masks the whole upper triangle including the diagonal, the token loses its own value.
- ch 4 [low] Section 1, formula note: 'QKT' is written without the transpose, while the formula uses QKᵀ. The same quantity is written two ways, which can confuse a reader scanning the note.
- ch 4 [low] Section 3, BERT special tokens: [SEP] is described only as appearing between sentences. BERT also appends [SEP] after the last token of each segment, so the full input is [CLS] A [SEP] B [SEP].
- ch 5 [high] Section 3, temperature paragraph: The comparison sign is missing: "T  1 flattens it, and T = 1 leaves it unchanged." A student cannot tell whether the claim is about T > 1 or T < 1, and the equally important case (T below 1 sharpening the distribution) is never stated.
- ch 5 [high] Quiz Q2 answer: Same missing sign: "T  1 makes it flatter and output more random." As written the answer is unreadable and also leaves out the T < 1 behaviour that the question asks about.
- ch 5 [low] Lead: The closing sentence is a table-of-contents roadmap ("This chapter explains pretraining, prompting, instruction tuning, decoding and evaluation") and adds no content for a student revising on a phone.
- ch 6 [low] Exam traps, third bullet: The comparison in the brevity-penalty bullet is broken: "(c  r, BP = 1." The operator is missing and the parenthesis never closes, so a student cannot tell which case gives BP = 1.
- ch 6 [low] Worked example 1, step 7 and Quiz Q3 answer: The geometric mean is written as "(p1 × p2)1/2" with a plain "1/2". On a phone this reads as multiplying by one half, which would give 0.25, not 0.707.
- ch 6 [low] Section 3 (BLEU definition): The chapter allows "one or more reference translations" but defines r simply as "the reference length", and does not say what r is when several references exist.
- ch 7 [low] Worked example 1: The example defines its own normalisation as lower case plus punctuation stripped, and under that rule the step-by-step answer is fine. But the standard SQuAD evaluation script also drops articles (a, an, the), and SQuAD is the benchmark named in Section 2. Under the real metric 'the cat' normalises to 'cat', so EM would be 1 and F1 also 1. A student who memorises this example can then get the official SQuAD score wrong.
- ch 7 [low] Exam traps, third bullet: The bullet is headed 'Neutral is not contradiction', but its only example ('A man is playing guitar' vs 'A man is playing a musical instrument') contrasts entailment with neutral, not neutral with contradiction. The student is told to reserve neutral for cases the premise leaves open, yet no example shows a neutral pair sitting next to a contradictory one.
- ch 8 [high] Section 1: "intersect the two sorted lists in one merge pass; the cost is proportional to the shorter list" is wrong. A plain merge pass walks both lists, so the cost is linear in the total number of postings examined, not in the shorter list. Only with skip pointers or galloping search can the cost drop below that.
- ch 8 [high] Worked example 2: The recall and average-precision steps contradict the data. The four relevant documents sit at ranks 1, 3, 4 and 8, so all four are retrieved; recall is 4 ÷ 4 = 1.0, not 0.75. Step 3 and step 6 quietly evaluate only the top 5, yet step 5 divides the precision sum by 4 (the number of judged relevant documents), mixing a top-5 cutoff with a full-collection denominator.
- ch 8 [low] Worked example 2: The relevance grades 3, 2, 1, 1 are introduced but never used, because precision, recall and average precision are all binary measures. A student will look for somewhere to plug the grades in.
- ch 8 [low] Section 3 (MAP bullet): "average of precision@1, precision@2, … taken at each relevant hit" does not say what the sum is divided by. Standard average precision divides by the number of judged relevant documents for the query, including relevant documents that were never retrieved.
- ch 8 [low] Section 3 (NDCG bullet): "graded relevance discounted by the log of the rank" is imprecise: with ranks starting at 1, log(1) = 0 and the discount divides by zero. The position discount is log₂(1 + rank), or equivalently the gain is multiplied by 1 ÷ log₂(1 + rank).
- ch 8 [low] Section 4: cos(q,d) = 0 means the two vectors are perpendicular (orthogonal), not that the documents are "unrelated"; the similarity can also be negative for opposing vectors. Separately, "the query with one BERT-style encoder and each document with the same encoder, kept separate" is muddled about what is separate.
