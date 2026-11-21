"""University free n easy: the fourth thumbnail (t16), one style per subject category.

Seven styles, chosen by the owner on 20 Nov 2026 from their Pinterest "banner" board:
  cubes    orange cubes pushed out of a white grid        Data Structures, Algorithms, Digital Logic, Computer Organization, Quantum
  glass    mint frosted-glass dashboard with a chart      AI, Machine Learning, Data Science, Computer Vision
  terrain  orange 3D ridges, a ball rolling to a minimum  Deep Learning, NLP
  letters  big 3D white symbol with confetti and tags     Computer Fundamentals, Web Technologies, Linux & Shell, Compiler Design
  emboss   soft raised circles joined by arrows           Theory of Computation, Networks, Cryptography, Parallel & Distributed, Blockchain, IoT
  phone    cream clay phone with raised rows              Mobile, Operating Systems, DBMS, Cloud, Computer Graphics, AR/VR
  cards    two soft cards compared, with a VS badge       Software Engineering, OOP

Usage
  python t16.py example <style>                    print an example "t16" block for that style
  python t16.py build <thumbs.json> [--only KEY] [--logo logo.png]
      For every lesson in thumbs.json that has a "t16" block, writes <lesson>_t16.jpg (1280 x 720) next to
      thumbs.json and t16_sheet.jpg (all of them, small). Prints OK, or the lessons that need fixing.

thumbs.json is the file make_thumbs.py writes: {"lessons": {"<lesson>": {"subject", "topic", "hook", ...}}}.
Add to each lesson a "t16" block with the fields of its style (see STYLE_DOC). The style comes from the subject id
(the lesson key's prefix, e.g. c-os) via STYLE_OF, or from "t16": {"style": ...} to override.
Rules: subject + topic only (no unit or lesson numbers, no college names), hook <= 40 characters and answered by
the lesson, every value in the picture true to the lesson (a DFA must be complete, a tree must really be balanced).
"""
import sys, os, json, math, html, random, base64, argparse

STYLE_OF = {
    'c-ds': 'cubes', 'c-algo': 'cubes', 'c-digital': 'cubes', 'c-coa': 'cubes', 'c-quantum': 'cubes',
    'c-ml': 'glass', 'c-data': 'glass', 'c-cv': 'glass',
    'c-dl': 'terrain', 'c-nlp': 'terrain',
    'c-fund': 'letters', 'c-web': 'letters', 'c-unix': 'letters', 'c-compiler': 'letters',
    'c-toc': 'emboss', 'c-cn': 'emboss', 'c-sec': 'emboss', 'c-dist': 'emboss', 'c-block': 'emboss', 'c-iot': 'emboss',
    'c-mobile': 'phone', 'c-os': 'phone', 'c-cloud': 'phone', 'c-graphics': 'phone', 'c-xr': 'phone',
    'c-se': 'cards', 'c-oop': 'cards',
    'ec-comm': 'glass', 'ec-optical': 'glass',
    'c-ai': 'glass', 'c-dbms': 'phone',      # on YouTube already: only the thumbnail is added, the lessons are not rebuilt
}

EXAMPLES = {
 'cubes': {"rows": 6, "cols": 6, "flat": "0", "raised": {"0,1": "7", "1,4": "3", "2,2": "9", "3,0": "5", "4,5": "8", "5,3": "2"},
           "note": "<b>6</b> of 36 cells are not zero"},
 'glass': {"title": "Error vs model size",
           "series": [{"name": "train", "y": [0.94, 0.62, 0.42, 0.30, 0.22, 0.16, 0.12, 0.10, 0.08]},
                      {"name": "test", "y": [0.98, 0.66, 0.42, 0.28, 0.22, 0.25, 0.33, 0.45, 0.62]}],
           "xlabels": ["UNDERFIT", "JUST RIGHT", "OVERFIT"], "mark": 0.5, "chip": "test error ↑"},
 'terrain': {"label": "min error"},
 'letters': {"word": "</>", "tags": ["<form>", "GET", "POST"]},
 'emboss': {"nodes": [{"name": "q0", "start": True}, {"name": "q1", "accept": True}],
            "edges": [{"from": 0, "to": 1, "label": "1"}, {"from": 1, "to": 0, "label": "0"},
                      {"from": 0, "to": 0, "label": "0"}, {"from": 1, "to": 1, "label": "1"}],
            "tape": ["1", "0", "1", "1"], "head": 3, "caption": "1011 ends in q1: <b>accepted</b>"},
 'phone': {"title": "Activity", "rows": ["onCreate()", "onStart()", "onResume()", "onPause()", "onStop()", "onDestroy()"],
           "on": 2, "tag": "running"},
 'cards': {"left": {"title": "WATERFALL", "sub": "one pass, in order", "steps": ["Plan", "Design", "Build", "Test", "Ship"]},
           "right": {"title": "AGILE", "sub": "short loops, feedback", "loop": ["Plan", "Build", "Review", "Ship"]}},
}

