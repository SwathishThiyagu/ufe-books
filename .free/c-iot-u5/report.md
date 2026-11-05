# c-iot-u5: free-model run

- Book: `books/cse/c-iot/c-iot-u5.html`
- Status: ok
- Model calls so far: 20 (64,454 tokens in, 142,538 out), 4.1 minutes

## Checker

```
c-iot-u5.html: 7 chapters, 13080 words, 8 figures, 143 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, Chennai water-meter example and figure: The term 'cloud broker' is used for the MQTT/message broker. In standard cloud computing, a cloud broker is a different role: an entity that intermediates between cloud providers and consumers. The same sentence also makes the broker keep months of history and run billing, but a message broker only ingests messages; storage and billing are separate services. A student can confuse the two meanings.
- ch 1 [low] Section 3, deployment models: Hybrid cloud is defined as joining public and private resources only. The standard definition is a composition of two or more distinct cloud infrastructures, which may include a community cloud. The narrow wording can cost marks.
- ch 1 [low] Section 1, first paragraph: 'The cloud also adds servers when traffic rises' can make students picture physical servers. In cloud computing, capacity is added as virtual servers or instances; the provider may add physical hosts invisibly.
- ch 2 [low] Section 2, paragraph on SAS versus certificates: The contrast says a SAS token is easy on a microcontroller 'while a certificate needs a trusted clock and more memory'. This hints that SAS does not need a clock, but the SAS expiry is an absolute time, so a wrong clock breaks SAS exactly as the exam trap later says. The point about memory is correct; the clock part is misleading.
- ch 2 [low] Section 1, last paragraph (pricing): The pricing sentence lists 'messages in and out, device-minutes connected, and operations such as shadow updates' as if it were common to both platforms. That is the AWS IoT Core model; Azure IoT Hub is billed per throughput unit per day (with a daily message allowance per unit), not per message or per connected minute.
- ch 2 [low] Beyond: The pointer to the next topic is plain text ('the subject of Chapter 5.3'), so a reader on a phone cannot tap through to it, unlike other cross-references in the book.
- ch 3 [low] Beyond: Delta-of-delta encoding is said to cut storage 'for slowly changing signals'. Delta-of-delta is normally applied to time stamps that arrive at regular spacing; for slowly changing values the usual choices are delta or XOR encoding.
- ch 3 [low] Worked example 1, step 3 and exam traps: The example fixes 1 MB = 1,000,000 bytes, but many students use 1 MB = 1,048,576 bytes (1 MiB), so answers can differ in the last digits. The chapter never tells the student which convention to follow in an exam.
- ch 3 [low] Exam traps, second bullet: 'A one-minute average stores 60 values per hour, not 60 samples per second' mixes time bases in a confusing way; a student can misread it as saying the average gives 60 values per second.
- ch 4 [high] Exam traps, third bullet ("Revoked or expired certificates sit in a revocation list"): Expired certificates are not put on a revocation list. A CRL or OCSP responder lists certificates that were revoked before expiry. An expired certificate simply stops being valid because its validity period has ended, and verifiers reject it on the date check alone.
- ch 4 [low] Exam traps (replay bullet) and Quiz Q5 answer: "The resent message is encrypted again inside a new session" hides the key condition. TLS ciphertext captured off the wire cannot be replayed into a new TLS session, because the session keys differ. The replay only works when the attacker has valid credentials of its own (a stolen token, a compromised device) or holds the plaintext payload and can publish it again as a legitimate client.
- ch 4 [low] Quiz Q6 answer: The answer gives two conflicting retention rules for the same raw data: keep 1-minute readings only for a short diagnostic window such as 24 hours, then delete raw readings after 90 days. A student cannot tell which rule applies to which data.
- ch 4 [low] Section 2 (device identity) against the sequence figure: Section 2 says the manufacturer writes the certificate and private key into the device at production, but the figure shows the smart lock requesting a certificate from a CA and receiving it at run time. The two are not wrong, but nothing says why a provisioned device would ask a CA again.
- ch 5 [high] Section 1, servient paragraph: The sentence 'A device servient runs on a stronger node' is wrong and contradicts the W3C WoT model. A device servient runs on the device itself, which is usually the constrained node; it is the gateway servient that runs on a stronger node and proxies many small devices. As written, a student will learn the roles backwards.
- ch 5 [low] Section 1, resource model paragraph: 'A property is readable state. An action is an operation that changes state' is too narrow: properties are often writable as well as readable, and an action is an operation the Thing performs when invoked, which need not change state (for example, a self-test or a long-running job).
- ch 5 [low] Section 2, opening: 'Some syllabi call this layer IoT middleware' is circular: the section is already titled IoT middleware, so the sentence adds nothing and may confuse a reader into thinking two different things are being named.
- ch 5 [low] Section 2, discovery bullet: 'mDNS, DNS-SD or UPnP from Unit 3' points to earlier material as plain text, so a phone reader cannot jump there and may not find it.
- ch 6 [low] Section 3, limits paragraph: The sentence '6LoWPAN frames (Unit 3) are tiny, so a full OpenFlow header does not fit' is technically wrong as written. An OpenFlow header is only 8 bytes (version, type, length, xid) and fits easily in a 6LoWPAN frame; what does not fit is a complete OpenFlow message carrying a long match specification, together with the per-message overhead and the many round trips needed. A student would wrongly learn that the 8-byte header itself is too big.
- ch 7 [high] Beyond: LoRaWAN does not use cluster heads. In LoRaWAN, end devices send to gateways, and gateways are transparent bridges to a network server; there is no cluster-head layer. A student may carry this wrong topology into an exam answer.
- ch 7 [low] Worked example 1, answer: 'a 5× reduction' can be misread as 'reduced by 5 times' (a 500% cut). The bytes fall to one-fifth of the original, i.e. an 80% cut.
- ch 7 [low] Section 1, formula M_gw = C × (T/Δt): Δt is called 'reporting interval' without saying whose. Node reporting interval and cluster-head reporting interval can differ, and the formula only counts head-to-gateway messages, so Δt must be the CH interval.
- ch 7 [low] Worked example 1, steps: Each step label is doubled ('step 1: 1.'), which looks like a numbering slip when read on a phone.
