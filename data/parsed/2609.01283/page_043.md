For any query \(U=(I,F)\subseteq E_Q\), the auxiliary update set **U**<sup>∗</sup> on \(\mathcal{G}_h^*\) involves edges in _E<sub>Q</sub>_, their counterparts, and auxiliary edges (_s_<sup>∗</sup>_,x_) and (_y,t_<sup>∗</sup>) for endpoints of edges in \(F_h:=\{e\in F:h(e)=1\}\). The susceptible set for the subset sensitivity oracle on \(\mathcal{G}_h^*\) therefore consists of: (i) the edges in _E<sub>Q</sub>_ and their counterparts in G_<sub>h</sub>_, (ii) for each endpoint _x_ or _y_ of an edge in _E<sub>Q</sub>_, the auxiliary edges (_s_<sup>∗</sup>_,x_) and (_y,t_<sup>∗</sup>), and (iii) the _k_ parallel edges for the fixed query pair (_s_<sup>∗</sup>_,t_<sup>∗</sup>). The susceptible set size is

\(\sigma'=O(|E_Q|+k)=O(|E_Q|+f).\)

For a query _U_ with \(|U|\le f\), the auxiliary update **U**<sup>∗</sup> modifies _O(f_) diagonal entries within this susceptible set, and the fixed (_s_<sup>∗</sup>_,t_<sup>∗</sup>) query edges contribute _O(k_)=_O(f_) additional modifications. The total number of modified diagonal entries is _O(f_).

**Theorem 8.3.** _Let G_=(_V,E,**c**_) _be an n-vertex directed graph with integer edge costs in_ \[-_W,W_\]_, with source s, sink t, and susceptible set_ \(E_Q\subseteq E\) _of size_ \(\sigma\)_. Then there exist the following subset sensitivity oracles that, for any_ \(U\in E_Q^f\)_, answer queries on G+U with high probability:_

_Proof._ We set _k_:=2_f_ and instantiate the subset sensitivity oracle of Theorem 3.7 on the partition matroids _M_<sub>out</sub>_,M_<sub>in</sub> associated with the auxiliary graph \(\mathcal{G}_h^*\), with rank _r=n_+1, packing parameter _k=O(f_), and susceptible set of size \(\sigma'=O(|E_Q|+f)\).

The preprocessing bounds follow by first calculating min-cost (_s,t_) max-flow in _G_ using the algorithm of \[CKL<sup>+</sup>23\] and then, substituting _kr=O(fn_) and \(\sigma=\sigma'\) into Theorem 3.7. The space is \(O(\sigma'^2)\) for the decision oracle.

### Max-Flow Oracle.

By Theorem 4.3, \(\lambda_{G+U}(s,t)=\lambda_G(s,t)+f-i\), where _i_ is determined by binary search. For each candidate _i_, the auxiliary update set **U**<sup>∗</sup> together with the fixed (_s_<sup>∗</sup>_,t_<sup>∗</sup>) query edges modifies _O(f_) diagonal entries within the susceptible set. By Theorem 3.7, each determinant evaluation takes \(O(f^\omega)\) time; the binary search yields the answer in \(\widetilde{O}(f^\omega)\) time.

### Nearest Min-Cut Oracle.

We first compute \(\lambda:=\lambda_{G+U}(s,t)\) via the max-flow oracle. For each \(w\in V\backslash\{s,t\}\), we invoke the max-flow oracle on _G+U_+(_w,t_), adding one additional element change. To accommodate the edges (_w,t_) for all \(w\in V\) , the susceptible set in this case grows to size _O_(|_E<sub>Q</sub>_|+_f+n_), whence the space term \(O(\sigma^2+n^2)\). Each of the _n_ queries takes \(\widetilde{O}(f^\omega)\) time by Theorem 2.1, giving \(\widetilde{O}(f^\omega\cdot n)\) total.

### Min-Cost Flow Oracle.

By Theorem 4.4, the minimum cost is determined by the min-cost (_s_<sup>∗</sup>_,t_<sup>∗</sup>)-flow in G<sup>∗</sup>. We invoke the weighted oracle of Theorem 3.7 with _kr=O(fn_) and _O(f_) modified diagonal entries, giving query time \(\widetilde{O}(W\cdot fn\cdot f^\omega)=\widetilde{O}(Wnf^{\omega+1})\). □

## 8.1.3 _s_-Min-Cut and Global Min-Cut

We now leverage the subset framework to obtain space-efficient oracles for _s_-min-cut and global min-cut, provided the updates are confined to \(E_Q\subseteq E\).

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Max-Flow_ & \(O(m^{1+o(1)}+\sigma^2(fn)^{\omega-2})\) & \(O(\sigma^2)\) & \(\widetilde{O}(f^\omega)\) & \(\lambda_{G+U}(s,t)\) \\
_Nearest Min-Cut_ & \(O((\sigma^2+n^2)(fn)^{\omega-2})\) & \(O(\sigma^2+n^2)\) & \(\widetilde{O}(f^\omega n)\) & _NMC_<sub>_G+U_</sub>(_s,t_) \\
_Min-Cost Flow_ & \(\widetilde{O}(m^{1+o(1)}+W\sigma^2(fn)^{\omega-1})\) & \(\widetilde{O}(Wfn\sigma^2)\) & \(\widetilde{O}(Wnf^{\omega+1})\) & _Min-cost max-flow in G+U_ \\
\end{tabular}

