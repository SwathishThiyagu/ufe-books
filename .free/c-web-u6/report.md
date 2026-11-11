# c-web-u6: free-model run

- Book: `work/claude_figs/c-web-u6/tree/books/cse/c-web/c-web-u6.html`
- Status: ok
- Model calls so far: 45 (184,615 tokens in, 264,771 out), 7.2 minutes

## Checker

```
c-web-u6.html: 9 chapters, 15915 words, 10 figures, 188 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: tree is too wide (5 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, description of the call stack: The sentence 'a new function is pushed only when the one above it returns' is backwards. A function is pushed onto the stack when it is called, while its caller is still on the stack; the caller is popped only after the callee returns. As written, a student would think functions run one after another with no nesting.
- ch 1 [high] Quiz Q5, answer: The first half is right (40 × 50 ms = 2 s of blocking), but the closing claim is wrong: forty fs.readFile calls do not finish in 'close to 50 ms'. With the default pool of 4 threads they run in about 10 batches of 4, so roughly 10 × 50 ms = 500 ms.
- ch 1 [low] Section 2 and Quiz Q3, microtask queues: The chapter says Node 'empties both' queues but never says that the process.nextTick queue is drained before the promise microtask queue. A student comparing process.nextTick(f) with Promise.resolve().then(f) has no rule to apply.
- ch 1 [low] Section 1, Section 3 figure note, and Exam traps: 'DNS lookups run on the libuv thread pool' is only true for dns.lookup. dns.resolve() uses the operating system's async resolver and does not use the pool.
- ch 2 [low] Section 2 and Exam traps: The rule as written says the caret always locks the major number. That is true only for major version 1 and above. For a 0.x package npm's caret locks the minor number, so ^0.2.3 allows 0.2.3 up to but not including 0.3.0, and ^0.0.3 allows only 0.0.3. Many published packages are still on 0.x, so a student applying the stated rule to ^0.2.3 would wrongly accept 0.3.0.
- ch 3 [low] Section 2 and Quiz Q2: The chapter states flatly that highWaterMark 'is the chunk size in bytes' and that its default is 64 KB = 65536 bytes. That default is correct only for fs.createReadStream and fs.createWriteStream. A plain Readable, Writable, Transform or TCP socket defaults to 16 KB (16384 bytes) for byte streams. Quiz Q2 asks 'what is its default?' without naming the fs context, so a student can carry away a wrong general number. Also, highWaterMark is strictly a buffer threshold: for fs streams each chunk is at most that many bytes, not always exactly that many.
- ch 4 [low] Figure, route handler node: The note says 'req.params.id = 42', which shows the parameter as a number. The chapter itself states twice (Section 2 and worked example step 2) that route parameters are always strings. A student reading only the figure would learn the wrong type.
- ch 4 [low] Section 2, first paragraph: The list of methods reads as if get, post, put, patch and delete are the complete set. Express also exposes app.head, app.options, app.all and app.use, so a student may think only those five exist.
- ch 5 [high] Worked example 1, step 6: Step 6 answers 'Safe and idempotent: GET, PUT and DELETE', which lumps the two properties together and contradicts Section 2, where PUT and DELETE are explicitly called not safe because they change state. A student copying this into an exam would wrongly claim PUT and DELETE are safe.
- ch 5 [low] Section 2 (safe, idempotent): PATCH is listed in the method table in Section 1 but is never classified here, so a student cannot tell whether PATCH is safe or idempotent. In general PATCH is not guaranteed idempotent, and it is not safe.
- ch 5 [low] Section 2, first line: 'A method is safe if it does not change server state' is loose. Servers do change state on every call (logs, counters, audit rows); safety is about whether the client asks for a change of the resource.
- ch 6 [low] Section 2, placeholders paragraph: The mechanism described is only true for prepared statements. With pool.query(), mysql2 escapes the values in JavaScript and sends one finished SQL string to MySQL; the server does not receive statement and values separately. Only pool.execute() sends a real prepared statement whose text is parsed before the values are bound.
- ch 6 [low] Section 2, SQL injection paragraph: The payload 1; DROP TABLE students does not drop the table under mysql2's default settings, because multipleStatements is false, the second statement is rejected with a syntax error. A student who tries it will think the example is wrong.
- ch 6 [low] Worked example 1, answer line: Typo: 'affactedRows check' should be 'affectedRows check'. Students copy these lines into notes and answers.
- ch 7 [high] Section 3, last paragraph (and Quiz Q7, which contradicts it): The chapter presents strict multi-statement transactions as a reason to leave MongoDB for MySQL, which reads as if MongoDB cannot do them. MongoDB has supported multi-document ACID transactions on replica sets since version 4.0, and Quiz Q7's own answer says "MongoDB would need a multi-document transaction". A student could write "MongoDB has no transactions" in the exam and be wrong.
- ch 7 [low] Section 2, first paragraph: "Every call returns a promise" is not true: client.db('shop') and .collection('books') are synchronous and are not awaited anywhere in the code shown.
- ch 7 [low] Section 2, after the code block: "updateOne and deleteOne return matchedCount, modifiedCount and deletedCount" lumps two different result objects together; deleteOne never returns matchedCount or modifiedCount.
- ch 7 [low] Exam traps, item 3: The claim that .map does not exist on a cursor is wrong for the Node.js driver: cursor.map(transform) is a real method. Only .length is missing.
- ch 7 [low] Quiz Q5, answer: The replacement document is printed as {_id: , marks: 75}, with nothing after _id. A student copying this writes an invalid document.
- ch 7 [low] Worked example 1, step 1 and code block: Step 1 tells the reader to connect and take the handle coll = client.db('shop').collection('students'), but the code shown is Python over a list and never connects or uses a driver handle. The two do not match.
- ch 8 [low] Section 1, bcrypt paragraph: The cost factor is called '10 to 12 rounds'. In bcrypt the cost is a logarithmic work factor: cost 10 means 2^10 ≈ 1024 key-setup iterations, and each extra unit doubles the time. A student can read this as 'only 10 to 12 passes over the password'.
- ch 8 [low] Section 2, signature paragraph: The verification step is incomplete. The server must also check that the header's alg value is the expected one and reject alg 'none'; verifying only the signature and exp leaves the classic 'alg: none' forgery open. The text also implies the key is always one secret; with RS256/ES256 the server signs with a private key and others verify with the public key.
- ch 8 [low] Section 1, cookie flags paragraph: 'SameSite=Lax or Strict stops another site from making the browser send the cookie on a cross-site request' overstates Lax. Lax still sends the cookie on top-level cross-site GET navigations; it blocks cross-site POST, fetch and form submissions.
- ch 8 [low] Section 2, last paragraph (JWT storage): 'Keep it in memory or in an HttpOnly cookie' is given without the catch: an HttpOnly cookie is sent automatically by the browser, so CSRF protection (SameSite, CSRF token) becomes necessary, and the Authorization: Bearer pattern no longer applies.
- ch 9 [high] Section 3, build step bullet: The build command ends with two dots: docker build -t registry.example.com/shop:${SHA} .. — the second dot makes the build context the parent directory, so the Dockerfile in the project folder is not used as intended. The command as written is wrong.
- ch 9 [high] Quiz Q3 answer: The answer command has no image name: docker run -p 8080:3000 . — read literally, the image would be ".", which is not an image. The port mapping is right but the command is incomplete/wrong.
- ch 9 [low] Section 2, Docker Compose paragraph: "app ... waits for db" overstates what Compose does. depends_on only starts services in order; it does not wait until the database is ready to accept connections unless a health-check condition is set.
- ch 9 [low] Section 3, registry sentence: "A registry is a private image store" is too narrow — registries such as Docker Hub are public by default; the key contrast with Git is what they store, not their visibility.
