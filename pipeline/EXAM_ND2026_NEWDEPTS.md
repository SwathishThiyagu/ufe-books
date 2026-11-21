# Nov/Dec 2026 exam subjects: Civil, Chemical, Aero, Biomedical (8 subjects, 2 per department)

Checked 21 Nov 2026. Owner approved the 8 picks on 21 Nov 2026.

Timetables: the R2025 (revised 27 Oct 2026) and R2021 Nov/Dec 2026 UG timetables, read from mirror copies of the official PDFs (the official exam site was not reachable from the workspace):
- R2025 revised: `files.padeepz.com/documents/UG/TT/ND 26 Revised/TT ND 26 aucr2025_rev.pdf` (header "REVISED ON 27-OCT-2026"; pages 1-44 read).
- R2021: `files.padeepz.com/documents/Notification/TT ND 26/Padeepz App aucr2021.pdf` and a second copy on kalvinesan.com (same header and dates; only pages 1-26 of 158 could be read: Aeronautical, Automobile, Civil, CSE, EEE).

Syllabi: the official R2025 (revised) and R2021 curriculum PDFs in the owner's 01_Syllabus_PDFs folder (AU_R2025rev_CIVIL/CHEM/AERO/BME, AU_R2021_CIVIL/CHEM/AERO/BME).

All exams FN = 10.00 am to 1.00 pm.

## Exam order

| Date | Exam course | Subject id | Dept, year | Status of the date |
|---|---|---|---|---|
| 20 Nov FN (past) | CH25301 Chemical Engineering Thermodynamics I | ch-thermo | Chemical 2nd | read from the timetable (B.Tech Chemical block) |
| 24 Nov FN | CE3501 Design of Reinforced Concrete Structural Elements | ce-rcc | Civil 3rd | read from the timetable (B.E. Civil sem 5) |
| 25 Nov FN | AE25301 Aircraft Electrical and Electronics Systems | ae-avionics | Aero 2nd | read from the timetable (B.E. Aeronautical) |
| 26 Nov FN | AE3501 Aircraft Structures II | ae-struct | Aero 3rd | read from the timetable (B.E. Aeronautical sem 5) |
| 27 Nov FN | CE25C03 Surveying and Geomatics | ce-survey | Civil 2nd | read from the timetable (B.E. Civil) |
| 27 Nov FN | BM25C05 Sensors and Measurements | ei-sensor | Biomedical 2nd | read from the timetable (B.E. Biomedical) |
| not found | CH3551 Mass Transfer II | ch-mass | Chemical 3rd | Chemical block is past the readable pages |
| not found | BM3591 Diagnostic and Therapeutic Equipment | bm-instr | Biomedical 3rd | Biomedical block is past the readable pages |

Dates are read by column position from a text extraction, so spot-check against the official PDF before quoting a date to students.

## Why these picks

- Civil 2nd: R2025 semester 3 has AG25C01 Engineering Geology (18 Nov), CE25301 Strength of Materials I (20 Nov), CE25C03 Surveying and Geomatics (27 Nov) and CE25C02 Fluid Mechanics and Machinery (30 Nov). ce-survey matches CE25C03.
- Civil 3rd: R2021 semester 5 has CE3503 Foundation Engineering (19 Nov), CE3502 Structural Analysis I (21 Nov) and CE3501 Design of RC Structural Elements (24 Nov). ce-rcc is built from CE3501 itself and its exam is still ahead.
- Chemical 2nd: CH25301 matches ch-thermo; it was already over when checked. The other semester 3 courses (CH25C02 Mechanical Operations 18 Nov, CH25C03 Fluid Mechanics 2 Dec, CH25302, CH25303) have no matching candidate packet.
- Chemical 3rd: R2021 semester 5 has CH3501 Thermodynamics II and CH3551 Mass Transfer II; ch-mass matches CH3551 (its units 3-6).
- Aero 2nd: R2025 semester 3 (Aeronautical) has no course matching ae-intro, ae-aero, ae-struct, ae-prop or ae-flight (those courses sit in semesters 2 and 4). AE25301 Aircraft Electrical and Electronics Systems (25 Nov) is closest to ae-avionics (outside the candidate list; owner approved).
- Aero 3rd: R2021 semester 5 has AE3502 Aerodynamics II (21 Nov) and AE3501 Aircraft Structures II (26 Nov). ae-struct matches AE3501 (its units 4-6, plus wing/fuselage/tail stress analysis from unit 1).
- Biomedical 2nd: R2025 semester 3 has BM25C03 Electric Circuit Analysis (18 Nov), BM25C04 Electronic Devices and Circuits (20 Nov), BM25C06 Healthcare Data Analytics (25 Nov) and BM25C05 Sensors and Measurements (27 Nov). None of bm-anat, bm-signal, bm-instr or bm-medphys is a semester 3 course; ei-sensor (Sensors and Transducers) fits BM25C05 (outside the candidate list; owner approved). Deliver it under Biomedical; the book stays at books/eie/ei-sensor/.
- Biomedical 3rd: R2021 semester 5 has BM3551 Embedded Systems and IoMT and BM3591 Diagnostic and Therapeutic Equipment; bm-instr matches BM3591 (the packet was built from the R2025 course BM25C08).

