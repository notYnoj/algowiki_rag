<tbc>_Proof._ For the sake of contradiction, suppose that both _u_<sub>1</sub>_u_<sub>2</sub> and _v_<sub>1</sub>_v_<sub>2</sub> are not blocking edges with respect to \(\eta\). Without loss of generality, we may assume that _u_<sub>1</sub>_u_<sub>2</sub> is not a blocking edge. Since _u_<sub>1</sub> and _u_<sub>2</sub> prefer each other over any other vertex, \(u_1u_2\in\eta\), otherwise it will contradict the fact that _u_<sub>1</sub>_u_<sub>2</sub> is not a blocking edge. For any \(h\in[r]\), suppose that \(u_{2h+1}e'\in\eta\), where \(e'=\sigma(E_u,h)\). Since \(e'\) and \(\tilde{e'}\) prefer each other over any other vertex \(e'\tilde{e'}\in\mathsf{B}_\eta\). Since \(u_{2h+1}e'\in\eta\), the edge \(q_{\lceil\ell/2\rceil}^{ij}e'\notin\eta\), where \(\ell=\sigma(E_{ij},e')\), a contradiction to Claim 16. Thus, for any \(h\in[r]\), \(u_{2h+1}e'\notin\eta\), where \(e'=\sigma(E_u,h)\). Since \(u_1u_2\in\eta\) and \(\eta\) is a perfect matching, we can infer that for each \(h\in[r]\), \(u_{2h+1}u_{2h+2}\in\eta\). Since \(e\tilde{e}\in\mathsf{B}_\eta\), due to Claim 16, \(q_{\lceil\ell/2\rceil}^{ij}e\in\eta\), where \(\ell=\sigma(E_{ij},e)\). Note that there exists \(h\in[r]\) such that \(u_{2h+1}e\in E(G')\). Since _u_<sub>2_h_+1</sub> prefers _e_ more than its matched partner in \(\eta\), i.e., _u_<sub>2_h_+2</sub>, and _e_ prefers _u_<sub>2_h_+1</sub> more than its matched partner in \(\eta\), \(u_{2h+1}e\in\mathsf{B}_\eta\), a contradiction to Corollary 2.

Next, we construct two sets _S_ and _E<sub>S</sub>_ as follows. Let \(S=\{u\in V(G):u_1u_2\in\mathsf{B}_\eta\}\), i.e, the set of vertices in _G_ that correspond to a _u_-type static blocking edge. Let \(E_S=\{e\in E(G):e\tilde{e}\in\mathsf{B}_\eta\}\), i.e, the set of edges in _G_ that correspond to a _e_-type static blocking edge.

We claim that _G<sub>S</sub>_=(_S,E<sub>S</sub>_) is a clique, and \(|S\cap V_i|=1\), for each \(i\in[k]\). Using Claim 17, we know that for each edge \(e\in E_S\), we have \(\{u,v\}\subseteq S\), where _u_ and _v_ are the two endpoints of the edge _e_.

Moreover, using Corollary 1, we that \(|V_i\cap S|=1\) for each \(i\in[k]\) and |_E<sub>S</sub>_|=<sup>_k(k_-1)</sup>/2. Hence, we may conclude that _G<sub>S</sub>_ is a clique on _k_ vertices. This completes the proof of the lemma.

Thus, Theorem 1 is proved.

## 4 W\[1\]-hardness of LS-ASM

In this section, we show the parameterized intractability of LS-ASM with respect to several parameters. In particular, we prove Theorem 2 and Theorem 3.

### 4.1 Proof of Theorem 2

We again give a polynomial-time parameter preserving many-to-one reduction from MCQ on regular graphs. Let (_G,k_) be an instance of MCQ. To construct an instance \((G',\mathcal{L},\mu,k',q,t)\) of LS-ASM, we construct a graph \(G'\), a set of L containing the preference list of each vertex of \(G'\), and a stable matching \(\mu\) as defined in the proof of Theorem 1. We set the parameters \(k'\) and _t_ also as in the proof of Theorem 1. We set parameter _q_ as follows:

\(q=(2r+3)k+\frac{3k(k-1)}{2}+4klog_2\left(\frac{n}{2}\right)+2k(k-1)log_2\left(\frac{m}{2}\right)\)

Next, we show that (_G,k_) is a Yes-instance of MCQ if and only if \((G',\langle,\rangle\mu,k',q,t)\) is a Yes-instance of LS-ASM. In the forward direction, let _X_ be a solution of

