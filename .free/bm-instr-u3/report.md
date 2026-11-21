# bm-instr-u3: free-model run

- Book: `books/bme/bm-instr/bm-instr-u3.html`
- Status: ok
- Model calls so far: 26 (93,659 tokens in, 196,038 out), 6.4 minutes

## Checker

```
bm-instr-u3.html: 8 chapters, 12357 words, 9 figures, 141 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Exam traps, third bullet (mixing up absorbance and transmittance): The trap says doubling concentration 'halves T'. That is only true when the starting transmittance happens to be 0.50. In general, if A doubles then T is squared, not halved: T_new = 10^(−2A) = (T_old)². For example, A going from 0.10 to 0.20 takes T from 0.79 to 0.63, not to 0.40. A student who memorises 'doubling c halves T' will get numerical questions wrong.
- ch 1 [low] Exam traps, fourth bullet (glass cuvette for UV): The reason given is incomplete and can mislead. If the blank is also in a glass cuvette, the glass absorption is cancelled by blanking (A = 0 is set with glass in the beam); the real trouble is that almost no UV reaches the detector, so noise and stray light make the reading unreliable. Absorbance reads falsely high only when the sample cell is glass and the blank is quartz.
- ch 1 [low] Quiz Q8 answer: The last clause is muddled: 'each factor of 3 in concentration multiplies the old transmittance by 10^(−A_old) again' mixes two symbols for the same quantity and reads as if the concentration were tripled several times. It is also unclearly worded for a second-language reader.
- ch 2 [low] Section 2, first paragraph: The single range 1700–2000 °C is low for an air–acetylene flame, which is usually quoted near 2200–2300 °C; that range fits air–LPG better.
- ch 2 [low] Section 3, internal standard paragraph, and Quiz Q5: The internal-standard ratio is described only as sodium-to-lithium, so a student can conclude the lithium standard helps only sodium measurements, while the chapter also measures potassium.
- ch 2 [low] Figure, node 's' note: The note says the sample is diluted 1:50 in water, but Section 3 says an internal lithium standard is added to every sample, which in practice means the diluent contains lithium.
- ch 2 [low] Section 2 and Exam traps: Potassium is read at 766 nm, which is in the near-infrared, but the chapter never says the photodetector must respond at that wavelength; a student may assume any detector used for the yellow sodium line also suits potassium.
- ch 3 [low] Lead: The lead says the three measured variables 'set the acid–base state', but pO₂ does not take part in acid–base balance; it reports oxygenation. A student may think a low pO₂ makes blood acidic.
- ch 3 [low] Section 3 and Exam trap 2: The chamber is held at 37 °C and the sample warms to that temperature inside it, so a cold sample measured there does not give a 'falsely low pCO₂ and falsely high pH'. The lower pCO₂ and higher pH belong to a sample measured below 37 °C (CO₂ solubility rises, electrode slope changes). As written, the stated cause and the stated effect do not match the setup.
- ch 3 [low] Beyond: The sentence says co-oximetry measures 'haemoglobin species, electrolytes and lactate'. Co-oximetry measures haemoglobin species only; electrolytes and lactate come from separate ion-selective and amperometric sensors on the cartridge.
- ch 4 [low] Section 1, Section 2 formula list, worked example 1, exam traps, quiz Q1 and Q4 answers: Powers of ten are printed as plain digits in most places: "4.5–5.5 × 1012", "4–11 × 109", "2.0 × 106", "10-6 L". Read literally these are wrong numbers (1012 instead of 10¹²), and a student skimming on a phone will misread them. Only the Section 1 formula uses a superscript tag.
- ch 4 [low] Worked example 1, steps 2–3: The stated formula uses V in µL, but the example plugs in V = 0.2 mL. The arithmetic is right, but the mismatch with the formula invites unit mistakes in the exam.
- ch 4 [low] Section 1, dilution step and the formula that follows: "D is often 1:200" can be read as D = 1/200, yet the formula says multiply by D. A student who substitutes 0.005 gets a count 40,000 times too small.
- ch 4 [low] Section 2, threshold paragraph: Listing platelet, red cell and white cell pulses in one pass of the same unlysed sample suggests all three are counted together. In whole blood white cells are about one per thousand red cells, so the white count is taken on a separate aliquot after the red cells are lysed.
- ch 4 [low] Section 3, last paragraph: The cross-reference "as in 3.1" is plain text, so it does not link to the earlier chapter the way other cross-references do.
- ch 5 [high] Section 3, bichromatic paragraph (and Quiz Q5): The sentence says lipaemia, haemolysis and a cuvette scratch 'add roughly the same absorbance at both wavelengths'. That is not true of haemolysis. Free haemoglobin absorbs strongly near 400–430 nm and much less at 600 nm, so its added absorbance at a main wavelength like 505 nm and a reference like 600 nm is very different and is not cancelled by the subtraction. Only turbidity (lipaemia) and cuvette/blank differences behave roughly the same at both wavelengths.
- ch 5 [low] Section 3, calibration formula: The formula uses A(sample) and A(std) as if they were the raw readings, but a single-point ratio is only valid when both absorbances have had the reagent blank subtracted. A student who plugs in raw readings gets a biased concentration.
- ch 5 [low] Section 1, liquid-level sensing: The text says sensing is 'capacitive or resistive' but then explains only the capacitive case (probe tip as one plate of a capacitor). The resistive case is left unexplained, so the two ideas get mixed.
- ch 5 [low] Section 1 and the figure: The order of the optical parts is muddled. The text says the filter wheel selects the wavelength and then the photodiode reads light through the cuvette, and the figure labels the detector block 'filter wheel'. In a filter photometer the light passes the filter before the cuvette; the photodetector sits after the cuvette.
- ch 5 [low] Section 2, throughput sentence: '600 tests per hour means 6 s per test' can be read as the time one test takes from pipetting to result. In a random-access analyser many cuvettes are processed in parallel and incubation takes minutes, so 6 s is only the average interval at which results come out.
- ch 5 [low] Exam traps, third bullet: A reagent blank does not correct reagent carryover. A blank corrects the absorbance of the reagent itself; carryover is corrected by adequate washing and by carryover studies with a high-reagent sample followed by a blank.
- ch 5 [low] Section 3, kinetic assay sentence: 'Enzyme tests are read as a rate and never as a final absorbance' is too absolute; some enzyme methods are fixed-time or end-point colorimetric assays that are read once after a set incubation.
- ch 6 [low] Figure: The figure shows a UV detector at 280 nm in a generic chromatography diagram. GC uses a flame ionisation detector, and UV detection is specific to HPLC/protein work, so a student may think every chromatograph uses a UV detector.
- ch 6 [low] Section 1, retention time: Retention time is defined as the time from injection to the peak maximum. Injection applies to column methods (GC and HPLC). TLC and paper chromatography use Rf values, so the definition can mislead a student applying it to a plate or sheet.
- ch 6 [low] Section 2, SDS-PAGE: 'SDS-PAGE binds SDS' is awkward and technically imprecise: SDS-PAGE is the technique, and SDS is the detergent that binds to proteins.
- ch 6 [low] Section 2, formula: The friction factor is written as 'N per m/s'. A student may read this as (N/m)/s rather than N·s/m.
- ch 7 [low] Lead: "Denser particles move outward" does not say denser than what. A student can read it as denser particles in general and miss the case of particles lighter than the liquid, which move inward.
- ch 7 [low] Section 1, after the RCF formula: "so one tube gives different forces on different rotors" is unclear: the same tube sits at a different radius in different rotors, and that is why the force changes.
- ch 7 [low] Section 1, Stokes' law formula: The symbols d, Δρ and η are named but their units are not given. The formula is only valid in consistent units, so a student may put d in µm or Δρ in g/cm³ and get a wrong answer.
- ch 7 [low] Section 2, serum protocol: The chapter has just shown that rpm alone does not fix the force, yet the protocol is given only in rpm. On a rotor of different radius this range gives a different force.
- ch 8 [high] Quiz Q6: The answer says the tube is 'blind for the whole second' while also recording about 5000 counts in that second. A dead-time fraction of 1.0 does not mean zero output; it means the observed rate has reached its ceiling of 1/τ = 1/(200 µs) = 5000 counts per second, so the tube is dead between pulses but still emits the maximum possible number of pulses. As written, a student will read the two statements as contradicting each other.
- ch 8 [low] Exam traps, bullet 2: 'only the scintillation counter does that' overstates the case: proportional counters and semiconductor detectors (for example cadmium zinc telluride, mentioned in the Beyond section) also give pulse heights that follow the radiation energy.
- ch 8 [low] Section 1, first paragraph: Absorbed dose is defined as energy deposited per kilogram of tissue. The gray is defined for any material, not only tissue; radiation dosimetry applies it to tissue, but the definition should not be tied to tissue.
- ch 8 [low] Quiz Q1: The answer defines the sievert as 'equivalent dose', which just repeats the name of the quantity instead of defining the unit.
