<tbc>Remarkably, the reconstruction rules preserve every optimum. On the instance constructed from 819 samples, the reductions decrease the graph from 440 to 281 vertices and from 1868 to 1076 conflict edges. Thus one can remove 36.1% of the logical variables and 42.4% of the conflict edges. These reductions benefit both classical and quantum solvers.

Our solver-agnostic approach has the potential to completely reduce the input graph: in one instance, the residual graph could be completed exactly after a reduction from 64 to five edge-free vertices. Then the enumeration problem becomes trivial and the full optimum set on the original graph can be easily recovered.

The second contribution is a QUBO formulation of the MWC problem through the corresponding MWIS problem on the complement graph, together with modifications to the standard QAOA procedure aimed at sampling multiple optimum solutions on current devices. We use a postprocessing procedure inspired by the classical greedy algorithm for the clique problem. This procedure runs in polynomial time, removes conflicts, and extends the resulting feasible solution until it is maximal. It maps sampled subgraphs to maximal cliques, which form a substantially smaller set than arbitrary subgraphs. The procedure does not by itself establish that the result has maximum weight. A repaired clique is accepted as an MWC only when its weight agrees with a current optimum value.

Since the postprocessing procedure enforces the edge constraints, the cost Hamiltonian need not enforce them with the same strength. On the small graphs for which all subgraphs could be enumerated, we found that a smaller Lagrange multiplier produced a larger proportion of low energy states that repaired to MWCs among the tested values. In this regime, the MWCs need no longer correspond exactly to the ground states of the Hamiltonian. However, low energy states may contain conflict edges that can be removed during postprocessing, rather than forming a lower weight clique whose structure differs substantially from every MWC. This motivates the use of the Hamiltonian as a sampling objective together with deterministic repair, rather than as an exact encoding in this parameter regime.

Using a sampling method to enumerate _N_ optimum solutions requires at least _N_ samples. Under uniform independent sampling, the coupon collection model gives an expected sample count of order _N_log_N_. The classical experiments show that the distribution over the optimum solutions can be strongly nonuniform, so this estimate should be treated as an idealised reference.

On a graph with 64 vertices, the modified QAOA procedure recovered more distinct certified MWCs than the random shot baseline in each of the ten reported runs. This result demonstrates improved sample coverage on the tested instance, but it is not a claim of quantum advantage. Taken together, the results support a modular approach in which exact preprocessing, classical completion, and sampling methods are selected according to the residual graph and the required level of completeness.

## 7  Availability

AClique is available from `https://github.com/q4bio-qpg/aclique`.

The modified Cherry’s algorithm is available from `https://github.com/q4bio-qpg/qcompat`.<tbc>

