6. Are there necessary or sufficient conditions on a topology such that the projection of its LP to _D_-space is integral (and thus optimal)? Figure 6 shows that many non-integer LPs do become integer when projected.

**Improved Approximations and Rounding Alternatives**

1. What is the true integrality gap of the LP? Denote it \(\rho\), we know that \(\rho\le 2\) by Property 3 and that \(\rho\ge\frac{95}{93}\approx 1.02\) by  2. Can we tighten these bounds?<tbc>

2. Can the root rounding (Definition 1.6) be refined, to define tie breaking more carefully, to guaranteed an integrality gap better than 2?<tbc>

3. Is there a way to take the frequencies into account when rounding? Observe that the root rounding is agnostic, which is somewhat less natural. Studying the dual LP in this context may be relevant since its polytope depends on the frequencies.<tbc>

4. Is there an alternative rounding scheme which is better (absolutely, or by being easier to analyze)? As a concrete suggestion, is there a way to take a feasible solution and (almost) decompose it to STT induced points? For example, "peel" off STTs one by one until the remainder is small. Then we can choose the best STT in the decomposition. Another alternative decomposition rounding would be to maintain a collection of STTs whose convex combination is "close" to the solution we wish to round. Start by choosing a single node of the topology (a singleton STT is exact for it), then extend the topology by one node at a time, where in each step we update the set of STTs by adding the new node to each STT, possibly forking some of them if we need different STTs that are the same up to the location of the new node. As an example, the non-integer vertex _P_ shown in Figure 3 with depths _D<sup>P</sup>_=(2,2,4.5,2,2,1.5,0.5) can be presented as almost-average of STTs _B_ and _C_ with depths vectors _D<sup>B</sup>_=(2,3,4,1,2,0,1), _D<sup>C</sup>_=(2,1,5,3,2,4,0) (_P_ is better: \(D^P=\frac{1}{2}(D^B+D^C)-(0,0,0,0,0,0,\frac{1}{2},0)\)).<tbc>

5. Is there an iterative rounding scheme that improves the approximation or even achieves optimality? The root rounding (Definition 1.6) takes a fractional solution of the LP, and rounds it fully. Iterative rounding does not help the root rounding, but perhaps it could help in other ways. For example, if could determine a good choice of root, we could apply this method repeatedly, _O(n_) times, each time fixing the root of a subtree of the resulting STT. This will still take polynomial time in total. Ideally we could hope to determine an optimal choice for the root, but any choice that would lead to an approximation ratio better than 2 would improve the state of the art. A related question is whether there a way to remove an arbitrary (non-root) node, or contract an edge of the topology and recur on the smaller problem?

**Miscellaneous LP Properties**

1. Considering the LP version without the _Z_ variables (Section 5.2), every coordinate of every vertex that we found was either integer, half-integer, or third-integer. When considering vertices that are solutions of the LP in _D_-direction, we only encounter integer and half-integer coordinates (Remark 2.6). Can we prove that these properties hold in general?<tbc>

