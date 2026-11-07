# c-block-u1: free-model run

- Book: `books/cse/c-block/c-block-u1.html`
- Status: ok
- Model calls so far: 32 (114,985 tokens in, 175,799 out), 5.8 minutes

## Checker

```
c-block-u1.html: 7 chapters, 12586 words, 8 figures, 147 KB
OK
```

## For the reviewer

- chapter 6: the figure cannot be drawn: tree is too wide (7 leaves); use fewer leaves or shorter labels
- chapter 6: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Exam traps, third bullet: It says starting at Ethereum in 2015 'skips roughly seven years of working Bitcoin history'. The working ledger began with the genesis block on 3 January 2009, so 2009 to 2015 is six years by the chapter's own year-counting convention (used in Worked example 2 and Quiz Q5). The 'seven years' figure belongs to the whitepaper (2008), not to the running network.
- ch 1 [low] Worked example 1, step 6 and answer: It states 'the genesis block followed 1 year later in 2009'. That is the year difference (2009 minus 2008), but the actual elapsed time from the October 2008 whitepaper to 3 January 2009 is about three months. A student can read '1 year later' as a duration and place the genesis block in late 2009.
- ch 2 [low] Section 1, the four bullets (Administrator trust, Conflict resolution, Reconciliation, Query needs): The bullets arrive with no lead-in sentence, so a student cannot tell what they list. They also follow a paragraph that already announces 'Four ideas', so readers may think these four bullets are those same ideas, when in fact they are the weak points of an ordinary distributed database.
- ch 2 [low] Section 3, Two Generals paragraph: 'Common knowledge' is used as if already defined, but it is a technical term (each side knows, knows that the other knows, and so on). Without a one-line definition the last sentence of the paragraph is easy to misread.
- ch 3 [low] Section 2, bullet list: The bullets mix benefits and costs with no label, and one bullet is named "Cost:" even though it describes a saving (removing a middle party's fees). A student skimming the list can read it as a cost of decentralization, the opposite of the meaning.
- ch 3 [low] Section 3, last paragraph of methods: "See Unit 3 for consensus and Unit 5 for smart contracts" points to other units but carries no link, so on a phone the reader cannot jump there; the rest of the book uses chapter links.
- ch 4 [low] Section 1, tamper-evidence limit: "more than 50% of power" leaves the unit of power undefined; students on a proof-of-work chain read hash power, on a proof-of-stake chain the same sentence is wrong unless stake is named.
- ch 4 [low] Lead paragraph: The lead promises a cost for every feature but lists only six costs (collusion risk, lost privacy, lower throughput, fees, key loss, oracle trust) for seven features; the auditability limit (bad input stays bad) is missing from the list.
- ch 4 [low] Exam traps, first trap: "51% collusion can rewrite recent history, not the entire chain" is too absolute: the standard limit is that a majority attacker can reverse their own recent transactions and block new ones, but cannot spend other users' coins or change block rewards; depth is limited in practice by cost and checkpoints, not by the protocol.
- ch 4 [low] Figure: The node labelled "Final" with note "forks possible" appears only in the figure; the myth list in Section 3 never discusses finality, so the caption's claim that each branch carries a limit explained in the text does not hold for that branch.
- ch 4 [low] Figure: The central "Claims" node carries the note "5 pools", which describes the worked example, not the idea of a claim; a reader can mistake the centre for a pool count.
- ch 5 [high] Section 2, sentence 'Privacy follows read permission... Private and consortium chains restrict readers and data.': This contradicts Section 1 ('Read access may be open or limited' for a private chain), the comparison table (Private: who reads = 'Approved users or public'), and the worked example, where citizens may read records on a private land-registry chain. A student will think the worked example breaks the rule.
- ch 5 [low] Figure caption and the '12 offices' note in the tree: The caption says '12 offices and 3 banks match the worked example', but the worked example counts 13 validating offices: 1 registrar + 12 sub-registrar offices. The number the figure gives does not match the number the student works out.
- ch 5 [low] Figure root and second level: The root asks 'Who joins?' and the second-level node is 'Invited', but its children 'One org' and 'Many orgs' describe who owns and validates, not who joins. The chapter's own deciding question is 'who validates', so the tree asks a different question from the rule it teaches.
- ch 5 [low] Lead: 'private chains restrict one organisation' can be read as restricting an organisation rather than restricting access to one organisation.
- ch 6 [high] Quiz Q3: The answer says Block 31's previous hash '00ff' is wrong. 00ff is Block 30's own previous-hash field (the hash of Block 29). Block 31 stores the hash of Block 30's header, which is a different value that the question never gives. A student would wrongly learn that a child block repeats the parent's previous-hash field.
- ch 6 [low] Worked example 1, step 2: '7c2e-prime' looks like a hash value but is not valid hexadecimal, which can confuse students about what a Merkle root looks like.
- ch 6 [low] Quiz Q6: 'Must change first' suggests an order of operations, but the Merkle root is not changed before the others by choice; it is simply the only one of the four values computed from the transactions.
- ch 6 [low] Figure spec: The root node is labelled 'Block n' but carries the note 'height 20'; the worked example uses 'Block 20', so the two do not match.
- ch 7 [high] Worked example 1, step 5 (and its answer line): It says L1 and L2 "store headers and Merkle proofs, not full blocks". A light client does not store Merkle proofs. It stores block headers and asks a full node for a Merkle branch for one transaction, checks it, and discards it. The sentence also contradicts the chapter's own table, which says a light node stores "block headers only".
- ch 7 [low] Section 2, roles table, row 'Full node': The 'Stores' cell reads "All blocks, or recent blocks after pruning", but the very next rows already give a separate 'Pruned full node' entry. Putting the pruning case in the full-node row makes the two rows look like the same role.
- ch 7 [low] Section 2, roles table, row 'Seed node': The 'Validates' cell says "No chain data", which answers the 'Stores' column, not the 'Validates' column. A student can read it as 'a seed node is data that is not validated'.
- ch 7 [low] Worked example 1, step 2: "F1 checks signature, format and available balance" uses account-model language. In a UTXO chain, a full node does not look up a balance; it checks that the referenced coins exist and are still unspent. The chapter covers both models, so a fixed wording is safer.
