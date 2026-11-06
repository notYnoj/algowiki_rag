_Existence._ During preprocessing, finding the \(\alpha\)-factor of _G_ takes \(O(T_\alpha)\) time \[Ans85, DHZ20\], then constructing _H_ and bounded \(\beta\)-factor oracle on _H_ costs \(O((2n\cdot f)^\omega)=O((nf)^\omega)\) and takes _O_((_fn_)<sup>2</sup>log_n_) space; a query with _O(f_) updates costs \(O(f^\omega\cdot f^{2\omega})\) time.

_Min-cost._ During preprocessing, finding min-cost \(\alpha\)-factor _M_ and then constructing sensitivity oracle on _H_ costs \(\widetilde{O}(W(fn)^3)\) time and takes _O(W(fn_)<sup>3</sup>log_n_) space; a query with _O(f_) updates costs \(\widetilde{O}(Wnf^{3\omega+1})\) time. \(\square\)

## 8 Subset Sensitivity Oracles

### 8.1 Subset Sensitivity for Flows, Cuts, _s_-Min-Cut, and Global Min-Cut

We now lift the flow and cut oracles of Section 4 to the subset model. All reductions, namely the path-packing equivalence (Theorem 4.1), the flow-rerouting lemmas (Theorems 4.3 and 4.4), and the cut characterization (Theorem 4.7), are reused unchanged; we replace only the underlying packing oracle of Theorem 3.5 with its subset counterpart, Theorem 3.7.

#### 8.1.1 All-Pairs _k_-Bounded Flow

Let _G_=(_V,E,c_) be an _n_-vertex directed graph with integer edge costs in \[-_W,W_\] and flow bound \(k\in[1,n]\). We are given a set of _query vertices_ \(V_Q\subseteq V\) from which source-sink pairs are drawn, and a set of _susceptible edges E<sub>Q</sub>_ (which may include edges not currently in _E_) subject to insertions or deletions. Any query (_s,t,U_) satisfies \(s,t\in V_Q\) and \(U\subseteq E_Q\) with \(|U|\le f\).

#### Ground Set and Susceptible Set

We construct the auxiliary graph _G_<sup>∗</sup> on _N=n_+2 vertices with super-source _s_<sup>∗</sup> and super-sink _t_<sup>∗</sup>, and the partition matroids _M_<sub>out</sub>_,M_<sub>in</sub> as in Section 4. To support all-pairs queries from _V<sub>Q</sub>_, we include in the ground set _k_ parallel edges from _s_<sup>∗</sup> to _s_ for each \(s\in V_Q\), and _k_ parallel edges from _t_ to _t_<sup>∗</sup> for each \(t\in V_Q\).

#### Query Reduction

For a query (_s,t,U_) with \(s,t\in V_Q\) and \(U\subseteq E_Q\), we modify the diagonal entries of _D_ corresponding to: the _k_ parallel edges from _s_<sup>∗</sup> to _s_, the _k_ parallel edges from _t_ to _t_<sup>∗</sup>, and the _f_ updates in _U_. The total number of modified diagonal entries is at most _f_+2_k_. By Theorem 4.1, the resulting _k_-packing exists if and only if _G+U_ admits \(\lambda\) edge-disjoint (_s,t_)-paths.

**Theorem 8.1.** _Let G_=(_V,E,c_) _be an n-vertex directed graph with integer edge costs in_ \[-_W,W_\] _with designated sets_ \(V_Q\subseteq V\) _and_ \(E_Q\subseteq E\)_, and let_ \(k\in[1,n]\)_. Let_ \(\sigma:=|E_Q|+k|V_Q|\)_. Then there exist the following subset sensitivity oracles that, for any query_ \((s,t,U)\in V_Q^2\times E_Q^f\)_, answer queries on G+U with high probability:_

_Proof._ We instantiate the subset sensitivity oracles of Theorem 3.7 on the partition matroids _M_<sub>out</sub>_,M_<sub>in</sub> associated with _G_<sup>∗</sup>, with rank _r=N_-1=_n_+1 and packing parameter _k_.

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Bounded Flow_ & \(O((kn)^{\omega-2}\sigma^2)\) & \(O(\sigma^2)\) & \(O((f+k)^\omega logk)\) & \(\lambda^*=min(k,\lambda_{G+U}(s,t))\) \\
_Nearest Min-Cut_ & \(O((kn)^{\omega-2}(\sigma+n|V_Q|)^2)\) & \(O((\sigma+n|V_Q|)^2)\) & \(O((f+k)^\omega n)\) & _NMC_<sub>_G+U_</sub>(_s,t_) _(if_ \(\lambda^*<k\)_)_ \\
_Min-Cost Flow_ & \(\widetilde{O}(W(kn)^{\omega-1}\sigma^2)\) & \(\widetilde{O}(Wkn\sigma^2)\) & \(\widetilde{O}(Wkn(f+k)^\omega)\) & _Min-cost for flow of value_ \(\lambda^*\) \\
\end{tabular}

