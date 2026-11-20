#!/usr/bin/env python3
"""Build a University free n easy voiced lesson from a lesson file and the template.

usage: python3 lesson_build.py lesson.js out.html [--silent] [--check] [--reuse] [--no-bumper] [--voice af_heart] [--speed 1.0] [--gap 0.55] [--lead 0.3]
  --check   evaluate the lesson, render every scene, check cues and narration, print the report, build nothing
  --silent  build a draft with estimated timing and no voice (for layout work)
  --reuse   keep the voice already built (out.mp3 and out.words.json beside out.html) when only the drawing or the engine changed
  --revoice keep the voice of every unchanged line (from out.mp3 and out.words.json) and voice only the new or changed lines
  --no-bumper  build without the channel logo (by default the red panda crossfade plays at the top right over the hook, its three
            poses on the hook's caption cues, and returns over the last 6 s with the Like and Subscribe pills and their sounds;
            poses and sounds come from bumper/ beside this script; nothing is added to the running time)
Needs node (lesson_eval.js beside this script), the template (lesson_template.html beside it), and for the voice
/home/claude/kokoro/kokoro_tts.py with the model unpacked (kokoro-tts skill, step 1) plus ffmpeg."""
import sys, os, re, json, subprocess, base64, tempfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
LESSON = ''
KOKORO = os.environ.get('KOKORO_HOME', '/home/claude/kokoro')
GENERIC_MARK = re.compile(r'\[([^\]]+)\]\(/[^)]*/\)')          # [word](/phonemes/) -> word, for captions and cue matching
BUMPER_IN, BUMPER_OUT = 0.0, 0.0                                   # no padding: the logo plays over the hook and the end card over the last OUTRO s of the lesson itself
INTRO, OUTRO = 6.0, 6.0                                            # the logo over the first INTRO s (2 s per pose) and over the last OUTRO s with the pills
LOGO_OPACITY = 0.8
SFX = [('sfx_like.wav', 0.9 + 0.55), ('sfx_sub.wav', 1.9 + 0.55)]      # sounds mixed in: each at OUTRO-relative time (the moment its pill lands)

def opt(args, key, default, cast=str):
    if key in args:
        i = args.index(key); v = cast(args[i + 1]); del args[i:i + 2]; return v
    return default

def evaluate(lesson, tpl):
    r = subprocess.run(['node', os.path.join(HERE, 'lesson_eval.js'), lesson, tpl], capture_output=True, text=True)
    if r.returncode != 0: sys.exit('lesson_eval.js failed: ' + r.stderr[-800:])
    out = json.loads(r.stdout); out['_src'] = open(lesson, encoding='utf8').read(); return out

def clean(say): return GENERIC_MARK.sub(r'\1', say)
def bare(say): return GENERIC_MARK.sub('', say)                   # the narration without its phoneme-marked words

def norm(w): return re.sub(r"[^a-z0-9'-]", '', w.lower())

