# c-block-u3: free-model run

- Book: `work/claude_figs/c-block-u3/tree/books/cse/c-block/c-block-u3.html`
- Status: ok
- Model calls so far: 36 (144,070 tokens in, 242,122 out), 7.6 minutes

## Checker

```
c-block-u3.html: 7 chapters, 13953 words, 8 figures, 156 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, first two paragraphs, and exam trap 5 / Q7: The chapter states that Bitcoin floods messages 'to neighbours with a time-to-live (TTL) counted in hops' and that 'many peers receive the same message'. Bitcoin does not use hop-count TTL flooding. A node announces a 32-byte inventory hash (inv) to its peers; a peer that does not already have the transaction asks for it with getdata; and each node keeps a record of what it has already seen and does not announce it again. TTL flooding is the Gnutella-style mechanism. A student who writes 'Bitcoin uses TTL flooding' in an exam is stating a wrong protocol fact.
- ch 1 [low] Section 2, 'Structured lookup': 'Each node keeps contacts whose IDs are close to its own' is misleading for Kademlia. A node keeps a few contacts in every distance band from itself, out to the far side of the ID space (k-buckets), so it always holds some far-away contacts. That is exactly why each hop can halve the remaining distance.
- ch 1 [low] Section 3, heading and third paragraph: The heading says 'Types in blockchain', but the paragraphs classify overlays into unstructured, structured and hybrid — repeating Section 1's architecture list — and 'hybrid' is given a second meaning here (a few well-connected nodes plus flooding) that differs from Section 1's hybrid (supernodes and bootstrap servers). A student can end up with two incompatible definitions of one word.
- ch 1 [low] Section 1, 'Short history': 'BitTorrent (2001) ... used a tracker or a DHT to find holders' is anachronistic. BitTorrent in 2001 used a central tracker; trackerless operation over a DHT came some years later.
- ch 1 [low] Worked example 1, final answer: The answer says 'The peers send 39 copies in all', but the 39 already includes the 3 copies sent by the originator, and the next clause counts the originator's own copy again as a separate item. The arithmetic is right; the wording makes it look as though the originator is not a peer.
- ch 2 [low] Section 3, Exam traps (stale block bullet), Quiz Q7: The stale block's coinbase is called 'invalid'. The coinbase transaction in a stale block does not break any rule; it simply is not on the best chain, so its output never matures and can never be spent. Calling it invalid suggests the miner broke a consensus rule, which is a different situation (a rejected block).
- ch 2 [low] Section 3, step 1 and step 2: The steps tell the miner to place the coinbase transaction first, then fill the rest of the block from the mempool. But the coinbase value is the block subsidy plus the fees of the included transactions, and those fees are unknown until the transactions have been chosen. A student following the steps in this order cannot compute the coinbase amount.
- ch 2 [low] Section 1, bullet list of node checks: The five checks appear as bullets with no sentence introducing them, straight after the signing paragraph. The reader is not told who performs these checks or when.
- ch 2 [low] Section 2 (fee = size × fee rate) and Section 3 (block size limit): The chapter prices block space per byte, but Bitcoin after SegWit measures space in virtual bytes (weight units ÷ 4), and wallets quote sat/vB. Since the chapter mentions SegWit in Section 4, using plain bytes without a note is inconsistent with what a student will see in a wallet.
- ch 3 [high] Quiz Q7 answer: The closing sentence says "That is why 2f + 1 nodes are needed and 2f + 1 votes are needed", which contradicts the bound the answer just derived. The node count required for Byzantine fault tolerance is 3f + 1, not 2f + 1; 2f + 1 is the quorum size. A student revising from this answer would write the wrong bound in the exam.
- ch 4 [high] Lead, Section 1 and the mining steps: Bitcoin's proof of work hashes the 80-byte header with SHA-256d (SHA-256 applied twice), not a single SHA-256. The chapter says 'SHA-256 hash' and 'hash the header with SHA-256', and still says Bitcoin uses it.
- ch 4 [high] Section 3, shares definition: It defines shares as hashes that beat the pool target 'but not the network target'. A hash that solves the block also beats the pool target and is a valid share; the extra clause is wrong.
- ch 4 [low] Beyond: Verifiable delay functions are listed as proofs that reuse work; a VDF is a delay primitive, not a proof-of-useful-work scheme.
- ch 4 [low] Quiz Q7 answer: It says pay-per-share accounting is a reason expected value shifts. PPS mainly shifts variance and who carries the luck; it does not change expected value except through its fee.
- ch 5 [high] worked example 1, part (c), and quiz Q7: The chapter states twice (Section 1 and Section 2) that slashing destroys part of the stake and removes the validator. The worked example then gives the slashed validator B a new chance of proposing (28.5% of the old total, 28.93% of the new total), and Q7 does the same. A removed validator has zero chance of proposing, so the example contradicts the rule the chapter just taught.
- ch 5 [low] Section 2 and quiz Q2: Slashing is described only as signing two different blocks at the same height. Validators mostly sign attestations (votes), and signing two conflicting attestations is also a slashable offence, so a student may think only block proposers can be slashed.
- ch 5 [low] Section 3, disadvantage bullets: 'Cartel risk, because a few large stakers can coordinate' and 'DPoS uses fewer block producers, which can increase collusion risk' make the same point twice, which reads as two separate disadvantages.
- ch 5 [low] Section 3, disadvantage bullet on stake majority: 'Security still needs an honest majority of stake' is vague and can mislead. A majority above one half is enough to control block production and censor, but finality in BFT-style PoS needs about two thirds of stake attesting; a student may read 'honest majority' as 51% being enough to break finality.
- ch 5 [low] Section 2, paragraph on checkpoints: 'a block can be declared final after two rounds or a fixed number of epochs' mixes two different things and does not say what a round is. In Casper-style designs a checkpoint is first justified and then finalised, one epoch apart.
- ch 6 [high] Exam traps, fourth bullet: The bullet says 'not every validator waits to its own random time and then races'. That contradicts how PoET actually works: every validator draws a random wait and sleeps for it; the one whose wait ends first (the smallest W) wakes first and proposes, while the rest are still waiting and then verify the proof. A student who learns this bullet will believe only the winner waits, which is the wrong model.
- ch 6 [low] Section 2, formula block: The formula defines proposer(n), n, N, T and mod, but never says what start(n) means or where time zero is. A reader cannot tell whether start(n) is the slot's beginning time in seconds from chain start.
- ch 6 [low] Section 1, first paragraph: '(see 3.4)' is written as plain text; cross-references in this book are meant to be links so the student can tap through to the Proof of Work chapter.
- ch 7 [high] Section 3 (confirmation depth) and Quiz Q5: The confirmation definition is off by one against the standard textbooks. A transaction in a block already has 1 confirmation, so k confirmations means k−1 blocks built on top of it, not 'k later blocks'. This makes the Q5 reasoning wrong: a transaction with 3 confirmations sits third from the tip, so a reorg that replaces 3 blocks already removes it. The test '4 > 3' would wrongly suggest that a 3-block reorg is safe.
- ch 7 [low] Worked example 1, step 5: The sentence 'Each chain will retarget its own difficulty later; that does not change this count' states something false. Difficulty is held fixed only because of the example's own assumption; in a real split the old chain's difficulty drops with its 15% hash power and its block rate rises, so the expected old-chain count over the same period would be larger than 356.
