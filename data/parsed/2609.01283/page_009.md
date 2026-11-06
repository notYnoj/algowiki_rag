_Any f edge updates in the graph translate to a sparse additive update to_ L<sub>pack</sub> _containing only O(fk_<sup>2</sup>) _non-zero entries._

To evaluate this perturbed determinant, we utilize the Matrix Determinant Lemma, which allows us to compute the determinant of a matrix under a low-rank update in time proportional to the update size, provided we have precomputed its inverse. We leverage the data structure of Brand and Saranurak \[vdBS19\] to achieve this.

_Remark on Singular Matrices:_ The original tool of \[vdBS19\] required the base matrix L<sub>pack</sub> to be invertible (i.e., the base graph must already possess the required flow). We remove this limitation by introducing a random low-rank numeric pad _UV<sup>T</sup>_ during preprocessing that forces invertibility. When a query arrives, we fold the numeric pad back into the query update as a structured low-rank perturbation (Theorem A.2), allowing the determinant lemma to work seamlessly even if the base matrix is identically singular.

With this tool, an _f_-edge update can be evaluated in \(O((fk^2)^\omega)\) time for the decision version, and \(\widetilde{O}(Wkr(fk^2)^\omega)\) time for the weighted version.

### Extension to All-Pairs queries via Parallel Elements.

To extend this to dynamic all-pairs \((V\times V)\) queries without blowing up the matrix dimension, we introduce a static dummy source _s_<sup>∗</sup> and dummy sink _t_<sup>∗</sup> during preprocessing. At query time, to test (_s,t_)-flow, we dynamically insert _k_ parallel edges from _s_<sup>∗</sup> to _s_ and from _t_ to _t_<sup>∗</sup>. Crucially, parallel copies of an edge share the exact same sparse column support in the base matroid representations. Thus, adding _k_ parallel edges only perturbs an \(O(k)\times O(k)\) block in the Laplacian-contributing _O(k_<sup>2</sup>) modified entries, exactly the same cost as a _single_ edge update. Therefore, an all-pairs query with _f_ updates costs \(O((fk^2+k^2)^\omega)=O((fk^2)^\omega)\) time, rather than a naive multiplicative blowup of \(O(((f+k)k^2)^\omega)\).

## 1.2.2 Two Strategies for Exact (_s,t_)-Max-Flow

The bounded flow oracle performs well for small flow values, whereas extending it to exact, unbounded (_s,t_)-max-flow remains challenging. In particular, setting _k=n_ in the all-pairs oracle leads to extremely slow query time.

We develop two distinct strategies to resolve this: one focusing on algorithmic rerouting, and the other on structurally decoupling the matrix updates.

### Strategy 1: Residual Graph Reduction

Here we consider the question if recomputing the exact flow value after _f_ edge updates can be reduced to All-pairs bounded flow problem. Our core insight is that _sensitivity does not require computing the entire flow, only repairing it_.

During preprocessing, we compute an exact max-flow _h_ of value \(\lambda_G(s,t)\). Consider a set of edge failures _F_, of which \(d\le f\) edges actually carried flow in _h_. Deleting these _d_ edges destroys exactly _d_ units of flow, leaving _d_ units of excess at the severed tail vertices and _d_ units of deficit at the head vertices.

To repair the flow, we must re-route these _d_ units of excess to the deficits. This is equivalent to finding _d_ edge-disjoint paths in the _residual graph_ (_G-F)<sub>h</sub>_. By attaching a dummy source to the excess vertices and a dummy sink to the deficit vertices, repairing the exact max-flow is reduced completely to an all-pairs bounded-flow query on the residual graph with an effective capacity bound of \(k=d\le f\).

To support insertions and accurately track the new flow value, we pad the base graph _G_ with 2_f_ zero-cost parallel (_s,t_)-buffer edges, saturating _f_ of them in _h_. Insertions and deletions simply<tbc>

