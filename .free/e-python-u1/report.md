# e-python-u1: free-model run

- Book: `books/common/e-python/e-python-u1.html`
- Status: ok
- Model calls so far: 25 (87,865 tokens in, 165,382 out), 4.4 minutes

## Checker

```
e-python-u1.html: 8 chapters, 14682 words, 9 figures, 151 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3, pseudocode block: The pseudocode is followed by an empty "[shown output]" placeholder. The reader is shown the steps but never the result, so the link between the plan and the answer (₹126) is left unstated here, although the worked example later gives it.
- ch 1 [low] Quiz Q6, answer: The answer refers to "Two input steps read the data", but the question never mentions how many inputs there are or what is read. A student comparing answer to question will be confused about where those steps came from.
- ch 1 [low] Quiz Q5, answer: The repetition is written as "repeat 5 times", which is not the repetition syntax the chapter defined (WHILE condition ... ENDWHILE). The answer should use the same fixed shape that Section 3 taught.
- ch 2 [high] Figure (timeline spec) in Section 2: The Python 2 lane draws one bar from 2000 to 2008 and the next only from 2010 to 2020, leaving 2008-2010 blank. The chapter itself says the two lines overlapped from 2008 to 2020, and in reality the 2.x line was in use the whole time (2.6, then 2.7 from 2010). The figure contradicts the text and the history it is meant to show.
- ch 2 [low] Figure aria text / spec in Section 2: The Python 3 bar has a fixed end year of 2025, but the aria text and the surrounding prose say Python 3 runs 'to today'. In any later year the bar is wrong and the picture looks like Python 3 stopped.
- ch 2 [low] Section 2 heading: The heading promises 'three dates that matter', but the section gives five years: 1991, 2000, 2008, 2010 and 2020. A student counting the dates thinks a date is missing.
- ch 3 [low] Exam traps, item 1: The first trap is written as a flat statement of fact — 'A name typed at the prompt is still there tomorrow' — which is false and directly contradicts Section 2. Every other trap in the list is phrased as a mistake the student makes, so this one reads like a rule to memorise.
- ch 3 [low] Exam traps, item 5: 'A line below a failed line may not run' is vaguer than the truth. When a script hits a runtime error, execution stops there and every line below it does not run at all.
- ch 4 [low] Section 2, identifier rules: The rule 'Allowed characters are a–z, A–Z, 0–9 and underscore' is a simplification. Python 3 also accepts Unicode letters and digits in identifiers, so names like π or a Devanagari word are legal; a student who sees one working will think the rules in this section are wrong.
- ch 4 [low] Section 2, keyword list: The list leaves out async, await and nonlocal, which are keywords in Python 3. A student may then treat async as a legal variable name, and the answer key for Q8 looks incomplete.
- ch 4 [low] Section 1, first paragraph: An assignment's left side is not always a plain name; a subscript or attribute target such as marks[0] = 45 or obj.price = 45 is also legal. Stating 'a left side (a name)' will contradict what students meet in the lists chapter.
- ch 4 [low] Worked example 1, dry run table: The dry run rows are numbered 1, 2, 3 but the same three lines are steps 7, 8, 9 in the step list. Readers may look for a mismatch between the two numberings.
- ch 4 [low] Beyond: 'Linters such as pycodestyle flag bad names' overstates the tool. Naming-convention checks (snake_case, CapWords) come from the pep8-naming plugin used with flake8; pycodestyle itself only flags ambiguous names such as l, O and I.
- ch 5 [high] Section 2: The text says the letter j marks the imaginary part. In 3 + 4j, the imaginary part is 4.0; j is the imaginary unit, the square root of −1. This contradicts the standard definition of real and imaginary parts.
- ch 5 [low] Section 2 and Exam traps: The rule "Never test two floats with ==" is too absolute. Equality is safe for exactly representable values such as 0.5, and the real issue is computed floating-point results like 0.1 + 0.2.
- ch 6 [high] Section 4, comparisons paragraph: The sentence is broken and half the content is missing: "Python chains comparisons, so 1  means 1 not flips a boolean, and is true only when both sides are true, or is true when at least one side is." The chained-comparison example has lost its operators and the sentence about not/and/or has lost its opening, so a student cannot read it.
- ch 6 [high] Quiz Q2 answer: The answer starts with the stray text "4? No —", which puts a wrong value (9 / 3 = 4) in front of the student before the correction.
- ch 6 [high] Section 3, mixed types paragraph: "Two ints stay int for + - * // % **, with / the lone exception" is wrong for **. When the exponent is negative the result is a float: 2 ** -1 is 0.5, not an int.
- ch 6 [low] Section 2, precedence ladder: The comparison rung lists only > >= == != and leaves out < and <=, so the ladder is incomplete.
- ch 6 [low] Lead: The lead uses "order of operations" for the tie-break between equal operators, but Section 2 (and the chapter title) use that phrase for the whole precedence system and call the tie-break associativity. The same term carries two meanings.
- ch 6 [low] Section 3, first sentence: "rounds down to the nearest whole number below the exact answer" reads as if the answer must be strictly smaller, which would make 8 // 2 equal to 3.
- ch 6 [low] Section 4, falsy values: The list of false values stops at 0, 0.0, an empty string and None; empty lists, tuples, dicts, sets and the value False itself are also false, and students meet them early.
- ch 6 [low] Beyond: The operator module does not "extend precedence into element-wise array arithmetic"; it only supplies named functions such as operator.add for the existing operators. Element-wise array arithmetic comes from NumPy, not from operator.
- ch 6 [low] Beyond: Spreadsheets do not use an identical rule set: Excel evaluates -2^2 as 4 because its unary minus binds tighter than the power, the opposite of Python, and its % is the percent sign, not a remainder operator.
- ch 7 [high] Worked example 1 (task line, code block and steps 1–2): The task says the program 'asks for a name and a birth year', and steps 1 and 2 trace name = input("Name: ") and year = int(input("Birth year: ")), but the code block shows bare name = input() and year = int(input()) with no prompt inside the brackets. The code contradicts the steps and the task; a student copying the code gets no prompt on screen, and a student reading the steps sees calls that are not in the code.
- ch 7 [high] Exam traps, 'Double separators' bullet: The bullet says name + ", you are" 'already ends in a comma'. It does not; it ends in the word 'are', with a comma only inside the string. The stated result (Ravi, you are 24) is also not an error, and 'not Ravi,you are24' is unexplained. The trap teaches a wrong fact about string concatenation.
- ch 7 [low] Section 1, first sentence: It says print() takes 'one or more items'. print() may also be called with no items, and print() alone prints just a newline.
- ch 8 [low] Section 1: The sentence 'Python's built-in error names end in Error' is stated as a rule, but several built-in exceptions do not end in Error (StopIteration, KeyboardInterrupt, SystemExit). A student may conclude those are not exceptions at all.
- ch 8 [low] Quiz Q5: The answer fixes the reported line at 7 with certainty. On several Python 3 versions a missing colon is reported on the line after the faulty one, so the student's screen may say line 8. The teaching point (nothing runs, so only the syntax error is seen) is right, but the line number is stronger than the facts.
- ch 8 [low] Quiz Q7: The answer tells the student to read the bottom line and the line above it, and stops there. In the stated situation the bottom frames are inside the library; the student can only edit the line at the top, so the answer is incomplete and may send them to fix code they do not own.
