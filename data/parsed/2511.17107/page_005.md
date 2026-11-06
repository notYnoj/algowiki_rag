The assembling of the discrete permittivity matrix \(\mathcal{M}_\varepsilon\) will be covered in Section 3. In the rest of this section we assume that \(\mathcal{M}_\varepsilon\) is HPD.

## 2.2. Coordinate Transform

In Subsection 2.1, the periodic cell \(\Omega\) is assumed to be a unit cube. For general cases, the formulations (2.6) and (2.7) can be generalized for any linearly independent lattice vectors \(\{a_i\}_{i=1}^3\) through a simple coordinate transform. If we apply the following operation:

\(\text{Replace}H\text{in}(1.4)\text{by}(x\mapsto H(\text{\textbf{A}}x)),\text{\textbf{A}}=(a_1,a_2,a_3),\) (2.8)

then equation (1.4) can be equivalently written as

\(\left\{\begin{array}{ c } \nabla_{\text{\textbf{A}},\text{\textbf{k}}}\times\varepsilon^{-1}\nabla_{\text{\textbf{A}},\text{\textbf{k}}}\times H=\omega^2H,\text{in}(0,1)^3, \\ \nabla_{\text{\textbf{A}},\text{\textbf{k}}}\cdot H=0,\text{in}(0,1)^3, \\ H(x+e_i)=H(x),i=1,2,3, \end{array}\right.\) (2.9)

where \(\nabla_{\text{\textbf{A}},\text{\textbf{k}}}=\nabla_\text{\textbf{A}}+\text{i}\text{\textbf{k}}I\) and \(\nabla_\text{\textbf{A}}\) is given by

\(\nabla_\text{\textbf{A}}=\left(\sum_{j=1}^3b_{j1}\frac{\partial}{\partial x_j},\sum_{j=1}^3b_{j2}\frac{\partial}{\partial x_j},\sum_{j=1}^3b_{j3}\frac{\partial}{\partial x_j}\right)^\top,b_{ij}=(\text{\textbf{A}}^{-1})_{ij}.\) (2.10)

In this case we reformulate the matrix blocks in (2.6) as

\(\hat{D}_i=\sum_{j=1}^3b_{ji}D_{1,i}+\text{i}k_iD_{0,i},i=1,2,3.\) (2.11)

The matrices A and B preserve the structure in (2.7) by updating matrix blocks \(\hat{D}_i\). In summary, the discrete formulation of model problem (1.4) as well as (2.9) results in the system:

\(\left\{\begin{array}{ c } \left(\mathcal{A}\mathcal{M}_\varepsilon\mathcal{A}^\dagger\right)H_h=\omega_h^2H_h, \\ \mathcal{B}H_h=0. \end{array}\right.\) (2.12)

## 2.3. Kernel Compensation

Motivated by the mixed formulation of Maxwell’s equations [10], kernel compensation is introduced to find the nontrivial eigenpairs that satisfy the discrete divergence-free condition B_H<sub>h</sub>_=0 while avoiding the null space of A<sup>†</sup>, which is formulated as:

**The first several smallest positive eigenvalues of** \((\mathcal{A}\mathcal{M}_\varepsilon\mathcal{A}^\dagger+\gamma\mathcal{B}^\dagger\mathcal{B})H_h=\omega_h^2H_h\) **coincide with** (2.12) **when** \(\gamma>0\) **is sufficiently large.** (2.13)

Now, we come to prove the correctness of (2.13) with an explicit choice of the penalty coefficient \(\gamma\). For this aim, we first introduce the following lemma.

**Lemma 2.1.** _If_ \(\text{\textbf{C}}\in\mathbb{C}^{N\times N}\) _is a circulant matrix with the first row_ \((c_1,\cdots,c_N)\)_, then it can be diagonalized by the unitary DFT matrix_ **F** _as_

\(\text{\textbf{C}}=\text{Fdiag}(\lambda_1,\cdots,\lambda_N)\text{\textbf{F}}^\dagger,\lambda_i=\sum_{j=1}^Nc_j\omega^{(i-1)(j-1)},i=1,\cdots,N.\) (2.14)

