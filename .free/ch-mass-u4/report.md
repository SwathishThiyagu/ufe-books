# ch-mass-u4: free-model run

- Book: `books/chem/ch-mass/ch-mass-u4.html`
- Status: ok
- Model calls so far: 26 (111,317 tokens in, 254,989 out), 5.8 minutes

## Checker

```
ch-mass-u4.html: 9 chapters, 16328 words, 10 figures, 181 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, first formula and symbol list: The total-pressure equation P = pA + pB uses pB and xB, but the symbol list defines only pA, xA, P°A and P. A student meeting pB for the first time has to guess what it means.
- ch 1 [low] Section 1, last paragraph and exam trap 4: The statement that a two-phase mixture needs P between P°B and P°A is only a necessary condition. A mixture whose overall composition is rich in A can already be all liquid at a pressure below P°A. A student may read 'between P°B and P°A' as meaning 'then it is two-phase'.
- ch 1 [low] Section 1, opening paragraph: 'Some syllabi call this vapour-liquid equilibrium (VLE)' reads oddly, because the paragraph is already describing VLE, not a special case of it.
- ch 2 [high] Section 2, degrees of freedom paragraph: "Fix P and V/F instead and the drum temperature adjusts — the adiabatic flash" is wrong. In an adiabatic flash the vapour fraction is not a specified quantity; what is fixed is the feed enthalpy (feed T, P, composition) and the drum pressure. The drum temperature and V/F then come out together from the energy balance combined with Rachford-Rice. Naming a fixed-V/F calculation "adiabatic flash" teaches a wrong specification.
- ch 2 [high] Quiz Q5: The answer is self-contradictory and the conclusion is backwards. With z_A = 0.50, K_A = 2.0 and K_B = 0.5, Σ z_i K_i = 0.50(2.0) + 0.50(0.5) = 1.25 > 1, so this condition is <i>above</i> the bubble point, already inside the two-phase region, and the root of Rachford-Rice lies at ψ > 0, not at ψ = 0. The answer says the condition "lies below the two-phase region; the drum must be heated further", which is the opposite. It also quotes y_A = 1.00 while y_B = 0.5 × 0.667 = 0.25, so the quoted vapour does not sum to one.
- ch 2 [high] Quiz Q6: The answer is garbled and breaks off: "0.85  1 and Σ z_i/K_i > 1." A student cannot read what happens or what to change.
- ch 2 [low] Quiz Q3: "V/F is set by the pressure drop instead" is loose. In an adiabatic flash the pressure sets the K values, but the vapour fraction is fixed by the feed enthalpy together with that pressure, not by the pressure drop alone.
- ch 2 [low] Figure caption: "Note that the vapour and liquid flows are equal here" reads as a property of a flash drum. V = L only because of the particular numbers chosen (F = 100, V/F = 0.50); in general V and L differ.
- ch 2 [low] Section 3, root location: "a single root lies in 0 ≤ ψ ≤ 1" hides that the root is strictly inside the interval only while two phases exist; at a bubble or dew point it sits exactly at an endpoint.
- ch 3 [low] Section 2, first sentence: "For an ideal binary pair, α = (y/(1 − y))/(x/(1 − x))" makes it sound as if α can only be written this way for ideal systems. The ratio definition holds at any equilibrium point; what fails for non-ideal systems is α staying constant.
- ch 3 [low] Section 3, "Steam bubbles through the organic": A student may picture a separate organic layer being sparged. In practice steam is injected into the still that holds the immiscible organic liquid (or the plant material soaked in water), and both phases are present together.
- ch 3 [low] Exam traps, last bullet: "L₁, L₂, D are moles, not mass, unless the same mass basis is used consistently" is self-contradictory as written and can confuse a student about whether mass units are allowed.
- ch 3 [low] Figure spec notes: The notes L1=100, x1=0.5, L2=15.6, x2=0.2, D=84.4 carry no units, so the reader cannot tell that these are moles.
- ch 3 [low] Quiz Q3, answer: The answer stops at 0.571 without saying what the number is; a student may attach units to it.
- ch 4 [high] Exam traps, trap 5 (also Section 2 bullet 'Below the feed use the stripping line'): The rule 'use the rectifying line while x > x_F and the stripping line while x < x_F' is true only for a saturated liquid feed, where the q-line is vertical at x_F. For any other feed (two-phase, saturated vapour, subcooled liquid) the changeover point is the x-coordinate of P, the intersection of the two operating lines, which is not x_F. For a two-phase feed x_P is greater than x_F, so a student following this rule switches too early and gets a wrong stage count.
- ch 4 [low] Section 1, q-line definition and bullets: 'q is the fraction of feed that is liquid' is only true for feeds between bubble point and dew point. A subcooled liquid feed has q > 1 and a superheated vapour feed has q < 0, where 'fraction liquid' has no meaning; these two cases are also missing from the bullet list.
- ch 4 [low] Section 2, drawing instructions: 'Draw the q-line at x_F' tells the reader the q-line is always the vertical x = x_F. It is vertical only for a saturated liquid feed.
- ch 4 [low] Section 2, staircase bullets: x* appears in 'This gives x* at the current y' without being defined, and the equilibrium formula above defines only y*.
- ch 4 [low] Section 2, stage counting: 'Count each horizontal-vertical pair as one theoretical stage' is inaccurate at the bottom: the last step is often a horizontal move only, with no vertical move after it, yet it still counts as a stage.
- ch 4 [low] Section 2, last sentence: 'Real trays are more than theoretical stages' is garbled; it reads as if trays are a larger quantity than stages rather than a larger number of trays being needed.
- ch 4 [low] Quiz Q2, answer: 'The feed enters at liquid composition x_F' is misleading: x_F is the overall feed composition and the q-line passes through (x_F, x_F) for vapour and two-phase feeds too.
- ch 4 [low] Figure spec: The stripping line is plotted up to x ≈ 0.66, well past P at x = 0.40. Above the feed the operating line in use is the rectifying line, so the extra segment can make a reader think the stripping line applies there.
- ch 5 [low] Figure caption (and Section 3 / Lead): The caption gives the optimum range as '1.3 to 1.5 times R_min', while the lead and Section 3 give '1.2 to 1.5', and the plotted minimum sits at about 1.3 R_min. Three slightly different ranges in one chapter confuse a reader about which rule to quote in an exam.
- ch 5 [low] Section 2 (minimum reflux): The formula R_min = (x_D - y_F*)/(y_F* - x_F) is presented as the general R_min for a saturated-liquid feed. It is the true R_min only when the pinch lies on the q-line, that is, at the point (x_F, y_F*). With strongly non-ideal equilibrium curves the pinch can be a tangent point elsewhere and this formula gives too low a value.
- ch 5 [low] Quiz Q2 answer: 'Operating line slope R/(R+1) rises toward diagonal' mixes two ideas: the slope rises toward 1, and the line moves toward the diagonal y = x. A student may write the slope becomes equal to the diagonal, which is not meaningful.
- ch 5 [low] Section 1, last sentence: 'That balance matters.' is filler and carries no information.
- ch 5 [low] Section 3, last paragraph: The sentence 'Only a few universities teach this topic in detail' is vague and unverifiable, and it sits oddly next to a full section and a worked example on the same topic.
- ch 6 [low] Section 2, construction steps 4–5: The difference point ΔD and the reflux liquid point share the same abscissa xD, so the joining line is vertical. Step 4 tells the student to 'extend the line to cut the H curve', which will look like a mistake on the graph, and the text never says what the cut means here.
- ch 6 [low] Section 2, first paragraph: 'When HV and hL do not change from tray to tray, the balance gives the ordinate of ΔD' suggests the formula needs constant enthalpies. It does not: V·HV − L·hL is the same for every envelope taken from a tray up to the condenser, so the top values alone fix ΔD even when the H and h curves slope.
- ch 6 [low] Section 3: 'For a liquid point (x, hL), the line from ΔD cuts the H line at the y-x operating line' is garbled — a line cuts a curve at a point, not at another line.
- ch 6 [low] Quiz Q1: The question calls the vapour curve the 'H-x curve', but on that curve H is plotted against vapour mole fraction y, not x. The answer corrects it, the question does not.
- ch 6 [low] Figure: The figure draws both H and h as horizontal lines (50 and 20 kJ/mol). That is exactly the equal-latent-heat case in which the method collapses to McCabe-Thiele, so the reader cannot see why the difference point is needed.
- ch 7 [low] Figure: The caption says 'a packed column replaces the trays with a bed of packing', but the diagram and its aria description contain only the tray column, so the figure promises something it does not show.
- ch 7 [low] Section 1, sieve tray bullet: 'a narrow range of vapour rates before liquid weeps through the holes' can be read as weeping happening at high vapour rate. Weeping is a low-rate limit; the high-rate limits are entrainment and flooding.
- ch 7 [low] Worked example 1: Eo = 0.60 and EM = 0.70 are given in the same data set with no comment, so a student may use 0.70 to count trays or think the 0.60 applies to the single tray. The two numbers come from different sources.
- ch 7 [low] Section 3, Eo formula: The definition does not say that Nt and Na must be counted on the same basis (both excluding, or both including, the reboiler and condenser). Mixing bases gives a wrong tray count.
- ch 8 [high] Exam traps, last bullet: The trap says substituting mole fractions for d and b in Fenske is safe 'only when D = B'. This is wrong. In the product (dLK/bLK)(bHK/dHK) the factors D/B and B/D always cancel, so the mole-fraction form (xD,LK xB,HK)/(xB,LK xD,HK) is exact for any D and B. The chapter's own worked example uses D = B, which hides this and reinforces a false rule.
- ch 8 [low] Exam traps, first bullet: 'Fenske and Underwood use each component's αi' is misleading. Fenske uses only the single value αLK-HK; only Underwood needs every component's αi. A student may start hunting for αi of all components to do Fenske.
- ch 8 [low] Section 4: N is a count of theoretical stages and normally includes the reboiler as one stage, so dividing N itself by the tray efficiency overcounts trays by one.
- ch 9 [high] Figure (block diagram) — solvent recovery node and bottom stream: The diagram shows the stream leaving the bottom of the solvent-recovery column as 'Bottoms: water-rich'. The extractive solvent is the high-boiling component, so in the recovery column it is the solvent that leaves at the bottom (and is recycled); water leaves at the top as the distillate. As drawn, the diagram contradicts Section 3, which says the lean solvent is recovered and recycled to the top of the extractive column.
- ch 9 [low] Quiz Q6: The stem says 'At an azeotrope, yi/xi = 1.2 and yj/xj = 1.2', but at an azeotrope yi = xi, so yi/xi = 1, not 1.2. A student will read this as contradicting Q1 and Section 1.
- ch 9 [low] Section 2: 'an entrainer can form a low-boiling azeotrope rich in ethanol or water depending on the choice' is vague and can mislead: in the usual industrial ethanol dehydration the entrainer (benzene, cyclohexane, pentane) forms a low-boiling, often heterogeneous azeotrope that is mostly entrainer and carries water overhead, so ethanol leaves at the bottom.
