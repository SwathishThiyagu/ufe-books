# au-elec-u1: free-model run

- Book: `books/auto/au-elec/au-elec-u1.html`
- Status: ok
- Model calls so far: 32 (112,490 tokens in, 217,003 out), 5.9 minutes

## Checker

```
au-elec-u1.html: 9 chapters, 16096 words, 10 figures, 171 KB
OK
```

## For the reviewer

- chapter 9: the figure cannot be drawn: tree label "Power distribution" is too long; shorten it
- chapter 9: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, paragraph 2: The sentence 'The industry moved to a 12 V nominal bus, which gives about 14.0 V when charged' can be read as saying the 12 V battery itself sits at 14.0 V, which contradicts the exam trap later in the chapter.
- ch 1 [low] Section 2, paragraph 1: 'Europe set Euro I to Euro V and later steps' is loose: it mixes Roman numerals with 'later steps' and skips that the Euro stages began in the early 1990s, not the 1970s where the paragraph starts.
- ch 1 [low] Section 3, paragraph 1: 'It also enables on-board diagnostics (OBD-II)' overstates the link. OBD-II existed before CAN; CAN is only one of the protocols OBD-II allows, though it became the required one for new cars in the US from 2008.
- ch 1 [low] Section 1, paragraph 2: 'Some syllabi call this topic electronics in automotive and its evolution' is vague and sits in the middle of a technical paragraph about bus voltage, breaking the flow.
- ch 1 [low] Figure, node c: The single node 'Dynamo and 12 V' merges two separate changes. Moving from 6 V to 12 V was one change; the alternator came later, as node d shows, and readers may think 12 V arrived only with the alternator.
- ch 2 [high] Section 2 (plates) and Quiz Q4: Plante plates are described as 'thin'. In standard construction the Plante plate is a thick, solid cast lead plate, formed by cycling; its thickness and pure lead are exactly why it lasts long but stores little energy per kilogram. Calling it thin contradicts the textbooks and the reason given for its low energy density.
- ch 2 [low] Section 4 (gassing) and Exam traps: The per-cell figure and the whole-battery figure do not match: 6 × 2.3 V = 13.8 V, not 14.1 V. A student who multiplies will get a different number from the one printed.
- ch 2 [low] Section 1, third paragraph: 'Series connection also lets the pack deliver the very high cranking current' is misleading. Series connection raises voltage, not current capability; the hundreds of amperes come from the large plate area and the few milliohms of internal resistance.
- ch 3 [high] Section 3, maintenance-free designs, second paragraph: Saying a maintenance-free battery 'is not sealed against all pressure; most have a valve' mixes two different products. A flooded maintenance-free (low-water-loss) battery is simply vented; a pressure-relief valve is the defining feature of VRLA (AGM/gel) batteries, which the chapter itself explains two paragraphs later. A student will conclude that every maintenance-free battery is a VRLA.
- ch 3 [low] Section 3, lead-calcium paragraph: 'Replace some antimony with calcium' is loose. Standard lead-calcium grids use essentially no antimony; antimony is removed (or kept very low in hybrid designs) and calcium is added to the alloy.
- ch 3 [low] Section 2, open-circuit voltage paragraph: 12.0 V on a rested battery is roughly a quarter charge, not 'deeply discharged'; calling it deep discharge exaggerates and hides the 12.2 V half-charge step.
- ch 3 [low] Section 2, charging-system test: 'Measure the bus' is jargon an ESL reader will not follow; the quantity to measure is not named.
- ch 3 [low] Figure caption and plot: The figure says 'same load' but never states the current, and a good battery held above 10.5 V for 600 min at 25 A would give 250 Ah, far beyond any car battery. Without a stated current the curve cannot be tied to the reserve-capacity definition just taught.
- ch 3 [low] Exam traps, fifth bullet: 'Do not load-test a sealed AGM below its safe voltage' is vague; the student is not told what the safe limit is, and the point is really about depth of discharge, not about the test itself.
- ch 5 [low] Figure and Section 3 description: The plotted curve rises from 0 A at 0 rpm (about 5.9 A at 100 rpm, 26 A at 500 rpm). This contradicts the text just above it, which says the alternator cannot charge below cut-in speed. A student will believe current flows at any speed, and the caption's 'knee' does not exist in the drawn curve.
- ch 5 [low] Section 3, flat-top explanation: 'The flat top appears because the voltage regulator reduces field current' can be misread as: less field current directly reduces output current. The regulator reduces field current to hold the terminal voltage constant; the current stops rising because stator reactance (which grows with speed) and the diode ratings limit it.
- ch 5 [low] Section 1, Faraday's law formula note: 'The minus sign gives Lenz's law' is too terse for a reader meeting the formula for the first time.
- ch 6 [low] Section 2, last paragraph: The sentence "Some syllabi call these regulator circuits 'voltage regulations versions'" is garbled and carries no meaning; a reader cannot tell what it refers to.
- ch 6 [low] Lead: The lead says the regulator holds the bus near 14 V at idle with headlights and battery charging, but Q4 of the same chapter shows 13.2 V at idle with headlights on. The two statements pull against each other.
- ch 6 [low] Section 1, power balance formula: P_mech is defined as 'brush, bearing and fan loss', but brush loss was already given its own symbol P_brush just above. A student cannot see where P_brush enters the balance.
- ch 7 [low] Section 3: The feedback sentence says that lower terminal voltage 'reduces speed, which raises current and deepens the sag'. The logic is circular and can mislead a student: at a lower terminal voltage the motor current at a given speed falls, and current rises only because the back-emf falls with speed. As written it reads as if a lower voltage directly pushes the current up.
- ch 7 [low] Section 3: 'This is why poor terminals or a flat battery prevent cranking' mixes two different mechanisms. A flat battery acts through internal resistance (the sag described by V = E − IRint). Poor or corroded terminals add resistance outside the battery in the starter cable circuit, so the voltage reaching the starter falls even though the battery's own terminal voltage may sag less.
- ch 7 [low] Quiz Q2: The answer supports a rise in resistance torque with a power argument ('work per second increases'). Power rising with speed does not by itself explain a rise in torque, and a student may repeat this loose link.
- ch 7 [low] Figure: The chart description gives only the end points and the 200 rpm starter value. It leaves out the intersection at 275 rpm and 37.5 N·m, which is the main point of the figure, and the 30 N·m resistance value at 200 rpm.
- ch 8 [high] Section 3, first paragraph and the key-turn sequence: The control circuit is said to carry 'a few amperes', but three lines later the same circuit carries the pull-in and hold-in coils at 'about 40 A in total' (and about 10 A when held). A student is left with two contradictory current values for one conductor. 40 A is not a few amperes, and that coil current flows through the terminal 50 line, the relay contact and any safety switch in it.
- ch 8 [low] Section 3, second bullet of the key-turn sequence: 'Battery voltage reaches terminal 50 of the starter relay coil' mixes two nodes. Terminal 50 is the starter control line at the solenoid. The relay coil is fed from the ignition switch (terminal 15 side), and the relay contact feeds terminal 50 of the solenoid.
- ch 8 [low] Quiz Q7: 'Four starter motor arrangements' is ambiguous, because the chapter also describes four drive arrangements (Bendix, pre-engaged, overrunning clutch, armature shift). A student cannot tell which list is wanted.
- ch 8 [low] Worked example 1, step 4 and answer: The power is found from the terminal voltage at the starter (10.5 V) and is then called 'energy taken from the battery'. The battery actually supplies more, because of its internal resistance and the cable drop; 5250 J is the energy delivered to the starter.
- ch 9 [high] Worked example 1, step 4 (and the matching sentence in Section 2: 'The spark plug gap ionises at a breakdown voltage; the remaining voltage drives the arc'): The subtraction treats the 8 kV breakdown as a series drop and says 27 kV is left to drive the arc. In reality the secondary voltage rises only until the gap ionises (about 8 kV here) and then collapses to the arc voltage, which is a few hundred volts; the arc current comes from the energy stored in the coil, not from a 27 kV driving voltage. A student will wrongly believe a 27 kV arc burns across the plug.
- ch 9 [low] Quiz Q5: The answer uses 4 A both before and after adding 0.25 Ω. Once the wire drop is added the current falls (about 3.7 A for a 3 Ω lamp), so the true drop is about 0.9 V and the lamp sees about 11.1 V, not exactly 1 V and 11 V.
