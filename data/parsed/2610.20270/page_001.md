Benign Degeneracy for First-Order Methods in Exact Boolean Moment–SOS Relaxations

Shucheng Kang

School of Engineering and Applied Sciences, Harvard University

`skang1@g.harvard.edu`

**Abstract**

Pseudo-Boolean optimization--minimizing a polynomial over \(\{\pm 1\}^n\)--includes MAX- CUT, binary quadratic optimization, and Ising models. The moment--sum-of-squares (Moment–SOS) hierarchy provides certified semidefinite relaxations that are often empirically exact at low order. We ask: once a relaxation is exact, how difficult is the resulting semidefinite program (SDP) to solve with first-order methods?

Exactness does not imply regularity. At every order \(d\ge 2\), a unique rank-one moment optimum is primal degenerate; moreover, if one optimal SOS certificate is strictly complementary, then the certificate set is positive-dimensional and contains singular boundary points. Thus first-order methods may converge to such singular points, around which pointwise analyses that assume regularity at the limit cannot establish a local linear convergence rate.

We show that, for exact Boolean Moment–SOS relaxations in their canonical quotient form, this degeneracy is nevertheless benign. We develop an abstract mechanism, which we call _residual-field rigidity_, that propagates regularity from the relative interior of the optimal set to its singular boundary. It requires neither the primal nor the dual optimal solution to be unique, and it is equivalent to the first-order stall directions of the residual coinciding with the tangent directions of the optimal set. For Boolean Moment–SOS, unique rank-one exactness and the existence of one strictly complementary certificate suffice to trigger this mechanism, yielding a uniform error bound around the entire optimal set. Consequently, ADMM, sGS–ADMM, and PDHG converge eventually linearly from every initialization, even when their limiting certificate is singular. Finally, outside a lower-dimensional semialgebraic exceptional set of Boolean objectives, these hypotheses hold simultaneously at every uniquely rank-one exact order.

