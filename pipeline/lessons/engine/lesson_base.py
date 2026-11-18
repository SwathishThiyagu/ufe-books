#!/usr/bin/env python3
"""lesson_base.py: get a built lesson ready for lesson_build.py --revoice when its narration mp3 was not kept.

usage: lesson_base.py built_lesson.html out_stem
Writes out_stem.mp3 (the page's embedded audio, which has the end-card sounds in it) and out_stem.words.json (the page's
line timings, marked "premixed", so --revoice voices again the lines under the end-card sounds and the build mixes the
sounds in once). The page must have been built with no bumper padding (BUMPER_IN = 0), as every lesson since engine v4.6.
"""
import base64, json, re, sys
h = open(sys.argv[1], encoding='utf-8').read()
m = re.search(r'const DATA=(\{.*?\});\s*\n', h, flags=re.S)
a = re.search(r'src="data:audio/mpeg;base64,([^"]+)"', h)
if not (m and a): sys.exit('not a lesson built by lesson_build.py, or a silent draft')
data = json.loads(m.group(1))
if data['lines'] and data['lines'][0]['start'] > 3: sys.exit('the first line starts late: this page has bumper padding; use lesson_extract.py and a full re-voice')
vo = re.search(r'voice (\w+) at ([\d.]+)', h)
open(sys.argv[2] + '.mp3', 'wb').write(base64.b64decode(a.group(1)))
json.dump({'voice': 'af_heart', 'speed': 1.0, 'lines': data['lines'], 'total': data['dur'], 'premixed': True},
          open(sys.argv[2] + '.words.json', 'w', encoding='utf-8'), ensure_ascii=False)
print(f"{sys.argv[2]}.mp3 and .words.json: {len(data['lines'])} lines, {data['dur']:.1f} s, premixed")
