"""Build ec-signals-u3 from the corrected state in work/ec-signals-u3/state with Claude's figures, then check it."""
import sys, os, json, importlib.util, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'pipeline'))
import render as R
unit = 'ec-signals-u3'
ST = os.path.join(os.path.dirname(__file__), 'state')
P = json.load(open(os.path.join(ROOT, 'packets', unit + '.json')))
shell = open(os.path.join(ROOT, 'pack', 'book_shell.html'), encoding='utf-8').read()
spec = importlib.util.spec_from_file_location('figs', os.path.join(ROOT, 'pipeline', 'claude_figs', 'ec_signals_u3.py'))
F = importlib.util.module_from_spec(spec); spec.loader.exec_module(F)
ids = {s['id'] for s in P['unit']['subtopics']}
chs = []
for k in range(1, len(P['unit']['subtopics']) + 1):
    ch = json.load(open(os.path.join(ST, f'ch{k}.json'), encoding='utf-8'))
    d = F.spec(k)
    ch['figure'] = {'after_section': d.get('after_section', (ch.get('figure') or {}).get('after_section', 1)), 'caption': d['caption'], 'spec': d['spec']}
    json.dump(ch, open(os.path.join(ST, f'ch{k}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    h, ok = R.chapter_html(P, k, ch, ids)
    if not ok: sys.exit(f'figure {k} failed to render')
    chs.append(h)
plan = json.load(open(os.path.join(ST, 'plan.json'), encoding='utf-8'))
us = json.load(open(os.path.join(ST, 'unit.json'), encoding='utf-8'))
web = json.load(open(os.path.join(ST, 'web.json'), encoding='utf-8'))
page = R.book(P, shell, plan, chs, us, web)
out = os.path.join(ROOT, 'books', 'ece', 'ec-signals', unit + '.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(page)
args = [sys.executable, os.path.join(ROOT, 'pack', 'check_book.py'), out, os.path.join(ROOT, 'packets', unit + '.json')] + (['--render'] if '--render' in sys.argv else [])
r = subprocess.run(args, capture_output=True, text=True); print(r.stdout[-3000:], r.stderr[-1500:])
if '--shots' in sys.argv:
    subprocess.run([sys.executable, os.path.join(ROOT, 'pipeline', 'claude_figs', 'shot.py'), out, os.path.join(os.path.dirname(__file__), 'shots', 'fig')])
