# c-cn-u3: free-model run

- Book: `books/cse/c-cn/c-cn-u3.html`
- Status: problems
- Model calls so far: 18 (67,597 tokens in, 90,139 out), 11.5 minutes

## Checker

```
c-cn-u3.html: 9 chapters, 11822 words, 10 figures, 142 KB
PROBLEMS:
 - chapter "data-link-protocols-hdlc-and-ppp": needs a <div class="quiz"> with at least 5 <details data-level=...> questions
```

## For the reviewer

- chapter 1: a c program's shown output was replaced by its real output; check the text around it
- chapter 9: a c program's shown output was replaced by its real output; check the text around it
- chapter 7: a python program's shown output was replaced by its real output; check the text around it
- chapter 7: give 6 to 8 quiz questions
- chapter 7: the figure cannot be drawn: cannot evaluate "G*exp(-2*G)": name 'G' is not defined
- chapter 7: a python program prints
Retry 0: backoff = 0.0 µs
Retry 1: backoff = 0.0 µs
Retry 2: backoff = 0.0 µs
Retry 3: backoff = 256.0 µs
but the chapter shows
Retry 0: backoff = 0.0 µs
Retry 1: backoff = 51.2 µs
Retry 2: backoff = 51.2 µs
Retry 3: backoff = 358.4 µs
Make the shown output and any explanation match what the program really prints
- chapter 6: a c program's shown output was replaced by its real output; check the text around it
- chapter 6: give 6 to 8 quiz questions
- chapter 6: worked example 1: the worked example states [21005.0] but recomputing it gives [522.0]; fix the steps and the answer so they match the correct values
- checker: chapter "data-link-protocols-hdlc-and-ppp": needs a <div class="quiz"> with at least 5 <details data-level=...> questions

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q3: The provided stuffed payload and final frame are incorrect. The answer shows "Stuffed payload: 10111111001 0" and frame "01111110 101111110010 01111110", which do not follow the bit‑stuffing rule.
- ch 1 [low] Section 1 (Why framing is needed): Sentence "Both ends add the flag at the front and the rear of the payload" may mislead students to think the receiver also adds flags.
- ch 1 [low] Section 2 (Bit stuffing algorithm) – bullet point: Bullet "When the count reaches five, output a 0 and reset the count" is ambiguous about handling the inserted 0.
- ch 1 [low] Quiz Q3 answer formatting: The answer shows an extra space and a stray "0" after the payload string, making it hard to read.
- ch 2 [high] Section 2 (One's‑complement checksum): The text says the checksum catches "all errors that flip an odd number of bits". One's‑complement checksum does not guarantee detection of every odd‑bit error; it only guarantees detection of all single‑bit errors.
- ch 2 [high] Section 3 (CRC with G(x)=x³+x+1): The description claims the generator detects "any odd number of bit errors". The generator 1011 does not contain the factor (x+1), so it cannot guarantee detection of all odd‑bit errors.
- ch 2 [high] Worked example 1, step 4 (checksum verification): The verification step shows the sum as 0x1FFFF and then adds a carry to get 0xFFFF, which is incorrect for one's‑complement addition.
- ch 2 [low] Section 1 (Two‑dimensional parity): The sentence about the intersection cell may be unclear to beginners.
- ch 2 [low] Section 3 (CRC example): The phrase "Append three zero bits: 11010011101100000" does not state that the number of zeros equals the degree of the generator.
- ch 2 [low] Section 4 (When to use which method): The statement "CRC adds 2–4 bytes" could be more specific.
- ch 2 [low] Quiz Q4 answer: The answer gives the remainder "110" but does not mention that the remainder length is 3 bits.
- ch 3 [high] Quiz Q5 (apply, 6 marks): The answer says a double‑bit error makes the overall parity odd. In an (8,4) SEC‑DED code a double‑bit error gives a non‑zero syndrome while the overall parity check is satisfied (even). The answer therefore misstates the detection condition.
- ch 3 [low] Section 1, formula for p3: The formula line for p3 ends with a colon and no expression.
- ch 4 [high] Section 2: Sliding‑window flow control: The description mixes two different protocols. It first says the receiver maintains a receive window of size N to buffer out‑of‑order frames (Selective‑Repeat behavior) and later says that if a frame is lost the receiver discards it and all later frames (Go‑Back‑N behavior). This contradiction can confuse students.
- ch 4 [low] Section 2: Sliding‑window flow control, bullet "When ACK = k arrives, sender slides window to start at k and may send new frame k+N‑1.": The wording is ambiguous about which new frame can be sent after the window slides.
- ch 4 [low] Exam traps bullet "Using only the forward propagation delay in a makes a too small, giving an inflated efficiency.": The phrase "makes a too small" is grammatically unclear.
- ch 5 [high] Section 1 (formula) and Quiz Q6: The inequality W ≤ (M+1)/2 is stated as a requirement for both Go‑Back‑N and Selective Repeat. For Go‑Back‑N the correct bound is W ≤ M (or W ≤ M+1‑1), not half the sequence‑number space. Only Selective Repeat needs W ≤ (M+1)/2 to avoid ambiguity.
- ch 5 [high] Quiz Q6: The answer given is “W ≤ (M+1)/2”, which is incorrect for Go‑Back‑N as explained above.
- ch 5 [low] Section 2, step description: The sentence “Timer for frame 2 expires before ACK=3 arrives.” is misleading because ACK=3 never arrives when frame 2 is lost; the timer expires because no ACK for frame 2 is received.
- ch 6 [high] Section 3: PPP encapsulation and LCP negotiation: The PPP Protocol field is described as a one‑byte field, but PPP uses a two‑byte (16‑bit) Protocol field.
- ch 6 [high] Section 3: PPP encapsulation and LCP negotiation: PPP is said to be defined in ISO‑3309, which actually defines HDLC. PPP is defined in RFC 1661 (and later in ISO/IEC 1172).
- ch 6 [high] Worked example 1 (code and step‑by‑step CRC calculation): The C code uses the reflected polynomial 0x8408 (CRC‑16‑CCITT) while the example claims to use the HDLC CRC‑16 polynomial 0x8005 reflected. The computed CRC values (0xE1C0, 0xC2A1, 0x522D) do not match the HDLC CRC‑16 for the given data.
- ch 6 [high] Worked example 1 (output line): The line "output: CE71" appears without explanation and does not correspond to the CRC or the transmitted bit sequence.
- ch 6 [low] Quiz Q3 answer: The answer gives a placeholder CRC value "0x3B4F (example result)" which may mislead students.
- ch 7 [high] Section 2, bullet about jam signal: The text says "jam signal for 32 bytes". Ethernet jam signal length is 32 bits (4 bytes), not 32 bytes.
- ch 7 [low] Section 3, bullet "Backoff range = [0, CW‑1] where CW starts at 15 and doubles after each failure": The phrase "doubles after each failure" is not precise. The contention window updates as CW = (CW+1)·2 − 1 (i.e., roughly doubles but adds one).
- ch 7 [low] Section 2, bullet "Ethernet slot time = 512 bits (64 bytes) at 10 Mbps": Slot time is defined as 512 bits regardless of link speed; the statement ties it only to 10 Mbps, which may mislead.
- ch 7 [low] Section 3, bullet "Sense the channel for DIFS (Distributed Inter‑Frame Space)": DIFS is a waiting period after the channel is sensed idle, not a sensing action itself.
- ch 8 [high] Section 1: The CRC‑32 formula and description say the CRC is computed over Dest‖Src‖Type‖Payload only. It omits any padding bytes and also any VLAN tag that may be present, which is incorrect.
- ch 8 [high] Section 2: The TCI numeric formula uses PCP×2⁹ + DEI×2⁸ + VID, which shifts the fields by only 9 and 8 bits. In 802.1Q the PCP occupies bits 15‑13 and DEI bit 12, so the correct shifts are 13 and 12.
- ch 8 [high] Quiz Q4: The computed TCI value 0x0C64 is wrong because it uses the incorrect shift amounts from the faulty formula.
- ch 8 [high] Section 3: The text says “If the payload plus headers is smaller than 46 bytes, padding is added…”. The 46‑byte minimum applies to the payload alone, not to payload + headers.
- ch 8 [low] Section 2, bullet list: The instruction “Adjust the FCS to cover the new frame” is vague; the FCS must be recomputed, not merely adjusted.
- ch 8 [low] Section 3, padding rule: The bullet “If total < 64 bytes, add padding bytes of value 0 until it equals 64.” mixes the concept of total‑frame padding with payload padding, which can confuse students.
- ch 9 [high] Section 1, formula for contention window: The formula CW = 2^m – 1 is incomplete. The IEEE 802.11 standard defines CW = (2^m)·(CWmin+1) – 1, where CWmin is the minimum contention window (15 for DCF).
- ch 9 [high] Section 2, DCF description of DIFS: DIFS is given as 34 µs while the slot_time used in the same section is 20 µs (2.4 GHz band). For 2.4 GHz, DIFS = SIFS + 2·slot_time = 10 µs + 2·20 µs = 50 µs, not 34 µs.
- ch 9 [high] Worked example 1 (backoff calculation): The example uses DIFS = 34 µs together with slot_time = 20 µs, which is inconsistent with the 2.4 GHz parameters. This leads to an incorrect waiting time before RTS.
- ch 9 [high] Quiz Q4: The answer is contradictory and wrong. It first says CW = 2^1 – 1 = 1, then says CW = 2×(CWmin+1) – 1 = 31. The correct new CW after the first collision is 31.
- ch 9 [low] Section 1, MAC header description: The description mentions only source address, destination address, and frame type, omitting the other address fields (Address1‑4) that are part of the 802.11 MAC header.
