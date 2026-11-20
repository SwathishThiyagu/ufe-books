"""helpers to write chapter state in light markup: x_s -> x<sub>s</sub>, x_{max} , a^n, a^{n+1}"""
import re, json
def M(s):
    if not isinstance(s, str): return s
    s = re.sub(r'(?<=[A-Za-zΔτλωΣ\]\)])_\{([^}]+)\}', r'<sub>\1</sub>', s)
    s = re.sub(r'(?<=[A-Za-zΔτλωΣ])_([A-Za-z0-9]+)', r'<sub>\1</sub>', s)
    s = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', s)
    s = re.sub(r'(?<=[A-Za-z0-9\)\]>λωτΔ])\^([A-Za-z0-9−\-]+)', r'<sup>\1</sup>', s)
    return s
def deep(o):
    if isinstance(o, str): return M(o)
    if isinstance(o, list): return [deep(x) for x in o]
    if isinstance(o, dict): return {k: (v if k in ('spec', 'check', 'svg') else deep(v)) for k, v in o.items()}
    return o
def p(t): return {'type': 'p', 'text': t}
def steps(*a): return {'type': 'steps', 'items': list(a)}
def bullets(*a): return {'type': 'bullets', 'items': list(a)}
def table(head, rows): return {'type': 'table', 'head': head, 'rows': rows}
def F(t, where=''):
    raw = M(t)
    if len(raw) <= 46: return [{'type': 'formula', 'text': t, 'where': where}]
    return [p('<b>' + t + '</b>')] + ([p(where)] if where else [])
def sec(h3, *blocks):
    out = []
    for b in blocks: out += b if isinstance(b, list) else [b]
    return {'h3': h3, 'blocks': out}
def ex(q, st, ans, dry=None):
    e = {'question': q, 'steps': st, 'answer': ans}
    if dry: e['dry_run'] = {'head': dry[0], 'rows': dry[1]}
    return e
def Q(level, marks, q, a): return {'level': level, 'q': q, 'marks': marks, 'a': a}
def save(k, ch, old):
    ch = deep(ch); ch['figure'] = old['figure']
    json.dump(ch, open(f'new/ch{k}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return ch
