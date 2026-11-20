"""Rebuild ec-signals-u5 from the corrected state (no model): copy state into the branch worktree, render, check."""
import json, os, sys, subprocess, shutil, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
UNIT, BR = 'ec-signals-u5', 'free/ec-signals-u5-book'
OUT = 'books/ece/ec-signals/ec-signals-u5.html'
sys.path.insert(0, os.path.join(ROOT, 'pipeline')); import render as R
sys.path.insert(0, HERE); from u import M; import figmod
wt = os.path.join(HERE, 'tree')
if not os.path.exists(wt):
    subprocess.run(['git', '-C', ROOT, 'fetch', '-q', 'origin', f'{BR}:refs/remotes/origin/{BR}'], check=True)
    subprocess.run(['git', '-C', ROOT, 'worktree', 'add', '-q', '-B', f'fix-{UNIT}', wt, f'origin/{BR}'], check=True)
st = os.path.join(wt, '.free', UNIT)
P = json.load(open(os.path.join(ROOT, 'packets', f'{UNIT}.json')))
shell = open(os.path.join(ROOT, 'pack', 'book_shell.html'), encoding='utf-8').read()
plan = json.load(open(os.path.join(HERE, 'plan.json')))
plan['about'] = ("The unit follows a signal from the analog world into the discrete world. The first chapter states the sampling theorem and shows how an ideal low-pass filter rebuilds the signal; the second explains what goes wrong below the Nyquist rate and why an analog filter sits before the sampler. "
                 "The third covers band-pass sampling and the aperture effect of practical, flat-top sampling, and the fourth, which only a few syllabi list, rounds the held samples to a finite set of levels. "
                 "The last two chapters move to discrete-time LTI systems: the convolution sum, and linear constant-coefficient difference equations with their recursive solution and pole-based stability. The discrete-time Fourier transform and the Z-transform are pointed to here and taught under Z-transform and discrete Fourier analysis.")
plan['lead'] = M(plan['lead'])
plan['links'] = [[a, b, M(t)] for a, b, t in plan['links']]
json.dump(plan, open(os.path.join(st, 'plan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
subs = P['unit']['subtopics']; ids = [s['id'] for s in subs]
chs = []
for k in range(1, len(subs) + 1):
    ch = json.load(open(os.path.join(HERE, 'new', f'ch{k}.json'), encoding='utf-8'))
    d = figmod.spec(k)
    ch['figure'] = {'after_section': {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2}[k], 'caption': M(d['caption']), 'spec': d['spec']}
    json.dump(ch, open(os.path.join(st, f'ch{k}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    h, ok = R.chapter_html(P, k, ch, ids)
    if not ok: sys.exit(f'figure {k} failed')
    chs.append(h)
us = json.load(open(os.path.join(HERE, 'new', 'unit.json'), encoding='utf-8'))
json.dump(us, open(os.path.join(st, 'unit.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
web = [w for w in json.load(open(os.path.join(st, 'web.json'), encoding='utf-8')) if 'mit.edu' not in w['url']]
json.dump(web, open(os.path.join(st, 'web.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
page = R.book(P, shell, plan, chs, us, web)
out = os.path.join(wt, OUT); os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(page)
r = subprocess.run([sys.executable, os.path.join(ROOT, 'pack', 'check_book.py'), out, os.path.join(ROOT, 'packets', f'{UNIT}.json')] + (['--render'] if '--render' in sys.argv else []), capture_output=True, text=True)
print(r.stdout.strip()[-3000:], r.stderr[-1500:])
if '--shots' in sys.argv:
    os.makedirs(os.path.join(HERE, 'shots'), exist_ok=True)
    subprocess.run([sys.executable, os.path.join(ROOT, 'pipeline', 'claude_figs', 'shot.py'), out, os.path.join(HERE, 'shots', 'fig')])
