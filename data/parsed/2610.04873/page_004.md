for all \(m\ge 2\) and \(V_x=2\sum_{m=2}^\infty\pi_m(\mathbf{P})x^{m-1}\). Comparing with (14), the Maclaurin coefficients of _V<sub>x</sub>_ are \(v_{m-1}=2\pi_m(\mathbf{P})\). We collect the anti-diagonal sums in the lower- triangular Toeplitz matrix

\(\unknown:=\left[\begin{array}{ c c c c }
\pi_2(\mathbf{P}) & 0 & 0 & \cdots \\
\pi_3(\mathbf{P}) & \pi_2(\mathbf{P}) & 0 & \cdots \\
\pi_4(\mathbf{P}) & \pi_3(\mathbf{P}) & \pi_2(\mathbf{P}) & \cdots \\
\vdots & \vdots & \vdots & \ddots
\end{array}\right].\) (26)

Many matrices **P** have the same anti-diagonal sums. They all give the same _V<sub>x</sub>_, and \(\unknown\) is what they have in common. The next theorem rewrites the HJB equation (22) and the control law (23) in terms of \(\unknown\) alone. Let us denote \(\mathbf{f}=[f_1,f_2,f_3,\dots]^\top\), \(\mathbf{g}=[g_0,g_1,g_2,\dots]^\top\), and \(\bar{\mathbf{A}}=\mathbf{f}\mathbf{e}_1^\top\).

_Theorem 1:_ Suppose that **A**, **B**, **P**, **Q**, and \(\unknown\) are as in (18), (19), (24), (21), and (26). Under the ansatz (24), the lifted HJB equation (22) is equivalent to<tbc>

\(\Psi^\top\left(\unknown\bar{\mathbf{A}}+\bar{\mathbf{A}}^\top\unknown^\top+\mathbf{Q}-\frac{1}{r}\unknown\mathbf{g}\mathbf{g}^\top\unknown^\top\right)\Psi=0,\) (27)

<tbc>and the control law (23) becomes

\(u^*=-\frac{1}{r}\Psi^\top\unknown\mathbf{g}.\) (28)

The proof is given in Appendix A. Before we use the theorem, we point out what it implies. Equation (27) has the form of an algebraic Riccati equation, \(PA+A^\top P+Q-\frac{1}{r}Pbb^\top P=0\), with \(\unknown\) in the role of _P_. The data are read off the lift where **f** is the first row of **A**, **g** is the second row of **B**, and **Q** is the lifted cost. The unknown is a single sequence, \(\pi_2,\pi_3,\dots\), which, for the solution of Theorem 2, is the sequence of Maclaurin coefficients of _V<sub>x</sub>_ up to the factor two. In our earlier work \[24\], the quadratic term of the lifted equation contained an auxiliary operator that depended on the unknown only implicitly. Here that operator is gone. The quadratic term is \(\unknown\mathbf{g}\mathbf{g}^\top\unknown^\top\), explicit and of rank one, as in the single-input linear-quadratic case; along \(\Psi(x)\) it gives \(\frac{1}{r}(\Psi^\top\unknown\mathbf{g})^2=r\left(u^*\right)^2\), the control cost. The (1,1) entry of the matrix in (27) is \(2f_1\pi_2+q_2-\frac{g_0^2}{r}\pi_2^2\). With \(v=2\pi_2\), this is the Riccati equation (10) of the linearization. The infinite Riccati equation thus contains the finite one as its first entry, and the rest of its entries hold the nonlinear terms.

Two facts explain why the lift produces an equation with a Riccati form rather than something more complicated. First, by (20), the Carleman vector \(\Psi(x)\) is an eigenvector of **A** with eigenvalue _f(x)/x_, and the analogous relation holds for **B**. Thus, the lifted equation depends on **P** only through the series \(\sum_{m=2}^\infty\pi_m(\mathbf{P})x^m\). Second, products of power series are represented by products of lower-triangular Toeplitz matrices. The matrix \(\unknown\) is the Toeplitz matrix of the series \(\sum_{m=2}^\infty\pi_m(\mathbf{P})x^{m-2}\), and for any sequence \(\mathbf{c}=[c_0,c_1,\dots]^\top\) with generating function _c(x_),

