<tbc>We add _A_ to _X_ and \(\tilde{A}\) to _Y_ . Note that there is no edge between the vertices in _A_ (or \(\tilde{A}\)). Since no vertex of _B_(or \(\tilde{B}\)) is adjacent to \(\tilde{A}\)(or _A_), we add _B_ to _Y_ and \(\tilde{B}\) to _X_.

Let \(P=\{p_\ell^i:i\in[k],\ell\in[\beta_1]\}\) and \(\tilde{P}=\{\tilde{p}_\ell^i:i\in[k],\ell\in[\beta_1]\}\). We add _P_ to _Y_ and \(\tilde{P}\) to _X_. We define the following sets of vertices.

\(U_{odd}=\{u_{2h-1}:u\in V_i,i\in[k],h\in[r+1]\}\text{and}\)<br>
\(U_{even}=\{u_{2h}:u\in V_i,i\in[k],h\in[r+1]\}\)

We add _U<sub>odd</sub>_ to _X_ and _U<sub>even</sub>_ to _Y_ . We define the following sets.

\(E_1=\{e:e\in E_{ij},\{i,j\}\subseteq[k]\}\text{and}\)<br>
\(E_2=\{\tilde{e}:e\in E_{ij},\{i,j\}\subseteq[k]\}\)

We add _E_<sub>1</sub> to _Y_ and _E_<sub>2</sub> to _X_.

We next define the following sets.

\(Q=\{q_\ell^{ij}:\{i,j\}\subseteq[k],i<j,\ell\in[\rho_1]\}\text{and}\)<br>
\(\tilde{Q}=\{\tilde{q}_\ell^{ij}:\{i,j\}\subseteq[k],i<j,\ell\in[\rho_1]\}\)

We add _Q_ to _X_ and \(\tilde{Q}\) to _Y_ . Again define the the following two sets.

\(C=\{c_{h,\ell}^{ij}:\{i,j\}\subseteq[k],i<j,h\in[\mathrm{log}_2(m/2)],\ell\in[\rho_h]\}\)<br>
\(\tilde{C}=\{\tilde{c}_{h,\ell}^{ij}:\{i,j\}\subseteq[k],i<j,h\in[\mathrm{log}_2(m/2)],\ell\in[\rho_h]\}\)

We add _C_ to _Y_ and \(\tilde{C}\) to _X_. Finally we define the sets,

\(D=\{d_{h,\ell}^{ij}:\{i,j\}\subseteq[k],i<j,h\in[\mathrm{log}_2(m/2)],\ell\in[\tau_h]\}\)<br>
\(\tilde{D}=\{\tilde{d}_{h,\ell}^{ij}:\{i,j\}\subseteq[k],i<j,h\in[\mathrm{log}_2(m/2)],\ell\in[\tau_h]\}\)

We add _D_ to _X_ and \(\tilde{D}\) to _Y_ . Observe that _X_ and _Y_ are independent sets in \(G'\). Hence, \(G'\) is a bipartite graph. Figure 2 illustrates this bipartition of the graph \(G'\).

This completes the construction of an instance of ASM.

**Correctness:** Since we are interested in a matching which is at least _t_ more than the size of a stable matching, we need to know the size of a stable matching. Towards this, we construct a stable matching \(\mu\) that contains the following set of edge

\(\big(\cup_{u\in V(G)}\{u_{2h-1}u_{2h}\in E(G'):h\in[r+1]\}\big)\bigcup\big(\cup_{e\in E(G)}\{e\tilde{e}\in E(G')\}\big)\) (1)

Additionally, for each \(i\in[k]\) and \(\ell\in[n/2]\), we add \(a_{1,\ell}^ip_\ell^i\) and \(\tilde{a}_{1,\ell}^i\tilde{p}_\ell^i\) to \(\mu\). For each \(i\in[k]\), \(j\in[\mathrm{log}_2(n/2)]\backslash\{1\}\), and \(\ell\in[\beta_j]\), we add \(a_{j,\ell}^ib_{j-1,\ell}^i\) and \(\tilde{a}_{j,\ell}^i\tilde{b}_{j-1,\ell}^i\) to \(\mu\). For each \(\{i,j\}\subseteq[k]\), _i\<j_, and \(\ell\in[m/2]\), we add \(c_{1,\ell}^{ij}a_\ell^{ij}\) and \(\tilde{c}_{1,\ell}^{ij}\tilde{d}_\ell^{ij}\) to \(\mu\). For each \(\{i,j\}\subseteq[k]\), _i\<j_, \(h\in[\mathrm{log}_2(m/2)]\backslash\{1\}\), and \(\ell\in[\rho_h]\), we add \(c_{h,\ell}^{ij}d_{h-1,\ell}^{ij}\) and \(\tilde{c}_{h,\ell}^{ij}\tilde{d}_{(h-1)\ell}^{ij}\) to \(\mu\). This completes the construction of the matching \(\mu\).

