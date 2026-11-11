# c-web-u1: free-model run

- Book: `work/claude_figs/c-web-u1/tree/books/cse/c-web/c-web-u1.html`
- Status: ok
- Model calls so far: 30 (117,956 tokens in, 174,409 out), 5.8 minutes

## Checker

```
c-web-u1.html: 6 chapters, 12184 words, 7 figures, 140 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Exam traps, third bullet: The sentence 'A URL with no port takes the default from its scheme, so https always means 443' is false as written. A written port overrides the default, and Q5 in this same chapter uses https://api.example.org:8443, which is https on port 8443. A student may answer '443' for any https URL and lose marks, or contradict the quiz.
- ch 1 [low] Worked example 1, step 5: 'So 3 servers were asked on the chain' counts root, TLD and authoritative but leaves out the resolver, which the browser also asks. A careful reader may count 4 and think the given output of 3 is wrong.
- ch 1 [low] Section 4, closing paragraph: 'The whole path is one request-response round trip' clashes with the step just above it, where the browser makes more requests for CSS, JavaScript and images, each a separate request-response.
- ch 1 [low] Section 2, TTL paragraph: 'This is why a DNS answer is cached and can change later' reads as a cause that is not stated: caching does not cause change, it delays the change by the TTL.
- ch 1 [low] Beyond: 'Weighted and latency-based answers send users to the nearest data centre' is wrong for weighted routing. Weighted answers split traffic in set proportions (for example 90/10 during a rollout); only latency-based answers choose the nearest data centre.
- ch 1 [low] Beyond: 'DNS over HTTPS encrypts lookups so an ISP cannot read them' overstates it. The ISP can still see that a device is connecting to the DoH server and when; what it cannot read is the name being queried.
- ch 2 [low] Worked example 1, step 4 (and quiz Q4): The ceiling brackets ⌈ ⌉ are used without being defined, so a reader meeting them for the first time cannot tell what ⌈1.333...⌉ = 2 means.
- ch 2 [low] Section 2, first paragraph: "The request reaches a load balancer first" is written as if every three-tier system has one. A small app on one server has no load balancer, and the request goes straight to the app server.
- ch 2 [low] Section 2, first sentence: "A browser sends an HTTP request to a host name" hides the order of steps: the host name must be resolved to an IP address before any request can be sent to it.
- ch 3 [low] Section 1, same-origin policy sentence: The clause 'unless the server allows otherwise' is attached to both storage and responses. A server can relax cross-origin reading of responses using CORS headers, but it cannot give a page access to another origin's cookies or localStorage. As written, a student may think CORS opens storage too.
- ch 3 [low] Section 1, JavaScript engine sentence: Node.js is listed next to Chrome and Firefox as if it were a browser. Node.js is a runtime that uses V8; inside a list of browser parts it can confuse a reader about what a browser is.
- ch 3 [low] Section 2, Nginx example numbers: 'Nginx may serve 700 static requests per minute and proxy 300 requests per minute' repeats the figure's split of a 1,000 req/min load, but reads like a limit on what Nginx can do. Nginx handles far more than 700 requests per minute.
- ch 4 [high] Exam traps, second bullet: It says POST is the only common method that is neither safe nor idempotent, but the methods table and the Q7 answer both say PATCH is also neither safe nor idempotent. This internal contradiction will confuse a student who is asked to list the unsafe, non-idempotent methods.
- ch 4 [low] Section 2 and Quiz Q1: The chapter treats GET, HEAD and OPTIONS as the complete set of safe methods. Standard definitions (RFC 9110) also define TRACE as safe, so a student who writes TRACE in an exam would also be right.
- ch 4 [low] Section 2, paragraph on GET: "an Angular HTTP client call (Unit 5) all send GET" is wrong: Angular's HttpClient sends whichever method you call, and http.post sends POST.
- ch 4 [low] Section 1, second paragraph: "The message is plain text" is only true for HTTP/1.1. Section 4 later says HTTP/2 is binary on the wire, so the two statements appear to contradict each other.
- ch 4 [low] Worked example 1: The output block prints three loose numbers (84, 0, 3), but part (c) only asks for the two body lengths; the count "3" comes from step 5, which answers a question that was never asked. The output also does not match the parts (a) and (b).
- ch 4 [low] Worked example 2: It repeats Worked example 1 almost word for word (same URL, same 200/201/204, same 84 bytes), so it adds no new practice.
- ch 4 [low] Beyond section: "gRPC and GraphQL both sit on HTTP/2 framing" is inaccurate: gRPC requires HTTP/2, but GraphQL is transport-agnostic and is most often sent as an ordinary HTTP POST, frequently over HTTP/1.1.
- ch 4 [low] Section 4 and Beyond section: The sentences "Only a few universities teach HTTP/3 here" and "Only a few universities teach these here" are syllabus-coverage markers repeated inside technical paragraphs. They break the flow and read as filler.
- ch 5 [high] Worked example 1, step 4 and answer: The question (b) asks for the spare capacity expressed as a multiple of peak traffic. Step 3 correctly finds the spare capacity as 40 − 8 = 32 requests/s, but step 4 then divides total capacity by peak (40 ÷ 8 = 5) instead of spare capacity by peak (32 ÷ 8 = 4). The answer sentence attaches '5 times peak' to the 32 requests/s figure, which is wrong: 32 requests/s is 4 times peak.
- ch 5 [high] Worked example 2, step 3 and answer: Same error as Worked example 1. Spare capacity is 50 − 10 = 40 requests/s, so as a multiple of peak it is 40 ÷ 10 = 4. Step 3 gives 50 ÷ 10 = 5, which is total capacity as a multiple of peak, not spare capacity.
- ch 5 [high] Quiz Q4, answer: The answer repeats the same mistake. Spare capacity is 40 requests/s; as a multiple of peak (10 requests/s) that is 4 times, not 5 times.
- ch 5 [low] Section 1 (DevOps) and Beyond: Section 1 calls DevOps 'a fourth group' (three tiers plus DevOps), while Beyond calls DevOps 'the fifth layer of the stack'. A student may wonder which count is right.
- ch 6 [high] Section 2 (Git), paragraph on remotes: The command is written as `git remote add origin` with no URL argument (there is just a blank space before 'names that copy origin'). As shown, the command is incomplete and fails when a student types it; the remote cannot be created without an address.
- ch 6 [low] Section 3 (Network) and worked example step 4: The text says a 304 response has transferred size 0 bytes, and that the 404 'adds 0 KB' because it 'fails before any content arrives'. Strictly, both exchanges still carry response headers over the network, and a 404 often carries a small error body. The zero is an idealisation, not a literal measurement, and a sharp student who looks at the Size column will see a few hundred bytes for a 304 row.
- ch 6 [low] Section 1 (VS Code), debugging paragraph: 'The Variables panel and the debug console then show the live value of every symbol' overstates the panel. The Variables panel lists the variables in the current scope (plus globals and closure variables it can reach), not every symbol in the program.
