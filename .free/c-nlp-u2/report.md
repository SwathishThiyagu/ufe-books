# c-nlp-u2: free-model run

- Book: `books/cse/c-nlp/c-nlp-u2.html`
- Status: ok
- Model calls so far: 37 (145,844 tokens in, 275,607 out), 7.6 minutes

## Checker

```
c-nlp-u2.html: 9 chapters, 15406 words, 10 figures, 175 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q7: The answer says that without ⟨/s⟩ "the row for sat no longer sums to 1 over modelled continuations". That is false for an unsmoothed maximum-likelihood model. Dropping ⟨/s⟩ leaves c(sat)=1 with the single continuation sat on, so the row is renormalised and P(on | sat) becomes 1.00, which sums to 1. The real damage is that no probability is ever assigned to stopping, so mass leaks to longer and longer strings.
- ch 1 [low] Section 1: The sentence "the cat sat" is said to be scored as P(cat | the) × P(sat | cat). With the boundary symbols used everywhere else in the chapter, this leaves out P(the | ⟨s⟩) and P(⟨/s⟩ | sat), so a student may think the sentence probability has no boundary terms.
- ch 2 [high] quiz Q7: The answer says the unseen mass in add-one smoothing is V/(N+V). That is the total mass added by all the +1 pseudo-counts, not the mass assigned to word types with count 0. The worked example gives the single unseen word dog 1/16, not 6/16.
- ch 2 [low] Section 3 table, main check row for backoff: The table says the discounted model must sum to 1. In Katz backoff the discounted seen-count part sums to less than 1; α(h) adds the missing mass from the lower-order model. The full backoff distribution, not the discounted part alone, must sum to 1.
- ch 2 [low] Worked example 1: Step 6 uses the MLE bigram P(dog|the)=0, but step 7 uses the add-one unigram P(dog)=0.0625. The example does not say that the bigram term is unsmoothed while the unigram term is add-one. If a student applies add-one to the bigram too, P(dog|the)=1/(4+6)=0.1 and the interpolated value is different.
- ch 2 [low] Section 3, Katz backoff definition: It says c* is a discounted count with c*<c. In standard Katz backoff, high counts can be left undiscounted (c*=c); only the discounted counts are reduced.
- ch 2 [low] Lead: The sentence says every phone keyboard, speech recogniser and machine translation decoder uses some form of smoothing/interpolation/backoff. Modern neural systems often avoid explicit n-gram smoothing, as the Beyond box itself notes.
- ch 3 [high] Worked example 1, step 3: The log step has a sign error: ln 0.1 = -2.302585, dividing by 3 gives -0.767528, and exp(-0.767528) is about 0.464, not 2.1544. The exponent must be +0.767528.
- ch 3 [high] Worked example 2: The model is called a trigram, but the conditionals condition on only one previous token: P(dog | the) and P(</s> | dog). A trigram must condition on the previous two tokens.
- ch 3 [low] Section 2, paragraph after the vocabulary rule: 'The ranking survives any monotone transform' is false for a decreasing monotone transform; it would reverse the ranking.
- ch 3 [low] Section 2, paragraph after the vocabulary rule: The sentence says a larger vocabulary makes perplexity 'naturally higher' even if the model is better. That is only a tendency, not a rule; with <unk> mapping and different effective test sequences, the larger-vocabulary model can sometimes have lower perplexity.
- ch 4 [low] Section 1 (and Section 2 lexicon line): The example says 'that' is tagged PRP in 'I know that'. The chapter has just defined the Penn Treebank tagset, and in that tagset demonstrative 'that' keeps its DT label even when it stands alone as a pronoun ('I know that' = I know that fact). PRP is reserved for personal pronouns such as I, you, he, she, it, we, they. A student who memorises PRP here will lose marks on a tagset question.
- ch 4 [low] Section 3, formula line and baseline sentence: 'argmaxt P(t|w)' is printed without the subscript, so the symbol is not readable as argmax over t.
- ch 4 [low] Exam traps, item 3: 'Do not confuse a tag with a word class in the abstract: the same word carries different tags in different sentences, and a tagset label is context-dependent.' The last clause is misleading: the label itself is fixed; what is context-dependent is which label a given occurrence gets. A student may read it as 'the meaning of the label changes with context'.
- ch 4 [low] Section 1, ambiguity paragraph: 'The average English word has more than one possible tag' overstates it: most word types are unambiguous; the ambiguity is concentrated in frequent words. Stated this way it can puzzle a student who checks a small dictionary.
- ch 5 [low] Section 1 and Worked example 1, step 1: Section 1 says emission rows must sum to 1 (Σo b(i,o)=1), but the example's emissions do not: for tag N, 0.5+0.1=0.6, and for tag V, 0.2+0.6=0.8. A student who checks the stated property against the given numbers will think either the rule or the numbers are wrong.
- ch 5 [low] Section 1 versus Worked example 1: Section 1 defines S as the number of tags ('Let S be the number of tags'), then Worked example 1 writes 'tags S={N,V}', using S for the tag set. The same clash appears in Section 3, where S is the tag count in O(T·S²).
- ch 5 [low] Figure (trellis caption and edge styles): The caption says the dashed edge is not on the winning backtrace, but three solid edges (v1→n2, v1→v2, and the dashed n1→n2) are also off the winning path; only n1→v2 is on it. The solid/dashed coding suggests solid means 'on the winning backtrace', which is false. Also, the dashed edge n1→n2 is exactly the backpointer chosen at node N, so calling it 'not on the winning backtrace' without saying why confuses the reader.
- ch 5 [low] Section 3, memory sentence: 'Memory is O(T·S) with all backpointers, or O(S) scores if only the previous row is kept' can be read as saying Viterbi runs in O(S) memory, but Viterbi must store backpointers for every (t,j) to recover the path.
- ch 5 [low] Whole chapter, running text: Subscripts are dropped in the prose: qt, wt, αt(j), δt−1(i), ψt(j) are written flat, while the formula blocks correctly use <sub>. On a phone this makes the indices hard to follow.
- ch 6 [low] Figure spec, node c note: The note says 'one per position', which suggests a separate classifier per position. The text later says the weights are shared across all positions, so a student may read a contradiction.
- ch 6 [low] Worked example 1: The features are named only by the word or the previous tag ('word = flies', 'previous tag = N') but are given different weights for tag V and tag N. Under the definition f_j(i, t_{i−1}, t_i, x), a feature that does not mention t_i would add the same amount to every tag's score and cancel in the softmax, so the naming hides that the feature is conjoined with the candidate tag.
- ch 6 [low] Section 2, maximum entropy principle sentence: 'feature counts on training data match the observed counts' is imprecise; the constraint is on the model's expected feature counts, not on counts computed from training data (those are already the target).
- ch 6 [low] Exam traps, trap 1: 'Dividing by a sum over all positions and histories gives a CRF' misdescribes global normalisation: a CRF divides by one partition function summed over whole tag sequences, not over positions.
- ch 7 [high] Section 2, first paragraph: The symbol m is reused with two different meanings. Section 1 defines m as the number of feature functions, but here 'Z(x) sums over mⁿ sequences' and 'O(n m²)' need m to be the number of labels. A student will read 'mⁿ' as (feature functions)ⁿ, which is wrong, and will not see where the label-set size comes from in the O(n m²) cost. Section 1 already introduced |Y(x)| = 2ⁿ for that count.
- ch 7 [low] Quiz Q7 answer: The answer ends with 'Both take O(n m²)', but in this chapter m is the number of feature functions, so the complexity is written with the wrong symbol. The idea is right; only the notation is wrong.
- ch 8 [low] Worked example 1, step 5: Step 5 says the predicted span 'team in Pune' 'misses the gold boundary and type target'. Its type is LOC, which is the same type as the gold entity Pune (LOC); only the start and end are wrong. A student may conclude the type was also wrong and that a type mismatch is what caused the error.
- ch 8 [low] Quiz Q4 (and its contrast with Worked example 1, step 2): The worked example puts the title 'Mr' outside the person span (O), but Q4's answer puts 'Ms' inside the span as B-PER. The question does not say whether titles belong to the gold span, so a student who follows the worked-example convention (Ms/O Iyer/B-PER) would be marked wrong even though that answer is a legal BIO sequence.
- ch 9 [high] Worked example 1, step 2 (repeated in Quiz Q5): The triple (TCS, based_in, Pune) is read off "Rao joined TCS in Pune last Monday", but that sentence does not say where TCS is based. The phrase "in Pune" attaches to the joining event, so it locates Rao's employment, not the company's headquarters. A student copying this step will learn to invent triples the text does not support, which is the opposite of what IE must do.
- ch 9 [low] Section 2, hand-written patterns: The pattern "PER joined ORG in LOC" is said to give (PER, works_for, ORG), so the LOC slot is matched but never appears in the output. A reader cannot tell whether LOC is required, optional, or produces its own triple.
- ch 9 [low] Worked example 1, step 3: Step 3 writes precision as 2/3, where 3 is the number of sentences the pattern fired on. The formula in Section 3 defines the denominator as the number of triples produced, not the number of sentences. The two counts agree only if every firing yields exactly one triple.
