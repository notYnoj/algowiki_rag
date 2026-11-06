\(\text{DCMCF}_\text{env}:\mathrm{max}\gamma\)<br>
\((1),(2),\) (17)

\(\sum_{a\in p}d_a^{pk}-\frac{x_p^k}{u_p^k}d^k\le 0\forall k\in K,p\in P^k,\) (18)

\(\frac{x_p^k}{u_p^k}\frac{c_a-l_a}{c_a-l_a}-d_a^{pk}\le 0\forall k\in K,p\in P^k,a\in p,\) (19)

\(\frac{\frac{x_p^k}{u_p^k}}{c_a-l_a_p^k-\frac{(u_a-l_a_p^k)}{u_a-(y_a-b^kx_p^k)}b^kx_p^k}-d_a^{pk}\le 0\forall k\in K,p\in P^k,a\in p,\) (20)

\(\frac{(\frac{x_p^k}{u_p^k})^2}{c_a\frac{x_p^k}{u_p^k}-y_a+(1-\frac{x_p^k}{u_p^k})u_a}-d_a^{pk}\le 0\forall k\in K,p\in P^k,a\in p,\) (21)

\(x_p^k\ge 0\forall k\in K,p\in P^k,\) (22)

\(x_p^k\le u_p^k\forall k\in K,p\in P^k,\) (23)

\(y_a\le u_a\forall k\in K,p\in P^k,a\in p,\) (24)

\(y_a\ge b^kx_p^k+l_{ap}^k\forall k\in K,p\in P^k,a\in p,\) (25)

where Constraints (18) represent the relaxed delay constraint and Constraints (19), (20) and (21) represent the respective contributions of functions \(r\frac{l_a}{c_a}\), \(s\frac{c_a-u_a}{c_a}\), \(\frac{l_ap^k}{c_a}\) and \(t\frac{c_a-u_a}{c_a}\), \(\frac{c_a-b^ku_p^k}{c_a}\) to the envelope function. Constraints (22) to (25) describe, for \(k\in K\), \(p\in P^k\) and \(a\in A\) the feasible domain for variables \(x_p^k\) and _y<sub>a</sub>_ on which the convex envelopes of the delay functions are built.

From Proposition 3.5, one can observe that the DCMCF<sub>env</sub> problem can be formulated as a second-order cone program.

## 3.6 Computation of a tight domain

The DCMCF<sub>env</sub> relaxation relies on the bounds _l<sub>a</sub>_, _u<sub>a</sub>_ (lower and upper bounds of _y<sub>a</sub>_ for \(a\in A\)), \(u_p^k\) (upper bound of \(x_p^k\) for \(k\in K\), \(p\in P^k\)) and \(l_{ap}^k\) (lower-bound of \(y_a-b^kx_p^k\) for \(k\in K\), \(p\in P^k\) and \(a\in p\)).

As suggested in [4], explicit upper bounds for _y<sub>a</sub>_ can be computed by exploiting the observation that the load on each arc of the graph is induced by paths whose delays must satisfy some constraints. Therefore,<tbc>

