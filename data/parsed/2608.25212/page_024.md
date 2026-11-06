to _Q_, for each \(t\in[s]\). We build in time O(|_Q_|log<sup>3</sup>|_Q_|)=O<sub>C</sub>(_m_log<sup>5</sup>_n_) a 4-dimensional orthogonal range data structure D_<sub>Q</sub>_ that, given a query box, returns in time O(log<sup>3</sup>|_Q_|)=O<sub>C</sub>(log<sup>3</sup>_n_) one point of _Q_ contained in the box, if one exists \[21, Theorem 5.11\].

Now for every triple _J<sub>h</sub>_, _J<sub>j</sub>_, and \(J_k=[\alpha_k,\beta_k]\), we query the box \(J_h\times J_j\times(-\infty,\beta_k]\times(-\infty,-\alpha_k]\) on D_<sub>Q</sub>_. If the query returns a point \(q_{u,v,t}\in Q\), it holds that \(u\in J_h\), \(v\in J_j\), \(uv\in E(G)\), \(\ell_t\unknown\beta_k\), and \(r_t\unknown\alpha_k\). In particular, the interval \([\ell_t,r_t]\) of \(N_G(u)\cap N_G(v)\) intersects _J<sub>k</sub>_. Let _z_ be any vertex in \([\ell_t,r_t]\cap J_k\). It holds that _uvz_ is a triangle in \(\widehat{Z}_{i,a}\supseteq J_k\), and we return the 5-vertex clique {_u<sub>i</sub>,a,u,v,z_}. If no _K_<sub>5</sub> is found, _u<sub>i</sub>_ is removed and the algorithm continues with _G_<sub>_i_+1</sub> (next iteration).

Each iteration takes time O<sub>C</sub>((log<sup>2</sup>_n_)<sup>3</sup>log<sup>3</sup>_n_)=O<sub>C</sub>(log<sup>9</sup>_n_), hence the overall running time O<sub>C</sub>(_n_log<sup>9</sup>_n+m_log<sup>5</sup>_n_).

One should, however, not expect an almost-linear dependence on _n_ uniformly over all clique sizes _k_. The Exponential Time Hypothesis (ETH) asserts that there exists a constant \(\lambda>0\) such that 3-SAT on _n_ variables cannot be solved in time \(O(2^{\lambda n})\) \[33\].

**Theorem 31.** _There is a class_ C _of linear neighborhood complexity such that k-Clique cannot be solved in time f(k)n_<sup>_o(k/_log_k_)</sup> _for any function f, unless the ETH fails._

_Proof._ By \[41, Theorem 1.3\] specialized to bipartite 3-regular graphs, as stated in \[34, Theorem 1.4\], unless the ETH fails, 2-CSP with alphabet \(\Sigma\) and _q_ constraints cannot be solved in time \(g(q)|\Sigma|^{o(q/logq)}\) for any computable function _g_.

Let \(\Gamma\) be such an instance, and _H_=(_X,Y;E_) be its constraint graph. Thus |_E_|=_q_. For every constraint \(e=uv\in E\), where \(u\in X\) and \(v\in Y\) , let \(C_e\subseteq\Sigma^2\) be the set of pairs allowed by _e_. We construct the cell gadget from the proof of \[10, Theorem 3\] with _r_=3 and tile set _C<sub>e</sub>_: each of its five _blocks_ contains a copy of (_a,b_) for every \((a,b)\in C_e\). Denote the two border blocks at the ends of its horizontal (resp. vertical) path by _L<sub>e</sub>_ and _R<sub>e</sub>_ (resp. by _U<sub>e</sub>_ and _D<sub>e</sub>_), and the central block by _M<sub>e</sub>_. Each block is a clique, and every copy of (_a,b_) in _M<sub>e</sub>_ is adjacent to every vertex in \(L_e\cup R_e\cup U_e\cup D_e\) except the four copies of (_a,b_).

For every \(u\in X\), let _e_<sub>1</sub>_,e_<sub>2</sub>_,e_<sub>3</sub> be the edges of _H_ incident to _u_. For every \(i\in[3]\), we add edges between _R<sub>e<sub>i</sub></sub>_ and _L_<sub>_e<sub>i</sub>_mod3+1</sub>, making two vertices adjacent precisely when their first coordinates differ. Similarly, for each variable \(v\in Y\) , we arbitrarily list the edges of _H_ incident to _v_ as _f_<sub>1</sub>_,f_<sub>2</sub>_,f_<sub>3</sub> and, for every \(i\in[3]\), add edges between _D<sub>f<sub>i</sub></sub>_ and _U_<sub>_f<sub>i</sub>_mod3+1</sub>, making two vertices adjacent precisely when their second coordinates differ.

Denote the resulting graph by \(G_\Gamma\). By the correctness argument of \[10\], \(\Gamma\) is satisfiable if and only if \(\alpha(G_\Gamma)\unknown 5q\), and

\(|V(G_\Gamma)|=5\sum_{e\in E}|C_e|\unknown 5q|\Sigma|^2.\)

Moreover, by the radius-2 merge sequence from \[10\], \(\mathsf{mw}_2(G_\Gamma)=\mathsf{mw}_{r-1}(G_\Gamma)\unknown 4r-3=9\). Observe indeed that the upper bound on the width of the merge sequences does not depend on which pairs of border blocks from distinct cells are connected. Let C consist of the complements of all graphs \(G_\Gamma\). By \[9, Theorem 1.5\], the graphs \(G_\Gamma\) form a class of linear neighborhood complexity. This property is preserved under complementation.

Now an algorithm for _k_-Clique on C running in time _f(k)n_<sup>_o(k/_log_k_)</sup>, applied to \(\overline{G_\Gamma}\) with _k_=5_q_, would decide \(\Gamma\) in time

\(f(5q)\big(5q|\Sigma|^2\big)^{o(q/logq)}=g(q)|\Sigma|^{o(q/logq)}.\)

The polynomial time needed to construct \(G_\Gamma\) is absorbed in this bound. This contradicts the ETH lower bound of 2-CSP.

