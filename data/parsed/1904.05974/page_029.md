## Unpopular Vertices and Edges.

It is easy to check that a max-size popular matching in _G_ leaves _a_<sub>0</sub> and _b_<sub>0</sub> unmatched and matches the remaining _n_-2 vertices. For instance, one could run the max- size popular matching algorithm from \[29\]: it first computes the stable matching \(\cup_i\{(a_i,b_i),(a'_i,b'_i)\}\cup_e\{(s'_e,t'_e),(s''_e,t''_e)\}\), and finally outputs the matching \(\cup_i\{(a_i,b'_i),(a'_i,b_i)\}\cup_e\{(s_e,t'_e),(s'_e,t_e),(s''_e,t''_e)\}\). Thus _a_<sub>0</sub> and _b_<sub>0</sub> are _unpopular_ vertices, i.e., _a_<sub>0</sub> and _b_<sub>0</sub> are left unmatched in all popular matchings, while \(\{s_e,t_e\}_{e\in E_H}\) are _unstable_ vertices, i.e., they are left unmatched in every stable matching. Moreover, for each _i_: all the four vertices of _Z<sub>i</sub>_ are contained in the same connected component of the popular subgraph _G_<sub>0</sub>.

Consider any edge _e_=(_i,j_). Since _a<sub>i</sub>_ prefers _b_<sub>0</sub> to _t<sub>e</sub>_ and similarly, _b<sub>j</sub>_ prefers _a_<sub>0</sub> to _s<sub>e</sub>_, the unpopularity of vertices _a_<sub>0</sub>_,b_<sub>0</sub> implies that no popular matching contains (_a<sub>i</sub>,t<sub>e</sub>_) or (_s<sub>e</sub>,b<sub>j</sub>_). Thus (_a<sub>i</sub>,t<sub>e</sub>_) and (_s<sub>e</sub>,b<sub>j</sub>_) are unpopular edges. So for any \(i\in[n_H]\): every popular matching _M_ in _G_ includes either the pair of edges \((a_i,b_i),(a'_i,b'_i)\) or the pair of edges \((a_i,b'_i),(a'_i,b_i)\) and similarly, for every \(e\in E_H\), every maximum size popular matching contains either the pair of edges \((s_e,t'_e),(s'_e,t_e)\) or the pair of edges \((s_e,t''_e),(s''_e,t_e)\).

Let _M_ be any max-size popular matching in _G_. It matches all vertices in \(A\cup B\) other than _a_<sub>0</sub>_,b_<sub>0</sub>. Let \(\alpha\in\{0,\pm 1\}^n\) be a witness of _M_. Lemma 1 (see Section 3) implies the following two useful properties:

(i) For every \(e\in E_H\): \(\alpha_{s_e}=\alpha_{t_e}=-1\) (because _s<sub>e</sub>_ and _t<sub>e</sub>_ are unstable vertices).<tbc>

(ii) For every \(i\in[n_H]\): either \(\alpha_u=0\) for all \(u\in Z_i\) or \(\alpha_u\in\{\pm 1\}\) for all \(u\in Z_i\).

Let _S<sub>M</sub>_ be the set of indices \(i\subseteq[n_H]\) such that \(\alpha_u=0\) for all \(u\in Z_i\).

**Lemma 9.** _The set S<sub>M</sub> is an independent set in the graph H._

_Proof._ We will show that the set _U<sub>M</sub>_=\[_n<sub>H</sub>_\]\\_S<sub>M</sub>_ is a vertex cover in _H_. Note that _U<sub>M</sub>_ is the set of indices _i_ such that \(\alpha_u\in\{\pm 1\}\) for all \(u\in Z_i\). Consider any edge \(e=(i,j)\in E_H\), let _i\<j_. Since _M_ is a max-size popular matching in _G_, we know from what was discussed above that either the pair \((s_e,t'_e),(s'_e,t_e)\) or the pair \((s_e,t''_e),(s''_e,t_e)\) is in _M_.

- If \((s'_e,t_e)\in M\), then wt_<sub>M</sub>(a<sub>i</sub>,t<sub>e</sub>_)=0 for _t<sub>e</sub>_ prefers _a<sub>i</sub>_ to \(s'_e\) and _a<sub>i</sub>_ prefers both _b<sub>i</sub>_ and \(b'_i\) (its possible partners in _M_) to _t<sub>e</sub>_. Since \(\alpha_{t_e}=-1\) (see property (i) above), \(\alpha_{a_i}=1\) because \(\alpha_{a_i}+\alpha_{t_e}\ge 0\).<tbc>

**-** If \((s_e,t''_e)\in M\), then wt_<sub>M</sub>(s<sub>e</sub>,b<sub>j</sub>_)=0 since _s<sub>e</sub>_ prefers _b<sub>j</sub>_ to \(t''_e\) while _b<sub>j</sub>_ prefers both _a<sub>j</sub>_ and \(a'_j\) (its possible partners in _M_) to _s<sub>e</sub>_. Since \(\alpha_{s_e}=-1\) (see property (i) above), \(\alpha_{b_j}\) has to be 1 so that \(\alpha_{s_e}+\alpha_{b_j}\ge 0\).

Thus, for every edge \((i,j)\in E_H\), at least one of _i,j_ is in _U<sub>M</sub>_, that is, _U<sub>M</sub>_ is a vertex cover of _H_. \(\sqcap\sqcup\)

**Lemma 10.** _Let_ \(S\subseteq[n_H]\) _be an independent set in H. Then there is a max-size popular matching M<sub>S</sub> in G such that_ \(M_S\supseteq\cup_{i\in S}\{(a_i,b_i)\}\).

_Proof._ We will construct a matching _M<sub>S</sub>_ that matches all vertices in _G_ other than _a_<sub>0</sub>_,b_<sub>0</sub> along with a witness \(\alpha\) of _M<sub>S</sub>_’s popularity as follows. For every \(i\in[n_H]\):

- if \(i\in S\) then include edges (_a<sub>i</sub>,b<sub>i</sub>_) and \((a'_i,b'_i)\) in _M<sub>S</sub>_ and set \(\alpha_u=0\) for all \(u\in Z_i\);<tbc>

**-** else include edges \((a_i,b'_i)\) and \((a'_i,b_i)\) in _M<sub>S</sub>_ and set \(\alpha_{a_i}=\alpha_{b_i}=1\) and set \(\alpha_{a_i^\prime}=\alpha_{b_i^\prime}=-1\).

For every \(e=(i,j)\in E_H\), where _i\<j_, we do as follows:

- if \(i\notin S\) then include the edges \((s_e,t'_e),(s'_e,t_e)\), and \((s''_e,t''_e)\) in _M<sub>S</sub>_; set \(\alpha_{s_e}=\alpha_{t_e}=\alpha_{t_{e^\prime}}=-1\) and \(\alpha_{s_e^\prime}=\alpha_{t_e^\prime}=\alpha_{s_e^{\prime\prime}}=1\).<tbc>

**-** else (so \(j\notin S\) since \(i\in S\)) include the edges \((s_e,t''_e),(s'_e,t'_e)\), and \((s''_e,t_e)\) in _M<sub>S</sub>_; set \(\alpha_{s_e}=\alpha_{t_e}=\alpha_{s_e^\prime}=-1\) and \(\alpha_{t_e^\prime}=\alpha_{s_e^{\prime\prime}}=\alpha_{t_e^{\prime\prime}}=1\).<tbc>

