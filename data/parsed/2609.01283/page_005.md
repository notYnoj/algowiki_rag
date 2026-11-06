<tbc>Theorem 8.7) that reports the cut _value_ in just \(\widetilde{O}(f^\omega)\) time, at the cost of _O(fm_<sup>2</sup>) space, exhibiting a complementary space-query trade-off.

## Spanning structures.

Our framework also yields sensitivity oracles for a broad class of spanning structure problems. As a basic example, consider the problem of deciding whether _G_ admits a reachability tree rooted at _s_ after _f_ updates. Existing pairwise reachability oracle of Brand and Saranurak \[vdBS19\] require \(\Omega(n)\) queries<sup>1</sup> to certify this property, and with query time depending only on _f_ was previously not known. We instead obtain an oracle for deciding the existence of _k_ edge-disjoint arborescences rooted at a _query_ root _s_ in \(O((fk^2)^\omega)\) time. Instantiating _k_=1 yields an \(O(f^\omega)\)-time oracle for rooted reachability trees.

As an immediate consequence, since _k_-strong connectivity amounts to existence of _k_-arborescence packing in both directions from any root, we decide _k_-strong connectivity of _G+U_ in \(O((fk^2)^\omega)\) time with _O_((_kn_)<sup>2</sup>log_n_) space (Theorem 5.4). For comparison, for _k_=1, the oracle of \[BCR19\] reports the strongly connected components after _f_ failures using _O_(2_<sup>f</sup>n_<sup>2</sup>) space and \(\widetilde{O}(2^fn)\) query time; for the decision problem we replace both exponential dependencies by poly(_f_).

The same guarantees extend to deciding the existence of _k_ edge-disjoint spanning trees. We also obtain the first sensitivity oracle for colorful (rainbow) spanning trees, with \(O(f^\omega)\) query time and quadratic space, and additionally provide a matching lower bound on the oracle size. Finally, we give the first sensitivity oracle for deciding whether the updated graph has arboricity (the minimum number of forests needed to cover edges of a graph) at most _k_, answering queries in \(O((fk)^\omega)\) time (see  3).

## Matroid matching, matchings, and \(\alpha\)-factors.

Finally, our framework extends to _matroid matching (parity)_: for a _c_-sparse linear matroid of rank _r_ on _m_ pairs, we obtain sensitivity oracles deciding the existence of a parity basis after _f_ pair updates in \(O((c^2f)^\omega)\) time using _O(r_<sup>2</sup>log_r_) space. Since matroid parity generalizes both matroid intersection and non-bipartite matching, these<tbc>

<sup>1</sup>Note that poly(_f_) query time is possible using work of \[vdBS19\] when updates are restricted to edge deletions, but the general setting of both insertions and deletions is more challenging.

\begin{tabular}{ccccc}
**Query pair** & **#Failures** & **Space** & **Query Time** & **Ref.** \\
_Prior work_ & & & & \\
fixed (_s,t_) & \(f\le 2\) & _O(n_<sup>2</sup>) & _O_(1) & \[BBP22\] \\
fixed (_s,t_) & \(f\le 2\) & \(O(\lambda n)\) & _O_(1) & \[ACP<sup>+</sup>26\] \\
fixed (_s,t_) & any _f_ & \(2^{O_f(\lambda^4log\lambda)}n\mathrm{log}n\) & \(2^{O_f(\lambda^4log\lambda)}\mathrm{log}n\) & \[ACP<sup>+</sup>26\] \\
_This paper_ & & & & \\
\(V\times V\) , _k_-bounded & any _f_ & \(\widetilde{O}((kn)^2)\) & \(\widetilde{O}((fk^2)^\omega)\) & Thm 4.2 \\
nearest min-cut & any _f_ & \(\widetilde{O}((kn)^2)\) & \(O((fk^2)^\omega n)\) & Thm 4.2 \\
min-cost flow & any _f_ & \(\widetilde{O}(W(kn)^3)\) & \(\widetilde{O}((fk^2)^\omega kWn)\) & Thm 4.2 \\
fixed (_s,t_), exact & any _f_ & \(\widetilde{O}((fn)^2)\) & \(\widetilde{O}(f^{3\omega})\) & Thm 4.5 \\
nearest min-cut & any _f_ & \(\widetilde{O}((fn)^2)\) & \(\widetilde{O}(f^{3\omega} n)\) & Thm 4.5 \\
min-cost max-flow & any _f_ & \(\widetilde{O}(W(fn)^3)\) & \(\widetilde{O}(f^{3\omega+1}Wn)\) & Thm 4.5 \\
\end{tabular}

2: Sensitivity oracles for (_s,t_)- max-flow and min-cut in directed graphs. Here \(\lambda\) is the value of (_s,t_)-max-flow in _G_.

