# c-sec-u2: free-model run

- Book: `books/cse/c-sec/c-sec-u2.html`
- Status: ok
- Model calls so far: 25 (88,607 tokens in, 196,641 out), 4.6 minutes

## Checker

```
c-sec-u2.html: 7 chapters, 11411 words, 8 figures, 131 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Lead: The claim that modular arithmetic "lets a computer handle 2048-bit numbers while storing only 2048 bits per value" is vacuous: any arithmetic stores 2048 bits for a 2048-bit value. The real point (intermediate products would grow to 4096 bits, reduction brings them back) is lost, so a student gets no idea why reduction matters.
- ch 1 [low] Section 1 vs Section 2/4: The ring of residues is written Zn in Section 1 and Z_n in the Section 2 heading, Q2 and Section 4. Two spellings for one object.
- ch 1 [low] Beyond: "Real cryptographic libraries never use the schoolbook method above" is misleading. Libraries do use square-and-multiply; what they replace is the modular multiplication/reduction inside it (Montgomery, Barrett). A student may conclude square-and-multiply is not used in practice.
- ch 1 [low] Beyond: "Barrett reduction for large batches" is vague and not the standard description.
- ch 2 [high] Section 1, second paragraph: The remainder bound is printed as "0≤r21 is the remainder", which is not a valid inequality. The "<" plus the following letter was read as an HTML tag and the text "r1" disappeared, so a student sees a meaningless "0≤r21".
- ch 2 [low] Exam traps, third bullet: "0≤r<b" puts "<" straight against the letter b; the browser can read "<b" as the start of a bold tag and swallow the rest of the line.
- ch 2 [low] Section 3 and the lead-adjacent notation in Q7 area: "x mod n is the inverse a−1 mod n" and "d=e−1 mod φ(n)" print the exponent −1 on the baseline, so students can read "a minus 1" instead of "a inverse".
- ch 2 [low] Exam traps, first bullet: The recurrence is written r_i = r_(i−2) − q r_(i−1) with an unlabelled q, but the quotient here is the one from the step that produced r_(i−1), not any earlier quotient.
- ch 3 [high] Figure caption: The caption reverses the nesting: it says groups sit inside rings and rings inside fields. Every field is a ring and every ring is an abelian group under addition, so the containment runs the other way (abelian groups ⊃ rings ⊃ fields). The caption contradicts both the sketch and its own aria text.
- ch 3 [high] Section 2, paragraph on composite n: The sentence is broken and unreadable: 'take a factor d with 1  1, so d has no inverse.' The comparison symbols and middle of the argument are missing, so the proof that a composite modulus fails is lost.
- ch 3 [low] Worked example 2, step 1: The line writes x⁴ = x⁴ + x + 1 + x + 1 without brackets. Read literally the right side just collapses back to x⁴, so the step does not visibly show the reduction and a student may not see where x + 1 comes from.
- ch 4 [high] Figure (Miller-Rabin on 341, base 2) — lead sentence: The sentence says 341 'passes the first check but fails after squaring', but the flowchart's first check is 'x = 1 or 340?', and the answer for 341 is no (x = 32). So 341 does not pass the first check; it fails it and then is caught by the squaring step. The sentence contradicts the diagram and can make a student think x was 1 or 340.
- ch 4 [low] Section 2, Fermat paragraph: 'The number 341 is not Carmichael, but it passes base 2' does not say which test it passes, and the Miller-Rabin steps follow immediately, where 341 fails base 2. This invites confusion between the two tests.
- ch 4 [low] Section 2, error bound sentence: 'At most 1/4 of bases pass one round' does not say how the bases are chosen; the 1/4 theorem is about bases picked uniformly at random from {2, 3, …, n − 2}.
- ch 4 [low] Lead: 'Every integer factors into primes in one way' is not true for 1 (and for negative integers as stated); the fundamental theorem covers integers greater than 1.
- ch 4 [low] Section 2, algorithm steps: The step list never states that Miller-Rabin applies to odd n only; the step 'Write n − 1 = 2^s d' and the bound s ≥ 1 assume n is odd.
- ch 5 [low] Section 1, the three bullets after the Fermat primality test sentence: The three bullets that explain how to cut an exponent down (write e = q(p−1)+r, replace a^e by a^r, use repeated squaring) have no introducing sentence. They appear straight after a remark about the Fermat primality test, so a student meets a procedure with no statement of what it is for or which condition it needs (gcd(a,p)=1).
- ch 5 [low] Section 1, Section 2, Section 3 and the quiz answers (inline exponents): Display formulas mark exponents with <sup>, but inline expressions lose them and appear as plain letters: 'ap ≡ a (mod p)', 'Replace ae by ar', '(ap−1)q ≡ 1q', 'an−1 ≡ 1 (mod n)', '3φ(10)−1'. Read literally, 'ap' looks like a times p and '3φ(10)−1' looks like 3·φ(10) − 1 = 11, so the meaning is lost.
- ch 5 [low] Quiz Q5: The question contradicts itself. The student is said to reduce 100 modulo 11 to 1, which would give 2¹ = 2, yet the student is quoted as claiming 2¹⁰⁰ ≡ 1 (mod 11). The claimed value 1 happens to be correct (because 100 mod 10 = 0), so the stem reads as if the student reached the right answer by the wrong route, which is not what the question wants to test.
- ch 6 [low] Section 1 (generalized form): The text says a solution exists "only when" every pair agrees, which reads as one-directional. The condition aᵢ ≡ aⱼ (mod gcd(mᵢ,mⱼ)) for all pairs is also sufficient: it is exactly the test for existence.
- ch 6 [low] Section 1 (definitions) and Section 2 (construction): The moduli are never restricted to integers greater than 1. If any mᵢ = 1 the notion of pairwise coprime (and the inverse Mᵢ⁻¹ mod mᵢ in Section 2) breaks down, because there is no inverse modulo 1.
- ch 6 [low] Lead: "to solve systems of congruences in coding and cryptography" repeats the general idea instead of naming a use, so it tells the student nothing concrete.
- ch 6 [low] Section 3 (RSA): The speed argument compares only the size of the two small exponentiations with one large one, and does not mention that the receiver performs two of them plus a recombination step. A student can lose track of the total cost.
- ch 7 [high] Section 1 and Quiz Q1: The definition says 'a nonzero integer a'. A nonzero multiple of p, such as a=p, satisfies x²≡a (mod p) with x=0, so the wording would call it a quadratic residue. But the Legendre symbol is 0 when p divides a, and standard definitions exclude p|a from being a nonzero quadratic residue. Quiz Q1 repeats the same wording.
- ch 7 [high] Section 1: The sentence 'The squares of 1, 2, …, p−1 produce every residue' is false. They produce only the quadratic residues, and only (p−1)/2 distinct nonzero values. A student may read 'every residue' literally.
- ch 7 [high] Quiz Q2: The question asks why there are exactly (p−1)/2 'nonzero residues modulo p'. Literally there are p−1 nonzero residue classes modulo p. The intended phrase is 'nonzero quadratic residues'.
- ch 7 [high] Section 2 and Quiz Q6: Quadratic reciprocity is stated for 'two odd primes p and q' without requiring them to be distinct. If p=q, the left side contains (p/p)=0 and the formula is false. Standard statements require distinct odd primes.
- ch 7 [low] Section 3: The text says 'Supplement rules handle −1 and 2' but never gives those rules, so the student cannot compute Jacobi symbols involving −1 or 2 from this chapter alone.