\(\Psi^\top\unknown\mathbf{c}=x\left(\sum_{m=2}^\infty\pi_m(\mathbf{P})x^{m-2}\right)c(x).\) (29)

This identity turns every product in the HJB equation into a matrix product; both identities in the proof of Theorem 1 are<tbc>

<tbc>instances of it. We should highlight that (27) is an identity between quadratic forms evaluated along the curve \(\Psi(x)\). It says that every anti-diagonal sum of the matrix in parentheses vanishes, which is one scalar equation per degree. It does not say that the matrix vanishes entry by entry.

Theorem 1 writes the lifted HJB equation in terms of \(\unknown\) alone, but (27) is still infinite-dimensional. The next corollary closes the loop with Section II. The first column of \(\unknown\) defines a function that solves the scalar HJB equation (7), and the lifted feedback (28) is the feedback (6). This is what allows us to compute \(\unknown\) degree by degree in Section IV and to compare its finite sections with _V<sub>x</sub>_ in (12).

_Corollary 1:_ Let \(\unknown\) be a lower-triangular Toeplitz matrix of the form (26) that satisfies (27), and set

\(U(x):=2\Psi^\top\unknown\mathbf{e}_1=2\sum_{m=2}^\infty\pi_m(\mathbf{P})x^{m-1}.\) (30)

Then, \(U(x)=2x^{-1}\Psi^\top\mathbf{P}\Psi\) and the function _U_ satisfies the HJB equation

\(q(x)+U(x)f(x)-\frac{1}{4r}\big(g(x)U(x)\big)^2=0,\) (31)

and the control (28) equals \(u^*=-\frac{1}{2r}g(x)U(x)\), as in (6). Conversely, let _U_ be analytic around the origin with _U_(0)=0 and satisfy (31). Then, the Toeplitz matrix \(\unknown\) whose entries \(\pi_m\) are one half of the coefficient of _x_<sup>_m_-1</sup> in _U_ satisfies (27).

The proof is given in Appendix B. In words, the lifted Riccati-type equation and the scalar HJB equation have the same solutions.

_Remark 1:_ By (24) and the chain rule,

\(V_x=\frac{dV}{d\Psi}\frac{d\Psi}{dx}=x^{-1}V_\Psi^\top\mathbf{D}\Psi=2x^{-1}\Psi^\top\mathbf{P}\Psi=U(x).\) (32)

Thus, the function _U_ in (30) is the derivative of the lifted value function along \(\Psi(x)\). Along the closed loop, (31) and (28) give

\(\dot{V}=V_x\big(f(x)+g(x)u^*\big)=-\Psi^\top\mathbf{Q}\Psi-\frac{1}{r}\Psi^\top\unknown\mathbf{g}\mathbf{g}^\top\unknown^\top\Psi\)<br>
\(=-q(x)-r\left|u^*(x)\right|^2\le 0.\)

This is the Lyapunov inequality one expects from an HJB equation. Moreover, the solution constructed in Theorem 2 has \(\pi_2(\mathbf{P})>0\) by (33), and _U_ is analytic with \(U'(0)=2\pi_2(\mathbf{P})>0\). By Section II, there is only one such solution of the HJB equation. Hence, _U_ is the closed-form _V<sub>x</sub>_ in (12), the closed-loop system is \(\dot{x}=-x\sqrt{l(x)}\) as in (13), the origin is asymptotically stable in the sense of Lyapunov, and _V_ is the value function of the problem. Thus, the positive-diagonal solution of the lifted Riccati-type equation gives the optimal cost while serving as a Lyapunov function.

## IV. EXPONENTIAL CONVERGENCE OF FINITE-SECTION APPROXIMATIONS

By Theorem 1, solving the lifted HJB equation (22) amounts to finding the lower-triangular Toeplitz solution \(\unknown\)

