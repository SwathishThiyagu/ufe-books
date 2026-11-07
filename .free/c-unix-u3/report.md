# c-unix-u3: free-model run

- Book: `books/cse/c-unix/c-unix-u3.html`
- Status: ok
- Model calls so far: 35 (130,769 tokens in, 229,075 out), 6.6 minutes

## Checker

```
c-unix-u3.html: 8 chapters, 13549 words, 9 figures, 159 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1: The text says the file 'contains two lines' with line 2 being the echo, but the code block shows three lines: the shebang, a comment line, and then the echo on line 3. A student counting lines will be confused.
- ch 1 [low] Worked example 1, dry run table: The step numbers in the dry run table do not match the step numbers in the text: the table has four rows, and its rows 2–4 correspond to text steps 3–5 because the chmod step is missing from the table.
- ch 2 [high] Worked example 1, step 1: Step 1 says NAME=Asha stores the five-character string Asha, but Asha is four characters. Step 6 of the same example and the final answer both say the length is 4, so the example contradicts itself.
- ch 2 [low] Figure 'Quoting decides expansion', unquoted branch: The note on the unquoted output says 'splits on spaces', but the stored value is Asha, which has no spaces, so echo $NAME prints exactly Asha and no splitting happens. A student may think Asha itself was split.
- ch 2 [low] Section 2, quoting paragraph: 'A backslash \ escapes the next character, so \$NAME prints a literal dollar sign' can be read as saying the output is only a dollar sign, when the output is the whole text $NAME.
- ch 3 [high] Section 3, for loop forms: The C-style header is cut off mid-expression: "for ((i=0; i. In the C-style header...". The condition and update parts of the header are missing, so the code is not valid and the sentence cannot be read.
- ch 3 [high] Section 3, reading a file line by line: The input redirection is missing, so the text reads "done . -r stops backslash processing, and  sends the file to standard input." The command has a stray period and the sentence has a blank where the redirection should be. A student cannot see how the file reaches read.
- ch 3 [high] Exam traps, last bullet: The text is truncated: "for ((i=1; i does arithmetic." The comparison and increment are missing, so the trap about the difference between the word-list for and the C-style for is unreadable.
- ch 3 [low] Exam traps, first bullet: "1 is failure" suggests 1 is the only failure value. Failure is any non-zero status, for example 1, 2 or 127 (command not found).
- ch 4 [low] Section 3, shift loop: The while/shift loop is followed by an empty 'shown output' block. A reader cannot tell whether the loop prints nothing or whether the output was left out by mistake, since no sample argument list is given for the script.
- ch 4 [low] Section 1 and Worked example 1 dry run: The chapter never says that a function's positional parameters are temporary: $1, $2 and $# inside the function are restored to the caller's values when it returns. The dry-run table even keeps $1=4 and $2=6 in the rows s=$? and echo $s, which run in the main script, so a student may believe the call overwrites the caller's arguments.
- ch 4 [low] Section 3, unquoted expansion note: 'Unquoted $@ splits on spaces' is incomplete: an unquoted expansion splits on any character of IFS and the resulting words are also subject to filename generation, so an argument like * can expand to file names.
- ch 5 [low] Quiz Q5: The question uses grep root /etc/passwd to produce the message 'Permission denied'. /etc/passwd is readable by every user, so grep on it will not print that error. A student may think grep itself raises the message, or may not see how the example could fail.
- ch 5 [low] Section 3, paragraph on for line in $(cat file): The text says command substitution 'splits on spaces'. It actually splits on every character in IFS, which by default is space, tab and newline, and it also performs pathname expansion, so a name containing * or ? is expanded too. Calling it splitting on spaces only can make a student think tabs are safe.
- ch 6 [low] Worked example 1 and Quiz Q3: The pipeline is written with head -2 (and Q3 with head -1). head -2 is a GNU/BSD convenience form; POSIX head only guarantees -n, and the chapter itself stresses POSIX-portable scripts and teaches the -n form in Section 2. A student copying this onto a strict POSIX system may get an error.
- ch 6 [low] Section 1: The text says the pipe starts two processes but never says they run at the same time, connected by a kernel buffer. A student can easily read it as "left command finishes, then right command starts", which is wrong and makes later points (head exiting early, large streams) hard to understand.
- ch 6 [low] Section 3, PIPESTATUS sentence: PIPESTATUS is described as holding every stage's status, but not that it is overwritten by the very next command run. A student who writes a pipeline and then an echo before reading ${PIPESTATUS[0]} will read the wrong value.
- ch 7 [high] Figure (grep to sed to awk), awk node: The awk node is labelled awk -F, '$2 >= 60' with the note 'sum and count', but that program only prints the matching lines (Asha,78 / Meena,91 / Arjun,60). The figure then shows the output 3 229, which that command never produces. The shown command and the shown output disagree.
- ch 7 [low] Section 2 (sed): 'In-place editing needs write permission on the file' is not accurate for sed -i. sed -i writes a temporary file in the same directory and renames it over the original, so it needs write permission on the directory; a read-only file in a writable directory can still be edited this way.
- ch 8 [high] Section 3, 'Save status before cleanup' snippet: cp "$1" /backup; s=$?; if [ "$s" -ne 0 ]; then log ...; exit "$s"; fi: As written the snippet cannot do what the text promises when set -e is on. Under set -e the shell exits the moment cp fails, so s=$? is never executed and the log line never runs. The chapter recommends set -e elsewhere, so a student who copies this pattern gets silent failure with no log message.
- ch 8 [low] Section 3, trap ERR sentence: 'trap ... ERR runs when a command fails under set -e' suggests the ERR trap needs set -e. It fires on any command returning non-zero, with the same exceptions as set -e, whether or not set -e is set.
- ch 8 [low] Section 3, die() description: 'die writes to stderr and returns a non-zero status' is wrong wording: die calls exit 1, so it terminates the script with status 1 rather than returning to the caller.
- ch 8 [low] Quiz Q6: The question gives a bare command line 'set -e; echo start; false; echo end' without saying it is inside a script. Typed at an interactive prompt, set -e makes the shell itself exit, which is a different (and destructive) outcome from the answer given.
- ch 8 [low] Quiz Q5 answer: 'echo prints that saved value' is misleading: nothing is saved; $? is expanded before echo runs, which is exactly why it must not be preceded by another command.
- ch 8 [low] Worked example 1, dry run table, third row Status cell: '0 or not run' in the Status column mixes a status with a run condition, and does not match the plain single-value style of the other rows, so the table is hard to read.
