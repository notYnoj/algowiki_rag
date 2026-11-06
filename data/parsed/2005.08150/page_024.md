<tbc>**Corollary 4.** _Any edge in the set_ \(\mathtt{b}_\eta\) _is either a u-type static edge or an e-type static edge._

Next, we note a property that forces an edges in the matching \(\eta\).

**Claim 29** _For any_ \(\{i,j\}\subseteq[k]\)_, consider some_ \(e\in E_{ij}\) _such that_ \(e\tilde{e}\in\mathtt{b}_\eta\)_. Then_ \(q_1^{ij}e\in\eta\).

_Proof._ Suppose \(q_1^{ij}e\notin\eta\), then since \(\eta\) is a perfect matching, there exists a vertex \(e'\in V(G')\) such that \(q_1^{ij}e'\in\eta\). Since \(e'\) and \(\tilde{e'}\) prefer each other over any other vertex, \(e'\tilde{e'}\in\mathtt{b}_\eta\). Recall that \(N(q_1^{ij})=\{e'\in V(G'):e'\in E_{ij}\}\). Therefore, \(e'\in E_{ij}\), a contradiction to the uniqueness criteria in Corollary 3. Therefore, \(q_1^{ij}e\in\eta\).

**Claim 30** _Let e=uv,_ \(u\in V_i\) _and_ \(v\in V_j\) _where_ \(\{i,j\}\subseteq[k]\) _and i\<j. If_ \(e\tilde{e}\in\mathtt{b}_\eta\)_, then_ \(\{u_1u_2,v_1v_2\}\subseteq\mathtt{b}_\eta\),

_Proof._ We first show that \(u_1u_2\in\mathtt{b}_\eta\). Recall that the preference list of _u_<sub>3</sub> is \(\langle u_2,[\mathscr{E}_u],u_4\rangle\). If \(\eta(u_3)=u_2\), then since _u_<sub>1</sub> and _u_<sub>2</sub> prefer each other over any other vertex, \(u_1u_2\in\mathtt{b}_\eta\).

Suppose that \(\eta(u_3)=e'\) where \(e'\in\mathscr{E}_u\), then since \(e'\) and \(\tilde{e'}\) prefer each other over any other vertex, \(e'\tilde{e'}\in\mathtt{b}_\eta\). Since \(u_3e'\in\eta\), we get a contradiction to Claim 29. Therefore, \(\eta(u_3)\notin\mathscr{E}_u\). Since \(\eta\) is a perfect matching, \(\eta(u_3)=u_4\). Note that _u_<sub>3</sub> prefers the vertex _e_ over _u_<sub>4</sub>. Since, \(e\tilde{e}\in\mathtt{b}_\eta\), by Claim 29 we have that \(q_1^{ij}e\in\eta\). Note that _e_ also prefers _u_<sub>3</sub> over \(q_1^{ij}\). Therefore, \(u_3e\in\mathtt{b}_\eta\). This contradicts Corollary 4. Similarly, we can show that \(v_1v_2\in\mathtt{b}_\eta\).

Next, we construct two sets _S_ and _E<sub>S</sub>_ as follows. Let \(S=\{u\in V(G):u_1u_2\in\mathtt{b}_\eta,i\in[k]\}\), and \(E_S=\{e\in E(G):e\tilde{e}\in\mathtt{b}_\eta,\{i,j\}\subseteq[k]\}\). We claim that _G<sub>S</sub>_=(_S,E<sub>S</sub>_) is a clique, and \(|S\cap V_i|=1\), where \(i\in[k]\). Let _e=uv_, where \(u\in V_i\), and \(v\in V_j\). Using Claim 30, for each \(e\tilde{e}\in\mathtt{b}_\eta\), \(\{u_1u_2,v_1v_2\}\subseteq\mathtt{b}_\eta\). Hence for each \(uv\in E_S\), \(\{u,v\}\subseteq S\). Using Corollary 3, \(|S\cap V_i|=1\), i.e., |_S_|=_k_, and |_E<sub>S</sub>_|=<sup>_k(k_-1)</sup>/2. Hence, _G<sub>S</sub>_ is a clique. This completes the proof.

## 5 FPT Algorithm for LS-ASM

In this section, we give FPT algorithm for LS-ASM with respect to _q+d_ (Theorem 4). Recall that _d_ is the degree of the graph _G_, and _q_ is the symmetric difference between a solution matching and the given stable matching \(\mu\). Suppose \(\eta\) is a _hypothetical_ solution to \((G,\mathcal{L},\mu,k,q,t)\). Let matchings \(\mu=\mu_1\unknown\mu_2\) and \(\eta=\mu_2\unknown\eta_2\). Observe that we can obtain \(\eta\) from \(\mu\), by deleting \(\mu_2\), and adding the edges in \(\eta_2\). Equivalently, we can find \(\eta\), if we know \(\mu\triangle\eta\), as \(\mu\triangle\eta=\mu_2\unknown\eta_2\). Thus, our goal is reduced to find \(\mu\triangle\eta\). Now, we begin with the description of our algorithm, which has three phases: Vertex Separation, Edge Separation, and Size-Fitting. An example describes the algorithm in Figure 4. We begin with the

