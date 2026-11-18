#!/usr/bin/env python3
"""lesson_subfix.py <lesson.js>: turn on-screen underscore subscripts (A_TM, D_pre, x_{i+1}) into sub tspans, in place.

Only quoted JS strings change; narration (say:) and any token that also appears in the lesson's code text are left alone.
The tspan uses tab-separated attributes so wrapT keeps it whole, and its quotes match the string's quotes.
Run lesson_build.py --check after it and look at the sheet: a string used outside an SVG <text> would show the markup.
"""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TOK = re.compile(r'(?<![\w_])([A-Za-zα-ωΑ-Ω]{1,2})_(\{[^}]*\}|[A-Za-z0-9]{1,6})(?![\w(])')
def main(p):
    src = open(p, encoding='utf-8').read()
    ev = json.loads(subprocess.run(['node', os.path.join(HERE, 'lesson_eval.js'), p, os.path.join(HERE, 'lesson_template.html')],
                                   capture_output=True, text=True).stdout)
    txt = lambda k: ' '.join(' '.join(sc.get(k)) if isinstance(sc.get(k), list) else str(sc.get(k) or '') for sc in ev['scenes'])
    # a token only in code text (p_id) is code; one that is also on screen as prose (q_acc) gets the subscript everywhere
    skip = {m.group(0) for m in TOK.finditer(txt('code'))} - {m.group(0) for m in TOK.finditer(txt('screen'))}
    sk = os.path.join(os.path.dirname(os.path.abspath(p)), '.subfix_skip.json'); json.dump(sorted(skip), open(sk, 'w'))
    r = subprocess.run(['node', os.path.join(HERE, 'lesson_subfix_tok.js'), p, sk], capture_output=True, text=True); os.remove(sk)
    if r.returncode: sys.exit(r.stderr)
    res = json.loads(r.stdout); new, n = res['src'], res['n']
    if new != src: open(p, 'w', encoding='utf-8').write(new)
    print(f'{n} subscripts set', ('(skipped, also in code: ' + ', '.join(sorted(skip)) + ')') if skip else '', p)
if __name__ == '__main__':
    main(sys.argv[1])
