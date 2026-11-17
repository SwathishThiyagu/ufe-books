# c-graphics-u4: free-model run

- Book: `work/claude_figs/c-graphics-u4/tree/books/cse/c-graphics/c-graphics-u4.html`
- Status: ok
- Model calls so far: 43 (152,131 tokens in, 281,664 out), 6.0 minutes

## Checker

```
c-graphics-u4.html: 9 chapters, 15414 words, 10 figures, 183 KB
OK
```

## For the reviewer

- chapter 1: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 2: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 1: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Figure (tree diagram at the end of Section 3): The text says seven elements are usually listed and the table includes Images (stored as pixels), but the figure tree has only six branches — Text, Graphics, Audio, Video, Animation, Interactivity. Images is missing, so the diagram contradicts the table and would teach a student that images are not an element.
- ch 1 [low] Quiz Q3: The question places the looping advertisement on a 'shop's television screen', but the chapter's own second condition for multimedia is that a computer controls the order and timing. A television/player is not clearly a computer, so the question does not cleanly fit the definition it is testing, and the model answer has to assert computer control that the question never states.
- ch 1 [low] Section 3, Education bullet: The claim that an animation with voice-over 'explains faster than a page of text' is an unverified comparison, stated as fact.
- ch 2 [low] Section 1: "compression only reduces the count" is ambiguous: a student can read it as saying compression reduces the number of pixels, samples or frames, which it does not. Compression keeps the same units and reduces the bits used to store them.
- ch 3 [high] quiz Q2: The question mixes two different layers. Reading camera registers is an alternative to calling a camera API, not to calling a codec API. As written, the answer 'returns encoded frames' does not follow from the question, so a student revising from this card gets a wrong mental model of which API does what.
- ch 3 [low] section 2: 'USB, HDMI and audio interfaces carry data and power between boxes' overstates it. USB supplies power to a device; HDMI and audio cables carry signals, not useful power for the connected box.
- ch 3 [low] worked example, step 5: The product 48,000×2×2 is not explained, so the reader has to guess what each 2 is. The exam trap later warns about 16 bits = 2 bytes, but the step itself does not show it.
- ch 3 [low] section 3: Cross-references are written as plain text ('see Chapter 4.5', 'see Chapter 4.9'), so they are not tappable on a phone, which is the main way this book is read.
- ch 4 [low] Figure: The figure text says the raster branch lists the still raster formats covered in the text, but the branch note 'BMP JPEG GIF PNG TIFF' leaves out WBMP, which the chapter itself covers as a 1-bit raster still format.
- ch 5 [low] Section 2, formula where-list: The sentence "Channels C is 1 for mono and 2 for stereo" is grammatically broken and defines C as a plural noun, which a student may read as the number 1 or 2 being the symbol's value in all cases.
- ch 5 [low] Section 3, table and WebM sentence: WebM is described only as VP9 or AV1 video and Opus or Vorbis audio. VP8 (with Vorbis) is the original and still valid WebM pairing, so the list is incomplete and a student may mark VP8-in-WebM as wrong.
- ch 5 [low] Section 2, worked example 1 and Q3: The formula uses f<sub>s</sub> with a subscript but the quiz answer and where-list write f_s in plain text, so the symbol looks different in different places in the same chapter.
- ch 6 [low] Figure (tree spec): The figure puts DCT in the Lossy branch next to Quantization. The DCT itself is a reversible transform, so a student revising from the picture may write 'DCT is a lossy method' in the exam, which the text does not say.
- ch 6 [low] Figure (tree spec): The Lossless branch lists only RLE and Huffman, but the section also teaches LZW. A student who revises only from the figure will miss one of the three named lossless methods.
- ch 6 [low] Section 3, quantization paragraph: 'A value 137 can be stored as 136 or 144 if the step size is 8' is confusing. Both are multiples of 8, but rounding to the nearest level gives only 136, so the reader cannot tell which rule the codec uses.
- ch 7 [low] Quiz Q1 answer: The question asks what PCM stores for each audio sample, but the answer mixes in the sample rate, which is not a per-sample quantity. A student can read it as 'each sample carries a sample rate' and get confused between sample rate and bit depth.
- ch 7 [low] Section 2, paragraph 3: The section first says a B-frame 'may use an earlier and a later reference frame', then later says 'B-frames need two reference frames'. The two statements pull in different directions, and in newer standards a B-frame can be predicted from a single reference frame.
- ch 7 [low] Section 1, paragraph 3: 'MP3 and AAC use this scheme' overstates it for MP3. MP3 feeds the signal through a 32-band polyphase filterbank before the MDCT stage, so it does not apply the MDCT directly to the whole block as AAC does.
- ch 8 [low] Section 1, MPEG-1 target bit rate: The phrase 'about 1.5 Mbps video plus audio' reads two ways. A student may take 1.5 Mbps as the video rate alone and write that in an exam; the 1.5 Mbps figure is the total for video plus audio.
- ch 8 [low] Section 3, last sentence of the description-scheme paragraph: 'Descriptions support ... rights metadata' sits awkwardly with Section 4, which says MPEG-21 is the rights framework. It suggests MPEG-7 owns rights metadata.
- ch 8 [low] Quiz Q6 answer: 'it does not compare raw pixels only' is ambiguous; it can be read as saying raw pixels are partly compared.
- ch 9 [high] Worked example 1, step 6 (and the last bullet of Section 2): With t_V = 120 ms and t_A = 230 ms the audio plays 110 ms after the picture, so the picture leads and must be held back. 'Skip video' does the opposite: dropping video frames shows later picture content sooner and makes the lead larger. It also contradicts the chapter's own rule of delaying video by the skew.
- ch 9 [low] Section 1, last sentence: The claim that a player 'cannot hide a wrong order of units' with a buffer is misleading. A playout buffer that resequences units by sequence number or timestamp does restore the correct order, as long as the units arrive before their playout deadline.
