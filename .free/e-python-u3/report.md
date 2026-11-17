# e-python-u3: free-model run

- Book: `books/common/e-python/e-python-u3.html`
- Status: ok
- Model calls so far: 26 (94,393 tokens in, 210,867 out), 5.5 minutes

## Checker

```
e-python-u3.html: 9 chapters, 15580 words, 10 figures, 166 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, case methods: The chapter says s.capitalize() 'capitalises only the first character'. In Python, capitalize() also lowercases every other character, so 'hELLO'.capitalize() is 'Hello', not 'HELLO'. The same gap exists for s.title(): it uppercases the first letter of each word and lowercases the rest, so "it's a TEST".title() is "It'S A Test". A student following the chapter will predict wrong outputs.
- ch 1 [low] Section 2, slicing: The chapter states the defaults as start=0, stop=len(s), step=1 without saying these hold only for a positive step. A student who applies start=0 with step=-1 would expect s[::-1] to be empty, which contradicts the next sentence.
- ch 1 [low] Section 2, slicing: 'Every slice makes a new string, even s[:]' is not true in CPython: a full slice of a str can return the same object, so s[:] is s evaluates to True. The value is unchanged either way, but the absolute claim is false.
- ch 2 [low] Section 2, last line: The phrase "3.9 covers sorted lists" is ambiguous: a student can read 3.9 as the Python version (Python 3.9) rather than a chapter number, and the chapter reference is plain text with no link.
- ch 2 [low] Section 1, example f'₹{1234.5:,.2f}': The comma format inserts Western thousands groups (1,234, 12,345,678). Indian readers writing rupee amounts of a lakh or more need 1,23,456.78 style grouping, which this format does not give. The chapter never says so, so a student may think ',' produces Indian grouping.
- ch 2 [low] Figure description line: "the inner comma-space is replaced by a dash" is loose: splitting removes the commas and stripping removes the spaces around pieces; join then inserts the separator ' - '. Nothing is literally replaced.
- ch 2 [low] Beyond section: "f-strings appear in logging" is misleading advice. In logging calls the usual style is lazy %-formatting (logger.info('x=%s', x)); an f-string is formatted immediately, even if the message is never emitted, so it is discouraged inside logging calls.
- ch 3 [high] Section 1, operators paragraph: The comparison operators are missing from the text. It reads "ordering (, >) compares item by item" — only the > survives and the < has vanished. The example sentence is broken the same way: "For example, [1, 2]  is True and [1, 2]  is True" states nothing at all, and a student cannot tell which comparison is being asserted.
- ch 3 [high] Section 2, opening sentence: The sentence "The changing methods below edit the same list object and usually return None" is contradicted by the bullets that follow it, because those bullets also list index(x), count(x) and copy(). None of these three changes the list: index and count return an integer and copy returns a new list. A student will conclude that count() or copy() can be used as a mutating method and returns None.
- ch 3 [low] Section 2, insert/remove/index bullets: The chapter says remove(x) raises ValueError if x is absent but does not say what index(x) does when x is absent. Under try/except questions this is exactly the gap students fall into, since both raise ValueError and neither returns -1 (unlike str.find).
- ch 3 [low] Section 3, aliasing paragraph: "Some syllabi call this a reference copy" suggests a copy is made, but in b = a no copy of any kind exists — there is one object and two names. The phrase invites the very mistake the section is warning against.
- ch 4 [low] Section 2, after the table: The sentence 'Swapping the two for clauses changes the order of the results' is not true for the example just given. With [i + j for i in range(1, 3) for j in range(1, 3)] both clauses walk 1, 2 and addition is commutative, so the swapped line [i + j for j in range(1, 3) for i in range(1, 3)] also prints [2, 3, 3, 4]. A student who tries it will think the book is wrong.
- ch 4 [low] Section 3, last paragraph before the figure: 'Set and dictionary comprehensions reuse the same pattern with braces and a key-value pair' is wrong for set comprehensions. A set comprehension is {expr for item in iterable} with no key-value pair; only a dictionary comprehension has the key: value form.
- ch 4 [low] Section 3, last paragraph before the figure: The cross-references are given out of chapter order (3.7 Sets before 3.6 Dictionaries), which reads like a typing slip.
- ch 5 [high] Section 3 (Immutability, unpacking and comparison): Two comparison sentences have their expressions missing, so the sentences read '(1, 2)  is True' and '(1, 2)  is True'. Nothing is being compared, and a student cannot tell what is True.
- ch 5 [low] Worked example 1 (code block): The code block prints only t[1] and len(t), but the question and the answer also cover t[1:3], t + (40,) and t * 2. A reader may think these three were never actually run.
- ch 6 [low] Worked example 1, step 6 and answer: The line in the program is print(d.get('z')), so the program prints None. Step 6 and the answer only say get('z') 'returns None', and the answer lists the prints as '10, 99, 20 and 2' without saying that None is also printed. A student copying the output line by line will miss one line.
- ch 7 [low] Section 1, second paragraph: The parameter is named iterable, but the sentence then says set(iterable) builds a set from 'any sequence'. A sequence is narrower than an iterable; a range, a generator, a dict or a file can all be passed to set(). The mismatch can confuse students about what is allowed.
- ch 7 [low] Section 3, paragraph 2, and Exam traps bullet 4: The chapter says the four arithmetic operators need a set on both sides and illustrates only A | [7, 8]. The comparison operators behave the same way; A <= [1, 2] also raises TypeError. A student may believe list arguments are fine on the right of <=.
- ch 7 [low] Section 2, paragraph 2: 'x in A costs about the same for ten items and for ten lakh items' is true only on average. If many keys collide, for example objects with equal hashes, the lookup degrades towards comparing items one by one. Calling the cost constant without the average-case qualifier overstates the guarantee.
- ch 8 [low] Lead: The sentence 'A list can grow at its right end and shrink from either end' reads as if a list can only grow at the right end. That contradicts the later trap about insert(0, x), which grows the list at the left end (at O(n) cost). A student may take away the wrong rule.
- ch 8 [low] Section 3 and the table, peek row: Section 3 warns only that pop() and pop(0) raise IndexError on an empty list. The peek operations shown (s[-1] and q[0]) raise IndexError on an empty container too, and nothing says so.
- ch 9 [high] Section 1, cost paragraph and algorithm description: It says the search returns -1, "which is never a valid index". In Python this is false: negative indices are legal, so a[-1] is the last item of the list. A student who forgets to test for -1 and writes a[result] silently gets the last element instead of an error, which is exactly the bug the sentence claims cannot happen.
- ch 9 [high] Quiz Q7 answer: The answer says "-1 can never be a valid index, so it is unambiguous." As written it is wrong for Python, where -1 is a valid index (the last item). Only the point that 0 is a real position is correct.
- ch 9 [low] Section 1 and Section 2 code vs. text: The text says the functions return the index or -1, but the code returns a pair (index, comparisons), and the shown output is a tuple such as (999, 1000). A student matching the prose to the run may be confused about what the function actually returns.
- ch 9 [low] Section 3 heading: The heading promises an "exchange sort", but the section teaches bubble sort and selection sort. Bubble sort is the exchange sort; selection sort is not one, so the label is loose.
