#!/usr/bin/env python3
"""rail_patch.py: engine v4.6 fix for HTML-to-video converters. The section rail (PART 1 ... PRACTICE, top right) sits under the channel
logo; v4.1-v4.5 hid it with a CSS class toggled while the logo shows, which some converters do not apply, so in the video the logo
covered the rail. v4.6 leaves the rail out of the scene's own drawing for every scene the logo overlaps (the hook, the outro), so any
converter shows the same frame as the page. Works on the template and on built lessons (the engine is embedded): python3 rail_patch.py <file.html> [...]"""
import sys
OLD_FN = "function wayfinder(sc){if(sc.wf===false)return '';"
NEW_FN = ("/* v4.6: the rail is left out of every scene the logo overlaps (hook, outro), in the drawing itself, so a converter that ignores the logo-on class still shows no rail under the logo */\n"
          "function logoOver(i){const B=window.__bumper,T0=(window.__T||[])[i],T1=(window.__END||[])[i],TT=window.__TOTAL||0;return !!(B&&T0!=null&&((B.INTRO&&T0<B.INTRO)||(B.DUR_OUT&&T1>TT-B.DUR_OUT)))}\n"
          "function wayfinder(sc,i){if(sc.wf===false)return '';")
OLD_RAIL = " s+='<g class=\"rail\">';"
NEW_RAIL = " if(i!=null&&logoOver(i))return s+'</g>';s+='<g class=\"rail\">';"
OLD_CALL = "svg+=wayfinder(sc)}"
NEW_CALL = "svg+=wayfinder(sc,i)}"
def patch(s):
    if 'function logoOver(i)' in s:
        return s, 'already'
    for a in (OLD_FN, OLD_RAIL, OLD_CALL):
        if s.count(a) != 1:
            return s, f'not patched: found {s.count(a)} of {a[:40]!r}'
    return s.replace(OLD_FN, NEW_FN).replace(OLD_RAIL, NEW_RAIL).replace(OLD_CALL, NEW_CALL), 'patched'
if __name__ == '__main__':
    for p in sys.argv[1:]:
        s = open(p, encoding='utf8').read(); n, st = patch(s)
        if st == 'patched':
            open(p, 'w', encoding='utf8').write(n)
        print(p, st)
