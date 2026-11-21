# ec-optical-u6: free-model run

- Book: `books/ece/ec-optical/ec-optical-u6.html`
- Status: ok
- Model calls so far: 28 (101,832 tokens in, 242,286 out), 6.0 minutes

## Checker

```
ec-optical-u6.html: 8 chapters, 13915 words, 9 figures, 148 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, mux/demux parameters: Adjacent-channel crosstalk is defined as 'the wanted channel power divided by the leakage from the next channel', which is a ratio greater than 1 and therefore gives a positive dB value. The same sentence then says 'more negative is better', and Q6 and the exam traps also use negative dB. The definition contradicts its own sign convention and the standard textbook definition.
- ch 1 [high] Exam traps, second bullet (duplex pair): 'Total capacity is N × B per direction; do not multiply by N again for a duplex pair' is wrong as written. Counting both directions means multiplying by 2 (a factor of two), not by N; a student will copy 'multiply by N' into the exam.
- ch 2 [high] Figure and its caption (Section 3 add-drop description): The through output of the grating is labelled "Port 2". Circulator port 2 is the arm that feeds the grating, so the figure shows the same port name twice and teaches the wrong topology: it says λ1 and λ3 leave at port 2, while the text says they 'pass straight through to the output line'. A student would conclude the through channels come back out of circulator port 2.
- ch 2 [low] Section 1, first paragraph: 'Fused birefringent coupler' is not the standard name for the device described (two fibers fused and tapered). The description itself is correct, but the name will not match textbooks or exam keys.
- ch 2 [low] Section 3, apodization paragraph: The side lobes are called 'small unwanted notches'. In a reflecting grating the side lobes are small unwanted reflection peaks just outside the main reflected band; calling them notches reverses the meaning and muddles the crosstalk explanation given later in Q6.
- ch 2 [low] Section 1, directivity definition: The symbols P3in and P1leak appear in the formula but are never defined, and the layout 'P3in' reads as P times 3in.
- ch 3 [low] Section 3 and the figure: The text says there are isolators before and after the doped fiber, but the block diagram shows only one isolator, placed after the erbium-doped fiber. A student comparing the two will think one isolator is missing.
- ch 3 [low] Quiz Q5: The question mentions a 10 dB span loss, then gives an amplifier input of −18 dBm. The answer uses −18 dBm as the amplifier input, so the 10 dB never enters the calculation. A student may read −18 dBm as the power at the start of the span and get −5 dBm.
- ch 3 [low] Quiz Q4: 'The erbium gain medium has no carrier-density noise' is not the standard reason, and it is vague. The EDFA noise figure is low because 980 nm pumping gives almost complete population inversion, so the spontaneous-emission factor is close to 1, plus low excess loss; an SOA has incomplete inversion and higher internal loss, giving a larger spontaneous-emission factor and NF of 6-8 dB.
- ch 4 [high] Section 1, the nonlinear coefficient formula: The formula γ = 2πn₂/(λ A_eff) with λ in metres and A_eff in m² gives γ in W⁻¹m⁻¹, not W⁻¹km⁻¹ as the text states. A student who puts λ = 1550 nm and A_eff = 80 µm² gets about 1.3×10⁻³, not 1.3, and concludes the typical value '1 to 3' is wrong by a factor of 1000.
- ch 4 [high] Quiz Q5 answer: The answer is broken: 'Only β₂  0 the chirps add.' The inequality signs have been lost, so the key sentence of the answer is unreadable and a student cannot tell which dispersion sign is which.
- ch 4 [high] Lead: 'it is how long-haul links send pulses for thousands of kilometres without regeneration' states that deployed long-haul systems use solitons. Installed links use dispersion management with amplifiers and coherent detection; solitons were researched and trialled, not the standard method. This also contradicts the Beyond section, which says they were 'tried' in the 1990s.
- ch 4 [low] Section 3, soliton period sentence: 'It repeats its phase over the soliton period z₀ = (π/2)L_D' is misleading. The fundamental soliton never changes shape; its phase grows steadily with distance. It is the higher-order solitons that recover their shape after one soliton period.
- ch 4 [low] Figure: The plotted broadening law √(1+(z/5)²) is the Gaussian-pulse result, but the chapter (and the worked example, with FWHM = 1.763 T₀) uses sech pulses. A student may think this exact expression applies to the soliton's sech input.
- ch 5 [low] Worked example 1 (step 4) and Quiz Q3(c): The demand is written per node ('each node must send one 10 Gb/s lightpath to each of the other five'), which is 6 × 5 = 30 directed demands, but the traffic is then summed over the 15 undirected pairs. A 10 Gb/s lightpath normally carries 10 Gb/s in each direction, so a student counting node by node writes 300 Gb/s while the answer says 150 Gb/s. The same mismatch appears in Quiz Q3.
- ch 5 [low] Section 1: 'A span is one amplified section inside a link' is only one usage. Many textbooks use span and link as synonyms (the fiber between two adjacent nodes), so the later trap 'Link, span, path and channel are not synonyms' can contradict what a student reads elsewhere. Also, the power budget in Unit 5 applies to the whole transmitter-to-receiver link, not to one span alone.
- ch 5 [low] Section 1: Saying 'some syllabi call it a wavelength path or an optical channel' collides with the chapter's own definition of a channel as one wavelength on one link, so the two terms look contradictory to a student.
- ch 5 [low] Exam traps, second bullet: 'Protection doubles both wavelengths and transponders' is stated as a general rule, but the chapter itself says 1:N uses one backup for N working paths, and on a ring with no wavelength reuse the protection route is link-disjoint, so the working wavelength can be reused there. Only the transponder count always doubles; the wavelength count doubles only for dedicated 1+1 under a separate-wavelength assignment.
- ch 6 [high] Section 3: The chapter says in BLSR/MS-SPRing that working capacity is shared. In a BLSR/MS-SPRing, the protection capacity is shared; working capacity is not shared.
- ch 6 [low] Section 2: The sentence says one column is path overhead and then says the remaining 87 columns form the SPE. This can make students think path overhead is outside the SPE, although path overhead is inside the 87-column SPE.
- ch 6 [low] Quiz Q4: The answer lists unused VC-4 capacity as part of the remaining capacity. With 63 E1s mapped into a VC-4, the VC-4 payload is occupied by the E1 mappings and their VC-12/TU overhead and stuffing; there is no unused VC-4 capacity to count.
- ch 7 [high] Worked example 1, step 3: The step claims the path works 'with a converter at B' but then performs two conversions (λ1→λ2 at B and λ2→λ3 at C) and even puts λ2 on C–D, where λ2 is not free (S_CD = {λ1, λ3}). Only node B has a converter, so this step contradicts its own answer.
- ch 7 [low] Section 2, broadcast-and-select paragraph: The roles of arm and gate are muddled: the splitter has one arm per output port, and each arm needs one gate per wavelength (or a filter plus gate) so that the wanted wavelength is chosen. As written ('a gate in each arm opens only for the wanted output'), a student cannot tell whether a gate selects an output or a wavelength, and cannot count gates for the loss budget.
- ch 7 [low] Quiz Q4: The question moves straight from '16 wavelengths per input' to a 1:16 splitter. The number of splitter arms in broadcast-and-select is set by the number of output ports (times wavelengths), not by the wavelength count, so a careful student may object to the premise even though the dB estimate is right.
- ch 8 [low] Figure caption (Section 2): The wording 'padding fills 32 cells of 53 bytes' is confusing. Padding does not fill cells; padding plus the trailer make the payload spill into a 32nd cell, and 32 cells of 53 bytes gives 1696 bytes on the link.
- ch 8 [low] Section 2, AAL5 sentence: The order given is wrong in the PDU: the 8-byte trailer is appended after the padding, not before it. 'Adds an 8-byte trailer, then pads' would place the trailer in the middle of the cell stream.
- ch 8 [low] Section 1, PDU sentence: 'a segment at transport' holds only for TCP. A UDP transport PDU is a datagram, and students meeting UDP later may think the rule is broken.
