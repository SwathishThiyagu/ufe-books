# e-bee-u1: free-model run

- Book: `books/common/e-bee/e-bee-u1.html`
- Status: ok
- Model calls so far: 29 (106,768 tokens in, 196,949 out), 5.2 minutes

## Checker

```
e-bee-u1.html: 9 chapters, 18334 words, 10 figures, 169 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Lead and figure (resistor arrow labelled 'no change'): 'A resistor keeps a voltage drop' is misleading: a resistor only has a drop when current flows through it. Worked example (c) itself has 0 V across the 5 Ω resistor, which contradicts the sentence and the figure label 'no change'.
- ch 1 [low] Section 1 lead sentence of the chapter: 'A circuit is a network of three ideal elements: resistance, inductance and capacitance' leaves out sources, yet Section 3 and every worked example need a source. A student can read this as saying circuits contain only R, L and C.
- ch 2 [low] Section 1, v–i plot paragraph: The reasoning 'both are straight lines, so both are linear elements' is loose. A constant characteristic v = V or i = I is a straight line but not a proportional (through-origin) relation, and the phrase 'superposition works with them' sits next to sources in general, before dependent sources are introduced, so a student may conclude that a dependent source can be switched off in superposition — which the chapter itself later forbids.
- ch 2 [low] Section 1, practical source: Only the series form of a practical source is given. The parallel form (ideal current source in parallel with R_p, terminal current I_t = I − V_t/R_p) is missing, yet it is exactly what source transformation in Chapter 1.5 needs.
- ch 2 [low] Section 2, dependent source description: 'It has two output terminals like any source, plus a controlling pair' suggests a four-terminal device. The standard diamond symbol is a two-terminal element; the controlling voltage v_x or current i_x belongs to some other branch of the circuit and is only labelled next to the diamond.
- ch 2 [low] Section 2, closing sentence: 'These four elements are the only way to write a transistor or an op-amp as a circuit element' overstates it. Small-signal models use dependent sources together with resistors and capacitors, and large-signal or behavioural models use other constructions.
- ch 2 [low] Exam traps, fourth bullet: 'Mixing r and g gives an answer off by a factor of ohms squared' is not meaningful. r (Ω, V/A) and g (S, A/V) are reciprocal units, so a slip gives an answer with wrong units, not one wrong by a fixed factor of ohms squared.
- ch 3 [low] Quiz Q1: The question asks for two conditions under which Ohm's law applies, but the second item, 'the element is bilateral', is a property that follows from Ohm's law, not a condition for it. A student listing bilateral as a condition gives a loose answer.
- ch 3 [low] Worked example 1, step 6: The units are dropped in the middle of the calculation: 'P₂ = 4 × 3 = 12 W' writes I² as a bare 4 with no unit, so the reader cannot see that 4 is in A².
- ch 3 [low] Section 3 (power balance paragraph): The sentence 'If absorbed power is positive, a source delivering power is negative, so ΣP = 0' is compressed and easy to misread, because the first clause states a condition rather than the convention being used.
- ch 4 [high] Section 3, short branch: The sentence says 'any element in series with that short is bypassed — no current through it, no voltage across it'. This is backwards: the elements that lose their current are the ones in parallel with the short (the shunted group). An element in series with the shorted section still conducts, and in fact carries a larger current because the total resistance has fallen.
- ch 4 [low] Section 3, open branch: 'every other branch value changes' is too strong. If the opened branch sits directly across an ideal voltage source, the other parallel branches keep the same voltage and the same current.
- ch 4 [low] Quiz Q3, answer: 'The group with one branch removed would equal the smallest branch' is only true when the group has exactly two branches. For three or more branches, removing one still leaves a group larger than the smallest branch.
- ch 4 [low] Section 1: Conductance is introduced as G = 1/R but its unit is never given, while every other symbol in the chapter carries a unit.
- ch 5 [high] Exam traps, trap 1 (reversing the current-source arrow): The sentence contradicts itself. A voltage source drives current through the outside circuit out of its + terminal and back to its − terminal. The arrow inside the equivalent current source points from − to +, which is the opposite spatial direction to the current in the outside circuit. Telling a student the arrow must 'point the same way the voltage source drove current through the outside circuit' invites exactly the reversal this trap is warning about.
- ch 5 [low] Section 1, bullet on pointing the arrow: 'Point the arrow inside the current source from − to +; that is the direction it pushes current through the outside circuit' reads as if the internal arrow and the external current are the same direction. They are not; the external current leaves the + terminal and runs back to −.
- ch 5 [low] Quiz Q6 (why convert a star to a delta in a bridge): The stated reason is weak and can mislead. The standard bridge simplification is delta-to-star: the delta is replaced by a star, which breaks the loop and gives series-parallel branches. Converting a star to a delta usually adds a mesh and rarely helps reduction, so 'this is why we convert' teaches the less useful direction.
- ch 6 [low] Section 1 and Quiz Q1: The chapter says a mesh current is a real branch current only in branches 'on the outer edge'. That is not the criterion. The criterion is a branch that belongs to one mesh only. A branch that is not shared with another mesh (for example a dangling branch attached to an interior node) carries the mesh current but is not on the outer edge of the drawing.
- ch 6 [low] Exam traps, fourth bullet: 'the real current is the difference (or sum) of the two mesh currents' contradicts the rule stated earlier. With all mesh currents drawn clockwise, the two contributions in a shared branch always oppose, so the branch current is always the difference.
- ch 6 [low] Section 4, first sentence: 'write them as a resistance matrix times a current vector equals a source vector' is true only for mesh analysis. Node analysis gives a conductance matrix times a node-voltage vector equals a current-source vector.
- ch 6 [low] Figure spec: With show_index true and index_from 1, the mark key '1' points at the first column, so the accent falls on 6 in row 1 and on −4 in row 2. The caption says the accent is on the two shared 4 Ω terms, which are in the second column.
- ch 6 [low] Lead: 'Every circuit simulator builds these same matrices internally' overstates the case: simulators use node-based modified nodal analysis, not mesh analysis, as the Beyond note itself says.
- ch 7 [high] Section 1, 'Why it exists' paragraph: The sentence 'three sources mean three unknowns in a nodal or mesh solution' is false. The number of unknowns equals the number of independent node equations (nodes minus one) or mesh currents, which has nothing to do with how many sources the circuit contains. A student can carry this wrong rule into the exam.
- ch 7 [low] Section 3, sentence after the power formula: It says 'The cross term 2I′I″ is the part that the addition of powers misses.' The quantity 2I′I″ is a current squared, not a power; the missing power is 2I′I″R. Q4 states it correctly, so the two places disagree.
- ch 8 [high] Section 3, load line paragraph: The section first defines the load line as the line from the Thevenin side, V = Vth − I Rth. It then says 'Change RL and only the load line changes', which reverses that definition: the load line is fixed by Vth and Rth, and it is the load's own V–I characteristic (V = I RL) that changes when RL changes.
- ch 8 [low] Quiz Q7, answer: The answer says 'The load is part of the resistance seen at the terminals', which clashes with the chapter's own warning that Rth is not the resistance of the circuit including the load. The load is outside the network; it only corrupts Rth if it is left connected while measuring.
- ch 8 [low] Section 2, first paragraph: The text says 'as in Chapter 1.5' but gives no link, so the phone reader cannot jump to that chapter.
- ch 9 [low] Figure caption: The caption says the curve is 'zero at both ends', but the plotted axis stops at R_L = 12 Ω where the curve is still about 24.5 W. A student comparing caption with the drawn curve sees a contradiction; only the left end is truly zero.
- ch 9 [low] Quiz Q3: The answer justifies R_L = 0 Ω with 'P = V²/R is zero', but at R = 0 this expression is 0/0, not zero. A careful student is left with an undefined quantity.
- ch 9 [low] Section 3, paragraph starting 'V_th and R_th may include dependent sources': V_th and R_th are numbers, not networks, so they cannot 'include' sources. Only the network behind the terminals can contain dependent sources. As written, a student may think the Thevenin equivalent itself is not a plain source-plus-resistor.
- ch 9 [low] Quiz Q6 answer: 'The 10 Ω load is below maximum' is ambiguous: 10 Ω is above the matched value 5 Ω, though the power 4.44 W is below the maximum 5 W.
