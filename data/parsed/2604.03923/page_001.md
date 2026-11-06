# Error control technique of quadrature-based algorithms for the action of real powers of a Hermitian positive-definite matrix

**Abstract**

This study considers quadrature-based algorithms to compute \(A^\alpha b\), the action of a real power of a Hermitian positive- definite matrix _A_ on a vector **_b_**. In these algorithms, the computation of an integral representation of \(A^\alpha b\) is reduced to solving several tens or hundreds of shifted linear systems. Current approaches usually analyze the quadrature discretization error, but rarely take into account the additional error introduced by solving these shifted linear systems with iterative solvers. Here, we bound this error with the residual of the approximated solution of these linear systems. This allows the derivation of a stopping criterion for iterative solvers to keep the error of \(A^\alpha b\) below a prescribed error tolerance. Numerical results demonstrate that the proposed criterion enables the computation of \(A^\alpha b\) within prescribed tolerance limits.

_Keywords:_ matrix function, matrix fractional power, numerical quadrature, error control

### 1. Introduction

We consider the action of the matrix real power on a vector \(b\in\mathbb{C}^n\), given by \(A^\alpha b\) where the matrix \(A\in\mathbb{C}^{n\times n}\), is raised to the power of \(\alpha\), a real number. The matrix real power is defined via the matrix exponential exp(_X_):=<br>
\(I+X+X^2/2!+X^3/3!+\cdots\) (\(X\in\mathbb{C}^{n\times n}\)) and the matrix principal logarithm. The matrix logarithm is any matrix \(Y\in\mathbb{C}^{n\times n}\) that satisfies exp(_Y_)=_A_. If all the eigenvalues of _Y_ are contained in \(\{z\in\mathbb{C}:|\mathfrak{I}(z)|<\pi\}\), then _Y_ is called the principal logarithm of _A_ and is denoted log(_A_). The principal matrix real power is then defined as \(A^\alpha=exp(\alpha log(A))\), [1]. When \(0<\alpha<1\), \(A^\alpha\) admits the following integral representation [1, Eq. (1.4)]:

\(A^\alpha=\frac{sin(\alpha\pi)}{\alpha\pi}A\int_0^\infty(t^{1/\alpha} I+A)^{-1}dt(0<\alpha<1).\) (1)

Since \(A^\alpha=A^{[\alpha]}A^{\alpha-[\alpha]}\) holds for any real \(\alpha\), we focus on the cases where \(0<\alpha<1\) entails no loss of generality. Applications of the form of \(A^\alpha b\) arise in various scientific computing situations, e.g., numerical methods used for fractional differential equations [2, 3] and the computation of weighted matrix geometric means [4].

Although several computational methods for computing \(A^\alpha b\) exist, we here focus on quadrature-based algorithms. In these algorithms, Equation (1) is discretized using a suitable change of variables and quadrature formulas, such as the Gauss–Jacobi (GJ) quadrature [5, 4] and the double-exponential (DE) formula [6]. This gives the approximation

\(A^\alpha b\approx\frac{sin(\alpha\pi)}{\alpha\pi}\sum_{k=1}^mw_kA(t_k^{1/\alpha} I+A)^{-1}b,\) (2)

where \(t_k\ge 0\) are quadrature nodes and _w<sub>k</sub>_ are the corresponding weights. An advantage of quadrature-based algorithms is that, for large sparse matrices, they enable \(A^\alpha b\) to be computed without explicitly forming \(A^\alpha\). Moreover,

<sup>∗</sup>Corresponding author

Motohiro Otsuka<sup>a,∗</sup>, Fuminori Tatsuoka<sup>b</sup>, Tomohiro Sogabe<sup>a</sup>, Kota Takeda<sup>a</sup>, Shao-Liang Zhang<sup>a</sup>

<sup>_a_</sup>_Department of Applied Physics, Graduate School of Engineering, Nagoya University, Furo-cho, Chikusa-ku, Nagoya, Aichi, 464-8603, Japan_

<sup>_b_</sup>_Corporate Research and Development Division, IHI Corporation, 1 Shin-nakahara-cho, Isogo-ku, Yokohama, 235-8501, Japan_

