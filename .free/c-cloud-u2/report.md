# c-cloud-u2: free-model run

- Book: `books/cse/c-cloud/c-cloud-u2.html`
- Status: ok
- Model calls so far: 20 (69,271 tokens in, 152,513 out), 3.8 minutes

## Checker

```
c-cloud-u2.html: 7 chapters, 12579 words, 8 figures, 141 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Lead and Figure: The chain lists 'transit or peering, then an internet exchange' and the figure draws transit → IXP in series. Peering happens at the IXP, and transit and peering are alternative ways for the local ISP's traffic to reach the cloud provider, not two compulsory hops.
- ch 1 [low] Section 1, latency definition: Latency is defined as 'the time for a signal to cross the path', which is only propagation delay. In networking, delay is propagation + serialisation (transmission) + queuing + processing; the worked example itself adds switching and access delays, and Section 3 says serialisation appears in the user's wait.
- ch 1 [low] Section 3, opening line: 'Distance sets latency, not bandwidth alone' is ambiguous. It can be read as 'bandwidth also sets latency somewhat' or as 'distance, not bandwidth, sets latency', and neither reading matches the rest of the section.
- ch 1 [low] Worked example 1 and Quiz Q3: The extra delays (access 5 ms, ISP hops 2 ms, switching 0.5 ms) are silently treated as one-way. A student cannot tell whether access 'adds 5 ms' once or once per direction, so the doubling step looks arbitrary.
- ch 2 [low] Section 3, paragraph 2: The sentence 'With no index and no tenant filter, the engine scans every row' pairs the filter with the index. A student can read it as 'if I add the tenant filter, the scan is avoided'. That is false: without a usable index, the engine still scans every row even when WHERE tenant_id = 42 is present. The filter decides correctness, the index decides cost.
- ch 2 [low] Section 3, paragraph 1 and Figure: The path is drawn as Web server -> App -> Tenant DB, and the step says the application sends the query 'to the tenant database'. In the shared-schema model described in Section 2 there is one shared database, and Section 1 says a load balancer sits in front of the web server, but neither the wording nor the sequence shows this. A student may conclude every tenant has its own database, or that the browser reaches the web server directly.
- ch 2 [low] Section 3, paragraph 1: 'The web server passes sid to the application' suggests the web server parses the cookie and forwards a bare id. In practice the web server forwards the whole request, including the Cookie header, and the application reads sid from it.
- ch 2 [low] Quiz Q2, answer: The answer says 'State lives in the cookie and the store', but Section 1 says the cookie is only a key. A student may think the user identity or tenant is stored inside the cookie rather than in the server-side session store.
- ch 2 [low] Section 1, response example: The sample JSON body [{"id":7,"amount":499}] gives a bare number for money. Elsewhere in the book numbers carry units; here the reader cannot tell whether 499 is rupees, paise or dollars.
- ch 3 [low] Section 1 and the figure (messaging layer): Section 1 says the ESB "sits between providers and consumers", but the figure places the Messaging layer (ESB, queue) below the Services layer, next to Data. A student reading both will be unsure whether the bus fronts the services or backs them.
- ch 3 [low] Section 2 and quiz Q5 (PUT): PUT is described only as "replaces", and Q5 asks only which verb replaces a resource. Standard HTTP also lets PUT create a resource at a URI chosen by the client if none exists there, so the replace-only wording can mislead.
- ch 3 [low] Section 2 and Section 3 (cross-references): The text points to other material as plain words: "See Chapter 2.2 for the HTTP basics" and "see Unit 3, Virtualization and Containers". On a phone these are not tappable and the chapter id is not given.
- ch 4 [high] Section 3, paragraph on choosing a metric: "pair it with latency so you do not scale out when servers are slow" gives the opposite of the usual rule. Slow servers under load are exactly when scale out is needed; latency is paired with RPS to avoid scaling out when the bottleneck is elsewhere (a slow database, a slow downstream API) and to avoid scaling in when RPS falls only because servers cannot accept work.
- ch 4 [low] Section 1, formula note: "ceil rounds up to the next whole server" is not exact; when L ÷ C is already a whole number (for example 900 ÷ 75 = 12) ceil leaves it unchanged rather than going to the next one.
- ch 4 [low] Section 3, paragraph on metrics and failure modes: "use per-instance metrics or a health check" mixes two different tools. A health check only tells you whether a server answers; it cannot show that one instance is hot while the average looks fine.
- ch 4 [low] Worked example 1: The saving is only valid if the off-peak load fits inside the 2-server minimum (2 × 60 = 120 requests per second). The example never states this, so a student may think the elastic group always keeps exactly 2 servers outside the peak.
- ch 4 [low] Section 3, sentence on warm pools: "A warm pool reduces boot delay but costs for stopped capacity" is loose. A fully stopped server is not billed for compute time in most clouds; the cost is for the storage and reserved resources that are kept ready.
- ch 4 [low] Lead: "stop paying when it is gone" is unclear; a beginner may read "gone" as the data being deleted rather than the resource being released.
- ch 5 [low] Section 2, quorum paragraph: The sentence 'Quorum replication needs agreement from a majority' is not the general rule and contradicts the condition given in the next sentence. The rule is R + W > N; a value like N=4, W=2, R=3 satisfies it although the write quorum is not a majority. A student may think each operation alone needs more than N/2 acknowledgements.
- ch 5 [low] Section 3, availability formulas: The series and parallel formulas are stated without the independence assumption. They only hold when parts fail independently; parts sharing a rack, a power feed or a network link fail together and the formulas then give an optimistic answer.
- ch 5 [low] Section 1, algorithms: 'Least response time uses the fastest recent response' is too vague to act on and does not match the usual definition.
- ch 5 [low] Section 1, IP hash: The chapter says the pool can grow or shrink, but IP hash uses mod N, so changing N remaps almost every client and breaks their sticky mapping. The point is not mentioned and a student may think IP hash is stable under scaling.
- ch 5 [low] Section 3, last line: The forward reference to the SLA chapter is plain text, so it is not clickable like the other chapter links in the book.
- ch 6 [low] Section 1, paragraph 4: 'A good SLA is measurable by both sides' is ambiguous; it can be read as 'both sides can measure something different' rather than both parties measuring the same metric the same way.
- ch 6 [low] Section 1, paragraph 3: The SLA is described only as what the provider promises. Standard SLAs also set duties on the customer (paying on time, not misusing the service, reporting incidents) and that gap can mislead a student who thinks an SLA is one-sided.
- ch 6 [low] Section 2, paragraph 1: The nines list stops at 99.9%, but the chapter uses 99.95% everywhere (SLO and worked example) without ever saying it is 'three and a half nines'.
- ch 6 [low] Exam traps, first trap: 'An SLO must be stricter than the SLA' is stated as an absolute law. It is the usual discipline when a customer-facing SLA exists, but internal services often have an SLO and no SLA, and some contracts set the two equal.
- ch 6 [low] Worked example 1, part (b) and step 4: The example says flatly that no credits are due. Section 3 correctly says credits depend on the contract terms and on the customer filing a claim in time, so the example should state the assumption it is making.
- ch 7 [low] Figure (Metered resources to invoice): The figure shows an object store as a third metered resource feeding the monitor, but the invoice note ₹482.19 is exactly the total from Worked example 1, which prices only vCPU, RAM and the block volume. A student will look for the missing object-storage charge and find nothing.
- ch 7 [low] Worked example 1, step 4: Disk is billed only for the 10 hours of the run, yet Exam trap 1 says a stopped VM keeps billing its disk. Nothing in the example says the volume is deleted at the 10-hour mark, so the two statements read as contradictory.
- ch 7 [low] Quiz Q6: The answer's fix is 'tag every resource, then re-aggregate by tag', but the question says the provider exposes only host-level meters. Host-level totals carry no per-resource records, so tags have nothing to attach to and tagging alone cannot split them.
- ch 7 [low] Section 1 and Section 2 (forward references): 'Unit 3 covers how' and 'Unit 4 covers how these stores are built' are plain text, so a reader on a phone cannot jump to them; the book's convention is to link other chapters.
