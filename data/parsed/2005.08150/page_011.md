<tbc>**Claim 2** _Matching_ \(\mu\) _has size_ \(kn(r+1)+^{mk(k-1)/2}+2k(n-2)+k(k-1)(m-2)\)_. Furthermore,_ \(\mu\) _is a stable matching in_ \(G'\).

_Proof._ Due to Equation (I), we know that \(\mu\) contains at least _kn(r_+1)+<sup>_mk(k_-1)/2</sup> edges because |_V<sub>i</sub>_|=_n_ for each \(i\in[k]\) and |_E<sub>ij</sub>_|=_m_ for each \(\{i,j\}\subseteq[k]\). The other edges added to \(\mu\) can be counted separately, leading to the following relation.

\(|\mu|=kn(r+1)+^{mk(k-1)/2}+kn+k(n-4)+(^{mk(k-1)/2})+(m-4)(^{k(k-1)/2})\)<br>
\(=kn(r+1)+^{mk(k-1)/2}+2k(n-2)+k(k-1)(m-2)\)

Next, to show that \(\mu\) is a stable matching in \(G'\), we will exhaustively argue for each vertex in \(G'\) that there is no blocking edge incident to it.

We begin by noting that for any vertex \(u\in V(G)\), vertices _u_<sub>1</sub> and _u_<sub>2</sub> in \(G'\) prefer each other over any other vertex in \(G'\). Therefore, edge _u_<sub>1</sub>_u_<sub>2</sub> is a static edge and must belong to every stable matching in \(G'\). Similarly, for any \(e\in E(G)\), we note that \(e\tilde{e}\) is a static edge in \(G'\), and thus belongs to every stable matching in \(G'\). For any \(u\in V(G)\) and \(h\in[r]\), we know that vertex _u_<sub>2_h_+1</sub> is the first preference of _u_<sub>2_h_+2</sub>. Thus, there cannot exist a blocking edge incident to _u_<sub>2_h_+2</sub>, where \(h\in[r]\). Moreover, for any \(h\in[r]\), the vertices that _u_<sub>2_h_+1</sub> prefers over _u_<sub>2_h_+2</sub> are matched to their top preferences. Consequently, there cannot be a blocking edge incident to _u_<sub>2_h_+1</sub>.

Since for each \(u\in V_i\), \(i\in[k]\), vertices _u_<sub>1</sub> and _u_<sub>2_r_+2</sub> are matched to their top preferences respectively, thus for any \(\ell\in[n/2]\) the edges \(u_1p_\ell^i\) and \(u_{2r+2}\tilde{p}_\ell^i\) cannot be a blocking edge with respect to \(\mu\). Thus, there is no blocking edge incident to \(p_\ell^i\) and \(\tilde{p}_\ell^i\), for \(\ell\in[n/2]\). Analogously, we can argue that there is no blocking edge incident on \(q_h^{ij}\) and \(\tilde{q}_h^{ij}\), for any \(\{i,j\}\subseteq[k]\), _i\<j_ and \(h\in[m/2]\).

Since for each \(i\in[k]\), \(j\in[\mathrm{log}_2(n/2)]\), and \(\ell\in[\beta_j]\), vertices \(a_{j,\ell}^i\) and \(\tilde{a}_{j,\ell}^i\) are matched to their top preferences respectively, there is no blocking edge incident to \(a_{j,\ell}^i\) or \(\tilde{a}_{j,\ell}^i\). Analogously, there is no blocking edge incident on \(c_{h,\ell}^{ij}\) or \(\tilde{c}_{h,\ell}^{ij}\), for any \(\{i,j\}\subseteq[k],i<j,h\in[\mathrm{log}_2(m/2)]\), and \(\ell\in[\rho_h]\).

X
Y
A
A
B
B
P
P
Uodd
Ueven
E2
E1
Q
Q
C
C
D
D

**Fig.2.** A bipartition of the graph \(G'\), constructed in the W\[1\]-hardness of ASM.

