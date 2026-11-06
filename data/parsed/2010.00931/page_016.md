of _r_, so by Lemma 2, there must be some connected component _C_ of _S_\[_A_\]\\_r_, such that \(u\in\delta(C)\). Then, by assumption, there is some \(v\in\delta(A)\backslash\delta(C)\) (otherwise, by Lemma 2, _V(C_) has boundary size _k_+1 and _r_ is not _k_-admissible). Node _v_ is either a neighbor of _r_ or a boundary node of a component \(C'\neq C\) of _S_\[_A_\]\\_r_. The path between _u_ and _v_ must pass through _r_, implying \(r\in\mathfrak{ch}(\delta(A))\).

Conversely, assume \(r\in\mathfrak{ch}(\delta(A))\cap A\). Let \(u,v\in\delta(A)\) be two distinct nodes. Then _r_ is on the path between _u_ and _v_. Thus, _u_ and _v_ are in different connected components of _S_\[_A_\]\\_r_. Now Lemma 2 implies that the boundary of each connected component _C_ of _S_\[_A_\]\\_r_ is a proper subset of \(\delta(A)\cup\{r\}\), and thus has boundary size at most _k_.

Given Lemma 7, the enumeration of _k_-admissible roots in Line 4 is straightforward, via a traversal of the subtree _S_\[_A_\]. In case (i) we traverse the entire tree _S_\[_A_\], in case (ii) we traverse the tree of paths from some boundary node \(v\in\delta(A)\) to the other boundary nodes \(\delta(A)\backslash\{v\}\) (found e.g. with a breadth-first search). The cuts of the components can be found in linear time by straightforward data structuring.

## Running time.

In the preprocessing stage we enumerate O(_n<sup>k</sup>_) cuts, and for each cut we do a linear-time traversal to find the corresponding _k_-admissible set, all within time O(_n_<sup>_k_+1</sup>).

The recursive calls of OPT-STT are for smaller _k_-admissible sets. Therefore, during the preprocessing phase we sort the _k_-admissible sets by size, and in the dynamic programming table we fill in the entries by increasing order of size. It remains to show that filling in one entry takes time O(_n_), from which the overall running time of O(_n_<sup>_k_+1</sup>) follows.

Lines 2-3 take O(1) time. In Line 4 we iterate over all _k_-admissible roots, which, by the preceding discussion, takes time O(_n_). In Line 5 we read out the connected components indexed by their cuts, computed during preprocessing. Line 8 takes O(1) time, as the first term can be precomputed for all _k_-admissible sets, and the second term is collected from the recursive calls.

Line 7 is nested in two loops (iterating through possible root nodes, and through each connected component after the removal of the root). Nonetheless, it is easy to see that it is executed at most twice for each _edge_ in _S_\[_A_\] (once for each orientation). The total number of recursive calls is therefore at most \(2n-2\in\mathcal{O}(n)\), as is the cost of taking the minimum in Line 9.

Using Lemma 19 and setting _k_=2_t_, we obtain:

**Theorem 1.** _Let X be a search sequence over the nodes of an n-node tree S and let_ OPT(_X_) _be the minimum cost of serving X in a fixed search tree on S. For every integer_ \(t\ge 1\) _we can find in time_ O(_n_<sup>2_t_+1</sup>) _a search tree on S that serves X with cost at most_ \((1+\frac{1}{t})\cdot\mathsf{OPT}(X)\).

## Remark.

It is tempting to try extending the approximation algorithm (with some ratio _r\>_2) to the the easiest _k_=1 case, i.e. when the STT is a rooted version of _S_. Unfortunately, 1-cut trees cannot give an _o(n/_log_n_)-approximation of the STT optimum. To see this, take _S_ to be a path, and observe that every rooted version of _S_ has average depth \(\Omega(n)\), whereas a BST on _S_ (which is, in particular, a 2-cut tree) has maximum depth _O_(log_n_).

