# e-python-u4: free-model run

- Book: `books/common/e-python/e-python-u4.html`
- Status: ok
- Model calls so far: 20 (66,438 tokens in, 138,341 out), 3.7 minutes

## Checker

```
e-python-u4.html: 8 chapters, 13621 words, 9 figures, 156 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, first bullet on the missing self: The sentence 'Python may raise TypeError or treat amount as a local name' is muddled. With def deposit(amount) inside a class, the call a1.deposit(1500) passes a1 as amount and 1500 as an extra argument, so Python always raises TypeError ('takes 1 positional argument but 2 were given'); nothing is 'treated as a local name' in that call.
- ch 1 [low] Exam traps, second trap: It says calling BankAccount.deposit(1500) means 'self is missing'. That is not what happens: 1500 is bound to self and the error is a missing argument for amount ('missing 1 required positional argument: amount'). A student repeating 'self is missing' in an exam answer is technically wrong.
- ch 1 [low] Beyond section: It says the dataclasses module writes '__init__, __str__ and comparison methods'. dataclass generates __init__, __repr__ and __eq__ (ordering only with order=True); it does not generate __str__. Printing works only because object.__str__ falls back to __repr__.
- ch 2 [high] worked example 1, step 7: Step 7 says 'If c2 is still named, its __del__ runs during interpreter shutdown', but the code given ends with del c2, so c2 is not still named. Step 7 describes a program that is not the one shown and contradicts what the student will actually see.
- ch 2 [low] worked example 1, step 8: 'Output in order: 2, bye 5, 1 (and bye 7 when the second object is finally released)' is vague: the code releases the second object explicitly with del c2, so bye 7 is guaranteed and its place in the output is fixed.
- ch 3 [low] Lead: The lead says 'a caller cannot push an impossible value into an object'. In Python this is too strong: the chapter's own exam trap 2 shows that t.__celsius = -300 from module level creates a new attribute and breaks the object. A student may read the lead as a guarantee that Python enforces.
- ch 3 [low] Lead: The examples 'a datetime, a pandas DataFrame' are loose. datetime is immutable and offers no setters, so it is not an accessor/mutator example; a DataFrame lets callers assign many attributes directly with little validation. Both weaken the point being made.
- ch 3 [low] Section 1: 'The double underscore is called name mangling' confuses the trigger with the process. Name mangling is the renaming that Python performs; the double underscore prefix is what triggers it.
- ch 3 [low] Worked example 1, step 8: 'Inside the class the source says __celsius; outside, name mangling makes it _Temperature__celsius' suggests the rename happens when code outside runs. The rename happens at compile time, in the class body, before anything runs.
- ch 3 [low] Section 3: Missing point: __init__ writes self.__celsius = 0 directly. This attribute is the mangled _Temperature__celsius, not the property celsius, so the validation check does not run at construction. A student may assume the setter runs when the object is created.
- ch 3 [low] Section 2 (figure reference): Section 2 says 'The figure follows two calls on one object', but the figure is printed after Section 4, several screens later, so the pointer is misleading on a phone.
- ch 4 [low] Worked example 1, steps 1–4: The steps describe the parent constructor before the child constructor that triggers it. Step 1 says Person.__init__ receives 'Ravi' for s, but execution actually starts at Student.__init__, which then calls super().__init__ inside step 2. A student tracing the program line by line will get a different order from the steps.
- ch 4 [low] Section 3, last paragraph: The point that super() calls only the next class in the MRO, not every parent, is already made in the bullets of the same section. Saying it twice in one short section reads as repetition and weakens the emphasis.
- ch 4 [low] Section 2, isinstance/issubclass paragraph: Saying isinstance(obj, C) is True for 'any child of C' is slightly loose; it is True for any subclass at any depth, not only direct children.
- ch 5 [low] Worked example 1 (question statement vs code): The prompt says each class appends its name 'and then call super().__init__()', but class A's __init__ does not call super().__init__(). The printed output is still correct because the next class after A is object, but the code contradicts the stated setup and the chapter's own rule that every class in the chain must call super().
- ch 5 [low] Section 2, Reading the MRO: C3 linearization has three conditions, not two. Missing is monotonicity: if a class comes before another in a parent's MRO, it must also come before it in the child's MRO. Without this the stated rules are incomplete, even though the diamond examples in the chapter do not need it.
- ch 5 [low] Quiz Q4 answer: 'bases in listed order, shared ancestor next' is confusing: X is not a shared ancestor of two bases, it is Y's parent and also Z's second listed base.
- ch 6 [low] Quiz Q1: The answer says Python 'may try b.__radd__(a) if that fails'. 'Fails' is vague; a student may read it as 'raises an error'. Python falls back to __radd__ only when a.__add__(b) returns NotImplemented, not when it raises an exception.
- ch 6 [low] Worked example 1, dry-run table: The third row is labelled 'm1 + m2', but that is an expression, not an object; the row actually describes the new Money object returned by __add__.
- ch 7 [low] Quiz Q7 answer: The conclusion (Bike() raises TypeError) is right, but the explanation contains a wrong mechanism: it says 'self.wheels = 4 creates an instance attribute only'. A property is a data descriptor, so assigning self.wheels would not create an instance attribute in place of it; it would raise AttributeError because the abstract property has no setter. In this question the assignment never runs at all, since the TypeError from ABCMeta fires before __init__ is called.
- ch 7 [low] Section 3, interface paragraph: The sentence repeats itself: 'Python has no interface keyword; Java and C# have one, Python does not.' The same fact is stated twice in one line and reads as a slip.
- ch 8 [low] Figure (the sequence diagram after Section 3): The diagram calls the object 'Generator g' and shows next() giving 1, then 4, then list(g) giving [9, 16]. The only generator named g that the reader has seen so far is the Section 2 generator expression g = (i * i for i in range(1, 4)), which would give 1, 4, then [9] — not [9, 16]. A student can easily attach the figure to the wrong g and conclude the chapter contradicts itself.
- ch 8 [low] Section 3, first sentence: The definition says a decorator 'takes a function and returns a new function', but four sentences later the chapter says a class decorator takes a class and returns a class. The opening definition is narrower than the term it defines.
