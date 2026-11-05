# c-cn-u2: free-model run

- Book: `books/cse/c-cn/c-cn-u2.html`
- Status: ok
- Model calls so far: 37 (115,739 tokens in, 117,494 out), 5.5 minutes

## Checker

```
c-cn-u2.html: 8 chapters, 10477 words, 9 figures, 127 KB
OK
```

## For the reviewer

- chapter 6: a c program's shown output was replaced by its real output; check the text around it
- chapter 2: worked example 1: the example's "check" code failed: Traceback (most recent call last):
  File "/tmp/tmp0uzu9ku9/check.py", line 4, in <module>
    P_tx_dbm = 10 * (P_tx_w / 0.001).bit_length()  # placeholder not used
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'float' object has no attribute 'bit_length'
- chapter 4: give 6 to 8 quiz questions
- chapter 4: the figure cannot be drawn: a row of the block diagram has more than 5 boxes; use fewer nodes or set "layers"

## Reviewer notes (after any revision)

- ch 1 [high] Section 1: The definition says a digital signal belongs to a finite set, usually {0,1}. This is incorrect because digital signals can have more than two amplitude levels; binary is just one common representation.
- ch 1 [high] Section 1: The statement "The term discrete‑time signal is synonymous with digital signal when the values are binary" is misleading. Discrete‑time refers to sampling in time, not to the amplitude representation.
- ch 1 [low] Bullet list under Section 1: Bullet "Discrete‑time ↔ digital" repeats the same misleading equivalence.
- ch 1 [low] Section 3 (Quantisation and PCM): Step‑size formula Δ = (V_max – V_min)/L omits the common factor (L‑1) used when V_max and V_min are the extreme quantisation levels.
- ch 1 [low] Section 3 (Quantisation and PCM): The unit for the step size Δ is not mentioned.
- ch 2 [low] Section 2: Distortion and noise, paragraph on shot noise: The statement "Shot noise appears in semiconductor devices and is proportional to the square root of the current" is inaccurate. Shot‑noise current spectral density is proportional to the square root of the product of charge, average current and bandwidth (i² = 2qI·B). The noise power is proportional to the average current, not its square root.
- ch 3 [high] Section 3: Comparing Nyquist and Shannon limits: The text says "For a 3 MHz channel with an SNR of 30 dB, the Shannon capacity is about 18 Mbps", which contradicts the correct calculation (≈30 Mbps) shown later.
- ch 3 [low] Figure description: The caption states "The plot uses the same three points as the worked example", but the worked example provides only one numerical point (the 30 dB case).
- ch 3 [low] Figure data (spec: series points): The plotted capacity for 10 dB SNR is 9.9 Mbps, but the correct value for a 3 MHz channel is about 10.4 Mbps.
- ch 4 [high] Section 1, formula A = 10 log₁₀(P₁/P₀): The attenuation formula is reversed; using P₁/P₀ gives a negative value for loss.
- ch 4 [high] Quiz Q3 (apply, 4 marks): The required antenna gain is calculated incorrectly. The answer gives 70 dBi total, but the correct link‑budget gives a negative gain requirement.
- ch 4 [low] Section 3, bullet "Select guided if distance ≤ 2 km and cost permits; otherwise select unguided.": The rule is oversimplified; guided media such as fibre can be used for distances far beyond 2 km.
- ch 4 [low] Exam traps, bullet about microwave and satellite frequency ranges: The statement suggests satellite uses only higher bands than microwave, ignoring that C‑band and Ku‑band are also used for satellite and lie within the microwave range.
- ch 4 [low] Section 1, sentence "Attenuation adds up linearly with distance for copper...": May be misread as power attenuation adding linearly.
- ch 5 [high] Quiz Q4: The answer describes Differential Manchester incorrectly: it says a ‘1’ has a transition at the start and no transition at the centre, and a ‘0’ has no transition at the start and a transition at the centre. In Differential Manchester a transition at the centre of every bit period is mandatory, and the presence or absence of a transition at the start of the bit period encodes the data (commonly, a transition at the start denotes a ‘0’ and no transition denotes a ‘1’, or the opposite convention). The given description reverses the convention and omits the required centre transition.
- ch 5 [low] Section 3: The sentence "Codes that avoid long runs of identical levels (Manchester, Differential Manchester, 4B/5B) have little or no DC component" is inaccurate for 4B/5B. While 4B/5B limits run length and reduces DC, it does not guarantee a DC‑free signal because the subsequent NRZ transmission can still have a net DC offset.
- ch 6 [high] Section 3, formula B_total = B_baseband + B_modulation: The formula incorrectly adds baseband bandwidth to modulation bandwidth. In practice the required channel bandwidth is determined by the modulation scheme and already includes the effect of the baseband signal; it is not a simple sum.
- ch 6 [low] Section 2, ASK bandwidth statement: It says "ASK bandwidth ≈ 2B where B is the baseband bit rate", which overestimates the typical bandwidth for binary ASK with NRZ pulses.
- ch 6 [low] Section 2, FSK bandwidth formula: The formula "FSK bandwidth ≈ 2(Δf + B) where Δf = |f_1‑f_0|/2" mixes the frequency deviation Δf with the bit‑rate B without clear definition, which can confuse students.
- ch 6 [low] Quiz Q5: The answer states spectral efficiencies without explicitly linking them to the required bandwidth, which may leave students unclear why the numbers equal bits/s/Hz.
- ch 6 [low] Section 1, AM bandwidth note: The statement does not mention that single‑sideband AM reduces bandwidth to the baseband width.
- ch 8 [high] Section 1: The statement that the UPI app “BHIM” uses a form of spread spectrum for its Bluetooth handshake is inaccurate; BHIM operates over the internet and does not employ Bluetooth spread‑spectrum techniques.
- ch 8 [high] Section 2 (example of Wi‑Fi processing gain): The processing gain is given as 13 dB for a 2 Mbps data stream spread with a 20 Mbps chip rate, but the correct gain is 10 dB (10·log₁₀(20/2) = 10 dB).
- ch 8 [high] Beyond section: The claim that “5G NR includes a form of DSSS for control channels” is false; 5G NR uses OFDM and does not employ DSSS for its control channels.
- ch 8 [low] Section 2, bullet point 1: The phrase “Generate a pseudo‑random binary sequence of length equal to the spreading factor” may be misread; the sequence length per data bit equals the spreading factor, not the total sequence length.
- ch 8 [low] Section 2, bullet point 2: Saying “Map data bit ‘1’ to the chip sequence, data bit ‘0’ to the inverted sequence” could be unclear for beginners.
- ch 8 [low] Section 3, processing‑gain formula: The term “occupied bandwidth per hop” is not defined, which may confuse readers.
