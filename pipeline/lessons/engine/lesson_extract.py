#!/usr/bin/env python3
"""lesson_extract.py: take a built lesson apart so it can be rebuilt on a newer engine without re-recording the voice.

usage: lesson_extract.py built_lesson.html outdir [--as <name>_v2]

Writes into outdir:
  <sid>-u<N>-L<k>.js           the lesson source that was built into the page
  <name>.mp3                   the embedded audio (narration with the pill sounds already mixed in)
  <name>.words.json            the line and word timings, marked "premixed" so lesson_build.py --reuse does not mix the sounds again
Then: python3 lesson_build.py outdir/<sid>-u<N>-L<k>.js outdir/<name>.html --reuse
(<name> defaults to the built file's name with _v2 appended; the narration must stay unchanged for --reuse.)
"""
import base64, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        sys.exit(2)
    src_html, out = argv[0], argv[1]
    name = argv[argv.index('--as') + 1] if '--as' in argv else os.path.splitext(os.path.basename(src_html))[0] + '_v2'
    os.makedirs(out, exist_ok=True)
    h = open(src_html, encoding='utf-8').read()
    tpl = open(os.path.join(HERE, 'lesson_template.html'), encoding='utf-8').read()
    m = re.search(r'const DATA=(\{.*?\});\s*\n', h, flags=re.S)
    if not m:
        sys.exit('no DATA block: not a lesson built by lesson_build.py')
    data = json.loads(m.group(1))
    after = h[m.end():]
    t_after = tpl[tpl.index('const DATA=__DATA__;') + len('const DATA=__DATA__;'):]
    pre = t_after[:t_after.index('__LESSON__')].strip()
    post = t_after[t_after.index('__LESSON__') + len('__LESSON__'):].strip()[:60]
    start = after.index(pre) + len(pre) if pre else 0
    end = after.index(post, start)
    src = after[start:end].strip('\n') + '\n'
    meta = re.search(r"kick:\s*['\"]([^'\"]+)['\"]", src)
    key = re.match(r'(.+?-u\d+-L\d+)', os.path.basename(src_html))
    key = key.group(1) if key else os.path.splitext(os.path.basename(src_html))[0]
    open(os.path.join(out, key + '.js'), 'w', encoding='utf-8').write(src)
    a = re.search(r'src="data:audio/mpeg;base64,([^"]+)"', h)
    if not a:
        sys.exit('no embedded audio (a silent draft?)')
    open(os.path.join(out, name + '.mp3'), 'wb').write(base64.b64decode(a.group(1)))
    json.dump({'voice': 'af_heart', 'speed': 1.0, 'lines': data['lines'], 'total': data['dur'], 'premixed': True},
              open(os.path.join(out, name + '.words.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    print(f"{key}.js ({len(src)} chars), {name}.mp3, {name}.words.json: {len(data['lines'])} lines, {data['dur']:.1f} s"
          + (f" — {meta.group(1)}" if meta else ''))


if __name__ == '__main__':
    main(sys.argv[1:])
