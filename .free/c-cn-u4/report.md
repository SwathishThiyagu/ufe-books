# c-cn-u4: free-model run

- Book: `books/cse/c-cn/c-cn-u4.html`
- Status: ok
- Model calls so far: 36 (138,549 tokens in, 252,168 out), 6.8 minutes

## Checker

```
c-cn-u4.html: 9 chapters, 16140 words, 10 figures, 184 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Exam traps, item 5: It says 172.16.0.0/12 is wrongly seen as "three separate class B networks". The count is wrong: /12 covers 172.16.0.0 through 172.31.255.255, which is 16 class B (/16) networks, not three. The rest of the trap (one prefix, mask 255.240.0.0) is right, so the wrong number teaches a false fact.
- ch 1 [low] Section 2: "0.0.0.0 means this host or any address in a routing table" is too compressed. A student may not see that the meaning depends on where the address appears (source address versus routing-table entry).
- ch 1 [low] Figure: The Hosts note ".4.1 to .7.254" is written as octet fragments with no full address, so on a phone it reads like a different network from the one in the same figure.
- ch 2 [high] Section 1, the sentence about 192.168.1.64/26 and the sentence about borrowing s bits: The powers of two lost their superscripts, so the text states false arithmetic: "host bits h = 6, so there are 26 = 64 addresses" (26 is not 64) and "you create 2s equal subnets" (2s, not 2^s). A student reading quickly will be confused about where the 64 comes from.
- ch 2 [high] Worked example 1, step 1: The justification for h = 7 is garbled and mathematically unreadable: "h = 7 because 26 − 2 = 62 7 − 2 = 126 ≥ 100". The powers are lost and the required comparison symbol is missing, so the chain reads as 62 7 − 2 = 126.
- ch 2 [high] Section 2 bullet list, worked example 1 steps 2, 3 and 4, quiz Q3 and quiz Q4: The same superscript loss makes every remaining power of two read as a plain multiplication: "2h − 2 ≥ required hosts", "26 − 2 = 62 ≥ 50", "25 − 2 = 30 ≥ 25", "24 − 2 = 14 ≥ 10", "Usable hosts = 25 − 2 = 30", "25 − 2 = 30 is too small. 26 − 2 = 62 ≥ 45". Each line as printed is arithmetically false.
- ch 2 [low] Section 1, sentence after the subnets formula: "Each new subnet has h = old host bits − s host bits" is clumsy; "s host bits" reads as a quantity of host bits rather than the number borrowed.
- ch 3 [low] Section 1: Padding is listed as something the options field can 'add', next to timestamp and route. Padding is not an option type; it is filler bytes (end-of-list / no-op) that make the header a whole number of 32-bit words.
- ch 3 [low] Section 3, last paragraph: The sentence 'so routers and hosts may rate-limit ICMP and fragment queues' joins two unrelated defences. Limiting ICMP does not protect the memory used to hold half-complete fragment sets, so the reason-and-remedy link is broken and students may copy it as cause and effect.
- ch 3 [low] Figure caption: 'The offsets jump by 185 and 370' can be read as steps of 185 and then 370, but the offsets are 0, 185 and 370 (each step is 185). The wording is ambiguous about what the numbers are.
- ch 4 [low] Worked example 1, step 4 and answer line: The prefix is written 2001:db8:0:0::/64. This expands correctly, but it leaves zero groups 3 and 4 uncompressed while :: is used for a shorter zero run. That contradicts the compression rule taught just above in Section 1 (compress the longest run of zero groups). A student copying this pattern will get non-canonical prefixes.
- ch 4 [low] Quiz Q6: The question asks for one difference between the IPv6 hop limit and the IPv4 TTL, but the answer only says the field is renamed and then gives 'It is 8 bits'. The IPv4 TTL is also 8 bits, so that sentence reads like a difference when it is not, and no real difference is stated.
- ch 5 [high] Quiz Q8: The answer says 'an application gateway or passive mode may help' for an FTP server on a private host. This is backwards. For a server behind NAT, passive mode is exactly what breaks: the server's 227 reply carries its private IP address inside the payload, which NAT does not rewrite, so the outside client cannot open the data connection. Passive mode helps when the client, not the server, is behind NAT.
- ch 5 [low] Section 2, ICMP paragraph 1: 'the first eight bytes of the packet' is ambiguous. A student may read it as the first eight bytes of the IP header, not the first eight bytes of the original datagram's data after the header.
- ch 5 [low] Section 2, ICMP paragraph 1: The 'ICMP does not report every problem' point gives only one case. The other standard exceptions are missing, so a student may think that case is the only one.
- ch 5 [low] Section 4 example table and Worked example 1 step 5: The private port 4000 maps to the same public port 4000. This is legal, but the example is supposed to demonstrate PAT, and a student may conclude that PAT leaves the port unchanged. The quiz (Q4, Q7) does use different ports, which makes the mismatch more confusing.
- ch 5 [low] Worked example 1, step 4; Figure aria: 8.8.8.8 is Google's public DNS resolver, not a web server on port 80. Using a real address as an HTTP server is a sloppy teaching example and invites wrong assumptions about what runs there.
- ch 5 [low] Section 1, RARP sentence: 'DHCP replaced it' skips BOOTP. Historically RARP was replaced by BOOTP, and DHCP extended BOOTP.
- ch 6 [low] Section 3 and Exam traps: The chapter gives only 'contiguous addresses' as the condition for one summary prefix. Contiguity alone is not enough: the block must also be aligned, that is, it must have a power-of-two size and start at a multiple of that size. A student who follows the stated rule could wrongly 'aggregate' 10.0.1.0/24 to 10.0.4.0/24 (contiguous) into a /22 such as 10.0.1.0/22, which is not a valid network address for a /22 and does not cover the four networks cleanly.
- ch 6 [low] Section 2 table and Quiz Q6: 'Default route' is used twice (table row 'Best use: Stub, small, default route'; Q6 answer 'A single default static route works') but is never defined. A first-time reader does not know it means the 0.0.0.0/0 entry that matches every destination when no longer prefix matches.
- ch 6 [low] Section 1 (longest prefix match paragraph): The rule is stated only for the case where several entries match. It does not say what happens when no entry matches, which students often ask and which ties directly to the default route mentioned later.
- ch 7 [high] Section 3, first paragraph (RIP metric definition): The metric is described as 'one network or router crossed costs 1'. Counting routers contradicts the chapter's own worked case: in A—B—C only one router (B) is crossed, yet the cost from A to C is given as 2. The standard definition (and the 'directly connected networks have cost 1' line) counts networks/subnets on the path, not routers.
- ch 7 [low] Section 2, hold-down bullet: 'Bad news gets time to spread' states the purpose backwards. Hold-down exists so that a router does not install a new (possibly looped) route in the window before the bad news has reached everyone.
- ch 8 [low] Section 1, age field: The text says the age field 'is reduced as time passes', which is the older generic link-state convention. In OSPF, whose LSAs are introduced in Section 3, the LS age counts upward: it starts at 0 and reaches MaxAge (3600 s), after which the LSA is re-flooded and removed. A student may carry the wrong direction into an OSPF answer.
- ch 8 [low] Section 3, router names: The abbreviation ASBR is expanded as 'autonomous system border router'. OSPF documents and standard textbooks use 'autonomous system boundary router'. An examiner may mark the expansion as non-standard.
- ch 9 [high] Section 2 selection order, Section 3 policy paragraph, Quiz Q7: MED is treated as a general tie-breaker that can be compared across different neighbouring ASes. By default BGP compares MED only among routes received from the same neighbouring AS; MED is also non-transitive. Q7 compares MED 50 from ISP A with MED 80 from ISP B and says 50 wins, and Section 3 says MED can steer inbound traffic across two ISPs. Both are wrong or misleading under standard BGP.
- ch 9 [high] Figure: The node AS10 is labelled with note 'origin'. In BGP the origin AS is the last AS in AS_PATH (AS30 or AS60 in this example); AS10 is the local/receiving AS where the route decision is made. The figure also marks AS30 and AS60 both as 'prefix' for the same /24 without explaining that this means multi-origin.
- ch 9 [low] Section 1 and Quiz Q1: 'nearest AS first' is ambiguous. A student may read it as nearest to the origin AS. BGP puts the most recently added AS, closest to the receiving AS, first, and the origin AS last.
