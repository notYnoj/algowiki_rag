refer to the magnetic field and its variants hereafter:

\(\left\{\begin{array}{ c c } \nabla_\mathbf{k}\times(\varepsilon^{-1}\nabla_\mathbf{k}\times H)=\omega^2H, & \text{in}\Omega, \\ \nabla_\mathbf{k}\cdot H=\mathbf{0}, & \text{in}\Omega, \\ H(x+a_i)=H(x), & i=1,2,3.
\end{array}\right.\) (1.4)

This transformation is common in variational approaches [15] but is particularly advantageous for finite difference schemes, as the resulting simpler cyclic structure is crucial for implementing matrix-free operations.

The inverse permittivity \(\varepsilon^{-1}\) is a piecewise constant defined by

\(\varepsilon^{-1}(x)=\left\{\begin{array}{ c c } \varepsilon_1, & x\in\Omega_1, \\ I_3, & x\in\Omega_0:=\Omega\backslash\Omega_1, \end{array}\right.\) (1.5)

where \(\varepsilon_1\) is a \(3\times 3\) Hermitian positive definite (HPD) matrix. The media of the system (1.4) is classified as isotropic when \(\varepsilon_1\) is a scalar matrix, anisotropic when \(\varepsilon_1\) is a diagonal matrix with distinct entries or \(\varepsilon_1\) contains nonzero off-diagonal entries. This paper focuses on the behavior of the system with anisotropic media.

We present the kernel compensation formulation in our prior work [8] to handle the huge null space brought by \(\mathrm{ker}(\nabla_\mathbf{k}\times)\) as well as the divergence-free condition \(\nabla_\mathbf{k}\cdot H=\mathbf{0}\), which yields an HPD system with an efficient preconditioner. Our present focus is a novel discretization for \(\varepsilon^{-1}\) in (1.5) where nonzero entries of \(\varepsilon_1\) occur. Unlike finite element methods [2, 3, 14] or plane wave expansion methods [5, 18] which yield generalized eigenvalue problems, the finite difference framework, such as [6, 7], produces simpler eigenvalue problems and benefits from circulant matrix structures. Additionally, by applying a coordinate transform to the boundary conditions in (1.4), we align the periodicity with the standard R<sup>3</sup> basis, enabling highly efficient GPU acceleration.

In this paper, we overcome the limitations of solving the anisotropic system with finite difference method and present a corresponding robust, efficient eigensolver built upon the kernel compensation technique. We summarize the key innovations as follows:

\(\bullet\) We complete the theoretical foundation of the kernel compensation technique by rigorously demonstrating the exact structure of the null space and a detailed characterization of the penalty coefficient.

\(\bullet\) By using 3D discrete Fourier transform (DFT), we design matrix-free discrete differential operators, reducing the per-iteration cost of the eigensolver to a single 3D global DFT. Furthermore, we extend the Yee’s scheme to high-order discretizations under the framework of matrix-free operations, which improves the accuracy under certain cases.

\(\bullet\) We propose an innovative discretization concerning permittivity \(\varepsilon\) in anisotropic media, proving that the corresponding discrete matrix is HPD under physical constraints. This HPD property is essential for ensuring the correctness of the kernel compensation technique.

\(\bullet\) We present extensive numerical computations on various anisotropic systems and implement GPU acceleration on the whole process for high performance of large-scale simulations.

The paper is outlined as follows. Section 2 formally introduces the finite difference discretization process and the kernel compensation formulation. Section 3 details our innovative treatment of the anisotropic permittivity tensor and establishes the theoretical proof of the HPD property. Section 4 presents extensive numerical experiments, including band structure analysis and computational performance benchmarks. We conclude in Section 5.

## 2. Discretization and Kernel Compensation

In Subsection 2.1, we present Yee’s scheme [19] to discretize Maxwell’s equation with shifted nabla operator. Matrix representations of discrete differential operators are also provided. The results are generalized to arbitrary lattices \(\left\{a_i\right\}_{i=1}^3\) through coordinate transform, which is covered in Subsection 2.2. We then discuss the kernel compensation technique that eliminates the null space in Subsection 2.3. In Subsection 2.4, we imply matrix-free operations to replace sparse matrix-vector multiplication and design an efficient preconditioner. In Subsection 2.5, we introduce high-order finite difference stencils and extend previous results to high-order discretizations.

