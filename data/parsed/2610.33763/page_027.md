**Proposition 2.2 (\[12, Corollary 2\])** _Let_ {_A<sub>n</sub>}<sub>n</sub> be a matrix sequence such that A<sub>n</sub>=B<sub>n</sub>+C<sub>n</sub>, where B<sub>n</sub> is Hermitian_ \(\forall n\in\mathbb{N}\)_. Suppose that_

• \(\{B_n\}_n\sim_\lambda\psi\),<tbc>

• \(\|C_n\|=o(1)\).

_Then_ \(\{A_n\}_n\sim_\lambda\psi\).

An important aspect of spectral distributions for matrix sequences is their intrinsic non-uniqueness. Once a function describing the asymptotic spectral distribution has been identified, it is by no means unique. Indeed, there exist infinitely many alternative representations that encode exactly the same spectral information. In particular, any measurable function that satisfies the same integral identities with respect to all compactly supported continuous test functions yields an equivalent distribution. More precisely, let \(\psi\) be a distribution function defined on a measurable set _D_; then any measurable mapping \(\varphi:E\subset\mathbb{R}^s\rightarrow\mathbb{C}\) such that

\(\frac{1}{\mu_t(D)}\int_DF(\psi(x))dx=\frac{1}{\mu_s(E)}\int_EF(\varphi(x))dx,\forall F\in C_c(\mathbb{C}),\)

represents the same asymptotic distribution. These alternative representations may differ substantially in form, including the dimension of their domain or the number of variables involved. Moreover, by suitably extending the notion of distribution, the associated symbol may take matrix-valued values, provided that the corresponding integral characterization remains valid; see, for example, \[11, 10\].

The notion of clustering can be regarded as a special case of spectral distribution.

**Definition 2.2** _Let_ {_A<sub>n</sub>}<sub>n</sub> be a matrix sequence with_ \(A_n\in\mathbb{C}^{d_n\times d_n}\)_, and let_ \(S\subseteq\mathbb{C}\) _be a nonempty closed set._

• _The sequence_ {_A<sub>n</sub>}<sub>n</sub> is said to be_ strongly clustered at _S_ in the sense of the eigenvalues _if, for any_ \(\varepsilon>0\) _and as_ \(n\rightarrow+\infty\)_, the number of eigenvalues of A<sub>n</sub> lying outside the_ \(\varepsilon\)_-neighborhood of S is bounded independently of n, that is,_<tbc>

<tbc>\(\#\big\{j\in\{1,\dots,d_n\}:\lambda_j(A_n)\notin B(S,\varepsilon)\big\}=O(1),n\rightarrow+\infty.\)<tbc>

• _The sequence_ {_A<sub>n</sub>}<sub>n</sub> is said to be_ weakly clustered at _S_ in the sense of the eigenvalues _if, for any_ \(\varepsilon>0\) _and as_ \(n\rightarrow+\infty\)_, the number of eigenvalues of A<sub>n</sub> lying outside_ \(B(S,\varepsilon)\) _is negligible with respect to the matrix size, namely,_<tbc>

<tbc>\(\#\big\{j\in\{1,\dots,d_n\}:\lambda_j(A_n)\notin B(S,\varepsilon)\big\}=o(d_n),n\rightarrow+\infty.\)<tbc>

<tbc>**Remark 2.1** _Let us clarify the relationship between the concepts of distribution and clustering. We recall that the essential range of a measurable function_ \(g:D\subseteq\mathbb{R}^t\rightarrow\mathbb{C}\) _is the set_<tbc>

\(\{z\in\mathbb{C}:\mu_t\big(\{g\in B(z,\varepsilon)\}\big)>0\forall\varepsilon>0\}.\)

<tbc>_As reported in \[45, Theorem 4.2\], it holds_<tbc>

\(\{A_n\}_n\sim_\lambda\psi\Longrightarrow\{A_n\}_n\text{\textit{is weakly clustered at the essential range of}}\psi.\)

