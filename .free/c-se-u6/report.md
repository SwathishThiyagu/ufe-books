# c-se-u6: free-model run

- Book: `work/claude_figs/c-se-u6/tree/books/cse/c-se/c-se-u6.html`
- Status: ok
- Model calls so far: 45 (174,368 tokens in, 261,067 out), 7.7 minutes

## Checker

```
c-se-u6.html: 9 chapters, 15582 words, 10 figures, 188 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, control and replanning example: "The project is ₹5,000 ahead of the spending line" describes an overspend as if it were good progress. Spending ₹29,000 when the plan says ₹24,000 means ₹5,000 more money has gone out than planned; a student will read "ahead" as "doing well" and miss that this is a cost overrun.
- ch 1 [low] Section 3 formula and Worked example 1, steps 4–5: The formula B × k ÷ N silently assumes money is spent at the same rate every week. Real projects spend unevenly (design and testing weeks cost more), so the flat ₹4,000 per week is an assumption that is never stated.
- ch 2 [high] Exam traps, fourth bullet (mixing units in defect density): The bullet says 150 defects ÷ 25,000 lines is 0.006 per line, "not 6 per KLOC". But 0.006 defects per line IS exactly 6 defects per KLOC, so the two numbers are the same density written in different units. A student reads a contradiction where there is none, and may conclude that dividing by lines gives a different quantity from the density in the worked example.
- ch 2 [low] Section 2, process metrics paragraph: Phase containment is defined as "the percentage of defects found in the phase where they were injected". The denominator is missing, so a student cannot tell whether the base is all defects found or the defects injected in that phase.
- ch 2 [low] Section 1 table, Indicator row: The example says "DRE 80% and density falling: ship", but no falling density appears anywhere in the chapter's numbers; the worked example gives a single density of 6 defects per KLOC. The example does not match the data the reader has.
- ch 3 [high] Worked example 1, steps 2 and 3: The exponents have lost their superscript markup, so students read '2.4 × 101.05' and '2.5 × 26.9280.38', which look like multiplication by 101.05 and 26.9280.38. The numbers shown then contradict the stated answer.
- ch 3 [high] Quiz Q3: Same lost superscripts: 'E = 2.4 × 51.05 ≈ 13.0' and 'D = 2.5 × 13.00.38 ≈ 6.6 months' read as wrong arithmetic rather than 5<sup>1.05</sup> and 13.0<sup>0.38</sup>.
- ch 3 [high] Section 3, first line: The duration formula appears as 'D = c × Ed', which reads as c times E times d instead of E raised to d.
- ch 3 [low] Section 1, function points bullet: Only the five function types are listed; the value adjustment factor, which is the second half of the standard function-point method when a single adjusted size is used, is not mentioned.
- ch 3 [low] Section 3, end: The forward reference to Chapter 6.4 is plain text, so a phone reader cannot tap it.
- ch 4 [low] Section 3, milestones paragraph: The sentence 'They give checkpoints without pretending a review consumes no time' is confusing and reads as if it contradicts the zero-duration definition just given. A student can take away that a milestone itself takes time, or that milestones hide review work.
- ch 4 [low] Section 1, Duration ≈ Effort ÷ People formula note: 'Add roughly 10–20% for coordination when People is more than 1' does not say what to add it to. A student may add 10–20% to people, or to effort, instead of to the duration.
- ch 4 [low] Exam traps, fourth bullet, and Quiz Q6: 'Float' is used as a synonym for slack without ever being defined, so a student meeting the word in an exam paper may not connect it to the slack defined in Section 2.
- ch 5 [low] Section 1, three risk families: The chapter states flatly that 'software risks fall into three families' and names product, process and technology. Standard textbooks use a different set of three (project, technical, business), and business risks — a budget cut, a customer withdrawing, a competitor shipping first — are never mentioned at all. A student who meets the standard taxonomy in the exam may think it contradicts this page.
- ch 5 [low] Section 1, proactive strategy: 'One short meeting with the team and the tech lead usually finds the top ten risks in an afternoon' contradicts itself: a short meeting does not last an afternoon.
- ch 5 [low] Section 2, formula box for RE: The text allows impact in person-weeks or in rupees, but the formula and the table give I only in person-weeks and never say what the unit of RE is when I is in rupees. A student may write RE = 1.2 with no unit, or mix units inside one table.
- ch 5 [low] Beyond (not for the exam): Calling an error budget 'a risk exposure for service downtime' is loose. An error budget is the amount of unreliability a service is allowed (1 minus the SLO), not a probability times an impact.
- ch 6 [low] Section 3, end of first paragraph: The cross-reference 'See Unit 5, Version control systems' points outside the unit and is not given as a chapter link, while the rest of the chapter refers to same-unit chapters by number (6.9). A reader on a phone cannot jump to it, and the unit number may not match where version control is actually taught.
- ch 6 [low] Section 2, change control step list, third bullet: 'Send the CR to the CCB for approve or reject' is ungrammatical and reads awkwardly for second-language readers.
- ch 6 [low] Figure, Change to baseline: The figure and its aria text mention rejection, but every edge is drawn solid and the only path shown is the approval path, so a student may think a rejected CR still produces a new baseline.
- ch 7 [high] Section 2, Inspection: The text says the author 'presents' during a formal inspection. Standard inspection practice is that the author does not present or lead the reading; the moderator or a designated reader walks the team through the product, and the author stays silent except to answer factual questions about intent. As written it also contradicts the chapter's own role list, where the author only 'supplies the material, answers questions about intent, and fixes the defects', and it blurs the line the chapter draws between an author-led walkthrough and an inspection.
- ch 7 [low] Section 1 and Section 2 (cross-references): The text points to other chapters ('the project plan of 6.1', 'as in 6.6') in plain words, with no chapter links, so a student reading on a phone cannot jump to them.
- ch 8 [high] Section 3 (legacy systems and re-engineering): The section says re-engineering has three technical steps (reverse engineering, restructuring, rebuilding), but the next sentence, 'The third step improves structure; the fourth rebuilds', counts a fourth step. A student cannot tell whether restructuring is step 2 or step 3, and the paragraph contradicts itself.
- ch 8 [low] Section 3 (legacy systems and re-engineering): One of the three steps inside re-engineering is itself labelled 'Re-engineering', which reads as if the whole thing is a step inside itself. Students may think reverse engineering and restructuring are outside re-engineering.
- ch 8 [low] Section 2 (formula): The payback formula P = C ÷ S is placed in the maintenance-process section, before re-engineering and its cost C have been introduced. The reader meets C and payback with no decision context yet.
- ch 9 [low] Section 2: "Staging is a copy of production" is too absolute; real staging differs in data volumes, credentials and sometimes hostnames, so a student may believe exact equality is required and be confused when staging reveals differences at release time.
- ch 9 [low] Section 1: The chapter says a version number "has three parts" and then uses 2.5.0-rc1, which carries a fourth element. A student may wonder whether the RC tag is part of the version or not.
