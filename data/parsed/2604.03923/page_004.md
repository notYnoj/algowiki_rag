<tbc>_Proof._ In Proposition 1, set \(\sigma=t_k^{1/\alpha}\) and \(\mathbf{x}=\tilde{\mathbf{x}}_k\). Then,

\(\|\mathbf{g}_k-\tilde{\mathbf{g}}_k\|_2=\left\|\frac{\mathrm{sin}(\alpha\pi)}{\alpha\pi}w_kA\left(t_k^{1/\alpha}\mathbf{I}+A\right)^{-1}\mathbf{b}-\frac{\mathrm{sin}(\alpha\pi)}{\alpha\pi}w_kA\tilde{\mathbf{x}}_k\right\|_2\le\frac{\mathrm{sin}(\alpha\pi)}{\alpha\pi}w_k\frac{1}{1+t_k^{1/\alpha}/\lambda_\mathrm{max}}\|\mathbf{r}_k\|_2.\)

By Equation (4), it suffices to enforce \(\|\mathbf{g}_k-\tilde{\mathbf{g}}_k\|_2\le\epsilon/(2m)\). A rearrangement of the terms yields Equation (8).

Corollary 1 implies that, when iteratively solving the shifted systems at each quadrature node, iterations may be terminated once the residual norm \(\|\mathbf{r}_k\|_2\) falls below the right-hand side of Equation (8). This constitutes the error control technique proposed in this paper.

A concrete example of the stopping criterion applied to each shift parameter when using the DE formula is shown in Figure 2. The stopping criterion is relaxed for both extremely large and extremely small shift parameters, and it becomes most stringent for intermediate shifts. This behavior reflects the fact that, in Equation (8), both the magnitude of the shift parameter \(t_k^{1/\alpha}\) and the quadrature weight _w<sub>k</sub>_ influence the stopping criterion.

## 3. Numerical Experiments

In this section, we verify that the proposed error-control technique enables the computation of \(A^\alpha\mathbf{b}\) to a prescribed accuracy level. All numerical experiments were performed using Python 3.13.1. Computations were performed on an HP EliteBook 630 13-inch G9 Notebook PC equipped with a 12th Gen Intel(R) Core(TM) i5-1235U (1.30 GHz) CPU and 32 GB RAM. Unless otherwise stated, IEEE double-precision floating-point arithmetic was used.

For the test matrices, we used finite-difference discretizations of the one-dimensional and two-dimensional Laplace operators, obtained from the three- and five-point centered difference stencils, respectively. The corresponding matrix sizes were _n_=1000 and _n_=1024. The right-hand side vector was chosen as \(\mathbf{b}=[1,\dots,1]^\top\).

We computed \(A^\alpha\) for \(\alpha=0.2\) and 0.5, with total error tolerances \(\epsilon=10^{-3},10^{-6}\) and 10<sup>-9</sup>. For the quadrature rules, we employed the GJ quadrature (GJ1 \[5, Eq. (2.6)\] and GJ2 \[4, Eq. (7)\]) and the DE formula \[6, Alg. 1\]. The number of quadrature nodes _m_ was determined from scalar quadrature error bounds, as done elsewhere \[6, 8\]. Specifically, for HPD matrices, the matrix error requirement was reduced to checking the scalar approximation error of \(\lambda^\alpha\) at an extremal eigenvalue (\(\lambda_\mathrm{max}\) or \(\lambda_\mathrm{min}\), depending on the theorem setting). We therefore chose the smallest _m_ such that the corresponding scalar error bound was below the quadrature error budget (here, \(\epsilon/2\)). The shifted linear systems at each quadrature node were solved by using the Shifted CG method. We used Equation (8), derived in Corollary 1, as the stopping criterion for each shifted system. Reference solutions were computed using the `fractional\_matrix\_power` function in the SciPy library.

Absolute errors \(\|A^\alpha\mathbf{b}-\sum_{k=1}^m\tilde{\mathbf{g}}_k\|_2\) computed for each test matrix and each value of \(\alpha\) are reported in Figure 3. For all the test matrices, all values of \(\alpha\), and all quadrature rules (GJ1, GJ2, and DE), the absolute errors remain below the prescribed error tolerance \(\epsilon\), thereby confirming the effectiveness of the per-node stopping criterion derived in Corollary 1.

10-3
10-6
Residual tolerance
10-9
E
1 + tk 1/a/Amax
2m sin(aπ)
Wk
10-12
1
10
20
30
40
50
Quadrature point index k

Figure 2: Stopping criterion for the shifted systems at the quadrature nodes derived from Corollary 1 (DE formula, \(\alpha=0.2\), \(\epsilon=10^{-9}\)). The vertical axis represents the admissible residual norm, and the horizontal axis the quadrature-node index _k_.

