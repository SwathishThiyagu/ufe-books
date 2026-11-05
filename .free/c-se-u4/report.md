# c-se-u4: free-model run

- Book: `books/cse/c-se/c-se-u4.html`
- Status: ok
- Model calls so far: 26 (94,401 tokens in, 180,854 out), 5.1 minutes

## Checker

```
c-se-u4.html: 9 chapters, 16550 words, 10 figures, 178 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1, output block: The output lists 2000, 3000, 3500, 500 with no labels or units. A student cannot tell which number is the cash dispensed, the expected balance, the actual balance and the difference, so the block does not connect to steps 6 and 7.
- ch 1 [low] Quiz Q6: The question asks which principle decides where to test first, and the answer names defect clustering, but the reason given ('a defect there costs money and blocks users') is risk and impact, which is a separate idea. Clustering only helps if past defect data shows the payment module is a hot spot.
- ch 2 [low] Exam traps, first bullet: The trap heading and its correction do not match. The heading warns against 'saying testing is the only form of validation', but the correction talks about reviews and inspections being verification, which is a different mistake. A student cannot tell what error is being warned against.
- ch 2 [low] Section 3 and Quiz Q4: The two pairs are treated as one list of four exclusive labels, but they are on different axes: an acceptance test is validation and also QC, and a document review is verification and also QC. Q4 forces each item into a single label, which contradicts Section 3's line 'Reviews of deliverables and all testing are QC.'
- ch 2 [low] Worked example 1, step 5: Two users missed the 30-second target (38 s and 45 s), but step 5 mentions only the 45 s path getting a defect report, as if the 38 s run were acceptable.
- ch 2 [low] Section 2, V-model paragraph: The mapping merges two levels: 'design matches system and integration testing'. It hides which design level pairs with which test level, so the one-to-one pairing the V-model is famous for is lost.
- ch 3 [high] Exam traps, fourth bullet: The condition in the trap is cut off: "such as if (a > 0 && b ;" is not valid code, so the explanation that follows ("the two tests may leave b < 5 always true") cannot be understood. The reader cannot see which compound decision is being discussed or which sub-condition went untested.
- ch 3 [high] Quiz Q5 (question and answer): Both the question and the answer are broken. The question reads "if (x > 0 && y ." with no closing condition, and the answer contains the fragment "because y  0 and for y < 10" — a missing operator and missing words. A student cannot tell what is being tested or why condition coverage fails.
- ch 3 [low] Figure and worked example, step 1: The CFG labels jump from 3 to 5 and from 7 to 9, with no nodes 4 and 8. Readers may think two nodes were lost, and the count N = 8 then looks wrong.
- ch 4 [high] Section 2, bullet on yes/no conditions: It says a yes/no condition has one valid class (true) and one invalid class (false). When the specification allows either answer, both true and false are valid classes; calling false invalid is wrong and a student will repeat it in the exam.
- ch 4 [low] Section 2, fourth bullet: "Write one test case per class ... so the number of test cases equals the number of classes" is only true for a single input item. With several input items, one test case usually carries a valid representative from each input at once, so the count is not simply the number of classes.
- ch 4 [low] Section 2, bullet on lists: "A list of n items: classes for 0 items, 1 to max items, and more than max" mixes n and an undefined "max", so the symbol is not tied to the rule.
- ch 4 [low] Worked example 1, step 7: The fare check appears from nowhere: the specification in the example mentions only age and the senior discount, and a railway fare depends on many things besides age, so the step does not follow from the rules read in step 1.
- ch 5 [high] Worked example 1, parts (a) and step 2 (and the figure): The design says calculateGST(amount, rate) takes rate as a parameter, yet the test also uses a 'stub tax table' that supplies rate = 18, and the driver call is written as calculateGST(1000, stubTaxRate('GST')). That makes the driver call the stub, which directly contradicts the chapter's own rule and exam trap: the driver calls the unit, the stub is called by the unit.
- ch 5 [low] Figure (spec and caption): The diagram shows calculateGST calling both a tax-table stub and an Invoice stub, but in the worked example Invoice is called by Billing, not by calculateGST. The edge u→log also shows the unit sending its result to the result log, while the text says the driver/harness records the result.
- ch 6 [high] Section 3, Exam trap 4, Quiz Q6: The chapter defines a defect bash as a team session where developers 'fix many reported bugs together'. In standard usage a bug bash (defect bash) is a time-boxed event in which many team members test the product to find as many defects as possible; the fixing happens afterwards. As written, a student who answers Q6 faithfully to the textbook definition will clash with this common meaning, and the trap 'treating a defect bash as a test level' rests on that definition.
- ch 6 [low] Section 1, last two sentences: 'It is validation at product level: the product must meet the stated requirement and the user's need.' Meeting the stated requirement is verification; meeting the user's unstated need is validation, and that is exactly what Section 2 gives to acceptance testing. Mixing the two in one sentence blurs the distinction the chapter relies on.
- ch 6 [low] Section 1, first paragraph: 'A test case has preconditions, steps and one expected result' sits awkwardly beside the UPI example, which expects three values (A, B and the total). A reader may think the example breaks the rule.
- ch 7 [low] Section 2 and worked example step 6 / Figure: The figure says the 12 impact-selected tests contain only 'GST invoice', but step 6 says those same 12 tests include checkout total, payment amount and refund recalculation as well. The two descriptions of the same set disagree, and a student may think impact selection picked a single feature rather than the tests that exercise the invoice code path.
- ch 7 [low] Worked example step 8 and answer, Quiz Q6: 'Runs about 41.7 times fewer tests' is loose English and can be read as 500 minus 41.7×12. The intended meaning is a ratio of test counts.
- ch 8 [high] Section 3 (configuration, compatibility and internationalisation), currency example: The text says “The same amount is ₹1,23,456.78 in India and $123,456.78 in the US.” The digit strings are the same, but the amounts are not: ₹1,23,456.78 is roughly a thousand times smaller than $123,456.78. A student can read this as 1 rupee = 1 dollar. What the example is really showing is grouping (lakh style vs thousand style) and the currency symbol, not an equal amount.
- ch 8 [low] Quiz Q8 answer: Calling internationalisation testing “grouped under configuration testing” is loose. It is a separate type of non-functional test that this chapter happens to place in the same section; it is not a subset of configuration testing.
- ch 8 [low] Section 1, opening paragraph: The split “a performance test runs at expected load; a load test runs at the expected peak” is not the standard textbook split. Most syllabi use performance testing as the umbrella term, with load testing one of its types: running the system at anticipated load, including peak load.
- ch 9 [low] Lead and Section 3: The lead says the chapter extends 'the configuration testing from Chapter 8', but Section 3 says 'Configuration testing from 4.8 gives the matrix method'. A student cannot tell where configuration testing is actually covered.
- ch 9 [low] Section 1, first sentence: 'Some syllabi call this testing OO systems and website testing' is garbled and drops mobile, so the alternative name does not match the chapter title.
- ch 9 [low] Section 1, state-based testing: It says 'Use the state chart from Unit 3', but the rest of the chapter refers to chapters by number (4.4, 4.5, 4.8), so the naming of cross-references is inconsistent.
