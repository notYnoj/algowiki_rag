an exact available degree of _f<sub>v</sub>_. Because \(\beta(r_v)=f_v\), the \(\beta\)-factor _F_ must select all incident edges of _r<sub>v</sub>_, including the _f<sub>v</sub>_-del(_v_) surviving parallel edges to _s<sub>v</sub>_. Since _s<sub>v</sub>_ also has a budget of _f<sub>v</sub>_, it is forced to satisfy the remainder of its budget by selecting all del(_v_) newly added (_s<sub>v</sub>,v_<sub>1</sub>) edges.

Let _d(v_) and _p(v_) be the number of Layer 1 and parallel edges _F_ selects at _v_<sub>1</sub>, respectively. The budget at _v_<sub>1</sub> mandates that _d(v_)+del(_v_)+_p(v_)=_f<sub>v</sub>_. At _v_<sub>2</sub>, selecting _a(v_) Layer 2 edges alongside the shared _p(v_) parallel edges yields _a(v_)+_p(v_)=_f<sub>v</sub>_. Subtracting these two equations gives _a(v_)=_d(v_)+del(_v_).

In our projection to \(M'\), the total number of _M_-edges dropped at _v_ sums to _d(v_)+del(_v_) (Layer 1 selections plus explicitly deleted edges). This perfectly balances the _a(v_) edges added from Layer 2. Therefore, \(\mathrm{deg}_{M^\prime}(v)=\mathrm{deg}_M(v)=\alpha(v)\). Furthermore, \(M'\) is a simple graph because base edges partition across the layers, preventing simultaneous addition and dropping of the same edge. Finally, \(M'\subseteq G+U\) since removed edges are explicitly absent from Layer 2, and deleted _M_-edges are forcibly dropped. Thus, \(M'\) is a valid \(\alpha\)-factor.

(\(\Rightarrow\)) Let \(M'\) be the optimal witness of Theorem 7.5, and let _d(v_) denote the number of _non-deleted M_-edges dropped at _v_. By the construction of \(M'\) and the bounds on the symmetric difference, we know that for all \(v\in V\) , \(d(v)+\mathrm{del}(v)\le f_v\).

We construct a \(\beta\)-factor _F_ in _H+U<sub>H</sub>_ by selecting: the surviving Layer 1 edges of \(M\backslash M'\); the Layer 2 edges of \(M'\backslash M\); all incident edges to _r<sub>v</sub>_ and _s<sub>v</sub>_; and exactly _f<sub>v</sub>-d(v_)-del(_v_) parallel edges at each _v_ (which is always valid since \(d(v)+\mathrm{del}(v)\le f_v\)). Every vertex thus meets its exact budget constraint \(\beta\). Since all explicitly deleted _M_-edges correctly reside in \(M\backslash M'\) and are accounted for by the sinks, _F_ is a valid \(\beta\)-factor.

_Cost Analysis._ Only Layer 1 and Layer 2 edges carry non-zero costs. A Layer 2 selection adds +**_c_**(_e_), while a Layer 1 selection contributes -**_c_**(_e_) for _non-deleted_ dropped edges. Hence, the cost of _F_ is:

\(c_H(F)=\sum_{e\in M^\prime\backslash M}c(e)-\sum_{e\in M\backslash M^\prime\text{not deleted}}c(e)=c(M')-c(M)+\sum_{e\in U\cap M,\text{deleted}}c(e).\)

Rearranging this equation directly yields the cost identity in the theorem. Therefore, minimizing **_c_**_<sub>H</sub>(F_) minimizes \(c(M')\). In the unit-cost (existence) setting, all cost labels are discarded, and the exact same structural argument provides the existence equivalence. \(\square\)

Because _H_ restricts degree bounds to \(\beta\le 2f\), the corresponding sensitivity oracle matrix dimension is _N<sub>H</sub>=O(nf_). Furthermore, the update sparsity is tightly bounded at |_U<sub>H</sub>_|=_O(f_). Now, we invoke the _k_-bounded oracle of Section 7.2.1 on _H_, where _k=O(f_). This gives the following.

**Theorem 7.8.** _Let G_=(_V,E,**c**_) _be an undirected graph with integer edge costs in_ \[-_W,W_\] _and arbitrary degree bounds_ \(\alpha\)_. Then there exist the following sensitivity oracles that, for any update set U with f_=|_U|, answer queries on G+U with high probability:_

_Proof._ First, we compute a fixed initial min-cost \(\alpha\)-factor _M_ in the graph _G_. Using this, we construct the auxiliary graph _H_, the function \(\beta\), and instantiate the bounded \(\beta\)-factor oracle of Theorem 7.3.

By Theorem 7.7, a query on _G+U_ is equivalent to the corresponding query on a \(\beta\)-factor of _H+U<sub>H</sub>_, with matching cost. The graph _H_ has 4_n_ vertices, degree bounds \(\beta\le 2f\), and |_U<sub>H</sub>_|=_O(f_), so its sensitivity oracle matrix dimension is _N<sub>H</sub>=O(nf_). We instantiate Theorem 7.3 on _H_ with update size _O(f_).

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Existence_ & \(O((fn)^\omega+T_\alpha)\) & _O_((_fn_)<sup>2</sup>log_n_) & \(O(f^{3\omega})\) & _Whether G+U has an_ \(\alpha\)_-factor_ \\
_Min-Cost_ & \(\widetilde{O}(W(fn)^3)\) & _O(W(fn_)<sup>3</sup>log_n_) & \(\widetilde{O}(Wnf^{3\omega+1})\) & _Weight of a min-cost_ \(\alpha\)_-factor of G+U_ \\
\end{tabular}

