<tbc>in the tables), the convergence rates may fall short of expectations, which is attributed to the limited mesh resolution or the poor regularity of the eigenfunctions.

To verify the accuracy of the high-order stencils, we construct a test case where the dielectric coefficient \(\varepsilon\) is smooth with respect to **_x_**:

\(\varepsilon(x,y,z)=8.9sin(2\pi(x+y+z))+13.\) (4.7)

5 presents the convergence results for the first eight eigenvalues, computed using a 10th-order finite difference stencil with _m_=5 at the wave vector \(\mathbf{k}=(\pi,\pi,\pi)\). As shown in the table, the high-order finite difference stencils successfully achieve the theoretical convergence rate when the coefficients are smooth. Similar results hold for stencils of orders 2, 4, 6, and 8: these results are omitted here for simplicity.

## 4.3. Computational Performance

In  6 we present iteration counts required to achieve convergence for the types of PCs discussed in Subsection 4.1. To be precise, we compute both the average and the standard deviation of iterations at different **k**’s, showing the numbers don’t vary too much. More iterations are required when computing anisotropic system than that of computing isotropic system with same lattice type and tolerance. Specifically, \(\mathcal{M}_\varepsilon=\mathcal{M}_\text{CrossDoF}\) requires fewer iterations than \(\mathcal{M}_\varepsilon=\mathcal{M}_\text{Trivial}\).

Next, we provide a quantitative measure of performance enhancement brought by GPU acceleration. The linear algebra operations are done by NumPy and CuPy packages on CPU and GPU, respectively. From  7, we observe that GPU acceleration achieves an average speedup of over 40 times.

## 4.4. Robustness under Extreme Cases

We construct an ill-conditioned \(\varepsilon_1\) as \(\varepsilon_1=U\text{diag}(10^{-1},10^{-3},10^{-5})U^\dagger\), where _U_ is a randomly generated unitary matrix. Under the setting of SC-CURV lattice, the system is computed with both \(\mathcal{M}_\varepsilon=\mathcal{M}_\text{Trivial}\) and \(\mathcal{M}_\varepsilon=\mathcal{M}_\text{CrossDoF}\).<tbc>

\begin{tabular}{ccccc}
**Eigenvalue** & **Absolute** & **Difference** & \(|\omega_h^2-\omega_{2h}^2|\) & **Average** \\
**Index** & _h_=1/32 & _h_=1/64 & _h_=1/128 & **Order** \\
1 & 2.58e-02 & 7.70e-03 & 2.64e-03 & 1.64 \\
2 & 3.09e-02 & 1.10e-02 & 3.43e-03 & 1.59 \\
3 & 1.65e-02 & 1.89e-02 & 8.63e-03 & 0.47 \\
4 & 9.54e-03 & 1.62e-02 & 1.02e-02 & -0.05 \\
5 & 4.71e-02 & 1.45e-02 & 4.85e-03 & 1.64 \\
6 & 3.15e-02 & 2.10e-02 & 7.67e-03 & 1.02 \\
7 & 3.85e-02 & 2.06e-02 & 6.66e-03 & 1.27 \\
8 & 5.69e-02 & 2.10e-02 & 5.73e-03 & 1.66 \\
\end{tabular}

\begin{tabular}{ccccc}
**Eigenvalue** & **Absolute** & **Difference** & \(|\omega_h^2-\omega_{2h}^2|\) & **Average** \\
**Index** & _h_=1/32 & _h_=1/64 & _h_=1/128 & **Order** \\
1 & 2.90e-02 & 8.21e-03 & 2.90e-03 & 1.66 \\
2 & 3.31e-02 & 1.21e-02 & 3.81e-03 & 1.56 \\
3 & 1.91e-02 & 2.30e-02 & 1.08e-02 & 0.41 \\
4 & 1.39e-02 & 1.58e-02 & 1.27e-02 & 0.06 \\
5 & 5.01e-02 & 2.16e-02 & 6.28e-03 & 1.50 \\
6 & 4.01e-02 & 2.59e-02 & 9.60e-03 & 1.03 \\
7 & 5.10e-02 & 2.43e-02 & 8.81e-03 & 1.27 \\
8 & 7.02e-02 & 2.55e-02 & 6.14e-03 & 1.76 \\
\end{tabular}

** 3**<br>
BCC-SG lattice in anisotropic media with wave number vector \(\mathbf{k}=(\pi,\pi,\pi)\), convergence analysis of the first 8 eigenvalues, M=M<sub>Trivial</sub>.

** 4**<br>
BCC-SG lattice in anisotropic media with wave number vector \(\mathbf{k}=(\pi,\pi,\pi)\), convergence analysis of the first 8 eigenvalues, M=M<sub>CrossDoF</sub>.

