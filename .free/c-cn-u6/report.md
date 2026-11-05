# c-cn-u6: free-model run

- Book: `books/cse/c-cn/c-cn-u6.html`
- Status: ok
- Model calls so far: 38 (126,779 tokens in, 129,284 out), 6.9 minutes

## Checker

```
c-cn-u6.html: 7 chapters, 10429 words, 8 figures, 122 KB
OK
```

## For the reviewer

- chapter 4: a c program's shown output was replaced by its real output; check the text around it
- chapter 4: a c program prints
HTTP/1.1 404 Not Found
Date: Thu, 05 Nov 2026 15:17:03 GMT
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Connection: close
Server: cloudflare
Age: 1
cf-cache-status: HIT
CF-RAY: a55cd2b9dcf08e40-IAD
alt-svc: h3=":443"; ma=86400

241
<!doctype html><html lang=en><head><meta charset=utf-8><link rel=icon href=data:,><meta name=viewport content="width=device-width,initial-scale=1">
but the chapter shows
HTTP/1.1 404 Not Found
Date: Thu, 05 Nov 2026 15:17:03 GMT
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Connection: close
Server: cloudflare
Age: 1
cf-cache-status: HIT
CF-RAY: a55cd2b94ad1d62c-IAD
alt-svc: h3=":443"; ma=86400

