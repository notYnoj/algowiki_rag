<tbc>Then by Theorem 6.28 (K2), we have that

\(f(E_{H_{i,1}}(v,S_1,S_2,S_3))=\)<br>
\((1\pm log^{3l_3+7}(n)t_i^{-\epsilon_1})\sum_{e\in E_{H_i}(v,S_1,S_2,S_3)}f(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u)).\)

Thus

\(f(E_{H_{i+1}}(v,S_1,S_2,S_3))=\)<br>
\(\big(1\pm(max_ep_e^i+1.1log^{3l_3+7}(n)t_i^{-\epsilon_1})\big)\sum_{e\in E_{H_i}(v,S_1,S_2,S_3)}f(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u)),\)

and by Proposition 6.51 and the bound given for \(p_e^i\), the general result follows, and taking _f_=1 yields the result for |_E_<sub>_H<sub>i</sub>_+1</sub>(_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>)|. This completes the proof. □

We complete this section by noting that we only make claims about the error terms in the statement of Lemma 6.52, such as _m<sub>i</sub> giveni_-permissibility of (_H<sub>i</sub>,w<sub>i</sub>_). In particular, to ensure that these are sufficiently small _o_(1) terms, as we require to be the case, we’ll wish to understand \(E_{out}^i\) and \(E_{in}^i\) (among other variables) in terms of _H_<sub>1∗</sub> and _w_<sub>1∗</sub>. This is the content of the next section, from which we shall be able to conclude that Plan 6.34 completes to reach _L_<sup>∗</sup>.

**6.4.2.** (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) **in terms of** (_H_<sub>1∗</sub>_,w_<sub>1∗</sub>)**.** Recall by Lemma 6.23 that we know, assuming Theorem 6.1, that (_H_<sub>1∗</sub>_,w_<sub>1∗</sub>) is 1-permissible. We now suppose that (_H<sub>i</sub>,w<sub>i</sub>_) is _i_-permissible for every \(i\le l\), and obtain bounds for the properties of (_H_<sub>_l_+1</sub>_,w_<sub>_l_+1</sub>) in terms of (_H_<sub>1∗</sub>_,w_<sub>1∗</sub>), and show, subsequently, that (_H_<sub>_l_+1</sub>_,w_<sub>_l_+1</sub>) is (_l_+1)-permissible. Note that all properties remain the same as in (_H_<sub>1∗</sub>_,w_<sub>1∗</sub>) until the vertices and edges relating to such properties become reachable. Once they are reachable, provided that Plan 6.34 does not abort, there are fewer than 40loglog(_n_) iterations of Plan 6.34 before all of these vertices have been covered by the process. Indeed, a vertex or edge containing a vertex in _H<sub>l</sub>[I<sub>t<sub>l</sub></sub>_\\_I_<sub>_t<sub>l</sub>_+1</sub>], where _H<sub>l</sub>_ has depth _j_, is no longer present after iteration _l_ and first became reachable at iteration \(l'\) such that \(l'=k_{j-3}\) (where \(k_{j-1}\ge l>k_j\)). For each \(j\in[c_g]\) let _t_<sup>∗</sup>(_k<sub>j</sub>_):=_i_ such that _t<sub>i</sub>=t<sub>k<sub>j</sub></sub>_. Then note that if _H<sub>l</sub>_ has depth _j_, (so that _t<sub>l</sub>\>k<sub>j</sub>_), we have that _l-t_<sup>∗</sup>(_k_<sub>_j_-3</sub>)_\<a_, where \(k_j=c_\mathrm{vor}^ak_{j-3}\), yielding _l-t_<sup>∗</sup>(_k_<sub>_j_-3</sub>)_\<_40loglog(_n_).

Lemma 6.53. _Suppose that_ (_H<sub>i</sub>,w<sub>i</sub>_) _is i-permissible for every_ \(i\le l\)_, and that H<sub>l</sub> has depth j. Let_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _be an open or closed l-reachable tuple such that_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _is_ (_l_+1)_-valid. Then_

\(w_{l+1}(E_{H_{l+1}}(v,S_1,S_2,S_3))=\)<br>
\(\frac{w_{1*}(E_{H_{1*}}(v,S_1,S_2,S_3))}{w_{1*}(E_{H_{1*}}(v,I_{t_{l+1}}))}\prod_{t^*(k_{j-3})\le i\le l}\big(1\pm 2.1\left(\frac{1.1c_{H_i,v}}{\delta_{H_i,v}}+1.2log^{3l_2+7}(n)t_i^{-\epsilon_1}\right)\big).\)

Proof. Consider an open or closed _l_-reachable tuple that is (_l_+1)-valid. Such a tuple was certainly not reachable before _K_<sub>_j_-3</sub>, and so up until reaching _H_<sub>_t_<sup>∗</sup>(_k_<sub>_j_-3</sub>)</sub>

