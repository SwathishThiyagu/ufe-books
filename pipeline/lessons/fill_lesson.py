#!/usr/bin/env python3
"""Fill a book2lesson.py lesson file with a model (DeepSeek by default), then fix it until lesson_build.py --check is clean.

usage: fill_lesson.py lesson.js [--rounds 4]
Needs OPENAI_BASE_URL / OPENAI_API_KEY / OPENAI_MODEL (see pipeline/llm.py). Writes lesson.js in place and lesson.log."""
import os, sys, re, subprocess, json, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from llm import OpenAICompat
ENG = os.path.join(HERE, 'engine')

def check(path):
    r = subprocess.run([sys.executable, os.path.join(ENG, 'lesson_build.py'), path, path + '.html', '--check'], capture_output=True, text=True)
    out = r.stdout + r.stderr
    probs = [l[3:] for l in out.splitlines() if l.startswith(' - ')]
    return probs, out

def strip_fences(t):
    t = t.strip()
    m = re.search(r'```(?:js|javascript)?\s*\n(.*?)```', t, re.S)
    return (m.group(1) if m else t).strip() + '\n'

SYSTEM = ("You fill University free n easy video-lesson files: JavaScript objects that a fixed engine turns into a voiced, animated HTML lesson "
          "for Indian B.Tech students. Follow the rules exactly. Reply with the complete JavaScript file only, no explanation.")

PICS = """Redraw ONLY the pictures in this lesson file: every vis:(c,u,box)=>`...` (notebook and traps panels, 640 x 690), every wv/rv
(trap cards, 640 x 330 each), the pa.vis answer pictures and the hook art. Each picture must show the line it sits beside, as a
real diagram a teacher would draw: labelled axes and curves for training loss, a stepped path down a bowl for gradient descent,
batches as rows of sample boxes, arrows for updates, before/after side by side. Fill the box (no tiny shapes in a corner), use
large text (24 px or more), the colour names the file already uses (RED, GRN, TRED, var(--fig)...), and animate parts on their
item's cue the way the file's helpers do (g('pop', tk(c,'i1'), ...)). Keep every say, cues, title, text line, number and the
rest of the file exactly as it is: change nothing but the picture functions. Return the whole file."""

def pictures(path, rounds):
    logf = open(path + '.log', 'a')
    def log(m): print(m, flush=True); logf.write(m + '\n'); logf.flush()
    ask = OpenAICompat.from_env(log)
    rules = open(os.path.join(os.path.dirname(path), 'WRITE.md')).read()
    kinds = open(os.path.join(ENG, 'lesson_kinds.md')).read()
    src = open(path).read()
    say_of = lambda t: re.findall(r"say:(['`])(.*?)(?<!\\)\1", t, re.S)
    before = say_of(src)
    prompt = f"RULES:\n{rules}\n\nSCENE KINDS:\n{kinds}\n\n{PICS}\n\nTHE FILE:\n{src}"
    for r in range(rounds + 1):
        new = strip_fences(ask.text(f'pictures{r}', SYSTEM, prompt, json_mode=False, temperature=0.4))
        if 'META' not in new or len(new) < len(src) * 0.6:
            log(f'pictures {r}: reply is not the whole file'); continue
        if say_of(new) != before:
            log(f'pictures {r}: the narration changed; asking again'); prompt += '\n\nYour last reply changed the narration (say). Keep every say exactly as it is.'; continue
        open(path + '.new', 'w').write(new)
        probs, raw = check(path + '.new')
        log(f'pictures {r}: {len(probs)} problem(s) ' + ' | '.join(probs[:6]))
        if not probs:
            os.replace(path + '.new', path); log('PICTURES CLEAN'); return 0
        prompt = f"RULES:\n{rules}\n\nSCENE KINDS:\n{kinds}\n\n{PICS}\n\nYour redrawn file fails these checks; fix them and return the whole file:\n- " + '\n- '.join(probs[:20]) + f"\n\nTHE FILE:\n{new}"
    return 1

def main():
    path = sys.argv[1]
    if '--pictures' in sys.argv: return pictures(path, int(sys.argv[sys.argv.index('--rounds') + 1]) if '--rounds' in sys.argv else 3); rounds = int(sys.argv[sys.argv.index('--rounds') + 1]) if '--rounds' in sys.argv else 4
    logf = open(path + '.log', 'a')
    def log(m): print(m, flush=True); logf.write(m + '\n'); logf.flush()
    ask = OpenAICompat.from_env(log)
    rules = open(os.path.join(os.path.dirname(path), 'WRITE.md')).read()
    kinds = open(os.path.join(ENG, 'lesson_kinds.md')).read()
    pron = sorted(json.load(open(os.path.join(ENG, 'pronunciation.json'))).keys())
    src = open(path).read()
    prompt = (f"RULES (WRITE.md):\n{rules}\n\nSCENE KINDS (lesson_kinds.md):\n{kinds}\n\nWords already in pronunciation.json (use ${{P('word')}} for them): "
              f"{', '.join(pron[:400])}\n\nTHE LESSON FILE TO FILL. Replace every TODO, keep all the book content and structure, write every number in "
              f"`say` as words, add the required vis/wv/rv pictures, and return the whole file:\n\n{src}")
    for r in range(rounds + 1):
        out = ask.text(f'lesson{r}', SYSTEM, prompt, json_mode=False, temperature=0.5)
        new = strip_fences(out)
        if 'META' not in new or len(new) < len(src) * 0.6:
            log(f'round {r}: reply does not look like the whole file ({len(new)} chars); asking again'); continue
        open(path, 'w').write(new); src = new
        probs, raw = check(path)
        log(f'round {r}: {len(probs)} problem(s) ' + ' | '.join(probs[:6]))
        if not probs: log('CLEAN'); return 0
        prompt = (f"RULES (WRITE.md):\n{rules}\n\nSCENE KINDS:\n{kinds}\n\nThe lesson file below fails these checks; fix every one and return the whole file:\n- "
                  + '\n- '.join(probs[:30]) + f"\n\nTHE FILE:\n{src}")
    return 1

if __name__ == '__main__':
    sys.exit(main())
