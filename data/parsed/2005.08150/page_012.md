<tbc>For any \(i\in[k]\), \(j\in[\mathrm{log}_2(n/2)]\), and \(\ell\in[\gamma_j]\), vertices that \(b_{j,\ell}^i\) prefers over \(a_{j+1,\ell}^i\) (i.e., \(a_{j,2\ell-1}^i\) and \(a_{j,2\ell}^i\)) are matched to their top preferences respectively, there is no blocking edge incident to \(b_{j,\ell}^i\). By symmetry, there is no blocking edge incident to \(\tilde{b}_{h,\ell}^i\). Analogously, there is also no blocking edge incident to \(d_{h^\prime,\ell^\prime}^{ij}\), or \(\tilde{d}_{h^\prime,\ell^\prime}^{ij}\), for any \(\{i,j\}\subseteq[k],i<j,h'\in[\mathrm{log}_2(m/2)]\), and \(\ell'\in[\tau_h]\).

Hence, we can conclude that \(\mu\) is a stable matching in \(G'\).

Next, we will formally prove the equivalence between the instance of MCQ and the instance of ASM. In particular, we will prove the following lemma.

**Lemma 1.** I=(_G,(V_<sub>1</sub>_,...,V<sub>k</sub>_)) _is a_ Yes_-instance of_ MCQ _if and only if_ \(\mathcal{J}=(G',\mathcal{L},\mu,k',t)\) _is a_ Yes_-instance of_ ASM.

Before giving the proof of Lemma 1, we give a structural property of any matching in \(G'\) which will be used later.

**Claim 3** _Let_ \(\tilde{\eta}\) _be a matching in_ \(G'\) _of size_ \(|\mu|+t\)_. Then,_ \(\tilde{\eta}\) _is a perfect matching in_ \(G'\).

_Proof._ We first count the number of vertices in \(G'\). Note that for each vertex in _G_, we have a path of length 2_r_+2 in \(G'\). Since |_V(G_)|=_nk_, there are (2_r_+2)_nk_ such vertices in \(V(G')\). For each \(i\in[k]\) and \(\ell\in[n/2]\), we added \(p_\ell^i,\tilde{p}_\ell^i\). Hence, we have added _kn_ special vertices to \(V(G')\). Note that there are 2_k(n_-2) vertices in the set \(\{a_{j\ell}^i,\tilde{a}_{j\ell}^i:i\in[k],j\in[\mathrm{log}_2(n/2)],\ell\in[n/2^j]\}\). Additionally, we have _k(n_-2) vertices in the set \(\{b_{j,\ell}^i,\tilde{b}_{j,\ell}^i:i\in[k],j\in[\mathrm{log}_2(n/2)],\ell\in[n/2^{j+1}]\}\).

Now, we count the vertices in \(G'\) that corresponding to edges in _G_. Note that for each edge in _G_, we have two vertices in \(G'\). Since |_E<sub>ij</sub>_|=_m_, where \(\{i,j\}\subseteq[k]\), there are 2_m_(<sup>_k(k_-1)</sup>/2) vertices in the set \(\{e,\tilde{e}:e\in E(G)\}\). There are _m_(<sup>_k(k_-1)</sup>/2) vertices in the set \(\{q_\ell^{ij},\tilde{q}_\ell^{ij}:\{i,j\}\subseteq[k],i<j,\ell\in[m/2]\}\). There are _k(k_-1)(_m_-2) vertices in the set \(\{c_{h,\ell}^{ij},\tilde{c}_{h,\ell}^{ij}:\{i,j\}\subseteq[k],i<j,h\in[\mathrm{log}_2(m/2)],\ell\in[m/2^h]\}\). Similarly, we have <sup>_k(k_-1)(_m_-2)</sup>/2 vertices in the set \(\{d_{h,\ell}^{ij},\tilde{d}_{h,\ell}^{ij}:\{i,j\}\subseteq[k],h\in[\mathrm{log}_2(m/2)],\ell\in[m/2^h]\}\).

\(|V(G')|=2(r+1)kn+2k(2n-3)+mk(k-1)+2k(k-1)(m-3/2)\)

Recall that \(|\mu|=(r+1)kn+^{mk(k-1)/2}+2k(n-2)+k(k-1)(m-2)\) and _t=k_+<sup>_k(k_-1)</sup>/2. Therefore, \(|\tilde{\eta}|=(r+1)kn+^{mk(k-1)/2}+k(2n-3)+k(k-1)(m-3/2)\). Hence, \(\tilde{\eta}\) is a perfect matching in \(G'\).

Now, we are ready to prove Lemma 1.

_Proof (Proof of Lemma 1)._

In the forward direction, let _S_ be a solution of MCQ for I, i.e \(|X\cap V_i|=1\), for each \(i\in[k]\) and _G_\[_X_\] is a clique in _G_.

**Defining a solution matching:** We construct a solution \(\eta\) to J as follows. Initially, we set \(\eta=\mu\). Suppose that \(u=S\cap V_i\), then from \(\eta\) we delete edges \(\{u_{2h-1}u_{2h}:h\in[r+1]\}\); and add edges \(\{u_{2h}u_{2h+1}:h\in[r]\}\).

