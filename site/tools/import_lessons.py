#!/usr/bin/env python3
"""import_lessons.py: add lessons to site/data/lessons.json from the files the lesson pipeline already makes.

usage:  python3 site/tools/import_lessons.py <file> [<file> ...]

Each file may be either
  * the data pack's videos.json   (keys <subject id>-u<N>, each with its lessons: n, title, chapters, minutes, video;
                                   plus "playlists"), or
  * a subject's upload_sheet.json (a list of lessons with key, name, length and, once uploaded, a video id).

Existing entries are updated, never dropped. A video id already in lessons.json is kept when the new file has none.
Run site/build.py afterwards.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(os.path.dirname(HERE), 'data', 'lessons.json')
KEY = re.compile(r'^([a-z0-9-]+-u\d+)-L(\d+)$')


def minutes(length):
    m = re.match(r'^(\d+):(\d+)$', str(length or ''))
    return round(int(m.group(1)) + int(m.group(2)) / 60) if m else 0


def merge(data, topic, lesson):
    lessons = data.setdefault(topic, {}).setdefault('lessons', [])
    old = next((l for l in lessons if l.get('n') == lesson['n']), None)
    if old is None:
        lessons.append(lesson)
        lessons.sort(key=lambda l: l['n'])
        return 1
    for k, v in lesson.items():
        if v or k not in old:
            old[k] = v
    old.pop('notes', None)          # the lesson's place in the topic is now confirmed
    return 0


def main(paths):
    data = json.load(open(TARGET, encoding='utf8'))
    added = 0
    for p in paths:
        src = json.load(open(p, encoding='utf8'))
        if isinstance(src, dict):                       # videos.json
            data.setdefault('playlists', {}).update({k: v for k, v in src.get('playlists', {}).items() if v})
            for topic, v in src.items():
                if isinstance(v, dict) and 'lessons' in v:
                    for l in v['lessons']:
                        added += merge(data, topic, {'n': l['n'], 'title': l.get('title', ''), 'chapters': str(l.get('chapters', '')),
                                                     'minutes': round(l.get('minutes') or 0), 'video': l.get('video', '')})
        else:                                           # upload_sheet.json
            for e in src:
                m = KEY.match(e.get('key', ''))
                if m:
                    added += merge(data, m.group(1), {'n': int(m.group(2)), 'title': e.get('name', ''), 'chapters': str(e.get('chapters', '')),
                                                      'minutes': minutes(e.get('length')), 'video': e.get('video', '')})
    json.dump(data, open(TARGET, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    total = sum(len(v['lessons']) for v in data.values() if isinstance(v, dict) and 'lessons' in v)
    print('added %d new lesson(s); lessons.json now holds %d' % (added, total))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1:])
