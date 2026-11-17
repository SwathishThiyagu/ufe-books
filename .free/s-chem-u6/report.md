# s-chem-u6: free-model run

- Book: `books/common/s-chem/s-chem-u6.html`
- Status: ok
- Model calls so far: 23 (76,304 tokens in, 158,161 out), 6.0 minutes

## Checker

```
s-chem-u6.html: 7 chapters, 10648 words, 8 figures, 122 KB
OK
```

## For the reviewer

- chapter 1: the figure cannot be drawn: tree is too wide (7 leaves); use fewer leaves or shorter labels
- chapter 5: the figure cannot be drawn: a row of the block diagram has more than 5 boxes; use fewer nodes or set "layers"
- chapter 5: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Exam traps, bullet 4: It says the red or blue colour of a gold or CdSe nanoparticle comes from 'confined electrons'. That is right for a CdSe quantum dot, but wrong for gold. The red colour of ordinary gold nanoparticles (about 5-100 nm) comes from surface plasmon resonance, a collective oscillation of the conduction electrons, not from widening of a confined-electron energy gap. A student who repeats this in an answer loses marks.
- ch 1 [low] Section 3 and Quiz Q6: The text quotes TiO₂ as 3.0-3.2 eV but then says both oxides absorb 'below roughly 390 nm'. A 3.2 eV gap corresponds to about 388 nm, whereas a 3.0 eV gap corresponds to about 413 nm, so the single 390 nm figure does not match the range given.
- ch 1 [low] Lead paragraph: The formula is written as 'TiO2' while everywhere else in the chapter it is 'TiO₂'. Inconsistent chemical notation on a phone screen reads as a typo.
- ch 1 [low] Section 1, quantum confinement sentence: 'smaller than the natural spread of an electron' is vague; no student can attach a meaning or a number to it.
- ch 1 [low] Section 2, last paragraph, and Section 3 first paragraph: Cross-references to 6.2, 6.3, 6.4 and 'Unit 1' are typed as plain numbers, so they cannot be tapped and a student reading on a phone cannot jump to them.
- ch 2 [low] Section 1: Lithography is listed among processes that 'remove material or break it apart'. In Section 2 the chapter correctly says lithography writes a pattern into a resist and that development and etching transfer that pattern. A student can read the two statements as contradictory.
- ch 2 [low] Section 3, CVD bullet: The cross-reference 'see 6.7 for thin-film detail' is left as plain text, so on a phone it cannot be tapped like the other chapter links.
- ch 3 [low] Section 1: The sentence says confinement 'raises the lowest electron level above the highest hole level'. That only restates that the electron level is above the hole level; it does not say that the hole level moves down, so a student cannot see why the gap grows as the dot shrinks.
- ch 3 [low] Section 1, formula line: Writing 'E = hc ÷ λ ≈ Eg' with no comment invites the reading that the emitted photon energy equals the band gap exactly. In a real dot the emitted photon is slightly lower in energy than Eg (Stokes shift), and for absorption the photon energy must be at least Eg.
- ch 4 [low] Figure (stack spec for doping): The stack lists, from top to bottom, conduction band, donor level, Fermi level, acceptor level, valence band. That single ordering is right only for a compensated or near-intrinsic crystal. In a plain n-type sample the Fermi level lies near the donor level (well above midgap), and in a plain p-type sample it lies near the acceptor level (well below midgap). A student can read the picture as saying both dopant levels exist together and the Fermi level always sits between them.
- ch 4 [low] Worked example 1, step 1: Step 1 says absorption happens only if the photon energy is at least Eg, but Section 2 and the traps say silicon is an indirect-gap material, where a phonon is also needed. Taken literally, a photon of exactly 1.12 eV would give the electron no energy to spare for the required phonon, so the stated cutoff is slightly loose for silicon.
- ch 4 [low] Beyond, last line: The cross-reference '(see 6.7)' is written as plain text, while the book's convention is to link other chapters with an anchor tag.
- ch 5 [low] worked example 1, steps 1–3 (and quiz Q3): The example assumes the Meissner state without checking that the applied field is below Hc, and the number chosen (0.10 T, i.e. 7.96×10⁴ A/m) is above the zero-temperature critical field of every type-I element — Pb has Hc(0) ≈ 0.080 T and Hg ≈ 0.041 T. So no real type-I material would be superconducting at 0.10 T, and a student may carry away the wrong picture. The arithmetic itself (H = 7.96×10⁴ A/m, M = −7.96×10⁴ A/m, χ = −1) is correct.
- ch 5 [low] section 1, first paragraph: M is introduced only as 'magnetisation (A/m)'. The chapter insists that every symbol be defined, but never says that M is the magnetic moment per unit volume, which is what makes its unit A/m.
- ch 6 [low] Section 2 and Figure stack: The text says the nematic layer is sandwiched between transparent ITO electrodes (two), but the figure stack lists only one electrode, placed after the liquid-crystal layer. A student may think a single electrode is enough to apply the field.
- ch 6 [low] Section 1 and Section 2 (last sentences): Liquid-crystal composites (polymer-dispersed liquid crystals) are described twice in almost the same words, once at the end of Section 1 and again at the end of Section 2. The repetition adds length without new information.
- ch 7 [low] Section 1, first paragraph: The four stages listed (source, transport, deposition, growth) are the process steps, not the film-formation stages. The standard stages after atoms arrive are adsorption, surface diffusion, nucleation, island growth, coalescence and a continuous layer. As written, a student may write 'deposition sticks it' as the whole mechanism.
- ch 7 [low] Section 1, first paragraph: 'Deposition sticks it' is too vague for an exam answer; it hides the key word adsorb.
- ch 7 [low] Quiz Q4: The working 'V = 2.0 × 2.0×10⁻⁵ = 4.0×10⁻⁵ cm³' drops the units and does not show that the first 2.0 is the area in cm². A student copying this cannot see which factor is area and which is thickness.
- ch 7 [low] Exam traps, third trap: The trap warns against 10⁻⁹ but does not say that 10⁻⁹ is the value in metres. Students who mix up nm with m are exactly the ones this trap targets.
- ch 7 [low] Section 2, table, Cost row: 'Vacuum hardware' and 'Gas handling and safety' name only the cost item, so the point of the row is not clear.
