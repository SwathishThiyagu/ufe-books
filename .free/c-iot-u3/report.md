# c-iot-u3: free-model run

- Book: `books/cse/c-iot/c-iot-u3.html`
- Status: ok
- Model calls so far: 36 (135,421 tokens in, 223,773 out), 5.6 minutes

## Checker

```
c-iot-u3.html: 9 chapters, 16452 words, 10 figures, 179 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, standards-body table (ITU-T row): The table gives IMT-2020 as an ITU-T output. IMT-2020 (the 5G framework) is an ITU-R (Radiocommunication Sector) Recommendation. ITU-T writes telecom network standards, but IMT-2020 itself is not an ITU-T standard, so the row teaches a wrong body-to-standard pairing.
- ch 1 [low] Section 2, sentence 'Links to the detailed standards are in IEEE 802.15.4, 6LoWPAN and Bluetooth Low Energy.': The text promises links but the chapter names are plain text, so the student cannot tap through on a phone. The same happens with 'see industrial protocols' in Section 3.
- ch 1 [low] Lead and Section 1, opening lines: The definition of a protocol is written twice in almost the same words ('A protocol is a set of rules for messages: who sends/which side sends, in what order, which fields appear, and what a reply means'). On a phone this reads as a printing mistake.
- ch 2 [high] Section 2, sentence after the BI/SD formula: The duty cycle is printed as 'SD / BI = 2SO−BO' with no exponent. Read literally this is 2×SO − BO, which is wrong; for BO = 6, SO = 3 a student would get 2×3 − 6 = 0 instead of 1/8. The quiz answer Q6 uses the correct exponent form, so chapter and quiz disagree.
- ch 2 [low] Section 1, last sentence: 'The PHY adds 6 bytes around the PSDU' suggests bytes on both sides. All six PHY overhead bytes (preamble, SFD, length) come before the PSDU; nothing is added after it.
- ch 2 [low] Figure (PHY frame block diagram): The FCS is drawn as a separate block after the 'MAC frame' block and linked by an arrow from it. The FCS is not extra PHY overhead; it is the last 2 bytes inside the MAC frame. A student may add 2 bytes to the 127-byte PSDU when computing air time.
- ch 2 [low] Quiz Q7 answer: The answer says 127 − 40 = 87 B is left for transport and application. The MAC header (up to 25 bytes) and the 2-byte FCS also sit inside the same 127-byte PSDU, so the real payload left after the IPv6 header is far less than 87 B.
- ch 2 [low] Lead, last sentence: 'This chapter completes the subject' clashes with the chapter's own pointers to Chapter 3.3 (ZigBee) and Chapter 3.5 (6LoWPAN), which come later.
- ch 3 [low] Section 1, device roles (last sentence): The sentence says flatly that the end device is a reduced-function device. In ZigBee a ZigBee end device may be built on either an FFD or an RFD; only the coordinator and routers must be FFDs. As written it contradicts the standard texts.
- ch 3 [low] Section 2, profiles paragraph: "Some syllabi call these application profiles, others the ZigBee application layer" treats two different things as two names for one thing. The ZigBee application layer is the whole upper layer (APS + ZDO + application framework); an application profile is one of the documents that defines clusters such as HA or SE.
- ch 3 [low] Worked example 1, step 1: The count of 5 parents with 6 free child slots each ignores that in ZigBee every router itself joins as a child of some parent, so it occupies one of the coordinator's (or another router's) child slots. The number 30 therefore double-counts capacity; a student who takes the example literally will get a different answer in an exam that states the routers are children of the coordinator.
- ch 3 [low] Worked example 1, part (b): "How many end devices lose their parent?" is ambiguous. Strictly, every child of the two failed routers loses its parent; the number 2 is the number that cannot find a new parent after re-joining.
- ch 4 [high] comparison table, Latency row: Classic Bluetooth connection setup is given as 'tens of ms'. Classic setup needs an inquiry (up to 10.24 s) plus paging, so in practice it takes hundreds of milliseconds to a few seconds, not tens of milliseconds. The row also labels the BLE 7.5 ms figure as latency, but 7.5 ms is the minimum connection interval, which only bounds the latency.
- ch 4 [low] comparison table, Data rate row: The classic column says only '1 Mbps Basic Rate', while Section 1 states that EDR raises classic Bluetooth to 2 or 3 Mbps. A student reading only the table will think classic tops out at 1 Mbps, the same as BLE.
- ch 4 [low] Figure (sequence diagram): The figure shows SCAN_REQ and SCAN_RSP as fixed steps of every connection setup. The text correctly says a central sends SCAN_REQ only if it wants extra data, so the picture overstates active scanning.
- ch 5 [high] Quiz Q4: The answer says the objective function 'may lower its rank'. In RPL, rank counts distance from the root, so a node whose parent link turns lossy must move to a higher rank (further from the root), not a lower one. A student copying 'lower its rank' into the exam writes the opposite of what happens, and it also contradicts Q6, where moving one hop away raises rank by one.
- ch 5 [high] Figure (DODAG tree): E3 is drawn as a child of R2, which is at rank 1, yet E3 is labelled rank 3, skipping rank 2. Q6 in the same chapter teaches that under a hop-count objective a child of a rank-1 node gets rank 2. The figure and the quiz contradict each other, and the caption's 'rank rises as nodes move away from the root' does not explain a jump of two.
- ch 5 [low] Section 1: 'Some syllabi call 6LoWPAN IPv6 over Low-Power Wireless Personal Area Networks' presents the standard full form as if it were an optional syllabus variant. Students may think the expansion is one of several competing names.
- ch 5 [low] Section 2, header compression: 'IPHC sends a short tag and the changing fields' reuses the word tag, which this chapter already uses for the fragmentation datagram_tag, so the two mechanisms look alike. IPHC has no tag: it sends a dispatch byte plus bit flags that mark which header fields are elided and which are carried in compressed form.
- ch 6 [low] Figure caption (QoS 1 flow): The caption states as a rule that 'the publisher gets PUBACK before the broker forwards the message'. MQTT does not fix this ordering: the broker may forward to subscribers before or after it sends PUBACK. A student may read the diagram as a guaranteed sequence in the protocol.
- ch 6 [low] Figure spec (QoS 1 flow): The forwarded PUBLISH is labelled 'PUBLISH QoS 1' and the subscriber replies PUBACK. The broker actually delivers at min(publisher QoS, subscription QoS), so if the subscription QoS is 0 the forwarded packet carries QoS 0 and there is no PUBACK from the subscriber. The figure contradicts the text of Section 2.
- ch 6 [low] Section 1 / Exam traps (wildcard rule): '# matches all remaining levels and must be the last character' is incomplete. The multi-level wildcard must either stand alone or follow a level separator, so a topic filter such as home/room# is invalid even though # is the last character.
- ch 6 [low] Quiz Q1: The lead hedges ('Some syllabi call MQTT Message Queuing Telemetry Transport') while Q1 asks for the expansion as if it were fixed, so the student gets two different messages about the same fact.
- ch 7 [low] Section 1, opening paragraph: The LPWAN data-rate range is given as '0.3 to 50 kbit/s'. The 0.3 kbit/s floor is a LoRa figure and the 50 kbit/s ceiling sits below the NB-IoT peak (about 100 kbit/s in downlink multi-tone), so a student may wrongly conclude that NB-IoT cannot exceed 50 kbit/s.
- ch 8 [high] Quiz Q4: The answer contradicts the chapter's own definition. Section 2 and Q3 say a notification is sent when Present_Value moves by MORE than COV_Increment. The step from 22.6 °C to 23.1 °C is exactly 0.5 °C, which is equal to, not more than, the increment of 0.5 °C. So 23.1 should not trigger a notification. The answer says it does trigger.
- ch 8 [low] Figure (WirelessHART stack) and Section 3: The stack is drawn and described as four layers: Application, Network, Data link, PHY. The standard WirelessHART stack has five layers; the transport layer between application and network is missing. The text elsewhere talks about end-to-end delivery and retries, which the transport layer is responsible for, so a student may wonder where that sits.
- ch 9 [low] Section 1 (mDNS): The sentence 'A client multicasts a query holding one question' reads like a rule of the protocol. mDNS packets may legally carry more than one question; one question per packet is only the common practice, so a student may wrongly mark a multi-question mDNS packet as invalid.
- ch 9 [low] Section 2 vs Figure: Section 2 lists the PTR, SRV, TXT and A/AAAA lookups as separate steps, but the figure shows one question and three answers arriving together. Both are correct in practice because a responder normally puts the SRV, TXT and address records in the Additional section of the reply to a PTR query, but the text never says this, so the figure and the steps appear to contradict each other.
- ch 9 [low] Quiz Q4: The answer implies the client waits until the record is fully expired at t = 4500 s before refreshing. mDNS cache maintenance re-queries earlier for records in active use, so the answer is incomplete rather than wrong.
