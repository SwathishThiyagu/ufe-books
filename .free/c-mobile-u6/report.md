# c-mobile-u6: free-model run

- Book: `books/cse/c-mobile/c-mobile-u6.html`
- Status: ok
- Model calls so far: 45 (152,516 tokens in, 234,655 out), 6.2 minutes

## Checker

```
c-mobile-u6.html: 8 chapters, 11872 words, 9 figures, 140 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Worked example 1, step 1: The step shows the Swift line 'let baseFare: Double = 20.0 rupees'. The word 'rupees' after the literal is not Swift and would not compile, so the code as printed is wrong.
- ch 1 [high] Exam traps, last bullet: It says Double is 'the usual choice for money'. Binary floating point cannot hold most decimal money values exactly (0.1 + 0.2 is not 0.3), so standard practice is Decimal or integer paise for currency. Telling students to store money in Double teaches a rounding bug.
- ch 1 [low] Figure spec (title): The figure title says 'Three names, their types and their values' but the array has four rows (baseFare, rate, km, total), and the surrounding text also says four slots.
- ch 1 [low] Worked example 1, step 3 and figure: km is declared with var but is never changed, which makes the compiler warn 'variable was never mutated; consider changing to let'. As written it also blurs the chapter's own rule for choosing var.
- ch 2 [high] Section 1: Operators and ranges: The sentence 'Comparison operators == !=  = produce a Bool' is broken: two operators are missing and '=' (assignment) is shown as producing a Bool. Assignment does not produce a Bool in Swift, and a student will read '=' as a comparison.
- ch 2 [low] Section 2: Branching and looping (switch example): The switch snippet is followed by '[shown output]' but the code contains no print statement and no declaration of km or rate, so there is nothing to show as output.
- ch 2 [low] Section 3: Strings and functions: 'The word before a parameter is its argument label' is misleading. The full form is func f(label name: Type), so the label is the word before the parameter name, not before the parameter; when only one word is written it acts as both, as with km in fareLabel(km:).
- ch 3 [low] Section 1 (structs): The chapter says the memberwise initializer is automatic, but does not say it disappears once the struct declares any initializer of its own. A student who adds a custom init and still writes Trip(km: 8) gets a compile error, which is exactly the kind of question that comes up.
- ch 3 [low] Section 1 / Exam traps (mutating): The mutating rule is stated only as 'a method that changes a stored property must be marked mutating'. The companion rule is missing: a mutating method cannot be called on a constant (let) instance, the compiler rejects it with 'cannot use mutating member on immutable value'. Students lose marks here because they mark the method mutating but declare the instance with let.
- ch 4 [high] Section 1 and Quiz Q1: The chapter says a scheme chooses the target, configuration and run destination. In Xcode, the run destination is selected separately in the toolbar; a scheme stores build/run/test/profile/analyze/archive actions, target(s), build configuration and executable/launch settings. Quiz Q1 repeats the same error.
- ch 5 [low] Section 1, first sentence of the UIKit layer: It says UIResponder sits 'at the root of the tree'. The actual root class is NSObject; UIResponder is a subclass of NSObject and is only the base of the responder chain (views and view controllers). A student can come away thinking UIResponder has no superclass.
- ch 5 [low] Section 3, after the @IBAction code block: The '[shown output]' placeholder is empty. There is no stated output for the action code, so a reader cannot tell what the action does on screen.
- ch 5 [low] Worked example 1, step 4 and answer: The code writes fareLabel.text = "₹92", but the answer says the label shows ₹92.00. The code and the stated output are not the same string.
- ch 5 [low] Worked example 1, step 5: 'Put the connection check nowhere else' is unclear — it is not a check, and a reader may think some check must be added somewhere.
- ch 5 [low] Figure, aria description: The aria text says 'UIView branching to UIControl and UIButton', but the tree shows UIView → UIControl → UIButton. A screen-reader user gets a different hierarchy from the drawn one.
- ch 6 [high] Exam traps, fifth bullet: It says that connecting a control's event to a method whose signature has no sender parameter causes an 'unrecognized selector' crash. That is wrong. Target-action accepts zero-argument methods such as @IBAction func fareChanged() as well as one-argument and two-argument forms, so a missing sender parameter never crashes anything. The real cause of an unrecognized selector is a stale storyboard connection to a method that was renamed or deleted.
- ch 6 [high] Quiz Q4: The question states that sorting the array in place without reloadData() makes the table 'crash on a tap'. Sorting keeps the same number of rows, so no index goes out of range and no crash happens; only the wrong fare is passed on. The model answer itself contradicts the question by saying the crash occurs only 'if the array shrank'.
- ch 6 [low] Quiz Q7: The question says a bar button item already has a UIMenu assigned, but the first cause in the answer is that the menu property was never assigned. The answer also mentions showsMenuAsPrimaryAction, which applies to a plain UIButton, not to a bar button item.
- ch 7 [high] Section 1, paragraph on ambiguous and unsatisfiable layouts: Says both defects are 'cured by deleting a rule'. That is only true for an unsatisfiable layout, which has too many conflicting rules. An ambiguous layout has too few rules — one equation and two unknowns — so deleting a rule makes it worse. The chapter's own quiz Q5 deletes a rule, but that case is unsatisfiable, not ambiguous.
- ch 7 [high] Section 2, distribution bullet for .fill: Defines .fill as 'the last child absorbs slack'. UIStackView does not pick the last arranged subview. It stretches whichever child has the lowest content hugging priority (or shrinks the one with the lowest compression resistance), so the slack can go to any child, and often goes to a label.
- ch 7 [low] Section 1, priorities paragraph: 'Priority 1000 is required and cannot be dropped' contradicts the chapter's own statement later (and the Q5 answer) that the runtime breaks one constraint and logs the conflict. A student will ask which is true.
- ch 7 [low] Section 1, first sentence of 'Constraints are equations': Says a constraint is 'one linear equation'. Many real constraints are inequalities, written with ≥ or ≤ (for example a minimum height or 'greater than or equal' spacing), which the Beyond note itself mentions. Students then read '≥ 44' and think it is not a constraint.
- ch 8 [high] Section 2 and exam trap 3: The chapter says a show segue 'works only inside a navigation controller' and that using one outside a navigation controller 'does nothing useful'. That is wrong. A show segue outside a navigation controller does not fail silently; UIKit falls back to presenting the destination modally. So the screen does appear, but without a push, back button or navigation bar. A student will answer the trap question wrongly in an exam.
- ch 8 [high] Section 3: 'prepare(for:sender:) is the only correct place to hand data to a destination' is a false absolute. It is the correct place for a storyboard segue. For a programmatic push you instantiate the destination and set its properties before calling pushViewController(_:animated:). Handing data through an initializer or a closure is also valid. Stated as written, a student would mark the code-only route as wrong.
- ch 8 [high] Section 3 and exam trap 1: tableView.indexPathForSelectedRow is a property of the source table view controller's table view. The destination view controller has no access to that table view, so it cannot read this property in its viewDidLoad at all. The stated reason, that the selection 'may already be cleared', is also wrong: UIKit does not deselect the row automatically when you push. Deselection is manual.
- ch 8 [low] Section 1: 'set navigationItem.largeTitleDisplayMode and prefersLargeTitles' blurs where each property lives. prefersLargeTitles is a property of the navigation bar, not of navigationItem, so a student may write navigationItem.prefersLargeTitles and get a compile error.
- ch 8 [low] Section 2, pseudo code block: The line '[shown output]' is left empty, so the reader cannot see what the snippet produces.
