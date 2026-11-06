the lifted equation can therefore be checked exactly, as was done for scalar bilinear systems in \[10\]. We focus on the scalar case, where the structure of the lifted equation can be shown explicitly, as a first step towards multivariable systems.

For scalar systems, our contributions are threefold. First, we eliminate the implicit operator. The lifted HJB equation then becomes a Riccati-type equation for a lower-triangular Toeplitz matrix. Second, we show that, under controllability of the linearization and detectability of the cost, this equation has a unique solution with positive diagonal entries. The solution is obtained from the scalar Riccati equation of the linearized problem, followed by a sequence of scalar linear equations. It is a bounded operator whenever the Maclaurin coefficients of the derivative of the value function decay fast enough. Third, we prove that the finite sections of this solution converge exponentially to the derivative of the value function near the origin. Numerical simulations illustrate the results, and Fig. 1 summarizes the approach and the role of the theorems.

## II. PROBLEM STATEMENT

We start from Al’brekht’s 1961 problem \[1\] and specialize it to one state and one input, which is its simplest nonlinear case. Its solution has a closed form, which serves as a benchmark as it tells us what the lifted HJB equation must compute. In this section, we state the problem, list our assumptions, and give the solution.

The system is input-affine,

\(\dot{x}=f(x)+g(x)u,x(0)=x_0\in\mathbb{R},\) (1)

with input \(u\in\mathbb{R}\). We assume that _f_(0)=0 and that _f_ and _g_ are analytic around the origin, with Maclaurin expansions

\(f(x)=\sum_{k=1}^\infty f_kx^k\text{and}g(x)=\sum_{k=0}^\infty g_kx^k.\) (2)

The cost to be minimized is

\(J(x_0,u)=\int_0^\infty\big(q(x(t))+ru^2(t)\big)dt,\) (3)

where _r\>_0 weights the control and the state cost _q_ satisfies the following condition.

**Detectability.** The state cost \(q:\mathbb{R}\rightarrow\mathbb{R}_+\) is nonnegative, and _f_ and _q_ have no common zero other than the origin, i.e., \(q(x)\ge 0\) for all _x_ and _f(x_)=_q(x_)=0 only if _x_=0. In addition, _q_ is analytic around the origin with

\(q(x)=\sum_{k=2}^\infty q_kx^k\text{with}q_2>0.\) (4)

The second part of (4), along with the condition that _f_ and _q_ have no common zero other than the origin, says that the origin is the only rest point of zero cost. This is zero-state detectability of (_f,q_) \[28\]. The condition _q_<sub>2</sub>_\>_0 means that the linearized pair \((\sqrt{q_2},f_1)\) is observable.

Let _V(x_<sub>0</sub>)=inf_<sub>u</sub>J(x_<sub>0</sub>_,u_) be the value function, and let _V<sub>x</sub>_ denote its derivative. Dynamic programming gives

\(min_{u\in\mathbb{R}}\big\{V_x\big(f(x)+g(x)u\big)+q(x)+ru^2\big\}=0.\) (5)

The expression in braces is a convex quadratic in _u_. Its minimizer is the optimal feedback

\(u^*(x)=-\frac{1}{2r}g(x)V_x.\) (6)

Substituting (6) into (5) gives the HJB equation

\(V_xf(x)-\frac{1}{4r}(V_xg(x))^2+q(x)=0.\) (7)

The optimal feedback is known as soon as _V<sub>x</sub>_ is. The rest of the paper is about _V<sub>x</sub>_.

**Controllability.** The linearization of (1) at the origin is \(\dot{x}=f_1x+g_0u\). We assume that it is controllable,

\(g_0\neq 0.\) (8)

**Existence.** Let us define

\(\Delta:=f_1^2+\frac{1}{r}q_2g_0^2.\) (9)

By (4) and (8), \(\Delta>0\). The numbers \(\pm\sqrt{\Delta}\) are the eigenvalues of the Hamiltonian matrix of the linearized problem. The coefficient of _x_<sup>2</sup> in (7) is its Riccati equation,

\(q_2+f_1v-\frac{g_0^2}{4r}v^2=0,v=V_{xx}(0).\) (10)

Its roots are \(v=2rg_0^{-2}(f_1\pm\sqrt{\Delta})\). They are real and have opposite signs, because _q_<sub>2</sub>_\>_0. The positive root, \(v=2rg_0^{-2}(f_1+\sqrt{\Delta})\), gives the closed-loop pole \(f_1-\frac{g_0^2}{2r}v=-\sqrt{\Delta}\). As done by Al’brekht, the recursion shown in this paper starts from the mentioned root.

**Closed-form solution.** The recursion is not needed to find _V<sub>x</sub>_. The HJB equation (7) is quadratic in the single unknown _V<sub>x</sub>_, and it can be solved in closed form. Let

\(l(x):=x^{-2}f(x)^2+r^{-1}x^{-2}q(x)g(x)^2.\) (11)

By (2) and (4), _l_ is analytic around the origin with \(l(0)=\Delta>0\). By (4), _l(x)\>_0 for \(x\neq 0\) wherever \(g(x)\neq 0\). Among the solutions of (7) that are twice differentiable at the origin, exactly one has _V<sub>xx</sub>_(0)_\>_0:

\(V_x=\frac{2r\big(f(x)+x\sqrt{l(x)}\big)}{g(x)^2}.\) (12)

The other one has \(V_{xx}(0)=2rg_0^{-2}(f_1-\sqrt{\Delta})<0\). To see this, note that for \(x\neq 0\) a solution must coincide with one of the two branches \(2r\big(f\pm\sqrt{f^2+qg^2/r}\big)/g^2\), which are distinct because _l\>_0. If _V<sub>xx</sub>_(0) exists, the one-sided slopes at the origin must agree, and this leaves the two analytic functions \(2r(f\pm x\sqrt{l})/g^2\). By (6), the optimal feedback is

\(u^*(x)=-\frac{f(x)+x\sqrt{l(x)}}{g(x)}\)

and the optimal closed-loop system is

\(\dot{x}=f(x)+g(x)u^*(x)=-x\sqrt{l(x)}.\) (13)

On any interval around the origin where \(g\neq 0\), the closed loop in (13) strictly decreases |_x_|. The origin is

