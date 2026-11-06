Recall the two ingredients from Section 4.3. First, using Theorem 4.6, we precompute in time _T_aug an optimal _f_-edge augmenting set _I_<sup>∗</sup> that maximizes the _s_-min-cut, and set \(\lambda^*:=\mu_{G+I^*}(s)\). Second, by Theorem 4.7, for any update set _U_ with \(|U|\le f\),

\(\mu_{G+U}(s)=\mathrm{min}\big(\lambda^*,\mathrm{min}_{y\in Yy\neq s}\lambda_{G+U}(s,y)\big),Y:=\{y:(x,y)\in I^*\cup U\},|Y|\le 2f.\)

The candidate targets therefore lie in \(V(E_Q)\cup V(I^*)\), where _V(E<sub>Q</sub>_) is the set of endpoints of the edges in _E<sub>Q</sub>_ and _V(I_<sup>∗</sup>) is the set of (at most _f_) endpoints of the augmenting edges. Both _V(E<sub>Q</sub>_) and _V(I_<sup>∗</sup>) are known before any query, so we pre-initialize one subset (_s,y_)-max-flow oracle for every \(y\in V(E_Q)\cup V(I^*)\). Since \(|V(E_Q)|\le 2\sigma\) and \(|V(I^*)|\le f\le\sigma\), this amounts to \(O(\sigma)\) oracles, each of which is exactly the subset (_s,y_) oracle of Theorem 8.3.

**Theorem 8.4.** _Let G_=(_V,E,**c**_) _be an n-vertex directed graph with a fixed source s and a susceptible set_ \(E_Q\subseteq E\) _of size_ \(\sigma\)_. Then there exist the following subset sensitivity oracles that, for any update set_ \(U\in E_Q^f\) _consisting of insertions and deletions, answer queries on G+U with high probability:_

_Proof._ During preprocessing we compute in _T_aug time the optimal augmenting set _I_<sup>∗</sup> of size _f_ using Theorem 4.6, together with \(\lambda^*=\mu_{G+I^*}(s)\). Also, find a minimum-cut partition (_A_<sub>0</sub>_,V_\\_A_<sub>0</sub>) of _G_ subject to the constraint that \((\{s\}\cup V(E_Q))\subseteq A_0\).

For every target \(y\in(V(E_Q)\cup V(I^*))\backslash\{s\}\) we instantiate the subset sensitivity max-flow and nearest-min-cut oracles of Theorem 8.3 on _G_, with source _s_, sink _y_, and susceptible set _E<sub>Q</sub>_. There are \(O(\sigma)\) such targets. For each target, the max-flow oracle uses a susceptible set of size \(O(|E_Q|+f)=O(\sigma)\) and hence \(O(\sigma^2)\) space, while the nearest-min-cut oracle uses a susceptible set of size \(O(|E_Q|+f+n)=O(\sigma+n)\) (to accommodate the auxiliary edges (_w,y_)) and hence \(O(\sigma^2+n^2)\) space. Summing over the \(O(\sigma)\) targets gives space \(O(\sigma^3)\) for the value oracle and \(O(\sigma^3+\sigma n^2)\) for the partition oracle; the preprocessing times are the corresponding \((fn)^{\omega-2}\)-scaled bounds of Theorem 8.3, plus an additive _T_aug term.

Given a query \(U\in E_Q^f\), we form the candidate sink set \(Y=\{y:(x,y)\in I^*\cup U\}\), with \(|Y|\le 2f\) and \(Y\subseteq V(E_Q)\cup V(I^*)\). For each \(y\in Y\) with \(y\neq s\) we call the (_s,y_) subset max-flow oracle on _G+U_, computing \(\lambda_{G+U}(s,y)\) in \(\widetilde{O}(f^\omega)\) time; over the \(\le 2f\) targets this takes \(\widetilde{O}(f^{\omega+1})\) time. By Theorem 4.7,

\(\mu_{G+U}(s)=\mathrm{min}\big(\lambda^*,\mathrm{min}_{y\in Y,y\neq s}\lambda_{G+U}(s,y)\big).\)

For the partition query, we consider two cases:

• If \(\mu_{G+U}(s)<\lambda^*\), we set \(y^*=\mathrm{argmin}_{y\in Y,y\neq s}\lambda_{G+U}(s,y)\) and invoke the (_s,y_<sup>∗</sup>) subset nearest- min-cut oracle on _G+U_, which returns the partition in \(\widetilde{O}(f^\omega n)\) time.<tbc>

• If \(\mu_{G+U}(s)=\lambda^*\), we query for all vertices \(v\in V(E_Q)\) if \(\lambda_{G+U}(s,v)=\lambda^*\).<tbc>

<tbc>If there exists such a vertex _v_, then invoking the (_s,v_) subset nearest-min-cut oracle on _G+U_ returns the desired partition in \(\widetilde{O}(f^\omega n)\) time.<tbc>

<tbc>If no such \(v\in V(E_Q)\) exists, then all vertices of _V(E<sub>Q</sub>_) lie on the source side of the _s_-min-cut in _G+U_. Since updates to edges in _E<sub>Q</sub>_ do not affect the value of such cuts, we obtain that the cut (_A_<sub>0</sub>_,V_\\_A_<sub>0</sub>) is the desired min-cut vertex partition.

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_s-Min-Cut Value_ & \(O(\sigma m^{1+o(1)}+\sigma^3(fn)^{\omega-2}+T_{aug})\) & \(O(\sigma^3)\) & \(\widetilde{O}(f^{\omega+1})\) & \(\mu_{G+U}(s)\) \\
_s-Min-Cut Partition_ & \(O\big((\sigma^3+\sigma n^2)(fn)^{\omega-2}+T_{aug}\big)\) & \(O(\sigma^3+\sigma n^2)\) & \(\widetilde{O}(f^\omega n)\) & _s-min-cut in G+U_ \\
\end{tabular}

