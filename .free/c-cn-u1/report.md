# c-cn-u1: free-model run

- Book: `books/cse/c-cn/c-cn-u1.html`
- Status: ok
- Model calls so far: 24 (69,500 tokens in, 68,259 out), 2.8 minutes

## Checker

```
c-cn-u1.html: 8 chapters, 10063 words, 9 figures, 119 KB
OK
```

## For the reviewer

- chapter 3: a c program's shown output was replaced by its real output; check the text around it

## Reviewer notes (after any revision)

- ch 2 [high] Worked example 1: The example adds the capacities of three links (LAN, MAN, WAN) as if they were parallel, but in a typical end‑to‑end path the links are sequential. The effective bandwidth of the path is limited by the smallest link (100 Mbps), not the sum 11.1 Gbps.
- ch 2 [low] Section 2: The term "dense‑wave‑division‑multiplexed (DWDM)" is incorrect.
- ch 2 [low] Section 3: Reference to "ring MAN may use a token ring" is outdated; token‑ring technology is not used in modern MANs.
- ch 3 [high] Section 1: Bus topology, termination step: The termination resistor is given as 75 Ω, but Ethernet coaxial bus (10BASE2/10BASE5) requires a 50 Ω resistor at each end.
- ch 3 [high] Quiz Q3 (apply, 4 marks): The answer is incorrect and confusing. It treats "three layers of switches" as three switches total, leading to an impossible negative unused port count.
- ch 3 [low] Section 1: Bus topology, CSMA/CD description: The text says CSMA/CD is used "to avoid collisions"; CSMA/CD actually detects and resolves collisions.
- ch 3 [low] Section 2: Star and tree topologies, hub statement: It states "Each link can operate at full duplex; the hub/switch determines the aggregate bandwidth," implying hubs support full duplex, which is false (hubs are half‑duplex).
- ch 3 [low] Section 1: Bus topology, repeaters comment: The statement "repeaters extend the bus" is outdated for modern Ethernet; repeaters are rarely used and are replaced by switches or media converters.
- ch 3 [low] Section 2: Star and tree topologies, aggregate bandwidth formula: Formula C_agg = N × C_link suggests the hub can always handle the sum of link speeds, ignoring the switch’s backplane capacity.
- ch 4 [low] Lead paragraph: The phrase “speak a uniform protocol to the layer above” is inaccurate because each layer uses its own protocol, not a uniform one.
- ch 4 [low] Section 2, first paragraph: The description of a service‑access point (SAP) is vague and may confuse students.
- ch 4 [low] Section 1, last sentence: The statement “Only a few universities call this topic ‘protocol layering’ in their syllabus” is vague and not verifiable.
- ch 4 [low] Formula description in Section 2: Units for Header_i are not explicitly stated.
- ch 4 [low] Worked example 1, dry‑run table: The key name “head” is unclear; it should describe the column contents.
- ch 4 [low] Quiz Q8 answer: The answer mentions “processing delay of each layer is usually small” without clarifying that it can be significant in some cases.
- ch 5 [high] Section 2, sentence about checksum failure: The text says "if the checksum fails, the error is in the Data Link layer" which is incorrect because checksums exist at multiple layers (e.g., Transport layer TCP/UDP checksum, Network layer IP header checksum, Data Link layer FCS). Attributing all checksum failures to the Data Link layer is a factual error.
- ch 5 [low] Section 2, sentence about packet drop: The statement "If a packet is dropped, the Network layer header points to a routing issue" is vague; packet drops can be caused by many factors, not only routing problems.
- ch 6 [high] Section 2: The statement "IPv6 adds built‑in security and eliminates the need for NAT" is inaccurate. IPv6 includes optional IPsec support, not mandatory security, and while NAT is generally unnecessary, it can still be used in some deployments.
- ch 6 [low] Section 3: The description of the TCP header mentions only source/destination ports, sequence number, and checksum. It omits other mandatory fields such as acknowledgment number, data offset, flags, window size, and urgent pointer.
- ch 6 [low] Worked example 1: The calculation of total bytes on the wire ignores the Ethernet frame trailer (4 B CRC) and the preamble/IFG, so the reported size (554 B) is lower than the actual on‑wire size.
- ch 6 [low] Section 2: The sentence "Routers operate only at the Internet layer" oversimplifies router operation. Routers also process Link‑layer frames to forward them on the next hop.
- ch 7 [high] Section 1: Circuit switching – dedicated path: The sentence "Because the bandwidth on each link is fixed, the user gets a guaranteed data rate and a constant propagation delay" incorrectly attributes constant propagation delay to fixed bandwidth.
- ch 7 [low] Section 2: Packet switching – shared links: The delay formula D = L ⁄ R + Q omits the propagation delay (and processing delay) that are part of total packet delay.
- ch 7 [low] Section 2: Packet switching – shared links, bullet point: The wording "a packet can use any free link at the moment it arrives" oversimplifies routing and may mislead students.
- ch 8 [low] Quiz Q2: The answer says "only devices sharing the same port can collide", which is confusing because typically only one device is attached to a port. The intended meaning is that only devices on the same link (connected to the same switch port) can collide.
- ch 8 [low] Quiz Q6: The answer states that a switch creates a single broadcast domain for all attached ports, ignoring the possibility of VLANs which create multiple broadcast domains.
- ch 8 [low] Lead paragraph: It says "Network devices move frames or packets" and includes hubs, which actually repeat raw electrical signals rather than frames.