241
<!doctype html><html lang=en><head><meta charset=utf-8><link rel=icon href=data:,><meta name=viewport content="width=device-width,initial-scale=1">
Make the shown output and any explanation match what the program really prints
- chapter 5: give 6 to 8 quiz questions
- chapter 6: the figure cannot be drawn: label "FROM:<student@college.edu>" is too long for its box; use a shorter label
- chapter 2: a c program does not run (compile error: ing terminating " character
   20 |     printf("Server received: )
- chapter 2: a c program does not run (compile error: 1c7rt/p.c:20:1: error: missing terminating " character
   20 | ",)
- chapter 2: a c program does not run (compile error: jyrvc/p.c:20:1: error: missing terminating " character
   20 | ",)
- chapter 2: a c program does not run: compile error: ing terminating " character
   20 |     printf("Server received: %s
      |            ^~~~~~~~~~~~~~~~~~~~
/tmp/tmpdplmr8g4/p.c:21:1: error: missing terminating " character
   21 | ", buf);
      | ^~~~~~~~
/tmp/tmpdplmr8g4/p.c:22:5: error: expected expression before ‘const’
   22 |     const char *reply = "ACK";
      |     ^~~~~
/tmp/tmpdplmr8g4/p.c:26:14: error: expected ‘;’ bef
- chapter 2: a c program does not run: compile error: yc1b_/p.c:20:1: error: missing terminating " character
   20 | ", buf);
      | ^~~~~~~~
/tmp/tmpkbnyc1b_/p.c:21:16: error: expected ‘)’ before ‘;’ token
   21 |     close(sock);
      |                ^
      |                )
/tmp/tmpkbnyc1b_/p.c:19:11: note: to match this ‘(’
   19 |     printf("Received: %s
      |           ^
/tmp/tmpkbnyc1b_/p.c:22:14: error: expected ‘;’ bef
- chapter 2: a c program does not run: compile error: r5glg/p.c:20:1: error: missing terminating " character
   20 | ", buf);
      | ^~~~~~~~
/tmp/tmp7ndr5glg/p.c:21:16: error: expected ‘)’ before ‘;’ token
   21 |     close(sock);
      |                ^
      |                )
/tmp/tmp7ndr5glg/p.c:19:11: note: to match this ‘(’
   19 |     printf("Received: %s
      |           ^
/tmp/tmp7ndr5glg/p.c:22:14: error: expected ‘;’ bef
- chapter 2: the reviewer found 3 serious problem(s) and the revision did not pass the checks; read the review in the state folder

## Reviewer notes (after any revision)

- ch 1 [high] Section 1 (formula): The round‑trip time formula RT = T_req + T_proc + T_resp omits propagation delay, so it underestimates the true RTT.
- ch 1 [low] Lead: Sentence reads "peer‑to‑peer are the two main ways" which is grammatically incorrect.
- ch 1 [low] Quiz Q3: Unit notation "kb" may be confused with kilobytes; the answer should specify kilobits.
- ch 2 [high] Section 2, TCP server code: The printf string contains a literal line break ("Server received: %s
" is written as "Server received: %s
" with an actual newline), which is invalid C syntax.
- ch 2 [high] Section 2, TCP server code: The code uses struct sockaddr_in but does not include the required header <netinet/in.h>. This will cause a compilation error on many systems.
- ch 2 [high] Section 3, UDP example: Only a client program is shown, yet the displayed output "Received: Hi" assumes a server that echoes the message. No server code is provided, so the example is misleading.
- ch 2 [low] Figure specification (three‑way handshake): The label for the fourth message uses an undefined variable "y" ("ACK, ack=y+1").
- ch 2 [low] Section 2, TCP socket programming steps: The description of send() does not mention that it may send fewer bytes than requested, requiring a loop to ensure full transmission.
- ch 2 [low] Section 2, TCP socket programming steps: The list of system calls omits the domain argument (AF_INET) for socket(), which is essential for beginners.
- ch 3 [low] Section 2, bullet list: Root returns only NS records for the .in TLD. In practice the root also provides glue A records for those NS servers.
- ch 3 [low] Section 3, cache eviction statement: It says "least‑recently‑used entries are evicted first" which is not true for all resolvers; some use size‑based or time‑based policies.
- ch 3 [low] Exam traps, TTL cache entry bullet: The wording "many resolvers keep the stale entry until a new query is made" may suggest that stale data can be served, which is incorrect.
- ch 3 [low] Quiz Q4 answer: Answer ignores EDNS0, which allows UDP messages larger than 512 bytes, so the justification is incomplete.
- ch 3 [low] Section 1, TTL formula: Formula "remaining_TTL = TTL – elapsed" can produce negative values if elapsed > TTL.
- ch 3 [low] Section 2, iterative query description: The phrase "resolver sends an iterative query to a root server" may confuse students who think the client sends iterative queries.
- ch 4 [high] Worked example 1, step 1: Object size conversion uses 1.2 KB × 1024 B/KB × 8 bits/B = 9 728 bits, which is incorrect. 1.2 KB = 1.2 × 1024 = 1228.8 B, multiplied by 8 gives 9 830.4 bits (≈9 830 bits).
- ch 4 [high] Worked example 1, code output section: The displayed server response is HTTP/1.1 404 Not Found, but a GET request to http://example.com/index.html returns 200 OK with the example domain page. The output does not match the described scenario.
- ch 4 [low] Section 2, idempotence paragraph: Only GET, PUT and DELETE are listed as idempotent, omitting HEAD (and OPTIONS) which are also idempotent.
- ch 4 [low] Section 1, URL description: Host is described only as a domain name, but an IP address is also a valid host component.
- ch 4 [low] Section 3, Connection: keep-alive description: The text implies that the keep-alive header must be sent, while in HTTP/1.1 persistent connections are the default.
- ch 4 [low] Exam traps, idempotent methods point: The trap mentions only GET, PUT, DELETE as idempotent, missing HEAD (and OPTIONS).
- ch 5 [high] Quiz Q4: The answer says that in passive mode uploads use a different port range than downloads, which is incorrect. In passive FTP both uploads and downloads use a client‑initiated connection to the same server‑chosen passive port.
- ch 5 [low] Worked example 1 description: The phrase "Each command‑reply pair (USER, PASS, PASV, STOR, final 226) adds 0.04 s of latency" incorrectly lists the final 226 as a pair; it is only a reply.
- ch 5 [low] Quiz Q3 answer: The answer counts "final 226" as a separate command‑reply pair, which can confuse students because 226 is only a reply.
- ch 5 [low] Section 3 Python code: The code does not send a QUIT command before closing the control connection, which is the proper way to end an FTP session.
- ch 6 [low] Section 1: The sentence "Port 587 is used for submission with STARTTLS, which upgrades the connection to TLS after a plain handshake" is inaccurate. STARTTLS upgrades the connection after the client sends the STARTTLS command, not after a plain handshake.
- ch 6 [low] Worked example 1: The example calls the attachment size "200 KB" but then converts using 1 KB = 1024 bytes, which is actually kibibytes (KiB). This may confuse students who think 1 KB = 1000 bytes.
- ch 6 [low] Quiz Q5: The answer "EHLO , MAIL FROM:, RCPT TO:, DATA, , ., QUIT" contains stray commas, a missing placeholder for the message body, and does not clearly show the terminating period line.
- ch 6 [low] Section 2: The formula description does not explicitly state that Rate must be in bits per second while Size is in bytes, which could lead to unit mismatch.
- ch 7 [high] Section 3: The statement "FTPS works like FTP but adds TLS before the control connection is used" is inaccurate for the widely used explicit FTPS mode, where TLS is started after the client sends an AUTH TLS command, not before the control connection is established.
- ch 7 [high] Exam trap Q7: The answer claims the server is completely safe from a DoS attack on port 80 because the firewall blocks that port. While the server process does not receive the traffic, the attack can still consume upstream bandwidth or overload the firewall, affecting service availability.
- ch 7 [low] Lead paragraph: The phrase "firewalls, NAT, and encryption protect data before it reaches the network" suggests NAT provides confidentiality, which it does not.
