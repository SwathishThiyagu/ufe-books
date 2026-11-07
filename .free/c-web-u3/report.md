# c-web-u3: free-model run

- Book: `books/cse/c-web/c-web-u3.html`
- Status: ok
- Model calls so far: 38 (147,800 tokens in, 214,261 out), 5.1 minutes

## Checker

```
c-web-u3.html: 9 chapters, 16133 words, 10 figures, 184 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3, falsy values sentence: The falsy list gives only false, 0, '', null, undefined and NaN, then says everything else is truthy. But -0 and 0n (BigInt zero, and the chapter itself introduced bigint in Section 1) are also falsy, so a student testing 0n or -0 in an if would get a branch different from what this sentence promises.
- ch 1 [low] Section 2, ternary formula: The two branches are called valueIfTrue and valueIfFalse, but the explanation says they 'run'. They are expressions whose value is chosen, not steps that execute; this can confuse a student into thinking statements go there.
- ch 1 [low] Figure caption: '72 fails 90 and fails 75' is awkward phrasing; 'fails 90' reads as if the marks failed something rather than the test failing.
- ch 2 [high] Section 3, paragraph on nested objects: The object literal a few lines earlier is let student = { name: 'Asha', marks: 88 }; so student.marks is the number 88, not an object. The nested-object example then writes student.marks.math, which is undefined for that literal and contradicts the example the student just read.
- ch 2 [low] Section 1, rest parameters: The sketch function sum(...nums); is not valid JavaScript — a function needs a body in braces (or an arrow body). A student copying the line gets a syntax error and cannot see where the array is built.
- ch 2 [low] Section 1, function expression: The line 'const average = function (a) { ... };.' ends with both a semicolon and a full stop, which reads like part of the code and looks like a typo.
- ch 3 [low] Section 1, element property example: The lines b.onclick = pay; and b.removeEventListener('click', pay); use the symbols b and pay without saying what they stand for, so a first-time reader has to guess.
- ch 3 [low] Section 2, three phases: The capture phase is described as running 'from window down to the target's parent', which leaves it unclear what happens to a listener added with {capture:true} on the target itself (it runs in the target phase, in registration order with the ordinary listeners). Readers can be confused when the capture listener sits on the clicked element.
- ch 3 [low] Section 3 table, scroll and resize rows: The chapter teaches that bubbling makes delegation work, but scroll and resize listeners do not bubble from elements; a student may try to delegate them on a parent and see nothing fire.
- ch 3 [low] Section 3 table, change row: 'Value is committed' does not say that change fires only if the value actually changed since the field gained focus; a student may expect a log on every blur.
- ch 4 [high] Section 2 (Selecting and changing nodes) and Exam trap 1 / Quiz Q2 answer: The text says innerHTML 'runs scripts it finds', and the Q2 answer says 'scripts can run'. A script element inserted with innerHTML does not execute — browsers explicitly do not run it. The XSS risk from innerHTML comes from event-handler attributes (such as onerror) and javascript: URLs, not from a script tag inserted through innerHTML. As written, students learn a wrong behaviour.
- ch 4 [high] Section 3, last line: 'Cookies and sessions are server-side' is wrong for cookies. A cookie is stored in the browser (client side) and sent to the server with each request. Only the session data normally lives on the server.
- ch 4 [high] Quiz Q3: The stem reads 'Given AB', so the markup the student must work on is missing. The answer uses document.querySelectorAll('#list li'), which assumes a ul with id 'list' that is never shown. The question cannot be answered from what is printed.
- ch 4 [low] Worked example 1, step 6 and code: Part (d) asks for the count before and after step (b), but the variable after is read only after step (c) (the class change). The output is the same, but a student may think the class change affects the count.
- ch 5 [high] Worked example 1, question line: The code in the question is broken and unreadable: it shows 'for (var i = 0; i  console.log(i), 0); }'. The loop condition and the setTimeout call were lost, so a student cannot trace the loop the steps then discuss.
- ch 5 [high] Section 3, Modules paragraph: The sentence ends as 'In a browser use .' The tag that was meant to appear has been stripped, so the key instruction (how to load a module in a browser) is missing and the sentence has no meaning.
- ch 5 [high] Quiz Q6: The question reads 'What does  change?' The thing being asked about is missing, so the question cannot be answered as printed.
- ch 5 [low] Section 1, const paragraph: Object.freeze is presented as a full stop to changes, but it is shallow: properties of a nested object can still be changed after freezing the outer one.
- ch 5 [low] Quiz Q2, answer: The question is general ('a var loop') but the answer names the value 3, which holds only for the three-iteration loop in the worked example.
- ch 6 [low] Section 1, second paragraph: 'if a function waits 2 seconds, nothing else on the stack runs' can confuse a student: await and setTimeout also 'wait' but do not block the stack. Only a synchronous busy loop blocks it, which is the point being made.
- ch 6 [low] Section 1, timers paragraph: setInterval(fn, delay) is said to 'repeat every delay ms', but delay is a minimum, not exact. Long callbacks, long synchronous code and browser clamping (nested timers are held to about 4 ms) all stretch the gap.
- ch 6 [low] Exam traps, bullet 'Reading an async function's result without await': 'You get a pending promise' is not always true. The promise may already be fulfilled or rejected by the time the student inspects it; the real trap is that you get a promise object, never the value itself.
- ch 6 [low] Section 3, React sentence: 'async state initialization' is not defined and is easy to misread as making the component function async, which React does not allow.
- ch 7 [low] Worked example 1, question line: The target element id is missing: the sentence reads "writes 'Asha: 72' into ." — the div name has been dropped, so the code and question do not match each other.
- ch 7 [low] Worked example 1, step 5 and dry run row for readyState 1: The code assigns onreadystatechange after open() has already run, so no call-back fires for readyState 1; the handler first runs at readyState 2. Step 5 ("does nothing on 1, 2 and 3") and the dry-run row "1 | 0 | call-back fires, guard returns" both say otherwise.
- ch 7 [low] Section 3, JSON building blocks: The schematic "objects {key: value}" shows an unquoted key, which contradicts the very next rule that every key is a double-quoted string. Students copy such patterns straight into code.
- ch 8 [high] Quiz Q3: The DTD declaration the question refers to is missing. The question reads 'Given , how many book elements may a bookstore contain?', so there is nothing to apply the star to and the student cannot answer it. The answer ('Zero or more; the star means zero or more') points to a declaration containing * that never appears.
- ch 8 [high] Quiz Q6: The model answer is empty: it shows only a full stop after 'answer:'. The student is asked to write an ATTLIST declaration and there is no declaration to check against.
- ch 8 [low] Section 3, built-in types: 'xs:decimal for numbers with a decimal point' is misleading. xs:decimal holds decimal numbers that may or may not have a decimal point, so the integer 350 is a valid xs:decimal. A student may believe a whole-number price is rejected by xs:decimal.
- ch 8 [low] Section 1, first paragraph: An element is defined only as 'a pair of tags with content between them'. Empty elements such as <code>&lt;price/&gt;</code> are never introduced, yet the DTD section later uses EMPTY as a content model, so the two parts do not connect.
- ch 9 [high] Section 2, Effects paragraph: The sentence 'Chain after the effect to run when it ends' is wrong. A chained non-effect method (e.g. .fadeIn(400).addClass('done')) runs at once, not after the animation. Only a further queued effect waits on the previous one.
- ch 9 [high] Quiz Q8: The answer says .append('New') 'adds a fresh li inside the still-existing list'. It does not. Appending a plain string inserts a text node directly inside the ul, so the ul holds the text 'New' and no new li; the 'new item' is not a list item and would not match '#items li'.
- ch 9 [low] Section 1, Selectors paragraph (and quiz Q7): :input is listed with 'CSS selectors', but it is a jQuery-only extension. CSS has no :input pseudo-class, and Q7 then offers :input as a filter, which contradicts the chapter's own grouping.
- ch 9 [low] Section 3, AJAX paragraph: 'Chaining returns the same jQuery object' sits inside the AJAX discussion, where the thing being chained is the $.ajax return value (a jqXHR), which is a promise-like object, not a jQuery element set. A student may think jqXHR is a wrapped DOM set.
- ch 9 [low] Worked example 1, opening line: 'A page has PenBookBag' is a missing-separator typo and reads like one word.
