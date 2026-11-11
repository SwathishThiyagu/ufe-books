# c-se-u2: free-model run

- Book: `work/claude_figs/c-se-u2/tree/books/cse/c-se/c-se-u2.html`
- Status: ok
- Model calls so far: 49 (178,846 tokens in, 308,782 out), 9.5 minutes

## Checker

```
c-se-u2.html: 9 chapters, 14698 words, 10 figures, 192 KB
OK
```

## For the reviewer

- chapter 1: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 1: the figure could not be drawn; a plain box diagram stands in for it
- chapter 8: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, table: The text says two families exist, but the table has a third row headed 'Family' called 'Constraint / interface', and it puts 'Android 8+' there, while the worked example later classifies Android 8+ as a non-functional portability/platform constraint. A student reading both will not know whether the platform limit is a third family or an NFR.
- ch 1 [low] Figure caption: The caption says 'each branch starts as a user-level statement and is then expanded into system requirements', but the tree shows only Functional and Non-functional with service/quality leaves. Nothing about user level or system level appears in the figure, so the caption describes a picture that is not there.
- ch 1 [low] Section 3, last paragraph: The rule 'an NFR needs a number, a condition and a unit' contradicts the chapter's own constraint examples. 'Runs on Android 8 and above' and 'payment data travels over HTTPS' are accepted as NFRs but carry no unit.
- ch 1 [low] Beyond: 'a quality-attribute scenario: a stimulus, a response, and a measured response' is garbled — the third part is the response measure, not a second response.
- ch 2 [low] Lead: 'It is a loop, not a one-time form' — 'form' is unclear; a student may read it as an application form rather than a one-off activity.
- ch 2 [low] Section 1, process stages: The text says some syllabi call the first five stages (feasibility through validation) 'requirements development'. Feasibility is normally kept outside requirements development, which covers elicitation, analysis, specification and validation.
- ch 2 [low] Figure: The text says management runs beside every stage, but the diagram draws the management box with a single dashed edge to analysis only, and validation's feedback edge goes only to elicitation although the text says it can return work to elicitation or analysis.
- ch 2 [low] Section 1: Cross-references appear as bare numbers ('2.3 covers how to run it', 'Links: 2.6, 2.7, 2.8'), so they are not clickable in the book.
- ch 3 [low] Section 1, stakeholder classification: The line 'external stakeholders regulate or depend on it' is loose: passengers and clerks also depend on the system, yet they are primary stakeholders. A student may think any dependent party is external.
- ch 3 [low] Section 1, definition of secondary stakeholders: 'Secondary stakeholders support it' is too narrow and can be read as only operational support. Standard usage also covers people involved in developing and maintaining the system.
- ch 3 [low] Section 3, conflict resolution paragraph: The text says 'convenience features become later options', but the very next sentence delivers one-click in the same release as a remembered profile after authentication. The two sentences read as contradictory.
- ch 3 [low] Quiz Q4 answer: The answer makes OTP mandatory, but Section 3 only declares the audit trail mandatory; OTP is not labelled mandatory anywhere. A student comparing text and answer sees a mismatch.
- ch 3 [low] Worked example 1, part (c): Splitting the 20-minute conflict-resolution block equally across the five stakeholder groups suggests each group resolves conflicts separately, which conflicts with the chapter's own advice to resolve by joint ranking, not by giving each side its own slot.
- ch 3 [low] Figure and Section 3: The accessibility representative is treated as an important stakeholder in the text and invited to the workshop, but does not appear in the stakeholder map figure, so the figure and text do not match.
- ch 4 [high] worked example 1, step 2 and answer: The count of clean requirements is wrong. The 3 missing requirements are not among the 40 (they are absent, so they cannot be subtracted), and the 2 conflicting pairs involve up to 4 existing requirements, not 2. So 40 − 11 = 29 does not give the number of defect-free requirements.
- ch 4 [high] quiz Q4: The answer repeats the same error. The 4 missing requirements are not inside the 60, and the 3 conflicting requirements are inside it, so 60 − 15 = 45 clean requirements is not a valid result.
- ch 4 [low] section 1, checklist technique: "ambiguity (one meaning, numbers with units)" is confusing: a requirement must have exactly one meaning, and units belong with testability/measurability, not ambiguity.
- ch 4 [low] quiz Q5: Q5 contradicts the traceability table shown in Section 2, where R14 refund is already covered by T-14. It also skips the point that R14 is already baselined, so the missing test cannot simply be added.
- ch 5 [low] Section 2, verifiability example: The line 'FR-01 The app shall show an alert within 30 s of an official outage message' is declared to pass because 'the clock start is named', but the start point (receipt of the message) is not actually stated. The exam traps later say the same phrasing is incomplete without 'from receipt of official message to visible alert', so the chapter contradicts itself.
- ch 5 [low] Section 1 and Figure: The bullet list has eight sections, with Performance and Security written as one bullet. The figure stack has nine items and splits them into 'Performance' and 'Security'. A reader counting sections gets two different answers.
- ch 5 [low] Section 1, last sentence: 'If a section has no effect on a test, cut it' can be read as licence to delete the Introduction, scope and definitions, which the same section says are needed and which traceability depends on. A student may cut the purpose and definitions.
- ch 5 [low] Worked example 1, step 2: Step 2 names the first section 'Scope', but the section order in Section 1 names it 'Introduction' (purpose, scope, definitions, references). Mixing the two names confuses the mapping of step 2 to the recommended order.
- ch 5 [low] Quiz Q7: The platform requirement is labelled FR-01, but earlier in the chapter functional requirements are FR and platform/quality limits are NFR. The labelling clashes with the convention the chapter just taught.
- ch 6 [low] Section 2, Table 1 (Goal and Postconditions rows) versus Section 1 'Use case versus scenario': Section 1 says 'Withdraw cash' is the use case and 'withdraw ₹5,000 with a valid card' is a scenario, but Table 1 writes the use case named 'Withdraw cash' with the fixed goal 'Customer gets ₹5,000 cash and a receipt' and the postcondition 'Account debited by ₹5,000'. This contradicts the chapter's own distinction and teaches students to write one instance as the use case.
- ch 6 [low] Section 2, Table 1 (Main success scenario row): The text right after the table says 'Keep each step as one actor action or one system response; name who does it', but the table's steps name nobody: 'Validate card; verify PIN; request ₹5,000; check balance ...; debit account ...'. A student copying this style loses marks for actorless steps, and the instruction then looks wrong.
- ch 6 [low] Section 1 versus Section 2, Table 1 (Secondary actor row): Section 1 defines the secondary actor as 'the Bank's account system', but the table lists the secondary actor simply as 'Bank'. 'Bank' is an organisation, not the external system the ATM talks to, so the system boundary the chapter stresses becomes fuzzy.
- ch 7 [low] Figure (class model): The class nodes carry instance counts as notes — Doctor '3 doctors' and Slot '30/day'. A class model shows how many objects may take part (multiplicity), not how many objects exist in one scenario; a student may copy this habit into exam answers.
- ch 7 [low] Figure caption and aria text: The caption says Appointment 'carries the four-state machine used in the example' and the aria says 'Appointment has a state machine', but the drawing only has a note '4 states' and no states or transitions. A reader looks for something that is not there.
- ch 7 [low] Quiz Q6: 'Action state' is a standard UML term from activity diagrams (an activity node that performs an action). Using it here for a wrong state name will confuse a student who has met the real term.
- ch 7 [low] Section 3: State, event and transition are defined, but the initial state is never mentioned, so nothing says an appointment starts in requested. Every state machine needs a defined start.
- ch 8 [high] Section 2, levelling rules bullet 5 and the balancing formula note: The text says 'Only the flows between processes and stores are new', and the formula note says flows 'between its processes and stores' are the extra ones. Opening one parent process into several child processes creates new flows between those child processes as well (for example Booking sending a confirmed-booking message to Cancellation). A student reading this will think a process-to-process arrow inside a child diagram is an error, and will be marked down for it.
- ch 8 [high] Worked example 1, step 5, and the Figure: The Train Schedule (Timetable) store is only read: it receives 'sched query' from Enquiry and from Booking and returns 'sched data'. No process ever writes it, and a query sent into a store is not a write. This contradicts the chapter's own rules in Section 1 ('Every data store is written by some process and read by some process') and Section 3 ('A store that is never read, or never written').
- ch 8 [low] Section 3, bullet list of checks: The bullet list of errors starts straight after 'check it mechanically' with no lead-in, so the reader does not know these are the things a CASE tool flags.
- ch 8 [low] Worked example 1 versus the Figure: The same data is named differently in the two places: 'train details' in the example against 'train list' in the figure, 'Train Schedule' against 'Timetable', 'Ticket' against 'Tickets', 'payment request' against 'pay request'. The chapter itself insists a flow or store name must mean the same thing everywhere, so the example undercuts its own rule.
- ch 8 [low] Quiz Q4: The 'corrected count' is 8 + 6 = 14, which is exactly the number of flows the faulty child already has, so a student may think nothing changed and that the answer is wrong.
- ch 9 [high] Section 1, sentence 'A need is a what; a response is a how. This follows the split in 2.1 Functional and non-functional requirements.': This links the what/how split to the functional vs non-functional requirement split. That is wrong. A what is a customer need; a how is a technical response or design characteristic. Functional and non-functional is a different cut (what the system does vs a quality attribute such as speed or security). A student will wrongly conclude that every what is a functional requirement and every how is a non-functional requirement.
- ch 9 [low] Section 3, sentence 'If a response has a zero column': A response is itself a column, so 'a response has a zero column' is confusing and clashes with the wording 'column of zeros' used in Q5.
- ch 9 [low] Quiz Q6 answer: 'All responses get the same weighted pattern' is vague. When every cell is 9, every response gets exactly the same total score, which is the actual reason ranking fails.
- ch 9 [low] Figure, column header 'Ctrs': The abbreviation 'Ctrs' is not explained in the visible table, so a reader on a phone may not connect it to 'counter count'.