# ---- text rules (SLOP.md, approved 17 Nov): run on every say, on the text each scene draws (code excepted), and on META.
# A hit fails the check; WARN rules only print. META.allow lists phrases that are content, not slop ("booking site", "h_a").
NUM = r'(?:one|two|three|four|five|six|seven|eight|nine|ten|\d+)'
BLOOM = r'(?:remember|understand|apply|analy[sz]e|evaluate|create)'
TEXT_RULES = [
    ('book wording ("your free notes", never "book")', re.compile(r"\b(?:your|the|unit|this) book(?:['’]s|s)?\b|\bof your notes\b", re.I)),
    ('a unit number or unit reference (name the topic)', re.compile(r"\bunits? " + NUM + r"\b|\b(?:this|next|previous|last) unit\b(?! (?:vector|circle|cell|test|step|price|cost|of|square|matrix))|\ball \w+ units\b|\bunits \d+ (?:to|-|–) \d+\b", re.I)),
    ('a spoken or shown Bloom level', re.compile(r"\ban? " + BLOOM + r" question\b|\bat the \w+ level\b|\bquestion " + NUM + r"[,.:]? (?:an? |at the )?" + BLOOM + r"(?: level| question)?\s*(?:[,.:;!?·]|$)|\bquestion " + NUM + r" · " + BLOOM + r"\b", re.I)),
    ('a site or finder line (no site yet)', re.compile(r"\bfind (?:this unit|your (?:own )?syllabus)\b|\bon (?:our|the university free (?:n|and) easy) (?:web)?site\b|\buniversity free (?:n|and) easy (?:web)?site\b", re.I)),
]
SCREEN_RULES = [
    ('caret maths (use ² or a sup tspan)', re.compile(r"[\w)]\^[\w(−-]")),
    ('a chapter, figure or lesson number (they reveal the unit: name the topic)', re.compile(r"\bchapters? \d+\.\d+|\bfigure \d+\.\d+|\blesson \d+\b", re.I)),
    ('underscore subscript (use ₐ or a sub tspan)', re.compile(r"(?<![\w.$])(?<!->)(?![A-Z]{2}_[A-Z]{3})(?![a-z]{2}_[a-z]{3})[A-Za-zα-ωΑ-Ω]{1,2}_(?:\{[^}]*\}|[A-Za-z0-9]{1,6})(?![\w(])")),
]
WARN_RULES = [
    ('filler word', re.compile(r"\b(?:delve|delving|journey|unlock|crucial|essentially|imagine|amazing|dive into|let['’]s take control)\b", re.I)),
]
CODE_LINE = re.compile(r"[;{}]|[A-Za-z_]\w*\(|\b(?:int|float|double|void|char|return|def|let|const|var|public|private|class|import)\b|==|->|=>")
INDIAN, WESTERN = re.compile(r"(?<![\d,])\d{1,2},\d{2},\d{3}(?![\d,])"), re.compile(r"(?<![\d,])\d{3},\d{3}(?![\d,])|,\d{3},\d{3}")

def text_rules(ev):
    meta, probs, warns = ev.get('meta', {}), [], []
    allow = [a.lower() for a in (meta.get('allow') or [])]
    def strip(t):
        t = GENERIC_MARK.sub(r'\1', t); low = t.lower()
        for a in allow:
            while a and a in low: i = low.index(a); t = t[:i] + ' ' * len(a) + t[i + len(a):]; low = t.lower()
        return t
    def hit(where, txt, rules, out):
        for name, rx in rules:
            m = rx.search(txt)
            if m: out.append(f'{where}: {name}: "{txt[max(0, m.start() - 25):m.end() + 25].strip()}"')
    for key in ('kick', 'title', 'series', 'star', 'big', 'badge'):
        if isinstance(meta.get(key), str): hit(f'META.{key}', strip(meta[key]), TEXT_RULES + SCREEN_RULES, probs)
    nums = {'in': [], 'we': []}
    for sc in ev['scenes']:
        n = sc['i'] + 1
        say = strip(sc.get('say', ''))
        hit(f'scene {n} say', say, TEXT_RULES, probs); hit(f'scene {n} say', say, WARN_RULES, warns)
        for line in sc.get('screen', []):
            if CODE_LINE.search(line): continue
            t = strip(line)
            hit(f'scene {n} screen', t, TEXT_RULES + SCREEN_RULES, probs); hit(f'scene {n} screen', t, WARN_RULES, warns)
            if INDIAN.search(t): nums['in'].append(n)
            if WESTERN.search(t): nums['we'].append(n)
        stock = [i for i in sc.get('icons', []) if i and i in ev.get('builtin_icons', []) and i.lower() not in allow]
        if stock: warns.append(f'scene {n}: recap uses built-in icons {", ".join(stock)}; draw the card\'s own picture (or list the name in META.allow)')
    if nums['in'] and nums['we']: warns.append(f'Indian (scenes {sorted(set(nums["in"]))}) and Western (scenes {sorted(set(nums["we"]))}) number grouping in one lesson; use one')
    return probs, warns

