## 1.1 Our Contributions

Let _M_<sub>1</sub>_,M_<sub>2</sub> be two linear matroids of rank _r_ on a common ground set _E_ of size _m_, with integer element weights in \[-_W,W_\]. Given \(k\ge 1\), the _k-packing_ problem asks whether there is a set \(S\subseteq E\) of size _kr_ that can be partitioned into _k_ pairwise disjoint common bases of _M_<sub>1</sub> and _M_<sub>2</sub> (the two partitions may differ); the weighted version asks for the minimum weight of such a set. The _k- covering_ problem asks whether the entire ground set can be partitioned into _k_ independent sets of a given matroid. In the _general sensitivity model_, the oracle must support up to _f_ arbitrary element updates (insertions, deletions, or weight changes) anywhere in the ground set.

For _sparse_ linear matroids (constant many non-zeros per column of the linear representation), we obtain the following.

Instantiating this framework, and combining it with new problem-specific reductions, yields the first sensitivity oracles supporting an arbitrary number _f_ of updates for a broad range of problems.

### All-pairs Bounded Flow.

For directed unit-capacity graphs with costs in \[-_W,W_\] and a flow bound _k_, we obtain an oracle that, for any pair (_s,t_) and any _f_ edge updates, report \(min(k,\lambda_{G+U}(s,t))\) in \(O((fk^2)^\omega logk)\) time, where \(\lambda_{G+U}(s,t)\) denotes the value of (_s,t_)-max-flow in the updated graph. Further, the oracle identifies the nearest (_s,t_) min-cut and computes the minimum cost of the corresponding flow, when \(\lambda_{G+U}(s,t)<k\) (see  2). Our result extends the reachability and distance sensitivity oracles of Brand and Saranurak \[vdBS19\] (the special case _k_=1), which are known to be near-optimal for constant _f_; for _k\>_1 no comparable oracles were known even for undirected graphs, where the state of the art was the single-failure all-pairs min-cut oracle of \[BP22\].

### Fixed-pair (_s,t_)-max-flow.

Our most notable application is for a fixed source-sink pair with _arbitrary_ flow value. Applying the all-pairs oracle with _k=n_ would be unnecessarily expensive; instead we present a flow-rerouting reduction whose effective capacity bound is _k=O(f_), thereby eliminating the blowup associated with large flow values. After any _f_ updates the oracle outputs the updated flow value in just \(O(f^{3\omega})\) time (see  2).

This fully resolves the open problem of Baswana, Bhanja, and Pandey \[BBP22\] for every _f_. Moreover, the space is essentially optimal for any constant \(f\ge 2\) due to \(\Omega(n^2)\) space lower bound by Bhanja \[Bha24\]. In contrast with \[ACP<sup>+</sup>26\], whose bounds degrade as 2<sup>_O<sub>f</sub>(k_<sup>4</sup>log_k_)</sup>, our bounds are polynomial in _f_ and independent of _k_.

### _s_-min-cut and global min-cut in directed graphs.

No non-trivial sensitivity oracles were known for these problems in directed graphs; undirected results \[DN95, Bha25\] existed for \(f\le 2\). We present the first directed _s_-min-cut and global min-cut oracles for arbitrary _f_ with _O(f_<sup>2</sup>_n_<sup>3</sup>log_n_) space and \(\widetilde{O}(f^{3\omega+1})\) query time. Additionally, the oracle reports the corresponding cut in \(\widetilde{O}(f^{3\omega} n)\) time. Further, we provide \(\Omega(n^2)\) lower bound for these problems, for any constant \(f\ge 2\). We also present an alternate oracle for _s_-min-cut and global min-cut via arborescence packings (see<tbc>

\begin{tabular}{ccccc}
**Problem** & **Ref** & **Preprocessing** & **Space** & **Query Time** \\
_k_-Packing (decision) & Thm 3.5 & \(O(k^2m+(kr)^\omega)\) & _O(km_+(_kr_)<sup>2</sup>log(_kr_)) & \(O((fk^2)^\omega)\) \\
_k_-Packing (weighted) & Thm 3.5 & \(\widetilde{O}(k^2m+W(kr)^3)\) & _O(km+W(kr_)<sup>3</sup>log(_kr_)) & \(\widetilde{O}(Wkr(fk^2)^\omega)\) \\
_k_-Covering (decision) & Thm 3.10 & \(O((kr)^\omega)\) & _O_((_kr_)<sup>2</sup>log(_kr_)) & \(O((fk)^\omega)\) \\
\end{tabular}

1: Sensitivity oracles for matroid _k_-packing and _k_-covering.

