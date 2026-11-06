<tbc>_Proof._ We first consider the case when \(j\in[\mathrm{log}_2(n/2)-1]\). Recall that<br>
\(N(b_{j,\ell}^i)=\langle a_{j,2\ell-1}^i,a_{j,2\ell}^i,a_{j+1,\ell}^i\rangle\). If \(b_{j,\ell}^ia_{j,2\ell-1}^i\in\eta\), then \(b_{j,\ell}^i\) is matched to its most preferred vertex. Hence, there is no blocking edge incident on \(b_{j,\ell}^i\). Suppose that \(b_{j,\ell}^ia_{j,2\ell}^i\in\eta\). Note that \(a_{j,2\ell-1}^i\) is the only vertex that \(b_{j,\ell}^i\) prefers over \(a_{j,2\ell}^i\). Since \(b_{j,\ell}^i\) is the last preference of \(a_{j,2\ell-1}^i\), and \(a_{j,2\ell-1}^i\) is saturated in \(\eta\) (Claims 3 and 4 imply that \(\eta\) is a perfect matching), there is no blocking edge incident on \(b_{j,\ell}^i\). If \(b_{j,\ell}^ia_{j+1,\ell}^i\in\eta\), then using the same argument as earlier, there is no blocking edge incident on \(b_{j,\ell}^i\). Now, consider the case when _j_=log<sub>2</sub>(_n/_2). Since \(N(b_{j,1}^i)=\langle a_{j,1}^i,a_{j,2}^i\rangle\), there is no blocking edge incident on \(b_{j,1}^i\) using the same arguments as earlier. Similarly, there is no blocking edge incident on \(\widetilde{b}_{j,\ell}^i\) with respect to \(\eta\).

**Claim 10** _For any_ \(\{i,j\}\subseteq[k],i<j\)_, and_ \(\ell\in[m/2]\)_, there is no blocking edge with respect to_ \(\eta\) _that is incident to vertex_ \(q_\ell^{ij}\) _or_ \(\widetilde{q}_\ell^{ij}\).

_Proof._ The proof is similar to the proof of Claim 7.

**Claim 11** _For any_ \(\{i,j\}\subseteq[k],i<j\), \(h\in[\mathrm{log}_2(m/2)]\) _and_ \(\ell\in[\rho_h]\)_, there is no blocking edge with respect to_ \(\eta\) _that is incident to vertex_ \(c_{h,\ell}^{ij}\) _or_ \(\widetilde{c}_{h,\ell}^{ij}\).

_Proof._ The proof is similar to the proof of Claim 8.

**Claim 12** _For any_ \(\{i,j\}\subseteq[k],i<j,h\in[\mathrm{log}_2(m/2)],\ell\in[\tau_h]\)_, there is no block ing edge with respect to_ \(\eta\) _that is incident to vertex_ \(d_{h,\ell}^{ij}\) _or_ \(\widetilde{d}_{h,\ell}^{ij}\).

_Proof._ The proof is similar to the proof of Claim 9.

**Claim 13** _Let e denote an edge in the clique G_\[_S_\]_. Then, the edge_ \(e\tilde{e}\) _in_ \(G'\) _is a blocking edge with respect to_ \(\eta\)_. Moreover, there is no other blocking edge with respect to_ \(\eta\) _that is incident to vertex e or_ \(\tilde{e}\) _in_ \(G'\).

_Proof._ Since vertices _e_ and \(\tilde{e}\) prefer each other over any other vertex in \(G'\), and the edge \(e\tilde{e}\) is not in \(\eta\), it must be a blocking edge with respect to \(\eta\).

Let _e=uv_, that is vertices \(u\in V_i\) and \(v\in V_j\) are the two endpoints of the edge _e_ in _G_. Suppose that for some \(h,h'\in[r]\), we have \(h=\sigma(E_u,e)\) and \(h'=\sigma(E_v,e)\) i.e, _e_ is the _h<sup>th</sup>_ element of _E<sub>u</sub>_ and the _h<sup>th</sup><sup>th</sup>_ element of _E<sub>v</sub>_.

Recall that \(N_{G^\prime}(e)=\langle\tilde{e},u_{2h+1},v_{2h^\prime+1},q_{\lceil\ell/2\rceil}^{ij}\rangle\), where \(\ell=\sigma(E_{ij},e)\), i.e, _e_ is the \(\ell^{th}\) element in the set _E<sub>ij</sub>_. By the construction of \(\eta\), we know that the edge \(eq_{\lceil\ell/2\rceil}^{ij}\) is in \(\eta\). Moreover, since \(\{u,v\}\subseteq S\), we know that vertices _u_<sub>2_h_+1</sub> and \(v_{2h^\prime+1}\) are matched to their most preferred vertices in \(\eta\). Hence, \(e\tilde{e}\) must be the only blocking edge with respect to \(\eta\) that is incident to _e_. Similarly, we note that since \(N(\tilde{e})=\langle e,\widetilde{q}_{\lceil\ell/2\rceil}^{ij}\rangle\) and edge \(\tilde{e}\widetilde{q}_{\lceil\ell/2\rceil}^{ij}\) is in \(\eta\), the only blocking edge that is incident to the vertex \(\tilde{e}\) is \(e\tilde{e}\). Thus, the claim is proved.

Note that Claims 5 and 6 imply that for each vertex \(u\in S\), there is a unique blocking edge with respect to \(\eta\) (namely _u_<sub>1</sub>_u_<sub>2</sub>); and Claim 13 implies that for each edge _e_ in _G_\[_S_\], there is a unique blocking edge (namely \(e\tilde{e}\) )with respect