def check(ev):
    probs = list(ev['errors'])
    src = ev.get('_src', '')
    todo = [i + 1 for i, l in enumerate(src.splitlines()) if 'TODO' in l and not l.lstrip().startswith(('/*', '//', '-', '*'))]
    if todo: probs.append(f'{len(todo)} line(s) still have TODO (lines {", ".join(map(str, todo[:12]))}{"…" if len(todo) > 12 else ""})')
    meta, scenes = ev.get('meta', {}), ev['scenes']
    for key in ('title', 'parts', 'chips', 'badge', 'kick'):
        if key not in meta: probs.append(f'META.{key} is missing')
    if meta.get('parts') and meta.get('chips') and len(meta['parts']) != len(meta['chips']): probs.append('META.chips must have one [two lines] per part')
    kinds = [s['k'] for s in scenes]
    for need in ('agenda', 'recap', 'outro'):
        if need not in kinds: probs.append(f'no {need} scene')
    if 'pq' in kinds and kinds.count('pq') != kinds.count('pa'): probs.append('every pq (question) needs a pa (answer) scene right after it')
    jokes = []
    for s in scenes:
        n = s['i'] + 1; say = s['say']
        if not say.strip(): probs.append(f'scene {n}: no narration (say)'); continue
        words = clean(say).split()
        if re.search(r'\d', bare(say)): probs.append(f'scene {n}: digits in the narration; write numbers as words')
        if re.search(r'[%&$+=/@#<>]', bare(say)): probs.append(f'scene {n}: a symbol in the narration; write it as a word')
        if len(words) > 60: probs.append(f'scene {n}: {len(words)} words in one line; split the scene')
        # the letter A: a bare "a"/"A" that reads as a letter (before "and", "is", "equals", a capital letter, or at a phrase end)
        txt = GENERIC_MARK.sub('mark', say)                        # marked words ([a](/ɐ/), [A](/ˈA/), [GEF](/…/)) are already decided
        for m in re.finditer(r'(?<![\[\w])([aA])(?=[\s,.;:!?]|$)', txt):
            after = txt[m.end():m.end() + 12]
            if re.match(r'\s*(and|is|equals|or|to|plus|minus|times|over|[A-Z]\b)', after) or re.match(r'[,.;:!?]', after):
                probs.append(f'scene {n}: "{txt[max(0, m.start()-15):m.end()+12].strip()}" — is this the letter A? write [A](/ˈA/) or the article [a](/ɐ/)'); break
        low = [norm(w) for w in words]
        for k, phrase in (s.get('cues') or {}).items():
            toks = [norm(t) for t in str(phrase).split() if norm(t)]
            if not toks: probs.append(f'scene {n}: cue {k} is empty'); continue
            hits = [j for j in range(len(low)) if all(j + x < len(low) and (low[j + x].startswith(toks[x]) if x == len(toks) - 1 else low[j + x] == toks[x]) for x in range(len(toks)))]
            if not hits: probs.append(f'scene {n}: cue {k} "{phrase}" is not in the narration')
            elif len(hits) > 1: probs.append(f'scene {n}: cue {k} "{phrase}" occurs {len(hits)} times in the line; the first one wins, so add words until it is unique')
        if s.get('joke'): jokes.append(f'scene {n}: {s["joke"]}')
    # dictionary check through Kokoro when it is installed
    try:
        sys.path.insert(0, KOKORO); import kokoro_tts as K
        load_pron(K); g = K.g2p('us'); unknown = []
        for s in scenes:
            a = g.align(s['say'])
            for w in a['unknown']: unknown.append(f'scene {s["i"]+1}: {w}')
        if unknown: probs.append('not in the dictionary (give inline phonemes or add to EXTRA): ' + '; '.join(unknown[:12]))
    except Exception as e:
        print('dictionary check skipped:', str(e)[:80])
    tp, warns = text_rules(ev); probs += tp
    return probs, jokes, warns

def estimate(scenes, gap, lead):
    lines, t = [], lead
    for s in scenes:
        text = clean(s['say']); words = text.split(); dur = max(1.2, len(words) / 2.3)                              # Kokoro af_heart at 1.0 averages 2.3 words a second
        lines.append(dict(start=round(t, 3), end=round(t + dur, 3), text=text, words=[[w, round(t + i * dur / max(1, len(words)), 3)] for i, w in enumerate(words)]))
        t += dur + gap + s['pause']
    return lines, t

def load_pron(K):
    # words the dictionary lacks, in misaki notation: pronunciation.json beside the lesson or beside this script
    # also <lesson>.pron.json beside the lesson: each lesson of a unit keeps its own, so parallel writers never overwrite each other
    stem = os.path.splitext(os.path.abspath(LESSON))[0]
    for f in (os.path.join(HERE, 'pronunciation.json'), os.path.join(os.path.dirname(os.path.abspath(LESSON)), 'pronunciation.json'), stem + '.pron.json'):
        if os.path.exists(f): K.EXTRA.update(json.load(open(f, encoding='utf-8')))

