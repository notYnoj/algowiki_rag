<tbc>**Proof.** The result will hold for any \(k\ge N\), where _N_ is the total number of binary trees of the given size. Since each tree has a fixed associated cost, there can be no sequence of properly increasing costs (as per the lemma) of size greater than _N_.

**Proposition 9** _Let T be a weighted binary tree of size n. Then if k is a positive integer, an element of_ \(\beta^k(T)\) _can be found in time_

\(O((n+k)log(min(n,k))).\)

**Proof.** The result will follow from the following:

1. It is possible to compute both <o>_p_</o>(_x_) and \(\mu(x)\) for all \(x\in T\) in time _O(n_) in an initialization phase, along with<tbc>

2. A list of at least min(_n,k_) nodes, sorted by merit, that can be initialized in time _O(n_log(min(_n,k_))),<tbc>

3. When a node is bumped, it is possible to update the various <o>_p_</o>(_x_) and \(\mu(x)\) in time _O_(1), and<tbc>

4. It is possible to update the merit-sorted list of nodes in time _O_(log(min(_n,k_))).

The proposition then follows immediately, since the running time is _O(n+n_log(min(_n,k_))) for the initialization and _O_(1+log(min(_n,k_))) for each of _k_ iterations. The total running time is thus as described in the statement of the proposition.

1. <o>_p_</o> can be computed for all of the nodes in the tree in time _O(n_) by simply working back from the fringe. \(\mu\) can then be computed, also in time _O(n_), by virtue of Proposition 5.<tbc>

2. Given merits for all of the nodes, the _k_ highest-merit nodes can be found in time _O(n_log_k_). If _k\>n_, it suffices to simply sort the merits, so that the time is therefore _O(n_log(min(_n,k_))).<tbc>

3. Consider Figures 2 and 3. When a node _x_ is bumped, the value of <o>_p_</o>(_x_) will change only for _x_ itself, since its parent is now a child, and _x_’s parent \(\pi(x)\), since both _x_ and one of the subtrees rooted at a child of _x_ are no longer descendants of \(\pi(x)\). Computing <o>_p_</o>(_z_) for each of these two nodes takes constant time.<br>
Similarly, \(\mu(z)\) changes only for the nodes labeled _a_ through _e_ in the figures. Again, the update takes constant time.<tbc>

4. When the merits are recomputed, inserting any new positive values into the list of nodes to bump takes time _O_(log_s_), where _s_ is the size of that list, with \(s\le min(n,k)\) as a result. Note that we don’t need to search the entire tree for a node to "replace" the one that was just bumped; if we only plan on bumping _k_ nodes in total, we will be interested in one fewer node on the next iteration.<tbc>

