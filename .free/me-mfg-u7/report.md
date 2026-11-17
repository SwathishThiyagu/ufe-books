# me-mfg-u7: free-model run

- Book: `books/mech/me-mfg/me-mfg-u7.html`
- Status: ok
- Model calls so far: 34 (116,269 tokens in, 226,691 out), 6.1 minutes

## Checker

```
me-mfg-u7.html: 9 chapters, 16371 words, 10 figures, 166 KB
OK
```

## For the reviewer

- chapter 8: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 9: the figure cannot be drawn: tree is too wide (5 leaves); use fewer leaves or shorter labels
- chapter 1: the figure cannot be drawn: tree is too wide (7 leaves); use fewer leaves or shorter labels
- chapter 1: the figure could not be drawn; a plain box diagram stands in for it
- chapter 8: the figure could not be drawn; a plain box diagram stands in for it
- chapter 9: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Section 2 and Figure: The text and table give material jetting the examples 'MJM, PolyJet', but the figure note gives only 'PolyJet'. A student revising from the figure alone will miss MJM, and the abbreviation MJM is expanded only in the sentence above the table.
- ch 1 [low] Section 3, mass customisation bullet: 'as in dental aligners' is loose. Clear aligners are usually thermoformed over additively made models; the printed part is the mould, not the aligner itself.
- ch 1 [low] Section 2, directed energy deposition sentence: The sentence says DED feeds powder or wire into a 'laser melt pool'. Laser is only the most common energy source; electron beam and electric arc (wire-arc DED) are also used in this family.
- ch 2 [low] Lead and Section 1: The abbreviation AM (additive manufacturing) is used in the title, in the figure and in Section 1 ('Early AM was used mainly for such models') but is never spelled out or defined. An ESL reader meets an undefined two-letter term in the first paragraph.
- ch 2 [low] Quiz Q6: The answer says the part becomes 'about 25 times too large'. The exact factor is 25.4 (1 inch = 25.4 mm), and the chapter elsewhere uses 1016 mm for the same case, so the two statements do not match exactly.
- ch 2 [low] Lead: 'CAD design' repeats the word design, since CAD already means computer-aided design. Small point, but the lead is where terms are first defined.
- ch 3 [low] Section 1, bulleted cycle: The bullet list contradicts the paragraph above it and repeats the platform move. The paragraph gives: scan → platform down by one layer → blade spreads resin. The list instead starts with 'Lower the platform' and then later says 'Move the platform down by one layer thickness' again after curing, so a student following the bullets would lower the platform twice per layer and would spread resin after the next scan instead of before it.
- ch 3 [low] Section 1, second paragraph (DLP): Saying a projector machine flashes a layer 'through a mask' suggests a fixed physical mask. In digital light processing the pattern comes from a digital micromirror device that switches pixel by pixel, so the mask is dynamic, not a printed mask.
- ch 4 [low] Figure caption: It says the filament is 'laid as a 0.2 mm raster'. A raster is a road whose width is set by the nozzle diameter (for example 0.4 mm); 0.2 mm is the layer height, that is the road thickness, not the raster.
- ch 4 [low] Section 1, filament list: PETG is expanded as 'polyethylene terephthalate glycol'. The standard expansion is glycol-modified PET.
- ch 4 [low] Section 2, infill definition: 'from 0% hollow to 100% solid' can mislead: at 0% infill the part is not empty, because the perimeters and top and bottom skins are still printed solid.
- ch 5 [low] Lead: The lead states as a general property of the whole PBF family that 'overhangs need no separate support structure'. This is true for polymer SLS but false for metal PBF, where supports/anchors are needed for heat flow and to control warping. Section 2 corrects this, but a student reading only the lead will learn the wrong rule.
- ch 5 [low] Section 1, layer cycle list: The platform is lowered twice: bullet 1 is 'Lower the build platform by one layer thickness' and bullet 6 is 'Lower the platform and repeat until all slices are built'. A student cannot tell whether lowering once or twice per layer is intended.
- ch 5 [low] Section 2 and its table: The chapter says DMLS 'fully melts' metal powder. Many textbooks and exam keys describe DMLS as liquid-phase sintering at the grain level and reserve full melting for SLM, so a student writing 'DMLS sinters' in an exam would appear to contradict this book.
- ch 5 [low] Worked example 1, step 5: Step 5 and the answer line both give 'about 6.94 h', repeating the same value twice with no new information.
- ch 6 [low] Lead and Section 1: "track over track makes a layer" reads as if tracks are stacked vertically to form a layer. It is tracks laid side by side next to each other that fill one layer; layers are what get stacked track over track.
- ch 6 [low] Section 1, second paragraph: "the powder you feed is never the powder you deposit" is confusing: some fed powder does land, only part of it. A student may read it as meaning no fed powder ever becomes deposit.
- ch 6 [low] Figure spec: The edge list flows track → table and table → part, which suggests the track feeds the table and the table feeds the part. In reality the pool lays the track on the part, and the part is held on the table.
- ch 6 [low] Quiz Q6: The question asks for two process causes, but the answer mixes three causes with remedies, so the student cannot see exactly which two causes are being marked.
- ch 7 [high] Exam traps, last trap (glue line): The trap says the finished stack is taller than n × t (correct) but then concludes that a part built to height H 'may need one extra layer of allowance'. The conclusion runs the wrong way. Because each bonded layer is t plus the glue line, H ÷ t layers would overshoot H; reaching height H needs slightly fewer layers than H ÷ t, never more.
- ch 7 [low] Figure caption: 'the cut is the only step that changes shape; the last two steps happen once, after the whole stack is built' is confusing. Removing the excess also changes the shape, and the two clauses are not really connected.
- ch 7 [low] Section 3, advantages list: Listing 'simple post-processing' as an advantage sits badly with the text's own account of de-cubing, which is slow manual work and is normally quoted as a disadvantage of LOM.
- ch 7 [low] Section 1 table, row 'Z accuracy': The entry 'one sheet thickness plus the glue line' is a step height (the vertical resolution), not an accuracy or tolerance. Students may then write that LOM's Z accuracy equals 0.1 mm when asked for a tolerance.
- ch 8 [low] Section 2, first sentence: MJM and PolyJet are treated as two names for one product family. They are two vendors' related material-jetting technologies (one is often wax-based, the other photopolymer), so a student may quote the brand names interchangeably in an exam.
- ch 8 [low] Section 2, durability sentence: 'Softens under strong sunlight' is not the usual behaviour. Sunlight is UV, and UV exposure degrades a photopolymer, making it embrittle, yellow and absorb moisture rather than soften.
- ch 8 [low] Section 3 bullet list and Section 4 table (SLS row): The table lists SLS feed material as 'polymer, metal or ceramic powder', and the section 3 bullet says the furnace supplies 'melting energy'. In standard usage SLS is mainly a polymer process; metals and ceramics normally need powder bed fusion variants that reach higher temperatures, and printed sand moulds are cured in an oven, not melted.
- ch 9 [low] Section 2, conformal cooling channel dimensions: The stated ranges (8-15 mm offset from the cavity surface, 6-12 mm channel diameter) are much larger than the usual conformal-cooling practice for small and medium inserts; a student will size channels wrongly for a phone-cover type mould. Typical practice is a channel about 1.5 to 2 channel diameters away from the surface, with diameters of roughly 3-8 mm; the big values only apply to very large moulds.
- ch 9 [low] Section 2, first paragraph of the cooling description: 'with round bends instead of drilled plugs' is unclear — a drilled circuit needs cross-drilled holes closed with plugs, and the student may think the plug is a feature of the channel shape.
- ch 9 [low] Section 4, cost-per-part formula: c_part is described as 'the cost of one part on the machine', but for a tooling route the part is made on the moulding press, not on the AM machine, so 'the machine' is ambiguous.
- ch 9 [low] Worked example 1, step 2: Cycle time is the time per moulding shot, not per part. Treating 10 s saved as 10 s saved per part is only true for a single-cavity mould, and the example does not say so.
