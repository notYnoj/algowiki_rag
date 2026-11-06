_Proof._ The result follows directly from previous propositions.

Since \(\mathcal{A}\mathcal{M}_\varepsilon\mathcal{A}^\dagger+\gamma B^\dagger B=\mathcal{F}_3(\mathcal{K}_\mathcal{A}\mathcal{F}_3^\dagger\mathcal{M}_\varepsilon\mathcal{F}_3\mathcal{K}_\mathcal{A}^\dagger+\gamma\mathcal{K}_B)\mathcal{F}_3^\dagger\), by eliminating _F_<sub>3</sub> on both sides the kernel compensation formulation (2.13) is simplified into the equivalent system:

\(\left(\mathcal{K}_\mathcal{A}\mathcal{F}_3^\dagger\mathcal{M}_\varepsilon\mathcal{F}_3\mathcal{K}_\mathcal{A}^\dagger+\gamma\mathcal{K}_B\right)x=\omega_h^2x,x=\mathcal{F}_3^\dagger H_h.\) (2.30)

To construct an effective preconditioner, we consider an approximation by neglecting the middle term \(\mathcal{F}_3^\dagger\mathcal{M}_\varepsilon\mathcal{F}_3\). This yields the following matrix:

\(\mathcal{K}_P:=\mathcal{K}_\mathcal{A}\mathcal{K}_\mathcal{A}^\dagger+\gamma\mathcal{K}_B.\) (2.31)

Therefore, once we select an iterative algebraic eigensolver, a complete formulation of operations during each iteration is

\(\left\{\begin{array}{ c }
\text{Originalsystem:}\left(\mathcal{K}_\mathcal{A}\mathcal{F}_3^\dagger\mathcal{M}_\varepsilon\mathcal{F}_3\mathcal{K}_\mathcal{A}^\dagger+\gamma\mathcal{K}_B\right)x=\omega_h^2x, \\
\text{Preconditioning:}x\mapsto\mathcal{K}_P^{-1}x,\mathcal{K}_P=\mathcal{K}_\mathcal{A}\mathcal{K}_\mathcal{A}^\dagger+\gamma\mathcal{K}_B.
\end{array}\right.\) (2.32)

Crucially, the matrices K<sub>A</sub> and K_<sub>B</sub>_ are assembled using the diagonal matrices defined in (2.28) and (2.29). Since K<sub>P</sub> is a \(3\times 3\) block matrix where each block is diagonal, its inverse \(\mathcal{K}_P^{-1}\) can be trivially computed. Meanwhile, explicit construction of sparse matrices is unnecessary since manipulations of these K-matrices are reduced to piecewise vector multiplication, which significantly enhances GPU acceleration efficiency.

**Proposition 2.9.** _The condition number of the preconditioned system_ (2.32) _is bounded by the condition number of the permittivity matrix_ \(\mathcal{M}_\varepsilon\).

_Proof._ We consider the Rayleigh quotient \(\rho(\cdot)\) (\(\|\cdot\|_2\) is vector 2-norm):

\(\rho(x):=\frac{x^*\mathcal{K}_\mathcal{A}\hat{\mathcal{M}}\mathcal{K}_\mathcal{A}^\dagger x+\gamma\|\mathcal{K}_Bx\|_2^2}{\left\|\mathcal{K}_\mathcal{A}^\dagger x\right\|_2^2+\gamma\left\|\mathcal{K}_Bx\right\|_2^2},\hat{\mathcal{M}}=\mathcal{F}_3^\dagger\mathcal{M}_\varepsilon\mathcal{F}_3,\) (2.33)

where \(x\in\mathbb{C}^{3N^3}\) and superscript "∗" refers to vector conjugate transpose. Since _F_<sub>3</sub> is unitary, \(\hat{\mathcal{M}}\) has exactly the same spectrum as \(\mathcal{M}_\varepsilon\). The inequality

\(\lambda_{min}(\mathcal{M}_\varepsilon)\|y\|_2^2\le y^*\mathcal{M}_\varepsilon y\le\lambda_{max}(\mathcal{M}_\varepsilon)\|y\|_2^2\)

holds for any \(y\in\mathbb{C}^{3N^3}\), which implies the range of the Rayleigh quotient is bounded by the minimum and maximum eigenvalues of \(\mathcal{M}_\varepsilon\).

## 2.5. Matrix-free High-order Discretization

In the final part of this section, we investigate the design of high-order discretizations. Due to the discontinuity of the dielectric permittivity \(\varepsilon^{-1}\) at material interfaces, the magnetic field **_H_** generally does not possess high regularity. From a theoretical perspective, neither a high-order finite element scheme using adaptive mesh nor a high-order finite difference scheme is able to reach the desired convergence order. Nevertheless, a high-order discretization can still bring unexpected improvements in accuracy under certain cases.

To design high-order discretizations, we simply replace the first rows of **D**<sub>0</sub> and **D**<sub>1</sub> with the corresponding 1D symmetric finite difference stencils. While (2.5) corresponds to a second order stencil, for a general 2_m_-th order stencil,