STYLE_DOC = {
 'cubes': 'rows, cols (each 2..6); flat = text on the flat cells ("0", "" or "."); raised = {"r,c": text} for the cells that stick out '
          '(1..12 of them, text up to 3 characters); note = one short line under the grid (may use <b>).',
 'glass': 'title (the chart, up to 24 characters); series = 1..3 lines, each {"name", "y": 2..40 values from 0 to 1} or a scatter '
          '{"name", "pts": [[x, y], ...] with x, y from 0 to 1}; xlabels = up to 3 words under the axis (left, middle, right); '
          'mark = x (0..1) of the point to circle, or null; chip = a short floating tag, or "".',
 'terrain': 'label = the tag on the ball at the lowest point (up to 14 characters), e.g. "min error", "min loss".',
 'letters': 'word = the big symbol or keyword (1..5 characters: "</>", "{ }", "$_", "int", "SQL"); tags = 1..3 small tags under it '
            '(each up to 10 characters).',
 'emboss': 'nodes = 2..4 circles in a row, each {"name" (up to 3 characters), "start"?: true, "accept"?: true}; edges = '
           '{"from", "to", "label"} by node index (forward = arc above, backward = arc below, same node = loop on top); '
           'tape = 0..6 cells shown under it; head = index of the lit cell; caption = one short line under the tape (may use <b>). '
           'A DFA must be complete; a network or protocol drawing must match the lesson.',
 'phone': 'title (up to 14 characters, the screen heading); rows = 3..6 rows (each up to 14 characters); on = index of the lit row; '
          'tag = the short tag beside the lit row, or "".',
 'cards': 'left = {"title" (up to 11 characters), "sub" (up to 24), "steps": 3..5 short words on a staircase}; '
          'right = {"title", "sub", "loop": 3..4 short words on a loop}. Use for two approaches the lesson compares.',
}

NAVY = '#1F2A44'
E = html.escape

