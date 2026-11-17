# c-mobile-u5: free-model run

- Book: `work/claude_figs/c-mobile-u5/tree/books/cse/c-mobile/c-mobile-u5.html`
- Status: ok
- Model calls so far: 30 (104,910 tokens in, 179,715 out), 5.7 minutes

## Checker

```
c-mobile-u5.html: 6 chapters, 10847 words, 7 figures, 129 KB
OK
```

## For the reviewer

- chapter 4: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 4: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 1 (repeated in the figure note, Worked example 1, Exam traps and Quiz Q2): The text says each concatenated part 'spends 7 bytes on a user data header'. The concatenation header is 6 bytes (octets): 1 length byte + 1 IEI + 1 IE length + 3 data bytes (reference, total parts, sequence). Six octets are 48 bits, which after 7-bit packing occupy 7 characters (septets) of the 160. So the loss is 7 characters, not 7 bytes. A student will write 'the UDH is 7 bytes' in the exam, which is wrong.
- ch 1 [low] Section 2, paragraph 3: The text says to catch ActivityNotFoundException if no app matches, but just before it says to wrap the intent in Intent.createChooser. When the intent is launched through createChooser, the chooser activity itself handles the no-match case and shows its own message; ActivityNotFoundException is thrown when you start an implicit intent directly with no chooser.
- ch 1 [low] Section 2, paragraph 2: The list of extras mixes two intents. EXTRA_EMAIL is not a reliable way to set recipients for ACTION_SENDTO; with ACTION_SENDTO the address belongs in the mailto: URI, and some mail apps ignore EXTRA_EMAIL there. A student may build a SENDTO intent with EXTRA_EMAIL and find the To: field empty.
- ch 1 [low] Section 1, step 1: SmsManager.getDefault() is deprecated from Android 12 (API 31). Students targeting recent SDKs will see a deprecation warning and, on multi-SIM phones, cannot choose the SIM.
- ch 2 [high] Section 3, wiring checklist, third bullet: The step reads "Declare the com.google.android.geo.API_KEY meta-data inside ." — the sentence is cut off and never names the parent XML element. A student following the checklist cannot place the entry, and a misplaced meta-data entry is exactly what produces the grey grid described later.
- ch 2 [low] Section 3, wiring checklist, fifth bullet: "In onCreate call getMapAsync(this)" hides two requirements: the fragment must first be obtained with getSupportFragmentManager().findFragmentById(R.id.map), and the activity must implement OnMapReadyCallback for `this` to be a valid argument.
- ch 2 [low] Section 2, after the centre/span formula: The text says "the bounding box is the pair of them", which can be read as passing centre and span. newLatLngBounds needs a LatLngBounds built from the corner points, and the chapter never shows how to build it.
- ch 2 [low] Exam traps, last trap: "Zoom is an integer scale" is not accurate for the Maps SDK. Zoom level is a continuous value (for example 10.5 is legal); only the tile index is the integer floor of it. The useful point is that zoom is not measured in degrees.
- ch 2 [low] Quiz Q3 answer: The reasoning does not explain the error. Both 80.2 and 13.1 are legal values in either slot, so "longitude must stay within −180 to +180" justifies nothing; the point is that the intended point (13.1° N, 80.2° E) becomes a different place near the pole.
- ch 2 [low] Exam traps, first trap: 77.0° N, 12.0° E is in the Norwegian Sea west of Svalbard, not the Arctic Ocean proper.
- ch 3 [low] Section 1, fine versus coarse: Coarse accuracy is stated flatly as 'about a kilometre'. A coarse fix is usually a Wi-Fi/cell-tower estimate, so it can be a few hundred metres (several Wi-Fi networks seen) up to one or two kilometres (single cell tower). The single figure may be taken as a guaranteed value.
- ch 3 [low] Section 3, proximity alerts: The formula lists an 'expiration' argument but never says what it means or what value to pass. A student cannot use the call from this description.
- ch 3 [low] Section 3, geocoding: The text says to call Geocoder off the main thread but does not say that the geocoding service may be absent, so the call fails on some devices and emulators.
- ch 3 [low] Quiz Q3: The answer 'about 1.4 per minute' is an average rate, but the question asks how many updates arrive per minute. A student may read it as 'two fixes in one minute', when in the first minute after starting from rest only one fix arrives (at about 41.7 s).
- ch 4 [low] Figure and its caption: The caption says 'the two shaded leaves' are certificate checking and remote wipe, but the spec marks three leaves as live (shaded): Permissions (least privilege), TLS (check certificates) and Lost device (remote wipe). The picture a student sees will not match the caption.
- ch 4 [low] Section 3 (Android Keystore): 'you receive a Cipher object that uses it' is not how the API works. The keystore returns a key handle, not a Cipher. A student who believes this will look for a Cipher coming out of the keystore and find none.
- ch 4 [low] Section 3, first paragraph: 'Internal storage is private but not encrypted by your app' is literally true but can be read as 'internal files sit in plaintext on flash'. On current Android the OS itself encrypts internal storage (file-based encryption), though only while the device is locked.
- ch 4 [low] Section 4 (remote wipe) and Quiz Q6: 'It works only while the phone is online' and 'remote wipe fails because the phone never receives the command' are too absolute. The erase command is queued by the service and runs the next time the handset connects; it fails only if the thief keeps the phone offline or the queued command expires.
- ch 4 [low] Beyond: The MASVS list is incomplete: the current set also has a resilience/anti-tampering category, and the statement that MASVS 'pairs each with a test' blurs two documents.
- ch 4 [low] Section 4 formula: The formula is written as N = 10^d with a caret, while the rest of the chapter uses Unicode superscripts (10⁴, 10⁶). Inconsistent notation on a phone screen.
- ch 5 [high] Lead paragraph: "Both are set once and then follow the app for its whole life" is false for the version numbers. versionCode must be increased on every single upload; only the signing key is set once. A student who remembers the lead will reuse versionCode and get rejected uploads.
- ch 5 [high] Exam traps, fifth trap ("Testing only the debug build"): The claim that "certificate-restricted API keys fail only in release" is inverted. An API key restricted to the release certificate (package name plus release SHA-1, the usual Maps setup) fails in the debug build, because the debug APK is signed with the per-machine debug key. Registering the release fingerprint in the console is what makes the key work in release. The same confusion appears in Section 3, where the reader is told to test screens that call "a key restricted to the release certificate".
- ch 5 [low] Quiz Q7: The question asks for two ways out, but the answer gives one: upload with a code greater than 12. There is no second, distinct remedy.
- ch 5 [low] Figure, Release APK pipeline: The node "Sign with keystore" is placed before "Build release APK". In a Gradle release build the signing step runs at the end, after compiling, shrinking and packaging, so the diagram shows the steps in the wrong order.
- ch 5 [low] Section 2, first paragraph: "It proves who built it" overstates what a self-signed certificate does. There is no certificate authority behind an Android signing key, so the signature proves the APK comes from whoever holds that key, not a verified identity.
- ch 6 [low] Section 2, UPI bullet and fee table: It says merchant fees on UPI are zero only for 'many small merchants'. In India the zero-MDR rule on UPI (and RuPay debit) applies to merchants generally, not just small ones, so a student may wrongly assume large merchants always pay MDR on UPI.
- ch 6 [low] Section 2, card row of the fee table: The card range 1.5%–3% + ₹2–₹5 is a credit-card style rate. Debit card MDR in India is capped much lower (about 0.40% up to ₹2,000 and 0.90% above ₹2,000), and RuPay debit is zero, so a student costing a debit card sale from this table will overstate the fee badly.
