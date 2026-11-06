<tbc>showing that any deterministic two-player communication protocol for exactly computing the _value_ of the minimum _s-t_ cut requires \(\widetilde{\Omega}(n^{3/2})\) bits of communication would be an exciting result.

### Improving Combinatorial Protocols.

Similarly, it is natural to ask whether a \(\widetilde{O}(n^{3/2})\)-bit protocol for computing minimum _s-t_ cuts can be achieved using combinatorial techniques. The work of \[GJ25\] confirms that such an upper bound is indeed possible, but their protocol relies on non-combinatorial continuous optimization approaches. We leave it as an open question whether this \(\widetilde{O}(n^{3/2})\) bound can be matched by a fully combinatorial protocol. Our \(\widetilde{O}(n^{11/7})\)-bit deterministic protocol (Theorem 1.2) represents progress in this direction.

### Deterministic Algorithms.

While our \(\widetilde{O}(n^{11/7})\) protocol for the two-party communication model is fully deterministic, our \(\widetilde{O}(n^{8/5})\) cut-query algorithm is randomized. To date, the only known deterministic cut-query algorithm for computing a minimum _s-t_ cut is the \(\widetilde{O}(n^{5/3})\)-query algorithm of \[ASW25\], which is based on a careful implementation of Dinitz’s blocking flow method. It remains an open question whether this \(\widetilde{O}(n^{5/3})\) bound can be improved in the deterministic setting.

Notably, our \(\widetilde{O}(n^{8/5})\) algorithm is deterministic except for one component: the computation of an \(\varepsilon\)-cut sparsifier. Hence, a deterministic algorithm for constructing such a sparsifier using \(\widetilde{O}(n/\varepsilon^2)\) cut queries would immediately yield a fully deterministic \(\widetilde{O}(n^{8/5})\)-query algorithm for the minimum _s-t_ cut problem under our framework. Moreover, via the reduction of \[ASW25\], such an improvement would also extend to computing global minimum cuts deterministically within the same query complexity, up to polylogarithmic factors.

### All-Pairs Min-Cut.

Another natural problem in the cut-query model is to compute the _all- pairs_ min-cut of a graph. Simultaneous to our work, Kenneth-Mordoch and Krauthgamer \[KK25a\] presented the first non-trivial algorithm for this problem, requiring \(\widetilde{O}(n^{7/4})\) randomized cut queries. Given the recent progress in the sequential setting, where the complexity of all-pairs min-cut has been nearly matched to that of an _s-t_ min-cut \[ALPS23; AKL+25; GKYY25\], it is natural to ask whether a similar equivalence can be achieved in the cut-query model. A weaker, yet still interesting, open question is whether one can improve upon the complexity of \(\widetilde{O}(n^{7/4})\) in either the cut-query or two-player communication setting, which is already an interesting problem in its own right.

## References

\[ACK19\] Sepehr Assadi, Yu Chen, and Sanjeev Khanna. "Polynomial pass lower bounds for graph streaming algorithms". In: _Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing, S 2019, Phoenix, AZ, USA, June 23-26, 2019._ Ed. by Moses Charikar and Edith Cohen. ACM, 2019, pp. 265–276.

\[AD21\] Sepehr Assadi and Aditi Dudeja. "A Simple Semi-Streaming Algorithm for Global Minimum Cuts". In: _4th Symposium on Simplicity in Algorithms, SOSA 2021, Virtual Conference, January 11-12, 2021._ Ed. by Hung Viet Le and Valerie King. SIAM, 2021, pp. 172–180.

\[AEG+22\] Simon Apers, Yuval Efron, Pawel Gawrychowski, Troy Lee, Sagnik Mukhopadhyay, and Danupon Nanongkai. "Cut Query Algorithms with Star Contraction". In: _63rd IEEE Annual Symposium on Foundations of Computer Science, FOCS 2022, Denver, CO, USA, October 31 - November 3, 2022._ IEEE, 2022, pp. 507–518.

