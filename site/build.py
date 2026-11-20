#!/usr/bin/env python3
"""build.py: the University Free N Easy website, as a static folder (site/dist).

usage:  python3 site/build.py            (from the repo root; standard library only)

Reads   pack/universal.json     the syllabus: subjects, topics (units) and chapters (subtopics)
        site/data/site.json     degrees shown, department names, notes address
        site/data/lessons.json  the lessons of each topic, with YouTube ids
Writes  site/dist/              home, degree, department, subject and lesson pages, search, sitemap

Mapping: degree -> department -> subject -> topic -> lesson.
Rules the build enforces on every page (it stops if one is broken): no college name, no unit number,
no lesson number. Topics and lessons are shown by name only; the numbers appear only inside the
notes PDF file names, which must never change.
"""
import html, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
OUT = os.path.join(HERE, 'dist')
sys.path.insert(0, os.path.join(HERE, 'vendor'))
import make_site as ms   # the data pack's site script: chapter helpers and the college-name pattern

E = html.escape
BRAND = 'University Free N Easy'
ICONS = {
    'tech': 'M8 3v3m4-3v3m4-3v3M8 18v3m4-3v3m4-3v3M3 8h3m-3 4h3m-3 4h3m12-8h3m-3 4h3m-3 4h3M6 6h12v12H6z M9 9h6v6H9z',
    'med': 'M3 4v4a5 5 0 0 0 10 0V4M3 4h2m6 0h2M8 13v2a6 6 0 0 0 12 0v-3m0 0a2 2 0 1 0 0-4 2 2 0 0 0 0 4',
    'book': 'M3 5q5-2 9 1 4-3 9-1v13q-5-2-9 1-4-3-9-1z M12 6v13',
}
PLAY = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="#254C40"><path d="M8 5v14l11-7z"/></svg>'
DOWN = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M4 21h16"/></svg>'
TICK = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&amp;family=DM+Sans:wght@400;500;600;700&amp;display=swap">')


def read(p):
    with open(p, encoding='utf8') as f:
        return f.read()


def slug(s):
    s = re.sub(r'[^a-z0-9]+', '-', s.lower().replace('&', ' and ').replace('+', ' plus ').replace('#', ' sharp '))
    return s.strip('-')


CFG = json.loads(read(os.path.join(HERE, 'data', 'site.json')))
LES = json.loads(read(os.path.join(HERE, 'data', 'lessons.json')))
U = json.loads(read(os.path.join(REPO, 'pack', 'universal.json')))
DEPT = CFG['departments']
SITE = CFG.get('site_url', '').rstrip('/')
PAGES = []          # (url path, html) of every page written, for the sitemap and the rule check


# ---------- the syllabus as the site sees it ----------
def build_model():
    subs = {}
    for s in U['subjects']:
        if s.get('scope') != 'btech' or s['dept'] not in DEPT:
            continue
        d = DEPT[s['dept']]
        sub = {'id': s['id'], 'name': s['name'], 'aka': s.get('aka', []), 'dept': s['dept'], 'sem': s.get('usual_sem') or 99,
               'url': '/btech/%s/%s/' % (d['slug'], slug(s['name'])), 'topics': [], 'lessons': []}
        for u in s['units']:
            key = '%s-u%s' % (s['id'], u['n'])
            chapters = [('%s.%d' % (u['n'], i), st['t'], st.get('match', [])) for i, st in enumerate(u['subtopics'], 1)]
            topic = {'name': u['name'], 'key': key, 'chapters': chapters, 'lessons': []}
            for l in LES.get(key, {}).get('lessons', []):
                les = {'id': '%s-L%s' % (key, l['n']), 'title': l['title'], 'video': l.get('video', ''), 'minutes': l.get('minutes') or 0,
                       'topic': topic, 'sub': sub, 'covers': [t for num, t, _ in chapters if ms.covers(l.get('chapters', ''), num)],
                       'notes': ('%s/%s-L%s.pdf' % (CFG['notes_base'], key, l['n'])) if l.get('notes', True) else ''}
                topic['lessons'].append(les)
                sub['lessons'].append(les)
            sub['topics'].append(topic)
        used = set()
        for les in sub['lessons']:
            sl = slug(les['title'])
            while sl in used:
                sl += '-2'
            used.add(sl)
            les['url'] = sub['url'] + sl + '/'
        subs[s['id']] = sub
    return subs


