# c-os-u6: free-model run

- Book: `books/cse/c-os/c-os-u6.html`
- Status: ok
- Model calls so far: 37 (111,166 tokens in, 102,605 out), 4.3 minutes

## Checker

```
c-os-u6.html: 9 chapters, 10570 words, 10 figures, 134 KB
OK
```

## For the reviewer

- chapter 5: a c program's shown output was replaced by its real output; check the text around it
- chapter 4: a python program's shown output was replaced by its real output; check the text around it
- chapter 9: a python program's shown output was replaced by its real output; check the text around it
- chapter 9: give 6 to 8 quiz questions

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1 – dry run table: Process name is inconsistent: earlier called "Payment Service" but table uses "Payment".
- ch 1 [low] Section 2 – principle "Fail‑safe defaults": Definition equates fail‑safe defaults with default‑deny, which is a narrower concept.
- ch 1 [low] Figure description: Phrase "note the order Confidentiality → Integrity → Availability" suggests a hierarchy that does not exist.
- ch 2 [high] Worked example 1: The C code shown does not implement any protection‑domain check; it always prints 1 regardless of the rights. This misleads the reader that the code verifies the request.
- ch 2 [high] Section 2 (Reference monitor operation): The three classic properties of a reference monitor are *complete*, *tamper‑proof* (isolated), and *verifiable*. The text lists *always invoked* instead of *verifiable*, which is a factual deviation from standard textbooks.
- ch 2 [low] Worked example 1 – dry run table: The table header order is ['subject', 'object', 'right'] while the text describes rights as subject → operation → object. This may confuse readers.
- ch 2 [low] Quiz Q3: The answer assumes delete is never allowed with write permission, but many OS treat delete as a write on the containing directory. The statement can be misleading.
- ch 2 [low] Quiz Q6: The answer omits the step of assigning default rights or placing the new process in an existing domain.
- ch 3 [low] Section 2, bullet point on efficiency: The statement says ACLs are "Efficient for objects that have many subjects", which is opposite to the usual property; ACLs are efficient when an object has few subjects because the list is short.
- ch 3 [low] Section 3, bullet point on capability presentation: It says "The subject presents its capability list to the kernel", implying the whole list is sent each time, which is not how capabilities work.
- ch 3 [high] Quiz Q5: The answer claims the process can read and write because the capability list is authoritative, ignoring the ACL. In systems that use both ACLs and capabilities, the effective rights are the intersection of the two; the ACL can restrict rights granted by a capability.
- ch 4 [high] Section 1 (Discretionary and mandatory access control): The formula allow(s, o, op) = (label(s) ≥ label(o)) ∧ (op ∈ ACL(o, s)) mixes MAC (label comparison) with DAC (ACL lookup). In a pure MAC system the decision is based only on security labels; ACLs are not consulted.
- ch 4 [high] Section 1 (Discretionary and mandatory access control): The step‑by‑step description says that after comparing labels the kernel checks the ACL for the requested operation. This is incorrect for mandatory access control, which does not use ACLs.
- ch 4 [high] Section 3 (Revocation techniques for capabilities): The text claims that capabilities use reference counting and are freed when the count reaches zero. Standard capability systems do not employ reference counting; revocation is usually done via a revocation list, version numbers, or a single revoked flag.
- ch 4 [low] Section 2 (Role‑based access control and ACLs): The sentence "When a role is revoked, the system removes all ACL entries that belong to that role" may mislead students because RBAC typically removes the role assignment, and ACL entries are derived rather than stored directly.
- ch 4 [low] Quiz Q7 (compare overhead of ACL‑based revocation with capability invalidation): The answer mentions that capability invalidation is constant‑time, but does not note the need to propagate the revocation flag to all processes, which can add overhead in distributed settings.
- ch 5 [high] Quiz Q4: The answer says the Java bytecode verifier stops an illegal cast before execution. In reality the verifier ensures type safety at load time, but an illegal cast is detected at runtime and results in a ClassCastException.
- ch 5 [high] Section 3: The statement "Erlang processes communicate only by passing messages (capabilities)" incorrectly equates Erlang messages with capabilities.
- ch 5 [low] Section 2: The C code example about subtracting a payment from a balance does not illustrate capability revocation and is unrelated to the surrounding text.
- ch 5 [low] Section 2: Listing "reference count" as a revocation mechanism is misleading; reference counting tracks holders but does not itself revoke capabilities.
- ch 7 [high] Worked example 1, code snippet: The code computes `grant = (ts1 > ts2 ? ts1 : ts2) + 1;` which selects the larger timestamp (7) and adds 1, contradicting the described rule that the lock must be granted to the node with the smallest timestamp (Node1 with ts = 5). The printed message also mixes the decision (grant to Node1) with the logical‑time calculation, making the algorithm unclear.
- ch 7 [high] Message exchange spec (Figure) in Section 3: The spec JSON shows a message from RM to Node2 labeled "Grant lock", while the text explains that the reference monitor grants the lock to Node1 (the node with the smallest timestamp). This inconsistency can mislead students.
- ch 8 [high] Worked example 1: The example computes stale‑read probability as D ÷ T = 0.02, but the client reads 150 ms after the write while the replication delay is 200 ms. Because the read occurs before replication finishes, the read is certainly stale. The probability should be 1 (100 %), not 0.02. The D ÷ T formula only applies when the read time is uniformly random within the timeout window, which is not the case here.
- ch 8 [high] Quiz Q4: The answer uses P(stale)=150/10000=0.015, ignoring that the client reads 80 ms after the write, which is before the 150 ms replication delay. Hence the read is certainly stale, not 1.5 %.
- ch 8 [low] Section 2 (Consistency models): The sentence "It requires the client to contact a majority of replicas or to wait for all replicas to acknowledge a write" may mislead students; strong consistency does not require contacting all replicas, only a quorum that guarantees overlap.
- ch 8 [low] Section 3 (Replication, caching and failure handling): The terms N, W, and R are used in the quorum description before being defined.
- ch 9 [high] Section 1: The mode is described as a three‑octal digit value. In reality, file mode is usually shown as a four‑digit octal number, where the leading digit holds the setuid, setgid, and sticky bits.
- ch 9 [low] Section 2: Integrity levels are said to "limit write access" only, which is incomplete.
- ch 9 [low] Quiz Q1: The answer "4 (octal)" may be misinterpreted because the full mode for owner read‑only is 0400.
