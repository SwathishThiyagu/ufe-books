# c-block-u5: free-model run

- Book: `books/cse/c-block/c-block-u5.html`
- Status: ok
- Model calls so far: 37 (140,490 tokens in, 217,603 out), 5.5 minutes

## Checker

```
c-block-u5.html: 8 chapters, 14972 words, 9 figures, 160 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2 (formula note) and Exam traps, fourth bullet: The chapter says the whole fee gasUsed × gasPrice is 'paid to the block producer'. On Ethereum today (since the London upgrade) the transaction's gas price is split: the base fee is burned and only the priority (tip) part reaches the block producer. A student who writes 'the entire fee goes to the miner/validator' loses marks, and the formula's gasPrice field no longer exists on current transaction types (they carry maxFeePerGas and maxPriorityFeePerGas).
- ch 1 [low] Section 2, account fields list: codeHash is described as 'empty for a plain account'. In the standard account definition an externally owned account has codeHash set to the Keccak-256 hash of empty code, not a blank value.
- ch 1 [low] Section 1, light node paragraph: A light node cannot check a balance against a header on its own; the balance it receives must come with a Merkle proof that hashes up to the state root in the header. As written, a student may think any header alone is enough to verify any balance.
- ch 1 [low] Section 2, world state paragraph: 'Every node that has validated the chain holds the same table' contradicts the node table in Section 1, where a light node stores block headers only.
- ch 2 [high] Section 3 (Messages, receipts and logs): After listing CALL, STATICCALL and DELEGATECALL together, the chapter says the message carries 'a sender (the calling contract's address), a value that may be zero'. That is true for CALL, but wrong for DELEGATECALL: there the callee sees the parent's msg.sender and the parent's msg.value, not the calling contract's own address and not its own value. A student who writes 'the sender is always the calling contract' loses marks on the standard DELEGATECALL question.
- ch 2 [low] Section 2 (A transaction: fields and life cycle): 'A call to a contract consumes 21,000 plus the gas of the opcodes it executes' leaves out calldata gas. Intrinsic gas is 21,000 plus 16 gas per non-zero data byte and 4 gas per zero byte, and contract creation adds 32,000 fix on top. A student may then under-estimate the cost of a token transfer, which carries a lot of calldata.
- ch 2 [low] Section 4 (Tokens): The ERC-20 list omits balanceOf and the allowance mapping, so 'approve' and 'transferFrom' appear without the structure they work on. Wallets also need balanceOf to read a balance, which the paragraph says they do.
- ch 3 [low] Lead: The sentence "The EVM changes account state only through state changes that a block finally commits" is circular and a first-time reader may not see what it means.
- ch 3 [low] Lead: The sentence says determinism follows from the 256-bit word size ("It is a stack machine with 256-bit words, so the same bytecode gives the same result on every node"). Word size does not cause determinism; the fixed opcode rules do.
- ch 3 [low] Quiz Q5: "Gas already used is not fully returned" is vague and a student may read it as a partial refund. In fact the unused gas left in B's frame returns to the caller and the gas consumed is kept.
- ch 4 [high] Worked example 1, setup sentence: The rule is stated as 'otherwise the seller can refund the buyer after 7 days'. This gives the seller control over the buyer's money and contradicts step 4 and Q5, where the refund path is the buyer's to claim. A student reading the setup will answer 'the seller refunds' and lose marks.
- ch 4 [low] Section 4, Escrow: 'refunds the buyer if nobody confirms' reads as if the contract refunds on its own once the deadline passes. A contract cannot keep a timer or start itself, and the chapter's own exam trap says so.
- ch 4 [low] Section 1, second paragraph: 'Nobody can change the rule after deployment' sits badly with the Beyond note on upgradeable proxy patterns, where logic does change while the address stays fixed. The absolute claim teaches a fact the student must later unlearn.
- ch 4 [low] Exam traps, third bullet: The reason given, 'because no node stores the result', is not the real reason. The node does run the code; it simply persists no state change, so the caller is charged no gas.
- ch 5 [low] Section 2, modifiers and custom errors: The sentence 'error ZeroAmount(); then revert ZeroAmount();;' has a doubled semicolon and does not say where the error must be declared. A student may copy 'error ZeroAmount();' inside a function body, where it does not compile; custom errors are declared at file or contract level.
- ch 5 [low] Section 2, visibility: 'external only from outside' can mislead. A contract can call its own external function, but only through an external call such as this.deposit(), not by its bare name.
- ch 5 [low] Section 2, visibility: 'private only this contract' may be read as confidentiality. private stops other contracts and child contracts from reading the variable in Solidity, but the value is still visible on chain to anyone reading state.
- ch 5 [low] Section 3, inheritance: 'Savings gets the state and functions of SimpleBank' is not exact. Members marked private are not accessible in the child contract, and functions must be marked virtual and override to be redefined.
- ch 6 [low] worked example 1, steps 3–5 and Section 3: The example says the fee goes to the miner, but the only account in the genesis alloc is A, and mining needs a local account as etherbase. If A mines, A also collects the 0.000021 ETH fee and ends at 100 − 1 = 99 ETH, not 98.999979 ETH. The stated answer only holds if the miner is a separate account that the example never defines.
- ch 6 [low] Section 3, reading the numbers: 'The miner receives the fee' is only true for pre-London chains or for the tip on a post-London chain. After EIP-1559 the base fee part of every transaction fee is burned, so the block proposer gets only the priority fee.
- ch 6 [low] Section 3 and exam traps, pending transaction: 'A pending transaction has no balance change' is too absolute. A node that tracks pending state already deducts the sender's gas and amount in that pending state; only the confirmed ('latest') balance is unchanged until the block is mined.
- ch 6 [low] Section 1, testnet state paragraph: 'The address can look the same' is vague. When the same key is used, the address is exactly the same; what differs is the state, balance and code stored at that address on each chain.
- ch 7 [low] Section 3, bullet on frameworks ("All three produce a build artifact ... plus the address after deployment"): The address is not part of the build artifact for Hardhat or Foundry. Hardhat's artifact JSON carries abi, bytecode and deployedBytecode only; the deployment address lives in a separate deployments file or a script you write. Foundry writes addresses to a broadcast/ run file, not into out/*.json. Only Truffle's artifact JSON holds a networks entry with the address. As written, students will look for the address inside the artifact and not find it.
- ch 7 [low] Section 2, definition of the ABI: The ABI is defined as a description of functions only, but the front end is later told to update the screen from contract events. Decoding an event log also needs its ABI entry (name and indexed/non-indexed parameter types); without it the library cannot turn a log into named values. Errors (custom errors) are in the ABI too.
- ch 7 [low] Quiz Q8: "Why is a private key written into front-end JavaScript unrecoverable as a security failure" is garbled; a student cannot tell whether 'unrecoverable' describes the loss of funds or the mistake.
- ch 7 [low] Beyond: "viem and wagmi wrap ethers-style calls" is inaccurate: viem is a standalone low-level client that competes with ethers, not a wrapper around it, and wagmi is a set of React hooks built on viem.
- ch 8 [low] Worked example 1: The question asks for every weight, but the weight of the root A is never computed or stated in the steps or the answer, so a student who follows the steps literally leaves A out.
- ch 8 [low] Section 2, GHOST bullets: The rule 'move to the child with the larger weight' has no tie-breaking rule, so a student cannot handle two children of equal weight, which happens often in real block trees.
- ch 8 [low] Section 2, uncle blocks: 'Orphaned blocks become uncles' is too loose: only stale blocks within a short window (a few generations) of the naming block, and that the miner has actually seen, can be included as uncles. Students may think every orphan is paid.
- ch 8 [low] Quiz Q6: The answer says three of the five validators can finalise false blocks, but the question never states the side chain's consensus threshold. If the chain needs more than two-thirds, four validators are required, so the number 3 is an assumption.
- ch 8 [low] Beyond: 'Ethereum's fork choice has moved toward LMD-GHOST' is vague; LMD-GHOST is already the fork-choice rule Ethereum uses, so 'moved toward' can read as a future plan.