def voice(scenes, out_base, voice, speed, gap, lead):
    sys.path.insert(0, KOKORO); import kokoro_tts as K
    load_pron(K)
    rows = [{'pause': lead}] + [{'text': s['say'], 'pause_after': gap + s['pause']} for s in scenes]
    wav = out_base + '.wav'
    lines, total = K.make(rows, wav, voice, speed, gap, None, False, log=lambda m: None)
    mp3 = out_base + '.mp3'
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', wav, '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11', '-ar', '44100', '-c:a', 'libmp3lame', '-b:a', '112k', mp3], check=True)
    os.remove(wav)
    return [dict(start=l['start'], end=l['end'], text=l['text'], words=l['words']) for l in lines], total, mp3

def revoice(scenes, base, vo, speed, gap, lead):
    """Keep the voice of every line whose narration is unchanged (cut from base.mp3 at its words.json start and end) and voice
    only the new or changed lines with Kokoro; then lay the lines out again with the usual lead and gaps. New clips are scaled
    to the reused clips' loudness before the whole track gets the same loudnorm pass as a full build."""
    import numpy as np
    sys.path.insert(0, KOKORO); import kokoro_tts as K
    load_pron(K); SR = K.SR
    W = json.load(open(base + '.words.json', encoding='utf-8'))
    # a track taken out of a built page (premixed) has the end-card sounds in its last OUTRO s: voice again every line that
    # reaches the first sound, so the sounds are not cut in and then mixed in a second time
    cut = W['total'] - OUTRO + min(at for _, at in SFX) - 0.05 if W.get('premixed') else None
    if (W.get('voice'), float(W.get('speed', 1.0))) != (vo, float(speed)): sys.exit(f"--revoice: the old track is {W.get('voice')} at {W.get('speed')}; build with the same voice and speed or without --revoice")
    raw = subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-i', base + '.mp3', '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True, check=True).stdout
    old = np.frombuffer(raw, dtype=np.float32)
    used, plan = set(), []
    for i, sc in enumerate(scenes):
        txt = clean(sc['say'])
        ok = lambda j: W['lines'][j]['text'] == txt and j not in used and (cut is None or W['lines'][j]['end'] < cut)
        cand = [i] if i < len(W['lines']) and ok(i) else []
        cand = cand or [j for j in range(len(W['lines'])) if ok(j)][:1]
        if cand: used.add(cand[0]); plan.append(('old', cand[0]))
        else: plan.append(('new', None))
    clips, metas, rms_old = [], [], []
    for (kind, j), sc in zip(plan, scenes):
        if kind == 'old':
            l = W['lines'][j]; a = old[int(round(l['start'] * SR)):int(round(l['end'] * SR))].copy()
            clips.append(a); metas.append({'text': l['text'], 'words': [[w, round(t - l['start'], 3)] for w, t in l['words']]})
            if len(a): rms_old.append(float(np.sqrt(np.mean(a ** 2))))
        else:
            a, m = K.speak(sc['say'], vo, speed)
            clips.append(a); metas.append({'text': m['text'], 'words': m['words'], 'new': True})
    ref = float(np.median(rms_old)) if rms_old else None
    for k, m in enumerate(metas):
        if m.get('new') and ref and len(clips[k]):
            r = float(np.sqrt(np.mean(clips[k] ** 2)))
            if r > 0: clips[k] = np.clip(clips[k] * (ref / r), -1, 1)
    parts, lines, n = [np.zeros(int(lead * SR), np.float32)], [], int(lead * SR)
    for k, (a, m, sc) in enumerate(zip(clips, metas, scenes)):
        t = n / SR
        lines.append(dict(start=round(t, 3), end=round(t + len(a) / SR, 3), text=m['text'], words=[[w, round(t + wt, 3)] for w, wt in m['words']]))
        parts.append(a.astype(np.float32)); n += len(a)
        parts.append(np.zeros(int(max(0.0, gap + sc['pause'] - K.PAD_IN - K.PAD_OUT) * SR), np.float32)); n += len(parts[-1])
    wav = base + '.revoice.wav'; K.write_wav(wav, np.concatenate(parts))
    mp3 = base + '.mp3'
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', wav, '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11', '-ar', '44100', '-c:a', 'libmp3lame', '-b:a', '112k', mp3], check=True)
    os.remove(wav)
    nn = sum(1 for k, _ in plan if k == 'new')
    print(f'--revoice: {len(scenes) - nn} lines reused, {nn} voiced again' + (': scenes ' + ', '.join(str(i + 1) for i, (k, _) in enumerate(plan) if k == 'new') if nn else ''))
    return lines, n / SR, mp3

