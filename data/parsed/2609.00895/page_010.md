**Theorem 2.5.** _Fix_ \(j\in[2q]\).

_If_ \(1\le m\le q\)_, then_

\(M_{j,m}=\sum_{T\subseteq R_j|T|=q-1}\varepsilon_j(T)\left(\prod_{i\in T}\alpha_i\right)\left(\prod_{i\in T^\prime}\beta_i\right)\mathrm{det}\left(V_T^{E_m}\right)\mathrm{det}(V_{T^\prime}),\) (23)

_where_

\(\mathrm{det}\left(V_T^{E_m}\right)=\prod_{r<sr,s\in T}(x_s-x_r)e_{q-m}((x_t)_{t\in T}).\) (24)

_If_ \(m=q+\ell\), \(1\le\ell\le q\)_, then_

\(M_{j,q+\ell}=\sum_{T\subseteq R_j|T|=q}\varepsilon_j(T)\left(\prod_{i\in T}\alpha_i\right)\left(\prod_{i\in T^\prime}\beta_i\right)\mathrm{det}(V_T)\mathrm{det}\left(V_{T^\prime}^{E_\ell}\right),\) (25)

_where_

\(\mathrm{det}\left(V_{T^\prime}^{E_\ell}\right)=\prod_{r<sr,s\in T^\prime}(x_s-x_r)e_{q-\ell}((x_t)_{t\in T^\prime}).\) (26)

_Proof._ We compute the minors _M<sub>j,m</sub>_. First suppose that \(1\le m\le q\), so that the deleted column belongs to the \(\alpha\)-block. After deleting row _j_ and column _m_, the remaining rows are indexed by _R<sub>j</sub>_. The remaining \(\alpha\)-block has exponent set _E<sub>m</sub>_, while the \(\beta\)-block still has exponent set

\(\{0,1,\dots,q-1\}.\)

Applying the same Cauchy-Binet argument as in the proof of Theorem 2.2 to the matrix obtained after deleting row _j_ and column _m_, a nonzero term is obtained by assigning _q_-1 indices to the \(\alpha\)-block and _q_ indices to the \(\beta\)-block. Hence the contributing subsets are precisely

\(T\subseteq R_j,|T|=q-1.\)

Then \(|T'|=q\). The indices in _T_ contribute to the \(\alpha\)-block, while the indices in \(T'\) contribute to the \(\beta\)-block.

For a fixed _T_, the diagonal weights contribute

\(\left(\prod_{i\in T}\alpha_i\right)\left(\prod_{i\in T^\prime}\beta_i\right).\)

The associated shuffle places the elements of _T_ before the elements of \(T'\), while preserving the natural order within each set. By definition, the sign of this shuffle is

\(\varepsilon_j(T)=(-1)\sum_{k=1}^{q-1}(\rho_j(t_k)-k),T=\{t_1<\cdots<t_{q-1}\}.\)

The polynomial part contributes

\(\mathrm{det}\left(V_T^{E_m}\right)\text{and}\mathrm{det}(V_{T^\prime}).\)

Therefore

\(M_{j,m}=\sum_{T\subseteq R_j|T|=q-1}\varepsilon_j(T)\left(\prod_{i\in T}\alpha_i\right)\left(\prod_{i\in T^\prime}\beta_i\right)\mathrm{det}\left(V_T^{E_m}\right)\mathrm{det}(V_{T^\prime}).\)

This proves (23).

