# c-cn-u5: free-model run

- Book: `books/cse/c-cn/c-cn-u5.html`
- Status: ok
- Model calls so far: 31 (103,724 tokens in, 97,143 out), 4.2 minutes

## Checker

```
c-cn-u5.html: 8 chapters, 10500 words, 9 figures, 131 KB
OK
```

## For the reviewer

- chapter 4: a c program's shown output was replaced by its real output; check the text around it
- chapter 1: a c program's shown output was replaced by its real output; check the text around it
- chapter 8: a c program does not run (compile error: /tmp/tmpcmaz0lf8/p.c:1:10: fatal error: netinet/sctp.h: No such f)
- chapter 8: a c program does not run: compile error: /tmp/tmpim97gef5/p.c:1:10: fatal error: netinet/sctp.h: No such file or directory
    1 | #include <netinet/sctp.h>
      |          ^~~~~~~~~~~~~~~~
compilation terminated.
- chapter 3: a c program's shown output was replaced by its real output; check the text around it
- chapter 6: a c program's shown output was replaced by its real output; check the text around it
- chapter 8: the reviewer found 5 serious problem(s) and the revision did not pass the checks; read the review in the state folder

## Reviewer notes (after any revision)

- ch 1 [low] lead: The text says "The pair IP address + port is called a socket", which is inaccurate. A socket includes the transport protocol and is more than just the address‑port pair.
- ch 1 [low] section 1: Bullet states "Port 0 is reserved and never used for normal communication." This omits that port 0 can be used as a source port to let the OS choose an ephemeral port or as a wildcard in some APIs.
- ch 1 [high] quiz Q5: The answer says the OS may generate an ICMP “port unreachable” for a TCP segment with destination port 0. TCP does not use ICMP port‑unreachable; the correct reaction is to drop the segment and typically send a TCP RST.
- ch 2 [high] Quiz Q5: The description of the TCP header is wrong. It says TCP has a 20‑byte header plus a 4‑byte option for the checksum, giving 24 bytes total. In reality the TCP checksum is part of the standard 20‑byte header; there is no extra 4‑byte option.
- ch 2 [low] Section 1, bullet list for Source Port: Says "0 means no port" which may be unclear. Port 0 is reserved and not used for normal applications.
- ch 2 [low] Section 1, bullet list for Destination Port: Mentions range 0‑65535 without noting that 0 is also reserved for destination ports.
- ch 3 [high] figure spec: The Src Port and Dst Port notes are swapped. The source port note shows 80 and the destination port note shows 34567, which contradicts the text where Src Port = 34567 and Dst Port = 80.
- ch 3 [high] Quiz Q6: The answer lists FIN and RST as the two flags used to terminate a TCP connection. RST aborts a connection; graceful termination uses FIN (and ACK).
- ch 3 [low] Section 2: The flag field is called "Data Offset" in the TCP standard, not just "Offset".
- ch 3 [low] Section 2: The list of control bits omits the ECN‑related flags (CWR, ECE) and the NS flag, which are part of the modern 9‑bit flag field.
- ch 3 [low] Section 3: The SYN‑ACK description does not mention the Window field, which is present in every segment.
- ch 3 [low] Section 2: The description of the Window field does not mention the optional Window Scale option that allows windows larger than 65 535 bytes.
- ch 4 [high] Quiz Q6: The question asks for the state after receipt of the final ACK by the side that initiated the close, but that side never receives the final ACK; it sends it. The side that receives the final ACK (the passive closer) goes to TIME_WAIT.
- ch 4 [low] Section 1, formula: The formula "ack = seq_sent + 1" is presented as a general rule, but it only holds when the acknowledged segment contains a SYN or FIN and no data.
- ch 4 [low] Section 2, termination description: The description does not mention the TCP states LAST_ACK (for the side that sent the first FIN) and TIME_WAIT (for the side that sent the final ACK).
- ch 5 [high] Section 2: Sender limit and zero‑window probing: The condition for sending a zero‑window probe is stated as "If allowed = 0, send a zero‑window probe (a 1‑byte segment)". This is incorrect. A probe is sent only when the advertised receive window (rwnd) is zero, not when allowed is zero because outstanding already equals rwnd.
- ch 5 [low] Section 2: Sender limit and zero‑window probing: The wording "If allowed = 0, send a zero‑window probe" is ambiguous and reinforces the high‑severity error.
- ch 5 [low] Worked example 1: C code: The code calculates the number of segments using only rwnd and ignores cwnd, while the textual explanation uses min(cwnd, rwnd). This mismatch may confuse students.
- ch 5 [low] Section 1: Receive window field: The phrase "rwnd is measured from the left edge of the receiver buffer to the next free byte" can be misinterpreted as an offset rather than a size.
- ch 5 [low] Lead paragraph: The term "tiny probe segments" is vague; the standard term is "zero‑window probe".
- ch 6 [high] Quiz Q3: The answer assumes cwnd before loss is 8 MSS, but the connection is in slow start with cwnd = 4 MSS when the three duplicate ACKs arrive. In slow start the cwnd has not yet doubled for that RTT, so cwnd before loss is 4 MSS. Therefore ssthresh = floor(4 ÷ 2) = 2 MSS and cwnd after fast retransmit = 2 MSS.
- ch 6 [low] Section 2, loss detection table: The bullet "Triple duplicate ACKs → fast retransmit; stay in congestion avoidance" may mislead readers because after fast retransmit the cwnd is reduced to ssthresh and then congestion avoidance continues. The phrase "stay in congestion avoidance" skips the reduction step.
- ch 7 [high] Section 2 – token‑bucket formula: The formula "Available tokens after time t = min(B, C·t)" assumes the bucket starts empty and ignores any initial token count. Standard token‑bucket behavior is tokens = min(B, B₀ + C·t) where B₀ is the initial number of tokens (often equal to B for a full bucket).
- ch 7 [high] Exam trap Q5 (list of reasons for loss): First reason says "the EF queue is empty, causing packets to be dropped," which is incorrect; an empty queue cannot cause drops.
- ch 7 [low] Section 3 – core router scheduling description: Statement "Core routers schedule packets using weighted‑fair queuing (WFQ) based on class" may mislead because EF traffic is normally given strict priority, not WFQ.
- ch 7 [low] Section 1 – delay‑sensitive bullet list: Interactive gaming, which is delay‑sensitive, is omitted from the list.
- ch 8 [high] Section 1: The term "Association ID" is not defined in the SCTP standard. SCTP uses a 32‑bit Verification Tag, not an Association ID, to identify an association.
- ch 8 [high] Section 2: The handshake description uses the TCP term "Initial Sequence Number (ISN)". SCTP does not have an ISN; it uses an Initiate Tag.
- ch 8 [high] Section 2: It states that the COOKIE‑ACK carries the association ID. COOKIE‑ACK only acknowledges the cookie; it does not contain an association identifier.
- ch 8 [high] Section 2: The description of the cookie says it is a MAC of the client’s IP address, the ISN and a timestamp. The ISN is incorrect; the cookie is computed over the Initiate Tag (and other parameters).
- ch 8 [high] Quiz Q2: The answer says COOKIE‑ACK carries the secret cookie, which is wrong. The cookie is first sent in INIT‑ACK and then echoed back in COOKIE‑ECHO.
- ch 8 [low] Code example: The socket is created with SOCK_STREAM, which is less common for SCTP examples and may confuse students who expect SOCK_SEQPACKET.
- ch 8 [low] Section 1: The sentence "The protocol guarantees that a transmitted chunk arrives intact or is retransmitted" could be misread as guaranteeing no loss at all.
