"""Draw book figures from small JSON specs.

The writing model never draws SVG by hand. It picks one of the figure types below and fills
its fields; this module lays the figure out so every label fits, colours follow the shell's CSS
variables (light and dark mode), and arrowhead ids are unique in the page.

    svg = render(spec, uid="f3-2-1")   # raises FigureError with a readable reason

Types: blocks, tree, graph, array, plot, gantt, stack, sets, sequence.
"""
import math, re, html

W = 720          # viewBox width used by every book figure
M = 20           # outer margin
FS = 14          # label font size (never below 13)

STYLES = {   # box fill, stroke
    'normal': ('var(--panel)', 'var(--accent)'),
    'accent': ('var(--accent-soft)', 'var(--accent)'),
    'live':   ('var(--live-soft)', 'var(--live)'),
    'next':   ('var(--next-soft)', 'var(--next)'),
    'muted':  ('var(--panel)', 'var(--line2)'),
}
INK = {'normal': 'var(--accent)', 'accent': 'var(--accent)', 'live': 'var(--live)', 'next': 'var(--next)', 'muted': 'var(--line2)'}


class FigureError(ValueError):
    pass


# ---------- text helpers ----------
def esc(s):
    return html.escape(str(s), quote=True)

def tw(s, size=FS, bold=False):
    """Estimated text width in px (generous, so fallback fonts still fit)."""
    s = str(s)
    w = 0.0
    for ch in s:
        if ch in 'il.,:;|!\'`': w += 0.32
        elif ch in 'mwMW@%': w += 0.9
        elif ch.isupper() or ch.isdigit(): w += 0.66
        elif ch == ' ': w += 0.3
        else: w += 0.56
    return w * size * (1.06 if bold else 1.0)

def wrap(s, max_w, size=FS, bold=False, max_lines=4):
    """Split text into lines no wider than max_w. Raises if a single word cannot fit."""
    words = str(s).split()
    lines, cur = [], ''
    for wd in words:
        t = (cur + ' ' + wd).strip()
        if tw(t, size, bold) <= max_w or not cur:
            cur = t
        else:
            lines.append(cur); cur = wd
    if cur: lines.append(cur)
    lines = lines or ['']
    for ln in lines:
        if tw(ln, size, bold) > max_w:
            raise FigureError(f'label "{ln}" is too long for its box; use a shorter label')
    if len(lines) > max_lines:
        raise FigureError(f'label "{s}" needs {len(lines)} lines; shorten it to a few words')
    return lines

def text_block(x, y_mid, lines, size=FS, bold=False, anchor='middle', fill='currentColor', lh=None):
    lh = lh or round(size * 1.25)
    y0 = y_mid - (len(lines) - 1) * lh / 2 + size * 0.35
    out = []
    for i, ln in enumerate(lines):
        out.append(f'<text x="{x:.1f}" y="{y0 + i * lh:.1f}" font-size="{size}"{" font-weight=\"600\"" if bold else ""} text-anchor="{anchor}" fill="{fill}">{esc(ln)}</text>')
    return ''.join(out)

def style_of(d):
    s = (d or {}).get('style') or 'normal'
    return s if s in STYLES else 'normal'

def box(x, y, w, h, st='normal', rx=10, dashed=False):
    f, s = STYLES[st]
    da = ';stroke-dasharray:6 5' if dashed else ''
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" style="fill:{f};stroke:{s};stroke-width:2{da}"/>'

def defs(uid):
    out = ['<defs>']
    for k, c in (('n', 'var(--accent)'), ('m', 'var(--line2)'), ('l', 'var(--live)'), ('x', 'var(--next)')):
        out.append(f'<marker id="ar-{uid}-{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:{c}"/></marker>')
    out.append('</defs>')
    return ''.join(out)

EDGE = {'solid': ('var(--accent)', 'n', ''), 'accent': ('var(--accent)', 'n', ''), 'dashed': ('var(--line2)', 'm', ';stroke-dasharray:6 5'),
        'muted': ('var(--line2)', 'm', ''), 'live': ('var(--live)', 'l', ''), 'next': ('var(--next)', 'x', '')}

def line(x1, y1, x2, y2, uid, st='solid', arrow=True, both=False, width=2):
    c, k, da = EDGE.get(st or 'solid', EDGE['solid'])
    mk = f' marker-end="url(#ar-{uid}-{k})"' if arrow else ''
    if both and arrow: mk += f' marker-start="url(#ar-{uid}-{k})"'
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" style="stroke:{c};stroke-width:{width}{da}"{mk}/>'

def label_bg(x, y, s, size=13, fill='currentColor'):
    w = tw(s, size) + 8
    return (f'<rect x="{x - w / 2:.1f}" y="{y - size * 0.75:.1f}" width="{w:.1f}" height="{size * 1.5:.1f}" rx="4" style="fill:var(--fig)"/>'
            f'<text x="{x:.1f}" y="{y + size * 0.35:.1f}" font-size="{size}" text-anchor="middle" fill="{fill}">{esc(s)}</text>')

