# c-cn-u1: free-model run

- Book: `work/claude_figs/c-cn-u1/tree/books/cse/c-cn/c-cn-u1.html`
- Status: ok
- Model calls so far: 38 (147,920 tokens in, 251,678 out), 8.3 minutes

## Checker

```
c-cn-u1.html: 8 chapters, 16729 words, 9 figures, 180 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1 and the figure: Section 1 lists the five components as message, sender, receiver, medium and protocol and says 'The five parts are drawn as a chain in the figure below'. The figure is titled 'Five components of data communication' but its five boxes are source, modem, medium, modem, server. There is no message box and no protocol box, so the figure names a different set of five from the text. A student revising from the figure will list the wrong five.
- ch 1 [high] Beyond box: 'Mobile networks already switch between half-duplex and full-duplex operation in time division duplex (TDD) bands' is wrong. A TDD band uses one frequency and alternates the direction in time, so it does not become full-duplex. Uplink and downlink speeds differ because the frame gives each direction a different share of time slots, not because the link switches to full duplex.
- ch 1 [low] Section 3, simplex paragraph: 'Simplex works only when the protocol is right in advance' is vague; 'right' does not say what must be right.
- ch 1 [low] Section 3, simplex example: 'A server pushes a bank statement that your app can only read' suggests the phone sends nothing at all, yet the app had to request the statement. The example hides the request and can mislead a student about what simplex means here.
- ch 2 [low] Worked example 1 step 6, Worked example 2 steps 2–3, Quiz Q5 answer: The division is written as '544 × 10⁶ ÷ 34 × 10⁶'. Read left to right by normal precedence this multiplies back by 10⁶ and gives a nonsense answer (1.6 × 10¹⁰); the powers of ten must be grouped or cancelled before the numbers are divided.
- ch 2 [low] Section 1, LAN bullet: 'A VLAN is a logical LAN carved inside one switch' is too narrow. A VLAN is a logical grouping of ports that normally spans several switches joined by trunk links, which is exactly why one building can be split into several LANs.
- ch 2 [low] Section 1 last paragraph, Exam trap 1, Quiz Q8 answer: The invented term 'private WAN-style link' for a 40 km or 25 km fibre inside one company conflicts with the chapter's own span table (MAN is roughly 5–50 km) and leaves students unsure what to call such a link. Q8's answer only labels the rented case as a MAN.
- ch 2 [low] Exam traps, second trap: 'Divide by 8 the wrong way and you are off by 64' is hard to follow. Converting MB to Mbit means multiplying by 8; a student who divides instead is off by a factor of 64, but the sentence does not say which operation is the wrong one.
- ch 2 [low] Figure caption and aria text: The caption says the figure shows LAN as 'the one network a single organisation owns' and that ownership passes from one organisation to many as you move right. Exam trap 4 and Section 1 both say a company can own its own city-wide links, so the caption overstates the rule.
- ch 3 [high] Exam traps, last bullet: The trap tells students that a bus cable break 'splits the bus' and that 'nodes on one part may still work'. Standard textbooks say the opposite for a bus: a break in the backbone removes termination, causes reflections and stops all transmission, even between devices on the same side of the break. A student who writes the trap's version in an exam loses marks.
- ch 3 [low] Section 1 and Section 3 table: The symbol n changes meaning. In the mesh formulas n is the total number of nodes, but in the star row of the table (and the star paragraph) n counts only the end devices, so the switch is not counted. A student who uses n = total nodes for a star gets n − 1 cables and n − 1 central ports.
- ch 3 [low] Section 1, growth sentence: It says adding a node to a full mesh needs 'n new cables and n new ports across the old nodes', but the new node also needs n ports of its own, and the total port count is not mentioned. The sentence understates the cost.
- ch 4 [high] Worked example 1: The arithmetic gives a 1,558-byte Ethernet frame for a 1,500-byte application message. Standard Ethernet MTU is 1,500 bytes of IP payload, so 1,500 bytes of application data plus 20-byte TCP and 20-byte IP headers is 1,540 bytes and cannot fit in one Ethernet frame; max Ethernet frame size is 1,518 bytes. In practice TCP MSS limits application data to 1,460 bytes or IP fragments the packet.
- ch 4 [low] Section 2: The statement that 'every layer adds its own header' is not true for the physical layer. The physical layer sends the frame as bits/signals and adds no header, so a student may wrongly think physical-layer encapsulation exists.
- ch 5 [low] Section 1: "Each layer has exactly one job" contradicts the chapter's own layer list in Section 2, where the data link layer is given four jobs (framing, MAC addressing, error detection, medium access control) and the network layer three. A student can read this as a strict rule and then be confused when the same chapter lists several duties per layer.
- ch 5 [low] Lead: "built it in the 1980s" is loose about the history: the work began in the late 1970s and the reference model was published as an ISO standard in 1984.
- ch 5 [low] Quiz Q3(e): "Keeping a user logged in across many requests" is ambiguous: in real software that is usually done by the application (cookies, tokens), so an examiner could mark either session or application.
- ch 6 [high] Section 1, end of the section: It says the top three layers run only on the two end hosts. The internet layer is the exception: IP is implemented in every router as well as in the hosts, and routers read and rewrite the IP header at every hop. Only the application and transport layers are confined to the end hosts.
- ch 6 [high] Worked example 1, steps 6 and 7: The counts contradict the definition given one line earlier ('end-to-end means the protocol runs only in the two end hosts'). IP is processed by every router in the path, not only by the two end hosts, and ICMP is generated by routers too (destination unreachable, time exceeded). Step 7's own definition, 'runs on every device along the path', therefore also fits IP and ICMP, yet they are left out of the hop-by-hop count. The arithmetic 5+2+2+... = 9 is consistent but the classification is wrong.
- ch 6 [low] Beyond: QUIC is described as carrying HTTP/3 'with its own reliability built inside the application'. QUIC is normally classed as a transport protocol implemented in user space above UDP; calling it part of the application blurs the layer it is usually placed in, which is exactly what a student will be asked about.
- ch 7 [low] Section 3, third paragraph: "a 0.5 s setup twice" is unclear: it can be read as two setups of 0.5 s each. What the worked example actually charges is 0.5 s setup plus 0.5 s teardown, 1 s in all.
- ch 7 [low] Worked example 1, answer line: "Packet switching wins here because setup dominates" overstates the numbers. Setup plus teardown is 1 s of the 9 s circuit total, roughly 11 percent, and packet switching wins by only about 0.98 s. A student may quote "setup dominates" for a 1 MB file at 1 Mbps, which the arithmetic does not support.
- ch 7 [low] Section 2, first paragraph, and Quiz Q7: "Each packet carries a header with ... a sequence number" and "A sequence number in the header" are imprecise for IP. The IP header has no sequence number; ordering is done by a sequence number in the transport header (TCP), and UDP has none.
- ch 7 [low] Figure caption: The packet lane shows four back-to-back 3 s packets on a single link and ends at 12 s, so the figure shows no store-and-forward delay across hops even though the aria text says the packet lane pays per-packet store-and-forward. A reader may conclude packet switching never adds hop delay.
- ch 8 [high] Section 2, also the lead and Q6 answer: The blanket statement that each switch port is its own collision domain is wrong when a port connects to a hub: that port shares one collision domain with every device on the hub. The figure has such a hub under Switch 1, and the correct count there puts the hub and PC 1, PC 2, PC 3 in one domain together with the switch port. A student applying the blanket rule would add a false extra domain and get the count wrong.
- ch 8 [low] Section 2, actions list: The three actions omit the filter case: when the destination MAC is on the ingress port p, the switch drops the frame. The rule is only implied by the flooding bullet.
- ch 8 [low] Section 2: MAC table aging and multicast flooding are not mentioned; both are standard switch behaviour and exam answers often expect them.
- ch 8 [low] Section 3, figure paragraph, and exam trap 5: PC 4's full-duplex port is counted as a collision domain, while the chapter defines a collision domain as devices whose transmissions can collide and says a full-duplex port has no collisions. Students need the counting convention stated explicitly.
