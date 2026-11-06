## 3. Two Grid method

The Galerkin multigrid method belongs to the class of classical multigrid methods and is primarily applicable to symmetric positive definite linear systems _Au=b_. Its simplest form is the two grid method (TGM), which consists of a smoother and a coarse-grid correction. Multi-level schemes such as the V-cycle are realized by recursively cycling the TGM. The specific procedure of the TGM is shown in  1. In this paper, we choose the weighted Jacobi as the smoother, whose update formula is<tbc>

\(u^{(j+1)}=Gu^{(j)}+\omega\mathrm{diag}(A)^{-1}b,\)

<tbc>where _u_<sup>(_j_)</sup> is the iteration vector at the _j_-th step, and<tbc>

\(G=I_n-\omega\mathrm{diag}(A)^{-1}A.\) (3.1)

<tbc>The coarse grid correction is obtained by combining the restriction operator \(I_h^H\) and the prolongation operator \(I_H^h\), where \(I_h^H\) is a rectangular matrix with full row rank. Specifically, we take<tbc>

\(I_h^H=P\otimes P,\) (3.2)

<tbc>where<tbc>

\(P=\left[\begin{array}{ c c c c c c c }
1 & 2 & 1 &  &  &  &  \\
1 & 2 &  & 1 &  &  &  \\
 & \ddots & \ddots &  & \ddots &  &  \\
 &  &  & 1 & 2 & 1
\end{array}\right]\in\mathbb{R}^{[\frac{N}{2}]\times N}.\)

<tbc>The prolongation operator is defined by

\(I_H^h=\left(I_h^H\right)^T=P^T\otimes P^T,\) (3.3)

which defines a Galerkin coarse matrix \(A_H=I_h^HAI_H^h\).

1) **Pre-smoothing:** Apply _j_<sub>1</sub> iterations of _G_ to the system _Au=b_ to obtain _u_<sup>(_j_<sub>1</sub>)</sup><br>
2) **Compute the residual:** _r=b-Au_<sup>(_j_<sub>1</sub>)</sup><br>
3) **Restriction:** \(b_H=I_h^hr\)<br>
4)**Coarse grid equation solving:** Solve the system _A<sub>H</sub>e=b<sub>H</sub>_ exactly to obtain \(\hat{e}\)<br>
5) **Update solution** \(\hat{u}=u^{(j_1)}+I_H^h\hat{e}\)<br>
6) **Post-smoothing:** Starting from \(\hat{u}\), perform _j_<sub>2</sub> iterations using _G_

Take _j_<sub>1</sub>=0, _j_<sub>2</sub>=1. In this setting, the iteration matrix of the TGM is given as follows:

\(E_{TG}=G\left(I_n-I_H^h(I_h^HAI_H^h)^{-1}I_h^HA\right).\) (3.4)

_E<sub>TG</sub>_ is also referred to as the two grid error propagation operator. To characterize its convergence, we introduce the following inner product and the corresponding induced energy norm.

**Definition 3.1.** Let \(\langle u,v\rangle\) be the standard Euclidean inner product, and let \(A=(a_{ij})\in\mathbb{R}^{n\times n}\) be a symmetric positive definite matrix. Define<tbc>

\(\langle u,v\rangle_{0,A}=\langle\mathrm{diag}(A)u,v\rangle,\langle u,v\rangle_{1,A}=\langle Au,v\rangle,\langle u,v\rangle_{2,A}=\langle(\mathrm{diag}(A))^{-1}Au,Av\rangle.\) (3.5)

<tbc>The corresponding energy norms are<tbc>

\(||u||_{0,A}=\sqrt{\langle u,u\rangle_{0,A}},||u||_{1,A}=\sqrt{\langle u,u\rangle_{1,A}},||u||_{2,A}=\sqrt{\langle u,u\rangle_{2,A}}.\) (3.6)

1: Two Grid method

