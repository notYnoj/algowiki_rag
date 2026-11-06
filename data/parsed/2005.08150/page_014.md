<tbc>to its most preferred neighbor, it follows that there is no blocking edge incident to _u_<sub>2_r_+2</sub>.

**Claim 6** _For any vertex_ \(u\in S\)_, u_<sub>1</sub>_u_<sub>2</sub> _is a blocking edge in_ \(G'\) _with respect to_ \(\eta\)_. Moreover, there is no other blocking edge incident to u_<sub>1</sub> _or u_<sub>2</sub> _in_ \(G'\)

_Proof._ Since vertices _u_<sub>1</sub> and _u_<sub>2</sub> in \(G'\) prefer each other over any other vertex, and the edge _u_<sub>1</sub>_u_<sub>2</sub> is not in \(\eta\), it must be a blocking edge with respect to \(\eta\).

Let \(\ell=\sigma(V_i,u)\), i.e the solution _S_ contains the \(\ell^{th}\) vertex of the set _V<sub>i</sub>_. Then, \(N(u_1)=\langle u_2,p_{\lceil\epsilon/2\rceil}^i\rangle\), and we know that \(u_1p_{\lceil\epsilon/2\rceil}^i\in\eta\). Thus, other than _u_<sub>1</sub>_u_<sub>2</sub>, there is no other blocking edge incident to _u_<sub>1</sub> in \(\eta\). Similarly, since \(N(u_2)=\langle u_1,u_3\rangle\), and \(u_2u_3\in\eta\), it follows that there is no other blocking edge incident to _u_<sub>2</sub>.

**Claim 7** _For any_ \(i\in[k]\) _and_ \(\ell\in[n/2]\)_, there is no blocking edge with respect to_ \(\eta\) _that is incident to vertex_ \(p_\ell^i\) _or_ \(\widetilde{p}_\ell^i\).

_Proof._ Let \(u=V_i(2\ell-1)\) and \(v=V_i(2\ell)\), i.e, _u_ and _v_ denote the \(2\ell-1^{st}\) and \(2\ell^{th}\) elements of _V<sub>i</sub>_, respectively.

Suppose that \(\{u,v\}\cap S=\emptyset\). Then, due to the construction of \(\eta\), we know that _u_<sub>1</sub>_u_<sub>2</sub> and _v_<sub>1</sub>_v_<sub>2</sub> are in \(\eta\). Recall that \(N(p_\ell^i)=\langle u_1,v_1,a_{1\ell}^i\rangle\). Since _u_<sub>1</sub> and _v_<sub>1</sub> are matched to their most preferred neighbor in \(\eta\), namely _u_<sub>2</sub> and _v_<sub>2</sub>, so there is no blocking edge incident to \(p_\ell^i\). Hence, this case is resolved.

Suppose that \(u\in S\). Then, \(p_\ell^iu_1\in\eta\). Since \(p_\ell^i\) prefers _u_<sub>1</sub> over any other vertex, so there is no blocking edge incident to \(p_\ell^i\).

Suppose that \(v\in S\). Then, \(p_\ell^iv_1\in\eta\), by the construction of \(\eta\). Since \(|S\cap V_i|=1\), and \(v\in S\), it follows that \(u\notin S\). Hence, \(u_1u_2\in\eta\), implying that _u_<sub>1</sub> is matched to its most preferred neighbor _u_<sub>2</sub>. Therefore, there is no blocking edge with respect to \(\eta\) that is incident to \(p_\ell^i\). By symmetry, we can argue that there is no blocking edge incident to \(\widetilde{p}_\ell^i\).

**Claim 8** _For any_ \(i\in[k],j\in[\mathrm{log}_2(n/2)]\) _and_ \(\ell\in[\beta_j]\)_, there is no blocking edge with respect to_ \(\eta\) _that is incident to vertex_ \(a_{j,\ell}^i\) _or_ \(\widetilde{a}_{j,\ell}^i\).

_Proof._ We first consider the case when _j_=1. Recall that \(N(a_{1,\ell}^i)=\langle p_\ell^i,b_{1,\ell}^i\rangle\). If \(a_{1,\ell}^ip_\ell^i\in\eta\), then \(a_{1,\ell}^i\) is matched to its most preferred vertex. Thus, there is no blocking edge incident on \(a_{1,\ell}^i\). Suppose that \(a_{1,\ell}^ib_{1,\ell}^i\in\eta\). In this case, by the construction of \(\eta\), either \(p_\ell^iu_1\in\eta\) or \(p_\ell^iv_1\in\eta\), where \(u=V_i(2\ell-1)\) and \(v=V_i(2\ell)\). Note that \(p_\ell^i\) prefers both _u_<sub>1</sub> and _v_<sub>1</sub> over \(a_{1,\ell}^i\). Hence, there is no blocking edge incident to \(a_{1,\ell}^i\). Next, we consider the case when \(j\ge 2\). Recall that \(N(a_{j,\ell}^i)=\langle b_{j-1,\ell}^i,b_{j,\ell}^i\rangle\). If \(a_{j,\ell}^ib_{j-1,\ell}^i\in\eta\), then \(a_{j,\ell}^i\) is matched to its most preferred vertex. Thus, there is no blocking edge incident on \(a_{j\ell}^i\). Suppose that \(a_{j,\ell}^ib_{j,\ell}^i\in\eta\). Since \(a_{j,\ell}^i\) is the last preference of \(b_{j-1,\ell}^i\) (and \(b_{j-1,\ell}^i\) is matched to \(a_{j-1,\ell}^i\) in \(\eta\)), we can conclude that there is no blocking edge incident to \(a_{j,\ell}^i\). Similarly, there is no blocking edge with respect to \(\eta\) that is incident to \(\widetilde{a}_{j,\ell}^i\)

**Claim 9** _For any_ \(i\in[k],j\in[\mathrm{log}_2(n/2)]\)_, and_ \(\ell\in[\gamma_j]\)_, there is no blocking edge with respect to_ \(\eta\) _that is incident to vertex_ \(b_{j\ell}^i\) _or_ \(\widetilde{b}_{j\ell}^i\).

