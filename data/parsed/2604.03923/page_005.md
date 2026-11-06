## 4. Conclusion

In this study, we analyzed the integrand evaluation error of quadrature-based algorithms used for computing \(A^\alpha\mathbf{b}\). We proposed a stopping criterion for iterative methods used for solving shifted linear systems in the integrand to keep the total error below a prescribed error tolerance.

The present results open several avenues for future work. First, we used a simple error allocation in which the quadrature discretization error and the integrand evaluation error were each controlled to be no greater than \(\epsilon/2\); optimizing the allocation between these two error sources may therefore reduce the computational cost. Second, while our analysis was restricted to the case where _A_ is Hermitian positive-definite, there is a need to extend the proposed error-control technique to more general matrices. Third, investigating the applicability of the proposed approach to other matrix functions beyond matrix real powers would open new possibilities. These functions would include the matrix sign function and functionals arising in applications, such as the von Neumann entropy.

## Acknowledgments

This work was supported by JSPS KAKENHI Grant Number 25H00449.

## References

1D Laplacian (a = 0.2)
1D Laplacian (a = 0.5)
10-3
10-3
GJ1
10-6
10-6
GJ2
DE
Absolute error |Aab - gll2
10-9
10-9
10-9
10-9
10-6
10-3
10-9
10-6
10-3
2D Laplacian (a = 0.2)
2D Laplacian (a = 0.5)
10-3
10-3
10-6
10-6
10-9
10-9
10-9
10-6
10-3
10-9
10-6
10-3
Tolerance E

Figure 3: Absolute errors of \(A^\alpha\mathbf{b}\) computed using quadrature-based algorithms. Left column: \(\alpha=0.2\); right column: \(\alpha=0.5\). Top row: one- dimensional Laplacian; bottom row: two-dimensional Laplacian. The horizontal axis represents the prescribed error tolerance \(\epsilon\), and the vertical axis the absolute error.

