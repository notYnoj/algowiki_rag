It remains to evaluate \(\mathrm{det}(V_T^{E_m})\). By the classical alternant formula for Schur polynomials (see, for example, \[17\]), the generalized Vandermonde determinant factors as the ordinary Vandermonde determinant times the Schur polynomial associated with the exponent set. For _E<sub>m</sub>_, this Schur polynomial is the elementary symmetric polynomial _e_<sub>_q-m_</sub>. Hence

\(\mathrm{det}\big(V_T^{E_m}\big)=\prod_{r<sr,s\in T}(x_s-x_r)e_{q-m}((x_t)_{t\in T}).\)

This proves (24).

Now suppose that<tbc>

\(m=q+\ell,1\le\ell\le q.\)

<tbc>Then the deleted column belongs to the \(\beta\)-block. The \(\alpha\)-block keeps the full exponent set<tbc>

\(\{0,1,\dots,q-1\},\)

<tbc>whereas the \(\beta\)-block has exponent set \(E_\ell\). Thus a nonzero Cauchy–Binet term must assign _q_ indices to the \(\alpha\)-block and _q_-1 indices to the \(\beta\)-block. Hence the contributing subsets satisfy<tbc>

\(T\subseteq R_j,|T|=q.\)

<tbc>Then \(|T'|=q-1\). The same shuffle-sign argument gives

\(M_{j,q+\ell}=\sum_{T\subseteq R_j|T|=q}\varepsilon_j(T)\left(\prod_{i\in T}\alpha_i\right)\left(\prod_{i\in T^\prime}\beta_i\right)\mathrm{det}(V_T)\mathrm{det}\big(V_{T^\prime}^{E_\ell}\big).\)

This proves (25).

Similarly, the same alternant formula gives

\(\mathrm{det}\big(V_{T^\prime}^{E_\ell}\big)=\prod_{r<sr,s\in T^\prime}(x_s-x_r)e_{q-\ell}((x_t)_{t\in T^\prime}).\)

This proves (26) and completes the proof.

**Remark 2.6.** For large _q_ the \(\genfrac(){pt}{2}{2q}{q}\) terms in (21) are too numerous for the determinant formula to be useful for numerical computation. In practice, one may solve the system

\(\Lambda\mathbf{u}=\mathbf{e}_j\)

by Gaussian elimination, which requires _O(q_<sup>3</sup>) operations. For ordinary Vandermonde systems, specialized algorithms such as the Björck–Pereyra algorithm reduce the computational complexity; see, for example, \[5\]. Whether the particular block Vandermonde structure of (19) can be exploited to obtain a comparable fast algorithm is an interesting numerical question, which we do not pursue here.

## 3 The KEG-D system with approximate boundary values

### 3.1 Setting up the system

Let \(q\ge 1\), let<tbc>

\(f\in C^q([-1,1];\mathbb{R}^2),p,r\in C^q[-1,1],\)

<tbc>and assume that _f_<sup>(_q_)</sup> is absolutely continuous. For sufficiently large _N_, choose 2_q_ distinct indices \(n_1,\dots,n_{2q}\in\mathbb{Z}\backslash\{0\}\) satisfying

\(\alpha_0N\le|n_s|\le N,s=1,\dots,2q,\) (27)

