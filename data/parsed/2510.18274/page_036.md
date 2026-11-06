An analogous calculation also shows that \(w_{H_A\cup H_B}(S,T)\ge(1-\varepsilon)\cdot|E_{G_A\cup G_B}(S,T)|\). These bounds together conclude that \(H_A\cup H_B\) as an \(\varepsilon\)-cut sparsifier of \(G=G_A\cup G_B\).

## B Spectral Sparsification with Optimal Weights

For any undirected graph _G_=(_V,E_) with a nonnegative weight function _w<sub>G</sub>_, denote its _Laplacian matrix_ by

\(L_G:=\sum_{e\in E}w_G(e)\cdot\chi_e\chi_e^\top\)

whereas \(\chi_e=e_a-e_b\) for an edge _e_=(_a,b_).

We say a graph _H_ is an \(\varepsilon\)_-spectral sparsifier_ of _G_ iff \(E(H)\subseteq E(G)\) and for any \(v\in\mathbb{R}^n\), we have

\(1-\varepsilon\le\frac{v^\top L_Hv}{v^\top L_Gv}\le 1+\varepsilon.\)

As a corner case, we note that any Laplacian of a connected graph has null space spanned by an all-one vector \(\vec{1}\). Therefore, it suffices to consider only vectors _v_ that are orthogonal to \(\vec{1}\).

**Observation B.1.** _An_ \(\varepsilon\)_-spectral sparsifier is also an_ \(\varepsilon\)_-cut sparsifier._

The goal of this section is to show that any unweighted undirected graph _G_ has an \(\varepsilon\)-spectral sparsifer with an optimal tradeoff between the number of edges and the maximum weights, as stated in Theorem 2.6. We begin by introducing necessary tools, and then proceed to prove the theorem.

### B.1 Preliminaries

For any matrix \(M\in\mathbb{R}^{n\times n}\), denote \(\lambda_1(M)\ge\dots\ge\lambda_n(M)\) to be its eigenvalues in a decreasing order. We say a matrix _M_ is _positive semidefinite_ (or _psd_ for short) iff \(\lambda_n(M)\ge 0\).

For any connected graph _G_=(_V,E_), its Laplacian _L<sub>G</sub>_ is symmetric and is psd. Plus, _L<sub>G</sub>_ has _n_-1 non-zero eigenvalues, and its kernel is of dimension 1 and spanned by \(\vec{1}\). Hence, we can write

\(L_G:=\sum_{i=1}^n\lambda_iu_iu_i^\top\)

where \(\lambda_1\ge\dots\ge\lambda_{n-1}>0\) are the top _n_-1 eigenvalues of _L<sub>G</sub>_ and _u_<sub>1</sub>_,...,u_<sub>_n_-1</sub> are the corresponding orthonormal eigenvectors. Note that its bottom eigenvalue is \(\lambda_n=0\) with respect to an orthonormal eigenvector is \(u_n=\frac{1}{\sqrt{n}}\cdot\vec{1}\).

Denote a Moore-Penrose pseudoinverse of _L<sub>G</sub>_ as:<tbc>

\(L_G^+=\sum_{i=1}^{n-1}\frac{1}{\lambda_i}u_iu_i^\top\)

<tbc>and its "square root" as<tbc>

\(L_G^{+/2}=\sum_{i=1}^{n-1}\frac{1}{\sqrt{\lambda_i}}u_iu_i^\top.\)

<tbc>Also denote

\(\Pi=L_G^{+/2}L_GL_G^{+/2}=\sum_{i=1}^{n-1}u_iu_i^\top\)

to be a projection matrix on to the range of _L<sub>G</sub>_.

