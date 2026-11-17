# c-mobile-u4: free-model run

- Book: `work/claude_figs/c-mobile-u4/tree/books/cse/c-mobile/c-mobile-u4.html`
- Status: ok
- Model calls so far: 24 (81,621 tokens in, 153,531 out), 13.7 minutes

## Checker

```
c-mobile-u4.html: 6 chapters, 9913 words, 7 figures, 135 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1 and Quiz Q2: The chapter says a preference value is only a String, int, boolean, long or float, and tells students lists belong to file storage or SQLite. SharedPreferences also has putStringSet/getStringSet for a Set of Strings, so a student who answers 'lists are impossible' in an exam is technically wrong.
- ch 1 [low] Section 2 and Quiz Q7: The chapter tells students to register an OnSharedPreferenceChangeListener but not that SharedPreferences holds listeners weakly. A listener created as a temporary object with nothing else pointing at it can be garbage collected and silently stop firing, which is a common bug for students doing Q7 exactly as written.
- ch 1 [low] Beyond: The chapter points students to EncryptedSharedPreferences as the current way to store secrets, but the Jetpack security-crypto library that provides it has since been deprecated, so the pointer is out of date.
- ch 2 [high] Exam traps, bullet 1: The claim that an unmounted write gives 'no friendly error; the file simply never appears' is technically wrong. The usual symptom is not a silent success: getExternalFilesDir() returns null when external storage is not mounted, so building a File or stream from it throws NullPointerException, and a path on unmounted storage fails with FileNotFoundException. A student would learn the wrong failure behaviour.
- ch 2 [low] Section 3: The section never says that getExternalFilesDir(type) can return null when external storage is not mounted, so students will chain calls on a null result.
- ch 2 [low] Section 2: OutputStreamWriter without an explicit charset uses the platform default charset, not a guaranteed UTF-8. It happens to be UTF-8 on Android, but the sentence states it as a guarantee of OutputStreamWriter.
- ch 2 [low] Section 2, reading step: openFileInput(name) is a byte stream; it cannot be wrapped directly in BufferedReader. The InputStreamReader step is missing.
- ch 2 [low] Quiz Q4: The answer lists 'missing permission' as a cause without saying that storage permission only matters for shared public folders, and only up to Android 9 (API 28). The app's own external folder needs no permission, so the answer can mislead.
- ch 2 [low] Lead: 'getFilesDir and getCacheDir return their folders' — 'their' is ambiguous, since openFileOutput writes only into files/, never into cache/.
- ch 3 [low] Section 2, paragraph on AUTOINCREMENT: "AUTOINCREMENT makes SQLite fill 1, 2, 3 for you" teaches the common misconception that AUTOINCREMENT is what produces automatic numbering. Numbering comes from declaring the column INTEGER PRIMARY KEY (it is an alias for the rowid). AUTOINCREMENT only adds the extra promise that an id from a deleted row is never reused.
- ch 3 [low] Figure (spec title and caption): The title "The students table after three inserts, ordered by marks" contradicts the figure itself: the rows are shown in insertion order (Asha, Ravi, Meera) and the caption says the pointer marks the row that would come first in a descending sort. A student reading the title expects 95, 88, 72 down the marks column.
- ch 3 [low] Section 3 (Cursor) and Exam trap 3: "Leaked cursors eventually exhaust the database" and "enough of them and the database fails" name the wrong failure. The real cost of an unclosed cursor is a retained file handle and a CursorWindow (a fixed-size in-memory buffer of rows), so the app runs out of memory or hits a CursorWindowAllocationException / too-many-open-files error. The database file itself is not exhausted.
- ch 3 [low] Worked example 1 code block: The chapter is about Android/Java, but the code block is an unlabelled Python sqlite3 script. A student can mistake it for Android code, since nothing says it is only there to run the SQL and print the true result.
- ch 4 [low] Worked example 1, step 5 and the answer line: The trace mixes a query() call with getType(). ContentResolver.query() never calls getType(); getType() is reached only when someone calls getContentResolver().getType(uri) (for example to decide whether a URI is a directory or a single item). The caller also never sees the UriMatcher code — that number stays inside the provider. A student will read the answer as if the Cursor comes back carrying a MIME type and a match code.
- ch 4 [low] Section 3, exam traps and quiz Q4: "Authority in code and manifest differ; every URI returns NO_MATCH" is only half true. If the caller's URI carries the authority from the code (UriMatcher) and the manifest registered a different one, the resolver finds no provider at all and throws IllegalArgumentException (unknown URL); NO_MATCH is returned only when the URI matches the manifest authority but the UriMatcher was built with a different string.
- ch 4 [low] Section 3, permissions paragraph: The custom permissions READ and WRITE are declared on the provider, but the chapter never says the other app must request them. Without that step the client gets a SecurityException even when the provider is exported.
- ch 4 [low] Section 1, built-in example bullet: ContactsContract.Contacts.CONTENT_URI cannot be read with the few lines shown unless the app holds READ_CONTACTS. On Android 6.0 and later that is a runtime permission request, so the code fails with SecurityException as written.
- ch 4 [low] Figure message labels: The label 'query(uri, null, null)' shows a three-argument call, but ContentResolver.query() and ContentProvider.query() take uri, projection, selection, selectionArgs and sortOrder. The label can teach a wrong signature.
- ch 5 [high] Section 2 (Publish your file with FileProvider) and worked example 1, step 1: The <provider> tag is described without the <meta-data> child that points to res/xml/file_paths.xml. Without it FileProvider has no configured roots, so getUriForFile throws IllegalArgumentException ("Failed to find configured root that contains ...") and the whole worked example fails.
- ch 5 [high] Exam traps, first bullet: "Putting a File in EXTRA_STREAM creates a file:// URI" is wrong. A File object is not a URI; putting it in EXTRA_STREAM just gives the receiver an unusable value. FileUriExposedException comes from putting a file:// URI in the intent.
- ch 5 [low] Section 1, sentence "Always set the type before putting extras; the chooser reads it.": The order of setType() and putExtra() does not matter, so the rule as written teaches a non-rule. The real order trap is between setData() and setType(), which clear each other.
- ch 6 [high] Section 1 (both paragraphs and code blocks), worked example 1 step 1, exam traps item 2, quiz Q5: Every occurrence of the XML tags <layout>, <data> and <variable> has been lost, so key sentences are unreadable: "Rename the root of activity_main.xml to .", "Inside it a  block declares the variables", "one setter is generated per .", "Root of activity_main.xml: , containing , then a LinearLayout", "Forgetting the  root", and the Q5 answer "instead of  (wrap it and rebuild)". A student cannot see which tag goes where, and step 1 of the 6-mark example shows an empty root.
- ch 6 [low] Section 2 (two-way binding sentence) and exam traps item 4: The text says the field "must be observable" for @= and that using @= on a non-observable field makes "write-back silently do nothing". Write-back (view to object) works with a plain field too; observability is needed only for the object-to-view direction, so a plain field stores the typed text but never redraws the view from the model.
- ch 6 [low] Quiz Q2: The question is garbled: "State one thing view binding can do and data binding can do that view binding cannot" reads as one item and hides that two answers are wanted.
