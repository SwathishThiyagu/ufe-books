"""Put Claude's hand-drawn figures into a library book that has no writer branch (no .free/<unit>/ state), straight in the HTML.

    python pipeline/claude_figs/apply_html.py <unit> [--push]      e.g. c-coa-u1

For books written before the free-model pipeline (c-coa, c-data, ...) the library copy on main is the only source. This
replaces the first figure of each chapter k that pipeline/claude_figs/<unit with _>.py defines (spec(k) as in apply.py);
other figures and all text stay as they are. The original <figure> blocks are saved once to
pipeline/claude_figs/old/<unit>.json so the change can be undone. Runs the checker with --render and takes the
screenshots; with --push commits the book (and the saved originals) to main and pushes.
"""
import sys, os, json, re, subprocess, importlib.util, shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'pipeline'))
import render as RD

unit = sys.argv[1]
push = '--push' in sys.argv
q = json.load(open(os.path.join(ROOT, 'queue.json')))
out = next(u['out'] for u in q if u['unit'] == unit)
P = json.load(open(os.path.join(ROOT, 'packets', f'{unit}.json')))
N = P['unit']['n']
run = lambda *a: subprocess.run(a, check=True)
if push:
    run('git', '-C', ROOT, 'pull', '-q', '--rebase', '--autostash', 'origin', 'main')

src = os.path.join(ROOT, out)
html = open(src, encoding='utf-8').read()
oldp = os.path.join(ROOT, 'pipeline', 'claude_figs', 'old', f'{unit}.json')
old = json.load(open(oldp, encoding='utf-8')) if os.path.exists(oldp) else {}

spec = importlib.util.spec_from_file_location('figs', os.path.join(ROOT, 'pipeline', 'claude_figs', unit.replace('-', '_') + '.py'))
F = importlib.util.module_from_spec(spec); spec.loader.exec_module(F)

done = []
for k in range(1, 30):
    try: d = F.spec(k)
    except KeyError: continue
    num = f'{N}.{k}.1'
    m = None
    for f in re.finditer(r'<figure class="fig">.*?</figure>', html, re.S):
        if re.search(r'<b>Figure ' + re.escape(num) + r'</b>', f.group(0)): m = f; break
    if not m: sys.exit(f'no Figure {num} in {out}')
    old.setdefault(str(k), m.group(0))
    fh, ok = RD.figure_html(d['spec'], f'f{N}-{k}-1', num, d['caption'], '', [])
    if not ok: sys.exit(f'figure {num}: the svg spec did not render')
    html = html[:m.start()] + fh + html[m.end():]
    done.append(k)

os.makedirs(os.path.dirname(oldp), exist_ok=True)
json.dump(old, open(oldp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(src, 'w', encoding='utf-8').write(html)
r = subprocess.run([sys.executable, os.path.join(ROOT, 'pack', 'check_book.py'), src, os.path.join(ROOT, 'packets', f'{unit}.json'), '--render'],
                   capture_output=True, text=True)
last = (r.stdout.strip().splitlines() or [''])[-1].strip()
print(r.stdout.strip() if last != 'OK' else last)
shots = os.path.join(ROOT, 'work', 'claude_figs', unit)
os.makedirs(shots, exist_ok=True)
subprocess.run([sys.executable, os.path.join(ROOT, 'pipeline', 'claude_figs', 'shot.py'), src, os.path.join(shots, 'fig')])
print(f'redrew chapters {done}; screenshots in {shots}/fig-<k>.png')
if last != 'OK':
    sys.exit('checker not clean: fix the drawings and run again (the book file is changed; git checkout it to undo)')
if push:
    run('git', '-C', ROOT, 'add', out, oldp, os.path.join(ROOT, 'pipeline', 'claude_figs', unit.replace('-', '_') + '.py'))
    run('git', '-C', ROOT, 'commit', '-q', '-m', f'Library: {unit} with figures redrawn by Claude (chapters {done}); text unchanged')
    run('git', '-C', ROOT, 'push', '-q', 'origin', 'HEAD:main')
    print('pushed to main')
