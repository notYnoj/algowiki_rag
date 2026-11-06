## 5.6 Certifying Near-Optimal Water-Network Design

The waterund36 instance in MINLPLib minimizes the cost of a water-using network under nonlinear flow and concentration constraints (MINLPLib, 2026). A feasible network costing approximately 662.807 was already known, but the listed global lower bound was only about 655.544.

Épi tightens the lower bound to within approximately 10<sup>-5</sup> of that same feasible value, closing more than 99.999% of the MINLPLib gap. This certifies the near-optimality of the existing network. The full-precision comparison appears in Appendix A.12.

To establish the bound, the agent constructs a relaxation containing every feasible network. Exact rational inequalities then rule out objective values below the stated cutoff. The certificate therefore applies to the original nonlinear problem. Appendix A.12 explains this argument and relates the instance to earlier optimization work.

## 5.7 From Numerical Optimization to Proof: Tuza’s Conjecture

For a finite simple graph _G_, let \(\upsilon_\triangle(G)\) be the maximum number of pairwise edge-disjoint triangles and \(\tau_\triangle(G)\) the minimum size of a _triangle cover_: a set of edges meeting every triangle in _G_. Equivalently, deleting a triangle cover makes the entire graph triangle-free. Tuza’s conjecture, proposed in 1981 (Bonamy et al., 2022), asserts

\(\tau_\triangle(G)\le 2\upsilon_\triangle(G).\) (6)

Thus, if _G_ contains no _k_+1 pairwise edge-disjoint triangles, deleting at most 2_k_ edges suffices to eliminate every triangle in _G_.

**Packing and covering.** König’s theorem equates the maximum matching size and minimum vertex-cover size in a bipartite graph (König, 1931). Tuza’s conjecture concerns a matching-cover relation in the _triangle hypergraph_, whose vertices are the edges of _G_ and whose hyperedges are its triangles. Taking all edges of a maximum triangle packing gives the elementary bound \(\tau_\triangle\le 3\upsilon_\triangle\): any uncovered triangle could be added to the packing. The conjectured factor of two is attained by _K_<sub>4</sub>, where \(\upsilon_\triangle=1\) and \(\tau_\triangle=2\).



A Quartic attractor dimension
B Water-network design
>3.6 millionx narrower
Width of the rigorous enclosure
>99.999% gap closed
Gap to the same known feasible value
Reference 0.0078
Reference 7.26
Épi 2.13e-09
Épi 1.001e-05
10-9
10-6
10-3
10-5
10-2
101
Interval width (log scale)
Objective gap (log scale)

**Figure 6:** Two improvements in certified uncertainty. The horizontal axes show interval or bound-gap width on logarithmic scales. Left: the rigorous enclosure for the quartic Feigenbaum attractor dimension becomes over 3.6 million times narrower. Right: the waterund36 gap to the same known feasible value decreases from about 7.263 to \(1.001\times 10^{-5}\).

