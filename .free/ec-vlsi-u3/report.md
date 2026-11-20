# ec-vlsi-u3: free-model run

- Book: `books/ece/ec-vlsi/ec-vlsi-u3.html`
- Status: problems
- Model calls so far: 35 (144,885 tokens in, 333,008 out), 8.6 minutes

## Checker

```
ec-vlsi-u3.html: 9 chapters, 17538 words, 10 figures, 176 KB
PROBLEMS:
 - chapter "nmos-inverters-resistive-enhancement-depletion-pseudo-nmos-loads": 1915 words is too long (keep under 1900; 900-1600 is the target)
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, the five regions: The region boundaries have lost their inequality signs and are unreadable: '(1) Vin tn', '(2) Vtn in M', '(4) VM in DD − |Vtp|'. A student cannot tell where each region starts or ends, and 'M' and 'DD' appear as stray letters.
- ch 1 [low] Quiz Q2 answer: 'the other pulls the output to its rail through no DC path' reads as if the output is floating. The on transistor is exactly the path that charges or discharges the output; what is absent is a DC current from VDD to ground.
- ch 1 [low] Section 3, chain check: 'each gate must drive the next gate to at least VIL or VIH with margin' is ambiguous: it can be read as the output high needing only to exceed VIL, which defeats the purpose of a noise margin.
- ch 2 [low] Worked example 1, step 9: The region check reads "VOL = 0.566 V GS − Vtn = 4.2 V", with the comparison sign missing. The whole point of the step is to show VOL is far below VGS − Vtn, and as printed the sentence is broken and a student cannot read the check.
- ch 2 [low] Section 2, depletion load: Body effect is called out for the enhancement load but silently dropped for the depletion load. In the depletion load the source is the output, so VSB = Vout > 0 and the (negative) threshold is pushed toward zero as the output rises. That makes IDSS fall as Vout rises, so the load is only an ideal constant-current source if body effect is ignored, and the formula IDSS = (knL/2)Vtd² uses the zero-body-bias threshold.
- ch 2 [low] Quiz Q6, answer: "The static current also doubles" is exact only while the pMOS stays saturated. Doubling kp raises VOL; once VOL rises above |Vtp| the pMOS enters its linear region, its current no longer depends only on (VDD − |Vtp|)², and the current rises by less than a factor of two.
- ch 2 [low] Section 3, pseudo-nMOS formula: The equation assumes the pMOS is saturated but the condition for that is never stated: the pMOS is saturated only while VDD − VOL ≥ VDD − |Vtp|, that is VOL ≤ |Vtp|. Without it the table entry "≈ kp(VDD − |Vtp|)²/2" looks exact when it is only the saturated case.
- ch 2 [low] Quiz Q7, answer, last clause: "the gate is much weaker against a high input on the driven node" is confusing. The small low noise margin VIL − VOL means an input that is meant to be low (sitting at the previous stage's VOL) is only a little below VIL, so noise that pulls that input up can cross VIL and be read as a high.
- ch 2 [low] Section 2, depletion load, last line: "a load that is on whenever the output is low" is misleading: the depletion load is on at all times (VGS = 0). What changes is that it carries current only when the driver pulls the output below VDD.
- ch 3 [high] Section 2, average-current method (paragraph and table row): The claim that the nMOS 'stays in saturation' over the whole VDD-to-VDD/2 swing is wrong. The nMOS is saturated only while Vout > VDD − Vtn. With Vtn < VDD/2 (the normal case, e.g. 0.5 V against 1.8 V) it leaves saturation at Vout = 1.3 V, above the 50% point of 0.9 V, and spends the lower part of the swing in the linear region with a smaller current. So the formula is not derived from a saturation current over the half swing; it is an optimistic estimate.
- ch 3 [high] Figure caption: 'The output holds its old value until the input passes the switching threshold, then falls' is wrong. The output starts to fall once the rising input passes Vtn (about 0.5 V here), well before Vin reaches VDD/2 at 2 ns. Only the 50% crossings are used to define tPHL; they do not mark the start of the fall.
- ch 3 [low] Section 1, paragraph on rise time versus delay: The example 'a short tp and a long tr if its driver is weak but the threshold is crossed early' is self-contradictory: a weak driver crosses 50% late, not early. For a single exponential tr ≈ 3.2 tp, so the two are not independent in the way stated.
- ch 3 [low] Worked example 1, steps 1-6 and Section 2 RC paragraph: Superscripts are lost in the plain-text steps: '2.66×10−10 s', '(200×10−6/2)', '100×10−6', and 'e−t/τ'. A student reading 'VDD(1 − e−t/τ)' can misread it as e minus t over τ.
- ch 3 [low] Section 2, RC method, Req value: Req ≈ VDD/(2·IDsat) combined with tp = 0.69 Req CL gives 0.345 CLVDD/IDsat, while the average-current formula gives 0.5 CLVDD/IDsat — about 30% apart for the same device, and the text does not say the two methods are not numerically identical.
- ch 3 [low] Section 3, feedthrough sentence: 'Cgd gives a short feedthrough spike at the output ... which is why a floating output node is never left undriven' draws a weak causal link. Floating nodes are mainly avoided because of charge sharing, leakage and noise, not because of the Cgd spike.
- ch 3 [low] Lead sentence: 'the four standard numbers (tPHL, tPLH, tp, and rise/fall times)' lists five quantities under the count of four.
- ch 4 [high] Lead, definition of τ: The lead calls τ the delay of a reference inverter driving an identical inverter, but the chapter's own model gives that case d = (1×1 + 1)τ = 2τ, not τ. A student will be confused.
- ch 4 [high] Figure: The x-axis is labelled 'fanout f', but the chapter defines f as stage effort and h as fanout/electrical effort. The plotted expressions 1+x and 2+(4/3)x are functions of h. Also 'starts at 2τ' is the h=0 intercept, not the left edge at h=1.
- ch 4 [high] Section 2, equal stage effort formula and bullet: The text writes f = F1/N. As written this is F/N, not the Nth root. The formula block uses F<sup>1/N</sup>, so the text is inconsistent and wrong.
- ch 4 [high] Worked example 1, step 4: f = F1/3 = (85.33)1/3 = 4.4026 is wrong as written because 85.33/3 = 28.44, not 4.4026. The exponent is missing.
- ch 4 [high] Exam traps, third bullet: The trap says 'Using H = Cload/Cload instead of Cload/Cinput'. The first formula is nonsense (it gives 1) and is not the common mistake.
- ch 4 [high] Quiz Q2: The answer says 'wider pMOS transistors' make the NAND input capacitance larger. In the standard equal rise/fall NAND2, the series nMOS are the wider transistors; the pMOS are in parallel and can stay the same width as the inverter pMOS. The extra input capacitance is from the nMOS.
- ch 4 [high] Quiz Q4: The answer writes f = F1/4 = 641/4 = 2.828. As written 641/4 = 160.25, not 2.828. The exponent is missing.
- ch 4 [high] Quiz Q5: The answer writes F = fN = 53 = 125. As written 53 is not 125. The exponent is missing.
- ch 4 [low] Lead: The lead says delay is smallest when every stage carries the same effort for a fixed load. This is only true for a fixed number of stages; changing N changes the optimum.
- ch 5 [low] Lead: "Static power decides whether a chip can sit idle without draining its battery" is ambiguous. Every chip drains its battery while idle; static power decides how fast.
- ch 5 [low] Section 1: The phrase "the brief time in a switching input when both nMOS and pMOS are on" is garbled and does not say when both devices are actually on.
- ch 5 [low] Section 3: "Lowering VDD ... also lowers static power for a given leakage current" is true only as P = VDD Ileak with Ileak held fixed. A student may read it as "lower VDD and leakage power drops", but in practice keeping speed at lower VDD needs a lower Vt, which raises subthreshold leakage sharply.
- ch 6 [high] Section 1, sentence after the dynamic-power formula: The text says 'Energy per switching event is E = α C VDD2'. With α defined (correctly, just above) as the fraction of cycles in which the node switches, α C VDD² is the energy per clock cycle, not per switching event. Multiplying by α again double-counts the activity. Students will carry this into energy-per-operation sums and get answers that are too small by a factor of α.
- ch 6 [low] Section 3 DVFS paragraph, worked example 1 steps 1 and 3, and exam trap 3: Squares are written as plain digits: '(V2/V1)2 × (f2/f1)', '(1.2 V)2', '0.83332 = 0.6944', 'Pdyn = α C VDD2 f'. A student reads 0.83332 as a five-digit number and VDD2 as a subscript-less variable, and the notation does not match the superscript tags used in Section 1.
- ch 6 [low] Quiz Q4, answer: The answer says 'The off time is short compared with the wake-up time', but the data given in the question (period 10 µs, wake-up 2 µs) leaves about 8 µs off, which is four times the wake-up time. The sentence contradicts the question's own numbers and reads as an error.
- ch 6 [low] Section 1, opening sentence: Dynamic power is attributed only to charging and discharging node capacitance. Short-circuit (direct-path) power, which flows while both input and output transistors of a gate conduct during a transition, is part of dynamic power too, and the chapter never mentions it.
- ch 7 [high] Section 2, the sentence after the Iload formula: The saturation condition is garbled: "which requires VOL tp|" is not a readable condition. A student cannot tell what limit VOL must satisfy for the pMOS load to stay in saturation.
- ch 7 [high] Section 2, second paragraph ("When the output is high, the nMOS network is off. The load pulls the output to VDD..."): This is stated for both pseudo-nMOS and the saturated nMOS load, but a saturated nMOS load with its gate at VDD cannot pull the output above VDD − Vtn. The high output is VDD − Vtn, not VDD, because the load turns off once VGS falls to Vtn.
- ch 7 [high] Quiz Q6, answer: "reduced VOL" says the opposite of the trade-off: ratioed logic raises VOL above 0 V, which is the cost. A student reading this answer would learn that pseudo-nMOS lowers VOL.
- ch 7 [low] Section 1, first paragraph: "A high input turns on the nMOS path and turns off the pMOS path, so the output is 0 V" describes a single-input gate, but it follows the general claim about every input combination. In a NAND, one high input alone does not pull the output low.
- ch 8 [high] Section 1, paragraph on passing a low input: The source terminal is stated wrongly. With A = 0 V, C = VDD and the output Y at any level above 0 V, the terminal at the lower potential is the input side A, not Y. The source is therefore A, not Y, so VGS = VG − VA = VDD − 0 = VDD, which does not depend on Y. Writing VGS = C − Y makes it look as if VGS falls as Y rises and the nMOS would turn off near VDD, which is exactly what does not happen. A student will carry this wrong picture into the high-level case, where Y really is the source.
- ch 8 [low] Section 3, first paragraph on PTL costs: The sentence 'a passed low through a pMOS alone is |Vtp|' reads as if the low level equals |Vtp| volts from ground without saying so, next to 'a passed high is VDD − Vtn'. The two levels are not written in the same form, so the comparison reads oddly.
- ch 8 [low] Quiz Q8, answer: The answer says a TG multiplexer 'can have weak levels'. A transmission gate with full-rail data inputs and a full-rail C bar passes both rails without loss, so weak levels are not the usual drawback of a TG mux. The listed handicap is misleading for a student who has just learnt that a TG restores the rail.
- ch 8 [low] Section 3, sentence on long chains: 'A long chain of pass transistors adds the drops' is only true when the gate of a later transistor is driven by a passed (already degraded) level. If every gate is held at VDD, each stage stops at VDD − Vtn and the level does not fall further from stage to stage; only the delay grows.
- ch 8 [low] Section 1, first mention of the threshold: The symbol Vtn appears in 'The transistor turns off when VGS = Vtn' before it is defined; the definition only comes in the formula box below. English-as-second-language readers on a phone will stumble here.
- ch 9 [high] Section 3, last paragraph: The sentence "Some syllabi call domino logic clocked CMOS" is factually wrong. Clocked CMOS (C²MOS) is a separate clocked static family built from clock transistors, not another name for domino logic. A student would carry a wrong synonym into the exam.
- ch 9 [low] Section 2, keeper description: "Its gate is driven by the output inverter" is imprecise: the keeper gate is driven by the inverter's output node (the gate output), not by the inverter as a block.
- ch 9 [low] Section 4, summary list: "Dynamic: ... n+2 transistors" only holds for an n-input dynamic NAND, and only if the keeper and any output inverter are not counted. Stated as a general figure it is misleading.
