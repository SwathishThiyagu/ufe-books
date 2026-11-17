# m-discrete-u6: free-model run

- Book: `books/common/m-discrete/m-discrete-u6.html`
- Status: ok
- Model calls so far: 25 (87,798 tokens in, 205,677 out), 14.6 minutes

## Checker

```
m-discrete-u6.html: 9 chapters, 16802 words, 10 figures, 165 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, table, Qn row: "Qn | 2n | n·2n−1" is written without superscripts, so it reads as 2n vertices and n·2n−1 edges. For n = 3 that gives 6 vertices and 15 edges, whereas the cube Q3 has 2³ = 8 vertices and 3·2² = 12 edges. A student copying the row gets wrong numbers.
- ch 1 [low] Section 2, table, Wn row: The row gives the rim degree as 3 for every n, but the rim is C(n−1), which only exists as a simple cycle when n−1 ≥ 3. For n = 3 the rim would be C2, which is not a simple cycle, and a rim vertex would have degree 3 only with a doubled edge.
- ch 1 [low] Section 1, first paragraph: "In an undirected graph an edge is a two-element subset {u, v}" contradicts the very next lines, which allow parallel edges and loops; a loop is not a two-element subset, and parallel edges are not distinguished by subsets.
- ch 1 [low] Quiz Q5 answer: "An even number of odd numbers is needed" is vague — the object being counted is not named, so the sentence can be misread as being about the edge count.
- ch 2 [low] Section 1, adjacency-matrix formula box: The formula a_ij = 1 if {i, j} ∈ E else 0 makes every diagonal entry 0, but the paragraph just above says 'The diagonal entry aii records a loop', and Exam trap 1 depends on a loop appearing as a diagonal 1. A student cannot tell which statement to use for a graph with loops.
- ch 2 [low] Exam traps, fourth trap: 'A matrix with only rows permuted usually represents a different graph' is misleading. Permuting rows only does not give the adjacency matrix of some other undirected graph at all, because the result is generally not symmetric; the graph has not changed, only the labelling was half-done.
- ch 2 [low] Section 2, invariants paragraph: The text says the listed invariants are necessary but not sufficient, then illustrates with C6 versus two disjoint triangles. Those two graphs agree only on vertices, edges and degree sequence; they are already separated by connected components, which is itself in the list. As written, a student may think the full list failed on this pair.
- ch 3 [low] Exam traps, last bullet: It says complete graphs 'use special conventions' for κ(G) ≤ λ(G) ≤ δ(G). With the chapter's own definition (removal disconnects G or leaves one vertex), K_n gives κ = λ = δ = n − 1, so the inequality holds for complete graphs with no extra convention. A student may wrongly conclude the inequality fails for K_n.
- ch 3 [low] Quiz Q4: '2-edge-connected' is used in the question but never defined in the chapter, so an ESL reader has to guess its meaning before answering.
- ch 4 [high] Quiz Q7: The answer uses the bipartite balance test as if it proves the cycle exists: 'K₃,₃ has parts of size 3 and 3, so it has a Hamiltonian cycle.' Equal parts are only a necessary condition, never a guarantee, so the reasoning is invalid even though the conclusion for K₃,₃ is true.
- ch 4 [low] Section 1: Euler path is first defined as a walk that 'is not closed', but the next paragraph says 'If zero vertices have odd degree, an Euler circuit exists and is also an Euler path.' The two statements contradict each other and a student may lose marks repeating the first one.
- ch 4 [low] Worked example 1, step 6: 'A Hamiltonian cycle cannot contain a cut vertex' is wrong as written: C is a vertex of the graph, so any Hamiltonian cycle would contain C. The valid statement is about the graph, not the cycle.
- ch 5 [low] Section 3 (edge bounds): The results are stated for 'a simple planar graph with V ≥ 3' with no connectivity condition, but the derivation substitutes F = 2 − V + E, which is Euler's formula for connected plane graphs only. For a disconnected graph that substitution is false (e.g. two disjoint triangles: V = 6, E = 6, F = 3, yet 2 − V + E = 2). The bounds themselves are correct for disconnected graphs too, but the proof step as written does not cover them.
- ch 6 [low] Section 1, colour class paragraph: The chapter defines k-colourable as using at most k colours (unused colours allowed), then says a k-colouring splits V into exactly k independent sets. If a colour is unused its class is empty, so the count can be less than k. A student may think all k colours must appear.
- ch 6 [low] Section 2, bipartite paragraph: 'A graph is bipartite exactly when it is 2-colourable exactly when it has no odd cycle' is correct, but the trap later repeats it as 'bipartite graphs are exactly the 2-colourable graphs with no odd cycle', which is redundant and reads as if 2-colourable graphs might have odd cycles.
- ch 6 [low] Section 2, bipartite paragraph: The BFS argument 'a breadth-first search from any vertex assigns alternating colours' silently assumes a connected graph; a disconnected graph needs a BFS in each component.
- ch 6 [low] Exam traps, trap 3: 'An empty graph is 3-colourable but has χ = 1' is ambiguous: many textbooks use 'empty graph' for the graph with no vertices, whose chromatic number is 0. As written the example can look wrong.
- ch 6 [low] Section 3, register allocation: Grammar: 'χ is the minimum registers needed' is missing a noun.
- ch 6 [low] Beyond: The name is misspelt; the standard spelling carries an accent.
- ch 7 [low] Lead: UPI payment routing is not a shortest-path application; UPI routing picks a payment switch/issuer, it does not minimise a sum of edge weights. Listing it next to map route planning and OSPF packet forwarding may mislead students about where Dijkstra is actually used.
- ch 7 [low] Lead, last sentence: 'This chapter shows the distance table, the predecessor array, and why negative edges break the greedy choice' is a tour of the chapter, not content; the house style asks for no such filler.
- ch 7 [low] Quiz Q2: The answer is correct but compressed: 'adds a nonnegative weight to a distance that is already at least d(u)' leaves the key link implicit — a later route to u must leave the settled set through some unsettled vertex x with d(x) ≥ d(u). A student can read the sentence and still not see the argument.
- ch 7 [low] Section 2, path rebuild step: The rebuild step does not say what to do when the target is unreachable, so a student with d(t) = ∞ may start walking pred(t) from 'none' and get a broken path.
- ch 8 [high] Section 1, equivalent-forms list, statement (6): Statement (6) 'removing any edge disconnects it' is not equivalent to being a tree. A forest with two or more components also satisfies it: deleting an edge splits one of its trees in two, so the number of components rises. A student can therefore accept a disconnected graph such as two separate K₂'s (n = 4, m = 2) as a tree. Connectedness has to be built into the condition; the textbook form is 'connected, and every edge is a bridge' or 'connected, and removing any edge disconnects it'.
- ch 8 [low] Section 1, proof of m = n − 1: The proof deletes a leaf and its one edge, but the existence of a leaf in a tree with n > 1 is only asserted just before, not justified. The step that carries the induction is left unexplained.
- ch 9 [low] Figure caption (section 4 figure): The caption says 'The lighter edges were skipped by Kruskal or never reached', but every unused edge in the figure (AC 3, CD 5, CE 6, BE 7) is heavier than the edges chosen at the moment it was considered. 'Lighter' is the opposite of what happened and a student may learn the wrong reason for skipping.
- ch 9 [low] Worked example 1, step 11: The step says 'cut edges AC 3 (inside), BD 4, CE 6, BE 7', but AC has both ends in S = {A, B, C}, so it does not cross the cut and cannot be listed among the cut edges. Also CD 5 does cross the cut and is left out.
- ch 9 [low] Quiz Q5 answer: At the third stage S = {B, D, E}, the answer lists BE 7 as a crossing edge, but B and E are both already in S. Edge BE has both ends inside the cut set and cannot be chosen.
- ch 9 [low] Quiz Q6 answer: The answer asserts that e is 'the unique lightest edge crossing that cut' without saying why. That claim is the key step and depends on T1 being minimum-weight, so as written it looks like an unproved assumption.
- ch 9 [low] Lead: The lead says a spanning tree 'uses exactly n − 1 edges' before n is defined; n is only introduced in Section 1.
