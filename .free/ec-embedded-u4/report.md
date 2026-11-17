# ec-embedded-u4: free-model run

- Book: `books/ece/ec-embedded/ec-embedded-u4.html`
- Status: ok
- Model calls so far: 22 (76,633 tokens in, 164,776 out), 4.8 minutes

## Checker

```
ec-embedded-u4.html: 7 chapters, 13397 words, 8 figures, 138 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Figure (UART frame for 'A' = 0x41, 8N1): Cell index 7 is marked 'live' but nothing in the caption or pointers explains it, and index 7 is data bit D6 = 1, not any special bit. A student may think bit 7 or the MSB is being highlighted, when the point the text makes is that the first data bit after start (index 1) is 1. The cell value itself is right.
- ch 1 [low] Section 3, TI description: 'Hardware sets TI = 1 after the stop bit leaves TXD' is one bit time too late. In mode 1 the 8051 sets TI when the 8th data bit finishes and the stop bit begins, which is why back-to-back bytes can be sent by loading SBUF right after clearing TI.
- ch 1 [low] Section 2, last sentence: EIA-232 is the formal name of the standard itself, not a nickname used by some syllabi, so grouping it with 'serial port' and 'COM port' as alternative course names is misleading.
- ch 2 [high] Section 1, paragraph on the shift register: "After eight pulses, the two bytes have swapped places. A 16-bit transfer simply repeats this 16 times." It is unclear what "this" repeats. A student can read it as repeating the 8-bit exchange 16 times, which gives 128 bits, not 16.
- ch 2 [low] Section 1, daisy chain sentence: "its MISO goes to the next slave" does not say which pin of the next slave receives the data. Read literally, MISO goes to MISO, which would be wrong.
- ch 2 [low] Quiz Q4 answer: The answer does not state the practical limit: a daisy chain works only if every device has a pass-through shift register (or the chain is built for it), and each device receives all bits shifted through it, so a transfer is four bytes long for four sensors.
- ch 3 [high] section 3: It says the LIN break 'wakes slaves and marks a new frame'. A break field only delimits the frame. A sleeping LIN node is woken by a separate wake-up pulse (the bus held dominant for roughly 250 µs to 5 ms), not by a break field. A student who repeats this in an exam will lose marks.
- ch 3 [low] section 2: Calling CAN 'CSMA/CA' (collision avoidance) is not uniform. Many standard textbooks describe CAN as CSMA/CD with non-destructive bit-wise arbitration, and CAN does detect bit-level collisions during arbitration. A student may think no collision ever happens on CAN.
- ch 3 [low] section 1: 'Standard bit rates are 125 kbit/s to 1 Mbit/s' reads as the full range of classic CAN. Classic CAN supports bit rates from about 10 kbit/s up to 1 Mbit/s; 125 kbit/s to 1 Mbit/s is only the usual automotive set.
- ch 3 [low] section 2: The list of errors that trigger an error frame leaves out the bit error, one of the five standard CAN error types (bit, stuff, CRC, form, ACK).
- ch 3 [low] section 3: 'This gives predictable latency without a crystal in every slave' joins two different benefits of two different mechanisms. Predictable latency comes from the master's schedule table; not needing a crystal comes from the sync byte, which lets each slave calibrate its own oscillator.
- ch 4 [low] Section 3, Centronics handshake steps: The step order suggests the host keeps STROBE asserted until the printer's ACK, and that after ACK the host 'can place the next byte'. In a Centronics port STROBE is a short pulse (held low for roughly 0.5 µs minimum) that the host returns high once the byte is latched, and the host must see BUSY low before putting the next byte on D0–D7. A student copying this order will draw the timing diagram wrongly.
- ch 4 [low] Section 1, transfer-type table, Control row: Calling control transfers 'best effort' misleads. Control transfers are error-checked with retries and are given reserved bus bandwidth; the type with no latency or bandwidth guarantee is bulk, which the table already says.
- ch 4 [low] Quiz Q8 and Section 3: IEEE 488 allows at most 15 devices on one bus counting the controller. A system of 15 instruments plus a controller is 16 devices and exceeds the limit, yet the question and answer say IEEE 488 'fits' for 15 instruments.
- ch 4 [low] Section 2, bus power sentence: The 500 mA figure is the maximum a device may draw after it is configured. Before configuration a device may draw only one unit load, 100 mA. Stating only 500 mA hides the link between enumeration and power.
- ch 5 [high] Section 4, LoRa paragraph: Each step up in spreading factor doubles the airtime — that part is right — but it cannot 'roughly double the link budget'. Link budget is measured in dB, so a doubling is meaningless, and the real gain is about 2.5 dB per SF step.
- ch 5 [low] Section 3, last paragraph: The sentence 'All these radios share 2.4 GHz and interfere' follows a section that includes LoRaWAN, but LoRaWAN sits at 865–867 MHz and never enters the 2.4 GHz fight.
- ch 5 [low] Section 1, first paragraph and formula: The text defines data rate as 'the useful bit rate in bit/s', then the formula uses R as the raw bit rate. A student will plug the application rate into t_air = N/R and get the wrong airtime.
- ch 5 [low] Worked example 1, output line: The output block prints six bare numbers (160, 0.00016, 0.0000267, 0.64, 0.1067, 4000) mixing microseconds, seconds and percent, so the reader cannot tell which number goes with which step.
- ch 5 [low] Section 4, LoRaWAN paragraph: The sentence 'The Indian band allows about 1 percent duty cycle per sub-band' presents a 1% duty cycle as an Indian rule. India's 865–867 MHz low-power rules are written mainly as a power limit (400 mW ERP); the 1% duty cycle is an operator practice borrowed from EU-style regulation, not a fixed Indian sub-band limit.
- ch 6 [low] Section 1, last paragraph, and the figure: The chapter states flatly that MQTT and CoAP 'sit at the application layer'. In the four-layer IoT model used here (perception, network, middleware, application) many syllabi file MQTT, CoAP and 6LoWPAN under the network layer, because they move data rather than present it to a user. A student with a different textbook will see an apparent contradiction.
- ch 6 [low] Quiz Q4 and the QoS 2 row of the table: The answer implies that QoS 2 gives exactly-once delivery all the way from publisher to subscriber. MQTT's exactly-once handshake works separately on each leg, publisher-to-broker and broker-to-subscriber, so it is exactly once per hop, not end-to-end across the broker.
- ch 6 [low] Section 2, QoS paragraph: 'The receiver acknowledges, so duplicates can happen' jumps a step: duplicates appear because a lost acknowledgement makes the sender retransmit a message the receiver already got. As written, a student may think the acknowledgement itself creates the duplicate.
- ch 7 [high] Section 2, the paragraph beginning "Bursts are the bandwidth trick": It says one address phase covers several beats and "the slave increments its own address; the address is not re-sent". That is AXI behaviour, not AHB. On AHB every beat of a burst has its own address phase: the master drives the next (incremented or wrapped) address while the previous data phase completes. A student who believes the slave increments the address will misread every AHB timing diagram and will wrongly compare AHB burst efficiency with AXI.
- ch 7 [low] Section 2, the bullet "HRESP reports OKAY, or ERROR over two cycles": The wording reads as if OKAY also takes two cycles. In AHB, OKAY is a single-cycle response; ERROR and the SPLIT/RETRY responses take two cycles. A student can mis-state the timing in an exam.
