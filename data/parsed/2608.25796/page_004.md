• {_A<sub>n</sub>}<sub>n</sub> has an (asymptotic) spectral or eigenvalue distribution described by_ \(\psi\) _if for any_ \(F\in C_c(\mathbb{C})\)<tbc>

<tbc>\(lim_{n\rightarrow\infty}\frac{1}{d_n}\sum_{i=1}^{d_n}F(\lambda_i(A_n))=\frac{1}{\mu_t(D)}\int_DF(\psi(x))dx,\)<tbc>

<tbc>_where_ \(\lambda_i(A_n)\)_, i_=1_,...,d<sub>n</sub>, are the eigenvalues of A<sub>n</sub>. We use the notation_ \(\{A_n\}_n\sim_\lambda\psi\).

The informal meaning behind Definition 2.1 is the following: if \(\psi\) is continuous and _n_ is large, then the eigenvalues or singular values of _A<sub>n</sub>_ (suitably ordered and possibly except at most for _o(d<sub>n</sub>_) outliers) are approximated by a uniform sampling of \(\psi\) or \(|\psi|\) over its domain; see \[27, Remark 2\] and also \[37, Remark 2.7\] for the more general setting of matrix-valued symbols.

**Remark 2.2.** _The relation_ \(\{A_n\}_n\sim_\lambda\psi\) _and_ \(\Lambda(A_n)\subseteq S\) _for all n imply that the range of_ \(\psi\) _is a subset of the closure <o>S</o> of S. In particular,_ \(\{A_n\}_n\sim_\lambda\psi\) _and A<sub>n</sub> positive definite for all n imply that_ \(\psi\) _is nonnegative almost everywhere; see e.g. \[7\] for its use in the spectral analysis of approximated FDEs and \[1, 27\] for the spectral study of matrix sequences stemming from geometric means._

The notion of clustering can be seen a special case of distribution. In what follows, we denote the \(\varepsilon\)-expansion of a set \(S\subseteq\mathbb{C}\) as

\(B(S,\varepsilon):=\bigcup_{z\in S}B(z,\varepsilon),\)

where \(B(z,\varepsilon):=\{w\in\mathbb{C}:|w-z|<\varepsilon\}\) is the complex disk with center _z_ and radius \(\varepsilon>0\).

**Definition 2.3.** _Let_ {_A<sub>n</sub>}<sub>n</sub> be a matrix sequence, with A<sub>n</sub> of size_ \(d_n\times d_n\)_, and let_ \(S\subseteq\mathbb{C}\) _be nonempty and closed. The sequence_ {_A<sub>n</sub>}<sub>n</sub> is **strongly clustered** at S in the sense of the eigenvalues if_ \(\forall\varepsilon>0\)<tbc>

\(\#\{j\in\{1,\dots,d_n\}:\lambda_j(A_n)\notin B(S,\varepsilon)\}=O(1),n\rightarrow\infty.\)

<tbc>_In other words, the number of eigenvalues of A<sub>n</sub> outside_ \(B(S,\varepsilon)\) _is bounded by a constant independent of n. Moreover,_ {_A<sub>n</sub>}<sub>n</sub> is **weakly clustered** at S if_ \(\forall\varepsilon>0\)

\(\#\{j\in\{1,\dots,d_n\}:\lambda_j(A_n)\notin B(S,\varepsilon)\}=o(d_n),n\rightarrow\infty,\)

_meaning that the number of eigenvalues of A<sub>n</sub> outside_ \(B(S,\varepsilon)\) _is negligible with respect to the size of the matrix. A corresponding definition can be given for the singular values, with_ \(S\subseteq\mathbb{R}^+\).

**Remark 2.4.** _Let us clarify the relationship between the concepts of distribution and clustering. We recall that the essential range of a measurable function_ \(g:D\subseteq\mathbb{R}^t\rightarrow\mathbb{C}\) _is the set_<tbc>

\(\{z\in\mathbb{C}:\mu_t(\{g\in B(z,\varepsilon)\})>0\forall\varepsilon>0\}.\)

<tbc>_As reported in \[23, Theorem 4.2\], it holds_<tbc>

\(\{A_n\}_n\sim_\lambda\psi\Longrightarrow\{A_n\}_n\text{\textit{is weakly clustered at the essential range of}}\psi.\)

<tbc>_Furthermore, if the essential range of_ \(\psi\) _consists of a single number_ \(s\in\mathbb{C}\)_, then_

\(\{A_n\}_n\sim_\lambda\psi\Longleftrightarrow\{A_n\}_n\text{\textit{is weakly clustered at s in the sense of the eigenvalues.}}\)

_The latter case is typically of interest in the context of preconditioning. Corresponding statements can be given for the singular values, with the obvious suitable changes._

