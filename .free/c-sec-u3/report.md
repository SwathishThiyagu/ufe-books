# c-sec-u3: free-model run

- Book: `work/claude_figs/c-sec-u3/tree/books/cse/c-sec/c-sec-u3.html`
- Status: ok
- Model calls so far: 43 (171,151 tokens in, 335,611 out), 12.4 minutes

## Checker

```
c-sec-u3.html: 9 chapters, 15549 words, 10 figures, 205 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, columnar transposition example: The stated ciphertext XSEEMA has six letters, but the plaintext EXAMS has five and the chapter itself says the ciphertext is split as 2, 2, 1. Column 2 gives X, S; column 1 gives E, M; column 3 gives A, so the ciphertext is five letters. A student following the worked steps cannot get XSEEMA, which makes the example look wrong.
- ch 1 [low] Section 2, first paragraph after the affine formula: "a = 2 sends both A (0) and N (13) to 0" is only true when b = 0. With a general b the two letters collide on the value b, not on 0, so the sentence is slightly inaccurate as written.
- ch 1 [low] Section 3, bullet list and example on columnar transposition: "padding the last row if it is short" suggests adding filler letters, but the example then leaves the third cell of row 2 empty and counts only 5 ciphertext letters. A student may add an X as filler and get a different rectangle.
- ch 2 [low] Section 1 (perfect secrecy, last paragraph): The stated necessary condition for perfect secrecy is incomplete. It names key length and uniformity but leaves out that the key must be independent of the message and used only once (the reuse point appears only later, in Section 2). Stated as a general theorem, students may read it as sufficient.
- ch 2 [low] Quiz Q4: The answer stops at m₁ ⊕ m₂. In practice the XOR of two natural-language (or otherwise redundant) messages is enough to recover both plaintexts, so the answer understates what the attacker gains.
- ch 3 [low] Section 3, RC4 deprecation paragraph: It says the first keystream bytes are biased 'and many short-term biases exist'. This suggests all biases are confined to the start of the keystream, so a student may conclude that discarding the first few hundred bytes makes RC4 safe. The well-known single-byte and byte-pair biases also persist throughout the keystream.
- ch 3 [low] Section 1, PRG formula line: The formula uses negl(n) and only labels it 'a negligible function'. A reader on a phone will not know what negligible means, and the indistinguishability bound cannot be judged without it.
- ch 4 [high] Section 2, first paragraph: The left and right halves of the round output are stated the wrong way round. The chapter's own formula gives L₁ = R₀ and R₁ = L₀⊕F(R₀,K₁), so the RIGHT half of the output is L₀⊕F(R₀,K₁) and the LEFT half is R₀. The text says the opposite, and this contradicts the formula, the figure and Worked example 1 (where L₁ = 0110 = R₀ and R₁ = 1001 = L₀⊕F).
- ch 4 [low] Section 2, second paragraph: Feeding Lᵢ as the right input and Rᵢ as the left input into the round formula returns the two halves in swapped positions: the round outputs Rᵢ₋₁ on the left and Lᵢ₋₁ on the right, i.e. Rᵢ₋₁ Lᵢ₋₁, not Lᵢ₋₁ Rᵢ₋₁. As written a student may think the ordering comes back exactly as the plaintext.
- ch 5 [high] Section 3, paragraph on two-key 3DES: The sentence 'an attacker who searches K1 and K2 separately does roughly 2⁵⁶ + 2⁵⁶ work' is wrong and contradicts the 112-bit figure given in the same sentence. 2⁵⁶ + 2⁵⁶ is about 2⁵⁷, so a student who follows that reasoning would conclude 2-key 3DES is worth only ~57 bits. The keys in EDE are used in nested calls, not side by side, so they cannot be searched independently and added.
- ch 5 [low] Worked example 1, step 3: The line 'Binary 01 = 1 × 1 + 0 × 2? No: read as a two-bit number, 01 = decimal 1' poses and answers its own doubt. A student reading it may think the '1 × 1 + 0 × 2' reading was a real alternative that gives a different value, which it does not.
- ch 5 [low] Quiz Q7 answer: The described attack does not actually give the stated 2¹¹² cost. Encrypting P under all K1 and decrypting C under all K3, then 'matching the middle value', leaves K2 unaccounted for: the two lists cannot be matched directly because D_K2 sits between them. A careful student will be unable to reproduce the 2¹¹² figure from this description.
- ch 6 [low] Figure (AES round structure): The only exit path to ciphertext leaves from AddRoundKey and loops through MixColumns, so the diagram never shows the final round skipping MixColumns; a student reads the last 'round' as SubBytes, ShiftRows, MixColumns, AddRoundKey once more.
- ch 6 [low] Lead: 'Some syllabi call the family Rijndael' can be read as AES and Rijndael being the same thing; Rijndael also defines 192- and 256-bit blocks, which AES does not use.
- ch 7 [high] Section 2, CBC IV rules (chosen-IV sentence): The described chosen-IV attack is written wrongly: 'set IV = guessed P₁ ⊕ C₁, then watch whether the first ciphertext block repeats.' C₁ is the output of E_K that the attacker has not seen yet, and E_K(G ⊕ C₁ ⊕ P₁) cannot produce a repeat this way. A student will memorise a formula that does not work.
- ch 7 [high] Quiz Q4: The question says 'CTR mode with the same toy cipher' but never gives the key. The previous question (Q3) used K = 1111, so the natural reading gives keystream E_K(0000) = 1111 and C₁ = 1010 ⊕ 1111 = 0101, not the shown 0000. The shown answer silently uses K = 1010 from Worked example 1.
- ch 7 [low] Section 3, CTR definition: 'Tᵢ = nonce ‖ counter + i' can be read as (nonce ‖ counter) + i, i.e. addition applied after concatenation, which is not what is meant.
- ch 7 [low] Section 3, counter rules paragraph, and Exam traps bullet 3: The subscript 1 and 2 are used for blocks of two different messages (C₁ ⊕ C₂ = P₁ ⊕ P₂), while everywhere else in the chapter the same subscripts mean block 1 and block 2 of one message. A student may misread this as a relation between two blocks of a single ciphertext.
- ch 8 [high] Quiz Q3: The arithmetic in the worked answer is wrong. With DP = count/2^6, count = 2^6 × DP = 64 × (1/32) = 2. The quiz writes 32 × (1/32) = 2, which evaluates to 1, not 2. The final answer of 2 ordered inputs is right, but the shown step contradicts it.
- ch 8 [low] Section 2, last lines: The claim 'Matsui's linear attack on DES used about 2^43 known plaintexts in its original report' is imprecise. The 2^43 figure is the data volume of Matsui's later experimental attack on DES; the original theoretical estimate is usually quoted as about 2^47 known plaintexts. A student may memorize the wrong number for an exam.
- ch 8 [low] Section 3: The body text opens with 'From trails to key bits.', which just repeats the section heading. It reads like a stray line.
- ch 9 [low] Section 2, PRF game: The game says the challenger 'answers with a random function f(x)', but never says that f is fixed once at the start of the game. A student can read this as a fresh random value for every query, which would make the two worlds distinguishable after one repeated input.
- ch 9 [low] Section 2, PRP definition: 'A PRP is a PRF with X = Y where F_K is a bijection; the adversary may also query the inverse' mixes two definitions. The plain PRP game gives no inverse oracle; letting the adversary query F_K⁻¹ defines a strong PRP.
- ch 9 [low] Worked example 1, step 1: Step 1 converts K, m0 and m1 to decimal, but every later step works in binary and never uses the decimal values. The step adds work without adding understanding.
- ch 9 [low] Quiz Q2 answer: 'learning b with high probability' is too weak. In a deterministic scheme the adversary computes E_K(m0) itself and compares, so it learns b with certainty.
- ch 9 [low] Quiz Q7 answer: The answer says the attacker 'learns a relation about m'. The attack is stronger: the decryption oracle returns m ⊕ Δ, so the attacker flips the bits back and recovers the whole plaintext m, then compares it with m0 and m1.
- ch 9 [low] Exam traps, last bullet: 'Decrypt-then-MAC' is not a standard name for a composition. The standard names are encrypt-then-MAC, MAC-then-encrypt and encrypt-and-MAC. The real danger is that the receiver decrypts data it has not authenticated yet (padding-oracle style attacks), and MAC-then-encrypt/encrypt-and-MAC are not proven CCA-secure.
- ch 9 [low] Section 3, encrypt-then-MAC paragraph and Section 2, block cipher sentence: Cross-references are written as plain text ('see Chapter 3.6'), which breaks the book's rule that chapter references are links a phone reader can tap.
