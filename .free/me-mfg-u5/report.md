# me-mfg-u5: free-model run

- Book: `books/mech/me-mfg/me-mfg-u5.html`
- Status: ok
- Model calls so far: 34 (118,235 tokens in, 246,858 out), 6.1 minutes

## Checker

```
me-mfg-u5.html: 9 chapters, 15990 words, 10 figures, 164 KB
OK
```

## For the reviewer

- chapter 4: the figure cannot be drawn: tree is too wide (5 leaves); use fewer leaves or shorter labels
- chapter 8: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 8: worked example 1: the worked example states [8.0] but recomputing it gives [90.0, 9.425, 3.0, 3.75, 96.0, 1.333, 7.0]; fix the steps and the answer so they match the correct values
- chapter 4: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, depth of cut definition: Two different things are collapsed into d. The first clause says d is the layer thickness removed in one pass (that is the uncut chip thickness t₁), and the second clause says the width of cut measured along the edge is taken as d in orthogonal tests. In the standard orthogonal model the width of cut is b (equal to the feed per revolution in tube turning, or to the plate width in planing/broaching); d is not the width along the edge. A student will write the wrong sentence in the exam.
- ch 1 [low] Section 2, paragraph after the shear angle formula: Internal contradiction. If r is held fixed, t₂ = t₁/r does not change, so the chip cannot be thinner. The last part of the sentence contradicts 'for the same r'.
- ch 1 [low] Exam traps, third trap: Rake-angle names in oblique cutting are convention-dependent and the trap mixes them. The standard oblique model distinguishes the normal rake αn (measured in the plane normal to the cutting edge), the velocity rake and the effective rake αe (measured in the chip flow direction). In the usual tool-signature convention the side rake is measured in the plane normal to the side cutting edge, so calling it the opposite of the normal rake can mislead.
- ch 2 [low] Section 3, procedure: A high τ is answered with 'reduce feed', but reducing feed lowers the uncut chip thickness and raises the shear stress on the shear plane (the size effect). The student is told to do the opposite of what helps.
- ch 2 [low] Quiz Q7, answer: The answer says 'a smaller shear area raise shear stress'. With μ falling, β falls and Merchant's relation gives a larger φ, hence a larger shear area, not a smaller one. The reason contradicts the chapter's own relation.
- ch 3 [high] Section 2, and repeated in Exam traps bullet 1: The text says that reading 10 as back rake instead of side rake 'changes the wedge and the relief' (trap: 'changes rake and relief'). Swapping slots 1 and 2 changes only the two rake angles and therefore the wedge. The relief angles sit in slots 3 and 4 and are not affected by misreading a rake value. A student will memorize this wrong link between rake slots and relief slots.
- ch 3 [low] Section 1, first sentence: The sentence says the tool has five parts, then lists six: shank, face, flank, nose, side cutting edge and end cutting edge. The count and the list do not match.
- ch 4 [high] Exam traps, second bullet: The trap says 18-4-1 means '18% W, 4% Cr and 1% V by mass, not 18 parts, 4 parts and 1 part'. A percentage is parts per hundred, so 18% W is exactly 18 parts of tungsten in 100 parts of steel. The contrast drawn is false, and a student will come away thinking percentages and parts mean different things.
- ch 4 [low] Section 2, application methods: 'Mist carries fluid droplets in air; it cools little' is misleading. Mist is essentially a cooling method, since the fine droplets evaporate at the cutting zone and take heat away. Its real drawbacks are poor lubrication, low heat-carrying capacity compared with flooding, and the health risk from inhaled droplets.
- ch 4 [low] Section 1, comparison table (CBN, diamond row): The table puts ceramic and CBN/diamond at the same toughness, 'Very low'. CBN is clearly tougher than ceramic and is chosen for interrupted cutting of hardened steel, where a ceramic insert would chip. Grouping CBN with diamond in one row also hides that the two behave quite differently.
- ch 4 [low] Figure caption: The caption says materials are ordered by hot hardness and cost, but coated carbide is placed after uncoated carbide. The coating raises wear resistance and lowers friction; it does not make the substrate keep its hardness at a higher temperature.
- ch 4 [low] Section 2, application methods: 'only a few universities teach MQL, but industry uses it to cut fluid waste' is filler about syllabi sitting inside a technical description; it tells the student nothing about how MQL works in the cut.
- ch 4 [low] Lead and end of Section 2: The cross-reference 'See 5.5 for how heat becomes wear' appears twice in the same short stretch, once in the lead and once at the end of Section 2.
- ch 4 [low] Section 1, carbon tool steel bullet: 'loses hardness at a few hundred degrees Celsius' is too vague to be useful; a student cannot tell whether 250 °C is safe. Carbon tool steel is tempered from about 200 °C, so its working limit is well below 300 °C.
- ch 5 [low] Section 2 and exam trap 2: The text says C "carries units that depend on n" and that "its value and unit depend on n". With T taken in minutes, C is simply the cutting speed at T = 1 min and its unit is m/min for every n. Only the numerical value of C changes with n, not the unit. A student may write C in odd units such as m/min·minⁿ in the exam.
- ch 6 [high] Worked example 1, step 6: The split of the two passes is wrong. The stock on radius is 3 mm, so if the first pass takes 2 mm the second can only take 1 mm. Saying the second takes 1.5 mm removes 3.5 mm in total, which is more metal than exists.
- ch 6 [high] Exam traps, feed trap: The direction of the error is reversed. Dividing L by f instead of by f N gives L/f = 150/0.2 = 750 min, which is N times larger than 3.93 min, not smaller.
- ch 6 [high] Exam traps, depth-of-cut trap: The stated consequence is wrong. A student who treats the whole diameter reduction D₁ − D₂ as one depth of cut computes 6/2 = 3 passes, which is twice the correct 1.5 passes, not half.
- ch 6 [low] Section 3, depth of cut paragraph: "The tool removes d from the radius on each side of the axis" suggests cutting happens on both sides of the axis at once and confuses the reader about where the factor 2 comes from.
- ch 6 [low] Section 2, capstan and turret lathe: "batch production of one part in thousands" reads like a defect rate rather than a batch size.
- ch 7 [low] Section 2, milling feed sentence: The table feed is written as 'fzzN', which a reader can misread as one symbol. The per-tooth feed fz is also given without its unit.
- ch 7 [low] Section 1, drill point description: The approach allowance is tied to the chisel edge. The approach comes from the point cone geometry: the drill tip must travel its point length before the full diameter cuts.
- ch 7 [low] Section 1 formula box and Worked example 1, step 3: The time formula uses L + A, which suits a blind hole depth. For a through hole the drill must also break through, so the travel is a little longer than plate thickness plus approach.
- ch 8 [low] Section 1, and Quiz Q1: The module is described as having the unit 'mm per tooth', and Q1 repeats 'Its unit is mm per tooth'. A student may write mm/tooth in the exam and lose the mark; the standard unit of module is simply the millimetre.
- ch 8 [low] Section 2 (conventional and climb hobbing): 'Climb hobbing ... giving thinner chips' is loose and contradicts the Q7 answer. In climb cutting the chip is thickest at entry and tapers to zero at exit; the gain is less rubbing and work hardening, not thinner chips.
- ch 8 [low] Section 2, first paragraph: The statement that the hob axis is tilted by its lead angle is true only for spur gears; for helical gears the swivel angle also involves the gear helix angle, so the sentence is incomplete.
- ch 8 [low] Section 2, rack planning sentence: Saying only that the rack cutter reciprocates while the work rotates leaves out the rolling motion that actually makes the involute; the rack pitch line must roll on the pitch circle without slip.
- ch 9 [low] Section 1, wheel marking explanation: 'Structure is the spacing of grains; 5 is medium dense' is loose. Structure numbers run from 1 to 15 and a higher number means wider spacing (more open). A value of 5 sits on the dense side, so calling it 'medium dense' can mislead a student reading the marking.
- ch 9 [low] Section 4, superfinishing: 'removes only the fragmented surface layer and no measurable geometry' is ambiguous. Superfinishing does remove a few micrometres of metal; what it does not do is correct size, roundness or other geometry errors.
