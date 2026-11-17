"""Claude's hand-drawn figures for c-mobile-u4 (Mobile Application Development, unit 4: data storage and sharing),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def codebox(x, y, w, lines, fill=PANEL, stroke=AC, size=13, lh=20, title=None):
    h = len(lines) * lh + 16 + (22 if title else 0)
    o = [R(x, y, w, h, fill, stroke, 8, 2)]
    y0 = y + 22
    if title:
        o.append(T(x + 12, y0, title, 14, 'start', bold=True)); y0 += 22
    for i, s in enumerate(lines):
        o.append(TM(x + 12, y0 + i * lh, s, size, 'start'))
    return ''.join(o), h


# ---- 4.1 two settings saved and read back ----
def f1():
    o = [T(16, 24, 'Save two settings, restart the app, read them back', 15, 'start', bold=True)]
    s, h = codebox(16, 44, 300, ['editor.putInt("best_score", 4200)', 'editor.putBoolean("sound_on", false)', 'editor.apply()'], title='write')
    o.append(s)
    o.append(L(318, 90, 352, 90, AC, 2, arrow='n'))
    s, h2 = codebox(356, 44, 348, ['<int name="best_score" value="4200" />'.replace('<', '&lt;').replace('>', '&gt;'),
                                    '<boolean name="sound_on" value="false" />'.replace('<', '&lt;').replace('>', '&gt;')],
                    LVS, LV, 12, title='shared_prefs/settings.xml')
    o.append(s)
    o.append(T(530, 44 + h2 + 18, 'one private XML file in /data/data/<pkg>/'.replace('<', '&lt;').replace('>', '&gt;'), 12, fill=MUT))
    o.append(R(16, 190, 688, 30, 'var(--fig)', L2, 6, 1.5, '6 4'))
    o.append(T(360, 210, 'app closed and opened again: the file stays', 13, fill=MUT))
    o.append(L(530, 44 + h2 + 26, 530, 236, LV, 2, arrow='l'))
    s, h3 = codebox(16, 242, 420, ['prefs.getInt("best_score", 0)', 'prefs.getBoolean("sound_on", true)'], title='read (same keys, a default each)')
    o.append(s)
    o.append(L(438, 282, 470, 282, AC, 2, arrow='n'))
    o.append(boxt(474, 250, 230, 64, ['4200', 'false'], ACS, AC, 15, bold_first=False))
    o.append(T(16, 338, 'The defaults 0 and true are used only if a key is missing.', 14, 'start', MUT))
    return 352, ''.join(o)
FIG[1] = (f1, 'putInt and putBoolean write best_score = 4200 and sound_on = false, and apply() saves them into settings.xml. After a restart, getInt and getBoolean with the same keys read 4200 and false back.',
          'Three steps: a write box with putInt, putBoolean and apply; the settings.xml file holding the int 4200 and the boolean false; a read box with getInt and getBoolean returning 4200 and false.')


# ---- 4.2 where each file goes ----
def f2():
    o = [T(16, 24, 'Choose the folder by what the file is', 15, 'start', bold=True)]
    o.append(R(16, 44, 420, 214, PANEL, AC, 10, 2))
    o.append(TM(30, 70, '/data/data/<pkg>/'.replace('<', '&lt;').replace('>', '&gt;'), 14, 'start', bold=True))
    o.append(T(422, 70, 'internal, private', 13, 'end', AC))
    o.append(R(34, 86, 384, 64, ACS, AC, 6, 1.5))
    o.append(TM(46, 110, 'files/log.txt', 13, 'start', bold=True)); o.append(T(406, 110, 'getFilesDir()', 13, 'end', MUT))
    o.append(T(46, 136, '3 lines × 32 B = 96 B', 14, 'start'))
    o.append(R(34, 160, 384, 64, ACS, AC, 6, 1.5))
    o.append(TM(46, 184, 'cache/thumb', 13, 'start', bold=True)); o.append(T(406, 184, 'getCacheDir()', 13, 'end', MUT))
    o.append(T(46, 210, '40 KB × 1024 = 40,960 B (can be rebuilt)', 14, 'start'))
    o.append(T(30, 248, 'total 96 + 40,960 = 41,056 B; uninstall deletes both', 13, 'start', NX, True))
    # external
    o.append(R(470, 44, 234, 214, LVS, LV, 10, 2, '6 4'))
    o.append(T(587, 70, 'app external folder', 14, bold=True))
    o.append(TM(587, 96, 'getExternalFilesDir(null)', 12))
    o.append(T(587, 132, '5 MB log', 15, bold=True))
    o.append(T(587, 166, 'first check', 13, fill=MUT))
    o.append(TM(587, 186, 'getExternalStorageState()', 12))
    o.append(TM(587, 206, '== MEDIA_MOUNTED', 12, fill=LV, bold=True))
    o.append(T(587, 238, 'may be absent or unmounted', 12, fill=MUT))
    return 270, ''.join(o)
FIG[2] = (f2, 'The 96-byte log goes to files/ and the 40,960-byte thumbnail to cache/, both private under /data/data/<pkg>, 41,056 bytes in all and both deleted on uninstall. A 5 MB log can go to the app\'s external folder once the storage reports MEDIA_MOUNTED.',
          'A private folder box holding files/log.txt of 96 bytes and cache/thumb of 40,960 bytes, total 41,056 bytes; beside it a dashed external folder box for a 5 MB log, reached only after the MEDIA_MOUNTED check.')


# ---- 4.3 the query, step by step ----
def table(x, y, rows, hl=None, title=None, widths=(50, 90, 70)):
    o = []
    if title: o.append(T(x, y - 10, title, 13, 'start', MUT, True))
    hd = ['_id', 'name', 'marks']
    xx = x
    for j, wd in enumerate(widths):
        o.append(R(xx, y, wd, 26, 'var(--panel)', L2, 0, 1)); o.append(T(xx + wd / 2, y + 18, hd[j], 13, bold=True)); xx += wd
    for i, r in enumerate(rows):
        xx = x
        for j, wd in enumerate(widths):
            o.append(R(xx, y + 26 + i * 26, wd, 26, ACS if hl and i in hl else 'var(--fig)', L2, 0, 1))
            o.append(T(xx + wd / 2, y + 44 + i * 26, str(r[j]), 13)); xx += wd
    return ''.join(o)


def f3():
    rows = [(1, 'Asha', 88), (2, 'Ravi', 72), (3, 'Meera', 95)]
    o = [T(16, 24, 'SELECT _id, name, marks FROM students WHERE marks > 60 ORDER BY marks DESC', 14, 'start', bold=True)]
    o.append(table(16, 66, rows, title='inserted'))
    o.append(L(230, 118, 262, 118, AC, 2, arrow='n')); o.append(Tb(246, 106, '> 60', 12, fill=AC, bold=True))
    o.append(table(266, 66, rows, hl=[0, 1, 2], title='all 3 kept'))
    o.append(L(480, 118, 512, 118, AC, 2, arrow='n')); o.append(Tb(496, 106, 'DESC', 12, fill=AC, bold=True))
    srt = sorted(rows, key=lambda r: -r[2])
    o.append(table(516, 66, srt, title='sorted 95, 88, 72', widths=(46, 84, 58)))
    # cursor walk
    y = 210
    o.append(T(16, y, 'The Cursor, read with while (cursor.moveToNext())', 14, 'start', bold=True))
    calls = [('1st', '3, Meera, 95'), ('2nd', '1, Asha, 88'), ('3rd', '2, Ravi, 72'), ('4th', 'false: loop ends')]
    for i, (n, v) in enumerate(calls):
        x = 16 + i * 174
        last = i == 3
        o.append(R(x, y + 14, 160, 52, NXS if last else LVS, NX if last else LV, 8, 2))
        o.append(T(x + 80, y + 34, f'{n} moveToNext()', 13, bold=True))
        o.append(T(x + 80, y + 54, v, 13))
        if i < 3: o.append(L(x + 162, y + 40, x + 172, y + 40, L2, 2))
    o.append(T(16, y + 96, 'getCount() = 3.   Same query via the helper: query("students", null, "marks > ?", {"60"}, null, null, "marks DESC")', 13, 'start'))
    return y + 112, ''.join(o)
FIG[3] = (f3, 'All three rows pass marks > 60, and ORDER BY marks DESC puts them in the order Meera 95, Asha 88, Ravi 72. The cursor hands them out one per moveToNext(); the fourth call returns false, and getCount() is 3.',
          'Three small tables: the three inserted rows, the same rows kept by the filter, and the rows sorted by marks highest first; below, four cursor steps returning Meera, Asha, Ravi and then false.')


# ---- 4.4 one URI through the provider ----
def f4():
    o = [T(16, 24, 'getContentResolver().query(content://com.example.marks/students/2, ...)', 14, 'start', bold=True)]
    parts = [('content://', 'scheme', PANEL, L2), ('com.example.marks', 'authority', ACS, AC), ('/students', 'table', LVS, LV), ('/2', 'row id', NXS, NX)]
    x = 60
    for s, lab, f, st in parts:
        w = len(s) * 15 * 0.62 + 18
        o.append(R(x, 46, w, 34, f, st, 4, 1.5)); o.append(TM(x + w / 2, 68, s, 15, bold=True))
        o.append(T(x + w / 2, 98, lab, 13, fill=MUT)); x += w + 4
    # matcher
    y = 124
    o.append(R(16, y, 330, 104, PANEL, AC, 8, 2))
    o.append(T(30, y + 24, 'UriMatcher', 14, 'start', bold=True))
    o.append(TM(30, y + 50, '"students"   → 1  (many rows)', 13, 'start', MUT))
    o.append(R(24, y + 62, 314, 26, ACS, AC, 4, 1.5))
    o.append(TM(30, y + 80, '"students/#" → 2  (one row)  ✓', 13, 'start', bold=True))
    o.append(L(348, y + 75, 380, y + 75, AC, 2, arrow='n'))
    o.append(R(384, y, 320, 104, PANEL, AC, 8, 2))
    o.append(T(398, y + 24, 'code 2 runs', 14, 'start', bold=True))
    o.append(TM(398, y + 50, 'db.query("students", null,', 13, 'start'))
    o.append(TM(398, y + 70, '  "_id = ?", {"2"}, ...)', 13, 'start'))
    o.append(L(544, y + 106, 544, y + 132, LV, 2, arrow='l'))
    y = 262
    o.append(T(384, y + 80, 'Cursor back to the caller: 1 row', 13, 'start', LV, True))
    o.append(table(384, y + 8, [(2, 'Ravi', 72)], widths=(70, 140, 110)))
    o.append(T(16, y + 26, 'getType():', 13, 'start', bold=True))
    o.append(TM(16, y + 48, 'vnd.android.cursor.item/', 13, 'start'))
    o.append(TM(16, y + 68, '  com.example.marks.students', 13, 'start'))
    o.append(T(16, y + 92, 'item, because the URI names one row', 13, 'start', MUT))
    return y + 104, ''.join(o)
FIG[4] = (f4, 'The URI splits into scheme, authority, table and row id. Its path students/2 matches the pattern students/#, code 2, so the provider queries SQLite for _id = 2 and the caller gets a one-row Cursor, Ravi with 72, typed as an item.',
          'The URI content://com.example.marks/students/2 split into four coloured parts; a UriMatcher box picks code 2; a query box asks for _id 2; a one-row table returns Ravi, 72, with the item MIME type beside it.')


# ---- 4.5 one temporary read grant ----
def f5():
    o = [T(16, 24, 'Sharing report.pdf (1.5 MB = 1,572,864 bytes) with a PDF viewer', 15, 'start', bold=True)]
    o.append(R(16, 46, 220, 96, PANEL, AC, 8, 2))
    o.append(T(30, 70, 'report app (private)', 14, 'start', bold=True))
    o.append(TM(30, 96, 'files/reports/', 13, 'start')); o.append(TM(46, 118, 'report.pdf', 13, 'start', bold=True))
    o.append(L(238, 94, 266, 94, AC, 2, arrow='n'))
    o.append(R(270, 46, 434, 96, ACS, AC, 8, 2))
    o.append(T(284, 70, 'FileProvider.getUriForFile(...)', 13, 'start', bold=True))
    o.append(TM(284, 98, 'content://com.example.reportapp', 13, 'start'))
    o.append(TM(284, 118, '  .fileprovider/reports/report.pdf', 13, 'start'))
    # intent
    o.append(L(487, 144, 487, 166, AC, 2, arrow='n'))
    o.append(R(270, 170, 434, 96, PANEL, AC, 8, 2))
    o.append(T(284, 194, 'Intent', 14, 'start', bold=True))
    o.append(TM(284, 216, 'ACTION_SEND, type application/pdf', 12, 'start'))
    o.append(TM(284, 234, 'EXTRA_STREAM = that URI', 12, 'start'))
    o.append(TM(284, 252, 'FLAG_GRANT_READ_URI_PERMISSION', 12, 'start', LV, True))
    o.append(L(268, 218, 242, 218, AC, 2, arrow='n'))
    o.append(boxt(16, 186, 222, 64, ['createChooser', '"Share report"'], PANEL, L2, 13))
    o.append(L(127, 252, 127, 290, AC, 2, arrow='n'))
    o.append(R(16, 294, 688, 92, LVS, LV, 8, 2))
    o.append(T(30, 318, 'PDF viewer', 14, 'start', bold=True))
    o.append(T(30, 342, '✓ openInputStream(uri) reads exactly 1,572,864 bytes of this one file', 14, 'start', LV))
    o.append(T(30, 366, '✗ cannot list reports/, cannot write; the grant ends with the receiving activity', 14, 'start', NX))
    return 400, ''.join(o)
FIG[5] = (f5, 'FileProvider turns the private report.pdf into a content URI; an ACTION_SEND intent carries it with FLAG_GRANT_READ_URI_PERMISSION through the chooser. The viewer may read the 1,572,864 bytes of that one file, and nothing else.',
          'A private folder holding report.pdf; an arrow to FileProvider making a content URI; an intent box with ACTION_SEND, the URI and the read flag; a chooser; and the viewer, which can read the file but cannot list the folder or write.')


# ---- 4.6 one ObservableInt change ----
def f6():
    o = [T(16, 24, 'Data binding: change the object, and only the bound view redraws', 15, 'start', bold=True)]
    s, h = codebox(16, 44, 250, ['name = "Asha"', 'score = ObservableInt(88)'], title='User object')
    o.append(s)
    s, h2 = codebox(16, 156, 250, ['@{user.name}', '@{String.valueOf(user.score)}'], LVS, LV, title='activity_main.xml')
    o.append(s)
    o.append(T(16, 266, 'binding.setUser(user)', 13, 'start', MUT))
    def scr(x, a, b, hb):
        r = R(x, 50, 150, 200, PANEL, INK, 12, 2) + R(x + 10, 68, 130, 168, 'var(--fig)', L2, 4, 1)
        r += R(x + 20, 90, 110, 40, PANEL, L2, 4, 1) + T(x + 75, 116, a, 16, bold=True)
        r += R(x + 20, 150, 110, 40, ACS if hb else PANEL, AC if hb else L2, 4, 2 if hb else 1) + T(x + 75, 176, b, 16, bold=True)
        return r
    o.append(L(270, 120, 302, 140, AC, 2, arrow='n')); o.append(L(270, 200, 302, 180, LV, 2, arrow='l'))
    o.append(scr(306, 'Asha', '88', False))
    o.append(T(381, 274, 'first screen', 13, fill=MUT))
    o.append(L(460, 170, 534, 170, NX, 2.5, arrow='x'))
    o.append(T(497, 150, 'tap +7', 13, fill=NX, bold=True))
    o.append(TM(497, 196, 'score.set(95)', 12, fill=NX))
    o.append(scr(554, 'Asha', '95', True))
    o.append(T(629, 274, 'only the score view redrawn', 13, fill=AC))
    o.append(T(16, 306, 'No findViewById and no setText: 88 + 7 = 95 reaches the screen because ObservableInt notifies the binding.', 14, 'start'))
    return 320, ''.join(o)
FIG[6] = (f6, 'setUser fills the two TextViews with Asha and 88. One tap runs score.set(95); the ObservableInt tells the binding, which redraws only the score view, while the name view keeps Asha.',
          'A User object and a layout with two binding expressions feed a phone showing Asha and 88; after score.set(95) a second phone shows Asha and 95 with only the score view highlighted.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        1: [('In SharedPreferences the key is a String, and the value is a String, int, boolean, long or float.',
             'In SharedPreferences the key is a String, and the value is a String, int, boolean, long or float, or a Set of Strings through putStringSet.'),
            ('String, int, boolean, long and float are the five simple types.',
             'String, int, boolean, long and float are the five simple types; a Set of Strings (putStringSet) is the one collection allowed.'),
            ('For secrets, EncryptedSharedPreferences wraps the same key-value idea with encryption keys held by the Android Keystore. Search for DataStore Preferences, EncryptedSharedPreferences, and Android Keystore to see the newer APIs.',
             'For secrets, EncryptedSharedPreferences once wrapped the same key-value idea with encryption, but its library is now deprecated; keys belong in the Android Keystore. Search for DataStore Preferences and Android Keystore to see the newer APIs.')],
        2: [(' Only a few universities teach the mode flags and scoped-storage rules at this depth.', '')],
        4: [('Creating one is advanced; only a few universities teach it.', 'Creating one is the advanced part.')],
        5: [(' Only a few universities teach this advanced topic.', '')],
        6: [(' Only a few universities teach this topic; most stop at findViewById.', '')],
    }.get(k, [])


def chapter_fix(k, ch):
    # the example database was named after a college; the books name no colleges
    if k == 3:
        ch = json.loads(json.dumps(ch, ensure_ascii=False).replace('college.db', 'marks.db'))
    return ch


# sentences removed outright go through chapter_fix, which is idempotent, so the module can be applied again
_tf_all = text_fixes
_cf_prev = globals().get('chapter_fix')


def text_fixes(k):
    return [(a, b) for a, b in _tf_all(k) if b]


def chapter_fix(k, ch):
    import json
    if _cf_prev: ch = _cf_prev(k, ch) or ch
    raw = json.dumps(ch, ensure_ascii=False)
    for a, b in _tf_all(k):
        if not b: raw = raw.replace(json.dumps(a, ensure_ascii=False)[1:-1], '')
    return json.loads(raw)
