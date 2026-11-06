### Bounded Flow Oracle.

The susceptible set _E_<sub>0</sub> is the union of the susceptible graph edges and the potential query edges:

\(E_0=E_Q\cup\bigcup_{s\in V_Q}E_{s^*,s}\cup\bigcup_{t\in V_Q}E_{t,t^*},\)

of size \(\sigma_{flow}=|E_Q|+2k|V_Q|=O(|E_Q|+k|V_Q|)=O(\sigma)\). For a query (_s,t,U_), we binary search over \(\lambda\in[0,k]\). Each candidate modifies at most _f_+2_k_ diagonal entries within _E_<sub>0</sub>. By Theorem 3.7, each determinant evaluation takes \(O((f+k)^\omega)\) time. The binary search yields \(\lambda^*\) in \(O((f+k)^\omega logk)\) time. The stated bounds follow by substituting \(\sigma_{flow}\) into the theorem.

### Nearest Min-Cut Oracle.

We first compute \(\lambda:=\lambda_{G+U}(s,t)\). For each \(w\in V\backslash\{s,t\}\), we query \(\lambda_{G+U+(w,t)}(s,t)\) by adding one further diagonal change. To ensure the edge (_w,t_) lies in the susceptible set for any query pair, we must absorb the edge set \(\{(w,t):w\in V,t\in V_Q\}\) into _E_<sub>0</sub> at preprocessing time. This yields a larger susceptible set of size \(\sigma_{cut}=O(|E_Q|+k|V_Q|+n|V_Q|)=O(\sigma+n|V_Q|)\). Each of the _n_ queries modifies _O(f+k_) entries, yielding a total query time of \(O((f+k)^\omega n)\).

### Min-Cost Flow Oracle.

After computing \(\lambda^*\) via the bounded flow oracle, we invoke the weighted subset sensitivity oracle using the smaller susceptible set \(\sigma_{flow}\). By Theorem 3.7, substituting \(\sigma_{flow}\) yields the required preprocessing and space bounds, with query time scaling by the weight degree \(W\cdot kn\). □

### Implications for Reachability and Distance Sensitivity.

As a direct application of our bounded-flow subset-sensitivity oracles with _k_=1 and integral edge costs (assuming no negative- weight cycles so that distances are well-defined), we obtain subset reachability and distance sensitivity oracles. Setting _k_=1 in Theorem 8.1, the all-pairs bounded-flow decision oracle reduces to the problem of computing reachability and the min-cost oracle reduces to distances after _f_ edge updates.

**Corollary 8.2** (Reachability and Distance Subset Sensitivity Oracle)**.** _Let G_=(_V,E,c_) _be an n- vertex directed graph with integer edge costs in_ \[-_W,W_\] _with designated sets_ \(V_Q\subseteq V\) _and_ \(E_Q\subseteq E\)_, having no negative weight cycles. Let_ \(\sigma=|V_Q|+|E_Q|\)_. Then there exist the following subset sensitivity oracles that, for any query_ \((s,t,U)\in V_Q^2\times E_Q^f\)_, answer queries on G+U with high probability:_

We note that for the general model, the celebrated distance sensitivity oracle of Brand and Saranurak \[vdBS19\] achieves \(\widetilde{O}(Wn^3)\) preprocessing and \(\widetilde{O}(Wnf^\omega)\) query time for _f_ failures using the adjoint oracle on the generic matrix of the graph.

## 8.1.2 (_s,t_)-Max-Flow and (_s,t_)-Min-Cut

Let _G_=(_V,E,c_) be an _n_-vertex directed graph with fixed source _s_, sink _t_, and a susceptible edge set _E<sub>Q</sub>_ (which may include edges not currently in _E_). We set _k_=2_f_. As in Section 4.2, we precompute a min-cost (_s,t_)-max-flow _h_ in _G_, extend it to saturate the first _f_ edges of a set _E<sub>f</sub>_ of 2_f_ zero-cost parallel (_s,t_)-edges, and construct the auxiliary graph \(\mathcal{G}_h^*\) on _N=n_+2 vertices and _m_+2_f_ edges by adding a dummy source _s_<sup>∗</sup> and a dummy sink _t_<sup>∗</sup>.

\begin{tabular}{cccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ \\
_Reachability_ & \(O(\sigma^2n^{\omega-2})\) & \(O(\sigma^2)\) & \(O(f^\omega)\) \\
_Distances_ & \(\widetilde{O}(W\sigma^2n^{\omega-1})\) & \(\widetilde{O}(Wn\sigma^2)\) & \(\widetilde{O}(Wnf^\omega)\) \\
\end{tabular}

