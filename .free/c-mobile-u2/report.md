# c-mobile-u2: free-model run

- Book: `work/claude_figs/c-mobile-u2/tree/books/cse/c-mobile/c-mobile-u2.html`
- Status: ok
- Model calls so far: 28 (96,928 tokens in, 172,348 out), 8.7 minutes

## Checker

```
c-mobile-u2.html: 6 chapters, 11489 words, 7 figures, 143 KB
OK
```

## For the reviewer

- chapter 1: the figure cannot be drawn: note "QNX, legacy" runs off the right edge; shorten it
- chapter 1: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, iOS paragraph: The sentence 'Installation is through the App Store alone' is too absolute. Apple also allows ad hoc installs for registered devices, in-house enterprise distribution, TestFlight beta builds, and (in some regions) alternative marketplaces — a point the 'Beyond' paragraph itself raises, so a student meets two answers that disagree.
- ch 1 [low] Section 2, iOS paragraph and the comparison table: 'Darwin kernel' is loose. Darwin is Apple's Unix core (kernel plus the BSD userland and drivers). The kernel inside Darwin is XNU, made of Mach plus BSD code. Writing 'Darwin kernel' in the text and 'Darwin' in the Kernel column teaches the wrong layering.
- ch 1 [low] Section 1, fourth job (install, update and payment): 'On Android and iOS that means an app store' suggests the store is the only install path on both. On Android the user can allow installs from unknown sources, sideload an APK and add a third-party store. A student can misread this as Android blocking non-Play installs.
- ch 1 [low] Section 2 comparison table, Windows Phone row: The App languages cell lists 'C#, XAML'. XAML is a markup language for describing the interface, not a programming language, and listing it beside C# and Kotlin muddles what a student should write in an exam.
- ch 2 [high] Section 1, native libraries: WebKit is listed as the current native library for web content. Android's WebView has been based on Chromium (Blink), not WebKit, since Android 4.4 (API 19). A student reading this in 2024+ gets an outdated fact.
- ch 2 [low] Section 3, last paragraph: 'All three are written in the module's build.gradle ... Gradle copies them into the manifest' implies compileSdk also reaches the manifest. Only minSdk and targetSdk become manifest attributes; compileSdk is build-time only and never appears in the manifest.
- ch 2 [low] Section 1, Android runtime: The sentence 'ART replaced Dalvik from Android 5.0; it compiles ahead of time at install and just in time while the app runs' merges two eras. In Android 5.0 and 6.0 ART was ahead-of-time only at install; just-in-time compilation with profile-guided AOT arrived in Android 7.0.
- ch 2 [low] Worked example 1, step 6: The guard 'if (Build.VERSION.SDK_INT >= 24)' is presented as the general rule, but the constant must be the API level that introduced the method being called, not a fixed 24.
- ch 2 [low] Beyond: 'baseline profiles, which record the hot code paths at install' is wrong about when they are made. Baseline profiles are generated at build time (from benchmark runs) and shipped inside the APK; ART uses them during installation to compile those paths ahead of time.
- ch 3 [high] Worked example 1, steps 3–4 and answer: The example asks the student to make the screen show 'Hello, Chennai', then counts three edited files including MainActivity.java. No Java edit is needed: the template already calls setContentView(R.layout.activity_main), and the TextView gets its text from @string/greeting in the layout. Step 3 itself admits findViewById is only for changing text at run time, so it contradicts the answer.
- ch 3 [low] Section 1: Saying MainActivity 'extends Activity' does not match what Android Studio generates. The Empty Activity template produces a class extending AppCompatActivity (an androidx subclass of Activity); a plain Activity also forces a non-AppCompat theme.
- ch 3 [low] Section 3, last sentence: 'A crash on launch usually points to the manifest or a missing layout name' is misleading. A missing or misspelled layout resource fails the build (no R.layout constant), so it cannot cause a launch crash. Runtime crashes on launch typically come from an undeclared activity or a findViewById returning null (wrong id, or called after a changed layout).
- ch 3 [low] Exam traps, second bullet: "Writing import com.example.hello.R by hand" is described as a mistake, but R for this module lives in com.example.hello, the same package as MainActivity, so such an import is redundant, not wrong. The real mistake students make is importing android.R by accident.
- ch 3 [low] Lead and Section 1 (build file naming): Students using a current Android Studio see MainActivity.kt and build.gradle.kts by default, while the chapter speaks only of Java files and build.gradle. Nothing in the chapter tells them how to get the Java/XML project the chapter assumes.
- ch 4 [low] Section 3, the onSaveInstanceState timing sentence: The blanket statement 'onSaveInstanceState runs after onPause and before onStop' is only true for apps targeting below Android 9 (API 28). For apps targeting API 28 or higher the system calls it after onStop, so a student who memorises this sentence will be wrong for modern targetSdk values.
- ch 4 [low] Quiz Q5, answer: 'onPause or onSaveInstanceState, which always run before the activity can be hidden or killed' overstates both callbacks. onSaveInstanceState is not called at all when the user presses Back (the activity is finishing), and on new targets it runs after the activity is already hidden (after onStop).
- ch 4 [low] Worked example 1, steps 5 and 6: Step (d) ends with onDestroy, so the activity no longer exists. Step (e) then says 'rotate while the activity is resumed', which is only possible after a fresh launch. The total of 17 treats (a) to (e) as one continuous session, but a real session would log 3 more lines (onCreate, onStart, onResume) before the rotation.
- ch 4 [low] Section 2, the list of seven callbacks: The list is introduced as being 'in a fixed order', but onRestart is placed last, after onDestroy, which is not the order Android calls it. A student skimming the bullets can carry away a wrong sequence.
- ch 4 [low] Quiz Q1, question wording: The question asks for 'the seven life cycle callbacks in the order' but the sequence it describes produces only six; the seventh (onRestart) does not appear. The mismatch is only explained in the answer, not the question.
- ch 5 [low] Section 1, after the description of intent filters: The sentence "Only a few universities teach this detail" is attached to intent filters, which are core Android material in every syllabus and a standard exam question. It invites students to treat filters as optional trivia and skip them.
- ch 5 [low] Section 2 and Worked example step 5 (resolveActivity check): On Android 11 (API 30) and later, package visibility hides other apps by default. resolveActivity can return null for an app that would in fact handle the intent, unless the manifest declares a <queries> element. A student following the advice blindly will see the check fail and refuse a valid launch.
- ch 5 [low] Exam traps, first bullet: "causes ActivityNotFoundException" is too absolute, and a chooser never throws it. The exception can happen, and only when you call startActivity directly without a matching app.
- ch 5 [low] Quiz Q4 answer: The code uses single quotes: Uri.parse('geo:13.0827,80.2707'). Java string literals need double quotes, so the shown answer would not compile.
- ch 5 [low] Figure spec, third message: The message 'onCreate, shows screen' is drawn from the target app to the Android system. The direction is reversed: the system calls the target activity's onCreate, the activity does not call the system.
- ch 6 [high] Section 2 (fragment life cycle list) and Quiz Q1 answer: The callback list jumps from onDestroyView() straight to onDetach() and leaves out onDestroy(). The prose a few lines later says the object exists 'from onCreate to onDestroy', so the list contradicts itself. A student who memorises this list for Q1 will write an incomplete answer.
- ch 6 [low] Section 2, third paragraph: 'A stopping activity stops its fragments first' gives the wrong ordering. The host activity's own onStop() runs before the FragmentManager dispatches onStop() to its fragments, so the fragments stop after the activity, not before it.
