Let \(X=\left(A_S|U\right)\), \(Y=\left(B_S|V\right)\), and \(M_S=\left(\begin{array}{ c c }
\Delta_S & 0 \\
0 & -I_\delta
\end{array}\right)\). Applying the Matrix Determinant lemma to the invertible matrix _L_<sub>pad</sub> yields:

\(det(L')=det(L_\mathrm{pad})det\big(I_{f+\delta}+M_SY^TL_\mathrm{pad}^{-1}X\big).\) (2)

### Preprocessing.

We compute _L_, its rank, and \(\delta\). If \(\delta>f\), we store a flag to return 0 for all queries. Otherwise, we sample _U,V_ until \(det(L_\mathrm{pad})\neq 0\), then compute and store det(_L_<sub>pad</sub>).

Because all queries are restricted to the susceptible set _Q_ of size \(\sigma\), the matrix \(Y^TL_\mathrm{pad}^{-1}X\) will always be a principal submatrix of a larger precomputed matrix restricted to _Q_ and the pad. We construct and store this \((\sigma+\delta)\times(\sigma+\delta)\) matrix:

\(W_Q:=\left(B_Q|V\right)^TL_\mathrm{pad}^{-1}\left(A_Q|U\right).\)

Note that since \(\delta\le f\le\sigma\), the dimensions of _W<sub>Q</sub>_ are \(O(\sigma\times\sigma)\).

• **For** _d_=0**:** Inverting _L_<sub>pad</sub> costs \(O(r^\omega)\) operations. Multiplying the \(r\times r\) matrix \(L_\mathrm{pad}^{-1}\) by the \(r\times(\sigma+\delta)\) matrix (_A<sub>Q</sub>|U_) requires \(O(\sigma r^{\omega-1}+r^\omega)\) time using rectangular matrix multiplication. Multiplying (_B<sub>Q</sub>|V)<sup>T</sup>_ by the result takes \(O(\sigma^2r^{\omega-2}+r^\omega)\) time. Thus, total preprocessing is \(O(\sigma^2r^{\omega-2}+r^\omega)\), and storing _W<sub>Q</sub>_ requires \(O(\sigma^2)\) space.<tbc>

• **For** \(d\ge 1\)**:** _L_<sub>pad</sub> is an \(r\times r\) matrix with entries of degree _d_. Thus, \(L_\mathrm{pad}^{-1}\) has entries that are rational functions of degree _O(dr_). From \[Sto15\], computing \(L_\mathrm{pad}^{-1}\) costs \(\widetilde{O}(dr^3)\) operations. By the same rectangular multiplication bounds scaled for polynomials, computing _W<sub>Q</sub>_ requires \(\widetilde{O}(d\sigma^2r^{\omega-1}+dr^{\omega+1})\) time. Storing the \(O(\sigma\times\sigma)\) matrix _W<sub>Q</sub>_ requires \(\widetilde{O}(dr\sigma^2)\) space.

### Query.

If we stored \(\delta>f\), we immediately answer 0. Otherwise, let _I<sub>S</sub>_ be the index set corresponding to the queried columns _S_ alongside the \(\delta\) pad indices. The required \((f+\delta)\times(f+\delta)\) matrix \(Y^TL_\mathrm{pad}^{-1}X\) is exactly the submatrix (_W<sub>Q</sub>)<sub>I<sub>S</sub>,I<sub>S</sub></sub>_.

We extract (_W<sub>Q</sub>)<sub>I<sub>S</sub>,I<sub>S</sub></sub>_, multiply it by _M<sub>S</sub>_, add the identity matrix \(I_{f+\delta}\), and compute the determinant of the resulting \((f+\delta)\times(f+\delta)\) matrix as per Equation (2).

• **For** _d_=0**:** Since \(f+\delta\le 2f\), evaluating this determinant costs \(O(f^\omega)\) field operations.<tbc>

• **For** \(d\ge 1\)**:** The entries of (_W<sub>Q</sub>)<sub>I<sub>S</sub>,I<sub>S</sub></sub>_ have degree _O(dr_), so computing the determinant costs \(\widetilde{O}(drf^\omega)\) field operations. Multiplying the result by the precomputed scalar det(_L_<sub>pad</sub>) completes the evaluation.

This proves the claim. \(\square\)

## A.2 Extension of Theorem 2.4 to General matrices

**Lemma A.2.** _Let_ \(M\in\mathbb{F}_d[Y]^{N\times N}\) _be a matrix (possibly singular). Let_ \(Q\subseteq[N]\) _be a designated_ susceptible set _of size_ \(\sigma\)_, identified at preprocessing time, such that all future queries add a modification matrix_ \(C\in\mathbb{F}_d[Y]^{N\times N}\) _whose non-zero entries are entirely confined to_ \(Q\times Q\)_. Then, there is a randomized algorithm that preprocesses M using_ \(\widetilde{O}(dN^3)\) _operations to create a data structure occupying_ \(\widetilde{O}(dN\sigma^2)\) _space with the following guarantee: given C with at most_ \(\delta_C\) _nonzero entries, one can query_ det(_M+C_) _in_ \(\widetilde{O}(dN\delta_C^\omega)\) _operations._

_Moreover, if d_=0_, then the preprocessing time, space, and query time are_ \(O(N^\omega)\), \(O(\sigma^2)\)_, and_ \(O(\delta_C^\omega)\) _respectively._

