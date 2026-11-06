<tbc>of the Riccati-type equation (27). In this section, we solve this equation by a recursion of scalar equations, and we show that the finite-sections of the solution converge exponentially to _V<sub>x</sub>_ near the origin.

_Theorem 2:_ Suppose that the system (1) with _f_, _g_ and _q_ satisfying (2), (4) and (8), and let \(\Delta>0\) be as in (9). Then, the Riccati-type equation (27) has exactly one lower- triangular Toeplitz solution \(\unknown\) with positive diagonal entries, where its diagonal entry is<tbc>

\(\pi_2(\mathbf{P})=rg_0^{-2}(f_1+\sqrt{\Delta}),\) (33)

<tbc>and its remaining entries \(\pi_{m+2}(\mathbf{P})\), for \(m\ge 1\), are given recursively by

\(\pi_{m+2}(\mathbf{P})=(2\sqrt{\Delta})^{-1}\big(q_{m+2}\)<br>
\(+2\sum_{k=0}^{m-1}\big(f_{m-k+1}-g_0g_{m-k}\pi_2(\mathbf{P})/r\big)\pi_{k+2}(\mathbf{P})\)<br>
\(-\frac{1}{r}\sum_{n=1}^{m-1}\sum_{j=0}^n\sum_{j^\prime=0}^{m-n}g_{n-j}g_{m-n-j^\prime}\pi_{j+2}(\mathbf{P})\pi_{j^\prime+2}(\mathbf{P})\big).\) (34)

Moreover, \(2\pi_m(\mathbf{P})=v_{m-1}\) for all \(m\ge 2\), where _v<sub>k</sub>_ are the Maclaurin coefficients of _V<sub>x</sub>_ in (14).

The proof is given in Appendix C. The recursion deserves a closer look. Its first equation, the case _m_=0, is the Riccati equation (10) of the linearization, and (33) is its positive solution. Every later equation is linear in the new unknown \(\pi_{m+2}(\mathbf{P})\), and the coefficient in front of it is always the same number, \(-2\sqrt{\Delta}\), which is twice the closed-loop pole of Section II. The right-hand side involves only the data _f<sub>k</sub>_, _g<sub>k</sub>_, _q<sub>k</sub>_ and the entries already computed. This is Al’breht’s recursion for the scalar case, with one difference: _here it is read off a single matrix equation, degree by degree, rather than derived anew at each degree_. Two consequences follow. Existence and uniqueness of the solution are decided entirely by the first equation, since \(\Delta>0\) makes every later pivot nonzero. And, the first _N_ equations involve only \(\pi_2(\mathbf{P}),\dots,\pi_{N+1}(\mathbf{P})\). Therefore, truncating the equation and truncating the solution give the same result. The finite-section of the solution is the exact solution of the finite-section. No truncation error is introduced by the recursion.

Let us consider the finite-section of order \(N\ge 1\),<tbc>

\(\unknown_N=\left[\begin{array}{ c c c c c c }
\pi_2(\mathbf{P}) & 0 & 0 & \cdots & 0 \\
\pi_3(\mathbf{P}) & \pi_2(\mathbf{P}) & 0 & \cdots & 0 \\
\pi_4(\mathbf{P}) & \pi_3(\mathbf{P}) & \pi_2(\mathbf{P}) & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \ddots \\
\pi_{N+1}(\mathbf{P}) & \pi_N(\mathbf{P}) & \pi_{N-1}(\mathbf{P}) & \cdots & \pi_2(\mathbf{P})
\end{array}\right],\) (35)

<tbc>of the matrix \(\unknown\) in (26), and define

\(U_N(x)=2\Psi_N^\top\unknown_N\mathbf{e}_1,\) (36)

where \(\Psi_N=[x,x^2,\dots,x^N]^\top\). By Theorem 2, \(U_N(x)=\sum_{k=1}^Nv_kx^k\) is the Taylor polynomial of degree _N_ of _V<sub>x</sub>_. The next theorem gives the rate at which _U<sub>N</sub>_ converges to _V<sub>x</sub>_.

