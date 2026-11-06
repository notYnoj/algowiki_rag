therefore asymptotically stable under _u_<sup>∗</sup>, with linearization \(\dot{x}=-\sqrt{\Delta}x\). The function \(V(x)=\int_0^xV_x(s)ds\) is positive definite. Since _f_, _g_ and _l_ are analytic around the origin with \(g(0)=g_0\neq 0\) and \(l(0)=\Delta>0\), the function _V<sub>x</sub>_ in (12) is analytic around the origin:

\(V_x=\sum_{k=1}^\infty v_kx^k,x\in(-\rho,\rho).\) (14)

Here \(\rho\) is any number below the radius of convergence. By Cauchy’s estimate, there is a constant \(M=M(\rho)\) such that

\(|v_k|\le M\rho^{-k},k\ge 1.\) (15)

The radius of convergence is set by the complex singularities of _V<sub>x</sub>_, such as the complex zeros of _g_ and of _l_. It can be smaller than the real interval on which (12) is defined. We return to this point in Section IV.

While the closed form solves the scalar problem, it does not show how the coefficients _v<sub>k</sub>_ fit together. In the next section, we lift the HJB equation by Carleman linearization. We then show that all of the coefficients _v<sub>k</sub>_ solve a single infinite-dimensional Riccati-type equation whose first entry is the Riccati equation (10).

## III. HJB EQUATION FOR CARLEMAN LINEARIZATION

Carleman linearization replaces the scalar state _x_ by the sequence of its powers \[12\], \[13\]. In the new variables, the nonlinear system (1) becomes an infinite-dimensional bilinear system. We first write this system down and then lift the HJB equation along with it. The Carleman lifting operator is the infinite-dimensional nonlinear map

\(\Psi(x):=\text{col}[x,x^2,x^3,\dots],\) (16)

where col\[_v,w_\] stacks the column vector _v_ on top of the vector _w_. Along a trajectory of (1), each power satisfies \(\frac{d}{dt}x^m=mx^{m-1}\big(f(x)+g(x)u\big)\). Expanding _x_<sup>_m_-1</sup>_f(x_) and _x_<sup>_m_-1</sup>_g(x_) by (2) gives the Carleman linearization

\(\dot{\Psi}=\mathbf{D}\big(\mathbf{A}\Psi+(\mathbf{B}\Psi+\mathbf{b}_0)u\big),\) (17)

where the operators are defined by

\(\mathbf{A}=\left[\begin{array}{ c c c c c }
f_1 & f_2 & f_3 & \cdots &  \\
0 & f_1 & f_2 & \cdots &  \\
0 & 0 & f_1 & \cdots &  \\
\vdots & \vdots & \vdots & \ddots &  \\
\end{array}\right],\mathbf{B}=\left[\begin{array}{ c c c c c c }
g_1 & g_2 & g_3 & \cdots &  \\
g_0 & g_1 & g_2 & \cdots &  \\
0 & g_0 & g_1 & \cdots &  \\
\vdots & \vdots & \vdots & \ddots &  \\
\end{array}\right]\) (18)

\(\mathbf{D}=\left[\begin{array}{ c c c c c }
1 & 0 & 0 & \cdots &  \\
0 & 2 & 0 & \cdots &  \\
0 & 0 & 3 & \cdots &  \\
\vdots & \vdots & \vdots & \ddots &  \\
\end{array}\right],\mathbf{b}_0=g_0\mathbf{e}_1=\left[\begin{array}{ c }
g_0 \\
0 \\
0 \\
\vdots
\end{array}\right]\) (19)

and \(\mathbf{e}_1=[1,0,0,\dots]^\unknown\). The structure of these matrices is the point of this section. **A** is upper-triangular Toeplitz, with the Maclaurin coefficients of _f_ along its rows. **B** is upper Hessenberg Toeplitz, with the coefficients of _g_ along its rows<tbc>

<tbc>and _g_<sub>0</sub> on the subdiagonal. On the lifted state they act as multiplication operators:

\(\mathbf{A}\Psi=x^{-1}f(x)\Psi,\mathbf{B}\Psi+\mathbf{b}_0=x^{-1}g(x)\Psi,\) (20)

because the _m_-th entries of the two sides are _x_<sup>_m_-1</sup>_f(x_) and _x_<sup>_m_-1</sup>_g(x_). These two identities are all we need from the lift. In this section, we study the HJB equation of (17), and in Section IV we prove exponential convergence of its finite-section approximations; see Figure 1.

The cost lifts in the same way. By (4),

\(q(x)=\Psi^\top\mathbf{Q}\Psi,\) (21)

where \(\mathbf{Q}=[q(i,j)]_{i,j=1}^\infty\) is the symmetric tridiagonal matrix with _q(i,i_)=_q_<sub>2_i_</sub>_,q(i,i_+1)=_q(i_+1_,i_)=_q_<sub>2_i_+1</sub>/2 for \(i\ge 1\), and _q(i,j_)=0 otherwise. Following the quadratization procedure in \[24\], we view the value function as a function of \(\Psi\) and write \(V_\Psi\) for its gradient. The HJB equation for the lifted system (17) is then

\(V_\Psi^\top\mathbf{DA}\Psi-\frac{1}{4r}\big(V_\Psi^\top\mathbf{D}(\mathbf{B}\Psi+\mathbf{b}_0)\big)^2+\Psi^\top\mathbf{Q}\Psi=0,\) (22)

and the corresponding optimal control law is

\(u^*=-\frac{1}{2r}(\mathbf{B}\Psi+\mathbf{b}_0)^\top\mathbf{D}V_\Psi.\) (23)

By the chain rule, \(V_x=V_\Psi^\top\frac{d\Psi}{dx}=x^{-1}V_\Psi^\top\mathbf{D}\Psi\). Together with (20), this shows that on the lifted state (22) and (23) are the HJB equation (7) and the feedback (6) of Section II. Lifting therefore leaves the HJB equation unchanged on the lifted state and expresses it through the lifted operators, whose structure is exploited next.

We look for a solution whose gradient is linear in \(\Psi\),

\(\mathbf{D}V_\Psi=2\mathbf{P}\Psi\) (24)

for some infinite matrix \(\mathbf{P}=[p(i,j)]_{i,j=1}^\infty\). Then, \(V_x=2x^{-1}\Psi^\top\mathbf{P}\Psi\). Since \(\Psi^\top\mathbf{P}\Psi=\sum_{i,j=1}^\infty p(i,j)x^{i+j}\), the matrix **P** enters only through the sums of its anti-diagonal entries,

\(\pi_m(\mathbf{P})=\pi_m(\mathbf{P}^\top)=\sum_{i=1}^{m-1}p(i,m-i)\) (25)

