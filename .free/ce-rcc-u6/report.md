# ce-rcc-u6: free-model run

- Book: `books/civil/ce-rcc/ce-rcc-u6.html`
- Status: ok
- Model calls so far: 28 (90,957 tokens in, 250,005 out), 9.8 minutes

## Checker

```
ce-rcc-u6.html: 9 chapters, 15996 words, 10 figures, 163 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Lead: The lead says a stretched tendon 'puts the whole section into compression'. The chapter's own worked example shows the top fibre left in 2.5 N/mm² tension by an eccentric tendon, so 'whole section' is misleading.
- ch 1 [low] Section 1 and Section 2: Transfer is described only through anchorages bearing on the concrete, but Section 2 also mentions taking the beam 'off the bed'. That is pre-tensioning, where transfer happens by bond, not through anchorages. A student meets two mechanisms without being told they are different systems.
- ch 1 [low] Worked example 1, steps 7 and 8: The chapter says to take compression as positive, but steps 7 and 8 compute in a tension-positive sense (8 − 12.5 = −4.5, then call it compression). The magnitudes are right, yet the sign working contradicts the stated convention and can confuse a student copying the method.
- ch 1 [low] Section 2: 'The concrete cracks only when that tension reaches its own tensile strength' names the direct tensile strength. A bending member cracks at the flexural tensile strength (modulus of rupture), which is higher.
- ch 1 [low] Section 1 formula: Calling P × e 'the moment resisted by the prestress couple' under the symbol Mr invites the reading that P·e is the moment capacity of the section, which it is not.
- ch 2 [low] Section 2 (high-strength concrete): The M30 relaxation is attached to 'lightly stressed members', which is not the usual basis for it. The general minimum grade for prestressed work is M40; where older or other codes permit a lower grade, it is an exception for post-tensioned members, not for members that happen to be lightly stressed.
- ch 2 [low] Section 2, sentence after the Ec formula: 'Better resistance to creep and shrinkage' is loose wording. What happens is that higher-grade concrete has lower creep and lower shrinkage, so the losses they cause are smaller; it is not a matter of good concrete 'resisting' shrinkage.
- ch 2 [low] Worked example 1, part (c): The question asks the student to state one practical conclusion, but the answer line only repeats the two areas and never states the conclusion, so there is no model answer for part (c).
- ch 3 [low] Lead: The sentence "Only a few universities teach this detail; the main split is simple" has no clear antecedent — a reader cannot tell which detail is meant, and it interrupts the lead's flow.
- ch 3 [low] Section 1: The order of work skips the condition for release. A student may think the tendon is released as soon as casting is done, and the reason slow release matters (shock, slip) is left hanging.
- ch 3 [low] Section 2: "End slip means bond has failed" is too absolute. A small end slip at release is normal; only excessive slip points to poor bond or a long transfer length.
- ch 3 [low] Section 2: "The tendon profile is usually straight, so eccentricity is small" is misleading. A straight tendon in a long-line bed is still placed low in the section, giving working eccentricity; the real limitation is that the profile cannot easily be curved, though deflectors (harping) can be used.
- ch 3 [low] Section 3: "The transfer point is the exam favourite" is vague slang and does not say what the point is.
- ch 3 [low] Figure: The post-tensioning bar is labelled "Cast duct". The duct is fixed or placed, and concrete is cast around it; the duct itself is not cast.
- ch 4 [low] Worked example 1, step 3 and answer: Section 2 says the member self-weight acts at transfer, but step 3 sets M = 0 at transfer and the answer then calls the 2 N/mm² top tension the transfer stress. A student may conclude that no moment ever acts at transfer, or may not see that the self-weight moment was deliberately dropped.
- ch 4 [low] Section 2, paragraph on uncracked range: The sentence 'A beam with M below M_dec is uncracked and the elastic formulas hold' suggests the elastic gross-section formula stops being valid just above M_dec, but it still holds between M_dec and M_cr.
- ch 4 [low] Section 3, w_p formula and definition of e: e is described only as 'tendon sag at midspan'. In a real draped tendon the ends are not at the centroid, and the w_p formula needs the sag measured from the straight chord joining the two tendon ends, not the midspan eccentricity measured from the centroid.
- ch 4 [low] Section 2, cracking moment: f_cr is defined only as 'modulus of rupture'. No value or expression is given, so a student cannot use M_cr in a numerical check.
- ch 5 [high] Section 2 (anchorage slip): L is defined as the 'tendon length affected by slip', but the formula Δfp,slip = Esδ/L only holds when the whole tendon length shortens uniformly by δ. With friction, the slip is absorbed over a shorter length ls (< tendon length), the strain varies from a maximum at the anchor to zero at the end of ls, and the stress loss at the anchor is about twice the average δEs/ls. Using the 'affected length' in this formula therefore underestimates the loss at the anchor.
- ch 5 [low] Section 2 (elastic shortening and anchorage slip force losses): ΔPes = Aps Δfp,es and ΔPslip = Aps Δfp,slip give the force in newtons (mm² × N/mm²), but Section 1 defines every ΔP term in kN. A student who keeps the stated units gets a force 1000 times too large.
- ch 5 [low] Figure: The curve starts at 100% at month 0 and glides down to 96% at month 1, but friction, anchorage slip and elastic shortening are immediate losses that occur during stressing or at transfer. Drawing them as a slow month-long fall contradicts Section 1.
- ch 6 [high] Quiz Q7 (and Section 2 flanged-section rule): The answer uses 0.36 fck for the flange overhang as well as the web: C = 0.36 fck[bw xu + (bf − bw) Df]. The standard stress block (IS 456 style, as used in prestressed flanged design) uses 0.36 fck bw xu for the web but 0.45 fck (bf − bw) yf for the flange overhang, so the quiz number 0.36 fck × 132,000 N is not the correct compression force.
- ch 6 [low] Section 1 and Q3: The three tension categories are called Type 1, Type 2, Type 3, but IS 1343 names them Class 1, Class 2, Class 3. Students meeting the code terminology may not connect the two.
- ch 7 [high] Lead: The lead says the spreading of the force creates both bursting and spalling ("This spreading creates transverse tension ... called bursting, and small surface tension, called spalling"). Spalling is not caused by the spreading of the force. It is a local effect at the loaded face, where the stiff bearing plate restrains the lateral expansion of the concrete around it, so tension appears on planes parallel to the loaded face just outside the plate. The chapter's own Q4 answer contradicts the lead: it says a larger plate (which reduces spreading) still leaves spalling to be dealt with.
- ch 7 [low] Section 3, bursting steel formula: Ast ≈ Fbst / (0.87 fy) does not state the units to be used. With fy in N/mm², Fbst must be in N. A student who puts Fbst in kN (as the worked example and Q3 report it) gets an Ast that is 1000 times too small.
- ch 7 [low] Section 3 and worked example: Section 2 defines P as the anchorage force after losses, but Section 3 and the worked example use P without saying what it is (jack force or force after losses). The bursting force and bearing stress both change with the force chosen.
- ch 7 [low] Section 3, bursting force formula: For a rectangular plate the formula uses a and b in one direction only. The chapter never says that bursting must be checked separately in each direction, with a and b taken as the plate and end-block dimensions in that direction.
- ch 8 [high] Section 2, definition of linear transformation: It says a and b are constants with units of length. In enew = e + a + b x, x has units of length, so b x has units of length only if b is dimensionless; b is a slope. Only a has units of length.
- ch 8 [high] Section 3, two-span example: The beam has two equal spans L, so its total length is 2L. With et = k x/L measured from the left end, at the right end x = 2L and et = 2k, not k. The stated right-end eccentricity 100 + k mm is inconsistent.
- ch 8 [low] Section 2, reactions from equivalent loads: The statement that reactions from prestress are found from wp and support conditions is incomplete: anchorage forces and moments also enter the equivalent load system. The linear transformation conclusion is still correct because the added straight line’s anchorage effects are self-equilibrated, but the text does not say this.
- ch 8 [low] Figure, node e: The note 'Same reactions if concordant' suggests reactions are preserved only for concordant cables. Linear transformation leaves the existing reactions unchanged for any cable; they are zero only when the cable is concordant.
- ch 9 [high] Section 2, first design-check bullet: The bullet says to estimate the prestress moment Mp using the effective prestress at the service or ultimate state. Effective prestress is a service-load value; at ultimate the tendon stress is higher and must be found from strain compatibility. Using effective prestress in Mu = Mp + Ms mixes service and ultimate states and gives a wrong ultimate contribution.
- ch 9 [low] Lead: The phrase 'ordinary reinforced concrete needs larger sections and wider cracks under heavy load' says ordinary RC needs wider cracks. Cracks are not a design need; they are an unwanted result.
