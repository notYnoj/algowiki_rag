- For each \(\ell\in[\rho_1]\), we add vertices \(q_\ell^{ij}\) and \(\tilde{q}_\ell^{ij}\) to \(V(G')\).<br>
Moreover, let _e_ and \(e'\) denote the \(2\ell-1^{st}\) and \(2\ell^{th}\) elements of _E<sub>ij</sub>_, respec tively. Then, \(q_\ell^{ij}\) is a neighbor of _e_ and \(e'\); and symmetrically \(\tilde{q}_\ell^{ij}\) is a neighbor of \(\tilde{e}\) and \(\tilde{e'}\) in \(G'\).<tbc>

**-** For each \(h\in[\mathrm{log}_2(m/2)]\), and \(\ell\in[\rho_h]\), we add vertices \(c_{h,\ell}^{ij}\) and \(\tilde{c}_{h\ell}^{ij}\) to \(V(G')\). Moreover, for \(\ell\in[\rho_1]\), \(c_{1,\ell}^{ij}\) is a neighbor of \(q_\ell^{ij}\), and symmetrically \(\tilde{c}_{1,\ell}^{ij}\) is a neighbor of \(\tilde{q}_\ell^{ij}\) in \(G'\).<tbc>

**-** For each \(h\in[\mathrm{log}_2(m/2)]\) and \(\ell\in[\tau_h]\), we add vertices \(d_{h,\ell}^{ij}\) and \(\tilde{d}_{h,\ell}^{ij}\) to \(G'\). Moreover, when \(h\in[\mathrm{log}_2(m/2)-1]\), \(d_{h,\ell}^{ij}\) is a neighbor of \(c_{h,2\ell-1}^{ij}\), \(c_{h,2\ell}^{ij}\), and \(c_{h+1,\ell}^{ij}\); and symmetrically, \(\tilde{d}_{h,\ell}^{ij}\) is a neighbor of \(\tilde{c}_{h,2\ell-1}^{ij}\), \(\tilde{c}_{h,2\ell}^{ij}\), and \(\tilde{c}_{h+1,\ell}^{ij}\) in \(G'\).<br>
For the special case, when _h_=log<sub>2</sub>(_m/_2), \(d_{h,1}^{ij}\) is a neighbor of \(c_{h,1}^{ij}\) and \(c_{h,2}^{ij}\); and symmetrically, \(\tilde{d}_{h,1}^{ij}\) is a neighbor of \(\tilde{c}_{h,1}^{ij}\), \(\tilde{c}_{h,2}^{ij}\) in \(G'\).

Figure 1 illustrates the construction of \(G'\). The preference list of each vertex in \(G'\) is presented in  1.

**Parameter**: We set \(k'=k+k(k-1)/2\), and \(t=k'\).

Clearly, this construction can be carried out in polynomial time. Next, we will prove that the graph \(G'\) is bipartite.

**Claim 1** _Graph_ \(G'\) _is bipartite._

_Proof._ We show that \(G'\) is a bipartite graph by creating a bipartition (_X,Y_) for \(G'\) as follows. We define the following sets.

\(A=\{a_{j,\ell}^i:i\in[k],j\in[\mathrm{log}_2(n/2)],\ell\in[\beta_j]\}\)<br>
\(\tilde{A}=\{\tilde{a}_{j,\ell}^i:i\in[k],j\in[\mathrm{log}_2(n/2)],\ell\in[\beta_j]\}\)