_Theorem 3:_ Suppose that the system (1) with _f_, _g_ and _q_ satisfying (2), (4) and (8), and let _V<sub>x</sub>_ be the solution (12) of the HJB equation (7). Let \(\pi_m(\mathbf{P})\), for \(m\ge 2\), be as in (33) and (34), and let \(\unknown_N\) and _U<sub>N</sub>_ be as in (35) and (36). Then,

\(|U_N(x)-V_x|\le M(1-|x|/\rho)^{-1}|x/\rho|^N\) (37)

for all \(x\in(-\rho,\rho)\) and \(N\ge 1\), where _M_ and \(\rho\) are the constants in (15).

The proof is given in Appendix D. The bound is exponential in _N_ with ratio \(|x|/\rho\). Each additional row of \(\unknown_N\) reduces the error by this factor. The constant \(\rho\) is any number below the radius of convergence of _V<sub>x</sub>_, and, as noted in Section II, that radius is set by the complex singularities of _V<sub>x</sub>_. It can be smaller than the real interval on which (12) is defined, in which case the finite-sections converge only on \((-\rho,\rho)\) even though _V<sub>x</sub>_ is defined beyond it. The truncated feedback \(u_N^*(x):=-\frac{1}{r}g(x)U_N(x)\) inherits the bound with an extra factor |_g(x_)|/(2_r_).

The state matrix **DA** arising in the Carleman linearization (17) is unbounded, whereas the Riccati-type solution \(\unknown\) of the corresponding HJB equation need not be. In fact, as shown in the following remark, \(\unknown\) is a bounded operator whenever the Maclaurin coefficients of _V<sub>x</sub>_ exhibit sufficiently fast decay. This distinction highlights that the unboundedness of the lifted dynamics does not preclude the existence of a well-behaved solution to the associated HJB equation.

_Remark 2:_ For an infinite matrix \(\mathbf{C}=[c(i,j)]_{i,j=1}^\infty\), define its Schur norm by<tbc>

\(\|\mathbf{C}\|_\mathcal{S}=max\left\{sup_{i\ge 1}\sum_{j=1}^\infty|c(i,j)|,sup_{j\ge 1}\sum_{i=1}^\infty|c(i,j)|\right\}.\)

<tbc>Suppose that the radius of convergence of _V<sub>x</sub>_ in (14) exceeds one, and choose \(\rho>1\) in (15). Since \(\unknown\) is lower-triangular Toeplitz, every column sum equals \(\sum_{m=2}^\infty|\pi_m(\mathbf{P})|\), and by \(2\pi_m(\mathbf{P})=v_{m-1}\) and (15),

\(\|\unknown\|_\mathcal{S}=\sum_{m=2}^\infty|\pi_m(\mathbf{P})|\le\frac{M}{2}\sum_{m=2}^\infty\rho^{-(m-1)}=\frac{M}{2(\rho-1)}.\)

By the Schur test, \(\unknown\) is then a bounded operator on \(\ell^p\) for every \(1\le p\le\infty\), where \(\ell^p\) is the Banach space of _p_- summable sequences \(\{c(k)\}_{k=1}^\infty\) with its standard norm. The threshold one reflects the choice of unit weights. On the weighted space with norm \(\|c\|_{p,\sigma}:=\big(\sum_{k=1}^\infty|c(k)|^p\sigma^{kp}\big)^{1/p}\) for \(1\le p<\infty\) and \(\|c\|_{\infty,\sigma}=sup_{k\ge 1}|c(k)|\sigma^k\), the same computation shows that \(\unknown\) is bounded for every \(0<\sigma<\rho\).

## V. SIMULATIONS

In the previous sections, we showed that the solution of the lifted HJB equation is obtained from one Riccati equation followed by a sequence of linear scalar equations. We also showed that the finite sections _U<sub>N</sub>_ for \(N\ge 1\) in (36) converge exponentially to the solution _V<sub>x</sub>_ of the HJB equation for \(|x|<\rho\), where the convergence radius \(\rho\) is related to the Maclaurin series of _V<sub>x</sub>_ in Theorem 3. To show the accuracy<tbc>

