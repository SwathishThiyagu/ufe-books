"""lesson_rules_fix.py <lesson.js> <sid>: the mechanical part of the approved SLOP rules on an already-written lesson (in place).
Prints every change; the rest is fixed by hand after lesson_build.py --check."""
import sys, re
p, sid = sys.argv[1], sys.argv[2]
s = open(p, encoding='utf-8').read(); o = s
B = r'(?:understand|apply|analy[sz]e|remember|evaluate|create)'
R = [
 (r"Sources the book draws on:", "Sources your free notes draw on:"),
 (r"of your book(['\"])", r"of your free notes\1"),
 (r"subject:'biotech'", f"subject:'{sid}'"), (r'subject:"biotech"', f"subject:'{sid}'"),
 (r'next:\["NEXT UNIT", "Unit \d+", ', 'next:["UP NEXT", "Next topic", '),
 (r'next:\["NEXT TIME", "Lesson \d+", ', 'next:["NEXT TIME", "Next lesson", '),
 (r"Next time, [Uu]nit \w+: ", "Next time: "),
 (r"(Question (?:one|two|three)), (?:an? " + B + r" question|at the " + B + r" level|" + B + r"(?: level)?)\.", r"\1."),
 (r"(Exam practice! )An? " + B + r" question\.", r"\1Question one."),
 (r"\bAn? " + B + r" question\. ", "Question one. "),
 (r"\b[Yy]our book['’]s (\w+)", lambda m: ('The ' if m.group(0)[0] == 'Y' else 'the ') + m.group(1) + ' from your free notes'),
 (r"\b[Tt]he book['’]s (\w+)", lambda m: ('The ' if m.group(0)[0] == 'T' else 'the ') + m.group(1) + ' from your free notes'),
 (r"\bfrom your book\b", "from your free notes"),
 (r"\bof your notes\b", "of your free notes"),
 (r"(k\s*:\s*['\"])An? (?:understand|apply|analy[sz]e|remember|evaluate|create)(['\"])", r"\1Question one\2"),
 (r"All six units", "The whole course"), (r"all six units", "the whole course"),
]
for a, b in R:
    for m in re.finditer(a, s): print(f'  {m.group(0)[:70]!r}')
    s = re.sub(a, b, s)
if s != o: open(p, 'w', encoding='utf-8').write(s)
print('changed' if s != o else 'no change', p)
