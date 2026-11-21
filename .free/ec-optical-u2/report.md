# ec-optical-u2: free-model run

- Book: `books/ece/ec-optical/ec-optical-u2.html`
- Status: ok
- Model calls so far: 32 (128,210 tokens in, 274,419 out), 7.0 minutes

## Checker

```
ec-optical-u2.html: 9 chapters, 14886 words, 10 figures, 162 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1 (also quiz Q2 and Q3 answers): The inverse formula is written as Pout = Pin × 10−A/10, with no exponent. Read literally this means 10 minus A/10, which is wrong and will mislead a student calculating output power.
- ch 1 [low] Exam traps, trap 4: The sentence 'Pout in gives log₁₀(Pin/Pout) > 0' is garbled and has no clear subject, so the point about the sign of a loss is lost.
- ch 1 [low] Section 3 table: The text says three windows matter, but the table has four rows: the water peak at 1380 nm is a loss feature, not a usable window.
- ch 1 [low] Section 1, anchor points: 'A gain of 3 dB doubles power, which is why a 3 dB coupler splits power equally' can read as if a 3 dB coupler amplifies; in a coupler the 3 dB is a loss at each output port.
- ch 2 [high] Worked example 1, step 3: The decay is written as '10−10/10 = 0.1'. With no exponent marked, this reads as 10 − 10/10 = 9, not 0.1. The value 0.1 is right, but the line as printed is a wrong step and a student copying it will get 9.
- ch 2 [high] Quiz Q4 answer: 'Ratio = 10−2.4 = 0.00398' is wrong as written: 10 − 2.4 = 7.6, and the printed 0.00398 only comes from 10^(−2.4). The final 99.6 % is correct, but the shown equation is not.
- ch 2 [low] Worked example 1, step 1: The step re-derives 0.4 dB/km from 0.75 − 0.35 even though 0.4 dB/km is already given as the OH⁻ excess, and calls the result 'absorption coefficient'. Total loss minus Rayleigh is all non-Rayleigh loss (OH⁻ plus the silica IR tail), not the OH⁻ excess alone, and it is a dB/km attenuation figure, not an absorption coefficient α.
- ch 2 [low] Quiz Q5 answer: Listing dispersion vaguely as the 'cost' of moving to 1310 nm can mislead: in standard single-mode fiber 1310 nm is close to the zero-dispersion wavelength, so dispersion there is usually lower, not worse.
- ch 3 [low] Section 1: 'No energy goes into heat' is too flat. The scattering event itself is elastic, but the light that leaves the core is eventually absorbed in the cladding, coating or jacket and does end up as heat. A student can read this sentence as 'scattering causes no loss at all', which contradicts the rest of the section.
- ch 3 [low] Section 2: 'Better drawing cannot remove it because it comes from frozen disorder' conflicts with the formula given just above, where αR is proportional to the fictive temperature Tf. Tf depends on cooling rate and drawing conditions, so processing does change the Rayleigh term; it can be reduced, not removed.
- ch 3 [low] Figure: The aria text and Section 3 call the Mie curve 'nearly flat', but the plotted Mie term (0.05/λ²) falls by a factor of four between 0.8 µm and 1.6 µm. It only looks flat because the y-axis is scaled to 3 dB/km.
- ch 4 [low] Section 1, shop-floor check paragraph: Mandrel sizes are normally quoted as diameter, so a 10 mm mandrel means a 5 mm bend radius. The next sentence says a 5 mm radius can already cost noticeable loss, which contradicts the harmless 10 mm check. A student cannot tell whether 10 mm is the diameter or the radius.
- ch 4 [low] Section 3, first paragraph: The sentence 'It is not a loss per kilometre' contradicts the comparison table in Section 2, which gives micro bending in dB/km. The student sees one statement saying bend loss is never per km and another giving it per km.
- ch 4 [low] Figure and Section 1: The text says the real curve is flat at large R and turns up sharply near R_c, but the plot draws one exponential 8e^(−0.6R) over the whole 2–12 mm range, which keeps falling steeply and never flattens or kinks. A student may take the exponential as the true physical curve at all radii.
- ch 5 [high] Section 1, "Two rays, two arrival times": The arrival time of the steepest guided ray is wrong. The zig-zag path is L/cos θ = L n₁/n₂, but light in the core travels at speed c/n₁, not c. So the time is (L n₁/n₂) × (n₁/c) = L n₁²/(c n₂). The printed t₂ = L n₁/(c n₂) is missing one factor of n₁ and does not give the ΔT formula printed just below it (subtracting t₁ = L n₁/c from L n₁/(c n₂) does not produce (L n₁/c)((n₁ − n₂)/n₂)).
- ch 5 [high] Section 3, formula box for B ≤ 1/(2ΔT): The note under the formula says "Both lengths must be in the same unit before you compare them." The formula contains no lengths, only times (the spread ΔT and the bit period 1/B). A student will look for two lengths that are not there and miss the real point about units.
- ch 5 [low] Figure aria description: The description says the step-index line "climbs fifty times faster" than the graded-index line. The slopes are 50 ns/km and 0.25 ns/km, so the step-index line climbs two hundred times faster. Fifty is the step-index slope in ns/km, not the ratio.
- ch 5 [low] Lead: The lead says graded-index profiles shrink the spread "by about a factor of a hundred", but section 2 and worked example 1 show the improvement is 2/Δ = 200 for Δ = 0.01, and the chapter's own numbers (50 ns/km against 0.25 ns/km) give 200. The two figures conflict.
- ch 6 [high] Figure, caption and the 'Material D_m' node note: The figure note says the material part has 'zero ≈ 1310 nm' and the caption says the material zero 'is fixed near 1310 nm by the glass'. This contradicts the text, which puts the material zero near 1300 nm and the fiber zero near 1310 nm. 1310 nm is where D_m + D_w = 0, not where D_m = 0. A student reading only the figure will conclude the glass itself has zero material dispersion at 1310 nm.
- ch 6 [low] Quiz Q7: The answer says D_m at 1310 nm is 'about +3 ps/(nm·km)', which implies the material zero sits near 1275 nm. The text says the material zero is near 1300 nm, and with the stated slope of about 0.09 ps/(nm²·km) a 10 nm offset gives only about +1 ps/(nm·km). The two statements do not agree.
- ch 6 [low] Lead: 'That spreading is chromatic dispersion, quoted in ps/(nm·km)' mixes the spread (a time, in ps) with the coefficient (ps/(nm·km)). A student may quote the pulse spread in ps/(nm·km).
- ch 6 [low] Section 1, sign-convention sentence: 'Some call the red-first case positive' uses 'red-first' without definition; many readers will not connect red with the longer wavelength.
- ch 7 [high] Section 2, second formula: The inequality D_PMD √L ≤ 0.1 T_b mixes units. D_PMD √L comes out in ps (D_PMD in ps/√km, L in km), but T_b is defined in ns, so the two sides differ by a factor of 1000. A student who plugs T_b = 0.1 ns and mean DGD = 1 ps into the formula as written gets 1 ≤ 0.01, which is false. The worked example converts correctly to ps, so the formula itself contradicts the example.
- ch 7 [low] Sections 1 and 2: The symbol B is used twice with different meanings: B = |n_x − n_y| for birefringence in Section 1, and B for bit rate in the Section 2 formula (0.1/B). Students can confuse the two in the same chapter.
- ch 7 [low] Section 1: "Only a few universities teach this topic" sits in the middle of the explanation, breaks the flow, and is doubtful: PMD is a standard item in most optical fiber communication syllabi.
- ch 7 [low] Section 1, first paragraph: "the differential group delay (DGD) adds linearly" is loose wording; DGD does not add, its accumulated value grows with length in a uniform piece.
- ch 8 [low] Exam traps, first bullet: The wording "20 km at −85 outweighs 100 km at +17" is numerically false: 20 × 85 = 1700 ps/nm and 100 × 17 = 1700 ps/nm, so the two exactly cancel (as Worked example 1 shows). A student may read it as saying the spool over-compensates and contradicts the worked example.
- ch 8 [low] Section 2: "Neighbouring channels drift out of phase within a few kilometres" overstates the distance. With D of a few ps/(nm·km) and channel spacing of about 0.8 nm (100 GHz at 1550 nm), the walk-off length 1/(D·Δλ) is well under 1 km, not several kilometres.
- ch 8 [low] Section 3: "Ten to twenty kilometres of DCF cancels a hundred kilometres of standard fiber" does not fit the D values just quoted. With DCF at −85 to −100 ps/(nm·km) and line fiber at about +17 ps/(nm·km), the required length is 17 to 20 km; 10 km would need a DCF near −170 ps/(nm·km).
- ch 8 [low] Section 2: "Small enough that the spread over a span stays within the receiver's tolerance" is vague: the tolerable dispersion depends on bit rate (roughly 1000 ps/nm at 10 Gb/s, far less at 40 Gb/s), so the statement is only true for lower rates.
- ch 9 [high] Section 2, the nepers-per-metre conversion in the L_eff formula: The conversion instruction is wrong by a factor of 1000. Dividing dB/km by 4.343 gives nepers per kilometre, not nepers per metre, because 1 Np = 4.343 dB for the power-attenuation coefficient. A student following it gets α = 0.046 Np/m instead of 4.6×10⁻⁵ Np/m, and then 1/α = 22 m, which contradicts the 22 km stated two lines later.
- ch 9 [low] Section 2, first sentence: 'Both effects switch on when the gain collected over the strong part of the span equals the loss' contradicts the formula that follows, where the required gain factor is G ≈ 21 (Brillouin) or ≈ 16 (Raman), not unity.
- ch 9 [low] Section 1, SBS mechanism: 'The signal beats with acoustic waves in the glass' is imprecise: an optical wave does not beat with an acoustic wave. The beat is between the signal and the Stokes wave, and that beat drives the acoustic wave through electrostriction.
