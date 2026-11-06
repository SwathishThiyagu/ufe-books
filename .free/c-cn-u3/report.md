# c-cn-u3: free-model run

- Book: `books/cse/c-cn/c-cn-u3.html`
- Status: problems
- Model calls so far: 37 (151,713 tokens in, 300,458 out), 7.1 minutes

## Checker

```
c-cn-u3.html: 9 chapters, 18209 words, 10 figures, 179 KB
PROBLEMS:
 - text contains "I cannot"
```

## For the reviewer

- chapter 8: the figure cannot be drawn: label "Destination" is too long for its box; use a shorter label
- checker: text contains "I cannot"

## Reviewer notes (after any revision)

- ch 1 [low] Quiz Q2: The question asks for "the four parts around a frame's payload", but the answer lists flag, header, payload and trailer. Payload cannot be a part around itself, so a student cannot tell whether the answer should be three items or four, and the marking is unclear.
- ch 1 [low] Section 2 (byte-oriented framing): The byte values 0x7E (flag) and 0x7D (escape) are the ones used by PPP, but PPP does not restore the escaped byte as it is: after the escape byte it sends the original byte XORed with 0x20 (so 0x7E goes out as 0x7D 0x5E). The chapter states the simpler BISYNC-style rule (ESC then the byte itself) while borrowing PPP's numbers, so a student who later reads PPP will meet a rule that contradicts this page.
- ch 1 [low] Section 3, receiver rule: "After five 1s it discards the next 0" leaves out what happens when the bit after five 1s is a 1. In HDLC that bit is the start of the flag (or of the seven-1s abort sequence), not data, and a student may think the receiver always deletes a bit after five 1s.
- ch 2 [low] Section 1, two-dimensional parity, last sentence: The cost comparison 'more than single parity but less than a CRC of the same strength' is vague and the direction is wrong: for equal detection strength a CRC needs fewer check bits than two-dimensional parity, and a block of m rows and n columns actually needs m + n + 1 parity bits, not m + n, because of the corner bit.
- ch 2 [low] Section 2, Internet checksum: The chapter never says the sender must first set the checksum field itself to zero before summing the 16-bit words; a student who sums the header as it stands will compute the wrong value.
- ch 2 [low] Worked example 1, step 2: Step 2 says 'use a 3-bit remainder', but the register values printed in steps 3 and 4 are 4 bits wide (1001 = 9, 1011 = 11). A student may not see why a '3-bit' register holds 9.
- ch 3 [low] Section 1: The word 'burst' is used loosely. A burst is a run of consecutive bit errors, a separate concept; here the point is any pattern of fewer than dmin flips.
- ch 3 [low] Section 1 table: The column heading '2r' reads as 2 × r, while the entries (8 for r = 3, 16 for r = 4) are 2 raised to the power r.
- ch 3 [low] Worked example 1, step 9: 'Position 5 is d2 = 0. Flip it back to 0.' reads as if position 5 already holds 0; the received bit there is 1, only the sent value is 0.
- ch 3 [low] Quiz Q5: The first sentence, 'Two flipped bits can still leave the word at distance 1 from a valid codeword, so it can be detected', is confusing: detection comes from the received word being at distance 2 from the sent codeword and therefore not equal to any codeword.
- ch 3 [low] Section 3: The abbreviation SECDED is used without being expanded.
- ch 3 [low] Quiz Q2: The answer's reason ('Position 0 has no nonzero bit pattern') is vague. The concrete failure is that no check bit covers position 0, so a flip there gives syndrome 0, the same as a clean word.
- ch 4 [high] Lead paragraph: PPP is listed as carrying a version of flow control. PPP has no sequence numbers, no acknowledgements and no window; it only detects errors with its FCS and drops bad frames. Standard texts state that PPP provides error detection but no flow or error control.
- ch 4 [low] Exam traps, first trap: The consequence is stated wrongly. If a student puts the round-trip delay into a, the denominator does not double and the answer does not halve. With t_prop/t_frame = 2 the correct denominator is 1 + 2(2) = 5; using a = 2t_prop/t_frame gives 1 + 2(4) = 9, so U falls from 0.20 to 0.11, not to 0.10.
- ch 4 [low] Quiz Q7 answer: 'Hand corrupted data upward' is not what happens. The duplicate frame is not corrupted; its bits are intact. The receiver simply delivers a second copy of data it has already passed up, which silently duplicates or reorders the byte stream.
- ch 4 [low] Section 3, sliding window paragraph: 'Every acknowledgement slides the window forward by one position' is only true for one ACK per frame. Real sliding-window protocols send cumulative ACK n, meaning all frames up to n are received, which slides the window forward by several positions at once.
- ch 4 [low] Worked example 1, step 8 and answer: 'Two frames in the pipe each way' invites the reading that a window of 2 frames fills this link, which contradicts step 5 (5 frames needed). The two numbers measure different things and the step does not say so.
- ch 5 [high] Worked example 1, steps 7–8 (Selective Repeat trace): Steps 7 and 8 describe a receiver that buffers frames 3, 4, 5 and 6 while frame 2 is still missing, and a sender that sends 0,1,2,3 then 4,5,6 at once. That contradicts the chapter's own window rule. With k = 3 the Selective Repeat window is 4, so the receiver window spans frames 2 to 5 only and the sender's window is 2 to 5 after frames 0 and 1 are acknowledged: frame 6 cannot be sent and cannot be buffered before frame 2 is acknowledged. A student copying this trace learns a wrong receiver-window rule, even though the final total of 8 happens to be right.
- ch 5 [low] Worked example 1, step 10: It says Selective Repeat pays 'at the cost of a 4-frame buffer and per-frame timers at the receiver'. The per-frame timers are kept by the sender, as section 3 itself states; the receiver holds the buffer and does the reordering.
- ch 5 [low] Worked example 1, step 8: The problem statement says frame 2 is damaged in transit, but step 8 says 'Frame 2 is lost', and it also says the NAK and the timer both trigger the resend without distinguishing them.
- ch 6 [low] Section 2, HDLC frame fields (Address): The address field is described as naming the secondary station 'for which the frame is meant'. In HDLC the address field always carries the secondary station's address, in both directions: it is the destination address on frames sent by the primary and the source address on frames sent by the secondary. In a balanced (ABM) link there is no secondary at all; the field then names one of the two combined stations.
- ch 6 [low] Section 2, U-frame list: The U-frame names SNRM, SABM, DISC, UA and FRMR are used without being expanded, which an ESL reader cannot decode from the chapter.
- ch 7 [high] Section 3, binary exponential backoff paragraph: The backoff set is written as {0, 1, …, 2i − 1}. Without a superscript this reads as 2×i − 1, so a student would compute {0, 1, …, 5} after the third collision instead of {0, …, 7}. The exponent is missing even though the rest of the chapter uses <sup> for exponents.
- ch 7 [low] Lead paragraph: "it runs on every wired Ethernet LAN" is an overstatement. A modern switched, full-duplex Ethernet link has no shared medium, so CSMA/CD is not used there. The Beyond box later says exactly this, so the lead contradicts the chapter.
- ch 7 [low] Figure note and Exam traps: Exponent notation switches between <sup> (e<sup>−2G</sup>, 2<sup>i</sup>) and caret shorthand (2^i, 2i). On a phone the caret form is easy to misread as multiplication.
- ch 8 [high] Section 1, the sentence after the 64-byte explanation: The chapter says the receiver strips padding by using 'the length or type field'. This is only true when the 2-byte field holds a length. When it holds a type (the normal case, e.g. 0x0800 for IPv4), the field says nothing about how many payload bytes are real. The receiving MAC passes the padding up with the data, and the upper layer removes it using its own length (IPv4 uses its Total Length field). As written, a student will believe a type value can locate the end of the data.
- ch 8 [low] Quiz Q6, answer: The two PCs sit in different subnets (VLAN 10 and VLAN 20 normally carry different IP subnets), so PC A does not ARP for PC B's IP address. It ARPs for its default gateway and sends the packet to the router; only if no gateway is configured does an ARP for PC B's own address go out and fail. The conclusion (flooding stays inside VLAN 10, ping fails, a router or layer-3 switch is needed) is correct, but the stated first step is not.
- ch 9 [low] Section 2, third bullet of DCF: The backoff is said to be a random integer 'from 0 to CW', but CW is never given a starting value, and the chapter never says that CW doubles after each failed attempt. A student cannot tell what the first backoff range actually is, and misses the exponential-backoff part of DCF.
- ch 9 [low] Section 3, virtual carrier sensing paragraph: 'Any station that hears it sets its NAV' is too broad. The station the frame is addressed to must not defer, otherwise the receiver would silence itself and never send the ACK.
- ch 9 [low] Figure (sequence diagram): The dashed arrow labelled 'CTS sets NAV' is drawn as a message from Receiver to Other node, which suggests the receiver sends a separate frame to the third station. In reality the third station only overhears the CTS.
