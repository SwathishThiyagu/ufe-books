# c-iot-u4: free-model run

- Book: `books/cse/c-iot/c-iot-u4.html`
- Status: problems
- Model calls so far: 33 (127,821 tokens in, 230,824 out), 7.6 minutes

## Checker

```
c-iot-u4.html: 7 chapters, 14114 words, 8 figures, 143 KB
PROBLEMS:
 - text contains "I cannot"
```

## For the reviewer

- chapter 6: the figure cannot be drawn: note "Linux, Uno pins" runs off the right edge; shorten it
- chapter 6: the figure could not be drawn; a plain box diagram stands in for it
- checker: text contains "I cannot"

## Reviewer notes (after any revision)

- ch 1 [high] Section 1 (boards): The sentence 'The barrel jack takes 7–12 V and an onboard regulator makes the 5 V' follows 'Uno, Nano and Mega are 5 V boards', so it reads as applying to all three. The Nano has no barrel jack at all; it is powered from USB or from the Vin pin.
- ch 1 [low] Section 1 (boards): Pin labels are given as 'digital pins 0–13, analog inputs A0–A5' as if this were true of every board, but the table two paragraphs later gives the Nano 8 analog inputs and the Mega 54 digital and 16 analog pins. A student will not know which statement to trust.
- ch 1 [low] Section 1 (boards): 'When memory runs out you change the board, not the code' is too strong. Many sketches fit after small code changes such as storing text in flash with the F() macro or PROGMEM, or using smaller integer types.
- ch 1 [low] Section 2 (IDE): 'The compiler underneath is a C++ compiler for the AVR chip' is written as a general fact about Arduino, but only AVR boards use that compiler; ESP32, STM32 and other families bring their own C++ toolchains through their board packages.
- ch 1 [low] Exam traps (4th trap): 'loop() repeats thousands of times a second' is not generally true: a single delay(1000) inside loop() makes one pass per second. The wording can confuse a student who has just computed a 1 Hz blink.
- ch 2 [high] Worked example 1, [code] block: The code is a desktop C program, not an Arduino sketch. It adds #include <stdio.h>, int main(), and redefines HIGH, LOW, INPUT, OUTPUT, pinMode(), digitalRead() and digitalWrite() as macros and stand-in functions. A student copying this into the Arduino IDE gets a program that will not compile on the board, and may conclude that an Arduino sketch needs main() and stdio.h. The chapter never says this is a host-side simulation.
- ch 2 [high] Section 1, first sentence: 'A sketch is C++ without classes' is false and contradicts the chapter's own Beyond section, which says Arduino C++ supports classes and libraries. Sketches are C++ and can define and use classes freely; only main() is hidden by the core.
- ch 2 [high] Quiz Q6: The answer says the fix is 'Set pinMode or add a pull resistor'. On AVR boards a pin already defaults to INPUT at reset, so calling pinMode(4, INPUT) changes nothing about floating. Floating is cured only by a defined path to 5 V or ground: INPUT_PULLUP, or an external pull-up/pull-down resistor, or driving the pin from a real source. The quiz answer teaches the wrong remedy.
- ch 2 [low] Section 2, 'The pin must be set as INPUT before reading': 'Must' overstates it: pins come out of reset as inputs on AVR boards, so an unset pin still reads. The following sentence about floating then suggests that calling pinMode(pin, INPUT) cures floating, which it does not.
- ch 2 [low] Quiz Q3 answer: '5 V, within the pin current limit' mixes voltage and current and reads as if the answer were about current. A student may copy this into an exam as a confused statement.
- ch 2 [low] Section 1, variable types: int size is not stated. On AVR-based boards int is 16 bits (up to 32767); on 32-bit boards it is 32 bits. A student storing a large reading in an int on an Uno can get overflow without knowing why.
- ch 3 [low] Section 3, UART: The UART description lists only two wires, TX and RX. A student wiring a sensor or a second board will often connect only these two and get no working link, because both ends must also share a 0 V reference.
- ch 3 [low] Figure, stack item 'Linux libraries': The note under 'Linux libraries' is 'gpiozero, smbus'. Both are Python libraries, not Linux system libraries, and placing them below the 'Python / app' layer hides that the app imports them directly.
- ch 3 [low] Section 1, 'RAM chips sit beside it': On some board models the RAM is stacked on top of the SoC package (package-on-package) rather than placed beside it, so the sentence is not true of every Pi.
- ch 3 [low] Quiz Q5 answer: 'Reads may clash' is vague. The concrete failure is that both sensors answer in the same address slot, so their replies overlap on SDA and the data is corrupted.
- ch 3 [low] Lead: 'This chapter looks at the board blocks, the Linux system that starts on power-up, and the serial interfaces' is filler of the kind this book avoids; it delays the content.
- ch 4 [high] Section 3 formula term list and Worked example 1, step 1: The full-scale code is written as "1023 is 210 − 1" and "ADC full-scale code = 210 − 1 = 1023". Without superscript markup this reads as 210 − 1 = 209, which contradicts the stated 1023 and will confuse a student meeting the term for the first time.
- ch 4 [low] Section 3: "you create it with the SPI pins and call adc.value for a channel" mixes two things: the channel is fixed when the MCP3008 object is created, and adc.value is a property (a fraction 0 to 1), not a method you call per channel.
- ch 4 [low] Section 2: GPIO.input(27) is shown working on the header, but RPi.GPIO requires the pin to be set up as an input first, and the setup step is not mentioned.
- ch 5 [high] Section 3, Buzzer bullet: The text says a small buzzer may draw 'under about 30 mA' and that 'a pin can drive them'. Section 1 of the same chapter says to keep an Arduino pin at or below 20 mA. A student who follows the buzzer sentence will drive a pin past the limit the chapter itself set, which is the exact mistake the LED section warns against.
- ch 5 [low] Section 2, first paragraph and Quiz Q1: The step size is given as 5 V ÷ 1024 while the conversion formula used everywhere (and in Q3) is V = reading × 5 ÷ 1023. Both numbers appear without explanation, so a student will not see why they differ and may mix them up.
- ch 5 [low] Section 2, first paragraph: The pointer '(see Chapter 4.4)' is plain text, not a cross-link, so the phone reader cannot jump to the ADC chapter.
- ch 6 [high] Quiz Q6: The answer picks the NodeMCU because its average is about 2.69 mA and claims it can run a year on two AA cells. The arithmetic contradicts the requirement: 2.69 mA for 8760 h is about 23,600 mA·h, while two AA alkaline cells in series store only about 2500 mA·h, so the node would last about 2500 ÷ 2.69 ≈ 930 h ≈ 39 days, not a year.
- ch 6 [low] Worked example 2, step 4 and Quiz Q5: The high threshold is given as the general CMOS rule 0.7 × VDD = 2.31 V. The ESP8266 datasheet value is VIH = 0.75 × VDD = 2.475 V. The conclusion is unchanged, but a student may quote the wrong threshold for this chip.
- ch 6 [low] Section 1 and Worked example 1: The 20 µA deep-sleep figure is for the ESP8266 chip alone. On a stock NodeMCU the 3.3 V regulator and the USB-to-serial chip keep drawing, so the measured board current in deep sleep is roughly a milliamp, not 20 µA. The worked example silently treats a NodeMCU as if it were a bare chip.
- ch 6 [low] Section 3: Cubieboard is described as having Arduino-style headers on some models. Cubieboard boards expose GPIO on plain pin headers, not on an Arduino Uno shield layout, so the claim misleads.
- ch 7 [high] Section 1, second paragraph (sentence on operators): The sentence "Start at ≤ 30 cm and stop at ≥ 90 cm are different from  at the boundary" has a missing comparison, so the student cannot tell what the rule is being compared with. As printed the sentence is incomplete and the point about ≤ versus < is lost.
- ch 7 [high] Section 2, local loop bullet 'Convert': The condition "if h  H, mark the reading invalid" is missing its operator, so the invalidity test is unreadable and a student cannot code it.
- ch 7 [low] Section 2, paragraph on MQTT and HTTP: "HTTP suits simple one-way updates" contradicts the sentence just before it, which correctly calls HTTP the request-reply protocol. A student may conclude HTTP does not wait for a reply.
- ch 7 [low] Quiz Q1: Q1 asks for four steps (answer: sense, decide, act, report), but the local-loop list in Section 2 has five bullets because 'Convert' is listed separately. A student may answer five steps and mark it correct.
