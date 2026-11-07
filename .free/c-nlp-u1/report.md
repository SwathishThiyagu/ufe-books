# c-nlp-u1: free-model run

- Book: `books/cse/c-nlp/c-nlp-u1.html`
- Status: ok
- Model calls so far: 43 (173,306 tokens in, 318,238 out), 10.0 minutes

## Checker

```
c-nlp-u1.html: 8 chapters, 15076 words, 9 figures, 171 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q5: The answer says code-mixing brings a second language and a second script into the sentence. Its own Hinglish example, "kal meeting cancel hai", is written in Roman script, not Devanagari, so there is no second script. Script mixing (writing Hindi in Devanagari inside an English sentence, or romanised Hindi) is a separate problem from code-mixing, and a student would carry the wrong claim into the exam.
- ch 1 [low] Section 3 (semantic ambiguity) and Quiz Q4(ii): "The chicken is ready to eat" is presented as the case where "the structure is fixed". In the two readings the chicken fills different roles: it is the eater in one and the thing eaten in the other, so the argument structure differs, and many texts call this an argument-structure or control ambiguity rather than a purely semantic one. Telling students the structure is fixed here can mislead them.
- ch 1 [low] Lead: The lead defines NLP as turning human text into something a computer can act on, but Section 1 says the input is text or speech and the output can be a translation or a reply, and Section 2 includes speech transcription and text-to-speech. A student reading only the lead will think NLP is text-only and spoken input belongs elsewhere.
- ch 2 [low] Lead and Section 1: The lead promises five levels, but Section 1 describes seven: phonetics, phonology, morphology, syntax, semantics, pragmatics and discourse. The figure and Q1 have only the five from phonology to pragmatics, with phonology at the base, while the text says to start at the bottom with phonetics. A student cannot tell whether phonetics is one of the five.
- ch 2 [low] Section 1: The sentence giving the unit and question ('The unit is the utterance in context; the question is ...') comes after the discourse sentence, so it reads as if it describes discourse, and discourse is left with no unit at all.
- ch 2 [low] Worked example 1, step 1: The step is labelled Phonology but contains only phonetic facts (syllable count, the phones /d/ and /bæŋk/, the allomorph of 'the'). This is exactly the phonetics-phonology confusion the third exam trap warns against.
- ch 2 [low] Section 2, ambiguity list, phonology line: 'read has two pronunciations' is a spelling-to-sound (homograph) ambiguity of the written word, not an ambiguity inside the sound system, so it sits awkwardly as the phonology example.
- ch 2 [low] Quiz Q6, answer: The answer says semantics uses the neighbouring words 'from syntax and morphology'. Neighbouring words are a syntactic (phrase) fact; morphology supplies the word forms and lemmas, not the surrounding words.
- ch 2 [low] Section 2, sentence 'Discourse cannot resolve it until earlier sentences and syntax give possible antecedents': 'it' has no stated antecedent; the previous sentences talk about intent, so the student cannot see that the point is about referring expressions.
- ch 3 [high] section 2, Star R* bullet: The Thompson construction for R* is stated with only three of its four ε arcs. The bullet lists the skip arc (new start to new final), the entry arc (new start into R's start) and the loop-back arc (R's final to R's start), but never connects R's final to the new final. A student who follows the bullet builds a machine in which no string that enters R can ever reach the final state, so R* would accept only the empty string.
- ch 3 [low] section 3, bound on DFA states: The bound is written as '2k for k NFA states'. As written it reads as two times k, which is not the subset-construction bound; it also renders as plain text on the phone.
- ch 3 [low] section 3, definition of a DFA: The definition says a DFA has 'exactly one arc per symbol from each state', but the DFA table given just below, and the sentence 'If no arc exists, the machine dies and rejects', both describe a partial DFA with dashes. A student meets two different definitions in the same section.
- ch 3 [low] section 4, last paragraph of the section: 'balanced brackets, square brackets, and XML tags' repeats the same thing twice, since brackets are square brackets.
- ch 4 [high] Section 3, hyphen decision: The text says state-of-the-art can be one token or five. It has four word parts and three hyphens: keeping it whole gives 1 token; splitting into words gives 4 tokens; treating each hyphen as punctuation gives 7 tokens. Five is not a possible count.
- ch 4 [high] Section 2, naive sentence-splitting rule: The stated naive rule is an end mark followed by a space. That rule does not split 5.5, ₹1,250.50 or site.in because the period is not followed by a space; so listing decimal points and site names as failures of this rule is wrong. A closing quote after the full stop is a missed boundary, not an internal-period over-split.
- ch 4 [low] Section 1, placeholder sentence: The sentence 'Replacing numbers, dates and money amounts with placeholders such as  or ' leaves the placeholders blank, so the example is missing.
- ch 4 [low] Section 1, Unicode normalization example: 'The word café is either U+00E9 or e followed by U+0301' is imprecise: U+00E9 is the accented e, not the whole word café.
- ch 4 [low] Section 3, Indian languages: Hindi postpositions are normally separate words, not attached inside one whitespace token; agglutination in these examples is mainly case endings. The sentence overgeneralises by saying a token can carry postpositions.
- ch 4 [low] Quiz Q7: The answer says the sentence-final period 'disappears from the token list'. The period is actually swallowed into the e-mail token rao@site.in.; what disappears is the separate period token, and the token count drops by one.
- ch 4 [low] Section 2 checklist: 'Shield the shielded cases' is unclear and appears to be a typo.
- ch 5 [high] Quiz Q4: The answer says ponies → poni removes 3 characters. 'ponies' has 6 letters and 'poni' has 4, so only 2 characters (e and s) are removed. The worked example correctly gives 2 for the same ies → i rule on lies, so the quiz contradicts the chapter.
- ch 5 [high] Section 2 (step-1a s rule), Figure stem row, Worked example steps 2, 5 and 7, Exam traps, Quiz Q4: The s-rule is stated as 'delete a final s when the remaining stem contains a vowel'. Porter's rule adds one condition: the preceding part must contain a vowel not immediately before the s. Without that condition the chapter stems gas → ga and was → wa, but standard Porter leaves both unchanged (the vowel a sits directly before the s). Q4's answer 'gas → ga, 1 character removed' is therefore wrong under the standard definition, and so are the 'wa' entries.
- ch 5 [low] Worked example, step 2: The parenthetical for cats → cat contains the garbled phrase 'stem ga-free', which has no meaning and confuses the reader about why the s is deleted.
- ch 5 [low] Section 4, second paragraph: 'patient is empty in general text' is unclear; 'empty' is not a property of a word, and a student may read it as an empty string.
- ch 5 [low] Section 1, third paragraph: 'lemmatization is slower, needs a lexicon and a tag, and is correct' contradicts Section 3 and the exam traps, which show that a wrong tag gives a wrong lemma.
- ch 5 [low] Section 2, measure formula: The form C(VC)ᵐV ends in a vowel, yet the very next sentence writes cat as CVC to get m = 1. As written the formula does not cover consonant-final words, so a careful student sees a contradiction.
- ch 6 [high] Section 4 (analysis and ambiguity): The example 'better may be the comparative of good or an adjective' does not show two different analyses: the comparative of good is itself an adjective, so the two alternatives collapse into one and a student cannot see the ambiguity.
- ch 6 [low] Section 1 (regular plural) and Quiz Q4: The chapter calls x a sibilant ('box ends in x, a sibilant'). In phonetics the sibilant sounds are s, z, sh, zh, ch, j; x is a letter whose sound ends in the sibilant /s/.
- ch 6 [low] Section 4, last sentence of paragraph 2: 'morphological analysis feeds tagging, not replaces it' is ungrammatical and reads awkwardly for second-language readers.
- ch 7 [high] Section 3, candidate generation sentence: The count of distance-1 candidates is wrong by roughly a factor of two. Insertions number 26(L+1) (all letters at L+1 gaps) and substitutions number about 26L, so insertions plus substitutions are about 52L+26, not 26L. The stated total of about 26L + L is far short of the true neighbourhood size.
- ch 7 [high] Worked example 1, step 4, cell t vs t: The first term uses the wrong cell value. The cell above D[2][4] is 2, so the deletion term is 2+1 = 3; the text writes 1+1 = 2. The minimum is still 1, but the arithmetic shown is wrong.
- ch 7 [high] Quiz Q5 answer: The lower bound is wrong. The triangle inequality also gives d(A,C) ≥ |d(A,B) − d(B,C)| = |2 − 3| = 1, so d(A,C) cannot be 0.
- ch 7 [low] Section 1, transposition and Damerau distance: The definition given (one adjacent swap at cost 1, no substring edited twice) is the restricted form often called optimal string alignment; true Damerau–Levenshtein allows repeated edits and the restricted form does not obey the triangle inequality stated just above. A careful reader may think all the metric properties still hold once transposition is added.
- ch 8 [high] Section 3, sentence on vocabulary size: It says vocabulary size is far smaller than the token count because it is counted after normalization. That is the wrong reason. The vocabulary (types) is far smaller than the token count because words repeat many times; normalization only trims the vocabulary a little further. A student will conclude that lowercasing is what makes the two numbers differ.
- ch 8 [low] Section 2, bullet on near-duplicates: The terms shingle and Jaccard overlap are used before being defined, then used again in Quiz Q4. An ESL reader on a phone has nothing to fall back on.
- ch 8 [low] Section 2, sentence 'Do the split before any cleaning tuned on the test data.': The wording is circular: nothing should ever be tuned on test data, so the sentence does not tell the student what to do with the split and the cleaning steps.
- ch 8 [low] Worked example 1, output block: Six bare numbers are printed with no units and no labels (1.56 and 1.248 in particular are MB, not characters). The student has to match them back to the steps by position.