def page(vis, subject, topic, hook, bg, logo, kick='#4C66E0', extra_css=''):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;width:1280px;height:720px;overflow:hidden;background:{bg}}}
.vis{{position:absolute;left:0;top:0;width:720px;height:720px}}
.txt{{position:absolute;left:720px;top:96px;width:510px;height:560px;display:flex;flex-direction:column;justify-content:center;align-items:flex-start}}
.kick{{font:800 21px Rubik;letter-spacing:.16em;color:{kick};margin-bottom:18px;display:flex;gap:10px;align-items:center;white-space:nowrap}}
.kick b{{font:900 22px Rubik;letter-spacing:0;background:{NAVY};color:#FFC21A;border-radius:10px;padding:2px 9px}}
h1{{margin:0;width:510px;font:900 96px/0.98 Rubik;color:#141C33;letter-spacing:-.025em}}
.hook{{margin-top:22px;font:600 28px/1.25 'Nunito Sans';color:#141C33;opacity:.78}}
.pill{{margin-top:26px;background:#FDEBC8;border:3px solid #F4C977;color:#141C33;font:800 28px Rubik;padding:10px 26px;border-radius:999px;box-shadow:0 4px 0 #F0BC5E}}
.logo{{position:absolute;right:46px;top:38px;width:104px}}
{extra_css}
</style></head><body>
<div class="vis">{vis}</div>
<img class="logo" src="{logo}">
<div class="txt"><div class="kick"><b>&lt;/&gt;</b>{E(subject)}</div><h1>{E(topic)}</h1>
<div class="hook">{E(hook)}</div><div class="pill">FREE NOTES PDF</div></div>
<script>const h=document.querySelector('h1');let f=96;
while(f>40&&(h.scrollWidth>h.clientWidth+1||h.offsetHeight>f*0.98*3+4)){{f-=2;h.style.fontSize=f+'px'}}
const k=document.querySelector('.kick');let kf=21;while(kf>14&&k.scrollWidth>510){{kf-=1;k.style.fontSize=kf+'px'}}
document.body.dataset.title=f;document.body.dataset.kick=kf;</script>
</body></html>"""

# ---------------------------------------------------------------- cubes
def r_cubes(t, L, logo):
    R, C = int(t.get('rows', 6)), int(t.get('cols', 6))
    raised = {tuple(int(v) for v in k.split(',')): str(val) for k, val in t.get('raised', {}).items()}
    flat = E(str(t.get('flat', '0')))
    D, cs = 46, 72
    cells = ''
    for r in range(R):
        for c in range(C):
            v = raised.get((r, c))
            if v is None:
                cells += f'<div class="cell"><span>{flat}</span></div>'
            else:
                fs = 34 if len(v) <= 2 else 26
                cells += (f'<div class="cell cube"><div class="f fr"><span style="font-size:{fs}px">{E(v)}</span></div><div class="f rt"></div>'
                          f'<div class="f lt"></div><div class="f tp"></div><div class="f bt"></div></div>')
    gw, gh = C * cs + (C - 1) * 10, R * cs + (R - 1) * 10
    left, top = 40 + (640 - gw) // 2 + 20, 40 + (560 - gh) // 2 + 10
    css = f""".scene{{position:absolute;left:0;top:0;width:720px;height:720px;perspective:1500px}}
.wall{{position:absolute;left:{left}px;top:{top}px;display:grid;grid-template-columns:repeat({C},{cs}px);gap:10px;transform:rotateX(14deg) rotateY(28deg) rotateZ(-2deg);transform-style:preserve-3d}}
.cell{{width:{cs}px;height:{cs}px;border-radius:14px;background:#FFFFFF;box-shadow:0 2px 0 #E3E6EC,0 8px 16px rgba(31,42,68,.08);display:flex;align-items:center;justify-content:center;position:relative;transform-style:preserve-3d}}
.cell span{{font:800 24px Rubik;color:#C9CED8}}
.cube{{background:transparent;box-shadow:none}}
.f{{position:absolute;border-radius:12px}}
.fr{{inset:0;transform:translateZ({D}px);background:linear-gradient(150deg,#FFB15A,#FF8A1F);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 2px 0 rgba(255,255,255,.5)}}
.fr span{{font-family:Rubik;font-weight:900;color:#FFFFFF}}
.rt{{left:{cs}px;top:0;width:{D}px;height:{cs}px;transform-origin:left center;transform:rotateY(-90deg);background:#D96A08}}
.lt{{left:-{D}px;top:0;width:{D}px;height:{cs}px;transform-origin:right center;transform:rotateY(90deg);background:#F07F14}}
.tp{{left:0;top:-{D}px;width:{cs}px;height:{D}px;transform-origin:center bottom;transform:rotateX(-90deg);background:#FFC07A}}
.bt{{left:0;top:{cs}px;width:{cs}px;height:{D}px;transform-origin:center top;transform:rotateX(90deg);background:#C95F05}}
.note{{position:absolute;left:70px;top:620px;font:800 22px Rubik;color:#1F2A44;background:#FFFFFF;border-radius:999px;padding:8px 20px;box-shadow:0 6px 16px rgba(31,42,68,.12);max-width:560px;white-space:nowrap}}
.note b{{color:#F07F14}}"""
    note = f'<div class="note">{t["note"]}</div>' if t.get('note') else ''
    vis = f'<div class="scene"><div class="wall">{cells}</div></div>{note}'
    return page(vis, L['subject'], L['topic'], L['hook'], 'radial-gradient(120% 100% at 30% 40%,#FFFFFF 0%,#F4F5F8 70%,#EAECF1 100%)',
                logo, kick='#E8590C', extra_css=css)

# ---------------------------------------------------------------- glass
def r_glass(t, L, logo):
    W, Hc, x0, y0 = 420, 230, 40, 40
    cols = ['#2FB380', '#FF7A59', '#5B7CFA']
    svg = ''.join(f'<line x1="{x0}" x2="{x0 + W}" y1="{y0 + k * Hc / 4}" y2="{y0 + k * Hc / 4}" stroke="#DDEFE7" stroke-width="1.5"/>' for k in range(5))
    mark = t.get('mark')
    if mark is not None:
        bx = x0 + float(mark) * W
        svg += f'<line x1="{bx}" x2="{bx}" y1="{y0}" y2="{y0 + Hc}" stroke="#7FD1AE" stroke-width="3" stroke-dasharray="4 8" stroke-linecap="round"/>'
    leg = ''
    for i, s in enumerate(t.get('series', [])[:3]):
        c = cols[i]
        leg += f'<span><i style="background:{c}"></i>{E(s["name"])}</span>'
        if 'y' in s:
            ys = s['y']; n = len(ys) - 1
            # smooth the given points with a Catmull-Rom curve
            P = [(x0 + j / n * W, y0 + Hc - max(0, min(1, v)) * Hc) for j, v in enumerate(ys)]
            d = f'M{P[0][0]:.1f},{P[0][1]:.1f}'
            for j in range(len(P) - 1):
                p0, p1, p2, p3 = P[max(0, j - 1)], P[j], P[j + 1], P[min(len(P) - 1, j + 2)]
                c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
                c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
                d += f' C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}'
            svg += f'<path d="{d}" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
            if mark is not None and i == len(t['series']) - 1:
                v = ys[min(n, round(float(mark) * n))]
                svg += f'<circle cx="{x0 + float(mark) * W}" cy="{y0 + Hc - v * Hc}" r="11" fill="#FFFFFF" stroke="#1F2A44" stroke-width="4"/>'
        else:
            for x, y in s.get('pts', []):
                svg += f'<circle cx="{x0 + x * W:.1f}" cy="{y0 + Hc - y * Hc:.1f}" r="8" fill="{c}" stroke="#FFFFFF" stroke-width="2.5"/>'
    xl = t.get('xlabels', [])
    for j, lab in enumerate(xl[:3]):
        anc, x = [('start', x0), ('middle', x0 + (float(mark) if mark is not None else .5) * W), ('end', x0 + W)][j if len(xl) == 3 else (0 if j == 0 else 2)]
        svg += f'<text x="{x}" y="{y0 + Hc + 36}" text-anchor="{anc}" font-family="Rubik" font-weight="800" font-size="18" fill="{"#1F7A57" if (j == 1 and len(xl) == 3) else "#7A8A86"}">{E(lab)}</text>'
    css = """.glass{position:absolute;left:70px;top:150px;width:540px;height:430px;border-radius:34px;background:rgba(255,255,255,.72);border:2px solid rgba(255,255,255,.9);
box-shadow:0 30px 60px rgba(30,90,70,.18),inset 0 2px 0 #FFFFFF;transform:perspective(1200px) rotateY(10deg) rotateX(6deg)}
.gh{position:absolute;left:30px;top:24px;font:900 24px Rubik;color:#1F2A44}
.leg{position:absolute;right:28px;top:26px;display:flex;gap:14px;font:800 17px Rubik;color:#1F2A44}
.leg span{display:flex;align-items:center;gap:6px}.leg i{width:22px;height:7px;border-radius:4px;display:inline-block}
.ch{position:absolute;left:20px;top:64px}
.chip{position:absolute;left:470px;top:96px;border-radius:22px;background:rgba(255,255,255,.85);box-shadow:0 16px 30px rgba(30,90,70,.16);font:800 20px Rubik;color:#1F2A44;padding:14px 18px;white-space:nowrap}
.orb{position:absolute;border-radius:50%;box-shadow:8px 14px 24px rgba(30,90,70,.18)}"""
    chip = f'<div class="chip">{E(t["chip"])}</div>' if t.get('chip') else ''
    vis = (f'<div class="orb" style="left:46px;top:70px;width:64px;height:64px;background:radial-gradient(circle at 35% 30%,#E9FFF5,#7FD1AE)"></div>'
           f'<div class="orb" style="left:600px;top:600px;width:46px;height:46px;background:radial-gradient(circle at 35% 30%,#FFF1EC,#FF9C80)"></div>'
           f'<div class="glass"><div class="gh">{E(t.get("title", ""))}</div><div class="leg">{leg}</div><svg width="500" height="330" class="ch">{svg}</svg></div>{chip}')
    return page(vis, L['subject'], L['topic'], L['hook'], 'radial-gradient(120% 100% at 30% 40%,#F4FFFA 0%,#E4F6EE 70%,#D6EFE4 100%)',
                logo, kick='#1F9D6B', extra_css=css)

# ---------------------------------------------------------------- terrain
def r_terrain(t, L, logo):
    s = ('<defs><linearGradient id="rg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF4D2E"/><stop offset=".3" stop-color="#FF9A3C"/>'
         '<stop offset=".75" stop-color="#FFE3CC" stop-opacity=".5"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>'
         '<radialGradient id="ball" cx=".35" cy=".3" r=".75"><stop offset="0" stop-color="#9FD3FF"/><stop offset=".55" stop-color="#3D8BFF"/><stop offset="1" stop-color="#1E4FC4"/></radialGradient>'
         '<filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6"/></filter></defs>')
    for i in range(13):
        q = i / 12
        s += f'<line x1="{-200 + q * 1100:.0f}" y1="690" x2="{260 + q * 300:.0f}" y2="250" stroke="#F1D9C8" stroke-width="1.5"/>'
    for j in range(9):
        y = 250 + (j / 8) ** 1.6 * 440
        s += f'<line x1="0" y1="{y:.0f}" x2="720" y2="{y:.0f}" stroke="#F1D9C8" stroke-width="1.5"/>'
    def loss(x, k):
        bowl = 0.0016 * (x - 330) ** 2
        bumps = 34 * math.exp(-((x - 150 - 20 * k) / 38) ** 2) + 26 * math.exp(-((x - 520 + 15 * k) / 44) ** 2) + 9 * math.sin(x / 23 + k * 1.7)
        win = math.sin(math.pi * (x - 30) / 640) ** .6
        return (-min(bowl, 190) - bumps) * win
    front = []
    for k in range(7):
        base, amp = 330 + k * 46, .62 + k * .07
        pts = [(x, base + loss(x, k) * amp) for x in range(30, 670, 8)]
        d = f'M30,{base + 60} ' + ' '.join(f'L{x},{y:.1f}' for x, y in pts) + f' L670,{base + 60} Z'
        s += f'<path d="{d}" fill="url(#rg)" opacity="{.45 + k * .08:.2f}"/>'
        s += '<path d="M' + ' L'.join(f'{x},{y:.1f}' for x, y in pts) + '" fill="none" stroke="#FFFFFF" stroke-width="2.5" opacity=".9"/>'
        front = pts
    lo = max(front, key=lambda p: p[1] if 260 < p[0] < 420 else -1)
    path = [p for p in front if 70 <= p[0] <= lo[0] - 30]
    for i, (x, y) in enumerate(path[::2]):
        s += f'<circle cx="{x}" cy="{y - 14:.1f}" r="{3 + i * .5:.1f}" fill="#1F2A44" opacity="{min(.95, .25 + i * .06):.2f}"/>'
    bx, by = lo
    lab = str(t.get('label', 'min error'))
    w = len(lab) * 12 + 36
    s += f'<ellipse cx="{bx}" cy="{by + 4:.1f}" rx="34" ry="9" fill="#7A2E10" opacity=".35" filter="url(#sh)"/>'
    s += f'<circle cx="{bx}" cy="{by - 30:.1f}" r="32" fill="url(#ball)"/>'
    s += (f'<g transform="translate({bx + 40},{by - 120})"><rect x="0" y="0" width="{w}" height="48" rx="24" fill="#1F2A44"/>'
          f'<text x="{w / 2}" y="32" text-anchor="middle" font-family="Rubik" font-weight="800" font-size="22" fill="#FFFFFF">{E(lab)}</text></g>')
    for (x, y, r, c) in [(80, 600, 16, '#3D8BFF'), (610, 610, 12, '#FF6B5E'), (560, 150, 10, '#FFC21A'), (110, 190, 8, '#3D8BFF')]:
        s += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'
    vis = f'<svg width="720" height="720" viewBox="0 0 720 720">{s}</svg>'
    return page(vis, L['subject'], L['topic'], L['hook'], 'radial-gradient(120% 100% at 30% 30%,#FFFFFF 0%,#FFF7F0 60%,#FDEBDD 100%)',
                logo, kick='#E8590C')

# ---------------------------------------------------------------- letters
def r_letters(t, L, logo):
    word = str(t.get('word', '</>'))
    fs = min(200, int(560 / max(1, len(word)) / .62))
    ext = ','.join(f'{i}px {i}px 0 #D3D8E1' for i in range(1, 22)) + ',26px 34px 40px rgba(31,42,68,.25)'
    conf = [(80, 120, 70, 16, -20, '#FFC21A'), (560, 90, 46, 14, 30, '#845EF7'), (120, 560, 54, 14, 15, '#20C997'),
            (600, 520, 70, 16, -35, '#FF6B5E'), (330, 600, 40, 12, 60, '#4DA3FF'), (470, 210, 30, 30, 12, '#FF6B5E'),
            (90, 330, 26, 26, -10, '#4DA3FF'), (520, 640, 28, 28, 25, '#FFC21A')]
    bits = ''.join(f'<div class="cf" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{c};transform:rotate({r}deg)"></div>' for x, y, w, h, r, c in conf)
    tags = ''.join(f'<span>{E(x)}</span>' for x in t.get('tags', [])[:3])
    css = f""".word{{position:absolute;left:70px;top:{330 - fs // 2 - 20}px;font:900 {fs}px/1 Rubik;color:#FFFFFF;letter-spacing:-.02em;text-shadow:{ext};transform:skewY(-6deg);white-space:nowrap}}
.cf{{position:absolute;border-radius:6px;box-shadow:4px 8px 14px rgba(31,42,68,.18)}}
.req{{position:absolute;left:96px;top:480px;display:flex;gap:14px}}
.req span{{font:800 24px Rubik;color:#1F2A44;background:#FFFFFF;border-radius:14px;padding:10px 18px;box-shadow:0 8px 18px rgba(31,42,68,.12);white-space:nowrap}}
.req span:first-child{{background:#1F2A44;color:#FFC21A}}"""
    vis = f'{bits}<div class="word">{E(word)}</div><div class="req">{tags}</div>'
    return page(vis, L['subject'], L['topic'], L['hook'], 'radial-gradient(120% 100% at 30% 40%,#FFFFFF 0%,#F2F4F7 70%,#E7EAF0 100%)',
                logo, kick='#7048E8', extra_css=css)

# ---------------------------------------------------------------- emboss
def r_emboss(t, L, logo):
    nodes = t.get('nodes', [])[:4]
    n = len(nodes)
    y = 330
    size = 150 if n <= 2 else (128 if n == 3 else 108)
    gapx = {2: 310, 3: 220, 4: 160}.get(n, 300)
    xs = [360 - (n - 1) * gapx / 2 + i * gapx for i in range(n)]
    xs = [x + 20 for x in xs]
    r = size / 2
    circles = ''.join(f'<div class="st{" acc" if nd.get("accept") else ""}" style="left:{x - r:.0f}px;top:{y - r:.0f}px;width:{size}px;height:{size}px;font-size:{size * .25:.0f}px">{E(nd["name"])}</div>'
                      for nd, x in zip(nodes, xs))
    def lab(x, yy, txt):
        return f'<text x="{x:.0f}" y="{yy:.0f}" text-anchor="middle" font-family="Rubik" font-weight="900" font-size="28" fill="#5B7CFA">{E(str(txt))}</text>'
    a = ('<defs><marker id="m" markerUnits="userSpaceOnUse" markerWidth="22" markerHeight="22" refX="18" refY="11" orient="auto">'
         '<path d="M2,2 L20,11 L2,20 z" fill="#2B3A5E"/></marker></defs>')
    st = 'fill="none" stroke="#2B3A5E" stroke-width="5" stroke-linecap="round" marker-end="url(#m)"'
    for i, nd in enumerate(nodes):
        if nd.get('start'):
            a += f'<line x1="{xs[i] - r - 74:.0f}" y1="{y}" x2="{xs[i] - r - 4:.0f}" y2="{y}" {st}/>'
    pairs = {(e['from'], e['to']) for e in t.get('edges', [])}
    for e in t.get('edges', []):
        f, to, tx = e['from'], e['to'], e.get('label', '')
        if f == to:
            x = xs[f]
            a += f'<path d="M{x - 30:.0f},{y - r + 4:.0f} C {x - 60:.0f},{y - r - 96:.0f} {x + 60:.0f},{y - r - 96:.0f} {x + 30:.0f},{y - r + 4:.0f}" {st}/>'
            a += lab(x, y - r - 84, tx)
        elif to > f:
            x1, x2 = xs[f] + r * .8, xs[to] - r * .8
            if (to, f) in pairs or to - f > 1:
                h = 60 + 40 * (to - f - 1)
                a += f'<path d="M{x1:.0f},{y - r * .55:.0f} C {x1 + 40:.0f},{y - r * .55 - h:.0f} {x2 - 40:.0f},{y - r * .55 - h:.0f} {x2:.0f},{y - r * .55:.0f}" {st}/>'
                a += lab((x1 + x2) / 2, y - r * .55 - h * .75 - 8, tx)
            else:
                a += f'<line x1="{xs[f] + r + 4:.0f}" y1="{y}" x2="{xs[to] - r - 4:.0f}" y2="{y}" {st}/>'
                a += lab((xs[f] + xs[to]) / 2, y - 16, tx)
        else:
            x1, x2 = xs[f] - r * .8, xs[to] + r * .8
            h = 60 + 40 * (f - to - 1)
            a += f'<path d="M{x1:.0f},{y + r * .55:.0f} C {x1 - 40:.0f},{y + r * .55 + h:.0f} {x2 + 40:.0f},{y + r * .55 + h:.0f} {x2:.0f},{y + r * .55:.0f}" {st}/>'
            a += lab((x1 + x2) / 2, y + r * .55 + h * .75 + 30, tx)
    tape = t.get('tape', [])[:6]
    head = t.get('head')
    tx0 = 360 + 20 - (len(tape) * 84 - 12) / 2
    tp = ''.join(f'<div class="{"on" if i == head else ""}">{E(str(c))}</div>' for i, c in enumerate(tape))
    css = f""".st{{position:absolute;border-radius:50%;background:#EDF1F6;box-shadow:14px 14px 30px #C9D1DC,-12px -12px 26px #FFFFFF;display:flex;align-items:center;justify-content:center;font-family:Rubik;font-weight:900;color:#2B3A5E}}
.st.acc::after{{content:'';position:absolute;inset:14px;border-radius:50%;box-shadow:inset 6px 6px 12px #C9D1DC,inset -6px -6px 12px #FFFFFF}}
.ar{{position:absolute;left:0;top:0}}
.tape{{position:absolute;left:{tx0:.0f}px;top:540px;display:flex;gap:12px}}
.tape div{{width:72px;height:72px;border-radius:18px;background:#EDF1F6;box-shadow:inset 6px 6px 12px #C9D1DC,inset -6px -6px 12px #FFFFFF;display:flex;align-items:center;justify-content:center;font:900 30px Rubik;color:#2B3A5E}}
.tape div.on{{background:#5B7CFA;color:#FFFFFF;box-shadow:6px 8px 16px rgba(91,124,250,.4)}}
.cap{{position:absolute;left:0;width:720px;text-align:center;top:632px;font:800 21px Rubik;color:#5B6B86;padding-left:40px;box-sizing:border-box}}
.cap b{{color:#2FB380}}"""
    cap = f'<div class="cap">{t["caption"]}</div>' if t.get('caption') else ''
    vis = circles + f'<svg class="ar" width="720" height="720">{a}</svg>' + (f'<div class="tape">{tp}</div>' if tape else '') + cap
    return page(vis, L['subject'], L['topic'], L['hook'], '#EDF1F6', logo, kick='#4C66E0', extra_css=css)

# ---------------------------------------------------------------- phone
def r_phone(t, L, logo):
    rows = t.get('rows', [])[:6]
    on = t.get('on')
    rh = {3: 74, 4: 66, 5: 60, 6: 56}.get(len(rows), 56)
    body = ''.join(f'<div class="row{" on" if i == on else ""}" style="height:{rh}px"><i></i>{E(x)}</div>' for i, x in enumerate(rows))
    tag_top = 56 + 18 + 58 + 36 + (on or 0) * (rh + 12) + rh // 2 - 20 if on is not None else 300
    css = """.ph{position:absolute;left:190px;top:56px;width:300px;height:600px;border-radius:56px;background:linear-gradient(160deg,#FBF7F0,#EDE4D6);
box-shadow:26px 30px 50px rgba(110,90,60,.25),-10px -10px 30px #FFFFFF,inset 0 3px 0 #FFFFFF;transform:rotate(7deg)}
.scr{position:absolute;left:18px;top:18px;right:18px;bottom:18px;border-radius:42px;background:#F4EEE4;box-shadow:inset 8px 8px 16px #DCD2C2,inset -8px -8px 16px #FFFFFF;padding:58px 22px 0;box-sizing:border-box}
.notch{position:absolute;left:110px;top:16px;width:80px;height:20px;border-radius:10px;background:#E4DACB}
.ttl{font:900 22px Rubik;color:#5A4632;margin:0 0 14px 6px}
.row{display:flex;align-items:center;gap:12px;margin-bottom:12px;border-radius:18px;background:#F4EEE4;box-shadow:6px 6px 12px #DCD2C2,-6px -6px 12px #FFFFFF;padding:0 16px;font:800 21px Rubik;color:#6B5843;white-space:nowrap;overflow:hidden}
.row i{width:14px;height:14px;border-radius:50%;background:#D8CBB8;flex:none}
.row.on{background:#7BC79A;color:#FFFFFF;box-shadow:6px 8px 16px rgba(60,140,90,.35)}.row.on i{background:#FFFFFF}
.blob{position:absolute;border-radius:50%;box-shadow:10px 14px 24px rgba(110,90,60,.2)}
.tag{position:absolute;left:470px;font:800 22px Rubik;color:#FFFFFF;background:#1F2A44;border-radius:999px;padding:10px 18px;transform:rotate(7deg);white-space:nowrap}"""
    tag = f'<div class="tag" style="top:{tag_top}px">{E(t["tag"])}</div>' if t.get('tag') and on is not None else ''
    vis = (f'<div class="blob" style="left:70px;top:120px;width:80px;height:80px;background:radial-gradient(circle at 35% 30%,#FFF4E6,#E9C29A)"></div>'
           f'<div class="blob" style="left:560px;top:540px;width:60px;height:60px;background:radial-gradient(circle at 35% 30%,#EAF7EF,#9ED3B3)"></div>'
           f'<div class="ph"><div class="notch"></div><div class="scr"><div class="ttl">{E(t.get("title", ""))}</div>{body}</div></div>{tag}')
    return page(vis, L['subject'], L['topic'], L['hook'], 'radial-gradient(120% 100% at 30% 40%,#FFFCF7 0%,#F5EEE3 70%,#ECE2D3 100%)',
                logo, kick='#B5651D', extra_css=css)

# ---------------------------------------------------------------- cards
def r_cards(t, L, logo):
    lt, rt = t.get('left', {}), t.get('right', {})
    steps = lt.get('steps', [])[:5]
    sc = ['#BFE3D0', '#A9D8C1', '#93CDB1', '#7DC2A1', '#67B791']
    stairs = ''.join(f'<div class="step" style="left:{14 + i * 30}px;top:{30 + i * 44}px;background:{sc[i]}">{E(s)}</div>' for i, s in enumerate(steps))
    loop_items = rt.get('loop', [])[:4]
    k = len(loop_items)
    angs = [-math.pi / 2 + 2 * math.pi * j / max(1, k) for j in range(k)]
    lc = ['#FFD3B6', '#FFC2A0', '#FFB08A', '#FF9F75']
    loop = ''.join(f'<div class="dot" style="left:{120 + 78 * math.cos(a) - 34:.0f}px;top:{150 + 78 * math.sin(a) - 34:.0f}px;background:{lc[j]}">{E(s)}</div>'
                   for j, (a, s) in enumerate(zip(angs, loop_items)))
    css = """.card{position:absolute;width:280px;height:380px;border-radius:40px;background:#F2F4F7;box-shadow:18px 18px 38px #CDD3DC,-14px -14px 34px #FFFFFF}
.ct{margin:30px 0 0 30px;font:900 32px Rubik;color:#26324F;letter-spacing:.02em;white-space:nowrap}
.cs{margin:4px 0 0 30px;font:600 19px 'Nunito Sans';color:#6B7488;white-space:nowrap}
.stairs,.loop{position:absolute;left:20px;top:96px;width:240px;height:270px}
.loop svg{position:absolute;left:0;top:-30px}
.step{position:absolute;width:104px;height:44px;border-radius:14px;font:800 18px Rubik;color:#1F4D3A;display:flex;align-items:center;justify-content:center;box-shadow:6px 8px 14px rgba(60,90,80,.25),inset 0 2px 0 rgba(255,255,255,.6);white-space:nowrap}
.dot{position:absolute;width:68px;height:68px;border-radius:50%;font:800 14px Rubik;color:#7A3518;display:flex;align-items:center;justify-content:center;box-shadow:6px 8px 14px rgba(150,80,40,.25),inset 0 2px 0 rgba(255,255,255,.6);margin-top:-30px;text-align:center}
.vs{position:absolute;left:320px;top:330px;width:92px;height:92px;border-radius:50%;background:#26324F;color:#FFC21A;font:900 34px Rubik;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 24px rgba(31,42,68,.35)}
.ball{position:absolute;border-radius:50%;box-shadow:10px 14px 24px rgba(31,42,68,.18)}"""
    vis = f"""<div class="ball" style="left:40px;top:70px;width:70px;height:70px;background:radial-gradient(circle at 35% 30%,#FFE9DC,#F7A98B)"></div>
<div class="ball" style="left:600px;top:560px;width:56px;height:56px;background:radial-gradient(circle at 35% 30%,#E6F7EE,#8CCFAE)"></div>
<div class="ball" style="left:590px;top:80px;width:38px;height:38px;background:radial-gradient(circle at 35% 30%,#EEE9FF,#B3A3F5)"></div>
<div class="card" style="left:60px;top:150px;transform:rotate(-5deg)"><div class="ct">{E(lt.get('title', ''))}</div><div class="cs">{E(lt.get('sub', ''))}</div><div class="stairs">{stairs}</div></div>
<div class="card" style="left:380px;top:200px;transform:rotate(4deg)"><div class="ct">{E(rt.get('title', ''))}</div><div class="cs">{E(rt.get('sub', ''))}</div><div class="loop"><svg width="240" height="300"><circle cx="120" cy="150" r="78" fill="none" stroke="#FFD8C2" stroke-width="10" stroke-dasharray="4 14" stroke-linecap="round"/></svg>{loop}</div></div>
<div class="vs">VS</div>"""
    return page(vis, L['subject'], L['topic'], L['hook'], 'radial-gradient(120% 100% at 30% 40%,#F7F8FA 0%,#ECEFF3 70%,#E3E7ED 100%)',
                logo, kick='#2F9E6E', extra_css=css)

RENDER = {'cubes': r_cubes, 'glass': r_glass, 'terrain': r_terrain, 'letters': r_letters, 'emboss': r_emboss, 'phone': r_phone, 'cards': r_cards}

def style_for(key, t):
    if t.get('style'):
        return t['style']
    sid = key.split('-u')[0]
    return STYLE_OF.get(sid)

def check_spec(key, L, style):
    p = []
    if not style:
        p.append('no style for this subject (add it to STYLE_OF or set t16.style)')
    for f in ('subject', 'topic', 'hook'):
        if not L.get(f):
            p.append(f'missing {f}')
    if len(L.get('hook', '')) > 40:
        p.append(f'hook is {len(L["hook"])} characters (max 40)')
    if any(ch.isdigit() for ch in L.get('topic', '')) and ('Unit' in L.get('topic', '') or 'Lesson' in L.get('topic', '')):
        p.append('topic carries a unit or lesson number')
    t = L.get('t16', {})
    if style == 'emboss':
        n = len(t.get('nodes', []))
        if not 2 <= n <= 4:
            p.append('emboss needs 2..4 nodes')
    if style == 'cubes' and not t.get('raised'):
        p.append('cubes needs raised cells')
    if style == 'glass' and not t.get('series'):
        p.append('glass needs at least one series')
    if style == 'phone' and not 3 <= len(t.get('rows', [])) <= 6:
        p.append('phone needs 3..6 rows')
    if style == 'cards' and not (t.get('left', {}).get('steps') and t.get('right', {}).get('loop')):
        p.append('cards needs left.steps and right.loop')
    return p

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd', choices=['build', 'example'])
    ap.add_argument('arg')
    ap.add_argument('--only')
    ap.add_argument('--logo', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logo.png'))
    a = ap.parse_args()
    if a.cmd == 'example':
        print(json.dumps(EXAMPLES[a.arg], ensure_ascii=False, indent=1))
        print('\nFields:', STYLE_DOC[a.arg])
        return
    tj = a.arg
    folder = os.path.dirname(os.path.abspath(tj))
    D = json.load(open(tj, encoding='utf-8'))
    lessons = D.get('lessons', D)
    logo = 'data:image/png;base64,' + base64.b64encode(open(a.logo, 'rb').read()).decode()
    from playwright.sync_api import sync_playwright
    problems, done = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1280, 'height': 720})
        for key, L in lessons.items():
            if key.startswith('_') or (a.only and key != a.only) or 't16' not in L:
                continue
            style = style_for(key, L['t16'])
            pr = check_spec(key, L, style)
            if pr:
                problems.append((key, pr)); continue
            htm = RENDER[style](L['t16'], L, logo)
            tmp = os.path.join(folder, f'.{key}_t16.html')
            open(tmp, 'w', encoding='utf-8').write(htm)
            pg.goto('file://' + tmp)
            pg.wait_for_timeout(250)
            tf = int(pg.evaluate('document.body.dataset.title'))
            if tf < 56:
                problems.append((key, [f'topic only fits at {tf}px; shorten it']))
            out = os.path.join(folder, f'{key}_t16.jpg')
            pg.screenshot(path=out, type='jpeg', quality=90)
            os.remove(tmp)
            done.append(out)
        b.close()
    lessons_without = [k for k in lessons if not k.startswith('_') and 't16' not in lessons[k] and (not a.only or k == a.only)]
    if done:
        from PIL import Image
        cols = 4
        rows = math.ceil(len(done) / cols)
        sheet = Image.new('RGB', (cols * 330, rows * 190), 'white')
        for i, f in enumerate(sorted(done)):
            sheet.paste(Image.open(f).resize((320, 180)), ((i % cols) * 330 + 5, (i // cols) * 190 + 5))
        sheet.save(os.path.join(folder, 't16_sheet.jpg'), quality=85)
    print(f'{len(done)} built')
    for k in lessons_without:
        problems.append((k, ['no t16 block yet']))
    for k, pr in problems:
        print('FIX', k, '; '.join(pr))
    print('OK' if not problems else f'{len(problems)} lesson(s) to fix')

if __name__ == '__main__':
    main()
