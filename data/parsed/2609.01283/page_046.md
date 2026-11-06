_Proof._ We invoke Theorem 3.7 on _M_<sub>graph</sub> and _M_<sub>part</sub> with rank _r=n_, packing parameter _k_, and susceptible set size \(\sigma\). Since any query modifies exactly _f+k_ diagonal entries in the weight matrix, we substitute these parameters directly into the bounds of Theorem 3.7 to complete the proof. \(\square\)

### Improved _s_-Min-Cut and Global Min-Cut via Fixed-Root Arborescences.

Recall that the \((f+k)^\omega\) query time in Theorem 8.6 is due to the fact that a query toggles _f+k_ diagonal entries: _f_ for the edge updates and _k_ for activating the parallel (_z,s_) query edges. If the root _s_ is _fixed_ at preprocessing, the _k_ parallel edges _E<sub>z,s</sub>_ can be activated once during preprocessing, so a query toggles only the _f_ entries of _U_. This yields a fixed-root oracle with query time \(O(f^\omega)\) and space \(O(\sigma^2)\), where now \(\sigma=|E_Q|\), independent of _k_.

This observation gives an alternate route to _s_-min-cut and global min-cut oracles. By Edmonds’ theorem, \(\mu_G(s)\) equals the maximum _k_ for which _G_ admits _k_ edge-disjoint _s_-rooted arborescences, and _f_ updates change this value by at most _f_. Hence, letting \(\rho:=\mu_G(s)\), it suffices to instantiate the fixed-root decision oracle for each \(k\in[max(0,\rho-f),\rho+f]\), that is, _O(f_) instances. A query performs a binary search over these instances to locate the largest feasible _k_. Global min-cut follows by maintaining these structures for both _G_ and _G_<sup>rev</sup> with respect to an arbitrary fixed _s_, since \(\mu_{G+U}=min\big(\mu_{G+U}(s),\mu_{(G+U)^\mathrm{rev}}(s)\big)\). We thus obtain the following.

**Corollary 8.7** (_s_-Min-Cut and Global Min-Cut Value via Arborescence Packing)**.** _Let G_=(_V,E_) _be an n-vertex directed graph with a susceptible set_ \(E_Q\subseteq E\) _of size_ \(\sigma\)_. Then there exist subset sensitivity oracles that, for any update set_ \(U\in E_Q^f\)_, report the values_ \(\mu_{G+U}(s)\) _(for a source s fixed at preprocessing) and_ \(\mu_{G+U}\)_, each with_ \(O(f\sigma^2)\) _space and_ \(\widetilde{O}(f^\omega)\) _query time, with high probability._

_Moreover, in the general sensitivity model, taking E<sub>Q</sub>=E yields s-min-cut and global min-cut value oracles with O(fm_<sup>2</sup>) _space and_ \(\widetilde{O}(f^\omega)\) _query time._

Compared to Theorems 8.4 and 8.5, Theorem 8.7 improves the query time from \(\widetilde{O}(f^{\omega+1})\) to \(\widetilde{O}(f^\omega)\) and the space from \(O(\sigma^3)\) to \(O(f\sigma^2)\). Similarly, in the general model it provides an alternative to Theorems 4.8 and 4.9, improving the query time from \(\widetilde{O}(f^{3\omega+1})\) to \(\widetilde{O}(f^\omega)\) at the cost of increased space. We note that Theorem 8.7 reports only the cut _value_; reporting the cut partition still goes through the nearest-min-cut approach of Theorem 8.4.

## 8.2.2 _k_-Disjoint Spanning Trees

Recall from Theorem 5.6 that finding _k_ edge-disjoint spanning trees was cast as a _k_-packing of common bases of two copies of the graphic matroid. We now restrict all updates to a susceptible set fixed at preprocessing time, replacing the general packing oracle of Theorem 3.5 with its subset counterpart, Theorem 3.7.

Let _E<sub>Q</sub>_ be a susceptible set of size \(\sigma\) (which may include edges not currently in _E_), representing edges that can be added, deleted, or re-weighted. Because this problem requires no auxiliary root vertices, the susceptible set for the data structure consists entirely of the edges in _E<sub>Q</sub>_, and modifying _f_ elements toggles or re-weights exactly _f_ diagonal entries in the packing Laplacian.

**Theorem 8.8.** _Let_ \(k\ge 1\) _be an integer, and G_=(_V,E,c_) _be an n-vertex undirected graph with integer edge costs in_ \[-_W,W_\] _and a susceptible edge set E<sub>Q</sub> of size_ \(\sigma\)_. Then there exist the following subset sensitivity oracles that, for any set of updates_ \(U\subseteq E_Q\) _of size at most f , answer queries on G+U with high probability:_

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Decision_ & \(O(\sigma^2(kn)^{\omega-2}+(kn)^\omega)\) & \(O(\sigma^2)\) & \(O((f+k)^\omega)\) & _Whether G+U has k-disjoint s-rooted arborescences_ \\
_Weighted_ & \(\widetilde{O}(W\sigma^2(kn)^{\omega-1}+W(kn)^{\omega+1})\) & \(\widetilde{O}(Wkn\sigma^2)\) & \(\widetilde{O}(Wkn(f+k)^\omega)\) & _Min total cost of such k-arborescences_ \\
\end{tabular}

