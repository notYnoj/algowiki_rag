For 3SUM, Fischer, Kaliciak, and Polak \[5\] derandomized the set-disjointness reduction of Kopelowitz, Pettie, and Porat \[4\]. For Exact Triangle, Vassilevska Williams and Xu \[6\] gave a randomized reduction to the lopsided problem. Chan and Xu \[7\] gave a deterministic reduction to All-Edges Sparse Triangle, but its construction does not ensure the small middle part needed here. Alman and Vassilevska Williams \[1\] obtain the deterministic lopsided reduction by combining deterministic hashing with the earlier graph constructions. We use these reductions as black boxes.

_Proof of Theorem 1.2. 3SUM._ Fischer, Kaliciak, and Polak \[5\] show that, for every fixed \(0<\eta<1\), a deterministic truly subquadratic algorithm for Offline Set Disjointness with _O(n_) sets, universe size \(O(n^{2\eta})\), set size \(O(n^\eta)\), and \(O(n^{2-\eta})\) queries gives a deterministic truly subquadratic algorithm for 3SUM. Choose \(\eta>0\) with \(2\eta K<1\). After padding the families and universe to sizes \(\Theta(n)\) and \(d=\Theta(n^{2\eta})\), respectively, the query bound is \(O(n^2/\sqrt{d})\). A constant number of query batches allows Theorem 3.1 to solve these instances in \(\widetilde{O}(n^{2-\eta/4})\) time, giving the 3SUM conclusion.

_APSP._ Exact Triangle asks whether an integer-weighted tripartite graph with _n_ vertices per part contains a triangle whose edge weights sum to zero. We restrict to weights of magnitude _n_<sup>_O_(1)</sup>. Alman and Vassilevska Williams \[1\] reduce it deterministically, for \(16\le d\le n\) and an integer \(1\le g\le\sqrt{d}\), to _O(ng_) set-disjointness instances with parameters (_n,d_) and at most \(n^2/\sqrt{d}\) queries each, with additional time

\(\widetilde{O}(n^3/g+n^{\omega+o(1)}d^{3/2}+n^2dg),\)

where \(\omega<3\) is the square matrix multiplication exponent.

Choose \(d=\lfloor n^\varepsilon\rfloor\) for a sufficiently small fixed \(\varepsilon>0\), and set \(g=\lceil d^{1/16}\rceil\). By Theorem 3.1, the oracle calls cost \(\widetilde{O}(ng\cdot n^2/d^{1/8})=\widetilde{O}(n^3/d^{1/16})\), as does the first overhead term. Since \(\omega<3\), choosing \(\varepsilon\) small enough also ensures \(d^K\le n\) and makes the other two overhead terms smaller than this bound. Thus Exact Triangle takes \(\widetilde{O}(n^{3-\rho})\) time for some constant \(\rho>0\).

The deterministic reduction of Vassilevska Williams and Williams \[8, 9\] solves APSP in \(\widetilde{O}(n^{3-\rho/3})\) time, using only the decision version of Exact Triangle. Absorbing logarithmic factors gives the claimed polynomial improvement.

## References

