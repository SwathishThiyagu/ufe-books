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
 (r"\b[Yy]our book['’]s (\w+)", lambda m: ('The ' if m.group(0)[0] == 'Y' else 'the ') + m.group(1) + ' from your free notes'),
 (r"\b[Tt]he book['’]s (\w+)", lambda m: ('The ' if m.group(0)[0] == 'T' else 'the ') + m.group(1) + ' from your free notes'),
 (r"\bfrom your book\b", "from your free notes"),
 (r"\bof your notes\b", "of your free notes"),
 (r"All six units", "The whole course"), (r"all six units", "the whole course"),
]
# Bloom-introduced practice questions: "An apply question." -> "Question two." by the scene's own n,
# in the say line and its cue. Also repairs lessons an earlier version turned into "Question one" three times.
W = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
def pq(seg):
    m = re.search(r"\bk\s*:\s*['\"]pq['\"]", seg); n = re.search(r"\bn\s*:\s*(\d+)", seg)
    if not (m and n) or int(n.group(1)) not in W: return seg
    q = 'Question ' + W[int(n.group(1))]
    seg2 = re.sub(r"(Exam practice! |say\s*:\s*[`'\"])Question one\.", lambda x: x.group(1) + q + '.', seg)
    seg2 = re.sub(r"\bAn? " + B + r" question([.:])", lambda x: q + x.group(1), seg2)
    seg2 = re.sub(r"(\bk\s*:\s*['\"])(?:An? " + B + r" question|An? " + B + r"|Question one)(['\"])", lambda x: x.group(1) + q + x.group(2), seg2)
    if seg2 != seg: print(f'  pq n={n.group(1)}: -> {q!r}')
    return seg2
parts = re.split(r"(?=\{\s*s\s*:)", s)
s = ''.join(pq(x) for x in parts)
for a, b in R:
    for m in re.finditer(a, s): print(f'  {m.group(0)[:70]!r}')
    s = re.sub(a, b, s)
if s != o: open(p, 'w', encoding='utf-8').write(s)
print('changed' if s != o else 'no change', p)
