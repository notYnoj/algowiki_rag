So, the total query time to output the vertex partition is \(\widetilde{O}(f^\omega n)\). \(\square\)

**Theorem 8.5.** _Let G_=(_V,E,**c**_) _be an n-vertex directed graph with a susceptible set_ \(E_Q\subseteq E\) _of size_ \(\sigma\)_. Then there exist the following subset sensitivity oracles that, for any update set_ \(U\in E_Q^f\) _consisting of insertions and deletions, answer queries on G+U with high probability:_

_Proof._ We fix an arbitrary vertex \(s\in V\) at preprocessing. As in the general construction (Theorem 4.9), we compute _independent_ optimal augmentations, and hence distinct augmenting sets _I_<sup>∗</sup>, for _G_ and for _G_<sup>rev</sup> with respect to _s_. We then instantiate the subset _s_-min-cut value and partition oracles of Theorem 8.4 for both _G_ (with susceptible set _E<sub>Q</sub>_) and _G_<sup>rev</sup> (with the reversed susceptible set \(E_Q^\mathrm{rev}\), of the same size \(\sigma\)). The preprocessing and space bounds are same as in Theorem 8.4.

Using the fact \(\mu_{G+U}=\mathrm{min}\big(\mu_{G+U}(s)\), \(\mu_{(G+U)^\mathrm{rev}}(s)\big)\), a value query evaluates the _s_-min-cut value on both _G+U_ and (_G+U_)<sup>rev</sup> in \(\widetilde{O}(f^{\omega+1})\) time and returns the smaller value. For a partition query, we first determine which of the two attains the minimum and then invoke the corresponding subset partition oracle in \(\widetilde{O}(f^\omega n)\) time. \(\square\)

## 8.2 Subset Sensitivity for Spanning Structures

Finally, we lift the spanning-structure oracles of Section 5 to the subset model. The reductions of Theorems 5.2, 5.5 and 5.9 are reused unchanged; only the underlying packing/covering oracle is replaced by its subset counterpart.

### 8.2.1 _k_-Disjoint Arborescences

Let _G_=(_V,E,**c**_) be an _n_-vertex directed graph. We are given a set of _query roots_ \(V_Q\subseteq V\) from which the arborescence root can be chosen, and a set of _susceptible edges E<sub>Q</sub>_ (which may include edges not currently in _E_) subject to insertions or deletions.

### Ground Set and Susceptible Set

We construct _G_<sup>∗</sup> with the dummy root _z_ and matroids _M_<sub>graph</sub> and _M_<sub>part</sub> as in Section 5. To support dynamic root queries from _V<sub>Q</sub>_, we include in the full ground set _k_ parallel edges from _z_ to _s_ for each \(s\in V_Q\). The susceptible set is the union of the susceptible graph edges and the potential root query edges:

\(E_0=E_Q\cup\bigcup_{s\in V_Q}E_{z,s},\sigma:=|E_0|=|E_Q|+k|V_Q|.\)

A query (_s,U_) with \(s\in V_Q\) and \(U\subseteq E_Q\) modifies exactly _f_ diagonal entries for the edge updates and exactly _k_ diagonal entries to activate the (_z,s_) query edges. Thus, all queries toggle at most _f+k_ entries, strictly within _E_<sub>0</sub>.

**Theorem 8.6.** _Let G_=(_V,E,**c**_) _be an n-vertex directed graph with integer edge costs in_ \[-_W,W_\]_, query roots_ \(V_Q\subseteq V\) _, and a susceptible set E<sub>Q</sub>, and let_ \(k\ge 1\)_. Let_ \(\sigma=|E_Q|+k|V_Q|\)_. Then there exist the following subset sensitivity oracles that, for any_ \(s\in V_Q\) _and any_ \(U\in E_Q^f\)_, answer queries on G+U with high probability:_

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Global Min-Cut Value_ & \(O(\sigma m^{1+o(1)}+\sigma^3(fn)^{\omega-2}+T_{aug})\) & \(O(\sigma^3)\) & \(\widetilde{O}(f^{\omega+1})\) & \(\mu_{G+U}\) \\
_Global Min-Cut Partition_ & \(O\big((\sigma^3+\sigma n^2)(fn)^{\omega-2}+T_{aug}\big)\) & \(O(\sigma^3+\sigma n^2)\) & \(\widetilde{O}(f^\omega n)\) & _Global min-cut in G+U_ \\
\end{tabular}

