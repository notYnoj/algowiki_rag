<tbc>On the (Parameterized) Complexity of Almost Stable Marriage17<tbc>

<tbc>Now, since \(\eta\) is a perfect matching, and \(N(d_{h-1,z}^{ij})=\langle c_{h-1,2z-1}^{ij},c_{h-1,2z}^{ij},c_{h,z}^{ij}\rangle\), either \(d_{h-1,z}^{ij}c_{h-1,2z-1}^{ij}\in\eta\) or \(d_{h-1,z}^{ij}c_{h-1,2z}^{ij}\in\eta\). We view the index _h_ as indicating a level, the highest being log<sub>2</sub>(_m/_2). As we go down each level starting from the highest, we obtain a matching edge in \(\eta\). The lowest level is reached when for some value \(h'\in[m/4]\), we reach the vertex \(d_{1,h^\prime}^{ij}\). For this vertex, there are two pos sible matching partners in \(\eta\): \(c_{1,2h^\prime-1}^{ij}\) or \(c_{1,2h^\prime}^{ij}\). Thus, for some \(\bar{h}\in\{2h'-1,2h'\}\), edge \(d_{1,h^\prime}^{ij}c_{1,\bar{h}}^{ij}\in\eta\).

Since \(\eta\) is a perfect matching, \(q_\bar{h}^{ij}\) is matched to either _e_ or \(e'\) in \(\eta\), where \(e=E_{ij}(2\bar{h}-1)\) and \(e'=E_{ij}(2\bar{h})\), i.e, _e_ is the 2\(\bar{h}-1^{st}\) element of _E<sub>ij</sub>_ and \(e'\) is the 2\(\bar{h}^{th}\) element of _E<sub>ij</sub>_. If \(q_\bar{h}^{ij}e\in\eta\), then since _e_ and \(\tilde{e}\) are each others first preference, edge \(e\tilde{e}\in\mathtt{B}_\eta\). Else if \(q_\bar{h}^{ij}e'\in\eta\), then with analogous argument, it follows that \(e'\tilde{e'}\in\mathtt{B}_\eta\). Hence, the result is proved.

**Corollary 1.** _For each_ \(i\in[k]\)_, there exists a unique_ \(u\in V_i\)_, such that the edge u_<sub>1</sub>_u_<sub>2</sub> _is a blocking edge with respect to_ \(\eta\)_; and for each_ \(\{i,j\}\subseteq[k]\)_, there exists a unique_ \(e\in E_{ij}\)_, such that_ \(e\tilde{e}\) _is a blocking edge with respect to_ \(\eta\).

_Proof._ Using Claims 14 and 15, we know that there are at least _k_+<sup>_k(k_-1)</sup>/<sub>2</sub> blocking edges with respect to \(\eta\). Since \(k'=k+^{k(k-1)}/2\), the uniqueness condition follows.

Conversely, we can also argue the following.

**Corollary 2.** _Any blocking edge with respect to_ \(\eta\) _is either a u-type static edge or an e-type static edge._

_Proof._ Using Corollary 1, we know that there are at least _k_ u-type blocking edges and <sup>_k(k_-1)</sup>/<sub>2</sub>_e_-type blocking edges with respect to \(\eta\). Since \(k'=k+^{k(k-1)}/2\), there cannot exist any other (besides _u_-type and _e_-type) blocking edge with respect to \(\eta\).

Next, we prove that the _e_-type (static) blocking edges force certain edges to be in the matching \(\eta\).

**Claim 16** _For any_ \(\{i,j\}\subseteq[k]\)_, consider some_ \(e\in E_{ij}\) _such that_ \(e\tilde{e}\) _is a blocking edge with respect to_ \(\eta\)_. Then, for the value_ \(\ell=\sigma(E_{ij},e)\)_, the edge_ \(q_{\lceil\ell/2\rceil}^{ij}e\) _is in_ \(\eta\).

_Proof._ By Claim 15, there exists an edge \(e'\in E_{ij}\) such that \(e'\tilde{e'}\) is a blocking edge with respect to \(\eta\) and \(q_{\lceil\ell^\prime/2\rceil}^{ij}e'\) is in \(\eta\), where \(\ell'=\sigma(E_{ij},e')\). By Corollary 1, we know that \(e'=e\).

**Claim 17 (consistency between u-type static edge and e-type static edge)** _Suppose that for some_ \(\{i,j\}\subseteq[k],i<j\)_, we have_ \(e\in E_{ij}\) _such that_ \(e\tilde{e}\) _is a blocking edge with respect to_ \(\eta\)_. Let u and v denote the two endpoints of the edge e in G. Then, both u_<sub>1</sub>_u_<sub>2</sub> _and v_<sub>1</sub>_v_<sub>2</sub> _are blocking edges with respect to_ \(\eta\).

