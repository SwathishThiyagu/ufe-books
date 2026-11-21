# bm-instr-u2: free-model run

- Book: `work/bm-instr-u2/tree/books/bme/bm-instr/bm-instr-u2.html`
- Status: ok
- Model calls so far: 27 (101,576 tokens in, 221,995 out), 5.6 minutes

## Checker

```
bm-instr-u2.html: 8 chapters, 22703 words, 10 figures, 250 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, first bullet (cuff too narrow): The bladder length is given as '80 percent of its length', which reads as 80 percent of the arm's length. Standard practice sizes the bladder length against the arm circumference, not the arm length, so the student learns a wrong rule.
- ch 1 [high] Section 3, fourth bullet: Talking, a full bladder, caffeine and anxiety are all labelled 'the white-coat effect'. The white-coat effect is specifically a rise in pressure caused by the clinic setting or the observer, with normal pressures outside the clinic. The other factors raise pressure anywhere.
- ch 1 [low] Section 1, paragraph on dynamic response: 'If the natural frequency is low or the damping is wrong, the trace rings or overshoots' mixes two different faults. Ringing and overshoot come from too little damping; a natural frequency that is too low with normal damping makes the trace sluggish and blunts the peaks.
- ch 1 [low] Worked example 1, step 5: The reason given for the catheter reading being higher ('the cuff senses pressure through the arm tissue') is vague and does not name the main mechanism, peripheral amplification of the pulse wave.
- ch 1 [low] Section 2, table, phase IV: The table says some clinics call phase IV diastolic but does not say when it is used, so the student cannot tell why phase IV exists at all.
- ch 2 [high] Exam traps, first trap: It says dropping the factor 60 gives 0.083 L/min. Dropping 60 actually gives a value in L/s, so the number is 0.083 L/s, which equals 5 L/min. The unit L/min is wrong and would mislead a student.
- ch 2 [high] Section 2, paragraph on extrapolation: It says 'The area between the first-pass curve and this extrapolated line is A.' That describes the recirculation area, not the first-pass area. A is the area under the first-pass curve: the measured part up to recirculation plus the area under the extrapolated line after that.
- ch 3 [high] Section 1, first sentence: The definition 'A heart sound is a short vibration set off when a valve closes' is contradicted two sentences later, where S3 and S4 are described as sounds made by blood moving into the ventricle, not by valve closure. A student learns a definition that then fails for two of the four sounds the chapter names.
- ch 3 [low] Section 1, third paragraph: 'S3 and S4 are common in young people and are not always disease' lumps the two together. S3 is a normal finding in children and young adults, but S4 is normal mainly in children and trained athletes; in an older adult it usually points to a stiff, poorly compliant ventricle and is a sign of disease.
- ch 3 [low] Section 1, second paragraph: The claim that murmurs 'carry more high-frequency energy than normal S1 and S2' is too broad and sits badly with the same chapter's own example of a low-pitched mitral stenosis murmur that needs the bell. A student may conclude every murmur is high frequency and reach for the diaphragm every time.
- ch 3 [low] Section 3, third paragraph: 'S1 and S2 follow it by fixed delays' overstates the case. The delay from the R wave to S1 is short and fairly stable, but the R-to-S2 delay changes with heart rate, contractility and conduction, which is exactly why the delays must be measured on each trace.
- ch 4 [high] Section 2, deceleration table: The table says a late deceleration 'starts after contraction peak'. Standard definition: a late deceleration begins after the contraction has started (in the latter part of the contraction), and its lowest point (nadir) comes after the peak of the contraction. A student who writes 'starts after the peak' loses marks.
- ch 4 [low] Worked example 1: Variability is written as '±5 beats per minute'. CTG variability is quoted as an amplitude in beats per minute (normally 5 to 25), not as a plus-minus band; ±5 suggests a 10 beats-per-minute swing.
- ch 4 [low] Quiz Q2: The question asks for 'two quantities', but the answer gives one quantity (the RR interval in seconds) plus a formula. The second item is a relation, not a quantity.
- ch 4 [low] Figure, Pause limit lane: The pause limit is drawn as a bar running from 0 to 1500 ms, which looks like a duration on the time axis rather than a threshold that the third interval crosses.
- ch 5 [low] Section 1, first line: Missing article and unclear verb: 'Spirometer measures the volume...' and 'the instrument draws volume against time'. A student may read 'draws' as suction rather than plotting.
- ch 5 [low] Section 2, turbine spirometer: 'rotation gives flow, and integrated flow gives volume' is loose and can be read backwards. What is measured is how fast the vane spins (proportional to flow) and how many turns it makes (proportional to volume).
- ch 5 [low] Section 3 and Exam trap 1: 'only the FEV1/FVC ratio separates them' overstates what spirometry can do. Spirometry only suggests a restrictive pattern; true restriction needs a low TLC, which a simple spirometer cannot measure.
- ch 5 [low] Section 3, ratio cutoff: 'some laboratories use 0.75' is vague and dated. The usual modern alternative to the fixed 0.70 cutoff is the lower limit of normal (z-score) for the patient's age, sex and height, not a second fixed number.
- ch 5 [low] Quiz Q5: The answer says 'FVC and FEV1 are low' but the question gives no predicted values, so a student cannot know they are low; only the ratio can be computed.
- ch 6 [low] Lead and Section 2: The lead says 'Pressure sensors inside the alveoli and in the oesophagus', and Section 2 says 'otherwise a small catheter can reach it'. No sensor sits inside an air sac; intra-alveolar pressure is obtained indirectly from mouth pressure during an occlusion, or from a wedged catheter. A student may take the lead literally.
- ch 6 [low] Section 1, Worked example 1(a), Quiz Q3: The same number, ΔP/Q, is called 'sensitivity' in the bullets and the worked example, is defined as the resistance R in the formula box, and is written with the symbol R in the Q3 answer. Sensitivity normally means output per unit input; ΔP/Q is a calibration factor. Two names and one symbol for one quantity confuse students.
- ch 6 [low] Section 3: 'Check linearity with a calibrated syringe before a test, because a clogged mesh changes the resistance and the sensitivity.' A syringe delivers a known volume, so it checks volume accuracy and integrator drift, not the linearity of ΔP against flow. Flow linearity needs several steady reference flows.
- ch 6 [low] Exam traps, gauge pressure versus absolute pressure: The wording suggests that using absolute pressures gives a wrong transpulmonary pressure. Transpulmonary pressure is a difference, so it is unchanged as long as both pressures use the same reference; the error appears only when the two references are mixed, or when a single alveolar value is compared with a gauge value.
- ch 7 [high] Section 1, Beer–Lambert formula: The stated unit of ε is 'per mole per centimetre'. With c in moles per litre and d in centimetres, that unit makes A come out with the unit per litre, which contradicts 'A is absorbance (no unit)'. The molar absorption coefficient must carry the litre.
- ch 7 [low] Section 2, first paragraph: SpO₂ is defined as 'the share of haemoglobin binding sites that carry oxygen'. The displayed SpO₂ is functional saturation: oxygenated haemoglobin as a percentage of oxygenated plus reduced haemoglobin. Dyshaemoglobins are not counted. As written, the definition clashes with the carboxyhaemoglobin bullet later in the same section, where the reading is high while many sites carry no oxygen.
- ch 7 [low] Section 1, opening of Beer–Lambert explanation: 'A coloured substance absorbs light in proportion to how much is present and how far the light travels' suggests transmitted light falls linearly. Absorbance is proportional to c and d; the transmitted intensity falls exponentially.
- ch 8 [high] Worked example 1, step 5 (also answer line): The example computes Raw = 2.0 cm H2O per L/s and then calls it 'mildly raised', but the same sentence, and Section 3, give the normal range as 0.6 to 2.4 cm H2O per L/s. A value of 2.0 lies inside the normal range, so the comment contradicts the chapter's own numbers and would teach a student to label a normal result abnormal.
- ch 8 [low] Section 1 and Section 2 formula: Section 1 says box gas behaves adiabatically (no heat exchange) and lung gas isothermally, then says 'Boyle's law ... links pressure and volume in each gas space'. Boyle's law (PV = constant) holds only for the isothermal lung gas; for the adiabatic box gas the relation is PV^γ = constant, with γ ≈ 1.4 for air. Because of this, the exact relation between the swings carries a factor of about 1.4 (Vtg ≈ Vbox × ΔPbox/(1.4 × ΔPmouth)), so the bare ratio in the worked example is a simplification, not the full law.
