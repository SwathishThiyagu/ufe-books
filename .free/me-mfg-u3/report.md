# me-mfg-u3: free-model run

- Book: `books/mech/me-mfg/me-mfg-u3.html`
- Status: ok
- Model calls so far: 21 (74,289 tokens in, 157,806 out), 4.9 minutes

## Checker

```
me-mfg-u3.html: 6 chapters, 10952 words, 7 figures, 119 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Worked example 1, steps 2, 3, 5; Quiz Q2 answer; Quiz Q5 answer: The exponent has lost its superscript, so the formula is displayed as σ = K εn and the arithmetic as 500 × 0.200.20 and 600 × 0.150.22. Read literally, K εn means K × ε × n, and 0.200.20 looks like 0.200 × 0.20. A student can follow the wrong operation and get a meaningless answer.
- ch 1 [low] Section 2, formula for r: In a tensile test the width strain is positive and the thickness strain is negative, so the ratio as written comes out negative (about −1.8) and clashes with the stated r = 1.5 to 2.0. The sign convention is not given.
- ch 1 [low] Section 1, first paragraph: "In forming, the punch shape and clearance set the strain path" mixes blanking clearance with forming. Cutting clearance is not what sets the strain path in a forming operation; the punch and die profile, the blank-holder force and friction do.
- ch 1 [low] Section 1, first paragraph: "first thins locally, then necks, then tears" puts local thinning before necking, but local thinning is the local neck itself. The usual order is uniform thinning, then diffuse necking, then a local neck, then tearing.
- ch 1 [low] Quiz Q7 answer: "Thickness strain must carry most of the deformation, so thinning localises earlier" gives the wrong reason: for the same major strain, thinning is actually larger on the tension-tension side (ε3 = −(ε1+ε2)) yet the limit there is higher. The point to make is that at plane strain there is no minor strain to share the deformation, so the major strain is carried entirely by thinning, and any local thin patch cannot be supported by sideways flow.
- ch 2 [low] Lead: The lead defines shearing as cutting 'along a closed line', but shearing also covers straight cuts (a guillotine shear, slitting, trimming, notching), all of which the chapter itself lists in Section 2. The narrow definition contradicts the later text.
- ch 2 [low] Figure (tree notes and aria): The punching branch is labelled 'hole is scrap' and the aria says 'where the hole is scrap'. The hole is empty space; the scrap is the slug. This contradicts Section 2, which correctly says the slug is scrap.
- ch 2 [low] Section 2: 'The same 50 mm punch makes a punching if you keep the strip' is awkward wording that can confuse a second-language reader about the operation name.
- ch 3 [high] Lead and Section 2: The lead says the flat blank must be longer than the bent part's outside dimensions. This contradicts standard sheet-metal practice: the flat length is the sum of outside dimensions minus the bend deduction, and BD is positive for a 90° bend. The outer surface stretches to a length longer than the flat blank, not the other way round. Section 2 itself uses 'outside dimensions minus BD', which makes the blank shorter than the outside-dimension sum.
- ch 3 [high] Section 3 and Quiz Q7: The chapter defines θ as the angle through which the sheet turns. Springback reduces this turn angle; the included angle between the flanges opens. To finish at a 90° turn, the punch should be set to about 92° (92° − 2° springback = 90°), not 88°. Setting 88° is correct only if 88° is the included angle between flanges, which is not the angle defined earlier and used in the bend-allowance formula.
- ch 4 [low] Section 3, ironing paragraph: "Ironing forces the cup through a die that is slightly smaller than the cup wall" compares a die size with a wall thickness, so a student can read it as a die smaller than 2 mm. The comparison should be with the cup's outside diameter.
- ch 4 [low] Worked example 1, step 1: The sheet thickness t = 2.0 mm is listed in the data but never used anywhere in the solution, which makes students think a step is missing. The formula used is the thin-sheet one that ignores thickness.
- ch 4 [low] Figure spec, edges: The edge from the blank holder to the punch is labelled "held", which says the blank holder holds the punch. It is the blank that the blank holder holds, so the reading order of the block diagram is misleading.
- ch 4 [low] Section 2, blank holder paragraph: The flange is described as "the unsupported flange", but the flange is exactly the part the blank holder presses on; the imprecise word can confuse students about which region wrinkles.
- ch 4 [low] Section 1, definition of cup drawing: The chapter never states the usual shop convention that separates ordinary drawing from deep drawing (depth large compared with diameter); Q1 asks students to define deep drawing but the answer gives no such basis.
- ch 5 [high] Section 2, coining paragraph: The sentence 'the blank is thinner than the rim' is wrong and self-contradictory. Material for the raised rim and relief must come from the blank itself, so the blank has to be thicker than the finished coin's field thickness. As written, a student cannot see where the metal for the relief comes from, and the statement clashes with the same paragraph's own claim that the metal 'has nowhere to escape'.
- ch 5 [low] Section 1, after the process steps: 'Only gentle, mostly single-curvature shapes pay off' is misleading. Stretch forming does produce compound (double) curvature, for example contoured aircraft skins; what it cannot do is deep, sharply contoured shapes, because the sheet would tear at a sharp corner of the block.
- ch 6 [low] Section 1, bullet list of machine parts: The list mixes machine components (hopper, barrel and screw, nozzle, mould, injection unit) with cycle stages (fill, pack, cool, eject) in one ungrouped list, so a student may read 'fill' or 'pack' as a machine part.
- ch 6 [low] Section 1, 'Barrel and screw' and 'Injection unit' bullets: Heaters are named as the only melting source, and the injection unit bullet describes an action ('stops screw rotation and pushes the screw forward as a ram') rather than the unit itself.
- ch 6 [low] Figure, edge from 'm' (Mould) to 'p' (Part): The arrow out of the mould is labelled 'cool', but cooling happens inside the closed mould; what that arrow represents is ejection of the cooled part.
