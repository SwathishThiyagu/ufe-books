# c-iot-u1: free-model run

- Book: `books/cse/c-iot/c-iot-u1.html`
- Status: ok
- Model calls so far: 28 (95,864 tokens in, 188,114 out), 4.7 minutes

## Checker

```
c-iot-u1.html: 9 chapters, 16121 words, 10 figures, 175 KB
OK
```

## For the reviewer

- chapter 8: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [low] Section 2: The chapter says 'Eight characteristics appear in most definitions' and then lists connectivity, identity, sensing, actuation, intelligence, energy limit, heterogeneity and dynamic operation. Security and privacy, and scale, appear in the standard lists used in most Indian syllabi and are absent, so the claim about 'most definitions' overstates the list.
- ch 1 [low] Section 1: The heading is 'Definition: thing, internet, service' and the text says 'Three words carry the definition', but four ideas are then explained: thing, internet, service and 'little or no direct human control'.
- ch 2 [low] Section 2, opening line of the five parts: "Every active IoT device has five jobs, and usually five parts" is too strong. Many nodes are input only (a soil-moisture node has no relay or motor), and the chapter's own exam trap says a device needs a control unit, a communication module and a power source, with no mention of an actuator. A student may conclude every device must have an actuator.
- ch 2 [low] Section 1, gateway paragraph: The gateway is called "a device", but the chapter has just defined a device as the package that gives a thing sensing, computation, communication and action. A gateway usually does no sensing or actuation, so the two sentences pull against each other.
- ch 2 [low] Section 3 and worked example 1, step 5-6: The life estimate ignores self-discharge and cell ageing, so 6.2 years looks like a guaranteed field life. A careful reader of a real datasheet will find the number misleading.
- ch 2 [low] Section 1, definition of identity: "The identity may be an RFID tag on a parcel" confuses the carrier of the identity with the identity itself. A tag holds a code; the code is the identity.
- ch 2 [low] Quiz Q4, answer: Saying a passive RFID tag has "no control unit" is loose. The tag chip does contain simple logic and memory for the stored code; what it lacks is a programmable control unit and its own power source.
- ch 3 [high] Section 3, path from thing to service: The path lists Act after Serve. This contradicts the chapter's own figure note, which says actuation is a return path at the device end with sensing. It suggests actuation happens after the service step, which is wrong for most IoT control loops.
- ch 3 [high] Figure: The figure nodes omit Actuation, even though actuation is one of the eight functional blocks and the text says it sits at the device end with sensing. A student sees a diagram missing a block.
- ch 3 [high] Figure: Management and security are shown with only one dashed edge each: management to processing, security to communication. The text says management and security act on all other blocks; security wraps identification, communication and services; management sets sampling interval and checks data arrival. The figure misrepresents them as touching only one block each.
- ch 3 [high] Section 3, security sentence: The text says security wraps only identification, communication and service steps. This contradicts Section 2 ('Security protects all of the above') and Q7, which says management commands can be forged and every block carries risk.
- ch 3 [high] Exam traps, first bullet: The list of verb functions omits act: 'identify, sense, process, communicate, serve, manage, secure.' A student following this trap could leave out actuation, which is a standard functional block.
- ch 3 [low] Section 3, formula D = N × 86400 ÷ T: The formula assumes every source produces exactly one data item every T seconds and that all sources share the same interval T. The chapter does not state this assumption, so students may apply it to mixed or event-driven sources.
- ch 4 [high] Section 3, Choosing a model (repeated in Quiz Q6 answer): The text says a publish-subscribe broker 'sends only when a value changes'. That is not how a broker works. The broker forwards every message it receives to all current subscribers. Deciding to publish only on a change is the publisher's choice (event-driven reporting), not a broker feature. A sensor that publishes the same 31.5 °C every 10 s still causes the broker to forward every one of those messages.
- ch 4 [low] Section 2, APIs expose the models: The example body {value: 31.5, unit: °C} is not valid JSON. Object keys must be quoted strings, and °C must be a string value.
- ch 4 [low] Figure spec: The actors are listed as ['Device', 'API server', 'Client'], so the Client sits on the far right and every arrow runs right-to-left, against the reading order of the caption.
- ch 4 [low] Exam traps, fourth bullet: 'Forgetting the response halves the load' is not generally true; the error depends on the size ratio. In worked example 1, counting only the 300-byte requests gives 5.4 MB per hour instead of 14.4 MB, which is far more than a factor of two.
- ch 4 [low] Section 3, Choosing a model (last paragraph): The sentence 'The API style and the communication model must agree' is contradicted by the example that follows it, where a REST endpoint behind a publish-subscribe broker is still request-response. A student will not know which rule to keep.
- ch 4 [low] Quiz Q6: The answer says publish-subscribe 'removes 500 separate polling requests per second', which is true, but it does not mention that the broker still delivers one copy of each update to each of the 500 viewers. The fan-out traffic to the viewers does not disappear.
- ch 5 [low] Section 1: The five layers are described one by one but never listed in order as a single set, so a student counting them has to infer that application is the fourth layer and business the fifth.
- ch 5 [low] Quiz Q7: The question asks which design principle was ignored (singular), but the answer names two, and energy efficiency is a poor fit for a rising cloud bill; the real cost driver is sending unfiltered data upward (bandwidth and processing cost).
- ch 5 [low] Section 1, last paragraph: The sentence 'The logical design describes functions; a layered architecture arranges those functions into levels' is too vague for a student to tell what a logical design actually contains.
- ch 6 [low] Figure caption: The caption says the wide-area link and the cloud 'sit on opposite sides of the device', but the graph has no device node at all: IoT is the centre, and both the cloud (3,3) and '5G and NB-IoT' (4,2) lie on the same upper-right side. A student reading the caption cannot match it to the picture.
- ch 6 [low] Section 3, edge computing example: The example says the local gateway keeps its last reading during a power cut and uploads later. A power cut also removes power from the gateway and the home router, so the gateway would not be working; the benefit being illustrated is loss of the uplink, not loss of power.
- ch 6 [low] Section 3, fog sentence: 'Fog computing is the older name for the same idea' overstates it. Standard usage treats edge computing as the broad term (computation at the device or the gateway) and fog computing as the specific layer of nodes between device and cloud; it is not just an earlier label for edge.
- ch 7 [low] Section 2, 'Addressing' bullet: NB-IoT is grouped with 6LoWPAN and LoRaWAN as a technology that reaches IP 'through a gateway'. NB-IoT is a cellular technology that gives the device its own IP connection to the operator network; only 6LoWPAN (via a border router) and LoRaWAN (via a gateway) are truly gateway-to-IP paths. A student may conclude that an NB-IoT device needs a separate gateway.
- ch 7 [low] Section 1, third paragraph, and Section 3 table row 'Human role': 'Nobody builds a dashboard on it' and 'Human role: alerts only' overstate the case. The same section names SCADA, and SCADA systems always have operator HMIs; many M2M deployments also have a local monitoring screen. The real difference is that M2M data is not stored with other data or shared with many applications, not that no screen exists.
- ch 7 [low] Section 1, second paragraph: SCADA is listed as if it were a protocol family alongside Modbus and DNP3. SCADA is a system architecture built on protocols; the protocols are Modbus, DNP3, IEC 60870-5 and similar.
- ch 7 [low] Exam traps, first bullet: The sentence 'the two overlap in devices and sensors, they are not nested' is a comma splice, and 'not nested' reads as contradicting Section 2's 'IoT keeps the machine-to-machine core'. Readers can take away either 'M2M is inside IoT' or 'M2M is outside IoT'.
- ch 8 [low] Figure caption and spec (Technical branch): The text calls the technical limit 'energy' but the tree labels the same branch 'Power'. A student may read power and energy as interchangeable quantities, which they are not.
- ch 8 [low] Exam traps, fourth bullet: 'A positive simple ROI does not prove a project is safe' is ambiguous: 'safe' can be read as physical safety, while the point is financial soundness of the business case.
- ch 8 [low] Quiz Q1 model answer: The answer lists 'heterogeneity or interoperability' as one of the technical challenge areas, but Section 1 says variety is not itself a fault and the lead lists only heterogeneity. Including interoperability in the list invites the very confusion the chapter warns against.
- ch 9 [low] Section 1, list of connectivity suppliers: "Network operators supply SIMs, NB-IoT, LoRaWAN or Wi-Fi backhaul" mixes up local links and backhaul. Wi-Fi is a short-range local link, not backhaul, and mobile operators do not normally supply it; LoRaWAN is often run privately by an enterprise rather than a telecom operator, so a student may think all four are the same kind of operator service.
- ch 9 [low] Section 2, business models: "XaaS, everything as a service" is a loose expansion. The usual expansion is "anything as a service", and the sentence reads as if XaaS means only the full outcome bundle.
- ch 9 [low] Section 1, opening lines: "Chapter 1.7 contrasts this with IoT" is a plain-text cross-reference; series convention is a link to the other chapter, and as written the reader on a phone cannot jump to it.