def clip_rect(cx, cy, w, h, tx, ty, pad=3):
    """Point where the segment from the box centre (cx,cy) towards (tx,ty) leaves the box."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0: return cx, cy
    sx = (w / 2 + pad) / abs(dx) if dx else 1e9
    sy = (h / 2 + pad) / abs(dy) if dy else 1e9
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s

def clip_circle(cx, cy, r, tx, ty, pad=3):
    d = math.hypot(tx - cx, ty - cy) or 1
    return cx + (tx - cx) * (r + pad) / d, cy + (ty - cy) * (r + pad) / d

def svg(h, body, aria, uid):
    h = int(math.ceil(h))
    return (f'<svg viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(aria)}">'
            f'{defs(uid)}{body}</svg>')

def need(spec, key, kind=list, min_n=1, max_n=None):
    v = spec.get(key)
    if not isinstance(v, kind) or (kind is list and len(v) < min_n):
        raise FigureError(f'"{key}" must be a {kind.__name__} with at least {min_n} item(s)')
    if max_n and kind is list and len(v) > max_n:
        raise FigureError(f'"{key}" has {len(v)} items; keep at most {max_n} (split the idea or simplify)')
    return v

def title_row(spec, y=M):
    t = spec.get('title')
    if not t: return '', y
    lines = wrap(t, W - 2 * M, 15, True, 2)
    return text_block(W / 2, y + 10 + (len(lines) - 1) * 9, lines, 15, True), y + 18 + len(lines) * 19


# ---------- blocks: block diagrams and flowcharts ----------
def r_blocks(spec, uid):
    nodes = need(spec, 'nodes', list, 2, 14)
    ids = [str(n.get('id')) for n in nodes]
    if len(set(ids)) != len(ids): raise FigureError('node ids must be unique')
    edges = [e for e in (spec.get('edges') or []) if str(e.get('from')) in ids and str(e.get('to')) in ids]
    idx = {i: k for k, i in enumerate(ids)}
    # layers by longest path, ignoring edges that close a cycle
    succ = {i: [] for i in ids}
    state, back = {}, set()
    for e in edges: succ[str(e['from'])].append(str(e['to']))
    def dfs(u):
        state[u] = 1
        for v in succ[u]:
            if state.get(v) == 1: back.add((u, v))
            elif not state.get(v): dfs(v)
        state[u] = 2
    for i in ids:
        if not state.get(i): dfs(i)
    layer = {i: 0 for i in ids}
    for _ in range(len(ids)):
        for e in edges:
            a, b = str(e['from']), str(e['to'])
            if (a, b) in back or a == b: continue
            if layer[b] < layer[a] + 1: layer[b] = layer[a] + 1
    if isinstance(spec.get('layers'), list):   # the model may fix the rows itself
        for li, row in enumerate(spec['layers']):
            for i in row:
                if str(i) in layer: layer[str(i)] = li
    L = max(layer.values()) + 1
    rows = [[i for i in ids if layer[i] == l] for l in range(L)]
    direction = spec.get('direction', 'down')
    if direction == 'right' and (L > 5 or max(len(r) for r in rows) > 4): direction = 'down'
    if direction == 'down' and max(len(r) for r in rows) > 5:
        raise FigureError('a row of the block diagram has more than 5 boxes; use fewer nodes or set "layers"')
    head, y = title_row(spec)
    pos = {}
    body = [head]
    def box_lines(n, bw):
        lab = wrap(n.get('label', ''), bw - 16, FS, True, 3)
        note = wrap(n['note'], bw - 16, 13, False, 3) if n.get('note') else []
        return lab, note
    if direction == 'down':
        gap_y = 54 if any(e.get('label') for e in edges) else 40
        for r in rows:
            n = len(r)
            gap = 24
            bw = min(230, (W - 2 * M - (n - 1) * gap) / n)
            content = [box_lines(nodes[idx[i]], bw) for i in r]
            bh = max(14 + len(a) * 18 + len(b) * 16 + (4 if b else 0) for a, b in content)
            total = n * bw + (n - 1) * gap
            x0 = (W - total) / 2
            for k, i in enumerate(r):
                pos[i] = (x0 + k * (bw + gap) + bw / 2, y + bh / 2, bw, bh, content[k])
            y += bh + gap_y
        H = y - gap_y + M
    else:
        lab_w = max([tw(e.get('label', ''), 13) for e in edges if e.get('label')] + [0])
        gap_x = max(44, lab_w + 34)
        bw = min(200, (W - 2 * M - (L - 1) * gap_x) / L)
        if bw < 90: raise FigureError('too many columns for a left-to-right diagram; use direction "down"')
        col_h = []
        cols = []
        for r in rows:
            content = [box_lines(nodes[idx[i]], bw) for i in r]
            hs = [14 + len(a) * 18 + len(b) * 16 + (4 if b else 0) for a, b in content]
            cols.append((r, content, hs)); col_h.append(sum(hs) + (len(r) - 1) * 26)
        Hc = max(col_h)
        for l, (r, content, hs) in enumerate(cols):
            x = M + l * (bw + gap_x) + bw / 2 + (W - 2 * M - (L * bw + (L - 1) * gap_x)) / 2
            yy = y + (Hc - col_h[l]) / 2
            for k, i in enumerate(r):
                pos[i] = (x, yy + hs[k] / 2, bw, hs[k], content[k]); yy += hs[k] + 26
        H = y + Hc + M
    # edges first (under boxes); edges that go back up the flow curve around the side
    labels = []
    extra = 0
    route = {}
    if direction == 'right':
        def clear(i, side):
            x, y, w, h, _ = pos[i]
            return not any(j != i and abs(pos[j][0] - x) < 1 and ((pos[j][1] > y) if side == 'bottom' else (pos[j][1] < y)) for j in ids)
        for e in edges:
            a, b = str(e['from']), str(e['to'])
            if (a, b) in back or layer[a] > layer[b]:
                route[(a, b)] = 'bottom' if clear(a, 'bottom') and clear(b, 'bottom') else ('top' if clear(a, 'top') and clear(b, 'top') else 'bottom')
        if 'top' in route.values():
            for i in ids:
                x, yy, w, h, c = pos[i]; pos[i] = (x, yy + 52, w, h, c)
            H += 52
    for e in edges:
        a, b = str(e['from']), str(e['to'])
        if a == b: continue
        ax, ay, aw, ah, _ = pos[a]; bx, by, bw_, bh, _ = pos[b]
        st = e.get('style', 'solid')
        c, k, da = EDGE.get(st or 'solid', EDGE['solid'])
        if (a, b) in back or (layer[a] > layer[b]):
            if direction == 'down':
                x1, y1, x2, y2 = ax + aw / 2 + 3, ay, bx + bw_ / 2 + 5, by
                bend = max(x1, x2) + 46
                if bend > W - 8: x1, x2, bend = ax - aw / 2 - 3, bx - bw_ / 2 - 5, min(ax - aw / 2, bx - bw_ / 2) - 46
                if bend < 8: raise FigureError('a back edge has no room beside the boxes; make the boxes narrower')
                body.append(f'<path d="M{x1:.1f},{y1:.1f} C{bend:.1f},{y1:.1f} {bend:.1f},{y2:.1f} {x2:.1f},{y2:.1f}" style="fill:none;stroke:{c};stroke-width:2{da}" marker-end="url(#ar-{uid}-{k})"/>')
                lx, ly = bend - (12 if bend > x1 else -12), (y1 + y2) / 2
            elif route.get((a, b)) == 'top':
                high = min(ay - ah / 2, by - bh / 2)
                x1, y1, x2, y2 = ax, ay - ah / 2 - 3, bx, by - bh / 2 - 5
                body.append(f'<path d="M{x1:.1f},{y1:.1f} C{x1:.1f},{high - 50:.1f} {x2:.1f},{high - 50:.1f} {x2:.1f},{y2:.1f}" style="fill:none;stroke:{c};stroke-width:2{da}" marker-end="url(#ar-{uid}-{k})"/>')
                lx, ly = (x1 + x2) / 2, high - 38
            else:
                low = max(ay + ah / 2, by + bh / 2)
                x1, y1, x2, y2 = ax, ay + ah / 2 + 3, bx, by + bh / 2 + 5
                body.append(f'<path d="M{x1:.1f},{y1:.1f} C{x1:.1f},{low + 50:.1f} {x2:.1f},{low + 50:.1f} {x2:.1f},{y2:.1f}" style="fill:none;stroke:{c};stroke-width:2{da}" marker-end="url(#ar-{uid}-{k})"/>')
                lx, ly = (x1 + x2) / 2, low + 38
                extra = max(extra, low + 52 - (H - M))
        else:
            x1, y1 = clip_rect(ax, ay, aw, ah, bx, by)
            x2, y2 = clip_rect(bx, by, bw_, bh, ax, ay, pad=5)
            body.append(line(x1, y1, x2, y2, uid, st, True, bool(e.get('both'))))
            lx, ly = (ax + bx) / 2, (ay + by) / 2
            if direction == 'down' and abs(ay - by) > 1 and abs(ax - bx) > 1:
                ly = (y1 + y2) / 2
        if e.get('label'): labels.append(label_bg(lx, ly, e['label'], 13))
    H += max(0, extra)
    body += labels
    for i in ids:
        x, yc, bw, bh, (lab, note) = pos[i]
        st = style_of(nodes[idx[i]])
        body.append(box(x - bw / 2, yc - bh / 2, bw, bh, st, dashed=nodes[idx[i]].get('dashed', False)))
        tot = len(lab) * 18 + (len(note) * 16 + 4 if note else 0)
        top = yc - tot / 2
        body.append(text_block(x, top + len(lab) * 9, lab, FS, True, lh=18))
        if note: body.append(text_block(x, top + len(lab) * 18 + 4 + len(note) * 8, note, 13, False, fill='var(--muted)', lh=16))
    return svg(H, ''.join(body), spec.get('aria') or 'Block diagram', uid)


# ---------- tree ----------
def r_tree(spec, uid):
    root = spec.get('root')
    if not isinstance(root, dict): raise FigureError('"root" must be an object {label, children}')
    allnodes = []
    def walk(n, d):
        if d > 6: raise FigureError('tree is deeper than 6 levels; show fewer levels')
        n['_d'] = d; allnodes.append(n)
        n['children'] = [c for c in (n.get('children') or []) if isinstance(c, dict)]
        for c in n['children']: walk(c, d + 1)
    walk(root, 0)
    if len(allnodes) > 40: raise FigureError('tree has more than 40 nodes; show a smaller example')
    circle = spec.get('shape', 'auto') == 'circle' or (spec.get('shape', 'auto') == 'auto' and all(len(str(n.get('label', ''))) <= 3 for n in allnodes))
    leaves = [n for n in allnodes if not n['children']]
    nw = 40 if circle else min(150, max(tw(n.get('label', ''), FS, True) + 22 for n in allnodes))
    spacing = max(nw + 14, min(110 if circle else nw + 30, (W - 2 * M) / max(1, len(leaves))))
    if len(leaves) * spacing > W - 2 * M:
        spacing = (W - 2 * M) / len(leaves)
        if spacing < nw + 6:
            if circle and spacing >= 36: nw = spacing - 4
            else: raise FigureError(f'tree is too wide ({len(leaves)} leaves); use fewer leaves or shorter labels')
    head, y0 = title_row(spec)
    depth = max(n['_d'] for n in allnodes)
    level_h = 74 if any(n.get('edge') for n in allnodes) else 64
    nh = 36
    counter = [0]
    def place(n):
        if not n['children']:
            n['_x'] = counter[0] * spacing + spacing / 2; counter[0] += 1
        else:
            for c in n['children']: place(c)
            n['_x'] = (n['children'][0]['_x'] + n['children'][-1]['_x']) / 2
        n['_y'] = y0 + 22 + n['_d'] * level_h
    place(root)
    off = (W - counter[0] * spacing) / 2
    body = [head]
    for n in allnodes: n['_x'] += off
    for n in allnodes:
        for c in n['children']:
            st = c.get('edge_style') or 'solid'
            if circle:
                x1, y1 = clip_circle(n['_x'], n['_y'], nw / 2, c['_x'], c['_y'])
                x2, y2 = clip_circle(c['_x'], c['_y'], nw / 2, n['_x'], n['_y'])
            else:
                x1, y1 = clip_rect(n['_x'], n['_y'], nw, nh, c['_x'], c['_y'])
                x2, y2 = clip_rect(c['_x'], c['_y'], nw, nh, n['_x'], n['_y'])
            body.append(line(x1, y1, x2, y2, uid, st, bool(spec.get('arrows'))))
            if c.get('edge'):
                body.append(label_bg((n['_x'] + c['_x']) / 2 + (8 if c['_x'] >= n['_x'] else -8), (n['_y'] + c['_y']) / 2, str(c['edge']), 13, 'var(--live)'))
    for n in allnodes:
        st = style_of(n); f, s = STYLES[st]
        lab = str(n.get('label', ''))
        if circle:
            body.append(f'<circle cx="{n["_x"]:.1f}" cy="{n["_y"]:.1f}" r="{nw / 2:.1f}" style="fill:{f};stroke:{s};stroke-width:2"/>')
            if tw(lab, FS, True) > nw - 4: raise FigureError(f'tree label "{lab}" does not fit in a circle; use shape "box"')
        else:
            body.append(box(n['_x'] - nw / 2, n['_y'] - nh / 2, nw, nh, st, 8))
            if tw(lab, FS, True) > nw - 10: raise FigureError(f'tree label "{lab}" is too long; shorten it')
        body.append(text_block(n['_x'], n['_y'], [lab], FS, True))
        if n.get('note'):
            body.append(f'<text x="{n["_x"] + (nw / 2 + 4):.1f}" y="{n["_y"] - nh / 2 + 2:.1f}" font-size="13" fill="var(--live)">{esc(n["note"])}</text>')
    H = y0 + 22 + depth * level_h + nh / 2 + M
    # notes to the right of the right-most node must stay inside
    for n in allnodes:
        if n.get('note') and n['_x'] + nw / 2 + 4 + tw(n['note'], 13) > W - 6:
            raise FigureError(f'note "{n["note"]}" runs off the right edge; shorten it')
    return svg(H, ''.join(body), spec.get('aria') or 'Tree diagram', uid)


# ---------- graph ----------
def r_graph(spec, uid):
    nodes = need(spec, 'nodes', list, 2, 16)
    ids = [str(n.get('id')) for n in nodes]
    if len(set(ids)) != len(ids): raise FigureError('node ids must be unique')
    edges = [e for e in (spec.get('edges') or []) if str(e.get('from')) in ids and str(e.get('to')) in ids]
    directed = bool(spec.get('directed'))
    head, y0 = title_row(spec)
    r = 20 if all(len(str(n.get('label', n.get('id')))) <= 3 for n in nodes) else 0
    bwid = {i: (2 * r if r else min(140, tw(n.get('label', i), FS, True) + 20)) for i, n in zip(ids, nodes)}
    gh = 300
    if all(isinstance(n.get('x'), (int, float)) and isinstance(n.get('y'), (int, float)) for n in nodes):
        xs = [n['x'] for n in nodes]; ys = [n['y'] for n in nodes]
        sx = (max(xs) - min(xs)) or 1; sy = (max(ys) - min(ys)) or 1
        gh = max(160, min(380, 300 * sy / sx * 1.2)) if sx else 300
        P = {i: (M + 50 + (n['x'] - min(xs)) / sx * (W - 2 * M - 100), y0 + 40 + (n['y'] - min(ys)) / sy * (gh - 80)) for i, n in zip(ids, nodes)}
    else:
        n = len(nodes); cx, cy = W / 2, y0 + gh / 2
        rx, ry = min(280, 60 + 26 * n), gh / 2 - 40
        P = {i: (cx + rx * math.cos(-math.pi / 2 + 2 * math.pi * k / n), cy + ry * math.sin(-math.pi / 2 + 2 * math.pi * k / n)) for k, i in enumerate(ids)}
    pairs = {(str(e['from']), str(e['to'])) for e in edges}
    body = [head]
    def clip(i, tx, ty, pad=3):
        x, y = P[i]
        return clip_circle(x, y, r, tx, ty, pad) if r else clip_rect(x, y, bwid[i], 34, tx, ty, pad)
    for e in edges:
        a, b = str(e['from']), str(e['to'])
        if a == b: continue
        (ax, ay), (bx, by) = P[a], P[b]
        st = e.get('style', 'solid')
        c, k, da = EDGE.get(st, EDGE['solid'])
        curved = directed and (b, a) in pairs
        if curved:
            mx, my = (ax + bx) / 2, (ay + by) / 2
            dx, dy = bx - ax, by - ay; d = math.hypot(dx, dy) or 1
            cxp, cyp = mx - dy / d * 26, my + dx / d * 26
            x1, y1 = clip(a, cxp, cyp); x2, y2 = clip(b, cxp, cyp, 5)
            mk = f' marker-end="url(#ar-{uid}-{k})"'
            body.append(f'<path d="M{x1:.1f},{y1:.1f} Q{cxp:.1f},{cyp:.1f} {x2:.1f},{y2:.1f}" style="fill:none;stroke:{c};stroke-width:{3 if st == "accent" else 2}{da}"{mk}/>')
            lx, ly = (x1 + 2 * cxp + x2) / 4, (y1 + 2 * cyp + y2) / 4
        else:
            x1, y1 = clip(a, bx, by); x2, y2 = clip(b, ax, ay, 5 if directed else 3)
            body.append(line(x1, y1, x2, y2, uid, st, directed, False, 3 if st == 'accent' else 2))
            lx, ly = (ax + bx) / 2, (ay + by) / 2
        if e.get('label') not in (None, ''):
            body.append(label_bg(lx, ly, str(e['label']), 13, 'var(--live)'))
    for i, n in zip(ids, nodes):
        x, y = P[i]; st = style_of(n); f, s = STYLES[st]
        lab = str(n.get('label', i))
        if r:
            body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{f};stroke:{s};stroke-width:2"/>')
        else:
            body.append(box(x - bwid[i] / 2, y - 17, bwid[i], 34, st, 8))
            if tw(lab, FS, True) > bwid[i] - 8: raise FigureError(f'graph label "{lab}" is too long')
        body.append(text_block(x, y, [lab], FS, True))
        if n.get('note'):
            nt = str(n['note'])
            lower = y > y0 + gh / 2 + 10
            ty = y + (r or 17) + 18 if lower else y - (r or 17) - 9
            if x + tw(nt, 13) / 2 > W - 6 or x - tw(nt, 13) / 2 < 6: raise FigureError(f'note "{nt}" runs off the edge; shorten it')
            body.append(f'<text x="{x:.1f}" y="{ty:.1f}" font-size="13" font-weight="600" text-anchor="middle" style="fill:var(--next)">{esc(nt)}</text>')
    for i in ids:
        x, y = P[i]
        if x - bwid[i] / 2 < 4 or x + bwid[i] / 2 > W - 4: raise FigureError('a graph node falls outside the figure; use fewer nodes')
    return svg(y0 + gh + 10, ''.join(body), spec.get('aria') or 'Graph', uid)


# ---------- array ----------
def r_array(spec, uid):
    rows = need(spec, 'rows', list, 1, 8)
    maxn = max(len(r.get('cells') or []) for r in rows)
    if maxn < 1: raise FigureError('array rows need cells')
    if maxn > 16: raise FigureError('an array row has more than 16 cells; show a shorter array')
    labw = max([tw(r.get('label', ''), 13, True) for r in rows] + [0])
    labw = labw + 12 if labw else 0
    if labw > 150: raise FigureError('row labels are too long; keep them to a few words')
    allv = [str(c) for r in rows for c in (r.get('cells') or [])]
    vw = max(tw(v, FS, True) for v in allv) + 14
    cw = min(max(40, vw), 64, (W - 2 * M - labw) / maxn)
    if vw > cw: raise FigureError(f'array values are too long for {maxn} cells; shorten values')
    ch = 40
    head, y = title_row(spec)
    body = [head]
    ptrs = spec.get('pointers') or []
    x0 = (W - labw - maxn * cw) / 2 + labw
    if spec.get('show_index', True):
        for k in range(maxn):
            body.append(f'<text x="{x0 + k * cw + cw / 2:.1f}" y="{y + 12:.1f}" font-size="13" text-anchor="middle" style="fill:var(--muted)">{k + spec.get("index_from", 0)}</text>')
        y += 20
    for ri, r in enumerate(rows):
        cells = r.get('cells') or []
        marks = {str(k): v for k, v in (r.get('marks') or {}).items()}
        if r.get('label'):
            body.append(f'<text x="{x0 - 10:.1f}" y="{y + ch / 2 + 5:.1f}" font-size="13" font-weight="600" text-anchor="end" fill="currentColor">{esc(r["label"])}</text>')
        for k, v in enumerate(cells):
            st = marks.get(str(k), 'normal'); st = st if st in STYLES else 'normal'
            body.append(box(x0 + k * cw, y, cw, ch, st, 4))
            body.append(text_block(x0 + k * cw + cw / 2, y + ch / 2, [str(v)], FS, True))
        rp = [p for p in ptrs if int(p.get('row', 0)) == ri]
        y += ch
        if rp:
            for p in rp:
                k = int(p.get('cell', 0)); px = x0 + k * cw + cw / 2
                body.append(line(px, y + 26, px, y + 4, uid, 'live', True))
                lab = str(p.get('label', ''))
                if px + tw(lab, 13) / 2 > W - 4 or px - tw(lab, 13) / 2 < 4: raise FigureError(f'pointer label "{lab}" runs off the edge')
                body.append(f'<text x="{px:.1f}" y="{y + 42:.1f}" font-size="13" font-weight="600" text-anchor="middle" style="fill:var(--live)">{esc(lab)}</text>')
            y += 48
        y += 14
    return svg(y + M - 14, ''.join(body), spec.get('aria') or 'Array diagram', uid)


# ---------- plot ----------
SAFE = {k: getattr(math, k) for k in ('sqrt', 'log', 'log2', 'log10', 'exp', 'sin', 'cos', 'tan', 'pi', 'e', 'floor', 'ceil', 'factorial', 'atan', 'tanh')}
SAFE.update(abs=abs, min=min, max=max, pow=pow)

def safe_eval(expr, x):
    if re.search(r'__|import|lambda|open|exec|eval', expr): raise FigureError('plot expression not allowed')
    return float(eval(expr, {'__builtins__': {}}, dict(SAFE, x=x, n=x, t=x)))

def nice_ticks(lo, hi, n=5):
    if hi <= lo: hi = lo + 1
    raw = (hi - lo) / n
    mag = 10 ** math.floor(math.log10(raw))
    step = min((m * mag for m in (1, 2, 2.5, 5, 10) if m * mag >= raw), default=10 * mag)
    a = math.floor(lo / step) * step
    ticks = []
    t = a
    while t <= hi + step * 0.001:
        ticks.append(round(t, 10)); t += step
    return ticks, step

def fmt(v):
    if abs(v) >= 1e6 or (abs(v) < 1e-3 and v): return f'{v:.1e}'
    if float(v).is_integer(): return f'{int(v):,}'
    return f'{v:.3g}'

def r_plot(spec, uid):
    series = need(spec, 'series', list, 1, 4)
    X = spec.get('x') or {}; Y = spec.get('y') or {}
    xlo, xhi = float(X.get('min', 0)), float(X.get('max', 10))
    if xhi <= xlo: raise FigureError('x.max must be above x.min')
    pts_all = []
    for s in series:
        if s.get('points'):
            pts = [(float(p[0]), float(p[1])) for p in s['points']]
        elif s.get('expr'):
            k = 80
            discrete = bool(s.get('discrete'))
            xs = list(range(int(math.ceil(xlo)), int(math.floor(xhi)) + 1)) if discrete else [xlo + (xhi - xlo) * i / k for i in range(k + 1)]
            pts = []
            for x in xs:
                try:
                    v = safe_eval(s['expr'], x)
                    if math.isfinite(v): pts.append((x, v))
                except (ValueError, ZeroDivisionError, OverflowError):
                    pass
                except FigureError: raise
                except Exception as e:
                    raise FigureError(f'cannot evaluate "{s["expr"]}": {e}')
        else:
            raise FigureError('each series needs "expr" or "points"')
        if not pts: raise FigureError(f'series "{s.get("name")}" has no points')
        s['_pts'] = pts; pts_all += pts
    ylo = float(Y['min']) if 'min' in Y else min(0, min(p[1] for p in pts_all))
    yhi = float(Y['max']) if 'max' in Y else max(p[1] for p in pts_all)
    if 'max' in Y:
        for s in series: s['_pts'] = [p for p in s['_pts'] if p[1] <= yhi * 1.0001]
    yt, _ = nice_ticks(ylo, yhi); xt, _ = nice_ticks(xlo, xhi)
    ylo, yhi = min(yt[0], ylo), max(yt[-1], yhi)
    xlo2, xhi2 = min(xt[0], xlo), max(xt[-1], xhi)
    head, y0 = title_row(spec)
    ylab_w = max(tw(fmt(t), 13) for t in yt)
    L, R, T, B = M + 26 + ylab_w, W - M - 10, y0 + 14, y0 + 274
    px = lambda x: L + (x - xlo2) / (xhi2 - xlo2) * (R - L)
    py = lambda y: B - (y - ylo) / (yhi - ylo) * (B - T)
    body = [head]
    for t in yt:
        body.append(f'<line x1="{L}" y1="{py(t):.1f}" x2="{R}" y2="{py(t):.1f}" style="stroke:var(--line);stroke-width:1"/>')
        body.append(f'<text x="{L - 6}" y="{py(t) + 4:.1f}" font-size="13" text-anchor="end" style="fill:var(--muted)">{fmt(t)}</text>')
    for t in xt:
        body.append(f'<line x1="{px(t):.1f}" y1="{B}" x2="{px(t):.1f}" y2="{B + 5}" style="stroke:var(--line2);stroke-width:1"/>')
        body.append(f'<text x="{px(t):.1f}" y="{B + 20}" font-size="13" text-anchor="middle" style="fill:var(--muted)">{fmt(t)}</text>')
    body.append(f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" style="stroke:var(--line2);stroke-width:1.5"/><line x1="{L}" y1="{T}" x2="{L}" y2="{B}" style="stroke:var(--line2);stroke-width:1.5"/>')
    if X.get('label'): body.append(f'<text x="{(L + R) / 2:.1f}" y="{B + 40}" font-size="13" font-weight="600" text-anchor="middle" fill="currentColor">{esc(X["label"])}</text>')
    if Y.get('label'):
        yl = str(Y['label'])
        if tw(yl, 13, True) > (B - T): raise FigureError('y-axis label is too long')
        body.append(f'<text transform="translate({M + 6},{(T + B) / 2:.1f}) rotate(-90)" font-size="13" font-weight="600" text-anchor="middle" fill="currentColor">{esc(yl)}</text>')
    colors = ['var(--accent)', 'var(--live)', 'var(--next)', 'var(--muted)']
    labels = []
    for k, s in enumerate(series):
        c = {'accent': 'var(--accent)', 'live': 'var(--live)', 'next': 'var(--next)', 'muted': 'var(--muted)'}.get(s.get('style'), colors[k % 4])
        pts = sorted(s['_pts'])
        d = ' '.join(f'{"M" if i == 0 else "L"}{px(x):.1f},{py(y):.1f}' for i, (x, y) in enumerate(pts))
        dash = ';stroke-dasharray:7 5' if s.get('dashed') else ''
        if s.get('points') and not s.get('line', True):
            pass
        else:
            body.append(f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:2.5{dash}"/>')
        if s.get('points'):
            for x, y in pts: body.append(f'<circle cx="{px(x):.1f}" cy="{py(y):.1f}" r="4" style="fill:{c}"/>')
        if s.get('name'):
            lx, ly = px(pts[-1][0]), py(pts[-1][1])
            labels.append([lx, ly, str(s['name']), c])
    # direct labels at the end of each line, nudged apart and kept inside the plot
    labels.sort(key=lambda a: a[1])
    for i, a in enumerate(labels):
        a[1] = max(a[1] - 8, T + 12)
        if i and a[1] - labels[i - 1][1] < 17: a[1] = labels[i - 1][1] + 17
    for lx, ly, name, c in labels:
        wdt = tw(name, 13, True)
        x = min(lx - 4, R - 2)
        if x - wdt < L + 4: raise FigureError(f'series name "{name}" is too long; shorten it')
        body.append(f'<rect x="{x - wdt - 3:.1f}" y="{ly - 12:.1f}" width="{wdt + 6:.1f}" height="17" rx="3" style="fill:var(--fig);opacity:.85"/>')
        body.append(f'<text x="{x:.1f}" y="{ly:.1f}" font-size="13" font-weight="600" text-anchor="end" style="fill:{c}">{esc(name)}</text>')
    return svg(B + (52 if X.get('label') else 32), ''.join(body), spec.get('aria') or 'Plot', uid)


# ---------- gantt: schedules and timelines ----------
def r_gantt(spec, uid):
    lanes = need(spec, 'lanes', list, 1, 6)
    bars = [b for ln in lanes for b in (ln.get('bars') or [])]
    if not bars: raise FigureError('gantt lanes need bars')
    t0 = min(float(b['start']) for b in bars); t1 = max(float(b['end']) for b in bars)
    if t1 <= t0: raise FigureError('bar end must be after start')
    labw = max(tw(ln.get('label', ''), 13, True) for ln in lanes) + 14
    if labw > 160: raise FigureError('lane labels are too long')
    head, y = title_row(spec)
    L, R = M + labw, W - M - 8
    px = lambda t: L + (t - t0) / (t1 - t0) * (R - L)
    body = [head]
    lh = 46
    for ln in lanes:
        body.append(f'<text x="{L - 10:.1f}" y="{y + lh / 2 + 5:.1f}" font-size="13" font-weight="600" text-anchor="end" fill="currentColor">{esc(ln.get("label", ""))}</text>')
        for b in ln.get('bars') or []:
            x1, x2 = px(float(b['start'])), px(float(b['end']))
            st = style_of(b) if b.get('style') else 'accent'
            body.append(box(x1, y + 4, max(2, x2 - x1), lh - 8, st, 4, dashed=bool(b.get('idle'))))
            lab = str(b.get('label', ''))
            if lab:
                if tw(lab, 13, True) + 6 <= x2 - x1:
                    body.append(text_block((x1 + x2) / 2, y + lh / 2, [lab], 13, True))
                elif tw(lab, 13, True) + 4 <= (x2 - x1) * 1.8 and x2 - x1 > 14:
                    body.append(text_block((x1 + x2) / 2, y + lh / 2, [lab], 13, True))   # tight but readable
                else:
                    raise FigureError(f'bar "{lab}" is too short for its label; widen the time span or shorten the label')
        y += lh + 6
    ticks = sorted({float(b['start']) for b in bars} | {float(b['end']) for b in bars})
    if len(ticks) > 18: ticks, _ = nice_ticks(t0, t1, 8)
    last = -1e9
    body.append(f'<line x1="{L}" y1="{y}" x2="{R}" y2="{y}" style="stroke:var(--line2);stroke-width:1.5"/>')
    for t in ticks:
        x = px(t)
        if x - last < tw(fmt(t), 13) + 6: continue
        body.append(f'<line x1="{x:.1f}" y1="{y}" x2="{x:.1f}" y2="{y + 5}" style="stroke:var(--line2)"/><text x="{x:.1f}" y="{y + 20}" font-size="13" text-anchor="middle" style="fill:var(--muted)">{fmt(t)}</text>')
        last = x
    if spec.get('unit'):
        body.append(f'<text x="{R:.1f}" y="{y + 38}" font-size="13" text-anchor="end" style="fill:var(--muted)">time ({esc(spec["unit"])})</text>')
        y += 18
    return svg(y + 28 + M, ''.join(body), spec.get('aria') or 'Timeline', uid)


# ---------- stack: layers, hierarchies, pyramids ----------
def r_stack(spec, uid):
    items = need(spec, 'items', list, 2, 10)
    side = spec.get('side') or {}
    pyramid = bool(spec.get('pyramid'))
    head, y = title_row(spec)
    sidew = 120 if side else 0
    full = W - 2 * M - sidew
    body = [head]
    n = len(items)
    y_start = y
    for k, it in enumerate(items):
        w = full * (0.42 + 0.58 * (k + 1) / n) if pyramid else full
        x = M + (full - w) / 2
        lab = wrap(it.get('label', ''), w - 24, FS, True, 2)
        note = wrap(it['note'], w - 24, 13, False, 2) if it.get('note') else []
        h = 16 + len(lab) * 18 + (len(note) * 16 + 2 if note else 0)
        body.append(box(x, y, w, h, style_of(it), 6))
        tot = len(lab) * 18 + (len(note) * 16 + 2 if note else 0)
        top = y + (h - tot) / 2
        body.append(text_block(x + w / 2, top + len(lab) * 9, lab, FS, True, lh=18))
        if note: body.append(text_block(x + w / 2, top + len(lab) * 18 + 2 + len(note) * 8, note, 13, False, fill='var(--muted)', lh=16))
        y += h + 6
    if side:
        ax = W - M - sidew / 2
        body.append(line(ax, y_start + 26, ax, y - 30, uid, 'live', True, True))
        for key, yy in (('top', y_start + 12), ('bottom', y - 6)):
            if side.get(key):
                lines = wrap(side[key], sidew - 4, 13, True, 2)
                body.append(text_block(ax, yy - (6 if key == 'bottom' else -2), lines, 13, True, fill='var(--live)', lh=15))
    return svg(y + M - 6, ''.join(body), spec.get('aria') or 'Layer diagram', uid)


# ---------- sets: nested classes or a Venn diagram ----------
def r_sets(spec, uid):
    sets = need(spec, 'sets', list, 1, 4)
    mode = spec.get('mode', 'nested')
    head, y0 = title_row(spec)
    body = [head]
    if mode == 'venn' and len(sets) in (2, 3):
        r = 120 if len(sets) == 2 else 105
        cx0 = W / 2
        if len(sets) == 2: C = [(cx0 - 78, y0 + 40 + r), (cx0 + 78, y0 + 40 + r)]
        else: C = [(cx0 - 70, y0 + 40 + r), (cx0 + 70, y0 + 40 + r), (cx0, y0 + 40 + r + 115)]
        sts = ['accent', 'live', 'next']
        for (x, y), s, st in zip(C, sets, sts):
            f, c = STYLES[style_of(s) if s.get('style') else st]
            body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{f};fill-opacity:.55;stroke:{c};stroke-width:2"/>')
        for k, ((x, y), s) in enumerate(zip(C, sets)):
            lab = wrap(s.get('label', ''), 2 * r - 20, FS, True, 2)
            ly = y - r - 10 if k < 2 else y + r + 18
            body.append(text_block(x, ly, lab, FS, True))
            items = [str(i) for i in (s.get('items') or [])][:5]
            ix = x - 62 if (len(sets) >= 2 and k == 0) else (x + 62 if k == 1 else x)
            iy = y if k < 2 else y + 40
            if items:
                lines = []
                for it in items: lines += wrap(it, r * 0.85, 13, False, 2)
                body.append(text_block(ix, iy, lines[:6], 13, False, lh=16))
        ov = [str(i) for i in (spec.get('overlap') or [])][:4]
        if ov and len(sets) == 2:
            lines = []
            for it in ov: lines += wrap(it, 70, 13, True, 2)
            body.append(text_block(cx0, C[0][1], lines[:5], 13, True, lh=16))
        H = (C[-1][1] + r + (30 if len(sets) == 3 else 0)) + M
        return svg(H, ''.join(body), spec.get('aria') or 'Venn diagram', uid)
    # nested ellipses, outermost first
    n = len(sets)
    rx0, ry0 = 320, 52 + 46 * n
    cx, cy = W / 2, y0 + 10 + ry0
    for k, s in enumerate(sets):
        rx, ry = rx0 - k * (rx0 - 90) / max(1, n - 1) * (0.9 if n > 1 else 0), ry0 - k * 46
        if n == 1: rx, ry = 300, 90
        st = style_of(s) if s.get('style') else ['muted', 'accent', 'live', 'next'][k % 4]
        f, c = STYLES[st]
        body.append(f'<ellipse cx="{cx}" cy="{cy + k * 46 - (0 if k == 0 else 0):.1f}" rx="{rx:.1f}" ry="{ry:.1f}" style="fill:{f};fill-opacity:.6;stroke:{c};stroke-width:2"/>')
        top = cy + k * 46 - ry
        band_w = rx * 1.3 if k < n - 1 else rx * 1.5
        lab = wrap(s.get('label', ''), band_w, FS, True, 1)
        items = ', '.join(str(i) for i in (s.get('items') or [])[:4])
        body.append(text_block(cx, top + 18, lab, FS, True))
        if items:
            if k < n - 1:
                il = wrap(items, band_w * 0.95, 13, False, 1)
                body.append(text_block(cx, top + 36, il, 13, False, fill='var(--muted)'))
            else:
                il = wrap(items, band_w * 0.9, 13, False, 3)
                body.append(text_block(cx, top + 30 + len(il) * 8 + 8, il, 13, False, fill='var(--muted)', lh=16))
    H = cy + ry0 + M
    return svg(H, ''.join(body), spec.get('aria') or 'Nested sets', uid)


# ---------- sequence: messages between parties ----------
def r_sequence(spec, uid):
    actors = [str(a) for a in need(spec, 'actors', list, 2, 5)]
    msgs = need(spec, 'messages', list, 1, 14)
    head, y = title_row(spec)
    n = len(actors)
    colw = (W - 2 * M) / n
    X = {a: M + colw * k + colw / 2 for k, a in enumerate(actors)}
    body = [head]
    bh = 36
    for a in actors:
        lab = wrap(a, colw - 16, FS, True, 2)
        body.append(box(X[a] - (colw - 12) / 2, y, colw - 12, bh + (len(lab) - 1) * 18, 'accent', 8))
        body.append(text_block(X[a], y + (bh + (len(lab) - 1) * 18) / 2, lab, FS, True, lh=18))
    top = y + bh + 18 * (max(len(wrap(a, colw - 16, FS, True, 2)) for a in actors) - 1)
    y = top + 30
    rows = []
    for m in msgs:
        a, b = str(m.get('from')), str(m.get('to'))
        if a not in X or b not in X: raise FigureError(f'message between unknown actors "{a}" and "{b}"')
        lab = str(m.get('label', ''))
        span = abs(X[b] - X[a]) or colw
        lines = wrap(lab, span - 14, 13, False, 2) if lab else []
        rows.append((a, b, lines, m));
    bottom = y + sum(16 * max(1, len(r[2])) + 26 for r in rows)
    for a in actors:
        body.append(f'<line x1="{X[a]:.1f}" y1="{top}" x2="{X[a]:.1f}" y2="{bottom:.1f}" style="stroke:var(--line2);stroke-width:1.5;stroke-dasharray:5 5"/>')
    for a, b, lines, m in rows:
        y += 16 * max(1, len(lines))
        st = 'dashed' if m.get('dashed') else ('live' if m.get('style') == 'live' else 'solid')
        if a == b:
            x = X[a]
            body.append(f'<path d="M{x:.1f},{y - 8:.1f} h34 v16 h-30" style="fill:none;stroke:var(--accent);stroke-width:2" marker-end="url(#ar-{uid}-n)"/>')
            if lines: body.append(text_block(x + 40, y - 18, lines, 13, False, anchor='start', lh=15))
        else:
            body.append(line(X[a], y, X[b] + (-5 if X[b] > X[a] else 5), y, uid, st, True))
            if lines: body.append(text_block((X[a] + X[b]) / 2, y - 10 - (len(lines) - 1) * 7.5, lines, 13, False, lh=15))
        y += 26
    return svg(bottom + M, ''.join(body), spec.get('aria') or 'Message sequence', uid)


RENDER = {'blocks': r_blocks, 'flow': r_blocks, 'tree': r_tree, 'graph': r_graph, 'array': r_array, 'plot': r_plot,
          'gantt': r_gantt, 'timeline': r_gantt, 'stack': r_stack, 'layers': r_stack, 'sets': r_sets, 'sequence': r_sequence}

def render(spec, uid):
    if not isinstance(spec, dict): raise FigureError('figure must be an object')
    t = spec.get('type')
    if t not in RENDER: raise FigureError(f'unknown figure type "{t}"; use one of {sorted(set(RENDER) - {"flow", "timeline", "layers"})}')
    uid = re.sub(r'[^a-z0-9-]', '', str(uid).lower())
    try:
        return RENDER[t](spec, uid)
    except FigureError:
        raise
    except (KeyError, TypeError, ValueError, IndexError, ZeroDivisionError) as e:
        raise FigureError(f'{t} figure: {type(e).__name__}: {e}')

def fallback(title, steps, uid, aria):
    """A plain chain of boxes, used only when the model's figure cannot be drawn."""
    steps = [s for s in steps if s][:5] or [title]
    nodes = [{'id': str(i), 'label': s[:60]} for i, s in enumerate(steps)]
    edges = [{'from': str(i), 'to': str(i + 1)} for i in range(len(nodes) - 1)]
    spec = {'type': 'blocks', 'direction': 'down', 'nodes': nodes, 'edges': edges, 'aria': aria}
    try:
        return render(spec, uid)
    except FigureError:
        for n in nodes: n['label'] = ' '.join(n['label'].split()[:4])
        return render(spec, uid)
