## A Technical Results for Section 4

This appendix collects technical results used in the proof of our main stability bound (i.e., Theorem 4.6).

### A.1 Vandermonde Bounds

For a set of (distinct and nonzero) points \(\varepsilon_1,\dots,\varepsilon_p\in\mathbb{C}\), consider the \(p\times p\) Vandermonde system

\(\left(\begin{array}{ c c c c c }
1 & 1 & \cdots & 1 \\
\varepsilon_1 & \varepsilon_2 & \cdots & \varepsilon_p \\
\vdots & \vdots &  & \vdots \\
\varepsilon_1^{p-1} & \varepsilon_2^{p-1} & \cdots & \varepsilon_p^{p-1}
\end{array}\right)\left(\begin{array}{ c }
\alpha_1 \\
\alpha_2 \\
\vdots \\
\alpha_p
\end{array}\right)=\left(\begin{array}{ c }
1 \\
0 \\
\vdots \\
0
\end{array}\right).\) (A.1)

Recall from Section 4 that the exact solution to this system is

\(\alpha_j=\prod_{k\neq j}\frac{\varepsilon_k}{\varepsilon_k-\varepsilon_j},1\le j\le p.\) (A.2)

Below, we derive the following:

1. A (relative) error bound for evaluating (A.2) in floating-point arithmetic (Theorem A.1).<tbc>

2. An (exact-arithmetic) perturbation bound for the \(\alpha_j\) (Theorem A.2).

We start with the floating-point error bound, which assumes the same model of floating-point arithmetic used in Section 4 (i.e, \[31, 48\]). Informally, Theorem A.1 implies that, under some mild assumptions, the \(\alpha_j\) can be computed accurately (in a relative sense) by simply evaluating (A.2) directly.

**Proposition A.1.** _Given distinct, nonzero_ \(\varepsilon_1,\dots,\varepsilon_p\in\mathbb{C}\)_, let_

\(\alpha_j=\prod_{k\neq j}\frac{\varepsilon_k}{\varepsilon_k-\varepsilon_j}\text{\textit{for}}1\le j\le p.\)

_Suppose that the approximate quantities_ \(\widehat{\alpha}_1,\dots,\widehat{\alpha}_p\) _are the result of evaluating this expression in floating-point arithmetic, where we assume the following:_

1. _Each_ \(\varepsilon_i\) _is a normalized floating-point number._<tbc>

_2._ _The quotients_ \(\frac{\varepsilon_k}{\varepsilon_k-\varepsilon_j}\) _are evaluated directly and multiplied in an order that guarantees no over/underflow occurs._<tbc>

_3._ \(\frac{2(p-1)\mathbf{u}}{1-\mathbf{u}}<1\)_, where_ **u** _is the unit roundoff._<tbc>

<tbc>_In this case, we have_<tbc>

\(\frac{|\widehat{\alpha}_j-\alpha_j|}{|\alpha_j|}\le 3p\mathbf{u}+O(\mathbf{u}^2).\)

