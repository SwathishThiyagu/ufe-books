# e-python-u5: free-model run

- Book: `books/common/e-python/e-python-u5.html`
- Status: ok
- Model calls so far: 26 (89,530 tokens in, 187,718 out), 5.6 minutes

## Checker

```
e-python-u5.html: 7 chapters, 11968 words, 8 figures, 138 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: tree is too wide (5 leaves); use fewer leaves or shorter labels
- chapter 2: the reviewer found 1 serious problem(s) and the revision did not pass the checks; read the review in the state folder
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Lead: The claim 'Every program that reads input, opens a file or calls a server uses this shape, and so does every library you import' is false as stated. Many programs read input with plain input() or validate with if checks, and many libraries handle failure without a try statement. A student may take it literally and think a try block is mandatory around any I/O.
- ch 1 [low] Section 1, bullet list: 'If no clause matches, the exception leaves the try statement, as if no try existed' contradicts the next bullet: the finally block still runs before the exception leaves. Read alone, the sentence tells a student that finally is skipped on an unhandled error, which is the opposite of the rule in Section 3.
- ch 1 [low] Section 1, bullet list: 'If the try block finished with no exception, the else block runs' misses an important case: else also does not run when the try block leaves through return, break or continue. A student tracing a function with a return inside try can get this wrong in an exam.
- ch 1 [low] Section 1, first paragraph: '(see Unit 1)' is a vague cross-reference; the reader on a phone cannot jump to it, and the book style is to link other chapters inline.
- ch 1 [low] Section 3, 'One rule surprises everyone': The rule is stated only for a return in try or except. It also applies to a pending exception: returning from finally discards the exception that was travelling up, so the caller never sees it. Q7 tests exactly this, but the body text does not state it.
- ch 2 [high] Section 1, built-in exception tree: The text says "Two classes sit directly under BaseException: SystemExit and KeyboardInterrupt." That is factually wrong: GeneratorExit is also a direct subclass of BaseException. The claim is wrong as a count and as a complete list.
- ch 2 [low] Section 1, Arithmetic bullet: "OverflowError for a float too large to represent" is loose. Plain float arithmetic does not raise OverflowError in Python; 1e308 * 10 quietly gives inf. OverflowError comes from operations that cannot produce a float at all, such as float(10**400) or math.exp(1000).
- ch 2 [low] Section 2, set_percent example: The block is tagged [pseudo code] but it is ordinary, valid Python. The [shown output] placeholder is empty, and no call such as set_percent(150) is shown, so the claim that the traceback ends with ValueError: percent must be 0 to 100 is never connected to a line the student can run.
- ch 2 [low] Section 3 last paragraph and Exam traps, first bullet: "A class that does not inherit from Exception is not an exception" is imprecise. A class inheriting directly from BaseException (for example a custom class modelled on KeyboardInterrupt) is still raisable; only classes outside the BaseException family are rejected.
- ch 2 [low] Exam traps, last bullet: "A bare raise works only inside an except block" is too narrow. A bare raise also works in a finally block that is running because an exception is propagating, since an exception is still active there.
- ch 2 [low] Worked example 1, dry run table: The 'short' column already shows 1000 in the 'start' row, before the subtraction withdraw - balance has been performed. A student reading the table sees a value that does not yet exist.
- ch 3 [high] Section 1 (tell/seek definitions), reused in Section 3, worked example step 6 and Quiz Q4: tell() is defined as returning the pointer position 'in characters' and seek(n) as moving to character position n. For text files Python returns an opaque position that is a byte offset in the underlying buffer, not a character count. For ASCII text the two happen to match, but the chapter itself recommends encoding='utf-8' for non-ASCII characters, and there the number from tell() is larger than the character count. Also, in text mode seek() accepts only 0 or a value that a previous tell() returned; arbitrary n is not valid.
- ch 3 [low] Figure 'File object and pointer', first node and caption: The caption and aria text say open() creates a file object 'at position 0', but the first node's note allows mode 'r, w or a'. With mode 'a' the pointer starts at the end of the existing text, not at 0.
- ch 3 [low] Figure 'File object and pointer', nodes 'pointer at 8' and 'tell() gives 8': The number 8 is correct only if the first line has 8 characters, but the figure never says what marks.txt contains, so the reader cannot see where 8 comes from.
- ch 4 [low] Worked example 1, steps 2–3: The steps name the loop variable r[1], but the code loops with 'for row in csv.reader(f)' and uses row[1]. A student copying the step names into code gets a NameError.
- ch 4 [low] Quiz Q7: The mechanism is described loosely as 'rows can be split twice'. What actually happens is that the writer writes \r\n, and text mode then turns the \n part into \r\n, so the file holds \r\r\n, which a reader sees as an extra empty row. A student can repeat the answer without understanding it.
- ch 4 [low] Section 2, quoting paragraph: 'the first field is Anil, Jr..' ends with a doubled full stop, which reads like a typo or like part of the value.
- ch 5 [high] Section 1, paragraph 2: The text says a forward-slash path 'project/data' breaks on Windows. That is not true: Windows and Python's file APIs generally accept '/' as a separator, so open('project/data') works there. A student learns a wrong rule and may waste time converting working paths.
- ch 5 [low] Figure caption: The caption reads 'after os.makedirs('data/2024') and a file report.txt', which can be read as if makedirs created report.txt. makedirs creates folders only.
- ch 5 [low] Section 3, sys.path sentence: 'see 5.6' is a bare chapter number, not a clickable cross-reference, so a phone reader cannot jump to it.
- ch 5 [low] Section 2, os.rename: 'os.rename(old, new) renames or moves a file or folder' hides a common failure: on Linux a move to a different filesystem (say /tmp to /home) raises OSError, so a student may trust os.rename to move files between disks.
- ch 5 [low] Worked example 1 vs figure: The worked example uses the script add.py, but the figure tree shows os_demo.py in the same folder, so a student may wonder whether the figure belongs to the example.
- ch 6 [low] Section 1, first paragraph: The text says 'Python has four common import forms' and then lists five: import mymath, from mymath import PI, import shop.billing, import mymath as m, and from mymath import *. A student counting on the phone will stop and wonder which one is not a 'form'.
- ch 6 [low] Worked example 1, code block: The question asks for mymath.square(7), PI after from mymath import PI, and shop.billing.gst(1000), but the code block just prints 7 * 7, 3.14159 and 1000 * 0.18. A student sees raw arithmetic instead of the import statements being tested, and the step-by-step substitution then looks disconnected from the code.
- ch 6 [low] Figure spec, node 's': The note on the 'search sys.path' node reads 'built-ins, stdlib, script folder'. Built-in modules such as sys are found before and outside the sys.path search, as the text itself says, so the figure contradicts the prose.
- ch 6 [low] Beyond: Phrasing namespace packages as a folder that 'can be a package without __init__.py in some versions' is vague and suggests an optional quirk. It is a defined feature with a known starting point.
- ch 7 [high] Section 2, advanced forms: The named-group syntax is shown as (?P\d{4}), which is not valid Python syntax. A named group needs a name inside angle brackets: (?P<name>...). As written, a student who copies this gets an error from re.
- ch 7 [high] Quiz Q4: The question and answer are garbled: both patterns appear as the empty pattern r'' on an empty string s = '', so the two calls are identical and the stated answers [''] and ['', ''] cannot both be produced. The angle-bracket characters in the string and patterns have been dropped, so the question cannot be answered as printed.
- ch 7 [low] Section 2, advanced forms: The sentence says the named group, the backreference and the lookahead 'change what is captured'. A lookahead (?=...) captures nothing; it is a zero-width check on what follows and does not consume text.
