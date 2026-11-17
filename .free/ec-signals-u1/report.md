# ec-signals-u1: free-model run

- Book: `books/ece/ec-signals/ec-signals-u1.html`
- Status: ok
- Model calls so far: 29 (109,053 tokens in, 230,264 out), 5.6 minutes

## Checker

```
ec-signals-u1.html: 7 chapters, 13228 words, 8 figures, 140 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: note "x(-t)=-x(t)" runs off the right edge; shorten it
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, definition of DT signal and the sampling formula that follows it: The prose says n = 0, 1, 2, … but the formula two paragraphs later uses n = 0, ±1, ±2, …. A student may think negative indices are forbidden in one place and allowed in another.
- ch 1 [low] Section 1, paragraph on x[n]: 'One value x[n] is called a sample when it came from a measurement' ties the word sample to measurement. In standard usage any single value of a discrete-time sequence is a sample, whether measured, counted or produced by a formula such as x[n] = 3 cos(0.25πn).
- ch 1 [low] Section 2, bullet list: The bullet says 'A CT input with a DT output is a conversion, not a plain CT or DT system', and Q7 repeats 'not a CT or DT system in the simple sense'. Read together with the earlier definition ('a system is an operator that turns an input signal into an output signal'), a student can conclude the sampler is not a system at all.
- ch 1 [low] Section 2, 'Systems are split into CT and DT in 1.5': The forward reference is ambiguous: this chapter already splits CT and DT systems in Section 3, so '1.5' reads like a section of this chapter rather than a later chapter.
- ch 2 [low] Section 1, energy formula note: The note says "|x(t)|² is instantaneous power" without the 1 Ω condition, while the 1 Ω condition is applied only to the units of E. A reader can carry away the idea that |x|² is power in general, which is false when x is a voltage or current.
- ch 2 [low] Section 1, DT energy and power formula note: "P the same units per sample" is dimensionally wrong. The count 2N+1 is a pure number, so dividing by it does not change units; DT average power has the same units as DT energy, namely (sample value)².
- ch 2 [low] Section 2, last paragraph: The rational-ratio rule for sums of periodic signals is a CT result. It is placed right after the DT sentence, so a student may conclude that a sum of DT periodic signals can be aperiodic. In DT the periods are integers, so a common multiple always exists and the sum is always periodic.
- ch 3 [high] Lead: The lead says a ramp models 'a constant acceleration'. A ramp r(t)=t rises at a constant rate, so it models a quantity changing at constant speed (constant velocity), not constant acceleration; constant acceleration gives a parabola (t² term).
- ch 3 [high] Section 1, and repeated in Quiz Q1 answer: The definition of the unit step is broken: 'Unit step u(t) is 0 for t0' has no condition for t>0, so the signal is never defined to be 1. The same broken text appears in the Q1 answer.
- ch 3 [high] Section 2: The growth/decay sentence is broken: 'If a0 it grows' gives no condition for decay and no value for a=0, so a student cannot tell which sign does what.
- ch 3 [low] Section 1, sifting property formula: The sifting property holds only when x(t) is continuous at t=t0; the note under the formula does not state this condition, and students then apply it to signals with jumps.
- ch 4 [high] Lead and Exam traps, first bullet: The claim that x(2t − 1) is not obtained by 'shift by 1, then compress', and that shifting first by 1 and then replacing t by 2t gives x(2t − 2), is wrong. Replacing t by 2t in x(t − 1) gives x(2t − 1), which is exactly the waveform wanted. This also contradicts Section 4, which correctly lists 'shift first, then scale' as a valid recipe, and contradicts the answer to Q6, which correctly says the shift parameter is not multiplied by 2. The real mistake is not the order of operations but reporting the delay as 1 s.
- ch 4 [low] Quiz Q6: The student's quoted step is muddled: delaying x by 4 s and then compressing by 2 does not give x(2t − 8); it gives x(2t − 4), the very signal the student is asked about. Only the answer's last line (delay = 4/2 = 2 s) states the real error, so the question reads oddly and repeats the wrong arithmetic of the first exam trap.
- ch 5 [high] Section 2, last paragraph ('When blocks are linear and time-invariant...'): The text says series and parallel connections 'reduce to multiplication and addition of impulse responses'. In the time domain this is wrong: two LTI systems in series have overall impulse response h₁(t)*h₂(t) (convolution), not h₁(t)·h₂(t). Multiplication holds only in the transform domain, and no transform is named here. A student will carry 'multiply the impulse responses' into the exam.
- ch 5 [low] Exam traps, fourth trap: 'A fixed over-amplifying system can be time-invariant and unstable' is misleading. A memoryless fixed gain y(t)=Kx(t) is BIBO stable for every finite K, however large, so the example does not support the (correct) point that stability and time invariance are independent. It also sits oddly with the earlier statement 'An audio amplifier with a fixed gain is stable'.
- ch 5 [low] Section 4, reading rules (third bullet): The rule 'If only x(t) or only x[n] appears, the system is memoryless' does not cover scaled arguments. In y(t)=x(2t) or y[n]=x[2n] only the symbol x appears, so a student may wrongly call it memoryless, when the output at t uses the input at another time (2t) and is also noncausal.
- ch 6 [high] Exam traps, third trap: The trap tells the student that examiners give a system 'that passes one and fails the other, such as y(t) = x²(t)', but x²(t) fails both conditions: scaling gives T{a x} = a²x² ≠ a x², and additivity gives (x₁ + x₂)² ≠ x₁² + x₂². The example contradicts the point it is used to make, so a student memorising this trap learns the wrong thing.
- ch 6 [low] Worked example 1, dry run table: The first two rows label the tested quantities as 't x(t)' and '(t − 1) x(t)'. The quantities actually computed are t x(t − 1) and (t − 1) x(t − 1). With the constant test input 2 V the numbers come out the same, but the labels are wrong notation and can confuse a student about what was shifted.
- ch 6 [low] Section 2, LTI sentence: 'For a linear time-invariant (LTI) system the two properties have crisp tests on the impulse response h(t)' — the phrase 'the two properties' is never defined here. The reader cannot tell whether it means CT and DT, or causality and stability (stability is only treated in Section 3).
- ch 7 [low] Lead: The lead says the norm measures a signal's size, "which here is its energy". The norm is the square root of the energy; saying the norm is the energy is a definitional slip a student may carry forward.
- ch 7 [low] Section 1 (inner product): "A large value means the two signals rise and fall together" ignores sign and magnitude. A large negative inner product means the signals are near-negatives of each other, and for complex signals ⟨x, y⟩ is complex, so the size being judged is |⟨x, y⟩|.
- ch 7 [low] Section 2 (orthogonal sets): The definition "⟨φ_m, φ_n⟩ = 0 for every m ≠ n" is satisfied by a set that contains the zero signal. Then ‖φ_n‖² = 0, the coefficient formula c_n = ⟨x, φ_n⟩/‖φ_n‖² divides by zero, and the zero element adds nothing to the span.
- ch 7 [low] Section 3 table: The vector row "‖u‖² = Σ u_n²" uses plain squares, but the chapter works with complex signals and the signal column correctly uses |c_n|². For complex vectors the squared modulus is needed, otherwise the two rows disagree.
- ch 7 [low] Beyond: "Wavelets ... stay orthogonal, which is why JPEG 2000 works" overstates the case. The default JPEG 2000 wavelet filters are biorthogonal; they need a dual basis rather than strict orthogonality, so the stated reason is not accurate.
