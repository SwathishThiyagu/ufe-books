#!/usr/bin/env python3
"""Check one University free n easy unit book against its packet.
usage: python3 check_book.py <book.html> <packet.json> [--render]
Exit code 0 = OK. Prints every problem it finds; fix them all, then run it again."""
import sys, re, json, os, html
from html.parser import HTMLParser

class Walk(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []            # (tag, attrs dict)
        self.sections = {}         # id -> dict(text words, counts)
        self.cur = None            # id of the enclosing main>section
        self.depth_main = None
        self.ids = []
        self.scripts = 0; self.ext = []; self.in_skip = 0
        self.titles = {}           # section id -> h2 text
        self._h2 = None
        self.words_all = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs); self.stack.append((tag, a))
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'main': self.depth_main = len(self.stack)
        if tag == 'section' and self.depth_main and len(self.stack) == self.depth_main + 1:
            self.cur = a.get('id') or f'<section without id #{len(self.sections)}>'
            self.sections[self.cur] = dict(words=0, fig=0, svg=0, example=0, traps=0, beyond=0, quiz=0, levels=set(), cls=a.get('class', ''), h2='', details=0, h3=0)
        s = self.sections.get(self.cur)
        if s is not None:
            cls = a.get('class', '').split()
            if tag == 'figure' and 'fig' in cls: s['fig'] += 1
            if tag == 'svg': s['svg'] += 1
            if tag == 'h3': s['h3'] += 1
            if tag == 'div':
                for k in ('example', 'traps', 'beyond', 'quiz'):
                    if k in cls: s[k] += 1
            if tag == 'details':
                s['details'] += 1
                if a.get('data-level'): s['levels'].add(a['data-level'].lower())
            if tag == 'h2': self._h2 = ''
        if tag == 'script':
            self.scripts += 1
            if a.get('src'): self.ext.append(a['src'])
        if tag in ('img', 'iframe', 'video', 'audio', 'link') and a.get('src', a.get('href', '')).startswith('http') and tag != 'link':
            self.ext.append(a.get('src') or a.get('href'))
        if tag == 'link' and a.get('href', '').startswith('http') and 'fonts.googleapis.com' not in a.get('href', '') and 'fonts.gstatic.com' not in a.get('href', ''):
            self.ext.append(a['href'])
        if tag in ('script', 'style', 'svg'): self.in_skip += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'svg'): self.in_skip = max(0, self.in_skip - 1)
        if tag == 'h2' and self._h2 is not None and self.cur in self.sections:
            self.sections[self.cur]['h2'] = re.sub(r'\s+', ' ', self._h2).strip(); self._h2 = None
        # pop to the matching open tag
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]; break
        if tag == 'section' and self.depth_main and len(self.stack) == self.depth_main: self.cur = None
    def handle_data(self, data):
        if self._h2 is not None: self._h2 += data
        if self.in_skip: return
        n = len(data.split()); self.words_all += n
        if self.cur in self.sections: self.sections[self.cur]['words'] += n

