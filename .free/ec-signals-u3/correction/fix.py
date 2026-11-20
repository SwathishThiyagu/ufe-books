"""Corrections for ec-signals-u3: start from the draft state, write the corrected state to work/ec-signals-u3/state."""
import json, os, re, sys, shutil
H = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(H, 'draft', '.free', 'ec-signals-u3')
S = os.path.join(H, 'state')
os.makedirs(S, exist_ok=True)
sys.path.insert(0, H)

def conv(s):
    """ASCII maths to sup/sub tags."""
    for _ in range(3):
        s = re.sub(r'\^\{([^{}]*)\}', r'<sup>\1</sup>', s)
        s = re.sub(r'_\{([^{}]*)\}', r'<sub>\1</sub>', s)
    s = re.sub(r'\^\(([^()]*)\)', r'<sup>\1</sup>', s)
    s = re.sub(r'(?<![A-Za-z])([A-Za-zωτ])_(xx|xy|yx|T0|[A-Za-z0-9])(?![A-Za-z0-9])', r'\1<sub>\2</sub>', s)
    s = re.sub(r'\bT0\b', 'T₀', s); s = re.sub(r'ω0\b', 'ω₀', s); s = s.replace('ω0 ', 'ω₀ ')
    return s

def walk(o):
    if isinstance(o, str): return conv(o)
    if isinstance(o, list): return [walk(x) for x in o]
    if isinstance(o, dict): return {k: (v if k in ('figure', 'check', 'values') else walk(v)) for k, v in o.items()}
    return o

def formulas_to_p(ch):
    for sec in ch.get('sections') or []:
        nb = []
        for b in sec.get('blocks') or []:
            if b.get('type') == 'formula':
                nb.append({'type': 'p', 'text': '<b>' + b['text'] + '</b>'})
                if b.get('where'): nb.append({'type': 'p', 'text': 'Here ' + b['where']})
            else:
                nb.append(b)
        sec['blocks'] = nb
    return ch

def rep(ch, pairs):
    raw = json.dumps(ch, ensure_ascii=False)
    for a, b in pairs:
        ea, eb = json.dumps(a, ensure_ascii=False)[1:-1], json.dumps(b, ensure_ascii=False)[1:-1]
        n = raw.count(ea)
        if n != 1: sys.exit(f'not found exactly once ({n}): {a[:90]!r}')
        raw = raw.replace(ea, eb)
    return json.loads(raw)

import edits
for k in range(1, 9):
    ch = json.load(open(os.path.join(D, f'ch{k}.json'), encoding='utf-8'))
    ch = walk(ch)
    ch = formulas_to_p(ch)
    ch = edits.chapter(k, ch, rep)
    json.dump(ch, open(os.path.join(S, f'ch{k}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
us = walk(json.load(open(os.path.join(D, 'unit.json'), encoding='utf-8')))
us = edits.unit(us, rep)
json.dump(us, open(os.path.join(S, 'unit.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
plan = json.load(open(os.path.join(D, 'plan.json'), encoding='utf-8'))
plan = edits.plan(plan)
json.dump(plan, open(os.path.join(S, 'plan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
web = json.load(open(os.path.join(D, 'web.json'), encoding='utf-8'))
json.dump(edits.web(web), open(os.path.join(S, 'web.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('state written')