## Packet changes (exam course added to `where`, missing topics added as subtopics)

Every packet of the eight subjects now has `where` entries for the exam course with the official topic lists, and `course_used.anna` names it first. Subtopics added (unis = anna):

- ce-rcc (CE3501): none needed. Cover singly reinforced beam design by the working stress method in u1, eccentrically loaded pad and sloped footings and the two-column combined footing in u5, circular columns in u5. u6 (prestressed concrete), retaining walls, water tanks and yield lines are not in CE3501.
- ae-avionics (AE25301; the packet was built from AS3302 Flight Systems): u2 Landing gear and flap control, stall warning and protection; u2 Ice and rain protection systems; u3 Voltage regulators; u3 Wires, cables and circuit protection; u3 Bus systems (split, parallel, split-parallel), switches and relays; u3 Power system architecture of the A320 and B787; u3 Engine indicators and fuel quantity indication; u4 Aircraft transducers; u4 Avionics electronics (diodes, transistors, op-amps, ADC/DAC, microcontrollers); u5 Terrain awareness and ground proximity warning. Also cover lithium batteries and the APU in u3. u1 (flight controls), u6 (guidance) and most of u4-u5 go beyond AE25301.
- ae-struct (AE3501; the packet was built from AE25C02 and Structures I/II): u1 Stress analysis of fuselage and tail unit; u5 Torsion of thin-walled open sections; u6 Plate buckling under shear and combined loading. Also cover the k method and principal axis method in u4. u2 and u3 (energy methods, columns, failure theories) are Structures I.
- ce-survey (CE25C03): none needed (control surveying, coordinate computation and bathymetry are already subtopics). u6 (remote sensing) and u7 (GIS), compass and plane table are not in CE25C03.
- ei-sensor (BM25C05; the packet was built from EI25C02 Transducers Engineering): u2 Thermocouples; u4 Phototube, PMT and scintillation counter; u4 Photodiodes, phototransistors, photovoltaic and photoconductive cells, spectrophotometric uses; u5 Biosensor classes, ISFET, IMFET and glucose sensors; u6 DC and AC bridges; u6 Filters, pre-amplifiers, differential and isolation amplifiers; u6 Display instruments (DVM, multimeter, CRO/CRT, DSO, spectrum analyser). Also cover biomedical applications of strain gauges, RTDs, thermistors and piezo ultrasound transducers. Actuators (u6) and MEMS fabrication (u5) go beyond BM25C05.
- ch-mass (CH3551): u3 Multicomponent absorption and absorption with chemical reaction; u5 Pulsed, centrifugal and supercritical extraction; u5 Leaching by percolation, moving bed and the Shanks system with multistage stage calculations; u6 Membrane separations (reverse osmosis, electrodialysis, ultrafiltration). u1, u2 (diffusion, coefficients) and u7 (humidification, drying) are Mass Transfer I; crystallization (u6) is not in CH3551.
- bm-instr (BM3591; the packet was built from BM25C08): u1 Heart rate monitor, Holter monitor and ECG troubleshooting; u1 Multichannel EEG, epilepsy, evoked potentials and MEG; u1 EEG and EMG biofeedback; u1 Biomechanical measurement (pedobarograph, gait, limb position); u2 Whole-body plethysmograph, residual volume and airway resistance; u5 Defibrillator protection circuit and cardiac ablation catheter; u6 Polygraph, BSR and GSR; u6 Ophthalmic instruments (tonometers, slit lamp, auto refractometer). u3 (clinical lab) and u4 (biosensors) are not in BM3591.
- ch-thermo (CH25301): u3 Entropy from a microscopic point of view. Also cover compression, expansion and duct flow of compressible fluids in u1 and the steam power plant in u3. u5-u7 (solutions, phase and reaction equilibria) are Thermodynamics II.

## Thumbnails

Not made for these subjects (owner has not chosen the department look). Each subject folder gets an empty `thumbnail\`; the upload sheet says "pending: department look not chosen"; the hook for each lesson goes into thumbs.json so the thumbnail step can run later.