SUBS = build_model()
BY_DEPT = {}
for _s in SUBS.values():
    BY_DEPT.setdefault(_s['dept'], []).append(_s)
for _d in BY_DEPT.values():
    _d.sort(key=lambda x: (0 if x['lessons'] else 1, x['sem'], x['name']))
ALL_LESSONS = [l for d in CFG['degrees'][0]['departments'] for s in BY_DEPT.get(d, []) for l in s['lessons']]


def dept_url(d):
    return '/btech/%s/' % DEPT[d]['slug']


def dept_live(d):
    return any(s['lessons'] for s in BY_DEPT.get(d, []))


# ---------- page shell ----------
def shell(path, title, desc, band, body, crumbs=(), extra_head='', scripts=('/assets/site.js',)):
    canon = '<link rel="canonical" href="%s%s">' % (SITE, path) if SITE else ''
    og = ('<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:type" content="website">'
          '<meta property="og:site_name" content="%s">' % (E(title), E(desc), BRAND))
    crumb = ''
    if crumbs:
        crumb = '<nav class="crumb" aria-label="Breadcrumb">' + ' <span aria-hidden="true">/</span> '.join('<a href="%s">%s</a>' % (u, E(n)) for n, u in crumbs) + '</nav>'
    page = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title><meta name="description" content="%s"><meta name="theme-color" content="#18382f">%s%s
