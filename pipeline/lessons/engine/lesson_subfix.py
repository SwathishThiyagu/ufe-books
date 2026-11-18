#!/usr/bin/env python3
"""lesson_subfix.py <lesson.js>: turn on-screen underscore subscripts (A_TM, D_pre, x_{i+1}) into sub tspans, in place.

Only quoted JS strings change. Left alone: narration (say:); tokens also in the lesson's code text; code identifiers
(ALL_CAPS like NO_MATCH, snake_case like mm_struct or st_mtime, member access like p.st_mtime, names the JS itself uses
like ICON.q_graph); and tokens that appear on screen only in lines the checker's CODE_LINE treats as code
(such as "p.stat().st_mtime > 7 * 86400"). The checker (lesson_build.py) uses the same identifier rules, so what this
leaves alone passes --check.
Rerunning it repairs a lesson an earlier version damaged: it first turns its own sub tspans back into X_sub, then applies
the rules again, so wrongly subscripted identifiers come back as plain text.
The tspan uses tab-separated attributes so wrapT keeps it whole, and its quotes match the string's quotes.
Run lesson_build.py --check after it and look at the sheet: a string used outside an SVG <text> would show the markup.
"""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lesson_build import CODE_LINE
TOK = re.compile(r'(?<![\w.$])(?<!->)(?![A-Z]{2}_[A-Z]{2})(?![a-z]{2}_[a-z]{3})([A-Za-zα-ωΑ-Ω]{1,2})_(\{[^}]*\}|[A-Za-z0-9]{1,6})(?![\w(])')
def main(p):
    src = open(p, encoding='utf-8').read()
    # undo this tool's own sub tspans in quoted strings first, so a rerun repairs what an earlier version got wrong
    r = subprocess.run(['node', os.path.join(HERE, 'lesson_subfix_tok.js'), p, '--undo'], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr)
    und = json.loads(r.stdout)
    tmp = p[:-3] + '.subfix_tmp.js'; open(tmp, 'w', encoding='utf-8').write(und['src'])
    try:
        ev = json.loads(subprocess.run(['node', os.path.join(HERE, 'lesson_eval.js'), tmp, os.path.join(HERE, 'lesson_template.html')],
                                       capture_output=True, text=True).stdout)
    except Exception:
        os.remove(tmp); raise
    txt = lambda k: ' '.join(' '.join(sc.get(k)) if isinstance(sc.get(k), list) else str(sc.get(k) or '') for sc in ev['scenes'])
    # a token only in code text (p_id) is code; one that is also on screen as prose (q_acc) gets the subscript everywhere
    # likewise a token seen on screen only in lines the checker treats as code (CODE_LINE: "p.stat().st_mtime > 7")
    lines = [l for sc in ev['scenes'] for l in (sc.get('screen') or [])]
    codey = {m.group(0) for l in lines if CODE_LINE.search(l) for m in TOK.finditer(l)}
    prose = {m.group(0) for l in lines if not CODE_LINE.search(l) for m in TOK.finditer(l)}
    skip = ({m.group(0) for m in TOK.finditer(txt('code'))} | codey) - prose
    sk = os.path.join(os.path.dirname(os.path.abspath(p)), '.subfix_skip.json'); json.dump(sorted(skip), open(sk, 'w'))
    r = subprocess.run(['node', os.path.join(HERE, 'lesson_subfix_tok.js'), tmp, sk], capture_output=True, text=True); os.remove(sk); os.remove(tmp)
    if r.returncode: sys.exit(r.stderr)
    res = json.loads(r.stdout); new, n = res['src'], res['n']
    if new != src: open(p, 'w', encoding='utf-8').write(new)
    print(f'{n} subscripts set' + (f' ({und["n"]} earlier ones undone and redone by the current rules)' if und['n'] else ''), ('(skipped, also in code: ' + ', '.join(sorted(skip)) + ')') if skip else '', p)
if __name__ == '__main__':
    main(sys.argv[1])
