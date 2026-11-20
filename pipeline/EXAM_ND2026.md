# Nov/Dec 2026 exam subjects (8 subjects, 2 per department)

Checked 20 Nov 2026. Timetable: the R2025 (revised 27 Oct 2026) and R2021 Nov/Dec 2026 UG timetables, read from a mirror of the official PDFs (the official exam site was not reachable from the workspace). Syllabi: the official R2025 (revised) and R2021 curriculum PDFs in the owner's 01_Syllabus_PDFs folder.

## Exam order

| Date | Exam course | Subject id | Year | Status of the date |
|---|---|---|---|---|
| 18 Nov FN | ME25301 Engineering Thermodynamics | me-thermo | Mech 2nd | read from the timetable |
| 19 Nov | EE3591 Power Electronics | ee-pe | EEE 3rd | date likely, session not confirmed |
| 20 Nov FN | EE25302 Electric Circuit Analysis | ec-circuits | EEE 2nd | read from the timetable |
| 21 Nov FN | AU3502 Automotive Electrical and Electronics | au-elec | Auto 3rd | read from the timetable |
| 30 Nov FN | EC25C04 Signals and Systems | ec-signals | ECE 2nd | read from the timetable |
| 30 Nov FN | AU25301 Automotive Engines | me-ic | Auto 2nd | read from the timetable |
| not found | EC3552 VLSI and Chip Design | ec-vlsi | ECE 3rd | not in the pages that could be read |
| not found | ME3591 Design of Machine Elements | me-design | Mech 3rd | not in the pages that could be read |

Automobile 2nd year: the R2025 Automobile semester 3 curriculum has AU25301 Automotive Engines (3-0-2, 4 credits), so me-ic stays. (R2021's AU3303 Automotive Engines sits on 3 Dec AN.)

## Packet changes (exam course added to `where`, missing topics added as subtopics)

Every packet of the eight subjects now has `where` entries for the exam course with the official topic lists, and `course_used.anna` names it. Subtopics added (unis = anna):

- ec-circuits (EE25302): u2 Compensation theorem; u4 Locus diagrams of RL, RC and RLC circuits.
- ec-signals (EC25C04): u1 Complete sets of orthogonal functions and Parseval's relation. Also cover the aperture effect in u5 "Low-pass, band-pass and practical sampling".
- ee-pe (EE3591): u2 Voltage doubler and three-phase diode bridge rectifiers; u2 Inversion mode and the inverter angle limit.
- ec-vlsi (EC3552; the packet was built from the testing course CEC362): u3 Interconnect parameters and electrical wire models; u3 Elmore delay model; u4 Pipelining and nonbistable sequential circuits; u4 Timing classification: synchronous and self-timed design; u4 Memory architecture: core and peripheral circuits; u5 Introduction to ASICs. Also cover shift registers in u4 "Static and dynamic latches and registers".
- me-thermo (ME25301; the packet was built from ME25C11 Applied Thermodynamics): u2 Unsteady flow processes; u3 Entropy generation and second-law analysis of control volumes (with the microscopic view of entropy); u4 Exact differentials, reciprocity and cyclic relations; u4 Expansivity, compressibility, Mayer relation and Joule-Thomson coefficient; u5 Gibbs phase rule. Also cover the state postulate and state diagrams in u1 "Properties, state, path, process and cycle". u6 (cycles) is not in ME25301.
- me-design (ME3591; the packet was built from the R2025 course ME25C06): u3 Connecting rods and crankshafts; u4 Riveted joints for structures and bonded joints; u4 Rubber springs; u5 Seals and gaskets. Also cover the crane hook and C frame in u1 "Curved beams". u6 (belts, chains, ropes) and u7 (gears) are not in ME3591.
- me-ic (AU25301; the packet was built from AU3303): u2 Gasoline direct injection (GDI); u2 Electronic ignition and laser ignition; u3 Gasoline fuel properties and cycle-to-cycle variations; u4 Crankcase ventilation; u6 Stratified charge and low heat rejection (LHR) engines. Also cover air filters and the throttle in u2 "Carburettors". u5 testing and most of u6 emissions are not in AU25301.
- au-elec (AU3502): u1 Vehicle electrical systems: power supply, wire sizing and circuit diagrams; u1 Electromagnetic compatibility and interference suppression; u3 Automotive microelectronics: semiconductor components and microcontrollers; u3 Fluid-mechanical actuators; u3 Electrical machines in vehicles and duty-type ratings; u6 Network topology, OSI model and classification of bus systems; u6 MOST and coupling of networks through gateways. Also cover electric horns and washers in u2 "Wipers, keyless entry and immobilisers". u4 and u5 go beyond AU3502.

The DeepSeek drafts were written (or started) from the older packets, so each correction thread adds the new chapters.