<link rel="icon" href="/assets/favicon.png">%s<link rel="stylesheet" href="/assets/site.css">%s</head>
<body><a class="skip" href="#main">Skip to the content</a>
<div class="band"><div class="wrap">
<header class="pill"><a class="brand" href="/"><img src="/assets/logo.png" alt="" width="56" height="44"><span><b>University</b><small>FREE N EASY</small></span></a>
<nav aria-label="Main"><a href="/#degrees">Degree directory</a><a href="/#how">How it works</a><a href="/search/">Search</a></nav>
<span style="display:flex;gap:8px"><a class="btn ghost" href="%s" rel="noopener">YouTube</a><a class="btn gold" href="/#degrees">Start learning</a></span></header>
%s%s</div></div>
<main id="main"><div class="wrap">
%s
</div></main>
<footer class="site"><div class="wrap"><div><b>%s <span style="color:#D2E0D7">Learning campus</span></b><p>Free lessons and notes for university students. No ads. Lessons and notes need no sign-up.</p></div>
<nav aria-label="Footer"><a href="/#degrees">Degree directory</a><a href="/about/">About</a><a href="/privacy/">Privacy</a><a href="%s" rel="noopener">YouTube channel</a></nav></div></footer>
%s</body></html>
''' % (E(title), E(desc), canon, og, FONTS, extra_head, CFG['channel'], crumb, band, body, BRAND, CFG['channel'],
       ''.join('<script src="%s" defer></script>' % s for s in scripts))
    write(path, page)


def write(path, page):
    fp = os.path.join(OUT, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(OUT, path.strip('/'))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, 'w', encoding='utf8') as f:
        f.write(page)
    if fp.endswith('.html'):
        PAGES.append((path, page))


def card(url, name, small, tag='', live=False):
    return ('<a class="card" href="%s"><span class="more" aria-hidden="true">+</span><b>%s</b><small>%s</small>%s</a>'
            % (url, E(name), E(small), '<span class="tag%s">%s</span>' % (' live' if live else '', E(tag)) if tag else ''))


def plural(n, word):
    return '%d %s%s' % (n, word, '' if n == 1 else 's')


# ---------- degree and department pages ----------
def degree_pages():
    for deg in CFG['degrees']:
        url = '/%s/' % deg['id']
        base = next(x for x in CFG['degrees'] if x['id'] == deg.get('same_as', deg['id']))
        if 'departments' in base:
            cards = ''.join(card(dept_url(d), DEPT[d]['name'], DEPT[d]['sub'] or plural(len(BY_DEPT.get(d, [])), 'subject'),
                                 'Lessons live' if dept_live(d) else 'Coming soon', dept_live(d)) for d in base['departments'])
            note = '<p class="muted" style="margin-bottom:16px">B.E. students study the same subjects as B.Tech, so these pages serve both.</p>' if deg.get('same_as') else ''
            body = '<section><div class="headrow"><h2>Departments</h2></div>%s<div class="grid">%s</div></section>' % (note, cards)
            lede = 'Pick your department, then your subject. Lessons and notes are free.'
        else:
            body = ('<section><div class="headrow"><h2>Courses planned</h2><span class="tag">Coming soon</span></div><ul class="soonlist">%s</ul></section>'
                    '<section class="prose"><h2>Not ready yet</h2><p>Lessons and notes for %s are being planned. Nothing to pay and nothing to sign up for when they arrive.</p>'
                    '<p><a class="btn green" href="%s" rel="noopener">Subscribe on YouTube to see them first</a></p><p class="muted">Subscribing is optional.</p></section>'
                    % (''.join('<li>%s</li>' % E(c) for c in deg['courses']), E(deg['name']), CFG['channel']))
            lede = 'Coming soon. Here is what is planned.'
        band = '<p class="kicker">DEGREE DIRECTORY</p><h1>%s</h1><p class="lede">%s</p>' % (E(deg['name']), lede)
        shell(url, '%s lessons and notes | %s' % (deg['name'], BRAND),
              'Free video lessons and notes for %s students: %s. Pick your department and subject.' % (deg['name'], deg['desc']), band, body, [('Degrees', '/#degrees')])


def department_pages():
    for d, info in DEPT.items():
        subs = BY_DEPT.get(d, [])
        live = [s for s in subs if s['lessons']]
        cards = ''.join(card(s['url'], s['name'], plural(len(s['topics']), 'topic'),
                             plural(len(s['lessons']), 'lesson') if s['lessons'] else 'Coming soon', bool(s['lessons'])) for s in subs)
        lede = ('%s, %s with lessons so far.' % (plural(len(subs), 'subject'), len(live))) if live else 'Lessons for this department are being made. These are the subjects planned.'
        band = '<p class="kicker">B.TECH</p><h1>%s</h1><p class="lede">%s</p>' % (E(info['name']), lede)
        body = '<section><div class="headrow"><h2>Subjects</h2></div><div class="grid">%s</div></section>' % cards
        shell(dept_url(d), 'B.Tech %s: free lessons and notes | %s' % (info['name'], BRAND),
              'Free video lessons and notes PDFs for B.Tech %s subjects: %s and more.' % (info['name'], ', '.join(s['name'] for s in subs[:4])),
              band, body, [('B.Tech', '/btech/')])


# ---------- subject and lesson pages ----------
def lesson_row(l):
    meta = ('%s min' % l['minutes']) if l['minutes'] else ('Video lesson' if l['video'] else 'Video coming')
    return ('<a class="row" href="%s" data-done-id="%s"><span class="rowmain"><span class="play">%s</span><span><strong>%s</strong><small>%s</small></span></span>'
            '<span class="tag">Open</span></a>' % (l['url'], l['id'], PLAY, E(l['title']), meta))


def subject_pages():
    for s in SUBS.values():
        d = DEPT[s['dept']]
        crumbs = [('B.Tech', '/btech/'), (d['name'], dept_url(s['dept']))]
        topics = ''
        for t in s['topics']:
            rows = ''.join(lesson_row(l) for l in t['lessons'])
            chapters = ''.join('<li>%s</li>' % E(c[1]) for c in t['chapters'])
            topics += ('<div class="topic" id="%s"><h3>%s</h3><p class="count">%s</p>%s<ul class="chapters">%s</ul>'
                       '<div class="book"><span><strong>Full topic book</strong><small>Every chapter of this topic with solved long answers, in one PDF.</small></span><span class="tag">Coming soon</span></div></div>'
                       % (slug(t['name']), E(t['name']), plural(len(t['lessons']), 'lesson') if t['lessons'] else 'Lessons coming soon',
                          '<div class="rows">%s</div>' % rows if rows else '', chapters))
        n = len(s['lessons'])
        if n:
            lede = '%s, %s. Every lesson comes with notes.' % (plural(len(s['topics']), 'topic'), plural(n, 'lesson'))
            actions = ('<div class="actions"><a class="btn gold" href="%s">Start with the first lesson</a></div>'
                       '<div class="progress" data-progress="%s"><b><i></i></b><span></span></div>' % (s['lessons'][0]['url'], ' '.join(l['id'] for l in s['lessons'])))
        else:
            lede = 'Lessons for this subject are being made. These are the topics and chapters it will cover.'
            actions = '<div class="actions"><a class="btn light" href="%s" rel="noopener">Subscribe on YouTube to see them first</a></div>' % CFG['channel']
        band = '<p class="kicker">%s</p><h1>%s</h1><p class="lede">%s</p>%s' % (E(d['name'].upper()), E(s['name']), lede, actions)
        body = '<section><div class="headrow"><h2>Topics</h2></div>%s</section>' % topics
        desc = 'Free video lessons and notes PDFs for %s (B.Tech %s): %s.' % (s['name'], d['name'], ', '.join(t['name'] for t in s['topics'][:4]))
        shell(s['url'], '%s: free lessons and notes | %s' % (s['name'], BRAND), desc, band, body, crumbs)
        for i, l in enumerate(s['lessons']):
            lesson_page(s, l, s['lessons'][i - 1] if i else None, s['lessons'][i + 1] if i + 1 < n else None, crumbs + [(s['name'], s['url'])])


def lesson_page(s, l, prev, nxt, crumbs):
    t = l['topic']
    if l['video']:
        player = ('<div class="player" data-video="%s" data-title="%s"><img src="https://i.ytimg.com/vi/%s/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">'
                  '<button type="button" aria-label="Play the lesson: %s"><svg aria-hidden="true" viewBox="0 0 24 24" fill="#203C30"><path d="M8 5v14l11-7z"/></svg></button>'
                  '<span class="note">The video loads when you press play</span></div>' % (E(l['video']), E(l['title']), E(l['video']), E(l['title'])))
        yt = '<a class="btn" href="https://www.youtube.com/watch?v=%s" rel="noopener">Watch on YouTube</a>' % E(l['video'])
    else:
        player = '<div class="player soon">The video for this lesson is on its way.</div>'
        yt = ''
    notes_btn = '<a class="btn green" href="%s">%sNotes PDF, free</a>' % (l['notes'], DOWN) if l['notes'] else ''
    syl = '<strong>%s</strong>' % E(s['name'])
    for tt in s['topics']:
        if tt['lessons']:
            syl += '<div class="group">%s</div>' % E(tt['name']) + ''.join(
                '<a href="%s" data-done-id="%s"%s>%s</a>' % (x['url'], x['id'], ' class="active" aria-current="page"' if x is l else '', E(x['title'])) for x in tt['lessons'])
    res = ''
    if l['notes']:
        res += ('<div class="resource"><strong>Revision notes</strong><small>The figures, worked examples and exam traps of this lesson in one PDF. Free, no sign-up.</small>'
                '<a class="btn green" href="%s">%sDownload the PDF</a></div>' % (l['notes'], DOWN))
    if l['covers']:
        res += '<div class="resource"><strong>In this lesson</strong><small>%s</small></div>' % '<br>'.join(E(c) for c in l['covers'])
    if nxt:
        res += '<div class="resource"><strong>Related study</strong><small>Continue with the next lesson: %s.</small><a class="btn" href="%s">Open it</a></div>' % (E(nxt['title']), nxt['url'])
    res += '<div class="resource"><strong>Full topic book</strong><small>Every chapter of this topic with solved long answers, in one PDF.</small><span class="tag">Coming soon</span></div>'
    pager = '<nav class="pager" aria-label="Lesson order">%s%s</nav>' % (
        '<a class="btn" href="%s"><span>Back: %s</span></a>' % ((prev['url'], E(prev['title'])) if prev else (s['url'], E(s['name']))),
        '<a class="btn gold" href="%s"><span>Next: %s</span></a>' % (nxt['url'], E(nxt['title'])) if nxt else '<a class="btn gold" href="%s"><span>All topics</span></a>' % s['url'])
    band = '<p class="kicker">%s</p><h1>%s</h1>' % (E(t['name'].upper()), E(l['title']))
    body = ('<section class="watch"><div>%s<div class="controls">%s<button type="button" class="btn" data-done-id="%s" aria-pressed="false">%s<span>Mark as done</span></button>%s</div></div>'
            '<aside class="syllabus" aria-label="Lessons in this subject">%s</aside></section>'
            '<section><p class="kicker dark">STUDY THIS TOPIC</p><div class="headrow"><h2>Notes and next steps</h2></div><div class="resources">%s</div>%s</section>'
            % (player, notes_btn, l['id'], TICK, yt, syl, res, pager))
    covers = (' It covers ' + ', '.join(l['covers'][:3]) + '.') if l['covers'] else ''
    ld = ''
    if l['video']:
        ld = '<script type="application/ld+json">%s</script>' % json.dumps({
            '@context': 'https://schema.org', '@type': 'LearningResource', 'name': l['title'], 'learningResourceType': 'Video lesson',
            'isAccessibleForFree': True, 'about': s['name'], 'provider': {'@type': 'Organization', 'name': BRAND}}).replace('</', '<\\/')
    shell(l['url'], '%s | %s notes and video lesson | %s' % (l['title'], s['name'], BRAND),
          'Free video lesson and notes PDF: %s (%s, %s).%s' % (l['title'], s['name'], t['name'], covers), band, body, crumbs, extra_head=ld)


# ---------- home ----------
def directory_html():
    cards, lists = '', ''
    tints = [('#E2EDDF', '#BDCABE'), ('#E2EBF2', '#C5D4DD'), ('#F6E9D7', '#DED0BA'), ('#ECE5F1', '#D5CCDE')]
    row = ('<a href="%s" style="display: flex; align-items: center; justify-content: space-between; gap: 12px; min-height: 56px; border-top: 1px solid rgba(244,246,233,0.3); color: #F9FAF6; '
           'text-decoration: none; font-family: \'Instrument Serif\', Georgia, serif; font-size: 25px"><span>%s</span>%s</a>')
    open_tag = '<span style="font-family: \'DM Sans\', sans-serif; font-weight: 700; font-size: 14px; color: #203C30; background: #E9CE83; border-radius: 13px; padding: 3px 12px">Open</span>'
    soon_tag = '<span style="font-family: \'DM Sans\', sans-serif; font-size: 14px; color: #A7B8AB">Coming soon</span>'
    for i, deg in enumerate(CFG['degrees']):
        base = next(x for x in CFG['degrees'] if x['id'] == deg.get('same_as', deg['id']))
        live = 'departments' in base
        cards += ('<button type="button" data-degree="%s courses" aria-pressed="false" style="position: relative; display: flex; flex-direction: column; align-items: flex-start; text-align: left; gap: 10px; min-height: 190px; '
                  'padding: 22px 22px 18px; border-radius: 12px; border: 1px solid %s; background: %s; color: #182E27; font: inherit; cursor: pointer; transition: box-shadow 0.25s">'
                  '<span style="width: 44px; height: 44px; border-radius: 9px; border: 1px solid #A7B8AB; background: rgba(255,255,255,0.35); display: flex; align-items: center; justify-content: center">'
                  '<svg aria-hidden="true" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#182E27" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="%s"/></svg></span>'
                  '<span aria-hidden="true" style="position: absolute; right: 16px; top: 12px; font-size: 22px; color: #5B695F">+</span>'
                  '<span style="font-family: \'Instrument Serif\', Georgia, serif; font-size: 54px; line-height: 1.05; letter-spacing: -0.03em">%s</span>'
                  '<span style="font-size: 15px; color: #47584F">%s</span>'
                  '<span style="margin-top: auto; font-size: 14px; font-weight: 700; %s; border-radius: 13px; padding: 3px 12px">%s</span></button>\n'
                  % (E(deg['name']), tints[i % 4][1], tints[i % 4][0], ICONS[deg['icon']], E(deg['name']), E(deg['desc']),
                     'color: #203C30; background: #E9CE83' if live else 'color: #47584F; background: rgba(255,255,255,0.55)', 'Lessons live' if live else 'Coming soon'))
        if live:
            rows = ''.join(row % (dept_url(d), E(DEPT[d]['name']), open_tag if dept_live(d) else soon_tag) for d in base['departments'])
        else:
            rows = ''.join(row % ('/%s/' % deg['id'], E(c), soon_tag) for c in deg['courses'])
        lists += ('<div data-degree-list%s style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(340px, 100%%), 1fr)); gap: 0 44px">%s'
                  '<a href="/%s/" style="grid-column: 1 / -1; margin-top: 18px; color: #F4D884; font-weight: 600">Open the %s page</a></div>\n'
                  % ('' if i == 0 else ' hidden', rows, deg['id'], E(deg['name'])))
    arrow = ('<button type="button" id="%s" aria-label="%s" style="width: 52px; height: 52px; border-radius: 26px; border: 1.5px solid #F9FAF6; background: transparent; color: #F9FAF6; display: flex; '
             'align-items: center; justify-content: center; cursor: pointer"><svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.4" '
             'stroke-linecap="round" stroke-linejoin="round"><path d="%s"/></svg></button>')
    return ('''<section id="degrees" class="ufe-scene" data-nav="dark" style="position: relative; overflow: hidden; background: #13261E; color: #F9FAF6">
