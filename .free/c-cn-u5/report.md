# c-cn-u5: free-model run

- Book: `books/cse/c-cn/c-cn-u5.html`
- Status: ok
- Model calls so far: 36 (141,524 tokens in, 233,197 out), 6.8 minutes

## Checker

```
c-cn-u5.html: 8 chapters, 13946 words, 9 figures, 154 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Figure spec (Section 3 figure): The block spec sets direction to 'down' while the figure shows demultiplexing, which is data moving up the stack (node a is 'Segment from IP' with the note 'network layer hands up'). Rendered arrows would point the wrong way and contradict the text.
- ch 1 [low] Lead: The wording 'adds a 16-bit port number to the IP address' can be read as if the port is written into the IP address field. The port sits in the transport header; the IP address and port are only used together as a lookup key.
- ch 2 [high] Quiz Q2, answer: The answer says IP's total length 'can include padding to the minimum frame size'. That is wrong: the IPv4 total length field counts only the IP header plus the IP payload; link-layer padding added to reach the Ethernet minimum frame size is not counted, and padding is exactly the case where IP length already tells the receiver where the datagram ends. A student who memorises this will justify UDP's length field with a false reason.
- ch 2 [low] Quiz Q4: The wording 'sets the IPv4 checksum field to 0000' can be read as the 16-bit header checksum inside the IPv4 header, which has nothing to do with UDP. The question means the UDP checksum field of a datagram travelling over IPv4.
- ch 2 [low] Section 1, formula and Q6, answer: 65527 bytes is correct as the largest value the length field can describe, but over IPv4 an application can never send that much: the IPv4 total length caps the IP datagram at 65535 bytes, so the real maximum UDP payload is 65535 − 20 − 8 = 65507 bytes. As written, a student may believe a 65527-byte payload actually goes on an IPv4 network.
- ch 3 [low] Section 2, acknowledgment formula ack = S₀ + R: S₀ was just defined as the first data byte 'in this direction', but an acknowledgment number always names bytes of the other direction. A student can plug in the wrong side's starting number and get a wrong ACK.
- ch 3 [low] Section 3, header table row 'Reserved + flags': The row is 12 bits, but the flags listed are only eight (URG, ACK, PSH, RST, SYN, FIN, CWR, ECE), and with three reserved bits that adds to 11. The 12th bit (NS, the ECN-nonce bit) is missing, so the bit count does not add up for a student.
- ch 3 [low] Section 3, urgent pointer row: 'Points to urgent data' is vague. The standard meaning is that it gives the sequence number of the byte after the urgent data, so the receiver knows where urgent data ends; the loose wording invites the common wrong answer.
- ch 3 [low] Figure, aria text: The aria description calls the diagram 'six 32-bit words', but the sixth block is the options field of 0 to 40 bytes, not a 32-bit word. The visual and the description disagree.
- ch 3 [low] Quiz Q6 answer: One duplicate ACK does not by itself trigger fast retransmit; the sender normally needs three duplicate ACKs. 'Can trigger fast retransmit' is loose enough that a student may write that a single duplicate ACK causes the retransmission.
- ch 3 [low] Lead: The sequence number is described only as 'which byte this segment starts at'. For a segment carrying no data, such as a pure ACK, the sequence number is the number of the next byte the sender will send, not the start of data in that segment.
- ch 4 [low] Section 1, handshake bullets (third segment): The text says that after the third segment 'the connection is now ESTABLISHED at both ends'. This hides a real distinction: the client becomes ESTABLISHED when it sends the third ACK, but the server reaches ESTABLISHED only when that ACK arrives. If the ACK is lost the server stays in SYN-RECEIVED and retransmits SYN+ACK, while the client already believes the connection is open. A student meeting this after the TIME-WAIT retransmission discussion can get confused about who is in which state.
- ch 4 [low] Quiz Q6: The question asks which state shows a half-close and the answer gives only CLOSE-WAIT, but the chapter's own state notes say both FIN-WAIT-2 and CLOSE-WAIT are half-closed. As written, the answer contradicts the earlier text.
- ch 4 [low] Lead paragraph: 'then waits in TIME-WAIT' reads as if the connection, or both hosts, wait in TIME-WAIT. Only the side that sends the final ACK does.
- ch 4 [low] Section 3, state table, CLOSING row: 'Both sides sent FIN before ACKs' is imprecise: in CLOSING each side has already ACKed the peer's FIN; what is still outstanding is the ACK of its own FIN. A student can read it as 'before sending any ACK', which is wrong.
- ch 4 [low] Section 3, paragraph after the table: 'Read the diagram once' points students to a full state-transition diagram that is not printed in this chapter; the only figure is a message sequence chart. A reader on a phone will search for a diagram that is not there.
- ch 5 [low] Section 1: LastByteRcvd and LastByteRead are called "byte counts". They are byte positions (sequence numbers counted from the start of the connection), not counts of bytes. A student may think LastByteRcvd = 3000 means 3000 bytes were counted in some other way, and misread the subtraction LastByteRcvd − LastByteRead.
- ch 5 [low] Section 2, sender side: Nagle's algorithm is stated as "hold small segments until a full one is ready". As written, a sender with one small segment outstanding would wait forever for a full segment. Nagle also releases the buffered small data as soon as the outstanding ACK arrives.
- ch 5 [low] Section 3: The sentence "if the ACK covers byte M and advertises W, the sender may send up to byte M + W" is ambiguous about whether M is the last byte acknowledged or the ACK number. With the second reading the limit is off by one (M + W − 1).
- ch 5 [low] Exam traps, third trap: A field value of 65535 is not 64 KB; 64 KiB is 65536 bytes, and the text itself says "about 64 KB" in Section 1. The trap states it as exact.
- ch 5 [low] Beyond: "QUIC replaces the single byte window" is wrong wording: the TCP window is a 16-bit field, not a single byte. A student may take it as a factual claim about TCP.
- ch 6 [high] Lead: The lead says TCP grows cwnd slowly at first. Slow start doubles cwnd every round trip, which is exponential, not slow. The chapter's own exam trap says the same, so the lead contradicts the body and can confuse a student.
- ch 6 [low] Lead: A video call is normally carried over UDP/RTP, not TCP. 'From a UPI payment to a video call' can make students think video calls use TCP.
- ch 6 [low] Section 3: The Reno fast-recovery rule is simplified to cwnd = ssthresh. In the common Kurose treatment, Reno sets cwnd = ssthresh + 3 MSS on the third duplicate ACK and deflates to ssthresh later; the simplified cwnd = ssthresh is the Forouzan convention. The chapter does not say which convention it follows, so students using the other textbook may be marked wrong.
- ch 6 [low] Quiz Q4: The answer says 'round 6 enters congestion avoidance'. cwnd at round 5 is 16 MSS, equal to ssthresh, so congestion avoidance already applies during round 5 and round 6 is 17 MSS. The explanation is off by one round.
- ch 7 [high] Quiz Q2 answer: It says a faster link 'does not stop packets from overtaking each other in the queue'. A FIFO queue never reorders packets, so no overtaking happens; the real cause of jitter is that the queue length (and so the waiting time) changes from packet to packet, and a faster link only shortens each wait. A student will come away with a false picture of jitter as packet reordering.
- ch 7 [low] Section 3 and Exam traps: The TSpec is defined with r and p in bits per second, and the trap states this as the rule. The standard TSpec (RFC 2210) expresses the token bucket rate, token bucket depth, peak rate, minimum policed unit and maximum packet size all in bytes (rates in bytes per second). The chapter is self-consistent, but the trap turns a local convention into a claim about the standard.
- ch 7 [low] Figure 'What a reserved flow passes through': The chain puts admission control in the per-packet path between the classifier and the token-bucket policer. Admission control runs once, at reservation setup, not on every packet; only classification, policing and queueing are per packet. The caption hints at this but the boxes do not.
- ch 8 [high] Quiz Q6: The chunk length field is wrong. A DATA chunk's length field covers the 4-byte chunk header plus the 12 bytes of DATA-specific fields (TSN 4 + stream id 2 + stream sequence 2 + PPID 4) plus the payload, so it is 4 + 12 + 100 = 116, not 104. The packet size is therefore 12 + 116 = 128 bytes, not 116. This also contradicts the worked example, which correctly uses a 16-byte DATA chunk header.
- ch 8 [low] Worked example 1, step 1: The 16 bytes are called the 'DATA chunk header', but Section 2 defines the chunk header as 4 bytes and says DATA 'adds four fields after the chunk header'. The same phrase used with two meanings can confuse a reader.
- ch 8 [low] Section 3, cookie paragraph: 'After sending INIT-ACK the server stores nothing' is too absolute; the server still keeps its secret key and listening socket. What it avoids is per-association state.
- ch 8 [low] Section 2, DATA flags: The I (immediate) flag is left out of the DATA chunk flag list, which may make students think only three flags exist.
