# e-python-u6: free-model run

- Book: `books/common/e-python/e-python-u6.html`
- Status: ok
- Model calls so far: 23 (78,481 tokens in, 183,413 out), 6.4 minutes

## Checker

```
e-python-u6.html: 7 chapters, 11422 words, 8 figures, 136 KB
OK
```

## For the reviewer

- chapter 4: a python program's shown output was replaced by its real output; check the text around it

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, last sentence: "The stored type and shape are fixed when the array is made" is wrong for shape, and it contradicts Section 4 of the same chapter, where a.reshape(3,2) changes the shape of the same data. A student will not know which statement to believe.
- ch 1 [low] Section 2, slice description: a[0:2, 1:3] is called "a 2 by 2 block of columns 1 and 2". The row part of the slice is never explained, so a student may think both slices act on columns.
- ch 1 [low] Section 4, axis explanation: The text does not say that the summed axis disappears from the result. a.sum(axis=0) returning length 3 and a.sum(axis=1) returning length 2 can look arbitrary.
- ch 2 [low] Section 1, list-of-dictionaries paragraph: The phrase 'such as records read from a CSV file' can make a student think a CSV is normally loaded by first building a list of dictionaries around Python's csv module. Pandas reads a CSV straight into a DataFrame with one call, and that call is never mentioned.
- ch 2 [low] Section 3, merge paragraph: 'pandas is comfortable with thousands of rows, not millions' overstates the limit. pandas handles millions of rows; the real limit is available RAM and how many columns and object (string) columns the table has.
- ch 2 [low] Lead: Calling the chapter's topic 'data wrangling' treats two different things as names for the same idea. Data wrangling is the general activity of cleaning and reshaping data; pandas is one tool used for it.
- ch 2 [low] Figure spec: The spec gives the row labels and cell values but no list of column headers, so the rendered table will not show Math, Sci and Total even though the aria text and the caption refer to them.
- ch 2 [low] Quiz Q4: The answer gives the two statements but not what the second one produces, so a student cannot self-check. df.loc['Asha'] returns the row as a Series named 'Asha' with entries Math, Sci and Total.
- ch 3 [low] Section 1 and exam trap 3: The claim that a non-square A means the system 'does not have one unique solution in the usual sense' is too absolute. An overdetermined but consistent system, such as x = 1 and 2x = 2, does have exactly one solution; only the square-solve call is unavailable for it, and least squares is the standard tool there.
- ch 3 [low] Section 2 (estimator definition): 'An estimator is an object with fit, predict and score' is not true of all estimators: transformers such as StandardScaler have fit and transform but no predict, and clustering models have no score by default. A reader can be confused when StandardScaler is called an estimator two paragraphs later.
- ch 3 [low] Section 2 (train_test_split): 'test_size=0.2 means 20% of rows go to test' hides the rounding. scikit-learn rounds the test count up with ceil, so for 7 rows and test_size=0.2 the test set has 2 rows, not 1.4.
- ch 3 [low] Worked example 1, steps 3 and 4: The wording 'scipy.linalg.solve computes x = (5×3 − 1×6)/5' presents Cramer's rule as if it were the library's method. solve uses LU decomposition with partial pivoting; Cramer's rule is only the hand-check here.
- ch 3 [low] Figure spec: The 'split' node carries the note 'fit on train', the same note as the 'scale' node, so the figure does not say what the split step actually does.
- ch 4 [high] Worked example 1, code block and output: The question asks for a Tkinter program (root, Label, Entry bound to a StringVar, Greet Button), and steps 1–9 describe one. The [code] block, however, shows an ordinary function def greet(name): return 'Hello, ' + name with name = 'Asha' and print() calls. That code creates no window, no Entry and no StringVar, and it reuses the name greet for a completely different function than the one in step 6. A student who copies the block gets console text, not a GUI.
- ch 4 [high] Section 3, events paragraph: widget.bind("", handler) passes an empty string as the event sequence. An empty sequence is not a valid event and Tkinter raises a TclError when bind is called, so the example as printed cannot work.
- ch 4 [low] Section 2 table, Frame row: The 'key option or method' column gives 'parent' for Frame, but the parent is the first constructor argument of every widget, not an option or a method. The cell tells a student nothing about Frame in particular.
- ch 4 [low] Section 2 table, Listbox row: A Listbox is described as a 'Scrollable list of lines'. A Listbox does not scroll on its own; it needs a Scrollbar linked through yscrollcommand, or a mouse wheel.
- ch 4 [low] Worked example 1, steps 3–8: None of the widgets in the example is placed with a geometry manager. As written, the program runs without error but the root window stays empty, so a student reproducing the steps sees a blank window.
- ch 4 [low] Section 3, Entry and Text indices: 'Use "end" as the insert index and 0 as the first delete index' is stated just before the Text widget is introduced. Those indices are for Entry; in a Text widget the first position is "1.0" and 0 is not a valid Text index.
- ch 4 [low] Section 1, mainloop paragraph: 'Without mainloop() the window appears and vanishes' is misleading. Until the event loop (or an update call) runs, the window is normally never drawn at all; only in some environments does it flash for a moment. The two cases are presented as one.
- ch 5 [high] Quiz Q3: The vertical padding answer (8 px) is wrong. The Label and the Entry share row 0, so their pady does not add up. Grid makes the row tall enough for the tallest widget plus its top and bottom padding. With pady=2 on both widgets the row gains only 2 + 2 = 4 px of height, not 2 x 2 x 2 = 8 px. The horizontal case is different and the answer there is right: each widget sits in its own column, so padx adds 4 + 4 px to column 0 and 4 + 4 px to column 1, giving 16 px.
- ch 5 [low] Lead: The names are swapped. Tkinter's own term is geometry manager (pack, grid, place); 'layout manager' is the general term used by other toolkits. Saying 'Tkinter calls it a layout manager' teaches the opposite of the standard usage.
- ch 5 [low] Section 1, grid paragraph: padx and pady are called padding 'around the cell'. In grid they are padding around the widget inside its cell; the cell then grows to hold widget plus padding. The wording makes students think the gap is drawn between cells.
- ch 5 [low] Exam traps, relief bullet: 'relief=raised looks flat on its own' overstates it. The default borderwidth is 1 pixel, not 0, so a raised bevel is drawn, just thin.
- ch 6 [low] Lead: The sentence 'A lock, or a thread-safe queue, makes the order safe' suggests that a Queue protects shared variables too. The Exam traps later state the opposite (a Queue does not replace a lock for a shared counter), so a student meets two different messages.
- ch 6 [low] Section 3, Queue paragraph: It says put(block=True) waits if full, but does not say that Queue() with default settings has maxsize=0, which means unbounded, so put never blocks unless maxsize is set. A student may think put blocks by default.
- ch 6 [low] Worked example 1, step 2: 'Repeating this gives a final value below 200000' is stated as certain. A lost update is only possible, not guaranteed: in normal CPython the GIL switch interval is large next to the load-add-store window, so the unlocked version of this exact code usually still prints 200000. A student who runs it will think the chapter is wrong.
- ch 7 [high] Worked example 1, step 5: The comparison operator is missing: '40  30' is not a valid comparison, so the step does not show why 40 becomes the right child of 30.
- ch 7 [high] Quiz Q3, answer: The comparison operator is missing: '35  30' is not a valid comparison, so the insertion path is incomplete and confusing.
- ch 7 [low] Section 2, 'Search cost is height + 1 comparisons': Height is used without a definition, and the formula is the worst-case cost only; a search that finds the root takes 1 comparison, not height + 1.
- ch 7 [low] Quiz Q6: Inorder, preorder and postorder are binary-tree traversal orders; calling them 'depth-first traversal orders' can confuse students with graph DFS, where these names are not used.
- ch 7 [low] Worked example 1, step 8 and Section 1: The example says to build the list by appending 10, 20, 30, but Section 1 only explains insert at head and delete head; appending at the tail is not defined.
