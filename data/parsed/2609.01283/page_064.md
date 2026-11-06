_Proof._ Let \(\delta=N-rank(M)\ge 0\) be the rank deficiency of the base matrix _M_. The modification matrix _C_ has at most \(\delta_C\) nonzero entries, meaning \(rank(C)\le\delta_C\). Therefore, the rank of the updated matrix \(M'=M+C\) is bounded by:

\(rank(M')\le(N-\delta)+\delta_C.\)

If \(\delta>\delta_C\), then \(rank(M')<N\) for all possible queries, implying det(_M+C_)=0 identically. In this scenario, the algorithm flags this condition during preprocessing and answers all queries with 0 in _O_(1) time. Thus, we assume henceforth that \(\delta\le\delta_C\).

We sample random matrices \(U,V\in\mathbb{F}_d^{N\times\delta}\). Since the rank deficiency of _M_ is exactly \(\delta\), a generic rank-\(\delta\) correction makes the matrix nonsingular. By the Schwartz-Zippel lemma, assuming the field F_<sub>d</sub>_ is of size poly(_N_), a random choice of _U,V_ ensures that _M_<sub>pad</sub>=_M+UV<sup>T</sup>_ is invertible with high probability.

Since the matrix _C_ contains at most \(\delta_C\) nonzero entries, all located within \(Q\times Q\), we can explicitly factor it as a low-rank product using only indices from _Q_. Let \(k\le\delta_C\) be the exact number of nonzero entries in _C_, located at coordinates (_i_<sub>1</sub>_,j_<sub>1</sub>)_,...,(i<sub>k</sub>,j<sub>k</sub>_) where \(i_m,j_m\in Q\). We decompose _C_ as \(C=U_C\Delta_CV_C^T\), where \(\Delta_C\in\mathbb{F}_d[Y]^{k\times k}\) is a diagonal matrix with its _m_-th diagonal entry being _C<sub>i<sub>m</sub>,j<sub>m</sub></sub>_. The matrices \(U_C,V_C\in\mathbb{F}_d^{N\times k}\) are constructed from the standard basis vectors of \(\mathbb{F}_d^N\): the _m_-th column of _U<sub>C</sub>_ is _e<sub>i<sub>m</sub></sub>_, and the _m_-th column of _V<sub>C</sub>_ is _e<sub>j<sub>m</sub></sub>_.

We can now express the query matrix \(M'\) by introducing and immediately subtracting the numeric pad:<tbc>

\(M'=M+C=M_\mathrm{pad}+C-UV^T=M_\mathrm{pad}+\left(U_CU\right)\left(\begin{array}{ c c }
\Delta_C & 0 \\
0 & -I_\delta
\end{array}\right)\left(\begin{array}{ c }
V_C^T \\
V^T
\end{array}\right).\)

<tbc>Let \(X=\left(U_CU\right)\), \(Y=\left(V_CV\right)\), and \(\Sigma=\left(\begin{array}{ c c }
\Delta_C & 0 \\
0 & -I_\delta
\end{array}\right)\). Applying the Matrix Determinant lemma to the invertible matrix _M_<sub>pad</sub> yields:

\(det(M+C)=det(M_\mathrm{pad})det\left(I_{k+\delta}+\Sigma Y^TM_\mathrm{pad}^{-1}X\right).\) (3)

## Preprocessing.

We compute the rank of _M_ and determine \(\delta\). If \(\delta>\delta_C\), we store a short-circuit flag. Otherwise, we sample \(U,V\) until \(det(M_\mathrm{pad})\neq 0\). We then compute det(_M_<sub>pad</sub>) and the complete inverse matrix \(M_\mathrm{pad}^{-1}\).

Because all queries restrict the non-zero entries of _C_ to the susceptible set _Q_ of size \(\sigma\), the selection matrices _U<sub>C</sub>_ and _V<sub>C</sub>_ only ever sample rows and columns from _Q_. Thus, the inner matrix \(Y^TM_\mathrm{pad}^{-1}X\) will always be a principal submatrix of a larger precomputed matrix restricted to _Q_ and the pad. We construct and store this \((\sigma+\delta)\times(\sigma+\delta)\) matrix:

\(W_Q:=\left(I_{N,Q}V\right)^TM_\mathrm{pad}^{-1}\left(I_{N,Q}U\right),\)

where _I<sub>N,Q</sub>_ represents the \(N\times\sigma\) submatrix of the identity matrix _I<sub>N</sub>_ consisting of the columns indexed by _Q_. Note that since \(\delta\le\delta_C\le\sigma\), the dimensions of _W<sub>Q</sub>_ are \(O(\sigma\times\sigma)\).

• **For** _d_=0**:** Computing \(M_\mathrm{pad}^{-1}\) costs \(O(N^\omega)\) arithmetic operations. Extracting _W<sub>Q</sub>_ and storing it requires \(O(\sigma^2)\) space.<tbc>

• **For** \(d\ge 1\)**:** The entries of _M_<sub>pad</sub> have degree _d_, meaning the entries of \(M_\mathrm{pad}^{-1}\) are rational func tions of degree _O(dN_). From \[Sto15\] (Corollary 6.12), computing this inverse costs \(\widetilde{O}(dN^3)\) operations. Storing the \(O(\sigma)\times O(\sigma)\) matrix _W<sub>Q</sub>_ requires \(\widetilde{O}(dN\sigma^2)\) space.<tbc>

