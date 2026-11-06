In the first round, Algorithm 3 queries the degree of all _n_ vertices, followed by \(n/(1+\varepsilon)\) vertices in the second round, \(n/(1+\varepsilon)^2\) vertices in the third round, and so on. Thus, the total number of cut queries is \(3n(1+\frac{1}{1+\varepsilon}+\frac{1}{(1+\varepsilon)^2}+\cdots)\). This geometric series has sum \(3n(1+\varepsilon)/\varepsilon\), and so Algorithm 3 requires \(O(n/\varepsilon)\) queries, assuming that \(\varepsilon=O(1)\).

## B.3 add Algorithms for DSH

In this section, we point out two existing algorithms for Densest Subhypergraph that can be implemented with add queries since one can learn induced degrees using the identity deg_<sub>S</sub>(v_)=add(_S_)-add(_S_\\_v_). In the case of _r_-uniform hypergraphs, one can verify that running Algorithm 3 with a threshold of \(r(1+\varepsilon)\rho(S)\) yields an \(r(1+\varepsilon)\)-approximation to DSH by similar analysis to Proposition 1.

**Proposition 11.** Let _H_ be an _r_-uniform weighted hypergraph. There is a deterministic algorithm that makes \(O(n/\varepsilon)\) add queries and returns a \(r(1+\varepsilon)\) approximation to the densest subhypergraph of _H_.

Beyond uniform hypergraphs, the iterative peeling algorithm Super-Greedy++ yields an add approximation scheme for DSH making polynomially-many queries.

**Proposition 12** (\[13, Theorem 4.1\])**.** Let _H_ be a weighted hypergraph. There is a deterministic algorithm that makes \(O(n^3\mathrm{log}n/\varepsilon)\) add queries and returns a \((1+\varepsilon)\) approximation to the densest subhypergraph of _H_.

Based on the algorithm Greedy++ proposed in \[8\], Chekuri et al. \[13\] prove that Super- Greedy++ achieves a \((1+\varepsilon)\)-approximation to the Densest Supermodular Subset problem in \(O(\Delta\mathrm{log}n/\varepsilon^2\rho^*(G))\) rounds over the graph, where each round is essentially the one-by-one pruning algorithm of Charikar \[12\]. Since these rounds require learning _O(n_<sup>2</sup>) induced degrees and we can make a rough lower bound of \(\rho^*(G)\ge\rho(V)\ge\Delta/n\), then Super-Greedy++ requires at most \(O(n^3\mathrm{log}n/\varepsilon)\) add queries for a \((1+\varepsilon)\)-approximation to DSH.

