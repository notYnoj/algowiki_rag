## 6.1. Ehrhart enumeration.

For the nightrider we need more of the technique from Parts I-IV; thus we continue the exposition from Section 2. The board is the square board \[0,1\]<sup>2</sup>.

The _intersection lattice_ L(A<sub>P</sub>) is the lattice of all intersections of subsets of A<sub>P</sub>, ordered by reverse inclusion. The Möbius function of L(A<sub>P</sub>) is denoted by \(\mu\) and the bottom element is \(\hat{0}=\mathbb{R}^{2q}\). Each subspace \(\EuScript{U}\in\mathscr{L}(\mathscr{A}_\mathbb{P})\) is the intersection of hyperplanes involving a set _I_ consisting of \(\kappa\) of the _q_ pieces. The _essential part_ of U is the subspace \(\widetilde{\EuScript{U}}\) of \(\mathbb{R}^{2\kappa}\) that satisfies the same move equations as U. Then \(\alpha(\EuScript{U};n)\), defined as the number of integral points in the dilation of \((\EuScript{B}^\circ)^\kappa\cap\widetilde{\EuScript{U}}\), is independent of _q_ because \(\widetilde{\EuScript{U}}\) depends only on \(\kappa\). By Ehrhart theory \(\alpha(\EuScript{U};n)\) is a quasipolynomial of degree \(2\kappa-\mathrm{codim}\widetilde{\EuScript{U}}\). Since \(\EuScript{U}\cong\mathbb{R}^{2(q-\kappa)}\times\widetilde{\EuScript{U}}\), \(\mathrm{codim}\widetilde{\EuScript{U}}=\mathrm{codim}\EuScript{U}\) and the number of lattice points in \(\EuScript{U}\cap(0,1)^{2q}\) is \(n^{2(q-\kappa)}\alpha(\EuScript{U};n)\). To get _o_<sub>P</sub>(_q;n_) we use Möbius inversion to combine these numbers:

\(o_\mathbb{P}(q;n)=\sum_{\EuScript{U}\in\mathscr{L}(\mathscr{A}_\mathbb{P})}\mu(\hat{0},\EuScript{U})n^{2(q-\kappa)}\alpha(\EuScript{U};n).\)

This is justified by the Ehrhart theory of inside-out polytopes because the nonattacking configurations are the integral lattice points in (_n_+1)(0,1)<sup>2_q_</sup> and not in any of the hyperplanes \(\EuScript{H}_{ij}^{d/c}\).

In Part II we defined \(\alpha^{d/c}(n):=\alpha(\EuScript{H}_{12}^{d/c};n)\), the number of ordered pairs of positions that attack each other along slope _d/c_ (they may occupy the same position; that is considered attacking). Similarly, \(\beta^{d/c}(n):=\alpha(\EuScript{H}_{12}^{d/c}\cap\EuScript{H}_{13}^{d/c};n)\), the number of ordered triples that are collinear along slope _d/c_. Proposition II.3.1 gives general formulas for \(\alpha\) and \(\beta\). We need only two examples:

\(\alpha^{1/2}(n)=\left\{\begin{array}{ c c }
\frac{5}{12}n^3+\frac{1}{3}n & \text{for}n\text{even,} \\
\frac{5}{12}n^3+\frac{7}{12}n & \text{for}n\text{odd}
\end{array}\right.=\frac{5}{12}n^3+\frac{11}{24}n-(-1)^n\left\{\frac{1}{8}n\right\},\beta^{1/2}(n)=\left\{\begin{array}{ c c }
\frac{3}{16}n^4+\frac{1}{4}n^2 & \text{for}n\text{even,} \\
\frac{3}{16}n^4+\frac{5}{8}n^2+\frac{3}{16} & \text{for}n\text{odd.}
\end{array}\right.=\frac{3}{16}n^4+\frac{7}{16}n^2+\frac{3}{32}-(-1)^n\left\{\frac{3}{16}n^2+\frac{3}{32}\right\}.\text{(6.1)}\)

## 6.2. Strong Parity Theorem.

The Parity Theorem (Theorem II.4.1) tells us that \(\alpha(\EuScript{U};n)\) is an even or odd function of _n_, depending on the codimension of U. What it does not say is how that affects the number of undetermined coefficients in computing \(\alpha(\EuScript{U};n)\), which is, in particular, the number of values of the function we need to interpolate all the coefficients. In general, an Ehrhart quasipolynomial of degree _d_ with period _p_ has _pd_+1 coefficients that have to be computed. (The leading coefficient is the volume of \(\EuScript{U}\cap[0,1]^{2q}\) for all constituents.) The full theorem, then, should be this:

**Theorem 6.1** (Strong Parity Theorem)**.** _For a subspace_ \(\EuScript{U}\in\mathscr{L}(\mathscr{A}_\mathbb{P})\) _whose equations involve_ \(\kappa\) _pieces, for which_ \(\alpha(\EuScript{U};n)\) _has period p, the number of values of_ \(\alpha(\EuScript{U};n)\) _that are sufficient_

