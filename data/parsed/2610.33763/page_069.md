Using the estimate of \(\mathcal{G}(t,\zeta)\) given in (5.61) and assumptions of Theorem 5.3, we find that<tbc>

\(max_{0\le t\le T}|\mathcal{I}(w_1(t))-\mathcal{I}(w_2(t))|\le TQ_0Q_2max_{0\le t\le T}|w_1(\tau)-w_2(\tau)|,\)

<tbc>which implies<tbc>

\(\|\mathcal{I}(w_1)-\mathcal{I}(w_2)\|_{C([0,T])}\le TQ_0Q_2\|w_1-w_2\|_{C([0,T])}.\)

<tbc>This demonstrates that the mapping I(_w(t_)) is a contraction for \(T<\frac{1}{Q_0Q_2}\), by applying the Banach fixed-point theorem, which guarantees the unique existence of _w(t_). Since \(w\in C([0,T])\), we have

\(\|w\|_{C([0,T])}\le Q,\)

where _Q_ is a constant.

To show the existence of a solution for the second-ISP, we will verify the continuity of<tbc>

\(u(x,y,t),u_{xx}(x,y,t),u_{yy}(x,y,t),\text{and}_G\mathcal{D}_t^{(\varrho)}u(x,y,t).\)

<tbc>First, note that the norm estimate for _f(x,y,t_) in the function space \(C^{0,2,2}(\bar{\Omega})\) is given as follows

\(\|f\|_{C^{0,2,2}(\bar{\Omega}))}^2=\int_0^T\|f\|_{C^2([0,1]\times[0,1])}^2dt\)<br>
\(=\int_0^T\sum_{j=1}^\infty\sum_{k=1}^\infty|f_{j,k}(t)|^2dt\)<br>
\(=\sum_{j=1}^\infty\sum_{k=1}^\infty\|f_{j,k}(t)\|_{C^2([0,T])}^2.\)

Due to Young’s inequality for integral convolution and using Eq. (42) from \[13\], we obtain

\(\big\|\int_0^t\mathbf{V}_{j,k}(t-\tau)f_{j,k}(\tau)d\tau\big\|_{C^2([0,T])}^2\le\big(\int_0^T\mathbf{V}_{j,k}(t)dt\big)^2\int_0^T|f_{j,k}(t)|^2dt\)<br>
\(\le\frac{1}{\lambda_{j,k}^2}\int_0^T|f_{j,k}(t)|^2dt.\) (5.63)

By virtue of Lemmas 5.1, 5.3, and inequality (5.63), we have

\(|U_{j,k}(t)|\le\frac{C_0}{|\lambda_{j,k}|^2}\big(\|\psi^{(iv)}\|_{C^4([0,1]\times[0,1])}+Q\|f_{j,k}(t)\|_{C^2([0,T])}\big).\) (5.64)

Based on inequality (5.64), the uniform convergence of _u(x,y,t_), defined by Eq. (5.23), is bounded. Therefore, applying the WMT established the continuity of _u(x,y,t_).

We now proceed to demonstrate the continuity of the second partial derivatives, _u<sub>xx</sub>(x,y,t_) and _u<sub>yy</sub>(x,y,t_). Using the relationships established in Eqs. (5.64) and<tbc>

