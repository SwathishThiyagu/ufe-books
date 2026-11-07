# c-iot-u2: free-model run

- Book: `books/cse/c-iot/c-iot-u2.html`
- Status: ok
- Model calls so far: 40 (161,436 tokens in, 281,542 out), 6.8 minutes

## Checker

```
c-iot-u2.html: 7 chapters, 13402 words, 8 figures, 151 KB
OK
```

## For the reviewer

- chapter 5: the figure cannot be drawn: tree label "Embedded platform" is too long; shorten it
- chapter 5: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 4, Resistive bullet: The platinum RTD temperature coefficient is given as "about 0.385 Ω per Ω per °C". Per ohm per °C the correct value is 0.00385; 0.385 is the change per °C of a 100 Ω element, i.e. 0.385% per °C. As written the coefficient is 100 times too large and a student will compute a 100 Ω RTD changing by 38.5 Ω/°C.
- ch 1 [high] Section 3, Second order bullet: The sentence "ζ  1 is sluggish" has lost its comparison signs and the crucial middle case, so it conveys no usable rule about damping.
- ch 1 [high] Section 2, Range bullet: "Span = y_max − y_min, the width of the output, here 100 °C" mixes the two conventions: y is defined as the output in the sensitivity formula, but 100 °C is the input range. Worked example 1 then computes span on the output (16 mA). A student cannot tell whether span belongs to input or output.
- ch 1 [low] Section 4, Inductive bullet: The LVDT is said to slide a core "between two coils", while quiz Q3 correctly speaks of a primary and two secondary coils. The two descriptions do not match.
- ch 1 [low] Figure and its caption: The caption says the resistive branch covers strain gauges, RTDs and thermistors, but the resistive node of the tree is labelled only "strain gauge, RTD". The thermistor promised by the caption is missing from the figure.
- ch 2 [low] Section 1, second paragraph: The chapter defines an actuator as converting a signal into motion or force, then lists a heater as an electrical actuator. A heater produces heat, not motion or force, and the chapter already puts expansion-based devices under thermal actuators. A student can read this as two different definitions of an actuator.
- ch 2 [low] Section 2, second paragraph: 'Hall sensors or a back-EMF estimate tell the driver the rotor position' hides an important limitation. Back-EMF is zero at standstill, so a sensorless drive cannot get position from it when starting. A student may think the two methods are interchangeable at all speeds.
- ch 2 [low] Section 3 and Worked example 1: The symbol p means number of magnetic poles in the Section 2 formula but lead-screw pitch in the worked example. The worked example also uses N for steps per revolution while the Section 3 formula uses N_r. In addition, the worked example calls the lead-screw pitch '2 mm per revolution'; for a multi-start screw, pitch (thread spacing) and lead (travel per revolution) are different.
- ch 2 [low] Exam traps, second bullet: 'It is not the resolution by itself' is ambiguous. A student may read it as saying microstepping does not improve resolution, which is false.
- ch 2 [low] Section 4, selection paragraph: 'A BLDC is efficient and fast but needs commutation' is imprecise: a brushed DC motor also commutates, mechanically. The point is that the BLDC needs an electronic driver to do it.
- ch 2 [low] Section 1 and Section 4, cross-references: '(see 2.1)' and 'Unit 4, Interfacing sensors and actuators with boards' are plain text, not chapter links, so a phone reader cannot jump to them.
- ch 3 [high] Section 2, sentence on the ADC: The text prints "210 = 1024". A student reads this as the number two hundred ten, which equals 1024 is false. The intent is 2 to the power 10.
- ch 3 [low] Section 2, last sentence: The wording "the microcontroller sets sleep current if it is not put into deep sleep" is garbled and can be read two ways; the reader cannot tell which state is being described.
- ch 3 [low] Lead: The lead says a sensor node is "the hardware form of this idea" (the smart object), but Section 1 says a sensor node only senses and forwards, while a smart object also adds actuation and identity. The two statements contradict each other.
- ch 3 [low] Figure, 'Inside a sensor node': The figure places an Identification block inside the sensor node, but Section 2 lists only four units for a node (sensing, processing, transceiver, power) and Section 1 says identity is what a smart object adds on top of a mote. The figure contradicts the text.
- ch 4 [high] Section 3 (Power source), quiescent-current paragraph, and Exam trap 3: The numbers contradict the stated claim. A 5 µA quiescent current added to a 10 µA sleep load gives 15 µA total, so the cell lasts 10/15 = 67% of the expected life — a cut of one third, not 'halves battery life'. Exam trap 3 says the regulator 'can double the sleep budget', which would need 10 µA of quiescent current, not 5 µA.
- ch 4 [low] Worked example 1, step 7: Life is not 'linear in average current'. It is inversely proportional, which is why a ten-times fall in current gives a ten-times rise in life. The wording teaches the wrong relation.
- ch 4 [low] Section 1, first paragraph: 'Runs no operating system' is too strong: many MCU products run a small real-time operating system such as FreeRTOS. What distinguishes an MCU is that it does not run a full Linux-class OS.
- ch 4 [low] Figure spec, LoRa node note: The figure note gives LoRa as '2–15 km, 50 kbps', which is only the top of the range; the table in Section 2 says 0.3–50 kbps. Also NB-IoT (about 100 kbps) is drawn at the same vertical level as ZigBee (250 kbps), which breaks the data-rate ordering the axis claims.
- ch 5 [low] Section 3, Arduino Uno paragraph: The claim that the sketch starts 'within milliseconds of power-on' is wrong for the Uno board, whose bootloader waits briefly for a serial download before handing over; it also contradicts the lead, which promises microsecond start-up. The microsecond figure belongs to the bare ATmega328P, not the board.
- ch 5 [low] Section 1, first bullet of the properties list: 'no keyboard or screen' is listed as a property of embedded systems, but the chapter's own SBC branch (Raspberry Pi 4 with HDMI, USB) has both. The bullet is false for half the family being described.
- ch 5 [low] Section 3, definition of microcontroller (MCU): Defining an MCU as 'running without an operating system' contradicts the same section, which says an MCU can run an RTOS, and the ESP32 note about loading one. Many MCUs ship with a small RTOS.
- ch 5 [low] Section 3, ESP8266 and ESP32 paragraph: 'still runs no operating system unless you load one' is misleading: the standard ESP32 toolchains (ESP-IDF, and the Arduino core underneath) include FreeRTOS, so an OS is present by default.
- ch 5 [low] Quiz Q5 answer: The arithmetic does not reproduce itself: 1.00 V / 0.000806 V = 1240.7, which truncates to 1240, not 1241.2 → 1241. The 1241.2 comes only from the unrounded LSB.
- ch 5 [low] Quiz Q7 answer: 'external memory' is offered as a fix on an Uno, but the ATmega328P has no external memory bus, so extra RAM cannot be added that way.
- ch 5 [low] Exam traps, first trap: A sensor giving 0-5 V is said to need only an external ADC, but most I²C ADCs on a 3.3 V Pi run from a 3.3 V reference; the 5 V swing must be divided down before the ADC as well.
- ch 6 [high] Section 3, paragraph after the transmit-energy formula: The sentence 'Transmit energy falls by a factor n' is wrong. Splitting d into n equal hops leaves the electronics term k·E_elec per hop, so the electronics cost grows with n. Only the amplifier part εd² falls, to εd²/n. Total transmit energy per bit for n hops is n·E_elec + εd²/n, which may be higher or lower than the single-hop value. A student will write the false 'factor n' claim in the exam, and it also contradicts the very next clause of the same sentence.
- ch 6 [low] Section 3, definition of ε under the transmit-energy formula: The chapter calls 100 pJ/bit/m² the typical free-space amplifier energy. The first-order radio model quoted in most textbooks uses E_elec = 50 nJ/bit with ε_fs = 10 pJ/bit/m² (free space) and about 0.0013 pJ/bit/m⁴ (multipath). Presenting 100 pJ/bit/m² as the typical value will conflict with the student's reference book.
- ch 6 [low] Exam traps, third trap (unit slips in the radio model): 'Using 100 instead of 100 × 10⁻¹² inflates the answer a thousand times' is arithmetically wrong. Dropping the 10⁻¹² factor inflates the amplifier term by 10¹², not 1000. A factor of 1000 comes from a different slip: writing 100 nJ/bit/m² where 100 pJ/bit/m² is meant.
- ch 6 [low] Quiz Q4, answer: The working '50 + 100 × 10⁻¹² × 40 000 × 10⁹' mixes units inside one expression: the 50 is already in nJ, while the second term is in joules until the ×10⁹ is applied. The final 4050 nJ is right, but the line as printed does not evaluate as written.
- ch 7 [high] Worked example 1, step 1 (and answer/dry run): The source is stated as 2 W ERP but step 1 uses it directly in S = P/(4πd²), which is the EIRP formula. ERP is referenced to a half-wave dipole, so EIRP = 1.64 × ERP. The example therefore understates the power density by a factor of 1.64 (2.15 dB), and this contradicts the chapter's own exam trap that says ERP is not EIRP.
- ch 7 [low] Section 3, singulation paragraph: Binary-tree splitting is described right after frame-slotted ALOHA inside the EPC Gen 2 discussion, so a student can conclude Gen 2 uses both. Gen 2 singulation is slotted ALOHA with the Q parameter; tree-walking is used by other UHF standards.
