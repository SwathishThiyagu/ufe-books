# ae-avionics-u5: free-model run

- Book: `work/ae-avionics-u5/tree/books/aero/ae-avionics/ae-avionics-u5.html`
- Status: ok
- Model calls so far: 37 (146,503 tokens in, 323,072 out), 10.5 minutes

## Checker

```
ae-avionics-u5.html: 10 chapters, 28631 words, 11 figures, 294 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: tree is too wide (7 leaves); use fewer leaves or shorter labels
- chapter 10: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, ellipsoid paragraph: WGS-84 is a datum (a coordinate system with an ellipsoid, an origin and a realisation), not an ellipsoid. Calling the shape itself 'WGS-84' blurs the two.
- ch 1 [low] Section 1, ellipsoid paragraph: 'Satellite orbits and GPS coordinates are expressed on this ellipsoid' is loose: a satellite position is a point in space fixed by a frame (ECEF/ECI), not a point on the ellipsoid surface. Only the ground coordinates use the ellipsoid.
- ch 1 [low] Section 2, bearing paragraph: 'The bearing of the station from the aircraft differs from the bearing of the aircraft from the station by 180°' is exact only for magnetic or rhumb-line bearings. For true great-circle bearings the two differ by 180° plus the convergence of the meridians, which is not negligible on long legs.
- ch 1 [low] Section 3, fix-error formula annotation: σ is described as 'the 1-sigma position error along each line of position', but the error that matters is measured perpendicular to the line of position; along the line the position is unconstrained. This contradicts the sentence two paragraphs above saying uncertainty is largest along each line.
- ch 2 [low] Section 1, VOR paragraph: The sentence says a CVOR 'rotates a loop or dipole physically'. In most CVOR installations the rotating pattern is produced electrically (the antenna itself does not move), and only some older or large-aperture designs turn the antenna mechanically. A student may take 'physically' as the definition of CVOR.
- ch 2 [low] Figure (classification tree): GNSS is placed under the hyperbolic branch whose note reads 'two stations'. GNSS measures ranges (pseudoranges) to four or more satellites; it only borrows the time-difference idea through the receiver clock offset. The note can make students think two satellites give a fix.
- ch 2 [low] Quiz Q7: The explanation says the hyperbolas 'reduce to nearly parallel straight lines'. What actually happens on the baseline extension is that the gradient of the range difference becomes very small, so each line of position there is nearly parallel to the baseline and the two families cross at a shallow angle.
- ch 2 [low] Section 3, last sentence: The cross-reference 'see 5.6' is plain text, so a reader on a phone cannot jump to the satellite navigation chapter.
- ch 3 [low] Section 2 (categories): 'IIIB needs 50 m' can be read as a decision height and leaves out the CAT IIIB decision height entirely; the earlier sentences use the format 'DH ... and RVR ...', so the omission is confusing.
- ch 3 [low] Quiz Q2 answer: The answer says 'the ratio of 90 Hz to 150 Hz depth', but DDM is the difference of the two depths, not their ratio. The reason is that the difference (not a ratio) is set by the angle from beam centre.
- ch 3 [low] Quiz Q2 answer (physics): Rain is listed as a cause of signal-strength change, but at 110 MHz and 330 MHz rain attenuation is negligible; only a few GHz and above does rain matter.
- ch 3 [low] Quiz Q6 answer: 'DME gives continuous range to the threshold' is imprecise: the DME zero-range point is at the DME antenna site, which is offset from the threshold, so the reading is slant range to that site.
- ch 3 [low] Worked example 1 and Quiz Q7: The 3° path is treated as passing through the threshold at zero height, so the threshold crossing height (about 15 m / 50 ft) is ignored. The answers are the standard simplified ones but the assumption is never stated.
- ch 4 [low] Section 2, right-hand rule sentence: The rule (curl fingers from H toward T, thumb gives precession direction) is correct, but the trailing clause "in the sense of the spin" is vague and can be read as saying precession runs the same way as the rotor spin. Precession is perpendicular to H and simply reverses when the spin reverses.
- ch 4 [low] Section 3, sentence on nutation and precession: "Some syllabi call nutation the wobble and precession the topple" is not a standard usage. In gyrocompass work 'topple' means the rise and fall of the spin axis about the horizontal and 'drift' means the azimuthal motion; neither is a name for precession. The sentence risks teaching wrong vocabulary.
- ch 4 [low] Section 1, caging sentence: "Caging locks the rotor" can be read as stopping the rotor. Caging locks the gimbals so the rotor axis is held fixed to the case; the rotor keeps spinning.
- ch 4 [low] Section 2, formula box for Ω: Ω = T/H is the steady precession rate only when the torque is perpendicular to the spin axis. The condition is not stated, so a student may apply it to any torque.
- ch 4 [low] Exam traps, third trap: "Ω comes out too small by a factor of 2π/60" is easy to read backwards. With ω in rpm the wrong answer is correct answer × (2π/60), i.e. about 9.55 times too small; the phrase names a number below 1 as the factor.
- ch 4 [low] Figure, node 'h': The node note gives H = Iω = 50.3 with no unit, while the caption and text use kg·m²/s. Numbers should carry units everywhere.
- ch 5 [high] Worked example 1, steps 6 and 7 (part b) and the answer line: The example contradicts the chapter's own error model. A constant gyro bias ε makes the tilt grow linearly, θ(t) = εt, so the false acceleration gεt is not constant over the hour. The example uses the final tilt as if it acted for the whole hour: velocity error = (gεt)·t = 6.164 m/s and position error = ½(gεt)t² = 11.1 km. The correct values from Δv = ½gεt² and Δp = gεt³/6 (the formula printed earlier in the chapter and used correctly in quiz Q5) are 3.08 m/s and about 3.7 km. As written, part (b) is 2× too big in velocity and 3× too big in position, and it disagrees with Q5's method.
- ch 5 [low] Section 1 table: The accelerometer bias column uses µg (micro-g) without defining it, while mg is defined just above. Students may read it as micrograms.
- ch 5 [low] Section 3, after the error formulas: The sentence 'Schuler tuning keeps these errors oscillatory rather than runaway' is loose. With the Schuler loop closed, the accelerometer-bias position error becomes a bounded 84.4 min oscillation, but the gyro-bias position error still grows roughly linearly with time (a ramp with an 84.4 min ripple); only the tilt stays bounded.
- ch 5 [low] Quiz Q7 answer: The symbols Ω and φ are used without definition.
- ch 6 [low] Worked example 1, step 2: The line '= 2.0200 × 10⁷ ÷ 2.99792458 × 10⁸' has no brackets around the denominator. Read left to right it means (2.02 × 10⁷ ÷ 2.99792458) × 10⁸, a huge wrong number, not 0.06738 s.
- ch 6 [low] Worked example 1, step 5: 'The reading is too late by 3 µs' is confusing: a fast clock reads ahead of true time, so it is not the reading that is late but the clock that is advanced. The conclusion (pseudorange too long) is right, but the sentence can be misread.
- ch 6 [low] Section 1, list of orbital elements: The sixth element is given as true anomaly ν, but the broadcast ephemeris sends mean anomaly at the reference epoch (with small harmonic corrections). A student who looks for ν in the decoded message will not find it.
- ch 6 [low] Section 4, other constellations: 'Galileo serves Europe, BeiDou serves China' makes both sound regional like NavIC. Galileo and BeiDou are global systems; only NavIC is regional.
- ch 6 [low] Section 1, orbital period formula: Calling μ = 3.986 × 10¹⁴ m³/s² 'the Earth's gravitational constant' blurs it with G, the universal gravitational constant (6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻²).
- ch 7 [low] Section 3: The troposphere is described as extending 'from the surface to about 8–12 km'. That is a mid-latitude figure; over India the tropopause sits near 16–17 km, so a student may think the model stops well below the real path.
- ch 7 [low] Section 1: 'Four corrections are applied before the fix: satellite clock, orbit, ionosphere and troposphere' reads as if orbit error were a range correction added to the pseudorange. Orbit (ephemeris) data are used to compute the satellite position; only clock, ionosphere and troposphere are subtracted from the measured range.
- ch 7 [low] Section 1 and Section 2: Symbols are typed with underscores and carets (a_f0, a_f1, d_I, d_T, d_z, δt_s, 10^16), which a phone reader will misread.
- ch 8 [low] Figure (Predict–update loop, edges): The caption says the dashed return pushes bias corrections 'back into the sensors themselves', but the dashed edge labelled 'reset sensors' runs from Update to the 'INS mechanization' block, not to the IMU. A student following the arrow will think the feedback acts on the integration step, not on the sensors.
- ch 8 [low] Worked example 1, step 5 (also quiz Q5): σ appears for the first time as 'σ = √20 ≈ 4.47 m' with no definition; the chapter defines variance but never names the standard deviation.
- ch 9 [high] Section 3, TCAS/ACAS paragraph: It says the resolution advisory 'drives the autopilot'. In TCAS II the RA is a command shown to the crew on the flight director and vertical-speed indicator, and the pilot must fly it; the autopilot is normally disengaged during an RA and is never commanded by TCAS.
- ch 9 [low] Section 3, ADS-B sentence: One 112-bit extended squitter does not carry position, altitude, velocity and identity together. Position with altitude, velocity, and identity (callsign) travel in separate message types, sent in turn.
- ch 9 [low] Section 3, ADS-B In sentence: FIS-B weather is broadcast on the 978 MHz UAT data link, not on 1090 MHz extended squitter, so 'ADS-B In receives ... weather (FIS-B)' is too general.
- ch 9 [low] Worked example 1, step 4: The example uses 1030 MHz as the transmit frequency of a primary pulse radar, which is the SSR ground-interrogation frequency the chapter warns about. A student may read it as a rule that primary radars transmit at 1030 MHz.
- ch 10 [high] Quiz Q6 (and its answer): The answer teaches that the reactive modes 'may still fire' on a mast, with the radio-altimeter return changing once the mast is below the aircraft. That is wrong in the way that matters. The radio altimeter measures the surface directly below over a wide beam; a thin mast is not a reliable reflector and does not raise a clearance or sink-rate alert. A level aircraft flying into an unmapped mast gets no GPWS warning at all. The answer contradicts the chapter's own database bullet ('many wires and unlit obstacles are never mapped') and gives students the false comfort that reactive modes are a backstop for obstacles.
