# c-se-u1: free-model run

- Book: `work/claude_figs/c-se-u1/tree/books/cse/c-se/c-se-u1.html`
- Status: ok
- Model calls so far: 51 (199,202 tokens in, 325,097 out), 12.8 minutes

## Checker

```
c-se-u1.html: 7 chapters, 13183 words, 8 figures, 170 KB
OK
```

## For the reviewer

- chapter 6: the figure cannot be drawn: tree is too wide (5 leaves); use fewer leaves or shorter labels
- chapter 1: the figure cannot be drawn: note "2 payroll systems" runs off the right edge; shorten it
- chapter 1: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 2 and the figure note and Worked example 1 (steps 5 and 9) and Quiz Q5: Legacy software is listed as an application domain and the payroll systems are said to fall 'under legacy, not under application software'. Legacy is a status (old, still in production, still business-critical), not a domain: a payroll system is application software that happens to be legacy. A student who copies this exclusive classification into an exam answer is marked wrong, because domains in the standard lists do not include legacy at all.
- ch 1 [high] Section 3, myths table, row 2: The myth 'a general statement of the objective is enough to start coding' is put under the management group. Standard textbook groupings place it under customer myths ('a general statement of objectives is sufficient to begin writing programs; we can fill in the details later'). A student reproducing the table by group loses marks.
- ch 1 [low] Section 2, application domain list, application software bullet: The bullet says 'Web and mobile apps are the largest modern sub-class' of application software, while the next-but-one bullet lists 'web and mobile applications' as a separate domain. A student cannot tell which domain a web app belongs to.
- ch 1 [low] Section 2, four shapes of software, software as a service: 'the customer pays a subscription and uses the vendor's running system, like a GST filing portal billed per return' mixes a subscription model with per-use billing, so the defining feature of SaaS reads unclearly.
- ch 2 [low] Lead paragraph: The lead says the essence of practice sits "underneath" the layers, but it places this right after describing a stack whose base is the quality focus. A student can read it as a fifth layer below the quality focus, which contradicts Section 1 and the figure.
- ch 2 [low] Section 1, quality-focus example: "at most 2 defects per thousand lines of code (KLOC) at release" attaches the abbreviation to the spelled-out phrase in a way that hides what KLOC stands for. Defect density is normally quoted as defects per KLOC.
- ch 2 [low] Figure side notes: The side label 'hard to change' is placed at the bottom, level with the quality focus. Read literally, it says the quality focus is hard to change, which is not the intended point and can confuse a student comparing it with the text that tools are 'least decisive'.
- ch 3 [low] Section 3, Testing paragraph: The paragraph says testing checks the assembled product, then lists a unit test, which checks one module, not an assembled product. This also overlaps with Construction, whose exit criterion already requires unit tests to pass.
- ch 3 [low] Section 3, final paragraph and Exam traps, second bullet: The post-go-live change path lists requirements, design, construction and testing but omits deployment. A changed product still has to be released, and the worked example and quiz Q4 include deployment.
- ch 3 [low] Figure: The Testing node note says 'system and acceptance' but the text says testing includes unit, integration, system and acceptance tests. The figure can suggest that integration testing is not part of testing.
- ch 3 [low] Quiz Q7: The question asks for four feasibility questions, but the answer gives four feasibility types. The body lists the questions themselves.
- ch 4 [high] Section 4, process model families: Spiral is grouped with the prescriptive models, but the same paragraph then defines evolutionary models as those that grow with the product. Standard textbooks treat the spiral model as an evolutionary (iterative) model, so a student who learns this line will classify spiral wrongly in the exam.
- ch 4 [low] Section 3, umbrella activities list: The text says six umbrella activities 'are commonly listed', but standard lists also include software project tracking and control (and reusability management). A student who answers with only these six can lose marks on a 'name the umbrella activities' question.
- ch 4 [low] Section 3, technical reviews bullet: 'done before the product is tested' makes reviews sound like a single stage placed before testing. Reviews of requirements, design, code and test plans happen throughout the project, each one before the work product is used by the next activity.
- ch 4 [low] Section 4 and Quiz Q7, concurrent model states: The state name 'under review' is used where the usual textbook state list is inactive, awaiting changes, under development, under revision, and done. 'Awaiting' is also left without its object, so 'awaiting' alone is unclear.
- ch 4 [low] Figure and its caption: The caption says umbrella activities run alongside every framework activity 'shown by the dashed links', but the figure spec draws dashed links only to Communication and Deployment, so the picture contradicts the caption.
- ch 5 [low] Section 2, spiral four sectors, intro line: "Each loop covers one part of the product" is not how the spiral works. A loop is a level of elaboration driven by risk, and a loop may revisit the same part rather than build a separate part. As written, students will think the spiral is just feature slicing, and will be unable to explain how it differs from incremental beyond the risk step.
- ch 5 [low] Section 3 table, Spiral row, column 'Cost of change': The cell says "risk-led reviews each loop", which answers a different question. It does not state the cost of change for spiral, so the column breaks and a student comparing models gets no value for spiral.
- ch 5 [low] Section 3 table, Spiral row, column 'User sees working software': "every loop" overstates the model. The first loops of a spiral often deliver a prototype, a simulation or a specification used to cut risk, not shippable software. The cell as written contradicts the chapter's own example of prototyping inside the risk sector.
- ch 6 [high] Section 4 (Conventional versus agile), final paragraph before the figure: The sentence is broken and duplicated: '...then agile increments. Agile is not' appears, then 'Agile is not a licence to skip planning...' starts again. A student reads a truncated fragment in the middle of the argument.
- ch 6 [high] Worked example 1, step 8: The step says 'Order the work by value, not by size', but the order it then gives (payment 13, search 8, login 5, report 3, help 2) is exactly the order by size. It teaches the opposite of what it states, and a student will conclude that the biggest story is automatically the most valuable.
- ch 6 [low] Section 1, paragraph on velocity: 'Agile measures progress with velocity' conflicts with the earlier principle, repeated in the same section, that working software is the main measure of progress. Velocity is a planning number, not a progress measure.
- ch 6 [low] Section 1, velocity formula: 'velocity = story points finished in one iteration ÷ 1 iteration' divides by a meaningless 1. It suggests velocity is a ratio of two quantities when it is simply points per iteration.
- ch 6 [low] Section 3, twelve practices, 'Testing and integration' group: The 40-hour week (sustainable pace) is filed under testing and integration, where it does not belong; it is a programmer-welfare practice. The group label misleads students revising the twelve practices by group.
- ch 7 [low] Lead: The lead says causes are 'people, process and requirement conditions', but Section 1 and the figure cluster them as requirements, management and engineering. A student may look for a 'people' branch that does not exist.
- ch 7 [low] Worked example 1, step 4: The testing window uses the inclusive formula 6 − 5 + 1 = 2, but the '+1' is not explained. A student counting 6 − 5 will write 1 month and think the answer key is wrong.
- ch 7 [low] Worked example 1, step 5 and answer: 'Testing starts in month 5' is known from the project plan on day 1, so it is a plan fact rather than the emerging warning sign the chapter defines in Section 2.
- ch 7 [low] Section 2, warning signs list: 'requirements marked to be decided near build' is compressed and reads oddly; students may not see that it means decisions postponed until near the build phase.
- ch 7 [low] Section 2, last line: 'Late hiring adds training and communication load' sits alone with no link to the retrospective or prevention advice around it, so it reads as an orphan remark.
