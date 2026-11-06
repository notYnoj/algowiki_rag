approach to matrix-free operations via 3D DFT and extensions to high order discretizations. Numerical experiments on various lattice structures demonstrate practicality and efficiency, where an average speedup of more than 40\(\times\) is achieved on GPU. An ill-conditioned example also shows the robustness. Our future work will focus on extending this powerful framework to more complex, nonlinear eigenvalue problems in photonic crystals.

## References

LOBPCG: residuals damping history. 102 Trivial CrossDoF 100 10-2 Residuals log10 10-4 10-6 10-8 10-10 0
500 1000 1500 2000 2500 3000 3500 Iterations

**Figure 7:** Convergence history where \(\varepsilon_1\) is very ill-conditioned. Anisotropic SC-CURV lattice at \(\mathbf{k}=(\frac{1}{7},\frac{3}{5},\frac{4}{13})\pi\), grid division _N_=120.

