variables. Its number of constraints and their encoding size are also polynomial in _n_, _m_, and _q_ for fixed _D_, and all scalar coefficients are \(0,\pm 1\). Thus the direct formulation already admits polynomial- time LP optimization in that setting. The construction below instead has _O(mq_<sup>2</sup>) variables and constraints, hence _O(nDq_<sup>2</sup>) for maximum degree _D_. Its size has no exponential dependence on _D_.

## Representing a parity check by a layered graph.

Fix a syndrome \(\mathbf{s}\in\mathrm{im}H\). For each nonempty check, we construct a separate auxiliary directed graph, called a _trellis_. Its nodes are arranged in successive layers, and its directed edges go from one layer to the next. These nodes are not vertices of _G_: they record running sums as the symbols in one check are assigned values.

Fix a vertex _v_ with _d<sub>v</sub>\>_0, and order the edges in its parity-check support as \(\partial v=\{e_1,\dots,e_{d_v}\}\). At layer _i_=0_,...,d<sub>v</sub>_, include one node (_i,z_) for each \(z\in\unknown_q\). The node records the weighted partial sum \(z=\sum_{j=1}^ih_{ve_j}b_{e_j}\). Assigning the next symbol value _b<sub>e<sub>i</sub></sub>=a_ is represented by the directed edge

\((i-1,z)\rightarrow(i,z+h_{ve_i}a),\text{labelled}a.\) (219)

We include this edge for every _i_=1_,...,d<sub>v</sub>_ and \(z,a\in\unknown_q\). Starting at (0,0), each sequence of symbol values determines exactly one path. The assignment satisfies the check precisely when that path ends at (_d<sub>v</sub>,s<sub>v</sub>_). Different partial assignments with the same weighted sum reach the same node; the graph need not store them separately.

## A binary example.

For the check _b_<sub>1</sub>+_b_<sub>2</sub>+_b_<sub>3</sub>=0 over \(\unknown_2\), the state at layer _i_ is the sum of the first _i_ symbols modulo two. Choosing 0 preserves the sum, whereas choosing 1 changes it to the other value. The full trellis has eight nodes and twelve directed edges, as shown in Fig. 2. The four paths from (0,0) to (3,0) represent exactly the satisfying assignments 000, 011, 101, and 110. For example, the assignments 000 and 110 both reach (2,0) after two steps and use the same final edge. Their earlier choices are recorded by their paths, not by separate copies of the node (2,0).

## From assignment probabilities to flows.

A probability distribution over satisfying assignments is a probability distribution over paths from (0,0) to (_d<sub>v</sub>,s<sub>v</sub>_). Send each path’s probability along its directed edges. The resulting nonnegative edge flows have total supply one at (0,0), total demand one at (_d<sub>v</sub>,s<sub>v</sub>_), and flow conservation at all other nodes, with zero supply or demand elsewhere. Conversely, any flow obeying these constraints in this acyclic graph decomposes into a convex combination of such paths, hence into a distribution over satisfying assignments.

Let _f<sub>v,i,z,a</sub>_ be the flow on the edge labelled _a_ from (_i_-1_,z_). The total flow choosing _a_ for symbol _e<sub>i</sub>_ must equal its marginal:

\(x_{e_i,a}=\sum_{z\in\unknown_q}f_{v,i,z,a}.\) (220)

Use the same variables _x<sub>e,a</sub>_ in the trellises for both endpoints of _e_, and keep the objective L(**x**) unchanged. The two formulations then have exactly the same feasible symbol marginals, and therefore the same optimal marginal vectors. The reformulation neither tightens nor weakens the LP relaxation, so all recovery guarantees proved above apply to it. A vertex with _d<sub>v</sub>_=0 imposes only _s<sub>v</sub>_=0 and can be omitted because the syndrome is valid.

## Size and complexity.

Each nonempty check uses _d<sub>v</sub>q_<sup>2</sup> directed edges and _O(d<sub>v</sub>q_) node constraints. Since \(\sum_vd_v=2m\le nD\), including the shared symbol marginals and their consistency<tbc>

