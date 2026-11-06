# c-block-u2: free-model run

- Book: `books/cse/c-block/c-block-u2.html`
- Status: ok
- Model calls so far: 19 (65,772 tokens in, 152,990 out), 4.2 minutes

## Checker

```
c-block-u2.html: 7 chapters, 13532 words, 8 figures, 139 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3 (key length paragraph): The sentence reads "For a random n-bit key, there are 2n possible keys." Written as 2n this says the keyspace is twice n, which is wrong. It should be 2 to the power n. Students will read "2n" as a multiplication and get a nonsense keyspace that also contradicts the formula that follows.
- ch 1 [low] Quiz Q2, answer: "It does not hide the input" clashes with the previous sentence calling the hash one-way. A one-way function does hide the input from inversion; the real reason a hash gives no confidentiality is that it is unkeyed and deterministic, so anyone can test a guessed message and match the digest. As written a student may think a hash is reversible or that it leaks the message.
- ch 2 [low] Section 1: Three security properties: The section says there are three security properties, but the bullet list contains five items: preimage, second-preimage, collision, avalanche and birthday. Avalanche and birthday are not security properties, so students may mistakenly count them as promises of the hash.
- ch 2 [low] Section 2, padding formula: The formula uses 448 without saying where it comes from. A student may not see that 448 = 512 − 64, which is the space left for the 64-bit length field.
- ch 2 [low] Section 1, collision resistance bullet: Calling collision resistance 'stronger' than second-preimage resistance while later saying SHA-256 gives only about 128 bits of collision security can confuse students. The word 'stronger' refers to the security requirement, not to the cost of the generic attack.
- ch 2 [low] Beyond: The phrase 'SHA-3, BLAKE3 or hash-based signatures' mixes hash functions (SHA-3, BLAKE3) with signature schemes (hash-based signatures), which are different kinds of tools.
- ch 3 [high] Section 1 formula and Exam traps bullet on hash pointers: The formula says a block header stores an address plus a hash. A Bitcoin block header stores only the 32-byte previous block hash; there is no stored address. This contradicts Section 2's 80-byte header and Q1's statement that the address is implicit. The exam trap repeats the same error.
- ch 3 [high] Section 1 verification steps; Section 2; Section 3 bullet 'Checking one link costs one SHA-256 call'; Quiz Q5: Bitcoin's block hash is double SHA-256 (SHA-256d) of the 80-byte header, not a single SHA-256. The chapter says H is SHA-256 and that checking one Bitcoin link costs one SHA-256 call.
- ch 3 [high] Section 1 paragraph on names: 'Linking box', 'linking box using SHA' and 'digital structure' are not standard names for a hash pointer. Claiming that some textbooks use them is unsupported and will mislead exam answers.
- ch 3 [low] Section 1 paragraph after the formula: The sentence 'One flipped bit in block i−1 changes H(block i−1)' can make students think the transaction body is directly hashed. Only the header is hashed; a body edit changes the Merkle root, and the header hash changes only after the header is updated.
- ch 3 [low] Beyond: 'Proof of history' is not a skip-list technique for jumping back over a header chain. It is a different timing/verifiable-delay construction, so grouping it with skip lists is inaccurate.
- ch 4 [low] Section 1, formula note: The formula box gives R = H( H(h1 || h2) || H(h3 || h4) ), which is only the four-leaf case, but it appears inside the general build section that starts with n transactions. A student can read it as the general definition.
- ch 4 [low] Section 1, formula note, and Section 3: The note says H is 'SHA-256 in Bitcoin'. Bitcoin's Merkle tree applies SHA-256 twice: the leaves are txids = SHA-256(SHA-256(tx)) and each internal node is SHA-256(SHA-256(left || right)). Stating only SHA-256 is imprecise.
- ch 4 [low] Section 3, last paragraph: 'Some syllabi call this topic digital structures in blockchain' is vague and the name is not a recognised term, so it does not help the reader map the chapter to a syllabus.
- ch 5 [low] Section 1, paragraph 4: "A longer key is not automatically a better key" can be misread: within one system a longer key is strictly better. The point being made is only that key lengths cannot be compared across different hard problems.
- ch 5 [low] Exam traps, trap 1: The chain "77/2 mod 17 is 77 × 9 = 13" writes a false equality: 77 × 9 = 693, which is congruent to 13 modulo 17, not equal to it. A student copying this line into an answer loses a mark for notation.
- ch 5 [low] Quiz Q3, answer: "No efficient algorithm is known for a well-chosen secp256k1 curve" is muddled: secp256k1 is one fixed curve, so it cannot be "well-chosen" or otherwise. The hardness belongs to the discrete log problem on the group of points of that curve.
- ch 6 [low] Section 2, definition of the order n: The wording says n is 'how many distinct multiples G, 2G, 3G, … exist before the pattern returns to the point at infinity'. A student counting those multiples gets n − 1 (for the chapter's own example, n = 11 gives 10 distinct multiples before 11G = O), which contradicts the definition and the later use of n as the modulus (for example, k⁻¹ mod n, r = R.x mod n).
- ch 6 [low] Beyond: 'Bitcoin's Taproot upgrade moved to Schnorr signatures' suggests ECDSA was replaced. Taproot added Schnorr (BIP340) for Taproot spends, while ordinary (non-Taproot) inputs still use ECDSA, so a student may write that Bitcoin no longer uses ECDSA.
- ch 7 [low] Quiz Q8: The answer begins 'Usually no', which suggests the public key can sometimes be computed from an address. It never can: the address is a hash, and hashing is one-way. Seeing the public key in a spending transaction is not deriving it from the address.
- ch 7 [low] Section 3, WIF: The text gives one WIF form only. WIF has two forms, and the choice matters for the address. The uncompressed form is version || 32-byte key || checksum. The compressed form inserts a 0x01 flag byte before the checksum, so the same private key imported in the two forms gives two different public-key encodings and two different addresses.
- ch 7 [low] Section 2, SegWit sentence: Saying 'SegWit addresses use bech32 instead, start with bc1' is incomplete. Only native SegWit addresses use bech32 and start with bc1. SegWit wrapped in P2SH uses a Base58Check address that starts with 3, and Taproot uses bech32m with bc1p.
- ch 7 [low] Figure, address node note: The note 'Base58Check, 25 bytes' on the Address node suggests the address itself is 25 bytes. 25 bytes is the payload written into Base58Check; the address you see is Base58 text, typically 26 to 35 characters.
- ch 7 [low] Quiz Q2: The checksum is listed as a reason for hashing the public key, but the checksum is added by the Base58Check encoding step, not by the hash. A student may think hashing produces the checksum.
