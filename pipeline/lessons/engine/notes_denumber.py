"""Run make_site.py --pdf-only with chapter and figure numbers taken out of the lesson notes (coordinator ruling 21 Nov 2026:
chapter numbers like 3.1 reveal the unit). Chapter numbers become chapter titles, figure numbers count from 1 in each file.
usage: python3 notes_denumber.py <make_site.py> <make_site args...>"""
import importlib.util, os, re, sys, html as H
spec = importlib.util.spec_from_file_location('make_site', sys.argv[1]); ms = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[1]] + sys.argv[2:]; spec.loader.exec_module(ms)
orig = ms.cut_lesson_notes
NUM = r'\d+\.\d+'

def visible(htm, fn):
    out, pos = [], 0
    for m in re.finditer(r'<(script|style)\b.*?</\1>|<[^>]+>', htm, flags=re.S):
        out.append(fn(htm[pos:m.start()])); out.append(m.group(0)); pos = m.end()
    out.append(fn(htm[pos:])); return ''.join(out)

def denumber(book, cut):
    titles = {m.group(1): H.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
              for m in re.finditer(r'<h2>\s*<span class="num">(' + NUM + r')</span>\s*(.*?)</h2>', book, flags=re.S)}
    keys = sorted(titles, key=lambda x: tuple(int(p) for p in x.split('.')))
    def rng(a, b):
        ia, ib = keys.index(a), keys.index(b); return keys[ia:ib + 1]
    def q(k): return '“' + H.escape(titles.get(k, k), quote=False) + '”'
    def names(ks):
        ks = [q(k) for k in ks]
        return ks[0] if len(ks) == 1 else ', '.join(ks[:-1]) + ' and ' + ks[-1]
    cut = re.sub(r'<span class="num">' + NUM + r'</span>\s*', '', cut)
    cut = re.sub(r'<span class="chip">Chapters? ' + NUM + r'(?: to ' + NUM + r')?</span>', '', cut)
    figs = []
    def fig(m):
        if m.group(2) not in figs: figs.append(m.group(2))
        return f'{m.group(1)} {figs.index(m.group(2)) + 1}'
    def chap(m):
        word, a, b = m.group(1), m.group(2), m.group(3)
        if b and a in keys and b in keys: ks = rng(a, b)
        else: ks = [a] + re.findall(NUM, m.group(4) or '')
        ks = [k for k in ks if k in titles] or ks
        plural = len(ks) > 1
        lead = ('the chapters ' if plural else 'the chapter ') if word[0].islower() else ('The chapters ' if plural else 'The chapter ')
        return lead + names(ks)
    def text(t):
        t = re.sub(r'\b(Fig(?:ure|\.))\s+(\d+\.\d+\.\d+)', fig, t)
        t = re.sub(r'\b([Cc]hapters?)\s+(' + NUM + r')(?:\s+to\s+(' + NUM + r'))?((?:(?:,\s*|\s+and\s+)' + NUM + r')*)', chap, t)
        t = re.sub(r'\b(?:in|see)\s+' + NUM + r'\b', lambda m: m.group(0).split()[0] + ' ' + q(re.search(NUM, m.group(0)).group(0)) if re.search(NUM, m.group(0)).group(0) in titles else m.group(0), t)
        return t
    cut = re.sub(r'(<a href="#[^"]*">)(' + NUM + r')(</a>)', lambda m: m.group(1) + (q(m.group(2)) if m.group(2) in titles else m.group(2)) + m.group(3), cut)
    cut = visible(cut, text)
    # key-terms table: the Chapter column holds bare numbers
    def keyterms(sec):
        return re.sub(r'<td>((?:' + NUM + r')(?:,\s*' + NUM + r')*)</td>', lambda m: '<td>' + names(re.findall(NUM, m.group(1))) + '</td>' if all(k in titles for k in re.findall(NUM, m.group(1))) else m.group(0), sec.group(0))
    cut = re.sub(r'<section id="summary">.*?</section>', keyterms, cut, flags=re.S)
    return cut

def wrapped(book_html, meta, n, lesson, lessons, unit_book_name, standalone=False):
    cut = orig(book_html, meta, n, lesson, lessons, unit_book_name, standalone)
    if cut and standalone:
        cut = denumber(book_html, cut)
        if os.environ.get('DENUMBER_DUMP'):   # optional: keep each cut html for checking
            open(os.path.join(os.environ['DENUMBER_DUMP'], f'{meta["sid"]}-u{n}-L{lesson["n"]}.html'), 'w').write(cut)
    return cut
ms.cut_lesson_notes = wrapped
ms.main(sys.argv[1:])
