"""Put Claude's hand-drawn figures into a written book on its branch, rebuild the book and push.

    python pipeline/claude_figs/apply.py <unit> <branch> [--push]      e.g. c-os-u3 free/c-os-u3-book

Reads pipeline/claude_figs/<unit with _>.py, which defines spec(k) -> {'caption', 'spec': {'type': 'svg', ...}} for every
chapter k it redraws (chapters it does not define keep their figure). The text is not touched. The book is rebuilt from the
branch's .free/<unit>/ state with no model (--mock --offline); if the checker is not clean the run stops before the fix
loop could touch anything, so fix the drawing and run again. Screenshots of each figure go to work/claude_figs/<unit>/.
"""
import sys, os, json, subprocess, importlib.util, shutil, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
unit, branch = sys.argv[1], sys.argv[2]
push = '--push' in sys.argv
library = '--library' in sys.argv
q = json.load(open(os.path.join(ROOT, 'queue.json')))
out = next(u['out'] for u in q if u['unit'] == unit)
wt = os.path.join(ROOT, 'work', 'claude_figs', unit, 'tree')
run = lambda *a, **k: subprocess.run(a, check=True, **k)
if os.path.exists(wt):
    subprocess.run(['git', '-C', ROOT, 'worktree', 'remove', '--force', wt])
    shutil.rmtree(wt, ignore_errors=True)
run('git', '-C', ROOT, 'fetch', '-q', 'origin', f'{branch}:refs/remotes/origin/{branch}')
run('git', '-C', ROOT, 'worktree', 'add', '-q', '-B', f'cf-{unit}', wt, f'origin/{branch}')

spec = importlib.util.spec_from_file_location('figs', os.path.join(ROOT, 'pipeline', 'claude_figs', unit.replace('-', '_') + '.py'))
F = importlib.util.module_from_spec(spec); spec.loader.exec_module(F)
st = os.path.join(wt, '.free', unit)
done, fixed = [], []
for k in range(1, 30):
    p = os.path.join(st, f'ch{k}.json')
    if not os.path.exists(p): break
    try: d = F.spec(k)
    except KeyError: continue
    ch = json.load(open(p, encoding='utf-8')); old = ch.get('figure') or {}
    if not os.path.exists(os.path.join(st, f'figclaude_old{k}.json')):
        json.dump(old, open(os.path.join(st, f'figclaude_old{k}.json'), 'w'), ensure_ascii=False, indent=1)
    ch['figure'] = {'after_section': d.get('after_section', old.get('after_section', 1)), 'caption': d['caption'], 'spec': d['spec']}
    # sentences in the chapter text that describe this figure: the drawing module gives them as (old, new) pairs
    fixes = getattr(F, 'text_fixes', lambda k: [])(k) or []
    if fixes:
        raw = json.dumps(ch, ensure_ascii=False)
        for a, b in fixes:
            if raw.count(json.dumps(a, ensure_ascii=False)[1:-1]) == 0 and raw.count(json.dumps(b, ensure_ascii=False)[1:-1]) == 1:
                continue  # already rewritten by an earlier run on this branch
            if raw.count(json.dumps(a, ensure_ascii=False)[1:-1]) != 1:
                sys.exit(f'chapter {k}: text to replace not found exactly once: {a[:80]!r}')
            raw = raw.replace(json.dumps(a, ensure_ascii=False)[1:-1], json.dumps(b, ensure_ascii=False)[1:-1])
        ch = json.loads(raw)
    # a wrong worked example the drawing exposed: the module may correct the chapter in place (idempotent)
    if hasattr(F, 'chapter_fix'):
        ch = F.chapter_fix(k, ch) or ch
    json.dump(ch, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1); done.append(k)
    if fixes: fixed.append(k)
for fn in os.listdir(st):
    if re.match(r'(chfix|resize|spill|figfix)\d+', fn): os.remove(os.path.join(st, fn))
# web sources to leave out of the book (e.g. university-hosted pages): the drawing module may list URL fragments
drops = getattr(F, 'drop_sources', lambda: [])() or []
wp = os.path.join(st, 'web.json')
if drops and os.path.exists(wp):
    web = json.load(open(wp, encoding='utf-8'))
    keep = [w for w in web if not any(d in (w.get('url') or '') for d in drops)]
    if len(keep) != len(web):
        json.dump(keep, open(wp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'dropped {len(web) - len(keep)} web source(s)')

# assemble only: refuse to enter the fix loop with mock answers
sys.path.insert(0, os.path.join(ROOT, 'pipeline'))
import run_unit
real = run_unit.subprocess.run
def guard(cmd, *a, **k):
    r = real(cmd, *a, **k)
    if 'check_book.py' in ' '.join(map(str, cmd)):
        lines = (r.stdout or '').strip().splitlines()
        if not lines or lines[-1].strip() != 'OK':
            print(r.stdout); sys.exit('checker not clean: fix the drawings and run again')
    return r
run_unit.subprocess.run = guard
sys.argv = ['run_unit.py', unit, '--mock', '--offline', '--state', st, '--out', os.path.join(wt, out)]
try:
    run_unit.main()
except SystemExit as e:
    if e.code not in (0, None): raise
r = real([sys.executable, os.path.join(ROOT, 'pack', 'check_book.py'), os.path.join(wt, out), os.path.join(ROOT, 'packets', f'{unit}.json'), '--render'], capture_output=True, text=True)
print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-500:])
if 'OK' != (r.stdout.strip().splitlines() or [''])[-1].strip():
    sys.exit('checker not clean')
shots = os.path.join(ROOT, 'work', 'claude_figs', unit)
real([sys.executable, os.path.join(ROOT, 'pipeline', 'claude_figs', 'shot.py'), os.path.join(wt, out), os.path.join(shots, 'fig')])
print(f'redrew chapters {done}; screenshots in {shots}/fig-<k>.png')
if push:
    run('git', '-C', wt, 'add', '-A', '.free', out)
    textnote = f'figure sentences rewritten in chapters {fixed}' if fixed else 'text unchanged'
    trailer = os.environ.get('CF_TRAILER', '')  # e.g. Co-Authored-By / session lines, appended to every commit
    msg = f'{unit}: figures redrawn by Claude (chapters {done}); {textnote}' + (f'\n\n{trailer}' if trailer else '')
    run('git', '-C', wt, 'commit', '-q', '-m', msg)
    run('git', '-C', wt, 'push', '-q', 'origin', f'HEAD:{branch}')
    print('pushed to', branch)
if push and library:
    # the book is also the library copy on main: update it there too
    run('git', '-C', ROOT, 'pull', '-q', '--rebase', 'origin', 'main')
    os.makedirs(os.path.dirname(os.path.join(ROOT, out)), exist_ok=True)  # first book of a subject in the library
    shutil.copy(os.path.join(wt, out), os.path.join(ROOT, out))
    for e in q:
        if e['unit'] == unit: e['status'] = 'ok'
    json.dump(q, open(os.path.join(ROOT, 'queue.json'), 'w'), ensure_ascii=False, indent=1)
    run('git', '-C', ROOT, 'add', out, 'queue.json')
    run('git', '-C', ROOT, 'commit', '-q', '-m', f'Library: {unit} with figures redrawn by Claude' + (f'\n\n{trailer}' if trailer else ''))
    run('git', '-C', ROOT, 'push', '-q', 'origin', 'main')
    print('library copy on main updated')
