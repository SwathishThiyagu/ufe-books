# c-se-u5: free-model run

- Book: `work/claude_figs/c-se-u5/tree/books/cse/c-se/c-se-u5.html`
- Status: ok
- Model calls so far: 33 (145,441 tokens in, 237,496 out), 7.8 minutes

## Checker

```
c-se-u5.html: 8 chapters, 15788 words, 9 figures, 203 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, the paragraph beginning "Locating test items is the mapping step": The paragraph mixes up test items with requirements. A test item is the thing being tested (a build, module, interface or document, identified by name and version). The mapping that the plan records is between requirements and test cases, not between test items and requirements. A student will carry this confusion into the RTM described in Section 3, where rows are requirements, not test items.
- ch 1 [low] Worked example 1, steps 2 to 6: The example treats the 40 automated cases as costing nothing: each full cycle is charged only for the 95 manual cases, and the two testers are assumed to work in perfect parallel. Re-running automated suites, checking their results and maintaining them takes real effort, so the 17.9-day answer is optimistic and the example does not say so.
- ch 2 [high] Worked example 1 (given numbers and step 3); Q3 and the exam traps rely on the same figures: The case counts do not add up. 480 cases cannot contain 456 passed + 24 failed + 6 blocked, because 456 + 24 + 6 = 486. Yet step 1 and step 2 divide by 480 (456 ÷ 480 = 95.0%, 6 ÷ 480 = 1.25%), and Q3 uses 480 − 6 = 474, which assumes the 6 blocked cases are inside the 480. Under that reading the failed count must be 480 − 456 − 6 = 18, not 24, so the failure count and the defect derivation in step 3 (24 + 6 = 30) contradict the rest of the example.
- ch 2 [high] Worked example 1, step 7, and the figure caption: The span of control is computed wrongly and contradicts the definition given in Section 2 ('the number of people one supervisor can supervise well') and the tree in the figure. The test manager supervises two leads directly, so the manager's span is 1:2. Step 7 counts the two leads inside the 12 'staff below the manager' and then divides by 2 supervisor positions, counting the leads twice; 12 ÷ 2 = 6 is not any supervisor's span. The figure caption also states 'a span of control of 1:6', which conflicts with its own tree (manager → 2 leads; functional lead → 8 engineers; automation lead → 2 engineers).
- ch 2 [high] Worked example 1, step 5 and step 8: A deferred defect is not closed; it is acknowledged and postponed, so it stays open until it is fixed. Step 5's claim 'so no defect is still open' is therefore wrong. Step 8 then declares the exit criterion 'no open severity 1 or 2 defect' as met, but the example never says what severity the 3 deferred defects have, so the verdict is not supported by the data.
- ch 2 [low] Section 2 (text describing the figure): The sentence says 'a group of 13: one test manager, a functional test lead with 8 test engineers, an automation lead with 2 automation engineers, and a domain expert'. Those people add up to 14. The figure caption treats the 13 as the line staff and puts the domain expert outside the line, so the two descriptions disagree and a student counting will get 14.
- ch 2 [low] Worked example 1 (defect severity sentence): '12 of severity 1 or 2, 14 of severity 3 and 4 of severity 4' is hard to parse on a phone; 'and 4 of severity 4' can be misread as one count.
- ch 3 [low] Exam traps, first bullet: "It finds regression, not new defects" is self-contradictory: a regression is itself a defect newly introduced by a change. A student can read this as saying automated tests never report a bug.
- ch 3 [low] Section 2, bullet list of pyramid layers: The classic test pyramid has three layers: unit, service/API, UI. Listing "Behaviour layer: Cucumber scenarios" as a fourth layer implies BDD sits at one level of the pyramid, which is wrong; Cucumber scenarios can drive unit, API or UI tests.
- ch 3 [low] Section 1, break-even formula: Section 3 lists run cost (machine time and people time to execute) as part of ROI, but the break-even formula R = B ÷ (M − A) contains no run-cost term. A student cannot see where run cost goes.
- ch 3 [low] Section 1 and Section 3, chapter cross-references: "The test plan from 5.1" and "the pipeline from 5.6 and 5.7" are bare numbers with no link, so a reader on a phone cannot jump to those chapters.
- ch 3 [low] Section 1, paragraph on strong candidates: "API checks and performance tests are strong candidates because they are fast and call little user interface" is awkward and unclear; "call" is not the right verb for a UI.
- ch 3 [low] Figure caption: "automation starts at 60 and rises by 2" gives 2 without a unit.
- ch 4 [low] Section 2, execution progress and the definition of executed: Two neighbouring sentences pull in opposite directions: 'A case counts as executed once it has a result — pass, fail or blocked' and 'A blocked case cannot run'. A student may ask how something that could not run is counted as executed.
- ch 4 [low] Worked example 1, question and answer: The question asks which number to raise 'at the go/no-go meeting', but the leakage figure (10%) comes from the first six months after release, which is not known at that meeting. The timeline in the scenario and the timeline in the question do not match.
- ch 4 [low] Worked example 1, step 6 and answer: Calling 10% leakage a sign that 'the exit criteria let too many defects through' is a judgement stated as fact. No benchmark or earlier release is given, and the chapter itself warns against comparing across dissimilar projects and treating measures as targets.
- ch 5 [low] Section 1, the commit id formula: The formula id = H(tree, parents, author, message) leaves out the committer identity, the commit timestamps and the timezone, all of which Git feeds into the hash. A student may conclude that the author name and the message alone fix the id, and then be confused when two commits with the same tree, author and message get different ids because they were committed at different times or by different committers.
- ch 5 [low] Figure, node D: D is drawn at the same horizontal position as C, one row below it (x = 2 for both), although D's parent is B. On a phone a reader can easily read the vertical alignment as C → D, i.e. the feature branch splitting off main after the release commit, which contradicts the caption and the edge list.
- ch 6 [low] Worked example 1, step 3: The sentence "Shard length = 20 ÷ 4 = 5 min. 26 min replaces 20 min." is wrong and confusing: the shard stage is 5 min, and 5 min replaces the 20-minute integration stage. 26 min is the new total, not a replacement for 20 min.
- ch 6 [low] Section 1, table row "Who decides to ship?": "Nobody yet" is unclear for the CI column. CI alone does not fix who ships or when; the entry reads as if no one ever decides.
- ch 7 [low] Section 2, fail-fast ordering: The section says 'put the shortest tests first' and then lists the order as compile, unit tests, static analysis. In most projects static analysis (lint, type check) is far cheaper than the unit-test suite, so keeping it after the tests contradicts the rule the paragraph is teaching, and a student will copy the wrong order.
- ch 7 [low] Section 3 and quiz Q8, artifact name 2.3.0-231: The hyphen form is used for release plus build number without a warning. Under Semantic Versioning a hyphen suffix (2.3.0-231) marks a pre-release, which sorts before 2.3.0 and is not a build number at all; build metadata uses '+'. A student who meets SemVer later will apply the wrong rule.
- ch 7 [low] Figure: The prose says the run 'ends with one immutable artifact', but the diagram's last node is 'Deploy to dev', placed after 'Publish artifact'. The aria text also says the diagram ends in artifact 2.3.0-231, which does not match the node list.
- ch 7 [low] Worked example 1, step 5 and answer: '9.23 times shorter' is ambiguous English: the ratio 1800 ÷ 195 = 9.23 means the full build takes 9.23 times as long, not that the short build is 9.23 times shorter.
- ch 8 [low] Worked example 1, step 1: On a fresh host the template output changes, so the reload handler is notified and does run at the end of the play. In a real recap a handler that runs is also counted in the changed column, so the first-run recap usually shows 4 changes per host, not 3. The example counts only the three declared tasks and never says why the reload is excluded.
- ch 8 [low] Worked example 1, step 3; quiz Q3: An unreachable host is not a failed host. Ansible's PLAY RECAP keeps a separate unreachable column, so a host that cannot be reached is reported as unreachable=1 with failed=0. The text says 'the recap shows 11 ok and 1 failed', and the quiz answer says 'failed hosts = 2', which will not match what a student sees on the terminal.
- ch 8 [low] Beyond: 'Real estates use dynamic inventories' reads like property or land, not server fleets.
