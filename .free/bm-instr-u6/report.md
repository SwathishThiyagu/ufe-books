# bm-instr-u6: free-model run

- Book: `books/bme/bm-instr/bm-instr-u6.html`
- Status: ok
- Model calls so far: 22 (73,890 tokens in, 152,013 out), 5.1 minutes

## Checker

```
bm-instr-u6.html: 8 chapters, 14399 words, 9 figures, 155 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1, steps 1–4 and quiz Q3: The powers of ten have lost their superscript markup: the text shows '20 log10', 'p / p0 = 103 = 1000' and '10(40/20) = 100'. Read literally, 103 = 1000 and 10(40/20) = 100 are false arithmetic, and a student copying the steps will write the wrong working.
- ch 1 [low] Section 2, Hughson-Westlake steps: The list starts at 30 dB HL but never says what to do if that first tone is not heard, so a student following the steps has no next move and cannot reach threshold for a patient with a moderate loss.
- ch 1 [low] Section 1 (reference pressure) and Section 3 (calibration): The chapter says flatly that 0 dB HL at 1 kHz is a pressure of 20 µPa, then in Section 3 says the coupler sets a reference equivalent threshold sound pressure level for each earphone model. Both cannot hold at once: 20 µPa (0 dB SPL) is the 1 kHz reference for insert earphones, but for a supra-aural earphone such as the TDH-39 the 1 kHz reference is roughly 7 dB SPL, about 45 µPa.
- ch 1 [low] Section 3, first paragraph: 'Some syllabi call this speech reception threshold testing' repeats the name already defined and tells the student nothing. The alternative name in common use is speech recognition threshold.
- ch 1 [low] Figure (audiogram plot): The plot uses a linear frequency axis from 125 Hz to 8000 Hz and puts 0 dB HL at the bottom with larger numbers upward. Clinical audiograms use octave (logarithmic) frequency spacing and plot hearing level with 0 at the top and increasing loss downward, so the shape a student reads here does not match the audiogram printed in a clinic report.
- ch 1 [low] Section 1, patient data sentence: 'The patient hears 20 dB HL at 250 Hz' reads as an observation rather than a threshold, which is the point of the whole paragraph.
- ch 2 [low] Section 2, total internal reflection sentence: "A ray that strikes the core-cladding boundary steeper than the critical angle is reflected back inside" is ambiguous, because θc is defined from the normal to the wall but "steeper" suggests an angle measured from the wall. A student can read it backwards.
- ch 2 [low] Worked example 1, step 5: The answer says two points closer than one core diameter merge. Resolution is set by the centre-to-centre spacing of the fibres, that is core plus cladding, not the bare core diameter. This also contradicts exam trap 3, which states the spacing correctly.
- ch 2 [low] Section 1, rod-lens description: "Air gaps between the rods keep the lens power high, so the tube stays short" gives the wrong cause. The strong refraction comes from the curved glass-air surfaces; the long glass rods help because they need fewer surfaces, so less light is lost and the relay is compact.
- ch 2 [low] Exam traps, bullet 2 (lamp at the tip): "The lamp stays outside the body" is stated as a general rule, but the swallowed capsule described in the same chapter carries its own tiny LEDs and battery at the tip. A student will find the two statements inconsistent.
- ch 3 [high] Section 2: Filtration, collimation and the cone: "Total filtration is usually about 2.5 mm aluminium" is wrong for the 60–70 kVp range given in Section 1. Standard codes require a minimum total filtration of 1.5 mm Al equivalent for dental units operating at or below 70 kVp; 2.5 mm Al applies to units above 70 kVp. A student could carry the wrong minimum into an exam or a QA question.
- ch 4 [low] Worked example 1, part (c) and step 5: Part (c) gives the catheter path as 1 kΩ, but Section 1 states that an internal path from a catheter is a few hundred ohms (300 Ω to 500 Ω). A student meets two different values for the same path in one chapter.
- ch 4 [low] Section 3, third paragraph: "The common design target for patient-connected equipment is 10 µA of leakage current" is too broad. In IEC 60601-1 the 10 µA patient-leakage limit applies to Type CF (intracardiac) applied parts; Type BF and Type B parts are allowed 100 µA in normal condition.
- ch 4 [low] Exam traps, second bullet: "About a thousand times smaller" does not match "tens of microamps". At 20 µA the ratio to 100 mA is 5000, not 1000; only 100 µA gives a ratio of 1000, and 100 µA is not "tens of microamps".
- ch 5 [high] Section 2, formula and limits block: The symbol I<sub>earth</sub> is defined as 'enclosure or earth leakage' with a single 5 mA limit. These are two different measurements with very different limits. Earth leakage (current in the protective earth conductor) is ≤ 5 mA in normal condition, but enclosure leakage (case to earth through a person) is ≤ 100 µA in normal condition and ≤ 500 µA in single fault. A student who learns 5 mA as the enclosure limit will pass an unsafe device.
- ch 5 [high] Exam traps, trap 4: The trap repeats the same conflation: '5 mA is an earth or enclosure limit'. Enclosure leakage is a 100 µA limit, not 5 mA.
- ch 5 [high] Quiz Q4: The answer gives the wrong fault. In the single-fault test the tester deliberately opens the protective earth, so a rise in leakage then is the device's own single-fault leakage (insulation, EMI-filter capacitors, mains-to-patient capacitance) exceeding the single-fault limit. A broken earth wire is a different fault that the earth-continuity test would already have caught.
- ch 5 [high] Figure caption, Section 3: The caption says to measure '... insulation resistance and leakage, and only then run the device'. Leakage current cannot be measured with the device off; the body of the chapter correctly says 'run the device and measure enclosure and patient leakage'. The two contradict each other and a student will think leakage is measured unpowered.
- ch 5 [low] Quiz Q1: Q1 asks for 'the four safety tests', but the chapter's own procedure has six steps (visual, earth continuity, insulation resistance, leakage, single-fault leakage, functional test), and the answer silently adds the functional test to the four.
- ch 5 [low] Section 1, isolation transformer paragraph: 'breaks the earth path from the mains neutral to the device' is muddled. The transformer does not break the earth wire; it removes the earth reference of the secondary, so touching one live conductor does not complete a circuit through earth.
- ch 6 [high] Figure spec and figure caption (Section 2): The figure and caption send every invasive device to class C or D ('enters body → class C or D', invasive branch edges 'transient use → Class C'). This contradicts the chapter's own worked example step 2 and quiz Q3, where an invasive, transiently used device (syringe, single-use scalpel) is class B. A student who follows the figure will answer the exam question wrongly.
- ch 6 [high] Section 2, paragraph 1: The sentence 'Class A and B licences come from the State Licensing Authority. Class C and D licences come from the Central Licensing Authority' follows a sentence about manufacture, import, sale and distribution, so it reads as if a class A or B imported device can be licensed by the State. In fact that split is for manufacturing licences only; every import licence, for any class, is issued by the Central Licensing Authority (CDSCO).
- ch 6 [low] Section 2, paragraph 3 (US description): A 510(k) shows substantial equivalence to a device 'already on the market', which is loose: the comparison device (predicate) must be legally marketed in the United States, not merely on some market.
- ch 7 [high] Section 2, electrode placement sentence: The text says palm or finger electrodes are used 'with a neutral reference'. Skin resistance and conductance are measured between two active sites (for example thenar and hypothenar of the palm, or two fingers); there is no neutral reference in the measuring path. A student will picture a unipolar recording against a quiet site, which is not how EDA is recorded.
- ch 7 [low] Worked example 1, steps 1 to 3, and Quiz Q3 answer: The power of ten is written as plain text '10−6' and the basal resistance as 'RBSR'. On a phone screen '10−6' reads as 'ten minus six', and 'RBSR' reads as one symbol.
- ch 7 [low] Section 2, 'keep the current small and use a dry, clean contact': 'Dry contact' is misleading for a constant-current resistance measurement. Bare dry metal on skin polarises under the small DC current, so the voltage drifts and BSR wanders; standard practice is clean skin with Ag/AgCl electrodes and a thin layer of isotonic (about 0.05 M NaCl) paste or gel.
- ch 8 [low] Q6 (quiz): The answer 'Axis 180° gives the meridian of the cylinder' is shorthand that students often misread. In minus-cylinder form, 180° is the meridian in which the cylinder has no power; the -0.75 D cylinder acts along 90°. As written, a student may think the cylinder power acts at 180°.
- ch 8 [low] Section 3, definition of refraction: 'Refraction is the lens power that corrects a focus error' mixes the measurement with the prescription. In clinical use, refraction is the determination of the eye's refractive state; the correcting power is written as the prescription.
- ch 8 [low] Section 3, acuity sentence: 'A person can have 6/6 acuity with glasses and still need a strong prescription' is easily misread as saying the person needs a stronger prescription than the glasses they wear.
- ch 8 [low] Lead: 'in every eye clinic' overstates the claim; small or basic clinics may not have all three instruments.
