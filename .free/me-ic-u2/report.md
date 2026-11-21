# me-ic-u2: free-model run

- Book: `books/mech/me-ic/me-ic-u2.html`
- Status: ok
- Model calls so far: 25 (82,998 tokens in, 242,784 out), 6.8 minutes

## Checker

```
me-ic-u2.html: 11 chapters, 20457 words, 12 figures, 231 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] exam traps, first bullet: The sentence says the circuits 'add or subtract fuel', but no carburettor circuit subtracts fuel. The main jet sets the base supply; idle, power valve, accelerator pump and choke only add extra fuel to enrich the mixture.
- ch 1 [low] section 3, paragraph after the table: The sentence says at part throttle the idle and main circuits both contribute. In most carburettors the idle circuit has largely stopped at normal part throttle; it contributes only at closed or very small throttle openings, where it overlaps with the main circuit.
- ch 1 [low] section 1, formula where clause: The symbols mair and mfuel are written without subscripts, unlike the formula itself.
- ch 2 [low] Lead: The lead says the system must "meter, atomise, distribute and time the fuel", listing four jobs, but Section 1 correctly lists five (pressure is missing). A student reading only the lead gets an incomplete list that conflicts with the rest of the chapter.
- ch 2 [low] Section 2, direct injection examples: Distributor (rotary) pump systems are named as direct-injection examples, but distributor pumps are used on both direct-injection and indirect-injection (prechamber) diesel engines. The figure also leaves distributor pump out, so text and figure disagree about the examples of direct injection.
- ch 2 [low] Section 2, indirect injection: Grouping petrol port injection and throttle body injection under "indirect injection" goes beyond standard usage, where indirect injection means a diesel prechamber or swirl chamber. The reasoning (fuel meets air outside the cylinder) is sound, but the label will confuse a student who meets the standard textbook definition.
- ch 2 [low] Section 2, control: "Continuous injection sprays all the time; intermittent injection sprays in pulses" gives no example of either, so the distinction stays abstract.
- ch 2 [low] Section 2 and Section 3 cross-references: The references "See 2.3", "see 2.4" and "see chapter 2.9" are plain text, so a student reading on a phone cannot jump to them.
- ch 2 [low] Figure caption: "Solid injection is the working family" is unclear; "working" could be read as "functioning" or as "the family that does the work".
- ch 3 [low] Figure (block 'Plunger', note in spec): The note says 'd=8 mm, stroke=3 mm'. In this chapter 3 mm is the effective stroke, not the total cam stroke, and Exam trap 1 warns students about exactly this mix-up. A reader can carry the wrong meaning away from the figure.
- ch 3 [low] Section 1, step list, third bullet: 'Pressure opens the delivery valve and the nozzle at its set pressure' can be read as if the delivery valve and the nozzle open at the same pressure. The delivery valve has only a light spring and opens well before the nozzle, which opens at its own set pressure (of the order of a few hundred bar).
- ch 3 [low] Section 4, first paragraph: 'check dynamic timing by spill or strobe method' mixes the two. Spill timing is normally a static, hand-turned check (delivery valve removed, fuel spills until the ports close); only the strobe/timing-light check is done with the engine running.
- ch 3 [low] Quiz Q4 (5-mark answer): The question asks for a comparison, but the answer covers only the pipe and pressure-lag side. For 5 marks a student also needs the other trade-offs: cam/rocker load and crowded head versus compact single-element layout, cost and service, and metering method.
- ch 4 [high] Section 3, bullet on split injection and retarded timing: The bullet says retarded timing lowers soot. Retarding injection timing lowers nitrogen oxides but normally increases soot and fuel consumption, because it lowers peak temperature and leaves less time for soot oxidation. This also contradicts Quiz Q6, which credits retarded timing only with lowering nitrogen oxides.
- ch 4 [low] Lead: The sentence 'The high-pressure pump and the injector are no longer one unit' is misleading. In pump-line-nozzle systems the pump and injector are also separate. The real change is that pressure generation is continuous and decoupled from the injection event.
- ch 4 [low] Section 2, paragraph on main injection: 'The main injection delivers most of the work' is imprecise: injection delivers fuel; combustion delivers work. A student may think the injector produces work.
- ch 4 [low] Figure: The figure omits the rail pressure sensor and its signal to the ECU, although the text says the sensor reports rail pressure to the ECU. The dashed 'pressure' edge from ECU to rail can be misread as the sensor signal, but it represents a command to the pressure control valve.
- ch 4 [low] Lead, last sentence: The sentence 'This chapter covers the layout, the pressure and timing control, split injection, and the cost that comes with it' is a roadmap filler; the chapter starts its content immediately after.
- ch 5 [low] Section 2, mono-point paragraph: "often once per engine revolution or twice per cycle" is presented as two alternatives, but on a four-stroke engine they are the same thing (two revolutions per cycle, one pulse per revolution = two pulses per cycle). A student reads it as two different possible rates and gets confused.
- ch 5 [low] Section 3, sequential firing paragraph: "a cam or crank sensor that identifies the cylinder" — a crank sensor alone gives speed and piston position but cannot tell which cylinder is on its compression stroke, so it cannot identify the cylinder. This also sits badly with the exam trap that says sequential needs cylinder identification, not just crank speed.
- ch 5 [low] Section 1, first paragraph: "Sensors turn physical quantities into voltages" contradicts the coolant sensor line, which says the sensor is a thermistor, i.e. it changes resistance, not voltage.
- ch 7 [low] Section 3, penetration bullet: Penetration is defined as 'how far the spray tip travels before it is fully broken up and mixed'. Breakup and mixing do not stop the spray tip; penetration is the maximum distance the tip reaches from the nozzle at a given time. A student may think penetration ends when atomisation finishes.
- ch 7 [low] Section 3, cone angle bullet: The wording 'the full angle between the spray edges, often 10° to 25° for multi-hole nozzles' can be read as the included angle of all jets from a multi-hole nozzle. The 10°–25° value is the cone angle of one individual jet; the included angle between the outer jets of a multi-hole nozzle is much larger.
- ch 7 [low] Beyond: The Beyond note says production nozzles use holes of about 0.1 mm, but Section 1 gives the multi-hole range as 0.15 mm to 0.4 mm. The two statements conflict unless the text says the smaller holes are a modern development.
- ch 8 [low] Section 2, opening paragraph: "driven by the engine, often by a belt" is misleading for diesel governors. Mechanical diesel governors are usually gear-driven from the camshaft or built into the injection pump; belt drive is not typical.
- ch 8 [low] Section 2, formula definition: "r is ball radius from the spindle" is ambiguous. A student may read it as the radius of the ball itself instead of the radius of its circular path about the spindle axis.
- ch 8 [low] Figure 'Governor speed control loop': The edge from Engine to Actual speed carries the label "senses", but the engine does not sense speed; it produces it. A student reading the diagram may get the signal direction wrong.
- ch 8 [low] Quiz Q6: "the droop set shares poorly" is vague for an analyze-level answer. The specific behaviour is that the isochronous set holds frequency, so the droop set sees almost constant speed and carries a nearly constant load.
- ch 9 [low] Quiz Q2 answer: "Fine wire keeps resistance and bulk reasonable" points the wrong way: fine wire has more resistance per metre than thick wire, so it does not keep resistance low. A student may think fine wire lowers resistance, which contradicts the primary/secondary comparison in Section 1.
- ch 9 [low] Section 1, contact breaker description: The breaker is said to be "driven by the engine camshaft". In car battery-coil systems the points are opened by a cam on the distributor shaft, which turns at half crankshaft speed; the engine camshaft drives the valves, not the points.
- ch 9 [low] Section 2, first line: "A magneto has a permanent magnet and a coil on the same shaft" is imprecise: in many magnetos the magnet rotates and the coil (armature) is stationary, and the two are not on a common shaft. The next sentence partly corrects this, so the opening line can confuse.
- ch 11 [low] lead: The claim that only a few universities teach this chapter is misleading: ignition timing and spark advance are standard content in almost every IC engines syllabus, so the sentence gives a wrong impression of the topic's place in the course.
- ch 11 [low] Section 2, vacuum advance paragraph: The reason given for vacuum advance is loose. At part load the air-fuel ratio is often close to stoichiometric; the flame is slow mainly because the charge is diluted by leftover exhaust gas and its density is low. Calling it simply 'the lean mixture' can mislead a student. Also, the source of the vacuum is not distinguished: many engines take ported vacuum, which is near zero at idle and at wide-open throttle, not manifold vacuum that is highest at idle.
- ch 11 [low] Figure and sample schedule: 40° of advance at 4000 rpm is at the extreme end; production engines usually top out near 30°–35° of total advance. A student may take this as a typical value rather than an illustration.
- ch 11 [low] Section 2, timing-light check: The procedure is missing two steps a student needs: identifying the fixed pointer and the matching mark on the crank pulley, and remembering that the light must be triggered by number one cylinder's lead and the reading taken with the engine idling at the specified speed.