def bumper_overlay(total, poses):
    """The channel logo as an SVG overlay with CSS keyframes on the page timeline (the CBSE lessons' converter-safe way):
    the three poses crossfade 2 s each at the top right over the first INTRO s (pop in, pop out) and again, larger, over the last OUTRO s,
    with the Like and Subscribe pills sliding up at the bottom right. Returns (svg markup, css)."""
    T = total; HOLD, FADE = 1.2, 0.8; STEP = HOLD + FADE; POP = 0.45; O = LOGO_OPACITY
    src = ['data:image/png;base64,' + base64.b64encode(open(f, 'rb').read()).decode() for f in poses]
    pc = lambda t: f'{max(0.0, min(100.0, t / T * 100)):.6f}%'
    def kf(name, steps):   # steps: [(time, css)] on the T-long timeline, linear between them
        return '@keyframes ' + name + '{' + ''.join(f'{pc(t)}{{{css}}}' for t, css in steps) + '}\n'
    E = 0.001; o = T - OUTRO
    css = ''
    # the logo group: pops in, holds, pops out (intro); pops in larger and stays (outro)
    css += kf('lgPop', [(0, f'opacity:0;transform:scale(.6) rotate(5deg)'), (POP, f'opacity:{O};transform:scale(1) rotate(0deg)'), (INTRO - POP, f'opacity:{O};transform:scale(1) rotate(0deg)'), (INTRO, 'opacity:0;transform:scale(.6) rotate(0deg)'),
                        (o - E, 'opacity:0;transform:scale(.6) rotate(5deg)'), (o, 'opacity:0;transform:scale(.6) rotate(5deg)'), (o + POP, f'opacity:{O};transform:scale(1) rotate(0deg)'), (T, f'opacity:{O};transform:scale(1) rotate(0deg)')])
    # the three poses, 2 s each: hold 1.2 s, crossfade 0.8 s; the same over the outro, ending asleep
    def pose(i, name):
        on, off = i * STEP, i * STEP + HOLD                       # fully on from (on) ... fade out from (off) to (off+FADE); fade in from (on-FADE) to (on)
        seq = []
        for base in (0, o):
            a = base + on; b = base + off
            if i == 0: seq += [(base, 'opacity:1'), (b, 'opacity:1'), (b + FADE, 'opacity:0')]
            elif i == 1: seq += [(base, 'opacity:0'), (a - FADE, 'opacity:0'), (a, 'opacity:1'), (b, 'opacity:1'), (b + FADE, 'opacity:0')]
            else: seq += [(base, 'opacity:0'), (a - FADE, 'opacity:0'), (a, 'opacity:1'), (base + INTRO if base == 0 else T, 'opacity:1')] + ([(INTRO + E, 'opacity:0')] if base == 0 else [])
            if base == 0: seq += [(o - E, seq[-1][1] if i == 2 and False else 'opacity:0')]
        if i < 2: seq += [(T, 'opacity:0')]          # end point: the pose stays faded out to the end (10 Nov 2026)
        seq = sorted(seq, key=lambda q: q[0])
        return kf(name, seq)
    css += pose(0, 'lgP0') + pose(1, 'lgP1') + pose(2, 'lgP2')
    # the pills: 6 s animations that start at T - OUTRO (Like at 0.9 s, Subscribe at 1.9 s)
    def pill(nm, t0):
        q = lambda t: f'{t / OUTRO * 100:.6f}%'
        m = f'@keyframes {nm}M{{0%{{opacity:0;transform:translateY(42px)}}{q(t0)}{{opacity:0;transform:translateY(42px)}}{q(t0+.4)}{{opacity:1;transform:translateY(8px)}}{q(t0+.55)}{{opacity:1;transform:translateY(0)}}{q(t0+.78)}{{transform:translateY(0) scale(1.07)}}{q(t0+1)}{{transform:translateY(0) scale(1)}}100%{{opacity:1;transform:translateY(0)}}}}\n'
        d = f'@keyframes {nm}D{{0%{{opacity:0}}{q(t0+.72)}{{opacity:0}}{q(t0+.8)}{{opacity:1}}100%{{opacity:1}}}}\n'
        d2 = f'@keyframes {nm}U{{0%{{opacity:1}}{q(t0+.72)}{{opacity:1}}{q(t0+.8)}{{opacity:0}}100%{{opacity:0}}}}\n'
        return m + d + d2
    css += pill('ecLike', 0.9) + pill('ecSub', 1.9)
    css += f'@keyframes ecLikeI{{0%{{transform:rotate(0) scale(1)}}{1.45/OUTRO*100:.4f}%{{transform:rotate(0) scale(1)}}{1.7/OUTRO*100:.4f}%{{transform:rotate(-22deg) scale(1.45)}}{1.95/OUTRO*100:.4f}%{{transform:rotate(0) scale(1)}}100%{{transform:rotate(0) scale(1)}}}}\n'
    css += f'@keyframes ecSubI{{0%{{transform:rotate(0)}}{2.7/OUTRO*100:.4f}%{{transform:rotate(0)}}{2.78/OUTRO*100:.4f}%{{transform:rotate(20deg)}}{2.94/OUTRO*100:.4f}%{{transform:rotate(-18deg)}}{3.1/OUTRO*100:.4f}%{{transform:rotate(12deg)}}{3.26/OUTRO*100:.4f}%{{transform:rotate(-6deg)}}{3.4/OUTRO*100:.4f}%{{transform:rotate(0)}}100%{{transform:rotate(0)}}}}\n'
    css += f'@keyframes ecNote{{0%{{opacity:0}}{.5/OUTRO*100:.4f}%{{opacity:0}}{1/OUTRO*100:.4f}%{{opacity:1}}100%{{opacity:1}}}}\n'
    css += f'#lgPop{{animation:lgPop {T:.3f}s linear both}}#lgP0{{animation:lgP0 {T:.3f}s linear both}}#lgP1{{animation:lgP1 {T:.3f}s linear both}}#lgP2{{animation:lgP2 {T:.3f}s linear both}}\n'
    for nm in ('ecLikeM', 'ecLikeD', 'ecLikeD2', 'ecLikeU', 'ecLikeI', 'ecLikeI2', 'ecSubM', 'ecSubD', 'ecSubD2', 'ecSubU', 'ecSubI', 'ecSubI2', 'ecNote'):
        css += f'#{nm}{{animation:{nm[:-1] if nm.endswith("2") else nm} {OUTRO:.3f}s linear {o:.3f}s both}}'
    # markup: the logo (144 x 181 at the top right, 646 x 812 art inside; the characters clipped above the wordmark, the wordmark from pose 2)
    W, H = 144, 181
    clip0 = 'M0 0H646V570H460L440 574L270 580L230 582L185 587L170 570H0Z'; clip1 = 'M0 0H646V574H380L370 586H280L270 574H0Z'
    svg = (f'<svg id="bumpSvg" viewBox="0 0 1600 900" preserveAspectRatio="none" aria-hidden="true">'
           f'<defs><clipPath id="lgc0"><path d="{clip0}"/></clipPath><clipPath id="lgc1"><path d="{clip1}"/></clipPath><clipPath id="lgc2"><rect width="646" height="560"/></clipPath><clipPath id="lgcw"><rect y="565" width="646" height="247"/></clipPath></defs>'
           f'<g transform="translate({1540 - W} 6)"><g id="lgPop" class="bx" opacity="0"><svg width="{W}" height="{H}" viewBox="0 0 646 812">'
           f'<image id="lgP0" href="{src[0]}" width="646" height="812" clip-path="url(#lgc0)"/><image id="lgP1" href="{src[1]}" width="646" height="812" clip-path="url(#lgc1)" opacity="0"/>'
           f'<image id="lgP2" href="{src[2]}" width="646" height="812" clip-path="url(#lgc2)" opacity="0"/><image href="{src[2]}" width="646" height="812" clip-path="url(#lgcw)"/></svg></g></g>')
    # the pills (60 % size) at the bottom right, with the note above
    thumb = 'M2 10h4v11H2zM9 21h8.2a2 2 0 0 0 1.9-1.4l2.6-7.6A2 2 0 0 0 19.8 9H14l.9-4.3A1.6 1.6 0 0 0 12.2 3.4L9 9.2z'
    bell = 'M12 22a2.5 2.5 0 0 0 2.4-2h-4.8A2.5 2.5 0 0 0 12 22zm7-6V11a7 7 0 0 0-5.5-6.8V3.5a1.5 1.5 0 0 0-3 0v.7A7 7 0 0 0 5 11v5l-2 2v1h18v-1z'
    FS, PH = 29, 56; LW, SW = 150, 222; y = 824; xs = 1540 - SW; xl = xs - 16 - LW
    def pillsvg(nm, x, w, label, icon, cls, bg, fg, done, fgdone):
        txt = lambda col, gid, extra: (f'<g id="{gid}" {extra}><g transform="translate({x+22} {y+12}) scale(1.35)"><g id="{nm}I{"2" if gid.endswith("D2") else ""}" class="{cls}"><path d="{icon}" fill="{col}"/></g></g>'
                                       f'<text x="{x+62}" y="{y+PH/2+10}" font-family="\'Nunito Sans\',Arial,sans-serif" font-size="{FS}" font-weight="800" fill="{col}">{label}</text></g>')
        return (f'<g id="{nm}M" class="pm" opacity="0"><rect x="{x}" y="{y+7}" width="{w}" height="{PH}" rx="{PH/2}" fill="#18213A" opacity=".14"/>'
                f'<rect x="{x}" y="{y}" width="{w}" height="{PH}" rx="{PH/2}" fill="{bg}"/><rect id="{nm}D" x="{x}" y="{y}" width="{w}" height="{PH}" rx="{PH/2}" fill="{done}" opacity="0"/>'
                + txt(fg, nm + 'U', 'opacity="1"') + txt(fgdone, nm + 'D2', 'opacity="0"') + '</g>')
    svg += (f'<text id="ecNote" x="1540" y="{y-18}" text-anchor="end" font-family="\'Nunito Sans\',Arial,sans-serif" font-size="15" font-weight="800" letter-spacing="3.3" fill="#0CA678" opacity="0">IF THIS HELPED</text>'
            + pillsvg('ecLike', xl, LW, 'Like', thumb, 'ic', '#FFFFFF', '#18213A', '#18213A', '#FFFFFF') + pillsvg('ecSub', xs, SW, 'Subscribe', bell, 'bl', '#E03131', '#FFFFFF', '#B02222', '#FFFFFF') + '</svg>')
    return svg, css

