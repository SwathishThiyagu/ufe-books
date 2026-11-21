# au-elec-u6: free-model run

- Book: `books/auto/au-elec/au-elec-u6.html`
- Status: ok
- Model calls so far: 21 (68,362 tokens in, 148,231 out), 4.0 minutes

## Checker

```
au-elec-u6.html: 8 chapters, 12958 words, 9 figures, 146 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3, exam traps and Quiz Q5: Class A, B and C are the standard SAE speed classes. Class D is not part of that standard classification; it appears only in some syllabi and textbooks for safety-critical/time-triggered buses. The chapter hedges once in Section 3, but the quiz then asks students to 'name bus classes A to D' as if all four were standard, and the answer gives Class D as fact.
- ch 1 [low] Exam traps, fourth bullet: 'Do not treat the letters as order of speed without checking' contradicts the rates just given, where A < B < C in bit rate. A student can read it as saying the letter order carries no speed meaning at all.
- ch 2 [high] Section 3, CAN FD: FDF sentence: It says classic nodes treat FDF as an error 'and do not disturb the bus'. A classic controller that sees the recessive FDF (and res) bit where it expects dominant raises a form error and transmits an error frame, which destroys the FD frame. The claim also contradicts the later line in the same section that a classic controller on the same bus rejects FD frames.
- ch 2 [low] Figure (frame field array) and its aria text: The aria says the identifier and bit-rate switch fields are highlighted, but the classic row marks 'ID' plus 'DATA' (as 'live'), and the CAN FD row marks only 'BRS'. The FD identifier is not highlighted, and the 'live' mark on classic DATA has no meaning given in the caption.
- ch 2 [low] Figure, CAN FD row: The classic row shows IDE (and RTR) between the identifier and DLC, but the FD row jumps from ID straight to FDF, so a student may think an FD frame has no IDE bit or that FDF replaces the whole control field.
- ch 3 [low] Section 1, bullet 'Break': The break field is described as something that 'wakes slaves'. Waking a sleeping cluster is a separate wake-up pulse; the break only marks the start of a frame and lets every slave detect the beginning and get ready to read the sync field.
- ch 3 [low] Section 1, paragraph on the header: 'A header names the slave or signal to be exchanged' is loose. The header carries the protected identifier, which names the frame, not a particular slave. A frame can be published by a slave, or published by the master as a command or diagnostic request, so the header alone does not point at a slave.
- ch 3 [low] Section 2, bullet 'Symbol window': The symbol window does not carry startup and wakeup. It carries the collision avoidance symbol (CAS) and the media access test symbol (MTS). Startup frames are sent in static slots, and wakeup uses a separate wakeup pattern.
- ch 3 [low] Section 2, bullet 'Dynamic segment': 'Short frames leave time for later slots' hides the actual mechanism. A node with data transmits inside its minislot and stretches it to the frame length, which shortens the time left for later minislots; a node with nothing to send uses only the minislot.
- ch 3 [low] Section 3, paragraph 1 (and exam trap 3): 'Office Ethernet needed four pairs' is true only for 1000BASE-T. Office 100BASE-TX uses two pairs. The comparison should state which office standard uses four pairs.
- ch 3 [low] Figure 'Bus comparison': The FlexRay row gives the access method as plain 'TDMA', which contradicts the chapter text saying only the static segment is TDMA and the dynamic segment is FTDMA. A student revising from the table alone will miss the distinction.
- ch 4 [low] Lead: 'Almost any car made after the late 1990s' is true for the United States (OBD-II required from 1996) and roughly for Europe, but not for India, where most cars sold before BS-VI had no OBD-II socket. An Indian student may expect a port on a 2010 hatchback and not find one.
- ch 4 [low] Section 3, bullet on CAN: The bullet couples bit rate to identifier length as if fixed: 500 kbit/s with 11-bit, 250 kbit/s with 29-bit. ISO 15765-4 allows four combinations (11-bit or 29-bit identifiers, each at 500 kbit/s or 250 kbit/s). Most cars use 11-bit at 500 kbit/s; 29-bit at 250 kbit/s is common on heavy vehicles.
- ch 4 [low] Section 3, paragraph on the lamp: 'When a fault is confirmed, the ECU stores the DTC and lights the MIL' hides the two-trip rule that examiners ask about. For most (two-trip) faults the ECU waits for the same fault on two consecutive drive cycles before lighting the MIL; only some faults light it on the first trip.
- ch 4 [low] Exam traps, second bullet: 'P1xxx ... needs enhanced diagnostics beyond the standard services' can be read as: a generic tool cannot see a P1 code. A generic tool does read P1xxx codes through service 03; what it lacks is the manufacturer's table that explains the code.
- ch 4 [low] Section 2, list of services: The service list jumps from 06 to 09 and never names service 07, pending codes, which students meet whenever a fault is seen once but the MIL is still off.
- ch 5 [high] Section 1, list of common rules: The chapter states a MISRA rule as 'no dynamic memory allocation after start-up'. MISRA C:2012 does not allow dynamic allocation after start-up; the allocation and deallocation functions of <stdlib.h> are banned outright (Rule 21.3, plus advisory Directive 4.12). A student who writes the chapter's version in an exam will be marked wrong.
- ch 5 [low] Section 2, definition of FTTI: 'The time from fault occurrence to a hazardous event' is loose. FTTI is the shortest such span for the given fault; without 'minimum' a student may treat it as a fixed measured time.
- ch 5 [low] Worked example 1, answer line: The arithmetic 200 − 20 − 40 − 30 = 110 ms is correct, but the sentence attached to it mixes the windows. The 110 ms is only the time left for the detection logic after sampling (20 ms) and confirmation (40 ms); detection is therefore complete 170 ms after the fault, and the actuator uses the last 30 ms to reach the safe state at 200 ms.
- ch 5 [low] Section 2, hardware metrics: SPFM and LFM are not measures of diagnostic coverage. They are architectural hardware metrics computed from failure rates and the diagnostic coverage of the safety mechanisms; diagnostic coverage is a separate input.
- ch 5 [low] Quiz Q6: The question does not say what the original ASIL was, and the answer does not mention that each decomposed requirement still carries the original ASIL as a tag (for example ASIL B(D)).
- ch 6 [low] lead paragraph: The lead says the car exchanges short radio messages with 'the grid', but Section 1 defines V2G as an electric vehicle that charges or sends power back. Power flow, not a safety radio message, is the main content of V2G, so the lead contradicts the definition later in the chapter.
- ch 6 [low] Figure caption and graph edges: The caption says 'the central car sends V2V, V2I and V2P messages', but Car 1 sits at the left of the layout, not in the centre, and the V2P edge is drawn from the pedestrian to Car 1, so the figure shows the pedestrian sending, not the car.
- ch 6 [low] Figure caption, dashed-link convention: The caption says dashed links are 'optional paths that use a roadside unit or the cellular cloud', yet Car 1 to RSU (V2I, using a roadside unit) is solid while Car 2 to RSU (also V2I, using a roadside unit) is dashed. The same kind of link is drawn two ways.
- ch 6 [low] Section 1 formula and definition: The formula uses the symbol v<sub>rel</sub> but the definition line and the worked example write the same quantity as 'vrel' and 'v_rel'. Students copying the symbol may be unsure which form is correct.
- ch 7 [high] Section 3, position-based routing paragraph (and exam trap 3): Perimeter mode of GPSR is described as forwarding 'around the void using the road graph'. In the standard definition, GPSR perimeter mode forwards on a planarized graph of the radio neighbours (Gabriel graph or relative neighbourhood graph) using face routing / the right-hand rule. It is the positions of neighbours, not the road layout, that define the faces. Students will reproduce a wrong mechanism.
- ch 7 [low] Lead and Section 1: The lead says a VANET works 'with no fixed base station', then Section 1 introduces the RSU, a fixed access point. A reader can take these as contradictory.
- ch 7 [low] Exam trap 3: 'Greedy forwarding ... guarantees delivery only after perimeter mode' reads as an unconditional guarantee. Delivery is guaranteed only when the network graph is connected and has been planarized, and the destination lies in the same connected component.
- ch 8 [low] Section 1: The US band is given as 5.85–5.925 GHz without noting the 2020 FCC reallocation, in which the lower 45 MHz went to unlicensed use, so the figure is out of date for a student reading current material.
- ch 8 [low] Figure: The text lists IEEE 1609.2 security as one of the four 1609 standards, but the stack diagram leaves it out, so a student may think security sits outside the stack.
- ch 8 [low] Quiz Q5: 1609.1 is a resource manager for applications, not a protocol layer in the stack, so calling all four 'IEEE 1609 layers' is loose and conflicts with the Figure.

## Correction pass (Claude, 21 Nov 2026)

- Packet on main now has 10 chapters: new 6.2 Network topology, OSI model and classification of bus systems and new 6.5 MOST and coupling of networks through gateways; the draft's chapters 2 to 8 moved to 3, 4, 6, 7, 8, 9, 10 (review files renamed to match).
- Every chapter rewritten from the draft against the exam course topics; every example and quiz answer traced; every reviewer flag above fixed.
- Every figure hand-drawn (pipeline/claude_figs/au_elec_u6.py); 15 long questions with full model answers.
- Checker: OK with --render.
