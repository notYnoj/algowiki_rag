<tbc>**Claim 26** _For each_ \(\{i,j\}\subseteq[k],i<j\)_, there is no blocking edge incident to_ \(q_1^{ij}\) _or_ \(q_2^{ij}\) _with respect to_ \(\eta\).

_Proof._ Let \(e_1\in E(G[X])\cap E_{ij}\). Hence, by the construction of \(\eta\), \(e_1q_1^{ij},\tilde{e}_1q_2^{ij}\in\eta\). Let \(e_2\in E_{ij}\backslash\{e_1\}\). Since \(|E(G[X])\cap E_{ij}|=1\), _e_<sub>2</sub> does not belong to _E(G_\[_X_\]). Therefore, by the construction of \(\eta\), \(e_2\tilde{e}_2\in\eta\). Since _e_<sub>2</sub> and \(\tilde{e}_2\) prefer each other over any other vertex, there is no blocking edge incident to _e_<sub>2</sub> or \(\tilde{e}_2\). Hence, \(e_2q_1^{ij}\) and \(\tilde{e}_1q_2^{ij}\) are not blocking edges. Since \(N(q_1^{ij})=\{e\in V(G'):e\in E_{ij}\}\), and \(N(q_2^{ij})=\{\tilde{e}\in V(G'):e\in E_{ij}\}\), there is no blocking edge incident to \(q_1^{ij}\) or \(q_2^{ij}\).

Hence, for each \(e\in E(G[X])\), we introduce one blocking edge \(e\tilde{e}\) with respect to \(\eta\). That is, we introduce <sup>_k(k_-1)</sup>/2 blocking edges. Using Claims 22 to 26, there are _k_+<sup>_k(k_-1)</sup>/2 blocking edges for \(\eta\). This completes the proof in the forward direction.

In the reverse direction, let \(\eta\) be a matching of size at least \(|\mu|+t\) such that \(|\mu\triangle\eta|\le 5k+3k(k-1)/2\), and \(\eta\) has at most \(k'\) blocking edges. Recall that \(|V(G')|=4|V(G)|+2|E(G)|+2k+k(k-1)\), \(\mu=2|V(G)|+|E(G)|\), and _t=k_+<sup>_k(k_-1)</sup>/2. Hence, \(\eta\) is a perfect matching in \(G'\).

Note that, similar to Theorem 1, in our instance, the static edges in \(G'\) are of the following type: For any \(u\in V(G)\), edge _u_<sub>1</sub>_u_<sub>2</sub> in \(G'\) is a static edge and is called the _u_-type static edge; for any \(e\in E(G)\), edge \(e\tilde{e}\) in \(G'\) is a static edge and is called the _e_-type static edge.

Let \(\mathtt{B}_\eta\) be the set of blocking edges with respect to \(\eta\). Let us note the following properties of the set \(\mathtt{B}_\eta\). Specifically we show that an edge in \(\mathtt{B}_\eta\) is either a _u_-type static edge or an _e_-type static edge. In fact, for each \(i\in[k]\), there is a unique _u_-type static edge which is a blocking edge, and for each \(\{i,j\}\subseteq[k]\), there is a unique _e_-type static edge in \(\mathtt{B}_\eta\).

**Claim 27 (_u_-type static edge)** _For each_ \(i\in[k]\)_, there exists a vertex_ \(u\in V_i\) _such that the edge_ \(u_1u_2\in\mathtt{B}_\eta\).

_Proof._ Since \(\eta\) is a perfect matching, \(p_1^i\) is saturated by \(\eta\), for each \(i\in[k]\). Since \(N(p_1^i)=\{u_1:u\in V_i\}\), we have that \(p_1^iu_1\in\eta\), for some \(u\in V_i\). Since _u_<sub>1</sub> and _u_<sub>2</sub> prefer each other over any other vertex, it follows that \(u_1u_2\in\mathtt{B}_\eta\).

**Claim 28 (_e_-type static edge)** _For each_ \(\{i,j\}\subseteq[k]\)_, there exists an edge_ \(e\in E_{ij}\) _such that the edge_ \(e\tilde{e}\in\mathtt{B}_\eta\).

_Proof._ Since \(\eta\) is a perfect matching, \(q_1^{ij}\) is saturated by \(\eta\), for each \(\{i,j\}\subseteq[k]\), where _i\<j_. Since \(N(q_1^{ij})=\{e\in V(G'):e\in E_{ij}\}\), \(eq_1^{ij}\in\eta\), for some \(e\in V(G')\). Since _e_ and \(\tilde{e}\) prefer each other over any other vertex, it follows that \(e\tilde{e}\in\mathtt{B}_\eta\).

Using Claims 27 and 28, and the fact that \(|\mathtt{B}_\eta|=k+k(k-1)/2\), we have following two properties of \(\mathtt{B}_\eta\).

**Corollary 3.** _For each_ \(i\in[k]\)_, there exists a unique vertex_ \(u\in V_i\) _such that the edge_ \(u_1u_2\in\mathtt{B}_\eta\)_; and for each_ \(\{i,j\}\subseteq[k]\) _where i\<j, there exists a unique edge_ \(e\in E_{ij}\) _such that the edge_ \(e\tilde{e}\in\mathtt{B}_\eta\).

