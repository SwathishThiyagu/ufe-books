# ec-analog-u1: free-model run

- Book: `books/ece/ec-analog/ec-analog-u1.html`
- Status: ok
- Model calls so far: 34 (134,049 tokens in, 296,433 out), 7.9 minutes

## Checker

```
ec-analog-u1.html: 8 chapters, 14648 words, 9 figures, 153 KB
OK
```

## For the reviewer

- chapter 6: the figure cannot be drawn: note "small drop" runs off the right edge; shorten it

## Reviewer notes (after any revision)

- ch 1 [low] Exam traps, item 2: The wording is misleading. It says subtracting the drop 'after division gives the wrong answer', but algebraically (Vm − Vd)/π = Vm/π − Vd/π, so subtracting Vd/π after the division is exactly right. A student can read this and think any post-division subtraction is forbidden.
- ch 1 [low] Section 2, first paragraph: 'The DC output doubles' is unqualified. It is true only when the peak per half-winding Vm is the same as the half-wave peak. With one 12-0-12 transformer, using the whole 24 V winding in a half-wave circuit gives the same Vdc as the centre-tap connection.
- ch 1 [low] Beyond box: Silicon Schottky diodes have low reverse-voltage ratings, so they are not used in the bridge that sits directly on a 230 V mains (peak inverse about 325 V). There they are silicon or SiC parts; Schottky types appear on the low-voltage output side of the charger.
- ch 2 [low] Section 3, first paragraph: The shunt impedance is written as 1/(2πfC) where f was defined as the supply frequency. The ripple that the capacitor must bypass sits at the ripple frequency, which is 2f (100 Hz for a 50 Hz full-wave supply) and f for half-wave. A student may plug in 50 Hz and get a wrong impedance.
- ch 2 [low] Section 1, last bullet paragraph: The sentence 'This charge-discharge cycle repeats at f: twice per cycle for full-wave, once per cycle for half-wave' is ambiguous: for full-wave the recharge happens twice every supply cycle, so the cycle repeats at 2f, not at f.
- ch 2 [low] Figure spec, node c: The figure labels the discharge path 'through RL' while the text, formulas and worked example all use R for the load resistance. Two symbols for one quantity.
- ch 3 [high] Section 1, bullet list of clipper types: The bullets say the output is flat at +Vref (positive clipper) and at −Vref (negative clipper), but the formula box two lines above gives Vout = Vref + VD, and the chapter itself sets VD ≈ 0.7 V for silicon. A student following the bullets will report 4 V where the formula gives 4.7 V, so the two statements contradict each other.
- ch 3 [high] Figure (positive shunt clipper, 4 V reference): The plotted output is wrong between the breakpoints. The output series jumps straight from (0°, 0 V) to (45°, 4 V) and from (135°, 4 V) to (180°, 0 V). A sine of 10 V peak reaches 4 V at 23.6°, so the flat top must run from 23.6° to 156.4°. As drawn, the clipping starts at 45° (where the input is 7.07 V), which contradicts worked example 1, and at, say, 30° the plot shows about 2.7 V instead of the correct flat 4 V.
- ch 3 [low] Lead paragraph: 'Both use a diode as a switch and a battery or capacitor as a reference' suggests the capacitor is a reference source. In a clamper the capacitor stores the DC shift, and the reference is the ground (or battery) the diode is returned to.
- ch 4 [low] Quiz Q2, answer: The last sentence says "At a load of 27.3 mA, IZ reaches zero and regulation ends." Regulation actually ends much earlier, when IZ falls to the 5 mA knee (load about 22.3 mA). A student can read this as "the Zener still regulates down to IZ = 0", which contradicts the knee rule taught in Section 1 and used everywhere else in the chapter.
- ch 4 [low] Section 2, first formula block: IZ(max) is used in the inequality IZ(min) ≤ IZ ≤ IZ(max) before it is ever defined. IZ(min) is defined in Section 1 (knee current), but nothing in the text says what sets IZ(max).
- ch 5 [high] Exam traps, first trap: The arithmetic and the wording of the swapping trap are wrong. With R1 = 20 kΩ (upper) and R2 = 10 kΩ (lower), Vout = 5.6 × (1 + 20/10) = 16.8 V, not 8.4 V. The 2.8 V figure comes from an inverted formula (5.6 × R2/R1), not from swapping the resistors in the correct formula, so the sentence 'the other way round gives 2.8 V' does not follow from what precedes it and will confuse a student.
- ch 5 [low] Quiz Q3 answer: 'The divider ratio is 4.7 + 1 = 5.7' misuses the term. The divider ratio is the feedback fraction β = R2/(R1 + R2) = 1/5.7 ≈ 0.175. The number 5.7 is the gain factor 1 + R1/R2, i.e. the reciprocal of β.
- ch 5 [low] Section 2, dropout check bullet: 'about 0.3 V for a single BJT plus drive' is optimistic for a plain discrete series regulator, where the error amplifier runs off the same Vin and its output must sit one VBE above Vout. Only when the base (or gate) can be driven above Vin, as in an LDO with a PNP or PMOS pass device, does the figure fall to a few hundred millivolts.
- ch 6 [high] Section 1 (the formula Vout = Vref × (1 + R1/R2)): The R1/R2 naming contradicts Section 3. In Section 3, R1 is the resistor from OUT to ADJ (upper) and R2 is from ADJ to ground (lower), giving Vout = 1.25(1 + R2/R1). In Section 1 the same symbols are used the other way round, so a student who carries R1 (upper) = 240 Ω and R2 (lower) = 720 Ω into Section 1's formula gets 1.25 × (1 + 240/720) = 1.67 V instead of 5 V.
- ch 6 [low] Section 1 ("a temperature-stable bandgap reference of about 1.25 V"): 1.25 V is the LM317's OUT-to-ADJ voltage, and the chapter presents it as the reference inside the whole three-terminal family, including the fixed 78xx/79xx, where the internal reference value is different and not a standard textbook figure. A student may then 'derive' a 7805 divider using 1.25 V.
- ch 6 [low] Exam traps, second bullet: "not the mirror of the 78xx order" is ambiguous — the mirror of IN–GND–OUT is OUT–GND–IN, and some books describe the 79xx as a mirrored part. A student may read the sentence as confirming a mirror.
- ch 7 [low] Lead: "Switches the input on and off thousands of times a second" understates the switching rate and clashes with the chapter's own example (100 kHz = 100,000 times a second). A student may picture a few kHz.
- ch 7 [low] Section 2, ripple formula box: ΔIL = (Vin − Vout) D T / L and the off-time check Vout(1 − D)T/L are buck-only results, but the box does not name the topology. It sits just after the boost and buck-boost formulas, so a student can wrongly apply it to a boost.
- ch 7 [low] Section 2, buck-boost paragraph: "Many isolated supplies use a transformer instead, which also gives isolation" reads as if the buck-boost already gave isolation; "also" and "instead" pull in opposite directions.
- ch 7 [low] Section 3, output-ripple formula: The extra term ΔIL × ESR uses ESR without ever defining it.
- ch 7 [low] Section 3, losses paragraph: "I is switch current in amperes" is ambiguous in I² Rds(on) D; the squared current must be the RMS current in the switch while it is on (for a buck, essentially the DC output current).
- ch 8 [high] Section 3, capacitor-rating bullet; Exam traps, 'Under-rating capacitors'; Quiz Q7 and its answer: The chapter says C1 sits at 2Vp and must be rated above 2Vp, but its own Section 1 says C1 charges only to Vp. In the doubler the capacitor that stands at the full 2Vp is C2 (the output capacitor). The 2Vp figure belongs to D1's reverse voltage, not to C1. A student who follows this will fit a needlessly large C1 and may under-rate C2.
- ch 8 [low] Section 3, first paragraph: The ripple is written as ΔV ≈ I/(f·C) and then said to 'grow with n', but that formula contains no n, so nothing grows. For a cascade the ripple is larger than the single-capacitor value.
- ch 8 [low] Section 3, first paragraph: 'Under load current I the output falls by about n·Vd plus the resistive drop' counts the diode drops twice: the formula Vout ≈ n·Vp − n·Vd already removes n·Vd at no load.
- ch 8 [low] Lead paragraph: 'One stage doubles, two stages triple, three stages quadruple' conflicts with the formula, where n is 'the number of stages' yet n = 2 for a doubler, n = 3 for a tripler. A student can plug n = 2 into a tripler.
