# c-sec-u6: free-model run

- Book: `books/cse/c-sec/c-sec-u6.html`
- Status: ok
- Model calls so far: 23 (80,422 tokens in, 187,373 out), 5.3 minutes

## Checker

```
c-sec-u6.html: 9 chapters, 16697 words, 10 figures, 185 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3 (Configurations) and the figure: The text says the firewall allows 'VPN and web into the internal LAN' and the figure shows 'allow VPN,443' to the LAN, yet two lines later it says 'The internal LAN is not directly reachable from the Internet.' A student can read this as a contradiction, and inbound TCP 443 straight to internal hosts is unusual when the chapter also says public web servers belong in the DMZ.
- ch 1 [low] Section 2 end ('IDS and IPS detail is in 6.2') and Section 3 end ('Security policy work is in 6.7'): The cross-references to other units are plain numbers, not links, so a reader on a phone cannot tap through.
- ch 2 [low] Lead: "Detection covers what a rule list cannot hold in advance" uses "rule list" for firewall rules, but Section 2 uses "list of rules" for signature rules. A student can read the two lists as the same thing, and then the item "a known attack signature crossing an allowed port" looks like a contradiction.
- ch 2 [low] Section 1, HIDS bullet: "It sees traffic after the host decrypts it" can be read as saying a host-based IDS sniffs the network. A HIDS mainly reads logs, file hashes, processes and system calls; it sees application data in clear only where TLS ends on that host.
- ch 2 [low] Section 3, promiscuous mode paragraph: "On a switched network a plain port sees only broadcast traffic" is not exact: the port also delivers frames to the sensor's own MAC address and multicast frames. Only other hosts' unicast traffic is hidden.
- ch 2 [low] Exam traps, 4th bullet: "3% of 980 beats 90% of 20" is ambiguous: "beats" can be read as "is better than", which is the opposite of the intended lesson that the false alerts simply outnumber the true ones.
- ch 2 [low] Section 2, rule example (code block): The rule snippet is followed by an empty "[shown output]" block. A rule definition produces no output, so the empty output block is misleading.
- ch 2 [low] Section 3, last paragraph on routing: "Autonomous system" and "prefix" are used without definition, and "hijack attempt" is asserted without saying what a hijack is. A reader who has not met BGP cannot follow it.
- ch 2 [low] Worked example 2, opening line: "Second example:" repeats the heading "Worked example 2" and reads as leftover text.
- ch 3 [low] Section 1, first paragraph: "A port scan, a login attempt or a worm probe that reaches it is recorded, not served" reads as if the honeypot never answers. The same paragraph (and the low-interaction definition) says a honeypot emulates fake SSH or HTTP banners, so it does answer. A student may think a honeypot must stay silent.
- ch 3 [low] Section 2, containment paragraph: "hash malware instead of running it" skips a step and can confuse: the sample still has to be captured and stored somewhere before it can be hashed. The point is to avoid detonating it on the sensor.
- ch 4 [low] Section 2 (integer overflow sentence): The wrap example is not what C does. If len is an unsigned 16-bit type, then len + 1 is promoted to int and equals 65536; it does not become 0. The wrap only happens when the arithmetic is done in the same fixed width as the stored size (for example a 32-bit size_t with len = 0xFFFFFFFF). A student may copy the wrong mechanism into an exam answer.
- ch 4 [low] Worked example 1, code and output: The program never calls strcpy or overflows anything. It copies fixed bytes into three separate arrays with memcpy, and the line printf("null index=16\n") prints a hard-coded string. The shown output therefore looks computed but the 17th byte is never written, so the code does not demonstrate the overflow it claims to model.
- ch 4 [low] Worked example 1, step 4 and answer: "Corrupts the next 4-byte word" overstates it. The strcpy terminator writes one zero byte at offset 16, so it changes only the lowest byte of the word after the return address; the other three bytes of that word keep their old values.
- ch 4 [low] Worked example 1, step 2: Bytes 8-11 overwrite the saved EBP, but the step says the field is overwritten "with 0x42". The saved EBP then holds 0x42424242, not 0x42, and the shorthand can confuse readers comparing with the dry-run table.
- ch 5 [low] Section 1, last paragraph (umask): The sentence gives one starting point, 666, and then quotes both 644 and 755. A directory does not start from 666; read as written, a student will compute 666 − 022 = 644 for a new directory and get the wrong mode.
- ch 5 [low] Section 2, PATH attack sentence: The attack is described as if placing a malicious ls in any 'early PATH directory' is enough. It only works if root's search path contains a directory the attacker can write, or if a setuid-root program runs a command by bare name and inherits the user's PATH. Without that precondition a student cannot see why the attack succeeds.
- ch 6 [low] Section 1: getfacl is described as a way to 'test' ACLs. getfacl only prints the ACL entries of a file; it does not test whether a particular access would be allowed.
- ch 6 [low] Worked example 1, parts (c) and (d): Parts (c) and (d) ask the student to give an ACL and a capability list, but the dry run and output replace both answers with the entry count 3. A student may conclude that 'give an ACL' means counting entries.
- ch 6 [low] Section 1: The default-ACL example says the default ACL applies to 'new files in dir1'. Default ACL entries also apply to new subdirectories created inside dir1.
- ch 7 [low] Figure (5 by 5 risk matrix): The matrix uses show_index with index_from 0, so the displayed column numbers run 0 to 4, while impact in the text runs 1 to 5. A student can read the last column as impact 4 instead of 5, and the column axis is otherwise unlabelled.
- ch 7 [low] Section 2, risk score formula: Impact is defined just above as 'the loss if it happens' (a rupee amount), then the formula uses impact as an integer 1 to 5, and later SLE uses a rupee loss again. The same word carries two different meanings without a warning, which can confuse students in the numerical questions.
- ch 8 [high] Section 2: "A security group is a virtual firewall attached to a resource; it allows or denies traffic by port, protocol and source. Rule order matters, as in 6.1." A security group does not evaluate rules in order and does not hold explicit deny rules: all its rules are checked together (allow rules only, with an implicit deny for everything else). Order and priority belong to network ACLs and to rule-list firewalls, not to security groups, so a student who remembers this will answer wrongly.
- ch 8 [low] Section 2: "Logging is a provider service; monitoring and alerting are customer duties" is too absolute. The provider supplies the logging and monitoring service, but the customer must switch logging on, choose what to retain and define the alerts. As written it suggests the customer has nothing to do about logs at all.
- ch 8 [low] Worked example 1, answer: The answer reports "500 users, 3 roles, 90 days of logs" as if they were results. The question asked only for the owner of each control and the two counts; repeating the given numbers as an outcome confuses the student about what was computed.
- ch 9 [low] Section 1, unsupervised sentence: The sentence says the unsupervised model 'sees mostly normal records', which blurs the difference from semi-supervised training defined two sentences later (normal data plus a small labelled attack set). A student can read 'mostly normal' and conclude that unsupervised training uses a few labelled attacks.
- ch 9 [low] Section 3, perturbation bullet: 'Malware appends unused bytes, renames an import or packs a section. The file looks harmless' conflicts with Section 4, which recommends section entropy as a robust feature because packing raises entropy. Packing does not make a file look harmless to an entropy-based model; it makes it look packed.
- ch 9 [low] Quiz Q1: The question asks for 'the two label settings', but Section 1 describes three (supervised, unsupervised, semi-supervised) and calls semi-supervised the common case in practice. The answer omits semi-supervised, so a student who writes it would be marked wrong against this key.
- ch 9 [low] Quiz Q7: The question asks 'which feature is fragile' (one feature), but the answer correctly says both the file name and the known string are fragile. Question and answer do not match.
- ch 9 [low] Quiz Q8: The answer mixes levels of the taxonomy. Perturbation is how an evasion attack is carried out, not a separate attack class, and a backdoor is a form of poisoning, not 'a fourth' type.
