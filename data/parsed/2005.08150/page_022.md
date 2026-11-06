<tbc>Next, we prove that \(\eta\) has \(k'=k+k(k-1)/2\) blocking edges. Due to Proposition 1, to count the blocking edges with respect to \(\eta\), we only investigate the vertices of \(V(\mu\triangle\eta)\). Note that

\(V(\mu\triangle\eta)=\{u_j,p_\ell^i\in V(G'):u\in X\cap V_i,j\in[4],\ell\in[2],i\in[k]\}\)<br>
\(\bigcup\{e,\tilde{e},q_\ell^{ij}\in V(G'):e\in E(G[X]),\{i,j\}\subseteq[k],i<j,\ell\in[2]\}\)

**Claim 22** _Let_ \(u\in X\)_. There is no blocking edge incident to u_<sub>3</sub> _or u_<sub>4</sub> _with respect to_ \(\eta\).

_Proof._ Since \(u_2u_3\in\eta\), and _u_<sub>3</sub> prefers _u_<sub>2</sub> over any other vertex, there is no blocking edge incident to _u_<sub>3</sub>. Let \(u\in V_i\), for some \(i\in[k]\). Recall that the preference list of _u_<sub>4</sub> is \(\langle u_3,p_2^i\rangle\). Since there is no blocking edge incident to _u_<sub>3</sub> and \(u_4p_2^i\in\eta\), it follows that there is no blocking edge incident to _u_<sub>4</sub>.

**Claim 23** _Let_ \(u\in X\)_. Then, u_<sub>1</sub>_u_<sub>2</sub> _is a blocking edge with respect to_ \(\eta\)_. Moreover, there is no other blocking edge incident to u_<sub>1</sub> _or u_<sub>2</sub>.

_Proof._ Since _u_<sub>1</sub> and _u_<sub>2</sub> prefer each other over any other vertex and \(u_1u_2\notin\eta\), it is a blocking edge with respect to \(\eta\). Let \(u\in V_i\), for some \(i\in[k]\). Since the preference list of _u_<sub>1</sub> is \(\langle u_2,p_1^i\rangle\) and \(u_1p_1^i\in\eta\), there is no other blocking edge incident to _u_<sub>1</sub>. Similarly, since the preference list of _u_<sub>2</sub> is \(\langle u_1,u_3\rangle\) and \(u_2u_3\in\eta\), it follows that there is no other blocking edge incident to _u_<sub>2</sub>.

Using Claims 22 and 23, for each \(i\in[k]\) and \(u\in X\cap V_i\), we introduce exactly one blocking edge with respect to \(\eta\) by deleting _u_<sub>1</sub>_u_<sub>2</sub> and _u_<sub>3</sub>_u_<sub>4</sub> from \(\eta\), and adding edges \(u_1p_1^i,u_2u_3\), and \(u_4p_2^i\) to it. Since |_X_|=_k_, in total we introduce _k_ blocking edges with respect to \(\eta\) due to the said alternation.

**Claim 24** _For each_ \(i\in[k]\)_, there is no blocking edge incident to_ \(p_1^i\) _or_ \(p_2^i\) _with respect to_ \(\eta\).

_Proof._ Let \(u\in X\cap V_i\). Then, by the construction of \(\eta\), \(u_4p_2^i\in\eta\). Let \(v\in V_i\backslash\{u\}\). Since \(|X\cap V_i|=1\), \(v\notin X\). Hence, \(v_4v_3\in\eta\). Since _v_<sub>4</sub> prefers _v_<sub>3</sub> over \(p_2^i\), \(v_4p_2^i\) is not a blocking edge. Hence, there is no blocking edge incident to \(p_2^i\) as \(N(p_2^i)=\{w_4:w\in V_i\}\). Similarly, there is no blocking edge incident to \(p_1^i\).

**Claim 25** _Let_ \(e\in E(G[X])\)_. Then,_ \(e\tilde{e}\) _is a blocking edge with respect to_ \(\eta\)_. Moreover, there is no other blocking edge incident to e or_ \(\tilde{e}\).

_Proof._ Since \(e\tilde{e}\notin\eta\), and _e_ and \(\tilde{e}\) prefer each other over any other vertex, \(e\tilde{e}\) is a blocking edge with respect to \(\eta\). Let _e=uv_ where \(u\in V_i\), and \(v\in V_j\). Recall that the preference list of _e_ is \(\langle\tilde{e},u_3,v_3,q_1^{ij}\rangle\). Since _u_<sub>3</sub> does not prefer _e_ over \(u_2(=\eta(u_3))\), _u_<sub>3</sub>_e_ is not a blocking edge with respect to \(\eta\). Similarly, _v_<sub>3</sub>_e_ is not a blocking edge with respect to \(\eta\). Since \(eq_1^{ij}\in\eta\), \(e\tilde{e}\) is the only blocking edge incident to _e_ for \(\eta\). Since \(N(\tilde{e})=\{e,q_2^{ij}\}\), and \(\tilde{e}q_2^{ij}\in\eta\), there is no other blocking edge incident to \(\tilde{e}\) with respect to \(\eta\).

