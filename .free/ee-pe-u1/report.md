# ee-pe-u1: free-model run

- Book: `books/eee/ee-pe/ee-pe-u1.html`
- Status: problems
- Model calls so far: 32 (118,373 tokens in, 276,301 out), 10.4 minutes

## Checker

```
ee-pe-u1.html: 9 chapters, 16668 words, 10 figures, 170 KB
PROBLEMS:
 - chapter "ratings-snubber-circuits-and-gate-drive-circuits": 2091 words is too long (keep under 1900; 900-1600 is the target)
```

## For the reviewer

- chapter 4: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [low] Figure: The plotted turn-off waveform is not triangular: it falls from −8 A at 2.2 μs to −2 A at 3.2 μs and then to 0 at 4.0 μs. The negative area of this plot is about 6.6 μC, while the worked example and the formula Qrr = ½ IRRM trr give 8 μC for the same 8 A and 2 μs. A student who measures the area under the figure will not get the example answer.
- ch 1 [low] Section 1, static V–I curve: VF is used for two different things: the cut-in voltage (0.8 V to 1.2 V) and the intercept of the linear model vD = VF + iD rd. In a silicon power diode the cut-in is nearer 0.6 V to 0.8 V; 1 V to 1.2 V is the full on-state drop at rated current, which already includes the iD rd part.
- ch 1 [low] Section 1, comparison with an ideal switch: 'A real diode fails all four: it has VF, finite rd, leakage IS, breakdown VBR, and stored charge that delays turn-off' does not map cleanly onto the four ideal properties. rd is part of the on-state behaviour, not a separate failure, and the idea of finite resistance is not one of the four listed properties.
- ch 1 [low] Section 3, diode types and converter map: The other units are named in plain text ('See Unit 2, Controlled and Uncontrolled Rectifiers'), not as links, so a student reading on a phone cannot tap through to them.
- ch 2 [high] Lead: "It blocks voltage in both directions until a small gate pulse starts conduction" says a gate pulse can end reverse blocking. A gate pulse cannot turn on an SCR whose anode is negative; reverse blocking is broken only by reverse breakdown, which damages the device.
- ch 2 [low] Section 1: "The device is a three-terminal, four-layer switch even though the drawing has four layers" is confusing: the drawing and the device both have four layers. The sentence adds no information and suggests a mismatch.
- ch 3 [low] Section 1, closing sentence: The sentence 'the other four are either slow, destructive or accidental' lumps light triggering with the unwanted ones. Light triggering is a deliberate, precisely timed method used in HVDC valves, so a student may conclude light turn-on is always an accident or a fault.
- ch 3 [low] Section 3, RC triggering bullet: 'when the control switch closes, the capacitor discharges into the gate through a resistor' is vague. Most exam RC trigger circuits have no switch at all: the capacitor charges through R from the supply and dumps its charge into the gate-cathode path when the circuit conditions allow, giving one sharp gate current spike per cycle.
- ch 3 [low] Exam traps, second bullet: 'A 1.05 W pulse in a 0.25 W resistor can still fail if the pulse is long or repeated fast' is loose: the resistor rating is an average (continuous) rating, so a short pulse above it is normally safe and failure comes from average power or pulse energy, not from the peak alone.
- ch 4 [low] Section 1, first paragraph: "Gate current starts regeneration" uses an unexplained word. A student who has not yet met the two-transistor model will not know what regeneration means here.
- ch 4 [low] Section 2, tc formula: tc = C × V / I silently assumes the load current stays constant at I while the capacitor charges or discharges. Without that assumption the formula does not follow, and students will apply it to circuits where the current changes.
- ch 4 [low] Beyond: "Wide band-gap devices have short tq" is loose. tq is a thyristor datasheet quantity; MOSFETs and IGBTs are not thyristors and are turned off from the gate, so they do not have a tq in this sense.
- ch 5 [low] Figure (TRIAC equivalent), edge from MT1 to SCR2: The edge MT1 → SCR2 is labelled 'reverse', but in the negative half-cycle MT1 is positive with respect to MT2, so SCR2 is forward biased and conducting. The label contradicts the text and can make a student think SCR2 works in reverse.
- ch 5 [low] Lead: 'A TRIAC and a DIAC together make a simple bidirectional AC switch' can be read as if the DIAC is in the load path. The DIAC only delivers the gate pulse; the TRIAC alone carries the load current.
- ch 5 [low] Worked example 1, step 4: The power does not follow from the rounded voltage shown in step 3: (162.6)²/100 = 264.4 W, not 264.5 W. The 264.5 W value needs the unrounded 162.63 V.
- ch 6 [low] Section 1, cut-off sentence: "In cut-off the base is open and no current flows" is loose. An open base still leaves a leakage current (I_CEO, roughly (1+β) times the collector-base leakage), and opening the base is not how a power BJT is held off in a converter; hard cut-off uses a reverse base-emitter bias to sweep out stored charge quickly.
- ch 6 [low] Section 3, end of second paragraph: "The gate still needs only a short charge pulse" can be read as: pulse the gate and leave it floating. The IGBT needs a sustained gate voltage while it conducts; only the current is transient, delivered at each switching edge.
- ch 6 [low] Section 3, selection paragraph: "IGBT loss is V_CE(sat) × I plus a small resistive part, a line with an offset" mixes two graphs. The loss-versus-current curve P = V_CE(sat) I passes through the origin; the offset belongs to the output characteristic V = V_CE(sat) + I R, not to the loss curve.
- ch 6 [low] Lead: "Choosing between them is mostly a question of conduction loss at your operating current" is too strong. Blocking voltage, switching frequency (the IGBT tail, the MOSFET's fast body diode) and gate-drive complexity decide the choice as much as conduction loss.
- ch 6 [low] Table, IGBT row: The column is headed "Main loss" and gives conduction formulas for the BJT and MOSFET, but for the IGBT it adds "+ tail", which is a switching loss. A student may compare the three rows as if they were the same kind of quantity.
- ch 7 [low] Section 1, dynamic ratings paragraph: The paragraph says 'Two dynamic ratings decide protection' and then lists three items: di/dt, dv/dt and gate charge Qg. Qg is not a protection limit; it is a drive requirement.
- ch 7 [low] Section 1, surge current definition: ITSM is described as 'the single 50 Hz half-cycle current'. The datasheet value is a peak current; without the word peak a student may use an RMS or average value.
- ch 7 [low] Section 1, di/dt definition: The text presents di/dt as a rating on 'anode or drain current'. A MOSFET has no datasheet di/dt rating for drain current; the drain-current rise is set by the gate drive and circuit. The di/dt rating is mainly a thyristor/SCR rating (MOSFETs have body-diode di/dt and dv/dt limits).
- ch 7 [low] Section 2, resistor rating sentence: 'The resistor must be rated for this continuous pulse power, not its average DC value alone' is confusing and contradicts itself. The continuous rating of a resistor is its average power rating; the pulse/overload rating is a separate short-time check.
- ch 7 [low] Exam traps, trap 2: 'The R-C turn-off snubber is useless without Rs' overstates the point and conflicts with Section 2 and Q4. Cs alone still limits dv/dt at turn-off; the danger is the huge turn-on discharge current through the switch.
- ch 7 [low] Section 3, peak gate current formula and Quiz Q6: The formula and Q6 use VGE (gate-emitter voltage) for a MOSFET. MOSFET datasheets use VGS (gate-source voltage); VGE is the IGBT term.
- ch 8 [high] Section 1, paragraph after the P_sw formula: "Faster switching reduces P_sw" reads as if raising f_s lowers P_sw, and it sits directly above "Switching loss rises linearly with f_s". A student will read the two lines as a contradiction.
- ch 8 [low] Section 2, first paragraph: "I is average current in amperes" is ambiguous: if I is already the average over the whole period, multiplying by D counts the off-time twice. The same ambiguity appears in the MOSFET line with I_rms.
- ch 8 [low] Section 3, second paragraph: "Some syllabi call the heat-sink-to-ambient resistance Rθ_SA" repeats the symbol just defined and carries no information; the reader looks for a second name that never comes.
- ch 8 [low] Exam traps, first bullet: "Using one edge halves the answer" is only true when t_on = t_off; in the worked example (1 μs and 2 μs) dropping t_off leaves one third, not one half.
- ch 9 [low] Section 1, formula: The formula uses E_c in V/cm, but the preceding text gives E_c in MV/cm. A student may plug in 2.2 instead of 2.2×10⁶, giving a thickness that is a million times too large.
- ch 9 [low] Section 3, last sentence: The sentence 'Only a few universities teach this at device level' is filler and adds no technical value. It also sounds like an unsupported claim.
