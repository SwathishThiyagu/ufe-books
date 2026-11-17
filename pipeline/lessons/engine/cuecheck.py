#!/usr/bin/env python3
"""cuecheck.py lesson.js [...]: on trap2, traps, notebook, recap and pa pages every cue must sit on the first two or three
words of the sentence that introduces its item. Prints each cue that starts later than word 3 of its sentence."""
import json, re, subprocess, sys, os
E = os.environ.get('E', os.path.dirname(os.path.abspath(__file__)))
KINDS = {'trap2', 'traps', 'notebook', 'recap', 'pa'}
bad_total = 0
for f in sys.argv[1:]:
    r = subprocess.run(['node', os.path.join(os.path.dirname(os.path.abspath(__file__)),'lesson_eval2.js'), f, f'{E}/lesson_template.html'], capture_output=True, text=True)
    d = json.loads(r.stdout)
    bad = []
    for s in d['scenes']:
        if s['k'] not in KINDS: continue
        say = re.sub(r'\[([^\]]+)\]\(/[^)]*/\)', r'\1', s['say'])
        for k, ph in s['cues'].items():
            if not isinstance(ph, str): continue
            if s['k']=='pa' and s.get('calc') and k not in s.get('al',[]) and k not in ('k','q','b'): continue
            ph2 = re.sub(r'\[([^\]]+)\]\(/[^)]*/\)', r'\1', ph)
            i = say.find(ph2)
            if i < 0: bad.append((s['i'] + 1, s['k'], k, ph, 'not found')); continue
            st = max([m.end() for m in re.finditer(r'[.!?:;]\s+', say[:i])] + [0])
            pre = say[st:i].split()
            if len(pre) > 2 and re.search(r',\s*$', say[:i]): continue  # cue opens a comma clause: on time
            if len(pre) > 2: bad.append((s['i'] + 1, s['k'], k, ph, f'word {len(pre)+1} of: "{say[st:i+len(ph2)][:70]}"'))
    bad_total += len(bad)
    print(f"{os.path.basename(f)}: {len(bad)} late cue(s)")
    for b in bad: print('   scene %d %s cue %s "%s": %s' % b)
sys.exit(1 if bad_total else 0)
