where

\(g_0^{(\alpha)}=1,g_{k+1}^{(\alpha)}=\left(1-\frac{\alpha+1}{k+1}\right)g_k^{(\alpha)},k\ge 0.\) (8.4)

This recurrence can be rewritten in closed form as

\(g_k^{(\alpha)}=(-1)^k\genfrac(){pt}{2}{\alpha}{k},k\ge 0,\) (8.5)

where

\(\genfrac(){pt}{2}{\alpha}{k}=\frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}\)

denotes the generalized binomial coefficient.

**Proposition 8.1** _Let_ \(\alpha\in(1,2)\) _and_ \(g_k^{(\alpha)}\) _be defined as in_ (8.4)_. Then we have_

\(\left\{\begin{array}{ c c }
g_0^{(\alpha)}=1, & g_1^{(\alpha)}=-\alpha, \\
\sum_{k=0}^\infty g_k^{(\alpha)}=0, & \sum_{k=0}^ng_k^{(\alpha)}<0,
\end{array}\right.\)

When combined with the variable diffusion coefficient _a(x_), the spatial discretization for the fractional diffusion term at time level _m_ becomes

\(a(x)\mathcal{D}_x^\alpha u(x,t)\big|_{x=x_i,t=t_m}=\frac{a(x_i)}{(\Delta x)^\alpha}\sum_{k=0}^{i+1}g_{i-k+1}^{(\alpha)}u(x_k,t_m)+\mathcal{O}(\Delta x).\) (8.6)

Finally, by coupling the \(\theta\)-method \[101\] to discretize the temporal derivative in (8.2) with the approximation in (8.6), we obtain the following time-stepping scheme

\(\frac{u_i^{(m+1)}-u_i^{(m)}}{\Delta t}=\theta\left(\frac{a(x_i)}{(\Delta x)^\alpha}\sum_{k=0}^{i+1}g_k^{(\alpha)}u_{i-k+1}^{(m+1)}\right)+(1-\theta)\left(\frac{a(x_i)}{(\Delta x)^\alpha}\sum_{k=0}^{i+1}g_k^{(\alpha)}u_{i-k+1}^{(m)}\right)+f_i^{(m,\theta)},\) (8.7)

where \(0\le\theta\le 1\) is a weighting parameter, \(u_i^{(m)}\) approximates _u(x<sub>i</sub>,t<sub>m</sub>_), and \(f_i^{(m,\theta)}=\theta f(x_i,t_{m+1})+(1-\theta)f(x_i,t_m)\). The value of \(\theta\) determines the nature of the method: \(\theta=0\) corresponds to the Forward Euler method, \(\theta=1\) yields the Backward Euler method, and \(\theta=\frac{1}{2}\) gives the Crank-Nicolson scheme.

By defining \(u_N^{(m)}=\left[u_i^{(m)}\right]_{i=1,\dots,N}^T\), that is the numerical approximation of the solution _u(x,t<sub>m</sub>_) at all points of the interior spatial grid _x<sub>i</sub>,i_=1_,...,N_, and accordingly, the vector \(f_N^{(m,\theta)}=\left[f_i^{(m,\theta)}\right]_{i=1,\dots,N}^T\), and by multiplying both sides of (8.7) by \(\Delta t\) and simplifying, we obtain<tbc>

\(u_n^{(m+1)}-u_n^{(m)}=\theta G_{\alpha,N}u_N^{(m+1)}+(1-\theta)G_{\alpha,N}u_N^{(m)}+\Delta tf_N^{(m,\theta)},m=0,\dots,M-1,\)

<tbc>where<tbc>

\(G_{\alpha,N}=\gamma\mathcal{D}_N(a)\overline{G_{\alpha,N}},\) (8.8)

