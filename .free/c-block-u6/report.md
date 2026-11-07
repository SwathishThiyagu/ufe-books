# c-block-u6: free-model run

- Book: `books/cse/c-block/c-block-u6.html`
- Status: ok
- Model calls so far: 43 (152,979 tokens in, 261,544 out), 7.8 minutes

## Checker

```
c-block-u6.html: 9 chapters, 14549 words, 10 figures, 174 KB
OK
```

## For the reviewer

- chapter 7: the figure cannot be drawn: note "BTC sidechain" runs off the right edge; shorten it
- chapter 7: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, bullet on commit (and repeated idea in Exam traps): The sentence "A version change means another transaction wrote first; that transaction is marked invalid" reads as if the earlier transaction, the one that wrote first, is the invalid one. It is the opposite: the earlier transaction is valid, and the transaction being validated now is the one marked invalid because its read-set version is stale.
- ch 1 [low] Section 1, Consensus bullet: "older deployments used Kafka or Solo for development" lumps two different things together. Solo (later called the solo orderer) was only ever a single-node orderer for development and testing. Kafka was a real multi-node ordering service used in production networks before Raft replaced it.
- ch 2 [low] Section 1, namespace paragraph: The text says a namespace is a key prefix such as car and CAR1 becomes carCAR1, but never says who adds the prefix. A student may conclude the chaincode must call PutState("carCAR1"); in Fabric the chaincode calls PutState("CAR1") and the peer's state database applies the chaincode-name prefix on disk. The worked example later uses the plain key CAR1, so the two parts read inconsistently.
- ch 2 [low] Worked example 1, step 6: "the write sets owner = Ravi in namespace carCAR1" mixes two ideas: carCAR1 is the fully prefixed key, not the namespace (the namespace is car). The sentence is also grammatically muddled ("the write sets owner").
- ch 2 [low] Quiz Q4: The question contradicts itself: "TransferAsset commits owner Ravi" and then "a query runs before the commit block is written". If the transfer has committed, there is no pending block.
- ch 2 [low] Figure spec: The last message goes from Ledger straight to Client ("query owner"). A client never reads the ledger directly; a query is a proposal sent to a peer, which runs the chaincode against its committed state and returns the result.
- ch 2 [low] Section 1, last paragraph: "See Unit 5 for Solidity" is a bare cross-reference; the house style for other chapters is a link so the reader can jump to it on a phone.
- ch 3 [low] Section 2 and Exam traps (5th bullet): The channel privacy topic is cross-referenced to 6.8 in Section 2 but to 6.1 in the traps list, so the reader is sent to two different chapters for the same idea.
- ch 3 [low] Section 1, KYC paragraph: 'Personal data never reaches the ledger' is too strong. The signed attestation has to identify the customer for another bank to match it, and a hash of a document that can be linked back to a person is still treated as personal data under laws such as the DPDP Act.
- ch 3 [low] Section 3, payout formula: The cap uses 'sum insured', the policy maximum, but Worked example 1 step 6 and Quiz Q5 reduce a remaining sum insured after each payout. Applying the formula literally to a second claim on the same policy would overpay.
- ch 3 [low] Section 2, letter of credit paragraph: 'Documents prove the goods were shipped' overstates the bank's role. Banks deal in documents, not goods; they pay against documents that appear to comply with the LC terms, which is exactly why the later point about unverifiable facts matters.
- ch 3 [low] Section 3 and Figure: The double-payment guard is called the 'paid-claims set' in the preconditions and worked examples but the 'audit log' in the figure and its caption, so a student may think two separate structures are needed.
- ch 3 [low] Section 2, DvP paragraph: 'That gap is counterparty risk' is loose. The specific risk from the time gap between the two legs is principal (settlement) risk; counterparty risk is the broader term.
- ch 4 [low] Section 2, cold chain paragraph: The word 'excursion' is used without a definition ('minimum, maximum, count and any excursion'). A second-language reader may not know it means a reading outside the allowed band.
- ch 4 [low] Worked example 1, step 3: The example uses the transporter's receive record (98 kg) as the quantity dispatched to the warehouse, so it silently assumes each intermediate party dispatches exactly what it received. The gain or loss inside a party's own custody is therefore never measured, although Section 1 says each party writes both a receive and a dispatch event.
- ch 4 [low] Section 3, second bullet: 'Some syllabi call this supply chain insight from enterprise resource planning' does not name a term and reads as unclear filler.
- ch 4 [low] Section 2 last paragraph and Section 3 payment paragraph: The cross-references 'see Chapter 6.5' and 'chaincode from Chapter 6.2' are plain text, not links, so a reader on a phone cannot jump to them.
- ch 5 [high] Exam traps, trap 1: The trap says to store a hash or a Merkle root off-chain. That is the opposite of what the chapter teaches everywhere else: the raw readings stay off-chain and the hash or Merkle root goes on the ledger. A student revising from the trap list would learn the wrong placement.
- ch 5 [low] Section 2, first bullet: It says the gateway 'signs the reading with the device key'. But Section 4 says the gateway rejects readings signed by an unknown key, which means the device signs and the gateway verifies. As written, the gateway appears to hold every device's private key, which is both inconsistent and bad practice.
- ch 5 [low] Section 1, clinical trials paragraph: 'each data lock' is undefined and unclear. The reader cannot tell what is being hashed and time-stamped.
- ch 6 [low] Section 2, first paragraph: NFT is used throughout but never expanded, and the reader is never told the defining property: unique and not interchangeable. On a phone, days before the exam, an unexplained acronym costs marks.
- ch 6 [low] Section 2, first paragraph: 'It proves who controls an asset' is loose. The ledger records which address controls the token; the asset itself stays off-chain, as the chapter's own exam trap says ('proves control of a token'). A student may read the two sentences as contradicting each other.
- ch 6 [low] Section 2, third paragraph: EVM is not expanded, and pairing 'chaincode' with 'EVM contract' for NFT escrow and royalties is loose: chaincode is Hyperledger Fabric's smart-contract term, and the standard NFT standards (ERC-721, ERC-2981 royalties) are EVM standards.
- ch 6 [low] Quiz Q7: The answer says 'the token and metadata hash are on-chain'. Usually the metadata file (with its URL) is off-chain and only the tokenURI string, or at most a content hash, is on-chain. This is stricter than the Section 2 statement that metadata 'usually includes a URL or content hash'.
- ch 7 [high] Section 2, paragraph 2: The rule "quorum = 2f + 1 votes" is presented as general for any n, but it is only correct when n = 3f + 1. With n = 6, f = floor(5/3) = 1 gives quorum = 3, yet 3 of 6 is half, not more than two-thirds, so the block cannot commit; the true quorum is 5. A student who applies the printed formula to n = 5, 6 or 8 gets a wrong answer.
- ch 7 [high] Lead: "Tendermint commits with one BFT vote" contradicts the body of the chapter, which correctly shows two voting steps (prevote, then precommit) before a block commits. A student reading only the lead will think a single round is enough.
- ch 7 [low] Section 1, Ripple paragraph: "It is still a ledger at the contract level" has no clear meaning here; the reader cannot tell what is being contrasted.
- ch 7 [low] Section 2, Tendermint paragraph: "Cosmos uses Tendermint-style consensus to link application chains" mixes two things: consensus orders blocks inside one chain, while linking between chains is done by IBC.
- ch 7 [low] Table (Tendermint row) and Section 3 closing sentence: The table lists Tendermint permissioning as "permissioned validators", and the text says Tendermint is "often permissioned". Public stake-based chains such as the Cosmos Hub run Tendermint-style consensus with an open, permissionless validator set, so the table entry is not generally true.
- ch 7 [low] Section 3 closing sentence and Table (Ripple row): Ripple is called permissioned and its permissioning cell says "permissioned list", while the same sentence calls the XRP Ledger public. Both are true of different things (validator agreement vs who may hold and send XRP), but as written a student sees a contradiction.
- ch 7 [low] Worked example 1, step 2 and answer line: f is the maximum number of faulty validators the network can tolerate, not a count of faulty validators present; "f = 2 faulty validators" reads as if two validators are actually faulty.
- ch 8 [low] Section 2 (layer-2 paragraph): The sentence says a rollup 'posts compressed data plus a proof back' and then describes optimistic rollups. An optimistic rollup does not post any proof when it posts data; it posts data plus a bond and relies on a challenge window, with a fraud proof produced only if someone challenges. A student can read the sentence as saying every rollup posts a proof.
- ch 8 [low] Section 2 (Fabric sentence) and Quiz Q6: 'Only endorsed parties can read through chaincode' is loose. The private payload goes to the peers of the organisations named in the collection policy, which is not the same set as the endorsing peers of one transaction.
- ch 9 [low] Section 3, first paragraph, and Quiz Q4 answer: 'An auditor reruns the model hash' is technically imprecise: a hash value cannot be rerun. A student may carry away the idea that the hash itself reproduces the model.
- ch 9 [low] Figure (sequence spec): The message from Blockchain to AI service labelled 'read approved data' contradicts the text, which says the AI service reads approved off-chain data. A sequence arrow from the chain to the AI service suggests the ledger pushes the data, and a student may conclude the training or input data sits on-chain.
- ch 9 [low] Section 3, last sentence before the figure: 'If an oracle lies, the hash is valid but the fact is false; trust the oracle process' can be read as telling students to trust oracles. The point is the opposite: the hash only fixes what was written, so trust must come from how the oracle is run and checked.
- ch 9 [low] Section 1, first paragraph: The cross-reference '(see finance)' is plain text, so on a phone it does not link anywhere and the reader cannot jump to the chapter.
