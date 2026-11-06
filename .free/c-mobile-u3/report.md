# c-mobile-u3: free-model run

- Book: `books/cse/c-mobile/c-mobile-u3.html`
- Status: ok
- Model calls so far: 20 (64,784 tokens in, 120,273 out), 3.9 minutes

## Checker

```
c-mobile-u3.html: 6 chapters, 10786 words, 7 figures, 122 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3 (dp and the conversion formula): The formula says dpi is 'the screen density in dots per inch'. Read literally, a student will use the physical panel dpi printed on a spec sheet. Android converts with the logical density it reports (DisplayMetrics.densityDpi, snapped to values like 320 or 480), which is often not the physical dpi.
- ch 1 [low] Lead and Section 1: 'The activity window holds exactly one root ViewGroup. Everything else is a descendant' implies the XML root is itself the top of the tree. In practice the layout is inflated as a child of the window's own content FrameLayout, and setContentView can even take a single View, not only a ViewGroup.
- ch 1 [low] Exam traps, first bullet: 'gravity centres a layout's own children' is only half true and clashes with Q4, where gravity on a Button centres its text. On a widget, gravity positions the widget's own content, not children.
- ch 1 [low] Quiz Q4 answer: 'layout_gravity centres the button inside the parent' is too broad. In a LinearLayout, layout_gravity acts only on the axis perpendicular to the orientation (it centres vertically in a horizontal row; horizontally in a vertical column).
- ch 2 [high] Section 2, and the answer to Quiz Q4: The claim 'Any view with an android:id writes its own state into that Bundle' and the follow-up 'my text vanishes on rotation only hits views you built in code without an id' is wrong for TextView. A TextView saves its text only when freezesText is on (EditText, being editable, is on by default). So a TextView declared in XML with an id and filled from code loses its text on rotation too. Quiz Q4 gives the right outcome but the wrong reason: the text is lost because a plain TextView does not freeze its text, not because the view has no id.
- ch 2 [low] Quiz Q1: The listed order onPause, onStop, onDestroy, then onCreate, onStart, onResume is correct, but the question asks for the callbacks an activity receives in order on rotation, and onSaveInstanceState belongs in that sequence between onPause and onStop. A student copying the answer into an exam may lose a mark for omitting it.
- ch 3 [high] Quiz Q2 (and the showAsAction paragraph in Section 2): The answer gives withText as if it were a fourth placement value of showAsAction, equal in kind to always, ifRoom and never. withText is a modifier flag (value 4), not a placement value. Written alone as app:showAsAction="withText" it requests no bar slot, so the item actually falls into overflow, which contradicts the chapter's own claim that withText shows the title beside the icon. The Section 2 sentence 'withText also shows the title beside the icon when there is room' repeats the confusion and never says it must be combined with a placement value.
- ch 3 [low] Exam traps, fourth trap: 'Forgetting either gives an empty long-press menu' is wrong for the missing super call. The default Activity.onCreateContextMenu does nothing, so skipping super does not empty the menu; only a missing inflate does. Students may believe a broken menu proves they forgot super.
- ch 4 [low] Section 3, picker views (TimePicker): The parenthetical '(0 to 23 in 24-hour mode, set by setIs24HourView(true))' suggests getHour() changes range when the picker is in 12-hour display mode. A student can read this as 'getHour() returns 1 to 12 in 12-hour mode', which is wrong.
- ch 4 [low] Section 4, adapter and click listener: 'id is the row id the adapter reports (for an ArrayAdapter it equals position)' is true only while the ListView has no header or footer. Once addHeaderView is used the ListView's adapter is the header-wrapping adapter, ids come from the inner ArrayAdapter, and id no longer equals position (header rows report -1).
- ch 4 [low] Exam traps, trap 1 (headers and footers): It says position 'shifts the moment a header or footer view is added'. A footer does not shift any existing row's position; it only adds a row after the last item.
- ch 4 [low] Section 3, DatePicker: Saying the DatePicker 'is set with init(year, month, day, listener)' without saying when the listener fires leaves a gap next to the Spinner point about setSelection. Students then expect init to call the listener, and do not know how to change the date from code.
- ch 4 [low] Section 3, Spinner bullets: 'getSelectedItemPosition() returns the index' leaves out the empty case, which matters because the same section already quotes -1 for RadioGroup.
- ch 5 [low] Section 2 (WebView): The sentence 'add  to the manifest' has an empty gap where the permission element should be, so the student is told to add nothing.
- ch 5 [low] Section 1 (scaleType list): The list never states which scaleType ImageView uses when android:scaleType is not written, so a student cannot answer 'what happens by default'.
- ch 5 [low] Exam trap 1: The clause 'it is the answer examiners expect to be marked wrong' is ambiguous: it can be read as saying fitXY is the correct answer.
- ch 6 [high] Lead: "every XML attribute has a setter" is false and contradicts what the rest of the chapter teaches. Layout attributes such as android:layout_width, android:layout_weight and android:layout_margin map to fields on the parent's LayoutParams, not to setters on the view (there is no setWeight). Some attributes, like android:onClick or android:style, are read by the framework during inflation and have no matching public setter. A student reading this will hunt for calls that do not exist.
- ch 6 [low] Section 1 note and Exam traps (first trap), repeated in Quiz Q2: "addView(view) alone falls back to wrap_content" is not always true. addView with no params uses the parent's generateDefaultLayoutParams(). For a vertical LinearLayout that is MATCH_PARENT width × WRAP_CONTENT height, so the width is not wrap_content. Only the horizontal case gives wrap_content in both directions. The main point (weight is ignored) is right, the detail is not.
- ch 6 [low] Worked example 1: The example says "Build a horizontal LinearLayout in code", but the shown code never creates a LinearLayout, a Button, LayoutParams, an id or an OnClickListener. It is only integer arithmetic in a main method, so the reader never sees the API calls the example claims to demonstrate.
