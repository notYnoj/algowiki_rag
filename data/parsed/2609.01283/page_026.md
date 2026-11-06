<tbc>multigraph \(\mathcal{G}_h^*\) from the residual graph G_<sub>h</sub>_ by adjoining a dummy source _s_<sup>∗</sup> and a dummy sink _t_<sup>∗</sup>, both initially isolated.

Given a query _U_=(_I,F_), let \(F_h:=\{e\in F:h(e)=1\}\) denote the set of deleted edges that carried flow, and for each such _e_=(_x,y_) let _e_<sup>rev</sup>=(_y,x_) denote its residual counterpart in G_<sub>h</sub>_. We define the auxiliary update set \(\mathcal{U}^*=(I^*,F^*)\) on \(\mathcal{G}_h^*\) as

\(\mathcal{U}^*:=\big(\underbrace{I\cup\{(s^*,x),(y,t^*):(x,y)\in F_h\}}_{I^*},\underbrace{(F\backslash F_h)\cup\{e^\mathrm{rev}:e\in F_h\}}_{F^*}\big).\)

That is, _I_<sup>∗</sup> inserts the edges of _I_ together with zero-cost edges incident to the dummy vertices, while _F_<sup>∗</sup> deletes the edges of _F_ that did not carry flow and the residual counterparts of those that did. Let \(\mathcal{G}^*:=\mathcal{G}_h^*+\mathcal{U}^*\); note that |U<sup>∗</sup>|=_O_(|_U_|).

**Lemma 4.4.** _Let U_=(_I,F_) _be a set of updates, and write d_:=|_F<sub>h</sub>|. The flow h in_ G _can be repaired into a valid flow_ \(h'\) _in_ G+_U if and only if the_ (_s_<sup>∗</sup>_,t_<sup>∗</sup>)_-max-flow in_ G<sup>∗</sup> _equals d. Moreover, the minimum cost of any such repaired flow satisfies_

\(c(h')=c_\mathcal{G}(h)+c_{\mathcal{G}^*}(s^*,t^*)-\sum_{e\in F_h}c(e).\)

_Proof._ Each edge \((x,y)\in F_h\) leaves _h_ with one unit of excess at _x_ and one of deficit at _y_; all other vertices remain balanced. Repairing _h_ is therefore equivalent to routing |_F<sub>h</sub>_| edge-disjoint paths in G_<sub>h</sub>_+U<sup>∗</sup> from the excess set \(X:=\{x:(x,y)\in F_h\}\) to the deficit set \(Y:=\{y:(x,y)\in F_h\}\). Since G<sup>∗</sup> adds exactly one zero-cost edge from _s_<sup>∗</sup> into each \(x\in X\) and one from each \(y\in Y\) to _t_<sup>∗</sup>, such a routing exists if and only if all _d_ edges leaving _s_<sup>∗</sup> in G<sup>∗</sup> are saturable, i.e., \(\lambda_{\mathcal{G}^*}(s^*,t^*)=d\).

We now derive the cost relation. Any min-cost (_s_<sup>∗</sup>_,t_<sup>∗</sup>)-flow _h_<sup>∗</sup> in G<sup>∗</sup> is decomposable into _d_ paths \(P_j^*=s^*\rightarrow x_j\unknown y_{\sigma(j)}\rightarrow t^*\), for some permutation \(\sigma\), and a (possibly empty) collection of negative-cost cycles \(C_1,\dots,C_\ell\) (which can appear due to insertions). The edges incident to _s_<sup>∗</sup> and _t_<sup>∗</sup> have zero cost and they cannot lie on any cycle, so \(c_{\mathcal{G}^*}(h^*)\) equals the total cost of the subpaths \(P_j:=P_j^*[x_j,y_{\sigma(j)}](1\le j\le d)\) and cycles \(C_1,\dots,C_\ell\) in G_<sub>h</sub>_. That is,

\(c_{\mathcal{G}^*}(s^*,t^*)=\sum_{j=1}^dc_{\mathcal{G}_h}(P_j)+\sum_{i=1}^\ell c_{\mathcal{G}_h}(C_i).\)

The repaired flow \(h'\) is obtained from _h_ by canceling flow along edges in _F<sub>h</sub>_ and rerouting it through the _P<sub>j</sub>_’s and _C<sub>i</sub>_’s. This removes the |_F<sub>h</sub>_| deleted-edge contributions to **_c_**(_h_) and adds the right-hand side above:

\(c(h')=c_\mathcal{G}(h)-\sum_{e\in F_h}c(e)+\sum_jc_{\mathcal{G}_h}(P_j)+\sum_ic_{\mathcal{G}_h}(C_i),\)

which yields the stated cost identity. \(\square\)

## Oracle Construction

We next provide the oracle construction that applies Theorem 4.2 to \(\mathcal{G}_h^*\).

**Theorem 4.5.** _Let G_=(_V,E,**c**_) _be an n-vertex directed graph with integer edge costs in_ \[-_W,W_\]_, and a designated source s and sink t. Then there exist the following sensitivity oracles that, for any set_ \(U\in E^f\)_, answer queries on G+U with high probability:_

