# e-python-u2: free-model run

- Book: `books/common/e-python/e-python-u2.html`
- Status: ok
- Model calls so far: 24 (82,774 tokens in, 151,522 out), 3.5 minutes

## Checker

```
e-python-u2.html: 8 chapters, 13751 words, 9 figures, 150 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, paragraph on comparison operators: The list of comparison operators is broken: it reads ": , , >, >=, == ..." — the less-than and less-than-or-equal operators have been lost, so students get an incomplete operator list and a sentence that does not parse.
- ch 1 [high] Section 1, last paragraph: The example condition is cut: "marks >= 60 and marks  is true for 70" has no upper bound, so the sentence states nothing checkable and a student cannot see the intended range test.
- ch 1 [high] Section 3, trap list, last bullet: The bullet on testing a range wrongly is incomplete: "marks >= 60 and  is invalid; write marks >= 60 and marks ." Both the wrong version and the corrected version have lost their comparison, so the trap teaches nothing.
- ch 1 [high] Section 2, nesting paragraph: "One level of nesting is allowed inside a block" states a Python restriction that does not exist. Python allows an if inside an if as deep as you like; the real advice is to keep nesting shallow for readability.
- ch 1 [low] Section 2, first paragraph of if-elif-else: "elif means else if. Some syllabi call elif 'else if'." says the same thing twice in two sentences.
- ch 2 [high] Worked example 2: The line labelled 'output: 6' is not the program's output. The program prints six lines of two numbers each (1 1, 2 1, 2 2, 3 1, 3 2, 3 3). '6' is the count of lines found in step 4, so a student reading the label will believe print(i, j) prints a single number.
- ch 2 [low] Section 1, paragraph after the shown output: The sentence 'Here i = i + 1 moves i towards 6, so the test i  finally fails and the loop stops' has a missing condition after 'i'. As printed it reads as broken text and the student cannot see which test fails.
- ch 2 [low] Section 2, range formula: N = ceiling((b − a) / s) only holds when b > a. For range(5, 1, 1) the formula gives ceiling(−4) = −4, but Python produces no values at all.
- ch 2 [low] Quiz Q4 and Q5: Both questions write the loop body after a colon and a semicolon on one line (for x in range(1, 10): total = total + x / while i > 0: print(i); i = i - 3). A student may read the second statement as being outside the loop, especially in Q5, where that reading gives an endless run of 10s instead of the stated answer.
- ch 3 [high] Quiz Q4: The code in the question is cut off: 'i=0; while i' is not a complete program, so a student cannot answer it. The answer describes a loop with a continue before i += 1, which does not match the fragment shown.
- ch 4 [low] Section 3, naming advice: The text says to give functions 'verb-like names' but then lists area, total and is_valid. area is a noun and total is a noun/adjective, so the examples contradict the advice and students may copy the wrong convention.
- ch 4 [low] Quiz Q7: add_gst(p) returning p + 18 suggests GST is a flat 18 rupees. GST is a percentage (18%), so on a price of 10 the tax is 1.80, not 18. The arithmetic of the trace (28, then 84) is correct, but the function name teaches a wrong GST calculation.
- ch 5 [high] Worked example 2, final 'output' field: The question asks students to predict the output of the program with bag=[]. The 'output' field however shows ['milk'] then ['rice'], which is the output of the corrected program, not of the program in the question. It contradicts step 3 and the answer line, which both say the second print shows ['milk', 'rice']. A student reading the field will write down the wrong prediction.
- ch 5 [low] Section 1, position matching paragraph: The claim 'The message names the function and the parameter that is missing' holds only for too few arguments. For too many arguments the TypeError message names the function and the counts, e.g. 'bill() takes 3 positional arguments but 4 were given'; no missing parameter is named.
- ch 5 [low] Section 3, defaults-must-follow paragraph, and Quiz Q3 answer: The stated reason for the rule is not accurate. Positional matching fills parameters from the left, so a call f(5) to a hypothetical def f(a=1, b) would bind a = 5 and leave b unsupplied, which is a TypeError, not an ambiguity over whether 5 belongs to a or to b.
- ch 5 [low] Section 1 lead/code versus Section 2 table and the figure: The name bill is defined two different ways: def bill(price, qty, tax) in the Section 1 code, and def bill(price, qty=1, tax=0.05) in the lead, the table and the figure. Under the Section 1 version, bill(100, 2) is a TypeError, yet the table lists it as legal with tax = 0.05.
- ch 6 [low] Lead: The lead says confusing scope with lifetime causes UnboundLocalError. UnboundLocalError actually comes from the compile-time rule that any name assigned anywhere in a function is local for the whole function, not from mixing up scope and lifetime.
- ch 6 [low] Section 1: "unless you use a mutable object, a module name, or a parameter" — a plain parameter does not carry a value from one call to the next. Only a default argument value, which is created once and reused, does that.
- ch 6 [low] Section 3: "A local name lives from the moment the function call starts until the call returns" clashes with the bullet list below, which says print(x) finds x marked local but with no value yet. The name slot exists from the start; the binding happens only at the assignment.
- ch 7 [low] Exam traps, third bullet: The wording 'forgetting return before the recursive call' is misleading. It suggests the position of return matters, when the real mistake is writing n × factorial(n−1) as a bare statement with no return at all in the recursive case. A student may place return only in front of the call and still be confused about where it belongs.
- ch 7 [low] Beyond: Tail recursion is listed as a topic to search for, but Python does not optimise tail calls. A reader may assume a tail-recursive version of a deep function will avoid the recursion limit, which is false in Python.
- ch 7 [low] Figure (fib(4) tree) aria text and caption: The aria text says the repeated calls give '3', which can be read as three repeated calls rather than the value fib(4) = 3. The caption also only says the calls appear 'in more than one branch' without giving the counts already stated in section 2.
- ch 7 [low] Section 2, first paragraph: The sentence 'A call to fib(n) makes two recursive calls' is stated without the exception for the base cases n = 0 and n = 1, where no recursive call is made. Read literally it contradicts the base cases given in the same paragraph.
- ch 8 [low] Section 3, reduce step list: The four-step procedure assumes there are always two items to start with. On a one-item iterable such as [5], reduce never calls the function and simply returns 5, which the steps do not cover and a student tracing the steps would find confusing.
- ch 8 [low] Section 3, initializer sentence: "If an initializer is given, it is used as the starting a" is correct but does not say what the first b is, and does not say what reduce returns when the iterable is empty but an initializer exists.
