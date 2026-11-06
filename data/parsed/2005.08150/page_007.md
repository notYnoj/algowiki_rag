# On the (Parameterized) Complexity of Almost Stable Marriage

7<tbc>

<tbc>It will be necessary for us to assume that certain sets are ordered. This ordering uniquely defines the _t<sup>th</sup>_ element of the set (for an appropriately defined value of _t_), and thereby enables us to refer to the _t<sup>th</sup>_ element of the set unambiguously. We assume that sets _V<sub>i</sub>_ (for each \(i\in[k]\)) and _E<sub>ij</sub>_ (for each \(\{i,j\}\subseteq[k],i<j\)) have a canonical order, and thus for an appropriately defined value _t_, _V<sub>i</sub>(t_) (_E<sub>ij</sub>(t_)) and \(\sigma(V_i,v)\) (\(\sigma(E_{ij},e)\)) are uniquely defined. For ease of exposition, for any vertex \(v\in V(G')\) we will refer to its set of neighbors, as an ordered set. In such a situation we will denote \(N(v)=\langle\cdot,\cdot\rangle\).

Given an instance I=(_G,(V_<sub>1</sub>_,...,V<sub>k</sub>_)) of MCQ, where _G_ is a regular graph whose degree is denoted by _r_, we will next describe the construction of an instance \(\mathcal{J}=(G',\mathcal{L},k',t)\) of ASM.

**Construction.** We begin by introducing some notations. For any \(\{i,j\}\subseteq[k]\), such that _i\<j_, we use _E<sub>ij</sub>_ to denote the set of edges between sets _V<sub>i</sub>_ and _V<sub>j</sub>_. For each \(i\in[k]\), we may assume that |_V<sub>i</sub>_|=_n_=2_<sup>p</sup>_, and for each \(\{i,j\}\subseteq[k]\), we may assume that \(|E_{ij}|=m=2^{p^\prime}\), for some positive integers _p_ and \(p'\) greater than one.<sup>7</sup>.

For each \(j\in[\mathrm{log}_2(n/2)]\), let \(\beta_j=^n/2^j\), and \(\gamma_j=^n/2^{j+1}\). For each \(j\in[\mathrm{log}_2(m/2)]\), let \(\rho_j=^m/2^j\), and \(\tau_j=^m/2^{j+1}\). Next, we are ready to describe the construction of the graph \(G'\).

**Base vertices:**

- For each vertex \(u\in V(G)\), we have 2_r_+2 vertices in \(G'\), denoted by \(\{u_i:i\in[2r+2]\}\), connected via a path: (_u_<sub>1</sub>_,...,u_<sub>2_r_+2</sub>).<tbc>

- For each edge \(e\in E(G)\), we have vertices _e_ and \(\tilde{e}\) in \(G'\) that are neighbors.<tbc>

**-** For each \(h\in[r]\), _u_<sub>2_h_+1</sub> is a neighbor of the vertex _e_, where \(e=\sigma(E_u,h)\).

**Special vertices.** For each \(i\in[k]\), we define a set of special vertices as follows.

- For each \(\ell\in[\beta_1]\), we add vertices \(p_\ell^i\) and \(\tilde{p}_\ell^i\) to \(V(G')\). Let _u_ and _v_ denote the \(2\ell-1^{st}\) and the \(2\ell^{th}\) vertices in _V<sub>i</sub>_, respectively. Then, the vertex \(p_\ell^i\) is a neighbor of vertices _u_<sub>1</sub> and _v_<sub>1</sub>; and the vertex \(\tilde{p}_\ell^i\) is a neighbor of vertices _u_<sub>2_r_+2</sub> and _v_<sub>2_r_+2</sub> in \(G'\).<tbc>

- For each \(j\in[\mathrm{log}_2(n/2)]\) and \(\ell\in[\beta_j]\), we add vertices \(a_{j,\ell}^i\) and \(\tilde{a}_{j,\ell}^i\) to \(V(G')\). Specifically, for the value _j_=1, we make \(a_{1,\ell}^i\) and \(\tilde{a}_{1,\ell}^i\) a neighbor of \(p_\ell^i\) and \(\tilde{p}_\ell^i\), respectively.<tbc>

**-** For each \(j\in[\mathrm{log}_2(n/2)]\) and \(\ell\in[\gamma_j]\), we add vertices \(b_{j,\ell}^i\) and \(\tilde{b}_{j,\ell}^i\) to \(V(G')\). Moreover, for \(j\in[\mathrm{log}_2(n/2)-1]\), we make \(b_{j,\ell}^i\) a neighbor of \(a_{j,2\ell-1}^i\), \(a_{j,2\ell}^i\), and \(a_{j+1,\ell}^i\). Symmetrically, we make \(\tilde{b}_{j,\ell}^i\) a neighbor of \(\tilde{a}_{j,2\ell-1}^i\), \(\tilde{a}_{j,2\ell}^i\), and \(\tilde{a}_{j+1,\ell}^i\). For the special case, when _j_=log<sub>2</sub>(_n/_2), \(b_{j,1}^i\) is a neighbor of \(a_{j,1}^i\) and \(a_{j,2}^i\); and \(\tilde{b}_{j,1}^i\) is a neighbor of \(\tilde{a}_{j,1}^i\) and \(\tilde{a}_{j,2}^i\).<tbc>

<tbc>For each \(\{i,j\}\subseteq[k]\), where _i\<j_, we do as follows.

<sup>7</sup> Let _p_ be the smallest positive integer greater than one such that _n\<_2_<sup>p</sup>_, add 2_<sup>p</sup>-n_ isolated vertices in _V<sub>i</sub>_. Similarly, let \(p'\) be the smallest positive integer greater than one such that \(m<2^{p^\prime}\), add \(2^{p^\prime}-m\) isolated edges (an edge whose endpoints are of degree exactly one) to _E<sub>ij</sub>_. Note that if (_G,(V_<sub>1</sub>_,...,V<sub>k</sub>_)) was a W\[1\]-hard instance of MCQ earlier, then so even now.

