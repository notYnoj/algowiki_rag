## Appendix

## A Omitted Proofs

### A.1 Subset Sensitivity Oracle for Matrix Determinant

**Lemma A.1.** _Let_ \(A,B\in\mathbb{F}_d[Y]^{r\times m}\) (\(r\le m\)), \(D\in\mathbb{F}_d[Y]^{m\times m}\) _be a diagonal matrix and let L=ADB<sup>T</sup>. Let_ \(Q\subseteq[m]\) _be a designated_ susceptible set _of size_ \(\sigma\)_, identified at preprocessing time, such that all future queries modify only diagonal entries of D indexed by Q._

_Then there is an algorithm that preprocesses A, B, and D to construct a data structure such that, given a diagonal matrix_ \(D'\) _differing from D in at most f positions (all within Q), computes_ \(\mathrm{det}(AD'B^T)\) _with the following complexity bounds:_

1. **_Scalar (d_=0):** _If the matrices A,B have entries in_ F_, then the preprocessing time is_ \(O(\sigma^2r^{\omega-2}+r^\omega)\)_, the space requirement is_ \(O(\sigma^2)\)_, and the query time is_ \(O(f^\omega)\).<tbc>

_2._ **_Polynomial (_**\(d\ge 1\)**_):_** _If the matrices have entries in_ F_<sub>d</sub>_\[_Y_\]_, then the preprocessing time is_ \(\widetilde{O}(d\sigma^2r^{\omega-1}+dr^{\omega+1})\)_, the space requirement is_ \(\widetilde{O}(dr\sigma^2)\)_, and the query time is_ \(\widetilde{O}(drf^\omega)\).

_Proof._ Let \(A,B\in\mathbb{F}_d[Y]^{r\times m}\) with \(r\le m\), and let \(D\in\mathbb{F}_d[Y]^{m\times m}\). Let \(Q\subseteq[m]\) be the given _susceptible set_ of size \(\sigma\). Let \(L=ADB^T\in\mathbb{F}_d[Y]^{r\times r}\). For a query \(D'\) that differs from _D_ on a set \(S\subseteq Q\) with \(|S|\le f\), let \(\Delta_S\) be the \(f\times f\) diagonal matrix with diagonal entries \(D'_{i_ji_j}-D_{i_ji_j}\) for \(i_j\in S\), and let _A<sub>S</sub>,B<sub>S</sub>_ be the submatrices of _A,B_ with columns indexed by _S_. The updated matrix is:<tbc>

\(L'=AD'B^T=L+A_S\Delta_SB_S^T.\)

<tbc>Let \(\delta=r-\mathrm{rank}(L)\ge 0\). Since \(\mathrm{rank}(A_S\Delta_SB_S^T)\le f\), we have:

\(\mathrm{rank}(L')\le(r-\delta)+f.\)

If \(\delta>f\), then \(\mathrm{rank}(L')<r\) for all valid queries, so \(\mathrm{det}(L')=0\) identically. In this case, we can answer every query in _O_(1) time and we are done. Thus, we assume \(\delta\le f\).

Take random matrices \(U,V\in\mathbb{F}_d^{r\times\delta}\) and let _L_<sub>pad</sub>=_L+UV<sup>T</sup>_. Since the rank deficiency of _L_ is exactly \(\delta\), there exist _U,V_ for which _L_<sub>pad</sub> is nonsingular. By the Schwartz-Zippel lemma, with high probability a random choice of _U,V_ yields \(\mathrm{det}(L_\mathrm{pad})\neq 0\), allowing us to assume _L_<sub>pad</sub> is invertible. (Note that we assume the field F is sufficiently large, in particular of size poly(_r_), which ensures that a random choice succeeds with high probability directly over F).

For any query, we can rewrite \(L'\) as:<tbc>

\(L'=L_\mathrm{pad}+\left(A_SU\right)\left(\begin{array}{ c c }
\Delta_S & 0 \\
0 & -I_\delta
\end{array}\right)\left(\begin{array}{ c }
B_S^T \\
V^T
\end{array}\right).\)

