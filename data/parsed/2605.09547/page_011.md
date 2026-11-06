For matrices \(\mathbf{A}\in\mathbb{R}^{m\times n}\), vectors \(b\in\mathbb{R}^n\), \(c\in\mathbb{R}^m\), and upper bounds \(u\in\mathbb{R}^m\), this IPM solves linear programs of the form<tbc>

\(min_{x\in\mathbb{R}^m:\mathbf{A}^\top x=b0\le x_e\le u_e\forall e\in[m]}c^\top x.\) (4)

<tbc>The central path method of \[LS14\] repeatedly solves the following minimization problem. In each iteration, parameter \(\mu\in\mathbb{R}_{>0}\) is decreased, and then the new minimizer \(x_\mu\) is found by performing one Newton-step from the old minimizer \(x_{\mu^\prime}\).

\(x_\mu:=argmin_{\mathbf{A}^\top x=b}f_\mu(x),f_\mu(x):=c^\top x+\mu\sum_{i=1}^m\tau(x)_e\phi_e(x_e),\) (5)

where \(\tau\in\mathbb{R}_{>0}^m\) and \(\phi_e:\mathbb{R}_{>0}\rightarrow\mathbb{R}\) is defined as \(\phi_e(z)=-log(u_e-z)-log(z)\). (For simplicity, we also write \(\phi(x)\in\mathbb{R}^m\) for the vector with entries \(\phi_e(x_e)\) for _e_=1_,..,m._) Note that as _x<sub>e</sub>_ approaches 0 or capacity _u<sub>e</sub>_, the \(\phi_e(x_e)\) term goes to \(\infty\), which keeps the minimizer \(x_\mu\) within the feasible region. As \(\mu\rightarrow 0\), the term \(c^\top x\) starts to dominate; thus \(x_\mu\) converges towards the optimal solution of the linear program for \(\mu\rightarrow\infty\). Here \(\tau\in\mathbb{R}^m\) is a weight measuring the importance of each row of **A**. \[LS14\] chooses \(\tau\) to be the regularized _l<sub>p</sub>_ Lewis-weight for \(p=1-\frac{1}{4log(4m/n)}\). This is defined to be the solution to

\(\tau=\sigma(\mathbf{T}^\frac{1}{2}-\frac{1}{p}(\Phi''(x))^{-\frac{1}{2}}\mathbf{A})+\frac{n}{m},\) (6)

where \(\Phi''(x)\) is a diagonal matrix with the 2nd derivatives \(\phi''_e(x_e)=1/x_e^2-1/(u_e-x_e)^2\) on the diagonal for _e_=1_,...,m_.

The curve \(x_\mu\) for \(\mu\in(\infty,0)\) is referred to as the central path. It turns out that it is easy to find a point _x_ close to \(x_\mu\) on this path for large \(\mu\) (see Section 6 for details). Starting from this point, we iteratively take steps to decrease \(\mu\) and move _x_ closer to the new minimizer \(x_\mu\).

To do this, we must define a measure for how far _x_ is from \(x_\mu\). To satisfy \(x=argmin_{\mathbf{A}^\top x=b}f_\mu(x)\) (eq. (5)), optimality conditions tell us that we need \(\mathbf{A}^\top x=b\) and the gradient \(\nabla f_\mu(x)=c+\mu\mathbf{T}\phi'(x)\) must be orthogonal to the feasible hyperplane \(\{x|\mathbf{A}^\top x=b\}\); i.e., \(c+\mathbf{A}y+\mu\mathbf{T}\phi'(x)=0\) for some \(y\in\mathbb{R}^n\). We can rewrite this as \(s=\mu\mathbf{T}\phi'(x)=0\), where _s_:=_c_+**A**_y_. Now, to define what it means to follow the central path, we say that a triple \((x,s,\mu)\) is _central_ if

\(\mathbf{A}^\top x=b,s=\mathbf{A}y+c,s+\mu\mathbf{T}\phi'(x)=0.\) (7)

As we cannot expect to be exactly centered, we measure centrality via the following potential function:

\(\Psi\left(\frac{s+\mu\tau(x)\phi'(x)}{\mu\tau(x)\sqrt{\phi''(x)}}\right):=\sum_{e=1}^mcosh\left(\lambda\left(\frac{s_e+\mu\tau(x)_e\phi'_e(x_e)}{\mu\tau(x)_e\sqrt{\phi''_e(x_e)}}\right)\right),\) (8)

where \(\lambda=O(logn)\). Note that the numerator is 0 (which is equivalent to minimizing (8)) if and only if (7) is satisfied.

Our goal is now to take steps where we alternate between decreasing \(\mu\) (which increases (8)) and updating (_x,y,s_) such that (8) decreases again. This way we approximately trace the curve \(x_\mu\).

In the central path method by \[BLL<sup>+</sup>21\], the improvements in each iterations are of the following form. Given \((x^{t-1},s^{t-1},\mu^{t-1})\) at iteration number _t_-1, the next values for iteration _t_ are given by

\(x^t\leftarrow x^{t-1}+\delta_x^t,s^t\leftarrow s^{t-1}+\delta_s^t,\mu^t\leftarrow\left(1-\frac{1}{\widetilde{O}(\sqrt{n})}\right)\mu^{t-1}.\)

To compute the movements \(\delta_x^t,\delta_s^t\) we first calculate the weights \(\tau^t\in\mathbb{R}^m\) of our current point _x_<sup>_t_-1</sup>, and set the vector \(g^t\in\mathbb{R}^m\) to be the gradient of (8), which intuitively moves _x_ as close as possible to \(x_\mu\) on the central path. \[BLL<sup>+</sup>21\] have shown that instead of exact calculation of \(\tau^t\), it suffices to compute weight \(\overline{\tau^t}\)<tbc>