def main(args):
    silent = '--silent' in args; chk = '--check' in args; reuse = '--reuse' in args; rev = '--revoice' in args; nobump = '--no-bumper' in args
    args = [a for a in args if a not in ('--silent', '--check', '--reuse', '--revoice', '--no-bumper')]
    vo = opt(args, '--voice', 'af_heart'); speed = opt(args, '--speed', 1.0, float); gap = opt(args, '--gap', 0.55, float); lead = opt(args, '--lead', 0.3, float)
    if len(args) < 2: sys.exit(__doc__)
    lesson, out = args[0], args[1]
    global LESSON; LESSON = lesson
    tpl = os.path.join(HERE, 'lesson_template.html')
    ev = evaluate(lesson, tpl)
    probs, jokes, warns = check(ev)
    print(f"{len(ev['scenes'])} scenes; kinds: {', '.join(sorted(set(s['k'] for s in ev['scenes'])))}")
    nw = sum(len(clean(s['say']).split()) for s in ev['scenes']); est = (nw / 2.3 + sum(0.55 + s['pause'] for s in ev['scenes'])) / 60
    print(f'{nw} narration words, about {est:.1f} min voiced (aim 5 to 7: 800 to 880 words with pauses)')
    if jokes: print('joke beats:', len(jokes)); [print('  ', j) for j in jokes]
    if warns: print('WARNINGS (do not fail the check):'); [print(' -', w) for w in warns]
    if probs:
        print('PROBLEMS:'); [print(' -', p) for p in probs]
        if chk or ev['errors']: sys.exit(1)
    if chk: print('OK'); return
    scenes = ev['scenes']; base = os.path.splitext(out)[0]
    if silent:
        lines, total = estimate(scenes, gap, lead); audio_src = ''
    elif reuse and os.path.exists(base + '.mp3') and os.path.exists(base + '.words.json'):
        W = json.load(open(base + '.words.json', encoding='utf-8')); lines, total, mp3 = W['lines'], W['total'], base + '.mp3'
        premixed = bool(W.get('premixed'))   # audio taken from a built lesson: the pill sounds are already in it
        if len(lines) != len(scenes): sys.exit(f'--reuse: {len(lines)} voiced lines but {len(scenes)} scenes; the narration changed, build with --revoice')
        for l, sc in zip(lines, scenes):
            if l['text'] != clean(sc['say']): sys.exit(f"--reuse: scene {sc['i']+1} narration changed, build with --revoice")
        print('voice reused from', mp3)
    elif rev and os.path.exists(base + '.mp3') and os.path.exists(base + '.words.json'):
        lines, total, mp3 = revoice(scenes, base, vo, speed, gap, lead)
    else:
        if rev: print('--revoice: no out.mp3 and out.words.json beside the output, so every line is voiced')
        lines, total, mp3 = voice(scenes, base, vo, speed, gap, lead)
    # the channel bumper: poses beside this script; the audio gets BUMPER_IN s of silence before and BUMPER_OUT s after, and every time shifts
    poses = [os.path.join(HERE, 'bumper', f'pose{k}.png') for k in range(3)]
    bump = (not nobump) and all(os.path.exists(f) for f in poses)
    din, dout = (BUMPER_IN, BUMPER_OUT) if bump else (0.0, 0.0)
    bumper = json.dumps({'intro': INTRO, 'out': OUTRO}) if bump else 'null'
    if not silent:
        src_mp3 = mp3
        sfx = [(os.path.join(HERE, 'bumper', f), total - OUTRO + at) for f, at in SFX] if bump else []
        sfx = [(f, at) for f, at in sfx if os.path.exists(f) and at > 0 and not (reuse and 'premixed' in dir() and premixed)]
        if sfx:
            # the pill sounds land on the narration track at their moments (amix without normalising keeps the voice level)
            src_mp3 = base + '.bumper.mp3'
            ins = sum([['-i', f] for f, _ in sfx], [])
            fc = ''.join(f'[{k+1}]adelay={int(at*1000)}|{int(at*1000)},volume=0.9[s{k}];' for k, (_, at) in enumerate(sfx)) + '[0]' + ''.join(f'[s{k}]' for k in range(len(sfx))) + f'amix=inputs={len(sfx)+1}:normalize=0:duration=first[out]'
            subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', mp3] + ins + ['-filter_complex', fc, '-map', '[out]', '-ar', '44100', '-c:a', 'libmp3lame', '-b:a', '112k', src_mp3], check=True)
        audio_src = ' src="data:audio/mpeg;base64,' + base64.b64encode(open(src_mp3, 'rb').read()).decode() + '"'
    sh = lambda l: dict(l, start=round(l['start'] + din, 3), end=round(l['end'] + din, 3), words=[[w, round(t + din, 3)] for w, t in l['words']])
    lines_t = [sh(l) for l in lines]
    starts = [max(0.0, round(l['start'] - lead + din, 3)) for l in lines]
    total_t = round(total + din + dout, 3)
    episode = {'scenes': [{'start': s} for s in starts], 'total': total_t}
    data = {'dur': total_t, 'lines': lines_t}
    src = open(lesson, encoding='utf-8').read()
    meta = ev['meta']
    html = (open(tpl, encoding='utf-8').read().replace('__TITLE__', f"{meta.get('kick', '')} · {meta.get('title', '')}".strip(' ·'))
            .replace('__AUDIO_SRC__', audio_src).replace('__EPISODE__', json.dumps(episode)).replace('__DATA__', json.dumps(data, ensure_ascii=False))
            .replace('__LESSON__', src).replace('__BUMPER__', bumper))
    bsvg, bcss = bumper_overlay(total, poses) if bump else ('', '')
    html = html.replace('__BUMPER_SVG__', bsvg).replace('__BUMPER_CSS__', bcss)
    open(out, 'w', encoding='utf-8').write(html)
    json.dump({'voice': vo, 'speed': speed, 'lines': lines, 'scenes': [max(0.0, round(l['start'] - lead, 3)) for l in lines], 'total': total, 'bumper': [din, dout]}, open(base + '.words.json', 'w'), ensure_ascii=False, indent=0)
    print(f"{out}: {len(scenes)} scenes, {total_t/60:.1f} min" + (f' (logo over the hook, end card over the last {OUTRO:g} s, {len(SFX)} sounds)' if bump else '') + f", {os.path.getsize(out)//1024} KB" + (' (silent draft)' if silent else f', voice {vo} at {speed:g}'))

if __name__ == '__main__':
    main(sys.argv[1:])
