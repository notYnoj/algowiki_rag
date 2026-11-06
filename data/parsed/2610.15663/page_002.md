The first term pays for preparing linear combinations of the inputs; the second pays for multiplying these forms and reconstructing the requested outputs. Reducing \(\tau\) makes the latter cheaper, at the expense of increasing \(\kappa\) and restricting the allowable middle dimension _d_. Alman and Vassilevska Williams \[1\] call such products _thin_ and the prescribed outputs _wanted entries_.

For example, take \(\tau=1/4\), let \(\kappa=\kappa(1/4)\), and suppose \(d^{\kappa+1}\le n\). Computing \(w=\lfloor n^2/d\rfloor\) specified entries of an \(n\times d\) by \(d\times n\) product then takes \(\widetilde{O}(n^2/d^{1/4})\) time. Separate dot products would take \(\Theta(n^2)\) operations, and the full product has _n_<sup>2</sup> entries. When _d_ is a fixed positive power of _n_, this saves a polynomial factor over both approaches.

### Fine grained algorithms.

Integer 3SUM asks whether a list of _n_ integers contains three entries with distinct indices whose sum is zero. All-pairs shortest paths (APSP) asks for the shortest-path distance between every ordered pair of vertices in a directed graph. We allow negative edge weights but assume there is no negative cycle. Combining Theorem 1.1 with known reductions gives the following corollary.

**Corollary 1.2.** _There are absolute constants_ \(\delta_1,\delta_2>0\) _such that integer 3SUM on n polynomially bounded integers has a deterministic_ \(O(n^{2-\delta_1})\)_-time algorithm, and APSP on an n-vertex directed graph with polynomially bounded integer edge weights and no negative cycle has a deterministic_ \(O(n^{3-\delta_2})\)_-time algorithm._

We have not tried to optimize the constants; our focus is on simplicity of exposition.

## 1.1 Proof overview

### Selected-entry matrix multiplication.

The algebraic starting point is the inner/outer-product identity of Schönhage \[2\], used by Coppersmith \[3\] for rectangular matrix multiplication. Alman and Vassilevska Williams \[1\] adapt this approach to exploit the overlap among the computations needed by selected entries. We express this sharing through an exact multiplication rule: each output is a sum of six products from a common collection, minus one private correction term. The common collection is small relative to the number of outputs, and the same intermediate value can serve many requested entries. We apply the rule recursively to matrix blocks and count the resulting requests, capping each count by the number of available output positions. Our simplification is in the explicit rule and this counting argument; the central idea of exploiting sparse output requests comes from Alman and Vassilevska Williams \[1\].

### Fine grained algorithms.

In _Offline Set Disjointness_ \[4, 5\], we are given two families of sets and a list of pairs, one set from each family, and must determine which pairs are disjoint. The product of the families’ incidence matrices records all intersection sizes. When the universe is small, Theorem 1.1 computes the requested intersection sizes efficiently. For 3SUM, we use the direct deterministic reduction of Fischer, Kaliciak, and Polak \[5\]. For APSP, we use the standard reduction to Exact Triangle, followed by the deterministic reduction to lopsided triangle queries of Alman and Vassilevska Williams \[1\].

### Further research.

How far can selected-entry matrix multiplication be improved? What is the best possible dependence on the middle dimension _d_ when computing _w_ arbitrary entries of an \(n\times d\) by \(d\times n\) product? Can we reduce the \(d^\tau\) loss in Theorem 1.1 without increasing the input-preparation cost or requiring thinner matrices? Can comparable savings hold for larger _d_? For which ranges of _d_ and _w_ can selected-entry algorithms substantially outperform the best rectangular<tbc>

