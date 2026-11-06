<tbc>For each \(i\in[k]\) and each \(u\in V_i\), we have the following preference lists:

\(u_1:\langle u_2,p_1^i\rangle\)<br>
\(u_2:\langle u_1,u_3\rangle\)<br>
\(u_3:\langle u_2,[\mathscr{E}_u],u_4\rangle\)<br>
\(u_4:\langle u_3,p_2^i\rangle\)

For each edge \(e\in E_{ij}\) with endpoints \(u\in V_i\) and \(v\in V_j\) , where \(\{i,j\}\subseteq[k]\), _i\<j_, we have the following preference lists:

\(e:\langle\tilde{e},u_3,v_3,q_1^{ij}\rangle\)<br>
\(\tilde{e}:\langle e,q_2^{ij}\rangle\)

For each \(i\in[k]\) and \(\{i,j\}\subseteq[k]\), _i\<j_, we have the following preference lists for the remaining vertices:

\(p_1^i:\langle[N(p_1^i)]\rangle\)<br>
\(p_2^i:\langle[N(p_2^i)]\rangle\)<br>
\(q_1^{ij}:\langle[N(q_1^{ij})]\rangle\)<br>
\(q_2^{ij}:\langle[N(q_2^{ij})]\rangle\)

** 2.** Preference lists in the constructed instance of W\[1\]-hardness of LS-ASM when parameterized by _k+q+t_. Here, for a set _S_, the symbol \[_S_\] denotes that the vertices in this set are listed in some arbitrarily strict order and the notation \(\langle\cdot,\cdot\rangle\) denotes the order of preference over neighbors.

**Lemma 2.** I=(_G,(V_<sub>1</sub>_,...,V<sub>k</sub>_)) _is a_ Yes_-instance of_ MCQ _if and only if_ \(\mathcal{J}=(G',\mathcal{L},\mu,k',q,t)\) _is a_ Yes_-instance of_ LS-ASM.

_Proof._ In the forward direction, let _X_ be a solution of MCQ for I, i.e., for each \(i\in[k]\), \(|X\cap V_i|=1\), and _G_\[_X_\] is a clique. We construct a solution \(\eta\) to J as follows. Initially, we set \(\eta=\mu\). For each \(i\in[k]\), if \(u\in X\cap V_i\), we delete edges _u_<sub>1</sub>_u_<sub>2</sub> and _u_<sub>3</sub>_u_<sub>4</sub> from \(\eta\), and add edges \(u_1p_1^i,u_2u_3\), and \(u_4p_2^i\) to \(\eta\). Also, for each \(\{i,j\}\subseteq[k]\), _i\<j_, if \(e\in E(G[X])\cap E_{ij}\), then we remove the edge \(e\tilde{e}\) from \(\eta\) and add edges \(eq_1^{ij}\) and \(\tilde{e}q_2^{ij}\) to \(\eta\).

**Claim 20** \(\eta\) _is a matching_

_Proof._ For each \(i\in[k]\) and \(u\in X\cap V_i\), edges \(u_1p_1^i\), _u_<sub>2</sub>_u_<sub>3</sub>, and \(u_4p_2^i\) are in \(\eta\), and no other edge incident to _u_<sub>1</sub>_,u_<sub>2</sub>_,u_<sub>3</sub> or _u_<sub>4</sub> is in \(\eta\). Since for each \(i\in[k]\), \(|X\cap V_i|=1\), there is only one edge incident to each \(p_1^i\) and \(p_2^i\). Similarly, for each \(e\in E(G[X])\), there is only one matching edge incident to _e_ and \(\tilde{e}\), namely \(eq_1^{ij}\) and \(\tilde{e}q_2^{ij}\). Since, the remaining edges of \(\eta\) are the same as in \(\mu\), this implies \(\eta\) is a matching.

**Claim 21** \(|\eta|=|\mu|+t\) _and_ \(|\mu\triangle\eta|=q\)

_Proof._ Note that for each \(u\in X\), we delete two edges from \(\eta\) (which also belongs to \(\mu\)), and add three edges to \(\eta\). Similarly, for an edge \(e\in E(G[X])\), we delete one edge from \(\eta\) which is also in \(\mu\), and add two edges to \(\eta\). Hence, \(|\eta|=|\mu|+k+^{k(k-1)}/2=|\mu|+t\), and \(|\mu\triangle\eta|=5k+^{3k(k-1)}/2=q\).

