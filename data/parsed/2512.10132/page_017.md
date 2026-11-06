**Corollary 3** (Banded traceback)**.** _Consider a banded global alignment DP on an_ \(N\times N\) _grid of bandwidth B, with a max-type scoring scheme and deterministic tie-breaking. Then an optimal alignment confined to the band can be reconstructed deterministically in space_

\(\mathsf{SPACE}=O\big(Blog(BN)+polylog(BN)\big).\)

Naively storing back-pointers across the band requires \(\Theta(BN)\) words of space, while applying Hirschberg directly to the full grid would give an _O(N_) words space bound that does not reflect the band constraint. Corollary 3 shows that in the structural setting captured by frontier width, the correct parameter governing traceback space is the band width _B_, not the full sequence length _N_.

### 6.4 Graphs of bounded pathwidth

Finally, we consider a more abstract structural setting. Let _G_ be a DP DAG whose underlying undirected graph admits a path decomposition of width pw(_G_). It is known that pathwidth bounds the size of a contiguous vertex separator along a path decomposition; by aligning the topological order \(\tau\) with such a decomposition, one can ensure that the frontier width is bounded in terms of pathwidth.

**Lemma 6.** _Let G be a DAG whose underlying undirected graph has pathwidth_ pw(_G). Then there exists a topological order_ \(\tau\) _of V consistent with the edge directions such that the frontier width satisfies_

\(\omega(G)\le pw(G)+1.\)

_Proof sketch._ It is a standard result in structural graph theory that the pathwidth of a graph is equal to its _vertex separation number_ minus one (see, e.g., Kinnersley 1992). The vertex separation number is defined as the minimum over all linear orderings of vertices of the maximum cut size (where the cut size at index _i_ is the number of vertices \(\le i\) with neighbors _\>i_). However, an arbitrary linear ordering minimizing vertex separation might not respect the edge directions of the DAG _G_. We appeal to the fact that for DAGs, a topological sort consistent with the optimal vertex separation layout exists provided the layout is compatible. Alternatively, if we view the DP as being _defined_ over a path decomposition (as is common in tree-decomposition based DPs), the natural order of bags induces a topological sort where the frontier size is bounded by the bag size, which is at most pw(_G_)+1.

Combining Lemma 6 with Theorem 2 yields:

**Corollary 4** (Pathwidth parameterization)**.** _Let G be a DP DAG whose underlying graph has pathwidth_ pw(_G), and suppose the recurrence satisfies Assumption 2. Then there exists a topological order under which an optimal witness path to any sink can be reconstructed in space_

\(\mathsf{SPACE}=O\big(pw(G)log|V|+polylog|V|\big).\)

This connects our algorithmic result to structural graph parameters: up to polylogarithmic factors, the space required for witness reconstruction is controlled by the same width measure that controls the space needed for decision DPs on _G_. In particular, on bounded-pathwidth graph families, the "price of reconstruction" over and above evaluation is negligible.

## 7 Lower Bounds, Limitations, and Model Variants

We now discuss the extent to which the bound of Theorem 2 is optimal, and how much of it is driven by (i) intrinsic structure of the DP DAG (in particular, frontier width) versus (ii) the computational model (random access vs. streaming, multi-pass vs. single-pass). Throughout this section we distinguish carefully between:

• _forward-only single-pass models_, where the algorithm processes the vertices once in increasing topological order and never re-reads earlier parts of the input, and<tbc>

• the _offline random-access model_ used in our upper bound, where the algorithm may perform multiple forward passes over arbitrary intervals of the DAG.<tbc>

