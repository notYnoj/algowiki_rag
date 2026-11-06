\(=\lambda_{max}((I-\widehat{M}^{-1}B)^{\nu_1}(I-\Pi_A)(I-\widehat{M}^{-1}B)^{\nu_2}(I-\Pi_A))\)<br>
\(=\lambda_{max}((I-\widehat{M}^{-1}B)^{\nu_1+\nu_2}(I-\Pi_A))\)<br>
\(=\lambda_{max}\left((I-\mathrm{diag}(\mu_1,\dots,\mu_n))^{\nu_1+\nu_2}\left(I-\left[\begin{array}{ c c }
I_{n_c} & 0 \\
0 & 0
\end{array}\right]\right)\right)\)<br>
\(=\lambda_{max}\left(\left[\begin{array}{ c c c }
0_{n_c} &  &  \\
(1-\mu_{n_c+1})^{\nu_1+\nu_2} &  &  \\
 & \ddots &  \\
 &  & (1-\mu_n)^{\nu_1+\nu_2}
\end{array}\right]\right)\)<br>
\(=(1-\mu_{n_c+1})^{\nu_1+\nu_2}<1.\) □

This result directly generalizes \[2, Theorems 4.5, 4.6\] where the same result is proven for \(\nu_1=1\) and \(\nu_2=0\).<br>
For _B=A_ HPD this result reduces to the known results \[38, Theorems 5.3, 5.6, 5.7\]. Theorem 4.1 holds for any HPD matrix _B_. This might seem like a contradiction to Theorem 2.9 (5) which describes the set of all HPD matrices such that a given matrix can be _B_-normal. But is not the case. Because \(\widehat{M}^{-1}B\) is _B_-orthogonal for any HPD matrix _B_ (see Proposition 3.3), any change in _B_ results in a different matrices \(\widehat{M}^{-1}B\), \(\hat{P}\) and \(\hat{R}\) and therefore also different error operators. Hence, if we use _M_<sup>-1</sup>_A_ and (_M_<sup>-1</sup>_A_)<sup>+</sup> as pre- and post-smoother, respectively, combined with \(\Pi_A(\hat{P},\hat{R})\) as in Theorem 4.1, we are able to construct a convergent two-grid method in any given inner product on C_<sup>n</sup>_.

_Remark_ 4.2. It is possible to achieve the same result for arbitrary \(\nu_1,\nu_2\in\mathbb{N}_0\) if we add the assumption that _M_<sup>-1</sup>_A_ is _B_-normal.

In the second part of our theoretical framework \[30\] we prove further characterizations for the _B_-norm of \(E_+^{\nu_1,\nu_2}\).

In Theorem 4.1 we considered the special choice \(\hat{P}\) and \(\hat{R}\) as prolongation and restriction operators. An obvious question is whether these choices of _P_ and _R_ are optimal in the sense that any other pair (_P,R_) of interpolation and restriction yields a larger _B_-norm of \(E_+^{\nu_1,\nu_2}(P,R)\) than \((\hat{P},\hat{R})\). To answer this question, we first require the generalized Courant-Fisher-Weyl theorem (cf. \[19, Theorem 3.2\]).

Theorem 4.3. _Let_ \(\lambda_1\le\cdots\le\lambda_n\) _be the eigenvalues of the matrix C_<sup>-1</sup>_A where_ \(A\in\mathbb{C}^{n\times n}\) _is Hermitian and_ \(C\in\mathbb{C}^{n\times n}\) _is HPD. Then, for any subspace_ \(M\subseteq\mathbb{C}^n\) _it holds_

\(\lambda_k=\mathrm{min}_{M\subseteq\mathbb{C}^n\mathrm{dim}(M)=n-k+1}\mathrm{max}_{x\in Mx\neq 0}\frac{x^HAx}{x^HCx}.\)

With this result we can now show that \((\hat{P},\hat{R})\) is indeed the combination that yields the smallest _B_-norm of the error operator \(E_+^{\nu_1,\nu_2}\) for \((\nu_1,\nu_2)\in\{(0,1),(1,0),(1,1)\}\). The only additional constraint we require is the invertibility of \(I-\widehat{M}^{-1}B\). The result also shows that the optimal transfer operators are not unique. The proof uses the same idea as the proof of \[16, Theorem 3.5\].

Theorem 4.4. _Let the smoothing assumption be satisfied. Let_

\(\widehat{M}^{-1}B=V\mathrm{diag}(\mu_1,\dots,\mu_n)V^{-1}=:VDV^{-1}\)

_be a B-unitary diagonalization of_ \(\widehat{M}^{-1}B\) _with sorted eigenvalues_ \(\mu_1\le\cdots\le\mu_n\) _and corresponding B-unitary eigenvectors_ \(V=\left[v_1\cdots v_n\right]\)_. Furthermore, let_ \(I-\widehat{M}^{-1}B\)

