where the constant is obtained by a Riemann-sum argument applied to

\(\sum_{|n|>N}K_0^2x_n^{2q+2}[(-1)^nA+B]^2,\)

split by parity (see the proof of Theorem 4.1), using \(K_0^2=1/2\). The formula (18) replaces Theorem 2 of \[2\]: the constant \(2^{2q+3}/\pi^{2q+3}\) stated there must be replaced by \(2^{2q+2}/\pi^{2q+2}\), in accordance with \(K_0^2=1/2\) rather than \(1/\pi\), and the boundary directions entering the constant _A_ there involve an extraneous angle \(2\theta-\beta\); the corrected constants are (17).

The approximation (15) has a serious drawback: it assumes the boundary values \(f_k(\pm 1)\) to be known in advance, while in many applications they are not. In the next two sections we develop the tools needed to compute them from the generalized Fourier coefficients themselves.

## 2 Block Vandermonde matrices

In this section, we study the algebraic structure of the coefficient matrix arising in the linear system used to approximate the reduced boundary values.

**Definition 2.1.** Let \(q\in\mathbb{N}\), and let \(\alpha_1,\dots,\alpha_{2q}\), \(\beta_1,\dots,\beta_{2q}\), and _x_<sub>1</sub>_,...,x_<sub>2_q_</sub> be complex numbers. We define the _block Vandermonde matrix of order_ 2_q_ to be the following \(2q\times 2q\) matrix:

\(\Lambda=\left(\begin{array}{ c c c c c c c c c c c }
\alpha_1 & \alpha_1x_1 & \cdots & \alpha_1x_1^{q-1} & \beta_1 & \beta_1x_1 & \cdots & \beta_1x_1^{q-1} \\
\alpha_2 & \alpha_2x_2 & \cdots & \alpha_2x_2^{q-1} & \beta_2 & \beta_2x_2 & \cdots & \beta_2x_2^{q-1} \\
\vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
\alpha_{2q} & \alpha_{2q}x_{2q} & \cdots & \alpha_{2q}x_{2q}^{q-1} & \beta_{2q} & \beta_{2q}x_{2q} & \cdots & \beta_{2q}x_{2q}^{q-1}
\end{array}\right).\) (19)

Let<tbc>

\(V_q=\left(x_i^{j-1}\right)_{1\le i\le 2q,1\le j\le q}\)

<tbc>denote the rectangular \(2q\times q\) Vandermonde matrix, and let<tbc>

\(D_\alpha=\text{diag}(\alpha_1,\dots,\alpha_{2q}),D_\beta=\text{diag}(\beta_1,\dots,\beta_{2q}).\)

<tbc>Then<tbc>

\(\Lambda=\left(D_\alpha V_q|D_\beta V_q\right)=BC,B=\left(D_\alpha|D_\beta\right),C=\left(\begin{array}{ c c }
V_q & 0 \\
0 & V_q
\end{array}\right).\) (20)

<tbc>Here,<tbc>

\(B\in\mathbb{C}^{2q\times 4q},C\in\mathbb{C}^{4q\times 2q}.\)

<tbc>For a subset \(T\subseteq[2q]:=\{1,\dots,2q\}\), write<tbc>

\(T=\{t_1<\cdots<t_m\},m=|T|,\)

<tbc>and define the square Vandermonde matrix associated with _T_ by<tbc>

\(V_T=\left(x_{t_i}^{j-1}\right)_{1\le i,j\le m}.\)

<tbc>Its determinant is

\(\text{det}(V_T)=\prod_{1\le i<j\le m}\left(x_{t_j}-x_{t_i}\right).\)

The factorization (20) allows us to compute the determinant of \(\Lambda\) systematically by means of the Cauchy-Binet formula.

