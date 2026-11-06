<tbc>Let \(\ell=\sigma(V_i,u)\), i.e the solution _S_ contains the \(\ell^{th}\) vertex of the set _V<sub>i</sub>_. Then, we delete \(\{a_{1,\lceil\ell/2\rceil}^ip_{\lceil\ell/2\rceil}^i,\tilde{a}_{1,\lceil\ell/2\rceil}^i\widetilde{p}_{\lceil\ell/2\rceil}^i\}\) from \(\eta\) and add \(\{u_1p_{\lceil\ell/2\rceil}^i,u_{2r+2}\widetilde{p}_{\lceil\ell/2\rceil}^i\}\) to \(\eta\). Additionally, we delete \(\{a_{j,h}^ib_{j-1,h}^i,\tilde{a}_{j,h}^i\widetilde{b}_{j-1,h}^i:j\in[\mathrm{log}_2(n/2)]\backslash\{1\},h=\lceil\ell/2^j\rceil\}\) and add set \(\{a_{j,h}^ib_{j,h^\prime}^i,\tilde{a}_{j,h}^i\widetilde{b}_{j,h^\prime}^i:j\in[\mathrm{log}_2(n/2)],h=\lceil\ell/2^j\rceil,h'=\lceil\ell/2^{j+1}\rceil\}\) to \(\eta\).

Let edge \(e=E(G[S])\cap E_{ij}\), i.e. edge _e_ in _E<sub>ij</sub>_ is in the clique solution, for some \(\{i,j\}\subseteq[k]\). Suppose that for some \(\ell\in[m]\), _e_ is the \(\ell^{th}\) edge in _E<sub>ij</sub>_. Then, we delete set \(\{e\tilde{e},q_{\lceil\ell/2\rceil}^{ij}c_{1,\lceil\ell/2\rceil}^{ij},\tilde{q}_{\lceil\ell/2\rceil}^{ij}\widetilde{c}_{1,\lceil\ell/2\rceil}^{ij}\}\) from \(\eta\) and add \(\{eq_{\lceil\ell/2\rceil}^{ij},\tilde{e}\widetilde{q}_{\lceil\ell/2\rceil}^{ij}\}\) to \(\eta\). Additionally, we delete edges \(\{c_{h,s}^{ij}d_{h-1,s}^{ij},\widetilde{c}_{h,s}^{ij}\widetilde{d}_{h-1,s}^{ij}:h\in[\mathrm{log}_2(m/2)]\backslash\{1\}\},s=\lceil\ell/2^h\rceil\}\) from \(\eta\) and add set \(\{c_{h,s}^{ij}d_{h,s^\prime}^{ij},\widetilde{c}_{h,s}^{ij}\widetilde{d}_{h,s^\prime}^{ij}:h\in[\mathrm{log}_2(m/2)],s=\lceil\ell/2^h\rceil,s'=\lceil\ell/2^{h+1}\rceil\}\). Due to the construction of \(\eta\), clearly it is a matching.

The following result implies that the matching \(\eta\) constructed as above satisfies the size bound of a solution for our instance J of ASM.

**Claim 4** _Matching_ \(\eta\) _described above has size_ \(|\mu|+k+^{k(k-1)}/2\).

_Proof._ For each (clique) vertex \(u=S\cap V_i\), where \(i\in[k]\), we delete _r_+2log<sub>2</sub>(_n/_2)+1 edges from \(\eta\) (which also belong to \(\mu\)), and add _r_+2log<sub>2</sub>(_n/_2)+2 edges to \(\eta\). This gives us an an additional _k_ edges in \(\eta\).

Similarly, for each clique edge \(e=E(G[S])\cap E_{ij}\), where \(\{i,j\}\subseteq[k],i<j\), we delete 2log<sub>2</sub>(_m/_2)+1 edges from \(\eta\) (which also belong to \(\mu\)), and add 2log<sub>2</sub>(_m/_2)+2 edges to \(\eta\). This, gives us an additional <sup>_k(k_-1)</sup>/2 edges in \(\eta\). Thus, in total \(|\eta|=|\mu|+k+^{k(k-1)}/2\).

Next, we prove that \(\eta\) has \(k'=k+^{k(k-1)}/2\) blocking edges. Due to Proposition 1, for a blocking edge with respect to \(\eta\), at least one of its endpoint is in \(V(\mu\triangle\eta)\). Therefore, we only need to investigate the vertices of \(V(\mu\triangle\eta)\). We begin by characterizing the vertices in the set \(V(\mu\triangle\eta)\).

Note that

\(V(\mu\triangle\eta)=\{u_{2h-1},u_{2h}:u\in S,h\in[r+1]\}\cup\{e,\tilde{e}:e\in E(G[S])\}\)<br>
\(\bigcup_{i\in[k]}\{p_{\lceil\ell/2\rceil}^i,\widetilde{p}_{\lceil\ell/2\rceil}^i,a_{j,\lceil\ell/2^j\rceil}^i,\widetilde{a}_{j,\lceil\ell/2^j\rceil}^i,b_{j,\lceil\ell/2^{j+1}\rceil}^i,\widetilde{b}_{j,\lceil\ell/2^{j+1}\rceil}^i:\)<br>
\(S\text{contains the}\ell^{th}\text{vertex of}V_i,j\in[\mathrm{log}_2(n/2)]\}\)<br>
\(\bigcup_{\{i,j\}\subseteq[k],i<j}\{q_{\lceil\ell/2\rceil}^{ij},\widetilde{q}_{\lceil\ell/2\rceil}^{ij},c_{h,\lceil\ell/2^h\rceil}^{ij},\widetilde{c}_{h,\lceil\ell/2^h\rceil}^{ij},d_{h,\lceil\ell/2^{h+1}\rceil}^{ij},\widetilde{d}_{h,\lceil\ell/2^{h+1}\rceil}^{ij}:\)<br>
\(G[S]\text{contains the}\ell^{th}\text{edge of}E_{ij},h\in[\mathrm{log}(m/2)]\}\)

**Claim 5** _For any_ \(u\in S\) _and any_ \(h\in[r]\)_, there is no blocking edge with respect to_ \(\eta\) _that is incident to the vertex u_<sub>2_h_+1</sub> _or u_<sub>2_h_+2</sub>.

_Proof._ For any value \(h\in[r]\), vertex _u_<sub>2_h_+1</sub> is matched to its most preferred vertex in \(\eta\), namely _u_<sub>2_h_</sub>. Therefore, there is no blocking edge incident on _u_<sub>2_h_+1</sub>. For any \(h'\in[r-1]\), we have \(N(u_{2h^\prime+2})=\langle u_{2h^\prime+1},u_{2h^\prime+3}\rangle\). Thus, there is no blocking edge incident to \(u_{2h^\prime+2}\).

Suppose that _u_ is the \(\ell^{th}\) vertex in _V<sub>i</sub>_. Then, we have \(N(u_{2r+2})=\langle u_{2r+1},\widetilde{p}_{\lceil\ell/2\rceil}^i\rangle\), and we know that the edge \(u_{2r+2}\widetilde{p}_{\lceil\ell/2\rceil}^i\) is in \(\eta\). However, since _u_<sub>2_r_+1</sub> is matched<tbc>