<canvas id="ufe-globe" aria-hidden="true" width="900" height="900" style="position: absolute; right: -240px; top: -80px; width: 900px; height: 900px; opacity: 0.7; pointer-events: none"></canvas>
<div style="position: relative; max-width: 1240px; margin: 0 auto; padding: 120px 24px 130px; display: flex; flex-direction: column; gap: 32px">
<div class="ufe-rise" style="display: flex; flex-direction: column; gap: 14px; opacity: var(--v, 1); transform: translateY(calc((1 - var(--v, 1)) * 48px))">
<span style="display: flex; align-items: center; gap: 9px; font-size: 13px; font-weight: 700; letter-spacing: 0.15em; color: #DFDFB4"><span aria-hidden="true" style="width: 24px; height: 2px; background: #DEBA65"></span>DEGREE DIRECTORY</span>
<h2 style="margin: 0; max-width: 820px; font-family: 'Instrument Serif', Georgia, serif; font-weight: 400; font-size: clamp(42px, 5.2vw, 76px); line-height: 1.02; letter-spacing: -0.03em; color: #F9FAF6">Explore by degree, <span style="color: #D2E0D7">then department, then subject.</span></h2>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(250px, 100%), 1fr)); gap: 14px">
''' + cards + '''</div>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 16px 28px; margin-top: 8px">
<div style="display: flex; gap: 10px">''' + arrow % ('ufe-degree-prev', 'Previous degree', 'm15 6-6 6 6 6') + arrow % ('ufe-degree-next', 'Next degree', 'm9 6 6 6-6 6') + '''</div>
<span id="ufe-degree-title" style="font-family: 'Instrument Serif', Georgia, serif; font-size: clamp(34px, 3.8vw, 54px); line-height: 1.05; color: #F4D884">''' + E(CFG['degrees'][0]['name']) + ''' courses</span>
</div>
''' + lists + '''</div>
</section>''')


def home():
    tpl = read(os.path.join(HERE, 'templates', 'home.html'))
    kf = read(os.path.join(HERE, 'templates', 'home.keyframes.css'))
    live_subs = [s for s in SUBS.values() if s['lessons']]
    mins = [l['minutes'] for l in ALL_LESSONS if l['minutes']]
    depts = CFG['degrees'][0]['departments']
    live_d = sum(1 for d in depts if dept_live(d))
    ring = '<circle cx="24" cy="24" r="21" stroke-dasharray="6 5"></circle><circle cx="24" cy="24" r="13"></circle><circle cx="24" cy="24" r="5"></circle>'
    stat = ('<span style="flex: 0 0 auto; display: flex; align-items: center; gap: 16px; padding-right: 88px"><svg aria-hidden="true" class="ufe-m" viewBox="0 0 48 48" width="48" height="48" fill="none" stroke="#FFFFFF" '
            'stroke-width="1.4" style="animation: ufeOrbit 14s linear infinite">' + ring + '</svg><span style="display: flex; flex-direction: column; line-height: 1.15">'
            '<span style="font-family: \'Instrument Serif\', Georgia, serif; font-size: 38px; white-space: nowrap">%s</span><span style="font-size: 16px; white-space: nowrap">%s</span></span></span>')
    stats = ''.join(stat % x for x in [
        (len(ALL_LESSONS), 'lessons with notes'), ('~%d min' % round(sum(mins) / len(mins)) if mins else 'Short', 'per lesson'),
        (len(live_subs), 'subjects with lessons'), (sum(len(BY_DEPT.get(d, [])) for d in depts), 'subjects mapped'),
        (live_d, 'departments live'), (len(depts) - live_d, 'departments coming'), ('₹0', 'no fees, no ads')])
    feat = [l for l in ALL_LESSONS if l['video']][:3]
    featured = ''.join(
        '<a href="%s" style="display: flex; align-items: center; gap: 12px; padding: 16px; border-radius: 12px; background: #FFFFFF; border: 1px solid #D4DCD2; color: #182E27; text-decoration: none">'
        '<span aria-hidden="true" style="flex: 0 0 40px; height: 40px; border-radius: 20px; background: #E6EEE5; display: flex; align-items: center; justify-content: center">'
        '<svg viewBox="0 0 24 24" width="16" height="16" fill="#254C40"><path d="M8 5v14l11-7z"/></svg></span><span style="display: flex; flex-direction: column"><span style="font-weight: 700; line-height: 1.3">%s</span>'
        '<span style="font-size: 14px; color: #55695E">%s · B.Tech</span></span></a>' % (l['url'], E(l['title']), E(l['sub']['name'])) for l in feat)
    body = (tpl.replace('<!--DIRECTORY-->', directory_html()).replace('<!--STATS-->', stats).replace('<!--FEATURED-->', featured)
            .replace('{{SAMPLE_LESSON}}', feat[0]['url'] if feat else '/#degrees')
            .replace('{{CS_MORE}}', str(max(0, len(BY_DEPT.get('cse', [])) - 4))).replace('{{BIO_MORE}}', str(max(0, len(BY_DEPT.get('bio', [])) - 3))))
    title = '%s: free video lessons and notes for university students' % BRAND
    desc = 'Free short video lessons with notes PDFs for B.Tech subjects. Find your degree, department and subject. No sign-up, no ads.'
    canon = '<link rel="canonical" href="%s/">' % SITE if SITE else ''
    page = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">\n<title>%s</title>'
            '<meta name="description" content="%s"><meta name="theme-color" content="#18382f">%s<meta property="og:title" content="%s"><meta property="og:description" content="%s">'
            '<link rel="icon" href="/assets/favicon.png">%s<link rel="stylesheet" href="/assets/site.css"><style>%s</style></head>\n<body>\n%s\n'
            '<script src="/assets/home.js" defer></script></body></html>\n' % (E(title), E(desc), canon, E(title), E(desc), FONTS, kf, body))
    write('/', page)


# ---------- small pages, search, sitemap ----------
def small_pages():
    shell('/search/', 'Search subjects and topics | %s' % BRAND, 'Search every subject, topic and lesson on %s.' % BRAND,
          '<p class="kicker">SEARCH</p><h1>Find your <em>subject or topic</em></h1>',
          '<section><div class="searchbox"><input id="q" type="search" aria-label="Search a subject or topic" placeholder="Search a subject or topic" autocomplete="off" autofocus></div><div id="results" aria-live="polite"></div></section>')
    shell('/about/', 'About | %s' % BRAND, 'What %s is: free short video lessons and notes for university students.' % BRAND,
          '<p class="kicker">ABOUT</p><h1>Free lessons, <em>free notes</em></h1>',
          '<section class="prose"><p>%s makes short video lessons for university subjects. Every lesson has a notes PDF with the figures, worked examples and exam traps.</p>'
          '<p>Lessons and notes are free and need no sign-up. There are no ads on this site.</p><h2>How to use it</h2><p>Pick your degree, then your department and subject. Each subject lists its topics in order; '
          'each topic lists its lessons. Watch the lesson, read or download the notes, then move to the next one.</p><h2>Found a mistake?</h2><p>Say so in the comments under the video on YouTube and it gets fixed in the next version.</p></section>' % BRAND)
    shell('/privacy/', 'Privacy | %s' % BRAND, 'What this site collects: nothing. No accounts, no tracking, no ads.',
          '<p class="kicker">PRIVACY</p><h1>Privacy</h1>',
          '<section class="prose"><p>This site has no accounts and collects no personal data. It sets no advertising or tracking cookies.</p>'
          '<h2>Mark as done</h2><p>When you tick a lesson as done, that tick is saved in your own browser on your own device. It is never sent to us. Clearing your browser data removes it.</p>'
          '<h2>Videos</h2><p>Lesson videos are hosted by YouTube. A lesson page shows the video\'s still picture from YouTube\'s image server. The player itself loads only when you press play; after that, YouTube\'s own privacy policy applies to it.</p>'
          '<h2>Fonts</h2><p>The page fonts are loaded from Google Fonts.</p></section>')
    nf = [(p, h) for p, h in PAGES if p == '/about/'][0][1]
    nf = nf.replace('<title>About | %s</title>' % BRAND, '<title>Page not found | %s</title>' % BRAND)
    nf = re.sub(r'<main id="main">.*?</main>', '<main id="main"><div class="wrap"><section class="prose"><h2>That page is not here</h2><p>It may have moved. Try the search or the degree directory.</p>'
                '<p><a class="btn green" href="/search/">Search</a> <a class="btn" href="/#degrees">Degree directory</a></p></section></div></main>', nf, flags=re.S)
    nf = re.sub(r'<p class="kicker">ABOUT</p><h1>.*?</h1>', '<p class="kicker">NOT FOUND</p><h1>Page not found</h1>', nf, flags=re.S)
    with open(os.path.join(OUT, '404.html'), 'w', encoding='utf8') as f:
        f.write(nf)


def search_index():
    subjects, items = [], []
    for s in sorted(SUBS.values(), key=lambda x: x['name']):
        si = len(subjects)
        subjects.append([s['name'], s['url'], ' | '.join(a.lower() for a in s['aka'])])
        for t in s['topics']:
            for num, title, match in t['chapters']:
                les = next((l for l in t['lessons'] if title in l['covers']), None)
                m = ' | '.join(x.lower() for x in match if x.lower() not in title.lower())
                items.append([si, t['name'], title, m, les['url'] if les else ''])
            for l in t['lessons']:
                items.append([si, t['name'], l['title'], '', l['url']])
    with open(os.path.join(OUT, 'search.json'), 'w', encoding='utf8') as f:
        json.dump({'subjects': subjects, 'items': items}, f, ensure_ascii=False, separators=(',', ':'))
    return len(items)


def check_rules():
    """Stop the build if a page shows a college name, a unit number or a lesson number."""
    bad = []
    for path, page in PAGES:
        text = re.sub(r'<(script|style)\b.*?</\1>', ' ', page, flags=re.S)
        for chunk in re.split(r'<[^>]+>', text):          # one piece of visible text at a time
            chunk = html.unescape(chunk)
            for name, pat in (('college name', ms.COLLEGE), ('unit number', re.compile(r'\bUnit\s+\d', re.I)), ('lesson number', re.compile(r'\bLesson\s+\d', re.I))):
                m = pat.search(chunk)
                if m:
                    bad.append('%s: %s "%s"' % (path, name, chunk[max(0, m.start() - 30):m.end() + 20].strip()))
    if bad:
        print('RULE CHECK FAILED on %d page(s):' % len(bad))
        for b in bad[:25]:
            print('  ', b)
        sys.exit(1)


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT)
    shutil.copytree(os.path.join(HERE, 'assets'), os.path.join(OUT, 'assets'))
    home()
    degree_pages()
    department_pages()
    subject_pages()
    small_pages()
    n_items = search_index()
    with open(os.path.join(OUT, 'robots.txt'), 'w') as f:
        f.write('User-agent: *\nAllow: /\n' + ('Sitemap: %s/sitemap.xml\n' % SITE if SITE else ''))
    if SITE:
        with open(os.path.join(OUT, 'sitemap.xml'), 'w') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                    + ''.join('<url><loc>%s%s</loc></url>\n' % (SITE, p) for p, _ in PAGES) + '</urlset>\n')
    with open(os.path.join(OUT, '_headers'), 'w') as f:
        f.write('/assets/*\n  Cache-Control: public, max-age=604800\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n')
    check_rules()
    print('built %d pages: %d subjects, %d lessons, %d search entries -> %s' % (len(PAGES), len(SUBS), len(ALL_LESSONS), n_items, os.path.relpath(OUT, REPO)))


if __name__ == '__main__':
    main()
