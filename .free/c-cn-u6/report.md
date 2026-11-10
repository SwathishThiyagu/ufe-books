# c-cn-u6: free-model run

- Book: `work/claude_figs/c-cn-u6/tree/books/cse/c-cn/c-cn-u6.html`
- Status: ok
- Model calls so far: 29 (107,864 tokens in, 212,510 out), 6.3 minutes

## Checker

```
c-cn-u6.html: 7 chapters, 12782 words, 8 figures, 144 KB
OK
```

## For the reviewer

- chapter 4: the figure cannot be drawn: label "www.example.com" is too long for its box; use a shorter label

## Reviewer notes (after any revision)

- ch 1 [low] Lead, second sentence and Section 1 opening: The lead states flatly that every network application is a pair of processes in two places. Section 3 of the same chapter describes peer-to-peer applications where many processes take part and no fixed pair exists, so a student meets a claim the chapter itself later contradicts.
- ch 1 [low] Section 1, server paragraph: The sentence 'The client must not need to know the server's schedule' is unclear: it is not a property students will recognise, and it reads as if the client has to check some timetable. The intended point is simply that the server is always listening, so the client may knock at any time.
- ch 2 [low] Figure (sequence spec): The labels 'accept() SYN-ACK' and 'recv(), reply' suggest that accept() sends the SYN-ACK and that recv() sends a message. In reality the TCP stack sends the SYN-ACK and accept() only returns afterwards; recv() only reads, the reply is a send(). A student can carry away the wrong picture of what these two calls do.
- ch 2 [low] Lead and Section 1: 'every client differs in its own address' is loose. Two clients behind one NAT can share the same IP address and differ only in source port. Read literally, the sentence says the IP address alone separates the clients.
- ch 2 [low] Beyond: io_uring is described as a kernel-bypass framework. It is not kernel bypass: it still goes through the kernel, using shared ring buffers to avoid one system call per operation. DPDK is the true kernel-bypass example.
- ch 3 [low] Section 2 and Worked example 1: The three-contact, six-message count assumes the resolver already has the address of each name server, usually from glue records. If the NS target is out-of-bailiwick and no glue is supplied, the resolver must resolve the NS name first and the count rises.
- ch 3 [low] Section 2: 'That is three server contacts and six messages' can be misread as the total DNS messages including the host-to-resolver query and reply; the six count is only resolver-to-name-server messages.
- ch 3 [low] Quiz Q5: Lowering TTL to 60 s only gives 60 s expiry after the IP change if the TTL was lowered at least one old TTL (86400 s) in advance. Caches that already stored the old 86400 s TTL keep it until it expires.
- ch 3 [low] Figure note: The figure note '13 root servers' can be read as 13 physical machines, while the exam trap correctly says these are 13 named server identities served by many anycast copies.
- ch 4 [low] Lead: The lead says flatly that HTTP runs on top of TCP. That is true for HTTP/1.0, 1.1 and 2, but HTTP/3 runs over QUIC on UDP, and the 'Beyond' note later says exactly that, so a careful student sees a contradiction.
- ch 4 [low] Section 1, message block: The reply declares Content-Length: 5120 bytes but the body shown is the 18-byte line <h1>Networks</h1>. A student checking the arithmetic will think the header is wrong.
- ch 4 [low] Section 1, request line rule (also Exam traps, last point): 'never the full URL' is stated as absolute. When a request goes to a proxy, the request line carries the absolute URI (GET http://host/path HTTP/1.1); only requests to an origin server carry the path alone.
- ch 4 [low] Section 2, status code table: Code 500 is given the reason phrase 'Server Error'. The standard reason phrase is 'Internal Server Error'; 'server error' is the name of the 5xx class, not of 500.
- ch 4 [low] Section 3, pipelining paragraph: 'On a slow link this removes several round trips' mixes up bandwidth and delay. Pipelining pays off when the round-trip time is large compared with transmission time; a slow (low-bandwidth) link with a short RTT gains little.
- ch 4 [low] Figure caption: 'the reply carries the same status line the request expects' is misleading: a request contains no status line, only a start line with method, path and version.
- ch 5 [low] Section 2, passive mode paragraph: It says passive mode is the default in most clients 'and browsers today', but the Beyond section says web browsers have dropped FTP support. The two statements contradict each other.
- ch 5 [low] Worked example 1 (and the PORT bullet in Section 3): The client address is 192.168.1.7, a private address, yet it is downloading with active FTP. Section 2 has just explained that active mode fails behind NAT because the announced address is private, so the example contradicts the text and can confuse a student.
- ch 5 [low] Section 3, reply-code classes: The class list gives 2xx, 3xx, 4xx and 5xx but leaves out 1xx, even though 150 (a 1xx preliminary reply) appears in the session list. A student cannot classify 150 from the text given.
- ch 5 [low] Lead and Quiz Q2: 'Status check' and especially 'progress query' suggest FTP has a command that reports transfer progress. Standard FTP has no such command; the status command is STAT (and ABOR for aborting).
- ch 5 [low] Figure (sequence diagram): The diagram jumps from PORT to file bytes without the 150 opening data connection reply on the control connection, and it draws two overlapping messages from Server :20 ('data from port 20' and 'file bytes') for one transfer.
- ch 5 [low] Quiz Q8: The question asks for 'which single change', but the answer offers two (FTPS or SFTP). The answer also mixes two facts: a passive eavesdropper can read USER, PASS and file bytes, but changing file bytes needs an active injection.
- ch 6 [low] Quiz Q5: The answer says the client sends DATA after the 354 reply, but 354 is the server's reply to DATA, so the client has already sent DATA and then sends the body. As written, the step order is wrong and contradicts the session shown in Section 2.
- ch 6 [low] Quiz Q6: A 550 is a permanent (5xx) rejection, so the sender's server bounces the message at once, not "later". "Later" applies to temporary 4xx failures that are retried.
- ch 6 [low] Section 1: The lookup step is described only as "looks up the receiver's domain with DNS". Students will not learn which record type actually gives the receiver's mail server.
- ch 6 [low] Section 2 (comment on the session): "EHLO opens the session and names the client" is loose: the session is opened by the server's 220 greeting, and EHLO's other job — asking the server to list its ESMTP extensions — is not mentioned.
- ch 6 [low] Worked example 1, output line: The output shows bare numbers "400" and "406" with no labels or units, so it is unclear which is the encoded photo and which is the total.
- ch 7 [high] Section 2, Worked example 1, and Quiz Q3: Every exponent has lost its superscript, so the formulas and the arithmetic read as wrong. "C = Me mod n", "M = Cd mod n", "gx mod p", "gxy mod p" look like products of variables named Me or Cd. In the worked example the lines "53 mod 33 = 125", "262 = 676", "264 ≡ 162 = 256", "267 = 264 × 262 × 26" are nonsense as printed; the quiz answer "C = 73 mod 55 = 343 mod 55 = 13" and "1327 mod 55" have the same problem. A student cannot follow the squaring steps or copy the formula correctly.
- ch 7 [low] Section 2, Diffie–Hellman sentence: x and y appear in g<sup>x</sup> and g<sup>xy</sup> without ever being defined, so the reader cannot tell which values are secret and which are public. The phrase "with public prime p and base g" also leaves the impression that the exponents are public too.
- ch 7 [low] Exam traps, last bullet: It says only a stateless filter cannot inspect malware inside encrypted HTTPS on port 443. A stateful firewall cannot do that either, so the trap understates the limitation and contradicts Section 4, which says plainly that a firewall fails to see encrypted malware inside port 443.
- ch 7 [low] Section 2, RSA definition: The condition on e is incomplete: the chapter gives e·d ≡ 1 mod φ(n) but never states that e must be coprime with φ(n), which is exactly why the inverse d exists. A student may pick e = 2 and find no d.
