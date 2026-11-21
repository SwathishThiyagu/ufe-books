# me-design-u2: free-model run

- Book: `books/mech/me-design/me-design-u2.html`
- Status: corrected (Claude correction pass, 21 Nov 2026)
- Model calls so far: 16 (65,562 tokens in, 132,620 out), 4.9 minutes

## Checker

```
me-design-u2.html: 5 chapters, 10065 words, 6 figures, 115 KB
PROBLEMS:
 - at 390px, text spills outside the svg box in figure(s) [4]: enlarge the viewBox or shorten the labels
 - at 1366px, text spills outside the svg box in figure(s) [4]: enlarge the viewBox or shorten the labels
```

## For the reviewer

- checker: at 390px, text spills outside the svg box in figure(s) [4]: enlarge the viewBox or shorten the labels
- checker: at 1366px, text spills outside the svg box in figure(s) [4]: enlarge the viewBox or shorten the labels

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, note under the theory table: The text says Coulomb–Mohr reduces to Rankine when Sut = Suc. Put S for both strengths in σ1/Sut − σ3/Suc = 1/n and the result is (σ1 − σ3)/S = 1/n, that is, n = S/(σ1 − σ3). That is the maximum shear stress (Tresca) criterion, not maximum principal stress (Rankine). The claim contradicts the standard textbooks and points a student to the wrong theory.
- ch 1 [high] Section 2, table row 'Rankine, maximum principal stress': Writing σeq = σ1 with no condition is wrong for compression. If all three principal stresses are compressive, σ1 is negative, so σeq is negative and the check σeq ≤ Sut/n is always satisfied, even at a dangerous compressive stress. The standard definition is: failure when σ1 = Sut (tension) or when σ3 = −Suc (compression).
- ch 1 [low] Quiz Q2: 'Tresca predicts failure at a lower stress, so it gives a smaller factor of safety' can be misread. A lower failure stress suggests a lower equivalent stress, which would give a larger n. The reason for the smaller n is that Tresca's equivalent stress is larger for the same applied load.
- ch 1 [low] Figure 'Choosing a failure theory', final node: The last node says 'σeq against Syt/n'. That is the ductile check only; the brittle path in the same figure ends at Sut/n, so the figure contradicts its own Section 1.
- ch 1 [low] Section 2, last paragraph of the choice rule: The cross-reference 'see 2.3' is plain text, so a student reading on a phone cannot jump to the fatigue chapter; every other cross-reference in the book is a link.
- ch 2 [high] Section 2, the sentence on Neuber's estimate: It says 'a stronger, more notch-sensitive material has a larger √a and also raises q'. The formula q = 1/(1 + √a/√r) shows that a larger √a lowers q. The clause therefore contradicts the equation just above it. The material trend is also backwards: a more notch-sensitive (stronger) steel has a smaller √a, which is what raises q at a given radius.
- ch 2 [low] Section 3, first paragraph: 'A large r lowers Kt directly and also raises q, so Kf falls' states it as certain, while q and Kt pull in opposite directions and the quiz answer (Q7) correctly says the net Kf 'usually' falls. A student could read the two statements as contradicting each other.
- ch 2 [low] Section 3, relief groove description: 'It moves the peak stress away from the change in diameter' is loose. A relief groove works by cutting away material at the shoulder so the stress lines spread over a longer length; the groove itself becomes the new, milder notch.
- ch 3 [high] Section 1 (stage 1, crack initiation): The text says a notch "raises the local stress by Kf". Kf is the fatigue notch factor (a factor that reduces the endurance limit, Kf ≤ Kt). The local elastic stress is raised by the theoretical stress concentration factor Kt; Kf is not a stress raiser. A student would wrongly treat Kf as the stress concentration factor, which contradicts what Chapter 2.2 teaches.
- ch 3 [low] Section 3, kd: "Strength drops away from room temperature" suggests the endurance limit falls both above and below room temperature. In the standard Marin tables the drop is at elevated temperature; at low temperature kd is taken as 1 (static strength usually rises, though ductility falls).
- ch 3 [low] Figure and its caption: The second series draws S = 230 MPa across the whole range 10³ to 10⁷, but the curve itself is flat only after 10⁶ cycles. The overlay duplicates the flat part of the S–N series and makes the endurance limit look like a limit from 10³ cycles onward.
- ch 3 [low] Exam traps, last bullet: "A slope of −0.12 per decade is not −0.12 per cycle" is confusing: b is the slope of log₁₀ S against log₁₀ N, so 3 decades means 3b in log S. The phrase does not tell the student what to do differently.
- ch 3 [low] Section 3, kb: "A larger section has less support from the core" is vague and does not say why kb falls.
- ch 3 [low] Sections 1 and 3, cross-references: "Chapter 2.2" and "Chapter 2.4" are written as plain text, so on a phone the student cannot jump to them.
- ch 4 [low] Quiz Q8: The answer writes the formulas with the wrong signs: 'σm = (200 − 100)/2 = 50' and 'σa = (200 + 100)/2 = 150'. The signed values σmin = −100 MPa must be substituted as given in Section 1. The numbers come out right only because of the coincidence that −(−100) = +100; a student copying this pattern for a cycle such as σmax = 150 MPa, σmin = −50 MPa would get the wrong mean stress.
- ch 4 [low] Figure: The Soderberg series is drawn past its σm intercept of 400 MPa and continues to σa = −115 MPa at σm = 600 MPa. Failure lines in the σa–σm diagram end at the horizontal intercept; the line dipping below the axis is meaningless and shows on the plot.
- ch 4 [low] Section 2, Goodman line: Calling the straight line joining Se and Sut the 'Goodman or Haigh line' mixes two terms. The Haigh diagram is the whole σm–σa plot; the line itself is the Goodman (modified Goodman) line.
- ch 5 [low] Lead: The lead says the extra stretch 'comes from the kinetic energy that must be stored as strain energy'. At maximum extension the weight is momentarily at rest, so the strain energy actually equals the weight's whole loss of potential energy over the fall, W(h + δ) — the kinetic energy at impact Wh plus the further work Wδ done during stretching. A student may think only Wh is absorbed and then mis-set the energy balance in Section 2.
- ch 5 [low] Section 2, first line: 'Shock loading is a repeated sudden load' is too narrow. Standard texts use shock (sudden/impact) loading for any load applied in a very short time; repetition makes it worse but is not part of the definition. A student may conclude that a single falling weight is not a shock load, contradicting Section 1 of this same chapter.
- ch 5 [low] Section 1: The falling-weight formula is used without stating its assumptions: the rod's own mass is neglected, the stress is taken as uniform at every instant (no stress-wave/propagation effect), and the weight stays in contact after impact. Without this, students apply the formula to long rods or high-speed impacts where it under-predicts stress.

## Correction pass (21 Nov 2026)

- Every reviewer note above fixed (Coulomb–Mohr reduces to Tresca; Rankine with both strengths; Neuber trend; Kt versus Kf in fatigue initiation; low-temperature kd; S–N overlay; Goodman versus Haigh naming; signed σmin in the quiz; Soderberg drawn past its intercept; impact energy W(h + δ); shock definition; impact assumptions).
- Every worked example, quiz and bank answer traced in Python; Gerber example now checked against the Langer yield line (4.06 capped at 3.33).
- New: maximum strain energy theory; shaft-diameter example (Tresca and von Mises); plate-with-hole example (Heywood); Marin factor values; Miner's rule with a worked example; finite-life design with Sf; Soderberg diameter design; cushioned-impact example.
- All five figures hand-drawn from the worked examples; 14 full model answers; cross-unit references named by topic; university-hosted and unopened links dropped.
