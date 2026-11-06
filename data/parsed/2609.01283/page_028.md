<tbc>_increase in the s-min-cut value of G, i.e.,_ \(I^*=\mathrm{arg}\mathrm{max}_{I\subseteq V\times V|I|=f}\mu_{G+I}(s)\).<sup>2</sup>

Let _I_<sup>∗</sup> be the optimal set of _f_ edges output by Theorem 4.6. We compute this augmentation in polynomial time _T_aug during preprocessing, and we define \(\lambda^*:=\mu_{G+I^*}(s)\) as the maximum possible _s_-min-cut achievable by adding _f_ edges to _G_.

For any general query update set _U_ consisting of at most _f_ insertions and deletions, we cannot guarantee that the insertions in _U_ are a subset of _I_<sup>∗</sup>. However, we can use _I_<sup>∗</sup> to bound the candidate target vertices for the new _s_-min-cut. Let _Y_ be the set of head vertices of the edges in \(I^*\cup U\). Since |_I_<sup>∗</sup>|=_f_ and \(|U|\le f\), we have \(|Y|\le 2f\).

**Lemma 4.7.** _For any update set U of size at most f, let Y be the set of head vertices of edges in_ \(I^*\cup U\)_. Then,_

\(\mu_{G+U}(s)=\mathrm{min}\big(\lambda^*,\mathrm{min}_{y\in Yy\neq s}\lambda_{G+U}(s,y)\big).\)

_Proof._ For the \(\le\) direction, observe that \(\mu_{G+U}(s)\le\lambda_{G+U}(s,y)\) for every \(y\neq s\) by the definition of the _s_-min-cut. Furthermore, because _I_<sup>∗</sup> maximizes the _s_-min-cut value over all possible insertions of _f_ edges, and _U_ adds at most _f_ edges (and potentially deletes others), we have \(\mu_{G+U}(s)\le\mu_{G+I^*}(s)=\lambda^*\).

For the \(\ge\) direction, let (_A,B_) be a minimum _s_-cut in _G+U_. We consider two cases based on whether any edge in \(I^*\cup U\) crosses from _A_ to _B_. If no edge of \(I^*\cup U\) crosses from _A_ to _B_, then no edge added by _I_<sup>∗</sup> crosses the cut, and no edge added or deleted by _U_ crosses the cut. Consequently, the edges crossing from _A_ to _B_ are identical in _G+U_ and _G+I_<sup>∗</sup>. Thus, the capacity of (_A,B_) in _G+U_ equals its capacity in _G+I_<sup>∗</sup>, which is at least \(\mu_{G+I^*}(s)=\lambda^*\).

Otherwise, some edge \(e\in I^*\cup U\) crosses from _A_ to _B_. Let _e_=(_x,y_). Since \(s\in A\) and \(y\in B\), we have \(y\neq s\). Because \(e\in I^*\cup U\), we have \(y\in Y\). The partition (_A,B_) is thus an (_s,y_)-cut in _G+U_, of capacity at least \(\lambda_{G+U}(s,y)\ge\mathrm{min}_{y^\prime\in Y,y^\prime\neq s}\lambda_{G+U}(s,y')\).

Hence \(\mu_{G+U}(s)\ge\mathrm{min}\big(\lambda^*,\mathrm{min}_{y\in Y,y\neq s}\lambda_{G+U}(s,y)\big)\). This completes the proof. □

**Theorem 4.8.** _Let G_=(_V,E,**c**_) _be an n-vertex directed graph, and let_ \(s\in V\)_. Then there exist the following sensitivity oracles that, for any set of edge updates U where_ \(|U|\le f\)_, answer queries on G+U with high probability:_

_Proof._ During preprocessing, we compute the optimal augmenting set _I_<sup>∗</sup> of size _f_ in polynomial time _T_aug and compute \(\lambda^*=\mu_{G+I^*}(s)\) For every vertex \(v\in V\backslash\{s\}\), we instantiate the (_s,t_)-max-flow and nearest-min-cut sensitivity oracles of Theorem 4.5 on _G_ with source _s_ and sink _v_, with a budget of _f_.

Given a query update set _U_, we construct the candidate sink set \(Y=\{y|(x,y)\in I^*\cup U\}\). For each \(y\in Y\) such that \(y\neq s\), we call the (_s,y_) max-flow oracle on _G+U_ to compute \(\lambda_{G+U}(s,y)\). Each of the at most 2_f_ valid queries takes \(\widetilde{O}(f^{3\omega})\) time. By Theorem 4.7, \(\mu_{G+U}(s)=\mathrm{min}\big(\lambda^*,\mathrm{min}_{y\in Y,y\neq s}\lambda_{G+U}(s,y)\big)\). Evaluating these bounds takes total time \(\widetilde{O}(f^{3\omega+1})\).

To report a corresponding vertex partition, we first compute \(\mu_{G+U}(s)\). We form two cases, which are handled separately:

<sup>2</sup>Although the theorem gives a characterization for the existence of such augmentation, the polynomial time algorithm can be inferred straightforwardly from the proof. The algorithm finds the minimum number of edges needed to increase the cut by \(\gamma\); we can binary search for finding _I_<sup>∗</sup>.

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_s-Min-Cut Value_ & \(O(f^\omega n^{\omega+1}+T_{aug})\) & _O(f_<sup>2</sup>_n_<sup>3</sup>log_n_) & \(\widetilde{O}(f^{3\omega+1})\) & \(\mu_{G+U}(s)\) \\
_s-Min-Cut Partition_ & \(O(f^\omega n^{\omega+1}+T_{aug})\) & _O(f_<sup>2</sup>_n_<sup>3</sup>log_n_) & \(\widetilde{O}(f^{3\omega} n)\) & _s-min-cut in G+U_ \\
\end{tabular}

