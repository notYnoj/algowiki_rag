**Definition 20** (Remaining mixed products)**.** _For a tripartition family_ S _and selected corrections_ \(\mathcal{Q}\subseteq\mathcal{P}(\mathcal{S})\)_, let_

\(\mathcal{J}=\{(i,j,k)\text{\textit{non-diagonal}}:\eta_r(i,j,k)\neq 2\text{\textit{for every}}r\in F,c_\mathcal{Q}(\mathcal{R}_{ijk})\neq 0\}.\) (104)

_When_ Q=P(S)_, we have_ J=B(S) _of Definition 17._

The following theorem shows that this scaling makes the unwanted products tend to zero while using at most \(\rho_{\mathcal{S},\mathcal{Q}}(n)\) rank-one terms for the main aggregate and its corrections.

**Theorem 3** (Border rank by parameter scaling)**.** _Let_ \(\mathcal{Q}\subseteq\mathcal{P}(\mathcal{S})\)_. If a grading of_ S _has a<sub>i</sub>+b<sub>j</sub>+c<sub>k</sub>\>_0 _for every remaining mixed product_ \((i,j,k)\in\mathcal{J}\) _of Definition 20, then_

\(\underline{R}\left(\oplus_{t=1}^m\left\langle n^{|V_t|},n^{|W_t|},n^{|U_t|}\right\rangle\right)\le\rho_{\mathcal{S},\mathcal{Q}}(n)\le\rho_\mathcal{S}(n).\) (105)

_Proof._ By (83), the main aggregate and selected corrections use at most \(\rho_{\mathcal{S},\mathcal{Q}}(n)\) rank-one terms for every \(\lambda>0\). In (103), each desired product has coefficient one, and every remaining mixed product has positive degree. Hence \(\Phi_{\mathcal{S},\mathcal{Q}}(\lambda)\rightarrow\phi_\mathcal{S}\) as \(\lambda\rightarrow 0\), giving the border-rank bound.

The choice \(\mathcal{Q}=\mathcal{Q}_{\le 0}\) satisfies this hypothesis because every replicated term of nonpositive degree has

\(c_{\mathcal{Q}_{\le 0}}(\mathcal{R}_{ijk})=\sum_{P\subseteq\mathcal{R}_{ijk}}(-1)^{|P|}=0.\) (106)

All remaining replicated terms have positive degree, as do the products in B(S) by the grading condition.

## 7 Stability and retained precision

We now study the approximation error introduced by \(\lambda\) and the sensitivity of the bilinear algorithm to round-off error. The first depends on the remaining mixed products. For the second, we distinguish input sensitivity, which depends on the bilinear map, from amplification of errors in the intermediate vectors, which depends on its factorization. The product of the three factor norms bounds the latter. We compare this product with that of classical multiplication and balance approximation error against round-off error at a fixed working precision.

Bini and Lotti analyzed stability of fast matrix multiplication \[8\], and Bini, Lotti, and Romani studied approximate bilinear algorithms \[9\]. Subsequent analyses quantify the effects of recursion, coefficient magnitudes, and scaling \[17, 4, 16\]. We use the product of spectral norms appearing in the bilinear norm estimates of Ju and Solomonik \[21, Theorem 9.1 and Corollary 9.2\] to bound the propagation of intermediate rounding errors. For centered constructions with distinct part labels, the row Gram matrices of the factors are block diagonal, with each diagonal block equal to a multiple of the identity matrix. Their spectral norms therefore follow directly from these scalars, which depend on the tripartition set, corrections, and parameter exponents.

After grouping the modes into matrix indices, write<tbc>

\(X^{(t)}\in\mathbb{C}^{n^{|V_t|}\times n^{|W_t|}},Y^{(t)}\in\mathbb{C}^{n^{|W_t|}\times n^{|U_t|}},x=(\text{vec}X^{(t)})_{t=1}^m,y=(\text{vec}Y^{(t)})_{t=1}^m.\) (107)

<tbc>The target is the bilinear map

\(\mathcal{M}(x,y)=\big(\text{vec}(X^{(t)}Y^{(t)})\big)_{t=1}^m.\) (108)

In the following analysis, vector norms are Euclidean, matrix norms are spectral, and \(\|\mathcal{L}\|=sup_{\|x\|=\|y\|=1}\|\mathcal{L}(x,y)\|\) for a bilinear map L. The norm inequalities below hold over R and C; the centering matrix _Q_ is real with _Q<sup>T</sup>Q=I_ and **1**_<sup>T</sup>Q_=0.