def main():
    if len(sys.argv) < 3: print(__doc__); sys.exit(2)
    path, pk = sys.argv[1], sys.argv[2]
    P = json.load(open(pk)); unit = P['unit']; subs = unit['subtopics']
    probs = []
    try: raw = open(path, encoding='utf-8').read()
    except Exception as e: print('cannot read', path, e); sys.exit(1)
    if not raw.lstrip().lower().startswith('<!doctype html'): probs.append('file must start with <!doctype html> (copy book_shell.html)')
    left = re.findall(r'__[A-Z_]+__', raw)
    if left: probs.append(f'placeholders not filled: {sorted(set(left))}')
    for bad in ('lorem ipsum', 'TODO', 'TBD', '[citation needed]', 'as an AI', 'I cannot', 'placeholder'):
        if bad.lower() in raw.lower(): probs.append(f'text contains "{bad}"')
    w = Walk(); w.feed(raw)
    if w.ext: probs.append(f'external resources are not allowed (books must be self-contained): {w.ext[:3]}')
    dup = {i for i in w.ids if w.ids.count(i) > 1}
    if dup: probs.append(f'duplicate ids: {sorted(dup)[:6]}')
    title = re.search(r'<title>(.*?)</title>', raw, re.S)
    if not title or P['subject']['name'] not in html.unescape(title.group(1)) or f"Unit {unit['n']}" not in html.unescape(title.group(1)):
        probs.append(f'<title> must contain the subject name and "Unit {unit["n"]}"')
    # the chapters: one section.ch per subtopic, in order, id = packet slug, h2 = packet text
    chs = [(i, s) for i, s in w.sections.items() if 'ch' in s['cls'].split()]
    want = [s['id'] for s in subs]
    got = [i for i, _ in chs]
    if got != want: probs.append(f'chapter sections must be exactly the packet subtopics in order; expected ids {want}, found {got}')
    for st in subs:
        s = w.sections.get(st['id'])
        if not s: continue
        name = f'chapter "{st["id"]}"'
        h2 = re.sub(r'^\s*\d+\.\d+\s*', '', s['h2'])
        if h2.strip().lower() != st['t'].strip().lower(): probs.append(f'{name}: h2 must be the subtopic text "{st["t"]}" (found "{h2}")')
        if s['words'] < 650: probs.append(f'{name}: only {s["words"]} words (write at least 650; 900-1600 is the target)')
        if s['words'] > 1900: probs.append(f'{name}: {s["words"]} words is too long (keep under 1900; 900-1600 is the target)')
        if s['fig'] < 1 or s['svg'] < 1: probs.append(f'{name}: needs at least one <figure class="fig"> with an inline <svg>')
        if s['example'] < 1: probs.append(f'{name}: needs a <div class="example"> worked example')
        if s['traps'] < 1: probs.append(f'{name}: needs a <div class="traps"> exam-traps box')
        if s['quiz'] < 1 or s['details'] < 5: probs.append(f'{name}: needs a <div class="quiz"> with at least 5 <details data-level=...> questions')
        missing = {'remember', 'understand', 'apply', 'analyze'} - s['levels']
        if missing: probs.append(f'{name}: quiz is missing levels {sorted(missing)}')
        if s['beyond'] < 1: probs.append(f'{name}: needs a <div class="beyond"> section')
    for sec in ('about', 'summary', 'question-bank', 'glossary', 'sources'):
        if sec not in w.sections: probs.append(f'missing unit section id="{sec}"')
    if 'about' in w.sections:
        for u in P['subject']['taught_at']:
            if P['universities'][u]['short'] not in raw: probs.append(f'the crosswalk must mention {P["universities"][u]["short"]}')
    if 'question-bank' in w.sections and w.sections['question-bank']['details'] < 8: probs.append('question bank needs at least 8 questions')
    if 'sources' in w.sections and w.sections['sources']['words'] < 40: probs.append('sources section is too thin')
    svgs = re.findall(r'<svg[^>]*>', raw)
    for sv in svgs:
        if 'viewBox' not in sv: probs.append('every <svg> needs a viewBox (so it scales on phones)'); break
    size = os.path.getsize(path)
    if size > 1_800_000: probs.append(f'file is {size//1024} KB; keep under 1,800 KB')
    if '--render' in sys.argv:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                b = p.chromium.launch(); errs = []
                for wdt in (390, 1366):
                    pg = b.new_page(viewport={'width': wdt, 'height': 900})
                    pg.on('pageerror', lambda e: errs.append(str(e)))
                    pg.goto('file://' + os.path.abspath(path)); pg.wait_for_timeout(400)
                    sw, iw = pg.evaluate('[document.documentElement.scrollWidth, innerWidth]')
                    if sw > iw: probs.append(f'page is wider than the screen at {wdt}px ({sw}>{iw}): a table, figure or long word overflows')
                    n = pg.evaluate("document.querySelectorAll('#toc a').length")
                    if n < len(subs): probs.append('the contents list did not build: check the shell script was kept')
                    # figures: text that spills out of its svg box
                    spill = pg.evaluate("""[...document.querySelectorAll('figure.fig svg')].map((s,i)=>{const r=s.getBoundingClientRect();let n=0;for(const t of s.querySelectorAll('text')){const b=t.getBoundingClientRect();if(b.right>r.right+1||b.left<r.left-1||b.bottom>r.bottom+1||b.top<r.top-1)n++;}return n?i+1:0;}).filter(Boolean)""")
                    if spill: probs.append(f'at {wdt}px, text spills outside the svg box in figure(s) {spill[:6]}: enlarge the viewBox or shorten the labels')
                    pg.close()
                b.close()
            if errs: probs.append(f'javascript errors: {errs[:3]}')
        except Exception as e:
            print('render check skipped:', e)
    print(f'{os.path.basename(path)}: {len(chs)} chapters, {w.words_all} words, {len(svgs)} figures, {size//1024} KB')
    if probs:
        print('PROBLEMS:'); [print(' -', x) for x in probs]; sys.exit(1)
    print('OK')

if __name__ == '__main__':
    main()
