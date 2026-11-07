# c-cloud-u4: free-model run

- Book: `books/cse/c-cloud/c-cloud-u4.html`
- Status: ok
- Model calls so far: 39 (152,631 tokens in, 278,070 out), 7.2 minutes

## Checker

```
c-cloud-u4.html: 9 chapters, 16557 words, 10 figures, 178 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, the paragraph starting 'The data type also matters': The sentence 'Block and file storage suit structured records with a schema' can mislead. A raw block volume has no schema inside it; the schema belongs to the database that runs on the volume. A student may think block storage itself understands records and fields.
- ch 1 [low] Section 1, first paragraph: 'call chunks blocks or extents' — 'extent' is a file-system term for a contiguous range of blocks on a disk, not a word object stores use for a chunk. A student may mix up file-system extents with object chunks.
- ch 1 [low] Section 3, the sentence on latency: 'Latency comes from distance and round trips: metadata lookup, chunk fetch, cache miss. A local cache cuts the last two.' A cache miss is not a round trip, and a local cache does not remove the chunk fetch, it serves it from closer. The sentence is vague about what the cache removes.
- ch 1 [low] Quiz Q7 answer: The question is about users in Chennai reading from a bucket in another region, but the answer explains locality as running compute near the bucket. That cuts compute-to-storage latency, not the Chennai user's latency, so the answer does not fully match the scenario.
- ch 2 [high] Figure (and Section 1): The figure shows the acknowledgement going straight from DataNode 3 to the Client ('ack b0'). This contradicts the text in Section 1, which says the primary sends the final ack, and contradicts both GFS and HDFS, where the ack travels back along the pipeline and the first DataNode (the primary) hands it to the client.
- ch 2 [low] Figure: The figure shows the NameNode replying '8 blocks, 3 replicas each' to a single create request, as if all block locations are handed out at file creation. In HDFS (and GFS) locations are allocated one block at a time as the client is ready to write each block. The figure also never states the 128 MB block size that makes 1024 MB equal 8 blocks.
- ch 2 [low] Section 1: 'For each chunk it grants a lease to one replica' read at file-creation time suggests leases for every chunk are issued up front. The master grants a chunk lease when the client is ready to write that chunk, and only to one replica.
- ch 2 [low] Worked example 1: The question asks for metadata entries and then says 'repeat for GFS', but the final answer line gives only 16 chunks and 48 replicas for GFS. The GFS metadata count (16 chunk entries + 1 file entry = 17) is left out, so a student copying the answer misses a mark.
- ch 3 [high] Section 2, write path, compaction step: The step says compaction 'drops overwritten versions' unconditionally. BigTable keeps multiple versions per cell, and old versions are removed only by per-family garbage-collection rules. As written it contradicts Section 1 and teaches that a newer write makes older versions unreadable.
- ch 3 [high] Section 4, crawler paragraph: It says that with key www.cnn.com 'pages of one site would scatter'. Pages on the same host www.cnn.com all share the prefix www.cnn.com, so they stay together. Reversing the host groups different cnn.com subdomains under com.cnn.
- ch 3 [low] Section 4, crawler paragraph and worked example: 'One tablet scan reads the whole site' is imprecise. A large site can span multiple tablets; a range scan may read several adjacent tablets, not a single tablet.
- ch 3 [low] Figure spec: The row org.wiki has cell 'b1' even though the spec says cells hold a version timestamp; b1 is not a timestamp label. This looks like a typo and confuses the figure.
- ch 3 [low] Lead: Saying 'Cloud databases generalise the trade: drop joins and fixed schemas' overgeneralises. Cloud relational databases keep joins and schemas; the statement is true only for the NoSQL cloud databases discussed here.
- ch 4 [high] Section 3 (Which host: allocation as bin packing): The best-fit sentence says best-fit 'keeps large holes for later big VMs'. This is backwards and contradicts the chapter's own Q5 answer. Best-fit takes the host with the least free space left after placing, so it leaves small leftover gaps, not large holes. First-fit is the one that leaves large free regions, because it fills hosts in list order to a similar level.
- ch 4 [high] Worked example 1, step 9 and answer: The 5.6 vCPU is called 'stranded because 4 VMs on the second host cannot reach 6', but the second host can hold 6 VMs. Usable vCPU on H2 is 12.8 and only 8 is used, so 4.8 vCPU is free and can take two more VMs; it is unused only because there are no more VMs to place. Stranded capacity means free capacity too small for one more VM, and that is only the 0.8 vCPU fraction on H1.
- ch 4 [low] Section 2, utilisation formula and its note: The lead defines utilisation as 'the share of installed capacity doing useful work', but the formula note allows allocated capacity to mean either what tenants were promised or what is busy. These are different numbers (allocation ratio versus real load), and the worked example silently uses the promised value.
- ch 5 [high] Section 1, paragraph 3: It says "Four times describe a job" and then defines only three: arrival, start and finish. A student counts three and is confused about the missing fourth.
- ch 5 [high] Section 2, fair share bullet: The definition "Fair share equalises each tenant's share of the resource it uses most" is the dominant-resource idea, not fair share. Fair share divides one pool (for example memory, or slots) equally among users or queues; it has no notion of a per-tenant dominant resource.
- ch 5 [low] Section 2, round robin bullet: "it suits interactive work" is attached to weighted round robin, but fast response for interactive work is the property of round robin in general (a short quantum). Proportional sharing is the separate point of the weighted form.
- ch 5 [low] Exam traps, first bullet: "In the example P1 completes at 3 s but waits 0 s" is true only in the FCFS lane; under SJF P1 waits 1.8 s. As written a student may think it holds for the whole example.
- ch 6 [low] Exam traps, fourth bullet: "Adding replicas inside one rack or zone: they share a failure domain, so availability does not rise" is too absolute. Replicas in one rack do protect against a single disk or server crash, so availability against those faults does rise; what they fail to protect against is a rack, zone or power failure.
- ch 6 [low] Beyond: "Cloud providers publish per-region error budgets" mixes two things. Providers publish SLAs and service health per region; an error budget is what a consuming team derives from its own SLO, and the team spends it on releases.
- ch 7 [low] Section 1, sentence after the power formula: "Energy is power over time" is ambiguous English. A second-language reader can read "over" as division (P ÷ t), which would give the wrong unit for kWh.
- ch 7 [low] Section 1, after the 260 W calculation: "so idle servers waste most of the power" does not follow clearly from the number just shown. The 260 W is a loaded server, not an idle one; the reader needs the point that the 200 W idle part, not the 60 W load part, is the big share.
- ch 7 [low] Section 3, last line: The pointer to Chapter 4.6 is plain text, so on a phone it is not tappable like the other chapter cross-references in the series.
- ch 8 [high] Section 2 and Quiz Q5: The section says it gives a 'six-way market list' but then lists seven items (posted price, on-demand, reserved/subscription, spot, auction, bidding and bargaining, differentiated/priority). Quiz Q5 asks for six categories, and its answer drops reserved/subscription — the very scheme used in Worked example 1. A student cannot tell whether reserved is one of the categories.
- ch 8 [low] Section 1: The text says the model names six parts including pricing policy, but the bullet list that follows replaces pricing policy with the optional 'market directory or auctioneer', which the same paragraph described as an addition in some versions.
- ch 9 [low] Section 1, multi-cloud definition: "a copy of the data in each" is presented as part of what multi-cloud means, but replication is not a defining property. A student may write in the exam that multi-cloud always keeps a copy of the data in every provider.
- ch 9 [low] Section 2, discovery step: VM and SLA are used for the first time without being expanded. Many readers in the first week of the course may not know the short forms.
- ch 9 [low] Section 2, cost formula: The egress term D × e uses one D and one e, but egress price and volume differ per provider, so a mixed federation cannot be costed with a single rate. The worked example itself never uses the term.
- ch 9 [low] Section 3, third-party broker: A content-delivery network is given as if it were the definition of a third-party broker. A CDN is one example of a commercial broker; a broker is a role, not a network type.
- ch 9 [low] Figure versus worked example 1: The figure note says cloud C "stays a dashed offer" and the aria text calls it an "unused offer", but the worked example says the broker may send delay-tolerant batch work to C. The two statements disagree.
- ch 9 [low] Worked example 1, step 5: Step 5 says B "adds about 0 ms", while the setup says B's delay is "close to A". The reader is left unsure whether B adds delay or none.
