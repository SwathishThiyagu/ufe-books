# c-sec-u1: free-model run

- Book: `books/cse/c-sec/c-sec-u1.html`
- Status: problems
- Model calls so far: 35 (134,402 tokens in, 219,546 out), 8.4 minutes

## Checker

```
c-sec-u1.html: 7 chapters, 14561 words, 8 figures, 152 KB
PROBLEMS:
 - chapter "network-attacks-dos-ddos-mitm-replay-port-scanning": 1901 words is too long (keep under 1900; 900-1600 is the target)
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 4 vs Worked example 1, step 3: The formula defines A as availability in percent, A = (T − D) ÷ T × 100, but step 3 writes A = 43092 ÷ 43200 = 0.9975 and then step 4 multiplies by 100. The same symbol A is used first for a fraction and then for a percentage, which will confuse a student copying the steps.
- ch 1 [low] Figure caption: The caption says each branch names the failure that breaks 'the promise above it', but in the figure the promises (the three goals) are below the message and the failure labels sit on the branches leading to them. 'Above' points the wrong way and a student reading the caption against the diagram will be misled.
- ch 1 [low] Lead: The lead says every security requirement met this year is one of three promises, but Section 2 then adds authentication, accountability and non-repudiation. The absolute claim contradicts the rest of the chapter.
- ch 1 [low] Quiz Q5: The answer classes the salary sheet as 'Internal, staff and HR only', but the chapter's matrix used Internal for the marks sheet read by exam-cell staff only. So 'Internal' appears to mean two different sets of readers, and the class stops being a fixed rule.
- ch 2 [high] Section 1 (passive and active attacks), exam trap 2, and Quiz Q5: The chapter states flatly that 'A replay is fabrication' and keys the answer to Q5 to that. Its own definition of fabrication is 'a new message is inserted and made to look like it came from a real sender', which a replayed copy is not: the copy is old and the sender is genuine. Standard treatments do not agree here; replay is commonly placed under modification (an old message is substituted for the fresh one expected, so the stream is altered) and sometimes under fabrication (a copy is inserted). Presenting one choice as fact will cost students marks against an answer key that uses the other.
- ch 2 [high] Worked example 1, step 4 and the answer: 'Attack class = fabrication/repudiation' contradicts the chapter's own line in Section 1, 'Every named attack is one of them', since repudiation is not one of the four classes. A sender who really sent the file and then denies it is not fabricating a message; X.800 treats repudiation as a separate threat against which the non-repudiation service is defined. The hybrid label also teaches a phrase that examiners do not accept as an attack class.
- ch 2 [low] Worked example 1, step 1 (event a): The event says the file body 'is unreadable', so confidentiality was not broken. The question then asks for 'one mechanism that would have prevented it', and the answer gives encipherment, which is already in place. A student will be unsure whether to name the mechanism already working or a further one.
- ch 2 [low] Lead paragraph: The lead says 'Attack classes, the X.800 service list and the X.800 mechanism list are the standard vocabulary for all three'. Only the service and mechanism lists come from X.800; the four attack classes come from the OSI-model attack taxonomy (interruption, interception, modification, fabrication) as presented in the standard security texts. A reader may wrongly cite X.800 for the four classes.
- ch 3 [low] Section 3, last sentence: The sentence 'Some syllabi call this compiling observations from organisational risk documents into a fixed table format, one column per field' does not parse and attaches no clear meaning to 'this'. A student cannot tell what is being named.
- ch 3 [low] Worked example 1, step 1 and step 2: The count of exposed servers (100) is computed but never used again; the risk uses one firm-wide likelihood. A student may wonder whether 0.20 is the chance per server or for the whole firm, and the two readings give very different answers (₹10,00,000 versus ₹10,00,00,000 per year).
- ch 3 [low] Exam traps, first bullet: 'risk is the expected damage, in rupees or in a severity score' contradicts the chapter's own definition. Risk is money per period (L × I). CVSS gives a 0 to 10 severity score; a severity score is not risk.
- ch 3 [low] Beyond: 'CVSS scores are combined with local context in schemes such as EPSS' is misleading. EPSS is an independent data-driven model that estimates the probability a CVE is exploited in the next 30 days; it does not take CVSS scores as its input.
- ch 3 [low] Section 1, exposure definition: Exposure is defined as a count ('100 servers, one database, 4,000 accounts'). Standard usage treats exposure as the state of being open to loss, and reserves counts for the asset inventory; the word is also easily confused with exposure factor (EF) in Section 4.
- ch 3 [low] Section 3, CVE bullet: 'CVE-YYYY-NNNN' implies exactly four digits and suggests the year is the year the flaw was found. The sequence part may be four or more digits, and the year is the year the ID was assigned, not the year of discovery.
- ch 4 [high] Quiz Q8, answer: The answer says a TCP connect scan gets RST from a closed port 'after the handshake'. No handshake happens on a closed port: the client's SYN is answered by RST and the connect() call fails immediately. A student would wrongly learn that a closed port completes a handshake.
- ch 4 [low] Section 4, scan table (FIN / NULL row): The table shows 'no reply' for both open and filtered ports on FIN and NULL scans, but the text never says these two states cannot be told apart. Only the UDP row carries that warning, so a reader may think the table separates open from filtered for FIN/NULL.
- ch 5 [low] Section 1, opening line and bullet list: 'Malware spreads by one of three routes' is not true of a trojan: a trojan does not spread at all, the attacker or the user carries it, and Section 4 later says a trojan may skip propagation entirely. A student meets a contradiction between the two sections.
- ch 5 [low] Section 1 bullets and Section 2, boot sector virus: The bullet 'Needs a host file plus a user action → virus' is too absolute. A boot sector virus runs when the machine boots from an infected disk; nobody opens a file.
- ch 5 [low] Section 3, and Worked example 1 part (d): 'A worm offers one door to close ... one patch closes the only door' contradicts the Morris worm paragraph just above it, which lists three entry points (the mail program, another network service, weak passwords). A student may conclude a worm always has exactly one vector.
- ch 5 [low] Worked example 1, step 8: 'A virus with the same speed would still need 64 users to open the infected file by 10:00' is off by one — the first machine is already infected, so reaching 64 machines needs 63 further openings — and it suggests people open files on a fixed 10-minute timetable, which is exactly what a virus cannot rely on.
- ch 5 [low] Section 1, definition of vector: 'a plugging-in USB stick' is awkward phrasing that reads badly for a second-language reader.
- ch 6 [low] Section 1, after the four bullet definitions: The sentence 'Only baiting needs technology' contradicts the chapter's own quid pro quo example, where the victim is asked to install a remote-access tool. Pretexting also often ends at a fake login page.
- ch 6 [low] Section 2 definition and variants table (Pharming row): The section defines phishing as social engineering delivered as a message, then lists pharming as a variant with channel 'Browser'. Quiz Q4 correctly says pharming needs no message. A student can read the table as 'pharming is a kind of phishing mail'.
- ch 6 [low] Section 2, 'Read a domain from the right': The rule is stated only for .com. It fails for icici-bank-verify.co.in, mail.icicibank.com.secure-login.top, and other public suffixes an Indian reader meets daily.
- ch 6 [low] Worked example 1, steps 2 and 5: Step 2 labels 50 captured username-password pairs as '50 accounts', and step 5 labels 25 pairs as '25 passwords'. Credentials captured and accounts actually taken are different quantities; the example's own step 6 depends on that difference.
- ch 6 [low] Section 3, Mail bullet (DMARC): 'DMARC tells the receiver what to do when SPF and DKIM both fail' skips alignment, which is the whole point of DMARC; a mail can pass SPF for the envelope domain and still fail DMARC.
- ch 6 [low] Whole chapter, first use of abbreviations: MFA appears first in the figure note and the worked example with no expansion, and OTP, CVV, KYC and VPN are never expanded. The instruction is to define each term at first use.
- ch 7 [low] Section 3, opening paragraph vs table: The paragraph defines remote access attacks as attacks on 'the service that is meant to let an administrator in', but the table then lists web shells and remote access trojans, which are not remote access services being attacked. A student may think a RAT is a service exposed on the machine.
- ch 7 [low] Figure spec: The edge label 'HTTPS beacon' sits on the Botmaster → C2 server edge, but beacons travel from the bots to the C2 server, not from the botmaster. The direction shown contradicts the text and the aria description.
- ch 7 [low] Section 1, jitter paragraph (and formula): 'Jitter is a random extra delay, say 20%, added to that interval' means every check-in comes later than T, so the real rate is lower than 3600 ÷ T. The formula is then only approximately right.
- ch 7 [low] Worked example 1, step 6: 'Rate limiting at the login page plus MFA reduces successful logins to 0' is stated as an absolute. MFA removes credential-stuffing success only where it is enforced on every account; it is not a guarantee of zero.
- ch 7 [low] Lead and table (DDoS, RDP, SSH, MFA, IDS): Several acronyms are used without being expanded at first use, which the rest of the chapter does for bot, C2, DGA and RAT. A second-language reader may not know RDP or MFA.
