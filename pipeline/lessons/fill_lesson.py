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

def main():
    path = sys.argv[1]; rounds = int(sys.argv[sys.argv.index('--rounds') + 1]) if '--rounds' in sys.argv else 4
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
