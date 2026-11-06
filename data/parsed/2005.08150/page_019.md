# On the (Parameterized) Complexity of Almost Stable Marriage

19<tbc>

<tbc>MCQ for (_G,k_). We construct a matching \(\eta\) as defined in the above proof. As proved above, \(|\eta|=|\mu|+t\) and the number of blocking edges with respect to \(\eta\) is \(k'\). Now, we show that \(|\mu\triangle\eta|\le q\). Recall that for each vertex in _X_, we delete _r_+2log<sub>2</sub>(_n/_2)+1 edges from \(\eta\) (which also belongs to \(\mu\)), and add _r_+2log<sub>2</sub>(_n/_2)+2 edges to \(\eta\). Similarly, for each edge in _E(G_\[_X_\]), we delete 2(log<sub>2</sub>_m/_2)+1 edge from \(\eta\) which is also in \(\mu\), and add 2(log<sub>2</sub>_m/_2)+2 edges to \(\eta\). Hence,

\(|\mu\triangle\eta|=(2r+3)k+\frac{3k(k-1)}{2}+4k\mathrm{log}_2\left(\frac{n}{2}\right)+2k(k-1)\mathrm{log}_2\left(\frac{m}{2}\right)\)

This completes the proof in the forward direction. The proof of backward direction is same as the proof of the backward direction of Theorem 1.

### 4.2 Proof of Theorem 3

We again give a polynomial-time parameter preserving many-to-one reduction from MCQ similar to the one in Theorem 1. Here, we do not need graph to be a regular graph.

**Construction.** Given an instance I=(_G,(V_<sub>1</sub>_,...,V<sub>k</sub>_)) of MCQ, we construct an instance \(\mathcal{J}=(G',\mathcal{L},\mu,k',q,t)\) of LS-ASM as follows. For any \(\{i,j\}\subseteq[k]\), such that _i\<j_, we use _E<sub>ij</sub>_ to denote the set of edges between sets _V<sub>i</sub>_ and _V<sub>j</sub>_.

- For each vertex \(v\in V(G)\), we add four vertices in \(G'\), denoted by \(\{u_i:i\in[4]\}\), connected via a path: (_u_<sub>1</sub>_,u_<sub>2</sub>_,u_<sub>3</sub>_,u_<sub>4</sub>) in \(G'\).<tbc>

- For each edge \(e\in E_{ij}\), we add vertices _e_ and \(\tilde{e}\) to \(V(G')\), and the edge \(e\tilde{e}\) to \(E(G')\).<tbc>

- For each \(i\in[k]\), we add two vertices \(p_1^i,p_2^i\), and for each \(\{i,j\}\subseteq[k]\) where _i\<j_, we add two vertices \(q_1^{ij},q_2^{ij}\) to \(V(G')\).<tbc>

**-** For each \(i\in[k]\) and for each vertex \(u\in V_i\), we add two edges \(u_1p_1^i\) and \(u_4p_2^i\) to \(E(G')\). For each \(\{i,j\}\subseteq[k]\), _i\<j_, and for each edge \(e\in E_{ij}\), we add four edges \(q_1^{ij}e,q_2^{ij}\tilde{e},eu_3\), and _ev_<sub>3</sub> to \(E(G')\).

Figure 3 describes the construction of \(G'\). Note that \(V(G')=4|V(G)|+2|E(G)|+2k+k(k-1)\). Recall that in the construction of an instance in the proof of Theorem 1, for each vertex in _V(G_), we added a path of length 2_r_+2, while here we add a path of length 4. Moreover, instead of adding _n_ vertices \(p_\ell^i\) and \(\tilde{p}_\ell^i\), for each \(i\in[k]\), \(\ell\in[n/2]\), we only add two vertices \(p_1^i\) and \(p_2^i\). Similarly, we added only two vertices \(q_1^{ij}\) and \(q_2^{ij}\) instead of adding _m_ such vertices. Furthermore, here we did not add the other special vertices which we added in the previous reduction. This is how we decrease the length of augmenting paths. But, note that degree of vertices \(u_3,p_1^i,p_2^i,q_1^{ij},q_2^{ij}\), where \(u\in V_i\), \(\{i,j\}\subseteq[k]\), _i\<j_, is large.

For any vertex \(u\in V(G)\), we define

\(\mathscr{E}_u=\{e\in V(G'):e\in E(G)\text{and}u\text{is an endpoint of}e\}\)

The preference list of each vertex in \(G'\) is presented in  2.

**Matching** \(\mu\)**:** Let \(\mu=\{u_1u_2,u_3u_4,e\tilde{e}:u\in V(G),e\in E(G)\text{, and}i\in[k]\}\). Clearly, \(\mu\) is a matching. Note that \(|\mu|=2|V(G)|+|E(G)|\).

