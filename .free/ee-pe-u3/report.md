# ee-pe-u3: free-model run

- Book: `books/eee/ee-pe/ee-pe-u3.html`
- Status: ok
- Model calls so far: 31 (135,821 tokens in, 341,945 out), 12.5 minutes

## Checker

```
ee-pe-u3.html: 8 chapters, 16118 words, 9 figures, 163 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, step-down (buck) bullet: The sentence reads "Step-down (buck) chopper: Vo s." — the comparison sign has dropped out, so the defining condition of a buck chopper is missing and the text is unreadable.
- ch 1 [high] Section 1 (output power formula) and Worked example 1, steps 5 and 8: The chapter calls the load "a 10 Ω resistor" (pure resistance, only a freewheeling diode, no inductor), yet uses Po = Vo·Io = D²·Vs²/R. For a purely resistive load fed by pulses, the average power is D·Vs²/R = (1/T)∫v²/R dt, not Vo·Io, because voltage and current are not smooth. So 640 W at D = 0.4 and 2560 W at D = 0.8 are wrong for a pure resistor; the true values are 1600 W and 3200 W. The D²·Vs²/R result is correct only when an inductor keeps the load current continuous, so that Io = D·Vs/R is a smooth DC current.
- ch 1 [low] Section 2, current-limit control bullet: "ripple current is larger" is vague and not generally true: the ripple is set by the band Imin to Imax chosen by the designer, and that band can be small.
- ch 1 [low] Quiz Q7 answer versus Section 2: Q7 lists "spread-spectrum EMI" as a gain of variable-frequency control, while Section 2 lists the widened noise band as a cost (harder to filter, harder to clear for EMI). The two statements pull in opposite directions.
- ch 1 [low] Beyond: "Peak current-mode control ... sits inside almost every switching regulator IC" overstates it; many regulator ICs use voltage-mode or constant on-time control.
- ch 2 [high] Figure caption: The caption calls the 12 V input '12 V mains'. Mains in India is about 230 V AC; 12 V here is the DC bus/input after the rectifier and filter (or an adapter output). A student can take away that mains is 12 V.
- ch 2 [low] Worked example 1, step 7: The step shows 7 W / 0.882 W = 7.93, but dividing by the rounded 0.882 gives 7.94. The 7.93 comes only from the unrounded 0.8824.
- ch 2 [low] Worked example 1, answer line: 'has 7.93 times less loss' is ambiguous — it is the SMPS that has the smaller loss, but 'times less' reads as if it were the linear regulator.
- ch 2 [low] Quiz Q5: The question asks for two reasons, but the answer's first two clauses restate one idea (less energy/volt-seconds per cycle), and the last sentence about filter components is a third, unrelated consequence of raising fs, not a reason the transformer shrinks.
- ch 2 [low] Section 2, frequency paragraph: 'each pulse stores less energy' is loose for a transformer, which transfers energy rather than storing it; the correct idea is that the flux swing (volt-seconds) per cycle is smaller.
- ch 2 [low] Section 1, efficiency formula: The text says input current is Io plus the quiescent current, but then gives η = Vo/Vin, which ignores that quiescent current. The two statements should be reconciled.
- ch 2 [low] Section 1, first paragraph: The symbol β appears in 'a fraction βVo' without being defined.
- ch 3 [low] Lead: A mains phone charger or laptop adapter is normally an isolated flyback supply; the buck stage is inside the device (charging IC, motherboard voltage regulator), not inside the adapter. Listing 'phone chargers, laptop adapters' as places where a buck converter sits is loose and can mislead.
- ch 3 [low] Section 2 and design steps: Section 2 shows that a real diode changes the gain to Vo ≈ D·Vs − (1−D)·VD, but the design steps later say 'choose D = Vo/Vs' without remarking that this ignores the diode drop. A student will use the ideal value and then wonder why the built circuit gives a lower output.
- ch 3 [low] Section 2 (diode drop sentence): 'it hurts most at low Vo' is true but the reason is not given, and the same sentence would read more precisely in terms of D: the loss term is (1−D)VD, largest when D is small.
- ch 3 [low] Section 3 (output ripple): The ripple formula is said to assume only an ideal capacitor and CCM. It also assumes the load current is constant, so all of ΔIL flows in C, and that capacitor ESR is negligible (ESR is mentioned only afterwards).
- ch 3 [low] Section 3 (design steps): The design list covers L, C and the diode/MOSFET drop but never mentions the input capacitor, even though the buck input current is a pulse train of amplitude close to Io and needs a local input capacitor.
- ch 3 [low] Quiz 6: The synchronous buck answer does not mention that the low-side MOSFET conducts in both directions, so at light load the inductor current reverses unless diode emulation is used. The chapter teaches DCM for the diode version but leaves this gap for the synchronous version.
- ch 3 [low] Quiz 5: 'supplies the load during switching transitions' is vague; the capacitor actually supplies the part of the load current the inductor does not carry, and holds Vo during the off-time.
- ch 4 [high] Section 1 (circuit description) and the gain formula: The letter D is used for two different things in the same section: first as the name of the diode ('the anode of diode D', 'D is reverse biased', 'D goes to output capacitor C'), and then as the duty ratio ('D = Ton/T', 'Vo = Vs/(1 − D)'). A student can read D = 1 − Vs/Vo as a diode quantity, and cannot tell from the formula which D is meant.
- ch 4 [low] Section 3, cross-references: The pointers to other chapters are written as plain text ('See Unit 2 for PFC rectifiers and Unit 6 for battery and solar interfaces', 'see Chapter 3.5'), so they are not clickable on a phone, unlike the rest of the book.
- ch 5 [high] Section 1, switch ON paragraph: The sentence is corrupted: "Here D is the duty ratio (0 ≤ D s, the diode cathode is the highest voltage in the circuit, so the diode blocks." The definition of D's range, of T and f, and the description of node A being at Vs during the on-time have all been lost, so the paragraph no longer explains why the diode blocks.
- ch 5 [high] Section 1, switch OFF paragraph: The inductor current direction is reversed. L carries current from node A to the return rail while the switch is on, and the inductor keeps that same direction when the switch opens. Saying "it flows from the return rail up through L into node A" contradicts the circuit and the correct load path given two sentences later.
- ch 5 [high] Section 3, switch OFF state: With the diode from B to the return rail and the on-state condition "B sits at −VC1 and the diode blocks", the diode's anode is at B and its cathode at the rail. When it conducts it clamps B to about zero (one diode drop above the return rail), not to Vo. The stated clamp voltage is wrong, and it also contradicts the L2 volt-second balance that follows, which only gives Vo = −Vs·D/(1 − D) if B is at zero during the off-time.
- ch 5 [low] Section 3, circuit description: The Cuk diode orientation is never stated, although the buck-boost diode orientation is. Without it the reader cannot tell which way B is clamped, and the on-state sentence "B sits at −VC1 and the diode blocks" only works for one orientation.
- ch 5 [low] Section 3, off-state description: "The current of L1 flows through C1 and the diode into L2 and the load" mixes two paths: the diode current goes to the return rail, and only the L2 part reaches the load.
- ch 5 [low] Section 2, "Pulsed input current": The input capacitor is discussed, but it is not part of the circuit described in Section 1 (source, switch, inductor, diode, output capacitor, load). A student may look for it in the schematic and not find it.
- ch 5 [low] Section 3, "The price is two inductors...": "C1 carrying the full power as a large alternating current" is loose phrasing: a capacitor carries current, not power, and the point being made is the current stress.
- ch 6 [low] quiz Q2 answer: The phrase 'the secondary voltage has the opposite polarity for conduction' is vague. A student can read it as the secondary voltage being negative during ON, or as some conduction condition, instead of the simple fact that the dot end is negative so the diode is reverse biased.
- ch 6 [low] section 2, reset winding paragraph: The paragraph explains the reset time but never states the consequence for the switch: with a 1:1 reset winding the switch holds about 2·Vs in the off-time, so the device rating must be chosen for roughly twice the input voltage.
- ch 6 [low] worked example 1, step 5 and answer: 'A 150 V device leaves margin' uses only the ideal stress and drops the leakage spike that the same chapter says the clamp must absorb. As written, the example suggests the rating follows from Vs + n·Vo alone.
- ch 6 [low] section 3, last paragraph: 'both trade a duty limit and isolation against a non-isolated buck' is unclear: it is not stated what is traded for what, and the flyback's 'duty limit' is not the same kind of limit as the forward's D < 0.5.
- ch 7 [low] Figure and its caption: The turn-off does not show ZCS. The gate pulse bar ends at 7.5 µs while the switch-current lane still shows 5 A up to 7.5 µs, and the current only reaches 0 A at 8 µs, when the voltage rises. Section 2 states the opposite rule: a resonant pulse brings the switch current to zero before the gate is removed. As drawn, the gate is removed while 5 A flows and the current then falls with the voltage still at 0 V, which is a capacitive (ZVS-type) turn-off, not a ZCS turn-off.
- ch 7 [low] Section 1, note after the P_sw formula: "The ½ assumes a triangular voltage-current overlap" can be read as voltage and current ramping together over the same interval. If both ramped together the energy would be V·I·t/6, not ½·V·I·t. The ½ in the standard formula comes from one quantity ramping while the other stays fixed.
- ch 7 [low] Section 3, paragraph on frequency control: "Moving f_s away from f_0 lowers the gain" is true only above resonance. Below f_0 an LLC gain curve rises above 1 to a peak before dropping, and that boost region is exactly how the converter holds output when the input sags. The sentence as written hides this.
- ch 8 [high] Exam traps, trap 5: The trap says that leaving Ae in cm² or L in µH makes N "come out wrong by a factor of ten". The error is far larger. Ae in cm² instead of m² makes N too small by 10⁴ (1 cm² = 10⁻⁴ m²). L in µH instead of H makes N too large by 10⁶. Even using both wrong units together gives a factor of 10², not 10.
- ch 8 [low] Worked example 1, step 6 and answer: The chapter's own rule is that strands must be thinner than about 0.4 mm (twice the 0.21 mm skin depth), but step 6 recommends "about six strands of 0.45 mm", which breaks that rule.
- ch 8 [low] Section 1, air-gap paragraph: "An ungapped ferrite core saturates at a small current however few turns you use" overstates the case. For an ungapped core the saturation current is Isat = Bmax·Ae·Rc/N, so it rises as the turns fall. What really fails is that a low turn count also makes L far too small.
- ch 8 [low] Section 2, core loss paragraph: "Keep the peak below about 0.3 T at 100 kHz" presents 0.3 T as a working limit at that frequency. 0.3 T is the ferrite saturation limit at any frequency; at 100 kHz, core loss usually forces the peak flux well below it, often 0.10 to 0.15 T.
- ch 8 [low] Quiz Q7 (flyback on an ungapped core): "The primary current ramps slowly and the core saturates early" mixes two ideas: a large magnetising inductance makes the ramp slow, which delays saturation in time. The real failure is that with no gap the saturation current Isat = Bmax·Ae·Rc/N is very small, so the core saturates at a low current.
