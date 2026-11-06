• If \(\mu_{G+U}(s)<\lambda^*\), then let \(y^*=argmin_{y\in Y,y\neq s}\lambda_{G+U}(s,y)\). We invoke the (_s,y_<sup>∗</sup>) nearest-min-cut oracle on _G+U_, which returns the desired partition in \(\widetilde{O}(f^{3\omega} n)\) time.<tbc>

• If \(\mu_{G+U}(s)=\lambda^*\), then scan all vertices to find a vertex _v_ such that \(\lambda_{G+U}(s,v)=\lambda*\). Then, invoke the (_s,v_) nearest-min-cut oracle on _G+U_. This procedure returns the desired partition in \(\widetilde{O}(f^{3\omega} n)\) time.

So, the total query time for reporting the vertex partition is bounded by \(\widetilde{O}(f^{3\omega} n)\).

\(\square\)

### Global Min-Cut

For the global min-cut, we use the standard symmetry property: for any fixed vertex _s_,

\(\mu_G=min\big(\mu_G(s),\mu_{G^\mathrm{rev}}(s)\big),\)

where _G_<sup>rev</sup> is _G_ with all edges reversed. For any global min-cut (_A,B_), either \(s\in A\) (so \(\mu_G(s)\le|\delta_G(A,B)|\)) or \(s\in B\) (so \(\mu_{G^\mathrm{rev}}(s)\le|\delta_{G^\mathrm{rev}}(A,B)|\)). Hence, a single arbitrary source _s_, chosen at preprocessing, suffices.

**Theorem 4.9.** _Let G_=(_V,E,**c**_) _be an n-vertex directed graph with unit edge capacities and integer edge costs in_ \[-_W,W_\]_. There exist the following sensitivity oracles that, for any update set U of size_ \(\le f\)_, answer queries on G+U with high probability:_

_Proof._ We choose an arbitrary source vertex \(s\in V\) during preprocessing. Note that we compute independent optimal augmentations (and thus distinct _I_<sup>∗</sup> sets) for _G_ and _G_<sup>rev</sup> with respect to _s_. We then instantiate the _s_-min-cut value and partition oracles from Theorem 4.8 for both augmented graphs. The preprocessing time and space match the bounds stated previously. To determine the value of the global min-cut, we query the value oracles on both _G+U_ and (_G+U_)<sup>rev</sup> and return the smaller value, which equals \(\mu_{G+U}\). For a partition query, we first determine whether the minimum is attained in _G+U_ or (_G+U_)<sup>rev</sup>, and then invoke the corresponding partition oracle. The partition-query time remains identical to Theorem 4.8. \(\square\)

## 5 Arborescences, Spanning Trees, Colorful Spanning Trees, Arboricity

### 5.1 Sensitivity Oracles for _k_-Disjoint Arborescences

To design sensitivity oracles for _k_-disjoint arborescences, we first formulate the problem using matroid _k_-packing. Consider a directed graph _H_=(_V<sub>H</sub>,E<sub>H</sub>_) with _N_ vertices and _M_ edges, along with a designated root node _z_. A valid _z_-rooted spanning arborescence in _H_ is a set of _N_-1 edges forming a spanning tree in the underlying undirected graph, where every vertex \(v\in V_H\backslash\{z\}\) has exactly one incoming edge, and _z_ has no incoming edges. We define two linear matroids on the ground set _E<sub>H</sub>_.

**Definition 5.1.** _The matroids M_<sub>graph</sub> _and M_<sub>part</sub> _on the ground set E<sub>H</sub>, both of rank r=N_-1_, are defined with respect to the root z as follows:_

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Global Min-Cut Value_ & \(O(f^\omega n^{\omega+1}+T_{aug})\) & _O(f_<sup>2</sup>_n_<sup>3</sup>log_n_) & \(\widetilde{O}(f^{3\omega+1})\) & \(\mu_{G+U}\) \\
_Global Min-Cut Partition_ & \(O(f^\omega n^{\omega+1}+T_{aug})\) & _O(f_<sup>2</sup>_n_<sup>3</sup>log_n_) & \(\widetilde{O}(f^{3\omega} n)\) & _Global-min-cut in G+U_ \\
\end{tabular}

