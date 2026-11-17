# c-graphics-u6: free-model run

- Book: `work/claude_figs/c-graphics-u6/tree/books/cse/c-graphics/c-graphics-u6.html`
- Status: ok
- Model calls so far: 38 (152,458 tokens in, 228,814 out), 7.1 minutes

## Checker

```
c-graphics-u6.html: 9 chapters, 15714 words, 10 figures, 210 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, bullet on the buffer and synchronisation stage: "It absorbs jitter and inserts or drops timing" is unclear and technically loose. A buffer cannot insert or drop timing. It inserts extra delay and drops (or repeats) frames, samples or packets.
- ch 1 [low] Lead versus Exam traps, third bullet: The lead says the stages are "joined by a common clock", while the trap says audio and video "have independent clocks". Read together, a student may think the two statements contradict.
- ch 1 [low] Figure and Section 2 list (ordering of buffer, storage and network): The pipeline draws buffer and sync before storage and network, but the text says the buffer absorbs jitter from storage and the network. On playback (set-top box, phone call) the playout buffer sits after the network and storage, just before presentation. A student drawing the receive path from this figure will put the buffer in the wrong place.
- ch 1 [low] Quiz Q7: The percentage is truncated, not rounded. 1,411,200 ÷ 222,595,200 × 100 = 0.633976%, which rounds to 0.6340%, not 0.6339%.
- ch 2 [high] Section 4, link capacity paragraph: The powers of ten have lost their superscripts: "100 × 106 bit/s" and "2 × 106 bit/s" read as 100 × 106 = 10 600 bit/s, which is not 100 Mbit/s and 2 Mbit/s. A student copying this gets a number that is wrong by a factor of a million.
- ch 2 [low] Section 1, client–server vs peer-to-peer: "Peer-to-peer lets clients exchange chunks directly, so load rises with users" is misleading: the "so" claims that peer-to-peer causes load to rise, but load rises with users in every model. The real point is that in peer-to-peer the total upload capacity also grows with the number of users, while in client–server it stays fixed.
- ch 2 [low] Quiz Q7: The question is worded as "Why can an edge node reduce start-up delay more than it raises average throughput?", which tells the student that an edge node does raise average throughput. The answer says the opposite, that throughput may not improve. The question and its answer do not match.
- ch 3 [low] Section 2, final sentence: The sentence 'Histograms are non-negative, so cosine is common in text and audio retrieval' gives a wrong reason. Non-negativity is not why cosine is used; cosine is used because it ignores vector length, which matters when histograms or term counts have different totals. It also jumps from image histograms to text and audio without saying so.
- ch 3 [low] Section 3, paragraph on precision and recall: 'A system that returns one safe item has high precision and low recall' — 'safe item' is undefined and precision is high only if that one item is actually relevant.
- ch 3 [low] Exam traps, first bullet: 'recall looks at what was missed' is ambiguous; a student can read it as 'recall counts the missed items', but recall counts the relevant items that were found.
- ch 3 [low] Quiz Q7, answer: 'pixels-derived features' is awkward and unclear wording.
- ch 4 [high] Section 1 (dynamic links), Exam traps item 3, Quiz Q2: The chapter says a dynamic link "does not appear in the page source" and that it is "not in the page source". That is wrong as stated: when a search engine or recommendation engine builds the page, the generated href does appear in the HTML that reaches the browser, so a student can open View Source and see it. What is true is that the link is not stored in the document file on the server; it is built per request. As written, a student will answer "dynamic links never appear in HTML", which an examiner will mark wrong.
- ch 4 [low] Section 2, Dexter model paragraph: "Some syllabi call the structural description the Dexter model" is loose and misleading. The Dexter model is a reference model for hypertext systems, and it has three layers, not two: storage, within-component and run-time. Leaving out the within-component layer hides where anchors live.
- ch 4 [low] Worked example 1, step 4: "The other path is Home → Courses → Unit6 → Notes" is incomplete: the given links also allow Home → Contact → FAQ → Notes, which is 3 links too. Calling one of two longer paths "the other path" can confuse a student checking the graph.
- ch 4 [low] Exam traps, last item (dangling link vs missing anchor): A link whose target anchor no longer exists inside a live node is itself a kind of dangling link, so the pair is not two separate faults. As worded, a student may think a missing anchor does not make the link dangling.
- ch 5 [high] Section 3, leaky bucket formula: The formula is written 'bytes sent over T ≤ r × T + b', but r is in bits per second and b is in bits, so the left side must be in bits, not bytes. The worked example right below it correctly works in bits, so the formula line contradicts it and also contradicts the unit-mixing exam trap.
- ch 5 [high] Worked example 1, step 6; Quiz Q3: Step 6 goes from 'spread S = 5 ms, so the playout offset must be D ≥ 5 ms'. That only works here because the smallest delay is 0, so spread and d_max happen to be equal. The correct rule (stated earlier in the text) is D ≥ d_max, the largest delay. Quiz Q3 shows the break: delays are 2, 5 and 4 ms, spread 3 ms, yet a playout offset of 3 ms would play packets 2 and 3 (arrivals 15 and 24 ms) at 13 and 23 ms, i.e. late. A student who follows step 6 sets D = 3 ms and loses packets.
- ch 5 [low] Figure caption and aria text: The caption and aria say 'two delayed packets', but three packets arrive after their send slot: delays are 0, 2, 5, 0 and 5 ms. Only two of them (P3 and P5) use up the whole 5 ms offset; P2 is 2 ms late.
- ch 5 [low] Section 2, delay measurement step: The list says to record s_i and a_i 'on one clock at the receiver'. A send time is stamped by the sender, so this quietly assumes synchronised clocks; a constant clock offset shifts every d_i equally, which leaves jitter and spread unchanged but makes the absolute mean delay wrong.
- ch 5 [low] Section 2, jitter definition: J = (1/n) Σ |d_i − d̄| is called 'the usual jitter figure'. In the standard RTP practice, jitter is a smoothed mean deviation of the successive transit-time differences, not of delays from the window mean. Students who later read the RTP specification will meet a different formula under the same name.
- ch 6 [high] Lead: The lead says the same segmentation/buffer/ABR machinery runs cloud video calls. Real-time calls (WebRTC and similar) use RTP over UDP, not segmented HTTP objects with a manifest and a bit-rate ladder, and the chapter itself says later that RTP is used where low delay matters. A student will carry away a wrong model of how calls work.
- ch 6 [low] Figure: The dashed 'rate request' edge runs from the client buffer back to the encoder ladder. The client does not ask the encoder to change rate; every rung is encoded in advance, and the client asks the server or CDN for a segment from a different rung.
- ch 6 [low] Quiz Q7: The last sentence, 'Pausing or reducing start-up reserve cannot create data, so the player may need to rebuffer', is garbled and mixes two ideas (pausing does not add data; lowering the reserve does not add data either).
- ch 7 [low] Section 1: The chapter says deadlines are 'often equal to T_i' and then states the RM bound U ≤ n(2^(1/n) − 1) as a general RM test. That bound is proved only for RM priority assignment with D_i = T_i, preemption and no blocking. A student may apply it to tasks with D_i < T_i, where it does not hold.
- ch 7 [low] Section 2, priority inversion fix: Only priority inheritance is given as the fix. The other standard fix, priority ceiling, is missing, and the inheritance rule is stated only as 'the waiter's priority' rather than the highest waiting priority.
- ch 7 [low] Quiz Q2: The answer says RM's test 'is sufficient but not exact' but does not say what to do when U is above the bound, which is exactly the case met in the worked example.
- ch 8 [low] Worked example 2 (and Exam traps, last bullet): The example calls the change 'motion-gated recording' and says the site 'records only 20% of each day'. This reads as if the motion gate itself reduced storage, which is exactly what the last exam trap and quiz Q4 deny. A student can come away with two opposite rules.
- ch 9 [low] Lead: "leaked paper images" is ambiguous; a student cannot tell whether it means exam papers, newspapers or printed photos.
- ch 9 [low] Section 1: The heading says "three kinds of mark", but the third item, steganography, hides the existence of a message rather than embedding a mark; the list mixing a mark, a technique and a per-copy mark confuses the vocabulary.
- ch 9 [low] Section 1 and Section 2: "Watermark: ownership proof or tamper check" is stated but never explained; the chapter never says why some watermarks reveal editing and others survive editing.
- ch 9 [low] Quiz Q4: The model answer says a mid-frequency DCT mark "is changed in the same transform domain", which does not by itself explain survival and can be copied by a student as a non-answer.
- ch 9 [low] Section 3: The closing sentence claims "the same evidence pipeline appears in 6.8", but the clause that follows describes camera output volume, not the read-metadata / detect-copy-move / hash-and-custody pipeline; the cross-reference asserts content of another chapter that may not match.
