"""Claude's hand-drawn figures for c-mobile-u2 (Mobile Application Development, unit 2: Android platform, project,
activities, intents and fragments), one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def chip(x, y, s, w=None, fill=ACS, stroke=AC, size=13, h=24, mono=True):
    w = w or tw(s, size) + 16
    t = TM(x + w / 2, y + h / 2 + size * 0.35, s, size) if mono else T(x + w / 2, y + h / 2 + size * 0.35, s, size)
    return R(x, y, w, h, fill, stroke, 5, 1.5) + t, w


# ---- 2.1 one to-do app, three platforms ----
def f1():
    cols = [('Android', ['Java or Kotlin', 'Android Studio + Gradle', 'Google Play', 'any Windows, macOS', 'or Linux PC'], ACS, AC, 'ships'),
            ('iOS', ['Swift', 'Xcode', 'App Store', 'needs a Mac', '(Xcode runs only there)'], ACS, AC, 'ships'),
            ('Windows Phone', ['C# + XAML', 'Visual Studio', 'Microsoft Store', 'platform retired:', 'no new devices'], PANEL, L2, 'dropped')]
    rows = ['language', 'build tool', 'store', 'extra need']
    o = [T(16, 24, 'The same to-do app, planned for three platforms', 15, 'start', bold=True)]
    x0, w, gap = 130, 186, 12
    for i, r in enumerate(rows):
        o.append(T(x0 - 12, 92 + i * 40 + (8 if i == 3 else 0), r, 14, 'end', MUT))
    for j, (name, vals, f, s, fate) in enumerate(cols):
        x = x0 + j * (w + gap)
        o.append(R(x, 40, w, 236, f, s, 10, 2, None if fate == 'ships' else '6 4'))
        o.append(T(x + w / 2, 64, name, 15, bold=True, fill=INK if fate == 'ships' else MUT))
        for i, v in enumerate(vals[:3]):
            o.append(T(x + w / 2, 97 + i * 40, v, 14, fill=INK if fate == 'ships' else MUT))
        o.append(T(x + w / 2, 214, vals[3], 13, fill=NX if j == 1 else (MUT if j == 2 else INK), bold=(j == 1)))
        o.append(T(x + w / 2, 232, vals[4], 13, fill=NX if j == 1 else MUT))
        o.append(boxt(x + w / 2 - 50, 290, 100, 30, [fate], LVS if fate == 'ships' else 'var(--fig)', LV if fate == 'ships' else L2, 14, bold_first=True))
        o.append(L(x + w / 2, 278, x + w / 2, 288, LV if fate == 'ships' else L2, 2))
    o.append(T(16, 352, 'Platforms still developed: 3 − 1 = 2, so the app is written twice, in Kotlin/Java and in Swift.', 14, 'start'))
    return 368, ''.join(o)
FIG[1] = (f1, 'Each platform fixes a language, a build tool and a store. Windows Phone is retired, so 3 − 1 = 2 builds ship: Android, buildable on any PC, and iOS, which needs a Mac because Xcode runs only on macOS.',
          'Three columns, Android, iOS and Windows Phone, listing language, build tool, store and extra need; Android and iOS are marked ships, the dashed Windows Phone column is marked dropped.')


# ---- 2.2 the three numbers on the API-level line ----
def f2():
    o = [T(16, 24, 'build.gradle: compileSdk 34, minSdk 24, targetSdk 34. A tester\'s phone is at API 21.', 15, 'start', bold=True)]
    x0, x1, y = 50, 690, 170
    fx = lambda a: x0 + (a - 19) / (35 - 19) * (x1 - x0)
    o.append(R(fx(24), y - 26, fx(35) - fx(24), 26, LVS, LV, 3, 1.5))
    o.append(T((fx(24) + fx(35)) / 2, y - 8, 'phones at API 24 and above may install', 13, fill=LV, bold=True))
    o.append(L(x0, y, x1, y, L2, 2))
    for a in range(19, 36):
        o.append(L(fx(a), y, fx(a), y + 6, L2, 1.5))
        if a % 2 == 1 or a in (24, 34): o.append(T(fx(a), y + 22, str(a), 13, fill=MUT))
    o.append(T((x0 + x1) / 2, y + 44, 'API level', 13, fill=MUT))
    # minSdk
    o.append(L(fx(24), y - 70, fx(24), y + 4, LV, 3))
    o.append(boxt(fx(24) - 58, y - 118, 116, 46, ['minSdk 24', 'who may install'], LVS, LV, 13, bold_first=True))
    # compile/target
    o.append(L(fx(34), y - 70, fx(34), y + 4, AC, 3))
    o.append(boxt(fx(34) - 150, y - 128, 160, 56, ['compileSdk 34', 'targetSdk 34'], ACS, AC, 13, bold_first=False))
    # phone at 21
    o.append(L(fx(21), y - 4, fx(21), y - 40, NX, 3))
    o.append(C(fx(21), y - 46, 8, NX))
    o.append(T(fx(21), y - 62, 'phone: API 21', 14, fill=NX, bold=True))
    o.append(P([(fx(21), y + 58), (fx(21), y + 66), (fx(24), y + 66), (fx(24), y + 58)], NX, 2))
    o.append(T((fx(21) + fx(24)) / 2, y + 86, '24 − 21 = 3 levels short', 14, fill=NX, bold=True))
    o.append(T(16, y + 120, 'Install on the API 21 phone: refused, INSTALL_FAILED_OLDER_SDK; on Google Play the app is hidden.', 14, 'start', NX))
    o.append(T(16, y + 146, 'compileSdk 34: the classes the build type-checks against.   targetSdk 34: the behaviour the app opts into.', 14, 'start'))
    o.append(T(16, y + 168, 'Neither of those two decides who may install; only minSdk does.', 14, 'start', MUT))
    return y + 182, ''.join(o)
FIG[2] = (f2, 'On the API-level line, minSdk 24 is the install floor; the tester\'s API 21 phone sits 24 − 21 = 3 levels below it, so the install fails with INSTALL_FAILED_OLDER_SDK. compileSdk 34 and targetSdk 34 do not change who may install.',
          'A number line of API levels 19 to 35; a shaded band from 24 upward marks phones that may install; markers show minSdk 24, compileSdk and targetSdk 34, and a phone at 21, three levels short.')


# ---- 2.3 HelloApp: the two edited files and R ----
def f3():
    o = [T(16, 24, 'HelloApp: edit two files, and AAPT2 turns them into R constants', 15, 'start', bold=True)]
    tree = [(0, 'app/', None), (1, 'manifests/AndroidManifest.xml', 'MAIN + LAUNCHER'), (1, 'java/com.example.hello/', None),
            (2, 'MainActivity.java', 'unchanged'), (1, 'res/layout/activity_main.xml', 'edit 1'), (1, 'res/values/strings.xml', 'edit 2'),
            (1, 'build.gradle', None)]
    y = 58
    for i, (d, name, tag) in enumerate(tree):
        x = 24 + d * 22
        yy = y + i * 34
        if d: o.append(P([(x - 14, yy - 22), (x - 14, yy - 4), (x - 4, yy - 4)], L2, 1.5))
        edited = tag and tag.startswith('edit')
        if edited: o.append(R(x - 2, yy - 18, len(name) * 13 * 0.62 + 10, 24, ACS, AC, 4, 1.5))
        o.append(TM(x + 2, yy - 1, name, 13, 'start', INK, bold=edited))
        if tag: o.append(T(342, yy - 1, tag, 13, 'start', AC if edited else MUT, edited))
    # the two edits
    o.append(boxt(16, 310, 300, 52, ['strings.xml: greeting = Hello, Chennai'], PANEL, AC, 13))
    o.append(boxt(16, 372, 300, 52, ['TextView id text1, text @string/greeting'], PANEL, AC, 13))
    o.append(L(320, 336, 394, 316, AC, 2, arrow='n')); o.append(L(320, 398, 394, 346, AC, 2, arrow='n'))
    o.append(Tb(356, 304, 'AAPT2', 13, fill=AC, bold=True))
    for i, s in enumerate(['R.string.greeting', 'R.id.text1', 'R.layout.activity_main']):
        o.append(R(398, 300 + i * 32, 186, 26, LVS, LV, 5, 1.5)); o.append(TM(491, 318 + i * 32, s, 13))
    # phone
    o.append(R(600, 210, 104, 196, PANEL, INK, 14, 2))
    o.append(R(608, 230, 88, 156, 'var(--fig)', L2, 4, 1))
    o.append(T(652, 262, 'Hello,', 14, bold=True)); o.append(T(652, 280, 'Chennai', 14, bold=True))
    o.append(L(586, 376, 606, 320, LV, 2, arrow='l'))
    o.append(T(652, 426, 'setContentView', 12, fill=MUT)); o.append(T(652, 442, 'inflates the layout', 12, fill=MUT))
    o.append(T(16, 450, 'Files edited: 2.  The template already calls setContentView(R.layout.activity_main).', 14, 'start'))
    return 464, ''.join(o)
FIG[3] = (f3, 'Only strings.xml and activity_main.xml change. AAPT2 turns them into R.string.greeting, R.id.text1 and R.layout.activity_main, and the template\'s setContentView call shows Hello, Chennai with no Java edit; the manifest\'s MAIN and LAUNCHER let the icon open it.',
          'A project tree with strings.xml and activity_main.xml highlighted as the two edits; arrows through AAPT2 to three R constants; a phone screen showing Hello, Chennai.')


# ---- 2.4 the callbacks logged for five actions ----
def f4():
    acts = [('(a) launch', ['onCreate', 'onStart', 'onResume']), ('(b) Home', ['onPause', 'onStop']),
            ('(c) from recents', ['onRestart', 'onStart', 'onResume']), ('(d) Back', ['onPause', 'onStop', 'onDestroy']),
            ('(e) rotate', ['onPause', 'onStop', 'onDestroy', 'onCreate', 'onStart', 'onResume'])]
    down = {'onPause', 'onStop', 'onDestroy'}
    o = [T(16, 24, 'Log lines for each action, in order', 15, 'start', bold=True)]
    w, gap, x0 = 128, 13, 16
    for j, (name, seq) in enumerate(acts):
        x = x0 + j * (w + gap)
        o.append(T(x + w / 2, 56, name, 14, bold=True))
        for i, cb in enumerate(seq):
            y = 70 + i * 34
            dn = cb in down
            o.append(R(x + 6, y, w - 12, 28, NXS if dn else ACS, NX if dn else AC, 6, 1.5))
            o.append(TM(x + w / 2, y + 19, cb, 13))
            if i: o.append(L(x + w / 2, y - 6, x + w / 2, y - 1, L2, 1.5))
        o.append(T(x + w / 2, 290, f'{len(seq)} lines', 14, fill=MUT, bold=True))
    o.append(L(x0 + 4 * (w + gap) + 4, 70 + 3 * 34 - 3, x0 + 5 * (w + gap) - gap - 4, 70 + 3 * 34 - 3, INK, 1.5, '4 3'))
    o.append(T(16, 344, 'Total: 3 + 2 + 3 + 3 + 6 = 17 lines.', 15, 'start', bold=True))
    o.append(T(16, 368, 'After (e) an int field count = 7 reads 0 in the new object, unless it was saved in the Bundle.', 14, 'start'))
    o.append(R(470, 330, 14, 14, ACS, AC, 3, 1.5)); o.append(T(490, 342, 'coming up', 13, 'start', MUT))
    o.append(R(570, 330, 14, 14, NXS, NX, 3, 1.5)); o.append(T(590, 342, 'going down', 13, 'start', MUT))
    return 384, ''.join(o)
FIG[4] = (f4, 'Launch logs 3 lines, Home 2, reopening from recents 3, Back 3 and rotation 6, 17 in all. Rotation destroys the activity and builds a new one, so a field holding 7 comes back as 0 unless it was saved in the Bundle.',
          'Five columns of callback names, one column per action: launch, Home, recents, Back and rotate, with 3, 2, 3, 3 and 6 lines; a dashed line in the rotate column splits the old object from the new one.')


# ---- 2.5 two buttons, two intents ----
def f5():
    o = [T(16, 24, 'Each button builds an intent; Android matches it and launches an app', 15, 'start', bold=True)]
    # row 1: Call
    y = 50
    o.append(boxt(16, y, 96, 60, ['Call', 'button'], ACS, AC, 14, bold_first=True))
    o.append(L(114, y + 30, 140, y + 30, AC, 2, arrow='n'))
    o.append(R(144, y, 230, 60, PANEL, AC, 8, 2))
    o.append(TM(156, y + 24, 'ACTION_DIAL', 13, 'start', bold=True)); o.append(TM(156, y + 46, 'tel:9876543210', 13, 'start'))
    o.append(L(376, y + 30, 402, y + 30, AC, 2, arrow='n'))
    o.append(boxt(406, y, 120, 60, ['filter match', 'dialer app'], PANEL, L2, 13))
    o.append(L(528, y + 30, 554, y + 30, AC, 2, arrow='n'))
    o.append(boxt(558, y, 146, 60, ['dialer opens with', '9876543210 filled'], LVS, LV, 13))
    o.append(T(144, y + 80, 'no permission needed: the user presses call (ACTION_CALL would need CALL_PHONE)', 13, 'start', MUT))
    # row 2: Share
    y = 170
    o.append(boxt(16, y, 96, 78, ['Share', 'button'], ACS, AC, 14, bold_first=True))
    o.append(L(114, y + 39, 140, y + 39, AC, 2, arrow='n'))
    o.append(R(144, y, 230, 78, PANEL, AC, 8, 2))
    o.append(TM(156, y + 24, 'ACTION_SEND', 13, 'start', bold=True)); o.append(TM(156, y + 45, 'type text/plain', 13, 'start'))
    o.append(TM(156, y + 66, 'EXTRA_TEXT "Table for 4"', 13, 'start'))
    o.append(L(376, y + 39, 402, y + 39, AC, 2, arrow='n'))
    o.append(boxt(406, y + 4, 120, 70, ['resolveActivity', '!= null ?'], PANEL, NX, 13))
    o.append(L(528, y + 39, 554, y + 39, LV, 2, arrow='l'))
    o.append(Tb(541, y + 30, 'yes', 12, fill=LV, bold=True))
    o.append(boxt(558, y, 146, 78, ['chooser "Send via"', 'user picks an app'], LVS, LV, 13))
    o.append(L(466, y + 76, 466, y + 110, NX, 2, arrow='x'))
    o.append(T(466, y + 128, 'no match: skip, else ActivityNotFoundException', 13, fill=NX))
    return y + 142, ''.join(o)
FIG[5] = (f5, 'Call builds ACTION_DIAL with tel:9876543210 and opens the dialer with the number filled, needing no permission. Share builds ACTION_SEND with text/plain and Table for 4, checks resolveActivity, then lets the user pick an app in the chooser.',
          'Two rows of boxes: the Call button leads to an ACTION_DIAL intent, a filter match and the dialer; the Share button leads to an ACTION_SEND intent, a resolveActivity check and a chooser, with a no-match branch below.')


# ---- 2.6 phone and tablet, one tap on item 2 ----
def screen(x, y, w, h, lab):
    return R(x, y, w, h, PANEL, INK, 12, 2) + T(x + w / 2, y - 10, lab, 14, bold=True)


def f6():
    o = [T(16, 24, 'One app, two widths; the user taps item 2', 15, 'start', bold=True)]
    # phone before and after
    o.append(screen(16, 64, 120, 210, 'phone 360 dp'))
    for i in range(3):
        o.append(R(26, 80 + i * 40, 100, 32, ACS if i != 1 else AC, AC, 5, 1.5))
        o.append(T(76, 101 + i * 40, f'item {i + 1}', 13, fill='var(--fig)' if i == 1 else INK, bold=i == 1))
    o.append(T(76, 234, 'list_container', 12, fill=MUT))
    o.append(L(142, 170, 176, 170, NX, 2.5, arrow='x')); o.append(T(159, 160, 'tap', 12, fill=NX))
    o.append(screen(182, 64, 120, 210, 'after the tap'))
    o.append(boxt(192, 80, 100, 140, ['Detail', 'item 2'], LVS, LV, 14, bold_first=True))
    o.append(T(242, 234, 'list_container', 12, fill=MUT))
    o.append(T(16, 302, 'res/layout: 1 container', 13, 'start'))
    o.append(T(16, 320, 'replace + addToBackStack', 13, 'start'))
    o.append(T(16, 340, 'back stack = 1', 14, 'start', NX, True))
    # tablet
    o.append(screen(350, 64, 354, 210, 'tablet 900 dp'))
    o.append(L(500, 74, 500, 264, L2, 1.5, '5 4'))
    for i in range(3):
        o.append(R(362, 80 + i * 40, 126, 32, ACS if i != 1 else AC, AC, 5, 1.5))
        o.append(T(425, 101 + i * 40, f'item {i + 1}', 13, fill='var(--fig)' if i == 1 else INK, bold=i == 1))
    o.append(T(425, 234, 'list_container', 12, fill=MUT))
    o.append(boxt(512, 80, 180, 140, ['Detail', 'item 2', '(was item 1)'], LVS, LV, 14, bold_first=True))
    o.append(T(602, 234, 'detail_container', 12, fill=MUT))
    o.append(T(350, 302, 'res/layout-sw600dp: 2 containers', 13, 'start'))
    o.append(T(350, 320, 'replace in detail_container, no back stack', 13, 'start'))
    o.append(T(350, 340, 'back stack = 0', 14, 'start', LV, True))
    o.append(T(16, 376, 'The sw600dp qualifier picks the layout: 360 dp < 600 dp, 900 dp ≥ 600 dp.', 14, 'start', MUT))
    return 392, ''.join(o)
FIG[6] = (f6, 'The 360 dp phone has one container, so tapping item 2 replaces the list with the detail and puts 1 entry on the back stack. The 900 dp tablet uses the sw600dp layout with two containers, so the detail changes beside the list and the back stack stays at 0.',
          'Left, a phone list of three items and, after a tap on item 2, the same screen filled by a detail fragment, back stack 1; right, a tablet with the list and a detail pane side by side, back stack 0.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        1: [('<b>iOS</b> runs on the Darwin kernel (Mach and BSD code), is closed source, and ships only on Apple hardware.',
             '<b>iOS</b> runs on Darwin, Apple\'s Unix core, whose kernel XNU is built from Mach and BSD code; iOS is closed source and ships only on Apple hardware.'),
            ('Installation is through the App Store alone.',
             'Ordinary installs go through the App Store; TestFlight betas and enterprise builds are the managed exceptions.'),
            ('iOS uses the Darwin kernel, built from Mach and BSD code.',
             'iOS uses XNU, the kernel inside Apple\'s Darwin core, built from Mach and BSD code.')],
        2: [('The Android platform is drawn as a stack of six layers.', 'The Android platform is a stack of six layers.')],
        3: [(' Only a few universities teach this depth.', '')],
        5: [(' Only a few universities teach this detail.', ''),
            ('The figure shows the call, match and launch.', 'The figure follows both buttons from the intent, through the match, to the launch.')],
    }.get(k, [])


def chapter_fix(k, ch):
    if k == 1:
        for s in ch['sections']:
            for b in s['blocks']:
                if b.get('type') == 'table' and b.get('head', [None, None])[1] == 'Kernel':
                    for r in b['rows']:
                        if r[0] == 'iOS' and r[1] == 'Darwin': r[1] = 'XNU (Darwin)'
    return ch
