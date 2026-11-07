# c-iot-u6: free-model run

- Book: `books/cse/c-iot/c-iot-u6.html`
- Status: ok
- Model calls so far: 29 (113,619 tokens in, 200,486 out), 6.8 minutes

## Checker

```
c-iot-u6.html: 6 chapters, 12343 words, 7 figures, 134 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Figure spec at the end of Section 4: The caption says the hub applies local rules and that 'the local path never depends on the cloud', but the block diagram has no edge from the hub to the relay. The only path to the relay lamp runs cloud → relay. A student reading the figure sees local control producing no action, which contradicts Sections 1 and 2.
- ch 1 [low] Section 4, first paragraph: The claim 'Most of a smart home bill is standby power' is contradicted by the chapter's own worked example, where the always-on hub and cameras are 312 of 762 Wh/day, about 41 %, which is not most. It also stretches the standard meaning of standby power (power drawn while a device is idle or in low-power mode) to cover devices doing useful work 24 h a day.
- ch 1 [low] Section 1, sensor list: The rule example uses lux ('IF motion = 1 AND lux < 200'), and Section 3's code uses a light level, but no light sensor appears among the sensors listed (PIR, door, temperature). The reader never learns which device produces lux.
- ch 2 [low] Section 3 table, NB-IoT power column: 'Years on one cell' is ambiguous in a cellular chapter; a student may read 'cell' as a radio cell (base station) rather than a battery cell.
- ch 2 [low] Section 2 message paragraph and Worked example 1: Section 2 says the sensor sends a state change plus a heartbeat every 5 minutes, but the worked example silently counts only one 60-byte message per slot per 5 minutes. A student may not see why the extra state-change messages are ignored.
- ch 2 [low] Quiz Q6: 'tens of kB, roughly a thousand times the 60-byte message' is loose arithmetic: 20 kB is about 330 times 60 B, and only about 60 kB reaches a thousand times.
- ch 2 [low] Section 1, water bullet: The cross-reference to 6.5 is plain text, so it is not a clickable chapter link like the rest of the book.
- ch 3 [low] Section 2 (edge vs cloud paragraph) and Quiz Q5: The text says edge computing 'keeps the line running during a wide area network outage'. The line keeps running because control sits in the local PLC, not because of edge computing. A student may conclude that edge computing is needed for production to continue.
- ch 3 [low] Section 1, automation hierarchy paragraph: 'OPC-UA is an integration name for exchanging plant data' is vague and the name is usually written OPC UA. It is an open communication standard, not just a name.
- ch 3 [low] Section 2 opening: The text says 'Four building blocks appear in most Industry 4.0 designs' and lists four, then treats edge computing, cloud computing and security as further blocks. The count does not match the content.
- ch 3 [low] Quiz Q4 answer: The premise says the plant 'still sends only daily OEE to ERP', but the answer says 'the data is not feeding MES or ERP decisions'. This reads as a contradiction and can confuse the student.
- ch 3 [low] Quiz Q6 answer: The answer only expands the acronym and names the factors; it does not define what OEE measures, which is what the question asks.
- ch 4 [high] Section 2, table: The table's second column is headed 'Sampling period', but its cells hold what is being sensed ('wheel speeds and load', 'radar/lidar gap updates'), not a period in seconds. A student will read the header and think those phrases are time values, so the table contradicts its own header.
- ch 4 [low] Section 2, table row 1: EBD is used as a row label before it is expanded anywhere in the chapter; the definition only comes in the paragraph after the table. Students meeting the abbreviation cold must guess.
- ch 4 [low] Quiz Q6: '1000-count encoder' does not say counts per revolution, yet the answer multiplies revolutions per second by 1000, which only works if the 1000 counts are per wheel revolution.
- ch 5 [low] Worked example 1, steps 5 and 7 (and the third exam trap): A motor's HP rating is its rated shaft (mechanical) output, not its electrical input. Step 5 labels 0.5 × 746 = 373 W as 'electrical input power', so the energy and cost figures are for shaft output, not for what the meter records. Actual input is 373 W ÷ efficiency, larger than 373 W.
- ch 5 [low] Section 2, last line of the fall-detection paragraph: 400 h is 400 ÷ 24 ≈ 16.7 days, so 'about 16 days' rounds the wrong way; the other life estimate in the chapter (167 h → about 7 days) rounds correctly, so the two look inconsistent.
- ch 5 [low] Section 1, the four parts and the bullets below them: The buffer is placed in two different places. The parts list says the gateway 'holds the network link and a short buffer', but the second bullet says the board 'keeps it in a small buffer' and the third bullet says the gateway 'publishes the buffer'. A student cannot tell which device is buffering.
- ch 5 [low] Quiz Q5: The answer assumes readings land at 10:00 and 10:05, so both are outside the 10:02–10:04 dip. With a 5-minute interval the readings could equally land at 10:02, or at 10:01 and 10:06; in the first case the dip is caught. The loss is a worst case, not a certainty, and the answer does not say so.
- ch 5 [low] Section 2, fall-detection rule: The magnitude a is defined in m/s² and rest is given as 9.81 m/s², then the threshold jumps to '2.5 g' with no conversion, so the student must switch units mid-rule.
- ch 6 [high] Worked example 1: A leftover template artifact sits inside the worked example: 'dry run: {'head': ['i', 'a[i]', 'sum'], 'rows': []}'. It is an empty array-trace table from a programming example and has nothing to do with the farm data-rate calculation. A student reading the page sees debug output with undefined symbols i, a[i] and sum.
- ch 6 [low] Worked example 1 step 5, exam traps, quiz Q7: The 51-byte LoRaWAN application payload limit is stated as a single fixed number. It is the maximum FRMPayload only for some regions and data rates (for example EU868/IN865 at the common data rates); other regions and higher data rates allow much larger payloads (up to 242 bytes in US915). A student may carry away 'LoRaWAN payload is always 51 bytes'.
- ch 6 [low] Quiz Q6 answer: 'A common offset cancels out in the decision' is wrong. A constant offset does not cancel; it shifts the reading, so the farmer's local threshold is crossed at a slightly different true moisture. The point is that a local, relative decision tolerates the offset, not that it disappears.
- ch 6 [low] Section 3, energy paragraph: 'the customer is credited for the shed units' is ambiguous: 'units' can read as the appliances that were switched off rather than the kWh not consumed.
- ch 6 [low] Section 3, vehicle paragraph: 'a remote route needs satellite' is unclear; 'remote route' is not defined and reads as if the route itself, not the coverage area, needs satellite.
- ch 6 [low] Figure and caption: The tree shows only agriculture, logistics and energy, but the chapter also treats retail, environment, wearables and vehicles, and the caption says 'Each domain reuses the same sensor–network–cloud chain', which overreaches for a three-branch figure.
- ch 6 [low] Section 2 and Section 3 cross-references: References to other chapters ('the same chain is described for water systems in remote monitoring and water management', 'is the same closed-loop structure covered in industrial IoT', 'in Unit 5') are plain text with no chapter links, so a phone reader cannot jump to them.
