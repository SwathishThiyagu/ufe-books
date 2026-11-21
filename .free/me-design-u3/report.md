# me-design-u3: free-model run

- Book: `work/me-design-u3/tree/books/mech/me-design/me-design-u3.html`
- Status: ok
- Model calls so far: 20 (77,438 tokens in, 198,964 out), 6.6 minutes

## Checker

```
me-design-u3.html: 6 chapters, 19367 words, 7 figures, 176 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Worked example 1, steps 5-7 and answer: The example checks only the side where bending tension is partly cancelled by the axial compression (σ_x = σ_b − σ_a). The maximum shear stress occurs on the opposite side, where bending compression and axial compression add: there σ_x = −(σ_b + σ_a). At the stated answer d = 35.45 mm that side gives σ_x = −(68.58 + 10.13) = −78.71 MPa and τ = 27.29 MPa, so τ_max = ½√(78.71² + 4×27.29²) ≈ 47.9 MPa, well above the 40 MPa allowable. The quoted diameter is unsafe, and it contradicts the chapter's own advice in Section 1 ('check the side where axial stress adds to bending') and the fourth exam trap.
- ch 1 [high] Worked example 2, steps 6-7 and answer: Same error as example 1. Taking σ_x = σ_b − σ_a checks the tension side only. On the compression side σ_x = −(70.27 + 13.15) = −83.42 MPa and τ = 27.96 MPa at D = 35.93 mm, so τ_max = ½√(83.42² + 4×27.96²) ≈ 50.2 MPa > 40 MPa. The hollow shaft is under-designed.
- ch 1 [high] Quiz Q7: The answer uses a minus sign, σ_x = 32M/(πd³) − 4P/(πd²). That is the normal stress at the point where bending tension and axial compression oppose, so it gives the smaller of the two shear values, not the maximum in the shaft. The question asks for the maximum shear stress, so the answer is wrong by a sign, and it repeats the mistake in the two worked examples.
- ch 1 [low] Section 1, first paragraph: The sentence 'a tangential force that produces torque T and a radial force that produces bending moment M' can make a student think the tangential force causes no bending. Both the tangential and the radial gear forces bend the shaft; the tangential force also produces the torque.
- ch 1 [low] Section 2, last sentence of the paragraph on shock factors: 'replace d³ by (D⁴ − d_i⁴)/D in the denominator with the appropriate factor' is vague; a student cannot tell what the resulting formula is.
- ch 2 [high] Section 3, critical speed and whirl: The unbalance response formula y = e/(1 − (ω/ωn)²) is wrong for the described case of mass eccentricity. For a rotor whose centre of mass is offset by e from the shaft's geometric centre, the correct undamped whirl amplitude is y = e r²/(1 − r²), which tends to e as r → ∞, not zero. The force balance is also wrong: the centrifugal force on the mass is m(y + e)ω², not m e ω², and equating it to k y gives the correct formula.
- ch 2 [high] Figure: The plotted expression 1/√((1−x²)²+(0.15x)²) is a force-response magnification factor, not the unbalance whirl response. It gives amplitude 1 at r = 0 and tends to 0 at high r, while the unbalance response starts at 0 and tends to 1 (times e). The damping term also uses ζr instead of 2ζr for ζ = 0.15, so the effective damping is half the stated value.
- ch 2 [high] Quiz Q6: The answer repeats the wrong formula y = e/(1 − (ω/ωn)²) and says the amplitude becomes small in magnitude, so the shaft runs smoothly. The correct unbalance response tends to e, not zero; the shaft deflection is about e (small only because e is small), and the centre of mass lies on the rotation axis.
- ch 2 [high] Exam traps, first trap: Plugging δ in millimetres makes the answer √1000 ≈ 31.6 times too small, not too large, because δ is in the denominator of g/δ.
- ch 2 [low] Section 3, numerical example: 0.07 mm gives Nc ≈ 3575 rpm, not 3590 rpm. The value 3590 rpm corresponds to 0.0694 mm from the worked example.
- ch 2 [low] Section 3, first sentence: e is the distance from the shaft's geometric centre to the centre of mass, not from the rotation axis. After whirl, the centre of mass is at y + e from the axis.
- ch 2 [low] Section 1, deflection limits: 0.08 mm is eight hundredths of a millimetre, not 'a few hundredths'.
- ch 2 [low] Section 1, seal: Shaft deflection at a seal changes the clearance; it closes the gap on one side and opens it on the other, so 'opens the gap' is incomplete.
- ch 3 [low] Section 1: The reason given for top clearance is imprecise: the hub does not seat on a 'shaft shoulder' because of the clearance. Top clearance exists so the hub seats on the shaft itself and the key does not bear on its top face, keeping the load on the key's side faces.
- ch 3 [low] Section 3: 'Reduce the shaft's torsional strength by about one-fifth' mixes a strength allowance with what handbooks actually express as a stress-concentration factor or a diameter increase. A 20% loss of strength means a diameter increase of only about 7%, which is easy to misapply.
- ch 3 [low] Section 3: 'Both let a hub slide along the shaft' over-generalises. A spline permits sliding only with a sliding fit; fixed splines (press or side fit) do not slide, and many spline joints are rigid.
- ch 3 [low] Quiz Q1: The answer lists a spline as a type of key. The chapter itself defines a spline as many keys cut as teeth, but standard key classification treats sunk, saddle and round keys as keys, with splines as a separate joint.
- ch 3 [low] Section 2: The bearing pressure calculated as crushing stress also acts on the hub keyway, and the hub (often cast iron or softer steel) can be the weaker member. The chapter checks only the key, so a student may pass a key that crushes the hub.
- ch 4 [low] Lead: "Couplings sit behind the shaft and key: the shaft is designed first, the key fixes the hub, and the coupling joins the next shaft" is compressed to the point of being unclear. A student cannot tell whether the coupling is designed before or after the shaft.
- ch 4 [low] Section 1: "Some syllabi call the flange coupling a rigid coupling, and design it as one" suggests that calling it rigid is a syllabus habit. In standard texts the plain bolted flange coupling is the rigid coupling; only the bushed-pin version is flexible. The sentence can make a student think the flange coupling is normally flexible.
- ch 4 [low] Section 1, sleeve coupling: The sleeve coupling is called "short". It wraps over both shaft ends, so it takes more axial room than a flange coupling, and removal needs one shaft to be moved back.
- ch 4 [low] Section 1, bolt crushing formula: The symbol σc is used for both the calculated crushing stress and the allowable value in the same line, σc = Fb ÷ (db t) ≤ σc,allow.
- ch 4 [low] Section 2, balancing paragraph: "Balance is more critical above 3000 rpm" gives a fixed speed with no basis, and the same number is repeated in Quiz Q7. The real reason is that the unbalance force grows with the square of speed, so there is no single threshold.
- ch 4 [low] Section 2, bushed pin coupling: The pin load path is only partly described. The bolt shank carries shear at the flange face, but the pin is also bent over the length of the bush, and that bending check is a standard part of bushed-pin design.
- ch 4 [low] Worked example 1, step 6: The crushing check is left open although M10 has been selected. A student may read the answer as a complete bolt design.
- ch 5 [high] Section 2 (uniform wear and uniform pressure): The sentence says the lining wears fastest where pressure × sliding speed is largest, 'which is at the inner radius'. Sliding speed is ωr, so pressure × sliding speed grows with radius. A new, nearly uniformly loaded face wears fastest at the OUTER radius. That is exactly why the face redistributes until p × r is constant, leaving the highest pressure at the inner radius. The sentence also contradicts the chapter's own Quiz Q2 answer, so a student gets two opposite statements.
- ch 5 [high] Worked example 1, step 9 (and the answer 11.8 kJ): Step 9 says 'the torque falls from its peak to zero as the speeds equalise'. Under a constant spring force the friction torque stays roughly constant; it is the relative speed Δω that falls from 600 rpm to zero. With constant torque the fall in Δω is linear, so the mean Δω is Δω₀/2 and the heat per engagement is about half the quoted value. The stated 11.8 kJ is therefore roughly double the correct estimate, and the reason given for calling it an estimate is wrong.
- ch 5 [low] Section 1 (plate counting) versus Section 2 (n = 2): Section 1 says 'p plates give p − 1 rubbing pairs', which read literally gives zero pairs for a single-plate clutch, while Section 2 and the example say a single-plate clutch has n = 2 rubbing pairs. The p − 1 rule only holds when the flywheel and pressure-plate faces are counted as plates too.

## Correction pass (21 Nov 2026, Claude)

- Every chapter rewritten from the draft for the ME3591 exam course; every worked example, quiz and bank number recomputed in Python.
- Reviewer flags all closed: ch 1 design point on the side where bending and axial compression add; ch 2 unbalance response y = e r²/(1 − r²) and the mm-trap direction; ch 3 top clearance, splines that slide only with a sliding fit, hub keyway crushing; ch 4 flange coupling wording, bushed-pin bending check, no fixed 3000 rpm threshold; ch 5 outer-edge wear, mean slip speed (5.9 kJ, not 11.8 kJ), pair counting.
- Added: shaft/axle, belt and gear loads, equivalent bending moment, ASME shock factors and allowable stress (ch 1); torsional rigidity design and Dunkerley with the shaft's own mass (ch 2); key types, key proportions, key as strong as the shaft, Moore's factor, spline torque (ch 3); muff, clamp and protected flange proportions, full flange coupling design, bushed-pin design (ch 4); new ch 6 connecting rods and crankshafts (exam subtopic).
- Six hand-drawn figures from the chapters' own examples; 15 long questions with full model answers.
- Unit numbers of other units, carets, underscores, MIT and NPTEL links removed; web reading list limited to pages opened.
