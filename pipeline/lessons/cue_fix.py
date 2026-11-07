#!/usr/bin/env python3
"""Move each card's cue to the start of the sentence that introduces it, so text appears as the narrator starts the idea.

Models tend to cue the last words of an idea ("stuck in a local minimum") instead of its first ("Students write"),
so cards land seconds late. For the kinds where a card or line should appear as its sentence begins (trap2, traps,
notebook, recap, pa), each cue phrase is replaced by the first three words of its sentence, when those are unique.
usage: cue_fix.py lesson.js   (edits in place, prints what moved)"""
import re, sys

KINDS = ('trap2', 'traps', 'notebook', 'recap', 'pa')

def words(s): return re.findall(r"[A-Za-z0-9'’-]+", s)

def fix(src):
    out, moved, pos = [], [], 0
    for m in re.finditer(r"\{s:\d+,k:'(\w+)'", src):
        pass
    starts = [m.start() for m in re.finditer(r"\{s:\d+,k:'", src)] + [len(src)]
    res = src[:starts[0]]
    for a, b in zip(starts, starts[1:]):
        blk = src[a:b]
        k = re.match(r"\{s:\d+,k:'(\w+)'", blk).group(1)
        sm = re.search(r"say:(['`])(.*?)(?<!\\)\1", blk, re.S)
        cm = re.search(r"cues:\{([^}]*)\}", blk)
        if k in KINDS and sm and cm and '${' not in sm.group(2)[:0]:
            say = sm.group(2)
            plain = re.sub(r"\$\{P\('([^']+)'\)\}", r'\1', say)
            plain = re.sub(r'\[([^\]]+)\]\(/[^)]*/\)', r'\1', plain)
            sents = [x for x in re.split(r'(?<=[.!?:;])\s+', plain) if x.strip()]
            low = plain.lower()
            def sent_of(phrase):
                i = low.find(phrase.lower()); acc = 0
                for si, snt in enumerate(sents):
                    j = plain.find(snt, acc)
                    if j <= i < j + len(snt) + 1: return si
                    acc = j + len(snt)
                return None
            idx = [sent_of(p) for _, _, p in re.findall(r"(\w+):(['\"])([^'\"]*)\2", cm.group(1))]
            shared = {x for x in idx if x is not None and idx.count(x) > 1}
            def repl(mm):
                if sent_of(mm.group(3)) in shared: return mm.group(0)
                key, q, phrase = mm.group(1), mm.group(2), mm.group(3)
                i = low.find(phrase.lower())
                if i < 0: return mm.group(0)
                acc = 0
                for snt in sents:
                    j = plain.find(snt, acc)
                    if j <= i < j + len(snt) + 1:
                        head = ' '.join(words(snt)[:3])
                        if head and low.count(head.lower()) == 1 and not phrase.lower().startswith(head.lower()):
                            moved.append(f'{k} {key}: "{phrase}" -> "{head}"')
                            return f"{key}:{q}{head}{q}"
                        return mm.group(0)
                    acc = j + len(snt)
                return mm.group(0)
            new_c = re.sub(r"(\w+):(['\"])([^'\"]*)\2", repl, cm.group(1))
            blk = blk[:cm.start(1)] + new_c + blk[cm.end(1):]
        res += blk
    return res, moved

if __name__ == '__main__':
    p = sys.argv[1]; s = open(p, encoding='utf-8').read()
    n, moved = fix(s)
    open(p, 'w', encoding='utf-8').write(n)
    print('\n'.join(moved) or 'nothing moved')
