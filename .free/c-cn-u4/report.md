# c-cn-u4: free-model run

- Book: `books/cse/c-cn/c-cn-u4.html`
- Status: problems
- Model calls so far: 31 (100,407 tokens in, 106,115 out), 4.3 minutes

## Checker

```
c-cn-u4.html: 9 chapters, 11943 words, 10 figures, 138 KB
PROBLEMS:
 - page is wider than the screen at 390px (467>390): a table, figure or long word overflows
```

## For the reviewer

- chapter 9: a c program's shown output was replaced by its real output; check the text around it
- chapter 8: a c program's shown output was replaced by its real output; check the text around it
- chapter 3: a c program's shown output was replaced by its real output; check the text around it
- chapter 4: a c program's shown output was replaced by its real output; check the text around it
- checker: page is wider than the screen at 390px (467>390): a table, figure or long word overflows

## Reviewer notes (after any revision)

- ch 1 [high] Worked example 1, steps 5‑6 and final answer: The example claims that 256 usable hosts can be obtained with a /24 prefix (8 host bits). However 8 host bits provide only 2⁸‑2 = 254 usable addresses, which is insufficient for the required 256 hosts. The correct smallest prefix that supports 256 usable hosts is /23 (9 host bits), giving 2⁹‑2 = 510 usable addresses.
- ch 2 [low] Section 3, first paragraph: The sentence "An address block is written as network/." is missing the prefix length placeholder after the slash.
- ch 2 [low] Quiz Q4: The question says "subnets that each support at most 100 hosts" but the answer gives a /25 subnet which provides 126 usable hosts, exceeding the stated limit.
- ch 2 [low] Section 2, step list: The phrase "Record the first subnet address (base address)" can be confused with the first usable host address.
- ch 2 [low] Section 2, step list: The instruction "Add the subnet size to obtain the next subnet’s base address" may be misread as adding to a host address.
- ch 2 [low] Section 2, example table: Column header "First address" is ambiguous; readers may think it refers to the first usable host address.
- ch 2 [low] Figure specification block: The JSON‑like spec uses single quotes, which is not valid JSON and may confuse students learning JSON syntax.
- ch 3 [high] Section 3 (Reassembly at the destination): The reassembly buffer is said to be sized to the Total Length of the first fragment received. The first fragment may not contain the total length of the original datagram, so the buffer size can be insufficient.
- ch 3 [high] Quiz Q2: The answer states that 8191 × 8 = 65 536 bytes, which is incorrect; 8191 × 8 = 65 528 bytes, and the maximum IPv4 datagram size is 65 535 bytes.
- ch 3 [high] Section 3 (Reassembly at the destination): The ICMP message described for a reassembly timeout is named "Destination Unreachable – Fragment Reassembly Time Exceeded", which is wrong. The correct message is ICMP Type 11 (Time Exceeded), Code 1 (Fragment Reassembly Time Exceeded).
- ch 3 [low] Section 2 (MTU and fragmentation rules): The rule "Divide the payload into chunks that are multiples of 8 bytes" does not mention the exception that the last fragment may have a payload length not a multiple of 8 bytes.
- ch 3 [low] Quiz Q5: The answer contains contradictory wording: it first says there is a gap of 0 bytes after the second fragment, then says the packet is complete. This may confuse students.
- ch 4 [high] Section 2: The text says "IPv6 defines three unicast scopes: global, link‑local and unique‑local." Unique‑local is not a scope; it is a type of unicast address with a site‑local scope.
- ch 4 [low] Quiz Q2: Answer states that ":: replaces the longest run of consecutive zero groups". The rule allows :: to replace any run of one or more consecutive zero groups, but the convention is to use the longest run for compact representation.
- ch 4 [low] Section 3: Payload Length description says "size of the data after the header" which may be interpreted as only the upper‑layer data and ignores extension headers.
- ch 5 [high] Section 1: The text says “ARP works only in IPv4 networks that use Ethernet.” This is incorrect; ARP works over any IPv4 broadcast link layer, not just Ethernet.
- ch 5 [high] Worked example 1, step 8: The example treats ICMP as having a source port (“Router rewrites src IP … and src port to 54321”). ICMP does not have ports; NAT for ICMP only rewrites the source IP (or the ICMP identifier field).
- ch 5 [low] Section 1, ICMP ping description: It says “Router forwards the packet to Host B.” For hosts on the same LAN the packet is delivered directly, not via a router, which may confuse students.
- ch 5 [low] Section 2, DHCP retry description: The sentence “If the client does not receive DHCPOFFER, it retries after a timeout.” does not specify what is retried, leading to ambiguity.
- ch 6 [high] Section 1 (Static routing): The text says "Metric is optional; usually set to 1" for static routes. In most router implementations static routes do not use a metric for route selection; they use an administrative distance (often 1) and the metric field is ignored or not present.
- ch 6 [low] Section 2 (Dynamic routing) – bullet "Router sends hello messages to discover neighbors": Hello messages are specific to OSPF (and some other link‑state protocols). Protocols like RIP use request/response messages, not hello packets.
- ch 6 [low] Section 2 (Dynamic routing) – sentence "Cost is usually the inverse of bandwidth": The wording is imprecise. OSPF cost is defined as reference bandwidth divided by link bandwidth, not simply the inverse of bandwidth.
- ch 6 [low] Section 2 (Dynamic routing) – list "Common protocols are OSPF, RIP, and BGP": BGP is an exterior gateway protocol, not an interior dynamic routing protocol like OSPF and RIP.
- ch 6 [low] Section 3 (Hierarchical routing) – bullet "Core router only stores routes to other areas, not to each host inside them": The statement should refer to network prefixes, not individual hosts.
- ch 6 [low] Worked example 1 – OSPF next‑hop address: The example uses next‑hop 192.168.1.2 without stating where that address comes from, which may confuse students.
- ch 6 [low] Quiz Q5 – answer explanation: The answer mentions a "more specific summary for its own subnet," which is inaccurate; the department router simply has its own directly connected prefixes and receives only the summary from the ABR.
- ch 7 [low] Section 2: The hold‑down timer is described as "to suppress flapping routes", which is inaccurate.
- ch 7 [low] Section 2: The term "Trigger updates" is used instead of the standard "Triggered updates".
- ch 7 [low] Section 2 and Quiz Q2 answer: The phrase "neighbours may still advertise the old cost for one period" suggests only a single update interval, which can mislead students.
- ch 7 [low] Section 3: Split horizon is described without mentioning the common variant "split horizon with poisoned reverse", which many textbooks include.
- ch 8 [high] Section 1, cost description: The text says “The cost is a numeric value that represents the bandwidth of the link.” Cost does not represent bandwidth; it is inversely proportional to bandwidth.
- ch 8 [high] Figure caption: The caption states that edge labels are “link cost in rupees per megabyte”, which gives the cost a monetary unit that OSPF does not use.
- ch 8 [high] Section 3, summary LSAs: It says a summary LSA advertises the total cost to reach an external network. Summary LSAs are for inter‑area routes, not external (AS‑External) routes.
- ch 8 [high] Section 2, SPF step description: The step “Update the distance of each neighbor: new = distance(source) + link cost.” incorrectly uses the word “source” for every iteration.
- ch 8 [low] Section 2, initial visited set: The step list marks the source as visited before any node selection, which can confuse beginners.
- ch 8 [low] Section 2, dry‑run table: The table header “Dist[2]” and the layout are unclear and add no value.
- ch 9 [high] Worked example 1 (section describing route propagation): The example states that LOCAL_PREF is changed and advertised to external ASes (AS65001 and AS65100). In BGP, LOCAL_PREF is a well‑known discretionary attribute that is never sent to external peers; it is used only inside a single AS.
- ch 9 [low] Lead paragraph: The term "UPI" is used for a campus network that pays for traffic, which is unrelated to networking.
- ch 9 [low] Section 1: Path‑vector idea and AS numbers: It says each AS is assigned a unique 16‑bit number. Modern BGP also supports 32‑bit AS numbers (AS4).
- ch 9 [low] Figure spec (sequence diagram): The third message shows AS65100 sending a BGP UPDATE to AS65001 labeled "Best path selected", which is not a BGP message and the direction is incorrect.
- ch 9 [low] Dry run table in Worked example 1: Row 1 lists AS_PATH = [64512] while the description of Step 1 says the AS_PATH after AS65001 adds its ASN should be [65001,64512].
- ch 9 [low] Quiz Q6: It lists LOCAL_PREF as an optional attribute for inbound traffic engineering, but LOCAL_PREF is a well‑known discretionary attribute used internally, not for inbound engineering.
